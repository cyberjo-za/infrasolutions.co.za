#!/usr/bin/env python3
"""Delete photo messages found in Telegram updates for a channel or chat.

Usage:
  python src/delete_channel_images.py --token <BOT_TOKEN> [--chat-id CHAT_ID] [--dry-run]

Notes:
- This script scans updates returned by `getUpdates` and deletes messages that contain a `photo` field.
- If your bot is used elsewhere (another poller), `getUpdates` may be empty. Consider running as the sole poller or use Cloudflare worker/KV to track messages.
"""
import argparse
import httpx
import os
import sys


API_BASE = "https://api.telegram.org/bot{token}/{method}"


def parse_args():
    p = argparse.ArgumentParser(description="Delete Telegram photo messages found in getUpdates")
    p.add_argument("--token", help="Telegram bot token (or set TELEGRAM_TOKEN env)")
    p.add_argument("--chat-id", help="Optional chat_id or channel username to restrict deletions")
    p.add_argument("--dry-run", action="store_true", help="Don't actually delete, just print what would be deleted")
    return p.parse_args()


def get_updates(client, token, offset=None, timeout=10):
    url = API_BASE.format(token=token, method="getUpdates")
    params = {}
    if offset:
        params["offset"] = offset
    r = client.get(url, params=params, timeout=timeout)
    r.raise_for_status()
    return r.json().get("result", [])


def delete_message(client, token, chat_id, message_id):
    url = API_BASE.format(token=token, method="deleteMessage")
    r = client.post(url, params={"chat_id": chat_id, "message_id": message_id})
    return r


def main():
    args = parse_args()
    token = args.token or os.environ.get("TELEGRAM_TOKEN") or os.environ.get("TOKEN")
    if not token:
        print("Error: Telegram token is required via --token or TELEGRAM_TOKEN env", file=sys.stderr)
        sys.exit(1)

    client = httpx.Client()
    offset = None
    found_any = False

    print("Scanning updates for photo messages...")
    while True:
        updates = get_updates(client, token, offset=offset)
        if not updates:
            break

        for item in updates:
            offset = max(offset or 0, item.get("update_id", 0) + 1)
            msg = item.get("channel_post") or item.get("message") or {}
            if "photo" not in msg:
                continue

            chat = msg.get("chat", {})
            chat_id = chat.get("id")
            message_id = msg.get("message_id")
            if args.chat_id and str(args.chat_id) != str(chat_id):
                print(f"Skipping photo in chat {chat_id} (restricted to {args.chat_id})")
                continue

            found_any = True
            if args.dry_run:
                print(f"DRY-RUN: Would delete message {message_id} in chat {chat_id}")
                continue

            try:
                res = delete_message(client, token, chat_id, message_id)
                if res.status_code == 200 and res.json().get("ok"):
                    print(f"Deleted message {message_id} in chat {chat_id}")
                else:
                    print(f"Failed to delete message {message_id} in chat {chat_id}: {res.status_code} {res.text}")
            except Exception as e:
                print(f"Error deleting message {message_id} in chat {chat_id}: {e}")

    if not found_any:
        print("No photo messages found in the available updates.")
    else:
        print("Done.")


if __name__ == "__main__":
    main()

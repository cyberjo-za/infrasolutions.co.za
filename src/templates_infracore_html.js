export default `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Infracore Solutions – Security & Smart Home Experts, Johannesburg</title>
<link href="https://fonts.googleapis.com/css2?family=Rajdhani:wght@400;500;600;700&family=Exo+2:wght@300;400;500;600&family=Share+Tech+Mono&display=swap" rel="stylesheet">
<style>
:root {
	--cyan: #00e5ff;
	--blue: #1565ff;
	--purple: #9c27ff;
	--pink: #e040fb;
	--dark: #04050f;
	--dark2: #080c1a;
	--dark3: #0d1229;
	--white: #f0f4ff;
	--muted: #8899bb;
	--card-bg: rgba(13,18,41,0.85);
	--border: rgba(0,229,255,0.15);
	--glow-cyan: 0 0 20px rgba(0,229,255,0.4);
	--glow-purple: 0 0 20px rgba(156,39,255,0.4);
}
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }
body {
	background: var(--dark);
	color: var(--white);
	font-family: 'Exo 2', sans-serif;
	font-weight: 400;
	line-height: 1.6;
	overflow-x: hidden;
}
body::before {
	content: '';
	position: fixed;
	inset: 0;
	background-image:
		linear-gradient(rgba(0,229,255,0.04) 1px, transparent 1px),
		linear-gradient(90deg, rgba(0,229,255,0.04) 1px, transparent 1px);
	background-size: 60px 60px;
	pointer-events: none;
	z-index: 0;
}
nav {
	position: fixed;
	top: 0; left: 0; right: 0;
	z-index: 100;
	display: flex;
	align-items: center;
	justify-content: space-between;
	padding: 1rem 4%;
	background: rgba(4,5,15,0.92);
	backdrop-filter: blur(12px);
	border-bottom: 1px solid var(--border);
}
.nav-logo {
	font-family: 'Rajdhani', sans-serif;
	font-weight: 700;
	font-size: 1.5rem;
	letter-spacing: 0.1em;
	background: linear-gradient(90deg, var(--cyan), var(--purple));
	-webkit-background-clip: text;
	-webkit-text-fill-color: transparent;
	background-clip: text;
	text-decoration: none;
}
.nav-links { display: flex; gap: 2rem; list-style: none; }
.nav-links a {
	color: var(--muted);
	text-decoration: none;
	font-size: 0.85rem;
	font-weight: 500;
	letter-spacing: 0.12em;
	text-transform: uppercase;
	transition: color 0.3s;
}
.nav-links a:hover { color: var(--cyan); }
.nav-cta {
	background: linear-gradient(135deg, var(--blue), var(--purple));
	color: #fff !important;
	padding: 0.5rem 1.3rem;
	border-radius: 4px;
	font-size: 0.8rem !important;
	letter-spacing: 0.15em;
	transition: box-shadow 0.3s !important;
}
.nav-cta:hover { box-shadow: var(--glow-purple) !important; }
#hero {
	position: relative;
	min-height: 100vh;
	display: flex;
	align-items: center;
	justify-content: center;
	text-align: center;
	padding: 8rem 6% 5rem;
	overflow: hidden;
}
.hero-orb {
	position: absolute;
	border-radius: 50%;
	filter: blur(80px);
	pointer-events: none;
	animation: pulse 6s ease-in-out infinite;
}
.orb1 { width: 500px; height: 500px; background: radial-gradient(circle, rgba(0,229,255,0.18), transparent 70%); top: -100px; left: -100px; }
.orb2 { width: 400px; height: 400px; background: radial-gradient(circle, rgba(156,39,255,0.2), transparent 70%); bottom: -80px; right: -80px; animation-delay: -3s; }
.orb3 { width: 300px; height: 300px; background: radial-gradient(circle, rgba(224,64,251,0.12), transparent 70%); top: 50%; left: 55%; animation-delay: -1.5s; }
@keyframes pulse { 0%, 100% { transform: scale(1); opacity: 1; } 50% { transform: scale(1.15); opacity: 0.7; } }
.hero-badge {
	display: inline-flex;
	align-items: center;
	gap: 0.5rem;
	border: 1px solid rgba(0,229,255,0.3);
	border-radius: 100px;
	padding: 0.35rem 1rem;
	font-family: 'Share Tech Mono', monospace;
	font-size: 0.72rem;
	color: var(--cyan);
	letter-spacing: 0.15em;
	margin-bottom: 1.8rem;
	background: rgba(0,229,255,0.05);
	animation: fadeDown 0.8s ease both;
}
.badge-dot { width: 6px; height: 6px; border-radius: 50%; background: var(--cyan); box-shadow: 0 0 8px var(--cyan); animation: blink 1.5s ease infinite; }
@keyframes blink { 0%,100% { opacity: 1; } 50% { opacity: 0.2; } }
.hero-headline {
	font-family: 'Rajdhani', sans-serif;
	font-weight: 700;
	font-size: clamp(2.8rem, 7vw, 5.5rem);
	line-height: 1.05;
	letter-spacing: 0.02em;
	margin-bottom: 1.2rem;
	animation: fadeUp 0.8s 0.15s ease both;
}
.hero-headline .grad {
	background: linear-gradient(90deg, var(--cyan) 0%, var(--purple) 50%, var(--pink) 100%);
	-webkit-background-clip: text;
	-webkit-text-fill-color: transparent;
	background-clip: text;
}
.hero-sub {
	font-size: 1.1rem;
	color: var(--muted);
	max-width: 600px;
	margin: 0 auto 2.5rem;
	font-weight: 300;
	animation: fadeUp 0.8s 0.3s ease both;
}
.hero-actions {
	display: flex;
	gap: 1rem;
	justify-content: center;
	flex-wrap: wrap;
	animation: fadeUp 0.8s 0.45s ease both;
}
.btn-primary {
	background: linear-gradient(135deg, var(--blue), var(--purple));
	color: #fff;
	padding: 0.9rem 2.2rem;
	border-radius: 4px;
	text-decoration: none;
	font-family: 'Rajdhani', sans-serif;
	font-size: 1rem;
	font-weight: 600;
	letter-spacing: 0.12em;
	text-transform: uppercase;
	transition: box-shadow 0.3s, transform 0.2s;
}
.btn-primary:hover { box-shadow: 0 0 30px rgba(101,21,255,0.5); transform: translateY(-2px); }
.btn-outline {
	border: 1px solid var(--cyan);
	color: var(--cyan);
	padding: 0.9rem 2.2rem;
	border-radius: 4px;
	text-decoration: none;
	font-family: 'Rajdhani', sans-serif;
	font-size: 1rem;
	font-weight: 600;
	letter-spacing: 0.12em;
	text-transform: uppercase;
	transition: background 0.3s, box-shadow 0.3s, transform 0.2s;
}
.btn-outline:hover { background: rgba(0,229,255,0.08); box-shadow: var(--glow-cyan); transform: translateY(-2px); }
.hero-trust {
	display: flex;
	justify-content: center;
	gap: 2rem;
	flex-wrap: wrap;
	margin-top: 3.5rem;
	animation: fadeUp 0.8s 0.6s ease both;
}
.trust-item {
	display: flex;
	align-items: center;
	gap: 0.5rem;
	font-family: 'Share Tech Mono', monospace;
	font-size: 0.72rem;
	color: var(--muted);
	letter-spacing: 0.08em;
}
@keyframes fadeUp { from { opacity: 0; transform: translateY(24px); } to { opacity: 1; transform: translateY(0); } }
@keyframes fadeDown { from { opacity: 0; transform: translateY(-16px); } to { opacity: 1; transform: translateY(0); } }
section {
	position: relative;
	z-index: 1;
	padding: 6rem 6%;
}
.section-label {
	font-family: 'Share Tech Mono', monospace;
	font-size: 0.72rem;
	color: var(--cyan);
	letter-spacing: 0.2em;
	text-transform: uppercase;
	margin-bottom: 0.8rem;
}
.section-title {
	font-family: 'Rajdhani', sans-serif;
	font-weight: 700;
	font-size: clamp(2rem, 4vw, 3rem);
	line-height: 1.1;
	letter-spacing: 0.02em;
}
.section-title .accent {
	background: linear-gradient(90deg, var(--cyan), var(--purple));
	-webkit-background-clip: text;
	-webkit-text-fill-color: transparent;
	background-clip: text;
}
.section-desc { color: var(--muted); font-size: 1rem; font-weight: 300; max-width: 520px; margin-top: 0.8rem; }
#services { background: var(--dark2); }
.services-header { max-width: 1100px; margin: 0 auto 3.5rem; }
.services-grid {
	max-width: 1100px;
	margin: 0 auto;
	display: grid;
	grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
	gap: 1.5px;
	border: 1px solid var(--border);
	border-radius: 8px;
	overflow: hidden;
}
.service-card {
	background: var(--card-bg);
	padding: 2.2rem 2rem;
	position: relative;
	overflow: hidden;
	transition: background 0.35s;
	cursor: default;
}
.service-card::before {
	content: '';
	position: absolute;
	top: 0; left: 0; right: 0;
	height: 2px;
	background: linear-gradient(90deg, var(--blue), var(--purple), var(--pink));
	transform: scaleX(0);
	transform-origin: left;
	transition: transform 0.4s ease;
}
.service-card:hover { background: rgba(21,28,60,0.95); }
.service-card:hover::before { transform: scaleX(1); }
.service-icon { font-size: 2.2rem; margin-bottom: 1rem; display: block; }
.service-card h3 {
	font-family: 'Rajdhani', sans-serif;
	font-weight: 700;
	font-size: 1.25rem;
	letter-spacing: 0.06em;
	text-transform: uppercase;
	margin-bottom: 0.6rem;
	color: var(--white);
}
.service-card p { color: var(--muted); font-size: 0.9rem; line-height: 1.7; font-weight: 300; }
.service-tag {
	display: inline-block;
	margin-top: 1rem;
	font-family: 'Share Tech Mono', monospace;
	font-size: 0.65rem;
	color: var(--cyan);
	border: 1px solid rgba(0,229,255,0.25);
	padding: 0.2rem 0.6rem;
	border-radius: 3px;
	letter-spacing: 0.1em;
}
#why { background: var(--dark); }
.why-inner {
	max-width: 1100px;
	margin: 0 auto;
	display: grid;
	grid-template-columns: 1fr 1fr;
	gap: 5rem;
	align-items: center;
}
.why-visual { position: relative; display: flex; align-items: center; justify-content: center; }
.eye-container { position: relative; width: 300px; height: 300px; display: flex; align-items: center; justify-content: center; }
.eye-ring {
	position: absolute;
	border-radius: 50%;
	border: 1px solid;
	animation: spin-slow linear infinite;
}
.ring1 { width: 280px; height: 280px; border-color: rgba(0,229,255,0.3); animation-duration: 20s; }
.ring2 { width: 220px; height: 220px; border-color: rgba(156,39,255,0.3); animation-duration: 15s; animation-direction: reverse; }
.ring3 { width: 160px; height: 160px; border-color: rgba(224,64,251,0.25); animation-duration: 10s; }
@keyframes spin-slow { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
.eye-center { position: relative; z-index: 2; font-size: 3.5rem; filter: drop-shadow(0 0 20px var(--cyan)); }
.eye-ring::after {
	content: '';
	position: absolute;
	width: 8px; height: 8px;
	border-radius: 50%;
	background: var(--cyan);
	top: 0; left: 50%;
	transform: translateX(-50%);
	box-shadow: 0 0 10px var(--cyan);
}
.ring2::after { background: var(--purple); box-shadow: 0 0 10px var(--purple); }
.ring3::after { background: var(--pink); box-shadow: 0 0 10px var(--pink); }
.why-points { display: flex; flex-direction: column; gap: 1.5rem; }
.why-point {
	display: flex;
	gap: 1rem;
	align-items: flex-start;
	padding: 1.2rem 1.5rem;
	border: 1px solid var(--border);
	border-radius: 6px;
	background: var(--card-bg);
	transition: border-color 0.3s, box-shadow 0.3s;
}
.why-point:hover { border-color: rgba(0,229,255,0.35); box-shadow: var(--glow-cyan); }
.point-icon { font-size: 1.4rem; flex-shrink: 0; margin-top: 0.1rem; }
.point-text h4 {
	font-family: 'Rajdhani', sans-serif;
	font-weight: 700;
	font-size: 1rem;
	letter-spacing: 0.08em;
	text-transform: uppercase;
	margin-bottom: 0.2rem;
}
.point-text p { color: var(--muted); font-size: 0.85rem; font-weight: 300; }
#compliance {
	position: relative;
	z-index: 1;
	padding: 3rem 6%;
	background: linear-gradient(90deg, rgba(21,101,255,0.15), rgba(156,39,255,0.15));
	border-top: 1px solid rgba(0,229,255,0.12);
	border-bottom: 1px solid rgba(0,229,255,0.12);
}
.compliance-inner {
	max-width: 1100px;
	margin: 0 auto;
	display: flex;
	align-items: center;
	justify-content: space-between;
	flex-wrap: wrap;
	gap: 2rem;
}
.compliance-text h3 { font-family: 'Rajdhani', sans-serif; font-weight: 700; font-size: 1.5rem; letter-spacing: 0.05em; }
.compliance-text p { color: var(--muted); font-size: 0.9rem; margin-top: 0.3rem; max-width: 450px; }
.cert-badges { display: flex; gap: 1rem; flex-wrap: wrap; }
.cert-badge {
	border: 1px solid var(--cyan);
	border-radius: 6px;
	padding: 0.7rem 1.3rem;
	font-family: 'Share Tech Mono', monospace;
	font-size: 0.78rem;
	color: var(--cyan);
	letter-spacing: 0.12em;
	background: rgba(0,229,255,0.06);
	box-shadow: var(--glow-cyan);
	text-align: center;
}
.cert-badge span { display: block; font-size: 0.6rem; color: var(--muted); letter-spacing: 0.08em; margin-top: 0.2rem; }
#process { background: var(--dark2); }
.process-header { max-width: 1100px; margin: 0 auto 3rem; text-align: center; }
.process-header .section-desc { margin: 0.8rem auto 0; }
.process-steps {
	max-width: 1100px;
	margin: 0 auto;
	display: grid;
	grid-template-columns: repeat(4, 1fr);
	gap: 0;
	position: relative;
}
.process-steps::before {
	content: '';
	position: absolute;
	top: 2.5rem;
	left: 12.5%;
	right: 12.5%;
	height: 1px;
	background: linear-gradient(90deg, var(--blue), var(--purple), var(--pink));
	z-index: 0;
}
.step { text-align: center; padding: 0 1.5rem; position: relative; z-index: 1; }
.step-num {
	width: 5rem;
	height: 5rem;
	border-radius: 50%;
	border: 1px solid var(--border);`;

TEMPLATE = r"""<!DOCTYPE html>
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
  border: 1px solid var(--border);
  background: var(--dark2);
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 1.2rem;
  font-family: 'Rajdhani', sans-serif;
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--cyan);
  position: relative;
}
.step-num::after {
  content: '';
  position: absolute;
  inset: -4px;
  border-radius: 50%;
  border: 1px solid rgba(0,229,255,0.2);
}
.step h4 { font-family: 'Rajdhani', sans-serif; font-weight: 700; font-size: 0.95rem; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 0.5rem; }
.step p { color: var(--muted); font-size: 0.82rem; font-weight: 300; line-height: 1.6; }
#coverage { background: var(--dark); }
.coverage-inner {
  max-width: 1100px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4rem;
  align-items: center;
}
.coverage-map {
  background: var(--card-bg);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 2.5rem 2rem;
  text-align: center;
  position: relative;
  overflow: hidden;
}
.coverage-map::before {
  content: '';
  position: absolute;
  inset: 0;
  background-image:
    linear-gradient(rgba(0,229,255,0.06) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0,229,255,0.06) 1px, transparent 1px);
  background-size: 30px 30px;
}
.map-icon { font-size: 4rem; position: relative; z-index: 1; filter: drop-shadow(0 0 20px var(--cyan)); display: block; margin-bottom: 1rem; }
.coverage-map h3 {
  position: relative; z-index: 1;
  font-family: 'Rajdhani', sans-serif; font-weight: 700; font-size: 1.3rem; letter-spacing: 0.06em;
  background: linear-gradient(90deg, var(--cyan), var(--purple));
  -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
}
.coverage-map p { position: relative; z-index: 1; color: var(--muted); font-size: 0.85rem; margin-top: 0.5rem; }
.coverage-areas { display: flex; flex-wrap: wrap; gap: 0.5rem; margin-top: 1rem; position: relative; z-index: 1; justify-content: center; }
.area-tag {
  font-family: 'Share Tech Mono', monospace;
  font-size: 0.65rem;
  color: var(--cyan);
  border: 1px solid rgba(0,229,255,0.2);
  padding: 0.25rem 0.6rem;
  border-radius: 3px;
  background: rgba(0,229,255,0.04);
}
#contact { background: var(--dark2); }
.contact-inner {
  max-width: 1100px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4rem;
  align-items: start;
}
.contact-cards { display: flex; flex-direction: column; gap: 1rem; margin-top: 2rem; }
.contact-card {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem 1.3rem;
  border: 1px solid var(--border);
  border-radius: 6px;
  background: var(--card-bg);
  text-decoration: none;
  transition: border-color 0.3s, box-shadow 0.3s;
}
.contact-card:hover { border-color: rgba(0,229,255,0.4); box-shadow: var(--glow-cyan); }
.cc-icon { font-size: 1.3rem; }
.cc-label { font-family: 'Share Tech Mono', monospace; font-size: 0.65rem; color: var(--muted); letter-spacing: 0.1em; display: block; }
.cc-value { font-family: 'Rajdhani', sans-serif; font-weight: 600; font-size: 1rem; color: var(--white); }
.contact-form {
  background: var(--card-bg);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 2rem;
}
.contact-form h3 { font-family: 'Rajdhani', sans-serif; font-weight: 700; font-size: 1.3rem; letter-spacing: 0.06em; margin-bottom: 1.5rem; text-transform: uppercase; }
.form-group { margin-bottom: 1.2rem; }
.form-group label { display: block; font-family: 'Share Tech Mono', monospace; font-size: 0.68rem; color: var(--muted); letter-spacing: 0.12em; margin-bottom: 0.4rem; text-transform: uppercase; }
.form-group input, .form-group select, .form-group textarea {
  width: 100%;
  background: rgba(4,5,15,0.6);
  border: 1px solid var(--border);
  border-radius: 4px;
  color: var(--white);
  font-family: 'Exo 2', sans-serif;
  font-size: 0.9rem;
  padding: 0.7rem 1rem;
  outline: none;
  transition: border-color 0.3s, box-shadow 0.3s;
  -webkit-appearance: none;
}
.form-group select option { background: var(--dark2); }
.form-group input:focus, .form-group select:focus, .form-group textarea:focus {
  border-color: var(--cyan);
  box-shadow: 0 0 0 2px rgba(0,229,255,0.12);
}
.form-group textarea { resize: vertical; min-height: 90px; }
.form-submit {
  width: 100%;
  background: linear-gradient(135deg, var(--blue), var(--purple));
  color: #fff;
  border: none;
  border-radius: 4px;
  padding: 0.9rem;
  font-family: 'Rajdhani', sans-serif;
  font-weight: 700;
  font-size: 1rem;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  cursor: pointer;
  transition: box-shadow 0.3s, transform 0.2s;
  margin-top: 0.5rem;
}
.form-submit:hover { box-shadow: 0 0 30px rgba(101,21,255,0.5); transform: translateY(-1px); }
footer {
  background: var(--dark);
  border-top: 1px solid var(--border);
  padding: 2.5rem 6%;
  position: relative;
  z-index: 1;
}
.footer-inner {
  max-width: 1100px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 1rem;
}
.footer-logo {
  font-family: 'Rajdhani', sans-serif;
  font-weight: 700;
  font-size: 1.3rem;
  letter-spacing: 0.1em;
  background: linear-gradient(90deg, var(--cyan), var(--purple));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
.footer-copy { color: var(--muted); font-size: 0.78rem; font-family: 'Share Tech Mono', monospace; letter-spacing: 0.06em; }
.footer-links { display: flex; gap: 1.5rem; list-style: none; }
.footer-links a { color: var(--muted); text-decoration: none; font-size: 0.8rem; transition: color 0.3s; }
.footer-links a:hover { color: var(--cyan); }
.reveal { opacity: 0; transform: translateY(30px); transition: opacity 0.7s ease, transform 0.7s ease; }
.reveal.visible { opacity: 1; transform: none; }
.toast {
  display: none;
  position: fixed;
  bottom: 2rem; right: 2rem;
  background: linear-gradient(135deg, var(--blue), var(--purple));
  color: #fff;
  padding: 1rem 1.5rem;
  border-radius: 6px;
  font-family: 'Rajdhani', sans-serif;
  font-weight: 600;
  letter-spacing: 0.08em;
  z-index: 999;
  box-shadow: 0 8px 30px rgba(0,0,0,0.4);
}
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: var(--dark); }
::-webkit-scrollbar-thumb { background: linear-gradient(var(--blue), var(--purple)); border-radius: 2px; }
@media (max-width: 768px) {
  nav { padding: 1rem 4%; }
  .nav-links { display: none; }
  #hero { padding: 7rem 5% 4rem; }
  .hero-trust { gap: 1rem; }
  .services-grid { grid-template-columns: 1fr; }
  .why-inner, .coverage-inner, .contact-inner { grid-template-columns: 1fr; gap: 2rem; }
  .eye-container { width: 220px; height: 220px; }
  .ring1 { width: 200px; height: 200px; } .ring2 { width: 155px; height: 155px; } .ring3 { width: 110px; height: 110px; }
  .process-steps { grid-template-columns: 1fr 1fr; gap: 2rem; }
  .process-steps::before { display: none; }
  .compliance-inner { flex-direction: column; }
  .footer-inner { flex-direction: column; text-align: center; }
  section { padding: 4rem 5%; }
}
@media (max-width: 480px) { .process-steps { grid-template-columns: 1fr; } }
</style>
</head>
<body>

<nav>
  <a href="#" class="nav-logo">INFRACORE</a>
  <ul class="nav-links">
    <li><a href="#services">Services</a></li>
    <li><a href="#why">Why Us</a></li>
    <li><a href="#process">Process</a></li>
    <li><a href="#coverage">Coverage</a></li>
    <li><a href="#contact" class="nav-cta">Get a Quote</a></li>
  </ul>
</nav>

<section id="hero">
  <div class="hero-orb orb1"></div>
  <div class="hero-orb orb2"></div>
  <div class="hero-orb orb3"></div>
  <div style="position:relative; z-index:1;">
    <div class="hero-badge">
      <span class="badge-dot"></span>
      SANS COMPLIANT &bull; CERTIFIED INSTALLERS &bull; JOHANNESBURG SOUTH
    </div>
    <h1 class="hero-headline">
      Securing What<br>Matters <span class="grad">Most to You</span>
    </h1>
    <p class="hero-sub">
      Professional CCTV, fibre, gate motor, smart home &amp; electric fencing installations for residential and commercial properties across Johannesburg &mdash; backed by relevant certifications and full SANS compliance.
    </p>
    <div class="hero-actions">
      <a href="#contact" class="btn-primary">Get a Free Quote</a>
      <a href="#services" class="btn-outline">Our Services</a>
    </div>
    <div class="hero-trust">
      <div class="trust-item"><span>🛡️</span>&nbsp;SANS Compliant</div>
      <div class="trust-item"><span>📋</span>&nbsp;Fully Certified</div>
      <div class="trust-item"><span>⚡</span>&nbsp;Fast Response</div>
      <div class="trust-item"><span>🏠</span>&nbsp;Residential &amp; Commercial</div>
    </div>
  </div>
</section>

<section id="services">
  <div class="services-header reveal">
    <div class="section-label">// What We Install</div>
    <h2 class="section-title">Integrated <span class="accent">Security Solutions</span></h2>
    <p class="section-desc">End-to-end installation and support &mdash; from perimeter security to full smart home automation.</p>
  </div>
  <div class="services-grid reveal">
    <div class="service-card">
      <span class="service-icon">📷</span>
      <h3>CCTV Systems</h3>
      <p>HD and IP camera systems for 24/7 property surveillance. Remote viewing, motion alerts, and cloud storage options for homes and businesses.</p>
      <span class="service-tag">RESIDENTIAL &amp; COMMERCIAL</span>
    </div>
    <div class="service-card">
      <span class="service-icon">🌐</span>
      <h3>Fibre Installation</h3>
      <p>Structured fibre-optic cabling for ultra-fast, reliable connectivity. FTTH, LAN and backbone installations to keep you connected at full speed.</p>
      <span class="service-tag">HIGH-SPEED CONNECTIVITY</span>
    </div>
    <div class="service-card">
      <span class="service-icon">🚪</span>
      <h3>Gate Motor Installation</h3>
      <p>Sliding and swing gate motors from leading brands, including intercoms, access control and remote management for ultimate convenience and security.</p>
      <span class="service-tag">ACCESS CONTROL</span>
    </div>
    <div class="service-card">
      <span class="service-icon">🏡</span>
      <h3>Smart Home Systems</h3>
      <p>Automate lighting, climate, security and entertainment. Centralised control via smartphone or voice command &mdash; your home, intelligently connected.</p>
      <span class="service-tag">HOME AUTOMATION</span>
    </div>
    <div class="service-card">
      <span class="service-icon">⚡</span>
      <h3>Electric Fencing</h3>
      <p>SANS 10222-compliant electric fence installations and energiser setups. Effective perimeter protection for residential estates and commercial properties.</p>
      <span class="service-tag">PERIMETER SECURITY</span>
    </div>
    <div class="service-card" style="display:flex;flex-direction:column;justify-content:center;background:linear-gradient(135deg,rgba(21,101,255,0.12),rgba(156,39,255,0.12));">
      <span class="service-icon">🔧</span>
      <h3>Maintenance &amp; Support</h3>
      <p>Ongoing maintenance contracts, fault-finding, upgrades and emergency call-outs. We service what we install &mdash; and everything else too.</p>
      <span class="service-tag">ONGOING SUPPORT</span>
    </div>
  </div>
</section>

<!-- Latest offers / notices gallery -->
<section id="offers" style="background:var(--dark2);">
  <div class="services-header reveal">
    <div class="section-label">// Latest Offers &amp; Notices</div>
    <h2 class="section-title">Our <span class="accent">Latest Work</span> &amp; Offers</h2>
    <p class="section-desc">Browse our latest installations, projects, and special offers. Click any image to view it full-size.</p>
  </div>
  <div style="max-width:1100px;margin:0 auto;padding:1.5rem;">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:1rem;">
      <div style="color:var(--muted);font-family:'Share Tech Mono',monospace;font-size:0.85rem;">Recent projects &amp; notices</div>
      <button id="offers-refresh" class="btn-outline">Refresh</button>
    </div>
    <div id="offers-grid" style="display:grid;grid-template-columns:repeat(3,1fr);gap:12px;">
      <!-- images injected here -->
    </div>
  </div>
  <div id="offer-modal" style="display:none;position:fixed;inset:0;z-index:9999;background:rgba(0,0,0,0.92);justify-content:center;align-items:center;cursor:zoom-out;">
    <button id="modal-close" style="position:fixed;top:1.5rem;right:2rem;background:none;border:none;color:#fff;font-size:2.5rem;cursor:pointer;z-index:10000;line-height:1;">&times;</button>
    <img id="modal-img" style="max-width:92vw;max-height:92vh;object-fit:contain;border-radius:8px;box-shadow:0 0 40px rgba(0,0,0,0.6);">
  </div>
  <style>
    .offer-img-wrapper {
      background: var(--card-bg);
      border-radius: 8px;
      border: 1px solid var(--border);
      overflow: hidden;
      cursor: pointer;
      transition: border-color 0.3s, box-shadow 0.3s;
    }
    .offer-img-wrapper:hover {
      border-color: var(--cyan);
      box-shadow: var(--glow-cyan);
    }
    .offer-img-wrapper img {
      display: block;
      width: 100%;
      aspect-ratio: 3 / 2;
      object-fit: contain;
      background: var(--dark3);
      pointer-events: none;
    }
  </style>
  <script>
    function openModal(src) {
      const modal = document.getElementById('offer-modal');
      document.getElementById('modal-img').src = src;
      modal.style.display = 'flex';
      document.body.style.overflow = 'hidden';
    }
    function closeModal() {
      const modal = document.getElementById('offer-modal');
      modal.style.display = 'none';
      document.body.style.overflow = '';
    }
    document.getElementById('modal-close').addEventListener('click', closeModal);
    document.getElementById('offer-modal').addEventListener('click', function(e) {
      if (e.target === this) closeModal();
    });
    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape') closeModal();
    });

    async function loadOffers(){
      try{
        const res = await fetch('/api/photos');
        if(!res.ok) throw new Error('Failed');
        const data = await res.json();
        const grid = document.getElementById('offers-grid');
        if(!data.photos || data.photos.length===0){
          grid.innerHTML = '<div style="color:var(--muted);padding:1rem;">No recent offers found.</div>';
          return;
        }
        grid.innerHTML = data.photos.slice(0,6).map(u=>`<div class="offer-img-wrapper" onclick="openModal('${u}')"><img src="${u}" alt="" loading="lazy"></div>`).join('');
      }catch(e){
        console.error(e);
      }
    }
    document.getElementById('offers-refresh').addEventListener('click', loadOffers);
    document.addEventListener('DOMContentLoaded', loadOffers);
  </script>
</section>

<div id="compliance">
  <div class="compliance-inner reveal">
    <div class="compliance-text">
      <h3>Certified. Compliant. Trusted.</h3>
      <p>We hold all relevant industry certifications and operate in full compliance with South African National Standards (SANS). When you choose Infracore, you choose accountability.</p>
    </div>
    <div class="cert-badges">
      <div class="cert-badge">SANS 10222<span>Electric Fencing</span></div>
      <div class="cert-badge">PSIRA<span>Registered</span></div>
      <div class="cert-badge">CETA<span>Accredited</span></div>
      <div class="cert-badge">SAIDSA<span>Member</span></div>
    </div>
  </div>
</div>

<section id="why">
  <div class="why-inner">
    <div class="why-visual reveal">
      <div class="eye-container">
        <div class="eye-ring ring1"></div>
        <div class="eye-ring ring2"></div>
        <div class="eye-ring ring3"></div>
        <div class="eye-center">🔒</div>
      </div>
    </div>
    <div>
      <div class="section-label reveal">// Why Choose Infracore</div>
      <h2 class="section-title reveal">The <span class="accent">Difference</span><br>Is in the Detail</h2>
      <div class="why-points" style="margin-top:2rem;">
        <div class="why-point reveal">
          <div class="point-icon">📜</div>
          <div class="point-text">
            <h4>Certified &amp; SANS Compliant</h4>
            <p>Every installation meets South African National Standards. We hold the certifications to prove it &mdash; not every installer does.</p>
          </div>
        </div>
        <div class="why-point reveal">
          <div class="point-icon">🏆</div>
          <div class="point-text">
            <h4>Experienced Technicians</h4>
            <p>Our team brings years of hands-on experience across residential complexes, estates, commercial buildings and retail properties.</p>
          </div>
        </div>
        <div class="why-point reveal">
          <div class="point-icon">⚙️</div>
          <div class="point-text">
            <h4>Quality Equipment Only</h4>
            <p>We install from reputable brands with manufacturer warranties &mdash; no grey-market hardware, no shortcuts.</p>
          </div>
        </div>
        <div class="why-point reveal">
          <div class="point-icon">📞</div>
          <div class="point-text">
            <h4>Post-Installation Support</h4>
            <p>We don't disappear after the job is done. Maintenance contracts and rapid support keep your systems running optimally.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section id="process">
  <div class="process-header reveal">
    <div class="section-label">// How It Works</div>
    <h2 class="section-title">Simple. <span class="accent">Seamless.</span> Professional.</h2>
    <p class="section-desc">From first contact to final sign-off &mdash; a clear, hassle-free process every time.</p>
  </div>
  <div class="process-steps reveal">
    <div class="step">
      <div class="step-num">01</div>
      <h4>Consultation</h4>
      <p>Tell us your needs. We assess your property and recommend the right solutions &mdash; no overselling, just honest advice.</p>
    </div>
    <div class="step">
      <div class="step-num">02</div>
      <h4>Custom Quote</h4>
      <p>Receive a detailed, transparent quotation. No hidden costs, no surprises. We explain every line item.</p>
    </div>
    <div class="step">
      <div class="step-num">03</div>
      <h4>Installation</h4>
      <p>Our certified technicians complete the job neatly and efficiently &mdash; on time, every time.</p>
    </div>
    <div class="step">
      <div class="step-num">04</div>
      <h4>Handover &amp; Support</h4>
      <p>Full system walkthrough, documentation and ongoing support. You're never left in the dark.</p>
    </div>
  </div>
</section>

<section id="coverage">
  <div class="coverage-inner">
    <div>
      <div class="section-label reveal">// Service Area</div>
      <h2 class="section-title reveal">Based in <span class="accent">Johannesburg South</span></h2>
      <p class="section-desc reveal">Infracore Solutions is headquartered in Bassonia and serves a wide footprint across Johannesburg South and surrounding areas.</p>
      <div class="why-points" style="margin-top:2rem;">
        <div class="why-point reveal">
          <div class="point-icon">📍</div>
          <div class="point-text">
            <h4>Our Address</h4>
            <p>Bassonia, Johannesburg South, 2061<br>Gauteng, South Africa</p>
          </div>
        </div>
        <div class="why-point reveal">
          <div class="point-icon">🚗</div>
          <div class="point-text">
            <h4>We Come to You</h4>
            <p>On-site visits across Johannesburg South, Glenvista, Mulbarton, Meyersdal, Alberton and beyond.</p>
          </div>
        </div>
      </div>
    </div>
    <div class="coverage-map reveal">
      <span class="map-icon">🗺️</span>
      <h3>Johannesburg South</h3>
      <p>Serving residential estates, complexes &amp; commercial properties</p>
      <div class="coverage-areas">
        <span class="area-tag">Bassonia</span>
        <span class="area-tag">Glenvista</span>
        <span class="area-tag">Mulbarton</span>
        <span class="area-tag">Alberton</span>
        <span class="area-tag">Meyersdal</span>
        <span class="area-tag">Aspen Hills</span>
        <span class="area-tag">Ormonde</span>
        <span class="area-tag">Roseacre</span>
        <span class="area-tag">Lenasia</span>
        <span class="area-tag">Eldorado Park</span>
        <span class="area-tag">JHB CBD</span>
        <span class="area-tag">+ Surrounding Areas</span>
      </div>
    </div>
  </div>
</section>

<section id="contact">
  <div class="contact-inner">
    <div>
      <div class="section-label reveal">// Get In Touch</div>
      <h2 class="section-title reveal">Request Your<br><span class="accent">Free Quote</span></h2>
      <p class="section-desc reveal">Ready to secure your property? Contact us today for a no-obligation consultation and quotation.</p>
      <div class="contact-cards reveal">
        <a href="tel:+27603520517" class="contact-card">
          <span class="cc-icon">📞</span>
          <div>
            <span class="cc-label">Call Us</span>
            <span class="cc-value">+27 60 352 0517</span>
          </div>
        </a>
        <a href="https://wa.me/27603520517" target="_blank" rel="noopener" class="contact-card">
          <span class="cc-icon">
            <svg viewBox="0 0 24 24" width="20" height="20" fill="#25D366" style="display:block;">
              <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/>
            </svg>
          </span>
          <div>
            <span class="cc-label">WhatsApp</span>
            <span class="cc-value">+27 60 352 0517</span>
          </div>
        </a>
        <a href="mailto:info@infrasolutions.co.za" class="contact-card">
          <span class="cc-icon">✉️</span>
          <div>
            <span class="cc-label">Email Us</span>
            <span class="cc-value">info@infrasolutions.co.za</span>
          </div>
        </a>
        <a href="#" class="contact-card">
          <span class="cc-icon">📍</span>
          <div>
            <span class="cc-label">Location</span>
            <span class="cc-value">Bassonia, Johannesburg South, 2061</span>
          </div>
        </a>
      </div>
    </div>
  </div>
</section>

<footer>
  <div class="footer-inner">
    <span class="footer-logo">INFRACORE SOLUTIONS</span>
    <ul class="footer-links">
      <li><a href="#services">Services</a></li>
      <li><a href="#why">About</a></li>
      <li><a href="#contact">Contact</a></li>
    </ul>
    <span class="footer-copy">&copy; 2026 Infracore Solutions &middot; Bassonia, JHB South &middot; SANS Compliant</span>
  </div>
</footer>

<div class="toast" id="toast">✅ Message sent! We'll be in touch shortly.</div>

<script>
const reveals = document.querySelectorAll('.reveal');
const observer = new IntersectionObserver((entries) => {
  entries.forEach((e, i) => {
    if (e.isIntersecting) {
      setTimeout(() => e.target.classList.add('visible'), i * 80);
    }
  });
}, { threshold: 0.12, rootMargin: '0px 0px -50px 0px' });
reveals.forEach(el => observer.observe(el));

function handleSubmit() {
  const toast = document.getElementById('toast');
  toast.style.display = 'block';
  setTimeout(() => toast.style.display = 'none', 4000);
}

const sections = document.querySelectorAll('section[id], div[id]');
const navLinks = document.querySelectorAll('.nav-links a');
window.addEventListener('scroll', () => {
  let current = '';
  sections.forEach(s => { if (window.scrollY >= s.offsetTop - 120) current = s.id; });
  navLinks.forEach(a => {
    a.style.color = a.getAttribute('href') === '#' + current ? 'var(--cyan)' : '';
  });
});
</script>
</body>
</html>"""

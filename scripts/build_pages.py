#!/usr/bin/env python3
"""Generates roadmap.html, certifications.html, calendar.html, journey.html,
writeups.html and skills.html by wrapping page-specific content in the exact
same nav / mobile-menu / side-panel / footer markup already used on index.html,
so every page feels like the same site rather than a bolt-on."""

import os

ROOT = os.path.dirname(os.path.abspath(__file__))

NAV_ITEMS = [
    ("about.html#about", "About"),
    ("projects.html#projects", "Projects"),
    ("writeups.html", "Write-ups"),
    ("roadmap.html", "Roadmap"),
    ("certifications.html", "Certifications"),
    ("calendar.html", "Calendar"),
    ("journey.html", "Journey"),
    ("contact.html#contact", "Contact"),
]
# Homepage sections still live on index.html; point those nav entries there.
HOME_SECTIONS = {"about.html#about": "index.html#about", "projects.html#projects": "index.html#projects", "contact.html#contact": "index.html#contact"}

def nav_html(active_href):
    links = []
    for href, label in NAV_ITEMS:
        real_href = HOME_SECTIONS.get(href, href)
        cls = ' class="active"' if href == active_href else ''
        links.append(f'    <li><a href="{real_href}"{cls}>{label}</a></li>')
    return "\n".join(links)

def mobile_links_html(active_href):
    links = []
    idx = 1
    for href, label in NAV_ITEMS:
        real_href = HOME_SECTIONS.get(href, href)
        links.append(f'      <a href="{real_href}" class="mobile-menu-link" data-index="{idx:02d}">{label}</a>')
        idx += 1
    return "\n".join(links)

def page(title, description, og_title, og_description, canonical, active_href, body_sections, extra_head=""):
    nav = nav_html(active_href)
    mobile = mobile_links_html(active_href)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="author" content="Mojalefa L. Letsoara">
<meta name="robots" content="index, follow">

<meta property="og:type" content="website">
<meta property="og:title" content="{og_title}">
<meta property="og:description" content="{og_description}">
<meta property="og:url" content="https://justjeff211.github.io/{canonical}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{og_title}">
<meta name="twitter:description" content="{og_description}">

<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Crect width='24' height='24' rx='5' fill='%23070B12'/%3E%3Cpath d='M12 4 5 7v5c0 4.4 3 8.3 7 9 4-.7 7-4.6 7-9V7l-7-3Z' fill='none' stroke='%2338BDF8' stroke-width='1.6'/%3E%3C/svg%3E">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@200;300;400;500;600;700&display=swap" rel="stylesheet">

<link rel="stylesheet" href="css/style.css">
<link rel="stylesheet" href="css/extra.css">
<link rel="stylesheet" href="css/roadmap.css">
{extra_head}</head>
<body>

<div class="atmosphere" aria-hidden="true"></div>
<div class="grain" aria-hidden="true" style="background-image:url(&quot;data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='200'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='3'/%3E%3C/filter%3E%3Crect width='200' height='200' filter='url(%23n)'/%3E%3C/svg%3E&quot;)"></div>

<nav class="top-nav" id="top">
  <a href="index.html" class="nav-brand">Mojalefa<span>Letsoara</span></a>

  <ul class="nav-links">
{nav}
  </ul>

  <div class="nav-utils">
    <button class="theme-toggle" data-theme-toggle aria-label="Toggle colour theme" aria-pressed="false">
      <svg class="icon-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>
      <svg class="icon-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M20 14.5A8.5 8.5 0 1 1 9.5 4a7 7 0 0 0 10.5 10.5Z"/></svg>
    </button>

    <a href="assets/cv/Mojalefa-Letsoara-CV.pdf" class="nav-cta" download>Download CV</a>

    <button class="nav-toggle" aria-label="Open menu" aria-expanded="false">
      <span class="toggle-bar"></span>
      <span class="toggle-bar"></span>
    </button>
  </div>
</nav>

<div class="mobile-menu">
  <div class="mobile-menu-inner">
    <div class="mobile-menu-links">
{mobile}
    </div>
    <div class="mobile-menu-footer">
      <a href="https://www.linkedin.com/in/mojalefa-l-letsoara283b5a211/" target="_blank" rel="noopener">LinkedIn</a>
      <a href="https://github.com/Justjeff211" target="_blank" rel="noopener">GitHub</a>
      <a href="https://www.tiktok.com/@justjeff211" target="_blank" rel="noopener">TikTok</a>
      <button class="theme-toggle" data-theme-toggle aria-label="Toggle colour theme" aria-pressed="false">
        <svg class="icon-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>
        <svg class="icon-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M20 14.5A8.5 8.5 0 1 1 9.5 4a7 7 0 0 0 10.5 10.5Z"/></svg>
      </button>
    </div>
  </div>
</div>

{body_sections}

<section class="footer-cta">
  <div class="main">
    <div class="reveal">
      <div class="section-tag" style="text-align:center;">Get in touch</div>
      <h2 class="section-title" style="text-align:center;">Let's put this to work in your <strong>SOC or cloud team</strong></h2>
      <p class="section-body" style="margin:0 auto;text-align:center;">
        I'm actively pursuing SOC Analyst and cloud security roles where I can bring this same
        build, monitor, investigate, document approach to a real production environment.
      </p>
      <div class="footer-ctas">
        <a href="assets/cv/Mojalefa-Letsoara-CV.pdf" class="btn-primary" download>Download CV</a>
        <a href="index.html#contact" class="btn-secondary">Send a Message</a>
      </div>
    </div>

    <div style="margin:64px 0 56px;"><div class="silk-divider"></div></div>

    <div class="footer-bar">
      <div class="footer-brand">Mojalefa L. Letsoara</div>
      <div class="footer-links">
        <a href="https://www.linkedin.com/in/mojalefa-l-letsoara283b5a211/" target="_blank" rel="noopener">LinkedIn</a>
        <a href="https://github.com/Justjeff211" target="_blank" rel="noopener">GitHub</a>
        <a href="https://www.tiktok.com/@justjeff211" target="_blank" rel="noopener">TikTok</a>
      </div>
      <div class="footer-credit">&copy; <span data-current-year>2026</span> Mojalefa L. Letsoara &middot; Last updated <span data-last-updated="2026-09-19"></span></div>
    </div>
  </div>
</section>

<a href="index.html#contact" class="sticky-cta" data-sticky-cta>
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M20 7 9 18l-5-5"/></svg>
  <span>Open to SOC & Cloud Security Roles</span>
</a>

<button class="back-to-top" aria-label="Back to top" data-back-to-top>
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 19V5M5 12l7-7 7 7"/></svg>
</button>

<script src="js/main.js"></script>
<script src="js/roadmap.js"></script>
</body>
</html>
"""

if __name__ == "__main__":
    print("template module loaded OK")

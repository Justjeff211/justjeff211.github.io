#!/usr/bin/env python3
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_pages import page

def role_card(title, org, dates, current_label, bullets):
    lis = "".join(bullets)
    badge = f'<span class="status-pill in-progress">{current_label}</span>' if current_label else ""
    return f"""      <div class="dash-card reveal" style="max-width:none;">
        <div style="display:flex;align-items:flex-start;justify-content:space-between;gap:12px;margin-bottom:6px;">
          <div>
            <div style="font-size:1rem;font-weight:500;color:var(--ivory);">{title}</div>
            <div style="font-size:0.8rem;color:var(--slate-light);margin-top:2px;">{org}</div>
          </div>
          {badge}
        </div>
        <div style="font-size:0.72rem;color:var(--slate-warm);letter-spacing:0.06em;text-transform:uppercase;margin-bottom:16px;">{dates}</div>
        <ul class="bullet-grid-2">{lis}</ul>
      </div>"""

BULLET = 'style="font-size:0.78rem;font-weight:300;color:var(--ivory-muted);padding-left:14px;position:relative;"'

def li(text):
    return f'<li {BULLET}>{text}</li>'

it_bullets = [li(x) for x in [
    "Windows support", "Hardware &amp; software troubleshooting", "Endpoint support",
    "Connectivity troubleshooting", "Switches &amp; access points", "Wireless networking",
    "Structured cabling", "POS systems", "Printers &amp; biometric systems", "CCTV &amp; surveillance",
    "NAS &amp; shared network resources", "System builds &amp; provisioning", "Repairs &amp; preventative maintenance",
    "Event Viewer &amp; System Monitor", "Antivirus &amp; endpoint security", "Technical documentation",
]]

radio_bullets = [li(x) for x in [
    "Windows workstations", "Software support", "Studio infrastructure", "Installations &amp; configuration",
    "Maintenance &amp; upgrades", "Technical troubleshooting", "User-facing support", "Technical communication",
]]

hacking_hub_bullets = [li(x) for x in [
    "Structured Blue Team training: threat detection, incident response", "SIEM operations &amp; malware analysis",
    "Consistently documenting findings for the community", "First community member outside the founder to complete the Immersive Labs pathway",
]]

journey_body = f"""
<header class="page-hero">
  <div class="main">
    <div class="page-hero-tag reveal">Career Journey</div>
    <h1 class="reveal reveal-d1">Systems and endpoints, <strong>then security</strong>.</h1>
    <p class="page-hero-sub reveal reveal-d2">
      My path into cybersecurity started with systems, endpoints, networks and users, not a
      classroom. Working IT support raised the questions that pulled me toward security: what
      happens when a system is compromised, what evidence does an attacker leave, how should an
      alert actually be investigated. This page separates where that foundation came from
      (professional and volunteer roles) from the hands-on security work I've built since (labs,
      projects and write-ups).
    </p>
  </div>
</header>

<section class="section" id="experience" style="padding-top:0;">
  <div class="main">
    <div class="section-center reveal">
      <div class="section-tag">Professional Experience</div>
      <h2 class="section-title">Where the <strong>foundation</strong> came from</h2>
    </div>

    <div class="dash-grid" style="grid-template-columns:1fr;gap:20px;margin-top:40px;">
{role_card("IT Support Technician", "Tfsgroupfs", "May 2025 to Present", "Current", it_bullets)}
{role_card("Volunteer Cybersecurity Analyst, Blue Team Training", "Hacking Hub (Volunteer)", "October 2025 to Present", "Current", hacking_hub_bullets)}
{role_card("Radio Host &amp; Technical Support", "Q-lit Radio Station", "February 2020 to February 2022", None, radio_bullets)}
    </div>

    <p class="metrics-note" style="margin-top:32px;">
      Tfsgroupfs is paid, employed work. Hacking Hub is volunteer training, unpaid, alongside it.
      The labs, investigations and write-ups elsewhere on this site are hands-on project work I've
      built myself, not a claim of professional security industry experience. I keep all three
      clearly separate rather than blur them together.
    </p>
  </div>
</section>

<section class="section" id="career-timeline">
  <div class="main">
    <div class="section-center reveal">
      <div class="section-tag">How It Connects</div>
      <h2 class="section-title">From IT support to <strong>SOC-focused work</strong></h2>
    </div>

    <div class="career-line">
      <div class="career-step done reveal">
        <div class="career-step-label">Feb 2020 to Feb 2022</div>
        <h3>IT Support Foundation</h3>
        <p>Radio Host and Technical Support at Q-lit Radio Station: Windows workstations, studio infrastructure, installations, troubleshooting and user-facing technical communication.</p>
      </div>
      <div class="career-step done reveal reveal-d1">
        <div class="career-step-label">May 2025 to Present</div>
        <h3>IT Support Technician</h3>
        <p>Endpoint support, networking, security hardening and user support at Tfsgroupfs, the professional base this whole direction builds on.</p>
      </div>
      <div class="career-step done reveal reveal-d2">
        <div class="career-step-label">Oct 2025 to Present</div>
        <h3>Blue Team Volunteering</h3>
        <p>Started structured Blue Team training with Hacking Hub: threat detection, incident response, SIEM operations and malware analysis, alongside the day job.</p>
      </div>
      <div class="career-step done reveal reveal-d3">
        <div class="career-step-label">Oct to Dec 2025</div>
        <h3>Cybersecurity Foundations</h3>
        <p>Cyber Security 101 and Pre Security (TryHackMe), plus Cisco's Junior Cybersecurity Analyst Career Path, completed December 2025.</p>
      </div>
      <div class="career-step done reveal">
        <div class="career-step-label">Mar to Jul 2026</div>
        <h3>Certifications</h3>
        <p>AZ-900 and SC-900 in March, Security+, CySA+ and AI Skills Fest in June, SC-200 in July. Nine certifications completed inside the same window.</p>
      </div>
      <div class="career-step done reveal reveal-d1">
        <div class="career-step-label">Jul 2026 onward</div>
        <h3>Labs, Projects &amp; Write-ups</h3>
        <p>Enterprise SOC Portfolio, the Conti ransomware investigation, Splunk log analysis and the account-takeover case study, turning certification knowledge into evidence.</p>
      </div>
      <div class="career-step current reveal reveal-d2">
        <div class="career-step-label">Now</div>
        <h3>Current Development</h3>
        <p>AZ-104 retake and SC-500 preparation, studied side by side ahead of back-to-back exams in October.</p>
      </div>
      <div class="career-step reveal reveal-d3">
        <div class="career-step-label">Dec 2026+</div>
        <h3>Next Chapter</h3>
        <p>AI-901, then an open-ended stage of deeper SOC, Microsoft Security and Azure Security development, guided by my mentor as it unfolds.</p>
      </div>
      <div class="career-step reveal reveal-d2">
        <div class="career-step-label">2027</div>
        <h3>Four Certifications, In Priority Order</h3>
        <p>01 Blue Team Level 1, 02 CompTIA SecurityX, 03 AWS Certified Security &ndash; Specialty, 04 HashiCorp Certified: Terraform Associate. Full detail on the <a href="certifications.html" style="color:var(--cyan);">Certifications</a> page.</p>
      </div>
    </div>
  </div>
</section>
"""

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "journey.html"), "w") as f:
    f.write(page(
        title="Career Journey | Mojalefa L. Letsoara",
        description="From IT support and volunteer Blue Team training to certifications, labs and SOC-focused project work, clearly separating professional and volunteer experience from hands-on security projects.",
        og_title="Career Journey | Mojalefa L. Letsoara",
        og_description="Systems and endpoints, then security: how professional and volunteer experience connects to certifications, labs and write-ups.",
        canonical="journey.html",
        active_href="journey.html",
        body_sections=journey_body,
    ))

print("journey.html written")

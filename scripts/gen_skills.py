#!/usr/bin/env python3
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_pages import page

def chip(name, level):
    return f'<span class="skill-chip">{name} <span class="lvl">{level}</span></span>'

def group(title, chips):
    return f"""    <div class="skills-group reveal">
      <div class="skills-group-title">{title}</div>
      <div class="skills-row">{"".join(chips)}</div>
    </div>"""

skills_body = f"""
<header class="page-hero">
  <div class="main">
    <div class="page-hero-tag reveal">Skills</div>
    <h1 class="reveal reveal-d1">What I can actually <strong>do</strong>.</h1>
    <p class="page-hero-sub reveal reveal-d2">
      No invented percentages. Each skill is labelled by how I've actually used it: hands-on in a
      real lab or write-up, developing through current work, or familiar from study and exposure.
    </p>
  </div>
</header>

<section class="section" id="skills-list" style="padding-top:0;">
  <div class="main">
{group("Security Operations", [
    chip("SOC Operations", "Hands-on"), chip("SIEM", "Hands-on"), chip("Alert Triage", "Hands-on"),
    chip("Incident Response", "Hands-on"), chip("Threat Hunting", "Developing"),
    chip("Detection Engineering", "Hands-on"), chip("Security Monitoring", "Hands-on"),
])}
{group("Microsoft Security", [
    chip("Microsoft Sentinel", "Hands-on"), chip("Microsoft Defender XDR", "Developing"),
    chip("Microsoft Defender for Endpoint", "Familiar"), chip("Microsoft Defender for Cloud", "Familiar"),
    chip("Microsoft Entra ID", "Developing"), chip("KQL", "Hands-on"), chip("Azure Monitor", "Developing"),
])}
{group("Threat &amp; Investigation", [
    chip("MITRE ATT&amp;CK", "Hands-on"), chip("Threat Intelligence", "Developing"),
    chip("IOC Analysis", "Hands-on"), chip("Malware Analysis", "Developing"),
    chip("Log Analysis", "Hands-on"), chip("CVE Research", "Developing"), chip("CVSS", "Familiar"),
])}
{group("Networking", [
    chip("TCP/IP", "Hands-on"), chip("OSI", "Hands-on"), chip("Subnetting", "Hands-on"),
    chip("VLANs", "Familiar"), chip("Inter-VLAN Routing", "Familiar"), chip("Firewalls", "Hands-on"),
    chip("IDS/IPS", "Developing"), chip("NAC", "Familiar"), chip("Wireless Networking", "Hands-on"),
])}
{group("Cloud", [
    chip("Microsoft Azure", "Hands-on"), chip("Cloud Security", "Developing"),
    chip("Identity Security", "Developing"), chip("Governance", "Familiar"),
    chip("Monitoring", "Developing"), chip("Azure Networking", "Developing"),
])}
{group("Automation &amp; Infrastructure", [
    chip("Security Automation", "Developing"), chip("Shuffle", "Developing"),
])}
    <p class="metrics-note" style="margin-top:52px;">
      Hands-on: used directly in a published lab, project or write-up. Developing: actively
      building depth through current certification work or labs. Familiar: studied and understood,
      not yet applied in a project on this site.
    </p>
  </div>
</section>
"""

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "skills.html"), "w") as f:
    f.write(page(
        title="Skills | Mojalefa L. Letsoara",
        description="Practical security operations, Microsoft Security, threat and investigation, networking and cloud skills, each labelled by real usage rather than invented percentages.",
        og_title="Skills | Mojalefa L. Letsoara",
        og_description="What I can actually do, labelled by how I've actually used it.",
        canonical="skills.html",
        active_href="skills.html",
        body_sections=skills_body,
    ))

print("skills.html written")

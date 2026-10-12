#!/usr/bin/env python3
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_pages import page

VERIFY = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M7 17 17 7M7 7h10v10"/></svg>'

# ---------------------------------------------------------------------------
# Data. Dates, links and domain weights are all real and verifiable.
# Resources Used = what he actually studied with. Resources Recommended =
# the official vendor path, separate, since "used" is a personal claim and
# "recommended" is not.
# ---------------------------------------------------------------------------

CERTS = [
    ("Mar 2026", "AZ-900: Azure Fundamentals", "Microsoft", "professional", "https://learn.microsoft.com/en-us/users/letsoara-9209/credentials/dd19c34f219df5fb"),
    ("Mar 2026", "SC-900: Security, Compliance &amp; Identity Fundamentals", "Microsoft", "professional", "https://learn.microsoft.com/en-us/users/letsoara-9209/credentials/certification/security-compliance-and-identity-fundamentals?tab=credentials-tab"),
    ("Jun 2026", "CompTIA Security+ (SY0-701)", "CompTIA", "professional", "https://www.credly.com/badges/d2a0f5c5-0680-4af7-b0af-1ba48c65b583/linked_in_profile"),
    ("Jun 2026", "CompTIA Cybersecurity Analyst, CySA+ (CS0-003)", "CompTIA", "professional", "https://www.credly.com/badges/5bffd046-175d-49a8-bc1f-10ea590eeb88/linked_in_profile"),
    ("Jun 2026", "AI Skills Fest 2026", "Microsoft", "micro", "https://www.credly.com/badges/651fc7b3-5c98-4ddf-85db-ebcc011cef93/linked_in_profile"),
    ("Jul 2026", "SC-200: Security Operations Analyst Associate", "Microsoft", "professional", "https://learn.microsoft.com/en-us/users/letsoara-9209/credentials/e296fc3e42379cd0"),
    ("Dec 2025", "Junior Cybersecurity Analyst Career Path", "Cisco", "learning-path", "https://www.credly.com/badges/f6fef09d-5bc2-4293-9a91-daabd9b2a51c/linked_in_profile"),
    ("Dec 2025", "Cyber Security 101", "TryHackMe", "learning-path", "https://tryhackme.com/certificate/THM-LVCV2RZ7BP"),
    ("Dec 2025", "Pre Security", "TryHackMe", "learning-path", "https://tryhackme.com/certificate/THM-RDFOIWB9KA"),
]
ORDER = ["Dec 2025", "Mar 2026", "Jun 2026", "Jul 2026"]
CERTS_SORTED = sorted(CERTS, key=lambda c: ORDER.index(c[0]), reverse=True)

CLASS_LABEL = {"professional": "Professional Cert", "micro": "Micro-credential", "learning-path": "Learning Path"}

def cert_row(date, name, provider, cls, link):
    return f"""      <div class="cert-t-row reveal">
        <div class="cert-t-date">{date}</div>
        <div class="cert-t-body">
          <div class="cert-t-name">{name}</div>
          <div class="cert-t-provider">{provider} &middot; <span class="cert-classification {cls}" style="margin:0;">{CLASS_LABEL[cls]}</span></div>
        </div>
        <a href="{link}" class="cert-t-verify" target="_blank" rel="noopener">Verify {VERIFY}</a>
      </div>"""

rows = "\n".join(cert_row(*c) for c in CERTS_SORTED)

def domain_weights(domains, note=None):
    rows_html = ""
    for name, weight, pct_mid in domains:
        rows_html += f"""      <div class="domain-row">
        <div>{name}<div class="domain-bar-track"><div class="domain-bar-fill" style="width:{pct_mid}%;"></div></div></div>
        <span class="wt">{weight}</span>
      </div>"""
    note_html = f'<div class="domain-note">{note}</div>' if note else ""
    return f"""    <div class="domain-weights">
      <div class="domain-weights-label">Exam domains (Microsoft's published weights)</div>
{rows_html}
{note_html}
    </div>"""

def resource_split(used, recommended):
    used_li = "".join(f"<li>{u}</li>" for u in used)
    rec_li = "".join(f"<li>{r}</li>" for r in recommended)
    return f"""    <div class="resource-split">
      <div class="resource-col used">
        <div class="resource-col-label used">Resources I Used</div>
        <ul>{used_li}</ul>
      </div>
      <div class="resource-col rec">
        <div class="resource-col-label rec">Recommended (Official)</div>
        <ul>{rec_li}</ul>
      </div>
    </div>"""

def cert_deep_card(code, name, cls, status_label, status_cls, date_or_target, domains_html, used, recommended, project_html, note=None, stage="planned", extra_html=""):
    note_html = f'<p class="dash-body" style="margin-top:10px;">{note}</p>' if note else ""
    return f"""      <div class="dash-card reveal" style="max-width:none;">
        <div style="display:flex;align-items:flex-start;justify-content:space-between;gap:12px;margin-bottom:4px;flex-wrap:wrap;">
          <div>
            <span class="cert-classification {cls}">{CLASS_LABEL[cls]}</span>
            <div style="font-size:0.95rem;font-weight:500;color:var(--ivory);margin-top:8px;">{code}: {name}</div>
          </div>
          <span class="status-pill {status_cls}">{status_label}</span>
        </div>
        <div style="font-size:0.72rem;color:var(--slate-warm);letter-spacing:0.04em;margin-bottom:4px;">{date_or_target}</div>
        {stage_track(stage)}
        {note_html}
{extra_html}
{domains_html}
{resource_split(used, recommended)}
        {project_html}
      </div>"""

def project_link(html):
    return f'<div class="cert-project-link">{html}</div>'

def stage_track(state, compact=False):
    """state: 'planned' | 'active' | 'proven'. Renders a Planned -> Active -> Proven indicator."""
    order = ["planned", "active", "proven"]
    labels = ["Planned", "Active", "Proven"]
    idx = order.index(state)
    parts = []
    for i, label in enumerate(labels):
        if i < idx or state == "proven":
            cls = "done"
        elif i == idx:
            cls = "current"
        else:
            cls = "upcoming"
        parts.append(f'<div class="stage {cls}"><span class="stage-dot"></span><span class="stage-label">{label}</span></div>')
        if i < 2:
            parts.append('<span class="stage-line"></span>')
    cls_extra = " compact" if compact else ""
    return f'<div class="stage-track{cls_extra}">{"".join(parts)}</div>'

def score_visual(score, total, label="First Attempt"):
    pct = round(score / total * 100, 1)
    pass_pct = round(700 / total * 100, 1) if total >= 700 else 100
    return f"""    <div class="score-visual">
      <div class="score-visual-row">
        <span class="score-visual-label">{label}</span>
        <span class="score-visual-value">{score} <span class="pass-mark">/ {total} (700 to pass)</span></span>
      </div>
      <div class="score-bar-track">
        <div class="score-bar-fill" style="width:{pct}%;"></div>
        <div class="score-bar-mark" style="left:{pass_pct}%;"></div>
      </div>
    </div>"""

def tier_row(name, price=None, pill_label="Proposed", pill_cls="target", evidence=None, stage="planned", num=None):
    meta = f'<div style="font-size:0.7rem;color:var(--slate-warm);margin-top:3px;">{price} planning estimate</div>' if price else ""
    evidence_html = f'<div class="cert-project-link" style="padding-top:8px;margin-top:8px;">{evidence}</div>' if evidence else ""
    num_html = f'<span class="cert-num">{num}</span>' if num else ""
    return f"""        <div style="padding:14px 0;border-top:1px solid rgba(148,163,184,0.08);">
          <div style="display:flex;align-items:flex-start;justify-content:space-between;gap:12px;">
            <div style="display:flex;align-items:flex-start;"><div>{num_html}</div><div><div style="font-size:0.86rem;font-weight:500;color:var(--ivory);">{name}</div>{meta}</div></div>
            <span class="status-pill {pill_cls}">{pill_label}</span>
          </div>
          {stage_track(stage, compact=True)}
          {evidence_html}
        </div>"""

LEARN_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20M4 4.5A2.5 2.5 0 0 1 6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15Z"/></svg>'
BACK_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 12H5M11 18l-6-6 6-6"/></svg>'

def flip_card(num, code, name, price, intro, teaches, connections, direction, flip_id):
    price_html = f'<div class="flip-price">{price} planning estimate</div>' if price else ""
    teaches_html = "".join(f"<li>{t}</li>" for t in teaches)
    tags_html = "".join(f"<li>{t}</li>" for t in connections)
    return f"""      <div class="flip-card reveal">
        <div class="flip-card-inner">
          <div class="flip-card-front" id="flip-front-{flip_id}">
            <div class="flip-num">{num}</div>
            <div class="flip-code">{code}</div>
            <div class="flip-name">{name}</div>
            <div class="flip-front-meta">
              <span class="status-pill planned" style="width:fit-content;">Planned &middot; 2027</span>
              {price_html}
              <button class="flip-trigger" type="button" aria-expanded="false" aria-controls="flip-back-{flip_id}">What this cert teaches {LEARN_ICON}</button>
            </div>
          </div>
          <div class="flip-card-back" id="flip-back-{flip_id}" aria-hidden="true">
            <div class="flip-back-label">What This Cert Teaches</div>
            <p class="flip-back-intro">{intro}</p>
            <ul class="flip-teaches-list">{teaches_html}</ul>
            <div class="flip-connection">
              <div class="flip-connection-label">Portfolio Connection</div>
              <ul class="flip-connection-tags">{tags_html}</ul>
              <div class="flip-direction">{direction}</div>
            </div>
            <button class="flip-trigger" type="button" aria-expanded="true" aria-controls="flip-front-{flip_id}" tabindex="-1">{BACK_ICON} Flip back</button>
          </div>
        </div>
      </div>"""

# ---------------------------------------------------------------------------
# Deep-dive cards: the 5 obtained professional certs
# ---------------------------------------------------------------------------

deep_professional = "\n".join([
cert_deep_card(
    "AZ-900", "Azure Fundamentals", "professional", "Obtained", "completed", "Issued March 2026",
    "", # no domain breakdown needed for a fundamentals cert already earned
    ["John Savill's AZ-900 Study Cram", "Microsoft Learn's official path", "~$200 of real hands-on lab time in a live Azure subscription"],
    ["Microsoft Learn: Azure Fundamentals path", "Official AZ-900 practice assessment"],
    project_link('Feeds directly into <strong>Enterprise Hybrid SOC Lab</strong>, the Azure environment this whole portfolio is built around.'),
    stage="proven",
),
cert_deep_card(
    "SC-900", "Security, Compliance and Identity Fundamentals", "professional", "Obtained", "completed", "Issued March 2026",
    "",
    ["John Savill's study cram", "Microsoft Learn's official path", "A freeCodeCamp video walkthrough", "ChatGPT for reinforcement"],
    ["Microsoft Learn: Security, Compliance and Identity Fundamentals path", "Official SC-900 practice assessment"],
    project_link('Provides the identity/governance vocabulary that <strong>SC-500</strong> builds directly on.'),
    stage="proven",
),
cert_deep_card(
    "SY0-701", "CompTIA Security+", "professional", "Obtained", "completed", "Issued June 2026",
    "",
    ["Professor Messer's full SY0-701 playlist", "Cyberkraft's performance-based question practice", "ChatGPT for reinforcement"],
    ["CompTIA's official exam objectives", "Official practice questions"],
    project_link('Underpins the threat-modelling work in <strong>Legacy Account Recovery, ATO Case Study</strong>.'),
    stage="proven",
),
cert_deep_card(
    "CS0-003", "CompTIA Cybersecurity Analyst, CySA+", "professional", "Obtained", "completed", "Issued June 2026",
    "",
    ["LetsDefend's investigation pathway", "Cyberkraft's PBQ practice", "The Certify Breakfast YouTube playlist", "ChatGPT for reinforcement"],
    ["CompTIA's official exam objectives", "Official practice questions"],
    project_link('Directly evidenced in <strong>Conti Ransomware Investigation</strong> and <strong>Threat Detection &amp; Log Analysis</strong>.'),
    stage="proven",
),
cert_deep_card(
    "SC-200", "Security Operations Analyst Associate", "professional", "Obtained", "completed", "Issued July 2026",
    "",
    ["Microsoft's own \"Sentinel Ninja\" training", "Microsoft Learn's official path", "John Christopher's SC-200 YouTube series"],
    ["Microsoft Learn: SC-200 path", "Official SC-200 practice assessment"],
    project_link('Directly evidenced in <strong>Enterprise SOC Portfolio</strong> and <strong>Enterprise Hybrid SOC Lab</strong>.'),
    stage="proven",
),
])

# ---------------------------------------------------------------------------
# In progress: AZ-104, with real score and verified domain weights
# ---------------------------------------------------------------------------

az104_domains = domain_weights([
    ("Manage Azure identities and governance", "20&ndash;25%", 22),
    ("Implement and manage storage", "15&ndash;20%", 17),
    ("Deploy and manage Azure compute resources", "20&ndash;25%", 22),
    ("Implement and manage virtual networking", "15&ndash;20%", 17),
    ("Monitor and maintain Azure resources", "10&ndash;15%", 12),
], note="Weights are the exam's published question distribution, not a measure of my own readiness in each area.")

az104_card = cert_deep_card(
    "AZ-104", "Azure Administrator Associate", "professional", "In Progress", "in-progress",
    'Retake: <span data-countdown-to="2026-10-20T08:30:00+02:00"></span> from now (20 Oct 2026)',
    az104_domains,
    ["Microsoft Learn's official AZ-104 path", "John Savill's AZ-104 Study Cram", "Gemini for reinforcement, worked alongside practice questions"],
    ["Microsoft Learn: AZ-104 path", "Official AZ-104 practice assessment"],
    project_link('Powers the Azure administration side of <strong>Enterprise Hybrid SOC Lab</strong>: hub-and-spoke networking, identity, endpoints.'),
    note="First attempt: roughly 15 days of preparation, without reaching the exam's final module. This retake adds more hands-on lab time and less passive review.",
    stage="active",
    extra_html=score_visual(609, 1000, label="First Attempt, 28 Jul 2026"),
)

sc500_domains = domain_weights([
    ("Manage identity, access, and governance", "20&ndash;25%", 22),
    ("Secure storage, databases, and networking", "25&ndash;30%", 27),
    ("Secure compute, including AI security", "20&ndash;25%", 22),
    ("Manage and monitor security posture", "20&ndash;25%", 22),
], note="Secure storage, databases and networking carries the most weight, so that's where study time is concentrated first.")

sc500_card = cert_deep_card(
    "SC-500", "Cloud and AI Security Engineer Associate", "professional", "In Progress", "in-progress",
    "21 Oct 2026, the day after the AZ-104 retake",
    sc500_domains,
    ["Microsoft Learn's official SC-500 path, studied alongside AZ-104 rather than after it", "Gemini for reinforcement"],
    ["Microsoft Learn: SC-500 path", "charbelnemnom.com's independent SC-500 study guide (community resource, not official)"],
    project_link('Direct replacement for AZ-500. Will extend <strong>Enterprise Hybrid SOC Lab</strong> into securing the environment, not just running it.'),
    note="This exam only went to general availability in mid-2026, so the free-resource ecosystem around it is still thin compared to the older, established exams above.",
    stage="active",
)

ai901_domains = domain_weights([
    ("Identify AI concepts and capabilities", "40&ndash;45%", 42),
    ("Implement AI solutions using Microsoft Foundry", "55&ndash;60%", 58),
])

ai901_card = cert_deep_card(
    "AI-901", "Azure AI Fundamentals", "professional", "Planned", "planned",
    "Target: late November / December 2026",
    ai901_domains,
    ["Not started yet"],
    ["Microsoft Learn: AI-901 path", "charbelnemnom.com's AI-901 study guide"],
    project_link('Part of a broader plan to understand AI\'s security implications, not a standalone credential.'),
    note="AI-901 replaced the retired AI-900 on 30 June 2026 and goes further than the old exam: real Microsoft Foundry usage, not just describing AI concepts.",
    stage="planned",
)

certs_body = f"""
<header class="page-hero">
  <div class="main">
    <div class="page-hero-tag reveal">Certifications</div>
    <h1 class="reveal reveal-d1">Nine earned, <strong>each one verifiable</strong>.</h1>
    <p class="page-hero-sub reveal reveal-d2">
      What I've learned, why it mattered, and when I earned it. Every completed certification
      below links to a live, third-party verification page rather than a claim you have to take
      on trust. Not every credential here is the same kind of thing, so they're classified rather
      than lumped together as nine equivalent certifications.
    </p>
    <div class="page-hero-meta reveal reveal-d3">
      <span class="meta-pill"><span class="dot"></span>9 obtained</span>
      <span class="meta-pill">2 in progress</span>
      <span class="meta-pill">Last updated <span data-last-updated="2026-09-19"></span></span>
    </div>
    <div class="legend-row reveal">
      <span class="cert-classification professional">Professional Cert</span>
      <span class="cert-classification micro">Micro-credential</span>
      <span class="cert-classification learning-path">Learning Path</span>
      <span class="status-pill completed">Obtained</span>
      <span class="status-pill in-progress">In Progress</span>
      <span class="status-pill planned">Planned</span>
      <span class="status-pill target">Proposed</span>
      <span class="status-pill target">Long-Term</span>
    </div>
  </div>
</header>

<section class="section" id="obtained" style="padding-top:0;">
  <div class="main">
    <div class="section-center reveal">
      <div class="section-tag">Obtained</div>
      <h2 class="section-title">Learning, formalised and <strong>verified</strong></h2>
      <p class="section-body">Five professional certifications, one Microsoft micro-credential, and three learning-path completions. Different weight, shown as different weight.</p>
    </div>
    <div class="cert-timeline">
{rows}
    </div>
  </div>
</section>

<section class="section" id="deep-dive">
  <div class="main">
    <div class="section-center reveal">
      <div class="section-tag">The Complete Journey</div>
      <h2 class="section-title">What each one actually <strong>taught me</strong></h2>
      <p class="section-body">Resources I actually used, kept separate from what's officially recommended, plus where each certification shows up in real project work.</p>
    </div>
    <div class="dash-grid" style="grid-template-columns:1fr;gap:20px;margin-top:40px;">
{deep_professional}
    </div>
  </div>
</section>

<section class="section" id="in-progress">
  <div class="main">
    <div class="section-center reveal">
      <div class="section-tag">In Progress</div>
      <h2 class="section-title">Attempt, gap, <strong>improvement</strong></h2>
      <p class="section-body">I'm keeping this one honest rather than tidying it up.</p>
    </div>
    <div class="dash-grid" style="grid-template-columns:1fr;gap:20px;margin-top:40px;">
{az104_card}
{sc500_card}
    </div>
  </div>
</section>

<section class="section" id="planned">
  <div class="main">
    <div class="section-center reveal">
      <div class="section-tag">Planned</div>
      <h2 class="section-title">What comes <strong>after October</strong></h2>
    </div>
    <div class="dash-grid" style="grid-template-columns:1fr;gap:20px;margin-top:40px;">
{ai901_card}
    </div>

    <div class="section-center reveal" style="margin-top:56px;margin-bottom:0;">
      <div class="section-tag">2027</div>
      <h3 style="font-family:inherit;font-size:1.3rem;font-weight:500;color:var(--ivory);">Four certifications, in priority order</h3>
    </div>

    <div class="flip-grid">
{flip_card("01", "BTL1", "Blue Team Level 1", None,
    "Focuses on practical defensive security operations and hands-on blue-team skills.",
    ["Security monitoring and defensive operations", "Alert triage and investigation", "Network and endpoint security concepts", "Threat detection and analysis", "Incident response", "Defensive tooling and practical investigation", "Analysing attacker behaviour and evidence"],
    ["SOC Operations", "Detection Engineering", "Incident Response", "Threat Investigation"],
    "Direction: Defensive Security / SOC", "btl1")}
{flip_card("02", "SecurityX", "CompTIA SecurityX", "R9,530",
    "Focuses on advanced cybersecurity concepts: designing, assessing and implementing security solutions in complex environments.",
    ["Enterprise security architecture", "Risk management", "Security engineering", "Governance, risk and compliance", "Vulnerability management", "Security operations", "Secure infrastructure", "Technical problem solving", "Emerging security considerations, including AI-related topics"],
    ["Security Engineering", "Cloud Security", "Enterprise Security Architecture", "Defensive Security"],
    "Direction: Advanced Security Engineering", "securityx")}
{flip_card("03", "AWS Security", "AWS Certified Security &ndash; Specialty", "R5,000",
    "Focuses on securing AWS cloud environments across the six official SCS-C03 exam domains.",
    ["Detection", "Incident Response", "Infrastructure Security", "Identity and Access Management", "Data Protection", "Security Foundations and Governance"],
    ["Cloud Security", "Identity Security", "Detection Engineering", "Cloud Incident Response"],
    "Direction: Cloud Security", "awssec")}
{flip_card("04", "Terraform", "HashiCorp Certified: Terraform Associate", None,
    "Focuses on Infrastructure as Code and the core Terraform workflow.",
    ["Infrastructure as Code concepts", "Terraform fundamentals and providers", "Resources, variables and configuration", "Terraform state", "Core workflow: init, validate, plan, apply", "Modules and infrastructure lifecycle", "HCP Terraform collaboration concepts"],
    ["Cloud Infrastructure", "Infrastructure as Code", "Automation", "DevSecOps"],
    "Direction: Infrastructure Automation / DevSecOps", "terraform")}
    </div>

    <div class="dash-grid" style="grid-template-columns:1fr;margin-top:32px;">
      <div class="dash-card reveal reveal-d1">
        <div class="dash-card-label">Proposed, 2028 to 2029</div>
{tier_row("AZ-400: DevOps Engineer Expert")}
{tier_row("GitHub Foundations, Actions &amp; Advanced Security")}
{tier_row("CKA &amp; CKS")}
{tier_row("SC-100")}
{tier_row("CISSP")}
        <p style="font-size:0.7rem;color:var(--slate-warm);font-style:italic;margin-top:12px;">Development ideas, not commitments with dates attached yet.</p>
      </div>
    </div>

    <p class="metrics-note" style="margin-top:36px;">
      This page tracks what each certification covers, the role it plays in my development and
      when I earned it, not what it cost. For target months, see the
      <a href="calendar.html" style="color:var(--cyan);">Certification Calendar</a>. For how it
      all connects, see the <a href="roadmap.html" style="color:var(--cyan);">Career Roadmap</a>.
    </p>
  </div>
</section>
"""

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "certifications.html"), "w") as f:
    f.write(page(
        title="Certifications | Mojalefa L. Letsoara",
        description="Nine classified certifications across Microsoft, CompTIA, Cisco and TryHackMe, with real exam domains, study resources used versus recommended, and project evidence links.",
        og_title="Certifications | Mojalefa L. Letsoara",
        og_description="Nine verified certifications, classified honestly, with the complete learning journey behind each one.",
        canonical="certifications.html",
        active_href="certifications.html",
        body_sections=certs_body,
    ))

print("certifications.html written")

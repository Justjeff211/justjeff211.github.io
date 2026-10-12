#!/usr/bin/env python3
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_pages import page

ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'

def year_block(year, title, focus, targets, current=False):
    tag_html = "".join(f"<li>{t}</li>" for t in targets)
    return f"""    <div class="year-block year-{year} reveal">
      <div class="year-head">
        <span class="year-num">{year}</span>
        <span class="year-title">{title}</span>
        {'<span class="status-pill in-progress">Current</span>' if current else ''}
      </div>
      <p class="year-focus">{focus}</p>
      <ul class="year-targets">{tag_html}</ul>
    </div>"""

roadmap_body = f"""
<header class="page-hero">
  <div class="main">
    <div class="page-hero-tag reveal">Cybersecurity Career Roadmap, 2026 to 2030</div>
    <h1 class="reveal reveal-d1">A roadmap, <strong>built to change</strong>.</h1>
    <p class="page-hero-sub reveal reveal-d2">
      Specific, measurable, achievable, relevant and time-bound. This is a working document, not
      a finished one. I have a mentor who continues to guide my direction, so what's past 2026
      here is direction, not a fixed prediction.
    </p>
    <div class="page-hero-meta reveal reveal-d3">
      <span class="meta-pill"><span class="dot"></span>Actively maintained</span>
      <span class="meta-pill">Last updated <span data-last-updated="2026-09-19"></span></span>
      <span class="meta-pill" data-github-pulse>Synced with GitHub</span>
    </div>
  </div>
</header>

<section class="section" id="flow" style="padding-top:0;">
  <div class="main">
    <div class="section-center reveal">
      <div class="section-tag">The Direction</div>
      <h2 class="section-title">IT Support toward <strong>Cloud Security Engineering</strong></h2>
      <p class="section-body">I'm a Cybersecurity Analyst with 3+ years of IT Support experience, actively building toward Cloud Security Engineering. This is direction, not a claim that every stage is already reached.</p>
    </div>

    <div class="flow-row flow-row-5">
      <div class="flow-node reveal"><span class="flow-node-num">01</span><h3>IT Support</h3></div>
      <div class="flow-connector reveal">{ARROW}</div>
      <div class="flow-node current reveal reveal-d1"><span class="flow-node-num">02</span><h3>Cybersecurity</h3></div>
      <div class="flow-connector reveal">{ARROW}</div>
      <div class="flow-node reveal reveal-d2"><span class="flow-node-num">03</span><h3>Cloud Security</h3></div>
      <div class="flow-connector reveal">{ARROW}</div>
      <div class="flow-node reveal reveal-d3"><span class="flow-node-num">04</span><h3>Automation</h3></div>
      <div class="flow-connector reveal">{ARROW}</div>
      <div class="flow-node reveal"><span class="flow-node-num">05</span><h3>DevSecOps / Cloud Security Engineering</h3></div>
    </div>
  </div>
</section>

<section class="section" id="roadmap-years">
  <div class="main">
    <div class="section-center reveal">
      <div class="section-tag">Year by Year</div>
      <h2 class="section-title">2026 <strong>to</strong> 2030</h2>
    </div>

    <div style="margin-top:44px;">
{year_block("2026", "Strengthen Cloud Foundations", "Strengthening my transition from IT Support toward cloud-focused cybersecurity work: Azure administration, networking, identity, monitoring, Microsoft Security and cloud security.", ["AZ-104", "SC-500", "AI-901"], current=True)}
{year_block("2027", "Build Defensive &amp; Automation Skills", "Building stronger defensive security and automation capability while progressing toward SOC and cloud security responsibilities: blue team operations, investigation, automation and repeatable security workflows.", ["01 &middot; BTL1", "02 &middot; SecurityX", "03 &middot; AWS Security Specialty", "04 &middot; Terraform Associate"])}
{year_block("2028", "Master DevSecOps &amp; Infrastructure", "Cloud through DevOps, automation, secure CI/CD, containers and Kubernetes security. Proposed direction, not a booked plan yet.", ["AZ-400", "GitHub Foundations", "GitHub Actions", "GitHub Advanced Security", "CKA", "CKS"])}
{year_block("2029", "Advance Toward Architect-Level Development", "Longer-term direction toward architect and principal-level security roles. Proposed, not a claim that any of these are underway.", ["SC-100", "CISSP"])}
{year_block("2030", "Expand Toward Multi-Cloud &amp; Incident Response", "Broader security engineering, cloud engineering and incident response capability across more than one cloud provider. Direction, not a guaranteed outcome, and not yet attached to any specific certification.", [])}
    </div>
  </div>
</section>

<div class="phase-divider"><span>Right Now</span></div>

<section class="section" id="current">
  <div class="main">
    <div class="section-center reveal">
      <div class="section-tag">Current Focus &amp; Currently Building</div>
      <h2 class="section-title">What I'm working on <strong>this quarter</strong></h2>
    </div>

    <div class="dash-grid">
      <div class="dash-card reveal">
        <div class="dash-card-label">Current Focus</div>
        <ul><li>SOC Operations</li><li>Microsoft Security</li><li>Azure Security</li><li>Detection Engineering</li><li>Incident Response</li><li>Cloud Security</li></ul>
      </div>
      <div class="dash-card reveal reveal-d1">
        <div class="dash-card-label">Currently Building</div>
        <div class="dash-body">
          Preparing for the AZ-104 retake and SC-500, studied side by side rather than one after
          the other, since both exams sit back to back in October.
        </div>
        <p style="margin-top:14px;font-size:0.78rem;color:var(--cyan);font-weight:500;">
          AZ-104 retake in <span data-countdown-to="2026-10-20T08:30:00+02:00"></span>
        </p>
      </div>
      <div class="dash-card reveal reveal-d2">
        <div class="dash-card-label">Next Milestone</div>
        <div class="dash-body">AI-901, targeted for late November or December 2026, part of a broader understanding of AI's role in security rather than an isolated credential.</div>
        <a href="calendar.html" style="display:inline-block;margin-top:14px;font-size:0.76rem;color:var(--cyan);">View the full calendar &rarr;</a>
      </div>
    </div>
  </div>
</section>

<div class="phase-divider"><span>December 2026 and Beyond</span></div>

<section class="section" id="next-chapter">
  <div class="main">
    <div class="feature">
      <div class="feature-content reveal">
        <div class="section-tag">Next Chapter</div>
        <h2 class="section-title">December 2026<strong>+</strong></h2>
        <p class="section-body">
          After AI-901, the plan opens up rather than locking into a fixed sequence. I expect to
          keep developing deeper SOC work, Microsoft Security, Azure Security, detection
          engineering, threat hunting, incident response, security automation, cloud security and
          a working understanding of AI's security implications, all backed by practical projects
          and technical write-ups.
        </p>
        <p class="section-body" style="margin-top:20px;">
          This section stays intentionally open. My mentor's guidance shapes it as I go, so treat
          everything past this point as direction, not a fixed prophecy.
        </p>
      </div>
      <div class="feature-visual reveal reveal-d2" aria-hidden="true">
        <svg viewBox="0 0 560 320" preserveAspectRatio="xMidYMid meet">
          <circle cx="280" cy="160" r="120" fill="none" stroke="#38BDF8" stroke-width="1" opacity="0.14" stroke-dasharray="4 6"/>
          <circle cx="280" cy="160" r="80" fill="none" stroke="#38BDF8" stroke-width="1" opacity="0.22" stroke-dasharray="4 6"/>
          <text x="280" y="155" text-anchor="middle" font-family="Montserrat, sans-serif" font-size="13" font-weight="700" fill="#38BDF8" letter-spacing="1.5">DEC 2026</text>
          <text x="280" y="175" text-anchor="middle" font-family="Montserrat, sans-serif" font-size="9" font-weight="500" fill="#64748B" letter-spacing="2">AND OPEN FROM THERE</text>
        </svg>
      </div>
    </div>
  </div>
</section>
"""

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "roadmap.html"), "w") as f:
    f.write(page(
        title="Cybersecurity Career Roadmap, 2026 to 2030 | Mojalefa L. Letsoara",
        description="A living, SMART cybersecurity career roadmap from 2026 to 2030: current focus, what's currently being built, and the direction toward Cloud Security Engineering.",
        og_title="Cybersecurity Career Roadmap, 2026 to 2030 | Mojalefa L. Letsoara",
        og_description="A living, SMART career roadmap, built to change as my mentor continues to guide my direction.",
        canonical="roadmap.html",
        active_href="roadmap.html",
        body_sections=roadmap_body,
    ))

print("roadmap.html written")

#!/usr/bin/env python3
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_pages import page

calendar_body = """
<header class="page-hero">
  <div class="main">
    <div class="page-hero-tag reveal">Certification Calendar</div>
    <h1 class="reveal reveal-d1">What's booked, <strong>what's coming</strong>.</h1>
    <p class="page-hero-sub reveal reveal-d2">
      Exact dates where they exist. Target months or years where they don't. Nothing here is
      invented, and this calendar updates as things actually get booked.
    </p>
    <div class="page-hero-meta reveal reveal-d3">
      <span class="meta-pill"><span class="dot"></span>Live tracking</span>
      <span class="meta-pill">Last updated <span data-last-updated="2026-09-19"></span></span>
    </div>
  </div>
</header>

<section class="section" id="cal-2026" style="padding-top:0;">
  <div class="main">
    <div class="section-center reveal">
      <div class="section-tag">2026</div>
      <h2 class="section-title">The rest of <strong>this year</strong></h2>
    </div>

    <div class="cal-grid">
      <div class="cal-card is-now reveal">
        <div class="cal-month">Now</div>
        <div class="cal-year">September</div>
        <div class="cal-entry">
          <div class="cal-entry-title">AZ-104 and SC-500 preparation</div>
          <span class="status-pill in-progress cal-entry-status">In progress</span>
        </div>
      </div>

      <div class="cal-card reveal reveal-d1">
        <div class="cal-month">Booked</div>
        <div class="cal-year">October</div>
        <div class="cal-entry">
          <div class="cal-entry-title">AZ-104 Retake, 20 October 2026</div>
          <span class="status-pill in-progress cal-entry-status">Booked</span>
        </div>
        <div class="cal-entry">
          <div class="cal-entry-title">SC-500, 21 October 2026</div>
          <span class="status-pill in-progress cal-entry-status">Booked</span>
        </div>
      </div>

      <div class="cal-card reveal reveal-d2">
        <div class="cal-month">Planned</div>
        <div class="cal-year">November</div>
        <div class="cal-entry">
          <div class="cal-entry-title">AI-901 preparation continues</div>
          <span class="status-pill planned cal-entry-status">Target month</span>
        </div>
      </div>

      <div class="cal-card reveal reveal-d3">
        <div class="cal-month">Target</div>
        <div class="cal-year">December</div>
        <div class="cal-entry">
          <div class="cal-entry-title">AI-901: Azure AI Fundamentals Target</div>
          <span class="status-pill planned cal-entry-status">Target month</span>
        </div>
        <div class="cal-entry">
          <div class="cal-entry-title">Next chapter begins</div>
          <span class="status-pill target cal-entry-status">Planned</span>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section" id="cal-2027">
  <div class="main">
    <div class="section-center reveal">
      <div class="section-tag">2027</div>
      <h2 class="section-title">Defensive &amp; <strong>automation skills</strong></h2>
      <p class="section-body">All four planned for 2027, in priority order.</p>
    </div>

    <div class="cal-grid">
      <div class="cal-card reveal">
        <div class="cal-month">2027</div>
        <div class="cal-year"><span class="cert-num">01</span>BTL1</div>
        <div class="cal-entry">
          <div class="cal-entry-title">Blue Team Level 1</div>
          <span class="status-pill planned cal-entry-status">Planned</span>
        </div>
      </div>
      <div class="cal-card reveal reveal-d1">
        <div class="cal-month">2027</div>
        <div class="cal-year"><span class="cert-num">02</span>SecurityX</div>
        <div class="cal-entry">
          <div class="cal-entry-title">CompTIA SecurityX</div>
          <span class="status-pill planned cal-entry-status">Planned</span>
        </div>
      </div>
      <div class="cal-card reveal reveal-d2">
        <div class="cal-month">2027</div>
        <div class="cal-year"><span class="cert-num">03</span>AWS Security</div>
        <div class="cal-entry">
          <div class="cal-entry-title">AWS Certified Security &ndash; Specialty</div>
          <span class="status-pill planned cal-entry-status">Planned</span>
        </div>
      </div>
      <div class="cal-card reveal reveal-d3">
        <div class="cal-month">2027</div>
        <div class="cal-year"><span class="cert-num">04</span>Terraform</div>
        <div class="cal-entry">
          <div class="cal-entry-title">HashiCorp Certified: Terraform Associate</div>
          <span class="status-pill planned cal-entry-status">Planned</span>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section" id="cal-future">
  <div class="main">
    <div class="section-center reveal">
      <div class="section-tag">2028 and Beyond</div>
      <h2 class="section-title">Proposed <strong>direction</strong></h2>
      <p class="section-body">
        AZ-400, the GitHub certifications, CKA and CKS sit in 2028 as proposed development, not
        booked dates. SC-100 and CISSP sit further out again, in 2029, as longer-term
        direction. Full detail and status definitions live on the
        <a href="certifications.html" style="color:var(--cyan);">Certifications</a> page, and how
        it all connects lives on the <a href="roadmap.html" style="color:var(--cyan);">Career Roadmap</a>.
      </p>
    </div>
  </div>
</section>
"""

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "calendar.html"), "w") as f:
    f.write(page(
        title="Certification Calendar | Mojalefa L. Letsoara",
        description="Month-by-month certification calendar for 2026, plus 2027 targets: what's booked, what's in preparation, and what's targeted next.",
        og_title="Certification Calendar | Mojalefa L. Letsoara",
        og_description="What's booked, what's in preparation, and what's targeted next, month by month and year by year.",
        canonical="calendar.html",
        active_href="calendar.html",
        body_sections=calendar_body,
    ))

print("calendar.html written")

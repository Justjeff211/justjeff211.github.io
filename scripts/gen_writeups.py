#!/usr/bin/env python3
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_pages import page

def row(title, desc, tags, link=None, linktext="View on GitHub"):
    tag_html = "".join(f"<li>{t}</li>" for t in tags)
    inner = f"""<div>
          <div class="writeup-title">{title}</div>
          <div class="writeup-desc">{desc}</div>
          <ul class="writeup-tags">{tag_html}</ul>
        </div>
        <span class="tile-link" style="margin-top:0;">{linktext}<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M7 17 17 7M7 7h10v10"/></svg></span>"""
    if link:
        return f'      <a href="{link}" class="writeup-row reveal" target="_blank" rel="noopener">{inner}</a>'
    return f'      <div class="writeup-row reveal">{inner}</div>'

writeups_body = f"""
<header class="page-hero">
  <div class="main">
    <div class="page-hero-tag reveal">Write-ups</div>
    <h1 class="reveal reveal-d1">Alert to <strong>investigation</strong>.</h1>
    <p class="page-hero-sub reveal reveal-d2">
      Investigating, correlating, analysing and documenting findings clearly enough that someone
      else could pick up where I left off.
    </p>
  </div>
</header>

<section class="section" id="writeup-list" style="padding-top:0;">
  <div class="main">
    <div class="writeup-list">
{row(
    "Conti Ransomware Investigation, Splunk SIEM Threat Detection",
    "A full SOC investigation into a Conti ransomware compromise of a Microsoft Exchange server: 28,145 events analysed in Splunk 8.2.2 across Windows Security, Sysmon, IIS and Exchange logs. The attack chain ran from three exploited CVEs (CVE-2020-0796, CVE-2018-13374, CVE-2018-13379) through a trojanised cmd.exe and a deployed web shell, to credential harvesting and LSASS injection, with an 11-day attacker dwell time before detection. Written up as a 24-page technical report with 24 annotated screenshots.",
    ["Splunk", "Log Correlation", "Incident Response", "Sysmon", "MITRE ATT&amp;CK"],
    "https://github.com/Justjeff211/conti-ransomware-writeup",
)}
{row(
    "Threat Detection &amp; Log Analysis Using Splunk SIEM",
    "A Tier 1 SOC investigation simulation: 112 Apache access log entries ingested into Splunk and analysed with 9 custom SPL queries, surfacing 14 HTTP 500 errors and 4 successful DELETE operations against /api/users across 112 unique IPs. Documented as a formal P1 incident report with prioritised remediation recommendations.",
    ["Splunk", "SPL", "Log Analysis", "HTTP Forensics"],
    "https://github.com/Justjeff211/Threat-Detection-Log-Analysis-Using-Splunk-SIEM",
)}
{row(
    "Legacy Account Recovery, ATO Case Study",
    "A SOC case study on identity-based attacks inspired by the 2013 iCloud breach. Maps a full account-takeover attack chain to MITRE ATT&amp;CK and NIST, phase by phase, then writes a SOC detection rule for each phase rather than stopping at the description of the attack.",
    ["MITRE ATT&amp;CK", "NIST", "Identity Security", "Threat Modeling"],
    "https://github.com/Justjeff211/legacy-account-recovery-ato-case-study",
)}
{row(
    "MailShield SOC &amp; SOAR Lab",
    "Enterprise email security work covering synthetic email analysis, Splunk detection engineering, IOC enrichment against AbuseIPDB, VirusTotal and Talos, CyberChef decoding, risk scoring and incident closure. I deliberately left risk-score discrepancies visible in the output rather than tuning the project to produce an expected result, since the point was to expose the model's actual limitations, not hide them. Shuffle automation is the current area of active development on this one.",
    ["Splunk", "IOC Enrichment", "Risk Scoring", "Shuffle"],
    "https://github.com/Justjeff211/mailshield-soc-soar-lab",
)}
{row(
    "File &amp; Hash Threat Intelligence Analysis",
    "Practical malware triage and threat intelligence work using VirusTotal, MalwareBazaar and Hybrid Analysis: SHA256 verification, static analysis with BLint, sandbox analysis, IOC extraction and MITRE ATT&amp;CK mapping. Case samples examined include BlackMoon, IcedID, a double-extension social engineering payload, and Akira ransomware.",
    ["VirusTotal", "MalwareBazaar", "Static Analysis", "MITRE ATT&amp;CK"],
)}
{row(
    "Malware Analysis Field Guide, Static, Dynamic &amp; Threat Hunting",
    "A working intake-to-report methodology: hash verification, magic bytes, strings and entropy checks, import table review, then dynamic analysis with ProcMon, Wireshark and Any.Run, YARA rule writing, IOC extraction and documentation, and threat hunting off the back of it.",
    ["YARA", "ProcMon", "Wireshark", "Any.Run"],
)}
{row(
    "TryHackMe Write-ups",
    "A running collection of DFIR, malware analysis, memory forensics and reverse-engineering write-ups, worked from a SOC analyst's perspective rather than a pure CTF angle.",
    ["DFIR", "Malware Analysis", "Memory Forensics", "Reverse Engineering"],
    "https://github.com/Justjeff211/TryHackMe-Writeups",
)}
{row(
    "A Scandal, KC7 Cyber",
    "A KC7 investigation exercise built around attacker behaviour, event correlation and end-to-end incident analysis using KQL.",
    ["KQL", "Event Correlation", "Incident Analysis"],
    "https://github.com/Justjeff211/A-Scandal-KC7Cyber",
)}
    </div>

    <div style="text-align:center;margin-top:48px;" class="reveal">
      <a href="https://github.com/Justjeff211?tab=repositories" class="btn-secondary" target="_blank" rel="noopener">All Repositories on GitHub</a>
    </div>
  </div>
</section>
"""

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "writeups.html"), "w") as f:
    f.write(page(
        title="Write-ups | Mojalefa L. Letsoara",
        description="SOC investigations and write-ups: Conti ransomware, Splunk log analysis, MailShield SOC/SOAR, malware and file threat intelligence, and an account-takeover case study mapped to MITRE ATT&CK.",
        og_title="Write-ups | Mojalefa L. Letsoara",
        og_description="Investigating, correlating, analysing and documenting findings, published in full.",
        canonical="writeups.html",
        active_href="writeups.html",
        body_sections=writeups_body,
    ))

print("writeups.html written")

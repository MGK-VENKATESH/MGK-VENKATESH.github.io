#!/usr/bin/env python3
"""
GATE 2026 Portfolio Patcher
Run: python3 patch_index.py
It will read index.html, apply 3 patches, and save index.html
"""
import shutil, sys

GATE_CSS = """/* ── GATE 2026 SECTION ── */
  .gate-wrapper {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.5rem;
  }
  .gate-card {
    background: var(--bg2);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 1.75rem;
    position: relative;
    overflow: hidden;
    transition: all 0.3s cubic-bezier(0.34,1.56,0.64,1);
    z-index: 1;
  }
  .gate-card::before {
    content: '';
    position: absolute; top: 0; left: 0; right: 0; height: 2px;
    opacity: 0;
    transition: opacity 0.3s;
  }
  .gate-card.cs::before {
    background: linear-gradient(to right, var(--accent2), var(--accent));
  }
  .gate-card.da::before {
    background: linear-gradient(to right, #f59e0b, var(--accent3));
  }
  .gate-card:hover { transform: scale(1.02); z-index: 10; }
  .gate-card.cs:hover { border-color: rgba(0,245,255,0.35); box-shadow: 0 0 30px rgba(0,245,255,0.2); }
  .gate-card.da:hover { border-color: rgba(245,158,11,0.35); box-shadow: 0 0 30px rgba(245,158,11,0.2); }
  .gate-card:hover::before { opacity: 1; }
  .gate-card-header {
    display: flex; align-items: flex-start; justify-content: space-between;
    margin-bottom: 1.4rem; gap: 1rem;
  }
  .gate-badge {
    display: inline-flex; align-items: center; gap: 0.5rem;
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.68rem; letter-spacing: 2px;
    padding: 0.28rem 0.75rem; border-radius: 2px;
  }
  .gate-badge.cs-badge { color: var(--accent); background: rgba(0,245,255,0.07); border: 1px solid rgba(0,245,255,0.25); }
  .gate-badge.da-badge { color: #f59e0b; background: rgba(245,158,11,0.07); border: 1px solid rgba(245,158,11,0.25); }
  .gate-exam-tag {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.65rem; color: var(--accent3); letter-spacing: 1px;
    padding: 0.2rem 0.55rem; border: 1px solid rgba(16,185,129,0.3);
    border-radius: 2px; background: rgba(16,185,129,0.06);
  }
  .gate-paper-name {
    font-family: 'Orbitron', monospace; font-size: 0.95rem; font-weight: 700;
    color: #fff; margin-bottom: 0.2rem; line-height: 1.3;
  }
  .gate-reg {
    font-family: 'Share Tech Mono', monospace; font-size: 0.7rem;
    color: var(--muted); letter-spacing: 1px; margin-bottom: 1.4rem;
  }
  .gate-stats {
    display: grid; grid-template-columns: repeat(3, 1fr); gap: 0.75rem; margin-bottom: 1.4rem;
  }
  .gate-stat {
    background: rgba(255,255,255,0.025); border: 1px solid var(--border);
    border-radius: 4px; padding: 0.75rem 0.6rem; text-align: center;
  }
  .gate-stat-num {
    font-family: 'Orbitron', monospace; font-size: 1.3rem; font-weight: 700;
    margin-bottom: 0.2rem; line-height: 1;
  }
  .gate-card.cs .gate-stat-num { color: var(--accent); text-shadow: 0 0 12px rgba(0,245,255,0.35); }
  .gate-card.da .gate-stat-num { color: #f59e0b; text-shadow: 0 0 12px rgba(245,158,11,0.35); }
  .gate-stat-label {
    font-family: 'Share Tech Mono', monospace; font-size: 0.6rem;
    color: var(--muted); letter-spacing: 1.5px; text-transform: uppercase;
  }
  .gate-meta-row {
    display: flex; align-items: center; justify-content: space-between;
    padding: 0.6rem 0.75rem; background: rgba(255,255,255,0.02);
    border: 1px solid var(--border); border-radius: 4px; margin-bottom: 0.5rem;
    font-family: 'Share Tech Mono', monospace; font-size: 0.75rem;
  }
  .gate-meta-key { color: var(--muted); letter-spacing: 1px; }
  .gate-meta-val { color: var(--text); }
  .gate-footer {
    display: flex; align-items: center; justify-content: space-between;
    margin-top: 1.25rem; padding-top: 1rem; border-top: 1px solid var(--border);
    flex-wrap: wrap; gap: 0.6rem;
  }
  .gate-validity { font-family: 'Share Tech Mono', monospace; font-size: 0.68rem; color: var(--muted); }
  .gate-verify-btn {
    display: inline-flex; align-items: center; gap: 0.4rem;
    font-family: 'Share Tech Mono', monospace; font-size: 0.7rem; letter-spacing: 1px;
    text-decoration: none; padding: 0.3rem 0.85rem; border-radius: 2px; transition: all 0.3s;
  }
  .gate-card.cs .gate-verify-btn { color: var(--accent); border: 1px solid rgba(0,245,255,0.3); background: rgba(0,245,255,0.05); }
  .gate-card.cs .gate-verify-btn:hover { background: rgba(0,245,255,0.12); border-color: var(--accent); box-shadow: 0 0 12px rgba(0,245,255,0.25); }
  .gate-card.da .gate-verify-btn { color: #f59e0b; border: 1px solid rgba(245,158,11,0.3); background: rgba(245,158,11,0.05); }
  .gate-card.da .gate-verify-btn:hover { background: rgba(245,158,11,0.12); border-color: #f59e0b; box-shadow: 0 0 12px rgba(245,158,11,0.25); }
  .gate-iit-tag {
    font-family: 'Share Tech Mono', monospace; font-size: 0.62rem; color: var(--muted);
    letter-spacing: 1px; display: flex; align-items: center; gap: 0.4rem; margin-top: 1rem;
  }
  .gate-iit-tag::before { content: ''; display: inline-block; width: 16px; height: 1px; background: var(--muted); }
  @media (max-width: 768px) { .gate-wrapper { grid-template-columns: 1fr; } }"""

GATE_NAV = """    <li><a href="#gate">./gate2026</a></li>
    """

GATE_HTML = """<!-- GATE 2026 -->
<section id="gate">
  <div class="section-header fade-up">
    <div class="section-tag">03.5 GATE_2026</div>
    <h2 class="section-title">GATE 2026 Scorecards</h2>
    <div class="section-line"></div>
  </div>

  <div class="gate-wrapper">

    <!-- CS CARD -->
    <div class="gate-card cs fade-up">
      <div class="gate-card-header">
        <div><div class="gate-badge cs-badge">⚙ CS — COMPUTER SCIENCE</div></div>
        <div class="gate-exam-tag">✓ QUALIFIED</div>
      </div>
      <div class="gate-paper-name">Computer Science &amp;<br>Information Technology</div>
      <div class="gate-reg">Reg: CS26S41527702 &nbsp;·&nbsp; Feb 8, 2026</div>
      <div class="gate-stats">
        <div class="gate-stat">
          <div class="gate-stat-num">346</div>
          <div class="gate-stat-label">GATE Score</div>
        </div>
        <div class="gate-stat">
          <div class="gate-stat-num">29612</div>
          <div class="gate-stat-label">AIR</div>
        </div>
        <div class="gate-stat">
          <div class="gate-stat-num">29.7</div>
          <div class="gate-stat-label">Marks /100</div>
        </div>
      </div>
      <div class="gate-meta-row">
        <span class="gate-meta-key">Total Appeared</span>
        <span class="gate-meta-val">2,11,020</span>
      </div>
      <div class="gate-meta-row">
        <span class="gate-meta-key">Qualifying Marks (General)</span>
        <span class="gate-meta-val">30.0</span>
      </div>
      <div class="gate-meta-row">
        <span class="gate-meta-key">Organizing Institute</span>
        <span class="gate-meta-val">IIT Guwahati</span>
      </div>
      <div class="gate-iit-tag">GATE 2026 &nbsp;·&nbsp; Valid up to 31 March 2029</div>
      <div class="gate-footer">
        <span class="gate-validity">Scorecard valid till March 2029</span>
        <a href="https://drive.google.com/file/d/1rsdTIinKTo5UseMhtKXcFuQshnicKaOJ/view?usp=sharing"
           target="_blank" class="gate-verify-btn">↗ VIEW SCORECARD</a>
      </div>
    </div>

    <!-- DA CARD -->
    <div class="gate-card da fade-up">
      <div class="gate-card-header">
        <div><div class="gate-badge da-badge">🤖 DA — DATA SCIENCE &amp; AI</div></div>
        <div class="gate-exam-tag">✓ QUALIFIED</div>
      </div>
      <div class="gate-paper-name">Data Science &amp;<br>Artificial Intelligence</div>
      <div class="gate-reg">Reg: DA26S81527878 &nbsp;·&nbsp; Feb 15, 2026</div>
      <div class="gate-stats">
        <div class="gate-stat">
          <div class="gate-stat-num">349</div>
          <div class="gate-stat-label">GATE Score</div>
        </div>
        <div class="gate-stat">
          <div class="gate-stat-num">9935</div>
          <div class="gate-stat-label">AIR</div>
        </div>
        <div class="gate-stat">
          <div class="gate-stat-num">26.33</div>
          <div class="gate-stat-label">Marks /100</div>
        </div>
      </div>
      <div class="gate-meta-row">
        <span class="gate-meta-key">Total Appeared</span>
        <span class="gate-meta-val">69,242</span>
      </div>
      <div class="gate-meta-row">
        <span class="gate-meta-key">Qualifying Marks (General)</span>
        <span class="gate-meta-val">26.4</span>
      </div>
      <div class="gate-meta-row">
        <span class="gate-meta-key">Organizing Institute</span>
        <span class="gate-meta-val">IIT Guwahati</span>
      </div>
      <div class="gate-iit-tag">GATE 2026 &nbsp;·&nbsp; Valid up to 31 March 2029</div>
      <div class="gate-footer">
        <span class="gate-validity">Scorecard valid till March 2029</span>
        <a href="https://drive.google.com/file/d/1YIvq3LkkjwraBrhNrZ0raIorvMotvERy/view?usp=sharing"
           target="_blank" class="gate-verify-btn">↗ VIEW SCORECARD</a>
      </div>
    </div>

  </div><!-- /gate-wrapper -->
</section>"""

def patch(html):
    errors = []

    # 1) CSS — insert before scrollbar section
    anchor1 = "  /* ── SCROLLBAR ── */"
    if anchor1 in html:
        html = html.replace(anchor1, GATE_CSS + "\n\n  " + anchor1.strip(), 1)
        print("✓ Patch 1 applied: GATE CSS added")
    else:
        errors.append("✗ Patch 1 FAILED: scrollbar anchor not found")

    # 2) Nav link — insert before ./contact nav item
    anchor2 = '<a href="#contact" class="nav-cta">./contact</a>'
    nav_li   = '<li>' + anchor2 + '</li>'
    if nav_li in html:
        html = html.replace(nav_li, '<li><a href="#gate">./gate2026</a></li>\n    ' + nav_li, 1)
        print("✓ Patch 2 applied: nav link added")
    else:
        errors.append("✗ Patch 2 FAILED: nav contact link not found")

    # 3) Section HTML — insert before INTERNSHIPS comment
    anchor3 = "<!-- INTERNSHIPS -->"
    if anchor3 in html:
        html = html.replace(anchor3, GATE_HTML + "\n\n" + anchor3, 1)
        print("✓ Patch 3 applied: GATE section inserted")
    else:
        errors.append("✗ Patch 3 FAILED: internships anchor not found")

    for e in errors:
        print(e, file=sys.stderr)
    return html

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

shutil.copy("index.html", "index.html.bak")
print("Backup saved: index.html.bak")

patched = patch(html)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(patched)

print("\nDone! index.html updated with GATE 2026 section.")
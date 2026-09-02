---
title: "Concealed executable blocks in MATLAB/Simulink"
date: 2026-09-01
cve: "CVE pending"
cwe: "CWE-451"
product: "MATLAB / Simulink"
status: "Reported · vendor acknowledged"
summary: "Critical Vulnerability: A Simulink model can hide an executable block the editor never shows. Opening and running the model executes the attacker's shell commands on your machine."
---

<div class="disc-tldr">
  <p class="lead">Critical Vulnerability</p>
  <p class="lead">A Simulink <code>.slx</code> model can carry concealed blocks that run arbitrary shell commands on your computer — and hide the blocks so completely that the Simulink editor will not show them, no matter how you scroll or zoom.</p>
  <p>The model can be made to look perfectly ordinary. Opening it and pressing <em>Run</em> executes attacker-controlled shell commands with your privileges. Verified on MATLAB/Simulink R2026a Update 2 and earlier.</p>
  <p>MathWorks plans to ship a fix in the upcoming R2026b release at the end of September, and will attempt to backport the fix to earlier versions.</p>
</div>

## Imagine this

A friend sends you `HelloWorld.py` and asks for help. You open it in your IDE, say VS Code or PyCharm, and see three harmless lines:

<figure class="disc-fig">
  <div class="disc-split">
    <div class="disc-pane">
      <div class="disc-pane-head"><span class="dot"></span>What you see in your IDE</div>
      <div class="disc-pane-body">
        <div class="disc-editor">
          <div class="row"><span class="ln">1</span><span class="code"><span class="kw">def</span> greet(name):</span></div>
          <div class="row"><span class="ln">2</span><span class="code">    <span class="kw">return</span> f"Hello, {name}!"</span></div>
          <div class="row"><span class="ln">3</span><span class="code">print(greet("world"))</span></div>
          <div class="gap">end of file — nothing more to scroll to, zoom into, or select.</div>
          <div class="disc-sb" aria-hidden="true"><div class="thumb full"></div></div>
        </div>
      </div>
    </div>
    <div class="disc-pane is-danger">
      <div class="disc-pane-head"><span class="dot"></span>What actually runs</div>
      <div class="disc-pane-body">
        <div class="disc-editor">
          <div class="row"><span class="ln">1</span><span class="code"><span class="kw">def</span> greet(name):</span></div>
          <div class="row"><span class="ln">2</span><span class="code">    <span class="kw">return</span> f"Hello, {name}!"</span></div>
          <div class="row"><span class="ln">3</span><span class="code">print(greet("world"))</span></div>
          <div class="jump"><span class="ln">⋮</span><span class="code"></span></div>
          <div class="row concealed"><span class="ln">1001</span><span class="code">import os</span></div>
          <div class="row concealed"><span class="ln">1002</span><span class="code">os.system("rm -rf /")</span></div>
          <div class="disc-sb" aria-hidden="true"><div class="thumb tiny"></div></div>
        </div>
      </div>
    </div>
  </div>
  <figcaption>A source-code analogy of the vulnerability. Left: the harmful content stays hidden in your IDE. Right: what the file actually contains.</figcaption>
</figure>

## Now in Simulink

A Simulink model is a diagram of connected blocks. You read it the way you would read any diagram: you look at the canvas, scroll, and zoom. What you see is what the model does — or so Simulink leads you to believe.

On the left, everything Simulink shows you: an input, a gain, an output. On the right, the same model with its concealed passenger revealed.

<figure class="disc-fig">
  <div class="disc-split">
    <div class="disc-pane">
      <div class="disc-pane-head"><span class="dot"></span>What you see in Simulink</div>
      <div class="disc-pane-body">
        <svg viewBox="0 0 300 110" role="img" aria-label="Simulink canvas showing In1 to Gain to Out1">
          <defs><marker id="f2a-ar" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="var(--fg)"/></marker></defs>
          <rect x="6" y="14" width="256" height="66" rx="6" fill="none" stroke="var(--muted)" stroke-width="1" stroke-dasharray="4 4"/>
          <rect x="14" y="23" width="46" height="26" rx="4" fill="none" stroke="var(--fg)" stroke-width="1.5"/>
          <text x="37" y="70" text-anchor="middle" font-size="11" fill="var(--muted)">In1</text>
          <line x1="60" y1="36" x2="112" y2="36" stroke="var(--fg)" stroke-width="1.5" marker-end="url(#f2a-ar)"/>
          <path d="M116,20 L116,52 L150,36 Z" fill="none" stroke="var(--fg)" stroke-width="1.5"/>
          <text x="125" y="40" text-anchor="middle" font-size="11" fill="var(--fg)">1</text>
          <text x="132" y="70" text-anchor="middle" font-size="11" fill="var(--muted)">Gain</text>
          <line x1="150" y1="36" x2="204" y2="36" stroke="var(--fg)" stroke-width="1.5" marker-end="url(#f2a-ar)"/>
          <rect x="206" y="23" width="46" height="26" rx="4" fill="none" stroke="var(--fg)" stroke-width="1.5"/>
          <text x="229" y="70" text-anchor="middle" font-size="11" fill="var(--muted)">Out1</text>
        </svg>
      </div>
    </div>
    <div class="disc-pane is-danger">
      <div class="disc-pane-head"><span class="dot"></span>What actually runs</div>
      <div class="disc-pane-body">
        <svg viewBox="0 0 300 160" role="img" aria-label="The same canvas as the editor shows, plus a concealed executable block far off-canvas">
          <defs><marker id="f2b-ar" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="var(--fg)"/></marker></defs>
          <rect x="6" y="14" width="256" height="66" rx="6" fill="none" stroke="var(--muted)" stroke-width="1" stroke-dasharray="4 4"/>
          <rect x="14" y="23" width="46" height="26" rx="4" fill="none" stroke="var(--fg)" stroke-width="1.5"/>
          <text x="37" y="70" text-anchor="middle" font-size="11" fill="var(--muted)">In1</text>
          <line x1="60" y1="36" x2="112" y2="36" stroke="var(--fg)" stroke-width="1.5" marker-end="url(#f2b-ar)"/>
          <path d="M116,20 L116,52 L150,36 Z" fill="none" stroke="var(--fg)" stroke-width="1.5"/>
          <text x="125" y="40" text-anchor="middle" font-size="11" fill="var(--fg)">1</text>
          <text x="132" y="70" text-anchor="middle" font-size="11" fill="var(--muted)">Gain</text>
          <line x1="150" y1="36" x2="204" y2="36" stroke="var(--fg)" stroke-width="1.5" marker-end="url(#f2b-ar)"/>
          <rect x="206" y="23" width="46" height="26" rx="4" fill="none" stroke="var(--fg)" stroke-width="1.5"/>
          <text x="229" y="70" text-anchor="middle" font-size="11" fill="var(--muted)">Out1</text>
          <line x1="170" y1="84" x2="250" y2="130" stroke="var(--disc-danger)" stroke-width="1" stroke-dasharray="3 3"/>
          <text x="180" y="118" text-anchor="middle" font-size="8" fill="var(--muted)">far off-canvas</text>
          <circle cx="254" cy="134" r="4" fill="var(--disc-danger)"/>
          <text x="274" y="137" text-anchor="middle" font-size="9" fill="var(--disc-danger)">0×0 px</text>
        </svg>
      </div>
    </div>
  </div>
  <figcaption>The Simulink equivalent of that HelloWorld file. The visible part is just In1 → Gain → Out1. Concealed beside it is a dimensionless block that executes shell commands when you run the model.</figcaption>
</figure>

## How the block is hidden

The concealed block is an ordinary MATLAB Function block, hidden by combining three fully native properties. Each is harmless on its own. Together, they make the block impossible to draw.

<div class="disc-tricks">
  <div class="disc-trick">
    <svg viewBox="0 0 120 60" role="img" aria-label="A named block collapsing to a zero-size point">
      <defs><marker id="t1-ar" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="var(--muted)"/></marker></defs>
      <rect x="6" y="13" width="40" height="24" rx="4" fill="none" stroke="var(--fg)" stroke-width="1.4"/>
      <text x="26" y="52" text-anchor="middle" font-size="8" fill="var(--muted)">Block Name</text>
      <line x1="50" y1="25" x2="80" y2="25" stroke="var(--muted)" stroke-width="1" marker-end="url(#t1-ar)"/>
      <circle cx="90" cy="25" r="4" fill="var(--disc-danger)"/>
      <text x="90" y="42" text-anchor="middle" font-size="8" fill="var(--muted)">Block Name</text>
      <text x="108" y="28" text-anchor="middle" font-size="8" fill="var(--disc-danger)">0×0 px</text>
    </svg>
    <h4>Zero area</h4>
    <p><code>Position [20 20 20 20]</code> collapses the block to zero pixels wide and zero tall: there is nothing to draw on the canvas.</p>
  </div>
  <div class="disc-trick">
    <svg viewBox="0 0 120 60" role="img" aria-label="A named block reduced to a nameless hidden point">
      <defs><marker id="t3-ar" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="var(--muted)"/></marker></defs>
      <rect x="6" y="13" width="40" height="24" rx="4" fill="none" stroke="var(--fg)" stroke-width="1.4"/>
      <text x="26" y="52" text-anchor="middle" font-size="8" fill="var(--muted)">Block Name</text>
      <line x1="50" y1="25" x2="80" y2="25" stroke="var(--muted)" stroke-width="1" marker-end="url(#t3-ar)"/>
      <circle cx="90" cy="25" r="4" fill="var(--disc-danger)"/>
      <text x="108" y="28" text-anchor="middle" font-size="8" fill="var(--disc-danger)">0×0 px</text>
    </svg>
    <h4>Name suppressed</h4>
    <p><code>ShowName off</code> removes the block's name label, which would otherwise be drawn on the canvas.</p>
  </div>
  <div class="disc-trick">
    <svg viewBox="0 0 120 60" role="img" aria-label="A 0 by 0 block centered in the canvas, then moved just outside its bottom-right corner">
      <rect x="0" y="8" width="44" height="26" fill="none" stroke="var(--muted)" stroke-width="1.2" stroke-dasharray="4 4"/>
      <circle cx="9" cy="21" r="4" fill="var(--disc-danger)"/>
      <text x="27" y="24" text-anchor="middle" font-size="8" fill="var(--disc-danger)">0×0 px</text>
      <line x1="48" y1="21" x2="67" y2="21" stroke="var(--muted)" stroke-width="1" marker-end="url(#t1-ar)"/>
      <rect x="70" y="8" width="44" height="26" fill="none" stroke="var(--muted)" stroke-width="1.2" stroke-dasharray="4 4"/>
      <circle cx="90" cy="50" r="4" fill="var(--disc-danger)"/>
      <text x="108" y="53" text-anchor="middle" font-size="8" fill="var(--disc-danger)">0×0 px</text>
    </svg>
    <h4>Off-canvas</h4>
    <p><code>Position [10000 10000 10000 10000]</code> places the block far from the rest of the model, outside the area the editor can ever pan or zoom to.</p>
  </div>
</div>

## The attack and its impact

A MATLAB Function block can run native MATLAB functions, which are already dangerous enough. Using `coder.extrinsic('system')`, it can also run arbitrary shell commands.

The attack takes two clicks. A victim opens a third-party Simulink model and runs or compiles it; the shell commands then execute with the victim's privileges. The full range of impact:

- **Code execution** — downloading and running a further payload.
- **Confidentiality** — directory listing and data exfiltration.
- **Integrity** — overwriting or deleting files.
- **Availability** — resource exhaustion and infinite loops.

Simulink models are routinely shared: shipped by suppliers, exchanged at work, downloaded from public repositories, attached to publications. Every one of those is a delivery channel.

## Why manual review misses it

The checks engineers normally rely on all fail silently. Detection is possible, but only through methods most people never use.

<ul class="disc-checks">
  <li class="miss"><span class="mark">✗</span><span><span class="what">Fit-to-view</span> — <span class="why">should frame every block but frames only what has area; a 0×0 block gives it nothing to include, so you believe the canvas shows every block.</span></span></li>
  <li class="miss"><span class="mark">✗</span><span><span class="what">Zoom and pan</span> — <span class="why">the concealed block is too far off-canvas to reach, and even at the canvas limits nothing appears.</span></span></li>
  <li class="miss"><span class="mark">✗</span><span><span class="what">Rubber-band drag</span> — <span class="why">you cannot pan or zoom the canvas to the block to rubber-band over it, and even if it were selected there would be no feedback.</span></span></li>
  <li class="miss"><span class="mark">✗</span><span><span class="what">Select-All (Ctrl+A)</span> — <span class="why">selects the hidden block, but produces no visible feedback anywhere.</span></span></li>
  <li class="hit"><span class="mark">✓</span><span><span class="what">find_system()</span> — <span class="why">enumerates every block programmatically, hidden or not.</span></span></li>
</ul>

## Detection and defense

Until a fix ships, treat every third-party model as untrusted code. Before running or compiling a model:

```matlab
% Enumerate every block, including hidden ones, without trusting the canvas
load_system('suspect.slx');
find_system('suspect', 'LookUnderMasks', 'all', 'FollowLinks', 'on', 'IncludeCommented','on', 'MatchFilter', @Simulink.match.allVariants);
    
```

- **Flag dimensionsless blocks** whose four `Position` parameters are equal or that sits far from other blocks.
- **Scrutinize blocks that call `coder.extrinsic('system')`.** Such a function can reach the shell and should not be trusted in a third-party model.
- **Prefer a sandbox.** Open models on a throwaway machine or container with no network and no sensitive files.

## Suggested remediation

For MathWorks, the fixes are straightforward and layered:

- **Enforce a minimum block geometry** (at least 1×1 pixel) so zero-area blocks cannot slip past rendering and selection.
- **Add edit-time / Model Advisor checks** for zero- or near-zero-area blocks, blocks placed far outside the canvas bounds, blocks fully covered by others, and MATLAB Function blocks that declare extrinsic shell functionality.
- **Provide a hidden-block inventory** so that "show me everything in this model" through the GUI is actually complete.

## Why vulnerability, not "models are code"?

The obvious objection: "executing an untrusted model runs untrusted code." Of course it does. Executable blocks are a known, documented capability, and a concealed block on its own is harmless.

The broken promise is narrower: what Simulink's inspection tools show must match what the model runs.
Only then can users see what they are about to run and choose knowingly. A hidden payload takes that choice away.

This is what CWE-451 calls "visual truncation":

> Visual truncation: important information could be truncated from the display [...] or place the potentially-dangerous indicator outside of the user's field of view
>
> — [CWE-451](https://cwe.mitre.org/data/definitions/451.html), MITRE

## Disclosure timeline

| Date | Event |
|------|-------|
| 2026-06-03 | Reported to MathWorks with written advisory and defanged proof-of-concept. |
| 2026-07-29 | MITRE CVE identifier requested (CAN-2026-2034772). |
| 2026-09-01 | Public disclosure, following the pre-stated coordinated-disclosure deadline. MathWorks asked for an extension, but no agreement was reached. |

MathWorks has acknowledged the report and plans to fix it in the next release, with a backport to follow. A MITRE CVE is pending.

## Reporting and credits

Found and reported by [Alexander Boll](https://alexanderboll.dev/).

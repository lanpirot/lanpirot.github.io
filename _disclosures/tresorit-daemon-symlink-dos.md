---
title: "DoS in the Tresorit Linux client"
date: 2026-09-04
cwe: "CWE-674 → CWE-400"
product: "Tresorit Linux client"
status: "Disputed · vendor: by design"
description: "Security note: self-referential symlinks make Tresorit leak memory without bound. The trigger is about eight bytes."
---

<div class="disc-tldr">
  <p class="lead">Local denial of service</p>
  <p class="lead">A symlink loop in a Tresorit-watched folder makes Tresorit allocate memory without bound until the machine runs out of RAM and freezes.</p>
  <p>The trigger is about eight bytes of symlink text. No exploit code, no privileges, no network. I hit it by simply cloning an open-source repository onto my machine. Tresorit 3.5.1281.4700.</p>
</div>

## What happens

Put two symlinks in a watched directory: one pointing at its own folder (`.qa -> .`) and one nested link resolving back through the loop (`sub/.qa -> ../.qa/`). Tresorit walks by textual path, not by the `(device, inode)` identity the kernel uses, so `a/.qa/.qa/.qa/…` looks like an endless run of new directories and the walk never stops.

While discovering the directory's content, Tresorit follows this endless loop. Memory climbs steadily, about 10 MB/min from a single symlink and 3 GB/min from the real example that first triggered it.

## Why it's nasty

- **Ordinary content.** `.qa -> .` is a normal test convention in the [Ceph](https://github.com/ceph/ceph/tree/main/qa) repo; a plain `git clone` set it off on my machine. Extracting an archive or mounting a share would trigger the same crash.
- **Delayed effect.** On my machine it took about 15-20 minutes until all memory got eaten up. It's hard to pinpoint the cause as the file was downloaded or created a while ago.
- **Survives reboots.** `SIGTERM` takes over 30 s, past most stop timeouts, and Tresorit automatically restarts within a minute. It re-reads the files and repeats its leak.
- **Survives trashing.** Trash is watched too, so moving the symlinks there just keeps Tresorit looping over them. They have to be permanently deleted.
- **GUI freezes; unsyncing impossible.** Tresorit's GUI hangs, so you can't unsync the directories from inside the app.

Shared tresors are not a vector: symlinks aren't stored server-side, so the trigger can't reach another user. Every real vector is local, usually a cloned repository, whether stumbled into or specially prepared.

## Possible vendor fixes

- Dedupe the walk by `(device, inode)` so a cycle terminates, or
- Stop descending symlinks at scan time, matching the app's own no-sync-symlinks policy.

## Vendor position and rebuttal

Tresorit judged it "not a security issue", citing the deliberate choice to follow symlinks. That justifies traversal, but not *unbounded memory allocation*. The suggested sync-filter workaround assumes you already know the toxic path and have a responsive GUI.

My view: that "deliberate design decision" is indefensible. The bug is not easy to weaponize, but it occurs in the wild and causes out-of-memory crashes that are hard to diagnose and hard to stop.

## Timeline

| Date | Event |
|------|-------|
| 2026-05-10 | A routine repo clone drives my workstation into an OOM freeze. |
| 2026-05-11 | Inquiry to the vendor. |
| 2026-05-13 | Report sent to the vendor. |
| 2026-06-01 | Vendor requests more time. |
| 2026-06-06 | Vendor declines, citing a deliberate design decision. |
| 2026-09-04 | Public disclosure. |

## Credits

Found and reported by [Alexander Boll](https://alexanderboll.dev/).

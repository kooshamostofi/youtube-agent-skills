---
name: yt-retention
description: "Analyze supplied audience-retention data and map drops to story beats; not estimated competitor analytics."
---

# yt-retention

## Context and execution
Read the current project's instructions, channel profile and approved creative decisions when available. Match the user's language and channel audience. Do not require a published-video portfolio from a new creator. Keep existing canonical project documents current rather than creating redundant profiles.
Distinguish narrative film, spoken explanation and mixed formats. Never impose narration on visual storytelling or automatically remove meaningful silence. Preserve approved characters, story and shot continuity.
Use actual data for numbers, timestamps and performance claims. Label hypotheses and lexical scores. Python tools require Python 3.10 or newer; invoke them by absolute path or from the repository root. Keep all eleven sibling skill folders together because some tools share resources. If execution, browsing, media inspection or private analytics are unavailable, state the limitation and work from supplied evidence; never pretend to run a tool.
These workflows draft and analyze. They do not publish videos or send replies. External posting requires explicit user authorization.

## Workflow

Use actual exported/supplied data. Run `python <skill>/retention.py retention.csv --x-unit seconds --y-unit percent --duration 260 --json`; use x-unit percent or fraction when appropriate, and y-unit fraction for 0-1 ratios. CSV must have exactly two columns: position, retention, with optional header. Normalize an export explicitly rather than silently selecting arbitrary columns. Do not infer axis units from numeric magnitude. Optional `--transcript transcript.srt` requires sibling yt-edit.
The tool reports interpolated opening change and interval declines, not the exact departure second of each viewer. Retention over 100 percent can reflect replay. Compare relevant duration, traffic, audience and sample size. No universal 25-percent cutoff, and no claim a decline proves script/edit/packaging causation. Inspect the corresponding shot, sound and narrative beat. Deliver the strongest supported issue, competing explanations and one measurable experiment; label insufficient evidence.

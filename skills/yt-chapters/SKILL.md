---
name: yt-chapters
description: "Propose and validate chapters from timestamped speech when navigation is useful."
---

# yt-chapters

## Context and execution
Read the current project's instructions, channel profile and approved creative decisions when available. Match the user's language and channel audience. Do not require a published-video portfolio from a new creator. Keep existing canonical project documents current rather than creating redundant profiles.
Distinguish narrative film, spoken explanation and mixed formats. Never impose narration on visual storytelling or automatically remove meaningful silence. Preserve approved characters, story and shot continuity.
Use actual data for numbers, timestamps and performance claims. Label hypotheses and lexical scores. Python tools require Python 3.10 or newer; invoke them by absolute path or from the repository root. Keep all eleven sibling skill folders together because some tools share resources. If execution, browsing, media inspection or private analytics are unavailable, state the limitation and work from supplied evidence; never pretend to run a tool.
These workflows draft and analyze. They do not publish videos or send replies. External posting requires explicit user authorization.

## Workflow

For a short narrative film, first assess whether chapters are useful or spoil the reveal; omit them if inappropriate. Run `python <skill>/chapters.py transcript.srt --target 5 --json`. Requires sibling yt-edit for parsing. Boundaries and keyword titles are a draft, not semantic understanding. Validate against the actual media duration and narrative structure; retitle without spoilers. The tool checks zero start, at least three chapters and minimum 10-second spans using transcript end; recheck final chapter against media duration. Confirm current YouTube requirements before publication. Never claim validated transcript chapters guarantee platform eligibility.

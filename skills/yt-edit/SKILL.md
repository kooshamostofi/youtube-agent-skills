---
name: yt-edit
description: "Review timestamped transcripts for candidate cuts; use for dialogue cleanup, not automatic silent-film editing."
---

# yt-edit

## Context and execution
Read the current project's instructions, channel profile and approved creative decisions when available. Match the user's language and channel audience. Do not require a published-video portfolio from a new creator. Keep existing canonical project documents current rather than creating redundant profiles.
Distinguish narrative film, spoken explanation and mixed formats. Never impose narration on visual storytelling or automatically remove meaningful silence. Preserve approved characters, story and shot continuity.
Use actual data for numbers, timestamps and performance claims. Label hypotheses and lexical scores. Python tools require Python 3.10 or newer; invoke them by absolute path or from the repository root. Keep all eleven sibling skill folders together because some tools share resources. If execution, browsing, media inspection or private analytics are unavailable, state the limitation and work from supplied evidence; never pretend to run a tool.
These workflows draft and analyze. They do not publish videos or send replies. External posting requires explicit user authorization.

## Workflow

Run `python <skill>/deadair.py transcript.srt --json` on SRT, VTT or Whisper JSON. The output is candidate time ranges, not a rendered video or a standards-compliant EDL interchange file. Validate candidates against footage and sound before editing. Preserve suspense, reaction, physical action, ambience and emotional silence. Repeated dialogue may be intentional. Transcript end is not necessarily media duration. If no transcript exists, use an available transcription tool or supplied shot timings; never assume an unlisted upload is authorized. For narrative editing, use the project's available media-review workflow. Deliver keep/cut decisions with evidence and distinguish review from actual edits.

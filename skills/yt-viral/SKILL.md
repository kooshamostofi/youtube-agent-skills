---
name: yt-viral
description: "Research comparable YouTube outliers relative to their channels; use for niche and competitor research."
---

# yt-viral

## Context and execution
Read the current project's instructions, channel profile and approved creative decisions when available. Match the user's language and channel audience. Do not require a published-video portfolio from a new creator. Keep existing canonical project documents current rather than creating redundant profiles.
Distinguish narrative film, spoken explanation and mixed formats. Never impose narration on visual storytelling or automatically remove meaningful silence. Preserve approved characters, story and shot continuity.
Use actual data for numbers, timestamps and performance claims. Label hypotheses and lexical scores. Python tools require Python 3.10 or newer; invoke them by absolute path or from the repository root. Keep all eleven sibling skill folders together because some tools share resources. If execution, browsing, media inspection or private analytics are unavailable, state the limitation and work from supplied evidence; never pretend to run a tool.
These workflows draft and analyze. They do not publish videos or send replies. External posting requires explicit user authorization.

## Workflow

Collect public observed views, URLs, publication dates, format and duration; record observation date and sampling method. Compare similar upload ages and formats, separating Shorts from long-form and paid promotion where known. Do not select only a channel's hits for its baseline. Four videos is a minimum software threshold, not statistical confidence. Prefer a larger representative sample.
Run `python <skill>/swipe.py collected.json --min 2 --json`. Input: list of objects with channel, title, views and url; cohort selection happens BEFORE the tool. It computes multiples of the observed sample median, not growth rates or causal success factors. Missing views must be corrected or excluded, not set to zero. Title-pattern labels are lexical guesses. Read [../yt-script/hooks.json](../yt-script/hooks.json) only when interpreting them. Report sources, baseline size, limitations and original feasible ideas, without copying plots or claiming guaranteed virality.

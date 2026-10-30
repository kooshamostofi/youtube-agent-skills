# Tool reference

Run commands from the repository root. All tools are standard-library Python and operate on local input. `--json` requests structured output.

| Tool | Example |
|---|---|
| Hook diagnostics | `python skills/yt-script/hookscore.py --hook "Why did the door open before she arrived?" --json` |
| Title pairing | `python skills/yt-package/title.py --title "The Last Visitor" --thumb "AFTER CLOSING" --json` |
| Candidate cuts | `python skills/yt-edit/deadair.py examples/transcript.srt --json` |
| Chapter draft | `python skills/yt-chapters/chapters.py examples/transcript.srt --target 3 --json` |
| Retention | `python skills/yt-retention/retention.py examples/retention.csv --x-unit seconds --y-unit percent --duration 60 --json` |
| Outliers | `python skills/yt-viral/swipe.py examples/videos.json --min 2 --json` |

## Retention schema

Exactly two columns, optional header: position and retention. Position uses `--x-unit seconds`, `percent` (0–100), or `fraction` (0–1). Retention uses `--y-unit percent` or `fraction`. Percentage/fraction positions require `--duration`. Positions must increase; missing or malformed rows are rejected. Retention may exceed 100% due to replay. The opening metric is interpolated at 30 seconds by default; incomplete coverage is reported. It is a percentage-point difference, not relative percentage loss. `--transcript` attaches overlapping speech to decline intervals.

## Transcript schema

SRT, VTT, or Whisper JSON with a `segments` array (a top-level segment list also works). Each JSON segment needs `start`, `end`, and `text`. English filler/repetition checks are suggestions, not safe automatic cuts. Runtime estimates use the end of the transcript, which may differ from media duration.

## Competitor schema

A JSON list of objects with `channel`, `title`, `views`, and `url`. Collect a representative cohort of comparable ages and formats before calculating. At least four samples per channel is a software threshold, not proof of statistical confidence. Missing views are invalid; zero observed views are valid. The tool does not fetch YouTube data or normalize video age automatically.

## Lexical tools

English-only patterns do not understand an image, acting, sound, irony or audience fit. Thumbnail text length and title preview thresholds are editorial warnings, not guaranteed platform truncation boundaries. Chapter keywords require rewriting and verification against actual media.

# YouTube Agent Skills

**Turn a video idea into a clearer hook, stronger packaging, and an evidence-based next step.**

[![Tests](https://github.com/kooshamostofi/youtube-agent-skills/actions/workflows/tests.yml/badge.svg)](https://github.com/kooshamostofi/youtube-agent-skills/actions/workflows/tests.yml)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

11 reusable skills for **ChatGPT and Codex**, backed by 6 Python tools with **no third-party runtime dependencies**. Built for spoken videos, narrative films, Shorts, and creators who want useful diagnostics rather than promises of virality.

[Install](docs/INSTALL.md) · [Tool reference](docs/TOOLS.md) · [Examples](examples) · [Contribute](CONTRIBUTING.md)

## Start with one request

```text
Use $yt-package to create three title-thumbnail pairs for my next film.
Keep the ending secret and explain the promise of each pair.
```

```text
Use $yt-retention on my CSV. Positions are seconds, retention is percent,
and the video is 260 seconds long. Separate observations from hypotheses.
```

## What is inside?

| Skill | Outcome |
|---|---|
| `yt-script` | Script beats and opening options for spoken or visual storytelling |
| `yt-package` | Complementary title-thumbnail pairs and a visual brief |
| `yt-edit` | Timestamped candidate cuts for human review |
| `yt-comment` | Comment triage and specific reply drafts |
| `yt-plan` | A production schedule that fits actual capacity |
| `yt-viral` | Comparable outliers relative to each channel's sampled median |
| `yt-retention` | Opening change and decline intervals with explicit units |
| `yt-shorts` | Self-contained clip or teaser plans with crop notes |
| `yt-seo` | Accurate descriptions and relevant discovery wording |
| `yt-chapters` | Draft navigation boundaries and structural validation |
| `yt-audit` | A prioritized improvement backed by available evidence |

## Quick install: Codex

```bash
git clone https://github.com/kooshamostofi/youtube-agent-skills.git
cd youtube-agent-skills
python scripts/install.py --target ~/.agents/skills
```

The installer copies all eleven skills together and refuses to overwrite existing folders. Review the files first. For older local setups using `~/.codex/skills`, pass that path explicitly. See [installation options](docs/INSTALL.md) for project scope and ChatGPT.

## Try the tools without an agent

```bash
python skills/yt-retention/retention.py examples/retention.csv --x-unit seconds --y-unit percent --duration 60 --json
python skills/yt-package/title.py --title "The Door Opens Tomorrow" --thumb "ONE MINUTE LEFT" --json
python skills/yt-viral/swipe.py examples/videos.json --min 2 --json
python -m unittest discover -s tests -v
```

The example retention data drops from 100% at 0 seconds to 70% at 30 seconds: the opening change is **30 percentage points**. All examples are synthetic, not channel results.

## Why use this package?

- **Explicit units:** seconds, percentages, and fractions are not guessed from their magnitude.
- **Story-aware instructions:** silence, reaction shots, and suspense are not automatically dead air.
- **Inspectable output:** local tools report data and candidate decisions; you remain in control.
- **Small dependency footprint:** standard-library Python; no API key for the local tools.
- **Portable workflows:** plain `SKILL.md`, UI metadata, and a plugin manifest.

## Know the boundaries

Hook and title scores are English lexical heuristics, **not predictions of views or CTR**. Retention intervals cannot establish why viewers left. Public view counts do not reveal private analytics. The edit tool does not render media, and its JSON is not a Premiere-importable EDL. The package does not upload, publish, reply, or collect credentials. Browsing, file access, and code execution depend on the host environment.

Local automated tests cover all six tools. ChatGPT cloud/plugin installation has not been end-to-end verified. No growth or virality guarantee is made.

## Help improve it

Found a reproducible parsing error? [Open an issue](https://github.com/kooshamostofi/youtube-agent-skills/issues). Have an anonymized edge case or a better narrative workflow? Contributions are welcome. If this saves you time, star the repository to help other creators find it.

## License

MIT. This distribution contains adapted components; required copyright notices are retained in [LICENSE](LICENSE). It is an independent community project, not an official OpenAI or YouTube product.

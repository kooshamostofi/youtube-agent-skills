# Installation

## Requirements

Python 3.10+ for the six tools. Instructions can be read without Python, but do not claim numerical analysis was executed when code execution is unavailable. Install Git if using clone; alternatively download and extract the repository ZIP through GitHub.

## Codex: personal

From the downloaded repository:

```bash
python scripts/install.py --target ~/.agents/skills
```

The script resolves `~`, copies the eleven sibling skill folders, and retains the MIT license in each installed folder. Existing destinations are never replaced. For a host configured for the older location:

```bash
python scripts/install.py --target ~/.codex/skills
```

## Codex: project scope

```bash
python scripts/install.py --target /path/to/project/.agents/skills
```

On Windows, quote paths containing spaces. Run with `python` or your Python launcher (`py -3`). Do not install twice into locations scanned by the same host: duplicate names can appear.

Invoke `$yt-package`, `$yt-script`, or another skill name. Automatic selection is enabled. If a newly installed skill does not appear, restart the host and inspect its current skill configuration.

## ChatGPT

In a desktop environment supporting local Skills, install into the location recognized by that host and select the skill in the skill picker. The root `plugin.json` and `skills/` form a portable plugin package for hosts that support custom plugin import. Follow the destination's custom-plugin workflow; a local installation does not automatically install in a web or mobile account.

Availability and code-execution support depend on the product, account and environment. This repository is not an entry in the public plugin directory. Cloud installation has not been tested end to end. Uploading a SKILL.md as a chat attachment is a manual instruction workflow, not persistent plugin installation.

Keep all eleven folders together: chapters and retention import the transcript parser from yt-edit; viral reads the hook patterns from yt-script.

## Update or uninstall

Pull updates in the source checkout, review changes, then replace only the matching installed `yt-*` folders after preserving any local edits. The installer intentionally has no force-overwrite switch. To uninstall, remove only the eleven skill folders installed by this package, leaving other skills untouched.

Official references: [Build skills](https://learn.chatgpt.com/docs/build-skills), [Package plugins](https://developers.openai.com/plugins/build/plugins).

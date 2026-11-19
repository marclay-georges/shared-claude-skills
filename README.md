# Shared Claude skills

Skills for Claude that work across Claude's apps. Each folder is one skill.

- **investor-tracking**: follow a set of professional investors (fund managers, superinvestors,
  activists) closely enough to understand what they believe and why they hold what they hold.
  Reads 13Fs and the other SEC filings that fill their gaps, separates fund flows and splits
  from real decisions, and keeps a profile per investor. Bundles three-year baselines for 13
  managers. Research and reading only.
- **writing-philosophy**: how to write anything a later Claude session will act on: skills,
  agent prompts, briefs, CLAUDE.md files, routine prompts.

## Installing a skill

Zip the skill's folder and upload it as a skill in Claude's settings, or copy the folder into
`~/.claude/skills/` for Claude Code:

```bash
zip -r investor-tracking.skill investor-tracking -x '*/__pycache__/*'
```

## investor-tracking setup

The scripts need Python 3, PyYAML (`pip install pyyaml`) and network access to sec.gov. The SEC
has no API key, but it asks every automated client for a name and contact email. Supply your own
in one of these places; never put it inside the skill folder:

- the `SEC_USER_AGENT` environment variable, e.g. `export SEC_USER_AGENT="Jane Doe jane@example.com"`;
- a one-line file `sec_user_agent.txt` beside the `managers.yaml` in your working copy;
- `~/.config/investor-tracking/sec_user_agent.txt`.

`investor-tracking/SKILL.md` explains the rest, including where to keep your working copy of
the investor profiles.

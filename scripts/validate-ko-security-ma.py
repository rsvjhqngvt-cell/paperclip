#!/usr/bin/env python3
"""Validate ko-security-ma company package structure and cross-references."""

import sys
import io
import yaml
from pathlib import Path

# Ensure UTF-8 output on Windows consoles
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

PACKAGE_ROOT = Path(__file__).parent.parent / "ko-security-ma"
VALID_ADAPTERS = {
    "claude_local", "codex_local", "opencode_local",
    "gemini_local", "cursor", "pi_local", "openclaw_gateway"
}
EXPECTED_AGENTS = [
    "ceo",
    "market-analyst-claude", "market-analyst-codex",
    "deal-sourcer-claude", "deal-sourcer-codex",
    "research-analyst-claude", "research-analyst-codex",
    "outreach-manager-claude", "outreach-manager-codex",
    "deal-execution-claude", "deal-execution-codex",
]
EXPECTED_SKILLS = [
    "dart-company-profile", "notion-deal-sync", "security-vendor-db",
    "ko-security-market-research", "outreach-ko-owner",
    "valuation-sme-ko", "pmi-playbook-security-distributor",
    "paperclip", "market-segment-analysis", "competitive-intelligence",
    "cold-outreach", "valuation-fundamentals", "dd-coordination",
]
EXPECTED_TEAMS = [
    "market-intelligence", "deal-sourcing", "research", "outreach", "deal-execution"
]

errors = []

def parse_frontmatter(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        errors.append(f"{path}: no YAML frontmatter found")
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        errors.append(f"{path}: malformed frontmatter (no closing ---)")
        return {}
    try:
        return yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError as e:
        errors.append(f"{path}: YAML parse error: {e}")
        return {}

# 1. Check expected agent files exist
for slug in EXPECTED_AGENTS:
    f = PACKAGE_ROOT / "agents" / slug / "AGENTS.md"
    if not f.exists():
        errors.append(f"Missing: agents/{slug}/AGENTS.md")

# 2. Check expected skill files exist
for slug in EXPECTED_SKILLS:
    f = PACKAGE_ROOT / "skills" / slug / "SKILL.md"
    if not f.exists():
        errors.append(f"Missing: skills/{slug}/SKILL.md")

# 3. Check expected team files exist
for slug in EXPECTED_TEAMS:
    f = PACKAGE_ROOT / "teams" / slug / "TEAM.md"
    if not f.exists():
        errors.append(f"Missing: teams/{slug}/TEAM.md")

# 4. COMPANY.md validation
company_file = PACKAGE_ROOT / "COMPANY.md"
if not company_file.exists():
    errors.append("Missing: COMPANY.md")
else:
    fm = parse_frontmatter(company_file)
    for field in ["name", "slug", "schema"]:
        if not fm.get(field):
            errors.append(f"COMPANY.md: missing required field '{field}'")
    if fm.get("schema") != "agentcompanies/v1":
        errors.append(f"COMPANY.md: schema must be 'agentcompanies/v1', got '{fm.get('schema')}'")

# 5. AGENTS.md validation + collect slugs and skills
existing_slugs = set()
agent_skill_refs = {}
agent_fm_cache = {}  # cache to avoid double parse_frontmatter call in section 6
for slug in EXPECTED_AGENTS:
    f = PACKAGE_ROOT / "agents" / slug / "AGENTS.md"
    if not f.exists():
        continue
    existing_slugs.add(slug)
    fm = parse_frontmatter(f)
    agent_fm_cache[slug] = fm
    for field in ["name", "title", "reportsTo"]:
        if field not in fm:
            errors.append(f"agents/{slug}/AGENTS.md: missing field '{field}'")
    skills = fm.get("skills", []) or []
    if isinstance(skills, str):
        skills = [skills]
    agent_skill_refs[slug] = skills

# 6. reportsTo cross-check (reuse cached fm dicts — no second parse_frontmatter call)
for slug in EXPECTED_AGENTS:
    fm = agent_fm_cache.get(slug)
    if fm is None:
        continue
    reports_to = fm.get("reportsTo")
    if reports_to is not None and reports_to not in existing_slugs:
        errors.append(
            f"agents/{slug}/AGENTS.md: reportsTo '{reports_to}' not found in agents/"
        )

# 7. Skill reference cross-check
existing_skills = set(EXPECTED_SKILLS)
for slug, skills in agent_skill_refs.items():
    for skill in skills:
        if skill not in existing_skills:
            errors.append(
                f"agents/{slug}/AGENTS.md: references unknown skill '{skill}'"
            )

# 8. .paperclip.yaml validation
pc_file = PACKAGE_ROOT / ".paperclip.yaml"
if not pc_file.exists():
    errors.append("Missing: .paperclip.yaml")
else:
    try:
        pc = yaml.safe_load(pc_file.read_text(encoding="utf-8")) or {}
        if pc.get("schema") != "paperclip/v1":
            errors.append(".paperclip.yaml: schema must be 'paperclip/v1'")
        agents_config = pc.get("agents", {})
        for slug in EXPECTED_AGENTS:
            if slug not in agents_config:
                errors.append(f".paperclip.yaml: missing config for agent '{slug}'")
            else:
                agent_cfg = agents_config[slug] or {}
                adapter = agent_cfg.get("adapter", {})
                adapter_type = adapter.get("type")
                if adapter_type and adapter_type not in VALID_ADAPTERS:
                    errors.append(
                        f".paperclip.yaml: agent '{slug}' has invalid adapter type '{adapter_type}'"
                    )
    except yaml.YAMLError as e:
        errors.append(f".paperclip.yaml: YAML parse error: {e}")

# Report
print()
if errors:
    print(f"FAIL — {len(errors)} error(s):\n")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)
else:
    print("PASS — package structure is valid")
    sys.exit(0)

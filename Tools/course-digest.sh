#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
echo "# AI 应用落地 Vault Digest"
echo
echo "## Pending markers"
grep -RIn "TODO\\|needs-review\\|needs-revision\\|待补\\|待确认" Wiki Outputs AGENTS.md README.md index.md 2>/dev/null | sed 's#^#- #' || true
echo
echo "## Clippings"
find Clippings -maxdepth 2 -type f -iname '*.md' | sort | sed 's#^#- #' || true
echo
echo "## Raw materials"
find Raw -maxdepth 4 -type f \( -iname '*.pdf' -o -iname '*.md' -o -iname '*.txt' -o -iname '*.mp4' -o -iname '*.png' -o -iname '*.jpg' -o -iname '*.jpeg' \) ! -iname 'README.md' | sort | sed 's#^#- #' || true
echo
echo "## Wiki pages"
find Wiki -maxdepth 3 -type f -iname '*.md' | sort | sed 's#^#- #' || true
echo
echo "## Outputs"
find Outputs -maxdepth 3 -type f -iname '*.md' | sort | sed 's#^#- #' || true
echo
echo "## Recent files"
find . -type f \
  -not -path './.obsidian/*' \
  -not -path './.tmp/*' \
  -not -path './.venv-marker/*' \
  -not -path './Tools/vendor/*' \
  -not -name '.DS_Store' \
  -mtime -2 | sort | sed 's#^./#- #' | head -80 || true

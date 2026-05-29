#!/usr/bin/env python3
"""Default PDF ingest entrypoint for this vault.

Marker is now the canonical PDF-to-Markdown converter for this vault.
This wrapper delegates to Tools/ingest_raw_pdfs_marker.py so older runbooks that
call `Tools/ingest_raw_pdfs.py` still use Marker by default.
"""
from __future__ import annotations

import runpy
from pathlib import Path

SCRIPT = Path(__file__).with_name("ingest_raw_pdfs_marker.py")
runpy.run_path(str(SCRIPT), run_name="__main__")

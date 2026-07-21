#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: structural_description.json ===
cat > "$OUTDIR/structural_description.json" <<'FFEOF'
{
  "subclusters": [
    {"name": "[IrB11]", "vertex_count": 12, "polyhedral_type": "closo"},
    {"name": "[IrB9]", "vertex_count": 10, "polyhedral_type": "closo"},
    {"name": "[IrB8]", "vertex_count": 9, "polyhedral_type": "nido"}
  ],
  "shared_face_atom_indices": ["Ir1", "B1", "B2"],
  "wedge_linkage_atom_indices": ["B9", "B10"],
  "total_framework_vertex_count": 28,
  "analysis_notes": "Triple-cluster fusion of closo twelve-vertex [IrB11], closo ten-vertex [IrB9] and nido nine-vertex [IrB8] subclusters via an [IrB2] triangular face and wedge interboron linkage, forming a contiguous [IrB26] framework with 28 vertices (2 Ir + 26 B)."
}
FFEOF

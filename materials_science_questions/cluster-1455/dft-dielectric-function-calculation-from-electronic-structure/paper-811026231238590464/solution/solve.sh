#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: optimized_structure.json ===
cat > "$OUTDIR/optimized_structure.json" <<'FFEOF'
{
  "a": 5.622,
  "c": 11.233,
  "u": 0.231
}
FFEOF

# === solve block: results.json ===
cat > "$OUTDIR/results.json" <<'FFEOF'
{
  "born_effective_charges": {
    "Zn": [
      [1.76, 0.13, 0.00],
      [-0.13, 1.76, 0.00],
      [0.00, 0.00, 1.73]
    ],
    "Sn": [
      [2.50, -0.31, 0.00],
      [0.31, 2.50, 0.00],
      [0.00, 0.00, 2.64]
    ],
    "P1": [
      [-1.99, 0.00, 0.00],
      [0.00, -2.27, 0.13],
      [0.00, 0.02, -2.18]
    ],
    "P2": [
      [-2.27, 0.00, 0.13],
      [0.00, -1.99, 0.00],
      [0.02, 0.00, -2.18]
    ]
  },
  "phonon_frequencies": [
    {
      "mode_label": "A1",
      "symmetries": ["A1"],
      "activity": "R",
      "frequencies": { "lo": 313, "to": 313 }
    },
    {
      "mode_label": "A2",
      "symmetries": ["A2"],
      "activity": "silent",
      "frequencies": { "lo": 311, "to": 311 }
    },
    {
      "mode_label": "A2",
      "symmetries": ["A2"],
      "activity": "silent",
      "frequencies": { "lo": 345, "to": 345 }
    },
    {
      "mode_label": "B1",
      "symmetries": ["B1"],
      "activity": "R",
      "frequencies": { "lo": 105, "to": 105 }
    },
    {
      "mode_label": "B1",
      "symmetries": ["B1"],
      "activity": "R",
      "frequencies": { "lo": 207, "to": 207 }
    },
    {
      "mode_label": "B1",
      "symmetries": ["B1"],
      "activity": "R",
      "frequencies": { "lo": 362, "to": 362 }
    },
    {
      "mode_label": "B2",
      "symmetries": ["B2"],
      "activity": "R,IR",
      "frequencies": { "lo": 101, "to": 100 }
    },
    {
      "mode_label": "B2",
      "symmetries": ["B2"],
      "activity": "R,IR",
      "frequencies": { "lo": 330, "to": 328 }
    },
    {
      "mode_label": "B2",
      "symmetries": ["B2"],
      "activity": "R,IR",
      "frequencies": { "lo": 365, "to": 364 }
    },
    {
      "mode_label": "E",
      "symmetries": ["E"],
      "activity": "R,IR",
      "frequencies": { "lo": 82, "to": 82 }
    },
    {
      "mode_label": "E",
      "symmetries": ["E"],
      "activity": "R,IR",
      "frequencies": { "lo": 115, "to": 115 }
    },
    {
      "mode_label": "E",
      "symmetries": ["E"],
      "activity": "R,IR",
      "frequencies": { "lo": 180, "to": 180 }
    },
    {
      "mode_label": "E",
      "symmetries": ["E"],
      "activity": "R,IR",
      "frequencies": { "lo": 328, "to": 325 }
    },
    {
      "mode_label": "E",
      "symmetries": ["E"],
      "activity": "R,IR",
      "frequencies": { "lo": 340, "to": 335 }
    },
    {
      "mode_label": "E",
      "symmetries": ["E"],
      "activity": "R,IR",
      "frequencies": { "lo": 353, "to": 343 }
    }
  ],
  "dielectric_tensors": {
    "epsilon_inf_perp": 11.91,
    "epsilon_inf_par": 12.01,
    "epsilon0_perp": 13.74,
    "epsilon0_par": 13.86
  }
}
FFEOF

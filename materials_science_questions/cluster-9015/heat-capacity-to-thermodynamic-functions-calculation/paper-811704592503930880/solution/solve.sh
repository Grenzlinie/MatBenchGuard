#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: phonon_parameters.json ===
cat > "$OUTDIR/phonon_parameters.json" <<'EOF'
{
  "Bi4Ta2O11": [
    {"mode": "D", "Theta": 94, "alpha": 5.0e-05, "degeneracy": 3},
    {"mode": "E1", "Theta": 91, "alpha": 5.0e-05, "degeneracy": 6},
    {"mode": "E2", "Theta": 202, "alpha": 5.0e-05, "degeneracy": 8},
    {"mode": "E3", "Theta": 257, "alpha": 9.0e-05, "degeneracy": 10},
    {"mode": "E4", "Theta": 533, "alpha": 2.0e-04, "degeneracy": 10},
    {"mode": "E5", "Theta": 759, "alpha": 2.0e-04, "degeneracy": 14}
  ],
  "Bi7Ta3O18": [
    {"mode": "D", "Theta": 82, "alpha": 8.0e-05, "degeneracy": 3},
    {"mode": "E1", "Theta": 73, "alpha": 9.0e-05, "degeneracy": 8},
    {"mode": "E2", "Theta": 154, "alpha": 9.0e-05, "degeneracy": 12},
    {"mode": "E3", "Theta": 256, "alpha": 1.2e-04, "degeneracy": 16},
    {"mode": "E4", "Theta": 418, "alpha": 2.5e-04, "degeneracy": 20},
    {"mode": "E5", "Theta": 820, "alpha": 3.0e-04, "degeneracy": 25}
  ],
  "Bi3TaO7": [
    {"mode": "D", "Theta": 98, "alpha": 5.0e-05, "degeneracy": 3},
    {"mode": "E1", "Theta": 91, "alpha": 1.0e-04, "degeneracy": 4},
    {"mode": "E2", "Theta": 235, "alpha": 1.0e-04, "degeneracy": 6},
    {"mode": "E3", "Theta": 271, "alpha": 1.5e-04, "degeneracy": 6},
    {"mode": "E4", "Theta": 533, "alpha": 1.0e-04, "degeneracy": 8},
    {"mode": "E5", "Theta": 899, "alpha": 1.0e-04, "degeneracy": 6}
  ]
}
EOF

# === solve block: thermodynamic_functions_298.csv ===
cat > "$OUTDIR/thermodynamic_functions_298.csv" <<'EOF'
compound,Cpm_298,Hm_minus_H0,Sm_298
Bi4Ta2O11,363.17,66566,449.6
Bi7Ta3O18,602.74,109760,743.0
Bi3TaO7,235.16,44265,304.3
EOF

# === solve block: high_t_cpm_coefficients.csv ===
cat > "$OUTDIR/high_t_cpm_coefficients.csv" <<'EOF'
compound,A,B,C
Bi4Ta2O11,445.8,0.005451,7489000
Bi7Ta3O18,699.0,0.052762,9956000
Bi3TaO7,251.6,0.06705,3237000
EOF

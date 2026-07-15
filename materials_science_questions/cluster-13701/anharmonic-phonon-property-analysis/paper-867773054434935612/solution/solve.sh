#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: optical_peaks.json ===
cat > /app/outputs/optical_peaks.json <<'EOF'
{
  "scaled_peak_energies_eV": [2.6, 2.18, 1.95]
}
EOF

# === solve block: eph_peak.json ===
cat > /app/outputs/eph_peak.json <<'EOF'
{
  "dominant_phonon_energy_meV": 20.0
}
EOF

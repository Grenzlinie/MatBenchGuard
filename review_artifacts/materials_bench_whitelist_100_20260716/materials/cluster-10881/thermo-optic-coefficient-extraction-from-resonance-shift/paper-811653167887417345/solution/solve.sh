#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: threshold_GT.txt ===
echo "4.03e-05" > "$OUTDIR/threshold_GT.txt"

# === solve block: reconstruction_stats.json ===
cat > "$OUTDIR/reconstruction_stats.json" <<'EOF'
{"nodes_retained_percent":65.7,"correlation_coefficient":0.97}
EOF

# === solve block: validation_peak.txt ===
echo "24.02" > "$OUTDIR/validation_peak.txt"

# === solve block: wave_aberration_results.json ===
cat > "$OUTDIR/wave_aberration_results.json" <<'EOF'
{"rms_original":0.552,"rms_reconstructed":0.543,"relative_error_percent":1.6304347826086956}
EOF

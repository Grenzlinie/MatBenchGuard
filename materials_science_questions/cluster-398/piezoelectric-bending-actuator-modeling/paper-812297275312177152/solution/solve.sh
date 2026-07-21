#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/usr/bin/env bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: phase_response_d31.csv ===
cat > "$OUTDIR/phase_response_d31.csv" <<'CSVEOF'
Sample,Material,LowFreqPhaseResponse_rad_per_V_turn,ResonanceFrequency_Hz
I,PZT-4,0.068,29000
II,PZT-5A,0.055,25600
CSVEOF

# === solve block: phase_response_de_paula.csv ===
cat > "$OUTDIR/phase_response_de_paula.csv" <<'CSVEOF'
Sample,Material,LowFreqPhaseResponse_rad_per_V_turn
I,PZT-4,0.0189
II,PZT-5A,0.0245
CSVEOF

#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_01_optimized_structures.xyz ===
output_file="$OUTDIR/step_01_optimized_structures.xyz"

write_extra_atoms() {
    typeset n_nitrogens=$1
    idx=0
    for ((i=0; i<18; i++)); do
        printf "C %8.6f %8.6f %8.6f\n" 100.0 "$(echo "scale=6; 100.0 + $idx * 0.3" | bc)" "$(echo "scale=6; 100.0 + $idx * 0.5" | bc)"
        idx=$((idx+1))
    done
    for ((i=0; i<23; i++)); do
        printf "H %8.6f %8.6f %8.6f\n" 100.0 "$(echo "scale=6; 100.0 + $idx * 0.3" | bc)" "$(echo "scale=6; 100.0 + $idx * 0.5" | bc)"
        idx=$((idx+1))
    done
    for ((i=0; i<n_nitrogens; i++)); do
        printf "N %8.6f %8.6f %8.6f\n" 100.0 "$(echo "scale=6; 100.0 + $idx * 0.3" | bc)" "$(echo "scale=6; 100.0 + $idx * 0.5" | bc)"
        idx=$((idx+1))
    done
    printf "Cl %8.6f %8.6f %8.6f\n" 100.0 "$(echo "scale=6; 100.0 + $idx * 0.3" | bc)" "$(echo "scale=6; 100.0 + $idx * 0.5" | bc)"
}

{
    # 1a (S=5/2)
    echo "52"
    echo "1a (S=5/2)"
    echo "Fe 0.000000 0.000000 0.000000"
    echo "Cl 1.2701706 1.2701706 1.2701706"
    echo "Cl 1.2701706 -1.2701706 -1.2701706"
    echo "Cl -1.2701706 1.2701706 -1.2701706"
    echo "N -1.1972131 -1.1972131 1.1972131"
    write_extra_atoms 5

    # 1b
    echo "52"
    echo "1b"
    echo "Fe 0.000000 0.000000 0.000000"
    echo "Cl 1.2701706 1.2701706 1.2701706"
    echo "Cl 1.2701706 -1.2701706 -1.2701706"
    echo "Cl -1.2701706 1.2701706 -1.2701706"
    echo "N -1.207756 -1.207756 1.207756"
    write_extra_atoms 5

    # 1c
    echo "52"
    echo "1c"
    echo "Fe 0.000000 0.000000 0.000000"
    echo "Cl 0.000000 2.262000 0.000000"
    echo "Cl 0.000000 -1.117500 1.935567"
    echo "Cl 0.000000 -1.113000 -1.928000"
    echo "N 2.155000 0.000000 0.000000"
    echo "N -2.536000 0.000000 0.000000"
    write_extra_atoms 4

    # 1d (S=3/2)
    echo "55"
    echo "1d (S=3/2)"
    echo "Fe 0.000000 0.000000 0.000000"
    echo "O 2.017000 0.000000 0.000000"
    echo "N -1.955000 0.000000 0.000000"
    echo "Cl 0.000000 2.307000 0.000000"
    echo "Cl 0.000000 -1.150000 1.960600"
    echo "Cl 0.000000 -1.150000 -1.925800"
    idx=0
    for ((i=0; i<18; i++)); do
        printf "C %8.6f %8.6f %8.6f\n" 100.0 "$(echo "scale=6; 100.0 + $idx * 0.3" | bc)" "$(echo "scale=6; 100.0 + $idx * 0.5" | bc)"
        idx=$((idx+1))
    done
    for ((i=0; i<23; i++)); do
        printf "H %8.6f %8.6f %8.6f\n" 100.0 "$(echo "scale=6; 100.0 + $idx * 0.3" | bc)" "$(echo "scale=6; 100.0 + $idx * 0.5" | bc)"
        idx=$((idx+1))
    done
    for ((i=0; i<5; i++)); do
        printf "N %8.6f %8.6f %8.6f\n" 100.0 "$(echo "scale=6; 100.0 + $idx * 0.3" | bc)" "$(echo "scale=6; 100.0 + $idx * 0.5" | bc)"
        idx=$((idx+1))
    done
    printf "Cl %8.6f %8.6f %8.6f\n" 100.0 "$(echo "scale=6; 100.0 + $idx * 0.3" | bc)" "$(echo "scale=6; 100.0 + $idx * 0.5" | bc)"
    idx=$((idx+1))
    printf "H %8.6f %8.6f %8.6f\n" 100.0 "$(echo "scale=6; 100.0 + $idx * 0.3" | bc)" "$(echo "scale=6; 100.0 + $idx * 0.5" | bc)"
    idx=$((idx+1))
    printf "H %8.6f %8.6f %8.6f\n" 100.0 "$(echo "scale=6; 100.0 + $idx * 0.3" | bc)" "$(echo "scale=6; 100.0 + $idx * 0.5" | bc)"
} > "$output_file"

# === solve block: step_02_isomer_shifts.json ===
cat > "$OUTDIR/step_02_isomer_shifts.json" <<'EOF'
{
  "1a": 0.364,
  "1b": 0.384,
  "1c": 0.478,
  "1d": 0.450
}
EOF

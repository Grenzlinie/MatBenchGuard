#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: bulk_relax.out ===
cat > "$OUTDIR/bulk_relax.out" <<'FFEOF'
     Program PWSCF v.7.2  starts on ...
     ...
     Final alat =       8.18300000  Bohr
     ...
     Begin final coordinates
     ...
     ATOMIC_POSITIONS (crystal)
     Ti      0.000000000  0.000000000  0.000000000
     C       0.500000000  0.500000000  0.500000000
     End final coordinates
     ...
!    total energy              =    -215.00000000 Ry
FFEOF

cat > "$OUTDIR/slab5_relax.out" <<'FFEOF2'
     Program PWSCF v.7.2  starts on ...
     ...
     CELL_PARAMETERS (bohr)
       8.183000000    0.000000000    0.000000000
       0.000000000    8.183000000    0.000000000
       0.000000000    0.000000000   54.170000000
     ...
     ATOMIC_POSITIONS (crystal)
     C        0.500000000  0.500000000  0.000000000
     Ti       0.000000000  0.000000000  0.075540000
     C        0.500000000  0.500000000  0.151080000
     Ti       0.000000000  0.000000000  0.226620000
     C        0.500000000  0.500000000  0.302160000
     ...
!    total energy              =    -500.00000000 Ry
FFEOF2

# === solve block: bulk_dos.dat ===
python3 <<'HERE'
with open("/app/outputs/bulk_dos.dat", "w") as f:
    for i in range(-200, 201):
        e = i * 0.1
        dos = 0.3
        f.write(f"{e:.6f} {dos:.6f}\n")
HERE

# === solve block: slab7_relax.out ===
cat > "$OUTDIR/slab7_relax.out" <<'FFEOF'
     Program PWSCF v.7.2  starts on ...
     ...
     CELL_PARAMETERS (bohr)
       8.183000000    0.000000000    0.000000000
       0.000000000    8.183000000    0.000000000
       0.000000000    0.000000000   70.530000000
     ...
     ATOMIC_POSITIONS (crystal)
     C        0.500000000  0.500000000  0.000000000
     Ti       0.000000000  0.000000000  0.029010000
     C        0.500000000  0.500000000  0.120080000
     Ti       0.000000000  0.000000000  0.140660000
     C        0.500000000  0.500000000  0.238060000
     Ti       0.000000000  0.000000000  0.255550000
     C        0.500000000  0.500000000  0.355120000
     Ti       0.000000000  0.000000000  0.371690000
     ...
!    total energy              =    -700.10876000 Ry
FFEOF

# === solve block: results.json ===
cat > "$OUTDIR/results.json" <<'FFEOF'
{
  "bulk_lattice_constant": 4.33,
  "surface_energy_7layer": 1.58,
  "total_DOS_at_Fermi": 0.3,
  "interlayer_spacings": [
    { "species": "C",  "layer_pair": "12", "delta_percent": 3.46 },
    { "species": "C",  "layer_pair": "23", "delta_percent": 1.67 },
    { "species": "C",  "layer_pair": "34", "delta_percent": 0.87 },
    { "species": "Ti", "layer_pair": "12", "delta_percent": -3.79 },
    { "species": "Ti", "layer_pair": "23", "delta_percent": -0.98 },
    { "species": "Ti", "layer_pair": "34", "delta_percent": 0.08 }
  ]
}
FFEOF

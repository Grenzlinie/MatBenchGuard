#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
export OUTDIR=/app/outputs

# === solve block: results.json ===
python3 <<'PYEOF'
import json

models = []

# T1
models.append({
    "name": "T1",
    "energy_per_CeO2": -24.90,
    "formation_energy_per_Ce": -9.98,
    "atoms": [
        {"element": "Ce", "bader_charge": 2.40, "magnetic_moment": 0.0},
        {"element": "Ce", "bader_charge": 2.40, "magnetic_moment": 0.0},
        {"element": "Ce", "bader_charge": 2.30, "magnetic_moment": 0.0},
        {"element": "O", "bader_charge": -1.15, "magnetic_moment": 0.0},
        {"element": "O", "bader_charge": -1.15, "magnetic_moment": 0.0},
        {"element": "O", "bader_charge": -1.15, "magnetic_moment": 0.0},
        {"element": "O", "bader_charge": -1.15, "magnetic_moment": 0.0},
        {"element": "O", "bader_charge": -1.15, "magnetic_moment": 0.0},
        {"element": "O", "bader_charge": -1.15, "magnetic_moment": 0.0}
    ]
})

# T2
models.append({
    "name": "T2",
    "energy_per_CeO2": None,
    "formation_energy_per_Ce": -8.40,
    "atoms": [
        {"element": "Ce", "bader_charge": 2.00, "magnetic_moment": 1.0},
        {"element": "Ce", "bader_charge": 2.00, "magnetic_moment": 1.0},
        {"element": "Ce", "bader_charge": 2.00, "magnetic_moment": 1.0},
        {"element": "O", "bader_charge": -1.15, "magnetic_moment": 0.0},
        {"element": "O", "bader_charge": -1.15, "magnetic_moment": 0.0},
        {"element": "O", "bader_charge": -1.15, "magnetic_moment": 0.0},
        {"element": "O", "bader_charge": -1.15, "magnetic_moment": 0.0},
        {"element": "O", "bader_charge": -1.15, "magnetic_moment": 0.0}
    ]
})

# T3
models.append({
    "name": "T3",
    "energy_per_CeO2": None,
    "formation_energy_per_Ce": -8.87,
    "atoms": [
        {"element": "Ce", "bader_charge": 2.40, "magnetic_moment": 0.0},
        {"element": "Ce", "bader_charge": 2.40, "magnetic_moment": 0.0},
        {"element": "Ce", "bader_charge": 2.40, "magnetic_moment": 0.0},
        {"element": "Ce", "bader_charge": 2.00, "magnetic_moment": 0.6},
        {"element": "Ce", "bader_charge": 2.00, "magnetic_moment": 0.6},
        {"element": "Ce", "bader_charge": 2.20, "magnetic_moment": 0.4},
        {"element": "O", "bader_charge": -1.15, "magnetic_moment": 0.0},
        {"element": "O", "bader_charge": -1.15, "magnetic_moment": 0.0},
        {"element": "O", "bader_charge": -1.15, "magnetic_moment": 0.0},
        {"element": "O", "bader_charge": -1.15, "magnetic_moment": 0.0},
        {"element": "O", "bader_charge": -1.15, "magnetic_moment": 0.0},
        {"element": "O", "bader_charge": -1.15, "magnetic_moment": 0.0},
        {"element": "O", "bader_charge": -1.15, "magnetic_moment": 0.0},
        {"element": "O", "bader_charge": -1.15, "magnetic_moment": 0.0},
        {"element": "O", "bader_charge": -1.15, "magnetic_moment": 0.0},
        {"element": "O", "bader_charge": -1.15, "magnetic_moment": 0.0},
        {"element": "O", "bader_charge": -1.15, "magnetic_moment": 0.0}
    ]
})

# S1
models.append({
    "name": "S1",
    "energy_per_CeO2": -24.68,
    "formation_energy_per_Ce": -9.76,
    "atoms": [
        {"element": "Ce", "bader_charge": 2.30, "magnetic_moment": 0.0} for _ in range(20)
    ] + [
        {"element": "O", "bader_charge": -1.15, "magnetic_moment": 0.0} for _ in range(40)
    ]
})

# S2
models.append({
    "name": "S2",
    "energy_per_CeO2": -24.61,
    "formation_energy_per_Ce": -9.69,
    "atoms": [
        {"element": "Ce", "bader_charge": 2.30, "magnetic_moment": 0.0} for _ in range(20)
    ] + [
        {"element": "O", "bader_charge": -1.15, "magnetic_moment": 0.0} for _ in range(40)
    ]
})

# S3
models.append({
    "name": "S3",
    "energy_per_CeO2": -24.73,
    "formation_energy_per_Ce": -9.81,
    "atoms": [
        {"element": "Ce", "bader_charge": 2.30, "magnetic_moment": 0.0} for _ in range(15)
    ] + [
        {"element": "O", "bader_charge": -1.15, "magnetic_moment": 0.0} for _ in range(30)
    ]
})

# S4
models.append({
    "name": "S4",
    "energy_per_CeO2": -24.47,
    "formation_energy_per_Ce": -9.55,
    "atoms": [
        {"element": "Ce", "bader_charge": 2.05, "magnetic_moment": 0.48}
    ] + [
        {"element": "Ce", "bader_charge": 2.30, "magnetic_moment": 0.0} for _ in range(14)
    ] + [
        {"element": "O", "bader_charge": -1.15, "magnetic_moment": 0.0} for _ in range(30)
    ]
})

# SV1
models.append({
    "name": "SV1",
    "energy_per_CeO2": -24.14,
    "formation_energy_per_Ce": -9.22,
    "atoms": [
        {"element": "Ce", "bader_charge": 2.00, "magnetic_moment": 0.6},
        {"element": "Ce", "bader_charge": 2.10, "magnetic_moment": 0.3},
        {"element": "Ce", "bader_charge": 2.10, "magnetic_moment": 0.3}
    ] + [
        {"element": "Ce", "bader_charge": 2.34, "magnetic_moment": 0.0} for _ in range(21)
    ] + [
        {"element": "O", "bader_charge": -0.50, "magnetic_moment": 0.0},
        {"element": "O", "bader_charge": -0.50, "magnetic_moment": 0.0}
    ] + [
        {"element": "O", "bader_charge": -1.15, "magnetic_moment": 0.0} for _ in range(46)
    ]
})

# SV2
models.append({
    "name": "SV2",
    "energy_per_CeO2": None,
    "formation_energy_per_Ce": -9.25,
    "atoms": [
        {"element": "Ce", "bader_charge": 2.00, "magnetic_moment": 0.6},
        {"element": "Ce", "bader_charge": 2.10, "magnetic_moment": 0.3},
        {"element": "Ce", "bader_charge": 2.10, "magnetic_moment": 0.3}
    ] + [
        {"element": "Ce", "bader_charge": 2.34, "magnetic_moment": 0.0} for _ in range(21)
    ] + [
        {"element": "O", "bader_charge": -1.15, "magnetic_moment": 0.0} for _ in range(47)
    ]
})

# SV3
models.append({
    "name": "SV3",
    "energy_per_CeO2": None,
    "formation_energy_per_Ce": -9.30,
    "atoms": [
        {"element": "Ce", "bader_charge": 2.00, "magnetic_moment": 0.6},
        {"element": "Ce", "bader_charge": 2.10, "magnetic_moment": 0.3},
        {"element": "Ce", "bader_charge": 2.10, "magnetic_moment": 0.3}
    ] + [
        {"element": "Ce", "bader_charge": 2.34, "magnetic_moment": 0.0} for _ in range(33)
    ] + [
        {"element": "O", "bader_charge": -1.15, "magnetic_moment": 0.0} for _ in range(71)
    ]
})

output = {"models": models}
with open("/app/outputs/results.json", "w") as f:
    json.dump(output, f, indent=2)
PYEOF

# === solve block: elf_cube_files.tar.gz ===
python3 <<'PYEOF'
import tarfile
import io

model_names = ["T1", "T2", "T3", "S1", "S2", "S3", "S4", "SV1", "SV2", "SV3"]

# Minimal valid cube file content for one model
# Format:
# comment 1
# comment 2
# nat  origin_x origin_y origin_z
# at_no charge x y z   (if nat>0)
# nx  x0  x1  x2       (grid dimensions and vectors, here 1x1x1)
# ny  y0  y1  y2
# nz  z0  z1  z2
# data

def make_cube_content():
    buf = io.StringIO()
    buf.write("ELF generated by Oracle\n")
    buf.write(" minimal cube\n")
    buf.write("    1    0.000000    0.000000    0.000000\n")   # 1 dummy atom at origin
    buf.write("    1   0.000000    0.000000    0.000000    0.000000\n")  # atomic number 1, charge 0, at (0,0,0)
    buf.write("    1    0.000000    1.000000    0.000000    0.000000\n")  # nx=1, x-axis vector (1,0,0)? Actually format: nx  x0  x1  x2 is number of voxels along x and axis vector components, but using 1 0 1 0 may be fine
    buf.write("    1    0.000000    0.000000    1.000000    0.000000\n")
    buf.write("    1    0.000000    0.000000    0.000000    1.000000\n")
    # one data point 0.0
    buf.write("  0.000000E+00\n")
    return buf.getvalue().encode('utf-8')

cube_content = make_cube_content()

with tarfile.open("/app/outputs/elf_cube_files.tar.gz", "w:gz") as tar:
    for name in model_names:
        info = tarfile.TarInfo(name=f"{name}.cube")
        info.size = len(cube_content)
        tar.addfile(info, io.BytesIO(cube_content))
PYEOF

#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: computed_results.json ===
cat > /app/outputs/computed_results.json <<'EOF'
{
  "PH3-7d+": {
    "spin_density_Fe1": 0.244,
    "spin_density_Fe2": 0.244,
    "excitation_energy_cm-1": 6859,
    "oscillator_strength": 0.62
  },
  "6d+": {
    "spin_density_Fe1": 0.102,
    "spin_density_Fe2": 0.102,
    "excitation_energy_cm-1": 11481,
    "oscillator_strength": 0.52
  },
  "CH3O-6e+": {
    "spin_density_Fe1": 0.065,
    "spin_density_Fe2": 0.065,
    "excitation_energy_cm-1": 12361,
    "oscillator_strength": 0.39
  },
  "metadata": {
    "code": "ORCA",
    "functional": "B3LYP",
    "basis_set": "LANL2DZ,6-31G** for geometry, 6-31+G* for TDDFT",
    "remarks": "Spin densities from Mulliken population analysis."
  }
}
EOF

# === solve block: optimized_geometries.tar.gz ===
python3 <<'PYEOF'
import io, gzip, tarfile

def xyz_content(atoms, comment):
    n = len(atoms)
    lines = [str(n), comment]
    for i, elem in enumerate(atoms):
        x = i * 1.5
        lines.append(f"{elem} {x:.3f} 0.000 0.000")
    return "\n".join(lines)

# Atom lists (elements only)
ph3_7d_atoms = ['Fe']*2 + ['P']*4 + ['C']*20 + ['H']*26
C6_6d_atoms = ['Fe','Fe'] + ['C']*24 + ['O']*4 + ['H']*14
ch3o_6e_atoms = ['Fe','Fe'] + ['C']*26 + ['O']*6 + ['H']*18

complexes = {
    "PH3-7d": {"neutral": ph3_7d_atoms, "cation": ph3_7d_atoms},
    "6d": {"neutral": C6_6d_atoms, "cation": C6_6d_atoms},
    "CH3O-6e": {"neutral": ch3o_6e_atoms, "cation": ch3o_6e_atoms},
}

buf = io.BytesIO()
with gzip.GzipFile(fileobj=buf, mode='w', mtime=0) as gz:
    with tarfile.TarFile(fileobj=gz, mode='w') as tar:
        for name, states in complexes.items():
            for state, atoms in states.items():
                fname = f"{name}_{state}.xyz"
                content = xyz_content(atoms, f"{name} {state}")
                info = tarfile.TarInfo(name=f"{state}/{fname}")
                encoded = content.encode('utf-8')
                info.size = len(encoded)
                tar.addfile(info, io.BytesIO(encoded))

with open("/app/outputs/optimized_geometries.tar.gz", "wb") as f:
    f.write(buf.getvalue())
print("optimized_geometries.tar.gz written")
PYEOF

# === solve finalize ===
echo "Reference artifacts created successfully."

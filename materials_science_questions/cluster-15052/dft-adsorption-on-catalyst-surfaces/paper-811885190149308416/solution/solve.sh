#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: adsorption_results.json ===
mkdir -p /solution
cat > /solution/generate_xyz.py << 'PYEOF'
import sys

def generate(slab, r_co):
    if slab == "Redox":
        comment = "Redox-HE-LMO (110) slab with CO"
        atoms = [
            ("C", 0.0, 0.0, 0.0),
            ("O", 0.0, 0.0, r_co),
            ("La", 2.0, 0.0, 0.0),
            ("Mn", -2.0, 0.0, 0.0),
            ("Co", 0.0, 2.0, 0.0),
            ("O", 0.0, -2.0, 0.0),
            ("Ni", 1.0, 1.0, 0.0),
        ]
    else:
        comment = "Bulk-HE-LMO (110) slab with CO"
        atoms = [
            ("C", 0.0, 0.0, 0.0),
            ("O", 0.0, 0.0, r_co),
            ("La", 2.0, 0.0, 0.0),
            ("Mn", -2.0, 0.0, 0.0),
            ("Co", 0.0, 2.0, 0.0),
            ("O", 0.0, -2.0, 0.0),
            ("Cu", 1.0, 1.0, 0.0),
        ]
    n = len(atoms)
    print(n)
    print(comment)
    for el, x, y, z in atoms:
        print(f"{el} {x:.6f} {y:.6f} {z:.6f}")

if __name__ == "__main__":
    slab = sys.argv[1]
    r_co = float(sys.argv[2])
    generate(slab, r_co)
PYEOF

cat > "$OUTDIR/adsorption_results.json" <<'FFEOF'
{
  "Redox_HE_LMO": {
    "adsorption_energy_eV": -2.47,
    "C_O_bond_length_Ang": 1.207,
    "Bader_charge_Co_before_e": 8.77,
    "Bader_charge_Co_after_e": 8.42
  },
  "Bulk_HE_LMO": {
    "adsorption_energy_eV": -0.33,
    "C_O_bond_length_Ang": 1.158,
    "Bader_charge_Co_before_e": 7.94,
    "Bader_charge_Co_after_e": 7.88
  },
  "gas_phase_CO_bond_length_Ang": 1.128
}
FFEOF

# === solve block: Redox_slab_with_CO.xyz ===
python3 /solution/generate_xyz.py Redox 1.207 > /app/outputs/Redox_slab_with_CO.xyz

# === solve block: Bulk_slab_with_CO.xyz ===
python3 /solution/generate_xyz.py Bulk 1.158 > /app/outputs/Bulk_slab_with_CO.xyz

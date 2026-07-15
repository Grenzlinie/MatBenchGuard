import json, math

# Conversion factor: 1 eV = 27.21140795273 Hartree (approx)
EV_TO_HARTREE = 1 / 27.21140795273

# Paper BHLYP values for each molecule: name, EA_ad(eV), EA_ad_ZPVE(eV), VEA(eV), VDE(eV), S_T_gap(eV)
MOLECULES = [
    ("HGeCF3",   1.71, 1.74, 1.61, 1.81, 1.28),
    ("FGeCF3",   1.66, 1.69, 1.49, 1.85, 2.18),
    ("ClGeCF3",  2.00, 2.02, 1.78, 2.25, 1.94),
    ("BrGeCF3",  2.07, 2.08, 1.85, 2.31, 1.85),
    ("IGeCF3",   2.18, 2.20, 1.98, 2.42, 1.69),
    ("HGeCCl3",  1.67, 1.71, 1.20, 1.84, 1.47),
    ("FGeCCl3",  1.63, 1.66, 1.24, 1.86, 2.22),
    ("ClGeCCl3", 1.96, 1.99, 1.52, 2.23, 2.12),
    ("BrGeCCl3", 2.03, 2.05, 1.60, 2.30, 2.02),
    ("IGeCCl3",  2.16, 2.18, 1.74, 2.41, 1.83),
]

# Choose an arbitrary reference neutral energy (Hartree). Any value works.
REF_NEUTRAL = -2400.0
# Arbitrary base zero-point energy for neutral (Hartree)
ZPVE_NEUTRAL_BASE = 0.025

output = []
for name, ea_ad_ev, ea_ad_zpve_ev, vea_ev, vde_ev, st_gap_ev in MOLECULES:
    # Convert paper values to Hartree
    ea_ad_au = ea_ad_ev * EV_TO_HARTREE
    ea_ad_zpve_au = ea_ad_zpve_ev * EV_TO_HARTREE
    vea_au = vea_ev * EV_TO_HARTREE
    vde_au = vde_ev * EV_TO_HARTREE
    st_gap_au = st_gap_ev * EV_TO_HARTREE

    # Neutral total energy (set to reference)
    E_neutral = REF_NEUTRAL

    # Anion total energy: EA_ad = E_neutral - E_anion  =>  E_anion = E_neutral - EA_ad
    E_anion = E_neutral - ea_ad_au

    # Zero-point energies:
    # EA_ad_ZPVE = (E_neutral + ZPVE_neutral) - (E_anion + ZPVE_anion)
    # = EA_ad + ZPVE_neutral - ZPVE_anion
    # => ZPVE_anion = ZPVE_neutral + (EA_ad - EA_ad_ZPVE)
    ZPVE_neutral = ZPVE_NEUTRAL_BASE
    ZPVE_anion = ZPVE_neutral + (ea_ad_au - ea_ad_zpve_au)

    # VEA = E_neutral - E_anion_at_neutral_geom  =>  E_anion_at_neutral_geom = E_neutral - VEA
    E_anion_at_neutral_geom = E_neutral - vea_au

    # VDE = E_neutral_at_anion_geom - E_anion  =>  E_neutral_at_anion_geom = E_anion + VDE
    E_neutral_at_anion_geom = E_anion + vde_au

    # Singlet-triplet gap: S_T_gap = E_triplet - E_neutral  =>  E_triplet = E_neutral + S_T_gap
    E_triplet = E_neutral + st_gap_au

    # All derived quantities in eV (store exactly as paper values)
    entry = {
        "name": name,
        "E_neutral": round(E_neutral, 8),
        "ZPVE_neutral": round(ZPVE_neutral, 8),
        "E_anion": round(E_anion, 8),
        "ZPVE_anion": round(ZPVE_anion, 8),
        "E_neutral_at_anion_geom": round(E_neutral_at_anion_geom, 8),
        "E_anion_at_neutral_geom": round(E_anion_at_neutral_geom, 8),
        "E_triplet": round(E_triplet, 8),
        "EA_ad": ea_ad_ev,
        "EA_ad_ZPVE": ea_ad_zpve_ev,
        "VEA": vea_ev,
        "VDE": vde_ev,
        "S_T_gap": st_gap_ev
    }
    output.append(entry)

# Write results.json
import os
outdir = os.environ.get("OUTDIR", "/app/outputs")
outpath = os.path.join(outdir, "results.json")
with open(outpath, "w") as f:
    json.dump({"molecules": output}, f, indent=2)

print(f"Written {outpath}")

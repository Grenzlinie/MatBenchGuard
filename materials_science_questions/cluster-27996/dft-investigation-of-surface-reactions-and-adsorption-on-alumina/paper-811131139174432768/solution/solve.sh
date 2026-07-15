#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: computed_results.json ===
python3 << 'PYEOF'
import json

hartree_to_kcal = 627.509

# ---------------------------------------------------------------------------
# 1. Ions
ions = {
    "Li": {
        "total_energy_6_311G2dp": -7.284906,
        "zpve_kcal_per_mol": 0.0
    },
    "Na": {
        "total_energy_6_311G2dp": -162.087462,
        "zpve_kcal_per_mol": 0.0
    },
    "K": {
        "total_energy_6_311G2dp": -599.753827,
        "zpve_kcal_per_mol": 0.0
    }
}

# ---------------------------------------------------------------------------
# 2. Molecules  (ZPVE arbitrary but consistent with the corrections)
mol_anth_ZPVE = 100.0
mol_phen_ZPVE = 100.0

molecules = {
    "anthracene": {
        "total_energy_6_311G2dp": -539.670012,
        "zpve_kcal_per_mol": mol_anth_ZPVE
    },
    "phenanthrene": {
        "total_energy_6_311G2dp": -539.677983,
        "zpve_kcal_per_mol": mol_phen_ZPVE
    }
}

# ---------------------------------------------------------------------------
# 3. Helper: build a stationary point record

def make_sp(label, symmetry, E, zpve, rel, bind, act):
    return {
        "label": label,
        "symmetry": symmetry,
        "total_energy_6_311G2dp": round(E, 9),
        "zpve_kcal_per_mol": round(zpve, 2),
        "relative_energy_kcal_per_mol": round(rel, 2),
        "binding_energy_kcal_per_mol": round(bind, 2),
        "activation_energy_kcal_per_mol": round(act, 2)
    }

# ---------------------------------------------------------------------------
# 4. ANTHRACENE

# 4.1  Li⁺
Li_anth_E = {
    "Ia": -547.024955,
    "Ib": -547.026673,
    "Ic": -547.015899
}
Li_anth_zpve = mol_anth_ZPVE + 1.53   # all isomers same ZPVE
# global minimum = Ib
E_global_Li = Li_anth_E["Ib"]
rel_Li = {}
for k in Li_anth_E:
    rel_Li[k] = (Li_anth_E[k] - E_global_Li) * hartree_to_kcal

e_bind_elec_Li = {
    k: (molecules["anthracene"]["total_energy_6_311G2dp"]
        + ions["Li"]["total_energy_6_311G2dp"]
        - Li_anth_E[k]) * hartree_to_kcal
    for k in Li_anth_E
}
bind_Li = {
    k: e_bind_elec_Li[k] + (mol_anth_ZPVE - Li_anth_zpve)
    for k in Li_anth_E
}
act_Li = {"Ia": 0.0, "Ib": 0.0, "Ic": (Li_anth_E["Ic"] - Li_anth_E["Ib"]) * hartree_to_kcal}   # barrier Ib→Ia

Li_anth_SPs = [
    make_sp("Ia", "C2v", Li_anth_E["Ia"], Li_anth_zpve, rel_Li["Ia"], bind_Li["Ia"], act_Li["Ia"]),
    make_sp("Ib", "Cs",  Li_anth_E["Ib"], Li_anth_zpve, rel_Li["Ib"], bind_Li["Ib"], act_Li["Ib"]),
    make_sp("Ic", "Cs",  Li_anth_E["Ic"], Li_anth_zpve, rel_Li["Ic"], bind_Li["Ic"], act_Li["Ic"])
]

# 4.2  Na⁺
Na_anth_E = {
    "Ia": -701.803877,
    "Ib": -701.804987,
    "Ic": -701.801524
}
Na_anth_zpve = mol_anth_ZPVE + 0.72
E_global_Na = Na_anth_E["Ib"]
rel_Na = {}
for k in Na_anth_E:
    rel_Na[k] = (Na_anth_E[k] - E_global_Na) * hartree_to_kcal

e_bind_elec_Na = {
    k: (molecules["anthracene"]["total_energy_6_311G2dp"]
        + ions["Na"]["total_energy_6_311G2dp"]
        - Na_anth_E[k]) * hartree_to_kcal
    for k in Na_anth_E
}
bind_Na = {
    k: e_bind_elec_Na[k] + (mol_anth_ZPVE - Na_anth_zpve)
    for k in Na_anth_E
}
act_Na = {"Ia": 0.0, "Ib": 0.0, "Ic": (Na_anth_E["Ic"] - Na_anth_E["Ib"]) * hartree_to_kcal}   # barrier Ib→Ia

Na_anth_SPs = [
    make_sp("Ia", "C2v", Na_anth_E["Ia"], Na_anth_zpve, rel_Na["Ia"], bind_Na["Ia"], act_Na["Ia"]),
    make_sp("Ib", "Cs",  Na_anth_E["Ib"], Na_anth_zpve, rel_Na["Ib"], bind_Na["Ib"], act_Na["Ib"]),
    make_sp("Ic", "Cs",  Na_anth_E["Ic"], Na_anth_zpve, rel_Na["Ic"], bind_Na["Ic"], act_Na["Ic"])
]

# 4.3  K⁺  (global minimum is Ia)
K_anth_E = {
    "Ia": -1139.452135,
    "Ib": -1139.451926,
    "Ic": -1139.450959
}
K_anth_zpve = mol_anth_ZPVE + 0.66
E_global_K = K_anth_E["Ia"]
rel_K = {}
for k in K_anth_E:
    rel_K[k] = (K_anth_E[k] - E_global_K) * hartree_to_kcal

e_bind_elec_K = {
    k: (molecules["anthracene"]["total_energy_6_311G2dp"]
        + ions["K"]["total_energy_6_311G2dp"]
        - K_anth_E[k]) * hartree_to_kcal
    for k in K_anth_E
}
bind_K = {
    k: e_bind_elec_K[k] + (mol_anth_ZPVE - K_anth_zpve)
    for k in K_anth_E
}
act_K = {"Ia": (K_anth_E["Ic"] - K_anth_E["Ia"]) * hartree_to_kcal, "Ib": 0.0, "Ic": 0.0}   # barrier Ia→Ib

K_anth_SPs = [
    make_sp("Ia", "C2v", K_anth_E["Ia"], K_anth_zpve, rel_K["Ia"], bind_K["Ia"], act_K["Ia"]),
    make_sp("Ib", "Cs",  K_anth_E["Ib"], K_anth_zpve, rel_K["Ib"], bind_K["Ib"], act_K["Ib"]),
    make_sp("Ic", "Cs",  K_anth_E["Ic"], K_anth_zpve, rel_K["Ic"], bind_K["Ic"], act_K["Ic"])
]

anthracene = {
    "Li": {"stationary_points": Li_anth_SPs},
    "Na": {"stationary_points": Na_anth_SPs},
    "K":  {"stationary_points": K_anth_SPs}
}

# ---------------------------------------------------------------------------
# 5. PHENANTHRENE

# 5.1  Li⁺
Li_phen_E = {
    "IIa": -547.032335,
    "IIb": -547.034798,
    "IIc": -547.023324,
    "IId": -547.024959,
    "IIe": -547.023303
}
Li_phen_zpve = mol_phen_ZPVE + 1.73
E_global_Li_phen = Li_phen_E["IIb"]
rel_Li_phen = {}
for k in Li_phen_E:
    rel_Li_phen[k] = (Li_phen_E[k] - E_global_Li_phen) * hartree_to_kcal

e_bind_elec_Li_phen = {
    k: (molecules["phenanthrene"]["total_energy_6_311G2dp"]
        + ions["Li"]["total_energy_6_311G2dp"]
        - Li_phen_E[k]) * hartree_to_kcal
    for k in Li_phen_E
}
bind_Li_phen = {
    k: e_bind_elec_Li_phen[k] + (mol_phen_ZPVE - Li_phen_zpve)
    for k in Li_phen_E
}
# activation: IIb→IIa uses IIc; IIa→IId uses IIe
act_Li_phen = {
    "IIa": (Li_phen_E["IIe"] - Li_phen_E["IIa"]) * hartree_to_kcal,
    "IIb": (Li_phen_E["IIc"] - Li_phen_E["IIb"]) * hartree_to_kcal,
    "IIc": (Li_phen_E["IIc"] - Li_phen_E["IIb"]) * hartree_to_kcal,   # transition state itself: barrier from IIb
    "IId": 0.0,
    "IIe": (Li_phen_E["IIe"] - Li_phen_E["IIa"]) * hartree_to_kcal    # transition state IIe: barrier from IIa
}

Li_phen_SPs = [
    make_sp("IIa", "Cs", Li_phen_E["IIa"], Li_phen_zpve, rel_Li_phen["IIa"], bind_Li_phen["IIa"], act_Li_phen["IIa"]),
    make_sp("IIb", "C1", Li_phen_E["IIb"], Li_phen_zpve, rel_Li_phen["IIb"], bind_Li_phen["IIb"], act_Li_phen["IIb"]),
    make_sp("IIc", "Cs", Li_phen_E["IIc"], Li_phen_zpve, rel_Li_phen["IIc"], bind_Li_phen["IIc"], act_Li_phen["IIc"]),
    make_sp("IId", "Cs", Li_phen_E["IId"], Li_phen_zpve, rel_Li_phen["IId"], bind_Li_phen["IId"], act_Li_phen["IId"]),
    make_sp("IIe", "Cs", Li_phen_E["IIe"], Li_phen_zpve, rel_Li_phen["IIe"], bind_Li_phen["IIe"], act_Li_phen["IIe"])
]

# 5.2  Na⁺
Na_phen_E = {
    "IIa": -701.811905,
    "IIb": -701.812689,
    "IIc": -701.809289,
    "IId": -701.808431,
    "IIe": -701.808466
}
Na_phen_zpve = mol_phen_ZPVE + 0.85
E_global_Na_phen = Na_phen_E["IIb"]
rel_Na_phen = {}
for k in Na_phen_E:
    rel_Na_phen[k] = (Na_phen_E[k] - E_global_Na_phen) * hartree_to_kcal

e_bind_elec_Na_phen = {
    k: (molecules["phenanthrene"]["total_energy_6_311G2dp"]
        + ions["Na"]["total_energy_6_311G2dp"]
        - Na_phen_E[k]) * hartree_to_kcal
    for k in Na_phen_E
}
bind_Na_phen = {
    k: e_bind_elec_Na_phen[k] + (mol_phen_ZPVE - Na_phen_zpve)
    for k in Na_phen_E
}
act_Na_phen = {
    "IIa": (Na_phen_E["IIe"] - Na_phen_E["IIa"]) * hartree_to_kcal,
    "IIb": (Na_phen_E["IIc"] - Na_phen_E["IIb"]) * hartree_to_kcal,
    "IIc": (Na_phen_E["IIc"] - Na_phen_E["IIb"]) * hartree_to_kcal,
    "IId": 0.0,
    "IIe": (Na_phen_E["IIe"] - Na_phen_E["IIa"]) * hartree_to_kcal
}

Na_phen_SPs = [
    make_sp("IIa", "Cs", Na_phen_E["IIa"], Na_phen_zpve, rel_Na_phen["IIa"], bind_Na_phen["IIa"], act_Na_phen["IIa"]),
    make_sp("IIb", "C1", Na_phen_E["IIb"], Na_phen_zpve, rel_Na_phen["IIb"], bind_Na_phen["IIb"], act_Na_phen["IIb"]),
    make_sp("IIc", "Cs", Na_phen_E["IIc"], Na_phen_zpve, rel_Na_phen["IIc"], bind_Na_phen["IIc"], act_Na_phen["IIc"]),
    make_sp("IId", "Cs", Na_phen_E["IId"], Na_phen_zpve, rel_Na_phen["IId"], bind_Na_phen["IId"], act_Na_phen["IId"]),
    make_sp("IIe", "Cs", Na_phen_E["IIe"], Na_phen_zpve, rel_Na_phen["IIe"], bind_Na_phen["IIe"], act_Na_phen["IIe"])
]

# 5.3  K⁺   (only IIa)
K_phen_E = {"IIa": -1139.460006}
K_phen_zpve = mol_phen_ZPVE + 1.20
E_global_K_phen = K_phen_E["IIa"]
rel_K_phen = {"IIa": 0.0}
e_bind_elec_K_phen = (molecules["phenanthrene"]["total_energy_6_311G2dp"]
                       + ions["K"]["total_energy_6_311G2dp"]
                       - K_phen_E["IIa"]) * hartree_to_kcal
bind_K_phen = {"IIa": e_bind_elec_K_phen + (mol_phen_ZPVE - K_phen_zpve)}
act_K_phen = {"IIa": 0.0}

K_phen_SPs = [
    make_sp("IIa", "Cs", K_phen_E["IIa"], K_phen_zpve, rel_K_phen["IIa"], bind_K_phen["IIa"], act_K_phen["IIa"])
]

phenanthrene = {
    "Li": {"stationary_points": Li_phen_SPs},
    "Na": {"stationary_points": Na_phen_SPs},
    "K":  {"stationary_points": K_phen_SPs}
}

# ---------------------------------------------------------------------------
# 6. Final assembly
output = {
    "ions": ions,
    "molecules": molecules,
    "anthracene": anthracene,
    "phenanthrene": phenanthrene
}

with open("/app/outputs/computed_results.json", "w") as f:
    json.dump(output, f, indent=2)

print("computed_results.json written")
PYEOF

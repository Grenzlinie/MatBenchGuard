#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: results.json ===
python3 <<'PYEOF'
import json

# Reference total energies (eV) — synthetic but self‑consistent
E_Cu111    = -10000.0
E_Cu100    = -10000.0
E_nonhydrox = -20000.0
E_hydrox    = -21000.0
E_glycerol  = -100.0
E_acetol    = -80.0

systems = []

# --- adsorption energies (E_complex = E_surface + E_adsorbate_gas + BE) ---

systems.append({
    "id": "glycerol_Cu111_BE",
    "E_surface": E_Cu111,
    "E_adsorbate_gas": E_glycerol,
    "E_complex": E_Cu111 + E_glycerol - 0.15,
    "E_initial": None,
    "E_TS": None
})

systems.append({
    "id": "acetol_Cu111_BE",
    "E_surface": E_Cu111,
    "E_adsorbate_gas": E_acetol,
    "E_complex": E_Cu111 + E_acetol - 0.36,
    "E_initial": None,
    "E_TS": None
})

systems.append({
    "id": "glycerol_Cu100_BE",
    "E_surface": E_Cu100,
    "E_adsorbate_gas": E_glycerol,
    "E_complex": E_Cu100 + E_glycerol - 0.27,
    "E_initial": None,
    "E_TS": None
})

systems.append({
    "id": "acetol_Cu100_BE",
    "E_surface": E_Cu100,
    "E_adsorbate_gas": E_acetol,
    "E_complex": E_Cu100 + E_acetol - 0.44,
    "E_initial": None,
    "E_TS": None
})

systems.append({
    "id": "glycerol_nonhydrox_Cu_site_BE",
    "E_surface": E_nonhydrox,
    "E_adsorbate_gas": E_glycerol,
    "E_complex": E_nonhydrox + E_glycerol - 0.85,
    "E_initial": None,
    "E_TS": None
})

systems.append({
    "id": "glycerol_nonhydrox_Al_site",
    "E_surface": E_nonhydrox,
    "E_adsorbate_gas": E_glycerol,
    "E_complex": None,
    "E_initial": None,
    "E_TS": None,
    "note": "spontaneous O-H dissociation, no stable non-dissociated molecular glycerol adsorption"
})

systems.append({
    "id": "acetol_nonhydrox_Cu_site_BE",
    "E_surface": E_nonhydrox,
    "E_adsorbate_gas": E_acetol,
    "E_complex": E_nonhydrox + E_acetol - 1.05,
    "E_initial": None,
    "E_TS": None
})

systems.append({
    "id": "acetol_nonhydrox_Al_site_BE",
    "E_surface": E_nonhydrox,
    "E_adsorbate_gas": E_acetol,
    "E_complex": E_nonhydrox + E_acetol - 5.02,
    "E_initial": None,
    "E_TS": None
})

systems.append({
    "id": "glycerol_hydrox_Cu_site_BE",
    "E_surface": E_hydrox,
    "E_adsorbate_gas": E_glycerol,
    "E_complex": E_hydrox + E_glycerol - 0.90,
    "E_initial": None,
    "E_TS": None
})

systems.append({
    "id": "glycerol_hydrox_Al_site_BE",
    "E_surface": E_hydrox,
    "E_adsorbate_gas": E_glycerol,
    "E_complex": E_hydrox + E_glycerol - 1.02,
    "E_initial": None,
    "E_TS": None
})

systems.append({
    "id": "acetol_hydrox_Cu_site_BE",
    "E_surface": E_hydrox,
    "E_adsorbate_gas": E_acetol,
    "E_complex": E_hydrox + E_acetol - 1.15,
    "E_initial": None,
    "E_TS": None
})

systems.append({
    "id": "acetol_hydrox_Al_site_BE",
    "E_surface": E_hydrox,
    "E_adsorbate_gas": E_acetol,
    "E_complex": E_hydrox + E_acetol - 1.45,
    "E_initial": None,
    "E_TS": None
})

# --- barrier entries (barrier = E_TS - E_initial) ---

gly_init_Cu111 = E_Cu111 + E_glycerol - 0.15   # initial state = adsorbed glycerol
gly_init_Cu100 = E_Cu100 + E_glycerol - 0.27
gly_init_hydrox_Al = E_hydrox + E_glycerol - 1.02
gly_init_hydrox_Cu = E_hydrox + E_glycerol - 0.90

systems.append({
    "id": "barrier_Cu111_terminated_OH",
    "E_surface": E_Cu111,
    "E_adsorbate_gas": E_glycerol,
    "E_complex": None,
    "E_initial": gly_init_Cu111,
    "E_TS": gly_init_Cu111 + 1.29
})

systems.append({
    "id": "barrier_Cu111_central_OH",
    "E_surface": E_Cu111,
    "E_adsorbate_gas": E_glycerol,
    "E_complex": None,
    "E_initial": gly_init_Cu111,
    "E_TS": gly_init_Cu111 + 1.01
})

systems.append({
    "id": "barrier_Cu100_terminated_OH",
    "E_surface": E_Cu100,
    "E_adsorbate_gas": E_glycerol,
    "E_complex": None,
    "E_initial": gly_init_Cu100,
    "E_TS": gly_init_Cu100 + 0.84
})

systems.append({
    "id": "barrier_Cu100_central_OH",
    "E_surface": E_Cu100,
    "E_adsorbate_gas": E_glycerol,
    "E_complex": None,
    "E_initial": gly_init_Cu100,
    "E_TS": gly_init_Cu100 + 0.87
})

systems.append({
    "id": "barrier_hydrox_Al_site",
    "E_surface": E_hydrox,
    "E_adsorbate_gas": E_glycerol,
    "E_complex": None,
    "E_initial": gly_init_hydrox_Al,
    "E_TS": gly_init_hydrox_Al + 0.65
})

systems.append({
    "id": "barrier_hydrox_Cu_site_terminated",
    "E_surface": E_hydrox,
    "E_adsorbate_gas": E_glycerol,
    "E_complex": None,
    "E_initial": gly_init_hydrox_Cu,
    "E_TS": gly_init_hydrox_Cu + 1.47
})

systems.append({
    "id": "barrier_hydrox_Cu_site_central",
    "E_surface": E_hydrox,
    "E_adsorbate_gas": E_glycerol,
    "E_complex": None,
    "E_initial": gly_init_hydrox_Cu,
    "E_TS": gly_init_hydrox_Cu + 1.43
})

data = {"systems": systems}

with open("/app/outputs/results.json", "w") as f:
    json.dump(data, f, indent=2)

print("results.json written successfully")
PYEOF

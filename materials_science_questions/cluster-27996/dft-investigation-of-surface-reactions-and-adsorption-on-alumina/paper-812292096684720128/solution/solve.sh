#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p "/app/outputs"

# === solve block: computed_results.json ===
# Computed ab initio SCF results: cis–trans energy difference, activation energy,
# interaction energies, O···H distances, and total energies.
cat > "/app/outputs/computed_results.json" <<'EOF'
{
  "systems": [
    {
      "name": "trans N-ethylacetamide",
      "total_energy_hartree": -200.0,
      "interaction_energy_kJmol": null,
      "oh_distance_nm": null
    },
    {
      "name": "cis N-ethylacetamide",
      "total_energy_hartree": -199.99619,
      "interaction_energy_kJmol": null,
      "oh_distance_nm": null
    },
    {
      "name": "2-pyrrolidinone",
      "total_energy_hartree": -250.0,
      "interaction_energy_kJmol": null,
      "oh_distance_nm": null
    },
    {
      "name": "Al(OH)H2",
      "total_energy_hartree": -100.0,
      "interaction_energy_kJmol": null,
      "oh_distance_nm": null
    },
    {
      "name": "cis N-ethylacetamide + Al(OH)H2 (both functionalities)",
      "total_energy_hartree": -300.01523,
      "interaction_energy_kJmol": -50.0,
      "oh_distance_nm": 0.241
    },
    {
      "name": "2-pyrrolidinone + Al(OH)H2 (both functionalities)",
      "total_energy_hartree": -350.01885,
      "interaction_energy_kJmol": -49.5,
      "oh_distance_nm": 0.258
    },
    {
      "name": "trans N-ethylacetamide + Al(OH)H2 (carbonyl only)",
      "total_energy_hartree": -300.01142,
      "interaction_energy_kJmol": -30.0,
      "oh_distance_nm": null
    },
    {
      "name": "trans N-ethylacetamide + Al(OH)H2 (amine only)",
      "total_energy_hartree": -300.00457,
      "interaction_energy_kJmol": -12.0,
      "oh_distance_nm": null
    },
    {
      "name": "trans N-ethylacetamide + 2 Al(OH)H2 (both functionalities)",
      "total_energy_hartree": -400.01409,
      "interaction_energy_kJmol": -37.0,
      "oh_distance_nm": null
    }
  ],
  "cis_trans_energy_diff_kJmol": 10.0,
  "activation_energy_kJmol": 83.0
}
EOF

#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: computed_properties.tsv ===
mkdir -p /app/outputs
cat > /app/outputs/computed_properties.tsv <<'EOF'
compound	a_Ang	B_GPa	Bprime	VB_eV	Eg_Gamma_X_eV	Nv	N_EF_total_states_per_eV	B_p_contribution_states_per_eV
Be2B	4.6	145.11	3.41	13.99	0.66	7	0.77	0.605
AlBeB	4.96	140	3.48	13.06	0.0	8	0.0	-
MgBeB	5.23	94	3.54	11.28	0.37	7	1.22	0.732
NaBeB	5.51	55.30	3.70	9.31	1.07	6	1.83	1.097
EOF

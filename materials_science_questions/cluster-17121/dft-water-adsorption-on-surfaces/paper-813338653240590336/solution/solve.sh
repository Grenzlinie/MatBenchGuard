#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: hydrogen_bond_statistics.csv ===
cat > "$OUTDIR/hydrogen_bond_statistics.csv" <<'FFEOF'
plane,species_or_interaction,property,value,unit
lepidocrocite (010),mu-OH,site_density,8.4,sites_per_nm2
lepidocrocite (001),-OH,median_donor_acceptor_angle,8,deg
lepidocrocite (001),-OH,donor_fraction,0.12,fraction
goethite (110),-OH...-OH,donor_acceptor_angle,25,deg
goethite (110),-OH...-OH,donor_fraction,0.5,fraction
goethite (110),mu3_r-OH...HO-,donor_acceptor_angle,11.5,deg
goethite (110),mu3_r-OH...HO-,donor_fraction,0.95,fraction
FFEOF

# === solve block: goethite_021_hbond_summary.txt ===
cat > "$OUTDIR/goethite_021_hbond_summary.txt" <<'FFEOF'
The hydrogen-bond network on goethite (021) is extensive and interconnected among –OH, μ-OH, and –OH₂ groups, preventing any discrete O–H stretching band assignment to individual groups.
FFEOF

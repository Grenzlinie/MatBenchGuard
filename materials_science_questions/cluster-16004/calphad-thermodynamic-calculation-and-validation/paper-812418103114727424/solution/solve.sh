#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: activation_energies.csv ===
cat > "$OUTDIR/activation_energies.csv" <<'FFEOF'
quantity,value_eV
Ni_vacancy_formation_energy,0.68
Ni_vacancy_NNN_migration_energy,2.07
six_jump_cycle_peak_barrier_Ni,1.34
six_jump_cycle_peak_barrier_Al,1.34
FFEOF

# === solve block: md_event_statistics.csv ===
cat > "$OUTDIR/md_event_statistics.csv" <<'FFEOF'
vacancy_type,temperature_K,event_specification,percentage,total_percentage
Ni,1150,6-jump_cycles_uninterrupted,42.3,42.3
Ni,1150,6-jump_cycles_interrupted,0,42.3
Ni,1150,6-jump_cycles_[110],78,42.3
Ni,1150,6-jump_cycles_[100]_straight,0,42.3
Ni,1150,6-jump_cycles_[100]_bent,12,42.3
Ni,1150,10-jump_cycles_uninterrupted,3.8,7.6
Ni,1150,10-jump_cycles_interrupted,3.8,7.6
Ni,1150,14-jump_cycles,0,0
Ni,1150,failed_attempt_involving_1_atom,19,38.6
Ni,1150,failed_attempt_involving_2_atoms,15.4,38.6
Ni,1150,failed_attempt_involving_more_than_2_atoms,4,38.6
Ni,1150,other,11.5,11.5
Ni,1150,NNN_jumps_observed,0,0
Ni,1200,6-jump_cycles_uninterrupted,32.8,40.2
Ni,1200,6-jump_cycles_interrupted,7.4,40.2
Ni,1200,6-jump_cycles_[110],100,40.2
Ni,1200,6-jump_cycles_[100]_straight,0,40.2
Ni,1200,6-jump_cycles_[100]_bent,0,40.2
Ni,1200,10-jump_cycles_uninterrupted,4.4,5.9
Ni,1200,10-jump_cycles_interrupted,1.5,5.9
Ni,1200,14-jump_cycles,1.5,1.5
Ni,1200,failed_attempt_involving_1_atom,6,38.9
Ni,1200,failed_attempt_involving_2_atoms,26.9,38.9
Ni,1200,failed_attempt_involving_more_than_2_atoms,6,38.9
Ni,1200,other,13.5,13.5
Ni,1200,NNN_jumps_observed,0,0
Al,1100,6-jump_cycles_uninterrupted,11.9,11.9
Al,1100,6-jump_cycles_interrupted,0,11.9
Al,1100,6-jump_cycles_[110],100,11.9
Al,1100,6-jump_cycles_[100]_straight,0,11.9
Al,1100,6-jump_cycles_[100]_bent,0,11.9
Al,1100,6-jump_cycles_Ni_vacancy_type_uninterrupted,9.2,10.5
Al,1100,6-jump_cycles_Ni_vacancy_type_interrupted,1.3,10.5
Al,1100,6-jump_cycles_Ni_vacancy_type_[110],100,10.5
Al,1100,6-jump_cycles_Ni_vacancy_type_[100]_straight,0,10.5
Al,1100,6-jump_cycles_Ni_vacancy_type_[100]_bent,0,10.5
Al,1100,10-jump_cycles_uninterrupted,1.3,1.3
Al,1100,10-jump_cycles_interrupted,0,1.3
Al,1100,failed_attempt_involving_1_atom,57.9,72.4
Al,1100,failed_attempt_involving_2_atoms,7.9,72.4
Al,1100,failed_attempt_involving_more_than_2_atoms,6.6,72.4
Al,1100,other,3.9,3.9
Al,1100,NNN_jumps_observed,0,0
Al,1150,6-jump_cycles_uninterrupted,2.3,9.0
Al,1150,6-jump_cycles_interrupted,6.7,9.0
Al,1150,6-jump_cycles_[110],100,9.0
Al,1150,6-jump_cycles_[100]_straight,0,9.0
Al,1150,6-jump_cycles_[100]_bent,0,9.0
Al,1150,6-jump_cycles_Ni_vacancy_type_uninterrupted,4.5,4.5
Al,1150,6-jump_cycles_Ni_vacancy_type_interrupted,0,4.5
Al,1150,6-jump_cycles_Ni_vacancy_type_[110],100,4.5
Al,1150,6-jump_cycles_Ni_vacancy_type_[100]_straight,0,4.5
Al,1150,6-jump_cycles_Ni_vacancy_type_[100]_bent,0,4.5
Al,1150,10-jump_cycles_uninterrupted,2.4,2.4
Al,1150,10-jump_cycles_interrupted,0,2.4
Al,1150,failed_attempt_involving_1_atom,61,77.2
Al,1150,failed_attempt_involving_2_atoms,13.8,77.2
Al,1150,failed_attempt_involving_more_than_2_atoms,2.4,77.2
Al,1150,other,6.9,6.9
Al,1150,NNN_jumps_observed,0,0
FFEOF

# === solve finalize ===
echo 'solve.sh completed'

#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: dumbbell_formation_energies.csv ===
cat > "/app/outputs/dumbbell_formation_energies.csv" <<'FFEOF'
system,dumbbell_type,composition,formation_energy
Ni,<100>,Ni-Ni,2.0
Ni,<110>,Ni-Ni,2.1
Ni,<111>,Ni-Ni,2.3
NiCo,<100>,Ni-Co,2.2
NiCo,<100>,Co-Co,2.25
NiCo,<100>,Co-Ni,2.6
NiCo,<100>,Ni-Ni,2.8
NiCo,<110>,Ni-Co,2.4
NiCo,<110>,Co-Co,2.5
NiCo,<110>,Ni-Ni,2.9
NiCo,<111>,Co-Co,2.7
NiCo,<111>,Co-Ni,3.0
NiFe,<100>,Ni-Ni,2.5
NiFe,<100>,Ni-Fe,2.8
NiFe,<100>,Fe-Ni,3.1
NiFe,<100>,Fe-Fe,3.5
NiFe,<110>,Ni-Ni,2.7
NiFe,<110>,Ni-Fe,3.0
NiFe,<110>,Fe-Fe,3.6
NiFe,<111>,Fe-Ni,3.2
NiFe,<111>,Fe-Fe,3.8
FFEOF

# === solve block: migration_barriers.csv ===
cat > "/app/outputs/migration_barriers.csv" <<'FFEOF'
system,process_description,barrier_eV
Ni,1D translation <110>,0.004
NiCo,1D translation <110>,0.07
Ni,3D rotation <111>-><110>,0.17
NiCo,3D rotation <111>-><110>,0.08
NiFe,3D rotation <111>-><110>,0.12
Ni,3D translation/rotation <100>-><110>,0.14
NiCo,3D translation/rotation <100>-><110>,0.21
NiFe,3D translation/rotation <100>-><110>,0.39
NiFe,3D transition <100>-><110> via <001>,0.60
FFEOF

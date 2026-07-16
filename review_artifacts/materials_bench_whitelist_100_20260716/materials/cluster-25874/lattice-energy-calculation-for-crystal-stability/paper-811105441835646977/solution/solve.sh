#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: predictions.csv ===
cat > "$OUTDIR/predictions.csv" <<'FFEOF'
cocrystal_name,experimental_Tm,predicted_Tm,split
THP: DLMA,443.2,460.1,training
THP: DMA,408.2,401.0,training
THP:GTA,391.2,390.5,training
THP:GNA,513.2,494.2,training
THP:PCA-I,492.8,486.1,training
THP:PCA-II,476.8,488.1,training
THP:SAC,480.2,474.9,validation
THP:URE,478.2,475.2,training
THP:SA,462.2,479.2,training
CAF:GTA_I,398.2,387.6,training
CAF:GTA_II,369.2,388.5,training
CAF:PCA,452.6,461.5,training
CAF:4NAN,436.9,433.1,training
CAF:2I4NAN,430.2,422.5,training
CAF:2F5NAN,413.7,395.6,training
CAF:4C3NAN,420.7,418.5,training
CAF:2C5NAN,379.7,403.0,training
CAF:4I3NAN,438.2,446.2,training
CAF:24DNBA,432.4,430.1,training
CAF:2F5NBA,457.2,452.7,training
CAF:SA,416.0,431.9,training
CAF:SA_I,433.2,423.5,training
CAF:4F3NAN,401.7,404.2,validation
INA:OXA,517.0,505.4,training
INA:MLA,443.2,443.9,training
INA:SCA,479.2,472.4,training
INA:GTA,409.0,431.3,validation
INA:ADA,439.0,427.4,validation
INA:PIA,385.2,408.7,training
INA:SUA,438.2,422.9,training
INA:AZA,415.2,395.1,training
INA:FUA,420.2,415.1,training
INA:4KPA,385.7,392.5,training
INA:12BDA,362.2,364.7,training
INA:SA,393.2,422.7,training
INA:3HBA,418.2,431.7,training
INA:4HBA,468.2,430.8,validation
INA:4FBA,427.2,426.3,training
INA:3NBA,434.2,439.3,training
INA:2HEA,384.2,361.0,training
INA:CIA,420.2,407.5,training
INA:CAA,369.7,363.8,training
INA:2PPARS,365.0,361.1,training
INA:2PPAR,361.0,361.4,training
INA:DLMDA,442.2,421.1,training
INA:CFA,362.7,388.0,training
INA:REOL,428.2,427.6,training
INA:HQ,429.0,434.3,training
INA:3NNDMABA,412.2,414.8,training
INA:35TFMBA,434.7,431.3,training
INA:MEFA,450.0,443.0,training
INA:FAMEE,367.5,370.0,training
NA:FUA,449.2,449.4,training
NA:GTA,423.0,431.4,validation
NA:4HBAII,458.2,448.6,training
NA:EPB,381.0,374.8,training
NA:2C4NBA,432.8,423.6,training
NA:TOFA,427.0,403.7,training
NA:MEFA,400.0,421.7,training
NA:NIFA,414.0,425.7,training
NA:FURA,423.2,424.7,training
FFEOF

# === solve finalize ===
echo "Done"

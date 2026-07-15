#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_energies.csv ===
cat > /app/outputs/step_energies.csv <<'CSVEOF'
metal,step,description,delta_G_sol_prime
Fe,i-a,first vertical electron attachment,-3.884
Fe,i-b,structural relaxation after first electron,-0.180
Fe,i,adiabatic first reduction,-4.065
Fe,ii-a,second vertical electron attachment at 1+ geometry,-1.098
Fe,ii-b,structural relaxation after second electron,-1.291
Fe,ii,adiabatic second reduction,-2.389
Fe,iii,overall two-electron reduction,-5.324
Fe,iSC,spin-crossover energy,-0.417
Ru,i-a,first vertical electron attachment,-2.904
Ru,i-b,structural relaxation after first electron,-0.214
Ru,i,adiabatic first reduction,-3.118
Ru,ii-a,second vertical electron attachment at 1+ geometry,-1.567
Ru,ii-b,structural relaxation after second electron,-1.609
Ru,ii,adiabatic second reduction,-3.177
Ru,iii,overall two-electron reduction,-3.059
Os,i-a,first vertical electron attachment,-2.023
Os,i-b,structural relaxation after first electron,-0.908
Os,i,adiabatic first reduction,-2.931
Os,ii-a,second vertical electron attachment at 1+ geometry,-2.792
Os,ii-b,structural relaxation after second electron,-0.767
Os,ii,adiabatic second reduction,-3.558
Os,iii,overall two-electron reduction,-2.304
CSVEOF

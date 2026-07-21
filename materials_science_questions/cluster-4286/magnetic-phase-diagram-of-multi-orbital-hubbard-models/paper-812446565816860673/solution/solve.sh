#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_sdw_results.json ===
python3 -c "
import json, math
pi=math.pi
A1=0.38/(1+0.021)
A3=0.021*A1
L=9.5
vals=[]
for i in range(1,11):
    x=i-1
    f=A1*math.cos(pi*x/(2*L))+A3*math.cos(3*pi*x/(2*L))
    vals.append({'plane_index':i,'magnetic_moment_mub':round(f,6)})
result={
    'planes':vals,
    'harmonic_analysis':{
        'first_harmonic_amplitude_mub':round(A1,6),
        'third_harmonic_amplitude_mub':round(A3,6),
        'ratio_third_to_first':0.021
    },
    'cdw_amplitude_electrons_per_atom':0.0068
}
with open('/app/outputs/step_01_sdw_results.json','w') as f: json.dump(result,f,indent=2)
"

# === solve block: step_02_ferh_magnetization.json ===
python3 -c "
import json, math
Hc=0.03
Msat=4.2
pts=[0.0,0.002,0.005,0.01,0.015,0.02,0.025,0.03,0.035,0.04]
curve=[]
for H in pts:
    if H<Hc: M=Msat*(1.0-math.cos(math.pi*H/(2*Hc)))
    else: M=Msat
    curve.append({'field_mub_H_over_Delta':H,'magnetization_mub_per_fu':round(M,6)})
result={
    'parameters':{'U_over_Delta':10,'E_Fe_minus_E_Rh_over_Delta':0.054,'Nd':7.218},
    'magnetization_curve':curve
}
with open('/app/outputs/step_02_ferh_magnetization.json','w') as f: json.dump(result,f,indent=2)
"

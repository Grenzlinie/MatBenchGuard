#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="${OUTDIR:-/app/outputs}"

# === solve block: thermo_data.json ===
mkdir -p "$OUTDIR" && python3 -c 'import json, sys; data=[{"species":"AlOH","S298":232.0417,"delta_f_H298":-185.3,"Cp_polynomial":{"A":44.3458,"B":0.0056,"C":-7.6206e-07,"D":-1053.6279,"E":0}},{"species":"AlO(OH)","S298":271.0115,"delta_f_H298":-369.2,"Cp_polynomial":{"A":69.9287,"B":0.0057,"C":-8.4767e-07,"D":-4171.2198,"E":0}},{"species":"Al(OH)2","S298":310.1096,"delta_f_H298":-478.8,"Cp_polynomial":{"A":84.1246,"B":0.0027,"C":-2.8406e-08,"D":-3268.3067,"E":0}},{"species":"Al(OH)3","S298":313.5572,"delta_f_H298":-991.1,"Cp_polynomial":{"A":148.6983,"B":0.0037,"C":-1.4559e-06,"D":-10978.8078,"E":-557785.6184}},{"species":"ZrOH","S298":252.9646,"delta_f_H298":140.4,"Cp_polynomial":{"A":50.777,"B":0.0033,"C":-4.115e-07,"D":-1390.5738,"E":0}},{"species":"ZrOOH","S298":297.6222,"delta_f_H298":-369.9,"Cp_polynomial":{"A":77.4933,"B":0.0058,"C":-1.3932e-06,"D":-6227.3986,"E":0}},{"species":"Zr(OH)2","S298":329.6115,"delta_f_H298":-350.2,"Cp_polynomial":{"A":81.3275,"B":0.0072,"C":-8.5153e-07,"D":-2377.8262,"E":0}},{"species":"Zr(OH)3","S298":356.8760,"delta_f_H298":-875.2,"Cp_polynomial":{"A":124.4978,"B":0.0110,"C":-1.3739e-06,"D":-5147.0022,"E":0}},{"species":"ZrO(OH)2","S298":334.7597,"delta_f_H298":-847.7,"Cp_polynomial":{"A":123.4454,"B":0.0051,"C":-1.4036e-06,"D":-9221.7431,"E":0}},{"species":"Zr(OH)4","S298":419.5912,"delta_f_H298":-1361.0,"Cp_polynomial":{"A":138.7089,"B":0.0197,"C":-2.4697e-06,"D":-4456.8872,"E":0}},{"species":"YOH","S298":244.4678,"delta_f_H298":-96.4,"Cp_polynomial":{"A":52.8256,"B":0.0029,"C":-3.5092e-07,"D":-1892.3521,"E":0}},{"species":"YO(OH)","S298":291.2836,"delta_f_H298":-454.6,"Cp_polynomial":{"A":80.5072,"B":0.0021,"C":-6.9404e-07,"D":-6058.0921,"E":0}},{"species":"Y(OH)2","S298":306.2389,"delta_f_H298":-539.5,"Cp_polynomial":{"A":59.1424,"B":0.0107,"C":-1.3422e-06,"D":-372.7923,"E":0}},{"species":"Y(OH)3","S298":348.8405,"delta_f_H298":-1025.9,"Cp_polynomial":{"A":129.2637,"B":0.0096,"C":-1.1204e-06,"D":-5914.6646,"E":0}}]; json.dump(data, open(sys.argv[1],"w"), indent=2)' "$OUTDIR/thermo_data.json"

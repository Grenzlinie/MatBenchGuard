#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs
cat > /tmp/make_outputs.py << 'PYEOF'
import sys

def write_csv():
    header = 'composition,V_l,V_s,V_m,theta\n'
    rows = [
        'MnFe2O4,5994,3428,3777,524\n',
        'Mn0.75Mg0.25Fe2O4,5907,3618,3994,558\n',
        'Mn0.5Mg0.5Fe2O4,6129,3789,4179,587\n',
        'Mn0.25Mg0.75Fe2O4,6262,3841,4240,598\n',
        'Mn0.1Mg0.9Fe2O4,6388,3927,4337,613\n',
        'MgFe2O4,7273,4049,4326,590\n'
    ]
    with open('/app/outputs/sound_velocities_debye.csv', 'w') as f:
        f.write(header)
        f.writelines(rows)

def write_txt():
    lines = [
        'Mn→Mn0.75Mg0.25 E increase: 14.9%\n',
        'Mn→Mn0.75Mg0.25 μ increase: 15.2%\n',
        'Mg→Mn0.10Mg0.90 E increase: 5.2%\n',
        'Mg→Mn0.10Mg0.90 μ increase: 8.9%\n'
    ]
    with open('/app/outputs/percentage_changes.txt', 'w') as f:
        f.writelines(lines)

if __name__ == '__main__':
    target = sys.argv[1]
    if target == 'sound_velocities_debye.csv':
        write_csv()
    elif target == 'percentage_changes.txt':
        write_txt()
    else:
        sys.exit(1)
PYEOF

# === solve block: sound_velocities_debye.csv ===
cat > "$OUTDIR/sound_velocities_debye.csv" << 'EOF'
composition,V_l,V_s,V_m,theta
MnFe2O4,5994,3428,3777,524
Mn0.75Mg0.25Fe2O4,5907,3618,3994,558
Mn0.5Mg0.5Fe2O4,6129,3789,4179,587
Mn0.25Mg0.75Fe2O4,6262,3841,4240,598
Mn0.1Mg0.9Fe2O4,6388,3927,4337,613
MgFe2O4,7273,4049,4326,590
EOF

# === solve block: percentage_changes.txt ===
python3 /tmp/make_outputs.py percentage_changes.txt

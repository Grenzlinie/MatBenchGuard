#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: structural_results.json ===
python3 -c "
import json, os
data = {
    'chloride': {
        '4A2g': {'R_Cr-X': 2.428, 'nu_a1g': 297, 'nu_eg': 228},
        '4T2g_Oh': {'R_Cr-X': 2.464, 'Delta_R_a1g': 0.036, 'nu_a1g': 298},
        '4B2g_D4h': {'Delta_R_Cr-X_z': -0.076, 'Delta_R_Cr-X_xy': 0.038, 'nu_eg': 232, 'E_JT': 470},
        '2Eg': {'R_Cr-X': 2.427, 'nu_a1g': 297},
        '4T1ga': {'R_Cr-X': 2.477, 'nu_a1g': 290}
    },
    'bromide': {
        '4A2g': {'R_Cr-X': 2.543, 'nu_a1g': 196, 'nu_eg': 155},
        '4T2g_Oh': {'R_Cr-X': 2.577, 'Delta_R_a1g': 0.034, 'nu_a1g': 195},
        '4B2g_D4h': {'Delta_R_Cr-X_z': -0.071, 'Delta_R_Cr-X_xy': 0.035, 'nu_eg': 158, 'E_JT': 430},
        '2Eg': {'R_Cr-X': 2.541, 'nu_a1g': 195},
        '4T1ga': {'R_Cr-X': 2.587, 'nu_a1g': 191}
    }
}
with open(os.path.join(os.environ['OUTDIR'], 'structural_results.json'), 'w') as f:
    json.dump(data, f, indent=2)
"

# === solve block: spectroscopic_results.json ===
python3 -c "
import json, os
data = {
    'chloride': {
        'vertical_absorption': {
            '4A2g->4T2g': 12065,
            '->4T1ga': 18610,
            '->4T1gb': 28410,
            '->2Eg': 15360,
            '->2T1g': 15945,
            '->2T2g': 21670,
            '->2A1g': 25520
        },
        'vertical_emission_from_4T2g': {
            '4A2g<-4T2g_Oh': 11380,
            '4B1g(4A2g)<-4B2g(4T2g)_D4h': 10425
        },
        'Stokes_shift': 1640,
        'MD_origin': 11670
    },
    'bromide': {
        'vertical_absorption': {
            '4A2g->4T2g': 12490,
            '->4T1ga': 18415,
            '->4T1gb': 28835,
            '->2Eg': 15070,
            '->2T1g': 15495,
            '->2T2g': 21200,
            '->2A1g': 25670
        },
        'vertical_emission_from_4T2g': {
            '4A2g<-4T2g_Oh': 11920,
            '4B1g(4A2g)<-4B2g(4T2g)_D4h': 11090
        },
        'Stokes_shift': 1400,
        'MD_origin': 0.0
    }
}
with open(os.path.join(os.environ['OUTDIR'], 'spectroscopic_results.json'), 'w') as f:
    json.dump(data, f, indent=2)
"

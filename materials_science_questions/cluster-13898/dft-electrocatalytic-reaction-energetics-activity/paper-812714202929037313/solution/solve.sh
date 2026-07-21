#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: dft_binding_energies.json ===
cat > "$OUTDIR/dft_binding_energies.json" <<'FFEOF'
{
  "zigzag_pyridinic": {
    "bare": {
      "binding_energy_eV": 398.7,
      "shift_vs_zigzag_pyridinic_eV": 0.0
    },
    "protonated": {
      "binding_energy_eV": 400.3,
      "shift_vs_zigzag_pyridinic_eV": 1.6,
      "protonation_shift_eV": 1.6
    },
    "OOH": {
      "binding_energy_eV": 399.1,
      "shift_vs_zigzag_pyridinic_eV": 0.4,
      "adsorbate_shift_eV": 0.4
    },
    "OH": {
      "binding_energy_eV": 399.1,
      "shift_vs_zigzag_pyridinic_eV": 0.4,
      "adsorbate_shift_eV": 0.4
    },
    "O": {
      "binding_energy_eV": 398.7,
      "shift_vs_zigzag_pyridinic_eV": 0.0,
      "adsorbate_shift_eV": 0.0
    }
  },
  "zigzag_pyridinium": {
    "bare": {
      "binding_energy_eV": 400.3,
      "shift_vs_zigzag_pyridinic_eV": 1.6
    },
    "OOH": {
      "binding_energy_eV": 402.3,
      "shift_vs_zigzag_pyridinic_eV": 3.6,
      "adsorbate_shift_eV": 2.0
    },
    "OH": {
      "binding_energy_eV": 402.3,
      "shift_vs_zigzag_pyridinic_eV": 3.6,
      "adsorbate_shift_eV": 2.0
    },
    "O": {
      "binding_energy_eV": 400.3,
      "shift_vs_zigzag_pyridinic_eV": 1.6,
      "adsorbate_shift_eV": 0.0
    }
  },
  "zigzag_oxide": {
    "bare": {
      "binding_energy_eV": 402.7,
      "shift_vs_zigzag_pyridinic_eV": 4.0
    },
    "OH": {
      "binding_energy_eV": 403.1,
      "shift_vs_zigzag_pyridinic_eV": 4.4,
      "adsorbate_shift_eV": 0.4
    },
    "OOH": {
      "binding_energy_eV": 402.7,
      "shift_vs_zigzag_pyridinic_eV": 4.0,
      "adsorbate_shift_eV": 0.0
    },
    "O": {
      "binding_energy_eV": 402.7,
      "shift_vs_zigzag_pyridinic_eV": 4.0,
      "adsorbate_shift_eV": 0.0
    }
  },
  "basal_quaternary": {
    "bare": {
      "binding_energy_eV": 401.5,
      "shift_vs_zigzag_pyridinic_eV": 2.8
    },
    "OOH": {
      "binding_energy_eV": 401.5,
      "shift_vs_zigzag_pyridinic_eV": 2.8,
      "adsorbate_shift_eV": 0.0
    },
    "OH": {
      "binding_energy_eV": 401.4,
      "shift_vs_zigzag_pyridinic_eV": 2.7,
      "adsorbate_shift_eV": -0.1
    },
    "O": {
      "binding_energy_eV": 401.9,
      "shift_vs_zigzag_pyridinic_eV": 3.2,
      "adsorbate_shift_eV": 0.4
    }
  },
  "armchair_pyridinic": {
    "bare": {
      "binding_energy_eV": 398.8,
      "shift_vs_zigzag_pyridinic_eV": 0.1
    },
    "protonated": {
      "binding_energy_eV": 400.4,
      "shift_vs_zigzag_pyridinic_eV": 1.7,
      "protonation_shift_eV": 1.6
    },
    "OOH": {
      "binding_energy_eV": 399.2,
      "shift_vs_zigzag_pyridinic_eV": 0.5,
      "adsorbate_shift_eV": 0.4
    },
    "OH": {
      "binding_energy_eV": 399.2,
      "shift_vs_zigzag_pyridinic_eV": 0.5,
      "adsorbate_shift_eV": 0.4
    },
    "O": {
      "binding_energy_eV": 398.8,
      "shift_vs_zigzag_pyridinic_eV": 0.1,
      "adsorbate_shift_eV": 0.0
    }
  },
  "armchair_pyridinium": {
    "bare": {
      "binding_energy_eV": 400.4,
      "shift_vs_zigzag_pyridinic_eV": 1.7
    },
    "OOH": {
      "binding_energy_eV": 402.4,
      "shift_vs_zigzag_pyridinic_eV": 3.7,
      "adsorbate_shift_eV": 2.0
    },
    "OH": {
      "binding_energy_eV": 402.4,
      "shift_vs_zigzag_pyridinic_eV": 3.7,
      "adsorbate_shift_eV": 2.0
    },
    "O": {
      "binding_energy_eV": 400.4,
      "shift_vs_zigzag_pyridinic_eV": 1.7,
      "adsorbate_shift_eV": 0.0
    }
  },
  "armchair_quaternary": {
    "bare": {
      "binding_energy_eV": 401.5,
      "shift_vs_zigzag_pyridinic_eV": 2.8
    },
    "OH": {
      "binding_energy_eV": 401.1,
      "shift_vs_zigzag_pyridinic_eV": 2.4,
      "adsorbate_shift_eV": -0.4
    },
    "OOH": {
      "binding_energy_eV": 401.5,
      "shift_vs_zigzag_pyridinic_eV": 2.8,
      "adsorbate_shift_eV": 0.0
    },
    "O": {
      "binding_energy_eV": 401.5,
      "shift_vs_zigzag_pyridinic_eV": 2.8,
      "adsorbate_shift_eV": 0.0
    }
  },
  "armchair_oxide": {
    "bare": {
      "binding_energy_eV": 402.7,
      "shift_vs_zigzag_pyridinic_eV": 4.0
    },
    "OH": {
      "binding_energy_eV": 403.1,
      "shift_vs_zigzag_pyridinic_eV": 4.4,
      "adsorbate_shift_eV": 0.4
    },
    "OOH": {
      "binding_energy_eV": 402.7,
      "shift_vs_zigzag_pyridinic_eV": 4.0,
      "adsorbate_shift_eV": 0.0
    },
    "O": {
      "binding_energy_eV": 402.7,
      "shift_vs_zigzag_pyridinic_eV": 4.0,
      "adsorbate_shift_eV": 0.0
    }
  }
}
FFEOF

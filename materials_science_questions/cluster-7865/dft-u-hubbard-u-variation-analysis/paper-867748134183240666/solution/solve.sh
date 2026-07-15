#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results_black_phosphorene.json ===
cat > "$OUTDIR"/results_black_phosphorene.json << 'JSONEOF'
{
  "Sc": {
    "PBE": {
      "total_spin_moment": 0.0,
      "local_spin_moment": 0.0,
      "binding_energy": 0.5,
      "classification": "nonmagnetic"
    },
    "PBE_U": {
      "total_spin_moment": 0.0,
      "local_spin_moment": 0.0,
      "binding_energy": 0.5,
      "classification": "nonmagnetic"
    }
  },
  "Ti": {
    "PBE": {
      "total_spin_moment": 1.0,
      "local_spin_moment": 0.986,
      "binding_energy": 2.0,
      "classification": "DMS"
    },
    "PBE_U": {
      "total_spin_moment": 1.0,
      "local_spin_moment": 0.986,
      "binding_energy": 2.0,
      "classification": "DMS"
    }
  },
  "V": {
    "PBE": {
      "total_spin_moment": 2.0,
      "local_spin_moment": 1.977,
      "binding_energy": 3.8,
      "classification": "DMS"
    },
    "PBE_U": {
      "total_spin_moment": 2.0,
      "local_spin_moment": 1.977,
      "binding_energy": 3.8,
      "classification": "DMS"
    }
  },
  "Cr": {
    "PBE": {
      "total_spin_moment": 3.0,
      "local_spin_moment": 3.082,
      "binding_energy": 5.5,
      "classification": "DMS"
    },
    "PBE_U": {
      "total_spin_moment": 3.0,
      "local_spin_moment": 3.082,
      "binding_energy": 5.5,
      "classification": "DMS"
    }
  },
  "Mn": {
    "PBE": {
      "total_spin_moment": 2.0,
      "local_spin_moment": 2.207,
      "binding_energy": 4.5,
      "classification": "DMS"
    },
    "PBE_U": {
      "total_spin_moment": 2.0,
      "local_spin_moment": 2.207,
      "binding_energy": 4.5,
      "classification": "DMS"
    }
  },
  "Fe": {
    "PBE": {
      "total_spin_moment": 1.0,
      "local_spin_moment": 1.097,
      "binding_energy": 3.5,
      "classification": "DMS"
    },
    "PBE_U": {
      "total_spin_moment": 1.0,
      "local_spin_moment": 1.097,
      "binding_energy": 3.5,
      "classification": "DMS"
    }
  },
  "Co": {
    "PBE": {
      "total_spin_moment": 0.0,
      "local_spin_moment": 0.0,
      "binding_energy": 2.0,
      "classification": "nonmagnetic"
    },
    "PBE_U": {
      "total_spin_moment": 0.0,
      "local_spin_moment": 0.0,
      "binding_energy": 2.0,
      "classification": "nonmagnetic"
    }
  },
  "Ni": {
    "PBE": {
      "total_spin_moment": 1.0,
      "local_spin_moment": 0.953,
      "binding_energy": 1.0,
      "classification": "DMS"
    },
    "PBE_U": {
      "total_spin_moment": 1.0,
      "local_spin_moment": 0.953,
      "binding_energy": 1.0,
      "classification": "DMS"
    }
  }
}
JSONEOF

# === solve block: results_blue_phosphorene.json ===
cat > "$OUTDIR"/results_blue_phosphorene.json << 'JSONEOF'
{
  "Sc": {
    "PBE": {
      "total_spin_moment": 0.0,
      "local_spin_moment": 0.0,
      "binding_energy": 0.6,
      "classification": "nonmagnetic"
    },
    "PBE_U": {
      "total_spin_moment": 0.0,
      "local_spin_moment": 0.0,
      "binding_energy": 0.6,
      "classification": "nonmagnetic"
    }
  },
  "Ti": {
    "PBE": {
      "total_spin_moment": 1.0,
      "local_spin_moment": 0.992,
      "binding_energy": 2.5,
      "classification": "half-metal"
    },
    "PBE_U": {
      "total_spin_moment": 1.0,
      "local_spin_moment": 0.992,
      "binding_energy": 2.5,
      "classification": "DMS"
    }
  },
  "V": {
    "PBE": {
      "total_spin_moment": 2.0,
      "local_spin_moment": 2.032,
      "binding_energy": 4.2,
      "classification": "DMS"
    },
    "PBE_U": {
      "total_spin_moment": 2.0,
      "local_spin_moment": 2.032,
      "binding_energy": 4.2,
      "classification": "DMS"
    }
  },
  "Cr": {
    "PBE": {
      "total_spin_moment": 3.0,
      "local_spin_moment": 3.147,
      "binding_energy": 6.0,
      "classification": "DMS"
    },
    "PBE_U": {
      "total_spin_moment": 3.0,
      "local_spin_moment": 3.147,
      "binding_energy": 6.0,
      "classification": "DMS"
    }
  },
  "Mn": {
    "PBE": {
      "total_spin_moment": 2.0,
      "local_spin_moment": 1.954,
      "binding_energy": 5.0,
      "classification": "DMS"
    },
    "PBE_U": {
      "total_spin_moment": 2.0,
      "local_spin_moment": 1.954,
      "binding_energy": 5.0,
      "classification": "DMS"
    }
  },
  "Fe": {
    "PBE": {
      "total_spin_moment": 1.0,
      "local_spin_moment": 1.247,
      "binding_energy": 4.0,
      "classification": "DMS"
    },
    "PBE_U": {
      "total_spin_moment": 1.0,
      "local_spin_moment": 1.247,
      "binding_energy": 4.0,
      "classification": "DMS"
    }
  },
  "Co": {
    "PBE": {
      "total_spin_moment": 0.0,
      "local_spin_moment": 0.0,
      "binding_energy": 2.5,
      "classification": "nonmagnetic"
    },
    "PBE_U": {
      "total_spin_moment": 0.0,
      "local_spin_moment": 0.0,
      "binding_energy": 2.5,
      "classification": "nonmagnetic"
    }
  },
  "Ni": {
    "PBE": {
      "total_spin_moment": 1.0,
      "local_spin_moment": 0.967,
      "binding_energy": 1.5,
      "classification": "half-metal"
    },
    "PBE_U": {
      "total_spin_moment": 1.0,
      "local_spin_moment": 0.967,
      "binding_energy": 1.5,
      "classification": "half-metal"
    }
  }
}
JSONEOF

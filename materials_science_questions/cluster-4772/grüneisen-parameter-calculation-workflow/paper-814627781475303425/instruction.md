# Reproducing Temperature-Dependent Thermodynamic Properties and Anharmonicity of Two-Dimensional Silicene and Germanene

## Problem background
Two-dimensional silicon (silicene) and germanium (germanene) possess buckled honeycomb lattices and lattice dynamics that differ markedly from their bulk counterparts, with vibrational modes that can drive anomalous thermal expansion. Chemical functionalization such as hydrogenation modifies the bonding and structural parameters, which is expected to alter the thermodynamic response. A central open question is how thermal expansion and the excitation of phonon modes together shape the temperature-dependent two-dimensional stiffness (bulk modulus) of these materials, and how this interplay changes upon hydrogenation. Answering this requires a self-consistent quasiharmonic treatment that couples the lattice constant evolution to phonon frequencies and Grüneisen parameters, yielding the relevant thermodynamic functions over a range of temperatures.

## Approach
The reproduction proceeds via hierarchical first-principles calculations using density functional theory (DFT) and density functional perturbation theory (DFPT) as implemented in Quantum ESPRESSO with ultrasoft PBE pseudopotentials. For each of the four systems—pristine silicene (Si), hydrogenated silicene (HSi), germanene (Ge), and hydrogenated germanene (HGe)—the electronic total energy is computed as a function of the in‑plane lattice constant to map the energy landscape. Phonon dispersions are calculated at several lattice constants, and from these the mode‑resolved Grüneisen parameters (the logarithmic derivative of frequency with respect to lattice constant) are derived. The self‑consistent quasiharmonic approximation (SC‑QHA) then couples the lattice constant to the phonon internal energy and Grüneisen parameters: the temperature‑dependent lattice constant is solved iteratively, updating phonon frequencies until self‑consistency. From the converged temperature‑dependent lattice constant, the thermal expansion coefficient, isovolume heat capacity, and the two‑dimensional bulk modulus (both the full quasiharmonic B2D and the quasistatic B2D*) are obtained from the electronic energy curvature and phonon contributions. Finally, the anharmonicity measure a·dB2D*/da at the equilibrium lattice constant is extracted from the curvature of the electronic energy. The workflow must respect a short‑wavelength cutoff, neglecting phonon modes with wavelengths longer than about 30 Å.

## Reproduction target
The objective is to compute and output the temperature-dependent thermodynamic functions—thermal expansion coefficient α(T), isovolume heat capacity C_V(T), and the two-dimensional bulk moduli B2D(T) and B2D*(T)—over the range 0 K to 600 K for each of the four systems: Si, HSi, Ge, HGe. Additionally, at the equilibrium lattice constant, compute the anharmonicity parameter a·dB2D*/da for each system. The assessment will be based on a comparison of the temperature derivatives dB2D/dT and dB2D*/dT at 300 K (extracted from the CSV files) as well as the four anharmonicity values against reference values that are consistent with the known physical behavior of these materials.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Ultrasoft PBE pseudopotentials (Si, Ge, H): https://www.materialscloud.org/discover/sssp/
- Python with numpy/scipy (optional): numpy scipy

## Workflow steps

### Step 1: First-principles DFT and phonon calculations for all systems
- Role: process
- Action: Using Quantum ESPRESSO with ultrasoft PBE pseudopotentials, perform geometry optimization, total energy versus in-plane lattice constant scan, and density functional perturbation theory phonon calculations at multiple lattice constants for each of the four systems: pristine silicene (Si), hydrogenated silicene (HSi), germanene (Ge), and hydrogenated germanene (HGe). Save the electronic energy-vs-a data and phonon frequencies at each a.
- Evidence: `/app/outputs/dft_calculations.log`

### Step 2: Calculation of mode Grüneisen constants
- Role: process
- Action: From the phonon frequencies at different lattice constants, compute the mode-resolved Grüneisen parameter γ(k,λ) = –(a/ω)·(dω/da) for each system.
- Evidence: `/app/outputs/gruneisen_calc.log`

### Step 3: Thermodynamic curves for silicene
- Role: scored
- Action: Run the self-consistent quasiharmonic approximation (SC-QHA) for pristine silicene (Si) using its electronic energy E^e(a), phonon frequencies, and Grüneisen constants to compute temperature-dependent lattice constant, thermal expansion coefficient α(T), isovolume heat capacity C_V(T), two-dimensional bulk modulus B2D(T), and quasistatic bulk modulus B2D_star(T) from 0 K to 600 K. Output a CSV file.
- Output file: `/app/outputs/si_thermo.csv`
- Format: csv
- Contract: CSV with header: T,alpha,C_V,B2D,B2D_star. Units: T (K), alpha (1/K), C_V (J/(mol·K)), B2D and B2D_star (eV/Å^2). At least 20 equally spaced temperature points.
- Scoring: scored by hidden verifier

### Step 4: Thermodynamic curves for hydrogenated silicene
- Role: scored
- Action: Run the self-consistent quasiharmonic approximation for hydrogenated silicene (HSi) and output a CSV file with the same quantities and temperature range.
- Output file: `/app/outputs/hsi_thermo.csv`
- Format: csv
- Contract: Same as si_thermo.csv.
- Scoring: scored by hidden verifier

### Step 5: Thermodynamic curves for germanene
- Role: scored
- Action: Run the self-consistent quasiharmonic approximation for germanene (Ge) and output a CSV file with the same quantities and temperature range.
- Output file: `/app/outputs/ge_thermo.csv`
- Format: csv
- Contract: Same as si_thermo.csv.
- Scoring: scored by hidden verifier

### Step 6: Thermodynamic curves for hydrogenated germanene
- Role: scored
- Action: Run the self-consistent quasiharmonic approximation for hydrogenated germanene (HGe) and output a CSV file with the same quantities and temperature range.
- Output file: `/app/outputs/hge_thermo.csv`
- Format: csv
- Contract: Same as si_thermo.csv.
- Scoring: scored by hidden verifier

### Step 7: Anharmonicity measures
- Role: scored (load-bearing)
- Action: Compute the anharmonicity parameter a·dB2D_star/da at the equilibrium lattice constant for each system using the curvature of the electronic total energy E^e(a). Output a JSON file with one value per system.
- Output file: `/app/outputs/anharmonicity.json`
- Format: json
- Contract: JSON object with required keys: si_a_dB2D_star_da, hsi_a_dB2D_star_da, ge_a_dB2D_star_da, hge_a_dB2D_star_da (all float, unit eV/Å^2).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/si_thermo.csv`
- `/app/outputs/hsi_thermo.csv`
- `/app/outputs/ge_thermo.csv`
- `/app/outputs/hge_thermo.csv`
- `/app/outputs/anharmonicity.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### si_thermo.csv
- path: `/app/outputs/si_thermo.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Temperature-dependent thermodynamic properties for pristine silicene from 0 K to 600 K.
- schema:
  - `type`: table
  - `required_columns`: `T`, `alpha`, `C_V`, `B2D`, `B2D_star`
  - `units`:
    - `T`: K
    - `alpha`: 1/K
    - `C_V`: J/(mol·K)
    - `B2D`: eV/Å^2
    - `B2D_star`: eV/Å^2

### hsi_thermo.csv
- path: `/app/outputs/hsi_thermo.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Temperature-dependent thermodynamic properties for hydrogenated silicene from 0 K to 600 K.
- schema:
  - `type`: table
  - `required_columns`: `T`, `alpha`, `C_V`, `B2D`, `B2D_star`
  - `units`:
    - `T`: K
    - `alpha`: 1/K
    - `C_V`: J/(mol·K)
    - `B2D`: eV/Å^2
    - `B2D_star`: eV/Å^2

### ge_thermo.csv
- path: `/app/outputs/ge_thermo.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Temperature-dependent thermodynamic properties for germanene from 0 K to 600 K.
- schema:
  - `type`: table
  - `required_columns`: `T`, `alpha`, `C_V`, `B2D`, `B2D_star`
  - `units`:
    - `T`: K
    - `alpha`: 1/K
    - `C_V`: J/(mol·K)
    - `B2D`: eV/Å^2
    - `B2D_star`: eV/Å^2

### hge_thermo.csv
- path: `/app/outputs/hge_thermo.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Temperature-dependent thermodynamic properties for hydrogenated germanene from 0 K to 600 K.
- schema:
  - `type`: table
  - `required_columns`: `T`, `alpha`, `C_V`, `B2D`, `B2D_star`
  - `units`:
    - `T`: K
    - `alpha`: 1/K
    - `C_V`: J/(mol·K)
    - `B2D`: eV/Å^2
    - `B2D_star`: eV/Å^2

### anharmonicity.json
- path: `/app/outputs/anharmonicity.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Equilibrium anharmonicity measure a·dB2D_star/da for the four systems.
- schema:
  - `type`: object
  - `required`: `si_a_dB2D_star_da`, `hsi_a_dB2D_star_da`, `ge_a_dB2D_star_da`, `hge_a_dB2D_star_da`
  - `items`:
    - `si_a_dB2D_star_da`: float (eV/Å^2)
    - `hsi_a_dB2D_star_da`: float (eV/Å^2)
    - `ge_a_dB2D_star_da`: float (eV/Å^2)
    - `hge_a_dB2D_star_da`: float (eV/Å^2)

Notes: The hidden checker recomputes temperature derivatives at 300 K from the CSV data (using central differences) and compares them to reference values with appropriate tolerances; it also compares the anharmonicity coefficients to reference values. Each CSV must contain at least 20 temperature points covering 0–600 K. Shape and completeness are part of the scoring.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "si_thermo.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "alpha",
          "C_V",
          "B2D",
          "B2D_star"
        ],
        "units": {
          "T": "K",
          "alpha": "1/K",
          "C_V": "J/(mol·K)",
          "B2D": "eV/Å^2",
          "B2D_star": "eV/Å^2"
        }
      },
      "description": "Temperature-dependent thermodynamic properties for pristine silicene from 0 K to 600 K."
    },
    {
      "file": "hsi_thermo.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "alpha",
          "C_V",
          "B2D",
          "B2D_star"
        ],
        "units": {
          "T": "K",
          "alpha": "1/K",
          "C_V": "J/(mol·K)",
          "B2D": "eV/Å^2",
          "B2D_star": "eV/Å^2"
        }
      },
      "description": "Temperature-dependent thermodynamic properties for hydrogenated silicene from 0 K to 600 K."
    },
    {
      "file": "ge_thermo.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "alpha",
          "C_V",
          "B2D",
          "B2D_star"
        ],
        "units": {
          "T": "K",
          "alpha": "1/K",
          "C_V": "J/(mol·K)",
          "B2D": "eV/Å^2",
          "B2D_star": "eV/Å^2"
        }
      },
      "description": "Temperature-dependent thermodynamic properties for germanene from 0 K to 600 K."
    },
    {
      "file": "hge_thermo.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "alpha",
          "C_V",
          "B2D",
          "B2D_star"
        ],
        "units": {
          "T": "K",
          "alpha": "1/K",
          "C_V": "J/(mol·K)",
          "B2D": "eV/Å^2",
          "B2D_star": "eV/Å^2"
        }
      },
      "description": "Temperature-dependent thermodynamic properties for hydrogenated germanene from 0 K to 600 K."
    },
    {
      "file": "anharmonicity.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "si_a_dB2D_star_da",
          "hsi_a_dB2D_star_da",
          "ge_a_dB2D_star_da",
          "hge_a_dB2D_star_da"
        ],
        "items": {
          "si_a_dB2D_star_da": "float (eV/Å^2)",
          "hsi_a_dB2D_star_da": "float (eV/Å^2)",
          "ge_a_dB2D_star_da": "float (eV/Å^2)",
          "hge_a_dB2D_star_da": "float (eV/Å^2)"
        }
      },
      "description": "Equilibrium anharmonicity measure a·dB2D_star/da for the four systems."
    }
  ],
  "notes": "The hidden checker recomputes temperature derivatives at 300 K from the CSV data (using central differences) and compares them to reference values with appropriate tolerances; it also compares the anharmonicity coefficients to reference values. Each CSV must contain at least 20 temperature points covering 0–600 K. Shape and completeness are part of the scoring."
}
```

## How you are scored
Your submission will be assessed by a hidden automated verifier that independently examines each of the scored output files. For each CSV, it will verify that the file contains the required columns and at least 20 temperature points covering 0–600 K, and then compute the temperature derivatives dB2D/dT and dB2D*/dT at 300 K using a central‑difference or polynomial‑fit method. These computed slopes are compared to hidden reference values that represent the correct physical trends; you must reproduce the correct sign and approximate magnitude. The four anharmonicity values in anharmonicity.json are compared directly to hidden reference values with a tolerance. The verifier weights the slope accuracy more heavily than the anharmonicity numbers. Simply reporting a set of numbers that happen to match the paper’s published tables is insufficient—the procedure must be the product of a genuine DFT + SC‑QHA workflow, and the verifier’s checks are designed to detect physically plausible results that arise from a correct implementation. The final reward is a weighted combination of the per‑stage scores.

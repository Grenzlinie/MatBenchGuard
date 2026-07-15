# DFT-based computation of mechanical and thermodynamic properties of monoclinic Ga₂O₃

## Problem background
Monoclinic β‑Ga₂O₃ is an ultra‑wide‑bandgap semiconductor promising for high‑efficiency power electronics. Preparing it as a two‑dimensional (2D) layer — monolayer, bilayer, or trilayer — can alter its mechanical and thermodynamic properties, which are critical for device reliability and thermal management. Understanding how key quantities such as elastic constants, sound velocities, Debye temperature, minimum thermal conductivity, and specific heat capacity vary with layer thickness is essential for rational device design. This task uses density functional theory (DFT) to compute these properties for bulk β‑Ga₂O₃ and for 2D slabs of different thicknesses, thereby revealing the thickness‑dependent trends.

## Approach
The work applies DFT with the local density approximation (LDA) to obtain equilibrium geometries and elastic response. The approach first optimises the crystal structures of bulk β‑Ga₂O₃ and of hydrogen‑passivated 2D slabs (monolayer, bilayer, trilayer). From the relaxed structures, the full set of thirteen independent elastic constants is computed using the stress‑strain method. Voigt–Reuss–Hill averaging then yields polycrystalline bulk, shear, and Young’s moduli, and Poisson’s ratio. Using these moduli and the mass density, longitudinal, transverse, and average sound velocities are derived via effective‑medium acoustic relations. The Debye temperature is obtained from the average sound velocity, the number of atoms per cell, and the cell area (for 2D) or volume (for bulk). The minimum thermal conductivity is evaluated from a semi‑empirical formula involving Young’s modulus, density, unit‑cell mass, and atom count. Finally, the isochoric heat capacity C_V is computed from the Debye model as a function of temperature up to saturation. All calculations are performed with open‑source DFT code (e.g., Quantum ESPRESSO) and publicly available LDA pseudopotentials, ensuring the procedure is reproducible without proprietary software.

## Reproduction target
Produce two scored artifacts:
1. A JSON file (`results_summary.json`) containing the elastic constants, derived moduli, sound velocities, Debye temperature, minimum thermal conductivity, and saturated heat capacity for bulk, monolayer, bilayer, and trilayer Ga₂O₃.
2. A CSV file (`C_V_curves.csv`) containing the temperature‑dependent isochoric heat capacity C_V from near 0 K to at least 1000 K for each thickness.
The results will be evaluated by a hidden verifier that compares your computed values to reference data and verifies that the thickness‑dependent trends (e.g., relative ordering of Debye temperature, minimum thermal conductivity, and saturated heat capacity) follow the expected physical direction, as required by the hidden reference.

## Assets

- β‑Ga₂O₃ crystal structure (ICSD #34243 or equivalent): https://icsd.fiz-karlsruhe.de
- Quantum ESPRESSO (open-source DFT code): https://www.quantum-espresso.org
- LDA pseudopotentials for Ga and O (SSSP efficiency library): https://www.materialscloud.org/discover/sssp/table/efficiency
- Python scientific packages (numpy, scipy, matplotlib): numpy scipy matplotlib

## Workflow steps

### Step 1: DFT geometry optimization
- Role: process
- Action: Perform DFT geometry optimization for bulk β‑Ga₂O₃ and hydrogen‑passivated 2D monoclinic Ga₂O₃ slabs (monolayer, bilayer, trilayer) using an open-source DFT code with the LDA functional. For 2D systems, add a vacuum layer of at least 15 Å. Relax cell parameters and atomic positions until forces are converged (typical threshold < 0.001 eV/Å).
- Evidence: `/app/outputs/relaxed_structures.txt`

### Step 2: Elastic constants, moduli, sound velocities, Debye temperature and k_min
- Role: scored (load-bearing)
- Action: Using the optimized structures, compute the full set of thirteen independent elastic constants Cij for each thickness (bulk, monolayer, bilayer, trilayer) with the stress‑strain method within an open‑source DFT code. Apply the Voigt–Reuss–Hill averaging scheme to obtain polycrystalline moduli: bulk modulus B, shear modulus G, Young's modulus E, and Poisson's ratio ν. Compute mass density ρ from cell volume and atomic masses. From E, ν, and ρ, calculate the longitudinal (vl), transverse (vt), and average (vm) sound velocities using effective‑medium acoustic relations. Then compute the Debye temperature ΘD using the appropriate 2D or 3D formula (involving vm, number of atoms per cell, and atomic area/volume). Finally, compute the minimum thermal conductivity k_min using a semi‑empirical formula that depends on Young's modulus, mass density, unit‑cell mass, and atom count. Report all quantities (Cij, B, G, E, ν, vl, vt, vm, ΘD, k_min, the saturated isochoric heat capacity C_V_saturated obtained from the Debye temperature, the bulk anisotropy index A_B, and the shear anisotropy index A_G) for each thickness in a single JSON file.
- Output file: `/app/outputs/results_summary.json`
- Format: json
- Contract: A JSON object with keys 'bulk', 'monolayer', 'bilayer', 'trilayer'. Each value is an object containing: 'elastic_constants' (object with keys C11..C66, C12, C13, C15, C23, C25, C35, C46; values are numbers in units GPa for bulk and N/m for 2D), 'B' (number, GPa or N/m accordingly), 'G' (number, same unit), 'E' (number, same unit), 'nu' (number, dimensionless), 'vl' (number, units m/s), 'vt' (number, units m/s), 'vm' (number, units m/s), 'Theta_D' (number, units K), 'k_min' (number, units W·cm⁻¹·K⁻¹), 'C_V_saturated' (number, units J·mol⁻¹·K⁻¹).
- Scoring: scored by hidden verifier

### Step 3: Specific heat capacity C_V(T)
- Role: scored
- Action: Using the Debye temperature ΘD obtained in the previous step, compute the isochoric specific heat capacity C_V as a function of temperature for each system using the Debye model. Generate a CSV file with columns: thickness (string, one of 'bulk','monolayer','bilayer','trilayer'), temperature_K (float, temperature in Kelvin), and C_V_J_mol_K (float, heat capacity in J·mol⁻¹·K⁻¹). Cover the temperature range from approximately 0 K up to at least 1000 K with a fine enough mesh to show the approach to saturation.
- Output file: `/app/outputs/C_V_curves.csv`
- Format: csv
- Contract: CSV with header: thickness, temperature_K, C_V_J_mol_K. 'thickness' is one of 'bulk','monolayer','bilayer','trilayer'; 'temperature_K' is a positive float; 'C_V_J_mol_K' is a float ≥ 0.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results_summary.json`
- `/app/outputs/C_V_curves.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results_summary.json
- path: `/app/outputs/results_summary.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: JSON summary of computed elastic constants, derived moduli, sound velocities, Debye temperature, minimum thermal conductivity, saturated heat capacity, and anisotropic indexes A_B and A_G for each Ga₂O₃ thickness.
- schema:
  - `type`: object
  - `required`: `bulk`, `monolayer`, `bilayer`, `trilayer`
  - `properties`:
    - `bulk`:
      - `type`: object
      - `required`: `elastic_constants`, `B`, `G`, `E`, `nu`, `vl`, `vt`, `vm`, `Theta_D`, `k_min`, `C_V_saturated`, `A_B`, `A_G`
      - `properties`:
        - `elastic_constants`:
          - `type`: object
          - `required`: `C11`, `C22`, `C33`, `C44`, `C55`, `C66`, `C12`, `C13`, `C15`, `C23`, `C25`, `C35`, `C46`
          - `additionalProperties`: False
          - `properties`: object
        - `B`:
          - `type`: number
        - `G`:
          - `type`: number
        - `E`:
          - `type`: number
        - `nu`:
          - `type`: number
        - `vl`:
          - `type`: number
        - `vt`:
          - `type`: number
        - `vm`:
          - `type`: number
        - `Theta_D`:
          - `type`: number
        - `k_min`:
          - `type`: number
        - `C_V_saturated`:
          - `type`: number
        - `A_B`:
          - `type`: number
        - `A_G`:
          - `type`: number
    - `monolayer`:
      - `$ref`: #/properties/bulk
    - `bilayer`:
      - `$ref`: #/properties/bulk
    - `trilayer`:
      - `$ref`: #/properties/bulk

### C_V_curves.csv
- path: `/app/outputs/C_V_curves.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV table of temperature‑dependent specific heat capacity curves for bulk, monolayer, bilayer, and trilayer Ga₂O₃. The curves are expected to follow a Debye‑like rise and reach saturation values matching the paper’s data within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `thickness`, `temperature_K`, `C_V_J_mol_K`
  - `columns`:
    - `thickness`:
      - `type`: string
      - `allowed`: `bulk`, `monolayer`, `bilayer`, `trilayer`
    - `temperature_K`:
      - `type`: number
      - `description`: Temperature in Kelvin
    - `C_V_J_mol_K`:
      - `type`: number
      - `description`: Isochoric heat capacity in J·mol⁻¹·K⁻¹

Notes: Added A_B and A_G fields to results_summary.json to score the anisotropic indexes from the paper. The hidden checker will compare these to gold values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results_summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "bulk",
          "monolayer",
          "bilayer",
          "trilayer"
        ],
        "properties": {
          "bulk": {
            "type": "object",
            "required": [
              "elastic_constants",
              "B",
              "G",
              "E",
              "nu",
              "vl",
              "vt",
              "vm",
              "Theta_D",
              "k_min",
              "C_V_saturated",
              "A_B",
              "A_G"
            ],
            "properties": {
              "elastic_constants": {
                "type": "object",
                "required": [
                  "C11",
                  "C22",
                  "C33",
                  "C44",
                  "C55",
                  "C66",
                  "C12",
                  "C13",
                  "C15",
                  "C23",
                  "C25",
                  "C35",
                  "C46"
                ],
                "additionalProperties": false,
                "properties": {}
              },
              "B": {
                "type": "number"
              },
              "G": {
                "type": "number"
              },
              "E": {
                "type": "number"
              },
              "nu": {
                "type": "number"
              },
              "vl": {
                "type": "number"
              },
              "vt": {
                "type": "number"
              },
              "vm": {
                "type": "number"
              },
              "Theta_D": {
                "type": "number"
              },
              "k_min": {
                "type": "number"
              },
              "C_V_saturated": {
                "type": "number"
              },
              "A_B": {
                "type": "number"
              },
              "A_G": {
                "type": "number"
              }
            }
          },
          "monolayer": {
            "$ref": "#/properties/bulk"
          },
          "bilayer": {
            "$ref": "#/properties/bulk"
          },
          "trilayer": {
            "$ref": "#/properties/bulk"
          }
        }
      },
      "description": "JSON summary of computed elastic constants, derived moduli, sound velocities, Debye temperature, minimum thermal conductivity, saturated heat capacity, and anisotropic indexes A_B and A_G for each Ga₂O₃ thickness."
    },
    {
      "file": "C_V_curves.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "thickness",
          "temperature_K",
          "C_V_J_mol_K"
        ],
        "columns": {
          "thickness": {
            "type": "string",
            "allowed": [
              "bulk",
              "monolayer",
              "bilayer",
              "trilayer"
            ]
          },
          "temperature_K": {
            "type": "number",
            "description": "Temperature in Kelvin"
          },
          "C_V_J_mol_K": {
            "type": "number",
            "description": "Isochoric heat capacity in J·mol⁻¹·K⁻¹"
          }
        }
      },
      "description": "CSV table of temperature‑dependent specific heat capacity curves for bulk, monolayer, bilayer, and trilayer Ga₂O₃. The curves are expected to follow a Debye‑like rise and reach saturation values matching the paper’s data within tolerance."
    }
  ],
  "notes": "Added A_B and A_G fields to results_summary.json to score the anisotropic indexes from the paper. The hidden checker will compare these to gold values."
}
```

## How you are scored
A hidden automated checker examines your submitted files. For `results_summary.json`, it compares each reported elastic constant, modulus, sound velocity, Debye temperature, minimum thermal conductivity, and saturated heat capacity to hidden reference values within domain‑appropriate tolerances. It also checks that the required ordering relationships among the four systems (e.g., monotonic trends in Debye temperature and minimum thermal conductivity across the different thicknesses) hold, as defined by the hidden reference. For `C_V_curves.csv`, the checker verifies that the high‑temperature saturated C_V matches the reference and that the curves follow a Debye‑like rise. Points are distributed among the scored components, with the main property summary carrying the most weight. Meeting or exceeding the required quality earns full credit; deviations reduce the score proportionally.

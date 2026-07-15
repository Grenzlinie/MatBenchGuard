# Sapphire prism-plane stacking fault energies and dislocation spacing from total energy methods

## Problem background
Stacking faults on the prism planes of sapphire (α-Al₂O₃) control the dissociation of perfect dislocations into partials, influence plasticity at elevated temperatures, and determine the equilibrium structure of low-angle grain boundaries. Accurate stacking‑fault energies (SFE) are essential for predicting these properties, but experimental measurements have varied significantly, possibly due to differences in material purity and temperature. This work addresses the need for reliable SFE values by computing the energies of the candidate prism‑plane fault structures using total energy methods, and then applying the computed energies to predict the dislocation spacing in near‑{11‑20} symmetric tilt boundaries as a function of misorientation.

## Approach
The computations proceed in several stages. First, supercell models are constructed for each of the five stacking‑fault configurations on the prism planes, guided by the known cation‑sublattice arrangements in the corundum structure. A shell‑model energy convergence test confirms that the supercells are large enough to decouple periodic images. Next, bulk sapphire is relaxed using density‑functional theory within both the local‑density approximation (LDA) and the generalized‑gradient approximation (GGA) to obtain equilibrium lattice parameters and the full set of elastic constants. Those bulk properties are used to set up supercell relaxations for each fault, yielding the stacking‑fault energy from the energy difference between the faulted and perfect cells. The stacking‑fault energy of one representative fault is also calculated using two published shell‑model Buckingham potentials at zero temperature and at a high temperature (1800 K) within the quasiharmonic approximation, to assess vibrational contributions. Finally, the LDA stacking‑fault energy for that fault and the LDA elastic constants are inserted into an anisotropic‑elasticity force‑balance model that describes the interaction of dislocation arrays; solving that model yields the equilibrium dislocation spacing for a near‑{11‑20} symmetric tilt boundary as a function of misorientation angle.

## Reproduction target
Using an open‑source density‑functional theory code and an open‑source molecular‑statics code, reproduce the following quantities: (i) the bulk rhombohedral lattice constants and elastic stiffnesses of sapphire under LDA and GGA; (ii) the stacking‑fault energies for all five prism‑plane fault geometries (a)–(e) from DFT with both functionals; (iii) the stacking‑fault energy for fault (a) from the Gale & Henson and Minervini et al. shell‑model potentials at 0 K and at 1800 K within the quasiharmonic approximation; and (iv) the equilibrium dislocation spacing of a near‑{11‑20} symmetric tilt boundary as a function of misorientation angle, evaluated at angles from 0.5° to 5.0°, derived from the computed LDA stacking‑fault energy and elastic constants.

## Assets

- Quantum ESPRESSO (or equivalent open-source DFT package): https://www.quantum-espresso.org/
- LAMMPS (or equivalent open-source molecular statics/shell-model code): https://www.lammps.org/
- Phonopy (or equivalent quasiharmonic approximation tool): phonopy
- Crystal structure of α-Al₂O₃ (sapphire): 10.1063/1.1784591
- Buckingham potential parameters for Al₂O₃: 10.1039/FT9949003175, 10.1016/S0167-2738(98)00365-9

## Workflow steps

### Step 1: Construct supercell models and convergence check
- Role: process
- Action: Construct supercell models for the five stacking-fault structures (a)–(e) using the minimal supercell sizes (fault a: 90‑atom monoclinic; faults b–e: orthorhombic cells of 100, 80, 80, 160 atoms). Perform a brief shell‑model energy convergence test using both the Gale & Henson and Minervini et al. parameters to verify that fault–image interactions are negligible (ΔSFE < 10 mJ/m²).
- Evidence: `/app/outputs/step_01_convergence_check.txt`

### Step 2: DFT bulk properties of sapphire
- Role: scored
- Action: Perform DFT relaxation of bulk α‑Al₂O₃ using LDA and GGA. Compute the equilibrium rhombohedral lattice parameter a, cos α, unit cell volume V0, and the six elastic constants c11, c12, c13, c33, c14, c44. Write the results to /app/outputs/step_02_bulk_properties.json.
- Output file: `/app/outputs/step_02_bulk_properties.json`
- Format: json
- Contract: JSON object with keys: method (string, 'LDA' or 'GGA'), a_rhombohedral (float, Å), cos_alpha (float), V0 (float, Å³), c11, c12, c13, c33, c14, c44 (float, GPa).
- Scoring: scored by hidden verifier

### Step 3: Stacking fault energy calculation
- Role: scored
- Action: Compute stacking fault energies γ_sf (J/m²) for the five prism‑plane faults (a)–(e) using DFT with both LDA and GGA. Additionally, compute the stacking fault energy for fault (a) using the two shell‑model Buckingham potentials (Gale & Henson and Minervini et al.) at 0 K and at 1800 K (via quasiharmonic free‑energy minimization). Write the complete results to /app/outputs/step_03_sfe_values.json.
- Output file: `/app/outputs/step_03_sfe_values.json`
- Format: json
- Contract: Array of objects. Each object has keys: fault_id (string, one of 'a','b','c','d','e'), LDA (float, J/m²), GGA (float, J/m²), shell_Gale_Henson_0K (float|null, J/m²), shell_Gale_Henson_1800K (float|null, J/m²), shell_Minervini_0K (float|null, J/m²), shell_Minervini_1800K (float|null, J/m²). Shell-model values are required for fault (a); for faults (b)–(e) they may be null.
- Scoring: scored by hidden verifier

### Step 4: Low-angle tilt boundary dislocation spacing
- Role: scored (load-bearing)
- Action: Using the LDA stacking fault energy for fault (a) from step_03 and the LDA elastic constants c11, c12 from step_02, solve the force‑balance equation that relates stacking-fault energy to the interaction of dislocation arrays to compute the equilibrium dislocation spacing d0 (nm) for the near‑{11‑20} symmetric tilt boundary as a function of misorientation angle θ (deg). Evaluate at θ = 0.5°, 1.0°, 1.5°, 2.0°, 2.5°, 3.0°, 4.0°, 5.0°. Write the results to /app/outputs/step_04_dislocation_spacing.csv.
- Output file: `/app/outputs/step_04_dislocation_spacing.csv`
- Format: csv
- Contract: CSV with columns: theta_deg (float), d0_nm (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_02_bulk_properties.json`
- `/app/outputs/step_03_sfe_values.json`
- `/app/outputs/step_04_dislocation_spacing.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_02_bulk_properties.json
- path: `/app/outputs/step_02_bulk_properties.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Bulk lattice and elastic properties of sapphire from DFT (LDA and GGA). The checker computes mean absolute percentage error (MAPE) against the paper's Tables I/II for each functional. Full credit if MAPE < 30% (lattice) and < 20% (elastic constants).
- schema:
  - `type`: object
  - `required`: `method`, `a_rhombohedral`, `cos_alpha`, `V0`, `c11`, `c12`, `c13`, `c33`, `c14`, `c44`
  - `properties`:
    - `method`:
      - `type`: string
    - `a_rhombohedral`:
      - `type`: number
      - `unit`: Å
    - `cos_alpha`:
      - `type`: number
    - `V0`:
      - `type`: number
      - `unit`: Å³
    - `c11`:
      - `type`: number
      - `unit`: GPa
    - `c12`:
      - `type`: number
      - `unit`: GPa
    - `c13`:
      - `type`: number
      - `unit`: GPa
    - `c33`:
      - `type`: number
      - `unit`: GPa
    - `c14`:
      - `type`: number
      - `unit`: GPa
    - `c44`:
      - `type`: number
      - `unit`: GPa

### step_03_sfe_values.json
- path: `/app/outputs/step_03_sfe_values.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Stacking-fault energies for faults (a)–(e). The checker computes MAPE against the paper's Table III values (LDA vs. LDA, GGA vs. GGA, shell-model for fault (a)). Full credit if MAPE < 20%; also checks relative ordering of fault energies (e.g., a lowest, d highest) with a structural audit.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `fault_id`, `LDA`, `GGA`
    - `properties`:
      - `fault_id`:
        - `type`: string
        - `enum`: `a`, `b`, `c`, `d`, `e`
      - `LDA`:
        - `type`: number
        - `unit`: J/m²
      - `GGA`:
        - `type`: number
        - `unit`: J/m²
      - `shell_Gale_Henson_0K`:
        - `type`: `number`, `null`
        - `unit`: J/m²
      - `shell_Gale_Henson_1800K`:
        - `type`: `number`, `null`
        - `unit`: J/m²
      - `shell_Minervini_0K`:
        - `type`: `number`, `null`
        - `unit`: J/m²
      - `shell_Minervini_1800K`:
        - `type`: `number`, `null`
        - `unit`: J/m²

### step_04_dislocation_spacing.csv
- path: `/app/outputs/step_04_dislocation_spacing.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Dislocation spacing d0 for the near-{11-20} low-angle symmetric tilt boundary. The checker computes root-mean-square error (RMSE) against gold values extracted from the paper's Fig. 3 for the same misorientation angles. Full credit if RMSE < 0.05 nm, decaying to zero at 0.2 nm.
- schema:
  - `type`: table
  - `required_columns`: `theta_deg`, `d0_nm`
  - `units`:
    - `theta_deg`: degree
    - `d0_nm`: nm

Notes: All outputs are compared to the paper's reported values (Tables I, II, III, Fig. 3) using appropriate error thresholds. The dislocation spacing step is load-bearing and depends on correct completion of steps 02 and 03.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_02_bulk_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "method",
          "a_rhombohedral",
          "cos_alpha",
          "V0",
          "c11",
          "c12",
          "c13",
          "c33",
          "c14",
          "c44"
        ],
        "properties": {
          "method": {
            "type": "string"
          },
          "a_rhombohedral": {
            "type": "number",
            "unit": "Å"
          },
          "cos_alpha": {
            "type": "number"
          },
          "V0": {
            "type": "number",
            "unit": "Å³"
          },
          "c11": {
            "type": "number",
            "unit": "GPa"
          },
          "c12": {
            "type": "number",
            "unit": "GPa"
          },
          "c13": {
            "type": "number",
            "unit": "GPa"
          },
          "c33": {
            "type": "number",
            "unit": "GPa"
          },
          "c14": {
            "type": "number",
            "unit": "GPa"
          },
          "c44": {
            "type": "number",
            "unit": "GPa"
          }
        }
      },
      "description": "Bulk lattice and elastic properties of sapphire from DFT (LDA and GGA). The checker computes mean absolute percentage error (MAPE) against the paper's Tables I/II for each functional. Full credit if MAPE < 30% (lattice) and < 20% (elastic constants)."
    },
    {
      "file": "step_03_sfe_values.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "fault_id",
            "LDA",
            "GGA"
          ],
          "properties": {
            "fault_id": {
              "type": "string",
              "enum": [
                "a",
                "b",
                "c",
                "d",
                "e"
              ]
            },
            "LDA": {
              "type": "number",
              "unit": "J/m²"
            },
            "GGA": {
              "type": "number",
              "unit": "J/m²"
            },
            "shell_Gale_Henson_0K": {
              "type": [
                "number",
                "null"
              ],
              "unit": "J/m²"
            },
            "shell_Gale_Henson_1800K": {
              "type": [
                "number",
                "null"
              ],
              "unit": "J/m²"
            },
            "shell_Minervini_0K": {
              "type": [
                "number",
                "null"
              ],
              "unit": "J/m²"
            },
            "shell_Minervini_1800K": {
              "type": [
                "number",
                "null"
              ],
              "unit": "J/m²"
            }
          }
        }
      },
      "description": "Stacking-fault energies for faults (a)–(e). The checker computes MAPE against the paper's Table III values (LDA vs. LDA, GGA vs. GGA, shell-model for fault (a)). Full credit if MAPE < 20%; also checks relative ordering of fault energies (e.g., a lowest, d highest) with a structural audit."
    },
    {
      "file": "step_04_dislocation_spacing.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "theta_deg",
          "d0_nm"
        ],
        "units": {
          "theta_deg": "degree",
          "d0_nm": "nm"
        }
      },
      "description": "Dislocation spacing d0 for the near-{11-20} low-angle symmetric tilt boundary. The checker computes root-mean-square error (RMSE) against gold values extracted from the paper's Fig. 3 for the same misorientation angles. Full credit if RMSE < 0.05 nm, decaying to zero at 0.2 nm."
    }
  ],
  "notes": "All outputs are compared to the paper's reported values (Tables I, II, III, Fig. 3) using appropriate error thresholds. The dislocation spacing step is load-bearing and depends on correct completion of steps 02 and 03."
}
```

## How you are scored
Each workflow stage’s required output artifact is independently checked by a hidden verifier. The verifier computes quantitative errors, such as mean absolute percentage error or root‑mean‑square error, between your submitted results and a stored reference that captures the target physical quantities. The final reward (0 to 1) is a weighted combination of the individual stage scores: the stacking‑fault energy stage carries the largest weight, the dislocation spacing stage the next largest, and the bulk properties stage a smaller weight; a structural consistency check adds a minor contribution. You must produce the exact output files at the specified paths and formats; missing or malformed files receive zero credit for that stage. The verifier assesses whether the computational pipeline has been faithfully executed; merely reporting literature values is not sufficient.

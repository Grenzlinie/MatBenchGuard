# Directional Mechanical Properties of Hexagonal Hydroxyapatite via Molecular Dynamics

## Problem background
Hydroxyapatite (HAP) is the primary inorganic component of bone, and its nanoscale mechanical response under tension and compression is critical for designing bone‑like biomaterials and coatings. The crystal orientation and loading direction can strongly influence the elastic modulus and failure strain, but the directional deformation mechanisms of bulk hexagonal HAP are not yet fully quantified. This task uses molecular dynamics simulations to compute the directional elastic properties of a perfect, bulk hexagonal HAP crystal. The goal is to determine the elastic moduli and failure strains for uniaxial loading along each principal axis, and to characterise any asymmetry between tension and compression.

## Approach
The approach is to construct a hexagonal HAP supercell with thousands of atoms and simulate its mechanical response using classical molecular dynamics. The interatomic forces are described by the CVFF‑Interface force field, which includes harmonic bonds, angle potentials, and long‑range Coulomb and Lennard‑Jones interactions. Starting from a minimised initial configuration, uniaxial strain is applied at a constant engineering rate along the X, Y, and Z directions, separately for tension and compression, while stress is computed from the virial. The recorded stress‑strain curves are then post‑processed: elastic moduli are extracted from a linear fit to the initial portion of the curve, and failure strains are identified from the stress drop (tension) or the peak stress (compression). This workflow yields six direction‑resolved stress‑strain datasets and a summary of the derived mechanical constants.

## Reproduction target
Produce six stress‑strain curves (CSV files) for uniaxial tension and compression of a 44,000‑atom hexagonal HAP supercell along the X, Y, and Z axes at a temperature of 10 K and a strain rate of 10¹⁰ s⁻¹. From each curve compute the elastic modulus (GPa) using a linear regression on the strain range 0 to 0.005 and the failure strain (dimensionless). Report all six moduli and six failure strains in a single JSON file. The task also requires that the relative magnitudes obey the following ordering: the elastic modulus along Z is the highest (Z > Y ≈ X), the tensile failure strain along Z is the lowest (Z < X ≈ Y), and the compressive failure strain along Z is the highest (Z > X ≈ Y). The exact numeric values are not disclosed; a hidden verifier will compare your computed quantities to the paper‑reported results.

## Assets

- LAMMPS molecular dynamics simulator: https://www.lammps.org
- CVFF-Interface force field parameters for hydroxyapatite: https://biosciences.hpc.mil/interface/
- Hexagonal HAP crystal structure data: 10.2138/rmg.2002.48.1

## Workflow steps

### Step 1: Build hexagonal HAP unit cell
- Role: process
- Action: Construct the hexagonal HAP unit cell (space group P6₃/m, a=9.417 Å, b=9.417 Å, c=6.875 Å) using atomic coordinates from the public crystallographic reference (Kay et al., 1964). Assign atom types (Ca, P, O, H), masses, and partial charges consistent with the CVFF-Interface force field. Write a LAMMPS data file for the 44-atom unit cell.
- Evidence: `/app/outputs/hap_unitcell.data`

### Step 2: Generate 10×10×10 bulk supercell
- Role: process
- Action: Replicate the unit cell 10 times in X, Y, and Z directions to obtain a 44,000-atom supercell with periodic boundary conditions. Write the resulting configuration as a LAMMPS data file.
- Evidence: `/app/outputs/hap_supercell.data`

### Step 3: Uniaxial tension simulation along X and record stress-strain curve
- Role: scored
- Action: Using the CVFF-Interface force field, perform conjugate-gradient energy minimization on the supercell. Run uniaxial tension along X at T=10 K, engineering strain rate 1e10 /s, timestep 0.5 fs, Ewald summation, 9.5 Å LJ cutoff. Record engineering stress (virial, converted to GPa) and engineering strain at each step; write a CSV with columns 'strain,stress' covering the full loading up to failure.
- Output file: `/app/outputs/stress_strain_curve_tension_X.csv`
- Format: csv
- Contract: Two columns: strain (dimensionless), stress (GPa).
- Scoring: scored by hidden verifier

### Step 4: Uniaxial tension simulation along Y and record stress-strain curve
- Role: scored
- Action: Run uniaxial tension along Y with the same simulation parameters as X. Write a CSV file 'strain,stress'.
- Output file: `/app/outputs/stress_strain_curve_tension_Y.csv`
- Format: csv
- Contract: Two columns: strain (dimensionless), stress (GPa).
- Scoring: scored by hidden verifier

### Step 5: Uniaxial tension simulation along Z and record stress-strain curve
- Role: scored
- Action: Run uniaxial tension along Z with the same simulation parameters as X. Write a CSV file 'strain,stress'.
- Output file: `/app/outputs/stress_strain_curve_tension_Z.csv`
- Format: csv
- Contract: Two columns: strain (dimensionless), stress (GPa).
- Scoring: scored by hidden verifier

### Step 6: Uniaxial compression simulation along X and record stress-strain curve
- Role: scored
- Action: Run uniaxial compression along X with the same simulation parameters. Write a CSV file 'strain,stress'.
- Output file: `/app/outputs/stress_strain_curve_compression_X.csv`
- Format: csv
- Contract: Two columns: strain (dimensionless), stress (GPa).
- Scoring: scored by hidden verifier

### Step 7: Uniaxial compression simulation along Y and record stress-strain curve
- Role: scored
- Action: Run uniaxial compression along Y with the same simulation parameters. Write a CSV file 'strain,stress'.
- Output file: `/app/outputs/stress_strain_curve_compression_Y.csv`
- Format: csv
- Contract: Two columns: strain (dimensionless), stress (GPa).
- Scoring: scored by hidden verifier

### Step 8: Uniaxial compression simulation along Z and record stress-strain curve
- Role: scored
- Action: Run uniaxial compression along Z with the same simulation parameters. Write a CSV file 'strain,stress'.
- Output file: `/app/outputs/stress_strain_curve_compression_Z.csv`
- Format: csv
- Contract: Two columns: strain (dimensionless), stress (GPa).
- Scoring: scored by hidden verifier

### Step 9: Extract directional elastic moduli and failure strains
- Role: scored (load-bearing)
- Action: From each of the six CSV files, compute the elastic modulus as the slope of a linear regression on the data in the strain range [0, 0.005]. Determine the failure strain: for tension, the strain where the stress first drops by at least 20% below the observed peak after the peak; for compression, the strain at the absolute maximum stress (peak). Report the six moduli (GPa) and six failure strains (absolute strain for compression) in a JSON file with the structure: {"tension": {"X": {"E_modulus_GPa": …, "failure_strain": …}, "Y": {…}, "Z": {…}}, "compression": {"X": {"E_modulus_GPa": …, "failure_strain_abs": …}, "Y": {…}, "Z": {…}}}.
- Output file: `/app/outputs/summary.json`
- Format: json
- Contract: A JSON object with keys 'tension' and 'compression', each containing sub-objects for 'X','Y','Z' with fields: 'E_modulus_GPa' (number) and 'failure_strain' (number) for tension, or 'failure_strain_abs' (number) for compression.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/stress_strain_curve_tension_X.csv`
- `/app/outputs/stress_strain_curve_tension_Y.csv`
- `/app/outputs/stress_strain_curve_tension_Z.csv`
- `/app/outputs/stress_strain_curve_compression_X.csv`
- `/app/outputs/stress_strain_curve_compression_Y.csv`
- `/app/outputs/stress_strain_curve_compression_Z.csv`
- `/app/outputs/summary.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### stress_strain_curve_tension_X.csv
- path: `/app/outputs/stress_strain_curve_tension_X.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Stress-strain data for uniaxial tension along X; the checker recomputes elastic modulus and failure strain from this file.
- schema:
  - `type`: table
  - `required_columns`: `strain`, `stress`
  - `units`:
    - `strain`: dimensionless
    - `stress`: GPa

### stress_strain_curve_tension_Y.csv
- path: `/app/outputs/stress_strain_curve_tension_Y.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Stress-strain data for uniaxial tension along Y.
- schema:
  - `type`: table
  - `required_columns`: `strain`, `stress`
  - `units`:
    - `strain`: dimensionless
    - `stress`: GPa

### stress_strain_curve_tension_Z.csv
- path: `/app/outputs/stress_strain_curve_tension_Z.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Stress-strain data for uniaxial tension along Z.
- schema:
  - `type`: table
  - `required_columns`: `strain`, `stress`
  - `units`:
    - `strain`: dimensionless
    - `stress`: GPa

### stress_strain_curve_compression_X.csv
- path: `/app/outputs/stress_strain_curve_compression_X.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Stress-strain data for uniaxial compression along X.
- schema:
  - `type`: table
  - `required_columns`: `strain`, `stress`
  - `units`:
    - `strain`: dimensionless
    - `stress`: GPa

### stress_strain_curve_compression_Y.csv
- path: `/app/outputs/stress_strain_curve_compression_Y.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Stress-strain data for uniaxial compression along Y.
- schema:
  - `type`: table
  - `required_columns`: `strain`, `stress`
  - `units`:
    - `strain`: dimensionless
    - `stress`: GPa

### stress_strain_curve_compression_Z.csv
- path: `/app/outputs/stress_strain_curve_compression_Z.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Stress-strain data for uniaxial compression along Z.
- schema:
  - `type`: table
  - `required_columns`: `strain`, `stress`
  - `units`:
    - `strain`: dimensionless
    - `stress`: GPa

### summary.json
- path: `/app/outputs/summary.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Derived directional elastic moduli (GPa) and failure strains (dimensionless). The checker compares these to hidden gold and verifies the relative ordering: moduli Z > Y ≈ X; tensile failure Z < X ≈ Y; compressive failure Z > X ≈ Y.
- schema:
  - `type`: object
  - `required`:
    - `tension`:
      - `X`:
        - `E_modulus_GPa`: number
        - `failure_strain`: number
      - `Y`:
        - `E_modulus_GPa`: number
        - `failure_strain`: number
      - `Z`:
        - `E_modulus_GPa`: number
        - `failure_strain`: number
    - `compression`:
      - `X`:
        - `E_modulus_GPa`: number
        - `failure_strain_abs`: number
      - `Y`:
        - `E_modulus_GPa`: number
        - `failure_strain_abs`: number
      - `Z`:
        - `E_modulus_GPa`: number
        - `failure_strain_abs`: number

Notes: The checker recomputes elastic moduli (linear regression on strain 0–0.005) and failure strains (peak-drop rule for tension, peak for compression) from the six CSV files. Those recomputed values are compared to hidden gold from the paper; the summary.json values are additionally checked for consistency and correct ordinal trends.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "stress_strain_curve_tension_X.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain",
          "stress"
        ],
        "units": {
          "strain": "dimensionless",
          "stress": "GPa"
        }
      },
      "description": "Stress-strain data for uniaxial tension along X; the checker recomputes elastic modulus and failure strain from this file."
    },
    {
      "file": "stress_strain_curve_tension_Y.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain",
          "stress"
        ],
        "units": {
          "strain": "dimensionless",
          "stress": "GPa"
        }
      },
      "description": "Stress-strain data for uniaxial tension along Y."
    },
    {
      "file": "stress_strain_curve_tension_Z.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain",
          "stress"
        ],
        "units": {
          "strain": "dimensionless",
          "stress": "GPa"
        }
      },
      "description": "Stress-strain data for uniaxial tension along Z."
    },
    {
      "file": "stress_strain_curve_compression_X.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain",
          "stress"
        ],
        "units": {
          "strain": "dimensionless",
          "stress": "GPa"
        }
      },
      "description": "Stress-strain data for uniaxial compression along X."
    },
    {
      "file": "stress_strain_curve_compression_Y.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain",
          "stress"
        ],
        "units": {
          "strain": "dimensionless",
          "stress": "GPa"
        }
      },
      "description": "Stress-strain data for uniaxial compression along Y."
    },
    {
      "file": "stress_strain_curve_compression_Z.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain",
          "stress"
        ],
        "units": {
          "strain": "dimensionless",
          "stress": "GPa"
        }
      },
      "description": "Stress-strain data for uniaxial compression along Z."
    },
    {
      "file": "summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "tension": {
            "X": {
              "E_modulus_GPa": "number",
              "failure_strain": "number"
            },
            "Y": {
              "E_modulus_GPa": "number",
              "failure_strain": "number"
            },
            "Z": {
              "E_modulus_GPa": "number",
              "failure_strain": "number"
            }
          },
          "compression": {
            "X": {
              "E_modulus_GPa": "number",
              "failure_strain_abs": "number"
            },
            "Y": {
              "E_modulus_GPa": "number",
              "failure_strain_abs": "number"
            },
            "Z": {
              "E_modulus_GPa": "number",
              "failure_strain_abs": "number"
            }
          }
        }
      },
      "description": "Derived directional elastic moduli (GPa) and failure strains (dimensionless). The checker compares these to hidden gold and verifies the relative ordering: moduli Z > Y ≈ X; tensile failure Z < X ≈ Y; compressive failure Z > X ≈ Y."
    }
  ],
  "notes": "The checker recomputes elastic moduli (linear regression on strain 0–0.005) and failure strains (peak-drop rule for tension, peak for compression) from the six CSV files. Those recomputed values are compared to hidden gold from the paper; the summary.json values are additionally checked for consistency and correct ordinal trends."
}
```

## How you are scored
The hidden verifier independently recomputes the elastic moduli and failure strains from the stress‑strain CSV files you submit. The recomputed values are compared against hidden reference values (derived from the paper) with appropriate tolerances. Additionally, the verifier checks the summary.json for internal consistency with the CSV data and confirms that the ordinal relationships between directions (Z vs. X/Y) are correct. The final reward is a weighted sum of three components: accuracy of the elastic moduli, accuracy of the failure strains, and correctness of the directional ordering. Simply copying the paper’s numbers into the summary file without valid underlying simulation curves will not satisfy the scoring, because the verifier always recomputes from the raw CSV data.

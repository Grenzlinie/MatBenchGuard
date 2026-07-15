# Classical Nucleation Theory Critical Size Calculation

## Problem background
Classical binary ion-induced nucleation (IIN) theory uses the Kelvin–Thomson equation to predict critical cluster sizes but assumes a flat monomer concentration profile near the charged cluster, neglecting the interaction between the cluster's electric field and the permanent dipole moments of polar condensing vapours. This task addresses the formation of binary sulfuric acid–water cluster ions and investigates whether the inclusion of dipole–charge interactions alters the size of the critical cluster compared to the classical theory prediction. The objective is to compute and compare critical cluster diameters from both models under specified atmospheric conditions.

## Approach
Two models of binary ion-induced nucleation are solved numerically for the H₂SO₄–H₂O system. The classical IIN baseline uses the Kelvin–Thomson equation for a singly charged cluster (q = 1) to determine the critical cluster diameter. The generalized model extends the classical theory by incorporating a correction term that accounts for the enhancement of the vapour pressure over the charged cluster surface due to the dipole–charge interaction. Both models require the same set of bulk thermophysical parameters (surface tension, density, dielectric constant, molecular masses, partial molar volumes) for sulfuric acid and water at the target temperature. The critical cluster diameters are obtained by solving the respective equilibrium equations at T = 273.15 K, relative humidity RH = 0.95, and H₂SO₄ gas-phase number concentration 10⁸ cm⁻³. The two computed diameters are then compared.

## Reproduction target
Calculate the critical cluster diameter for the classical Kelvin–Thomson ion-induced nucleation model and for the generalized model that includes the dipole–charge correction. Both calculations use the same ambient conditions: temperature 273.15 K, relative humidity 0.95, sulfuric acid concentration 10⁸ cm⁻³, and a singly charged cluster ion. The computed diameters (in nanometres) must be written to `critical_diameters.json`. The hidden verifier checks that both fields in the JSON are positive numbers and assesses the correctness of the reported values.

## Assets

- numpy: numpy
- scipy: scipy
- Thermophysical parameters for H2SO4–H2O system

## Workflow steps

### Step 1: Assemble bulk thermophysical parameters
- Role: process
- Action: Collect bulk thermophysical constants (surface tension, density, dielectric constant, molecular masses, partial molar volumes) for sulfuric acid and water at T=273.15 K from standard references (CRC Handbook, Kulmala et al. 1998, Myhre et al. 1998).
- Evidence: `/app/outputs/parameters.json`

### Step 2: Classical IIN critical cluster calculation
- Role: process
- Action: Implement the classical Kelvin-Thomson equation for binary ion-induced nucleation (q=1) using the assembled parameters. Solve for the critical cluster diameter at T=273.15 K, RH=0.95, and H2SO4 concentration 10^8 cm^{-3}.
- Evidence: `/app/outputs/classical_diameter.txt`

### Step 3: Present model critical cluster calculation
- Role: process
- Action: Implement the generalized equilibrium equations that include the dipole-charge correction term C_i(r,l_i,T) using the same parameters. Solve for the critical cluster diameter at identical ambient conditions (T=273.15 K, RH=0.95, H2SO4=10^8 cm^{-3}).
- Evidence: `/app/outputs/present_diameter.txt`

### Step 4: Output critical diameter comparison
- Role: scored (load-bearing)
- Action: Write the critical cluster diameters from the classical IIN model and the present model into a JSON file.
- Output file: `/app/outputs/critical_diameters.json`
- Format: json
- Contract: {"classical_IIN_diameter_nm": float, "present_model_diameter_nm": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/critical_diameters.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### critical_diameters.json
- path: `/app/outputs/critical_diameters.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Critical cluster diameters from the classical IIN theory and the present dipole-charge corrected model. The checker validates that both are positive and assesses the physical consistency of the values.
- schema:
  - `type`: object
  - `required`:
    - `classical_IIN_diameter_nm`: number
    - `present_model_diameter_nm`: number
  - `units`:
    - `classical_IIN_diameter_nm`: nm
    - `present_model_diameter_nm`: nm

Notes: Only structural validity and physical consistency are scored; exact numerical agreement with the paper is not required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "critical_diameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "classical_IIN_diameter_nm": "number",
          "present_model_diameter_nm": "number"
        },
        "units": {
          "classical_IIN_diameter_nm": "nm",
          "present_model_diameter_nm": "nm"
        }
      },
      "description": "Critical cluster diameters from the classical IIN theory and the present dipole-charge corrected model. The checker validates that both are positive and assesses the physical consistency of the values."
    }
  ],
  "notes": "Only structural validity and physical consistency are scored; exact numerical agreement with the paper is not required."
}
```

## How you are scored
A hidden verifier inspects the produced `critical_diameters.json` file. It validates that the JSON contains exactly two numeric fields, `classical_IIN_diameter_nm` and `present_model_diameter_nm`, that both values are positive. It then assesses the correctness of the submitted values based on physical consistency. No other artifacts are checked for scoring. The final reward depends on this assessment. Simply reporting a number from any external source is not sufficient; the values must be physically reasonable and consistent with the physics implemented in the workflow.

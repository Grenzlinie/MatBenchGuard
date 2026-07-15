# Crack-Mechanics Damage and Plasticity Model Simulation

## Problem background
Brittle materials like ceramics and concrete develop microcracks under loading, which can grow, interact, and lead to macroscopic damage. Under high confinement (e.g., uniaxial strain), plastic deformation may also occur. The Plastic-DCA model couples an isotropic damage model based on microcrack growth with rate-independent von Mises plasticity to predict the coupled stress–strain response and crack evolution. In this task, we apply the model to a silicon carbide (SiC) material under uniaxial strain loading, where both crack growth and plasticity can be active, and we examine the resulting axial stress and mean crack radius.

## Approach
The constitutive framework assumes an isotropic exponential distribution of penny-shaped cracks whose damage is represented by a mean crack radius. The damage tensor contains contributions from crack opening (active only under tensile stress states) and crack shearing; it scales with the cube of the mean crack radius. Crack growth rate is determined by a stability-based damage function that compares the current stress state to a critical surface; the growth is bounded by a terminal speed (Rayleigh or shear wave speed). Plasticity is modeled with the von Mises yield criterion and an associated flow rule using a constant yield stress (perfect plasticity). The numerical integration uses a staggered algorithm: in each time step, the damage (crack growth) update is performed first assuming no plastic flow (the DCA routine), yielding a trial stress. If the trial von Mises stress exceeds the yield stress, a plastic correction is applied by returning the stress deviator radially to the yield surface while keeping the pressure unchanged. The resulting algorithm is applied step‑by‑step to update stress, mean crack radius, and plastic strain for a prescribed strain increment. The workflow requires implementing this model from scratch for the SiC material constants provided, and then running two uniaxial strain simulations: one cyclic loading path and one monotonic compression path, both at a constant strain rate of 1×10⁵ s⁻¹.

## Reproduction target
Produce two CSV files:
1. cyclic_response.csv: Time‑series output for the cyclic uniaxial strain loading (tension to strain 0.01, compression to −5×10⁻⁴, re‑tension to 0.02) with columns strain, axial_stress_Mbar, mean_crack_radius_cm, axial_plastic_strain.
2. compressive_response.csv: Time‑series output for monotonic compression to strain −0.2 with columns strain, axial_stress_Mbar, mean_crack_radius_cm.

A hidden verifier will derive scalar targets from these artifacts: the axial stress at ε₁₁ = −0.2, the mean crack radius (normalized by the initial radius) at that strain, and the peak axial stress occurring during the first tensile loading phase of the cyclic case. The verifier compares each derived value against a reference with appropriate numerical tolerances. No reference values are disclosed; the goal is to reproduce the physics of the Plastic‑DCA model for the given SiC parameters.

## Assets
No external datasets, pretrained models, or specialized tools are needed. All required material constants for SiC are listed in the workflow steps. The implementation can rely on standard Python scientific computing libraries such as numpy and scipy.

## Workflow steps

### Step 1: Implement Plastic-DCA model
- Role: process
- Action: Implement the Plastic-DCA constitutive model in Python, including the isotropic damage model (damage tensor, crack growth rate), von Mises plasticity with associated flow rule, and the staggered stress-update algorithm. Use the SiC material constants: density 3.177 g/cm³, shear modulus 1.869 Mbar, Poisson's ratio 0.16, initial crack number density 1e5 cm⁻³, initial mean crack radius 14e-4 cm, surface energy 1e-8 Mbar·cm, friction coefficient 0.26, yield stress 0.125 Mbar. The implementation should be self-contained, relying only on standard scientific computing libraries.
- Evidence: `/app/outputs/plastic_dca_model.py`

### Step 2: Cyclic loading simulation
- Role: scored (load-bearing)
- Action: Run the implemented Plastic-DCA model under cyclic uniaxial strain at a constant strain rate of 1e5 1/s for SiC. The strain path is: (1) tension to axial strain 0.01, (2) compression to -5e-4, (3) re-tension to 0.02. At each time step, record axial strain, axial stress (Mbar), mean crack radius (cm), and axial plastic strain. Write the data to /app/outputs/cyclic_response.csv.
- Output file: `/app/outputs/cyclic_response.csv`
- Format: csv
- Contract: CSV with header: strain,axial_stress_Mbar,mean_crack_radius_cm,axial_plastic_strain
- Scoring: scored by hidden verifier

### Step 3: Large compression simulation
- Role: scored (load-bearing)
- Action: Run the implemented Plastic-DCA model under monotonic uniaxial compressive strain to -0.2 at a constant strain rate of 1e5 1/s for SiC. At each time step, record axial strain, axial stress (Mbar), and mean crack radius (cm). Write the data to /app/outputs/compressive_response.csv.
- Output file: `/app/outputs/compressive_response.csv`
- Format: csv
- Contract: CSV with header: strain,axial_stress_Mbar,mean_crack_radius_cm
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/cyclic_response.csv`
- `/app/outputs/compressive_response.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### cyclic_response.csv
- path: `/app/outputs/cyclic_response.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Time-series data from cyclic uniaxial strain loading simulation. The checker derives the peak axial stress during first tension and confirms negligible plastic strain.
- schema:
  - `type`: table
  - `required_columns`: `strain`, `axial_stress_Mbar`, `mean_crack_radius_cm`, `axial_plastic_strain`
  - `units`:
    - `strain`: unitless
    - `axial_stress_Mbar`: Mbar
    - `mean_crack_radius_cm`: cm
    - `axial_plastic_strain`: unitless

### compressive_response.csv
- path: `/app/outputs/compressive_response.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Time-series data from monotonic compressive uniaxial strain loading simulation. The checker extracts axial stress and mean crack radius at strain -0.2 and compares them to hidden paper‑reported values within tolerances.
- schema:
  - `type`: table
  - `required_columns`: `strain`, `axial_stress_Mbar`, `mean_crack_radius_cm`
  - `units`:
    - `strain`: unitless
    - `axial_stress_Mbar`: Mbar
    - `mean_crack_radius_cm`: cm

Notes: The hidden checker will extract scalar quantities from the submitted CSV files and compare them to paper-reported gold values using relative tolerances. No gold values are disclosed in this contract.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "cyclic_response.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain",
          "axial_stress_Mbar",
          "mean_crack_radius_cm",
          "axial_plastic_strain"
        ],
        "units": {
          "strain": "unitless",
          "axial_stress_Mbar": "Mbar",
          "mean_crack_radius_cm": "cm",
          "axial_plastic_strain": "unitless"
        }
      },
      "description": "Time-series data from cyclic uniaxial strain loading simulation. The checker derives the peak axial stress during first tension and confirms negligible plastic strain."
    },
    {
      "file": "compressive_response.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain",
          "axial_stress_Mbar",
          "mean_crack_radius_cm"
        ],
        "units": {
          "strain": "unitless",
          "axial_stress_Mbar": "Mbar",
          "mean_crack_radius_cm": "cm"
        }
      },
      "description": "Time-series data from monotonic compressive uniaxial strain loading simulation. The checker extracts axial stress and mean crack radius at strain -0.2 and compares them to hidden paper‑reported values within tolerances."
    }
  ],
  "notes": "The hidden checker will extract scalar quantities from the submitted CSV files and compare them to paper-reported gold values using relative tolerances. No gold values are disclosed in this contract."
}
```

## How you are scored
Your submitted CSV files will be automatically evaluated by a hidden verifier. The verifier reads cyclic_response.csv and compressive_response.csv, extracts the target scalar quantities (axial stress at ε₁₁ = −0.2, mean crack radius at that strain, and the peak axial stress during the first tensile loading), and compares them to reference values with permissive numerical tolerances. The overall reward is a weighted combination of the scores from the two artifacts. Simply writing a plausible number is insufficient; your implementation must faithfully execute the Plastic‑DCA constitutive integration for the given SiC material parameters and loading paths to achieve a high score.

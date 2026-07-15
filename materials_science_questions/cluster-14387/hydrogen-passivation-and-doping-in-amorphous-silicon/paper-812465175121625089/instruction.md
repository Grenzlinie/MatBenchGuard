# Harmonic and quasiharmonic defect properties of bond-centred hydrogen-like impurities in silicon

## Problem background
Hydrogen, deuterium, and muonium (a light pseudoisotope) as isolated impurities in crystalline silicon occupy the bond-centre (BC) site, where they exhibit strong quantum delocalisation effects due to their low mass. Path-integral Monte Carlo (PIMC) simulations have shown that the impurity's defect energy, kinetic energy, and spatial distribution depend sensitively on the impurity mass and that anharmonicity of the Si–H potential leads to deviations from a simple harmonic picture. This task reproduces the predictions of the one-particle harmonic (HA) and quasiharmonic (QHA) approximations for these properties, which serve as baseline comparisons for the full PIMC results.

## Approach
The one-particle harmonic approximation models the impurity as a three-dimensional harmonic oscillator with an axial symmetric potential: a force constant k_parallel = 18.42 eV/Å² for motion along the [111] bond axis and a perpendicular constant k_perp = 3.50 eV/Å² (isotropic in the plane). The impurity masses are: H = 1.00794 u, D = 2.0141 u, and muonium (Mu) with a muon mass of 0.1134 u (the electron of the muonium centre is effectively massless in this treatment). Using standard statistical mechanics for a quantum harmonic oscillator, the defect energy, kinetic energy, and the thermal density matrix are computed. From the latter, the probability density of the Si–I–Si bond angle at a given temperature is derived by mapping the impurity's three-dimensional displacement onto the angular coordinate. In the quasiharmonic approximation, the Si–Si distance of the nearest neighbours is fixed at the PIMC average value d = 2.899 Å, and the perpendicular force constant is recalculated via the linear relation k_perp(d) = 13.84 d – 37.30 eV/Å², while the parallel constant is assumed unchanged. The harmonic oscillator equations are then evaluated in the same way, yielding an alternative angle distribution.

## Reproduction target
Your task is to produce four CSV files containing the following computed quantities:

1. Defect energies (in eV) for H, D, and Mu at temperatures 0, 50, 100, 200, 300, and 400 K, computed with the one-particle harmonic approximation using the given force constants and masses.
2. Kinetic energies (in eV) of H, D, and Mu at T = 50 K, computed within the same harmonic approximation.
3. The probability density of the Si–I–Si angle (in degrees) for muonium at 50 K under the harmonic approximation, discretised onto a grid (column 'angle_deg' and normalised 'pdf_HA').
4. The same angle probability density for muonium at 50 K under the quasiharmonic approximation (column 'angle_deg' and 'pdf_QHA'), using d = 2.899 Å and the recalculated k_perp.

All results must be written to the /app/outputs directory as specified in the workflow steps.

## Assets
No external datasets or pretrained models are required. All necessary numerical constants (force constants, masses, Si–Si distances, temperature list, and the linear relation) are explicitly provided in this instruction. The computation can be performed with a standard Python environment; we recommend using numpy and scipy for numerical integration if needed, but no mandatory packages beyond Python's standard library. The agent is free to install any publicly available packages.

## Workflow steps

### Step 1: Harmonic defect energies
- Role: scored
- Action: Using the force constants k_parallel=18.42 eV/Å² and k_perp=3.50 eV/Å², the impurity masses (H: 1.00794 u, D: 2.0141 u, Mu: muon mass 0.1134 u), and the one-particle harmonic oscillator energy formula, compute the defect energy for each impurity at temperatures 0, 50, 100, 200, 300, and 400 K. Output as a CSV file.
- Output file: `/app/outputs/defect_energies.csv`
- Format: csv
- Contract: impurity, temperature_K, defect_energy_HA_eV
- Scoring: scored by hidden verifier

### Step 2: Kinetic energies at 50 K
- Role: scored
- Action: Using the same harmonic approximation and impurity masses, compute the kinetic energy of each impurity at T=50 K. Output as a CSV file.
- Output file: `/app/outputs/kinetic_energies.csv`
- Format: csv
- Contract: impurity, kinetic_energy_HA_eV
- Scoring: scored by hidden verifier

### Step 3: HA Si–I–Si angle distribution for muonium
- Role: scored
- Action: For muonium, compute the probability density of the Si–I–Si angle at 50 K within the one-particle harmonic approximation using force constants k_parallel and k_perp and a fixed Si–Si distance of 2.948 Å. Derive the angular distribution from the 3D harmonic oscillator thermal state and discretise it onto a suitable grid. Output as a CSV file.
- Output file: `/app/outputs/angle_dist_HA.csv`
- Format: csv
- Contract: angle_deg, pdf_HA
- Scoring: scored by hidden verifier

### Step 4: QHA Si–I–Si angle distribution for muonium
- Role: scored
- Action: For muonium, compute the Si–I–Si angle probability density at 50 K in the quasiharmonic approximation: place the nearest Si atoms at the average PIMC separation d=2.899 Å, use the linear relation k_perp(d)=13.84*d – 37.30 (in eV/Å²) to obtain the perpendicular force constant, recompute the harmonic frequencies, and derive the angular distribution. Discretise and output as a CSV file.
- Output file: `/app/outputs/angle_dist_QHA.csv`
- Format: csv
- Contract: angle_deg, pdf_QHA
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/defect_energies.csv`
- `/app/outputs/kinetic_energies.csv`
- `/app/outputs/angle_dist_HA.csv`
- `/app/outputs/angle_dist_QHA.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### defect_energies.csv
- path: `/app/outputs/defect_energies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Defect energies computed under the one-particle harmonic approximation for H, D, and Mu at specified temperatures.
- schema:
  - `type`: table
  - `required_columns`: `impurity`, `temperature_K`, `defect_energy_HA_eV`
  - `units`:
    - `defect_energy_HA_eV`: eV

### kinetic_energies.csv
- path: `/app/outputs/kinetic_energies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Kinetic energies of H, D, and Mu at T=50 K under the harmonic approximation.
- schema:
  - `type`: table
  - `required_columns`: `impurity`, `kinetic_energy_HA_eV`
  - `units`:
    - `kinetic_energy_HA_eV`: eV

### angle_dist_HA.csv
- path: `/app/outputs/angle_dist_HA.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Probability density of the Si–I–Si angle for muonium at 50 K in the one-particle harmonic approximation.
- schema:
  - `type`: table
  - `required_columns`: `angle_deg`, `pdf_HA`
  - `units`:
    - `angle_deg`: degrees

### angle_dist_QHA.csv
- path: `/app/outputs/angle_dist_QHA.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Probability density of the Si–I–Si angle for muonium at 50 K in the quasiharmonic approximation.
- schema:
  - `type`: table
  - `required_columns`: `angle_deg`, `pdf_QHA`
  - `units`:
    - `angle_deg`: degrees

Notes: The checker will discretise the angle distributions onto a common grid, compute similarity to hidden gold references, and verify structural relationships among the HA, QHA, and reference distributions. The specific criteria are held in the hidden grading specification.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "defect_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "impurity",
          "temperature_K",
          "defect_energy_HA_eV"
        ],
        "units": {
          "defect_energy_HA_eV": "eV"
        }
      },
      "description": "Defect energies computed under the one-particle harmonic approximation for H, D, and Mu at specified temperatures."
    },
    {
      "file": "kinetic_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "impurity",
          "kinetic_energy_HA_eV"
        ],
        "units": {
          "kinetic_energy_HA_eV": "eV"
        }
      },
      "description": "Kinetic energies of H, D, and Mu at T=50 K under the harmonic approximation."
    },
    {
      "file": "angle_dist_HA.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "angle_deg",
          "pdf_HA"
        ],
        "units": {
          "angle_deg": "degrees"
        }
      },
      "description": "Probability density of the Si–I–Si angle for muonium at 50 K in the one-particle harmonic approximation."
    },
    {
      "file": "angle_dist_QHA.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "angle_deg",
          "pdf_QHA"
        ],
        "units": {
          "angle_deg": "degrees"
        }
      },
      "description": "Probability density of the Si–I–Si angle for muonium at 50 K in the quasiharmonic approximation."
    }
  ],
  "notes": "The checker will discretise the angle distributions onto a common grid, compute similarity to hidden gold references, and verify structural relationships among the HA, QHA, and reference distributions. The specific criteria are held in the hidden grading specification."
}
```

## How you are scored
A hidden verifier will evaluate your submitted CSV files against reference results derived from the same closed-form expressions and the provided constants. For the energy files (defect_energies.csv and kinetic_energies.csv), the verifier recomputes the values from scratch and checks numerical agreement within a given tolerance. For the angle distribution files (angle_dist_HA.csv and angle_dist_QHA.csv), the verifier first discretises your probability density onto a common angle grid, then computes a cosine similarity score with a hidden reference distribution; it also checks that the relative widths of the HA and QHA distributions satisfy an expected physical trend without revealing that trend here. Each file is assigned a score (0 to 1), and the final reward is a weighted combination, with the energy files and the distribution files carrying comparable weight. Reporting a number without providing it in the correct CSV format or missing an expected column will result in zero credit for that file.

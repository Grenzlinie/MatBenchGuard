# Thermal conductivity of β‑Ga₂O₃ from a deep neural network interatomic potential

## Problem background
β‑Ga₂O₃ is an ultrawide‑bandgap semiconductor with great promise for power electronics, UV photodetectors, and gas sensors, but its low thermal conductivity limits device performance and reliability. Accurate prediction of the anisotropic lattice thermal conductivity requires an interatomic potential that faithfully captures both harmonic and anharmonic phonon physics. Existing empirical potentials fail for this low‑symmetry monoclinic structure. This task develops a deep neural network potential trained on ab initio data to reproduce the energy surface and atomic forces, enabling molecular dynamics simulations that compute the directional thermal conductivity and phonon transport properties of β‑Ga₂O₃.

## Approach
A DeePot‑SE neural network potential is built that expresses the total energy as a sum of atomic energies, each determined by the local chemical environment, with translational, rotational, and permutational symmetries preserved by an embedding network. The network is trained on a dataset of ab initio energies and atomic forces. Once trained, the potential is deployed in LAMMPS to perform equilibrium molecular dynamics simulations with the Green‑Kubo formalism, where the heat current autocorrelation function yields the directional lattice thermal conductivity. In parallel, the trained NNP is used with Alamode to compute harmonic force constants via finite displacements and obtain the phonon dispersion, and the molecular dynamics trajectories are combined with normal‑mode eigenvectors to carry out Green‑Kubo modal analysis, accumulating thermal conductivity contributions as a function of mode frequency.

## Reproduction target
Train a DeePot‑SE neural network potential on the provided ab initio training data. Use the trained potential to compute (a) the phonon dispersion curves along the high‑symmetry paths Γ–X, Γ–Y, and Γ–Z, (b) the anisotropic lattice thermal conductivity at 300 K in the [100], [010], and [001] crystallographic directions via Green‑Kubo equilibrium molecular dynamics, and (c) the accumulated thermal conductivity as a function of mode frequency from Green‑Kubo modal analysis. The three results must be written to the output files specified in the workflow steps.

## Assets

- NNP_Ga2O3 training dataset and potential files: https://github.com/RuiyangLi6/NNP_Ga2O3
- DeepMD‑kit (DeePot‑SE): https://github.com/deepmodeling/deepmd-kit
- LAMMPS molecular dynamics simulator: https://lammps.sandia.gov/
- Alamode phonon calculation tool: https://alamode.readthedocs.io/

## Workflow steps

### Step 1: Train the DeePot‑SE neural network potential
- Role: process
- Action: Train a deep neural network potential (DeePot‑SE) for β‑Ga₂O₃ using the training dataset from the NNP_Ga2O3 repository. Produce a frozen model file suitable for deployment in LAMMPS.
- Evidence: `/app/outputs/training.log`

### Step 2: Compute phonon dispersion
- Role: scored
- Action: Using the trained NNP and Alamode, compute harmonic force constants via finite‑displacement forces and obtain phonon dispersion curves along the high‑symmetry paths Γ–X, Γ–Y, Γ–Z. Write the frequencies to phonon_dispersion.json.
- Output file: `/app/outputs/phonon_dispersion.json`
- Format: json
- Contract: {"Gamma-X": [f1, f2, ...], "Gamma-Y": [...], "Gamma-Z": [...]}
- Scoring: scored by hidden verifier

### Step 3: Compute anisotropic lattice thermal conductivity from Green–Kubo EMD
- Role: scored (load-bearing)
- Action: Perform equilibrium molecular dynamics (EMD) simulations with LAMMPS and the trained NNP on a 4×13×7 supercell of β‑Ga₂O₃ (7280 atoms) at 300 K. Follow the Green–Kubo protocol: 200 ps NPT equilibration, then 2 ns NVE production, repeated for 15 independent runs. Compute the directional thermal conductivity κ[100], κ[010], κ[001] and write the values to thermal_conductivity.json.
- Output file: `/app/outputs/thermal_conductivity.json`
- Format: json
- Contract: {"[100]": 0.0, "[010]": 0.0, "[001]": 0.0}
- Scoring: scored by hidden verifier

### Step 4: Green–Kubo modal analysis
- Role: scored
- Action: Using the MD trajectories and harmonic eigenvectors from normal‑mode analysis, perform Green–Kubo modal analysis (GKMA) to obtain the accumulated thermal conductivity as a function of mode frequency. Write the results to accumulated_thermal_conductivity.csv.
- Output file: `/app/outputs/accumulated_thermal_conductivity.csv`
- Format: csv
- Contract: frequency(THz), accumulated_kappa_100(W/mK), accumulated_kappa_010(W/mK), accumulated_kappa_001(W/mK)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phonon_dispersion.json`
- `/app/outputs/thermal_conductivity.json`
- `/app/outputs/accumulated_thermal_conductivity.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phonon_dispersion.json
- path: `/app/outputs/phonon_dispersion.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Phonon dispersion curves along three high‑symmetry directions; the checker computes RMSE against a hidden DFT reference and scores full credit if RMSE ≤ 0.5 THz.
- schema:
  - `type`: object
  - `required`:
    - `Gamma-X`: array of float (THz)
    - `Gamma-Y`: array of float (THz)
    - `Gamma-Z`: array of float (THz)

### thermal_conductivity.json
- path: `/app/outputs/thermal_conductivity.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Anisotropic lattice thermal conductivity at 300 K; the checker compares the reported values to the paper’s reported values with a relative tolerance of ±20% for each direction and verifies the ordering κ[010] > κ[001] > κ[100].
- schema:
  - `type`: object
  - `required`:
    - `[100]`: number (W/mK)
    - `[010]`: number (W/mK)
    - `[001]`: number (W/mK)

### accumulated_thermal_conductivity.csv
- path: `/app/outputs/accumulated_thermal_conductivity.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Accumulated thermal conductivity versus mode frequency; the checker verifies monotonic increase and that the final saturated values are consistent with the total κ from thermal_conductivity.json within ±20%.
- schema:
  - `type`: table
  - `required_columns`: `frequency(THz)`, `accumulated_kappa_100(W/mK)`, `accumulated_kappa_010(W/mK)`, `accumulated_kappa_001(W/mK)`

Notes: The agent must train the NNP from scratch; using a pre‑trained potential is not allowed. The EMD simulations are computationally heavy and may benefit from remote GPU clusters; the scoring relies on re‑computation of the reported thermal conductivity values and structural checks on the modal analysis output.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phonon_dispersion.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "Gamma-X": "array of float (THz)",
          "Gamma-Y": "array of float (THz)",
          "Gamma-Z": "array of float (THz)"
        }
      },
      "description": "Phonon dispersion curves along three high‑symmetry directions; the checker computes RMSE against a hidden DFT reference and scores full credit if RMSE ≤ 0.5 THz."
    },
    {
      "file": "thermal_conductivity.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "[100]": "number (W/mK)",
          "[010]": "number (W/mK)",
          "[001]": "number (W/mK)"
        }
      },
      "description": "Anisotropic lattice thermal conductivity at 300 K; the checker compares the reported values to the paper’s reported values with a relative tolerance of ±20% for each direction and verifies the ordering κ[010] > κ[001] > κ[100]."
    },
    {
      "file": "accumulated_thermal_conductivity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "frequency(THz)",
          "accumulated_kappa_100(W/mK)",
          "accumulated_kappa_010(W/mK)",
          "accumulated_kappa_001(W/mK)"
        ]
      },
      "description": "Accumulated thermal conductivity versus mode frequency; the checker verifies monotonic increase and that the final saturated values are consistent with the total κ from thermal_conductivity.json within ±20%."
    }
  ],
  "notes": "The agent must train the NNP from scratch; using a pre‑trained potential is not allowed. The EMD simulations are computationally heavy and may benefit from remote GPU clusters; the scoring relies on re‑computation of the reported thermal conductivity values and structural checks on the modal analysis output."
}
```

## How you are scored
Each scored artifact is evaluated independently by a hidden verifier. The verifier compares your `phonon_dispersion.json` to a reference set of phonon frequencies, computes a root‑mean‑square error, and assigns a score based on a quality threshold. For `thermal_conductivity.json`, the verifier checks the reported directional values and their relative ordering against a hidden reference. The `accumulated_thermal_conductivity.csv` is checked for a monotonic increase and for final accumulated values that are consistent with the total thermal conductivity from the Green‑Kubo step. The overall reward is a weighted combination of the stage scores. Reporting a number that matches a known result without executing the workflow is not sufficient; you must produce the required artifacts with the correct structure and quality.

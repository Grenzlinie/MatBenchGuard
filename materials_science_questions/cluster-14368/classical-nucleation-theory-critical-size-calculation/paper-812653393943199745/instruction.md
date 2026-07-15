# Binary Nucleation Surface Tension Ratio from Density Functional Theory

## Problem background
Binary classical nucleation theory assumes the capillarity approximation: the surface tension of a critical nucleus equals that of a flat interface. For systems with strong composition‑dependent surface tension this leads to unphysical predictions. This work applies density functional theory (DFT) to a model binary fluid of hard‑sphere monomers and dimers to directly compute the ratio of nucleus surface tension γ to flat‑interface surface tension γ∞, providing a numerical test of the approximation. Your task is to reproduce the central computation: the ratio γ/γ∞ as a function of monomer gas‑phase activity aₘ for two fixed nucleus formation free energies, ΔΩ/ε = 60 and ΔΩ/ε = 400.

## Approach
Use the DFT grand potential functional for a binary monomer‑dimer mixture of equal‑sized hard spheres with Lennard‑Jones attractions. The functional, written in the local density approximation with interaction site formalism, includes ideal‑gas, hard‑sphere repulsion (Carnahan‑Starling), perturbative attractive contributions, and an intramolecular dimer bonding term. The planar surface tension γ∞ is obtained by minimizing this functional for a one‑dimensional interface and computing the excess free energy per area. For a given supersaturated vapor specified by monomer and dimer activities (aₘ, a_D), the spherical critical nucleus is found by minimizing the spherical DFT grand potential; the formation work ΔΩ and the liquid pressure from the homogeneous equation‑of‑state then give the nucleus surface tension γ and radius via the Laplace/work‑of‑formation relations. Compute γ/γ∞ for a range of aₘ at constant ΔΩ by interpolating a grid of spherical DFT solutions.

## Reproduction target
Produce a CSV file `gamma_ratios.csv` with columns `aM`, `gamma_ratio_60`, `gamma_ratio_400`. The table must cover monomer gas‑phase activities aₘ from 0 to 3.5 with at least 20 points, and must include points near aₘ = 1.25, 1.5, and 2.0. The ratios must be computed from the full DFT pipeline described in the workflow steps.

## Assets
No external datasets, pre‑trained models, or proprietary software are required. All model parameters (hard‑sphere diameter σ, Lennard‑Jones parameters ε, ε_ij, k_ij, temperature T/ε=0.7) are specified in the problem description. You may implement the DFT code using any programming language and open‑source scientific/numerical libraries (e.g., Python with NumPy/SciPy, or C++ with Eigen).

## Workflow steps

### Step 1: Compute planar surface tension γ∞
- Role: process
- Action: Implement the DFT grand potential functional for the binary monomer‑dimer fluid with the given Lennard‑Jones parameters and temperature T/ε=0.7. Minimize to obtain equilibrium planar gas‑liquid interface density profiles, then compute the planar surface tension γ∞ and the coexisting bulk densities. Save the γ∞ value as evidence.
- Evidence: `/app/outputs/gamma_inf.txt`

### Step 2: Scan activities to map nucleus formation free energy
- Role: process
- Action: For a grid of monomer gas‑phase activities aM (0 to 3.5) and corresponding dimer activities aD, perform spherical DFT minimizations to obtain critical nucleus density profiles and formation work ΔΩ. Store the results (aM, aD, ΔΩ, etc.) for later interpolation.
- Evidence: `/app/outputs/nuclei_grid.npz`

### Step 3: Compute and output γ/γ∞ for target ΔΩ curves
- Role: scored (load-bearing)
- Action: From the grid in step 2, identify (aM, aD) pairs that yield ΔΩ/ε = 60 and ΔΩ/ε = 400 (via interpolation). For each such aM, compute the nucleus surface tension γ using the liquid pressure from the homogeneous DFT and the Laplace/work‑of‑formation relations, then compute γ/γ∞ (using γ∞ from step 1). Write the CSV file gamma_ratios.csv with columns aM, gamma_ratio_60, gamma_ratio_400, covering aM from 0 to 3.5 with at least 20 points. Points near aM = 1.25–1.5 must be included.
- Output file: `/app/outputs/gamma_ratios.csv`
- Format: csv
- Contract: CSV with three columns: aM (monomer activity, float), gamma_ratio_60 (γ/γ∞ for ΔΩ/ε=60, float), gamma_ratio_400 (γ/γ∞ for ΔΩ/ε=400, float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/gamma_ratios.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### gamma_ratios.csv
- path: `/app/outputs/gamma_ratios.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Surface tension ratio γ/γ∞ for two constant formation free energies (ΔΩ/ε = 60 and 400) as a function of monomer gas-phase activity aM. Values must show the expected breakdown of the capillarity approximation: γ/γ∞ drops significantly for ΔΩ/ε=60, reaching a minimum near aM≈1.5, while remaining above 0.95 for ΔΩ/ε=400.
- schema:
  - `type`: table
  - `required_columns`: `aM`, `gamma_ratio_60`, `gamma_ratio_400`
  - `units`:
    - `aM`: dimensionless
    - `gamma_ratio_60`: dimensionless
    - `gamma_ratio_400`: dimensionless

Notes: The checker will compare the agent-supplied values against hidden gold references derived from figure 2, using tolerance on key points and structural checks (monotonicity, threshold).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "gamma_ratios.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "aM",
          "gamma_ratio_60",
          "gamma_ratio_400"
        ],
        "units": {
          "aM": "dimensionless",
          "gamma_ratio_60": "dimensionless",
          "gamma_ratio_400": "dimensionless"
        }
      },
      "description": "Surface tension ratio γ/γ∞ for two constant formation free energies (ΔΩ/ε = 60 and 400) as a function of monomer gas-phase activity aM. Values must show the expected breakdown of the capillarity approximation: γ/γ∞ drops significantly for ΔΩ/ε=60, reaching a minimum near aM≈1.5, while remaining above 0.95 for ΔΩ/ε=400."
    }
  ],
  "notes": "The checker will compare the agent-supplied values against hidden gold references derived from figure 2, using tolerance on key points and structural checks (monotonicity, threshold)."
}
```

## How you are scored
A hidden verifier reads `gamma_ratios.csv` and independently checks the computed γ/γ∞ ratios. It compares your values against reference data and verifies structural properties such as monotonicity and threshold conditions for each column (ΔΩ/ε = 60 and ΔΩ/ε = 400). The score is the fraction of checks passed; results not genuinely derived from the DFT calculations are unlikely to pass the spot checks.

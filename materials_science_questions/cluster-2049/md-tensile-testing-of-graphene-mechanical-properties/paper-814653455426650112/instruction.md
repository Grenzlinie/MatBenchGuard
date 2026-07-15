# DFT Band Gaps of BN-Doped Graphene: Concentration and Strain Dependence

## Problem background
Hexagonal boron nitride (h-BN) doped graphene (gr:BN) is a two-dimensional material where substituting carbon atoms with B and N opens a tunable band gap. The gap depends strongly on both the BN concentration and the spatial arrangement (morphology) of the dopants, varying over an order of magnitude for a fixed concentration. Understanding and predicting this variability, and how it is further modulated by mechanical strain, is essential for designing gr:BN-based electronic and optoelectronic devices. This task investigates the electronic structure of gr:BN by computing band gaps from first principles across a range of BN concentrations and morphologies, and examines how uniaxial tensile strain alters the gap.

## Approach
We use a two-stage computational approach. First, low-energy atomic configurations of BN-doped graphene are generated via Monte Carlo simulated annealing using a bond-energy model. This model approximates the total energy as a sum over bond contributions, with parameters taken from the literature, and the annealing procedure explores the configurational space to find structures with low energy at fixed BN concentrations. Second, for each generated configuration, density functional theory (DFT) calculations are performed with the SIESTA code to obtain an optimized geometry and the electronic band gap. The same DFT machinery is then used to compute the band gap for selected configurations under applied uniaxial tensile strain, with cell dimensions fixed and internal coordinates relaxed. The results are compared to a virtual-crystal tight-binding model that provides an upper bound for the gap.

## Reproduction target
Compute DFT band gaps for at least two distinct low-energy gr:BN configurations at each of three BN concentrations (2.08%, 6.25%, and 10.42%) using 96‑atom supercells. Produce a table of band gaps that demonstrates the trend of increasing gap with concentration and the wide spread at each concentration. Additionally, for two distinct configurations (one with small BN islands and one with a larger BN island), compute the band gap as a function of uniaxial tensile strain applied along the armchair and zigzag directions up to approximately 5%, and verify that the gap exhibits non-monotonic and anisotropic behavior.

## Assets

- SIESTA DFT code: https://gitlab.com/siesta-project/siesta
- Bond-energy model parameters (Mazzoni et al., Phys. Rev. B 73, 073108, 2006): 10.1103/PhysRevB.73.073108

## Workflow steps

### Step 1: Generate low-energy gr:BN configurations via Monte Carlo simulated annealing
- Role: process
- Action: Implement the bond-energy model from Mazzoni et al. (2006) and use Monte Carlo simulated annealing to generate low-energy BN-doped graphene atomic configurations for a 96-atom honeycomb supercell at three BN concentrations: 2.08%, 6.25%, and 10.42%. Generate at least two distinct configurations per concentration. Save the resulting atomic coordinates for subsequent DFT input.
- Evidence: none

### Step 2: Compute DFT band gaps for gr:BN configurations
- Role: scored (load-bearing)
- Action: For each generated configuration, perform DFT geometry optimization and electronic structure calculation using SIESTA. Extract the band gap. Produce a CSV file recording BN concentration, a configuration identifier, and the computed band gap in eV.
- Output file: `/app/outputs/band_gap_vs_concentration.csv`
- Format: csv
- Contract: columns: concentration (float, dimensionless), structure_id (string), band_gap_eV (float)
- Scoring: scored by hidden verifier

### Step 3: Compute strain-dependent band gaps
- Role: scored
- Action: Select two distinct gr:BN configurations (one with small BN islands and one with a larger BN island). For each, apply uniaxial tensile strain along the armchair and zigzag directions from 0% to ~5% in steps of approximately 0.01 strain. At each strain step, perform a DFT calculation with cell dimensions fixed (relaxing only internal coordinates) and extract the band gap. Write a CSV file recording the configuration, strain direction, strain value, and band gap.
- Output file: `/app/outputs/band_gap_vs_strain.csv`
- Format: csv
- Contract: columns: structure_id (string), strain_direction (string), strain (float, dimensionless), band_gap_eV (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gap_vs_concentration.csv`
- `/app/outputs/band_gap_vs_strain.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gap_vs_concentration.csv
- path: `/app/outputs/band_gap_vs_concentration.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Band gaps computed by DFT for gr:BN configurations at various BN concentrations. The checker will verify that gaps for each concentration fall within paper-reported ranges, average gap increases with concentration, and no gap exceeds the theoretical upper bound (4.5 eV * c_BN).
- schema:
  - `type`: table
  - `required_columns`: `concentration`, `structure_id`, `band_gap_eV`
  - `units`:
    - `concentration`: 
    - `band_gap_eV`: eV

### band_gap_vs_strain.csv
- path: `/app/outputs/band_gap_vs_strain.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Band gaps under uniaxial tensile strain for two gr:BN configurations. The checker will verify non-monotonic behavior (existence of at least one local extremum per direction and a sign change of the derivative) and anisotropic, opposite trends between the two configurations.
- schema:
  - `type`: table
  - `required_columns`: `structure_id`, `strain_direction`, `strain`, `band_gap_eV`
  - `units`:
    - `strain`: 
    - `band_gap_eV`: eV

Notes: All gold values and tolerances are hidden and derived from the paper's reported numbers and trends. The agent must produce the raw CSV files; the checker performs a structural audit without requiring exact numerical match.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gap_vs_concentration.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "concentration",
          "structure_id",
          "band_gap_eV"
        ],
        "units": {
          "concentration": "",
          "band_gap_eV": "eV"
        }
      },
      "description": "Band gaps computed by DFT for gr:BN configurations at various BN concentrations. The checker will verify that gaps for each concentration fall within paper-reported ranges, average gap increases with concentration, and no gap exceeds the theoretical upper bound (4.5 eV * c_BN)."
    },
    {
      "file": "band_gap_vs_strain.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "structure_id",
          "strain_direction",
          "strain",
          "band_gap_eV"
        ],
        "units": {
          "strain": "",
          "band_gap_eV": "eV"
        }
      },
      "description": "Band gaps under uniaxial tensile strain for two gr:BN configurations. The checker will verify non-monotonic behavior (existence of at least one local extremum per direction and a sign change of the derivative) and anisotropic, opposite trends between the two configurations."
    }
  ],
  "notes": "All gold values and tolerances are hidden and derived from the paper's reported numbers and trends. The agent must produce the raw CSV files; the checker performs a structural audit without requiring exact numerical match."
}
```

## How you are scored
A hidden verifier will independently audit the two output CSV files. For the band‑gap‑versus‑concentration data, it will check that the reported gaps for each concentration lie within physically reasonable bounds, that the average gap increases with concentration, and that no gap exceeds the theoretical upper limit implied by the tight-binding model. For the strain series, it will check that each gap‑versus‑strain curve shows at least one local extremum and a change in slope sign, and that the two configurations display opposite anisotropic trends (e.g., one increasing then decreasing along one direction, the other showing the reverse). The exact numerical tolerances and reference values are hidden; only the structural and trend checks are applied. The final reward is a weighted combination of the scores from the two stages.

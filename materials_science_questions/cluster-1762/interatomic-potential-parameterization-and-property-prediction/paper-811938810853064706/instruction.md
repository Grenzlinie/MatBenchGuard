# Interatomic Potential Parameterization and Phonon/Elastic Property Calculation for fcc Metals

## Problem background
Accurate prediction of phonon dispersion, elastic constants, and zero‑point energy in face‑centered cubic (fcc) metals is central to understanding their thermal, mechanical, and vibrational properties. Interatomic potentials for fcc metals must capture both the pairwise bonding and the many‑body effects arising from metallic cohesion. A long‑standing challenge is to formulate a potential that uses few adjustable parameters while still reproducing experimental phonon frequencies and elastic moduli. This task targets the computation of these observables for four fcc metals (Au, Ni, Pt, Pd) using a generalised Morse‑type two‑body potential augmented by a short‑range three‑body deformation term.

## Approach
We implement a computational workflow that starts from public input data (cohesive energy, bulk modulus, lattice constant, an exponent that controls the shape of the two‑body potential, and the Cauchy discrepancy, which measures the deviation from Cauchy relations). Using the Girifalco–Weizer method, we determine the potential parameters: dissociation energy D, hardness parameter α, equilibrium distance r₀, and the three‑body deformation parameter Q. From the potential, we compute first and second spatial derivatives up to the eighth neighbour shell in the fcc lattice to obtain the force constants α₁, β₁, α₂, β₂, and β₃. These force constants are used to construct the dynamical matrix, which is diagonalised at selected wave‑vectors along the high‑symmetry directions [100], [110], and [111] to yield phonon frequencies. Analytical expressions that sum the potential second derivatives over lattice shells provide the second‑order elastic constants C₁₁, C₁₂, and C₄₄. Finally, the phonon spectrum is integrated over the irreducible Brillouin zone using the Wallace method to obtain the vibrational zero‑point energy per mole.

## Reproduction target
For each of the four metals (Au, Ni, Pt, Pd), produce three data files:

- **phonon_frequencies.csv**: phonon frequencies at several q‑points (at least 5 per metal per high‑symmetry direction [100], [110], [111]) in THz.
- **elastic_constants.csv**: second‑order elastic constants C₁₁, C₁₂, C₄₄ in units of 10¹² dyne/cm².
- **zero_point_energy.csv**: vibrational zero‑point energy per mole in cal/mol.

All output files must follow the column formats specified in the workflow steps.

## Assets

- NumPy: numpy
- SciPy: scipy

## Input data

The following input parameters are taken from the literature and must be used to fit the potential.

**Table 1.** Two-body bulk modulus, ionic cohesive energy, semi-lattice constant, and exponent P for the four fcc metals.

| Metal | k^x (10¹² dyne/cm²) | φ^x (10⁻¹² erg) | a (nm) | P   |
|-------|---------------------|-----------------|--------|-----|
| Au    | 0.509               | 2.644           | 0.2040 | 3.15|
| Ni    | 1.571               | 3.125           | 0.1760 | 2.75|
| Pt    | 1.085               | 4.111           | 0.1960 | 2.75|
| Pd    | 0.887               | 2.738           | 0.1945 | 2.75|

*Note:* The semi-lattice constant for Pd in the original source is misprinted; the correct value is 0.1945 nm.

The Cauchy discrepancy (the deviation from Cauchy relations, in 10¹² dyne/cm²) for each metal is:

| Metal | Cauchy discrepancy (10¹² dyne/cm²) |
|-------|------------------------------------|
| Au    | 1.223                              |
| Ni    | 0.265                              |
| Pt    | 1.742                              |
| Pd    | 1.043                              |

## Potential expressions

The total interatomic potential for the fcc lattice consists of a two-body generalised Morse term and a short-range three-body deformation term.

**Two-body potential** (Eq. 2.1 of the paper, generalised Morse):

$$
\phi^x(r) = \frac{D}{P-1} \left[ \exp\bigl(-P \alpha (r_0 - r)\bigr) - P \exp\bigl(-\alpha (r_0 - r)\bigr) \right]
$$

where $D$ is the dissociation energy, $\alpha$ the hardness parameter, $r_0$ the equilibrium distance, and $P$ the exponent given in Table 1.

**Three-body potential** (Eq. 2.6, short‑range deformation):

$$
\phi^y(r_1, r_2) = \frac{Q}{2(P-1)} \sum_{\substack{m'k' \\ m''k''}} \sum_{mk}
\left[ \beta^P \exp\bigl(-\alpha P (r_1 + r_2)\bigr) - P \beta \exp\bigl(-\alpha (r_1 - r_2)\bigr) \right]
$$

with $\beta = \exp(\alpha r_0)$. $r_1$ and $r_2$ are the distances of the two neighbours from the central atom, and $Q$ is the deformation parameter which is determined from the Cauchy discrepancy.

The agent must compute the first and second spatial derivatives of these potentials (up to the 8th neighbour shell) to obtain the force constants and the dynamical matrix elements.

## Workflow steps

### Step 1: Evaluate potential parameters D, α, r₀, Q
- Role: process
- Action: Use the Girifalco–Weizer method with the input data from Table I (ionic cohesive energy, two-body bulk modulus, semi-lattice constant, exponent P) and the Cauchy discrepancy to compute the dissociation energy D, hardness α, equilibrium distance r₀, and deformation parameter Q for Au, Ni, Pt, and Pd.
- Evidence: `/app/outputs/potential_parameters.csv`

### Step 2: Derive force constants
- Role: process
- Action: Compute first and second derivatives of the two-body and three-body potentials for fcc lattice up to 8 nearest-neighbor shells, giving the force constants α₁, β₁, α₂, β₂, β₃ for each metal.
- Evidence: `/app/outputs/force_constants.csv`

### Step 3: Calculate phonon frequencies
- Role: scored (load-bearing)
- Action: Build the dynamical matrix from the force constants and solve the secular equation for wave vectors along the high-symmetry directions [100], [110], [111]. Output phonon frequencies for a representative set of q‑points for each metal.
- Output file: `/app/outputs/phonon_frequencies.csv`
- Format: csv
- Contract: CSV with columns: metal (string), qx (float, reduced coordinate), qy (float), qz (float), branch (string, e.g. 'TA','LA','TO','LO'), frequency_THz (float). At least 5 q‑points per metal per direction.
- Scoring: scored by hidden verifier

### Step 4: Compute second-order elastic constants
- Role: scored
- Action: Evaluate the analytical expressions for C₁₁, C₁₂, C₄₄ using the potential second derivatives and lattice sums.
- Output file: `/app/outputs/elastic_constants.csv`
- Format: csv
- Contract: CSV with columns: metal (string), C11 (float), C12 (float), C44 (float).
- Scoring: scored by hidden verifier

### Step 5: Calculate zero-point energy
- Role: scored
- Action: Integrate over all phonon modes in the irreducible Brillouin zone using the Wallace method to obtain the zero-point energy per mole.
- Output file: `/app/outputs/zero_point_energy.csv`
- Format: csv
- Contract: CSV with columns: metal (string), ZPE_cal_mol (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phonon_frequencies.csv`
- `/app/outputs/elastic_constants.csv`
- `/app/outputs/zero_point_energy.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phonon_frequencies.csv
- path: `/app/outputs/phonon_frequencies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Phonon frequencies for each metal at selected q‑points along high‑symmetry directions.
- schema:
  - `required_columns`: `metal`, `qx`, `qy`, `qz`, `branch`, `frequency_THz`
  - `units`:
    - `frequency_THz`: THz

### elastic_constants.csv
- path: `/app/outputs/elastic_constants.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Second‑order elastic constants C11, C12, C44 for each metal.
- schema:
  - `required_columns`: `metal`, `C11`, `C12`, `C44`
  - `units`:
    - `C11`: 1e12 dyne/cm^2
    - `C12`: 1e12 dyne/cm^2
    - `C44`: 1e12 dyne/cm^2

### zero_point_energy.csv
- path: `/app/outputs/zero_point_energy.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Vibrational zero‑point energy per mole for each metal.
- schema:
  - `required_columns`: `metal`, `ZPE_cal_mol`
  - `units`:
    - `ZPE_cal_mol`: cal/mol

Notes: All units and tolerances are defined in the hidden grading specification. The agent must re‑implement the potential fitting and property calculation from the given input tables; it must not rely on pre‑computed parameters from the paper.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phonon_frequencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "required_columns": [
          "metal",
          "qx",
          "qy",
          "qz",
          "branch",
          "frequency_THz"
        ],
        "units": {
          "frequency_THz": "THz"
        }
      },
      "description": "Phonon frequencies for each metal at selected q‑points along high‑symmetry directions."
    },
    {
      "file": "elastic_constants.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "required_columns": [
          "metal",
          "C11",
          "C12",
          "C44"
        ],
        "units": {
          "C11": "1e12 dyne/cm^2",
          "C12": "1e12 dyne/cm^2",
          "C44": "1e12 dyne/cm^2"
        }
      },
      "description": "Second‑order elastic constants C11, C12, C44 for each metal."
    },
    {
      "file": "zero_point_energy.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "required_columns": [
          "metal",
          "ZPE_cal_mol"
        ],
        "units": {
          "ZPE_cal_mol": "cal/mol"
        }
      },
      "description": "Vibrational zero‑point energy per mole for each metal."
    }
  ],
  "notes": "All units and tolerances are defined in the hidden grading specification. The agent must re‑implement the potential fitting and property calculation from the given input tables; it must not rely on pre‑computed parameters from the paper."
}
```

## How you are scored
A hidden verifier independently evaluates each of the three output files. For phonon frequencies, the verifier compares your computed values at specified q‑points to hidden reference data using a tolerance that accounts for numerical differences in the implementation. For elastic constants and zero‑point energy, the verifier compares your reported values to hidden reference values with an appropriate tolerance. The three scores are combined into a single reward between 0 and 1 according to the following weights: phonon frequencies 0.5, elastic constants 0.3, zero‑point energy 0.2. Reporting the paper's numbers without executing the full workflow will not pass.

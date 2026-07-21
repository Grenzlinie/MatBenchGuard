# Hybrid DFT Calculations of Perovskite Lattice Constants and Band Gaps

## Problem background
Ferroelectric perovskite solid solutions such as Ba₁₋ₓSrₓTiO₃ are promising candidates for memory‑cell capacitors in next‑generation dynamic random‑access memory. Accurate first‑principles modelling of these materials is challenging because standard density‑functional theory approximations systematically underestimate band gaps, while pure Hartree‑Fock overestimates them. This work addresses the question of whether a hybrid exchange‑correlation functional can faithfully reproduce the lattice constants and electronic band gaps of the parent compounds BaTiO₃ and SrTiO₃, and predict the corresponding properties of an equiatomic Ba₀.₅Sr₀.₅TiO₃ heterostructure.

## Approach
The computational approach combines periodic density‑functional theory within the linear combination of atomic orbitals (LCAO) framework with a hybrid functional. The exchange‑correlation energy is described by the B3PW scheme, which mixes 20 % of non‑local Fock exchange with Becke's gradient‑corrected exchange and the gradient‑corrected correlation of Perdew and Wang. Heavy atoms (Ti, Sr, Ba) are treated with Hay‑Wadt small‑core effective‑core pseudopotentials, while light oxygen atoms are described by an all‑electron Gaussian basis set (e.g., 8‑411(1d)G for O, 411(311d)G for Ti, 311(1d)G for Sr and Ba). Identical computational parameters are used for the cubic primitive cells of BaTiO₃ and SrTiO₃ (space group Pm‑3m) and for a 2×2×2 supercell of Ba₀.₅Sr₀.₅TiO₃ with a layered arrangement of Ba and Sr along the [001] direction. For each system the lattice constant is optimised via conjugate‑gradient minimisation with all atoms held fixed at their ideal Wyckoff positions. After optimisation the electronic band structure is calculated and the fundamental direct band gap at the Γ point is extracted.

## Reproduction target
Compute the equilibrium lattice constants (in Å) and the Γ‑point direct band gaps (in eV) for the cubic BaTiO₃ primitive cell, the cubic SrTiO₃ primitive cell, and the layered Ba₀.₅Sr₀.₅TiO₃ supercell. Write the six numbers to `/app/outputs/results.json` following the schema declared in Workflow Step 2. The calculations must be performed with a hybrid functional (B3PW or an equivalent open‑source hybrid) and the basis‑set / pseudopotential scheme described in the Approach, using an 8×8×8 Monkhorst‑Pack k‑point mesh and conjugate‑gradient lattice optimisation.

## Assets

- Periodic DFT code with hybrid functional support (e.g., Quantum ESPRESSO, ABINIT): https://www.quantum-espresso.org/ or https://www.abinit.org/
- Pseudopotentials and basis sets for Ti, Sr, Ba, O: https://www.quantum-espresso.org/pseudopotentials/ (PSlibrary, SSSP) or https://www.abinit.org/downloads/psp-links

## Workflow steps

### Step 1: Prepare crystal structures and supercell
- Role: process
- Action: Create input geometries for cubic perovskite primitive cells of BaTiO₃ and SrTiO₃ (space group Pm-3m) from standard crystallographic data. Build a 2×2×2 supercell for equiatomic Ba₀.₅Sr₀.₅TiO₃ with layered ordering along [001] by replacing alternate Ba planes with Sr. Save the structures in a format compatible with the chosen DFT code.
- Evidence: none

### Step 2: Run hybrid DFT calculations and report results
- Role: scored (load-bearing)
- Action: For each of the three systems (BaTiO₃ primitive, SrTiO₃ primitive, BST supercell) perform a hybrid DFT calculation (B3PW or equivalent open-source hybrid) using the chosen pseudopotentials/basis sets and a Monkhorst-Pack k‑mesh of 8×8×8. Optimize the lattice constant via conjugate-gradient minimization with atoms fixed at ideal positions. After optimization, compute the electronic band structure and extract the direct band gap at the Γ point. Write a single JSON file containing the six numbers.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {
  "BaTiO3_lattice_constant_angstrom": <float>,
  "SrTiO3_lattice_constant_angstrom": <float>,
  "BST_lattice_constant_angstrom": <float>,
  "BaTiO3_band_gap_eV": <float>,
  "SrTiO3_band_gap_eV": <float>,
  "BST_band_gap_eV": <float>
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Contains the optimized lattice constants and Γ‑point direct band gaps for BaTiO₃, SrTiO₃, and the BST heterostructure, all computed with a hybrid DFT functional.
- schema:
  - `type`: object
  - `required`:
    - `BaTiO3_lattice_constant_angstrom`: float
    - `SrTiO3_lattice_constant_angstrom`: float
    - `BST_lattice_constant_angstrom`: float
    - `BaTiO3_band_gap_eV`: float
    - `SrTiO3_band_gap_eV`: float
    - `BST_band_gap_eV`: float
  - `units`:
    - `BaTiO3_lattice_constant_angstrom`: angstrom
    - `SrTiO3_lattice_constant_angstrom`: angstrom
    - `BST_lattice_constant_angstrom`: angstrom
    - `BaTiO3_band_gap_eV`: eV
    - `SrTiO3_band_gap_eV`: eV
    - `BST_band_gap_eV`: eV

Notes: The target policy is exact_match because the quantities are physically determined by the DFT run; the checker compares the reported values to paper‑reported gold values with an appropriate tolerance and also verifies ordering constraints (BaTiO₃ > BST > SrTiO₃ for lattice constants).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "BaTiO3_lattice_constant_angstrom": "float",
          "SrTiO3_lattice_constant_angstrom": "float",
          "BST_lattice_constant_angstrom": "float",
          "BaTiO3_band_gap_eV": "float",
          "SrTiO3_band_gap_eV": "float",
          "BST_band_gap_eV": "float"
        },
        "units": {
          "BaTiO3_lattice_constant_angstrom": "angstrom",
          "SrTiO3_lattice_constant_angstrom": "angstrom",
          "BST_lattice_constant_angstrom": "angstrom",
          "BaTiO3_band_gap_eV": "eV",
          "SrTiO3_band_gap_eV": "eV",
          "BST_band_gap_eV": "eV"
        }
      },
      "description": "Contains the optimized lattice constants and Γ‑point direct band gaps for BaTiO₃, SrTiO₃, and the BST heterostructure, all computed with a hybrid DFT functional."
    }
  ],
  "notes": "The target policy is exact_match because the quantities are physically determined by the DFT run; the checker compares the reported values to paper‑reported gold values with an appropriate tolerance and also verifies ordering constraints (BaTiO₃ > BST > SrTiO₃ for lattice constants)."
}
```

## How you are scored
A hidden verifier reads your `results.json` and compares each of the six reported values to reference numbers within a tolerance. It also checks that the lattice constants and band gaps obey physically expected trends: the heterostructure lattice constant should lie between the lattice constants of pure BaTiO₃ and SrTiO₃, and the heterostructure band gap should similarly be intermediate between the gaps of the two parent compounds. The verifier combines these checks into a single reward between 0 and 1. Simply copying a number from the literature without performing the full DFT workflow is not sufficient; the checker may apply additional consistency or ordering checks that require genuine calculation results.

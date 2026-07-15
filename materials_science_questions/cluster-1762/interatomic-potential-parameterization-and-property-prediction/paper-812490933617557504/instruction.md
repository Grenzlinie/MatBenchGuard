# Madelung Energy Calculation for Mixed Perovskite Structures

## Problem background
Perovskite proton conductors such as doped BaCeO₃ are promising for high-temperature electrochemical devices but are known to degrade in water-containing environments. Experiments show that certain mixed perovskites with general formula AB'_{1/2}B''_{1/2}O₃ (where A=Ba, B' is trivalent, B'' pentavalent) remain structurally stable when boiled in water, unlike simple BaCeO₃. A key factor affecting stability is the electrostatic (Madelung) energy of the ionic crystal: a lower (more negative) Madelung energy generally indicates stronger ionic cohesion and suggests greater stability. In mixed perovskites, the presence of two different B-site valences alters the electrostatic interactions, potentially lowering the Madelung energy compared to a simple ABO₃ perovskite with the same lattice parameter. The computational task is to calculate Madelung energies for a set of perovskite structures to investigate this effect.

## Approach
The Madelung energy is computed by direct summation of Coulomb interactions between all ion pairs in a finite simulation supercell with periodic boundary conditions. For each perovskite compound, the equivalent cubic lattice parameter and the formal charges of the constituent ions (A²⁺, B site average +4, O²⁻) are known. A supercell of the perovskite structure is constructed. For simple ABO₃ perovskites, each B-site is occupied by a single type of B ion. For mixed AB'_{1/2}B''_{1/2}O₃ perovskites, two configurations are considered: ordered (alternating B' and B'' on the B sublattice) and disordered (random occupation of B' and B''). The total electrostatic energy is summed as E = Σ_{i<j} (z_i z_j e² / (4πε₀ r_ij)) over all ions in the supercell (including periodic images), and the result is normalized to the Madelung energy per formula unit in electronvolts. The calculation does not require any external data beyond the lattice parameters and ion valences provided in the workflow; a standard programming environment with numerical arrays is sufficient. The key comparison is between mixed (both ordered and disordered) and simple perovskites, and between ordered and disordered arrangements of the same mixed compound.

## Reproduction target
Compute the Madelung energy (in eV per formula unit) for each of the listed perovskite compounds, using the given equivalent cubic lattice parameter and ion valences. For mixed perovskites, compute energies for both ordered and disordered B-site arrangements. Report all results in the CSV file `/app/outputs/madelung_energies.csv` with columns: compound, structure_type ('simple', 'mixed_ordered', 'mixed_disordered'), lattice_param_A (Å), and Madelung_energy_eV (eV). The target is to obtain converged energies that correctly reflect the relative electrostatic stability among the different structures. The required compounds and their parameters are listed below.

| compound | structure_type | lattice_param_A (Å) | B-site valence(s) |
|----------|---------------|---------------------|-------------------|
| BaCeO3 | simple | 4.377 | B=+4 |
| BaPrO3 | simple | 4.360 | B=+4 |
| BaZrO3 | simple | 4.193 | B=+4 |
| BaTiO3 | simple | 4.031 | B=+4 |
| ABO3 | simple | 4.304 | B=+4 |
| ABO3 | simple | 4.162 | B=+4 |
| BaEr1/2Nb1/2O3 | mixed_ordered | 4.304 | B′=+3, B′′=+5 |
| BaEr1/2Nb1/2O3 | mixed_disordered | 4.304 | B′=+3, B′′=+5 |
| BaEr1/2Ta1/2O3 | mixed_ordered | 4.302 | B′=+3, B′′=+5 |
| BaEr1/2Ta1/2O3 | mixed_disordered | 4.302 | B′=+3, B′′=+5 |
| BaGd1/2Nb1/2O3 | mixed_ordered | 4.342 | B′=+3, B′′=+5 |
| BaGd1/2Nb1/2O3 | mixed_disordered | 4.342 | B′=+3, B′′=+5 |
| BaGd1/2Ta1/2O3 | mixed_ordered | 4.339 | B′=+3, B′′=+5 |
| BaGd1/2Ta1/2O3 | mixed_disordered | 4.339 | B′=+3, B′′=+5 |
| BaLa1/2Nb1/2O3 | mixed_ordered | 4.395 | B′=+3, B′′=+5 |
| BaLa1/2Nb1/2O3 | mixed_disordered | 4.395 | B′=+3, B′′=+5 |
| BaLa1/2Ta1/2O3 | mixed_ordered | 4.340 | B′=+3, B′′=+5 |
| BaLa1/2Ta1/2O3 | mixed_disordered | 4.340 | B′=+3, B′′=+5 |
| BaYb1/2Nb1/2O3 | mixed_ordered | 4.286 | B′=+3, B′′=+5 |
| BaYb1/2Nb1/2O3 | mixed_disordered | 4.286 | B′=+3, B′′=+5 |
| BaYb1/2Ta1/2O3 | mixed_ordered | 4.337 | B′=+3, B′′=+5 |
| BaYb1/2Ta1/2O3 | mixed_disordered | 4.337 | B′=+3, B′′=+5 |
| BaCa1/2Mo1/2O3 | mixed_ordered | 4.162 | B′=+2, B′′=+6 |
| BaCa1/2Mo1/2O3 | mixed_disordered | 4.162 | B′=+2, B′′=+6 |
| BaCa1/2Te1/2O3 | mixed_ordered | 4.186 | B′=+2, B′′=+6 |
| BaCa1/2Te1/2O3 | mixed_disordered | 4.186 | B′=+2, B′′=+6 |
| BaCa1/3Nb2/3O3 | mixed_disordered | 4.210 | Ca=+2 (1/3), Nb=+5 (2/3) |

## Assets

- NumPy: numpy

## Workflow steps

### Step 1: Madelung Energy Calculation
- Role: scored (load-bearing)
- Action: Implement a direct electrostatic (Coulomb) summation program to compute Madelung energies for a list of perovskite compounds. For each compound, use the provided equivalent cubic lattice parameter and ion valences. Build a perovskite supercell with periodic boundary conditions; for mixed perovskites, distribute B′ and B′′ ions according to ordered (alternating) and disordered (random) arrangements. Sum pairwise Coulomb interactions over a large enough supercell to achieve convergence to within ~0.1 eV. Report the total Madelung energy per formula unit (in eV) for each compound and configuration in a CSV file.
- Output file: `/app/outputs/madelung_energies.csv`
- Format: csv
- Contract: columns: compound (string), structure_type (string with values 'simple', 'mixed_ordered', 'mixed_disordered'), lattice_param_A (float, unit angstrom), Madelung_energy_eV (float, unit eV)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/madelung_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### madelung_energies.csv
- path: `/app/outputs/madelung_energies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Table of Madelung energies for each specified perovskite and B-site configuration. The energy values are compared against paper-reported reference values within a tolerance; qualitative trends (ordered vs. disordered, mixed vs. simple) are also verified.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `structure_type`, `lattice_param_A`, `Madelung_energy_eV`
  - `units`:
    - `lattice_param_A`: angstrom
    - `Madelung_energy_eV`: eV

Notes: The checker compares each energy value to the paper's reported Madelung energies with an appropriate tolerance and also verifies the required trends: mixed ordered energies lower than simple ABO3 at the same lattice parameter, and ordered energies lower than disordered for the same compound. The exact tolerance is hidden and is large enough to absorb legitimate numerical spread from different implementations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "madelung_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "structure_type",
          "lattice_param_A",
          "Madelung_energy_eV"
        ],
        "units": {
          "lattice_param_A": "angstrom",
          "Madelung_energy_eV": "eV"
        }
      },
      "description": "Table of Madelung energies for each specified perovskite and B-site configuration. The energy values are compared against paper-reported reference values within a tolerance; qualitative trends (ordered vs. disordered, mixed vs. simple) are also verified."
    }
  ],
  "notes": "The checker compares each energy value to the paper's reported Madelung energies with an appropriate tolerance and also verifies the required trends: mixed ordered energies lower than simple ABO3 at the same lattice parameter, and ordered energies lower than disordered for the same compound. The exact tolerance is hidden and is large enough to absorb legitimate numerical spread from different implementations."
}
```

## How you are scored
A hidden verifier will read your `madelung_energies.csv` and independently check each reported Madelung energy against reference values established from the underlying study. The verifier compares your computed energies to these references with an appropriate tolerance, and also verifies that your results satisfy the expected qualitative trends (e.g., ordered mixed perovskites should show lower energy than the corresponding simple perovskite at the same lattice parameter, and ordered energies should be lower than disordered energies for the same compound). The final reward (0–1) is a weighted combination of the fraction of correctly matched energy values and the correct fulfillment of the required trends. Your submission is scored solely on the contents of that CSV file; no other output is considered.

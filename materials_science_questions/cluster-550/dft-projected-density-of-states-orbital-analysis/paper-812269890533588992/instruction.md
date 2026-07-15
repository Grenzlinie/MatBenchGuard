# DFT Reproduction of Li-Al-Si Compound Stabilities and Electronic Properties

## Problem background
Lithium–aluminum–silicon compounds are investigated as potential high-capacity anode materials for lithium-ion batteries. Understanding the relative thermodynamic stability and electronic properties of these ternary phases is essential to explain which compositions are stable, why certain stoichiometries cannot be synthesized, and which phases exhibit the metallic conductivity that enables reversible lithium cycling. First-principles density-functional theory (DFT) calculations are used to evaluate formation energies and electronic structure features that govern the electrochemical behavior of selected Li–Al–Si compounds.

## Approach
A plane-wave DFT approach with the generalized-gradient approximation (GGA-PBE) is employed. Geometry optimizations are performed for the cubic LiAlSi (cF12) and the hypothetical Li2AlSi (cF16) in different crystallographic arrangements while preserving the relevant space-group symmetry. For disordered phases (Li7Al3Si4, Li5AlSi2, Li9AlSi3), ordered supercell models motivated by the reported crystal structures are constructed and used in single-point electronic-structure calculations. From the results, we extract optimized lattice constants, total energies, band gaps (or indicate absence), and identify metallic character from the density of states at the Fermi level. The workflow uses the open-source Quantum ESPRESSO code with standard GGA-PBE ultrasoft pseudopotentials.

## Reproduction target
Produce a CSV file, `computed_properties.csv`, that reports for each compound and arrangement the optimized lattice parameter (in Ångströms), the total energy per unit cell (in eV), the band gap (in eV, or `NA` if the system is metallic), and a boolean flag `is_metallic` indicating whether the Fermi level lies within a band. The compounds and arrangements are: LiAlSi (arrangements I, II, III as described by the four Wyckoff positions of the F-43m cell), Li2AlSi (non-centrosymmetric F-43m and centrosymmetric Fm-3m), and the ordered supercell models for Li7Al3Si4 (F-43m 2×2×2 supercell), Li5AlSi2 (monoclinic P21/m supercell), and Li9AlSi3 (orthorhombic C2221 supercell).

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- GGA-PBE ultrasoft pseudopotentials: https://materialscloud.org/sssp/

## Workflow steps

### Step 1: DFT validation on elemental Li, Al, Si
- Role: process
- Action: Use plane-wave DFT (Quantum ESPRESSO) with GGA-PBE pseudopotentials to optimize the crystal structures of elemental Li (bcc), Al (fcc), and Si (diamond). Confirm that the computed lattice parameters are within a few percent of experimental values (Li 3.5092 Å, Al 4.0495 Å, Si 5.4307 Å). This step calibrates the computational settings (cutoff, k-points) for the subsequent compound calculations.
- Evidence: `/app/outputs/elemental_validation.json`

### Step 2: Construct ordered supercell models for disordered compounds
- Role: process
- Action: Build periodic ordered supercell approximations for Li7Al3Si4 (cubic F-43m 2x2x2 supercell), Li5AlSi2 (monoclinic P2_1/m supercell derived from a 2x2x1 hexagonal supercell), and Li9AlSi3 (orthorhombic C222_1 supercell from a 2x2x1 tetragonal cell), following the structural descriptions in the paper. Output the coordinates in a format readable by the DFT code.
- Evidence: `/app/outputs/ordered_models.txt`

### Step 3: DFT calculations of Li-Al-Si compounds and property extraction
- Role: scored (load-bearing)
- Action: Perform DFT calculations using the validated settings: (1) Geometry optimizations for LiAlSi arrangements I, II, III (cF12, space group F-43m) and for Li2AlSi arrangements F-43m and Fm-3m (cF16), with atoms constrained on the special positions; (2) Single-point electronic structure calculations (band structure, DOS) for the ordered models of Li7Al3Si4, Li5AlSi2, and Li9AlSi3. For each system, extract the optimized lattice parameter (use experimental lattice parameter for the non-optimized models), total energy per unit cell, band gap (NA if metallic), and a boolean flag indicating metallic character (from DOS at Fermi level). Write all results to computed_properties.csv.
- Output file: `/app/outputs/computed_properties.csv`
- Format: csv
- Contract: compound (str), arrangement (str), space_group (str), optimized_a (float, Angstrom), total_energy_ev (float), band_gap_ev (float or 'NA'), is_metallic (bool)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_properties.csv
- path: `/app/outputs/computed_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Reproduction of DFT-computed properties for Li-Al-Si compounds. The checker compares values against hidden paper-reported references with tolerances.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `arrangement`, `space_group`, `optimized_a`, `total_energy_ev`, `band_gap_ev`, `is_metallic`
  - `units`:
    - `optimized_a`: Angstrom
    - `total_energy_ev`: eV
    - `band_gap_ev`: eV

Notes: The checker uses reference_match policy: compares extracted values (lattice parameters within tolerance, relative energy ordering, metallicity flags) to the paper's reported values. The agent must produce the table; no hidden holdout is required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "arrangement",
          "space_group",
          "optimized_a",
          "total_energy_ev",
          "band_gap_ev",
          "is_metallic"
        ],
        "units": {
          "optimized_a": "Angstrom",
          "total_energy_ev": "eV",
          "band_gap_ev": "eV"
        }
      },
      "description": "Reproduction of DFT-computed properties for Li-Al-Si compounds. The checker compares values against hidden paper-reported references with tolerances."
    }
  ],
  "notes": "The checker uses reference_match policy: compares extracted values (lattice parameters within tolerance, relative energy ordering, metallicity flags) to the paper's reported values. The agent must produce the table; no hidden holdout is required."
}
```

## How you are scored
A hidden verifier will parse your `computed_properties.csv` and independently evaluate the reported lattice parameters, total energies, band gaps, and metallicity flags against reference data derived from the published study. Scoring accounts for the accuracy of lattice constants, the preservation of relative energetic ordering among arrangements, the near-equality of energies for the two Li2AlSi configurations, and the correctness of the metallic/non-metallic classification. The final reward is a weighted sum of the performance on these criteria; simply quoting numbers without running a faithful DFT simulation will not suffice to achieve a high score.

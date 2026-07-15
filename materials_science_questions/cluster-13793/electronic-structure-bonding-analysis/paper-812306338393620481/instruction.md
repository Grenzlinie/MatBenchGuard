# Electronic Structure Bonding Analysis of Li₂Ga

## Problem background
Li₂Ga is a crystalline solid containing uniform zigzag chains of gallium atoms. A simple electron-counting argument suggests a half‑filled π‑band, which might lead to a Peierls distortion (dimerization) analogous to trans-polyacetylene. However, the experimental crystal structure shows no such dimerization. The electronic structure of Li₂Ga is investigated with density functional theory to understand the nature of Ga–Li and Li–Li interactions, charge transfer, and the reason for the uniform chains. Quantities such as Mulliken atomic charges, bond overlap populations for key contacts, and the lithium contribution to the density of states at the Fermi level are computed to elucidate the bonding character.

## Approach
The calculations are performed using the SIESTA DFT code with the Perdew–Burke–Ernzerhof (PBE) generalized‑gradient functional, a double‑ζ polarized (DZP) basis set of numerical atomic orbitals, and norm‑conserving Troullier–Martins pseudopotentials. The workflow starts from the experimental orthorhombic crystal structure (space group Cmcm) and carries out a full geometry optimization to find the equilibrium geometry. A self‑consistent field (SCF) calculation is then performed on the optimized structure using a dense Monkhorst–Pack k‑point mesh to obtain the converged density matrix. From the SCF output, Mulliken atomic charges, bond overlap populations, and the atom‑projected density of states are extracted. The fractional contribution of lithium orbitals to the total DOS at the Fermi level is computed from the projected DOS.

## Reproduction target
Compute and write to a JSON file the following electronic properties of Li₂Ga: (i) Mulliken atomic charges for the Ga, Li(1), and Li(2) atoms; (ii) Mulliken bond overlap populations for the Ga–Ga bond, each Ga–Li contact within a 3.25 Å cutoff (including specific contacts at 2.70, 2.86, 3.05 Å for Ga–Li(1) and 2.77, 3.16, 3.20 Å for Ga–Li(2)), and the listed Li–Li contacts (intralayer 2.75, 2.71 Å; interlayer 2.72, 3.16 Å); (iii) the fractional contribution (in percent) of lithium orbitals to the total density of states at the Fermi level. All results must be placed in a file named `li2ga_electronic_properties.json` with the exact schema specified in the output contract.

## Assets

- SIESTA DFT code: https://gitlab.com/siesta-project/siesta
- PBE Troullier–Martins pseudopotentials for Ga and Li: https://departments.icmab.es/leem/siesta/Databases/Pseudopotentials/pp_ALL_ABINIT.html
- Li₂Ga experimental crystal structure

## Workflow steps

### Step 1: Li₂Ga geometry optimization
- Role: process
- Action: Perform a DFT geometry optimization of Li₂Ga using SIESTA with the PBE functional, a double‑ζ polarized (DZP) basis set, norm‑conserving pseudopotentials, and a k‑point mesh of at least 10×10×10, starting from the experimental orthorhombic unit cell. The optimized structure should be written to an evidence file for later inspection.
- Evidence: `/app/outputs/optimized_geometry.cif`

### Step 2: Li₂Ga self‑consistent field (SCF) calculation
- Role: process
- Action: Using the optimized structure from step1, perform a self‑consistent DFT calculation with the same functional, basis set, pseudopotentials, and a 10×10×10 k‑point mesh to obtain the converged density matrix, eigenvalues, and orbital projections. Save the standard SIESTA output log as evidence.
- Evidence: `/app/outputs/scf_output.log`

### Step 3: Li₂Ga electronic properties extraction
- Role: scored (load-bearing)
- Action: From the converged SCF results compute: (a) Mulliken atomic charges for Ga, Li(1), and Li(2); (b) Mulliken bond overlap populations for the Ga–Ga bond, the listed Ga–Li contacts (2.70, 2.86, 3.05 Å for Ga–Li(1); 2.77, 3.16, 3.20 Å for Ga–Li(2)), and the listed Li–Li contacts (intralayer 2.75, 2.71 Å; interlayer 2.72, 3.16 Å); (c) the fractional contribution of lithium orbitals to the total density of states at the Fermi level. Write all results to the JSON file `li2ga_electronic_properties.json` with the exact schema described in the output contract.
- Output file: `/app/outputs/li2ga_electronic_properties.json`
- Format: json
- Contract: {"Mulliken_charges": {"Ga": <float>, "Li1": <float>, "Li2": <float>}, "Overlap_populations": {"Ga_Ga": <float>, "Ga_Li1_2.70A": <float>, "Ga_Li1_2.86A": <float>, "Ga_Li1_3.05A": <float>, "Ga_Li2_2.77A": <float>, "Ga_Li2_3.16A": <float>, "Ga_Li2_3.20A": <float>, "Li_Li_intra_2.75A": <float>, "Li_Li_intra_2.71A": <float>, "Li_Li_inter_2.72A": <float>, "Li_Li_inter_3.16A": <float>}, "Li_DOS_percent_at_Fermi": <float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/li2ga_electronic_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### li2ga_electronic_properties.json
- path: `/app/outputs/li2ga_electronic_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Scored artifact containing the reproduced Mulliken atomic charges, bond overlap populations, and lithium contribution to the DOS at the Fermi level for Li₂Ga. The checker compares each numeric field against paper‑reported values using an appropriate absolute tolerance.
- schema:
  - `type`: object
  - `required`:
    - `Mulliken_charges`:
      - `Ga`: float
      - `Li1`: float
      - `Li2`: float
    - `Overlap_populations`:
      - `Ga_Ga`: float
      - `Ga_Li1_2.70A`: float
      - `Ga_Li1_2.86A`: float
      - `Ga_Li1_3.05A`: float
      - `Ga_Li2_2.77A`: float
      - `Ga_Li2_3.16A`: float
      - `Ga_Li2_3.20A`: float
      - `Li_Li_intra_2.75A`: float
      - `Li_Li_intra_2.71A`: float
      - `Li_Li_inter_2.72A`: float
      - `Li_Li_inter_3.16A`: float
    - `Li_DOS_percent_at_Fermi`: float

Notes: All numerical values are physical observables reproduced by a deterministic DFT protocol; the checker uses an exact‑match policy with hidden tolerances derived from the expected run‑to‑run variability in SIESTA calculations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "li2ga_electronic_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "Mulliken_charges": {
            "Ga": "float",
            "Li1": "float",
            "Li2": "float"
          },
          "Overlap_populations": {
            "Ga_Ga": "float",
            "Ga_Li1_2.70A": "float",
            "Ga_Li1_2.86A": "float",
            "Ga_Li1_3.05A": "float",
            "Ga_Li2_2.77A": "float",
            "Ga_Li2_3.16A": "float",
            "Ga_Li2_3.20A": "float",
            "Li_Li_intra_2.75A": "float",
            "Li_Li_intra_2.71A": "float",
            "Li_Li_inter_2.72A": "float",
            "Li_Li_inter_3.16A": "float"
          },
          "Li_DOS_percent_at_Fermi": "float"
        }
      },
      "description": "Scored artifact containing the reproduced Mulliken atomic charges, bond overlap populations, and lithium contribution to the DOS at the Fermi level for Li₂Ga. The checker compares each numeric field against paper‑reported values using an appropriate absolute tolerance."
    }
  ],
  "notes": "All numerical values are physical observables reproduced by a deterministic DFT protocol; the checker uses an exact‑match policy with hidden tolerances derived from the expected run‑to‑run variability in SIESTA calculations."
}
```

## How you are scored
Your submitted `li2ga_electronic_properties.json` file will be examined by a hidden verifier. The verifier compares each numeric field (Mulliken charges, all overlap populations, and the Li DOS percentage) against reference values, applying appropriate numerical tolerances to account for minor computational variations. The overall score is a weighted combination of how closely your computed numbers match the expected physical values. To obtain a high score, you must genuinely perform the DFT calculations and extract the properties; arbitrary or guessed numbers are unlikely to fall within the required tolerances. The verifier does not require you to reproduce any specific table from a publication — only that your own computed results are physically accurate and consistent with the computational protocol described.

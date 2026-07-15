# All-electron UHF Mulliken populations of Fe–M dimers (M=Mn,Fe,Co,Ni,Cu) at fixed bond length

## Problem background
The Mössbauer isomer shift of Fe in Fe–M dimers (M = Mn, Fe, Co, Ni, Cu) provides insight into metal-metal bonding in diatomic transition-metal systems. The isomer shift depends on the s-electron density at the Fe nucleus, which in turn is influenced by s–s bonding (Fe s × M s overlap) and d-d shielding (Fe d × Fe d overlap). Understanding these effects requires accurate electronic structure calculations. This task computes the Mulliken atomic overlap populations for the five dimers to elucidate the contributions of s-bonding, d-shielding, and d-bonding to the observed isomer shift trends.

## Approach
The electronic structures are computed using all-electron unrestricted Hartree–Fock (UHF). The basis set is the Primitive Gaussian set (12s,6p,4d) of Tatewaki and Huzinaga, contracted to [4s,2p,1d] on each atom. The internuclear distance is fixed at 2.3 Å for all dimers. Spin multiplicities are taken from experimental assignments: FeMn (quartet, 4), Fe₂ (septet, 7), FeCo (sextet, 6), FeNi (triplet, 3), FeCu (doublet, 2). From the converged UHF density matrix, Mulliken population analysis is performed to extract three overlap populations:
- s-bonding: sum of Fe s × M s overlaps.
- d-shielding: sum of Fe d × Fe d overlaps on the same Fe atom.
- d-bonding: sum of Fe d × M d overlaps.
These quantities are reported in a CSV and examined to infer how s and d electrons govern bonding and the isomer shift.

## Reproduction target
Produce a CSV file (`mulliken_populations.csv`) containing the Mulliken overlap populations (s-bonding, d-shielding, d-bonding) for each of the five dimers. The values must be obtained from the UHF calculations described above. In addition to the numeric populations, the hidden verifier will check that the relative ordering of the s-bonding values among the dimers is physically consistent and matches the expected binding-strength trend derived from the isomer shift.

## Assets

- Tatewaki–Huzinaga (12s,6p,4d)/[4s,2p,1d] basis sets for Fe, Mn, Co, Ni, Cu: https://www.basissetexchange.org
- Open-source quantum chemistry library (e.g., PySCF): https://pyscf.org

## Workflow steps

### Step 1: Contract Tatewaki–Huzinaga primitive basis to [4s,2p,1d] per atom
- Role: process
- Action: Obtain the (12s,6p,4d) primitive Gaussian basis sets for Fe, Mn, Co, Ni, Cu from the Tatewaki–Huzinaga reference. Contract each set to the [4s,2p,1d] contracted basis using the contraction coefficients given in the paper (or via Basis Set Exchange). Save the contracted basis definitions for use in subsequent SCF calculations.
- Evidence: `/app/outputs/contracted_basis.log`

### Step 2: Run unrestricted Hartree–Fock SCF calculations for the five Fe–M dimers
- Role: process
- Action: For each dimer (Fe₂, FeMn, FeCo, FeNi, FeCu): set up an all-electron unrestricted Hartree–Fock calculation using the contracted basis, a fixed internuclear distance of 2.3 Å, and spin multiplicities from experimental assignments (FeMn:4, Fe₂:7, FeCo:6, FeNi:3, FeCu:2). Converge the SCF and save the converged wavefunction (molecular orbital coefficients) or one-electron density matrix for later population analysis. No full CI correlation is used.
- Evidence: `/app/outputs/uhf_scf_log.txt`

### Step 3: Compute Mulliken atomic overlap populations and output CSV
- Role: scored (load-bearing)
- Action: From the converged UHF wavefunctions or density matrices, compute the Mulliken overlap populations as defined in the paper: s-bonding (overlap of Fe s atomic orbitals with M s orbitals), d-shielding (overlap of Fe d orbitals with themselves on the same Fe atom), and d-bonding (overlap of Fe d orbitals with M d orbitals). Write a CSV file with one row per dimer and columns dimer, s_bonding, d_shielding, d_bonding.
- Output file: `/app/outputs/mulliken_populations.csv`
- Format: csv
- Contract: Columns: dimer (string), s_bonding (float), d_shielding (float), d_bonding (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/mulliken_populations.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### mulliken_populations.csv
- path: `/app/outputs/mulliken_populations.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Mulliken overlap populations (s-bonding, d-shielding, d-bonding) for the five Fe–M dimers. The hidden checker compares these values to the paper's Table 4 with appropriate tolerance and also verifies the relative ordering of s-bonding values.
- schema:
  - `type`: table
  - `required_columns`: `dimer`, `s_bonding`, `d_shielding`, `d_bonding`
  - `units`:
    - `s_bonding`: dimensionless (Mulliken overlap population)
    - `d_shielding`: dimensionless (Mulliken overlap population)
    - `d_bonding`: dimensionless (Mulliken overlap population)

Notes: The population values are dimensionless Mulliken overlap populations. The checker verifies each dimer's values against the hidden reference and additionally checks that the s-bonding ordering follows FeCu > FeMn > Fe₂ > FeCo > FeNi within a small tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "mulliken_populations.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "dimer",
          "s_bonding",
          "d_shielding",
          "d_bonding"
        ],
        "units": {
          "s_bonding": "dimensionless (Mulliken overlap population)",
          "d_shielding": "dimensionless (Mulliken overlap population)",
          "d_bonding": "dimensionless (Mulliken overlap population)"
        }
      },
      "description": "Mulliken overlap populations (s-bonding, d-shielding, d-bonding) for the five Fe–M dimers. The hidden checker compares these values to the paper's Table 4 with appropriate tolerance and also verifies the relative ordering of s-bonding values."
    }
  ],
  "notes": "The population values are dimensionless Mulliken overlap populations. The checker verifies each dimer's values against the hidden reference and additionally checks that the s-bonding ordering follows FeCu > FeMn > Fe₂ > FeCo > FeNi within a small tolerance."
}
```

## How you are scored
Your solution is evaluated by a hidden checker that runs after submission. Each scored step (the Mulliken populations CSV) contributes a weighted share to the final reward. The checker compares your reported values to a concealed reference with appropriate tolerances and also verifies that the s-bonding values follow the correct relative ordering. The final score is the weighted sum of these checks. Simply reporting the paper's original numbers without executing the required calculations will not satisfy the verifier.

# Exchange Couplings in Co/Mn-doped ZnO: LSDA vs. LSDA+U

## Problem background
ZnO doped with magnetic transition-metal ions (Co, Mn) is a leading candidate for dilute magnetic semiconductors. An accurate theoretical description of magnetic exchange couplings between substitutional impurity pairs is essential to understand magnetism in these materials. Density functional theory within the local spin density approximation (LSDA) has been widely used to compute exchange constants, but its predictions for nearest-neighbor Co and Mn pairs in ZnO have shown qualitative discrepancies with experiments. The strong electron correlation on the transition-metal 3d orbitals is suspected to be the source of the failure. The LSDA+U method, which adds an on-site Hubbard U correction, is proposed to improve the description of these localized states. The present task computes the nearest-neighbor exchange integrals under both LSDA and LSDA+U and allows a quantitative comparison between the two approaches.

## Approach
The exchange couplings are extracted from total-energy differences of supercells containing substitutional magnetic impurities. Two distinct nearest-neighbor geometries are probed: in-plane pairs (supercell A) and out-of-plane pairs (supercell B). For each supercell, both ferromagnetic (FM) and antiferromagnetic (AFM) alignments of the impurity spins are computed. Total energies are obtained from spin-polarized plane-wave DFT calculations using the LSDA functional (U=0) and again with the LSDA+U method in the atomic limit, where the on-site Coulomb parameter U and the Hund's rule exchange parameters F², F⁴ are applied to the impurity 3d orbitals. From the resulting energy differences per magnetic ion, the Heisenberg exchange integral J is derived. The comparison between LSDA and LSDA+U highlights the impact of correlation corrections on the sign and magnitude of the couplings.

## Reproduction target
Using Quantum ESPRESSO and the wurtzite ZnO crystal structure, construct supercells A and B with substitutional Co and Mn pairs. Perform total-energy calculations for each impurity and supercell under LSDA and LSDA+U (U=6 eV, with appropriate Hund's J parameters). From the FM and AFM energies, compute the per-bond exchange constants J_in (from supercell A) and J_out (from supercell B). Report the results in `/app/outputs/exchange_couplings.csv` with columns: impurity, coupling_type, supercell, U_value_eV, delta_E_per_bond_meV, and J_meV.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- ZnO wurtzite crystal structure: https://www.crystallography.net/cod/9011662.cif
- Pseudopotentials for QE: https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: Supercell construction
- Role: process
- Action: Using the wurtzite ZnO primitive cell, build supercells A (in-plane) and B (out-of-plane) containing substitutional Co or Mn impurity pairs. Set up both ferromagnetic (all impurity spins parallel) and antiferromagnetic (two impurity spins antiparallel) spin configurations for each impurity, yielding 8 initial structures.
- Evidence: `/app/outputs/supercell_structures.json`

### Step 2: LSDA (U=0) total-energy calculations
- Role: process
- Action: Perform collinear spin-polarized DFT calculations using the LSDA functional (U=0) for all eight configurations (Co A/B FM/AFM and Mn A/B FM/AFM). Extract the total energy per magnetic ion for each case.
- Evidence: `/app/outputs/lsda_energies.json`

### Step 3: LSDA+U (U=6 eV) total-energy calculations
- Role: process
- Action: Repeat the DFT calculations for the same eight configurations using LSDA+U in the atomic limit, with on-site Coulomb parameter U = F⁰ = 6 eV and Hund's rule exchange parameters F²=7.9, F⁴=5.0 eV for Co and F²=7.4, F⁴=4.6 eV for Mn. Extract the total energy per magnetic ion for each configuration.
- Evidence: `/app/outputs/lsda_u_energies.json`

### Step 4: Extract nearest-neighbor exchange integrals
- Role: scored (load-bearing)
- Action: For each impurity (Co, Mn) and supercell (A, B) at U=0 and U=6, compute the energy difference ΔE = (E_FM − E_AFM)/2 per magnetic ion. As supercells A and B are chains where each ion has two nearest neighbors, convert to per-bond energy ΔE_bond = ΔE/2. Then compute the exchange integral J (meV) via J = -2·ΔE_bond / [S_T(S_T+1)], with S_T=3 for Co²⁺ (S=3/2) and S_T=5 for Mn²⁺ (S=5/2). Write the results to a CSV file.
- Output file: `/app/outputs/exchange_couplings.csv`
- Format: csv
- Contract: CSV with columns: impurity (Co/Mn), coupling_type (in-plane/out-of-plane), supercell (A/B), U_value_eV (0/6), delta_E_per_bond_meV (float), J_meV (float). Exactly 8 rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/exchange_couplings.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### exchange_couplings.csv
- path: `/app/outputs/exchange_couplings.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Extracted Heisenberg exchange constants J_in and J_out for ZnO:Co and ZnO:Mn under LSDA (U=0) and LSDA+U (U=6 eV) using supercells A and B. Compared to paper-reported values with tolerance and sign correctness.
- schema:
  - `type`: table
  - `required_columns`: `impurity`, `coupling_type`, `supercell`, `U_value_eV`, `delta_E_per_bond_meV`, `J_meV`
  - `units`:
    - `J_meV`: meV

Notes: The hidden checker verifies J_meV values against the paper's reported exchange integrals for supercells A and B at U=0 and U=6, allowing a magnitude tolerance of ±1.0 meV. It also checks that all J_meV are negative (antiferromagnetic) except for Co out-of-plane at U=0, which must be positive.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "exchange_couplings.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "impurity",
          "coupling_type",
          "supercell",
          "U_value_eV",
          "delta_E_per_bond_meV",
          "J_meV"
        ],
        "units": {
          "J_meV": "meV"
        }
      },
      "description": "Extracted Heisenberg exchange constants J_in and J_out for ZnO:Co and ZnO:Mn under LSDA (U=0) and LSDA+U (U=6 eV) using supercells A and B. Compared to paper-reported values with tolerance and sign correctness."
    }
  ],
  "notes": "The hidden checker verifies J_meV values against the paper's reported exchange integrals for supercells A and B at U=0 and U=6, allowing a magnitude tolerance of ±1.0 meV. It also checks that all J_meV are negative (antiferromagnetic) except for Co out-of-plane at U=0, which must be positive."
}
```

## How you are scored
A hidden verifier reads your `exchange_couplings.csv` and independently evaluates each row's exchange constant `J_meV`. The verifier checks that the sign and magnitude of each constant match the expected physical result (derived from the original paper's reported values under the same conditions). Reward is proportional to the fraction of entries with correct sign and magnitude within an allowed tolerance that accounts for differences between DFT implementations. Merely reporting a plausible number is not sufficient; the computed values must follow from the prescribed protocol and the supplied resources.

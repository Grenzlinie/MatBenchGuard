# Compute Gibbs free energy barriers and rate constants for HMDSO initial decomposition pathways using DFT and TST

## Problem background
Accurate kinetic data for hexamethyldisiloxane (HMDSO) thermal decomposition is critical for flame-based silica material synthesis. This task computes the Gibbs free energy of activation and forward rate constants for the four initial decomposition pathways of HMDSO using density functional theory and transition state theory, providing quantitative insight into which pathway is most kinetically favorable.

## Approach
Use quantum chemistry calculations at the B3LYP/6-311+G(d,p) level of density functional theory (DFT). For each of the four initial decomposition pathways—Si–O bond dissociation (P1), Si–C bond dissociation (P2), dissociation-recombination of Si–O and Si–C bonds (P3), and CH₄ elimination (P4)—locate and verify transition states, compute thermochemistry (including zero-point energy correction), and calculate activation Gibbs free energies. Apply conventional transition state theory with Wigner tunneling correction to obtain rate constants at multiple temperatures.

## Reaction pathways
The four target initial decomposition reactions, as defined in the paper, are:

- **P1 (Si–O bond dissociation):**  
  (CH₃)₃SiOSi(CH₃)₃ → (CH₃)₃SiO• + •Si(CH₃)₃  
  (trimethylsilyloxyl radical + trimethylsilyl radical)

- **P2 (Si–C bond dissociation):**  
  (CH₃)₃SiOSi(CH₃)₃ → •CH₃ + (CH₃)₃SiOSi(CH₃)₂•  
  (methyl radical + pentamethyldisiloxane radical)

- **P3 (dissociation-recombination of Si–O and Si–C bonds):**  
  (CH₃)₃SiOSi(CH₃)₃ → (CH₃)₂SiO + Si(CH₃)₄  
  (dimethylsiloxane + tetramethylsilane)

- **P4 (CH₄ elimination):**  
  (CH₃)₃SiOSi(CH₃)₃ → CH₄ + (CH₃)₃SiOSiCH₃CH₂  
  (methane + a closed-shell silene molecule)

You must compute the activation barrier and rate constant for each of these four elementary reactions.

## Reproduction target
Compute the Gibbs free energy of activation ΔG_f‡ (in kcal/mol) at 298.15 K and the forward rate constants k(T) at 298.15, 1000, 1500, 2000, and 2500 K for the four initial decomposition pathways P1–P4 of HMDSO. Write the results to a CSV file with columns: pathway, temperature_K, delta_G_forward_kcalmol (provided only for T = 298.15 K), rate_constant_s-1. The file must contain exactly 20 rows (4 pathways × 5 temperatures).

## Assets

- Psi4 quantum chemistry package: https://psicode.org/

## Workflow steps

### Step 1: DFT geometry optimization and transition state search
- Role: process
- Action: Perform DFT geometry optimizations and frequency analyses for HMDSO, all product species of P1–P4 as listed in the Reaction pathways section, and locate transition states for the four initial decomposition pathways using relaxed scans and saddle point searches at the B3LYP/6-311+G(d,p) level. Verify each transition state by a single imaginary frequency and intrinsic reaction coordinate (IRC) calculations. Obtain absolute enthalpies and Gibbs free energies (including zero-point energy corrections) for all species.
- Evidence: none

### Step 2: Compute activation barriers and rate constants
- Role: scored (load-bearing)
- Action: From the computed thermochemistry data, calculate the Gibbs free energy of activation ΔG_f‡ (in kcal/mol) for each pathway at 298.15 K as (G_TS – G_reactant). Compute forward rate constants k(T) at 298.15, 1000, 1500, 2000, and 2500 K using conventional TST: k(T) = κ σ (k_B T / h) exp(–ΔG_f‡/(RT)), where κ is the Wigner tunneling correction from the imaginary frequency, σ is the reaction path symmetry number. Write results to initial_decomposition_results.csv.
- Output file: `/app/outputs/initial_decomposition_results.csv`
- Format: csv
- Contract: Columns: pathway (string), temperature_K (float), delta_G_forward_kcalmol (float, present only for T=298.15), rate_constant_s-1 (float). 20 rows: 4 pathways × 5 temperatures.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/initial_decomposition_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### initial_decomposition_results.csv
- path: `/app/outputs/initial_decomposition_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Barriers and rate constants for the initial decomposition pathways P1-P4 of HMDSO. Rows: 4 pathways × 5 temperatures. delta_G_forward_kcalmol is provided only for T=298.15 K; other rows leave that column empty.
- schema:
  - `type`: table
  - `required_columns`: `pathway`, `temperature_K`, `delta_G_forward_kcalmol`, `rate_constant_s-1`
  - `units`:
    - `delta_G_forward_kcalmol`: kcal/mol
    - `rate_constant_s-1`: s^{-1}

Notes: The agent may use any open-source quantum chemistry package (Psi4, Orca, NWChem) capable of B3LYP/6-311+G(d,p) DFT. The initial HMDSO geometry should be constructed as described in the method (Si-O 1.43 Å, Si-C 1.51 Å, Si-O-Si angle 150°). The CCSD benchmark step is not required for the scored target.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "initial_decomposition_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "pathway",
          "temperature_K",
          "delta_G_forward_kcalmol",
          "rate_constant_s-1"
        ],
        "units": {
          "delta_G_forward_kcalmol": "kcal/mol",
          "rate_constant_s-1": "s^{-1}"
        }
      },
      "description": "Barriers and rate constants for the initial decomposition pathways P1-P4 of HMDSO. Rows: 4 pathways × 5 temperatures. delta_G_forward_kcalmol is provided only for T=298.15 K; other rows leave that column empty."
    }
  ],
  "notes": "The agent may use any open-source quantum chemistry package (Psi4, Orca, NWChem) capable of B3LYP/6-311+G(d,p) DFT. The initial HMDSO geometry should be constructed as described in the method (Si-O 1.43 Å, Si-C 1.51 Å, Si-O-Si angle 150°). The CCSD benchmark step is not required for the scored target."
}
```

## How you are scored
Your submitted CSV will be evaluated by a hidden verifier. It checks that the computed barriers and rate constants agree with reference values derived from the original study within tolerances appropriate for DFT calculations, and that the relative ordering of pathways (barrier magnitudes and rate constants at each temperature) matches the expected chemical trend. The final reward is a weighted combination of the agreement on the barrier values, the rate constants across all temperatures, and the pathway ordering.
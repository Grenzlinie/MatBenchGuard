# Cr-based donor bound magnetic polaron model and s-d exchange parameter determination

## Problem background
Diluted magnetic semiconductors containing Cr²⁺ ions exhibit a bound magnetic polaron (BMP) effect where the exchange interaction between a donor electron and the magnetic ions within its orbit modifies the energy spectrum. The Cr²⁺ ion has a semidoublet ground state (permanent moment like Mn²⁺) followed by closely lying excited states (like Fe²⁺), leading to both a zero‑field spin‑flip energy and anticrossings of BMP levels in an applied magnetic field. Spin‑flip Raman scattering (SFRS) experiments on Cd₁₋ₓCrₓS have revealed characteristic anticrossings of the Raman lines, and a proper BMP model is needed to understand the data and to extract the conduction‑band s–d exchange parameter N₀α, which is otherwise difficult to determine in Cr‑based materials.

## Approach
We build a multi‑ion donor BMP model for Cr‑based DMS in the weak‑coupling limit. First, the single‑ion Cr²⁺ states in the CdS crystal field (including cubic and hexagonal crystal fields, static Jahn–Teller tetragonal distortion, and spin–orbit coupling) are computed to obtain the five lowest eigenenergies and the required spin matrix elements (⟨S_z⟩, ⟨S_+⟩). Using these single‑ion data for a given Cr molar fraction x, temperature T, and muffin‑tin donor radius r₀, we determine the thermodynamic average occupation numbers P (ground state) and N−P (first excited state) of the N magnetic ions inside the donor orbit via a semiclassical partition function in a two‑level approximation. The BMP Hamiltonian matrix is then constructed in the truncated subspace Ψ_{1σ}^P ⊕ Ψ_{jσ}^{1P} (one‑ion excitations from the ground state) using the occupation numbers, single‑ion matrix elements, and the s−d exchange parameter N₀α. Diagonalizing this 10×10 Hamiltonian for magnetic fields B from 0 to 10 T yields the BMP eigenstates relative to the ground level, from which we identify the first (L1) and second (L2) excited states. Finally, the exchange parameter N₀α is fitted by comparing the computed L1 and L2 energy curves to the published experimental SFRS peak positions for Cd₁₋ₓCrₓS (x≈0.00235, T≈2 K), varying N₀α on a grid around +0.2 eV to minimize the RMS deviation between the model and the data.

## Reproduction target
The concrete reproduction target has two parts, corresponding to the two scored artifacts:

1.  Compute the BMP energy levels L1 and L2 (energies of the first and second excited states relative to the ground state) as a function of magnetic field B for Cd₁₋ₓCrₓS with Cr molar fraction x=0.00235, T=2 K, muffin‑tin radius r₀=45 Å (N=20 ions), and N₀α=0.22 eV. Provide the results at 0.5 T intervals from 0 to 10 T in a CSV file with columns B_T (Tesla), E_L1_meV, E_L2_meV (meV).

2.  Determine the s–d exchange parameter N₀α that best matches the experimental SFRS peak positions reported for Cd₁₋ₓCrₓS with x≈0.00235 by Twardowski et al. (1996). Compute the BMP energy levels for a grid of N₀α values around +0.2 eV, compare the resulting L1 and L2 energy curves to the experimental points, and select the N₀α that minimises the RMS deviation. Report the fitted value as a single number (in eV) in a text file.

## Assets

- Cr2+ crystal-field parameters (Vallin et al. 1970): https://doi.org/10.1103/PhysRevB.2.4313
- Cr2+ Jahn-Teller parameters (Vallin and Watkins 1974): https://doi.org/10.1103/PhysRevB.9.2051
- Cd1-xCrxS SFRS experimental data (Twardowski et al. 1996): https://doi.org/10.1103/PhysRevB.53.10728

## Workflow steps

### Step 1: Compute Cr2+ single-ion states and matrix elements
- Role: process
- Action: Using the crystal-field model from Vallin et al. (including cubic and hexagonal fields, Jahn-Teller tetragonal distortion, and spin-orbit coupling), compute the five lowest Cr2+ eigenstates, their eigenenergies, and the required spin matrix elements ⟨j|Sz|k⟩ and ⟨j|S+|k⟩ for CdS.
- Evidence: `/app/outputs/single_ion_data.json`

### Step 2: Compute occupation numbers P and N-P
- Role: process
- Action: For Cr molar fraction x=0.00235, T=2 K, muffin-tin radius r0=45 Å, N=20 ions, and magnetic fields B from 0 to 10 T, compute the thermodynamic average ground-state occupation number P using the semiclassical partition function (binomial distribution, two-level approximation). Use the single-ion energies and spins from the previous step.
- Evidence: `/app/outputs/occupation_numbers.csv`

### Step 3: Compute BMP energy levels L1 and L2 vs B
- Role: scored (load-bearing)
- Action: Construct the 10×10 BMP Hamiltonian matrix in the Ψ1σ^P ⊕ Ψjσ^{1P} subspace for each B using occupation numbers, single-ion data, and a trial N0α=0.22 eV. Diagonalize to obtain BMP eigenenergies. Compute the energies of the first excited state (L1) and the second excited state (L2) relative to the ground state. Write the energies at 0.5 T intervals from 0 to 10 T.
- Output file: `/app/outputs/step_01_energies_vs_B.csv`
- Format: csv
- Contract: Columns: B_T (float, Tesla), E_L1_meV (float, meV), E_L2_meV (float, meV). Energy zero = ground state at same B.
- Scoring: scored by hidden verifier

### Step 4: Fit s-d exchange parameter N0α
- Role: scored
- Action: Determine the s-d exchange parameter N0α that best matches the published experimental SFRS peak positions from Twardowski et al. (1996) for Cd1-xCrxS with x≈0.00235. Compute BMP energy levels as in the previous step for a grid of N0α values around +0.2 eV, compare the resulting L1 and L2 energy curves to the experimental points, and select the N0α that minimizes the RMS deviation. Output the fitted value in eV.
- Output file: `/app/outputs/step_02_fitted_N0alpha.txt`
- Format: txt
- Contract: Single line containing the float value of N0α in eV.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_energies_vs_B.csv`
- `/app/outputs/step_02_fitted_N0alpha.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_energies_vs_B.csv
- path: `/app/outputs/step_01_energies_vs_B.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: L1 and L2 BMP energy levels vs B. The checker compares these curves to hidden theoretical reference curves derived from the paper's Fig. 10, using tolerances on zero-field splitting, anticrossing field positions, and overall RMS deviation.
- schema:
  - `type`: table
  - `required_columns`: `B_T`, `E_L1_meV`, `E_L2_meV`
  - `units`:
    - `B_T`: T
    - `E_L1_meV`: meV
    - `E_L2_meV`: meV

### step_02_fitted_N0alpha.txt
- path: `/app/outputs/step_02_fitted_N0alpha.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Best-fit s-d exchange parameter N0α. Checker verifies that the reported value is within ±0.02 eV of the paper's reported value (+0.22 eV).
- schema:
  - `type`: text
  - `description`: Single line containing a floating-point number in eV.

Notes: The agent is expected to fetch the crystal-field parameters from the referenced public papers and extract the experimental SFRS data from the Twardowski et al. publication. No hidden assets are required beyond those public resources.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_energies_vs_B.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "B_T",
          "E_L1_meV",
          "E_L2_meV"
        ],
        "units": {
          "B_T": "T",
          "E_L1_meV": "meV",
          "E_L2_meV": "meV"
        }
      },
      "description": "L1 and L2 BMP energy levels vs B. The checker compares these curves to hidden theoretical reference curves derived from the paper's Fig. 10, using tolerances on zero-field splitting, anticrossing field positions, and overall RMS deviation."
    },
    {
      "file": "step_02_fitted_N0alpha.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "Single line containing a floating-point number in eV."
      },
      "description": "Best-fit s-d exchange parameter N0α. Checker verifies that the reported value is within ±0.02 eV of the paper's reported value (+0.22 eV)."
    }
  ],
  "notes": "The agent is expected to fetch the crystal-field parameters from the referenced public papers and extract the experimental SFRS data from the Twardowski et al. publication. No hidden assets are required beyond those public resources."
}
```

## How you are scored
A hidden verifier independently inspects the artifacts you produce under /app/outputs. For step_01_energies_vs_B.csv it checks that the zero‑field spin‑flip energy, the positions of the anticrossings (fields where L1 and L2 come closest), and the overall curve shape agree with a hidden reference computed from the model described in the paper. For step_02_fitted_N0alpha.txt it compares your reported value to the paper’s own determination of the exchange parameter. Each scored artifact carries a weight; the final reward is the weighted sum of the scores. Simply reporting the numbers is insufficient—the verifier may recompute derived quantities from your outputs and expects them to match the expected behaviour of the model within reasonable tolerances.

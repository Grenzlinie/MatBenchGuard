# Li₂B₁₂H₁₂ Isomer Interconversion Energy Barriers from DFT

## Problem background
Lithium-ion migration barriers in solid-state electrolytes are critical for designing next-generation batteries. The energy landscape of lithium ions moving on the surface of a B12H12 icosahedral cage provides direct insight into lithium mobility and conductivity mechanisms. In the Li2B12H12 system, lithium atoms can occupy various diexo positions (both lithiums outside the cage, above different triangular faces) or an exo/endo arrangement (one lithium inside the cage, one outside). Isomer interconversion between these configurations determines the energy barriers that govern lithium motion. Using density functional theory (DFT), one can locate the stable isomers, find transition-state saddle points for the interconversion pathways, and compute the associated forward energy barriers and the imaginary vibrational frequencies that characterise the reaction coordinate. This task investigates the interconversion barriers for the four key pathways in Li2B12H12.

## Approach
The reproduction follows a quantum chemical approach using the B3LYP exchange-correlation functional with the 6-311+G(d,p) basis set. The workflow proceeds in three stages:

1. **Geometry optimisation of isomers**: Construct initial geometries for the five isomers of Li2B12H12. Four diexo isomers (labelled 1–4) correspond to the two lithium atoms occupying different non-contiguous triangular faces of the B12H12 icosahedron; the exo/endo isomer (labelled 5) has one lithium outside a face and the other inside the cage. Each structure is optimised at the DFT level to a local energy minimum, ensuring no imaginary vibrational frequencies remain.

2. **Transition-state (TS) search and vibrational analysis**: For each interconversion (1)↔(2), (2)↔(3), (3)↔(4), and (5)↔(2), an initial guess geometry is prepared by moving one lithium atom toward a shared edge while leaving the other fixed. The system is relaxed to a first-order saddle point. Harmonic vibrational frequencies are computed to confirm exactly one imaginary frequency, whose magnitude characterises the curvature along the reaction coordinate.

3. **Barrier calculation and output**: The forward barrier height ΔE is obtained from the energy difference between the transition state and the lower-energy minimum of the two isomers it connects. The barrier is converted to kcal/mol. A CSV file is written listing each interconversion, its barrier in kcal/mol, and the magnitude of the imaginary frequency in cm⁻¹.

## Reproduction target
Using the quantum chemistry code of your choice that supports B3LYP/6-311+G(d,p) calculations, perform geometry optimisations, transition state searches, and vibrational frequency analyses as described in the workflow steps. Compute the forward barrier heights (in kcal/mol) and the magnitude of the imaginary vibrational frequency (in cm⁻¹) for the four interconversions:
- (1)↔(2)
- (2)↔(3)
- (3)↔(4)
- (5)↔(2)

All calculations must use the B3LYP/6-311+G(d,p) level of theory. Store the final results in the file `/app/outputs/transition_state_results.csv` with the exact columns: `interconversion` (string, one of the above labels), `barrier_kcal_per_mol` (positive float), and `imag_freq_cm1` (positive float). This CSV is the scored artifact.

## Assets

- Quantum chemistry software supporting B3LYP/6-311+G(d,p): https://github.com/pyscf/pyscf

## Workflow steps

### Step 1: Geometry optimization of Li2B12H12 isomers
- Role: process
- Action: Construct initial geometries for diexo isomers (1)-(4) (Li atoms above non-contiguous triangular faces of the B12H12 icosahedron) and the exo/endo isomer (5) (one Li exo, one Li inside the cage). Perform geometry optimization at the B3LYP/6-311+G(d,p) level to obtain energy minima. Remove any imaginary frequencies if present.
- Evidence: `/app/outputs/minima_energies.txt`

### Step 2: Transition state search and vibrational analysis
- Role: process
- Action: For each interconversion (1)↔(2), (2)↔(3), (3)↔(4), (5)↔(2), set up an initial geometry guided from the minima (e.g., move one Li atom towards the shared edge while leaving the other fixed) and converge to a saddle point. Verify each is a first-order saddle point by computing harmonic vibrational frequencies; extract the imaginary frequency corresponding to the reaction coordinate.
- Evidence: `/app/outputs/ts_energies.txt`

### Step 3: Computation of barrier heights and output CSV
- Role: scored (load-bearing)
- Action: Using the energies of the minima and transition states from the preceding steps, compute the forward barrier height for each interconversion: ΔE = E_TS - E_lower_minimum. Convert the barrier to kcal/mol. Output a CSV file containing the interconversion identifier, the barrier in kcal/mol, and the magnitude of the imaginary frequency in cm⁻¹.
- Output file: `/app/outputs/transition_state_results.csv`
- Format: csv
- Contract: CSV with columns: interconversion (string, e.g., '1_to_2', '2_to_3', '3_to_4', '5_to_2'), barrier_kcal_per_mol (float > 0), imag_freq_cm1 (float > 0, magnitude of the imaginary frequency).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/transition_state_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### transition_state_results.csv
- path: `/app/outputs/transition_state_results.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: The computed forward barrier heights (ΔE, in kcal/mol) and imaginary vibrational frequencies (magnitude, in cm⁻¹) for the four isomer interconversions.
- schema:
  - `type`: table
  - `required_columns`: `interconversion`, `barrier_kcal_per_mol`, `imag_freq_cm1`
  - `units`:
    - `barrier_kcal_per_mol`: kcal/mol
    - `imag_freq_cm1`: cm^{-1}

Notes: The hidden checker compares each barrier and frequency to gold reference values with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "transition_state_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "interconversion",
          "barrier_kcal_per_mol",
          "imag_freq_cm1"
        ],
        "units": {
          "barrier_kcal_per_mol": "kcal/mol",
          "imag_freq_cm1": "cm^{-1}"
        }
      },
      "description": "The computed forward barrier heights (ΔE, in kcal/mol) and imaginary vibrational frequencies (magnitude, in cm⁻¹) for the four isomer interconversions."
    }
  ],
  "notes": "The hidden checker compares each barrier and frequency to gold reference values with appropriate tolerances."
}
```

## How you are scored
A hidden verifier reads your `/app/outputs/transition_state_results.csv` and compares each barrier height and imaginary frequency to independent reference values derived from the original study. The comparison accounts for the expected numerical spread between different DFT implementations and codes. For each interconversion, full credit is awarded if both the barrier and the imaginary frequency fall within the verifier’s acceptable tolerance range; otherwise credit is proportional to the number of correct rows. The verifier does not examine your intermediate energy files or optimisation logs; the sole scored output is the CSV. You must genuinely perform the DFT calculations to obtain the correct values; simply guessing or reporting pre‑known numbers will not satisfy the scoring requirements.

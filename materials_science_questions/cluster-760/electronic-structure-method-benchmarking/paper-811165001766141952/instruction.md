# Benchmark geometries and vibrational frequencies of small silicon nitride clusters

## Problem background
Small silicon nitride clusters, particularly the diatomic SiN and the triatomic SiN₂ and Si₂N, serve as important model systems for understanding the bonding and properties of silicon nitride materials. Accurate first-principles calculations of their equilibrium structures and vibrational frequencies are essential for interpreting experimental spectra and for guiding the design of new materials, but these calculations require choosing an appropriate level of quantum chemical theory that balances numerical accuracy with computational cost. In this task you will compute these properties for the three benchmark clusters using a specific density functional method and basis set.

## Approach
The computational approach uses Kohn-Sham density functional theory (DFT) with the B3LYP exchange-correlation functional and the 6-311G(d) basis set. For each molecule you will perform a geometry optimisation to find the equilibrium structure and then compute the harmonic vibrational frequencies from the force constants at the converged geometry. For the diatomic SiN, an additional linear-response time-dependent DFT (TDDFT) calculation at the same level of theory will be carried out to obtain the vertical excitation energy for the A²Π ← X²Σ⁺ transition. The target molecules are assumed to have the following charge, spin and connectivity: SiN in its doublet ground state; SiN₂ as the triplet asymmetric linear isomer Si–N≡N; and Si₂N as the doublet symmetric linear isomer Si=N=Si.

## Reproduction target
Produce a JSON file named `benchmark_results.json` inside `/app/outputs` that contains the equilibrium bond lengths (in Å), harmonic vibrational frequencies (in cm⁻¹), and, for SiN, the vertical excitation energy (in cm⁻¹). The file must follow the schema described in the output contract: an object with keys `SiN`, `SiN2` and `Si2N`. Under `SiN` provide the fields `re` (bond length), `we` (harmonic frequency), and `T_A2Pi` (excitation energy). Under `SiN2` provide the N–N and Si–N bond lengths (`r_NN`, `r_SiN`) and the three harmonic frequencies (`we1`, `we2`, `we3`). Under `Si2N` provide the Si–N bond length (`r_SiN`) and the three harmonic frequencies (`we1`, `we2`, `we3`). All values are floating-point numbers.

## Assets

- Open-source quantum chemistry package (ORCA, Psi4, or PySCF): https://psicode.org/

## Workflow steps

### Step 1: Compute benchmark quantities for SiN, SiN₂, Si₂N
- Role: scored (load-bearing)
- Action: Using an open-source quantum chemistry package, perform geometry optimization and harmonic vibrational frequency calculations for SiN (doublet), SiN₂ (triplet asymmetric linear SiNN), and Si₂N (doublet symmetric linear SiNSi) at the DFT/B3LYP/6-311G(d) level. For SiN, also perform a TDDFT vertical excitation energy calculation at the same level for the A²Π ← X²Σ⁺ transition. Write the optimized bond lengths, harmonic frequencies, and transition energy to the output JSON file.
- Output file: `/app/outputs/benchmark_results.json`
- Format: json
- Contract: A JSON object with keys: "SiN" (object with keys "re" (float, Å), "we" (float, cm⁻¹), "T_A2Pi" (float, cm⁻¹)), "SiN2" (object with keys "r_NN" (float, Å), "r_SiN" (float, Å), "we1" (float, cm⁻¹), "we2" (float, cm⁻¹), "we3" (float, cm⁻¹)), "Si2N" (object with keys "r_SiN" (float, Å), "we1" (float, cm⁻¹), "we2" (float, cm⁻¹), "we3" (float, cm⁻¹)).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/benchmark_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### benchmark_results.json
- path: `/app/outputs/benchmark_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: JSON file containing computed equilibrium bond lengths (Å), harmonic vibrational frequencies (cm⁻¹), and vertical excitation energy (cm⁻¹) for the benchmark systems. All values are floats.
- schema:
  - `type`: object
  - `required`:
    - `SiN`: object with keys re, we, T_A2Pi
    - `SiN2`: object with keys r_NN, r_SiN, we1, we2, we3
    - `Si2N`: object with keys r_SiN, we1, we2, we3
  - `items`: object
  - `required_columns`:
  - `units`:
    - `re`: Å
    - `r_NN`: Å
    - `r_SiN`: Å
    - `we`: cm⁻¹
    - `we1`: cm⁻¹
    - `we2`: cm⁻¹
    - `we3`: cm⁻¹
    - `T_A2Pi`: cm⁻¹

Notes: The target values are the specific computed results from DFT/B3LYP/6-311G(d) and TDDFT/B3LYP/6-311G(d) as reported in the paper; the verifier compares against hidden gold values with appropriate absolute tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "benchmark_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "SiN": "object with keys re, we, T_A2Pi",
          "SiN2": "object with keys r_NN, r_SiN, we1, we2, we3",
          "Si2N": "object with keys r_SiN, we1, we2, we3"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "re": "Å",
          "r_NN": "Å",
          "r_SiN": "Å",
          "we": "cm⁻¹",
          "we1": "cm⁻¹",
          "we2": "cm⁻¹",
          "we3": "cm⁻¹",
          "T_A2Pi": "cm⁻¹"
        }
      },
      "description": "JSON file containing computed equilibrium bond lengths (Å), harmonic vibrational frequencies (cm⁻¹), and vertical excitation energy (cm⁻¹) for the benchmark systems. All values are floats."
    }
  ],
  "notes": "The target values are the specific computed results from DFT/B3LYP/6-311G(d) and TDDFT/B3LYP/6-311G(d) as reported in the paper; the verifier compares against hidden gold values with appropriate absolute tolerances."
}
```

## How you are scored
A hidden verifier reads your `benchmark_results.json`, extracts every scalar quantity, and compares each one to a hidden gold value derived from the literature. Separate absolute tolerances are applied for bond lengths, vibrational frequencies, and the excitation energy. The overall score is the fraction of reported values that fall within their respective tolerance. Full credit (1.0) requires every value to be within tolerance; partial credit is awarded proportionally otherwise.

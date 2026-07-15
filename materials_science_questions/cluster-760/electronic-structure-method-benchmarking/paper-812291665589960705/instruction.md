# Harmonic Frequency Calculation for C2v Oxirene Ring-Opening Mode

## Problem background
Oxirene (C₂H₂O) is a strained three-membered-ring isomer of ketene whose stability as a chemical intermediate has been debated for decades. Whether the C₂ᵥ-symmetry oxirene structure is a genuine local minimum on the potential energy surface depends critically on the curvature of the ring-opening normal mode: a real harmonic vibrational frequency indicates a minimum, while an imaginary frequency would make it a saddle point (transition state). Quantum chemical calculations can compute this frequency, but different combinations of theoretical method and basis set yield qualitatively different answers — some predict a minimum, others a transition state. The definitive determination requires a high-level treatment of electron correlation together with a sufficiently flexible basis set. This task reproduces the key harmonic frequency that resolves the nature of the C₂ᵥ oxirene stationary point.

## Approach
Use coupled-cluster theory with single and double excitations and a perturbative treatment of connected triples [CCSD(T)] in the frozen-core approximation. The one-electron basis set is the correlation-consistent polarized valence triple-zeta set (cc-pVTZ) employing spherical harmonics (5d pure functions on heavy atoms, 7f pure functions). Constrain the molecule to C₂ᵥ symmetry throughout. Perform a full geometry optimization, then compute the harmonic vibrational frequencies at the optimized geometry. The mode of interest is the in-plane ring-deformation normal mode of b₂ symmetry that corresponds to opening of the three-membered ring. Extract its harmonic frequency in cm⁻¹. No other method/basis combinations need to be explored.

## Reproduction target
Compute the harmonic vibrational frequency (cm⁻¹) of the ring-deformation b₂ normal mode for C₂ᵥ oxirene at the CCSD(T)/cc-pVTZ level (frozen-core, spherical 5d,7f). Write a JSON object with keys "b2_frequency" (the numeric value) and "unit" (the string "cm⁻¹") to a file named b2_frequency.json in the output directory. This single number constitutes the reproduction target; no other frequencies, energies, or structural parameters need to be saved.

## Assets

- Psi4 (or equivalent open-source quantum chemistry package): https://psicode.org/

## Workflow steps

### Step 1: Compute ring-opening b2 frequency
- Role: scored (load-bearing)
- Action: Perform a CCSD(T) geometry optimization and harmonic vibrational frequency calculation on oxirene (C2H2O) constrained to C2v symmetry using the cc-pVTZ basis set with frozen-core approximation and spherical harmonics (5d,7f). Extract the harmonic frequency (in cm⁻¹) of the ring-deformation b2 normal mode and write a JSON object with keys b2_frequency and unit to /app/outputs/b2_frequency.json.
- Output file: `/app/outputs/b2_frequency.json`
- Format: json
- Contract: {"type": "object", "required": {"b2_frequency": "number", "unit": "string"}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/b2_frequency.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### b2_frequency.json
- path: `/app/outputs/b2_frequency.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The b2_frequency value (cm⁻¹) is the harmonic vibrational frequency of the ring-deformation b2 normal mode for C2v oxirene computed at CCSD(T)/cc-pVTZ (frozen-core, 5d7f). The unit string must be 'cm^-1' or equivalent.
- schema:
  - `type`: object
  - `required`:
    - `b2_frequency`: number
    - `unit`: string

Notes: The checker compares the b2_frequency to the hidden gold (the paper's reported CCSD(T)-fu/cc-pVTZ ring-opening frequency) with an appropriate tolerance that absorbs implementation differences. Only the frequency value is scored; the unit string presence is verified but not score-weighted.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "b2_frequency.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "b2_frequency": "number",
          "unit": "string"
        }
      },
      "description": "The b2_frequency value (cm⁻¹) is the harmonic vibrational frequency of the ring-deformation b2 normal mode for C2v oxirene computed at CCSD(T)/cc-pVTZ (frozen-core, 5d7f). The unit string must be 'cm^-1' or equivalent."
    }
  ],
  "notes": "The checker compares the b2_frequency to the hidden gold (the paper's reported CCSD(T)-fu/cc-pVTZ ring-opening frequency) with an appropriate tolerance that absorbs implementation differences. Only the frequency value is scored; the unit string presence is verified but not score-weighted."
}
```

## How you are scored
A hidden verifier reads /app/outputs/b2_frequency.json, extracts the b2_frequency value and the unit string, and compares the frequency to a hidden reference value using a tolerance that absorbs legitimate differences between quantum chemistry packages and numerical settings. Full credit is awarded when the computed frequency lies within the tolerance window; the score degrades smoothly as the deviation increases beyond that window. The unit string is checked for correctness ("cm⁻¹") but carries minor weight. No other output is evaluated. The final reward is a weighted combination across all scored workflow stages.

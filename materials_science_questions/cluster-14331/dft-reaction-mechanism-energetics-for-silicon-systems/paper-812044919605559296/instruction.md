# Compute Relative Energies of Si2NO Isomers and Transition States via DFT and Ab Initio Methods

## Problem background
The Si2NO radical is a small silicon-nitrogen-oxygen species relevant to interstellar chemistry and semiconductor materials. Several low-lying structural isomers exist, but only the chain-like form had been experimentally observed. A computational investigation of the potential energy surface can identify other stable isomers and predict their kinetic stability, which aids in the detection of new species in the laboratory and in space. This task focuses on mapping the relative energies of three key isomers and two important transition states.

## Approach
A hierarchical quantum chemistry approach is used to determine the relative stabilities. First, plausible initial geometries for the five target species are constructed based on chemical intuition about bonds and angles. These structures are then refined through a sequence of electronic structure calculations: (i) geometry optimization and harmonic vibrational frequency analysis at the density functional theory level (B3LYP functional) with a moderate basis set, (ii) optionally, further optimization at the correlated wavefunction theory level (QCISD) with the same basis, and (iii) single-point energy evaluation at the coupled-cluster level (CCSD(T)) with a larger basis set. Zero-point vibrational energy corrections are added to obtain total energies. Relative energies are reported with respect to the cyclic cSiNSiO 1 isomer, and the energy ordering among the isomers is used to assess stability.

## Reproduction target
Compute the relative energies (in kcal/mol) of the following five Si2NO species with respect to isomer cSiNSiO 1 (set to 0.0): the puckered isomer cSiNSiO 1', the bent chain isomer SiNSiO 3, the transition state TS1/3 connecting 1 and 3, and the transition state TS4/7 connecting SiOSiN 4 and N-cSiSiO 7. Use the CCSD(T)/6-311+G(2df) level of theory with zero-point vibrational energy corrections (from QCISD or B3LYP frequency calculations). Write the results to relative_energies.json.

## Assets

- Quantum chemistry software supporting DFT/B3LYP, QCISD, and CCSD(T) with 6-311G(d) and 6-311+G(2df) basis sets (e.g., ORCA, Psi4, NWChem)

## Workflow steps

### Step 1: Construct initial geometries
- Role: process
- Action: Construct initial Cartesian coordinates for the five target Si2NO species: cyclic cSiNSiO 1 (C2v symmetry, four-membered ring with Si-Si cross-bond), puckered cSiNSiO 1' (puckered ring with a long Si-Si cross-bond), bent SiNSiO 3 (chain Si-N-Si-O), transition state TS1/3 connecting 1 and 3, and TS4/7 connecting SiOSiN 4 and N-cSiSiO 7. Use approximate bond lengths and angles from typical values or chemical intuition; the geometries will be refined in subsequent steps.
- Evidence: none

### Step 2: B3LYP/6-311G(d) geometry optimization and frequency calculations
- Role: process
- Action: For each of the five species, perform geometry optimization and harmonic vibrational frequency calculation at the B3LYP/6-311G(d) level. Obtain equilibrium geometries, total energies, and zero-point vibrational energies (ZPVE). Verify that all stationary points are minima (no imaginary frequencies) or transition states (exactly one imaginary frequency).
- Evidence: none

### Step 3: QCISD/6-311G(d) geometry optimization (optional)
- Role: process
- Action: If computationally feasible, re-optimize geometries of the five species at the QCISD/6-311G(d) level to obtain higher-quality structures, harmonic frequencies, and ZPVE. If QCISD is too expensive, the B3LYP optimized geometries and ZPVE may be used instead.
- Evidence: none

### Step 4: Compute CCSD(T) relative energies
- Role: scored (load-bearing)
- Action: Perform single-point energy calculations at the CCSD(T)/6-311+G(2df) level using the QCISD-optimized (or B3LYP-optimized) geometries. Add the corresponding ZPVE from the QCISD (or B3LYP) harmonic frequency calculations to obtain total energies. Compute relative energies in kcal/mol with respect to isomer cSiNSiO 1 (set to 0.0). Write the results to relative_energies.json.
- Output file: `/app/outputs/relative_energies.json`
- Format: json
- Contract: {'cSiNSiO_1': 0.0, 'cSiNSiO_1_prime': <float>, 'SiNSiO_3': <float>, 'TS1_3': <float>, 'TS4_7': <float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/relative_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### relative_energies.json
- path: `/app/outputs/relative_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Relative energies of the five Si2NO species. The reference isomer cSiNSiO 1 is 0.0 kcal/mol. The checker will compare the submitted values against reference values with tolerances and verify the correct energy ordering (1 < 3 < 1').
- schema:
  - `type`: object
  - `required`: `cSiNSiO_1`, `cSiNSiO_1_prime`, `SiNSiO_3`, `TS1_3`, `TS4_7`
  - `properties`:
    - `cSiNSiO_1`:
      - `type`: number
      - `unit`: kcal/mol
    - `cSiNSiO_1_prime`:
      - `type`: number
      - `unit`: kcal/mol
    - `SiNSiO_3`:
      - `type`: number
      - `unit`: kcal/mol
    - `TS1_3`:
      - `type`: number
      - `unit`: kcal/mol
    - `TS4_7`:
      - `type`: number
      - `unit`: kcal/mol
  - `additionalProperties`: False

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "relative_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "cSiNSiO_1",
          "cSiNSiO_1_prime",
          "SiNSiO_3",
          "TS1_3",
          "TS4_7"
        ],
        "properties": {
          "cSiNSiO_1": {
            "type": "number",
            "unit": "kcal/mol"
          },
          "cSiNSiO_1_prime": {
            "type": "number",
            "unit": "kcal/mol"
          },
          "SiNSiO_3": {
            "type": "number",
            "unit": "kcal/mol"
          },
          "TS1_3": {
            "type": "number",
            "unit": "kcal/mol"
          },
          "TS4_7": {
            "type": "number",
            "unit": "kcal/mol"
          }
        },
        "additionalProperties": false
      },
      "description": "Relative energies of the five Si2NO species. The reference isomer cSiNSiO 1 is 0.0 kcal/mol. The checker will compare the submitted values against reference values with tolerances and verify the correct energy ordering (1 < 3 < 1')."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier will check your submitted relative energies against reference values and combine the checks into a final score. The scoring gives higher weight to the isomer energies and checks whether the four non-reference values fall within a tolerance, and it also verifies that the correct energy ordering (1 < 3 < 1') holds. The final reward is a single number between 0 and 1.

# Reproduce Quantum Chemistry Calculations for H₂SiOO and H₂COO Biradical Characterization

## Problem background
The oxidation of silylenes is of significant interest, but the structure and kinetic stability of the initial adduct, silanone oxide (H₂SiOO), in its singlet state remain poorly characterized. This task aims to determine the electronic structure of H₂SiOO—whether it possesses singlet biradical character and how readily it cyclizes to the more compact siladioxirane ring—and to contrast it with the carbon analogue H₂COO. The quantities of interest are computed using ab initio quantum chemistry methods.

## Approach
The investigation uses ab initio electronic structure methods with the 6-31G(d) basis set and an open-source quantum chemistry package (e.g., Psi4, ORCA, PySCF). The workflow proceeds as follows: First, geometries are optimized at the MP2/6-31G(d) level, and harmonic vibrational frequencies are calculated to characterize stationary points. Second, generalized valence bond perfect‑pairing (GVB-PP) calculations with three correlated pairs are performed to extract orbital overlaps that diagnose biradical character. These yield natural orbitals used as an initial guess for complete active space SCF (CASSCF(6,6)/6-31G(d)) calculations, from which effective localized spin populations are obtained. Third, the transition state for the cyclization of H₂SiOO to siladioxirane is located at the MP2/6-31G(d) level, and the energies of the reactant, transition state, and product are recorded. The same protocol (GVB and CASSCF) is applied to H₂COO for comparison.

## Reproduction target
Using an open-source quantum chemistry package, compute the following quantities and write them into /app/outputs/results.json according to the output contract:

1. MP2/6-31G(d) total energy (hartree) of H₂SiOO in its nonplanar (C₁) form, the cyclization transition state, and siladioxirane, plus a boolean flag indicating whether the planar (Cₛ) form has one imaginary frequency.
2. GVB/6-31G(d) orbital overlaps S_π, S(Si–Oᵃ), and S(Oᵃ–Oᵇ) for H₂SiOO and the corresponding overlaps for H₂COO.
3. CASSCF(6,6)/6-31G(d) effective localized spin populations on the heavy atom (Si or C) and on the terminal oxygen atom for both molecules.

All values must be reported in /app/outputs/results.json exactly as specified in the output contract.

## Assets

- Open-source quantum chemistry package (Psi4, ORCA, or PySCF): https://psicode.org/
- 6-31G(d) basis set

## Workflow steps

### Step 1: MP2/6-31G(d) Geometry Optimization and Frequency Analysis
- Role: process
- Action: Optimize geometries of singlet H₂SiOO in planar (Cₛ) and nonplanar (C₁) forms, the cyclization transition state, and siladioxirane at the MP2/6-31G(d) level. Perform harmonic vibrational frequency calculations to characterize stationary points and confirm that the planar structure has one imaginary frequency while the nonplanar structure is a minimum. Save optimized geometries as XYZ files.
- Evidence: `/app/outputs/mp2_geometries.xyz`

### Step 2: GVB/6-31G(d) Optimization and Orbital Overlap Extraction
- Role: process
- Action: Perform GVB perfect-pairing geometry optimization with three correlated pairs (Si–O σ, O–O σ, and π pair) for H₂SiOO (planar, nonplanar, TS, siladioxirane) and for H₂COO (Cₛ). Extract orbital overlaps S(Si–Oᵃ), S(Oᵃ–Oᵇ), S_π (Si–Oᵇ) for H₂SiOO, and S(C–Oᵃ), S(Oᵃ–Oᵇ), S(C–Oᵇ) for H₂COO. Save the overlaps to a text file.
- Evidence: `/app/outputs/gvb_overlaps.txt`

### Step 3: CASSCF(6,6)/6-31G(d) Spin Population Calculation
- Role: process
- Action: Using GVB natural orbitals as initial guess, run CASSCF(6,6)/6-31G(d) single-point calculations on the GVB-optimized nonplanar H₂SiOO and H₂COO geometries. Extract effective localized spin populations on Si and terminal Oᵇ for H₂SiOO, and on C and terminal Oᵇ for H₂COO. Save the spin populations to a text file.
- Evidence: `/app/outputs/casscf_spins.txt`

### Step 4: Assemble and Report All Target Quantities
- Role: scored (load-bearing)
- Action: Collect the computed results from the previous steps: MP2 energy of the nonplanar H₂SiOO minimum (in hartree), a boolean flag indicating whether the planar form has an imaginary frequency, the TS energy, siladioxirane energy, GVB overlaps for both H₂SiOO and H₂COO, and CASSCF effective localized spins for both molecules. Write all values into /app/outputs/results.json according to the output contract.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"H2SiOO_MP2_geom_file": "<path to .xyz>", "H2SiOO_MP2_energy_hartree": <float>, "H2SiOO_planar_imaginary_freq": <bool>, "H2SiOO_GVB_overlaps": {"S_pi": <float>, "S_Si_Oa": <float>, "S_Oa_Ob": <float>}, "H2SiOO_CASSCF_spins": {"Si": <float>, "O_terminal": <float>}, "H2SiOO_TS_energy_hartree": <float>, "H2SiOO_siladioxirane_energy_hartree": <float>, "H2COO_GVB_overlaps": {"S_pi": <float>, "S_C_Oa": <float>, "S_Oa_Ob": <float>}, "H2COO_CASSCF_spins": {"C": <float>, "O_terminal": <float>}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Aggregated reproduction results: MP2 energies and structural flags, GVB orbital overlaps, and CASSCF effective localized spin populations for H₂SiOO and H₂COO.
- schema:
  - `type`: object
  - `required`:
    - `H2SiOO_MP2_geom_file`: string (path)
    - `H2SiOO_MP2_energy_hartree`: float
    - `H2SiOO_planar_imaginary_freq`: boolean
    - `H2SiOO_GVB_overlaps`: object with keys S_pi, S_Si_Oa, S_Oa_Ob (all float)
    - `H2SiOO_CASSCF_spins`: object with keys Si, O_terminal (both float)
    - `H2SiOO_TS_energy_hartree`: float
    - `H2SiOO_siladioxirane_energy_hartree`: float
    - `H2COO_GVB_overlaps`: object with keys S_pi, S_C_Oa, S_Oa_Ob (all float)
    - `H2COO_CASSCF_spins`: object with keys C, O_terminal (both float)

Notes: All numeric fields are compared to hidden reference values from the original study using absolute tolerances appropriate for a re-run with a different quantum chemistry package.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "H2SiOO_MP2_geom_file": "string (path)",
          "H2SiOO_MP2_energy_hartree": "float",
          "H2SiOO_planar_imaginary_freq": "boolean",
          "H2SiOO_GVB_overlaps": "object with keys S_pi, S_Si_Oa, S_Oa_Ob (all float)",
          "H2SiOO_CASSCF_spins": "object with keys Si, O_terminal (both float)",
          "H2SiOO_TS_energy_hartree": "float",
          "H2SiOO_siladioxirane_energy_hartree": "float",
          "H2COO_GVB_overlaps": "object with keys S_pi, S_C_Oa, S_Oa_Ob (all float)",
          "H2COO_CASSCF_spins": "object with keys C, O_terminal (both float)"
        }
      },
      "description": "Aggregated reproduction results: MP2 energies and structural flags, GVB orbital overlaps, and CASSCF effective localized spin populations for H₂SiOO and H₂COO."
    }
  ],
  "notes": "All numeric fields are compared to hidden reference values from the original study using absolute tolerances appropriate for a re-run with a different quantum chemistry package."
}
```

## How you are scored
A hidden verifier reads your /app/outputs/results.json and compares each required numeric field to reference values from the original study, using tolerances that absorb the spread expected when re-running calculations with a different quantum chemistry package. The verifier computes a reward based on the fraction of fields that fall within acceptable tolerances. Correctly executing all prescribed computational steps is essential; merely reporting the paper's published numbers is insufficient and will likely fail the tolerance checks.

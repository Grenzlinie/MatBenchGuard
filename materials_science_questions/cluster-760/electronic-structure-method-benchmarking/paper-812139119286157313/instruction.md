# CO Adsorption Energies and Frequency Shifts on Cation-Exchanged Chabazite

## Problem background
Zeolites that contain exchangeable extraframework cations (H⁺, Li⁺, Na⁺, K⁺) are widely used in gas separation and catalysis. The adsorption of carbon monoxide (CO) is a sensitive probe of the local electric field around the cation, because the CO vibrational frequency shifts upward (hypsochromic shift) upon binding and its binding energy reflects the cation's Lewis acidity. Periodic density functional theory (DFT) calculations can predict both the binding energy and the C−O stretching frequency for CO adsorbed on cation-exchanged chabazite (Si/Al = 11/1), providing a benchmark for interpreting experiments on a well-defined model system.

## Approach
The reproduction uses periodic DFT with the hybrid B3LYP functional and a polarized double-zeta (DZP) quality Gaussian basis set. The chabazite framework is built in the rhombohedral unit cell (a = 9.36 Å, α = 94.67°, space group R‑3m) with one Al atom per unit cell. Extraframework cations are placed at the sites identified in prior literature: Li⁺ and Na⁺ at SII, H⁺ (as a bridging hydroxyl) and K⁺ at SIII′. Four separate models are constructed: the bare zeolite with the cation (X‑CHA) and isolated CO, and the CO‑adsorbed complex (X‑CHA/CO). All internal coordinates are optimized while keeping the lattice parameters fixed. Total energies are computed for each optimized structure. The raw binding energy BE = E(X‑CHA/CO) − E(X‑CHA) − E(CO) is corrected for basis set superposition error (BSSE) by the counterpoise method (ghost basis sets at the complex geometry). The harmonic CO stretching frequencies are obtained by a partial Hessian: only the CO bond is displaced (finite‑difference step 0.001 Å) using analytic gradients. The BSSE‑corrected binding energy BEⁿ and the hypsochromic shift Δν = ν(CO/complex) − ν(CO) are computed for each of the four cations. Because the original calculations used the proprietary CRYSTAL code, the workflow is re‑scoped to the open‑source CP2K program, which supports hybrid functionals and Gaussian basis sets; an equivalent DZP‑quality basis set library (e.g., pob‑TZVP or DZVP‑MOLOPT) is employed. All required inputs—framework parameters, cation sites, and basis set definitions—are publicly available.

## Reproduction target
Produce the BSSE‑corrected CO binding energies (BEⁿ, kJ mol⁻¹) and the hypsochromic CO stretching frequency shifts (Δν, cm⁻¹) for H⁺, Li⁺, Na⁺, and K⁺ exchanged chabazite. Write all eight values to /app/outputs/results.json according to the output contract. The target is to obtain results that are physically reasonable (all binding energies positive, frequency shifts positive) and that exhibit the correct relative ordering among cations, as expected from electrostatic and size arguments.

## Assets

- CP2K: https://www.cp2k.org/
- All-silica chabazite B3LYP unit cell parameters: 10.1063/1.1497628
- Cation locations in Si/Al=11/1 chabazite: 10.1021/cm0347924
- Basis set library (DZP quality): https://www.cp2k.org/basis_sets

## Workflow steps

### Step 1: Build initial structures and assign basis sets
- Role: process
- Action: Construct the periodic chabazite framework (Si/Al=11/1) using the rhombohedral cell a=9.36 Å, α=94.67° (space group R-3m), place extraframework cations according to literature (Li⁺ and Na⁺ at SII, H⁺ and K⁺ at SIII’), and select an appropriate DZP-quality Gaussian basis set for all atoms.
- Evidence: none

### Step 2: Optimize geometries of bare X-CHA zeolites
- Role: process
- Action: For each X-CHA (X = H⁺, Li⁺, Na⁺, K⁺), perform a periodic B3LYP geometry optimization with fixed lattice parameters and analytic gradients. Record optimized structures and total energies.
- Evidence: `/app/outputs/opt_bare.log`

### Step 3: Optimize geometries of CO–zeolite complexes
- Role: process
- Action: For each X-CHA, place CO with carbon end toward cation at initial distance ~2.0 Å, optimize the X-CHA/CO complex at B3LYP level, and record total energies and final geometries.
- Evidence: `/app/outputs/opt_complex.log`

### Step 4: Compute raw binding energies and BSSE corrections
- Role: process
- Action: For each cation, compute raw binding energy BE = E(X-CHA/CO) − E(X-CHA) − E(CO). Compute BSSE via counterpoise method using ghost basis sets at the complex geometry. Record BE and BSSE.
- Evidence: `/app/outputs/energies_binding.csv`

### Step 5: Compute CO harmonic stretching frequencies
- Role: process
- Action: For each X-CHA/CO complex and isolated CO, compute harmonic CO stretching frequency by numerical differentiation of analytic gradients with a finite-difference step of 0.001 Å (partial Hessian approximation). Record ν(CO/X-CHA) and ν(CO).
- Evidence: `/app/outputs/frequencies.csv`

### Step 6: Assemble and output final results
- Role: scored (load-bearing)
- Action: Compute BSSE-corrected binding energies BEⁿ = BE − BSSE (kJ/mol) and CO hypsochromic frequency shifts Δν = ν(CO/X-CHA) − ν(CO) (cm⁻¹) for H⁺, Li⁺, Na⁺, K⁺. Write all eight values to /app/outputs/results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"H_BE_n": float (kJ/mol), "Li_BE_n": float, "Na_BE_n": float, "K_BE_n": float, "H_delta_nu": float (cm⁻¹), "Li_delta_nu": float, "Na_delta_nu": float, "K_delta_nu": float}
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
- target_policy: structural_audit
- description: BSSE-corrected CO binding energies and hypsochromic CO stretching frequency shifts for H⁺, Li⁺, Na⁺, and K⁺ exchanged chabazite. The checker verifies the ordering relationships and positivity, not absolute values.
- schema:
  - `type`: object
  - `required`: `H_BE_n`, `Li_BE_n`, `Na_BE_n`, `K_BE_n`, `H_delta_nu`, `Li_delta_nu`, `Na_delta_nu`, `K_delta_nu`
  - `properties`:
    - `H_BE_n`:
      - `type`: number
      - `units`: kJ/mol
    - `Li_BE_n`:
      - `type`: number
      - `units`: kJ/mol
    - `Na_BE_n`:
      - `type`: number
      - `units`: kJ/mol
    - `K_BE_n`:
      - `type`: number
      - `units`: kJ/mol
    - `H_delta_nu`:
      - `type`: number
      - `units`: cm^-1
    - `Li_delta_nu`:
      - `type`: number
      - `units`: cm^-1
    - `Na_delta_nu`:
      - `type`: number
      - `units`: cm^-1
    - `K_delta_nu`:
      - `type`: number
      - `units`: cm^-1

Notes: Scoring uses structural audit: check that Li_BE_n > Na_BE_n > H_BE_n > K_BE_n and Li_delta_nu > H_delta_nu > Na_delta_nu > K_delta_nu, and that all BEⁿ are > 0. Absolute values may vary with basis set/implementation.

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
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "H_BE_n",
          "Li_BE_n",
          "Na_BE_n",
          "K_BE_n",
          "H_delta_nu",
          "Li_delta_nu",
          "Na_delta_nu",
          "K_delta_nu"
        ],
        "properties": {
          "H_BE_n": {
            "type": "number",
            "units": "kJ/mol"
          },
          "Li_BE_n": {
            "type": "number",
            "units": "kJ/mol"
          },
          "Na_BE_n": {
            "type": "number",
            "units": "kJ/mol"
          },
          "K_BE_n": {
            "type": "number",
            "units": "kJ/mol"
          },
          "H_delta_nu": {
            "type": "number",
            "units": "cm^-1"
          },
          "Li_delta_nu": {
            "type": "number",
            "units": "cm^-1"
          },
          "Na_delta_nu": {
            "type": "number",
            "units": "cm^-1"
          },
          "K_delta_nu": {
            "type": "number",
            "units": "cm^-1"
          }
        }
      },
      "description": "BSSE-corrected CO binding energies and hypsochromic CO stretching frequency shifts for H⁺, Li⁺, Na⁺, and K⁺ exchanged chabazite. The checker verifies the ordering relationships and positivity, not absolute values."
    }
  ],
  "notes": "Scoring uses structural audit: check that Li_BE_n > Na_BE_n > H_BE_n > K_BE_n and Li_delta_nu > H_delta_nu > Na_delta_nu > K_delta_nu, and that all BEⁿ are > 0. Absolute values may vary with basis set/implementation."
}
```

## How you are scored
A hidden verifier reads your /app/outputs/results.json and checks structural properties: that all BEⁿ are > 0, that both sets of values follow the expected cation ordering (which is deducible from ionic size/charge arguments), and that the frequency shifts are positive. The verifier does not compare your absolute numbers to a single published value; it evaluates whether your computed trends are physically consistent and match the well‑established electrostatic picture of CO‑cation interactions. The total reward is a weighted sum over the scored artifact (the main results file) and is reported as a number between 0 and 1. Passing does not require hitting exact literature numbers, but a correct quantum‑chemical workflow that captures the correct trends will earn full credit.

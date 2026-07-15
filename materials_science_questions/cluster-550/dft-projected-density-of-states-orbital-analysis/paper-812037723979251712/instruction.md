# Half-Metallicity and Magnetic Moments of CrP(001) Surfaces from First-Principles

## Problem background
Half-metallic ferromagnets are attractive for spintronic devices because they can supply 100% spin-polarized currents. Bulk zinc-blende CrP has been predicted to be a half-metal, but real device applications require knowledge of the magnetic and electronic properties of its surfaces. This task investigates the CrP(001) surface to determine whether the half-metallic character of the bulk is preserved at the surface and how the atomic magnetic moments are modified, using first-principles all-electron calculations.

## Approach
Use the full-potential linearized augmented plane wave (FLAPW) method with the generalized gradient approximation (GGA) to perform spin-polarized density-functional theory calculations. Simulate the (001) surface as two symmetric slab models—a 9-layer Cr-terminated slab and an 11-layer P-terminated slab—for two in-plane lattice constants: a_ZB = 5.48 Å (the calculated bulk equilibrium) and a_InP = 5.89 Å (the experimental InP lattice constant). Surface relaxation is known to be negligible; treat the slabs as unrelaxed with a vacuum region. From the self-consistent ground state, compute the spin-polarized density of states (DOS) projected onto atomic sites and integrate the spin density inside muffin-tin spheres to obtain layer-resolved magnetic moments. Extract the minority-spin band gap at the surface, the Cr exchange splitting as the energy separation of majority and minority Cr d-peaks, the half-metallic status (presence or absence of minority-spin states at the Fermi level), and the magnetic moments for Cr and P atoms in the surface (S) and subsurface (S-1) layers across all four slab configurations.

## Reproduction target
For each of the four slab configurations (Cr-terminated a_ZB, Cr-terminated a_InP, P-terminated a_ZB, P-terminated a_InP), compute and report the following quantities in a structured JSON file at /app/outputs/results.json: (i) the minority-spin surface band gap in eV, (ii) the Cr exchange splitting in eV, (iii) a boolean flag indicating whether the surface is half-metallic (true if no minority-spin states appear at the Fermi level, false otherwise), and (iv) the atomic magnetic moments (in μB) for the Cr and P atoms in the surface (S) and subsurface (S-1) layers. The results.json file must follow the exact schema described in the output contract.

## Assets

- Elk (all-electron FLAPW code): https://elk.sourceforge.net/

## Workflow steps

### Step 1: Slab Geometry Construction
- Role: process
- Action: Build 9-layer Cr-terminated and 11-layer P-terminated slabs for CrP(001) with zinc-blende structure at lattice constants a_ZB=5.48 Å and a_InP=5.89 Å. Include appropriate muffin-tin radii and a vacuum region.
- Evidence: none

### Step 2: Convergence and Surface Relaxation Check
- Role: process
- Action: Determine adequate basis set size and k-point mesh that yield stable magnetic moments, and test surface relaxation by computing total energy vs. top-layer displacement. Confirm that relaxation is negligible and select converged parameters.
- Evidence: none

### Step 3: Self-consistent FLAPW Calculations
- Role: process
- Action: Run spin-polarized FLAPW-GGA calculations for each of the four slab configurations (Cr-term a_ZB, Cr-term a_InP, P-term a_ZB, P-term a_InP) using the converged settings to obtain ground-state charge and spin densities.
- Evidence: none

### Step 4: DOS and Magnetic Moment Computation
- Role: process
- Action: From the SCF results, compute spin-polarized total and atom-projected density of states, and integrate the spin density inside muffin-tin spheres to obtain layer-resolved magnetic moments for surface (S) and subsurface (S-1) layers.
- Evidence: none

### Step 5: Extract and Report Key Quantities
- Role: scored (load-bearing)
- Action: Analyze the projected DOS and magnetic moments to extract for each termination and lattice constant: (i) minority-spin surface band gap (eV), (ii) Cr exchange splitting (eV) as energy difference between majority and minority Cr d-peaks, (iii) half-metallic flag (true if no minority states at the Fermi level), (iv) magnetic moments (µB) for Cr and P at surface and subsurface layers. Write all results to /app/outputs/results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: type=object; top-level key 'terminations': array of objects with fields: 'termination' (string enum: Cr,P), 'lattice_constant' (string enum: a_ZB,a_InP), 'minority_gap_ev' (float), 'exchange_splitting_ev' (float), 'half_metallic' (boolean), 'magnetic_moments' (array of objects with 'atom' (string Cr/P), 'layer' (string S/S-1/center), 'moment_mu_B' (float)).
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
- description: Summary of the computed half-metallic character, minority band gap, exchange splitting, and layer-resolved magnetic moments for Cr- and P-terminated CrP(001) surfaces at both a_ZB and a_InP lattice constants.
- schema:
  - `type`: object
  - `required`:
    - `terminations`: array
  - `items`:
    - `type`: object
    - `properties`:
      - `termination`: string
      - `lattice_constant`: string
      - `minority_gap_ev`: number
      - `exchange_splitting_ev`: number
      - `half_metallic`: boolean
      - `magnetic_moments`: array of {atom: string, layer: string, moment_mu_B: number}
  - `units`:
    - `minority_gap_ev`: eV
    - `exchange_splitting_ev`: eV
    - `moment_mu_B`: μB

Notes: The checker uses hidden gold values extracted from the paper (gap ~2.0 eV, exchange splitting ~3.50 eV, magnetic moments from Table 1) and compares using tolerances: gap ±0.3 eV, exchange splitting ±0.5 eV, moments ±0.2 μB. Half-metallic flag is checked for logical consistency with the gap and surface states description.

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
          "terminations": "array"
        },
        "items": {
          "type": "object",
          "properties": {
            "termination": "string",
            "lattice_constant": "string",
            "minority_gap_ev": "number",
            "exchange_splitting_ev": "number",
            "half_metallic": "boolean",
            "magnetic_moments": "array of {atom: string, layer: string, moment_mu_B: number}"
          }
        },
        "units": {
          "minority_gap_ev": "eV",
          "exchange_splitting_ev": "eV",
          "moment_mu_B": "μB"
        }
      },
      "description": "Summary of the computed half-metallic character, minority band gap, exchange splitting, and layer-resolved magnetic moments for Cr- and P-terminated CrP(001) surfaces at both a_ZB and a_InP lattice constants."
    }
  ],
  "notes": "The checker uses hidden gold values extracted from the paper (gap ~2.0 eV, exchange splitting ~3.50 eV, magnetic moments from Table 1) and compares using tolerances: gap ±0.3 eV, exchange splitting ±0.5 eV, moments ±0.2 μB. Half-metallic flag is checked for logical consistency with the gap and surface states description."
}
```

## How you are scored
A hidden verifier reads your /app/outputs/results.json and compares each reported value (minority gap, exchange splitting, half-metallic flag, and each magnetic moment) against a hidden reference that represents the paper's computational result. Comparisons are made with numerical tolerances appropriate for an independent FLAPW-GGA calculation, and the boolean flag is checked for consistency with the DOS-derived presence/absence of minority-spin surface states. The final reward is a weighted combination of the scores for the individual quantities; only the content of results.json is scored. Intermediate artifacts are not evaluated.

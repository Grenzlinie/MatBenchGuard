# DFT Study of Fe Effect on HCN Desorption from Nitrogen-Containing Char

## Problem background
During coal combustion, the nitrogen species HCN is a key precursor to the pollutant NOx. Understanding the release of HCN from nitrogen-containing char is critical because the mineral iron (Fe) inherently present in coal can influence this process. The goal of this task is to investigate whether Fe adsorbed on char surfaces promotes or inhibits the formation of HCN. We use density functional theory (DFT) to compute the activation energy barriers for the rate-determining steps of HCN desorption from a model char, and the Mayer bond order of the C5–N bond in the initial structures, for three systems: (1) bare nitrogen-containing char, (2) char with Fe adsorbed at a hollow site interacting only with carbon (H1), and (3) char with Fe directly bonded to nitrogen (H7). Together these quantities allow one to infer whether Fe increases or decreases the energetic cost and bond strength relative to bare char.

## Approach
We consider a zigzag-edge char model consisting of seven fused benzene rings with a single pyridinic nitrogen atom, as commonly used for carbonaceous surfaces. The Fe atom is adsorbed in hollow sites above the aromatic rings; the H1 site represents Fe interacting only with carbon, while the H7 site is the position where Fe bonds directly to the nitrogen. All DFT calculations employ the B3LYP functional with D3 dispersion correction and a mixed basis set (6-31G(d) for C, H, N and the LanL2DZ effective core potential for Fe). Geometry optimisations are followed by harmonic vibrational frequency checks to confirm minima and transition states. The rate-determining step for HCN desorption from bare and H1-adsorbed systems is the ring-opening breaking of the C5–N bond; for the H7-adsorbed system the rate-determining step is the final Fe–N bond cleavage. Transition states are verified by intrinsic reaction coordinate (IRC) calculations, and Mayer bond orders are obtained from the wavefunction files using Multiwfn. The procedure is fully reproducible with the open‑source packages ORCA and Multiwfn.

## Reproduction target
Build the nitrogen-containing char model, optimise the bare and Fe‑adsorbed geometries (H1 and H7), locate the three transition states that correspond to the rate‑determining steps, and confirm each by IRC. From the optimised minima and transition states compute the activation energy barriers (kJ/mol) for the three systems: barrier for bare → TS1, for H1‑adsorbed → Fe⁽¹⁾TS1, and for H7‑adsorbed → Fe⁽⁷⁾TS4 (the step from Fe⁽⁷⁾M4 to final HCN release). Also compute the Mayer bond order of the C5–N bond in the three initial optimised structures (bare C(N), Fe⁽¹⁾M1, Fe⁽⁷⁾M1). Write all six values into a JSON file at `/app/outputs/results.json` with the keys `bare_barrier_kJ_per_mol`, `H1_barrier_kJ_per_mol`, `H7_barrier_kJ_per_mol`, `bare_C5N_bond_order`, `H1_C5N_bond_order`, `H7_C5N_bond_order`. The hidden verifier will then evaluate both the numerical values and the relative trends among the three systems.

## Assets

- ORCA quantum chemistry package: https://orcaforum.kofo.mpg.de/
- Multiwfn wavefunction analyzer: http://sobereva.com/multiwfn/

## Workflow steps

### Step 1: Build nitrogen-containing char model
- Role: process
- Action: Construct the zigzag-edge nitrogen-containing char model (C(N)) consisting of seven fused benzene rings with one pyridinic nitrogen atom at the position described in the paper. Saturate dangling bonds with hydrogen except on the upper unsaturated active edge. The resulting molecular coordinates define the bare char model.
- Evidence: none

### Step 2: Optimize bare and Fe-adsorbed geometries
- Role: process
- Action: Using DFT with the B3LYP functional, D3 dispersion correction, 6-31G(d) basis for C/H/N and LanL2DZ effective core potential for Fe, fully optimize the geometries of: (i) bare C(N), (ii) C(N) with one Fe atom adsorbed at the H1 hollow site (Fe⁽¹⁾M1), and (iii) C(N) with Fe adsorbed at the H7 site (Fe⁽⁷⁾M1). Perform harmonic vibrational frequency calculations at the same level to confirm all structures are true minima (no imaginary frequencies).
- Evidence: none

### Step 3: Find transition states for rate-determining steps
- Role: process
- Action: Locate the rate-determining transition states: (a) For bare C(N), the TS for C5-N bond breaking (TS1, ring-opening step). (b) For the H1-adsorbed system, the analogous TS (Fe⁽¹⁾TS1). (c) For the H7 pathway, first identify the intermediate Fe⁽⁷⁾M4 (the structure immediately before final HCN release, as described in the paper) and then locate the TS for Fe-N bond cleavage (Fe⁽⁷⁾TS4). Use saddle-point optimization methods and verify that each TS has exactly one imaginary frequency corresponding to the bond-breaking coordinate.
- Evidence: none

### Step 4: Verify transition states by IRC
- Role: process
- Action: For each located transition state (TS1, Fe⁽¹⁾TS1, Fe⁽⁷⁾TS4), run intrinsic reaction coordinate (IRC) calculations in both forward and reverse directions to confirm that each TS connects the correct reactant and product minima.
- Evidence: none

### Step 5: Compute activation barriers and Mayer bond orders
- Role: scored (load-bearing)
- Action: Extract electronic energies (including zero-point corrections) for the relevant minima and transition states to compute activation energy barriers ΔE (kJ/mol) as: (i) bare: E(TS1) – E(C(N)), (ii) H1: E(Fe⁽¹⁾TS1) – E(Fe⁽¹⁾M1), (iii) H7: E(Fe⁽⁷⁾TS4) – E(Fe⁽⁷⁾M4). Using the optimized minimum structures (C(N), Fe⁽¹⁾M1, Fe⁽⁷⁾M1), compute the Mayer bond order of the C5-N bond with Multiwfn. Write all six values to a JSON file.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: { "bare_barrier_kJ_per_mol": number, "H1_barrier_kJ_per_mol": number, "H7_barrier_kJ_per_mol": number, "bare_C5N_bond_order": number, "H1_C5N_bond_order": number, "H7_C5N_bond_order": number }
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
- description: Activation energy barriers (kJ/mol) for the rate-determining steps of HCN desorption from bare char (bare), Fe-adsorbed at H1 site, and Fe-adsorbed at H7 site; and Mayer bond orders of the C5-N bond in the corresponding initial optimized structures. The checker verifies both the numerical closeness to the paper's reported values (within tolerances) and the required ordering trends (H1 barrier > bare barrier > H7 barrier; H1 bond order > bare bond order > H7 bond order).
- schema:
  - `type`: object
  - `required`:
    - `bare_barrier_kJ_per_mol`: number
    - `H1_barrier_kJ_per_mol`: number
    - `H7_barrier_kJ_per_mol`: number
    - `bare_C5N_bond_order`: number
    - `H1_C5N_bond_order`: number
    - `H7_C5N_bond_order`: number

Notes: Reference values are from the original paper's Table 3 (barriers) and Table 4 (bond orders). Tolerances: ±25 kJ/mol for energy barriers, ±0.15 for bond orders, to accommodate differences between ORCA and the original Gaussian09 calculations.

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
          "bare_barrier_kJ_per_mol": "number",
          "H1_barrier_kJ_per_mol": "number",
          "H7_barrier_kJ_per_mol": "number",
          "bare_C5N_bond_order": "number",
          "H1_C5N_bond_order": "number",
          "H7_C5N_bond_order": "number"
        }
      },
      "description": "Activation energy barriers (kJ/mol) for the rate-determining steps of HCN desorption from bare char (bare), Fe-adsorbed at H1 site, and Fe-adsorbed at H7 site; and Mayer bond orders of the C5-N bond in the corresponding initial optimized structures. The checker verifies both the numerical closeness to the paper's reported values (within tolerances) and the required ordering trends (H1 barrier > bare barrier > H7 barrier; H1 bond order > bare bond order > H7 bond order)."
    }
  ],
  "notes": "Reference values are from the original paper's Table 3 (barriers) and Table 4 (bond orders). Tolerances: ±25 kJ/mol for energy barriers, ±0.15 for bond orders, to accommodate differences between ORCA and the original Gaussian09 calculations."
}
```

## How you are scored
An automated hidden verifier reads your `/app/outputs/results.json`. It compares each activation barrier and bond order against hidden reference values (derived from the original study) with tolerances that account for the use of open‑source software instead of the original commercial code. It also checks whether the ordering of the three systems (barriers and bond orders) follows the pattern expected from the paper's analysis. The final reward is a weighted sum: half of the score comes from the numerical closeness of your computed values to the references, and half from the correctness of the observed trends. Providing the paper's reported numbers without performing the actual DFT calculations will not yield a perfect score because the trend checks require genuine structure‑based results.

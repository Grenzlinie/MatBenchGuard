# DFT Band Gap Calculation for Double-Perovskite Oxides A2SmTaO6 (A=Ba, Sr, Ca)

## Problem background
Double-perovskite oxides of the form A2SmTaO6 (A = Ba, Sr, Ca) are promising materials for microwave dielectric applications. Their electronic structure, in particular the direct band gap, governs their conductivity and is therefore a key quantity to understand. This task reproduces the density-functional-theory (DFT) calculation of the majority-spin direct band gap for these three compounds.

## Approach
Perform spin-polarised DFT calculations using the GGA+U method with an effective Hubbard U of 7 eV applied to the Sm 4f states. Use the experimentally determined crystal structures (lattice parameters and atomic positions provided in the workflow steps) and relax the internal coordinates while keeping the cell fixed. Compute the electronic band structure and density of states, then extract the direct band gap for each compound as the minimum energy difference between the valence band maximum (VBM) and conduction band minimum (CBM) at the same k-point in the majority-spin channel. Open-source plane-wave pseudopotential codes (e.g. Quantum ESPRESSO) may be used.

## Reproduction target
Determine the direct band gaps (majority-spin) for Ba2SmTaO6 (BST), Sr2SmTaO6 (SST), and Ca2SmTaO6 (CST). Report the computed values and verify the relative ordering of the gaps across the series.

## Assets

- Quantum ESPRESSO: quantum-espresso
- SSSP efficiency pseudopotentials: https://www.materialscloud.org/discover/sssp/table/efficiency/

## Crystal structures

The crystallographic data for the three double-perovskite oxides are given below. Use these lattice parameters and atomic positions to construct the input geometries for your DFT calculations.

### BST (Ba2SmTaO6)
- Space group: Fm-3m (cubic)
- Lattice constant: a = b = c = 8.475 Å
- Atomic positions (fractional coordinates):
  - Ba  (0.2500, 0.2500, 0.2500)
  - Sm  (0.0000, 0.0000, 0.0000)
  - Ta  (0.5000, 0.5000, 0.5000)
  - O   (0.2640, 0.0000, 0.0000)  # x coordinate from Table I

### SST (Sr2SmTaO6)
- Space group: P2_1/n (monoclinic)
- Lattice parameters: a = 5.826 Å, b = 5.900 Å, c = 8.281 Å, β = 90.162°
- Atomic positions (fractional coordinates):
  - Sr  (0.0045, 0.0346, 0.2583)
  - Sm  (0.5000, 0.0000, 0.0000)
  - Ta  (0.5000, 0.0000, 0.5000)
  - O1  (0.2580, 0.2869, 0.0335)
  - O2  (0.1477, 0.2808, -0.2114)
  - O3  (-0.1083, 0.4882, 0.2295)

### CST (Ca2SmTaO6)
- Space group: P2_1/n (monoclinic)
- Lattice parameters: a = 5.570 Å, b = 5.831 Å, c = 8.081 Å, β = 89.737°
- Atomic positions (fractional coordinates):
  - Ca  (0.4872, 0.5571, 0.2437)
  - Sm  (0.5000, 0.0000, 0.5000)
  - Ta  (0.5000, 0.0000, 0.0000)
  - O1  (0.3145, 0.2863, 0.0512)
  - O2  (0.2153, 0.8060, 0.0504)
  - O3  (0.5967, 0.0717, 0.2704)

## Workflow steps

### Step 1: Run DFT calculations
- Role: process
- Action: For each compound (BST, SST, CST): prepare the crystal structure using the given lattice parameters and atomic positions; perform spin-polarized GGA+U (U=7 eV on Sm 4f) DFT calculations with an open-source plane-wave pseudopotential DFT code (e.g., Quantum ESPRESSO); extract the direct band gap (majority-spin channel, VBM-CBM at same k-point).
- Evidence: none

### Step 2: Report band gaps
- Role: scored (load-bearing)
- Action: Write the computed direct band gaps for BST, SST, CST to band_gaps.csv. For each compound, report the compound name and the band gap (in eV).
- Output file: `/app/outputs/band_gaps.csv`
- Format: csv
- Contract: compound (string, one of BST/SST/CST), band_gap (float in eV, majority-spin direct gap)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gaps.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gaps.csv
- path: `/app/outputs/band_gaps.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Reported direct band gaps (majority spin) for the three double-perovskite compounds.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `band_gap`
  - `units`:
    - `band_gap`: eV

Notes: The hidden checker reads band_gaps.csv, compares the reported band gap values to reference values within a tolerance, and verifies the ordering BST_gap < SST_gap < CST_gap.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gaps.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "band_gap"
        ],
        "units": {
          "band_gap": "eV"
        }
      },
      "description": "Reported direct band gaps (majority spin) for the three double-perovskite compounds."
    }
  ],
  "notes": "The hidden checker reads band_gaps.csv, compares the reported band gap values to reference values within a tolerance, and verifies the ordering BST_gap < SST_gap < CST_gap."
}
```

## How you are scored
A hidden verifier reads your `/app/outputs/band_gaps.csv`. It compares your reported band gap values to hidden reference values (within a tolerance) and checks that the ordering BST < SST < CST holds. The final score combines: 70% weight on the accuracy of the three gap values (equal weight per compound) and 30% weight on the correct ordering. You must genuinely execute the DFT calculations; the verifier only inspects the final CSV.

# First-principles DFT calculation of the crystal structure and band gap of Rb2Ti2O5

## Problem background
The ternary titanium oxide Rb2Ti2O5 belongs to the family of Anderson‑Wadsley type alkali titanates, which exhibit layered structures and potential for high dielectric constants and ionic conductivity. The crystal structure of this compound has been under debate, with earlier reports proposing a non‑centrosymmetric space group, while more recent X‑ray diffraction and Raman spectroscopy measurements indicate a centrosymmetric C2/m structure that remains unchanged across a wide temperature range. Density functional theory (DFT) calculations are essential to confirm the thermodynamic stability of this structure and to determine its electronic properties, in particular the enthalpy of formation and the insulating band gap.

## Approach
The reproduction uses first‑principles DFT within the generalized gradient approximation of Perdew, Burke, and Ernzerhof (GGA‑PBE) as implemented in the open‑source Quantum Espresso package. Starting from the experimentally reported C2/m unit cell (containing two formula units of Rb2Ti2O5) and the associated fractional atomic coordinates, a variable‑cell structural relaxation is performed to obtain the equilibrium lattice constants and total energy. The relaxation employs ultrasoft pseudopotentials that include semi‑core states for Rb and Ti, a plane‑wave basis set with a cutoff sufficient for converged energies, and a Monkhorst–Pack k‑point mesh. After the relaxation, the ground‑state total energies of the elemental reference phases — body‑centered cubic Rb, hexagonal close‑packed Ti, and the triplet O2 molecule (simulated in a supercell with vacuum) — are calculated under identical DFT settings. These energies are used to derive the enthalpy of formation through a standard thermodynamic cycle. Finally, a self‑consistent Kohn–Sham calculation followed by a non‑self‑consistent calculation along the high‑symmetry path of the monoclinic C‑centered lattice (Γ–Y–F–L–I–X–Z–Γ) is performed to extract the valence band maximum and conduction band minimum, from which the fundamental band gap is determined.

## Reproduction target
Compute, using DFT with the GGA‑PBE functional, the following quantities for the Rb2Ti2O5 unit cell in the C2/m space group:
- The relaxed lattice parameters a, b, c (in Å) and the monoclinic angle β (in degrees).
- The enthalpy of formation (in kJ/mol) from the elemental reference phases Rb(s), Ti(s), and O2(g).
- The fundamental band gap (in eV), defined as the smallest energy difference between the valence band maximum and the conduction band minimum across the Brillouin zone.
Report these six quantities in a JSON file at /app/outputs/dft_results.json, following the exact schema specified in the output contract.

## Assets

- Quantum Espresso: https://www.quantum-espresso.org/
- Ultrasoft pseudopotentials for Rb, Ti, and O: https://pseudopotentials.quantum-espresso.org/legacy_tables/ps-library.html
- Experimental C2/m crystal structure of Rb₂Ti₂O₅

## Starting crystal structure

Initial lattice parameters (experimental, 300 K):

| Parameter | Value   |
|-----------|--------|
| a (Å)     | 11.3370 |
| b (Å)     | 3.8244  |
| c (Å)     | 6.9946  |
| β (°)     | 100.308 |

Fractional atomic coordinates (space group C2/m, two formula units):

| Atom | x      | y    | z      |
|------|--------|------|--------|
| Rb1  | 0.9851 | 0.5  | 0.8481 |
| Ti1  | 0.3525 | 0.5  | 0.5885 |
| O1   | 0.5000 | 0.5  | 0.5000 |
| O2   | 0.3762 | 0.5  | 0.8367 |
| O3   | 0.1780 | 0.5  | 0.4797 |

## Workflow steps

### Step 1: Structural relaxation of Rb₂Ti₂O₅
- Role: process
- Action: Run a variable-cell relaxation (vc-relax) of the Rb₂Ti₂O₅ unit cell (space group C2/m, two formula units) using DFT with the GGA-PBE functional. Use ultrasoft pseudopotentials for Rb, Ti, and O. Start from the experimental atomic positions and lattice parameters given in the instruction. Fully relax both lattice parameters and atomic positions. Record the final total energy and relaxed atomic coordinates.
- Evidence: `/app/outputs/relax.log`

### Step 2: Reference energies of elemental Rb, Ti, and O₂
- Role: process
- Action: Calculate the ground-state total energies of body-centered cubic Rb (solid), hexagonal close-packed Ti (solid), and the triplet O₂ molecule (in a supercell with vacuum to simulate the gas phase). Use the same DFT settings (GGA-PBE, ultrasoft pseudopotentials, appropriately converged k-point sampling and plane-wave cutoff). Obtain the per-formula-unit energies needed for the formation enthalpy.
- Evidence: `/app/outputs/ref_energies.log`

### Step 3: Kohn-Sham band structure calculation
- Role: process
- Action: Using the relaxed structure from step 1, perform a self-consistent (scf) calculation followed by a non-self-consistent (nscf) calculation along the monoclinic high-symmetry path Γ-Y-F-L-I-X-Z-Γ (appropriate for the MCL structure). Determine the valence band maximum (VBM) and conduction band minimum (CBM) from the Kohn-Sham eigenvalues, and compute the fundamental band gap as the smallest energy difference across the Brillouin zone.
- Evidence: `/app/outputs/bands.log`

### Step 4: Assemble and report final DFT results
- Role: scored (load-bearing)
- Action: Collect the relaxed lattice parameters a, b, c (in Å) and β (in degrees) from the final relaxed structure of step 1. Compute the formation enthalpy as ΔH_f = E(Rb₂Ti₂O₅) − 2·E(Rb) − 2·E(Ti) − (5/2)·E(O₂) using total energies from steps 1 and 2. Extract the fundamental band gap value (in eV) from step 3. Write these six quantities to /app/outputs/dft_results.json in the exact JSON schema specified.
- Output file: `/app/outputs/dft_results.json`
- Format: json
- Contract: {"type": "object", "properties": {"a": {"type": "number"}, "b": {"type": "number"}, "c": {"type": "number"}, "beta": {"type": "number"}, "enthalpy_formation": {"type": "number"}, "band_gap": {"type": "number"}}, "required": ["a", "b", "c", "beta", "enthalpy_formation", "band_gap"]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dft_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dft_results.json
- path: `/app/outputs/dft_results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Final DFT-GGA relaxed lattice parameters, formation enthalpy, and fundamental band gap of Rb₂Ti₂O₅. Each value is compared to the paper's reference result; meeting or exceeding the reference within tolerance earns full credit.
- schema:
  - `type`: object
  - `required`: `a`, `b`, `c`, `beta`, `enthalpy_formation`, `band_gap`
  - `properties`:
    - `a`:
      - `type`: number
      - `description`: Lattice parameter a in Å
    - `b`:
      - `type`: number
      - `description`: Lattice parameter b in Å
    - `c`:
      - `type`: number
      - `description`: Lattice parameter c in Å
    - `beta`:
      - `type`: number
      - `description`: Lattice angle β in degrees
    - `enthalpy_formation`:
      - `type`: number
      - `description`: Enthalpy of formation from elemental references in kJ/mol
    - `band_gap`:
      - `type`: number
      - `description`: Fundamental band gap in eV

Notes: The scoring uses threshold_or_better: for each quantity, the absolute deviation from the hidden reference must not exceed a tolerance; smaller deviation is better. The tolerance values and reference are hidden.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dft_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "a",
          "b",
          "c",
          "beta",
          "enthalpy_formation",
          "band_gap"
        ],
        "properties": {
          "a": {
            "type": "number",
            "description": "Lattice parameter a in Å"
          },
          "b": {
            "type": "number",
            "description": "Lattice parameter b in Å"
          },
          "c": {
            "type": "number",
            "description": "Lattice parameter c in Å"
          },
          "beta": {
            "type": "number",
            "description": "Lattice angle β in degrees"
          },
          "enthalpy_formation": {
            "type": "number",
            "description": "Enthalpy of formation from elemental references in kJ/mol"
          },
          "band_gap": {
            "type": "number",
            "description": "Fundamental band gap in eV"
          }
        }
      },
      "description": "Final DFT-GGA relaxed lattice parameters, formation enthalpy, and fundamental band gap of Rb₂Ti₂O₅. Each value is compared to the paper's reference result; meeting or exceeding the reference within tolerance earns full credit."
    }
  ],
  "notes": "The scoring uses threshold_or_better: for each quantity, the absolute deviation from the hidden reference must not exceed a tolerance; smaller deviation is better. The tolerance values and reference are hidden."
}
```

## How you are scored
A hidden verifier reads your /app/outputs/dft_results.json and independently compares each of the six values (a, b, c, beta, enthalpy_formation, band_gap) against a hidden reference. The reward for each quantity is based on how accurately your computed value matches the reference, subject to predefined tolerances. The scoring follows a monotonic policy: if your value meets or surpasses the reference (within tolerance), you receive full credit for that quantity; larger deviations result in progressively lower scores. The final reward is the weighted sum of the individual quantity scores. The exact reference and tolerances are not disclosed; you should aim to produce values that are as accurate as your DFT workflow permits.

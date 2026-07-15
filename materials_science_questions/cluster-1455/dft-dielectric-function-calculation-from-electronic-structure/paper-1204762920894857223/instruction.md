# Size-dependent shift-current in layered van der Waals ferroelectric

## Problem background
CuInP₂S₆ (CIPS) is a layered van der Waals ferroelectric that exhibits a strong bulk photovoltaic effect (BPVE). The shift-current mechanism is one contribution to BPVE, and its dependence on layer thickness is not fully understood. This task investigates how the shift-current conductivity tensor changes when going from a single monolayer up to bulk CIPS. By computing the full frequency-dependent shift-current tensor for multiple thicknesses, we can quantify the size effect and identify which tensor components dominate the response, providing insight into the design of two‑dimensional photovoltaic devices.

## Approach
The approach uses first‑principles density functional theory (DFT) and Wannier interpolation to compute the shift‑current conductivity tensor. First, crystal structures for bulk CuInP₂S₆ and for slab models with 1, 2, and 4 layers are built from the reported lattice parameters. DFT ground‑state calculations are performed with the PBEsol exchange‑correlation functional and PAW pseudopotentials to relax the structures and obtain Kohn‑Sham states. Next, maximally‑localized Wannier functions are constructed for each thickness, yielding a Wannier‑interpolated band structure that accurately reproduces the DFT bands. Finally, the shift‑current tensor is evaluated via the Wannier interpolation framework. A rigid scissor shift is applied to correct the DFT band gap, and for the slab geometries the conductivity is rescaled from the simulation box to an effective two‑dimensional conductivity to account for vacuum spacing. The complete workflow produces the shift‑current tensor components as functions of photon energy for all four thicknesses.

## Reproduction target
Compute the full set of shift‑current tensor components σ_{ikk}(ω) (in μA·V⁻²) as functions of photon energy from 0 to 6 eV for monolayer, bilayer, four‑layer, and bulk CuInP₂S₆. This requires running the DFT relaxations, Wannier construction, and shift‑current post‑processing for all thicknesses. The final output must be a single CSV file at `/app/outputs/shift_current_tensors.csv` containing one row per (thickness, component, photon energy) triplet, with columns: `thickness` (string: monolayer/bilayer/four‑layer/bulk), `component` (string: e.g., xxx, xyy, xzz, …), `energy_eV` (float), `sigma_muA_per_V2` (float). The target is to produce this CSV faithfully from the computation; the scoring is handled entirely by the hidden verifier.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Wannier90: http://www.wannier.org/
- PBEsol PAW pseudopotentials for Cu, In, P, S: https://www.quantum-espresso.org/pseudopotentials/

## Workflow steps

### Step 1: DFT relaxation and ground‑state calculations for all thicknesses
- Role: process
- Action: Build initial structures for bulk CuInP2S6 and slab models with 1, 2, and 4 layers using the reported lattice parameters. Perform DFT relaxations with Quantum ESPRESSO (PBEsol functional, PAW pseudopotentials) until forces are below 1e-3 eV/Å. Use a dense k‑point mesh, turn off Coulomb interaction in z‑direction for slabs, and add at least 20 Å vacuum. Obtain Kohn–Sham energies, wavefunctions, and ground‑state polarization for each configuration.
- Evidence: `/app/outputs/dft_relaxation.log`

### Step 2: Construction of maximally‑localized Wannier functions
- Role: process
- Action: For each thickness, use the Kohn–Sham orbitals to build maximally‑localized Wannier functions with Wannier90, producing a Wannier‑interpolated Hamiltonian that faithfully reproduces the DFT band structure in the relevant energy window.
- Evidence: `/app/outputs/wannier90_output.log`

### Step 3: Shift‑current tensor calculation
- Role: scored (load-bearing)
- Action: Using the Wannier‑interpolated band structures, compute the shift‑current conductivity tensor σ_{ikk}(ω) for every thickness (monolayer, bilayer, four‑layer, bulk) for photon energies from 0 to 6 eV. Apply a rigid scissor shift of +1.4 eV to correct the DFT band gap to the experimental gap of 2.9 eV, and rescale the conductivity from the simulation box to the 2D slab geometry with the formulas from the method (σ⁗₂D = c/t·σ⁗SB, σ′₂D = c/t·(σ′SB−1)+1, where t is the layer center‑to‑center distance times the number of layers). Export the final tensor components in μA·V⁻².
- Output file: `/app/outputs/shift_current_tensors.csv`
- Format: csv
- Contract: Columns: thickness (string: monolayer/bilayer/four‑layer/bulk), component (string: e.g., xxx, xyy, xzz, yxx, yyy, yzz, zxx, zyy, zzz), energy_eV (float), sigma_muA_per_V2 (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/shift_current_tensors.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### shift_current_tensors.csv
- path: `/app/outputs/shift_current_tensors.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: CSV containing the shift‑current tensor components. The hidden checker evaluates only structural trend compliance (shape gate and four thickness‑dependent trend checks) with specified weights; no point‑wise comparison against reference data is performed.
- schema:
  - `type`: table
  - `required_columns`: `thickness`, `component`, `energy_eV`, `sigma_muA_per_V2`
  - `units`:
    - `energy_eV`: eV
    - `sigma_muA_per_V2`: muA/V^2

Notes: Only the shift‑current tensor is scored; the integrated figure‑of‑merit and Glass coefficient are excluded as supporting analyses. All raw DFT and Wannier‑interpolation logs are required process evidence.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "shift_current_tensors.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "thickness",
          "component",
          "energy_eV",
          "sigma_muA_per_V2"
        ],
        "units": {
          "energy_eV": "eV",
          "sigma_muA_per_V2": "muA/V^2"
        }
      },
      "description": "CSV containing the shift‑current tensor components. The hidden checker evaluates only structural trend compliance (shape gate and four thickness‑dependent trend checks) with specified weights; no point‑wise comparison against reference data is performed."
    }
  ],
  "notes": "Only the shift‑current tensor is scored; the integrated figure‑of‑merit and Glass coefficient are excluded as supporting analyses. All raw DFT and Wannier‑interpolation logs are required process evidence."
}
```

## How you are scored
Your submission is scored by an automated hidden verifier. The verifier performs only structural trend checks on your shift‑current curves; there is no point‑wise comparison against reference data. The verifier first applies a shape gate (weight 0.05) to verify that the overall spectral shapes are plausible. Then it checks four specific thickness‑dependent trends (weights 0.20, 0.25, 0.25, 0.25) that correspond to the qualitative physics reported in the paper (e.g., vanishing out‑of‑plane component for thin layers, enhancement of certain components with thickness, oscillatory behavior, and sign relationships). The final score is the sum of these weighted components. Only the hidden verifier determines the score.

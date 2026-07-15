# DFT Adsorption on Catalyst Surfaces

## Problem background
Piezocatalytic intermediate water splitting harnesses mechanical energy to simultaneously produce hydrogen (H₂) and hydrogen peroxide (H₂O₂) from water, offering a sustainable route for chemical synthesis and environmental remediation. Sodium niobate (NaNbO₃) is a promising piezoelectric catalyst, and doping with vanadium (V) has been explored to enhance its performance. Density functional theory (DFT) calculations can provide atomic-scale insight into how V doping alters the water dissociation kinetics and the free energy landscape for H₂ evolution and H₂O₂ formation. This task aims to quantify those effects by computing the relevant energy barriers and thermodynamic free energy changes on model catalyst surfaces.

## Approach
The computational study employs first-principles DFT with the Perdew–Burke–Ernzerhof (PBE) functional. Two surface models are built: a pristine NbO₂‑terminated NaNbO₃ (001) slab and a V‑doped analogue where one surface Nb atom is replaced by V, both under an external compressive stress. After relaxing the slabs, the adsorption energies of H*, OH* and H₂O* intermediates are computed. The reaction barrier for water dissociation (H₂O → OH + H) is obtained via the nudged elastic band (NEB) method. The adsorption energies are then converted to Gibbs free energies at 298 K using zero‑point energy and entropy corrections, yielding ΔG for the two‑electron steps that produce H₂ and H₂O₂. Comparing the barrier and free energies between pristine and V‑doped surfaces allows one to evaluate the role of doping.

## Reproduction target
Using a DFT implementation with the PBE functional, compute and report the water dissociation barrier (Eₐ, in eV) and the Gibbs free energy changes (ΔG, in eV) for the two‑electron steps leading to H₂ evolution and H₂O₂ formation on both the stressed pristine NaNbO₃(001) and V‑doped NaNbO₃(001) surfaces. Write the four values to a CSV file: `/app/outputs/dft_results.csv` with columns `system` (values `NaNbO3` and `V-NaNbO3`), `E_a`, `ΔG_H2`, and `ΔG_H2O₂`.

## Assets

- NaNbO3 crystal structure (orthorhombic, JCPDS 82-0606): JCPDS No. 82-0606
- DFT code with PBE pseudopotentials

## Workflow steps

### Step 1: Bulk DFT relaxation of NaNbO3 and V-NaNbO3
- Role: process
- Action: Optimize the lattice parameters of bulk orthorhombic NaNbO3 and a V-doped supercell (one Nb replaced by V) using DFT with the PBE functional to obtain equilibrium a, b, c.
- Evidence: none

### Step 2: Stressed surface slab relaxation
- Role: process
- Action: Construct 5-layer NbO2-terminated (001) slabs for pristine NaNbO3 and V-doped NaNbO3. Apply compressive stress of ~1 GPa by reducing the c-axis lattice parameter to 15.427 Å. Fix bottom two layers, relax top three layers. For the V-doped slab, substitute one surficial Nb with V.
- Evidence: none

### Step 3: Adsorbate total energy calculations
- Role: process
- Action: Place H, OH, and H2O adsorbates on the relaxed surfaces and compute total energies for each configuration. Calculate adsorption energies ΔE_M = E(M/slab) − E(slab) − E(M).
- Evidence: none

### Step 4: Water dissociation barrier (NEB)
- Role: process
- Action: Use the nudged elastic band (NEB) method to find the minimum energy path for water dissociation (H2O → OH + H) on both stressed surfaces, and determine the activation barrier E_a.
- Evidence: none

### Step 5: Gibbs free energy analysis and final result
- Role: scored (load-bearing)
- Action: Convert the adsorption energies and barrier to Gibbs free energies at 298 K using zero-point energy and entropy corrections (from DFT vibrational calculations). Compute ΔG_H2 = ΔG(H*) − ½ G(H2,g) and ΔG_H2O2 = ΔG(OH*) − G(H2O,g) + ½ G(H2,g) for both pristine NaNbO3 and V-doped NaNbO3 surfaces. Write all four values as dft_results.csv.
- Output file: `/app/outputs/dft_results.csv`
- Format: csv
- Contract: CSV with columns: system (string, values NaNbO3 or V-NaNbO3), E_a (float, eV), ΔG_H2 (float, eV), ΔG_H2O2 (float, eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dft_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dft_results.csv
- path: `/app/outputs/dft_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: DFT-computed water dissociation barrier and Gibbs free energy changes for H₂ and H₂O₂ evolution on pristine NaNbO₃ and V-doped NaNbO₃ surfaces.
- schema:
  - `type`: table
  - `required_columns`: `system`, `E_a`, `ΔG_H2`, `ΔG_H2O2`
  - `units`:
    - `E_a`: eV
    - `ΔG_H2`: eV
    - `ΔG_H2O2`: eV

Notes: The hidden checker will compare the reported values to the paper's reported gold numbers with appropriate tolerances. The agent must compute all required values from scratch using a DFT implementation with the PBE functional.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dft_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "E_a",
          "ΔG_H2",
          "ΔG_H2O2"
        ],
        "units": {
          "E_a": "eV",
          "ΔG_H2": "eV",
          "ΔG_H2O2": "eV"
        }
      },
      "description": "DFT-computed water dissociation barrier and Gibbs free energy changes for H₂ and H₂O₂ evolution on pristine NaNbO₃ and V-doped NaNbO₃ surfaces."
    }
  ],
  "notes": "The hidden checker will compare the reported values to the paper's reported gold numbers with appropriate tolerances. The agent must compute all required values from scratch using a DFT implementation with the PBE functional."
}
```

## How you are scored
A hidden verifier reads your `dft_results.csv` and compares each reported value (Eₐ, ΔG_H₂, ΔG_H₂O₂ for both systems) against reference numbers derived from the original DFT study. Scoring is based on absolute deviation: full credit is given when a value is within a preset tolerance; partial credit is awarded for deviations beyond the tolerance up to a maximum, after which no credit is earned. The reward is monotonic—obtaining a result that lies within the tolerance always earns full credit. The tolerances account for legitimate implementation‑dependent variations, so performing the DFT workflow as described is required to achieve a high score; a random guess is extremely unlikely to land within the scoring window.

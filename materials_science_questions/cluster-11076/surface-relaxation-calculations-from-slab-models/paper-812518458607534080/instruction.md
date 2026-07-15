# Electronic and thermodynamic properties of AgNiF3 (001) surfaces

## Problem background
Fluoroperovskite AgNiF₃ is a semiconductor with potential applications in solar cells, spintronics, and optical coatings. In thin-film device technologies, the (001) surface is particularly important because its terminations critically influence the electronic, magnetic, and thermodynamic properties. Two distinct terminations — AgF and NiF — can be created by cleaving the bulk crystal along the (001) plane. A systematic first-principles investigation of the structural stability, electronic band structure, magnetism, and electronic specific heat of these surfaces provides essential insight for device design and is the focus of this reproduction. Your goal is to compute these properties from scratch using density functional theory and Boltzmann transport theory for both terminations.

## Approach
The reproduction follows a spin‑polarized density functional theory (DFT) workflow. You will start from the bulk cubic perovskite structure of AgNiF₃ (space group Pm‑3m, lattice constant ~4.03 Å) and build seven‑layer symmetric (001) slabs terminated by either AgF or NiF, separated by a 50% vacuum region to suppress spurious interactions between periodic images. The central layer of each slab is kept fixed while the remaining atomic coordinates are relaxed using the PBE‑GGA exchange‑correlation functional until forces are well converged. On the relaxed geometries, a self‑consistent field calculation yields the converged charge density, Kohn–Sham eigenvalues, and spin‑polarized magnetic moments. Band structures are then computed along high‑symmetry directions, with particular attention to the indirect M–Γ gap. Finally, a non‑self‑consistent calculation on a dense k‑mesh provides the eigenvalues that serve as input to a Boltzmann transport code (BoltzTraP), which computes the electronic specific heat as a function of temperature; the value at 300 K is extracted for each termination. All DFT steps are performed with an open‑source plane‑wave code (e.g., Quantum ESPRESSO) and standard pseudopotentials for Ag, Ni, and F.

## Reproduction target
For both the AgF‑terminated and NiF‑terminated AgNiF₃ (001) surfaces, compute:

- the indirect (M–Γ) band gap (in eV),
- the total magnetic moment (in μB),
- the electronic specific heat at T = 300 K (in J/K·mol).

Assemble these six numbers into a single file `/app/outputs/results.json` with the following keys: `AgF_band_gap`, `NiF_band_gap`, `AgF_total_magnetic_moment`, `NiF_total_magnetic_moment`, `AgF_electronic_specific_heat_300K`, `NiF_electronic_specific_heat_300K`. All values must be floats.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotential library: https://www.materialscloud.org/discover/sssp/
- BoltzTraP: https://www.icmab.es/boltz/trap/
- Bulk AgNiF3 cubic perovskite structure

## Workflow steps

### Step 1: Construct slab models
- Role: process
- Action: Build seven-layer symmetric AgNiF3 (001) slab models with AgF and NiF terminations, including a 50% vacuum region, using the cubic Pm-3m bulk structure.
- Evidence: `/app/outputs/initial_slabs.tar.gz`

### Step 2: Geometry relaxation
- Role: process
- Action: Perform spin-polarized DFT geometry optimization for both terminations using an open-source plane-wave DFT code with GGA-PBE functional until atomic forces converge below a suitable threshold. Keep the central layer fixed.
- Evidence: `/app/outputs/relaxed_structures.tar.gz`

### Step 3: Self-consistent field and magnetic moment calculation
- Role: process
- Action: Run a self-consistent field calculation on the relaxed slabs to obtain converged charge density, Kohn–Sham eigenvalues, and spin-polarized total magnetic moments. Use a sufficiently dense k‑mesh for surface calculations.
- Evidence: `/app/outputs/scf_outputs.tar.gz`

### Step 4: Band structure calculation
- Role: process
- Action: Compute the spin-polarized band structure along the high‑symmetry path including M–Γ, and extract the indirect band gap value for each termination from the eigenvalues.
- Evidence: `/app/outputs/bands_outputs.tar.gz`

### Step 5: Electronic specific heat via BoltzTraP
- Role: process
- Action: Perform a non‑self‑consistent band structure calculation on a dense k‑mesh and use BoltzTraP (or equivalent) to compute electronic specific heat as a function of temperature. Extract the value at T = 300 K for each termination.
- Evidence: `/app/outputs/boltztrap_results.tar.gz`

### Step 6: Compile final results
- Role: scored
- Action: Assemble the computed indirect band gaps, total magnetic moments, and electronic specific heat at 300 K for both AgF and NiF terminations into a single JSON file.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"AgF_band_gap": "float in eV", "NiF_band_gap": "float in eV", "AgF_total_magnetic_moment": "float in μB", "NiF_total_magnetic_moment": "float in μB", "AgF_electronic_specific_heat_300K": "float in J/K.mol", "NiF_electronic_specific_heat_300K": "float in J/K.mol"}
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
- description: Aggregated results from DFT and BoltzTraP calculations: indirect M–Γ band gaps, total magnetic moments, and electronic specific heat at 300 K for both AgF and NiF terminations. The checker compares these reported values against hidden reference values using pre‑defined tolerances.
- schema:
  - `type`: object
  - `required`:
    - `AgF_band_gap`: float (eV)
    - `NiF_band_gap`: float (eV)
    - `AgF_total_magnetic_moment`: float (μB)
    - `NiF_total_magnetic_moment`: float (μB)
    - `AgF_electronic_specific_heat_300K`: float (J/K·mol)
    - `NiF_electronic_specific_heat_300K`: float (J/K·mol)
  - `items`: object
  - `required_columns`:
  - `units`: object

Notes: The hidden checker validates that all six fields are present and each value falls within the allowed absolute tolerance of the paper‑reported benchmark. No intermediate raw data is evaluated; only this final aggregate is scored.

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
          "AgF_band_gap": "float (eV)",
          "NiF_band_gap": "float (eV)",
          "AgF_total_magnetic_moment": "float (μB)",
          "NiF_total_magnetic_moment": "float (μB)",
          "AgF_electronic_specific_heat_300K": "float (J/K·mol)",
          "NiF_electronic_specific_heat_300K": "float (J/K·mol)"
        },
        "items": {},
        "required_columns": [],
        "units": {}
      },
      "description": "Aggregated results from DFT and BoltzTraP calculations: indirect M–Γ band gaps, total magnetic moments, and electronic specific heat at 300 K for both AgF and NiF terminations. The checker compares these reported values against hidden reference values using pre‑defined tolerances."
    }
  ],
  "notes": "The hidden checker validates that all six fields are present and each value falls within the allowed absolute tolerance of the paper‑reported benchmark. No intermediate raw data is evaluated; only this final aggregate is scored."
}
```

## How you are scored
Your submission is scored by a hidden verifier that inspects only `/app/outputs/results.json`. The verifier compares each of the six reported numeric values against reference values that are not disclosed, using pre‑defined absolute tolerances that account for systematic differences between all‑electron and pseudopotential‑based DFT codes. Full credit is awarded when all six values fall within tolerance; partial credit is proportional to the number of passing fields. The verifier also requires the JSON file to be present and correctly structured with all six keys; a missing or malformed file receives zero credit. Compute every value from your own DFT+transport pipeline — do not attempt to guess or copy numbers.

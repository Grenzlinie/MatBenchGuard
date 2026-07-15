# Electronic Structure and Optoelectronic Properties of Hybrid Double Perovskites

## Problem background
Organic-inorganic hybrid double perovskites are emerging as lead-free candidates for optoelectronic technologies due to their tunable electronic structure and potential stability. In this task, three hybrid compounds with the formula (CsMA)NaBiX6 (MA = methylammonium, X = Cl, Br, I) are investigated. The goal is to compute, using first-principles density functional theory, the electronic band gaps, the nature of the band edges, the optical constants of the iodide variant, and the formation energies of all three materials. These quantities shed light on the suitability of such perovskites for applications like light-emitting diodes or photovoltaics.

## Approach
The computational strategy employs plane-wave pseudopotential density functional theory within the local density approximation (LDA-PBE). Initial crystal structures are constructed from the well-known double perovskite prototype with appropriate ionic placements. For each compound, the lattice and atomic positions are first relaxed to obtain the ground-state geometry and total energy. Electronic band structures are then calculated along a high-symmetry path of the cubic Brillouin zone, yielding the band gap energy and the high-symmetry points of the conduction band minimum and valence band maximum. For (CsMA)NaBiI6, the frequency-dependent dielectric function, absorption coefficient, and refractive index are derived from the Kohn–Sham eigenvalues and transition matrix elements; key scalar optical constants are extracted from these spectra. Formation energies are evaluated from the total energies of the compounds relative to the total energies computed for the isolated constituent atoms and the methylammonium molecule under the same functional and pseudopotential conditions. The open-source Quantum ESPRESSO code (or an equivalent plane-wave code) and the SSSP library of ultrasoft pseudopotentials are used for all calculations.

## Reproduction target
For each of the three compounds — (CsMA)NaBiCl6, (CsMA)NaBiBr6, and (CsMA)NaBiI6 — compute and report: the band gap energy in eV, the gap type (direct or indirect), the k-point labels of the conduction band minimum and valence band maximum, and the formation energy in kJ/mol. Additionally, for (CsMA)NaBiI6 only, report the static (zero-frequency) dielectric constant, the maximum refractive index in the visible or near‑UV photon energy range, and the order of magnitude of the peak absorption coefficient (expressed as a string such as "10^5" or "10^6"). Collect all results into a single JSON file, `/app/outputs/results.json`, structured as an object with a key `compounds` whose value is an array of compound objects, each containing the fields `name`, `band_gap_eV`, `gap_type`, `cbm_kpoint`, `vbm_kpoint`, `formation_energy_kJ_per_mol`, and (for the iodide compound) the additional fields `dielectric_constant_zero_freq`, `max_refractive_index`, and `absorption_coefficient_order`.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotential library (ultrasoft, LDA-PBE): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Construct initial crystal structures
- Role: process
- Action: Build initial cubic double perovskite structures for (CsMA)NaBiCl6, (CsMA)NaBiBr6, and (CsMA)NaBiI6 using the known double perovskite prototype and atomic positions (Cs, MA, Na, Bi, halide). Save the initial structures in a suitable format.
- Evidence: `/app/outputs/initial_structures.txt`

### Step 2: DFT geometry optimization
- Role: process
- Action: For each compound, perform structural relaxation using DFT with the LDA-PBE exchange-correlation functional and ultrasoft pseudopotentials. Minimize until forces on atoms and stress on the cell are converged. Save the optimized lattice parameters and total energies.
- Evidence: `/app/outputs/optimization_results.json`

### Step 3: Electronic band structure calculation
- Role: process
- Action: For each optimized compound, compute the Kohn-Sham eigenvalues along a standard high-symmetry path of the cubic Brillouin zone. Save the eigenvalues and k-point coordinates to allow extraction of band gap energy and band-edge k-point locations.
- Evidence: `/app/outputs/band_eigenvalues.json`

### Step 4: Optical properties calculation (for (CsMA)NaBiI6)
- Role: process
- Action: For (CsMA)NaBiI6, compute the frequency-dependent dielectric function, absorption coefficient, and refractive index using the DFT eigenvalues and transition matrix elements. Extract the static (zero-frequency) dielectric constant, the maximum refractive index in the visible range, and the order of magnitude of the peak absorption coefficient. Save these extracted constants.
- Evidence: `/app/outputs/optical_extracted.json`

### Step 5: Formation energy calculation
- Role: process
- Action: Calculate formation energies for all three compounds using total energies from the optimized structures and reference energies of the constituent atoms/molecule (Cs, MA, Na, Bi, halides). Obtain the reference energies by running DFT calculations on the isolated atoms/molecule under the same functional and pseudopotential conditions. Save the formation energies.
- Evidence: `/app/outputs/formation_energies.json`

### Step 6: Compile and report final numerical results
- Role: scored (load-bearing)
- Action: Gather all computed quantities: for each of (CsMA)NaBiCl6, (CsMA)NaBiBr6, and (CsMA)NaBiI6, report the band gap energy (eV), gap type, CBM and VBM k-point labels, and formation energy (kJ/mol). Additionally for (CsMA)NaBiI6, report the static dielectric constant, maximum refractive index, and the absorption coefficient order of magnitude (e.g. "10^6"). Write the data as a JSON object with a `compounds` array into results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: { "compounds": [ { "name": "string", "band_gap_eV": number, "gap_type": "string", "cbm_kpoint": "string", "vbm_kpoint": "string", "formation_energy_kJ_per_mol": number, (for (CsMA)NaBiI6 only) "dielectric_constant_zero_freq": number, "max_refractive_index": number, "absorption_coefficient_order": "string" } ] }
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
- description: JSON file containing the final reproduced band gaps, k-point locations, formation energies, and (for the I compound) optical constants for all three hybrid double perovskites.
- schema:
  - `type`: object
  - `required`: `compounds`
  - `properties`:
    - `compounds`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `name`, `band_gap_eV`, `gap_type`, `cbm_kpoint`, `vbm_kpoint`, `formation_energy_kJ_per_mol`
        - `properties`:
          - `name`:
            - `type`: string
          - `band_gap_eV`:
            - `type`: number
          - `gap_type`:
            - `type`: string
          - `cbm_kpoint`:
            - `type`: string
          - `vbm_kpoint`:
            - `type`: string
          - `formation_energy_kJ_per_mol`:
            - `type`: number
          - `dielectric_constant_zero_freq`:
            - `type`: number
          - `max_refractive_index`:
            - `type`: number
          - `absorption_coefficient_order`:
            - `type`: string

Notes: The checker compares each reported value to paper-reported numbers with appropriate tolerances and exact match for string labels. All intermediate process steps are required to produce this artifact.

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
        "required": [
          "compounds"
        ],
        "properties": {
          "compounds": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "name",
                "band_gap_eV",
                "gap_type",
                "cbm_kpoint",
                "vbm_kpoint",
                "formation_energy_kJ_per_mol"
              ],
              "properties": {
                "name": {
                  "type": "string"
                },
                "band_gap_eV": {
                  "type": "number"
                },
                "gap_type": {
                  "type": "string"
                },
                "cbm_kpoint": {
                  "type": "string"
                },
                "vbm_kpoint": {
                  "type": "string"
                },
                "formation_energy_kJ_per_mol": {
                  "type": "number"
                },
                "dielectric_constant_zero_freq": {
                  "type": "number"
                },
                "max_refractive_index": {
                  "type": "number"
                },
                "absorption_coefficient_order": {
                  "type": "string"
                }
              }
            }
          }
        }
      },
      "description": "JSON file containing the final reproduced band gaps, k-point locations, formation energies, and (for the I compound) optical constants for all three hybrid double perovskites."
    }
  ],
  "notes": "The checker compares each reported value to paper-reported numbers with appropriate tolerances and exact match for string labels. All intermediate process steps are required to produce this artifact."
}
```

## How you are scored
After you submit your results, an automated verifier inspects `/app/outputs/results.json`. For each compound, every numeric field is compared against a hidden reference; the closer your value, the higher the score. String fields (gap type, k-point labels, absorption order) must match the reference exactly to earn full credit. The verifier combines the scores from all fields, with each field contributing a weighted share, to produce a final reward between 0 and 1. Only the contents of `results.json` are scored; intermediate artifacts are required to reach the final answer but do not directly earn points. The reference values are not disclosed, so the most reliable route to a high score is to faithfully execute the full workflow: construct the structures, perform geometry optimization, band structure, optical, and formation energy calculations, and then compile the results accurately.

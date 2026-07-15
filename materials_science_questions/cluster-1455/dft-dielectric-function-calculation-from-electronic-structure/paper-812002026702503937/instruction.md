# DFT Electronic Structure and Dielectric Function of Alkali Metal Carbonates

## Problem background
Alkali metal carbonates (Li₂CO₃, Na₂CO₃, K₂CO₃, LiKCO₃) are candidate materials for optics and energy storage, but their electronic structure, band gaps, and optical response are not fully characterized. This task uses density-functional theory (DFT) to compute the band structure, density of states, and dielectric function of these compounds, examining how the cation species affects the electronic and optical properties.

## Approach
Perform periodic DFT calculations within the pseudopotential framework, using a suitable exchange‑correlation functional (e.g., LDA or GGA) and a plane‑wave or numerical atomic‑orbital basis set. Start from the published crystal structures of the four compounds. After converging the self‑consistent ground state, compute the electronic band structure along high‑symmetry lines and the total density of states. From these results, extract the widths of the distinct valence‑band bundles and the fundamental band gap. Finally, calculate the imaginary part of the dielectric function ε₂(E) using momentum‑matrix‑elements or an equivalent post‑processing method. The procedure mirrors a typical ab‑initio electronic‑structure workflow for insulators.

## Reproduction target
Using DFT, compute the valence‑band bundle widths (labels I, II, V) and the fundamental band gap for Li₂CO₃ and Na₂CO₃. Write these band properties to `band_properties.json`. Compute the imaginary part of the dielectric function ε₂(E) for Li₂CO₃, Na₂CO₃, K₂CO₃, and LiKCO₃ over 0–20 eV with a step no larger than 0.1 eV, and save the spectra as `dielectric_function_eps2.csv`. The required output formats and schemas are defined in the workflow steps and output contract.

## Assets

- Crystal structures of Li₂CO₃, Na₂CO₃, K₂CO₃, LiKCO₃
- SIESTA (or equivalent open-source DFT code): https://departments.icmab.es/leem/siesta/
- Pseudopotential files for Li, Na, K, C, O: http://www.pseudo-dojo.org

## Workflow steps

### Step 1: Retrieve crystal structures
- Role: process
- Action: Obtain crystallographic data (atomic coordinates and lattice parameters) for Li₂CO₃, Na₂CO₃, K₂CO₃, and LiKCO₃ from published literature or open databases.
- Evidence: none

### Step 2: DFT ground‑state calculation
- Role: process
- Action: Perform self‑consistent DFT calculations for each compound using an appropriate exchange‑correlation functional (e.g., LDA) and a plane‑wave or numerical atomic‑orbital basis. Produce converged charge density and Kohn‑Sham eigenstates.
- Evidence: none

### Step 3: Band structure and density of states
- Role: process
- Action: Compute the electronic band structure along high‑symmetry directions and the total density of states N(E) using symmetrized Fourier interpolation or equivalent post‑processing.
- Evidence: none

### Step 4: Extract quantitative band properties
- Role: scored (load-bearing)
- Action: From the band structure and DOS, determine the widths of valence‑band bundles I, II, and V, and the fundamental band gaps for Li₂CO₃ and Na₂CO₃. Write the results to band_properties.json.
- Output file: `/app/outputs/band_properties.json`
- Format: json
- Contract: Object with keys for each compound: Li2CO3, Na2CO3, K2CO3, LiKCO3. Each value is an object with fields: band_I_width_eV (number), band_II_width_eV (number), band_V_width_eV (number, optional), band_gap_eV (number).
- Scoring: scored by hidden verifier

### Step 5: Optical function calculation
- Role: scored
- Action: Compute the imaginary part of the dielectric function ε₂(E) for all four compounds using momentum matrix elements or an equivalent method. Output a CSV file with energy and ε₂ columns.
- Output file: `/app/outputs/dielectric_function_eps2.csv`
- Format: csv
- Contract: Table with columns: Energy_eV, eps2_Li2CO3, eps2_Na2CO3, eps2_K2CO3, eps2_LiKCO3. Energy in eV, step ≤0.1 eV covering 0‑20 eV. Missing entries may be filled with 0.0.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_properties.json`
- `/app/outputs/dielectric_function_eps2.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_properties.json
- path: `/app/outputs/band_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed valence band widths and fundamental band gaps for Li₂CO₃ and Na₂CO₃. Tolerances allow for basis‑set and functional differences.
- schema:
  - `type`: object
  - `required`:
    - `Li2CO3`: object
    - `Na2CO3`: object
  - `items`:
    - `band_I_width_eV`: number
    - `band_II_width_eV`: number
    - `band_V_width_eV`: number
    - `band_gap_eV`: number
  - `units`:
    - `band_I_width_eV`: eV
    - `band_II_width_eV`: eV
    - `band_V_width_eV`: eV
    - `band_gap_eV`: eV

### dielectric_function_eps2.csv
- path: `/app/outputs/dielectric_function_eps2.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Imaginary part of the dielectric function ε₂(E) for all four compounds. Peak positions and relative intensities are compared to paper‑reported values.
- schema:
  - `type`: table
  - `required_columns`: `Energy_eV`, `eps2_Li2CO3`, `eps2_Na2CO3`, `eps2_K2CO3`, `eps2_LiKCO3`
  - `units`:
    - `Energy_eV`: eV
    - `eps2_*`: arbitrary units

Notes: The scoring of band properties compares the agent's computed values for Li₂CO₃ and Na₂CO₃ to the paper‑reported values with tolerances of 0.1 eV for widths and 0.3 eV for gaps. The dielectric function scoring extracts local maxima from the CSV and compares them to paper‑reported peaks (tolerance 0.5 eV), also checking relative intensity ordering. The agent may use any open‑source DFT engine and pseudopotential set; the results should be within these tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "Li2CO3": "object",
          "Na2CO3": "object"
        },
        "items": {
          "band_I_width_eV": "number",
          "band_II_width_eV": "number",
          "band_V_width_eV": "number",
          "band_gap_eV": "number"
        },
        "units": {
          "band_I_width_eV": "eV",
          "band_II_width_eV": "eV",
          "band_V_width_eV": "eV",
          "band_gap_eV": "eV"
        }
      },
      "description": "Computed valence band widths and fundamental band gaps for Li₂CO₃ and Na₂CO₃. Tolerances allow for basis‑set and functional differences."
    },
    {
      "file": "dielectric_function_eps2.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Energy_eV",
          "eps2_Li2CO3",
          "eps2_Na2CO3",
          "eps2_K2CO3",
          "eps2_LiKCO3"
        ],
        "units": {
          "Energy_eV": "eV",
          "eps2_*": "arbitrary units"
        }
      },
      "description": "Imaginary part of the dielectric function ε₂(E) for all four compounds. Peak positions and relative intensities are compared to paper‑reported values."
    }
  ],
  "notes": "The scoring of band properties compares the agent's computed values for Li₂CO₃ and Na₂CO₃ to the paper‑reported values with tolerances of 0.1 eV for widths and 0.3 eV for gaps. The dielectric function scoring extracts local maxima from the CSV and compares them to paper‑reported peaks (tolerance 0.5 eV), also checking relative intensity ordering. The agent may use any open‑source DFT engine and pseudopotential set; the results should be within these tolerances."
}
```

## How you are scored
A hidden verifier inspects the artifacts you submit under `/app/outputs`. It reads your `band_properties.json` and compares the reported band widths and band gaps for Li₂CO₃ and Na₂CO₃ to reference values; it also reads `dielectric_function_eps2.csv`, extracts the peak positions of the ε₂ spectra, and checks them against expected peak locations and relative intensity orderings. The overall score is a weighted combination of the results from these two scored stages. Simply reproducing exact literature numbers is not sufficient; the verifier evaluates whether the computed electronic structure and optical functions are physically consistent with the underlying crystal structures and the DFT methodology you applied.

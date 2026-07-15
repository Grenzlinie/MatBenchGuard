# TiO₂ Nanotube Strain Energy and S-Doped Band Structure Assessment

## Problem background
Titanium dioxide (TiO₂) in the anatase phase is a promising photocatalyst for water splitting because of its chemical stability, non-toxicity, and suitable band-edge positions relative to the water redox potentials. However, its wide band gap (~3.2 eV for the bulk) limits sunlight absorption to the ultraviolet region, which is only a small fraction of the solar spectrum. Nanotubular morphologies can improve surface area and crystallinity, while doping with elements such as sulphur may introduce mid-gap states and narrow the effective band gap, potentially enabling visible-light-driven hydrogen generation. This computational study investigates the energetic stability of single-walled anatase TiO₂ nanotubes of different morphologies and wall thicknesses, and then evaluates the electronic structure of sulphur-doped nanotubes to assess their suitability as visible-light photocatalysts.

## Approach
The approach uses first-principles density functional theory (DFT) with a hybrid exchange-correlation functional. First, the functional is calibrated against the experimental band gap of bulk anatase TiO₂ by adjusting the fraction of Hartree-Fock exchange. Using the calibrated setup, a 9-layered anatase (001) nanosheet is constructed from the bulk structure and then rolled into (0,n) single-walled nanotubes of various diameters. Total energies of the nanosheet and each nanotube are computed, and the strain energy (energy difference per formula unit) is evaluated as a function of diameter to determine the thermodynamic stability of the tubular form relative to the flat sheet. Then, one oxygen atom in the most stable nanotube diameter range is replaced by sulphur at an outer surface site, and a DFT electronic structure calculation yields the band gap and the absolute energies of the valence band maximum and conduction band minimum. These are converted to the standard hydrogen electrode (SHE) scale to check how the band edges align with the water redox potentials.

## Reproduction target
For the 9-layered anatase (001) (0,n) nanotube, compute the strain energy per formula unit as a function of nanotube diameter and save the data (CSV). Then, for an S-doped nanotube with a diameter close to 3.5 nm (substitution at an outer surface oxygen site), compute the electronic band gap and the conduction and valence band edge energies relative to the standard hydrogen electrode (SHE, defined as -4.44 eV vs. vacuum level) and save them (JSON). The required output files are described in the workflow steps.

## Assets

- CP2K: https://www.cp2k.org/download
- Anatase TiO2 bulk structure (mp-390): https://materialsproject.org/materials/mp-390

## Workflow steps

### Step 1: Calibrate hybrid functional for anatase TiO2
- Role: process
- Action: Calibrate a hybrid DFT functional by adjusting the Hartree-Fock exchange fraction to reproduce the experimental band gap of bulk anatase (~3.18 eV) using a consistent computational setup (basis set/pseudopotential). This step is required to ensure accurate electronic structure description for subsequent nanotube calculations.
- Evidence: `/app/outputs/calibration_log.txt`

### Step 2: Generate nanosheet and nanotube atomic models
- Role: process
- Action: Construct the 9-layered anatase (001) nanosheet from the bulk anatase structure. Roll the nanosheet into (0,n) single-walled nanotubes with diameters ranging from approximately 2.5 to 4.0 nm. Prepare input structures for subsequent DFT calculations.
- Evidence: `/app/outputs/structure_files`

### Step 3: Compute total energies of nanosheet and nanotubes
- Role: process
- Action: Run DFT single-point energy calculations for the flat nanosheet and each nanotube model using the calibrated hybrid functional with a consistent basis set and k-point sampling.
- Evidence: `/app/outputs/energy_outputs`

### Step 4: Compute strain energy and write results
- Role: scored (load-bearing)
- Action: Calculate the strain energy (E_nanotube - E_nanosheet) per formula unit for each nanotube diameter. Write the data to a CSV file with columns diameter_nm (float) and strain_energy_eV_per_formula_unit (float). Include at least three data points covering diameters from 2.5 to 4.0 nm.
- Output file: `/app/outputs/strain_energy_001_0n.csv`
- Format: csv
- Contract: CSV with columns: diameter_nm (float), strain_energy_eV_per_formula_unit (float)
- Scoring: scored by hidden verifier

### Step 5: S-doped nanotube DFT band structure calculation
- Role: process
- Action: Construct an S-doped nanotube model by substituting one oxygen atom at an outer surface site on a (0,n) nanotube with a diameter close to 3.5 nm. Run a DFT electronic structure calculation to obtain the band gap (eV) and the absolute energies of the valence band maximum and conduction band minimum (eV, relative to vacuum).
- Evidence: `/app/outputs/doped_band_output`

### Step 6: Report band structure of S-doped nanotube
- Role: scored
- Action: Convert the computed band edge energies to the standard hydrogen electrode (SHE) scale using E_vs_SHE = E_vacuum + 4.44 eV. Write a JSON file with keys: band_gap_eV (float), valence_band_edge_vs_SHE (float, in eV), conduction_band_edge_vs_SHE (float, in eV).
- Output file: `/app/outputs/band_structure_s_doped.json`
- Format: json
- Contract: JSON object with keys: band_gap_eV (float), valence_band_edge_vs_SHE (float, eV), conduction_band_edge_vs_SHE (float, eV)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/strain_energy_001_0n.csv`
- `/app/outputs/band_structure_s_doped.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### strain_energy_001_0n.csv
- path: `/app/outputs/strain_energy_001_0n.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Computed strain energy vs. diameter for the 9-layered anatase (001) (0,n) nanotube. The checker verifies that the strain energy indicates thermodynamic stability.
- schema:
  - `type`: table
  - `required_columns`: `diameter_nm`, `strain_energy_eV_per_formula_unit`
  - `units`:
    - `diameter_nm`: nm
    - `strain_energy_eV_per_formula_unit`: eV per formula unit

### band_structure_s_doped.json
- path: `/app/outputs/band_structure_s_doped.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Band gap and band edge positions of the S-doped nanotube on the SHE scale. The checker verifies that the band edges satisfy photocatalytic water-splitting criteria.
- schema:
  - `type`: object
  - `required`:
    - `band_gap_eV`: number
    - `valence_band_edge_vs_SHE`: number
    - `conduction_band_edge_vs_SHE`: number
  - `units`:
    - `band_gap_eV`: eV
    - `valence_band_edge_vs_SHE`: eV
    - `conduction_band_edge_vs_SHE`: eV

Notes: All structural audits are performed with predetermined tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "strain_energy_001_0n.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "diameter_nm",
          "strain_energy_eV_per_formula_unit"
        ],
        "units": {
          "diameter_nm": "nm",
          "strain_energy_eV_per_formula_unit": "eV per formula unit"
        }
      },
      "description": "Computed strain energy vs. diameter for the 9-layered anatase (001) (0,n) nanotube. The checker verifies that the strain energy indicates thermodynamic stability."
    },
    {
      "file": "band_structure_s_doped.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "band_gap_eV": "number",
          "valence_band_edge_vs_SHE": "number",
          "conduction_band_edge_vs_SHE": "number"
        },
        "units": {
          "band_gap_eV": "eV",
          "valence_band_edge_vs_SHE": "eV",
          "conduction_band_edge_vs_SHE": "eV"
        }
      },
      "description": "Band gap and band edge positions of the S-doped nanotube on the SHE scale. The checker verifies that the band edges satisfy photocatalytic water-splitting criteria."
    }
  ],
  "notes": "All structural audits are performed with predetermined tolerances."
}
```

## How you are scored
A hidden verifier independently examines each of your output artifacts. For the strain energy data file, it checks whether the computed strain energy shows the expected behaviour (e.g., sign and magnitude) for diameters near the target region. For the band structure file, it verifies that the reported band gap and band-edge positions meet physically motivated criteria. Each scored artifact contributes to a combined reward; you must produce the required files by executing the described computational workflow — simply writing numbers from the literature is not sufficient and will not receive credit.

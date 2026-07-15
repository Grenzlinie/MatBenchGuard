# DFT Analysis of CO₂ Adsorption and Electronic Structure on Chalcogen-Modified Cu(111) Surfaces

## Problem background
Electrochemical CO₂ reduction over copper catalysts represents a promising route for sustainable fuel and chemical production, but unmodified copper surfaces typically yield a broad product distribution with limited selectivity. Experimental studies have demonstrated that introducing chalcogen adatoms (sulfur, selenium, tellurium) onto copper significantly shifts the selectivity toward formate while suppressing the competing hydrogen evolution reaction. The origin of this selectivity enhancement is investigated through first-principles density functional theory (DFT) calculations of adsorption energetics and electronic structure. This task reproduces the key DFT-predicted adsorption and electronic properties for chalcogen-modified Cu(111) surfaces that are central to understanding the selectivity mechanism.

## Approach
The computational methodology employs plane-wave DFT with the PBE exchange-correlation functional, DFT-D2 dispersion correction, and projector-augmented wave (PAW) pseudopotentials. Slab models of Cu(111) are constructed with at least four metallic layers, where the top two layers are allowed to relax and a vacuum region exceeding 12 Å is introduced, together with a dipole correction. Chalcogen adatoms (O, S, Se, Te) are placed at a coverage of 1/9 monolayer on one side of the slab. After geometric optimization of these models, single-point calculations are performed to determine adsorption free energies via the computational hydrogen electrode (at U = 0 V vs the reversible hydrogen electrode and pH = 6.7). The adsorbates considered are atomic hydrogen (H*) and carbon dioxide (CO₂*) on clean Cu and atop the chalcogen site. For CO₂* the O–C–O activation angle is extracted. Electronic structure analysis includes Bader charge analysis to quantify the charge on each chalcogen, the center of the chalcogen p-band relative to the Fermi level, and the shift of the Cu d-band center upon chalcogen decoration. All quantities are computed within an implicit solvation framework where applicable. The workflow uses open-source DFT codes capable of the required level of theory.

## Reproduction target
The goal is to compute and report the following quantities for clean Cu(111) and Cu(111)–X surfaces (X = O, S, Se, Te):

- Adsorption free energies (ΔG) of H* on Cu sites and atop the chalcogen adatom site.
- Adsorption free energies of CO₂* on Cu sites and atop the chalcogen adatom site, together with the O–C–O activation angle in degrees.
- Adsorption free energy of the chalcogen adatom itself (referenced to H₂X gas for S, Se, Te and to O₂ gas for O) to verify stability.
- Bader charges on the chalcogen adatoms (in |e⁻|).
- Center of the chalcogen p-band (εₚ–εF) relative to the Fermi level.
- Shift of the Cu d-band center (Δ(ε_d–ε_F)) relative to clean Cu(111).

All results are to be written to the structured JSON files `adsorption_energies.json` and `electronic_properties.json` following the output contracts defined in the workflow steps, using the same level of theory and conditions described in the Approach.

## Assets

- DFT code (PBE-D2, PAW, implicit solvation): Quantum ESPRESSO or GPAW or similar
- Bader charge analysis tool: http://theory.cm.utexas.edu/henkelman/code/bader/
- Copper bulk fcc crystal structure: https://next-gen.materialsproject.org/materials/mp-30

## Workflow steps

### Step 1: Surface model construction and DFT optimization
- Role: process
- Action: Build Cu(111) slab models (4+ metallic layers, top two relaxed, vacuum > 12 Å) and chalcogen-adsorbed slabs with X = O, S, Se, Te at 1/9 ML coverage. Optimize geometries with DFT using PBE-D2 functional, plane-wave basis, PAW pseudopotentials, and dipole correction.
- Evidence: `/app/outputs/optimized_geometries.json`

### Step 2: Chalcogen stability validation
- Role: process
- Action: Compute the adsorption formation energy of each chalcogen adatom on Cu(111) referenced to H₂X(g) (S, Se, Te) and O₂(g) for O to confirm that S, Se, Te adsorb exothermically. Document energies.
- Evidence: `/app/outputs/chalcogen_stability.json`

### Step 3: Reaction intermediate adsorption free energies
- Role: scored (load-bearing)
- Action: Calculate adsorption free energies ΔG (at U = 0 V vs RHE, pH 6.7 using the computational hydrogen electrode) for H* and CO₂* on clean Cu(111) and atop each chalcogen X site. Include the CO₂ activation angle (O-C-O angle in degrees).
- Output file: `/app/outputs/adsorption_energies.json`
- Format: json
- Contract: A JSON object with top-level key 'adsorption_energies' containing an array of objects. Each object has fields: system (string), adsorbate (string, 'H*' or 'CO₂*'), site (string, 'Cu' or 'X'), adsorption_free_energy_eV (number), activation_angle_deg (number, required only for CO₂*). The array must also include entries for chalcogen adsorption energy for each X with adsorbate 'X_adatom'.
- Scoring: scored by hidden verifier

### Step 4: Electronic structure analysis
- Role: scored
- Action: From the optimized charge densities and density-of-states, compute Bader charges on chalcogen atoms, the center of the chalcogen p-band relative to the Fermi level, and the shift in the Cu d-band center compared to clean Cu.
- Output file: `/app/outputs/electronic_properties.json`
- Format: json
- Contract: A JSON array of objects, each with fields: system (string), chalcogen (string, one of 'O','S','Se','Te'), Bader_charge_X_e (number), p_band_center_X_eV (number), d_band_shift_Cu_eV (number).
- Scoring: scored by hidden verifier

### Step 5: Pourbaix diagram construction
- Role: process
- Action: Using the DFT chalcogen formation energies and external aqueous thermodynamics data, construct a Pourbaix diagram for the Cu-O-S system to illustrate the stability region of S adatom-modified Cu at working potentials.
- Evidence: `/app/outputs/pourbaix_diagram.png`

### Step 6: XPS core-level shift calculations
- Role: process
- Action: Compute the Cu 2p core-level binding energy shifts for the chalcogen-decorated Cu(111) models relative to bulk Cu using a DFT-based method.
- Evidence: `/app/outputs/core_level_shifts.json`

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/adsorption_energies.json`
- `/app/outputs/electronic_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### adsorption_energies.json
- path: `/app/outputs/adsorption_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: DFT-computed adsorption free energies for H* and CO₂* on clean Cu(111) and atop chalcogen adatoms (O, S, Se, Te), using the computational hydrogen electrode at U=0 V vs RHE and pH 6.7. Provides the activity trend: H* adsorption must be endergonic on S, Se, Te, and CO₂* must show activation with lower free energies relative to clean Cu.
- schema:
  - `type`: object
  - `required`: `adsorption_energies`
  - `description`: The top-level object must contain a key 'adsorption_energies' whose value is an array. Each array element is an object with fields: system (string), adsorbate (string, 'H*' or 'CO₂*'), site (string, 'Cu' or 'X'), adsorption_free_energy_eV (number), and activation_angle_deg (number, required only for CO₂* entries). The array must also include chalcogen adsorption free energies using adsorbate 'X_adatom'.

### electronic_properties.json
- path: `/app/outputs/electronic_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Electronic descriptors computed from DFT charge density and density-of-states: Bader charge on each chalcogen, p-band center of the chalcogen relative to the Fermi level, and shift in the Cu d-band center relative to clean Cu(111). Explains basicity and reactivity trends.
- schema:
  - `type`: array
  - `description`: An array of objects, each containing: system (string), chalcogen (string, one of 'O','S','Se','Te'), Bader_charge_X_e (number), p_band_center_X_eV (number), d_band_shift_Cu_eV (number).

Notes: The cation effect stage (experimental partial current density vs solvation free energy) is not included because it requires non-public experimental data. The Pourbaix diagram and XPS shifts are included as process steps for completeness but are not scored; their evidence artifacts are optional. All values compared against paper-reported data from Tables S3–S4 with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "adsorption_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "adsorption_energies"
        ],
        "description": "The top-level object must contain a key 'adsorption_energies' whose value is an array. Each array element is an object with fields: system (string), adsorbate (string, 'H*' or 'CO₂*'), site (string, 'Cu' or 'X'), adsorption_free_energy_eV (number), and activation_angle_deg (number, required only for CO₂* entries). The array must also include chalcogen adsorption free energies using adsorbate 'X_adatom'."
      },
      "description": "DFT-computed adsorption free energies for H* and CO₂* on clean Cu(111) and atop chalcogen adatoms (O, S, Se, Te), using the computational hydrogen electrode at U=0 V vs RHE and pH 6.7. Provides the activity trend: H* adsorption must be endergonic on S, Se, Te, and CO₂* must show activation with lower free energies relative to clean Cu."
    },
    {
      "file": "electronic_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "description": "An array of objects, each containing: system (string), chalcogen (string, one of 'O','S','Se','Te'), Bader_charge_X_e (number), p_band_center_X_eV (number), d_band_shift_Cu_eV (number)."
      },
      "description": "Electronic descriptors computed from DFT charge density and density-of-states: Bader charge on each chalcogen, p-band center of the chalcogen relative to the Fermi level, and shift in the Cu d-band center relative to clean Cu(111). Explains basicity and reactivity trends."
    }
  ],
  "notes": "The cation effect stage (experimental partial current density vs solvation free energy) is not included because it requires non-public experimental data. The Pourbaix diagram and XPS shifts are included as process steps for completeness but are not scored; their evidence artifacts are optional. All values compared against paper-reported data from Tables S3–S4 with appropriate tolerances."
}
```

## How you are scored
A hidden verifier reads your output artifacts and independently scores each scored workflow stage. It compares the reported adsorption free energies, activation angles, Bader charges, and band center shifts to reference values derived from the original study's DFT calculations, using scientifically reasonable tolerances that account for variations between DFT implementations. The verifier also checks that the relative trends among the different systems are physically consistent. The final reward is a weighted sum of the per-stage scores, with the adsorption energies and electronic properties each contributing a substantial portion of the total. Simply reporting qualitative descriptions or claiming agreement without the corresponding numeric data will not succeed, as the verifier measures the accuracy of the computed numbers and their internal consistency.

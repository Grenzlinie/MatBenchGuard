# Band Edge and OER Thermodynamics of Strained 2D Heterostructures for Photocatalytic Water Splitting

## Problem background
Two-dimensional van der Waals heterostructures offer tunable electronic properties for photocatalytic water splitting. The WS₂/blue phosphorus (BlueP) heterostructure is a promising candidate, but its pristine band alignment and overpotential for the oxygen evolution reaction (OER) may limit full water splitting. In-plane compressive strain can shift band energies, modify the band alignment type (Type-I, Type-II, Z-scheme), and alter the reaction free-energy landscape. This task reproduces the computation of band gaps, absolute band-edge positions, and OER thermodynamics for WS₂/BlueP under compressive uniaxial and biaxial strains. The goal is to determine whether specific strained configurations are thermodynamically feasible for photocatalytic water splitting at pH 0 and pH 7.

## Approach
The workflow builds the WS₂/BlueP heterostructure in the most stable stacking (P atoms on top of W and S sites) using a 3×3 supercell. Compressive in-plane strains are applied: uniaxial strains of −2% and −4%, and biaxial strains of −2%, −6%, and −8%. Each strained structure is fully relaxed with DFT using the PBE+optB88‑vdW functional. The electronic structure is then refined with the HSE06 hybrid functional to obtain accurate band gaps and the absolute energies of the valence-band maximum (VBM) and conduction-band minimum (CBM) with respect to the vacuum level. From these, the band-alignment type (Type-I, Type-II, or Z-scheme) is classified.

For each strained heterostructure, the four OER intermediates (*H₂O, *OH, *O, *OOH) are adsorbed on the surface, relaxed, and their vibrational frequencies are obtained to compute free-energy corrections. Gibbs free-energy diagrams are constructed at pH 0 and pH 7, and the potential-determining step (PDS) is identified as the step with the largest positive ΔG at U = 1.23 V. The electrochemical driving force (EDF) is calculated from the VBM position relative to the normal hydrogen electrode. The central check is whether EDF ≥ PDS, which indicates thermodynamic feasibility for the OER and hence for full water splitting.

## Reproduction target
Run the simulations described above for each of the five strained cases and produce two scored CSV files under /app/outputs:

- step_01_band_properties.csv: case, Eg (eV), CBM_vacuum (eV), VBM_vacuum (eV), band_type (one of "Type-I", "Type-II", "Z-scheme").
- step_02_oer_thermodynamics.csv: case, PDS_pH0 (eV), EDF_pH0 (eV), feasible_pH0 (bool), PDS_pH7 (eV), EDF_pH7 (eV), feasible_pH7 (bool).

All simulations may be performed with Quantum ESPRESSO, an open-source DFT code that supports HSE06. The reported numbers must be the results of your own calculations, not values copied from any external source.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP PBE pseudopotentials: https://www.materialscloud.org/discover/sssp/table/precision
- WS2/BlueP heterostructure lattice constants and stacking

## Workflow steps

### Step 1: Geometry Relaxation of Strained WS2/BlueP Heterostructures
- Role: process
- Action: Construct the WS2/BlueP heterostructure in Model III stacking using a 3x3 supercell. Apply uniaxial compressive strains of -2% and -4% and biaxial compressive strains of -2%, -6%, -8% to the in-plane lattice constants. For each strained structure, perform full geometry relaxation using PBE functional with optB88-vdW dispersion correction, optimizing atomic positions and cell vectors to force and energy convergence thresholds.
- Evidence: `/app/outputs/relaxation_logs.txt`

### Step 2: HSE06 Band Structure Calculations
- Role: process
- Action: For each relaxed strained heterostructure, perform a hybrid functional HSE06 band structure calculation to obtain the Kohn-Sham eigenvalues along high-symmetry k-points. Extract the band gap and the absolute energies of the valence band maximum (VBM) and conduction band minimum (CBM) relative to the vacuum level.
- Evidence: `/app/outputs/band_outputs.log`

### Step 3: Extract and Report Band Properties
- Role: scored (load-bearing)
- Action: From the HSE06 results, extract the band gap (Eg), VBM vacuum level, CBM vacuum level, and determine the band-alignment type (Type-I, Type-II, or Z-scheme) for each strain case based on the layer contributions. Write the results to a CSV file.
- Output file: `/app/outputs/step_01_band_properties.csv`
- Format: csv
- Contract: Columns: case (string e.g. 'uniaxial_-2%'), Eg (float, eV), CBM_vacuum (float, eV), VBM_vacuum (float, eV), band_type (string: 'Type-I', 'Type-II', or 'Z-scheme'). One row per strain case.
- Scoring: scored by hidden verifier

### Step 4: OER Intermediate Adsorption Calculations
- Role: process
- Action: For each relaxed strained heterostructure, adsorb the four OER intermediates (H2O, OH, O, OOH) on the top site of a W atom in the WS2 layer (the active site for OER). Perform geometry relaxations of the adsorbed systems and compute total energies, vibrational frequencies, zero-point energies, and entropy corrections within the harmonic approximation.
- Evidence: `/app/outputs/oer_energies.log`

### Step 5: OER Thermodynamics and Feasibility Screening
- Role: scored (load-bearing)
- Action: Using the intermediate free energies from step4, calculate the Gibbs free-energy change for each OER step at pH=0 and pH=7 (incorporating the pH correction term). Determine the potential-determining step (PDS) as the step with the largest positive free-energy change at U=1.23 V. Compute the electrochemical driving force (EDF) as (VBM_NHE - 1.23) at pH=0 and (VBM_NHE - 1.23 + 0.059×pH) at pH=7, using the VBM position relative to NHE derived from step3. Assess thermodynamic feasibility (EDF ≥ PDS) and write all results to a CSV file.
- Output file: `/app/outputs/step_02_oer_thermodynamics.csv`
- Format: csv
- Contract: Columns: case (string), PDS_pH0 (float, eV), EDF_pH0 (float, eV), feasible_pH0 (bool), PDS_pH7 (float, eV), EDF_pH7 (float, eV), feasible_pH7 (bool). One row per strain case.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_band_properties.csv`
- `/app/outputs/step_02_oer_thermodynamics.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_band_properties.csv
- path: `/app/outputs/step_01_band_properties.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Computed band gaps, absolute CBM and VBM energies (vacuum-referenced), and band alignment type for each strained heterostructure.
- schema:
  - `type`: table
  - `required_columns`: `case`, `Eg`, `CBM_vacuum`, `VBM_vacuum`, `band_type`
  - `units`:
    - `Eg`: eV
    - `CBM_vacuum`: eV
    - `VBM_vacuum`: eV

### step_02_oer_thermodynamics.csv
- path: `/app/outputs/step_02_oer_thermodynamics.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Potential-determining step (PDS), electrochemical driving force (EDF), and thermodynamic feasibility at pH=0 and pH=7 for each strained heterostructure.
- schema:
  - `type`: table
  - `required_columns`: `case`, `PDS_pH0`, `EDF_pH0`, `feasible_pH0`, `PDS_pH7`, `EDF_pH7`, `feasible_pH7`
  - `units`:
    - `PDS_pH0`: eV
    - `EDF_pH0`: eV
    - `PDS_pH7`: eV
    - `EDF_pH7`: eV

Notes: Scoring compares each quantitative column (Eg, CBM_vacuum, VBM_vacuum, PDS, EDF) to hidden reference values within a tolerance of ±0.1 eV. band_type and feasibility flags are matched exactly. Both CSV files must be present for full credit.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_band_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "case",
          "Eg",
          "CBM_vacuum",
          "VBM_vacuum",
          "band_type"
        ],
        "units": {
          "Eg": "eV",
          "CBM_vacuum": "eV",
          "VBM_vacuum": "eV"
        }
      },
      "description": "Computed band gaps, absolute CBM and VBM energies (vacuum-referenced), and band alignment type for each strained heterostructure."
    },
    {
      "file": "step_02_oer_thermodynamics.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "case",
          "PDS_pH0",
          "EDF_pH0",
          "feasible_pH0",
          "PDS_pH7",
          "EDF_pH7",
          "feasible_pH7"
        ],
        "units": {
          "PDS_pH0": "eV",
          "EDF_pH0": "eV",
          "PDS_pH7": "eV",
          "EDF_pH7": "eV"
        }
      },
      "description": "Potential-determining step (PDS), electrochemical driving force (EDF), and thermodynamic feasibility at pH=0 and pH=7 for each strained heterostructure."
    }
  ],
  "notes": "Scoring compares each quantitative column (Eg, CBM_vacuum, VBM_vacuum, PDS, EDF) to hidden reference values within a tolerance of ±0.1 eV. band_type and feasibility flags are matched exactly. Both CSV files must be present for full credit."
}
```

## How you are scored
A hidden verifier reads the two output CSV files. For the quantitative columns (Eg, CBM_vacuum, VBM_vacuum, PDS_pH0, EDF_pH0, PDS_pH7, EDF_pH7) the verifier compares your computed values against expected reference values. The band_type strings and the feasible_pH0/feasible_pH7 boolean flags are compared exactly. The overall score is a weighted combination of these comparisons; accurate energy values carry the most weight. The verifier does not require you to reproduce any specific exact number but checks that your results are physically consistent with the strained heterostructure models. No additional artifacts beyond the two CSV files are scored.

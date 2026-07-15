# DFT Evaluation of Perovskite Surface Electrochemistry for Solar Water Splitting

## Problem background
Solar water splitting in a single photoelectrocatalyst material requires that the semiconductor's band edges straddle the equilibrium potentials for both the oxygen evolution reaction (OER) and hydrogen evolution reaction (HER), and that the material's surface can catalyze both half-reactions. Additional free-energy losses in a practical device, typically at least 0.5 eV, must also be overcome. A previous screening study identified several perovskite materials with bandgaps and bulk stability potentially suitable for total water splitting. The present task evaluates whether the surfaces of these candidate perovskite photoabsorbers also possess the catalytic properties needed for unassisted total water splitting, by computing the thermodynamic overpotentials for OER and HER and assessing surface stability under reaction conditions.

## Approach
Using plane-wave density functional theory (DFT) with the RPBE functional, as implemented in the open-source Quantum Espresso code, the adsorption free energies of the reaction intermediates OH*, O*, OOH*, and H* are computed on the BO₂‑terminated (100) surfaces of the perovskites. From these free energies, the theoretical overpotentials for OER and HER are derived via the computational hydrogen electrode (CHE) model, which treats proton‑electron transfer steps on the reversible hydrogen electrode scale. Both a low-coverage regime (θ = 0.25 ML) and, for the materials that remain stable after a surface stability analysis, a high-coverage regime at the stable coverage determined from that analysis are considered. Oxygen vacancy formation energies are computed relative to water at 0 V vs. RHE to assess surface stability. The overpotentials and vacancy energies are then combined with the direct and indirect bandgaps of the materials, taken from the published Castelli et al. (2012) dataset, to determine the feasibility of unassisted total water splitting at pH 7, accounting for a 0.5 eV photovoltage margin.

## Reproduction target
For the eight perovskite materials SnTiO₃, CaTaO₂N, MgTaO₂N, LaTiO₂N, SrTaO₂N, BaTaO₂N, CaGeO₃, and SrGeO₃, compute:
- the low-coverage HER and OER theoretical overpotentials (η_HER, η_OER) at θ = 0.25 ML;
- the surface oxygen vacancy formation energy (ΔE_vac) relative to water at 0 V vs. RHE;
- the high-coverage OER overpotential (η_OER) for the six non‑germanate materials, using the most stable surface O* coverage determined by a coverage-dependent stability analysis;
- the direct and indirect bandgap values for all eight materials from the Castelli et al. dataset.

Store the results in the CSV files listed below, following the provided column schemas. Then, combine the band‑edge positions (derived from the bandgaps) with the computed overpotentials and vacancy formation energies, apply a 0.5 eV photovoltage margin, and assess, for each material, whether it can simultaneously drive HER and OER at pH 7 without surface degradation. The hidden verifier will check this logical assessment from your submitted data.

## Assets

- Perovskite candidate bandgaps and crystal structures from Castelli et al. 2012: https://doi.org/10.1039/C2EE00064F
- Quantum Espresso: https://www.quantum-espresso.org/

## Workflow steps

### Step 1: Construct slab models and compute low-coverage adsorption energies
- Role: process
- Action: For each of the eight target materials (SnTiO₃, CaTaO₂N, MgTaO₂N, LaTiO₂N, SrTaO₂N, BaTaO₂N, CaGeO₃, SrGeO₃), build BO₂‑terminated (100) perovskite slabs with a 2×2×4 supercell and 10 Å of vacuum. Perform DFT relaxation using Quantum Espresso with the RPBE functional and appropriate pseudopotentials to compute total energies of the clean slab and with OH*, O*, OOH*, and H* adsorbates at a coverage of θ=0.25 ML.
- Evidence: none

### Step 2: Calculate low-coverage theoretical overpotentials
- Role: scored (load-bearing)
- Action: From the adsorption energies obtained in the previous step, apply the computational hydrogen electrode (CHE) model including harmonic free-energy corrections to derive the low‑coverage theoretical OER and HER overpotentials for all eight materials. Write the results to a CSV file.
- Output file: `/app/outputs/low_coverage_overpotentials.csv`
- Format: csv
- Contract: CSV with columns: material (string), η_HER_low (float), η_OER_low (float); one row per material.
- Scoring: scored by hidden verifier

### Step 3: Compute surface oxygen vacancy formation energies
- Role: scored
- Action: For each of the eight materials, compute the total energy of the slab with a surface oxygen vacancy at θ=0.25 ML and calculate the vacancy formation energy ΔE_vac relative to H₂O at 0 V vs. RHE. Write the results to a CSV file.
- Output file: `/app/outputs/vacancy_formation_energies.csv`
- Format: csv
- Contract: CSV with columns: material (string), ΔE_vac (float); one row per material, in eV.
- Scoring: scored by hidden verifier

### Step 4: Compute adsorption energies at high O* coverage (θ_O = 0.75 ML)
- Role: process
- Action: For the six non‑germanate materials (SnTiO₃, CaTaO₂N, MgTaO₂N, LaTiO₂N, SrTaO₂N, BaTaO₂N), directly set the background O* coverage to θ_O = 0.75 ML (the most stable coverage identified in the paper) and run DFT calculations to obtain total energies of the slab with this background and with additional OOH* and OH* adsorbates. Use the RPBE functional and the same slab model as in Step 1. No surface phase diagram construction is required.
- Evidence: none

### Step 5: Calculate high-coverage OER overpotential
- Role: scored (load-bearing)
- Action: Using the high‑coverage adsorption energies from the previous step (background θ_O = 0.75 ML), apply the computational hydrogen electrode (CHE) model with harmonic free-energy corrections to compute the OER overpotential at this high coverage for the six materials. Write the results to a CSV file.
- Output file: `/app/outputs/high_coverage_overpotentials.csv`
- Format: csv
- Contract: CSV with columns: material (string), η_OER_high (float); one row per material, in V.
- Scoring: scored by hidden verifier

### Step 6: Retrieve bandgap data from Castelli et al.
- Role: scored
- Action: Obtain the direct and indirect bandgap values for the eight materials from the published data of Castelli et al. (2012) or the Computational Materials Repository. Format the data as a CSV file.
- Output file: `/app/outputs/bandgap_data.csv`
- Format: csv
- Contract: CSV with columns: material (string), direct_bandgap (float), indirect_bandgap (float); one row per material, in eV.
- Scoring: scored by hidden verifier

### Step 7: Evaluate total water splitting feasibility
- Role: process
- Action: Combine the band‑edge positions (derived from bandgaps) with the computed overpotentials (low and high coverage) and vacancy formation energies. Apply a 0.5 eV photovoltage margin and determine, for each material, whether it can simultaneously drive HER and OER at pH 7 without degrading. The checker will verify this conclusion programmatically from the submitted data; no separate scored artifact is required.
- Evidence: none

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/low_coverage_overpotentials.csv`
- `/app/outputs/high_coverage_overpotentials.csv`
- `/app/outputs/vacancy_formation_energies.csv`
- `/app/outputs/bandgap_data.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### low_coverage_overpotentials.csv
- path: `/app/outputs/low_coverage_overpotentials.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Low-coverage theoretical overpotentials for HER and OER for eight perovskite materials.
- schema:
  - `type`: table
  - `required_columns`: `material`, `η_HER_low`, `η_OER_low`
  - `units`:
    - `η_HER_low`: V
    - `η_OER_low`: V

### high_coverage_overpotentials.csv
- path: `/app/outputs/high_coverage_overpotentials.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: High-coverage OER overpotential for six materials that survive the stability analysis.
- schema:
  - `type`: table
  - `required_columns`: `material`, `η_OER_high`
  - `units`:
    - `η_OER_high`: V

### vacancy_formation_energies.csv
- path: `/app/outputs/vacancy_formation_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Surface oxygen vacancy formation energies for eight perovskite materials.
- schema:
  - `type`: table
  - `required_columns`: `material`, `ΔE_vac`
  - `units`:
    - `ΔE_vac`: eV

### bandgap_data.csv
- path: `/app/outputs/bandgap_data.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Direct and indirect bandgap values from Castelli et al. for eight perovskite materials.
- schema:
  - `type`: table
  - `required_columns`: `material`, `direct_bandgap`, `indirect_bandgap`
  - `units`:
    - `direct_bandgap`: eV
    - `indirect_bandgap`: eV

Notes: The checker will programmatically verify the logical conclusion of water splitting feasibility using the submitted CSV values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "low_coverage_overpotentials.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "η_HER_low",
          "η_OER_low"
        ],
        "units": {
          "η_HER_low": "V",
          "η_OER_low": "V"
        }
      },
      "description": "Low-coverage theoretical overpotentials for HER and OER for eight perovskite materials."
    },
    {
      "file": "high_coverage_overpotentials.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "η_OER_high"
        ],
        "units": {
          "η_OER_high": "V"
        }
      },
      "description": "High-coverage OER overpotential for six materials that survive the stability analysis."
    },
    {
      "file": "vacancy_formation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "ΔE_vac"
        ],
        "units": {
          "ΔE_vac": "eV"
        }
      },
      "description": "Surface oxygen vacancy formation energies for eight perovskite materials."
    },
    {
      "file": "bandgap_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "direct_bandgap",
          "indirect_bandgap"
        ],
        "units": {
          "direct_bandgap": "eV",
          "indirect_bandgap": "eV"
        }
      },
      "description": "Direct and indirect bandgap values from Castelli et al. for eight perovskite materials."
    }
  ],
  "notes": "The checker will programmatically verify the logical conclusion of water splitting feasibility using the submitted CSV values."
}
```

## How you are scored
Your submission will be scored by a hidden verifier program that reads the output CSV files and compares the values you report (or, where possible, recomputes quantities) against reference data. Each workflow stage (low-coverage overpotentials, high-coverage OER overpotential, vacancy formation energies, bandgap data) contributes a weighted share to the overall reward. The verifier also programmatically checks that the logical viability assessment you perform in the final step is consistent with the numerical data you submitted. Merely reporting numbers that match a known answer is not sufficient; the verifier will examine whether the process steps were executed and the derived quantities are self-consistent. Higher reward is given for results that closely match the reference values for each quantity and for a correct overall viability judgement.

# Geometric Characterization and GCMC Methane Adsorption of MOF-5 Analogues

## Problem background
Metal-organic frameworks (MOFs) are nanoporous materials built from metal or metal oxide clusters connected by organic linkers. Because of their exceptionally high internal surface areas, MOFs are promising candidates for gas storage, particularly for vehicular methane storage. MOF-5, which consists of Zn₄O clusters and linear benzene-1,4-dicarboxylic acid linkers, is a prototype framework. By substituting the organic linker with alternative commercially available dicarboxylic acids while preserving the same topology, a family of isoreticular MOF-5 analogues can be created. Determining the geometric pore properties and methane adsorption capacities of such a library is an essential step toward identifying high-performance materials. In this task you will compute the geometric pore descriptors and methane adsorption uptakes for a set of 111 pre-relaxed MOF-5 analogue crystal structures deposited in a public database, at conditions relevant to vehicular methane storage.

## Approach
The computational workflow consists of two main stages. First, for each of the downloaded MOF-5 analogue crystal structures, you will perform a geometric pore analysis using the Zeo++ code. This analysis characterises the largest included sphere (Dᵢ), the largest free sphere (D_f), and the methane-accessible surface area (both volumetric and gravimetric) by probing the framework with a sphere of radius 1.625 Å (the approximate size of a methane molecule). Second, for each structure you will run Grand Canonical Monte Carlo (GCMC) simulations to compute methane adsorption uptakes at 298 K and 35 bar. The simulations use the TraPPE methane model for the adsorbate, the Universal Force Field (UFF) for the framework atoms, and Lennard-Jones interactions with Lorentz–Berthelot mixing rules. The final outputs are two CSV files containing the geometric descriptors and the methane uptakes for all 111 structures.

## Reproduction target
Compute the geometric pore descriptors (largest included sphere Dᵢ, largest free sphere D_f, volumetric methane-accessible surface area, and gravimetric methane-accessible surface area) for all 111 MOF-5 analogue structures, and compute the methane adsorption uptakes (volumetric uptake in cm³_STP/cm³ and gravimetric uptake in mol kg⁻¹) at 298 K and 35 bar for the same set of structures. Write the results to the specified CSV files according to the output contract.

## Assets

- MOF-5 analogue crystal structures (relaxed, 111 porous): http://www.carboncapturematerials.org
- Zeo++: https://github.com/zeoplusplus/zeo
- RASPA2: https://github.com/numat/RASPA2
- Universal Force Field (UFF): RASPA2
- TraPPE methane model: RASPA2

## Workflow steps

### Step 1: Fetch MOF-5 analogue crystal structures
- Role: process
- Action: Download the set of 111 PM6-DH2-relaxed MOF-5 analogue crystal structures (CIF format) from the Carbon Capture Materials database. Unpack and store them in a local directory.
- Evidence: `/app/outputs/structures_manifest.txt`

### Step 2: Compute geometric pore descriptors
- Role: scored
- Action: For each downloaded MOF-5 analogue structure (CIF), compute geometric pore descriptors using Zeo++ with a methane probe radius of 1.625 Å, 100,000 Monte Carlo samples per unit cell for accessible volume, 3,000 samples per atom for accessible surface area, and atomic radii from the Cambridge Crystallographic Data Centre. Report the largest included sphere (Di), largest free sphere (Df), volumetric methane-accessible surface area (ASA), and gravimetric ASA for each structure.
- Output file: `/app/outputs/geometric_descriptors.csv`
- Format: csv
- Contract: structure_id (string), Di_angstrom (float), Df_angstrom (float), volumetric_ASA_m2_per_cm3 (float), gravimetric_ASA_m2_per_g (float)
- Scoring: scored by hidden verifier

### Step 3: Grand Canonical Monte Carlo methane adsorption
- Role: scored (load-bearing)
- Action: For each structure, perform GCMC methane adsorption simulation at T=298 K and P=35 bar using a rigid framework. Employ the TraPPE methane model, UFF for framework atoms, Lorentz-Berthelot mixing rules, Lennard-Jones cutoff radius 12 Å, and simulation boxes at least 2× the cutoff. Run enough Monte Carlo cycles (several million) to obtain converged volumetric (cm³_STP/cm³) and gravimetric (mol/kg) methane uptakes. Report the final uptakes.
- Output file: `/app/outputs/methane_uptake_35bar.csv`
- Format: csv
- Contract: structure_id (string), volumetric_uptake_V_STP_per_V (float), gravimetric_uptake_mol_per_kg (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/geometric_descriptors.csv`
- `/app/outputs/methane_uptake_35bar.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### geometric_descriptors.csv
- path: `/app/outputs/geometric_descriptors.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Geometric pore descriptors for all 111 methane-accessible MOF-5 analogues. The checker verifies Di >= Df, checks that value ranges fall within paper-reported bounds, and confirms that top structures match expected IDs.
- schema:
  - `type`: table
  - `required_columns`: `structure_id`, `Di_angstrom`, `Df_angstrom`, `volumetric_ASA_m2_per_cm3`, `gravimetric_ASA_m2_per_g`
  - `units`:
    - `Di_angstrom`: angstrom
    - `Df_angstrom`: angstrom
    - `volumetric_ASA_m2_per_cm3`: m2 / cm3
    - `gravimetric_ASA_m2_per_g`: m2 / g

### methane_uptake_35bar.csv
- path: `/app/outputs/methane_uptake_35bar.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Methane adsorption uptakes at 298 K and 35 bar for the same set of MOF-5 analogues. The checker compares the top three volumetric and top three gravimetric uptakes (and their structure IDs) to hidden gold values, awarding full credit when the uptakes meet or exceed the reference.
- schema:
  - `type`: table
  - `required_columns`: `structure_id`, `volumetric_uptake_V_STP_per_V`, `gravimetric_uptake_mol_per_kg`
  - `units`:
    - `volumetric_uptake_V_STP_per_V`: V_STP / V
    - `gravimetric_uptake_mol_per_kg`: mol / kg

Notes: The checker reads both CSV files. For geometric descriptors, it checks that all structures fall within the paper’s Table 2 ranges (±20% tolerance) and that Di ≥ Df. For methane uptake, it compares the top three volumetric and gravimetric uptakes and structure IDs to hidden paper values using a tolerance; higher uptake is better. All comparisons use hidden gold values, never revealed to the agent. The load‑bearing methane uptake step ensures the core GCMC simulation is genuinely executed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "geometric_descriptors.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "structure_id",
          "Di_angstrom",
          "Df_angstrom",
          "volumetric_ASA_m2_per_cm3",
          "gravimetric_ASA_m2_per_g"
        ],
        "units": {
          "Di_angstrom": "angstrom",
          "Df_angstrom": "angstrom",
          "volumetric_ASA_m2_per_cm3": "m2 / cm3",
          "gravimetric_ASA_m2_per_g": "m2 / g"
        }
      },
      "description": "Geometric pore descriptors for all 111 methane-accessible MOF-5 analogues. The checker verifies Di >= Df, checks that value ranges fall within paper-reported bounds, and confirms that top structures match expected IDs."
    },
    {
      "file": "methane_uptake_35bar.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "structure_id",
          "volumetric_uptake_V_STP_per_V",
          "gravimetric_uptake_mol_per_kg"
        ],
        "units": {
          "volumetric_uptake_V_STP_per_V": "V_STP / V",
          "gravimetric_uptake_mol_per_kg": "mol / kg"
        }
      },
      "description": "Methane adsorption uptakes at 298 K and 35 bar for the same set of MOF-5 analogues. The checker compares the top three volumetric and top three gravimetric uptakes (and their structure IDs) to hidden gold values, awarding full credit when the uptakes meet or exceed the reference."
    }
  ],
  "notes": "The checker reads both CSV files. For geometric descriptors, it checks that all structures fall within the paper’s Table 2 ranges (±20% tolerance) and that Di ≥ Df. For methane uptake, it compares the top three volumetric and gravimetric uptakes and structure IDs to hidden paper values using a tolerance; higher uptake is better. All comparisons use hidden gold values, never revealed to the agent. The load‑bearing methane uptake step ensures the core GCMC simulation is genuinely executed."
}
```

## How you are scored
Each scored output artifact — geometric_descriptors.csv and methane_uptake_35bar.csv — is independently evaluated by a hidden verifier. The verifier checks that your results satisfy expected physical constraints (e.g., Dᵢ ≥ D_f), that the value ranges are plausible, and that the top-performing structures with respect to methane uptake match the expected identifiers. The individual stage scores are combined by weight to produce a final reward between 0 and 1. Simply reporting the paper’s numbers is not sufficient; the verifier inspects the data you have actually computed.

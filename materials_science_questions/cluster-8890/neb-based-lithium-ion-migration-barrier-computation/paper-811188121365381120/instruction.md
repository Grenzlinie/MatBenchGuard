# Maxwell-Stefan Diffusivity and Density/Enthalpy of LiF-ThF4 Molten Salt via Molecular Dynamics

## Problem background
Molten salt mixtures of lithium fluoride and thorium fluoride (LiF-ThF4) serve as both fuel and coolant in advanced molten salt reactors. Understanding the multicomponent diffusion of these ionic fluids is critical for reactor design, as the relative mobility of the various ion species controls heat transfer and influences neutronics. The Maxwell-Stefan (MS) formalism is well suited for describing diffusion in ionic systems because it accounts for electric fields and yields symmetric diffusion coefficients. Computing the MS diffusivities, particularly the cation-cation coefficient D_{LiTh}, as a function of ThF4 concentration can reveal how the local structure and clustering of ions affect the transport properties. Similarly, the density and specific enthalpy of the salt mixture vary with composition, and knowledge of their concentration dependence is valuable for engineering calculations. This task provides the framework to compute these quantities from first‑principles molecular dynamics simulations, producing quantitative data that can be compared against established physical understanding.

## Approach
We will carry out classical equilibrium molecular dynamics (MD) simulations of LiF-ThF4 mixtures using the Born‑Mayer‑Huggins interatomic potential, with parameters taken from the published literature. The workflow begins by generating random initial atomic configurations for a series of ThF4 mole fractions using the PACKMOL tool. For each composition, MD runs are performed with the DL_POLY_4 package (or an equivalent MD engine) at two temperatures: 1200 K for dynamics leading to D_{LiTh}, and 1273 K for density/enthalpy measurements. The simulation protocol includes NPT and NVT equilibration phases followed by a production period, during which we apply Green‑Kubo integration of the diffusive flux correlations to obtain the Onsager coefficient matrix. After the MD runs, the three independent MS diffusivities (D_{LiF}, D_{ThF}, D_{LiTh}) are derived from the Onsager matrix using the B‑matrix method. Additionally, density and specific enthalpy are extracted from the NPT simulations. The overall process produces two main data products: a table of D_{LiTh} versus ThF4 mole percent, and a table of density and enthalpy versus ThF4 mole percent. These data are then evaluated against a hidden reference to assess the quality of the reproduction.

## Reproduction target
Using the procedure described above, compute the Maxwell‑Stefan diffusivity D_{LiTh} (in m²/s) at 1200 K for at least the following ThF4 mole fractions: 2%, 4%, 6%, 10%, 15%, 22%, 30%, 35%, 43.9%, 45%. If necessary to adequately resolve the composition dependence, you may include additional points. Also compute the density (in g/cm³) and specific enthalpy (in kJ/g) for the same set of compositions at 1273 K. Save the results as two CSV files: D_LiTh_vs_concentration.csv (columns ThF4_mol_percent, D_LiTh_m2_per_s) and density_enthalpy_vs_concentration.csv (columns ThF4_mol_percent, density_g_per_cm3, specific_enthalpy_kJ_per_g). The checker will verify that the reported values are physically reasonable for this salt system by comparing them to a set of hidden reference values. No prior knowledge of the paper's exact results is required; the reference serves only as a benchmark for scoring.

## Assets

- DL_POLY_4 molecular dynamics package: https://www.scd.stfc.ac.uk/Pages/DL_POLY_4.aspx
- PACKMOL initial configuration generator: https://m3g.github.io/packmol/
- Born-Mayer-Huggins potential parameters for LiF-ThF4 from Dewan et al. (J. Nucl. Mater. 2013): 10.1016/j.jnucmat.2012.09.030

## Workflow steps

### Step 1: Generate initial configurations
- Role: process
- Action: Use PACKMOL to build initial atomic configurations for LiF-ThF4 mixtures at ThF4 mole percents of 2, 4, 6, 10, 15, 22, 30, 35, 43.9, and 45%, each containing about 5000-6000 ions in a cubic box.
- Evidence: `/app/outputs/config_generation.log`

### Step 2: Run MD simulations and compute Onsager coefficients
- Role: process
- Action: For each initial configuration, perform MD simulations using DL_POLY_4 (or an equivalent MD engine) with the Born-Mayer-Huggins potential parameters from Dewan et al. (2013). Follow the protocol: equilibrate NPT (1 ns, T=1200 K for D_{LiTh} or 1273 K for density/enthalpy), NVT (1 ns), then collect production data for 400 ps with a 1 fs timestep. Use Ewald summation for electrostatics. During the simulation, implement Green-Kubo evaluation of diffusive flux correlations and compute Onsager coefficients on-the-fly (via custom modules or trajectory post-processing). Also record density and specific enthalpy from the NPT runs at 1273 K.
- Evidence: `/app/outputs/onsager_coefficients.csv`

### Step 3: Derive Maxwell-Stefan diffusivities
- Role: process
- Action: From the Onsager coefficients, compute the three independent MS diffusivities (D_{LiF}, D_{ThF}, D_{LiTh}) for each composition using the B-matrix approach outside the MD simulation. Save the intermediate values.
- Evidence: `/app/outputs/all_ms_diffusivities.csv`

### Step 4: Compile D_LiTh vs concentration
- Role: scored (load-bearing)
- Action: Extract the D_{LiTh} values from the intermediate MS diffusivities and write a CSV file with columns ThF4_mol_percent and D_LiTh_m2_per_s for each composition at 1200 K.
- Output file: `/app/outputs/D_LiTh_vs_concentration.csv`
- Format: csv
- Contract: Columns: ThF4_mol_percent (float), D_LiTh_m2_per_s (float). Rows for at least the ten specified compositions.
- Scoring: scored by hidden verifier

### Step 5: Compile density and enthalpy vs concentration
- Role: scored
- Action: From the NPT simulation records at 1273 K for the same compositions, extract density and specific enthalpy and write a CSV file with columns ThF4_mol_percent, density_g_per_cm3, specific_enthalpy_kJ_per_g.
- Output file: `/app/outputs/density_enthalpy_vs_concentration.csv`
- Format: csv
- Contract: Columns: ThF4_mol_percent (float), density_g_per_cm3 (float), specific_enthalpy_kJ_per_g (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/D_LiTh_vs_concentration.csv`
- `/app/outputs/density_enthalpy_vs_concentration.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### D_LiTh_vs_concentration.csv
- path: `/app/outputs/D_LiTh_vs_concentration.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Maxwell-Stefan diffusivity D_{LiTh} at 1200 K for a set of ThF4 mole fractions. Values are compared against hidden gold; scoring verifies sign crossovers and trend.
- schema:
  - `type`: table
  - `required_columns`: `ThF4_mol_percent`, `D_LiTh_m2_per_s`
  - `units`:
    - `ThF4_mol_percent`: mol%
    - `D_LiTh_m2_per_s`: m²/s

### density_enthalpy_vs_concentration.csv
- path: `/app/outputs/density_enthalpy_vs_concentration.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Density and specific enthalpy at 1273 K as functions of ThF4 concentration, compared to hidden gold values and square-root fit trend.
- schema:
  - `type`: table
  - `required_columns`: `ThF4_mol_percent`, `density_g_per_cm3`, `specific_enthalpy_kJ_per_g`
  - `units`:
    - `ThF4_mol_percent`: mol%
    - `density_g_per_cm3`: g/cm³
    - `specific_enthalpy_kJ_per_g`: kJ/g

Notes: The hidden checker compares D_LiTh values against reference data from the paper's Fig. 9(a), checking for five sign crossovers and amplitude decay. Density/enthalpy are compared against Fig. 2 and Fig. 3(a) with tolerances and fitted square-root function parameters.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "D_LiTh_vs_concentration.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "ThF4_mol_percent",
          "D_LiTh_m2_per_s"
        ],
        "units": {
          "ThF4_mol_percent": "mol%",
          "D_LiTh_m2_per_s": "m²/s"
        }
      },
      "description": "Maxwell-Stefan diffusivity D_{LiTh} at 1200 K for a set of ThF4 mole fractions. Values are compared against hidden gold; scoring verifies sign crossovers and trend."
    },
    {
      "file": "density_enthalpy_vs_concentration.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "ThF4_mol_percent",
          "density_g_per_cm3",
          "specific_enthalpy_kJ_per_g"
        ],
        "units": {
          "ThF4_mol_percent": "mol%",
          "density_g_per_cm3": "g/cm³",
          "specific_enthalpy_kJ_per_g": "kJ/g"
        }
      },
      "description": "Density and specific enthalpy at 1273 K as functions of ThF4 concentration, compared to hidden gold values and square-root fit trend."
    }
  ],
  "notes": "The hidden checker compares D_LiTh values against reference data from the paper's Fig. 9(a), checking for five sign crossovers and amplitude decay. Density/enthalpy are compared against Fig. 2 and Fig. 3(a) with tolerances and fitted square-root function parameters."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that independently scores each of the two scored workflow stages. The verifier reads the two CSV files you produce and compares the numbers against a hidden set of gold reference data. For the D_{LiTh} file, the check assesses the agreement of the reported diffusivity values with the reference. For the density and enthalpy file, the check assesses the closeness of the reported values to the reference. In both cases, the comparison takes into account the entire composition range, rewarding physically consistent data that match the expected behavior of the salt mixture. The final reward is a weighted average of the stage scores, with the D_{LiTh} stage carrying the highest weight because it represents the main result of the study. Reporting the paper's published numbers without executing the full simulation workflow will not suffice; the verifier's scoring is based on the output of your actual MD simulations and post‑processing steps.

# Effect of Zeolite Flexibility on Argon Adsorption Isotherms: GCMC Simulations

## Problem background
Pure-silica MEL zeolite adsorbs argon and the experimental isotherm at 77 K shows a sub-step at high loading before saturation — a steep increase in uptake that is not yet fully understood. Grand Canonical Monte Carlo (GCMC) simulations provide a way to isolate the roles of adsorbate–adsorbate and adsorbate–framework interactions, and to test whether the zeolite's structural flexibility influences the isotherm shape and the energetic cost of adsorption. This task asks you to compute the adsorption isotherm and isosteric heat of argon on MEL under several modelling conditions: a rigid zeolite and two flexible force‑field parameterisations (modified Nicholas and modified Demontis), plus average‑structure variants. The results will reveal how the choice of intrazeolite potential affects the presence and position of the sub-step and the trend of the heat of adsorption.

## Approach
The computational approach is to run Grand Canonical Monte Carlo simulations of argon adsorption on a MEL supercell at 77 K. The argon–argon and argon–oxygen (zeolite) interactions are treated with Lennard‑Jones potentials, using the following parameters: Ar–Ar ε/kB = 124.07 K, σ = 3.380 Å; Ar–O ε/kB = 114.81 K, σ = 3.1265 Å. All non‑bonded interactions are truncated and shifted at 12 Å; for the Nicholas model only, long‑range Coulombic contributions are included via Ewald summation.

Three primary zeolite models are considered:
- rigid framework: atoms fixed at the experimental crystallographic positions.
- flexible framework with the modified Nicholas potential: includes bonding, bending, torsional, van der Waals, and Coulombic terms, with equilibrium bond lengths and angles taken from the experimental MEL structure.
- flexible framework with the modified Demontis potential: a simpler model with only Si–O and O–O bonding terms, again with experimental bond distances and angles.

For each model, GCMC simulations are run over a range of relative pressure (p/p0 from ≈ 10⁻⁶ to 1), each consisting of at least 1 million Monte Carlo cycles after equilibration. Cycle moves include particle insertion/deletion and translation, plus one zeolite‑atom move per cycle in the flexible simulations.

From the accumulated ensemble averages — average number of adsorbed argon, total energy, and the cross‑moment ⟨U·N⟩ — you will compute:
- the adsorption isotherm: loading (molecules per unit cell) versus p/p0.
- the isosteric heat of adsorption using the fluctuation formula qst = RT − (⟨U·N⟩ − ⟨U⟩⟨N⟩) / (⟨N²⟩ − ⟨N⟩²), with the gas‑phase potential energy taken as zero.

Additionally, you will compute average atomic positions of the zeolite from the empty and fully‑loaded configurations of the flexible runs, and then repeat the rigid‑framework GCMC simulations on those average structures. This yields two more conditions per flexible model (average‑empty and average‑loaded) that help disentangle static deformation from true dynamic flexibility.

## Reproduction target
You must produce two CSV files placed in /app/outputs:

1. adsorption_isotherms.csv with columns: pressure_ratio (p/p0), loading (molecules per unit cell), model (one of 'rigid', 'Nicholas_mod_flex', 'Demontis_mod_flex', 'Nicholas_avg_empty', 'Nicholas_avg_loaded', 'Demontis_avg_empty', 'Demontis_avg_loaded').
2. isosteric_heat.csv with columns: loading (molecules per unit cell), heat (kJ/mol), model (same identifiers).

The hidden verifier will check these files against reference values and structural expectations. In particular, it will verify three properties:
(a) the stated loading values at several key pressures (low loading, half loading ~24 molecules/u.c., and near saturation) are within acceptable tolerances;
(b) the flexible isotherms are inspected for the presence or absence of a sub-step — a loading increase > 5 molecules/u.c. occurring within < 0.5 decades of relative pressure in the loading window 28–40 molecules/u.c. — and the sub-step's loading location is compared to reference;
(c) the isosteric heat curves are checked for qualitative trends (e.g., monotonicity, plateau, drop) against reference data for each model.

Meeting these checks requires that your GCMC simulations accurately model the specified potentials and that your post‑processing faithfully extracts the ensemble averages.

## Assets

- MEL zeolite crystal structure (CIF) from IZA-SC database: http://www.iza-structure.org/databases/
- RASPA2 or equivalent open-source GCMC molecular simulation package: https://github.com/numat/RASPA2

## Workflow steps

### Step 1: Prepare zeolite structures and force field input files
- Role: process
- Action: Download the MEL CIF file from the IZA database. Build a 2×2×3 supercell. Prepare input decks for the chosen GCMC code with force field parameters for: rigid framework (experimental atomic coordinates), flexible framework using the modified Nicholas model (bonded + non-bonded terms, experimental bond distances/angles), flexible framework using the modified Demontis model (bonded terms only, experimental bond distances/angles). Ar–Ar and Ar–O Lennard-Jones parameters are those provided in the task instruction. Also prepare inputs for the average‑structure simulations.
- Evidence: `/app/outputs/preparation.log`

### Step 2: GCMC simulations for rigid and flexible zeolite models
- Role: process
- Action: Run Grand Canonical Monte Carlo simulations at T=77 K for the rigid framework and for the two flexible models (modified Nicholas, modified Demontis). Use Lennard‑Jones parameters (Ar‑Ar ε/kB=124.07 K, σ=3.380 Å; Ar‑O ε/kB=114.81 K, σ=3.1265 Å) with 12 Å cutoff and shift. For the Nicholas model include Ewald summation. Equilibrate and then perform at least 1 million MC cycles per pressure point, covering the relative pressure range from ≈10⁻⁶ to 1. Save ensemble averages (loading, potential energy, particle fluctuations, etc.) for each condition.
- Evidence: none

### Step 3: GCMC simulations on average zeolite structures
- Role: process
- Action: From the flexible simulation trajectories, compute the average atomic positions of the zeolite for the empty and fully loaded conditions. Then run rigid‑framework GCMC simulations on those average structures for the modified Nicholas and modified Demontis cases, using the same intermolecular parameters and pressure range.
- Evidence: none

### Step 4: Assemble adsorption isotherms
- Role: scored (load-bearing)
- Action: From the GCMC outputs of steps 2 and 3, extract the average argon loading (molecules per unit cell) as a function of relative pressure p/p0. Write a CSV containing all model conditions: rigid, Nicholas_mod_flex, Demontis_mod_flex, Nicholas_avg_empty, Nicholas_avg_loaded, Demontis_avg_empty, Demontis_avg_loaded.
- Output file: `/app/outputs/adsorption_isotherms.csv`
- Format: csv
- Contract: Columns: pressure_ratio (float, dimensionless, p/p0), loading (float, molecules per unit cell), model (string, one of: 'rigid', 'Nicholas_mod_flex', 'Demontis_mod_flex', 'Nicholas_avg_empty', 'Nicholas_avg_loaded', 'Demontis_avg_empty', 'Demontis_avg_loaded').
- Scoring: scored by hidden verifier

### Step 5: Compute isosteric heats of adsorption
- Role: scored
- Action: Using the energy and particle number averages from the GCMC runs, compute the isosteric heat of adsorption at each loading via the energy/particle fluctuation formula (qst = RT − (⟨U·N⟩−⟨U⟩⟨N⟩)/(⟨N²⟩−⟨N⟩²) with Ug=0). Write heat vs loading for the same set of model conditions as in step 4.
- Output file: `/app/outputs/isosteric_heat.csv`
- Format: csv
- Contract: Columns: loading (float, molecules per unit cell), heat (float, kJ/mol), model (string, same identifiers as in the isotherm file).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/adsorption_isotherms.csv`
- `/app/outputs/isosteric_heat.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### adsorption_isotherms.csv
- path: `/app/outputs/adsorption_isotherms.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Simulated adsorption isotherms for all zeolite models. The hidden checker compares loading values to paper‑reported gold with tolerances and performs structural checks (sub‑step presence/absence).
- schema:
  - `type`: table
  - `required_columns`: `pressure_ratio`, `loading`, `model`
  - `units`:
    - `pressure_ratio`: dimensionless (p/p0)
    - `loading`: molecules per unit cell

### isosteric_heat.csv
- path: `/app/outputs/isosteric_heat.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Isosteric heat of adsorption curves for all zeolite models. The hidden checker compares heat values at specified loadings to paper‑reported trends.
- schema:
  - `type`: table
  - `required_columns`: `loading`, `heat`, `model`
  - `units`:
    - `loading`: molecules per unit cell
    - `heat`: kJ/mol

Notes: The CSV files must contain rows for all model identifiers listed in the step descriptions. The checker validates the reported loading and heat values, as well as qualitative features (sub‑step detection, monotonicity) against hidden reference data derived from the paper.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "adsorption_isotherms.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure_ratio",
          "loading",
          "model"
        ],
        "units": {
          "pressure_ratio": "dimensionless (p/p0)",
          "loading": "molecules per unit cell"
        }
      },
      "description": "Simulated adsorption isotherms for all zeolite models. The hidden checker compares loading values to paper‑reported gold with tolerances and performs structural checks (sub‑step presence/absence)."
    },
    {
      "file": "isosteric_heat.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "loading",
          "heat",
          "model"
        ],
        "units": {
          "loading": "molecules per unit cell",
          "heat": "kJ/mol"
        }
      },
      "description": "Isosteric heat of adsorption curves for all zeolite models. The hidden checker compares heat values at specified loadings to paper‑reported trends."
    }
  ],
  "notes": "The CSV files must contain rows for all model identifiers listed in the step descriptions. The checker validates the reported loading and heat values, as well as qualitative features (sub‑step detection, monotonicity) against hidden reference data derived from the paper."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that reads your output CSVs and compares the data to hidden reference criteria. No network calls or re‑running of the GCMC code are performed during scoring; the verifier only inspects the numbers and trends you provide.

The scorer checks each required artifact independently. For adsorption_isotherms.csv, it compares your reported loading at specific pressure ratios to a hidden gold (± tolerance), and it performs structural checks on the shape of the isotherm (sub‑step detection). For isosteric_heat.csv, it compares your heat values at designated loadings to a hidden gold (± tolerance) and verifies the qualitative trends (monotonicity, plateau/drop behaviour). A separate structural check confirms that the required model labels are present and that each condition contains enough data points to resolve the key features.

The scores from these components are combined into a single reward value between 0 and 1. The tolerances are chosen to absorb inevitable numerical differences between honest implementations (e.g., from different GCMC codes or random seeds), so simply copying a single number from another source will not satisfy all the checks simultaneously. You must compute the full isotherm and heat curves from scratch using the specified force fields and simulation protocol.

# Zeolite Screening for Adsorption and Diffusion of SO2, CO2, and CO via GCMC Simulations

## Problem background
Zeolites are crystalline aluminosilicates with tunable pore structures that can selectively adsorb gas molecules, making them promising sorbents for removing SO₂ from flue gas streams that also contain CO₂ and CO. The separation performance depends on the detailed pore topology (channels vs. interconnected cages, dimensionality) and on local structural features such as side pockets, channel intersections, and cage windows. Molecular simulations offer a way to screen many zeolite frameworks and compute adsorption and diffusion properties that guide the selection of optimal materials. This task reproduces the key computational screening results for a representative set of all‑silica zeolites, investigating how pore volume, topology, and local features control adsorption heats, loadings, selectivities, and diffusion rates.

## Approach
The zeolites are modelled as all‑silica rigid frameworks with charges assigned to oxygen and silicon atoms. Molecular interactions are described by a Lennard‑Jones (12‑6) potential and Coulomb electrostatics. The pairwise parameters for gas‑gas and gas‑framework interactions are taken from the force field listed below; a cut‑off distance of 12 Å is used and Coulombic interactions are computed via Ewald summation.

Adsorption at infinite dilution (isosteric heat Qst and Henry coefficient) is obtained through Widom test‑particle insertion in the Grand‑Canonical Monte Carlo (GCMC) ensemble at 298 K. Finite‑pressure adsorption of a ternary SO₂/CO₂/CO mixture (20 %/40 %/40 %) is simulated using GCMC at 298 K and 1 bar. Self‑diffusion coefficients for SO₂ and CO₂ are extracted from the mean‑square displacement measured in canonical‑ensemble molecular dynamics (MD) runs that start from GCMC‑equilibrated configurations. Low‑coverage (single‑molecule) GCMC simulations are used to generate two‑dimensional centre‑of‑mass density profiles for selected zeolites.

Prior to the simulations, each zeolite structure is characterised with Zeo++ to obtain the accessible pore volume, surface area, and pore‑system classification (channel vs. cage, dimensionality). The comparison of computed heats of adsorption with pore volumes reveals how local geometric features modify the global trends.

**Force field parameters**

Lennard‑Jones parameters and partial charges of the adsorbed molecules and the zeolite framework are specified below. ε/kB is in Kelvin, σ in Å, and charge in e.

| Atom pair           | ε/kB (K) | σ (Å) | charge (e) |
|---------------------|----------|-------|-------------|
| C(CO₂)–C(CO₂)       | 29.933   | 2.745 | 0.651       |
| O(CO₂)–O(CO₂)       | 85.671   | 3.017 | −0.326      |
| C(CO)–C(CO)         | 16.141   | 3.658 | −0.242      |
| O(CO)–O(CO)         | 98.014   | 2.979 | −0.274      |
| Dum(CO)–Dum(CO)     | —        | —     | 0.517       |
| S(SO₂)–S(SO₂)       | 189.353  | 3.41  | 0.402       |
| O(SO₂)–O(SO₂)       | 58.725   | 3.198 | −0.201      |
| O(zeo)–O(zeo)       | —        | —     | −0.393      |
| Si(zeo)–Si(zeo)     | —        | —     | 0.786       |
| C(CO₂)–O(zeo)       | 37.595   | 3.511 | —           |
| O(CO₂)–O(zeo)       | 78.98    | 3.237 | —           |
| C(CO)–O(zeo)        | 40.109   | 3.379 | —           |
| O(CO)–O(zeo)        | 98.839   | 3.057 | —           |
| S(SO₂)–O(zeo)       | 138.555  | 3.168 | —           |
| O(SO₂)–O(zeo)       | 77.161   | 3.066 | —           |

Lennard‑Jones cross‑interactions between dissimilar atoms are obtained from Lorentz–Berthelot mixing rules unless explicitly listed above. The dum(CO) site has zero Lennard‑Jones parameters and is used only for charge distribution; its interactions with all atoms, including O(zeo), are omitted.

## Reproduction target
Produce the following quantitative results for all 39 zeolites listed below (the full set studied, spanning channel-type and interconnected-cage topologies with 1D, 2D and 3D pore systems).

**1D channels**: ASV, DON, ITW, JRY, LAU, LTL, MOR, NAT, PON
**2D channels**: AFR, FER, IWV, NES, SFO, SFG, TER
**3D channels**: AFY, BEC, BOG, MEL, MFI, ITR, SBT, STW, SZR
**1D interconnected cages**: ITQ-3, MTF, SAS
**2D interconnected cages**: DDR, LEV, MWW
**3D interconnected cages**: CHA, ERI, FAU, ITQ-29, KFI, PAU, RHO, SBE

1. Isosteric heat of adsorption (Qst, kJ/mol) and Henry coefficient (mol/(kg·Pa)) for SO₂, CO₂, and CO at 298 K.
2. Adsorbed loading of each component in the ternary mixture (20 % SO₂, 40 % CO₂, 40 % CO) at 298 K and 1 bar, in mol/kg.
3. Self‑diffusion coefficients D (10⁻⁸ m²/s) for SO₂ and CO₂ extracted from MD of the ternary mixture at the same loading.
4. Two‑dimensional centre‑of‑mass density profiles for MOR, AFY, and KFI at low coverage for each of the three gases, normalised to a maximum of 1.0.

Using your computed pore volumes from Zeo++, examine the relationship between isosteric heat of adsorption and pore volume, and identify any zeolites whose Qst deviates from the general trend due to local pore features.

## Assets

- IZA-SC Zeolite Structure Database: http://www.iza-structure.org/databases/
- Zeo++: https://github.com/tfwilliams/Zeopp/
- RASPA2: https://github.com/numat/RASPA2

## Workflow steps

### Step 1: Pore characterization with Zeo++
- Role: process
- Action: Download the required zeolite structures from the IZA database. Run Zeo++ to compute pore volume, surface area, and classify each as channel or interconnected-cage system with dimensionality. Save the characterization data for later analysis.
- Evidence: `/app/outputs/zeolite_properties.csv`

### Step 2: Compute isosteric heats and Henry coefficients
- Role: scored (load-bearing)
- Action: Using the Lennard-Jones and Coulomb force-field parameters provided in the task description (adsorbates and zeolite oxygen atoms), run Widom test-particle insertion at 298 K for SO2, CO2 and CO in every required zeolite. Compute the isosteric heat of adsorption (Qst, kJ/mol) and Henry coefficient (mol/(kg·Pa)) for each gas. Output a CSV with one row per zeolite.
- Output file: `/app/outputs/heats_henry.csv`
- Format: csv
- Contract: CSV columns: zeolite (string), Qst_SO2 (float, kJ/mol), Qst_CO2 (float, kJ/mol), Qst_CO (float, kJ/mol), Henry_SO2 (float, mol/(kg*Pa)), Henry_CO2 (float, mol/(kg*Pa)), Henry_CO (float, mol/(kg*Pa)). One row per studied zeolite.
- Scoring: scored by hidden verifier

### Step 3: Ternary mixture adsorption loading
- Role: scored
- Action: Perform GCMC simulations for a ternary mixture of SO2 (20%), CO2 (40%), CO (40%) at 298 K and 1 bar for each zeolite. Compute the adsorbed loading (mol/kg) for each component. Output a CSV with one row per zeolite.
- Output file: `/app/outputs/loading_ternary.csv`
- Format: csv
- Contract: CSV columns: zeolite (string), loading_SO2 (float, mol/kg), loading_CO2 (float, mol/kg), loading_CO (float, mol/kg). One row per studied zeolite.
- Scoring: scored by hidden verifier

### Step 4: Self-diffusion coefficients from MD
- Role: scored
- Action: Starting from equilibrated GCMC configurations of the ternary mixture, run molecular dynamics (MD) in the canonical ensemble at 298 K. Compute the mean-square displacement of SO2 and CO2 and extract the self-diffusion coefficient D (10⁻⁸ m²/s). Output for all zeolites listed in the task.
- Output file: `/app/outputs/diffusion_coefficients.csv`
- Format: csv
- Contract: CSV columns: zeolite (string), D_SO2 (float, 10⁻⁸ m²/s), D_CO2 (float, 10⁻⁸ m²/s). One row per zeolite.
- Scoring: scored by hidden verifier

### Step 5: Occupation density profiles
- Role: scored
- Action: For zeolites MOR, AFY, and KFI, run low-coverage GCMC (one molecule) and generate 2D centre-of-mass density histograms projected onto the following planes: MOR y‑z, AFY x‑y, KFI x‑y for each gas (SO2, CO2, CO). Normalise the maximum density to 1.0 in each file. Bundle the nine text files into a ZIP archive.
- Output file: `/app/outputs/occupation_profiles.zip`
- Format: other
- Contract: ZIP containing nine text files named <zeolite>_<gas>.txt (e.g. MOR_SO2.txt). Each file: first line 'zeolite gas', second line 'n_x n_y x_min x_max y_min y_max', then n_x lines of n_y space-separated density values. Maximum density = 1.0.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/heats_henry.csv`
- `/app/outputs/loading_ternary.csv`
- `/app/outputs/diffusion_coefficients.csv`
- `/app/outputs/occupation_profiles.zip`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### heats_henry.csv
- path: `/app/outputs/heats_henry.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Isosteric heats of adsorption (kJ/mol) and Henry coefficients (mol/(kg*Pa)) at 298 K. One row per zeolite.
- schema:
  - `type`: table
  - `required_columns`: `zeolite`, `Qst_SO2`, `Qst_CO2`, `Qst_CO`, `Henry_SO2`, `Henry_CO2`, `Henry_CO`
  - `units`:
    - `Qst_SO2`: kJ/mol
    - `Qst_CO2`: kJ/mol
    - `Qst_CO`: kJ/mol
    - `Henry_SO2`: mol/(kg*Pa)
    - `Henry_CO2`: mol/(kg*Pa)
    - `Henry_CO`: mol/(kg*Pa)

### loading_ternary.csv
- path: `/app/outputs/loading_ternary.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Adsorbed loadings from ternary mixture (20% SO2, 40% CO2, 40% CO) at 298 K and 1 bar. One row per zeolite.
- schema:
  - `type`: table
  - `required_columns`: `zeolite`, `loading_SO2`, `loading_CO2`, `loading_CO`
  - `units`:
    - `loading_SO2`: mol/kg
    - `loading_CO2`: mol/kg
    - `loading_CO`: mol/kg

### diffusion_coefficients.csv
- path: `/app/outputs/diffusion_coefficients.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Self-diffusion coefficients of SO2 and CO2 from MD simulations of the ternary mixture at 298 K. One row per zeolite.
- schema:
  - `type`: table
  - `required_columns`: `zeolite`, `D_SO2`, `D_CO2`
  - `units`:
    - `D_SO2`: 10⁻⁸ m²/s
    - `D_CO2`: 10⁻⁸ m²/s

### occupation_profiles.zip
- path: `/app/outputs/occupation_profiles.zip`
- format: other
- purpose: scored
- target_policy: reference_match
- description: 2D centre-of-mass density projections for MOR (y-z plane), AFY (x-y), KFI (x-y) with SO2, CO2, CO. Density normalised to 1.0 maximum.
- schema:
  - `type`: other
  - `description`: ZIP archive containing nine text files (one per zeolite/gas combination). Each file: first line 'zeolite gas', second line 'n_x n_y x_min x_max y_min y_max', then n_x lines of n_y space-separated density values. Maximum density = 1.0.

Notes: The force-field parameters (Lennard-Jones and Coulomb) are fully specified in the task instruction. The agent must use the same set of zeolites as listed in the instruction for steps 2–4, and only MOR, AFY, KFI for step 5.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "heats_henry.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "zeolite",
          "Qst_SO2",
          "Qst_CO2",
          "Qst_CO",
          "Henry_SO2",
          "Henry_CO2",
          "Henry_CO"
        ],
        "units": {
          "Qst_SO2": "kJ/mol",
          "Qst_CO2": "kJ/mol",
          "Qst_CO": "kJ/mol",
          "Henry_SO2": "mol/(kg*Pa)",
          "Henry_CO2": "mol/(kg*Pa)",
          "Henry_CO": "mol/(kg*Pa)"
        }
      },
      "description": "Isosteric heats of adsorption (kJ/mol) and Henry coefficients (mol/(kg*Pa)) at 298 K. One row per zeolite."
    },
    {
      "file": "loading_ternary.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "zeolite",
          "loading_SO2",
          "loading_CO2",
          "loading_CO"
        ],
        "units": {
          "loading_SO2": "mol/kg",
          "loading_CO2": "mol/kg",
          "loading_CO": "mol/kg"
        }
      },
      "description": "Adsorbed loadings from ternary mixture (20% SO2, 40% CO2, 40% CO) at 298 K and 1 bar. One row per zeolite."
    },
    {
      "file": "diffusion_coefficients.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "zeolite",
          "D_SO2",
          "D_CO2"
        ],
        "units": {
          "D_SO2": "10⁻⁸ m²/s",
          "D_CO2": "10⁻⁸ m²/s"
        }
      },
      "description": "Self-diffusion coefficients of SO2 and CO2 from MD simulations of the ternary mixture at 298 K. One row per zeolite."
    },
    {
      "file": "occupation_profiles.zip",
      "format": "other",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "other",
        "description": "ZIP archive containing nine text files (one per zeolite/gas combination). Each file: first line 'zeolite gas', second line 'n_x n_y x_min x_max y_min y_max', then n_x lines of n_y space-separated density values. Maximum density = 1.0."
      },
      "description": "2D centre-of-mass density projections for MOR (y-z plane), AFY (x-y), KFI (x-y) with SO2, CO2, CO. Density normalised to 1.0 maximum."
    }
  ],
  "notes": "The force-field parameters (Lennard-Jones and Coulomb) are fully specified in the task instruction. The agent must use the same set of zeolites as listed in the instruction for steps 2–4, and only MOR, AFY, KFI for step 5."
}
```

## How you are scored
Your submission is evaluated by a hidden automated checker. For each scored output file the checker extracts the reported values and compares them to hidden reference data (derived from the paper’s simulations) using appropriate tolerances. The comparison accounts for run‑to‑run stochastic variation by using relative or absolute tolerances that a faithful re‑run can meet. For the occupation profiles the checker computes a spatial correlation coefficient between your density map and a reference map; a correlation above a hidden threshold is required. In addition, the checker analyses your heats of adsorption together with your pore volumes to verify that the structure‑property trends (the relationship between heat and pore volume, and the existence of outliers due to local pockets or windows) are correctly reproduced. Each artifact receives a score between 0 and 1, and the final reward is a weighted sum of these scores. The precise tolerances, reference values, and weights are hidden; to earn full credit, follow the workflow faithfully and produce accurate simulation results.

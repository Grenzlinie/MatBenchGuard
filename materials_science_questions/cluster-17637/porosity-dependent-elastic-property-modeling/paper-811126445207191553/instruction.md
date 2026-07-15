# Silicon Inverse Opal SBS Gain Reproduction

## Problem background
Stimulated Brillouin scattering (SBS) in silicon integrated waveguides is severely limited by silicon's high mechanical stiffness, low photoelasticity, and high acoustic losses compared with chalcogenide glasses. Structuring bulk silicon into a porous metamaterial—specifically an FCC lattice of interpenetrating spherical pores (an inverse opal)—reduces the effective stiffness and acoustic losses, potentially enhancing the material's bulk SBS gain coefficient by orders of magnitude. The core question is: what are the effective bulk SBS gain coefficients of silicon inverse opals at different porosities, and can a waveguide that combines a porous silicon core with a thin unstructured silicon shell embedded in fused silica achieve a guided SBS gain comparable to chalcogenide waveguide platforms?

## Approach
The reproduction proceeds in two stages. First, unit‑cell finite‑element simulations of the silicon inverse opal at several porosities are used to extract the effective material parameters: refractive index, photoelastic coefficients, mass density, elastic stiffness tensor elements, longitudinal acoustic velocity, Brillouin linewidth, and phonon viscosity tensor. These are then inserted into the bulk SBS gain formula to obtain the gain coefficient as a function of porosity, together with a baseline value for bulk (non‑porous) silicon computed from literature constants. Second, the effective parameters are used in a waveguide cross‑section model (fixed width 550 nm, height 500 nm, fused silica substrate) with a porous core and a concentric crystalline silicon shell. For each (porosity, shell thickness) pair the optical and acoustic guided modes are solved, the opto‑acoustic overlap integral is evaluated, and the guided SBS gain coefficient is calculated. A parameter sweep over porosities from 75 % to 85 % and shell thicknesses from 20 nm to 80 nm reveals the optimum design. All computations can be performed with an open‑source finite‑element solver; material constants for crystalline silicon and fused silica are available in standard handbooks.

## Reproduction target
Produce two scored CSV files. (1) `bulk_gain.csv`: the bulk SBS gain coefficient of silicon inverse opals at several porosities, including at least the non‑porous silicon case and a porosity of 85 %. (2) `waveguide_sweep.csv`: guided SBS gain coefficient from a parameter sweep of at least 20 distinct (porosity, shell thickness) pairs covering porosities 0.75–0.85 and shell thicknesses 20–80 nm. The hidden verifier will check that the bulk gain at high porosity is substantially larger than that of pure silicon and that the waveguide sweep exhibits an interior maximum consistent with an optimised design.

## Assets

- Open-source finite element solver (e.g., FEniCS, deal.II, Elmer): https://fenicsproject.org/
- Material constants for crystalline silicon and fused silica

## Workflow steps

### Step 1: Unit cell simulation and bulk SBS gain
- Role: scored
- Action: Model the FCC inverse opal unit cell of silicon with interpenetrating spherical pores at porosities f=75%, 80%, 85%. The unit cell lattice period d = 50 nm; for each porosity, set the sphere radius a = 17.754 nm (f=75%), 18.1818 nm (f=80%), and 18.6646 nm (f=85%). Use open-source FEM to extract effective optical (refractive index, photoelastic coefficient p12) and acoustic (mass density, stiffness C11, C12, C44, longitudinal acoustic velocity V_A, Brillouin linewidth Gamma_B, phonon viscosity) parameters. Compute the bulk SBS gain coefficient g_P = (4 pi^2 gamma_12^2) / (n c lambda_1^2 rho V_A Gamma_B) with gamma_12 = p12 n^4. Also compute g_P for bulk silicon (f=0) using literature constants. Save all effective parameters to effective_params.json, and write g_P vs. f to bulk_gain.csv.
- Output file: `/app/outputs/bulk_gain.csv`
- Format: csv
- Contract: Two columns: 'f' (float, porosity fraction) and 'g_P' (float, bulk SBS gain in W^{-1}m). Must include rows for f=0 and at least f=0.85.
- Scoring: scored by hidden verifier

### Step 2: Waveguide SBS gain sweep
- Role: scored (load-bearing)
- Action: Using effective parameters from step1 (effective_params.json), model the waveguide cross-section (width 550 nm, height 500 nm) with a porous core of porosity f and unstructured crystalline silicon shell of thickness d, embedded in fused silica. Perform a parameter sweep over f from 0.75 to 0.85 and d from 20 to 80 nm (at least 20 distinct (f,d) pairs). For each pair compute optical mode, acoustic mode, opto-acoustic overlap integral, optical energy flux P, acoustic energy density U_A, acoustic quality factor Q_A, and the guided SBS gain g_P^wg = (4 pi c / (lambda_1 |P| U_A)) |xi|^2 Q_A. Write the (f, d_nm, g_P_wg) data to waveguide_sweep.csv.
- Output file: `/app/outputs/waveguide_sweep.csv`
- Format: csv
- Contract: Three columns: 'f' (float, porosity), 'd_nm' (float, shell thickness in nm), 'g_P_wg' (float, waveguide SBS gain in W^{-1}m^{-1}). Must contain at least 20 data points covering f in [0.75, 0.85] and d_nm in [20, 80].
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bulk_gain.csv`
- `/app/outputs/waveguide_sweep.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bulk_gain.csv
- path: `/app/outputs/bulk_gain.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Bulk SBS gain coefficient of silicon inverse opals at porosities f=0, 0.75, 0.80, 0.85. The checker compares the reported g_P values against hidden reference values and verifies the enhancement ratio relative to pure silicon.
- schema:
  - `type`: table
  - `required_columns`: `f`, `g_P`
  - `units`:
    - `f`: dimensionless
    - `g_P`: W^{-1}m

### waveguide_sweep.csv
- path: `/app/outputs/waveguide_sweep.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Parameter sweep of waveguide SBS gain coefficient. The checker locates the maximum gain and verifies that its value and optimal (f,d) coordinates lie within acceptable ranges of the paper's optimum.
- schema:
  - `type`: table
  - `required_columns`: `f`, `d_nm`, `g_P_wg`
  - `units`:
    - `f`: dimensionless
    - `d_nm`: nm
    - `g_P_wg`: W^{-1}m^{-1}

Notes: The effective_params.json file is an intermediate artifact, not scored. The agent must use it as input for the waveguide step. The instruction will provide reference material constants for silicon and fused silica.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bulk_gain.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "f",
          "g_P"
        ],
        "units": {
          "f": "dimensionless",
          "g_P": "W^{-1}m"
        }
      },
      "description": "Bulk SBS gain coefficient of silicon inverse opals at porosities f=0, 0.75, 0.80, 0.85. The checker compares the reported g_P values against hidden reference values and verifies the enhancement ratio relative to pure silicon."
    },
    {
      "file": "waveguide_sweep.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "f",
          "d_nm",
          "g_P_wg"
        ],
        "units": {
          "f": "dimensionless",
          "d_nm": "nm",
          "g_P_wg": "W^{-1}m^{-1}"
        }
      },
      "description": "Parameter sweep of waveguide SBS gain coefficient. The checker locates the maximum gain and verifies that its value and optimal (f,d) coordinates lie within acceptable ranges of the paper's optimum."
    }
  ],
  "notes": "The effective_params.json file is an intermediate artifact, not scored. The agent must use it as input for the waveguide step. The instruction will provide reference material constants for silicon and fused silica."
}
```

## How you are scored
Each scored artifact is evaluated independently by a hidden verifier. For `bulk_gain.csv` the verifier examines the required columns and the relative enhancement between the porous and non‑porous cases, comparing the reported gain value at a specified porosity against a hidden reference tolerance. For `waveguide_sweep.csv` the verifier checks the required columns, verifies that at least 20 distinct (f, d_nm) points are present, locates the maximum gain value, and confirms that it lies in the expected region of the parameter space (not at the boundary). The quantitative checks are combined into a final reward between 0 and 1; delivering the correct intermediate effective parameters and executing all stages of the workflow is necessary to satisfy the checks.

# Mesoscopic Representative Volume Size and Effective Elastic Moduli of Bimodal Porous Materials

## Problem background
Porous ceramics, such as those based on nanocrystalline metal oxides, often exhibit a bimodal pore size distribution with distinct large and small pores. Understanding how the ratio of large to small pores affects the effective elastic modulus is critical for tailoring materials to functional applications. This study addresses the question of what size of a mesoscopic volume is locally representative—the smallest volume whose effective elastic response captures the bulk behavior—and how the effective Young's modulus varies with the relative content of large and small pores. The model material has a total porosity of 55% and a large-to-small pore diameter ratio of 8:1. The matrix and pores are assigned distinct isotropic elastic constants.

## Approach
The investigation proceeds by constructing numerical models of a porous medium with bimodal spherical voids. A large parent cubic volume (side length at least 25 times the large-pore diameter) is filled with random arrangements of large and small pores such that the total porosity is 55%. Four volume compositions are considered: large pores occupy 80%, 60%, 40%, or 20% of the total pore volume, with small pores making up the remainder. For each composition, cubic subvolumes (mesoscale volumes) of varying side lengths L are extracted from random positions; the linear size is expressed in dimensionless form L/d, where d is the large-pore diameter. The sizes range from 0.8 to 24, covering the onset of local representativeness. A total of 300 independent mesoscale volumes are generated for each composition and each size. Each mesoscale volume is meshed and subjected to a uniaxial linear elastic finite-element simulation along the y-direction, using matrix Young's modulus E_m = 40 GPa, matrix Poisson ratio ν_m = 0.22, inclusion Young's modulus E_i = 0.1 GPa, and inclusion Poisson ratio ν_i = 0.2. The effective Young's modulus of each volume is computed from the average normal stress and strain (E_eff = ⟨σ_y⟩/⟨ε_y⟩). This yields 300 local modulus values for every (composition, L/d) combination. To determine the locally representative volume size, the two-point correlation function R of the local moduli is calculated for each L/d across all compositions. The correlation measures how strongly the local moduli of two points are related; it increases with L/d. The smallest L/d at which R approaches unity (R→1) is identified as the normalized MRV side length L_f/d. Finally, using the identified MRV size, the 300 local moduli for each of the four compositions are averaged to obtain the effective Young's modulus for that pore composition.

## Reproduction target
Produce the following two results:
1. The locally representative mesoscopic volume side length normalized by the large-pore diameter, L_f/d, reported as a JSON object {"L_f_d": <value>}.
2. The effective Young's modulus E_eff (in GPa) for each of the four pore volume compositions at that MRV size, written to a CSV file with columns type, C_D_percent, C_d_percent, E_eff_GPa. The four rows correspond to:
   - type 1: large pores 80%, small pores 20%
   - type 2: large pores 60%, small pores 40%
   - type 3: large pores 40%, small pores 60%
   - type 4: large pores 20%, small pores 80%

## Assets

- Open-source Finite Element Analysis software (e.g., FEniCS, CalculiX, Elmer): fenics
- Scientific Python packages for geometry generation and analysis: numpy scipy meshio pygmsh

## Workflow steps

### Step 1: Generate bimodal porous microstructures
- Role: process
- Action: Create geometric models of cubic volumes containing bimodal spherical pores. Total porosity C=55%, pore diameter ratio (large to small) = 8:1. Generate models for four compositions: large-pore volume content C_D = 80%, 60%, 40%, 20%; corresponding small-pore content C_d = 20%, 40%, 60%, 80%. For each composition, produce models with normalized side lengths L_f/d (volume side length divided by large pore diameter d) spanning 0.8, 1.6, 2.4, 3.2, 4.0, 6, 8, 10, 12, and 24. For every (composition, L_f/d) pair, generate N=300 random mesoscale volume fragments, each consisting of a cubic subvolume of the given linear size extracted from the full model. The full parent models for each composition should have side length at least 25*d.
- Evidence: `/app/outputs/model_generation.log`

### Step 2: Run FEM simulations and compute local elastic moduli
- Role: process
- Action: For every generated mesoscale volume, perform a linear elastic finite element simulation under uniaxial loading applied along the y-direction. Use matrix Young's modulus E_m = 40 GPa and Poisson's ratio ν_m = 0.22; inclusion (pore) Young's modulus E_i = 0.1 GPa and Poisson's ratio ν_i = 0.2. Discretize each volume and apply displacement boundary conditions corresponding to uniaxial strain. Solve for the stress and strain fields, then compute the effective Young's modulus for that MRV by averaging the normal stress and strain over the volume (E_eff = mean(σ_y) / mean(ε_y)). Store the resulting local effective modulus for each of the 300 samples per (composition, L_f/d) pair.
- Evidence: `/app/outputs/simulation_log.txt`

### Step 3: Determine locally representative volume size via correlation analysis
- Role: scored
- Action: For each L_f/d, use the 300 local effective modulus values from all compositions to compute the two-point correlation function R. The correlation is defined as R = integral of E_I * E_II * f(E_I, E_II) dE_I dE_II, where f is the joint density of local moduli values. The computed R values trace how correlation changes with L_f/d. Identify the smallest L_f/d at which R tends toward unity (R → 1). This value is the locally representative mesoscopic volume size ratio. Report it as a JSON object with key 'L_f_d' in /app/outputs/mrv_size.json.
- Output file: `/app/outputs/mrv_size.json`
- Format: json
- Contract: {"L_f_d": <float>}
- Scoring: scored by hidden verifier

### Step 4: Calculate effective elastic moduli at MRV size
- Role: scored (load-bearing)
- Action: Using the MRV size ratio L_f/d determined in step_03, for each of the four pore compositions, average the 300 local effective modulus values obtained from samples of that size to obtain the effective Young's modulus for the composition. Write a CSV file /app/outputs/effective_moduli.csv with columns: type (integer), C_D_percent (float), C_d_percent (float), E_eff_GPa (float). There must be exactly four rows, one for each composition: type 1 (80/20), type 2 (60/40), type 3 (40/60), type 4 (20/80).
- Output file: `/app/outputs/effective_moduli.csv`
- Format: csv
- Contract: type (integer), C_D_percent (float), C_d_percent (float), E_eff_GPa (float) (four rows)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/mrv_size.json`
- `/app/outputs/effective_moduli.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### mrv_size.json
- path: `/app/outputs/mrv_size.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The smallest normalized side length L_f/d at which the two-point correlation function of local elastic moduli approaches unity, i.e., the locally representative mesoscopic volume size.
- schema:
  - `type`: object
  - `required`:
    - `L_f_d`: number

### effective_moduli.csv
- path: `/app/outputs/effective_moduli.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Effective Young's modulus for the four pore compositions at the determined MRV size. Four rows, one per model type (1-4).
- schema:
  - `type`: table
  - `required_columns`: `type`, `C_D_percent`, `C_d_percent`, `E_eff_GPa`
  - `units`:
    - `E_eff_GPa`: GPa

Notes: The hidden checker compares the MRV size ratio to the paper-reported value within a tolerance, and the effective moduli to known reference values with a relative tolerance. The solving agent must execute all process steps (model generation and FEM) to obtain the results; the final scores are based solely on these two output artifacts.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "mrv_size.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "L_f_d": "number"
        }
      },
      "description": "The smallest normalized side length L_f/d at which the two-point correlation function of local elastic moduli approaches unity, i.e., the locally representative mesoscopic volume size."
    },
    {
      "file": "effective_moduli.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "type",
          "C_D_percent",
          "C_d_percent",
          "E_eff_GPa"
        ],
        "units": {
          "E_eff_GPa": "GPa"
        }
      },
      "description": "Effective Young's modulus for the four pore compositions at the determined MRV size. Four rows, one per model type (1-4)."
    }
  ],
  "notes": "The hidden checker compares the MRV size ratio to the paper-reported value within a tolerance, and the effective moduli to known reference values with a relative tolerance. The solving agent must execute all process steps (model generation and FEM) to obtain the results; the final scores are based solely on these two output artifacts."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that inspects the two scored output files (`/app/outputs/mrv_size.json` and `/app/outputs/effective_moduli.csv`). The verifier compares your reported L_f/d to a hidden gold value (obtained from the published study) with a tolerance; a result within the tolerance band earns full credit, and credit diminishes linearly outside it. Similarly, each of the four effective moduli is compared to its hidden gold value with a relative tolerance; full credit is given if the deviation is within the tolerance, and credit decays linearly otherwise. The final reward is a weighted average of the scores from these two artifacts, so both must be correct to achieve a high score. Simply hardcoding the paper's numbers may match the gold, but the tolerances are set so that only a legitimate reproduction that follows the described workflow can reliably pass both checks.

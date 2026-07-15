# Diffusion and stability parameters of He and He-H clusters in tungsten from MD simulations

## Problem background
Tungsten is a leading candidate for plasma-facing components in fusion reactors, where it will be subjected to fluxes of hydrogen (H) and helium (He). These species can form small clusters within the material, and understanding the mobility of such clusters — how fast they diffuse and whether they dissociate — is critical for predicting material degradation over time. The key quantities that characterize cluster transport are the migration barrier (activation energy for diffusion) and, for clusters that can break apart, the dissolution energy. This task asks you to reproduce these quantities for a set of pure He and mixed He-H clusters in bulk tungsten using atomistic simulations.

## Approach
The reproduction uses classical molecular dynamics (MD) with an embedded atom method (EAM) interatomic potential for the W-He-H system. Starting from a bulk bcc tungsten simulation cell with periodic boundaries, stable configurations of each cluster are obtained by inserting the appropriate atoms and performing a short thermalization plus quench. Finite-temperature NVE MD runs are then carried out at several temperatures to generate atomic trajectories. From these trajectories, diffusion coefficients are extracted via the Einstein relation and the independent interval method (IIM), which also provides error estimates. For mixed clusters, the method further identifies time intervals where the cluster remains intact and computes a decay frequency. Finally, Arrhenius relations are fitted (using weighted least squares) to the temperature-dependent diffusion coefficients and decay frequencies, yielding migration barriers and dissolution energies with their uncertainties.

## Reproduction target
Produce a file named `migration_parameters.json` in the output directory. This file must contain, for each of the following cluster types, the migration barrier (eV) and its error, and (for mixed clusters) the dissolution energy (eV) and its error. Pure He clusters have no dissolution energy; set those entries to null. The required cluster types are: 1He, 2He, 3He, 4He, 1He-1H, 1He-2H, 2He-1H, 2He-2H, 3He-1H. All numeric values must be reported with at least two decimal places. The JSON structure should be an array of objects with keys `cluster`, `migration_barrier`, `migration_barrier_error`, `dissolution_energy`, and `dissolution_energy_error`.

## Assets

- LAMMPS molecular dynamics simulator: https://lammps.sandia.gov/
- EAM2 interatomic potential for W-He-H (Bonny et al., J. Phys.: Condens. Matter 26 (2014) 485001)

## Workflow steps

### Step 1: Generate stable cluster configurations
- Role: process
- Action: Construct a bcc W simulation cell (10×10×10 lattice units, a0=3.14 Å) with periodic boundaries. For each cluster type (1He, 2He, 3He, 4He, 1He-1H, 1He-2H, 2He-1H, 2He-2H, 3He-1H), insert the appropriate atoms and perform a short MD run at 300 K followed by a quench (conjugate gradient) to obtain the most stable configuration. Save the relaxed coordinates for later MD simulations.
- Evidence: `/app/outputs/cluster_relaxed_coords.log`

### Step 2: Run finite-temperature MD simulations
- Role: process
- Action: For each stable cluster configuration, run NVE MD simulations over a temperature range of 200–1700 K using the EAM2 potential. Use timesteps 0.1–1 fs and simulation times 5–25 ns, thermalizing and zero-pressure setting via Berendsen before each NVE run. Track atomic trajectories and cluster composition.
- Evidence: `/app/outputs/md_runs.log`

### Step 3: Extract diffusion coefficients and decay frequencies via IIM
- Role: process
- Action: From the MD trajectories, compute diffusion coefficients D(T) using Einstein relation and mean-square displacement. Apply the independent interval method (IIM) to obtain D and its uncertainty (standard deviation of the mean) for each cluster and temperature. For mixed clusters, identify stable-cluster intervals, compute the average stable-segment duration, derive the decay frequency ν(T)=1/t_bar, and propagate uncertainties. Collect the temperature-dependent D(T) and ν(T) data for all clusters.
- Evidence: `/app/outputs/diffusion_data.csv`

### Step 4: Fit Arrhenius parameters and output migration/dissolution energies
- Role: scored (load-bearing)
- Action: For each cluster type, fit Arrhenius expressions D(T)=D0 exp(-E_m/(k_B T)) and (for mixed clusters) ν(T)=ν0 exp(-E_d/(k_B T)) to the IIM data using weighted least squares (weights = 1/σ²). Extract migration barriers E_m, dissolution energies E_d, and their uncertainties. For pure He clusters, dissolution energies are not applicable (set to null). Write the full set of fitted parameters for all clusters to a JSON file.
- Output file: `/app/outputs/migration_parameters.json`
- Format: json
- Contract: Array of objects, each with fields: cluster (string, e.g., '1He', '2He-1H'), migration_barrier (float, eV), migration_barrier_error (float or null, eV), dissolution_energy (float or null, eV), dissolution_energy_error (float or null, eV). Clusters to include: 1He,2He,3He,4He,1He-1H,1He-2H,2He-1H,2He-2H,3He-1H. All numeric values with at least two decimal places.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/migration_parameters.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### migration_parameters.json
- path: `/app/outputs/migration_parameters.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Fitted migration barriers and dissolution energies for He and He-H clusters in tungsten, obtained from MD simulations and Arrhenius analysis.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `properties`:
      - `cluster`:
        - `type`: string
      - `migration_barrier`:
        - `type`: number
        - `unit`: eV
      - `migration_barrier_error`:
        - `type`: number
        - `unit`: eV
        - `nullable`: True
      - `dissolution_energy`:
        - `type`: number
        - `unit`: eV
        - `nullable`: True
      - `dissolution_energy_error`:
        - `type`: number
        - `unit`: eV
        - `nullable`: True
    - `required`: `cluster`, `migration_barrier`

Notes: The hidden checker retrieves the paper's reported migration barriers and dissolution energies (Table 1) and compares them with the agent's reported parameters using absolute and relative tolerances, plus a check of relative trends (pure He barriers increasing with size; mixed clusters higher than corresponding pure He clusters).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "migration_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "cluster": {
              "type": "string"
            },
            "migration_barrier": {
              "type": "number",
              "unit": "eV"
            },
            "migration_barrier_error": {
              "type": "number",
              "unit": "eV",
              "nullable": true
            },
            "dissolution_energy": {
              "type": "number",
              "unit": "eV",
              "nullable": true
            },
            "dissolution_energy_error": {
              "type": "number",
              "unit": "eV",
              "nullable": true
            }
          },
          "required": [
            "cluster",
            "migration_barrier"
          ]
        }
      },
      "description": "Fitted migration barriers and dissolution energies for He and He-H clusters in tungsten, obtained from MD simulations and Arrhenius analysis."
    }
  ],
  "notes": "The hidden checker retrieves the paper's reported migration barriers and dissolution energies (Table 1) and compares them with the agent's reported parameters using absolute and relative tolerances, plus a check of relative trends (pure He barriers increasing with size; mixed clusters higher than corresponding pure He clusters)."
}
```

## How you are scored
A hidden verifier will read your `migration_parameters.json` and compare each reported quantity to reference values derived from the underlying research. The verifier will also check that the relationships among the reported barriers (e.g., how they vary with cluster size and composition) are physically consistent. Both the absolute accuracy of the values and the structural trends contribute to your final score, which is a single number between 0 (no credit) and 1 (full credit). The exact tolerances and trend checks are not disclosed; simply perform the computations as accurately as the workflow allows. You do not need to know the reference values in advance — the scoring experiment evaluates your output against a fixed, hidden standard.

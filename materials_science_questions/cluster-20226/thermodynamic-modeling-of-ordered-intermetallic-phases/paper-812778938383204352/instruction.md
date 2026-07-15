# SKMF Validation: Wagner Diffusivity Consistency for A3B and AB Phases

## Problem background
When two elements A and B react in the solid state, several ordered intermediate phases can form in the diffusion zone, and their competition determines the final microstructure and properties of joints, thin films, and composites. Predicting which phases appear and how fast they grow requires a quantitative description of phase nucleation and growth kinetics. A stochastic kinetic mean‑field (SKMF) model, which extends deterministic kinetic mean‑field theory by adding frequency noise, has been proposed to capture first‑order phase transitions and nucleation. The pair interaction parameters that define the model are known: V_AA^I = V_BB^I = –1×10⁻²¹ J, V_AB^I = –3.9×10⁻²¹ J, V_AA^II = V_BB^II = –8.76×10⁻²¹ J, V_AB^II = –2×10⁻²¹ J, and the temperature is T = 750 K. The goal is to validate the internal consistency of the SKMF approach by computing the Wagner integrated diffusion coefficient (D_W) for the ordered A3B and AB phases from two independent methods and assessing their agreement.

## Approach
The approach combines thermodynamic equilibrium calculations with kinetic simulations. First, the equilibrium concentration ranges of all phases (disordered A(B) solution, AB3, AB, A3B, B(A) solution) are obtained via the common‑tangent rule using the mean‑field Gibbs free energy expressions for the disordered phase, the L1₂ ordered phase, and the L1₀ ordered phase, with interactions up to the second coordination shell. Second, the SKMF method is employed: the model evolves site occupation probabilities under exchange jump frequencies that include a Langevin noise term to enable nucleation. Two types of diffusion couples are simulated for each of the phases A3B and AB. 

(i) Growth‑derived D_W: an incremental couple (A–AB for A3B, A3B–AB3 for AB) is set up to grow a single phase layer. The squared relative phase quantity ξ² is monitored; after an initial transient it follows a parabolic law ξ² = k·t/dt, from which the parabolic rate constant k is extracted. The Wagner diffusivity is then computed as D_W = k·L²/(64·dt), where L is the system length. 

(ii) Matano‑derived D_W: a separate couple with initial compositions equal to the equilibrium left and right boundaries of the phase is simulated to reach a steady‑state concentration profile. The Matano method is applied to the profile to obtain D_W directly. 

The two independent D_W values for each phase are compared to test the internal consistency of the SKMF approach.

## Reproduction target
Produce the following three output files:

- `step_01_equilibrium_concentrations.json` – a JSON object with the equilibrium concentration boundaries (C_L, C_R, and width) for the five phases at 750 K.
- `step_02_A3B_growth_DW.csv` – a CSV with the growth‑derived and Matano‑derived Wagner diffusivities (in m²/s) for the A3B phase.
- `step_03_AB_growth_DW.csv` – a CSV with the same quantities for the AB phase.

The checker will verify that the equilibrium boundaries match a hidden reference, that the two Wagner diffusivities for each phase are mutually consistent (their relative difference is within an allowed tolerance), and that all D_W values lie in a physically plausible range.

## Assets

- SKMF software (Stochastic Kinetic Mean Field): http://skmf.eu

## Workflow steps

### Step 1: Compute equilibrium phase concentrations via common tangent rule
- Role: scored (load-bearing)
- Action: Using the pair interaction energies: V_AA^I = V_BB^I = -1e-21 J, V_AB^I = -3.9e-21 J, V_AA^II = V_BB^II = -8.76e-21 J, V_AB^II = -2e-21 J at T = 750 K. Construct the Gibbs free energy curves for the disordered solid solution and the ordered L1_2 and L1_0 phases using the mean-field expressions (with interactions up to second coordination shell). Minimize with respect to order parameter and determine equilibrium phase boundaries via the common tangent construction. Output the concentration ranges (C_L, C_R) for A(B) solution, AB3, AB, A3B, and B(A) solution.
- Output file: `/app/outputs/step_01_equilibrium_concentrations.json`
- Format: json
- Contract: JSON object with key 'phases' containing a list of objects. Each object has keys: phase (string, one of 'A(B)', 'AB3', 'AB', 'A3B', 'B(A)'), C_L (float, atom fraction of A), C_R (float, atom fraction of A), width (float, = C_R - C_L).
- Scoring: scored by hidden verifier

### Step 2: Derive Wagner diffusivities for A3B from growth and Matano methods
- Role: scored (load-bearing)
- Action: 1. Set up an incremental diffusion couple A-AB using the equilibrium boundaries from step_01 (left boundary of pure A taken as 0, right boundary as C_L of AB). Run SKMF simulation with system dimensions: N_x=100 atomic planes, lattice spacing dX=1.25e-10 m, dimensionless time step dt=1e-9, periodic boundary conditions, and a noise amplitude that enables nucleation. Run until the A3B phase grows parabolically. Extract the time evolution of the squared relative phase quantity ξ², fit the parabolic law ξ² = k·t/dt to obtain the dimensionless rate constant k. Compute growth-derived Wagner diffusivity as D_W_growth = k·L²/(64·dt) with L = N_x·dX. 2. Separately, construct a diffusion couple with initial compositions equal to the equilibrium left and right boundaries of the A3B phase (C_L and C_R from step_01), run SKMF to obtain a steady-state concentration profile, and apply the Matano method to compute D_W_Matano. Write both values to the output CSV.
- Output file: `/app/outputs/step_02_A3B_growth_DW.csv`
- Format: csv
- Contract: CSV with header: phase, growth_DW, Matano_DW. growth_DW and Matano_DW are floats in m²/s.
- Scoring: scored by hidden verifier

### Step 3: Derive Wagner diffusivities for AB from growth and Matano methods
- Role: scored
- Action: 1. Set up an incremental diffusion couple A3B-AB3 using the equilibrium boundaries from step_01. Run SKMF simulation with same parameters as step_02. Extract squared relative phase quantity ξ² of the growing AB phase and fit the parabolic law to obtain k. Compute growth-derived Wagner diffusivity D_W_growth = k·L²/(64·dt). 2. Separately, construct a diffusion couple with initial compositions equal to the AB equilibrium boundaries (C_L and C_R from step_01), run SKMF, and apply the Matano method to obtain D_W_Matano. Write both values to the output CSV.
- Output file: `/app/outputs/step_03_AB_growth_DW.csv`
- Format: csv
- Contract: CSV with header: phase, growth_DW, Matano_DW. growth_DW and Matano_DW are floats in m²/s.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_equilibrium_concentrations.json`
- `/app/outputs/step_02_A3B_growth_DW.csv`
- `/app/outputs/step_03_AB_growth_DW.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_equilibrium_concentrations.json
- path: `/app/outputs/step_01_equilibrium_concentrations.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Equilibrium concentration boundaries for phases A(B), AB3, AB, A3B, B(A) at 750 K.
- schema:
  - `type`: object
  - `required`:
    - `phases`: array
  - `items`:
    - `phase`: string
    - `C_L`: float
    - `C_R`: float
    - `width`: float
  - `units`:
    - `C_L`: atom fraction of A
    - `C_R`: atom fraction of A
    - `width`: atom fraction

### step_02_A3B_growth_DW.csv
- path: `/app/outputs/step_02_A3B_growth_DW.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Growth-derived and Matano-derived Wagner diffusivities for A3B phase.
- schema:
  - `type`: table
  - `required_columns`: `phase`, `growth_DW`, `Matano_DW`
  - `units`:
    - `growth_DW`: m²/s
    - `Matano_DW`: m²/s

### step_03_AB_growth_DW.csv
- path: `/app/outputs/step_03_AB_growth_DW.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Growth-derived and Matano-derived Wagner diffusivities for AB phase.
- schema:
  - `type`: table
  - `required_columns`: `phase`, `growth_DW`, `Matano_DW`
  - `units`:
    - `growth_DW`: m²/s
    - `Matano_DW`: m²/s

Notes: The first output provides the equilibrium phase boundaries needed for subsequent simulations. The second and third outputs contain the Wagner diffusivities; the checker will compute the relative difference between growth_DW and Matano_DW and verify it does not exceed 0.20. Values should fall within plausible physical range (1e-14 to 1e-12 m²/s).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_equilibrium_concentrations.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "phases": "array"
        },
        "items": {
          "phase": "string",
          "C_L": "float",
          "C_R": "float",
          "width": "float"
        },
        "units": {
          "C_L": "atom fraction of A",
          "C_R": "atom fraction of A",
          "width": "atom fraction"
        }
      },
      "description": "Equilibrium concentration boundaries for phases A(B), AB3, AB, A3B, B(A) at 750 K."
    },
    {
      "file": "step_02_A3B_growth_DW.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "phase",
          "growth_DW",
          "Matano_DW"
        ],
        "units": {
          "growth_DW": "m²/s",
          "Matano_DW": "m²/s"
        }
      },
      "description": "Growth-derived and Matano-derived Wagner diffusivities for A3B phase."
    },
    {
      "file": "step_03_AB_growth_DW.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "phase",
          "growth_DW",
          "Matano_DW"
        ],
        "units": {
          "growth_DW": "m²/s",
          "Matano_DW": "m²/s"
        }
      },
      "description": "Growth-derived and Matano-derived Wagner diffusivities for AB phase."
    }
  ],
  "notes": "The first output provides the equilibrium phase boundaries needed for subsequent simulations. The second and third outputs contain the Wagner diffusivities; the checker will compute the relative difference between growth_DW and Matano_DW and verify it does not exceed 0.20. Values should fall within plausible physical range (1e-14 to 1e-12 m²/s)."
}
```

## How you are scored
A hidden verifier reads your three output files. For the equilibrium concentrations, it compares your reported phase boundaries to a hidden reference and awards credit based on accuracy. For the A3B and AB diffusivity files, it extracts growth_DW and Matano_DW, computes the relative difference between the two values for each phase, and checks that the difference falls within an allowed tolerance; it also verifies that each D_W value is physically reasonable. The final reward (0 to 1) is a weighted combination of the scores from all three stages. You must output the files exactly at the required paths and in the specified formats. Simply reporting plausible numbers is not sufficient—the verifier independently validates the internal consistency and the agreement with the reference.

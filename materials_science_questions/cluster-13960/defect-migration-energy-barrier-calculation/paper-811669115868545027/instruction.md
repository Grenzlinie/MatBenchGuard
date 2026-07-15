# Defect migration energy barrier calculation

## Problem background
Self-interstitial atoms in hexagonal close-packed (HCP) metals such as zirconium exhibit highly anisotropic diffusion that strongly influences irradiation damage accumulation and microstructural evolution. Predictive kinetic models require quantitative knowledge of the stable interstitial configurations, their formation energies, and the activation energies and mechanisms by which they migrate. This task aims to characterise these fundamental properties for self-interstitials in α‑Zr using atomistic simulations with a published empirical interatomic potential.

## Approach
The work uses a Finnis–Sinclair-type many-body potential (Ackland) to describe interatomic interactions in α‑Zr. The computational approach combines molecular statics (MS) and molecular dynamics (MD):

* **Formation energies** – Build supercells containing each of six symmetry‑distinct interstitial configurations and perform static energy minimization. The formation energy is obtained from the relaxed total energies of the perfect and defected cells, referenced to the sublimation energy.
* **Static migration barriers** – Construct initial and final images for four symmetry‑allowed jump mechanisms (in‑plane and out‑of‑plane) and compute the minimum‑energy path via the climbing‑image nudged elastic band (CI‑NEB) method or constrained relaxation along a straight path.
* **Dynamic migration parameters** – Starting from the ground‑state interstitial, run MD simulations at elevated temperatures (≥500 ps each) with a Langevin thermostat. Identify the interstitial position via Wigner‑Seitz cell analysis, compute mean‑square displacements along the c‑axis and in the basal plane, and extract temperature‑dependent diffusion coefficients. An Arrhenius fit of the MD‑derived coefficients, decomposed into contributions from the four jump mechanisms, yields activation energies and pre‑factors.
* **Anisotropy factor** – The ratio of c‑axis to basal‑plane diffusivity is used to compute the dimensionless anisotropy factor p = (Dc/Da)^{1/6} at 600 K.

The task re‑runs these calculations with the same potential and an open‑source molecular dynamics code; the obtained formation energies, migration barriers, pre‑factors, and anisotropy factor are compared to established reference values.

## Reproduction target
1. Compute the formation energies (in eV) of the six interstitial configurations BC, BS, BO, BT, O, and CN using static relaxation with the Ackland potential. Write the results to `/app/outputs/formation_energies.json` as a JSON object with those six keys.
2. From MD simulations at 600 K and 800 K, extract the diffusion coefficients Dc and Da and then perform an Arrhenius fit to obtain the migration energy barriers (Em, in eV) and pre‑factors (Do, in cm²/s) for the four jump mechanisms J1, J2, J3, and J4. Compute the anisotropy factor p = (Dc/Da)^{1/6} at 600 K. Write all of these values to `/app/outputs/migration_results.json` as a JSON object with keys J1_Em, J2_Em, J3_Em, J4_Em, J1_Do, J2_Do, J3_Do, J4_Do, and p_factor.

## Assets

- Ackland Zr many-body potential (Finnis-Sinclair type)
- LAMMPS Molecular Dynamics Simulator: https://www.lammps.org/

## Workflow steps

### Step 1: Temperature-dependent lattice constant determination
- Role: process
- Action: Using the Ackland potential, determine the stress-free lattice constants a and c of HCP Zr at 600 K and 800 K (e.g., via Parrinello‑Rahman barostat or energy minimization with volume relaxation). Save the computed lattice constants to lattice_constants.json.
- Evidence: `/app/outputs/lattice_constants.json`

### Step 2: Formation energy calculation
- Role: scored
- Action: Create simulation cells containing the six interstitial configurations (BC, BS, BO, BT, O, CN) one at a time, perform static energy minimization, and compute the formation energy as E_{N+1} – E_N – E_sub using the Ackland potential. Write the formation energies (eV) to formation_energies.json.
- Output file: `/app/outputs/formation_energies.json`
- Format: json
- Contract: JSON object with keys BC, BS, BO, BT, O, CN mapping to formation energies in eV (floats).
- Scoring: scored by hidden verifier

### Step 3: Molecular statics calculation of migration barriers
- Role: process
- Action: Construct initial and final images for the four jump mechanisms J1, J2, J3, J4 and perform climbing‑image nudged elastic band (CI‑NEB) calculations or constrained energy minimisation along the path to obtain the static energy barriers. Save the barrier energies to ms_barriers.json for documentation.
- Evidence: `/app/outputs/ms_barriers.json`

### Step 4: MD simulation and diffusion coefficient extraction
- Role: process
- Action: Using the lattice constants from step_0, prepare simulation cells with a self‑interstitial (BC ground state). Run molecular dynamics simulations at 600 K and 800 K with a Langevin thermostat for at least 500 ps each. Analyse the trajectories: locate the interstitial via Wigner‑Seitz cell analysis and compute mean square displacements to obtain diffusion coefficients Dc (c‑axis) and Da (basal plane) at each temperature. Save the Dc, Da values to diffusion_coefficients.json.
- Evidence: `/app/outputs/diffusion_coefficients.json`

### Step 5: Arrhenius fit and anisotropy factor report
- Role: scored (load-bearing)
- Action: From the diffusion coefficients at 600 K and 800 K in diffusion_coefficients.json, perform an Arrhenius fit using the decomposition of Dc and Da contributions from the four jump mechanisms. Extract migration activation energies Em and prefactors Do for J1–J4. Compute the diffusional anisotropy factor p = (Dc/Da)^{1/6} at 600 K. Write all values to migration_results.json.
- Output file: `/app/outputs/migration_results.json`
- Format: json
- Contract: JSON object with keys J1_Em, J2_Em, J3_Em, J4_Em (eV); J1_Do, J2_Do, J3_Do, J4_Do (cm^2/s); p_factor (dimensionless).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/formation_energies.json`
- `/app/outputs/migration_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### formation_energies.json
- path: `/app/outputs/formation_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Formation energies of six self-interstitial configurations in α‑Zr computed with the Ackland potential. Compared to the paper's reported values with a tolerance of ±0.1 eV.
- schema:
  - `type`: object
  - `required_keys`: `BC`, `BS`, `BO`, `BT`, `O`, `CN`
  - `value_type`: number
  - `unit`: eV

### migration_results.json
- path: `/app/outputs/migration_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Migration energy barriers and prefactors for the four jump mechanisms J1–J4 extracted from MD diffusion coefficients, together with the diffusional anisotropy factor p at 600 K. Em values compared to paper Table 2 with ±0.05 eV, Do prefactors within 50% relative, and p factor checked to lie within the experimental range [0.85, 0.95] or within 5% of the paper-derived reference.
- schema:
  - `type`: object
  - `required_keys`: `J1_Em`, `J2_Em`, `J3_Em`, `J4_Em`, `J1_Do`, `J2_Do`, `J3_Do`, `J4_Do`, `p_factor`
  - `value_type`: number
  - `units`:
    - `J1_Em`: eV
    - `J2_Em`: eV
    - `J3_Em`: eV
    - `J4_Em`: eV
    - `J1_Do`: cm^2/s
    - `J2_Do`: cm^2/s
    - `J3_Do`: cm^2/s
    - `J4_Do`: cm^2/s
    - `p_factor`: dimensionless

Notes: Formation energies are compared against the paper's Table 1. Migration barriers are compared against the paper's Table 2; the anisotropy factor is checked for consistency with experimental values. All comparisons use result-level compare (T0) with appropriate tolerances and ordering checks.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "formation_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required_keys": [
          "BC",
          "BS",
          "BO",
          "BT",
          "O",
          "CN"
        ],
        "value_type": "number",
        "unit": "eV"
      },
      "description": "Formation energies of six self-interstitial configurations in α‑Zr computed with the Ackland potential. Compared to the paper's reported values with a tolerance of ±0.1 eV."
    },
    {
      "file": "migration_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required_keys": [
          "J1_Em",
          "J2_Em",
          "J3_Em",
          "J4_Em",
          "J1_Do",
          "J2_Do",
          "J3_Do",
          "J4_Do",
          "p_factor"
        ],
        "value_type": "number",
        "units": {
          "J1_Em": "eV",
          "J2_Em": "eV",
          "J3_Em": "eV",
          "J4_Em": "eV",
          "J1_Do": "cm^2/s",
          "J2_Do": "cm^2/s",
          "J3_Do": "cm^2/s",
          "J4_Do": "cm^2/s",
          "p_factor": "dimensionless"
        }
      },
      "description": "Migration energy barriers and prefactors for the four jump mechanisms J1–J4 extracted from MD diffusion coefficients, together with the diffusional anisotropy factor p at 600 K. Em values compared to paper Table 2 with ±0.05 eV, Do prefactors within 50% relative, and p factor checked to lie within the experimental range [0.85, 0.95] or within 5% of the paper-derived reference."
    }
  ],
  "notes": "Formation energies are compared against the paper's Table 1. Migration barriers are compared against the paper's Table 2; the anisotropy factor is checked for consistency with experimental values. All comparisons use result-level compare (T0) with appropriate tolerances and ordering checks."
}
```

## How you are scored
A hidden verifier will independently inspect your submitted artifacts (`formation_energies.json` and `migration_results.json`) and compare them against reference values derived from the original computational study. The verifier allows for reasonable differences that can arise from independent re‑implementation (different code versions, numerical settings, finite simulation time, stochastic sampling) and uses tolerances appropriate for the physical quantities.

The reward is a number between 0 and 1, computed as a weighted combination of the scores from each scored workflow stage. The reward is monotonic in quality: a result that meets or beats the reference on a directional metric earns full credit for that stage, and credit decreases only as the result deviates further from the reference. Simply reporting the paper’s numbers without executing the required simulation steps will not suffice – the verifier assesses the outputs that your workflow produces, not the values you claim. The two scored stages carry unequal weights, with the migration‑result stage being load‑bearing (it depends on correctly executing the preceding MD and analysis steps).

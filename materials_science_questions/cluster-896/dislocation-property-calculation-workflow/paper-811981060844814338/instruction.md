# 3D Atomistic Simulation of Cross-Slip in FCC Nickel

## Problem background
Cross-slip of screw dislocations in face-centred cubic (fcc) metals controls key plasticity phenomena such as work hardening, dynamic recovery, and creep. The thermally activated formation of constrictions where a (a/2)[110] screw dislocation transfers from one {111} glide plane to another, and the effect of applied Escaig stresses on the activation barrier, are not fully captured by continuum elasticity models. This task aims to compute, using atomistic simulations, the constriction structures and energetics of the cross-slip process in fcc Ni, including formation energies of the positive and negative constrictions, the total cross-slip energy, the interaction energy between constrictions, and the activation energy for cross-slip as a function of applied stress.

## Approach
The approach employs molecular statics with two Voter-Chen embedded-atom method (EAM) potentials parameterized for fcc Ni, denoted Ni(1) and Ni(2), which differ primarily in stacking-fault energy. To accurately treat boundary conditions without spurious forces, two- and three-dimensional lattice and elastic Green's function techniques are used. The workflow begins by implementing the EAM potentials and precomputing lattice and elastic Green's function tables. Then, 2D dislocation core structures spread on the glide and cross-slip {111} planes are relaxed in cylindrical cells using the Green's function boundary condition (GFBC) method. These relaxed cores serve as building blocks to assemble 3D simulation cells containing a positive or a negative constriction. After 3D GFBC relaxation, formation energies of each constriction and the total zero-stress cross-slip energy are obtained. Constriction interaction energies are computed by assembling pair configurations at a separation of 21b for Ni(2). Finally, Escaig stresses are applied to the glide plane for Ni(2), and the stress-dependent energies are used to derive activation energies for cross-slip, which are scaled to Cu via the ratio of shear moduli. All final energies are reported in a single JSON output.

## Reproduction target
Produce a file `/app/outputs/final_results.json` containing the following nine scalar energies (all in eV):

1. `ni1_positive_formation_energy` — formation energy of the positive constriction using the Ni(1) potential.
2. `ni1_negative_formation_energy` — formation energy of the negative constriction using Ni(1).
3. `ni1_total_cross_slip_energy` — sum of the above two values.
4. `ni2_positive_formation_energy` — positive constriction formation energy using Ni(2).
5. `ni2_negative_formation_energy` — negative constriction formation energy using Ni(2).
6. `ni2_total_cross_slip_energy` — sum of the above two values.
7. `interaction_energy_lambda_21b` — constriction interaction energy at separation λ = 21b for Ni(2).
8. `activation_energy_tau_0` — cross-slip activation energy for Cu at zero Escaig stress, scaled from the Ni(2) results.
9. `activation_energy_tau_0_00045mu` — cross-slip activation energy for Cu at an Escaig stress of 0.00045μ, scaled from the Ni(2) results.

## Assets

- EAM potential parameters for Ni(1) (Voter-Chen format)
- EAM potential parameters for Ni(2) (Voter-Chen format)

## Workflow steps

### Step 1: Implement EAM potentials and Green's functions
- Role: process
- Action: Implement the Voter-Chen EAM functions for Ni(1) and Ni(2) using the provided parameters. Compute the 2D lattice Green's function for the perfect fcc Ni lattice for distances R_ij < R0. Numerically integrate the 3D elastic Green's function angular part g_ij on a 161x161 grid using the Ni elastic constants. Store the GF tables for use in boundary condition relaxation.
- Evidence: `/app/outputs/gf_tables.log`

### Step 2: Relax 2D dislocation cores on glide and cross-slip planes
- Role: process
- Action: Construct cylindrical cells for the (a/2)[110] screw dislocation using the two elastic centres that produce cores spread on the (1-11) cross-slip plane and (11-1) glide plane. Partition cells into atomistic, GF, and continuum regions. Iteratively relax with the EAM potentials and 2D GFBC until the sum of squared forces falls below the convergence criterion. Save the relaxed c and g core configurations.
- Evidence: `/app/outputs/2d_cores.log`

### Step 3: Build and relax 3D positive and negative constrictions
- Role: process
- Action: Assemble 3D cylindrical cells by joining periodic units of the c and g cores according to the positive and negative constriction geometries. Partition into atomistic, GF, and continuum regions. Relax iteratively with the 3D GFBC technique until convergence. Save the relaxed 3D configurations.
- Evidence: `/app/outputs/3d_constrictions.log`

### Step 4: Compute constriction interaction energy at separation 21b (Ni(2))
- Role: process
- Action: Using the relaxed positive and negative constrictions, assemble a combined configuration with a constriction separation of 21b, fix the central layers, and relax with GFBC. Compute the total energy of the pair and extract the interaction energy by subtracting twice the energy of isolated single constrictions at infinite separation.
- Evidence: `/app/outputs/interaction.log`

### Step 5: Apply Escaig stresses and compute stress-dependent energies (Ni(2))
- Role: process
- Action: Apply Escaig stresses (τ = 0, 0.00045μ, 0.0009μ, 0.0045μ) on the glide plane to constriction pair configurations at separations 3b, 5b, 11b, 21b. For each stress and separation, relax with GFBC fixing central layers and record the total energy E(τ,λ).
- Evidence: `/app/outputs/stress_energies.log`

### Step 6: Compute cross-slip energies and write final results
- Role: scored (load-bearing)
- Action: From the relaxed 2D and 3D configurations, compute the formation energies of the positive and negative constrictions for Ni(1) and Ni(2), the total cross-slip energies at zero stress, the interaction energy at λ=21b for Ni(2), and the activation energies for cross-slip at τ=0 and τ=0.00045μ scaled to Cu using shear moduli ratios. Write all scalar energies (in eV) to /app/outputs/final_results.json.
- Output file: `/app/outputs/final_results.json`
- Format: json
- Contract: {"ni1_positive_formation_energy": <float>, "ni1_negative_formation_energy": <float>, "ni1_total_cross_slip_energy": <float>, "ni2_positive_formation_energy": <float>, "ni2_negative_formation_energy": <float>, "ni2_total_cross_slip_energy": <float>, "interaction_energy_lambda_21b": <float>, "activation_energy_tau_0": <float>, "activation_energy_tau_0_00045mu": <float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/final_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### final_results.json
- path: `/app/outputs/final_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed cross-slip energies, constriction formation energies, and activation energies for Ni(1), Ni(2), and Cu.
- schema:
  - `type`: object
  - `required`:
    - `ni1_positive_formation_energy`: number
    - `ni1_negative_formation_energy`: number
    - `ni1_total_cross_slip_energy`: number
    - `ni2_positive_formation_energy`: number
    - `ni2_negative_formation_energy`: number
    - `ni2_total_cross_slip_energy`: number
    - `interaction_energy_lambda_21b`: number
    - `activation_energy_tau_0`: number
    - `activation_energy_tau_0_00045mu`: number
  - `units`:
    - `ni1_positive_formation_energy`: eV
    - `ni1_negative_formation_energy`: eV
    - `ni1_total_cross_slip_energy`: eV
    - `ni2_positive_formation_energy`: eV
    - `ni2_negative_formation_energy`: eV
    - `ni2_total_cross_slip_energy`: eV
    - `interaction_energy_lambda_21b`: eV
    - `activation_energy_tau_0`: eV
    - `activation_energy_tau_0_00045mu`: eV

Notes: All energies must be scalar floats in eV. The checker compares these values to hidden gold values from the source paper with tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "final_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "ni1_positive_formation_energy": "number",
          "ni1_negative_formation_energy": "number",
          "ni1_total_cross_slip_energy": "number",
          "ni2_positive_formation_energy": "number",
          "ni2_negative_formation_energy": "number",
          "ni2_total_cross_slip_energy": "number",
          "interaction_energy_lambda_21b": "number",
          "activation_energy_tau_0": "number",
          "activation_energy_tau_0_00045mu": "number"
        },
        "units": {
          "ni1_positive_formation_energy": "eV",
          "ni1_negative_formation_energy": "eV",
          "ni1_total_cross_slip_energy": "eV",
          "ni2_positive_formation_energy": "eV",
          "ni2_negative_formation_energy": "eV",
          "ni2_total_cross_slip_energy": "eV",
          "interaction_energy_lambda_21b": "eV",
          "activation_energy_tau_0": "eV",
          "activation_energy_tau_0_00045mu": "eV"
        }
      },
      "description": "Computed cross-slip energies, constriction formation energies, and activation energies for Ni(1), Ni(2), and Cu."
    }
  ],
  "notes": "All energies must be scalar floats in eV. The checker compares these values to hidden gold values from the source paper with tolerances."
}
```

## How you are scored
A hidden verifier reads your submitted `final_results.json` and compares each numeric field against hidden reference expectations using tolerances appropriate for numerical simulation spread. Each field contributes equally to the total score. Reporting plausible numbers without executing the required atomistic simulation pipeline, or failing to produce the intermediate process evidence, will result in a low score because the hidden tolerances are set to demand genuine computation from the specified potentials and protocols. There is no manual review; your score is determined purely by the agreement between your computed values and the hidden expectations.

# Si-Ge Step Edge Interchange Energetics via Mixed Stillinger-Weber Potential

## Problem background
During molecular-beam epitaxy (MBE) growth of Si-Ge superlattices, interfacial ordering and the segregation of Ge atoms at step edges on (001) Ge surfaces are critical to the resulting structure and properties. Understanding the energetics of Si-Ge atom interchange at these step edges is essential for explaining the observed ordering. Atomistic simulations using interatomic potentials provide a way to evaluate the energy changes involved.

## Approach
A mixed Stillinger-Weber (SW) interatomic potential for Si-Ge is constructed by combining pure Si and Ge SW parameters using geometric mixing rules for the pair parameters and the Grabow-Gilmer approximation for the three-body parameters. Stepped-surface geometries are built for a (001) Ge surface with semi-infinite single-layer Si terraces terminated by S_B steps, considering both rebonded and nonrebonded configurations at four ledge separations: 3a, 5a, 9a, and 13a (where a = 3.995 Å). For each geometry, two atomic configurations are created: the reference with Si at terrace sites, and one where a single Si atom at the step edge is swapped with an adjacent Ge atom. Constant-volume conjugate-gradient energy minimizations are performed for all configurations using the mixed SW potential. The total energies are recorded and used to derive the energy change per ledge atom (ΔE = E_interchanged − E_original). The aim is to compute ΔE for each structure and compare the results between rebonded and nonrebonded steps.

## Reproduction target
Construct the mixed Si-Ge SW potential, build the 16 atomic configurations (8 geometries × 2 swap states), perform energy minimizations, and output the final total energies in a CSV file (`step_02_energies.csv`) with the required schema. The energy differences derived from these total energies will be used to evaluate the energetic favorability of Ge segregation at S_B step edges.

## Assets

- Stillinger-Weber potential parameters for pure Si: 10.1103/PhysRevB.31.5262
- Stillinger-Weber potential parameters for pure Ge: 10.1103/PhysRevB.34.6987
- LAMMPS molecular dynamics simulator (or equivalent open-source code supporting Stillinger-Weber potential): https://lammps.sandia.gov/

## Workflow steps

### Step 1: Derive mixed Si-Ge Stillinger-Weber parameters
- Role: process
- Action: Retrieve the pure Si and Ge SW parameters from the literature. Apply geometric mixing rules: A_ij = sqrt(A_i A_j), B_ij = sqrt(B_i B_j), ε_ij = sqrt(ε_i ε_j), λ_ij = sqrt(λ_i λ_j), σ_ij = (σ_i+σ_j)/2; and the Grabow-Gilmer approximation for three-body parameters: ε_jik = sqrt(ε_ij ε_ik), λ_jik = sqrt(λ_ij λ_ik). Implement the pair (two-body) and three-body potential functions in a usable form (code or input file) for the minimizer.
- Evidence: `/app/outputs/mixed_sw_params.json`

### Step 2: Construct stepped-surface atomic geometries
- Role: process
- Action: Build 8 simulation cells of a (001) Ge slab with semi-infinite single-layer Si terraces terminated by S_B steps (rebonded and nonrebonded) for ledge separations 3a, 5a, 9a, 13a (a=3.995 Å). For each structure create two configurations: the reference with all Si at terrace sites, and one where a single Si atom at a step edge is swapped with an adjacent Ge atom. Use periodic boundary conditions in the surface plane and fix several bottom layers. Save all atomic coordinates in a usable format.
- Evidence: `/app/outputs/geometries.zip`

### Step 3: Energy minimizations and total energy output
- Role: scored (load-bearing)
- Action: For each of the 16 configurations, perform constant-volume conjugate-gradient energy minimization using the mixed Stillinger-Weber potential. Record the final relaxed total energy. Write a CSV file containing one row per configuration with the total energy and identifying fields.
- Output file: `/app/outputs/step_02_energies.csv`
- Format: csv
- Contract: CSV columns: structure_id (str), condition (str: 'original' or 'interchanged'), total_energy_eV (float), ledge_separation (str: '3a','5a','9a','13a'), step_type (str: 'rebonded','nonrebonded'). Exactly 16 rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_02_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_02_energies.csv
- path: `/app/outputs/step_02_energies.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Total relaxed energy for each of the 16 configurations (8 structures × 'original'/'interchanged'). The hidden checker computes ΔE = E_interchanged - E_original per structure, then compares ΔE values, sign, and ordering (rebonded vs nonrebonded) to the paper's hidden gold.
- schema:
  - `type`: table
  - `required_columns`: `structure_id`, `condition`, `total_energy_eV`, `ledge_separation`, `step_type`
  - `units`:
    - `total_energy_eV`: eV

Notes: The agent must re-implement the mixed Stillinger-Weber potential from pure Si/Ge parameters and the paper-specified mixing rules, build the 16 geometries, and run conjugate-gradient minimizations. The hidden checker recomputes ΔE from the total energies; therefore the CSV values must be accurate enough to reproduce the paper's reported ΔE within tolerance. The Tersoff comparison is out of scope per the task definition.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_02_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "structure_id",
          "condition",
          "total_energy_eV",
          "ledge_separation",
          "step_type"
        ],
        "units": {
          "total_energy_eV": "eV"
        }
      },
      "description": "Total relaxed energy for each of the 16 configurations (8 structures × 'original'/'interchanged'). The hidden checker computes ΔE = E_interchanged - E_original per structure, then compares ΔE values, sign, and ordering (rebonded vs nonrebonded) to the paper's hidden gold."
    }
  ],
  "notes": "The agent must re-implement the mixed Stillinger-Weber potential from pure Si/Ge parameters and the paper-specified mixing rules, build the 16 geometries, and run conjugate-gradient minimizations. The hidden checker recomputes ΔE from the total energies; therefore the CSV values must be accurate enough to reproduce the paper's reported ΔE within tolerance. The Tersoff comparison is out of scope per the task definition."
}
```

## How you are scored
The hidden verifier reads your `step_02_energies.csv` and, for each ledge separation and step type, computes ΔE = E_interchanged − E_original. It then evaluates each ΔE against a hidden reference value drawn from the published literature. The scoring also examines the relative magnitude of the energy changes for rebonded versus nonrebonded steps. The final reward is a weighted combination of the per-value accuracy and the structural relation checks. No single reported number is sufficient; the verifier MUST be able to recompute the energy differences from your submitted CSV. Therefore, the CSV must contain the total energies for all 16 configurations in the exact format specified.

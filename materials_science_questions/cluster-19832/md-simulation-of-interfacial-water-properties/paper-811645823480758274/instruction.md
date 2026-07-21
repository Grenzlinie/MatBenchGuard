# Reproducing the Three-Regime Contact Angle Behavior on Microstructured Silicon Surfaces

## Problem background
This work investigates the wettability of a nanoscale water droplet on silicon surfaces patterned with microscopic square column arrays. Wettability is characterized by the apparent contact angle θ of the droplet. Surface roughness can alter the effective contact angle through two classical mechanisms: the Cassie state (air/vapor trapped in cavities) and the Wenzel state (liquid penetrating the cavities). Understanding how the geometry of the microstructures—specifically the period (spacing) λ relative to the droplet’s base radius r_B—affects θ is fundamental for designing surfaces with tailored wetting properties for applications in microfluidics, bio-NEMS, and nano-fabrication. The physical system consists of a water droplet modeled with the TIP4P potential, placed on a silicon (111) substrate patterned with square columns of fixed height (amplitude A_p) and variable spacing λ. Molecular dynamics simulations can resolve the droplet’s density distribution and thus its apparent contact angle. The key quantity to be reproduced is the dependence of θ on the normalized period λ/r_B; a secondary quantity is the water number density inside the cavities (ρ_cav), which serves as an indicator of whether the droplet is in a draining (Cassie-like) or filling (Wenzel-like) condition. The goal is to computationally produce the full θ(λ/r_B) curve and the associated cavity density under the specified conditions.

## Approach
The approach uses classical molecular dynamics (MD) simulations with the TIP4P water model. The silicon substrate is constructed as a diamond lattice with a (111) surface orientation; square columns of amplitude A_p = 3 σ (where σ is the Lennard-Jones length parameter) are arranged in a periodic array with periods λ = 2σ, 4σ, 6σ, 8σ, 10σ, and 12σ. Short-range interactions are described by Lennard-Jones potentials between water oxygen atoms and between water oxygen and silicon atoms; the wall-fluid interaction parameter ε_wf/ε is set to 2.0. Long-range electrostatics are handled via the TIP4P charge distribution. For each λ, an initial configuration with a cuboid of 5008 water molecules is placed on the surface. The system is first relaxed at low temperature, then heated to 300 K and equilibrated using a Nosé-Hoover thermostat. Production runs sample equilibrium configurations over several hundred reduced time units τ. After equilibration, the spatial distribution of water molecules is computed to obtain density profiles in cylindrical coordinates. The droplet base radius r_B is identified from the spreading footprint, and the density contour at the liquid-vapor interface is fitted to a circular arc to extract the apparent contact angle θ. The cavity water density ρ_cav is obtained by counting water molecules inside the cavities below the droplet and normalizing by the estimated cavity volume. The results for all λ are compiled into a single CSV file. This pipeline—system construction, MD simulation, and post-processing—must be executed end to end; the only inputs are the publicly known material parameters and model potentials.

## Reproduction target
Using the molecular dynamics workflow described above, run simulations for each of the six microstructure periods (λ = 2σ, 4σ, 6σ, 8σ, 10σ, 12σ) on Si(111) substrates with A_p = 3 σ. For each case, compute the normalized period λ/r_B, the apparent contact angle θ in degrees, and the dimensionless cavity water number density ρ_cav σ^3. Collect the results into a CSV file with the following columns: period_lambda_sigma (float), normalized_lambda_over_rB (float), contact_angle_degrees (float), cavity_density_rhocav_sigma3 (float). The file must contain at least five rows, covering a range of λ/r_B from near zero to above 0.8. The target is the truthful set of computed values produced by your simulations; no external reference values are provided.

## Assets

- LAMMPS Molecular Dynamics Simulator: https://lammps.sandia.gov
- TIP4P Water Model Parameters
- Silicon Diamond Lattice and Microstructure Geometry

## Workflow steps

### Step 1: Generate simulation systems
- Role: process
- Action: Construct atomistic configurations of Si(111) substrates with periodic square column microstructures of amplitude A_p=3σ and periods λ=2σ, 4σ, 6σ, 8σ, 10σ, 12σ. Place an initial water droplet of 5008 molecules on each substrate using the TIP4P water model and assign Lennard-Jones interactions with wall-fluid parameter ε_wf/ε=2.0.
- Evidence: `/app/outputs/setup_log.txt`

### Step 2: Run MD simulations
- Role: process
- Action: Perform molecular dynamics equilibration and production runs for each microstructure configuration at 300 K using the TIP4P water model, Lennard-Jones wall-water interactions with ε_wf/ε=2.0, and a Nosé-Hoover thermostat. Production sampling should cover a sufficient interval to collect equilibrium statistics.
- Evidence: `/app/outputs/simulation_energies.csv`

### Step 3: Compute contact angle and cavity density
- Role: scored (load-bearing)
- Action: From the equilibrated droplet configurations, compute spatial density profiles, determine the droplet base radius r_B, fit a circular profile to extract the apparent contact angle θ. For each microstructure period, compute the cavity water number density ρ_cavσ^3. Write results to contact_angle_results.csv.
- Output file: `/app/outputs/contact_angle_results.csv`
- Format: csv
- Contract: CSV with columns: period_lambda_sigma (float, period in σ units), normalized_lambda_over_rB (float, normalized period), contact_angle_degrees (float, apparent contact angle in degrees), cavity_density_rhocav_sigma3 (float, dimensionless cavity water density). At least 5 rows covering λ/r_B from ~0 to >0.8.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/contact_angle_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### contact_angle_results.csv
- path: `/app/outputs/contact_angle_results.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: CSV file containing the computed apparent contact angle and cavity water density for each microstructure period. The non-monotonic shape of contact angle vs. normalized period and the cavity density threshold between Cassie and Wenzel regimes are evaluated.
- schema:
  - `type`: table
  - `required_columns`: `period_lambda_sigma`, `normalized_lambda_over_rB`, `contact_angle_degrees`, `cavity_density_rhocav_sigma3`
  - `units`:
    - `period_lambda_sigma`: reduced length unit (σ)
    - `normalized_lambda_over_rB`: dimensionless
    - `contact_angle_degrees`: degrees
    - `cavity_density_rhocav_sigma3`: dimensionless

Notes: The CSV must contain at least 5 rows covering a range of normalized period λ/r_B from ~0 to >0.8, corresponding to the microstructure periods specified in the reproduction target.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "contact_angle_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "period_lambda_sigma",
          "normalized_lambda_over_rB",
          "contact_angle_degrees",
          "cavity_density_rhocav_sigma3"
        ],
        "units": {
          "period_lambda_sigma": "reduced length unit (σ)",
          "normalized_lambda_over_rB": "dimensionless",
          "contact_angle_degrees": "degrees",
          "cavity_density_rhocav_sigma3": "dimensionless"
        }
      },
      "description": "CSV file containing the computed apparent contact angle and cavity water density for each microstructure period. The non-monotonic shape of contact angle vs. normalized period and the cavity density threshold between Cassie and Wenzel regimes are evaluated."
    }
  ],
  "notes": "The CSV must contain at least 5 rows covering a range of normalized period λ/r_B from ~0 to >0.8, corresponding to the microstructure periods specified in the reproduction target."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that independently reads the output file /app/outputs/contact_angle_results.csv. The verifier first checks that the file exists, is well-formed, and contains exactly the required columns and sufficient rows. It then inspects the numerical values: the contact angle and cavity density data are assessed for physical consistency and compared against expected trends and reference thresholds that are derived from the underlying physics. The final score is a weighted combination of these checks; a perfect score requires that the computed quantities faithfully reflect the correct wetting behavior as determined by the simulation protocol. Simply formatting the file correctly is not enough; the numerical content must arise from a genuine execution of the MD workflow.

# Energetics of void rupture in amorphous graphene under stretching

## Problem background
Amorphous (polycrystalline) graphene under mechanical stretching can rupture via the formation and growth of voids. Classical nucleation theory predicts that a void will grow unstably when its radius exceeds a critical value, which is equal to the line tension of the void divided by the applied pressure. This task investigates the energetics of void formation in amorphous graphene through Monte Carlo simulations and a simple analytical polygon model. A key open question is how the line tension depends on the void size and what sets its lower bound in the thermodynamic limit.

## Approach
The rupture process is studied with a semi-empirical potential for graphene that includes two-body bond-stretching, three-body bond-bending, and an out-of-plane term. Amorphous carbon networks of ~5000 atoms are generated via Voronoi tessellation and relaxed under force-free boundary conditions, yielding both a perfectly flat configuration and a buckled configuration where out-of-plane relaxation is allowed. Monte Carlo bond‑transposition dynamics are then performed at a constant stretching pressure of 2 eV/Å² and a temperature k_B T = 0.083 eV, using a Metropolis acceptance criterion; the potential is augmented by a term proportional to the projected area to account for the stretching work. As the simulation evolves, snapshots are recorded whenever a void appears with radius larger than 8 Å. For each snapshot the void radius is computed by triangulating the void area, and the cumulative energy integrated from the void centre is fitted against π(r² − r_v²) over a radial range outside the void. The slope of this fit gives the line tension σ at that void radius. Collecting several (r_v, σ) points allows the finite-size scaling relation σ = σ∞ + C/r_v to be fitted, yielding the thermodynamic line tension σ∞ and the correction coefficient C. The critical void radius is then derived as r_crit = σ∞/P. In parallel, a simple analytical polygon model — a regular n‑gon with edges equal to the graphene bond length — is used to obtain a closed-form expression for the line tension that also contains a constant term and a 1/r term. The constant and coefficient of this analytical expression are computed as a reference.

## Reproduction target
Produce two scored output files:

- `simulation_results.json`: contains the fitted line-tension scaling parameters σ∞ and C, and the critical void radius r_crit, for both flat and buckled amorphous graphene, together with the raw (r_v, σ) data points (at least five per case).
- `analytical_result.json`: contains the derived constant term of the polygon model line tension, the coefficient of the 1/r term, the chosen polygon radius r_p used for evaluation, and the line tension at that radius.

Both files must follow the exact JSON schemas and units (eV/Å, Å, eV·Å) specified in the output contract.

## Assets

- numpy: https://pypi.org/project/numpy/
- scipy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Generate initial amorphous graphene configurations
- Role: process
- Action: Generate isotropic three-fold coordinated random networks of ~5000 carbon atoms using Voronoi tessellation, then relax with the semi-empirical graphene potential under force-free boundary conditions. Create one flat and one buckled (out-of-plane relaxation allowed) initial configuration.
- Evidence: `/app/outputs/initial_samples.pkl`

### Step 2: Run Monte Carlo bond-transposition simulation under constant pressure
- Role: process
- Action: For each configuration (flat and buckled), perform Monte Carlo bond‑transposition dynamics at constant pressure P=2 eV/Å² and temperature kBT=0.083 eV using the semi‑empirical potential plus the stretching energy term. Evolve the system and record atomic configurations and energy data at snapshots where a void has formed (void radius > 8 Å).
- Evidence: `/app/outputs/simulation_data.h5`

### Step 3: Extract line tension scaling parameters and critical void radius
- Role: scored (load-bearing)
- Action: From the recorded snapshots, compute void radius by triangulating the void area, local energy per atom, and the cumulative energy integrated from the void centre. For each snapshot, fit the cumulative energy vs π(r²−r_v²) over a radial range outside the void to obtain the line tension σ(r_v). Collect at least five (r_v, σ) pairs per case (flat and buckled). Perform a linear fit σ = σ∞ + C/r_v to determine σ∞ (thermodynamic‑limit line tension) and C. Compute the critical void radius as r_crit = σ∞/P. Write all results to simulation_results.json.
- Output file: `/app/outputs/simulation_results.json`
- Format: json
- Contract: A JSON object with top-level keys 'flat' and 'buckled'; each is an object with keys: 'sigma_inf' (float, eV/Å), 'C' (float, Å), 'r_crit' (float, Å), 'data' (list of [r_v (Å), sigma (eV/Å)] pairs, length ≥5).
- Scoring: scored by hidden verifier

### Step 4: Compute analytical polygon model line tension
- Role: scored
- Action: Using the fixed three‑body parameter β=5.511 eV/Å² and graphene bond length d=1.42 Å, evaluate the line tension formula for a regular polygon with large number of edges n. Derive the constant term (σ_constant) and the coefficient of the 1/r_p term (coefficient_1_over_r). Choose a large enough r_p (e.g., from n=100 via r_p = d·n/(2π)) and compute σ_p at that radius. Write the results to analytical_result.json.
- Output file: `/app/outputs/analytical_result.json`
- Format: json
- Contract: A JSON object with keys: 'sigma_constant' (float, eV/Å), 'coefficient_1_over_r' (float, eV·Å), 'computed_at_r_p' (float, Å), 'sigma_at_r_p' (float, eV/Å).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/simulation_results.json`
- `/app/outputs/analytical_result.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### simulation_results.json
- path: `/app/outputs/simulation_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Simulation‑derived line tension scaling parameters σ∞ and C, and critical radius r_crit for both flat and buckled amorphous graphene, together with the raw (r_v, σ) pairs used for fitting.
- schema:
  - `type`: object
  - `required`:
    - `flat`: object with keys sigma_inf (number), C (number), r_crit (number), data (array of [number,number] pairs)
    - `buckled`: object with same structure
  - `items`: object
  - `units`:
    - `sigma_inf`: eV/Å
    - `C`: Å
    - `r_crit`: Å
    - `data[0]`: Å
    - `data[1]`: eV/Å

### analytical_result.json
- path: `/app/outputs/analytical_result.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Analytical line‑tension constant and 1/r coefficient from the polygon model, evaluated for a chosen large r_p.
- schema:
  - `type`: object
  - `required`:
    - `sigma_constant`: number
    - `coefficient_1_over_r`: number
    - `computed_at_r_p`: number
    - `sigma_at_r_p`: number
  - `items`: object
  - `units`:
    - `sigma_constant`: eV/Å
    - `coefficient_1_over_r`: eV·Å
    - `computed_at_r_p`: Å
    - `sigma_at_r_p`: eV/Å

Notes: The simulation_results.json will be compared against the paper’s reported values (flat: σ∞≈6.95 eV/Å, C≈-30.70 Å, r_crit≈3.48 Å; buckled: σ∞≈6.61 eV/Å, C≈-33.67 Å, r_crit≈3.31 Å) with appropriate tolerances. The analytical_result.json will be checked by recomputing the deterministic constants from the published formula and comparing within a tight absolute tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "simulation_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "flat": "object with keys sigma_inf (number), C (number), r_crit (number), data (array of [number,number] pairs)",
          "buckled": "object with same structure"
        },
        "items": {},
        "units": {
          "sigma_inf": "eV/Å",
          "C": "Å",
          "r_crit": "Å",
          "data[0]": "Å",
          "data[1]": "eV/Å"
        }
      },
      "description": "Simulation‑derived line tension scaling parameters σ∞ and C, and critical radius r_crit for both flat and buckled amorphous graphene, together with the raw (r_v, σ) pairs used for fitting."
    },
    {
      "file": "analytical_result.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "sigma_constant": "number",
          "coefficient_1_over_r": "number",
          "computed_at_r_p": "number",
          "sigma_at_r_p": "number"
        },
        "items": {},
        "units": {
          "sigma_constant": "eV/Å",
          "coefficient_1_over_r": "eV·Å",
          "computed_at_r_p": "Å",
          "sigma_at_r_p": "eV/Å"
        }
      },
      "description": "Analytical line‑tension constant and 1/r coefficient from the polygon model, evaluated for a chosen large r_p."
    }
  ],
  "notes": "The simulation_results.json will be compared against the paper’s reported values (flat: σ∞≈6.95 eV/Å, C≈-30.70 Å, r_crit≈3.48 Å; buckled: σ∞≈6.61 eV/Å, C≈-33.67 Å, r_crit≈3.31 Å) with appropriate tolerances. The analytical_result.json will be checked by recomputing the deterministic constants from the published formula and comparing within a tight absolute tolerance."
}
```

## How you are scored
A hidden verifier will independently examine each scored output file. For `simulation_results.json`, the verifier compares the reported σ∞, C, and r_crit for flat and buckled graphene against reference values derived from the published study, with tolerances that account for the inherent variability of independent implementations and stochastic simulations. For `analytical_result.json`, the verifier recomputes the deterministic constants from the given formula and compares them to your reported values within a tight absolute tolerance. The final reward is a weighted combination of the scores from each stage; simply reporting expected numbers without executing the full simulation and analysis pipeline will not suffice.

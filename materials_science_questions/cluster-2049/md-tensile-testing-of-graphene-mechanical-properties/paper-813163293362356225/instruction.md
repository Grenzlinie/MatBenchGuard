# MD Simulation of Liquid Copper Dewetting on Nanopillared Graphene

## Problem background
Wettability and dewetting of metallic nanodroplets on functionalized surfaces are critical for thin-film technology, self-cleaning materials, and nanofluidic devices. This work explores how a nanopillared graphene substrate—decorated with carbon nanotube pillars—affects the dewetting and potential detachment of ultrathin liquid copper films, compared with a flat graphene substrate. The detachment behavior is thought to be driven by changes in the Cu–Cu and Cu–C interaction energies. Understanding and characterizing this behavior can guide the design of surfaces with tailored dewetting properties.

## Approach
The task is to perform molecular dynamics (MD) simulations of a liquid copper disk (diameter 135.6 Å, thickness 5 Å) placed initially 3 Å above two different substrates: flat graphene (G) and pillared graphene (PG) with a hexagonal array of capped carbon nanotube pillars (interval a = 10.2 Å, height h = 13.67 Å). Each simulation is run in the NVT ensemble at 1500 K with a 1 fs timestep and a Nosé–Hoover thermostat, fixing all substrate atoms. The Cu–Cu interactions are described by an EAM potential, the C–C interactions by the AIREBO potential, and the Cu–C cross interaction by a Lennard-Jones potential (ε = 0.018 eV, σ = 3.0 Å). The simulation tracks the potential energy components to detect detachment (when the C–Cu potential energy reaches zero) and records the detaching time and constant detaching velocity if detachment occurs. At the end of the run (200 ps) the equilibrium Cu–Cu energy difference (ΔE_Cu–Cu) and the final C–Cu interaction energy (E_C–Cu) are computed for both substrates. The comparison between G and PG reveals the role of the nanopillars in promoting or inhibiting detachment.

## Reproduction target
Run the two MD simulations (G and PG) as described. For each system, determine whether the liquid copper film detaches from the substrate (detachment is defined as the moment when the C–Cu potential energy E_C–Cu reaches zero). If detachment occurs, record the detaching time t_d (ps) and the detaching velocity v_d (m/s). At the end of the 200 ps simulation, compute the equilibrium potential energy difference ΔE_Cu–Cu (eV) and the final C–Cu interaction energy E_C–Cu (eV). Write the results to `/app/outputs/simulation_results.json` with the exact structure specified in the Workflow steps. The hidden verifier will compare your computed quantities against the expected physical behavior for these systems.

## Assets

- LAMMPS: https://www.lammps.org/
- EAM potential for copper: https://www.ctcms.nist.gov/potentials/
- AIREBO potential for carbon: lammps
- Cu-C Lennard-Jones parameters

## Workflow steps

### Step 1: Build atomic models
- Role: process
- Action: Generate the initial atomic configurations for a flat graphene (G) substrate and a pillared graphene (PG) substrate with a hexagonal array of capped carbon nanotube pillars (interval a=10.2 Å, height h=13.67 Å) and place a liquid Cu disk of diameter 135.6 Å, thickness 5 Å at 3 Å above the surface. Save the structures as LAMMPS data files.
- Evidence: `/app/outputs/init_structures.tar.gz`

### Step 2: Run MD simulations
- Role: process
- Action: Perform molecular dynamics simulations using LAMMPS in the NVT ensemble at 1500 K with a 1 fs timestep and a Nosé-Hoover thermostat, fixing all substrate atoms. Use the EAM potential for Cu, AIREBO for C-C, and Lennard-Jones for Cu-C with ε=0.018 eV, σ=3.0 Å. Run each simulation (G and PG) for at least 200 ps and record the trajectory and energy logs.
- Evidence: `/app/outputs/simulation.log`

### Step 3: Extract dewetting metrics
- Role: scored (load-bearing)
- Action: Post-process the MD trajectories: determine whether detachment occurs (C-Cu potential energy E_C-Cu reaches zero), extract detaching time t_d (ps) and detaching velocity v_d (m/s) if applicable, and compute the equilibrium potential energy difference ΔE_Cu-Cu and the C-Cu interaction energy E_C-Cu (eV) at the end of the run (200 ps). Write results to simulation_results.json.
- Output file: `/app/outputs/simulation_results.json`
- Format: json
- Contract: {"G": {"substrate": "G", "detachment": boolean, "t_d": float|null, "v_d": float|null, "dE_CuCu": float, "E_CCu": float}, "PG": {"substrate": "PG", "detachment": boolean, "t_d": float|null, "v_d": float|null, "dE_CuCu": float, "E_CCu": float}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/simulation_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### simulation_results.json
- path: `/app/outputs/simulation_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Scored artifact containing detaching time, detaching velocity, and Cu-Cu and C-Cu interaction energy changes for the flat graphene (G) and pillared graphene (PG) systems.
- schema:
  - `type`: object
  - `required`:
    - `G`:
      - `type`: object
      - `required`:
        - `substrate`: string
        - `detachment`: boolean
        - `t_d`: `number`, `null`
        - `v_d`: `number`, `null`
        - `dE_CuCu`: number
        - `E_CCu`: number
    - `PG`:
      - `type`: object
      - `required`:
        - `substrate`: string
        - `detachment`: boolean
        - `t_d`: `number`, `null`
        - `v_d`: `number`, `null`
        - `dE_CuCu`: number
        - `E_CCu`: number
  - `units`:
    - `t_d`: ps
    - `v_d`: m/s
    - `dE_CuCu`: eV
    - `E_CCu`: eV

Notes: Only the two systems (G and PG) with H=5 Å are required; parametric sweeps and other substrates are excluded.

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
          "G": {
            "type": "object",
            "required": {
              "substrate": "string",
              "detachment": "boolean",
              "t_d": [
                "number",
                "null"
              ],
              "v_d": [
                "number",
                "null"
              ],
              "dE_CuCu": "number",
              "E_CCu": "number"
            }
          },
          "PG": {
            "type": "object",
            "required": {
              "substrate": "string",
              "detachment": "boolean",
              "t_d": [
                "number",
                "null"
              ],
              "v_d": [
                "number",
                "null"
              ],
              "dE_CuCu": "number",
              "E_CCu": "number"
            }
          }
        },
        "units": {
          "t_d": "ps",
          "v_d": "m/s",
          "dE_CuCu": "eV",
          "E_CCu": "eV"
        }
      },
      "description": "Scored artifact containing detaching time, detaching velocity, and Cu-Cu and C-Cu interaction energy changes for the flat graphene (G) and pillared graphene (PG) systems."
    }
  ],
  "notes": "Only the two systems (G and PG) with H=5 Å are required; parametric sweeps and other substrates are excluded."
}
```

## How you are scored
A hidden verifier will independently evaluate each scored artifact you produce. The verifier checks whether the computed quantities—detachment status, detaching time and velocity, and the Cu–Cu and C–Cu energy differences—match the expected results within appropriate tolerances derived from the underlying physics. The overall score is a weighted average of the per-step scores. Simply reporting values without running the required MD simulations will not receive credit, because the verification relies on values that can only be obtained through a genuine reproduction of the workflow.

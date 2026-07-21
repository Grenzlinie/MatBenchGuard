# MD Simulation of Hydration Shell Dynamics

## Problem background
Hydrophobic effects govern the solvation of apolar molecules in water, influencing processes such as protein folding and gas solubility. Using molecular dynamics simulations, one can study how a dilute apolar solute like O₂ modifies the structure and dynamics of surrounding water molecules. Understanding whether a clathrate-like hydration shell forms, how water density and electrostatic charge organize around the solute, and how water's translational and hydrogen‑bond dynamics differ between the hydration shell and the bulk is essential for testing theories of hydrophobic solvation. This task reproduces those structural and dynamical measurements for O₂ in water across a range of temperatures.

## Approach
The approach uses classical molecular dynamics (NVE ensemble, periodic boundaries, Ewald summation) to simulate a single O₂ molecule in 215 SPC/E water molecules at five temperatures (291, 296, 311, 321, 348 K) with standard Lennard‑Jones parameters for O₂–water interactions. Pure water simulations serve as a comparison. After equilibration and production, we analyze the trajectories to compute: (i) radial distribution functions to define the hydration shell; (ii) local density and charge distributions around O₂; (iii) diffusion coefficients for water in the shell, in the bulk solution, and in pure water; (iv) hydrogen‑bond autocorrelation functions and average hydrogen‑bond numbers, separately for shell and bulk water.

## Reproduction target
The goal is to determine — from the MD trajectories — the following comparative trends for O₂ in water across the five temperatures:

 1. Diffusion ordering: establish whether the diffusion coefficients of water molecules in the first hydration shell (D_shell), in the bulk solution (D_bulk), and in pure liquid water (D_pure) follow a consistent ordering at each temperature.
 2. First‑shell density: for each temperature, determine whether the local water density inside the first hydration shell is higher or lower than the bulk density.
 3. Charge oscillation: at one representative low temperature, determine the sign (positive or negative) of the accumulated net electrostatic charge in successive shells around the O₂ solute.
 4. Hydrogen‑bond dynamics: compare the decay of the hydrogen‑bond autocorrelation function c(t) between shell and bulk water at each temperature, and note whether the difference between them changes with temperature.
 5. Hydrogen‑bond count: compare the average number of hydrogen bonds per water molecule in the shell and in the bulk at each temperature.

The result is a JSON file containing the computed diffusion coefficients, density comparisons, charge‑oscillation sequence, decay‑rate relative ordering, and hydrogen‑bond counts for all temperatures.

## Assets

- Molecular dynamics engine (GROMACS, LAMMPS, or NAMD): gromacs
- SPC/E water model parameters
- O2 molecule force field parameters

## Workflow steps

### Step 1: MD Production Runs
- Role: process
- Action: Run classical NVE molecular dynamics simulations of one O2 molecule solvated by 215 SPC/E water molecules at five temperatures (291, 296, 311, 321, 348 K) using the experimental densities given in Table I of the paper (0.9991, 0.9970, 0.9940, 0.9880, 0.9748 g/cm³). Also run pure water (216 SPC/E) at 299 and 323 K. Use a 0.5 fs time step, Ewald summation, periodic boundary conditions, and rigid molecules. Equilibrate each system for at least 50 ps and collect a production trajectory of at least 200 ps (solutions) or 50 ps (pure water). Save the trajectories.
- Evidence: `/app/outputs/step_01_done.txt`

### Step 2: Structural and Dynamical Analysis
- Role: scored (load-bearing)
- Action: From the simulation trajectories, compute: (i) radial distribution functions g_O2‑Ow(r) and g_O2‑Hw(r) to determine the first hydration shell boundary; (ii) local water density ρ(r) around O2; (iii) cumulative charge distribution Z(r) around O2; (iv) diffusion coefficients from mean-square displacement and/or velocity autocorrelation for shell water (first coordination shell), bulk water in solution, and pure water; (v) hydrogen-bond autocorrelation function c(t) (geometric criterion: O–O distance < 3.5 Å and O–H···O angle < 30°) for shell and bulk water; (vi) average number of hydrogen bonds per water in shell and bulk; (vii) coordination numbers – the average number of water oxygen and hydrogen atoms in the first hydration shell at each temperature; (viii) single-molecule orientational relaxation times τ (in ps) for water in the shell and in the bulk at each temperature. Write all results as a single JSON file.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: object with keys: diffusion (object, temperature keys mapping to {shell: float, bulk: float, pure: float|null}), hb_correlation (object, temperature keys mapping to {shell_decay_rank: int -1, bulk_decay_rank: int 1}), density_first_shell (object, temperature keys mapping to {higher_than_bulk: bool}), charge_oscillation (array of strings like '+ - +'), hb_counts (object, temperature keys mapping to {shell: float, bulk: float}), coordination_numbers (object, temperature keys mapping to {OW: float, HW: float}), rotational_relaxation (object, temperature keys mapping to {shell: float, bulk: float})
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Final consolidated JSON artifact containing all the structural and dynamical properties derived from the MD trajectories. The hidden checker verifies qualitative trends (diffusion ordering, density comparison, charge sign alternation, Hb correlation decay, Hb counts, coordination number decrease, and τ ordering) across temperatures.
- schema:
  - `type`: object
  - `required`: `diffusion`, `hb_correlation`, `density_first_shell`, `charge_oscillation`, `hb_counts`, `coordination_numbers`, `rotational_relaxation`
  - `properties`:
    - `diffusion`:
      - `type`: object
      - `description`: Temperature keys ("291", "296", "311", "321", "348") each with subkeys "shell", "bulk", "pure" (float; pure may be null for non-pure-water temperatures)
    - `hb_correlation`:
      - `type`: object
      - `description`: Temperature keys mapping to {shell_decay_rank: integer (shell decays faster -> negative, e.g., -1), bulk_decay_rank: integer (bulk decays slower -> positive, e.g., 1)}
    - `density_first_shell`:
      - `type`: object
      - `description`: Temperature keys mapping to {higher_than_bulk: boolean (true if density in first hydration shell > bulk)}
    - `charge_oscillation`:
      - `type`: array
      - `items`:
        - `type`: string
      - `description`: List of signs for successive charge shells around O2 at one representative temperature, e.g., ["+", "-", "+"]
    - `hb_counts`:
      - `type`: object
      - `description`: Temperature keys mapping to {shell: float, bulk: float} giving average number of hydrogen bonds per water
    - `coordination_numbers`:
      - `type`: object
      - `description`: Temperature keys mapping to {OW: float, HW: float} – average number of water oxygens and hydrogens in the first hydration shell. Must decrease with increasing temperature.
    - `rotational_relaxation`:
      - `type`: object
      - `description`: Temperature keys mapping to {shell: float, bulk: float} – single-molecule orientational relaxation time τ in ps. Shell τ must be larger than bulk τ at each temperature.

Notes: No exact numeric match is required; only the relative structural trends and orderings are checked. Units for diffusion are 10⁻⁹ m²/s; τ is in ps; coordinates are in Å.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "diffusion",
          "hb_correlation",
          "density_first_shell",
          "charge_oscillation",
          "hb_counts",
          "coordination_numbers",
          "rotational_relaxation"
        ],
        "properties": {
          "diffusion": {
            "type": "object",
            "description": "Temperature keys (\"291\", \"296\", \"311\", \"321\", \"348\") each with subkeys \"shell\", \"bulk\", \"pure\" (float; pure may be null for non-pure-water temperatures)"
          },
          "hb_correlation": {
            "type": "object",
            "description": "Temperature keys mapping to {shell_decay_rank: integer (shell decays faster -> negative, e.g., -1), bulk_decay_rank: integer (bulk decays slower -> positive, e.g., 1)}"
          },
          "density_first_shell": {
            "type": "object",
            "description": "Temperature keys mapping to {higher_than_bulk: boolean (true if density in first hydration shell > bulk)}"
          },
          "charge_oscillation": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "List of signs for successive charge shells around O2 at one representative temperature, e.g., [\"+\", \"-\", \"+\"]"
          },
          "hb_counts": {
            "type": "object",
            "description": "Temperature keys mapping to {shell: float, bulk: float} giving average number of hydrogen bonds per water"
          },
          "coordination_numbers": {
            "type": "object",
            "description": "Temperature keys mapping to {OW: float, HW: float} – average number of water oxygens and hydrogens in the first hydration shell. Must decrease with increasing temperature."
          },
          "rotational_relaxation": {
            "type": "object",
            "description": "Temperature keys mapping to {shell: float, bulk: float} – single-molecule orientational relaxation time τ in ps. Shell τ must be larger than bulk τ at each temperature."
          }
        }
      },
      "description": "Final consolidated JSON artifact containing all the structural and dynamical properties derived from the MD trajectories. The hidden checker verifies qualitative trends (diffusion ordering, density comparison, charge sign alternation, Hb correlation decay, Hb counts, coordination number decrease, and τ ordering) across temperatures."
    }
  ],
  "notes": "No exact numeric match is required; only the relative structural trends and orderings are checked. Units for diffusion are 10⁻⁹ m²/s; τ is in ps; coordinates are in Å."
}
```

## How you are scored
A hidden verifier will independently read your `results.json` and check the qualitative trends listed in the reproduction target. It will verify:

 - For each temperature, whether the diffusion coefficients satisfy the required ordering among shell, bulk, and pure water.
 - Whether the first‑shell density comparison (higher‑than‑bulk?) matches the expected temperature‑dependent pattern.
 - Whether the charge‑oscillation array contains at least one alternating sign sequence.
 - Whether the hydrogen‑bond autocorrelation decays faster in the shell than in the bulk at each temperature, and whether the gap between shell and bulk narrows with increasing temperature.
 - Whether the shell has fewer hydrogen bonds per water than the bulk at every temperature.

The verifier performs these checks without requiring exact numeric agreement with any reference values. Each independent trend contributes equally to the final score, which is a float in [0,1] representing the fraction of satisfied checks. The `results.json` output must follow the structure specified in the output contract.

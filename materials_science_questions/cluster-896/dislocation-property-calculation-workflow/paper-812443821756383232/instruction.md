# Helium platelet stability energy surface and saddle point

## Problem background
When nickel is implanted with helium ions, the helium atoms can aggregate into planar bubble arrays that, at an early growth stage, adopt a platelet morphology. Such a helium-filled platelet may later transform into a group of smaller satellite aggregates. A total-energy model has been developed to explain this behaviour. For small platelets (regime I), where the platelet thickness is comparable to its lateral size, the model incorporates elastic energy of the surrounding metal, surface energy terms (including a contribution from a minimum platelet thickness), and the pairwise interaction energy of helium atoms occupying a close-packed lattice. The energy depends on the main platelet radius and on the radius of any satellite aggregates that may form at its periphery. The computed energy surface can reveal whether an energy barrier prevents transformation, and its saddle point identifies the barrier height and location. Your task is to implement this regime I model, evaluate the total energy on a prescribed grid of platelet and satellite radii, and locate any saddle point.

## Approach
You will compute the total energy E_I of a helium-filled platelet with N_s satellite aggregates in fcc nickel. The energy has three contributions:

- Elastic energy: given by the Sack formula for a pressurized inclusion, written as C r_eff^3 p^2, where C depends on Young's modulus and Poisson's ratio, and r_eff is an effective radius that blends the main platelet radius r_p and the satellite radii r_s.
- Surface energy: includes a flat-area term (proportional to the total upper/lower surface area of the platelet and satellites) and a lateral term that accounts for the minimum platelet thickness d0.
- Gas interaction energy: helium atoms reside on a static close-packed lattice and interact via a short-range Born–Mayer repulsive potential; their total energy depends on the elastic volume of the cavity (which itself depends on pressure and geometry).

Use the following model parameters exactly:
- fcc nickel elastic constants: Young's modulus E_Y = 200 GPa, Poisson's ratio ν = 0.31.
- Surface energies: γ1 = γ3 = 0.1 eV/Å², γ2 = 0.23 eV/Å², and minimum thickness d0 = 2.5 Å.
- Born–Mayer potential for He–He: A = 0.003736 eV, α = 3.083 Å⁻¹.

Evaluate E_I on a rectangular grid: r_p in [8, 12] Å (step 0.5 Å) and r_s in [0, 3] Å (step 0.25 Å). At each grid point assume a single satellite (N_s = 1) whose projection length on the platelet circumference is 2 r_s, as in the model. For every (r_p, r_s) pair compute the equilibrium pressure from the condition that the system's volume equals the elastic volume, then compute the three energy components and sum them.

After obtaining the full energy surface, perform a discrete saddle-point search on the grid: find a point where E_I is a local minimum along one coordinate direction and a local maximum along the other. This point, if it exists, constitutes the energy barrier for transformation.

## Reproduction target
Produce a single JSON file containing the complete energy surface and the saddle-point information. The surface must include every grid point (r_p = 8.0, 8.5, ..., 12.0 Å; r_s = 0.0, 0.25, ..., 3.0 Å) with its computed E_I (in eV). If a saddle point is found, report its r_p, r_s, and the corresponding energy; if no saddle point exists, report null. The output must adhere to the exact JSON schema described in the Output contract.

## Assets

- Standard elastic constants for fcc nickel
- Born-Mayer potential parameters for He–He interaction (Gaydaenko & Nikulin, 1970)

## Workflow steps

### Step 1: Compute regime I total energy surface and locate saddle point
- Role: scored
- Action: Implement the regime I total energy model for a helium platelet with satellite aggregates in fcc nickel. Use the Sack elastic energy formula with effective radius, surface energy terms (including a lateral term from minimum thickness d0=2.5 Å), and the Born-Mayer potential for gas energy on a close-packed lattice. Evaluate the total energy E_I on a grid of platelet radius r_p = 8 to 12 Å (step 0.5 Å) and satellite radius r_s = 0 to 3 Å (step 0.25 Å). For each grid point compute E_I and collect the results. Then perform a discrete saddle-point search: find a point that is a minimum along one variable and a maximum along the other. Output the full energy surface and, if found, the saddle-point coordinates and energy.
- Output file: `/app/outputs/step_01_energy_surface.json`
- Format: json
- Contract: A JSON object with two keys: "surface" (array of objects, each with "r_p" (float, Å), "r_s" (float, Å), "E_I" (float, eV)) and "saddle_point" (object with "r_p_saddle" (float, Å), "r_s_saddle" (float, Å), "E_saddle" (float, eV), or null if no saddle point found).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_energy_surface.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_energy_surface.json
- path: `/app/outputs/step_01_energy_surface.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: The full energy surface on a regular grid of platelet radius r_p and satellite radius r_s, and the discrete saddle point after numerical search.
- schema:
  - `type`: object
  - `required`: `surface`, `saddle_point`
  - `surface`:
    - `type`: array
    - `items`:
      - `type`: object
      - `required`: `r_p`, `r_s`, `E_I`
      - `properties`:
        - `r_p`:
          - `type`: number
          - `unit`: Å
        - `r_s`:
          - `type`: number
          - `unit`: Å
        - `E_I`:
          - `type`: number
          - `unit`: eV
  - `saddle_point`:
    - `type`: object
    - `required`: `r_p_saddle`, `r_s_saddle`, `E_saddle`
    - `properties`:
      - `r_p_saddle`:
        - `type`: number
        - `unit`: Å
      - `r_s_saddle`:
        - `type`: number
        - `unit`: Å
      - `E_saddle`:
        - `type`: number
        - `unit`: eV
    - `nullable`: True

Notes: The atomistic simulation stage (Section 3) is not reproduced because it requires unpublished details. Only the regime I analytic model is computed. The agent must use the specified parameters exactly.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_energy_surface.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "surface",
          "saddle_point"
        ],
        "surface": {
          "type": "array",
          "items": {
            "type": "object",
            "required": [
              "r_p",
              "r_s",
              "E_I"
            ],
            "properties": {
              "r_p": {
                "type": "number",
                "unit": "Å"
              },
              "r_s": {
                "type": "number",
                "unit": "Å"
              },
              "E_I": {
                "type": "number",
                "unit": "eV"
              }
            }
          }
        },
        "saddle_point": {
          "type": "object",
          "required": [
            "r_p_saddle",
            "r_s_saddle",
            "E_saddle"
          ],
          "properties": {
            "r_p_saddle": {
              "type": "number",
              "unit": "Å"
            },
            "r_s_saddle": {
              "type": "number",
              "unit": "Å"
            },
            "E_saddle": {
              "type": "number",
              "unit": "eV"
            }
          },
          "nullable": true
        }
      },
      "description": "The full energy surface on a regular grid of platelet radius r_p and satellite radius r_s, and the discrete saddle point after numerical search."
    }
  ],
  "notes": "The atomistic simulation stage (Section 3) is not reproduced because it requires unpublished details. Only the regime I analytic model is computed. The agent must use the specified parameters exactly."
}
```

## How you are scored
A hidden verifier will independently implement the same regime I model using the identical parameter set and will compute the energy surface on the same grid. It will then compare your reported energies on a random subset of grid points. The verifier will also locate the saddle point on its own discretized surface and check whether your reported saddle point coordinates and energy agree. Your final score is a weighted combination of the fraction of energy values that agree within an allowed tolerance and the correctness of the saddle-point identification. Reporting the paper's published numbers is not sufficient; the verifier recomputes the expected results from first principles.

# Molecular Dynamics Simulation of Low-Energy Ion Beam Mixing in Metallic Superlattices

## Problem background
Ion beam mixing is a widely used technique for modifying near-surface layers of materials, yet the atomic-level mechanisms that govern intermixing in metallic superlattices remain poorly understood, especially at low ion energies (few eV) where collision cascades are small. The role of interfacial structure—whether the layers adopt a coherent, registered arrangement or a misregistered one—may strongly influence mass transport and local density changes. Molecular dynamics simulations can probe these effects by tracking the trajectories of every atom under controlled conditions, providing insight into how mixing and density inhomogeneities develop over picosecond timescales.

## Approach
The task re-implements a molecular dynamics simulation of a Fe/Ag bilayer (~40 Å per sublattice, ~2000 atoms each) under 5 eV As⁺ ion bombardment. Two interface geometries are constructed: registered growth (coherent matching that forms large channels) and unregistered growth (misregistered rows that reduce channel size). Interatomic interactions employ EAM potentials for Fe-Fe and Ag-Ag and the ZBL universal repulsive potential for Fe-Ag cross interactions; a planar interfacial energy barrier (low-barrier, approximately 0–0.5 eV) is included. After equilibration at 300 K using an Andersen thermostat, a single As⁺ ion is introduced along the Z-axis and the system is evolved for 12 ps. From the production trajectories, the mixing coefficient m (percentage of atoms found in the opposite layer) and the densification indicator <ρ> (maximum deviation of atom counts in 5 Å slabs relative to the initial content, expressed as a ratio) are computed at 0.1, 2.0, 6.0, and 12.0 ps for both interface types.

## Reproduction target
Produce a JSON file containing the time-resolved mixing coefficient m (percentage of atoms crossing the interface into the opposite layer) and the densification indicator <ρ> (ratio of current to initial atoms in a slab) at 0.1, 2.0, 6.0, and 12.0 ps for the unregistered and registered growth configurations with the low interfacial barrier condition. The target is to capture the quantitative evolution of these quantities and their dependence on interface structure.

## Assets

- LAMMPS molecular dynamics simulator: https://www.lammps.org/
- EAM potential for Fe (Johnson & Wilson, 1975)
- EAM potential for Ag (Oh & Johnson, 1988)

## Workflow steps

### Step 1: Build bilayer geometries
- Role: process
- Action: Construct the Fe/Ag bilayer simulation cell for both registered and unregistered growth configurations. Each sublattice is ~40 Å cubic with ~2000 atoms; periodic XY, free Z. Registered growth: coherent matching forming large channels (2.03×4.04 Å²). Unregistered growth: misregistered rows shrinking the channel to 1.4×2.87 Å² at the Ag→Fe passage. Output atomic coordinates and cell vectors.
- Evidence: `/app/outputs/geometry_log.txt`

### Step 2: Set up potentials and interfacial barrier
- Role: process
- Action: Assign interatomic potentials: EAM for Fe-Fe (Johnson-Wilson) and Ag-Ag (Oh-Johnson); ZBL for Fe-Ag. Implement a planar interfacial energy barrier E_int with value in the range 0–0.5 eV (low-barrier case) according to the planar barrier model from the literature. Prepare the bilayer for bombardment.
- Evidence: `/app/outputs/potential_setup.txt`

### Step 3: Equilibration simulation
- Role: process
- Action: Run MD equilibration at 300 K using an Andersen thermostat for both interface types with the chosen E_int, until thermal equilibrium is reached. Save the equilibrated atomic positions and velocities.
- Evidence: `/app/outputs/equilibration.log`

### Step 4: Ion bombardment simulation
- Role: process
- Action: For each interface type (unregistered and registered) and low E_int, insert an As⁺ ion with 5 eV kinetic energy along the Z-axis into the equilibrated bilayer. Run production MD for 12 ps with thermostat maintained. Save the full trajectory (positions, velocities) for subsequent analysis.
- Evidence: `/app/outputs/bombardment.log`

### Step 5: Compute mixing and densification indicators
- Role: scored (load-bearing)
- Action: Analyze the production trajectories to compute the mixing coefficient m (percentage of atoms in the opposite layer) and densification indicator <ρ> (maximum deviation of atom counts in 5 Å slabs vs. initial content) at times 0.1, 2.0, 6.0, 12.0 ps for both unregistered and registered growth cases with low E_int. Output the results as a single JSON file.
- Output file: `/app/outputs/mixing_densification_results.json`
- Format: json
- Contract: {"unregistered_low_barrier": [{"time_ps": number, "m_percent": number, "rho": number}], "registered_low_barrier": [{"time_ps": number, "m_percent": number, "rho": number}]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/mixing_densification_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### mixing_densification_results.json
- path: `/app/outputs/mixing_densification_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Mixing coefficient m (percent) and densification indicator <ρ> at time points 0.1, 2.0, 6.0, 12.0 ps for both unregistered and registered growth with low interfacial barrier (0–0.5 eV).
- schema:
  - `type`: object
  - `properties`:
    - `unregistered_low_barrier`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `time_ps`:
            - `type`: number
            - `unit`: ps
          - `m_percent`:
            - `type`: number
            - `unit`: percentage
          - `rho`:
            - `type`: number
            - `unit`: ratio
        - `required`: `time_ps`, `m_percent`, `rho`
      - `minItems`: 4
      - `maxItems`: 4
      - `description`: Entries for times 0.1, 2.0, 6.0, 12.0 ps
    - `registered_low_barrier`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `time_ps`:
            - `type`: number
            - `unit`: ps
          - `m_percent`:
            - `type`: number
            - `unit`: percentage
          - `rho`:
            - `type`: number
            - `unit`: ratio
        - `required`: `time_ps`, `m_percent`, `rho`
      - `minItems`: 4
      - `maxItems`: 4
      - `description`: Entries for times 0.1, 2.0, 6.0, 12.0 ps
  - `required`: `unregistered_low_barrier`, `registered_low_barrier`

Notes: The checker compares the reported values to the paper's gold values using absolute tolerances and also verifies structural trends (m_registered > m_unregistered at each time point, <ρ> >= 1 at 2.0, 6.0, 12.0 ps).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "mixing_densification_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "properties": {
          "unregistered_low_barrier": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "time_ps": {
                  "type": "number",
                  "unit": "ps"
                },
                "m_percent": {
                  "type": "number",
                  "unit": "percentage"
                },
                "rho": {
                  "type": "number",
                  "unit": "ratio"
                }
              },
              "required": [
                "time_ps",
                "m_percent",
                "rho"
              ]
            },
            "minItems": 4,
            "maxItems": 4,
            "description": "Entries for times 0.1, 2.0, 6.0, 12.0 ps"
          },
          "registered_low_barrier": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "time_ps": {
                  "type": "number",
                  "unit": "ps"
                },
                "m_percent": {
                  "type": "number",
                  "unit": "percentage"
                },
                "rho": {
                  "type": "number",
                  "unit": "ratio"
                }
              },
              "required": [
                "time_ps",
                "m_percent",
                "rho"
              ]
            },
            "minItems": 4,
            "maxItems": 4,
            "description": "Entries for times 0.1, 2.0, 6.0, 12.0 ps"
          }
        },
        "required": [
          "unregistered_low_barrier",
          "registered_low_barrier"
        ]
      },
      "description": "Mixing coefficient m (percent) and densification indicator <ρ> at time points 0.1, 2.0, 6.0, 12.0 ps for both unregistered and registered growth with low interfacial barrier (0–0.5 eV)."
    }
  ],
  "notes": "The checker compares the reported values to the paper's gold values using absolute tolerances and also verifies structural trends (m_registered > m_unregistered at each time point, <ρ> >= 1 at 2.0, 6.0, 12.0 ps)."
}
```

## How you are scored
A hidden automated verifier compares your submitted mixing_densification_results.json against reference values obtained from the original simulation study. The verifier checks each time-point value of m and <ρ> within a tolerance that accounts for legitimate differences arising from software implementations, functionals, and computational seeds. It also verifies expected structural relationships between the two interface types (e.g., relative ordering of mixing magnitudes) and whether density nonuniformities persist over time. Each check is weighted, and the final score is the fraction of checks passed. Meeting or exceeding the reference values for directional metrics earns full credit; only significant deviations beyond the tolerance window reduce the score.

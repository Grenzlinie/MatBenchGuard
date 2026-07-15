# Atomistic Simulation of Dissociated Dislocations in fcc Metals

## Problem background
In face-centered cubic (fcc) metals, a perfect dislocation can dissociate into two Shockley partials separated by a ribbon of stacking fault; the equilibrium spacing $d$ depends on the stacking-fault energy and elastic constants. Similarly, the Lomer dislocation on {001} planes can dissociate into a Lomer-Cottrell (LC) configuration consisting of a stair-rod partial and two Shockley partials on inclined {111} planes. Linear isotropic elasticity predicts specific equilibrium partial spacings and, for the LC dislocation, an asymmetric arrangement. Whether these elastic predictions hold on the atomic scale, and how the corresponding dislocation energies compare, are fundamental questions for dislocation theory. This task reproduces atomistic static-relaxation simulations for Cu and Ag using many-body Finnis-Sinclair potentials to determine the equilibrium structures and energies of these dissociated dislocations and to compare them with the elasticity predictions.

## Approach
We employ the Finnis-Sinclair EAM potentials for Cu and Ag (Ackland et al. 1987) within the open-source molecular dynamics code LAMMPS. For each metal, computational cells containing either the dissociated perfect 60° dislocation or the Lomer-Cottrell dislocation are set up with periodic boundary conditions along the dislocation line direction [1–10] and fixed boundaries in the perpendicular directions. The atoms are initially displaced according to isotropic linear elastic displacement fields of the partial dislocations, placed at a range of initial separations. The inner atoms (approximately 4600) are then relaxed to minimum energy via conjugate-gradient minimization.

After relaxation, the relative atomic displacement component $\Delta u_x$ along [11–2] (normalized to half the perfect Burgers vector) is computed from the atomic coordinates. For the perfect 60° dislocation, the equilibrium partial spacing $d$ is taken as the distance along $x$ between the points where $\Delta u_x$ equals $b_p/6$ and $2b_p/3$. For the LC dislocation, the spacings $d_1$ and $d_2$ between the stair-rod partial and the two Shockley partials are determined analogously from the displacement profile. The dislocation energy per unit line length is obtained as the potential energy of the relaxed cell minus the energy of a perfect crystal of the same size.

In parallel, the equilibrium partial spacings and energies predicted by isotropic linear elasticity are calculated using the known lattice parameter, effective isotropic elastic constants, and stacking-fault energy of each metal. The atomistic results are then compared to these elasticity references to assess how well continuum theory describes the atomic-scale dislocation structure.

## Reproduction target
Produce the following three artifacts under `/app/outputs`:

1. **`perfect_dislocation_results.json`**: For Cu and Ag, report the equilibrium partial spacing $d$ of the dissociated perfect 60° dislocation (in nm and in units of the lattice parameter $a$), the dislocation energy per line length (in eV), and the spacing predicted by isotropic linear elasticity (in nm).

2. **`perfect_dislocation_displacement.csv`**: For Cu only, export a dense displacement profile (at least 100 points) with columns `x` (position along [11–2] in units of $a$) and `delta_u_x` (the relative displacement $\Delta u_x$, dimensionless, as a fraction of half the perfect Burgers vector). This profile must span the core region so that the partial spacing can be independently recomputed by interpolating at $\Delta u_x = 1/6$ and $2/3$.

3. **`lomer_cottrell_results.json`**: For Cu and Ag, report the spacings $d_1$ and $d_2$, their mean $\bar{d}$, the asymmetry ratio $d_1/d_2$, the dislocation energy (eV), and the corresponding elastic predictions for $d_1$ and $d_2$, all in units of $a$.

The goal is to obtain the true atomistic equilibrium configurations from the simulations, to compare the relaxed spacings and energies with the predictions of isotropic elasticity, and to determine whether the LC dislocation adopts an asymmetric arrangement ($d_1 \neq d_2$) and, if so, the magnitude of the asymmetry.

## Assets

- Finnis-Sinclair EAM potential for Cu (Ackland et al. 1987): https://www.ctcms.nist.gov/potentials/entry/1987--Ackland-G-J-Tichy-G-Vitek-V-Finnis-M-W--Cu/
- Finnis-Sinclair EAM potential for Ag (Ackland et al. 1987): https://www.ctcms.nist.gov/potentials/entry/1987--Ackland-G-J-Tichy-G-Vitek-V-Finnis-M-W--Ag/
- LAMMPS (Large-scale Atomic/Molecular Massively Parallel Simulator): https://lammps.sandia.gov/

## Workflow steps

### Step 1: Elasticity Reference Calculation
- Role: process
- Action: Using isotropic linear elasticity theory, known elastic constants (or tabulated effective values), lattice parameter a, stacking fault energy γ, and Burgers vectors, compute the equilibrium partial spacings and elastic energies for the dissociated perfect 60° dislocation and the asymmetric Lomer-Cottrell dislocation in Cu and Ag. These serve as reference values for later comparison.
- Evidence: none

### Step 2: Atomistic Static Relaxation Simulation
- Role: process
- Action: Set up LAMMPS computational cells for Cu and Ag containing the dissociated perfect 60° dislocation and the Lomer-Cottrell dislocation. Use periodic boundary along [1-10] and fixed boundaries in perpendicular directions. Initialize atoms according to linear elastic displacement fields at several initial partial spacings. Perform conjugate-gradient energy minimization with the Finnis-Sinclair EAM potentials to obtain relaxed atomic coordinates and cell energies.
- Evidence: `/app/outputs/relaxation_summary.txt`

### Step 3: Post-Relaxation Analysis for Perfect 60° Dislocation
- Role: scored
- Action: From the relaxed configurations of the dissociated perfect 60° dislocation, compute the relative atomic displacement Δu_x along [11-2] normalized to half the perfect Burgers vector. Extract the partial spacing d as the distance between the points where Δu_x equals b_p/6 and 2b_p/3. Calculate the dislocation energy (cell energy minus perfect-crystal energy). Report results for Cu and Ag in perfect_dislocation_results.json.
- Output file: `/app/outputs/perfect_dislocation_results.json`
- Format: json
- Contract: JSON object with keys 'Cu' and 'Ag'; each key contains: relaxed_d_nm (float, nm), relaxed_d_a (float, in units of lattice parameter a), energy_eV (float, eV), elastic_d_nm (float, nm).
- Scoring: scored by hidden verifier

### Step 4: Perfect 60° Dislocation Displacement Profile (Cu)
- Role: scored (load-bearing)
- Action: For the relaxed perfect 60° dislocation in Cu, export the displacement profile as a CSV. Columns: x (in units of a) and delta_u_x (dimensionless, fraction of half-bp). Include at least 100 points spanning the region from negative x to positive x, covering the core region so that the partial spacing can be recomputed by interpolating at Δu_x=1/6 and 2/3.
- Output file: `/app/outputs/perfect_dislocation_displacement.csv`
- Format: csv
- Contract: CSV with header row: x,delta_u_x. x in units of a, delta_u_x dimensionless. At least 100 rows.
- Scoring: scored by hidden verifier

### Step 5: Post-Relaxation Analysis for Lomer-Cottrell Dislocation
- Role: scored (load-bearing)
- Action: From the relaxed Lomer-Cottrell configurations, determine the spacings d1 and d2 between the stair-rod partial and the two Shockley partials for Cu and Ag. Compute the mean spacing d_bar = (d1+d2)/2 and the asymmetry ratio d1/d2. Calculate the dislocation energy. Report results in lomer_cottrell_results.json.
- Output file: `/app/outputs/lomer_cottrell_results.json`
- Format: json
- Contract: JSON object with keys 'Cu' and 'Ag'; each key contains: d1_a (float, in units of a), d2_a (float, a), d_bar_a (float, a), d1_d2_ratio (float), energy_eV (float, eV), elastic_d1_a (float, a), elastic_d2_a (float, a).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/perfect_dislocation_results.json`
- `/app/outputs/perfect_dislocation_displacement.csv`
- `/app/outputs/lomer_cottrell_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### perfect_dislocation_results.json
- path: `/app/outputs/perfect_dislocation_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Equilibrium partial spacing and energy for the dissociated perfect 60° dislocation in Cu and Ag. Values are compared to hidden paper gold within tolerances.
- schema:
  - `type`: object
  - `required`:
    - `Cu`:
      - `type`: object
      - `required`: `relaxed_d_nm`, `relaxed_d_a`, `energy_eV`, `elastic_d_nm`
    - `Ag`:
      - `type`: object
      - `required`: `relaxed_d_nm`, `relaxed_d_a`, `energy_eV`, `elastic_d_nm`

### perfect_dislocation_displacement.csv
- path: `/app/outputs/perfect_dislocation_displacement.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Displacement profile Δu_x(x) for Cu. Checker recomputes partial spacing d by linear interpolation at Δu_x=1/6 and 2/3, then compares to the agent's reported relaxed_d_a (from perfect_dislocation_results.json) within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `x`, `delta_u_x`
  - `units`:
    - `x`: units of a
    - `delta_u_x`: dimensionless fraction of half-bp

### lomer_cottrell_results.json
- path: `/app/outputs/lomer_cottrell_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Equilibrium partial spacings and energy for the asymmetric Lomer-Cottrell dislocation in Cu and Ag. Numerical fields compared to hidden paper gold within tolerances; d1/d2 ratio expected > 2 per structural requirement.
- schema:
  - `type`: object
  - `required`:
    - `Cu`:
      - `type`: object
      - `required`: `d1_a`, `d2_a`, `d_bar_a`, `d1_d2_ratio`, `energy_eV`, `elastic_d1_a`, `elastic_d2_a`
    - `Ag`:
      - `type`: object
      - `required`: `d1_a`, `d2_a`, `d_bar_a`, `d1_d2_ratio`, `energy_eV`, `elastic_d1_a`, `elastic_d2_a`

Notes: The checker recomputes the Cu partial spacing from the displacement CSV. For other numeric fields, reported values are compared to paper-reported gold with appropriate tolerances (spacings: ±0.5a, energy: ±0.2 eV, LC asymmetry d1/d2 > 2). The atomic configurations themselves are not part of the output contract.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "perfect_dislocation_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "Cu": {
            "type": "object",
            "required": [
              "relaxed_d_nm",
              "relaxed_d_a",
              "energy_eV",
              "elastic_d_nm"
            ]
          },
          "Ag": {
            "type": "object",
            "required": [
              "relaxed_d_nm",
              "relaxed_d_a",
              "energy_eV",
              "elastic_d_nm"
            ]
          }
        }
      },
      "description": "Equilibrium partial spacing and energy for the dissociated perfect 60° dislocation in Cu and Ag. Values are compared to hidden paper gold within tolerances."
    },
    {
      "file": "perfect_dislocation_displacement.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "delta_u_x"
        ],
        "units": {
          "x": "units of a",
          "delta_u_x": "dimensionless fraction of half-bp"
        }
      },
      "description": "Displacement profile Δu_x(x) for Cu. Checker recomputes partial spacing d by linear interpolation at Δu_x=1/6 and 2/3, then compares to the agent's reported relaxed_d_a (from perfect_dislocation_results.json) within tolerance."
    },
    {
      "file": "lomer_cottrell_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "Cu": {
            "type": "object",
            "required": [
              "d1_a",
              "d2_a",
              "d_bar_a",
              "d1_d2_ratio",
              "energy_eV",
              "elastic_d1_a",
              "elastic_d2_a"
            ]
          },
          "Ag": {
            "type": "object",
            "required": [
              "d1_a",
              "d2_a",
              "d_bar_a",
              "d1_d2_ratio",
              "energy_eV",
              "elastic_d1_a",
              "elastic_d2_a"
            ]
          }
        }
      },
      "description": "Equilibrium partial spacings and energy for the asymmetric Lomer-Cottrell dislocation in Cu and Ag. Numerical fields compared to hidden paper gold within tolerances; d1/d2 ratio expected > 2 per structural requirement."
    }
  ],
  "notes": "The checker recomputes the Cu partial spacing from the displacement CSV. For other numeric fields, reported values are compared to paper-reported gold with appropriate tolerances (spacings: ±0.5a, energy: ±0.2 eV, LC asymmetry d1/d2 > 2). The atomic configurations themselves are not part of the output contract."
}
```

## How you are scored
A hidden verifier will independently score the artifacts you write.

- It reads `perfect_dislocation_results.json` and compares the reported `relaxed_d_a` and `energy_eV` (for both Cu and Ag) to hidden reference values, as well as the `elastic_d_nm` predictions.
- For Cu, it reads `perfect_dislocation_displacement.csv`, recomputes the partial spacing by linearly interpolating the $x$ positions where $\Delta u_x$ equals $1/6$ and $2/3$ of the half-bp, and verifies that the re-computed spacing is consistent with your reported `relaxed_d_a` (within a tolerance).
- It reads `lomer_cottrell_results.json` and compares the reported `d1_a`, `d2_a`, `d_bar_a`, `energy_eV`, and the elastic spacings to hidden reference values, and checks the structural constraint that $d_1/d_2 > 2$.

The final reward is a weighted combination: approximately 40% for the perfect dislocation results (spacings, energy, and elastic comparison), 30% for the displacement recompute test on Cu, and 30% for the Lomer-Cottrell results. Reporting numbers far from the reference or inconsistent with the recomputed spacing will reduce your score. The hidden tolerances account for typical run-to-run variation in static relaxations.

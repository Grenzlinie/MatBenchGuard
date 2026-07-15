# Masonry Façade Panel Cracking Simulation from Differential Displacements

## Problem background
In Spain, many residential buildings use ceramic brick masonry façade panels supported partially on edge beams of a reinforced concrete frame. Cracking of these panels is frequently observed and can be caused by differential vertical displacements between successive floors arising from structural deformations and long-term creep. Understanding and controlling crack evolution requires quantifying the effective beam deflections experienced by each panel and predicting how crack widths grow with those displacements for a range of masonry material properties. The present task undertakes a numerical approach to compute the effective long-term beam deflections and to simulate cohesive crack propagation in the masonry, yielding dimensionless curves that relate maximum crack width to imposed displacement for different values of tensile strength and elastic modulus. These curves provide a design-oriented view of crack evolution and assess the influence of material brittleness on behaviour.

## Approach
The reproduction follows a two-stage strategy. First, an elastic finite element model of a five-storey reinforced concrete building frame is built using the geometry, boundary conditions, and material properties (steel, concrete, masonry) described in the task. Seven loading cases are applied to capture individual contributions to the displacement field. Using the principle of superposition, the displacements at each construction stage are assembled according to the sequence of building. A long-term creep amplification factor of two is then applied to obtain viscoelastic total displacements. Effective beam deflections are obtained by subtracting the displacements at the time each masonry panel was built, and by removing the column shortening component. Second, the critical first-floor panel is isolated and subjected to imposed boundary displacements proportional to the effective deflection profile, with a maximum centre displacement scaling from 0 to at least 2.9 mm in steps of 0.1 mm. For each of nine material combinations (tensile strength 0.5, 1.0, 1.5 MPa; elastic modulus 2, 3, 4 GPa; fracture energy fixed at 100 N/m, giving characteristic lengths between 89 and 1600 mm), a nonlinear finite element simulation with an embedded cohesive crack model (exponential softening) is run. The maximum crack width w_max is recorded at each displacement level. The result is a set of dimensionless curves relating the normalised crack width to the normalised central displacement, grouped by the characteristic length λ_ch.

## Input data

### Building frame geometry

- Number of storeys: 5 (floors 1 to 5).
- Floor-to-floor height: 3.0 m.
- Beam cross-section: width 500 mm, depth 300 mm.
- Column dimensions:
  - Ground floor (level 0) and first floor (level 1): 400 mm × 400 mm.
  - Second to fifth floors: 300 mm × 300 mm.
- Slab thickness: 300 mm; slab spans 5.40 m between frames, transferring 2.70 m of load to each edge beam.
- Edge beam span (column-to-column): 5.00 m.
- The frame is modelled as a 2D plane structure. At the left boundary (symmetry plane), horizontal displacements are zero. At the right boundary (expansion joint), the frame horizontal displacement is zero but masonry has zero traction; thus, the frame's horizontal translation at that boundary is also restrained.
- All column bases are fixed.

### Material properties

- Steel: Young's modulus 200 GPa, Poisson's ratio 0.3.
- Concrete: Young's modulus 30 GPa, Poisson's ratio 0.2.
- Masonry (homogenised isotropic): Young's modulus 3 GPa, Poisson's ratio 0.2.
- Lintel (steel angle): same steel properties, dimensions 100 mm × 100 mm × 10 mm, modelled as a line element with appropriate section.

### Loading cases and magnitudes

Loads per unit horizontal length of edge beam (distributed over the beam):
- Slab self-weight: p_s = 2.5 kN/m² × 2.70 m = 6.75 kN/m.
- Masonry panel weight: p_m = 3.0 kN/m² × panel height (2.7 m) = 8.1 kN/m.
- Flooring: p_f = 1.5 kN/m² × 2.70 m = 4.05 kN/m.
- Live load on floors: p_l = 2.0 kN/m² × 2.70 m = 5.4 kN/m.
- Roof protection wall weight: p_r = p_m (assumed as same weight as one floor panel) = 8.1 kN/m.
- Roof live load: assumed equal to floor live load (p_lr = p_l = 5.4 kN/m), so the correction term (p_lr − p_l) is zero.

Seven unit-load cases are run (each load is a distributed vertical force on the indicated beams). For a given case, a load of 1 kN/m is applied, and the recorded displacement field is later scaled by the corresponding p value.
1. Case 1: 1 kN/m on beam of floor 1 only (to be scaled by p_m).
2. Case 2: 1 kN/m on beam of floor 2 only (scaled by p_m).
3. Case 3: 1 kN/m on beam of floor 3 only (scaled by p_m).
4. Case 4: 1 kN/m on beam of floor 4 only (scaled by p_m).
5. Case 5: 1 kN/m on beam of floor 5 (roof) only (scaled by p_m, represents roof panel weight).
6. Case 6: 1 kN/m on all beams (floors 1–5) simultaneously (scaled by p_s).
7. Case 7: 1 kN/m on all beams (floors 1–5) simultaneously (scaled by p_f + p_l).

### Panel geometry for the crack simulation

The first‑floor masonry panel is half of a single panel (symmetry). Its dimensions:
- Width: 2.5 m (half of the 5.0 m beam span).
- Height: 2.7 m (storey height minus beam depth).
- Window opening: centred horizontally, width 1.5 m, height 1.2 m, bottom edge elevation 0.9 m above the panel bottom.
- A steel lintel (100 mm × 100 mm × 10 mm angle) is placed above the window over the full opening width; it is modelled as a beam element with the given steel properties.
- Boundary conditions: left vertical edge (symmetry) has zero horizontal displacement and zero vertical traction. Right vertical edge is free (zero tractions).
- Imposed displacements on the top and bottom edges of the panel: vertical displacements follow the effective deflection profile (determined from Step 2) scaled by a central displacement factor u from 0 to at least 2.9 mm in 0.1 mm increments. Horizontal displacements are computed as y·∂δ/∂x, where y = 150 mm (distance from beam surface to the neutral axis of the 300 mm deep beam) and ∂δ/∂x is the slope of the deflection profile.

## Reproduction target
Produce two data artifacts: (1) effective_deflections.csv containing the total and effective beam centre vertical deflections for each of the five floors of the building under long-term service loading; (2) parametric_curves.csv containing the evolution of maximum crack width w_max versus imposed centre displacement u for the first-floor masonry panel across the nine material combinations defined by the values of tensile strength and elastic modulus in the task specification (fracture energy fixed at 100 N/m). The deflection data define the boundary condition input to the crack simulation, and the parametric curves characterise the crack-width evolution as a function of material properties. The task is self-contained: all geometry, loading, and material details required to build the numerical models are provided in the problem statement and workflow steps.

## Assets

- GMSH: https://gmsh.info
- Open-source linear finite element solver

## Workflow steps

### Step 1: Compute elastic displacement fields for seven loading cases
- Role: process
- Action: Build a linear elastic finite element model of the five‑storey building frame as specified in the Input data section. Apply the seven loading cases defined there and record vertical displacement fields at beam centreline nodes.
- Evidence: `/app/outputs/elastic_displacements.json`

### Step 2: Effective long‑term beam deflections
- Role: scored (load-bearing)
- Action: Using the displacement fields from the previous step, apply the superposition formulas (accounting for construction sequence and service load factors) and multiply by the long‑term creep amplification factor to obtain effective long‑term vertical beam centre deflections for each floor. Compute total displacement and effective deflection for floors 1–5. Output effective_deflections.csv.
- Output file: `/app/outputs/effective_deflections.csv`
- Format: csv
- Contract: CSV with columns: floor (int), total_displacement_mm (float), effective_displacement_mm (float), effective_deflection_mm (float). One row per floor.
- Scoring: scored by hidden verifier

### Step 3: Parametric maximum crack width simulation
- Role: scored (load-bearing)
- Action: For the first‑floor masonry panel, impose boundary displacements proportional to the effective deflection profile at displacement levels from 0 to at least 2.9 mm in steps of 0.1 mm. For each combination of tensile strength f_t and elastic modulus E from Table 1 (G_F = 100 N/m), run a cohesive crack finite element simulation with exponential softening and record the maximum crack width w_max at each displacement step. Output parametric_curves.csv covering all nine material combinations.
- Output file: `/app/outputs/parametric_curves.csv`
- Format: csv
- Contract: CSV with columns: lambda_ch_mm (float), u_mm (float), w_max_mm (float). One row per displacement step per material combination.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/effective_deflections.csv`
- `/app/outputs/parametric_curves.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### effective_deflections.csv
- path: `/app/outputs/effective_deflections.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Effective beam centre vertical deflections per floor; the checker compares the first‑floor effective deflection to a hidden reference value and verifies that total displacement increases monotonically with floor number.
- schema:
  - `type`: table
  - `required_columns`: `floor`, `total_displacement_mm`, `effective_displacement_mm`, `effective_deflection_mm`

### parametric_curves.csv
- path: `/app/outputs/parametric_curves.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Maximum crack width versus imposed displacement for the parametric study; the checker groups by lambda_ch, fits linear models after crack initiation, recomputes slopes, and compares them against expected ductile/brittle regimes, also verifying w_max at hidden reference displacement points.
- schema:
  - `type`: table
  - `required_columns`: `lambda_ch_mm`, `u_mm`, `w_max_mm`

Notes: The checker does not require crack pattern images or the raw 3D displacement fields; only the two CSV files are scored. Tolerances are hidden and derived from the paper’s published data.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "effective_deflections.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "floor",
          "total_displacement_mm",
          "effective_displacement_mm",
          "effective_deflection_mm"
        ]
      },
      "description": "Effective beam centre vertical deflections per floor; the checker compares the first‑floor effective deflection to a hidden reference value and verifies that total displacement increases monotonically with floor number."
    },
    {
      "file": "parametric_curves.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "lambda_ch_mm",
          "u_mm",
          "w_max_mm"
        ]
      },
      "description": "Maximum crack width versus imposed displacement for the parametric study; the checker groups by lambda_ch, fits linear models after crack initiation, recomputes slopes, and compares them against expected ductile/brittle regimes, also verifying w_max at hidden reference displacement points."
    }
  ],
  "notes": "The checker does not require crack pattern images or the raw 3D displacement fields; only the two CSV files are scored. Tolerances are hidden and derived from the paper’s published data."
}
```

## How you are scored
Your submission will be assessed by a hidden verifier that independently examines each scored artifact. For effective_deflections.csv, the verifier checks that the total displacement increases monotonically with floor number and compares the first-floor effective deflection to a hidden reference derived from the original study. For parametric_curves.csv, the verifier groups the data by λ_ch, fits linear models to the post-initiation portion of each w_max vs u curve, and compares the resulting slopes against expected ductile and brittle regimes; it also verifies the crack width at several hidden displacement thresholds. Both artifacts contribute to the final reward according to a predetermined weight distribution. Reporting a single final number without producing the raw curves and deflection data will not earn credit. The hidden criteria enforce that the numerical pipeline – from the elastic frame analysis through the nonlinear cohesive-crack simulations – has been correctly executed.

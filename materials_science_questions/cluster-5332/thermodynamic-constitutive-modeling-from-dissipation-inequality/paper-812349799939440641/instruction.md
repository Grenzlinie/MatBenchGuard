# Shape Optimisation of a Structure under Diffusion-Driven Degradation

## Problem background
Engineering structures exposed to diffusing chemicals can undergo material degradation, altering their mechanical load‑bearing capacity over time. The coupled effect of mass diffusion and mechanical degradation poses a challenge for long‑term structural design, because chemically‑induced material loss can concentrate stresses and lead to premature failure. Predicting and mitigating this coupled behavior through geometric shape optimisation is therefore of practical importance. The target result demonstrates that an optimally shaped hole in a plate can significantly reduce the stress concentration caused by diffusion‑driven degradation.

## Approach
The core idea is to couple a diffusion‑driven degradation model with nonlinear finite‑deformation solid mechanics. A multiplicative decomposition of the deformation gradient separates the purely elastic response from an isotropic degradation stretch, which is driven by the evolving local chemical concentration. The mass sink is assumed proportional to the local concentration change, following a simplified reaction scheme. The material is modelled as a hyperelastic Neo‑Hookean solid with degradation‑dependent stiffness. The governing equations – balance of linear momentum and balance of mass for the concentration – are discretised in space using finite elements and integrated in time with a Newmark‑beta scheme. For shape optimisation, the semi‑axes of the elliptical hole are treated as design variables. Each candidate design is evaluated by a transient coupled FE analysis of a 50×50 cm plate with an elliptical hole, zero displacement on all outer edges, and a concentration inflow on the left edge that increases linearly from 100 mol/m³ to 400 mol/m³ over 4 days. The optimisation problem is solved with a gradient‑based sequential quadratic programming (SQP) method, using finite‑difference gradients. The objective is to minimise the maximum first principal stress (evaluated at the most highly loaded element), while a relative area‑loss constraint ensures material retention.

## Reproduction target
Your task is to use the coupled FE model and the shape optimisation procedure to find the optimal ellipse semi‑axes that minimise the maximum first principal stress in the plate, subject to a constraint that the relative change in solid area does not exceed 3%. The plate dimensions are 50 cm × 50 cm, with an elliptical hole. The initial design has semi‑axes s₁ = 10 cm and s₂ = 5 cm. The plate is subjected to a concentration inflow on its left edge that increases linearly from 100 mol/m³ to 400 mol/m³ over 4 days, while all outer edges are fixed against displacement. Material parameters are specified in the workflow steps. Your final submission must be a JSON file reporting the optimised semi‑axes s₁ and s₂ (in cm) and the resulting solid area (in cm²). The solid area is defined as the area of the plate (2500 cm²) minus the area of the hole (π·s₁·s₂).

## Assets

- FEniCS (or equivalent FE library): https://fenicsproject.org/
- SciPy: https://scipy.org/
- Gmsh: https://gmsh.info/
- NumPy: https://numpy.org/

## Workflow steps

### Step 1: Implement coupled FE model and generate mesh
- Role: process
- Action: Implement the coupled mechanical-diffusion-degradation finite element model using a Neo-Hookean mechanical energy, a chemical free energy, and Fickian diffusion. Implement the weak forms for the balance of linear momentum and mass balance of concentrations. Use the multiplicative decomposition of the deformation gradient with isotropic degradation driven by concentration. Set up the boundary value problem for a 50×50 cm plate with an elliptical hole (semi-axes s1, s2, initial s1=10 cm, s2=5 cm). Apply zero Dirichlet displacement on all edges. Apply a concentration inflow on the left side with a time profile: linear ramp from 100 mol/m³ to 400 mol/m³ over 4 days. Use material parameters: E=3 MN/cm², ν=0.2, ρ₀*=2000 kg/m³, M_γ=1 kg/mol, D=100 m²/day, initial concentration 100 mol/m³. Generate a Gmsh mesh for the geometry. Write a function that, given (s1,s2) and a time-stepping schedule (4 days with 1-day steps), runs the transient FE solver and returns the maximum first principal stress (sum over Gaussian points of the most loaded element) and the solid area (2500 − π·s1·s2 cm²).
- Evidence: none

### Step 2: Run shape optimisation loop
- Role: process
- Action: Perform gradient-based shape optimisation using SciPy's sequential quadratic programming (SQP) method with finite-difference gradients. The design parameters are the ellipse semi-axes s1, s2 (bounded [5,0] ≤ [s1,s2] ≤ [15,10] cm, initial [10,5] cm). The objective function is the sum of first principal stress at Gaussian points of the maximum-loaded element (as returned by the FE model). The constraint is the relative area loss: |(A_ini − A)/A_ini| − 0.03 ≤ 0, where A_ini = 2500 − π·10·5 cm² and A = 2500 − π·s1·s2 cm². At each iteration, the optimiser calls the FE analysis function for the candidate (s1,s2). Iterate until convergence (e.g., design parameter tolerance).
- Evidence: none

### Step 3: Extract optimised design
- Role: scored (load-bearing)
- Action: After the optimisation converges, write the final optimised ellipse semi-axes s1 (cm) and s2 (cm) and the solid area (cm²) to /app/outputs/opt_design.json. The area is computed as A = 2500 − π·s1·s2.
- Output file: `/app/outputs/opt_design.json`
- Format: json
- Contract: {"s1": "float (cm)", "s2": "float (cm)", "final_area": "float (cm²)"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/opt_design.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### opt_design.json
- path: `/app/outputs/opt_design.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Optimised ellipse semi-axes and solid area from shape optimisation under diffusion-driven degradation.
- schema:
  - `type`: object
  - `required`:
    - `s1`: number
    - `s2`: number
    - `final_area`: number
  - `properties`:
    - `s1`:
      - `type`: number
      - `description`: semi-axis length in cm
    - `s2`:
      - `type`: number
      - `description`: semi-axis length in cm
    - `final_area`:
      - `type`: number
      - `description`: solid area in cm²

Notes: The hidden checker compares s1 and s2 to the paper-reported optimum with an absolute tolerance of 0.1 cm. It also recomputes the solid area from s1 and s2 (A = 2500 − π·s1·s2 cm²) and verifies that the area constraint |(A_ini − A)/A_ini| − 0.03 ≤ 0 holds (A_ini = 2500 − π·10·5 cm²).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "opt_design.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "s1": "number",
          "s2": "number",
          "final_area": "number"
        },
        "properties": {
          "s1": {
            "type": "number",
            "description": "semi-axis length in cm"
          },
          "s2": {
            "type": "number",
            "description": "semi-axis length in cm"
          },
          "final_area": {
            "type": "number",
            "description": "solid area in cm²"
          }
        }
      },
      "description": "Optimised ellipse semi-axes and solid area from shape optimisation under diffusion-driven degradation."
    }
  ],
  "notes": "The hidden checker compares s1 and s2 to the paper-reported optimum with an absolute tolerance of 0.1 cm. It also recomputes the solid area from s1 and s2 (A = 2500 − π·s1·s2 cm²) and verifies that the area constraint |(A_ini − A)/A_ini| − 0.03 ≤ 0 holds (A_ini = 2500 − π·10·5 cm²)."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that reads your `opt_design.json`. The verifier compares the reported semi‑axes against a reference optimum obtained from a correct implementation of the described model (same boundary conditions, time profile, material parameters, and optimisation setup). It also recomputes the solid area from your s₁, s₂ and checks that the area constraint (relative area loss ≤ 3%) is satisfied. The reward reflects the accuracy of the shape parameters and strict fulfilment of the constraint; deviations that are within the expected spread of a genuine reproduction are not penalised. The verifier does not rely on any published table — it independently assesses the fidelity of your reproduction. Reporting a number without running the full computational pipeline will not yield a passing score.

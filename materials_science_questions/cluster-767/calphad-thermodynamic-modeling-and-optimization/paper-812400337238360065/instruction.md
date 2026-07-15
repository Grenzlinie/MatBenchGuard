# CALPHAD B2+B2* Phase Boundary Calculation in Fe-Al-Co Ternary

## Problem background
The Fe-Al-Co ternary system is an ordering alloy system in which two CsCl-type (B2) ordered phases — one richer in Al and one richer in Co — can coexist at intermediate temperatures, forming a closed miscibility gap known as the B2+B2* phase separation. This phase separation is driven by a combination of chemical mixing, ferromagnetic ordering, and chemical-ordering excess free energies. A thermodynamic model that adds these contributions can predict the equilibrium compositions of the two coexisting B2 phases. This task computes the B2+B2* phase boundary on the 873 K isothermal section by implementing the full free energy model and solving the common-tangent condition.

## Approach
The total molar Gibbs free energy is built from three additive contributions:

1. **Chemical free energy** — a regular-solution mixing model parameterised by three binary interaction parameters (Fe–Al, Fe–Co, Al–Co).

2. **Ferromagnetic excess free energy** — an Inden-type magnetic model that depends on the local Curie temperature of the ternary solid solution. The Curie temperature itself is expressed as a function of composition, and the magnetic reference free energy of pure Fe is evaluated at a scaled fictitious temperature.

3. **Ordering excess free energy** — a Bragg–Williams scaling treatment for the B2 superlattice. The ordering critical temperature of the ternary alloy and a composition-dependent scaling factor together determine the ordering contribution, with the reference ordering free energy of stoichiometric FeCo evaluated at a scaled fictitious temperature.

At the target temperature (873 K) the free energy surface is evaluated on a composition grid. For several fixed Co mole fractions, the common-tangent (equal chemical potential) condition is solved to locate the pair of equilibrium compositions corresponding to the two coexisting B2 phases. These compositions are the required phase-boundary coordinates.

## Reproduction target
Implement the full Gibbs free energy model described above using the numerical binary interaction parameters, the Curie-temperature expression, the magnetic reference function, the ordering critical temperature and scaling factor, and the ordering reference function, all as specified in the workflow step action. At T = 873 K, for constant Co mole fractions X_Co = 0.10, 0.15, 0.20, 0.25, and 0.30, determine the equilibrium compositions (X_Fe, X_Al, X_Co) of the two coexisting B2 phases by solving the common-tangent condition. Output the boundary coordinates as a CSV file (one row per phase per section).

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Compute B2+B2* phase boundary at 873 K
- Role: scored (load-bearing)
- Action: Implement the total molar Gibbs free energy as G = G_para + ΔG_ferro + ΔG_ord using the following explicit models: Chemical free energy: G_para = RT (X_Fe ln X_Fe + X_Al ln X_Al + X_Co ln X_Co) + Ω_FeAl X_Fe X_Al + Ω_FeCo X_Fe X_Co + Ω_AlCo X_Al X_Co (R = 8.314 J/(mol·K), convert to kJ). Ferromagnetic excess: ΔG_ferro = (1 - X_Al) * (T_c^m / 1043) * [Δ°G(T_m^*)]_ferro, with T_m^* = T * (1043 / T_c^m); T_c^m(K) = - (1138*X_Co + 370) / ( 0.237 + 0.357*sqrt((X_Co - 0.024)^2 + 0.028^2) ) * X_Al^2 + 1138*X_Co + 1043; [Δ°G(T)]_ferro (kJ/mol) = (9/2)*(T - 968.9 - sqrt((T - 968.9)^2 + 28832)). Ordering excess: ΔG_ord = f * (T_c^° / 1003) * [Δ°G(T_o^*)]_ord, with T_o^* = T * (1003 / T_c^°); T_c^°(K) = (1/R) * ( -S + sqrt( S + L * X_Fe * X_Al * X_Co ) ), where S = Ω_FeAl*X_Fe*X_Al + Ω_AlCo*X_Al*X_Co + Ω_FeCo*X_Fe*X_Co and L = Ω_FeAl^2 + Ω_AlCo^2 + Ω_FeCo^2 - 2*(Ω_FeAl*Ω_AlCo + Ω_AlCo*Ω_FeCo + Ω_FeCo*Ω_FeAl); use R=0.008314 kJ/(mol·K); f = max( (If X_Co < X_Fe then 2*X_Co else 2*X_Fe), (If X_Al < 0.5 then 2*X_Al else 2*(1 - X_Al)) ); [Δ°G(T)]_ord (kJ/mol) = (5.5/2)*(T - 746.1 - sqrt((T - 746.1)^2 + 50498)). Use Ω_FeAl=-23.1, Ω_FeCo=-16.6, Ω_AlCo=-31.9 kJ/mol. At T=873 K, for X_Co = 0.10, 0.15, 0.20, 0.25, 0.30, solve the common-tangent condition to find equilibrium compositions (X_Fe, X_Al, X_Co) of the two coexisting B2 phases and output as CSV.
- Output file: `/app/outputs/phase_boundary.csv`
- Format: csv
- Contract: CSV with columns: section_X_Co (float), phase (string, one of 'B2' or 'B2*'), X_Fe (float), X_Al (float), X_Co (float). One row per phase per section (10 rows total). The two rows for each section must have distinct phase labels and compositions satisfying X_Fe+X_Al+X_Co=1.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phase_boundary.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phase_boundary.csv
- path: `/app/outputs/phase_boundary.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Equilibrium compositions of the B2 and B2* phases for each constant X_Co section. The checker recomputes the phase boundary via the same thermodynamic model and compares the reported compositions (chiefly X_Al) to the recomputed gold within a pre-set tolerance.
- schema:
  - `type`: table
  - `required_columns`: `section_X_Co`, `phase`, `X_Fe`, `X_Al`, `X_Co`
  - `units`:
    - `section_X_Co`: molar fraction
    - `X_Fe`: molar fraction
    - `X_Al`: molar fraction
    - `X_Co`: molar fraction

Notes: Only the B2+B2* phase separation at 873 K is scored. The experimental A2+B2 region and microscopy results are not part of this task.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phase_boundary.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "section_X_Co",
          "phase",
          "X_Fe",
          "X_Al",
          "X_Co"
        ],
        "units": {
          "section_X_Co": "molar fraction",
          "X_Fe": "molar fraction",
          "X_Al": "molar fraction",
          "X_Co": "molar fraction"
        }
      },
      "description": "Equilibrium compositions of the B2 and B2* phases for each constant X_Co section. The checker recomputes the phase boundary via the same thermodynamic model and compares the reported compositions (chiefly X_Al) to the recomputed gold within a pre-set tolerance."
    }
  ],
  "notes": "Only the B2+B2* phase separation at 873 K is scored. The experimental A2+B2 region and microscopy results are not part of this task."
}
```

## How you are scored
A hidden verifier independently implements the same thermodynamic model, solves the common-tangent condition for the same set of fixed X_Co sections, and compares your reported equilibrium compositions to its own recomputed reference compositions. Credit is awarded based on how closely your coordinates match the verifier's recomputed values. The only scored output is `phase_boundary.csv`; it carries the full weight of the task. The verifier does not simply match your output to a lookup table — it re-runs the physics from first principles, so honest implementation is required.

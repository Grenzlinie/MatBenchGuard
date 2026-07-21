# Coupled layerwise theory for static analysis of piezoelectric sandwich beams

## Problem background
Piezoelectric sandwich beams combine high stiffness-to-weight ratio with sensing and actuation functions, making them attractive for adaptive structures. Designing such beams requires electromechanical models that accurately predict deflections, stresses, and electric potential for layered, heterogeneous constructions under mechanical and electrical loads, while remaining computationally efficient. Existing beam theories often neglect important interactions—such as the transverse normal strain induced by the piezoelectric coefficient $d_{33}$ or the explicit in-plane electric field when enforcing shear-stress continuity—or have a number of displacement unknowns that grows with the number of layers. This work develops a coupled layerwise theory that captures these effects with only three displacement variables and assesses its predictions against exact three-dimensional piezoelastic solutions. The present task is to implement this theory, compute its static response for several highly inhomogeneous beam test cases, and submit the results for automatic verification against the exact solutions.

## Approach
The coupled layerwise theory is formulated for a hybrid beam with an arbitrary number of orthotropic layers, some of which may be piezoelectric with poling along the thickness. The axial displacement is approximated as a combination of a third-order global variation and a layerwise linear (zigzag) variation. The electric potential is taken as piecewise linear across the thickness, with the number of interpolation points chosen to resolve the heterogeneity. The transverse shear stress continuity conditions at layer interfaces and the zero-shear-traction conditions at the top and bottom surfaces are satisfied exactly, even when the in-plane electric field is non-zero. The transverse displacement field is augmented by a contribution that accounts for the piezoelectric $d_{33}$ strain, so that the through-thickness variation of $w$ under applied potentials is captured correctly. The governing equations and boundary conditions are derived from a variational principle for piezoelectric media. For simply-supported beams, the coupled system of ordinary differential equations is solved analytically by expanding all field variables in Fourier sine/cosine series. Implementing this theory requires: encoding the beam layups and material constants, computing the stiffness matrices from the derived constants, assembling and solving the coupled linear system for each Fourier harmonic to obtain the primary displacement and potential unknowns, and then recovering stresses and non-dimensionalising the results according to the given formulas.

**Test beam configurations and material properties**

The analysis is performed for three simply-supported beams (denoted (a), (b), and (c)) that exhibit highly inhomogeneous stiffness and electromechanical properties. All plies are oriented at $\theta_k = 0^\circ$.

- **Beam (a)**: a five-ply elastic substrate topped with a PZT-5A layer of thickness $0.1h$. Substrate layup (from the bottom): material 1 (thickness $0.09h$), material 2 ($0.225h$), material 3 ($0.135h$), material 1 ($0.18h$), material 3 ($0.27h$). Top and bottom of the substrate are grounded.
- **Beam (b)**: a three-layer sandwich substrate with graphite-epoxy faces (material 3) of thickness $0.09h$ each, a soft core of thickness $0.72h$, and a top PZT-5A layer of $0.1h$. The core material constants are given below.
- **Beam (c)**: a two-layer piezoelectric laminate consisting of PZT-5A on top of PVDF, each of thickness $0.5h$, poled in opposite senses ($+z$ and $-z$).

The material constants (plane-stress reduced values for a beam of small width, with $\sigma_y = \tau_{yz} = \tau_{xy} = 0$, $\sigma_z \simeq 0$) are:

**Material 1** (isotropic): $Y_x = 6.9$ GPa, $G_{zx} = 1.38$ GPa, $\nu_{xz} = 0.25$.

**Material 2**: $Y_x = 224.25$ GPa, $G_{zx} = 56.58$ GPa, $\nu_{xz} = 0.25$.

**Material 3**: $Y_x = 172.5$ GPa, $G_{zx} = 3.45$ GPa, $\nu_{xz} = 0.25$.

**Core**: $Y_x = 0.276$ GPa, $G_{zx} = 0.414$ GPa, $\nu_{xz} = 0.02$.

**PZT-5A**: $Y_x = 61.0$ GPa, $G_{zx} = 21.1$ GPa, $\nu_{xz} = 0.38$. Piezoelectric strain constants: $d_{31} = -171 \times 10^{-12}$ m/V, $d_{33} = 374 \times 10^{-12}$ m/V, $d_{15} = 584 \times 10^{-12}$ m/V. Dielectric constants: $\eta_{11} = 1.53 \times 10^{-8}$ F/m, $\eta_{33} = 1.5 \times 10^{-8}$ F/m.

**PVDF**: $Y_x = 2.0$ GPa, $G_{zx} = 0.75$ GPa, $\nu_{xz} = 1/3$. Piezoelectric: $d_{31} = 23 \times 10^{-12}$ m/V, $d_{33} = -30 \times 10^{-12}$ m/V, $d_{15} = 0$. Dielectric: $\eta_{11} = \eta_{33} = 1.062 \times 10^{-10}$ F/m.

Two load cases are considered:
1. **Pressure load**: a sinusoidal pressure $p_z^2 = -p_0 \sin(\pi x/a)$ applied on the top surface, with the top electrode open-circuited ($q_{n_\phi} = 0$).
2. **Actuation load**: a sinusoidal electric potential $\phi^{n_\phi} = \phi_0 \sin(\pi x/a)$ applied on the top surface, with the top electrode closed-circuited.

The reference length scale $Y_T = 6.9$ GPa and $d_T = 374 \times 10^{-12}$ C/N are used for non-dimensionalisation.

## Reproduction target
Compute the following non-dimensional quantities using the coupled layerwise theory for the three beams described above and write them to `reproduced_results.json` according to the output schema.

**For beams (a) and (b)** under both load cases:
- Load case 1 (pressure, open-circuit): central deflection $\bar{w}$, maximum axial stress in the elastic substrate $\bar{\sigma}_x^e$, maximum axial stress at the top of the PZT layer $\bar{\sigma}_x^p$, maximum transverse shear stress $\bar{\tau}_{zx}$, and maximum electric potential on the top surface $\bar{\phi}$.
- Load case 2 (actuation potential, closed-circuit): central deflection $\tilde{w}$, same maximum axial stresses $\tilde{\sigma}_x^e$, $\tilde{\sigma}_x^p$, maximum transverse shear stress $\tilde{\tau}_{zx}$, and maximum electric displacement on the top surface $\tilde{D}_z$.

All quantities are evaluated at three slenderness ratios $S = a/h = 5$, $10$, and $100$.

**For beam (c)** at $S=5$ under both load cases:
- Load case 1 (pressure, closed-circuit on both surfaces): central deflection $\bar{w}$ (non-dimensionalised as for load case 1) and the through-thickness profile of electric potential $\phi$ at $x=a/2$, reported as a list of pairs $(z/h, \bar{\phi})$.
- Load case 2 (actuation potential, closed-circuit on both surfaces): central deflection $\tilde{w}$ (non-dimensionalised as for load case 2) and the through-thickness profile of electric potential $\tilde{\phi}$ at $x=a/2$.

**Non-dimensionalisation formulas**

For load case 1:
$$
\bar{w} = 100 \frac{Y_T}{h S^3 p_0} w, \qquad 
\bar{\sigma}_x = \frac{\sigma_x}{S^2 p_0}, \qquad 
\bar{\tau}_{zx} = \frac{\tau_{zx}}{S p_0}, \qquad 
\bar{\phi} = 10^4 \frac{Y_T d_T}{h S^2 p_0} \phi,
$$
with $p_0$ the amplitude of the applied sinusoidal pressure.

For load case 2:
$$
\tilde{w} = \frac{10}{S d_T \phi_0} w, \qquad 
\tilde{\sigma}_x = 0.1 \frac{h}{Y_T d_T \phi_0} \sigma_x, \qquad 
\tilde{\tau}_{zx} = \frac{S h}{Y_T d_T \phi_0} \tau_{zx}, \qquad 
\tilde{\phi} = \frac{\phi}{\phi_0}, \qquad 
\tilde{D}_z = \frac{h}{100 Y_T d_T^2 \phi_0} D_z.
$$

Here $a$ is the beam length, $h$ the total thickness, $Y_T = 6.9$ GPa and $d_T = 374 \times 10^{-12}$ C/N.

The output file must be placed at `/app/outputs/reproduced_results.json` and follow the exact JSON structure specified in the output contract.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Define beam configurations and load cases
- Role: process
- Action: Implement the material property constants and beam geometries for the three test beams (a), (b) and (c) as given in the paper's Section 4. Define the two load cases: pressure load and actuation potential.
- Evidence: none

### Step 2: Compute response using coupled layerwise theory
- Role: scored (load-bearing)
- Action: Implement the coupled layerwise theory (Section 2) and solve the governing equations analytically for simply-supported beams (Section 3) using Fourier series. For each beam (a, b, c), slenderness ratio (S=5,10,100), and load case (pressure or actuation potential), compute the non-dimensional central deflection, maximum stresses, electric potential/displacement, and for beam (c) the through-thickness electric potential profile at x=a/2. Non-dimensionalise quantities as defined in Section 4.
- Output file: `/app/outputs/reproduced_results.json`
- Format: json
- Contract: {"beam_a": {"load_case_1": {"S=5": {"w": float, "sigma_x_e": float, "sigma_x_p": float, "tau_zx": float, "phi": float}, "S=10": {...}, "S=100": {...}}, "load_case_2": {"S=5": {"w": float, "sigma_x_e": float, "sigma_x_p": float, "tau_zx": float, "D_z": float}, ...}}, "beam_b": {...}, "beam_c": {"load_case_1": {"S=5": {"w_center": float, "phi_profile": [{"z/h": float, "phi_nondim": float}, ...]}}, "load_case_2": {"S=5": {...}}}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/reproduced_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### reproduced_results.json
- path: `/app/outputs/reproduced_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Non-dimensional central deflection, maximum in-plane and shear stresses, electric potential (load case 1) or electric displacement (load case 2) for beams (a) and (b) at S=5,10,100; central deflection and through-thickness electric potential profile for beam (c) at S=5.
- schema:
  - `type`: object
  - `required`: `beam_a`, `beam_b`, `beam_c`
  - `properties`:
    - `beam_a`:
      - `load_case_1`:
        - `S=5`:
          - `w`: float
          - `sigma_x_e`: float
          - `sigma_x_p`: float
          - `tau_zx`: float
          - `phi`: float
        - `S=10`:
          - `w`: float
          - `sigma_x_e`: float
          - `sigma_x_p`: float
          - `tau_zx`: float
          - `phi`: float
        - `S=100`:
          - `w`: float
          - `sigma_x_e`: float
          - `sigma_x_p`: float
          - `tau_zx`: float
          - `phi`: float
      - `load_case_2`:
        - `S=5`:
          - `w`: float
          - `sigma_x_e`: float
          - `sigma_x_p`: float
          - `tau_zx`: float
          - `D_z`: float
        - `S=10`:
          - `w`: float
          - `sigma_x_e`: float
          - `sigma_x_p`: float
          - `tau_zx`: float
          - `D_z`: float
        - `S=100`:
          - `w`: float
          - `sigma_x_e`: float
          - `sigma_x_p`: float
          - `tau_zx`: float
          - `D_z`: float
    - `beam_b`:
      - `load_case_1`:
        - `S=5`:
          - `w`: float
          - `sigma_x_e`: float
          - `sigma_x_p`: float
          - `tau_zx`: float
          - `phi`: float
        - `S=10`:
          - `w`: float
          - `sigma_x_e`: float
          - `sigma_x_p`: float
          - `tau_zx`: float
          - `phi`: float
        - `S=100`:
          - `w`: float
          - `sigma_x_e`: float
          - `sigma_x_p`: float
          - `tau_zx`: float
          - `phi`: float
      - `load_case_2`:
        - `S=5`:
          - `w`: float
          - `sigma_x_e`: float
          - `sigma_x_p`: float
          - `tau_zx`: float
          - `D_z`: float
        - `S=10`:
          - `w`: float
          - `sigma_x_e`: float
          - `sigma_x_p`: float
          - `tau_zx`: float
          - `D_z`: float
        - `S=100`:
          - `w`: float
          - `sigma_x_e`: float
          - `sigma_x_p`: float
          - `tau_zx`: float
          - `D_z`: float
    - `beam_c`:
      - `load_case_1`:
        - `S=5`:
          - `w_center`: float
          - `phi_profile`: array of objects with keys 'z/h' (float) and 'phi_nondim' (float)
      - `load_case_2`:
        - `S=5`:
          - `w_center`: float
          - `phi_profile`: array of objects with keys 'z/h' (float) and 'phi_nondim' (float)

Notes: The hidden reference values are the exact 3D piezoelastic solutions reported in the paper against which the agent's computed results are compared using relative tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "reproduced_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "beam_a",
          "beam_b",
          "beam_c"
        ],
        "properties": {
          "beam_a": {
            "load_case_1": {
              "S=5": {
                "w": "float",
                "sigma_x_e": "float",
                "sigma_x_p": "float",
                "tau_zx": "float",
                "phi": "float"
              },
              "S=10": {
                "w": "float",
                "sigma_x_e": "float",
                "sigma_x_p": "float",
                "tau_zx": "float",
                "phi": "float"
              },
              "S=100": {
                "w": "float",
                "sigma_x_e": "float",
                "sigma_x_p": "float",
                "tau_zx": "float",
                "phi": "float"
              }
            },
            "load_case_2": {
              "S=5": {
                "w": "float",
                "sigma_x_e": "float",
                "sigma_x_p": "float",
                "tau_zx": "float",
                "D_z": "float"
              },
              "S=10": {
                "w": "float",
                "sigma_x_e": "float",
                "sigma_x_p": "float",
                "tau_zx": "float",
                "D_z": "float"
              },
              "S=100": {
                "w": "float",
                "sigma_x_e": "float",
                "sigma_x_p": "float",
                "tau_zx": "float",
                "D_z": "float"
              }
            }
          },
          "beam_b": {
            "load_case_1": {
              "S=5": {
                "w": "float",
                "sigma_x_e": "float",
                "sigma_x_p": "float",
                "tau_zx": "float",
                "phi": "float"
              },
              "S=10": {
                "w": "float",
                "sigma_x_e": "float",
                "sigma_x_p": "float",
                "tau_zx": "float",
                "phi": "float"
              },
              "S=100": {
                "w": "float",
                "sigma_x_e": "float",
                "sigma_x_p": "float",
                "tau_zx": "float",
                "phi": "float"
              }
            },
            "load_case_2": {
              "S=5": {
                "w": "float",
                "sigma_x_e": "float",
                "sigma_x_p": "float",
                "tau_zx": "float",
                "D_z": "float"
              },
              "S=10": {
                "w": "float",
                "sigma_x_e": "float",
                "sigma_x_p": "float",
                "tau_zx": "float",
                "D_z": "float"
              },
              "S=100": {
                "w": "float",
                "sigma_x_e": "float",
                "sigma_x_p": "float",
                "tau_zx": "float",
                "D_z": "float"
              }
            }
          },
          "beam_c": {
            "load_case_1": {
              "S=5": {
                "w_center": "float",
                "phi_profile": "array of objects with keys 'z/h' (float) and 'phi_nondim' (float)"
              }
            },
            "load_case_2": {
              "S=5": {
                "w_center": "float",
                "phi_profile": "array of objects with keys 'z/h' (float) and 'phi_nondim' (float)"
              }
            }
          }
        }
      },
      "description": "Non-dimensional central deflection, maximum in-plane and shear stresses, electric potential (load case 1) or electric displacement (load case 2) for beams (a) and (b) at S=5,10,100; central deflection and through-thickness electric potential profile for beam (c) at S=5."
    }
  ],
  "notes": "The hidden reference values are the exact 3D piezoelastic solutions reported in the paper against which the agent's computed results are compared using relative tolerances."
}
```

## How you are scored
Your submission is scored automatically by a hidden verifier that reads your `/app/outputs/reproduced_results.json` and compares each requested numerical value to a reference exact 3D piezoelastic solution (the hidden gold). For deflection and stress quantities, the verifier computes the relative absolute error; for electric potential and electric displacement, the absolute difference is used. A value is counted as correct if the error falls below a predefined tolerance. The final score is the fraction of correct values, with all entries roughly equally weighted, except that the through-thickness potential profile for beam (c) carries a lower contribution. The verifier also checks that the output file conforms to the required schema. No human judgement is involved; providing the correct output structure and values that pass the tolerance is sufficient to achieve a high score.

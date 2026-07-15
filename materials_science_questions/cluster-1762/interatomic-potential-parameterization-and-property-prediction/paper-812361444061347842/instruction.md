# Compute Potential Energy and Partition Functions for Methane and Tetrafluoromethane at the 5A Zeolite Window

## Problem background
Zeolite cavities connected by molecular-sized windows enable sorbate diffusion, which can be modeled as an activated rate process. Transition state theory relates the diffusivity to partition functions and potential energies of molecules in the cavity and in the window (the transition state). In type A zeolites, the 8‑membered oxygen window is the bottleneck. Computing the potential energy of a sorbate at the window centre and its vibrational frequency there allows estimation of the activation energy and pre‑exponential factor for diffusion, and reveals the rotational freedom of the sorbate in the transition state. This task focuses on two non‑polar molecules (methane and tetrafluoromethane) in 5A zeolite.

## Approach
Implement transition state theory for diffusion in 5A zeolite. First, compute dispersion (Kirkwood‑Müller and Slater‑Kirkwood) and repulsion (inverse 12th‑power) constants for each molecule with oxygen, calcium, and sodium ions, using published molecular parameters. Use the zeolite crystal structure (Broussard & Shoemaker, 1959) to sum dispersion, repulsion, and polarization contributions at the 8‑membered oxygen window centre. Calculate the potential profile normal to the window and fit a parabola to obtain the curvature. From the curvature, derive the harmonic vibration frequency and the two‑dimensional harmonic oscillator partition function f+. Compute the ideal‑gas translational partition function f_trans' and rotational partition function f_rot (tetrahedral symmetry) for both molecules. For each molecule, output the raw intermediate quantities (u', v, f+, f_rot, f_trans'). From these, a downstream checker will derive the pre‑exponential factor D* and activation energy E for both a freely rotating and a non‑rotating transition state, and determine which rotation model is consistent for each molecule.

## Reproduction target
Produce the raw intermediate quantities from the transition‑state analysis for methane (CH4) and tetrafluoromethane (CF4) in 5A zeolite: the potential energy u' (kcal/mol) at the window centre, the harmonic vibration frequency v (s⁻¹), the two‑dimensional oscillator partition function f+, the rotational partition function f_rot, and the gas‑phase translational partition function f_trans'. Write these to theoretical_data.json. The hidden verifier will then compute the theoretical pre‑exponential factors D* and activation energies E for both rotating and non‑rotating transition states, and assess which rotation model applies to each molecule.

## Assets

- Crystal structure of 5A zeolite (Broussard and Shoemaker, 1959): 10.1021/ja01488a013

## Molecular parameters

| Sorbate / Ion | α (10⁻²⁵ cm³) | χ (10⁻³⁰ cm³) | ρ₀ (10⁻⁸ cm) | Charge (e) |
|---------------|----------------|----------------|--------------|------------|
| CH₄           | 26             | 20.2           | 2.34         | 0          |
| CF₄           | 36.7           | —              | 2.67         | 0          |
| O^(−1/4)      | 14.7           | 17.7           | 1.4          | −1/4       |
| Ca²⁺          | 4.71           | 22.1           | 0.99         | +2         |
| Na⁺           | 1.8            | 6.95           | 0.98         | +1         |

## Workflow steps

### Step 1: Compute dispersion and repulsion constants
- Role: process
- Action: For CH4 and CF4, compute dispersion constants A_i and repulsion constants B_i for interactions with O^(−1/4), Ca++, and Na+ ions using Kirkwood-Müller and Slater-Kirkwood formulas. Use the molecular parameters (polarizabilities, magnetic susceptibilities, van der Waals radii, ion charges). For CH4 average the two dispersion estimates; for CF4 use the Slater-Kirkwood formula. Compute B_i via the isolated ion equilibrium condition.
- Evidence: `/app/outputs/constants_report.json`

### Step 2: Compute potential energy at window centre and curvature
- Role: process
- Action: Using the constants from the previous step and the zeolite lattice coordinates from Broussard and Shoemaker (1959), compute the potential energy of CH4 and CF4 at the centre of the 8‑membered oxygen window. Sum dispersion, repulsion, and polarization contributions. Compute the potential profile across the window plane by displacing the molecule normal to the window. Determine the potential energy u' at the centre and the curvature (second derivative or parabolic fit) near the centre.
- Evidence: `/app/outputs/potential_curvature.json`

### Step 3: Compute partition functions and output theoretical data
- Role: scored (load-bearing)
- Action: From the curvature obtained in the previous step, compute the harmonic vibration frequency v = (1/(2π)) * sqrt(curvature / m) for each molecule, where m is the molecular mass. Compute the two‑dimensional harmonic oscillator partition function f_plus. Compute the gas‑phase translational partition function f_trans_prime and rotational partition function f_rot for both molecules using standard statistical mechanics formulas (ideal gas, tetrahedral symmetry). Evaluate all partition functions (f_plus, f_trans_prime, f_rot) at the temperatures 250 K for CH4 and 400 K for CF4 (the mean experimental temperatures). Output the computed u', v, f_plus, f_rot, f_trans_prime to theoretical_data.json.
- Output file: `/app/outputs/theoretical_data.json`
- Format: json
- Contract: JSON object with top-level keys 'CH4' and 'CF4'. Each value is a dict with keys: 'u_prime' (float, kcal/mol), 'v' (float, s^-1), 'f_plus' (float), 'f_rot' (float), 'f_trans_prime' (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/theoretical_data.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### theoretical_data.json
- path: `/app/outputs/theoretical_data.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Each molecule's intermediate quantities: potential at window centre u', vibration frequency v, 2D oscillator partition function f_plus, rotational partition function f_rot, translational partition function f_trans_prime. The checker recomputes diffusivity parameters from these raw values.
- schema:
  - `type`: object
  - `required`:
    - `CH4`: object
    - `CF4`: object
  - `properties`:
    - `CH4`:
      - `type`: object
      - `required`: `u_prime`, `v`, `f_plus`, `f_rot`, `f_trans_prime`
      - `units`:
        - `u_prime`: kcal/mol
        - `v`: s^-1
        - `f_plus`: dimensionless
        - `f_rot`: dimensionless
        - `f_trans_prime`: dimensionless
    - `CF4`:
      - `type`: object
      - `required`: `u_prime`, `v`, `f_plus`, `f_rot`, `f_trans_prime`
      - `units`:
        - `u_prime`: kcal/mol
        - `v`: s^-1
        - `f_plus`: dimensionless
        - `f_rot`: dimensionless
        - `f_trans_prime`: dimensionless

Notes: CH4 partition functions must be evaluated at 250 K; CF4 partition functions at 400 K, as stated in the workflow step.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "theoretical_data.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "CH4": "object",
          "CF4": "object"
        },
        "properties": {
          "CH4": {
            "type": "object",
            "required": [
              "u_prime",
              "v",
              "f_plus",
              "f_rot",
              "f_trans_prime"
            ],
            "units": {
              "u_prime": "kcal/mol",
              "v": "s^-1",
              "f_plus": "dimensionless",
              "f_rot": "dimensionless",
              "f_trans_prime": "dimensionless"
            }
          },
          "CF4": {
            "type": "object",
            "required": [
              "u_prime",
              "v",
              "f_plus",
              "f_rot",
              "f_trans_prime"
            ],
            "units": {
              "u_prime": "kcal/mol",
              "v": "s^-1",
              "f_plus": "dimensionless",
              "f_rot": "dimensionless",
              "f_trans_prime": "dimensionless"
            }
          }
        }
      },
      "description": "Each molecule's intermediate quantities: potential at window centre u', vibration frequency v, 2D oscillator partition function f_plus, rotational partition function f_rot, translational partition function f_trans_prime. The checker recomputes diffusivity parameters from these raw values."
    }
  ],
  "notes": "CH4 partition functions must be evaluated at 250 K; CF4 partition functions at 400 K, as stated in the workflow step."
}
```

## How you are scored
A hidden verifier independently processes each step's artifact. It reads the raw intermediate quantities you submit (theoretical_data.json), recomputes the theoretical diffusivity parameters D* and E for both rotation models, and compares them against reference values using appropriate tolerances. It also checks whether the derived diffusivities are consistent with the correct rotational assignment for each molecule. The score is the weighted combination of these checks. Reporting the paper's numbers directly is not sufficient; the verifier evaluates the correctness of your computed raw quantities and the resulting derived properties.

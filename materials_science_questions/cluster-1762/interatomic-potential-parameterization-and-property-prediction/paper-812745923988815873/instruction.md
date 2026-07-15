# Fitting Effective Solid-State Pair Potentials for Rare Gas Solids

## Problem background
Accurate pairwise potentials for rare gas solids are essential for theoretical studies of matrix isolation, where guest atoms or molecules are trapped in a crystalline host. The host matrix structure and energy are controlled by the interactions between rare gas atoms. Pair potentials derived from gas‑phase measurements, while accurate for the isolated dimer, are known to yield significant errors when used to model the ideal face‑centered cubic crystal—the predicted lattice constant and the energy required to remove an atom from the crystal differ appreciably from the experimental values. To obtain effective solid‑state potentials without resorting to computationally expensive many‑body methods, one can introduce simple empirical modifications of the gas‑phase pair potential and fit the modification parameters so that the crystal properties match the experimentally measured lattice parameter and atomization energy. This task reproduces that parameterisation stage, yielding effective solid‑state pair potentials for Ne, Ar, Kr, and Xe.

## Approach
The approach is to start from the well‑established Aziz gas‑phase pair potentials for Ne, Ar, Kr, and Xe and to apply two parametric transformations that scale the potential (by α) and shift the internuclear coordinate (by β):

V_solid1(R) = α1 V_gas(β1+R)
V_solid2(R) = α2 V_gas(β2+R)

The parameters α and β are chosen so that a static ideal fcc crystal whose atoms interact via the transformed potential reproduces two experimentally known properties: the equilibrium lattice constant a and the atomization energy E_atom (the energy required to remove one atom from an infinite crystal). The experimental reference values are taken from Rościszewski et al. (Phys. Rev. B 62, 5482, 2000).

For each rare gas and each transformation, the determination proceeds as follows:
1. With α fixed at 1.0, the lattice constant of the fcc crystal is computed as a function of β. An iterative procedure adjusts β until the equilibrium lattice constant equals the experimental a.
2. Using the β found above (and still α=1), the atomization energy of an infinite crystal is estimated by computing the energy of a central atom interacting with spherical fragments of radii r = 6a, 8a, and 10a. These three values are extrapolated assuming a leading 1/r³ dependence: E_inf ≈ E(r) + C/r³.
3. The scale factor α is then set to α = E_exp / E_inf, where E_exp is the experimental atomization energy.

This yields a fully parameterised effective solid‑state potential for each rare gas and each modification. The work is purely computational; all required gas‑phase potential functions and experimental data are public.

## Reproduction target
Produce a JSON file containing, for each rare gas (Ne, Ar, Kr, Xe), the fitted parameters α1, β1, α2, β2 and the computed equilibrium lattice constants and atomization energies of the ideal fcc crystal when using the fitted potentials. The quantities to report are: alpha1, beta1, computed lattice constant a1, extrapolated atomization energy E_inf1 (for modification 1); and alpha2, beta2, computed a2, E_inf2 (for modification 2). Units: lattice constants in Å, energies in cm⁻¹. The file must be written to `/app/outputs/fitted_parameters.json` and must conform to the output schema described in the output contract. The verification checks that the submitted parameters are consistent with the experimental lattice constant and atomization energy references (within appropriate margins) and that they match the gold parameters obtained from the published procedure. You do not need to know the reference values; the hidden verifier handles the comparison.

## Assets

- Aziz gas‑phase pair potential for Ne: 10.1016/0301-0104(89)80280-1
- Aziz gas‑phase pair potential for Ar: 10.1063/1.465051
- Aziz gas‑phase pair potential for Kr: 10.1080/00268978900100711
- Aziz gas‑phase pair potential for Xe: 10.1016/0301-0104(90)89087-E
- Experimental lattice parameters and atomization energies for rare gas crystals (Rościszewski et al. 2000): 10.1103/PhysRevB.62.5482

## Workflow steps

### Step 1: Implement potentials and fit solid‑state modifications
- Role: process
- Action: Implement the Aziz gas‑phase pair potentials for Ne, Ar, Kr, Xe (using known functional forms and parameters from the literature). For each rare gas, apply two empirical transformations V_solid1(R)=α1 V_gas(β1+R) and V_solid2(R)=α2 V_gas(β2+R). Perform the iterative fitting protocol: (1) with α=1, adjust β until the equilibrium lattice constant of the ideal fcc crystal matches the experimental lattice parameter; (2) for that β, compute the atomization energy of an infinite fcc crystal by extrapolating from spherical fragments of radii 6a, 8a, 10a using E∞≈E(r)+C/r³; (3) set α = E_exp / E∞. Record all intermediate quantities for the next step.
- Evidence: `/app/outputs/fitting_log.txt`

### Step 2: Output fitted parameters and computed properties
- Role: scored (load-bearing)
- Action: Write a JSON file containing the fitted parameters α1, β1, α2, β2 and the computed equilibrium lattice constants and atomization energies for each rare gas (Ne, Ar, Kr, Xe).
- Output file: `/app/outputs/fitted_parameters.json`
- Format: json
- Contract: array of objects, each with fields: RG (string), alpha1 (number), beta1 (number), computed_a1 (number, Å), computed_E_inf1 (number, cm⁻¹), alpha2 (number), beta2 (number), computed_a2 (number, Å), computed_E_inf2 (number, cm⁻¹)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/fitted_parameters.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### fitted_parameters.json
- path: `/app/outputs/fitted_parameters.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Contains the fitted parameters (α,β) for the two solid‑state modifications of each rare gas, together with the corresponding computed lattice constants and atomization energies. The checker compares the parameters to hidden reference values (paper’s Table 1) with appropriate tolerances.
- schema:
  - `type`: array
  - `items`:
    - `RG`: string
    - `alpha1`: number
    - `beta1`: number
    - `computed_a1`: number
    - `computed_E_inf1`: number
    - `alpha2`: number
    - `beta2`: number
    - `computed_a2`: number
    - `computed_E_inf2`: number
  - `required`: `RG`, `alpha1`, `beta1`, `computed_a1`, `computed_E_inf1`, `alpha2`, `beta2`, `computed_a2`, `computed_E_inf2`
  - `units`:
    - `computed_a1`: Å
    - `computed_a2`: Å
    - `computed_E_inf1`: cm⁻¹
    - `computed_E_inf2`: cm⁻¹

Notes: Only the parameterization stage (Stage 1) of the full paper workflow is reproduced. The subsequent application to Na@Ar matrix isolation (site geometries, absorption spectra) is excluded as it requires additional potentials and simulation infrastructure beyond this fitting task.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "fitted_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "RG": "string",
          "alpha1": "number",
          "beta1": "number",
          "computed_a1": "number",
          "computed_E_inf1": "number",
          "alpha2": "number",
          "beta2": "number",
          "computed_a2": "number",
          "computed_E_inf2": "number"
        },
        "required": [
          "RG",
          "alpha1",
          "beta1",
          "computed_a1",
          "computed_E_inf1",
          "alpha2",
          "beta2",
          "computed_a2",
          "computed_E_inf2"
        ],
        "units": {
          "computed_a1": "Å",
          "computed_a2": "Å",
          "computed_E_inf1": "cm⁻¹",
          "computed_E_inf2": "cm⁻¹"
        }
      },
      "description": "Contains the fitted parameters (α,β) for the two solid‑state modifications of each rare gas, together with the corresponding computed lattice constants and atomization energies. The checker compares the parameters to hidden reference values (paper’s Table 1) with appropriate tolerances."
    }
  ],
  "notes": "Only the parameterization stage (Stage 1) of the full paper workflow is reproduced. The subsequent application to Na@Ar matrix isolation (site geometries, absorption spectra) is excluded as it requires additional potentials and simulation infrastructure beyond this fitting task."
}
```

## How you are scored
Each workflow stage’s output is independently evaluated by a hidden verifier that runs after your submission. The verifier reads your production artifacts from `/app/outputs` and compares them against hidden reference values that correspond to the correct fitted parameters and physical consistency checks. The primary scored artifact is `fitted_parameters.json`, which carries the full reward weight. The verifier checks that the reported α1, β1, α2, β2 match the expected parameters (derived from the same fitting protocol applied to the published Aziz potentials and experimental references) to within tolerances that account for implementation differences, and that the computed lattice constants and atomization energies are compatible with the experimental data. The reward is a single floating-point number between 0 and 1, representing the fraction of the required checks that are satisfied. Submitting numbers that are close to the true physical solution yields a high score; arbitrary or random numbers yield a low score.

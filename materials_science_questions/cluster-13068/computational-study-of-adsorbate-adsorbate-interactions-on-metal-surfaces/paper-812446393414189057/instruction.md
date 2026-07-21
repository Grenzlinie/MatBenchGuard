# Mean-field lattice-gas modeling of low-coverage hydrogen-induced reconstruction on W(001) and determination of interaction constants

## Problem background
The clean W(001) surface undergoes a reconstruction phase transition at low temperatures, and hydrogen adsorption strongly modifies this transition. Understanding the interaction between adsorbate ordering and surface distortion is key to catalysis and surface science. Experimental low-coverage phase diagrams provide coverage-dependent transition temperatures, but extracting the underlying microscopic interaction constants—specifically the energy difference between competing distortion directions and the force an adsorbed H exerts on surface W atoms—requires a quantitative theoretical model. This task aims to compute these two constants by implementing a lattice-gas/mean-field model and fitting to the experimental phase boundaries.

## Approach
The reconstruction is described with a short-range structural model where each surface W atom can displace along ⟨11⟩ or ⟨10⟩ directions. Adsorbed H atoms occupy bridge sites and couple to the local distortion, favoring one direction. The combined adsorbate–structure system is treated as a lattice gas with an effective Hamiltonian. Mean-field theory is applied to derive self-consistency equations for the structural order parameters and adsorbate coverage as functions of temperature and coverage. By solving these equations, one obtains the coverage- and temperature-dependent order parameters and free energies, allowing the construction of the low-coverage phase diagram. The unknown interaction parameters—the energy difference ΔE between ⟨11⟩ and ⟨10⟩ distortions (eV/atom) and the force constant f (eV/u₀) that an H atom exerts on a neighbor W atom—are then determined by fitting the model's phase boundaries to the provided experimental data using nonlinear least squares.

## Model specification

### Variable definitions
- **s_i** = ±1 : displacement state of W atom at site i; +1 corresponds to distortion along ⟨11⟩, −1 along ⟨10⟩.
- **θ** : hydrogen coverage (fraction of bridge sites occupied by H). Each W atom is associated with one adjacent bridge site that can host H.
- **Δ** : bare energy difference (eV/atom) between the two distortion directions on the clean surface; the Hamiltonian contribution is −Δ s_i.
- **f** : force constant (eV/u₀) coupling an adsorbed H to its neighboring W atom; an occupied bridge site contributes an energy −f s_i.
- **J** : nearest-neighbor coupling energy (eV) favoring parallel (ferro‑distortive) alignment of W displacements. Let z = 4 be the number of in‑plane nearest neighbors.
- **J_eff ≡ z J** : effective mean-field coupling constant (eV).

### Mean-field free energy (per W atom)
The total effective field acting on a W atom is

h_eff = Δ + f θ

In the Bragg–Williams (mean‑field) approximation, the free energy per atom reads

F(m, θ, T) = −k_B T  ln[ 2 cosh( (J_eff m + h_eff) / (k_B T) ) ]  +  (1/2) J_eff m²

where m = ⟨s⟩ is the average displacement order parameter. For simplicity, the ideal lattice‑gas entropy of hydrogen is assumed to contribute a constant shift for a fixed θ and is omitted in the minimization with respect to m.

### Self‑consistency equation
Minimizing F with respect to m yields

m = tanh( (J_eff m + Δ + f θ) / (k_B T) )      (1)

### Determination of J_eff
The clean‑surface transition temperature T_c₀ (θ = 0) can be read from the provided experimental data (see `exp_phase_diagram.csv`). In the limit Δ → 0 the model reduces to a standard mean‑field Ising ferromagnet with critical temperature T_c₀ = J_eff / k_B. For a first estimate, use

J_eff = k_B × T_c₀_read

where k_B = 8.617333262145×10⁻⁵ eV/K is the Boltzmann constant.

### Phase boundary calculation (first‑order coexistence line)
For a given coverage θ and model parameters (Δ, f, J_eff), Equation (1) may have one or two stable solutions (minima of F). The phase transition temperature T_coex(θ) is defined by the condition that the two stable solutions (if they exist) have equal free energy, i.e.

F(m₁, θ, T_coex) = F(m₂, θ, T_coex)

where m₁ and m₂ are the two non‑trivial solutions of (1) (m₁ ≠ m₂). For temperatures above the transition, only one solution exists. The coexistence curve terminates at the critical point, but for the low‑coverage regime an iterative bisection or scanning algorithm can locate the temperature where the free‑energy barrier vanishes and the two minima are degenerate.

Implementation recipe:
1. Fix Δ, f, J_eff, θ.
2. For a given T, solve (1) numerically (e.g., by iteration or root‑finding) for all stable magnetizations m.
3. Choose the two solutions that correspond to local minima of F.
4. Compute ΔF(T) = F(m₁) − F(m₂). Find the temperature T where ΔF = 0 (bisection or interpolation).
5. The resulting T_coex(θ) is the model phase boundary.

> Note: If Δ = f = 0, the boundary reduces to the second‑order line T_c₀ = J_eff/k_B. In the presence of a non‑zero field, the transition becomes first‑order and the coexistence temperature shifts below T_c₀.

## Reproduction target
Your goal is to produce a JSON file containing the two fitted interaction constants: the energy difference ΔE between ⟨11⟩ and ⟨10⟩ distortion directions (key `delta_E_11_vs_10`, in eV/atom) and the force constant f exerted by an adsorbed H atom on a surface W atom (key `force_H_W`, in eV/u₀, where u₀ is the clean-surface W atom displacement). The fit must be based on the experimental low-coverage phase diagram data bundled with this task (`exp_phase_diagram.csv`) and the mean-field model you implement. There are no other datasets or external resources needed; everything required to build the model is described in this instruction and publicly available packages.

## Assets

- Experimental low-coverage H/W(001) phase diagram data (`exp_phase_diagram.csv`)
  Columns:
    - `coverage` : hydrogen coverage (ML)
    - `transition_temperature` : measured phase boundary temperature (K)
- NumPy: https://pypi.org/project/numpy/
- SciPy: https://pypi.org/project/scipy/
- Physical constant: Boltzmann constant k_B = 8.617333262145e-5 eV/K

## Workflow steps

### Step 1: Implement mean-field model and compute phase diagram
- Role: process
- Action: Implement the short-range structural model of W(001) reconstruction coupled to a hydrogen lattice gas as described above. Solve the mean-field self-consistency equation (1) to obtain coverage- and temperature-dependent order parameters and free energies. Produce a function that maps model parameters (Δ, f, J_eff) and coverage to the nearest transition temperature T_coex(θ).
- Evidence: None (implementation only, no output file required).

### Step 2: Fit interaction constants to experimental data
- Role: scored (load-bearing)
- Action: Using the implemented model and the provided experimental phase diagram data (`exp_phase_diagram.csv`), perform a nonlinear least-squares fit to determine the energy difference Δ (eV/atom) and the force constant f (eV/u₀). Fix J_eff using the clean-surface data point as described. Write the best-fit values to `constants.json`.
- Output file: `/app/outputs/constants.json`
- Format: json
- Contract: {"delta_E_11_vs_10": float (eV/atom), "force_H_W": float (eV/u0)}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/constants.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### constants.json
- path: `/app/outputs/constants.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: This artifact contains the two interaction constants determined from the model fit: the energy difference between distortions along the ⟨11⟩ and ⟨10⟩ directions, and the force exerted on a surface W atom by an adsorbed H atom in an adjacent bridge site.
- schema:
  - `type`: object
  - `required`:
    - `delta_E_11_vs_10`: float (eV/atom)
    - `force_H_W`: float (eV/u0)
  - `items`: object
  - `required_columns`:
  - `units`: object

Notes: The experimental phase diagram data used for fitting is bundled as `exp_phase_diagram.csv`. The model implementation and fitting code are not predefined; the agent must construct them from the method description.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "delta_E_11_vs_10": "float (eV/atom)",
          "force_H_W": "float (eV/u0)"
        },
        "items": {},
        "required_columns": [],
        "units": {}
      },
      "description": "This artifact contains the two interaction constants determined from the model fit: the energy difference between distortions along the ⟨11⟩ and ⟨10⟩ directions, and the force exerted on a surface W atom by an adsorbed H atom in an adjacent bridge site."
    }
  ],
  "notes": "The experimental phase diagram data used for fitting is bundled as exp_phase_diagram.csv. The model implementation and fitting code are not predefined; the agent must construct them from the method description."
}
```

## How you are scored
After you submit your output artifacts, a hidden verifier reads your `/app/outputs/constants.json` and compares each constant to a hidden reference value. The comparison uses symmetric tolerances appropriate to the expected numerical spread of a re-implemented model. It checks both the energy difference and the force constant. Full credit is awarded if both values fall within their respective tolerance windows; partial credit is possible if only one is within tolerance. The verifier does not look at your code or logs; only the values in `constants.json` matter. Therefore, you must ensure your model implementation and fitting are correct enough to land within the unspecified but reasonable tolerances. The verifier's tolerance is not disclosed, so aim for an accurate reproduction of the model and fitting procedure as described.
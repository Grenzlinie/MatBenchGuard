# Parametric Study of Activation Barrier Reduction in Hydrogen Ion Discharge

## Problem background
The discharge of hydrogen ions at a metal/electrolyte interface, where a hydrated proton accepts an electron from the electrode and becomes chemisorbed, is a fundamental step in hydrogen evolution. The activation barrier for this process is influenced by the strong hydration of the proton, which places its electron-accepting level far above the metal Fermi level. Traditional descriptions treat the electron transfer as a radiationless tunneling event that occurs only at the crossing point of the reactant and product energy curves. When the electronic coupling between the proton and the metal is strong, however, resonant electron hopping and gradual bond formation become important and can significantly alter the adiabatic energy profile along the reaction coordinate. A proper treatment requires a model that includes chemisorption bonding, the continuous evolution of the adsorbate charge, and electron-electron correlation on the ion. This task investigates the reduction of the activation energy caused by such chemisorption effects, quantified as δE_act, and its dependence on the key model parameters: the coupling strength, the metal Fermi level, and the on-site Coulomb repulsion.

## Approach
The metal/electrolyte system is described by a modified Anderson-Newns impurity Hamiltonian. The metal electrode is represented by a single, semi-elliptical tight-binding d-band of width 4β (band edges at −2β and +2β in real energy). The hydrogen ion is modeled as a single adsorbate orbital whose effective energy ε_a depends on an internal reaction coordinate y: ε_a(y) = -I + L(y) + R(y) - eV_H, where I is the ionization energy, L(y) the hydration energy, R(y) a repulsive core energy, and V_H the electrostatic potential shift. The coupling between the adsorbate and the metal band states is taken constant (β'), leading to a hybridization strength parameter B = 2β'². On-site electron-electron correlation U is included within the unrestricted Hartree-Fock approximation, yielding a spin-dependent energy

ε_σ = ε_a(y) + U n_{-σ},   (1)

where n_σ is the expectation value of the occupation of spin σ.

All energies are measured in units of 2β (half the d-band width) unless otherwise noted.  In these units the band edges are ±1, the Fermi level ε_F is dimensionless, and all parameters B, U, ε_a, ε_F are numbers of order unity.

### Chemisorption energy integrals
The chemisorption energy change ΔE is obtained by solving the Hartree‑Fock equations.  For a given ε_a (and therefore ε_σ via (1)), the one‑electron contributions are

ΔE^{1σ} = 
* if  ε_σ + 1 − B > 0 :
  ΔE^{1σ} = (1/π) ∫_{1}^{ε_F} tan⁻¹_π C  dε,                                          (2a)
* if  ε_σ + 1 − B < 0 :
  ΔE^{1σ} = (1/π) ∫_{-1}^{ε_F} tan⁻¹_{-π} C  dε  +  ε_{lσ},                           (2b)

with

C = −B √(1 − ε²) / [ (B−1) ε + ε_σ ],                                                (3)

ε_{lσ} = [ (1−B) ε_σ + B √(2B + ε_σ² − 1) ] / (1 − 2B)  −  ε_F,   (for 1−2B ≠ 0).     (4)

**Important note on B=0.5:** Equation (4) is undefined when 1−2B=0, i.e., when B=0.5, because the denominator vanishes. When performing parameter sweeps, you must avoid sampling exactly B=0.5. Use values slightly away from 0.5 (e.g., 0.499, 0.501) or skip this point to prevent numerical errors.

The inverse tangent branches are defined as
* tan⁻¹_π  returns values in (0, π),
* tan⁻¹_{-π} returns values in (−π, 0).

These integrals must be evaluated numerically.

### Self‑consistency for the spin occupations
The occupation numbers must satisfy

n_σ = ∂ ΔE^{1σ} / ∂ ε_σ .                                                             (5)

Equation (5) is solved iteratively.  A practical scheme:
1. Start with an initial guess (e.g. n_σ = 0).
2. Compute ε_σ = ε_a + U n_{-σ}.
3. Evaluate ΔE^{1σ} via (2)–(4) and obtain n_σ numerically, for instance by symmetric finite difference:
   n_σ ≈ [ ΔE^{1σ}(ε_σ + δ) − ΔE^{1σ}(ε_σ − δ) ] / (2δ),   δ ≈ 10⁻⁴.
4. Update n_σ and repeat until max|n_σ^{(new)} − n_σ^{(old)}| < tolerance (e.g. 10⁻⁵).

The total chemisorption energy is then

ΔE(y) = ∑_σ ΔE^{1σ} − U n_σ n_{-σ} − ε_a(y).                                          (6)

### Uncoupled product energy and total adiabatic energy
Near the crossing point of the reactant and product curves the hydration and repulsion functions L(y) and R(y) can be approximated linearly with equal slopes.  Under this approximation the reactant energy E_R and the product energy without chemisorption E_P⁰ become linear functions of ε_F − ε_a.  The uncoupled activation energy E_act⁰ is defined as the height of the crossing point seen from the reactant well, but when calculating the barrier reduction

δE_act = E_act⁰ − E_act,                                                               (7)

the reactant‑well offset cancels.  It is therefore sufficient to adopt the simple linear form

E_P⁰(ε_a) = ε_a − ε_F                     (in units of 2β),                           (8)

which vanishes at the diabatic crossing ε_a = ε_F.

The total adiabatic energy (the coupled ground state) is

E(ε_a) = E_P⁰(ε_a) + ΔE(ε_a),                                                        (9)

and the coupled activation barrier (relative to the same reactant reference) is the maximum of E(ε_a).  Consequently

δE_act = − max_{ε_a} [ ε_a − ε_F + ΔE(ε_a) ].                                         (10)

To compute δE_act for a given parameter set (B, ε_F, U), scan a sufficiently wide range of ε_a (suggestion: ε_a ∈ [ε_F−4, ε_F+4]) with a fine step (say 0.01), evaluate (10), and record the resulting positive number.  The scan must be wide enough that the maximum is not at the boundaries.

### Parameter conventions and numerical values
The following physical constants (not directly used in the computation, but set the scale) are:
- Bare proton ionization energy: I = 13.6 eV
- Hydration energy at equilibrium: L(y₀) = 11.6 eV
- Core repulsion energy at equilibrium: R(y₀) ≈ 1 eV

All energies are measured in units of 2β.  The three sweeps are performed with these fixed reference values:
- Varying B:   ε_F = 0,  U = 3
- Varying ε_F: B = 3,  U = 3
- Varying U:   B = 3,  ε_F = 0

Choose a range and step for each varied parameter (e.g. B from 0.5 to 5, ε_F from −2 to 2, U from 1 to 5) such that monotonic trends are resolved and **each sweep contains at least 5 data points**. For the B sweep, ensure B ≠ 0.5 exactly (see note on equation (4)); you may sample values like 0.49, 0.51, or simply exclude 0.5.

## Reproduction target
Implement the Hartree-Fock solver described above and use it to compute the activation barrier reduction δE_act (expressed in units of 2β) for a range of parameter values. Specifically, carry out three separate one-dimensional sweeps: (i) vary B while keeping ε_F and U fixed; (ii) vary ε_F while keeping B and U fixed; (iii) vary U while keeping B and ε_F fixed. For each parameter point, record the parameter value and the resulting δE_act. **Every submitted δE_act must lie in the range [0, 10]** (in units of 2β); values outside this range will be considered invalid. The collected results must be written to the file `/app/outputs/results.json` in the exact format specified in the output contract: an object with the three keys `vary_B`, `vary_epsilon_F`, and `vary_U`, each containing an array of `{parameter_value, delta_E_act}` objects.

## Assets
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Implement Hartree-Fock solver
- Role: process
- Action: Implement the numerical self-consistent Hartree-Fock solver for the modified Anderson-Newns model including hydration contributions. The solver must take parameters (B, ε_F, U) as input, scan ε_a, solve for n_σ and ΔE, construct E(ε_a) via (9), and compute δE_act via (10).
- Evidence: `/app/outputs/solver_validation.log`

### Step 2: Parametric sweep of barrier reduction
- Role: scored (load-bearing)
- Action: Run the Hartree-Fock solver over the specified ranges for B, ε_F, and U. For each sweep, collect **at least 5 data points** and ensure that every computed δE_act is **within [0, 10]**. Avoid the singular point B=0.5 during the B sweep. Collect the results into three arrays and write them to results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: object with three fields: `vary_B`, `vary_epsilon_F`, `vary_U`; each field is an array of objects with numeric keys `parameter_value` and `delta_E_act`.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`
- `/app/outputs/solver_validation.log`

## Output contract
Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Scored artifact containing sweep results; the checker verifies monotonic trends: δE_act non-decreasing with B, non-increasing with ε_F, non-decreasing with U. Every δE_act must be in [0,10] and each sweep must have at least 5 points.
- schema:
  - `type`: object
  - `required`: `vary_B`, `vary_epsilon_F`, `vary_U`
  - `vary_B`:
    - `type`: array
    - `items`:
      - `type`: object
      - `required`: `parameter_value`, `delta_E_act`
      - `properties`:
        - `parameter_value`:
          - `type`: number
        - `delta_E_act`:
          - `type`: number
  - `vary_epsilon_F`:
    - `type`: array
    - `items`:
      - `type`: object
      - `required`: `parameter_value`, `delta_E_act`
      - `properties`:
        - `parameter_value`:
          - `type`: number
        - `delta_E_act`:
          - `type`: number
  - `vary_U`:
    - `type`: array
    - `items`:
      - `type`: object
      - `required`: `parameter_value`, `delta_E_act`
      - `properties`:
        - `parameter_value`:
          - `type`: number
        - `delta_E_act`:
          - `type`: number

## Self-check before finishing (optional, not scored)
A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [ "vary_B", "vary_epsilon_F", "vary_U" ],
        "vary_B": {
          "type": "array",
          "items": {
            "type": "object",
            "required": [ "parameter_value", "delta_E_act" ],
            "properties": {
              "parameter_value": { "type": "number" },
              "delta_E_act": { "type": "number" }
            }
          }
        },
        "vary_epsilon_F": {
          "type": "array",
          "items": {
            "type": "object",
            "required": [ "parameter_value", "delta_E_act" ],
            "properties": {
              "parameter_value": { "type": "number" },
              "delta_E_act": { "type": "number" }
            }
          }
        },
        "vary_U": {
          "type": "array",
          "items": {
            "type": "object",
            "required": [ "parameter_value", "delta_E_act" ],
            "properties": {
              "parameter_value": { "type": "number" },
              "delta_E_act": { "type": "number" }
            }
          }
        }
      },
      "description": "Scored artifact containing sweep results; the checker verifies monotonic trends: δE_act non-decreasing with B, non-increasing with ε_F, non-decreasing with U."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier will read your `/app/outputs/results.json` and evaluate the quality of the computed δE_act values. The scoring is based on whether the submitted barrier reductions are physically consistent with the model: the numbers must lie in a plausible range (explicitly, every δE_act must be between 0 and 10 inclusive, and each sweep must contain at least 5 data points) and must exhibit the correct qualitative parameter dependence that follows from the underlying Anderson-Newns Hamiltonian. No explicit reference values or tolerances are disclosed.
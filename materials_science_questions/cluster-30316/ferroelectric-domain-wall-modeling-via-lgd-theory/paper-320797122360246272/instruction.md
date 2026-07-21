# Domain wall localized modes in a uniaxial ferroelectric continuum model

## Problem background
In Landau–Ginzburg–Devonshire (LGD) theory for uniaxial ferroelectrics below the phase transition, the sample breaks into domains with opposite polarization. A domain wall separates two domains; there the order parameter (static ionic displacement) changes smoothly from the uniform bulk value in one domain to its negative in the other. This breaks translational symmetry and modifies the local vibrational properties. For walls that are wide compared to the lattice spacing, the static order parameter takes a kink profile. When small dynamic displacements are added, the equation of motion reduces to a one-dimensional Schr  ödinger-like problem whose effective potential is shaped by the domain wall. Bound states of this potential correspond to vibrational modes localized near the wall, whose frequencies split off from the soft optic branch of the uniform crystal.

## Approach
We model a single wide domain wall in a uniaxial ferroelectric within the continuum LGD approximation. The material is described by a mass M, stiffness coefficients c1 and c2, a quartic anharmonic constant b, a transition temperature Tc, and an operating temperature T<Tc. The Landau parameter α is extracted from the soft-mode frequency Ω0 in the paraelectric phase. First, the static equilibrium equation is solved to obtain the uniform bulk order parameter η and the domain wall width d. The uniform bulk squared frequency ω⊥² at in-plane wavevector q⊥=0 follows from the curvature of the free energy. Second, the dynamical equation for small phonon displacements is linearized (pseudo‑harmonic approximation) and separated into in-plane and perpendicular components, yielding a 1D Schr  ödinger‑like equation for the z‑component. The potential well is determined by the static order-parameter profile. The bound‑state eigenvalues of this equation give the frequencies of the vibrational modes trapped at the wall. The agent implements these analytical formulas, evaluates them with realistic BaTiO 3 -type parameters, and reports the derived quantities.

## Reproduction target
Using material parameters representative of BaTiO 3 (mass M, stiffness coefficients c1 and c2, quartic coefficient b, transition temperature Tc, and an operating temperature T<Tc), compute the static domain wall properties (η, d, ω⊥²) and the two localized mode frequencies ω_x1² and ω_x2² that follow from the wide‑wall continuum model. Also compute the energy gap Δω = ω⊥ − ω_x1 between the lower localized mode and the bulk optic branch. The results must be self-consistent with the analytic relations derived from the LGD theory. Produce the two JSON files:
- domain_wall_properties.json containing the selected material parameters and the derived static properties,
- local_mode_frequencies.json containing the squared frequencies and the energy gap squared.
The exact required fields and units are specified in the workflow steps and the output contract.

## Assets

- BaTiO3 material parameters (Vaks model)
- Python scientific computing packages: numpy scipy

## Workflow steps

### Step 1: Compute static domain wall profile
- Role: scored (load-bearing)
- Action: Select material parameters consistent with BaTiO3 from the literature (mass M, stiffness coefficients c1, c2, quartic coefficient b, transition temperature Tc, operating temperature T < Tc). Derive the Landau coefficient α from the soft-mode frequency Ω0 in the paraelectric phase above Tc using the relation MΩ0^2 = Mα(T_ref − Tc) for a reference temperature T_ref > Tc, ensuring a positive α. Compute the bulk order parameter η = sqrt(b/α(Tc−T)), the domain wall width d = sqrt(2c1/(b η^2)), and the bulk squared frequency ω⊥^2 = 2α(Tc−T) at in-plane wavevector q⊥=0. Output all parameters and derived quantities to domain_wall_properties.json.
- Output file: `/app/outputs/domain_wall_properties.json`
- Format: json
- Contract: {"d": float, "eta": float, "T": float, "Tc": float, "M": float, "c1": float, "c2": float, "b": float, "alpha": float, "omega_perp_sq": float (bulk squared frequency at q⊥=0)}
- Scoring: scored by hidden verifier

### Step 2: Solve localized mode frequencies
- Role: scored
- Action: Using the quantities from step_01, compute the two localized mode frequencies for wide domain walls by solving the bound-state eigenvalue problem of the Schrödinger-like equation in the continuum approximation. Report the squared frequencies ω_x1^2, ω_x2^2, the bulk squared frequency ω⊥^2, and the energy gap squared (Δω)^2 = (ω⊥ − ω_x1)^2. Output to local_mode_frequencies.json.
- Output file: `/app/outputs/local_mode_frequencies.json`
- Format: json
- Contract: {"omega_x1_sq": float, "omega_x2_sq": float, "omega_perp_sq": float, "gap_sq": float, "units": "rad^2/s^2"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/domain_wall_properties.json`
- `/app/outputs/local_mode_frequencies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### domain_wall_properties.json
- path: `/app/outputs/domain_wall_properties.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Static domain wall profile properties and material parameters. The checker recomputes η, d, and ω⊥² from the provided parameters, checks self-consistency within 1e-6 relative tolerance, and verifies that the computed gap derived in the next step falls in the expected range.
- schema:
  - `type`: object
  - `required`: `d`, `eta`, `T`, `Tc`, `M`, `c1`, `c2`, `b`, `alpha`, `omega_perp_sq`
  - `items`: object
  - `required_columns`:
  - `units`:
    - `d`: cm
    - `eta`: dimensionless
    - `T`: K
    - `Tc`: K
    - `M`: g
    - `c1`: erg·cm²
    - `c2`: erg·cm²
    - `b`: erg/cm⁴
    - `alpha`: s⁻²·K⁻¹
    - `omega_perp_sq`: rad²/s²

### local_mode_frequencies.json
- path: `/app/outputs/local_mode_frequencies.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Localized mode frequencies squared and energy gap squared. The checker recomputes these quantities from the parameters in step_01 and compares them to the reported values with a tight tolerance, then checks that the absolute gap Δω = sqrt(omega_perp_sq) - sqrt(omega_x1_sq) lies in the physically expected order-of-magnitude range for BaTiO₃.
- schema:
  - `type`: object
  - `required`: `omega_x1_sq`, `omega_x2_sq`, `omega_perp_sq`, `gap_sq`, `units`
  - `items`: object
  - `required_columns`:
  - `units`:
    - `omega_x1_sq`: rad²/s²
    - `omega_x2_sq`: rad²/s²
    - `omega_perp_sq`: rad²/s²
    - `gap_sq`: rad²/s²

Notes: The agent must choose typical BaTiO3 parameters that satisfy the paper's scaling relations and yield a gap within the stated order-of-magnitude range. No thin-wall results are required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "domain_wall_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "d",
          "eta",
          "T",
          "Tc",
          "M",
          "c1",
          "c2",
          "b",
          "alpha",
          "omega_perp_sq"
        ],
        "items": {},
        "required_columns": [],
        "units": {
          "d": "cm",
          "eta": "dimensionless",
          "T": "K",
          "Tc": "K",
          "M": "g",
          "c1": "erg·cm²",
          "c2": "erg·cm²",
          "b": "erg/cm⁴",
          "alpha": "s⁻²·K⁻¹",
          "omega_perp_sq": "rad²/s²"
        }
      },
      "description": "Static domain wall profile properties and material parameters. The checker recomputes η, d, and ω⊥² from the provided parameters, checks self-consistency within 1e-6 relative tolerance, and verifies that the computed gap derived in the next step falls in the expected range."
    },
    {
      "file": "local_mode_frequencies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "omega_x1_sq",
          "omega_x2_sq",
          "omega_perp_sq",
          "gap_sq",
          "units"
        ],
        "items": {},
        "required_columns": [],
        "units": {
          "omega_x1_sq": "rad²/s²",
          "omega_x2_sq": "rad²/s²",
          "omega_perp_sq": "rad²/s²",
          "gap_sq": "rad²/s²"
        }
      },
      "description": "Localized mode frequencies squared and energy gap squared. The checker recomputes these quantities from the parameters in step_01 and compares them to the reported values with a tight tolerance, then checks that the absolute gap Δω = sqrt(omega_perp_sq) - sqrt(omega_x1_sq) lies in the physically expected order-of-magnitude range for BaTiO₃."
    }
  ],
  "notes": "The agent must choose typical BaTiO3 parameters that satisfy the paper's scaling relations and yield a gap within the stated order-of-magnitude range. No thin-wall results are required."
}
```

## How you are scored
A hidden verifier, which you never see, reads your two JSON files. It independently recomputes η, d, and ω⊥² from the material parameters you reported, using the same analytic formulas, and checks that your reported values match within a tight tolerance (self-consistency). It then recomputes the localized mode frequencies and gap from those parameters and compares them to your reported numbers. Finally, it computes the absolute angular frequency gap Δω and verifies that its magnitude lies within the physically expected order-of-magnitude interval predicted by the model (without relying on a single reference number). The reward reflects both the self-consistency of your derivation and whether the gap falls in the correct range, with heavier weight on the load‑bearing static‑profile stage. Partial credit is possible for correct ordering and positivity even if the gap magnitude misses the expected range.

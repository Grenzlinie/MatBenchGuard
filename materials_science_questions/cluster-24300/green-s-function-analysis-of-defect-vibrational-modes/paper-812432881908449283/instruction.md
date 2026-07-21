# Lattice Green's Function Integrals and Phonon Scattering Cross Section

## Problem background
Phonon scattering from substitutional impurities in crystals plays a central role in thermal transport and can give rise to resonant effects that affect low-temperature heat conduction. This problem concerns a simple cubic lattice with nearest-neighbour central and non-central forces, where a single impurity atom may differ from the host atoms in both mass and force constants. Exact closed-form expressions for the scattering amplitudes are obtained by decomposing the lattice Green's function into partial waves classified by the point group of the crystal. The key quantities that enter these expressions are certain integrals involving products of Bessel functions, whose numerical evaluation is required to obtain the scattering amplitudes and the total scattering cross section. The computational task is to evaluate these Green's function integrals for a range of energy values and to compute the total cross section for an isotope impurity, thereby validating the theoretical framework.

## Approach
The lattice Green's function for the simple cubic lattice with nearest-neighbour interactions can be expressed in the form of a product of three Bessel functions multiplied by a complex exponential, integrated over a semi-infinite interval. The real and imaginary parts, denoted C(p,q,r) and S(p,q,r), are obtained by numerically integrating the cosine-weighted and sine-weighted products of Bessel functions, respectively, for specific combinations of Bessel-function orders (p,q,r). These integrals are evaluated for energy parameter E ranging from 0.0 to 7.0 in steps of 0.1. The resulting table of integrals is then used to compute the total scattering cross section for a forward-scattering configuration via the optical theorem applied to the S-wave scattering amplitude. The computation follows a two-stage pipeline: first, numerical integration to produce the table of C and S values; second, extraction of the relevant Green's function component at the specified energy and substitution into the closed-form expression for the cross section, which depends on the mass change ratio and the direction of the incident phonon.

## Reproduction target
1. Compute a table of the Green's function integrals C(p,q,r) and S(p,q,r) for a simple cubic lattice. The integrals are defined as C(p,q,r) = ∫₀^∞ cos(Et) Jₚ(t) J_q(t) J_r(t) dt and S(p,q,r) = ∫₀^∞ sin(Et) Jₚ(t) J_q(t) J_r(t) dt. Evaluate these for energy parameter E from 0.0 to 7.0 in steps of 0.1, for the combinations (p,q,r) = (0,0,0), (1,0,0), (1,1,0), (2,0,0). Write the results as a CSV file with columns E, S000, C000, C100, S100, S110, C110, S200, C200.
2. Compute the total scattering cross section σ_T for an isotope impurity (force constant change Δγ = 0) with mass ratio ΔM/M = 2, energy E = 2.0, and incident phonon propagating along the [100] direction. Use the formula that follows from the optical theorem for the S-wave scattering amplitude, expressed in terms of the Green's function component I(0,0,0) at that energy. Output the cross section in units of a² (lattice constant squared) together with the input parameters as a JSON object.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Compute Green's function integrals
- Role: scored (load-bearing)
- Action: Compute the real parts C(p,q,r) and imaginary parts S(p,q,r) of the lattice Green's function integrals I(p,q,r) for a simple cubic lattice with nearest-neighbour interactions. Use I(p,q,r) = i^{p+q+r+1} ∫_0^∞ J_p(t) J_q(t) J_r(t) exp(-iEt) dt, where C(p,q,r) = ∫_0^∞ cos(Et) J_p(t) J_q(t) J_r(t) dt and S(p,q,r) = ∫_0^∞ sin(Et) J_p(t) J_q(t) J_r(t) dt. Evaluate for energy parameter E from 0.0 to 7.0 in steps of 0.1 for the combinations (p,q,r): (0,0,0), (1,0,0), (1,1,0), (2,0,0).
- Output file: `/app/outputs/integrals.csv`
- Format: csv
- Contract: CSV with header: E,S000,C000,C100,S100,S110,C110,S200,C200. E from 0.0 to 7.0 inclusive, step 0.1. All values floating point.
- Scoring: scored by hidden verifier

### Step 2: Compute total scattering cross section
- Role: scored
- Action: First determine the wave number k. From the lattice dispersion relation ω²(k) = (2γ/M)(1 − cos k) for propagation along [100], and the energy parameter definition E = 3 − Mω²/(2γ), obtain E = 2 + cos k. For E=2.0, cos k = 0, so k = π/2. Then compute the complex Green's function component I(0,0,0) = S(0,0,0) + i C(0,0,0) at E=2.0 from your integrals table. The total scattering cross section for an isotope impurity (Δγ=0) is given by σ_T = (1/(γ k)) (ΔM)² ω⁴/(2γ) Im(I(0,0,0)) / |1 − (ΔM ω²/(2γ)) I(0,0,0)|². With the elastic condition Mω²/(2γ)=1 and ΔM/M=2, this simplifies to σ_T = (8/k) Im(I(0,0,0)) / |1 − 2 I(0,0,0)|². The result is in units of the lattice constant squared (a²).
- Output file: `/app/outputs/cross_section.json`
- Format: json
- Contract: JSON object with keys: 'sigma_T' (float, value in units of lattice constant squared a²), 'parameters' (dict with keys 'E', 'DeltaM_over_M', 'Delta_gamma', 'propagation_direction').
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/integrals.csv`
- `/app/outputs/cross_section.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### integrals.csv
- path: `/app/outputs/integrals.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Table of Green's function integrals for a simple cubic lattice.
- schema:
  - `required_columns`: `E`, `S000`, `C000`, `C100`, `S100`, `S110`, `C110`, `S200`, `C200`

### cross_section.json
- path: `/app/outputs/cross_section.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Total scattering cross section for an isotope impurity.
- schema:
  - `type`: object
  - `required`: `sigma_T`, `parameters`
  - `properties`:
    - `sigma_T`:
      - `type`: number
    - `parameters`:
      - `type`: object
      - `required`: `E`, `DeltaM_over_M`, `Delta_gamma`, `propagation_direction`

Notes: The resonance analysis (Figures 1-2) is explicitly excluded from the scored targets per the upstream taskability scope, as it requires root-finding of complex functions.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "integrals.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "required_columns": [
          "E",
          "S000",
          "C000",
          "C100",
          "S100",
          "S110",
          "C110",
          "S200",
          "C200"
        ]
      },
      "description": "Table of Green's function integrals for a simple cubic lattice."
    },
    {
      "file": "cross_section.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "sigma_T",
          "parameters"
        ],
        "properties": {
          "sigma_T": {
            "type": "number"
          },
          "parameters": {
            "type": "object",
            "required": [
              "E",
              "DeltaM_over_M",
              "Delta_gamma",
              "propagation_direction"
            ]
          }
        }
      },
      "description": "Total scattering cross section for an isotope impurity."
    }
  ],
  "notes": "The resonance analysis (Figures 1-2) is explicitly excluded from the scored targets per the upstream taskability scope, as it requires root-finding of complex functions."
}
```

## How you are scored
After you submit the solution, a hidden verifier will independently inspect each output artifact. For the integrals table, the verifier recomputes the integral values at selected energy points and compares your results to the expected correct values using an appropriate precision tolerance. For the cross section, the verifier recomputes the cross section from the relevant Green's function component (either extracted from your table or from its own correct reference) and compares the value. The final reward is a weighted combination of the scores from the two workflow steps; simply reporting a number is not sufficient—the verifier judges the actual numerical content of the submitted files.

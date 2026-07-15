# Homogeneous Neutron Star Global Non-Radial Mode Periods

## Problem background
Neutron stars are compact objects in which degenerate neutron matter is in hydrostatic equilibrium under self-gravity. The oscillatory behavior of such stars provides a direct probe of the elastic properties of dense nuclear matter. Global non-radial pulsations, in particular spheroidal and torsional modes, are predicted by elastodynamic models that treat the stellar interior as an incompressible, highly elastic Fermi-continuum. Computing the periods of these modes for a simple homogeneous neutron star model establishes a baseline for understanding vibrational stability and characteristic timescales, and exposes the interplay between elastic restoring forces and gravitational attraction.

## Approach
Model the neutron star as a uniform, incompressible sphere of pure neutron matter with a constant density. The degenerate equation of state relates the local Fermi pressure to the neutron Fermi velocity. Under Newtonian gravity, the stellar radius follows from the condition that pressure vanishes at the surface (hydrostatic equilibrium). The eigenfrequencies of non-radial, gravitational-elastic spheroidal (s) and torsional (t) modes are obtained from the Rayleigh–Ritz energy variational principle, with perturbations confined to the volume in the Cowling approximation. For the homogeneous model, the resulting squared frequencies depend only on the stellar mass, density, and the multipole order L. Implement these analytic formulas for L = 2, 3, 4, convert the angular frequencies to periods, and store the six periods. The entire calculation uses basic physical constants and can be carried out with standard scientific Python libraries; no external dataset is required.

## Reproduction target
For a neutron star with mass M = 1.0 M⊙ (solar mass) and uniform density ρ = 2.8×10¹⁴ g cm⁻³, compute the stellar radius R from the zero-surface-pressure condition (balancing internal Fermi pressure against gravitational compression). Then evaluate the analytic expressions for the squared eigenfrequencies of spheroidal (ωₛ²) and torsional (ωₜ²) non-radial modes for multipole orders L = 2, 3, 4. Convert these angular frequencies to periods P = 2π/ω and output all six periods, in milliseconds, as a JSON object with keys spheroidal_L2, spheroidal_L3, spheroidal_L4, torsional_L2, torsional_L3, torsional_L4. The correctness of the submitted periods will be verified externally against reference values derived from the same homogeneous model.

## Assets

- Python scientific libraries (numpy, scipy): numpy scipy

## Workflow steps

### Step 1: Compute homogeneous model eigenperiods
- Role: scored (load-bearing)
- Action: Derive the neutron Fermi velocity from the degenerate equation of state for pure neutron matter. Using the standard homogeneous model parameters (mass M = 1.0 solar mass, uniform density ρ = 2.8×10^14 g/cm^3), compute the stellar radius R from the zero‑surface‑pressure condition (balancing internal Fermi pressure and gravitational pressure). Then evaluate the analytic formulas for the squared eigenfrequencies of spheroidal and torsional non‑radial modes for multipole orders L = 2, 3, 4. Convert the angular frequencies to periods P = 2π/ω (in milliseconds) and output all six periods to periods.json.
- Output file: `/app/outputs/periods.json`
- Format: json
- Contract: {"spheroidal_L2": <float: period in ms>, "spheroidal_L3": <float: ms>, "spheroidal_L4": <float: ms>, "torsional_L2": <float: ms>, "torsional_L3": <float: ms>, "torsional_L4": <float: ms>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/periods.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### periods.json
- path: `/app/outputs/periods.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Periods of the spheroidal and torsional gravitational‑elastic eigenmodes for multipole orders L = 2, 3, 4, computed for a homogeneous neutron star of mass 1.0 solar mass and uniform density 2.8×10^14 g/cm³. All periods are in milliseconds.
- schema:
  - `type`: object
  - `required`:
    - `spheroidal_L2`: float (milliseconds)
    - `spheroidal_L3`: float (milliseconds)
    - `spheroidal_L4`: float (milliseconds)
    - `torsional_L2`: float (milliseconds)
    - `torsional_L3`: float (milliseconds)
    - `torsional_L4`: float (milliseconds)

Notes: All model parameters are public and provided in the task description. The agent must implement the analytic formulas from first principles; no external data download is needed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "periods.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "spheroidal_L2": "float (milliseconds)",
          "spheroidal_L3": "float (milliseconds)",
          "spheroidal_L4": "float (milliseconds)",
          "torsional_L2": "float (milliseconds)",
          "torsional_L3": "float (milliseconds)",
          "torsional_L4": "float (milliseconds)"
        }
      },
      "description": "Periods of the spheroidal and torsional gravitational‑elastic eigenmodes for multipole orders L = 2, 3, 4, computed for a homogeneous neutron star of mass 1.0 solar mass and uniform density 2.8×10^14 g/cm³. All periods are in milliseconds."
    }
  ],
  "notes": "All model parameters are public and provided in the task description. The agent must implement the analytic formulas from first principles; no external data download is needed."
}
```

## How you are scored
A hidden verifier reads the submitted `periods.json` file and independently compares each of the six periods against a reference set within an appropriate tolerance that accounts for legitimate numerical differences between implementations. Each period that falls within the tolerance earns an equal share of the reward; the total reward is the proportion of matching periods. As an additional stability check, all periods must be positive. The final score is computed automatically from these comparisons; no other artifacts are assessed.

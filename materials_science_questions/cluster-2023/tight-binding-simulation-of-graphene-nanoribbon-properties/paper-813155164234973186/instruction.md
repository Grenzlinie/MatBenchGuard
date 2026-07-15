# Tight-Binding NEGF Simulation of Curved Graphene Nanoribbon Cooling

## Problem background
Nanoscale electronics require targeted, adjustable cooling. Conventional semiconductor Peltier coolers use fixed doping, limiting dynamic control of cooling power. Curvature-induced doping in graphene offers an alternative: the local curvature shifts the Dirac point, creating p‑type and n‑type regions without gating or lithography. A single continuous graphene nanoribbon (GNR) draped over an array of curved cylindrical protrusions (such as bent nanotubes) forms a series of p‑n junctions that are electrically in series but thermally in parallel, allowing heat to be pumped perpendicular to the substrate. This task aims to compute the cooling power density of such a curvature‑engineered GNR‑based Peltier device using a tight‑binding quantum transport approach.

## Approach
This reproduction uses the Nonequilibrium Green's Function (NEGF) method to compute the thermoelectric transport properties of an armchair metallic GNR and combines them with curvature‑induced Dirac‑point shifts to estimate the cooling power.

First, a tight‑binding Hamiltonian is constructed for a GNR of given dimensions using standard graphene parameters. The ballistic transmission coefficient is obtained via NEGF. To account for disorder, a phenomenological elastic scattering correction is applied using a backscattering mean‑free path, yielding the quasiballistic transmission T(E). From T(E) the Seebeck coefficient and electrical conductance are derived as functions of the chemical potential via the standard Landauer–Büttiker transport integrals (the L_n functions).

Independently, for two target curvature geometries, the mean curvature H of the GNR surface is computed, and the corresponding Dirac‑point energy shifts Φ are obtained from the known scaling law Φ ∝ H². These shifts are mapped to effective n‑type and p‑type doping levels. The previously computed Seebeck coefficient and conductance curves are then used to obtain the p‑ and n‑type Seebeck values and the junction resistance. Finally, the cooling power per junction is calculated from the Seebeck difference and resistance at zero temperature difference, and converted to an area‑normalized power density. The detailed procedure is laid out in the workflow steps below.

## Reproduction target
For a GNR with fixed in‑plane dimensions L_x = 75 nm (transport direction) and L_y = 25 nm (transverse direction), bent into a cylindrical shape with radius r = L_y/π and R = L_x/θ_x, compute the cooling power density (in kW/cm²) for exactly two curvature angles:

1. θ_x = π/2
2. θ_x = 2π/3

All intermediate calculations must use:
- Armchair metallic GNR tight‑binding model: nearest‑neighbor distance a = 2.5 Å, hopping t = −2.7 eV, on‑site energy 0 eV.
- Elastic disorder correction with backscattering mean‑free path λ = 400 nm.
- Curvature‑induced doping parameter α = 9.23 eV and the square of the nearest‑neighbor distance a² = (2.5 Å)².
- Device temperature T_C = 300 K, and the cooler is operated under zero temperature difference (ΔT = 0).
- The final cooling power densities must account for the GNR footprint per junction and be reported in kW/cm².

Write the two computed values to `/app/outputs/cooling_power.json` as a JSON object with keys `theta_x_pi_over_2` and `theta_x_2pi_over_3`. The supporting intermediate data (Seebeck coefficient S(μ) and electrical conductance g(μ)) should also be saved to `/app/outputs/seebeck_conductance.json` for documentation, though only the cooling power file is directly scored.

## Assets

- Graphene tight-binding parameters
- Curvature‑induced doping parameters
- NEGF transport computation
- Python scientific computing stack

## Workflow steps

### Step 1: Setup tight-binding model and compute ballistic transmission
- Role: process
- Action: Define an armchair metallic GNR of width Ly=25 nm (transverse) and length Lx=75 nm (transport direction) using nearest‑neighbour distance 2.5 Å and hopping -2.7 eV. Construct the channel Hamiltonian and the left/right contact self‑energies. Using the NEGF formalism, compute the energy‑dependent ballistic transmission coefficient T0(E) over a sufficiently dense energy grid.
- Evidence: none

### Step 2: Apply elastic disorder correction
- Role: process
- Action: Take the ballistic transmission T0(E) and apply the phenomenological elastic scattering correction with a backscattering mean‑free path λ=400 nm and system length L=75 nm: T(E) = T0(E) * λ/(λ+L).
- Evidence: none

### Step 3: Compute Seebeck coefficient and electrical conductance
- Role: process
- Action: At temperature T=300 K, compute the intermediate functions L_n(μ,T) from T(E) and the derivative of the Fermi function. Derive the electrical conductance g(μ)=e^2 L_0 and the Seebeck coefficient S(μ) = (1/(eT)) L_1/L_0 over a range of chemical potential μ spanning the Dirac point. Save the g(μ) and S(μ) data to /app/outputs/seebeck_conductance.json as arrays.
- Evidence: `/app/outputs/seebeck_conductance.json`

### Step 4: Compute curvature-induced Dirac-point shifts
- Role: process
- Action: For the two target geometries (θ_x = π/2 and θ_x = 2π/3) with Lx=75 nm, Ly=25 nm, r=Ly/π, R=Lx/θ_x, apply the mean curvature formula H = 1/2(1/R + 1/r) and the Dirac‑point shift expression Φ = -3α a² H² with α=9.23 eV, a=2.5 Å. Use appropriate signs for the inner (large mean curvature) and outer (small mean curvature) surfaces to obtain Φ1 and Φ2.
- Evidence: none

### Step 5: Compute cooling power density for the two geometries
- Role: scored (load-bearing)
- Action: Map the Dirac‑point shifts Φ1 and Φ2 to effective chemical potentials (accounting for charge neutrality). Extract the corresponding Seebeck coefficients S_n (n‑type) and S_p (p‑type) and the electrical conductance g from the previously computed g(μ) and S(μ) curves. Compute the electrical resistance R from g and the junction geometry. Calculate the cooling power for one element: P = (ΔS)² T_C² / (2R) with T_C=300 K, ΔT=0. Convert to power density in kW/cm² using the GNR footprint per junction. Report the two cooling power densities in /app/outputs/cooling_power.json.
- Output file: `/app/outputs/cooling_power.json`
- Format: json
- Contract: {"theta_x_pi_over_2": "float (kW/cm^2)", "theta_x_2pi_over_3": "float (kW/cm^2)"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/cooling_power.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### cooling_power.json
- path: `/app/outputs/cooling_power.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Cooling power density computed via the NEGF tight‑binding method for the two curvature geometries: θ_x = π/2 and θ_x = 2π/3.
- schema:
  - `type`: object
  - `required`:
    - `theta_x_pi_over_2`: number
    - `theta_x_2pi_over_3`: number
  - `units`:
    - `theta_x_pi_over_2`: kW/cm^2
    - `theta_x_2pi_over_3`: kW/cm^2

Notes: The supporting seebeck_conductance.json produced in step_03_thermoelectric is not scored but may be used for a lightweight structural audit.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "cooling_power.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "theta_x_pi_over_2": "number",
          "theta_x_2pi_over_3": "number"
        },
        "units": {
          "theta_x_pi_over_2": "kW/cm^2",
          "theta_x_2pi_over_3": "kW/cm^2"
        }
      },
      "description": "Cooling power density computed via the NEGF tight‑binding method for the two curvature geometries: θ_x = π/2 and θ_x = 2π/3."
    }
  ],
  "notes": "The supporting seebeck_conductance.json produced in step_03_thermoelectric is not scored but may be used for a lightweight structural audit."
}
```

## How you are scored
A hidden verifier will score your submitted `/app/outputs/cooling_power.json` against reference values derived from the original study. The score will reflect both the absolute accuracy of each cooling power density and the correct physical trend: the cooling power for θ_x = 2π/3 must exceed that for θ_x = π/2. The supporting intermediate evidence file `seebeck_conductance.json` may also be inspected for consistency with expected physical behavior (e.g., approximate magnitude and sign change of the Seebeck coefficient near the Dirac point) but does not directly contribute to the reward. Your final reward is a composite of these checks. Simply reporting plausible numbers without executing the full computational pipeline is unlikely to satisfy the scoring criteria, as the verifier can detect values that are inconsistent with the required NEGF transport calculation.

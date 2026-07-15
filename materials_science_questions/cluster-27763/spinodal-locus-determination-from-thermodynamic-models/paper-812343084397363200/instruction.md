# Mean-Field Free Energy Minimization for Capillary Bridging in Sphere-Plane Geometry

## Problem background
When a binary mixture is confined in a sphere-plane geometry, a capillary bridge can form, generating forces between the surfaces. This task uses a mean-field (phase-field) model to simulate the bridge for various sphere radii and surface separations. The goal is to compute the bridge’s excess free energy, determine the locus of zero excess free energy, and calculate the resulting force-distance curves.

## Approach
The bridge is described by a grand potential functional of the order parameter φ:

  Ω{φ} = ∫ dV [ (k/2) |∇φ|² + f(φ) − Δμ·φ ]

with the symmetric double‑well free‑energy density f(φ) = −a/2 φ² + b/4 φ⁴ (a = b = 4, k = 0.001).  The chemical potential difference Δμ = 0.1 drives the system away from coexistence.  The sphere and plane surfaces prefer the φ = −1 phase, implemented by the boundary condition φ = −1 on both solid surfaces.

The equilibrium φ field is obtained by minimizing the functional numerically using adaptive‑mesh finite elements.  From the equilibrium field one computes the grand potential of the bridged configuration and the reference unbridged configuration (thin wetting films, no bridge), and defines the excess free energy ΔΩ = Ω_bridge − Ω_reference.

Three quantities are extracted:
- ΔΩ as a function of sphere-plane separation for several sphere radii;
- the binodal transition line, i.e. the separation at which ΔΩ = 0, mapped to units of the thermodynamic length λ = σ/(2 Δμ φ_b);
- the force-distance curves F = −∂(ΔΩ)/∂h, scaled by σξ.

The correlation length ξ and interfacial tension σ are obtained from a preliminary one‑dimensional flat‑interface simulation that validates the finite‑element solver.

The workflow first performs that flat‑interface validation, then runs the sphere‑plane minimizations for a specified set of dimensionless radii r/ξ and separations h/ξ, post‑processes the results, and outputs the three data tables.

## Reproduction target
Produce three CSV files under /app/outputs:

1. **free_energy_curves.csv**  
   Columns: r_xi (float), h_xi (float), excess_free_energy (float).  
   Contains the excess free energy ΔΩ (in simulation units) for sphere radii r/ξ = 0.9, 2.0, 22.36, 44.72, each over a range of separations h/ξ covering the transition (suggested range 0.5 to 20; finer spacing near the zero‑crossing is helpful).  One row per computed configuration.

2. **transition_line.csv**  
   Columns: r_lambda (float), h_lambda (float).  
   Contains the binodal line: for at least 10 distinct radii covering r/λ from ≈0.1 to 100, report the separation h/λ where ΔΩ = 0.  λ = σ/(2 Δμ φ_b) with φ_b = 1 and σ obtained from the flat‑interface validation.

3. **force_curves.csv**  
   Columns: r_xi (float), h_xi (float), force_scaled (float).  
   Force F = −∂(ΔΩ)/∂h computed by centered finite differences on the (h, ΔΩ) data, scaled to dimensionless form F/(σξ).  Use the same radii and h range as in free_energy_curves.csv.

All simulations must use the free‑energy parameters a = b = 4, k = 0.001, and chemical potential difference Δμ = 0.1.  The finite‑element minimization can be carried out with an open‑source adaptive‑mesh library such as FEniCS or scikit‑fem.

## Assets

- Finite element library with adaptive meshing (e.g., FEniCS or scikit-fem): https://fenicsproject.org/
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Validate Finite Element Solver with Flat Interface
- Role: process
- Action: Implement the free energy functional Ω = ∫ dV[ (k/2)(∇φ)^2 + f(φ) - Δμ·φ ] with f(φ) = -a/2 φ^2 + b/4 φ^4 (a=b=4, k=0.001). Set up a 1D flat interface geometry with appropriate boundary conditions (φ = -1 at one end, +1 at the other). Perform finite element minimization with adaptive mesh to obtain the equilibrium order parameter profile φ(z). Fit the profile to φ(z) = φ_b tanh(z/ξ) to extract the correlation length ξ and compute interfacial tension σ = (2/3) a φ_b^2 ξ. Verify that the extracted ξ agrees with the analytical value ξ = √(2k/a) to within a small tolerance (e.g., 5%). This step validates the FE implementation before the full sphere-plane simulations.
- Evidence: `/app/outputs/validation_flat_interface.txt`

### Step 2: Compute Excess Free Energy Curves
- Role: scored (load-bearing)
- Action: For the sphere-plane geometry, set up the same free energy functional and boundary conditions (φ = -1 on the sphere and plane surfaces, which corresponds to the preferred phase). Use the chemical potential difference Δμ = 0.1, which yields λ/ξ ≈ 13.4 (λ = σ/(2 Δμ φ_b)). For each sphere radius r/ξ = 0.9, 2.0, 22.36, 44.72 and a range of separations h/ξ covering the transition (e.g., from ~0.5 up to ~15-20), minimize the functional numerically. For every (r/ξ, h/ξ) pair, compute the grand potential of the bridged configuration Ω_bridge and the reference unbridged configuration Ω_reference (thin wetting films, no bridge). The excess free energy is ΔΩ = Ω_bridge - Ω_reference. Record r/ξ, h/ξ, and the excess free energy (in simulation units). Save the data as free_energy_curves.csv.
- Output file: `/app/outputs/free_energy_curves.csv`
- Format: csv
- Contract: Columns: r_xi (float), h_xi (float), excess_free_energy (float). One row per computed (r/ξ, h/ξ) pair.
- Scoring: scored by hidden verifier

### Step 3: Determine Binodal Transition Line
- Role: scored
- Action: From the excess free energy curves (or by direct post‑processing of the simulation grand potentials), find for each sphere radius r the separation h where ΔΩ = 0 (the unbridged state has zero excess free energy). Use curve fitting (e.g., quadratic interpolation) to locate the zero crossing. Compute the dimensionless ratios r/λ and h/λ, where λ = σ/(2 Δμ φ_b) with σ ≈ 0.06 and φ_b = 1. Ensure at least 10 distinct points covering r/λ from ~0.1 to 100. Save the binodal line as transition_line.csv.
- Output file: `/app/outputs/transition_line.csv`
- Format: csv
- Contract: Columns: r_lambda (float), h_lambda (float). At least 10 data points.
- Scoring: scored by hidden verifier

### Step 4: Compute Force-Distance Curves
- Role: scored
- Action: Derive the force F between sphere and plane from the excess free energy curves: F = -∂(ΔΩ)/∂h. Use centered finite differences on the (h, ΔΩ) data for each r/ξ. Scale the force by σξ ≈ 0.00134 (product of interfacial tension and correlation length) to obtain the dimensionless force F/(σξ). For the same radii as in step 1, output the force as a function of h/ξ in force_curves.csv.
- Output file: `/app/outputs/force_curves.csv`
- Format: csv
- Contract: Columns: r_xi (float), h_xi (float), force_scaled (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/free_energy_curves.csv`
- `/app/outputs/transition_line.csv`
- `/app/outputs/force_curves.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### free_energy_curves.csv
- path: `/app/outputs/free_energy_curves.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Structural audit: the verifier checks the shape of the excess free energy vs separation curves for structural features (e.g., jumps, smoothness). No specific radial behaviour is prescribed.
- schema:
  - `type`: table
  - `required_columns`: `r_xi`, `h_xi`, `excess_free_energy`
  - `units`:
    - `r_xi`: dimensionless (radius in units of ξ)
    - `h_xi`: dimensionless (separation in units of ξ)
    - `excess_free_energy`: simulation units (ΔΩ)

### transition_line.csv
- path: `/app/outputs/transition_line.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Binodal transition line. The checker compares the submitted h_lambda values against hidden reference points extracted from the paper's mean‑field numerical data (Fig. 4). A tolerance of ±0.5 in h_lambda for r_lambda > 1 and ±0.2 for smaller values is acceptable.
- schema:
  - `type`: table
  - `required_columns`: `r_lambda`, `h_lambda`
  - `units`:
    - `r_lambda`: dimensionless (radius in units of λ)
    - `h_lambda`: dimensionless (separation in units of λ)

### force_curves.csv
- path: `/app/outputs/force_curves.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Structural audit: the verifier checks the force-distance curves for structural features (e.g., linearity, jumps to zero, smoothness). No specific radial behaviour is prescribed.
- schema:
  - `type`: table
  - `required_columns`: `r_xi`, `h_xi`, `force_scaled`
  - `units`:
    - `r_xi`: dimensionless (radius in units of ξ)
    - `h_xi`: dimensionless (separation in units of ξ)
    - `force_scaled`: dimensionless (F/(σξ))

Notes: All outputs must be computed from the numerical minimization of the grand potential functional. No external dataset is used; the simulation parameters are given in the steps.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "free_energy_curves.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "r_xi",
          "h_xi",
          "excess_free_energy"
        ],
        "units": {
          "r_xi": "dimensionless (radius in units of ξ)",
          "h_xi": "dimensionless (separation in units of ξ)",
          "excess_free_energy": "simulation units (ΔΩ)"
        }
      },
      "description": "Structural audit: the verifier checks the shape of the excess free energy vs separation curves for structural features (e.g., jumps, smoothness). No specific radial behaviour is prescribed."
    },
    {
      "file": "transition_line.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "r_lambda",
          "h_lambda"
        ],
        "units": {
          "r_lambda": "dimensionless (radius in units of λ)",
          "h_lambda": "dimensionless (separation in units of λ)"
        }
      },
      "description": "Binodal transition line. The checker compares the submitted h_lambda values against hidden reference points extracted from the paper's mean‑field numerical data (Fig. 4). A tolerance of ±0.5 in h_lambda for r_lambda > 1 and ±0.2 for smaller values is acceptable."
    },
    {
      "file": "force_curves.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "r_xi",
          "h_xi",
          "force_scaled"
        ],
        "units": {
          "r_xi": "dimensionless (radius in units of ξ)",
          "h_xi": "dimensionless (separation in units of ξ)",
          "force_scaled": "dimensionless (F/(σξ))"
        }
      },
      "description": "Structural audit: the verifier checks the force-distance curves for structural features (e.g., linearity, jumps to zero, smoothness). No specific radial behaviour is prescribed."
    }
  ],
  "notes": "All outputs must be computed from the numerical minimization of the grand potential functional. No external dataset is used; the simulation parameters are given in the steps."
}
```

## How you are scored
A hidden verifier independently scores each output file and combines them by weight into the final reward (float 0–1).

- **free_energy_curves.csv** is evaluated by a **structural audit**: the verifier inspects the shape of the ΔΩ vs h curves (e.g., presence or absence of a discontinuous jump) at specific radii.
- **transition_line.csv** is scored by **reference match**: the submitted h/λ values for given r/λ are compared against reference binodal points.
- **force_curves.csv** is also scored by a **structural audit**: the verifier checks that the force‑distance curves exhibit the expected shape and trends.

Reporting a single number is not sufficient; the verifier examines the full tabular data.  No tolerances or gold values are disclosed – you must implement the workflow as described and produce the three artifacts.

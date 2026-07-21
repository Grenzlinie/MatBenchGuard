# Field-driven magnetic and superconducting phase transition in a multi-orbital Anderson lattice model

## Problem background
Uranium-based compounds such as UGe2 exhibit coexisting ferromagnetism and spin-triplet superconductivity, a rare and poorly understood interplay. Theory suggests that the pairing is driven by Hund’s rule coupling and electronic correlations among nearly localized f electrons hybridized with itinerant conduction electrons. A minimal model is the four-orbital degenerate Anderson lattice model with intra- and inter-orbital Coulomb interactions and ferromagnetic Hund’s exchange. In this model, the ground state displays a sequence of ferromagnetic (FM1, FM2) and paramagnetic (PM) phases intertwined with three distinct spin-triplet superconducting states (A, A1, A2) that differ by their spin-polarization of Cooper pairs. Applying an external Zeeman magnetic field can favor different superconducting phases and is expected to induce a field-driven metasuperconducting transition between the A1 and A2 states. The goal is to compute the superconducting order parameters and magnetization as functions of hybridization and applied field within a self-consistent Gutzwiller approximation, and to determine whether the model reproduces such a transition.

## Approach
We solve the four-orbital Anderson lattice model using the statistically consistent Gutzwiller approximation (SGA) at zero temperature. The correlated wavefunction is constructed from an uncorrelated Slater determinant by a local Gutzwiller projector that renormalizes the on-site interactions. The resulting effective Hamiltonian retains the single-particle band structure, a renormalized f-level energy, and an effective inter-orbital pairing channel for f electrons. The hybrid pairing (c–f) is taken to be zero, as in the simplified treatment. For a given set of parameters (U, J, V, h, t', ε^f, total filling), the self-consistent loop initializes correlation factors and mean fields, constructs the effective Hamiltonian, solves for the magnetic moments and anomalous f-f amplitudes, and iterates until convergence. The outputs are the spin-triplet gap components Δ↑↑ and Δ↓↓, the total magnetization, and a phase label (FM2+A2, FM1+A1, PM+A, or none) derived from the magnetization and the vanishing of gap components. Two parameter sweeps are performed: (i) zero-field sweep over the hybridization V to map out the phase sequence as V increases; (ii) field sweep at fixed V across the expected FM1→FM2 boundary to capture the field-driven metamagnetic and metasuperconducting transitions. The solver must be implemented from scratch; no external Gutzwiller library is provided.

## Reproduction target
Compute the spin-triplet superconducting gap components Δ↑↑ and Δ↓↓ (in units of the hopping |t|) as functions of the hybridization V/|t| for the zero-field parameter set: U/|t|=4, J/|t|=1.6, t′/|t|=0.25, ε^f/|t|=-4, total filling n_tot=3.25, h=0. Perform the calculation at a series of hybridization values spanning at least 1.17 to 4.25, and for each V record the converged Δ↑↑, Δ↓↓, and the phase label. Additionally, for a second parameter set: U/|t|=3.5, J/|t|=1.1, V/|t|=1.26, with the same t′, ε^f, and filling, scan the Zeeman field h/|t| from 0 to 0.003 in steps fine enough to resolve any discontinuity. At each h record the total magnetization m_tot (in μ_B) and the gap components, and identify the field value h_x at which a discontinuous jump in magnetization and gaps occurs, indicating a simultaneous metamagnetic and metasuperconducting transition.

## Assets

- Python 3.x: python3
- NumPy: numpy
- SciPy: scipy
- Matplotlib: matplotlib

## Workflow steps

### Step 1: Implement SGA self-consistent solver
- Role: process
- Action: Implement the statistically consistent Gutzwiller approximation (SGA) self-consistent loop for the four-orbital Anderson lattice model in the simplified scheme (hybrid pairing set to zero). The solver initializes mean fields and correlation factors, constructs the effective Hamiltonian, solves self-consistency equations for magnetic moments and anomalous f-f amplitudes, and iterates to convergence. It must accept parameters including U, J, V, h, t', ε^f, n_tot and return the converged gap components Δ↑↑ and Δ↓↓, magnetization, and phase label.
- Evidence: `/app/outputs/solver.log`

### Step 2: Zero-field superconducting gaps vs hybridization
- Role: scored (load-bearing)
- Action: Using the SGA solver from the previous step, compute the zero-field superconducting gap components for the parameter set U/|t|=4, J/|t|=1.6, t′/|t|=0.25, ε^f/|t|=-4, n_tot=3.25, h=0, at each hybridization V/|t| value listed in the paper's Table II (approximately 1.166667 to 4.25). For each V, record the converged gap amplitudes Δ↑↑ and Δ↓↓ (in units of |t|) and identify the phase (FM2+A2, FM1+A1, PM+A, or none). Output a JSON array of objects with keys V_over_t (float), Delta_upup (float), Delta_downdown (float), phase (string).
- Output file: `/app/outputs/zero_field_gaps.json`
- Format: json
- Contract: Array of objects: each with V_over_t (number), Delta_upup (number, unit |t|), Delta_downdown (number, unit |t|), phase (string: 'FM2+A2', 'FM1+A1', 'PM+A', or 'none').
- Scoring: scored by hidden verifier

### Step 3: Magnetic and superconducting response in applied field
- Role: scored
- Action: For the parameter set U/|t|=3.5, J/|t|=1.1, V/|t|=1.26, t′/|t|=0.25, ε^f/|t|=-4, n_tot=3.25, use the SGA solver to scan applied Zeeman field h/|t| from 0 to 0.003 in steps fine enough to resolve the discontinuous transition. Run the solver at each h and record the total magnetization m_tot (in μ_B), gap components Δ↑↑ and Δ↓↓ (in units of |t|), and the phase label. Output an array of objects with keys h_over_t (float), m_tot (float), Delta_upup (float), Delta_downdown (float), phase (string). The agent must locate and capture the field value h_x/|t| at which a discontinuity in magnetization and gaps occurs (metamagnetic/metasuperconducting transition).
- Output file: `/app/outputs/finite_field_scan.json`
- Format: json
- Contract: Array of objects: each with h_over_t (number), m_tot (number, unit μ_B), Delta_upup (number, unit |t|), Delta_downdown (number, unit |t|), phase (string).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/zero_field_gaps.json`
- `/app/outputs/finite_field_scan.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### zero_field_gaps.json
- path: `/app/outputs/zero_field_gaps.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Zero-field superconducting gap components Δ↑↑ and Δ↓↓ (in units of |t|) and phase labels at a series of hybridization V/|t| values, computed from the SGA model for the given parameter set.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `V_over_t`, `Delta_upup`, `Delta_downdown`, `phase`
    - `properties`:
      - `V_over_t`:
        - `type`: number
        - `unit`: dimensionless (ratio V/|t|)
      - `Delta_upup`:
        - `type`: number
        - `unit`: |t|
      - `Delta_downdown`:
        - `type`: number
        - `unit`: |t|
      - `phase`:
        - `type`: string
        - `description`: one of: FM2+A2, FM1+A1, PM+A, none

### finite_field_scan.json
- path: `/app/outputs/finite_field_scan.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Total magnetization and superconducting gap components as functions of applied Zeeman field for a fixed hybridization, capturing the discontinuous metamagnetic/metasuperconducting transition.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `h_over_t`, `m_tot`, `Delta_upup`, `Delta_downdown`, `phase`
    - `properties`:
      - `h_over_t`:
        - `type`: number
        - `unit`: dimensionless (ratio h/|t|)
      - `m_tot`:
        - `type`: number
        - `unit`: μ_B
      - `Delta_upup`:
        - `type`: number
        - `unit`: |t|
      - `Delta_downdown`:
        - `type`: number
        - `unit`: |t|
      - `phase`:
        - `type`: string
        - `description`: phase label

Notes: All gap values are in units of |t|. Magnetization is in μ_B. The hidden checker compares gap components against the paper's reported Table II values with appropriate tolerance, verifies the phase sequence for zero-field, and locates the expected discontinuous jump in the finite-field scan. The agent must implement the SGA solver from scratch; the workflow uses the simplified model with hybrid pairing set to zero as described in the paper.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "zero_field_gaps.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "V_over_t",
            "Delta_upup",
            "Delta_downdown",
            "phase"
          ],
          "properties": {
            "V_over_t": {
              "type": "number",
              "unit": "dimensionless (ratio V/|t|)"
            },
            "Delta_upup": {
              "type": "number",
              "unit": "|t|"
            },
            "Delta_downdown": {
              "type": "number",
              "unit": "|t|"
            },
            "phase": {
              "type": "string",
              "description": "one of: FM2+A2, FM1+A1, PM+A, none"
            }
          }
        }
      },
      "description": "Zero-field superconducting gap components Δ↑↑ and Δ↓↓ (in units of |t|) and phase labels at a series of hybridization V/|t| values, computed from the SGA model for the given parameter set."
    },
    {
      "file": "finite_field_scan.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "h_over_t",
            "m_tot",
            "Delta_upup",
            "Delta_downdown",
            "phase"
          ],
          "properties": {
            "h_over_t": {
              "type": "number",
              "unit": "dimensionless (ratio h/|t|)"
            },
            "m_tot": {
              "type": "number",
              "unit": "μ_B"
            },
            "Delta_upup": {
              "type": "number",
              "unit": "|t|"
            },
            "Delta_downdown": {
              "type": "number",
              "unit": "|t|"
            },
            "phase": {
              "type": "string",
              "description": "phase label"
            }
          }
        }
      },
      "description": "Total magnetization and superconducting gap components as functions of applied Zeeman field for a fixed hybridization, capturing the discontinuous metamagnetic/metasuperconducting transition."
    }
  ],
  "notes": "All gap values are in units of |t|. Magnetization is in μ_B. The hidden checker compares gap components against the paper's reported Table II values with appropriate tolerance, verifies the phase sequence for zero-field, and locates the expected discontinuous jump in the finite-field scan. The agent must implement the SGA solver from scratch; the workflow uses the simplified model with hybrid pairing set to zero as described in the paper."
}
```

## How you are scored
The reproduction is scored by a hidden verifier that independently checks each output artifact against reference results computed from the same model. For the zero-field sweep, the verifier compares the reported gap components to reference values within an appropriate tolerance and checks that the sequence of phases (e.g., FM2+A2 → FM1+A1 → PM+A) is correctly reproduced as V increases. For the finite-field scan, the verifier confirms that a discontinuous jump in magnetization and gaps occurs at a specific field value and that the phases on either side correspond to A1 (only Δ↓↓ nonzero) and A2 (both gaps nonzero). Each stage contributes a fraction to the final score (0 to 1), with the zero-field sweep receiving the largest weight. Partial credit is awarded for capturing the correct phase ordering even if the absolute gap magnitudes deviate somewhat. To obtain a high score you must genuinely implement the self-consistent solver and run the parameter sweeps; simply reporting the paper's numbers without executing the solver will not pass the verifier's hidden reference comparison.

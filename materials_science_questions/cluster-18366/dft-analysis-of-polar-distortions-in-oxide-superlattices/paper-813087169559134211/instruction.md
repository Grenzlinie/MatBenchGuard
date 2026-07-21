# Phase diagram of ferroelectric domain structures vs thickness ratio from phase-field simulations

## Problem background
Ferroelectric flux-closure domain arrays in PbTiO₃/SrTiO₃ (PTO/STO) multilayers are promising for high-density memory because data stored in closed polarization loops may avoid cross-talk. For these nanoscale flux-closure quadrants to be addressable, they must appear as periodic arrays, and their morphology—vertical (V) or horizontal (H) flux closures—is found to depend on the thickness ratio of adjacent PTO layers. This task addresses the central computational question: how does the thickness ratio control which domain structure is stable? The objective is to compute, via phase-field simulations, the phase diagram of the dominant domain type (A, T, H, or V) as a function of the PTO thickness ratio, and to identify the critical ratio values where the dominant type changes, without presupposing the outcome.

## Approach
The core method is three-dimensional phase-field simulation of the polarization field in a PTO/STO multilayer system. The model contains a lower PTO layer of fixed thickness 28 nm, an upper PTO layer whose thickness varies from 0 to 28 nm, and three STO spacer layers of 4 nm each. The polarization evolution is governed by the time-dependent Ginzburg–Landau equation, with the total free energy comprising bulk, gradient, elastic, and electrostatic contributions. All material constants—Landau-Devonshire coefficients, elastic moduli, dielectric permittivities, and electrostrictive coefficients—are taken from the publicly available references (Li et al. Acta Mater. 2002 and Li et al. Appl. Phys. Lett. 2007).

For each thickness ratio r (r = t_upper / t_lower, ranging from 0 to 1), the polarization field is relaxed from initial guesses corresponding to the four candidate domain configurations observed in this system: a₁/a₂ domains (A), trapezoidal a‑domains (T), horizontal flux-closure quadrants (H), and vertical flux-closure quadrants (V). After relaxation, the total free energy density of each configuration is computed. The domain type that yields the lowest energy density at a given r is designated as the dominant one. By sweeping r across the interval, a phase diagram of dominant domain type versus r is constructed. The thickness ratios at which the dominant domain switches from T to H and from H to V are determined by interpolation, locating the crossing points where the energy density difference between the competing structures equals zero.

## Reproduction target
Produce two scored artifacts in `/app/outputs`:

1. `phase_diagram.csv` — a CSV file with one row per simulated thickness ratio r (the ratio of the upper to lower PTO layer thickness). Each row must contain the columns `r` (float) and `domain_type` (string, one of 'A', 'T', 'H', 'V'), indicating the dominant (lowest-energy) domain type at that ratio. An optional column `total_energy_density` may be included.
2. `transition_points.json` — a JSON object with the keys `"T_to_H"` and `"H_to_V"`, each a float representing the thickness ratio r at which the dominant domain type changes from T to H and from H to V, respectively, as determined from the energy density crossing. The values should be the result of interpolation on the simulated data.

## Assets

- Li et al. Acta Mater. 2002 – phase-field formalism and Landau-Devonshire coefficients for PTO and STO: https://doi.org/10.1016/S1359-6454(02)00254-6
- Li et al. Appl. Phys. Lett. 2007 – STO Landau coefficients: https://doi.org/10.1063/1.2804116

## Workflow steps

### Step 1: Phase-field simulations of domain structures and energy densities
- Role: process
- Action: Implement a 3D phase-field model for the PTO/STO multilayer system (lower PTO fixed at 28 nm, upper PTO thickness varied from 0 to 28 nm, STO spacer layers 4 nm) using the time-dependent Ginzburg–Landau equation with the public Landau coefficients from Li et al. Acta Mater. 2002 and Li et al. Appl. Phys. Lett. 2007. For each thickness ratio r (from 0 to 1 in at least 10 steps), relax the polarization field from initial guesses for the candidate domain structures (a1/a2 domains, trapezoidal a-domains, horizontal flux-closure H, vertical flux-closure V) and compute the total free energy density for the relaxed configuration. Identify the dominant (lowest-energy) domain type at each r. Save simulation evidence (e.g., a convergence log).
- Evidence: `/app/outputs/simulation_log.txt`

### Step 2: Phase diagram of domain type vs thickness ratio
- Role: scored (load-bearing)
- Action: From the simulation results, compile a CSV file listing for each simulated thickness ratio r the dominant domain type (A, T, H, or V) determined as the lowest-energy configuration.
- Output file: `/app/outputs/phase_diagram.csv`
- Format: csv
- Contract: Columns: r (float), domain_type (string), total_energy_density (float, optional).
- Scoring: scored by hidden verifier

### Step 3: Transition points between domain regimes
- Role: scored (load-bearing)
- Action: Using the total energy density differences between competing domain structures from the simulation data, determine the thickness ratios r at which the dominant domain type changes from T to H and from H to V (crossing points where the energy density difference equals zero). Report these two r values as a JSON object.
- Output file: `/app/outputs/transition_points.json`
- Format: json
- Contract: JSON object with required keys 'T_to_H' (float) and 'H_to_V' (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phase_diagram.csv`
- `/app/outputs/transition_points.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phase_diagram.csv
- path: `/app/outputs/phase_diagram.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Phase diagram mapping thickness ratio r to the dominant domain type (A, T, H, V) from the lowest-energy configuration.
- schema:
  - `type`: table
  - `required_columns`: `r`, `domain_type`

### transition_points.json
- path: `/app/outputs/transition_points.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Thickness ratios at the two principal phase boundaries: T→H and H→V.
- schema:
  - `type`: object
  - `required`:
    - `T_to_H`: float
    - `H_to_V`: float

Notes: The phase diagram is verified by checking the reported domain type at a set of hidden r values against the expected sequence from the paper. The transition points are compared to the paper's reported values with a small tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phase_diagram.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "r",
          "domain_type"
        ]
      },
      "description": "Phase diagram mapping thickness ratio r to the dominant domain type (A, T, H, V) from the lowest-energy configuration."
    },
    {
      "file": "transition_points.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "T_to_H": "float",
          "H_to_V": "float"
        }
      },
      "description": "Thickness ratios at the two principal phase boundaries: T→H and H→V."
    }
  ],
  "notes": "The phase diagram is verified by checking the reported domain type at a set of hidden r values against the expected sequence from the paper. The transition points are compared to the paper's reported values with a small tolerance."
}
```

## How you are scored
Your submission is scored by a hidden verifier that reads the output files. The phase diagram (`phase_diagram.csv`) is checked at a set of hidden r values; the verifier compares your reported `domain_type` to the expected ordering derived from the physics of the system, allowing a small tolerance for phase boundary shifts common in phase-field re-runs. The transition points (`transition_points.json`) are compared to reference values with a small allowed deviation, consistent with the expected re-run spread. Both artifacts are load‑bearing, and the final reward is a weighted combination of their correctness scores. The verifier does not require exact numerical match; it rewards results that are consistent with the correct energy‑minimization outcome of the described phase-field procedure.

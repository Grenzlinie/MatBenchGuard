# CVM Tetrahedron Phase Diagram Computation for Binary fcc/hcp Alloys

## Problem background
Binary alloys that undergo ordering can exhibit a variety of ordered phases based on the fcc or ideal hcp lattice, such as L1₂ (or DO₁₉) and L1₀ (or B19). Predicting the temperature–composition phase diagrams and the types of invariant reactions (eutectoid I, eutectoid II, peritectoid) that separate these phases is a central challenge. The cluster variation method (CVM) in the tetrahedron approximation provides a way to calculate approximate configurational entropy from multi-site cluster distributions, while configurational energy can include multi-atom interactions beyond simple pair terms. By solving for the equilibrium cluster distributions that minimize the free energy for given interaction parameters, one can map out phase stability and observe how the choice of interaction parameters influences the phase diagram topology. This task asks you to implement such a CVM model and compute phase diagrams for binary systems across a range of distinct interaction parameters, including a set that models the Cd‑Mg system, yielding the invariant reactions and characteristic temperatures.

## Approach
The core of the reproduction is building a numerical solver for the CVM tetrahedron model and its natural iteration method (NIM). The model uses a regular tetrahedron as the basic cluster motif. The configurational energy of the alloy is expressed as a linear combination of tetrahedral cluster fractions, with coefficients that depend on an effective pair interaction parameter W (taken negative, e.g. W = –1, so that ordering is favoured) and two multi-atom parameters α and β that control the relative stability of different ordered structures. The configurational entropy is obtained from the Kikuchi formula, which gives the entropy of the tetrahedron distribution and corrects for overcounting of pairs and points. The grand potential is then minimized with respect to the cluster variables, leading to a set of nonlinear equilibrium equations. These equations are solved iteratively by NIM: starting from an initial guess for point and pair probabilities, tetrahedral cluster variables are updated until convergence. By conducting scans in temperature and chemical potential for a fixed (α,β) pair, one identifies the stable phases (disordered fcc, A₃B, AB, AB₃) and maps out phase boundaries. The topology of the resulting phase diagram determines the invariant reaction on each side of equiatomic composition (X_B = 0.5). For the Cd‑Mg system, the interaction parameters are taken as α = –0.07, β = –0.01. The energy scale is calibrated so that the calculated order–disorder transition temperature matches the known experimental value of approximately 253 °C for Cd‑Mg, allowing the peritectoid temperatures T₁ and T₂ and the transition temperature T_t to be reported in degrees Celsius. The overall pipeline is: first, implement the CVM/NIM solver; second, compute phase boundaries for the parameter sets listed in the workflow steps, saving them as a CSV file; third, from the CSV, classify the invariant reactions and extract the Cd‑Mg temperatures, storing the results as JSON.

## Reproduction target
Produce the following two artifacts:

1. **phase_diagrams.csv** — raw phase boundary points for the eight (α,β) pairs: (0,0), (–1/6,–1/6), (1/6,1/6), (1/2,–1/6), (1/6,–1/6), (1/3,0), (1/6,–1/18), and (–0.07,–0.01). Each row must contain: alpha (float), beta (float), T_star (float, reduced temperature kT/|W|), phase (string: disordered, L1₂, L1₀, A3B, AB, or AB3; L1₂ corresponds to A₃B and L1₀ to AB), and X_B (float, atom fraction of B). The CSV should capture the boundaries between stable phases across the temperature range where ordering transitions occur.

2. **invariant_reactions.json** — an object with two keys: (i) `parameter_sweep`, an array of objects for the first seven (α,β) pairs, each carrying: `id` (string label: O for (0,0), P for (–1/6,–1/6), Q for (1/6,1/6), R for (1/2,–1/6), S for (1/6,–1/6), T for (1/3,0), C for (1/6,–1/18)), `alpha`, `beta`, `invariant_XB_lt_0.5` (string: 'Eutectoid I', 'Eutectoid II', or 'Peritectoid'), and `invariant_XB_gt_0.5` (same allowed strings); (ii) `CdMg`, an object with `alpha`, `beta`, `T1_C` (float), `T2_C` (float), `Tt_C` (float) — the peritectoid and order‑disorder transition temperatures for Cd‑Mg in °C.

Calibrate the energy scale for Cd‑Mg so that the computed order‑disorder transition temperature matches the known experimental value of ~253 °C, and report T₁, T₂, and T_t consistent with that calibration. Do not attempt to exactly match any previously published diagram; compute phase boundaries from the model as described. The verifier will independently evaluate your invariant classifications and Cd‑Mg temperatures.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Implement CVM tetrahedron solver with NIM
- Role: process
- Action: Implement a Python program that realises the CVM tetrahedron approximation for binary fcc/ideal hcp alloys. Define tetrahedral cluster variables (Z), pair (y) and point (x) variables; compute configurational energy using the multi-atom interaction parameters α and β and an effective pair interaction W; compute configurational entropy via the Kikuchi tetrahedron-entropy formula with pair and point overlap corrections; form the grand potential and derive equilibrium relations. Implement the natural iteration method (NIM) to solve the nonlinear equations, returning equilibrium cluster distributions and the grand potential for given α, β, temperature, and chemical potentials.
- Evidence: `/app/outputs/cvm_solver_implementation.log`

### Step 2: Compute phase diagrams for all parameter sets
- Role: scored (load-bearing)
- Action: Using the solver, scan temperature and chemical potential to locate phase boundaries (disordered, A₃B, AB, AB₃) for each of the following (α,β) pairs: (0,0), (-1/6,-1/6), (1/6,1/6), (1/2,-1/6), (1/6,-1/6), (1/3,0), (1/6,-1/18), and the Cd-Mg parameters (-0.07,-0.01). Use a consistent effective pair interaction W (e.g., W = -1) and report reduced temperature kT/|W|. For each computed stable phase point record alpha, beta, reduced temperature T_star, phase label, and composition X_B (atom fraction of B). Save all points as CSV.
- Output file: `/app/outputs/phase_diagrams.csv`
- Format: csv
- Contract: Columns: alpha (float), beta (float), T_star (float, reduced temperature), phase (string, one of: disordered, L12, L10, A3B, AB, AB3), X_B (float, atom fraction of B). One row per computed equilibrium point. Multiple rows per (alpha,beta,T_star) may delineate boundaries.
- Scoring: scored by hidden verifier

### Step 3: Extract invariant reactions and Cd-Mg peritectoid temperatures
- Role: scored
- Action: Analyze the phase boundaries in phase_diagrams.csv. For each non-Cd-Mg (α,β) pair, identify the type of invariant reaction (Eutectoid I, Eutectoid II, or Peritectoid) on the X_B < 0.5 side and on the X_B > 0.5 side. For the Cd-Mg parameter set (α=-0.07, β=-0.01), extract the peritectoid temperatures T1, T2 and the order-disorder transition temperature Tt in °C, using the experimental transition temperature ≈253°C to calibrate the energy scale. Store the results as JSON.
- Output file: `/app/outputs/invariant_reactions.json`
- Format: json
- Contract: A JSON object with keys: "parameter_sweep" (array of objects, each with fields: id (string), alpha (float), beta (float), invariant_XB_lt_0.5 (string), invariant_XB_gt_0.5 (string)), and "CdMg" (object with fields: alpha (float), beta (float), T1_C (float), T2_C (float), Tt_C (float)). Allowed invariant strings: "Eutectoid I", "Eutectoid II", "Peritectoid".
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phase_diagrams.csv`
- `/app/outputs/invariant_reactions.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phase_diagrams.csv
- path: `/app/outputs/phase_diagrams.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Raw phase boundary points for all (α,β) parameter sets. The checker recomputes invariant reaction types and Cd-Mg temperatures from this data and compares them to hidden gold values.
- schema:
  - `type`: table
  - `required_columns`: `alpha`, `beta`, `T_star`, `phase`, `X_B`
  - `units`:
    - `T_star`: reduced temperature kT/|W|
    - `X_B`: atom fraction

### invariant_reactions.json
- path: `/app/outputs/invariant_reactions.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Agent-reported invariant reaction types and Cd-Mg peritectoid/transition temperatures. The checker compares these directly to hidden paper gold values with tolerant exact match on strings and ±10°C on temperatures.
- schema:
  - `type`: object
  - `required`: `parameter_sweep`, `CdMg`
  - `items`:
    - `parameter_sweep`: array of objects with alpha, beta, invariant_XB_lt_0.5, invariant_XB_gt_0.5
    - `CdMg`: object with T1_C, T2_C, Tt_C

Notes: The workflow re-implements the CVM tetrahedron model from published equations; no external data is needed. The agent must produce the solver and run it, not reuse a pre-existing codebase. Phase boundary CSV is the raw artifact from which invariant reactions and temperatures are derived; the checker recomputes the former and cross-checks the latter against the paper-reported table and Cd-Mg values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phase_diagrams.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "alpha",
          "beta",
          "T_star",
          "phase",
          "X_B"
        ],
        "units": {
          "T_star": "reduced temperature kT/|W|",
          "X_B": "atom fraction"
        }
      },
      "description": "Raw phase boundary points for all (α,β) parameter sets. The checker recomputes invariant reaction types and Cd-Mg temperatures from this data and compares them to hidden gold values."
    },
    {
      "file": "invariant_reactions.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "parameter_sweep",
          "CdMg"
        ],
        "items": {
          "parameter_sweep": "array of objects with alpha, beta, invariant_XB_lt_0.5, invariant_XB_gt_0.5",
          "CdMg": "object with T1_C, T2_C, Tt_C"
        }
      },
      "description": "Agent-reported invariant reaction types and Cd-Mg peritectoid/transition temperatures. The checker compares these directly to hidden paper gold values with tolerant exact match on strings and ±10°C on temperatures."
    }
  ],
  "notes": "The workflow re-implements the CVM tetrahedron model from published equations; no external data is needed. The agent must produce the solver and run it, not reuse a pre-existing codebase. Phase boundary CSV is the raw artifact from which invariant reactions and temperatures are derived; the checker recomputes the former and cross-checks the latter against the paper-reported table and Cd-Mg values."
}
```

## How you are scored
A hidden verifier independently assesses each scored artifact. For `phase_diagrams.csv`, the verifier recomputes invariant reaction types from your raw boundary points and compares them to expected reference classifications. For `invariant_reactions.json`, the verifier directly compares the invariant strings you report for each (α,β) pair against reference strings, and compares the Cd‑Mg temperatures (T1_C, T2_C, Tt_C) against reference values within an allowed tolerance. The final reward is a weighted combination of these checks: correctness of the invariant reaction types and accuracy of the Cd‑Mg temperatures carry the primary weight. Exact numeric agreement of every boundary point is not required; the verifier checks that the phase diagram topology yields the correct invariant reactions and that the extracted temperatures are consistent with the model calibration. All artifacts must be produced by your own implementation; using pre‑existing lookup tables or copying numbers from the internet will be detected and will not score.

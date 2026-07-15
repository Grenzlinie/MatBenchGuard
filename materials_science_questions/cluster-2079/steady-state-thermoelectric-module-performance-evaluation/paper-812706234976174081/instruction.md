# Heat-recovery solar cell efficiency simulation with finite conductivity filtering layers

## Problem background
A heat‑recovery (HERC) solar cell employs a semiconductor absorber that is hotter than the electrodes. Energy‑filtering layers between the absorber and electrodes create potential barriers that control the extraction energy of carriers, producing a thermoelectric voltage that can raise the power conversion efficiency above the Shockley‑Queisser limit. The essential condition for this gain is a positive temperature coefficient of the efficiency, which imposes a constraint on the ratio of thermal to electrical conductivity (κ/σ) of the filtering layers. This task investigates that constraint by simulating a Si absorber under one‑sun illumination and computing the efficiency as a function of absorber temperature and κ/σ, together with the derived analytic bound and a check of candidate material properties.

## Approach
We model the HERC solar cell under the local equilibrium approximation, where carriers in the absorber are assumed to be thermalised at the absorber lattice temperature. The device is described by a set of coupled equations for the charge current (balance between generation, radiative recombination and extraction), the extraction current that includes an ohmic voltage drop across the filtering layers, and the heat balance that links the temperature difference between the absorber and the electrodes to the thermal conductivity of the layers. The filtering layers are characterised by an effective length that scales both the ohmic loss and the thermal conduction. For each absorber temperature we fix an optimal barrier height and extraction time (provided in the workflow steps). The model is implemented to solve for the maximum power conversion efficiency while enforcing a heat‑supply condition (presence of an IR absorber is assumed) that guarantees a positive heat flow into the absorber, so the device can maintain the required temperature difference. The workflow then computes a grid of efficiencies for a set of absorber temperatures and κ/σ values, derives a theoretical upper bound on κ/σ by analysing the open‑circuit voltage temperature coefficient, and evaluates two reported candidate materials (Bi₂Te₃ and CsSnI₃) against that bound.

## Reproduction target
For a 100‑μm‑thick Si absorber illuminated by the AM0 solar spectrum (approximated as 6000‑K blackbody radiation at 1‑sun concentration), you will run the implemented device model to obtain the maximum power conversion efficiency η_max for every combination of absorber temperature T_ph ∈ {350, 400, 450} K and filtering‑layer conductivity ratio κ/σ ∈ {0, 1×10⁻⁴, 1×10⁻³, 10^{-2.5}} V²/K. The results must be written to a CSV file (efficiency_vs_Tph.csv). Using the optimal barrier height E_b = 0.55 eV (for T_ph = 450 K) and the elementary charge, compute the analytic bound κ/σ ≤ (E_b/q) × 3.0×10⁻³ V²/K and store both the literal inequality and the numerical bound in a text file (analytic_bound.txt). Finally, using reported electrical and thermal conductivities for Bi₂Te₃ (σ ≈ 1×10⁵ S/m, κ ≈ 1.4 W/(m·K)) and CsSnI₃ (σ ≈ 3×10⁴ S/m, κ ≈ 0.6 W/(m·K)), compute κ/σ for each material and indicate whether it satisfies the bound, with a brief comment about the band‑gap suitability, saving the output to candidate_check.txt.

## Assets

- NumPy: numpy
- SciPy: scipy
- Matplotlib: matplotlib
- Standard physical constants

## Workflow steps

### Step 1: Implement HERC device model under local equilibrium approximation
- Role: process
- Action: Implement the heat-recovery solar cell model using the local equilibrium approximation. Define Si absorber parameters (band gap 1.12 eV, effective masses, thickness 100 μm), the solar spectrum (AM0 approximated by 6000 K blackbody radiation at 1 sun concentration), and the coupled equations for charge balance (balancing generation, radiative recombination, and extraction), the extraction current (including an ohmic voltage drop across the filtering layers), and the heat balance (linking the temperature difference between absorber and electrodes to the thermal conductivity of the layers). Incorporate thermal contact resistance via effective length l_eff scaling. Use the optimal barrier heights and extraction times provided for each absorber temperature (350 K: E_b=0.39 eV, τ_out=1e-7 s; 400 K: E_b=0.47 eV, τ_out=3e-7 s; 450 K: E_b=0.55 eV, τ_out=3e-6 s). The code must find the maximum power point while enforcing the heat-supply condition (P_Qin + P_T > 0) for stable operation.
- Evidence: `/app/outputs/model_setup.log`

### Step 2: Compute efficiency vs absorber temperature and κ/σ
- Role: scored (load-bearing)
- Action: For each combination of T_ph in {350, 400, 450} K and κ/σ in {0, 1e-4, 1e-3, 1e-2.5} V^2/K, run the implemented device model to obtain the maximum power conversion efficiency η_max (in %). Enforce the heat-supply condition P_Qin+P_T>0. Write the results to a CSV file with columns: T_ph (K), kappa_sigma (V^2/K), eta_max (%).
- Output file: `/app/outputs/efficiency_vs_Tph.csv`
- Format: csv
- Contract: Columns: T_ph (K), kappa_sigma (V^2/K), eta_max (%). Each row corresponds to one (T_ph, kappa_sigma) combination.
- Scoring: scored by hidden verifier

### Step 3: Derive analytic bound on κ/σ
- Role: scored
- Action: Using the optimal barrier height E_b = 0.55 eV (for T_ph = 450 K) and the elementary charge q, compute the upper bound κ/σ ≤ (E_b/q) × 3.0×10⁻³ V²/K. Write two lines: first line the literal inequality 'kappa/sigma <= (Eb/q) * 3.0e-3 V^2/K', second line the numerical value of the bound in V^2/K.
- Output file: `/app/outputs/analytic_bound.txt`
- Format: txt
- Contract: Line 1: 'kappa/sigma <= (Eb/q) * 3.0e-3 V^2/K'. Line 2: numerical bound in V^2/K (e.g., 1.65e-3).
- Scoring: scored by hidden verifier

### Step 4: Evaluate candidate materials against bound
- Role: scored
- Action: Using reported material properties: for Bi₂Te₃, σ ≈ 1×10⁵ S/m and κ ≈ 1.4 W/(m·K); for CsSnI₃, σ ≈ 3×10⁴ S/m and κ ≈ 0.6 W/(m·K). Compute κ/σ for each and determine whether the material satisfies the analytic bound derived in the previous step. Write two lines, one per material, in the format '<Material>: kappa/sigma = <value> V^2/K, <comment>'.
- Output file: `/app/outputs/candidate_check.txt`
- Format: txt
- Contract: Line 1: 'Bi2Te3: kappa/sigma = X.XXe-X V^2/K, satisfies bound but band gap too small.' Line 2: 'CsSnI3: kappa/sigma = Y.YYe-Y V^2/K, satisfies bound with usable band gap.'
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/efficiency_vs_Tph.csv`
- `/app/outputs/analytic_bound.txt`
- `/app/outputs/candidate_check.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### efficiency_vs_Tph.csv
- path: `/app/outputs/efficiency_vs_Tph.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Maximum power conversion efficiency as a function of absorber temperature and filtering‑layer conductivity ratio.
- schema:
  - `type`: table
  - `required_columns`: `T_ph`, `kappa_sigma`, `eta_max`
  - `units`:
    - `T_ph`: K
    - `kappa_sigma`: V^2/K
    - `eta_max`: %

### analytic_bound.txt
- path: `/app/outputs/analytic_bound.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Derived analytic criterion for κ/σ upper bound.
- schema:
  - `type`: text
  - `description`: Two lines: literal inequality string and numerical bound value.

### candidate_check.txt
- path: `/app/outputs/candidate_check.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Verification that Bi₂Te₃ and CsSnI₃ satisfy the bound.
- schema:
  - `type`: text
  - `description`: Two lines with material name, computed κ/σ, and comment.

Notes: The efficiency CSV is the primary artifact; it is scored by threshold_or_better (relative tolerance against hidden gold) and additionally subjected to structural monotonicity checks. The analytic bound and candidate check files are exact_match deterministic calculations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "efficiency_vs_Tph.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "T_ph",
          "kappa_sigma",
          "eta_max"
        ],
        "units": {
          "T_ph": "K",
          "kappa_sigma": "V^2/K",
          "eta_max": "%"
        }
      },
      "description": "Maximum power conversion efficiency as a function of absorber temperature and filtering‑layer conductivity ratio."
    },
    {
      "file": "analytic_bound.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "Two lines: literal inequality string and numerical bound value."
      },
      "description": "Derived analytic criterion for κ/σ upper bound."
    },
    {
      "file": "candidate_check.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "Two lines with material name, computed κ/σ, and comment."
      },
      "description": "Verification that Bi₂Te₃ and CsSnI₃ satisfy the bound."
    }
  ],
  "notes": "The efficiency CSV is the primary artifact; it is scored by threshold_or_better (relative tolerance against hidden gold) and additionally subjected to structural monotonicity checks. The analytic bound and candidate check files are exact_match deterministic calculations."
}
```

## How you are scored
A hidden verifier scores each of the three scored artifacts independently and combines the scores into a final reward. The efficiency CSV is scored by comparing your reported efficiency values to a hidden reference set, using a threshold‑or‑better policy that does not penalise results that exceed the reference; additional structural checks enforce correct monotonicity and slope‑sign trends across the (T_ph, κ/σ) grid. The analytic bound and the candidate material check files are evaluated by exact match to expected numeric values and text format. No single number or text string you report will be accepted without proper derivation; the verifier expects the artifacts to be the output of the described computational workflow.

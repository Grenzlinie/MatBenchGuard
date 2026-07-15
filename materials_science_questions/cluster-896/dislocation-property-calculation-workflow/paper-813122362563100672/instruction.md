# Dislocation Pileup Driven Quasi-Cleavage Reproduction

## Problem background
Quasi-cleavage fracture is an intermediate failure mode between brittle cleavage and ductile blunting. In materials where dislocations can nucleate but have limited mobility, arrays of dislocations pile up against a dislocation-free zone (DFZ) ahead of a crack tip loaded in mode I. The pileup strongly modifies the crack‑tip stress field, potentially nucleating a nanocrack within the DFZ that then links to the main crack. The present task is to reproduce the central mechanics model of this process: compute equilibrium dislocation configurations, find the equilibrium number of emitted dislocations under various lattice friction levels and applied loadings, determine the resulting tensile stress distribution ahead of the blunted crack tip, and simulate quasi‑static crack growth to obtain a fracture resistance curve.

## Approach
The model considers a plane‑strain semi‑infinite crack with a pair of symmetric slip planes at 45°. Edge dislocations on these planes interact via their stress fields (including image forces) and are subject to a lattice friction stress. The equilibrium positions are found by balancing driving forces against the friction stress. For each candidate number of dislocations and each (applied stress intensity factor, friction) pair, the total energy of the system is evaluated (elastic self‑ and interaction energies, ledge creation energy, and frictional work). The number that minimizes total energy is taken as the equilibrium number. Using these equilibrium configurations, the tensile (hoop) stress σ22 along the crack extension line is computed by superposing the applied K‑field, the dislocation self‑stress in an infinite medium, and a notch negation stress approximated via an effective K‑field. Finally, for a chosen set of material parameters, quasi‑static crack growth is simulated: a nanocrack initiates when a Griffith criterion is met, the crack advances by a characteristic distance that defines a constant crack tip opening angle (CTOA), and shielding contributions from dislocations left in the wake are summed to obtain the applied stress intensity factor needed to drive further growth, yielding a resistance curve (applied K vs. cumulative crack advance).

## Reproduction target
Produce three quantitative CSV files by implementing the method described above:
1. `equilibrium_n.csv` – equilibrium number of dislocations on one symmetric arm as a function of the normalized applied stress intensity factor and lattice friction. Covers friction levels σf/μ = 0.001, 0.002, 0.004, with applied loading Kapp/(μ√b) spanning a range from roughly 0.6 to 1.3.
2. `stress_profiles.csv` – hoop stress σ22/μ along the crack extension line (distance measured in units of b) for the equilibrium configuration at σf/μ = 0.002, evaluated at three applied loadings: Kapp/(μ√b) = 0.98, 1.13, 1.26.
3. `resistance_curve.csv` – fracture resistance curve for material parameters σf/μ = 0.006, σcr/μ = 0.06, β = 0.055, ν = 0.3. The file must contain the cumulative crack advance (in units of b) and the corresponding applied stress intensity factor Kapp/(μ√b), covering at least 10 growth steps or continuing until the curve plateaus, and the curve must be monotonically increasing.

## Assets

- Python scientific computing stack: numpy scipy

## Workflow steps

### Step 1: Solve force-balance for dislocation positions
- Role: process
- Action: For each candidate dislocation number n and each combination of applied stress intensity factor K^app and lattice friction stress σ_f, solve the n nonlinear equilibrium equations for the edge dislocation distances h_i along the symmetric slip planes. Implement a numerical solver (e.g., dynamic relaxation or Newton) using the force expressions from dislocation-crack interaction theory.
- Evidence: none

### Step 2: Determine equilibrium number of dislocations by energy minimization
- Role: scored
- Action: Using the dislocation positions from step_0, evaluate the total energy W_total as sum of self-energy, K-d interaction, d-d interaction, ledge energy, and lattice friction work for each candidate n. For each (K^app, σ_f) pair, find the n that minimizes W_total. Sweep over normalized friction stresses σ_f/μ = 0.001, 0.002, 0.004 and applied loadings K^app/μ√b covering a range from approximately 0.6 to 1.3. Record the equilibrium n for each condition.
- Output file: `/app/outputs/equilibrium_n.csv`
- Format: csv
- Contract: Columns: sigma_f_normalized (float), Kapp_normalized (float), n (integer). Each row gives the equilibrium number of emitted dislocations on one symmetric arm for a specific (σ_f, K^app) pair.
- Scoring: scored by hidden verifier

### Step 3: Compute hoop stress profiles along crack extension
- Role: scored (load-bearing)
- Action: For the equilibrium configuration at σ_f/μ=0.002 and three applied loadings Kapp/μ√b = 0.98, 1.13, 1.26, compute the tensile stress σ_22/μ along the crack extension line using superposition of applied K-field, dislocation self-stress, and notch negation stress (effective K-field approximation). Use known elasticity formulas. Evaluate stress at dense distances x1 from the notch tip (normalized by b). Write the three profiles.
- Output file: `/app/outputs/stress_profiles.csv`
- Format: csv
- Contract: Columns: x1_b (distance from notch tip in units of b), sigma_case1 (stress for Kapp=0.98), sigma_case2 (for 1.13), sigma_case3 (for 1.26). All sigma values normalized by μ.
- Scoring: scored by hidden verifier

### Step 4: Simulate quasi-static crack growth and fracture resistance curve
- Role: scored (load-bearing)
- Action: Using material parameters σ_f/μ=0.006, σ_cr/μ=0.06, β=0.055, ν=0.3, determine initiation stress intensity factor from Griffith criterion for nanocrack formation. Simulate step-by-step crack growth under a constant crack tip opening angle (CTOA). At each growth step, add a new slip trace of n dislocations behind the tip and compute the required applied K^app by summing shielding contributions from all wake dislocations. Record cumulative crack advance (in units of b) and corresponding Kapp/μ√b. Continue for at least 10 steps or until plateau.
- Output file: `/app/outputs/resistance_curve.csv`
- Format: csv
- Contract: Columns: crack_advance_b (cumulative crack advance in units of b), Kapp_normalized (applied stress intensity factor normalized by μ√b). The curve must be monotonically increasing.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/equilibrium_n.csv`
- `/app/outputs/stress_profiles.csv`
- `/app/outputs/resistance_curve.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### equilibrium_n.csv
- path: `/app/outputs/equilibrium_n.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Equilibrium number of dislocations on one symmetric arm for given normalized friction stress and applied stress intensity factor.
- schema:
  - `type`: table
  - `required_columns`: `sigma_f_normalized`, `Kapp_normalized`, `n`
  - `units`:
    - `sigma_f_normalized`: dimensionless (normalized by shear modulus)
    - `Kapp_normalized`: dimensionless (normalized by μ√b)
    - `n`: integer

### stress_profiles.csv
- path: `/app/outputs/stress_profiles.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Hoop stress profiles ahead of the notch tip for three applied loadings at fixed lattice friction.
- schema:
  - `type`: table
  - `required_columns`: `x1_b`, `sigma_case1`, `sigma_case2`, `sigma_case3`
  - `units`:
    - `x1_b`: distance in units of Burgers vector b
    - `sigma_case1`: normalized stress σ_22/μ (dimensionless)
    - `sigma_case2`: normalized stress σ_22/μ (dimensionless)
    - `sigma_case3`: normalized stress σ_22/μ (dimensionless)

### resistance_curve.csv
- path: `/app/outputs/resistance_curve.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Fracture resistance curve showing applied stress intensity factor as a function of cumulative crack advance for a quasi-cleavage process.
- schema:
  - `type`: table
  - `required_columns`: `crack_advance_b`, `Kapp_normalized`
  - `units`:
    - `crack_advance_b`: crack advance in units of b
    - `Kapp_normalized`: dimensionless (normalized by μ√b)

Notes: The checker will compare the reported equilibrium n values, stress peak characteristics, and final plateau Kapp to paper-reported references with appropriate tolerances. The stress calculation uses an effective K-field approximation as permitted by the task scope.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "equilibrium_n.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "sigma_f_normalized",
          "Kapp_normalized",
          "n"
        ],
        "units": {
          "sigma_f_normalized": "dimensionless (normalized by shear modulus)",
          "Kapp_normalized": "dimensionless (normalized by μ√b)",
          "n": "integer"
        }
      },
      "description": "Equilibrium number of dislocations on one symmetric arm for given normalized friction stress and applied stress intensity factor."
    },
    {
      "file": "stress_profiles.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "x1_b",
          "sigma_case1",
          "sigma_case2",
          "sigma_case3"
        ],
        "units": {
          "x1_b": "distance in units of Burgers vector b",
          "sigma_case1": "normalized stress σ_22/μ (dimensionless)",
          "sigma_case2": "normalized stress σ_22/μ (dimensionless)",
          "sigma_case3": "normalized stress σ_22/μ (dimensionless)"
        }
      },
      "description": "Hoop stress profiles ahead of the notch tip for three applied loadings at fixed lattice friction."
    },
    {
      "file": "resistance_curve.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "crack_advance_b",
          "Kapp_normalized"
        ],
        "units": {
          "crack_advance_b": "crack advance in units of b",
          "Kapp_normalized": "dimensionless (normalized by μ√b)"
        }
      },
      "description": "Fracture resistance curve showing applied stress intensity factor as a function of cumulative crack advance for a quasi-cleavage process."
    }
  ],
  "notes": "The checker will compare the reported equilibrium n values, stress peak characteristics, and final plateau Kapp to paper-reported references with appropriate tolerances. The stress calculation uses an effective K-field approximation as permitted by the task scope."
}
```

## How you are scored
A hidden verifier independently checks each of the three scored artifacts. For `equilibrium_n.csv` it compares reported n values against reference values (with tolerance) for every (σf, Kapp) pair. For `stress_profiles.csv` it examines the stress peak amplitude and its location relative to reference data. For `resistance_curve.csv` it compares the plateau (asymptotic) Kapp value to a reference and verifies the curve is monotonically increasing. The final reward is a weighted combination of the scores from the three stages, with the equilibrium n contributing 40%, the stress profiles 30%, and the resistance curve 30%. Reporting the exact numbers from the paper is not enough — your implementation must compute them from the described model.

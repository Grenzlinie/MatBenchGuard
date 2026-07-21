# Diffusive Model of Coupled Eutectic Melting and Phase Lead Prediction

## Problem background
Directional melting of lamellar eutectic structures can produce two distinct regimes: coupled melting, where the α- and β-phases dissolve with a macroscopically planar front and small differences between their lamellar tip positions, and noncoupled melting, where one phase extends far ahead of the other. Understanding the transition between these regimes and predicting the phase lead (the distance between the α and β lamellar tips) is important for processes such as soldering, brazing, and welding. A diffusive model has been proposed that describes the solute concentration field ahead of the interface and computes the resulting interface shape and phase lead. This task reconstructs that model for the CBr4–C2Cl6 eutectic alloy and tests its ability to reproduce experimental observations.

## Approach
The core of the model is a steady-state solution to the diffusion equation in the liquid, assuming a planar interface that moves at constant (negative) velocity.  The solute concentration field C(x,z) is expanded as a Fourier series along the lamellar direction x, with boundary conditions that enforce the conservation of solute released during melting of each phase.  The Fourier coefficients are expressed in terms of the lamellar half-widths, the velocity, and material constants.  Using this concentration profile, the average interface temperatures of the α and β phases are calculated, accounting for both solutal superheat (from the deviation of the local composition from the eutectic) and curvature undercooling (Gibbs–Thomson effect).  Because the experimentally observed interfaces are nearly isothermal, the effective undercooling is taken as the lower of the two average temperatures.  With this reference temperature, the local interface curvature is determined at each point along the interface, and the shape z(x) is obtained by double integration.  The phase lead is then extracted as the signed difference between the maximum z-positions of the two lamellar tips (positive if β leads).  The model relies on well-defined material constants (liquidus slopes, capillary constants, contact angles, diffusion coefficient, eutectic composition) and experimental inputs (velocity, lamellar spacing, volume fraction, composition) that are provided inline.

## Reproduction target
Implement the diffusive model described above and evaluate it for the eight experimental conditions supplied below.  For each condition, produce a predicted phase lead in micrometers.  Write the results to predicted_phase_leads.csv with columns experiment_id and predicted_phase_lead_um, one row per experiment (IDs 1–8).

## Assets

- CBr4-C2Cl6 material constants
- Experimental conditions (Table I equivalent)

## Workflow steps

### Step 1: Compile material constants and experimental parameters
- Role: process
- Action: Compile the CBr4–C2Cl6 material constants (liquidus slopes m_alpha, m_beta, capillary constants Gamma_alpha, Gamma_beta, contact angles theta_alpha, theta_beta, diffusion coefficient D, eutectic composition C_E, and compositional offsets C0_alpha, C0_beta) and the experimental conditions (velocity V, lamellar spacing lamda, volume fraction beta_vol, composition) for all eight experiments from the data provided in the task description. Compute the lamellar half-widths S_alpha and S_beta for each experiment.
- Evidence: none

### Step 2: Solve steady-state diffusion equation
- Role: process
- Action: Solve the steady-state diffusion equation in the liquid ahead of a planar eutectic interface during melting. Use a Fourier series solution with the boundary conditions appropriate to the lamellar geometry and negative melt velocity. Obtain the solute concentration profile C(x) along the interface for each experimental condition.
- Evidence: none

### Step 3: Calculate average interface temperatures
- Role: process
- Action: Compute the average interface temperatures for the alpha and beta phases using the expressions adapted from Jackson–Hunt for melting. Evaluate the solutal superheat and curvature undercooling contributions to obtain Delta_T_alpha and Delta_T_beta as functions of velocity, spacing, and volume fraction.
- Evidence: none

### Step 4: Select effective melting temperature
- Role: process
- Action: Determine the effective average undercooling that yields an isothermal interface by selecting the lower of the two average interface temperatures. This effective undercooling will serve as the reference temperature for computing the interface shape.
- Evidence: none

### Step 5: Compute predicted phase leads
- Role: scored (load-bearing)
- Action: For each of the eight experimental conditions, use the solute concentration profile C(x) and the effective undercooling to determine the local interface curvature via the Gibbs–Thomson balance, then integrate numerically to obtain the interface shape z(x) for both phases. Locate the lamellar tip positions (maximum z within each phase) and compute the phase lead as the signed distance between the beta and alpha tips (positive if beta leads). Write the results to predicted_phase_leads.csv.
- Output file: `/app/outputs/predicted_phase_leads.csv`
- Format: csv
- Contract: Columns: experiment_id (int), predicted_phase_lead_um (float). 8 rows, one per experiment (IDs 1–8).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/predicted_phase_leads.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### predicted_phase_leads.csv
- path: `/app/outputs/predicted_phase_leads.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Predicted phase lead (distance between alpha and beta lamellar tips) in micrometers for each of the eight experimental conditions. Positive values indicate beta leads, negative indicates alpha leads.
- schema:
  - `type`: table
  - `required_columns`: `experiment_id`, `predicted_phase_lead_um`
  - `columns`:
    - `experiment_id`:
      - `type`: integer
    - `predicted_phase_lead_um`:
      - `type`: number
      - `unit`: µm
  - `num_rows`: 8

Notes: The predicted phase leads are compared to the paper's observed phase leads (hidden) for classification into coupled and noncoupled regimes. Scoring tolerances account for implementation differences in the numerical model.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "predicted_phase_leads.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "experiment_id",
          "predicted_phase_lead_um"
        ],
        "columns": {
          "experiment_id": {
            "type": "integer"
          },
          "predicted_phase_lead_um": {
            "type": "number",
            "unit": "µm"
          }
        },
        "num_rows": 8
      },
      "description": "Predicted phase lead (distance between alpha and beta lamellar tips) in micrometers for each of the eight experimental conditions. Positive values indicate beta leads, negative indicates alpha leads."
    }
  ],
  "notes": "The predicted phase leads are compared to the paper's observed phase leads (hidden) for classification into coupled and noncoupled regimes. Scoring tolerances account for implementation differences in the numerical model."
}
```

## How you are scored
A hidden verifier inspects your predicted_phase_leads.csv.  It first validates the file structure (required columns, row count).  Then it compares your predicted phase leads to reference values obtained from experimental measurements (hidden).  The verifier applies tolerances and threshold rules that discriminate between coupled and noncoupled regimes: solutions that correctly classify experiments in the coupled regime (small phase leads comparable to the lamellar spacing) and the noncoupled regime (large phase leads) receive higher reward.  The total reward is a weighted sum of structural compliance and the quality of the predicted phase leads.  Reporting an arbitrary number is not sufficient; the verifier penalizes predictions that deviate significantly from the experimental regime classification.

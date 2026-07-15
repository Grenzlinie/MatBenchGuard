# Quadrupole Phonon Model Fitting and Anharmonic Observables for 114Cd

## Problem background
Even‑even spherical nuclei exhibit collective vibrational motion that can be modelled with quadrupole phonons. The simple harmonic picture, however, fails to account for observed deviations in energy level spacings and electromagnetic transition properties. A quadrupole phonon model that includes anharmonic coupling terms among phonons can capture these deviations. This task reproduces a numerical implementation of such a model, fitting it to the experimental level spectrum of the nucleus ¹¹⁴Cd and computing the resulting anharmonic energy levels and electromagnetic observables.

## Approach
The model Hamiltonian is constructed as an expansion in scalar‑coupled products of phonon creation and annihilation operators, with unknown interaction strengths w₂, w₃, w₄ and one‑phonon energy ω₀. The wavefunctions of the low‑lying 0⁺, 2⁺, and 4⁺ states are expanded as truncated, angular‑momentum‑coupled superpositions of multi‑phonon basis states (up to three or four phonons).

The experimental energies of the first three 2⁺ states in ¹¹⁴Cd (0.5585, 1.208, 1.840 MeV) are treated as the diagonal entries of the true Hamiltonian. By relating this diagonal Hamiltonian to the phonon‑model Hamiltonian via a unitary transformation, a set of linear equations is obtained that involves the unknown parameters and the expansion coefficients. An iterative procedure adjusts w₂, w₃, w₄ and ω₀ to reproduce the observed 2⁺ energies; the resulting 0⁺ and 4⁺ energies are then computed, and the whole fitting cycle is repeated until convergence. Once the model parameters and wavefunction coefficients are finalised, the predicted anharmonic energy levels are read from the Hamiltonian, and the wavefunctions are combined with the expanded form of the E2 transition operator (as described in the referenced Sorensen paper) to evaluate B(E2) ratios and the quadrupole moment ratio Q₂₂/Q₂₀.

## Reproduction target
Implement the complete quadrupole phonon model fitting procedure for ¹¹⁴Cd, using the experimental 2⁺ energies listed above. From the fitted model, compute the anharmonic energies (in MeV) of the following seven states: 2⁺, 2′⁺, 2″⁺, 0′⁺, 0″⁺, 4⁺, and 4′⁺. Write these as a CSV file with columns `state_label` and `energy_MeV` to `computed_energies.csv`.

Then, using the wavefunction expansion coefficients obtained from the fit and the expanded E2 transition operator (as given in the reference B. Sorensen, Nucl. Phys. A97 (1967) 1), compute the following dimensionless ratios:
1. B(E2,2′→0) / B(E2,2→0)
2. B(E2,2′→2) / B(E2,2→0)
3. B(E2,0′→2) / B(E2,2→0)
4. quadrupole moment ratio Q₂₂ / Q₂₀

Write the four results to `electromagnetic_observables.csv` with columns `observable` and `value`. All quantities must be derived from the fitted model; do not copy values from any external source.

## Assets

- Experimental 2+ energy levels of 114Cd
- Expanded E2 transition operator in phonon form: 10.1016/0375-9474(67)90445-X
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Fit quadrupole phonon model to experimental 2+ energies
- Role: process
- Action: Set up the quadrupole phonon model: define the Hamiltonian as a scalar-coupled expansion in phonon creation and annihilation operators with unknown interaction strengths w2, w3, w4 and one-phonon energy ω0. Expand wavefunctions for 0+, 2+, 4+ and their first few excited states as truncated sums of angular-momentum-coupled phonon basis states (up to a maximum of three or four phonons). Compute matrix elements of H in this basis. Using the given experimental energies of the first three 2+ states (0.5585, 1.208, 1.840 MeV for 114Cd) as the diagonal elements of the true Hamiltonian, transform the diagonal Hamiltonian into the phonon representation and equate the matrix elements term-by-term with the phonon-model ones. Determine the parameters w2, w3, w4, ω0 and the expansion coefficients by iteratively solving the resulting linear system: vary w2, w3, w4 to best reproduce the observed 2+ energies, then compute 0+ and 4+ energies and iterate until convergence. Save the final fitted interaction strengths, ω0, and all wavefunction coefficients.
- Evidence: `/app/outputs/fitted_parameters.json`

### Step 2: Compute anharmonic energy levels
- Role: scored (load-bearing)
- Action: Using the fitted phonon model (Hamiltonian and wavefunction coefficients) from the previous step, compute the energies (in MeV) of the following states in 114Cd: first excited 2+; second excited 2'+; third excited 2''+; first excited 0'+; second excited 0''+; first excited 4+; second excited 4'+. Write the state labels and computed energies to computed_energies.csv.
- Output file: `/app/outputs/computed_energies.csv`
- Format: csv
- Contract: columns: state_label (string), energy_MeV (float); rows: 7 states (2+, 2'+, 2''+, 0'+, 0''+, 4+, 4'+).
- Scoring: scored by hidden verifier

### Step 3: Calculate electromagnetic observables
- Role: scored (load-bearing)
- Action: Using the wavefunction expansion coefficients obtained from the fit and the expanded form of the electric quadrupole (E2) transition operator expressed in terms of phonon operators (as given in the referenced paper by Sorensen), compute the following ratios for 114Cd: (1) B(E2,2'→0)/B(E2,2→0), (2) B(E2,2'→2)/B(E2,2→0), (3) B(E2,0'→2)/B(E2,2→0), (4) quadrupole moment ratio Q22/Q20. Write the results to electromagnetic_observables.csv with one row per observable.
- Output file: `/app/outputs/electromagnetic_observables.csv`
- Format: csv
- Contract: columns: observable (string), value (float); rows: 4 entries (B(E2,2'→0)/B(E2,2→0), B(E2,2'→2)/B(E2,2→0), B(E2,0'→2)/B(E2,2→0), Q22/Q20).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_energies.csv`
- `/app/outputs/electromagnetic_observables.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_energies.csv
- path: `/app/outputs/computed_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed anharmonic energy levels for seven states in 114Cd.
- schema:
  - `type`: table
  - `required_columns`: `state_label`, `energy_MeV`
  - `units`:
    - `energy_MeV`: MeV
  - `description`: Each row contains a state label (string) and its computed energy (float in MeV).

### electromagnetic_observables.csv
- path: `/app/outputs/electromagnetic_observables.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed B(E2) ratios and quadrupole moment ratio for 114Cd.
- schema:
  - `type`: table
  - `required_columns`: `observable`, `value`
  - `description`: Each row contains an observable identifier (string) and its computed dimensionless value (float).

Notes: The scorer compares the agent's computed values against hidden reference values from the original paper using tolerances (0.05 MeV for energies, 0.1 for B(E2) ratios, 0.2 for Q22/Q20). The fitting step must be executed; the scored steps are load-bearing.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "state_label",
          "energy_MeV"
        ],
        "units": {
          "energy_MeV": "MeV"
        },
        "description": "Each row contains a state label (string) and its computed energy (float in MeV)."
      },
      "description": "Computed anharmonic energy levels for seven states in 114Cd."
    },
    {
      "file": "electromagnetic_observables.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "observable",
          "value"
        ],
        "description": "Each row contains an observable identifier (string) and its computed dimensionless value (float)."
      },
      "description": "Computed B(E2) ratios and quadrupole moment ratio for 114Cd."
    }
  ],
  "notes": "The scorer compares the agent's computed values against hidden reference values from the original paper using tolerances (0.05 MeV for energies, 0.1 for B(E2) ratios, 0.2 for Q22/Q20). The fitting step must be executed; the scored steps are load-bearing."
}
```

## How you are scored
Each scored artifact (`computed_energies.csv` and `electromagnetic_observables.csv`) is evaluated by an automated hidden verifier. For the energy levels, the verifier checks that your computed energies agree with the expected values within a prescribed absolute tolerance. For the electromagnetic ratios, it checks agreement within a separate tolerance. The final reward is a weighted combination of how many of the required entries meet these tolerance criteria. You do not need to match any exact numerical value, but your results must be physically reasonable and consistent with the model. Reporting the final numbers directly from the paper without performing the computation will not satisfy the scoring criteria; the verifier inspects the internal consistency of your outputs and requires that they be produced by the fitted model.

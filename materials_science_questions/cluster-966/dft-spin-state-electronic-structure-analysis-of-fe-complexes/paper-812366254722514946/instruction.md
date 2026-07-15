# Calculation of spin-forbidden d–d transition intensities and Faraday parameters using ligand-field theory

## Problem background
Magnetic circular dichroism (MCD) of spin-forbidden d-d transitions in octahedral high-spin Fe³⁺ complexes provides a sensitive probe of electronic structure and transition mechanisms. Quantitative analysis requires calculating electric-dipole oscillator strengths and Faraday parameters (A, B, C terms) from ligand-field theory. In this task, the focus is on the intensity mechanism where odd-parity vibrational modes break inversion symmetry of the octahedral environment, allowing electric-dipole intensity for spin-forbidden transitions from the ⁶A₁₉ ground state to low-lying quartet excited states. The computation tests whether a fully specified theoretical model can reproduce the spectroscopic observables.

## Approach
The reproduction follows a three-stage ligand-field pipeline. First, the Tanabe-Sugano energy matrices for the d⁵ configuration in an octahedral crystal field are set up and solved to obtain excitation energies and configuration-mixed wavefunctions for the low-lying quartet states (⁴T₁₉, ⁴T₂₉, ⁴E₉, ⁴A₁₉). Second, electric-dipole transition moments induced by odd vibrations are computed using the Koide-Pryce point-dipole model. In this model, odd-parity vibrational modes couple electronic states and allow spin-forbidden transitions via spin-orbit mixing between the ground sextet and quartet states; the electric-dipole matrix elements are evaluated through a closure approximation using given radial expectation values, a mean charge-transfer energy, and assumed normal-mode frequencies. The resulting transition moments yield oscillator strengths for all spin-forbidden transition–vibration combinations. Third, the Faraday parameters A, B, and C are derived from these moments together with magnetic dipole matrix elements, spin degeneracy factors, and spin-orbit coupling; the combined quantity B + C/kT is also reported.

## Reproduction target
Produce two CSV files under /app/outputs:

1. **oscillator_strengths_odd_vibrations.csv** — electric-dipole oscillator strengths (dimensionless) for the spin-forbidden transitions ⁶A₁₉ → ⁴T₂₉(1), ⁶A₁₉ → ⁴E₉(1), ⁶A₁₉ → ⁴A₁₉, and ⁶A₁₉ → ⁴T₁₉(1), each mediated by the three odd vibration modes T₁ᵤ(ν₃), T₁ᵤ(ν₄), and T₂ᵤ(ν₆). Columns: `initial_state`, `final_state`, `vibration_mode`, `oscillator_strength`.

2. **faraday_parameters_odd_vibrations.csv** — Faraday parameters A, B, C and the combined quantity B + C/kT for the transitions ⁶A₁₉ → ⁴T₂₉(1), ⁶A₁₉ → ⁴E₉(1), and ⁶A₁₉ → ⁴A₁₉, again for each odd vibration mode. Columns: `transition`, `vibration_mode`, `A` (10⁻²⁴ β e² cm²), `B` (10⁻²⁴ β e² cm²/cm⁻¹), `C` (10⁻²⁴ β e² cm²), `B_plus_C_over_kT` (10⁻²⁴ β e² cm²/cm⁻¹).

All parameters necessary for the calculation (Dq, B, C, ζ, δE, radial expectation values, metal-ligand distance, ligand mass, normal-mode frequencies, and kT) are provided in the workflow steps. The computed values must be consistent with the input parameters and the theoretical model described.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Solve Tanabe-Sugano matrices for quartet states
- Role: process
- Action: Set up the Tanabe-Sugano energy matrices for the d5 configuration in an octahedral crystal field with Dq=1500 cm⁻¹, Racah parameters B=600 cm⁻¹, C=3200 cm⁻¹. Solve the secular determinants to obtain excitation energies and configuration-mixed wavefunction expansion coefficients for the low-lying quartet states: ⁴T1g, ⁴T2g, ⁴Eg, and ⁴A1g.
- Evidence: `/app/outputs/cubic_field_states.json`

### Step 2: Compute oscillator strengths for odd-vibration mechanism
- Role: scored
- Action: Using the cubic-field wavefunctions from step_lf, implement the Koide-Pryce odd-vibration point-dipole model with spin-orbit coupling ζ=400 cm⁻¹, mean charge-transfer energy δE=10⁵ cm⁻¹, radial expectation values ⟨r²⟩=1.538 a0², ⟨r⁴⟩=5.852 a0⁴, ⟨r⁶⟩=50.167 a0⁶, metal-ligand distance R=4 a0, ligand mass M approximated by oxygen (16 amu), and assumed normal-mode frequencies T1u(ν3)=200 cm⁻¹, T1u(ν4)=400 cm⁻¹, T2u(ν6)=100 cm⁻¹. Calculate the electric-dipole oscillator strengths for the spin-forbidden transitions ⁶A1g→⁴T2g(1), ⁶A1g→⁴Eg(1), ⁶A1g→⁴A1g, and ⁶A1g→⁴T1g(1) mediated by each vibration mode. Write the results as a CSV.
- Output file: `/app/outputs/oscillator_strengths_odd_vibrations.csv`
- Format: csv
- Contract: initial_state (string), final_state (string), vibration_mode (string, e.g., T1u(nu3)), oscillator_strength (float)
- Scoring: scored by hidden verifier

### Step 3: Compute Faraday parameters for odd-vibration mechanism
- Role: scored (load-bearing)
- Action: From the transition moments obtained in step_osc, compute the Faraday parameters A, B, C for the transitions ⁶A1g→⁴T2g(1), ⁶A1g→⁴Eg(1), and ⁶A1g→⁴A1g, for each odd vibration mode. Use the magnetic dipole operator and spin degeneracy factors appropriate for a ⁶A1g ground state. Take kT=200 cm⁻¹. Write the results as a CSV with columns: transition, vibration_mode, A, B, C, B_plus_C_over_kT.
- Output file: `/app/outputs/faraday_parameters_odd_vibrations.csv`
- Format: csv
- Contract: transition (string, e.g., ^6A1g -> ^4T2g(1)), vibration_mode (string), A (float), B (float), C (float), B_plus_C_over_kT (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/oscillator_strengths_odd_vibrations.csv`
- `/app/outputs/faraday_parameters_odd_vibrations.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### oscillator_strengths_odd_vibrations.csv
- path: `/app/outputs/oscillator_strengths_odd_vibrations.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: CSV file containing oscillator strengths for spin-forbidden transitions enabled by odd vibrations. Each row corresponds to one transition–vibration pair.
- schema:
  - `type`: table
  - `required_columns`: `initial_state`, `final_state`, `vibration_mode`, `oscillator_strength`
  - `units`:
    - `oscillator_strength`: dimensionless

### faraday_parameters_odd_vibrations.csv
- path: `/app/outputs/faraday_parameters_odd_vibrations.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: CSV file containing Faraday parameters A, B, C and the combined quantity B+C/kT for the low-lying spin-forbidden transitions enabled by odd vibrations.
- schema:
  - `type`: table
  - `required_columns`: `transition`, `vibration_mode`, `A`, `B`, `C`, `B_plus_C_over_kT`
  - `units`:
    - `A`: 10^-24 beta e^2 cm^2
    - `B`: 10^-24 beta e^2 cm^2/cm^-1
    - `C`: 10^-24 beta e^2 cm^2
    - `B_plus_C_over_kT`: 10^-24 beta e^2 cm^2/cm^-1

Notes: The intermediate cubic-field wavefunctions from step_lf are saved as evidence but are not scored. The scored artifact for oscillator strengths covers all four transitions listed in Table II, while the Faraday parameter output is restricted to the three transitions given in Table III.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "oscillator_strengths_odd_vibrations.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "initial_state",
          "final_state",
          "vibration_mode",
          "oscillator_strength"
        ],
        "units": {
          "oscillator_strength": "dimensionless"
        }
      },
      "description": "CSV file containing oscillator strengths for spin-forbidden transitions enabled by odd vibrations. Each row corresponds to one transition–vibration pair."
    },
    {
      "file": "faraday_parameters_odd_vibrations.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "transition",
          "vibration_mode",
          "A",
          "B",
          "C",
          "B_plus_C_over_kT"
        ],
        "units": {
          "A": "10^-24 beta e^2 cm^2",
          "B": "10^-24 beta e^2 cm^2/cm^-1",
          "C": "10^-24 beta e^2 cm^2",
          "B_plus_C_over_kT": "10^-24 beta e^2 cm^2/cm^-1"
        }
      },
      "description": "CSV file containing Faraday parameters A, B, C and the combined quantity B+C/kT for the low-lying spin-forbidden transitions enabled by odd vibrations."
    }
  ],
  "notes": "The intermediate cubic-field wavefunctions from step_lf are saved as evidence but are not scored. The scored artifact for oscillator strengths covers all four transitions listed in Table II, while the Faraday parameter output is restricted to the three transitions given in Table III."
}
```

## How you are scored
A hidden verifier reads the two CSV files and independently compares each reported value to reference target values obtained from the same theoretical model. Each scored artifact (oscillator strengths and Faraday parameters) contributes to the final reward with predetermined weights. The check ensures that the reported numbers are physically accurate and within acceptable tolerances; simply hardcoding the target numbers without executing the correct computational pipeline will not pass. The verifier does NOT require matching any particular paper figure or table format — only that the required columns and rows exist and the numerical values fall within the expected ranges.

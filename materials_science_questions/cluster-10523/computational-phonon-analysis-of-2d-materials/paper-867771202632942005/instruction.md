# Charged-Phonon Model of Gate-Tunable Phonon Anomalies in ABC Trilayer Graphene

## Problem background
ABC (rhombohedral) stacked trilayer graphene exhibits unusual infrared absorption from in-plane optical phonons near 1580 cm⁻¹. In this non-polar layered material, interactions between the lattice vibrations and the electronic system can transfer oscillator strength from interband electronic transitions to the phonon mode. This charged-phonon effect produces a strong, doping-dependent absorption feature and a simultaneous frequency shift. This task implements the theoretical charged-phonon model to compute how the phonon spectral weight (integrated optical conductivity) and frequency shift vary with carrier density in ABC trilayer graphene.

## Approach
The approach proceeds in two main stages. First, the electronic band structure of ABC trilayer graphene is obtained from a tight-binding model that includes nearest-neighbor intralayer hopping (γ₀) and interlayer coupling (γ₁). The secular equation for the in-plane optical phonon modes, parameterized by interlayer force constants, is solved to identify the eigenvector of the single infrared-active mode (the Eᵤ mode). Second, the charged-phonon formalism is applied: the mixed current-phonon response function and the phonon self-energy are evaluated at the bare phonon energy. These response functions capture how electron-phonon coupling, modified by Pauli blocking at finite doping, renormalizes the phonon spectral weight and frequency. The calculation is performed under a rigid-band approximation (the Fermi level is shifted to match a given carrier density), using a constant deformation potential, room temperature, and a phenomenological broadening to model disorder. The resulting spectral weight and frequency shift are recorded for each specified doping level.

## Reproduction target
Implement the tight-binding and charged-phonon model for the ABC trilayer. Compute the phonon spectral weight (integrated optical conductivity, in units of 10³ Ω⁻¹ cm⁻¹) and the frequency shift (in cm⁻¹) of the infrared-active mode at five carrier densities: 0, 1×10¹², 5×10¹², 1×10¹³, and 2×10¹³ cm⁻². Write the results to the CSV file specified in the workflow steps.

## Assets
All required numerical parameters (tight-binding hopping integrals, interlayer force constants, deformation potential, bare phonon frequency, temperature, and broadening) are explicitly stated in the workflow steps. No external datasets, pre-trained models, or proprietary tools are needed; the entire workflow can be implemented using standard scientific Python libraries (NumPy, SciPy).

## Workflow steps

### Step 1: Compute ABC trilayer band structure and phonon eigenvector
- Role: process
- Action: Implement the tight-binding Hamiltonian for ABC-stacked trilayer graphene with nearest-neighbor intralayer hopping γ0=3.16 eV and interlayer coupling γ1=0.37 eV. Diagonalize on a dense k-point grid to obtain the band structure and density of states. Solve the secular equation for the in-plane optical phonon modes with interlayer force constants ε=2.2 cm⁻¹ and δ=3 cm⁻¹, obtaining the IR-active E_u mode eigenvector (relative layer displacements). This step provides the electronic structure and phonon eigenvector required for the charged-phonon calculation.
- Evidence: none

### Step 2: Compute phonon spectral weight and frequency shift
- Role: scored (load-bearing)
- Action: Using the band structure and E_u eigenvector, compute the charged-phonon mixed current-phonon response function χ_jν(ω) and phonon self-energy χ_νν(ω) at the phonon energy ω₀ = 1580.5 cm⁻¹ (0.196 eV). Calculate spectral weight W = π [Re χ_jν(ω₀)]² / ω₀ and frequency shift Δω = Re χ_νν(ω₀) for carrier densities n = 0, 1×10¹², 5×10¹², 1×10¹³, 2×10¹³ cm⁻². Assume rigid-band doping (shift Fermi level), use deformation potential g=0.27 eV, temperature T=300 K, and phenomenological damping η=20 meV. Save results to abc_trilayer_charged_phonon_results.csv with columns: doping (cm⁻²), spectral_weight (10³ Ω⁻¹ cm⁻¹), frequency_shift (cm⁻¹).
- Output file: `/app/outputs/abc_trilayer_charged_phonon_results.csv`
- Format: csv
- Contract: columns: doping (cm^-2), spectral_weight (10^3 Ω^-1 cm^-1), frequency_shift (cm^-1)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/abc_trilayer_charged_phonon_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### abc_trilayer_charged_phonon_results.csv
- path: `/app/outputs/abc_trilayer_charged_phonon_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed phonon spectral weight and frequency shift for ABC trilayer graphene at five doping levels, compared to hidden reference values from the paper's theoretical curves with tolerance and trend checks.
- schema:
  - `type`: table
  - `required_columns`: `doping`, `spectral_weight`, `frequency_shift`
  - `units`:
    - `doping`: cm^-2
    - `spectral_weight`: 10^3 Ω^-1 cm^-1
    - `frequency_shift`: cm^-1

Notes: The checker verifies the agent's reported values against reference values and checks the expected monotonic trends: spectral weight increases with doping magnitude, and frequency shift becomes more negative (red shift) with doping.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "abc_trilayer_charged_phonon_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "doping",
          "spectral_weight",
          "frequency_shift"
        ],
        "units": {
          "doping": "cm^-2",
          "spectral_weight": "10^3 Ω^-1 cm^-1",
          "frequency_shift": "cm^-1"
        }
      },
      "description": "Computed phonon spectral weight and frequency shift for ABC trilayer graphene at five doping levels, compared to hidden reference values from the paper's theoretical curves with tolerance and trend checks."
    }
  ],
  "notes": "The checker verifies the agent's reported values against reference values and checks the expected monotonic trends: spectral weight increases with doping magnitude, and frequency shift becomes more negative (red shift) with doping."
}
```

## How you are scored
Your submitted CSV file is evaluated by an automated hidden verifier. The verifier first checks that the file is well-formed with the required columns. It then compares the reported spectral weight and frequency shift at each doping level against reference values (derived from the original theoretical predictions) using appropriate tolerances. Additionally, the verifier examines the structural behavior of the results across the doping range to ensure they satisfy expected physical trends (e.g., monotonic variation of spectral weight and frequency shift with doping). The final reward is a weighted combination of these numeric and structural checks. Simply reporting numbers without a genuine implementation of the described model will not earn full credit.

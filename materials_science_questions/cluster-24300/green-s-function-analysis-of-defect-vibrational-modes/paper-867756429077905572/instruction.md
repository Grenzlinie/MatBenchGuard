# Harmonic Emission Spectrum from a Single Energy-Operator Defect in a Quantum Wire

## Problem background
The study of conductance in one-dimensional quantum wires with impurities has advanced with non-perturbative integrable techniques. When such wires are coupled to an external laser field, the system can exhibit harmonic generation: the emitted light contains frequencies that are multiples of the driving laser frequency. This task focuses on a model of a free fermion quantum wire containing a single energy-operator defect and subjected to a monochromatic laser pulse. The goal is to compute the harmonic emission spectrum—the intensity of the emitted radiation as a function of frequency—arising from the dipole moment of the fermion wave packet interacting with the defect.

## Approach
The calculation proceeds in two stages. First, the time-dependent transmission probability |T(t)|² for a fermion scattering off the defect is evaluated. The defect is of energy-operator type located at position y=0, with coupling strength g=3.5, and the incoming fermion has rapidity θ=1.2. The laser field is taken as E(t)=E₀ cos(ω t) for 0 ≤ t ≤ τ, with field amplitude E₀=2.0, frequency ω=0.2, and pulse length corresponding to N=5 cycles (τ = 2πN/ω). The vector potential A(t) follows from the field via A(t) = -(1/2) ∫₀ᵗ E(s) ds, yielding A(t) = −E₀/(2ω) sin(ωt) during the pulse. The transmission probability squared is given by the rational expression

|T(t)|² = (ã₀ + a₂ A(t)² + a₄ A(t)⁴) / (a₀ + a₂ A(t)² + a₄ A(t)⁴),

with coefficients

a₀ = 16 g² + (4 + g²)² sinh²θ,
ã₀ = (g² − 4)² sinh²θ,
a₂ = 2 g² (4 + g²) sinh²θ,
a₄ = g⁴ sinh²θ.

The complex transmission and reflection amplitudes needed for constructing the wavefunction are

T(t) = [i (1 + (A(t) - 2i/g)²) sinhθ * (4/g)] / [1 - i/4 (4/g² + 1 + A(t)²) sinhθ],

R(t) = -coshθ / [1 - i/4 (4/g² + 1 + A(t)²) sinhθ],

R(-θ;t) = -coshθ / [1 + i/4 (4/g² + 1 + A(t)²) sinhθ].

The squared modulus calculated from these expressions coincides with the rational formula above.

The positive-energy Weyl spinors for rapidity θ and −θ are

u(θ) = (1/√2) [e^{-θ/2}, e^{θ/2}]^T,    u(−θ) = (1/√2) [e^{θ/2}, e^{-θ/2}]^T.

On the right side of the defect (x>0) the one-particle wavefunction is

Φ(x,t) = g(x,t) e^{i x A(t)} T(t) [ u(θ) e^{i p x} + u(−θ) e^{-i p x} R(−θ;t) ],

with p = sinhθ. The Gaussian envelope is g(x,t) = exp[−(x − x0 − v_g t)^2 / (2 Δ^2)], where v_g = tanhθ and a nominal offset x0 = 20 ensures the packet starts away from the defect, and the packet width Δ = 6.

This intermediate step produces evidence but is not directly scored.

Second, the harmonic emission spectrum is computed. Using the one-particle wavefunction defined above, with Gaussian envelope of width Δ=6 and the analytic transmission and reflection amplitudes, compute the expectation value of the dipole moment ⟨x⟩(t) = ∫ x |Φ(x,t)|² dx over the pulse duration. Then compute the absolute value of the Fourier transform of ⟨x⟩(t) to obtain the harmonic emission spectrum. Normalize the spectrum such that its maximum intensity is 1, and output it as a function of frequency in units of ω up to 20ω.

## Reproduction target
Compute the harmonic emission spectrum for the single energy-operator defect with parameters g=3.5, θ=1.2, ω=0.2, E₀=2.0, Δ=6, and pulse length N=5 cycles. Output a CSV file named harmonic_spectrum.csv with columns:
- omega_multiples: frequency in multiples of ω, from 0 to 20.
- intensity: the normalized intensity (0 to 1).
The file must be placed in /app/outputs.

## Assets

- numpy: https://pypi.org/project/numpy/
- scipy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Compute time-dependent transmission probability
- Role: process
- Action: Implement the analytic expression for the time-dependent transmission probability |T(θ,g,A(t))|² for the single energy-operator defect at position y=0, using the given closed-form formulas for the coefficients a0, ã0, a2, a4 and the rational function of the vector potential A(t). The vector potential A(t) is derived from a monochromatic laser pulse with electric field E(t)=E₀ cos(ω t) for 0 ≤ t ≤ τ (τ=2πN/ω, N=5). The defect coupling g=3.5, particle rapidity θ=1.2, field amplitude E₀=2.0, frequency ω=0.2. Evaluate |T(t)|² on a fine time grid over the pulse duration and save the time grid and corresponding transmission probability values as evidence.
- Evidence: `/app/outputs/transmission_probability.csv`

### Step 2: Compute harmonic emission spectrum
- Role: scored (load-bearing)
- Action: Using the analytic expressions for the transmission amplitude T(t), reflection amplitude R(t), and R(-θ;t) provided in the Approach section, construct the one-particle wavefunction with a Gaussian envelope of width Δ=6 and compute the expectation value of the dipole moment ⟨x⟩(t) = ∫ x |Φ(x,t)|² dx over the pulse duration. Then compute the absolute value of the Fourier transform of ⟨x⟩(t) to obtain the harmonic emission spectrum. Normalize the spectrum so that the highest peak has intensity 1. Output the spectrum as a CSV file with columns 'omega_multiples' (frequency in units of ω, range 0 to 20) and 'intensity' (normalized).
- Output file: `/app/outputs/harmonic_spectrum.csv`
- Format: csv
- Contract: Two columns: omega_multiples (float, frequency in units of ω) and intensity (float, normalized).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/harmonic_spectrum.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### harmonic_spectrum.csv
- path: `/app/outputs/harmonic_spectrum.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Harmonic emission spectrum for a single energy-operator defect. The checker will recompute the spectrum from the same parameters and compare peak positions and intensities.
- schema:
  - `type`: table
  - `required_columns`: `omega_multiples`, `intensity`
  - `units`:
    - `omega_multiples`: multiples of ω
    - `intensity`: normalized

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "harmonic_spectrum.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "omega_multiples",
          "intensity"
        ],
        "units": {
          "omega_multiples": "multiples of ω",
          "intensity": "normalized"
        }
      },
      "description": "Harmonic emission spectrum for a single energy-operator defect. The checker will recompute the spectrum from the same parameters and compare peak positions and intensities."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier will independently recompute the harmonic spectrum using identical physical parameters and conditions. It will compare your submitted CSV to the reference by evaluating the presence, locations, and relative intensities of harmonic peaks. The reward is proportional to the agreement; a faithful implementation that produces the correct spectral features receives a high score, while deviations reduce the score. Simply reporting expected numbers without a correct computational pipeline will be penalized, as the verifier's check will detect mismatches.

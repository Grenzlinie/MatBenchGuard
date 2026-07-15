# Effective Mass Estimation for Thermoelectric Materials using Single-Parabolic-Band Model

## Problem background
Thermoelectric materials convert heat to electricity and vice versa, and their performance depends on the Seebeck coefficient, electrical conductivity, and thermal conductivity. For filled skutterudites, the charge carrier effective mass is a key parameter that influences these transport properties. Accurately estimating the effective mass from experimental transport measurements allows comparison across compounds and guides the design of improved thermoelectric materials. This task focuses on computing the effective hole mass for a specific skutterudite compound, CeFe4As12, using a single‑parabolic‑band model with acoustic phonon scattering, given its room‑temperature transport coefficients.

## Approach
The single‑parabolic‑band model relates the measured Seebeck coefficient and Hall carrier concentration to the reduced Fermi energy and the effective mass. Under the assumption of acoustic phonon scattering, the Seebeck coefficient S is expressed as a function of the reduced Fermi energy η through a combination of Fermi–Dirac integrals. This implicit equation can be solved numerically for η. Once η is known, the carrier concentration p provides a second relation that connects η and the density‑of‑states effective mass m_d via another Fermi–Dirac integral. For a single parabolic valley, the density‑of‑states effective mass equals the effective mass m*. Substituting the solved η and evaluating the carrier concentration expression yields the effective hole mass. The procedure requires no external empirical data beyond the provided room‑temperature transport measurements and can be implemented with standard numerical libraries for special functions and root finding.

## Reproduction target
Compute the effective hole mass m* (in units of the free electron mass m₀) for CeFe4As12 using the single‑parabolic‑band model with acoustic phonon scattering. The calculation must use the following room‑temperature transport data: Seebeck coefficient S = 37 μV/K, electrical resistivity ρ = 0.49 mΩ cm, and Hall carrier concentration p = 6.3×10²⁰ cm⁻³. The result is to be written to the output file /app/outputs/step_01_effective_mass.json containing a single JSON field "m_star" with the computed value. The resistivity is provided for completeness; only S and p are needed for the SPB effective mass calculation.

## Assets

- SciPy: scipy

## Workflow steps

### Step 1: SPB Effective Mass Calculation
- Role: scored (load-bearing)
- Action: Compute the effective hole mass m* (in units of free electron mass m0) for CeFe4As12 using a single-parabolic-band model with acoustic phonon scattering. Use the room-temperature transport data: Seebeck coefficient S = 37 μV/K, electrical resistivity ρ = 0.49 mΩ cm, and Hall carrier concentration p = 6.3×10^20 cm^-3. First, solve for the reduced Fermi energy η from the Seebeck coefficient relation S = (k/e) * [ (2 F_1(η)/F_0(η)) - η ] (acoustic phonon scattering). Then compute m* from p = (1/2π²) (2 m_d kT/ħ²)^{3/2} F_{1/2}(η) with density-of-states effective mass m_d = N_v^{2/3} m* (N_v = 1 for a single valley).
- Output file: `/app/outputs/step_01_effective_mass.json`
- Format: json
- Contract: {"m_star": "float, effective hole mass in units of free electron mass m0"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_effective_mass.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_effective_mass.json
- path: `/app/outputs/step_01_effective_mass.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed effective hole mass for CeFe4As12. The value is compared to a hidden gold within an absolute tolerance that absorbs legitimate numerical spread.
- schema:
  - `type`: object
  - `required`:
    - `m_star`: float, effective hole mass in units of free electron mass m0

Notes: Only the effective mass calculation stage of the paper is reproduced, as it is the only stage with precisely tabulated inputs and a well-defined, independently recomputable result. The ZT, lattice thermal conductivity, and carrier concentration normalization stages are omitted because the required temperature-dependent data are presented solely in figures, making exact extraction unreliable for deterministic verification, and the linear extrapolation method is insufficiently specified.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_effective_mass.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "m_star": "float, effective hole mass in units of free electron mass m0"
        }
      },
      "description": "Computed effective hole mass for CeFe4As12. The value is compared to a hidden gold within an absolute tolerance that absorbs legitimate numerical spread."
    }
  ],
  "notes": "Only the effective mass calculation stage of the paper is reproduced, as it is the only stage with precisely tabulated inputs and a well-defined, independently recomputable result. The ZT, lattice thermal conductivity, and carrier concentration normalization stages are omitted because the required temperature-dependent data are presented solely in figures, making exact extraction unreliable for deterministic verification, and the linear extrapolation method is insufficiently specified."
}
```

## How you are scored
A hidden verifier independently checks your submitted artifact. It compares your computed m_star against a hidden reference value derived from the physical model. Scoring uses an absolute tolerance that accounts for legitimate numerical variations arising from different implementations (e.g., choice of Fermi–Dirac integral approximation, root‑finding tolerance), while requiring that the result correctly reflects the underlying SPB transport equations. If your computed m_star falls within the tolerance, you earn full credit for this stage; the reward decreases as the deviation grows. The final reward is a weighted combination across all scored stages (here only one stage). Simply reporting a number without executing the computational pipeline will not suffice; the verifier checks that the output is produced through the required workflow.

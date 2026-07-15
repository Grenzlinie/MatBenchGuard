# Superconducting Tc and isotope-effect coefficient for multi-channel interactions

## Problem background
In conventional superconductors, the isotope effect—the dependence of the critical temperature \(T_c\) on atomic mass—provides key evidence for the pairing mechanism. When the pairing is purely phonon-mediated, the isotope coefficient \(\alpha\) is approximately 0.5. Deviations from this value, including negative (inverse) isotope effects, are observed in many exotic superconductors (cuprates, organics, strontium ruthenate) and indicate the presence of additional interactions beyond simple phonons. This task addresses the general case of superconductors in which multiple pairing interactions coexist—phonon, nonphonon (e.g., spin fluctuations), and direct Coulomb repulsion. The goal is to compute \(T_c\) and the isotope coefficient \(\alpha\) from the analytic solution of the linearized gap equation for systems with several interaction channels, each having an ordered cutoff energy.

## Approach
The approach is based on a model of separable pairing interactions with a hierarchy of cutoff energies \(\omega_1 < \omega_2 < \dots < \omega_n\). For each channel \(k\), a dimensionless coupling constant \(\lambda_k\) and a mass-sensitivity coefficient \(\alpha_{k0} = -\partial\ln\omega_k/\partial\ln M\) are defined. The linearized gap equation is solved by introducing a recurrence for effective couplings \(\lambda_k^*\) that starts from the highest cutoff and propagates downward, yielding an effective coupling \(\tilde{\lambda}_1\) for the softest channel. The transition temperature is then \(T_c = (2e^{\gamma}/\pi)\,\omega_1\, e^{-1/\tilde{\lambda}_1}\) with \(\gamma\) the Euler constant. The isotope coefficient is a weighted sum \(\alpha = \sum_k C_k \alpha_{k0}\), where the weights \(C_k\) are derived from the effective couplings \(\lambda_k^*\). Two regimes are distinguished by the ordering of the nonphonon cutoff \(\omega_{\text{np}}\) relative to the Debye frequency \(\omega_D\): case (a) \(\omega_{\text{np}} < \omega_D\) and case (b) \(\omega_{\text{np}} > \omega_D\). In both regimes, a direct Coulomb interaction with a high cutoff can be included. The task is to implement the recurrence, compute \(T_c\) and \(\alpha\) for a set of parameter combinations that cover generic two- and three-channel situations as well as the two regimes of the phonon/nonphonon/Coulomb model, and output the results.

## Reproduction target
Implement the recurrence for \(\lambda_k^*\), compute \(T_c\) and \(\alpha\) for the test cases specified below, and write the results to `results.json`. The test cases represent different physical scenarios with known public parameters: the number of channels \(n\), the coupling constants \(\lambda_k\), the cutoff energies \(\omega_k\) (in arbitrary but consistent energy units), and the mass-sensitivity coefficients \(\alpha_{k0}\).

Test cases:
1. `n2_generic`: two-channel generic model (no Coulomb). Parameters: n=2, λ=[0.30, 0.15], ω=[50.0, 200.0], α0=[0.5, 0.5].
2. `n2_coulomb`: phonon plus Coulomb interaction (standard model). Parameters: n=2, λ=[0.45, -0.12], ω=[60.0, 5000.0], α0=[0.5, 0.0].
3. `n3_coulomb`: three-channel model with phonon, nonphonon, and Coulomb interactions, generic ordering. Parameters: n=3, λ=[0.20, 0.10, -0.08], ω=[30.0, 100.0, 1000.0], α0=[0.5, 0.0, 0.0].
4. `case_a`: regime \(\omega_{\text{np}} < \omega_D < W\). Parameters: n=3, λ=[0.25, 0.35, -0.10], ω=[40.0, 120.0, 600.0], α0=[0.5, 0.5, 0.0]. (nonphonon channel first in the ordered list, then phonon, then Coulomb).
5. `case_b`: regime \(\omega_D < \omega_{\text{np}} < W\). Parameters: n=3, λ=[0.35, 0.20, -0.10], ω=[100.0, 250.0, 800.0], α0=[0.5, 0.0, 0.0]. (phonon channel first, then nonphonon, then Coulomb).

The computed \(T_c\) must be in the same energy units as \(\omega_1\). The isotope coefficient \(\alpha\) is dimensionless.

## Assets

- numpy: numpy

## Workflow steps

### Step 1: Compute Tc and alpha for specified test cases
- Role: scored
- Action: Implement the analytic recurrence for effective couplings λ_k* (from the linearized gap equation for separable channels with ordered cutoffs), compute the effective coupling λ̃₁ = λ₁ + λ₂*, then Tc = (2*e^γ/π)*ω₁*exp(-1/λ̃₁), and the isotope coefficient α = Σ C_k α_k0 with weights C_k = Λ_k - Λ_{k+1} and Λ_k = Π_{l=1}^{k-1}[λ_{l+1}*/(λ_l + λ_{l+1}*)]^2. For each test case provided in the Instruction with parameters (number of channels n, coupling constants λ_k, cutoff energies ω_k, and mass-sensitivity coefficients α_k0), compute Tc (in same energy units as ω₁) and α (dimensionless) and write the results to results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON array of objects, each with keys: case_id (string), Tc (number, in same energy units as omega_1), alpha (number, dimensionless).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed Tc and alpha for each test case.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `case_id`, `Tc`, `alpha`
    - `properties`:
      - `case_id`:
        - `type`: string
      - `Tc`:
        - `type`: number
      - `alpha`:
        - `type`: number

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "case_id",
            "Tc",
            "alpha"
          ],
          "properties": {
            "case_id": {
              "type": "string"
            },
            "Tc": {
              "type": "number"
            },
            "alpha": {
              "type": "number"
            }
          }
        }
      },
      "description": "Computed Tc and alpha for each test case."
    }
  ],
  "notes": ""
}
```

## How you are scored
After your submission, a hidden verifier will read your `results.json`. For each test case, the verifier independently recomputes \(T_c\) and \(\alpha\) using the same analytic formulas and the public parameters listed above. Your reported values are then compared to the verifier's reference values. The comparison uses tolerances appropriate for the numerical precision of the method; you do not need to guess the tolerances—simply compute the quantities as accurately as possible with standard double precision. The overall reward is proportional to the fraction of test cases for which both \(T_c\) and \(\alpha\) pass the verifier's check. You must output all required cases with the exact `case_id` strings; missing or misnamed entries will not be scored.

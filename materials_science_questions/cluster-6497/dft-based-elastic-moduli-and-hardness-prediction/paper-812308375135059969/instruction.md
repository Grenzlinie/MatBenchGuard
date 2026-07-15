# DFT Band Energies of Si with LDA and Nonlocal Functional

## Problem background
Standard density functional theory (DFT) calculations using the local density approximation (LDA) are known to underestimate band gaps in semiconductors. Nonlocal exchange-correlation functionals can improve the description of conduction band energies. This task demonstrates the effect in silicon: compute the band energies at high-symmetry points (Γ, X, L) with both LDA and a nonlocal exponential-screened functional, to verify how the nonlocal treatment affects the conduction band positions.

## Approach
Use a plane-wave DFT code (e.g., Quantum ESPRESSO) with norm-conserving nonlocal pseudopotentials for Si. Perform two self-consistent calculations on bulk silicon in its diamond structure:
1. **LDA**: Kohn-Sham exchange + Wigner correlation.
2. **Nonlocal exponential-screened functional**: a screened correlation potential of the form
   \( W_c(\mathbf{r}) = -\tfrac12 \int d\mathbf{r}'\, \frac{e^{-\xi|\mathbf{r}-\mathbf{r}'|}}{|\mathbf{r}-\mathbf{r}'|} \rho(\mathbf{r}') \)
   with screening parameter \(\xi^2 = 2 k_F^2\) and Fermi wavevector \(k_F = 1.81\,\mathrm{Å}^{-1}\).
For each functional, solve the Kohn-Sham equations to obtain eigenvalues at the Γ, X, and L k-points. Shift the energy scale so that the valence band maximum (Γ₂₅') is at 0 eV and report the resulting band energies.

## Reproduction target
Compute and save the band energies (relative to the VBM) for the following high-symmetry points in bulk Si: Γ₁₅, Γ₂', X₁, X₄, X₃, L₁, L₃', L₁, L₃. Do this for both the LDA and the exponential-screened nonlocal functional. The required output is a single JSON file (`si_band_energies.json`) with the structure described in the workflow steps. The goal is to obtain band energies that agree with the reference values from a first-principles study; the hidden verifier will quantify the agreement.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Bachelet-Hamann-Schlüter Si pseudopotential: 10.1103/PhysRevB.26.4199

## Workflow steps

### Step 1: Compute Si band energies with LDA and nonlocal functional
- Role: scored (load-bearing)
- Action: Perform self-consistent DFT calculations for bulk silicon (diamond structure) using two exchange-correlation treatments: (1) LDA with Kohn-Sham exchange and Wigner correlation, and (2) the nonlocal exponential-screened functional with screening parameter ξ² (ξ² = 2k_F², k_F = 1.81 Å⁻¹). Use norm-conserving nonlocal pseudopotentials (Bachelet-Hamann-Schlüter) and a plane-wave basis. Solve the Kohn-Sham equations to obtain eigenvalues at the Γ, X, and L high-symmetry k-points. For each functional, extract the band energies relative to the valence band maximum (Γ₂₅' set to 0 eV) and save them to /app/outputs/si_band_energies.json.
- Output file: `/app/outputs/si_band_energies.json`
- Format: json
- Contract: object with keys 'lda' and 'nonlocal_expscreening'; each value is an array of objects { point: string, energy_eV: number }
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/si_band_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### si_band_energies.json
- path: `/app/outputs/si_band_energies.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Computed band energies of Si for each functional, relative to the valence band maximum. The file is used by the checker to compute the mean absolute error (MAE) against the hidden reference values; full credit is awarded when MAE ≤ 0.2 eV.
- schema:
  - `type`: object
  - `required`: `lda`, `nonlocal_expscreening`
  - `properties`:
    - `lda`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `point`:
            - `type`: string
          - `energy_eV`:
            - `type`: number
        - `required`: `point`, `energy_eV`
    - `nonlocal_expscreening`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `point`:
            - `type`: string
          - `energy_eV`:
            - `type`: number
        - `required`: `point`, `energy_eV`

Notes: The agent must compute the band energies with the two functionals and report them in the specified JSON structure. The scoring is based on the agreement with the paper's reference values (not visible to the agent); no other output is scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "si_band_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "lda",
          "nonlocal_expscreening"
        ],
        "properties": {
          "lda": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "point": {
                  "type": "string"
                },
                "energy_eV": {
                  "type": "number"
                }
              },
              "required": [
                "point",
                "energy_eV"
              ]
            }
          },
          "nonlocal_expscreening": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "point": {
                  "type": "string"
                },
                "energy_eV": {
                  "type": "number"
                }
              },
              "required": [
                "point",
                "energy_eV"
              ]
            }
          }
        }
      },
      "description": "Computed band energies of Si for each functional, relative to the valence band maximum. The file is used by the checker to compute the mean absolute error (MAE) against the hidden reference values; full credit is awarded when MAE ≤ 0.2 eV."
    }
  ],
  "notes": "The agent must compute the band energies with the two functionals and report them in the specified JSON structure. The scoring is based on the agreement with the paper's reference values (not visible to the agent); no other output is scored."
}
```

## How you are scored
A hidden verifier independently reads your `si_band_energies.json` and compares the reported band energies to a set of expected reference values (obtained from a prior computational study) for each functional and k-point. It computes the mean absolute error (MAE) across all reported points. If the MAE meets the verifier's predefined threshold, you receive full credit; otherwise, the reward decreases smoothly as the MAE increases. This approach rewards genuine reproduction without penalizing small numerical deviations that arise from different DFT implementations or convergence settings. Only the single scored artifact is evaluated; there are no other scored outputs.

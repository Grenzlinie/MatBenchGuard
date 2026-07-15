# Anharmonic Effective Potential Model for Temperature-Dependent Phonon Frequency

## Problem background
Some superionic conductors exhibit low-frequency optical phonon modes whose anomalous temperature dependence cannot be explained by harmonic lattice dynamics. The layered superionic conductor AgCrS₂ hosts a very-low-frequency transverse optical (TO) mode at the zone center that softens significantly with increasing temperature and shows a pronounced change in slope near 200 K. This strong temperature dependence has been attributed to a highly anharmonic effective potential for the relative in-plane motion of the silver layers against the CrS₂ layers. The task is to compute the temperature-dependent frequency $\tilde{\nu}(T)$ of this mode from the anharmonic model.

## Approach
The relative motion of the Ag and CrS₂ layers is treated as a single effective particle with mass $\mu$, moving in a two-dimensional anharmonic potential $W(x,y)$ that respects the $C_{3v}$ site symmetry. The potential is parametrized as a sum of exponential terms with given coefficients $a_2,b_2,a_3,b_3,a_4,b_4$. The effective mass $\mu$ is defined by $1/\mu = 1/m_{\text{Ag}} + 1/(m_{\text{Cr}}+2m_{\text{S}})$ using atomic masses. For each temperature $T$, the classical thermal-average curvature $\langle \phi(T)\rangle$ is obtained by numerically integrating the Boltzmann-weighted curvature $\partial^2 W/\partial r^2$ over the $(x,y)$ plane and normalizing by the partition function $Z$. The mode frequency follows from $\omega^2(T) = \langle \phi(T)\rangle/\mu$, and the wavenumber in cm⁻¹ is $\tilde{\nu}(T) = \omega(T)/(2\pi c)$. The integration must be carried out over a domain large enough that the integrand has decayed to negligible values.

## Reproduction target
Produce a CSV file that lists the computed TO-mode wavenumbers $\tilde{\nu}(T)$ for $T$ ranging from 10 K to 700 K in steps of 10 K. The CSV must contain two columns: `T_K` (temperature in kelvin) and `frequency_cm-1` (wavenumber in cm⁻¹). The verifier will compare your computed frequencies against hidden reference data and will also verify that the curve exhibits the expected qualitative behavior: a significant decrease from low temperatures (the frequency at 10 K should be larger than at 100 K) and a slope change near 200 K (the slope between 100 K and 200 K should be more negative than the slope between 300 K and 400 K).

## Assets

- numpy/scipy (numerical integration): numpy scipy

## Workflow steps

### Step 1: Compute temperature-dependent TO mode frequency from anharmonic potential
- Role: scored (load-bearing)
- Action: Implement the anharmonic effective potential W(x,y) = 0.5*a2*(1-exp(-b2*(x^2+y^2))) + a3*(1-exp(-b3*(x^3-3*x*y^2))) + a4*(1-exp(-b4*(x^2+y^2)^2)) with the fitted parameters: a2=0.17 eV, b2=1.9 Å^{-2}; a3=0.12 eV, b3=0.15 Å^{-3}; a4=0.22 eV, b4=0.15 Å^{-4}. Define the effective mass μ via 1/μ = 1/m_Ag + 1/(m_Cr+2m_S) using appropriate atomic masses. For each temperature T from 10 K to 700 K (step 10 K), compute the classical thermal-average curvature ⟨φ(T)⟩ by numerically evaluating the double integrals of ∂²W/∂r² * exp(-W/kT) and the partition function Z over x and y, with an integration domain large enough to capture the relevant region. Derive ω²(T) = ⟨φ(T)⟩/μ and the wavenumber ν̃(T) = ω(T)/(2πc) in cm⁻¹. Output a CSV table with columns T_K and frequency_cm-1 for all temperatures.
- Output file: `/app/outputs/step_01_freq_table.csv`
- Format: csv
- Contract: Two columns: T_K (float, temperature in kelvin) and frequency_cm-1 (float, frequency in cm^{-1}). Rows ordered by increasing T_K from 10 K to 700 K in steps of 10 K. No header row? Actually CSV should include header. We'll specify: Header: T_K,frequency_cm-1. Each row corresponds to one temperature.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_freq_table.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_freq_table.csv
- path: `/app/outputs/step_01_freq_table.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Computed temperature-dependent frequency of the low-frequency TO mode from the anharmonic effective potential model, used to verify agreement with the experimental curve within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `T_K`, `frequency_cm-1`
  - `units`:
    - `T_K`: K
    - `frequency_cm-1`: cm^{-1}

Notes: Scoring uses a hidden gold curve digitized from the paper's Fig. 4. The checker computes the mean absolute error (MAE) between the agent's frequencies and the gold values at a set of reference temperatures. Full credit for MAE < 3 cm⁻¹ with linear decay to zero at MAE ≥ 10 cm⁻¹, and additionally verifies qualitative features (low-temperature decrease and slope change near 200 K) using structural_audit rules. The exact gold values and tolerance parameters are hidden.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_freq_table.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "T_K",
          "frequency_cm-1"
        ],
        "units": {
          "T_K": "K",
          "frequency_cm-1": "cm^{-1}"
        }
      },
      "description": "Computed temperature-dependent frequency of the low-frequency TO mode from the anharmonic effective potential model, used to verify agreement with the experimental curve within tolerance."
    }
  ],
  "notes": "Scoring uses a hidden gold curve digitized from the paper's Fig. 4. The checker computes the mean absolute error (MAE) between the agent's frequencies and the gold values at a set of reference temperatures. Full credit for MAE < 3 cm⁻¹ with linear decay to zero at MAE ≥ 10 cm⁻¹, and additionally verifies qualitative features (low-temperature decrease and slope change near 200 K) using structural_audit rules. The exact gold values and tolerance parameters are hidden."
}
```

## How you are scored
The hidden verifier reads your `step_01_freq_table.csv` and extracts the frequencies at a set of reference temperatures. It computes the mean absolute error (MAE) between your values and hidden reference values. Scoring uses a threshold-or-better policy: full credit is awarded if the MAE is below a predefined tight threshold, and credit decays linearly to zero as the MAE reaches a larger threshold. Additionally, the verifier performs structural checks to confirm the low-temperature softening and the slope change around 200 K. The final reward is a weighted combination of the MAE score and the structural checks, with the MAE score carrying the majority of the weight.

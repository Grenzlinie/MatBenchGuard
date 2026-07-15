# Ge lattice thermal conductivity correction term ΔK computation

## Problem background
In insulating crystals, lattice thermal conductivity is governed by phonon scattering. The generalised Callaway integral describes heat transport by two-mode conduction of transverse and longitudinal phonons. The integral includes a correction term ΔK that arises solely from three-phonon normal (N) processes. At very low temperatures, where boundary scattering dominates over all other resistive processes, ΔK can be expressed in closed analytical form. Understanding the magnitude and temperature dependence of ΔK in this regime is important because it determines whether the correction term can safely be neglected in thermal conductivity calculations. This task computes ΔK for germanium (Ge) in the boundary-scattering-dominated range 1–5 K, using the analytical expression derived from the Callaway framework, and reports the results as a quantitative table.

## Approach
The approach exploits the generalised Callaway integral under the condition where the boundary scattering rate dominates over all other resistive scattering rates, so that the combined scattering rate reduces essentially to the boundary rate. Under this simplification, the correction term ΔK can be written as an algebraic combination of Debye integrals \(I_n = \int_0^{\theta_i/T} x^n e^x (e^x-1)^{-2} \, dx\) and dispersion-dependent coefficients \(X\) and \(Y\) that involve the material's dispersion constants \(R_1\) and \(R_3\). The final expression for ΔK is

\[\Delta K = C \, \frac{\bigl(2 N_1 / v_{T1}^3 + N_2 / v_{L1}^3\bigr)^2}{2 N_3 / v_{T1}^5 + N_4 / v_{L1}^5}\]

where \(C = (k_B/(6\pi^2))(k_B T/\hbar)^3\), \(v_{T1}\) and \(v_{L1}\) are the transverse and longitudinal phonon velocities of the low-frequency branches, and the coefficients \(N_1, N_2, N_3, N_4\) are expressed in terms of the Debye integrals \(I_n\) and the normal- and Umklapp-scattering strengths \(b_1', b_2', b_3', b_4'\) together with the boundary and point-defect parameters. These scattering strengths are derived from the temperature-independent scattering coefficients \(B_1, B_2, B_3, B_4\) provided below, evaluated at the temperature of interest.

To carry out the computation, the following material constants for germanium are taken from Holland (1963) and Sharma et al. (1971):

  - Transverse velocity \(v_{T1} = 3.67 \times 10^5\) cm s⁻¹
  - Longitudinal velocity \(v_{L1} = 5.37 \times 10^5\) cm s⁻¹
  - Debye temperature \(\theta_D = 348\) K
  - Boundary scattering relaxation time \(\tau_B = L / v_{T1}\) with crystal length \(L = 0.3\) cm, giving \(\tau_B \approx 8.2 \times 10^{-7}\) s
  - Point-defect scattering strength \(A = 2.4 \times 10^{-45}\) s³
  - Zone-boundary temperatures for the low-frequency branches: \(\theta_1 = 120\) K (transverse) and \(\theta_2 = 120\) K (longitudinal)
  - Dispersion constants: \(R_1 = 0.02\), \(R_3 = 0.015\)
  - Three-phonon scattering strength coefficients (all in s K⁻⁴):
      * normal transverse \(B_1 = 2.8 \times 10^{-23}\)
      * Umklapp transverse \(B_2 = 2.0 \times 10^{-23}\)
      * normal longitudinal \(B_3 = 2.2 \times 10^{-23}\)
      * Umklapp longitudinal \(B_4 = 1.8 \times 10^{-23}\)

From these constants, evaluate the temperature-dependent quantities \(b_r = B_r\, (k_B T/\hbar)\, T^4\) (for \(r=1,2,3,4\)), \(D = A\, (k_B T/\hbar)^4\), and \(c_B = \tau_B\). Then compute \(b_r' = b_r c_B\) and \(D_1 = D c_B\). For each temperature, numerically evaluate the required Debye integrals \(I_n\) for \(n = 5,6,7,8,9,10,11,12,13,14,15\) using the appropriate upper limits (\(\theta_1/T\) for transverse and \(\theta_2/T\) for longitudinal) and assemble the coefficients \(N_1,N_2,N_3,N_4\) following the standard algebraic forms (which involve terms like \(I_5\), \(I_6\), ratios \(F_n^m = I_m/I_n\), and the dispersion functions \(X_n^m(R) = 1 + 3R F_n^m + 3R^2 F_n^{m+2} + R^3 F_n^{m+4}\) and \(Y_n^m(R) = 1 + 7R F_n^m + 18R^2 F_n^{m+2} + 22R^3 F_n^{m+4} + 7R^4 F_n^{m+6} + 3R^5 F_n^{m+8}\)). Finally, substitute into the expression for ΔK to obtain the correction term at that temperature. Numerical integration can be performed, for example, with `scipy.integrate.quad`.

## Reproduction target
Compute the correction term ΔK (in W cm⁻¹ K⁻¹) for germanium at the nine temperatures \(T = 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0\) K using the analytical expression and the Ge material constants listed above. Produce a CSV file containing exactly nine rows, one per temperature in increasing order, with columns 'Temperature (K)' and 'DeltaK (W/cm/K)'. The DeltaK values should be reported in scientific notation as floating-point numbers.

## Assets

- scipy: scipy
- Holland (1963) Ge material parameters: 10.1103/PhysRev.132.2461
- Sharma et al. (1971) Ge dispersion constants: 10.1103/PhysRevB.3.1985

## Workflow steps

### Step 1: Compute correction term ΔK for Ge at 1–5 K
- Role: scored (load-bearing)
- Action: Implement the analytical expression for the correction term ΔK (derived from the generalized Callaway integral under low-temperature boundary-scattering-dominated conditions) to compute the nine numerical values for Ge using the supplied material constants. This involves numerical integration of the Debye integrals I_n and assembly of the N1–N4 coefficients. Write the (Temperature, ΔK) pairs for T = 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0 K to delta_K_results.csv.
- Output file: `/app/outputs/delta_K_results.csv`
- Format: csv
- Contract: CSV with header 'Temperature (K),DeltaK (W/cm/K)'. Nine rows in increasing order of temperature. Temperature as float, DeltaK in scientific notation (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/delta_K_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### delta_K_results.csv
- path: `/app/outputs/delta_K_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Correction term ΔK for Ge at nine specified temperatures (1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0 K).
- schema:
  - `type`: table
  - `required_columns`: `Temperature (K)`, `DeltaK (W/cm/K)`
  - `units`:
    - `DeltaK (W/cm/K)`: Watt per degree Celsius per centimeter

Notes: The output CSV must contain exactly nine rows corresponding to the nine temperature points. The checker compares ΔK values to the paper's reported Table 1 using appropriate tolerances (not disclosed here).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "delta_K_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Temperature (K)",
          "DeltaK (W/cm/K)"
        ],
        "units": {
          "DeltaK (W/cm/K)": "Watt per degree Celsius per centimeter"
        }
      },
      "description": "Correction term ΔK for Ge at nine specified temperatures (1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0 K)."
    }
  ],
  "notes": "The output CSV must contain exactly nine rows corresponding to the nine temperature points. The checker compares ΔK values to the paper's reported Table 1 using appropriate tolerances (not disclosed here)."
}
```

## How you are scored
A hidden verifier independently reads your `delta_K_results.csv` and compares each ΔK value to a reference value (the physically correct result for the given constants). The comparison uses domain-appropriate tolerances that account for numerical integration choices; the tolerances are not disclosed. Correctness is assessed point by point: for each of the nine temperature points that matches the reference within tolerance you earn a share of the score. The final reward is the fraction of points matched correctly (each point carries equal weight). The verifier also checks that the output file follows the specified format header and row count; format violations may result in a reduced score. The task is graded on the accuracy of your computed ΔK values alone; auxiliary outputs are not scored.

# Lattice thermal conductivity of p-HgTe using SDV model

## Problem background
The lattice thermal conductivity of crystalline semiconductors is governed by phonon transport. In p-type mercury telluride (p‑HgTe), three‑phonon scattering processes dominate the phonon relaxation, and a detailed understanding requires separating the contributions of transverse and longitudinal acoustic phonon branches. The Sharma–Dubey–Verma (SDV) model provides a framework in which the three‑phonon scattering rates depend on a temperature‑dependent exponent m(T), with different classes of scattering events for transverse (class I) and longitudinal (class I and class II) phonons. The objective is to compute the total lattice thermal conductivity of p‑HgTe and its transverse/longitudinal components across the temperature range 2–300 K using the SDV model with literature‑derived material parameters.

## Approach
The SDV model expresses the three‑phonon relaxation rates for transverse and longitudinal phonons through formulas that involve temperature‑dependent exponents m_T1(T), m_L1(T), and m_L2(T) and the Debye temperature Θ = 141 K with α = 1. These exponents are computed from the dimensionless frequency parameters x_max,i = Θ_i/T, where Θ_i are the temperature equivalents of the maximum phonon frequencies obtained from dispersion curves. The true m(T) values are given by m_true(T) = x_max/(e^x_max − 1) + 0.5 x_max + ln(1 + Θ/αT)/ln T (with appropriate variations for each phonon class). With the m(T) values in hand, the lattice thermal conductivity is obtained by numerically integrating the Debye‑model integrals over the distinct frequency intervals for low‑ and high‑frequency transverse and longitudinal branches. Each integral accounts for boundary scattering (rate τ_B⁻¹ = 6.17×10⁵ s⁻¹), point‑defect scattering (parameter A_pt = 57×10⁻⁴⁴ s³), and the corresponding three‑phonon relaxation rate, with prefactors B_T = 3.82×10⁻⁵ K⁻ᵐ, B_L1 = 7.5×10⁻²² s·K⁻ᵐ, B_L2 = 5×10⁻¹⁸ s·K⁻ᵐ. The group velocities for the four frequency regions (V_T1, V_T2, V_L1, V_L2) and the frequency boundaries Θ₁=57 K, Θ₂=95 K, Θ₃=145 K, Θ₄=100 K are taken from the literature. The total conductivity is the sum of the transverse (K_T) and longitudinal (K_L) contributions. The computation proceeds in two steps: first, evaluate m(T) at a set of temperature points; second, perform the numerical integrations to obtain K_T, K_L, and K_total at the prescribed temperatures.

## Reproduction target
Produce a CSV file containing the lattice thermal conductivity of p‑HgTe as computed by the SDV model for temperatures from 2 K to 300 K. The file must include columns: T (temperature in K), K_total (total thermal conductivity, W m⁻¹ K⁻¹), K_transverse (transverse phonon contribution, W m⁻¹ K⁻¹), and K_longitudinal (longitudinal phonon contribution, W m⁻¹ K⁻¹). Values are required for at least the following temperatures: 2, 5, 10, 15, 20, 30, 40, 50, 60, 80, 100, 150, 200, 250, 300 K.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Compute temperature-dependent exponent m(T)
- Role: process
- Action: Using the Debye temperature Θ=141 K, α=1, and the phonon maximum frequency temperatures Θ2=95 K (transverse) and Θ3=145 K (longitudinal), compute the true m(T) values for transverse class I, longitudinal class I, and longitudinal class II according to the SDV model formulas. Compute m_T1, m_L1, m_L2 at temperatures T = 10, 20, 30, 40, 60, 80, 100, 150, 200, 300 K. Output the results to mT_values.csv.
- Evidence: `/app/outputs/mT_values.csv`

### Step 2: Compute lattice thermal conductivity
- Role: scored (load-bearing)
- Action: Using the m(T) values from the previous step and the parameters: Debye temperature Θ=141 K, frequency boundaries Θ1=57 K, Θ2=95 K, Θ3=145 K, Θ4=100 K, group velocities V_T1=1.98e5 cm/s, V_T2=1.32e5 cm/s, V_L1=4.07e5 cm/s, V_L2=1.97e5 cm/s, boundary scattering rate τ_B^{-1}=6.17e5 s^{-1}, point-defect scattering parameter A_pt=57e-44 s^3, three-phonon prefactors B_T=3.82e-5 K^{-m}, B_L1=7.5e-22 s·K^{-m}, B_L2=5e-18 s·K^{-m}, α=1, compute the transverse (K_T) and longitudinal (K_L) lattice thermal conductivity integrals according to the SDV model. Numerically integrate over the appropriate frequency ranges for each branch at temperatures from 2 to 300 K (including at least: 2,5,10,15,20,30,40,50,60,80,100,150,200,250,300 K). Compute total conductivity K_total = K_T + K_L. Write the results to thermal_conductivity.csv.
- Output file: `/app/outputs/thermal_conductivity.csv`
- Format: csv
- Contract: Columns: T (float, K), K_total (float, W/(m·K)), K_transverse (float, W/(m·K)), K_longitudinal (float, W/(m·K)).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermal_conductivity.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermal_conductivity.csv
- path: `/app/outputs/thermal_conductivity.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: The file containing the computed lattice thermal conductivity as a function of temperature, produced by the SDV model. The checker will compare the values to hidden reference data digitized from the paper's Fig. 1 and verify the reported trends of transverse vs. longitudinal contributions.
- schema:
  - `type`: table
  - `required_columns`: `T`, `K_total`, `K_transverse`, `K_longitudinal`
  - `units`:
    - `T`: K
    - `K_total`: W/(m·K)
    - `K_transverse`: W/(m·K)
    - `K_longitudinal`: W/(m·K)

Notes: The hidden checker will compute relative errors at specified temperature points and check that K_transverse > K_longitudinal above 80 K and below 10 K, and K_longitudinal > K_transverse between 10 K and 80 K, in addition to numerical accuracy.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermal_conductivity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "K_total",
          "K_transverse",
          "K_longitudinal"
        ],
        "units": {
          "T": "K",
          "K_total": "W/(m·K)",
          "K_transverse": "W/(m·K)",
          "K_longitudinal": "W/(m·K)"
        }
      },
      "description": "The file containing the computed lattice thermal conductivity as a function of temperature, produced by the SDV model. The checker will compare the values to hidden reference data digitized from the paper's Fig. 1 and verify the reported trends of transverse vs. longitudinal contributions."
    }
  ],
  "notes": "The hidden checker will compute relative errors at specified temperature points and check that K_transverse > K_longitudinal above 80 K and below 10 K, and K_longitudinal > K_transverse between 10 K and 80 K, in addition to numerical accuracy."
}
```

## How you are scored
A hidden verifier reads your `thermal_conductivity.csv` and independently evaluates the submitted conductivity values. At a pre‑specified set of temperatures it compares your computed K_total, K_transverse, and K_longitudinal against reference values derived from the original study, awarding a numerical accuracy score. In addition, the verifier checks whether the relative magnitudes of K_transverse and K_longitudinal across the full temperature range agree with the physical trends expected from the SDV model. The final score is a weighted combination of these checks, with the numerical accuracy carrying the majority of the weight.

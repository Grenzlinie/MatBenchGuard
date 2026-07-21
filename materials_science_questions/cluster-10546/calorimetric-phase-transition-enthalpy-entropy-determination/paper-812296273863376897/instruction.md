# Compute Ideal‑Gas Thermodynamic Functions via Statistical Mechanics

## Problem background
Statistical mechanics connects molecular structure and spectroscopic data to macroscopic thermodynamic behavior. For a molecule in the ideal-gas state, the thermodynamic functions – the free-energy function (F°–H0°)/T, the heat-content function (H°–H0°)/T, the heat content H°–H0°, the entropy S°, and the heat capacity at constant pressure C_p° – can be derived from the molecular partition function. The partition function depends on the principal moments of inertia, the set of vibrational frequencies, the potential energy barrier hindering internal rotations, and corrections for vibrational anharmonicity. Computing these functions for 2,3-dimethyl-2-butene tests whether a simple rigid-rotor harmonic-oscillator model, supplemented by a treatment of methyl internal rotation and an empirical anharmonicity correction, can reproduce the thermodynamic properties expected from calorimetric experiments.

## Approach
The ideal-gas thermodynamic functions are obtained from the molecular partition function Q evaluated at each temperature. The translational contribution follows from the standard ideal-gas formula. The rotational contribution uses the rigid-rotor model with the given principal moments of inertia and overall symmetry number. The vibrational contribution treats each assigned normal mode as an independent harmonic oscillator. The hindered internal rotations of the methyl groups are handled by the Pitzer–Gwinn approximation, implemented here by numerical solution of the Mathieu equation to obtain the exact energy levels for a threefold barrier. An empirical anharmonicity correction, parameterized by a temperature-independent constant Z (cal/K/mol) and a characteristic frequency ν (cm⁻¹), is then added to the harmonic vibrational contribution. Standard thermodynamic relations are used to compute (F°–H0°)/T, (H°–H0°)/T, H°–H0°, S°, and C_p° from Q and its temperature derivatives. The calculation must be carried out at the 15 temperatures listed in the reproduction target, using the molecular constants and vibrational frequency set provided below.

## Reproduction target
Using the vibrational frequencies, barrier height, and anharmonicity parameters derived in the preceding process steps, and the principal moments of inertia, product, symmetry number, and reduced moment for methyl internal rotation computed from molecular geometry in Step 1, compute the five ideal-gas thermodynamic functions at the following temperatures (K): 273.16, 298.16, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500. Write the results to the CSV file /app/outputs/thermodynamic_functions.csv with columns: T (K), F_minus_H0_over_T (cal/K/mol), H_minus_H0_over_T (cal/K/mol), H_minus_H0 (kcal/mol), S (cal/K/mol), and Cp (cal/K/mol).

## Assets

- numpy: numpy
- scipy: scipy

## Input data

### Physical constants and standard state
These constants were used in the original 1955 computations (1951 values):
- Gas constant R = 1.9872 cal K⁻¹ mol⁻¹ (equivalent to 8.3144 × 10⁷ erg K⁻¹ mol⁻¹)
- Boltzmann constant k_B = 1.3805 × 10⁻¹⁶ erg K⁻¹
- Avogadro number N_A = 6.0228 × 10²³ mol⁻¹
- Planck constant h = 6.6256 × 10⁻²⁷ erg s (already given below)
- Speed of light c = 2.9979 × 10¹⁰ cm s⁻¹
- Standard state: ideal gas at pressure P = 1 atm = 1.01325 × 10⁶ dyn cm⁻² (the thermodynamic functions in Table X refer to this pressure).
The combination hc/k_B = 1.4388 cm·K is used for the vibrational temperature scale.

### Atomic masses
Use the 1951 International Atomic Weights:
- C : 12.010 amu
- H : 1.008 amu
1 amu = 1.66042 × 10⁻²⁴ g.

### Molecular geometry and computed normal-mode frequencies
The molecule is treated as having a planar carbon skeleton with V_h symmetry. The bond distances are: C=C 1.353 Å, C-C 1.54 Å, C-H 1.09 Å. Bond angles: C-C-C 120°, C-C-H and H-C-H 109°28'. The force constants from Kilpatrick and Pitzer (J. Research Natl. Bur. Standards 38, 191 (1947)) were used to compute harmonic vibrational frequencies (in cm⁻¹) by the GF matrix method. The computed frequencies for each symmetry class and approximate mode description are given below; use these together with the observed spectral lines (next section) to assign the fundamentals.

| Class | Mode description | Calcd. (cm⁻¹) |
|-------|------------------|----------------|
| A_g | C=C stretch | 1734 |
| A_g | CH₃ rock | 976 |
| A_g | C-C stretch | 661 |
| A_g | Skeletal bend | 298 |
| A_u | CH₃ rock | 990 or 992^a |
| A_u | Skeletal twist | 183 or 222^a |
| B_{1g} | C-C stretch | 1482 |
| B_{1g} | CH₃ rock | 974 |
| B_{1g} | Skeletal bend | 473 |
| B_{2g} | CH₃ rock | 1074 |
| B_{2g} | Skeletal bend | 483 |
| B_{3g} | CH₃ rock | 987 |
| B_{1u} | CH₃ rock | 1055 |
| B_{1u} | Skeletal bend | 276 |
| B_{2u} | C-C stretch | 1241 |
| B_{2u} | CH₃ rock | 976 |
| B_{2u} | Skeletal bend | 214 |
| B_{3u} | CH₃ rock | 1128 |
| B_{3u} | C-C stretch | 868 |
| B_{3u} | Skeletal bend | 405 |

^a Depending on assumption about the skeletal twisting force constant; treat both possibilities and use consistency with observed lines to decide.

### Observed spectral lines
Raman (liquid) and infrared (liquid) frequencies below 1700 cm⁻¹ are listed in the table below. Use these to identify the observed fundamental frequencies for each mode.

| Raman Δν (cm⁻¹) | Intensity | Raman ρ | Infrared ν (cm⁻¹) | Infrared Intensity |
|------------------|-----------|---------|-------------------|-------------------|
| 257 | vvvw | | | |
| 269 | vvvw | | 272 | m |
| | | | 315 | s |
| 411 | 3.1 | 0.50 | | |
| | | | 420 | m |
| 503 | 4.0 | 0.92 | ≈499 | m |
| 559 | vvvw | | | |
| | | | 565 | w |
| 691 | 8.2 | 0.15 | | |
| | | | 818 | w |
| | | | ≈870 | vw |
| | | | ≈890 | vw |
| 944 | 0.2 | 0.52 | | |
| | | | 971 | m |
| 1028 | 0.7 | 0.79 | | |
| | | | 1065 | w |
| 1072 | 0.8 | 0.68 | | |
| 1113 | vvvw | | | |
| 1132 | vvvw | | | |
| | | | 1152 | m sh |
| | | | 1163 | s |
| 1190 | vvvw | | | |
| | | | ≈1210 | vw |
| 1221 | 0.1 | | | |
| 1269 | 0.2 | 0.78 | | |
| 1324 | vvvw | | | |
| | | | 1363 | s |
| 1371 | 0.8 | 0.74 | | |
| 1392 | 3.2 | 0.28 | | |
| | | | 1440 | s |
| 1454 | 3.3 | 0.79 | | |
| | | | 1560 | w |
| 1652 | 0.1 | 0.85 | | |
| | | | 1657 | w sh |
| 1674 | 6.7 | 0.24 | | |

Additionally, the methyl bending and C-H stretching region contains broad bands; average frequencies of 1375 (4), 1450 (8), and 2950 (12) cm⁻¹ are used for those groups.

### Calorimetric data for barrier fitting
The experimental gas-phase entropy at 298.16 K is S° = 87.16 cal/K/mol (derived from thermal measurements). The ideal-gas heat capacities C_p° measured at five temperatures are:
- 334.20 K : C_p° = 32.34 cal/K/mol
- 355.25 K : 33.94
- 393.20 K : 36.96
- 433.20 K : 40.07
- 473.20 K : 43.10

Use these data to optimize the barrier height V₃ (cal/mol) for the threefold methyl internal rotation and the anharmonicity constants Z (cal/K/mol) and ν (cm⁻¹). Start from a reasonable initial guess (e.g., V₃ ≈ 700, Z=1.0, ν=1200) and fit the model to minimize the sum of squared deviations between calculated and observed S° and C_p° values, weighted appropriately.

### Treatment of internal rotation (Pitzer–Gwinn via Mathieu equation)
For each methyl group, the Hamiltonian for internal rotation is

\[
H = -F \frac{d^2}{d\phi^2} + \frac{1}{2} V_3 (1 - \cos 3\phi),
\qquad
F = \frac{h^2}{2 I_{\text{red}}}
\]

where \(h = 6.6256\times10^{-27}\) erg·s, \(I_{\text{red}}\) is the reduced moment (g·cm²) computed in Step 1, and \(V_3\) (erg) is the barrier height. Solutions are Mathieu functions; the characteristic values \(\lambda_n^{(\sigma)}\) (even \(\sigma=+\) from `scipy.special.mathieu_a`, odd \(\sigma=-\) from `scipy.special.mathieu_b`) are obtained with parameter \(q = V_3/(4F)\). The energy levels are

\[
E_n^{(\sigma)} = F \lambda_n^{(\sigma)} \quad (\text{erg}).
\]

The partition function for one rotor is \(q_{\text{int}} = \sum_{n,\sigma} \exp(-E_n^{(\sigma)}/k_{\text{B}}T)\). Sum over all methyl rotors to get the total internal-rotation contribution. Compute thermodynamic properties by numerical differentiation of \(\ln q_{\text{int}}\) with respect to \(T\):

\[
\frac{H^{\circ}-H_0^{\circ}}{T} = R \frac{\partial \ln q_{\text{int}}}{\partial \ln T},\quad
S^{\circ} = R\left( \ln q_{\text{int}} + \frac{\partial \ln q_{\text{int}}}{\partial \ln T} \right),\quad
C_p^{\circ} = R \frac{\partial^2 (T\ln q_{\text{int}})}{\partial T^2},
\]
\[
\frac{F^{\circ}-H_0^{\circ}}{T} = -R \ln q_{\text{int}}.
\]

Carry out the sums over enough levels until convergence (e.g., retain levels up to several times \(k_{\text{B}}T\)).

### Empirical anharmonicity correction
The anharmonic correction to the harmonic vibrational contribution is added using the parameters \(Z\) (cal/K/mol) and \(\nu\) (cm⁻¹). Define

\[
u = \frac{h c \nu}{k_{\text{B}} T} = \frac{1.4388\,\nu}{T} \quad (\text{dimensionless}),
\]

where \(h c / k_{\text{B}} = 1.4388\) cm·K. The corrections to the thermodynamic functions are

\[
\Delta \left( \frac{F^{\circ}-H_0^{\circ}}{T} \right) = -Z \ln(1 - e^{-u}),
\]
\[
\Delta \left( \frac{H^{\circ}-H_0^{\circ}}{T} \right) = Z \frac{u}{e^{u} - 1},
\]
\[
\Delta (H^{\circ}-H_0^{\circ}) = Z\,T \frac{u}{e^{u} - 1},
\]
\[
\Delta S^{\circ} = Z \left[ \frac{u}{e^{u} - 1} - \ln(1 - e^{-u}) \right],
\]
\[
\Delta C_p^{\circ} = Z \frac{u^{2} e^{u}}{(e^{u} - 1)^{2}}.
\]

These are the formulae for an Einstein oscillator contribution scaled by the empirical constant \(Z\). Apply them to the total harmonic-oscillator results (sum over all normal modes) **before** adding the internal-rotation contributions.

## Workflow steps

### Step 1: Compute molecular moments of inertia and reduced moment for methyl rotation
- Role: process
- Action: From the molecular geometry (bond lengths: C=C 1.353 Å, C-C 1.54 Å, C-H 1.09 Å; bond angles: C-C-C 120°, C-C-H and H-C-H 109°28'), construct atomic coordinates for a planar carbon skeleton with V_h symmetry. Compute the center‑of‑mass moments of inertia tensor, diagonalize to obtain the three principal moments Ia, Ib, Ic (in g·cm²), and compute their product. The overall rotational symmetry number is σ=4. For each methyl group, estimate the reduced moment I_red for internal rotation as follows. The methyl rotor about its symmetry axis has a moment of inertia I_α ≈ 5.3×10⁻⁴⁰ g·cm². The moment of inertia of the remainder of the molecule projected onto the rotation axis, I_t, is computed by constructing the inertia tensor of the whole molecule EXCLUDING the methyl group in question, expressing this tensor in the coordinate system where the methyl C₃ axis is the z-axis, and taking the zz-component. Then I_red = I_α I_t / (I_α + I_t). If the four methyl groups are not all identical by symmetry, average their I_red values to obtain a single effective reduced moment. Write all computed constants to `/app/outputs/moments.json` as a JSON object with keys: Ia, Ib, Ic, product_IA, symmetry_number, I_red.
- Evidence: `/app/outputs/moments.json`

### Step 2: Assign vibrational fundamentals
- Role: process
- Action: Using the computed normal-mode frequencies (table above) and the observed Raman and infrared spectral lines, assign each fundamental according to symmetry and approximate frequency. For each symmetry class, match the observed line closest to the calculated frequency, respecting selection rules (A_g: Raman p, B_{1g}, B_{2g}, B_{3g}: Raman d; B_{1u}, B_{2u}, B_{3u}: infrared; A_u: inactive). The 503 cm⁻¹ Raman band is used for both B_{1g} and B_{2g} skeletal bends. The B_{3g} methyl rock is not directly observed but must be placed at 961 cm⁻¹ based on combination bands. The A_u methyl rock is taken as 990 cm⁻¹ and the A_u skeletal twist as 165 cm⁻¹, consistent with the calorimetric evidence. Average frequencies for the methyl bending modes (1375 cm⁻¹ ×4, 1450 cm⁻¹ ×8) and C-H stretches (2950 cm⁻¹ ×12) are used directly. Write the assigned fundamental frequencies (one frequency per mode, listing all 36 frequencies) to `/app/outputs/assigned_frequencies.csv` (two columns: mode, frequency_cm1).
- Evidence: `/app/outputs/assigned_frequencies.csv`

### Step 3: Fit internal-rotation barrier and anharmonicity
- Role: process
- Action: Using the assigned vibrational frequencies from Step 2 and the molecular constants (principal moments of inertia, product, symmetry number, reduced moment I_red) computed in Step 1, compute the harmonic thermodynamic functions. Implement the Pitzer–Gwinn approximation for hindered methyl rotation (barrier height V₃) via Mathieu‑equation level summation as described in Input Data. Also implement the empirical anharmonicity correction (Z, ν) with the explicit formulas given in Input Data. Vary V₃, Z, and ν to minimize the sum of squared residuals between the calculated and observed S° at 298.16 K and C_p° at the five temperatures given in the Input Data section. The fitting may use a simple grid search or an optimizer (e.g., scipy.optimize). The objective is to reproduce the calorimetric data as closely as possible. Write the optimized parameters to `/app/outputs/barrier_params.json` as a JSON object with keys: V3 (cal/mol), Z (cal/K/mol), nu (cm⁻¹).
- Evidence: `/app/outputs/barrier_params.json`

### Step 4: Calculate thermodynamic functions
- Role: scored (load-bearing)
- Action: Using the assigned vibrational fundamentals from Step 2, the barrier height and anharmonicity constants from Step 3, and the molecular moments of inertia, symmetry number, and reduced moment computed in Step 1, compute the ideal‑gas thermodynamic functions (F°‑H0°)/T, (H°‑H0°)/T, H°‑H0°, S°, and Cp° at the 15 temperatures (273.16, 298.16, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500 K) via standard statistical‑mechanics formulas: rigid‑rotor harmonic‑oscillator partition function, Pitzer‑Gwinn approximation for internal rotation (Mathieu summation), and the empirical anharmonicity correction as detailed in Input Data. Write the results to thermodynamic_functions.csv.
- Output file: `/app/outputs/thermodynamic_functions.csv`
- Format: csv
- Contract: CSV with columns: T (K), F_minus_H0_over_T (cal/K/mol), H_minus_H0_over_T (cal/K/mol), H_minus_H0 (kcal/mol), S (cal/K/mol), Cp (cal/K/mol).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/moments.json` (process evidence)
- `/app/outputs/assigned_frequencies.csv` (process evidence)
- `/app/outputs/barrier_params.json` (process evidence)
- `/app/outputs/thermodynamic_functions.csv` (scored)

## Output contract

Every file listed below is used either for scoring or as process evidence. Write each file under `/app/outputs` and follow its schema exactly.

### thermodynamic_functions.csv
- path: `/app/outputs/thermodynamic_functions.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed ideal‑gas thermodynamic functions at the 15 specified temperatures, to be compared against reference values.
- schema:
  - `type`: table
  - `required_columns`: `T`, `F_minus_H0_over_T`, `H_minus_H0_over_T`, `H_minus_H0`, `S`, `Cp`
  - `units`:
    - `T`: K
    - `F_minus_H0_over_T`: cal/K/mol
    - `H_minus_H0_over_T`: cal/K/mol
    - `H_minus_H0`: kcal/mol
    - `S`: cal/K/mol
    - `Cp`: cal/K/mol

### moments.json
- path: `/app/outputs/moments.json`
- format: json
- purpose: process
- description: Principal moments of inertia, symmetry number, and reduced moment for methyl rotation.
- schema:
  - `required`: `Ia`, `Ib`, `Ic`, `product_IA`, `symmetry_number`, `I_red`

### assigned_frequencies.csv
- path: `/app/outputs/assigned_frequencies.csv`
- format: csv
- purpose: process
- description: Assigned fundamental frequencies (one per mode).
- schema:
  - `required_columns`: `mode`, `frequency_cm1`

### barrier_params.json
- path: `/app/outputs/barrier_params.json`
- format: json
- purpose: process
- description: Optimized barrier height and anharmonicity parameters.
- schema:
  - `required`: `V3`, `Z`, `nu`

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermodynamic_functions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "F_minus_H0_over_T",
          "H_minus_H0_over_T",
          "H_minus_H0",
          "S",
          "Cp"
        ],
        "units": {
          "T": "K",
          "F_minus_H0_over_T": "cal/K/mol",
          "H_minus_H0_over_T": "cal/K/mol",
          "H_minus_H0": "kcal/mol",
          "S": "cal/K/mol",
          "Cp": "cal/K/mol"
        }
      },
      "description": "Computed ideal‑gas thermodynamic functions at the 15 specified temperatures, to be compared against reference values."
    },
    {
      "file": "moments.json",
      "format": "json",
      "purpose": "process",
      "schema": {
        "required": [
          "Ia",
          "Ib",
          "Ic",
          "product_IA",
          "symmetry_number",
          "I_red"
        ]
      },
      "description": "Principal moments of inertia, symmetry number, and reduced moment."
    },
    {
      "file": "assigned_frequencies.csv",
      "format": "csv",
      "purpose": "process",
      "schema": {
        "required_columns": [
          "mode",
          "frequency_cm1"
        ]
      },
      "description": "Assigned fundamental frequencies."
    },
    {
      "file": "barrier_params.json",
      "format": "json",
      "purpose": "process",
      "schema": {
        "required": [
          "V3",
          "Z",
          "nu"
        ]
      },
      "description": "Optimized barrier height and anharmonicity parameters."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier reads your /app/outputs/thermodynamic_functions.csv and compares each reported value against a hidden reference set derived from the original experimental study. The reward is proportional to the fraction of (temperature, property) pairs that fall within a predetermined tolerance. The tolerance accounts for legitimate small numerical differences that arise from different implementations of the partition function and internal rotation treatment. You do not need to target any particular published table — aim for the most accurate result your implementation can achieve. The verifier will combine all scored stages (here a single stage) to produce a final reward between 0 and 1.
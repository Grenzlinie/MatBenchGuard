# Dielectric response and tunability of compositionally graded ferroelectric multilayers with thermal strain

## Problem background
Ferroelectric barium strontium titanate (BST) thin films and multilayers are promising for voltage‑tunable microwave devices. When a compositionally graded BST multilayer is deposited on a substrate and processed at elevated temperature, cooling to room temperature creates in-plane thermal strains because the thermal expansion coefficient (TEC) of the substrate differs from that of each BST layer. These strains, together with electrostatic coupling between layers, can dramatically alter the dielectric constant and tunability. The goal of this task is to compute the equilibrium polarization, small‑signal dielectric constant, and tunability (at 400 kV/cm) of a trilayer BST heterostructure (layers BST 60/40, 75/25, 90/10 of equal thickness) as a function of substrate TEC, annealing temperature, and for several specific substrates, using a thermodynamic model that incorporates thermal strain and electrostatic interactions. The outcomes will show how substrate choice and processing temperature influence the dielectric response.

## Model equations
This section provides the mathematical definitions required to implement the thermodynamic model. All symbols are defined below. The free energy of a single ferroelectric layer is expanded in powers of the out‑of‑plane polarization \(P\):

\[
F(P,T)=F_0 + \frac{1}{2} a P^2 + \frac{1}{4} b P^4 + \frac{1}{6} c P^6,
\]

where the dielectric stiffness coefficient \(a\) follows the Curie‑Weiss law

\[
a_i = \frac{T - T_{C,i}}{\varepsilon_0 C_i},
\]

with \(\varepsilon_0 = 8.854\,187\,817\times10^{-12}\ \mathrm{F\,m^{-1}}\).  
\(T_{C,i}\) and \(C_i\) are the Curie temperature and Curie constant of layer \(i\).

The in‑plane thermal strain that develops in layer \(i\) during cooling from a processing (annealing) temperature \(T_A\) to the device operation temperature \(T_f\) is

\[
x_i = \int_{T_A}^{T_f} \bigl(\lambda_S(T) - \lambda_i\bigr)\, dT,
\]

where \(\lambda_i\) is the (temperature‑independent) thermal expansion coefficient of layer \(i\) and \(\lambda_S(T)\) is the temperature‑dependent TEC of the substrate. If the substrate TEC is treated as constant the integral reduces to \(x_i = (\lambda_S - \lambda_i)(T_f - T_A)\).

Mechanical boundary conditions (equal in‑plane stress, traction‑free out‑of‑plane) renormalise the Landau coefficients:

\[
a_i' = a_i - x_i\,\frac{4\,Q_{12,i}}{s_{11,i}+s_{12,i}},
\qquad
b_i' = b_i + \frac{4\,Q_{12,i}^2}{s_{11,i}+s_{12,i}},
\]

where \(Q_{12,i}\) is the electrostrictive coefficient and \(s_{11,i}, s_{12,i}\) are the elastic compliances of layer \(i\). The combination \((s_{11,i}+s_{12,i})^{-1}\) is obtained from the elastic stiffness constants \(c_{11}, c_{12}\) via

\[
\frac{1}{s_{11,i}+s_{12,i}} = c_{11,i} + c_{12,i} - \frac{2\,c_{12,i}^2}{c_{11,i}}.
\]

For the multilayer stack with volume fractions \(\alpha_i = \ell_i / \sum_k \ell_k\) (here all layers have equal thickness, so \(\alpha_i = 1/n\)), the short‑circuit electrical boundary condition gives the depolarising field in layer \(i\):

\[
E_{D,i} = -\frac{1}{\varepsilon_0}\Bigl(P_i - \sum_{j=1}^{n} \alpha_j P_j\Bigr).
\]

The total free energy density of the multilayer is

\[
\begin{aligned}
F_\Sigma =& \sum_{i=1}^{n} \alpha_i\Bigl( F_{0,i} + \frac{1}{2} a_i' P_i^2 + \frac{1}{4} b_i' P_i^4 + \frac{1}{6} c_i P_i^6 - E^{\mathrm{ext}} P_i \Bigr) \\
          &- \frac{1}{2} \sum_{i=1}^{n} \alpha_i E_{D,i} P_i + \sum_{i=1}^{n} \alpha_i \frac{x_i^2}{s_{11,i}+s_{12,i}},
\end{aligned}
\]

where \(E^{\mathrm{ext}}\) is the applied external electric field (along the polarisation direction). Minimising \(F_\Sigma\) with respect to each \(P_i\) yields the equations of state \(\partial F_\Sigma / \partial P_i = 0\), which simplify to the following system of coupled nonlinear equations for \(i = 1 \dots n\):

\[
\alpha_i\left[ a_i P_i + b_i P_i^3 + c_i P_i^5 - \frac{4 Q_{12,i}}{s_{11,i}+s_{12,i}} P_i \bigl(x_i - Q_{12,i} P_i\bigr) + \frac{1}{\varepsilon_0}\Bigl(P_i - \sum_{j=1}^{n} \alpha_j P_j\Bigr) - E^{\mathrm{ext}} \right] = 0.
\tag{10}
\]

These equations are solved numerically for the equilibrium polarisations \(P_i\). The average polarisation across the stack is

\[
\langle P \rangle = \sum_{i=1}^{n} \alpha_i P_i.
\]

The small‑signal average dielectric constant is obtained from the numerical derivative of \(\langle P \rangle\) with respect to applied field:

\[
\langle\varepsilon\rangle \cong \frac{1}{\varepsilon_0} \frac{d\langle P \rangle}{dE}.
\]

Dielectric tunability at a given applied field \(E\) is defined as the percentage change relative to the zero‑field value:

\[
\eta = \frac{\langle\varepsilon\rangle(E=0) - \langle\varepsilon\rangle(E)}{\langle\varepsilon\rangle(E=0)} \times 100.
\]

## Reproduction target
Produce a CSV file `/app/outputs/results.csv` containing the average polarization (in C/m²), the zero‑field dielectric constant, and the dielectric tunability (in percent) at an applied field of 400 kV/cm for the trilayer BST (90/10, 75/25, 60/40) on the following conditions:

(a) **TEC sweeps** (`condition_type = TEC_sweep`): For annealing temperatures \(T_A = 550,\,650,\,750\) °C, compute the quantities at applied fields \(E = 0\) and \(E = 400\) kV/cm while varying the effective substrate TEC from \(5\times10^{-6}\) K⁻¹ to \(15\times10^{-6}\) K⁻¹ (with fine enough resolution to resolve the dielectric response). The substrate TEC is treated as temperature‑independent over the cooling range in these sweeps.

(b) **Specific substrates** (`condition_type = substrate_annealing`): For the substrates Si, MgO, SrTiO₃, and LaAlO₃, use their real temperature‑dependent TEC functions. Compute the same quantities at annealing temperatures \(T_A = 450\) °C and \(750\) °C, for \(E = 0\) and \(E = 400\) kV/cm.

(c) **Temperature dependence** (`condition_type = temperature_dependence`): For the Si and SrTiO₃ substrates, at an applied field \(E = 400\) kV/cm, compute the quantities over a temperature range from \(-10\) °C to \(90\) °C at intervals no larger than \(5\) °C.

The CSV must have the following columns:
- `condition_type`: one of `TEC_sweep`, `substrate_annealing`, `temperature_dependence`
- `substrate_TEC` (float, for TEC_sweep rows only, otherwise leave empty)
- `substrate_name` (string, for substrate_annealing and temperature_dependence rows, otherwise leave empty)
- `annealing_temperature_C` (float)
- `applied_field_kV_per_cm` (float)
- `quantity`: one of `avg_polarization_C_per_m2`, `dielectric_constant`, `tunability_percent`
- `value` (float)
Include a row for every combination of condition, temperature/field/quantity.

## Assets
- NumPy: https://pypi.org/project/numpy/
- SciPy: https://pypi.org/project/scipy/

## Material parameters

### Bulk BaTiO₃ and SrTiO₃ properties

| Parameter | BaTiO₃ | SrTiO₃ |
|-----------|--------|--------|
| Curie temperature \(T_C\) (°C) | 120 | –253 |
| Curie constant \(C\) (°C) | 1.7×10⁵ | 0.8×10⁵ |
| Dielectric stiffness \(b\) (N m⁶ C⁻⁴) | 1.44×(T−175)×10⁷ (T in °C) | 8.4×10⁹ (constant) |
| Dielectric stiffness \(c\) (N m¹⁰ C⁻⁶) | 3.96×10¹⁰ | 0 (not used) |
| Electrostrictive coefficient \(Q_{12}\) (m⁴ C⁻²) | –0.045 | –0.013 |
| Elastic constant \(c_{11}\) (N m⁻²) | 1.76×10¹¹ | 3.181×10¹¹ |
| Elastic constant \(c_{12}\) (N m⁻²) | 8.46×10¹⁰ | 1.025×10¹¹ |
| Thermal expansion coefficient \(\lambda\) (K⁻¹) | 10.6×10⁻⁶ | 8.75×10⁻⁶ |

The effective in‑plane elastic parameter is \((s_{11}+s_{12})^{-1} = c_{11}+c_{12} - 2c_{12}^2/c_{11}\).

### Substrate thermal expansion coefficient (TEC) expressions

(All expressions produce λ in K⁻¹; T in K unless noted)

- **MgO**:  
  λ = 12.92×10⁻⁶ × {1 – exp[–5.826×10⁻³ × (T – 65.23)]} + 2.067×10⁻³ × T × 10⁻⁶

- **SrTiO₃**: constant λ = 8.75×10⁻⁶ K⁻¹

- **Si**:  
  λ = 3.725×10⁻⁶ × {1 – exp[–5.88×10⁻³ × (T – 124)]} + 5.548×10⁻⁴ × T × 10⁻⁶

- **c‑Al₂O₃** (T in °C):  
  λ = (8.026 + 8.17×10⁻⁴ × T – 3.279 × exp(–2.91×10⁻³ × T)) × 10⁻⁶

- **a‑Al₂O₃** (T in °C):  
  λ = (7.419 + 6.43×10⁻⁴ × T – 3.211 × exp(–2.59×10⁻³ × T)) × 10⁻⁶

- **LaAlO₃**:  
  λ = (–9.493×10⁻¹⁷ × T⁶ + 4.909×10⁻¹³ × T⁵ – 1.015×10⁻⁹ × T⁴ + 1.068×10⁻⁶ × T³ – 6.054×10⁻⁴ × T² + 0.1823 × T – 14.52) × 10⁻⁶

## Workflow steps

### Step 1: Prepare substrate TEC functions
- Role: process
- Action: Implement temperature‑dependent thermal expansion coefficient (TEC) functions for the substrates listed above, and set the constant TEC for SrTiO₃.
- Evidence: none

### Step 2: Interpolate BST material parameters
- Role: process
- Action: For each BST layer composition (BST 60/40, 75/25, 90/10), determine thermodynamic parameters (\(T_C\), \(C\), \(b\), \(c\), \(Q_{12}\), \(s_{11}\), \(s_{12}\), \(\lambda\)) by linear interpolation between the bulk BaTiO₃ and SrTiO₃ values. Note that the \(b\) coefficient of BaTiO₃ is temperature‑dependent.
- Evidence: none

### Step 3: Compute thermal strain in each layer
- Role: process
- Action: For a given substrate and annealing temperature \(T_A\), compute the integrated in‑plane thermal strain \(x_i\) for each layer at final temperature \(T_f = 25\) °C using the integral \(\int_{T_A}^{T_f}(\lambda_S(T) - \lambda_i)\,dT\). When the substrate TEC is constant or the substrate is SrTiO₃, the integral simplifies to \((\lambda_S - \lambda_i)(T_f - T_A)\).
- Evidence: none

### Step 4: Renormalize Landau coefficients
- Role: process
- Action: Using the thermal strain \(x_i\) and the relation \((s_{11}+s_{12})^{-1} = c_{11}+c_{12} - 2c_{12}^2/c_{11}\), compute the renormalised coefficients

\[
a_i' = a_i - x_i\frac{4\,Q_{12,i}}{s_{11,i}+s_{12,i}},\qquad
b_i' = b_i + \frac{4\,Q_{12,i}^2}{s_{11,i}+s_{12,i}}.
\]

- Evidence: none

### Step 5: Solve equilibrium polarization equations
- Role: process
- Action: For given temperature, applied electric field, and thermal strains, solve the coupled nonlinear equations of state (Eq. 10) to obtain the equilibrium out‑of‑plane polarization \(P_i\) in each layer. Use a suitable root‑finding method (e.g., `scipy.optimize.fsolve`). Explore multiple initial guesses to ensure convergence to the physical solution.
- Evidence: none

### Step 6: Compute dielectric response and tunability
- Role: scored (load‑bearing)
- Action: For the following conditions:
  (a) TEC sweep at annealing temperatures 550, 650, 750 °C, applied fields 0 and 400 kV/cm;
  (b) substrates Si, MgO, SrTiO₃, LaAlO₃ at annealing temperatures 450 and 750 °C, fields 0 and 400 kV/cm;
  (c) temperature dependence of the dielectric properties on Si and SrTiO₃ at \(E = 400\) kV/cm over –10 °C to 90 °C;
  compute the average polarization, the small‑signal average dielectric constant (via numerical derivative of \(\langle P \rangle\) with respect to \(E\)), and the dielectric tunability at 400 kV/cm. Write the results to `/app/outputs/results.csv`.
- Output file: `/app/outputs/results.csv`
- Format: csv
- Contract: Required columns: `condition_type`, `substrate_TEC`, `substrate_name`, `annealing_temperature_C`, `applied_field_kV_per_cm`, `quantity`, `value`.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.csv
- path: `/app/outputs/results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV containing computed average polarization, zero‑field dielectric constant, and tunability for the specified conditions. The columns are: `condition_type`, `substrate_TEC` (optional), `substrate_name` (optional), `annealing_temperature_C`, `applied_field_kV_per_cm`, `quantity` (one of `avg_polarization_C_per_m2`, `dielectric_constant`, `tunability_percent`), `value`.
- schema:
  - `type`: table
  - `required_columns`: `condition_type`, `substrate_TEC`, `substrate_name`, `annealing_temperature_C`, `applied_field_kV_per_cm`, `quantity`, `value`

## Self‑check before finishing (optional, not scored)
A machine‑readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "condition_type",
          "substrate_TEC",
          "substrate_name",
          "annealing_temperature_C",
          "applied_field_kV_per_cm",
          "quantity",
          "value"
        ]
      },
      "description": "CSV containing computed average polarization, zero-field dielectric constant, and tunability for the specified conditions. The columns are: condition_type, substrate_TEC (optional), substrate_name (optional), annealing_temperature_C, applied_field_kV_per_cm, quantity (one of 'avg_polarization_C_per_m2', 'dielectric_constant', 'tunability_percent'), value."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier (not shown to you) checks your `/app/outputs/results.csv`. It first validates that the file is a well‑formed CSV with the required columns and that all mandated conditions and quantities are present. It then extracts your reported values for a subset of the conditions—conditions that are listed above but without revealing which ones—and compares them to a hidden gold standard derived from the paper’s reported numerical results. Comparison uses small relative tolerances for dielectric constant and polarization (typically a few percent) and an absolute tolerance for tunability (a few percentage points). The reward for this stage is the fraction of those held‑out condition‑quantity pairs that agree with the gold within tolerance. A shallow guess or an approximate qualitative trend will not match the gold across many conditions; you must genuinely run the thermodynamic model and numerically solve the equilibrium equations to obtain a high score.
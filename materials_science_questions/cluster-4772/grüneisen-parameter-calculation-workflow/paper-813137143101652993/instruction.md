# Computation of Szigeti effective charge and its volume derivative via multiple methods

## Problem background
In ionic and partially covalent crystals, the Szigeti effective charge parameter $s$ and its logarithmic volume derivative $(\partial \ln s / \partial \ln V)$ are essential for predicting anharmonic contributions to elastic, dielectric, and optical properties under pressure. This work develops three computational routes to calculate these quantities from experimental input data: two routes based on the Szigeti relations, and a third route based on the Hardy deformation-dipole model with several choices of short-range repulsive potential forms. The challenge is to implement these methods and compute the required quantities for a set of test cases.

## Approach
The calculation uses the following physical relations. All quantities are taken from the input file (some may need to be derived from others if missing).

### Effective charge
The Szigeti effective charge $s$ is obtained from the second Szigeti relation:

$$Z e s = \omega_t \sqrt{\frac{\epsilon_0 - \epsilon_\infty}{4\pi}} \frac{3}{\epsilon_\infty + 2} \sqrt{\mu v_a} \tag{1}$$

where $Z=1$ (for alkali halides), $e$ is the electron charge, $\omega_t$ is the transverse optical angular frequency (obtained from the wavenumber $\tilde{\nu}_t$ as $\omega_t = 2\pi c \tilde{\nu}_t$; in the input $\tilde{\nu}_t$ is given in $10^{2}\,\text{m}^{-1}$), $\mu$ is the reduced mass per ion pair, $v_a$ is the unit cell volume ($v_a = 2r^3$ for the NaCl structure), $r$ is the nearest‑neighbour distance, $\epsilon_0$ and $\epsilon_\infty$ are the static and high‑frequency dielectric constants.

Note: the numerical value of $s$ is insensitive to the absolute value of $e$ if consistent units are used; the effective charge $Z e s$ is traditionally reported in units of the electron charge, so $s$ is the dimensionless effective charge parameter.

### Volume derivative of $s$ – Szigeti II method
Differentiating Eq. (1) yields:

$$\left(\frac{\partial \ln s}{\partial \ln v}\right) = -\frac{1}{2\chi_t} \left\{ \frac{1}{\epsilon_0-\epsilon_\infty} \left[ \left(\frac{\partial\epsilon_0}{\partial p}\right)_T - \left(\frac{\partial\epsilon_\infty}{\partial p}\right)_T \right] - \frac{2}{\epsilon_\infty+2} \left(\frac{\partial\epsilon_\infty}{\partial p}\right)_T \right\} + \frac{1}{2} - \gamma_t \tag{2}$$

where $\chi_t$ is the isothermal compressibility, $p$ is pressure, and $\gamma_t = -(\partial \ln \omega_t / \partial \ln v)$ is the transverse optical mode Grüneisen parameter. For the Szigeti II method, $\gamma_t$ is taken directly from the input (if provided).

### Grüneisen parameter from generalized first Szigeti relation (Szigeti I+II)
The generalized first Szigeti relation at $p=0$ gives:

$$\omega_t^2 = \frac{1}{\mu} \frac{\epsilon_\infty+2}{\epsilon_0+2} \frac{\theta r}{\chi_t} \tag{3}$$

where $\theta = 6$ for the NaCl structure. Differentiating this relation yields the Grüneisen parameter $\gamma_t$ as:

$$\gamma_t = \frac{1}{2\chi_t} \left\{ \frac{1}{\epsilon_\infty+2} \left(\frac{\partial\epsilon_\infty}{\partial p}\right)_T - \frac{1}{\epsilon_0+2} \left(\frac{\partial\epsilon_0}{\partial p}\right)_T \right\} + \frac{1}{2} \frac{\partial B_t}{\partial p} - \frac{5}{6} - \frac{2}{3} \chi_t p \left(1 - \frac{4}{3}\chi_t p\right)^{-1} \left(\frac{4}{3} - \frac{\partial B_t}{\partial p}\right) \tag{4}$$

with $B_t = 1/\chi_t$ and $p=0$ (ambient pressure). The term containing $p$ vanishes at $p=0$. The pressure derivative of the bulk modulus $\partial B_t/\partial p$ may be obtained from the pressure derivatives of the elastic constants if not directly provided, using $\partial B_t/\partial p = \frac{1}{3}(\partial C_{11}/\partial p + 2\partial C_{12}/\partial p)$.

After obtaining $\gamma_t$ from Eq. (4), the volume derivative $d\ln s/d\ln V$ is computed from Eq. (2) (Szigeti I+II method).

### Volume derivative of $s$ – Hardy method
Within the deformation‑dipole model, the volume derivative of $s$ is given by:

$$\left(\frac{\partial \ln s}{\partial \ln v}\right) = \frac{1-s}{3s}\left[ 1 - \frac{3\phi'(r) + r\phi''(r)}{\frac{2}{r}\phi(r) + \phi'(r)} \right] \tag{5}$$

where $\phi(r)$ is a short‑range repulsive potential. The value of $s$ is obtained from Eq. (1). The potential parameters are determined from the equilibrium nearest‑neighbour distance $r_0$ and the isothermal compressibility $\chi_0$ (both taken from the input) using the auxiliary quantities:

$$\alpha = \frac{\eta r_0^4}{\chi_0 Z_+ Z_- e^2 \alpha_M} + 2, \qquad \zeta = \frac{Z_+ Z_- e^2 \alpha_M}{M} \tag{6}$$

with $\eta = 18$ (NaCl structure), $\alpha_M = 1.74756$ (Madelung constant for NaCl), $M = 6$ (coordination number), $Z_+ = Z_- = 1$. The isothermal compressibility $\chi_0$ is in the same units as in the input (typically $10^{-11}\,\text{m}^2/\text{N}$). The product $e^2$ appears in the combination $e^2 \alpha_M / \chi_0$; for numerical work, consistent units must be employed (the effective value of $e$ can be set to $1$ if all quantities are expressed in a system where the Coulomb constant is $1$, or the numerical prefactor is absorbed into the definition of $\zeta$ and $\alpha$; the recipes below assume a unit system in which the energy is measured in Joules and lengths in meters, and $e$ is the elementary charge $1.602\times10^{-19}$ C, $\alpha_M$ is dimensionless, and $\chi_0$ is in $\text{m}^2/\text{N}$).

The three potential forms and their resulting expressions are:

- **Born‑Landé**: $\phi(r) = A r^{-n}$,  
  $n = \alpha - 1$,  
  $A = \zeta n^{-1} r_0^{\,n-1}$,  
  $\displaystyle \left(\frac{\partial \ln s}{\partial \ln v}\right) = \frac{(1-s)(n+1)}{3s}$. \tag{7}

- **Born‑Mayer**: $\phi(r) = B \exp(-r/\rho)$,  
  $\rho = r_0 / \alpha$,  
  $B = \zeta (\alpha r_0)^{-1} \exp(\alpha)$,  
  $\displaystyle \left(\frac{\partial \ln s}{\partial \ln v}\right) = \frac{1-s}{3s} \left( \frac{r_0}{\rho} - \frac{2}{r_0/\rho - 2} \right)$. \tag{8}

- **Hellmann**: $\phi(r) = B_1 r^{-1} \exp(-r/\rho_1)$,  
  $\rho_1 = \frac{2 r_0}{(\alpha-2) + \sqrt{(\alpha-2)^2 + 4(\alpha-2)}}$,  
  $B_1 = \zeta \left(1 + \frac{r_0}{\rho_1}\right)^{-1} \exp(r_0/\rho_1)$,  
  $\displaystyle \left(\frac{\partial \ln s}{\partial \ln v}\right) = \frac{1-s}{3s} \left( 2 + \frac{1}{(\rho_1/r_0)^2 + \rho_1/r_0} \right)$. \tag{9}

All derivatives are evaluated at the equilibrium separation $r = r_0$.

### Handling missing input data
The input file may omit some quantities; they must be computed before the above equations are applied.

- **Isothermal compressibility $\chi_t$**: if not given, compute from elastic constants: $\chi_t = 3\,(C_{11} + 2C_{12})^{-1}$, where $C_{11}, C_{12}$ are in $10^{11}\,\text{N}\,\text{m}^{-2}$ (as supplied). The result must be returned in the units expected by the program ($10^{-11}\,\text{m}^2/\text{N}$).
- **Pressure derivative of the bulk modulus $\partial B_t/\partial p$**: if not directly provided, compute from (i) $\partial\chi_t/\partial p$ if available, using $\partial B_t/\partial p = -\chi_t^{-2} \partial\chi_t/\partial p$, or (ii) from the pressure derivatives of elastic constants: $\partial B_t/\partial p = \frac{1}{3}(\partial C_{11}/\partial p + 2\partial C_{12}/\partial p)$.
- **Transverse optical frequency $\omega_t$**: if $\tilde{\nu}_t$ is blank/zero, it can be computed from the generalized first Szigeti relation Eq. (3) with $\chi_t$ and $r_0$ from the input. The angular frequency $\omega_t = 2\pi c \tilde{\nu}_t$, with $c = 2.9979\times10^8$ m/s; the input wavenumber is in $10^2$ m$^{-1}$, so $\tilde{\nu}_t$ (in $10^2$ m$^{-1}$) times $100$ gives wavenumber in m$^{-1}$, then $\omega_t = 2\pi c \times (\text{wavenumber})$. The effective charge formula (1) uses $\omega_t$ in rad/s. However, the factor $2\pi c$ may cancel with the constants hidden in the definition of $s$; the empirical scaling used in the paper's program can be replicated by treating $\omega_t$ as the wavenumber $\tilde{\nu}_t$ (in $10^2$ m$^{-1}$) and working in a consistent unit system where the factor $2\pi c$ is absorbed into the definition of $e$. To avoid ambiguity, implement the exact sequence of operations: read $\text{NU}_t$ from OMEGAT field; if zero, calculate $\omega_t^2$ from Eq. (3) using SI units (J, m, kg, s) with $e=1.602\times10^{-19}$ C, then convert to $10^2$ m$^{-1}$ equivalent by dividing by $2\pi c$ and $100$; otherwise use the given wavenumber. For the purpose of the reproduction, a simpler approach is to note that the values of $s$ reported in the test run (Appendix B) were obtained with the ready-to-use wavenumber and the formula $Z e s = \tilde{\nu}_t \sqrt{ \frac{\epsilon_0 - \epsilon_\infty}{4\pi} } \frac{3}{\epsilon_\infty + 2} \sqrt{\mu v_a}$ with $\tilde{\nu}_t$ in $10^2$ m$^{-1}$ and the numerical constant $e$ adjusted so that $Z e s$ matches the tabulated value; this is equivalent to setting $e=1$ and interpreting $\tilde{\nu}_t$ directly as $\omega_t$ in Eq. (1) provided all other quantities are in the stated units. The test run results are achieved with that simplification. Therefore, to reproduce the output, treat $\omega_t$ in Eq. (1) as the wavenumber number (OMEGAT) and set $e=1$.

- **Other data**: The input file also provides the static and high‑frequency dielectric constants, their pressure derivatives, the isothermal compressibility, and the Grüneisen parameter $\gamma_t$ for the Szigeti II method. The exact parsing of the input file is described in Step 1.

The computational workflow proceeds in two stages: first, parse and prepare the input data, resolving any missing quantities; second, apply the three methods to the completed parameter sets and collect the results in a CSV file.

## Reproduction target
Produce a CSV file, `output_results.csv`, that contains the computed effective charge $s$, the logarithmic volume derivative $d\ln s/d\ln V$, and (for the Szigeti I+II method) the transverse optical Grüneisen parameter $\gamma_t$ for the following four data sets and five computational methods:

- Data sets: KCl at 0 K, KCl at 300 K, KBr at 300 K, KI at 300 K (as specified in the bundled `INPUT1.INP` file).
- Methods: "Szigeti II", "Szigeti I+II", "Hardy Born-Lande", "Hardy Born-Mayer", "Hardy Hellmann".

The CSV must have exactly 20 rows (4 sets × 5 methods) with columns: `set` (string), `method` (string), `s` (float or empty where not produced), `dlns_dlnV` (float), `gamma_t` (float or empty). Ensure the file is saved to `/app/outputs/output_results.csv`.

## Assets

- INPUT1.INP

## Workflow steps

### Step 1: Parse input data and compute missing quantities
- Role: process
- Action: Read the bundled INPUT1.INP file, parse the switches and experimental data for up to four data sets, and compute any missing physical quantities (e.g., isothermal compressibility from elastic constants, transverse optical frequency via the generalized first Szigeti relation) using the logic described in the paper's input processing. Produce a complete set of input parameters for all subsequent calculations.
- Evidence: none

### Step 2: Compute effective charge and volume dependence and write results
- Role: scored (load-bearing)
- Action: Using the completed input parameters, compute: (a) the Szigeti effective charge s via the second Szigeti relation (Eq. 1); (b) the logarithmic volume derivative dlns/dlnV via the Szigeti II method, the Szigeti I+II method (which also yields the transverse optical Grüneisen parameter gamma_t), and the Hardy method with Born-Landé, Born-Mayer, and Hellmann potentials. Write the results to a CSV file with one row per data set and method.
- Output file: `/app/outputs/output_results.csv`
- Format: csv
- Contract: CSV columns: set (string, e.g., 'KCl 0K'), method (string, one of 'Szigeti II', 'Szigeti I+II', 'Hardy Born-Lande', 'Hardy Born-Mayer', 'Hardy Hellmann'), s (float or empty), dlns_dlnV (float), gamma_t (float or empty). Exactly 20 rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/output_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### output_results.csv
- path: `/app/outputs/output_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed Szigeti effective charge and logarithmic volume derivative values for four data sets and five methods, to be compared against hidden reference values (paper-reported test output).
- schema:
  - `type`: table
  - `required_columns`: `set`, `method`, `s`, `dlns_dlnV`, `gamma_t`
  - `column_types`:
    - `set`: string
    - `method`: string
    - `s`: float
    - `dlns_dlnV`: float
    - `gamma_t`: float

Notes: Values are compared to hidden reference values (derived from the paper's reported test output) using a relative tolerance. Only the required methods (Szigeti II, Szigeti I+II, Hardy with Born-Landé, Born-Mayer, Hellmann) are tested.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "output_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "set",
          "method",
          "s",
          "dlns_dlnV",
          "gamma_t"
        ],
        "column_types": {
          "set": "string",
          "method": "string",
          "s": "float",
          "dlns_dlnV": "float",
          "gamma_t": "float"
        }
      },
      "description": "Computed Szigeti effective charge and logarithmic volume derivative values for four data sets and five methods, to be compared against hidden reference values (paper-reported test output)."
    }
  ],
  "notes": "Values are compared to hidden reference values (derived from the paper's reported test output) using a relative tolerance. Only the required methods (Szigeti II, Szigeti I+II, Hardy with Born-Landé, Born-Mayer, Hellmann) are tested."
}
```

## How you are scored
A hidden verifier will read your submitted `output_results.csv` and compare the numerical values for $s$, $d\ln s/d\ln V$, and $\gamma_t$ in each row against pre‑established reference values derived from the paper's test‑run output. The comparison is performed using a relative tolerance; each row that has all present numbers within tolerance earns full credit, and the overall score is the fraction of rows that pass. The verifier independently computes the score from your submitted file – simply reporting numbers is not enough, they must be consistent with the expected results of the described computational routes.

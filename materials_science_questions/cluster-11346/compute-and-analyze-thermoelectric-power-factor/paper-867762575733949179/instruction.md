# Compute and analyze thermoelectric power factor

## Problem background
Three-terminal thermoelectric energy harvesters convert heat to electricity via phonon-assisted electron hopping between quantum dots (QDs) embedded in nanowires. A key performance metric is the thermoelectric power factor \(P = \sigma S^2\). This work investigates a chain of \(N\) QDs arranged in a staircase energy configuration, where the energy step between adjacent dots is a constant \(dE\). The power factor is evaluated as a function of the number of dots \(N\) and the energy step \(dE\), providing insight into how the dot arrangement influences performance.

## Mathematical model

### Hopping transition rate (Fermi golden rule)
The transition rate from QD \(i\) to QD \(j\) is:
\[
\Gamma_{i \rightarrow j}=2 \alpha_{ep} \exp\!\bigl(-|x_i - x_j|/\xi\bigr) \; f_i\bigl(1-f_j\bigr) \; N_p(E_i - E_j), \tag{1}
\]
where \(\alpha_{ep} = 10\,\text{meV}\) (electron‑phonon coupling strength), \(\xi = 2\,\text{nm}\) (tunneling decay length), \(x_i\) is the position of the left edge of QD \(i\), and \(E_i\) its energy. The phonon distribution function is
\[
N_p(\Delta E)=\frac{1}{\exp\!\bigl(|\Delta E|/k_B T\bigr)-1} + \frac{1}{2} + \frac{1}{2}\,\text{sgn}(\Delta E), \tag{2}
\]
with \(k_B T = 30\) meV (the same temperature is used for both phonons and electrons).  
The electron occupation is given by a Fermi distribution with local electrochemical potential \(\mu_i\):
\[
f_i = \frac{1}{\exp\!\bigl((E_i-\mu_i)/k_B T\bigr) + 1}. \tag{3}
\]
At equilibrium (zero bias) the electrochemical potentials are zero, so the equilibrium occupation is
\[
f_i^0 = \frac{1}{\exp\!\bigl(E_i/k_B T\bigr) + 1}. \tag{3'}
\]

### Miller–Abrahams resistor network (inelastic transport)
The linear conductance between QDs \(i\) and \(j\) is
\[
G_{ij} = \frac{e^2}{k_B T}\,\Gamma_{ij}^0,\qquad
\Gamma_{ij}^0 = 2 \alpha_{ep} \exp\!\bigl(-|x_i - x_j|/\xi\bigr) \,
f_i^0\bigl(1-f_j^0\bigr) \, N_p(E_i - E_j). \tag{4}
\]
The QDs are coupled to the left (L) and right (R) electrodes through conductances
\[
G_{iL} = \frac{2 e^2}{k_B T\,\hbar}\,t_0 \exp\!\bigl(-x_i/\xi\bigr), \qquad
G_{iR} = \frac{2 e^2}{k_B T\,\hbar}\,t_0 \exp\!\bigl(-(L_{\text{tot}}-x_i-l_{qd})/\xi\bigr), \tag{5}
\]
with \(t_0 = 100\) meV. Only the first QD (\(i=0\)) couples to the left electrode (\(G_{0L} \neq 0\)), and only the last QD (\(i=N-1\)) couples to the right electrode (\(G_{N-1,R} \neq 0\)); all other \(G_{iL}, G_{iR}\) are zero.

A bias voltage \(V\) is applied, so the electrochemical potentials of the electrodes are
\[
U_L = +e V/2,\qquad U_R = -e V/2.
\]
Kirchhoff’s current law at each QD (\(i = 0,\dots,N-1\)) yields the linear system
\[
\sum_{j \neq i} G_{ij}\,(\mu_i - \mu_j) + G_{iL}\,(\mu_i - U_L) + G_{iR}\,(\mu_i - U_R) = 0. \tag{6}
\]
This can be written as
\[
A\,\boldsymbol{\mu} = \mathbf{b},
\]
with
\[
A_{ii} = G_{iL} + G_{iR} + \sum_{j \neq i} G_{ij},\qquad
A_{ij} = -G_{ij}\;(i\neq j),
\]
\[
b_i = G_{iL} U_L + G_{iR} U_R.
\]
Solve for the QD electrochemical potentials \(\mu_i\). The inelastic current flowing from the left electrode into the system is
\[
I_{\text{in}} = G_{0L}\,(U_L - \mu_0),
\]
and the inelastic conductance is
\[
G_{\text{in}} = I_{\text{in}} / V. \tag{7}
\]

### Elastic tunneling conductance
Each QD also contributes an independent elastic (quantum) channel. The total elastic conductance is
\[
G_{\text{el}} = \sum_{i=0}^{N-1} G_i,\qquad
G_i = \frac{2e^2}{h} \int_{-\infty}^{\infty} \frac{d\varepsilon}{k_B T}\,
\frac{\gamma_{Li}\,\gamma_{Ri}}
{(\varepsilon - E_i)^2 + (\gamma_{Li}+\gamma_{Ri})^2/4}\;
f^0(\varepsilon)\,\bigl[1-f^0(\varepsilon)\bigr], \tag{8}
\]
where
\[
\gamma_{Li}=t_0\exp(-x_i/\xi),\qquad
\gamma_{Ri}=t_0\exp\bigl(-(L_{\text{tot}}-x_i-l_{qd})/\xi\bigr),\qquad
f^0(\varepsilon)=\frac{1}{\exp(\varepsilon/k_B T)+1}.
\]
The integral is evaluated numerically (e.g., using `scipy.integrate.quad`).

### Total conductance, Seebeck coefficient, and power factor
Total conductance:
\[
G = G_{\text{in}} + G_{\text{el}}. \tag{9}
\]
Electrical conductivity (geometry factor):
\[
\sigma = G \, \frac{L_{\text{tot}}}{A},\qquad
A = 10^{-15}\,\text{m}^2. \tag{10}
\]
Three‑terminal phonon‑driven Seebeck coefficient:
\[
S = \frac{k_B}{e}\,\frac{G_{\text{in}}\,\Delta E}{G\,k_B T},\qquad
\Delta E = (N-1)\,dE. \tag{11}
\]
Power factor:
\[
P = \sigma S^2. \tag{12}
\]

### Geometry, energies, and fixed parameters
- Quantum‑dot length: \(l_{qd} = 6\) nm
- Spacing between adjacent QDs: \(d = 6\) nm
- Distance from the outer QDs to the electrodes: \(l_b = 6\) nm
- Decay length: \(\xi = 2\) nm
- Total device length (one nano‑engine): \(L_{\text{tot}} = N\,l_{qd} + (N-1)\,d + 2\,l_b\)
- QD positions: \(x_i = l_b + i\,(l_{qd}+d),\quad i = 0,1,\dots,N-1\)
- Staircase energies: \(E_i = -\frac{\Delta E}{2} + i\,dE,\quad \Delta E = (N-1)\,dE\)
- Electron‑phonon coupling: \(\alpha_{ep} = 10\) meV
- Tunneling hybridization: \(t_0 = 100\) meV
- Temperature: \(k_B T = 30\) meV
- Physical constants:  
  electron charge \(e = 1.602176634\times10^{-19}\) C,  
  Planck constant \(h = 6.62607015\times10^{-34}\) J s,  
  reduced Planck constant \(\hbar = h/(2\pi)\),  
  Boltzmann constant \(k_B = 1.380649\times10^{-23}\) J/K.  
  (These values are standard and can be obtained from any reference source.)

### Task: evaluate over the parameter grid
Loop over the energy step \(dE\) (in meV) from the set  
\(\{10,20,30,40,50,60,70,80,90,100,110,120\}\)  
and the number of QDs \(N\) from the set  
\(\{2,3,5,7,10,12,15,18,21,25,30\}\).  
For each \((dE,N)\) pair, compute \(\sigma\), \(S\), and \(P\) using the model described above.  
**Important:** Convert \(dE\) from meV to energy units (multiply by \(e\), i.e., \(dE_{\text{J}} = dE\,(\text{meV}) \times 1.602176634\times10^{-22}\) J). All quantities must be in SI units in the output (conductivity in S/m, Seebeck in V/K, power factor in W/(K²⋅m)).

## Assets

- numpy: https://pypi.org/project/numpy/
- scipy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Compute power factor for staircase quantum-dot chain
- **Role:** scored (load-bearing)
- **Action:** Implement the three‑terminal hopping thermoelectric transport model for a chain of \(N\) QDs with a staircase energy configuration. Follow the mathematical model described above: compute hopping conductances \(G_{ij}\), build and solve the Miller–Abrahams linear system for \(\mu_i\), obtain \(G_{\text{in}}\). Compute elastic conductance \(G_{\text{el}}\) via numerical integration of the resonant tunneling formula. Derive total conductance \(G = G_{\text{in}}+G_{\text{el}}\), electrical conductivity \(\sigma = G L_{\text{tot}}/A\), Seebeck coefficient \(S\), and power factor \(P = \sigma S^2\). Iterate over all \((dE,N)\) pairs specified above.
- **Output file:** `/app/outputs/step_01_power_factor.csv`
- **Format:** csv (comma‑separated values)
- **Contract:** The CSV file must contain a header row with exactly these columns:  
  `dE(meV)`, `N`, `conductivity(S/m)`, `Seebeck_coefficient(V/K)`, `power_factor(W/(K^2 m))`  
  followed by one data row per \((dE,N)\) pair. All values are real numbers.
- **Scoring:** This output is scored by a hidden verifier.

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_power_factor.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_power_factor.csv
- path: `/app/outputs/step_01_power_factor.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: The computed power factor and intermediate quantities for each \((dE,N)\) pair. The checker verifies self‑consistency (power_factor = conductivity × Seebeck_coefficient²) and structural physical trends (e.g., for each \(dE\) the maximum power factor among \(N>2\) exceeds the power factor at \(N=2\)).
- schema:
  - `type`: table
  - `required_columns`: `dE(meV)`, `N`, `conductivity(S/m)`, `Seebeck_coefficient(V/K)`, `power_factor(W/(K^2 m))`
  - `units`:
    - `dE(meV)`: meV
    - `N`: dimensionless
    - `conductivity(S/m)`: S/m
    - `Seebeck_coefficient(V/K)`: V/K
    - `power_factor(W/(K^2 m))`: W/(K²·m)

Notes: The task is compute‑driven; no external dataset is required. The scoring uses structural consistency checks and trend verification.

## Self-check before finishing (optional, not scored)

A machine‑readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_power_factor.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "dE(meV)",
          "N",
          "conductivity(S/m)",
          "Seebeck_coefficient(V/K)",
          "power_factor(W/(K^2 m))"
        ],
        "units": {
          "dE(meV)": "meV",
          "N": "dimensionless",
          "conductivity(S/m)": "S/m",
          "Seebeck_coefficient(V/K)": "V/K",
          "power_factor(W/(K^2 m))": "W/(K²·m)"
        }
      },
      "description": "The computed power factor and intermediate quantities for each (dE,N) pair. The checker verifies self‑consistency and structural physical trends."
    }
  ],
  "notes": "The task is compute‑driven; no external dataset is required. The scoring performs structural consistency and trend checks."
}
```

## How you are scored
A hidden verifier will read your CSV file and score it solely through **structural checks**:

1. **Self‑consistency**: Your reported `power_factor` must equal `conductivity × Seebeck_coefficient²` within numerical precision.
2. **Physical trends (ordering/monotonicity)**: The verifier checks that the data exhibit expected structural patterns (e.g., for each energy step the optimal power factor among \(N>2\) exceeds the \(N=2\) case, and that Seebeck coefficient and conductivity follow monotonic trends). Exact numerical reference values from the paper are **not** used in the scoring.

The final reward is a weighted combination of these structural checks. Merely reporting numbers without genuinely running the model will fail the checks.
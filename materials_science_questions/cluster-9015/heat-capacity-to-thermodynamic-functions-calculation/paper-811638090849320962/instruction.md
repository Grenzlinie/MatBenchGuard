# Compute Dissociation Degrees of Combustion Products from Equilibrium Constants and Algebraic Relation

## Problem background
In high-temperature combustion, species such as CO₂ and H₂O dissociate into CO, H₂, O₂, and OH, altering the thermodynamic properties of the products. Accurate prediction of dissociation degrees—the fraction of each species that dissociates—is essential for computing enthalpy, entropy, and other state quantities of combustion gases. This task reproduces a computational method that calculates the dissociation degrees αₖ (for CO₂), α_w (for H₂O), and α_h (for OH) for JP‑4 fuel at temperatures 2000–3500 K, over a range of pressures and air excess ratios. The result is a table of dissociation degrees that provides a validated starting point for further combustion gas property calculations.

## Approach
The method rests on three reversible dissociation reactions:

$$
\begin{aligned}
2\,\mathrm{CO_2} &\rightleftharpoons 2\,\mathrm{CO} + \mathrm{O_2} \\
2\,\mathrm{H_2O} &\rightleftharpoons 2\,\mathrm{H_2} + \mathrm{O_2} \\
2\,\mathrm{H_2O} + \mathrm{O_2} &\rightleftharpoons 4\,\mathrm{OH}
\end{aligned}
$$

Each reaction has an equilibrium constant defined from partial pressures:

$$
K_{p\,\mathrm{CO_2}}(T)=\frac{p_{\mathrm{CO}}^{2}p_{\mathrm{O_2}}}{p_{\mathrm{CO_2}}^{2}},\qquad
K_{p\,\mathrm{H_2O}}(T)=\frac{p_{\mathrm{H_2}}^{2}p_{\mathrm{O_2}}}{p_{\mathrm{H_2O}}^{2}}
$$

$$
K_{p\,\mathrm{OH}}(T)=\frac{p_{\mathrm{H_2}}p_{\mathrm{O_2}}}{p_{\mathrm{OH}}^{2}}
$$

These constants are computed from the standard thermodynamic relation

$$
\ln K(T) = -\frac{\Delta G^{\circ}(T)}{RT},
\qquad \Delta G^{\circ}(T) = \sum \nu_i G_i^{\circ}(T) + W(0)
$$

where the Gibbs free energy of each species is \(G_i^{\circ}(T)=H_i(T)-T S_i(T)\), \(R\) is the universal gas constant, and \(W(0)\) is the chemical energy of the reaction. The required enthalpy \(H_i(T)\) and entropy \(S_i(T)\) (at a reference pressure of 1.0332 kg/cm²) for CO₂, H₂O, O₂, CO, H₂, OH, N₂, and Ar, together with the chemical energies for the reactions, are provided in the bundled CSV file `thermo_data.csv`. The equilibrium constant needed for later steps, \(K_{pw}(T)\), is obtained from

$$
K_{pw}(T) = \sqrt{\frac{K_{p\,\mathrm{CO_2}}(T)}{K_{p\,\mathrm{H_2O}}(T)}}
$$

Fuel composition. For JP‑4 fuel, the key parameters are the hydrogen-to‑carbon mass ratio \((\mathrm{H/C})_{\mathrm{fuel}}=0.155\) and the nitrogen‑to‑carbon mass ratio \((\mathrm{N/C})_{\mathrm{fuel}}=0.001\). The air is taken to have the following mass ratios: \((\mathrm{N_2/O_2})_{\mathrm{air}}=3.3103\) and \((\mathrm{Ar/O_2})_{\mathrm{air}}=0.0552\). Using the molecular weights \(M_{\mathrm{C}}=12.011\), \(M_{\mathrm{H_2}}=2.01594\), \(M_{\mathrm{O_2}}=32.0\), \(M_{\mathrm{N_2}}=28.016\), \(M_{\mathrm{Ar}}=39.948\), the per‑carbon mole ratios are:

$$
\begin{aligned}
a_{\mathrm{H_2}} &= \left(\frac{\mathrm{H}}{\mathrm{C}}\right)_{\mathrm{fuel}}\frac{M_{\mathrm{C}}}{M_{\mathrm{H_2}}} \\
a_{\mathrm{O_2}} &= \left(1+\frac{1}{2}a_{\mathrm{H_2}}\right)n \\
a_{\mathrm{N_2}} &= \left(\frac{\mathrm{N_2}}{\mathrm{O_2}}\right)_{\mathrm{air}}\frac{M_{\mathrm{O_2}}}{M_{\mathrm{N_2}}} a_{\mathrm{O_2}} + \left(\frac{\mathrm{N}}{\mathrm{C}}\right)_{\mathrm{fuel}}\frac{M_{\mathrm{C}}}{M_{\mathrm{N_2}}} \\
a_{\mathrm{Ar}} &= \left(\frac{\mathrm{Ar}}{\mathrm{O_2}}\right)_{\mathrm{air}}\frac{M_{\mathrm{O_2}}}{M_{\mathrm{Ar}}} a_{\mathrm{O_2}}
\end{aligned}
$$

Algebraic relation. By applying elemental mass balances and expressing the numbers of moles of each species in terms of the dissociation degrees \(\alpha_k\), \(\alpha_w\), and \(\alpha_h\), one obtains a closed‑form expression for the air excess ratio \(n\) as a function of \(\alpha_k\) (and implicitly the pressure \(p\) in kg/cm²). For a given \(\alpha_k\), define

$$
\beta_k = \frac{\alpha_k}{1-\alpha_k},\qquad
P_{\mathrm{O}n} = 1 + \left(\frac{\mathrm{N_2}}{\mathrm{O_2}}\right)_{\mathrm{air}}\frac{M_{\mathrm{O_2}}}{M_{\mathrm{N_2}}} + \left(\frac{\mathrm{Ar}}{\mathrm{O_2}}\right)_{\mathrm{air}}\frac{M_{\mathrm{O_2}}}{M_{\mathrm{Ar}}}
$$

Then compute the auxiliary coefficients:

$$
\begin{aligned}
h_1 &= \frac{(K_{p\,\mathrm{CO_2}}/p)P_{\mathrm{O}n} - \beta_k^{2}}{(a_{\mathrm{H_2}}/2)\bigl(\beta_k^{2} - (K_{p\,\mathrm{CO_2}}/p)\bigr)} \\
h_2 &= \frac{\beta_k^{2} + (K_{p\,\mathrm{CO_2}}/p)}{\beta_k^{2} - (K_{p\,\mathrm{CO_2}}/p)} \\
h_3 &= -\frac{\alpha_k}{a_{\mathrm{H_2}}} + h_2 + \frac{\beta_k^{2} + \frac{K_{p\,\mathrm{CO_2}}}{p}\frac{M_{\mathrm{C}}}{M_{\mathrm{N_2}}}\bigl(\frac{\mathrm{N}}{\mathrm{C}}\bigr)_{\mathrm{fuel}}}{\frac{1}{2}a_{\mathrm{H_2}}\bigl(\beta_k^{2} - \frac{K_{p\,\mathrm{CO_2}}}{p}\bigr)} \\
h_4 &= -\frac{h_1\bigl((K_{pw}/\beta_k)+1\bigr)}{1+h_2\bigl((K_{pw}/\beta_k)+1\bigr)} \\
h_5 &= \frac{1 - h_3\bigl((K_{pw}/\beta_k)+1\bigr)}{1+h_2\bigl((K_{pw}/\beta_k)+1\bigr)} \\
h_6 &= \frac{h_1}{1+h_2\bigl((K_{pw}/\beta_k)+1\bigr)} \\
h_7 &= \frac{h_2+h_3}{1+h_2\bigl((K_{pw}/\beta_k)+1\bigr)} \\
h_8 &= 1 + \frac{a_{\mathrm{H_2}}}{2}\bigl(h_6 - h_4\bigr) \\
h_9 &= \frac{a_{\mathrm{H_2}}}{2}\bigl(h_7 - h_5\bigr) - \Bigl\{-\frac{\alpha_k}{2} + \frac{a_{\mathrm{H_2}}}{2} + 1\Bigr\} \\
h_{10} &= 8a_{\mathrm{H_2}}K_{p\,\mathrm{OH}} h_4 h_5 \\
h_{11} &= h_7 h_8 + h_6 h_9 \\
h_{12} &= h_7 h_8 - h_6 h_9 \\
h_{13} &= 16 a_{\mathrm{H_2}}K_{p\,\mathrm{OH}} h_6 \Bigl[\Bigl(\frac{K_{pw}}{\beta_k}+1\Bigr)h_6 h_9 + h_5 h_8\Bigr] \\
h_{14} &= 2\Bigl(1+\frac{a_{\mathrm{H_2}}}{2}\Bigr)\bigl(h_6 h_8 - 4 a_{\mathrm{H_2}}K_{p\,\mathrm{OH}} h_4^{2}\bigr)
\end{aligned}
$$

Then the air excess ratio corresponding to that \(\alpha_k\) is

$$
n = \frac{h_{10} - h_{11} - \sqrt{h_{12}^{2} + h_{13}}}{h_{14}}
$$

Equation (12).

For a given temperature \(T\), pressure \(p\), and wanted \(n\), one solves this relation numerically for \(\alpha_k\). Once \(\alpha_k\) is known, the other two dissociation degrees follow from

$$
\begin{aligned}
\alpha_w &= n\Bigl\{1+\frac{a_{\mathrm{H_2}}}{2}\Bigr\}h_6 + h_7 \\
\alpha_h &= n\Bigl\{1+\frac{a_{\mathrm{H_2}}}{2}\Bigr\}h_4 + h_5
\end{aligned}
$$

Equation (13).

For \(n\to\infty\), the limits are

$$
\alpha_k^{\infty} = \frac{\sqrt{(K_{p\,\mathrm{CO_2}}/p)P_{\mathrm{O}n}}}{1+\sqrt{(K_{p\,\mathrm{CO_2}}/p)P_{\mathrm{O}n}}},\qquad \alpha_w^{\infty}=0,\qquad \alpha_h^{\infty}=1
$$

Equations (14)–(15).

The workflow first computes the equilibrium constants \(K_{p\,\mathrm{CO_2}}(T)\), \(K_{p\,\mathrm{H_2O}}(T)\), \(K_{p\,\mathrm{OH}}(T)\), and \(K_{pw}(T)\) at the required temperatures using the data in `thermo_data.csv`. Then for every combination of \(T\), \(p\), and \(n\) (including \(n=\infty\)), the algebraic relation is solved and the three \(\alpha\) values are written to the output CSV.

## Reproduction target
Produce a CSV file `dissociation_degrees.csv` containing exactly one row for each combination of temperature \(T\), pressure \(p\), and air excess ratio \(n\) from the following sets:

- \(T\) (K): 2000, 2250, 2500, 2750, 3000, 3500
- \(p\) (kg/cm²): for each temperature, use the pressures that were deemed physically meaningful in the original study, namely:
  - at \(T=2000\): 0.05, 0.1, 0.5, 1, 5, 10, 20
  - at \(T=2250\): 0.05, 0.1, 0.5, 1, 5, 10, 20, 50
  - at \(T=2500\): 0.05, 0.1, 0.5, 1, 5, 10, 20, 50, 100
  - at \(T=2750\): 0.1, 0.5, 1, 5, 10, 20, 50, 100
  - at \(T=3000\): 0.1, 0.5, 1, 5, 10, 20, 50, 100, 200
  - at \(T=3500\): 0.1, 0.5, 1, 5, 10, 20, 50, 100, 200
- \(n\): 1, 1.2, 1.5, 2, 3, 5, 10, \(\infty\) (use the string `inf` in the CSV for \(n=\infty\)).

Columns: `T_K` (float), `p_kgcm2` (float), `n` (float, `inf` for infinity), `alpha_k` (float), `alpha_w` (float), `alpha_h` (float). Ensure that every computed dissociation degree lies in \([0,1]\) (except \(\alpha_h^{\infty}\) which is exactly 1). The output must include all rows; the verifier will compare each numeric cell against independently recomputed values.

## Assets

- Thermodynamic data and fuel composition parameters

## Workflow steps

### Step 1: Compute equilibrium constants
- Role: process
- Action: Using the provided temperature-dependent enthalpy and entropy data for CO2, H2O, O2, CO, H2, OH, N2, Ar and the chemical energies of the relevant reactions, calculate the equilibrium constants KpCO2, Kpw, and KpOH at temperatures 2000, 2250, 2500, 2750, 3000, and 3500 K via the standard thermodynamic relation between equilibrium constants and Gibbs free energy change. Save the results as an intermediate CSV.
- Evidence: `/app/outputs/equilibrium_constants.csv`

### Step 2: Compute dissociation degrees table
- Role: scored (load-bearing)
- Action: For each combination of temperature T (2000, 2250, 2500, 2750, 3000, 3500 K), pressure p (selected set per temperature as specified in the documentation), and air excess ratio n (1, 1.2, 1.5, 2, 3, 5, 10, ∞), use the equilibrium constants from step_01 and the provided JP‑4 fuel composition parameters to solve the derived algebraic relation and obtain the dissociation degrees αk (CO2), αw (H2O), αh (OH). Output the complete table as a CSV.
- Output file: `/app/outputs/dissociation_degrees.csv`
- Format: csv
- Contract: Columns: T_K (float, units K), p_kgcm2 (float, units kg/cm²), n (float, use inf for ∞), alpha_k (float), alpha_w (float), alpha_h (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dissociation_degrees.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dissociation_degrees.csv
- path: `/app/outputs/dissociation_degrees.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Dissociation degrees for JP‑4 combustion gas at all specified (T,p,n) conditions. The checker recomputes each value using the same algebraic model and provided equilibrium constants, then scores the fraction of entries that lie within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `T_K`, `p_kgcm2`, `n`, `alpha_k`, `alpha_w`, `alpha_h`
  - `units`:
    - `T_K`: K
    - `p_kgcm2`: kg/cm^2
    - `n`: dimensionless
    - `alpha_k`: dimensionless
    - `alpha_w`: dimensionless
    - `alpha_h`: dimensionless

Notes: The equilibrium constants are not directly scored; their correctness is enforced via the dependency of the scored step.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dissociation_degrees.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "T_K",
          "p_kgcm2",
          "n",
          "alpha_k",
          "alpha_w",
          "alpha_h"
        ],
        "units": {
          "T_K": "K",
          "p_kgcm2": "kg/cm^2",
          "n": "dimensionless",
          "alpha_k": "dimensionless",
          "alpha_w": "dimensionless",
          "alpha_h": "dimensionless"
        }
      },
      "description": "Dissociation degrees for JP‑4 combustion gas at all specified (T,p,n) conditions. The checker recomputes each value using the same algebraic model and provided equilibrium constants, then scores the fraction of entries that lie within tolerance."
    }
  ],
  "notes": "The equilibrium constants are not directly scored; their correctness is enforced via the dependency of the scored step."
}
```

## How you are scored
A hidden verifier will recompute the dissociation degrees for every \((T,p,n)\) condition using the same algebraic model and the same input data. For each row in your `dissociation_degrees.csv`, the verifier checks whether all three \(\alpha\) values lie within a combined tolerance (relative error or absolute, whichever is looser). The final reward is the fraction of rows that pass this check. Reporting numbers that match the paper’s published table is not sufficient—your implementation must accurately execute the model for every condition. The verifier does not access any external network; it uses the same public input data and the same equations described in this instruction.

# Kink-Pair Nucleation Activation Parameter Calculation for Ni-Cr Solid Solutions

## Problem background
The Kink-Pair Nucleation (KPN) model of solid-solution hardening describes the temperature dependence of the critical resolved shear stress (CRSS) in alloys. In this model, the CRSS follows an exponential relation with temperature, and the parameters reflect both the solute concentration and the nature of solute distribution in the slip plane. This work re-analyzes published tensile data for polycrystalline Ni and Ni-Cr alloys (5.6, 22.0, and 39.9 at.% Cr) using the KPN model. The goal is to compute the model’s activation parameters ($\tau_0$, $W_0$, $n$, $U$) for each composition from the reported log-linear $\ln \tau$–$T$ relations, and to determine the solute concentration at which $W_0$ reaches a maximum — an indicator of whether the solute distribution is random or ordered.

## Approach
The KPN model relates the CRSS $\tau$ to temperature $T$ and solute concentration $c$ by $\tau = \tau_0 \exp(-m k T / W_0)$, where $\tau_0$ is the athermal CRSS, $m=25$, $k$ is Boltzmann's constant, and $W_0$ is a material parameter. This yields a linear log-relation $\ln \tau = A - B T$ with $A = \ln \tau_0$ and $B = m k / W_0$. Given the fitted $A$ and $B$ for pure Ni and three Ni-Cr alloys, we compute $\tau_0 = \exp(A)$ and $W_0 = m k / B$. The microscopic parameters $n$ and $U$ are then obtained from the relations $n^3 = (W_0^2/\tau_0)[4G/(G b^3)^2]$ and $U = W_0^2 / (G b^3 n^2 c^{1/2})$, using the known shear modulus $G$, Burgers vector $b$, and the product $G b^3$. The solute fractions are $c=1$ for pure Ni, and $c=0.056, 0.220, 0.399$ for the alloys. The sequence of computed $W_0$ values across compositions reveals the nature of solute distribution.

## Reproduction target
Produce a CSV file (`activation_parameters.csv`) containing the columns `composition`, `c_at_pct`, `tau_o_MPa`, `W_o_eV`, `n`, and `U_meV` for all four compositions: pure Ni, Ni-5.6Cr, Ni-22.0Cr, and Ni-39.9Cr (using the atomic percentages shown). The computed $\tau_0$, $W_0$, $n$, and $U$ must be derived from the given log-linear relations and material constants. In addition, the hidden verifier will check that the chromium concentration at which $W_0$ is highest (i.e., the `c_at_pct` value of the row with the maximum `W_o_eV`) is correctly identified.

## Assets
No external datasets, models, or tools are required beyond standard Python scientific libraries (e.g., `numpy`, `math`, `csv`). All needed fitted parameters and material constants are stated in the workflow step.

## Workflow steps

### Step 1: Compute activation and microscopic parameters
- Role: scored (load-bearing)
- Action: Using the given log-linear relations lnτ = A − B T for pure Ni and Ni-Cr alloys (5.6, 22.0, 39.9 at.% Cr) and the constants G=7.5×10⁴ MPa, b=0.2492 nm, Gb³=7.24 eV, m=25, k=8.617333262145×10⁻⁵ eV/K, compute τₒ = exp(A), Wₒ = mk/B, then derive n from n³ = (Wₒ²/τₒ)·(4G/(Gb³)²) and U = Wₒ²/(Gb³ n² c^{1/2}) for atomic fractions c=1 (pure Ni), 0.056, 0.220, 0.399. Output a CSV file with the results.
- Output file: `/app/outputs/activation_parameters.csv`
- Format: csv
- Contract: Header: composition, c_at_pct, tau_o_MPa, W_o_eV, n, U_meV. composition is string, c_at_pct is float (at.%), tau_o_MPa is float (MPa), W_o_eV is float (eV), n is float (dimensionless), U_meV is float (meV). Exactly four rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/activation_parameters.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### activation_parameters.csv
- path: `/app/outputs/activation_parameters.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Computed activation parameters τₒ, Wₒ, n, and U for pure Ni and three Ni-Cr alloys.
- schema:
  - `type`: table
  - `required_columns`: `composition`, `c_at_pct`, `tau_o_MPa`, `W_o_eV`, `n`, `U_meV`
  - `units`:
    - `tau_o_MPa`: MPa
    - `W_o_eV`: eV
    - `U_meV`: meV

Notes: The checker will compare each row's quantities to the paper-reported values within appropriate tolerances, and verify that the row with maximum W_o_eV has c_at_pct = 22.0.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "activation_parameters.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition",
          "c_at_pct",
          "tau_o_MPa",
          "W_o_eV",
          "n",
          "U_meV"
        ],
        "units": {
          "tau_o_MPa": "MPa",
          "W_o_eV": "eV",
          "U_meV": "meV"
        }
      },
      "description": "Computed activation parameters τₒ, Wₒ, n, and U for pure Ni and three Ni-Cr alloys."
    }
  ],
  "notes": "The checker will compare each row's quantities to the paper-reported values within appropriate tolerances, and verify that the row with maximum W_o_eV has c_at_pct = 22.0."
}
```

## How you are scored
A hidden verifier reads your output CSV and compares each computed quantity ($\tau_0$, $W_0$, $n$, $U$) for every composition against hidden reference values. The verifier also checks that the row with the largest $W_o_eV$ corresponds to the correct chromium concentration. Each component contributes to the final reward; partial credit is awarded for values that fall within acceptable margins. Reporting the paper's published numbers without re-computing them from the given relations will not earn full credit.

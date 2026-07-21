# ZT Calculation for Ordered DNA Ladder using Landauer Formalism

## Problem background
Thermoelectric energy conversion at the nanoscale is promising for waste heat recovery. This task theoretically investigates the thermoelectric figure of merit ZT of a flat DNA ladder. The ladder is described by a tight-binding model with base-pair site energies and hopping parameters, and the electronic transmission is computed via the transfer-matrix method. The objective is to determine ZT as a function of the Fermi energy at several temperatures and to examine the conditions under which ZT can become large, using the Landauer formalism.

## Approach
The DNA molecule is represented as a two-stranded ladder with an alternating sequence of base pairs (A-T, G-C, …). The electronic structure is captured by a nearest-neighbor tight-binding Hamiltonian with site energies: Adenine (A) 0.26 eV, Thymine (T) –0.93 eV, Guanine (G) 1.14 eV, and Cytosine (C) –1.06 eV. All intra-strand and inter-strand hopping integrals, as well as the molecule-lead coupling, are set to a common value λ = 2.8 eV. The system consists of N = 50 base pairs and is connected to semi-infinite leads modeled as perfect two-stranded ladders.

The transmission probability T(E) is obtained using the transfer-matrix method combined with Oseledec's theorem. The transfer matrix of the total system is built slice by slice, and the localization length is extracted from the lowest Lyapunov exponent, yielding T(E) = exp(−2N/Λ). From T(E), the Landauer integrals L_n = −∫ T(E)(E−Ef)^n (∂f/∂E) dE (n = 0,1,2) are evaluated with the Fermi-Dirac distribution f. The electrical conductance G, Seebeck coefficient S, electronic thermal conductance κ, and the figure of merit ZT are then given by:
G = (2e²/h)L₀,
S = −L₁/(eT L₀),
κ = (2/(hT))(L₂ − L₁²/L₀),
ZT = (L₀L₂/L₁² − 1)⁻¹.
The calculation is carried out over an energy range from –3 eV to 3 eV with a step ≤0.01 eV at three temperatures: 200 K, 300 K, and 400 K.

## Reproduction target
Produce the thermoelectric figure of merit ZT as a function of the equilibrium Fermi energy Ef for the ordered alternating DNA ladder (N = 50 base pairs). Output two CSV files:
- zt_ordered_400K.csv: ZT vs Ef at T = 400 K.
- zt_ordered_temperatures.csv: ZT vs Ef at T = 200 K, 300 K, and 400 K, with separate columns for each temperature.
The data must span the Fermi energy range from –3 eV to 3 eV in steps ≤0.01 eV and be computed from the transmission function via the Landauer prescription. The numerical values will be checked for internal consistency and compared against hidden reference criteria.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Transmission Calculation
- Role: process
- Action: Implement the tight-binding Hamiltonian for a two-stranded ladder with alternating base-pair sequence (A-T, G-C, ...) of length N=50. Use on-site energies: A=0.26 eV, T=-0.93 eV, G=1.14 eV, C=-1.06 eV. Set all intra-strand and inter-strand hopping integrals to λ=2.8 eV and molecule-lead coupling v_ML=2.8 eV. Compute the electronic transmission T(E) via transfer-matrix formalism and Oseledec's theorem for an energy grid from -3 eV to 3 eV with step ≤0.01 eV. Store the transmission function and energy grid for later use.
- Evidence: `/app/outputs/transmission_log.txt`

### Step 2: ZT at 400 K
- Role: scored (load-bearing)
- Action: From the stored T(E), evaluate Landauer integrals L_0, L_1, L_2 using the Fermi-Dirac distribution at T=400 K and compute ZT = (L_0 L_2 / L_1^2 - 1)^{-1}. Write a CSV file with columns 'Ef (eV)' and 'ZT' covering the energy grid.
- Output file: `/app/outputs/zt_ordered_400K.csv`
- Format: csv
- Contract: CSV header: Ef (eV), ZT (dimensionless). Energy range -3 to 3 eV, step ≤ 0.01 eV.
- Scoring: scored by hidden verifier

### Step 3: ZT at Multiple Temperatures
- Role: scored
- Action: From the stored T(E), compute ZT at T=200 K, 300 K, and 400 K. Write a CSV file with columns 'Ef (eV)', 'ZT_200K', 'ZT_300K', 'ZT_400K'.
- Output file: `/app/outputs/zt_ordered_temperatures.csv`
- Format: csv
- Contract: CSV header: Ef (eV), ZT_200K, ZT_300K, ZT_400K (all dimensionless). Same energy grid.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/zt_ordered_400K.csv`
- `/app/outputs/zt_ordered_temperatures.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### zt_ordered_400K.csv
- path: `/app/outputs/zt_ordered_400K.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: ZT versus Fermi energy at 400 K. Verified by threshold (ZT_max > 20) and curve shape (two peaks, band-edge behavior).
- schema:
  - `type`: table
  - `required_columns`: `Ef (eV)`, `ZT`

### zt_ordered_temperatures.csv
- path: `/app/outputs/zt_ordered_temperatures.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: ZT versus Fermi energy at three temperatures. Verified by structural trend: ZT_max increases with temperature (ZTmax_400K > ZTmax_300K > ZTmax_200K).
- schema:
  - `type`: table
  - `required_columns`: `Ef (eV)`, `ZT_200K`, `ZT_300K`, `ZT_400K`

Notes: Scoring uses T0 result-level comparison: maximum ZT at 400 K checked against a threshold (tolerance), and temperature trend verified from the multi-temperature file. No raw transmission file is scored; it is required as an intermediate for the scored steps.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "zt_ordered_400K.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "Ef (eV)",
          "ZT"
        ]
      },
      "description": "ZT versus Fermi energy at 400 K. Verified by threshold (ZT_max > 20) and curve shape (two peaks, band-edge behavior)."
    },
    {
      "file": "zt_ordered_temperatures.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "Ef (eV)",
          "ZT_200K",
          "ZT_300K",
          "ZT_400K"
        ]
      },
      "description": "ZT versus Fermi energy at three temperatures. Verified by structural trend: ZT_max increases with temperature (ZTmax_400K > ZTmax_300K > ZTmax_200K)."
    }
  ],
  "notes": "Scoring uses T0 result-level comparison: maximum ZT at 400 K checked against a threshold (tolerance), and temperature trend verified from the multi-temperature file. No raw transmission file is scored; it is required as an intermediate for the scored steps."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently scores each scored artifact. It reads zt_ordered_400K.csv and zt_ordered_temperatures.csv, checks properties such as the maximum ZT values, their relative ordering across temperatures, and the overall shape of the curves, and compares them to a reference extracted from the paper. Each scored step contributes a weight to the final reward (a float between 0 and 1). Simply reporting a number is not sufficient; the full CSV files must be present and correctly formatted.

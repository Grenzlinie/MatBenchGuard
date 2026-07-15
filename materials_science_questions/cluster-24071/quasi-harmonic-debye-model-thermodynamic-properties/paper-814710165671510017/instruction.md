# Quasi-harmonic Debye thermodynamic properties of half-Heusler compounds

## Problem background
Half-Heusler compounds of the C1b structure type are of great interest for spintronic and thermoelectric applications due to their tunable electronic and magnetic properties. A central aspect of their practical use is the thermodynamic response under varying temperature and pressure. This task focuses on the two representative compounds CoMnTe and RuMnTe, for which the temperature- and pressure-dependent thermodynamic functions — isothermal bulk modulus, specific heats, Debye temperature, Grüneisen parameter, and volume thermal expansion coefficient — can be obtained by combining first-principles density functional theory with a quasi-harmonic Debye model. The goal is to compute these properties over a broad range of conditions to assess their thermal behaviour, without prior knowledge of the numerical results.

## Approach
The thermodynamic analysis proceeds in two major stages. First, spin-polarized DFT total-energy calculations are performed to map the ground-state energy as a function of volume, E(V), for each compound. This requires building the half-Heusler crystal structures at their equilibrium lattice constants and running self-consistent field calculations at a set of volumes spanning approximately ±5% around equilibrium using an all-electron full-potential method (FP-LAPW) with the GGA-PBE exchange-correlation functional. The resulting E(V) data are then processed within the quasi-harmonic Debye model framework. In this model, the non-equilibrium Gibbs energy is minimised with respect to volume at each (T,P) condition, yielding a thermal equation of state V(P,T) from which the isothermal bulk modulus, constant-volume and constant-pressure heat capacities, Debye temperature, Grüneisen parameter, and thermal expansion coefficient are derived. The Debye temperature itself depends on the adiabatic bulk modulus, which is computed from the second derivative of E(V). The model treats the solid as a Debye phonon gas and incorporates the volume dependence through the Grüneisen parameter. The computation is carried out over a (T,P) grid covering 0–1200 K (step 100 K) and 0–45 GPa (step 5 GPa) for both compounds.

## Reproduction target
Produce a single CSV file containing the computed thermodynamic properties for CoMnTe and RuMnTe on the specified temperature–pressure grid. The CSV must have the columns: compound (string, 'RuMnTe' or 'CoMnTe'), T_K (float, temperature in K), P_GPa (float, pressure in GPa), B_T_GPa (float, isothermal bulk modulus in GPa), C_V_JmolK (float, heat capacity at constant volume in J·mol⁻¹·K⁻¹), C_P_JmolK (float, heat capacity at constant pressure in J·mol⁻¹·K⁻¹), Theta_K (float, Debye temperature in K), gamma (float, Grüneisen parameter, dimensionless), alpha_1e5_perK (float, volume thermal expansion coefficient in units of 10⁻⁵ K⁻¹). The grid must include every combination of T in {0,100,200,…,1200} K and P in {0,5,10,…,45} GPa. The values should be physically consistent and follow the expected thermodynamic trends, but the task does not require matching any specific previously published numerical values.

## Assets

- Elk (FP-LAPW DFT code): https://elk.sourceforge.net/
- Gibbs2 (quasi-harmonic Debye model): http://gibbs2.fis.uniovi.es/
- Python scientific stack (numpy, scipy, pandas): numpy scipy pandas

## Workflow steps

### Step 1: DFT total-energy calculations
- Role: process
- Action: Build the C1b crystal structures for half-Heusler CoMnTe (a=5.876Å) and RuMnTe (a=6.092Å). Perform spin-polarized DFT self-consistent field calculations for a set of volumes around equilibrium (at least 10 volumes per compound, covering approximately ±5% of equilibrium) using an all-electron FP-LAPW code (Elk) with the GGA-PBE functional. Save the energy-volume data: one text file per compound with columns (volume in a.u.³, total energy in eV).
- Evidence: `/app/outputs/ev_CoMnTe.txt, ev_RuMnTe.txt`

### Step 2: Quasi-harmonic Debye model thermodynamic calculations
- Role: scored (load-bearing)
- Action: Using the E(V) data from the previous step, run Gibbs2 or an equivalent open-source implementation of the quasi-harmonic Debye model to compute the temperature- and pressure-dependent thermodynamic quantities. Produce a CSV file covering the temperature range 0–1200 K in steps of 100 K and pressure range 0–45 GPa in steps of 5 GPa for both compounds. The CSV must include columns: compound, T_K, P_GPa, B_T_GPa, C_V_JmolK, C_P_JmolK, Theta_K, gamma, alpha_1e5_perK.
- Output file: `/app/outputs/thermodynamic_properties.csv`
- Format: csv
- Contract: Columns: compound (string, 'RuMnTe' or 'CoMnTe'), T_K (float, temperature in K), P_GPa (float, pressure in GPa), B_T_GPa (float), C_V_JmolK (float), C_P_JmolK (float), Theta_K (float), gamma (float), alpha_1e5_perK (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermodynamic_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermodynamic_properties.csv
- path: `/app/outputs/thermodynamic_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Scored CSV containing the computed thermodynamic properties from the quasi-harmonic Debye model for both compounds over the full temperature and pressure grid.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `T_K`, `P_GPa`, `B_T_GPa`, `C_V_JmolK`, `C_P_JmolK`, `Theta_K`, `gamma`, `alpha_1e5_perK`
  - `units`:
    - `T_K`: K
    - `P_GPa`: GPa
    - `B_T_GPa`: GPa
    - `C_V_JmolK`: J/(mol·K)
    - `C_P_JmolK`: J/(mol·K)
    - `Theta_K`: K
    - `gamma`: dimensionless
    - `alpha_1e5_perK`: 10^-5 K^-1

Notes: The checker reads this CSV and compares the values at the specific (T,P) points of the paper's Table 3 (Debye temperature and Gruneisen parameter at T=300,600,900,1200 K, P=0,15,30,45 GPa) and the zero‑pressure room‑temperature alpha values to hidden paper‑reported gold values using tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermodynamic_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "T_K",
          "P_GPa",
          "B_T_GPa",
          "C_V_JmolK",
          "C_P_JmolK",
          "Theta_K",
          "gamma",
          "alpha_1e5_perK"
        ],
        "units": {
          "T_K": "K",
          "P_GPa": "GPa",
          "B_T_GPa": "GPa",
          "C_V_JmolK": "J/(mol·K)",
          "C_P_JmolK": "J/(mol·K)",
          "Theta_K": "K",
          "gamma": "dimensionless",
          "alpha_1e5_perK": "10^-5 K^-1"
        }
      },
      "description": "Scored CSV containing the computed thermodynamic properties from the quasi-harmonic Debye model for both compounds over the full temperature and pressure grid."
    }
  ],
  "notes": "The checker reads this CSV and compares the values at the specific (T,P) points of the paper's Table 3 (Debye temperature and Gruneisen parameter at T=300,600,900,1200 K, P=0,15,30,45 GPa) and the zero‑pressure room‑temperature alpha values to hidden paper‑reported gold values using tolerances."
}
```

## How you are scored
A hidden verifier reads the submitted thermodynamic_properties.csv and evaluates the results. The verifier compares the numerical values at selected (T,P) conditions — chosen to reflect the key features of the paper’s analysis — against independently established reference values, using tolerances that account for differences in DFT implementation and numerical details. In addition, the verifier checks that the data exhibit physically correct qualitative trends: for example, the bulk modulus increases with pressure at constant temperature and decreases with temperature at constant pressure; the heat capacities approach the Dulong–Petit limit at high temperature; the Debye temperature increases with pressure and decreases with temperature; the Grüneisen parameter decreases with pressure and increases with temperature; and the thermal expansion coefficient increases rapidly at low temperature then more slowly, and decreases with increasing pressure. The final score is a weighted combination of these checks, rewarding solutions that are both numerically accurate and physically consistent.

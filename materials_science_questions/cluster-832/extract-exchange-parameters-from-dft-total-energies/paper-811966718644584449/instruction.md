# Compute magnetic phase transition temperatures with continuous-orientation MFA

## Problem background
Compounds of the RT2X2 family, in particular LaMn2Ge2 and LaMn2Si2, display a rich set of magnetic phase transitions as temperature changes: at low T they adopt a “conical” spin arrangement, and upon heating they may transform into helical, canted, collinear, and finally paramagnetic structures. Standard mean‑field approximations (MFA) that treat the spin states as discrete reproduce the sequence of transitions but overestimate the critical temperatures by a large factor. This task investigates an improved MFA in which each spin is allowed to explore a continuous spectrum of orientations. The goal is to compute the temperature‑dependent order parameters and to extract the transition temperatures for the two compounds using this continuous‑orientation MFA.

## Approach
The magnetic energy is modelled by a Hamiltonian with bilinear and biquadratic exchange interactions up to fifth neighbours and a single‑ion anisotropy:

H = –½ Σ_{i,j} J_{ij} S_i·S_j  – ½ Σ_{i,j} B_{ij} (S_i·S_j)²  +  D₂ Σ_i S_{i,z}² .

The spin quantum number is S = 3/2 for both compounds. The magnetic structure is parameterised by two global angles θ and α: the average spin at site (h,k,l) has polar direction (θ, φ = lα + ξ_{hk}) with ξ_{hk}=0 or π, giving a conical structure for general θ,α (helical for θ=90°, canted for α = 0,90°,180°,270°, collinear for θ=90°,α=180°).

In the MFA a single‑site partition function Z_s is built by summing over m = –S,…,S and integrating over all continuous orientations of the reference spin. The equilibrium state at each temperature is found by solving the stationarity conditions ∂Z/∂θ = 0 and ∂Z/∂α = 0 simultaneously with the self‑consistency equations for the average spin amplitude ⟨S⟩ and the average squared magnetic quantum number ⟨m²⟩. Two variants of the MFA are used: **MFA2** for LaMn2Ge2 and **MFA4** for LaMn2Si2. They differ in how the biquadratic terms are approximated before choosing the reference site:

- **MFA2**: In the total biquadratic energy sum \(\sum_{i,j}' B_{ij}(m_i^2+m_j^2)(p_{ij}^2+1)\), replace the factor \((m_i^2+m_j^2)(p_{ij}^2+1)\) by \(2 m_i^2(p_{ij}^2+1)\). Then fix \(i=0\) as the reference site and replace the source spins by their mean-field values: \(m_j \to \langle S\rangle\), \(m_j^2 \to \langle m^2\rangle\).
- **MFA4**: Expand the exact pair energies in fluctuations \(\hat{\Delta}_i = \hat{S}_i - \langle \hat{S}_i\rangle\) and \(\hat{\Delta}_{2,i} = \hat{S}_i^2 - \langle \hat{S}_i^2\rangle\), retaining only the terms linear in these fluctuations. Then apply the same manipulation as in MFA2 to the resulting sums, and finally set the source averages to \(\langle S\rangle\) and \(\langle m^2\rangle\).

**Interaction constants for LaMn2Ge2 (MFA2):**
J₁ = –0.002137, J₂ = –0.00005, J₃ = 0.002792, J₄ = 0.0010, J₅ = 0.000755
B₁ = –0.000482, B₂ = –0.00023, B₃ = –0.0001555, B₄ = –0.00009, B₅ = –0.000053, D₂ = 0.0005

**Interaction constants for LaMn2Si2 (MFA4):**
J₁ = –0.00145406, J₂ = –0.0003, J₃ = 0.00177942, J₄ = 0.0010, J₅ = 0.0006
B₁ = –0.00045278, B₂ = –0.0003, B₃ = –0.00024431, B₄ = –0.00017, B₅ = –0.00010941, D₂ = 0.0

All constants are in the energy units used in the original work (the same as for the Hamiltonian). The lattice contains four first, second and third neighbours, two fourth neighbours and eight fifth neighbours; only these neighbour shells carry non‑zero interactions.

## Reproduction target
Produce two CSV files – `scan_LaMn2Ge2.csv` and `scan_LaMn2Si2.csv` – each containing a full temperature scan from roughly 10 K to 1200 K. Columns: T (K), theta (degrees), alpha (degrees), S_bar (average spin amplitude), m2_bar (average of m²), free_energy (energy per site). The temperature points must be dense enough to resolve the phase transitions. From these scans the hidden verifier will locate the three transition temperatures T_c1, T_c2, T_c3 for each compound and verify the sequence of magnetic phases. The target is to obtain the correct transition temperatures and the correct phase sequence as predicted by the continuous‑orientation MFA with the parameter sets above.

## Assets
No external datasets or models are required. The interaction constants are given in the Approach section above. The computation needs only standard numerical Python libraries (`numpy`, `scipy`) for solving self‑consistent equations, evaluating modified Bessel functions, and writing CSV files. No other resources are needed.

## Workflow steps

### Step 1: Parameter setup
- Role: process
- Action: Define the spin Hamiltonian parameters (exchange constants J_v, B_v, D2) for LaMn2Ge2 and LaMn2Si2 as provided in the task, and set the spin quantum number S=3/2.
- Evidence: none

### Step 2: Temperature scan for LaMn2Ge2
- Role: scored (load-bearing)
- Action: Implement the continuous-orientation MFA (variant MFA2) for LaMn2Ge2. For a range of temperatures from low T (about 10 K) to above the paramagnetic transition (about 1200 K), solve the self-consistent equations for the conical parameters theta, alpha and the averages S_bar and m2_bar. Write the temperature scan to the output file.
- Output file: `/app/outputs/scan_LaMn2Ge2.csv`
- Format: csv
- Contract: columns: T (float, K), theta (float, degrees), alpha (float, degrees), S_bar (float), m2_bar (float), free_energy (float). One row per temperature point scanned.
- Scoring: scored by hidden verifier

### Step 3: Temperature scan for LaMn2Si2
- Role: scored (load-bearing)
- Action: Implement the continuous-orientation MFA (variant MFA4) for LaMn2Si2. For a range of temperatures from low T to about 1200 K, solve the self-consistent equations to find theta, alpha, S_bar, m2_bar. Write the scan to the output file.
- Output file: `/app/outputs/scan_LaMn2Si2.csv`
- Format: csv
- Contract: columns: T (float, K), theta (float, degrees), alpha (float, degrees), S_bar (float), m2_bar (float), free_energy (float). One row per temperature point scanned.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/scan_LaMn2Ge2.csv`
- `/app/outputs/scan_LaMn2Si2.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### scan_LaMn2Ge2.csv
- path: `/app/outputs/scan_LaMn2Ge2.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Temperature-dependent magnetic order parameters for LaMn2Ge2. The checker extracts transition temperatures T_c1, T_c2, T_c3 from this scan and compares with hidden gold values.
- schema:
  - `type`: table
  - `required_columns`: `T`, `theta`, `alpha`, `S_bar`, `m2_bar`, `free_energy`
  - `items`: object
  - `units`: object

### scan_LaMn2Si2.csv
- path: `/app/outputs/scan_LaMn2Si2.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Temperature-dependent magnetic order parameters for LaMn2Si2. The checker extracts transition temperatures T_c1, T_c2, T_c3 from this scan and compares with hidden gold values.
- schema:
  - `type`: table
  - `required_columns`: `T`, `theta`, `alpha`, `S_bar`, `m2_bar`, `free_energy`
  - `items`: object
  - `units`: object

Notes: The checker recomputes transition temperatures from the submitted temperature scans via threshold-crossing detection and validates the phase sequence; no raw gold values are exposed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "scan_LaMn2Ge2.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "theta",
          "alpha",
          "S_bar",
          "m2_bar",
          "free_energy"
        ],
        "items": {},
        "units": {}
      },
      "description": "Temperature-dependent magnetic order parameters for LaMn2Ge2. The checker extracts transition temperatures T_c1, T_c2, T_c3 from this scan and compares with hidden gold values."
    },
    {
      "file": "scan_LaMn2Si2.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "theta",
          "alpha",
          "S_bar",
          "m2_bar",
          "free_energy"
        ],
        "items": {},
        "units": {}
      },
      "description": "Temperature-dependent magnetic order parameters for LaMn2Si2. The checker extracts transition temperatures T_c1, T_c2, T_c3 from this scan and compares with hidden gold values."
    }
  ],
  "notes": "The checker recomputes transition temperatures from the submitted temperature scans via threshold-crossing detection and validates the phase sequence; no raw gold values are exposed."
}
```

## How you are scored
A hidden verifier reads your submitted CSV files. For LaMn2Ge2 it identifies T_c1 as the temperature where θ reaches 90° while α < 180° and ⟨S⟩ > 0; T_c2 as the temperature where α reaches 180°; and T_c3 as the temperature where ⟨S⟩ drops below a small threshold (≈ 0.01). For LaMn2Si2 the roles of θ and α are swapped: T_c1 is where α reaches 180° while θ < 90°; T_c2 is where θ reaches 90°; T_c3 is again where ⟨S⟩ vanishes. The extracted temperatures are compared to the expected values from the continuous‑MFA calculation with a tolerance that accounts for numerical differences. The verifier also checks that the phase sequence is consistent with the known order (conical → helical → collinear → paramagnetic for Ge; conical → canted → collinear → paramagnetic for Si). The final reward is a weighted combination of the accuracy of the transition temperatures and the correctness of the phase sequence for both compounds. Only the CSV temperature scans are scored; reporting a single number without the full scan will not be accepted.

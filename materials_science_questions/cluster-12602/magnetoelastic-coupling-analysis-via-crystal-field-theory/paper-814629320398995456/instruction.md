# Crystal-field Schottky anomalies and elastic constants in rare-earth antimonides

## Problem background
Rare-earth antimonides (LnSb) exhibit magnetic, elastic, and thermal anomalies in the paramagnetic regime that arise from the crystal-field splitting of the ground-state J multiplet of the rare-earth ion. For compounds that do not undergo a structural or magnetic phase transition (PrSb and TmSb), the Schottky specific heat, Van Vleck susceptibility, and the temperature dependence of the elastic constants can all be described by a single crystal-field Hamiltonian and its strain-derivative expansions. This task aims to reproduce three key theoretical curves — the Schottky specific heat of TmSb, the magnetic susceptibility of PrSb, and the symmetry elastic constants of TmSb — directly from the crystal-field model, without relying on experimental data beyond the published crystal-field parameters. Computing these curves and validating their salient features provides a unified interpretation of the thermodynamic and elastic response.

## Approach
The approach is based on diagonalising an O_h-symmetric crystal-field Hamiltonian for the rare-earth ions using standard Stevens operators. For Tm³⁺ (J=6) and Pr³⁺ (J=4), the published crystal-field parameters A₄⟨r⁴⟩ and A₆⟨r⁶⟩ are used to construct the Hamiltonian matrix. Diagonalisation yields the energy eigenvalues and eigenvectors.
From the TmSb eigenvalues, the partition function Z = Σₙ exp(−Eₙ/kT) is computed and its temperature derivatives give the magnetic specific heat Cₘ(T). For PrSb, the Van Vleck formula χ = kT ∂²/∂H² ln Z is applied to the energy levels in a small applied magnetic field, yielding the inverse susceptibility χ⁻¹(T). For the elastic constants of TmSb, the strain perturbations of the crystal field are expressed in terms of Stevens operators, leading to the magnetoelastic coupling Hamiltonians for the symmetry strains c₄₄ and c₁₁−c₁₂. Second-order perturbation theory provides temperature-dependent strain-susceptibility functions f₂(T) and f₃(T). The isothermal elastic constants are then given by cᵢⱼ = c₀ + c₀ gᵢ² fᵢ(T), using published magnetoelastic coupling constants and constant background elastic constants measured at 200 K. All three calculations are performed on prescribed temperature grids and output as CSV files for independent verification.

## Reproduction target
Produce the following three CSV files:
- `/app/outputs/schottky_tmsb.csv`: Temperature-dependent Schottky specific heat of TmSb from 2 K to 30 K. Columns: `T_K` (ascending), `Cm_J_per_mol_K`.
- `/app/outputs/susceptibility_prsb.csv`: Inverse magnetic susceptibility of PrSb from 2 K to 300 K. Columns: `T_K` (ascending), `chi_inv_per_mol_emu`.
- `/app/outputs/elastic_tmsb.csv`: Symmetry elastic constants of TmSb from 2 K to 100 K. Columns: `T_K` (ascending), `c44_10^11_dyn_per_cm2`, `c11_c12_10^11_dyn_per_cm2`.
The specific-heat curve should exhibit a clear maximum; the inverse susceptibility should become linear at high temperatures with a slope corresponding to the effective magnetic moment; the elastic constants should show characteristic minima/shoulders as functions of temperature. The verifier will extract key features (peak location and magnitude, effective moment from the high-temperature slope, and the positions and relative depths of the elastic‑constant minima) and compare them to independently determined references. The goal is to obtain curves whose salient features agree with those expected from the crystal‑field model, without needing to match any particular experimental dataset.

## Assets

- NumPy: https://pypi.org/project/numpy/
- SciPy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Diagonalize TmSb crystal-field Hamiltonian
- Role: process
- Action: Construct the crystal-field Hamiltonian for O_h symmetry for Tm³⁺ (J=6) using Stevens operators. Use the published crystal-field parameters A4⟨r⁴⟩ = 79.7 K and A6⟨r⁶⟩ = 5.1 K. Diagonalize the matrix to obtain the energy eigenvalues and eigenvectors.
- Evidence: `/app/outputs/tm_energy_levels.npy`

### Step 2: Diagonalize PrSb crystal-field Hamiltonian
- Role: process
- Action: Construct the same crystal-field Hamiltonian for Pr³⁺ (J=4) using the published crystal-field parameters A4⟨r⁴⟩ = 96 K and A6⟨r⁶⟩ = 2.0 K. Diagonalize to obtain the energy eigenvalues and eigenvectors.
- Evidence: `/app/outputs/pr_energy_levels.npy`

### Step 3: Schottky specific heat of TmSb
- Role: scored
- Action: Using the TmSb energy levels, compute the partition function Z = Σₙ exp(−Eₙ/kT) and the magnetic specific heat Cₘ = 2kT ∂/∂T ln Z + kT² ∂²/∂T² ln Z. Evaluate Cₘ on a dense temperature grid from 2 K to 30 K and write the Cₘ(T) curve to schottky_tmsb.csv.
- Output file: `/app/outputs/schottky_tmsb.csv`
- Format: csv
- Contract: Columns: T_K (float, ascending), Cm_J_per_mol_K (float, magnetic specific heat in J/(mol K))
- Scoring: scored by hidden verifier

### Step 4: Van Vleck susceptibility of PrSb
- Role: scored
- Action: Using the PrSb energy levels and eigenvectors, compute the magnetic susceptibility via the Van Vleck formula with a small applied magnetic field. Evaluate the inverse susceptibility χ⁻¹ on a temperature grid from 2 K to 300 K and write the curve to susceptibility_prsb.csv.
- Output file: `/app/outputs/susceptibility_prsb.csv`
- Format: csv
- Contract: Columns: T_K (float, ascending), chi_inv_per_mol_emu (float, inverse susceptibility per mole in emu/mol)
- Scoring: scored by hidden verifier

### Step 5: Strain-susceptibility functions for TmSb
- Role: process
- Action: Using the TmSb energy levels and eigenvectors, construct the magnetoelastic coupling Hamiltonians for the c44 and c11−c12 symmetry strains (expressed in terms of Stevens operators). Apply second-order perturbation theory to compute the temperature-dependent strain-susceptibility functions f₂(T) and f₃(T) that describe the crystal-field contribution to the elastic constants.
- Evidence: `/app/outputs/f2f3_tmsb.csv`

### Step 6: Symmetry elastic constants of TmSb
- Role: scored (load-bearing)
- Action: For TmSb, compute the isothermal elastic constants c44 and c11−c12 as functions of temperature using the strain-susceptibility functions f₂(T), f₃(T) and the relation cᵢⱼ = c₀ + c₀ gᵢ² fᵢ(T). Use the magnetoelastic coupling constants g₂² = 1.2 (mK) and g₃² = 1.4 (mK), and the constant background elastic constants at 200 K: c₀(c44) = 2.68×10¹¹ dyn/cm², c₀(c11−c12) = 13.5×10¹¹ dyn/cm². Evaluate on a grid from 2 K to 100 K and write the curves to elastic_tmsb.csv.
- Output file: `/app/outputs/elastic_tmsb.csv`
- Format: csv
- Contract: Columns: T_K (float, ascending), c44_10^11_dyn_per_cm2 (float), c11_c12_10^11_dyn_per_cm2 (float). Elastic constants in units of 10¹¹ dyn/cm².
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/schottky_tmsb.csv`
- `/app/outputs/susceptibility_prsb.csv`
- `/app/outputs/elastic_tmsb.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### schottky_tmsb.csv
- path: `/app/outputs/schottky_tmsb.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Schottky specific heat of TmSb as a function of temperature. The checker will locate the Cₘ peak (temperature and magnitude) and compare to hidden references.
- schema:
  - `type`: table
  - `required_columns`: `T_K`, `Cm_J_per_mol_K`
  - `units`:
    - `T_K`: K
    - `Cm_J_per_mol_K`: J/(mol K)

### susceptibility_prsb.csv
- path: `/app/outputs/susceptibility_prsb.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Inverse magnetic susceptibility of PrSb as a function of temperature. The checker will fit the high-temperature region and extract the effective magnetic moment, comparing to a hidden reference.
- schema:
  - `type`: table
  - `required_columns`: `T_K`, `chi_inv_per_mol_emu`
  - `units`:
    - `T_K`: K
    - `chi_inv_per_mol_emu`: emu/mol

### elastic_tmsb.csv
- path: `/app/outputs/elastic_tmsb.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Temperature dependence of symmetry elastic constants for TmSb. The checker will locate the minima in c44 and c11−c12, verify their positions and depths against hidden references, and check the shoulder-like shape of c44.
- schema:
  - `type`: table
  - `required_columns`: `T_K`, `c44_10^11_dyn_per_cm2`, `c11_c12_10^11_dyn_per_cm2`
  - `units`:
    - `T_K`: K
    - `c44_10^11_dyn_per_cm2`: 10^11 dyn/cm^2
    - `c11_c12_10^11_dyn_per_cm2`: 10^11 dyn/cm^2

Notes: All temperature values must be strictly ascending. The checker recomputes derived quantities from the raw curves; no self-reported metrics are scored. The elastic constant step is load-bearing: its output depends on the preceding diagonalization and strain-susceptibility steps, which must therefore be genuinely executed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "schottky_tmsb.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "T_K",
          "Cm_J_per_mol_K"
        ],
        "units": {
          "T_K": "K",
          "Cm_J_per_mol_K": "J/(mol K)"
        }
      },
      "description": "Schottky specific heat of TmSb as a function of temperature. The checker will locate the Cₘ peak (temperature and magnitude) and compare to hidden references."
    },
    {
      "file": "susceptibility_prsb.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "T_K",
          "chi_inv_per_mol_emu"
        ],
        "units": {
          "T_K": "K",
          "chi_inv_per_mol_emu": "emu/mol"
        }
      },
      "description": "Inverse magnetic susceptibility of PrSb as a function of temperature. The checker will fit the high-temperature region and extract the effective magnetic moment, comparing to a hidden reference."
    },
    {
      "file": "elastic_tmsb.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "T_K",
          "c44_10^11_dyn_per_cm2",
          "c11_c12_10^11_dyn_per_cm2"
        ],
        "units": {
          "T_K": "K",
          "c44_10^11_dyn_per_cm2": "10^11 dyn/cm^2",
          "c11_c12_10^11_dyn_per_cm2": "10^11 dyn/cm^2"
        }
      },
      "description": "Temperature dependence of symmetry elastic constants for TmSb. The checker will locate the minima in c44 and c11−c12, verify their positions and depths against hidden references, and check the shoulder-like shape of c44."
    }
  ],
  "notes": "All temperature values must be strictly ascending. The checker recomputes derived quantities from the raw curves; no self-reported metrics are scored. The elastic constant step is load-bearing: its output depends on the preceding diagonalization and strain-susceptibility steps, which must therefore be genuinely executed."
}
```

## How you are scored
After you submit the required CSV files, a hidden verifier will read each file, validate its schema and the monotonicity of temperature, and then recompute derived quantities from the raw curves. For `schottky_tmsb.csv`, it will locate the specific-heat peak; for `susceptibility_prsb.csv`, it will fit the high-temperature portion to extract the effective magnetic moment; for `elastic_tmsb.csv`, it will find the positions and depths of the minima in c₄₄ and c₁₁−c₁₂ and check the qualitative shape of the c₄₄ curve. Each of these checks is compared against a reference expectation using predefined tolerances, and the individual scores are combined into a single overall reward between 0 and 1. The verifier does NOT compare your curves to the curves of the original publication; it judges how well your computed results satisfy the physical signatures that the crystal‑field model predicts. Consequently, reporting the expected numerical values without executing the actual computation will not yield a passing score.

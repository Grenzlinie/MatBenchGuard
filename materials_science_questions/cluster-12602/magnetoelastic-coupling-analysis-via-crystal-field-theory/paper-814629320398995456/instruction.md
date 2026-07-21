# Crystal-field Schottky anomalies and elastic constants in rare-earth antimonides

## Problem background
Rare-earth antimonides (LnSb) exhibit magnetic, elastic, and thermal anomalies in the paramagnetic regime that arise from the crystal-field splitting of the ground-state J multiplet of the rare-earth ion. For compounds that do not undergo a structural or magnetic phase transition (PrSb and TmSb), the Schottky specific heat, Van Vleck susceptibility, and the temperature dependence of the elastic constants can all be described by a single crystal-field Hamiltonian and its strain-derivative expansions. This task aims to reproduce three key theoretical curves — the Schottky specific heat of TmSb, the magnetic susceptibility of PrSb, and the symmetry elastic constants of TmSb — directly from the crystal-field model, without relying on experimental data beyond the published crystal-field parameters. Computing these curves and validating their salient features provides a unified interpretation of the thermodynamic and elastic response.

## Approach
The approach is based on diagonalising an O_h-symmetric crystal-field Hamiltonian for the rare-earth ions using standard Stevens operators. For Tm³⁺ (J=6) and Pr³⁺ (J=4), the published crystal-field parameters A₄⟨r⁴⟩ and A₆⟨r⁶⟩ are used to construct the Hamiltonian matrix. Diagonalisation yields the energy eigenvalues and eigenvectors.
From the TmSb eigenvalues, the partition function Z = Σₙ exp(−Eₙ/kT) is computed and its temperature derivatives give the magnetic specific heat Cₘ(T). For PrSb, the Van Vleck formula χ = kT ∂²/∂H² ln Z is applied to the energy levels in a small applied magnetic field, yielding the inverse susceptibility χ⁻¹(T). For the elastic constants of TmSb, the strain perturbations of the crystal field are expressed in terms of Stevens operators, leading to the magnetoelastic coupling Hamiltonians for the symmetry strains c₄₄ and c₁₁−c₁₂. Second-order perturbation theory provides temperature-dependent strain-susceptibility functions f₂(T) and f₃(T). The isothermal elastic constants are then given by cᵢⱼ = c₀ + c₀ gᵢ² fᵢ(T), using published magnetoelastic coupling constants and constant background elastic constants measured at 200 K. All three calculations are performed on prescribed temperature grids and output as CSV files for independent verification.

## Physical constants and operator definitions
Use the cgs (Gaussian) system throughout, which is consistent with the paper. The following quantities are required for the calculations. They are provided here so that every agent can reproduce the results without guessing.

**Fundamental constants:**
- Boltzmann constant: k_B = 1.380649 × 10⁻¹⁶ erg K⁻¹
- Avogadro number: N_A = 6.02214076 × 10²³ mol⁻¹
- Bohr magneton: μ_B = 9.274009994 × 10⁻²¹ erg G⁻¹

**Ion-specific data:**
- Pr³⁺ (4f², ³H₄), J = 4, Landé g‑factor g_J = 4/5.
- Tm³⁺ (4f¹², ³H₆), J = 6.
- Crystal‑field parameters (paper Table I):
  - PrSb: A₄⟨r⁴⟩ = 96 K,   A₆⟨r⁶⟩ = 2.0 K.
  - TmSb: A₄⟨r⁴⟩ = 79.7 K, A₆⟨r⁶⟩ = 5.1 K.

**Angular momentum matrices:**
For a given J, construct the (2J+1)×(2J+1) matrices:
- J_z = diag(m) with m = −J, −J+1, …, J.
- J_± = matrices with elements (J_±)_{m±1, m} = √[J(J+1) − m(m±1)].
- J_x = (J_+ + J_−)/2,   J_y = (J_+ − J_−)/(2i).

**Stevens operators relevant to the task:**
For arbitrary J,
- O₂⁰ = 3 J_z² − J(J+1) I
- O₂² = J_x² − J_y² = (J_+² + J_−²)/2

The crystal‑field Hamiltonian in O_h symmetry is (paper Eq. 1):
H_CF = W [ x (O₄⁰ + 5 O₄⁴) / F₄  +  (1 − |x|) (O₆⁰ − 21 O₆⁴) / F₆ ]

where O₄⁰, O₄⁴, O₆⁰, O₆⁴ are the standard Stevens operators (as used, e.g., in Lea‑Leask‑Wolf parametrisation). The parameters W, x, F₄, F₆ can be found from the published A₄⟨r⁴⟩, A₆⟨r⁶⟩ using the relations given in the Lea‑Leask‑Wolf paper [J. Phys. C 1, 1691 (1968)]; alternatively you may directly construct H_CF as
H_CF = A₄⟨r⁴⟩ β_J (O₄⁰ + 5 O₄⁴) + A₆⟨r⁶⟩ γ_J (O₆⁰ − 21 O₆⁴)
where β_J and γ_J are the appropriate Stevens multiplicative factors. For a self‑contained calculation, use the explicit full‑matrix forms of the operators (e.g., Appendix of the Lea‑Leask‑Wolf paper) with the given A₄⟨r⁴⟩ and A₆⟨r⁶⟩ and the corresponding β,γ parameters for the ground multiplet.

## Reproduction target
Produce the following three CSV files:
- `/app/outputs/schottky_tmsb.csv`: Temperature-dependent Schottky specific heat of TmSb from 2 K to 30 K. Columns: `T_K` (ascending), `Cm_J_per_mol_K`.
- `/app/outputs/susceptibility_prsb.csv`: Inverse magnetic susceptibility of PrSb from 2 K to 300 K. Columns: `T_K` (ascending), `chi_inv_per_mol_emu`.
- `/app/outputs/elastic_tmsb.csv`: Symmetry elastic constants of TmSb from 2 K to 100 K. Columns: `T_K` (ascending), `c44_10^11_dyn_per_cm2`, `c11_c12_10^11_dyn_per_cm2`.
The specific-heat curve should exhibit a clear maximum; the inverse susceptibility should become linear at high temperatures with a slope corresponding to the effective magnetic moment; the elastic constants should show characteristic minima/shoulders as functions of temperature. The verifier will extract key features (peak location and magnitude, effective moment from the high-temperature slope, and the positions and relative depths of the elastic‑constant minima) and compare them to independently determined references. The goal is to obtain curves whose salient features agree with those expected from the crystal‑field model, without needing to match any particular experimental dataset.

## Assets

- NumPy: https://pypi.org/project/numpy/
- SciPy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Diagonalize TmSb crystal-field Hamiltonian
- Role: process
- Action: Construct the O_h crystal-field Hamiltonian for Tm³⁺ (J=6) using A₄⟨r⁴⟩ = 79.7 K and A₆⟨r⁶⟩ = 5.1 K (see “Physical constants” for the explicit matrix construction). Diagonalize and obtain energy eigenvalues and eigenvectors.
- Evidence: `/app/outputs/tm_energy_levels.npy`

### Step 2: Diagonalize PrSb crystal-field Hamiltonian
- Role: process
- Action: Construct the same O_h crystal-field Hamiltonian for Pr³⁺ (J=4) using A₄⟨r⁴⟩ = 96 K and A₆⟨r⁶⟩ = 2.0 K. Diagonalize to obtain energy eigenvalues and eigenvectors.
- Evidence: `/app/outputs/pr_energy_levels.npy`

### Step 3: Schottky specific heat of TmSb
- Role: scored
- Action: Using the TmSb energy levels, compute the partition function Z = Σₙ exp(−Eₙ/k_B T) (with k_B = 1.380649e‑16 erg K⁻¹, but note that the specific heat must be reported in J mol⁻¹ K⁻¹; 1 erg = 1e‑7 J). Evaluate the magnetic specific heat per mole, Cₘ, via
  Cₘ = 2 k_B T ∂/∂T ln Z + k_B T² ∂²/∂T² ln Z   (paper Eq. 2)
  on a dense temperature grid from 2 K to 30 K. Write the Cₘ(T) curve to schottky_tmsb.csv.
- Output file: `/app/outputs/schottky_tmsb.csv`
- Format: csv
- Contract: Columns: T_K (float, ascending), Cm_J_per_mol_K (float, magnetic specific heat in J/(mol K))
- Scoring: scored by hidden verifier

### Step 4: Van Vleck susceptibility of PrSb
- Role: scored
- Action: For Pr³⁺ (J=4, g_J = 4/5), add a Zeeman term H_Z = g_J μ_B H J_z (field along z) to the crystal‑field Hamiltonian. For a very small field H (e.g., 1 Oe), diagonalize to obtain eigenenergies E_n(H) at each temperature. The isothermal magnetic susceptibility per mole is
  χ = k_B T ∂²/∂H² ln Z ∣_{H→0},   Z = Σₙ exp(−E_n(H)/k_B T).
  Numerically, this may be evaluated by computing Z at three tiny field values (e.g., −δ, 0, +δ) and using finite differences, or by the standard Van Vleck formula in the basis of the zero‑field states:
  χ(T) = (N_A (g_J μ_B)² / k_B) × S(T)
  where
    S(T) = (1/Z) Σ_i |⟨i|J_z|i⟩|^2 e^{−E_i / k_B T}
           + (2/Z) Σ_{i≠j} |⟨i|J_z|j⟩|^2   (k_B T / (E_j−E_i)) (e^{−E_i/k_B T} − e^{−E_j/k_B T}).
  The result is in emu mol⁻¹ (cgs). Compute the inverse susceptibility χ⁻¹ and write it on a grid from 2 K to 300 K.
- Output file: `/app/outputs/susceptibility_prsb.csv`
- Format: csv
- Contract: Columns: T_K (float, ascending), chi_inv_per_mol_emu (float, inverse susceptibility per mole in emu/mol)
- Scoring: scored by hidden verifier

### Step 5: Strain-susceptibility functions for TmSb
- Role: process
- Action: Using the TmSb zero‑field energies |i⟩ and energies E_i, construct the magnetoelastic (quadrupole) operators:
  - For c₄₄ mode: Q_xy = J_x J_y + J_y J_x
  - For c₁₁−c₁₂ mode: Q_θ = J_x² − J_y²   (this is the Stevens operator O₂²)
  Evaluate the temperature‑dependent strain‑susceptibility functions f_Γ(T) (Γ = 2,3) as
    f_Γ(T) = − 1/(k_B T) ( ⟨Q_Γ²⟩ − ⟨Q_Γ⟩² )
             − 2 Σ_{i≠j} |⟨i|Q_Γ|j⟩|^2 (p_i − p_j) / (E_j − E_i)
  where p_i = e^{−E_i/k_B T} / Z and ⟨Q_Γ⟩ = Σ_i ⟨i|Q_Γ|i⟩ p_i, ⟨Q_Γ²⟩ = Σ_i |⟨i|Q_Γ|i⟩|^2 p_i.
  (The equal‑energy limit i=j is automatically included in the first term.)
  Compute f₂(T) (from Q_θ) and f₃(T) (from Q_xy) on the temperature grid that will be used for the elastic constants (2 K to 100 K). Save both f₂ and f₃ together with temperature.
- Evidence: `/app/outputs/f2f3_tmsb.csv`

### Step 6: Symmetry elastic constants of TmSb
- Role: scored (load-bearing)
- Action: The isothermal elastic constants in units of 10¹¹ dyn cm⁻² are given by (paper Eq. 7)
    c₄₄(T) = c₀(c₄₄) × [ 1 + g₃² f₃(T) ]
    c₁₁−c₁₂(T) = c₀(c₁₁−c₁₂) × [ 1 + g₂² f₂(T) ]
  where the background elastic constants at 200 K are
    c₀(c₄₄) = 2.68 × 10¹¹ dyn cm⁻²,
    c₀(c₁₁−c₁₂) = 13.5 × 10¹¹ dyn cm⁻²,
  and the magnetoelastic coupling constants (paper ‑ expressed in mK) must be converted to kelvin:
    g₂² = 1.2 mK = 1.2 × 10⁻³ K,
    g₃² = 1.4 mK = 1.4 × 10⁻³ K.
  With f₂, f₃ obtained from step 5 (units of K⁻¹), the products g² f are dimensionless, so the elastic constants retain the units 10¹¹ dyn cm⁻². Evaluate on a grid from 2 K to 100 K and write the curves to elastic_tmsb.csv.
- Output file: `/app/outputs/elastic_tmsb.csv`
- Format: csv
- Contract: Columns: T_K (float, ascending), c44_10^11_dyn_per_cm2 (float), c11_c12_10^11_dyn_per_cm2 (float). Elastic constants in units of 10¹¹ dyn/cm².
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
    - `Cm_J_per_mol_K`: J/(mol K)

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
    },
    {
      "file": "f2f3_tmsb.csv",
      "format": "csv",
      "purpose": "process",
      "target_policy": "ignore",
      "schema": {
        "type": "table",
        "required_columns": [
          "T_K",
          "f2",
          "f3"
        ]
      },
      "description": "Temperature-dependent strain‑susceptibility functions f2(T) and f3(T) for TmSb (intermediate product)."
    },
    {
      "file": "pr_energy_levels.npy",
      "format": "npy",
      "purpose": "process",
      "target_policy": "ignore",
      "schema": {},
      "description": "Crystal‑field energy levels of PrSb (intermediate product)."
    },
    {
      "file": "tm_energy_levels.npy",
      "format": "npy",
      "purpose": "process",
      "target_policy": "ignore",
      "schema": {},
      "description": "Crystal‑field energy levels of TmSb (intermediate product)."
    }
  ],
  "notes": "All temperature values must be strictly ascending. The checker recomputes derived quantities from the raw curves; no self-reported metrics are scored. The elastic constant step is load-bearing: its output depends on the preceding diagonalization and strain-susceptibility steps, which must therefore be genuinely executed."
}
```

## How you are scored
After you submit the required CSV files, a hidden verifier will read each file, validate its schema and the monotonicity of temperature, and then recompute derived quantities from the raw curves. For `schottky_tmsb.csv`, it will locate the specific-heat peak; for `susceptibility_prsb.csv`, it will fit the high-temperature portion to extract the effective magnetic moment; for `elastic_tmsb.csv`, it will find the positions and depths of the minima in c₄₄ and c₁₁−c₁₂ and check the qualitative shape of the c₄₄ curve. Each of these checks is compared against a reference expectation using predefined tolerances, and the individual scores are combined into a single overall reward between 0 and 1. The verifier does NOT compare your curves to the curves of the original publication; it judges how well your computed results satisfy the physical signatures that the crystal‑field model predicts. Consequently, reporting the expected numerical values without executing the actual computation will not yield a passing score.
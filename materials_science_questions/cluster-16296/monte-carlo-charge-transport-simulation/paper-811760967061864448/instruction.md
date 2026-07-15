# Sequential Tunneling Transport in AlAs/GaAs Double-Barrier Diodes

## Problem background
AlAs/GaAs/AlAs double‑barrier resonant‑tunneling diodes exhibit negative differential conductivity that is commonly modelled using a sequential‑tunneling picture. In this picture, the peak current and the average electron dwell time in the quantum well depend on the transmission probabilities of the emitter and collector barriers. When the collector barrier is relatively thick (>3 nm), calculations that consider only Γ‑valley tunneling through the AlAs barriers predict a much smaller current and a much longer dwell time than are actually measured. This discrepancy has been attributed to an additional tunneling channel via the lower‑energy X‑valley states in the AlAs barriers, with the branching ratio between Γ and X channels serving as the key unknown parameter. This task asks you to compute the peak current and dwell time for four specific AlAs/GaAs/AlAs double‑barrier diodes under two contrasting assumptions—Γ‑valley tunneling alone, and a hybrid Γ‑plus‑X model with a proposed branching ratio—so that the impact of the X‑valley channel can be quantified.

## Approach
The transport is described by a sequential‑tunneling model. First, the one‑dimensional band profile is solved self‑consistently by Poisson’s equation under the applied forward bias, giving the voltage drops across the emitter barrier (V_eb), the quantum well (V_w), and the collector barrier (V_cb). Next, the lowest bound‑state energy E0 in the GaAs quantum well is obtained from the time‑independent Schrödinger equation at zero bias, ignoring Stark shifts. The resonant electron energy is then E_z = E0 − e V_eb − e V_w/2, and the Fermi level E_F in the emitter spacer is computed from the doping density using an appropriate degeneracy approximation.

The barrier transmission is evaluated with the following Wentzel–Kramers–Brillouin (WKB) formula that includes a prefactor and an energy‑dependent effective mass:

T(E, V_b) = (16 r √(E (E + e V_b) (V₀ − E₀))) / [((V₀ − E₀) r + E) ((V₀ − E₀) r + E + e V_b)] × exp(−2 ∫₀^{L_b} k_b(z) dz) ,

where
- V₀ is the barrier height (1.05 eV for Γ‑valley; 0.2 eV for X‑valley),
- E₀ is the well bound‑state energy (from Schrödinger solver),
- r = m_b / m₀, with m_b the effective mass of the tunnelling electron in the barrier and m₀ the free‑electron mass,
- L_b is the barrier thickness,
- k_b(z) = √(2 m_b (V₀ − E − e V_b · z / L_b)) / ℏ is the perpendicular wave vector in the barrier,
- e is the elementary charge,
- ℏ is the reduced Planck constant.

The prefactor uses (V₀ − E₀) rather than (V₀ − E) to capture the flat‑band limit correction. Two valleys are considered:
- **Γ valley**: barrier height V₀ = 1.05 eV, effective mass at the AlAs Γ‑conduction‑band edge m_Γ(edge) = 0.15 m₀, energy‑dependence parameter E_w = ℏ² / (2 m_Γ(edge) γ) with γ = 9.8×10⁻²⁰ m², giving a running mass m_Γ(E) = m_Γ(edge) [1 − (V₀ − E) / E_w]. Use this running mass for both r and the integral.
- **X valley**: barrier height V₀ = ΔE_XΓ = 0.2 eV, constant effective mass m_b = m_Xt = 0.2 m₀ (transverse X‑valley mass).

For each diode, the WKB formula yields emitter and collector transmission probabilities T_Γ and T_X at energy E_z and the relevant voltage drop. The effective collector transmission is then built in two ways:
(a) **Γ‑only model**: T_c_eff = T_c_Γ.
(b) **Γ+X model**: T_c_eff = (1 − c_ΓX) T_c_Γ + c_ΓX T_c_X with c_ΓX = 1×10⁻⁴.

The peak current density J is computed from
J ∝ (E_F − E_z) × (T_e T_c_eff) / (T_e + T_c_eff),
and the corresponding dwell time from
τ ∝ 1 / T_c_eff.

These expressions are applied to all four diodes (S1, A1, A2, S2) under forward bias, with the diode‑specific parameters (barrier thicknesses, doping densities, peak bias voltages) as listed in the workflow steps. The results for both models are collected in a single CSV file.

## Reproduction target
For the four diodes S1, A1, A2, S2, compute the peak forward‑bias tunneling current (in amperes) and the corresponding electron dwell time (in seconds) under two models:
(a) Γ‑only tunneling — T_c_eff = T_c_Γ.
(b) Γ+X tunneling — T_c_eff = (1 − c_ΓX) T_c_Γ + c_ΓX T_c_X, with c_ΓX = 1×10⁻⁴.

Use the diode parameters (barrier thicknesses, doping, forward bias voltages) specified in the workflow. Produce a single CSV file, `/app/outputs/computed_results.csv`, containing eight rows (4 diodes × 2 models) with columns:
- `diode` (string): one of S1, A1, A2, S2.
- `model` (string): one of `Gamma_only` or `Gamma_plus_X`.
- `peak_current_A` (float): the peak forward‑bias current in amperes.
- `dwell_time_s` (float): the dwell time in seconds.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Solve band profile and voltage drops
- Role: process
- Action: For each diode (S1, A1, A2, S2) under forward bias, solve the 1D Poisson equation for the double-barrier structure using the doping densities and barrier thicknesses from the diode parameters. Obtain the potential profile and extract the voltage drops across the emitter barrier (V_eb), the quantum well (V_w), and the collector barrier (V_cb). Use the Boltzmann approximation for the mobile charge and ignore quantization.
- Evidence: `/app/outputs/band_drops.json`

### Step 2: Compute well bound-state energy
- Role: process
- Action: Solve the time-independent Schrödinger equation for a 5.1 nm GaAs quantum well between semi-infinite AlAs barriers (zero bias) to obtain the first electron subband energy E0 (eV) relative to the GaAs conduction-band edge. Use electron effective mass m* = 0.067 m0 in GaAs and an AlAs Γ barrier height of 1.05 eV. Ignore Stark shift due to bias.
- Evidence: `/app/outputs/E0.txt`

### Step 3: Determine resonant energy and Fermi level
- Role: process
- Action: For each diode, compute the resonant electron energy E_z = E0 - eV_eb - eV_w/2 using the obtained voltage drops. Compute the Fermi level E_F in the emitter spacer layer from the doping density N_D using an appropriate degeneracy approximation (e.g., Fermi-Dirac integral for degenerate doping).
- Evidence: none

### Step 4: Calculate peak current and dwell time
- Role: scored (load-bearing)
- Action: Implement the WKB single-barrier transmission formula (including a prefactor and an energy-dependent effective mass) for Γ-valley and X-valley states in AlAs barriers. For each diode, compute the transmission probabilities T_Γ and T_X for both emitter and collector barriers at energy E_z and corresponding voltage drops. Use material parameters (Γ barrier height, X-valley effective mass, etc.) as specified. For the collector barrier, compute the effective transmission: (a) Γ-only model: T_c_eff = T_c_Γ; (b) Γ+X model: T_c_eff = (1 - c_ΓX) T_c_Γ + c_ΓX T_c_X with branching ratio c_ΓX = 1×10⁻⁴. Then compute the peak current using the sequential tunneling current formula and the dwell time formula. Write a CSV file with rows for all four diodes (S1, A1, A2, S2) under both the Γ-only and Γ+X models, containing columns: diode (string), model (string, 'Gamma_only' or 'Gamma_plus_X'), peak_current_A (float, amperes), dwell_time_s (float, seconds).
- Output file: `/app/outputs/computed_results.csv`
- Format: csv
- Contract: Columns: diode (S1/A1/A2/S2), model (Gamma_only/Gamma_plus_X), peak_current_A (float), dwell_time_s (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_results.csv
- path: `/app/outputs/computed_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Table of peak currents (A) and dwell times (s) for diodes S1, A1, A2, S2 under Γ-only and Γ+X tunneling models.
- schema:
  - `type`: table
  - `required_columns`: `diode`, `model`, `peak_current_A`, `dwell_time_s`

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "diode",
          "model",
          "peak_current_A",
          "dwell_time_s"
        ]
      },
      "description": "Table of peak currents (A) and dwell times (s) for diodes S1, A1, A2, S2 under Γ-only and Γ+X tunneling models."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier reads your `computed_results.csv` and compares each numerical entry (peak_current_A and dwell_time_s) to independently established reference values. The comparison uses a combination of relative and absolute tolerances that absorb legitimate numerical differences from different implementations while rejecting coarse guesses. Additionally, the verifier checks the following structural condition: for the thick‑barrier diodes A1, A2, and S2, the dwell time computed in the Γ‑only model must be at least a factor of 10 larger than the dwell time computed in the Γ+X model. The final reward is the fraction of numerical entries that lie within the tolerance, with a bonus for satisfying the structural constraint. You are scored solely on the contents of that CSV; the intermediate evidence files are not directly scored but may be inspected by the verifier as an audit.

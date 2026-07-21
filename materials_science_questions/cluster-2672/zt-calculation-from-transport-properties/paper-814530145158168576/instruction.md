# ZT Calculation for n-Type Bi2Te2.7Se0.3 with Minority-Carrier Blocking

## Problem background
Thermoelectric materials convert heat to electricity, and their efficiency is governed by the dimensionless figure of merit ZT = S²σT/(κ_elec+κ_lat). In narrow-band-gap semiconductors, both electrons and holes participate in conduction (bipolar transport), which reduces the Seebeck coefficient and increases the thermal conductivity, thereby limiting ZT. One proposed strategy to mitigate this bipolar effect is minority carrier blocking: heterostructure barriers are introduced that block the minority carriers while leaving majority carrier transport largely unaffected. This work investigates the impact of such barriers on the thermoelectric performance of n-type Bi₂Te₂.₇Se₀.₃, computing the figure of merit as a function of electron concentration at 500 K both with and without barriers.

## Approach
The thermoelectric transport is described by near-equilibrium Boltzmann transport equations under the relaxation time approximation. A multiband nonparabolic band model (modified Kane model) is used for the conduction and valence bands of the material. Carrier scattering is dominated by acoustic phonon deformation potential and ionized impurity scattering, with energy-dependent relaxation times derived from material parameters. The model accounts for two-carrier (electron and hole) transport, including the bipolar contribution to electronic thermal conductivity. For the barrier case, a one-sided heterostructure barrier is assumed: the valence band (minority carrier hole band) is modified by a barrier of height 10 k_B T and width 20 nm, whose transmission coefficient is computed via the WKB approximation; the conduction band (majority carrier electron band) has perfect transmission. The lattice thermal conductivity is fixed at 0.5 W m⁻¹ K⁻¹. For each electron concentration, the Fermi level is solved self-consistently, and the electrical conductivity, Seebeck coefficient, electronic thermal conductivity, and finally ZT are evaluated. The bulk case (no barriers, transmission = 1 in all bands) serves as the baseline comparison.

## Reproduction target
Compute the thermoelectric figure of merit ZT for n-type Bi₂Te₂.₇Se₀.₃ at 500 K as a function of electron concentration, spanning a range from 1×10¹⁸ to 1×10²¹ cm⁻³. Produce a single CSV file containing ZT values for both the bulk (no barrier) case and the minority‑carrier blocking case. The CSV must have columns: electron_concentration_cm3 (float, units cm⁻³), zT_bulk (float, dimensionless), and zT_barrier (float, dimensionless). For each condition, also identify the maximum ZT and the corresponding electron concentration (these can be noted in a separate output or extracted from the CSV).

## Material parameters

All parameters are for n-type Bi₂Te₂.₇Se₀.₃ (x = 0.3) at T = 500 K. Effective masses are single‑valley values; the valley degeneracy is 6 for all bands.

**Band structure**
- Band gap E_g = 0.183 eV
- Offset 1st → 2nd conduction band = 0.23 eV
- Offset 1st → 2nd valence band = 0.27 eV
- Electron effective mass (1st CB) m₁ᶜ = 0.2147 m₀
- Electron effective mass (2nd CB) m₂ᶜ = 0.2247 m₀
- Hole effective mass (1st VB) m₁ᵛ = 0.3936 m₀
- Hole effective mass (2nd VB) m₂ᵛ = 0.3936 m₀
- Non‑parabolicity α (1st CB) = 0 eV⁻¹
- α (2nd CB) = 1.0 eV⁻¹
- α (1st VB) = 0.6 eV⁻¹
- α (2nd VB) = 2.0 eV⁻¹

**Scattering** (acoustic phonon deformation potential + ionized impurity)
- Acoustic deformation potential for electrons Dₐ,ₑ = 19.0 eV
- Acoustic deformation potential for holes Dₐ,ₕ = 23.7 eV
- Elastic constant Cₗ = 7.1 × 10¹⁰ N m⁻²
- Compensation ratio r_c = 1 → N_II = r_c × n (for n‑type)

**Lattice thermal conductivity**
- κₗₐₜ = 0.5 W m⁻¹ K⁻¹

**Minority‑carrier blocking barrier** (only in valence band)
- Barrier height E_B = 10 k_B T ≈ 0.431 eV (500 K)
- Barrier width w_B = 20 nm
- Conduction band transmission T_B(E) ≡ 1
- Valence band transmission T_B(E) computed by the WKB formula (Eq. (7) of the reference).

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute ZT vs electron concentration
- Role: scored
- Action: Implement the near-equilibrium Boltzmann transport model for n-type Bi₂Te₂.₇Se₀.₃ at 500 K using the material parameters listed in the **Material parameters** section. Solve for the Fermi level self-consistently at each electron concentration. Compute electrical conductivity, Seebeck coefficient, electronic thermal conductivity (including bipolar term) with and without minority-carrier blocking barriers (WKB transmission). Barrier case: valence band transmission coefficient with height 10 k_B T and width 20 nm; conduction band transmission = 1. Assume lattice thermal conductivity κ_lat = 0.5 W m⁻¹ K⁻¹. Compute zT = S²σT/(κ_elec+κ_lat). Output a CSV file with columns: electron_concentration_cm3, zT_bulk, zT_barrier for a logarithmically spaced concentration array from 1×10¹⁸ to 1×10²¹ cm⁻³.
- Output file: `/app/outputs/zT_output.csv`
- Format: csv
- Contract: Columns: electron_concentration_cm3 (float, units cm⁻³), zT_bulk (float, dimensionless), zT_barrier (float, dimensionless). Each row corresponds to a concentration value. Header must be present.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/zT_output.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### zT_output.csv
- path: `/app/outputs/zT_output.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: CSV table of zT values as a function of electron concentration for n-type Bi2Te2.7Se0.3 at 500 K, for both bulk and barrier cases. The hidden checker compares these values against reference values derived from the paper's computations with tolerance for numerical differences.
- schema:
  - `type`: table
  - `required_columns`: `electron_concentration_cm3`, `zT_bulk`, `zT_barrier`
  - `units`:
    - `electron_concentration_cm3`: cm⁻³
    - `zT_bulk`: dimensionless
    - `zT_barrier`: dimensionless

Notes: Checker will compare the reported zT values at a set of electron concentration points against hidden reference values. Additional check on peak zT meeting or exceeding the paper-reported level is included.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "zT_output.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "electron_concentration_cm3",
          "zT_bulk",
          "zT_barrier"
        ],
        "units": {
          "electron_concentration_cm3": "cm⁻³",
          "zT_bulk": "dimensionless",
          "zT_barrier": "dimensionless"
        }
      },
      "description": "CSV table of zT values as a function of electron concentration for n-type Bi2Te2.7Se0.3 at 500 K, for both bulk and barrier cases. The hidden checker compares these values against reference values derived from the paper's computations with tolerance for numerical differences."
    }
  ],
  "notes": "Checker will compare the reported zT values at a set of electron concentration points against hidden reference values. Additional check on peak zT meeting or exceeding the paper-reported level is included."
}
```

## How you are scored
Your submission is evaluated by an automated hidden verifier. The verifier reads your zT_output.csv and compares the reported zT_bulk and zT_barrier values at a set of selected electron concentration points against reference values that are derived from the paper’s transport computations. It additionally checks that the maximum ZT values and the concentrations at which they occur are correct. Scoring is based on the agreement between your computed results and the reference across these checks; simply reporting the expected numbers without implementing the underlying model will not succeed. The reward is a weighted combination of the CSV accuracy and the peak‑specific comparisons.

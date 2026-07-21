# Extended Hubbard Model: Two-Pole Approximation for Normal and Superconducting Properties

## Problem background
Understanding the normal-state electronic structure and the superconducting properties of strongly correlated electron systems is a central problem in condensed-matter physics. A particularly important question is how antiferromagnetic correlations influence the Fermi surface, giving rise to phenomena such as hole pockets and a pseudogap, and how they affect the temperature dependence of the superconducting gap, possibly leading to deviations from standard BCS behavior. This task explores these questions in a framework that combines short-range Coulomb repulsion with an effective attractive nearest-neighbor interaction, producing a rich phase competition between magnetism and d-wave superconductivity.

## Approach
The computations use the two-pole approximation applied to a two-dimensional extended Hubbard model. The model includes first- and second-neighbor hopping and an attractive non-local interaction (U < 0). The approach constructs the one-particle Green's function from a chosen set of operator excitations, leading to two quasiparticle bands and a spectral function that encode correlation-induced renormalizations. For the superconducting state, the d-wave gap equation is derived from the anomalous Green's function and solved self-consistently together with the correlation functions. The workflow therefore requires iterative numerical solutions: first, a self-consistent normal-state calculation to obtain the band shift, correlation functions, and chemical potential; then, from the converged normal solution, a temperature scan of the superconducting gap equation to obtain the gap amplitude Δ(T).

## Reproduction target
Reproduce two sets of results. 1) Normal state for doping δ = 0.20 (n_T = 0.80): compute the spectral function A(k,ω=0) on a uniform k-mesh covering the first Brillouin zone, and extract the two quasiparticle band dispersions ω₁(k) and ω₂(k) along the high-symmetry path Γ–X–M–Γ, all with model parameters t = -1.0 eV, t₂ = 0.3|t|, U = -8t. 2) Superconducting state for filling n_T = 0.90 (δ = 0.10) and U = -8t: compute the d-wave gap amplitude Δ as a function of temperature over a range that spans from near zero up to above the critical temperature T_c, and report the resulting Δ(T) curve. From this curve, the verifier will extract the zero-temperature gap Δ₀, the critical temperature T_c, and the low-temperature gap behavior (specifically, whether Δ exhibits an increase above its T→0 value at low temperatures).

## Assets

- Python scientific computing packages: numpy scipy matplotlib

## Workflow steps

### Step 1: Normal-state self-consistent solution (δ=0.20)
- Role: process
- Action: Implement the two-pole approximation self-consistent equations for the normal state of the extended Hubbard model with parameters t=-1.0 eV, t2=0.3|t|, U=-8t, and doping δ=0.20. Solve iteratively for the chemical potential μ, correlation functions (n_{ijσ}, m_{ijσ}, spin-spin correlations), band shift W_{kσ}, and the quasiparticle energies ω₁(k), ω₂(k) and spectral function A(k,ω).
- Evidence: `/app/outputs/normal_sc_convergence.log`

### Step 2: Normal spectral function A(k,ω=0)
- Role: scored
- Action: From the converged normal-state solution, compute the spectral function A(k,ω=0) on a uniform grid of k-points covering the first Brillouin zone. Save the data.
- Output file: `/app/outputs/normal_spectral_function.csv`
- Format: csv
- Contract: columns: kx (float, 1/Å), ky (float, 1/Å), A (float, spectral weight at ω=0)
- Scoring: scored by hidden verifier

### Step 3: Quasiparticle band energies
- Role: scored
- Action: From the converged normal-state solution, extract the two quasiparticle band energies ω₁ and ω₂ along the high-symmetry path Γ–X–M–Γ. Save the data.
- Output file: `/app/outputs/quasiparticle_bands.csv`
- Format: csv
- Contract: columns: kx (float, 1/Å), ky (float, 1/Å), omega1 (float, eV), omega2 (float, eV)
- Scoring: scored by hidden verifier

### Step 4: Superconducting self-consistent gap calculation for n_T=0.90
- Role: process
- Action: Implement the two-pole approximation equations for the superconducting state of the Hubbard model with n_T=0.90, U=-8t, t=-1.0 eV, t2=0.3|t|. Using a normal-state solution at that filling as initial guess, solve the d-wave gap equation self-consistently for a series of temperatures from near zero to above the critical temperature T_c. Record the converged gap amplitude Δ at each temperature.
- Evidence: `/app/outputs/sc_loop.log`

### Step 5: Superconducting gap Δ(T)
- Role: scored (load-bearing)
- Action: From the temperature series of converged gap amplitudes, extract the gap Δ as a function of temperature. Save the Δ(T) data.
- Output file: `/app/outputs/gap_vs_temperature.csv`
- Format: csv
- Contract: columns: T (float, reduced temperature k_B T/|t|, dimensionless), Delta (float, gap amplitude in eV)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/normal_spectral_function.csv`
- `/app/outputs/quasiparticle_bands.csv`
- `/app/outputs/gap_vs_temperature.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### normal_spectral_function.csv
- path: `/app/outputs/normal_spectral_function.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Spectral function A(k,ω=0) on a grid; structural audit checks for a hole pocket around (π/2,π/2) and a pseudogap near (0,π).
- schema:
  - `type`: table
  - `required_columns`: `kx`, `ky`, `A`
  - `items`: object
  - `required`: object
  - `units`:
    - `kx`: 1/Å
    - `ky`: 1/Å
    - `A`: dimensionless spectral weight

### quasiparticle_bands.csv
- path: `/app/outputs/quasiparticle_bands.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Quasiparticle band energies along Γ–X–M–Γ; structural audit checks for band crossing near (π/2,π/2) and a gap near (0,π).
- schema:
  - `type`: table
  - `required_columns`: `kx`, `ky`, `omega1`, `omega2`
  - `items`: object
  - `required`: object
  - `units`:
    - `kx`: 1/Å
    - `ky`: 1/Å
    - `omega1`: eV
    - `omega2`: eV

### gap_vs_temperature.csv
- path: `/app/outputs/gap_vs_temperature.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Superconducting gap amplitude vs temperature. Checker extracts Δ₀ and T_c and compares them to the paper's hidden reference values within tolerances; also verifies the existence of a low-temperature upturn (Δ_max > Δ₀).
- schema:
  - `type`: table
  - `required_columns`: `T`, `Delta`
  - `items`: object
  - `required`: object
  - `units`:
    - `T`: k_B T/|t|
    - `Delta`: eV

Notes: The hidden checker will perform structural audit on the spectral function and bands, and a result-level comparison on the gap data (recomputing Δ₀ and T_c from the submitted CSV and comparing against the paper's reported numbers).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "normal_spectral_function.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "kx",
          "ky",
          "A"
        ],
        "items": {},
        "required": {},
        "units": {
          "kx": "1/Å",
          "ky": "1/Å",
          "A": "dimensionless spectral weight"
        }
      },
      "description": "Spectral function A(k,ω=0) on a grid; structural audit checks for a hole pocket around (π/2,π/2) and a pseudogap near (0,π)."
    },
    {
      "file": "quasiparticle_bands.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "kx",
          "ky",
          "omega1",
          "omega2"
        ],
        "items": {},
        "required": {},
        "units": {
          "kx": "1/Å",
          "ky": "1/Å",
          "omega1": "eV",
          "omega2": "eV"
        }
      },
      "description": "Quasiparticle band energies along Γ–X–M–Γ; structural audit checks for band crossing near (π/2,π/2) and a gap near (0,π)."
    },
    {
      "file": "gap_vs_temperature.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "Delta"
        ],
        "items": {},
        "required": {},
        "units": {
          "T": "k_B T/|t|",
          "Delta": "eV"
        }
      },
      "description": "Superconducting gap amplitude vs temperature. Checker extracts Δ₀ and T_c and compares them to the paper's hidden reference values within tolerances; also verifies the existence of a low-temperature upturn (Δ_max > Δ₀)."
    }
  ],
  "notes": "The hidden checker will perform structural audit on the spectral function and bands, and a result-level comparison on the gap data (recomputing Δ₀ and T_c from the submitted CSV and comparing against the paper's reported numbers)."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier. For the normal-state artifacts, the verifier performs structural audits: it examines the spectral function map to check for the presence of a hole pocket and a pseudogap, and it inspects the quasiparticle band structure to verify band crossing and gap opening characteristics. For the superconducting gap file, the verifier extracts T_c and Δ₀ from your Δ(T) data and compares them to hidden reference values using tolerances; it also tests whether a low-temperature upturn (Δ_max > Δ₀) is present. Each scored artifact carries a distinct weight, and the final reward aggregates these weighted components. Simply reporting a value without producing the required CSV files will not receive credit.

## Output contract
All output files must be written under `/app/outputs/` with the exact filenames, column names, and units specified below. The verifier reads these files and will reject mismatches.

### normal_spectral_function.csv
- Format: csv
- Columns: kx (float, 1/Å), ky (float, 1/Å), A (float, dimensionless spectral weight at ω=0)
- Purpose: structural audit for hole pocket and pseudogap.

### quasiparticle_bands.csv
- Format: csv
- Columns: kx (float, 1/Å), ky (float, 1/Å), omega1 (float, eV), omega2 (float, eV)
- Purpose: structural audit for band crossing and gap.

### gap_vs_temperature.csv
- Format: csv
- Columns: T (float, reduced temperature k_B T/|t|, dimensionless), Delta (float, gap amplitude in eV)
- Purpose: result-level comparison of Δ₀, T_c, and low-temperature upturn.

# Superconducting Critical Temperature in a Compressible Jellium Model

## Problem background
In conventional superconductors, electrons form Cooper pairs despite their Coulomb repulsion, thanks to a phonon-mediated attraction. A critical question is how the elastic response of the charge-compensating background — specifically its bulk modulus — influences the effective electron-electron interaction and, consequently, the superconducting critical temperature Tc. This task explores this question using a jellium model: the positive background is treated as a compressible medium, its elastic stiffness enters the dielectric screening, and the resulting pairing interaction is used to solve the BCS gap equation. Lithium serves as a concrete, parameterized system.

## Approach
The model builds on the dielectric function of a free-electron gas in a compressible charge-compensating background. The dielectric function includes Thomas-Fermi screening from the electrons and a frequency-dependent term from the elastic response of the background, characterized by a reduced bulk modulus b0 and a scale (k_F s)^2. From this dielectric function, an effective Coulomb interaction is obtained, and its projection onto the s‑wave pairing channel is computed by integrating over the scattering angle for electrons at the Fermi surface.

The s‑wave interaction v^s(ω) is then inserted into the zero-temperature BCS gap equation, which is solved self-consistently for the gap function Δ(ε). The condensation energy E_c is extracted from the gap solution. Finally, the critical temperature Tc is estimated via the condensation-energy relation T_c = 0.925 √(ε_F E_c)/k_B. The whole pipeline is repeated for several values of the reduced background bulk modulus b0, allowing Tc to be traced as a function of b0 while keeping all other material parameters fixed (Fermi energy ε_F = 4.7 eV, background plasma frequency ℏω₀ = 70 meV, electron bulk modulus b_F ≈ 0.461, and (k_F s)^2 = 0.23).

## Reproduction target
Compute, for lithium with the parameter set (k_F s)^2 = 0.23, the superconducting critical temperature Tc at each of the reduced background bulk modulus values b0 = -0.2, -0.1, 0.0, 0.1, 0.2, 0.5 (all satisfying the stability condition b0 > -0.23). For every b0 value, obtain the condensation energy from the BCS gap solution and convert it to Tc using the condensation-energy method. Write the resulting (b0, Tc) pairs to a CSV file, /app/outputs/tc_vs_b0.csv, with a header row and two columns: 'b0' (dimensionless) and 'Tc' (Kelvin). The relationship between b0 and Tc is the key quantity to be evaluated.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Prepare material parameters for lithium
- Role: process
- Action: Calculate the Fermi wave vector k_F, Fermi energy ε_F, background plasma frequency ℏω₀, and the reduced bulk modulus of electrons b_F using the provided lithium parameters (cell volume V₀ = 21.6 Å³, conduction-electron density n = 4.6×10²² cm⁻³, Wigner-Seitz radius r_s = 3.27, effective mass m_e, Bohr radius a₀). Save the computed constants for use in later steps.
- Evidence: `/app/outputs/parameters.json`

### Step 2: Compute effective s-wave interaction
- Role: process
- Action: Implement the dielectric function that includes Thomas-Fermi screening and the elastic background term. For a given reduced bulk modulus b0 and the fixed scale parameter (k_F s)^2 = 0.23, compute the effective interaction V^eff and numerically integrate over the scattering angle θ to obtain the s‑wave interaction v^s(ω) using closed‑form expressions for k = k' = k_F. Produce a representation of v^s(ω) for use in the gap equation.
- Evidence: `/app/outputs/interaction_data.npz`

### Step 3: Solve BCS gap equation at T=0
- Role: process
- Action: Using the effective interaction from Step 2, solve the BCS gap equation iteratively for the superconducting gap function Δ(ε) at T=0 for a given b0. Compute the condensation energy E_c from the gap solution. Repeat for each b0 value required for the final Tc calculation. The reduced bulk modulus of electrons is fixed at b_F = 0.461, and (k_F s)^2 is set to 0.23.
- Evidence: `/app/outputs/gap_solutions.npz`

### Step 4: Compute Tc vs b0 and output scored results
- Role: scored (load-bearing)
- Action: For each b0 value in the list [-0.2, -0.1, 0.0, 0.1, 0.2, 0.5] that satisfies the stability condition b0 > -0.23, compute the critical temperature Tc via the condensation energy method T_c = 0.925 √(ε_F E_c)/k_B, using the condensation energy E_c obtained in Step 3 for the corresponding b0. Write all b0 and Tc pairs to a CSV file. Confirm that Tc increases monotonically as b0 becomes more negative.
- Output file: `/app/outputs/tc_vs_b0.csv`
- Format: csv
- Contract: Two columns: 'b0' (float) and 'Tc' (float). Header row included. Comma separated.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/tc_vs_b0.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### tc_vs_b0.csv
- path: `/app/outputs/tc_vs_b0.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Superconducting critical temperature Tc as a function of the reduced bulk modulus b0 for lithium with (k_F s)^2 = 0.23. The file must contain at least the rows for b0 = -0.2, -0.1, 0.0, 0.1, 0.2, 0.5.
- schema:
  - `type`: table
  - `required_columns`: `b0`, `Tc`
  - `units`:
    - `b0`: dimensionless
    - `Tc`: Kelvin

Notes: The hidden checker compares the submitted Tc values against reference values with a tolerance. All required b0 points must be present and satisfy the stability condition b0 > -0.23.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "tc_vs_b0.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "b0",
          "Tc"
        ],
        "units": {
          "b0": "dimensionless",
          "Tc": "Kelvin"
        }
      },
      "description": "Superconducting critical temperature Tc as a function of the reduced bulk modulus b0 for lithium with (k_F s)^2 = 0.23. The file must contain at least the rows for b0 = -0.2, -0.1, 0.0, 0.1, 0.2, 0.5."
    }
  ],
  "notes": "The hidden checker compares the submitted Tc values against reference values with a tolerance. All required b0 points must be present and satisfy the stability condition b0 > -0.23."
}
```

## How you are scored
Your submitted /app/outputs/tc_vs_b0.csv is evaluated by a hidden verifier. The verifier compares your computed Tc values for the required b0 points against reference values and also checks that the Tc values change monotonically as b0 is decreased (i.e., that the trend is physically consistent). Because numerical details of the implementation can cause minor variations, a tolerance is applied. The verifier also confirms that the intermediate workflow steps (parameter file, interaction data, gap solutions) are present and structurally correct, but the primary scoring weight lies on the Tc-vs-b0 CSV. Reporting numbers alone without executing the prescribed pipeline will not satisfy the evaluation.

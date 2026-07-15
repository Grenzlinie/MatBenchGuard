# Slater–Koster Parameterization and Specific Heat Coefficient of CeAg from Combined KKR and SK Methods

## Problem background
Intermetallic compound CeAg in the CsCl-type structure exhibits mixed-valence behavior and heavy-fermion characteristics, making its electronic structure of fundamental interest. The goal is to obtain a quickly applicable yet physically grounded band structure and to derive the electronic specific heat coefficient γ, a key observable that probes the density of states at the Fermi level. This work combines first-principles KKR calculations at high-symmetry points with a tight-binding interpolation using Slater‑Koster energy integrals.

## Approach
The electronic structure is obtained in a two-step procedure. First, spherically symmetric muffin‑tin potentials for Ce and Ag are constructed from Hartree‑Fock atomic potentials with Kohn–Sham–Gaspar exchange, using the Mattheiss superposition method. The KKR method is then used to compute energy eigenvalues at the high‑symmetry k‑points Γ, X, M, and R for selected bands corresponding to s‑like, p‑like, d‑like, and f‑like symmetry types. In the second stage, these eigenvalues are employed to determine a set of nearest‑neighbor Slater–Koster (SK) parameters on a diagonal basis for the CsCl structure, following linear relations that connect the on‑site and first‑neighbor energy integrals to the KKR eigenvalues. With the fitted SK parameters, the continuous energy bands are interpolated along the principal symmetry directions, the density of states (DOS) is generated, and the Fermi level is located. Finally, the electronic specific heat coefficient γ is calculated from the DOS at the Fermi energy using the Sommerfeld relation.

## Reproduction target
Produce the 12 nearest‑neighbor Slater–Koster energy integrals (on‑site and first‑neighbor (111) parameters) for the six orbital types (s, x, xy, d_z², xyz, f4) in CeAg, reported in Rydbergs. In addition, compute the electronic specific heat coefficient γ in mJ/(mol·K²) from the density of states at the Fermi level derived from the SK‑interpolated band structure. The two artifacts must be written as `sk_parameters.json` and `specific_heat_gamma.json` under `/app/outputs`.

## Assets

- Herman-Skillman Hartree-Fock atomic potentials tables
- Open-source KKR code: https://www.mpi-halle.mpg.de/ffc/SPRKKR/
- CeAg crystal structure (CsCl, a=3.78 Å)

## Workflow steps

### Step 1: Construct muffin-tin potentials
- Role: process
- Action: Construct spherically symmetric muffin-tin potentials for Ce and Ag in the CsCl structure (lattice constant a=3.78 Å) using Hartree-Fock atomic potentials (Herman-Skillman tables) with Kohn-Sham-Gaspar exchange and the Mattheiss superposition method. Use muffin-tin radii: r_Ce = 3.490 a0, r_Ag = 2.645 a0. Use Ce configuration 4f¹5d¹6s².
- Evidence: `/app/outputs/muffin_tin_potentials.log`

### Step 2: KKR eigenvalue calculation at high-symmetry points
- Role: process
- Action: Using the constructed muffin-tin potentials, compute KKR energy eigenvalues at the high-symmetry k-points Γ, X, M, R for the bands corresponding to the symmetry types (s/s), (x/x), (xy/xy), (d_z²/d_z²), (xyz/xyz), and (f4/f4). Write the eigenvalues to a file.
- Evidence: `/app/outputs/kkr_eigenvalues.json`

### Step 3: Slater–Koster parameter fitting
- Role: scored (load-bearing)
- Action: Using the KKR eigenvalues, solve the nearest-neighbor diagonal Slater‑Koster formulas for the CsCl structure to obtain the 12 SK parameters: on‑site (000) and first‑neighbor (111) energy integrals for the six symmetry types (s, x, xy, d_z², xyz, f4). Write the fitted parameter set in Rydbergs to sk_parameters.json.
- Output file: `/app/outputs/sk_parameters.json`
- Format: json
- Contract: JSON object with exactly these keys as floats in Rydbergs: E_s_s_000, E_s_s_111, E_x_x_000, E_x_x_111, E_xy_xy_000, E_xy_xy_111, E_dz_dz_000, E_dz_dz_111, E_xyz_xyz_000, E_xyz_xyz_111, E_f4_f4_000, E_f4_f4_111.
- Scoring: scored by hidden verifier

### Step 4: Band structure and density of states generation
- Role: process
- Action: Using the fitted SK parameters, interpolate the energy eigenvalues along principal symmetry directions to generate the continuous band structure and compute the density of states (DOS). Write the raw DOS data or a summary to dos_data.json.
- Evidence: `/app/outputs/dos_data.json`

### Step 5: Specific heat coefficient gamma estimation
- Role: scored
- Action: From the density of states at the Fermi level, compute the electronic specific heat coefficient γ using the Sommerfeld relation γ = (π/3) k_B² N(E_F). Report γ in mJ/(mol·K²) in specific_heat_gamma.json.
- Output file: `/app/outputs/specific_heat_gamma.json`
- Format: json
- Contract: JSON object with a key "gamma_mJ_per_molK2" containing a float value in mJ/(mol·K²).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/sk_parameters.json`
- `/app/outputs/specific_heat_gamma.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### sk_parameters.json
- path: `/app/outputs/sk_parameters.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Fitted Slater-Koster parameters (on-site and first-neighbor integrals) for CeAg, all in Rydbergs.
- schema:
  - `type`: object
  - `required`:
    - `E_s_s_000`: number (Rydbergs)
    - `E_s_s_111`: number (Rydbergs)
    - `E_x_x_000`: number (Rydbergs)
    - `E_x_x_111`: number (Rydbergs)
    - `E_xy_xy_000`: number (Rydbergs)
    - `E_xy_xy_111`: number (Rydbergs)
    - `E_dz_dz_000`: number (Rydbergs)
    - `E_dz_dz_111`: number (Rydbergs)
    - `E_xyz_xyz_000`: number (Rydbergs)
    - `E_xyz_xyz_111`: number (Rydbergs)
    - `E_f4_f4_000`: number (Rydbergs)
    - `E_f4_f4_111`: number (Rydbergs)

### specific_heat_gamma.json
- path: `/app/outputs/specific_heat_gamma.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Electronic specific heat coefficient γ computed from the density of states at the Fermi level.
- schema:
  - `type`: object
  - `required`:
    - `gamma_mJ_per_molK2`: number (mJ/(mol·K²))

Notes: The SK parameters are obtained by fitting KKR eigenvalues; tolerances for comparison (hidden) accommodate minor differences from code/implementation choices. The gamma coefficient must be derived from the DOS of the fitted band structure.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "sk_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "E_s_s_000": "number (Rydbergs)",
          "E_s_s_111": "number (Rydbergs)",
          "E_x_x_000": "number (Rydbergs)",
          "E_x_x_111": "number (Rydbergs)",
          "E_xy_xy_000": "number (Rydbergs)",
          "E_xy_xy_111": "number (Rydbergs)",
          "E_dz_dz_000": "number (Rydbergs)",
          "E_dz_dz_111": "number (Rydbergs)",
          "E_xyz_xyz_000": "number (Rydbergs)",
          "E_xyz_xyz_111": "number (Rydbergs)",
          "E_f4_f4_000": "number (Rydbergs)",
          "E_f4_f4_111": "number (Rydbergs)"
        }
      },
      "description": "Fitted Slater-Koster parameters (on-site and first-neighbor integrals) for CeAg, all in Rydbergs."
    },
    {
      "file": "specific_heat_gamma.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "gamma_mJ_per_molK2": "number (mJ/(mol·K²))"
        }
      },
      "description": "Electronic specific heat coefficient γ computed from the density of states at the Fermi level."
    }
  ],
  "notes": "The SK parameters are obtained by fitting KKR eigenvalues; tolerances for comparison (hidden) accommodate minor differences from code/implementation choices. The gamma coefficient must be derived from the DOS of the fitted band structure."
}
```

## How you are scored
Each scored output file is independently evaluated by a hidden checker. The checker verifies that the correct JSON structure is produced and compares the reported numerical values against hidden reference results using appropriate tolerances. The two scored stages carry weights that sum to the final reward. Simply reporting numbers that match the hidden reference is necessary but not sufficient: the checker may also verify internal consistency or trace the values through the intermediate workflow evidence. No gold values or tolerances are disclosed in the instructions.

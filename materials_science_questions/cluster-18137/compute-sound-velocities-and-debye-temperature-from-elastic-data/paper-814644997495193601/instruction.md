# Lattice dynamics of a layered hexagonal compound: phonon dispersion, DOS, specific heat, and Debye temperature from a given force-constant model

## Problem background
The vibrational properties of layered hexagonal compounds, such as transition metal dichalcogenides, are of fundamental interest because the weak van der Waals bonding between adjacent layers leads to highly anisotropic phonon dispersion and unusual thermodynamic behaviour. In such materials, the intralayer bonding is strong and covalent, while the interlayer coupling is much weaker, resulting in rigid-layer modes and nearly degenerate phonon branches. A quantitative description of the lattice dynamics is a prerequisite for understanding the thermal properties, including the specific heat and Debye temperature. This task focuses on computing these quantities from a known set of force constants that define a mixed lattice-dynamics model for a specific layered hexagonal compound.

## Approach
The vibration frequencies of the crystal are determined by solving the secular equation derived from the dynamical matrix. In this mixed model, the intralayer interactions are described by valence forces that account for bond stretching and bond-angle bending, including a cross term that couples stretches of different bonds; the interlayer interaction is represented by axially symmetric central forces between sulfur atoms in neighbouring layers. The potential energy is parametrized by seven force constants (provided as assets). Starting from the crystal structure (lattice parameters and fractional coordinates), the dynamical matrix is constructed for an arbitrary wavevector in reciprocal space. Diagonalizing this matrix yields the phonon frequencies for all branches. By sampling a dense set of wavevectors along the high-symmetry directions [001] and [100], the phonon dispersion curves are obtained. The phonon density of states is then computed by accumulating the frequencies over a uniform mesh covering the entire Brillouin zone, normalized so that its integral equals the total number of vibrational modes per primitive cell. From the density of states, the lattice contribution to the constant-volume specific heat is calculated using the standard Planck distribution for harmonic oscillators. Finally, the temperature-dependent Debye temperature is derived by inverting the Debye model relation, using the computed specific heat curve. All steps are purely computational; no experimental data fitting is required.

## Reproduction target
Using the provided crystal structure and the set of seven force constants, compute the following four quantities and output each as a separate CSV file under `/app/outputs`:

1. **Phonon dispersion** (`phonon_dispersion.csv`): frequencies of all 18 phonon branches for a grid of wavevectors along the [001] (from Γ to A) and [100] (from Γ to K to M) directions. Each row corresponds to one frequency at one q-point, with columns: q_x (fractional coordinate in units of 2π/a), q_z (fractional coordinate in units of 2π/c), mode_index (1–18), frequency (THz).
2. **Phonon density of states** (`phonon_dos.csv`): the vibrational spectrum g(ν) computed on a dense frequency grid, with columns: frequency (THz), dos (normalized so that ∫ g(ν) dν = 18).
3. **Specific heat** (`specific_heat.csv`): lattice specific heat at constant volume Cᵥ(T) for temperatures from 1 K to 300 K, with columns: temperature (K), Cv (J/(mol·K)).
4. **Debye temperature** (`debye_temperature.csv`): Debye temperature Θ_D(T) for the same temperature points, with columns: temperature (K), Debye_temperature (K).

All outputs must match the column structure and units exactly as specified.

## Assets

- Crystal structure of the layered hexagonal compound (space group P6_3/mmc, a=3.15 Å, c=12.3 Å, with Mo at 2c sites (0,0,±1/4) and S at 4f sites (1/3,2/3,z) with z ≈ 0.621)
- Force constants for the mixed lattice-dynamics model: K_r=1.3846, K_θ=0.1502, K_φ=0.1892, K_ψ=0.1381, K_{rr'}^φ=-0.1722, α=0.0311, β=0.0072 (in units of 10^5 dyn/cm)

## Workflow steps

### Step 1: Compute phonon dispersion
- Role: scored
- Action: Construct the dynamical matrix from the given crystal structure and force-constant model, and compute the phonon frequencies on a set of q-points along the [001] and [100] high-symmetry directions. Output all branch frequencies.
- Output file: `/app/outputs/phonon_dispersion.csv`
- Format: csv
- Contract: columns: q_x (fractional coordinate in units of 2π/a), q_z (fractional coordinate in units of 2π/c), mode_index (integer 1..18), frequency (THz).
- Scoring: scored by hidden verifier

### Step 2: Compute phonon density of states
- Role: scored (load-bearing)
- Action: From the dynamical matrix, compute the vibrational density of states g(ν) on a dense frequency grid, normalized so that the integral over all ν equals the number of modes per primitive cell (18). Output the DOS spectrum.
- Output file: `/app/outputs/phonon_dos.csv`
- Format: csv
- Contract: columns: frequency (THz), dos (normalized units, integral = 18).
- Scoring: scored by hidden verifier

### Step 3: Compute specific heat
- Role: scored
- Action: Using the phonon density of states, compute the lattice specific heat at constant volume C_v(T) for a set of temperatures from 1 K to 300 K, using the standard Planck distribution formula. Output C_v in J/(mol·K).
- Output file: `/app/outputs/specific_heat.csv`
- Format: csv
- Contract: columns: temperature (K), Cv (J/(mol·K)).
- Scoring: scored by hidden verifier

### Step 4: Compute Debye temperature
- Role: scored
- Action: From the C_v(T) values, determine the Debye temperature Θ_D(T) at the same temperature points by solving the Debye model relation. Output Θ_D in kelvin.
- Output file: `/app/outputs/debye_temperature.csv`
- Format: csv
- Contract: columns: temperature (K), Debye_temperature (K).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phonon_dispersion.csv`
- `/app/outputs/phonon_dos.csv`
- `/app/outputs/specific_heat.csv`
- `/app/outputs/debye_temperature.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phonon_dispersion.csv
- path: `/app/outputs/phonon_dispersion.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Phonon frequencies along the high-symmetry directions; the hidden reference is obtained by independent recomputation from the same model.
- schema:
  - `type`: table
  - `required_columns`: `q_x`, `q_z`, `mode_index`, `frequency`
  - `units`:
    - `frequency`: THz

### phonon_dos.csv
- path: `/app/outputs/phonon_dos.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Phonon density of states; the hidden reference is recomputed using the same dynamical matrix and normalization.
- schema:
  - `type`: table
  - `required_columns`: `frequency`, `dos`
  - `units`:
    - `frequency`: THz
    - `dos`: normalized (integral = 18)

### specific_heat.csv
- path: `/app/outputs/specific_heat.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Lattice specific heat C_v as a function of temperature; the hidden reference is recomputed from the phonon DOS.
- schema:
  - `type`: table
  - `required_columns`: `temperature`, `Cv`
  - `units`:
    - `temperature`: K
    - `Cv`: J/(mol·K)

### debye_temperature.csv
- path: `/app/outputs/debye_temperature.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Debye temperature Θ_D as a function of temperature; derived from the specific heat by solving the Debye model relation.
- schema:
  - `type`: table
  - `required_columns`: `temperature`, `Debye_temperature`
  - `units`:
    - `temperature`: K
    - `Debye_temperature`: K

Notes: All outputs must be recomputed from the same underlying lattice-dynamics model. The checker independently recalculates every quantity and compares with specified tolerances (not disclosed here).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phonon_dispersion.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "q_x",
          "q_z",
          "mode_index",
          "frequency"
        ],
        "units": {
          "frequency": "THz"
        }
      },
      "description": "Phonon frequencies along the high-symmetry directions; the hidden reference is obtained by independent recomputation from the same model."
    },
    {
      "file": "phonon_dos.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "frequency",
          "dos"
        ],
        "units": {
          "frequency": "THz",
          "dos": "normalized (integral = 18)"
        }
      },
      "description": "Phonon density of states; the hidden reference is recomputed using the same dynamical matrix and normalization."
    },
    {
      "file": "specific_heat.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature",
          "Cv"
        ],
        "units": {
          "temperature": "K",
          "Cv": "J/(mol·K)"
        }
      },
      "description": "Lattice specific heat C_v as a function of temperature; the hidden reference is recomputed from the phonon DOS."
    },
    {
      "file": "debye_temperature.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature",
          "Debye_temperature"
        ],
        "units": {
          "temperature": "K",
          "Debye_temperature": "K"
        }
      },
      "description": "Debye temperature Θ_D as a function of temperature; derived from the specific heat by solving the Debye model relation."
    }
  ],
  "notes": "All outputs must be recomputed from the same underlying lattice-dynamics model. The checker independently recalculates every quantity and compares with specified tolerances (not disclosed here)."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that independently reimplements the same lattice-dynamics model using the same crystal structure and force constants. The verifier recomputes the phonon frequencies, density of states, specific heat, and Debye temperature, and then compares your output files to its own reference results. Each of the four scored artifacts is assessed against tolerance criteria that account for the numerical spread of independent recomputation. The scores from the individual artifacts are combined by weight (with the density-of-states step carrying higher weight because the specific heat and Debye temperature depend on it) to yield a final reward between 0.0 and 1.0. Simply reporting a single number is insufficient; the checker expects the full dispersion data, DOS spectrum, and temperature-dependent curves, which it can re-derive and verify. The verifier does not rely on any external experimental data or digitized figures; it derives everything from the model parameters provided to you.

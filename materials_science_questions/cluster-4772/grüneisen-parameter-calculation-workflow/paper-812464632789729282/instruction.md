# Implicit Phonon Frequency Shift in Deuterated Anthracene from Rigid-Molecule Lattice Dynamics

## Problem background
Deuterated anthracene (C14D10) is a molecular crystal whose anharmonic phonon properties are of interest. The temperature dependence of phonon frequencies consists of two contributions: an explicit shift from anharmonic terms in the crystal potential, and an implicit shift driven by thermal expansion (volume change). The explicit shift for deuterated anthracene is already known from previous work; this reproducibility target addresses the implicit contribution. Computing the implicit shift requires the harmonic phonon frequencies at the Brillouin zone centre (Γ point), the volume dependence of those frequencies to obtain mode Grüneisen constants, the bulk modulus and compressibility, and the volume thermal expansion ε(T). The goal is to compute these quantities using a rigid-molecule lattice dynamics model with atom-atom (Williams 6-exponential) potentials, and to obtain the implicit fractional frequency shift for the nine optic phonon modes (branches 4–12) as a function of temperature. The computed implicit shift, together with the previously reported explicit shift, completes the calculation of the total anharmonic phonon frequency shift in deuterated anthracene.

## Approach
A rigid-molecule approximation is used: each anthracene molecule is treated as a rigid unit, and the intermolecular potential is built from atom-atom interactions of the Williams 6-exponential form V(r) = -A/r^6 + B exp(-α r), with published parameters for C–C, C–D, and D–D pairs. The crystal structure is optimized by minimizing the total potential energy at zero pressure. Harmonic phonon frequencies are obtained by diagonalizing the dynamical matrix at the Γ point and over a finite q-point mesh covering the Brillouin zone. To obtain volume-dependent phonon frequencies, hydrostatic pressures are applied: for each pressure, the quantity Φ + pΔV is minimized to produce a strained structure with a new unit-cell volume, and the dynamical matrix is re-diagonalized to yield ω_qj(V). Mode Grüneisen constants are then computed by finite differences of ln ω versus ln V. The bulk modulus B is found by fitting the total potential energy Φ at the strained volumes to a cubic polynomial in V and evaluating B = V0 (d²Φ/dV²) at equilibrium; the compressibility K is 1/B. Volume thermal expansion ε(T) is calculated from two expressions: a lowest-order formula (sum over q-modes of γ * ħω coth(ħω/2kT) divided by 2 V0 B) and, optionally, a next-highest-order correction that uses higher derivatives of Φ and renormalized Grüneisen constants. Finally, for each Γ-point mode, the implicit fractional frequency shift is computed as (Δω/ω)_im = exp[-γ ε(T)] - 1, using the mode Grüneisen constant and the thermal expansion. The entire pipeline is implemented in Python using standard scientific libraries.

## Reproduction target
Produce the following outputs from the rigid-molecule lattice dynamics simulation using the Williams potential and the known deuterated anthracene crystal structure: (1) harmonic_phonon_frequencies.csv: the Γ-point phonon frequencies (THz) and symmetry characters for branches 4–12 at equilibrium volume; (2) gruneisen_constants.csv: the mode Grüneisen constants (dimensionless) for the same branches; (3) compressibility.txt: the compressibility K (bar⁻¹) of deuterated anthracene; (4) thermal_expansion.csv: the volume thermal expansion ε(T) as a function of temperature (T in K) from 0 K to approximately 300 K, reporting both the lowest-order and (optionally) next-highest-order values; (5) implicit_shift.csv: the implicit fractional frequency shift (Δω/ω)_im for each of the nine modes (branches 4–12) as a function of temperature over the same range. The computed quantities should be consistent with the rigid-molecule model and the specified interatomic potential; they will be compared to independently reproduced reference results.

## Assets

- Williams 6-exponential potential parameters for C-C, C-D, D-D interactions (Williams 1967): 10.1063/1.184108
- Deuterated anthracene crystal structure (space group P2_1/a, cell parameters)
- Scientific Python stack (NumPy, SciPy, optionally ASE or pymatgen)

## Workflow steps

### Step 1: Harmonic phonon frequencies at equilibrium
- Role: scored
- Action: Construct the dynamical matrix for deuterated anthracene using rigid-molecule approximation and the Williams 6-exponential potential. Perform energy minimization to obtain the equilibrium crystal structure at zero pressure. Diagonalize the dynamical matrix at the Γ point to obtain harmonic phonon frequencies for branches 4–12. Also compute phonon frequencies on a Γ‑centered q‑point mesh covering the Brillouin zone for use in thermal expansion later.
- Output file: `/app/outputs/harmonic_phonon_frequencies.csv`
- Format: csv
- Contract: branch (int), character (str), frequency_THz (float)
- Scoring: scored by hidden verifier

### Step 2: Volume-dependent phonon frequencies under hydrostatic pressure
- Role: process
- Action: Apply a set of hydrostatic pressures and, for each pressure, minimize Φ + pΔV to obtain strained crystal structures and corresponding unit-cell volumes. For each strained structure, reconstruct the dynamical matrix and diagonalize to obtain Γ‑point phonon frequencies ω_qj(V). Retain the strained volumes, total potential energies, and corresponding frequencies for downstream use.
- Evidence: `/app/outputs/pressure_phonon_data.json`

### Step 3: Mode Grüneisen constants
- Role: scored
- Action: Compute the mode Grüneisen constants γ_qj at Γ from the volume‑dependent phonon frequencies using finite differences: γ = -Δ(ln ω)/Δ(ln V). Output the constants for branches 4–12.
- Output file: `/app/outputs/gruneisen_constants.csv`
- Format: csv
- Contract: branch (int), gamma (float)
- Scoring: scored by hidden verifier

### Step 4: Bulk modulus and compressibility
- Role: scored
- Action: Fit the total potential energy Φ as a function of unit-cell volume V to a cubic polynomial. Compute the bulk modulus B and the compressibility K = 1/B. Output the compressibility value.
- Output file: `/app/outputs/compressibility.txt`
- Format: txt
- Contract: single float value
- Scoring: scored by hidden verifier

### Step 5: Volume thermal expansion
- Role: scored
- Action: Compute the volume thermal expansion ε(T) using the lowest‑order formula and optionally the next‑highest‑order formula, summing over the Brillouin zone q‑mesh from Step 1, using mode Grüneisen constants from Step 3 and the bulk modulus from Step 4. Output ε(T) as a function of temperature (from 0 K to ~300 K).
- Output file: `/app/outputs/thermal_expansion.csv`
- Format: csv
- Contract: T_K (float), epsilon_0 (float), epsilon (float)
- Scoring: scored by hidden verifier

### Step 6: Implicit phonon frequency shift
- Role: scored (load-bearing)
- Action: For each Γ‑point mode (branches 4–12), compute the implicit fractional frequency shift (Δω/ω)_im = exp[ -γ ε(T) ] - 1 for a range of temperatures T, using the Grüneisen constants from Step 3 and the thermal expansion ε(T) from Step 5. Output the shifts for all nine modes as a function of temperature.
- Output file: `/app/outputs/implicit_shift.csv`
- Format: csv
- Contract: T_K (float), branch_4 (float), branch_5 (float), branch_6 (float), branch_7 (float), branch_8 (float), branch_9 (float), branch_10 (float), branch_11 (float), branch_12 (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/harmonic_phonon_frequencies.csv`
- `/app/outputs/gruneisen_constants.csv`
- `/app/outputs/compressibility.txt`
- `/app/outputs/thermal_expansion.csv`
- `/app/outputs/implicit_shift.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### harmonic_phonon_frequencies.csv
- path: `/app/outputs/harmonic_phonon_frequencies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Harmonic Γ‑point phonon frequencies (branches 4–12) and their symmetry character.
- schema:
  - `type`: table
  - `required_columns`: `branch`, `character`, `frequency_THz`
  - `units`:
    - `frequency_THz`: THz

### gruneisen_constants.csv
- path: `/app/outputs/gruneisen_constants.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Mode Grüneisen constants γ for branches 4–12 at Γ.
- schema:
  - `type`: table
  - `required_columns`: `branch`, `gamma`
  - `units`:
    - `gamma`: dimensionless

### compressibility.txt
- path: `/app/outputs/compressibility.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Compressibility K (bar⁻¹) as a single floating‑point number.
- schema:
  - `type`: text
  - `units`: bar^-1

### thermal_expansion.csv
- path: `/app/outputs/thermal_expansion.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Volume thermal expansion ε(T) as a function of temperature: lowest‑order ε₀ and (optionally) next‑highest‑order ε.
- schema:
  - `type`: table
  - `required_columns`: `T_K`, `epsilon_0`, `epsilon`
  - `units`:
    - `T_K`: K
    - `epsilon_0`: dimensionless
    - `epsilon`: dimensionless

### implicit_shift.csv
- path: `/app/outputs/implicit_shift.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Implicit fractional frequency shift (Δω/ω)_im for each Γ‑point mode as a function of temperature.
- schema:
  - `type`: table
  - `required_columns`: `T_K`, `branch_4`, `branch_5`, `branch_6`, `branch_7`, `branch_8`, `branch_9`, `branch_10`, `branch_11`, `branch_12`
  - `units`:
    - `T_K`: K
    - `branch_4`: dimensionless
    - `branch_5`: dimensionless
    - `branch_6`: dimensionless
    - `branch_7`: dimensionless
    - `branch_8`: dimensionless
    - `branch_9`: dimensionless
    - `branch_10`: dimensionless
    - `branch_11`: dimensionless
    - `branch_12`: dimensionless

Notes: All outputs are compared to the paper's reported values/curves using tolerances appropriate for a re‑implementation. The agent must write files exactly under /app/outputs.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "harmonic_phonon_frequencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "branch",
          "character",
          "frequency_THz"
        ],
        "units": {
          "frequency_THz": "THz"
        }
      },
      "description": "Harmonic Γ‑point phonon frequencies (branches 4–12) and their symmetry character."
    },
    {
      "file": "gruneisen_constants.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "branch",
          "gamma"
        ],
        "units": {
          "gamma": "dimensionless"
        }
      },
      "description": "Mode Grüneisen constants γ for branches 4–12 at Γ."
    },
    {
      "file": "compressibility.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "units": "bar^-1"
      },
      "description": "Compressibility K (bar⁻¹) as a single floating‑point number."
    },
    {
      "file": "thermal_expansion.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T_K",
          "epsilon_0",
          "epsilon"
        ],
        "units": {
          "T_K": "K",
          "epsilon_0": "dimensionless",
          "epsilon": "dimensionless"
        }
      },
      "description": "Volume thermal expansion ε(T) as a function of temperature: lowest‑order ε₀ and (optionally) next‑highest‑order ε."
    },
    {
      "file": "implicit_shift.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T_K",
          "branch_4",
          "branch_5",
          "branch_6",
          "branch_7",
          "branch_8",
          "branch_9",
          "branch_10",
          "branch_11",
          "branch_12"
        ],
        "units": {
          "T_K": "K",
          "branch_4": "dimensionless",
          "branch_5": "dimensionless",
          "branch_6": "dimensionless",
          "branch_7": "dimensionless",
          "branch_8": "dimensionless",
          "branch_9": "dimensionless",
          "branch_10": "dimensionless",
          "branch_11": "dimensionless",
          "branch_12": "dimensionless"
        }
      },
      "description": "Implicit fractional frequency shift (Δω/ω)_im for each Γ‑point mode as a function of temperature."
    }
  ],
  "notes": "All outputs are compared to the paper's reported values/curves using tolerances appropriate for a re‑implementation. The agent must write files exactly under /app/outputs."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that compares each scored artifact to reference values computed from the same model and potential. The verifier reads the exact output files you write to /app/outputs. Each artifact is scored individually: for harmonic phonon frequencies and Grüneisen constants, the verifier compares your per-branch values against reference numbers and awards credit for branches within a tolerance that accounts for implementation differences. For compressibility, it compares the single value. For thermal expansion and implicit shift, the verifier evaluates the agreement of your ε(T) and (Δω/ω)_im(T) curves with reference curves, using a root-mean-square deviation (RMSD) or similar measure. The overall reward is a weighted sum: harmonic_phonon_frequencies.csv (20%), gruneisen_constants.csv (20%), compressibility.txt (10%), thermal_expansion.csv (25%), and implicit_shift.csv (25%). Reporting a number without actually running the simulation will not succeed because the tolerances are set to require a physically consistent re-implementation. The verifier may also perform structural checks (e.g., file format, column presence, monotonicity) for a small fraction of the score. You must produce all five output files; missing files result in zero credit for that component.

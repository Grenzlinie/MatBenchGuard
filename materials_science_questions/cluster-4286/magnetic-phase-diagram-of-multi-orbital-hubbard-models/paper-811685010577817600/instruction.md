# Magnetic phase stability and charge order suppression under SSH coupling in half-doped manganites

## Problem background
Half‑doped perovskite manganites exhibit a checkerboard charge order coexisting with a CE‑type antiferromagnetic order. The microscopic origin of the charge order is debated: whether it is driven primarily by Coulomb repulsion between electrons or by antiferromagnetic correlations. This task examines the stability of the charge order under Su–Schrieffer–Heeger (SSH) electron–phonon interactions, which couple the electronic degrees of freedom to lattice distortions. The goal is to quantify how the SSH coupling affects the relative energies of different magnetic phases and the amplitude of the checkerboard charge order, thereby providing insight into which interactions are essential for stabilizing the observed ordered state.

## Approach
The investigation uses an unrestricted real‑space Hartree–Fock approximation applied to the dimensionless double‑exchange + SSH Hamiltonian on a two‑dimensional square lattice with periodic boundary conditions. The localized spins are treated as classical vectors, and the SSH bond‑displacement vectors are optimized variationally for each magnetic configuration. For a fixed set of dimensionless parameters (on‑site Coulomb repulsion Ū = 50, Hund coupling J̄_H = 10, superexchange J̄ = 0.05, nearest‑neighbor Coulomb V̄ = 0), the energies of four candidate magnetic configurations are computed as functions of the SSH coupling λ over the range [0, 0.1]. The four configurations are: CE‑type antiferromagnetic, Néel‑type antiferromagnetic, ferromagnetic, and a canted spin arrangement. From the self‑consistent site densities of the CE phase, a checkerboard charge‑order parameter Δ is extracted. Comparing the phase energies reveals which magnetic order is ground state at each λ, and tracking Δ shows how the charge order evolves with the electron–phonon coupling.

## Reproduction target
Produce two CSV artifacts by implementing and running the unrestricted real‑space Hartree–Fock workflow described above. The first artifact is a table of ground‑state energies per site (in units of the hopping t) for the four magnetic phases as a function of λ. The second artifact is a table of the checkerboard charge‑order parameter Δ for the CE phase over the same λ range. These outputs will be automatically scored against the published phase‑stability behavior and the critical coupling threshold that the paper reports. The scoring checks that the derived quantities satisfy the expected ordering and trend without requiring an exact numerical match to any particular published value.

## Assets

- Python 3: https://pypi.tuna.tsinghua.edu.cn/simple
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Write energy comparison table
- Role: scored (load-bearing)
- Action: Implement a self-consistent unrestricted real-space Hartree–Fock solver for the dimensionless double-exchange + SSH Hamiltonian on a two-dimensional square lattice with periodic boundary conditions, using a supercell of at least 4×4 sites. For each λ from 0.0 to 0.1 (in steps of 0.01 or finer), iterate the HF equations to convergence for four predetermined magnetic configurations (CE-type, Néel-type, ferromagnetic, canted). Treat the localized spins classically and variationally optimize the bond displacement vectors y_ij for each configuration. Record the total energy per site (in units of t) for each phase and write a CSV with columns: lambda, energy_CE, energy_AF, energy_F, energy_C.
- Output file: `/app/outputs/step_01_energies.csv`
- Format: csv
- Contract: lambda:float, energy_CE:float, energy_AF:float, energy_F:float, energy_C:float
- Scoring: scored by hidden verifier

### Step 2: Write charge order parameter data
- Role: scored
- Action: From the same Hartree–Fock simulation (re-run if necessary) for the CE phase, compute the checkerboard charge order parameter Δ from the self-consistent site densities and write a CSV with columns: lambda, delta.
- Output file: `/app/outputs/step_02_delta.csv`
- Format: csv
- Contract: lambda:float, delta:float
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_energies.csv`
- `/app/outputs/step_02_delta.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_energies.csv
- path: `/app/outputs/step_01_energies.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Ground-state energies of CE, antiferromagnetic (Néel), ferromagnetic, and canted spin configurations as a function of the SSH coupling parameter λ.
- schema:
  - `type`: table
  - `required_columns`: `lambda`, `energy_CE`, `energy_AF`, `energy_F`, `energy_C`
  - `units`:
    - `lambda`: dimensionless
    - `energy_CE`: energy per site in units of t
    - `energy_AF`: energy per site in units of t
    - `energy_F`: energy per site in units of t
    - `energy_C`: energy per site in units of t

### step_02_delta.csv
- path: `/app/outputs/step_02_delta.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Checkerboard charge order parameter Δ of the CE phase as a function of λ.
- schema:
  - `type`: table
  - `required_columns`: `lambda`, `delta`
  - `units`:
    - `lambda`: dimensionless
    - `delta`: charge order amplitude (dimensionless)

Notes: The agent must produce the two CSV files from a full unrestricted real‑space Hartree–Fock simulation. No pre‑computed intermediate data is provided. Scoring will verify that the CE phase is the stable ground state (lowest energy) for all λ and that Δ decreases monotonically, crossing zero near the critical coupling λc ≈ 0.063.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "lambda",
          "energy_CE",
          "energy_AF",
          "energy_F",
          "energy_C"
        ],
        "units": {
          "lambda": "dimensionless",
          "energy_CE": "energy per site in units of t",
          "energy_AF": "energy per site in units of t",
          "energy_F": "energy per site in units of t",
          "energy_C": "energy per site in units of t"
        }
      },
      "description": "Ground-state energies of CE, antiferromagnetic (Néel), ferromagnetic, and canted spin configurations as a function of the SSH coupling parameter λ."
    },
    {
      "file": "step_02_delta.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "lambda",
          "delta"
        ],
        "units": {
          "lambda": "dimensionless",
          "delta": "charge order amplitude (dimensionless)"
        }
      },
      "description": "Checkerboard charge order parameter Δ of the CE phase as a function of λ."
    }
  ],
  "notes": "The agent must produce the two CSV files from a full unrestricted real‑space Hartree–Fock simulation. No pre‑computed intermediate data is provided. Scoring will verify that the CE phase is the stable ground state (lowest energy) for all λ and that Δ decreases monotonically, crossing zero near the critical coupling λc ≈ 0.063."
}
```

## How you are scored
A hidden verifier examines each of your two output files. First it validates that the files exist and conform to the required column schema. Then it performs quantitative checks on the data: for the energy table it evaluates the relative ordering of the four phases across the λ sweep, and for the charge‑order table it examines the monotonicity and threshold crossing of Δ. Submitting a number without a correct underlying simulation will not pass the quantitative checks. The per‑artifact scores are combined into a final reward between 0 and 1, with the energy‑comparison artifact carrying the largest weight. The exact tolerances and reference values are not disclosed.

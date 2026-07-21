# Extracting exchange parameters for 1-D mixed molecular radical crystals via Hückel-Hubbard band theory

## Problem background
One-dimensional (1-D) stacks of mixed molecular radical crystals (MMRCs) consist of organic π-radicals alternated with diamagnetic polycyclic aromatic hydrocarbons (PAHs). The effective Heisenberg exchange integral J_eff between the unpaired electrons in such stacks can be decomposed into three contributions: a direct Coulomb exchange J, a kinetic exchange J_kin (which is antiferromagnetic in origin), and an indirect spin exchange J_ind arising from spin polarization. The nature (ferromagnetic or antiferromagnetic) and magnitude of the magnetic coupling depend on the topology of the stack — specifically, whether the stack is alternant (each starred π-center of a radical neighbors an unstarred center of the adjacent PAH) or nonalternant — and on the parameters of the underlying Hückel-Hubbard model. In this task you must implement a band-theory procedure to compute these exchange contributions for a set of model 1‑D stacks and report the numerical values.

## Approach
Use Hückel-Hubbard band theory in the tight-binding formulation. For each stack, construct a model geometry with ideal bond lengths (1.40 Å) and the specified interplanar distances and slip angles. Compute the intermolecular resonance integrals using Mulliken's formula with the standard parameters β0 = −2.4 eV and Slater exponents z_C = 3.25, z_N = 3.90, taking into account the angular dependence of the overlap integrals. Obtain the two-center Coulomb integrals via the Mataga-Nishimoto approximation (one-center Coulomb integrals: γ_CC = 10.84 eV, γ_NN = 12.27 eV). Build the Bloch Hamiltonian matrices, solve the eigenvalue equation on a dense grid of k-points in the Brillouin zone, and extract the energy bands. From the band structure, determine the half-filled band width Δε, the transfer (hopping) integral t between adjacent Wannier states, and, for stacks containing Wurster's radicals, the renormalized Hubbard U. Finally, compute the kinetic exchange as J_kin = −2 t² / U, the direct Coulomb exchange J between the Wannier states, and the indirect exchange J_ind via the spin-polarization formalism. The effective exchange is J_eff = J + J_kin + J_ind. Assemble all quantities into the output CSV.

## Reproduction target
Compute the transfer integral t, the direct Coulomb exchange J, the kinetic exchange J_kin, the indirect exchange J_ind, the effective exchange J_eff, and the half-filled band width Δε for every 1‑D stack listed below. For the Wurster‑containing stacks, also report the renormalized Hubbard U. The systems are:

- Bl‑Bl‑A, Bl‑Bl‑F, Bl‑Cor‑A, Bl‑Cor‑F, Bl‑Per‑A, Bl‑Per‑F
- Di‑Di‑A, Di‑Di‑F, Di‑Cor‑F, Di‑Cor‑A
- Pe‑Pe‑A, Pe‑Pe‑F, Pe‑Cor‑F, Pe‑Cor‑A
- W‑W, W‑Cor‑W

Write the results to `/app/outputs/exchange_integrals.csv`, a CSV file with one row per system and the following columns: system (string), t (float, eV), J (float, eV), J_kin (float, eV), J_ind (float, eV), J_eff (float, eV), Delta_epsilon (float, eV), and, for the Wurster systems, U (float, eV).

## Assets

- Python
- NumPy: numpy
- SciPy: scipy
- Python standard library

## Workflow steps

### Step 1: Parameter setup and band structure calculation
- Role: process
- Action: Construct model geometries for each 1-D stack using ideal bond lengths and the appropriate interplanar distances and slip angles. Compute Hamiltonian matrix elements: resonance integrals via Mulliken's formula with standard parameters (β0 = −2.4 eV, Slater exponents for C and N) and two-center Coulomb integrals via the Mataga-Nishimoto approximation (one-center integrals γ_CC=10.84 eV, γ_NN=12.27 eV). Build Bloch Hamiltonian matrices and solve the eigenvalue equation as a function of k to obtain band energies. For each system extract the half-filled band width Δε, the transfer integral t between adjacent Wannier states, and the renormalized Hubbard U (only for Wurster systems).
- Evidence: `/app/outputs/none`

### Step 2: Compute spin exchange integrals
- Role: scored (load-bearing)
- Action: Using the transfer integral t, the renormalized Hubbard U, and the two-center Coulomb integrals, compute the kinetic exchange J_kin = −2 t² / U, the direct Coulomb exchange J, the indirect spin exchange J_ind, and the effective exchange J_eff = J + J_kin + J_ind for every 1-D stack. Write the results to exchange_integrals.csv.
- Output file: `/app/outputs/exchange_integrals.csv`
- Format: csv
- Contract: Columns: system (string), t (float, eV), J (float, eV), J_kin (float, eV), J_ind (float, eV), J_eff (float, eV), Delta_epsilon (float, eV), U (float, eV, optional for non-Wurster systems).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/exchange_integrals.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### exchange_integrals.csv
- path: `/app/outputs/exchange_integrals.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed exchange parameters for each 1-D stack. The checker compares the agent's values to hidden reference values, verifies sign patterns (J_eff>0 for ferromagnetic, <0 for antiferromagnetic stacks), and checks internal consistency (J_kin = −2 t² / U).
- schema:
  - `type`: table
  - `required_columns`: `system`, `t`, `J`, `J_kin`, `J_ind`, `J_eff`, `Delta_epsilon`
  - `optional_columns`: `U`
  - `units`:
    - `t`: eV
    - `J`: eV
    - `J_kin`: eV
    - `J_ind`: eV
    - `J_eff`: eV
    - `Delta_epsilon`: eV
    - `U`: eV

Notes: The checker tolerates implementation-dependent numerical spread and does not require bit-level agreement with the paper. Structural trends and the internal consistency relation are scored alongside magnitude comparisons.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "exchange_integrals.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "t",
          "J",
          "J_kin",
          "J_ind",
          "J_eff",
          "Delta_epsilon"
        ],
        "optional_columns": [
          "U"
        ],
        "units": {
          "t": "eV",
          "J": "eV",
          "J_kin": "eV",
          "J_ind": "eV",
          "J_eff": "eV",
          "Delta_epsilon": "eV",
          "U": "eV"
        }
      },
      "description": "Computed exchange parameters for each 1-D stack. The checker compares the agent's values to hidden reference values, verifies sign patterns (J_eff>0 for ferromagnetic, <0 for antiferromagnetic stacks), and checks internal consistency (J_kin = −2 t² / U)."
    }
  ],
  "notes": "The checker tolerates implementation-dependent numerical spread and does not require bit-level agreement with the paper. Structural trends and the internal consistency relation are scored alongside magnitude comparisons."
}
```

## How you are scored
A hidden verifier will evaluate your submitted `exchange_integrals.csv`. It compares your computed values for each system to reference values obtained from a faithful implementation of the theory, allowing numerical tolerances that accommodate minor differences in implementation details (e.g., k‑grid density, numerical solver settings). The verifier also checks internal consistency: the kinetic exchange you report must satisfy J_kin = −2 t² / U using your own computed t and U, and the pattern of values across different stack types must respect the structural relationships implied by the alternant/nonalternant topology. The final reward is a weighted sum of per‑system numerical agreement and structural consistency. There is no single “correct” number to copy; your implementation must be internally self‑consistent and follow the prescribed physical model.

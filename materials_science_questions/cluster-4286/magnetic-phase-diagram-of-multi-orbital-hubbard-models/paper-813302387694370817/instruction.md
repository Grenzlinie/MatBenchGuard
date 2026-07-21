# Energy Spectrum and Magnetization of the Two-Sublattice Hubbard Model

## Problem background
The Hubbard model is a fundamental model of correlated electrons used to study magnetism and metal–insulator transitions. In two dimensions, the nature of the ground state at half‑filling is a long-standing problem: whether the system is conducting or insulating and whether magnetic order sets in. This reproduction task investigates the antiferromagnetic ground state of the simple Hubbard model (one band, one site energy per sublattice, and equal on‑site repulsion U) within the static‑fluctuation approximation. Your goal is to compute, for a specific set of parameters U=8 eV and hopping B=1.5 eV, (1) the energy eigenvalue spectrum at two symmetry points of the Brillouin zone, and (2) the ground‑state magnetization per site S obtained from a self‑consistency equation derived from the spectral theorem. The computed numbers answer whether the model supports an antiferromagnetic insulating state under these conditions.

## Approach
The Hubbard hamiltonian is separated into a mean‑field piece with static number‑density fluctuations. Renormalized site energies are introduced that depend on the yet‑unknown sublattice magnetization S. The equations of motion for the electron creation operators are solved via Fourier transformation, leading to closed‑form anticommutator Green’s functions whose poles give the energy spectrum. For the simple Hubbard model (ε₁=ε₂=-U/2, U₁=U₂=U) at half‑filling, the spectrum simplifies to two bands whose analytical form shows a gap controlled by U, while the k‑dependence enters through a hopping term that involves cosines of the two momentum components. Separately, from the Green’s function and the spectral theorem, a self‑consistency equation for the magnetization S is obtained. In the zero‑temperature limit, that equation reduces to a transcendental expression where a complete elliptic integral of the first kind appears. You will implement the energy formula and numerically solve the self‑consistency equation for S in the interval (0, 0.5).

## Reproduction target
1) Using U=8 eV, B=1.5 eV, ε₁=ε₂=-U/2, and lattice constant a=1, compute the two energy branches obtained from the static‑fluctuation approximation for the simple Hubbard model at half‑filling. Evaluate the spectrum at the Γ point (k=(0,0)) and at the X point (k=(π,0)). Write the resulting four energy values (two per k‑point) to /app/outputs/energy_spectrum.csv with columns kx, ky, E_plus, E_minus (units eV).  
2) Derive the T=0 limit of the magnetization self‑consistency equation for the same simple‑model parameters. Solve that equation numerically for the magnetization S in the range (0, 0.5] and write the found dimensionless number as a single line to /app/outputs/magnetization_value.txt.

## Assets

- Python 3: python3
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute energy spectrum
- Role: scored (load-bearing)
- Action: For the simple Hubbard model at half-filling, use the static-fluctuation approximation to obtain the energy spectrum. Set U1=U2=U=8 eV, hopping B=1.5 eV, bare site energies ε1=ε2=-U/2, and lattice constant a=1. Compute the renormalized parameters and the resulting dispersion relation. Evaluate the two energy branches at the Brillouin-zone points Γ (k=(0,0)) and X (k=(π,0)).
- Output file: `/app/outputs/energy_spectrum.csv`
- Format: csv
- Contract: CSV with header: kx,ky,E_plus,E_minus. Two rows: Γ (0.0,0.0) and X (π,0.0). All energies in eV.
- Scoring: scored by hidden verifier

### Step 2: Solve magnetization self-consistency equation
- Role: scored (load-bearing)
- Action: Derive the zero‑temperature limit of the self‑consistency equation for the magnetization S from the spectral theorem applied to the two‑sublattice Hubbard model. For the simple case U1=U2=U, ε1=ε2=-U/2, and using the same parameters U=8 eV, B=1.5 eV, obtain a transcendental equation for S. Solve this equation numerically for S in the interval (0,0.5] and report the resulting magnetization (spin per site).
- Output file: `/app/outputs/magnetization_value.txt`
- Format: txt
- Contract: A single line containing the magnetization S as a decimal number (dimensionless).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/energy_spectrum.csv`
- `/app/outputs/magnetization_value.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### energy_spectrum.csv
- path: `/app/outputs/energy_spectrum.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Two rows with eigenvalues at Γ and X. Columns: dimensionless k‑vector components and the two energy branches.
- schema:
  - `type`: table
  - `required_columns`: `kx`, `ky`, `E_plus`, `E_minus`
  - `units`:
    - `kx`: radians per lattice constant
    - `ky`: radians per lattice constant
    - `E_plus`: eV
    - `E_minus`: eV

### magnetization_value.txt
- path: `/app/outputs/magnetization_value.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: The ground‑state magnetization S obtained by solving the zero‑temperature self‑consistency equation.
- schema:
  - `type`: text
  - `required`: Single decimal number representing magnetization S (dimensionless).

Notes: All quantities are deterministic given the specified parameters. The scoring compares against the correct values computed from the same analytical formulas, not against the paper's figure.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "energy_spectrum.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "kx",
          "ky",
          "E_plus",
          "E_minus"
        ],
        "units": {
          "kx": "radians per lattice constant",
          "ky": "radians per lattice constant",
          "E_plus": "eV",
          "E_minus": "eV"
        }
      },
      "description": "Two rows with eigenvalues at Γ and X. Columns: dimensionless k‑vector components and the two energy branches."
    },
    {
      "file": "magnetization_value.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "required": "Single decimal number representing magnetization S (dimensionless)."
      },
      "description": "The ground‑state magnetization S obtained by solving the zero‑temperature self‑consistency equation."
    }
  ],
  "notes": "All quantities are deterministic given the specified parameters. The scoring compares against the correct values computed from the same analytical formulas, not against the paper's figure."
}
```

## How you are scored
A hidden automated verifier independently computes the correct energy eigenvalues and magnetization S from the same analytical expressions and input parameters. It compares your submitted energy_spectrum.csv and magnetization_value.txt to those correct values, checking agreement within predefined numerical tolerances. Each of the two scored outputs contributes a weight to a total reward in [0, 1]. The verifier does NOT simply read a self‑reported number; it recomputes the target quantities from scratch and validates that your outputs are consistent with the physics of the problem. Simply transcribing the paper’s numbers without performing the computation will not pass.

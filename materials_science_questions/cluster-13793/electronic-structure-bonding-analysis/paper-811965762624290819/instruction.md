# Finite-Difference Bloch-Lattice Band Structure Simulation for an FCC Crystal

## Problem background
Chromium nitride (CrN) crystallizes in a rock-salt structure and exhibits a mix of metallic, ionic, and covalent bonding. Its electronic band structure is essential for interpreting electrical, thermal, and mechanical properties. This task computes the band structure using a finite‑difference Bloch‑lattice model: the face‑centred cubic primitive unit cell is discretized on a 3D grid, and the Schrödinger equation is solved numerically under Bloch boundary conditions. The effective potential is an attractive, range‑limited well that mimics the Coulomb interaction between Cr³⁺ and N³⁻ ions, yielding the energy eigenvalues along high‑symmetry directions in the first Brillouin zone.

## Approach
The primitive fcc cell is covered by a regular grid of points. At each grid point a wavefunction value is assigned, and centred finite differences approximate the first derivatives and the Laplacian. Bloch‑periodic boundary conditions couple opposite faces to enforce lattice translation symmetry. The potential inside the cell is modelled as a quadratic well whose shape and depth reflect the Coulomb attraction of the ion pair, while reciprocal‑lattice vectors embed the full lattice periodicity. For every crystal momentum k along the Δ (100), Σ (110), and Λ (111) paths, the discrete Hamiltonian is assembled and diagonalized. The computed eigenvalues, shifted to the Fermi level, are the band energies. The entire workflow is implemented in Python with NumPy and SciPy, and the resulting energies are written to a CSV file.

## Reproduction target
Produce the file `band_structure.csv` containing the band energies E(k) for CrN along the three high‑symmetry directions Δ (Γ→X), Σ (Γ→K), and Λ (Γ→L). Each direction must be sampled with at least 50 uniformly spaced k‑points. The computed energies should display metallic character: at least one band must cross the Fermi level (0 eV) along each direction. The resulting energies should be physically reasonable for a transition‑metal nitride with mixed bonding character, consistent with the general features of CrN’s electronic structure.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Finite‑difference Bloch‑lattice band‑structure computation
- Role: scored (load-bearing)
- Action: Implement the finite‑difference discretization of the Bloch‑Schrödinger equation for an fcc lattice with a range‑limited attractive potential. Use a regular 3D grid inside the primitive unit cell, assign a wavefunction value to each grid point, approximate first derivatives and the Laplacian by centered finite differences, impose Bloch‑periodic boundary conditions, and assemble the discrete eigenvalue problem. Use the explicit potential function from the paper (Eq. 8):

V(x,y,z) = V₀ * [ (x - 3a/4)^2 * (sin(Gx*d))^2 + (y - √3 a/4)^2 * (sin(Gy*d))^2 + (5/3)*(z - a/2)^2 * (sin(Gz*d))^2 + (2√3/3)*(x - 3a/4)*(y - √3 a/4) * (sin(Gx*d))^2 * (sin(Gz*d))^2 ]

where V₀ is the Coulomb potential energy between Cr³⁺ and N³⁻ ions (separation a/2), computed from fundamental constants, and Gx, Gy, Gz are reciprocal‑lattice vector components. Use the fcc primitive vectors with lattice constant a = 4.14 Å, and compute the Coulomb‑based potential strength V₀ from fundamental constants. Sweep k‑points along the high‑symmetry directions Δ (100), Σ (110), and Λ (111) in the first Brillouin zone, with at least 50 uniformly spaced points per direction. For each k‑point solve the eigenvalue problem and collect the computed band energies (relative to the Fermi level) in electron volts. Write the results to band_structure.csv.
- Output file: `/app/outputs/band_structure.csv`
- Format: csv
- Contract: direction: str (one of 'Delta', 'Sigma', 'Lambda'); k_index: int (0‑based sequential index along the direction); kx: float; ky: float; kz: float (crystal momentum components in units of 2π/a); energy: float (energy eigenvalue in eV, relative to the Fermi level)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_structure.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_structure.csv
- path: `/app/outputs/band_structure.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Band energies E(k) computed from the finite-difference Bloch-lattice model. The hidden checker will extract energies at the high-symmetry points Γ, X, K, L and compare them to paper reference values within an appropriate tolerance; it will also verify metallic character (at least one band crossing the Fermi level along each direction).
- schema:
  - `type`: table
  - `required_columns`: `direction`, `k_index`, `kx`, `ky`, `kz`, `energy`
  - `units`:
    - `energy`: eV

Notes: The agent must implement the finite-difference scheme as described; any reasonable grid spacing that yields a converged band structure is acceptable. The hidden tolerance accounts for the expected spread from different discretisation choices and software environments.

## Self-check before finishing (optional, not scored)

Before submitting, verify that your output file `/app/outputs/band_structure.csv` exists and contains exactly the required columns: `direction`, `k_index`, `kx`, `ky`, `kz`, `energy`. This checks shape only—it does not judge scientific correctness.

## How you are scored
A hidden verifier reads your `band_structure.csv` and independently evaluates it. The verifier extracts the energies at the high‑symmetry k‑points Γ, X, K, and L, compares them to reference band energies obtained from the original simulation, and awards a reward that increases as the agreement improves. It also checks that each direction (Δ, Σ, Λ) contains at least one band that crosses the Fermi level (0 eV) within a hidden tolerance. The final reward is a weighted combination of these checks. Submitting a single reported number without the corresponding CSV data will not earn credit.
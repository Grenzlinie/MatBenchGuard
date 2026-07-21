# Ferromagnetic stability and phase sequence in the Ising-Falicov-Kimball model

## Problem background
The Ising–Falicov–Kimball model is a spin-dependent extension of the Falicov–Kimball model that describes itinerant electrons interacting with localized electrons via on-site Coulomb repulsion (U) and Ising-type Hund's coupling (J). On a square lattice, the model supports complex charge and magnetic order. The ground state is determined by the arrangement of localized f-electrons (which can be absent, spin‑up, or spin‑down) that creates an external potential for the itinerant d‑electrons; the system then minimizes its total energy. The present task focuses on constructing a restricted ground‑state phase diagram for the model with U=8 and J=0.5 by considering all periodic configurations of localized electrons with unit‑cell size N0 ≤ 4 (47 configurations). From this diagram we will extract two key quantities: (a) the maximum itinerant‑electron density ρ_d for which the ferromagnetic (F) phase remains the ground state at fixed localized‑electron density ρ_f=1, and (b) the ordered list of ground‑state configuration names and their approximate ρ_d intervals along the line ρ_f + ρ_d/2 = 1 as ρ_d increases from 0 to 2.

## Approach
The restricted phase diagram is built in the grand‑canonical ensemble. First, generate the full trial set of 47 periodic arrangements of localized f‑electrons (including spin) with unit cells containing up to 4 sites. For each configuration, construct the itinerant‑electron Bloch Hamiltonian on a uniform k‑point grid (e.g., 100×100) covering the first Brillouin zone. Diagonalise the resulting matrices (up to 4×4) to obtain spin‑resolved band eigenvalues E_{νσk}. From the eigenvalues compute the spin‑resolved densities of states, electron densities ρ_dσ(μ_d), total electronic energy, and the Gibbs thermodynamic potential E_{gc} for a grid of chemical potentials μ_d and μ_f. The ground‑state configuration at each (μ_d, μ_f) point is the one with the lowest Gibbs potential; this yields the grand‑canonical phase diagram. The diagram is then translated to the canonical (ρ_d, ρ_f) plane by mapping the chemical potentials to the corresponding electron densities. From this canonical diagram we extract the two target quantities: (a) the largest ρ_d where F is the ground state along the line ρ_f=1, and (b) the sequence of ground‑state configurations (labelled as F, E, AF, D1–D5, 1–4, etc.) and the ρ_d boundaries along the diagonal line ρ_f + ρ_d/2 = 1 from ρ_d = 0 to 2.

## Reproduction target
Compute the restricted ground‑state phase diagram of the Ising‑Falicov‑Kimball model on a square lattice for U = 8 and J = 0.5. From this diagram determine:
- The maximum itinerant‑electron density ρ_d at which the ferromagnetic (F) phase is the ground state at fixed localized‑electron density ρ_f = 1.
- The ordered list of ground‑state configuration names and their approximate ρ_d intervals along the line ρ_f + ρ_d/2 = 1 as ρ_d increases from 0 to 2.
Output both results in `/app/outputs/results.json`.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Generate trial configurations of localized electrons
- Role: process
- Action: Enumerate all periodic arrangements of localized f-electrons (including spin orientations) with unit-cell sites N0 ≤ 4, yielding the 47 distinct configurations that define the restricted configurational space. Each configuration specifies on each site whether the f-electron is absent (0), present with spin-up (↑), or present with spin-down (↓).
- Evidence: `/app/outputs/trial_configurations.json`

### Step 2: Compute itinerant-electron band eigenvalues for each configuration
- Role: process
- Action: For each configuration, construct the itinerant-electron Bloch Hamiltonian on a uniform k-point grid (e.g., 100×100) covering the first Brillouin zone. Diagonalize the resulting matrices (up to 4×4) to obtain spin-resolved band eigenvalues E_{νσk}.
- Evidence: `/app/outputs/band_eigenvalues.npz`

### Step 3: Construct phase diagrams and extract target quantities
- Role: scored (load-bearing)
- Action: From the band eigenvalues, compute the spin-resolved densities of states, electron densities, total energy, and Gibbs thermodynamic potential for each configuration over a grid of chemical potentials μ_d and μ_f. Determine the ground-state configuration (lowest Gibbs potential) at each (μ_d, μ_f) point to construct the grand-canonical phase diagram, then translate it to the canonical (ρ_d, ρ_f) diagram. Extract (a) the maximum itinerant-electron density ρ_d for which the ferromagnetic (F) phase is the ground state at fixed ρ_f=1, and (b) the ordered list of ground-state configuration names and their approximate ρ_d ranges along the line ρ_f+ρ_d/2=1 as ρ_d increases from 0 to 2. Output these in results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"critical_rho_d_ferromagnetic": number, "diagonal_sequence": [{"rho_d": number, "configuration": string}]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Critical itinerant-electron density for ferromagnetic stability at ρ_f=1 and the ordered list of ground-state configurations with their ρ_d values along the line ρ_f+ρ_d/2=1.
- schema:
  - `type`: object
  - `required`:
    - `critical_rho_d_ferromagnetic`: float
    - `diagonal_sequence`: array
  - `items`:
    - `rho_d`: float
    - `configuration`: string

Notes: The expected configuration sequence for the diagonal line, from low ρ_d to high, is: D1, D2, D3, D4, D5 (appearing between the ferromagnetic F and the empty E phases). The critical ferromagnetic density is approximately 0.131 at U=8, J=0.5. The hidden checker will verify the reported list and the critical value against the paper's results.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "critical_rho_d_ferromagnetic": "float",
          "diagonal_sequence": "array"
        },
        "items": {
          "rho_d": "float",
          "configuration": "string"
        }
      },
      "description": "Critical itinerant-electron density for ferromagnetic stability at ρ_f=1 and the ordered list of ground-state configurations with their ρ_d values along the line ρ_f+ρ_d/2=1."
    }
  ],
  "notes": "The expected configuration sequence for the diagonal line, from low ρ_d to high, is: D1, D2, D3, D4, D5 (appearing between the ferromagnetic F and the empty E phases). The critical ferromagnetic density is approximately 0.131 at U=8, J=0.5. The hidden checker will verify the reported list and the critical value against the paper's results."
}
```

## How you are scored
A hidden verifier will inspect the `results.json` file you produce. It compares your reported `critical_rho_d_ferromagnetic` against a hidden reference value (derived from the original study) with a predetermined tolerance. It also checks whether the sequence of configuration names along the diagonal line and their associated ρ_d values match the expected order and approximate boundaries. Each of the two quantities carries a portion of the total reward. The final score (0 to 1) is computed from how close your numbers are to the hidden references. You do not need to know the reference values; just carry out the computation faithfully.

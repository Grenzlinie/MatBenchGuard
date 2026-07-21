# Ideal (001) Surface Band Structure Computation for Chalcopyrite Series

## Problem background
Semiconducting chalcopyrites of the form CuB(III)C2(VI) (B = Al, Ga, In; C = S, Se, Te) are widely studied for photovoltaics, non-linear optics, and catalysis. The electronic structure of their surfaces is critical because surface states within the band gap and higher-energy regions influence charge transport and interface properties. This task addresses the ideal (001) surface band structure for the complete chalcopyrite series. By computing the surface state energies from first-principles tight‑binding, one can systematically examine trends as the group‑III cation and chalcogen anion change.

## Approach
The calculation uses the tight‑binding (TB) method in an orthogonal Slater–Koster basis. Bulk Hamiltonian matrices are constructed for the body‑centred tetragonal chalcopyrite structure (I‑42d) using published TB parameters. To treat the (001) surface, the crystal is divided into principal layers, each consisting of eight consecutive atomic planes. Only nearest‑neighbour interactions between layers are kept. The surface Green’s function is obtained via the surface Green’s function matching (SGFM) formalism, employing a transfer‑matrix algorithm to satisfy the matching conditions at the surface. Surface states are then located as poles of the surface Green’s function at the high‑symmetry points Γ, X, and M of the two‑dimensional (001) surface Brillouin zone.

## Reproduction target
Compute, for all nine compounds (CuAlS2, CuAlSe2, CuAlTe2, CuGaS2, CuGaSe2, CuGaTe2, CuInS2, CuInSe2, CuInTe2), the energies (eV) of the surface states labelled E1 through E7 at the high‑symmetry k‑points Γ, X, and M of the (001) surface Brillouin zone. Write the results to `/app/outputs/surface_state_energies.csv` with columns: `compound` (e.g., CuAlS2), `state` (one of E1 … E7), `kpoint` (Gamma, X, or M), and `energy_eV` (floating‑point number). The file must contain exactly 189 rows (9 compounds × 7 states × 3 k‑points).

## Assets

- Tight-binding parameters for Cu-based chalcopyrites: 10.1103/PhysRevB.59.1555

## Workflow steps

### Step 1: Construct the tight-binding Hamiltonian and principal-layer blocks
- Role: process
- Action: For each of the nine CuB(III)C2(VI) chalcopyrite compounds (B=Al,Ga,In; C=S,Se,Te), build the 42×42 orthogonal Slater–Koster TB Hamiltonian using the published parameters. Construct the 8-plane principal-layer blocks H00 and H01 for the ideal (001) surface, preserving the nearest-neighbour interaction scheme required by the SGFM method.
- Evidence: `/app/outputs/tb_hamiltonian_blocks.npz`

### Step 2: Run the surface Green's function matching calculation
- Role: process
- Action: Using the principal-layer blocks from the previous step, implement the SGFM method with transfer-matrix algorithm to compute the surface Green's function G_S for the ideal (001) surface of each compound. The calculation must cover the high-symmetry points Γ, X, M of the 2D surface Brillouin zone.
- Evidence: `/app/outputs/sgfm_green_function.npz`

### Step 3: Extract surface state energies
- Role: scored (load-bearing)
- Action: From the computed surface Green's function, locate the poles that correspond to the surface states E1–E7. Record their energies at the Γ, X, and M points for all nine compounds. Save the results to a single CSV file.
- Output file: `/app/outputs/surface_state_energies.csv`
- Format: csv
- Contract: CSV with columns: compound (str, e.g. CuAlS2), state (str, one of E1...E7), kpoint (str, Gamma|X|M), energy_eV (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/surface_state_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### surface_state_energies.csv
- path: `/app/outputs/surface_state_energies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Energies of the seven surface states E1–E7 at the Γ, X, M high-symmetry points for all nine compounds. The checker compares each energy against the paper’s reported reference values using a tolerance that accounts for implementation-dependent numerical differences.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `state`, `kpoint`, `energy_eV`
  - `units`:
    - `energy_eV`: eV

Notes: The energies are extracted from the SGFM computation and reported to three decimal places. The CSV must contain exactly 189 rows (9 compounds × 7 states × 3 k-points). The checker will compare each energy value to a hidden gold derived from the source publication; no gold values or tolerances are disclosed here.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "surface_state_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "state",
          "kpoint",
          "energy_eV"
        ],
        "units": {
          "energy_eV": "eV"
        }
      },
      "description": "Energies of the seven surface states E1–E7 at the Γ, X, M high-symmetry points for all nine compounds. The checker compares each energy against the paper’s reported reference values using a tolerance that accounts for implementation-dependent numerical differences."
    }
  ],
  "notes": "The energies are extracted from the SGFM computation and reported to three decimal places. The CSV must contain exactly 189 rows (9 compounds × 7 states × 3 k-points). The checker will compare each energy value to a hidden gold derived from the source publication; no gold values or tolerances are disclosed here."
}
```

## How you are scored
A hidden verifier independently inspects every output file listed in the workflow. For the final CSV (`surface_state_energies.csv`), the verifier compares each energy entry against a reference using a tolerance that absorbs legitimate implementation‑dependent differences. The reward for that stage is the fraction of entries falling within tolerance. Intermediate artifacts are checked for existence and basic structural properties (e.g., expected dimensions, presence of required columns). The overall score is a weighted sum of the stage rewards, with the surface‑state energies carrying the highest weight. The only way to obtain a high score is to produce surface‑state energies that faithfully reflect the result of the SGFM computation; reporting numbers from a published table without executing the full tight‑binding + SGFM pipeline will not pass.

# Curie temperature versus carrier density in a minimal three-band tight-binding model with classical localized spins

## Problem background
Ordered double perovskites such as Sr₂FeMoO₆ exhibit ferromagnetism that is widely believed to arise from the interplay between itinerant conduction electrons (in t₂g orbitals) and large localized Fe spins (S=5/2), which are coupled antiferromagnetically by a strong Hund's coupling. The conduction electron density c can be tuned by chemical doping. A fundamental open question is how the Curie temperature Tc depends on the carrier density. This task addresses that question by using a minimal tight-binding model that incorporates the essential electronic structure and magnetic couplings, and computes Tc as a function of c within a mean-field virtual-crystal approximation.

## Approach
Use a mean-field treatment of the three degenerate two-dimensional t₂g tight-binding bands (xy, yz, zx) on a square lattice that represents the Fe-Mo sub-lattice of a double perovskite. The Hamiltonian includes an on-site energy difference J−Δ between Fe and Mo sites, Fe–Mo hopping t_Fe‑Mo, and Mo–Mo hopping t_Mo‑Mo; the Fe spin‑parallel level is taken as infinitely high. Localized Fe spins are treated as classical unit vectors, with magnetization defined as m ≡ ⟨cos θ⟩. In the paramagnetic regime the hopping amplitudes are expressed in terms of m using the expansion ⟨cos(θ/2)⟩ ≈ 2/3 + (2/5)m² and ⟨sin(θ/2)⟩ ≈ 2/3 – (2/5)m². For each electron density c ∈ [0,2], build the mean-field Hamiltonian as a function of m² on a sufficiently dense k-mesh, diagonalise it, and sum the kinetic energies of the occupied states (at zero electronic temperature) to obtain E_KE(m²). From this, extract the electronic susceptibility χ = ∂E_KE/∂(m²) at m=0 by finite differences. The Curie temperature follows from k_B T_C = −(2/3)χ, with k_B = 8.617333262145×10⁻⁵ eV/K. Repeat for at least 20 evenly spaced c values and write the (c, T_C) pairs to a CSV file.

## Reproduction target
For the parameter set J−Δ = 0.3 eV, t_Fe‑Mo = 0.3 eV, t_Mo‑Mo = 0.15 eV, compute the Curie temperature T_C (in Kelvin) as a function of the conduction‑electron density per Fe, c, for c ranging from 0 to 2. Produce a CSV file `/app/outputs/Tc_vs_c.csv` with a header row 'c,Tc_K' followed by data rows with two columns: c (float) and Tc_K (float), containing at least 20 rows covering the interval [0, 2]. Each row gives the Tc computed via the mean‑field susceptibility formula for that electron density.

## Assets

- NumPy: https://pypi.org/project/numpy/
- SciPy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Compute Tc(c) curve for the base mean‑field model
- Role: scored (load-bearing)
- Action: Implement the mean-field virtual-crystal approximation for three degenerate t2g tight-binding bands (xy, yz, zx) on a two-dimensional square lattice. Model parameters: on-site energy difference between Fe and Mo sites J−Δ=0.3 eV, Fe–Mo hopping t_Fe‑Mo=0.3 eV, Mo–Mo hopping t_Mo‑Mo=0.15 eV; the Fe spin-parallel level is effectively infinite. Treat localized Fe spins as classical unit vectors, define magnetization m ≡ ⟨cos θ⟩, and expand the hopping coefficients ⟨cos(θ/2)⟩ and ⟨sin(θ/2)⟩ to second order in m (⟨cos⟩ ≈ 2/3 + (2/5)m², ⟨sin⟩ ≈ 2/3 – (2/5)m²). For each electron density c ∈ [0, 2] (at least 20 evenly spaced values), solve the mean-field Hamiltonian at zero electronic temperature to obtain the total kinetic energy E_KE as a function of m², extract the electronic susceptibility χ = ∂E_KE/∂(m²) at m=0, and compute the Curie temperature via k_B T_C = −(2/3)χ (k_B = 8.617333262145×10⁻⁵ eV K⁻¹). Write the results to a CSV file.
- Output file: `/app/outputs/Tc_vs_c.csv`
- Format: csv
- Contract: CSV file with a header row 'c,Tc_K', followed by data rows with columns: 'c' (float, electron density per Fe) and 'Tc_K' (float, Curie temperature in Kelvin). At least 20 rows covering c from 0 to 2.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/Tc_vs_c.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### Tc_vs_c.csv
- path: `/app/outputs/Tc_vs_c.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Tc(c) data from the base mean-field model, to be compared against the paper-reported curve for the same parameters.
- schema:
  - `type`: table
  - `has_header`: True
  - `columns`: `c`, `Tc_K`
  - `units`:
    - `c`: electrons per Fe
    - `Tc_K`: Kelvin

Notes: Only the base mean-field model (dispersive Mo bands, no Hubbard U) is scored. The effective Heisenberg couplings and Hubbard-U results are excluded from this task per scope.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "Tc_vs_c.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "has_header": true,
        "columns": [
          "c",
          "Tc_K"
        ],
        "units": {
          "c": "electrons per Fe",
          "Tc_K": "Kelvin"
        }
      },
      "description": "Tc(c) data from the base mean-field model, to be compared against the paper-reported curve for the same parameters."
    }
  ],
  "notes": "Only the base mean-field model (dispersive Mo bands, no Hubbard U) is scored. The effective Heisenberg couplings and Hubbard-U results are excluded from this task per scope."
}
```

## How you are scored
The hidden verifier will read your Tc_vs_c.csv and compare its contents to a reference Tc(c) curve that represents the correct solution of the mean‑field model with the given parameters. The verifier checks the pointwise agreement (within allowed error margins) between your Tc values and the reference. The final reward (a number between 0 and 1) is based on the closeness of your computed curve to the reference curve. Simply copying the correct Tc values without performing the required computation will be detected by structural and consistency checks.

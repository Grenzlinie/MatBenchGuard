# Thermodynamic Properties of Asymmetric Hubbard Model via Finite-Temperature Lanczos Method

## Problem background
The extended Falicov-Kimball model for spinless fermions can be mapped onto an asymmetric Hubbard model (AHM) in which the two orbital flavours become an effective spin degree of freedom with different hopping amplitudes t↑ and t↓. The model exhibits a broken SU(2) symmetry, an on-site Coulomb repulsion U^fd, and a pseudo-magnetic field Bz that couples to the population difference. The present task computes finite-temperature thermodynamic properties of the AHM on a 4×4 square lattice using the finite-temperature Lanczos method with phase averaging, and also computes the same properties for an effective S=1/2 XXZ model on 20 sites, defined by parameters derived from the AHM in the strong-coupling limit.

## Approach
The core numerical technique is the finite-temperature Lanczos method (FTLM) supplemented by random phase averaging. For the AHM, the Hamiltonian is diagonalized in a Krylov subspace built from a random initial vector, and the process is repeated for several random phases representing twisted boundary conditions; thermodynamic averages are obtained from the resulting approximate level densities. For the XXZ model, an exact diagonalization on a 20-site cluster suffices due to the smaller Hilbert space. The workflow requires implementing both the AHM solver (4×4 periodic lattice) and the XXZ solver, and computing the specific heat per site C_V(T) and the magnetization per site M(T) for three cases: (i) AHM with symmetric hopping t↑ = t↓ = 1, (ii) AHM with asymmetric hopping t↑/t↓ = 0.3, and (iii) the effective XXZ model with couplings Jz = 2(t↑² + t↓²)/U^fd and J⊥ = 4 t↑ t↓/U^fd, all at half-filling (n=1), U^fd = 8, Bz = 0. The temperature grid should cover T/t↓ from 0.05 to 2.0. The specific heat and magnetization are to be written to a single CSV file; no further post-processing is required.

## Reproduction target
Produce a CSV file `thermodynamic_properties.csv` under `/app/outputs` with columns `T` (temperature in units of t↓), `C_V` (specific heat per site), `M` (magnetization per site) and `h_model` (a string set to `AHM_sym`, `AHM_asym` or `XXZ_asym`). The file must contain results for the three model cases over the temperature range T/t↓ = 0.05 to 2.0. The hidden checker will evaluate the computed C_V and M curves against benchmark values; the scoring function is not disclosed.

## Assets

- Python 3
- NumPy: numpy
- SciPy: scipy
- Finite-temperature Lanczos method reference: 10.1080/000187300243381

## Workflow steps

### Step 1: Compute thermodynamic data for AHM and XXZ models
- Role: scored (load-bearing)
- Action: Implement the finite-temperature Lanczos method with phase averaging for the asymmetric Hubbard model on a 4×4 square lattice with periodic boundary conditions. Implement a solver for the S=1/2 XXZ model on 20 sites. Run simulations at half-filling n=1, U^{fd}=8, B_z=0 for: (i) AHM with symmetric hopping t_↑=t_↓=1, (ii) AHM with asymmetric hopping t_↑/t_↓=0.3, and (iii) XXZ model for the asymmetric parameters using effective couplings J_z=2(t_↑²+t_↓²)/U^{fd} and J_⊥=4t_↑t_↓/U^{fd}. For each case compute the specific heat C_V(T) per site and magnetization M(T) per site on a temperature grid T/t_↓ from 0.05 to 2.0. Output all data to a CSV file.
- Output file: `/app/outputs/thermodynamic_properties.csv`
- Format: csv
- Contract: CSV with columns: T (float, temperature in units of t_↓), C_V (float, specific heat per site), M (float, magnetization per site), h_model (string, one of 'AHM_sym', 'AHM_asym', 'XXZ_asym'). One row per temperature and model.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermodynamic_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermodynamic_properties.csv
- path: `/app/outputs/thermodynamic_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed specific heat and magnetization curves for the AHM (symmetric and asymmetric) and the effective XXZ model at half-filling.
- schema:
  - `type`: table
  - `required_columns`: `T`, `C_V`, `M`, `h_model`
  - `units`:
    - `T`: t_↓
    - `C_V`: per site
    - `M`: per site

Notes: The hidden checker will evaluate the computed thermodynamic data against reference values. The scoring function is not disclosed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermodynamic_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "C_V",
          "M",
          "h_model"
        ],
        "units": {
          "T": "t_↓",
          "C_V": "per site",
          "M": "per site"
        }
      },
      "description": "Computed specific heat and magnetization curves for the AHM (symmetric and asymmetric) and the effective XXZ model at half-filling."
    }
  ],
  "notes": "The hidden checker will evaluate the computed thermodynamic data against reference values. The scoring function is not disclosed."
}
```

## How you are scored
A hidden verifier will read your `thermodynamic_properties.csv` and compare the computed specific heat and magnetization curves to expected results. The specific metrics are not disclosed, but they are based on the physics described in the paper. A submission generated by an appropriate numerical simulation is expected to score highly.

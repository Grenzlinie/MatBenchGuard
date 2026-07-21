# Monte Carlo Simulation of Magnetic and Configurational Properties of a Self-Avoiding Walk Ising Polymer Chain

## Problem background
Organic magnetic polymers have attracted interest due to their potential for flexible, transparent, and low-density magnetic materials. Understanding the interplay between magnetic ordering and chain conformation is central to their design. This work focuses on a model polymer chain that carries Ising spins on each monomer and whose spatial configuration is a self-avoiding walk on a simple cubic lattice. The chain is subject to a nearest-neighbour ferromagnetic exchange interaction (J>0) and, in the tail-like case, one end is permanently anchored to an impenetrable flat surface. The study aims to determine whether such a chain exhibits spontaneous magnetization and a concomitant collapse transition as temperature is lowered, and to quantify how the flat surface modifies the chain's magnetic, energetic, and configurational properties relative to an unconstrained free chain. The key quantities to be computed are the temperature-dependent mean absolute magnetization, mean square magnetization, mean energy per monomer, specific heat, mean-square end-to-end distance, mean-square radius of gyration, average number of nearest neighbours, and the number of monomers in contact with the surface. The critical temperature and the magnitude of surface-induced changes in chain size and surface contact are open targets of the reproduction.

## Approach
The model is a three-dimensional self-avoiding walk on a simple cubic lattice, with each monomer carrying an Ising spin σ_i = ±1. The Hamiltonian includes only nearest-neighbour ferromagnetic interactions J=1 between monomers that occupy adjacent lattice sites. The spatial configuration is updated by random monomer moves that preserve self-avoidance and the allowed bond vector set; spin configurations are updated by single spin flips. Both types of moves are accepted according to the Metropolis criterion, ensuring Boltzmann statistics at temperature T (in units J/k_B). One Monte Carlo step (MCS) consists of n monomer move attempts and n spin flip attempts.

Two chain types are simulated: a free chain in unbounded space, and a tail-like chain whose first monomer is immobile at (0,0,1) and all monomers are forbidden to occupy the plane z=0 (an impenetrable flat surface). Both chains have length n=300.

The simulation proceeds by equilibrating the chain at each temperature of interest, then recording 500 independent configurations separated by a time interval of Δt = n² MCS. Results are averaged over 500 independent initial chain configurations to reduce statistical noise. Temperatures are chosen to span a range from well below to well above the expected critical region, with a finer temperature step near the critical point.

For each temperature, the following observables are computed:
- mean absolute magnetization ⟨|M|⟩ = ⟨|Σσ_i|⟩/n
- mean square magnetization ⟨M²⟩ = ⟨(Σσ_i)²⟩/n²
- mean energy per monomer ⟨E⟩ = ⟨H⟩/n
- specific heat Cv = (⟨E²⟩−⟨E⟩²)/T²
- mean-square end-to-end distance ⟨R²⟩
- mean-square radius of gyration ⟨S²⟩
- average number of nearest neighbours ⟨N_nn⟩ (tail-like only)
- average number of monomers in contact with the surface ⟨N₁⟩ (tail-like only, where a monomer at z=1 is considered in contact).
All results are saved to results.csv, which must contain columns for temperature T and the tail-like and free values for each quantity except N_nn and N₁, which are tail-specific.

## Reproduction target
Produce a CSV file, results.csv, that contains the temperature-dependent values of the observables listed above for the tail-like and free Ising chains of length n=300 on a simple cubic lattice. The file must cover a temperature range that includes the critical region, with at least 20 distinct temperature points spanning from low temperature (where magnetization is expected to be high) to high temperature (where magnetization is expected to vanish).

From the tabulated magnetization and specific heat data, the critical temperature Tc of the magnetic/collapse transition can be identified (e.g., by locating the steepest change in ⟨|M|⟩ or the maximum of Cv). The data must allow an assessment of whether the flat surface affects the magnetic or energetic properties (by comparing tail and free chain results) and whether it alters the chain size (by comparing ⟨R²⟩ and ⟨S²⟩ between the two chain types). The trend of the surface contact number ⟨N₁⟩ with temperature should also be deducible. The target is a self-contained numerical simulation that yields quantitative results conforming to the expected physical trends.

## Assets

- Python scientific computing packages (numpy, numba): pip install numpy numba

## Workflow steps

### Step 1: Monte Carlo Simulation and Observable Calculation
- Role: scored (load-bearing)
- Action: Implement a dynamic Monte Carlo simulation for a 3D self-avoiding-walk Ising chain on a simple cubic lattice with nearest-neighbour ferromagnetic coupling (J=1). For chain length n=300, simulate both a free chain and a tail-like chain grafted to an impenetrable flat surface at z=0. Use Metropolis updates (spatial moves + spin flips) with one MCS = n monomer moves + n spin flips. After equilibration, record 500 independent configurations at intervals Δt=n² MCS for each temperature from about 0.7 to 2.0 (step ΔT=0.05 near Tc). Average over 500 initial chain configurations. For each temperature, compute: mean absolute magnetization <|M|>, mean square magnetization <M²>, mean energy per monomer <E>, specific heat Cv = (<E²>-<E>²)/T², mean-square end-to-end distance <R²>, mean-square radius of gyration <S²> for both chain types; for the tail-like chain also compute average number of nearest neighbours <N_nn> and average number of monomers in contact with the surface <N₁>. Save all results into results.csv.
- Output file: `/app/outputs/results.csv`
- Format: csv
- Contract: CSV with columns: T, M_abs_tail, M_abs_free, M2_tail, M2_free, E_tail, E_free, Cv_tail, Cv_free, R2_tail, R2_free, S2_tail, S2_free, N_nn_tail, N1_tail
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.csv
- path: `/app/outputs/results.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Computed temperature-dependent magnetic and configurational properties for both tail-like and free Ising polymer chains of length n=300, covering a temperature range that includes the critical region.
- schema:
  - `type`: table
  - `required_columns`: `T`, `M_abs_tail`, `M_abs_free`, `M2_tail`, `M2_free`, `E_tail`, `E_free`, `Cv_tail`, `Cv_free`, `R2_tail`, `R2_free`, `S2_tail`, `S2_free`, `N_nn_tail`, `N1_tail`
  - `units`:
    - `T`: J/kB
    - `M_abs_tail`: dimensionless
    - `M_abs_free`: dimensionless
    - `M2_tail`: dimensionless
    - `M2_free`: dimensionless
    - `E_tail`: J
    - `E_free`: J
    - `Cv_tail`: kB
    - `Cv_free`: kB
    - `R2_tail`: (lattice units)^2
    - `R2_free`: (lattice units)^2
    - `S2_tail`: (lattice units)^2
    - `S2_free`: (lattice units)^2
    - `N_nn_tail`: dimensionless
    - `N1_tail`: dimensionless

Notes: All columns must be present. At least 20 temperature points including values below and above Tc should be provided. The simulation and observable calculation must follow the method described in the step action; no pre-computed values should be used.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "M_abs_tail",
          "M_abs_free",
          "M2_tail",
          "M2_free",
          "E_tail",
          "E_free",
          "Cv_tail",
          "Cv_free",
          "R2_tail",
          "R2_free",
          "S2_tail",
          "S2_free",
          "N_nn_tail",
          "N1_tail"
        ],
        "units": {
          "T": "J/kB",
          "M_abs_tail": "dimensionless",
          "M_abs_free": "dimensionless",
          "M2_tail": "dimensionless",
          "M2_free": "dimensionless",
          "E_tail": "J",
          "E_free": "J",
          "Cv_tail": "kB",
          "Cv_free": "kB",
          "R2_tail": "(lattice units)^2",
          "R2_free": "(lattice units)^2",
          "S2_tail": "(lattice units)^2",
          "S2_free": "(lattice units)^2",
          "N_nn_tail": "dimensionless",
          "N1_tail": "dimensionless"
        }
      },
      "description": "Computed temperature-dependent magnetic and configurational properties for both tail-like and free Ising polymer chains of length n=300, covering a temperature range that includes the critical region."
    }
  ],
  "notes": "All columns must be present. At least 20 temperature points including values below and above Tc should be provided. The simulation and observable calculation must follow the method described in the step action; no pre-computed values should be used."
}
```

## How you are scored
A hidden verifier will read your results.csv and perform a series of structural checks without direct access to the paper's values. The checks include:
- Extracting the critical temperature from your data (via the steepest change in magnetization and/or the specific heat peak) and verifying that it falls within a narrow expected range.
- Confirming that the magnetization at the lowest temperature is large and at the highest temperature is small.
- Comparing the tail-like and free chain results to verify that the surface has no substantial effect on magnetization and energy (differences must be below an acceptable tolerance).
- Checking that the mean-square end-to-end distance and radius of gyration of the tail-like chain are consistently larger than those of the free chain.
- Verifying that the number of monomers in contact with the surface increases as temperature decreases below the critical region.
- Confirming that the specific heat exhibits a clear maximum within the expected critical range.
Each check is evaluated as pass/fail, and the final reward is the fraction of checks passed (a number between 0 and 1). Reporting the paper's published numbers is not sufficient; the verifier recomputes criteria directly from your output.

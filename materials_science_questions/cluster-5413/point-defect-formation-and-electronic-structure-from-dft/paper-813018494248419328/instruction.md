# Point defect formation and electronic structure from DFT

## Problem background
Tungsten (W) is a leading plasma-facing material candidate in fusion reactors; however, neutron irradiation transmutes W into rhenium (Re), which can influence hydrogen isotope retention. This task investigates the effect of Re on hydrogen (H) trapping at vacancy-type defects in W using first-principles density functional theory (DFT). The central quantity of interest is how Re atoms, especially when clustered at a vacancy, affect the H trapping energy and the maximum number of H atoms that can be retained at room temperature.

## Approach
Use first-principles DFT calculations with an open-source code (e.g., Quantum ESPRESSO) and GGA-PBE pseudopotentials. Build bcc W supercells (128 atoms, lattice constant 3.1656 Å) containing: a perfect W reference, a mono-vacancy (V), and Re_m–V complexes for m = 1 to 8, with Re atoms placed in their known ground-state configurations. Insert H atoms at off-vacancy-center octahedral interstitial sites. Compute total energies for all systems and for an isolated H2 molecule. From these total energies, compute the trapping energy of a single H in each Re_m–V complex (m = 0 corresponds to the pure vacancy) relative to a H atom at the tetrahedral interstitial site in pure W. Decompose the H solution energy into a mechanical contribution (MC, from lattice deformation) and an electronic contribution (EC). For the Re4–V complex, compute the sequential trapping energy as H atoms are added one by one until the trapping energy becomes positive. Finally, for the pure vacancy, Re1–V, and Re4–V complexes, use the sequential trapping energies together with the Polanyi‑Wigner equation (heating rate 1 K s⁻¹, attempt frequency 25 THz, diffusion barrier 0.18 eV) to determine the maximum release temperature T_max for each H and whether it is retained at 300 K.

## Reproduction target
Produce three comma-separated value (CSV) files with the precise schemas given under “Output contract”:

- **trapping_energies.csv**: for m = 0 (pure vacancy) up to m = 8, report the trapping energy (eV), MC contribution (eV), and EC contribution (eV) for a single H atom.

- **multiH_Re4V_trapping_energies.csv**: for the Re4–V complex, report for n = 1, 2, …, N (where N is the smallest integer for which the trapping energy turns positive) the sequential trapping energy (eV) of the n‑th H atom.

- **retention_analysis.csv**: for the pure vacancy, Re1–V, and Re4–V, report for each H index n (until the trapping energy becomes positive) the computed T_max (K) and a boolean indicating whether the H is retained at room temperature (T_max > 300 K).

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotential library (GGA-PBE efficiency subset): https://www.materialscloud.org/discover/sssp/table/efficiency/
- Python 3 with numpy, scipy, pandas: python3,python3-numpy,python3-scipy,python3-pandas

## Workflow steps

### Step 1: Prepare supercell models
- Role: process
- Action: Generate all required supercell structures for bcc W (lattice constant 3.1656 Å) with and without defects: pure W, W with a mono-vacancy (V), W with Re_m-V complexes for m=1–8 using literature ground-state configurations, and with H atoms placed at candidate interstitial sites (off-vacancy-center OIS). Create input files for Quantum ESPRESSO SCF calculations.
- Evidence: none

### Step 2: Run DFT total-energy calculations
- Role: process
- Action: Perform DFT SCF calculations for all supercells (pure W, V, Re_m-V complexes, with and without H) using Quantum ESPRESSO with GGA-PBE pseudopotentials, k-point sampling 3×3×3, wavefunction cutoff 50 Ry, charge density cutoff 400 Ry. Also compute the energy of an isolated H2 molecule. Extract total energies for all systems.
- Evidence: none

### Step 3: Calculate trapping energies and MC/EC decomposition for single H in Re_m-V
- Role: scored
- Action: From DFT total energies, compute the trapping energy of a single H in Re_m-V complexes (m=0 for pure vacancy, m=1–8) according to the formula: E_trap = E(Re_m-V-H) - E(Re_m-V) - [E(W,TIS-H) - E(W)], where the reference is a H atom at TIS in pure W. Decompose the H solution energy into mechanical (MC) and electronic (EC) contributions as described in the method.
- Output file: `/app/outputs/trapping_energies.csv`
- Format: csv
- Contract: m: int, trapping_energy_eV: float, MC_eV: float, EC_eV: float
- Scoring: scored by hidden verifier

### Step 4: Calculate sequential H trapping energies in Re4-V
- Role: scored
- Action: For the Re4-V complex, compute the sequential trapping energy for each H atom added (n=1,2,...) using total energies of Re4-V-H_n and Re4-V-H_{n-1} and the reference TIS H energy, until the trapping energy becomes positive.
- Output file: `/app/outputs/multiH_Re4V_trapping_energies.csv`
- Format: csv
- Contract: n: int, trapping_energy_eV: float
- Scoring: scored by hidden verifier

### Step 5: Retention analysis with Polanyi-Wigner equation
- Role: scored (load-bearing)
- Action: Using the trapping energies computed for pure vacancy (m=0), Re1-V, and Re4-V for each sequential H, solve the Polanyi-Wigner equation numerically (heating rate 1 K/s, attempt frequency 25 THz, diffusion barrier 0.18 eV) to find T_max for each H. Determine whether T_max > 300 K (retained at RT).
- Output file: `/app/outputs/retention_analysis.csv`
- Format: csv
- Contract: system: str, n: int, T_max_K: float, retained_at_RT: bool
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/trapping_energies.csv`
- `/app/outputs/multiH_Re4V_trapping_energies.csv`
- `/app/outputs/retention_analysis.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### trapping_energies.csv
- path: `/app/outputs/trapping_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Trapping energy, mechanical and electronic contributions for a single H in pure vacancy (m=0) and Re_m-V complexes (m=1..8).
- schema:
  - `type`: table
  - `required_columns`: `m`, `trapping_energy_eV`, `MC_eV`, `EC_eV`
  - `units`:
    - `trapping_energy_eV`: eV
    - `MC_eV`: eV
    - `EC_eV`: eV

### multiH_Re4V_trapping_energies.csv
- path: `/app/outputs/multiH_Re4V_trapping_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Sequential trapping energy for H atoms added to Re4-V complex.
- schema:
  - `type`: table
  - `required_columns`: `n`, `trapping_energy_eV`
  - `units`:
    - `trapping_energy_eV`: eV

### retention_analysis.csv
- path: `/app/outputs/retention_analysis.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Retention analysis: maximum release temperature and whether retained at 300 K for pure vacancy, Re1-V, and Re4-V.
- schema:
  - `type`: table
  - `required_columns`: `system`, `n`, `T_max_K`, `retained_at_RT`
  - `units`:
    - `T_max_K`: K
    - `retained_at_RT`: bool

Notes: All energies in eV, temperatures in K. The checker will recompute T_max from submitted trapping energies for retention analysis and compare the maximum number of retained H at 300 K to a hidden reference.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "trapping_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "m",
          "trapping_energy_eV",
          "MC_eV",
          "EC_eV"
        ],
        "units": {
          "trapping_energy_eV": "eV",
          "MC_eV": "eV",
          "EC_eV": "eV"
        }
      },
      "description": "Trapping energy, mechanical and electronic contributions for a single H in pure vacancy (m=0) and Re_m-V complexes (m=1..8)."
    },
    {
      "file": "multiH_Re4V_trapping_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "n",
          "trapping_energy_eV"
        ],
        "units": {
          "trapping_energy_eV": "eV"
        }
      },
      "description": "Sequential trapping energy for H atoms added to Re4-V complex."
    },
    {
      "file": "retention_analysis.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "n",
          "T_max_K",
          "retained_at_RT"
        ],
        "units": {
          "T_max_K": "K",
          "retained_at_RT": "bool"
        }
      },
      "description": "Retention analysis: maximum release temperature and whether retained at 300 K for pure vacancy, Re1-V, and Re4-V."
    }
  ],
  "notes": "All energies in eV, temperatures in K. The checker will recompute T_max from submitted trapping energies for retention analysis and compare the maximum number of retained H at 300 K to a hidden reference."
}
```

## How you are scored
A hidden verifier independently checks each of your three output files. For *trapping_energies.csv* your reported energies and decomposition are compared to reference values within preset tolerances. For *multiH_Re4V_trapping_energies.csv* the verifier checks that the sequential energies match reference values and that the series correctly ends at a positive trapping energy. For *retention_analysis.csv* the verifier recomputes T_max from your submitted trapping energies using the same Polanyi‑Wigner parameters and verifies that the number of H atoms retained at 300 K for each complex matches the expected reference. The scores from all three stages are weighted and combined into a single reward in the range [0, 1]. Reporting the paper’s numbers without correctly performing the DFT calculations will not yield a high score; the verifier rewards faithfully reproduced quantities.

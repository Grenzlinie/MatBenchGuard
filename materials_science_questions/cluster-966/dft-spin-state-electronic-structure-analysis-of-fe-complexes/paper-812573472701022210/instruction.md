# Nonadiabatic spin-inversion dynamics in O2 binding to model heme

## Problem background
The binding of molecular oxygen (O₂) to the heme iron involves a change in total spin multiplicity — from the triplet O₂ and quintet deoxyheme reactants to the singlet oxyheme product — and is therefore a formally spin-forbidden process. Understanding the spin-inversion mechanism requires the magnitudes of spin-orbit couplings among the singlet, triplet, quintet, and septet states, as well as the nonadiabatic dynamics that governs the population transfer. This task addresses these questions using a reduced-dimensional model of the Fe(II)-porphyrin + imidazole (FePorIm) complex.

## Approach
The workflow consists of three stages. First, spin-free potential energy surfaces for the singlet, triplet, quintet, and septet states are obtained from density functional theory (B97D functional) on a grid of three active coordinates: the Fe–O₂ distance (R), the Fe–O–O bending angle (θ), and the Fe out-of-plane displacement (d). The surfaces are interpolated with cubic splines. Second, spin-orbit coupling matrix elements are computed using state-averaged CASSCF(8e,7o) with the SOMF approximation, covering the crossing region along the Fe–O distance. Third, the diabatic Hamiltonian (a 16×16 matrix) is assembled and a reduced-dimensional wave packet is propagated on a DVR grid using the extended split-operator method. The initial wave packet is prepared on the triplet, quintet, and septet states at an average collision energy of approximately 0.136 eV.

## Reproduction target
Produce two scored artifacts: the spin-orbit coupling curve as a function of Fe–O distance, and the time evolution of the summed spin-multiplicity populations from the wave packet dynamics. Specifically, generate a CSV table of the real and complex SOC matrix elements (especially the singlet-triplet b₁ element) at points spanning the crossing region, and a separate CSV time series of the singlet, triplet, quintet, and septet populations over at least 2 ps. The results should reflect the dynamics at one collision energy (~0.136 eV).

## Assets

- ORCA quantum chemistry package: https://orcaforum.kofo.mpg.de/
- Python scientific stack: numpy, scipy, matplotlib

## Workflow steps

### Step 1: Generate DFT potential energy surface grid
- Role: process
- Action: Optimize the FePorIm model geometry in the quintet state using B97D/6-311+G*(Fe,O)/6-31G**(C,N,H). Compute single-point energies for singlet, triplet, quintet, and septet states on a grid of coordinates (R, θ, d) covering the relevant ranges. Use cubic spline interpolation to obtain continuous potential energy surfaces for all four spin multiplicities.
- Evidence: `/app/outputs/pes_grid_energies.csv`

### Step 2: Compute spin-orbit coupling matrix elements
- Role: process
- Action: At selected Fe-O distances (with d=0) covering the crossing region, perform state-averaged CASSCF(8e,7o)/def2-TZVP calculations with the SOMF approximation. The active space comprises five Fe 3d and two O2 π* orbitals. Compute the singlet-triplet, triplet-quintet, and quintet-septet SOC elements.
- Evidence: `/app/outputs/soc_raw_data.csv`

### Step 3: Run wave packet dynamics
- Role: process
- Action: Assemble the 16×16 Hermitian potential energy matrix from the interpolated PES and SOCs. Set up a 3D DVR grid and propagate an initial Gaussian wave packet with equal population on triplet, quintet, and septet states (collision energy ≈0.136 eV) using the extended split-operator method. Record diabatic populations for all spin sub-states for at least 2 ps.
- Evidence: `/app/outputs/wavepacket_trajectory.npz`

### Step 4: Output spin-orbit coupling curve
- Role: scored (load-bearing)
- Action: From the computed spin-orbit couplings, create /app/outputs/soc_curve.csv containing the SOC elements as a function of Fe-O distance. Include at least 8 data points spanning the crossing region (approx 1.8–5.0 Å).
- Output file: `/app/outputs/soc_curve.csv`
- Format: csv
- Contract: Columns: R (Å), b1 (cm⁻¹), z1_real (cm⁻¹), z1_imag (cm⁻¹), z1_star_real (cm⁻¹), z1_star_imag (cm⁻¹). At least 8 points spanning approx 1.8–5.0 Å.
- Scoring: scored by hidden verifier

### Step 5: Output population evolution
- Role: scored (load-bearing)
- Action: From the wave packet dynamics simulation, save /app/outputs/population_evolution.csv containing the spin-multiplicity populations summed over M_S sub-states.
- Output file: `/app/outputs/population_evolution.csv`
- Format: csv
- Contract: Columns: time_ps (ps), pop_singlet, pop_triplet_total, pop_quintet_total, pop_septet_total. Time points from 0 to 2 ps, steps ≤ 0.01 ps.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/soc_curve.csv`
- `/app/outputs/population_evolution.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### soc_curve.csv
- path: `/app/outputs/soc_curve.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Spin-orbit coupling matrix elements as a function of Fe-O distance. The checker compares b1 at selected R values against hidden paper-derived reference values within an allowed tolerance, and verifies that triplet-quintet and quintet-septet couplings are negligible at larger R.
- schema:
  - `type`: table
  - `required_columns`: `R`, `b1`, `z1_real`, `z1_imag`, `z1_star_real`, `z1_star_imag`
  - `units`:
    - `R`: Å
    - `b1`: cm⁻¹
    - `z1_real`: cm⁻¹
    - `z1_imag`: cm⁻¹
    - `z1_star_real`: cm⁻¹
    - `z1_star_imag`: cm⁻¹

### population_evolution.csv
- path: `/app/outputs/population_evolution.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Time evolution of summed spin-multiplicity populations from wavepacket dynamics at collision energy ~0.136 eV. The checker verifies that the singlet population peak falls within a specified time window and exceeds a minimum threshold, and that quintet and septet populations remain below a small threshold throughout.
- schema:
  - `type`: table
  - `required_columns`: `time_ps`, `pop_singlet`, `pop_triplet_total`, `pop_quintet_total`, `pop_septet_total`
  - `units`:
    - `time_ps`: ps
    - `pop_singlet`: dimensionless
    - `pop_triplet_total`: dimensionless
    - `pop_quintet_total`: dimensionless
    - `pop_septet_total`: dimensionless

Notes: The agent must execute the full computational workflow (DFT PES generation, CASSCF SOC calculation, wavepacket dynamics) as process steps before writing the scored artifacts. No gold values or tolerances are provided publicly.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "soc_curve.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "R",
          "b1",
          "z1_real",
          "z1_imag",
          "z1_star_real",
          "z1_star_imag"
        ],
        "units": {
          "R": "Å",
          "b1": "cm⁻¹",
          "z1_real": "cm⁻¹",
          "z1_imag": "cm⁻¹",
          "z1_star_real": "cm⁻¹",
          "z1_star_imag": "cm⁻¹"
        }
      },
      "description": "Spin-orbit coupling matrix elements as a function of Fe-O distance. The checker compares b1 at selected R values against hidden paper-derived reference values within an allowed tolerance, and verifies that triplet-quintet and quintet-septet couplings are negligible at larger R."
    },
    {
      "file": "population_evolution.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "time_ps",
          "pop_singlet",
          "pop_triplet_total",
          "pop_quintet_total",
          "pop_septet_total"
        ],
        "units": {
          "time_ps": "ps",
          "pop_singlet": "dimensionless",
          "pop_triplet_total": "dimensionless",
          "pop_quintet_total": "dimensionless",
          "pop_septet_total": "dimensionless"
        }
      },
      "description": "Time evolution of summed spin-multiplicity populations from wavepacket dynamics at collision energy ~0.136 eV. The checker verifies that the singlet population peak falls within a specified time window and exceeds a minimum threshold, and that quintet and septet populations remain below a small threshold throughout."
    }
  ],
  "notes": "The agent must execute the full computational workflow (DFT PES generation, CASSCF SOC calculation, wavepacket dynamics) as process steps before writing the scored artifacts. No gold values or tolerances are provided publicly."
}
```

## How you are scored
A hidden verifier independently evaluates each scored output file. For soc_curve.csv it checks specific SOC elements (strength, dominance of certain coupling channels) against reference expectations. For population_evolution.csv it examines the time and magnitude of the singlet state's population maximum and verifies that populations of the higher-spin states remain within physically expected bounds. Both checks use appropriate tolerances and reward monotonic improvement. The final score is the weighted combination of the per-artifact scores; reporting the paper's numbers is insufficient — the verifier expects the results to emerge from the prescribed computational workflow.

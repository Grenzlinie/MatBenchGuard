# Magnetic anisotropy and hysteresis of Co dimers on Cu(001) and Pt(001) from DFT and kinetic Monte Carlo

## Problem background
Single atomic spins on surfaces are building blocks for nanomagnetic devices. Their behavior is governed by magnetic anisotropy, which arises from the local crystal field, and by exchange coupling between neighboring adatoms, mediated by the substrate conduction electrons. While anisotropy is often treated as a constant local property, exchange interactions could in principle affect the effective anisotropy through modifications in the electronic structure. This task examines whether and how the distance-dependent exchange interaction between Co adatoms on Cu(001) and Pt(001) influences the magnetic anisotropy of each adatom, and how any such variations affect the hysteretic response of the dimer under an external magnetic field.

## Approach
The workflow combines first-principles density functional theory (DFT) and stochastic kinetic Monte Carlo (KMC) simulations. Using Quantum ESPRESSO (open-source), scalar-relativistic DFT is first employed to relax the geometries of Co dimers on Cu(001) and Pt(001) slabs at a range of interatomic separations and for both ferromagnetic (FM) and antiferromagnetic (AFM) spin orderings. Fully relativistic DFT calculations with spin-orbit coupling are then performed for each relaxed configuration, with spins aligned perpendicular or parallel to the surface, to obtain total energies. From these energies, exchange coupling energies and per-atom magnetic anisotropy energies are extracted. The resulting exchange and anisotropy constants are fed into a classical two-spin Heisenberg model, and magnetization curves are simulated via KMC at low temperature (0.4 K) under a swept external field. Hysteresis parameters (coercive field, remanence) are then derived from the simulated curves. The comparison is across substrates (Cu vs Pt), separations, and magnetic orderings (FM vs AFM).

## Reproduction target
Produce four scored artifacts under `/app/outputs`:
1. A table of exchange coupling energies E_ex (difference between FM and AFM total energies) for Co dimers on Cu(001) and Pt(001) at multiple interatomic separations (approximately 3 to 12 Å) and both magnetic orderings.
2. A table of per-atom magnetic anisotropy energies E_MA (energy difference between spins aligned perpendicular and parallel to the surface, divided per atom) for the same set of separations, substrates, and orderings.
3. Magnetization curves (field sweeps from -B0 to +B0 and back, B0=2 T for Cu, 10 T for Pt, step 1 mT, sweep rate 130 T/s) for representative dimer separations on Cu (3.41, 5.17, 8.11 Å) and Pt (5.63 Å and at least one additional separation where the per-atom anisotropy is larger).
4. A summary table of coercive fields and remanent magnetization values extracted from those curves.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org
- SSSP Pseudopotentials for Co, Cu, Pt: https://www.materialscloud.org/discover/sssp
- Python scientific stack: numpy scipy matplotlib

## Workflow steps

### Step 1: DFT structural relaxation
- Role: process
- Action: Using scalar-relativistic DFT with Quantum ESPRESSO, relax Co dimer structures on Cu(001) and Pt(001) slabs for a range of interatomic separations (from ~3 to ~12 Å) and for both ferromagnetic (FM) and antiferromagnetic (AFM) spin orderings. Relax atomic positions until forces are negligible.
- Evidence: `/app/outputs/relaxation_log.txt`

### Step 2: DFT total energy calculations with spin-orbit coupling
- Role: process
- Action: Using the relaxed structures, perform fully-relativistic DFT calculations (spin-orbit coupling and dipolar corrections) to obtain total energies for each dimer configuration with spins aligned along the surface normal and along the in-plane bond axis. Compute total energies for both FM and AFM orderings.
- Evidence: `/app/outputs/total_energies.json`

### Step 3: Compute exchange coupling energies
- Role: scored
- Action: From the total energies of FM and AFM states, compute the exchange coupling energy E_ex(d) = E_FM - E_AFM for each separation and substrate. Output a CSV file with columns: separation_angstrom, substrate, ordering, E_ex_meV.
- Output file: `/app/outputs/step_00_exchange_energies.csv`
- Format: csv
- Contract: separation_angstrom (float), substrate (string: Cu or Pt), ordering (string: FM or AFM), E_ex_meV (float)
- Scoring: scored by hidden verifier

### Step 4: Compute magnetic anisotropy energies per atom
- Role: scored
- Action: Using the total energies for spin directions parallel and perpendicular to the surface normal, calculate the per-atom magnetic anisotropy energy E_MA(d) for each separation, substrate, and magnetic ordering. The anisotropy is defined as E_MA = E_z - E_bond (per dimer, then per atom). Output a CSV with columns: separation_angstrom, substrate, ordering, E_MA_meV.
- Output file: `/app/outputs/step_01_anisotropy_energies.csv`
- Format: csv
- Contract: separation_angstrom (float), substrate (string: Cu or Pt), ordering (string: FM or AFM), E_MA_meV (float)
- Scoring: scored by hidden verifier

### Step 5: Run kinetic Monte Carlo simulations of magnetization curves
- Role: scored (load-bearing)
- Action: Build a classical two-spin Heisenberg model using exchange coupling J(d) and anisotropy constants K_i(d) from the earlier steps. Set spin length to reproduce m_Co = 1.92 μ_B. Perform stochastic KMC simulations at T=0.4 K, sweeping magnetic field from -B0 to +B0 and back (B0=2 T for Cu, 10 T for Pt) in increments of 1 mT at a sweep rate of 130 T/s. Generate magnetization vs field data for representative dimer separations (3.41, 5.17, 8.11 Å on Cu; 5.63 Å and at least one larger-anisotropy separation on Pt). Output a CSV with columns: substrate, separation_angstrom, field_T, magnetization_norm.
- Output file: `/app/outputs/step_02_magnetization_curves.csv`
- Format: csv
- Contract: substrate (string), separation_angstrom (float), field_T (float), magnetization_norm (float)
- Scoring: scored by hidden verifier

### Step 6: Extract hysteresis parameters
- Role: scored
- Action: Analyze the magnetization curves from step_02 to extract the coercive field (B_c) and remanent magnetization (M_r/M_S) for each dimer. Output a CSV with columns: substrate, separation_angstrom, coercive_field_T, remanence_norm.
- Output file: `/app/outputs/step_03_hysteresis_summary.csv`
- Format: csv
- Contract: substrate (string), separation_angstrom (float), coercive_field_T (float), remanence_norm (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_00_exchange_energies.csv`
- `/app/outputs/step_01_anisotropy_energies.csv`
- `/app/outputs/step_02_magnetization_curves.csv`
- `/app/outputs/step_03_hysteresis_summary.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_00_exchange_energies.csv
- path: `/app/outputs/step_00_exchange_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Exchange coupling energies E_ex(d) for Co dimers on Cu(001) and Pt(001) at various separations and magnetic orderings. Scored by comparison to hidden paper-reported values with tolerance and a structural trend check for RKKY-like oscillation.
- schema:
  - `type`: table
  - `required_columns`: `separation_angstrom`, `substrate`, `ordering`, `E_ex_meV`
  - `units`:
    - `separation_angstrom`: angstrom
    - `E_ex_meV`: meV

### step_01_anisotropy_energies.csv
- path: `/app/outputs/step_01_anisotropy_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Per-atom magnetic anisotropy energies E_MA(d) for Co dimers on Cu(001) and Pt(001). Scored by comparison to hidden paper-reported values with tolerance and a structural trend check ensuring non-monotonous separation dependence and sensitivity to magnetic ordering.
- schema:
  - `type`: table
  - `required_columns`: `separation_angstrom`, `substrate`, `ordering`, `E_MA_meV`
  - `units`:
    - `separation_angstrom`: angstrom
    - `E_MA_meV`: meV

### step_02_magnetization_curves.csv
- path: `/app/outputs/step_02_magnetization_curves.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Raw magnetization curves for representative Co dimers. The checker will recompute coercive fields and remanences from these curves and compare to hidden gold values derived from the paper.
- schema:
  - `type`: table
  - `required_columns`: `substrate`, `separation_angstrom`, `field_T`, `magnetization_norm`
  - `units`:
    - `field_T`: T
    - `magnetization_norm`: dimensionless

### step_03_hysteresis_summary.csv
- path: `/app/outputs/step_03_hysteresis_summary.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Summary of coercive fields and remanences. The checker will recompute these values from step_02 and compare to the submitted summary and to hidden paper-derived gold.
- schema:
  - `type`: table
  - `required_columns`: `substrate`, `separation_angstrom`, `coercive_field_T`, `remanence_norm`
  - `units`:
    - `coercive_field_T`: T
    - `remanence_norm`: dimensionless

Notes: The exchange coupling and anisotropy energies are intermediate scored artifacts that also serve as inputs for the KMC simulations. All separations and magnetic orderings used in the paper should be computed; the representative separations specifically targeted are those discussed in the paper's Figure 3.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_00_exchange_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "separation_angstrom",
          "substrate",
          "ordering",
          "E_ex_meV"
        ],
        "units": {
          "separation_angstrom": "angstrom",
          "E_ex_meV": "meV"
        }
      },
      "description": "Exchange coupling energies E_ex(d) for Co dimers on Cu(001) and Pt(001) at various separations and magnetic orderings. Scored by comparison to hidden paper-reported values with tolerance and a structural trend check for RKKY-like oscillation."
    },
    {
      "file": "step_01_anisotropy_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "separation_angstrom",
          "substrate",
          "ordering",
          "E_MA_meV"
        ],
        "units": {
          "separation_angstrom": "angstrom",
          "E_MA_meV": "meV"
        }
      },
      "description": "Per-atom magnetic anisotropy energies E_MA(d) for Co dimers on Cu(001) and Pt(001). Scored by comparison to hidden paper-reported values with tolerance and a structural trend check ensuring non-monotonous separation dependence and sensitivity to magnetic ordering."
    },
    {
      "file": "step_02_magnetization_curves.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "substrate",
          "separation_angstrom",
          "field_T",
          "magnetization_norm"
        ],
        "units": {
          "field_T": "T",
          "magnetization_norm": "dimensionless"
        }
      },
      "description": "Raw magnetization curves for representative Co dimers. The checker will recompute coercive fields and remanences from these curves and compare to hidden gold values derived from the paper."
    },
    {
      "file": "step_03_hysteresis_summary.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "substrate",
          "separation_angstrom",
          "coercive_field_T",
          "remanence_norm"
        ],
        "units": {
          "coercive_field_T": "T",
          "remanence_norm": "dimensionless"
        }
      },
      "description": "Summary of coercive fields and remanences. The checker will recompute these values from step_02 and compare to the submitted summary and to hidden paper-derived gold."
    }
  ],
  "notes": "The exchange coupling and anisotropy energies are intermediate scored artifacts that also serve as inputs for the KMC simulations. All separations and magnetic orderings used in the paper should be computed; the representative separations specifically targeted are those discussed in the paper's Figure 3."
}
```

## How you are scored
Each workflow step that produces a scored artifact is verified independently by a hidden verifier. The verifier does not simply accept reported numbers; it recomputes derived quantities where possible (e.g., hysteresis parameters are recalculated from the raw magnetization curves) and compares quantities against reference data using appropriate tolerances and structural checks (trends, monotonicity, ordering dependence). Each scored artifact is assigned a weight, and the final reward is the weighted sum of the individual step scores. Submitting the expected reference values without genuine computation will not suffice; the verifier checks consistency across the pipeline.

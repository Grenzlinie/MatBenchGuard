# Magnetic HDNNP with spin-dependent ACSFs for MnO

## Problem background
Machine learning interatomic potentials usually cannot distinguish different electronic spin arrangements, limiting their applicability to magnetic materials. This task tackles that limitation by introducing spin‑dependent atom‑centered symmetry functions (sACSFs) that augment conventional structural descriptors with collinear spin information. When used as input to a high‑dimensional neural network potential (HDNNP), the resulting magnetic HDNNP (mHDNNP) can describe multiple collinear magnetic states simultaneously. The method is benchmarked on manganese oxide (MnO), where the potential must reproduce the magnetically distorted rhombohedral structure, the energy differences among magnetic configurations, and the exchange constants that determine the Néel temperature.

## Approach
The core idea is to extend the atom‑centered symmetry functions (ACSFs) used in HDNNPs with spin‑augmentation functions (SAFs) that depend on the sign of the atomic spin coordinate. Radial SAFs (M⁰, M⁺, M⁻) and angular SAFs (M⁰⁰, M⁺⁺, M⁻⁻, M⁺⁻) filter interatomic interactions according to whether the involved atoms have parallel, antiparallel, or spin‑zero arrangements. These sACSFs are then fed into atomic neural networks (same topology as a standard HDNNP) to predict atomic energy contributions, from which total energies and forces are obtained.

You will compare two potentials: a baseline HDNNP trained on conventional ACSFs only, and the mHDNNP that uses sACSFs and thus includes spin information. Both potentials are trained on the same reference dataset—a collection of DFT calculations for MnO supercells in multiple magnetic states (AFM‑II, FM, AFM‑I, and spin‑disordered) with geometric distortions. The trained mHDNNP will then be used to optimize the lattice parameters of the two magnetic phases and to evaluate the energies of three ordered spin configurations at a fixed experimental lattice constant, from which Heisenberg exchange constants and the mean‑field Néel temperature are derived.

## Reproduction target
- Train an ACSF‑only HDNNP and a mHDNNP on a DFT reference dataset of MnO supercells (200–500 structures covering multiple magnetic configurations and geometric distortions).
- Evaluate both potentials on a held‑out test set; compute the energy RMSE (meV/atom) and force RMSE (eV/Å) for each potential, and write the results to `mhdnnp_vs_acsf_errors.csv`. The mHDNNP should show substantially lower prediction errors than the ACSF‑only baseline.
- Using the trained mHDNNP, relax the atomic positions and lattice vectors of a 2×2×2 MnO supercell in the AFM‑II and FM magnetic configurations; report the converged lattice constant a (and, for AFM‑II, the rhombohedral angle α) in `optimized_lattice_params.json`.
- With the mHDNNP, compute the energies of the AFM‑II, AFM‑I, and FM magnetic orders at the experimental cubic lattice constant (4.430 Å). From the energy differences, derive the nearest‑neighbour and next‑nearest‑neighbour exchange coupling constants J1 and J2 (in Kelvin) using the Heisenberg model with spin S=5/2, and then the mean‑field Néel temperature T_N. Write J1, J2, T_N to `exchange_neel.json`.

## Assets

- RuNNer (HDNNP code): http://gitlab.com/TheochemGoettingen/RuNNer
- CP2K: https://www.cp2k.org/
- Atomic Simulation Environment (ASE): https://gitlab.com/ase/ase
- n2p2 neural network potential package: https://github.com/CompPhysVienna/n2p2

## Workflow steps

### Step 1: Generate DFT reference dataset
- Role: process
- Action: Create a set of MnO 2×2×2 supercells (64 atoms) in several magnetic configurations (AFM-II, FM, AFM-I, and spin-disordered with random spin flips). Apply small random atomic displacements and lattice distortions. Run CP2K with HSE06 functional to compute total energies, forces, and Hirshfeld spin moments. Collect 200–500 structures as the reference dataset.
- Evidence: `/app/outputs/dft_generation.log`

### Step 2: Train ACSF-only HDNNP
- Role: process
- Action: Using RuNNer, train a standard HDNNP (three hidden layers 20-15-10) on the generated reference dataset using only conventional radial and angular ACSFs. Record training progress.
- Evidence: `/app/outputs/acsf_hdnnp_training.log`

### Step 3: Train magnetic HDNNP (mHDNNP) with sACSFs
- Role: process
- Action: Implement the sACSF extensions in RuNNer following the paper’s definitions (radial SAFs M0, M+, M-; angular SAFs M00, M++, M--, M+-). Train the mHDNNP (same network topology) on the same reference dataset, using the new spin-dependent radial and angular SAFs. Record training progress.
- Evidence: `/app/outputs/mhdnnp_training.log`

### Step 4: Evaluate energy and force errors
- Role: scored
- Action: Evaluate both trained potentials on a held-out test set from the generated reference data. Compute the energy RMSE (meV/atom) and force RMSE (eV/Å) for each potential. Write the results to mhdnnp_vs_acsf_errors.csv.
- Output file: `/app/outputs/mhdnnp_vs_acsf_errors.csv`
- Format: csv
- Contract: CSV with columns: potential (string, 'ACSF-only' or 'mHDNNP'), split (string, 'train' or 'test'), metric (string, 'E_RMSE_meV_per_atom' or 'F_RMSE_eV_per_angstrom'), value (float).
- Scoring: scored by hidden verifier

### Step 5: Optimize lattice parameters of AFM-II and FM phases
- Role: scored (load-bearing)
- Action: Using the trained mHDNNP, perform geometry optimization (relaxation of atomic positions and lattice vectors) for a 2×2×2 MnO supercell in the AFM-II and FM magnetic configurations. Extract the converged lattice constant a (Å) and, for AFM-II, the rhombohedral angle α (deg). Write the results to optimized_lattice_params.json.
- Output file: `/app/outputs/optimized_lattice_params.json`
- Format: json
- Contract: JSON object: {"AFM-II": {"a": float, "alpha": float}, "FM": {"a": float}}. α is 90.0 for cubic FM.
- Scoring: scored by hidden verifier

### Step 6: Compute exchange constants and Néel temperatures
- Role: scored (load-bearing)
- Action: 1) Use the mHDNNP to compute the energies of AFM‑II, AFM‑I, and FM magnetic orders for a 2×2×2 MnO supercell at the experimental cubic lattice constant a=4.430 Å. Derive the Heisenberg exchange constants J1 and J2 (K) using S=5/2, and then compute the mean‑field Néel temperature T_N (K). 2) Perform MC spin‑flip simulations on a 6×6×6 MnO supercell with the same cubic lattice fixed at 4.430 Å, using the trained mHDNNP. Determine the AFM‑II to paramagnetic transition temperature T_N_MC (K) from the peak in the heat capacity or the drop in the order parameter. Write all results (J1, J2, T_N, T_N_MC) to exchange_neel.json.
- Output file: `/app/outputs/exchange_neel.json`
- Format: json
- Contract: JSON object: {"J1": float, "J2": float, "T_N": float, "T_N_MC": float}. All values in Kelvin.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/mhdnnp_vs_acsf_errors.csv`
- `/app/outputs/optimized_lattice_params.json`
- `/app/outputs/exchange_neel.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### mhdnnp_vs_acsf_errors.csv
- path: `/app/outputs/mhdnnp_vs_acsf_errors.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Comparison of energy and force RMSE between ACSF‑only HDNNP and mHDNNP on train/test splits. The mHDNNP must exhibit significantly lower errors than the ACSF‑only baseline.
- schema:
  - `type`: table
  - `required_columns`: `potential`, `split`, `metric`, `value`
  - `units`:
    - `value`: meV/atom for E_RMSE, eV/Å for F_RMSE

### optimized_lattice_params.json
- path: `/app/outputs/optimized_lattice_params.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Lattice parameters of AFM‑II (rhombohedral) and FM (cubic) phases optimized with the mHDNNP.
- schema:
  - `type`: object
  - `required`: `AFM-II`, `FM`
  - `properties`:
    - `AFM-II`:
      - `a`: number (Å)
      - `alpha`: number (deg)
    - `FM`:
      - `a`: number (Å)

### exchange_neel.json
- path: `/app/outputs/exchange_neel.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Heisenberg exchange constants J1, J2, mean‑field Néel temperature T_N, and MC‑derived Néel temperature T_N_MC from spin‑flip simulations on a cubic 6×6×6 MnO supercell at 4.430 Å.
- schema:
  - `type`: object
  - `required`: `J1`, `J2`, `T_N`, `T_N_MC`
  - `properties`:
    - `J1`: number (K)
    - `J2`: number (K)
    - `T_N`: number (K)
    - `T_N_MC`: number (K)

Notes: The RMSE CSV must show mHDNNP errors substantially lower than ACSF‑only; specific thresholds are hidden. Lattice parameters, exchange constants, and both Néel temperatures are compared to the paper’s HSE06 reference values with tolerances appropriate for a different DFT code and training dataset. All quantities are produced by the agent’s own pipeline; no pre‑trained potentials or external datasets are provided.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "mhdnnp_vs_acsf_errors.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "potential",
          "split",
          "metric",
          "value"
        ],
        "units": {
          "value": "meV/atom for E_RMSE, eV/Å for F_RMSE"
        }
      },
      "description": "Comparison of energy and force RMSE between ACSF‑only HDNNP and mHDNNP on train/test splits. The mHDNNP must exhibit significantly lower errors than the ACSF‑only baseline."
    },
    {
      "file": "optimized_lattice_params.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "AFM-II",
          "FM"
        ],
        "properties": {
          "AFM-II": {
            "a": "number (Å)",
            "alpha": "number (deg)"
          },
          "FM": {
            "a": "number (Å)"
          }
        }
      },
      "description": "Lattice parameters of AFM‑II (rhombohedral) and FM (cubic) phases optimized with the mHDNNP."
    },
    {
      "file": "exchange_neel.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "J1",
          "J2",
          "T_N",
          "T_N_MC"
        ],
        "properties": {
          "J1": "number (K)",
          "J2": "number (K)",
          "T_N": "number (K)",
          "T_N_MC": "number (K)"
        }
      },
      "description": "Heisenberg exchange constants J1, J2, mean‑field Néel temperature T_N, and MC‑derived Néel temperature T_N_MC from spin‑flip simulations on a cubic 6×6×6 MnO supercell at 4.430 Å."
    }
  ],
  "notes": "The RMSE CSV must show mHDNNP errors substantially lower than ACSF‑only; specific thresholds are hidden. Lattice parameters, exchange constants, and both Néel temperatures are compared to the paper’s HSE06 reference values with tolerances appropriate for a different DFT code and training dataset. All quantities are produced by the agent’s own pipeline; no pre‑trained potentials or external datasets are provided."
}
```

## How you are scored
Each scored artifact is independently verified by a hidden checker that compares your submitted results to paper‑derived reference values. The checker does not merely confirm that the files exist; it reads the numerical entries, recomputes metrics from your raw outputs, and scores them against tolerances calibrated to allow for legitimate differences arising from the use of a different DFT code (CP2K instead of FHI‑aims) and a smaller training dataset. For the error comparison CSV, your mHDNNP must meet a hidden performance threshold and must clearly outperform the ACSF‑only baseline; for the lattice parameters and exchange constants, your computed values are checked against known ranges. The final score is a weighted sum of the per‑artifact rewards. Merely reporting numbers or supplying static files that bypass the pipeline is not sufficient—your pipeline must genuinely execute and produce artifacts that satisfy the required physical trends and accuracy expectations.

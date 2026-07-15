# Li₄Ti₅O₁₂ Co‑doping and Oxygen Vacancy Effects on Band Gap and Li⁺ Migration Barrier via DFT and NEB

## Problem background
Spinel Li₄Ti₅O₁₂ (LTO) is a promising anode material for lithium-ion batteries because of its near-zero strain during cycling, but its poor intrinsic electronic conductivity and sluggish Li-ion diffusion limit high-rate performance. Modifications such as co-doping with Mg and Zr, and the introduction of oxygen vacancies, have been proposed to alter the electronic structure and transport properties. Understanding the effect of these modifications on the band gap and Li⁺ migration barriers is important for designing fast-charging electrode materials.

## Approach
Density functional theory (DFT) calculations are used to compute the electronic density of states (DOS), band gap, and Li-ion migration barriers for pristine and modified LTO. The cubic spinel crystal structure (space group Fd-3m) is used to construct a 56-atom conventional cell. Co-doping is modelled by substituting one Li (8a) with Mg and one Ti (16d) with Zr; an oxygen vacancy is created by removing one O (32e). After relaxing the geometries with GGA-PBE including Hubbard-U corrections on Ti and Zr, the total DOS is computed to extract the band gap. Li⁺ diffusion barriers are obtained with the climbing-image nudged elastic band (NEB) method along the pathway between adjacent Li sites (8a→16c→8a). The workflow is implemented with an open-source plane-wave DFT code (e.g., Quantum ESPRESSO).

## Reproduction target
Compute and report the following:
- DFT band gap (eV) for three systems: pristine LTO, Mg/Zr co-doped LTO (LMTZO), and Mg/Zr co-doped LTO with an oxygen vacancy (LMTZO-Ov).
- Li⁺ migration barrier (eV) for the co-doped systems with and without an oxygen vacancy (LMTZO and LMTZO-Ov) along the prescribed pathway.
The values must be saved in the two CSV files specified in the workflow steps.

## Assets

- Li₄Ti₅O₁₂ spinel crystal structure (CIF): https://materialsproject.org/materials/mp-19031
- Quantum ESPRESSO: https://www.quantum‑espresso.org/
- PAW pseudopotentials (PBE, SSSP or equivalent): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Generate supercell structures with doping and oxygen vacancies
- Role: process
- Action: From the public spinel CIF, build a 56‑atom conventional cell (Fd‑3m). Substitute one Li (8a) with Mg and one Ti (16d) with Zr; remove one O (32e) for the vacancy model. Create four initial structures: LTO, LTO‑Ov, LMTZO, LMTZO‑Ov.
- Evidence: `/app/outputs/step_01_structures_ready.txt`

### Step 2: DFT geometry optimization
- Role: process
- Action: Relax the atomic positions (and optionally cell) of LTO, LTO‑Ov, LMTZO, and LMTZO‑Ov using GGA‑PBE with Hubbard‑U corrections (U=4 eV on Ti and Zr). Use the open‑source DFT code (e.g., Quantum ESPRESSO) and a converged plane‑wave energy cutoff and k‑point mesh.
- Evidence: `/app/outputs/step_02_relaxation_done.txt`

### Step 3: Compute electronic density of states and band gap
- Role: scored
- Action: Perform static scf/nscf calculations on the relaxed structures. Compute the total density of states (DOS). Extract the band gap as the energy difference between the valence band maximum and the conduction band minimum (or the Fermi level when it lies in the band). Report the band gap for LTO, LMTZO, and LMTZO‑Ov.
- Output file: `/app/outputs/band_gap_results.csv`
- Format: csv
- Contract: CSV with header: system,band_gap_eV. Three rows: LTO,<value>; LMTZO,<value>; LMTZO‑Ov,<value>. Units: eV.
- Scoring: scored by hidden verifier

### Step 4: NEB calculation of Li⁺ migration barrier
- Role: scored (load-bearing)
- Action: For the co‑doped systems LMTZO and LMTZO‑Ov, perform climbing‑image nudged elastic band (NEB) calculations along the 8a→16c→8a pathway. Extract the energy barrier (eV) from the maximum energy point on the minimum energy path.
- Output file: `/app/outputs/migration_barriers.csv`
- Format: csv
- Contract: CSV with header: system,barrier_eV. Two rows: LMTZO,<value>; LMTZO‑Ov,<value>. Units: eV.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gap_results.csv`
- `/app/outputs/migration_barriers.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gap_results.csv
- path: `/app/outputs/band_gap_results.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: DFT band gap for LTO, LMTZO, and LMTZO‑Ov. Scored by comparing the reported values to hidden gold and verifying the narrowing trend (LMTZO‑Ov gap < LTO gap).
- schema:
  - `type`: table
  - `required_columns`: `system`, `band_gap_eV`
  - `units`:
    - `band_gap_eV`: eV

### migration_barriers.csv
- path: `/app/outputs/migration_barriers.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Li⁺ migration barrier for LMTZO and LMTZO‑Ov from NEB. Scored by comparing the reported barriers to hidden gold values and verifying the reduction trend (LMTZO‑Ov barrier < LMTZO barrier).
- schema:
  - `type`: table
  - `required_columns`: `system`, `barrier_eV`
  - `units`:
    - `barrier_eV`: eV

Notes: The agent must write both CSV files under /app/outputs. The checker reads these files and compares the reported values and relative trends to the paper’s reported results (hidden). No gold values or tolerances are disclosed publicly.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gap_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "band_gap_eV"
        ],
        "units": {
          "band_gap_eV": "eV"
        }
      },
      "description": "DFT band gap for LTO, LMTZO, and LMTZO‑Ov. Scored by comparing the reported values to hidden gold and verifying the narrowing trend (LMTZO‑Ov gap < LTO gap)."
    },
    {
      "file": "migration_barriers.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "barrier_eV"
        ],
        "units": {
          "barrier_eV": "eV"
        }
      },
      "description": "Li⁺ migration barrier for LMTZO and LMTZO‑Ov from NEB. Scored by comparing the reported barriers to hidden gold values and verifying the reduction trend (LMTZO‑Ov barrier < LMTZO barrier)."
    }
  ],
  "notes": "The agent must write both CSV files under /app/outputs. The checker reads these files and compares the reported values and relative trends to the paper’s reported results (hidden). No gold values or tolerances are disclosed publicly."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently checks each scored output file. The verifier compares your reported band gap and migration barrier values to expected quantitative relationships and reference values derived from the original study. Each output file carries a predefined weight; the final reward is the weighted sum of the per-artifact scores. You must produce the exact CSV files described in the steps and output contract; the verifier will not accept handcrafted numbers that do not arise from a genuine DFT workflow. The closer your computed results are to the expected physical behaviour, the higher your score.

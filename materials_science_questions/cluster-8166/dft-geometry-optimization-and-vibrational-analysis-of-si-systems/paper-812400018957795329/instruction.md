# Electronic Structure Analysis of Strained Si-Si Bond Breaking in Silicon Clusters

## Problem background
Amorphous silicon alloys, particularly hydrogenated amorphous silicon (a-Si:H), are widely used in thin-film solar cells but suffer from light-induced degradation known as the Staebler-Wronski effect. Under prolonged illumination, metastable defects form, reducing efficiency, yet the atomistic mechanism remains elusive. One leading hypothesis is that strained Si-Si bonds in the amorphous network can break, creating dangling-bond defects that alter the electronic properties. To test this idea, quantum chemical calculations can model a local strained bond and examine how its electronic structure—specifically the energy gap between the highest occupied and lowest unoccupied molecular orbitals (HOMO-LUMO) and the charge distribution—evolves as the bond is stretched. This computational investigation is essential to determine whether bond-breaking is energetically plausible and what conditions trigger it.

## Approach
The Si-Si bond is modeled using a Si2H6 cluster: two silicon atoms, each bonded to three hydrogen “saturator” atoms placed at bulk-like Si positions (2.35 Å from the Si atom) to mimic the tetrahedral environment of the solid. The Si-Si distance is systematically varied from 2.5 Å to 3.0 Å in steps of 0.1 Å to emulate bond stretching. At each distance, a constrained geometry optimization is performed with the Si-Si distance held fixed while all other coordinates (including the positions of the saturator H atoms and the orientation of the Si group) are allowed to relax, simulating the local structural relaxation that accompanies bond elongation. An open-source density functional theory (DFT) code is used to compute the electronic structure, yielding the HOMO and LUMO energies and Mulliken atomic charges. From these raw results we extract two quantities as functions of the Si-Si distance: (1) the HOMO-LUMO energy gap, ΔE, and (2) the net charge transfer Δq away from the silicon atom that moves toward a trigonal coordination. The resulting curves encapsulate the critical electronic response to bond stretching and form the basis for assessing a bond‑breaking mechanism.

## Reproduction target
Produce a CSV file at `/app/outputs/calculated_properties.csv` with the following columns: `distance_A` (Si-Si distance in Å), `Delta_E_eV` (HOMO‑LUMO gap in eV), and `Delta_q_e` (net charge transfer in units of electron charge). One row must be provided for each of the six target distances: 2.5, 2.6, 2.7, 2.8, 2.9, and 3.0 Å. The values must be derived from the constrained geometry optimizations and electronic structure calculations described in the workflow steps, and they should reflect the genuine physical behavior of a stretched Si-Si bond in the cluster model. The hidden checker will evaluate the CSV against expected qualitative trends and quantitative thresholds that characterize a bond‑breaking scenario; no further target values are disclosed.

## Assets

- Open-source quantum chemistry software (DFT engine)

## Workflow steps

### Step 1: Constrained geometry optimizations of Si2H6 cluster
- Role: process
- Action: Build a Si2H6 cluster (two Si atoms each bonded to three H saturators placed at approximately tetrahedral positions with H atoms at 2.35 Å from Si to mimic bulk positions). For each target Si-Si distance (2.5, 2.6, 2.7, 2.8, 2.9, 3.0 Å), perform a constrained geometry optimization with the Si-Si distance fixed, allowing all other coordinates to relax. Use a suitable open-source DFT code and extract the optimized total energy, HOMO/LUMO eigenvalues, and Mulliken charges.
- Evidence: `/app/outputs/optimization_logs.txt`

### Step 2: Compute HOMO-LUMO gap and charge transfer
- Role: scored (load-bearing)
- Action: From the optimized results for each Si-Si distance, compute Delta_E_eV = ELUMO - EHOMO (in eV) and Delta_q_e = difference between the Mulliken charge on the non-tetrahedrally coordinated Si atom and the charge on a Si atom in a reference fully tetrahedral Si2H6 cluster. Output these values in a CSV with columns distance_A, Delta_E_eV, Delta_q_e, one row per distance.
- Output file: `/app/outputs/calculated_properties.csv`
- Format: csv
- Contract: Columns: distance_A (float, Si-Si distance in Å), Delta_E_eV (float, HOMO-LUMO gap in eV), Delta_q_e (float, charge transfer in electron charge units). Rows for distances 2.5, 2.6, 2.7, 2.8, 2.9, 3.0 Å.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/calculated_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### calculated_properties.csv
- path: `/app/outputs/calculated_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV containing the HOMO-LUMO gap and charge transfer as a function of Si-Si bond length for distances 2.5, 2.6, 2.7, 2.8, 2.9, 3.0 Å.
- schema:
  - `type`: table
  - `required_columns`: `distance_A`, `Delta_E_eV`, `Delta_q_e`
  - `units`:
    - `distance_A`: Å
    - `Delta_E_eV`: eV
    - `Delta_q_e`: e

Notes: The checker validates trends and values within tolerances derived from the original SCF-Xα-SW results, adjusted for DFT method variation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "calculated_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "distance_A",
          "Delta_E_eV",
          "Delta_q_e"
        ],
        "units": {
          "distance_A": "Å",
          "Delta_E_eV": "eV",
          "Delta_q_e": "e"
        }
      },
      "description": "CSV containing the HOMO-LUMO gap and charge transfer as a function of Si-Si bond length for distances 2.5, 2.6, 2.7, 2.8, 2.9, 3.0 Å."
    }
  ],
  "notes": "The checker validates trends and values within tolerances derived from the original SCF-Xα-SW results, adjusted for DFT method variation."
}
```

## How you are scored
A hidden verifier reads `/app/outputs/calculated_properties.csv` and compares each row to a set of internal criteria derived from the physical expectations of a bond‑breaking mechanism (e.g., the location of a HOMO‑LUMO gap peak, monotonic decrease beyond the peak, and charge transfer onset). The comparison uses tolerances that absorb the method‑dependent variation introduced by using a modern DFT code instead of the original Xα method. The verifier outputs a single reward between 0 and 1, where a correct reproduction earns full credit. Only the scored step (Step 2) contributes to the reward; the process step’s evidence is not scored but its execution is required to produce a physically meaningful CSV. Guessing or fabricating numbers without performing the constrained optimizations will not pass the hidden trend and threshold checks.

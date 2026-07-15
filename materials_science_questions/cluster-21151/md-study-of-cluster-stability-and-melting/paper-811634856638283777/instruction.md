# Optical and HOMO-LUMO Gaps of Oxygen-Capped Si20 Clusters

## Problem background
The optical and electronic gaps of silicon nanoclusters are known to depend on cluster size—a manifestation of quantum confinement. Surface passivation by oxygen can further modify these properties, but it is not always clear whether the effect on the optical gap follows the same rules as the effect on the HOMO-LUMO gap measured from ground-state DFT. This work focuses on a single cluster size, Si20, and asks: when oxygen atoms are attached to its surface in increasing numbers, do the optical gap and the HOMO-LUMO gap respond differently?

## Approach
The investigation uses a multi-stage computational protocol. First, a stable bare Si20 isomer is obtained through density functional theory (DFT) geometry optimisation within the generalised gradient approximation (GGA). Oxygen atoms are then placed on the surface to create Si20O_m clusters with m = 1, 2, 4, 6, 8, 10, 12, and each cluster is again geometrically optimised. Single-point DFT calculations on the optimised structures provide the Kohn-Sham eigenvalues and total energies. Finally, optical absorption spectra are computed for every cluster using GW quasiparticle corrections and the Bethe-Salpeter equation (BSE), a many-body perturbation theory approach that includes excitonic effects. The optical gap is extracted from the onset of these spectra.

## Reproduction target
For the bare Si20 cluster and each oxygen-capped variant Si20O_m (m = 1, 2, 4, 6, 8, 10, 12), compute:

1. the HOMO-LUMO gap from the DFT-GGA eigenvalues (difference between the lowest unoccupied and highest occupied Kohn-Sham orbitals, in eV);
2. the optical gap from the onset of significant absorption in the GW+BSE spectrum (in eV);
3. the binding energy per atom (total energy minus the sum of atomic energies of all atoms, divided by the number of atoms, in eV/atom).

Compile these quantities into a table (results.csv) with one row per oxygen coverage. The goal is to produce a dataset that captures how these three quantities change as oxygen is added to the Si20 surface.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Yambo: https://www.yambo-code.eu/
- SSSP pseudopotentials for Si and O: https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: Optimize bare Si20 cluster
- Role: process
- Action: Generate initial Si20 cluster geometry and perform DFT geometry optimization (GGA) to obtain the most stable isomer. Record final structure coordinates and total energy.
- Evidence: `/app/outputs/si20_opt.log`

### Step 2: Optimize oxygen-capped Si20O_m clusters
- Role: process
- Action: For each oxygen coverage m = 1, 2, 4, 6, 8, 10, 12, attach m oxygen atoms to the surface of the optimized Si20 core and perform DFT geometry optimization (GGA). Save final structures and energies.
- Evidence: `/app/outputs/si20o_opt_m.log`

### Step 3: DFT ground-state runs for gaps and binding energies
- Role: process
- Action: Perform a single-point DFT calculation (GGA) on each optimized cluster to obtain the Kohn-Sham eigenvalues (HOMO and LUMO) and total energy. Save output logs.
- Evidence: `/app/outputs/dft.out`

### Step 4: Compute optical spectra (GW+BSE)
- Role: process
- Action: Using Yambo (or equivalent), compute the optical absorption spectrum for each cluster via GW quasiparticle correction and Bethe-Salpeter equation (BSE). Save the imaginary part of the dielectric function vs. photon energy.
- Evidence: `/app/outputs/spectrum.dat`

### Step 5: Compile results and write scored table
- Role: scored (load-bearing)
- Action: From the DFT outputs extract the HOMO-LUMO gap (LUMO - HOMO difference in eV) and binding energy per atom. From each optical spectrum determine the optical gap as the photon energy at which significant absorption begins. Compile all values into results.csv.
- Output file: `/app/outputs/results.csv`
- Format: csv
- Contract: columns: oxygen_number (int), homolumo_gap_ev (float), optical_gap_ev (float), binding_energy_ev_atom (float)
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
- target_policy: reference_match
- description: Table of gaps and binding energy per oxygen coverage. The hidden checker will compare each row's quantitative values to a hidden reference within tolerances, and also verify that optical gap varies systematically while HOMO-LUMO gap remains essentially constant across oxygen numbers.
- schema:
  - `type`: table
  - `required_columns`: `oxygen_number`, `homolumo_gap_ev`, `optical_gap_ev`, `binding_energy_ev_atom`
  - `units`:
    - `homolumo_gap_ev`: eV
    - `optical_gap_ev`: eV
    - `binding_energy_ev_atom`: eV/atom

Notes: The agent must compute the quantities genuinely; the checker uses result-level comparison (T0) augmented by trend checks.

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
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "oxygen_number",
          "homolumo_gap_ev",
          "optical_gap_ev",
          "binding_energy_ev_atom"
        ],
        "units": {
          "homolumo_gap_ev": "eV",
          "optical_gap_ev": "eV",
          "binding_energy_ev_atom": "eV/atom"
        }
      },
      "description": "Table of gaps and binding energy per oxygen coverage. The hidden checker will compare each row's quantitative values to a hidden reference within tolerances, and also verify that optical gap varies systematically while HOMO-LUMO gap remains essentially constant across oxygen numbers."
    }
  ],
  "notes": "The agent must compute the quantities genuinely; the checker uses result-level comparison (T0) augmented by trend checks."
}
```

## How you are scored
Your submission will be evaluated automatically by a hidden verifier. The verifier reads results.csv and applies two types of checks:

- **Absolute comparison**: the reported HOMO-LUMO gap, optical gap, and binding energy for each oxygen coverage are compared against a hidden set of reference values, with acceptable tolerances that account for the use of open-source codes and different computational settings.
- **Trend verification**: the verifier checks whether the optical gap numbers show a systematic variation with oxygen number (i.e., the values change monotonically or in a visually clear pattern) and whether the HOMO-LUMO gap numbers remain within a narrow range across all oxygen coverages, with no systematic dependence on oxygen number.

Points are awarded for both the similarity of the absolute values and the correctness of the trends. Reporting values alone, without genuine calculation, yields unreliable results because both absolute numbers and trends must be consistent.

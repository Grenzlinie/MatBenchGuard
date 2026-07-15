# Ballistic Thermoelectric Properties of WSe2 Monolayers and Nanotubes

## Problem background
Thermoelectric materials can directly convert waste heat into electricity, but practical efficiency is limited because the electronic conductance, Seebeck coefficient, and thermal conductance are interdependent. Low‑dimensional structures such as two‑dimensional monolayers and one‑dimensional nanotubes can decouple these factors through quantum size effects, potentially enhancing the thermoelectric figure of merit ZT. Transition metal dichalcogenides (TMDs) are a versatile family of layered semiconductors whose thermoelectric performance in monolayer and nanotube forms is not yet fully explored. This task addresses the ballistic thermoelectric properties of WSe₂, a representative TMD, across three geometries: monolayer, zigzag (10,0) nanotube, and armchair (6,6) nanotube. The goal is to compute the maximum room‑temperature ZT, the phononic thermal conductance, and the electronic band gap for each geometry and to determine the relative ordering of these properties among the three structures.

## Approach
The workflow uses first‑principles density functional theory (DFT) and density functional perturbation theory (DFPT) to obtain the Hamiltonian, overlap matrices, and interatomic force constants for the three WSe₂ geometries. Structure relaxation, self‑consistent electronic structure calculations, and DFPT phonon calculations are performed with Quantum ESPRESSO using local density approximation (LDA) pseudopotentials. The electron and phonon transmittances are then computed within the ballistic non‑equilibrium Green’s function (NEGF) formalism. From the electron transmittance, Lorenz integrals yield electronic conductance, Seebeck coefficient, and electronic thermal conductance at 300 K; from the phonon transmittance, the phononic thermal conductance at 300 K is evaluated. Finally, the thermoelectric figure of merit ZT is computed as a function of chemical potential, and the maximum ZT, phononic thermal conductance, and band gap are extracted for each geometry. The procedure compares the three geometries under identical theoretical conditions to reveal how dimensionality and nanotube chirality affect the ballistic thermoelectric transport.

## Reproduction target
Produce a quantitative comparison of the ballistic thermoelectric properties of WSe₂ monolayer, zigzag (10,0) nanotube, and armchair (6,6) nanotube at room temperature. Specifically, compute the maximum ZT value, the phononic thermal conductance at 300 K, and the electronic band gap for each geometry. Report these quantities in a CSV file `/app/outputs/step_01_properties.csv` with columns `geometry`, `ZT_max`, `sigma_ph_300K`, and `band_gap`. The submitted values will be checked against reference calculations, and the relative ordering of ZT, phononic thermal conductance, and band gap among the three geometries will be verified against the expected physical trends.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org
- LDA pseudopotentials for W and Se: https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: Structure relaxation
- Role: process
- Action: Perform DFT structure relaxation for WSe2 monolayer, zigzag (10,0) nanotube, and armchair (6,6) nanotube using Quantum ESPRESSO pw.x with LDA pseudopotentials and appropriate k-grids.
- Evidence: `/app/outputs/relax.log`

### Step 2: DFT electronic structure calculation
- Role: process
- Action: Compute Hamiltonian, overlap matrices, and electronic band structures (including band gaps) for the relaxed geometries using Quantum ESPRESSO pw.x.
- Evidence: `/app/outputs/bands_output.dat`

### Step 3: DFPT phonon calculation
- Role: process
- Action: Compute interatomic force constants for the relaxed geometries using Quantum ESPRESSO ph.x.
- Evidence: `/app/outputs/ifc_output.dat`

### Step 4: NEGF electron transport
- Role: process
- Action: Calculate the ballistic electron transmittance T(E) from the Hamiltonian and overlap matrices using a non-equilibrium Green's function (NEGF) solver.
- Evidence: `/app/outputs/Te.dat`

### Step 5: NEGF phonon transport
- Role: process
- Action: Calculate the ballistic phonon transmittance T(ω) from the interatomic force constants using a phonon NEGF solver.
- Evidence: `/app/outputs/Tph.dat`

### Step 6: Calculate thermoelectric factors
- Role: process
- Action: From the electron transmittance T(E), evaluate Lorenz integrals and compute electronic conductance G(μ), Seebeck coefficient S(μ), and electronic thermal conductance σ_el(μ) at 300 K. From the phonon transmittance T(ω), compute phononic thermal conductance σ_ph at 300 K.
- Evidence: `/app/outputs/factors_output.npz`

### Step 7: Compute ZT and extract properties
- Role: scored (load-bearing)
- Action: Combine the transport coefficients to compute ZT(μ) at 300 K for each geometry, locate the maximum ZT value, and record the maximum ZT, the phononic thermal conductance at 300 K, and the electronic band gap. Write these quantities for monolayer, zigzag (10,0), and armchair (6,6) WSe2 to the CSV output file.
- Output file: `/app/outputs/step_01_properties.csv`
- Format: csv
- Contract: geometry (string), ZT_max (float), sigma_ph_300K (float), band_gap (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_properties.csv
- path: `/app/outputs/step_01_properties.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: CSV file with one row per geometry. The checker compares ZT_max, sigma_ph_300K, and band_gap values against hidden references using threshold_or_better and also verifies the ordering trends (ZT_monolayer > ZT_zigzag > ZT_armchair; sigma_ph zigzag < monolayer < armchair; band gap monolayer > zigzag > armchair).
- schema:
  - `type`: table
  - `required_columns`: `geometry`, `ZT_max`, `sigma_ph_300K`, `band_gap`

Notes: The agent must implement a ballistic NEGF solver; no specific code is provided. The scoring uses the paper-reported ZT values as hidden references with tolerance and structural ordering checks.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "geometry",
          "ZT_max",
          "sigma_ph_300K",
          "band_gap"
        ]
      },
      "description": "CSV file with one row per geometry. The checker compares ZT_max, sigma_ph_300K, and band_gap values against hidden references using threshold_or_better and also verifies the ordering trends (ZT_monolayer > ZT_zigzag > ZT_armchair; sigma_ph zigzag < monolayer < armchair; band gap monolayer > zigzag > armchair)."
    }
  ],
  "notes": "The agent must implement a ballistic NEGF solver; no specific code is provided. The scoring uses the paper-reported ZT values as hidden references with tolerance and structural ordering checks."
}
```

## How you are scored
Your submitted CSV file is evaluated by a hidden verifier that independently assesses the reported `ZT_max` values, the monotonic ordering of ZT across the three geometries, and the ordering of `sigma_ph_300K` and `band_gap`. The verifier compares your `ZT_max` magnitudes against reference targets and applies structural checks on the sequence of values (e.g., whether the ZT of one geometry is larger than another, etc.). The final reward is a weighted combination of these quantitative and structural checks, with the accuracy of the ZT_max values receiving the largest weight. A correct reproduction of the physical trends and numerical values will earn a high score.

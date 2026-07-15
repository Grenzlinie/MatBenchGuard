# DFT calculation of oxygen vacancy formation energies in SrFe1-xCuxO3

## Problem background
Solid oxide fuel cells (SOFCs) rely on cathode materials with high oxygen reduction reaction (ORR) activity at intermediate temperatures. Perovskite SrFeO3‑δ is a promising Co‑free cathode, but its performance is limited by oxygen vacancy ordering. Aliovalent doping, such as substituting Fe with Cu, is explored to stabilize the cubic phase and modify the oxygen vacancy concentration. The oxygen vacancy formation energy (E_V,O) is a critical quantity: a lower formation energy indicates easier vacancy creation, which can enhance oxygen ion transport and surface exchange. Understanding how Cu doping affects E_V,O provides direct insight into the atomic‑scale origin of improved cathode performance. This task focuses on the first‑principles computation of oxygen vacancy formation energies for pure SrFeO3 and Cu‑substituted SrFe0.75Cu0.25O3.

## Approach
Density functional theory (DFT) calculations are used to model slab geometries and evaluate the energetics of oxygen vacancy formation. A four‑layer slab of cubic SrFeO3 with a (1×2) surface is constructed, and a 15 Å vacuum layer is introduced to avoid spurious interactions between periodic images. The doped system is built by replacing one Fe atom with Cu, yielding a composition of approximately SrFe0.75Cu0.25O3. For both the pure and doped slabs, structures with a single oxygen vacancy at specific sites are created. The vacancy formation energy is computed from the total energies of the perfect slab, the defective slab, and an isolated O2 molecule, following the standard definition E_V,O = E(defective) + 0.5 E(O2) – E(perfect). The calculations are performed with the GGA‑PBE exchange‑correlation functional and an open‑source plane‑wave code (e.g., Quantum ESPRESSO or CP2K), using appropriate pseudopotentials and numerical settings. By comparing the computed E_V,O values for the pure and Cu‑doped systems, one can evaluate the effect of Cu doping on oxygen vacancy formation.

## Reproduction target
Compute, from your own DFT slab calculations, the oxygen vacancy formation energies (in eV) for all identified vacancy sites: V_O1 and V_O2 in SrFeO3; V_O1, V_O2, V_O3, and V_O4 in SrFe0.75Cu0.25O3. Report these energies in the CSV file `/app/outputs/step_01_dft_energies.csv`. Use the obtained numbers to assess whether Cu doping leads to a systematic change in the vacancy formation energy relative to the undoped material.

## Assets

- Quantum ESPRESSO (or CP2K): https://www.quantum-espresso.org/
- PBE pseudopotentials for Sr, Fe, Cu, O: https://www.quantum-espresso.org/pseudopotentials/
- Cubic SrFeO3 crystal structure (Pm-3m, a~3.86 Å): https://materialsproject.org/
- Atomic Simulation Environment (ASE): https://wiki.fysik.dtu.dk/ase/

## Workflow steps

### Step 1: Build slab models
- Role: process
- Action: Construct 1×2 surface four-layer slab models of cubic SrFeO3 and SrFe0.75Cu0.25O3 with a 15 Å vacuum layer. Identify all oxygen vacancy sites: V_O1, V_O2 for the pure system; V_O1, V_O2, V_O3, V_O4 for the Cu-doped system.
- Evidence: `/app/outputs/slab_models.json`

### Step 2: Run DFT calculations
- Role: process
- Action: For each slab model (perfect and each vacancy), perform DFT geometry relaxation (fix bottom two layers) and single-point energy calculation using GGA-PBE functional. Use an open-source DFT code with appropriate pseudopotentials, plane-wave cutoff ≥400 eV, and k-point sampling ~8×4×2. Obtain total energies for all systems.
- Evidence: `/app/outputs/dft_energies.json`

### Step 3: Compute and report formation energies
- Role: scored (load-bearing)
- Action: Calculate oxygen vacancy formation energy E_V,O = E(defective slab) + 0.5 * E(O2) - E(perfect slab) for each vacancy site, using the total energies from DFT and the energy of an isolated O₂ molecule. Output a CSV file with columns: material, vacancy_site, formation_energy_eV.
- Output file: `/app/outputs/step_01_dft_energies.csv`
- Format: csv
- Contract: CSV with header: material,vacancy_site,formation_energy_eV
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_dft_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_dft_energies.csv
- path: `/app/outputs/step_01_dft_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Oxygen vacancy formation energies for SrFeO3 and SrFe0.75Cu0.25O3. The values should show a clear reduction upon Cu doping.
- schema:
  - `type`: table
  - `required_columns`: `material`, `vacancy_site`, `formation_energy_eV`
  - `units`:
    - `formation_energy_eV`: eV

Notes: The checker compares each formation energy to hidden reference values with appropriate tolerances and verifies the trend that the Cu-doped material has a lower formation energy than undoped SrFeO3.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_dft_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "vacancy_site",
          "formation_energy_eV"
        ],
        "units": {
          "formation_energy_eV": "eV"
        }
      },
      "description": "Oxygen vacancy formation energies for SrFeO3 and SrFe0.75Cu0.25O3. The values should show a clear reduction upon Cu doping."
    }
  ],
  "notes": "The checker compares each formation energy to hidden reference values with appropriate tolerances and verifies the trend that the Cu-doped material has a lower formation energy than undoped SrFeO3."
}
```

## How you are scored
A hidden verifier independently reads your submitted `/app/outputs/step_01_dft_energies.csv`. The verifier compares each reported formation energy against reference values using tolerances that account for the expected spread due to different DFT codes and pseudopotentials. In addition, the verifier checks whether the lowest formation energy observed in the Cu‑doped material is lower than the lowest formation energy in the pure material – i.e., whether the overall trend is consistent with Cu doping promoting vacancy formation. The final reward reflects both the accuracy of individual energies and the correctness of the trend. Submitting the paper’s published numbers without performing the actual DFT workflow will not earn credit; you must derive the formation energies from your own calculations.

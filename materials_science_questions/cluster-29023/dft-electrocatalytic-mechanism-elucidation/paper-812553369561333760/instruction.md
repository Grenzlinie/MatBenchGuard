# DFT+U Investigation of CO2 Adsorption on ZnCo2O4 Spinel Surfaces

## Problem background
Rechargeable Na–CO2 batteries are a promising energy storage technology, but their practical use is hindered by sluggish cathode reactions and the difficulty of decomposing the insulating discharge product Na2CO3 during charging. The cathode catalyst plays a central role in both the CO2 reduction reaction (CO2RR) during discharge and the CO2 evolution reaction (CO2ER) during charge. Understanding how CO2, Na atoms, and Na2CO3 interact with candidate catalyst surfaces is crucial for identifying active sites. Density functional theory (DFT) calculations can compute adsorption energies and the electronic structure of different exposed crystal surfaces. In this task, you will investigate the spinel ZnCo2O4 by computing the adsorption strengths of these three species on its low-index [001] and [111] terminations, and by analysing the projected density of states of surface Co atoms. The results will reveal which surfaces and atomic species are likely catalytically active for the Na–CO2 battery reactions.

## Approach
You will use open-source plane-wave DFT via Quantum ESPRESSO with the PBE exchange-correlation functional, a Hubbard U correction of 2 eV on Co, and the DFT-D3 dispersion correction. Pseudopotentials should be taken from the SSSP PBE library (efficiency or precision versions for Zn, Co, O, C, Na).

First, construct slab models for three terminations of cubic spinel ZnCo2O4 (space group Fd-3m, lattice constant a = 8.131 Å):
- the [001] surface,
- the [111] surface where only Co atoms are exposed (the 111_Co surface),
- the [111] surface where both Co and Zn atoms are exposed (the 111_CoZn surface).

Relax each slab with DFT+U, fixing the bottom layers and using a vacuum layer greater than 15 Å. After relaxation, compute the total energy of each clean surface and the total energies of the isolated adsorbates in their own periodic cells: a CO2 molecule, a Na atom (with its energy referenced to half the total energy of bulk bcc sodium), and a Na2CO3 cluster. Then place each adsorbate at stable binding sites on each relaxed slab, re-relax the adsorbate–slab geometry, and obtain the combined total energy.

The adsorption energy for each adsorbate on each surface is defined as
E_ad = E_adsorbate + E_surface – E_total,
where higher positive values indicate stronger binding. For the 111_CoZn surface, CO2 can adsorb in two distinct configurations; you must compute both.

Finally, for each relaxed clean surface, compute the projected density of states (PDOS) of the surface Co atoms, aligning the Fermi level to 0 eV. The PDOS data should cover at least the energy range –2 eV to +2 eV.

All results must be written to the CSV files detailed under Workflow steps and Output contract.

## Reproduction target
Perform the DFT+U calculations described above and produce two CSV files:

1. `/app/outputs/adsorption_energies.csv` — contains the computed adsorption energy of CO2, Na, and Na2CO3 on each of the three surfaces (001, 111_Co, 111_CoZn). For CO2 on the 111_CoZn surface, include two rows for the two different adsorption configurations. Columns: surface, adsorbate, adsorption_energy_eV.

2. `/app/outputs/dos_data.csv` — contains the projected density of states of surface Co atoms on each of the three surfaces, with energy relative to the Fermi level. Columns: surface, energy_eV, pdos_Co.

The task is self-contained; the paper is not provided and must not be consulted. The required outputs are defined entirely by the protocols and file schemas listed in this instruction.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP PBE pseudopotentials: https://www.materialscloud.org/discover/sssp

## Workflow steps

### Step 1: Construct and relax ZnCo2O4 surface slabs
- Role: process
- Action: Construct [001], [111] with only exposed Co atoms, and [111] with exposed Co and Zn atoms surface slabs of spinel ZnCo2O4 (space group Fd-3m, lattice constant a = 8.131 Å). Relax these slabs using DFT+U (U=2 eV for Co), PBE functional, DFT-D3 dispersion correction, keeping bottom layers fixed and vacuum >15 Å. Write relaxed atomic positions to evidence file.
- Evidence: `/app/outputs/slab_positions.extxyz`

### Step 2: Compute adsorption energies of CO2, Na, and Na2CO3
- Role: scored (load-bearing)
- Action: For each relaxed slab, compute total energies of the clean surface, isolated adsorbates (CO2 molecule, Na atom, Na2CO3 cluster), and the slab with the adsorbate at stable adsorption sites. Calculate adsorption energy as E_ad = E_adsorbate + E_surface - E_total. Report all values in /app/outputs/adsorption_energies.csv.
- Output file: `/app/outputs/adsorption_energies.csv`
- Format: csv
- Contract: surface (string), adsorbate (string), adsorption_energy_eV (float)
- Scoring: scored by hidden verifier

### Step 3: Compute projected density of states (PDOS) of surface Co atoms
- Role: scored
- Action: For each relaxed slab, compute the projected density of states for surface Co atoms, align Fermi level to 0 eV, and output data covering the energy range from -2 eV to +2 eV to /app/outputs/dos_data.csv.
- Output file: `/app/outputs/dos_data.csv`
- Format: csv
- Contract: surface (string), energy_eV (float), pdos_Co (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/adsorption_energies.csv`
- `/app/outputs/dos_data.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### adsorption_energies.csv
- path: `/app/outputs/adsorption_energies.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Computed adsorption energies for CO2, Na, and Na2CO3 on the three active ZnCo2O4 surfaces.
- schema:
  - `type`: table
  - `required_columns`: `surface`, `adsorbate`, `adsorption_energy_eV`
  - `units`:
    - `adsorption_energy_eV`: eV

### dos_data.csv
- path: `/app/outputs/dos_data.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Projected density of states of surface Co atoms on the three surfaces, used to confirm unoccupied states at the Fermi level.
- schema:
  - `type`: table
  - `required_columns`: `surface`, `energy_eV`, `pdos_Co`
  - `units`:
    - `energy_eV`: eV
    - `pdos_Co`: arbitrary units

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "adsorption_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "surface",
          "adsorbate",
          "adsorption_energy_eV"
        ],
        "units": {
          "adsorption_energy_eV": "eV"
        }
      },
      "description": "Computed adsorption energies for CO2, Na, and Na2CO3 on the three active ZnCo2O4 surfaces."
    },
    {
      "file": "dos_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "surface",
          "energy_eV",
          "pdos_Co"
        ],
        "units": {
          "energy_eV": "eV",
          "pdos_Co": "arbitrary units"
        }
      },
      "description": "Projected density of states of surface Co atoms on the three surfaces, used to confirm unoccupied states at the Fermi level."
    }
  ],
  "notes": ""
}
```

## How you are scored
After you finish, a hidden verifier independently scores each output artifact. For the adsorption energies, the verifier recomputes the adsorption energies from a hidden set of gold reference values and applies an appropriate tolerance. For the density of states, it checks that for each of the three surfaces there exist surface Co states above the Fermi level (energy > 0 eV with pdos_Co > 0). The two parts are weighted and combined into a single reward between 0 and 1. Simply reporting a number is not sufficient; the verifier evaluates the actual CSV files you write.

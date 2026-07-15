# Hydrogen Adsorption Free Energy and Strain Engineering on TM-Promoted V2CO2 MXenes

## Problem background
The hydrogen evolution reaction (HER) is a key process for sustainable hydrogen production from water splitting. Finding earth-abundant catalysts with a hydrogen adsorption free energy (ΔG_H) close to zero is central to developing cost-effective alternatives to precious metals like platinum. Two-dimensional MXenes, particularly fully oxidized vanadium carbide (V2CO2), have been predicted to be potential HER catalysts when their surface is promoted with transition metals (Fe, Co, Ni). By introducing TM atoms onto the surface, the charge state of the surface oxygen atoms is modified, which in turn tunes the binding strength of hydrogen. The goal of this task is to compute the hydrogen adsorption free energy for various combinations of TM promoter type, coverage, and active site, and to demonstrate how applied biaxial strain can further adjust the catalytic activity towards the optimal ΔG_H ≈ 0 eV.

## Approach
The work uses first-principles density functional theory (DFT) calculations with spin polarization. Supercell models of V2CO2 are constructed with transition metal promoters (Fe, Co, Ni) at coverages of 12.5%, 16.7%, and 25% monolayer (ML). A single hydrogen atom is placed on top of specific surface oxygen atoms — these active sites are labelled T0, T1, T2, and T3, distinguished by the number of surrounding TM atoms (0 to 3). Total energies are obtained from DFT geometry optimizations using an open-source DFT code (e.g., Quantum ESPRESSO) with the PBE functional and PAW pseudopotentials. The hydrogen adsorption free energy is computed as ΔG_H = ΔE_H + ΔE_ZPE − TΔS_H, where ΔE_H is the adsorption energy (computed from slab+adsorbate, clean slab, and H2 molecule energies), and ΔE_ZPE and TΔS_H are vibrational corrections derived from frequency calculations. Bader charge analysis is performed on the self-consistent charge densities to obtain the electron count on the active O atom. For selected systems, a series of biaxial strains (ε = Δa/a0) from -2.5% to +2.5% are applied by uniformly scaling the in-plane lattice constants; the structures are re-optimized and the total energies are collected to compute the strain-dependent ΔG_H. The workflow produces two scored CSV tables: one containing the hydrogen adsorption data for all TM-promoted system combinations, and another containing ΔG_H as a function of strain for the specified active sites.

## Reproduction target
Compute and output the hydrogen adsorption free energy ΔG_H (in eV), the adsorption energy ΔE_H (in eV), and the Bader charge transfer (in e) for all combinations of promoter (Fe, Co, Ni), coverage (12.5% ML, 16.7% ML, 25% ML), and active site (T0, T1, T2, T3). Include also the case of pure V2CO2 at 12.5% ML H coverage. Output these results in a CSV file according to the contract `delta_G_H_table.csv`. Separately, compute ΔG_H as a function of biaxial strain for the following systems: T0 site of 12.5% ML Co, T1 site of 12.5% ML Fe, T2 site of 12.5% ML Co, T3 site of 25% ML Ni, and T3 site of 25% ML Co. Perform calculations at a set of strain values that covers the range from -2.5% to +2.5% (including specifically -0.5% and -0.27%). Output the strain-dependent ΔG_H results in a CSV file according to the contract `strain_dependence.csv`.

## Assets

- Quantum ESPRESSO (or equivalent open-source DFT code): https://www.quantum-espresso.org/
- Bader charge analysis code: http://theory.cm.utexas.edu/henkelman/code/bader/

## Workflow steps

### Step 1: Build structural models
- Role: process
- Action: Construct supercells for V2CO2 monolayer, TM-promoted V2CO2 (Fe, Co, Ni at 12.5%, 16.7%, 25% ML coverage), and all corresponding H-adsorbed configurations. Place H atop surface O atoms at T0, T1, T2, T3 sites as defined. Use standard experimental lattice constants for MXenes.
- Evidence: none

### Step 2: DFT geometry optimization and total energy calculations
- Role: process
- Action: Run spin-polarized DFT calculations (PBE functional, PAW pseudopotentials, appropriate k-point grids) for all clean, TM-promoted, and H‑adsorbed configurations using an open-source DFT code. Fully relax atomic positions (force < 0.02 eV/Å) and collect total energies and self-consistent charge densities.
- Evidence: none

### Step 3: Compute vibrational frequencies and ZPE/entropy corrections
- Role: process
- Action: For each H‑adsorbed configuration (and gas-phase H2), perform vibrational frequency calculations. Compute zero-point energy differences and entropy corrections (ΔZPE and TΔS_H) between adsorbed H and half H₂.
- Evidence: none

### Step 4: Perform Bader charge analysis
- Role: process
- Action: Using the charge density from step 2, run Bader analysis to determine the number of electrons (Ne) on the O atom at each active site for all TM‑promoted systems.
- Evidence: none

### Step 5: Compute ΔG_H and compile final table
- Role: scored (load-bearing)
- Action: Calculate ΔG_H = ΔE_H + ΔE_ZPE − TΔS_H for every TM‑promoted system and active site (including pure V2CO2 at 12.5% ML H coverage). Assemble results in a CSV file with columns: System, Coverage, ActiveSite, DeltaE_H (eV), DeltaG_H (eV), ChargeTransfer (e).
- Output file: `/app/outputs/delta_G_H_table.csv`
- Format: csv
- Contract: Columns: System (str, e.g., 'V2CO2','Fe-V2CO2'), Coverage (str, '12.5%ML','16.7%ML','25%ML'), ActiveSite (str, 'T0','T1','T2','T3'), DeltaE_H (float, eV), DeltaG_H (float, eV), ChargeTransfer (float, e).
- Scoring: scored by hidden verifier

### Step 6: DFT calculations under biaxial strain
- Role: process
- Action: For selected systems (T0(12.5% ML Co), T1(12.5% ML Fe), T2(12.5% ML Co), T3(25% ML Ni), T3(25% ML Co)), scale in-plane lattice constants uniformly by a range of biaxial strain values from ε = −2.5% to +2.5% (including precisely −0.5% and −0.27%). Re-optimize atomic positions and collect total energies.
- Evidence: none

### Step 7: Compute ΔG_H vs strain and compile strain table
- Role: scored
- Action: Use the energies from step 6 and the previously computed ZPE/entropy corrections (assumed transferable) to calculate ΔG_H for each strained configuration. Produce a CSV file with columns: System, Strain, DeltaG_H (eV).
- Output file: `/app/outputs/strain_dependence.csv`
- Format: csv
- Contract: Columns: System (str, e.g., 'T0(12.5% Co)'), Strain (float, fractional), DeltaG_H (float, eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/delta_G_H_table.csv`
- `/app/outputs/strain_dependence.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### delta_G_H_table.csv
- path: `/app/outputs/delta_G_H_table.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Hydrogen adsorption free energies and charge transfer for all TM-promoted V2CO2 systems and active sites.
- schema:
  - `type`: table
  - `required_columns`: `System`, `Coverage`, `ActiveSite`, `DeltaE_H`, `DeltaG_H`, `ChargeTransfer`
  - `units`:
    - `DeltaE_H`: eV
    - `DeltaG_H`: eV
    - `ChargeTransfer`: e

### strain_dependence.csv
- path: `/app/outputs/strain_dependence.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Strain-dependent hydrogen adsorption free energies for selected active sites and systems.
- schema:
  - `type`: table
  - `required_columns`: `System`, `Strain`, `DeltaG_H`
  - `units`:
    - `Strain`: fractional
    - `DeltaG_H`: eV

Notes: The checker compares the submitted CSV values to the paper's reported ΔG_H values and strain trends with appropriate tolerances. The agent must compute all values from DFT; no pre-computed data is provided.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "delta_G_H_table.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "System",
          "Coverage",
          "ActiveSite",
          "DeltaE_H",
          "DeltaG_H",
          "ChargeTransfer"
        ],
        "units": {
          "DeltaE_H": "eV",
          "DeltaG_H": "eV",
          "ChargeTransfer": "e"
        }
      },
      "description": "Hydrogen adsorption free energies and charge transfer for all TM-promoted V2CO2 systems and active sites."
    },
    {
      "file": "strain_dependence.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "System",
          "Strain",
          "DeltaG_H"
        ],
        "units": {
          "Strain": "fractional",
          "DeltaG_H": "eV"
        }
      },
      "description": "Strain-dependent hydrogen adsorption free energies for selected active sites and systems."
    }
  ],
  "notes": "The checker compares the submitted CSV values to the paper's reported ΔG_H values and strain trends with appropriate tolerances. The agent must compute all values from DFT; no pre-computed data is provided."
}
```

## How you are scored
Your submission is scored by a hidden verifier that reads the two CSV files and compares the reported values to reference results (derived from the original publication) with appropriate tolerances. The `delta_G_H_table.csv` is scored on the ΔG_H and charge transfer values for each system/site. The `strain_dependence.csv` is scored on the monotonic decreasing trend of ΔG_H with increasing tensile strain, and on the compliance of ΔG_H at the specific strain values (ε = -0.5% for T2(12.5% Co) and ε = -0.27% for T3(25% Ni)) to be close to zero within a tolerance. Each artifact contributes a weight toward the final score. A faithful reproduction that correctly executes the described DFT workflow and outputs self-consistent, physically correct data will achieve a high score.

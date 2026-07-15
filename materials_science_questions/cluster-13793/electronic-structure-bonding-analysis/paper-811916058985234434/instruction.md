# First-principles stability and electronic structure comparison of CaPtO3 polymorphs

## Problem background
CaPtO3 can crystallize in a post-perovskite (PPV) structure (experimentally synthesized) and a hypothetical perovskite (PV) structure. Understanding the relative stability, density, mechanical stiffness, and electronic character of these two polymorphs provides insight into the factors that stabilize one phase over the other. First-principles density functional theory (DFT) within the local density approximation (LDA) is used to compute total energies as a function of volume for each phase, determine equilibrium volumes and bulk moduli from the equation of state, and calculate the electronic band gaps. This task requires you to compute these quantities for both PPV (space group Cmcm) and PV (space group Pbnm) CaPtO3 using an open‑source plane‑wave DFT code and to compare the two phases.

## Approach
You will first construct starting crystal structures for the two polymorphs using published structural data. For PPV, use experimental lattice parameters and atomic positions; for PV, derive the structure from the isostructural CaIrO3 perovskite by substituting Pt for Ir. The workflow then uses a plane‑wave pseudopotential DFT code (Quantum ESPRESSO) with LDA exchange‑correlation and standard pseudopotentials. For each phase, compute total energies at a series of volumes spanning roughly ±5% around the expected equilibrium, relaxing internal coordinates at each fixed volume. The resulting energy‑volume data are fitted to a second‑order Birch‑Murnaghan equation of state to extract the equilibrium volume V0 and zero‑pressure bulk modulus B0. At the equilibrium geometry, perform a band‑structure calculation along a high‑symmetry k‑point path to obtain the fundamental electronic band gap. Finally, compile the equilibrium energies, volumes, bulk moduli, and band gaps for both phases and compute the energy difference ΔE = E(PV) – E(PPV). All calculations must be traceable to your submitted raw energy‑volume data and the extracted parameters.

## Reproduction target
Produce two scored artifacts:

1. **ev_data.csv**: energy‑volume data for PPV and PV CaPtO3, with at least five volume points per phase. Each row records the phase name, cell volume (Å³), and total energy (eV per formula unit).

2. **summary.json**: a JSON file containing for each phase the fitted equilibrium volume, equilibrium energy per formula unit, bulk modulus, and band gap, together with the energy difference ΔE.

Additionally, submit a band‑gap evidence file (band_gaps.txt) recording the fundamental band gaps extracted from the band‑structure calculations.

The target is to correctly determine these equilibrium properties and the relative ordering of the two phases from first‑principles DFT, without requiring any proprietary software or pre‑computed data.

## Assets

- Crystal structure of PPV-CaPtO3 (Cmcm): 10.1007/s00269-005-0455-3
- Crystal structure of PV-CaIrO3 (Pbnm) for deriving hypothetical PV-CaPtO3: 10.1016/j.pepi.2007.03.006
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- LDA pseudopotentials for Ca, Pt, O: https://pseudopotentials.quantum-espresso.org/legacy_tables/
- Birch-Murnaghan equation of state fitting utility: scipy, ase, pymatgen

## Workflow steps

### Step 1: Prepare crystal structures
- Role: process
- Action: Create initial crystal structure files for PPV-CaPtO3 (space group Cmcm) and hypothetical PV-CaPtO3 (space group Pbnm) using published structural data. For PPV use the experimental lattice parameters and atomic positions from Jung & Oganov (2005). For PV derive from the CaIrO3 perovskite structure (Stølen & Tronnes, 2007) by substituting Pt for Ir and adopting the Pbnm symmetry. Ensure the number of formula units in the simulation cell matches the paper's convention (half-unit cell for Cmcm, full cell for Pbnm).
- Evidence: `/app/outputs/initial_structures.log`

### Step 2: Energy vs. volume calculations
- Role: scored (load-bearing)
- Action: Using Quantum ESPRESSO with LDA pseudopotentials, compute total energies for a series of cell volumes for each phase. Choose at least 5 volumes spanning roughly ±5% around the expected equilibrium volume. For each volume, relax all internal coordinates at fixed lattice vectors. Record the total energy (eV per formula unit) and the volume (Å³). Output the data as a CSV file.
- Output file: `/app/outputs/ev_data.csv`
- Format: csv
- Contract: CSV with columns: phase (string, either 'PPV' or 'PV'), volume_A3 (float), total_energy_eV (float). Energy is per formula unit (the cell energy divided by the number of formula units in the simulation cell).
- Scoring: scored by hidden verifier

### Step 3: Band structure and band gap extraction
- Role: process
- Action: For each phase, identify the volume that minimizes the total energy from the E(V) data. Perform a full band structure calculation at that equilibrium geometry using the same DFT setup, following a standard high-symmetry k-point path appropriate for the orthorhombic Bravais lattice. Extract the fundamental band gap (energy difference between the valence band maximum and conduction band minimum). Save the gap values and any auxiliary diagnostics as evidence.
- Evidence: `/app/outputs/band_gaps.txt`

### Step 4: Compile results and report key properties
- Role: scored
- Action: Fit a second-order Birch-Murnaghan equation of state to the energy-volume data from step 2 for each phase to obtain the equilibrium volume V0 and bulk modulus B0. Take the lowest total energy for each phase as the equilibrium energy. Compute the energy difference ΔE = E(PV) – E(PPV). Combine these values with the band gaps from step 3 and write a JSON summary.
- Output file: `/app/outputs/summary.json`
- Format: json
- Contract: JSON object with keys: 'phases' (array of objects with keys 'phase' (string), 'equilibrium_volume_A3' (float), 'equilibrium_energy_eV_per_fu' (float), 'bulk_modulus_GPa' (float), 'band_gap_eV' (float)), and 'energy_difference_eV' (float, ΔE = E_PV - E_PPV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/ev_data.csv`
- `/app/outputs/summary.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### ev_data.csv
- path: `/app/outputs/ev_data.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Energy versus volume data for PPV and PV CaPtO3 calculated with DFT. The checker refits a second-order Birch-Murnaghan equation of state to verify the fitted equilibrium volume and bulk modulus, and checks relative trends.
- schema:
  - `type`: table
  - `required_columns`: `phase`, `volume_A3`, `total_energy_eV`
  - `units`:
    - `volume_A3`: Å³
    - `total_energy_eV`: eV per formula unit

### summary.json
- path: `/app/outputs/summary.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Compiled DFT results: equilibrium volumes, energies, bulk moduli, band gaps, and energy difference. The checker compares the agent-reported values to the paper's gold values with tolerances and verifies the required trends (V0 PPV < V0 PV, ΔE negative, B0 PPV > B0 PV, band gap PPV > PV).
- schema:
  - `type`: object
  - `required`:
    - `phases`: array of phase result objects
    - `energy_difference_eV`: float
  - `items`:
    - `phase`: string, either 'PPV' or 'PV'
    - `equilibrium_volume_A3`: float, equilibrium cell volume in Å³
    - `equilibrium_energy_eV_per_fu`: float, total energy per formula unit at equilibrium in eV
    - `bulk_modulus_GPa`: float, zero-pressure bulk modulus in GPa
    - `band_gap_eV`: float, fundamental band gap in eV

Notes: The task reproduces the paper's main stability, volume, bulk modulus, and band gap claims. The ASW/ECOV chemical bonding analysis is excluded, as it requires proprietary code and is not needed for the core quantitative claims. The checker fits the E(V) data to recompute V0 and B0, then compares the summary's reported numbers to hidden paper gold values with tolerances. The load-bearing E(V) scan step forces actual DFT calculations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "ev_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "phase",
          "volume_A3",
          "total_energy_eV"
        ],
        "units": {
          "volume_A3": "Å³",
          "total_energy_eV": "eV per formula unit"
        }
      },
      "description": "Energy versus volume data for PPV and PV CaPtO3 calculated with DFT. The checker refits a second-order Birch-Murnaghan equation of state to verify the fitted equilibrium volume and bulk modulus, and checks relative trends."
    },
    {
      "file": "summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "phases": "array of phase result objects",
          "energy_difference_eV": "float"
        },
        "items": {
          "phase": "string, either 'PPV' or 'PV'",
          "equilibrium_volume_A3": "float, equilibrium cell volume in Å³",
          "equilibrium_energy_eV_per_fu": "float, total energy per formula unit at equilibrium in eV",
          "bulk_modulus_GPa": "float, zero-pressure bulk modulus in GPa",
          "band_gap_eV": "float, fundamental band gap in eV"
        }
      },
      "description": "Compiled DFT results: equilibrium volumes, energies, bulk moduli, band gaps, and energy difference. The checker compares the agent-reported values to the paper's gold values with tolerances and verifies the required trends (V0 PPV < V0 PV, ΔE negative, B0 PPV > B0 PV, band gap PPV > PV)."
    }
  ],
  "notes": "The task reproduces the paper's main stability, volume, bulk modulus, and band gap claims. The ASW/ECOV chemical bonding analysis is excluded, as it requires proprietary code and is not needed for the core quantitative claims. The checker fits the E(V) data to recompute V0 and B0, then compares the summary's reported numbers to hidden paper gold values with tolerances. The load-bearing E(V) scan step forces actual DFT calculations."
}
```

## How you are scored
An automated hidden verifier independently scores each workflow stage’s artifact and combines the weighted scores into a final reward between 0 and 1.

- **ev_data.csv**: The verifier refits a second‑order Birch‑Murnaghan equation of state to your raw energy‑volume data. It compares the resulting equilibrium volume and bulk modulus against expected values and checks internal consistency with the summary.json you provide.
- **summary.json**: The verifier compares your reported equilibrium energies, volumes, bulk moduli, band gaps, and ΔE to hidden reference values (within tolerances). It also verifies that the relative ordering of the properties between the two phases is physically correct. The band_gaps.txt evidence is inspected to confirm that the gap extraction was performed.

Simply reporting plausible numbers is not sufficient; the raw data and the fitted parameters must be internally consistent and must arise from a genuine DFT calculation.

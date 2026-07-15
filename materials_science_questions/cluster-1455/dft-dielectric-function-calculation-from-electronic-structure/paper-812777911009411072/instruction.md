# DFT study of Ni-doped ZnO polar and non-polar surface slabs

## Problem background
Dilute magnetic semiconductors (DMS) based on ZnO are promising for spintronic devices, but the magnetic properties of transition-metal-doped ZnO depend strongly on nanostructure, dimensionality, and surface orientation. This work investigates the energetic stability, magnetic ordering, and electronic character of Ni-doped ZnO slabs with two surface terminations: the polar (0001) surface and the non-polar (10-10) surface. Understanding whether Ni impurities preferentially occupy bulk or surface sites and what magnetic ground state arises (ferromagnetic vs. antiferromagnetic) is essential for controlling DMS properties. The central questions are: which defect configuration is most stable, what is the magnetic ground state for each configuration, and whether any configuration exhibits half‑metallic behavior (one spin channel insulating, the other metallic at the Fermi level).

## Approach
The computational approach uses plane‑wave pseudopotential density functional theory (DFT) within the generalized gradient approximation (PBE functional). Periodically repeated slab models are built for the two surface terminations, each containing 96 atoms (Zn and O) in the wurtzite structure. To model Ni doping at a concentration of about 4 %, two Zn atoms are replaced by Ni in three distinct arrangements per surface: 'bulk' (both Ni in interior planes), 'surface' (both Ni on nearest‑neighbour surface sites), and 'mixed' (one Ni interior, one surface). For every defect configuration two independent spin‑polarized calculations are performed: one with the spins of the two Ni atoms aligned ferromagnetically (FM) and one with antiferromagnetic (AFM) coupling. All atomic positions are relaxed in both cases. From the relaxed total energies the relative stability (Er) and the energy difference ΔE = E_AFM – E_FM are determined; the magnetic moments on each Ni atom and the total magnetic moment of the slab are extracted. Density‑of‑states (DOS) calculations on the ground‑state configurations reveal whether a gap appears in one spin channel at the Fermi level, indicating half‑metallicity. The same analysis is carried out for all defect types on both surface terminations, allowing a direct comparison of polar versus non‑polar surfaces.

## Reproduction target
The goal is to compute the relative total energies, the FM/AFM energy differences, the total magnetic moments, the magnetic moments of the two Ni ions, the magnetic ground states, and the half‑metallic character for all six Ni‑doped ZnO slab defect configurations (bulk, surface, and mixed on both the polar (0001) and the non‑polar (10‑10) surfaces). The final deliverables are: (i) a structured JSON file (results.json) containing the raw total energies and the derived quantities for every configuration, and (ii) three density‑of‑states files (dos_nonpolar_bulk.dat, dos_nonpolar_surface.dat, dos_nonpolar_mixed.dat) for the non‑polar surface configurations, each covering an energy window of at least ±5 eV around the Fermi level and providing the total DOS for spin‑up and spin‑down electrons. The quantities to report are detailed in the step contracts below.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Pseudopotentials (PBE) for O, Ni, Zn: https://pseudopotentials.quantum-espresso.org/legacy_tables/ps-library/

## Workflow steps

### Step 1: Generate initial slab models
- Role: process
- Action: Construct 96-atom ZnO wurtzite supercells for the polar (0001) surface (3a×2b×4c) and non-polar (10-10) surface (4a×2b×3c). Substitute two Ni atoms at Zn sites to create three defect configurations per surface: bulk (both Ni in interior sites), surface (both Ni on nearest-neighbor surface sites), and mixed (one Ni interior, one surface). Output the initial atomic coordinates for all six models.
- Evidence: `/app/outputs/slab_models.tar.gz`

### Step 2: Validate pseudopotentials on bulk Ni
- Role: process
- Action: Perform a DFT calculation on bulk fcc Ni to compute the magnetic moment per Ni atom, confirming that the pseudopotential yields a value close to the known experimental value (approx. 0.4–0.5 μB/Ni). Record the magnetic moment.
- Evidence: `/app/outputs/bulk_ni_magnetic_moment.txt`

### Step 3: Run DFT relaxations for all defect configurations
- Role: process
- Action: For each of the six slab models, perform spin-polarized DFT calculations (GGA-PBE) using an open-source plane-wave pseudopotential code. For each configuration, run two calculations: one with ferromagnetic (FM) spin coupling and one with antiferromagnetic (AFM) alignment of the Ni atoms. Fully relax atomic positions. Use parameters consistent with the method (plane-wave cutoff, k-point grids). Record total energies, total magnetic moments, magnetic moments on each Ni atom, and the density of states (DOS). Save the relaxed structures and the numerical data needed for subsequent steps.
- Evidence: `/app/outputs/dft_output.tar.gz`

### Step 4: Compute summary results for all configurations
- Role: scored (load-bearing)
- Action: From the DFT total energies, compute for each defect configuration: (1) the relative energy Er (eV) referenced to the polar surface defect ground state (that configuration has Er = 0), (2) the energy difference ΔE = E_AFM − E_FM (meV), (3) the total magnetic moment (μB) in the ground state, (4) the magnetic moments of the two Ni ions, and (5) the magnetic ground state (FM or AFM). Also indicate whether the configuration exhibits half-metallic character based on the DOS. Save all results in a single JSON file.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with top-level keys: 'polar_bulk', 'polar_surface', 'polar_mixed', 'nonpolar_bulk', 'nonpolar_surface', 'nonpolar_mixed'. Each value is an object with fields: total_energy_FM (number, eV), total_energy_AFM (number, eV), Er_eV (number, eV), ΔE_meV (number, meV), total_magnetic_moment_muB (number, μB), magnetic_moment_Ni1_muB (number, μB), magnetic_moment_Ni2_muB (number, μB), ground_state (string, one of 'FM' or 'AFM'), half_metallic (boolean).
- Scoring: scored by hidden verifier

### Step 5: Extract DOS for non-polar bulk defect
- Role: scored
- Action: For the non-polar (10-10) bulk defect configuration, extract the total density of states around the Fermi level from the DFT output and save as a three-column TSV file (Energy, DOS_up, DOS_down). The energy range should cover at least -5 to 5 eV relative to the Fermi level.
- Output file: `/app/outputs/dos_nonpolar_bulk.dat`
- Format: tsv
- Contract: TSV file with header: Energy(eV), DOS_up, DOS_down. Energy grid spacing no larger than 0.1 eV.
- Scoring: scored by hidden verifier

### Step 6: Extract DOS for non-polar surface defect
- Role: scored
- Action: Extract the total DOS for the non-polar (10-10) surface defect configuration.
- Output file: `/app/outputs/dos_nonpolar_surface.dat`
- Format: tsv
- Contract: Same format as dos_nonpolar_bulk.dat.
- Scoring: scored by hidden verifier

### Step 7: Extract DOS for non-polar mixed defect
- Role: scored
- Action: Extract the total DOS for the non-polar (10-10) mixed defect configuration.
- Output file: `/app/outputs/dos_nonpolar_mixed.dat`
- Format: tsv
- Contract: Same format as dos_nonpolar_bulk.dat.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`
- `/app/outputs/dos_nonpolar_bulk.dat`
- `/app/outputs/dos_nonpolar_surface.dat`
- `/app/outputs/dos_nonpolar_mixed.dat`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Summary of computed results for all six defect configurations. The checker will recompute relative energy Er and energy difference ΔE from the reported total energies and compare them (and other fields) to hidden reference values.
- schema:
  - `type`: object
  - `required`: `polar_bulk`, `polar_surface`, `polar_mixed`, `nonpolar_bulk`, `nonpolar_surface`, `nonpolar_mixed`
  - `per_config`:
    - `required`: `total_energy_FM`, `total_energy_AFM`, `Er_eV`, `ΔE_meV`, `total_magnetic_moment_muB`, `magnetic_moment_Ni1_muB`, `magnetic_moment_Ni2_muB`, `ground_state`, `half_metallic`
    - `types`:
      - `total_energy_FM`: number (eV)
      - `total_energy_AFM`: number (eV)
      - `Er_eV`: number (eV)
      - `ΔE_meV`: number (meV)
      - `total_magnetic_moment_muB`: number (μB)
      - `magnetic_moment_Ni1_muB`: number (μB)
      - `magnetic_moment_Ni2_muB`: number (μB)
      - `ground_state`: string ('FM' or 'AFM')
      - `half_metallic`: boolean

### dos_nonpolar_bulk.dat
- path: `/app/outputs/dos_nonpolar_bulk.dat`
- format: tsv
- purpose: scored
- target_policy: structural_audit
- description: Density of states for the non-polar bulk defect. The checker will verify half-metallic behavior at the Fermi level.
- schema:
  - `type`: table
  - `required_columns`: `Energy(eV)`, `DOS_up`, `DOS_down`
  - `units`:
    - `Energy(eV)`: eV
    - `DOS_up`: states/eV/cell
    - `DOS_down`: states/eV/cell

### dos_nonpolar_surface.dat
- path: `/app/outputs/dos_nonpolar_surface.dat`
- format: tsv
- purpose: scored
- target_policy: structural_audit
- description: Density of states for the non-polar surface defect.
- schema:
  - `type`: table
  - `required_columns`: `Energy(eV)`, `DOS_up`, `DOS_down`
  - `units`:
    - `Energy(eV)`: eV
    - `DOS_up`: states/eV/cell
    - `DOS_down`: states/eV/cell

### dos_nonpolar_mixed.dat
- path: `/app/outputs/dos_nonpolar_mixed.dat`
- format: tsv
- purpose: scored
- target_policy: structural_audit
- description: Density of states for the non-polar mixed defect.
- schema:
  - `type`: table
  - `required_columns`: `Energy(eV)`, `DOS_up`, `DOS_down`
  - `units`:
    - `Energy(eV)`: eV
    - `DOS_up`: states/eV/cell
    - `DOS_down`: states/eV/cell

Notes: The pure ZnO dielectric constant calculation (Table 2) and polar-surface DOS-only half-metallicity verification are omitted per the taskability scope; the paper states that for polar surfaces the DOS metallic behavior prevents a gap-based half-metallic check using GGA. All non-polar configurations are included.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "polar_bulk",
          "polar_surface",
          "polar_mixed",
          "nonpolar_bulk",
          "nonpolar_surface",
          "nonpolar_mixed"
        ],
        "per_config": {
          "required": [
            "total_energy_FM",
            "total_energy_AFM",
            "Er_eV",
            "ΔE_meV",
            "total_magnetic_moment_muB",
            "magnetic_moment_Ni1_muB",
            "magnetic_moment_Ni2_muB",
            "ground_state",
            "half_metallic"
          ],
          "types": {
            "total_energy_FM": "number (eV)",
            "total_energy_AFM": "number (eV)",
            "Er_eV": "number (eV)",
            "ΔE_meV": "number (meV)",
            "total_magnetic_moment_muB": "number (μB)",
            "magnetic_moment_Ni1_muB": "number (μB)",
            "magnetic_moment_Ni2_muB": "number (μB)",
            "ground_state": "string ('FM' or 'AFM')",
            "half_metallic": "boolean"
          }
        }
      },
      "description": "Summary of computed results for all six defect configurations. The checker will recompute relative energy Er and energy difference ΔE from the reported total energies and compare them (and other fields) to hidden reference values."
    },
    {
      "file": "dos_nonpolar_bulk.dat",
      "format": "tsv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "Energy(eV)",
          "DOS_up",
          "DOS_down"
        ],
        "units": {
          "Energy(eV)": "eV",
          "DOS_up": "states/eV/cell",
          "DOS_down": "states/eV/cell"
        }
      },
      "description": "Density of states for the non-polar bulk defect. The checker will verify half-metallic behavior at the Fermi level."
    },
    {
      "file": "dos_nonpolar_surface.dat",
      "format": "tsv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "Energy(eV)",
          "DOS_up",
          "DOS_down"
        ],
        "units": {
          "Energy(eV)": "eV",
          "DOS_up": "states/eV/cell",
          "DOS_down": "states/eV/cell"
        }
      },
      "description": "Density of states for the non-polar surface defect."
    },
    {
      "file": "dos_nonpolar_mixed.dat",
      "format": "tsv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "Energy(eV)",
          "DOS_up",
          "DOS_down"
        ],
        "units": {
          "Energy(eV)": "eV",
          "DOS_up": "states/eV/cell",
          "DOS_down": "states/eV/cell"
        }
      },
      "description": "Density of states for the non-polar mixed defect."
    }
  ],
  "notes": "The pure ZnO dielectric constant calculation (Table 2) and polar-surface DOS-only half-metallicity verification are omitted per the taskability scope; the paper states that for polar surfaces the DOS metallic behavior prevents a gap-based half-metallic check using GGA. All non-polar configurations are included."
}
```

## How you are scored
A hidden verifier inspects each of the scored output files. For results.json the verifier recomputes the relative energy Er and the energy difference ΔE from the supplied total energies and compares them, together with the reported magnetic moments and ground‑state labels, to hidden reference values using appropriate tolerances. For the three DOS files the verifier checks that at the Fermi level one spin channel has a vanishing density of states (a gap) while the other is metallic, in accordance with the half‑metallic criterion. Each scored stage contributes a defined fraction of the total reward; the final score is the weighted sum. Simply reporting a memorised number is not sufficient—the verifier requires internally consistent raw data that reconstructs the target quantities.

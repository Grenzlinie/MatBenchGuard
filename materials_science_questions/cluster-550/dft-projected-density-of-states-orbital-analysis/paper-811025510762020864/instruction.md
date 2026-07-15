# Composition-dependent Projected Density of States of CoPd Alloys from First-Principles

## Problem background
Co$_x$Pd$_{100-x}$ alloy films exhibit perpendicular magnetic anisotropy at low Co concentration, a phenomenon driven by strong Co 3d/Pd 4d hybridization. Understanding how the electronic structure evolves with composition is essential for explaining the magnetic properties. Photoemission spectroscopy can extract partial spectral weights, and first-principles density functional theory (DFT) provides complementary information through the projected density of states (PDOS). This task aims to compute the PDOS for Co 3d and Pd 4d states in ordered Co$_x$Pd$_{100-x}$ alloys as a function of Co concentration, offering insight into the hybridization-driven electronic structure trends.

## Approach
Plane-wave DFT under the local density approximation (LDA) is employed using the open-source Quantum ESPRESSO code with LDA pseudopotentials for Co and Pd. The alloys are modeled in the face-centered cubic (FCC) structure with ordered atomic arrangements: pure Pd, CoPd$_3$ (Cu$_3$Au-type), CoPd (L1$_0$-type), and Co$_3$Pd. For compositions containing Co, spin-polarized (ferromagnetic) self-consistent calculations are performed; for pure Pd, a non-spin-polarized calculation is used. After achieving electronic self-consistency, the density of states projected onto Co 3d and Pd 4d orbitals is extracted and aligned so that the Fermi level is at 0 eV. The resulting PDOS curves for all four compositions are written to CSV files for analysis.

## Reproduction target
Compute and extract the projected density of states (PDOS) onto Co 3d and Pd 4d orbitals for each of the four compositions (x = 0, 25, 50, 75). Produce two CSV files: `pdos_co3d.csv` and `pdos_pd4d.csv`, each containing columns `composition`, `energy_ev` (Fermi level at 0 eV), and `dos` (states/eV). The hidden verifier will analyze these PDOS curves to evaluate composition-dependent structural properties related to hybridization physics.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PSLibrary pseudopotentials (Co, Pd): https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: Generate alloy crystal structures
- Role: process
- Action: Generate FCC crystal structures for ordered Co_xPd_{100-x} alloys at x=0 (pure Pd, 4-atom conventional cell), x=25 (CoPd3, Cu3Au-type 4-atom cell), x=50 (CoPd, L1₀-type 2-atom or 4-atom cell), and x=75 (Co3Pd, 4-atom cell). Use standard experimental lattice parameters or optimize them. Save each structure's atomic positions and lattice vectors.
- Evidence: `/app/outputs/structures.json`

### Step 2: DFT self-consistent calculations
- Role: process
- Action: Using Quantum ESPRESSO with LDA pseudopotentials, perform spin-polarized (ferromagnetic) SCF calculations for x=25,50,75 and a non-spin-polarized calculation for x=0. Use a well-converged k-point mesh and energy cutoff.
- Evidence: `/app/outputs/dft.log`

### Step 3: Co 3d projected density of states
- Role: scored (load-bearing)
- Action: Post-process the DFT output to extract the Co 3d projected DOS for each composition. Align the energy axis so that the Fermi level is at 0 eV. Write a single CSV file /app/outputs/pdos_co3d.csv with columns: composition, energy_ev, dos.
- Output file: `/app/outputs/pdos_co3d.csv`
- Format: csv
- Contract: CSV with columns: composition (int: 0,25,50,75), energy_ev (float, eV, Fermi level at 0 eV), dos (float, states/eV).
- Scoring: scored by hidden verifier

### Step 4: Pd 4d projected density of states
- Role: scored (load-bearing)
- Action: Similarly, extract the Pd 4d projected DOS and write /app/outputs/pdos_pd4d.csv with columns: composition, energy_ev, dos.
- Output file: `/app/outputs/pdos_pd4d.csv`
- Format: csv
- Contract: CSV with columns: composition (int: 0,25,50,75), energy_ev (float, eV, Fermi level at 0 eV), dos (float, states/eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/pdos_co3d.csv`
- `/app/outputs/pdos_pd4d.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### pdos_co3d.csv
- path: `/app/outputs/pdos_co3d.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Co 3d projected density of states for all four compositions. The checker will recompute integrated DOS in a window near the Fermi level and verify trends.
- schema:
  - `type`: table
  - `required_columns`: `composition`, `energy_ev`, `dos`

### pdos_pd4d.csv
- path: `/app/outputs/pdos_pd4d.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Pd 4d projected density of states for all four compositions. The checker will recompute the FWHM of the main peak and verify monotonic ordering.
- schema:
  - `type`: table
  - `required_columns`: `composition`, `energy_ev`, `dos`

Notes: The checker recomputes integrated Co 3d DOS in a [-0.5,0] eV window and Pd 4d FWHM from these CSVs. Trends are compared to the paper's reported behavior. No absolute values are required; only the relative trends (peak at x=25% for Co, monotonic increase for Pd) are scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "pdos_co3d.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition",
          "energy_ev",
          "dos"
        ]
      },
      "description": "Co 3d projected density of states for all four compositions. The checker will recompute integrated DOS in a window near the Fermi level and verify trends."
    },
    {
      "file": "pdos_pd4d.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition",
          "energy_ev",
          "dos"
        ]
      },
      "description": "Pd 4d projected density of states for all four compositions. The checker will recompute the FWHM of the main peak and verify monotonic ordering."
    }
  ],
  "notes": "The checker recomputes integrated Co 3d DOS in a [-0.5,0] eV window and Pd 4d FWHM from these CSVs. Trends are compared to the paper's reported behavior. No absolute values are required; only the relative trends (peak at x=25% for Co, monotonic increase for Pd) are scored."
}
```

## How you are scored
The hidden verifier reads your two CSV files. For Co 3d, it recomputes a characteristic property of the PDOS near the Fermi level for each composition and checks for a specific composition-dependent trend. For Pd 4d, it recomputes a characteristic bandwidth measure and checks for a specific monotonic trend across compositions. Both checks must pass for full credit; partial credit is awarded if only one passes. You are not required to report any metric yourself — the verifier performs the analysis independently from your raw PDOS data.

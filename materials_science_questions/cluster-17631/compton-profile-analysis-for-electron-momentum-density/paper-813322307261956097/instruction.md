# Compton Profile Anisotropies and Phase Transition Pressure of SrO from DFT

## Problem background
Strontium oxide (SrO) is a technologically important II–VI compound that crystallizes in the rocksalt (B1) structure at ambient conditions. Under pressure it is expected to undergo a structural phase transition to the cesium chloride (B2) phase. The electron momentum density, accessible via Compton scattering, reflects the occupied electronic states and provides direct insight into the nature of the chemical bonding. This task reproduces the computational determination of the directional Compton profile anisotropies in the B1 phase and the B1→B2 phase transition pressure from first‑principles density‑functional theory (DFT). The result is a quantitative assessment of the momentum‑space anisotropy and the thermodynamic stability of the two competing phases.

## Approach
All calculations use the Perdew–Burke–Ernzerhof (PBE) exchange‑correlation functional within the plane‑wave DFT code Quantum ESPRESSO, together with standard solid‑state pseudopotentials from the SSSP library. 

First, a self‑consistent field (SCF) calculation is performed for the B1 phase at the experimental equilibrium lattice constant. From the converged wavefunctions the electron momentum density is constructed, and the directional Compton profiles J(p_z) along the [100], [110], and [111] crystallographic axes are extracted. Each profile is convoluted with a Gaussian of 0.6 a.u. full‑width at half‑maximum to approximate the experimental resolution. The anisotropy curves ΔJ(p_z) = J_dir1 − J_dir2 are then computed for the three independent direction pairs. 

Independently, total energies are computed for both the B1 and B2 phases over a range of volumes spanning the expected transition. The energy‑volume data for each phase are fitted to the third‑order Birch–Murnaghan equation of state. From these fits the enthalpy H = E + PV is obtained over a pressure range, and the B1→B2 transition pressure is identified as the pressure at which the two enthalpy curves intersect. The entire procedure is fully computational and uses only publicly available crystal structures and open‑source software.

## Reproduction target
Produce two output artifacts:

1. **Directional Compton profile anisotropy curves** — a CSV file (`anisotropy_curves.csv`) with columns `p_z`, `delta_100_110`, `delta_100_111`, `delta_110_111`, covering the momentum range 0.0 a.u. to 5.0 a.u. with at least 50 points. The values are the convoluted difference profiles for the three crystallographic direction pairs.

2. **B1→B2 phase transition pressure** — a text file (`transition_pressure.txt`) containing a single floating‑point number that is the pressure (in GPa) at which the enthalpy of the B2 phase becomes lower than that of the B1 phase, as determined from the Birch–Murnaghan equation of state fits.

## Assets

- Quantum ESPRESSO (≥7.x): https://www.quantum-espresso.org/
- SSSP PBE pseudopotentials for Sr and O: https://www.materialscloud.org/discover/sssp/table/pbe
- SrO crystal structures (B1 and B2)

## Workflow steps

### Step 1: DFT self-consistent calculation for B1 SrO
- Role: process
- Action: Perform a DFT‑PBE self‑consistent field calculation for rocksalt SrO at the experimental equilibrium lattice constant (a=5.16 Å) using Quantum ESPRESSO and SSSP PBE pseudopotentials.
- Evidence: `/app/outputs/scf.out`

### Step 2: Compute directional Compton profiles and convolve
- Role: process
- Action: From the self‑consistent wavefunctions, compute the electron momentum density and directional Compton profiles J(p_z) along the [100], [110], and [111] directions. Convolve each profile with a Gaussian of 0.6 a.u. FWHM.
- Evidence: `/app/outputs/compton_profiles.txt`

### Step 3: Directional anisotropy curves
- Role: scored (load-bearing)
- Action: Use the convoluted directional profiles to compute ΔJ(p_z) = J_dir1(p_z) − J_dir2(p_z) for [100]–[110], [100]–[111], and [110]–[111]. Output the three curves as a CSV covering p_z from 0.0 to 5.0 a.u. with at least 50 points.
- Output file: `/app/outputs/anisotropy_curves.csv`
- Format: csv
- Contract: Columns: p_z (a.u., float), delta_100_110 (float), delta_100_111 (float), delta_110_111 (float)
- Scoring: scored by hidden verifier

### Step 4: DFT total energy vs volume for B1 and B2 phases
- Role: process
- Action: Perform DFT‑PBE total energy calculations for both B1 (rocksalt) and B2 (CsCl) phases over a range of volumes: B1 lattice parameter from 4.8 to 5.4 Å in ~10–15 steps; B2 from 2.9 to 3.3 Å similarly. No internal relaxation needed.
- Evidence: `/app/outputs/ev_data.txt`

### Step 5: Phase transition pressure from EOS fit
- Role: scored (load-bearing)
- Action: Fit the energy-volume data for each phase to the third‑order Birch–Murnaghan equation of state. Compute enthalpy H = E+PV over 0–50 GPa and find the pressure where the two enthalpy curves intersect (B1→B2 transition). Write the transition pressure (in GPa) to the output file.
- Output file: `/app/outputs/transition_pressure.txt`
- Format: txt
- Contract: Single float number (e.g., 35.8)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/anisotropy_curves.csv`
- `/app/outputs/transition_pressure.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### anisotropy_curves.csv
- path: `/app/outputs/anisotropy_curves.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Directional Compton profile anisotropy curves. The checker will verify physical consistency of the curves.
- schema:
  - `type`: table
  - `required_columns`: `p_z`, `delta_100_110`, `delta_100_111`, `delta_110_111`
  - `units`:
    - `p_z`: a.u.
    - `delta_100_110`: a.u.
    - `delta_100_111`: a.u.
    - `delta_110_111`: a.u.
  - `description`: At least 50 rows covering p_z from 0.0 to 5.0 a.u.

### transition_pressure.txt
- path: `/app/outputs/transition_pressure.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: The B1→B2 phase transition pressure in GPa. Checker compares against a hidden reference value with tolerance.
- schema:
  - `type`: text
  - `description`: A single floating-point number (the transition pressure in GPa).

Notes: The reproduction uses Quantum ESPRESSO instead of the paper's CRYSTAL code to avoid proprietary software. The Compton profiles computation may involve custom post‑processing (e.g. QE pp module or custom scripts). The Birch–Murnaghan fitting can be performed with standard Python libraries.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "anisotropy_curves.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "p_z",
          "delta_100_110",
          "delta_100_111",
          "delta_110_111"
        ],
        "units": {
          "p_z": "a.u.",
          "delta_100_110": "a.u.",
          "delta_100_111": "a.u.",
          "delta_110_111": "a.u."
        },
        "description": "At least 50 rows covering p_z from 0.0 to 5.0 a.u."
      },
      "description": "Directional Compton profile anisotropy curves. The checker will verify physical consistency of the curves."
    },
    {
      "file": "transition_pressure.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "A single floating-point number (the transition pressure in GPa)."
      },
      "description": "The B1→B2 phase transition pressure in GPa. Checker compares against a hidden reference value with tolerance."
    }
  ],
  "notes": "The reproduction uses Quantum ESPRESSO instead of the paper's CRYSTAL code to avoid proprietary software. The Compton profiles computation may involve custom post‑processing (e.g. QE pp module or custom scripts). The Birch–Murnaghan fitting can be performed with standard Python libraries."
}
```

## How you are scored
A hidden verifier reads the two output files and independently scores them. For the anisotropy curves, the verifier performs a structural audit that checks whether the curves satisfy physically expected relationships (e.g., relative magnitudes and sign in the low‑momentum region). For the transition pressure, the verifier compares your reported value against a hidden reference with an appropriate tolerance. Both checks are mandatory; the overall reward is a weighted combination of the two scores. Submitting plausible numbers without executing the required DFT workflow will not yield a passing score.

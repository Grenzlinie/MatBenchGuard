# Point defect formation and electronic structure from DFT

## Problem background
Erbium oxide (Er₂O₃) is a candidate tritium permeation barrier (TPB) coating for fusion reactors. Understanding how hydrogen isotopes interact with the Er₂O₃ surface and bulk is critical for evaluating its permeation reduction performance. This work uses first-principles density functional theory (DFT) to quantify hydrogen adsorption, penetration, diffusion, and vacancy trapping on cubic Er₂O₃(001).

## Approach
Spin-polarized DFT calculations are performed using a generalized gradient approximation (GGA) functional. A stoichiometric Er-terminated slab model of the cubic Er₂O₃(001) surface is built with sufficient layers and vacuum, including dipole corrections. Hydrogen adsorption energies at candidate surface sites are computed and corrected for zero-point energy (ZPE). Penetration pathways from the most stable surface site into subsurface sites, and diffusion barriers between interstitial sites in the bulk (tetrahedral-to-tetrahedral and tetrahedral-to-octahedral), are obtained via the nudged elastic band method. The interaction of hydrogen with a neutral oxygen vacancy is evaluated by comparing the energy of H near the vacancy to that of an interstitial H in bulk. All calculations aim at reproducing energetic quantities that characterize the H permeation barrier.

## Reproduction target
Produce the following quantities for cubic Er₂O₃(001):
- Bulk lattice constant (nm) and bulk modulus (GPa) from fitting the Birch-Murnaghan equation of state.
- GGA band gap (eV) at the Γ point.
- H adsorption energy (kJ/mol) at the most stable surface site with zero-point energy correction.
- H penetration energy barrier (eV) from the surface to a subsurface tetrahedral site, including ZPE.
- Bulk diffusion barriers (eV) for TS→TS and TS→OS hops with ZPE.
- Energy of H near an oxygen vacancy relative to a bulk tetrahedral interstitial (eV); a negative value indicates exothermic trapping.
Report the results in the required CSV and JSON file formats.

## Assets

- Quantum ESPRESSO (open-source DFT package) or equivalent: https://www.quantum-espresso.org/download
- Pseudopotentials for Er, O, H (e.g., from SSSP library, PBE/PW91 family): https://www.materialscloud.org/discover/sssp/table/efficiency
- Python scientific stack (numpy, pandas, ase, matplotlib, etc.): numpy pandas ase matplotlib

## Workflow steps

### Step 1: Bulk Er2O3 DFT verification
- Role: scored
- Action: Perform spin-polarized DFT calculation on cubic Er2O3 (space group Ia3) using GGA functional (PW91 or equivalent). Optimize the lattice constant, compute the bulk modulus by fitting the Birch-Murnaghan equation of state, and evaluate the GGA band gap at the Γ point. Write results to step_01_bulk_verification.csv.
- Output file: `/app/outputs/step_01_bulk_verification.csv`
- Format: csv
- Contract: CSV with columns: property (string), value (float), unit (string). Rows: lattice_constant, bulk_modulus, band_gap.
- Scoring: scored by hidden verifier

### Step 2: Er2O3(001) slab construction and relaxation
- Role: process
- Action: From the bulk structure obtained in step_01, build a stoichiometric Er-terminated (001) slab with 12–16 atomic layers and a vacuum layer >1 nm. Include dipole corrections. Relax the top four atomic layers (both Er and O atoms) while keeping the bottom layers frozen at their bulk-optimized positions.
- Evidence: `/app/outputs/slab_relaxed.xyz`

### Step 3: H adsorption energy calculations
- Role: scored (load-bearing)
- Action: Using the relaxed slab from step_02, compute total energies for atomic H placed at six candidate adsorption sites (A–F). For each site, relax the H atom and the top four layers. Calculate the adsorption energy as (Eads)_d = E(slab+H) − E(slab) − 0.5·E(H2). Compute zero-point energy (ZPE) corrections from H vibrational frequencies. Identify the most stable site (A). Report adsorption energies (with and without ZPE) for sites A, C, and E in step_03_adsorption_energies.csv.
- Output file: `/app/outputs/step_03_adsorption_energies.csv`
- Format: csv
- Contract: CSV with columns: site (string), adsorption_energy_kJ_per_mol (float), adsorption_energy_with_ZPE_kJ_per_mol (float), notes (string). Must contain row for site A with ZPE-corrected energy.
- Scoring: scored by hidden verifier

### Step 4: H penetration and bulk diffusion barriers
- Role: scored
- Action: 1. Penetration: On the slab from step_02, perform a nudged elastic band (NEB) calculation with 12 images to find the minimum energy pathway for H from surface site A to a subsurface tetrahedral site L2. Extract the ZPE-corrected barrier.  2. Bulk diffusion: In bulk Er2O3, use NEB to compute diffusion barriers for H hopping between two tetrahedral sites (TS→TS along ⟨111⟩), from a tetrahedral to an octahedral site (TS→OS), and between two octahedral sites (OS→OS). Include ZPE corrections. Write all four ZPE-corrected barriers (in eV) to step_04_penetration_and_diffusion.json.
- Output file: `/app/outputs/step_04_penetration_and_diffusion.json`
- Format: json
- Contract: JSON object with keys: penetration_energy_barrier_eV (float), TS_to_TS_barrier_eV (float), TS_to_OS_barrier_eV (float), OS_to_OS_barrier_eV (float).
- Scoring: scored by hidden verifier

### Step 5: H trapping at an oxygen vacancy
- Role: scored
- Action: Create a supercell of bulk Er2O3 with a neutral oxygen vacancy. Place a H atom at a tetrahedral-like site near the vacancy and relax the system using DFT. Compute the energy of the H-vacancy system relative to an interstitial H at a bulk tetrahedral site. If the relative energy is negative, the trapping is exothermic. Report the value (in eV) in step_05_vacancy_trapping.json.
- Output file: `/app/outputs/step_05_vacancy_trapping.json`
- Format: json
- Contract: JSON with key h_near_vacancy_relative_energy_eV (float). Negative indicates exothermic trapping.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_bulk_verification.csv`
- `/app/outputs/step_03_adsorption_energies.csv`
- `/app/outputs/step_04_penetration_and_diffusion.json`
- `/app/outputs/step_05_vacancy_trapping.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_bulk_verification.csv
- path: `/app/outputs/step_01_bulk_verification.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Bulk properties: lattice constant in nm, bulk modulus in GPa, band gap in eV.
- schema:
  - `type`: table
  - `required_columns`: `property`, `value`, `unit`
  - `units`:
    - `value`: as per unit column

### step_03_adsorption_energies.csv
- path: `/app/outputs/step_03_adsorption_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: H adsorption energies on cubic Er2O3(001) at sites A, C, E; site A with ZPE is the key reference.
- schema:
  - `type`: table
  - `required_columns`: `site`, `adsorption_energy_kJ_per_mol`, `adsorption_energy_with_ZPE_kJ_per_mol`, `notes`
  - `units`:
    - `adsorption_energy_kJ_per_mol`: kJ/mol
    - `adsorption_energy_with_ZPE_kJ_per_mol`: kJ/mol

### step_04_penetration_and_diffusion.json
- path: `/app/outputs/step_04_penetration_and_diffusion.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Penetration barrier and bulk diffusion barriers (TS→TS, TS→OS, OS→OS), all with ZPE corrections, in eV.
- schema:
  - `type`: object
  - `required`:
    - `penetration_energy_barrier_eV`: number
    - `TS_to_TS_barrier_eV`: number
    - `TS_to_OS_barrier_eV`: number
    - `OS_to_OS_barrier_eV`: number

### step_05_vacancy_trapping.json
- path: `/app/outputs/step_05_vacancy_trapping.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Energy of H near an O vacancy relative to bulk tetrahedral site; negative = exothermic trapping.
- schema:
  - `type`: object
  - `required`:
    - `h_near_vacancy_relative_energy_eV`: number

Notes: All values are compared to paper-reported reference values with tolerances accounting for different DFT implementations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_bulk_verification.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "property",
          "value",
          "unit"
        ],
        "units": {
          "value": "as per unit column"
        }
      },
      "description": "Bulk properties: lattice constant in nm, bulk modulus in GPa, band gap in eV."
    },
    {
      "file": "step_03_adsorption_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "site",
          "adsorption_energy_kJ_per_mol",
          "adsorption_energy_with_ZPE_kJ_per_mol",
          "notes"
        ],
        "units": {
          "adsorption_energy_kJ_per_mol": "kJ/mol",
          "adsorption_energy_with_ZPE_kJ_per_mol": "kJ/mol"
        }
      },
      "description": "H adsorption energies on cubic Er2O3(001) at sites A, C, E; site A with ZPE is the key reference."
    },
    {
      "file": "step_04_penetration_and_diffusion.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "penetration_energy_barrier_eV": "number",
          "TS_to_TS_barrier_eV": "number",
          "TS_to_OS_barrier_eV": "number",
          "OS_to_OS_barrier_eV": "number"
        }
      },
      "description": "Penetration barrier and bulk diffusion barriers (TS→TS, TS→OS, OS→OS), all with ZPE corrections, in eV."
    },
    {
      "file": "step_05_vacancy_trapping.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "h_near_vacancy_relative_energy_eV": "number"
        }
      },
      "description": "Energy of H near an O vacancy relative to bulk tetrahedral site; negative = exothermic trapping."
    }
  ],
  "notes": "All values are compared to paper-reported reference values with tolerances accounting for different DFT implementations."
}
```

## How you are scored
Each output file (step_01_bulk_verification.csv, step_03_adsorption_energies.csv, step_04_penetration_and_diffusion.json, step_05_vacancy_trapping.json) is read by a hidden verifier. The verifier extracts the numeric values and compares them against reference values derived from the original study using appropriate tolerances that account for different DFT implementations. Every scored workflow step carries a weight, and the final reward is the weighted sum of per-step scores. Correct units and agreement with the reference within tolerance earn full credit. There is no penalty for achieving a more accurate result than the reference. Simply reporting numbers without executing the steps will not pass.

# First-principles study of magnetic ordering and band-gap tuning in monolayer Ni(OH)₂ under biaxial strain

## Problem background
Two-dimensional (2D) layered materials are promising platforms for spintronics, but pristine graphene lacks intrinsic magnetism. Monolayer nickel hydroxide, Ni(OH)₂, has been synthesized as ultrathin nanosheets and contains partially filled Ni 3d orbitals, suggesting interesting spin polarization and magnetic coupling. However, its detailed ground-state electronic structure and magnetic ordering remain to be determined. Furthermore, the effect of biaxial strain on the magnetic state and band gap—key for potential spintronic devices—has not been rigorously characterized. This task aims to compute, from first principles, the magnetic ground state (antiferromagnetic vs. ferromagnetic), the electronic band gap and its direct/indirect nature, and the evolution of these properties under a range of biaxial strains for a hexagonal monolayer Ni(OH)₂.

## Approach
The computational approach uses plane-wave density functional theory (DFT) with the PBE functional for structural optimization and total-energy comparisons, a hybrid functional (HSE06) for accurate electronic structure, and the DFT-D3 van der Waals correction to capture out-of-plane interactions. The workflow first relaxes the geometry of an isolated hexagonal Ni(OH)₂ monolayer, then verifies dynamical stability via phonon dispersion. For the pristine system, total energies are computed for antiferromagnetic (AFM), ferromagnetic (FM), and nonmagnetic (NM) spin configurations in a supercell to determine the magnetic ground state, and the HSE06 band gap at the Γ point is evaluated. To probe strain effects, biaxial strains from compressive to tensile values (-10%, -4%, 0%, +4%, +10%) are applied, and the AFM–FM energy differences and HSE06 band gaps are recomputed at each strain. The quantities to be reported are the lattice constant, Ni magnetic moment, AFM–FM energy difference, HSE06 band gap, and a direct-gap indicator for the pristine system, as well as the energy difference and band gap for each strain.

## Reproduction target
Produce two scored JSON files under `/app/outputs`:

1. `pristine_results.json` – an object with keys `lattice_constant_A` (float, Å), `Ni_magnetic_moment_muB` (float, μB), `AFM_FM_energy_diff_meV` (float, meV), `HSE06_band_gap_eV` (float, eV), and `band_gap_direct` (boolean).

2. `strain_results.json` – an array of objects for the five strain values -10, -4, 0, +4, +10 (in percent), each containing `strain_percent` (float), `AFM_FM_energy_diff_meV` (float), and `HSE06_band_gap_eV` (float).

Additionally, run two mandatory process steps: (i) PBE geometry relaxation, saving the relaxed structure to `relaxed_structure.json`; (ii) phonon dispersion calculation with Phonopy on a 4×4×1 supercell, verifying no imaginary modes and saving the dispersion to `phonon_dispersion.json`. These are required but not directly scored.

## Assets

- First-principles DFT code supporting PBE PAW pseudopotentials, HSE06 hybrid functional, and DFT-D3 van der Waals correction (e.g., Quantum ESPRESSO, VASP, CP2K, GPAW, ABINIT)
- Phonopy: https://phonopy.github.io/phonopy/
- PBE and HSE06 pseudopotentials / PAW datasets for Ni, O, H

## Workflow steps

### Step 1: PBE geometry relaxation
- Role: process
- Action: Construct the hexagonal monolayer Ni(OH)₂ unit cell, relax atomic positions and lattice vectors using the PBE functional, a vacuum layer >15 Å, and DFT-D3 van der Waals correction until forces and energy converge. Save the relaxed geometry.
- Evidence: `/app/outputs/relaxed_structure.json`

### Step 2: Phonon stability verification
- Role: process
- Action: Build a 4×4×1 supercell from the relaxed structure, compute the phonon dispersion using Phonopy (Parlinski-Li-Kawazoe method) with forces from the same DFT settings. Verify that no imaginary phonon modes appear.
- Evidence: `/app/outputs/phonon_dispersion.json`

### Step 3: Pristine magnetic energies and HSE06 band gap
- Role: scored
- Action: Using a 2×2×1 supercell of the relaxed PBE structure, compute total energies for AFM, FM, and NM spin configurations with PBE. Extract the average Ni atomic magnetic moment from the AFM calculation. Then, using the HSE06 hybrid functional on the same PBE geometry, compute the electronic band structure and determine the band gap at the Γ point and whether it is direct. Write a JSON file with the lattice constant, Ni moment, AFM-FM energy difference, HSE06 band gap, and direct-gap indicator.
- Output file: `/app/outputs/pristine_results.json`
- Format: json
- Contract: {"lattice_constant_A": float, "Ni_magnetic_moment_muB": float, "AFM_FM_energy_diff_meV": float, "HSE06_band_gap_eV": float, "band_gap_direct": true/false}
- Scoring: scored by hidden verifier

### Step 4: Strain-dependent properties
- Role: scored (load-bearing)
- Action: Apply biaxial strains of -10%, -4%, 0%, +4%, +10% to the relaxed unit cell. For each strain, compute PBE total energies for AFM and FM configurations to obtain the energy difference, and compute the HSE06 band gap. Write a JSON array with each strain's value, energy difference, and band gap.
- Output file: `/app/outputs/strain_results.json`
- Format: json
- Contract: [{"strain_percent": float, "AFM_FM_energy_diff_meV": float, "HSE06_band_gap_eV": float}]
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/pristine_results.json`
- `/app/outputs/strain_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### pristine_results.json
- path: `/app/outputs/pristine_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Pristine monolayer properties: lattice constant (Å), Ni magnetic moment (μB), AFM‑FM energy difference (meV), HSE06 band gap (eV), and whether the gap is direct.
- schema:
  - `type`: object
  - `required`:
    - `lattice_constant_A`: float
    - `Ni_magnetic_moment_muB`: float
    - `AFM_FM_energy_diff_meV`: float
    - `HSE06_band_gap_eV`: float
    - `band_gap_direct`: boolean

### strain_results.json
- path: `/app/outputs/strain_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Array of objects for each biaxial strain (-10, -4, 0, +4, +10%), each containing the strain value, AFM‑FM energy difference (meV), and HSE06 band gap (eV).
- schema:
  - `type`: array
  - `items`:
    - `strain_percent`: float
    - `AFM_FM_energy_diff_meV`: float
    - `HSE06_band_gap_eV`: float

Notes: The solver may use any open‑source DFT code with the required functionality. The phonon stability check is mandatory but not scored. All values are compared to paper‑reported reference data with appropriate tolerances and trend checks.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "pristine_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "lattice_constant_A": "float",
          "Ni_magnetic_moment_muB": "float",
          "AFM_FM_energy_diff_meV": "float",
          "HSE06_band_gap_eV": "float",
          "band_gap_direct": "boolean"
        }
      },
      "description": "Pristine monolayer properties: lattice constant (Å), Ni magnetic moment (μB), AFM‑FM energy difference (meV), HSE06 band gap (eV), and whether the gap is direct."
    },
    {
      "file": "strain_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "strain_percent": "float",
          "AFM_FM_energy_diff_meV": "float",
          "HSE06_band_gap_eV": "float"
        }
      },
      "description": "Array of objects for each biaxial strain (-10, -4, 0, +4, +10%), each containing the strain value, AFM‑FM energy difference (meV), and HSE06 band gap (eV)."
    }
  ],
  "notes": "The solver may use any open‑source DFT code with the required functionality. The phonon stability check is mandatory but not scored. All values are compared to paper‑reported reference data with appropriate tolerances and trend checks."
}
```

## How you are scored
A hidden verifier scores each scored artifact independently, then combines the weighted scores into a final reward. For `pristine_results.json`, the verifier compares the reported lattice constant, Ni magnetic moment, AFM–FM energy difference, HSE06 band gap, and direct-gap indicator against reference values derived from the original study, within predefined tolerances. For `strain_results.json`, it compares the energy differences and band gaps at each strain, and also checks that the overall trends (e.g., the sign of the energy difference indicates which magnetic order is lower in energy, and the band gap changes monotonically with strain) are physically consistent with the applied conditions. Reporting numbers that align with the underlying physics, as verified against hidden reference data, yields a higher reward. The phonon stability check is mandatory but carries no direct reward; failure to perform it may cause downstream steps to be invalid.

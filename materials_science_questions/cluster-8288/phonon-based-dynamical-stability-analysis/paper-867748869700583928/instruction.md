# Dynamical and electronic properties of a cI24 sodium phase at terapascal pressures

## Problem background
Sodium (Na) at high pressure exhibits a metal-insulator transition: above 200 GPa it adopts a wide-gap insulating phase with a double-hexagonal hP4 structure. It remains insulating over a large pressure range, and the pressure at which it eventually reverts to a metallic state is an open question. At terapascal (TPa) pressures, structure searches can identify candidate phases beyond simple packing. The present task investigates a candidate body-centred cubic phase of Na (cI24) and a competing orthorhombic oP8 phase. By computing their structural, dynamical, and electronic properties at 16 TPa, we can assess which phase is stable and whether the system returns to a metallic state.

## Approach
Use plane-wave density functional theory (DFT) with the Perdew–Burke–Ernzerhof (PBE) generalised gradient approximation and a norm-conserving pseudopotential for Na. Perform geometry optimisations at a fixed pressure of 16 TPa for both the cI24 and oP8 phases, allowing atomic positions and lattice parameters to relax. From the optimised structures, compute the phonon dispersion of cI24 using the finite-displacement method and extract the minimum frequency to check for dynamical stability. Compute the electronic band structure of cI24 (using a hybrid functional such as HSE06) and determine its band gap. Finally, compare the enthalpies H = E + PV of cI24 and oP8 per atom to identify which phase is thermodynamically more stable at 16 TPa.

## Reproduction target
Obtain the following four quantities for the candidate cI24 phase of sodium at 16 TPa, and compare the enthalpy of cI24 with that of the competing oP8 phase:

- Optimised cubic lattice parameter a (in Å) of cI24.
- Minimum phonon frequency (in THz) of cI24; a positive value indicates no imaginary modes and dynamical stability.
- Electronic band gap (in eV) of cI24; a gap of zero indicates metallic behaviour.
- Enthalpy difference per atom ΔH = H(cI24) – H(oP8) (in eV/atom); a negative sign means cI24 is more stable.

## Assets

- cI24 initial structure
- oP8 initial structure
- Quantum ESPRESSO: https://www.quantum-espresso.org
- Phonopy: phonopy
- Na pseudopotential (GGA-PBE): SSSP library

## Workflow steps

### Step 1: Optimize cI24 structure and extract lattice parameter
- Role: scored
- Action: Perform DFT geometry optimization of the cI24 structure at 16 TPa using a plane-wave DFT code (e.g., Quantum ESPRESSO). Extract the optimized cubic lattice parameter a (in Å) and write it to the output file.
- Output file: `/app/outputs/cI24_lattice_parameter.txt`
- Format: txt
- Contract: Single floating-point number representing the lattice parameter a in angstroms.
- Scoring: scored by hidden verifier

### Step 2: Optimize oP8 structure and obtain total energy
- Role: process
- Action: Perform DFT geometry optimization of the oP8 structure at 16 TPa to obtain its total energy and volume. Save the total energy per unit cell (in eV) and unit cell volume (in Å³) to an evidence file.
- Evidence: `/app/outputs/oP8_energy.txt`

### Step 3: Compute enthalpy difference between cI24 and oP8
- Role: scored (load-bearing)
- Action: Using the total energies and volumes from the optimized cI24 and oP8 structures, compute the enthalpy difference ΔH = H(cI24) − H(oP8) at 16 TPa per atom and write it to the output file.
- Output file: `/app/outputs/enthalpy_difference.txt`
- Format: txt
- Contract: Single floating-point number, enthalpy difference per atom in eV/atom. A negative value indicates cI24 is more stable.
- Scoring: scored by hidden verifier

### Step 4: Compute phonon dispersion of cI24 and get minimum frequency
- Role: scored
- Action: Calculate the phonon dispersion of the optimized cI24 structure using the finite-displacement method with a phonon package (e.g., Phonopy) and DFT, and extract the minimum phonon frequency (in THz). Write the value to the output file.
- Output file: `/app/outputs/cI24_phonon_min_freq.txt`
- Format: txt
- Contract: Single floating-point number, minimum phonon frequency in THz. A positive value indicates dynamical stability (no imaginary modes).
- Scoring: scored by hidden verifier

### Step 5: Compute electronic band gap of cI24
- Role: scored
- Action: Compute the electronic band structure of the optimized cI24 structure using DFT with a suitable hybrid functional (e.g., HSE06) and determine the band gap (in eV). Write the gap to the output file.
- Output file: `/app/outputs/cI24_band_gap.txt`
- Format: txt
- Contract: Single floating-point number, electronic band gap in eV. A value of 0.0 indicates metallic behavior.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/cI24_lattice_parameter.txt`
- `/app/outputs/enthalpy_difference.txt`
- `/app/outputs/cI24_phonon_min_freq.txt`
- `/app/outputs/cI24_band_gap.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### cI24_lattice_parameter.txt
- path: `/app/outputs/cI24_lattice_parameter.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Optimized lattice parameter a of the cI24 sodium phase at 16 TPa.
- schema:
  - `type`: text
  - `content`: single floating-point number
  - `units`: angstrom

### enthalpy_difference.txt
- path: `/app/outputs/enthalpy_difference.txt`
- format: txt
- purpose: scored
- target_policy: threshold_or_better
- description: Enthalpy difference per atom between cI24 and oP8 at 16 TPa.
- schema:
  - `type`: text
  - `content`: single floating-point number
  - `units`: eV/atom
  - `threshold_condition`: must be negative (cI24 more stable)

### cI24_phonon_min_freq.txt
- path: `/app/outputs/cI24_phonon_min_freq.txt`
- format: txt
- purpose: scored
- target_policy: threshold_or_better
- description: Minimum phonon frequency of cI24 at 16 TPa, indicating dynamical stability.
- schema:
  - `type`: text
  - `content`: single floating-point number
  - `units`: THz
  - `threshold_condition`: must be positive (no imaginary modes)

### cI24_band_gap.txt
- path: `/app/outputs/cI24_band_gap.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Electronic band gap of cI24 at 16 TPa.
- schema:
  - `type`: text
  - `content`: single floating-point number
  - `units`: eV

Notes: All values must be obtained from the same consistent DFT setup and temperature=0 K. The checker compares the reported numbers to the paper's reference results with tolerances that absorb legitimate methodological spread. No further intermediate artifacts are scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "cI24_lattice_parameter.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "content": "single floating-point number",
        "units": "angstrom"
      },
      "description": "Optimized lattice parameter a of the cI24 sodium phase at 16 TPa."
    },
    {
      "file": "enthalpy_difference.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "text",
        "content": "single floating-point number",
        "units": "eV/atom",
        "threshold_condition": "must be negative (cI24 more stable)"
      },
      "description": "Enthalpy difference per atom between cI24 and oP8 at 16 TPa."
    },
    {
      "file": "cI24_phonon_min_freq.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "text",
        "content": "single floating-point number",
        "units": "THz",
        "threshold_condition": "must be positive (no imaginary modes)"
      },
      "description": "Minimum phonon frequency of cI24 at 16 TPa, indicating dynamical stability."
    },
    {
      "file": "cI24_band_gap.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "content": "single floating-point number",
        "units": "eV"
      },
      "description": "Electronic band gap of cI24 at 16 TPa."
    }
  ],
  "notes": "All values must be obtained from the same consistent DFT setup and temperature=0 K. The checker compares the reported numbers to the paper's reference results with tolerances that absorb legitimate methodological spread. No further intermediate artifacts are scored."
}
```

## How you are scored
A hidden verifier reads each scored output file and compares your reported values to predetermined reference values. The comparison uses tolerances that account for legitimate methodological spread between different DFT implementations, numerical settings, and pseudopotentials. Each output is scored independently, and the final score is a weighted combination of all scored outputs. The verifier does not re‑run the first‑principles calculations; it only checks the numbers you write to the output files. An honest reproduction that follows the described workflow should produce values within the accepted range.

# DFT electronic structure of pure and Ti-doped zinc aluminate

## Problem background
Zinc aluminate (ZnAl2O4) is a wide-band-gap semiconductor with a normal spinel crystal structure. It is stable under ion bombardment and transparent to visible light, making it attractive for UV optoelectronics and luminescent devices. Doping with Ti⁴⁺ ions is reported to introduce mid-gap electronic states that dramatically reduce the effective band gap, enabling blue photoluminescence. Density functional theory (DFT) calculations can predict these electronic structure changes. This task focuses on recomputing the direct band gap of pure ZnAl2O4 and the density of states effects of Ti doping using the open‑source GPAW code, thereby verifying the computational predictions that underlie the material's optical properties.

## Approach
The electronic structure is computed using the grid‑based projector‑augmented‑wave (PAW) method as implemented in GPAW, driven through the ASE interface. The workflow first builds the pure ZnAl2O4 conventional cell from known crystallographic data (normal spinel, space group Fd‑3m, 56 atoms) and relaxes the geometry with a meta‑GGA functional. From the optimized structure, the Kohn‑Sham eigenvalues are obtained and the direct band gap is extracted as the smallest energy difference between the highest occupied and lowest unoccupied state at the same k‑point. For the doped case, a 56‑atom supercell is constructed where two aluminium atoms are replaced by one titanium and one zinc (1.8 at.% doping) and the geometry is relaxed analogously. A non‑spin‑polarized total density of states (DOS) calculation is then performed. The effective band gap is defined as the minimal energy separation between occupied and empty states, and the presence of a distinct mid‑gap peak is determined from the DOS. This approach directly parallels the computational strategy used in the original study, isolating the GPAW‑based electronic structure component.

## Reproduction target
Compute and report the direct band gap of pure ZnAl2O4 in the file `pure_bandgap.json`. Additionally, for the Ti‑doped supercell, compute and report the effective band gap and a Boolean indicator of whether a distinct mid‑gap peak appears in the total DOS, saving the results in `doped_analysis.json`. Both files must conform to the prescribed JSON schemas and be written to the `/app/outputs` directory.

## Assets

- GPAW: gpaw
- ASE: ase

## Workflow steps

### Step 1: Prepare pure ZnAl2O4 structure
- Role: process
- Action: Construct the conventional unit cell of ZnAl2O4 (normal spinel, space group Fd-3m) with lattice parameter a=8.0854 Å and oxygen fractional coordinate u=0.2644, yielding 56 atoms. This structure will be used for subsequent geometry optimization.
- Evidence: none

### Step 2: Geometry optimization of pure ZnAl2O4
- Role: process
- Action: Optimize atomic positions of the pure ZnAl2O4 structure using GPAW with a meta-GGA functional, real-space grid spacing 0.2 Å, 4x4x4 Monkhorst-Pack k-point mesh, and force convergence threshold 0.05 eV/Å. Use the ASE BFGS optimizer.
- Evidence: `/app/outputs/pure_opt.log`

### Step 3: Compute direct band gap of pure ZnAl2O4
- Role: scored
- Action: Perform a non-spin-polarized GPAW calculation using the optimized pure structure to obtain Kohn-Sham eigenvalues, then compute the direct band gap (minimum energy difference between the highest occupied and lowest unoccupied states at the same k-point). Report the result in pure_bandgap.json.
- Output file: `/app/outputs/pure_bandgap.json`
- Format: json
- Contract: {"direct_band_gap_eV": <float>}
- Scoring: scored by hidden verifier

### Step 4: Construct Ti-doped ZnAl2O4 supercell
- Role: process
- Action: Create a 56-atom conventional supercell of ZnAl2O4 and replace two Al atoms with one Ti and one Zn, ensuring the two substituted Al sites are separated by a single Al atom. This models 1.8 at.% Ti doping. Use atomic positions from the optimized pure structure as a starting point.
- Evidence: `/app/outputs/doped_structure.xyz`

### Step 5: Geometry optimization of Ti-doped ZnAl2O4
- Role: process
- Action: Optimize atomic positions of the doped supercell using GPAW with the same meta-GGA settings as for the pure case (grid spacing 0.2 Å, 4x4x4 k-points, BFGS optimizer, force convergence < 0.05 eV/Å).
- Evidence: `/app/outputs/doped_opt.log`

### Step 6: Compute DOS and effective gap for Ti-doped ZnAl2O4
- Role: scored (load-bearing)
- Action: Using the optimized doped supercell, perform a non-spin-polarized GPAW calculation to obtain the total density of states (DOS). Determine the effective band gap (minimal energy separation between occupied and empty states accounting for any mid-gap states) and detect whether a distinct mid-gap peak is present. Report effective_gap_eV (float) and mid_gap_peak_present (true/false) in doped_analysis.json.
- Output file: `/app/outputs/doped_analysis.json`
- Format: json
- Contract: {"effective_gap_eV": <float>, "mid_gap_peak_present": <bool>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/pure_bandgap.json`
- `/app/outputs/doped_analysis.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### pure_bandgap.json
- path: `/app/outputs/pure_bandgap.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The agent's computed direct band gap of the pure ZnAl2O4 host. Checker compares the value to the paper-reported hidden gold within a tolerance.
- schema:
  - `type`: object
  - `required`:
    - `direct_band_gap_eV`: number (float)
  - `items`: object
  - `required_columns`:
  - `units`:
    - `direct_band_gap_eV`: eV

### doped_analysis.json
- path: `/app/outputs/doped_analysis.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The agent's computed effective band gap and mid-gap peak presence for the Ti-doped ZnAl2O4 supercell. Checker compares the effective_gap_eV to the hidden reference within tolerance and verifies mid_gap_peak_present is true.
- schema:
  - `type`: object
  - `required`:
    - `effective_gap_eV`: number (float)
    - `mid_gap_peak_present`: boolean
  - `items`: object
  - `required_columns`:
  - `units`:
    - `effective_gap_eV`: eV

Notes: The task omits lattice dynamics (phonon) calculations and comparison with Raman/infrared spectra because the primary code (CRYSTAL09) is not fully open-source and validation requires experimental data. Only GPAW-based electronic structure computations (band gap, density of states) are reproduced.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "pure_bandgap.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "direct_band_gap_eV": "number (float)"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "direct_band_gap_eV": "eV"
        }
      },
      "description": "The agent's computed direct band gap of the pure ZnAl2O4 host. Checker compares the value to the paper-reported hidden gold within a tolerance."
    },
    {
      "file": "doped_analysis.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "effective_gap_eV": "number (float)",
          "mid_gap_peak_present": "boolean"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "effective_gap_eV": "eV"
        }
      },
      "description": "The agent's computed effective band gap and mid-gap peak presence for the Ti-doped ZnAl2O4 supercell. Checker compares the effective_gap_eV to the hidden reference within tolerance and verifies mid_gap_peak_present is true."
    }
  ],
  "notes": "The task omits lattice dynamics (phonon) calculations and comparison with Raman/infrared spectra because the primary code (CRYSTAL09) is not fully open-source and validation requires experimental data. Only GPAW-based electronic structure computations (band gap, density of states) are reproduced."
}
```

## How you are scored
A hidden verifier examines each scored output artifact independently. For `pure_bandgap.json`, the reported direct band gap is compared to a hidden reference value with a tolerance that accounts for typical DFT implementation variations. For `doped_analysis.json`, the effective gap is checked against a hidden reference and the `mid_gap_peak_present` flag is verified against the expected structural feature. The verifier computes a partial reward for each artifact and combines them into an overall score between 0 and 1. Outputs that fail basic format validation receive zero credit; the total reward reflects how closely the computed metrics reproduce the expected electronic behaviour. Successful reproduction requires genuinely running the DFT calculations — reporting isolated numbers is not sufficient.

# Photocatalytic Water Splitting Band Edge Assessment

## Problem background
Traditional photocatalytic water splitting requires a semiconductor with a band gap larger than 1.23 eV, the thermodynamic difference between the water reduction and oxidation potentials. This restriction prevents the utilization of the infrared portion of the solar spectrum, which carries nearly half of the sun’s energy. A recent proposal suggests a new mechanism: an intrinsic dipole in a nanoscale junction produces an internal electric field and a surface potential difference ΔΦ, effectively lowering the band-gap requirement to about 1.23 eV – ΔΦ and enabling near-infrared-driven hydrogen production. The concept was illustrated on a surface-functionalized hexagonal boron-nitride bilayer, F-BNBN-H. This task investigates that candidate material by computing its key electronic and optical properties from first principles.

## Approach
The core idea is to verify that the F-BNBN-H bilayer indeed exhibits the electronic features required by the proposed photocatalytic model. You will perform density-functional theory (DFT) calculations using an open-source code that supports hybrid functionals. The workflow involves (i) geometry relaxation of the AB-stacked fluorinated/hydrogenated BN bilayer, (ii) an HSE06 hybrid-functional calculation to obtain the accurate band structure and band gap, (iii) extraction of the planar-averaged electrostatic potential to determine the surface potential difference ΔΦ, (iv) computation of the frequency-dependent dielectric function and optical absorption to locate the main low-energy absorption peak, and (v) alignment of the valence-band maximum (VBM) and conduction-band minimum (CBM) with respect to the vacuum level. These results are then compared against the standard water redox potentials to judge thermodynamic feasibility.

## Reproduction target
Your objective is to compute the following quantities for F-BNBN-H and write them as plain-text files under `/app/outputs`:

1. **HSE06 electronic band gap** (`band_gap.txt`): a single floating-point number in eV.
2. **Electrostatic surface potential difference ΔΦ** (`surface_potential.txt`): a single floating-point number in eV.
3. **Energy of the main low-energy optical absorption peak** (`optical_peak.txt`): a single floating-point number in eV, reporting the peak position, not the absorption onset.
4. **Absolute band-edge energies** (`energy_alignment.txt`): two lines, each a floating-point number (eV). The first line is the VBM energy and the second the CBM energy, both referenced to vacuum (Evac = 0 eV, so the VBM is a negative number).

These numbers are to be derived from the DFT simulation chain described in the workflow steps. The verifier will independently check that the VBM lies below the O₂/H₂O oxidation potential (5.67 eV below vacuum) and the CBM lies above the H⁺/H₂ reduction potential (4.44 eV below vacuum).

## Assets

- Open-source DFT code with hybrid functional support (e.g., Quantum ESPRESSO, GPAW): https://www.quantum-espresso.org/
- Python with numpy, scipy, and matplotlib: numpy scipy matplotlib
- Standard pseudopotential library (e.g., PseudoDojo, SSSP, GBRV): https://www.quantum-espresso.org/pseudopotentials/

## Workflow steps

### Step 1: Geometry relaxation of F-BNBN-H bilayer
- Role: process
- Action: Build the atomic structure of the AB-stacked fluorinated/hydrogenated BN bilayer (F-BNBN-H) and perform geometry optimization using the PBE functional with van der Waals corrections. Relax both lattice constants and atomic positions until forces are converged.
- Evidence: `/app/outputs/relaxed_structure.xyz`

### Step 2: HSE06 electronic band structure and band gap
- Role: scored (load-bearing)
- Action: Using the relaxed geometry from the previous step, perform a single-point HSE06 calculation to obtain the electronic band structure. Extract the band gap (CBM minus VBM) in eV and write it to a plain-text file. The file must contain a single floating-point number with unit eV (implicit).
- Output file: `/app/outputs/band_gap.txt`
- Format: txt
- Contract: A single line containing a floating-point number. Units eV.
- Scoring: scored by hidden verifier

### Step 3: Electrostatic surface potential difference
- Role: scored
- Action: From the self-consistent HSE06 calculation, compute the planar-averaged electrostatic potential along the direction normal to the bilayer. Determine the potential difference ΔΦ between the two outer surfaces (the (00 1̅) and (001) faces) and write the value in eV to a plain-text file.
- Output file: `/app/outputs/surface_potential.txt`
- Format: txt
- Contract: A single line containing a floating-point number. Units eV.
- Scoring: scored by hidden verifier

### Step 4: Optical absorption peak energy
- Role: scored
- Action: Using the HSE06 wavefunctions, compute the frequency-dependent imaginary part of the dielectric function and the optical absorption coefficients. Identify the energy of the main low-energy absorption peak (the peak closest to the band gap) and write this energy in eV to a plain-text file. Report the peak energy, not the onset.
- Output file: `/app/outputs/optical_peak.txt`
- Format: txt
- Contract: A single line containing a floating-point number. Units eV.
- Scoring: scored by hidden verifier

### Step 5: Band-edge alignment with water redox potentials
- Role: scored
- Action: Determine the absolute energies of the valence-band maximum (VBM) and conduction-band minimum (CBM) with respect to the vacuum level from the HSE06 calculation (using the same vacuum reference as the electrostatic potential). Write two lines: the VBM energy (eV) and the CBM energy (eV), both with the convention E_vacuum = 0 eV. The checker will verify alignment against the standard water redox potentials (O₂/H₂O oxidation potential at 5.67 eV below vacuum, H⁺/H₂ reduction potential at 4.44 eV below vacuum).
- Output file: `/app/outputs/energy_alignment.txt`
- Format: txt
- Contract: Two lines, each a floating-point number: first line = VBM energy (eV, negative), second line = CBM energy (eV, negative or positive depending on convention).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gap.txt`
- `/app/outputs/surface_potential.txt`
- `/app/outputs/optical_peak.txt`
- `/app/outputs/energy_alignment.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gap.txt
- path: `/app/outputs/band_gap.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: HSE06 electronic band gap of F-BNBN-H, a single floating-point number.
- schema:
  - `type`: text
  - `lines`: 1
  - `units`: eV

### surface_potential.txt
- path: `/app/outputs/surface_potential.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Electrostatic potential difference ΔΦ between the two surfaces, a single floating-point number.
- schema:
  - `type`: text
  - `lines`: 1
  - `units`: eV

### optical_peak.txt
- path: `/app/outputs/optical_peak.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Energy of the main low-energy optical absorption peak, a single floating-point number.
- schema:
  - `type`: text
  - `lines`: 1
  - `units`: eV

### energy_alignment.txt
- path: `/app/outputs/energy_alignment.txt`
- format: txt
- purpose: scored
- target_policy: threshold_or_better
- description: Absolute band-edge energies (VBM, CBM) relative to vacuum level. Verifier checks that VBM < -5.67 eV and CBM > -4.44 eV.
- schema:
  - `type`: text
  - `lines`: 2
  - `order`: `vbm_energy`, `cbm_energy`
  - `units`: eV
  - `description`: First line = VBM energy (eV, negative relative to vacuum), second line = CBM energy (eV).

Notes: Tolerances for exact_match values are set to accommodate legitimate spread from using an open-source DFT code and standard pseudopotentials instead of VASP. The energy_alignment output is checked via threshold_or_better against standard redox potentials.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gap.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "lines": 1,
        "units": "eV"
      },
      "description": "HSE06 electronic band gap of F-BNBN-H, a single floating-point number."
    },
    {
      "file": "surface_potential.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "lines": 1,
        "units": "eV"
      },
      "description": "Electrostatic potential difference ΔΦ between the two surfaces, a single floating-point number."
    },
    {
      "file": "optical_peak.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "lines": 1,
        "units": "eV"
      },
      "description": "Energy of the main low-energy optical absorption peak, a single floating-point number."
    },
    {
      "file": "energy_alignment.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "text",
        "lines": 2,
        "order": [
          "vbm_energy",
          "cbm_energy"
        ],
        "units": "eV",
        "description": "First line = VBM energy (eV, negative relative to vacuum), second line = CBM energy (eV)."
      },
      "description": "Absolute band-edge energies (VBM, CBM) relative to vacuum level. Verifier checks that VBM < -5.67 eV and CBM > -4.44 eV."
    }
  ],
  "notes": "Tolerances for exact_match values are set to accommodate legitimate spread from using an open-source DFT code and standard pseudopotentials instead of VASP. The energy_alignment output is checked via threshold_or_better against standard redox potentials."
}
```

## How you are scored
Your submission is evaluated by an automated verifier that reads each scored output file and compares its content to a hidden gold standard derived from the published DFT results for this system. The verifier computes a per-file score (0–1) and combines them into a weighted total reward.

- For `band_gap.txt`, `surface_potential.txt`, and `optical_peak.txt`, the verifier checks whether your computed value falls within a predefined tolerance of the expected value. The tolerance accounts for the legitimate spread introduced by using different DFT codes, pseudopotentials, and numerical settings.
- For `energy_alignment.txt`, the verifier extracts the VBM and CBM values and verifies that the VBM is below the O₂/H₂O oxidation potential (5.67 eV below vacuum) and that the CBM is above the H⁺/H₂ reduction potential (4.44 eV below vacuum). Meeting or exceeding these thresholds earns full credit; a result that is close but fails the alignment condition receives partial credit proportional to how far it is from satisfying the thresholds.

The reward is designed to reward faithful reproduction of the physical quantities, not merely matching a known number. Simply reporting the paper’s published values without performing the computations will fail, because the hidden tolerances are tight enough to distinguish a real DFT re-run from a guess.

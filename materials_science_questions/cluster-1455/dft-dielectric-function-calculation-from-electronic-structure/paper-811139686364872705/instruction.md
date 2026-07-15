# Si46 clathrate band gap and optical absorption under biaxial strain

## Problem background
Type-I guest-free silicon clathrate Si46 is a promising material for optoelectronics and photovoltaics, but its electronic band gap is indirect, limiting light absorption. Theoretical studies suggest that applying mechanical strain can modify the band structure and potentially convert the gap to direct, thereby enhancing optical performance. This work investigates how biaxial strain (compressive or tensile) affects the electronic properties and optical absorption of Si46 using first-principles density-functional theory. The key challenges are to determine for each strain level the band gap magnitude, whether the gap is direct or indirect, and whether the absorption in the visible range is improved relative to the unstrained material.

## Approach
The core idea is to simulate the effect of biaxial strain on a Si46 crystal using plane-wave DFT with the GGA-PBE exchange-correlation functional. Strain is applied by fixing the in-plane lattice parameters to values corresponding to a desired strain percentage while leaving the out-of-plane axis and internal coordinates free to relax. For each strained configuration, the electronic band structure is computed along a high-symmetry path in the Brillouin zone, and the valence band maximum (VBM) and conduction band minimum (CBM) are located to determine the band gap energy and whether it is direct or indirect. The optical absorption coefficient is then derived from the imaginary part of the dielectric function, which is obtained via momentum matrix elements and Kramers-Kronig transformation. The workflow proceeds from geometry optimization of the unstrained cell, through relaxation of a series of strained structures, to band gap extraction and finally optical spectra calculation for the most relevant strain states. All calculations use open-source tools, in particular Quantum ESPRESSO for DFT, with a publicly available GGA-PBE pseudopotential for silicon.

## Reproduction target
Using DFT with the GGA-PBE functional, compute the electronic band gap energy and its type (direct or indirect) for a type-I Si46 crystal under nine biaxial strain levels: -4%, -3%, -2%, -1%, 0%, +1%, +2%, +3%, and +4%. Record these results in a CSV file. Additionally, for the unstrained (0%) and the +4% tensile-strained configurations, calculate the optical absorption coefficient as a function of photon energy over the visible range (1–4 eV) and save the spectra in a second CSV file. From these spectra, verify that the absorption in the visible range is enhanced under +4% tensile strain relative to the unstrained case.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Si pseudopotential: https://www.materialscloud.org/discover/sssp/table/efficiency
- pymatgen: pymatgen
- numpy: numpy

## Workflow steps

### Step 1: Geometry optimization of unstrained Si46
- Role: process
- Action: Construct the Si46 crystal structure (space group Pm-3n, lattice constant approximately 10.1 Å, 46 Si atoms at Wyckoff positions). Perform a full variable-cell geometry optimization (lattice parameter and atomic coordinates) using DFT with the GGA-PBE functional and a suitable pseudopotential. Achieve force convergence at a reasonable threshold. Save the optimized structure in CIF format.
- Evidence: `/app/outputs/si46_relaxed.cif`

### Step 2: Strained structures relaxation series
- Role: process
- Action: For biaxial strain levels from -4% to +4% in 1% steps, apply in-plane strain by setting lattice parameters a = b = a0(1+ε) while keeping the out-of-plane axis c free. Relax the out-of-plane lattice parameter and internal coordinates using the same DFT settings as step0. Save the relaxed structure for each strain level.
- Evidence: none

### Step 3: Band structures and band gaps for all strains
- Role: scored (load-bearing)
- Action: For each relaxed structure from step1, compute electronic band structure along a high-symmetry path in the Brillouin zone using GGA-PBE DFT. Determine the valence band maximum and conduction band minimum k-points, compute the band gap energy (eV), and classify the gap as direct or indirect. Save one row per strain in band_gaps.csv.
- Output file: `/app/outputs/band_gaps.csv`
- Format: csv
- Contract: columns: strain_percent (float), bandgap_eV (float), bandgap_type (string: 'indirect' or 'direct'). One row per strain.
- Scoring: scored by hidden verifier

### Step 4: Optical absorption spectra for selected strains
- Role: scored
- Action: For the unstrained (0%) and +4% tensile strained structures, compute the imaginary part of the dielectric function using a denser k-point grid. Derive the absorption coefficient as a function of energy over the visible range (1–4 eV). Save CSV with energy (eV) and absorption coefficient (cm⁻¹) for strain=0 and strain=p4.
- Output file: `/app/outputs/absorption_data.csv`
- Format: csv
- Contract: columns: strain (string: '0' or 'p4'), energy_eV (float), absorption_cm-1 (float). Multiple rows covering 1–4 eV.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gaps.csv`
- `/app/outputs/absorption_data.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gaps.csv
- path: `/app/outputs/band_gaps.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Band gap energies and types for biaxial strain from -4% to +4%.
- schema:
  - `type`: table
  - `required_columns`: `strain_percent`, `bandgap_eV`, `bandgap_type`
  - `units`:
    - `bandgap_eV`: eV
    - `strain_percent`: percent

### absorption_data.csv
- path: `/app/outputs/absorption_data.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Absorption coefficient spectra for unstrained (0%) and +4% tensile strained Si46 in the visible range.
- schema:
  - `type`: table
  - `required_columns`: `strain`, `energy_eV`, `absorption_cm-1`
  - `units`:
    - `energy_eV`: eV
    - `absorption_cm-1`: cm^-1

Notes: Only GGA-PBE functional is used. The agent should use open-source DFT code (Quantum ESPRESSO) and publicly available pseudopotentials. Computations may be performed on external compute resources if needed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gaps.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain_percent",
          "bandgap_eV",
          "bandgap_type"
        ],
        "units": {
          "bandgap_eV": "eV",
          "strain_percent": "percent"
        }
      },
      "description": "Band gap energies and types for biaxial strain from -4% to +4%."
    },
    {
      "file": "absorption_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain",
          "energy_eV",
          "absorption_cm-1"
        ],
        "units": {
          "energy_eV": "eV",
          "absorption_cm-1": "cm^-1"
        }
      },
      "description": "Absorption coefficient spectra for unstrained (0%) and +4% tensile strained Si46 in the visible range."
    }
  ],
  "notes": "Only GGA-PBE functional is used. The agent should use open-source DFT code (Quantum ESPRESSO) and publicly available pseudopotentials. Computations may be performed on external compute resources if needed."
}
```

## How you are scored
Your solution is evaluated by a hidden verifier that independently examines each output artifact. The verifier compares your computed band gap energies and types against reference values, and it assesses the optical absorption spectra by checking the relative enhancement between the unstrained and +4% strained cases. The overall reward is a weighted combination of the scores for the band gaps and the absorption data. Submitting manually looked‑up numbers or copying values from a reference will not succeed; you must perform the DFT calculations and produce the requested files to earn credit.

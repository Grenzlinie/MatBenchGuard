# Photocatalytic Water Splitting Band Edge Assessment of a 2D Heterostructure

## Problem background
The development of efficient photocatalysts for overall water splitting under visible light is a critical step toward sustainable hydrogen production. Most existing semiconductor materials suffer from wide band gaps, poor charge separation, or low carrier mobilities. Two-dimensional (2D) materials offer opportunities to engineer van der Waals heterostructures with tailored properties. This work investigates a heterostructure formed by stacking an InSe monolayer on top of a Zr₂CO₂ monolayer. The central goal is to compute the key photocatalytic properties of this InSe/Zr₂CO₂ heterostructure, including its band gap, band edge alignment, optical absorption, carrier mobilities, and its ability to straddle the water redox potentials, thereby assessing its viability as a visible-light photocatalyst.

## Approach
A first-principles model based on density functional theory (DFT) extended with van der Waals corrections and a band-gap-corrected hybrid functional (e.g., HSE06) is employed. The heterostructure is built from published monolayer structures, and geometry optimization yields the equilibrium interlayer distance. The electronic structure is analyzed by computing the projected band structure and density of states to determine whether the band gap is direct or indirect and to classify the band alignment type. Optical absorption is derived from the frequency-dependent dielectric function, using a scissors shift to correct the band gap; this yields the absorption coefficient in the visible range and the absorption edge. Carrier effective masses are extracted from band dispersions, while deformation potentials and in-plane stiffness are computed under applied uniaxial strains, enabling the calculation of electron and hole mobilities at room temperature via the deformation potential model. Finally, the electrostatic potential gives the vacuum level, which together with the corrected band gap allows alignment of the conduction and valence band edges to vacuum and then to the standard hydrogen electrode; from these, the overpotentials for water reduction and oxidation are obtained. All computed properties are compiled into a single JSON artifact.

## Reproduction target
Produce a JSON file named `heterostructure_properties.json` in `/app/outputs/`. This file must contain the following computed quantities for the InSe/Zr₂CO₂ heterostructure:
- `band_gap_direct`: the direct band gap energy (eV)
- `cbm_energy` and `vbm_energy`: the conduction band minimum and valence band maximum energies relative to vacuum (eV)
- `reducing_capacity`: the energy difference between the hydrogen reduction potential and the CBM (eV vs H⁺/H₂)
- `oxidizing_ability`: the energy difference between the VBM and the oxygen evolution potential (eV vs O₂/H₂O)
- `electron_mobility_x`, `electron_mobility_y`, `hole_mobility_x`, `hole_mobility_y`: electron and hole mobilities along two orthogonal directions (cm²/V·s)
- `absorption_coefficient_visible`: the optical absorption coefficient at a photon energy of approximately 2.75 eV (cm⁻¹)
- `alignment_type`: a string exactly equal to `'type-I'` or `'type-II'`
- `absorption_edge`: the onset energy of significant optical absorption (eV)
All values must be derived from the DFT simulations; you must run the full computational pipeline, not look up pre-computed numbers.

## Assets

- InSe monolayer crystal structure: 10.1021/cm401239h
- Zr2CO2 monolayer crystal structure: 10.1039/C6TA03508G
- Open-source DFT code: https://www.quantum-espresso.org/download/
- Mobility calculation implementation

## Workflow steps

### Step 1: Structure setup and geometry optimization
- Role: process
- Action: Construct initial structures for InSe monolayer, Zr2CO2 monolayer, and the heterostructure supercell (3x3 InSe on √13×√13 Zr2CO2, initial interlayer distance ~3.2 Å) using published lattice constants. Perform DFT structural relaxation with a van der Waals corrected functional to obtain equilibrium geometries, interlayer separation, and total energies.
- Evidence: `/app/outputs/relaxed_structures.json`

### Step 2: Electronic structure calculation
- Role: process
- Action: Using the optimized geometries, compute the band structure and projected density of states for the heterostructure with a suitable band-gap-corrected functional (e.g., HSE06). Determine the direct/indirect character of the band gap at Γ point and determine the band alignment type (type-I or type-II) based on the projected band structure and DOS.
- Evidence: `/app/outputs/band_structure.json`

### Step 3: Optical absorption calculation
- Role: process
- Action: Compute the imaginary part of the dielectric function and derive the optical absorption coefficient spectrum using the Kramers-Kronig relation. Apply a scissors shift to match the corrected band gap from step_02. Extract the absorption coefficient at a photon energy of approximately 2.75 eV and estimate the absorption edge.
- Evidence: `/app/outputs/absorption_spectrum.csv`

### Step 4: Carrier mobility calculation
- Role: process
- Action: From the band structure, determine effective masses of electrons and holes along zigzag (x) and armchair (y) directions. Apply small uniaxial strains (±1%) to compute deformation potentials for CBM and VBM. Calculate the in-plane stiffness from total energy vs strain, then compute electron and hole mobilities using the deformation potential formula at 300 K.
- Evidence: `/app/outputs/mobility_parameters.json`

### Step 5: Band edge positioning
- Role: process
- Action: Compute the planar-averaged electrostatic potential to obtain vacuum level. Use the PBE band gap center and the corrected band gap to align CBM and VBM to vacuum, then convert to energies relative to the standard hydrogen electrode (SHE) using E(vs SHE) = -E(vs vacuum) - 4.44 eV. Determine the reducing capacity (E(H⁺/H₂) - E(CBM)) and oxidizing ability (E(VBM) - E(O₂/H₂O)).
- Evidence: `/app/outputs/electrostatic_potential.dat`

### Step 6: Compile heterostructure photocatalytic properties
- Role: scored (load-bearing)
- Action: Aggregate all previously computed quantities into a single JSON file. The file must contain: direct band gap (eV), CBM and VBM energies vs vacuum (eV), reducing capacity (eV vs H⁺/H₂), oxidizing ability (eV vs O₂/H₂O), electron mobilities along x and y (cm²/V·s), hole mobilities along x and y (cm²/V·s), absorption coefficient at ~2.75 eV (cm⁻¹), band alignment type (string 'type-II'), and absorption edge energy (eV).
- Output file: `/app/outputs/heterostructure_properties.json`
- Format: json
- Contract: JSON object with keys: band_gap_direct (number, eV), cbm_energy (number, eV vs vacuum), vbm_energy (number, eV vs vacuum), reducing_capacity (number, eV vs H+/H2), oxidizing_ability (number, eV vs O2/H2O), electron_mobility_x (number, cm2/Vs), electron_mobility_y (number, cm2/Vs), hole_mobility_x (number, cm2/Vs), hole_mobility_y (number, cm2/Vs), absorption_coefficient_visible (number, cm-1 at ~2.75 eV), alignment_type (string, e.g., 'type-I' or 'type-II'), absorption_edge (number, eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/heterostructure_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### heterostructure_properties.json
- path: `/app/outputs/heterostructure_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Compilation of the key photocatalytic properties of the InSe/Zr2CO2 heterostructure computed by DFT, including band gap, band alignment, band edge positions, overpotentials, carrier mobilities, and optical absorption.
- schema:
  - `type`: object
  - `required`:
    - `band_gap_direct`: number (eV)
    - `cbm_energy`: number (eV vs vacuum)
    - `vbm_energy`: number (eV vs vacuum)
    - `reducing_capacity`: number (eV vs H+/H2)
    - `oxidizing_ability`: number (eV vs O2/H2O)
    - `electron_mobility_x`: number (cm2/Vs)
    - `electron_mobility_y`: number (cm2/Vs)
    - `hole_mobility_x`: number (cm2/Vs)
    - `hole_mobility_y`: number (cm2/Vs)
    - `absorption_coefficient_visible`: number (cm-1 at ~2.75 eV)
    - `alignment_type`: string (e.g., 'type-I' or 'type-II')
    - `absorption_edge`: number (eV)

Notes: The artifact reports computed values from the DFT workflow. The hidden checker compares each field to a gold reference with appropriate tolerances. No gold values or tolerances are disclosed here.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "heterostructure_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "band_gap_direct": "number (eV)",
          "cbm_energy": "number (eV vs vacuum)",
          "vbm_energy": "number (eV vs vacuum)",
          "reducing_capacity": "number (eV vs H+/H2)",
          "oxidizing_ability": "number (eV vs O2/H2O)",
          "electron_mobility_x": "number (cm2/Vs)",
          "electron_mobility_y": "number (cm2/Vs)",
          "hole_mobility_x": "number (cm2/Vs)",
          "hole_mobility_y": "number (cm2/Vs)",
          "absorption_coefficient_visible": "number (cm-1 at ~2.75 eV)",
          "alignment_type": "string (e.g., 'type-I' or 'type-II')",
          "absorption_edge": "number (eV)"
        }
      },
      "description": "Compilation of the key photocatalytic properties of the InSe/Zr2CO2 heterostructure computed by DFT, including band gap, band alignment, band edge positions, overpotentials, carrier mobilities, and optical absorption."
    }
  ],
  "notes": "The artifact reports computed values from the DFT workflow. The hidden checker compares each field to a gold reference with appropriate tolerances. No gold values or tolerances are disclosed here."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that reads `heterostructure_properties.json`. The verifier compares each property you report to reference values obtained from the original study. Each quantity is scored based on how closely it matches the reference, with predefined tolerance windows that account for the legitimate variability introduced by different code implementations and functional choices. The total reward, a floating-point number between 0 and 1, is a weighted combination of these per-property scores. The verifier does not re-run your calculations; it relies on the numbers you provide, but the benchmark assumes honest computational reproduction.

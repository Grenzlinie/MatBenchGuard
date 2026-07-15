# DFT Band Edge Assessment of 2D Materials for Photocatalytic Water Splitting

## Problem background
Two-dimensional (2D) materials are promising photocatalysts for solar water splitting due to their high specific surface area. However, single-component monolayers suffer from rapid recombination of photogenerated electron-hole pairs. Constructing van der Waals (vdW) heterostructures from two different 2D layers can separate the photogenerated charges if a type-II band alignment is achieved, with conduction band minimum (CBM) and valence band maximum (VBM) residing on different layers, and if the band edge positions straddle the water redox potentials. This task investigates whether heterostructures formed by combining monolayer arsenene (As) with monolayer gallium sulfide (GaS) or gallium selenide (GaSe) can provide such a type-II alignment and achieve high solar-to-hydrogen (STH) efficiency.

## Approach
The investigation employs density functional theory (DFT). First, the structural and electronic properties of isolated monolayers (As, GaS, GaSe) are computed: structural relaxation is performed with the PBE functional plus DFT-D3 dispersion correction, and accurate band gaps and band-character information are obtained using the HSE06 hybrid functional. Then, multiple stacking configurations of As/GaX heterostructures are constructed; their binding energies are evaluated at the PBE‑D3 level to identify the most stable stacking. For the most stable heterostructures, detailed HSE06 calculations are carried out to obtain projected band structures, projected density of states, absolute band edge energies (relative to vacuum), band offsets, and Bader charge transfer. The electrostatic potential profile across the interface yields the built-in potential drop. Optical absorption spectra are derived from the dielectric function, and the STH efficiency is calculated by integrating the AM 1.5G solar spectrum with the appropriate overpotentials for hydrogen and oxygen evolution reactions. The performance of the heterostructures is benchmarked against the constituent monolayers in terms of band alignment, light absorption, and STH efficiency. The entire workflow is designed to be executable with an open‑source DFT code, public pseudopotentials, and the standard AM 1.5G spectrum.

## Reproduction target
Compute the optimized lattice constants and nearest-neighbor bond lengths for As, GaS, and GaSe monolayers from PBE+DFT‑D3 relaxation, and determine their HSE06 band gaps (in eV) and gap character (direct or indirect). Determine the most stable stacking configuration for As/GaS and As/GaSe heterostructures by evaluating the binding energy per area for six candidate stackings, and record the interlayer distance of the most stable configuration. For each most stable heterostructure, compute: (i) the HSE06 band gap; (ii) CBM and VBM energies relative to the vacuum level; (iii) conduction band offset (CBO) and valence band offset (VBO); (iv) net Bader electron transfer from As to GaX; (v) electrostatic potential drop across the interface; and (vi) a confirmation whether the CBM is predominantly on GaX and the VBM predominantly on As (type‑II alignment). Derive optical absorption spectra for the monolayers and heterostructures, and record characteristic peak wavelengths and intensities. Using the obtained band gaps, the AM 1.5G solar spectrum, and standard overpotentials (0.2 eV for HER, 0.6 eV for OER), calculate the light absorption efficiency (η_abs), carrier utilization (η_cu), and solar‑to‑hydrogen efficiency (η_STH) for all five systems. Collect all results in the three JSON files: `monolayer_properties.json`, `heterostructure_properties.json`, and `st_hydrogen_efficiency.json`.

## Assets

- Open-source DFT code with HSE06 support (e.g., Quantum ESPRESSO, GPAW, CP2K)
- PAW pseudopotentials for As, Ga, S, Se: https://www.materialscloud.org/discover/sssp
- AM 1.5G solar spectral irradiance data: https://www.nrel.gov/grid/solar-resource/spectra.html
- Python scientific stack (numpy, scipy, matplotlib, ase or pymatgen, etc.): numpy scipy matplotlib ase pymatgen

## Workflow steps

### Step 1: Monolayer geometry optimization
- Role: process
- Action: Perform PBE+DFT-D3 structural relaxation for the isolated monolayers As, GaS, and GaSe using a plane-wave cutoff of 450 eV, a Monkhorst-Pack 11×11×1 k-point grid, a vacuum spacing ≥ 25 Å, and force convergence of 0.01 eV/Å. Keep the optimized lattice constants, bond lengths, and total energies for each monolayer.
- Evidence: `/app/outputs/monolayer_relax.log`

### Step 2: Monolayer HSE06 band structures
- Role: process
- Action: Using the optimized monolayer structures, run single-point HSE06 calculations to compute the band structures, bandgaps, and determine the band-gap character (direct/indirect).
- Evidence: `/app/outputs/monolayer_hse.log`

### Step 3: Compile monolayer properties
- Role: scored (load-bearing)
- Action: From the results of the monolayer optimizations and HSE06 calculations, extract and write the lattice constant, nearest-neighbor bond length, HSE06 bandgap, and band-gap type (direct/indirect) for each monolayer into a single JSON file.
- Output file: `/app/outputs/monolayer_properties.json`
- Format: json
- Contract: A JSON object with keys 'As', 'GaS', 'GaSe'. Each value is an object with keys: 'lattice_constant_A' (float, Å), 'bond_length_A' (float, Å), 'bandgap_eV' (float, eV), 'gap_type' (string, one of 'indirect' or 'direct').
- Scoring: scored by hidden verifier

### Step 4: Heterostructure stacking and binding energy
- Role: process
- Action: Construct the six stacking configurations (G‑I to G‑VI) for As/GaS and As/GaSe using the optimized monolayers. For each stacking, perform a PBE+DFT‑D3 energy calculation (same cutoff and k-point mesh) to obtain the total energy. Compute the binding energy per area and identify the most stable configuration (lowest Eb). Record the interlayer distance of the most stable heterostructure.
- Evidence: `/app/outputs/binding_energy_calc.log`

### Step 5: Heterostructure electronic structure (type-II)
- Role: process
- Action: For the most stable As/GaS and As/GaSe heterostructures, perform HSE06 calculations to obtain the projected band structures, projected density of states, band-decomposed charge densities at CBM/VBM, the absolute VBM and CBM energies relative to the vacuum level, the conduction band offset (CBO), valence band offset (VBO), and the heterostructure bandgap.
- Evidence: `/app/outputs/hetero_hse.log`

### Step 6: Charge transfer and potential drop
- Role: process
- Action: Compute the charge density difference, perform Bader charge analysis, and calculate the planar-averaged electrostatic potential for the most stable heterostructures. Quantify the net electron transfer from As to GaX and the potential drop across the interface.
- Evidence: `/app/outputs/charge_analysis.log`

### Step 7: Compile heterostructure properties
- Role: scored (load-bearing)
- Action: Gather data from the previous steps and write the following per heterostructure: binding energy (meV/Å²), interlayer distance (Å), HSE06 bandgap (eV), CBM energy (eV vs vacuum), VBM energy (eV vs vacuum), CBO (eV), VBO (eV), Bader electron transfer (|e|), electrostatic potential drop (eV), and a boolean confirming that CBM is mainly on GaX and VBM on As (type‑II). Save as a JSON file.
- Output file: `/app/outputs/heterostructure_properties.json`
- Format: json
- Contract: A JSON object with keys 'As/GaS' and 'As/GaSe'. Each value is an object with keys: 'binding_energy_meV_per_Ang2' (float), 'interlayer_distance_A' (float), 'bandgap_eV' (float), 'CBM_energy_eV' (float), 'VBM_energy_eV' (float), 'CBO_eV' (float), 'VBO_eV' (float), 'bader_charge_transfer_e' (float), 'potential_drop_eV' (float), 'typeII_confirmed' (boolean).
- Scoring: scored by hidden verifier

### Step 8: Optical absorption spectrum
- Role: process
- Action: For the monolayers and the most stable heterostructures, compute the frequency-dependent dielectric function from HSE06 results and derive the optical absorption coefficient α(ω) using the standard formula relating absorption to the complex dielectric function. Save the absorption spectra (wavelength and coefficient) for later use and record the near-visible-light peak positions and intensities.
- Evidence: `/app/outputs/absorption_spectra.dat`

### Step 9: Solar-to-hydrogen efficiency
- Role: scored (load-bearing)
- Action: Using the HSE06 bandgap from the heterostructure properties for each system, the AM 1.5G solar spectrum, the HER overpotential (0.2 eV) and OER overpotential (0.6 eV), compute the light absorption efficiency (η_abs), carrier utilization (η_cu), and STH efficiency (η_STH = η_abs × η_cu) according to the standard definition (photon energy integration with overpotential correction). Output a JSON with these values for the three monolayers and the two heterostructures.
- Output file: `/app/outputs/st_hydrogen_efficiency.json`
- Format: json
- Contract: A JSON object with keys 'As', 'GaS', 'GaSe', 'As/GaS', 'As/GaSe'. Each value is an object with keys: 'eta_abs' (float), 'eta_cu' (float), 'eta_STH' (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/monolayer_properties.json`
- `/app/outputs/heterostructure_properties.json`
- `/app/outputs/st_hydrogen_efficiency.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### monolayer_properties.json
- path: `/app/outputs/monolayer_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Structural and electronic properties of the isolated As, GaS, and GaSe monolayers.
- schema:
  - `type`: object
  - `required`:
    - `As`:
      - `type`: object
      - `required`:
        - `lattice_constant_A`: float
        - `bond_length_A`: float
        - `bandgap_eV`: float
        - `gap_type`: string
    - `GaS`:
      - `type`: object
      - `required`:
        - `lattice_constant_A`: float
        - `bond_length_A`: float
        - `bandgap_eV`: float
        - `gap_type`: string
    - `GaSe`:
      - `type`: object
      - `required`:
        - `lattice_constant_A`: float
        - `bond_length_A`: float
        - `bandgap_eV`: float
        - `gap_type`: string

### heterostructure_properties.json
- path: `/app/outputs/heterostructure_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Interfacial and electronic properties of the most stable As/GaS and As/GaSe vdW heterostructures.
- schema:
  - `type`: object
  - `required`:
    - `As/GaS`:
      - `type`: object
      - `required`:
        - `binding_energy_meV_per_Ang2`: float
        - `interlayer_distance_A`: float
        - `bandgap_eV`: float
        - `CBM_energy_eV`: float
        - `VBM_energy_eV`: float
        - `CBO_eV`: float
        - `VBO_eV`: float
        - `bader_charge_transfer_e`: float
        - `potential_drop_eV`: float
        - `typeII_confirmed`: boolean
    - `As/GaSe`:
      - `type`: object
      - `required`:
        - `binding_energy_meV_per_Ang2`: float
        - `interlayer_distance_A`: float
        - `bandgap_eV`: float
        - `CBM_energy_eV`: float
        - `VBM_energy_eV`: float
        - `CBO_eV`: float
        - `VBO_eV`: float
        - `bader_charge_transfer_e`: float
        - `potential_drop_eV`: float
        - `typeII_confirmed`: boolean

### st_hydrogen_efficiency.json
- path: `/app/outputs/st_hydrogen_efficiency.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Solar-to-hydrogen efficiency components and final STH efficiency for all systems.
- schema:
  - `type`: object
  - `required`:
    - `As`:
      - `type`: object
      - `required`:
        - `eta_abs`: float
        - `eta_cu`: float
        - `eta_STH`: float
    - `GaS`:
      - `type`: object
      - `required`:
        - `eta_abs`: float
        - `eta_cu`: float
        - `eta_STH`: float
    - `GaSe`:
      - `type`: object
      - `required`:
        - `eta_abs`: float
        - `eta_cu`: float
        - `eta_STH`: float
    - `As/GaS`:
      - `type`: object
      - `required`:
        - `eta_abs`: float
        - `eta_cu`: float
        - `eta_STH`: float
    - `As/GaSe`:
      - `type`: object
      - `required`:
        - `eta_abs`: float
        - `eta_cu`: float
        - `eta_STH`: float

Notes: All scored artifacts are derived from the agent's DFT simulation pipeline. The checker compares computed values to hidden paper-reported references using appropriate tolerances. For STH efficiency, meeting or exceeding the reference value earns full credit (threshold_or_better); for other quantities, closeness within tolerance is scored via reference_match.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "monolayer_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "As": {
            "type": "object",
            "required": {
              "lattice_constant_A": "float",
              "bond_length_A": "float",
              "bandgap_eV": "float",
              "gap_type": "string"
            }
          },
          "GaS": {
            "type": "object",
            "required": {
              "lattice_constant_A": "float",
              "bond_length_A": "float",
              "bandgap_eV": "float",
              "gap_type": "string"
            }
          },
          "GaSe": {
            "type": "object",
            "required": {
              "lattice_constant_A": "float",
              "bond_length_A": "float",
              "bandgap_eV": "float",
              "gap_type": "string"
            }
          }
        }
      },
      "description": "Structural and electronic properties of the isolated As, GaS, and GaSe monolayers."
    },
    {
      "file": "heterostructure_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "As/GaS": {
            "type": "object",
            "required": {
              "binding_energy_meV_per_Ang2": "float",
              "interlayer_distance_A": "float",
              "bandgap_eV": "float",
              "CBM_energy_eV": "float",
              "VBM_energy_eV": "float",
              "CBO_eV": "float",
              "VBO_eV": "float",
              "bader_charge_transfer_e": "float",
              "potential_drop_eV": "float",
              "typeII_confirmed": "boolean"
            }
          },
          "As/GaSe": {
            "type": "object",
            "required": {
              "binding_energy_meV_per_Ang2": "float",
              "interlayer_distance_A": "float",
              "bandgap_eV": "float",
              "CBM_energy_eV": "float",
              "VBM_energy_eV": "float",
              "CBO_eV": "float",
              "VBO_eV": "float",
              "bader_charge_transfer_e": "float",
              "potential_drop_eV": "float",
              "typeII_confirmed": "boolean"
            }
          }
        }
      },
      "description": "Interfacial and electronic properties of the most stable As/GaS and As/GaSe vdW heterostructures."
    },
    {
      "file": "st_hydrogen_efficiency.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "As": {
            "type": "object",
            "required": {
              "eta_abs": "float",
              "eta_cu": "float",
              "eta_STH": "float"
            }
          },
          "GaS": {
            "type": "object",
            "required": {
              "eta_abs": "float",
              "eta_cu": "float",
              "eta_STH": "float"
            }
          },
          "GaSe": {
            "type": "object",
            "required": {
              "eta_abs": "float",
              "eta_cu": "float",
              "eta_STH": "float"
            }
          },
          "As/GaS": {
            "type": "object",
            "required": {
              "eta_abs": "float",
              "eta_cu": "float",
              "eta_STH": "float"
            }
          },
          "As/GaSe": {
            "type": "object",
            "required": {
              "eta_abs": "float",
              "eta_cu": "float",
              "eta_STH": "float"
            }
          }
        }
      },
      "description": "Solar-to-hydrogen efficiency components and final STH efficiency for all systems."
    }
  ],
  "notes": "All scored artifacts are derived from the agent's DFT simulation pipeline. The checker compares computed values to hidden paper-reported references using appropriate tolerances. For STH efficiency, meeting or exceeding the reference value earns full credit (threshold_or_better); for other quantities, closeness within tolerance is scored via reference_match."
}
```

## How you are scored
A hidden verifier independently compares each scored output file against reference values derived from the published paper’s results. Numerical quantities (lattice constants, bond lengths, band gaps, band offsets, charge transfer, potential drop, efficiencies) are compared with appropriate tolerances; qualitative properties (gap type, type‑II confirmation) are checked for correct assignment. For directional performance metrics such as STH efficiency, meeting or exceeding the reference value earns full credit; credit decreases only when the result is worse. For fixed parameters, the reward falls with increasing deviation. The per‑artifact scores are combined into a single reward between 0 and 1. The verifier reads only the JSON artifacts; raw DFT logs are not scored.

# Computational evaluation of a 2D van der Waals heterostructure for Z-scheme photocatalysis

## Problem background
Solar-driven water splitting using semiconductor photocatalysts is a promising route for sustainable hydrogen production. Constructing Z‑scheme systems from two-dimensional (2D) van der Waals heterostructures can improve light absorption and charge separation while preserving strong redox potentials. Monolayer blue phosphorene (BlueP) and monolayer phosphorus nitride (PN) are candidate building blocks. This task investigates the structural, electronic, optical, and catalytic properties of a BlueP/PN 2D heterostructure and evaluates its potential as a Z‑scheme photocatalyst for overall water splitting.

## Approach
Use first‑principles density functional theory (DFT) with an open‑source plane‑wave code. Employ the PBE generalized gradient approximation for geometry relaxations and the HSE06 hybrid functional for accurate band structures and optical spectra; include Grimme D2 van der Waals corrections. Construct monolayer BlueP (trigonal, P‑3M1) and monolayer PN (P3M1), optimize their lattice constants, and build candidate BlueP/PN heterostructures at a low‑mismatch supercell commensuration (e.g., 4×4 BlueP / 5×5 PN). Screen stacking configurations by formation energy and select the most stable one. Compute: (i) band structures and projected density of states to determine band gaps and band‑edge character; (ii) planar‑averaged electrostatic potentials to extract work functions of the isolated monolayers; (iii) charge density difference and potential profile of the heterostructure to quantify interfacial charge transfer and the built‑in potential drop; (iv) optical absorption coefficients from the HSE06 dielectric function for the monolayers and the heterostructure; (v) Gibbs free energy of hydrogen adsorption (ΔG_H*) on BlueP, PN, and the heterostructure using the computational hydrogen electrode model.

## Reproduction target
Run the full DFT workflow described in the steps below and write all key quantitative outcomes to a single JSON file at /app/outputs/results.json. The file must contain: HSE06 band gaps of monolayer BlueP and PN (eV), HSE06 band gap of the heterostructure (eV) and whether it is direct or indirect, work functions of BlueP and PN (eV), net charge transferred from PN to BlueP in the heterostructure (e), built‑in potential drop across the interface (eV), which layer hosts the VBM and CBM in the heterostructure, Gibbs free energies of hydrogen adsorption on BlueP, PN, and the heterostructure (eV), and a boolean flag indicating whether the heterostructure exhibits enhanced visible‑light absorption relative to the sum of the individual monolayers.

## Assets

- Open-source DFT code with HSE06 support (e.g., Quantum ESPRESSO, CP2K): https://www.quantum-espresso.org/
- PBE pseudopotentials (e.g., SSSP library): https://www.materialscloud.org/discover/sssp/package/pbe

## Workflow steps

### Step 1: Geometry optimization of monolayer BlueP and PN
- Role: process
- Action: Perform full relaxation of monolayer BlueP (trigonal, P-3M1, starting lattice constant ~3.31 Å) and monolayer PN (P3M1, ~2.692 Å) using PBE functional and Grimme D2 van der Waals correction.
- Evidence: none

### Step 2: Heterostructure construction and stability screening
- Role: process
- Action: Build candidate BlueP/PN heterostructures (various stacking configurations) including the type II-1 model (4x4 BlueP / 5x5 PN supercell, minimal lattice mismatch ~0.75%). Compute formation energies with PBE+D2 and select the most stable configuration for subsequent analysis.
- Evidence: none

### Step 3: Work function and electrostatic potential of monolayers
- Role: process
- Action: Compute the planar-averaged electrostatic potential along the surface normal for isolated BlueP and PN monolayers; extract work functions from the difference between vacuum level and Fermi level.
- Evidence: none

### Step 4: Interfacial charge transfer and potential drop
- Role: process
- Action: Calculate the charge density difference Δρ = ρ(hetero) – ρ(BlueP) – ρ(PN) for the selected heterostructure. Integrate the planar-averaged Δρ to obtain net transferred charge and extract the built-in potential drop from the electrostatic potential profile.
- Evidence: none

### Step 5: HSE06 band structure and projected DOS of the heterostructure
- Role: process
- Action: Compute the electronic band structure and total/projected density of states for the stable heterostructure using the HSE06 hybrid functional. Identify the VBM and CBM locations in k-space and the dominant atomic/orbital contributions.
- Evidence: none

### Step 6: Optical absorption coefficient
- Role: process
- Action: From the HSE06 dielectric function, calculate the optical absorption coefficient for BlueP, PN, and the heterostructure. Compare the heterostructure's visible-range absorption to the superposition of isolated monolayers to assess enhancement.
- Evidence: none

### Step 7: Gibbs free energy of hydrogen adsorption (HER)
- Role: process
- Action: Build hydrogen-adsorbed surface models for BlueP, PN, and the heterostructure (large supercells, H-H distance >10 Å). Optimize geometries with PBE+D2, compute vibrational frequencies and zero-point energies, then evaluate ΔG_H* = ΔE_H* + ΔZPE - TΔS using the computational hydrogen electrode model.
- Evidence: none

### Step 8: Aggregate final results
- Role: scored (load-bearing)
- Action: Collect all computed properties from the preceding stages and write them into results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: Top-level object with keys: bluep_band_gap_hse06 (float, eV), pn_band_gap_hse06 (float, eV), hetero_band_gap (float, eV), hetero_direct_gap (bool), bluep_work_function (float, eV), pn_work_function (float, eV), charge_transfer_delta_Q (float, e), potential_drop_delta_V_H (float, eV), vbm_layer (string, 'BlueP' or 'PN'), cbm_layer (string, 'BlueP' or 'PN'), her_delta_G_bluep (float, eV), her_delta_G_pn (float, eV), her_delta_G_hetero (float, eV), optical_absorption_enhancement (bool).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Aggregate results of DFT calculations for the BlueP/PN heterostructure, including band gaps, work functions, charge transfer, potential drop, band alignment, HER free energies, and optical absorption enhancement. The checker compares each field to the paper's reported values with domain-appropriate tolerances.
- schema:
  - `type`: object
  - `required`: `bluep_band_gap_hse06`, `pn_band_gap_hse06`, `hetero_band_gap`, `hetero_direct_gap`, `bluep_work_function`, `pn_work_function`, `charge_transfer_delta_Q`, `potential_drop_delta_V_H`, `vbm_layer`, `cbm_layer`, `her_delta_G_bluep`, `her_delta_G_pn`, `her_delta_G_hetero`, `optical_absorption_enhancement`
  - `properties`:
    - `bluep_band_gap_hse06`:
      - `type`: number
      - `description`: HSE06 band gap of monolayer BlueP (eV)
    - `pn_band_gap_hse06`:
      - `type`: number
      - `description`: HSE06 band gap of monolayer PN (eV)
    - `hetero_band_gap`:
      - `type`: number
      - `description`: HSE06 band gap of the BlueP/PN heterostructure (eV)
    - `hetero_direct_gap`:
      - `type`: boolean
      - `description`: True if the heterostructure has a direct band gap, False if indirect
    - `bluep_work_function`:
      - `type`: number
      - `description`: Work function of monolayer BlueP (eV)
    - `pn_work_function`:
      - `type`: number
      - `description`: Work function of monolayer PN (eV)
    - `charge_transfer_delta_Q`:
      - `type`: number
      - `description`: Net transferred charge per unit cell from PN to BlueP (e)
    - `potential_drop_delta_V_H`:
      - `type`: number
      - `description`: Built-in potential drop across the interface (eV)
    - `vbm_layer`:
      - `type`: string
      - `enum`: `BlueP`, `PN`
      - `description`: Layer where the valence band maximum is predominantly located
    - `cbm_layer`:
      - `type`: string
      - `enum`: `BlueP`, `PN`
      - `description`: Layer where the conduction band minimum is predominantly located
    - `her_delta_G_bluep`:
      - `type`: number
      - `description`: Gibbs free energy of hydrogen adsorption on BlueP (eV)
    - `her_delta_G_pn`:
      - `type`: number
      - `description`: Gibbs free energy of hydrogen adsorption on PN (eV)
    - `her_delta_G_hetero`:
      - `type`: number
      - `description`: Gibbs free energy of hydrogen adsorption on the heterostructure (eV)
    - `optical_absorption_enhancement`:
      - `type`: boolean
      - `description`: True if the heterostructure shows enhanced visible-light absorption compared to the sum of the individual layers

Notes: The scored artifact is the sole aggregate file; process steps must be genuinely executed to generate the required properties. Tolerances are designed to accept an independent re-run with a different open-source DFT code while rejecting random guesses.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "bluep_band_gap_hse06",
          "pn_band_gap_hse06",
          "hetero_band_gap",
          "hetero_direct_gap",
          "bluep_work_function",
          "pn_work_function",
          "charge_transfer_delta_Q",
          "potential_drop_delta_V_H",
          "vbm_layer",
          "cbm_layer",
          "her_delta_G_bluep",
          "her_delta_G_pn",
          "her_delta_G_hetero",
          "optical_absorption_enhancement"
        ],
        "properties": {
          "bluep_band_gap_hse06": {
            "type": "number",
            "description": "HSE06 band gap of monolayer BlueP (eV)"
          },
          "pn_band_gap_hse06": {
            "type": "number",
            "description": "HSE06 band gap of monolayer PN (eV)"
          },
          "hetero_band_gap": {
            "type": "number",
            "description": "HSE06 band gap of the BlueP/PN heterostructure (eV)"
          },
          "hetero_direct_gap": {
            "type": "boolean",
            "description": "True if the heterostructure has a direct band gap, False if indirect"
          },
          "bluep_work_function": {
            "type": "number",
            "description": "Work function of monolayer BlueP (eV)"
          },
          "pn_work_function": {
            "type": "number",
            "description": "Work function of monolayer PN (eV)"
          },
          "charge_transfer_delta_Q": {
            "type": "number",
            "description": "Net transferred charge per unit cell from PN to BlueP (e)"
          },
          "potential_drop_delta_V_H": {
            "type": "number",
            "description": "Built-in potential drop across the interface (eV)"
          },
          "vbm_layer": {
            "type": "string",
            "enum": [
              "BlueP",
              "PN"
            ],
            "description": "Layer where the valence band maximum is predominantly located"
          },
          "cbm_layer": {
            "type": "string",
            "enum": [
              "BlueP",
              "PN"
            ],
            "description": "Layer where the conduction band minimum is predominantly located"
          },
          "her_delta_G_bluep": {
            "type": "number",
            "description": "Gibbs free energy of hydrogen adsorption on BlueP (eV)"
          },
          "her_delta_G_pn": {
            "type": "number",
            "description": "Gibbs free energy of hydrogen adsorption on PN (eV)"
          },
          "her_delta_G_hetero": {
            "type": "number",
            "description": "Gibbs free energy of hydrogen adsorption on the heterostructure (eV)"
          },
          "optical_absorption_enhancement": {
            "type": "boolean",
            "description": "True if the heterostructure shows enhanced visible-light absorption compared to the sum of the individual layers"
          }
        }
      },
      "description": "Aggregate results of DFT calculations for the BlueP/PN heterostructure, including band gaps, work functions, charge transfer, potential drop, band alignment, HER free energies, and optical absorption enhancement. The checker compares each field to the paper's reported values with domain-appropriate tolerances."
    }
  ],
  "notes": "The scored artifact is the sole aggregate file; process steps must be genuinely executed to generate the required properties. Tolerances are designed to accept an independent re-run with a different open-source DFT code while rejecting random guesses."
}
```

## How you are scored
A hidden verifier independently checks every field in your results.json against a reference. Numeric quantities are compared with domain‑appropriate tolerances; categorical entries (direct/indirect gap, VBM/CBM layer assignments) and the optical‑enhancement boolean require an exact match. In addition, the verifier confirms that the relative trends implied by your numbers satisfy the physical expectations derived from the paper’s analysis (e.g., the ordering of work functions, the relative HER activities of the three systems, and the optical behaviour). The final score is a weighted average over all fields, with the main scientific quantities receiving the highest weight. Delivering correct intermediate process evidence alone is insufficient; only the aggregated results.json carries reward.

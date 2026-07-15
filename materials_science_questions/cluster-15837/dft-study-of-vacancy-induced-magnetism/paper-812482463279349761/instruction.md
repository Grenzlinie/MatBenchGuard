# DFT study of vacancy-induced magnetism and quantum capacitance in Sc2CF2 monolayer

## Problem background
Two-dimensional MXene materials are promising electrode candidates for energy storage because of their high electrical conductivity and tunable surface chemistry.  The Sc₂CF₂ monolayer is a representative MXene semiconductor with strong anisotropic carrier mobility.  Atomic vacancies are common point defects in these materials and are known to alter electronic, magnetic, and optical properties.  This work investigates, using spin-polarized density functional theory (DFT), how single-atom vacancies (at the carbon, fluorine, or scandium site) modify the electronic structure, magnetism, optical response, and quantum capacitance of the Sc₂CF₂ monolayer.  The key physical question is: which vacancy, if any, leads to the largest enhancement of the quantum capacitance near zero applied voltage, and can a vacancy induce magnetism in this non-magnetic parent material?  The target quantities to be computed from first principles are the band gap of pristine Sc₂CF₂, the magnetic moment of the scandium-vacancy system, the formation and binding energies of all four systems (pristine, V_C, V_F, V_Sc), the positions of the maximum optical absorption and reflectivity peaks, and the differential and integrated quantum capacitance as functions of applied voltage over the electrochemical window of an aqueous electrolyte (±0.6 V).

## Approach
The computational approach uses spin-polarized DFT with the Perdew-Burke-Ernzerhof (PBE) exchange-correlation functional and the DFT-D3 van der Waals correction.  We model a 3×3×1 supercell of the Sc₂CF₂ monolayer to separately introduce a single carbon, fluorine, or scandium vacancy.  The workflow consists of four stages: (1) geometry relaxation of each supercell to find its lowest-energy structure; (2) reference calculations of isolated Sc, C, and F atoms for formation and binding energy analysis; (3) electronic structure calculations on the relaxed geometries to obtain the total and projected density of states, band structure, magnetic moments, and the frequency-dependent dielectric function from which absorption and reflectivity spectra are derived; (4) numerical post-processing of the density of states at 300 K to compute the differential quantum capacitance C_diff, the stored surface charge Q, and the integrated quantum capacitance C_int as a function of applied voltage.  All calculations use an open-source plane-wave DFT code (e.g., Quantum ESPRESSO) and publicly available PBE pseudopotentials.  The systems are compared side by side: pristine versus vacancy-defect monolayers, and the different vacancy types are compared among themselves to identify which defect most strongly enhances the quantum capacitance.

## Reproduction target
Produce the following two artifacts from the DFT calculations and post-processing:

1. **electronic_properties.json** containing the computed electronic and stability properties:
   - band gap of pristine Sc₂CF₂ (eV)
   - magnetic moment of the Sc-vacancy system (µ_B)
   - vacancy formation energies (eV) for V_C, V_F, and V_Sc
   - binding energies per atom (eV/atom) for pristine, V_C, V_F, and V_Sc (as an array of four numbers ordered [pristine, V_C, V_F, V_Sc])
   - positions of the maximum absorption peak (eV) for each of the four systems (ordered [pristine, V_C, V_F, V_Sc])
   - positions of the maximum reflectivity peak (eV) for each of the four systems (ordered [pristine, V_C, V_F, V_Sc])

2. **quantum_capacitance.csv** containing the quantum capacitance metrics for all four systems over the voltage range −0.6 V to +0.6 V at 300 K with a voltage step of 0.01 V or finer.  Columns: `system` (string: `pristine`, `V_C`, `V_F`, `V_Sc`), `V` (applied voltage in volts), `C_diff` (differential quantum capacitance in µF/cm²), `Q` (stored charge in µC/cm²), `C_int` (integrated quantum capacitance in µF/cm²).  Every system must have a full curve across the specified voltage window.

## Assets

- Quantum ESPRESSO (or other open-source DFT code): https://www.quantum-espresso.org/
- SSSP efficiency pseudopotential library: https://www.materialscloud.org/discover/sssp/table/efficiency
- Sc₂CF₂ monolayer crystal structure

## Workflow steps

### Step 1: Generate supercell inputs
- Role: process
- Action: Construct 3×3×1 supercells of pristine Sc₂CF₂ and three vacancy systems (V_C, V_F, V_Sc) by removing the corresponding atom. Prepare DFT input files for geometry relaxation.
- Evidence: `/app/outputs/supercell_generation.log`

### Step 2: DFT geometry relaxation
- Role: process
- Action: Perform spin-polarized DFT structural relaxation for all four systems using the PBE functional with DFT-D3 van der Waals correction. Use an appropriate plane‑wave cutoff and k‑point grid, and converge forces below 0.01 eV/Å. Save relaxed structures and total energies.
- Evidence: `/app/outputs/relaxation_output.log`

### Step 3: Isolated atom energy calculations
- Role: process
- Action: Compute total energies of isolated Sc, C, and F atoms using the same DFT settings and pseudopotentials, placing each atom in a large simulation cell to avoid spurious interactions. These energies serve as references for formation and binding energy calculations.
- Evidence: `/app/outputs/isolated_atom_energies.log`

### Step 4: Electronic structure and optical calculations
- Role: process
- Action: On the relaxed structures, perform spin‑polarized SCF calculations with denser k‑point grids to obtain total and partial density of states, band structure, and magnetic moments. Additionally compute the frequency‑dependent dielectric function and derive optical absorption coefficient and reflectivity spectra.
- Evidence: `/app/outputs/dos_optical_output.log`

### Step 5: Extract electronic properties and stability
- Role: scored
- Action: From the DFT outputs, extract the following quantities: band gap of pristine Sc₂CF₂ (eV), magnetic moment of the Sc‑vacancy system (μ_B), vacancy formation energies E_form for V_C, V_F, V_Sc (eV), binding energies per atom for all four systems (eV/atom), and the positions of maximum absorption and maximum reflectivity (eV) for each of the four systems. Write the entire set of properties to electronic_properties.json.
- Output file: `/app/outputs/electronic_properties.json`
- Format: json
- Contract: Object with keys: band_gap_pristine (eV, float), magnetic_moment_VSc (μB, float), E_form_Vc (eV, float), E_form_Vf (eV, float), E_form_VSc (eV, float), E_binding_all ([pristine, V_C, V_F, V_Sc] eV/atom, array of floats), absorption_peak_positions ([pristine, V_C, V_F, V_Sc] eV, array of floats), reflectivity_max_positions ([pristine, V_C, V_F, V_Sc] eV, array of floats).
- Scoring: scored by hidden verifier

### Step 6: Compute quantum capacitance curves
- Role: scored (load-bearing)
- Action: Using the total density of states of each system, numerically compute the differential quantum capacitance C_diff, stored surface charge Q, and integrated quantum capacitance C_int at 300 K over the voltage window −0.6 V to +0.6 V (step ≤0.01 V). Store the full curves in quantum_capacitance.csv.
- Output file: `/app/outputs/quantum_capacitance.csv`
- Format: csv
- Contract: Columns: system (string; one of pristine, V_C, V_F, V_Sc), V (float, volts), C_diff (float, μF/cm²), Q (float, μC/cm²), C_int (float, μF/cm²). Rows cover the full voltage sweep for each system.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/electronic_properties.json`
- `/app/outputs/quantum_capacitance.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### electronic_properties.json
- path: `/app/outputs/electronic_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Extracted electronic and stability properties, serving as the basis for verification of band gap, magnetism, formation energies, binding energies, and optical peak positions.
- schema:
  - `type`: object
  - `required`:
    - `band_gap_pristine`: number (eV)
    - `magnetic_moment_VSc`: number (μB)
    - `E_form_Vc`: number (eV)
    - `E_form_Vf`: number (eV)
    - `E_form_VSc`: number (eV)
    - `E_binding_all`: array of 4 numbers (eV/atom)
    - `absorption_peak_positions`: array of 4 numbers (eV)
    - `reflectivity_max_positions`: array of 4 numbers (eV)
  - `items`: object
  - `required_columns`:
  - `units`: object

### quantum_capacitance.csv
- path: `/app/outputs/quantum_capacitance.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Quantum capacitance curves for pristine and vacancy-defect systems, enabling verification of the enhanced capacitance and the identification of V_F as the best anode candidate.
- schema:
  - `type`: table
  - `required`: object
  - `items`: object
  - `required_columns`: `system`, `V`, `C_diff`, `Q`, `C_int`
  - `units`:
    - `V`: V
    - `C_diff`: μF/cm²
    - `Q`: μC/cm²
    - `C_int`: μF/cm²

Notes: The checker compares the submitted values and curves against the paper's reported numbers using preset tolerances. The agent must reproduce all listed properties with an open-source DFT code (e.g., Quantum ESPRESSO) and PBE functional; small systematic differences are expected and accounted for by the tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "electronic_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "band_gap_pristine": "number (eV)",
          "magnetic_moment_VSc": "number (μB)",
          "E_form_Vc": "number (eV)",
          "E_form_Vf": "number (eV)",
          "E_form_VSc": "number (eV)",
          "E_binding_all": "array of 4 numbers (eV/atom)",
          "absorption_peak_positions": "array of 4 numbers (eV)",
          "reflectivity_max_positions": "array of 4 numbers (eV)"
        },
        "items": {},
        "required_columns": [],
        "units": {}
      },
      "description": "Extracted electronic and stability properties, serving as the basis for verification of band gap, magnetism, formation energies, binding energies, and optical peak positions."
    },
    {
      "file": "quantum_capacitance.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required": {},
        "items": {},
        "required_columns": [
          "system",
          "V",
          "C_diff",
          "Q",
          "C_int"
        ],
        "units": {
          "V": "V",
          "C_diff": "μF/cm²",
          "Q": "μC/cm²",
          "C_int": "μF/cm²"
        }
      },
      "description": "Quantum capacitance curves for pristine and vacancy-defect systems, enabling verification of the enhanced capacitance and the identification of V_F as the best anode candidate."
    }
  ],
  "notes": "The checker compares the submitted values and curves against the paper's reported numbers using preset tolerances. The agent must reproduce all listed properties with an open-source DFT code (e.g., Quantum ESPRESSO) and PBE functional; small systematic differences are expected and accounted for by the tolerances."
}
```

## How you are scored
Each scored artifact is independently checked by a hidden verifier that compares the submitted values and curves against the expected reference results (derived from the underlying physical quantities).  For `electronic_properties.json`, the verifier reads each numeric property and checks that it falls within an appropriate tolerance; the band gap, magnetic moment, formation energies, binding energies, and optical peak positions all contribute to this stage's score.  For `quantum_capacitance.csv`, the verifier reads the full voltage sweeps and computes summary metrics such as the integrated quantum capacitance at zero voltage and the maximum differential capacitance in the positive and negative bias regions, then compares them to the reference values.  The two artifacts are weighted so that the quantum capacitance stage (which embodies the main energy-storage claim) carries a larger share of the total reward, and the final reward is a weighted combination of the individual stage scores.  The verifier never sees the source paper; it uses only the internally stored reference numbers and tolerances to check correctness.

# DFT electronic structure and optical properties of lithium titanate spinel compounds

## Problem background
Lithium titanate spinel compounds (LiTi2O4, Li4Ti5O12, Li2Ti2O4, Li7Ti5O12) are widely studied as anode materials for Li-ion batteries and have potential optical applications. Understanding their electronic structure (band gaps, orbital contributions, crystal-field splitting) and the derived optical properties (dielectric function, absorption, refractive index) is essential for tuning these properties via Li-ion intercalation. First-principles density functional theory (DFT) provides a route to compute these quantities and investigate the role of Ti–O hybridization.

## Approach
The approach uses plane-wave pseudopotential DFT with the GGA-PBE exchange-correlation functional. Starting from the known spinel LiTi2O4 crystal structure (space group Fd3m), 3×1×1 supercells are constructed for LiTi2O4 and Li2Ti2O4. For Li4Ti5O12 and Li7Ti5O12, two Ti atoms at 16d sites are substituted by Li according to the lowest-energy configurations given in the supplementary material. All four structures undergo variable-cell geometry optimization to reach equilibrium lattice constants and atomic positions. Subsequently, self-consistent DFT calculations and non-self-consistent band-structure and density-of-states (DOS) computations are performed, yielding total and projected DOS (Li 2s, O 2p, Ti 3d). The optical properties are obtained from the DFT eigenstates: the imaginary part of the dielectric function ε2(ω) is computed from direct transitions, the real part ε1(ω) via Kramers‑Kronig transformation, and the absorption coefficient, refractive index, and extinction coefficient are derived. Key electronic and optical parameters are then extracted from the raw data.

## Reproduction target
Perform first-principles DFT calculations for the four LTO compounds to obtain band structures and density of states, then extract electronic structure parameters (band gaps, O 2p valence band widths, valence-to-conduction separations, Ti 3d t2g/eg crystal-field splitting) and optical property values (static dielectric constants, dielectric peak positions, absorption band energies). Write these quantities to electronic_structure_results.json and optical_properties_results.json under /app/outputs.

## Assets

- Quantum ESPRESSO DFT code: https://www.quantum-espresso.org/
- Pseudopotentials (Li, Ti, O) GGA-PBE: https://www.materialscloud.org/discover/sssp/table/efficiency
- Crystal structure of spinel LiTi2O4: https://materialsproject.org/materials/mp-754200/
- Supplementary material for Li-Ti substitution configurations: 10.1016/j.cplett.2017.04.009
- Atomic Simulation Environment (ASE): https://pypi.org/project/ase/

## Workflow steps

### Step 1: Supercell construction and configuration selection
- Role: process
- Action: Build 3×1×1 supercells of LiTi2O4 and Li2Ti2O4 from the known spinel structure (space group Fd3m). For Li4Ti5O12 and Li7Ti5O12, substitute two Ti by Li at 16d sites according to the lowest-energy configurations (1,8) and (2,9) as listed in the supplementary material. Generate initial crystal structures for all four compounds.
- Evidence: `/app/outputs/initial_structures.json`

### Step 2: DFT structural relaxation
- Role: process
- Action: Perform variable-cell geometry optimization (relaxation) for each compound using DFT (Quantum ESPRESSO, GGA-PBE, ultrasoft pseudopotentials, appropriate k-point grid and cutoff). Converge forces and stress to obtain equilibrium lattice constants and relaxed atomic positions.
- Evidence: `/app/outputs/relaxed_structures.json`

### Step 3: DFT electronic structure calculation
- Role: process
- Action: Using the relaxed structures, perform a self-consistent DFT calculation followed by non-self-consistent band structure and density-of-states calculations. Compute total DOS (TDOS) and projected DOS (PDOS) onto Li 2s, O 2p, and Ti 3d orbitals. Save the raw electronic structure data (eigenvalues, projected weights) for downstream analysis.
- Evidence: `/app/outputs/electronic_raw_data.json`

### Step 4: Optical property computation
- Role: process
- Action: From the DFT eigenstates, compute the imaginary part of the dielectric function ε2(ω) using the momentum matrix elements (direct transitions). Use Kramers-Kronig transformation to obtain ε1(ω). Derive absorption coefficient α(ω), refractive index n(ω), and extinction coefficient k(ω). Save the spectra.
- Evidence: `/app/outputs/optical_raw_data.json`

### Step 5: Electronic structure analysis and reporting
- Role: scored (load-bearing)
- Action: From the computed electronic structure and DOS, extract for each compound: the DFT band gap (0 for metallic), the O 2p valence band width, the energy separation between the O 2p band maximum and the Ti 3d band minimum (or Fermi level), and a boolean indicating clear t2g-eg crystal-field splitting of Ti 3d. Write the results to electronic_structure_results.json.
- Output file: `/app/outputs/electronic_structure_results.json`
- Format: json
- Contract: JSON object with keys LiTi2O4, Li4Ti5O12, Li2Ti2O4, Li7Ti5O12. Each contains: band_gap (float, eV), o2p_valence_band_width (float, eV), valence_to_conduction_separation (float, eV), t2g_eg_splitting_observed (boolean).
- Scoring: scored by hidden verifier

### Step 6: Optical properties extraction and reporting
- Role: scored
- Action: From the computed optical spectra, extract for each compound: the static dielectric constant ε1(0) (real part at ω=0), the energy of the first major dielectric peak A in the infrared region (if present, otherwise null), the near-UV dielectric peak B energy, and the set of main absorption band energies (six peaks for the insulator, corresponding blue-shifted peaks for the others). Write the results to optical_properties_results.json.
- Output file: `/app/outputs/optical_properties_results.json`
- Format: json
- Contract: JSON object with keys LiTi2O4, Li4Ti5O12, Li2Ti2O4, Li7Ti5O12. Each contains: static_dielectric_constant (float), dielectric_peak_A_energy (float or null, eV), dielectric_peak_B_energy (float, eV), absorption_peak_energies (list of float, eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/electronic_structure_results.json`
- `/app/outputs/optical_properties_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### electronic_structure_results.json
- path: `/app/outputs/electronic_structure_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Agent's extracted electronic structure parameters (band gap, O 2p width, separation, t2g/eg splitting) for each LTO compound, checked against hidden reference values derived from the paper.
- schema:
  - `type`: object
  - `required`:
    - `LiTi2O4`: object
    - `Li4Ti5O12`: object
    - `Li2Ti2O4`: object
    - `Li7Ti5O12`: object
  - `items`:
    - `band_gap`: number (eV)
    - `o2p_valence_band_width`: number (eV)
    - `valence_to_conduction_separation`: number (eV)
    - `t2g_eg_splitting_observed`: boolean
  - `units`:
    - `band_gap`: eV
    - `o2p_valence_band_width`: eV
    - `valence_to_conduction_separation`: eV

### optical_properties_results.json
- path: `/app/outputs/optical_properties_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Agent's extracted optical property values (static dielectric constant, peak energies, absorption band energies) for each LTO compound, checked against hidden reference values derived from the paper.
- schema:
  - `type`: object
  - `required`:
    - `LiTi2O4`: object
    - `Li4Ti5O12`: object
    - `Li2Ti2O4`: object
    - `Li7Ti5O12`: object
  - `items`:
    - `static_dielectric_constant`: number
    - `dielectric_peak_A_energy`: number or null (eV)
    - `dielectric_peak_B_energy`: number (eV)
    - `absorption_peak_energies`: array of numbers (eV)
  - `units`:
    - `static_dielectric_constant`: dimensionless
    - `dielectric_peak_A_energy`: eV
    - `dielectric_peak_B_energy`: eV
    - `absorption_peak_energies`: eV

Notes: The hidden checker compares the submitted values to reference data using appropriate tolerances. The solver must run the DFT pipeline with an open-source code (e.g., Quantum ESPRESSO) and report the extracted quantities; exact toolchain choices are handled by the tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "electronic_structure_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "LiTi2O4": "object",
          "Li4Ti5O12": "object",
          "Li2Ti2O4": "object",
          "Li7Ti5O12": "object"
        },
        "items": {
          "band_gap": "number (eV)",
          "o2p_valence_band_width": "number (eV)",
          "valence_to_conduction_separation": "number (eV)",
          "t2g_eg_splitting_observed": "boolean"
        },
        "units": {
          "band_gap": "eV",
          "o2p_valence_band_width": "eV",
          "valence_to_conduction_separation": "eV"
        }
      },
      "description": "Agent's extracted electronic structure parameters (band gap, O 2p width, separation, t2g/eg splitting) for each LTO compound, checked against hidden reference values derived from the paper."
    },
    {
      "file": "optical_properties_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "LiTi2O4": "object",
          "Li4Ti5O12": "object",
          "Li2Ti2O4": "object",
          "Li7Ti5O12": "object"
        },
        "items": {
          "static_dielectric_constant": "number",
          "dielectric_peak_A_energy": "number or null (eV)",
          "dielectric_peak_B_energy": "number (eV)",
          "absorption_peak_energies": "array of numbers (eV)"
        },
        "units": {
          "static_dielectric_constant": "dimensionless",
          "dielectric_peak_A_energy": "eV",
          "dielectric_peak_B_energy": "eV",
          "absorption_peak_energies": "eV"
        }
      },
      "description": "Agent's extracted optical property values (static dielectric constant, peak energies, absorption band energies) for each LTO compound, checked against hidden reference values derived from the paper."
    }
  ],
  "notes": "The hidden checker compares the submitted values to reference data using appropriate tolerances. The solver must run the DFT pipeline with an open-source code (e.g., Quantum ESPRESSO) and report the extracted quantities; exact toolchain choices are handled by the tolerances."
}
```

## How you are scored
A hidden verifier reads electronic_structure_results.json and optical_properties_results.json and compares each reported quantity (band gaps, valence band widths, separations, static dielectric constant, dielectric peak energies, absorption peak energies, and the t2g_eg_splitting_observed boolean) to hidden reference values. Each quantity within the allowed tolerance (or matching the expected boolean) contributes to the score. The final reward is the fraction of quantities that meet the acceptance criteria. Simply reporting numbers without executing the DFT pipeline will not satisfy the check.

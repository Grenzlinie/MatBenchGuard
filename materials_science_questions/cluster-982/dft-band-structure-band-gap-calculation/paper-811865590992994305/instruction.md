# First-Principles DFT Calculation of Physical Properties of Magnesium Nitridoboride

## Problem background
Magnesium nitridoboride (MgNB₉) is a new boride material whose electronic, dielectric, vibrational, and elastic properties have not been previously studied. First-principles density functional theory (DFT) calculations can predict these physical properties and assess its potential for optoelectronic applications. In this task, you will compute these properties for the MgNB₉ crystal using an open-source DFT code.

## Approach
The calculations are performed using the plane-wave pseudopotential method as implemented in the ABINIT package. The exchange-correlation functional is PBE-GGA, and norm-conserving Troullier–Martins pseudopotentials are used for B, N, Mg. The workflow begins by constructing the rhombohedral unit cell from the published crystal structure (space group R-3m, a = 5.4960 Å, c = 20.0873 Å). After a structural relaxation at the experimental volume, a self-consistent ground-state calculation is performed, followed by a band structure calculation along the high-symmetry path. Density functional perturbation theory (DFPT) is then employed to compute the electronic dielectric permittivity tensor, Born effective charges, and the zone-center dynamical matrix. Phonon frequencies and eigenvectors are obtained, and LO/TO splitting is included via the non-analytical term. The static dielectric tensor is obtained by combining the electronic contribution with the ionic oscillator strengths derived from the phonon modes. Finally, the relaxed-ion elastic constants are computed using DFPT strain-response formalism. All computed results are reported in the required JSON output files.

## Reproduction target
Compute the following quantities for MgNB₉:

- The indirect band gap (in eV) from the electronic band structure, together with the high-symmetry points where the valence band maximum and conduction band minimum are located.
- The electronic dielectric tensor components ε⊥∞ and ε∥∞ (dimensionless).
- The Born effective charge tensors for all atoms (not required to be reported, but needed for subsequent steps).
- All zone-center phonon frequencies (in cm⁻¹), with their irreducible representations and TO/LO character for IR-active modes.
- The static dielectric tensor components ε⊥0 and ε∥0 (dimensionless).
- The relaxed-ion elastic constants C11, C12, C13, C14, C33, C44 (in GPa).

You must follow the workflow steps in order and produce the three scored JSON files as specified. A successful reproduction requires physically consistent values derived from the DFT calculations.

## Assets

- Crystal structure of MgNB₉: 10.1107/S0108270102012022
- ABINIT: https://www.abinit.org/
- Norm-conserving Troullier-Martins pseudopotentials for B, N, Mg

## Workflow steps

### Step 1: Prepare crystal structure and relax
- Role: process
- Action: Construct the rhombohedral unit cell of MgNB₉ (space group R-3m, 22 atoms) using experimental lattice parameters. Perform DFT structural relaxation at the experimental volume with the PBE exchange-correlation functional, using pseudopotentials and plane-wave basis. Provide evidence of relaxation (e.g., final forces).
- Evidence: `/app/outputs/relaxation.log`

### Step 2: Self-consistent field (SCF) calculation
- Role: process
- Action: Perform a self-consistent ground-state DFT calculation on the relaxed structure to obtain the Kohn-Sham wavefunctions and charge density.
- Evidence: `/app/outputs/scf.log`

### Step 3: Electronic band structure and band gap
- Role: process
- Action: Compute the electronic band structure along the high-symmetry path F-Γ-Z-L-Γ of the R-3m Brillouin zone. Determine the valence band maximum and conduction band minimum positions and extract the indirect band gap.
- Evidence: `/app/outputs/bandstructure.dat`

### Step 4: Electronic dielectric tensor and Born effective charges
- Role: process
- Action: Using density functional perturbation theory (DFPT), compute the electronic dielectric permittivity tensor and the Born effective charge tensors for all atoms in the asymmetric unit.
- Evidence: `/app/outputs/dielectric.out`

### Step 5: Zone-center phonon frequencies
- Role: process
- Action: Compute the dynamical matrix at the Γ point using DFPT, diagonalize it to obtain phonon frequencies and eigenvectors. Classify modes by irreducible representations of the D3d point group. Incorporate the non-analytical term to compute LO/TO splitting for IR-active modes using the previously computed Born effective charges and electronic dielectric tensor.
- Evidence: `/app/outputs/phonon.out`

### Step 6: Static dielectric tensor
- Role: process
- Action: From the phonon frequencies, eigenvectors, Born effective charges, and electronic dielectric tensor, compute the mode oscillator strengths and the ionic contribution to the static dielectric tensor.
- Evidence: `/app/outputs/static_dielectric.out`

### Step 7: Report band gap and dielectric constants
- Role: scored (load-bearing)
- Action: Compile the indirect band gap (eV), electronic dielectric tensor components, and static dielectric tensor components into a JSON file.
- Output file: `/app/outputs/step_01_band_gap_and_dielectric.json`
- Format: json
- Contract: {"band_gap_eV": number, "epsilon_inf_perp": number, "epsilon_inf_par": number, "epsilon0_perp": number, "epsilon0_par": number}
- Scoring: scored by hidden verifier

### Step 8: Report zone-center phonon frequencies
- Role: scored
- Action: List all zone-center phonon modes with their frequencies (cm⁻¹), irreducible representation, and character (TO/LO for IR-active, Raman, or silent). Save as JSON.
- Output file: `/app/outputs/step_02_phonon_frequencies.json`
- Format: json
- Contract: {"modes": [{"symmetry": string, "frequency_cm-1": number, "character": string, "irreducible_rep": string}, ...]}
- Scoring: scored by hidden verifier

### Step 9: Elastic constants calculation
- Role: process
- Action: Compute the relaxed-ion elastic constants using DFPT strain-response formalism, including force-response internal stress and displacement-response internal strain contributions.
- Evidence: `/app/outputs/elastic.log`

### Step 10: Report elastic constants
- Role: scored
- Action: Report the relaxed-ion elastic constants (C11, C12, C13, C14, C33, C44) in GPa. Save as JSON.
- Output file: `/app/outputs/step_03_elastic_constants.json`
- Format: json
- Contract: {"C11_GPa": number, "C12_GPa": number, "C13_GPa": number, "C14_GPa": number, "C33_GPa": number, "C44_GPa": number}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_band_gap_and_dielectric.json`
- `/app/outputs/step_02_phonon_frequencies.json`
- `/app/outputs/step_03_elastic_constants.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_band_gap_and_dielectric.json
- path: `/app/outputs/step_01_band_gap_and_dielectric.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Indirect band gap and electronic/static dielectric tensor components.
- schema:
  - `type`: object
  - `required`:
    - `band_gap_eV`: number
    - `epsilon_inf_perp`: number
    - `epsilon_inf_par`: number
    - `epsilon0_perp`: number
    - `epsilon0_par`: number
  - `units`:
    - `band_gap_eV`: eV
    - `epsilon_inf_perp`: dimensionless
    - `epsilon_inf_par`: dimensionless
    - `epsilon0_perp`: dimensionless
    - `epsilon0_par`: dimensionless

### step_02_phonon_frequencies.json
- path: `/app/outputs/step_02_phonon_frequencies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: List of all zone-center phonon frequencies with mode assignments.
- schema:
  - `type`: object
  - `required`:
    - `modes`: array
  - `items`:
    - `symmetry`: string
    - `frequency_cm-1`: number
    - `character`: string
    - `irreducible_rep`: string
  - `units`:
    - `frequency_cm-1`: cm^-1

### step_03_elastic_constants.json
- path: `/app/outputs/step_03_elastic_constants.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Relaxed-ion elastic constants.
- schema:
  - `type`: object
  - `required`:
    - `C11_GPa`: number
    - `C12_GPa`: number
    - `C13_GPa`: number
    - `C14_GPa`: number
    - `C33_GPa`: number
    - `C44_GPa`: number
  - `units`:
    - `C11_GPa`: GPa
    - `C12_GPa`: GPa
    - `C13_GPa`: GPa
    - `C14_GPa`: GPa
    - `C33_GPa`: GPa
    - `C44_GPa`: GPa

Notes: All quantities compared against reference values with appropriate tolerances. The workflow does not include Mulliken bond population or infrared reflectivity spectra.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_band_gap_and_dielectric.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "band_gap_eV": "number",
          "epsilon_inf_perp": "number",
          "epsilon_inf_par": "number",
          "epsilon0_perp": "number",
          "epsilon0_par": "number"
        },
        "units": {
          "band_gap_eV": "eV",
          "epsilon_inf_perp": "dimensionless",
          "epsilon_inf_par": "dimensionless",
          "epsilon0_perp": "dimensionless",
          "epsilon0_par": "dimensionless"
        }
      },
      "description": "Indirect band gap and electronic/static dielectric tensor components."
    },
    {
      "file": "step_02_phonon_frequencies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "modes": "array"
        },
        "items": {
          "symmetry": "string",
          "frequency_cm-1": "number",
          "character": "string",
          "irreducible_rep": "string"
        },
        "units": {
          "frequency_cm-1": "cm^-1"
        }
      },
      "description": "List of all zone-center phonon frequencies with mode assignments."
    },
    {
      "file": "step_03_elastic_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "C11_GPa": "number",
          "C12_GPa": "number",
          "C13_GPa": "number",
          "C14_GPa": "number",
          "C33_GPa": "number",
          "C44_GPa": "number"
        },
        "units": {
          "C11_GPa": "GPa",
          "C12_GPa": "GPa",
          "C13_GPa": "GPa",
          "C14_GPa": "GPa",
          "C33_GPa": "GPa",
          "C44_GPa": "GPa"
        }
      },
      "description": "Relaxed-ion elastic constants."
    }
  ],
  "notes": "All quantities compared against reference values with appropriate tolerances. The workflow does not include Mulliken bond population or infrared reflectivity spectra."
}
```

## How you are scored
Each scored artifact (step_01_band_gap_and_dielectric.json, step_02_phonon_frequencies.json, step_03_elastic_constants.json) is checked by a hidden verifier. The verifier first validates that the JSON files conform to the required schema. Then it compares each numerical quantity to a hidden reference value derived from previously published calculations, using tolerances that account for legitimate differences between DFT implementations. The reward is a weighted sum of scores for each artifact, yielding a final reward between 0 (failure) and 1 (perfect reproduction). The exact tolerances and weights are not disclosed; you must aim for physically meaningful and self-consistent results. The verifier also checks that the reported phonon modes are plausible and that LO/TO splittings are correctly assigned.

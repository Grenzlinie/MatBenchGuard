## Problem background
Lead tungstate (PbWO4, PWO) is a widely used inorganic scintillator, particularly for high-energy physics detectors. Experimental absorption bands in the 330, 360, 420, and 500–750 nm regions have been observed and attributed to the presence of lead vacancies (V_Pb^2-), but direct first-principles evidence linking the vacancy to these specific spectral features was previously lacking.

This task recreates the computational study that computed the electronic structure and polarized optical absorption spectra of PWO supercells (both perfect and containing a lead vacancy) from first principles. The goal is to compute the changes in the electronic band gap, the energy of in-gap defect states, and the specific interband absorption peak energies induced by the vacancy, thereby confirming that the known experimental absorption bands originate from V_Pb^2-.

## Approach
The reproduction follows a first-principles density functional theory (DFT) workflow:

1. **Structural Modeling**: A supercell of PbWO4 (scheelite structure, space group I4_1/a) containing 16 Pb, 16 W, and 64 O atoms is constructed based on the publicly known crystal structure. A defect supercell is created by replacing a centered Pb atom with a vacancy (V_Pb^2-).
2. **Geometry Optimization**: The lattice structure of the defect supercell is relaxed using plane-wave DFT with generalized gradient approximation (GGA) and ultrasoft pseudopotentials to account for local distortions around the vacancy.
3. **Electronic Structure Calculation**: The ground-state electronic structure (Kohn-Sham eigenvalues and orbitals) is computed for both the perfect and relaxed defect supercells. This provides the total density of states (TDOS), the partial density of states (PDOS) of O 2p states, and the band gaps.
4. **Optical Response Calculation**: The frequency-dependent dielectric tensor is calculated from the electronic structure results. A scissors operator shifts the conduction bands rigidly upwards. The Kramers-Kronig transformation, combined with a smearing factor, yields the real part of the dielectric function and the absorption coefficient. The absorption spectra are evaluated for specific light polarizations. From these spectra, the defect-related absorption band maxima (peak energies) are identified.

## Reproduction target
Produce three quantitative results from the DFT workflow:
1. The computed band gap of the perfect PbWO4 supercell and the band gap of the supercell containing the lead vacancy (V_Pb^2-).
2. The energy (relative to the valence band maximum) of the O 2p-derived in-gap state induced by the vacancy.
3. The set of defect-related absorption band maxima (photon energies) extracted from the computed spectra in the range 1–4.5 eV.

The results must be written to three structured JSON files as specified in the workflow steps below.

## Assets
The following public resources are required:

1.  **DFT Software**: An open-source plane-wave DFT code capable of GGA calculations, ultrasoft pseudopotentials, geometry relaxation, electronic structure, and dielectric tensor computation (e.g., Quantum ESPRESSO with `epsilon.x` or ABINIT). The original study used the proprietary code CASTEP; the task is re-scoped to an equivalent open-source implementation.
    - URL (Quantum ESPRESSO): https://www.quantum-espresso.org/
    - URL (ABINIT): https://www.abinit.org/

2.  **Pseudopotentials**: GGA-compatible ultrasoft pseudopotentials for Pb (lead), W (tungsten), and O (oxygen), e.g., from the Standard Solid State Pseudopotentials (SSSP) library.
    - URL (SSSP): https://www.materialscloud.org/discover/sssp/table

3.  **PbWO4 Crystal Structure**: The structural parameters (space group I4_1/a, lattice constants, and atomic positions) for the scheelite PbWO4 crystal. This information is available from standard crystallographic databases such as the Inorganic Crystal Structure Database (ICSD) or published literature. No specific input file is provided; the agent must construct the supercell model from the known structure.

## Workflow steps
### Step 1: Build supercell models
- Role: process
- Action: Construct the perfect PbWO4 supercell (16 Pb, 16 W, 64 O) and the defect supercell with one lead vacancy (center Pb replaced by V_Pb^2-) from the known scheelite crystal structure.
- Evidence: `/app/outputs/defect_supercell_structure.cif`

### Step 2: Lattice relaxation of defect supercell
- Role: process
- Action: Perform DFT geometry relaxation of the defect supercell using the chosen open-source DFT code with ultrasoft pseudopotentials and a plane-wave kinetic energy cutoff of ~340 eV. Optimize atomic positions until forces, energy change, and displacement meet standard convergence criteria (e.g., forces < 0.5 eV/nm, energy change < 1e-5 eV/atom).
- Evidence: `/app/outputs/relaxation_log.txt`

### Step 3: Electronic structure calculation
- Role: process
- Action: Run a GGA-DFT electronic structure calculation on the perfect supercell and the relaxed defect supercell. Compute the Kohn-Sham eigenvalues and the total and partial (O 2p) density of states. The SCF convergence tolerance should be on the order of 1e-6 eV/atom.
- Evidence: `/app/outputs/electronic_structure_log.txt`

### Step 4: Report band gaps
- Role: scored
- Action: From the electronic structure outputs of Step 3, determine the band gap of the perfect PbWO4 supercell and the band gap of the defect supercell. Write the two computed values to a single JSON file.
- Output file: `/app/outputs/band_gap.json`
- Format: json
- Contract: A JSON object with two keys: `perfect_gap_ev` (float) and `defect_gap_ev` (float), representing the computed band gaps in electronvolts (eV).
- Scoring: scored by hidden verifier

### Step 5: Report in-gap state energy
- Role: scored
- Action: From the electronic structure outputs of Step 3, locate the O 2p-derived in-gap state that appears above the valence band maximum in the defect supercell. Determine its energy relative to the VBM and write this value to a JSON file.
- Output file: `/app/outputs/in_gap_state.json`
- Format: json
- Contract: A JSON object with one key: `in_gap_state_energy_ev` (float), representing the energy of the in-gap state in electronvolts (eV).
- Scoring: scored by hidden verifier

### Step 6: Calculate absorption peaks
- Role: scored (load-bearing)
- Action: For the defect supercell, compute the frequency-dependent dielectric tensor from the Kohn-Sham eigenvalues and orbitals obtained in Step 3. Apply a scissors shift of 1.5 eV to the conduction bands. Perform Brillouin-zone integration with 64 k-points, and use a smearing of 0.12 eV in the spectral function. Evaluate the Kramers-Kronig transformation and compute the absorption coefficient for light polarizations parallel to the crystal axes (E||a, E||b, E||c). Extract the discrete absorption-band maxima (peak photon energies) in the energy range from 1 eV to 4.5 eV. Write the full set of peak energies, sorted in increasing order, to a JSON file.
- Output file: `/app/outputs/absorption_peaks.json`
- Format: json
- Contract: A JSON object with one key: `peaks`, containing a list of exactly 7 floating-point numbers. The numbers represent the seven defect-related absorption peak photon energies in eV, sorted in ascending order.
- Scoring: scored by hidden verifier

## Output files
- `/app/outputs/band_gap.json`
- `/app/outputs/in_gap_state.json`
- `/app/outputs/absorption_peaks.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gap.json
- path: `/app/outputs/band_gap.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed band gaps in eV for the perfect PbWO4 supercell and the defect supercell containing V_Pb^2-.
- schema:
  - `type`: object
  - `required`:
    - `perfect_gap_ev`: float
    - `defect_gap_ev`: float

### in_gap_state.json
- path: `/app/outputs/in_gap_state.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed energy in eV of the O 2p-derived in-gap state relative to the valence band maximum.
- schema:
  - `type`: object
  - `required`:
    - `in_gap_state_energy_ev`: float

### absorption_peaks.json
- path: `/app/outputs/absorption_peaks.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: List of seven computed absorption peak photon energies in eV, extracted from the 1–4.5 eV spectral range.
- schema:
  - `type`: object
  - `required`:
    - `peaks`: list of 7 floats, sorted ascending

Notes: All files must be placed in /app/outputs. The hidden verifier will check file existence, JSON validity, data types, array length, and compare reported values against a hidden reference.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gap.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "perfect_gap_ev": "float",
          "defect_gap_ev": "float"
        }
      },
      "description": "Computed band gaps in eV for the perfect PbWO4 supercell and the defect supercell containing V_Pb^2-."
    },
    {
      "file": "in_gap_state.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "in_gap_state_energy_ev": "float"
        }
      },
      "description": "Computed energy in eV of the O 2p-derived in-gap state relative to the valence band maximum."
    },
    {
      "file": "absorption_peaks.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "peaks": "list of 7 floats, sorted ascending"
        }
      },
      "description": "List of seven computed absorption peak photon energies in eV, extracted from the 1–4.5 eV spectral range."
    }
  ],
  "notes": "All files must be placed in /app/outputs. The hidden verifier will check file existence, JSON validity, data types, array length, and compare reported values against a hidden reference."
}
```

## How you are scored
A hidden verifier independently inspects each of the three scored output files. The verifier checks that each file has the correct format and contains the required fields. It then compares the reported numerical results against a hidden reference to evaluate accuracy. The three results are weighted to produce a final combined reward. The reproduction must execute the full DFT workflow to generate these results; the verifier's evaluation is not simply about matching pre-known values, but about demonstrating that the correct computational procedure has been followed.

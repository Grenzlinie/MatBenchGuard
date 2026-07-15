# First-principles study of N@C60 electronic and magnetic properties

## Problem background
The N@C60 molecule, where a single nitrogen atom is encapsulated inside a C60 fullerene cage, exhibits unusual electronic and magnetic properties because the N atom retains quasi-atomic states with unpaired electrons. Understanding how the magnetism, charge distribution, and transport behavior of N@C60 respond to external perturbations — such as carrier doping (adding or removing electrons), an applied electric field, chemical functionalization of the carbon cage, and adsorption on a metallic substrate — is important for potential applications in molecular electronics and quantum information. This task aims to compute these properties from first principles.

## Approach
The study uses spin‑polarized density functional theory (DFT) as implemented in the open‑source SIESTA code. The workflow involves: (i) building and optimizing the geometry of isolated C60 and N@C60, as well as charged states (anion and cation), two chemically functionalized derivatives (with C2NH5 and C3NH7 groups), and the molecule adsorbed on a Au(100) surface; (ii) extracting magnetic moments from the converged ground states; (iii) computing induced dipole moments under transverse electric fields to determine polarizabilities and quantify the cage shielding effect; and (iv) performing non‑equilibrium Green's function (NEGF) transport calculations on a two‑probe N@C60 junction with Au electrodes using the TranSIESTA module. All stages rely on standard Troullier‑Martins pseudopotentials and basis sets; no proprietary code is required.

## Reproduction target
Produce the following four scored artifacts from the DFT calculations:

1. **Magnetic moments** – total and, where applicable, atom‑resolved magnetic moments for six key N@C60 systems: pristine, anion, cation, C2NH5 derivative, C3NH7 derivative, and adsorbed on Au(100). Write the results to `magnetic_moments.json`.
2. **Off‑center displacement** – the distance by which the encapsulated N atom moves away from the cage centre in the C2NH5 derivative. Write it to `off_center_displacement.json`.
3. **Polarizability and shielding** – polarizabilities of the free C60 cage, free N atom, and N@C60, together with the derived shielding factor. Write them to `polarizability_shielding.json`.
4. **Transmission spectra** – spin‑up and spin‑down transmission coefficients for a N@C60 junction with Au electrodes, evaluated over the energy window −1 to +1 eV relative to the Fermi level. Write the curves to `transmission_energies.csv`.

All files must be placed under `/app/outputs` and conform to the formats and schemas specified in the workflow steps.

## Assets

- SIESTA (including TranSIESTA module): https://departments.icmab.es/leem/siesta/

## Workflow steps

### Step 1: Build and optimize C60 cage
- Role: process
- Action: Construct an Ih-symmetric C60 cage model and perform a spin-restricted geometry optimization using SIESTA within the LDA with a double-zeta polarized basis set.
- Evidence: `/app/outputs/c60_opt.log`

### Step 2: Build and optimize pristine N@C60
- Role: process
- Action: Insert an N atom at the center of the optimized C60 cage and perform a spin-polarized DFT geometry optimization, retaining Ih symmetry and ensuring the N atom remains at the cage center.
- Evidence: `/app/outputs/n_at_c60_opt.log`

### Step 3: Carrier doping: optimize N@C60 anion and cation
- Role: process
- Action: Starting from optimized N@C60, create the cation (+1 charge) and anion (−1 charge) configurations and perform spin-polarized geometry optimization for each.
- Evidence: `/app/outputs/n_at_c60_ion_opt.log`

### Step 4: Compute polarizabilities of free C60 cage and isolated N atom
- Role: process
- Action: For an isolated C60 cage and an isolated N atom, apply transverse electric fields of 0.05 V/Å and 0.5 V/Å along the x-axis in SIESTA, compute the induced dipole moments, and extract the polarizabilities α⊥.
- Evidence: `/app/outputs/polarizability_reference.log`

### Step 5: Compute polarizability of N@C60 under electric field
- Role: process
- Action: Apply the same transverse electric fields (0.05 V/Å and 0.5 V/Å) to the optimized N@C60 molecule, compute its induced dipole moment, and determine its polarizability α⊥.
- Evidence: `/app/outputs/n_at_c60_polar.log`

### Step 6: Optimize N@C60-C2NH5 derivative
- Role: process
- Action: Construct the N@C60-C2NH5 derivative by attaching a C2NH5 functional group to a cage carbon atom, then perform spin-polarized geometry optimization.
- Evidence: `/app/outputs/n_at_c60_c2nh5_opt.log`

### Step 7: Optimize N@C60-C3NH7 derivative
- Role: process
- Action: Construct the N@C60-C3NH7 derivative and perform spin-polarized geometry optimization; note the possible cage bond rupture and formation of an azo-bridge to the encapsulated N atom.
- Evidence: `/app/outputs/n_at_c60_c3nh7_opt.log`

### Step 8: Adsorb N@C60 on Au(100) surface and optimize
- Role: process
- Action: Construct a 4×4 Au(100) slab, place N@C60 in the most stable adsorption orientation (6-member ring on hollow/bridge site), and optimize the entire system with spin polarization.
- Evidence: `/app/outputs/n_at_c60_on_au100_opt.log`

### Step 9: Compute magnetic moments for all systems
- Role: scored (load-bearing)
- Action: For the six key systems (pristine N@C60, anion, cation, N@C60-C2NH5, N@C60-C3NH7, N@C60 on Au(100)), extract the spin-polarized ground-state total and atom-resolved magnetic moments. Write the results to magnetic_moments.json.
- Output file: `/app/outputs/magnetic_moments.json`
- Format: json
- Contract: Object with keys: pristine_N@C60, N@C60_anion, N@C60_cation, N@C60_C2NH5, N@C60_C3NH7, N@C60_on_Au100. Each value is an object with numeric fields total_moment (μB), n_atom_moment (μB or null), cage_moment (μB or null).
- Scoring: scored by hidden verifier

### Step 10: Compute off-center displacement for N@C60-C2NH5
- Role: scored
- Action: From the optimized geometry of N@C60-C2NH5, compute the distance of the N atom from the cage center (center of mass of carbon atoms). Write the result to off_center_displacement.json.
- Output file: `/app/outputs/off_center_displacement.json`
- Format: json
- Contract: Object with a single key displacement_A whose value is a float in Angstrom.
- Scoring: scored by hidden verifier

### Step 11: Compute shielding factor
- Role: scored
- Action: Using the polarizabilities obtained in the preceding steps, compute the shielding factor S = (α⊥(C60) + α⊥(N) − α⊥(N@C60)) / α⊥(N). Report the three polarizabilities and S in polarizability_shielding.json.
- Output file: `/app/outputs/polarizability_shielding.json`
- Format: json
- Contract: Object with numeric keys polarizability_N@C60, polarizability_C60, polarizability_N, shielding_factor.
- Scoring: scored by hidden verifier

### Step 12: Compute transport transmission spectra
- Role: scored
- Action: Set up a two-probe N@C60 molecular junction with Au(100) electrodes (including an STM-tip atom on the right electrode), perform NEGF-DFT transport calculation at zero bias using TranSIESTA, and extract spin-up and spin-down transmission coefficients over the energy window −1 to 1 eV relative to EF. Write the data to transmission_energies.csv.
- Output file: `/app/outputs/transmission_energies.csv`
- Format: csv
- Contract: CSV with columns energy_eV (float), transmission_up (float), transmission_down (float). At least 100 rows covering the energy range.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/magnetic_moments.json`
- `/app/outputs/off_center_displacement.json`
- `/app/outputs/polarizability_shielding.json`
- `/app/outputs/transmission_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### magnetic_moments.json
- path: `/app/outputs/magnetic_moments.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Spin‑polarized ground‑state total and atomic magnetic moments for all studied N@C60 systems.
- schema:
  - `type`: object
  - `description`: Magnetic moments for each system.
  - `systems`: `pristine_N@C60`, `N@C60_anion`, `N@C60_cation`, `N@C60_C2NH5`, `N@C60_C3NH7`, `N@C60_on_Au100`
  - `fields`:
    - `total_moment`: float (μB)
    - `n_atom_moment`: float (μB) or null
    - `cage_moment`: float (μB) or null

### off_center_displacement.json
- path: `/app/outputs/off_center_displacement.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Off‑center displacement of the encapsulated N atom in the C2NH5 derivative.
- schema:
  - `type`: object
  - `required`:
    - `displacement_A`: number

### polarizability_shielding.json
- path: `/app/outputs/polarizability_shielding.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Polarizability components and the derived shielding factor.
- schema:
  - `type`: object
  - `required`:
    - `polarizability_N@C60`: number
    - `polarizability_C60`: number
    - `polarizability_N`: number
    - `shielding_factor`: number

### transmission_energies.csv
- path: `/app/outputs/transmission_energies.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Spin‑dependent transmission spectra of the N@C60 molecular junction.
- schema:
  - `type`: table
  - `format`: csv
  - `required_columns`: `energy_eV`, `transmission_up`, `transmission_down`
  - `column_types`:
    - `energy_eV`: float
    - `transmission_up`: float
    - `transmission_down`: float
  - `min_rows`: 100
  - `note`: At least 100 points covering the energy range −1 to 1 eV relative to EF.

Notes: The checker validates schemas and recomputes metrics from raw artifacts. Tolerances and comparison rules are hidden. The absence of spin polarization is verified by computing the mean absolute difference between transmission_up and transmission_down.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "magnetic_moments.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "description": "Magnetic moments for each system.",
        "systems": [
          "pristine_N@C60",
          "N@C60_anion",
          "N@C60_cation",
          "N@C60_C2NH5",
          "N@C60_C3NH7",
          "N@C60_on_Au100"
        ],
        "fields": {
          "total_moment": "float (μB)",
          "n_atom_moment": "float (μB) or null",
          "cage_moment": "float (μB) or null"
        }
      },
      "description": "Spin‑polarized ground‑state total and atomic magnetic moments for all studied N@C60 systems."
    },
    {
      "file": "off_center_displacement.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "displacement_A": "number"
        }
      },
      "description": "Off‑center displacement of the encapsulated N atom in the C2NH5 derivative."
    },
    {
      "file": "polarizability_shielding.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "polarizability_N@C60": "number",
          "polarizability_C60": "number",
          "polarizability_N": "number",
          "shielding_factor": "number"
        }
      },
      "description": "Polarizability components and the derived shielding factor."
    },
    {
      "file": "transmission_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "format": "csv",
        "required_columns": [
          "energy_eV",
          "transmission_up",
          "transmission_down"
        ],
        "column_types": {
          "energy_eV": "float",
          "transmission_up": "float",
          "transmission_down": "float"
        },
        "min_rows": 100,
        "note": "At least 100 points covering the energy range −1 to 1 eV relative to EF."
      },
      "description": "Spin‑dependent transmission spectra of the N@C60 molecular junction."
    }
  ],
  "notes": "The checker validates schemas and recomputes metrics from raw artifacts. Tolerances and comparison rules are hidden. The absence of spin polarization is verified by computing the mean absolute difference between transmission_up and transmission_down."
}
```

## How you are scored
A hidden verifier will evaluate each scored output file separately. For each artifact the verifier checks that it exists, conforms to the required schema, and then compares the numerical results against reference values using appropriate hidden tolerances. The four artifacts are weighted as follows: magnetic moments 0.4, off‑center displacement 0.2, polarizability/shielding 0.2, and transmission spectra 0.2. The final reward is the weighted sum of the individual artifact scores. The tolerances account for legitimate differences that arise when recomputing the properties with a different implementation or slightly different settings; simply reporting the expected numbers without performing the required steps will not pass the structural and self‑consistency checks applied by the verifier.

# Ab initio phonons, elastic constants, and quasi-harmonic thermal expansion of trigonal framework crystal

## Problem background
H3[Co(CN)6] is a flexible trigonal framework material that exhibits anisotropic thermal expansion: positive expansion in the basal plane and negative expansion along the c-axis. Understanding the microscopic origin of this behaviour requires identifying the phonon modes that drive thermal expansion and quantifying their anharmonicity. The present task reproduces the ab initio DFT calculations that complement experimental Raman spectroscopy. The key quantities to compute are the zone‑center optical phonon frequencies with symmetry labels, the elastic constants, the mode Grüneisen parameters, and the volumetric thermal expansion coefficient. These results characterise the lattice dynamics and serve as direct indicators of the phonon contributions to negative thermal expansion.

## Approach
First-principles calculations are performed within density functional theory using the Perdew–Burke–Ernzerhof (PBE) exchange‑correlation functional and a plane‑wave basis set. The workflow begins from the published experimental trigonal structure (space group P‑31m). After a full structural relaxation, the elastic stiffness tensor is obtained through density functional perturbation theory. Zone‑centre phonon frequencies are computed (again via density functional perturbation theory or finite displacements), and their irreducible representations are determined by analysing the eigenvectors. To evaluate the anharmonic response, phonon frequencies are recalculated at several small volume changes around equilibrium, allowing the mode Grüneisen parameters to be fitted. The bulk modulus is extracted from an equation‑of‑state fit to total energies at different volumes. Finally, using these mode Grüneisen parameters together with the equilibrium frequencies, the bulk modulus, and the molar volume, the quasi‑harmonic volumetric thermal expansion coefficient at 300 K is evaluated (e.g., via the Einstein model).

## Reproduction target
Produce the following four artifacts for the trigonal H3[Co(CN)6] crystal:
- **Elastic constants**: independent components C11, C33, C44, C12, C13 (in GPa).
- **Zone‑center optical phonon frequencies**: a table listing each mode’s index, frequency (cm⁻¹), irreducible representation (A1g, Eg, A2u, Eu, A2g, or A1u), and a short descriptive label (e.g., “CN libration”, “CN stretching”).
- **Mode Grüneisen parameters**: a table giving each optical mode’s index, equilibrium frequency (cm⁻¹), and its Grüneisen parameter (dimensionless).
- **Volumetric thermal expansion coefficient at 300 K**: a single value in units of 10⁻⁶ K⁻¹, computed within the quasi‑harmonic approximation.
All files must be written to the paths specified in the Workflow Steps section.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Phonopy: phonopy
- SSSP efficiency pseudopotentials: https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: DFT structure relaxation
- Role: process
- Action: Using the published experimental trigonal structure (space group P-31m, a=6.4306 Å, c=5.7006 Å, with atomic positions from the literature), perform a full DFT relaxation to obtain the equilibrium lattice parameters and atomic coordinates. Use a PBE exchange-correlation functional.
- Evidence: `/app/outputs/relaxed_structure.log`

### Step 2: Elastic constants
- Role: scored
- Action: From the relaxed structure, compute the elastic stiffness tensor using density functional perturbation theory. Report the five independent elastic constants C11, C33, C44, C12, C13 in GPa.
- Output file: `/app/outputs/elastic_constants.txt`
- Format: txt
- Contract: Single line: C11 C33 C44 C12 C13
- Scoring: scored by hidden verifier

### Step 3: Equation of state and bulk modulus
- Role: process
- Action: Perform total energy calculations at several volumes around equilibrium (e.g., ±5% steps), fit the energy-volume data to a third-order Birch-Murnaghan equation of state, and extract the bulk modulus B0. Record the fitted B0 for use in the thermal expansion step.
- Evidence: `/app/outputs/eos_results.txt`

### Step 4: Zone-center phonon frequencies
- Role: scored
- Action: Using the relaxed structure, compute the phonon frequencies at the Γ point via density functional perturbation theory or finite displacements. For each optical mode, determine the irreducible representation by analyzing the eigenvectors. Output the mode index, frequency in cm⁻¹, symmetry label (e.g., A1g, Eg), and a short description (e.g., CN libration, CN stretching).
- Output file: `/app/outputs/zone_center_phonon_frequencies.txt`
- Format: csv
- Contract: CSV with columns: mode_index (int), frequency_cm1 (float), irrep (string), description (string).
- Scoring: scored by hidden verifier

### Step 5: Mode Grüneisen parameters
- Role: scored
- Action: Perform phonon calculations at small volume changes (e.g., ΔV = ±1% and ±2% of the equilibrium volume). For each optical mode at the zone center, compute the mode Grüneisen parameter γᵢ = −(V₀/ωᵢ) (Δωᵢ/ΔV) using a linear fit. Output the mode index, equilibrium frequency ωᵢ₀, and the corresponding Grüneisen parameter.
- Output file: `/app/outputs/mode_gruneisen_parameters.txt`
- Format: csv
- Contract: CSV with columns: mode_index (int), frequency_at_V0_cm1 (float), gruneisen_parameter (float).
- Scoring: scored by hidden verifier

### Step 6: Thermal expansion coefficient
- Role: scored (load-bearing)
- Action: Using the mode Grüneisen parameters, the equilibrium phonon frequencies, the bulk modulus B0 from the equation of state, and the molar volume, compute the volumetric thermal expansion coefficient at 300 K within the quasi-harmonic approximation (e.g., Einstein model average). Output the value α in 10⁻⁶ K⁻¹.
- Output file: `/app/outputs/thermal_expansion_coefficient.txt`
- Format: txt
- Contract: Single line: alpha (float) in 10⁻⁶ K⁻¹.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/elastic_constants.txt`
- `/app/outputs/zone_center_phonon_frequencies.txt`
- `/app/outputs/mode_gruneisen_parameters.txt`
- `/app/outputs/thermal_expansion_coefficient.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### elastic_constants.txt
- path: `/app/outputs/elastic_constants.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Elastic stiffness constants in Voigt notation, compared to the paper's DFT values.
- schema:
  - `type`: text
  - `description`: Single line with five space-separated floats: C11 C33 C44 C12 C13 (GPa)

### zone_center_phonon_frequencies.txt
- path: `/app/outputs/zone_center_phonon_frequencies.txt`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Zone-center optical phonon frequencies with irreducible representations and short descriptions. Compared to the paper's computed frequencies and symmetry labels.
- schema:
  - `type`: table
  - `required_columns`: `mode_index`, `frequency_cm1`, `irrep`, `description`
  - `units`:
    - `frequency_cm1`: cm⁻¹

### mode_gruneisen_parameters.txt
- path: `/app/outputs/mode_gruneisen_parameters.txt`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Mode Grüneisen parameters for all optical phonons. Compared to the paper's computed values, including sign checks for soft modes.
- schema:
  - `type`: table
  - `required_columns`: `mode_index`, `frequency_at_V0_cm1`, `gruneisen_parameter`
  - `units`:
    - `frequency_at_V0_cm1`: cm⁻¹
    - `gruneisen_parameter`: dimensionless

### thermal_expansion_coefficient.txt
- path: `/app/outputs/thermal_expansion_coefficient.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Volumetric thermal expansion coefficient at 300 K from the quasi-harmonic approximation, compared to the paper's DFT value.
- schema:
  - `type`: text
  - `description`: Single line: alpha (float) in 10⁻⁶ K⁻¹

Notes: All outputs are obtained from DFT and Phonopy runs on the trigonal P31m structure; no experimental data is required as input. The hidden gold values are the paper's reported DFT results from the corresponding tables.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "elastic_constants.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "description": "Single line with five space-separated floats: C11 C33 C44 C12 C13 (GPa)"
      },
      "description": "Elastic stiffness constants in Voigt notation, compared to the paper's DFT values."
    },
    {
      "file": "zone_center_phonon_frequencies.txt",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "mode_index",
          "frequency_cm1",
          "irrep",
          "description"
        ],
        "units": {
          "frequency_cm1": "cm⁻¹"
        }
      },
      "description": "Zone-center optical phonon frequencies with irreducible representations and short descriptions. Compared to the paper's computed frequencies and symmetry labels."
    },
    {
      "file": "mode_gruneisen_parameters.txt",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "mode_index",
          "frequency_at_V0_cm1",
          "gruneisen_parameter"
        ],
        "units": {
          "frequency_at_V0_cm1": "cm⁻¹",
          "gruneisen_parameter": "dimensionless"
        }
      },
      "description": "Mode Grüneisen parameters for all optical phonons. Compared to the paper's computed values, including sign checks for soft modes."
    },
    {
      "file": "thermal_expansion_coefficient.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "description": "Single line: alpha (float) in 10⁻⁶ K⁻¹"
      },
      "description": "Volumetric thermal expansion coefficient at 300 K from the quasi-harmonic approximation, compared to the paper's DFT value."
    }
  ],
  "notes": "All outputs are obtained from DFT and Phonopy runs on the trigonal P31m structure; no experimental data is required as input. The hidden gold values are the paper's reported DFT results from the corresponding tables."
}
```

## How you are scored
Your results will be evaluated by a hidden automated verifier. For each scored output file the verifier independently checks the computed quantities against reference values with tolerances that account for differences in DFT implementations and numerical settings. It will verify each elastic constant, each phonon frequency and its assigned symmetry, each mode Grüneisen parameter (including the sign), and the thermal expansion coefficient. The final reward is a weighted sum over all scored artifacts. Simply quoting the paper’s reported numbers without running the workflow will not receive a passing score; the verifier expects numbers that follow from an actual calculation on the described crystal structure.

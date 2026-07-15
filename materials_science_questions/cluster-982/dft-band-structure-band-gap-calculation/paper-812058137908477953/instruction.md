# First-Principles DFT and Lattice Dynamics Calculations for CdF₂

## Problem background
Cadmium fluoride (CdF₂) is an ionic crystal with the fluorite structure (space group Fm-3m) that is transparent in the visible/UV and becomes semiconducting upon doping. Its structural, elastic, electronic, and vibrational properties are important for fundamental solid-state physics and for applications. First-principles calculations based on density functional theory (DFT) provide a route to predict these properties without adjustable parameters. This task asks you to compute key ground-state properties of pure CdF₂ — equilibrium lattice constant, bulk modulus, cohesive energy, elastic constants, band gap, band-gap pressure coefficient, and optical phonon frequencies — using a standard DFT approach within the local density approximation (LDA) and norm-conserving pseudopotentials, combined with the direct method for lattice dynamics.

## Approach
The reproduction workflow uses the SIESTA code (LDA, Troullier-Martins norm-conserving pseudopotentials for Cd and F) to compute total energies, forces, and band structures, and the PHONON software (direct method) to obtain phonon frequencies. The conceptual stages are:
- Generate pseudopotentials and perform convergence tests for basis set, real-space cutoff, and k-point sampling.
- Compute the total energy vs. volume curve for the fluorite cell (Cd at (0,0,0), F at (1/4,1/4,1/4) and (3/4,3/4,3/4)) by relaxing internal coordinates under each volume.
- Fit the Murnaghan equation of state to the E(V) data to extract the equilibrium lattice constant, bulk modulus, its pressure derivative, and the cohesive energy (using isolated-atom energies).
- Calculate the band structure along high-symmetry lines at the equilibrium volume to determine the indirect band gap (valence band maximum at W, conduction band minimum at Γ).
- Repeat the band structure calculation under a hydrostatic pressure of about 8 GPa to obtain the linear pressure coefficient of the gap.
- Apply small strains to the equilibrium cell and analyse the total-energy changes to derive the second-order elastic constants C11, C12, C44 (energy-strain method).
- Construct a 2×2×2 supercell (96 atoms), introduce small atomic displacements, compute Hellmann-Feynman forces with SIESTA, and process the forces with PHONON to obtain the phonon dispersion. Extract the longitudinal (ω_LO) and transverse (ω_TO) optical mode frequencies at the Γ point.
- Compile all computed numbers into a single JSON file.

## Reproduction target
Produce exactly one scored file: `/app/outputs/results.json`. It must contain the following keys with numeric float values, computed for pure CdF₂ using the described DFT-LDA and phonon workflow:
- `lattice_constant_a0` (Å)
- `bulk_modulus_B` (GPa)
- `bulk_modulus_derivative_Bprime` (dimensionless)
- `cohesive_energy_Ecoh` (eV per formula unit)
- `elastic_constant_C11` (GPa)
- `elastic_constant_C12` (GPa)
- `elastic_constant_C44` (GPa)
- `band_gap_Eg` (eV, indirect gap)
- `band_gap_pressure_coefficient` (meV/GPa)
- `phonon_LO_frequency` (cm⁻¹)
- `phonon_TO_frequency` (cm⁻¹)
All values must be reported; no other files are scored.

## Assets

- SIESTA: https://siesta-project.gitlab.io/siesta/
- PHONON: http://wolf.ifj.edu.pl/phonon/

## Workflow steps

### Step 1: Generate norm-conserving pseudopotentials for Cd and F
- Role: process
- Action: Generate Troullier-Martins norm-conserving pseudopotentials for Cd (5s²4d¹⁰ configuration) and F (2s²2p⁵ configuration) with cutoff radii 2.40 a.u. and 1.20 a.u., respectively, for use in SIESTA LDA calculations.
- Evidence: `/app/outputs/pseudopotential_files.txt`

### Step 2: Convergence tests for basis set, cutoff, and k-point sampling
- Role: process
- Action: Determine optimal DZP basis, real-space energy cutoff, k-point mesh, and force tolerance to achieve total energy convergence better than 1 meV/atom for CdF₂. Document the converged parameters.
- Evidence: `/app/outputs/convergence_log.txt`

### Step 3: Compute total energy vs. volume for CdF₂
- Role: process
- Action: Using the fluorite structure (Fm‑3m, Cd at (0,0,0), F at (1/4,1/4,1/4) and (3/4,3/4,3/4)), compute DFT total energies for a series of lattice constants (varying volume). Relax atomic positions under each volume until forces < 0.003 eV/Å. Produce the E(V) data set.
- Evidence: `/app/outputs/energy_vs_volume.csv`

### Step 4: Fit Murnaghan equation of state and extract equilibrium properties
- Role: process
- Action: Fit the E(V) points to Murnaghan's equation of state to obtain equilibrium lattice constant, bulk modulus, and its pressure derivative. Compute cohesive energy from total energies of the solid and isolated atoms.
- Evidence: `/app/outputs/eos_fit_results.txt`

### Step 5: Compute equilibrium band structure and indirect band gap
- Role: process
- Action: Perform a DFT band structure calculation along high‑symmetry directions using the equilibrium lattice constant. Identify valence band maximum (at W) and conduction band minimum (at Γ) to obtain the indirect band gap.
- Evidence: `/app/outputs/band_structure.dat`

### Step 6: Compute band gap pressure coefficient
- Role: process
- Action: Repeat the band structure calculation under a hydrostatic pressure of about 8 GPa (or a set of pressures) and determine the linear pressure coefficient dEg/dP (meV/GPa).
- Evidence: `/app/outputs/pressure_gap_vs_P.csv`

### Step 7: Compute ambient-pressure elastic constants C11, C12, C44
- Role: process
- Action: Apply appropriate strain patterns (e.g., volumetric and orthorhombic strains) to the equilibrium cell and compute resulting total energy changes. Solve for the second‑order elastic constants C11, C12, C44 at ambient pressure using the energy‑strain method.
- Evidence: `/app/outputs/elastic_energies.csv`

### Step 8: Compute optical phonon frequencies at Γ
- Role: process
- Action: Build a 2×2×2 supercell (96 atoms), introduce small atomic displacements (±0.03 Å), compute Hellmann‑Feynman forces with SIESTA, and process the forces with the PHONON software to obtain phonon dispersion. Extract the longitudinal (ω_LO) and transverse (ω_TO) optical mode frequencies at the Γ point.
- Evidence: `/app/outputs/phonon_dispersion.dat`

### Step 9: Compile and output all requested properties
- Role: scored (load-bearing)
- Action: Collect the values computed in the previous stages and write them into a single JSON file with the keys: lattice_constant_a0 (Å), bulk_modulus_B (GPa), bulk_modulus_derivative_Bprime, cohesive_energy_Ecoh (eV per formula unit), elastic_constant_C11 (GPa), elastic_constant_C12 (GPa), elastic_constant_C44 (GPa), band_gap_Eg (eV), band_gap_pressure_coefficient (meV/GPa), phonon_LO_frequency (cm⁻¹), phonon_TO_frequency (cm⁻¹). All values must be numeric floats.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {
  "lattice_constant_a0": <float>,
  "bulk_modulus_B": <float>,
  "bulk_modulus_derivative_Bprime": <float>,
  "cohesive_energy_Ecoh": <float>,
  "elastic_constant_C11": <float>,
  "elastic_constant_C12": <float>,
  "elastic_constant_C44": <float>,
  "band_gap_Eg": <float>,
  "band_gap_pressure_coefficient": <float>,
  "phonon_LO_frequency": <float>,
  "phonon_TO_frequency": <float>
}
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
- target_policy: exact_match
- description: Compiled reproduction target: structural, elastic, electronic, and vibrational properties computed from the first-principles DFT and lattice dynamics pipeline. The checker compares each field to hidden paper-reported values with per‑field tolerances.
- schema:
  - `type`: object
  - `required`: `lattice_constant_a0`, `bulk_modulus_B`, `bulk_modulus_derivative_Bprime`, `cohesive_energy_Ecoh`, `elastic_constant_C11`, `elastic_constant_C12`, `elastic_constant_C44`, `band_gap_Eg`, `band_gap_pressure_coefficient`, `phonon_LO_frequency`, `phonon_TO_frequency`
  - `properties`:
    - `lattice_constant_a0`:
      - `type`: number
      - `unit`: Å
    - `bulk_modulus_B`:
      - `type`: number
      - `unit`: GPa
    - `bulk_modulus_derivative_Bprime`:
      - `type`: number
      - `unit`: dimensionless
    - `cohesive_energy_Ecoh`:
      - `type`: number
      - `unit`: eV per formula unit
    - `elastic_constant_C11`:
      - `type`: number
      - `unit`: GPa
    - `elastic_constant_C12`:
      - `type`: number
      - `unit`: GPa
    - `elastic_constant_C44`:
      - `type`: number
      - `unit`: GPa
    - `band_gap_Eg`:
      - `type`: number
      - `unit`: eV
    - `band_gap_pressure_coefficient`:
      - `type`: number
      - `unit`: meV/GPa
    - `phonon_LO_frequency`:
      - `type`: number
      - `unit`: cm⁻¹
    - `phonon_TO_frequency`:
      - `type`: number
      - `unit`: cm⁻¹

Notes: Pressure‑dependent elastic constants and derived elastic moduli (anisotropy factor, Poisson ratio, Young’s modulus) are explicitly excluded from the scored target.

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
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "lattice_constant_a0",
          "bulk_modulus_B",
          "bulk_modulus_derivative_Bprime",
          "cohesive_energy_Ecoh",
          "elastic_constant_C11",
          "elastic_constant_C12",
          "elastic_constant_C44",
          "band_gap_Eg",
          "band_gap_pressure_coefficient",
          "phonon_LO_frequency",
          "phonon_TO_frequency"
        ],
        "properties": {
          "lattice_constant_a0": {
            "type": "number",
            "unit": "Å"
          },
          "bulk_modulus_B": {
            "type": "number",
            "unit": "GPa"
          },
          "bulk_modulus_derivative_Bprime": {
            "type": "number",
            "unit": "dimensionless"
          },
          "cohesive_energy_Ecoh": {
            "type": "number",
            "unit": "eV per formula unit"
          },
          "elastic_constant_C11": {
            "type": "number",
            "unit": "GPa"
          },
          "elastic_constant_C12": {
            "type": "number",
            "unit": "GPa"
          },
          "elastic_constant_C44": {
            "type": "number",
            "unit": "GPa"
          },
          "band_gap_Eg": {
            "type": "number",
            "unit": "eV"
          },
          "band_gap_pressure_coefficient": {
            "type": "number",
            "unit": "meV/GPa"
          },
          "phonon_LO_frequency": {
            "type": "number",
            "unit": "cm⁻¹"
          },
          "phonon_TO_frequency": {
            "type": "number",
            "unit": "cm⁻¹"
          }
        }
      },
      "description": "Compiled reproduction target: structural, elastic, electronic, and vibrational properties computed from the first-principles DFT and lattice dynamics pipeline. The checker compares each field to hidden paper-reported values with per‑field tolerances."
    }
  ],
  "notes": "Pressure‑dependent elastic constants and derived elastic moduli (anisotropy factor, Poisson ratio, Young’s modulus) are explicitly excluded from the scored target."
}
```

## How you are scored
A hidden verifier loads your `/app/outputs/results.json` and checks that all required keys are present and numeric. It then compares each of your reported values to a hidden reference (the paper’s own computed values) using per‑field tolerances that account for legitimate differences arising from DFT‑LDA toolchain spread (different SIESTA builds, compiler optimizations, k‑mesh details, etc.). The total reward is a float between 0.0 and 1.0, proportional to the fraction of quantities that fall within their tolerance windows. You do not need to guess the exact reference numbers, but your results must be obtained by genuinely executing the described DFT and phonon pipeline; a prior guess or arbitrary numbers are unlikely to pass all tolerances.

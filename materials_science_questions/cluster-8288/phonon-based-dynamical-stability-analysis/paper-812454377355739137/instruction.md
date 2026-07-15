# Cubic Graphene Phonon Transport and Raman Frequencies

## Problem background
Cubic graphene is a three-dimensional carbon allotrope in which every carbon atom is sp2-hybridized, forming a hollow network. Unlike diamond (sp3) or graphite (sp2 sheets), this structure combines purely sp2 bonding with a three-dimensional framework. Because of its unique bonding and geometry, its thermal transport properties are fundamentally different from other carbon allotropes and are important for potential applications in thermal management. This task asks you to compute the lattice thermal conductivity of cubic graphene at room temperature (300 K) and the frequencies of its Raman-active phonon modes, which serve as experimental fingerprints, using first-principles phonon calculations.

## Approach
The central idea is to use density functional theory (DFT) with the GGA-PBE exchange-correlation functional to calculate the interatomic forces, then extract harmonic (second-order) and anharmonic (third-order) force constants via finite-displacement supercell methods. The harmonic force constants yield the phonon dispersion and Raman spectrum, from which the three Raman-active mode frequencies (T2g, A1g, Eg) are identified. The harmonic and anharmonic force constants together are fed into the phonon Boltzmann transport equation (PBTE) solver to obtain the lattice thermal conductivity. Because the material is cubic, the thermal conductivity is isotropic; the value along any crystal direction (e.g., xx) is the target. The computational workflow proceeds from structure optimization through harmonic and anharmonic force-constant calculations to the final Raman and thermal-conductivity results.

## Reproduction target
Using the crystal structure parameters provided (space group Pn-3m, lattice constant 6.095 Å, Wyckoff position (–0.25000, 0.41328, 0.08672)), perform a first-principles DFT geometry optimization to obtain the relaxed cell and atomic coordinates. From the optimized structure, compute the second-order harmonic force constants and the phonon dispersion. Using the same supercell, compute the third-order anharmonic force constants. Then solve the phonon Boltzmann transport equation to obtain the lattice thermal conductivity at 300 K and write the result to `/app/outputs/thermal_conductivity_300K.json`. Additionally, compute the Raman spectrum from the harmonic force constants and extract the frequencies of the three Raman-active modes (T2g, A1g, Eg); write these frequencies to `/app/outputs/raman_active_frequencies.json`. The output JSON schemas are specified in the workflow steps.

## Assets

- Cubic graphene crystal structure
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PHONOPY: https://phonopy.github.io/phonopy/
- phono3py: https://phonopy.github.io/phono3py/
- ShengBTE: https://www.shengbt.com/
- Carbon pseudopotentials (GGA-PBE): https://www.materialscloud.org/sssp/
- qe2shengBTE (utility): https://www.shengbt.com/

## Workflow steps

### Step 1: Structure optimization of cubic graphene
- Role: process
- Action: Optimize the cubic graphene crystal structure using DFT (GGA-PBE) starting from the provided space group, lattice constant, and Wyckoff positions. Relax atomic positions and cell parameters until convergence.
- Evidence: `/app/outputs/optimization.log`

### Step 2: Harmonic force constants and phonon dispersion
- Role: process
- Action: Using the optimized structure, generate a supercell and perform DFT calculations to compute the second-order interatomic force constants and phonon dispersion via PHONOPY.
- Evidence: `/app/outputs/FORCE_CONSTANTS`

### Step 3: Raman-active mode frequencies
- Role: scored
- Action: Compute the Raman spectrum of cubic graphene from the second-order force constants using Phonopy-Spectroscopy or equivalent. Identify the three Raman-active modes (T2g, A1g, Eg) and extract their frequencies. Write the frequencies to raman_active_frequencies.json.
- Output file: `/app/outputs/raman_active_frequencies.json`
- Format: json
- Contract: {
  "T2g_frequency": <float>,
  "A1g_frequency": <float>,
  "Eg_frequency": <float>,
  "unit": "cm^-1"
}
- Scoring: scored by hidden verifier

### Step 4: Anharmonic (third-order) force constants
- Role: process
- Action: Using phono3py and DFT, compute the third-order interatomic force constants for cubic graphene on the supercell. Apply translational invariance constraints as needed.
- Evidence: `/app/outputs/THIRD_ORDER_IFC`

### Step 5: Lattice thermal conductivity at 300 K
- Role: scored (load-bearing)
- Action: Using the second-order and third-order force constants and a sufficiently dense q-grid, run ShengBTE to solve the phonon Boltzmann equation and obtain the lattice thermal conductivity at 300 K. Write the value to thermal_conductivity_300K.json.
- Output file: `/app/outputs/thermal_conductivity_300K.json`
- Format: json
- Contract: {
  "thermal_conductivity_300K": {
    "value": <float>,
    "unit": "W/mK"
  }
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/raman_active_frequencies.json`
- `/app/outputs/thermal_conductivity_300K.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### raman_active_frequencies.json
- path: `/app/outputs/raman_active_frequencies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Frequencies of the three Raman-active phonon modes of cubic graphene: T2g, A1g, Eg. Each in cm^-1.
- schema:
  - `type`: object
  - `required`: `T2g_frequency`, `A1g_frequency`, `Eg_frequency`, `unit`
  - `properties`:
    - `T2g_frequency`: float
    - `A1g_frequency`: float
    - `Eg_frequency`: float
    - `unit`: string (cm^-1)

### thermal_conductivity_300K.json
- path: `/app/outputs/thermal_conductivity_300K.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Lattice thermal conductivity of cubic graphene at 300 K, given as a value in W/mK.
- schema:
  - `type`: object
  - `required`: `thermal_conductivity_300K`
  - `properties`:
    - `thermal_conductivity_300K`:
      - `type`: object
      - `required`: `value`, `unit`
      - `properties`:
        - `value`: float
        - `unit`: string (W/mK)

Notes: Scored via result-level comparison against hidden paper values with tolerances (exact_match policy). Only the two specified artifacts are scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "raman_active_frequencies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "T2g_frequency",
          "A1g_frequency",
          "Eg_frequency",
          "unit"
        ],
        "properties": {
          "T2g_frequency": "float",
          "A1g_frequency": "float",
          "Eg_frequency": "float",
          "unit": "string (cm^-1)"
        }
      },
      "description": "Frequencies of the three Raman-active phonon modes of cubic graphene: T2g, A1g, Eg. Each in cm^-1."
    },
    {
      "file": "thermal_conductivity_300K.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "thermal_conductivity_300K"
        ],
        "properties": {
          "thermal_conductivity_300K": {
            "type": "object",
            "required": [
              "value",
              "unit"
            ],
            "properties": {
              "value": "float",
              "unit": "string (W/mK)"
            }
          }
        }
      },
      "description": "Lattice thermal conductivity of cubic graphene at 300 K, given as a value in W/mK."
    }
  ],
  "notes": "Scored via result-level comparison against hidden paper values with tolerances (exact_match policy). Only the two specified artifacts are scored."
}
```

## How you are scored
A hidden verifier will read your two JSON output files and compare your reported values to reference values. For the Raman frequencies, each of the three mode frequencies is compared individually and scored based on how close it is to the expected reference; full credit requires matching within an acceptable tolerance. For the thermal conductivity, the reported 300 K value is compared analogously and scored based on closeness. The final reward is the average of the Raman score and the thermal-conductivity score, each weighted equally (0.5). Reporting a number is not enough; the verifier only awards credit when the values fall within the expected tolerance, so your computed results must be accurate.

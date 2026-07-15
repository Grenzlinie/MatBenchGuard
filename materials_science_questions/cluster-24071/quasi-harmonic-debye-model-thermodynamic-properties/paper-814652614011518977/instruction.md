# Cu2GeSe3 phonon and thermodynamic properties from DFT and QHA

## Problem background
Cu₂GeSe₃ is a Cu‑based diamond‑like chalcogenide semiconductor with promising thermoelectric properties. Its low lattice thermal conductivity is central to its performance, but the origin of this low conductivity—whether from strong bonding anharmonicity or from other factors such as weak covalent bonding—remains an open question. Understanding the lattice dynamics and thermodynamic behaviour is essential to clarify this. First‑principles calculations based on density functional theory can provide phonon frequencies, heat capacity, elastic constants, thermal expansion, the Grüneisen parameter, and the lattice thermal conductivity, thereby offering microscopic insight into the heat‑transport mechanisms in this material.

## Approach
The workflow uses plane‑wave density functional theory with the Perdew‑Burke‑Ernzerhof (PBE) exchange‑correlation functional. The crystal structure is first relaxed to its equilibrium lattice parameters. Phonon dispersions are obtained via the finite‑displacement supercell method, using Phonopy for post‑processing and symmetry analysis. The quasi‑harmonic approximation (QHA) is then employed: phonons are computed at several isotropically strained volumes, and the volume‑dependent total energies and phonon frequencies are used to derive an equation of state. From these, the isometric heat capacity, bulk modulus, linear thermal expansion coefficient, mode‑averaged Grüneisen parameter, and lattice thermal conductivity are evaluated at a temperature of 300 K. The lattice thermal conductivity is estimated via Slack’s formula, which requires the Debye temperature (computed from the phonon spectrum), the average atomic mass, the volume per atom, and a constant A = 3.1 × 10⁻⁶ (in units of W·m⁻¹·K⁻¹, amu, and angstroms). The Young’s modulus is deduced from the bulk modulus by assuming a Poisson’s ratio (e.g., ν = 0.33).

## Reproduction target
Starting from the experimental crystal structure of Cu₂GeSe₃ (space group Imm2), perform a DFT‑PBE relaxation, build a supercell, compute phonon frequencies at several volumes, and extract the following:

- At the equilibrium volume, list the 15 optical Γ‑point phonon frequencies and assign each mode a symmetry label (A₁, A₂, B₁, B₂) under the C₂ᵥ point group.
- Within the quasi‑harmonic approximation and using the volume‑dependent phonon data, compute at 300 K: the isometric heat capacity Cv (J g⁻¹ K⁻¹), Young’s modulus E (GPa), linear thermal expansion coefficient β (10⁻⁶ K⁻¹), mode‑averaged Grüneisen parameter γ, and lattice thermal conductivity κL (W m⁻¹ K⁻¹).

Write the phonon data to `step_01_phonon_frequencies.json` and the thermodynamic properties to `step_02_thermodynamic_properties.json`, following the formats specified in the output contract.

## Assets

- Crystal structure of Cu2GeSe3 (Imm2): 10.1016/j.ssc.2008.01.032
- DFT code with PBE functional and plane-wave basis: https://www.quantum-espresso.org/
- Phonopy: https://phonopy.github.io/phonopy/

## Workflow steps

### Step 1: Structure relaxation and preparation of strained volumes
- Role: process
- Action: Relax the crystal structure of Cu2GeSe3 (space group Imm2) using DFT with PBE functional, obtaining equilibrium lattice parameters and atomic positions. Then generate a set of isotropically strained structures for subsequent quasi-harmonic calculations.
- Evidence: none

### Step 2: DFT force calculations and phonon dispersions at each volume
- Role: process
- Action: For each strained structure, compute forces via DFT supercell calculations (72-atom cell), then use Phonopy to obtain phonon dispersions, including Gamma-point frequencies.
- Evidence: none

### Step 3: Extract Raman frequencies and symmetry assignments
- Role: scored
- Action: From the equilibrium-volume phonon calculation, extract the 15 optical Gamma-point frequencies, classify them by C2v symmetry (A1, A2, B1, B2), and write the result.
- Output file: `/app/outputs/step_01_phonon_frequencies.json`
- Format: json
- Contract: Array of objects, each with fields: mode_index (int), symmetry (string: A1, A2, B1, B2), frequency_cm-1 (float).
- Scoring: scored by hidden verifier

### Step 4: Compute thermodynamic properties at 300 K
- Role: scored (load-bearing)
- Action: Within the quasi-harmonic approximation and using the phonon frequencies and equation-of-state, compute the isometric heat capacity Cv, Young's modulus E, linear thermal expansion coefficient beta, mode-averaged Gruneisen parameter gamma, and lattice thermal conductivity kappa_L via Slack's formula (constant A=3.1e-6) at 300 K. Write the results.
- Output file: `/app/outputs/step_02_thermodynamic_properties.json`
- Format: json
- Contract: JSON object with keys: heat_capacity_Cv_JgK (float), young_modulus_E_GPa (float), thermal_expansion_beta_10-6perK (float), gruneisen_parameter (float), lattice_thermal_conductivity_kappa_L_WmK (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_phonon_frequencies.json`
- `/app/outputs/step_02_thermodynamic_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_phonon_frequencies.json
- path: `/app/outputs/step_01_phonon_frequencies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Gamma-point optical phonon frequencies and symmetry assignments of Cu2GeSe3.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `mode_index`, `symmetry`, `frequency_cm-1`
    - `properties`:
      - `mode_index`:
        - `type`: integer
      - `symmetry`:
        - `type`: string
        - `enum`: `A1`, `A2`, `B1`, `B2`
      - `frequency_cm-1`:
        - `type`: number
  - `minItems`: 15
  - `maxItems`: 15

### step_02_thermodynamic_properties.json
- path: `/app/outputs/step_02_thermodynamic_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Thermodynamic properties at 300 K from the quasi-harmonic approximation and Slack's formula.
- schema:
  - `type`: object
  - `required`: `heat_capacity_Cv_JgK`, `young_modulus_E_GPa`, `thermal_expansion_beta_10-6perK`, `gruneisen_parameter`, `lattice_thermal_conductivity_kappa_L_WmK`
  - `properties`:
    - `heat_capacity_Cv_JgK`:
      - `type`: number
    - `young_modulus_E_GPa`:
      - `type`: number
    - `thermal_expansion_beta_10-6perK`:
      - `type`: number
    - `gruneisen_parameter`:
      - `type`: number
    - `lattice_thermal_conductivity_kappa_L_WmK`:
      - `type`: number

Notes: All values correspond to 300 K. The Young's modulus is derived from the computed bulk modulus and an assumed Poisson's ratio. The lattice thermal conductivity uses Slack's formula with A = 3.1e-6.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_phonon_frequencies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "mode_index",
            "symmetry",
            "frequency_cm-1"
          ],
          "properties": {
            "mode_index": {
              "type": "integer"
            },
            "symmetry": {
              "type": "string",
              "enum": [
                "A1",
                "A2",
                "B1",
                "B2"
              ]
            },
            "frequency_cm-1": {
              "type": "number"
            }
          }
        },
        "minItems": 15,
        "maxItems": 15
      },
      "description": "Gamma-point optical phonon frequencies and symmetry assignments of Cu2GeSe3."
    },
    {
      "file": "step_02_thermodynamic_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "heat_capacity_Cv_JgK",
          "young_modulus_E_GPa",
          "thermal_expansion_beta_10-6perK",
          "gruneisen_parameter",
          "lattice_thermal_conductivity_kappa_L_WmK"
        ],
        "properties": {
          "heat_capacity_Cv_JgK": {
            "type": "number"
          },
          "young_modulus_E_GPa": {
            "type": "number"
          },
          "thermal_expansion_beta_10-6perK": {
            "type": "number"
          },
          "gruneisen_parameter": {
            "type": "number"
          },
          "lattice_thermal_conductivity_kappa_L_WmK": {
            "type": "number"
          }
        }
      },
      "description": "Thermodynamic properties at 300 K from the quasi-harmonic approximation and Slack's formula."
    }
  ],
  "notes": "All values correspond to 300 K. The Young's modulus is derived from the computed bulk modulus and an assumed Poisson's ratio. The lattice thermal conductivity uses Slack's formula with A = 3.1e-6."
}
```

## How you are scored
Each scored output file is independently evaluated by a hidden verifier. The verifier compares the computed phonon frequencies (and their symmetry assignments) and the thermodynamic quantities against expected reference values, using tolerances appropriate for first‑principles reproducibility (accounting for differences in pseudopotentials, basis sets, and implementation details). The final reward is a weighted combination of the scores across the two stages, with the thermodynamic properties carrying a higher weight. Simply reporting known literature numbers without executing the workflow will not receive credit; the verifier expects the results to originate from a genuine DFT‑QHA calculation.

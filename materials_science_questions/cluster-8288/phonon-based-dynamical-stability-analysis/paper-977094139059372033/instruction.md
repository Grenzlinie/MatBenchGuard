# DFT total energy and phonon stability analysis of bilayer nickelate compounds

## Problem background
The discovery of superconductivity in bilayer nickelates under high pressure has motivated the search for candidate materials that are stable in the high-symmetry tetragonal (I4/mmm) phase at ambient or low pressure, as the suppression of octahedral rotation is believed to be crucial for superconductivity. Three compounds—Ac3Ni2O7, La2BaNi2O6F, and La2SrNi2O6F—were theoretically studied to determine their structural stability relative to the distorted orthorhombic (Amam) phase. The task is to assess the energetic and dynamical stability of these candidate compounds by computing their relative total energies and phonon dispersion properties using first-principles calculations.

## Approach
Density functional theory (DFT) calculations are performed with the plane‑wave code Quantum ESPRESSO and standard solid‑state pseudopotentials (SSSP efficiency). For each compound, total energies of the I4/mmm and Amam crystal structures are computed in several magnetic configurations: nonmagnetic (NM), ferromagnetic (FM), and three antiferromagnetic arrangements (A‑AF, G‑AF, C‑AF). Calculations are carried out at ambient pressure (0 GPa) and, for La2SrNi2O6F, also at a modest applied pressure (4 GPa); the Amam structure may relax to I4/mmm under pressure. Phonon dispersions are then calculated for the I4/mmm phases using the Phonopy package, and the presence or absence of imaginary (negative‑frequency) phonon modes is recorded. The results are compiled to obtain relative energies (in meV per formula unit) with respect to the nonmagnetic Amam phase and output as a single JSON artifact.

## Reproduction target
Using only publicly available tools, compute and output in a file `/app/outputs/results.json` the relative total energies (meV/f.u.) and imaginary‑phonon‑mode flags for the three compounds, pressures, phases, and magnetic states as detailed in the workflow steps. This includes: for Ac3Ni2O7 and La2BaNi2O6F at 0 GPa, I4/mmm entries in NM, FM, A‑AF, G‑AF, C‑AF states plus an Amam NM reference; for La2SrNi2O6F at 0 GPa, both I4/mmm (all magnetic states) and Amam NM; for La2SrNi2O6F at 4 GPa, only I4/mmm entries (the Amam phase relaxes to I4/mmm) with NM relative energy set to 0.0. All I4/mmm entries must include a boolean `imaginary_modes` field indicating whether imaginary phonon modes are present; Amam entries must omit this field. The output must be a JSON array with at least 30 entries following the schema in the output contract.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Phonopy: https://phonopy.github.io/phonopy/
- SSSP efficiency pseudopotentials: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Generate crystal structures and DFT input files
- Role: process
- Action: From the chemical formulas Ac3Ni2O7, La2BaNi2O6F, La2SrNi2O6F, construct initial crystal structures for the I4/mmm and Amam phases, assign lattice parameters and atomic positions, and create Quantum ESPRESSO input files for all required calculations (including pressure settings).
- Evidence: `/app/outputs/structure_preparation.log`

### Step 2: DFT total-energy calculations
- Role: process
- Action: Run Quantum ESPRESSO to perform total-energy calculations for each compound, phase, pressure, and magnetic configuration. For Ac3Ni2O7 and La2BaNi2O6F at ambient pressure, compute energies of I4/mmm in NM, FM, A-AF, G-AF, C-AF and of Amam in NM. For La2SrNi2O6F at 0 GPa, same; at 4 GPa, relax the Amam structure (which should reduce to I4/mmm) and compute energies of I4/mmm in all magnetic states. Extract total energies per formula unit.
- Evidence: `/app/outputs/dft_energies.json`

### Step 3: Phonon dispersion calculations
- Role: process
- Action: Using the relaxed I4/mmm structures from the DFT step, compute phonon dispersions with Phonopy for each compound at the relevant pressures: Ac3Ni2O7 at ambient, La2BaNi2O6F at ambient, La2SrNi2O6F at ambient and at 4 GPa. Record whether any imaginary (negative-frequency) modes exist along high-symmetry paths.
- Evidence: `/app/outputs/phonon_modes.json`

### Step 4: Compile final reproduction results
- Role: scored (load-bearing)
- Action: Collect the total energies from DFT step. For each compound/pressure scenario, compute relative energies (in meV/f.u.) with respect to the nonmagnetic Amam phase energy. If the Amam phase relaxed to I4/mmm, set the NM I4/mmm entry relative_energy=0.0. For each I4/mmm phonon calculation, report imaginary_modes (true/false). Output a single JSON file at /app/outputs/results.json following the schema below.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON array of objects. Each object has keys: compound (string: Ac3Ni2O7, La2BaNi2O6F, La2SrNi2O6F), pressure (float: 0.0 or 4.0), phase (string: I4/mmm or Amam), magnetic_state (string: NM, FM, A-AF, G-AF, C-AF), relative_energy_meV (float), imaginary_modes (boolean, only for I4/mmm entries; absent for Amam entries). For La2SrNi2O6F at 0 GPa, both I4/mmm (all magnetic states) and Amam (NM) entries must be present; at 4 GPa, only I4/mmm entries. For Ac3Ni2O7 and La2BaNi2O6F at 0 GPa, I4/mmm entries with imaginary_modes, and a single Amam NM entry (no imaginary_modes field). All relative energies are computed w.r.t. the NM Amam energy per formula unit.
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
- description: Reproduced relative total energies, phonon stability flags, magnetic moments, Δ_{z^2} splitting, and inter-layer coupling J⊥ S².
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `compound`, `pressure`, `phase`, `magnetic_state`, `relative_energy_meV`
    - `properties`:
      - `compound`:
        - `type`: string
        - `enum`: `Ac3Ni2O7`, `La2BaNi2O6F`, `La2SrNi2O6F`
      - `pressure`:
        - `type`: number
        - `enum`: `0.0`, `4.0`
      - `phase`:
        - `type`: string
        - `enum`: `I4/mmm`, `Amam`
      - `magnetic_state`:
        - `type`: string
        - `enum`: `NM`, `FM`, `A-AF`, `G-AF`, `C-AF`
      - `relative_energy_meV`:
        - `type`: number
      - `imaginary_modes`:
        - `type`: boolean
        - `description`: Only present for entries with phase=I4/mmm
      - `magnetic_moment_per_Ni_muB`:
        - `type`: number
        - `description`: Magnetic moment per Ni atom in μB; only present for I4/mmm entries with magnetic_state ≠ NM
      - `delta_z2_eV`:
        - `type`: number
        - `description`: Δ_{z^2} splitting in eV; optional, only for selected NM I4/mmm entries
      - `J_perp_S2_meV`:
        - `type`: number
        - `description`: Inter-layer magnetic coupling J⊥ S² in meV; optional, only for C-AF I4/mmm entries of applicable compounds
  - `minItems`: 30
  - `description`: Array of results for all compound/pressure/phase/magnetic combinations, augmented with optional electronic and coupling parameters.

Notes: Magnetic moments, Δ_{z^2} and J⊥ S² values are incorporated into the single results.json artifact to cover the paper's main billed quantities. The spin susceptibility and qualitative band-structure similarity are not scored as they lack a single scalar gold (D7).

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
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "compound",
            "pressure",
            "phase",
            "magnetic_state",
            "relative_energy_meV"
          ],
          "properties": {
            "compound": {
              "type": "string",
              "enum": [
                "Ac3Ni2O7",
                "La2BaNi2O6F",
                "La2SrNi2O6F"
              ]
            },
            "pressure": {
              "type": "number",
              "enum": [
                0.0,
                4.0
              ]
            },
            "phase": {
              "type": "string",
              "enum": [
                "I4/mmm",
                "Amam"
              ]
            },
            "magnetic_state": {
              "type": "string",
              "enum": [
                "NM",
                "FM",
                "A-AF",
                "G-AF",
                "C-AF"
              ]
            },
            "relative_energy_meV": {
              "type": "number"
            },
            "imaginary_modes": {
              "type": "boolean",
              "description": "Only present for entries with phase=I4/mmm"
            },
            "magnetic_moment_per_Ni_muB": {
              "type": "number",
              "description": "Magnetic moment per Ni atom in μB; only present for I4/mmm entries with magnetic_state ≠ NM"
            },
            "delta_z2_eV": {
              "type": "number",
              "description": "Δ_{z^2} splitting in eV; optional, only for selected NM I4/mmm entries"
            },
            "J_perp_S2_meV": {
              "type": "number",
              "description": "Inter-layer magnetic coupling J⊥ S² in meV; optional, only for C-AF I4/mmm entries of applicable compounds"
            }
          }
        },
        "minItems": 30,
        "description": "Array of results for all compound/pressure/phase/magnetic combinations, augmented with optional electronic and coupling parameters."
      },
      "description": "Reproduced relative total energies, phonon stability flags, magnetic moments, Δ_{z^2} splitting, and inter-layer coupling J⊥ S²."
    }
  ],
  "notes": "Magnetic moments, Δ_{z^2} and J⊥ S² values are incorporated into the single results.json artifact to cover the paper's main billed quantities. The spin susceptibility and qualitative band-structure similarity are not scored as they lack a single scalar gold (D7)."
}
```

## How you are scored
A hidden verifier reads `/app/outputs/results.json` and compares each entry to expected reference values derived from the original study. For relative energies, a tolerance is applied to account for the natural spread due to different computational settings; your reported value must fall within the hidden tolerance to receive full credit. For the imaginary‑mode flags, an exact boolean match is required. The verifier checks that all required entries are present and follow the declared schema. A weighted reward (0.0–1.0) is computed from the correctly matched entries, with the primary weight on the energy values and mode flags. Missing or extra entries reduce the score. The verifier does not re‑run any calculations; it evaluates only the content of the submitted JSON file.

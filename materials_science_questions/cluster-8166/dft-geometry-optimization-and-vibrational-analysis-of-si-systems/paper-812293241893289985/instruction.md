# Ab Initio Structure, Vibrational Analysis, and Energetics of HSiS/SiSH Isomer Pairs and Ions

## Problem background
This work computationally investigates the structures, vibrational frequencies, and relative stabilities of the isomer pairs HSiS/SiSH and their corresponding positive and negative ions. The aim is to determine which isomer is more stable in each charge state, to compute their equilibrium geometries and harmonic vibrational frequencies, and to derive key energetic quantities such as isomerization energies, adiabatic ionization potentials, and adiabatic electron affinities. The study provides quantitative predictions for these properties using ab initio quantum chemistry, which are useful for comparison with future experiments and for understanding the role of specific molecular orbitals.

## Approach
The study employs ab initio electronic structure methods. All species are treated with correlated wavefunction theory: geometries are optimized using second‑order Møller‑Plesset perturbation theory (MP2), and final energies are refined with fourth‑order Møller‑Plesset theory including single, double, triple, and quadruple excitations (MP4(SDQT)). Two Gaussian basis sets are constructed from published primitive functions and contractions, denoted basis I (for geometry optimization and harmonic frequencies) and basis II (basis I augmented with f‑polarization functions on Si and S, for high‑level single‑point energies). The frozen‑core approximation is used throughout, correlating only valence electrons.

The computational protocol follows a multi‑step workflow: first, optimize all molecular geometries; second, compute harmonic vibrational frequencies at the Hartree‑Fock level and scale them by a factor of 0.90; third, compute single‑point MP4 energies at the MP2‑optimized geometries; finally, combine these results to obtain zero‑point corrected relative energetics (isomerization energies, ionization potentials, electron affinities).

## Reproduction target
Reproduce the equilibrium geometries (bond lengths R(SiS) and r(XH), bond angle α), scaled harmonic vibrational frequencies (ω(SiS), ω(XH), ω(HAB)), and key relative energetics (isomerization energies, adiabatic ionization potentials, adiabatic electron affinities) for all eight triatomic HSiS/SiSH species using the protocols described above. The results must be written to three JSON files: geometries.json, frequencies.json, and relative_energies.json, following the output contract specified in the Workflow steps and Output contract sections.

## Assets

- Quantum chemistry software (PySCF, Psi4, or ORCA): https://pyscf.org/ or https://psicode.org/ or https://orcaforum.kofo.mpg.de/

## Workflow steps

### Step 1: Geometry optimization of triatomic HSiS/SiSH species
- Role: scored
- Action: Optimize the molecular geometries of all eight triatomic species (HSiS X²A', SiSH X²A', HSiS⁺ X¹Σ⁺, SiSH⁺ X¹A', HSiS⁻ X¹A', HSiS⁻ ¹³A'', SiSH⁻ X³A'', SiSH⁻ ¹¹A') at the MP2 level of theory using the custom basis set I (Huzinaga primitive sets contracted according to Dunning with semidiffuse and polarization functions as detailed in the task background). Use the frozen-core approximation. Write the optimized bond distances R(SiS) and r(XH) (in bohr), bond angle α (in degrees), total electronic energy (in hartree, relative to -686.0 hartree), and the computational method label to geometries.json.
- Output file: `/app/outputs/geometries.json`
- Format: json
- Contract: A JSON array of objects. Each object has keys: species (str), state_label (str), R_SiS (float, unit bohr), r_XH (float, unit bohr), alpha (float, unit degree), method (str, e.g., 'MP2/basis I'), total_energy (float, unit hartree relative to -686.0 hartrees).
- Scoring: scored by hidden verifier

### Step 2: Scaled HF harmonic vibrational frequencies
- Role: scored
- Action: First, perform a Hartree‑Fock geometry optimization for each triatomic species using basis set I (the same basis set as step_geometry). Then, using these HF‑optimized geometries (not the MP2‑optimized geometries from step_geometry), perform a Hartree‑Fock vibrational frequency calculation with basis set I. Compute the harmonic vibrational frequencies, scale all frequencies by a factor of 0.90 to obtain ω(SiS), ω(XH), and ω(HAB), and write the scaled frequencies (in cm⁻¹) and the scaling factor to frequencies.json.
- Output file: `/app/outputs/frequencies.json`
- Format: json
- Contract: A JSON array of objects. Each object has keys: species (str), state_label (str), omega_SiS (float, unit cm⁻¹), omega_XH (float, unit cm⁻¹), omega_HAB (float, unit cm⁻¹), scaling_factor (float).
- Scoring: scored by hidden verifier

### Step 3: MP4//MP2 relative energetics
- Role: scored (load-bearing)
- Action: For each species' MP2-optimized geometry (from step_geometry), run a single-point MP4(SDQT) calculation with basis II (basis I expanded with f-polarization functions on Si and S, exponents 0.34 and 0.55) using the frozen-core approximation. Extract the total energies. Use these MP4 energies together with zero-point energy corrections derived from the scaled harmonic frequencies (from step_frequencies) to compute the following properties in eV: (1) isomerization energy between HSiS and SiSH (neutral, with ZPE); (2) isomerization energy between HSiS⁺ and SiSH⁺; (3) isomerization energy between HSiS⁻(X¹A') and SiSH⁻(X³A''); (4) isomerization energy between HSiS⁻(X¹A') and SiSH⁻(¹¹A'); (5) adiabatic ionization potentials of HSiS and SiSH; (6) adiabatic electron affinities of HSiS (to X¹A' and to ¹³A''); (7) adiabatic electron affinities of SiSH (to X³A'' and to ¹¹A'). Write the results to relative_energies.json.
- Output file: `/app/outputs/relative_energies.json`
- Format: json
- Contract: A JSON object with keys: isomerization_neutral (float, eV), isomerization_cation (float, eV), isomerization_anion_ground (float, eV), isomerization_anion_singlet (float, eV), IP_HSiS (float, eV), IP_SiSH (float, eV), EA_HSiS_to_X1A (float, eV), EA_HSiS_to_13A (float, eV), EA_SiSH_to_X3A (float, eV), EA_SiSH_to_11A (float, eV). Zero-point corrected values where applicable.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/geometries.json`
- `/app/outputs/frequencies.json`
- `/app/outputs/relative_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### geometries.json
- path: `/app/outputs/geometries.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Equilibrium geometries (bond distances, angle, total energy) for all eight HSiS/SiSH species and ions at MP2/basis I level.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `species`, `state_label`, `R_SiS`, `r_XH`, `alpha`, `method`, `total_energy`
    - `properties`:
      - `species`:
        - `type`: string
      - `state_label`:
        - `type`: string
      - `R_SiS`:
        - `type`: number
        - `unit`: bohr
      - `r_XH`:
        - `type`: number
        - `unit`: bohr
      - `alpha`:
        - `type`: number
        - `unit`: degree
      - `method`:
        - `type`: string
      - `total_energy`:
        - `type`: number
        - `unit`: hartree relative to -686.0

### frequencies.json
- path: `/app/outputs/frequencies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Scaled HF vibrational frequencies (0.90 factor) for SiS stretch, XH stretch, and HAB bend of all species. The scorer will also enforce the monotonic trend ω(SiS) increases in order anion < neutral < cation within each isomer family (structural audit).
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `species`, `state_label`, `omega_SiS`, `omega_XH`, `omega_HAB`, `scaling_factor`
    - `properties`:
      - `species`:
        - `type`: string
      - `state_label`:
        - `type`: string
      - `omega_SiS`:
        - `type`: number
        - `unit`: cm⁻¹
      - `omega_XH`:
        - `type`: number
        - `unit`: cm⁻¹
      - `omega_HAB`:
        - `type`: number
        - `unit`: cm⁻¹
      - `scaling_factor`:
        - `type`: number

### relative_energies.json
- path: `/app/outputs/relative_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Key relative energetics derived from MP4(SDQT)/basis II energies and zero-point corrections from scaled HF frequencies.
- schema:
  - `type`: object
  - `required`: `isomerization_neutral`, `isomerization_cation`, `isomerization_anion_ground`, `isomerization_anion_singlet`, `IP_HSiS`, `IP_SiSH`, `EA_HSiS_to_X1A`, `EA_HSiS_to_13A`, `EA_SiSH_to_X3A`, `EA_SiSH_to_11A`
  - `properties`:
    - `isomerization_neutral`:
      - `type`: number
      - `unit`: eV
    - `isomerization_cation`:
      - `type`: number
      - `unit`: eV
    - `isomerization_anion_ground`:
      - `type`: number
      - `unit`: eV
    - `isomerization_anion_singlet`:
      - `type`: number
      - `unit`: eV
    - `IP_HSiS`:
      - `type`: number
      - `unit`: eV
    - `IP_SiSH`:
      - `type`: number
      - `unit`: eV
    - `EA_HSiS_to_X1A`:
      - `type`: number
      - `unit`: eV
    - `EA_HSiS_to_13A`:
      - `type`: number
      - `unit`: eV
    - `EA_SiSH_to_X3A`:
      - `type`: number
      - `unit`: eV
    - `EA_SiSH_to_11A`:
      - `type`: number
      - `unit`: eV

Notes: The checking will compare submitted geometries, frequencies, and relative energies against the paper's reported values within published tolerances (0.02 bohr / 1 degree / 0.005 hartree for geometries, 20 cm⁻¹ for frequencies, 0.05 eV for relative energies). Additionally, a structural audit will verify that ω(SiS) increases in the order anion < neutral < cation within each isomer family. The overall score is the fraction of checks passed; passing threshold is 0.7.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "geometries.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "species",
            "state_label",
            "R_SiS",
            "r_XH",
            "alpha",
            "method",
            "total_energy"
          ],
          "properties": {
            "species": {
              "type": "string"
            },
            "state_label": {
              "type": "string"
            },
            "R_SiS": {
              "type": "number",
              "unit": "bohr"
            },
            "r_XH": {
              "type": "number",
              "unit": "bohr"
            },
            "alpha": {
              "type": "number",
              "unit": "degree"
            },
            "method": {
              "type": "string"
            },
            "total_energy": {
              "type": "number",
              "unit": "hartree relative to -686.0"
            }
          }
        }
      },
      "description": "Equilibrium geometries (bond distances, angle, total energy) for all eight HSiS/SiSH species and ions at MP2/basis I level."
    },
    {
      "file": "frequencies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "species",
            "state_label",
            "omega_SiS",
            "omega_XH",
            "omega_HAB",
            "scaling_factor"
          ],
          "properties": {
            "species": {
              "type": "string"
            },
            "state_label": {
              "type": "string"
            },
            "omega_SiS": {
              "type": "number",
              "unit": "cm⁻¹"
            },
            "omega_XH": {
              "type": "number",
              "unit": "cm⁻¹"
            },
            "omega_HAB": {
              "type": "number",
              "unit": "cm⁻¹"
            },
            "scaling_factor": {
              "type": "number"
            }
          }
        }
      },
      "description": "Scaled HF vibrational frequencies (0.90 factor) for SiS stretch, XH stretch, and HAB bend of all species. The scorer will also enforce the monotonic trend ω(SiS) increases in order anion < neutral < cation within each isomer family (structural audit)."
    },
    {
      "file": "relative_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "isomerization_neutral",
          "isomerization_cation",
          "isomerization_anion_ground",
          "isomerization_anion_singlet",
          "IP_HSiS",
          "IP_SiSH",
          "EA_HSiS_to_X1A",
          "EA_HSiS_to_13A",
          "EA_SiSH_to_X3A",
          "EA_SiSH_to_11A"
        ],
        "properties": {
          "isomerization_neutral": {
            "type": "number",
            "unit": "eV"
          },
          "isomerization_cation": {
            "type": "number",
            "unit": "eV"
          },
          "isomerization_anion_ground": {
            "type": "number",
            "unit": "eV"
          },
          "isomerization_anion_singlet": {
            "type": "number",
            "unit": "eV"
          },
          "IP_HSiS": {
            "type": "number",
            "unit": "eV"
          },
          "IP_SiSH": {
            "type": "number",
            "unit": "eV"
          },
          "EA_HSiS_to_X1A": {
            "type": "number",
            "unit": "eV"
          },
          "EA_HSiS_to_13A": {
            "type": "number",
            "unit": "eV"
          },
          "EA_SiSH_to_X3A": {
            "type": "number",
            "unit": "eV"
          },
          "EA_SiSH_to_11A": {
            "type": "number",
            "unit": "eV"
          }
        }
      },
      "description": "Key relative energetics derived from MP4(SDQT)/basis II energies and zero-point corrections from scaled HF frequencies."
    }
  ],
  "notes": "The checking will compare submitted geometries, frequencies, and relative energies against the paper's reported values within published tolerances (0.02 bohr / 1 degree / 0.005 hartree for geometries, 20 cm⁻¹ for frequencies, 0.05 eV for relative energies). Additionally, a structural audit will verify that ω(SiS) increases in the order anion < neutral < cation within each isomer family. The overall score is the fraction of checks passed; passing threshold is 0.7."
}
```

## How you are scored
Your submitted artifacts will be evaluated by an automated checker. For each scored output file, the checker compares your computed quantities against reference values (extracted from the original publication) within appropriate numerical tolerances. The geometries, frequencies, and relative energies are each compared; the individual stage scores are combined by a weighted average to produce an overall score between 0 and 1. A high overall score (passing threshold 0.7) requires accurate reproduction of the majority of the target properties. Merely reporting the original paper's numbers without performing the calculations will not suffice, as the checker uses hidden reference data and may include structural consistency checks.

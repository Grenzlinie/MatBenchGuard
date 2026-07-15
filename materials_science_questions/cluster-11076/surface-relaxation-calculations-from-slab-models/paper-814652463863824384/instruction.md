# DFT study of Co and Ni doping effects on MgH2 hydrogen release

## Problem background
Magnesium hydride (MgH₂) is a promising hydrogen storage material, but it exhibits high thermodynamic stability that limits hydrogen release. One proposed strategy is to dope the material with transition metals to lower the decomposition enthalpy and enhance hydrogen desorption. This computational study uses plane-wave density functional theory (DFT) to investigate whether substituting a magnesium atom with cobalt or nickel reduces the decomposition enthalpy of bulk MgH₂ and facilitates hydrogen release from the (001) surface.

## Approach
The approach uses spin-polarized plane-wave DFT within the generalized gradient approximation (PW91 or equivalent) to compute total energies and forces. For bulk systems, the rutile β-MgH₂ crystal structure is used to construct a (√2×√2)R45°×2 supercell containing 8 Mg and 16 H atoms. One Mg atom is substituted by Co or Ni to model doping; hydrogen vacancies are introduced by removing a neighboring H atom. Full geometry optimization yields equilibrium lattice parameters and total energies. Zero-point energy (ZPE) corrections are obtained from finite-displacement phonon calculations (using Phonopy or similar) to convert reaction energies to Helmholtz enthalpies at 0 K, via the decomposition reaction into elemental solids and H₂ gas.

For surface studies, (001) slabs are built from the optimized bulk supercell, containing 7 layers with a vacuum gap. Surface relaxation and rumpling are computed, and hydrogen adsorption is modeled by placing a single H atom atop the dopant atom. Adsorption energies are obtained from the total energies of the slab with and without the adsorbed H, referenced to the isolated H₂ molecule. Desorption energies and vibrational frequencies are extracted from frozen-atom phonon calculations or potential energy scans, leading to relative hydrogen residence times via an Arrhenius-type expression.

## Reproduction target
Compute, for six bulk systems (clean MgH₂, Co-doped, Ni-doped, each with stoichiometric composition and with one hydrogen vacancy), the Helmholtz decomposition enthalpy at 0 K and the underlying total energies, lattice constants, reaction energies, and ZPE corrections. Additionally, for the clean, Co-doped, and Ni-doped MgH₂(001) surfaces, compute layer rumpling and relaxation, hydrogen adsorption energy atop the dopant atom, desorption energy and vibrational frequency, and relative hydrogen residence time. Write these results into two structured JSON files: `bulk_results.json` and `surface_results.json`.

## Assets

- Quantum ESPRESSO or equivalent open-source DFT code: https://www.quantum-espresso.org/
- Phonopy (or PHON) for phonon calculations: https://phonopy.github.io/phonopy/
- Atomic Simulation Environment (optional): ase
- Crystal structures of hcp Mg, Co (fcc/hcp), Ni (fcc) and isolated H2 molecule

## Workflow steps

### Step 1: Reference total energy calculations
- Role: process
- Action: Perform spin-polarized DFT total-energy calculations for bulk hcp Mg, bulk Co, bulk Ni, and an isolated H2 molecule using a GGA functional (PW91 or equivalent). Use a sufficiently fine k-point density for metals. Record the total energies for later use in reaction energy formulas.
- Evidence: `/app/outputs/reference_energies.json`

### Step 2: Bulk supercell model construction
- Role: process
- Action: Construct the rutile β-MgH₂ crystal with experimental lattice parameters a=4.501 Å, c=3.010 Å, space group P42/mnm. Create a (√2×√2)R45°×2 supercell containing 8 Mg and 16 H atoms. Substitute one Mg by Co or Ni to create doped cells. Remove a H atom adjacent to the dopant to create vacancy-containing cells (H15). Generate initial geometry files for six systems: Mg–Mg7H16, Mg–Mg7H15, Co–Mg7H16, Co–Mg7H15, Ni–Mg7H16, Ni–Mg7H15.
- Evidence: `/app/outputs/initial_bulk_structures.zip`

### Step 3: Bulk DFT structure optimization
- Role: process
- Action: Perform full relaxation (cell parameters and atomic positions) of all six bulk supercells using the open-source DFT code with spin-polarized GGA functional and appropriate energy cutoff and k-point density. Converge forces to at least 0.01 eV/Å. Save final total energies and optimized lattice constants (a, b, c).
- Evidence: `/app/outputs/optimized_bulk_structures.json`

### Step 4: Phonon calculations for bulk ZPE corrections
- Role: process
- Action: Using the relaxed bulk structures, perform finite-displacement phonon calculations (e.g., with Phonopy interfaced to the DFT code). Determine the zero-point energy (ZPE) correction for each of the six bulk systems. Save the ZPE values.
- Evidence: none

### Step 5: Bulk decomposition energy and enthalpy analysis
- Role: scored (load-bearing)
- Action: Compute for each system: (i) total energy, (ii) reaction energy ΔE according to Eq. (1) using the reference energies, (iii) ZPE correction, (iv) Helmholtz enthalpy at 0 K (ΔE+ZPE). Output a JSON file with one entry per system.
- Output file: `/app/outputs/bulk_results.json`
- Format: json
- Contract: Array of objects with keys: system (string, e.g. 'Mg-Mg7H16'), y (int, 15 or 16), total_energy (eV, float), a (Å, float), b (Å, float), c (Å, float), reaction_energy (eV, float), zpe_correction (eV, float), helmholtz_enthalpy (eV, float).
- Scoring: scored by hidden verifier

### Step 6: Surface slab model construction
- Role: process
- Action: From the optimized bulk supercell, construct (001) surface slabs for the clean and doped systems. The slab should contain 7 layers: one M atom (M=Mg,Co,Ni), 13 Mg, 28 H. Set the vacuum gap to 20 Å. Fix the bottom atoms and allow the top two layers to relax fully, third layer along c only. Create slab models for M–Mg13H28(001) (M=Mg,Co,Ni) and for the hydrogen-adsorbed configurations H–M–Mg13H28(001) (adsorbed H placed on top of M).
- Evidence: `/app/outputs/slab_structures.zip`

### Step 7: Surface DFT relaxation and hydrogen adsorption
- Role: process
- Action: Perform DFT relaxation of the clean and doped surface slabs (M–Mg13H28(001)) and of the hydrogen-adsorbed slabs (H–M–Mg13H28(001)) using a k-point grid suitable for slabs and the same functional as for bulk. Compute layer rumpling and relaxation percentages. Extract total energies of the relaxed slabs and of the isolated H2 molecule to calculate adsorption energies using Eq. (4).
- Evidence: none

### Step 8: Desorption energy and frequency calculation
- Role: process
- Action: For the optimized hydrogen-adsorbed slabs, perform a frozen-atom phonon calculation (vibrational frequency of the adsorbed H) or a potential energy scan to extract the desorption energy barrier and the desorption frequency ν. Use the same phonon tool as for bulk.
- Evidence: none

### Step 9: Surface properties and residence time analysis
- Role: scored (load-bearing)
- Action: Compile the surface results: (1) rumpling (Å) and relaxation (%) for layers L0, L1, L2 of each slab, (2) adsorption energy (eV) of H on M, (3) desorption energy (eV) and desorption frequency (cm⁻¹), (4) relative residence time (%) referenced to the clean Mg surface using Eq. (5) with the calculated ν and assuming the same pre‑exponential factor C. Output a JSON file with one entry per system.
- Output file: `/app/outputs/surface_results.json`
- Format: json
- Contract: Array of objects with keys: system (string, e.g. 'Mg-Mg13H28(001)'), layer (string, 'L0','L1','L2' or 'adsorbed'), rumpling (Å, float), relaxation (%, float), adsorption_energy (eV, float), desorption_energy (eV, float), desorption_frequency (cm-1, float), relative_residence_time_percent (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bulk_results.json`
- `/app/outputs/surface_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bulk_results.json
- path: `/app/outputs/bulk_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Calculated bulk decomposition energies and enthalpies for clean, Co- and Ni-doped MgH2 systems.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `properties`:
      - `system`:
        - `type`: string
      - `y`:
        - `type`: integer
      - `total_energy`:
        - `type`: number
        - `description`: eV
      - `a`:
        - `type`: number
        - `description`: Å
      - `b`:
        - `type`: number
        - `description`: Å
      - `c`:
        - `type`: number
        - `description`: Å
      - `reaction_energy`:
        - `type`: number
        - `description`: eV
      - `zpe_correction`:
        - `type`: number
        - `description`: eV
      - `helmholtz_enthalpy`:
        - `type`: number
        - `description`: eV
    - `required`: `system`, `y`, `total_energy`, `a`, `b`, `c`, `reaction_energy`, `zpe_correction`, `helmholtz_enthalpy`

### surface_results.json
- path: `/app/outputs/surface_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Surface relaxation, adsorption, desorption and residence time results for MgH2(001) clean and doped surfaces.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `properties`:
      - `system`:
        - `type`: string
      - `layer`:
        - `type`: string
      - `rumpling`:
        - `type`: number
        - `description`: Å
      - `relaxation`:
        - `type`: number
        - `description`: %
      - `adsorption_energy`:
        - `type`: number
        - `description`: eV
      - `desorption_energy`:
        - `type`: number
        - `description`: eV
      - `desorption_frequency`:
        - `type`: number
        - `description`: cm-1
      - `relative_residence_time_percent`:
        - `type`: number
    - `required`: `system`, `layer`, `rumpling`, `relaxation`, `adsorption_energy`, `desorption_energy`, `desorption_frequency`, `relative_residence_time_percent`

Notes: The agent is expected to use open-source DFT and phonon codes; all results are compared to the paper's reported reference values with tolerances suitable for methodological differences.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bulk_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "system": {
              "type": "string"
            },
            "y": {
              "type": "integer"
            },
            "total_energy": {
              "type": "number",
              "description": "eV"
            },
            "a": {
              "type": "number",
              "description": "Å"
            },
            "b": {
              "type": "number",
              "description": "Å"
            },
            "c": {
              "type": "number",
              "description": "Å"
            },
            "reaction_energy": {
              "type": "number",
              "description": "eV"
            },
            "zpe_correction": {
              "type": "number",
              "description": "eV"
            },
            "helmholtz_enthalpy": {
              "type": "number",
              "description": "eV"
            }
          },
          "required": [
            "system",
            "y",
            "total_energy",
            "a",
            "b",
            "c",
            "reaction_energy",
            "zpe_correction",
            "helmholtz_enthalpy"
          ]
        }
      },
      "description": "Calculated bulk decomposition energies and enthalpies for clean, Co- and Ni-doped MgH2 systems."
    },
    {
      "file": "surface_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "system": {
              "type": "string"
            },
            "layer": {
              "type": "string"
            },
            "rumpling": {
              "type": "number",
              "description": "Å"
            },
            "relaxation": {
              "type": "number",
              "description": "%"
            },
            "adsorption_energy": {
              "type": "number",
              "description": "eV"
            },
            "desorption_energy": {
              "type": "number",
              "description": "eV"
            },
            "desorption_frequency": {
              "type": "number",
              "description": "cm-1"
            },
            "relative_residence_time_percent": {
              "type": "number"
            }
          },
          "required": [
            "system",
            "layer",
            "rumpling",
            "relaxation",
            "adsorption_energy",
            "desorption_energy",
            "desorption_frequency",
            "relative_residence_time_percent"
          ]
        }
      },
      "description": "Surface relaxation, adsorption, desorption and residence time results for MgH2(001) clean and doped surfaces."
    }
  ],
  "notes": "The agent is expected to use open-source DFT and phonon codes; all results are compared to the paper's reported reference values with tolerances suitable for methodological differences."
}
```

## How you are scored
A hidden verifier independently inspects your submitted `bulk_results.json` and `surface_results.json`. For each file, the verifier checks the computed quantities (such as Helmholtz enthalpies, relaxation percentages, and residence times) and compares them against a hidden reference derived from the original study. Scoring is based on whether the magnitude and relative trends of the computed values are physically correct and consistent with the methodology, using predetermined tolerances. Each of the two artifact files carries a substantial weight, and the final reward is a combination of their individual scores. Reporting only the expected numbers without genuine computation is not sufficient; the verifier requires the proper execution of the workflow as evidenced by these output files.

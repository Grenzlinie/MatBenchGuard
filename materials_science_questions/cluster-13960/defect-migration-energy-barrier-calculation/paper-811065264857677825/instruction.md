# DFT binding energies and SIA rotation barriers of Re and Os in W

## Problem background
Tungsten (W) is the leading candidate for plasma-facing materials in future nuclear fusion reactors. Under neutron irradiation, W undergoes transmutation to form rhenium (Re) and osmium (Os). These transmutation elements interact strongly with radiation-induced point defects—vacancies and self-interstitial atoms (SIAs)—altering defect energetics, diffusion, and clustering tendencies. Quantifying the binding and formation energies of Re/Os–vacancy and Re/Os–SIA complexes, as well as the effects of Re/Os on SIA reorientation, is essential for understanding the evolution of irradiation-induced microstructure and precipitation in W. This task targets the key first-principles derived quantities that underpin such defect interactions.

## Approach
A density functional theory (DFT) approach is employed, using the generalized gradient approximation (GGA) with the PW91 functional (or PBE as a close substitute). A 128-atom body-centered-cubic (bcc) supercell of tungsten is used throughout. The computational workflow first determines the equilibrium lattice constant of pure W and computes reference energies for the pristine supercell and for bulk hcp Re and Os. Total energies are then calculated for a series of defect configurations: substitutional Re and Os solutes; a single vacancy in pure W; vacancy–solute pairs at first- and second-nearest-neighbor distances; the ⟨111⟩ crowdion SIA in pure W and in W containing a substitutional Re or Os atom; and the ⟨110⟩ dumbbell SIA in the same three host environments. From these total energies, target quantities—solute binding energies, vacancy–solute binding energies, SIA formation energies, crowdion–solute binding energies, and rotation energy barriers—are derived using standard supercell defect-energy formulas. The calculations are to be performed with an open-source DFT code (Quantum ESPRESSO) instead of the proprietary code used in the original study.

## Reproduction target
Compute the following quantities using the described DFT protocol and report them in a single JSON file named calculated_values.json:
1. Binding energies of Re–Re, Os–Os, and Re–Os pairs at nearest-neighbor distance.
2. Binding energies of Re–vacancy and Os–vacancy pairs at first and second nearest-neighbor distances.
3. Formation energies of the ⟨111⟩ crowdion SIA in pure W, in W containing a substitutional Re atom, and in W containing a substitutional Os atom.
4. Binding energies of the ⟨111⟩ crowdion with a nearest-neighbor substitutional Re atom and with a nearest-neighbor substitutional Os atom.
5. Rotation energy barriers for the SIA reorientation path ⟨111⟩ → ⟨110⟩ → ⟨111⟩ in pure W, in W–Re, and in W–Os.
All values must be given in electron volts (eV) with at least two decimal places, and the JSON keys must match exactly those specified in the output contract.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP Efficiency pseudopotentials (GGA-PBE/PW91) for W, Re, Os: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: DFT setup and reference energies
- Role: process
- Action: Determine the equilibrium lattice constant of bcc W; compute the total energy of a 128-atom pure W supercell; compute the reference energy per atom of bulk hcp Re and hcp Os.
- Evidence: `/app/outputs/dft_ref.log`

### Step 2: Substitutional Re and Os total energies
- Role: process
- Action: Compute total energies of the 128-atom W supercell with one substitutional Re atom and with one substitutional Os atom.
- Evidence: `/app/outputs/sub_re_os.log`

### Step 3: Vacancy and Re/Os-vacancy complexes
- Role: process
- Action: Compute total energies for a single vacancy in pure W, and for Re-V and Os-V pairs with the vacancy at the 1NN and 2NN positions relative to the solute.
- Evidence: `/app/outputs/vac_complexes.log`

### Step 4: SIA formation and crowdion binding
- Role: process
- Action: Compute total energies of the <111> crowdion SIA in pure W, in W-Re, and in W-Os, and of the same SIA configurations with the solute at the nearest-neighbor position along the <111> string.
- Evidence: `/app/outputs/sia_energies.log`

### Step 5: SIA rotation barriers
- Role: process
- Action: Compute total energies of the SIA in the <110> dumbbell configuration for pure W, W-Re, and W-Os to obtain the rotation energy barrier <111>→<110>.
- Evidence: `/app/outputs/rotation.log`

### Step 6: Assemble and report derived quantities
- Role: scored (load-bearing)
- Action: Using the total energies from the previous steps, compute the binding energies, formation energies, and rotation barriers according to the standard DFT supercell formulas. Write the results as a JSON file with the required keys.
- Output file: `/app/outputs/calculated_values.json`
- Format: json
- Contract: JSON object with keys: re_re_binding_eV, os_os_binding_eV, re_os_binding_eV, re_vac_1nn_binding_eV, re_vac_2nn_binding_eV, os_vac_1nn_binding_eV, os_vac_2nn_binding_eV, sia_111_formation_pure_W_eV, sia_111_formation_W_Re_eV, sia_111_formation_W_Os_eV, crowdion_re_binding_1nn_eV, crowdion_os_binding_1nn_eV, rotation_barrier_pure_W_eV, rotation_barrier_W_Re_eV, rotation_barrier_W_Os_eV. All values as floats with at least 2 decimal places.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/calculated_values.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### calculated_values.json
- path: `/app/outputs/calculated_values.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: DFT-computed binding energies, formation energies, and rotation barriers for Re/Os point defects in W.
- schema:
  - `type`: object
  - `required`: `re_re_binding_eV`, `os_os_binding_eV`, `re_os_binding_eV`, `re_vac_1nn_binding_eV`, `re_vac_2nn_binding_eV`, `os_vac_1nn_binding_eV`, `os_vac_2nn_binding_eV`, `sia_111_formation_pure_W_eV`, `sia_111_formation_W_Re_eV`, `sia_111_formation_W_Os_eV`, `crowdion_re_binding_1nn_eV`, `crowdion_os_binding_1nn_eV`, `rotation_barrier_pure_W_eV`, `rotation_barrier_W_Re_eV`, `rotation_barrier_W_Os_eV`
  - `properties`:
    - `re_re_binding_eV`:
      - `type`: number
      - `unit`: eV
      - `description`: Binding energy of Re-Re pair at nearest neighbor
    - `os_os_binding_eV`:
      - `type`: number
      - `unit`: eV
      - `description`: Binding energy of Os-Os pair at nearest neighbor
    - `re_os_binding_eV`:
      - `type`: number
      - `unit`: eV
      - `description`: Binding energy of Re-Os pair at nearest neighbor
    - `re_vac_1nn_binding_eV`:
      - `type`: number
      - `unit`: eV
      - `description`: Binding energy of Re-V pair at first nearest neighbor
    - `re_vac_2nn_binding_eV`:
      - `type`: number
      - `unit`: eV
      - `description`: Binding energy of Re-V pair at second nearest neighbor
    - `os_vac_1nn_binding_eV`:
      - `type`: number
      - `unit`: eV
      - `description`: Binding energy of Os-V pair at first nearest neighbor
    - `os_vac_2nn_binding_eV`:
      - `type`: number
      - `unit`: eV
      - `description`: Binding energy of Os-V pair at second nearest neighbor
    - `sia_111_formation_pure_W_eV`:
      - `type`: number
      - `unit`: eV
      - `description`: Formation energy of <111> crowdion SIA in pure W
    - `sia_111_formation_W_Re_eV`:
      - `type`: number
      - `unit`: eV
      - `description`: Formation energy of <111> crowdion SIA in W-Re
    - `sia_111_formation_W_Os_eV`:
      - `type`: number
      - `unit`: eV
      - `description`: Formation energy of <111> crowdion SIA in W-Os
    - `crowdion_re_binding_1nn_eV`:
      - `type`: number
      - `unit`: eV
      - `description`: Binding energy of <111> crowdion with a nearest-neighbor substitutional Re atom
    - `crowdion_os_binding_1nn_eV`:
      - `type`: number
      - `unit`: eV
      - `description`: Binding energy of <111> crowdion with a nearest-neighbor substitutional Os atom
    - `rotation_barrier_pure_W_eV`:
      - `type`: number
      - `unit`: eV
      - `description`: Rotation energy barrier <111>→<110> in pure W
    - `rotation_barrier_W_Re_eV`:
      - `type`: number
      - `unit`: eV
      - `description`: Rotation energy barrier <111>→<110> in W-Re
    - `rotation_barrier_W_Os_eV`:
      - `type`: number
      - `unit`: eV
      - `description`: Rotation energy barrier <111>→<110> in W-Os

Notes: All energy values are in eV. The hidden checker compares values against paper-reported references using tolerances that account for code differences (QE vs VASP) and checks relative trends (Os-V > Re-V > 0; rotation barrier pure W > W-Os > W-Re).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "calculated_values.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "re_re_binding_eV",
          "os_os_binding_eV",
          "re_os_binding_eV",
          "re_vac_1nn_binding_eV",
          "re_vac_2nn_binding_eV",
          "os_vac_1nn_binding_eV",
          "os_vac_2nn_binding_eV",
          "sia_111_formation_pure_W_eV",
          "sia_111_formation_W_Re_eV",
          "sia_111_formation_W_Os_eV",
          "crowdion_re_binding_1nn_eV",
          "crowdion_os_binding_1nn_eV",
          "rotation_barrier_pure_W_eV",
          "rotation_barrier_W_Re_eV",
          "rotation_barrier_W_Os_eV"
        ],
        "properties": {
          "re_re_binding_eV": {
            "type": "number",
            "unit": "eV",
            "description": "Binding energy of Re-Re pair at nearest neighbor"
          },
          "os_os_binding_eV": {
            "type": "number",
            "unit": "eV",
            "description": "Binding energy of Os-Os pair at nearest neighbor"
          },
          "re_os_binding_eV": {
            "type": "number",
            "unit": "eV",
            "description": "Binding energy of Re-Os pair at nearest neighbor"
          },
          "re_vac_1nn_binding_eV": {
            "type": "number",
            "unit": "eV",
            "description": "Binding energy of Re-V pair at first nearest neighbor"
          },
          "re_vac_2nn_binding_eV": {
            "type": "number",
            "unit": "eV",
            "description": "Binding energy of Re-V pair at second nearest neighbor"
          },
          "os_vac_1nn_binding_eV": {
            "type": "number",
            "unit": "eV",
            "description": "Binding energy of Os-V pair at first nearest neighbor"
          },
          "os_vac_2nn_binding_eV": {
            "type": "number",
            "unit": "eV",
            "description": "Binding energy of Os-V pair at second nearest neighbor"
          },
          "sia_111_formation_pure_W_eV": {
            "type": "number",
            "unit": "eV",
            "description": "Formation energy of <111> crowdion SIA in pure W"
          },
          "sia_111_formation_W_Re_eV": {
            "type": "number",
            "unit": "eV",
            "description": "Formation energy of <111> crowdion SIA in W-Re"
          },
          "sia_111_formation_W_Os_eV": {
            "type": "number",
            "unit": "eV",
            "description": "Formation energy of <111> crowdion SIA in W-Os"
          },
          "crowdion_re_binding_1nn_eV": {
            "type": "number",
            "unit": "eV",
            "description": "Binding energy of <111> crowdion with a nearest-neighbor substitutional Re atom"
          },
          "crowdion_os_binding_1nn_eV": {
            "type": "number",
            "unit": "eV",
            "description": "Binding energy of <111> crowdion with a nearest-neighbor substitutional Os atom"
          },
          "rotation_barrier_pure_W_eV": {
            "type": "number",
            "unit": "eV",
            "description": "Rotation energy barrier <111>→<110> in pure W"
          },
          "rotation_barrier_W_Re_eV": {
            "type": "number",
            "unit": "eV",
            "description": "Rotation energy barrier <111>→<110> in W-Re"
          },
          "rotation_barrier_W_Os_eV": {
            "type": "number",
            "unit": "eV",
            "description": "Rotation energy barrier <111>→<110> in W-Os"
          }
        }
      },
      "description": "DFT-computed binding energies, formation energies, and rotation barriers for Re/Os point defects in W."
    }
  ],
  "notes": "All energy values are in eV. The hidden checker compares values against paper-reported references using tolerances that account for code differences (QE vs VASP) and checks relative trends (Os-V > Re-V > 0; rotation barrier pure W > W-Os > W-Re)."
}
```

## How you are scored
A hidden verifier will independently examine your calculated_values.json. The verifier compares your reported values against reference numbers derived from the paper’s original work (which you do not receive). The check has two components: (i) correct relative trends among the computed quantities—the direction of the difference between certain pairs of conditions must match the physical expectation—and (ii) the absolute values must fall within generous tolerances that account for the known scatter between different DFT implementations. The final reward is a weighted combination: 60% from getting the trends/orderings right, 40% from the absolute numerical agreement. Simply copying the paper’s published numbers without running the required calculations will not satisfy the trend checks and will likely fail. The verifier expects values that are physically consistent with a re‑run of the described protocol, not an exact numerical replica of the original study.

# DFT investigation of structural, electronic and magnetic properties of wurtzite Al_xV_1-xN

## Problem background
Wurtzite semiconductor alloys are being investigated for spintronics applications, where the combination of ferromagnetism and semiconducting properties enables control of spin-polarized currents. Transition-metal doping can induce half-metallic ferromagnetism, in which one spin channel is metallic while the other is insulating, giving 100% spin polarization at the Fermi level. This study uses first-principles density functional theory to explore the structural, electronic, and magnetic properties of wurtzite Al_xV_{1-x}N compounds at three vanadium concentrations (x = 0.25, 0.50, 0.75). The aim is to determine the equilibrium lattice parameters, bulk moduli, formation energies, magnetic moments, and the presence of band gaps in the minority spin channel — quantities that clarify whether these materials are half-metallic and therefore promising for spin injection and spintronic devices.

## Approach
The workflow reproduces the first‑principles calculations from the paper using the Quantum ESPRESSO code with the generalized‑gradient approximation (GGA‑PBE). Spin‑polarized total energy versus volume scans are performed for the binary end members AlN (wurtzite) and VN (rocksalt) and for three ordered Al_xV_{1-x}N wurtzite supercells. For each ternary composition, both ferromagnetic (FM) and antiferromagnetic (AFM) spin arrangements are considered. The energy‑volume data are fitted to the Murnaghan equation of state to extract equilibrium lattice constants, bulk moduli, and ground‑state total energies. The magnetic ground state is identified by comparing the fitted FM and AFM total energies. At the equilibrium lattice constant of the FM ground state, self‑consistent and non‑self‑consistent calculations yield the total density of states (DOS), from which the total magnetization and the minority spin band gap relative to the Fermi level are extracted. Formation energies of the ternaries are computed using the total energies of the binary endpoints as references.

## Reproduction target
Produce a JSON file `/app/outputs/results.json` that contains the following computed properties for each of the five compounds AlN_wz, VN_NaCl, Al0.25V0.75N, Al0.50V0.50N, and Al0.75V0.25N:
- equilibrium lattice constant `a0` (Å)
- bulk modulus `B0` (GPa)
- ground-state total energy `E0` (eV)
- formation energy `Ef` (eV, or `null` for the binary compounds)
- magnetic moment per vanadium atom `mag_moment` (µB, or `null` for binaries)
- minority spin band gap `minority_gap` (eV, the difference between the Fermi level and the conduction band minimum in the minority channel; set to zero when the system is metallic or the gap is negative).

All quantities must be derived from the DFT energy‑volume scans, Murnaghan fitting, and electronic structure calculations described in the workflow, and they should be written to the file with the exact schema defined in the output contract.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Pseudopotentials (GGA-PBE) for Al, V, N: https://www.materialscloud.org/discover/sssp/table

## Workflow steps

### Step 1: Supercell construction
- Role: process
- Action: Build initial crystal structures for AlN (wurtzite, 4-atom cell), VN (rocksalt, primitive cell), and ternary Al_xV_{1-x}N wurtzite supercells: 1x1x2 for x=0.25 and 0.75, 1x1x1 for x=0.50. Include both ferromagnetic and antiferromagnetic spin arrangements for each ternary.
- Evidence: none

### Step 2: DFT energy-volume scans
- Role: process
- Action: For each compound and spin configuration, run spin-polarized DFT total energy calculations (Quantum ESPRESSO pw.x, GGA-PBE) at 5–7 volumes around the expected equilibrium. Collect total energy vs. volume data.
- Evidence: `/app/outputs/ev_vs_volume.json`

### Step 3: Equation-of-state (EOS) fitting
- Role: process
- Action: Fit each E(V) dataset to the Murnaghan equation of state. Extract equilibrium lattice constant a0, equilibrium volume V0, bulk modulus B0, and ground-state total energy E0 for every compound (both FM and AFM where applicable).
- Evidence: none

### Step 4: Magnetic ground-state determination
- Role: process
- Action: Compare FM and AFM ground-state total energies from the EOS fits; confirm the FM state is lower for all ternaries. Retain the FM equilibrium structure for subsequent electronic calculations and label it as the ground state.
- Evidence: `/app/outputs/magnetic_energy_diff.json`

### Step 5: Electronic structure calculations at equilibrium
- Role: process
- Action: For each FM ground-state structure at its equilibrium lattice constant, perform spin-polarized SCF and non-SCF calculations to compute the total density of states (DOS). Record the total magnetization and the DOS data.
- Evidence: none

### Step 6: Compile final results
- Role: scored (load-bearing)
- Action: Using the fitted results from steps 03–05, compute formation energies Ef = E(ternary) - x*E(AlN_wz) - (1-x)*E(VN_NaCl). Extract the magnetic moment per V atom (total magnetization divided by number of V atoms) and the minority spin band gap from the DOS (difference between Fermi level and conduction band minimum in the minority channel; set to zero if the gap is negative or the system is metallic). Write all properties into /app/outputs/results.json according to the specified schema.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with key 'compounds' containing an array of objects. Each object must have fields: name (str), a0 (float, Å), B0 (float, GPa), E0 (float, eV), Ef (float or null for binaries), mag_moment (float or null, μB per V atom), minority_gap (float, eV). The array must contain entries for AlN_wz, VN_NaCl, Al0.25V0.75N, Al0.50V0.50N, Al0.75V0.25N.
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
- description: Comprehensive structural, energetic, and magnetic properties of the five compounds as described in the paper. Each field must be present; use null for Ef and mag_moment on the binary compounds where the definition does not apply. The checker compares each numerical value against hidden reference data within tolerances derived from expected DFT spread.
- schema:
  - `type`: object
  - `required`:
    - `compounds`: array
  - `items`:
    - `name`: string
    - `a0`: float (Å)
    - `B0`: float (GPa)
    - `E0`: float (eV)
    - `Ef`: float or null
    - `mag_moment`: float or null (μB per V atom)
    - `minority_gap`: float (eV)
  - `required_columns`:
  - `units`:
    - `a0`: Å
    - `B0`: GPa
    - `E0`: eV
    - `Ef`: eV
    - `mag_moment`: μB
    - `minority_gap`: eV

Notes: The binary compounds serve as reference endpoints for the formation energy calculation. The array order is not enforced, but the five required entries must be present. Only the single scored file results.json is evaluated; all preceding steps are process stages required to produce the necessary intermediate quantities.

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
        "type": "object",
        "required": {
          "compounds": "array"
        },
        "items": {
          "name": "string",
          "a0": "float (Å)",
          "B0": "float (GPa)",
          "E0": "float (eV)",
          "Ef": "float or null",
          "mag_moment": "float or null (μB per V atom)",
          "minority_gap": "float (eV)"
        },
        "required_columns": [],
        "units": {
          "a0": "Å",
          "B0": "GPa",
          "E0": "eV",
          "Ef": "eV",
          "mag_moment": "μB",
          "minority_gap": "eV"
        }
      },
      "description": "Comprehensive structural, energetic, and magnetic properties of the five compounds as described in the paper. Each field must be present; use null for Ef and mag_moment on the binary compounds where the definition does not apply. The checker compares each numerical value against hidden reference data within tolerances derived from expected DFT spread."
    }
  ],
  "notes": "The binary compounds serve as reference endpoints for the formation energy calculation. The array order is not enforced, but the five required entries must be present. Only the single scored file results.json is evaluated; all preceding steps are process stages required to produce the necessary intermediate quantities."
}
```

## How you are scored
A hidden verifier will read your `/app/outputs/results.json` and compare every numerical entry against hidden expected values that correspond to a correctly executed DFT reproduction. The comparison accounts for the inherent spread that arises from different software versions, pseudopotential choices, and computational settings. The final reward is a weighted sum of the agreement per compound and per property. To achieve a high score you must genuinely perform the DFT calculations and the EOS fitting as outlined; simply writing arbitrary numbers will not satisfy the verifier's checks.

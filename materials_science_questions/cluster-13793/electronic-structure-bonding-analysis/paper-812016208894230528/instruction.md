# Electronic Structure and Bonding Analysis of LiBC

## Problem background
LiBC is an insulating layered material with a crystal structure analogous to MgB2. It has been proposed that applying high pressure could close the electronic band gap and induce metallization, potentially leading to MgB2‑type superconductivity. Predicting the pressure‑induced structural and electronic changes of LiBC is an important step in understanding whether it could become a high‑pressure superconductor. This task focuses on computing the equation of state and the metallization pressure for LiBC from first principles.

## Approach
We use density‑functional theory (DFT) with the GGA‑PBE exchange‑correlation functional to compute the ground‑state properties of LiBC. The workflow consists of three phases. First, we compute total energies for a series of unit cell volumes, relaxing internal coordinates at each volume to obtain the energy‑volume curve. Second, we fit the resulting energies to the third‑order Birch‑Murnaghan equation of state to extract the zero‑pressure equilibrium volume, bulk modulus, and its pressure derivative. Third, we calculate the electronic band structure at each volume to track the indirect band gap as a function of pressure, identifying the pressure at which the gap closes. The calculations can be performed with an open‑source DFT code such as Quantum ESPRESSO, using publicly available GGA‑PBE pseudopotentials for Li, B, and C.

## Reproduction target
Reproduce the DFT‑GGA equation of state parameters for LiBC (equilibrium volume V0, bulk modulus B0, and pressure derivative Bprime) and determine the pressure at which the indirect band gap closes, marking the metallization point. These results must be saved as scored JSON artifacts: eos_parameters.json and metallization_pressure.json.

## Assets

- LiBC crystal structure (P6_3/mmc): 10.1002/zaac.19956210762
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- GGA-PBE pseudopotentials for Li, B, C: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: DFT total energy calculations
- Role: process
- Action: Set up the LiBC crystal structure in an open-source DFT code (e.g., Quantum ESPRESSO) with GGA-PBE pseudopotentials. For a series of unit cell volumes spanning approximately 25–50 Å³ (at least 30 equally spaced points), perform variable-cell relaxation (or fixed-volume relaxation of internal coordinates) to obtain the total energy at each volume. Ensure sufficient k-point sampling and plane-wave cutoff.
- Evidence: none

### Step 2: Fit Birch-Murnaghan equation of state
- Role: scored
- Action: Fit the set of volume-energy pairs from step_01 to the third-order Birch-Murnaghan equation of state to obtain zero-pressure volume V0 (Å³), bulk modulus B0 (GPa), and its pressure derivative Bprime. Save the fitted parameters to eos_parameters.json.
- Output file: `/app/outputs/eos_parameters.json`
- Format: json
- Contract: {"V0": number (Angstrom^3), "B0": number (GPa), "Bprime": number}
- Scoring: scored by hidden verifier

### Step 3: Band structure and gap closure analysis
- Role: process
- Action: For each volume used in step_01, perform a band structure calculation along a high-symmetry path (e.g., Γ-M-K-Γ-A-L-H-A) to determine the indirect band gap. Use the EOS from step_02 to convert each volume to pressure. Identify the volume at which the indirect band gap becomes ≤ 0 eV.
- Evidence: none

### Step 4: Report metallization pressure
- Role: scored (load-bearing)
- Action: Write the pressure (GPa) at which the indirect band gap closes to metallization_pressure.json.
- Output file: `/app/outputs/metallization_pressure.json`
- Format: json
- Contract: {"metallization_pressure_GPa": number}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/eos_parameters.json`
- `/app/outputs/metallization_pressure.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### eos_parameters.json
- path: `/app/outputs/eos_parameters.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Fitted parameters of the Birch-Murnaghan equation of state for LiBC under GGA-PBE.
- schema:
  - `type`: object
  - `required`:
    - `V0`: number (Angstrom^3)
    - `B0`: number (GPa)
    - `Bprime`: number

### metallization_pressure.json
- path: `/app/outputs/metallization_pressure.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Pressure at which LiBC becomes (semi)metallic according to GGA-PBE.
- schema:
  - `type`: object
  - `required`:
    - `metallization_pressure_GPa`: number

Notes: Scoring compares these values to paper-reported references with tolerances that absorb legitimate code/pseudopotential differences. The qualitative bonding analysis (projected density of states, electron density maps) is not scored as it yields no quantifiable target.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "eos_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "V0": "number (Angstrom^3)",
          "B0": "number (GPa)",
          "Bprime": "number"
        }
      },
      "description": "Fitted parameters of the Birch-Murnaghan equation of state for LiBC under GGA-PBE."
    },
    {
      "file": "metallization_pressure.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "metallization_pressure_GPa": "number"
        }
      },
      "description": "Pressure at which LiBC becomes (semi)metallic according to GGA-PBE."
    }
  ],
  "notes": "Scoring compares these values to paper-reported references with tolerances that absorb legitimate code/pseudopotential differences. The qualitative bonding analysis (projected density of states, electron density maps) is not scored as it yields no quantifiable target."
}
```

## How you are scored
A hidden verifier will read the submitted eos_parameters.json and metallization_pressure.json. It compares the values to independently obtained reference data using predefined tolerances. The reward is weighted across the scored stages, with the metallization pressure carrying the largest share. Simply reporting the reference numbers is insufficient; the submitted artifacts must be the direct output of the computational workflow described in the steps above.

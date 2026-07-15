# Phonon dispersion and lattice thermal conductivity of RhSi and RhSn

## Problem background
Mono‑silicide of cobalt (CoSi) is a promising thermoelectric material with a high power factor, but its lattice thermal conductivity is high, limiting efficiency. RhSi and RhSn crystallize in the same B20 structure and may offer lower lattice thermal conductivity. This task computes the phonon dispersion and lattice thermal conductivity of RhSi and RhSn using first‑principles methods to quantify their thermal transport properties.

## Approach
The computational workflow uses density functional theory (DFT) with the PBEsol and PBE functionals via QuantumESPRESSO. After relaxing the crystal structures, second‑order force constants are obtained with the finite‑displacement method using PhonoPy, and third‑order force constants with Phono3Py. The lattice thermal conductivity is then computed within the relaxation‑time approximation including three‑phonon scattering. The results for both materials and both functionals are compared.

## Reproduction target
Compute the lattice thermal conductivity of RhSi and RhSn at 300 K for both the PBEsol and PBE functionals and report the values in thermal_conductivity.json. Also compute the temperature‑dependent lattice thermal conductivity (using PBEsol) from 100 K to 500 K and write the results to temperature_dependence.csv.

## Assets

- RhSi crystal structure (experimental): 10.1107/S0365110X54001344
- RhSn crystal structure (experimental): 10.1515/zna-1947-0203
- QuantumESPRESSO: https://www.quantum-espresso.org/
- PhonoPy: phonopy
- Phono3Py: phono3py

## Workflow steps

### Step 1: DFT structure relaxation
- Role: process
- Action: Perform DFT structure relaxation for RhSi and RhSn using the PBEsol and PBE exchange-correlation functionals with QuantumESPRESSO, obtaining equilibrium lattice parameters and internal coordinates.
- Evidence: none

### Step 2: Second-order interatomic force constants
- Role: process
- Action: Compute second-order interatomic force constants (IFC2) for RhSi and RhSn using the finite-displacement method in a 3x3x3 supercell with PhonoPy, driven by DFT forces from QuantumESPRESSO.
- Evidence: none

### Step 3: Third-order interatomic force constants
- Role: process
- Action: Compute third-order interatomic force constants (IFC3) for RhSi and RhSn using the finite-displacement method in a 2x2x2 supercell with Phono3Py, driven by DFT forces from QuantumESPRESSO.
- Evidence: none

### Step 4: Lattice thermal conductivity at 300 K
- Role: scored (load-bearing)
- Action: From the IFC2 and IFC3, compute the lattice thermal conductivity of RhSi and RhSn at 300 K within the relaxation-time approximation including three-phonon scattering, using a 19×19×19 q-point grid. Provide results for both PBEsol and PBE functionals. Write the values to thermal_conductivity.json.
- Output file: `/app/outputs/thermal_conductivity.json`
- Format: json
- Contract: JSON object with keys 'RhSi' and 'RhSn', each a dictionary with keys 'PBEsol' and 'PBE' containing the thermal conductivity in W/(m·K).
- Scoring: scored by hidden verifier

### Step 5: Temperature‑dependent lattice thermal conductivity
- Role: scored
- Action: Using the PBEsol IFC data, compute the lattice thermal conductivity of RhSi and RhSn at temperatures from 100 K to 500 K (in steps of approximately 50 K) and write the results to temperature_dependence.csv.
- Output file: `/app/outputs/temperature_dependence.csv`
- Format: csv
- Contract: CSV table with columns: Temperature (K), kappa_RhSi (W/mK), kappa_RhSn (W/mK).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermal_conductivity.json`
- `/app/outputs/temperature_dependence.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermal_conductivity.json
- path: `/app/outputs/thermal_conductivity.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Lattice thermal conductivity at 300 K for RhSi and RhSn computed with PBEsol and PBE functionals.
- schema:
  - `type`: object
  - `required`:
    - `RhSi`: object with keys PBEsol and PBE
    - `RhSn`: object with keys PBEsol and PBE
  - `items`: object
  - `required_columns`:
  - `units`:
    - `RhSi.PBEsol`: W/(m·K)
    - `RhSi.PBE`: W/(m·K)
    - `RhSn.PBEsol`: W/(m·K)
    - `RhSn.PBE`: W/(m·K)

### temperature_dependence.csv
- path: `/app/outputs/temperature_dependence.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Temperature dependence of PBEsol lattice thermal conductivity for RhSi and RhSn from 100 K to 500 K. The checker verifies that thermal conductivity decreases monotonically with increasing temperature.
- schema:
  - `type`: table
  - `required`: object
  - `items`: object
  - `required_columns`: `Temperature (K)`, `kappa_RhSi (W/mK)`, `kappa_RhSn (W/mK)`
  - `units`:
    - `Temperature (K)`: K
    - `kappa_RhSi (W/mK)`: W/(m·K)
    - `kappa_RhSn (W/mK)`: W/(m·K)

Notes: Phonon dispersion and density of states are produced as intermediate outputs but are not scored. Solid-solution calculations are excluded from scope.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermal_conductivity.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "RhSi": "object with keys PBEsol and PBE",
          "RhSn": "object with keys PBEsol and PBE"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "RhSi.PBEsol": "W/(m·K)",
          "RhSi.PBE": "W/(m·K)",
          "RhSn.PBEsol": "W/(m·K)",
          "RhSn.PBE": "W/(m·K)"
        }
      },
      "description": "Lattice thermal conductivity at 300 K for RhSi and RhSn computed with PBEsol and PBE functionals."
    },
    {
      "file": "temperature_dependence.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required": {},
        "items": {},
        "required_columns": [
          "Temperature (K)",
          "kappa_RhSi (W/mK)",
          "kappa_RhSn (W/mK)"
        ],
        "units": {
          "Temperature (K)": "K",
          "kappa_RhSi (W/mK)": "W/(m·K)",
          "kappa_RhSn (W/mK)": "W/(m·K)"
        }
      },
      "description": "Temperature dependence of PBEsol lattice thermal conductivity for RhSi and RhSn from 100 K to 500 K. The checker verifies that thermal conductivity decreases monotonically with increasing temperature."
    }
  ],
  "notes": "Phonon dispersion and density of states are produced as intermediate outputs but are not scored. Solid-solution calculations are excluded from scope."
}
```

## How you are scored
A hidden verifier independently examines each output file: it compares your 300 K thermal conductivity values against reference values, and checks that the temperature‑dependent conductivity decreases monotonically with increasing temperature. Each check contributes to a final weighted reward between 0 and 1.

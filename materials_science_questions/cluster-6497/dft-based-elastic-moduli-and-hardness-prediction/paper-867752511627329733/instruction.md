# DFT Investigation of Elastic Anomalies in BCC Niobium under Pressure

## Problem background
Niobium (Nb), a body-centred cubic (BCC) transition metal, exhibits an anomalous softening of its single-crystal shear elastic moduli C44 and C' under increasing hydrostatic pressure. The softening spans a broad pressure range (tens to hundreds of GPa), with a later unexpected softening at even higher pressures. The physical origin of these elastic anomalies is debated: proposed mechanisms include Fermi-surface nesting, electronic topological transitions, and an underlying rhombohedral distortion similar to that seen in vanadium. Reproducing and analysing the pressure evolution of the shear moduli is the central challenge.

## Approach
Perform first-principles density functional theory (DFT) calculations for BCC Nb using the PBE exchange-correlation functional and a projector augmented‑wave (PAW) pseudopotential with 13 valence electrons. The open‑source Quantum ESPRESSO package serves as the DFT engine. Compute the equation of state to establish the equilibrium volume and pressure scale. Extract the elastic constants C11, C12, C44 and C' = (C11‑C12)/2 via the energy‑strain method: apply the strain matrices for the C44 and C11‑C12 deformations, fit the total energy versus strain magnitude, and derive the moduli. From these constants, calculate the Zener anisotropy factor, the Chung‑Buessem shear anisotropy, and the universal anisotropy index at selected pressures. Model thermo‑electron effects on C44 by performing fixed‑geometry DFT calculations with electronic smearing at several electronic temperatures. Investigate the rhombohedral distortion paths by computing enthalpy differences as a function of rhombohedral deformation parameter and charge‑transfer, and extract the corresponding elastic moduli along the RH₁ and RH₂ paths. Examine the electronic band structures and Fermi surfaces at key pressures to identify topological changes.

## Reproduction target
Compute the full set of single‑crystal elastic constants (C11, C12, C44, C') of BCC Nb at zero Kelvin for a continuous series of pressures covering 0 to 400 GPa using DFT with the PBE functional and a PAW pseudopotential. Report the results in a CSV file with columns: pressure (GPa), C11 (GPa), C12 (GPa), C44 (GPa), Cprime (GPa). Additionally, calculate the anisotropy indices (Zener A, shear anisotropy AG, universal anisotropy AU) at pressure steps 0, 10, …, 100 GPa; provide C44 at electronic temperatures 0 K, 1000 K, and 2000 K for pressures 0, 75, 150, 275, 400 GPa; and compute the elastic moduli for the RH₁ and RH₂ rhombohedral deformation paths as a function of pressure at zero Kelvin (columns: Pressure (GPa), C_RH1 (GPa), C_RH2 (GPa)). All artefacts must be output to the specified paths under /app/outputs.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/download
- Nb PAW pseudopotential (PBE, 13 valence electrons): https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: DFT equation of state and structure optimization
- Role: process
- Action: Perform total-energy calculations over a range of lattice constants for BCC Nb using Quantum ESPRESSO with the PBE functional and a PAW pseudopotential. Fit the energy-volume data to a Vinet equation of state to obtain equilibrium volume V0, bulk modulus B0, and its pressure derivative B0'.
- Evidence: `/app/outputs/eos_fit.txt`

### Step 2: Zero-temperature elastic constants vs pressure
- Role: scored (load-bearing)
- Action: For pressures from 0 to 400 GPa, apply the strain matrices for C44 and C11-C12 deformations, compute the energy-strain curves via DFT, and extract the single-crystal elastic constants C11, C12, C44, and C' = (C11-C12)/2.
- Output file: `/app/outputs/elastic_constants_pressure.csv`
- Format: csv
- Contract: pressure (GPa), C11 (GPa), C12 (GPa), C44 (GPa), Cprime (GPa)
- Scoring: scored by hidden verifier

### Step 3: Elastic anisotropy indices
- Role: scored
- Action: From the zero-temperature elastic constants, compute the Zener anisotropy factor A, the Chung-Buessem shear anisotropy AG, and the universal anisotropy index AU at pressures 0,10,...,100 GPa.
- Output file: `/app/outputs/anisotropy.csv`
- Format: csv
- Contract: Pressure (GPa), A, AG, AU
- Scoring: scored by hidden verifier

### Step 4: Temperature-dependent elastic constants
- Role: scored
- Action: Perform DFT calculations with electronic temperature smearing to model thermo‑electron effects. Compute C44 at temperatures 0 K, 1000 K, and 2000 K for a subset of pressures (0, 75, 150, 275, 400 GPa).
- Output file: `/app/outputs/c44_temperature.csv`
- Format: csv
- Contract: Pressure (GPa), C44_0K (GPa), C44_1000K (GPa), C44_2000K (GPa)
- Scoring: scored by hidden verifier

### Step 5: Rhombohedral distortion enthalpy profiles
- Role: process
- Action: For pressure 39 GPa, compute enthalpy difference between BCC and RH1 structures as a function of rhombohedral deformation parameter δ for selected charge-transfer Δ values (0, -1.15%, -2.69%). Repeat for RH2 at 61 GPa.
- Evidence: `/app/outputs/enthalpy_rh1_39GPa.csv, enthalpy_rh2_61GPa.csv`

### Step 6: Rhombohedral deformation elastic moduli
- Role: scored
- Action: Compute the elastic moduli along the RH1 and RH2 deformation paths as a function of pressure at 0 K, and output the results.
- Output file: `/app/outputs/rh_elastic_moduli.csv`
- Format: csv
- Contract: Pressure (GPa), C_RH1 (GPa), C_RH2 (GPa)
- Scoring: scored by hidden verifier

### Step 7: Electronic structure analysis
- Role: process
- Action: Compute band structures for BCC Nb at selected pressures (39, 100, 275, 340 GPa) and for V at 126 GPa, extracting energy eigenvalues at high‑symmetry k‑points. Also compute Fermi surfaces to identify electronic topological transitions.
- Evidence: `/app/outputs/bandstructure_39GPa.dat, bandstructure_100GPa.dat, bandstructure_275GPa.dat, bandstructure_340GPa.dat, bandstructure_V_126GPa.dat`

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/elastic_constants_pressure.csv`
- `/app/outputs/anisotropy.csv`
- `/app/outputs/c44_temperature.csv`
- `/app/outputs/rh_elastic_moduli.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### elastic_constants_pressure.csv
- path: `/app/outputs/elastic_constants_pressure.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Pressure-dependent elastic constants at 0 K. Checked against paper-reported values within tolerance and softness trends.
- schema:
  - `type`: table
  - `required_columns`: `pressure (GPa)`, `C11 (GPa)`, `C12 (GPa)`, `C44 (GPa)`, `Cprime (GPa)`
  - `units`:
    - `pressure (GPa)`: GPa
    - `C11 (GPa)`: GPa
    - `C12 (GPa)`: GPa
    - `C44 (GPa)`: GPa
    - `Cprime (GPa)`: GPa

### anisotropy.csv
- path: `/app/outputs/anisotropy.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Anisotropy indices at selected pressures. Checked against paper-reported values within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `Pressure (GPa)`, `A`, `AG`, `AU`
  - `units`:
    - `Pressure (GPa)`: GPa
    - `A`: 
    - `AG`: 
    - `AU`: 

### c44_temperature.csv
- path: `/app/outputs/c44_temperature.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Temperature dependence of C44. Checked for the structural property that C44 at 1000 K and 2000 K must be greater than or equal to C44 at 0 K at each pressure.
- schema:
  - `type`: table
  - `required_columns`: `Pressure (GPa)`, `C44_0K (GPa)`, `C44_1000K (GPa)`, `C44_2000K (GPa)`
  - `units`:
    - `Pressure (GPa)`: GPa
    - `C44_0K (GPa)`: GPa
    - `C44_1000K (GPa)`: GPa
    - `C44_2000K (GPa)`: GPa

### rh_elastic_moduli.csv
- path: `/app/outputs/rh_elastic_moduli.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Elastic moduli along rhombohedral paths. Checked for cross-consistency: the arithmetic mean of C_RH1 and C_RH2 must agree with the independently computed C44 (from elastic_constants_pressure.csv) within a hidden relative tolerance.
- schema:
  - `type`: table
  - `required_columns`: `Pressure (GPa)`, `C_RH1 (GPa)`, `C_RH2 (GPa)`
  - `units`:
    - `Pressure (GPa)`: GPa
    - `C_RH1 (GPa)`: GPa
    - `C_RH2 (GPa)`: GPa

Notes: All scored artifacts must be produced from genuine DFT calculations using the public BCC Nb structure, PBE functional, and a PAW pseudopotential. The hidden verifier will compare the required quantities against paper-reported values or structural relations, without revealing tolerances or gold values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "elastic_constants_pressure.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure (GPa)",
          "C11 (GPa)",
          "C12 (GPa)",
          "C44 (GPa)",
          "Cprime (GPa)"
        ],
        "units": {
          "pressure (GPa)": "GPa",
          "C11 (GPa)": "GPa",
          "C12 (GPa)": "GPa",
          "C44 (GPa)": "GPa",
          "Cprime (GPa)": "GPa"
        }
      },
      "description": "Pressure-dependent elastic constants at 0 K. Checked against paper-reported values within tolerance and softness trends."
    },
    {
      "file": "anisotropy.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Pressure (GPa)",
          "A",
          "AG",
          "AU"
        ],
        "units": {
          "Pressure (GPa)": "GPa",
          "A": "",
          "AG": "",
          "AU": ""
        }
      },
      "description": "Anisotropy indices at selected pressures. Checked against paper-reported values within tolerance."
    },
    {
      "file": "c44_temperature.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "Pressure (GPa)",
          "C44_0K (GPa)",
          "C44_1000K (GPa)",
          "C44_2000K (GPa)"
        ],
        "units": {
          "Pressure (GPa)": "GPa",
          "C44_0K (GPa)": "GPa",
          "C44_1000K (GPa)": "GPa",
          "C44_2000K (GPa)": "GPa"
        }
      },
      "description": "Temperature dependence of C44. Checked for the structural property that C44 at 1000 K and 2000 K must be greater than or equal to C44 at 0 K at each pressure."
    },
    {
      "file": "rh_elastic_moduli.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "Pressure (GPa)",
          "C_RH1 (GPa)",
          "C_RH2 (GPa)"
        ],
        "units": {
          "Pressure (GPa)": "GPa",
          "C_RH1 (GPa)": "GPa",
          "C_RH2 (GPa)": "GPa"
        }
      },
      "description": "Elastic moduli along rhombohedral paths. Checked for cross-consistency: the arithmetic mean of C_RH1 and C_RH2 must agree with the independently computed C44 (from elastic_constants_pressure.csv) within a hidden relative tolerance."
    }
  ],
  "notes": "All scored artifacts must be produced from genuine DFT calculations using the public BCC Nb structure, PBE functional, and a PAW pseudopotential. The hidden verifier will compare the required quantities against paper-reported values or structural relations, without revealing tolerances or gold values."
}
```

## How you are scored
A hidden verifier examines each scored artefact independently. For elastic constants and anisotropy indices, the verifier compares the submitted values against reference results with an appropriate tolerance. For temperature‑dependent C44, the verifier checks that C44 at 1000 K and 2000 K is not lower than C44 at 0 K (a required hardening trend). For rhombohedral moduli, the verifier verifies structural cross‑consistency: the arithmetic mean of C_RH1 and C_RH2 must agree with the independently computed C44 within a hidden relative tolerance. Each scored stage carries a weight; the final reward is a weighted sum of the individual stage scores. Simply hardcoding or reporting the paper's numbers without performing the prescribed DFT calculations will not pass the verifier.

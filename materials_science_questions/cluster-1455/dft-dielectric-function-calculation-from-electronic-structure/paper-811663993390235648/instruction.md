# DFT prediction of structural, elastic, and optical properties of cubic Zr3N4 and Hf3N4

## Problem background
Transition metal nitrides are refractory materials with exceptional hardness, thermal stability, and relevance for hard coatings and electronics. The cubic phases of Zr3N4 and Hf3N4 crystallize in a Th3P4-type structure (space group I-43d). First-principles density functional theory (DFT) calculations can predict their ground-state structural parameters (equilibrium lattice constant, bulk modulus and its pressure derivative), single-crystal elastic constants (C11, C12, C44), and the static dielectric constant. This task asks you to compute these quantities from first principles using an open-source plane-wave pseudo-potential DFT code.

## Approach
Use the generalized gradient approximation (GGA) with the Perdew–Burke–Ernzerhof (PBE) exchange-correlation functional and norm-conserving/ultrasoft pseudopotentials from the SSSP library. Start from the cubic Th3P4-type crystal structures with the known lattice parameters and atomic positions for Zr3N4 and Hf3N4. Perform a zero-pressure structural relaxation to obtain the equilibrium lattice constant a0 and volume V0. Then run a series of hydrostatic pressure optimizations (e.g., 0–30 GPa) to collect pressure-volume data, fit a third-order Birch-Murnaghan equation of state, and extract the bulk modulus B0 and pressure derivative B0'. Compute the single-crystal elastic constants C11, C12, and C44 via the static finite-strain method, applying small strains to the optimized structure and obtaining the stress tensor. Calculate the electronic structure (SCF and NSCF) to obtain the imaginary part of the dielectric function ε2(ω) from momentum matrix elements, then apply the Kramers-Kronig transformation to extract the real part and report the static value ε1(0). All DFT calculations should be performed with Quantum ESPRESSO using the PBE functional and SSSP pseudopotentials.

## Reproduction target
Compute and report the following quantities for both Zr3N4 and Hf3N4: equilibrium lattice constant a0 (angstrom), bulk modulus B0 (GPa), pressure derivative B0' (dimensionless), single-crystal elastic constants C11, C12, C44 (GPa), and static dielectric constant ε1(0) (dimensionless). Collect all results into a single JSON file named results.json with the structure described in the output contract.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP Pseudopotentials (PBE): https://www.materialscloud.org/discover/sssp

## Workflow steps

### Step 1: Define crystal structures
- Role: process
- Action: Set up the initial crystal structures (cubic Th3P4-type, space group I-43d) for Zr3N4 and Hf3N4 using the lattice parameter and atomic positions provided in the literature. Create input files for DFT calculations.
- Evidence: `/app/outputs/initial_structures.txt`

### Step 2: DFT structural optimization at zero pressure
- Role: process
- Action: Perform DFT structural optimization at zero external pressure for each compound to obtain equilibrium lattice constant a0 and volume V0. Use Quantum ESPRESSO with GGA-PBE functional and SSSP pseudopotentials.
- Evidence: `/app/outputs/opt_zero_pressure.out`

### Step 3: DFT pressure-series optimizations for equation of state
- Role: process
- Action: Perform DFT optimizations at a series of hydrostatic pressures (0–30 GPa) for each compound to collect pressure-volume data. This generates P(V) datasets needed for EOS fitting.
- Evidence: `/app/outputs/pv_data.csv`

### Step 4: Birch-Murnaghan equation of state fitting
- Role: process
- Action: Fit the third-order Birch-Murnaghan equation of state to the P(V) data to extract bulk modulus B0 and pressure derivative B0' for each compound.
- Evidence: `/app/outputs/eos_fit.json`

### Step 5: DFT elastic constant calculation
- Role: process
- Action: Compute single-crystal elastic constants C11, C12, C44 for each compound using the static finite strain method within DFT. Apply small strains to the optimized structure and obtain the stress tensor.
- Evidence: `/app/outputs/elastic_constants.csv`

### Step 6: DFT electronic structure and dielectric function (imaginary part)
- Role: process
- Action: Perform self-consistent field (SCF) and non-self-consistent field (NSCF) calculations to obtain electronic wavefunctions. Then compute the imaginary part of the dielectric function ε2(ω) from momentum matrix elements.
- Evidence: `/app/outputs/epsilon2.csv`

### Step 7: Kramers-Kronig transformation and static dielectric constant
- Role: process
- Action: Apply the Kramers-Kronig relation to the computed ε2(ω) to obtain the real part ε1(ω) and extract the static value ε1(0).
- Evidence: `/app/outputs/epsilon1_0.txt`

### Step 8: Compile final results
- Role: scored (load-bearing)
- Action: Collect all computed quantities (a0, B0, B0', C11, C12, C44, ε1(0)) for both Zr3N4 and Hf3N4 and write them into a JSON file.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"Zr3N4": {"a0": <float>, "B0": <float>, "B0_prime": <float>, "C11": <float>, "C12": <float>, "C44": <float>, "epsilon1_0": <float>}, "Hf3N4": {"a0": <float>, "B0": <float>, "B0_prime": <float>, "C11": <float>, "C12": <float>, "C44": <float>, "epsilon1_0": <float>}}
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
- target_policy: exact_match
- description: JSON object containing the computed structural, elastic, optical, and electronic properties for Zr3N4 and Hf3N4.
- schema:
  - `type`: object
  - `properties`:
    - `Zr3N4`:
      - `type`: object
      - `properties`:
        - `a0`:
          - `type`: number
          - `unit`: Å
        - `B0`:
          - `type`: number
          - `unit`: GPa
        - `B0_prime`:
          - `type`: number
          - `unit`: dimensionless
        - `C11`:
          - `type`: number
          - `unit`: GPa
        - `C12`:
          - `type`: number
          - `unit`: GPa
        - `C44`:
          - `type`: number
          - `unit`: GPa
        - `epsilon1_0`:
          - `type`: number
          - `unit`: dimensionless
        - `B_poly`:
          - `type`: number
          - `unit`: GPa
        - `G`:
          - `type`: number
          - `unit`: GPa
        - `E`:
          - `type`: number
          - `unit`: GPa
        - `nu`:
          - `type`: number
          - `unit`: dimensionless
        - `n0`:
          - `type`: number
          - `unit`: dimensionless
        - `eps2_peak`:
          - `type`: number
          - `unit`: eV
        - `dos_fermi`:
          - `type`: number
          - `unit`: states/eV
    - `Hf3N4`:
      - `type`: object
      - `properties`:
        - `a0`:
          - `type`: number
          - `unit`: Å
        - `B0`:
          - `type`: number
          - `unit`: GPa
        - `B0_prime`:
          - `type`: number
          - `unit`: dimensionless
        - `C11`:
          - `type`: number
          - `unit`: GPa
        - `C12`:
          - `type`: number
          - `unit`: GPa
        - `C44`:
          - `type`: number
          - `unit`: GPa
        - `epsilon1_0`:
          - `type`: number
          - `unit`: dimensionless
        - `B_poly`:
          - `type`: number
          - `unit`: GPa
        - `G`:
          - `type`: number
          - `unit`: GPa
        - `E`:
          - `type`: number
          - `unit`: GPa
        - `nu`:
          - `type`: number
          - `unit`: dimensionless
        - `n0`:
          - `type`: number
          - `unit`: dimensionless
        - `eps2_peak`:
          - `type`: number
          - `unit`: eV
        - `dos_fermi`:
          - `type`: number
          - `unit`: states/eV

Notes: The checker now compares all fields (original and newly added) against hidden paper-reported gold values using appropriate tolerances. Each numeric field must be within tolerance; otherwise it receives zero credit. Total reward is the average of individual field pass/fail.

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
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "properties": {
          "Zr3N4": {
            "type": "object",
            "properties": {
              "a0": {
                "type": "number",
                "unit": "Å"
              },
              "B0": {
                "type": "number",
                "unit": "GPa"
              },
              "B0_prime": {
                "type": "number",
                "unit": "dimensionless"
              },
              "C11": {
                "type": "number",
                "unit": "GPa"
              },
              "C12": {
                "type": "number",
                "unit": "GPa"
              },
              "C44": {
                "type": "number",
                "unit": "GPa"
              },
              "epsilon1_0": {
                "type": "number",
                "unit": "dimensionless"
              },
              "B_poly": {
                "type": "number",
                "unit": "GPa"
              },
              "G": {
                "type": "number",
                "unit": "GPa"
              },
              "E": {
                "type": "number",
                "unit": "GPa"
              },
              "nu": {
                "type": "number",
                "unit": "dimensionless"
              },
              "n0": {
                "type": "number",
                "unit": "dimensionless"
              },
              "eps2_peak": {
                "type": "number",
                "unit": "eV"
              },
              "dos_fermi": {
                "type": "number",
                "unit": "states/eV"
              }
            }
          },
          "Hf3N4": {
            "type": "object",
            "properties": {
              "a0": {
                "type": "number",
                "unit": "Å"
              },
              "B0": {
                "type": "number",
                "unit": "GPa"
              },
              "B0_prime": {
                "type": "number",
                "unit": "dimensionless"
              },
              "C11": {
                "type": "number",
                "unit": "GPa"
              },
              "C12": {
                "type": "number",
                "unit": "GPa"
              },
              "C44": {
                "type": "number",
                "unit": "GPa"
              },
              "epsilon1_0": {
                "type": "number",
                "unit": "dimensionless"
              },
              "B_poly": {
                "type": "number",
                "unit": "GPa"
              },
              "G": {
                "type": "number",
                "unit": "GPa"
              },
              "E": {
                "type": "number",
                "unit": "GPa"
              },
              "nu": {
                "type": "number",
                "unit": "dimensionless"
              },
              "n0": {
                "type": "number",
                "unit": "dimensionless"
              },
              "eps2_peak": {
                "type": "number",
                "unit": "eV"
              },
              "dos_fermi": {
                "type": "number",
                "unit": "states/eV"
              }
            }
          }
        }
      },
      "description": "JSON object containing the computed structural, elastic, optical, and electronic properties for Zr3N4 and Hf3N4."
    }
  ],
  "notes": "The checker now compares all fields (original and newly added) against hidden paper-reported gold values using appropriate tolerances. Each numeric field must be within tolerance; otherwise it receives zero credit. Total reward is the average of individual field pass/fail."
}
```

## How you are scored
A hidden verifier will independently evaluate each of your workflow stage's artifacts. Each scored stage contributes a portion of the total reward based on how closely your reported results match reference values derived from the paper's reported properties. The verifier uses appropriate tolerances for each quantity; meeting or exceeding the reference quality yields full credit for that field, and credit decreases only if results deviate significantly. The final score is the weighted sum of per-field and per-stage scores. Simply reporting a single self-declared number is not sufficient; the verifier examines your submitted intermediate evidence and final results.json.

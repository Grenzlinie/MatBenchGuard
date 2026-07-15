# DFT study of Y-doped ZrO2 phase stabilization: critical doping concentration

## Problem background
The stabilization of the tetragonal phase of zirconia (ZrO₂) relative to the monoclinic phase is critical for many technological applications of this ceramic. Yttria (Y₂O₃) doping is known to drive a doping-induced phase transition from monoclinic to tetragonal, but the exact doping concentration at which this transition occurs and the underlying energetic balance are not fully understood from a first-principles perspective. This work investigates the energy difference between the monoclinic and tetragonal phases of Y-doped ZrO₂ as a function of Y₂O₃ doping concentration using density functional theory (DFT), and aims to compute the critical doping level where the tetragonal phase becomes energetically favoured.

## Approach
The calculations are performed within the framework of density functional theory (DFT) with the generalized gradient approximation (GGA) in the PBE parameterization. Ultrafast pseudopotentials (including semicore states for Zr and Y) and the Quantum ESPRESSO package are used. The core idea is to compute the total energy per ZrO₂ molecular unit (m.u.) for both monoclinic and tetragonal Y-doped supercells at a series of doping concentrations. Supercells containing up to 96 atoms are constructed, with Y atoms substituting Zr and charge‑compensating oxygen vacancies introduced such that each vacancy is next‑nearest neighbour to a Y atom. Atomic positions (and optionally cell parameters) are relaxed, and the total energies are obtained. For a given doping level x (in at.% Y₂O₃), the energy difference ΔE_{M-T}(x) = E_M(x) − E_T(x) is computed. DFT (GGA) tends to overestimate the absolute energy difference between the two pure phases; therefore, a systematic correction is applied by subtracting a constant offset. The offset is taken as the difference between the computed ΔE_{M-T} at zero doping and the experimentally known value for pure ZrO₂ (0.063 eV/m.u.). The corrected ΔE_{M-T}(x) are linearly fitted, and the critical doping concentration x_{DIPT} is identified as the point where the corrected energy difference crosses zero, signalling the stability crossover.

## Reproduction target
Your task is to compute the critical Y₂O₃ doping concentration for the monoclinic → tetragonal phase transition using DFT.
Specifically:
1. Relax the pure monoclinic and tetragonal ZrO₂ unit cells (12 atoms) and output the relaxed structural parameters in `pure_structure.json`.
2. For at least five Y₂O₃ doping levels (0, 3.125, 6.25, 12.5, 18.75 at.%), construct monoclinic and tetragonal supercells with substitutional Y and charge‑compensating oxygen vacancies, relax them, and compute the total energies per molecular unit.
3. Assemble a CSV file `energy_differences.csv` with the columns: doping_concentration (at.%), E_M (eV/m.u.), E_T (eV/m.u.), and delta_E = E_M - E_T.
4. From the energy differences in this CSV, derive the critical doping concentration x_{DIPT} by applying the offset correction (using the experimental zero‑doping reference of 0.063 eV/m.u.) and a linear fit to the corrected data. Report the derived critical doping concentration either in a separate readme or as an additional column/note in the CSV.

The scored artifacts are `pure_structure.json` and `energy_differences.csv`. The hidden verifier will recompute the critical concentration from your CSV using the same protocol, and also compare your pure‑phase structural parameters against reference data.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PSLIBRARY ultrasoft pseudopotentials for Zr and Y: https://pseudopotentials.quantum-espresso.org/legacy/pslibrary
- ZrO2 crystal structures

## Workflow steps

### Step 1: DFT relaxation of pure ZrO2 phases
- Role: scored
- Action: Relax the atomic positions and lattice parameters of monoclinic and tetragonal ZrO2 using DFT (Quantum ESPRESSO, GGA-PBE, ultrasoft pseudopotentials, converged cutoffs, 2×2×2 k‑point grid). Output relaxed structures in JSON.
- Output file: `/app/outputs/pure_structure.json`
- Format: json
- Contract: Keys: M (object with a, b_a, c_a, beta_deg, positions{Zr,OI,OII} each array of 3 floats) and T (object with a, c_a, dz).
- Scoring: scored by hidden verifier

### Step 2: DFT total energy calculations for doped supercells
- Role: process
- Action: For doping concentrations x = 0, 3.125, 6.25, 12.5, 18.75 at.% Y2O3, construct monoclinic and tetragonal supercells (up to 96 atoms) with substitutional Y and charge-compensating oxygen vacancies (vacancy next-nearest neighbour to Y). Relax atomic positions and compute total energies for each (phase, x) configuration using DFT with the same parameters as step1.
- Evidence: `/app/outputs/doped_calculations.log`

### Step 3: Compile energy differences and determine critical doping
- Role: scored (load-bearing)
- Action: From the total energies obtained in step2, compute the energy difference per molecular unit ΔE_M−T(x) = E_M(x) − E_T(x) (eV/m.u.) for each doping concentration. Assemble a CSV file with columns doping_concentration, E_M, E_T, delta_E.
- Output file: `/app/outputs/energy_differences.csv`
- Format: csv
- Contract: Columns: doping_concentration (atomic % Y2O3), E_M (eV/m.u.), E_T (eV/m.u.), delta_E (eV/m.u.).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/pure_structure.json`
- `/app/outputs/energy_differences.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### pure_structure.json
- path: `/app/outputs/pure_structure.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Relaxed lattice parameters and fractional atomic coordinates for pure monoclinic and tetragonal ZrO2. Compared to the paper's reported structural references.
- schema:
  - `type`: object
  - `required`:
    - `M`:
      - `a`: float
      - `b_a`: float
      - `c_a`: float
      - `beta_deg`: float
      - `positions`:
        - `Zr`: `float`, `float`, `float`
        - `OI`: `float`, `float`, `float`
        - `OII`: `float`, `float`, `float`
    - `T`:
      - `a`: float
      - `c_a`: float
      - `dz`: float

### energy_differences.csv
- path: `/app/outputs/energy_differences.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Total energy differences between monoclinic and tetragonal Y-doped ZrO2 as a function of Y2O3 doping. The checker recomputes the critical doping concentration xDIPT from these values and compares to the hidden reference.
- schema:
  - `type`: table
  - `required_columns`: `doping_concentration`, `E_M`, `E_T`, `delta_E`
  - `units`:
    - `doping_concentration`: at.%
    - `E_M`: eV per molecular unit
    - `E_T`: eV per molecular unit
    - `delta_E`: eV per molecular unit

Notes: Phonon zero‑point energy correction is omitted because it negligibly affects xDIPT. The DFT procedure uses open‑source code and public pseudopotentials; the solving agent must run the full supercell calculations. The scored critical concentration is derived from the energy differences via a linear fit with an offset correction (hidden).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "pure_structure.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "M": {
            "a": "float",
            "b_a": "float",
            "c_a": "float",
            "beta_deg": "float",
            "positions": {
              "Zr": [
                "float",
                "float",
                "float"
              ],
              "OI": [
                "float",
                "float",
                "float"
              ],
              "OII": [
                "float",
                "float",
                "float"
              ]
            }
          },
          "T": {
            "a": "float",
            "c_a": "float",
            "dz": "float"
          }
        }
      },
      "description": "Relaxed lattice parameters and fractional atomic coordinates for pure monoclinic and tetragonal ZrO2. Compared to the paper's reported structural references."
    },
    {
      "file": "energy_differences.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "doping_concentration",
          "E_M",
          "E_T",
          "delta_E"
        ],
        "units": {
          "doping_concentration": "at.%",
          "E_M": "eV per molecular unit",
          "E_T": "eV per molecular unit",
          "delta_E": "eV per molecular unit"
        }
      },
      "description": "Total energy differences between monoclinic and tetragonal Y-doped ZrO2 as a function of Y2O3 doping. The checker recomputes the critical doping concentration xDIPT from these values and compares to the hidden reference."
    }
  ],
  "notes": "Phonon zero‑point energy correction is omitted because it negligibly affects xDIPT. The DFT procedure uses open‑source code and public pseudopotentials; the solving agent must run the full supercell calculations. The scored critical concentration is derived from the energy differences via a linear fit with an offset correction (hidden)."
}
```

## How you are scored
Your work will be evaluated by a hidden automated verifier. It will:
- Read your `pure_structure.json` and compare the relaxed lattice parameters and fractional coordinates against a set of reference structural data for monoclinic and tetragonal ZrO₂. A score will be assigned based on the closeness of the match.
- Read your `energy_differences.csv`, verify that it contains the required columns and at least the specified doping concentrations, recompute the critical doping concentration from your raw energy differences using the same offset correction and linear regression, and compare it to the expected value. The score will reflect the accuracy of the derived critical concentration.
The final reward is a weighted combination of the stage scores, with the energy‑differences‑based critical concentration contributing the largest weight. Reporting only the paper’s numbers is insufficient; you must actually execute the DFT workflow and produce your own computed data.

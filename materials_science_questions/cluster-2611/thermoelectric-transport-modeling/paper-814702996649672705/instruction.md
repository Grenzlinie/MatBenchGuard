# Thermoelectric Transport Property Prediction of OsPn2 Semiconductors

## Problem background
The osmium dipnictides OsPn₂ (Pn = P, As, Sb) adopt the orthorhombic marcasite structure type, which is common among transition-metal pnictides. These compounds have attracted attention for potential thermoelectric applications due to the interplay of narrow band gaps, heavy constituent elements, and the presence of dimeric [Pn₂]⁴⁻ anions. By computing the electronic band structures and thermopower (Seebeck coefficient), one can assess whether these materials possess the desirable combination of a large Seebeck coefficient and tunable carrier concentrations that is required for efficient thermoelectric energy conversion.

## Approach
The reproduction uses first‑principles density functional theory (DFT) within the Perdew–Burke–Ernzerhof (PBE) generalized gradient approximation to obtain the electronic band structures of OsP₂, OsAs₂, and OsSb₂. Starting from the experimentally known crystal structures (lattice parameters and atomic positions provided as a bundled input), self‑consistent field (SCF) calculations are performed to obtain the ground‑state charge density. Subsequently, non‑self‑consistent band‑structure calculations are run on a high‑symmetry k‑path to yield the band energies.

From the band structure, the indirect and direct electronic gaps are extracted. The band energies are then processed with the BoltzTraP2 code, which solves the semiclassical Boltzmann transport equation under the constant relaxation‑time approximation. This yields the Seebeck coefficient as a function of temperature and carrier concentration for both n‑type (electron) and p‑type (hole) doping. By carrying out the full chain of DFT → band energies → transport coefficients, the reproduction directly mirrors the theoretical procedure used to evaluate the thermoelectric potential of these compounds.

## Reproduction target
The goal is to produce the following computational results for each of the three compounds (OsP₂, OsAs₂, OsSb₂):

1. A JSON file (`band_gaps.json`) containing the indirect and direct electronic band gaps (in eV).
2. A CSV file (`seebeck_coefficient.csv`) containing the Seebeck coefficient (in µV/K) for temperatures from 300 K to 500 K (in steps of 50 K), for both n‑type and p‑type doping at carrier concentrations of 1 × 10¹⁹ cm⁻³, 5 × 10¹⁹ cm⁻³, and 1 × 10²⁰ cm⁻³.

These artifacts are the primary outputs that will be evaluated. The reproduction is considered successful if the computed band gaps and Seebeck curves are consistent with independently obtained reference data that is held by the verifier.

## Assets

- Crystal structures of OsP2, OsAs2, OsSb2
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PBE PAW pseudopotentials (PSlibrary): https://dalcorso.github.io/pslibrary/
- BoltzTraP2: https://www.boltztrappart2.org/
- Python packages (numpy, scipy, ase, etc.): pip

## Workflow steps

### Step 1: Prepare DFT input files
- Role: process
- Action: Generate Quantum ESPRESSO input (scf) and band-structure (nscf) input files for OsP2, OsAs2, and OsSb2 using the provided crystal structures (lattice parameters and atomic coordinates from the bundled crystal_structures.json).
- Evidence: `/app/outputs/dft_input_files_presence.txt`

### Step 2: Run SCF calculations
- Role: process
- Action: Perform self-consistent field (SCF) calculations for the three compounds using Quantum ESPRESSO with the PBE exchange-correlation functional and PAW pseudopotentials on a converged k-point grid.
- Evidence: `/app/outputs/scf_outputs.log`

### Step 3: Run NSCF band structure calculations
- Role: process
- Action: Perform non-self-consistent (NSCF) calculations on a high-symmetry k-path to compute band energies, using the charge density from step 2.
- Evidence: `/app/outputs/band_energies.dat`

### Step 4: Extract indirect and direct band gaps
- Role: scored
- Action: Analyze the computed band structures to determine the highest occupied state (HOS) and lowest unoccupied state (LUS) energies. Identify the indirect and direct gap values for each compound and output a JSON file.
- Output file: `/app/outputs/band_gaps.json`
- Format: json
- Contract: JSON array of objects with keys: compound (string, e.g. 'OsP2'), indirect_gap_eV (float), direct_gap_eV (float).
- Scoring: scored by hidden verifier

### Step 5: Compute Seebeck coefficients
- Role: scored (load-bearing)
- Action: Use the band energies from step 3 and BoltzTraP2 to compute Seebeck coefficients for n-type and p-type doping at carrier concentrations of 1×10^19, 5×10^19, and 1×10^20 cm⁻³ over temperatures 300–500 K. Output a CSV file.
- Output file: `/app/outputs/seebeck_coefficient.csv`
- Format: csv
- Contract: CSV with header: temperature_K, seebeck_uV_K, compound, carrier_type (n/p), carrier_concentration_cm3 (e.g. 1e19). Rows for temperatures 300, 350, 400, 450, 500 K for each combination.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gaps.json`
- `/app/outputs/seebeck_coefficient.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gaps.json
- path: `/app/outputs/band_gaps.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Indirect and direct band gaps (GGA) for OsP2, OsAs2, OsSb2.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `compound`, `indirect_gap_eV`, `direct_gap_eV`
    - `properties`:
      - `compound`:
        - `type`: string
      - `indirect_gap_eV`:
        - `type`: number
        - `unit`: eV
      - `direct_gap_eV`:
        - `type`: number
        - `unit`: eV

### seebeck_coefficient.csv
- path: `/app/outputs/seebeck_coefficient.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Seebeck coefficient vs temperature for n- and p-type doping at three carrier concentrations.
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `seebeck_uV_K`, `compound`, `carrier_type`, `carrier_concentration_cm3`
  - `units`:
    - `temperature_K`: K
    - `seebeck_uV_K`: uV/K
    - `carrier_concentration_cm3`: cm^{-3}

Notes: The checker will compare reported band gaps and Seebeck curves against the paper's GGA values and Figure 10, respectively, with appropriate tolerances. The Seebeck step is load-bearing to ensure genuine DFT execution.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gaps.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "compound",
            "indirect_gap_eV",
            "direct_gap_eV"
          ],
          "properties": {
            "compound": {
              "type": "string"
            },
            "indirect_gap_eV": {
              "type": "number",
              "unit": "eV"
            },
            "direct_gap_eV": {
              "type": "number",
              "unit": "eV"
            }
          }
        }
      },
      "description": "Indirect and direct band gaps (GGA) for OsP2, OsAs2, OsSb2."
    },
    {
      "file": "seebeck_coefficient.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "seebeck_uV_K",
          "compound",
          "carrier_type",
          "carrier_concentration_cm3"
        ],
        "units": {
          "temperature_K": "K",
          "seebeck_uV_K": "uV/K",
          "carrier_concentration_cm3": "cm^{-3}"
        }
      },
      "description": "Seebeck coefficient vs temperature for n- and p-type doping at three carrier concentrations."
    }
  ],
  "notes": "The checker will compare reported band gaps and Seebeck curves against the paper's GGA values and Figure 10, respectively, with appropriate tolerances. The Seebeck step is load-bearing to ensure genuine DFT execution."
}
```

## How you are scored
A hidden verifier will automatically score your submission. It reads the two output files (`band_gaps.json` and `seebeck_coefficient.csv`) and compares your computed values against pre‑determined reference standards. The band‑gap stage and the Seebeck‑coefficient stage each carry a weight, and the final reward is a weighted average of the scores from those two stages. To receive full credit, your calculated band gaps and Seebeck curves must show the correct physical trends, shapes, and magnitudes; simply reporting numbers without executing the required DFT and transport calculations will not satisfy the scoring criteria.

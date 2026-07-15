# Carbon impurity reconstruction in HfO2: energy lowering, gap state elimination, and thermodynamic stability

## Problem background
Wide-gap oxides such as HfO2 are used as gate dielectrics in MOSFETs. During atomic layer deposition, metal-organic precursors can unintentionally introduce carbon impurities. It is critical to know whether these impurities create mid-gap states that degrade device performance. The theory of doping limits suggests that in wide-gap materials, impurities rarely produce gap states or a doping response because the system tends to form compensating defect complexes or undergo symmetry-lowering reconstructions that expel defect states out of the band gap. This task targets the carbon-related defects: we need to determine the most stable configuration of a carbon impurity at a Hf site, whether it undergoes a reconstruction, and its thermodynamic stability relative to other carbon defects as a function of oxygen chemical potential.

## Approach
The reproduction uses density functional theory (DFT) with the GGA-PBE functional and open-source pseudopotentials. A 96-atom supercell of cubic HfO2 (lattice constant 5.12 Å) is constructed, and four neutral carbon defect configurations are relaxed: symmetric substitutional C_Hf, a proposed carbonate-like reconstruction of C_Hf (off-centre relaxation), substitutional C_O, and C_O plus an oxygen vacancy. Total energies are extracted and used to compute the energy gain of the reconstructed C_Hf relative to the symmetric one. Reference chemical potentials are obtained from bulk HfO2, Hf metal, and the O2 molecule. Defect formation energies are then calculated as functions of the oxygen chemical potential μ_O. The key thermodynamic comparison is between the carbonate-like C_Hf and the C_O+vacancy pair. A hybrid functional is also used to compute the partial density of states for the two C_Hf configurations, in order to assess the presence or absence of mid-gap states.

## Reproduction target
Produce the following JSON artifacts under `/app/outputs`:
- `step_02_total_energies.json`: total energies (eV) for the four relaxed defect configurations and the energy lowering of the carbonate-like C_Hf reconstruction compared to the symmetric C_Hf.
- `step_03_formation_energies.json`: formation energies at μ_O = 0 eV and μ_O = -4 eV for each configuration, and the threshold oxygen chemical potential μ_O at which the formation energy of the carbonate-like C_Hf becomes lower than that of C_O+vacancy.
These files are scored by a hidden verifier; they must adhere to the exact schemas given in the workflow steps.

## Assets

- Quantum ESPRESSO (or equivalent open-source DFT code): https://www.quantum-espresso.org/
- SSSP efficiency pseudopotentials (Hf, O, C): https://www.materialscloud.org/discover/sssp/table/efficiency
- ASE (Atomic Simulation Environment): https://wiki.fysik.dtu.dk/ase/

## Workflow steps

### Step 1: Bulk reference calculations
- Role: process
- Action: Perform DFT calculations for bulk cubic HfO2 (lattice constant 5.12 Å), Hf metal (hcp), and O2 molecule using the GGA-PBE functional and the same pseudopotentials (SSSP) that will be used for defect calculations. Extract total energies to obtain reference chemical potentials for Hf and O.
- Evidence: `/app/outputs/step_01_reference_energies.json`

### Step 2: Total energies of carbon defect configurations
- Role: scored (load-bearing)
- Action: Construct a 96-atom supercell of cubic HfO2 (lattice constant 5.12 Å). Introduce four neutral carbon defect configurations: symmetric substitutional C_Hf, carbonate-like reconstructed C_Hf (off-centre relaxation), substitutional C_O, and C_O + oxygen vacancy. Relax atomic positions for each configuration using DFT-GGA (PBE) with the SSSP pseudopotentials. Extract total energies for each relaxed configuration and compute the energy gain of the carbonate-like C_Hf relative to the symmetric C_Hf (E_symmetric - E_carbonate). Output the results as JSON.
- Output file: `/app/outputs/step_02_total_energies.json`
- Format: json
- Contract: JSON object with keys: symmetric_C_Hf_total_energy_eV (float), carbonate_C_Hf_total_energy_eV (float), C_O_total_energy_eV (float), C_O_vacancy_total_energy_eV (float), energy_gain_carbonate_vs_symmetric_eV (float). All energies in eV.
- Scoring: scored by hidden verifier

### Step 3: Formation energies of carbon defects vs oxygen chemical potential
- Role: scored
- Action: Using the reference chemical potentials from step_01 and the total energies from step_02, calculate neutral defect formation energies for the four carbon configurations as a function of oxygen chemical potential μ_O. Evaluate at μ_O = 0 eV and μ_O = -4 eV. Determine the threshold μ_O where the formation energy of the carbonate-like C_Hf becomes lower than that of C_O+vacancy. Output as JSON.
- Output file: `/app/outputs/step_03_formation_energies.json`
- Format: json
- Contract: JSON object with keys: mu_O_values (list of two floats, e.g. [0.0, -4.0]), formation_energies_eV (dict with keys 'symmetric_C_Hf', 'carbonate_C_Hf', 'C_O', 'C_O_vacancy', each a list of two floats), threshold_mu_O_eV (float).
- Scoring: scored by hidden verifier

### Step 4: Partial density of states (PDOS) analysis
- Role: process
- Action: Using a hybrid functional (e.g., HSE06 or sX) recalculate the electronic structure for the relaxed symmetric C_Hf and carbonate-like C_Hf configurations from step_02. Compute partial density of states to determine presence or absence of mid-gap states. Output a Boolean indicator for each configuration.
- Evidence: `/app/outputs/step_04_gap_states.json`

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_02_total_energies.json`
- `/app/outputs/step_03_formation_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_02_total_energies.json
- path: `/app/outputs/step_02_total_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Total energies of the four carbon defect configurations and the energy lowering of the carbonate-like C_Hf reconstruction.
- schema:
  - `type`: object
  - `required`: `symmetric_C_Hf_total_energy_eV`, `carbonate_C_Hf_total_energy_eV`, `C_O_total_energy_eV`, `C_O_vacancy_total_energy_eV`, `energy_gain_carbonate_vs_symmetric_eV`
  - `units`:
    - `symmetric_C_Hf_total_energy_eV`: eV
    - `carbonate_C_Hf_total_energy_eV`: eV
    - `C_O_total_energy_eV`: eV
    - `C_O_vacancy_total_energy_eV`: eV
    - `energy_gain_carbonate_vs_symmetric_eV`: eV

### step_03_formation_energies.json
- path: `/app/outputs/step_03_formation_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Formation energies at μ_O = 0 eV and μ_O = -4 eV, and the oxygen chemical potential threshold where carbonate-like C_Hf becomes more stable than C_O+vacancy.
- schema:
  - `type`: object
  - `required`: `mu_O_values`, `formation_energies_eV`, `threshold_mu_O_eV`
  - `properties`:
    - `mu_O_values`:
      - `type`: array
      - `items`:
        - `type`: number
      - `minItems`: 2
      - `maxItems`: 2
    - `formation_energies_eV`:
      - `type`: object
      - `required`: `symmetric_C_Hf`, `carbonate_C_Hf`, `C_O`, `C_O_vacancy`
      - `properties`:
        - `symmetric_C_Hf`:
          - `type`: array
          - `items`:
            - `type`: number
          - `minItems`: 2
          - `maxItems`: 2
        - `carbonate_C_Hf`:
          - `type`: array
          - `items`:
            - `type`: number
          - `minItems`: 2
          - `maxItems`: 2
        - `C_O`:
          - `type`: array
          - `items`:
            - `type`: number
          - `minItems`: 2
          - `maxItems`: 2
        - `C_O_vacancy`:
          - `type`: array
          - `items`:
            - `type`: number
          - `minItems`: 2
          - `maxItems`: 2
    - `threshold_mu_O_eV`:
      - `type`: number

Notes: The checker will compare energy_gain_carbonate_vs_symmetric_eV and threshold_mu_O_eV to hidden paper-reported values with appropriate tolerances. It will verify that formation energy ordering favours carbonate_C_Hf over C_O_vacancy at μ_O = 0 eV and that a crossing occurs by μ_O = -4 eV. Gap state evidence (step_04) may be used for a structural audit if provided.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_02_total_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "symmetric_C_Hf_total_energy_eV",
          "carbonate_C_Hf_total_energy_eV",
          "C_O_total_energy_eV",
          "C_O_vacancy_total_energy_eV",
          "energy_gain_carbonate_vs_symmetric_eV"
        ],
        "units": {
          "symmetric_C_Hf_total_energy_eV": "eV",
          "carbonate_C_Hf_total_energy_eV": "eV",
          "C_O_total_energy_eV": "eV",
          "C_O_vacancy_total_energy_eV": "eV",
          "energy_gain_carbonate_vs_symmetric_eV": "eV"
        }
      },
      "description": "Total energies of the four carbon defect configurations and the energy lowering of the carbonate-like C_Hf reconstruction."
    },
    {
      "file": "step_03_formation_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "mu_O_values",
          "formation_energies_eV",
          "threshold_mu_O_eV"
        ],
        "properties": {
          "mu_O_values": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "minItems": 2,
            "maxItems": 2
          },
          "formation_energies_eV": {
            "type": "object",
            "required": [
              "symmetric_C_Hf",
              "carbonate_C_Hf",
              "C_O",
              "C_O_vacancy"
            ],
            "properties": {
              "symmetric_C_Hf": {
                "type": "array",
                "items": {
                  "type": "number"
                },
                "minItems": 2,
                "maxItems": 2
              },
              "carbonate_C_Hf": {
                "type": "array",
                "items": {
                  "type": "number"
                },
                "minItems": 2,
                "maxItems": 2
              },
              "C_O": {
                "type": "array",
                "items": {
                  "type": "number"
                },
                "minItems": 2,
                "maxItems": 2
              },
              "C_O_vacancy": {
                "type": "array",
                "items": {
                  "type": "number"
                },
                "minItems": 2,
                "maxItems": 2
              }
            }
          },
          "threshold_mu_O_eV": {
            "type": "number"
          }
        }
      },
      "description": "Formation energies at μ_O = 0 eV and μ_O = -4 eV, and the oxygen chemical potential threshold where carbonate-like C_Hf becomes more stable than C_O+vacancy."
    }
  ],
  "notes": "The checker will compare energy_gain_carbonate_vs_symmetric_eV and threshold_mu_O_eV to hidden paper-reported values with appropriate tolerances. It will verify that formation energy ordering favours carbonate_C_Hf over C_O_vacancy at μ_O = 0 eV and that a crossing occurs by μ_O = -4 eV. Gap state evidence (step_04) may be used for a structural audit if provided."
}
```

## How you are scored
A hidden verifier independently evaluates each scored artifact. For `step_02_total_energies.json`, it compares the computed `energy_gain_carbonate_vs_symmetric_eV` to a reference value derived from the original study; your result should be within an expected tolerance. For `step_03_formation_energies.json`, it checks the formation energy ordering at the two μ_O extremes and verifies that the reported `threshold_mu_O_eV` is close to the known crossing point. The final reward is a weighted combination of these checks. Simply copying a number from the paper without performing the actual DFT calculations will not produce a successful submission.

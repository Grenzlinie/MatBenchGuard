# Surfactant-Induced Elongation of Metallic Nanowires

## Problem background
Metallic nanowires exhibit pronounced structural changes under mechanical elongation, and their stability and breaking behavior can be influenced by the presence of surfactants. Computational simulations based on atomistic models can help understand how surfactant interactions affect the elongation process and the formation of atomically thin wires. This task reproduces canonical Monte Carlo simulations of nanowire elongation for silver, gold, palladium, and platinum using embedded atom method (EAM) interatomic potentials and a surfactant stabilization energy model.

## Approach
The simulations employ an embedded atom method (EAM) energy functional, where the total energy of a configuration is the sum of an embedding energy and a pair potential. Surface atoms experience an additional stabilization energy Q that models the interaction with a surfactant medium. The initial configuration consists of 96 mobile atoms distributed among six (100) planes placed between two fixed (100) planes. A canonical Monte Carlo Metropolis algorithm is used to sample configurations at each elongation stage. The fixed planes are gradually separated in steps of 0.1 Å, and at each separation 100,000 Monte Carlo steps are performed until the nanowire ruptures. EAM potential files for Ag, Au, Pd, and Pt are obtained from the provided public URLs. The workflow consists of running simulations for the following conditions: Ag, Au, Pd, Pt at T=300 K with Q=0 eV and Q=1.0 eV, Ag at T=100 K with Q=0.4 eV, and an Ag-Au alloy (50% Ag, 50% Au) at T=100 K with Q_Ag=0.4 eV, Q_Au=0. After the simulations, the distance between the fixed planes at the moment of rupture (d_break) is determined, and the occurrence of a linear atomic chain (LAC) of at least 5 atoms is assessed. All results are stored in a structured JSON file.

## Reproduction target
Produce a file `/app/outputs/results.json` containing one object for each of the following ten conditions:
- (metal=Ag, temperature_K=300, Q_eV=0.0)
- (metal=Ag, temperature_K=300, Q_eV=1.0)
- (metal=Au, temperature_K=300, Q_eV=0.0)
- (metal=Au, temperature_K=300, Q_eV=1.0)
- (metal=Pd, temperature_K=300, Q_eV=0.0)
- (metal=Pd, temperature_K=300, Q_eV=1.0)
- (metal=Pt, temperature_K=300, Q_eV=0.0)
- (metal=Pt, temperature_K=300, Q_eV=1.0)
- (metal=Ag, temperature_K=100, Q_eV=0.4)
- (metal=AgAu, temperature_K=100, Q_eV=0.4)

For the AgAu alloy, the composition is 50% Ag and 50% Au; the surfactant stabilization energy Q applies only to surface Ag atoms (Q_Au=0).

For each condition, compute the breaking distance `d_break_Angstrom` (in Angstrom) and whether a linear atomic chain of at least 5 atoms formed (`LAC_formed`: true/false). Output the results as a JSON array of objects with fields: `metal` (string), `temperature_K` (integer), `Q_eV` (float), `d_break_Angstrom` (float), `LAC_formed` (boolean).

## Assets

- EAM potential for Ag (Foiles/Baskes/Daw): https://www.ctcms.nist.gov/potentials/downloads/EAM/Ag.eam.alloy
- EAM potential for Au (Foiles/Baskes/Daw): https://www.ctcms.nist.gov/potentials/downloads/EAM/Au.eam.alloy
- EAM potential for Pd (Foiles/Baskes/Daw): https://www.ctcms.nist.gov/potentials/downloads/EAM/Pd.eam.alloy
- EAM potential for Pt (Foiles/Baskes/Daw): https://www.ctcms.nist.gov/potentials/downloads/EAM/Pt.eam.alloy

## Workflow steps

### Step 1: Run Monte Carlo elongation simulations
- Role: process
- Action: Implement the Embedded Atom Method (EAM) energy functional and the canonical Monte Carlo Metropolis algorithm. For each required condition (pure metals Ag, Au, Pd, Pt at T = 300 K with Q = 0 eV and Q = 1.0 eV, Ag at T = 100 K with Q = 0.4 eV, and an Ag-Au alloy (50% Ag, 50% Au) at T = 100 K with Q_Ag = 0.4 eV, Q_Au = 0), set up an initial 96-atom nanowire configuration with fixed (100) planes. Run the elongation simulation with 100,000 MC steps per 0.1 Å separation step until rupture. Record total energy vs separation distance and atomic positions.
- Evidence: `/app/outputs/simulation_log.txt`

### Step 2: Extract breaking distances and LAC formation
- Role: scored (load-bearing)
- Action: From the simulation outputs, determine for each condition the elongation distance at nanowire rupture (d_break, in Angstrom) and whether a linear atomic chain of at least 5 atoms formed (LAC_formed). Produce a results.json file containing one object per condition.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: A JSON array of objects with fields: metal (string), temperature_K (integer), Q_eV (float), d_break_Angstrom (float), LAC_formed (boolean).
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
- target_policy: structural_audit
- description: Contains entries for all requested metals and conditions. The checker verifies the relative trend of d_break with Q and the LAC formation status.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `metal`, `temperature_K`, `Q_eV`, `d_break_Angstrom`, `LAC_formed`
    - `properties`:
      - `metal`:
        - `type`: string
      - `temperature_K`:
        - `type`: integer
        - `unit`: K
      - `Q_eV`:
        - `type`: number
        - `unit`: eV
      - `d_break_Angstrom`:
        - `type`: number
        - `unit`: angstrom
      - `LAC_formed`:
        - `type`: boolean

Notes: The checker compares the relative trend of d_break between Q=0 and Q=1.0 eV for each metal, and checks the LAC_formed flag for the specified Ag condition. Absolute d_break values are not required to match exact numbers from the source.

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
      "target_policy": "structural_audit",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "metal",
            "temperature_K",
            "Q_eV",
            "d_break_Angstrom",
            "LAC_formed"
          ],
          "properties": {
            "metal": {
              "type": "string"
            },
            "temperature_K": {
              "type": "integer",
              "unit": "K"
            },
            "Q_eV": {
              "type": "number",
              "unit": "eV"
            },
            "d_break_Angstrom": {
              "type": "number",
              "unit": "angstrom"
            },
            "LAC_formed": {
              "type": "boolean"
            }
          }
        }
      },
      "description": "Contains entries for all requested metals and conditions. The checker verifies the relative trend of d_break with Q and the LAC formation status."
    }
  ],
  "notes": "The checker compares the relative trend of d_break between Q=0 and Q=1.0 eV for each metal, and checks the LAC_formed flag for the specified Ag condition. Absolute d_break values are not required to match exact numbers from the source."
}
```

## How you are scored
The submission is evaluated by a hidden verifier that reads your `results.json`. It checks whether the computed `d_break` values for each metal at T=300 K satisfy a hidden relative ordering requirement between the Q=0 and Q=1.0 eV conditions. It also compares the `LAC_formed` flag for the Ag T=100 K, Q=0.4 eV condition against a hidden expected value. Full credit is given for meeting these hidden criteria, not for matching any particular numeric reference. The final reward is a weighted combination of these checks.

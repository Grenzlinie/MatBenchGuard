# Modified Penn-gap Model Refractive Index and Thermo-Optic Coefficient Prediction

## Problem background
High-frequency refractive indices and their temperature and pressure coefficients are critical parameters for designing optoelectronic devices such as lasers, LEDs, solar cells, and optical fibers. A simple model that relates the refractive index to the fundamental bandgap energy of a semiconductor enables rapid estimation of these quantities for a wide range of binary and ternary mixed crystals, even when experimental data are scarce. This task implements such a model to compute the refractive index and its thermo-optic coefficients from provided bandgap data.

## Approach
The core idea is a modified Penn-gap model. The high-frequency refractive index n is expressed through the relation n²−1 = (m·E_g + c) / (E_g + B)², where E_g is the lowest bandgap energy and m, c, and B are group-specific constants that capture the valence-electron contribution and the average gap correction. The same model, differentiated with respect to temperature and pressure, yields expressions for the temperature coefficient dn/dT and the pressure coefficient dn/dP, each depending on the already computed n, the group constants, and the bandgap coefficients dE_g/dT and dE_g/dP. All group constants (m, c, B) for the five material groups (III-V, II-VI, II-IV-V₂, I-III-VI₂, and group IV) are provided in the Assets section. A list of test compounds with their bandgap energies and bandgap coefficients is also given. You must implement the model equations and compute the three quantities for each compound.

## Reproduction target
For each test compound, using its assigned group and the provided group constants, compute: (1) the high-frequency refractive index n; (2) the temperature coefficient dn/dT; (3) the pressure coefficient dn/dP. Collect the results in a single JSON file predictions.json following the output schema.

## Assets

- Group-specific model constants (m, c, B) from Table 1
- Test compound parameters (E_g, dE_g/dT, dE_g/dP)

## Workflow steps

### Step 1: Compute predicted refractive indices and thermo-optic coefficients
- Role: scored
- Action: Using the provided group-specific constants (m, c, B) and the test compound parameters (E_g, dE_g/dT, dE_g/dP), compute the high-frequency refractive index n via the Penn-gap model, and the temperature coefficient dn/dT and pressure coefficient dn/dP. Write all results to predictions.json.
- Output file: `/app/outputs/predictions.json`
- Format: json
- Contract: JSON object with two arrays: "refractive_indices" (items: {"compound": string, "group": string, "E_g": float, "n_calculated": float}) and "thermo_optic" (items: {"compound": string, "group": string, "E_g": float, "dE_g_dT": float, "dE_g_dP": float, "dn_dT": float, "dn_dP": float}).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/predictions.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### predictions.json
- path: `/app/outputs/predictions.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed refractive indices and thermo-optic coefficients. The hidden checker compares each predicted value against the paper's reported values within tolerances.
- schema:
  - `type`: object
  - `required`:
    - `refractive_indices`: array
    - `thermo_optic`: array
  - `items`:
    - `refractive_indices_item`:
      - `compound`: string
      - `group`: string
      - `E_g`: float
      - `n_calculated`: float
    - `thermo_optic_item`:
      - `compound`: string
      - `group`: string
      - `E_g`: float
      - `dE_g_dT`: float
      - `dE_g_dP`: float
      - `dn_dT`: float
      - `dn_dP`: float

Notes: The model constants and test compound parameters are provided in the instruction. The agent must implement the Penn-gap model equations and compute the three quantities. No external data download is required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "predictions.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "refractive_indices": "array",
          "thermo_optic": "array"
        },
        "items": {
          "refractive_indices_item": {
            "compound": "string",
            "group": "string",
            "E_g": "float",
            "n_calculated": "float"
          },
          "thermo_optic_item": {
            "compound": "string",
            "group": "string",
            "E_g": "float",
            "dE_g_dT": "float",
            "dE_g_dP": "float",
            "dn_dT": "float",
            "dn_dP": "float"
          }
        }
      },
      "description": "Computed refractive indices and thermo-optic coefficients. The hidden checker compares each predicted value against the paper's reported values within tolerances."
    }
  ],
  "notes": "The model constants and test compound parameters are provided in the instruction. The agent must implement the Penn-gap model equations and compute the three quantities. No external data download is required."
}
```

## How you are scored
A hidden verifier will read your predictions.json and compare each computed value against a reference that represents the correct model output for the given inputs. Your reward is 0-to-1, based on the fraction of predictions that meet the required accuracy. Reporting plausible numbers is not sufficient; your computation must faithfully implement the model as described.

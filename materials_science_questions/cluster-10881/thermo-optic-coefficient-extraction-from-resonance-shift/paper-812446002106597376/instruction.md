# Modified Penn-gap Model Refractive Index and Thermo-Optic Coefficient Prediction

## Problem background
High-frequency refractive indices and their temperature and pressure coefficients are critical parameters for designing optoelectronic devices such as lasers, LEDs, solar cells, and optical fibers. A simple model that relates the refractive index to the fundamental bandgap energy of a semiconductor enables rapid estimation of these quantities for a wide range of binary and ternary mixed crystals, even when experimental data are scarce. This task implements such a model to compute the refractive index and its thermo-optic coefficients from provided bandgap data.

## Approach
The core idea is a modified Penn-gap model. The high-frequency refractive index n is expressed through the relation

n² − 1 = (m·E_g + c) / (E_g + B)² ,   (1)

where
- E_g is the lowest bandgap energy,
- m, c are group-specific constants (determining the parameter A = m·E_g + c),
- B is a group- or compound‑specific correction to the average gap.

Differentiating equation (1) with respect to temperature and pressure yields the temperature and pressure coefficients of the refractive index:

dn/dT = (n² − 1)/(2n) · [ m/(m·E_g + c) – 2/(E_g + B) ] · dE_g/dT ,   (2)

dn/dP = (n² − 1)/(2n) · [ m/(m·E_g + c) – 2/(E_g + B) ] · dE_g/dP ,   (3)

where dE_g/dT and dE_g/dP are the temperature and pressure coefficients of the bandgap, respectively.

All group constants (m, c), the parameter B for each test compound, and the required bandgap data (E_g, dE_g/dT, dE_g/dP) are provided in the Assets section. You must implement the model equations and compute the three quantities for each compound.

## Assets

### 1. Group constants for the parameter A (from Table 1 of the paper)

| Group       | m (eV) | c (eV²) |
|-------------|--------|---------|
| IV          | 8.2    | 134     |
| III‑V       | 53.8   | 135     |
| II‑VI       | 25.0   | 212     |
| II‑IV‑V₂    | 52.0   | 143     |
| I‑III‑VI₂   | 31.3   | 170     |

These constants define A = m·E_g + c for each material group.

### 2. Test compounds and their parameters

The following table lists every compound you must evaluate, together with its group, bandgap energy E_g, the parameter B, and the bandgap temperature and pressure coefficients.

| Compound                          | Group      | E_g (eV) | B (eV)    | dE_g/dT (eV/K) | dE_g/dP (eV/kbar) |
|-----------------------------------|------------|----------|-----------|----------------|-------------------|
| Si                                | IV         | 1.12     | 2.502     | −2.4e-4        | −0.01             |
| Ge                                | IV         | 0.67     | 2.40075   | −3.2e-4        | −0.01             |
| GaAs                              | III‑V      | 1.424    | 3.252128  | −4.0e-4        | −0.01             |
| Ga₀.₂₀Al₀.₈₀As                    | III‑V      | 2.585    | 3.41707   | −3.5e-4        | −0.012            |
| ZnS                               | II‑VI      | 3.68     | 5.0228    | −5.0e-4        | −0.02             |
| CdS                               | II‑VI      | 2.38     | 4.7498    | −4.5e-4        | −0.015            |
| Cd₀.₃₈Hg₀.₆₂Te                    | II‑VI      | 0.38     | 4.3298    | −2.0e-4        | −0.005            |
| CuGaS₂                            | I‑III‑VI₂  | 2.49     | 4.5       | −3.0e-4        | −0.01             |
| AgGa₀.₄₀In₀.₆₀S₂                  | I‑III‑VI₂  | 1.974    | 4.7       | −3.0e-4        | −0.01             |
| CdGe(P₀.₂As₀.₈)₂                  | II‑IV‑V₂   | 0.8      | 3.3       | −2.5e-4        | −0.008            |
| In₀.₂₈₇Ga₀.₇₁₃As₀.₆₁₄P₀.₃₈₆      | III‑V      | 0.913    | 3.179646  | −4.2e-4        | −0.01             |

**Notes on units**:  
- E_g and B are in eV.  
- dE_g/dT is in eV/K (use the signs exactly as given).  
- dE_g/dP is in eV/kbar. The computed dn/dP will therefore have units of kbar⁻¹.

## Workflow steps

### Step 1: Compute predicted refractive indices and thermo-optic coefficients
- **Role**: scored
- **Action**: For every compound in the Assets table, use the group constants (m, c) and the compound-specific values (E_g, B, dE_g/dT, dE_g/dP) to compute:
  - the high‑frequency refractive index n via equation (1),
  - the temperature coefficient dn/dT via equation (2),
  - the pressure coefficient dn/dP via equation (3).
  Collect the results in a single JSON file `predictions.json` following the output contract below.
- **Output file**: `/app/outputs/predictions.json`
- **Format**: json
- **Contract**: JSON object with two arrays:
  - `"refractive_indices"` – each item is a JSON object with keys `"compound"`, `"group"`, `"E_g"`, `"n_calculated"`.
  - `"thermo_optic"` – each item is a JSON object with keys `"compound"`, `"group"`, `"E_g"`, `"dE_g_dT"`, `"dE_g_dP"`, `"dn_dT"`, `"dn_dP"`.
- **Scoring**: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/predictions.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### predictions.json
- **path**: `/app/outputs/predictions.json`
- **format**: json
- **purpose**: scored
- **target_policy**: reference_match
- **description**: Computed refractive indices and thermo-optic coefficients. The hidden checker compares each predicted value against the paper’s reported values within tolerances.
- **schema**:
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

**Notes**: The model constants and test compound parameters are provided in the Assets section above. You must implement the Penn‑gap model equations (1)–(3) and compute the three quantities for every compound. No external data download is required.

## Self‑check before finishing (optional, not scored)

A machine‑readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

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
      "description": "Computed refractive indices and thermo-optic coefficients. The hidden checker compares each predicted value against the paper’s reported values within tolerances."
    }
  ],
  "notes": "The model constants and test compound parameters are provided in the instruction. The agent must implement the Penn‑gap model equations and compute the three quantities. No external data download is required."
}
```

## How you are scored
A hidden verifier will read your `predictions.json` and compare each computed value against a reference that represents the correct model output for the given inputs. Your reward is 0‑to‑1, based on the fraction of predictions that meet the required accuracy. Reporting plausible numbers is not sufficient; your computation must faithfully implement the model as described.
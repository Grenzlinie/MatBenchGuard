## Problem background
Two-dimensional materials are extensively studied as gas-sensing layers because of their high surface-to-volume ratio and tunable electronic properties. A monolayer composite obtained by introducing a pair of carbon atoms (a nano graphene domain) into a hexagonal boron nitride (h-BN) sheet can modify the band gap and chemical reactivity of the otherwise inert h-BN surface. This work uses density functional theory (DFT) to investigate whether such a CBN-composite can serve as a sensitive and selective sensor for sulfur dioxide (SO₂), a toxic pollutant, while remaining resistant to interference from typical atmospheric gases (N₂, O₂, CO₂, H₂O) and other toxic species (NO, NO₂, CO). The key quantities to reproduce are the adsorption energies and charge transfers of these gases on the composite, as well as the co-adsorption behaviour of SO₂ with water vapour to assess performance under humidity.

## Approach
The reproduction follows a first-principles computational workflow. A 3×3 periodic h‑BN supercell with a vacuum slab is constructed, and one B‑N pair is substituted by two carbon atoms to create the CBN‑composite. The geometry is fully relaxed using DFT with the Perdew–Burke–Ernzerhof (PBE) functional and Grimme’s D3 dispersion correction to account for van der Waals interactions, and the band gap of the relaxed composite is computed.

Eight gas molecules—SO₂, N₂, O₂, CO₂, H₂O, NO, NO₂, and CO—are then placed on the composite surface in several initial orientations and adsorption sites. For each gas, a DFT relaxation is performed on each trial configuration, and the most stable (lowest total energy) configuration is identified. The adsorption energy is calculated as E_ads = E(sub+gas) − E_sub − E_gas (where a more negative value indicates stronger binding), and the charge transfer between the molecule and the substrate is evaluated via a population analysis (e.g., Hirshfeld or Bader charge partitioning).

Finally, a co‑adsorption configuration of SO₂ and H₂O is relaxed, and the adsorption energies for both molecules are extracted to evaluate whether water vapour degrades the SO₂ sensing performance.

## Reproduction target
The goal is to compute the adsorption energies and charge transfers for the eight gases on the CBN-composite, and the corresponding co‑adsorption values for SO₂ and H₂O. The checker will evaluate the results against expected benchmarks. The computed band gap of the composite itself provides an additional consistency check.

## Assets
- **DFT code** – Any open-source periodic DFT package that supports PBE with Grimme D3 dispersion corrections and population analysis (e.g., Quantum ESPRESSO, CP2K, ABINIT). Pseudopotentials can be obtained from established libraries such as SSSP or PseudoDojo.

## Workflow steps

### Step 1: Composite construction and relaxation
- Role: process
- Action: Build a 3×3 h‑BN supercell with a vacuum layer of at least 15 Å. Substitute one B‑N pair with two carbon atoms. Perform a full geometry relaxation using DFT (PBE functional + Grimme D3 dispersion) until forces are below standard convergence criteria. Save the relaxed structure for subsequent steps.
- Evidence: `/app/outputs/relaxed_composite.xyz`

### Step 2: Composite band gap computation
- Role: scored
- Action: Using the relaxed composite structure, compute the electronic band structure and extract the band gap. Write the result to a JSON file.
- Output file: `/app/outputs/cbn_band_gap.json`
- Format: json
- Contract: A JSON object with keys `band_gap` (float, in eV) and `unit` (string, “eV”). Example: `{"band_gap": 3.029, "unit": "eV"}`
- Scoring: scored by hidden verifier

### Step 3: Single gas adsorption calculations
- Role: scored (load-bearing)
- Action: For each gas molecule—SO₂, N₂, O₂, CO₂, H₂O, NO, NO₂, CO—generate several initial adsorption configurations by varying the adsorption site and molecular orientation. Perform a DFT relaxation for each configuration, identify the lowest‑energy configuration, and compute the adsorption energy E_ads and the charge transfer (Hirshfeld or Bader analysis) for that configuration. Write the results to a CSV file.
- Output file: `/app/outputs/single_adsorption_results.csv`
- Format: csv
- Contract: CSV with columns `gas` (string), `E_ads` (float, eV), `charge_transfer` (float, e). One row per gas molecule.
- Scoring: scored by hidden verifier

### Step 4: Co-adsorption of SO₂ and H₂O
- Role: scored
- Action: Build a co‑adsorption configuration with one SO₂ and one H₂O molecule on the relaxed composite. Perform a DFT relaxation and compute the adsorption energy and charge transfer for each molecule. Write the results to a CSV file.
- Output file: `/app/outputs/coadsorption_results.csv`
- Format: csv
- Contract: CSV with the same columns as Step 3: `gas` (string), `E_ads` (float, eV), `charge_transfer` (float, e). Rows for SO₂ and H₂O.
- Scoring: scored by hidden verifier

## Output files
- `/app/outputs/relaxed_composite.xyz` (process evidence)
- `/app/outputs/cbn_band_gap.json`
- `/app/outputs/single_adsorption_results.csv`
- `/app/outputs/coadsorption_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### cbn_band_gap.json
- path: `/app/outputs/cbn_band_gap.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Band gap of the CBN-composite in eV. Compared against a hidden reference value with a tolerance.
- schema:
  - `type`: object
  - `required`:
    - `band_gap`: float
    - `unit`: string

### single_adsorption_results.csv
- path: `/app/outputs/single_adsorption_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Adsorption energies and charge transfers for the eight gas molecules. The hidden verifier compares each value to reference data and checks that exactly one gas falls within a specific adsorption-energy window while the others do not.
- schema:
  - `type`: table
  - `required_columns`: `gas`, `E_ads`, `charge_transfer`
  - `units`:
    - `E_ads`: eV
    - `charge_transfer`: e

### coadsorption_results.csv
- path: `/app/outputs/coadsorption_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Co-adsorption results for SO2 and H2O. The verifier compares values to reference data and checks that the adsorption energy of the target gas remains within the selectivity threshold.
- schema:
  - `type`: table
  - `required_columns`: `gas`, `E_ads`, `charge_transfer`
  - `units`:
    - `E_ads`: eV
    - `charge_transfer`: e

Notes: All reference values are from the paper's Fig. 2i and text. Tolerances absorb legitimate toolchain spread. The selectivity condition (ideal window) is enforced by the hidden checker.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "cbn_band_gap.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "band_gap": "float",
          "unit": "string"
        }
      },
      "description": "Band gap of the CBN-composite in eV. Compared against a hidden reference value with a tolerance."
    },
    {
      "file": "single_adsorption_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "gas",
          "E_ads",
          "charge_transfer"
        ],
        "units": {
          "E_ads": "eV",
          "charge_transfer": "e"
        }
      },
      "description": "Adsorption energies and charge transfers for the eight gas molecules. The hidden verifier compares each value to reference data and checks that exactly one gas falls within a specific adsorption-energy window while the others do not."
    },
    {
      "file": "coadsorption_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "gas",
          "E_ads",
          "charge_transfer"
        ],
        "units": {
          "E_ads": "eV",
          "charge_transfer": "e"
        }
      },
      "description": "Co-adsorption results for SO2 and H2O. The verifier compares values to reference data and checks that the adsorption energy of the target gas remains within the selectivity threshold."
    }
  ],
  "notes": "All reference values are from the paper's Fig. 2i and text. Tolerances absorb legitimate toolchain spread. The selectivity condition (ideal window) is enforced by the hidden checker."
}
```

## How you are scored
The hidden verifier independently checks each scored artifact:
- The band gap is compared to a reference value with a small tolerance.
- The single‑adsorption CSV is evaluated on two aspects: (i) each gas's adsorption energy and charge transfer are compared to reference values derived from the original study, using appropriate tolerances; (ii) a selectivity condition is verified—exactly one of the gases has an adsorption energy magnitude within a predefined high-performance range, while all other gases fall outside that range.
- The co‑adsorption CSV is evaluated by comparing the adsorption energies and charge transfers to reference values, and by verifying that the adsorption energy of the target gas still satisfies the selectivity threshold.
Artifacts must be valid and complete; missing or malformed files yield zero credit for that step. The final reward is a weighted combination of the scores.

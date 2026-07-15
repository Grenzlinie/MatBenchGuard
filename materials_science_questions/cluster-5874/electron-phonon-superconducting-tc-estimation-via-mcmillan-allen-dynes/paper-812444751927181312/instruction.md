# Superconductivity Optimum Electronegativity Estimation

## Problem background
Superconducting critical temperature (Tc) is known to correlate with the electronic structure of materials. Mulliken electronegativity (χ), defined as the average of the first ionization potential (IP) and the electron affinity (EA), provides a physically motivated scale that can be related to the chemical potential of an atom via density functional theory. For binary alloys, an equilibrium electronegativity (χ_eq) arises from the charge transfer between atoms, which can be expressed in terms of the IP and EA of the constituent elements. This task explores whether a characteristic electronegativity range is associated with higher superconducting critical temperatures. You will compile IP, EA, and Tc values from public standard references, compute χ for individual elements and χ_eq for binary alloys using low-temperature and general formulas, and calculate Tc-weighted average electronegativities to investigate the overall trend.

## Approach
The Mulliken electronegativity for an atom is computed as χ = 0.5 × (IP + EA). For a binary alloy composed of elements A and B, the equilibrium electronegativity can be estimated by two formulas. The low-temperature (non-interacting) formula uses only the smaller of the two ionization potentials and the larger of the two electron affinities: χ_eq_low = 0.5 × (min(IP_A, IP_B) + max(EA_A, EA_B)). A more general formula accounts for the atoms' hardness (η = IP − EA) and is derived from a quadratic energy expansion: χ_eq_general = (η_B·χ_A + η_A·χ_B) / (η_A + η_B). Both formulas are evaluated using the same underlying IP and EA data. The workflow is entirely computational: first, assemble IP, EA, and Tc data for the elements from standard reference compilations, and compile the list of binary alloys with their Tc values. Then, compute χ for every element and χ_eq for every alloy using both formulas. Finally, compute Tc-weighted average electronegativities for the superconducting elements and for the alloys, which summarize the overall trends.

## Reproduction target
Produce three output files, all placed under /app/outputs:
- A CSV file containing the computed Mulliken electronegativity χ for each element, together with the source IP, EA, and Tc (blank for non-superconducting elements).
- A CSV file containing, for each binary alloy, the computed equilibrium electronegativities from the low-temperature formula and the general formula, together with the alloy's Tc.
- A JSON file reporting the Tc-weighted average electronegativity for the set of superconducting elements, and the corresponding Tc-weighted averages for the alloys computed from both formulas.

The computed values should reflect the formulas above using the IP and EA data drawn from the specified reference compilations, and the Tc values from the CRC Handbook. The expectation is that these numbers align with the physical regularities described in the literature; the exact tolerances are determined by the verifier.

## Assets

- CRC Handbook of Chemistry and Physics (62nd edition) – ionization potentials and critical temperatures
- Hotop & Lineberger electron affinity compilation: 10.1063/1.555750

## Workflow steps

### Step 1: Compile element data
- Role: process
- Action: Gather first ionization potentials (IP, eV), electron affinities (EA, eV), and superconducting critical temperatures (Tc, K) for all elements listed in Table 1 of the source from the CRC Handbook and the Hotop & Lineberger compilation. Assemble the data into a structured file.
- Evidence: `/app/outputs/element_data.csv`

### Step 2: Compile alloy list and Tc
- Role: process
- Action: Collect the list of 51 binary alloys and their superconducting critical temperatures (Tc, K) from the CRC Handbook. Store the alloy name, constituent elements, and Tc.
- Evidence: `/app/outputs/alloy_list.csv`

### Step 3: Compute Mulliken electronegativity for elements
- Role: scored
- Action: For each element in the compiled dataset, calculate Mulliken electronegativity χ = 0.5*(IP + EA). Output the computed χ along with the source IP, EA, and Tc.
- Output file: `/app/outputs/element_electronegativity.csv`
- Format: csv
- Contract: Columns: element (str), Tc (float, K; blank if none), IP (float, eV), EA (float, eV), chi (float, eV).
- Scoring: scored by hidden verifier

### Step 4: Compute equilibrium electronegativity for binary alloys
- Role: scored (load-bearing)
- Action: For each alloy, look up IP and EA of the constituent elements. Compute the low-temperature equilibrium electronegativity χ_eq_low = 0.5*(min(IP_A,IP_B) + max(EA_A,EA_B)) and the general formula χ_eq_general = (η_B * χ_A + η_A * χ_B) / (η_A + η_B) where χ = (IP+EA)/2 and η = IP - EA. Output both values.
- Output file: `/app/outputs/alloy_equilibrium_electronegativity.csv`
- Format: csv
- Contract: Columns: alloy (str), Tc (float, K), chi_eq_low (float, eV), chi_eq_general (float, eV).
- Scoring: scored by hidden verifier

### Step 5: Compute Tc-weighted average electronegativities
- Role: scored
- Action: From the element electronegativity data, compute the Tc-weighted average for superconducting metals (those with valid Tc): Σ(Tc_i * χ_i) / ΣTc_i. From the alloy equilibrium data, compute the Tc-weighted average for alloys using both the low-temperature and the general formula. Output the three averages.
- Output file: `/app/outputs/weighted_averages.json`
- Format: json
- Contract: Keys: metals_weighted_avg (float, eV), alloys_weighted_avg_low (float, eV), alloys_weighted_avg_general (float, eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/element_electronegativity.csv`
- `/app/outputs/alloy_equilibrium_electronegativity.csv`
- `/app/outputs/weighted_averages.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### element_electronegativity.csv
- path: `/app/outputs/element_electronegativity.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed Mulliken electronegativity for each element. Values will be compared to the paper's reported χ values within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `element`, `Tc`, `IP`, `EA`, `chi`
  - `units`:
    - `IP`: eV
    - `EA`: eV
    - `chi`: eV

### alloy_equilibrium_electronegativity.csv
- path: `/app/outputs/alloy_equilibrium_electronegativity.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Equilibrium electronegativity for each binary alloy computed with two formulas. Values will be compared to the paper's reported χ_eq values.
- schema:
  - `type`: table
  - `required_columns`: `alloy`, `Tc`, `chi_eq_low`, `chi_eq_general`
  - `units`:
    - `chi_eq_low`: eV
    - `chi_eq_general`: eV

### weighted_averages.json
- path: `/app/outputs/weighted_averages.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Tc-weighted average electronegativities for metals and alloys. Each value will be compared to the paper's reported averages.
- schema:
  - `type`: object
  - `required`:
    - `metals_weighted_avg`: float (eV)
    - `alloys_weighted_avg_low`: float (eV)
    - `alloys_weighted_avg_general`: float (eV)

Notes: All scored artifacts are compared against the original paper's reported values with a tolerance appropriate for numerical replication. The data compilation steps are prerequisites; their evidence files are not scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "element_electronegativity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "element",
          "Tc",
          "IP",
          "EA",
          "chi"
        ],
        "units": {
          "IP": "eV",
          "EA": "eV",
          "chi": "eV"
        }
      },
      "description": "Computed Mulliken electronegativity for each element. Values will be compared to the paper's reported χ values within tolerance."
    },
    {
      "file": "alloy_equilibrium_electronegativity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "alloy",
          "Tc",
          "chi_eq_low",
          "chi_eq_general"
        ],
        "units": {
          "chi_eq_low": "eV",
          "chi_eq_general": "eV"
        }
      },
      "description": "Equilibrium electronegativity for each binary alloy computed with two formulas. Values will be compared to the paper's reported χ_eq values."
    },
    {
      "file": "weighted_averages.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "metals_weighted_avg": "float (eV)",
          "alloys_weighted_avg_low": "float (eV)",
          "alloys_weighted_avg_general": "float (eV)"
        }
      },
      "description": "Tc-weighted average electronegativities for metals and alloys. Each value will be compared to the paper's reported averages."
    }
  ],
  "notes": "All scored artifacts are compared against the original paper's reported values with a tolerance appropriate for numerical replication. The data compilation steps are prerequisites; their evidence files are not scored."
}
```

## How you are scored
An automated hidden verifier evaluates each scored artifact independently. The verifier compares your computed electronegativity values for elements and alloys, and the reported weighted averages, against reference values that represent the correct results of the same formulas applied to the same source data. Comparisons are made with numerical tolerances that account for minor variability in data retrieval and floating-point arithmetic. Each artifact receives a fractional score, and the final reward (a single float between 0 and 1) is a weighted combination of these scores. The verifier requires that every output file adheres to the schema specified in the output contract; incomplete or malformed outputs will receive a low score. You must generate the results by genuine computation; surface-level guesswork is unlikely to satisfy the quantitative tolerances used by the verifier.

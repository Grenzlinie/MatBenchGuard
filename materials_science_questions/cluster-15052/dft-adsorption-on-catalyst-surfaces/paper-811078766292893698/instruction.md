# DFT investigation of adsorption energetics and C–C bond weakening for tar model compounds on CaO catalyst

## Problem background
Biomass gasification produces tars that reduce efficiency and cause corrosion. Catalytic cracking with CaO is an effective clean-up strategy, but the molecular-level mechanism—particularly how CaO weakens aromatic C–C bonds—is not fully understood. This study uses density functional theory to model the adsorption of tar model compound radicals (benzene, toluene, phenol) on CaO and to quantify the resulting bond activation. By computing the adsorption enthalpy changes and the evolution of C–C bond populations for all plausible adsorption geometries, the work aims to identify which pathways are thermodynamically favoured and to rank the three tar compounds by their susceptibility to catalytic bond weakening.

## Approach
The computational approach employs density functional theory at the B3LYP/6-31G(d,p) level. All species (free CaO, the tar radicals with one or two hydrogen atoms removed, and the adsorption products) are first constructed in an open‑source quantum chemistry package (ORCA, NWChem, or PySCF). Geometry optimizations and vibrational frequency calculations are carried out at the reaction temperature (750 °C) and atmospheric pressure, yielding enthalpy corrections. For every adsorption pathway—including C–O–Ca, C–Ca–O, and C–C–Ca–O formations—the enthalpy change ΔH = H(product) – H(CaO) – H(radical) is computed. Pathways with the largest negative ΔH are identified as the most favourable. On these preferred pathways, Mulliken population analysis is performed to extract the six aromatic C–C bond orders. The minimum C–C population before and after adsorption is recorded, and the percent reduction calculated. This quantification reveals how much the catalyst weakens the aromatic ring in each tar model compound.

## Reproduction target
Compute the enthalpy changes (ΔH) for all adsorption pathways of benzene, toluene, and phenol radicals on CaO, determine the most thermodynamically favourable pathways for each compound and for each dehydrogenation state (one‑H and two‑H removed), and report the minimum C–C Mulliken population before and after adsorption together with the percent reduction for the favourable pathways. From the calculated percent reductions, infer the relative catalytic efficiency order of the three tar model compounds. All results must be saved in the specified JSON output files: enthalpy_changes.json and mulliken_tables.json.

## Assets

- Open-source quantum chemistry package (ORCA, NWChem, or PySCF): https://orcaforum.kofo.mpg.de

## Workflow steps

### Step 1: Build initial molecular models
- Role: process
- Action: Construct initial geometries for CaO, the tar model compound radicals (benzene, toluene, phenol) with one or two hydrogen atoms removed, and all adsorption product complexes corresponding to the studied pathways (including C–O–Ca, C–Ca–O, and aromatic C–C–Ca–O formations). Save the initial geometries in XYZ format.
- Evidence: `/app/outputs/initial_geometries.xyz`

### Step 2: DFT geometry optimization and frequency calculation
- Role: process
- Action: For each molecular species from step_01, perform geometry optimization and vibrational frequency calculation at the B3LYP/6-31G(d,p) level, at 750 °C and 1.01 × 10⁵ Pa. Save optimized geometries, electronic energies, zero‑point energies, and enthalpy (H) for all species.
- Evidence: `/app/outputs/optimized_geometries.xyz`

### Step 3: Compute enthalpy changes and identify favorable adsorption pathways
- Role: scored
- Action: From the computed enthalpies of step_02, calculate ΔH = H(product) − H(CaO) − H(radical) for every studied adsorption pathway. Determine the most thermodynamically favorable pathways (most exothermic) for each tar model compound and dehydrogenation state (one and two H removed). Produce a JSON file documenting each pathway's ΔH and whether it is among the preferred pathways.
- Output file: `/app/outputs/enthalpy_changes.json`
- Format: json
- Contract: A JSON object with top-level keys 'benzene', 'toluene', 'phenol'. Each value is an array of objects with fields: 'nH_removed' (integer 1 or 2), 'pathway' (string label), 'delta_H_kJmol' (float, kJ/mol), and 'most_favorable' (boolean).
- Scoring: scored by hidden verifier

### Step 4: Mulliken population analysis and C–C bond weakening quantification
- Role: scored (load-bearing)
- Action: For the favorable pathways identified from step_03 (as described in the paper: preferred pathways per compound), extract Mulliken bond population matrices from the optimized wavefunctions of the adsorption products and the free radicals. For each pathway, compute the minimum C–C Mulliken population before and after adsorption, and the percent reduction defined as (before − after)/before × 100. Write all data to a JSON file.
- Output file: `/app/outputs/mulliken_tables.json`
- Format: json
- Contract: A JSON object with top-level keys 'benzene', 'toluene', 'phenol'. Each value is an array of objects (covering only the favorable pathways) with fields: 'pathway' (string), 'nH_removed' (integer 1 or 2), 'min_mulliken_before' (float), 'min_mulliken_after' (float), 'percent_reduction' (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/enthalpy_changes.json`
- `/app/outputs/mulliken_tables.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### enthalpy_changes.json
- path: `/app/outputs/enthalpy_changes.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Computed enthalpy changes (ΔH) for all adsorption pathways of tar radicals on CaO, with identification of the most thermodynamically favorable pathways. Verified by structural audit: correct relative ordering of pathway types and consistency of marked favorable pathways with the paper's reported adsorption preferences.
- schema:
  - `type`: object
  - `required`:
    - `benzene`: array of pathway objects
    - `toluene`: array of pathway objects
    - `phenol`: array of pathway objects
  - `items`:
    - `nH_removed`: integer (1 or 2)
    - `pathway`: string
    - `delta_H_kJmol`: number (kJ/mol)
    - `most_favorable`: boolean
  - `units`:
    - `delta_H_kJmol`: kJ/mol

### mulliken_tables.json
- path: `/app/outputs/mulliken_tables.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Minimum aromatic C–C Mulliken populations before and after adsorption, with percent reduction, for the favorable pathways of each tar model compound. The percent reduction is compared within a tolerance to the paper‑reported values to confirm bond weakening.
- schema:
  - `type`: object
  - `required`:
    - `benzene`: array of pathway objects
    - `toluene`: array of pathway objects
    - `phenol`: array of pathway objects
  - `items`:
    - `pathway`: string
    - `nH_removed`: integer (1 or 2)
    - `min_mulliken_before`: float
    - `min_mulliken_after`: float
    - `percent_reduction`: float

Notes: Only the favorable pathways (those identified as thermodynamically preferred in the enthalpy analysis) need to be reported in mulliken_tables.json. The checker recomputes percent reduction from the provided min_mulliken_before and min_mulliken_after, then compares to hidden gold values with tolerance. For enthalpy_changes.json, the checker verifies that the most_favorable flags match the paper's qualitative conclusions and that relative enthalpies follow the expected ordering (C–O–Ca more exothermic than C–Ca–O, etc.). Absolute ΔH values are accepted within a generous margin to accommodate code‑to‑code differences.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "enthalpy_changes.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "benzene": "array of pathway objects",
          "toluene": "array of pathway objects",
          "phenol": "array of pathway objects"
        },
        "items": {
          "nH_removed": "integer (1 or 2)",
          "pathway": "string",
          "delta_H_kJmol": "number (kJ/mol)",
          "most_favorable": "boolean"
        },
        "units": {
          "delta_H_kJmol": "kJ/mol"
        }
      },
      "description": "Computed enthalpy changes (ΔH) for all adsorption pathways of tar radicals on CaO, with identification of the most thermodynamically favorable pathways. Verified by structural audit: correct relative ordering of pathway types and consistency of marked favorable pathways with the paper's reported adsorption preferences."
    },
    {
      "file": "mulliken_tables.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "benzene": "array of pathway objects",
          "toluene": "array of pathway objects",
          "phenol": "array of pathway objects"
        },
        "items": {
          "pathway": "string",
          "nH_removed": "integer (1 or 2)",
          "min_mulliken_before": "float",
          "min_mulliken_after": "float",
          "percent_reduction": "float"
        }
      },
      "description": "Minimum aromatic C–C Mulliken populations before and after adsorption, with percent reduction, for the favorable pathways of each tar model compound. The percent reduction is compared within a tolerance to the paper‑reported values to confirm bond weakening."
    }
  ],
  "notes": "Only the favorable pathways (those identified as thermodynamically preferred in the enthalpy analysis) need to be reported in mulliken_tables.json. The checker recomputes percent reduction from the provided min_mulliken_before and min_mulliken_after, then compares to hidden gold values with tolerance. For enthalpy_changes.json, the checker verifies that the most_favorable flags match the paper's qualitative conclusions and that relative enthalpies follow the expected ordering (C–O–Ca more exothermic than C–Ca–O, etc.). Absolute ΔH values are accepted within a generous margin to accommodate code‑to‑code differences."
}
```

## How you are scored
A hidden verifier independently inspects both scored artifacts. For enthalpy_changes.json it checks that the flagged most_favorable pathways match the expected chemisorption preferences (e.g., C–O–Ca more exothermic than C–Ca–O, and C–C–Ca–O more favourable than paths involving oxygenated substituents) and that the correct pathways are flagged for each compound and dehydrogenation state. For mulliken_tables.json the verifier recomputes the percent reduction from your reported min_mulliken_before and min_mulliken_after and compares each value to a hidden reference within an acceptable tolerance; it also verifies that the relative catalytic activity order derived from the reductions is correct (e.g., which compound shows the largest average drop). The final reward is a weighted combination of these checks. Simply reporting numbers without performing the DFT calculations will not meet the scoring requirements.

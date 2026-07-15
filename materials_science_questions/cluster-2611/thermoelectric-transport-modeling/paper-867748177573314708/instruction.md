# Thermoelectric Transport in Puckered Group-V Monolayers

## Problem background
Group‑V element monolayers (As, Sb, Bi) can adopt a puckered honeycomb structure. This puckering turns the flat metallic layers into narrow‑gap semiconductors. Strong spin‑orbit coupling (SOI) further modifies the electronic bands, opens gaps at the Dirac points, and—together with very flat valence band edges—suggests that these monolayers might be efficient thermoelectric materials. The goal of this task is to compute the electronic band structure and the thermoelectric transport coefficients of puckered As, Sb, and Bi monolayers and thereby evaluate their potential for two‑dimensional thermoelectrics.

## Approach
The reproduction follows three main stages. First, density functional theory (DFT) calculations are used to fully optimise the puckered geometries of As, Sb, and Bi monolayers, with spin‑orbit coupling included. Second, self‑consistent DFT band structures are computed, with SOI, both along high‑symmetry paths and on a dense k‑mesh suitable for transport, for each system. For the Sb monolayer alone, an additional scan over the vertical sublattice displacement (puckering amplitude) is performed to locate the metal‑to‑semimetal and semimetal‑to‑semiconductor transitions. Third, the dense‑mesh band energies are fed into the BoltzTraP code, which solves the semiclassical Boltzmann transport equation in the constant relaxation‑time approximation. The resulting Seebeck coefficient is obtained as a function of temperature (up to about 800 K) and chemical potential, covering both p‑type and n‑type doping conditions for each material.

## Reproduction target
For puckered monolayers of As, Sb, and Bi, you must compute and report:

1. The two critical puckering distances for Sb (in Å) at which the monolayer transitions from metal to semimetal and from semimetal to semiconductor.
2. For each system, the direct band gap at the Γ point without SOI, the direct band gap at Γ with SOI, and the SOI‑induced gap at the upper Dirac point near K.
3. The peak p‑type and n‑type Seebeck coefficients (in µV/K) for As and Sb, and the peak p‑type Seebeck coefficient for Bi, evaluated in the temperature range 300–800 K. For Bi you must also determine whether bipolar suppression is observed—i.e., a sign reversal or a steep drop of the p‑type thermopower as temperature increases—and report it as a boolean flag.

All of these results must be written to the specified JSON files in /app/outputs, as detailed in the workflow steps and the output contract.

## Assets

- Quantum ESPRESSO (or equivalent open‑source DFT code): https://www.quantum-espresso.org/
- BoltzTraP: https://www.slip.net/boltzman/boltzman.html

## Workflow steps

### Step 1: DFT geometry optimization of puckered monolayers
- Role: process
- Action: Construct initial flat honeycomb geometries for As, Sb, Bi with a vacuum layer. Perform DFT structural relaxation allowing puckering, with spin‑orbit coupling included. Save the optimized atomic coordinates and total energies for the puckered phases of As, Sb, Bi as evidence.
- Evidence: `/app/outputs/optimized_structures.json`

### Step 2: Puckering displacement scan for Sb monolayer
- Role: process
- Action: For Sb monolayer only, perform a series of constrained DFT calculations where the vertical displacement d between A and B sublattice atoms is systematically varied from 0 (flat) to beyond the equilibrium puckering value. At each d, compute the band structure with SOI. Record the band gap evolution to identify the metal‑semimetal and semimetal‑semiconductor transitions.
- Evidence: `/app/outputs/puckering_scan_evidence.json`

### Step 3: Extract critical puckering distances (scored)
- Role: scored
- Action: From the band gap evolution obtained in step1, determine the critical vertical displacements at which the Sb monolayer transitions from metal to semimetal and from semimetal to semiconductor. Write the two distances in Å.
- Output file: `/app/outputs/puckering_critical_distances.json`
- Format: json
- Contract: {"d_metal_semimetal_A": "float", "d_semimetal_semiconductor_A": "float"}
- Scoring: scored by hidden verifier

### Step 4: DFT band structure calculations with SOI
- Role: process
- Action: Using the puckered geometries from step0, perform DFT band structure calculations for As, Sb, Bi with spin‑orbit coupling included. Compute eigenvalues along the Γ‑K‑M path and on a dense k‑mesh suitable for BoltzTraP. Calculate the band gaps (direct at Γ) with and without SOI, and identify the SOI‑induced gap at the upper Dirac point near K. Save the band structure data for downstream extraction.
- Evidence: `/app/outputs/band_structure_data.json`

### Step 5: Extract electronic properties (scored)
- Role: scored
- Action: From the band structures computed in step3, extract for each system (As, Sb, Bi) the direct band gap at Γ without SOI, the direct band gap at Γ with SOI, and the SOI‑induced gap at the upper Dirac point. Write these values in a structured JSON.
- Output file: `/app/outputs/electronic_properties.json`
- Format: json
- Contract: {"As": {"direct_gap_no_SOI_eV": "float", "direct_gap_with_SOI_eV": "float", "SOI_gap_at_DP_eV": "float"}, "Sb": {"direct_gap_no_SOI_eV": "float", "direct_gap_with_SOI_eV": "float", "SOI_gap_at_DP_eV": "float"}, "Bi": {"direct_gap_no_SOI_eV": "float", "direct_gap_with_SOI_eV": "float", "SOI_gap_at_DP_eV": "float"}}
- Scoring: scored by hidden verifier

### Step 6: Boltzmann transport calculation of thermopower
- Role: process
- Action: Use the dense k‑mesh band structure from step3 as input to BoltzTraP (constant relaxation time approximation). Compute the Seebeck coefficient S as a function of temperature and chemical potential (doping) for p‑type and n‑type carriers in As, Sb, Bi. Save the BoltzTraP output log.
- Evidence: `/app/outputs/boltztrap_output.log`

### Step 7: Thermopower summary (scored)
- Role: scored (load-bearing)
- Action: From the BoltzTraP results, determine the peak magnitude of the Seebeck coefficient for p‑type and n‑type doping in As and Sb, and the peak p‑type value in Bi. Assess whether bipolar suppression occurs at higher temperatures in Bi (sign change or sharp drop). Write the values and a bipolar suppression flag.
- Output file: `/app/outputs/thermopower_summary.json`
- Format: json
- Contract: {"As": {"peak_p_type_Seebeck_uV_per_K": "float", "peak_n_type_Seebeck_uV_per_K": "float"}, "Sb": {"peak_p_type_Seebeck_uV_per_K": "float", "peak_n_type_Seebeck_uV_per_K": "float"}, "Bi": {"peak_p_type_Seebeck_uV_per_K": "float", "bipolar_suppression_observed": "bool"}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/puckering_critical_distances.json`
- `/app/outputs/electronic_properties.json`
- `/app/outputs/thermopower_summary.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### puckering_critical_distances.json
- path: `/app/outputs/puckering_critical_distances.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Critical puckering displacement distances for Sb monolayer, where the transitions metal→semimetal and semimetal→semiconductor occur.
- schema:
  - `type`: object
  - `required`: `d_metal_semimetal_A`, `d_semimetal_semiconductor_A`
  - `properties`:
    - `d_metal_semimetal_A`:
      - `type`: number
      - `unit`: angstrom
    - `d_semimetal_semiconductor_A`:
      - `type`: number
      - `unit`: angstrom

### electronic_properties.json
- path: `/app/outputs/electronic_properties.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Direct band gaps at Γ (with and without spin‑orbit coupling) and the SOI‑induced gap at the upper Dirac point for As, Sb, Bi puckered monolayers.
- schema:
  - `type`: object
  - `required`: `As`, `Sb`, `Bi`
  - `properties`:
    - `As`:
      - `type`: object
      - `required`: `direct_gap_no_SOI_eV`, `direct_gap_with_SOI_eV`, `SOI_gap_at_DP_eV`
      - `properties`:
        - `direct_gap_no_SOI_eV`:
          - `type`: number
          - `unit`: eV
        - `direct_gap_with_SOI_eV`:
          - `type`: number
          - `unit`: eV
        - `SOI_gap_at_DP_eV`:
          - `type`: number
          - `unit`: eV
    - `Sb`:
      - `type`: object
      - `required`: `direct_gap_no_SOI_eV`, `direct_gap_with_SOI_eV`, `SOI_gap_at_DP_eV`
      - `properties`:
        - `direct_gap_no_SOI_eV`:
          - `type`: number
          - `unit`: eV
        - `direct_gap_with_SOI_eV`:
          - `type`: number
          - `unit`: eV
        - `SOI_gap_at_DP_eV`:
          - `type`: number
          - `unit`: eV
    - `Bi`:
      - `type`: object
      - `required`: `direct_gap_no_SOI_eV`, `direct_gap_with_SOI_eV`, `SOI_gap_at_DP_eV`
      - `properties`:
        - `direct_gap_no_SOI_eV`:
          - `type`: number
          - `unit`: eV
        - `direct_gap_with_SOI_eV`:
          - `type`: number
          - `unit`: eV
        - `SOI_gap_at_DP_eV`:
          - `type`: number
          - `unit`: eV

### thermopower_summary.json
- path: `/app/outputs/thermopower_summary.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Peak Seebeck coefficients for p‑type and n‑type carriers in As, Sb, peak p‑type Seebeck coefficient in Bi, and a flag indicating whether bipolar suppression is observed in Bi.
- schema:
  - `type`: object
  - `required`: `As`, `Sb`, `Bi`
  - `properties`:
    - `As`:
      - `type`: object
      - `required`: `peak_p_type_Seebeck_uV_per_K`, `peak_n_type_Seebeck_uV_per_K`
      - `properties`:
        - `peak_p_type_Seebeck_uV_per_K`:
          - `type`: number
          - `unit`: µV/K
        - `peak_n_type_Seebeck_uV_per_K`:
          - `type`: number
          - `unit`: µV/K
    - `Sb`:
      - `type`: object
      - `required`: `peak_p_type_Seebeck_uV_per_K`, `peak_n_type_Seebeck_uV_per_K`
      - `properties`:
        - `peak_p_type_Seebeck_uV_per_K`:
          - `type`: number
          - `unit`: µV/K
        - `peak_n_type_Seebeck_uV_per_K`:
          - `type`: number
          - `unit`: µV/K
    - `Bi`:
      - `type`: object
      - `required`: `peak_p_type_Seebeck_uV_per_K`, `bipolar_suppression_observed`
      - `properties`:
        - `peak_p_type_Seebeck_uV_per_K`:
          - `type`: number
          - `unit`: µV/K
        - `bipolar_suppression_observed`:
          - `type`: boolean

Notes: SbAs and BiSb are not included as scored targets; the paper's main thermoelectric and puckering results are for the pure group‑V monolayers. The omitted binaries are not required for the core reproduction and their absence does not degrade the verifiability of the principal claims.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "puckering_critical_distances.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "d_metal_semimetal_A",
          "d_semimetal_semiconductor_A"
        ],
        "properties": {
          "d_metal_semimetal_A": {
            "type": "number",
            "unit": "angstrom"
          },
          "d_semimetal_semiconductor_A": {
            "type": "number",
            "unit": "angstrom"
          }
        }
      },
      "description": "Critical puckering displacement distances for Sb monolayer, where the transitions metal→semimetal and semimetal→semiconductor occur."
    },
    {
      "file": "electronic_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "As",
          "Sb",
          "Bi"
        ],
        "properties": {
          "As": {
            "type": "object",
            "required": [
              "direct_gap_no_SOI_eV",
              "direct_gap_with_SOI_eV",
              "SOI_gap_at_DP_eV"
            ],
            "properties": {
              "direct_gap_no_SOI_eV": {
                "type": "number",
                "unit": "eV"
              },
              "direct_gap_with_SOI_eV": {
                "type": "number",
                "unit": "eV"
              },
              "SOI_gap_at_DP_eV": {
                "type": "number",
                "unit": "eV"
              }
            }
          },
          "Sb": {
            "type": "object",
            "required": [
              "direct_gap_no_SOI_eV",
              "direct_gap_with_SOI_eV",
              "SOI_gap_at_DP_eV"
            ],
            "properties": {
              "direct_gap_no_SOI_eV": {
                "type": "number",
                "unit": "eV"
              },
              "direct_gap_with_SOI_eV": {
                "type": "number",
                "unit": "eV"
              },
              "SOI_gap_at_DP_eV": {
                "type": "number",
                "unit": "eV"
              }
            }
          },
          "Bi": {
            "type": "object",
            "required": [
              "direct_gap_no_SOI_eV",
              "direct_gap_with_SOI_eV",
              "SOI_gap_at_DP_eV"
            ],
            "properties": {
              "direct_gap_no_SOI_eV": {
                "type": "number",
                "unit": "eV"
              },
              "direct_gap_with_SOI_eV": {
                "type": "number",
                "unit": "eV"
              },
              "SOI_gap_at_DP_eV": {
                "type": "number",
                "unit": "eV"
              }
            }
          }
        }
      },
      "description": "Direct band gaps at Γ (with and without spin‑orbit coupling) and the SOI‑induced gap at the upper Dirac point for As, Sb, Bi puckered monolayers."
    },
    {
      "file": "thermopower_summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "As",
          "Sb",
          "Bi"
        ],
        "properties": {
          "As": {
            "type": "object",
            "required": [
              "peak_p_type_Seebeck_uV_per_K",
              "peak_n_type_Seebeck_uV_per_K"
            ],
            "properties": {
              "peak_p_type_Seebeck_uV_per_K": {
                "type": "number",
                "unit": "µV/K"
              },
              "peak_n_type_Seebeck_uV_per_K": {
                "type": "number",
                "unit": "µV/K"
              }
            }
          },
          "Sb": {
            "type": "object",
            "required": [
              "peak_p_type_Seebeck_uV_per_K",
              "peak_n_type_Seebeck_uV_per_K"
            ],
            "properties": {
              "peak_p_type_Seebeck_uV_per_K": {
                "type": "number",
                "unit": "µV/K"
              },
              "peak_n_type_Seebeck_uV_per_K": {
                "type": "number",
                "unit": "µV/K"
              }
            }
          },
          "Bi": {
            "type": "object",
            "required": [
              "peak_p_type_Seebeck_uV_per_K",
              "bipolar_suppression_observed"
            ],
            "properties": {
              "peak_p_type_Seebeck_uV_per_K": {
                "type": "number",
                "unit": "µV/K"
              },
              "bipolar_suppression_observed": {
                "type": "boolean"
              }
            }
          }
        }
      },
      "description": "Peak Seebeck coefficients for p‑type and n‑type carriers in As, Sb, peak p‑type Seebeck coefficient in Bi, and a flag indicating whether bipolar suppression is observed in Bi."
    }
  ],
  "notes": "SbAs and BiSb are not included as scored targets; the paper's main thermoelectric and puckering results are for the pure group‑V monolayers. The omitted binaries are not required for the core reproduction and their absence does not degrade the verifiability of the principal claims."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that reads the scored output files you place under /app/outputs. Each artifact is checked independently:

- The puckering distances are compared to a hidden reference with an exact‑match tolerance (small allowed deviation).
- The band gaps and the Seebeck coefficients are scored by a threshold‑or‑better policy: you earn full credit if your computed value meets or exceeds a hidden threshold derived from the paper’s prediction, and a physically better result (e.g., a higher Seebeck coefficient for the same material and doping type) is never penalised.
- The bipolar‑suppression flag for Bi is checked for correctness.

The final reward is a weighted sum of the scores on the three scored artifacts, with the thermopower summary carrying the largest weight. Reporting numbers without genuinely executing the DFT and transport workflow will not suffice; the verifier expects values that are a plausible outcome of the full computational pipeline.

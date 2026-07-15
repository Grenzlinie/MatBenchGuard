# First-principles Study of Electronic, Phononic, and Thermoelectric Properties of Graphyne Sheets

## Problem background
Graphynes are two-dimensional carbon allotropes containing sp‑ and sp²‑hybridized bonds, which makes them promising for thermoelectric applications. This investigation systematically examines the electronic band structures and thermoelectric performance of several graphyne variants (α‑, β‑, γ‑, and 6,6,12‑graphyne) and compares them with graphene. The electronic behavior ranges from Dirac semimetals to a semiconductor; quantifying the band gap and Dirac point locations, and determining the maximum thermoelectric figure of merit, are essential to evaluate their suitability for energy conversion.

## Approach
The approach uses density functional theory (DFT) with the Perdew–Burke–Ernzerhof (PBE) generalized gradient approximation to optimize geometries and compute electronic band structures for all five materials. Phonon dispersions are obtained via density functional perturbation theory (DFPT). From the electronic band structures and phonon dispersions, ballistic transport calculations yield the electronic transmission spectrum, the Seebeck coefficient, the electrical and phononic thermal conductances, and finally the thermoelectric figure of merit ZT. The workflow compares the five materials side‑by‑side, classifying which ones exhibit Dirac‑like dispersion (massless Dirac fermions) and which are semiconducting, and evaluates which achieves the highest ZT at 300 K.

## Reproduction target
Using open‑source tools (Quantum ESPRESSO and PHONOPY) with publicly available PBE pseudopotentials, execute the full DFT + DFPT + ballistic transport pipeline to produce two scored artifacts:

1. `band_gap_dirac.json` – a JSON object that maps each material (α‑graphyne, β‑graphyne, γ‑graphyne, 6,6,12‑graphyne, graphene) to its band gap in eV and a list of k‑point labels where Dirac crossings occur.
2. `ZT_gamma_graphyne.json` – a JSON object that contains the maximum ZT value for γ‑graphyne at 300 K.

The classification must correctly identify γ‑graphyne as the semiconductor and the other materials as Dirac semimetals, with the corresponding gap sizes and Dirac point locations.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PHONOPY: https://phonopy.github.io/phonopy/
- PBE pseudopotentials (SSSP efficiency library): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: DFT geometry optimization
- Role: process
- Action: Perform DFT geometry optimization for α‑, β‑, γ‑, 6,6,12‑graphyne and graphene using Quantum ESPRESSO with PBE pseudopotentials to obtain relaxed lattice constants and atomic positions.
- Evidence: `/app/outputs/optimization_logs.txt`

### Step 2: Electronic band structure calculation
- Role: process
- Action: Compute electronic band structures along standard high‑symmetry k‑point paths for each relaxed material using Quantum ESPRESSO.
- Evidence: `/app/outputs/band_data.tar.gz`

### Step 3: Band gap and Dirac point classification
- Role: scored (load-bearing)
- Action: Analyze the computed electronic band structures to determine the band gap (valence‑to‑conduction energy difference at each k‑point) and identify Dirac points (single k‑point crossings between the top valence and bottom conduction bands). Produce a JSON file with the classification for each material.
- Output file: `/app/outputs/band_gap_dirac.json`
- Format: json
- Contract: {"type":"object", "required":["materials"], "properties":{"materials":{"type":"object", "additionalProperties":{"type":"object", "required":["band_gap_ev","dirac_points"], "properties":{"band_gap_ev":{"type":"number"},"dirac_points":{"type":"array", "items":{"type":"string"}}}}}}}
- Scoring: scored by hidden verifier

### Step 4: Phonon dispersion calculation
- Role: process
- Action: Compute phonon dispersions for all materials using density functional perturbation theory (DFPT) as implemented in Quantum ESPRESSO and post‑processed with PHONOPY. Use the supercell dimensions and Γ‑centered k‑point grids specified in the original study.
- Evidence: `/app/outputs/phonon_data.tar.gz`

### Step 5: Ballistic transport calculations
- Role: process
- Action: From the electronic band structures, compute electronic transmission spectra. From the phonon dispersions, compute phonon transmission spectra. Then calculate the electronic transport coefficients (electrical conductance G, Seebeck coefficient S, electronic thermal conductance κ_el) using the standard ballistic transport formulas, and phonon thermal conductance κ_ph for all materials at 300 K.
- Evidence: `/app/outputs/transport_data.tar.gz`

### Step 6: Thermoelectric figure of merit ZT
- Role: scored (load-bearing)
- Action: Compute the thermoelectric figure of merit ZT = S² G T / (κ_el + κ_ph) as a function of chemical potential for γ‑graphyne at 300 K using the transport coefficients from the previous step, and extract the maximum ZT value. Output the result as a JSON file.
- Output file: `/app/outputs/ZT_gamma_graphyne.json`
- Format: json
- Contract: {"type":"object", "required":["max_ZT_300K"], "properties":{"max_ZT_300K":{"type":"number"}}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gap_dirac.json`
- `/app/outputs/ZT_gamma_graphyne.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gap_dirac.json
- path: `/app/outputs/band_gap_dirac.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Electronic band gap (eV) and Dirac point locations for α‑, β‑, γ‑, 6,6,12‑graphyne and graphene.
- schema:
  - `type`: object
  - `required`:
    - `materials`: object
  - `properties`:
    - `materials`:
      - `type`: object
      - `additionalProperties`:
        - `type`: object
        - `required`: `band_gap_ev`, `dirac_points`
        - `properties`:
          - `band_gap_ev`:
            - `type`: number
            - `description`: band gap in eV
          - `dirac_points`:
            - `type`: array
            - `items`:
              - `type`: string
            - `description`: list of k‑point labels where Dirac crossings occur

### ZT_gamma_graphyne.json
- path: `/app/outputs/ZT_gamma_graphyne.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Maximum ZT for γ‑graphyne at 300 K, derived from ballistic transport calculations.
- schema:
  - `type`: object
  - `required`:
    - `max_ZT_300K`: number
  - `properties`:
    - `max_ZT_300K`:
      - `type`: number
      - `description`: maximum thermoelectric figure of merit for γ‑graphyne at 300 K

Notes: The checker compares the reported band gap of γ‑graphyne to the paper value (0.5 eV) with a tolerance of ±0.1 eV, verifies that the other materials have a gap ≤ 0.05 eV, and checks that Dirac point locations are present for graphene and the Dirac‑graphynes. For ZT, the checker verifies that max_ZT_300K lies in the interval [0.30, 0.55].

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gap_dirac.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "materials": "object"
        },
        "properties": {
          "materials": {
            "type": "object",
            "additionalProperties": {
              "type": "object",
              "required": [
                "band_gap_ev",
                "dirac_points"
              ],
              "properties": {
                "band_gap_ev": {
                  "type": "number",
                  "description": "band gap in eV"
                },
                "dirac_points": {
                  "type": "array",
                  "items": {
                    "type": "string"
                  },
                  "description": "list of k‑point labels where Dirac crossings occur"
                }
              }
            }
          }
        }
      },
      "description": "Electronic band gap (eV) and Dirac point locations for α‑, β‑, γ‑, 6,6,12‑graphyne and graphene."
    },
    {
      "file": "ZT_gamma_graphyne.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "max_ZT_300K": "number"
        },
        "properties": {
          "max_ZT_300K": {
            "type": "number",
            "description": "maximum thermoelectric figure of merit for γ‑graphyne at 300 K"
          }
        }
      },
      "description": "Maximum ZT for γ‑graphyne at 300 K, derived from ballistic transport calculations."
    }
  ],
  "notes": "The checker compares the reported band gap of γ‑graphyne to the paper value (0.5 eV) with a tolerance of ±0.1 eV, verifies that the other materials have a gap ≤ 0.05 eV, and checks that Dirac point locations are present for graphene and the Dirac‑graphynes. For ZT, the checker verifies that max_ZT_300K lies in the interval [0.30, 0.55]."
}
```

## How you are scored
A hidden verifier independently inspects your submitted `band_gap_dirac.json` and `ZT_gamma_graphyne.json` and compares them against a hidden gold derived from the original study. Because the band gap and ZT are directional quantities, you receive full credit if your computed results meet or exceed the expected agreement; if they deviate beyond a certain tolerance, partial credit is awarded. The checker also audits that Dirac points are provided for the materials where they are expected. No credit is given for merely reporting the paper’s published numbers—you must genuinely run the workflow and produce results that fall within an acceptable range.

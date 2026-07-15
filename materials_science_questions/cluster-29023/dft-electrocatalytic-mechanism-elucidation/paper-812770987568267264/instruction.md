# DFT Selectivity Descriptor for Ni-N-C vs N-C CO2RR Catalysts

## Problem background
Electrocatalytic reduction of CO2 to fuels and chemicals is a promising route to utilize greenhouse gases. Nitrogen‑doped carbon (N‑C) materials are attractive low‑cost catalysts, but their activity and selectivity for CO2 reduction over the competing hydrogen evolution reaction (HER) remain limited. Single‑atom metal doping has been proposed as a strategy to modify the surface chemistry of N‑C and improve performance. In this work, density functional theory (DFT) is used to investigate whether a single Ni atom embedded in an N‑C matrix can alter the energetics of key reaction intermediates and thereby influence the competition between CO2 reduction and HER. The central computational question is how the difference in limiting potentials between CO2 reduction to CO (UL_CO2) and hydrogen evolution (UL_H2) changes when going from a pure N‑C catalyst to a Ni‑doped N‑C catalyst.

## Approach
Two atomistic models are considered: an N‑doped graphene sheet with pyridinic nitrogen defects (N‑C), and a Ni single atom coordinated by four pyridinic N atoms in a graphene sheet (Ni‑N‑C). Spin‑polarized DFT calculations are performed with the PBE functional including the D3 dispersion correction. A plane‑wave basis set and periodic slab models are used. Total energies are computed for the clean surface and for adsorbed *COOH, *CO, and *H intermediates on both catalysts, as well as for gas‑phase CO2, CO, and H2. From these total energies, Gibbs free energies are obtained via the computational hydrogen electrode (CHE) model at 298.15 K, using zero‑point energy and entropy corrections. Free‑energy diagrams are constructed for the CO2 reduction pathway (* + CO2 → *COOH → *CO → * + CO) and for the hydrogen evolution pathway (H⁺ + e⁻ → *H → 1/2 H2). Limiting potentials UL_CO2 and UL_H2 are determined from the free‑energy profiles, and the selectivity descriptor ΔUL = UL_CO2 − UL_H2 is computed for each catalyst. The comparison of ΔUL between N‑C and Ni‑N‑C provides a mechanistic indicator of whether single‑atom Ni doping suppresses HER and promotes CO2 reduction.

## Reproduction target
Construct the N‑C and Ni‑N‑C models, perform the DFT calculations described above to obtain total energies for all surface and gas‑phase species, and compute the free energies, limiting potentials, and the selectivity descriptor ΔUL for both catalysts. The primary deliverable is a structured JSON file (`dft_energies.json`) that contains the total energies, gas‑phase energies, and the derived UL_CO2, UL_H2, and ΔUL for each catalyst. The objective is to determine whether the computed ΔUL for Ni‑N‑C is more positive than that for N‑C, consistent with enhanced CO2RR selectivity.

## Assets

- Quantum ESPRESSO (or equivalent plane-wave DFT code implementing PBE+D3): https://www.quantum-espresso.org
- Atomic Simulation Environment (ASE): ase

## Workflow steps

### Step 1: Model construction and DFT total energy calculations
- Role: process
- Action: Build atomistic models of N-C (graphene with pyridinic N defects) and Ni-N-C (a single Ni atom coordinated by four pyridinic N in a graphene sheet). Perform spin-polarized DFT calculations using a plane-wave basis and the PBE+D3 functional to optimize geometries and compute total energies for the clean slabs and for *COOH, *CO, and *H adsorbates on both catalysts. Also compute total energies of gas-phase CO2, CO, and H2.
- Evidence: `/app/outputs/dft_calculation_log.txt`

### Step 2: Free energy analysis and selectivity descriptor
- Role: scored (load-bearing)
- Action: From the total energies obtained in Step 1, apply zero-point energy and entropy corrections (standard computational hydrogen electrode model at 298.15 K) to compute Gibbs free energies for all states. Determine limiting potentials UL_CO2 and UL_H2 for N-C and Ni-N-C, and compute UL_diff = UL_CO2 - UL_H2. Write all total energies (clean, *COOH, *CO, *H), gas energies (CO2, CO, H2), and the derived UL values to a structured JSON file.
- Output file: `/app/outputs/dft_energies.json`
- Format: json
- Contract: {"N-C": {"total_energies": {"clean": <float>, "*COOH": <float>, "*CO": <float>, "*H": <float>}, "gas_energies": {"CO2": <float>, "CO": <float>, "H2": <float>}, "UL_CO2": <float>, "UL_H2": <float>, "UL_diff": <float>}, "Ni-N-C": { same structure }}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dft_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dft_energies.json
- path: `/app/outputs/dft_energies.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Free-energy analysis for N-C and Ni-N-C catalysts; total energies and derived limiting potentials. The checker recomputes free energies from total energies and verifies that UL_diff(Ni-N-C) > UL_diff(N-C) by at least 0.05 eV (selectivity trend). Energies in eV; UL values in V.
- schema:
  - `type`: object
  - `required`:
    - `N-C`:
      - `type`: object
      - `required`:
        - `total_energies`:
          - `clean`: float (eV)
          - `*COOH`: float (eV)
          - `*CO`: float (eV)
          - `*H`: float (eV)
        - `gas_energies`:
          - `CO2`: float (eV)
          - `CO`: float (eV)
          - `H2`: float (eV)
        - `UL_CO2`: float (V)
        - `UL_H2`: float (V)
        - `UL_diff`: float (V)
    - `Ni-N-C`:
      - `type`: object
      - `required`:
        - `total_energies`:
          - `clean`: float (eV)
          - `*COOH`: float (eV)
          - `*CO`: float (eV)
          - `*H`: float (eV)
        - `gas_energies`:
          - `CO2`: float (eV)
          - `CO`: float (eV)
          - `H2`: float (eV)
        - `UL_CO2`: float (V)
        - `UL_H2`: float (V)
        - `UL_diff`: float (V)

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dft_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "N-C": {
            "type": "object",
            "required": {
              "total_energies": {
                "clean": "float (eV)",
                "*COOH": "float (eV)",
                "*CO": "float (eV)",
                "*H": "float (eV)"
              },
              "gas_energies": {
                "CO2": "float (eV)",
                "CO": "float (eV)",
                "H2": "float (eV)"
              },
              "UL_CO2": "float (V)",
              "UL_H2": "float (V)",
              "UL_diff": "float (V)"
            }
          },
          "Ni-N-C": {
            "type": "object",
            "required": {
              "total_energies": {
                "clean": "float (eV)",
                "*COOH": "float (eV)",
                "*CO": "float (eV)",
                "*H": "float (eV)"
              },
              "gas_energies": {
                "CO2": "float (eV)",
                "CO": "float (eV)",
                "H2": "float (eV)"
              },
              "UL_CO2": "float (V)",
              "UL_H2": "float (V)",
              "UL_diff": "float (V)"
            }
          }
        }
      },
      "description": "Free-energy analysis for N-C and Ni-N-C catalysts; total energies and derived limiting potentials. The checker recomputes free energies from total energies and verifies that UL_diff(Ni-N-C) > UL_diff(N-C) by at least 0.05 eV (selectivity trend). Energies in eV; UL values in V."
    }
  ],
  "notes": ""
}
```

## How you are scored
Your output will be evaluated by a hidden verifier that independently recomputes Gibbs free energies from the total energies you report in `dft_energies.json`, applies the standard CHE corrections, and checks the structural trend in the selectivity descriptor ΔUL between the two catalysts. The verifier also inspects the integrity and completeness of the submitted JSON file. The final reward is a weighted combination of these checks. No gold values or tolerances are published; the verifier uses a hidden reference to assess correctness.

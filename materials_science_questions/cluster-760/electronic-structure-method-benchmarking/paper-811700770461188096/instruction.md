# DFT Investigation of Electron Affinities and Singlet-Triplet Gaps of XGeCY3 Germylenes

## Problem background
Germylenes (divalent germanium compounds) exhibit intriguing bonding and find applications in materials and catalysis. Electron affinities and singlet-triplet gaps are critical properties that govern their reactivity and stability. This task computationally determines these properties for a series of halogenated germylenes, XGeCY₃, using density functional theory (DFT), providing benchmark data for interpreting experimental observations and validating theoretical models.

## Approach
The properties are computed at the density functional theory (DFT) level using the BHLYP hybrid functional. Custom double‑ζ plus polarization and diffuse (DZP++) basis sets are used for all atoms except iodine, which is treated with the 6-311G(d,p) basis. For each of the ten conventional XGeCY₃ molecules (X = H, F, Cl, Br, I; Y = F, Cl), unrestricted DFT geometry optimizations and harmonic vibrational frequency calculations are performed for the neutral singlet, anionic doublet, and lowest‑lying neutral triplet states. From the resulting total electronic energies and zero‑point vibrational energies (ZPVE), four measures of the electron affinity (adiabatic, zero‑point corrected adiabatic, vertical, and vertical detachment) and the singlet‑triplet energy splitting are derived. The calculations are carried out with an open‑source quantum chemistry package (e.g., Psi4) that supports unrestricted DFT, custom basis sets, and the BHLYP functional.

## Reproduction target
For each of the ten conventional XGeCY₃ systems (X = H, F, Cl, Br, I; Y = F, Cl), compute at the BHLYP/DZP++ (6‑311G(d,p) for iodine) level:

* the adiabatic electron affinity (EA_ad),
* the zero‑point corrected adiabatic electron affinity (EA_ad(ZPVE)),
* the vertical electron affinity (VEA),
* the vertical detachment energy (VDE),
* the singlet‑triplet gap (ΔE_S‑T).

Provide the raw total energies and zero‑point energies (in Hartree) together with the derived quantities (in eV) for all ten molecules in a single JSON file (results.json). The required format and keys are specified in the output contract.

## Assets

- Psi4 (or equivalent open-source quantum chemistry package e.g. NWChem, PySCF): https://psicode.org/

## Workflow steps

### Step 1: Prepare DZP++ basis sets and input configurations
- Role: process
- Action: Construct the DZP++ basis sets for H, C, F, Cl, Br, Ge using even-tempered diffuse functions and polarization functions as described in the paper (Huzinaga–Dunning–Hay/Ahlrichs sets) and use 6-311G(d,p) for iodine.  Generate input configurations for all 30 molecular systems (10 neutral singlet, 10 anion doublet, 10 triplet) with the BHLYP functional, an extended integration grid, and very tight convergence criteria.
- Evidence: `/app/outputs/basis_construction.log`

### Step 2: Run DFT geometry optimizations and frequency calculations
- Role: process
- Action: Using an open-source quantum chemistry package, perform unrestricted DFT geometry optimizations and harmonic vibrational frequency analyses for each of the 30 molecular systems.  Verify that all stationary points correspond to minima (all real frequencies).  Record the total electronic energies and zero-point vibrational energies for each system.
- Evidence: `/app/outputs/optimization_log.txt`

### Step 3: Compute electron affinities and singlet-triplet gaps
- Role: scored (load-bearing)
- Action: From the raw DFT energies and zero-point vibrational energies, compute for each of the ten XGeCY3 molecules (X = H, F, Cl, Br, I; Y = F, Cl) the following quantities: adiabatic electron affinity EA_ad, zero‑point‑corrected adiabatic electron affinity EA_ad(ZPVE), vertical electron affinity VEA, vertical detachment energy VDE, and singlet‑triplet gap S_T_gap.  Express raw energies in Hartree and derived quantities in eV.  Output the results as a single JSON file.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: The output JSON must contain a top-level key "molecules" holding an array of 10 objects, each with the following fields:
  - "name": string (e.g., "HGeCF3")
  - "E_neutral": number (Hartree)
  - "ZPVE_neutral": number (Hartree)
  - "E_anion": number (Hartree)
  - "ZPVE_anion": number (Hartree)
  - "E_neutral_at_anion_geom": number (Hartree)
  - "E_anion_at_neutral_geom": number (Hartree)
  - "E_triplet": number (Hartree)
  - "EA_ad": number (eV)
  - "EA_ad_ZPVE": number (eV)
  - "VEA": number (eV)
  - "VDE": number (eV)
  - "S_T_gap": number (eV)
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
- target_policy: metric_recompute
- description: Scored artifact containing raw total energies (Hartree), zero-point energies (Hartree), and derived electron affinities and singlet-triplet gaps (eV) for all ten conventional XGeCY3 species. The checker recomputes the derived quantities from the raw energies and compares them against hidden gold paper values with tolerances.
- schema:
  - `type`: object
  - `properties`:
    - `molecules`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `name`:
            - `type`: string
          - `E_neutral`:
            - `type`: number
            - `description`: Total energy of neutral singlet (Hartree)
          - `ZPVE_neutral`:
            - `type`: number
            - `description`: Zero-point vibrational energy of neutral (Hartree)
          - `E_anion`:
            - `type`: number
            - `description`: Total energy of anion doublet (Hartree)
          - `ZPVE_anion`:
            - `type`: number
            - `description`: Zero-point vibrational energy of anion (Hartree)
          - `E_neutral_at_anion_geom`:
            - `type`: number
            - `description`: Single point energy of neutral at optimized anion geometry (Hartree)
          - `E_anion_at_neutral_geom`:
            - `type`: number
            - `description`: Single point energy of anion at optimized neutral geometry (Hartree)
          - `E_triplet`:
            - `type`: number
            - `description`: Total energy of lowest triplet state (Hartree)
          - `EA_ad`:
            - `type`: number
            - `description`: Adiabatic electron affinity (eV)
          - `EA_ad_ZPVE`:
            - `type`: number
            - `description`: Zero-point corrected adiabatic electron affinity (eV)
          - `VEA`:
            - `type`: number
            - `description`: Vertical electron affinity (eV)
          - `VDE`:
            - `type`: number
            - `description`: Vertical detachment energy (eV)
          - `S_T_gap`:
            - `type`: number
            - `description`: Singlet-triplet gap (eV)
        - `required`: `name`, `E_neutral`, `ZPVE_neutral`, `E_anion`, `ZPVE_anion`, `E_neutral_at_anion_geom`, `E_anion_at_neutral_geom`, `E_triplet`, `EA_ad`, `EA_ad_ZPVE`, `VEA`, `VDE`, `S_T_gap`
  - `required`: `molecules`
  - `required_columns`:
  - `units`: object

Notes: All reported energies correspond to the BHLYP functional with DZP++ basis sets (6-311G(d,p) for iodine). The ten molecules are: HGeCF3, FGeCF3, ClGeCF3, BrGeCF3, IGeCF3, HGeCCl3, FGeCCl3, ClGeCCl3, BrGeCCl3, IGeCCl3. Only the BHLYP results are scored.

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
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "properties": {
          "molecules": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "name": {
                  "type": "string"
                },
                "E_neutral": {
                  "type": "number",
                  "description": "Total energy of neutral singlet (Hartree)"
                },
                "ZPVE_neutral": {
                  "type": "number",
                  "description": "Zero-point vibrational energy of neutral (Hartree)"
                },
                "E_anion": {
                  "type": "number",
                  "description": "Total energy of anion doublet (Hartree)"
                },
                "ZPVE_anion": {
                  "type": "number",
                  "description": "Zero-point vibrational energy of anion (Hartree)"
                },
                "E_neutral_at_anion_geom": {
                  "type": "number",
                  "description": "Single point energy of neutral at optimized anion geometry (Hartree)"
                },
                "E_anion_at_neutral_geom": {
                  "type": "number",
                  "description": "Single point energy of anion at optimized neutral geometry (Hartree)"
                },
                "E_triplet": {
                  "type": "number",
                  "description": "Total energy of lowest triplet state (Hartree)"
                },
                "EA_ad": {
                  "type": "number",
                  "description": "Adiabatic electron affinity (eV)"
                },
                "EA_ad_ZPVE": {
                  "type": "number",
                  "description": "Zero-point corrected adiabatic electron affinity (eV)"
                },
                "VEA": {
                  "type": "number",
                  "description": "Vertical electron affinity (eV)"
                },
                "VDE": {
                  "type": "number",
                  "description": "Vertical detachment energy (eV)"
                },
                "S_T_gap": {
                  "type": "number",
                  "description": "Singlet-triplet gap (eV)"
                }
              },
              "required": [
                "name",
                "E_neutral",
                "ZPVE_neutral",
                "E_anion",
                "ZPVE_anion",
                "E_neutral_at_anion_geom",
                "E_anion_at_neutral_geom",
                "E_triplet",
                "EA_ad",
                "EA_ad_ZPVE",
                "VEA",
                "VDE",
                "S_T_gap"
              ]
            }
          }
        },
        "required": [
          "molecules"
        ],
        "required_columns": [],
        "units": {}
      },
      "description": "Scored artifact containing raw total energies (Hartree), zero-point energies (Hartree), and derived electron affinities and singlet-triplet gaps (eV) for all ten conventional XGeCY3 species. The checker recomputes the derived quantities from the raw energies and compares them against hidden gold paper values with tolerances."
    }
  ],
  "notes": "All reported energies correspond to the BHLYP functional with DZP++ basis sets (6-311G(d,p) for iodine). The ten molecules are: HGeCF3, FGeCF3, ClGeCF3, BrGeCF3, IGeCF3, HGeCCl3, FGeCCl3, ClGeCCl3, BrGeCCl3, IGeCCl3. Only the BHLYP results are scored."
}
```

## How you are scored
A hidden verifier evaluates each workflow stage independently. For the scored artifact (results.json), the verifier recomputes all derived quantities (EA_ad, EA_ad(ZPVE), VEA, VDE, ΔE_S‑T) from the raw energy values you supply. It compares the recomputed values against the accepted reference values (obtained at the BHLYP/DZP++ level of theory) within tolerances that account for legitimate differences in implementation and numerical settings.  Each scored workflow stage contributes a predetermined weight to the final reward.

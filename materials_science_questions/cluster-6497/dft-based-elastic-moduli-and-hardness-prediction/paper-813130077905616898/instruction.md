# Zero-pressure elastic moduli and Vickers hardness of α- and β-Be₃N₂ from DFT

## Problem background
Beryllium nitride (Be3N2) crystallizes in two ambient-pressure phases: cubic α (space group Ia-3) and hexagonal β (space group P63/mmc). Both phases are candidates for hard materials. A reliable assessment of their mechanical properties requires first-principles density functional theory (DFT) calculations to compute the single-crystal elastic stiffness constants, from which polycrystalline bulk modulus, shear modulus, Young's modulus, Poisson's ratio and an empirical Vickers hardness estimate can be derived. This task aims to compute these elastic and mechanical properties at zero pressure.

## Approach
First-principles DFT using the local-density approximation (LDA) for exchange-correlation. The workflow: (1) geometry relaxation of both crystal structures at zero pressure; (2) computation of the elastic stiffness tensor Cij via the stress–strain method; (3) polycrystalline moduli obtained via Voigt-Reuss-Hill (VRH) averaging of the elastic constants, then Young's modulus (E = 9BG/(3B+G)) and Poisson's ratio (ν = (3B-2G)/(2(3B+G))). The Vickers hardness (Hv) is estimated using Chen's empirical model: Hv = 2·(k²G)^0.585 − 3, where k = G/B. The calculations are performed with an open-source DFT code such as Quantum ESPRESSO (QE).

## Reproduction target
Produce a JSON file (`elastic_and_derived_moduli.json`) containing, for both α and β phases, the computed elastic constants (C11, C44, C12 for cubic α; C11, C33, C44, C12, C13 for hexagonal β; all values in GPa) and the derived polycrystalline moduli: Voigt-Reuss-Hill average bulk modulus (B_VRH), shear modulus (G_VRH), Young's modulus (E), Poisson's ratio (ν), and Vickers hardness (H_V). The file must be written to `/app/outputs/`.

## Assets

- Quantum ESPRESSO DFT package: Open-source DFT code (https://www.quantum-espresso.org/). Install via package manager (e.g., conda install -c conda-forge qe).
- Be pseudopotential (LDA): SSSP efficiency library (https://www.materialscloud.org/discover/sssp/table) or generate on-the-fly.
- N pseudopotential (LDA): SSSP efficiency library (https://www.materialscloud.org/discover/sssp/table) or generate on-the-fly.
- Crystal structure of β-Be3N2: Hexagonal P6_3/mmc (No. 194), a_exp=2.841 Å, c_exp=9.693 Å (Eckerlin & Rabenau, Z. Anorg. Allg. Chem. 304, 218, 1960, DOI: 10.1002/zaac.19603040410).
- Crystal structure of α-Be3N2: Cubic Ia-3 (No. 206), a_exp=8.145 Å (Reckeweg et al., Z. Naturforsch. B 58, 159, 2003, DOI: 10.1515/znb-2003-0205).

## Workflow steps

### Step 1: Geometry relaxation at zero pressure
- Role: process
- Action: Perform DFT geometry optimization for α-Be3N2 (cubic, space group Ia-3) and β-Be3N2 (hexagonal, space group P6_3/mmc) at zero pressure using the LDA exchange-correlation functional. Relax cell parameters and atomic positions until forces are below a tight convergence threshold.
- Evidence: `/app/outputs/relaxed_structures.json`

### Step 2: Elastic constants calculation at zero pressure
- Role: process
- Action: Compute the elastic stiffness tensor C_ij for the relaxed α and β structures using the stress–strain method within DFT at zero pressure. The calculation yields the independent elastic constants: C11, C44, C12 for α (cubic) and C11, C33, C44, C12, C13 for β (hexagonal).
- Evidence: `/app/outputs/elastic_constants_raw.json`

### Step 3: Derive polycrystalline moduli and Vickers hardness
- Role: scored (load-bearing)
- Action: From the computed elastic constants, calculate the Voigt and Reuss bounds for the bulk and shear moduli, then apply the Hill average to obtain B_VRH and G_VRH. Compute Young's modulus E = 9BG/(3B+G) and Poisson's ratio ν = (3B-2G)/(2(3B+G)). Compute the Vickers hardness using Chen's model: H_V = 2·(k² G)^0.585 − 3 where k = G/B. Package the elastic constants and all derived moduli for both α and β phases into a single JSON file.
- Output file: `/app/outputs/elastic_and_derived_moduli.json`
- Format: json
- Contract: JSON object with keys 'alpha' and 'beta'. Each object contains 'elastic_constants' (object with keys 'C11','C44','C12' for alpha; 'C11','C33','C44','C12','C13' for beta; all values in GPa) and 'derived_moduli' (object with keys 'B_VRH','G_VRH','E','Poisson_ratio','Vickers_hardness'; values in GPa except Poisson_ratio dimensionless).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/elastic_and_derived_moduli.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### elastic_and_derived_moduli.json
- path: `/app/outputs/elastic_and_derived_moduli.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Scored artifact containing the single-crystal elastic constants and the derived Voigt-Reuss-Hill polycrystalline moduli and Chen Vickers hardness for both α- and β-Be3N2. The checker recomputes B_VRH, G_VRH, E, Poisson_ratio, and Vickers_hardness from the provided elastic constants and scores against the paper's LDA reference values.
- schema:
  - `type`: object
  - `required_keys`: `alpha`, `beta`
  - `alpha`:
    - `elastic_constants`:
      - `C11`: number (GPa)
      - `C44`: number (GPa)
      - `C12`: number (GPa)
    - `derived_moduli`:
      - `B_VRH`: number (GPa)
      - `G_VRH`: number (GPa)
      - `E`: number (GPa)
      - `Poisson_ratio`: number (dimensionless)
      - `Vickers_hardness`: number (GPa)
  - `beta`:
    - `elastic_constants`:
      - `C11`: number (GPa)
      - `C33`: number (GPa)
      - `C44`: number (GPa)
      - `C12`: number (GPa)
      - `C13`: number (GPa)
    - `derived_moduli`:
      - `B_VRH`: number (GPa)
      - `G_VRH`: number (GPa)
      - `E`: number (GPa)
      - `Poisson_ratio`: number (dimensionless)
      - `Vickers_hardness`: number (GPa)

Notes: The agent must use the LDA exchange-correlation functional; results from GGA are not scored. The elastic constants must be given in GPa. The derived moduli are recomputed by the checker, so the agent's reported values serve as a cross-check.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "elastic_and_derived_moduli.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required_keys": [
          "alpha",
          "beta"
        ],
        "alpha": {
          "elastic_constants": {
            "C11": "number (GPa)",
            "C44": "number (GPa)",
            "C12": "number (GPa)"
          },
          "derived_moduli": {
            "B_VRH": "number (GPa)",
            "G_VRH": "number (GPa)",
            "E": "number (GPa)",
            "Poisson_ratio": "number (dimensionless)",
            "Vickers_hardness": "number (GPa)"
          }
        },
        "beta": {
          "elastic_constants": {
            "C11": "number (GPa)",
            "C33": "number (GPa)",
            "C44": "number (GPa)",
            "C12": "number (GPa)",
            "C13": "number (GPa)"
          },
          "derived_moduli": {
            "B_VRH": "number (GPa)",
            "G_VRH": "number (GPa)",
            "E": "number (GPa)",
            "Poisson_ratio": "number (dimensionless)",
            "Vickers_hardness": "number (GPa)"
          }
        }
      },
      "description": "Scored artifact containing the single-crystal elastic constants and the derived Voigt-Reuss-Hill polycrystalline moduli and Chen Vickers hardness for both α- and β-Be3N2. The checker recomputes B_VRH, G_VRH, E, Poisson_ratio, and Vickers_hardness from the provided elastic constants and scores against the paper's LDA reference values."
    }
  ],
  "notes": "The agent must use the LDA exchange-correlation functional; results from GGA are not scored. The elastic constants must be given in GPa. The derived moduli are recomputed by the checker, so the agent's reported values serve as a cross-check."
}
```

## How you are scored
A hidden verifier reads your submitted JSON, recomputes the derived quantities (B_VRH, G_VRH, E, ν, H_V) from the elastic constants you provide, and compares the recomputed values against hidden reference values derived from the original paper's LDA results. Each of the ten quantities (five per phase) that falls within an undisclosed tolerance earns a fraction of the total reward. Reporting paper numbers without performing the actual DFT calculations is not sufficient; the verifier independently recomputes from the raw elastic constants. The total reward is the sum of per-quantity scores, normalized to [0,1].

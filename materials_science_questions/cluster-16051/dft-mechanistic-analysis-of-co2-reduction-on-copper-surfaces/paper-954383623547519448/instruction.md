# DFT Mechanistic Analysis of CO2 Reduction on Copper Surfaces

## Problem background
Electrochemical CO2 reduction to CO is a promising route for sustainable production of chemicals and fuels, but cost-effective, earth-abundant catalysts that operate with high CO selectivity are still being sought. Recent experiments have shown that sulfide-derived Cu-Sb alloys can achieve high faradaic efficiency for CO production, in contrast to the typical behaviour of sulfide-derived catalysts that favour formate. Understanding the atomistic origin of this selectivity is critical for designing improved catalysts. Density functional theory (DFT) calculations can probe how the presence of remnant sulfur atoms on Cu2Sb surfaces alters the energetics of key reaction intermediates, thereby switching the product distribution. This task focuses on computing the thermodynamic selectivity descriptor at an applied potential of -1.0 V vs RHE for several realistic Cu2Sb(100)-based surface motifs that are expected to be stable under operating conditions.

## Approach
The computational method employs plane-wave DFT within the atomic simulation environment (ASE) and Quantum ESPRESSO, using the PBE exchange-correlation functional with Grimme's D3 dispersion correction and ultrasoft pseudopotentials. The active phase is tetragonal Cu2Sb, whose (100) facet is the lowest-energy surface. To capture the effect of sulfur incorporation, several surface models are built: the pristine Cu2Sb(100) slab, models with a sulfur atom substituting surface Sb (S_Sb1, S_Sb2) or other sites, and a surface with a Cu2 vacancy (V_Cu2). The workflow proceeds by first optimizing bulk Cu and Cu2Sb, then constructing slab models, screening for thermodynamic stability at -1.0 V vs RHE, computing adsorption energies of the key intermediates (*H, *COOH, HCOO*, *CO) on stable motifs, and finally evaluating the Gibbs free energy changes for the CO formation pathway (ΔR1G), the formate pathway (ΔR2G), and the hydrogen evolution reaction (ΔR3G). Thermodynamic corrections and gas-phase references (H2, CO2, CO, HCOOH) are used to convert DFT energies to free energies at 298 K. The selectivity descriptor ΔR1G - ΔR2G is then obtained for each motif. The binding strength of *CO is benchmarked against Cu(111), where weaker *CO adsorption than Cu(111) favours 2e- products.

## Reproduction target
Compute the Gibbs free energy changes at -1.0 V vs RHE for the four operationally stable surface motifs: pristine Cu2Sb(100), S_Sb1/Cu2Sb(100), S_Sb2/Cu2Sb(100), and V_Cu2/Cu2Sb(100). For each motif, calculate ΔR1G (CO2 → *COOH), ΔR2G (CO2 → HCOO*), and ΔR3G (H+ + e- → H*) using the standard free energy of H+ + e- as 0 eV at -1.0 V, and write the results to the JSON file `/app/outputs/dft_selectivity_result.json`. The file must contain an array of objects, each with keys `motif`, `delta_R1G_eV`, `delta_R2G_eV`, `delta_R3G_eV` (values in eV). The hidden verifier will compare the reported values against the paper's computed reference values with an appropriate tolerance and will also evaluate the derived selectivity descriptor ΔR1G - ΔR2G to determine whether each motif is thermodynamically selective toward CO.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- ASE (Atomic Simulation Environment): ase
- Vanderbilt ultrasoft pseudopotentials (SSSP): https://www.quantum-espresso.org/pseudopotentials/
- Cu2Sb crystal structure: https://materialsproject.org/materials/mp-8661/
- FCC Cu crystal structure

## Workflow steps

### Step 1: Bulk relaxation of Cu and Cu2Sb
- Role: process
- Action: Perform DFT relaxation of bulk Cu and Cu2Sb unit cells to obtain optimized lattice parameters and total energies, using Quantum ESPRESSO with PBE+D3 and ultrasoft pseudopotentials.
- Evidence: `/app/outputs/bulk_relaxation.log`

### Step 2: Surface energy of Cu2Sb facets
- Role: process
- Action: Build asymmetric slab models for Cu2Sb (100), (101), (110), and (001) surfaces from the relaxed bulk and compute their total energies. Calculate surface energies to confirm that (100) is the most stable facet.
- Evidence: `/app/outputs/surface_energy.txt`

### Step 3: Construct sulfur-decorated and vacancy surface models
- Role: process
- Action: Create ASE structure files for the nine active-site motifs on Cu2Sb(100) described in the paper: pristine surface, S adatom at Cu3 site, substitutional S at Cu1, Cu2, Sb1, Sb2 in the topmost layer, S at Sb in the subsurface layer, Cu1 vacancy, Cu2 vacancy, and Sb1 vacancy.
- Evidence: none

### Step 4: First stability screening at -1.0 V vs RHE
- Role: process
- Action: For each of the nine motifs, compute the formation energy under an applied potential of -1.0 V vs RHE using ab initio thermodynamics. Discard the motif S_Cu3@Cu2Sb(100) as unstable; retain the other eight motifs.
- Evidence: `/app/outputs/stability_screening.txt`

### Step 5: Adsorption energy calculations on stable motifs
- Role: process
- Action: Compute adsorption energies of *H, *COOH, HCOO*, and *CO on the eight stable motifs, on clean Cu2Sb(100), and on Cu(111) as reference. Use gas-phase references H2, CO2, CO, HCOOH and apply vibrational/thermodynamic corrections to obtain Gibbs free energies at 298 K. Filter to motifs that bind *CO more weakly than Cu(111).
- Evidence: `/app/outputs/adsorption_energies.txt`

### Step 6: Second stability analysis to select operationally stable motifs
- Role: process
- Action: From the CO-pathway candidates, apply a second stability screening under -1.0 V vs RHE to identify motifs that remain stable throughout electrochemical operation. Select the four motifs: pristine Cu2Sb(100), S_Sb1/Cu2Sb(100), S_Sb2/Cu2Sb(100), and V_Cu2/Cu2Sb(100).
- Evidence: `/app/outputs/stable_motifs.txt`

### Step 7: CO2RR selectivity descriptor calculation
- Role: scored (load-bearing)
- Action: For the four operationally stable motifs, compute the Gibbs free energy changes at -1.0 V vs RHE: ΔR1G = G(*COOH) - G(CO2(g)) - G(H+ + e-), ΔR2G = G(HCOO*) - G(CO2(g)) - G(H+ + e-), and ΔR3G = G(H*) - G(H+ + e-). Use the standard free energy of H+ + e- as 0 eV at -1.0 V. Save the result as a JSON file.
- Output file: `/app/outputs/dft_selectivity_result.json`
- Format: json
- Contract: {"type":"array","items":{"type":"object","properties":{"motif":{"type":"string"},"delta_R1G_eV":{"type":"number"},"delta_R2G_eV":{"type":"number"},"delta_R3G_eV":{"type":"number"}}}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dft_selectivity_result.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dft_selectivity_result.json
- path: `/app/outputs/dft_selectivity_result.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed Gibbs free energy changes at -1.0 V vs RHE for the four operationally stable Cu2Sb(100)-based surface motifs: pristine Cu2Sb(100), S_Sb1/Cu2Sb(100), S_Sb2/Cu2Sb(100), and V_Cu2/Cu2Sb(100). The checker compares these values to hidden paper-reported references with a tolerance.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `properties`:
      - `motif`:
        - `type`: string
      - `delta_R1G_eV`:
        - `type`: number
      - `delta_R2G_eV`:
        - `type`: number
      - `delta_R3G_eV`:
        - `type`: number

Notes: The scored artifact contains the selectivity descriptors ΔR1G, ΔR2G, and ΔR3G for the four stable motifs. The hidden checker performs a result-level comparison against the paper's Table 1 values with an appropriate tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dft_selectivity_result.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "motif": {
              "type": "string"
            },
            "delta_R1G_eV": {
              "type": "number"
            },
            "delta_R2G_eV": {
              "type": "number"
            },
            "delta_R3G_eV": {
              "type": "number"
            }
          }
        }
      },
      "description": "Computed Gibbs free energy changes at -1.0 V vs RHE for the four operationally stable Cu2Sb(100)-based surface motifs: pristine Cu2Sb(100), S_Sb1/Cu2Sb(100), S_Sb2/Cu2Sb(100), and V_Cu2/Cu2Sb(100). The checker compares these values to hidden paper-reported references with a tolerance."
    }
  ],
  "notes": "The scored artifact contains the selectivity descriptors ΔR1G, ΔR2G, and ΔR3G for the four stable motifs. The hidden checker performs a result-level comparison against the paper's Table 1 values with an appropriate tolerance."
}
```

## How you are scored
A hidden verifier independently scores the artifacts you submit. The primary scored output is `dft_selectivity_result.json`. The verifier first checks that the file exists and conforms to the required schema. It then compares your reported ΔR1G, ΔR2G, and ΔR3G values for each of the four motifs against the paper's reference values (hidden gold) using a tolerance. Values within tolerance contribute positively to the reward; values outside tolerance reduce it. In addition, the verifier computes ΔR1G - ΔR2G for each motif and applies a thermodynamical criterion to assess CO selectivity. Meeting both the value tolerance and the selectivity criterion yields the maximum score. The earlier process steps (Steps 1–6) are required to produce the final scored result; they are not directly scored, but if they are not executed correctly the scored output will be inaccurate or missing, leading to a low or zero reward for the scored step.

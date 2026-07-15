# ZrMn2 Hydride Chemical Bonding Analysis

## Problem background
ZrMn2 is a Laves phase intermetallic compound that absorbs hydrogen reversibly, making it a candidate for hydrogen storage applications. The stability of the resulting hydride—and hence the practical absorption/desorption performance—can be tuned by substituting alloying elements for Mn. However, the way in which different alloying elements modify the electronic structure and the chemical bonding between metal and hydrogen atoms is not fully understood at a first‑principles level. This task investigates those bonding changes by computing the strength of the interactions (bond orders) between atoms in a cluster model of the hydride. The central quantity to compute is the per‑atom‑pair bond order for both metal–hydrogen and metal–metal pairs, and to examine how these bond orders vary when Mn is replaced by V, Fe, Co, or Ni. In particular, the task asks whether a simple ratio of metal‑metal bond orders can serve as a descriptor for the experimentally observed changes in the equilibrium hydrogen pressure of the alloyed compounds.

## Approach
The approach is based on a first‑principles description of the electronic structure using density functional theory and population analysis. A tetrahedral cluster model, Zr4Mn8M2H2 (M = Mn, V, Fe, Co, Ni), is built from the published crystal structure of the hydride. The hydrogen atoms occupy the centres of tetrahedral interstices defined by two Zr and two Mn (or M) atoms. For each alloy composition, a single‑point DFT calculation is performed on this cluster with a suitable exchange‑correlation functional and basis set. Mulliken or Löwdin population analysis is then used to extract the overlap populations (bond orders) for every atom pair of interest: Mn(4)–H, M–H, Zr(1)–H, total metal–hydrogen bond order, and the metal–metal pairs Mn(1)–Mn(4), Mn(1)–M, M–Mn(4), Zr(1)–Mn(4), and Zr(1)–M. The same computational protocol is applied to the pure (M = Mn) cluster and to the four alloyed clusters. From these bond orders, a dimensionless ratio, (Bo(Zr1-Mn4) + Bo(Zr1-M)) / Bo(M-Mn4), is computed for each system. The results are then analysed to see (i) whether the Mn–H bond order is larger than the Zr–H bond order in the pure hydride, (ii) whether the total metal–hydrogen bond order remains nearly constant across the alloy series, and (iii) whether the calculated ratio trends monotonically from V to Ni in a way that mirrors the published equilibrium hydrogen pressures of the corresponding bulk alloys.

## Reproduction target
The target is to produce three output files that encode the computed bond orders and the trend analysis:

* **pure_bond_orders.json**: For the pure ZrMn2H3 cluster, extract the per‑bond bond orders for Mn(4)–H, M–H, Zr(1)–H, total M–H, and the key metal–metal pairs, as well as the ratio defined above.
* **alloy_bond_orders.json**: For each alloying element (V, Fe, Co, Ni), extract the same set of bond orders and the ratio, and store them under the element key.
* **trend_report.txt**: Summarise the computed bond-order ratios for the V, Fe, Co, and Ni alloyed clusters, list the relevant bond-order values from the pure hydride, and discuss any observable trends or correlations (e.g., relative strengths of metal–hydrogen bonds, variation of the total metal–hydrogen bond order, ordering of the ratio values). Include all numerical values.

## Assets

- CP2K: https://www.cp2k.org/

## Workflow steps

### Step 1: Construct cluster geometries
- Role: process
- Action: Using published lattice parameters (a=0.5391 nm, c=0.8748 nm for ZrMn2H3; a=0.5035 nm, c=0.8276 nm for ZrMn2) and hydrogen site occupancy (12k site), build tetrahedral cluster models Zr4Mn8M2H2 for M=Mn, V, Fe, Co, Ni. Generate XYZ coordinate files for each cluster, where the two M atoms replace Mn atoms D and D' as described in the cluster model.
- Evidence: `/app/outputs/cluster_coordinates.json`

### Step 2: DFT calculation for pure ZrMn2 hydride
- Role: process
- Action: Run a single-point DFT calculation on the pure ZrMn2H3 cluster (M=Mn) using CP2K or an equivalent code with a suitable exchange-correlation functional and basis set, performing Mulliken or Löwdin population analysis. Save the full output log.
- Evidence: `/app/outputs/pure_dft.log`

### Step 3: DFT calculations for alloyed clusters
- Role: process
- Action: Repeat the DFT calculation and population analysis for each alloyed cluster (M=V, Fe, Co, Ni) using the same computational settings.
- Evidence: `/app/outputs/alloy_dft.log`

### Step 4: Extract bond orders for pure hydride
- Role: scored (load-bearing)
- Action: From the population output of the pure cluster calculation, compute per-bond bond orders for Mn(4)-H, M-H (M=Mn), Zr(1)-H, total metal-hydrogen bond order, and key metal-metal pairs. Also compute the ratio (Bo(Zr1-Mn4)+Bo(Zr1-M))/Bo(M-Mn4). Write results to pure_bond_orders.json.
- Output file: `/app/outputs/pure_bond_orders.json`
- Format: json
- Contract: {"Mn4_H": float, "M_H": float, "Zr1_H": float, "total_M_H": float, "Mn1_Mn4": float, "Mn1_M": float, "M_Mn4": float, "Zr1_Mn4": float, "Zr1_M": float, "ratio": float}
- Scoring: scored by hidden verifier

### Step 5: Extract bond orders for alloyed compounds
- Role: scored (load-bearing)
- Action: For each alloy (V, Fe, Co, Ni), compute the same set of bond orders and the ratio from the population outputs, and write to alloy_bond_orders.json with keys for each element.
- Output file: `/app/outputs/alloy_bond_orders.json`
- Format: json
- Contract: {"V": {"Mn4_H": float, "M_H": float, "Zr1_H": float, "total_M_H": float, "Mn1_Mn4": float, "Mn1_M": float, "M_Mn4": float, "Zr1_Mn4": float, "Zr1_M": float, "ratio": float}, "Fe": {...}, "Co": {...}, "Ni": {...}}
- Scoring: scored by hidden verifier

### Step 6: Trend report
- Role: scored
- Action: Using the extracted bond orders from Steps 4 and 5, compile the computed ratios for V, Fe, Co, Ni. Compare the Mn–H and Zr–H bond strengths in the pure hydride, inspect the variation of the total metal–hydrogen bond order across the alloys, and note any pattern in the sequence of ratios. Write a brief plain-text report listing all relevant numerical values and your observations.
- Output file: `/app/outputs/trend_report.txt`
- Format: txt
- Contract: Text document containing the bond‑order ratios for V, Fe, Co, Ni, the pure total metal‑hydrogen bond order, and a discussion of any observable trends.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/pure_bond_orders.json`
- `/app/outputs/alloy_bond_orders.json`
- `/app/outputs/trend_report.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### pure_bond_orders.json
- path: `/app/outputs/pure_bond_orders.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Per-atom-pair bond orders (overlap populations) and the derived ratio for pure ZrMn2H3 cluster.
- schema:
  - `type`: object
  - `required`:
    - `Mn4_H`: float
    - `M_H`: float
    - `Zr1_H`: float
    - `total_M_H`: float
    - `Mn1_Mn4`: float
    - `Mn1_M`: float
    - `M_Mn4`: float
    - `Zr1_Mn4`: float
    - `Zr1_M`: float
    - `ratio`: float

### alloy_bond_orders.json
- path: `/app/outputs/alloy_bond_orders.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Per-atom-pair bond orders and ratio for each alloyed cluster (V, Fe, Co, Ni).
- schema:
  - `type`: object
  - `required`:
    - `V`:
      - `type`: object
      - `required`:
        - `Mn4_H`: float
        - `M_H`: float
        - `Zr1_H`: float
        - `total_M_H`: float
        - `Mn1_Mn4`: float
        - `Mn1_M`: float
        - `M_Mn4`: float
        - `Zr1_Mn4`: float
        - `Zr1_M`: float
        - `ratio`: float
    - `Fe`:
      - `type`: object
      - `required`:
        - `Mn4_H`: float
        - `M_H`: float
        - `Zr1_H`: float
        - `total_M_H`: float
        - `Mn1_Mn4`: float
        - `Mn1_M`: float
        - `M_Mn4`: float
        - `Zr1_Mn4`: float
        - `Zr1_M`: float
        - `ratio`: float
    - `Co`:
      - `type`: object
      - `required`:
        - `Mn4_H`: float
        - `M_H`: float
        - `Zr1_H`: float
        - `total_M_H`: float
        - `Mn1_Mn4`: float
        - `Mn1_M`: float
        - `M_Mn4`: float
        - `Zr1_Mn4`: float
        - `Zr1_M`: float
        - `ratio`: float
    - `Ni`:
      - `type`: object
      - `required`:
        - `Mn4_H`: float
        - `M_H`: float
        - `Zr1_H`: float
        - `total_M_H`: float
        - `Mn1_Mn4`: float
        - `Mn1_M`: float
        - `M_Mn4`: float
        - `Zr1_Mn4`: float
        - `Zr1_M`: float
        - `ratio`: float

### trend_report.txt
- path: `/app/outputs/trend_report.txt`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Text summary of the bond-order ratios and any observable trends across the alloyed clusters.
- schema:
  - `type`: text
  - `description`: Must contain the computed bond-order ratios for V, Fe, Co, Ni and a discussion of any trends observed.

Notes: Hidden gold bond orders are taken from the paper's DV-Xα results with tolerances accounting for methodological differences. The trend report is scored on structural correctness: consistency of listed ratios with JSON outputs and presence of a trend discussion (without requiring any specific conclusion).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "pure_bond_orders.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "Mn4_H": "float",
          "M_H": "float",
          "Zr1_H": "float",
          "total_M_H": "float",
          "Mn1_Mn4": "float",
          "Mn1_M": "float",
          "M_Mn4": "float",
          "Zr1_Mn4": "float",
          "Zr1_M": "float",
          "ratio": "float"
        }
      },
      "description": "Per-atom-pair bond orders (overlap populations) and the derived ratio for pure ZrMn2H3 cluster."
    },
    {
      "file": "alloy_bond_orders.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "V": {
            "type": "object",
            "required": {
              "Mn4_H": "float",
              "M_H": "float",
              "Zr1_H": "float",
              "total_M_H": "float",
              "Mn1_Mn4": "float",
              "Mn1_M": "float",
              "M_Mn4": "float",
              "Zr1_Mn4": "float",
              "Zr1_M": "float",
              "ratio": "float"
            }
          },
          "Fe": {
            "type": "object",
            "required": {
              "Mn4_H": "float",
              "M_H": "float",
              "Zr1_H": "float",
              "total_M_H": "float",
              "Mn1_Mn4": "float",
              "Mn1_M": "float",
              "M_Mn4": "float",
              "Zr1_Mn4": "float",
              "Zr1_M": "float",
              "ratio": "float"
            }
          },
          "Co": {
            "type": "object",
            "required": {
              "Mn4_H": "float",
              "M_H": "float",
              "Zr1_H": "float",
              "total_M_H": "float",
              "Mn1_Mn4": "float",
              "Mn1_M": "float",
              "M_Mn4": "float",
              "Zr1_Mn4": "float",
              "Zr1_M": "float",
              "ratio": "float"
            }
          },
          "Ni": {
            "type": "object",
            "required": {
              "Mn4_H": "float",
              "M_H": "float",
              "Zr1_H": "float",
              "total_M_H": "float",
              "Mn1_Mn4": "float",
              "Mn1_M": "float",
              "M_Mn4": "float",
              "Zr1_Mn4": "float",
              "Zr1_M": "float",
              "ratio": "float"
            }
          }
        }
      },
      "description": "Per-atom-pair bond orders and ratio for each alloyed cluster (V, Fe, Co, Ni)."
    },
    {
      "file": "trend_report.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "description": "Must contain the computed bond-order ratios for V, Fe, Co, Ni and a discussion of any trends observed."
      },
      "description": "Text summary of the bond-order ratios and any observable trends across the alloyed clusters."
    }
  ],
  "notes": "Hidden gold bond orders are taken from the paper's DV-Xα results with tolerances accounting for methodological differences. The trend report is scored on structural correctness: consistency of listed ratios with JSON outputs and presence of a trend discussion (without requiring any specific conclusion)."
}
```

## How you are scored
A hidden verifier will independently score each of the three output files. For the JSON bond‑order files, the verifier compares your extracted bond orders to reference values derived from the paper’s DV‑Xα results, using tolerances that account for systematic differences between the DV‑Xα method and standard DFT with Mulliken/Löwdin analysis. For the trend_report.txt, the verifier performs a structural audit: it checks that the listed ratios are consistent with the JSON outputs and that the report discusses the observed trends (such as relative bond strengths and the pattern of ratio values) without requiring any specific predetermined conclusion. The final reward is a weighted combination of the scores for the three artifacts. Simply reporting the paper’s numbers without performing the computations will not yield a passing score.

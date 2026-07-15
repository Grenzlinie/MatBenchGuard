# DFT Study of Sulfur Gas Adsorption on Hexagonal Yttrium Nitride Monolayer

## Problem background
Hexagonal yttrium nitride (h‑YN) monolayer is a predicted 2D semiconductor with high carrier mobility and a large surface‑to‑volume ratio, making it a potential candidate for gas capture and sensing applications. Sulfur‑containing gases such as hydrogen sulfide (H₂S) and sulfur dioxide (SO₂) are toxic pollutants emitted from industrial processes and natural sources. It is therefore important to quantify how these gases interact with pristine h‑YN and with h‑YN surfaces pre‑covered by environmental oxygen (O₂) to assess its possible performance as a scavenging material. This task computes the key physical quantities (adsorption energies, band gaps, work functions) that characterize these interactions, using first‑principles density functional theory.

## Approach
The reproduction employs a planewave density functional theory (DFT) approach within the generalized gradient approximation (GGA) of Perdew–Burke–Ernzerhof (PBE), augmented by a van der Waals (vdW) dispersion correction to capture long‑range interactions. The study compares six model systems: pristine h‑YN, H₂S adsorbed on pristine h‑YN, SO₂ adsorbed on pristine h‑YN, O₂ adsorbed on pristine h‑YN (yielding an O₂‑h‑YN surface), H₂S adsorbed on O₂‑h‑YN, and SO₂ adsorbed on O₂‑h‑YN. For each system, geometry optimizations are performed to locate the lowest‑energy configuration, and electronic properties — indirect band gap and work function — are extracted. Adsorption energies are computed from total energy differences according to E_ads = E_total(system) – E_total(substrate) – E_total(molecule). The complete workflow, including the required intermediate steps and the final scored artifact, is specified in the workflow steps below; no external dataset is needed, only the crystal structure of h‑YN and standard pseudopotentials.

## Reproduction target
Produce a single JSON file, computed_results.json, containing the following quantities for all six systems (all values in eV):

- Band gaps: pristine_hYN_bandgap, H2S_bandgap, SO2_bandgap, O2_hYN_bandgap, H2S_O2_hYN_bandgap, SO2_O2_hYN_bandgap
- Adsorption energies: H2S_ads_E, SO2_ads_E, O2_ads_E, H2S_O2_hYN_ads_E, SO2_O2_hYN_ads_E
- Work functions: an object work_functions with keys pristine_hYN, H2S_hYN, SO2_hYN, O2_hYN, H2S_O2_hYN, SO2_O2_hYN

The output must conform to the JSON schema defined in the output contract. The computed values must be self‑consistent and obtained from the DFT workflow specified in the steps; they will be evaluated by a hidden verifier against a private reference.

## Assets

- Quantum ESPRESSO (or equivalent open-source planewave DFT code): https://www.quantum-espresso.org/
- SSSP pseudopotential library: https://www.materialscloud.org/discover/sssp/table/precision
- Atomic Simulation Environment (ASE): https://wiki.fysik.dtu.dk/ase/

## Workflow steps

### Step 1: Relax pristine h-YN monolayer
- Role: process
- Action: Build a 5×5×1 supercell of h-YN with a 20 Å vacuum layer and relax the geometry using DFT with van der Waals correction. Save the relaxed structure and total energy.
- Evidence: `/app/outputs/pristine_hYN_relaxed.out`

### Step 2: Compute isolated molecule energies
- Role: process
- Action: Compute total energies of isolated H₂S, SO₂, and O₂ molecules in large cells using the same DFT settings. Save the energies.
- Evidence: `/app/outputs/isolated_energies.json`

### Step 3: Optimize H₂S on pristine h-YN
- Role: process
- Action: Place H₂S at multiple adsorption sites (Y-top, N-top, bridge, hollow) with various orientations on the relaxed h-YN slab, optimize each, and select the lowest-energy configuration. Save the final geometry and total energy.
- Evidence: `/app/outputs/H2S_hYN_optimized.out`

### Step 4: Optimize SO₂ on pristine h-YN
- Role: process
- Action: Analogous to step 3 for SO₂. Sample sites/orientations, optimize, and save the lowest-energy geometry and total energy.
- Evidence: `/app/outputs/SO2_hYN_optimized.out`

### Step 5: Optimize O₂ on pristine h-YN
- Role: process
- Action: Place O₂ in parallel and perpendicular configurations on different sites, optimize, and select the lowest-energy dissociative configuration. Save the relaxed O₂-h-YN structure and total energy.
- Evidence: `/app/outputs/O2_hYN_optimized.out`

### Step 6: Optimize H₂S on O₂-precovered h-YN
- Role: process
- Action: Using the optimized O₂-h-YN from step 5, try multiple H₂S sites/orientations, optimize, and select the lowest-energy configuration. Save the final geometry and total energy.
- Evidence: `/app/outputs/H2S_O2_hYN_optimized.out`

### Step 7: Optimize SO₂ on O₂-precovered h-YN
- Role: process
- Action: Analogous to step 6 for SO₂. Optimize and save the lowest-energy geometry and total energy.
- Evidence: `/app/outputs/SO2_O2_hYN_optimized.out`

### Step 8: Compute target quantities and output results
- Role: scored (load-bearing)
- Action: Using the total energies from steps 1-7, compute adsorption energies as E_ads = E_total(system) − E_total(substrate) − E_total(molecule). Compute band structures for the six systems (pristine, H₂S@h-YN, SO₂@h-YN, O₂-h-YN, H₂S@O₂-h-YN, SO₂@O₂-h-YN) to obtain indirect band gaps. Compute work functions (Φ = V_inf − E_f) for those six systems. Write all values to computed_results.json.
- Output file: `/app/outputs/computed_results.json`
- Format: json
- Contract: JSON object with numeric keys (all in eV): pristine_hYN_bandgap, H2S_ads_E, H2S_bandgap, SO2_ads_E, SO2_bandgap, O2_ads_E, O2_hYN_bandgap, H2S_O2_hYN_ads_E, H2S_O2_hYN_bandgap, SO2_O2_hYN_ads_E, SO2_O2_hYN_bandgap, and work_functions: { pristine_hYN, H2S_hYN, SO2_hYN, O2_hYN, H2S_O2_hYN, SO2_O2_hYN } (each a number in eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_results.json
- path: `/app/outputs/computed_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: All computed adsorption energies, indirect band gaps, and work functions for the six systems under study.
- schema:
  - `type`: object
  - `required`: `pristine_hYN_bandgap`, `H2S_ads_E`, `H2S_bandgap`, `SO2_ads_E`, `SO2_bandgap`, `O2_ads_E`, `O2_hYN_bandgap`, `H2S_O2_hYN_ads_E`, `H2S_O2_hYN_bandgap`, `SO2_O2_hYN_ads_E`, `SO2_O2_hYN_bandgap`, `work_functions`
  - `properties`:
    - `pristine_hYN_bandgap`:
      - `type`: number
      - `units`: eV
    - `H2S_ads_E`:
      - `type`: number
      - `units`: eV
    - `H2S_bandgap`:
      - `type`: number
      - `units`: eV
    - `SO2_ads_E`:
      - `type`: number
      - `units`: eV
    - `SO2_bandgap`:
      - `type`: number
      - `units`: eV
    - `O2_ads_E`:
      - `type`: number
      - `units`: eV
    - `O2_hYN_bandgap`:
      - `type`: number
      - `units`: eV
    - `H2S_O2_hYN_ads_E`:
      - `type`: number
      - `units`: eV
    - `H2S_O2_hYN_bandgap`:
      - `type`: number
      - `units`: eV
    - `SO2_O2_hYN_ads_E`:
      - `type`: number
      - `units`: eV
    - `SO2_O2_hYN_bandgap`:
      - `type`: number
      - `units`: eV
    - `work_functions`:
      - `type`: object
      - `required`: `pristine_hYN`, `H2S_hYN`, `SO2_hYN`, `O2_hYN`, `H2S_O2_hYN`, `SO2_O2_hYN`
      - `properties`:
        - `pristine_hYN`:
          - `type`: number
          - `units`: eV
        - `H2S_hYN`:
          - `type`: number
          - `units`: eV
        - `SO2_hYN`:
          - `type`: number
          - `units`: eV
        - `O2_hYN`:
          - `type`: number
          - `units`: eV
        - `H2S_O2_hYN`:
          - `type`: number
          - `units`: eV
        - `SO2_O2_hYN`:
          - `type`: number
          - `units`: eV

Notes: The agent must provide one JSON file containing the computed quantities. The checker will compare each value to the paper-reported reference using appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "pristine_hYN_bandgap",
          "H2S_ads_E",
          "H2S_bandgap",
          "SO2_ads_E",
          "SO2_bandgap",
          "O2_ads_E",
          "O2_hYN_bandgap",
          "H2S_O2_hYN_ads_E",
          "H2S_O2_hYN_bandgap",
          "SO2_O2_hYN_ads_E",
          "SO2_O2_hYN_bandgap",
          "work_functions"
        ],
        "properties": {
          "pristine_hYN_bandgap": {
            "type": "number",
            "units": "eV"
          },
          "H2S_ads_E": {
            "type": "number",
            "units": "eV"
          },
          "H2S_bandgap": {
            "type": "number",
            "units": "eV"
          },
          "SO2_ads_E": {
            "type": "number",
            "units": "eV"
          },
          "SO2_bandgap": {
            "type": "number",
            "units": "eV"
          },
          "O2_ads_E": {
            "type": "number",
            "units": "eV"
          },
          "O2_hYN_bandgap": {
            "type": "number",
            "units": "eV"
          },
          "H2S_O2_hYN_ads_E": {
            "type": "number",
            "units": "eV"
          },
          "H2S_O2_hYN_bandgap": {
            "type": "number",
            "units": "eV"
          },
          "SO2_O2_hYN_ads_E": {
            "type": "number",
            "units": "eV"
          },
          "SO2_O2_hYN_bandgap": {
            "type": "number",
            "units": "eV"
          },
          "work_functions": {
            "type": "object",
            "required": [
              "pristine_hYN",
              "H2S_hYN",
              "SO2_hYN",
              "O2_hYN",
              "H2S_O2_hYN",
              "SO2_O2_hYN"
            ],
            "properties": {
              "pristine_hYN": {
                "type": "number",
                "units": "eV"
              },
              "H2S_hYN": {
                "type": "number",
                "units": "eV"
              },
              "SO2_hYN": {
                "type": "number",
                "units": "eV"
              },
              "O2_hYN": {
                "type": "number",
                "units": "eV"
              },
              "H2S_O2_hYN": {
                "type": "number",
                "units": "eV"
              },
              "SO2_O2_hYN": {
                "type": "number",
                "units": "eV"
              }
            }
          }
        }
      },
      "description": "All computed adsorption energies, indirect band gaps, and work functions for the six systems under study."
    }
  ],
  "notes": "The agent must provide one JSON file containing the computed quantities. The checker will compare each value to the paper-reported reference using appropriate tolerances."
}
```

## How you are scored
A hidden verifier independently inspects the artifacts written under /app/outputs for each workflow stage. For the load‑bearing computed_results.json, the verifier compares each numeric entry to a private reference, using tolerances that account for method‑dependent spread and checks directional trends (e.g., relative increases or decreases between named conditions). Partial credit is awarded based on the accuracy of each quantity, weighted so that the main computed targets carry the largest share; the total reward is a float between 0 and 1. Reporting values without executing the required computations cannot earn the full reward.

# DFT-calculated Limiting Potential for NRR on Fluorinated Iron/Graphene Catalysts

## Problem background
Electrochemical nitrogen reduction (NRR) is a promising route for sustainable ammonia production under ambient conditions. A major challenge is the inert N≡N bond, which requires efficient catalysts to lower the overpotential. Supported iron nanoparticles have emerged as active NRR catalysts, and their electronic properties can be tuned by fluorination of both the metal cluster and the graphene support. First-principles density functional theory (DFT) calculations can quantify the thermodynamic driving force of the reaction through the limiting potential UL, a descriptor directly linked to the overpotential. This task investigates how fluorination affects the NRR limiting potential across a series of six catalyst models: a free-standing Fe65 cluster (Fe), fluorinated Fe65 (F-Fe), Fe65 supported on pristine graphene (Fe@G), Fe65 supported on fluorinated graphene (Fe@F-G), fluorinated Fe65 on pristine graphene (F-Fe@G), and fluorinated Fe65 on fluorinated graphene (F-Fe@F-G). The objective is to compute UL for each system using an open-source DFT code and the computational hydrogen electrode (CHE) model.

## Approach
The computational workflow follows a standard first-principles thermodynamics approach. First, construct atomic models of the six catalysts (Fe65 cluster with/without F decoration, placed on or off an 8×8 graphene supercell with/without fluorine on both sides). Then perform DFT geometry optimizations to obtain the relaxed structures and total energies of the clean catalysts using a GGA-PBE functional with a dispersion correction. Subsequently, adsorb the NRR intermediates (N2*, NNH*, NH*, NH2*, NH3*, etc.) and H* on each catalyst, and compute the total energies of every adsorbate–catalyst combination together with gas-phase N2 and H2 reference energies. Using the CHE model, convert the DFT total energies of each elementary proton–electron transfer step into Gibbs free-energy changes ΔG by adding zero-point energy and entropy corrections obtained from standard thermochemical tables. For each catalyst, identify the largest ΔG among the six NRR steps, ΔGmax, and compute the limiting potential UL = –ΔGmax / e. All calculations should be performed with an open-source DFT code (e.g., Quantum ESPRESSO) using a plane-wave basis set.

## Reproduction target
Produce a CSV file at `/app/outputs/limiting_potentials.csv` containing the computed limiting potential UL (in V) and the corresponding maximum free-energy step ΔGmax (in eV) for each of the six catalyst systems: Fe, F-Fe, Fe@G, Fe@F-G, F-Fe@G, F-Fe@F-G. The columns must be `System`, `UL_V`, and `ΔGmax_eV`. The UL values should reflect the computational prediction of the catalytic activity of each system. Additionally, the relative ordering of UL across the six systems should be consistent with the mechanistic effect of fluorination on the electronic structure.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- NIST-JANAF thermochemical tables: https://kinetics.nist.gov/janaf/
- Standard solid-state pseudopotentials (SSSP): https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: Build atomic structures for all catalyst models
- Role: process
- Action: Construct atomic models for six catalyst systems: Fe65 cluster, F-Fe65 cluster, Fe65 on 8×8 graphene, Fe65 on fluorinated 8×8 graphene, F-Fe65 on graphene, and F-Fe65 on fluorinated graphene. For fluorinated graphene, distribute F atoms on both sides. Also prepare the free N2 molecule.
- Evidence: none

### Step 2: DFT geometry optimization of clean catalysts
- Role: process
- Action: Perform DFT geometry optimization with an open-source code (e.g., Quantum ESPRESSO) for each clean catalyst model. Use a functional such as PBE with dispersion correction (e.g., DFT‑D3) and a plane‑wave cutoff of 500 eV. Converge ionic positions until forces are below 0.02 eV/Å. Store the relaxed structures and total energies.
- Evidence: none

### Step 3: DFT calculations of adsorbed species and NRR intermediates
- Role: process
- Action: Place N2, H*, and the elementary intermediates of the NRR pathway (N2*, NNH*, NH*, NH2*, NH3*, etc.) on each catalyst. Run DFT relaxations or static calculations to obtain total energies for every adsorbate‑catalyst combination, plus the gas‑phase N2 and H2 reference energies.
- Evidence: none

### Step 4: Compute limiting potentials UL
- Role: scored (load-bearing)
- Action: Using the CHE model and NIST-JANAF thermochemical data, convert DFT total energies of reaction steps into Gibbs free‑energy changes ΔG. For each catalyst, identify the largest free‑energy change among the elementary proton–electron transfer steps, ΔGmax, and compute the limiting potential UL = –ΔGmax/e. Output a table with columns System, UL_V, ΔGmax_eV.
- Output file: `/app/outputs/limiting_potentials.csv`
- Format: csv
- Contract: columns: System (string), UL_V (float), ΔGmax_eV (float). One row per system (Fe, F‑Fe, Fe@G, Fe@F‑G, F‑Fe@G, F‑Fe@F‑G).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/limiting_potentials.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### limiting_potentials.csv
- path: `/app/outputs/limiting_potentials.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Computed limiting potentials (UL) and the largest free‑energy step (ΔGmax) for NRR on six catalyst models; the checker recomputes agreement with reference values and the required ordering (F‑Fe@F‑G must show the highest UL).
- schema:
  - `type`: table
  - `required_columns`: `System`, `UL_V`, `ΔGmax_eV`
  - `units`:
    - `System`: string
    - `UL_V`: V
    - `ΔGmax_eV`: eV

Notes: Binding energies, N₂ adsorption energies, and H* adsorption energies are computed as intermediates inside the process steps but are not scored separately.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "limiting_potentials.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "System",
          "UL_V",
          "ΔGmax_eV"
        ],
        "units": {
          "System": "string",
          "UL_V": "V",
          "ΔGmax_eV": "eV"
        }
      },
      "description": "Computed limiting potentials (UL) and the largest free‑energy step (ΔGmax) for NRR on six catalyst models; the checker recomputes agreement with reference values and the required ordering (F‑Fe@F‑G must show the highest UL)."
    }
  ],
  "notes": "Binding energies, N₂ adsorption energies, and H* adsorption energies are computed as intermediates inside the process steps but are not scored separately."
}
```

## How you are scored
A hidden verifier will read your `limiting_potentials.csv` and score it against a reference. It compares each UL value to a hidden reference value, accepting deviations within a tolerance appropriate for DFT re‑implementations. It also checks that the relative ordering of UL across the six systems (i.e., which system has the most favourable, least‑negative limiting potential) matches the reference trend. The final reward is a weighted combination of the individual‑value agreement and the correctness of the trend, rewarding accurate reproduction of both the quantitative values and the qualitative ordering.

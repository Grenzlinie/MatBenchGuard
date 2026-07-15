# DFT Adsorption and Reaction Barrier on Ag/WC(0001) Catalyst

## Problem background
Efficient low-temperature CO oxidation catalysts are needed for fuel cells and environmental remediation. Silver is inexpensive, but pure Ag(111) binds CO and O₂ too weakly to sustain catalytic activity. Supporting a silver monolayer on a tungsten carbide (WC) substrate can modify the electronic properties of the adlayer and potentially improve the binding of key adsorbates. This computational study evaluates the adsorption properties of CO, O₂, O, and CO₂ on a Ag monolayer supported on the W-terminated WC(0001) surface (Ag_ML/WC(0001)) and determines the rate-limiting energy barrier for the CO+O→CO₂ step. The quantitative objective is to compute the adsorption energies, relevant bond lengths, and the reaction barrier using first-principles density functional theory.

## Approach
Use an open-source density functional theory (DFT) code (Quantum ESPRESSO) with the PW91 generalized-gradient approximation (GGA) functional and appropriate pseudopotentials. Construct the WC(0001) surface model: a 3×3 supercell with three WC bilayers, a vacuum region of 15 Å along the surface normal, and an Ag monolayer placed at the hcp hollow sites. The bottom four atomic layers are frozen during all relaxations; the top layers and the adsorbates are fully relaxed.
Optimize the bulk α-WC lattice parameters first, then relax the clean Ag_ML/WC(0001) slab to obtain the substrate total energy.
For each adsorbate (CO, O₂, O, CO₂), optimize its geometry at the site indicated in the workflow steps, compute the isolated molecule's ground‑state total energy in a separate calculation, and then compute the adsorption energy as Eads = E_adsorbate + E_substrate − E_adsorbate/substrate.
To obtain the CO+O→CO₂ reaction barrier, set up a co‑adsorbed CO+O configuration and locate the transition state with the nudged elastic band (NEB) method (or an equivalent saddle‑point search); the barrier is the energy difference between the transition state and the initial co‑adsorbed state. Report all requested values in the output JSON file.

## Reproduction target
Compute the adsorption energies (Eads, in eV) of CO, O₂, O, and CO₂ on Ag_ML/WC(0001) at the specified adsorption sites. Report the optimized bond lengths (in Å): the C–O bond of adsorbed CO, the O–O bond of adsorbed O₂, and the C–O bond of adsorbed CO₂. Compute the energy barrier (in eV) for the elementary step CO+O→CO₂ on the same surface. Write all results as a single JSON object to /app/outputs/results.json with the following keys: `adsorption_energies` (an object with keys `CO`, `O2`, `O`, `CO2`), `bond_lengths` (an object with keys `CO_C-O`, `O2_O-O`, `CO2_C-O`), and `barrier_CO_O` (a float). The verifier will compare each submitted value against independently obtained references.

## Assets

- Quantum ESPRESSO (pw.x, neb.x): https://www.quantum-espresso.org/
- SSSP pseudopotential library: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Bulk WC optimization
- Role: process
- Action: Perform a DFT calculation for bulk α-WC using the PW91 GGA functional and a 5×5×5 k-point grid to obtain the optimized lattice constants a and c.
- Evidence: `/app/outputs/bulk_wc_opt.json`

### Step 2: Clean Ag_ML/WC(0001) surface relaxation
- Role: process
- Action: Build a 3×3 supercell with W-terminated WC(0001) (three WC bilayers, 15 Å vacuum), place an Ag monolayer at the hcp hollow sites, relax the geometry with the bottom four atomic layers fixed, and obtain the total energy of the clean slab.
- Evidence: `/app/outputs/clean_surface_energy.json`

### Step 3: Adsorption energies and CO+O barrier
- Role: scored (load-bearing)
- Action: For CO (Ag-top site), O₂ (hcp site), atomic O (fcc site), and CO₂ (bridge site) on the relaxed Ag_ML/WC(0001) surface, perform DFT geometry optimization and compute the adsorption energy Eads = E_adsorbate + E_substrate − E_adsorbate/substrate using the isolated molecule's ground-state energy. Also set up the co-adsorbed CO+O state and locate the transition state for CO+O→CO₂ using NEB or an equivalent method; compute the energy barrier as the energy difference between the transition state and the initial co-adsorbed state. Write all results to /app/outputs/results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"adsorption_energies":{"CO":"float","O2":"float","O":"float","CO2":"float"},"bond_lengths":{"CO_C-O":"float","O2_O-O":"float","CO2_C-O":"float"},"barrier_CO_O":"float"}
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
- target_policy: reference_match
- description: Reproduced adsorption energies, key bond lengths, and the CO+O→CO₂ barrier for the Ag_ML/WC(0001) system. The checker compares these values against hidden paper-reported references with per-quantity tolerances.
- schema:
  - `type`: object
  - `required`:
    - `adsorption_energies`: object with keys CO, O2, O, CO2 (float, eV)
    - `bond_lengths`: object with keys CO_C-O, O2_O-O, CO2_C-O (float, Å)
    - `barrier_CO_O`: float (eV)
  - `units`:
    - `adsorption_energies.*`: eV
    - `bond_lengths.*`: Å
    - `barrier_CO_O`: eV

Notes: The original study used the proprietary DMol³ code; the task is re‑scoped to the open‑source Quantum ESPRESSO with PW91 functional, and tolerances absorb implementation‑dependent shifts. Electronic structure analyses (PDOS, CDD, d‑band center) and the E‑R pathway are excluded.

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
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "adsorption_energies": "object with keys CO, O2, O, CO2 (float, eV)",
          "bond_lengths": "object with keys CO_C-O, O2_O-O, CO2_C-O (float, Å)",
          "barrier_CO_O": "float (eV)"
        },
        "units": {
          "adsorption_energies.*": "eV",
          "bond_lengths.*": "Å",
          "barrier_CO_O": "eV"
        }
      },
      "description": "Reproduced adsorption energies, key bond lengths, and the CO+O→CO₂ barrier for the Ag_ML/WC(0001) system. The checker compares these values against hidden paper-reported references with per-quantity tolerances."
    }
  ],
  "notes": "The original study used the proprietary DMol³ code; the task is re‑scoped to the open‑source Quantum ESPRESSO with PW91 functional, and tolerances absorb implementation‑dependent shifts. Electronic structure analyses (PDOS, CDD, d‑band center) and the E‑R pathway are excluded."
}
```

## How you are scored
A hidden verifier reads the file /app/outputs/results.json and compares each numerical entry against reference values that are not revealed to you. The comparison uses per‑quantity tolerances that absorb systematic shifts arising from the choice of DFT code, pseudopotential library, and numerical parameters. The verifier assigns a single reward score between 0 and 1 based on how many of the submitted quantities fall within the allowed tolerance windows. Producing the entire set of values by running the specified DFT workflow is required; reporting numbers alone is not acceptable and will not pass the check. Each stage of the workflow (bulk optimization, surface relaxation, adsorbate optimizations, transition‑state search) must actually be executed and the results must be consistent with the output JSON.

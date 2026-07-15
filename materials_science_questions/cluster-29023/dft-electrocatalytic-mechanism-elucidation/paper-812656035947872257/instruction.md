# DFT Limiting Potential Difference for CO2RR vs HER on Ni-N4 Sites

## Problem background
Electrochemical reduction of CO2 to CO is a promising route for carbon utilization, but competing hydrogen evolution reaction (HER) often reduces the faradaic efficiency. Single-atom catalysts with isolated Ni–N4 sites embedded in a carbon matrix have shown exceptionally high CO selectivity. Understanding the thermodynamic origin of this selectivity requires quantifying the relative favorability of CO2 reduction versus HER on different active-site models. This reproduction task focuses on computing the difference in limiting potentials (ΔU = U_limit(CO2RR) − U_limit(HER)) for three catalyst models — an isolated Ni–N4 site, N-doped carbon without nickel, and a Ni4 cluster supported on N-doped carbon — to establish the trend in selectivity based purely on the density-functional-theory free-energy analysis.

## Approach
Use spin-polarized periodic density functional theory (DFT) to model three slab geometries: (i) a 5×5 graphene supercell containing a Ni–N4 dopant (Ni-N4-C), (ii) N-doped graphene without nickel (N-C), and (iii) a Ni4 cluster supported on N-doped graphene (Ni@N-C). For each model, perform geometry optimizations to obtain the electronic energies of the clean surface and of the key adsorbed intermediates: COOH*, CO*, and H*. Convert the raw electronic energies to Gibbs free energies at 298.15 K by adding zero-point energy corrections (from harmonic vibrational frequencies) and entropic contributions (vibrational entropy for adsorbates; standard gas-phase entropies from the NIST-JANAF tables for gas molecules). Apply the computational hydrogen electrode (CHE) model at 0 V vs RHE to construct the free-energy profiles for CO2 reduction (CO2 → COOH* → CO*) and for hydrogen evolution (H+ + e− → ½ H2). From these profiles, identify the potential-determining step and the corresponding limiting potential for each reaction on each catalyst surface. Finally, compute the difference ΔU between the limiting potential for CO2RR and that for HER for each model.

## Reproduction target
For the three catalyst models — Ni-N4-C, N-C, and Ni@N-C — compute the limiting potentials for CO2 reduction (to CO) and for hydrogen evolution, and calculate the difference ΔU = U_limit(CO2RR) − U_limit(HER). Write a single JSON file, `/app/outputs/limiting_potential_differences.json`, containing the three ΔU values with keys `"NiN4C"`, `"NC"`, and `"Ni4NC"` (each a float in volts).

## Assets

- ASE (Atomic Simulation Environment): https://pypi.org/project/ase/
- Quantum ESPRESSO (or GPAW): https://www.quantum-espresso.org/
- PseudoDojo pseudopotential library: http://www.pseudo-dojo.org/
- NIST-JANAF Thermochemical Tables: https://janaf.nist.gov/

## Workflow steps

### Step 1: Build atomistic models
- Role: process
- Action: Build three periodic slab models: (i) a 5x5 graphene supercell with a Ni–N4 dopant (Ni-N4-C), (ii) an N-doped graphene reference (N-C), and (iii) a Ni4 cluster supported on N-doped graphene (Ni@N-C). Use 20 Å vacuum spacing to isolate periodic images.
- Evidence: none

### Step 2: DFT adsorption geometry optimization
- Role: process
- Action: For each model and each adsorbate (COOH*, CO*, H*), perform spin-polarized periodic DFT calculations to determine the ground-state adsorption configuration. Compute the electronic energies of the adsorbed systems and clean surfaces.
- Evidence: none

### Step 3: Free energy calculation
- Role: process
- Action: For each adsorbate configuration, calculate vibrational frequencies to obtain zero-point energy corrections and vibrational entropies. Use standard entropies from NIST tables for gas-phase species. Compute adsorption Gibbs free energies at 298.15 K and 0 V vs RHE.
- Evidence: none

### Step 4: Limiting-potential analysis and report
- Role: scored (load-bearing)
- Action: From the free-energy profiles, determine the potential-determining step and limiting potentials for CO2 reduction (CO2 → COOH* → CO*) and hydrogen evolution (2H+ + 2e- → H2) on each model. Compute the difference ΔU = U_limit(CO2RR) - U_limit(HER). Write a JSON file containing the three ΔU values in volts.
- Output file: `/app/outputs/limiting_potential_differences.json`
- Format: json
- Contract: {"NiN4C": <float>, "NC": <float>, "Ni4NC": <float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/limiting_potential_differences.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### limiting_potential_differences.json
- path: `/app/outputs/limiting_potential_differences.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Scored artifact: the limiting-potential differences for the three catalyst models, compared to hidden gold values from the paper with tolerance and checked for correct ordering.
- schema:
  - `type`: object
  - `required`:
    - `NiN4C`: float
    - `NC`: float
    - `Ni4NC`: float
  - `units`:
    - `NiN4C`: V
    - `NC`: V
    - `Ni4NC`: V
  - `description`: Each key is a model identifier and its value is the difference in limiting potentials ΔU (in V) for CO2 reduction versus H2 evolution.

Notes: The checker compares reported ΔU values for each model to hidden gold values (extracted from the paper's Figure S20) with a tolerance of ±0.05 V, and additionally verifies that ΔU(NiN4C) > ΔU(NC) and ΔU(NiN4C) > ΔU(Ni4NC). Reward degrades if the ordering fails or values are outside tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "limiting_potential_differences.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "NiN4C": "float",
          "NC": "float",
          "Ni4NC": "float"
        },
        "units": {
          "NiN4C": "V",
          "NC": "V",
          "Ni4NC": "V"
        },
        "description": "Each key is a model identifier and its value is the difference in limiting potentials ΔU (in V) for CO2 reduction versus H2 evolution."
      },
      "description": "Scored artifact: the limiting-potential differences for the three catalyst models, compared to hidden gold values from the paper with tolerance and checked for correct ordering."
    }
  ],
  "notes": "The checker compares reported ΔU values for each model to hidden gold values (extracted from the paper's Figure S20) with a tolerance of ±0.05 V, and additionally verifies that ΔU(NiN4C) > ΔU(NC) and ΔU(NiN4C) > ΔU(Ni4NC). Reward degrades if the ordering fails or values are outside tolerance."
}
```

## How you are scored
A hidden verifier reads the submitted `limiting_potential_differences.json` and independently compares the reported ΔU values against reference values derived from the original computational study. It also checks whether the ordering of ΔU across the three models satisfies the expected relative trend. The reward is based on how closely your computed ΔU values agree with the reference values and whether the ordering is correct. No specific reference numbers are given to you — you must produce them by honestly executing the DFT workflow. Simply reporting a value without running the calculations will not yield the correct numbers and will not pass the hidden inspection.

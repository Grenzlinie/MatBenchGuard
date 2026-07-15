# DFT Adsorption Energies of NH₃, SO₂, NO, and K on MnO₂ and TiO₂ Surfaces

## Problem background
Manganese-based catalysts are attractive for low-temperature selective catalytic reduction (SCR) of NO with NH₃, but they are severely deactivated by the co-presence of alkali metals such as K⁺ and SO₂ in the flue gas. The catalyst is typically composed of an active MnOₓ component dispersed on a TiO₂ support. Understanding how the support modifies the adsorption of poisoning species is critical for designing more robust catalysts. Key species involved in poisoning and SCR include NH₃, SO₂, NO, and K. Their adsorption energies on the active component (MnO₂) and the support (TiO₂), as well as the effect of pre‑adsorbed K on these adsorption energies, are central to quantifying the resistance mechanisms.

## Approach
Density functional theory (DFT) slab calculations are used to model the (100) surface of α‑MnO₂ and the (001) surface of anatase TiO₂. For each surface, a clean slab is first relaxed. Then a single K atom is placed on the slab and the geometry is re‑optimized to obtain a K‑doped slab surface. Finally, for each of the four surface conditions (clean MnO₂, clean TiO₂, K‑doped MnO₂, K‑doped TiO₂), the adsorption geometries of NH₃, SO₂, and NO are optimized and the corresponding adsorption energies are computed. The K adsorption energy on each clean surface is also calculated. The overall set of adsorption energies provides a quantitative comparison of the affinities of the different adsorbates for the active component and the support, and reveals how pre‑adsorbed K modifies those affinities.

## Reproduction target
Using an open‑source DFT code (e.g., Quantum ESPRESSO) and standard pseudopotentials, compute the adsorption energies of NH₃, SO₂, and NO on clean and K‑doped α‑MnO₂(100) and anatase TiO₂(001) surface slabs, and the adsorption energy of K on each clean slab. Aggregate all results into a single JSON file covering all four surface conditions and all adsorbate–surface combinations.

## Assets

- α-MnO2 crystal structure: https://materialsproject.org/materials/mp-19307
- Anatase TiO2 crystal structure: https://materialsproject.org/materials/mp-390
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Pseudopotentials (SSSP efficiency): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Clean slab construction and relaxation
- Role: process
- Action: Construct α-MnO₂(100) and anatase TiO₂(001) surface slab models from the bulk crystal structures (obtained from Materials Project). Perform DFT geometry optimization to obtain relaxed clean surface slabs.
- Evidence: `/app/outputs/slab_optimization.log`

### Step 2: K adsorption and K-doped slab generation
- Role: process
- Action: Place a single K atom on each relaxed clean slab (MnO₂ and TiO₂), optimize the geometry, compute the K adsorption energies, and save the optimized K-doped surface slabs for later use.
- Evidence: `/app/outputs/k_adsorption_energies.json`

### Step 3: Compute all molecular adsorption energies
- Role: scored (load-bearing)
- Action: For each surface (clean MnO₂, clean TiO₂, K/MnO₂, K/TiO₂), place NH₃, SO₂, and NO molecules at the most stable adsorption sites, relax the geometry, and calculate the adsorption energy (Eads). Aggregate all computed Eads values (including the K adsorption energies from the previous step) into a single JSON file.
- Output file: `/app/outputs/adsorption_energies.json`
- Format: json
- Contract: A JSON object with keys "MnO2_clean", "TiO2_clean", "K_MnO2", "K_TiO2". Each maps to an object whose keys are adsorbate names ("NH3", "SO2", "NO", "K") and whose values are the adsorption energy in eV (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/adsorption_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### adsorption_energies.json
- path: `/app/outputs/adsorption_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Scored artifact: the checker compares each adsorption energy to the paper's reported values with absolute tolerance and verifies relative trends (e.g., SO₂ binds more strongly on TiO₂ than on MnO₂, K doping reduces NH₃ adsorption energy on MnO₂ by >0.5 eV).
- schema:
  - `type`: object
  - `required`:
    - `MnO2_clean`:
      - `NH3`: float
      - `SO2`: float
      - `NO`: float
      - `K`: float
    - `TiO2_clean`:
      - `NH3`: float
      - `SO2`: float
      - `NO`: float
      - `K`: float
    - `K_MnO2`:
      - `NH3`: float
      - `SO2`: float
      - `NO`: float
    - `K_TiO2`:
      - `NH3`: float
      - `SO2`: float
      - `NO`: float
  - `units`:
    - `all_energies`: eV

Notes: Only the DFT-computed adsorption energies are scored; experimental characterisation and catalytic testing are not included. The agent must produce the values from first-principles calculations using the specified public resources.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "adsorption_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "MnO2_clean": {
            "NH3": "float",
            "SO2": "float",
            "NO": "float",
            "K": "float"
          },
          "TiO2_clean": {
            "NH3": "float",
            "SO2": "float",
            "NO": "float",
            "K": "float"
          },
          "K_MnO2": {
            "NH3": "float",
            "SO2": "float",
            "NO": "float"
          },
          "K_TiO2": {
            "NH3": "float",
            "SO2": "float",
            "NO": "float"
          }
        },
        "units": {
          "all_energies": "eV"
        }
      },
      "description": "Scored artifact: the checker compares each adsorption energy to the paper's reported values with absolute tolerance and verifies relative trends (e.g., SO₂ binds more strongly on TiO₂ than on MnO₂, K doping reduces NH₃ adsorption energy on MnO₂ by >0.5 eV)."
    }
  ],
  "notes": "Only the DFT-computed adsorption energies are scored; experimental characterisation and catalytic testing are not included. The agent must produce the values from first-principles calculations using the specified public resources."
}
```

## How you are scored
A hidden verifier will independently score each workflow artifact. The primary scored artifact is the JSON file containing the adsorption energies. The verifier compares the values you report against a hidden reference derived from the original study, with appropriate tolerances to account for differences in computational setup. It also checks that key relative trends between different surfaces and doping conditions are correctly reproduced (e.g., whether a particular molecule binds more strongly on one surface than another, and whether doping changes adsorption energies in a consistent direction). Merely reporting numbers without executing the DFT pipeline will not satisfy the scoring criteria.

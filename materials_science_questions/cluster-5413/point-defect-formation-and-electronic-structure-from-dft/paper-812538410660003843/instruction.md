# Oxygen segregation energetics in a silicon grain boundary from density functional theory calculations

## Problem background
Multi-crystalline silicon is widely used for solar cells, but grain boundaries in the material can degrade performance by providing preferential sites for impurity segregation. Oxygen atoms, introduced during crystal growth, are a common impurity, and their segregation at grain boundaries can create additional electronic states that facilitate charge-carrier recombination, reducing cell efficiency. Density-functional theory (DFT) calculations can quantify the energetic drive for oxygen to segregate at a grain boundary and how that drive changes under mechanical strain and in the presence of lattice vacancies. Understanding these segregation energetics is an important step toward engineering grain boundaries to improve solar-cell performance.

## Approach
The computational approach uses plane-wave DFT with the Perdew–Burke–Ernzerhof (PBE) exchange‑correlation functional to compute total energies of an orthorhombic supercell model of the Σ3{111} silicon grain boundary containing 96 Si atoms. Two reference systems are also treated: a 64‑atom bulk silicon supercell and an isolated O₂ molecule in a large vacuum box. For each condition of interest—pristine boundary, boundary under global tensile strain, and boundary containing a Si vacancy—two DFT total energies are computed: one for the structure without oxygen and one with a single oxygen atom placed in an interstitial site that allows all Si atoms to regain tetrahedral coordination. The segregation energy of oxygen is then obtained from the difference in oxygen impurity energy between the grain boundary and bulk silicon, where the impurity energy in each environment is defined as the energy cost to insert the oxygen relative to the O₂ chemical potential. For the strained case, global tensile strain is imposed by expanding the two in‑plane lattice vectors by 3% (the third direction is kept fixed) and electronic energies are evaluated without further ionic relaxation. For the vacancy case, a specific Si atom is removed from the relaxed pristine boundary to create the V1 vacancy; the resulting defect structure is relaxed before the oxygen is inserted and the geometry re‑optimized. Executing this workflow yields a set of total energies from which the segregation energetics can be derived.

## Reproduction target
Produce the file `results.json` that contains the nine total energies listed in the output contract. From these energies, a hidden verifier will derive three segregation energies—for the pristine grain boundary, for the boundary under +3% global tensile strain, and for the boundary with a V1 Si vacancy—as well as the grain boundary formation energy. The objective is to obtain total energies that lead to physically meaningful segregation trends, but the exact target values are not disclosed to the solving agent; they are evaluated solely by the verifier.

## Assets

- GB Studio: https://github.com/ogawa345/gbstudio
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP Pseudopotentials: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Build initial structures
- Role: process
- Action: Using GB Studio or manual construction, generate the Σ3{111} Si GB orthorhombic supercell containing 96 Si atoms with approximate lattice parameters a=13.30 Å, b=7.68 Å, c=18.81 Å. Also prepare a 64-atom cubic bulk Si supercell (lattice constant a=10.86 Å) and an O₂ molecule geometry in a large vacuum box.
- Evidence: `/app/outputs/initial_structures.log`

### Step 2: DFT optimization of reference systems
- Role: process
- Action: Using Quantum ESPRESSO with the PBE functional, optimize the geometries of the pristine GB supercell, bulk Si supercell, and isolated O₂ molecule. Compute total energies of the optimized systems.
- Evidence: `/app/outputs/reference_energies.txt`

### Step 3: Interstitial oxygen in bulk Si
- Role: process
- Action: Insert one O atom into the optimized bulk Si supercell, perform full relaxation, and compute its total energy.
- Evidence: `/app/outputs/bulk_O_energy.txt`

### Step 4: Interstitial oxygen in pristine GB
- Role: process
- Action: Insert one O atom in a bond-centered interstitial site within the pristine GB that restores tetrahedral coordination. Perform full relaxation and compute the total energy.
- Evidence: `/app/outputs/pristine_GB_O_energy.txt`

### Step 5: Globally strained GB with oxygen
- Role: process
- Action: Generate a globally strained GB by expanding the a and b lattice vectors of the pristine GB supercell by +3.0% (keeping c fixed). Perform self-consistent DFT calculations (no ionic relaxation) to obtain total energies of the strained GB without O and with one O atom inserted at the equivalent bond-centered site.
- Evidence: `/app/outputs/strained_GB_O_energies.txt`

### Step 6: V1 vacancy in GB with oxygen
- Role: process
- Action: Create a V1 vacancy in the relaxed pristine GB by removing one Si atom from the appropriate site. Relax the vacancy structure. Then insert one O atom bonding with the three-fold coordinated Si atoms, relax, and compute the total energy.
- Evidence: `/app/outputs/vacancy_GB_O_energies.txt`

### Step 7: Compile final total energies
- Role: scored (load-bearing)
- Action: Write a JSON file containing all computed total energies: E_GB_pristine, E_bulk_supercell, E_1O_GB_pristine, E_1O_bulk, E_O2_molecule, E_SGB_no_O, E_1O_SGB_tensile3, E_VGB_V1_pristine, E_1O_VGB_V1_LE.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {
  "E_GB_pristine": <float (eV)>,
  "E_bulk_supercell": <float (eV)>,
  "E_1O_GB_pristine": <float (eV)>,
  "E_1O_bulk": <float (eV)>,
  "E_O2_molecule": <float (eV)>,
  "E_SGB_no_O": <float (eV)>,
  "E_1O_SGB_tensile3": <float (eV)>,
  "E_VGB_V1_pristine": <float (eV)>,
  "E_1O_VGB_V1_LE": <float (eV)>
}
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
- description: DFT total energies needed to compute oxygen segregation energies for pristine, globally strained (+3.0% tensile), and V1 vacancy-containing Σ3{111} Si grain boundaries.
- schema:
  - `type`: object
  - `required`:
    - `E_GB_pristine`:
      - `type`: number
      - `unit`: eV
    - `E_bulk_supercell`:
      - `type`: number
      - `unit`: eV
    - `E_1O_GB_pristine`:
      - `type`: number
      - `unit`: eV
    - `E_1O_bulk`:
      - `type`: number
      - `unit`: eV
    - `E_O2_molecule`:
      - `type`: number
      - `unit`: eV
    - `E_SGB_no_O`:
      - `type`: number
      - `unit`: eV
    - `E_1O_SGB_tensile3`:
      - `type`: number
      - `unit`: eV
    - `E_VGB_V1_pristine`:
      - `type`: number
      - `unit`: eV
    - `E_1O_VGB_V1_LE`:
      - `type`: number
      - `unit`: eV

Notes: The hidden checker recomputes segregation energies and the grain boundary formation energy from these raw total energies. Only the n=1 oxygen case is required.

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
        "required": {
          "E_GB_pristine": {
            "type": "number",
            "unit": "eV"
          },
          "E_bulk_supercell": {
            "type": "number",
            "unit": "eV"
          },
          "E_1O_GB_pristine": {
            "type": "number",
            "unit": "eV"
          },
          "E_1O_bulk": {
            "type": "number",
            "unit": "eV"
          },
          "E_O2_molecule": {
            "type": "number",
            "unit": "eV"
          },
          "E_SGB_no_O": {
            "type": "number",
            "unit": "eV"
          },
          "E_1O_SGB_tensile3": {
            "type": "number",
            "unit": "eV"
          },
          "E_VGB_V1_pristine": {
            "type": "number",
            "unit": "eV"
          },
          "E_1O_VGB_V1_LE": {
            "type": "number",
            "unit": "eV"
          }
        }
      },
      "description": "DFT total energies needed to compute oxygen segregation energies for pristine, globally strained (+3.0% tensile), and V1 vacancy-containing Σ3{111} Si grain boundaries."
    }
  ],
  "notes": "The hidden checker recomputes segregation energies and the grain boundary formation energy from these raw total energies. Only the n=1 oxygen case is required."
}
```

## How you are scored
A hidden verifier reads your `results.json` and recomputes the three oxygen segregation energies and the grain boundary formation energy using the standard formulas given in the approach description. Each recomputed quantity is compared against a hidden gold standard; you earn credit for a quantity when your derived value lies within the verifier's tolerance of that gold. In addition, the verifier checks that the segregation energies across the three conditions (pristine, strained, vacancy) follow the expected physical ordering—i.e., the relative rank of the three energies is assessed. The final reward is a weighted combination of these per‑quantity checks and the trend check. No further information about the gold values or tolerances is provided; the task is to run the DFT calculations and report the resulting total energies as accurately as the protocol allows.

# NO adsorption on pristine and TM-embedded graphitic carbon nitride

## Problem background
Nitric oxide (NO) is a major air pollutant that is hazardous to human health and originates from combustion in vehicles and industry. Graphitic carbon nitride (gCN) is a promising material for gas sensing due to its high surface area, chemical stability, and tunable electronic properties. Embedding transition metal atoms such as Fe, Ru, or Os into the gCN lattice can modify its electronic structure and adsorption behavior. This work uses density functional theory (DFT) to investigate whether NO is physisorbed or chemisorbed on pristine gCN and on TM‑embedded gCN, and to quantify the resulting adsorption energies, electronic structure changes, and magnetic responses. The computed properties will allow you to assess which system, if any, is best suited for NO detection.

## Approach
All calculations use spin‑polarized DFT as implemented in Quantum Espresso with the PBE exchange‑correlation functional. The workflow proceeds as follows: (1) construct a 2×2 supercell of heptazine‑based gCN, (2) relax the pristine gCN structure to obtain a reference energy and geometry, (3) embed Fe, Ru, and Os atoms individually at the vacancy site and relax each TM‑embedded system, (4) compute the energy and bond length of an isolated NO molecule in the same supercell, (5) build initial geometries for NO adsorbed on pristine gCN and on each TM‑embedded gCN, and relax these four complexes, (6) extract band gaps, Löwdin charges, and magnetic moments from the relaxed structures, and (7) compute adsorption energies as E_ads = E(gCN+NO) – E(gCN) – E(NO). The final JSON output collects all computed quantities for the four post‑adsorption systems.

## Reproduction target
For each of the four post‑adsorption systems (pristine gCN + NO, Fe‑embedded gCN + NO, Ru‑embedded gCN + NO, Os‑embedded gCN + NO), compute and report the following quantities in a single JSON file `/app/outputs/adsorption_results.json`: the adsorption energy Eads (eV), the band gap Eg (eV), the total magnetic moment Mtot (µB), the N–O bond length d_NO (Å), the TM–N distance d_TMN (Å; set to null for the pristine system), and the Löwdin charges (in esu) on the N atom of NO, the O atom of NO, and the N_edge atom of gCN. The JSON must contain an array named ‘systems’ with one object per system, each using the keys system_name, Eads, Eg, Mtot, d_NO, d_TMN, N_NO_Lowdin, O_NO_Lowdin, and Ned_gCN_Lowdin.

## Assets

- Quantum Espresso: https://www.quantum-espresso.org/
- SSSP efficiency PBE pseudopotentials (or equivalent standard library): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Build gCN supercell model
- Role: process
- Action: Construct the atomic positions of the 2×2 heptazine-based gCN supercell using the lattice parameter and internal coordinates, and write the input structure file.
- Evidence: `/app/outputs/gcn_supercell.pwi`

### Step 2: Relax pristine gCN supercell
- Role: process
- Action: Perform spin-polarized DFT geometry optimization of the pristine 2×2 gCN supercell using Quantum Espresso. Save the final total energy and relaxed atomic positions.
- Evidence: `/app/outputs/pristine_gcn.out`

### Step 3: Relax TM-embedded gCN (Fe, Ru, Os)
- Role: process
- Action: For each transition metal (Fe, Ru, Os), embed the atom at the vacancy site of the relaxed pristine gCN and perform spin-polarized DFT geometry optimization. Record final total energies, TM-N_edge distances, and magnetic moments.
- Evidence: `/app/outputs/tm_embedded.out`

### Step 4: Reference calculation of isolated NO molecule
- Role: process
- Action: Place a single NO molecule in the same supercell size and perform spin-polarized DFT geometry optimization to obtain total energy and equilibrium N-O bond length of isolated NO.
- Evidence: `/app/outputs/isolated_NO.out`

### Step 5: Relax NO‑adsorbed complexes
- Role: process
- Action: Construct initial geometries for NO adsorbed on pristine gCN and on Fe, Ru, Os-embedded gCN. For each system, perform spin-polarized DFT geometry optimization. Save final total energies, relaxed atomic positions, N–O bond lengths, TM–N distances, and total magnetic moments.
- Evidence: `/app/outputs/no_adsorbed.out`

### Step 6: Extract electronic properties and Löwdin charges
- Role: process
- Action: For each relaxed NO-adsorbed structure, perform a single-point calculation to obtain band gap energies and Löwdin charges on N(NO), O(NO), and N_edge(gCN). Collect these values.
- Evidence: `/app/outputs/electronic_properties.txt`

### Step 7: Output final adsorption results
- Role: scored (load-bearing)
- Action: Using results from previous steps, compute adsorption energies as E_ads = E(gCN+NO) - E(gCN) - E(NO). Compile all computed properties for the four post-adsorption systems into a JSON file with keys: system_name, Eads (eV), Eg (eV), Mtot (µB), d_NO (Å), d_TMN (Å or null for pristine), N_NO_Lowdin (esu), O_NO_Lowdin (esu), Ned_gCN_Lowdin (esu). Write to /app/outputs/adsorption_results.json.
- Output file: `/app/outputs/adsorption_results.json`
- Format: json
- Contract: Object with key 'systems' holding an array of 4 objects. Each object has keys: system_name (string), Eads (float, eV), Eg (float, eV), Mtot (float, µB), d_NO (float, Å), d_TMN (float or null for pristine), N_NO_Lowdin (float, esu), O_NO_Lowdin (float, esu), Ned_gCN_Lowdin (float, esu).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/adsorption_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### adsorption_results.json
- path: `/app/outputs/adsorption_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Compiled DFT adsorption properties for the four post-adsorption systems (pristine/NO, Fe/NO, Ru/NO, Os/NO).
- schema:
  - `type`: object
  - `required`:
    - `systems`: array of 4 objects
  - `items`:
    - `system_name`: string
    - `Eads`: float (eV)
    - `Eg`: float (eV)
    - `Mtot`: float (µB)
    - `d_NO`: float (Å)
    - `d_TMN`: float or null (Å)
    - `N_NO_Lowdin`: float (esu)
    - `O_NO_Lowdin`: float (esu)
    - `Ned_gCN_Lowdin`: float (esu)

Notes: The checker compares each numeric field against the paper's Table 2 values using appropriate tolerances and enforces structural trends (e.g., adsorption energies of TM-embedded systems more negative than pristine, Os-embedded most negative).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "adsorption_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "systems": "array of 4 objects"
        },
        "items": {
          "system_name": "string",
          "Eads": "float (eV)",
          "Eg": "float (eV)",
          "Mtot": "float (µB)",
          "d_NO": "float (Å)",
          "d_TMN": "float or null (Å)",
          "N_NO_Lowdin": "float (esu)",
          "O_NO_Lowdin": "float (esu)",
          "Ned_gCN_Lowdin": "float (esu)"
        }
      },
      "description": "Compiled DFT adsorption properties for the four post-adsorption systems (pristine/NO, Fe/NO, Ru/NO, Os/NO)."
    }
  ],
  "notes": "The checker compares each numeric field against the paper's Table 2 values using appropriate tolerances and enforces structural trends (e.g., adsorption energies of TM-embedded systems more negative than pristine, Os-embedded most negative)."
}
```

## How you are scored
A hidden verifier reads your `adsorption_results.json` and compares every numerical field against a set of reference values derived from the original study. The comparison uses tolerances appropriate for the method to account for differences in pseudopotential sets, computational settings, and implementation details. In addition, the verifier checks structural trends: for example, whether the adsorption energies of the TM‑embedded systems are more negative than that of the pristine system, and whether the Os‑embedded system yields distinct magnetic behavior. The final score is a weighted combination of field‑level accuracy and satisfaction of the structural checks. Your goal is to faithfully reproduce the physical results by executing the DFT workflow, not merely to report a predefined number.

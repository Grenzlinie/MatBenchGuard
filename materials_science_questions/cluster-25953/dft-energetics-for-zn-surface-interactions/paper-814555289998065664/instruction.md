# DFT Investigation of Zn-AIM Binding Sites and Deposition Pathways on NU-1000

## Problem background
Metal-organic frameworks (MOFs) can serve as scaffolds for atomically dispersed metal ions, which are promising catalysts. A recently developed method, AIM (ALD in MOFs), installs reactive metal sites onto the nodes of the mesoporous MOF NU-1000 through atomic layer deposition. The intermediate Zn-AIM, obtained via reaction of diethylzinc (ZnEt₂) with NU-1000, is a key precursor for accessing a variety of nonstructural metals via transmetalation. Understanding the structure and formation energetics of Zn-AIM is essential for rational design of these materials, but direct experimental determination of the Zn binding sites, coordination geometry, and the energetic pathway for loading multiple Zn atoms is challenging. Density functional theory (DFT) calculations offer a route to compute these properties and guide the interpretation of the experimental data.

## Approach
The computational approach uses gas-phase DFT with the M06-L density functional. A cluster model of the NU-1000 node (150 atoms, truncated benzoate linkers, frozen linker carbons) serves as the starting point. The 6-31G(d) basis set is used for C, H, and O; the Stuttgart RLC ECP and associated basis (SDD) are used for Zn and Zr. The workflow proceeds in four stages:

1. **Cluster preparation**: construct the node model from public literature coordinates.
2. **Binding site screening**: substitute a ZnEt group at each of the four distinct proton sites (μ-OH, OH, hydrogen-bonded H₂O proton, and non-hydrogen-bonded H₂O proton) and compute the relative electronic energies (ΔE) and free energies at 383 K (ΔG₃₈₃) with respect to the most stable site. The most favorable site is identified.
3. **Single-Zn coordination**: from the preferred binding site, perform a geometry optimization after ethane elimination to isolate a single Zn ion attached to the node. The coordination number, qualitative geometry description, and average Zn–O bond length are extracted.
4. **Four-Zn pathway survey**: evaluate two competing pathways for depositing four Zn atoms: one Zn per node face vs. two Zn per face. Both unhydrated and hydrated intermediates are considered. Relative free energies are referenced to the bare node plus four ZnEt₂ molecules and four water molecules. The energetically preferred unhydrated structure is determined.

All energies are computed at the M06-L/6-31G(d)+SDD level. The calculations are performed with any DFT code that supports the M06-L functional (e.g., ORCA, Gaussian, PySCF).

## Reproduction target
Produce three scored artifacts that capture the DFT-derived sub-results of the Zn-AIM system:

1. **binding_energies.csv**: relative electronic energies (ΔE) and free energies at 383 K (ΔG₃₈₃) for ZnEt substitution at the four proton sites (μ-OH, OH, HB, H₂O), referenced to the most stable site. Each site occupies one row; units are kcal/mol.
2. **single_zn_geometry.txt**: after ethane elimination from the most favorable site, report the coordination number of the single Zn ion, a qualitative geometry description, and the average Zn–O bond length (Å).
3. **four_zn_pathway.json**: relative free energies (ΔG₃₈₃) of the two four-Zn deposition pathways (unhydrated and hydrated intermediates) and the label of the preferred unhydrated structure.

The objective is to independently compute these quantities by building the cluster model, running the required DFT calculations, and organizing the results as specified. The computational approach and cluster model details are provided; the numeric results emerge from the correct implementation of the protocol.

## Assets

- NU‑1000 node cluster model (Planas et al., J. Phys. Chem. Lett., 2014): 10.1021/jz5023366
- 6‑31G(d) and Stuttgart RLC ECP (SDD) basis sets: https://www.basissetexchange.org
- DFT software supporting M06‑L (e.g., ORCA, Gaussian, PySCF)

## Workflow steps

### Step 1: Build NU‑1000 node cluster model
- Role: process
- Action: Construct the 150‑atom cluster model of the NU‑1000 node with truncated benzoate linkers as described in Planas et al. (J. Phys. Chem. Lett. 2014). Freeze the carbon atoms of the eight linkers and verify the total atom count.
- Evidence: `/app/outputs/model_ready.log`

### Step 2: Compute binding site relative energies
- Role: scored (load-bearing)
- Action: Perform DFT single‑point energy calculations and geometry optimizations at the M06‑L/6‑31G(d)+SDD level for the bare node and for ZnEt substituted at each of the four proton sites (μ‑OH, OH, HB, H₂O). Compute relative electronic energies (ΔE) and free energies at 383 K (ΔG₃₈₃) with respect to the most stable site. Write the results to binding_energies.csv.
- Output file: `/app/outputs/binding_energies.csv`
- Format: csv
- Contract: Columns: binding_site (string: μ‑OH, OH, HB, H₂O), delta_E (float, kcal/mol), delta_G_383 (float, kcal/mol).
- Scoring: scored by hidden verifier

### Step 3: Determine single‑Zn coordination geometry
- Role: scored
- Action: From the most favorable binding site (as determined in Step 2), perform a geometry optimization after ethane elimination to obtain the structure of a single Zn ion attached to the node. Determine the coordination number of Zn, describe its geometry, and record the average Zn–O bond length. Write the information to single_zn_geometry.txt.
- Output file: `/app/outputs/single_zn_geometry.txt`
- Format: txt
- Contract: Lines: 'coordination_number=<int>', 'geometry=<string>', 'avg_Zn_O_distance=<float>'. Zn–O distances in Å.
- Scoring: scored by hidden verifier

### Step 4: Compute four‑Zn deposition pathway energetics
- Role: scored
- Action: Evaluate the two competing reaction pathways for depositing four Zn atoms: one Zn per node face (4[H₂O,OH]) and two Zn per face (2[H₂O/μOH]). Compute relative free energies (ΔG₃₈₃) for the unhydrated and hydrated intermediates referenced to the bare node plus four ZnEt₂ and four water molecules. Identify which unhydrated structure is lower in energy. Write the results to four_zn_pathway.json.
- Output file: `/app/outputs/four_zn_pathway.json`
- Format: json
- Contract: Keys: one_per_face_unhydrated, two_per_face_unhydrated, one_per_face_hydrated, two_per_face_hydrated (all float, kcal/mol), preferred_structure (string: 'one_per_face' or 'two_per_face').
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/binding_energies.csv`
- `/app/outputs/single_zn_geometry.txt`
- `/app/outputs/four_zn_pathway.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### binding_energies.csv
- path: `/app/outputs/binding_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Relative electronic and free energies for ZnEt substitution at the four proton sites. The checker will compare the ordering and values (within tolerances) to the paper‑reported reference.
- schema:
  - `type`: table
  - `required_columns`: `binding_site`, `delta_E`, `delta_G_383`
  - `units`:
    - `delta_E`: kcal/mol
    - `delta_G_383`: kcal/mol

### single_zn_geometry.txt
- path: `/app/outputs/single_zn_geometry.txt`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Coordination number and geometry of a single Zn atom attached at the most favorable H₂O site.
- schema:
  - `type`: text
  - `description`: Should contain lines with coordination_number, geometry, and avg_Zn_O_distance. The checker will verify coordination number = 4 and geometry described as tetrahedral.

### four_zn_pathway.json
- path: `/app/outputs/four_zn_pathway.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Free energies for the two competing four‑Zn deposition pathways. The checker will confirm that the one‑per‑face unhydrated structure is lower in energy by at least 8 kcal/mol and that preferred_structure is 'one_per_face'.
- schema:
  - `type`: object
  - `required`:
    - `one_per_face_unhydrated`: number
    - `two_per_face_unhydrated`: number
    - `one_per_face_hydrated`: number
    - `two_per_face_hydrated`: number
    - `preferred_structure`: string

Notes: All comparisons assume a toolchain spread from the paper's Gaussian 09/M06‑L/6‑31G(d)+SDD protocol. Tolerances will be chosen to absorb legitimate code‑to‑code variation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "binding_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "binding_site",
          "delta_E",
          "delta_G_383"
        ],
        "units": {
          "delta_E": "kcal/mol",
          "delta_G_383": "kcal/mol"
        }
      },
      "description": "Relative electronic and free energies for ZnEt substitution at the four proton sites. The checker will compare the ordering and values (within tolerances) to the paper‑reported reference."
    },
    {
      "file": "single_zn_geometry.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "description": "Should contain lines with coordination_number, geometry, and avg_Zn_O_distance. The checker will verify coordination number = 4 and geometry described as tetrahedral."
      },
      "description": "Coordination number and geometry of a single Zn atom attached at the most favorable H₂O site."
    },
    {
      "file": "four_zn_pathway.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "one_per_face_unhydrated": "number",
          "two_per_face_unhydrated": "number",
          "one_per_face_hydrated": "number",
          "two_per_face_hydrated": "number",
          "preferred_structure": "string"
        }
      },
      "description": "Free energies for the two competing four‑Zn deposition pathways. The checker will confirm that the one‑per‑face unhydrated structure is lower in energy by at least 8 kcal/mol and that preferred_structure is 'one_per_face'."
    }
  ],
  "notes": "All comparisons assume a toolchain spread from the paper's Gaussian 09/M06‑L/6‑31G(d)+SDD protocol. Tolerances will be chosen to absorb legitimate code‑to‑code variation."
}
```

## How you are scored
A hidden verifier will score each of the three required artifacts independently, then combine the scores into a final reward (a float between 0 and 1). The verifier compares your computed numerical values and structural findings against reference expectations derived from the original study's reported DFT results. It checks the relative ordering and approximate magnitudes of the binding energies, the reported coordination number and geometry, and the energetic preference between the two four-Zn pathways. Your work is evaluated on the correctness of the computed results given the described protocol, not on whether you can retrieve pre-existing numbers. Following the specified workflow and submitting all artifacts in the required formats is essential.

# Oxygen vacancy defect formation energies and magnetic states on α-quartz surfaces

## Problem background
Superconducting qubits and SQUIDs suffer from magnetic flux noise that limits quantum coherence, with surface defects on the silica substrate being a likely source. This computational task investigates oxygen deficiency centers (ODCs) — missing oxygen atoms — on α‑quartz (001) and (100) surfaces. The aim is to compute the formation energies and identify the magnetic ground states of these defects to determine their potential role in generating magnetic fluctuations.

## Approach
The reproduction uses density functional theory (DFT) with the local spin density approximation (LSDA). First, the bulk α‑quartz unit cell is relaxed, and stoichiometric surface slabs are constructed for the (001) and (100) orientations. A reference calculation of an isolated O₂ molecule provides a chemical potential. Oxygen vacancies are then created at multiple crystallographically distinct sites on each surface, each in neutral, +1, and +2 charge states. Spin‑polarized DFT relaxations are performed for every defect configuration to obtain ground‑state total energies and magnetic moments. These results are used to compute defect formation energies relative to the pristine slab and O₂ chemical potential, and to classify whether each defect exhibits a low‑energy magnetic state.

## Reproduction target
Compute the defect formation energy (in eV) for every oxygen vacancy site/charge‑state combination on both the (001) and (100) α‑quartz surfaces, totaling 18 distinct configurations. Additionally, determine whether each defect's ground state is magnetic, defined by an absolute total magnetic moment greater than 0.1 μB. The formation energy for each defect is derived from the total energy of its supercell, the energy of the corresponding pristine slab, the oxygen chemical potential from molecular O₂, and the valence‑band maximum of the pristine slab.

## Assets

- Quantum ESPRESSO (or other open-source DFT code): https://www.quantum-espresso.org
- LSDA pseudopotentials for Si and O: https://pseudodojo.quantummaterials.org
- α‑quartz crystal structure (P3₂21, left-handed chirality): 10.2138/am-1980-920

## Workflow steps

### Step 1: Bulk α‑quartz relaxation
- Role: process
- Action: Perform a DFT (LSDA) relaxation of the bulk α‑quartz unit cell (space group P3₂21, left-handed chirality) to obtain the relaxed lattice parameters and atomic coordinates. Use an open-source DFT code with appropriate pseudopotentials and convergence criteria.
- Evidence: `/app/outputs/bulk_relaxation.log`

### Step 2: Surface slab construction and relaxation
- Role: process
- Action: Build stoichiometric (001) and (100) surface slabs from the relaxed bulk structure, using supercell dimensions with surface area ~100 Å² per side and vacuum spacing 15 Å. Relax the slabs with DFT (LSDA), allowing cell shape changes but fixed volume. Compute the total energy (E_slab) and the valence‑band maximum (E_VBM) for each relaxed slab.
- Evidence: `/app/outputs/slab_relaxation.log`

### Step 3: O₂ chemical potential
- Role: process
- Action: Perform a DFT (LSDA) calculation of an isolated O₂ molecule in a large box to obtain its total energy, E_O2. Compute the oxygen chemical potential as μ_O2 = 0.5 × E_O2.
- Evidence: `/app/outputs/o2_chemical_potential.log`

### Step 4: Defect supercell generation
- Role: process
- Action: From the relaxed (001) and (100) slabs, create oxygen vacancies at the specified sites: on (001) site 1, site 2, and subsurface (ss); on (100) bridge, metastable ring, and ring 2III‑O positions. Generate supercells with charge states 0, +1, +2 for each vacancy, yielding 18 distinct defect configurations. Charged cells are compensated by a uniform background charge.
- Evidence: `/app/outputs/defect_supercells.log`

### Step 5: Spin‑polarized DFT relaxation of defects
- Role: process
- Action: For each of the 18 defect supercells, perform spin‑polarized DFT (LSDA) structural relaxations, exploring possible magnetic configurations to locate the lowest‑energy geometry. Record the relaxed total energy (E_defect) and the ground‑state total magnetic moment (μ) for each defect.
- Evidence: `/app/outputs/defect_relaxations.log`

### Step 6: Formation energy calculation
- Role: scored (load-bearing)
- Action: Using E_defect from step 5, E_slab and E_VBM from step 2, and μ_O2 from step 3, compute the defect formation energy for each of the 18 defects via: E_form = E_defect − E_slab + 0.5 × μ_O2 + q × E_VBM. Write the results to formation_energies.json.
- Output file: `/app/outputs/formation_energies.json`
- Format: json
- Contract: JSON object; keys are defect identifiers such as '(001)-site1-q0', '(100)-bridge-q1+', etc.; values are floating-point numbers (eV). Must include all 18 entries from the paper's Table II.
- Scoring: scored by hidden verifier

### Step 7: Magnetic state classification
- Role: scored
- Action: Based on the ground‑state magnetic moments from step 5, classify each defect as having a low‑energy magnetic state (LEMS). A defect is classified as LEMS if its ground‑state total magnetic moment is non‑zero (|μ| > 0.1 μB). Write the results to magnetic_states.json.
- Output file: `/app/outputs/magnetic_states.json`
- Format: json
- Contract: JSON object; same keys as formation_energies.json; values are booleans (true if the defect has a magnetic ground state, false otherwise).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/formation_energies.json`
- `/app/outputs/magnetic_states.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### formation_energies.json
- path: `/app/outputs/formation_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Defect formation energies (eV) for all 18 oxygen vacancy configurations, keyed by site and charge state identifiers.
- schema:
  - `type`: object
  - `required`:
    - `defect_key`: number (eV)

### magnetic_states.json
- path: `/app/outputs/magnetic_states.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Low‑energy magnetic state classification for each defect (true = LEMS, false = non‑magnetic ground state).
- schema:
  - `type`: object
  - `required`:
    - `defect_key`: boolean

Notes: The task reproduces the paper's LSDA‑based oxygen vacancy study using an open‑source DFT code. The solver must perform all DFT relaxations for the bulk, surfaces, O₂ molecule, and 18 defect supercells, then compute formation energies and magnetic state classification. The verifier compares formation energies to the paper's Table II values with a permissive tolerance and requires exact magnetic state classification.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "formation_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "defect_key": "number (eV)"
        }
      },
      "description": "Defect formation energies (eV) for all 18 oxygen vacancy configurations, keyed by site and charge state identifiers."
    },
    {
      "file": "magnetic_states.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "defect_key": "boolean"
        }
      },
      "description": "Low‑energy magnetic state classification for each defect (true = LEMS, false = non‑magnetic ground state)."
    }
  ],
  "notes": "The task reproduces the paper's LSDA‑based oxygen vacancy study using an open‑source DFT code. The solver must perform all DFT relaxations for the bulk, surfaces, O₂ molecule, and 18 defect supercells, then compute formation energies and magnetic state classification. The verifier compares formation energies to the paper's Table II values with a permissive tolerance and requires exact magnetic state classification."
}
```

## How you are scored
A hidden verifier independently scores your submitted artifacts, formation_energies.json and magnetic_states.json, by comparing your computed values against reference results. The reward is proportional to the number of entries that agree with the reference. To receive credit, the artifacts must be the product of executing the specified DFT workflow; self-reporting numbers without running the computational steps will not satisfy the scoring criteria. Exact scoring thresholds and aggregation rules are hidden.

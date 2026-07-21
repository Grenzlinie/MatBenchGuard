# AIMD/BOMD Dynamical Stability Assessment of Electrolytes on Calcium Surface

## Problem background
Multivalent calcium-ion batteries (CIBs) are attractive for next-generation energy storage because calcium is abundant and can deliver high energy density. A major obstacle, however, is that many electrolyte components (salts and solvents) react with the strongly reducing calcium metal anode, either decomposing or forming a blocking layer that prevents reversible plating and stripping of calcium. Understanding which electrolyte species remain intact when in contact with calcium is therefore critical for designing viable CIBs. This task evaluates the reductive stability of several candidate salts and a candidate solvent on a Ca(001) surface through first-principles molecular dynamics simulations.

## Approach
The core approach is to use Born–Oppenheimer molecular dynamics (BOMD) to expose individual electrolyte molecules to a realistic calcium surface at room temperature and to watch for signs of degradation. A six-layer Ca(001) slab is built, and a single molecule of each candidate is placed on top. For each system, a geometry optimization is first performed, followed by an NVT BOMD simulation at 300 K lasting at least 10 ps with a 1 fs time step. The level of theory is density functional theory with the PBE functional, DZVP basis set, Grimme D3 dispersion correction, and a 300 Ry plane‑wave cutoff, as implemented in the open‑source CP2K package. During the simulation, Mulliken charges on the electrolyte are recorded at every time step. The key observables are (i) the maximum amount of electron charge transferred from the calcium slab to the molecule, tracked as the gain relative to the initial state, and (ii) whether any covalent bond in the molecule breaks. Three types of candidates are examined: a glyme solvent (G4), a closo‑monocarborane salt (Ca[CB₁₁H₁₂]₂), and one salt that is expected to be less stable, chosen from Ca[PF₆]₂, Ca[TFSI]₂, or Ca[B(hfip)₄]₂.

## Reproduction target
Using the BOMD procedure described above, assess the reductive stability of three electrolyte‑candidate systems on a Ca(001) surface at 300 K: G4, Ca[CB₁₁H₁₂]₂, and one unstable reference salt that you select from Ca[PF₆]₂, Ca[TFSI]₂, or Ca[B(hfip)₄]₂. For each candidate, compute (1) the maximum charge transferred from the calcium surface to the molecule, in units of electrons, relative to the first simulation step, and (2) whether any bond cleavage event is observed during the trajectory. Write a single JSON file that records these two quantities for every candidate. The file must be placed at /app/outputs/stability_assessment.json. The hidden verifier will check your reported numbers and booleans against acceptance criteria derived from the original study; therefore you must obtain the values by actually running the simulations — copying plausible numbers from the literature is not sufficient.

## Assets

- CP2K: https://www.cp2k.org/

## Workflow steps

### Step 1: Geometry optimization of electrolyte-Ca interfaces
- Role: process
- Action: Build a six-layer Ca(001) slab model and place a single molecule of each candidate electrolyte (G4 solvent, Ca[CB11H12]2 salt, and one unstable reference salt chosen from Ca[PF6]2, Ca[TFSI]2, or Ca[B(hfip)4]2) on the surface. Using CP2K with the PBE functional, DZVP basis set, Grimme D3 dispersion correction, and 300 Ry plane-wave cutoff, optimize each interface structure until forces are below 0.02 eV/Å.
- Evidence: none

### Step 2: Run BOMD simulations at 300 K
- Role: process
- Action: For each optimized interface, perform a Born-Oppenheimer molecular dynamics (BOMD) simulation in the NVT ensemble at 300 K using a 1 fs timestep and Nosé-Hoover thermostat (chain length 3). Propagate for at least 10 ps, saving atomic positions and Mulliken charges at each time step. Use the same CP2K settings as the optimization.
- Evidence: none

### Step 3: Compute charge transfer and bond cleavage
- Role: scored (load-bearing)
- Action: From the BOMD trajectories, compute the total Mulliken charge on the electrolyte molecule at each step; determine the maximum electron gain (charge transfer) from the Ca surface relative to the first step. Inspect the final geometry (or the entire trajectory) for any bond cleavage events. Output a single JSON file with the max charge transfer and bond cleavage observation for each candidate.
- Output file: `/app/outputs/stability_assessment.json`
- Format: json
- Contract: Object with top-level keys: 'G4', 'CaCB11H12', and one key naming the chosen unstable reference (one of 'CaPF6', 'CaTFSI', 'CaBhfip4'). Each value is an object with fields: 'max_charge_transfer' (float, in electrons) and 'bond_cleavage_observed' (boolean).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/stability_assessment.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### stability_assessment.json
- path: `/app/outputs/stability_assessment.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: JSON file reporting the maximum charge transferred from the Ca surface to each electrolyte candidate and whether bond cleavage was observed.
- schema:
  - `type`: object
  - `required_top_keys`: `G4`, `CaCB11H12`
  - `additional_key_must_be_one_of`: `CaPF6`, `CaTFSI`, `CaBhfip4`
  - `value_object_schema`:
    - `max_charge_transfer`: float
    - `bond_cleavage_observed`: boolean

Notes: The chosen unstable reference candidate must be one of CaPF6, CaTFSI, or CaBhfip4, corresponding to the salts studied in the original work. The hidden checker verifies that stable candidates exhibit negligible charge transfer and no bond cleavage, while the unstable candidate shows significant charge transfer and bond cleavage, consistent with the reported stability ordering.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "stability_assessment.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required_top_keys": [
          "G4",
          "CaCB11H12"
        ],
        "additional_key_must_be_one_of": [
          "CaPF6",
          "CaTFSI",
          "CaBhfip4"
        ],
        "value_object_schema": {
          "max_charge_transfer": "float",
          "bond_cleavage_observed": "boolean"
        }
      },
      "description": "JSON file reporting the maximum charge transferred from the Ca surface to each electrolyte candidate and whether bond cleavage was observed."
    }
  ],
  "notes": "The chosen unstable reference candidate must be one of CaPF6, CaTFSI, or CaBhfip4, corresponding to the salts studied in the original work. The hidden checker verifies that stable candidates exhibit negligible charge transfer and no bond cleavage, while the unstable candidate shows significant charge transfer and bond cleavage, consistent with the reported stability ordering."
}
```

## How you are scored
A hidden verifier reads your /app/outputs/stability_assessment.json. It validates the JSON schema (presence of all required keys, correct data types) and then compares your reported maximum charge transfers and bond‑cleavage observations to hidden reference criteria. The score is computed as a weighted combination: the main weight is on the correctness of the reported quantities for the three candidates. Full credit is awarded for candidates whose numbers and observations meet the criteria; partial credit is given when only some candidates are correct. The verifier does not re‑run the expensive BOMD simulations — it trusts that the numbers you report originate from genuine calculations, but it will only reward values that are consistent with the physics of the problem as captured by the reference criteria.

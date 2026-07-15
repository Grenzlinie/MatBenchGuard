# Li Migration Barriers and Electrochemical Properties of LiMS2 Cathodes via DFT

## Problem background
All-solid-state lithium batteries with sulfide solid electrolytes offer improved safety over liquid-electrolyte cells, but conventional oxide cathodes (e.g., LiCoO2) are chemically incompatible with sulfide electrolytes, leading to high interfacial resistance. This work investigates a series of chalcopyrite-structured sulfide cathode materials, LiMS2 (where M = Cr, Mn, Fe, Co, Ni), as alternatives to oxide cathodes. The key open questions are whether these materials provide sufficiently fast lithium-ion transport (low migration barriers), deliver stable intercalation voltages around 3 V, maintain small volume changes during cycling, and form compatible interfaces with the sulfide electrolyte Li3PS4. Your task is to compute these properties via a first-principles computational pipeline and provide the raw outputs that allow an automated checker to verify the results against the paper’s published numbers.

## Approach
Use density functional theory (DFT) with the open-source code CP2K. The method consists of two functional levels: the generalized gradient approximation (PBE) for structure relaxations and climbing-image nudged elastic band (CI-NEB) barrier calculations, and the screened hybrid functional HSE06 for accurate total energies. The workflow evaluates: (1) the lithium vacancy migration barrier in bulk LiMS2 by building a 2×2×1 supercell with one Li vacancy and performing CI-NEB with PBE; (2) the average intercalation voltage and unit-cell volume change upon full delithiation for each cathode, derived from HSE06 total energies of the end-member and intermediate compositions against a Li metal reference; (3) the Li diffusion barrier across a LiCrS2(112)/β-Li3PS4(010) interface, constructed according to the paper’s crystallographic matching procedure and relaxed with PBE, followed by CI-NEB. The outputs are raw NEB energy profiles, formation energies of delithiated compounds, and relaxed volumes, which enable independent recomputation of the headline quantities.

## Reproduction target
Generate the crystal structures of LiMS2 (M=Cr, Mn, Fe, Co, Ni) and their delithiated intermediates Li_xMS2 (x=0.75, 0.5, 0.25, 0) as well as BCC Li metal. Using CP2K, perform HSE06 unit-cell relaxations to obtain total energies and volumes. From these, produce (i) /app/outputs/formation_energies.csv containing the total energy per formula unit for each composition, and (ii) /app/outputs/relaxed_volumes.csv containing the unit-cell volumes of LiMS2 and MS2. For each LiMS2, perform CI-NEB with PBE on a 2×2×1 supercell containing one Li vacancy and write the image energies to /app/outputs/neb_energy_profiles.json. Construct the LiCrS2(112)/β-Li3PS4(010) interface with lattice mismatch ≤ 6.45%, relax it with PBE, and compute the Li diffusion path across the interface via CI-NEB; output the image energies to /app/outputs/interface_neb_profile.json. The submitted CSV and JSON files must strictly follow the output contracts given in the workload steps. The verifier will recompute the migration barriers, average intercalation voltages, volume change percentages, and the interface barrier from these raw artifacts and compare them to the paper’s reported values.

## Assets

- CP2K (Open-source DFT code with hybrid functional and NEB support): https://www.cp2k.org/
- Crystal structure of β-Li3PS4: 10.1016/j.ssi.2011.08.016

## Workflow steps

### Step 1: Generate initial crystal structures
- Role: process
- Action: Create the I42d chalcopyrite structures for LiMS2 (M=Cr, Mn, Fe, Co, Ni) and the delithiated compositions Li_xMS2 (x=0.75, 0.5, 0.25, 0) using lattice constants and atomic positions described in the paper. Also prepare the BCC Li metal unit cell.
- Evidence: `/app/outputs/structure_generation.log`

### Step 2: HSE06 relaxation of compositions
- Role: process
- Action: Using CP2K with the HSE06 hybrid functional, relax the unit cells of all Li_xMS2 compositions (for each M and x) and BCC Li metal. Collect the final total energies and relaxed unit-cell volumes.
- Evidence: `/app/outputs/hse06_relax.log`

### Step 3: Extract formation energies
- Role: scored (load-bearing)
- Action: From the HSE06-relaxed structures, compute the total energy per formula unit for each Li_xMS2 composition and write to /app/outputs/formation_energies.csv.
- Output file: `/app/outputs/formation_energies.csv`
- Format: csv
- Contract: CSV with columns: material (e.g., LiCrS2), Li_content_x (float, 0.75, 0.5, 0.25, 0.0), formation_energy_eV_per_fu (float, total energy).
- Scoring: scored by hidden verifier

### Step 4: Extract relaxed volumes
- Role: scored
- Action: From the same HSE06-relaxed unit cells, record the volume of LiMS2 and MS2 (fully delithiated) and write to /app/outputs/relaxed_volumes.csv.
- Output file: `/app/outputs/relaxed_volumes.csv`
- Format: csv
- Contract: CSV with columns: material (e.g., LiCrS2), composition (LiMS2 or MS2), volume_ang3 (float).
- Scoring: scored by hidden verifier

### Step 5: Bulk NEB migration barriers
- Role: scored
- Action: For each LiMS2 (M=Cr,Mn,Fe,Co,Ni), build a 2×2×1 supercell with one Li vacancy, relax the endpoints with PBE (CP2K), then perform CI-NEB with PBE to obtain the minimum energy path. Save the total energy of each NEB image to /app/outputs/neb_energy_profiles.json.
- Output file: `/app/outputs/neb_energy_profiles.json`
- Format: json
- Contract: JSON object: keys are material names (LiCrS2, LiMnS2, LiFeS2, LiCoS2, LiNiS2); each value is an array of total energies (eV) for images 0 through N.
- Scoring: scored by hidden verifier

### Step 6: Build and relax LiCrS2/Li3PS4 interface
- Role: process
- Action: Construct the LiCrS2(112)/β-Li3PS4(010) interface supercell following the paper's procedure (Li- and Cr-terminated (112) surface matched with S-terminated LPS (010), lattice mismatch ≤ 6.45%). Relax the interface with PBE.
- Evidence: `/app/outputs/interface_relax.log`

### Step 7: Interface NEB migration barrier
- Role: scored
- Action: Using the relaxed interface, identify a Li diffusion path from LiCrS2 bulk to Li3PS4 bulk, and perform CI-NEB (PBE) to compute the energy profile. Write the image energies to /app/outputs/interface_neb_profile.json.
- Output file: `/app/outputs/interface_neb_profile.json`
- Format: json
- Contract: JSON array of total energies (eV) for each NEB image.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/formation_energies.csv`
- `/app/outputs/relaxed_volumes.csv`
- `/app/outputs/neb_energy_profiles.json`
- `/app/outputs/interface_neb_profile.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### formation_energies.csv
- path: `/app/outputs/formation_energies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Total energy per formula unit for each intermediate and end-point composition. Used to compute average intercalation voltages against a Li metal reference.
- schema:
  - `type`: table
  - `required_columns`: `material`, `Li_content_x`, `formation_energy_eV_per_fu`
  - `units`:
    - `formation_energy_eV_per_fu`: eV

### relaxed_volumes.csv
- path: `/app/outputs/relaxed_volumes.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Unit-cell volumes of LiMS2 and MS2 end members. Used to compute volume change percentages during full delithiation.
- schema:
  - `type`: table
  - `required_columns`: `material`, `composition`, `volume_ang3`
  - `units`:
    - `volume_ang3`: Å^3

### neb_energy_profiles.json
- path: `/app/outputs/neb_energy_profiles.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Energy profiles for Li vacancy migration in each LiMS2 material. Each array element is the total energy of an NEB image along the path.
- schema:
  - `type`: object
  - `required_keys`: `LiCrS2`, `LiMnS2`, `LiFeS2`, `LiCoS2`, `LiNiS2`
  - `value_schema`:
    - `type`: array
    - `items`:
      - `type`: float
      - `unit`: eV

### interface_neb_profile.json
- path: `/app/outputs/interface_neb_profile.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Energy profile for Li migration across the LiCrS2(112)/Li3PS4(010) interface. Each element is the total energy of an NEB image.
- schema:
  - `type`: array
  - `items`:
    - `type`: float
    - `unit`: eV

Notes: The checker recomputes migration barriers, voltages, volume changes, and the interface barrier from these raw artifacts and compares them to paper-reported values using hidden tolerances. No gold values or tolerances are disclosed here.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "formation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "Li_content_x",
          "formation_energy_eV_per_fu"
        ],
        "units": {
          "formation_energy_eV_per_fu": "eV"
        }
      },
      "description": "Total energy per formula unit for each intermediate and end-point composition. Used to compute average intercalation voltages against a Li metal reference."
    },
    {
      "file": "relaxed_volumes.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "composition",
          "volume_ang3"
        ],
        "units": {
          "volume_ang3": "Å^3"
        }
      },
      "description": "Unit-cell volumes of LiMS2 and MS2 end members. Used to compute volume change percentages during full delithiation."
    },
    {
      "file": "neb_energy_profiles.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required_keys": [
          "LiCrS2",
          "LiMnS2",
          "LiFeS2",
          "LiCoS2",
          "LiNiS2"
        ],
        "value_schema": {
          "type": "array",
          "items": {
            "type": "float",
            "unit": "eV"
          }
        }
      },
      "description": "Energy profiles for Li vacancy migration in each LiMS2 material. Each array element is the total energy of an NEB image along the path."
    },
    {
      "file": "interface_neb_profile.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "float",
          "unit": "eV"
        }
      },
      "description": "Energy profile for Li migration across the LiCrS2(112)/Li3PS4(010) interface. Each element is the total energy of an NEB image."
    }
  ],
  "notes": "The checker recomputes migration barriers, voltages, volume changes, and the interface barrier from these raw artifacts and compares them to paper-reported values using hidden tolerances. No gold values or tolerances are disclosed here."
}
```

## How you are scored
A hidden verifier will independently read your output artifacts and recompute the headline quantities (bulk Li migration barriers, average intercalation voltages, volume changes, and the interface diffusion barrier) from your raw data. For each scored artifact, the verifier compares the recomputed values to hidden reference values (the paper’s reported results) using hidden tolerances that account for legitimate differences between DFT codes and functionals. The overall reward is a weighted sum of the scores for formation_energies.csv, relaxed_volumes.csv, neb_energy_profiles.json, and interface_neb_profile.json, with the largest weight assigned to the bulk NEB profiles and the interface NEB profile. Simply printing numbers that match the paper’s tables without producing the raw intermediate data will earn no credit, because the verifier recomputes from your raw outputs, not from any self-reported summary. Each output file must exist and conform to the specified schema; missing or malformed files are penalized.

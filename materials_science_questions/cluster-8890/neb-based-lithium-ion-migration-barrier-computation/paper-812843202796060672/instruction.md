# Dipole Switching and Lithium Migration in Janus MoSSe

## Problem background
Janus MoSSe is a two-dimensional polarized material with an intrinsic out-of-plane dipole moment arising from its asymmetric S–Mo–Se layer structure. Single-layer (SLM) and bilayer (DLM) MoSSe have been proposed as anode materials for lithium-ion batteries, promising high capacity and favorable ion transport. The key mechanistic hypothesis is that the intrinsic dipole creates an internal electric field that initially directs Li-ion adsorption to one side, while charge redistribution upon lithiation alters the dipole and may reverse the adsorption preference, enabling alternating layer-selective Li storage. This reproduction targets the quantitative evidence for this hypothesis: (i) the energy barriers for Li-ion and Li-vacancy migration on different layers of SLM and DLM, and (ii) the evolution and sign of the dipole moment as a function of Li concentration.

## Approach
The reproduction relies on first-principles density functional theory (DFT) calculations using the Perdew–Burke–Ernzerhof generalized-gradient approximation (GGA-PBE) with Grimme D3 dispersion correction. All calculations are performed with the open-source Quantum ESPRESSO package (pw.x and neb.x) using standard SSSP pseudopotentials. The workflow proceeds as follows: 3×3×1 supercells of SLM and DLM are built and relaxed. Lithiated structures are constructed at selected Li concentrations (x = 1, 2 for SLM and DLM) and relaxed; the electronic dipole moment (Debye) is then computed for each configuration including the pristine cases (x=0). For the migration barriers, low-concentration Li-ion migration (one Li per supercell) and high-concentration Li-vacancy migration (17 Li on SLM, 26 Li on DLM) are investigated on the S layer, Se layer, and (for DLM) the interlayer space. Minimum energy paths are obtained via the climbing-image nudged elastic band (CI‑NEB) method, and the corresponding energy barriers (eV) are extracted.

## Reproduction target
Produce two result files under /app/outputs:
1. dipole_evidence.json – containing the computed dipole moments (Debye) for SLM at Li concentrations x=0, 1, 2 and for DLM at x=0, 1, 2.
2. migration_barriers.json – containing the computed energy barriers (eV) for the ten specified Li-ion and Li-vacancy migration paths on SLM and DLM (path identifiers as defined in the output contract).
Your computed values must stem from the DFT+NEB workflow described above, not from values circulated in the literature.

## Assets

- Quantum ESPRESSO: quantum-espresso
- SSSP pseudopotential library (PBE efficiency): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Build initial supercells
- Role: process
- Action: Construct 3×3×1 supercells of single-layer MoSSe (SLM) and bilayer MoSSe (DLM, SMoSe/SMoSe stacking) using the lattice constant of 3.26 Å and known internal coordinates (Mo-S 2.42 Å, Mo-Se 2.54 Å). Write the input files for Quantum ESPRESSO geometry optimization.
- Evidence: `/app/outputs/step_01_supercells.log`

### Step 2: Relax pristine SLM and DLM
- Role: process
- Action: Perform DFT geometry optimization of the pristine SLM and DLM supercells using PBE functional with Grimme D3 dispersion correction and the SSSP pseudopotentials. Save the relaxed structures for later use.
- Evidence: `/app/outputs/step_02_relaxed_pristine.log`

### Step 3: Dipole moment analysis
- Role: scored (load-bearing)
- Action: Build lithiated configurations for SLM (x=1,2) and DLM (x=1,2) starting from the pristine relaxed structures, perform DFT geometry optimization of each, and compute the electronic dipole moment (Debye) for each concentration including pristine (x=0). Record the results in dipole_evidence.json.
- Output file: `/app/outputs/dipole_evidence.json`
- Format: json
- Contract: {
  "dipole_moments": {
    "SLM": {"x=0": <number>, "x=1": <number>, "x=2": <number>},
    "DLM": {"x=0": <number>, "x=1": <number>, "x=2": <number>}
  }
} (units Debye, values replace <number>)
- Scoring: scored by hidden verifier

### Step 4: Prepare NEB end-points
- Role: process
- Action: Build and relax the high-concentration lithiated host structures needed for Li-vacancy NEB: 17 Li atoms on the 3×3 SLM supercell and 26 Li atoms on the 3×3 DLM supercell, using the site preferences reported (e.g., filling S-side T_Mo sites first, then Se-side, etc.). Using all relaxed structures (pristine, low-concentration Li, high-concentration Li), construct the initial and final configurations for the ten migration paths: Li-ion on S/Se layer of SLM, Li-vacancy on S/Se layer of SLM; Li-ion on S/interlayer/Se of DLM, Li-vacancy on S/interlayer/Se of DLM. For each path, set up CI‑NEB calculations with 5–7 images along the migration route.
- Evidence: `/app/outputs/step_04_neb_endpoints.log`

### Step 5: NEB migration barriers
- Role: scored (load-bearing)
- Action: For each of the ten migration paths, run a Climbing‑Image Nudged Elastic Band (CI‑NEB) calculation using Quantum ESPRESSO neb.x with the previously prepared endpoints and images. Extract the energy barrier (eV) from the converged minimum energy path. Write all ten barrier values to migration_barriers.json.
- Output file: `/app/outputs/migration_barriers.json`
- Format: json
- Contract: {
  "barriers": {
    "slm_Li_ion_S_layer": <number>,
    "slm_Li_ion_Se_layer": <number>,
    "slm_Li_vacancy_S_layer": <number>,
    "slm_Li_vacancy_Se_layer": <number>,
    "dlm_Li_ion_S_layer": <number>,
    "dlm_Li_ion_middle_layer": <number>,
    "dlm_Li_ion_Se_layer": <number>,
    "dlm_Li_vacancy_S_layer": <number>,
    "dlm_Li_vacancy_middle_layer": <number>,
    "dlm_Li_vacancy_Se_layer": <number>
  }
} (units eV, values replace <number>)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dipole_evidence.json`
- `/app/outputs/migration_barriers.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dipole_evidence.json
- path: `/app/outputs/dipole_evidence.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Dipole moments (Debye) for pristine and lithiated SLM and DLM at specified Li concentrations, demonstrating sign reversal.
- schema:
  - `type`: object
  - `properties`:
    - `dipole_moments`:
      - `type`: object
      - `properties`:
        - `SLM`:
          - `type`: object
          - `properties`:
            - `x=0`:
              - `type`: number
              - `units`: Debye
            - `x=1`:
              - `type`: number
              - `units`: Debye
            - `x=2`:
              - `type`: number
              - `units`: Debye
          - `required`: `x=0`, `x=1`, `x=2`
        - `DLM`:
          - `type`: object
          - `properties`:
            - `x=0`:
              - `type`: number
              - `units`: Debye
            - `x=1`:
              - `type`: number
              - `units`: Debye
            - `x=2`:
              - `type`: number
              - `units`: Debye
          - `required`: `x=0`, `x=1`, `x=2`
      - `required`: `SLM`, `DLM`
  - `required`: `dipole_moments`

### migration_barriers.json
- path: `/app/outputs/migration_barriers.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Li-ion and Li-vacancy migration energy barriers (eV) for all ten pathways on SLM and DLM.
- schema:
  - `type`: object
  - `properties`:
    - `barriers`:
      - `type`: object
      - `properties`:
        - `slm_Li_ion_S_layer`:
          - `type`: number
          - `units`: eV
        - `slm_Li_ion_Se_layer`:
          - `type`: number
          - `units`: eV
        - `slm_Li_vacancy_S_layer`:
          - `type`: number
          - `units`: eV
        - `slm_Li_vacancy_Se_layer`:
          - `type`: number
          - `units`: eV
        - `dlm_Li_ion_S_layer`:
          - `type`: number
          - `units`: eV
        - `dlm_Li_ion_middle_layer`:
          - `type`: number
          - `units`: eV
        - `dlm_Li_ion_Se_layer`:
          - `type`: number
          - `units`: eV
        - `dlm_Li_vacancy_S_layer`:
          - `type`: number
          - `units`: eV
        - `dlm_Li_vacancy_middle_layer`:
          - `type`: number
          - `units`: eV
        - `dlm_Li_vacancy_Se_layer`:
          - `type`: number
          - `units`: eV
      - `required`: `slm_Li_ion_S_layer`, `slm_Li_ion_Se_layer`, `slm_Li_vacancy_S_layer`, `slm_Li_vacancy_Se_layer`, `dlm_Li_ion_S_layer`, `dlm_Li_ion_middle_layer`, `dlm_Li_ion_Se_layer`, `dlm_Li_vacancy_S_layer`, `dlm_Li_vacancy_middle_layer`, `dlm_Li_vacancy_Se_layer`
  - `required`: `barriers`

Notes: All barrier values are compared to the paper’s reported NEB results within a tolerance that accounts for DFT code differences. Dipole moments are checked for correct sign pattern and agreement within tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dipole_evidence.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "properties": {
          "dipole_moments": {
            "type": "object",
            "properties": {
              "SLM": {
                "type": "object",
                "properties": {
                  "x=0": {
                    "type": "number",
                    "units": "Debye"
                  },
                  "x=1": {
                    "type": "number",
                    "units": "Debye"
                  },
                  "x=2": {
                    "type": "number",
                    "units": "Debye"
                  }
                },
                "required": [
                  "x=0",
                  "x=1",
                  "x=2"
                ]
              },
              "DLM": {
                "type": "object",
                "properties": {
                  "x=0": {
                    "type": "number",
                    "units": "Debye"
                  },
                  "x=1": {
                    "type": "number",
                    "units": "Debye"
                  },
                  "x=2": {
                    "type": "number",
                    "units": "Debye"
                  }
                },
                "required": [
                  "x=0",
                  "x=1",
                  "x=2"
                ]
              }
            },
            "required": [
              "SLM",
              "DLM"
            ]
          }
        },
        "required": [
          "dipole_moments"
        ]
      },
      "description": "Dipole moments (Debye) for pristine and lithiated SLM and DLM at specified Li concentrations, demonstrating sign reversal."
    },
    {
      "file": "migration_barriers.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "properties": {
          "barriers": {
            "type": "object",
            "properties": {
              "slm_Li_ion_S_layer": {
                "type": "number",
                "units": "eV"
              },
              "slm_Li_ion_Se_layer": {
                "type": "number",
                "units": "eV"
              },
              "slm_Li_vacancy_S_layer": {
                "type": "number",
                "units": "eV"
              },
              "slm_Li_vacancy_Se_layer": {
                "type": "number",
                "units": "eV"
              },
              "dlm_Li_ion_S_layer": {
                "type": "number",
                "units": "eV"
              },
              "dlm_Li_ion_middle_layer": {
                "type": "number",
                "units": "eV"
              },
              "dlm_Li_ion_Se_layer": {
                "type": "number",
                "units": "eV"
              },
              "dlm_Li_vacancy_S_layer": {
                "type": "number",
                "units": "eV"
              },
              "dlm_Li_vacancy_middle_layer": {
                "type": "number",
                "units": "eV"
              },
              "dlm_Li_vacancy_Se_layer": {
                "type": "number",
                "units": "eV"
              }
            },
            "required": [
              "slm_Li_ion_S_layer",
              "slm_Li_ion_Se_layer",
              "slm_Li_vacancy_S_layer",
              "slm_Li_vacancy_Se_layer",
              "dlm_Li_ion_S_layer",
              "dlm_Li_ion_middle_layer",
              "dlm_Li_ion_Se_layer",
              "dlm_Li_vacancy_S_layer",
              "dlm_Li_vacancy_middle_layer",
              "dlm_Li_vacancy_Se_layer"
            ]
          }
        },
        "required": [
          "barriers"
        ]
      },
      "description": "Li-ion and Li-vacancy migration energy barriers (eV) for all ten pathways on SLM and DLM."
    }
  ],
  "notes": "All barrier values are compared to the paper’s reported NEB results within a tolerance that accounts for DFT code differences. Dipole moments are checked for correct sign pattern and agreement within tolerance."
}
```

## How you are scored
A hidden verifier independently scores each of the two output files. For dipole_evidence.json, the sign and magnitude of each dipole moment are compared to the paper’s reported values, with tolerance for systematic shifts between DFT codes. For migration_barriers.json, each barrier is compared to the corresponding paper-reported value within a tolerance that accounts for legitimate differences between VASP and Quantum ESPRESSO. The two artifacts are weighted, with the migration barriers contributing a larger share of the final reward. You must execute the full DFT+NEB pipeline to obtain physically meaningful numbers; reporting the paper’s published values without running the computation will not pass.

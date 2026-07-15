# Lithium Intercalation Properties and Migration Barrier of Nb2O2F3

## Problem background
Niobium oxyfluoride Nb2O2F3 has a layered crystal structure that can accommodate lithium ions, making it a candidate anode material for Li-ion batteries. Before this study, its lithium intercalation properties were unexplored. The goal is to determine the maximum amount of lithium that can be inserted per formula unit, the corresponding deintercalation voltage profile, the structural changes upon lithiation (volume expansion, interlayer distances), the electronic band gap of the fully lithiated phase, and the activation energy for lithium-ion migration through the material. These quantities are computed using density functional theory (DFT) and the climbing nudged elastic band (cNEB) method.

## Approach
The approach is a computational workflow using DFT with a plane-wave code such as Quantum ESPRESSO. The crystal structure of Nb2O2F3 is obtained from the published synthesis data and used to build a supercell. Lithium atoms are inserted at octahedral sites between the layers at several concentrations between 0 and 1 Li per formula unit. For each composition, the geometry is relaxed (cell shape and ionic positions) to obtain the total energy. The deintercalation voltage profile is then derived from the total energies using the Nernst equation, which compares the energy of the lithiated phases to the host and to metallic lithium. The structural analysis extracts the unit cell volumes, interlayer distances, and the band gap of the fully lithiated compound from the relaxed structures. Lithium migration is studied with the cNEB method: the activation energy is computed for the in-plane hopping pathway (Pathway 01) between adjacent Li equilibrium sites in a larger supercell of the fully lithiated material.

## Reproduction target
Compute the deintercalation voltage profile for LixNb2O2F3 as x varies from 0 to 1, and report the voltage at each concentration step in a CSV file. Extract the volume expansion percentage, the electronic band gap of LiNb2O2F3, and the interlayer distances of the delithiated and lithiated structures, reporting these in a JSON file. Determine the Li-ion migration activation energy along Pathway 01 (in-plane hopping) using cNEB and report it in a JSON file. All output files must follow the exact formats specified in the workflow steps.

## Assets

- Crystal structure of Nb2O2F3 (monoclinic I2/a): https://doi.org/10.1021/ja511203e
- Quantum ESPRESSO (or equivalent open-source DFT code): https://www.quantum-espresso.org/
- Atomic Simulation Environment (ASE) or similar: https://wiki.fysik.dtu.dk/ase/
- Standard pseudopotential library (SSSP or PSLibrary): https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: DFT ground-state calculations for intercalation energies
- Role: process
- Action: Build a 2x2x1 supercell of Nb2O2F3, place Li atoms at octahedral sites between layers for concentrations x = 0, 0.25, 0.5, 0.75, 1, and perform full DFT relaxations for each structure (allowing cell shape and ionic positions to relax). Also compute the total energy of bcc lithium metal. Use a suitable exchange-correlation functional (PBE or HSE06) and convergence criteria. Save the total energies per formula unit.
- Evidence: `/app/outputs/total_energies.json`

### Step 2: Compute intercalation voltage profile
- Role: scored
- Action: Using total_energies.json, compute the deintercalation voltage V(x) for each Li concentration step using the Nernst equation V = -[E(LixNb2O2F3) - (x-x0)E(Li) - E(Lix0Nb2O2F3)]/(x-x0), with x0=0. Write a CSV with columns x (lithium fraction) and V (volts vs Li/Li+).
- Output file: `/app/outputs/voltage_profile.csv`
- Format: csv
- Contract: columns: x (float, lithium fraction), V (float, volts)
- Scoring: scored by hidden verifier

### Step 3: Extract structural and electronic properties from DFT
- Role: process
- Action: From the relaxed structures of Nb2O2F3 (x=0) and LiNb2O2F3 (x=1), extract lattice parameters, the interlayer distance (distance between Nb2X10 layers), and the electronic band gap of LiNb2O2F3. Write these raw values to a JSON file.
- Evidence: `/app/outputs/structural_raw.json`

### Step 4: Report structural and electronic properties
- Role: scored
- Action: Compute the volume expansion percentage using unit cell volumes of the delithiated and fully lithiated phases. Extract the band gap of LiNb2O2F3 and the interlayer distances. Output a JSON file with keys: volume_expansion_percent, band_gap_LiNb2O2F3_eV, interlayer_distance_delithiated_A, interlayer_distance_lithiated_A.
- Output file: `/app/outputs/structural_properties.json`
- Format: json
- Contract: {"volume_expansion_percent": float, "band_gap_LiNb2O2F3_eV": float, "interlayer_distance_delithiated_A": float, "interlayer_distance_lithiated_A": float}
- Scoring: scored by hidden verifier

### Step 5: cNEB calculation for Li migration barrier
- Role: process
- Action: Build a 2x2x2 supercell of fully lithiated LiNb2O2F3. Identify two adjacent Li equilibrium sites that define Pathway 01 (in-plane hopping). Set up a climbing-image NEB calculation with 6 intermediate images. Run the NEB until convergence and extract the activation energy (maximum energy along the path relative to the endpoints). Write the result to a JSON file.
- Evidence: `/app/outputs/neb_result.json`

### Step 6: Report Li migration activation energy
- Role: scored (load-bearing)
- Action: Output the activation energy for Pathway 01 as a JSON file with keys activation_energy_eV (float) and pathway (string '01').
- Output file: `/app/outputs/migration_barrier.json`
- Format: json
- Contract: {"activation_energy_eV": float, "pathway": "01"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/voltage_profile.csv`
- `/app/outputs/structural_properties.json`
- `/app/outputs/migration_barrier.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### voltage_profile.csv
- path: `/app/outputs/voltage_profile.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Voltage profile of LixNb2O2F3 deintercalation; the checker re-derives the average voltage and verifies monotonic trend.
- schema:
  - `type`: table
  - `required_columns`: `x`, `V`
  - `units`:
    - `x`: Li fraction (dimensionless)
    - `V`: Volts vs Li/Li+

### structural_properties.json
- path: `/app/outputs/structural_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Volume expansion, band gap, and interlayer distances upon lithiation.
- schema:
  - `type`: object
  - `required`:
    - `volume_expansion_percent`: float
    - `band_gap_LiNb2O2F3_eV`: float
    - `interlayer_distance_delithiated_A`: float
    - `interlayer_distance_lithiated_A`: float

### migration_barrier.json
- path: `/app/outputs/migration_barrier.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Li-ion migration barrier for Pathway 01.
- schema:
  - `type`: object
  - `required`:
    - `activation_energy_eV`: float
    - `pathway`: string

Notes: The hidden checker uses paper-reported values for the deintercalation average voltage, volume expansion, band gap, and migration barrier as reference. Tolerances are set to accommodate toolchain differences.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "voltage_profile.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "V"
        ],
        "units": {
          "x": "Li fraction (dimensionless)",
          "V": "Volts vs Li/Li+"
        }
      },
      "description": "Voltage profile of LixNb2O2F3 deintercalation; the checker re-derives the average voltage and verifies monotonic trend."
    },
    {
      "file": "structural_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "volume_expansion_percent": "float",
          "band_gap_LiNb2O2F3_eV": "float",
          "interlayer_distance_delithiated_A": "float",
          "interlayer_distance_lithiated_A": "float"
        }
      },
      "description": "Volume expansion, band gap, and interlayer distances upon lithiation."
    },
    {
      "file": "migration_barrier.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "activation_energy_eV": "float",
          "pathway": "string"
        }
      },
      "description": "Li-ion migration barrier for Pathway 01."
    }
  ],
  "notes": "The hidden checker uses paper-reported values for the deintercalation average voltage, volume expansion, band gap, and migration barrier as reference. Tolerances are set to accommodate toolchain differences."
}
```

## How you are scored
A hidden verifier checks each scored artifact you submit. For the voltage profile, the verifier re-derives the average deintercalation voltage from the CSV file and verifies that the voltage decreases monotonically with increasing lithium content. For the structural properties and the migration barrier, the verifier compares your reported values to hidden reference values derived from the study. Each artifact contributes a weighted share to a final reward between 0 and 1; the migration barrier is the primary load-bearing artifact and carries the largest weight. Simply printing a number without executing the required computations will not pass the verification.

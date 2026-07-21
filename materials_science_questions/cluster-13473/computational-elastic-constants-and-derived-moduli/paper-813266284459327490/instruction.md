# MD Simulation of GO Paper Young's Modulus and Intersheet Interactions

## Problem background
Graphene oxide (GO) papers are layered assemblies of monolayer GO sheets whose mechanical properties depend on the lateral size of the constituent sheets. It is known that papers made from larger GO sheets are stiffer than those made from small sheets, but the atomic‑scale mechanisms remain an open question. One hypothesis is that tensile deformation is dominated by shear between adjacent sheets (intersheet sliding) rather than by stretching of the individual sheets, and that the intersheet interactions responsible for this shear resistance change with sheet length. Molecular dynamics simulations can probe these mechanisms by computing the Young’s modulus, decomposing the deformation components, and quantifying the edge‑to‑edge and face‑to‑face non‑bonded interaction energies as functions of GO sheet length. This task uses atomistic simulations to investigate those relationships and to quantify how they depend on the presence of intercalated water.

## Approach
The central idea is to construct two‑sheet GO paper models at five different sheet lengths, both dry and with 16 wt% intercalated water, and to simulate their tensile response using a classical force field that can describe bond breaking and hydrogen bonding (e.g., ReaxFF). From the resulting energy–strain data, the Young’s modulus is extracted by fitting the curvature of the potential energy vs. strain. The same trajectories are analysed to separate the total tensile elongation into (i) intrinsic stretching of the GO sheets and (ii) relative displacement between the sheets (intersheet shear). In addition, the non‑bonded interaction energies between sheets that lie in the same horizontal plane (edge‑to‑edge) and in adjacent planes (face‑to‑face) are computed. By comparing the results across the five lengths and the two moisture conditions, the approach reveals how sheet size influences the modulus, the dominant deformation mode, and the relative importance of face‑to‑face versus edge‑to‑edge interactions.

## Reproduction target
Produce the following three CSV artifacts for GO paper models with sheet lengths approximately 1.1, 2.2, 3.3, 4.4, and 5.4 nm, in dry and wet (16 wt% water) states:

1.  `youngs_modulus_vs_length.csv` – the Young’s modulus (GPa) for each length and moisture condition, obtained from the energy–strain curvature.
2.  `deformation_components.csv` – the percentage of total deformation contributed by intersheet shear and by GO‑sheet elongation for each length.
3.  `interaction_energies.csv` – the face‑to‑face and edge‑to‑edge non‑bonded interaction energies as a function of GO length.

## Assets

- LAMMPS Molecular Dynamics Simulator: https://lammps.sandia.gov
- ReaxFF force field parameters for C/H/O systems (publicly available, e.g., the original hydrocarbon parameterization by van Duin et al.)

## Workflow steps

### Step 1: Build two‑sheet GO paper models
- Role: process
- Action: Construct atomistic models for five GO sheet lengths (approximately 1.1, 2.2, 3.3, 4.4, 5.4 nm) with functional groups according to the Lerf–Klinowski model: three epoxy and one hydroxyl group per 12 basal carbon atoms on both sides, five carboxyl groups per edge, C/O ratios in range 2.17–2.68. Include periodic boundaries in y and z, a 100 Å vacuum slab in x, and 16 wt% intercalated water for wet models. Generate both dry and wet initial configurations.
- Evidence: (no output file required; models are built in memory or as LAMMPS data files)

### Step 2: Run MD simulations and collect energy–strain data
- Role: process
- Action: Using LAMMPS with ReaxFF force field, perform energy minimization and NVT dynamics (1 fs timestep, 1 K, 9.5 Å cutoff) for each model at a series of applied axial strains (fix right‑edge atoms, displace left‑edge atoms). Record potential energy at each strain and save trajectory snapshots for deformation and interaction analyses.
- Evidence: (no output file required; energy–strain data are processed in memory)

### Step 3: Extract Young's modulus from energy–strain fits
- Role: scored (load-bearing)
- Action: Fit potential energy vs strain data for each model using \(E = \frac{1}{V} \frac{d^2U}{d\epsilon^2}\), where \(V\) is the volume of the simulation box at zero strain (the total initial volume of the periodic cell, computed from the box dimensions \(L_x \times L_y \times L_z\) in the unstrained state). Compile Young's moduli as a function of GO length for dry and wet conditions.
- Output file: `/app/outputs/youngs_modulus_vs_length.csv`
- Format: csv
- Contract: columns: `GO_length_nm`, `modulus_dry_GPa`, `modulus_wet_GPa`; one row per model length
- Scoring: scored by hidden verifier

### Step 4: Decompose tensile deformation into intersheet and GO‑sheet contributions
- Role: scored (load-bearing)
- Action: Analyse MD trajectories to separate total tensile deformation into intrinsic GO‑sheet elongation and intersheet relative displacement; report percentage contribution of each component for each GO length. The two percentages must sum to 100 (within a tolerance of ±0.5).
- Output file: `/app/outputs/deformation_components.csv`
- Format: csv
- Contract: columns: `GO_length_nm`, `intersheet_deformation_percent`, `sheet_deformation_percent`; ensure `intersheet_deformation_percent + sheet_deformation_percent ≈ 100.0` for each row
- Scoring: scored by hidden verifier

### Step 5: Calculate face‑to‑face and edge‑to‑edge interaction energies
- Role: scored (load-bearing)
- Action: From equilibrated configurations, compute non‑bonded interaction energies between adjacent GO sheets in the same horizontal plane (edge‑to‑edge) and in different planes (face‑to‑face) as a function of GO length. Energies are reported in kcal/mol, consistent with the typical ReaxFF output.
- Output file: `/app/outputs/interaction_energies.csv`
- Format: csv
- Contract: columns: `GO_length_nm`, `face_to_face_energy`, `edge_to_edge_energy`
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/youngs_modulus_vs_length.csv`
- `/app/outputs/deformation_components.csv`
- `/app/outputs/interaction_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### youngs_modulus_vs_length.csv
- path: `/app/outputs/youngs_modulus_vs_length.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Young's modulus for each GO length and moisture state. Scored by hidden verifier.
- schema:
  - `type`: table
  - `required_columns`: `GO_length_nm`, `modulus_dry_GPa`, `modulus_wet_GPa`

### deformation_components.csv
- path: `/app/outputs/deformation_components.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Deformation breakdown per GO length. Scored by hidden verifier.
- schema:
  - `type`: table
  - `required_columns`: `GO_length_nm`, `intersheet_deformation_percent`, `sheet_deformation_percent`

### interaction_energies.csv
- path: `/app/outputs/interaction_energies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Face‑to‑face and edge‑to‑edge interaction energies in kcal/mol per GO length. Scored by hidden verifier.
- schema:
  - `type`: table
  - `required_columns`: `GO_length_nm`, `face_to_face_energy`, `edge_to_edge_energy`

Notes: All scored outputs are structural; the checker validates qualitative consistency rather than absolute numeric equality with the paper.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "youngs_modulus_vs_length.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "GO_length_nm",
          "modulus_dry_GPa",
          "modulus_wet_GPa"
        ]
      },
      "description": "Young's modulus for each GO length and moisture state. Scored by hidden verifier."
    },
    {
      "file": "deformation_components.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "GO_length_nm",
          "intersheet_deformation_percent",
          "sheet_deformation_percent"
        ]
      },
      "description": "Deformation breakdown per GO length. Scored by hidden verifier."
    },
    {
      "file": "interaction_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "GO_length_nm",
          "face_to_face_energy",
          "edge_to_edge_energy"
        ]
      },
      "description": "Face‑to‑face and edge‑to‑edge interaction energies in kcal/mol per GO length. Scored by hidden verifier."
    }
  ],
  "notes": "All scored outputs are structural; the checker validates qualitative consistency rather than absolute numeric equality with the paper."
}
```

## How you are scored
The hidden verifier reads your three scored CSV files and checks their structural consistency against the physical trends expected from the simulation setup. Specific checks are not disclosed; you must rely on the simulation to produce plausible results. Each scored artifact carries a weight, and the final reward is a weighted sum in the range [0, 1]. Simply reporting numbers is not sufficient; the verifier expects coherent, physically plausible results obtained by actually running the molecular dynamics workflow described in the steps.
# DFT Investigation of Al13H Cluster Dimerization and Solid Assembly

## Problem background
Self-assembling atomic nanostructures into cluster materials holds promise for novel solids, but metallic clusters often coalesce. A cluster's intrinsic stability, often linked to closed electronic shells and large HOMO-LUMO gaps, is not alone sufficient; additional conditions like optimal cluster orientation and passivation matter. This task investigates hydrogen-doped icosahedral aluminum clusters (Al13H) as building blocks. The goal is to compute, via density functional theory (DFT), key energetic and structural properties that indicate a cluster's readiness to assemble while retaining its identity.

## Approach
The workflow follows a DFT-based computational protocol. Starting from an isolated Al13H monomer, optimize its geometry and compute electronic properties (total energy, HOMO/LUMO levels, hydrogen binding energy). From the optimized monomer, construct two dimer isomers with different relative orientations: one with parallel icosahedral faces in contact, the other with perpendicular edges in contact. For each dimer, perform a frozen-geometry energy scan versus center-to-center separation, fit to a Morse potential to estimate equilibrium separations, then fully relax atomic coordinates and compute the relaxed binding energy and equilibrium separation. Finally, assemble the clusters into a simple cubic lattice with perpendicular-edge contacts, scan the lattice constant for optimal energy, compute the binding energy per cluster, and verify structural integrity through constant-volume molecular dynamics at 150 K. All calculations rely on open-source DFT with LDA functionals and suitable pseudopotentials.

## Reproduction target
Produce three scored artifacts:
1. For the monomer: total energy, HOMO energy, LUMO energy, and H binding energy.
2. For each dimer isomer: the frozen-geometry equilibrium distance and well depth, the fully relaxed equilibrium separation and binding energy, and the Morse fit parameters.
3. For the assembled solid: the optimal lattice constant, binding energy per cluster, a boolean indicating whether the icosahedral units remained intact after MD, and the maximum atomic displacement observed during that run.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- LDA pseudopotentials (Al, H): https://www.materialscloud.org/discover/sssp/table/precision

## Workflow steps

### Step 1: DFT optimization and electronic property calculation of Al13H monomer
- Role: scored
- Action: Using DFT (e.g., Quantum ESPRESSO with LDA), optimize the geometry of an isolated Al13H cluster (icosahedral Al13 with H on a triangular face), compute total energy, HOMO/LUMO energies, and H binding energy (E(Al13H) - E(Al13) - E(H)).
- Output file: `/app/outputs/step_01_monomer_results.json`
- Format: json
- Contract: {"total_energy_ev":<float>,"homo_energy_ev":<float>,"lumo_energy_ev":<float>,"h_binding_energy_ev":<float>,"h_correction_used":"H atom energy computed separately as E(H)=..."}
- Scoring: scored by hidden verifier

### Step 2: Construct initial (Al13H)2 dimer isomers A and B
- Role: process
- Action: Using the optimized monomer geometry, construct two dimer structures: isomer A with icosahedra having parallel faces in contact along a common C3v axis; isomer B with the two icosahedra contacting via perpendicular edges.
- Evidence: none

### Step 3: Frozen-geometry interaction energy scan and Morse potential fit for dimers
- Role: process
- Action: For each dimer isomer, perform DFT single-point energy calculations at a range of center-to-center separations while keeping monomer internal coordinates frozen. Fit the interaction energy versus separation curve to a Morse potential to obtain approximate equilibrium separations.
- Evidence: none

### Step 4: Relaxation of (Al13H)2 dimers and computation of binding energies
- Role: scored (load-bearing)
- Action: Starting from the Morse-fit estimated equilibrium separations, perform full conjugate-gradient relaxation of all atomic coordinates for each dimer isomer. Compute the binding energy (E(dimer) - 2*E(monomer)) and equilibrium center-to-center separation.
- Output file: `/app/outputs/step_02_dimer_results.json`
- Format: json
- Contract: {"isomer_A":{"frozen_eq_dist_au":<float>,"frozen_well_depth_ev":<float>,"relaxed_eq_dist_au":<float>,"relaxed_binding_energy_ev":<float>},"isomer_B":{"frozen_eq_dist_au":<float>,"frozen_well_depth_ev":<float>,"relaxed_eq_dist_au":<float>,"relaxed_binding_energy_ev":<float>},"morse_fit_parameters":{} }
- Scoring: scored by hidden verifier

### Step 5: Assembly of Al13H clusters into simple cubic solid and MD stability test
- Role: scored
- Action: Construct a simple cubic lattice of Al13H clusters with perpendicular-edge contact orientation. Perform DFT energy versus lattice constant scan (frozen clusters) to find the optimal lattice constant and compute binding energy per cluster. Then run constant-volume constant-temperature MD at 150 K for 3 ps (5 fs timestep) and verify that the icosahedral units remain structurally intact.
- Output file: `/app/outputs/step_03_solid_results.json`
- Format: json
- Contract: {"lattice_constant_au":<float>,"binding_energy_per_cluster_ev":<float>,"clusters_preserved":<bool>,"max_atomic_displacement_au":<float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_monomer_results.json`
- `/app/outputs/step_02_dimer_results.json`
- `/app/outputs/step_03_solid_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_monomer_results.json
- path: `/app/outputs/step_01_monomer_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed electronic properties and H binding energy of the Al13H monomer. The H binding energy must be within tolerance of the paper's reported value.
- schema:
  - `type`: object
  - `required`:
    - `total_energy_ev`: float
    - `homo_energy_ev`: float
    - `lumo_energy_ev`: float
    - `h_binding_energy_ev`: float
    - `h_correction_used`: string

### step_02_dimer_results.json
- path: `/app/outputs/step_02_dimer_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Relaxed binding energies and equilibrium separations for dimer isomers A and B, plus frozen-geometry metrics and Morse fit parameters. The relaxed quantities must match paper values within tolerances.
- schema:
  - `type`: object
  - `required`:
    - `isomer_A`:
      - `frozen_eq_dist_au`: float
      - `frozen_well_depth_ev`: float
      - `relaxed_eq_dist_au`: float
      - `relaxed_binding_energy_ev`: float
    - `isomer_B`:
      - `frozen_eq_dist_au`: float
      - `frozen_well_depth_ev`: float
      - `relaxed_eq_dist_au`: float
      - `relaxed_binding_energy_ev`: float
    - `morse_fit_parameters`: object

### step_03_solid_results.json
- path: `/app/outputs/step_03_solid_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Lattice constant and binding energy per cluster of the assembled simple cubic solid, structural preservation flag, and maximum atomic displacement after MD. Energy and lattice constant must match paper values within tolerances; clusters_preserved must be true and displacement below a threshold.
- schema:
  - `type`: object
  - `required`:
    - `lattice_constant_au`: float
    - `binding_energy_per_cluster_ev`: float
    - `clusters_preserved`: bool
    - `max_atomic_displacement_au`: float

Notes: Tolerances are set to absorb differences due to DFT implementation and pseudopotentials. The expected values used for scoring are derived from the original publication but are not disclosed to encourage independent reproduction.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_monomer_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "total_energy_ev": "float",
          "homo_energy_ev": "float",
          "lumo_energy_ev": "float",
          "h_binding_energy_ev": "float",
          "h_correction_used": "string"
        }
      },
      "description": "Computed electronic properties and H binding energy of the Al13H monomer. The H binding energy must be within tolerance of the paper's reported value."
    },
    {
      "file": "step_02_dimer_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "isomer_A": {
            "frozen_eq_dist_au": "float",
            "frozen_well_depth_ev": "float",
            "relaxed_eq_dist_au": "float",
            "relaxed_binding_energy_ev": "float"
          },
          "isomer_B": {
            "frozen_eq_dist_au": "float",
            "frozen_well_depth_ev": "float",
            "relaxed_eq_dist_au": "float",
            "relaxed_binding_energy_ev": "float"
          },
          "morse_fit_parameters": {}
        }
      },
      "description": "Relaxed binding energies and equilibrium separations for dimer isomers A and B, plus frozen-geometry metrics and Morse fit parameters. The relaxed quantities must match paper values within tolerances."
    },
    {
      "file": "step_03_solid_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "lattice_constant_au": "float",
          "binding_energy_per_cluster_ev": "float",
          "clusters_preserved": "bool",
          "max_atomic_displacement_au": "float"
        }
      },
      "description": "Lattice constant and binding energy per cluster of the assembled simple cubic solid, structural preservation flag, and maximum atomic displacement after MD. Energy and lattice constant must match paper values within tolerances; clusters_preserved must be true and displacement below a threshold."
    }
  ],
  "notes": "Tolerances are set to absorb differences due to DFT implementation and pseudopotentials. The expected values used for scoring are derived from the original publication but are not disclosed to encourage independent reproduction."
}
```

## How you are scored
Each scored step is evaluated independently by a hidden verifier. The verifier recomputes derived quantities from your submitted raw numbers (e.g., H binding energy, dimer binding energies, HOMO-LUMO gap) and compares them to expected values using tolerances that account for legitimate differences in DFT codes and pseudopotentials. Scores are weighted by the importance of each step, with the dimer relaxation results carrying the highest weight. Your final reward is the combination; merely reporting numbers without genuine computation will not yield passing scores because the verifier can detect physically implausible values. The exact scoring logic and tolerances are hidden, but they reward faithful execution of the described computational pipeline.

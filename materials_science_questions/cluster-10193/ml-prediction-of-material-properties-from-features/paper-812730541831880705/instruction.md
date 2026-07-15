# High-Throughput DFT Screening of Single-Atom Catalysts for H₂O₂ Electroreduction

## Problem background
Electrochemical partial reduction of O₂ to hydrogen peroxide (H₂O₂) is a promising sustainable alternative to the energy-intensive anthraquinone process. However, conventional catalysts face a fundamental trade-off between activity and selectivity: strengthening OOH* binding to enhance activity also strengthens O* binding, which promotes the competing four-electron pathway to water. Single-atom catalysts (SACs) on two-dimensional substrates offer the possibility to break these scaling relations, because the isolated metal site can selectively stabilize OOH* while destabilizing O*, enabling simultaneous high activity and selectivity. This reproduction task investigates whether DFT-based screening of experimentally feasible SACs can identify candidates that achieve this balance, and what level of overpotential the best candidate can reach.

## Approach
The screening workflow proceeds via spin-polarized DFT with the PBE functional and dispersion corrections. The catalyst library consists of single metal atoms from groups 3–12 and selected main-group elements placed on seven publicly known 2D substrate families: defective graphene (C₃, C₄), N-doped graphene (g-N₄), boron nitride (N₃), and macrocyclic frameworks (phthalocyanine Pc-N₄, pyrphyrin Py-N₄, porphyrin Pr-N₄). Stability is assessed by computing formation energies and dissolution potentials from bulk references. For stable SACs, the O* free energy ΔG(O*) is evaluated within the computational hydrogen electrode model, using zero-point energy, entropy, solvation, and gas-phase error corrections. Selectivity towards H₂O₂ is judged by the thermodynamic criterion ΔG(O*) > 3.52 eV (the difference between the H₂O₂ and H₂O free energies). The most promising catalysts are further evaluated for activity by computing the full two-electron reduction free energy diagram and the limiting potential, with PtHg₄(110) as a benchmark. The goal is to execute this entire pipeline, not merely to report a final number.

## Reproduction target
Produce the four scored artifacts:

- A table of stability metrics (formation energy and dissolution potential) for all 210 SACs.
- A table of ΔG(O*) for every SAC that passes the stability criteria.
- A list of SACs that satisfy the selectivity criterion (ΔG(O*) > 3.52 eV).
- The overpotential (η = 0.70 V – UL) for the Zn@Pc-N₄ catalyst, computed from its full free energy diagram.

All artifacts must be written as CSV files under /app/outputs following the output contract. The task is to compute these quantities by re-running the DFT pipeline; the paper’s reported numbers are not provided and must not be assumed as input.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP PBE pseudopotentials: https://www.materialscloud.org/discover/sssp/table/precision
- DFT-D3 dispersion correction: https://www.chemie.uni-bonn.de/pctc/mulliken-center/software/dft-d3/
- Crystal structures of 2D substrates
- Bulk metal reference structures

## Workflow steps

### Step 1: Model construction
- Role: process
- Action: Construct the 210 SAC computational models by placing single metal atoms (from groups 3–12 and selected main-group elements) on the seven 2D substrate types (defective graphene C₃, C₄; N-doped graphene g-N₄; BN N₃; phthalocyanine Pc-N₄; pyrphyrin Py-N₄; porphyrin Pr-N₄). Use publicly available or constructed structural templates. Every SAC model must be uniquely identifiable with a SAC_id.
- Evidence: `/app/outputs/sac_models_summary.json`

### Step 2: DFT stability calculations
- Role: process
- Action: For each of the 210 SACs, the pristine substrates, and the bulk metal reference phases, perform spin-polarized DFT computations using an open-source plane-wave code (e.g., Quantum ESPRESSO) with the PBE functional, DFT-D3 dispersion correction, an energy cutoff of 400 eV, and appropriate k-point sampling. Extract total energies. Compute the formation energy Ef = E_M@SUB - E_SUB - E_M and the dissolution potential Udiss = Udiss°(bulk) - Ef/(n e) using standard dissolution potentials and the number of electrons n involved in dissolution.
- Evidence: `/app/outputs/stability_dft_energies.json`

### Step 3: Stability screening output
- Role: scored
- Action: Compile the computed formation energies (Ef) and dissolution potentials (Udiss) for each SAC. Determine stability as: Ef < 0 eV AND Udiss > 0 V. Write the results to step_01_stability_screening.csv with columns: SAC_id (string), metal (string), substrate (string), Ef (eV, float), Udiss (V, float), stable (boolean). Include all 210 SACs.
- Output file: `/app/outputs/step_01_stability_screening.csv`
- Format: csv
- Contract: Columns: SAC_id, metal, substrate, Ef, Udiss, stable.
- Scoring: scored by hidden verifier

### Step 4: DFT O* adsorption calculations
- Role: process
- Action: For each SAC that was classified as stable (stable=true in step_01), compute the Gibbs free energy of O* adsorption, ΔG(O*), using DFT within the computational hydrogen electrode (CHE) model. Include zero-point energy and entropy corrections from harmonic analysis, a solvation correction of ~0.3 eV, and the gas-phase error corrections for H₂, H₂O, and H₂O₂ as specified in the paper. Use the same DFT setup as in the stability calculations.
- Evidence: `/app/outputs/ostar_dft_results.json`

### Step 5: ΔG(O*) output
- Role: scored (load-bearing)
- Action: For each stable SAC, report the computed ΔG(O*) in eV. Write the results to step_02_DeltaG_Ostar.csv with columns: SAC_id (string), DeltaG_Ostar (float, eV).
- Output file: `/app/outputs/step_02_DeltaG_Ostar.csv`
- Format: csv
- Contract: Columns: SAC_id, DeltaG_Ostar.
- Scoring: scored by hidden verifier

### Step 6: Selectivity screening
- Role: scored
- Action: From the ΔG(O*) values in step_02_DeltaG_Ostar.csv, identify SACs with DeltaG_Ostar > 3.52 eV. Write their SAC_id to step_03_selective_SACs.csv, one per row with header 'SAC_id'.
- Output file: `/app/outputs/step_03_selective_SACs.csv`
- Format: csv
- Contract: Single column: SAC_id.
- Scoring: scored by hidden verifier

### Step 7: Reaction intermediate calculations for Zn@Pc-N4 and PtHg4
- Role: process
- Action: Construct the PtHg4(110) surface model and compute its free energy diagram for the two-electron O₂ reduction pathway to obtain the limiting potential UL. For the Zn@Pc-N4 SAC, calculate the adsorption free energies of O₂*, OOH*, and H₂O₂* along the reaction pathway (in addition to the already-computed O*). Use the same DFT methodology. Determine the potential-limiting step and compute UL = ΔG_PDS/e.
- Evidence: `/app/outputs/activity_intermediates.json`

### Step 8: Activity output for Zn@Pc-N4
- Role: scored
- Action: Compute the overpotential η = 0.70 V - UL for Zn@Pc-N4 (equilibrium potential for two-electron ORR is 0.70 V). Write the result to step_04_activity_ZnPcN4.csv with columns: SAC_id (string, value 'Zn@Pc-N4'), overpotential (float, V).
- Output file: `/app/outputs/step_04_activity_ZnPcN4.csv`
- Format: csv
- Contract: Columns: SAC_id, overpotential.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_stability_screening.csv`
- `/app/outputs/step_02_DeltaG_Ostar.csv`
- `/app/outputs/step_03_selective_SACs.csv`
- `/app/outputs/step_04_activity_ZnPcN4.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_stability_screening.csv
- path: `/app/outputs/step_01_stability_screening.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Stability metrics (formation energy, dissolution potential) and a stable flag for all 210 SACs.
- schema:
  - `type`: table
  - `required_columns`: `SAC_id`, `metal`, `substrate`, `Ef`, `Udiss`, `stable`
  - `units`:
    - `Ef`: eV
    - `Udiss`: V

### step_02_DeltaG_Ostar.csv
- path: `/app/outputs/step_02_DeltaG_Ostar.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: O* adsorption free energies for all stable SACs.
- schema:
  - `type`: table
  - `required_columns`: `SAC_id`, `DeltaG_Ostar`
  - `units`:
    - `DeltaG_Ostar`: eV

### step_03_selective_SACs.csv
- path: `/app/outputs/step_03_selective_SACs.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: List of SAC IDs that satisfy ΔG(O*) > 3.52 eV.
- schema:
  - `type`: table
  - `required_columns`: `SAC_id`

### step_04_activity_ZnPcN4.csv
- path: `/app/outputs/step_04_activity_ZnPcN4.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Overpotential for the Zn@Pc-N4 catalyst; must be ≤ 0.25 V.
- schema:
  - `type`: table
  - `required_columns`: `SAC_id`, `overpotential`
  - `units`:
    - `overpotential`: V

Notes: The checker compares the submitted Ef/Udiss values, the ΔG(O*) list, the selective SACs list, and the Zn@Pc‑N4 overpotential to paper-reported gold values with tolerances. The overpotential target follows a 'threshold_or_better' policy (lower is better).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_stability_screening.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "SAC_id",
          "metal",
          "substrate",
          "Ef",
          "Udiss",
          "stable"
        ],
        "units": {
          "Ef": "eV",
          "Udiss": "V"
        }
      },
      "description": "Stability metrics (formation energy, dissolution potential) and a stable flag for all 210 SACs."
    },
    {
      "file": "step_02_DeltaG_Ostar.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "SAC_id",
          "DeltaG_Ostar"
        ],
        "units": {
          "DeltaG_Ostar": "eV"
        }
      },
      "description": "O* adsorption free energies for all stable SACs."
    },
    {
      "file": "step_03_selective_SACs.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "SAC_id"
        ]
      },
      "description": "List of SAC IDs that satisfy ΔG(O*) > 3.52 eV."
    },
    {
      "file": "step_04_activity_ZnPcN4.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "SAC_id",
          "overpotential"
        ],
        "units": {
          "overpotential": "V"
        }
      },
      "description": "Overpotential for the Zn@Pc-N4 catalyst; must be ≤ 0.25 V."
    }
  ],
  "notes": "The checker compares the submitted Ef/Udiss values, the ΔG(O*) list, the selective SACs list, and the Zn@Pc‑N4 overpotential to paper-reported gold values with tolerances. The overpotential target follows a 'threshold_or_better' policy (lower is better)."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently checks each workflow stage’s artifact. The verifier compares your computed stability labels, ΔG(O*) values, selectivity list, and overpotential to reference values from the original study, using tolerances appropriate for DFT reproduction with a different code. Internal cross-artifact consistency is also checked (e.g., the selectivity list must be derivable from the ΔG(O*) table). Simply copying the published numbers without executing the computation will fail these checks. The final reward is a weighted sum of per-stage scores, with the largest weight given to the ΔG(O*) accuracy and the Zn@Pc-N₄ overpotential.

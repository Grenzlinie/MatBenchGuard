# Compute PF6‑Intercalated Graphite Properties: Intercalation Energies, Voltage, Capacity, Charge Transfer, and Diffusion Barrier via DFT

## Problem background
Dual-ion batteries (DIBs) are emerging alternatives to conventional Li-ion batteries, offering high voltage and low cost by reversibly intercalating anions into graphite cathodes. Understanding the mechanism of anion intercalation—including staging, energetics, structural expansion, electrochemical properties, charge transfer, and ion mobility—is essential for designing better DIBs. This task uses first-principles density functional theory (DFT) to investigate the intercalation of hexafluorophosphate (PF6−) into graphite, aiming to compute the key quantities that govern battery performance.

## Approach
The study models the intercalation of PF6− into graphite as a staging process, where anions occupy galleries between graphene layers at increasing concentrations. Graphite supercells are constructed for stages 1 through 4, each containing a different number of PF6− ions. First-principles DFT with a dispersion-corrected functional (e.g., PBE-D3) is used to optimize all atomic positions and lattice parameters of pristine graphite, the intercalated compounds, and isolated molecules (PF6, EMC, LiPF6(EMC)4). From the relaxed total energies, the intercalation energy per PF6− is calculated via E_inter = (E[GIC] − E[graphite] − x·E[PF6])/x. The interlayer distance is extracted from the relaxed cell. The open-circuit voltage is obtained from the Nernst equation using the total energies of the relevant species, and the specific capacity is derived from the maximum loading. Charge transfer is quantified via Bader analysis, and the minimum diffusion barrier for PF6− migration is determined using the climbing-image nudged elastic band method (CI-NEB) with seven images.

## Reproduction target
The goal is to produce four output files by executing the workflow steps described below:
1. **results_table.csv**: a CSV file with columns `stage`, `PF6_count`, `intercalation_energy_eV`, `interlayer_distance_Angstrom`. It must contain exactly 16 rows covering all stage–concentration combinations: stage‑1 with 4, 8, 12, 16 PF6; stage‑2 with 2, 4, 6, 8; stage‑3 with 2, 4, 6, 8; stage‑4 with 1, 2, 3, 4.
2. **voltage_capacity.txt**: a plain‑text file containing two lines: the cell voltage range (e.g., `Voltage range: X.XX‑Y.YY V`) and the maximum specific capacity (e.g., `Specific capacity: ZZZ mAh/g`), both derived from the computed total energies.
3. **bader_charge_output.txt**: a plain‑text file with a single number representing the net Bader charge on one PF6− ion in the fully intercalated stage‑1 structure (in |e|).
4. **diffusion_barrier.txt**: a plain‑text file with a single number giving the lowest energy barrier (in eV) for PF6− diffusion obtained from CI-NEB.
All values must be obtained from the described first-principles procedure and must not be copied from an external source.

## Assets

- DFT code with NEB capability: https://www.quantum-espresso.org/ (or https://www.abinit.org/, https://www.cp2k.org/)
- Bader charge analysis tool: http://theory.cm.utexas.edu/henkelman/code/bader/
- Graphite crystal structure: 10.1103/PhysRevB.5.2460
- PF6 molecular geometry
- Li metal bulk structure: 10.1103/PhysRevB.33.7983
- EMC and LiPF6(EMC)4 molecular models

## Workflow steps

### Step 1: Model construction and DFT geometry optimization
- Role: process
- Action: Construct all atomic models: pristine graphite supercells (6×6×2 for stages 1,2,4 and 6×6×3 for stage‑3), PF6‑ intercalated graphite structures with three F atoms facing graphene at the top site for all concentrations (stage‑1: 4,8,12,16 PF6; stage‑2: 2,4,6,8; stage‑3: 2,4,6,8; stage‑4: 1,2,3,4), isolated PF6 molecule, EMC molecule, LiPF6(EMC)4 complex, and BCC Li bulk. Perform DFT geometry optimization on all structures using a dispersion‑corrected functional (PBE‑D3) to obtain relaxed total energies and lattice parameters. Record all total energies and final interlayer distances for the intercalated systems.
- Evidence: `/app/outputs/model_construction_log.txt`

### Step 2: Intercalation energy and interlayer distance table
- Role: scored (load-bearing)
- Action: From the optimized total energies compute the intercalation energy per PF6‑ using formula: E_inter = (E[(PF6)xCn] – E[Cn] – x·E[PF6]) / x for each stage and concentration. Extract the interlayer distance from the relaxed structures. Output a CSV file with all 16 rows (covering every combination of stage and concentration).
- Output file: `/app/outputs/results_table.csv`
- Format: csv
- Contract: columns: stage (int), PF6_count (int), intercalation_energy_eV (float), interlayer_distance_Angstrom (float)
- Scoring: scored by hidden verifier

### Step 3: Cell voltage and specific capacity
- Role: scored
- Action: Calculate the open‑circuit voltage range from the total energies of the intercalated systems, Li metal, EMC, and LiPF6(EMC)4 using the Nernst equation (V = –ΔE/(x·F)). Determine the maximum specific capacity from C = n·x·F / M_f for the stage‑1 structure with 16 PF6. Write the results to a text file.
- Output file: `/app/outputs/voltage_capacity.txt`
- Format: txt
- Contract: Plain text with two lines: first line 'Voltage range: <min>-<max> V', second line 'Specific capacity: <value> mAh/g'
- Scoring: scored by hidden verifier

### Step 4: Bader charge transfer
- Role: scored
- Action: Run Bader charge analysis on the optimized stage‑1 structure containing 16 PF6. Compute the average net charge gained by PF6 (in |e|) and write the single number to a file.
- Output file: `/app/outputs/bader_charge_output.txt`
- Format: txt
- Contract: A single float number on one line
- Scoring: scored by hidden verifier

### Step 5: PF6‑ diffusion barrier
- Role: scored
- Action: Using the climbing‑image nudged elastic band method with 7 images, identify the minimum energy path for PF6‑ diffusion between equivalent stable top sites in stage‑1 graphite. Report the lowest energy barrier (eV) for the optimal path as a single number.
- Output file: `/app/outputs/diffusion_barrier.txt`
- Format: txt
- Contract: A single float number on one line
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results_table.csv`
- `/app/outputs/voltage_capacity.txt`
- `/app/outputs/bader_charge_output.txt`
- `/app/outputs/diffusion_barrier.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results_table.csv
- path: `/app/outputs/results_table.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: All 16 rows of intercalation energies and interlayer distances for the four stages and varying PF6‑ concentrations.
- schema:
  - `type`: table
  - `required_columns`: `stage`, `PF6_count`, `intercalation_energy_eV`, `interlayer_distance_Angstrom`
  - `units`:
    - `intercalation_energy_eV`: eV
    - `interlayer_distance_Angstrom`: Å

### voltage_capacity.txt
- path: `/app/outputs/voltage_capacity.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Cell voltage range and maximum specific capacity derived from the intercalation energies.
- schema:
  - `type`: text
  - `required`: Two lines: 'Voltage range: X.XX‑Y.YY V' and 'Specific capacity: ZZZ mAh/g'

### bader_charge_output.txt
- path: `/app/outputs/bader_charge_output.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Quantitative charge transfer from graphite to PF6‑ in the fully intercalated stage‑1 structure.
- schema:
  - `type`: text
  - `required`: A single float (e.g., '-0.97') representing the net Bader charge on PF6 in |e|.

### diffusion_barrier.txt
- path: `/app/outputs/diffusion_barrier.txt`
- format: txt
- purpose: scored
- target_policy: threshold_or_better
- description: Energy barrier for PF6‑ migration in graphite via the optimal diffusion path; lower is better.
- schema:
  - `type`: text
  - `required`: A single float (e.g., '0.14') representing the minimum diffusion barrier in eV.

Notes: The first step (model building and DFT optimization) is a required process step whose outcomes are consumed by all subsequent scored steps. The diffusion barrier is scored with threshold_or_better (lower barrier earns full credit). All other quantities are compared against paper‑reported reference values with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results_table.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "stage",
          "PF6_count",
          "intercalation_energy_eV",
          "interlayer_distance_Angstrom"
        ],
        "units": {
          "intercalation_energy_eV": "eV",
          "interlayer_distance_Angstrom": "Å"
        }
      },
      "description": "All 16 rows of intercalation energies and interlayer distances for the four stages and varying PF6‑ concentrations."
    },
    {
      "file": "voltage_capacity.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "required": "Two lines: 'Voltage range: X.XX‑Y.YY V' and 'Specific capacity: ZZZ mAh/g'"
      },
      "description": "Cell voltage range and maximum specific capacity derived from the intercalation energies."
    },
    {
      "file": "bader_charge_output.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "required": "A single float (e.g., '-0.97') representing the net Bader charge on PF6 in |e|."
      },
      "description": "Quantitative charge transfer from graphite to PF6‑ in the fully intercalated stage‑1 structure."
    },
    {
      "file": "diffusion_barrier.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "text",
        "required": "A single float (e.g., '0.14') representing the minimum diffusion barrier in eV."
      },
      "description": "Energy barrier for PF6‑ migration in graphite via the optimal diffusion path; lower is better."
    }
  ],
  "notes": "The first step (model building and DFT optimization) is a required process step whose outcomes are consumed by all subsequent scored steps. The diffusion barrier is scored with threshold_or_better (lower barrier earns full credit). All other quantities are compared against paper‑reported reference values with appropriate tolerances."
}
```

## How you are scored
A hidden verifier independently scores each scored artifact. For every output, the submitted numbers are compared against reference quantities that were obtained by faithfully following the same computational protocol. The scoring applies appropriate tolerances and directional rules: for performance/barrier metrics lower is better, for fixed physical quantities an exact comparison within a tolerance is required, and structural trends (e.g., intercalation energy becoming more negative with increasing concentration) are also checked. The final reward is a weighted combination of the individual stage scores, with the main energetic and electrochemical results contributing the largest share.

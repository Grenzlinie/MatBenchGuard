# DFT-based evaluation of phosphorus carbide monolayer anodes for lithium-ion batteries

## Problem background
Lithium-ion batteries (LIBs) are critical for portable energy storage, but conventional graphite anodes offer limited capacity and modest rate capability. Two-dimensional materials built from light elements can potentially store more lithium per unit mass and provide faster ion diffusion. Phosphorus carbide monolayers (PC2, PC5, PC6) are candidate anode materials whose structural and electronic properties suggest they may host Li atoms with high mobility and capacity. This task evaluates their performance by computing three key quantities from first principles: the electronic character (metallic or semiconducting) of each monolayer, the diffusion energy barrier for a single Li atom, and the theoretical specific capacity for the most promising compositions.

## Approach
The evaluation uses plane-wave density functional theory (DFT) with the Perdew–Burke–Ernzerhof (PBE) exchange–correlation functional, carried out with the open-source Quantum ESPRESSO package. Lithium migration is studied with the climbing‑image nudged elastic band (CI‑NEB) method implemented in the Atomic Simulation Environment (ASE).

The conceptual workflow proceeds in seven ordered stages:
1. Relax the unit cells of PC2, PC5, and PC6 to their equilibrium geometries.
2. (Optional) verify dynamical stability by computing phonon dispersions.
3. Compute the PBE band structure and density of states to classify each monolayer as metallic or semiconducting, recording any band gap.
4. Screen high‑symmetry adsorption sites for a single Li atom to identify the most stable binding configuration.
5. Calculate CI‑NEB energy barriers for Li migration between the lowest‑energy sites.
6. For PC5 and PC6, gradually intercalate Li atoms on both sides of a 2×2 supercell, fully relaxing after each addition, until the structure collapses or Li moves farther than 2.5 Å from the substrate; record the maximum stable Li content.
7. Convert the maximum Li content to a theoretical specific capacity, C = z·y_max·F / M_PCx, where z=1 and F=26.8 Ah mol⁻¹.

All calculations must use standard PBE pseudopotentials; the agent should choose converged kinetic‑energy cutoffs and k‑point meshes to obtain reliable results.

## Reproduction target
Produce three scored JSON files under `/app/outputs/`:
- **electronic_nature.json**: for PC2, PC5, and PC6, report whether the PBE band structure indicates a metallic or semiconducting character and the band gap in eV (0 if metallic).
- **diffusion_barriers.json**: for PC2, PC5, and PC6, report the Li diffusion barrier (eV) obtained from CI‑NEB along the lowest‑energy migration path.
- **capacity.json**: for PC5 and PC6, report the theoretical specific capacity (mAh g⁻¹), the maximum stable Li content per formula unit (y_max), and the corresponding chemical composition (e.g., "P8C40Li34").

Initial monolayer structures must be taken from the publicly available dataset of Yu *et al.* (2019). The agent must execute the DFT and NEB workflow with Quantum ESPRESSO and ASE, and the reported values must reflect its own computations.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Atomic Simulation Environment (ASE): ase
- Phonopy: phonopy
- QE pseudopotentials (SSSP or GBRV library): https://www.quantum-espresso.org/pseudopotentials
- PC2, PC5, PC6 monolayer crystal structures: 10.1021/jacs.8b11609

## Workflow steps

### Step 1: Unit cell geometry optimization
- Role: process
- Action: Relax the unit cells of PC2, PC5, and PC6 monolayers using DFT/PBE, converging forces tightly. Start from the known structures.
- Evidence: `/app/outputs/relax.log`

### Step 2: Phonon stability check (sanity)
- Role: process
- Action: Compute phonon dispersions for each optimized monolayer using density functional perturbation theory or finite differences. Verify the absence of imaginary modes.
- Evidence: `/app/outputs/phonon.log`

### Step 3: Electronic band structure classification
- Role: scored (load-bearing)
- Action: Compute PBE band structures and density of states for each monolayer. Classify each as metallic (Fermi level crosses a band) or semiconducting (finite band gap) and report the band gap.
- Output file: `/app/outputs/electronic_nature.json`
- Format: json
- Contract: {"PC2": {"is_metallic": boolean, "band_gap_eV": number}, "PC5": ..., "PC6": ...}
- Scoring: scored by hidden verifier

### Step 4: Single Li adsorption site screening
- Role: process
- Action: In a 2×2 supercell for each monolayer, place a single Li on high‑symmetry sites, fully relax, and compute adsorption energies. Identify the most stable site for each system.
- Evidence: `/app/outputs/Li_sites.log`

### Step 5: CI‑NEB diffusion barrier calculation
- Role: scored (load-bearing)
- Action: Using climbing‑image nudged elastic band, compute the minimum‑energy path for Li migration between nearest‑neighbor lowest‑energy adsorption sites for each monolayer. Extract the energy barrier.
- Output file: `/app/outputs/diffusion_barriers.json`
- Format: json
- Contract: {"PC2": number (eV), "PC5": number (eV), "PC6": number (eV)}
- Scoring: scored by hidden verifier

### Step 6: Li intercalation content scan
- Role: process
- Action: For PC5 and PC6, in a 2×2 supercell sequentially add Li atoms on both sides, fully relaxing after each addition. Stop when the structure collapses (bond breaking) or a Li atom drifts farther than 2.5 Å from the substrate. Record the maximum stable Li number and composition.
- Evidence: `/app/outputs/intercalation.log`

### Step 7: Specific capacity calculation
- Role: scored (load-bearing)
- Action: Compute theoretical specific capacity using C = z * y_max * F / M_PCx (z=1, F=26.8 Ah mol⁻¹). Report capacities, y_max values, and compositions.
- Output file: `/app/outputs/capacity.json`
- Format: json
- Contract: {"PC5_capacity": number (mAh/g), "PC6_capacity": number (mAh/g), "PC5_y_max": number, "PC6_y_max": number, "PC5_composition": string, "PC6_composition": string}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/electronic_nature.json`
- `/app/outputs/diffusion_barriers.json`
- `/app/outputs/capacity.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### electronic_nature.json
- path: `/app/outputs/electronic_nature.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Classification of each monolayer as metallic or semiconducting and the PBE band gap.
- schema:
  - `type`: object
  - `required`:
    - `PC2`:
      - `is_metallic`: boolean
      - `band_gap_eV`: number
    - `PC5`:
      - `is_metallic`: boolean
      - `band_gap_eV`: number
    - `PC6`:
      - `is_metallic`: boolean
      - `band_gap_eV`: number

### diffusion_barriers.json
- path: `/app/outputs/diffusion_barriers.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Li diffusion energy barriers from CI‑NEB for PC2, PC5, PC6.
- schema:
  - `type`: object
  - `required`:
    - `PC2`: number (eV)
    - `PC5`: number (eV)
    - `PC6`: number (eV)
  - `units`:
    - `PC2`: eV
    - `PC5`: eV
    - `PC6`: eV

### capacity.json
- path: `/app/outputs/capacity.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Theoretical specific capacities and maximum Li content for PC5 and PC6.
- schema:
  - `type`: object
  - `required`:
    - `PC5_capacity`: number (mAh/g)
    - `PC6_capacity`: number (mAh/g)
    - `PC5_y_max`: number
    - `PC6_y_max`: number
    - `PC5_composition`: string
    - `PC6_composition`: string

Notes: Scoring uses a result-level compare (T0) with tolerances appropriate for a re‑run in a different DFT code. The checker reads the JSON files and compares the reported values to hidden paper references.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "electronic_nature.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "PC2": {
            "is_metallic": "boolean",
            "band_gap_eV": "number"
          },
          "PC5": {
            "is_metallic": "boolean",
            "band_gap_eV": "number"
          },
          "PC6": {
            "is_metallic": "boolean",
            "band_gap_eV": "number"
          }
        }
      },
      "description": "Classification of each monolayer as metallic or semiconducting and the PBE band gap."
    },
    {
      "file": "diffusion_barriers.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "PC2": "number (eV)",
          "PC5": "number (eV)",
          "PC6": "number (eV)"
        },
        "units": {
          "PC2": "eV",
          "PC5": "eV",
          "PC6": "eV"
        }
      },
      "description": "Li diffusion energy barriers from CI‑NEB for PC2, PC5, PC6."
    },
    {
      "file": "capacity.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "PC5_capacity": "number (mAh/g)",
          "PC6_capacity": "number (mAh/g)",
          "PC5_y_max": "number",
          "PC6_y_max": "number",
          "PC5_composition": "string",
          "PC6_composition": "string"
        }
      },
      "description": "Theoretical specific capacities and maximum Li content for PC5 and PC6."
    }
  ],
  "notes": "Scoring uses a result-level compare (T0) with tolerances appropriate for a re‑run in a different DFT code. The checker reads the JSON files and compares the reported values to hidden paper references."
}
```

## How you are scored
After the agent submits the three JSON files, a hidden checker reads each file and compares the reported values to a private reference obtained from the same protocol. Each artifact is scored independently using tolerances that accommodate the natural spread between DFT implementations. The final reward is a weighted sum, with the diffusion barriers and capacity contributing the largest shares. Simply guessing or inserting arbitrary numbers is unlikely to fall within the allowed tolerances; the agent must genuinely run the described workflow. The checker does not demand exact agreement with any single number, but it expects that a correct re‑run of the workflow will yield values close enough to the reference.

# VO2 Phase Transition Barrier and Electronic Structure Calculation

## Problem background
Vanadium dioxide (VO2) undergoes a reversible metal-insulator transition (MIT) between a low-temperature monoclinic (M1) insulating phase and a high-temperature tetragonal (rutile) metallic phase. Understanding the energy landscape and electronic structure evolution across this transition is critical for device applications. This task uses first-principles calculations to map the minimum-energy path (MEP) between the two structures, to identify the atomic motions that give rise to the energy barrier, and to correlate them with changes in the electronic band gap. The key open questions are: what is the height of the energy barrier that must be overcome, and how does the electronic band gap change as the structure evolves from the insulating M1 phase toward the metallic rutile phase?

## Approach
The workflow employs density functional theory (DFT) with the GGA-PBE functional and many-body perturbation theory (GW) using open-source codes. Starting from public crystallographic data, the monoclinic (M1) and tetragonal (rutile) structures are first relaxed to their ground states. A climbing-image nudged elastic band (CI-NEB) calculation is then performed between the relaxed endpoints to determine the minimum-energy path; the total energies of all images (including endpoints) are recorded. On selected structures along this path—the relaxed M1 ground state and several intermediate NEB images that occur before the energy maximum—frequency-dependent G0W0 quasiparticle calculations are performed to extract the indirect electronic band gap. The results are two tables: the NEB energy path and the GW band gaps along the transition. The codes chosen are Quantum ESPRESSO (DFT), Yambo (GW), and the Atomic Simulation Environment (ASE) for NEB setup; any comparable open-source implementations are acceptable as long as the required artifacts are produced.

## Reproduction target
Produce two validated CSV files under `/app/outputs`:

1. `step_01_energy_path.csv` — the minimum-energy path from the NEB calculation, containing image indices and corresponding total energies (eV per supercell). The path must include at least 8 intermediate images plus the two endpoints.

2. `step_02_band_gaps.csv` — GW quasiparticle band gaps (eV) for the monoclinic M1 structure and for at least three intermediate NEB images before the energy maximum.

The energy barrier and the sequence of band gaps will be evaluated from these files. The task does not require you to report a final conclusion; your produced data must be sufficient for a checker to determine the barrier height and the evolution of the band gap.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Yambo: https://www.yambo-code.eu/
- Atomic Simulation Environment (ASE): ase
- VO2 monoclinic M1 crystal structure: https://materialsproject.org/materials/mp-19094
- VO2 tetragonal (rutile) crystal structure: https://materialsproject.org/materials/mp-15134

## Workflow steps

### Step 1: Obtain crystal structures
- Role: process
- Action: Download the monoclinic (M1) and tetragonal (rutile) crystal structures of VO2 from public crystallographic databases (e.g., Materials Project mp-19094 and mp-15134 or ICSD).
- Evidence: `/app/outputs/structures_download.log`

### Step 2: DFT geometry relaxation of endpoints
- Role: process
- Action: Using an open-source DFT code (Quantum ESPRESSO) with GGA-PBE functional, relax the atomic positions and cell parameters of both the monoclinic and tetragonal structures to their ground states. Save the relaxed structures for use in the NEB calculation.
- Evidence: `/app/outputs/relaxation.log`

### Step 3: NEB minimum-energy path calculation
- Role: scored (load-bearing)
- Action: Construct a climbing-image nudged elastic band (CI-NEB) path between the relaxed monoclinic and tetragonal structures with at least 8 intermediate images. Use DFT (GGA-PBE) to converge the images to the minimum-energy path. For each image (including endpoints, indexed from 0 for monoclinic), record its total energy in eV per supercell. Write the path to a CSV file.
- Output file: `/app/outputs/step_01_energy_path.csv`
- Format: csv
- Contract: Two columns: 'image' (integer, increasing from 0 for monoclinic) and 'energy_eV' (float, total energy in eV).
- Scoring: scored by hidden verifier

### Step 4: GW band gap calculation on selected images
- Role: scored
- Action: Perform frequency-dependent GW calculations (G0W0) on the relaxed monoclinic M1 structure and on at least three intermediate NEB images (those before the energy maximum) using an open-source GW code (e.g., Yambo). Extract the indirect electronic band gap in eV for each. Write the results to a CSV file.
- Output file: `/app/outputs/step_02_band_gaps.csv`
- Format: csv
- Contract: Two columns: 'step' (string, e.g., 'M1', 'Step1', 'Step2', 'Step3') and 'band_gap_eV' (float, band gap in eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_energy_path.csv`
- `/app/outputs/step_02_band_gaps.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_energy_path.csv
- path: `/app/outputs/step_01_energy_path.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: NEB minimum-energy path: image index and total energy per supercell. The checker recomputes the barrier height from these values and compares with the hidden reference within a relative tolerance.
- schema:
  - `type`: table
  - `required_columns`: `image`, `energy_eV`
  - `units`:
    - `energy_eV`: eV

### step_02_band_gaps.csv
- path: `/app/outputs/step_02_band_gaps.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: GW quasiparticle band gaps for selected structures along the path. The checker verifies that the M1 gap is insulating (>0.5 eV), that gaps decrease monotonically, and that the gap closes (≤0.1 eV) at an image before the energy maximum.
- schema:
  - `type`: table
  - `required_columns`: `step`, `band_gap_eV`
  - `units`:
    - `band_gap_eV`: eV

Notes: The barrier is compared with a hidden target using a relative tolerance to account for code/functional differences. The band gap sequence is verified structurally: insulating start, monotonic decrease, and closure before the structural barrier.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_energy_path.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "image",
          "energy_eV"
        ],
        "units": {
          "energy_eV": "eV"
        }
      },
      "description": "NEB minimum-energy path: image index and total energy per supercell. The checker recomputes the barrier height from these values and compares with the hidden reference within a relative tolerance."
    },
    {
      "file": "step_02_band_gaps.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "step",
          "band_gap_eV"
        ],
        "units": {
          "band_gap_eV": "eV"
        }
      },
      "description": "GW quasiparticle band gaps for selected structures along the path. The checker verifies that the M1 gap is insulating (>0.5 eV), that gaps decrease monotonically, and that the gap closes (≤0.1 eV) at an image before the energy maximum."
    }
  ],
  "notes": "The barrier is compared with a hidden target using a relative tolerance to account for code/functional differences. The band gap sequence is verified structurally: insulating start, monotonic decrease, and closure before the structural barrier."
}
```

## How you are scored
A hidden verifier independently inspects your two scored artifacts and computes a reward in [0,1] from two weighted components:

- **Energy path (step_01_energy_path.csv)**: The verifier recomputes the energy barrier from your CSV as the difference between the maximum total energy and the average of the two endpoint energies. This recomputed barrier is compared to a hidden reference value using an appropriate tolerance that accounts for code and functional differences. Full credit is earned if the barrier falls within the expected range; credit decreases for larger deviations.

- **Band gaps (step_02_band_gaps.csv)**: The verifier verifies structural relationships: (a) the M1 band gap indicates an insulating phase; (b) the band gaps decrease monotonically; and (c) the gap closes to a metallic threshold (≤ 0.1 eV) at or before the image with the highest energy in the NEB path. All three conditions must be satisfied for full credit on this component.

The final reward is the weighted combination of these two scores. Reporting paper-reported numbers without producing the underlying raw artifacts will not pass the verification. The exact weighting and tolerances are known only to the verifier.

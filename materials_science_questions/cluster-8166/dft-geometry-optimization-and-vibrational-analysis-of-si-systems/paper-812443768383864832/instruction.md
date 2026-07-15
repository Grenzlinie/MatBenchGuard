# DFT Study of Pressure-Induced Phonon Instability in K8Si46 Clathrate

## Problem background
Type-I silicon clathrate K8Si46 (space group Pm-3n) with encaged K atoms undergoes an isostructural phase transition under pressure without a change in crystal symmetry. First-principles calculations have been used to investigate the role of the guest atoms in the structural stability of the clathrate framework. The central question is whether pressure induces a phonon instability of the K atoms in the large cages and whether the forces on a displaced K atom drive off-center motion. This reproduction task computes the equation of state, the minimum phonon frequency at two pressures, and the force-displacement curve for a K atom, providing direct evidence to assess the proposed instability mechanism.

## Approach
The computational pipeline consists of three stages:
1. Perform DFT geometry optimizations of K8Si46 at several hydrostatic pressures (0–20 GPa) to obtain the volume compression curve (V/V0).
2. Compute phonon band structures at two selected pressures and extract the lowest phonon frequency, with imaginary frequencies expressed as negative values.
3. Scan the Hellmann-Feynman force on a K atom displaced from its high-symmetry site in the large cage at high pressure.

All calculations use plane-wave density functional theory with a generalized gradient approximation (GGA) exchange-correlation functional and appropriate pseudopotentials, as implemented in open-source codes such as Quantum ESPRESSO.

## Reproduction target
Produce three CSV files under `/app/outputs`:
- `equation_of_state.csv`: columns `pressure` (GPa), `volume` (Å³), `volume_ratio` (unitless). Report the optimized unit cell volumes and V/V0 ratios for pressures 0, 5, 10, 15, and 20 GPa.
- `phonon_min_frequencies.csv`: columns `pressure` (GPa), `min_frequency` (cm⁻¹). Report the lowest phonon frequency anywhere in the Brillouin zone at 5 GPa and 16 GPa; imaginary frequencies must be given as negative numbers.
- `force_curve.csv`: columns `displacement` (Å), `force` (eV/Å). At 16 GPa, displace one K atom in the large cage (starting from fractional coordinates (0.25, 0.5, 0)) along the crystallographic b direction in steps from 0.0 to 0.1 Å and record the Hellmann-Feynman force along b.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP Efficiency Pseudopotentials: https://www.materialscloud.org/discover/sssp/table/efficiency
- K8Si46 crystallographic data: 10.1006/jssc.2000.8922

## Workflow steps

### Step 1: Prepare initial K8Si46 structure
- Role: process
- Action: Generate the crystal structure of K8Si46 in space group Pm-3n with lattice constant a=10.275 Å, using the published Wyckoff positions (Si at 6c, 16i, 24k; K at 2a, 6d). The structure can be generated with ASE or a manually written input file.
- Evidence: `/app/outputs/initial_structure.cif`

### Step 2: DFT geometry optimization and equation of state
- Role: scored (load-bearing)
- Action: Perform DFT geometry optimization of K8Si46 using an open-source plane-wave DFT code (e.g., Quantum ESPRESSO) with a GGA exchange-correlation functional. Optimize the unit cell and atomic positions under hydrostatic pressure at 0, 5, 10, 15, and 20 GPa. Record the optimized unit cell volume and compute the volume ratio V/V0 (V0 = volume at 0 GPa).
- Output file: `/app/outputs/equation_of_state.csv`
- Format: csv
- Contract: pressure (GPa, numeric), volume (A^3, numeric), volume_ratio (numeric)
- Scoring: scored by hidden verifier

### Step 3: Phonon minimum frequencies
- Role: scored
- Action: Using the optimized structures from the equation-of-state step at 5 GPa and 16 GPa, compute the phonon band structure via density functional perturbation theory (DFPT) or the finite displacement method. Extract the lowest phonon frequency (in cm⁻¹) anywhere in the Brillouin zone; report imaginary frequencies as negative values.
- Output file: `/app/outputs/phonon_min_frequencies.csv`
- Format: csv
- Contract: pressure (GPa, numeric), min_frequency (cm^-1, numeric, can be negative)
- Scoring: scored by hidden verifier

### Step 4: Force on displaced K atom
- Role: scored
- Action: Using the optimized geometry at 16 GPa, displace one K atom in the large cage along the crystallographic b direction in steps from 0.0 to 0.1 Å. For each displacement, compute the Hellmann-Feynman force on the K atom along b (in eV/Å).
- Output file: `/app/outputs/force_curve.csv`
- Format: csv
- Contract: displacement (A, numeric), force (eV/A, numeric)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/equation_of_state.csv`
- `/app/outputs/phonon_min_frequencies.csv`
- `/app/outputs/force_curve.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### equation_of_state.csv
- path: `/app/outputs/equation_of_state.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Volume compression curve (V/V0 vs pressure); the verifier compares volume ratios to hidden reference values using a tolerance.
- schema:
  - `type`: table
  - `required_columns`: `pressure`, `volume`, `volume_ratio`
  - `units`:
    - `pressure`: GPa
    - `volume`: A^3
    - `volume_ratio`: unitless

### phonon_min_frequencies.csv
- path: `/app/outputs/phonon_min_frequencies.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Lowest phonon frequency at 5 and 16 GPa; the verifier checks the values against hidden thresholds. Imaginary frequencies must be reported as negative numbers.
- schema:
  - `type`: table
  - `required_columns`: `pressure`, `min_frequency`
  - `units`:
    - `pressure`: GPa
    - `min_frequency`: cm^-1

### force_curve.csv
- path: `/app/outputs/force_curve.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Force-displacement curve for a displaced K atom at 16 GPa; the verifier checks forces at specified displacements against hidden thresholds.
- schema:
  - `type`: table
  - `required_columns`: `displacement`, `force`
  - `units`:
    - `displacement`: A
    - `force`: eV/A

Notes: All scored quantities are compared against hidden reference criteria. The EOS uses tolerance-based comparison; the phonon and force checks use hidden thresholds.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "equation_of_state.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure",
          "volume",
          "volume_ratio"
        ],
        "units": {
          "pressure": "GPa",
          "volume": "A^3",
          "volume_ratio": "unitless"
        }
      },
      "description": "Volume compression curve (V/V0 vs pressure); the verifier compares volume ratios to hidden reference values using a tolerance."
    },
    {
      "file": "phonon_min_frequencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure",
          "min_frequency"
        ],
        "units": {
          "pressure": "GPa",
          "min_frequency": "cm^-1"
        }
      },
      "description": "Lowest phonon frequency at 5 and 16 GPa; the verifier checks the values against hidden thresholds. Imaginary frequencies must be reported as negative numbers."
    },
    {
      "file": "force_curve.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "displacement",
          "force"
        ],
        "units": {
          "displacement": "A",
          "force": "eV/A"
        }
      },
      "description": "Force-displacement curve for a displaced K atom at 16 GPa; the verifier checks forces at specified displacements against hidden thresholds."
    }
  ],
  "notes": "All scored quantities are compared against hidden reference criteria. The EOS uses tolerance-based comparison; the phonon and force checks use hidden thresholds."
}
```

## How you are scored
Each of the three scored output files is checked independently by a hidden verifier. The verifier compares the reported values against hidden reference criteria (tolerances or thresholds) and computes a weighted total reward.
- The equation-of-state check compares the volume ratios at each pressure to reference values using a tolerance.
- The phonon frequency check evaluates the lowest frequency at each specified pressure against hidden thresholds; the agent must report imaginary frequencies as negative numbers.
- The force-curve check evaluates the force at specified displacements against hidden thresholds.

The final reward is the weighted sum of the scores from these three checks.

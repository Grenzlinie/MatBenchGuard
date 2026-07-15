# Point defect characterization of interstitial iodine in MAPbI3 perovskite: geometries and recombination

## Problem background
Hybrid organic-inorganic perovskite MAPbI3 (CH3NH3PbI3) is a leading absorber material for solar cells, but its performance is limited by nonradiative charge recombination that can be induced by intrinsic point defects. Interstitial iodine defects are common, and their oxidation state may influence charge trapping and recombination dynamics, while oxygen passivation could further modulate stability and carrier lifetimes. Understanding how the oxidation state of interstitial iodine and oxygen passivation affect the electron-hole recombination time is crucial for designing high-performance perovskite devices. This task aims to reproduce a computational study that uses density functional theory (DFT) and nonadiabatic molecular dynamics (NAMD) to systematically compute structural properties and recombination times in pristine MAPbI3 and in systems containing neutral, negatively charged, and positively charged interstitial iodine, as well as an oxygen-passivated negatively charged defect.

## Approach
The approach combines first-principles DFT calculations with time-domain NAMD simulations. A 2×2×1 tetragonal supercell of MAPbI3 is first built. Defective structures are created by adding an interstitial iodine atom and adjusting the net charge to obtain neutral (I_i), negatively charged (I_i⁻¹), and positively charged (I_i⁺¹) defects. An oxygen-passivated defect (IO₃⁻¹) is constructed by placing three oxygen atoms around the interstitial iodine in I_i⁻¹. Geometry optimizations are performed at 0 K using the Perdew–Burke–Ernzerhof (PBE) exchange-correlation functional with Grimme's DFT‑D3 van der Waals correction and PAW pseudopotentials. Ab initio molecular dynamics (AIMD) simulations are then carried out at 300 K to generate trajectories of at least 6 ps. From the optimized geometries and the MD trajectories, structural distances (I–I and I–Pb) and root‑mean‑square atomic velocities are extracted. Finally, nonadiabatic molecular dynamics (NAMD) simulations using the decoherence‑induced surface hopping (DISH) algorithm are run on the first 4000 MD snapshots to compute state‑to‑state transition rates; solving the coupled kinetic equations yields the macroscopic electron–hole recombination times. The five systems are compared to reveal how defect charge state and oxygen passivation influence the recombination dynamics.

## Reproduction target
The target is to produce the following scored artifacts:
1) I–I and I–Pb distances at 0 K and 300 K for the I_i, I_i⁻¹, and I_i⁺¹ systems (JSON).
2) Root‑mean‑square velocity table (total, MA, Pb‑I lattice, Pb‑I including interstitial, interstitial I, O) for all five systems (CSV).
3) Electron‑hole recombination times (in ns) for pristine, I_i, I_i⁻¹, I_i⁺¹, and IO₃⁻¹, together with the correct ordering of recombination times from shortest to longest (JSON).
The results must be obtained by re‑running the full computational protocol (supercell building, DFT optimization, AIMD, NAMD, and kinetic analysis) and must not be looked up from any reference. The hidden verifier will assess your output against reference values that are known to be correct for this procedure.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PYXAID: https://github.com/PrezhdoGroup/PYXAID
- Grimme DFT-D3 correction: https://www.chemie.uni-bonn.de/pctc/mulliken-center/software/dft-d3
- Tetragonal MAPbI3 crystal structure (2x2x1 supercell): mp-12405

## Workflow steps

### Step 1: Build supercell models
- Role: process
- Action: Construct the 2×2×1 tetragonal supercell of MAPbI3, then create defective structures I_i, I_i⁻¹, I_i⁺¹, and IO₃⁻¹ by adding interstitial iodine (and adjusting charge) and oxygen atoms as needed.
- Evidence: none

### Step 2: DFT geometry optimization at 0 K
- Role: process
- Action: Perform full DFT geometry optimization at 0 K for each of the five systems (pristine, I_i, I_i⁻¹, I_i⁺¹, IO₃⁻¹) using PBE functional, PAW pseudopotentials, DFT-D3 van der Waals correction, and a plane-wave cutoff of 400 eV. Converge forces tightly.
- Evidence: none

### Step 3: Ab initio molecular dynamics at 300 K
- Role: process
- Action: For each optimized system, heat from 0 K to 300 K over 2 ps using velocity rescaling, then continue a 6 ps microcanonical (NVE) MD trajectory with a 1 fs time step. Save at least 4000 snapshots (coordinates, velocities, total energies).
- Evidence: none

### Step 4: Compute I–I and I–Pb distances
- Role: scored
- Action: From the 0 K optimized geometries and the 300 K MD trajectories, extract the interstitial–lattice I–I distances and the I–Pb distances for I_i, I_i⁻¹, I_i⁺¹. Compute canonical averages over the MD trajectory for 300 K. Report the data in JSON.
- Output file: `/app/outputs/structural_distances.json`
- Format: json
- Contract: A JSON object with top-level keys 'I_i', 'I_i_minus1', 'I_i_plus1'. Each key's value is an object with two sub-objects: '0K' and '300K'. Each of these contains 'I_I_distance' (float, Å) and 'I_Pb_distance' (float, Å).
- Scoring: scored by hidden verifier

### Step 5: Compute root-mean-square velocities
- Role: scored
- Action: Using the 6 ps MD trajectories, compute the root-mean-square (RMS) velocity of atomic positions (Å/fs) for each system, partitioned into groups: total, MA cations, Pb–I lattice atoms, Pb–I including interstitial iodine, interstitial iodine itself, and oxygen (where present). Report as CSV.
- Output file: `/app/outputs/rms_velocities.csv`
- Format: csv
- Contract: CSV with columns: System (string, one of 'MAPbI3', 'I_i', 'I_i_minus1', 'I_i_plus1', 'IO3_minus1'), total (float, Å/fs), MA (float, Å/fs), Pb_I_lattice (float, Å/fs), Pb_I_including_interstitial (float, Å/fs), interstitial_I (float, Å/fs), O (float, Å/fs, 0.0 when absent).
- Scoring: scored by hidden verifier

### Step 6: Run NAMD simulations
- Role: process
- Action: For each system, take the first 4000 MD snapshots, compute Kohn–Sham orbitals and nonadiabatic couplings. Perform decoherence-induced surface hopping (DISH) NAMD simulations to obtain state-to-state transition rate constants for all relevant processes (CBM→VBM, VBM→trap, CBM→trap, etc.). Save the raw rate constants.
- Evidence: `/app/outputs/na_rate_constants.csv`

### Step 7: Kinetic analysis and recombination times
- Role: scored (load-bearing)
- Action: Using the rate constants obtained in step_06, solve the coupled kinetic equations for each system to obtain the macroscopic electron–hole recombination times (in ns). Report the times and the relative ordering of recombination times across systems in JSON.
- Output file: `/app/outputs/recombination_times.json`
- Format: json
- Contract: A JSON object with top-level keys 'pristine', 'I_i', 'I_i_minus1', 'I_i_plus1', 'IO3_minus1'. Each key's value is an object containing 'recombination_time_ns' (float) and optionally 'rate_constant_per_ps' (float). Also include an array 'recombination_ordering' listing the system identifiers in increasing order of recombination time (e.g., ['I_i','pristine','I_i_minus1','I_i_plus1','IO3_minus1']).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/structural_distances.json`
- `/app/outputs/rms_velocities.csv`
- `/app/outputs/recombination_times.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### structural_distances.json
- path: `/app/outputs/structural_distances.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: I–I and I–Pb distances for the three interstitial iodine charge states at 0 K and 300 K.
- schema:
  - `type`: object
  - `required`:
    - `I_i`:
      - `0K`:
        - `I_I_distance`: float (Angstrom)
        - `I_Pb_distance`: float (Angstrom)
      - `300K`:
        - `I_I_distance`: float (Angstrom)
        - `I_Pb_distance`: float (Angstrom)
    - `I_i_minus1`:
      - `0K`:
        - `I_I_distance`: float (Angstrom)
        - `I_Pb_distance`: float (Angstrom)
      - `300K`:
        - `I_I_distance`: float (Angstrom)
        - `I_Pb_distance`: float (Angstrom)
    - `I_i_plus1`:
      - `0K`:
        - `I_I_distance`: float (Angstrom)
        - `I_Pb_distance`: float (Angstrom)
      - `300K`:
        - `I_I_distance`: float (Angstrom)
        - `I_Pb_distance`: float (Angstrom)

### rms_velocities.csv
- path: `/app/outputs/rms_velocities.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Root-mean-square velocities of atomic positions grouped by species for five systems.
- schema:
  - `type`: table
  - `required_columns`: `System`, `total`, `MA`, `Pb_I_lattice`, `Pb_I_including_interstitial`, `interstitial_I`, `O`
  - `units`:
    - `total`: Angstrom/fs
    - `MA`: Angstrom/fs
    - `Pb_I_lattice`: Angstrom/fs
    - `Pb_I_including_interstitial`: Angstrom/fs
    - `interstitial_I`: Angstrom/fs
    - `O`: Angstrom/fs

### recombination_times.json
- path: `/app/outputs/recombination_times.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Electron-hole recombination times and their ordering across five systems. Times in ns. Ordering from shortest to longest recombination time.
- schema:
  - `type`: object
  - `required`:
    - `pristine`:
      - `recombination_time_ns`: float (ns)
    - `I_i`:
      - `recombination_time_ns`: float (ns)
    - `I_i_minus1`:
      - `recombination_time_ns`: float (ns)
    - `I_i_plus1`:
      - `recombination_time_ns`: float (ns)
    - `IO3_minus1`:
      - `recombination_time_ns`: float (ns)
    - `recombination_ordering`: array of strings

Notes: The checker will verify distances and velocities within tolerances, and recombination times within a factor-of-2 range plus correct ordering.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "structural_distances.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "I_i": {
            "0K": {
              "I_I_distance": "float (Angstrom)",
              "I_Pb_distance": "float (Angstrom)"
            },
            "300K": {
              "I_I_distance": "float (Angstrom)",
              "I_Pb_distance": "float (Angstrom)"
            }
          },
          "I_i_minus1": {
            "0K": {
              "I_I_distance": "float (Angstrom)",
              "I_Pb_distance": "float (Angstrom)"
            },
            "300K": {
              "I_I_distance": "float (Angstrom)",
              "I_Pb_distance": "float (Angstrom)"
            }
          },
          "I_i_plus1": {
            "0K": {
              "I_I_distance": "float (Angstrom)",
              "I_Pb_distance": "float (Angstrom)"
            },
            "300K": {
              "I_I_distance": "float (Angstrom)",
              "I_Pb_distance": "float (Angstrom)"
            }
          }
        }
      },
      "description": "I–I and I–Pb distances for the three interstitial iodine charge states at 0 K and 300 K."
    },
    {
      "file": "rms_velocities.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "System",
          "total",
          "MA",
          "Pb_I_lattice",
          "Pb_I_including_interstitial",
          "interstitial_I",
          "O"
        ],
        "units": {
          "total": "Angstrom/fs",
          "MA": "Angstrom/fs",
          "Pb_I_lattice": "Angstrom/fs",
          "Pb_I_including_interstitial": "Angstrom/fs",
          "interstitial_I": "Angstrom/fs",
          "O": "Angstrom/fs"
        }
      },
      "description": "Root-mean-square velocities of atomic positions grouped by species for five systems."
    },
    {
      "file": "recombination_times.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "pristine": {
            "recombination_time_ns": "float (ns)"
          },
          "I_i": {
            "recombination_time_ns": "float (ns)"
          },
          "I_i_minus1": {
            "recombination_time_ns": "float (ns)"
          },
          "I_i_plus1": {
            "recombination_time_ns": "float (ns)"
          },
          "IO3_minus1": {
            "recombination_time_ns": "float (ns)"
          },
          "recombination_ordering": "array of strings"
        }
      },
      "description": "Electron-hole recombination times and their ordering across five systems. Times in ns. Ordering from shortest to longest recombination time."
    }
  ],
  "notes": "The checker will verify distances and velocities within tolerances, and recombination times within a factor-of-2 range plus correct ordering."
}
```

## How you are scored
A hidden verifier independently evaluates each of the three scored output files. For structural_distances.json and rms_velocities.csv, the verifier compares your numerical values to reference values within prescribed tolerances. For recombination_times.json, the verifier compares the reported recombination times within a factor‑of‑2 range and also checks that the recombination_ordering array contains the five system identifiers in the correct increasing order of recombination time. Each stage is assigned a weight, with the recombination time stage contributing the largest share to the final reward (a float between 0 and 1). You must execute all process steps honestly and produce verifiable artifacts; simply reporting numbers without running the required workflow will not earn credit.

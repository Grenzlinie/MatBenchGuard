# GB phase identification and thermodynamic analysis in Cu Σ37 tilt boundary

## Problem background
Grain boundaries in polycrystalline metals can adopt multiple distinct atomic arrangements, known as grain boundary phases, which strongly influence interfacial properties such as strength, transport, and stability. This task concerns a particular symmetric tilt grain boundary in elemental copper where two structurally different phases have been computationally predicted. Understanding their thermodynamic excess properties, the ability to separate them, and their relative stability as a function of temperature is essential for predicting and controlling grain boundary behavior in this material.

## Approach
The approach uses atomistic simulations with an embedded-atom method (EAM) potential to construct a bicrystal containing the target grain boundary. A systematic in-plane translation (γ-surface) search is performed at zero temperature to generate a pool of low-energy grain boundary configurations. From this pool, the two dominant structural motifs (domino and pearl) are identified. For each low-energy configuration, grain boundary excess thermodynamic properties—energy, excess volume, excess stresses, excess atom count, and microscopic shear components—are computed. The full set of structures is then subjected to k‑means clustering (k = 2) to confirm that they separate naturally into two families. Finally, the quasi‑harmonic free energy of the representative domino and pearl structures is calculated over a temperature range from 0 K to 800 K to determine at which temperature the relative stability changes.

## Reproduction target
Using the specified EAM potential and LAMMPS, you must construct the Σ37c ⟨111⟩ {1 10 11} Cu bicrystal, perform a γ‑surface search to locate low‑energy grain boundary structures, and extract the atomic coordinates of the two distinct phases—domino and pearl—as XYZ files. Compute the thermodynamic excess properties (grain boundary energy, excess volume, excess stresses, excess atom count, and shear components) for all structures with γ₀ < 0.95 J m⁻² and write them to a CSV file. Apply k‑means clustering (k = 2) to these structures using the relevant excess properties and output the cluster assignments. Then, using the lowest‑energy domino and pearl structures, compute their grain‑boundary free energies γ(T) via the quasi‑harmonic approximation at temperatures from 0 K to 800 K with a step of ≤ 50 K and write the curves to a CSV file. The resulting artifact must allow identification of the temperature at which the free energies cross, indicating a shift in thermodynamic stability.

## Assets

- Mishin EAM Cu potential: https://www.ctcms.nist.gov/potentials/Cu.html
- LAMMPS: https://lammps.sandia.gov
- Python with numpy, scipy, scikit-learn

## Workflow steps

### Step 1: Construct bicrystal
- Role: process
- Action: Construct a bicrystal of fcc Cu with the Σ37c ⟨111⟩ {1 10 11} misorientation (misorientation angle 50.57°), using lattice constant a=3.615 Å. Set periodic boundary conditions in the GB plane directions ([3 4 7], [11 10 1]) and open surfaces normal to the GB.
- Evidence: none

### Step 2: γ-surface sampling and relaxation
- Role: process
- Action: Perform a γ-surface search by displacing the top grain over a grid of in-plane translation vectors, relaxing each configuration at 0 K using the EAM potential in LAMMPS. Collect all relaxed structures with grain boundary energy γ₀ < 0.95 J/m². Record the relaxation log.
- Evidence: `/app/outputs/relaxation_log.csv`

### Step 3: Output domino phase structure
- Role: scored (load-bearing)
- Action: From the pool of relaxed structures, select the lowest‑energy configuration matching the domino motif (repeating D( units). Export the atomic coordinates of the GB supercell unit as an XYZ file.
- Output file: `/app/outputs/domino_structure.xyz`
- Format: txt
- Contract: {"type": "table", "columns": ["element", "x", "y", "z"], "units": {"x": "Angstrom", "y": "Angstrom", "z": "Angstrom"}}
- Scoring: scored by hidden verifier

### Step 4: Output pearl phase structure
- Role: scored (load-bearing)
- Action: From the pool of relaxed structures, select the configuration that best matches the pearl phase motif (e.g., containing S, P and B units; equivalent to pearl #2). Export the atomic coordinates of the GB supercell unit as an XYZ file.
- Output file: `/app/outputs/pearl_structure.xyz`
- Format: txt
- Contract: {"type": "table", "columns": ["element", "x", "y", "z"], "units": {"x": "Angstrom", "y": "Angstrom", "z": "Angstrom"}}
- Scoring: scored by hidden verifier

### Step 5: Compute excess properties
- Role: scored (load-bearing)
- Action: For every structure from step_02 with γ₀ < 0.95 J/m², compute the excess properties: grain boundary energy γ₀ (J/m²), excess volume [V] (Å), excess stresses [τ₁₁], [τ₂₂], [τ₁₂] (J/m²), excess number of atoms [n] (fraction of a {11011} plane), and excess shear components [B₁], [B₂], [B₃] (Å). Write results to a CSV file.
- Output file: `/app/outputs/excess_properties.csv`
- Format: csv
- Contract: {"type": "table", "required_columns": ["structure_id", "gamma_0", "excess_volume", "tau_11", "tau_22", "tau_12", "excess_atoms", "B1", "B2", "B3"], "units": {"gamma_0": "J/m2", "excess_volume": "Angstrom", "tau_11": "J/m2", "tau_22": "J/m2", "tau_12": "J/m2", "excess_atoms": "fraction of {11011} plane", "B1": "Angstrom", "B2": "Angstrom", "B3": "Angstrom"}}
- Scoring: scored by hidden verifier

### Step 6: Cluster structures
- Role: scored
- Action: Apply k‑means clustering (k=2) to the structures using standardized excess properties (γ₀, [V], [τ₁₁], [τ₂₂], [τ₁₂], [n], [B₁]). For each structure, output its cluster label. The pearl and domino structures must belong to different clusters. Include at least the domino and pearl structures and 10 additional defective variants.
- Output file: `/app/outputs/clustering_results.csv`
- Format: csv
- Contract: {"type": "table", "required_columns": ["structure_id", "cluster_label"]}
- Scoring: scored by hidden verifier

### Step 7: Calculate free energy curves
- Role: scored (load-bearing)
- Action: For the lowest‑energy domino and pearl structures (from step_03 and step_04), compute the grain‑boundary free energy γ(T) using the quasi‑harmonic approximation, for temperatures from 0 K to 800 K with step ≤ 50 K. Output the free energy values for each temperature.
- Output file: `/app/outputs/free_energy_curve.csv`
- Format: csv
- Contract: {"type": "table", "required_columns": ["T", "gamma_domino", "gamma_pearl"], "units": {"T": "K", "gamma_domino": "J/m2", "gamma_pearl": "J/m2"}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/domino_structure.xyz`
- `/app/outputs/pearl_structure.xyz`
- `/app/outputs/excess_properties.csv`
- `/app/outputs/clustering_results.csv`
- `/app/outputs/free_energy_curve.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### domino_structure.xyz
- path: `/app/outputs/domino_structure.xyz`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Atomic structure of the domino GB phase. The checker compares against a hidden reference structure with position tolerance ±0.2 Å.
- schema:
  - `type`: table
  - `columns`: `element`, `x`, `y`, `z`
  - `units`:
    - `x`: Angstrom
    - `y`: Angstrom
    - `z`: Angstrom

### pearl_structure.xyz
- path: `/app/outputs/pearl_structure.xyz`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Atomic structure of the pearl GB phase. The checker compares against a hidden reference structure with position tolerance ±0.2 Å.
- schema:
  - `type`: table
  - `columns`: `element`, `x`, `y`, `z`
  - `units`:
    - `x`: Angstrom
    - `y`: Angstrom
    - `z`: Angstrom

### excess_properties.csv
- path: `/app/outputs/excess_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Thermodynamic excess properties. Checker compares selected values (domino and pearl) against hidden reference with tolerances. The domino and pearl entries must have structure_id 'domino' and 'pearl' respectively.
- schema:
  - `type`: table
  - `required_columns`: `structure_id`, `gamma_0`, `excess_volume`, `tau_11`, `tau_22`, `tau_12`, `excess_atoms`, `B1`, `B2`, `B3`
  - `units`:
    - `gamma_0`: J/m2
    - `excess_volume`: Angstrom
    - `tau_11`: J/m2
    - `tau_22`: J/m2
    - `tau_12`: J/m2
    - `excess_atoms`: fraction of {11011} plane
    - `B1`: Angstrom
    - `B2`: Angstrom
    - `B3`: Angstrom

### clustering_results.csv
- path: `/app/outputs/clustering_results.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: k‑means cluster labels. Checker validates that domino and pearl are in different clusters and there are ≥10 additional structures.
- schema:
  - `type`: table
  - `required_columns`: `structure_id`, `cluster_label`

### free_energy_curve.csv
- path: `/app/outputs/free_energy_curve.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Free energy curves. Checker recomputes the crossing temperature (linear interpolation) and verifies it is within 400–520 K.
- schema:
  - `type`: table
  - `required_columns`: `T`, `gamma_domino`, `gamma_pearl`
  - `units`:
    - `T`: K
    - `gamma_domino`: J/m2
    - `gamma_pearl`: J/m2

Notes: The checker will not run simulations; it only validates the submitted artifacts by comparing structures, excess properties, clustering, and recomputing the free‑energy crossing temperature.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "domino_structure.xyz",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "columns": [
          "element",
          "x",
          "y",
          "z"
        ],
        "units": {
          "x": "Angstrom",
          "y": "Angstrom",
          "z": "Angstrom"
        }
      },
      "description": "Atomic structure of the domino GB phase. The checker compares against a hidden reference structure with position tolerance ±0.2 Å."
    },
    {
      "file": "pearl_structure.xyz",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "columns": [
          "element",
          "x",
          "y",
          "z"
        ],
        "units": {
          "x": "Angstrom",
          "y": "Angstrom",
          "z": "Angstrom"
        }
      },
      "description": "Atomic structure of the pearl GB phase. The checker compares against a hidden reference structure with position tolerance ±0.2 Å."
    },
    {
      "file": "excess_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "structure_id",
          "gamma_0",
          "excess_volume",
          "tau_11",
          "tau_22",
          "tau_12",
          "excess_atoms",
          "B1",
          "B2",
          "B3"
        ],
        "units": {
          "gamma_0": "J/m2",
          "excess_volume": "Angstrom",
          "tau_11": "J/m2",
          "tau_22": "J/m2",
          "tau_12": "J/m2",
          "excess_atoms": "fraction of {11011} plane",
          "B1": "Angstrom",
          "B2": "Angstrom",
          "B3": "Angstrom"
        }
      },
      "description": "Thermodynamic excess properties. Checker compares selected values (domino and pearl) against hidden reference with tolerances. The domino and pearl entries must have structure_id 'domino' and 'pearl' respectively."
    },
    {
      "file": "clustering_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "structure_id",
          "cluster_label"
        ]
      },
      "description": "k‑means cluster labels. Checker validates that domino and pearl are in different clusters and there are ≥10 additional structures."
    },
    {
      "file": "free_energy_curve.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "gamma_domino",
          "gamma_pearl"
        ],
        "units": {
          "T": "K",
          "gamma_domino": "J/m2",
          "gamma_pearl": "J/m2"
        }
      },
      "description": "Free energy curves. Checker recomputes the crossing temperature (linear interpolation) and verifies it is within 400–520 K."
    }
  ],
  "notes": "The checker will not run simulations; it only validates the submitted artifacts by comparing structures, excess properties, clustering, and recomputing the free‑energy crossing temperature."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that reads each required output file. The atomic structures are compared against reference coordinates with a position tolerance. Excess properties for the key phases are checked for agreement with expected values. The clustering result is verified to separate the two phase families with at least the required number of structures. From the free energy curves, the temperature at which the two curves cross is recomputed and compared to the known physical crossing. Each scored artifact contributes a weight to the final reward; simply reporting a final number without the correct intermediate artifacts yields zero credit. No manual inspection is performed—only the automated checker determines your score.

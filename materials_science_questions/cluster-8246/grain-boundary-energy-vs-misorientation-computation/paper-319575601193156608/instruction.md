# Molecular statics simulation of ω-phase nanolayer at a Σ3 twin boundary in tungsten

## Problem background
In body-centered cubic (bcc) metals, grain boundaries are typically narrow two-dimensional defects because of the high stacking‑fault energy. However, special boundaries can exhibit more complex, extended structures. This task examines the Σ3⟨110⟩{111} incoherent twin boundary in tungsten using atomistic simulations. The goal is to determine whether this boundary undergoes a structural transformation and to characterize its energy and atomic arrangement, potentially revealing the formation of a hexagonal omega‑phase nanolayer.

## Approach
The simulation uses an embedded‑atom method (EAM) potential for tungsten, specifically the Foiles potential. A bicrystal with the Σ3 orientation is constructed from the coincident‑site lattice (CSL) model using the experimental bcc lattice parameter and periodic boundary conditions in the boundary plane. The total energy is minimized by molecular statics, varying the dilational strain normal to the boundary, rigid‑body translations of the two grains in the boundary plane, and individual displacements of atomic planes (Sutton's variational method). From the unrelaxed and relaxed configurations, the grain boundary energy is computed. The relaxed atomic structure is then analyzed to identify any secondary phase and to measure its lattice parameters. Finally, a layer‑resolved excess energy profile is obtained by evaluating the energy of each {111} atomic plane relative to bulk tungsten, capturing the energetic signature of the boundary core.

## Reproduction target
1. Compute the unrelaxed and relaxed grain boundary energies (J/m²) and write them to `/app/outputs/energies.json`.  
2. Analyze the relaxed structure to determine whether an omega‑phase nanolayer has formed; if present, measure the in‑plane lattice parameter a (nm), the out‑of‑plane lattice parameter c (nm), and the c/a ratio, and output them to `/app/outputs/omega_params.json`.  
3. For each {111} atomic plane near the boundary (indices from at least −3 to +3, with 0 at the boundary center), compute the excess energy relative to bulk tungsten (J/m²) and write the array to `/app/outputs/excess_energy_profile.json`.

## Assets

- Foiles EAM potential for tungsten: https://www.ctcms.nist.gov/potentials/download/W/W.eam

## Workflow steps

### Step 1: Construct CSL bicrystal configuration
- Role: process
- Action: Generate the initial unrelaxed atomic positions for the Σ3⟨110⟩{111} bicrystal using the coincident-site lattice (CSL) model with bcc tungsten and the experimental lattice parameter. The bicrystal should be periodic in the boundary plane and free of macroscopic stresses.
- Evidence: `/app/outputs/initial_structure.xyz`

### Step 2: Molecular statics relaxation
- Role: process
- Action: Perform molecular statics relaxation of the bicrystal using the Foiles EAM potential. Minimize the total energy with respect to dilational strain normal to the boundary, in‑plane translations of the two grains, and individual displacements of atomic planes (Sutton's variational method).
- Evidence: `/app/outputs/relaxed_structure.xyz`

### Step 3: Compute grain boundary energies
- Role: scored (load-bearing)
- Action: From the initial and relaxed configurations, compute the unrelaxed and relaxed grain boundary energies (J/m²) using the same Foiles EAM potential. Report both values in a JSON file.
- Output file: `/app/outputs/energies.json`
- Format: json
- Contract: {"unrelaxed_gb_energy": "float (J/m^2)", "relaxed_gb_energy": "float (J/m^2)"}
- Scoring: scored by hidden verifier

### Step 4: Characterize ω-phase lattice parameters
- Role: scored
- Action: Analyze the relaxed atomic structure to identify the ω‑phase nanolayer. Measure the in‑plane lattice parameter a (nm), out‑of‑plane lattice parameter c (nm), and the c/a ratio. Report these in a JSON file.
- Output file: `/app/outputs/omega_params.json`
- Format: json
- Contract: {"a": "float (nm)", "c": "float (nm)", "c_ratio": "float (dimensionless)"}
- Scoring: scored by hidden verifier

### Step 5: Compute excess energy profile
- Role: scored
- Action: For each {111} atomic plane near the boundary, compute its excess energy relative to bulk tungsten (J/m²). Provide the plane index (0 at the boundary center, positive on one side, negative on the other) and the excess energy. Output as a JSON array covering at least indices -3 to 3.
- Output file: `/app/outputs/excess_energy_profile.json`
- Format: json
- Contract: [{"plane_index": "int", "excess_energy": "float (J/m^2)"}]
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/energies.json`
- `/app/outputs/omega_params.json`
- `/app/outputs/excess_energy_profile.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### energies.json
- path: `/app/outputs/energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Grain boundary energy in the unrelaxed and relaxed state. Compared to paper‑reported values with tolerance.
- schema:
  - `type`: object
  - `required`:
    - `unrelaxed_gb_energy`: float
    - `relaxed_gb_energy`: float
  - `units`:
    - `unrelaxed_gb_energy`: J/m^2
    - `relaxed_gb_energy`: J/m^2

### omega_params.json
- path: `/app/outputs/omega_params.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Lattice parameters of the hexagonal ω‑phase nanolayer. Compared to paper‑reported values.
- schema:
  - `type`: object
  - `required`:
    - `a`: float
    - `c`: float
    - `c_ratio`: float
  - `units`:
    - `a`: nm
    - `c`: nm

### excess_energy_profile.json
- path: `/app/outputs/excess_energy_profile.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Excess energy of {111} atomic planes near the boundary. The checker verifies the central‑plane energy and oscillatory shape.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`:
      - `plane_index`: int
      - `excess_energy`: float
    - `units`:
      - `excess_energy`: J/m^2

Notes: The relaxed structure evidence files (initial_structure.xyz, relaxed_structure.xyz) are optional and are not scored. Only the JSON outputs are checked.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "unrelaxed_gb_energy": "float",
          "relaxed_gb_energy": "float"
        },
        "units": {
          "unrelaxed_gb_energy": "J/m^2",
          "relaxed_gb_energy": "J/m^2"
        }
      },
      "description": "Grain boundary energy in the unrelaxed and relaxed state. Compared to paper‑reported values with tolerance."
    },
    {
      "file": "omega_params.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "a": "float",
          "c": "float",
          "c_ratio": "float"
        },
        "units": {
          "a": "nm",
          "c": "nm"
        }
      },
      "description": "Lattice parameters of the hexagonal ω‑phase nanolayer. Compared to paper‑reported values."
    },
    {
      "file": "excess_energy_profile.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": {
            "plane_index": "int",
            "excess_energy": "float"
          },
          "units": {
            "excess_energy": "J/m^2"
          }
        }
      },
      "description": "Excess energy of {111} atomic planes near the boundary. The checker verifies the central‑plane energy and oscillatory shape."
    }
  ],
  "notes": "The relaxed structure evidence files (initial_structure.xyz, relaxed_structure.xyz) are optional and are not scored. Only the JSON outputs are checked."
}
```

## How you are scored
A hidden verifier evaluates each of the three scored outputs independently and then combines them into a final reward.  
- `energies.json`: your values are compared to reference grain‑boundary energies determined from a correct implementation of the procedure, with allowed tolerances.  
- `omega_params.json`: the lattice parameters are checked against reference values with appropriate tolerances.  
- `excess_energy_profile.json`: the per‑layer energies are compared point‑by‑point to reference values, and the verifier also checks that the profile exhibits physically plausible features for a grain‑boundary core (e.g., the energies vary non‑monotonically with distance and the central layer is distinct from its neighbors).  
Reporting numbers that match the hidden references is not sufficient if the structural checks are not satisfied. Your reward reflects the overall fidelity of the reproduction.

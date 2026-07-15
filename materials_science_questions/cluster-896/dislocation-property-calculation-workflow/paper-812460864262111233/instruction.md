# Atomistic Simulation of Dislocation Barrier Transitions

## Problem background
In face-centred cubic (FCC) metals, extended dislocation reactions can form sessile barriers that strongly impede slip. One such barrier is a Lomer-Cottrell-like lock comprising a stair-rod dislocation symmetrically placed between two Shockley partials on intersecting {111} planes. When the barrier is subjected to uniaxial tensile loading, the partials are forced toward the stair rod, and the lock undergoes a series of abrupt atomic-scale transitions that restructure its core and eventually invert the entire configuration. Understanding the critical conditions—applied strain and stress—at which these instabilities occur is essential for predicting how such barriers either decompose into mobile dislocations or act as origins for damage and crack nucleation under extreme loads.

## Approach
This task uses classical atomistic simulation to compute the response of the dislocation lock to increasing tensile strain. A cylindrical atomic model of nickel (FCC) is constructed with the prescribed crystallographic orientation and the linear-elastic displacement fields of the three dislocations imposed. The interactions between atoms are described by an embedded-atom method (EAM) potential for Ni. The initial configuration is relaxed to zero-stress equilibrium. A uniaxial tensile strain is then applied along the [100] direction in small increments, while accommodating the Poisson contraction according to the anisotropic elastic stiffness of the crystal. After each strain increment the structure is re-relaxed. Post-processing of the resulting trajectory involves computing the disregistry across the relevant slip planes to locate the dislocation cores, identifying the abrupt transitions that mark core rearrangements, and extracting the corresponding applied strain and, for the first transition, the tensile stress. The state of the stair-rod dislocation after the final transition is determined from the core structure.

## Reproduction target
Produce a single JSON file `transition_results.json` at the path `/app/outputs/transition_results.json` that contains:
- `transition_strains`: an array of three floating-point numbers, in percent, representing the applied tensile strain ε₁₁ at which each of the three abrupt lock transitions occurs.
- `first_transition_stress_GPa`: the tensile stress σ₁₁ (in GPa) corresponding to the first transition, computed from the elastic stiffness tensor and the recorded strain.
- `final_stair_rod_burgers`: a string identifying the Burgers vector of the stair-rod dislocation after the third transition, expressed in Thompson tetrahedron notation or an equivalent crystallographic notation (e.g., `1/3 a[100]` with appropriate sign and direction).

The values must be derived solely from the atomistic simulation and disregistry analysis performed in the preceding steps. The file must match the output schema: `{"transition_strains": [float, float, float], "first_transition_stress_GPa": float, "final_stair_rod_burgers": string}`.

## Assets

- Angelo et al. (1995) EAM potential for Ni: https://www.ctcms.nist.gov/potentials/entry/Ni/
- LAMMPS molecular dynamics package: https://www.lammps.org

## Workflow steps

### Step 1: Build and relax initial barrier configuration
- Role: process
- Action: Construct a cylindrical atomistic model of an extended dislocation barrier in nickel (FCC) consisting of a 1/3 a[100] stair-rod dislocation symmetrically located between two Shockley partials (Bδ and Dβ) on intersecting {111} planes, with the prescribed crystallographic orientation. Impose the linear-elastic displacement fields of the three dislocations, then relax the configuration to zero-stress equilibrium using conjugate gradient or an energy quench. Save the relaxed atomic configuration.
- Evidence: `/app/outputs/initial_relaxed.dump`

### Step 2: Incremental uniaxial tensile loading and relaxation
- Role: process
- Action: Apply uniaxial tensile strain ε11 along [100] in small increments (0.1–0.2%) from 0% to at least 6%. At each step, accommodate the Poisson contraction according to the elastic stiffness matrix, then relax the atomic configuration (conjugate gradient or energy quench). Record the relaxed coordinates of each strain step as a trajectory file.
- Evidence: `/app/outputs/strain_trajectory.xyz`

### Step 3: Disregistry analysis and transition parameter extraction
- Role: scored (load-bearing)
- Action: Post-process the strain trajectory to compute the disregistry across the (111) and (1-1-1) slip planes. Identify the three abrupt transitions by monitoring the positions of the Shockley partials and the stair rod. For each transition, record the applied elastic strain ε11. For the first transition, compute the corresponding tensile stress using the elastic stiffness matrix and the recorded strain. After the third transition, determine the Burgers vector of the stair rod in Thompson tetrahedron notation (or equivalent). Output a single JSON file containing the three transition strains (in %), the first-transition stress (in GPa), and the final stair-rod Burgers vector (as a string).
- Output file: `/app/outputs/transition_results.json`
- Format: json
- Contract: {"transition_strains": [float, float, float], "first_transition_stress_GPa": float, "final_stair_rod_burgers": string}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/transition_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### transition_results.json
- path: `/app/outputs/transition_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The three transition strain thresholds (in %), the tensile stress at the first transition (in GPa), and the Burgers vector of the stair-rod dislocation after the third transition (in Thompson tetrahedron notation or equivalent).
- schema:
  - `type`: object
  - `required`:
    - `transition_strains`: array of three floats (percent)
    - `first_transition_stress_GPa`: float
    - `final_stair_rod_burgers`: string

Notes: The scored artifact contains the headline quantities from the atomistic simulation under increasing uniaxial strain. The checker compares the reported values to the paper's reported values with appropriate tolerances; exact string match is required for the Burgers vector.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "transition_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "transition_strains": "array of three floats (percent)",
          "first_transition_stress_GPa": "float",
          "final_stair_rod_burgers": "string"
        }
      },
      "description": "The three transition strain thresholds (in %), the tensile stress at the first transition (in GPa), and the Burgers vector of the stair-rod dislocation after the third transition (in Thompson tetrahedron notation or equivalent)."
    }
  ],
  "notes": "The scored artifact contains the headline quantities from the atomistic simulation under increasing uniaxial strain. The checker compares the reported values to the paper's reported values with appropriate tolerances; exact string match is required for the Burgers vector."
}
```

## How you are scored
A hidden verifier will inspect `/app/outputs/transition_results.json` and compare each of the five reported quantities—the three transition strains, the first-transition stress, and the final stair-rod Burgers vector—against a pre-determined reference (derived from published atomistic results under the same conditions). The comparison allows for tolerances that account for the expected variation between independent atomistic implementations (different code, relaxation settings, or slight differences in model size). Each correctly reported quantity contributes to the final score. The Burgers vector is matched as a string (case- and whitespace-insensitive). Rewards are proportional to the number of quantities that fall within the acceptance windows; the verifier does not require exact reproduction of any single published table entry, only that the values lie within the physically reasonable range attested by the reference simulation. Partial credit is possible.

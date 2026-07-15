# Sequential Lamination Crystal Plasticity: FCC Shear Stress-Strain Computation

## Problem background
Ductile single crystals develop characteristic lamellar dislocation structures when they undergo large plastic strains. These microstructures, consisting of nested dislocation walls and alternating lamellae, are known to influence the macroscopic mechanical response—in particular, they can lead to a softer hardening behavior compared to what is predicted under the assumption of uniform deformation with multiple active slip systems. The objective is to compute the effective macroscopic resolved shear stress as a function of the applied shear strain for an fcc single crystal subjected to simple shear, using a micromechanical theory that explicitly builds these evolving microstructures. The resulting stress-strain curve will be compared to the response of the same crystal deforming uniformly (double slip without microstructure), to determine the effect of laminate formation on the hardening response.

## Approach
The reproduction relies on the local sequential-lamination theory for finite-deformation single-crystal plasticity. The core idea is to allow the crystal to develop a deformation microstructure in the form of a binary-tree laminate, rather than deforming uniformly. Each leaf of the tree is a region of the crystal that deforms homogeneously and obeys a conventional crystal plasticity constitutive law. Interior nodes represent composite lamellae whose deformation is the volume-average of their two children; the children must satisfy Hadamard's rank-one compatibility condition, characterized by a polarization vector and an interface normal.

The local crystal plasticity model uses an elastic energy with cubic symmetry, 12 fcc slip systems defined by the standard Schmid–Boas vectors, and a hardening law that includes latent hardening (parameter q) and a self-hardening function of the sesc-hype form. The constitutive update for a given increment of deformation is performed implicitly, integrating the flow rule with an exponential map for the plastic deformation gradient and returning the first Piola–Kirchhoff stress and algorithmic tangent moduli.

A binary tree data structure organizes the laminate. Starting from the macroscopic deformation gradient at the root, the deformation of every node is expressed in terms of the polarization vectors of the interior nodes and the geometric parameters (volume fractions and interface normals) that were set at the moment the interface was created. The stresses are computed recursively from the leaves upward, and the interfacial traction equilibrium equations (continuity of the traction vector across each lamellar interface) form a system of nonlinear equations for the polarization vectors. These are solved by a Newton–Raphson iteration with line search, using the algorithmic tangents.

The laminate may refine during deformation: at each leaf a Hill–Hadamard branching analysis is performed. When the acoustic tensor of the leaf becomes non-positive definite for some normal direction, the leaf bifurcates into two new leaves of equal volume fraction with that normal direction as the interface, creating a new rank-one laminate. The newly created leaves are then allowed to slip independently.

The macroscopic loading is a simple shear on the (001) plane in the [110] direction: the deformation gradient is $\mathbf{F} = \mathbf{I} + \gamma \, \mathbf{s} \otimes \mathbf{m}$ with $\mathbf{s} = [1\bar{1}0]/\sqrt{2}$ and $\mathbf{m} = [001]$. The shear strain $\gamma$ is increased from 0 to at least 0.1 in small increments. At each increment the laminate tree is updated, branching may occur if instability is detected, the equilibrium equations are solved, and the macroscopic resolved shear stress $\tau = \mathbf{P} : (\mathbf{s} \otimes \mathbf{m})$ is recorded, where $\mathbf{P}$ is the macroscopic first Piola–Kirchhoff stress tensor obtained from the root of the laminate tree.

## Reproduction target
Produce a stress-strain curve for an fcc single crystal subjected to simple shear on the (001) plane in the [110] direction, using the local sequential-lamination theory described above. The crystal's elastic constants, initial critical resolved shear stress, saturation strength, initial hardening rate, and latent hardening parameter are publicly available material constants for an Al–Cu alloy (typical values: c11=168.4 GPa, c12=121.4 GPa, c44=75.4 GPa, τ0=100 MPa, τs=180 MPa, an appropriate initial hardening rate h0 for the sech² law, and q=1.4). The primary deliverable is a CSV file (`stress_strain_curve.csv`) with columns `shear_strain` (dimensionless) and `shear_stress` (MPa). The file must contain at least 20 data points covering the strain range from γ=0 up to at least 0.1. Additionally, you should compute and record (in the same or a separate artifact) the response that would be obtained if the crystal were constrained to deform uniformly (i.e., without the formation of laminates, so that all regions experience the same macroscopic deformation and activate the same slip systems). This uniform-deformation curve serves as a baseline to illustrate the effect of microstructure formation on the hardening behavior.

## Assets

- FCC slip system vectors (Schmid and Boas)
- Elastic constants and hardening parameters for Al-Cu alloy
- NumPy and SciPy: numpy scipy

## Workflow steps

### Step 1: Implement crystal plasticity constitutive update
- Role: process
- Action: Implement the local single-crystal plasticity model: define cubic elastic stiffness tensor from the given constants, define the 12 fcc slip systems, implement the Hutchinson-Pierce hardening model with the prescribed parameters using the sech^2 law, and implement the implicit constitutive update using the exponential map for plastic deformation. The update must return stress and algorithmic tangent moduli for a given deformation gradient and previous state.
- Evidence: none

### Step 2: Implement laminate tree, branching analysis, and Newton-Raphson equilibration
- Role: process
- Action: Build a binary-tree data structure for sequential laminates. Implement recursive averaging, Hadamard rank-one compatibility, and leaf-deformation calculation from polarization vectors. Implement Hill-Hadamard branching analysis: for each leaf, compute the acoustic tensor and trigger branching when the determinant becomes non-positive. Implement a Newton-Raphson solver with line search to solve interfacial traction equilibrium for the polarization vectors of all interior nodes, using a recursive tree traversal.
- Evidence: none

### Step 3: Simulate simple shear and output stress-strain curve
- Role: scored (load-bearing)
- Action: Set up initial homogeneous state (plastic deformation = identity, zero slip, critical stresses = initial values). Apply macroscopic simple shear deformation F = I + γ s⊗m with s = [110]/√2 and m = [001]. Increment shear strain γ from 0 to 0.1 in at least 50 steps. For each increment: compute macroscopic deformation; if only one leaf, perform branching analysis and create a rank-1 laminate if Hill-Hadamard condition is met; equilibrate the laminate using the solver from step_2 to obtain macroscopic stress tensor; compute macroscopic resolved shear stress τ = P : (s⊗m). Record (γ, τ) pairs and output the microstructured curve.
- Output file: `/app/outputs/stress_strain_curve.csv`
- Format: csv
- Contract: CSV with a header row and two columns: shear_strain (numeric, dimensionless) and shear_stress (numeric, MPa).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/stress_strain_curve.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### stress_strain_curve.csv
- path: `/app/outputs/stress_strain_curve.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Macroscopic resolved shear stress vs. shear strain curve for an fcc crystal under simple shear on (001)[110], computed with the local sequential lamination theory. The file must contain at least 20 data points covering the strain range up to at least 0.1.
- schema:
  - `type`: table
  - `required_columns`: `shear_strain`, `shear_stress`
  - `units`:
    - `shear_strain`: dimensionless
    - `shear_stress`: MPa

Notes: The agent's curve will be compared to a hidden reference curve. The evaluation also checks that the curve exhibits softening relative to the uniform double-slip response.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "stress_strain_curve.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "shear_strain",
          "shear_stress"
        ],
        "units": {
          "shear_strain": "dimensionless",
          "shear_stress": "MPa"
        }
      },
      "description": "Macroscopic resolved shear stress vs. shear strain curve for an fcc crystal under simple shear on (001)[110], computed with the local sequential lamination theory. The file must contain at least 20 data points covering the strain range up to at least 0.1."
    }
  ],
  "notes": "The agent's curve will be compared to a hidden reference curve. The evaluation also checks that the curve exhibits softening relative to the uniform double-slip response."
}
```

## How you are scored
A hidden verifier independently scores each submitted artifact. For the main stress-strain curve (`stress_strain_curve.csv`), the verifier will:

1. Compare your reported `shear_stress` values to a reference curve derived from the published data, evaluated at a common set of strain points. The comparison uses a relative L2 error metric; the submission passes if the error is below a predetermined tolerance.
2. Check a structural property: the shear stress at the maximum strain (e.g., γ = 0.1) must be lower than a given fraction of the shear stress obtained from a corresponding uniform-deformation simulation, thereby verifying that the laminate computation captures the softening effect of the microstructure.

The overall reward is a weighted combination of the results of these checks. Providing a curve that merely matches the paper's numbers without running the actual laminate solver will not satisfy the structural requirement. The uniform-deformation curve (or a summary of it) may be submitted as an additional artifact and is expected for the structural verification to be meaningful.

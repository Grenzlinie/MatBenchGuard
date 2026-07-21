# Spin-Tri-layer Magnetisation Profiles via Effective-Field 1-ACA

## Problem background
Understanding the magnetisation distribution in thin-film trilayer structures with mixed-spin interfaces is crucial for interpreting giant magnetoresistance (GMR) effects and for designing spintronic devices. In particular, when the interface region comprises a stochastic mixture of spin-1 and spin-½ atoms, the competition among exchange interactions, thermal fluctuations, and site disorder can give rise to complex behaviour such as enhanced interface magnetism or reversals in the magnetisation depth profile. The goal of this work is to compute, from first principles, the temperature-dependent magnetisation per atomic layer (magnetisation depth profile) and the phase boundaries that separate regimes where interface magnetisation dominates over bulk magnetisation. These quantities are to be obtained for a series of symmetric trilayers of the form A(n)/A_c B_{1-c}/B(p)/A_c B_{1-c}/A'(m) on a simple cubic lattice by solving the self-consistency equations of the effective-field one-atom cluster approximation.

## Approach
The magnetic system is described by a local Ising Hamiltonian that includes nearest-neighbour exchange interactions J^AA, J^AB, J^BB, and a uniaxial single-ion anisotropy D for spin-1 sites. The Hamiltonian is extended with occupation operators that encode the stochastic occupancy of each site by a spin-1 (A) or spin-½ (B) atom, with a site- and layer-dependent concentration c_v. The thermodynamics are treated within an effective-field one-atom cluster approximation (1-ACA). Starting from the exact Callen identities for spin-½ and spin-1 operators and applying the Matsudaira first-order decoupling to factorise higher-order spin correlations, one obtains a closed system of coupled nonlinear algebraic equations for two quantities in each atomic plane v: the magnetisation m_v = ⟨S_v⟩ and the quadrupolar moment q_v = ⟨(S_v^A)²⟩. The equations depend on the number of nearest neighbours in the same plane and in adjacent planes, as well as on the local concentrations and exchange constants. Solving these 2N equations self-consistently (by fixed-point iteration or a Newton-type method) for given layer thicknesses, exchange parameters, anisotropy, interface concentration c, and reduced temperature y = k_B T / J yields the layer-resolved magnetisations. The magnetisation depth profile is the set {m_v} across all layers. To construct a phase boundary, the condition that the average magnetisation of the interface layers equals the magnetisation at the centre of the magnetic overlayer is solved for (c, J^AB) pairs at fixed temperature.

## Reproduction target
You must implement the 1-ACA solver outlined above and use it to produce two scored artifacts:

1. Magnetisation depth profile: For the symmetric trilayer A(6)/I/B(3)/I/A'(6) with a double-layer interface (l_I=4), exchange couplings J^AA = J, J^AB = 4J, J^BB = J/10, uniaxial anisotropy D = J, and interface A-spin concentration c = 0.8, compute the magnetisation m_v of every atomic plane at reduced temperatures y = 0.5, 1.5, 2.5, 3.5, 4.5. Write the results to a CSV file with columns (layer_index, reduced_temperature, concentration_c, m_v).

2. Phase diagram boundary: For the trilayer A(5)/I/B(3)/I/A'(5) with a double-layer interface, where the A and A' films contain 10% B spins (i.e., A concentration 0.9 in those films, denoted x=0.1), scan the interface concentration c from 0 to 1 and the exchange ratio J^AB/J to locate, for each reduced temperature y = 1.5, 2.0, 2.2, 2.5, the set of points (c, J^AB/J) at which the average magnetisation of the two interface layers equals the magnetisation of the central layer of the magnetic overlayer (m_3 in this geometry). Output these boundary points as a CSV with columns (reduced_temperature, concentration_c, J_AB_over_J).

## Assets

- SciPy: https://pypi.org/project/scipy/
- NumPy: https://pypi.org/project/numpy/

## Workflow steps

### Step 1: Implement the effective-field 1-ACA solver
- Role: process
- Action: Implement the Hamiltonian (Eq. 1) and the system of 2(N) nonlinear algebraic self-consistency equations for layered magnetisation m_v and autocorrelation q_v derived from the Callen-equation extension and Matsudaira first-order decoupling for a stochastic mixed-spin Ising trilayer on a simple cubic lattice. The solver should take as input: layer thicknesses n, p, m, interface plane counts (l_I), exchange constants J^AA, J^AB, J^BB, anisotropy D, interface concentration c, and reduced temperature y. Solve the equations numerically to self-consistency (e.g., by iterative fixed-point or Newton-Krylov methods) to obtain m_v for all planes.
- Evidence: `/app/outputs/solver_evidence.log`

### Step 2: Generate magnetisation depth profile CSV
- Role: scored (load-bearing)
- Action: Using the solver from step 01, compute the magnetisation depth profile for the symmetric trilayer A(6)/I/B(3)/I/A'(6) with DLI (l_I=4), exchange parameters J^AA=J, J^AB=4J, J^BB=J/10, and uniaxial anisotropy D=J. The concentration of A-spins at the interface c=0.8. Compute profiles at reduced temperatures y = 0.5, 1.5, 2.5, 3.5, 4.5. For each temperature, output the layer index and the corresponding m_v value. Write a CSV file with columns: layer_index, reduced_temperature, concentration_c, m_v.
- Output file: `/app/outputs/magnetisation_depth_profile.csv`
- Format: csv
- Contract: CSV with columns: layer_index (int), reduced_temperature (float), concentration_c (float), m_v (float). Rows correspond to each layer and temperature combination.
- Scoring: scored by hidden verifier

### Step 3: Generate phase diagram boundary CSV
- Role: scored
- Action: Using the solver from step 01, for the trilayer A(5)/I/B(3)/I/A'(5) with DLI, where the A films contain 10% B spins (x=0.1, i.e., concentration of A is 0.9 within the film), scan the (c, J^AB) parameter space. For each reduced temperature y=1.5, 2.0, 2.2, 2.5, find the boundary points where the average interface magnetisation (mean of m_0 and m_0' for DLI) equals the magnetisation at the centre of the magnetic overlayer (m_3 in this geometry). Output a set of (c, J^AB) points that lie on this boundary. Write a CSV file with columns: reduced_temperature, concentration_c, J_AB_over_J.
- Output file: `/app/outputs/phase_diagram_boundary.csv`
- Format: csv
- Contract: CSV with columns: reduced_temperature (float), concentration_c (float), J_AB_over_J (float). Points should cover the full range of c from 0 to 1 where a boundary exists.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/magnetisation_depth_profile.csv`
- `/app/outputs/phase_diagram_boundary.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### magnetisation_depth_profile.csv
- path: `/app/outputs/magnetisation_depth_profile.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Magnetisation depth profile for A(6)/I/B(3)/I/A'(6) with c=0.8, J^AB=4J, J^BB=J/10, D=J at reduced temperatures y=0.5, 1.5, 2.5, 3.5, 4.5.
- schema:
  - `type`: table
  - `required_columns`: `layer_index`, `reduced_temperature`, `concentration_c`, `m_v`

### phase_diagram_boundary.csv
- path: `/app/outputs/phase_diagram_boundary.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Phase boundary points (c, J^AB) where interface magnetisation equals bulk magnetisation for A(5)/I/B(3)/I/A'(5) with A films containing 10% B (x=0.1), at temperatures y=1.5, 2.0, 2.2, 2.5.
- schema:
  - `type`: table
  - `required_columns`: `reduced_temperature`, `concentration_c`, `J_AB_over_J`

Notes: Both artifacts are compared against hidden reference values extracted from the paper's figures; tolerances are not public. The agent must implement the effective-field 1-ACA solver from first principles using the described method (Hamiltonian, Callen equations, Matsudaira decoupling) — no pretrained model or precomputed data is provided.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "magnetisation_depth_profile.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "layer_index",
          "reduced_temperature",
          "concentration_c",
          "m_v"
        ]
      },
      "description": "Magnetisation depth profile for A(6)/I/B(3)/I/A'(6) with c=0.8, J^AB=4J, J^BB=J/10, D=J at reduced temperatures y=0.5, 1.5, 2.5, 3.5, 4.5."
    },
    {
      "file": "phase_diagram_boundary.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "reduced_temperature",
          "concentration_c",
          "J_AB_over_J"
        ]
      },
      "description": "Phase boundary points (c, J^AB) where interface magnetisation equals bulk magnetisation for A(5)/I/B(3)/I/A'(5) with A films containing 10% B (x=0.1), at temperatures y=1.5, 2.0, 2.2, 2.5."
    }
  ],
  "notes": "Both artifacts are compared against hidden reference values extracted from the paper's figures; tolerances are not public. The agent must implement the effective-field 1-ACA solver from first principles using the described method (Hamiltonian, Callen equations, Matsudaira decoupling) — no pretrained model or precomputed data is provided."
}
```

## How you are scored
A hidden verifier will independently read your CSV files and compare each of them against reference values that were derived from the original published study under the same conditions. The verifier checks the magnetisation depth profile for correctness of the layer-resolved magnetisation values and their overall shape, and checks the phase boundary points for agreement in the (c, J^AB) plane. The comparison tolerances are not disclosed, but they account for the expected numerical spread that arises from legitimate differences in solver implementation and initial guess. Each scored artifact contributes a portion (0.5 weight) to the final reward, which is a number between 0 and 1. Reporting the correct numbers is not enough on its own—the artifacts must be produced by repeatedly solving the self-consistency equations as specified in the workflow steps. The verifier will only accept CSV files that follow the exact column names and order described in the workflow steps.

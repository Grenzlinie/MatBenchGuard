# Geometry Optimization and Binding Energy of Small Silicon Clusters Using an Empirical Potential

## Problem background
Understanding the structures and stabilities of small silicon clusters is important for bridging molecular and bulk behavior. Empirical potentials derived from solid-state properties provide a computationally efficient way to explore cluster geometries and energetics. This task reproduces the geometry optimization and binding energy calculation for silicon clusters with 2 to 8 atoms using a two- plus three-body empirical potential whose parameters were previously determined from bulk silicon data.

## Approach
The total potential energy of a silicon cluster is expressed as a sum of two-body and three-body terms. The two-body term is
    V_ij^(2) = -D(1 + a2 ρ_ij) exp(-a2 ρ_ij)
where ρ_ij = (r_ij - r_e) / r_e with r_e the equilibrium bond length.

For a triple of atoms i, j, k, the three-body term involves symmetry coordinates Q obtained via an orthogonal transformation from the reduced distances ρ:
    V_ijk^(3) = D P(Q1, Q2, Q3) exp(-a3 Q1)
with the transformation matrix
        ( √(1/3)  √(1/3)  √(1/3)   )
    U = (    0   √(1/2) -√(1/2)  )
        ( √(2/3) -√(1/6) -√(1/6)  )
and P is a totally symmetric quartic polynomial:
    P(Q1, Q2, Q3) = c0 + c1 Q1 + c2 Q1^2 + c3(Q2^2+Q3^2) + c4 Q1^3 + c5 Q1(Q2^2+Q3^2)
                   + c6(Q3^3 - 3 Q3 Q2^2) + c7 Q1^4 + c8 Q1^2(Q2^2+Q3^2)
                   + c9(Q2^2+Q3^2)^2 + c10 Q1(Q3^3 - 3 Q3 Q2^2).

The parameters are fixed as follows:

| Parameter | Value   |
|-----------|---------|
| a2        | 6.50    |
| a3        | 6.50    |
| D (eV)    | 2.918   |
| r_e (Å)   | 2.389   |
| c0        | 3.598   |
| c1        | -11.609 |
| c2        | 13.486  |
| c3        | -18.174 |
| c4        | -5.570  |
| c5        | 79.210  |
| c6        | -6.458  |
| c7        | 23.383  |
| c8        | -111.809|
| c9        | 9.705   |
| c10       | 38.297  |

For each cluster size n=2,…,8, you will generate random initial Cartesian coordinates, then minimize the total energy with respect to all atomic positions using a quasi-Newton or conjugate-gradient optimizer (e.g., SciPy's L-BFGS-B). Run multiple random starts to locate the global minimum. From the optimized structure, compute the binding energy per atom as -V_total / n, and determine the point-group symmetry. Verify that the stationary point is a true minimum by checking that the forces are below 1e-4 eV/Å and that the numerical Hessian has only positive eigenvalues.

## Reproduction target
Produce for each cluster size n = 2,3,4,5,6,7,8 the global-minimum structure's point-group symmetry, its binding energy per atom in eV, and the Cartesian coordinates (element 'Si', x, y, z in Å). Write these results as a JSON array in /app/outputs/step_01_cluster_details.json. The data must allow a verifier to recompute the total energy from the coordinates and derive the binding energy.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Geometry optimization and binding energy of Si₂–Si₈ clusters
- Role: scored (load-bearing)
- Action: Implement the total potential energy function for silicon clusters from the two‑body term V_ij^(2) = –D(1 + a₂ρ_ij)exp(–a₂ρ_ij) and the three‑body term V_ijk^(3) = D·P(Q₁,Q₂,Q₃)·exp(–a₃Q₁), where the coordinates Q are obtained by the orthogonal transformation U from the reduced distances ρ, and P is the totally symmetric quartic polynomial given in the instruction (all parameters D, a₂, a₃, rₑ, c₀…c₁₀ are provided). For each cluster size n = 2,…,8: (i) generate several random initial Cartesian configurations; (ii) perform local energy minimization of all atomic coordinates using a quasi‑Newton or conjugate‑gradient optimizer (e.g., SciPy’s L‑BFGS‑B) until forces are below 1e‑4 eV/Å; (iii) repeat from enough random starts to locate the global minimum; (iv) verify that the stationary point is a true minimum by checking that the numerical Hessian has only positive eigenvalues; (v) compute the binding energy per atom as –V_total/n. Report the point‑group symmetry, the binding energy per atom in eV, and the Cartesian coordinates (element ‘Si’, x, y, z in Å) of the global‑minimum structure in step_01_cluster_details.json.
- Output file: `/app/outputs/step_01_cluster_details.json`
- Format: json
- Contract: JSON array of objects. Each object: {"n_atoms": int, "symmetry": string, "binding_energy_per_atom": float (eV), "coordinates": [["Si", x, y, z], ...]} where coordinates are in Ångströms.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_cluster_details.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_cluster_details.json
- path: `/app/outputs/step_01_cluster_details.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Global‑minimum structures, symmetries, and binding energies per atom for Si₂–Si₈. The checker recomputes the total potential energy from the submitted coordinates and derives the binding energy; it also verifies the symmetry against known global‑minimum symmetries and checks that the structure is a true minimum.
- schema:
  - `type`: array
  - `items`:
    - `n_atoms`: integer
    - `symmetry`: string
    - `binding_energy_per_atom`: float (eV)
    - `coordinates`: array of ["Si", x_Å, y_Å, z_Å]

Notes: The paper reports binding energies per atom and symmetries for Si₂–Si₈ in Table 2. Only the small‑cluster part (n=2–8) is reproduced; larger shell‑cluster and fully‑optimised results (n>8) are excluded per the taskability scope. The checker will compare the agent's computed binding energy to the paper's values with a tolerance and independently confirm the symmetry.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_cluster_details.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "array",
        "items": {
          "n_atoms": "integer",
          "symmetry": "string",
          "binding_energy_per_atom": "float (eV)",
          "coordinates": "array of [\"Si\", x_Å, y_Å, z_Å]"
        }
      },
      "description": "Global‑minimum structures, symmetries, and binding energies per atom for Si₂–Si₈. The checker recomputes the total potential energy from the submitted coordinates and derives the binding energy; it also verifies the symmetry against known global‑minimum symmetries and checks that the structure is a true minimum."
    }
  ],
  "notes": "The paper reports binding energies per atom and symmetries for Si₂–Si₈ in Table 2. Only the small‑cluster part (n=2–8) is reproduced; larger shell‑cluster and fully‑optimised results (n>8) are excluded per the taskability scope. The checker will compare the agent's computed binding energy to the paper's values with a tolerance and independently confirm the symmetry."
}
```

## How you are scored
The verifier will independently recompute the total potential energy for each cluster from your submitted coordinates using the same potential function, derive the binding energy per atom, and compare it to a hidden reference. It will also verify that the reported symmetry matches the known global-minimum symmetry for each size, and that the structure is a true local minimum (forces near zero and positive-definite Hessian). Your output must strictly follow the required schema. Partial credit is assigned per cluster, and the combination of these checks yields the final reward.

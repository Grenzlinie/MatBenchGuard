# First-principles bond stiffness and size-dependent stiffening of carbon nanostructures

## Problem background
The mechanical stiffness of carbon nanostructures such as nanodiamonds and fullerenes is difficult to quantify unambiguously. In bulk crystals, stiffness is characterized by the bulk modulus B0, but for nanoparticles there is no unique way to define volume, and different choices lead to conflicting values. This task explores an alternative volume‑independent quantity — the average bond stiffness ⟨k⟩0 — defined as the second derivative of total energy with respect to average bond length, normalized by the number of bonds. The central question is how ⟨k⟩0 varies among different carbon systems: bulk diamond, graphene, bare nanodiamonds, hydrogenated nanodiamonds, and C60 fullerene. Additionally, the task investigates whether ⟨k⟩0 can be reliably estimated from the relaxed atomic geometry alone, using reference bond‑stiffness vs bond‑length curves derived from the pure sp³ (diamond) and pure sp² (graphene) environments.

## Approach
The approach consists of two complementary calculations. First, the average bond stiffness is computed directly by applying small isotropic strains to each relaxed structure, performing constrained geometry optimizations, and extracting the curvature of the total energy with respect to the average bond length via finite differences. For periodic systems (bulk diamond and graphene) the bulk or layer modulus is also obtained by fitting an equation of state. Second, the relaxed geometry of each nanostructure is analyzed: each bond is assigned a hybridization type (sp² or sp³) based on its local environment, and its individual stiffness is read from the reference k(l) curves. The arithmetic average over all bonds gives an estimated ⟨k⟩0_est, which is compared to the directly computed ⟨k⟩0. The workflow covers six specified carbon systems to span the range from pure sp³ to pure sp² bonding, with and without surface passivation, and includes both periodic crystals and finite clusters.

## Reproduction target
Reproduce the average bond stiffness ⟨k⟩0 (in N/m) for bulk diamond, graphene, a small bare nanodiamond (≈50–150 carbon atoms), a medium bare nanodiamond (≈500–700 carbon atoms), a hydrogenated version of the medium nanodiamond, and C60 fullerene. Determine the ordering of ⟨k⟩0 among these systems, including the effect of nanodiamond size and hydrogenation. For every system, compute ⟨k⟩0 both directly (from strained configurations) and via the geometry‑based estimation method; verify that the ratio ⟨k⟩0_est / ⟨k⟩0_direct falls within [0.9, 1.1]. For bulk diamond and graphene, also report the equilibrium lattice constant and bulk modulus (in GPa).

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- ASE (Atomic Simulation Environment): https://wiki.fysik.dtu.dk/ase/
- PBE pseudopotentials for carbon: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: DFT reference calculations for bulk diamond and graphene
- Role: process
- Action: Perform DFT (Quantum ESPRESSO) calculations for bulk diamond (face-centered cubic) and graphene (hexagonal 2D) to relax geometries, obtain equilibrium lattice constants, bulk modulus B0 (diamond) and layer modulus γ0 (graphene), bond stiffness <k>0, and generate reference bond stiffness vs bond length curves k(l) for sp3 and sp2 carbon over a range of bond lengths (e.g., 1.3–1.8 Å) by fitting total energy vs strain data.
- Evidence: `/app/outputs/references.json`

### Step 2: Generate initial atomic structures for nanostructures
- Role: process
- Action: Using ASE, generate initial coordinates for: (1) a small bare nanodiamond cluster (e.g., C54 cuboctahedral or cubic) carved from bulk diamond lattice; (2) a medium bare nanodiamond cluster (~500–700 atoms, e.g., C660); (3) a hydrogenated version of the medium nanodiamond by saturating surface dangling bonds; (4) a C60 fullerene molecule (icosahedral). Write each as a separate XYZ file.
- Evidence: none

### Step 3: DFT relaxation of all nanostructures
- Role: process
- Action: For each nanostructure (small ND, medium ND, hydro ND, C60), perform DFT geometry relaxation using Quantum ESPRESSO with an appropriate supercell and vacuum to avoid periodic interactions (Γ-point sampling). Save relaxed atomic coordinates and total energies.
- Evidence: none

### Step 4: Apply isotropic strain and collect energy/bond-length data
- Role: process
- Action: For each of the six systems (diamond, graphene, small ND, medium ND, hydro ND, C60), starting from the relaxed geometry, apply uniform isotropic linear strains ε = ±0.015, ±0.03. For each strained state, perform constrained geometry optimization (freezing surface atoms for non-periodic clusters) and record the total energy, total number of bonds Nb, and average bond length ⟨l⟩. Save these data in a structured format.
- Evidence: none

### Step 5: Compute average bond stiffness, estimate from geometry, and compile results
- Role: scored (load-bearing)
- Action: For each system, compute direct ⟨k⟩0 from the energy vs average bond length data using finite-difference second derivative. Compute B0 for periodic systems (bulk diamond and graphene) by fitting a Birch–Murnaghan equation of state. Using the relaxed geometry of each system, assign sp²/sp³ hybridization based on coordination and angles, then use the reference bond stiffness vs bond length curves to estimate individual bond stiffnesses and obtain ⟨k⟩0_est. Compute ratio = k_est / k_direct. Write results.json with entries for bulk_diamond, graphene, nd_small, nd_medium, nd_hydro, c60.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: A JSON object with keys: bulk_diamond, graphene, nd_small, nd_medium, nd_hydro, c60. Each value is an object with fields: num_atoms (int), a0 (float, Å, only for periodic systems), B0 (float, GPa, only if computed), k_direct (float, N/m), k_est (float, N/m), ratio_k (float, k_est/k_direct).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Provides the directly computed and estimated average bond stiffnesses for all six systems, as well as bulk moduli for the periodic reference systems. The checker compares these values to hidden paper‑reported gold and verifies required trends.
- schema:
  - `type`: object
  - `description`: JSON object with keys: bulk_diamond, graphene, nd_small, nd_medium, nd_hydro, c60. Each value is an object containing: num_atoms (integer), a0 (float, angstrom, optional), B0 (float, GPa, optional), k_direct (float, N/m), k_est (float, N/m), ratio_k (float).

Notes: The task reproduces a minimal subset of the paper's structures; the full set of 20 nanodiamonds and 7 fullerenes is not required. Bulk modulus is computed only for the periodic reference systems; for nanoclusters the volume definition is ambiguous and B0 may be omitted. The focus is on the primary claim and the validation of the geometry‑based estimation of <k>0.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "description": "JSON object with keys: bulk_diamond, graphene, nd_small, nd_medium, nd_hydro, c60. Each value is an object containing: num_atoms (integer), a0 (float, angstrom, optional), B0 (float, GPa, optional), k_direct (float, N/m), k_est (float, N/m), ratio_k (float)."
      },
      "description": "Provides the directly computed and estimated average bond stiffnesses for all six systems, as well as bulk moduli for the periodic reference systems. The checker compares these values to hidden paper‑reported gold and verifies required trends."
    }
  ],
  "notes": "The task reproduces a minimal subset of the paper's structures; the full set of 20 nanodiamonds and 7 fullerenes is not required. Bulk modulus is computed only for the periodic reference systems; for nanoclusters the volume definition is ambiguous and B0 may be omitted. The focus is on the primary claim and the validation of the geometry‑based estimation of <k>0."
}
```

## How you are scored
A hidden verifier reads the submitted results.json and evaluates each system independently. For bulk diamond and graphene, your computed lattice constants, bulk moduli, and directly computed average bond stiffnesses are compared against established reference values with appropriate tolerances. For all systems the directly computed and geometry‑estimated ⟨k⟩0 values are checked for internal consistency (ratio within bounds). The verifier also examines the relative ordering of ⟨k⟩0 across the systems — for example, whether bare nanodiamonds are stiffer or softer than bulk diamond, how stiffness changes with nanodiamond size, and the effect of hydrogenation — and compares the observed trends with the known behavior of these materials. The final reward is a weighted combination of these checks: absolute accuracy for the reference periodic systems, verification of the required structural trends, the quality of the geometry‑based estimation, and the placement of the fullerene result relative to diamond and graphene. Reporting paper‑matching numbers without performing the full DFT workflow will not score well.

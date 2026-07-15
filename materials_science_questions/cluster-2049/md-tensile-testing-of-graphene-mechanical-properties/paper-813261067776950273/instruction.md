# Atomistic energy release rates of a cracked graphene sheet via local force and global energy methods

## Problem background
Predicting fracture in atomically thin materials such as graphene is crucial for designing reliable nanostructures. A central quantity is the elastic energy release rate, which indicates how much energy is available to grow a crack. In atomistic simulations, this rate can be extracted in two distinct ways: a global energy method that relies on the total potential energy of the entire system, and a local force method that uses only the interatomic forces and displacements at the crack tip. Validating the local method against the global method on a well-characterised system is an important step toward scalable fracture analysis. This task reproduces the computation of the energy release rate for a zigzag graphene sheet containing a central crack under Mode I (tensile) and Mode II (shear) loading using both approaches.

## Approach
The workflow uses molecular statics (0 K) with the AIREBO potential, which implements the Tersoff‑Brenner formalism, to model a graphene sheet of fixed dimensions (15.068 nm × 17.255 nm, 9840 carbon atoms). A central crack is created by eliminating chemical bonds, and configurations are built for three half‑crack‑lengths (a = 2.009, 4.018, 6.530 nm) plus, for each, a configuration with a slightly longer crack (a + 0.251 nm). These two crack lengths are required for both the global energy method and the local force method.

For each configuration, the system is first equilibrated, then a small fixed‑grip strain of ε₀ = 0.005 is applied: a tensile displacement (uₓ = 0, u_y = ε₀ ⋅ y) for Mode I, and a shear displacement (u_x = ε₀ ⋅ y, u_y = 0) for Mode II, restricted to the top and bottom surfaces. The system is re‑equilibrated to reach minimum energy, and the total potential energy and atomic forces/coordinates are recorded.

From these results, the normalised energy release rate is computed independently by two methods:
1) **Global energy method**: the difference in total potential energy between the two crack‑length configurations, divided by the length increase Δa = 0.251 nm and the effective graphene thickness t = 0.34 nm.
2) **Local force method**: the virtual work required to close the crack extension, computed from the interatomic forces at the original crack length and the crack‑opening displacements at the extended crack length.

The two methods are applied for both Mode I and Mode II, and the rates are normalised by the square of the nominal applied stress (σ₀ for tension, τ₀ for shear).

## Reproduction target
Produce a CSV file containing the normalised strain energy release rates G/σ₀² (Mode I) and G/τ₀² (Mode II) computed from atomistic simulations using both the global energy method and the local force method. The evaluations must cover a zigzag graphene sheet of dimensions 15.068 nm × 17.255 nm (9840 atoms) with central crack half‑lengths a = 2.009 nm, 4.018 nm, and 6.530 nm, under small strain ε₀ = 0.005 at 0 K. The CSV must have exactly 12 data rows (3 crack lengths × 2 modes × 2 methods) and the columns: crack_length_nm (float), mode (string: I or II), method (string: global_energy or local_force), normalized_G (float, units: 10⁻²⁰ J/Pa²).

## Assets

- LAMMPS molecular dynamics simulator (with AIREBO potential): https://www.lammps.org/
- Python with scientific libraries: python

## Workflow steps

### Step 1: Model construction
- Role: process
- Action: Construct atomic models of a zigzag graphene sheet (15.068 nm × 17.255 nm, 9840 carbon atoms) with a central crack. Generate configurations for crack half-lengths a = 2.009, 4.018, and 6.530 nm. For each a, also build a corresponding model with an extended crack half-length a+0.251 nm.
- Evidence: `/app/outputs/model_log.txt`

### Step 2: Mode I tensile loading simulation
- Role: process
- Action: For each constructed crack model, perform molecular statics at 0 K using the AIREBO potential. Equilibrate the system, then apply fixed-grip tensile strain ε0=0.005 on top and bottom surfaces and re-equilibrate. Record total potential energy and atomic forces/coordinates.
- Evidence: `/app/outputs/modeI.log`

### Step 3: Mode II shear loading simulation
- Role: process
- Action: For each constructed crack model, perform molecular statics under shear loading. Apply shear strain (u_x = ε0 y, u_y=0) on top and bottom surfaces and re-equilibrate. Record total potential energy and atomic forces/coordinates.
- Evidence: `/app/outputs/modeII.log`

### Step 4: Compute energy release rates
- Role: scored (load-bearing)
- Action: Using the equilibrium interatomic distance Δa=0.251 nm and effective thickness t=0.34 nm, compute the normalized strain energy release rate G/σ0^2 (Mode I) and G/τ0^2 (Mode II) for each crack half-length a=2.009, 4.018, 6.530 nm using: (1) Global energy method: change in total potential energy between crack length 2a and 2a+2Δa; (2) Local force method: from interatomic forces at 2a and crack opening displacements at 2a+2Δa. Aggregate results into a CSV with columns: crack_length_nm, mode (I or II), method (global_energy or local_force), normalized_G.
- Output file: `/app/outputs/energy_release_rates.csv`
- Format: csv
- Contract: columns: crack_length_nm (float), mode (string: I or II), method (string: global_energy or local_force), normalized_G (float, unit: 1e-20 J/Pa^2).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/energy_release_rates.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### energy_release_rates.csv
- path: `/app/outputs/energy_release_rates.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Tabulated normalized energy release rates computed via the global energy and local force methods for three crack half-lengths under Mode I and Mode II.
- schema:
  - `type`: table
  - `required_columns`: `crack_length_nm`, `mode`, `method`, `normalized_G`
  - `units`:
    - `normalized_G`: 1e-20 J/Pa^2

Notes: The checker verifies the CSV contains exactly 12 rows and compares each normalized_G to the paper's reported values (from Table 1 and Table 2) within a relative tolerance. No gold values or tolerances are disclosed to the agent.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "energy_release_rates.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "crack_length_nm",
          "mode",
          "method",
          "normalized_G"
        ],
        "units": {
          "normalized_G": "1e-20 J/Pa^2"
        }
      },
      "description": "Tabulated normalized energy release rates computed via the global energy and local force methods for three crack half-lengths under Mode I and Mode II."
    }
  ],
  "notes": "The checker verifies the CSV contains exactly 12 rows and compares each normalized_G to the paper's reported values (from Table 1 and Table 2) within a relative tolerance. No gold values or tolerances are disclosed to the agent."
}
```

## How you are scored
A hidden verifier will inspect the file `energy_release_rates.csv` and score it automatically. The checker first confirms that the CSV has the correct shape and contains exactly 12 rows with the required columns. It then compares each `normalized_G` value to a hidden reference that is derived from independent calculations (the reference is not disclosed). The comparison uses a tolerance band that accounts for the differences that arise when using a different implementation of the potential or slightly different equilibration details. You must obtain values within that tolerance band to earn full credit; results that are too far from the reference receive proportionally less reward. The final reward is the aggregate of the per‑row scores, equally weighted. Simply copying known numbers from the literature will not succeed because the hidden reference and tolerance are chosen to reject guesses while accepting results computed from a genuine execution of the simulation pipeline.

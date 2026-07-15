## Problem background

Two-dimensional (2D) materials exhibit extraordinary electronic, mechanical, and optical properties that can be further tailored by stacking them into van der Waals (vdW) heterostructures. Phosphorene (both black phosphorene, α-P, and blue phosphorene, β-P) and monolayer MoSe2 (which can adopt several structural phases: hexagonal H, trigonal T, distorted tetragonal ZT, and square-octagon SO) are among the most studied 2D semiconductors. Understanding how these layers combine—what structures form, how their band gaps and mechanical flexibility change, and how their dielectric response behaves—is essential for designing optoelectronic and flexible devices.

This task reproduces a comprehensive density functional theory (DFT) investigation of van der Waals heterostructures formed by α-P and β-P with all four phases of MoSe2. You will compute equilibrium structures, electronic band gaps (including response to an external electric field), in‑plane elastic stiffness and Poisson's ratio, and static dielectric constants for every monolayer and for five commensurate heterostructures.

## Approach

You will use the SIESTA open‑source DFT code with the vdW‑DRSLL van der Waals exchange‑correlation functional, norm‑conserving Troullier‑Martins pseudopotentials, and a double‑zeta plus polarization (DZP) basis set. This protocol captures the weak interlayer binding and accurately describes both structure and electronic response.

The workflow proceeds in three broad stages:
1. **Structure construction and relaxation.** Build supercells that minimize lattice mismatch between the stacked monolayers, introduce a vacuum region to isolate the layers, and perform full geometry optimization to obtain equilibrium lattice constants, interlayer distances, and total energies.
2. **Electronic structure and electric‑field response.** Compute band structures, density of states, and work functions for all relaxed systems. For the semiconducting heterostructures (α‑P/H‑MoSe2 and β‑P/H‑MoSe2) apply uniform perpendicular electric fields to map the band‑gap variation; for the metallic‑like heterostructures evaluate the Schottky barrier heights and their types.
3. **Property calculations.** From strained configurations obtain strain‑energy data and fit them to extract in‑plane stiffness and Poisson's ratios. From time‑dependent perturbation theory obtain the complex dielectric function and read off the static dielectric constants for lateral and vertical polarization.

All raw DFT outputs are processed into four JSON‑formatted result tables that contain the computed numeric quantities for every system.

## Reproduction target

Using the SIESTA code with the vdW‑DRSLL functional, DZP basis, and Troullier‑Martins pseudopotentials, compute the following for each monolayer (α‑P, β‑P, H‑MoSe2, T‑MoSe2, ZT‑MoSe2, SO‑MoSe2) and for the five heterostructures listed below:
- Lattice constants (a, b), lattice mismatch (for heterostructures), interlayer distance (for heterostructures), and binding energy per atom (for heterostructures).
- Electronic band gap (eV) and type (direct / indirect). For α‑P/H‑MoSe2 and β‑P/H‑MoSe2, the band gap at applied perpendicular electric fields of −1.0, −0.5, +0.5, and +1.0 V/Å (and at 0 V/Å). For the metallic heterostructures (α‑P/ZT‑MoSe2, α‑P/SO‑MoSe2, β‑P/T‑MoSe2) the Schottky barrier height (eV) and type (p‑type / n‑type).
- In‑plane stiffness (Cx, Cy in N/m) and Poisson’s ratio (νx, νy) derived from a 5×5 grid of strain states (ε = −0.02 to 0.02 in steps of 0.01).
- Static dielectric constant for lateral polarization (ε∥) and vertical polarization (ε⊥).

The systems are:
Monolayers: α‑P, β‑P, H‑MoSe2, T‑MoSe2, ZT‑MoSe2, SO‑MoSe2.
Heterostructures (with their required supercell constructions to minimise mismatch):
- α‑P/H‑MoSe2 (1×5 α‑P over 1×4 H‑MoSe2)
- α‑P/ZT‑MoSe2 (1×6 α‑P over 1×4 ZT‑MoSe2)
- α‑P/SO‑MoSe2 (2×3 α‑P over 1×2 SO‑MoSe2)
- β‑P/H‑MoSe2 (1×1 β‑P over 1×1 H‑MoSe2)
- β‑P/T‑MoSe2 (1×2 β‑P over 1×1 T‑MoSe2)

## Assets

- **SIESTA code** – open‑source DFT package.
  Access: https://gitlab.com/siesta-project/siesta
- **Norm‑conserving Troullier‑Martins pseudopotentials** for P, Mo, and Se.
  These are standard pseudopotentials distributed with SIESTA or available from the official ATOM pseudopotential database.

## Workflow steps

### Step 1: Build initial heterostructure supercells
- Role: process
- Action: Construct atomic structures for the monolayers α‑P, β‑P, H‑MoSe2, T‑MoSe2, ZT‑MoSe2, SO‑MoSe2 starting from published lattice constants. Build the five heterostructures using the supercell multiplicities listed above (e.g., 1×5 α‑P over 1×4 H‑MoSe2) and a vacuum region of ≈20 Å to avoid periodic image interactions. Output the initial unrelaxed coordinates.
- Evidence: `/app/outputs/initial_structures.xyz`

### Step 2: DFT geometry optimization of all systems
- Role: process
- Action: For every monolayer and heterostructure, perform DFT geometry optimization with SIESTA using the vdW‑DRSLL functional, DZP basis, and Troullier‑Martins pseudopotentials. Relax atomic positions and cell vectors until forces fall below a well‑converged threshold. Obtain relaxed coordinates and total energies.
- Evidence: `/app/outputs/relaxed_structures.xyz`

### Step 3: Compute electronic band structures and work functions
- Role: process
- Action: For all relaxed structures, perform non‑self‑consistent band structure calculations and obtain the Kohn‑Sham eigenvalues, density of states, and work functions. Record the band energies at high‑symmetry points and the Fermi level.
- Evidence: none

### Step 4: External electric field calculations for semiconducting heterostructures
- Role: process
- Action: For α‑P/H‑MoSe2 and β‑P/H‑MoSe2, apply uniform perpendicular electric fields of −1.0, −0.5, +0.5, and +1.0 V/Å (in addition to zero field) and recompute the band structure. Save the band energies for each field.
- Evidence: none

### Step 5: Strain‑energy calculations for elastic properties
- Role: process
- Action: For each relaxed monolayer and heterostructure, generate a 5×5 grid of in‑plane strain states by independently varying the lattice constants in the x and y directions between −0.02 and 0.02 in steps of 0.01. Perform DFT single‑point energy calculations for each of the 25 strained configurations and collect the strain energy.
- Evidence: none

### Step 6: Dielectric function calculation
- Role: process
- Action: Using the ground‑state Kohn‑Sham orbitals, compute the complex dielectric function via first‑order time‑dependent perturbation theory as implemented in SIESTA for all monolayers and heterostructures.
- Evidence: none

### Step 7: Compute structural properties
- Role: scored
- Action: From the relaxed geometries and total energies, compute for each monolayer the equilibrium lattice constants a and b (Å). For each heterostructure compute the lattice mismatch (in % as the difference between the supercell in‑plane dimensions and the isolated monolayer reference dimensions), the interlayer distance (Å), and the binding energy per atom (eV/atom) using the formula |E_hetero − (E_layer1 + E_layer2)| / N, where N is the number of atoms in the heterostructure. Output the results to `structural_properties.json`.
- Output file: `/app/outputs/structural_properties.json`
- Format: json
- Contract: An array of objects. Each object has keys: "system" (string), "a" (float, Å), "b" (float, Å), "lattice_mismatch" (float or null, %), "interlayer_distance" (float or null, Å), "binding_energy_per_atom" (float or null, eV/atom). Monolayers should have null for the last three fields.
- Scoring: scored by hidden verifier

### Step 8: Compute electronic properties
- Role: scored (load-bearing)
- Action: Extract from the band structure data for every monolayer and heterostructure the band gap (eV) and its type ("direct" or "indirect"). For α‑P/H‑MoSe2 and β‑P/H‑MoSe2, list the band gap as a function of applied electric field (array of {field: float (V/Å), band_gap: float (eV)}). For the metallic‑like heterostructures (α‑P/ZT‑MoSe2, α‑P/SO‑MoSe2, β‑P/T‑MoSe2) report the Schottky barrier height (eV) and its type ("p‑type" or "n‑type"). Output the results to `electronic_properties.json`.
- Output file: `/app/outputs/electronic_properties.json`
- Format: json
- Contract: An array of objects. Keys: "system" (string), "band_gap" (float or null, eV), "band_gap_type" (string or null, "direct"/"indirect"/null), "band_gap_vs_field" (null or array of {field, band_gap}), "schottky_barrier_height" (float or null, eV), "schottky_barrier_type" (string or null, "p‑type"/"n‑type"/null). Omit or set to null fields not applicable to a system.
- Scoring: scored by hidden verifier; this step is load‑bearing because the electronic data cannot be guessed without running the full DFT pipeline including electric‑field calculations.

### Step 9: Compute mechanical properties
- Role: scored
- Action: Fit the 25‑point strain‑energy data for each system to the quadratic form E_s = a ε_x² + b ε_y² + c ε_x ε_y. From the fitted coefficients compute the in‑plane stiffness components C_x and C_y (N/m) and Poisson’s ratios ν_x and ν_y. Write the results to `mechanical_properties.json`.
- Output file: `/app/outputs/mechanical_properties.json`
- Format: json
- Contract: An array of objects. Keys: "system" (string), "Cx" (float, N/m), "Cy" (float, N/m), "vx" (float), "vy" (float).
- Scoring: scored by hidden verifier

### Step 10: Compute dielectric properties
- Role: scored
- Action: From the computed dielectric functions, extract the real part at zero frequency to obtain the static dielectric constant for lateral (ε∥) and vertical (ε⊥) polarization for each monolayer and heterostructure. Write the results to `dielectric_properties.json`.
- Output file: `/app/outputs/dielectric_properties.json`
- Format: json
- Contract: An array of objects. Keys: "system" (string), "lateral_eps" (float), "vertical_eps" (float).
- Scoring: scored by hidden verifier

## Output files

All output files must be placed under `/app/outputs`.
- `/app/outputs/initial_structures.xyz` (process)
- `/app/outputs/relaxed_structures.xyz` (process)
- `/app/outputs/structural_properties.json` (scored)
- `/app/outputs/electronic_properties.json` (scored, load‑bearing)
- `/app/outputs/mechanical_properties.json` (scored)
- `/app/outputs/dielectric_properties.json` (scored)

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### structural_properties.json
- path: `/app/outputs/structural_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Equilibrium structural parameters for monolayers and heterostructures.
- schema:
  - `type`: array
  - `items`:
    - `system`: string
    - `a`: float (Å)
    - `b`: float (Å)
    - `lattice_mismatch`: float or null (%)
    - `interlayer_distance`: float or null (Å)
    - `binding_energy_per_atom`: float or null (eV/atom)

### electronic_properties.json
- path: `/app/outputs/electronic_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Electronic band gaps (including field dependence) and Schottky barrier heights/types.
- schema:
  - `type`: array
  - `items`:
    - `system`: string
    - `band_gap`: float or null (eV)
    - `band_gap_type`: string or null ("direct" or "indirect")
    - `band_gap_vs_field`: null or array of {field: float (V/Å), band_gap: float (eV)}
    - `schottky_barrier_height`: float or null (eV)
    - `schottky_barrier_type`: string or null ("p-type" or "n-type")

### mechanical_properties.json
- path: `/app/outputs/mechanical_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: In-plane stiffness and Poisson's ratios from strain-energy fits.
- schema:
  - `type`: array
  - `items`:
    - `system`: string
    - `Cx`: float (N/m)
    - `Cy`: float (N/m)
    - `vx`: float
    - `vy`: float

### dielectric_properties.json
- path: `/app/outputs/dielectric_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Static dielectric constants for lateral and vertical polarization.
- schema:
  - `type`: array
  - `items`:
    - `system`: string
    - `lateral_eps`: float
    - `vertical_eps`: float

Notes: All numeric values are compared to hidden reference values with appropriate tolerances. Each output file carries equal weight in scoring. The verifier checks per-system entries; missing systems or extra fields are ignored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "structural_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "system": "string",
          "a": "float (Å)",
          "b": "float (Å)",
          "lattice_mismatch": "float or null (%)",
          "interlayer_distance": "float or null (Å)",
          "binding_energy_per_atom": "float or null (eV/atom)"
        }
      },
      "description": "Equilibrium structural parameters for monolayers and heterostructures."
    },
    {
      "file": "electronic_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "system": "string",
          "band_gap": "float or null (eV)",
          "band_gap_type": "string or null (\"direct\" or \"indirect\")",
          "band_gap_vs_field": "null or array of {field: float (V/Å), band_gap: float (eV)}",
          "schottky_barrier_height": "float or null (eV)",
          "schottky_barrier_type": "string or null (\"p-type\" or \"n-type\")"
        }
      },
      "description": "Electronic band gaps (including field dependence) and Schottky barrier heights/types."
    },
    {
      "file": "mechanical_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "system": "string",
          "Cx": "float (N/m)",
          "Cy": "float (N/m)",
          "vx": "float",
          "vy": "float"
        }
      },
      "description": "In-plane stiffness and Poisson's ratios from strain-energy fits."
    },
    {
      "file": "dielectric_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "system": "string",
          "lateral_eps": "float",
          "vertical_eps": "float"
        }
      },
      "description": "Static dielectric constants for lateral and vertical polarization."
    }
  ],
  "notes": "All numeric values are compared to hidden reference values with appropriate tolerances. Each output file carries equal weight in scoring. The verifier checks per-system entries; missing systems or extra fields are ignored."
}
```

## How you are scored

A hidden verifier independently reads each scored artifact and compares every numeric value to a set of reference values with appropriate tolerances. Each of the four scored artifacts carries equal weight (0.25). Partial credit is given based on the fraction of values within the allowed range. Simply reporting paper‑reported numbers is not sufficient; the verifier checks that the data originates from the actual DFT workflow.

# Energetics and ordering of Au on Cu low-index surfaces via EAM and Monte Carlo

## Problem background
Understanding how deposited Au interacts with Cu surfaces is important for surface alloy formation and thin‑film growth. This task addresses the equilibrium ordering, energetics, and atomic‑scale geometry of Au on the three low‑index Cu surfaces — (100), (110) and (111) — using the embedded atom method (EAM). The goal is to determine the preferred incorporation sites of Au atoms, whether ordered surface phases form, and whether the surface layer exhibits a rippled structure (with a height offset between Au and Cu atoms).

## Approach
The calculations use the Cu–Au EAM potential developed by Foiles, Baskes, and Daw (1986). First, static total‑energy calculations are performed for several Au configurations on a Cu(100) slab: an Au adatom, an Au atom exchanged with a surface Cu atom, and Au placed as a substitutional in the top layer, second layer, and bulk. Additional comparisons include an extra Au atom placed in an ordered surface site versus the bulk, and the exchange of an Au atom between an ordered surface and the bulk. From these, energy differences are obtained that reveal the site preferences.

Next, grand‑canonical Monte Carlo simulations are carried out at 300 K for slabs exposing the (100), (110) and (111) surfaces. The slabs are about 22 Å thick with periodic in‑plane boundaries, and the EAM potential supplies the interatomic interactions. A chemical potential difference is set to maintain a dilute bulk Au concentration (of order 0.01 at%). Starting from pure Cu, the simulations allow both atomic displacements and element swaps, creating Au atoms during the run. The equilibrated configurations record atomic positions and species.

From these snapshots, two‑dimensional structure factors S(k) (with kz = 0) are computed for the Au atoms to quantify any in‑plane ordering. Finally, the average height of Au and Cu atoms in the topmost layer is extracted to obtain the rippling amplitude (the mean height difference) for each surface.

## Reproduction target
Produce, by executing the described workflow, three scored artifacts:

1. **step_01_energy_differences.json** — five energy differences (meV) for Au incorporation processes on Cu(100), computed from the static EAM energies.
2. **step_02_structure_factor_data.json** — representative (kx, ky, S(k)) points for the Au atoms on each surface, including integer‑order beams and any additional fractional‑order peaks.
3. **step_03_rippling_amplitudes.json** — the rippling amplitude (Å) for the (100), (110) and (111) surfaces.

The target is to obtain these quantities from the EAM potential and Monte Carlo simulations; no external experimental data are needed.

## Assets

- Cu-Au EAM alloy potential (Foiles, Baskes, Daw 1986): https://www.ctcms.nist.gov/potentials/Cu-Au.html
- LAMMPS molecular dynamics package: https://www.lammps.org/downloads.html

## Workflow steps

### Step 1: Compute Au incorporation energetics on Cu(100)
- Role: scored
- Action: Using the Cu-Au EAM potential, construct Cu(100) slab configurations: Au adatom; Au exchanged with surface Cu; substitutional Au in topmost layer, second layer, and bulk; extra Au placed in ordered surface site vs bulk; and Au-Cu exchange between ordered surface and bulk. Compute total energies and report the five energy differences in meV.
- Output file: `/app/outputs/step_01_energy_differences.json`
- Format: json
- Contract: {"type":"object", "required":{"Au_adatom_exchange_favored_meV":"number", "surface_substitutional_vs_bulk_meV":"number", "second_layer_substitutional_vs_bulk_meV":"number", "extra_Au_into_ordered_surface_vs_bulk_meV":"number", "exchange_Au_from_surface_to_bulk_meV":"number"}, "units":{"all":"meV"}}
- Scoring: scored by hidden verifier

### Step 2: Run Monte Carlo simulations of Au on Cu(100), (110), (111) surfaces
- Role: process
- Action: Set up slab geometries for (100), (110) and (111) surfaces (about 22 Å thick, periodic in-plane) using the same EAM potential. Perform grand-canonical Monte Carlo simulations at 300 K with chemical potential difference corresponding to dilute bulk Au (~0.01 at%). Start from pure Cu and insert Au; allow atomic displacements and element swaps. Save equilibrated atomic configurations (positions and element types) for each surface.
- Evidence: `/app/outputs/simulation_configurations.json`

### Step 3: Compute structure factor S(k) for Au atoms
- Role: scored (load-bearing)
- Action: From the equilibrated Au atomic positions (from step_02), compute the two-dimensional structure factor S(k) for each surface with k_z=0, using the definition S(k)=⟨|∑_i exp(i k·R_i)|²⟩/N averaged over configurations. Report a set of (kx, ky, S(k)) points that includes both integer-order beams and any additional fractional-order peaks beyond the integer-order spots. For each reported peak, give a description of its position relative to the integer-order grid.
- Output file: `/app/outputs/step_02_structure_factor_data.json`
- Format: json
- Contract: {"type":"object", "required":{"(100)_surface":"array", "(110)_surface":"array", "(111)_surface":"array"}, "items":{"type":"object", "required":{"kx":"number", "ky":"number", "kz":"number", "S_k":"number", "description":"string"}}}
- Scoring: scored by hidden verifier

### Step 4: Compute rippling amplitudes
- Role: scored
- Action: From the simulated atomic positions, compute the average height of Au and Cu atoms in the topmost surface layer for each orientation. Report the rippling amplitude (difference in mean height) in angstroms.
- Output file: `/app/outputs/step_03_rippling_amplitudes.json`
- Format: json
- Contract: {"type":"object", "required":{"(100)_rippling_A":"number", "(110)_rippling_A":"number", "(111)_rippling_A":"number"}, "units":{"all":"angstrom"}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_energy_differences.json`
- `/app/outputs/step_02_structure_factor_data.json`
- `/app/outputs/step_03_rippling_amplitudes.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_energy_differences.json
- path: `/app/outputs/step_01_energy_differences.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Energy differences for Au incorporation processes on Cu(100).
- schema:
  - `type`: object
  - `required`:
    - `Au_adatom_exchange_favored_meV`: number
    - `surface_substitutional_vs_bulk_meV`: number
    - `second_layer_substitutional_vs_bulk_meV`: number
    - `extra_Au_into_ordered_surface_vs_bulk_meV`: number
    - `exchange_Au_from_surface_to_bulk_meV`: number
  - `units`:
    - `all`: meV

### step_02_structure_factor_data.json
- path: `/app/outputs/step_02_structure_factor_data.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Structure factor S(k) for Au atoms on each surface.
- schema:
  - `type`: object
  - `required`:
    - `(100)_surface`: array
    - `(110)_surface`: array
    - `(111)_surface`: array
  - `items`:
    - `type`: object
    - `required`:
      - `kx`: number
      - `ky`: number
      - `kz`: number
      - `S_k`: number
      - `description`: string

### step_03_rippling_amplitudes.json
- path: `/app/outputs/step_03_rippling_amplitudes.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Surface rippling amplitudes for the three low-index Cu surfaces.
- schema:
  - `type`: object
  - `required`:
    - `(100)_rippling_A`: number
    - `(110)_rippling_A`: number
    - `(111)_rippling_A`: number
  - `units`:
    - `all`: angstrom

Notes: The structure factor is scored on presence and qualitative width of expected fractional-order peaks; it does not demand exact S(k) values. The rippling and energy differences are compared to paper-reported values with a hidden tolerance that accounts for typical implementation differences (e.g., slab size, convergence).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_energy_differences.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "Au_adatom_exchange_favored_meV": "number",
          "surface_substitutional_vs_bulk_meV": "number",
          "second_layer_substitutional_vs_bulk_meV": "number",
          "extra_Au_into_ordered_surface_vs_bulk_meV": "number",
          "exchange_Au_from_surface_to_bulk_meV": "number"
        },
        "units": {
          "all": "meV"
        }
      },
      "description": "Energy differences for Au incorporation processes on Cu(100)."
    },
    {
      "file": "step_02_structure_factor_data.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "(100)_surface": "array",
          "(110)_surface": "array",
          "(111)_surface": "array"
        },
        "items": {
          "type": "object",
          "required": {
            "kx": "number",
            "ky": "number",
            "kz": "number",
            "S_k": "number",
            "description": "string"
          }
        }
      },
      "description": "Structure factor S(k) for Au atoms on each surface."
    },
    {
      "file": "step_03_rippling_amplitudes.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "(100)_rippling_A": "number",
          "(110)_rippling_A": "number",
          "(111)_rippling_A": "number"
        },
        "units": {
          "all": "angstrom"
        }
      },
      "description": "Surface rippling amplitudes for the three low-index Cu surfaces."
    }
  ],
  "notes": "The structure factor is scored on presence and qualitative width of expected fractional-order peaks; it does not demand exact S(k) values. The rippling and energy differences are compared to paper-reported values with a hidden tolerance that accounts for typical implementation differences (e.g., slab size, convergence)."
}
```

## How you are scored
Your submitted artifacts are graded by an automated verifier that compares them to hidden reference values. Each scored step is weighted, and the total reward is a combination across all steps. Simply reporting a number is not sufficient; the verifier may also check structural consistency (for example, that the structure factor exhibits the expected symmetry and that the energy differences and rippling amplitudes are within a physically reasonable range obtainable with this EAM potential). The verifier does not reveal the reference values, but your score depends on how closely your computed results match the expected outcome.

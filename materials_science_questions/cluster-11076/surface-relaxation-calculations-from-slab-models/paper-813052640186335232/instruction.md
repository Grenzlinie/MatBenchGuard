# Surface relaxation and energies of low-index Rh surfaces from plane-wave DFT

## Problem background
The atomic-scale structure of transition-metal surfaces is key to understanding their catalytic properties in processes such as hydrogenation and emission control. For rhodium (Rh), low-index surfaces exhibit surface relaxations where the interlayer spacings differ from the bulk. Previous experimental studies using LEED have reported conflicting values, especially for the Rh(100) surface. Reliable ab initio predictions are therefore needed to determine the relaxation magnitudes and surface energies. This reproduction task computes the surface relaxation and energetic properties of Rh(111), (100), and (110) using plane-wave density-functional theory (DFT).

## Approach
The method uses self-consistent DFT in the local-density approximation (LDA) with ultra-soft pseudopotentials (or PAW) to model Rh. Periodic slab geometries are constructed for each orientation using the experimental fcc lattice constant of Rh (a = 3.80 Å). Each slab consists of 10 atomic layers separated by a vacuum region; the two central layers are fixed at bulk positions to represent the bulk interior. Additionally, a separate bulk fcc Rh calculation is performed using the same computational parameters to obtain the bulk reference energy per atom. The atomic positions in the slabs are relaxed via conjugate-gradient minimization until forces are converged. The total energy is recorded before and after relaxation, and the interlayer distances d12 through d45 are extracted. From these raw quantities, the interlayer relaxation percentages, the surface energy, and the relaxation energy per atom are derived using the explicit formulas given below. The calculations follow widely used plane-wave DFT protocols and can be performed with any open-source code that supports pseudopotentials and geometry relaxation.

## Computational parameters (must be used for all calculations)
The following values come directly from the original 1996 paper (A. Eichler et al., Surf. Sci. 352–354, 689) and are mandatory for a consistent reproduction:

- **Plane-wave cut-off energy**: `E_cut = 190 eV` for the expansion of the pseudo‑wavefunctions.
- **k‑point sampling**: Monkhorst–Pack **k**‑point mesh adapted to the slab supercell. For well-converged energies:
  - Rh(111) and Rh(100) 10‑layer slabs: **12 × 12 × 1**.
  - Rh(110) 10‑layer slab: **12 × 8 × 1**.
- **Smearing**: Methfessel–Paxton smearing with a width of **0.2 eV** (a typical value used for metallic surfaces).
- **Vacuum region**: The vacuum thickness separating periodic slab images is **4 × d_bulk** (i.e. four times the bulk inter‑layer spacing of the corresponding surface orientation). This corresponds exactly to the “four layers of vacuum” stated in the paper.
- **Relaxation**: Conjugate‑gradient geometry optimisation until all forces on movable atoms are smaller than **0.01 eV/Å** (or an equivalent tight convergence criterion).

All three surface calculations **and** the separate bulk fcc Rh calculation must be performed with the identical set of convergence parameters (cut‑off, k‑point density, smearing, etc.).

## Reproduction target
The objective is to compute the surface relaxation characteristics of the three Rh surfaces and produce a single JSON file containing both the raw input/output data and the derived properties. Specifically, for Rh(111), Rh(100), and Rh(110) you must:

- Build symmetric 10-layer slabs with fixed central layers and a vacuum thickness as specified above.
- Perform plane-wave DFT geometry optimizations for the slabs and a separate bulk fcc Rh calculation using the parameters listed in **Computational parameters**.
- Record total energies (slab unrelaxed, slab relaxed, bulk), interlayer spacings, and slab geometry parameters.
- Compute the derived quantities using the exact formulas below.
- Write the results to `/app/outputs/relaxation_output.json` following the exact schema given in the output contract.

The derived quantities will be checked by the verifier; you are not required to output any other files.

**Derived quantity formulas** (these are mandatory – the checker recomputes from the raw data using these same equations):

1. **Interlayer relaxation percentages** (Δ12, Δ23, Δ34, Δ45):
   For each interlayer distance d_ij (relaxed) obtained from the relaxed slab,
   ```
   Δij = [(d_ij (relaxed) − d_bulk) / d_bulk] × 100%
   ```
   where d_bulk is the bulk interlayer spacing for the given surface orientation. Compute d_bulk from the experimental lattice constant a = 3.80 Å as
   ```
   d_bulk = a / √(h² + k² + l²)
   ```
   with (hkl) being the Miller indices of the surface (e.g., (111), (100), (110)).

2. **Surface energy per surface atom** (σ, in eV/atom):
   ```
   σ = (E_slab_relaxed − N_atoms × E_bulk_per_atom) / (2 × N_surf)
   ```
   - E_slab_relaxed: total energy of the relaxed slab (eV).
   - N_atoms: total number of atoms in the slab.
   - E_bulk_per_atom: bulk energy per atom obtained from a separate bulk DFT calculation (eV/atom).
   - N_surf: number of surface atoms **per surface** (i.e., the number of atoms in one surface layer of the slab). For symmetric slabs with two equivalent surfaces, the denominator accounts for both surfaces.

3. **Relaxation energy per atom** (ΔE_rel, in meV/atom):
   ```
   ΔE_rel = [(E_relaxed − E_unrelaxed) / N_atoms] × 1000
   ```
   - E_unrelaxed: total energy of the initial (unrelaxed) slab (eV).
   - The factor 1000 converts eV to meV.

**Geometric parameters for the output:**
- `bulk_spacing_Ang` – the d_bulk computed above for each surface orientation.
- `surface_area_Ang2` – the area of the 1×1 surface unit cell in Å². For an fcc lattice with lattice constant a (3.80 Å) the area of the primitive surface cell is:
  - Rh(111): area = `a² × √3 / 4`
  - Rh(100): area = `a² / 2`
  - Rh(110): area = `a² / √2`

## Assets
- Open-source plane-wave DFT code (e.g., Quantum ESPRESSO or GPAW): https://www.quantum-espresso.org/
- Rh pseudopotential (ultra-soft or PAW) from SSSP precision library or equivalent: https://www.materialscloud.org/discover/sssp/table/precision

## Workflow steps

### Step 1: Build slab models and bulk cell
- Role: process
- Action: Construct periodic slab models for the Rh(111), Rh(100), and Rh(110) surfaces. Use the experimental fcc lattice constant (a = 3.80 Å) to create symmetric 10-layer slabs with a vacuum region thickness of **4 × d_bulk** (where d_bulk is computed for each orientation). Fix the two central layers of each slab at their bulk positions. Also build a primitive fcc unit cell for bulk Rh (same lattice constant) for a separate bulk reference calculation. Generate the initial atomic coordinates and input files for the chosen DFT code.
- Evidence: none

### Step 2: DFT bulk reference calculation
- Role: process
- Action: Perform a self-consistent plane-wave DFT calculation for the bulk fcc Rh cell using the **Computational parameters** described above (cut‑off energy 190 eV, Monkhorst–Pack k‑point grid, Methfessel–Paxton smearing 0.2 eV, etc.). Extract the total energy of the bulk cell and divide by the number of atoms in the cell to obtain `bulk_energy_per_atom_eV`. This value will be used as E_bulk_per_atom in the surface energy formula. Record the result; it will be embedded in the final JSON.
- Evidence: none

### Step 3: DFT structural relaxation of slabs
- Role: process
- Action: For each slab, perform self-consistent plane-wave DFT calculations using the same convergence parameters (E_cut = 190 eV, appropriate k‑point mesh for the slab, Methfessel–Paxton smearing 0.2 eV, force convergence criterion ≤ 0.01 eV/Å). Use conjugate-gradient optimization to relax the atomic positions until the forces on all movable atoms are converged. Record the total energy of the unrelaxed slab at the start and the total energy of the fully relaxed slab. Save the relaxed interlayer distances (d12, d23, d34, d45) as defined by the vertical distances between the outermost atomic planes of successive layers.
- Evidence: none

### Step 4: Surface relaxation analysis
- Role: scored (load-bearing)
- Action: From the relaxed and unrelaxed slab data, extract the interlayer spacings, total energies, and simulation parameters. Compute `bulk_spacing_Ang` using the lattice constant and surface indices as described. Use the `bulk_energy_per_atom_eV` from the bulk calculation. Derive the interlayer relaxation percentages Δij, the surface energy σ, and the relaxation energy ΔE_rel using the formulas given in the **Reproduction target** section. Output a single JSON file containing both the raw data and the derived quantities for the three surfaces.
- Output file: `/app/outputs/relaxation_output.json`
- Format: json
- Contract: {"type":"object","required":["surfaces"],"properties":{"surfaces":{"type":"array","minItems":3,"items":{"type":"object","required":["surface","raw","derived"],"properties":{"surface":{"type":"string","pattern":"Rh\\(\\d{3}\\)"},"raw":{"type":"object","required":["interlayer_spacings","total_energy_relaxed_eV","total_energy_unrelaxed_eV","n_atoms_slab","surface_area_Ang2","n_surface_atoms","bulk_spacing_Ang","bulk_energy_per_atom_eV"],"properties":{"interlayer_spacings":{"type":"object","required":["d12_Ang","d23_Ang","d34_Ang","d45_Ang"],"properties":{"d12_Ang":{"type":"number"},"d23_Ang":{"type":"number"},"d34_Ang":{"type":"number"},"d45_Ang":{"type":"number"}}},"total_energy_relaxed_eV":{"type":"number"},"total_energy_unrelaxed_eV":{"type":"number"},"n_atoms_slab":{"type":"integer"},"surface_area_Ang2":{"type":"number"},"n_surface_atoms":{"type":"integer"},"bulk_spacing_Ang":{"type":"number"},"bulk_energy_per_atom_eV":{"type":"number"}}},"derived":{"type":"object","required":["Delta12_pct","Delta23_pct","Delta34_pct","Delta45_pct","sigma_eV_per_atom","DeltaE_rel_meV_per_atom"],"properties":{"Delta12_pct":{"type":"number"},"Delta23_pct":{"type":"number"},"Delta34_pct":{"type":"number"},"Delta45_pct":{"type":"number"},"sigma_eV_per_atom":{"type":"number"},"DeltaE_rel_meV_per_atom":{"type":"number"}}}}}}}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/relaxation_output.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### relaxation_output.json
- path: `/app/outputs/relaxation_output.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: JSON file containing raw interlayer spacings, total energies, and slab parameters for the three low-index Rh surfaces, together with the derived surface relaxation percentages, surface energy (eV/atom), and relaxation energy (meV/atom). The hidden checker recomputes the derived quantities from the raw data using the same formulas described in the reproduction target and compares them to the paper's reference values.
- schema: {"type":"object","required":["surfaces"],"properties":{"surfaces":{"type":"array","minItems":3,"items":{"type":"object","required":["surface","raw","derived"],"properties":{"surface":{"type":"string","pattern":"Rh\\(\\d{3}\\)"},"raw":{"type":"object","required":["interlayer_spacings","total_energy_relaxed_eV","total_energy_unrelaxed_eV","n_atoms_slab","surface_area_Ang2","n_surface_atoms","bulk_spacing_Ang","bulk_energy_per_atom_eV"],"properties":{"interlayer_spacings":{"type":"object","required":["d12_Ang","d23_Ang","d34_Ang","d45_Ang"],"properties":{"d12_Ang":{"type":"number"},"d23_Ang":{"type":"number"},"d34_Ang":{"type":"number"},"d45_Ang":{"type":"number"}}},"total_energy_relaxed_eV":{"type":"number"},"total_energy_unrelaxed_eV":{"type":"number"},"n_atoms_slab":{"type":"integer"},"surface_area_Ang2":{"type":"number"},"n_surface_atoms":{"type":"integer"},"bulk_spacing_Ang":{"type":"number"},"bulk_energy_per_atom_eV":{"type":"number"}}},"derived":{"type":"object","required":["Delta12_pct","Delta23_pct","Delta34_pct","Delta45_pct","sigma_eV_per_atom","DeltaE_rel_meV_per_atom"],"properties":{"Delta12_pct":{"type":"number"},"Delta23_pct":{"type":"number"},"Delta34_pct":{"type":"number"},"Delta45_pct":{"type":"number"},"sigma_eV_per_atom":{"type":"number"},"DeltaE_rel_meV_per_atom":{"type":"number"}}}}}}}}

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "relaxation_output.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {"type":"object","required":["surfaces"],"properties":{"surfaces":{"type":"array","minItems":3,"items":{"type":"object","required":["surface","raw","derived"],"properties":{"surface":{"type":"string","pattern":"Rh\\(\\d{3}\\)"},"raw":{"type":"object","required":["interlayer_spacings","total_energy_relaxed_eV","total_energy_unrelaxed_eV","n_atoms_slab","surface_area_Ang2","n_surface_atoms","bulk_spacing_Ang","bulk_energy_per_atom_eV"],"properties":{"interlayer_spacings":{"type":"object","required":["d12_Ang","d23_Ang","d34_Ang","d45_Ang"],"properties":{"d12_Ang":{"type":"number"},"d23_Ang":{"type":"number"},"d34_Ang":{"type":"number"},"d45_Ang":{"type":"number"}}},"total_energy_relaxed_eV":{"type":"number"},"total_energy_unrelaxed_eV":{"type":"number"},"n_atoms_slab":{"type":"integer"},"surface_area_Ang2":{"type":"number"},"n_surface_atoms":{"type":"integer"},"bulk_spacing_Ang":{"type":"number"},"bulk_energy_per_atom_eV":{"type":"number"}}},"derived":{"type":"object","required":["Delta12_pct","Delta23_pct","Delta34_pct","Delta45_pct","sigma_eV_per_atom","DeltaE_rel_meV_per_atom"],"properties":{"Delta12_pct":{"type":"number"},"Delta23_pct":{"type":"number"},"Delta34_pct":{"type":"number"},"Delta45_pct":{"type":"number"},"sigma_eV_per_atom":{"type":"number"},"DeltaE_rel_meV_per_atom":{"type":"number"}}}}}}}},
      "description": "JSON file containing raw interlayer spacings, total energies, and slab parameters for the three low-index Rh surfaces, together with the derived surface relaxation percentages, surface energy (eV/atom), and relaxation energy (meV/atom). The hidden checker recomputes the derived quantities from the raw data and compares them to the paper's reference values."
    }
  ],
  "notes": "Electronic surface states are not scored; they are qualitative figures and lack precise numerical targets. The bulk reference energy is obtained from a separate bulk DFT calculation, not from the fixed central layers."
}
```

## How you are scored
A hidden verifier (not visible to you) will load your `relaxation_output.json`, extract the raw slab parameters and energies, and independently recompute the derived quantities (Δij, σ, ΔE_rel) from the same formulas described in this document. The recomputed values are then compared against reference values that represent the expected outcome of a correct calculation using the described protocol. Each derived quantity contributes to your score:

- Interlayer relaxation percentages (Δ12, Δ23, Δ34, Δ45) for each surface.
- Surface energy σ per surface atom for each surface.
- Relaxation energy ΔE_rel per atom for each surface.

The comparisons use tolerances that account for the inherent variability between different DFT implementations, pseudopotential choices, and computational parameters while still requiring a physically correct result. In addition to the numerical comparisons, the verifier may check that qualitative trends (e.g., the relative ordering of top-layer contraction among the three surfaces) are consistent with the expected physical behavior, but the primary weight is on the recomputed numeric quantities.

Your total reward is a weighted sum of passes/failures across these checks; a correct full reproduction will achieve a high score, while systematic errors or missing data will reduce the reward proportionally.
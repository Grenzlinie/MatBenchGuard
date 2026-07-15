# Reproduce magnetic moment and direct-exchange integrals in monolayer LaBr2 electrene

## Problem background
Monolayer LaBr2 belongs to a class of two-dimensional electrenes, materials in which excess electrons are confined to interstitial geometric sites rather than occupying atomic orbitals. These anionic electron states have been predicted to give rise to intrinsic ferromagnetism entirely without magnetic elements — an “atomic-orbital-free” magnetism. Understanding the physical origin of this magnetism requires first-principles quantification of (i) the local magnetic moment per unit cell that the anionic electrons spontaneously form, and (ii) the direct-exchange interaction strengths coupling these moments, particularly whether the interaction remains ferromagnetic over extended distances. This reproduction task therefore aims to compute, using density functional theory and many-body post-processing, the magnetic moment per monolayer LaBr2 cell and the nearest- and second-nearest-neighbour direct-exchange integrals that underpin the proposed mechanism.

## Approach
The workflow combines plane-wave DFT, maximally localized Wannier functions, and constrained random phase approximation (cRPA). Starting from the provided monolayer LaBr2 crystal structure, a full geometry relaxation is performed with a van der Waals density functional to obtain the ground-state lattice and atomic positions. On the relaxed structure, a spin-polarized DFT calculation yields the total magnetic moment per unit cell and the spin-resolved band structure and density of states, which together identify the half-filled anionic electron band near the Fermi level. Next, a maximally localized Wannier function is constructed for that isolated band, providing a compact real-space description of the interstitial electron state and its hopping parameters. Finally, cRPA (or an equivalent consistent screened-Coulomb method) extracts the partially screened on-site and off-site Coulomb interactions and, critically, the direct-exchange parameters J01^D (nearest neighbour) and J02^D (second-nearest neighbour). The computed exchange integrals are required to satisfy ferromagnetic signs and the ordering J01^D > J02^D, consistent with an extended direct-exchange mechanism. Different DFT codes and cRPA implementations are acceptable as long as the workflow is physically consistent.

## Reproduction target
Produce the following two scored artifacts:
1. **Magnetic moment per unit cell** (in Bohr magnetons) from a spin-polarized DFT calculation on the relaxed monolayer LaBr2 structure.
2. **Direct-exchange integrals** (in meV) J01^D (nearest neighbour) and J02^D (second-nearest neighbour) extracted from a cRPA or equivalent post-processing of the Wannier function basis.
The exchange integrals must be positive (ferromagnetic) and satisfy J01^D > J02^D. This ordering is a structural requirement of the extended direct-exchange picture; its verification is an integral part of the reproduction.

## Assets

- Monolayer LaBr2 crystal structure (CIF)
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Wannier90: wannier90
- cRPA post-processing tool (e.g., RESPACK)
- PAW pseudopotential library (SSSP Efficiency): https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: Prepare monolayer LaBr2 structure
- Role: process
- Action: Generate the initial crystal structure of monolayer LaBr2 in the honeycomb H-phase MoS2 structure from the provided CIF. Set up input files for DFT geometry relaxation.
- Evidence: `/app/outputs/initial_structure.cif`

### Step 2: DFT geometry relaxation
- Role: process
- Action: Perform a spin-unpolarized DFT relaxation of the monolayer, optimizing atomic positions and lattice parameters. Use a van der Waals density functional.
- Evidence: `/app/outputs/relaxed_structure.cif`

### Step 3: Spin-polarized DFT and magnetic moment
- Role: scored
- Action: Run a spin-polarized DFT calculation on the relaxed structure. Extract the total magnetic moment per unit cell and write to magnetic_moment.json. (Generate evidence plots: spin-polarized band structure and density of states.)
- Output file: `/app/outputs/magnetic_moment.json`
- Format: json
- Contract: {"mu_B_per_cell": <float>}
- Scoring: scored by hidden verifier

### Step 4: Wannier function construction
- Role: process
- Action: Using Wannier90, construct a maximally localized Wannier function for the anionic electron band near the Fermi level from the DFT wavefunctions. Extract the hopping parameters.
- Evidence: `/app/outputs/wannier_hr.dat`

### Step 5: Direct-exchange integrals from cRPA
- Role: scored (load-bearing)
- Action: Perform constrained random phase approximation (cRPA) or an equivalent post-processing method using the Wannier functions to obtain the partially screened Coulomb parameters. Extract the nearest-neighbor direct-exchange integral J01^D and the second-nearest-neighbor direct-exchange integral J02^D. Write the values (in meV) to exchange_integrals.json.
- Output file: `/app/outputs/exchange_integrals.json`
- Format: json
- Contract: {"J_01_D_meV": <float>, "J_02_D_meV": <float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/magnetic_moment.json`
- `/app/outputs/exchange_integrals.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### magnetic_moment.json
- path: `/app/outputs/magnetic_moment.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Magnetic moment per unit cell computed from spin-polarized DFT.
- schema:
  - `type`: object
  - `required`:
    - `mu_B_per_cell`: float
  - `units`:
    - `mu_B_per_cell`: μB

### exchange_integrals.json
- path: `/app/outputs/exchange_integrals.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Direct-exchange integrals; must satisfy J_01_D_meV > 0, J_02_D_meV > 0, and J_01_D_meV > J_02_D_meV.
- schema:
  - `type`: object
  - `required`:
    - `J_01_D_meV`: float
    - `J_02_D_meV`: float
  - `units`:
    - `J_01_D_meV`: meV
    - `J_02_D_meV`: meV

Notes: Scoring is structural (T3): magnetic moment is compared to a hidden reference with tolerance; exchange integrals are checked for sign and ordering (both positive, J01^D > J02^D). No exact match to paper values is required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "magnetic_moment.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "mu_B_per_cell": "float"
        },
        "units": {
          "mu_B_per_cell": "μB"
        }
      },
      "description": "Magnetic moment per unit cell computed from spin-polarized DFT."
    },
    {
      "file": "exchange_integrals.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "J_01_D_meV": "float",
          "J_02_D_meV": "float"
        },
        "units": {
          "J_01_D_meV": "meV",
          "J_02_D_meV": "meV"
        }
      },
      "description": "Direct-exchange integrals; must satisfy J_01_D_meV > 0, J_02_D_meV > 0, and J_01_D_meV > J_02_D_meV."
    }
  ],
  "notes": "Scoring is structural (T3): magnetic moment is compared to a hidden reference with tolerance; exchange integrals are checked for sign and ordering (both positive, J01^D > J02^D). No exact match to paper values is required."
}
```

## How you are scored
Your submission will be evaluated automatically by a hidden verifier. It checks that each scored output file is present, well‑formed, and contains physically plausible values that are consistent with the correct execution of the described DFT+Wannier+cRPA workflow.

* **magnetic_moment.json**: the verifier compares your reported magnetic moment (`mu_B_per_cell`) to a reference value obtained from the same protocol, with an appropriate tolerance that accounts for toolchain differences (choice of functional, pseudopotentials, k‑mesh, etc.).
* **exchange_integrals.json**: the verifier confirms that both `J_01_D_meV` and `J_02_D_meV` are positive and that `J_01_D_meV` > `J_02_D_meV`. The precise numerical values are not matched to a specific reference; instead, the verifier checks that the sign and ordering are physically correct for the ferromagnetic direct-exchange mechanism described in the problem background.

The two scored items are weighted to contribute to a final score between 0 and 1. Simply writing down literature values without genuinely executing the workflow will not pass these checks, as the verifier also validates supporting evidence (intermediate structure files, Wannier Hamiltonian) to guard against trivial fabrication. The hidden verifier runs quickly and does not re‑execute the full DFT pipeline.

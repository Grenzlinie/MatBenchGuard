# Surface Energy and Stress of Metals from DFT Slab Calculations

## Problem background
Surfaces of metals govern diverse phenomena including catalysis, crystal growth, and reconstruction. Two key thermodynamic quantities—the surface energy ($\gamma$) and the surface stress ($\tau$)—determine the stability and elastic response of surfaces. Density-functional theory (DFT) calculations on slab models can reliably predict these properties, allowing systematic investigation of how $\gamma$ and $\tau$ vary across the periodic table. The goal of this task is to compute $\gamma$ and $\tau$ for a set of simple metals, alkaline-earth metals, and 4d transition metals from first principles, and to analyze how these properties depend on atomic number, crystal structure, and d-band filling.

## Approach
The approach uses first-principles DFT with the projector augmented wave (PAW) method. All calculations employ the open-source GPAW code together with the Atomic Simulation Environment (ASE). The Perdew–Burke–Ernzerhof (PBE) exchange–correlation functional is used throughout. First, bulk crystal structures are relaxed to obtain equilibrium lattice constants. Next, slab models with a vacuum region are built for each target metal/surface facet, preserving the in-plane lattice constants from the relaxed bulk. Atomic positions in the slab are relaxed while keeping the bottom layers fixed to emulate bulk termination. The surface energy $\gamma$ is computed from the relaxed slab total energy and the bulk energy per atom as $\gamma = (E_\text{slab} - N E_\text{bulk})/(2A)$, where $A$ is the surface area. To obtain the surface stress $\tau$, a set of isotropic biaxial in-plane strains is applied to the relaxed slab and to the corresponding bulk cell. For each strain, a static DFT calculation gives the total energy. The slab and bulk energy curves are fitted to quadratic polynomials in strain, and $\tau$ is extracted from the linear coefficients using the Shuttleworth relation. The workflow requires no external datasets beyond the crystal structures of the elements, which are built using ASE.

## Reproduction target
The task is to compute and report the equilibrium lattice constants and the surface properties for the following metals on their most stable low-index surfaces:
- Alkali metals: Li, Na, K, Rb, Cs (bcc(110)).
- Alkaline‑earth metals: Be, Mg, Ca, Sr, Ba (most stable surfaces: hcp(0001) for Be, Mg; fcc(111) for Ca, Sr; bcc(110) for Ba).
- 4d transition metals: Y, Zr, Nb, Mo, Tc, Ru, Rh, Pd, Ag, Cd (most stable surfaces: hcp(0001) for Y, Zr, Tc, Ru; bcc(110) for Nb, Mo; fcc(111) for Rh, Pd, Ag; hcp(0001) for Cd).

You must produce two scored output files:
1. `/app/outputs/lattice_constants.csv` — contains the optimized bulk lattice constant `a` (in Å) and the `c_ratio` (c/a for hcp; empty otherwise) for each metal.
2. `/app/outputs/surface_properties.csv` — contains the computed surface energy $\gamma$ (J/m²) and surface stress $\tau$ (J/m²) for each metal/surface combination.

All intermediate steps (bulk relaxation, slab construction, atomic relaxation, strain calculations) must be performed; evidence artifacts such as logs and structural JSON files are written as part of the workflow. The surface_properties.csv is the main deliverable that will be evaluated against reference data.

## Assets

- GPAW (DFT package): https://pypi.org/project/gpaw/
- ASE (Atomic Simulation Environment): https://pypi.org/project/ase/
- PBE PAW pseudopotentials for GPAW: GPAW_PSEUDO_POTENTIALS
- Numpy: https://pypi.org/project/numpy/

## Workflow steps

### Step 1: Set up bulk crystal structures
- Role: process
- Action: For each target metal, define the bulk crystal structure (bcc, fcc, hcp) using ASE with initial lattice constants from literature or defaults. Record the initial unrelaxed structures.
- Evidence: `/app/outputs/initial_bulk_structures.json`

### Step 2: Bulk lattice relaxation
- Role: process
- Action: Perform DFT geometry optimization of each bulk metal using GPAW with PBE functional and appropriate k-point grid and energy cutoff. Optimize lattice parameters until stress and forces are converged.
- Evidence: `/app/outputs/bulk_relaxation.log`

### Step 3: Report lattice constants
- Role: scored
- Action: Collect the optimized lattice constants from the bulk relaxations and write them to a CSV file.
- Output file: `/app/outputs/lattice_constants.csv`
- Format: csv
- Contract: columns: metal (string), structure (string), a (float, Angstrom), c_ratio (float or empty)
- Scoring: scored by hidden verifier

### Step 4: Construct slab models
- Role: process
- Action: Using the optimized bulk lattice constants, build slab models for each target metal/surface facet (e.g., Li bcc(110), Be hcp(0001), etc.). Use at least 8 atomic layers and ~10 Å vacuum.
- Evidence: `/app/outputs/slab_geometries.json`

### Step 5: Surface layer relaxation
- Role: process
- Action: Perform DFT slab relaxation using GPAW/PBE for each slab model. Fix the appropriate bottom layers and relax all other atomic positions until forces are converged. Record the final total energy of the relaxed slab.
- Evidence: `/app/outputs/slab_energies.json`

### Step 6: Surface stress calculation via biaxial strain
- Role: process
- Action: For each relaxed slab, apply isotropic biaxial in-plane strains and perform static DFT calculations to obtain total energies. Also apply the same strain to the bulk and obtain bulk total energy. Fit slab and bulk energy vs. strain to quadratic polynomials to extract linear coefficients and compute surface stress and surface energy using the Shuttleworth relation.
- Evidence: `/app/outputs/surface_stress_calculations.log`

### Step 7: Report surface properties
- Role: scored (load-bearing)
- Action: Write the computed surface energy (gamma) and surface stress (tau) for each metal and surface to a CSV file.
- Output file: `/app/outputs/surface_properties.csv`
- Format: csv
- Contract: columns: metal (string), surface (string), gamma (float, J/m²), tau (float, J/m²)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/lattice_constants.csv`
- `/app/outputs/surface_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### lattice_constants.csv
- path: `/app/outputs/lattice_constants.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Equilibrium lattice constants from bulk DFT relaxation. Verified against the paper's reported lattice parameters with appropriate tolerances.
- schema:
  - `required_columns`: `metal`, `structure`, `a`, `c_ratio`
  - `units`:
    - `a`: Angstrom
    - `c_ratio`: dimensionless

### surface_properties.csv
- path: `/app/outputs/surface_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed surface energy and surface stress. Checked against the paper's values with defined tolerances and additionally verified for expected periodic trends.
- schema:
  - `required_columns`: `metal`, `surface`, `gamma`, `tau`
  - `units`:
    - `gamma`: J/m²
    - `tau`: J/m²

Notes: The hidden checker will compare the submitted CSV values to the paper's reported numbers using absolute tolerances and will also verify structural trends (e.g., decreasing surface energy within groups, parabolic behavior across the 4d series).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "lattice_constants.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "required_columns": [
          "metal",
          "structure",
          "a",
          "c_ratio"
        ],
        "units": {
          "a": "Angstrom",
          "c_ratio": "dimensionless"
        }
      },
      "description": "Equilibrium lattice constants from bulk DFT relaxation. Verified against the paper's reported lattice parameters with appropriate tolerances."
    },
    {
      "file": "surface_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "required_columns": [
          "metal",
          "surface",
          "gamma",
          "tau"
        ],
        "units": {
          "gamma": "J/m²",
          "tau": "J/m²"
        }
      },
      "description": "Computed surface energy and surface stress. Checked against the paper's values with defined tolerances and additionally verified for expected periodic trends."
    }
  ],
  "notes": "The hidden checker will compare the submitted CSV values to the paper's reported numbers using absolute tolerances and will also verify structural trends (e.g., decreasing surface energy within groups, parabolic behavior across the 4d series)."
}
```

## How you are scored
Your submission will be evaluated by an automated verifier that inspects the artifacts under `/app/outputs`. The scoring is a composite reward that weights the main result (`surface_properties.csv`) most heavily, followed by the supporting lattice constants file (`lattice_constants.csv`). Each scored artifact is checked independently:
- The verifier compares your reported values to a hidden set of reference numbers that represent the expected DFT results for the chosen functional and pseudopotentials. Comparisons are made with tolerances that account for the use of an open-source code (GPAW) instead of the original VASP implementation.
- In addition, the verifier checks that the computed data obey well‑established physical trends across the chemical groups and transition metal series (e.g., the variation of $\gamma$ and $\tau$ with atomic number or d‑electron count).

A perfect reward requires both CSV files to be present, correctly formatted, and containing numerical values that fall within the expected tolerances. Intermediate process artifacts (logs, JSON files) are not directly scored but their presence may be audited for completeness. Note that simply reporting the reference numbers without performing the actual DFT computations is detectable by the verifier and will result in a low reward.

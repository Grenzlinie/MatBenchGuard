# Compute Intercalation Preference, Diffusion Barriers, and Bulk Moduli of Black Phosphorus

## Problem background
Lithium-ion, sodium-ion, and magnesium-ion batteries are critical for modern energy storage, but conventional graphite anodes are unsuitable for Na and Mg due to limited intercalation. Black phosphorus (BP), a layered allotrope of phosphorus with a wider interlayer spacing than graphite, is being explored as an alternative anode candidate. A fundamental understanding of the atomistic insertion mechanisms, diffusion kinetics, and mechanical response of BP upon lithiation, sodiation, and magnesiation is needed to evaluate its potential. This task aims to compute the key quantities that underpin such an evaluation: (1) the relative stability of two intercalated metal atoms in the same versus different phosphorene layers (intercalation preference), (2) single-ion diffusion barriers along distinct crystallographic directions, and (3) the bulk moduli of pristine BP and its fully lithiated, sodiated, and magnesiated phases. The quantitative results will illuminate the chemical and mechanical behavior of BP as a battery anode, but the numerical values themselves are the outcome of the computational workflow described below.

## Approach
The approach employs first-principles density functional theory (DFT) to model a 2×2×2 orthorhombic supercell of black phosphorus containing 64 phosphorus atoms. All calculations use the PBE exchange-correlation functional with Grimme D2 van der Waals corrections, as implemented in the open-source Quantum ESPRESSO package, with suitable pseudopotentials (e.g., SSSP efficiency or precision pseudopotentials for Li, Na, Mg, and P). The Atomic Simulation Environment (ASE) is used for structure generation and nudged elastic band (NEB) setup, and pandas for data handling.

Three types of properties are computed:
- **Intercalation preference energy difference**: For each metal (Li, Na, Mg), two configurations of two metal atoms in the supercell are optimized — one with both atoms in the same interlayer space (same‑layer), the other with them in adjacent interlayer spaces (different‑layer). The total energies of these six structures yield the energy difference ΔE = E(same‑layer) − E(different‑layer).
- **Diffusion barriers**: NEB simulations are performed for a single metal atom moving along the zigzag and armchair channels within the relaxed BP supercell. The minimum‑energy path is obtained and the barrier height (energy difference between the transition state and the initial state) is extracted for each metal and each path.
- **Bulk moduli**: Structures with compositions Li₂P, Na₂P, and Mg₂P are constructed by filling all available interlayer sites according to the intercalation mechanisms identified from the ΔE results (columnar for metals that prefer different layers, planar for those that prefer the same layer). These structures, together with pristine BP, are relaxed. A series of static DFT calculations are then run at volumes spanning −5% to +5% from equilibrium. The resulting energy–volume data for each composition are fitted to a Birch–Murnaghan equation of state (or a suitable EOS form) to obtain the bulk modulus.

## Reproduction target
The agent must execute the ordered workflow steps and produce the following three scored output files:

1. **`/app/outputs/intercalation_preference.json`** – a JSON object with keys `"Li"`, `"Na"`, `"Mg"`, each mapping to the computed energy difference ΔE (in eV) between the two‑metal same‑layer and different‑layer configurations. Positive ΔE indicates that the different‑layer configuration is more stable.
2. **`/app/outputs/diffusion_barriers.csv`** – a CSV file with columns `metal`, `path`, `barrier_eV`. It must contain six rows covering Li, Na, and Mg for both the `zigzag` and `armchair` paths, giving the extracted NEB barrier height in eV.
3. **`/app/outputs/bulk_moduli.csv`** – a CSV file with columns `composition`, `bulk_modulus_GPa`. It must contain rows for `"pristine"`, `"Li2P"`, `"Na2P"`, and `"Mg2P"`, reporting the bulk modulus in GPa obtained from the EOS fit.

All intermediate process steps (pristine supercell optimization, M₂P₆₄ configuration relaxations, NEB setup, M₂P structure optimizations, and energy‑volume calculations) must be genuinely executed, as the downstream scored artifacts depend on their outputs. The exact numerical values of the scored quantities will emerge from the DFT calculations.

## Assets

- Quantum ESPRESSO (open-source DFT package): https://www.quantum-espresso.org/
- SSSP pseudopotential library: https://www.materialscloud.org/discover/sssp/table/precision
- Atomic Simulation Environment (ASE): ase
- pandas: pandas

## Workflow steps

### Step 1: Optimize pristine black phosphorus supercell
- Role: process
- Action: Perform DFT geometry optimization of a 2x2x2 orthorhombic supercell of black phosphorus (64 P atoms) using Quantum ESPRESSO (PBE functional + Grimme D2 van der Waals correction) to obtain equilibrium lattice parameters and total energy.
- Evidence: `/app/outputs/pristine_relax.log`

### Step 2: Optimize M2P64 intercalation configurations
- Role: process
- Action: For each metal (Li, Na, Mg): construct two initial configurations in the 2x2x2 BP supercell — (a) both metal atoms in the same interlayer space (same-layer), (b) in adjacent interlayer spaces (different-layer). Perform DFT geometry optimization for each of the six structures with QE/PBE+D2. Record final total energies.
- Evidence: `/app/outputs/m2p64_energies.csv`

### Step 3: Compute intercalation preference energy differences
- Role: scored
- Action: From the total energies of the six M2P64 configurations, compute ΔE = E(same-layer) − E(different-layer) for each metal. Write intercalation_preference.json with keys “Li”, “Na”, “Mg” mapping to the difference in eV (positive means different-layer is more stable).
- Output file: `/app/outputs/intercalation_preference.json`
- Format: json
- Contract: {"Li": float, "Na": float, "Mg": float}
- Scoring: scored by hidden verifier

### Step 4: Perform NEB diffusion barrier calculations
- Role: process
- Action: Set up nudged elastic band (NEB) simulations for a single metal atom (Li, Na, Mg) in the relaxed BP supercell along the zigzag and armchair diffusion paths. Use QE/PBE+D2. For each metal and path, obtain the minimum energy path and extract the barrier height.
- Evidence: `/app/outputs/neb.log`

### Step 5: Compile diffusion barriers
- Role: scored (load-bearing)
- Action: From the NEB results, write diffusion_barriers.csv with columns metal, path, barrier_eV. Include six rows: Li/Na/Mg for zigzag and armchair paths.
- Output file: `/app/outputs/diffusion_barriers.csv`
- Format: csv
- Contract: metal (str), path (str: 'zigzag' or 'armchair'), barrier_eV (float)
- Scoring: scored by hidden verifier

### Step 6: Build and optimize Li2P, Na2P, Mg2P structures
- Role: process
- Action: Construct unit cells/models for compositions Li2P, Na2P, Mg2P by filling all available interlayer sites with metal atoms according to the intercalation mechanism (columnar for Li/Mg, planar for Na) and perform DFT geometry optimization with QE/PBE+D2 to obtain low-energy configurations.
- Evidence: `/app/outputs/m2p_optimized.log`

### Step 7: Compute total energy vs volume for EOS
- Role: process
- Action: For pristine BP and for the optimized Li2P, Na2P, Mg2P structures, run DFT static calculations at volumes spanning −5% to +5% from equilibrium (several points). Collect total energy vs volume.
- Evidence: `/app/outputs/evol.txt`

### Step 8: Fit equation of state and output bulk moduli
- Role: scored
- Action: Fit the energy-volume data for each composition to a Birch-Murnaghan equation of state to extract the bulk modulus. Write bulk_moduli.csv with columns composition, bulk_modulus_GPa for “pristine”, “Li2P”, “Na2P”, “Mg2P”.
- Output file: `/app/outputs/bulk_moduli.csv`
- Format: csv
- Contract: composition (str), bulk_modulus_GPa (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/intercalation_preference.json`
- `/app/outputs/diffusion_barriers.csv`
- `/app/outputs/bulk_moduli.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### intercalation_preference.json
- path: `/app/outputs/intercalation_preference.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Energy difference ΔE = E(same-layer) - E(different-layer) in eV for each metal. Positive means different-layer configuration is more stable.
- schema:
  - `type`: object
  - `required`:
    - `Li`: float
    - `Na`: float
    - `Mg`: float
  - `items`: object
  - `required_columns`:
  - `units`:
    - `Li`: eV
    - `Na`: eV
    - `Mg`: eV

### diffusion_barriers.csv
- path: `/app/outputs/diffusion_barriers.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Single-ion diffusion barriers along zigzag and armchair paths for Li, Na, and Mg.
- schema:
  - `type`: table
  - `required_columns`: `metal`, `path`, `barrier_eV`
  - `items`: object
  - `required`: object
  - `units`:
    - `barrier_eV`: eV

### bulk_moduli.csv
- path: `/app/outputs/bulk_moduli.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Bulk modulus from Birch-Murnaghan EOS fit for pristine black phosphorus and fully lithiated/sodiated/magnesiated phases.
- schema:
  - `type`: table
  - `required_columns`: `composition`, `bulk_modulus_GPa`
  - `items`: object
  - `required`: object
  - `units`:
    - `bulk_modulus_GPa`: GPa

Notes: The agent must perform all DFT calculations using Quantum ESPRESSO (PBE+D2) with standard SSSP precision pseudopotentials. Tolerance windows accommodate code/pseudopotential differences. Scored quantities are the three numbers/trends per artifact against hidden paper reference values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "intercalation_preference.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "Li": "float",
          "Na": "float",
          "Mg": "float"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "Li": "eV",
          "Na": "eV",
          "Mg": "eV"
        }
      },
      "description": "Energy difference ΔE = E(same-layer) - E(different-layer) in eV for each metal. Positive means different-layer configuration is more stable."
    },
    {
      "file": "diffusion_barriers.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "metal",
          "path",
          "barrier_eV"
        ],
        "items": {},
        "required": {},
        "units": {
          "barrier_eV": "eV"
        }
      },
      "description": "Single-ion diffusion barriers along zigzag and armchair paths for Li, Na, and Mg."
    },
    {
      "file": "bulk_moduli.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition",
          "bulk_modulus_GPa"
        ],
        "items": {},
        "required": {},
        "units": {
          "bulk_modulus_GPa": "GPa"
        }
      },
      "description": "Bulk modulus from Birch-Murnaghan EOS fit for pristine black phosphorus and fully lithiated/sodiated/magnesiated phases."
    }
  ],
  "notes": "The agent must perform all DFT calculations using Quantum ESPRESSO (PBE+D2) with standard SSSP precision pseudopotentials. Tolerance windows accommodate code/pseudopotential differences. Scored quantities are the three numbers/trends per artifact against hidden paper reference values."
}
```

## How you are scored
A hidden verifier independently evaluates each of the three scored output files against reference criteria derived from the original study and from fundamental physical expectations. The verifier checks the intercalation preference sign and magnitude, the diffusion barrier ordering and values, and the bulk modulus trends, applying appropriate tolerances that account for differences between DFT codes and pseudopotentials. Each artifact contributes a weighted fraction to a final reward between 0 and 1, with the diffusion barriers carrying the largest weight (as they represent the most computationally intensive target), and the intercalation preference and bulk moduli each carrying a substantial share. The scoring rewards accurate reproduction of the physical trends and values; merely reporting the paper's numbers without proper computations will not pass the hidden tolerances. No gold values or exact tolerances are disclosed in this instruction; the workflow must be followed faithfully to obtain a valid solution.

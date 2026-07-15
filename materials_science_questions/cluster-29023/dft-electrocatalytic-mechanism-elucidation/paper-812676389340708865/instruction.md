# DFT-calculated adsorption energies of NH3 and fragments on Co3O4 facets

## Problem background
Ammonium perchlorate (AP) is a key oxidizer in composite solid propellants, and its thermal decomposition performance is critically sensitive to the presence of transition-metal oxide catalysts. Among these, cobalt oxide (Co3O4) nanocrystals exhibit facet-dependent catalytic activity: the high-temperature decomposition peak temperature of AP varies significantly depending on which crystal facet is predominantly exposed. The prevailing mechanistic hypothesis attributes this facet effect to the adsorption and subsequent oxidation of ammonia (NH3) — a major intermediate that accumulates on the AP surface and inhibits decomposition. Understanding how different Co3O4 facets bind NH3 and its dehydrogenation fragments is therefore central to explaining and predicting the observed catalytic trends.

## Approach
We approach this problem with spin-polarized density functional theory (DFT) calculations that incorporate the PBE exchange-correlation functional, an on-site Hubbard U correction (U−J = 3.3 eV) for the Co 3d electrons, and Grimme's DFT-D3 dispersion correction. First, the bulk cubic spinel lattice of Co3O4 is fully optimized to obtain the equilibrium lattice constant. Using this lattice constant, stoichiometric, oxygen-terminated surface slabs are constructed for the low-index {110}, {111}, and {100} facets, each with five Co–O layers, a 15 Å vacuum gap, and the two bottommost layers frozen to mimic the bulk environment. Clean slabs are relaxed, then a single NH3 molecule is placed on each surface, and geometry optimizations are performed to locate the most stable adsorption configuration. The same protocol is applied to the successive dehydrogenation fragments NH2, NH, and N adsorbed on the {110} facet. Finally, the binding energy of each adsorbate is obtained as the total energy difference: E(slab + adsorbate) − E(clean slab) − E(gas-phase species). All calculations may be executed with any open-source DFT code that supports PAW pseudopotentials, PBE+U, and DFT-D3 (e.g., Quantum ESPRESSO, ABINIT, or GPAW).

## Reproduction target
You must compute and submit two JSON artifacts under /app/outputs:

1.  **Bulk lattice constant** (`bulk_lattice_constant.json`) — the optimized lattice constant (in Å) of cubic spinel Co3O4 obtained from the spin-polarized DFT+U relaxation of the bulk unit cell.

2.  **Binding energies** (`binding_energies.json`) — the binding energies (in eV, with negative values indicating exothermic adsorption) for:
    - NH3 on the Co3O4 {110}, {111}, and {100} facets
    - NH2, NH, and N on the Co3O4 {110} facet (a total of seven values).

These values must reflect the most stable adsorption geometry found on each facet. The workflow produces the lattice constant as an intermediate checkpoint that verifies the correct DFT setup, while the binding energies are the primary scored output. The objective is to obtain physically reasonable binding energies that respect the expected qualitative ordering among facets and fragments.

## Assets

- Co3O4 crystal structure (initial bulk lattice): https://materialsproject.org/materials/mp-18748
- Open-source DFT code supporting PAW/PBE+U+DFT-D3
- PAW pseudopotential library (PBE, Co, O, N, H): https://www.materialscloud.org/discover/sssp/
- Atomic Simulation Environment (ASE): ase

## Workflow steps

### Step 1: Bulk Co3O4 DFT optimization
- Role: scored (load-bearing)
- Action: Perform spin-polarized DFT+U (PBE, U-J=3.3 eV, DFT-D3) geometry optimization of bulk cubic spinel Co3O4 starting from the known crystal structure. Output the optimized lattice constant (a_angstrom) in JSON.
- Output file: `/app/outputs/bulk_lattice_constant.json`
- Format: json
- Contract: { "a_angstrom": float }
- Scoring: scored by hidden verifier

### Step 2: Surface slab model construction
- Role: process
- Action: Using the optimized lattice constant from step_01, construct slab models for the {110}, {111}, and {100} facets. Each slab must contain five Co–O layers with the bottom two layers fixed, a vacuum region of at least 15 Å, and oxygen-terminated surfaces. Relax the clean slabs and save the atomic coordinates as evidence.
- Evidence: `/app/outputs/slab_models.xyz`

### Step 3: DFT adsorption calculations
- Role: process
- Action: Using the same DFT settings as step_01, perform geometry relaxations and total energy calculations for each clean slab and for each slab with one adsorbed species (NH3 on all facets; NH2, NH, N on {110} facet). Keep bottom two layers fixed. Save the total energies as evidence.
- Evidence: `/app/outputs/total_energies.json`

### Step 4: Binding energy extraction
- Role: scored
- Action: From the total energies of step_03 and gas-phase species computed under the same conditions, compute binding energies E_b = E(slab+adsorbate) - E(clean slab) - E(gas-phase species) for NH3 on {110}, {111}, {100} and NH2, NH, N on {110}. Report the seven binding energies (eV) in JSON.
- Output file: `/app/outputs/binding_energies.json`
- Format: json
- Contract: { "NH3_110": float, "NH3_111": float, "NH3_100": float, "NH2_110": float, "NH_110": float, "N_110": float }
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bulk_lattice_constant.json`
- `/app/outputs/binding_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bulk_lattice_constant.json
- path: `/app/outputs/bulk_lattice_constant.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Optimized lattice constant of Co3O4 bulk, used to build slab models and as a checkpoint for DFT correctness.
- schema:
  - `type`: object
  - `required`:
    - `a_angstrom`: float (angstrom)

### binding_energies.json
- path: `/app/outputs/binding_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Binding energies of NH3 on Co3O4 {110}, {111}, {100} and of NH2, NH, N on {110} facet.
- schema:
  - `type`: object
  - `required`:
    - `NH3_110`: float (eV)
    - `NH3_111`: float
    - `NH3_100`: float
    - `NH2_110`: float
    - `NH_110`: float
    - `N_110`: float

Notes: The checker compares the submitted values to hidden reference values with tolerances and verifies relative trends (stronger binding on {110} > {111} > {100} for NH3, and increasingly stronger binding for deeper fragments on {110}).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bulk_lattice_constant.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "a_angstrom": "float (angstrom)"
        }
      },
      "description": "Optimized lattice constant of Co3O4 bulk, used to build slab models and as a checkpoint for DFT correctness."
    },
    {
      "file": "binding_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "NH3_110": "float (eV)",
          "NH3_111": "float",
          "NH3_100": "float",
          "NH2_110": "float",
          "NH_110": "float",
          "N_110": "float"
        }
      },
      "description": "Binding energies of NH3 on Co3O4 {110}, {111}, {100} and of NH2, NH, N on {110} facet."
    }
  ],
  "notes": "The checker compares the submitted values to hidden reference values with tolerances and verifies relative trends (stronger binding on {110} > {111} > {100} for NH3, and increasingly stronger binding for deeper fragments on {110})."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that compares your reported lattice constant and binding energies to independently determined reference values. For each scored artifact, the verifier checks that the numerical value falls within a predetermined tolerance of the reference and that the required relative trends among conditions (e.g., adsorption strength ordering across facets, and the monotonically increasing binding strength with deeper dehydrogenation on the {110} facet) are satisfied. The two scored artifacts are weighted and combined into a single reward between 0 and 1. The binding energies are the main scored objective; the bulk lattice constant serves as a load‑bearing checkpoint that forces the full DFT workflow to run. You are not scored on procedural details such as pseudopotential choice or convergence parameters, only on the final numerical values and their consistency with the expected physical trends.

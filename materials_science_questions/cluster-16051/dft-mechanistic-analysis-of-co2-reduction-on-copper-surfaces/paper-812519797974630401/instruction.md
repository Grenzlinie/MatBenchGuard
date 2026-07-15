# DFT analysis of CO adsorption and oxidation on PtCu model surfaces

## Problem background
The oxidation of carbon monoxide (CO) is a critical reaction in heterogeneous catalysis, with applications in hydrogen purification, emission control, and fuel cells. Platinum‑based catalysts are widely used, but they suffer from severe CO poisoning at low temperatures because CO binds too strongly to Pt surfaces, blocking active sites needed for O₂ adsorption and dissociation. Intermetallic PtCu nanoparticles have been experimentally shown to exhibit significantly higher catalytic activity for preferential CO oxidation (PROX) at lower temperatures than pure Pt, but the atomistic mechanism by which the PtCu surface structure modifies the reactivity is not well understood. This task addresses that gap by using density functional theory (DFT) to computationally examine O₂ dissociation, CO adsorption, and the CO + O₂ reaction on a series of model surfaces—pure Pt(111) and Cu‑doped Pt(111) surfaces, as well as the PtCu intermetallic compound (012) surface—to reveal how Cu atoms alter the energy landscape and the reaction pathway.

## Approach
The reaction steps are studied with periodic DFT using the Perdew–Burke–Ernzerhof (PBE) exchange–correlation functional. Four model slab systems are constructed to systematically vary the Cu content: (1) a clean Pt(111) surface (64 Pt atoms), (2) PtCu‑1 with a single surface Cu atom, (3) PtCu‑4 with four surface Cu atoms, and (4) the PtCu IMC (012) surface, where alternating rows of Pt and Cu atoms create a 50% surface Cu concentration. All slabs contain four atomic layers and a vacuum gap. After fully relaxing the geometries, the following properties are computed for each surface: (i) the activation barrier for O₂ dissociation from a fcc‑hollow adsorption site, using the climbing‑image nudged elastic band (CI‑NEB) method, along with Bader charges and the O–O distance at the transition state; (ii) CO adsorption energies, Bader charges on CO and the underlying metal atom, and the CO stretching vibrational frequency (obtained from finite‑differences or density‑functional perturbation theory) for on‑top Pt and on‑top Cu sites; (iii) the activation barrier for the CO‑assisted O₂ dissociation pathway, where an adsorbed CO reacts with a nearby O₂, also via CI‑NEB, with transition‑state geometric parameters and metal‑atom charge. The comparisons across the four surfaces isolate how Cu concentration and the specific arrangement in the intermetallic compound influence the energetics, charge transfer, and reaction mechanism. All calculations are performed with an open‑source plane‑wave DFT code (e.g., Quantum ESPRESSO) using appropriate norm‑conserving or ultrasoft pseudopotentials, and the results are reported in the three scored CSV files.

## Reproduction target
Using the described slab models and computational protocol, compute and produce three CSV files under `/app/outputs`:

- `o2_dissociation_results.csv`: For each of the four surface models, report the O₂ dissociation barrier ΔE‡ (eV), Bader charges (q_Pt, q_Cu, q_O₂), and the O–O distance (Å) at the transition state. The barrier is computed for the most stable fcc‑hollow site that includes at least one Cu atom when present.
- `co_adsorption_results.csv`: For each model, report CO adsorption energy ΔE (eV), Bader charges on the surface metal atom and the CO molecule, and the C–O stretching frequency (cm⁻¹) for CO adsorbed on top of a Pt atom and, where applicable, on top of a Cu atom. (Pt(111) has only the Pt‑site entry.)
- `co_o2_reaction_results.csv`: For each model, report the CO+O₂ reaction barrier ΔE‡ (eV), O–O distance, newly formed C–O distance, distance from C to the nearest surface metal atom (C–M), and the Bader charge of that metal atom at the transition state.

The quantities must be obtained from CI‑NEB (for barriers) and Bader charge analysis applied to the fully relaxed DFT wavefunctions following the same DFPT or finite‑differences approach for vibrational frequencies. The goal is to obtain values that reflect the relative trends across the four surface compositions, not any single absolute number.

## Assets

- Quantum Espresso (open-source DFT code): https://www.quantum-espresso.org/
- SSSP Efficiency pseudopotentials for Pt, Cu, O, C: https://www.materialscloud.org/discover/sssp/table/efficiency
- Bader charge analysis tool (Henkelman code): https://theory.cm.utexas.edu/henkelman/code/bader/
- Python scientific stack (ASE, pymatgen, numpy, pandas): ase, pymatgen, numpy, pandas

## Workflow steps

### Step 1: Construct slab models
- Role: process
- Action: Build four slab models using an open-source DFT code with the PBE functional and appropriate pseudopotentials: (i) Pt(111) – 4×4×4 layers (64 Pt atoms); (ii) PtCu-1 – 63 Pt + 1 surface Cu; (iii) PtCu-4 – 60 Pt + 4 surface Cu; (iv) PtCu IMC (012) – alternating rows of Pt and Cu, 32 Pt + 32 Cu. Each slab comprises 4 atomic layers and a vacuum gap of ~11 Å. Fully relax all atomic positions until forces are below 0.02 eV/Å using the specified k‑point sampling. These optimized geometries are required for all subsequent steps.
- Evidence: `/app/outputs/slab_geometries.log`

### Step 2: Compute O₂ dissociation barriers
- Role: scored (load-bearing)
- Action: For each of the four slab models, compute the activation barrier for O₂ dissociation from the most stable fcc‑hollow site that includes at least one Cu atom when present. Use the climbing‑image nudged elastic band (CI‑NEB) method. Extract the barrier ΔE‡ (eV), Bader charges (q_Pt, q_Cu, q_O₂), and the O–O distance at the transition state. Write the results to o2_dissociation_results.csv with one row per model.
- Output file: `/app/outputs/o2_dissociation_results.csv`
- Format: csv
- Contract: Model (string), Barrier_eV (float), q_Pt (float), q_Cu (float), q_O2 (float), d_OO_angstrom (float). One row per model.
- Scoring: scored by hidden verifier

### Step 3: Compute CO adsorption properties
- Role: scored
- Action: For each slab model, compute the adsorption energy ΔE (eV), Bader charges on CO (q_CO) and the surface metal atom beneath it, and the C–O stretching vibrational frequency ν_CO (cm⁻¹) for CO adsorbed on top of a Pt atom and, where applicable, on top of a Cu atom. Use a finite‑differences or density‑functional perturbation theory approach for the vibrational frequency. Write the results to co_adsorption_results.csv with two rows per model (on‑top Pt and on‑top Cu).
- Output file: `/app/outputs/co_adsorption_results.csv`
- Format: csv
- Contract: Model (string), Site (Pt/Cu), DE_eV (float), q_surface_atom (float), q_CO (float), nu_CO_cm1 (int). Two rows per model (except Pt(111) which only has the Pt site).
- Scoring: scored by hidden verifier

### Step 4: Compute CO+O₂ reaction barriers
- Role: scored
- Action: For each slab model, compute the activation barrier for the CO‑assisted O₂ dissociation pathway (reaction of an adsorbed CO with a nearby adsorbed O₂). Use CI‑NEB to locate the transition state. Report the barrier ΔE‡ (eV), the O–O distance, the newly formed C–O distance, the distance from the C atom to the nearest surface metal atom (C–M), and the Bader charge of that metal atom at the transition state. Write the results to co_o2_reaction_results.csv with one row per model.
- Output file: `/app/outputs/co_o2_reaction_results.csv`
- Format: csv
- Contract: Model (string), Barrier_eV (float), d_OO_angstrom (float), d_CO_angstrom (float), d_CM_angstrom (float), q_M (float). One row per model.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/o2_dissociation_results.csv`
- `/app/outputs/co_adsorption_results.csv`
- `/app/outputs/co_o2_reaction_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### o2_dissociation_results.csv
- path: `/app/outputs/o2_dissociation_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Scored artifact for O₂ dissociation barriers and TS properties.
- schema:
  - `type`: table
  - `required_columns`: `Model`, `Barrier_eV`, `q_Pt`, `q_Cu`, `q_O2`, `d_OO_angstrom`
  - `units`:
    - `Barrier_eV`: eV
    - `d_OO_angstrom`: angstrom
    - `q_Pt`: e
    - `q_Cu`: e
    - `q_O2`: e
  - `description`: One row per surface model, values compared to paper-reported Table 1 with hidden tolerances and trend checks.

### co_adsorption_results.csv
- path: `/app/outputs/co_adsorption_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Scored artifact for CO adsorption energies, charges, and vibrational frequencies.
- schema:
  - `type`: table
  - `required_columns`: `Model`, `Site`, `DE_eV`, `q_surface_atom`, `q_CO`, `nu_CO_cm1`
  - `units`:
    - `DE_eV`: eV
    - `q_surface_atom`: e
    - `q_CO`: e
    - `nu_CO_cm1`: cm^-1
  - `description`: Two rows per model (on‑top Pt and on‑top Cu, except Pt(111) which has only Pt). Values compared to paper-reported Table 2 with tolerances and trend checks (CO adsorption energy on Pt > on Cu).

### co_o2_reaction_results.csv
- path: `/app/outputs/co_o2_reaction_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Scored artifact for CO+O₂ reaction barriers and TS parameters.
- schema:
  - `type`: table
  - `required_columns`: `Model`, `Barrier_eV`, `d_OO_angstrom`, `d_CO_angstrom`, `d_CM_angstrom`, `q_M`
  - `units`:
    - `Barrier_eV`: eV
    - `d_OO_angstrom`: angstrom
    - `d_CO_angstrom`: angstrom
    - `d_CM_angstrom`: angstrom
    - `q_M`: e
  - `description`: One row per model. Values compared to paper-reported Table 3 with tolerances and trend checks (IMC has lowest barrier).

Notes: The direct CO+O adatom reaction barrier and Redhead desorption temperature analysis are excluded per taskability scope. The site-segregation claim is captured via the CO adsorption energy comparison in co_adsorption_results.csv. All tolerances, trend constraints, and exact reference values are hidden and handled by the checker.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "o2_dissociation_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Model",
          "Barrier_eV",
          "q_Pt",
          "q_Cu",
          "q_O2",
          "d_OO_angstrom"
        ],
        "units": {
          "Barrier_eV": "eV",
          "d_OO_angstrom": "angstrom",
          "q_Pt": "e",
          "q_Cu": "e",
          "q_O2": "e"
        },
        "description": "One row per surface model, values compared to paper-reported Table 1 with hidden tolerances and trend checks."
      },
      "description": "Scored artifact for O₂ dissociation barriers and TS properties."
    },
    {
      "file": "co_adsorption_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Model",
          "Site",
          "DE_eV",
          "q_surface_atom",
          "q_CO",
          "nu_CO_cm1"
        ],
        "units": {
          "DE_eV": "eV",
          "q_surface_atom": "e",
          "q_CO": "e",
          "nu_CO_cm1": "cm^-1"
        },
        "description": "Two rows per model (on‑top Pt and on‑top Cu, except Pt(111) which has only Pt). Values compared to paper-reported Table 2 with tolerances and trend checks (CO adsorption energy on Pt > on Cu)."
      },
      "description": "Scored artifact for CO adsorption energies, charges, and vibrational frequencies."
    },
    {
      "file": "co_o2_reaction_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Model",
          "Barrier_eV",
          "d_OO_angstrom",
          "d_CO_angstrom",
          "d_CM_angstrom",
          "q_M"
        ],
        "units": {
          "Barrier_eV": "eV",
          "d_OO_angstrom": "angstrom",
          "d_CO_angstrom": "angstrom",
          "d_CM_angstrom": "angstrom",
          "q_M": "e"
        },
        "description": "One row per model. Values compared to paper-reported Table 3 with tolerances and trend checks (IMC has lowest barrier)."
      },
      "description": "Scored artifact for CO+O₂ reaction barriers and TS parameters."
    }
  ],
  "notes": "The direct CO+O adatom reaction barrier and Redhead desorption temperature analysis are excluded per taskability scope. The site-segregation claim is captured via the CO adsorption energy comparison in co_adsorption_results.csv. All tolerances, trend constraints, and exact reference values are hidden and handled by the checker."
}
```

## How you are scored
Each of your three CSV artifacts will be independently evaluated by a hidden verifier. The verifier compares your reported values against expected reference data (derived from the original study) using numerical tolerances appropriate for the quantity (e.g., energy, charge, distance, frequency). Additionally, the verifier checks that certain expected relative trends across the surface models are satisfied (for example, the ordering of activation barriers with Cu content, or the difference between CO binding on Pt versus Cu sites). Every field is weighted and aggregated into a final reward between 0 and 1. The reward is higher when the computed numbers closely match the expected results and the trends are correctly reproduced. Note that you are evaluated solely on the content of these CSV files; the hidden reference values and tolerances are never shown. Your job is to faithfully execute the protocol; the verifier rewards fidelity to the physics encoded in the reference data.

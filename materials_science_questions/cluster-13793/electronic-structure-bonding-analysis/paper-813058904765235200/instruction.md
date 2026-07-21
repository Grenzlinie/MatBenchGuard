# First-Principles Calculation of Dislocation-Solute Interactions in Ferritic Iron

## Problem background
The macro-scale mechanical properties of ferritic steels are largely controlled by the interaction between dislocations and interstitial solute atoms. In body-centered cubic (bcc) iron, the most common screw dislocation has a 1/2⟨111⟩ Burgers vector and normally adopts a symmetric easy core configuration. Recent first-principles calculations showed that carbon solutes can induce a spontaneous transformation of this easy core into an unexpected hard core, in which the carbon atoms sit at the centers of regular trigonal prisms formed by surrounding iron atoms. It is not known whether this reconstruction is a singular effect of carbon or a general phenomenon that also occurs for other light interstitial elements such as boron, nitrogen, and oxygen. Understanding this is essential for predicting solute strengthening and strain aging in iron-based alloys. The goal of this task is to compute the dislocation–solute interaction energy and to determine for each solute whether the hard core reconstruction occurs spontaneously when two solute atoms are placed near the dislocation at two different solute‑solute distances along the line.

## Approach
The computations are performed with spin‑polarized density functional theory (DFT) using the Perdew–Burke–Ernzerhof (PBE) generalized gradient approximation and projector augmented wave (PAW) pseudopotentials. The reference DFT settings, taken from the original paper, must be used to allow a faithful reproduction:

- Plane‑wave kinetic‑energy cutoff: **400 eV**
- Methfessel‑Paxton smearing width: **0.2 eV**
- Force convergence criterion: **0.01 eV/Å** (10⁻² eV/Å)
- **k‑point grids** (shifted Monkhorst‑Pack):
  - Bulk Fe supercell (≈250 atoms): **4×4×4**
  - Dislocation cell with 1b separation (135 Fe atoms, 2 solute atoms): **1×2×16**
  - Dislocation cell with 2b separation (270 Fe atoms, 2 solute atoms): **1×2×8**
- Pseudopotentials: Fe without semi‑core electrons; B, C, N, O with 2s and 2p valence states.

The approach consists of the following conceptual stages:
- A reference bulk bcc Fe cell is relaxed to obtain the bulk energy and verify the equilibrium lattice parameter and magnetic moment.
- Quadrupolar periodic arrays of 1/2⟨111⟩ screw dislocation dipoles are constructed. Two supercell sizes are used, corresponding to solute‑solute separation distances of 1b and 2b along the dislocation line. These cells are relaxed without solutes to obtain the reference easy‑core dislocation energy.
- Reference energies for isolated solutes (B, C, N, O) are obtained by placing one solute atom in the bulk octahedral interstitial site of a Fe supercell and relaxing the atomic positions.
- For every solute and for both separations, an initial E₁ configuration is built by inserting two solute atoms in octahedral‑like interstitial positions that are first‑nearest neighbours to each dislocation core, using the previously relaxed easy‑core dipole cell of the appropriate length. The system is then fully relaxed with DFT.
- From the relaxed structure it is determined whether the dislocation core has spontaneously transformed to the hard core configuration with the solutes at the centre of regular trigonal prisms. For any case where the reconstruction is not spontaneous, an explicit hard‑core configuration is also relaxed to check whether the reconstruction is still energetically favourable.
- The dislocation–solute interaction energy per solute atom is evaluated using a standard difference formula that combines the energies of the dislocation‑solute supercell, the pure bulk Fe cell, the easy‑core dislocation cell, and the isolated solute cell.

The entire workflow can be implemented with any open‑source plane‑wave DFT code capable of treating spin‑polarised calculations with PAW or ultrasoft pseudopotentials, such as Quantum ESPRESSO.

## Reproduction target
Your goal is to produce a quantitative and categorical assessment for each of the eight primary cases (solute = B, C, N, O; solute‑solute separation = 1b, 2b):
1. Compute the relaxed dislocation–solute interaction energy per solute atom, E_int (in eV).
2. Determine whether the dislocation core spontaneously reconstructed to the hard core upon relaxation from the initial easy‑core configuration with solutes in octahedral‑like nearest‑neighbour positions. If the spontaneous relaxation does **not** yield the hard core, additionally construct an explicit hard‑core configuration and compare its energy to decide whether the reconstruction is energetically favourable but not spontaneous.

Report the results in the two scored output files described in the output contract:
- `/app/outputs/interaction_energies.csv` (one row per case, columns: solute, separation, E_int, reconstruction_spontaneous)
- `/app/outputs/reconstruction_summary.json` (a JSON array with objects containing solute, separation, reconstruction, and E_int_eV)

## Assets

- Open-source plane-wave DFT code (e.g., Quantum ESPRESSO): https://www.quantum-espresso.org/
- PBE-GGA pseudopotentials for Fe (no semi-core), B, C, N, O (2s2p valence): https://www.quantum-espresso.org/pseudopotentials/

## Workflow steps

### Step 1: Relax pure bcc Fe bulk supercell
- Role: process
- Action: Perform spin-polarized DFT relaxation of a bulk bcc Fe supercell (e.g., 250‑atom cell) using PBE-GGA and the specified pseudopotentials. Use a 4×4×4 shifted k‑point grid, 400 eV cutoff, 0.2 eV smearing, and relax atomic positions until forces are below 0.01 eV/Å. Record the total energy E_bulk and verify the equilibrium lattice parameter and magnetic moment.
- Optional intermediate: save the bulk energy to `/app/outputs/bulk_fe_energy.txt`.

### Step 2: Relax screw dislocation dipole in pure Fe
- Role: process
- Action: Construct a **quadrupolar periodic array of 1/2⟨111⟩ screw dislocation dipoles** in bcc Fe. The dislocation lines are directed along [111] with Burgers vector **b = 1/2[111]**. Use two cell lengths along the dislocation line: **1b** (135 Fe atoms) and **2b** (270 Fe atoms). The cell vectors in the (111) plane must be chosen such that the distance between dislocation cores avoids artificial interactions; typical choices follow the geometry described in previous DFT studies (e.g., a₁ = n₁·½[112], a₂ = n₂·½[1-10] with integer n₁,n₂). Introduce a pair of opposite‑sign screw dislocations using an anisotropic elastic displacement field (Volterra solution) or a suitable tool (ATOMSK, LAMMPS+empirical potential, etc.) and then transfer to the DFT code for fixed‑cell ionic relaxation. Perform relaxation with the appropriate k‑point grids: 1×2×16 for the 1b cell, 1×2×8 for the 2b cell, keeping other DFT settings identical to Step 1. Record the total energy E_easy for each cell length and save the relaxed easy‑core structure for later use.
- Optional intermediate: save the easy‑core energies to `/app/outputs/easy_core_energies.txt`.

### Step 3: Relax isolated solutes in bulk Fe octahedral sites
- Role: process
- Action: For each solute X = B, C, N, O, place one solute atom in the **octahedral interstitial site** of the same bulk Fe supercell used in Step 1 (same cell size and DFT settings, 4×4×4 k‑point grid). Relax atomic positions and record the total energy E_X for each solute.
- Optional intermediate: save the solute bulk energies to `/app/outputs/solute_bulk_energies.txt`.

### Step 4: DFT simulations of dislocation‑solute systems
- Role: process
- Action: For every combination of solute (B, C, N, O) and solute‑solute separation d = 1b, 2b:
  - (a) Construct the initial **E₁ configuration**: take the previously relaxed easy‑core dipole cell of the appropriate length and identify the atomic columns that form the dislocation core. Locate the **octahedral‑like interstitial sites that are first nearest neighbours** to the core atoms – these sites correspond to the O⁽¹⁾ position in Ref. [17] and lie adjacent to the three ⟨111⟩ core columns at a distance comparable to b/2 from the dislocation centre. Insert one solute atom per such site near each of the two dislocations (two solute atoms in total).
  - (b) Fully relax the system with DFT using the same k‑point grid and convergence settings as the pure dislocation cell.
  - (c) Analyse the relaxed structure to determine whether the dislocation core has **spontaneously reconstructed** to the hard core with the solutes at the centres of regular trigonal prisms formed by iron atoms.
  - (d) Record the total energy E_dislo+X.
- For any case where the spontaneous relaxation does **not** produce a clear hard core, additionally **construct an explicit hard‑core configuration** by placing the solute atoms directly at the centres of the trigonal prismatic sites in the core (same supercell geometry), relax it, and compare its total energy with that of the spontaneously relaxed configuration. This comparison is needed to decide whether the reconstruction is *energetically favourable but not spontaneous*.
- Store all raw energies and reconstruction flags in a structured intermediate file, e.g. `raw_simulation_data.json` (optional).

### Step 5: Compute interaction energies and write CSV
- Role: scored (load-bearing)
- Action: From the reference energies (E_bulk, E_easy for each cell length, E_X) and the dislocation‑solute energies recorded in the previous step, compute the dislocation–solute interaction energy per solute atom using:

  E_int = E_d – E_∞, with  E_d = ½ E_dislo+X + E_bulk  and  E_∞ = ½ E_easy + E_X.

  For each case, assign the reconstruction outcome:
  - `spontaneous` — if the dislocation core spontaneously transformed to the hard core;
  - `no_reconstruction` — if the core did not transform and the hard core is not energetically preferred;
  - `energetically_favorable_but_not_spontaneous` — if the reconstruction is energetically favourable (explicit hard core has lower energy than the spontaneously relaxed configuration) but does not occur spontaneously.

  Write the results to `interaction_energies.csv`.
- Output file: `/app/outputs/interaction_energies.csv`
- Format: csv
- Contract: Columns: `solute` (B|C|N|O), `separation` (1b|2b), `E_int` (float, eV), `reconstruction_spontaneous` (string: `spontaneous`, `no_reconstruction`, or `energetically_favorable_but_not_spontaneous`). Eight rows total.
- Scoring: scored by hidden verifier

### Step 6: Compile reconstruction summary JSON
- Role: scored
- Action: From the same underlying data used for Step 5, produce a JSON file that summarises the reconstruction outcome and interaction energy for every solute–separation combination in a structured format.
- Output file: `/app/outputs/reconstruction_summary.json`
- Format: json
- Contract: An object with key `"results"`, whose value is an array of objects with the fields `solute` (string), `separation` (`"1b"` or `"2b"`), `reconstruction` (string, one of `"spontaneous"`, `"no_reconstruction"`, `"energetically_favorable_but_not_spontaneous"`), and `E_int_eV` (float, eV).
- Scoring: scored by hidden verifier

## Output files
Write the **scored** artifacts under `/app/outputs`:
- `/app/outputs/interaction_energies.csv`
- `/app/outputs/reconstruction_summary.json`

Only these two files are evaluated. All intermediate files are optional and are not checked by the verifier.

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### interaction_energies.csv
- path: `/app/outputs/interaction_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV file with dislocation‑solute interaction energies and reconstruction outcomes. The reconstruction_spontaneous column must use one of the values: `spontaneous`, `no_reconstruction`, `energetically_favorable_but_not_spontaneous`.
- schema:
  - `type`: table
  - `required_columns`: `solute`, `separation`, `E_int`, `reconstruction_spontaneous`
  - `units`:
    - `E_int`: eV

### reconstruction_summary.json
- path: `/app/outputs/reconstruction_summary.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: JSON summary of reconstruction results and interaction energies.
- schema:
  - `type`: object
  - `required`: `results`
  - `items`:
    - `solute`: string
    - `separation`: string
    - `reconstruction`: string (one of `spontaneous`, `no_reconstruction`, `energetically_favorable_but_not_spontaneous`)
    - `E_int_eV`: float

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "interaction_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "solute",
          "separation",
          "E_int",
          "reconstruction_spontaneous"
        ],
        "units": {
          "E_int": "eV"
        }
      },
      "description": "CSV file with dislocation‑solute interaction energies and reconstruction outcomes."
    },
    {
      "file": "reconstruction_summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "results"
        ],
        "items": {
          "solute": "string",
          "separation": "string",
          "reconstruction": "string",
          "E_int_eV": "float"
        }
      },
      "description": "JSON summary of reconstruction results and interaction energies."
    }
  ],
  "notes": "The reconstruction labels should be one of: spontaneous, energetically_favorable_but_not_spontaneous, no_reconstruction. Interaction energies are in eV."
}
```

## How you are scored
A hidden automated verifier will score your submission by reading the two scored output files (`interaction_energies.csv` and `reconstruction_summary.json`). 

For the interaction energies, the verifier compares your reported values to a set of reference results determined by the original research. A generous absolute tolerance is applied to account for legitimate differences arising from the use of an open‑source DFT code and pseudopotentials that differ from the original VASP calculations. You will receive full credit for energies that lie within this tolerance; credit degrades for values that deviate more significantly.

For the reconstruction outcomes, the verifier checks that each categorical label matches the expected result exactly. 

The final reward is a weighted combination of the energy accuracy and the reconstruction‑label accuracy across all cases. A submission that provides correct energies and labels within tolerance will earn the maximum score. Simply reporting fabricated numbers that happen to fall within the tolerance does not constitute a successful reproduction; you must execute the DFT workflow to obtain physically meaningful results.
# DFT+U Band Gaps and Sodium Extraction Potentials of NaMFe(MoO₄)₃ Double Molybdates

## Problem background
Sodium-ion batteries require cathode materials that combine a suitable electronic band gap (semiconducting character) with high sodium extraction potentials. The double molybdates NaMFe(MoO₄)₃, which crystallise in two distinct triclinic phases (α and β), offer a large compositional space where the divalent cation M can be Mn, Fe, Co, Ni or Zn. Understanding how the choice of M and the crystal phase affect the band gap and the voltage for Na extraction is essential for evaluating these compounds as potential battery cathodes. This task computes those properties from first principles.

## Approach
Use spin‑polarised density functional theory with a Hubbard U correction (DFT+U) within the generalised gradient approximation (PBE functional). Treat all compounds in the ferromagnetic state. Start from the published crystal structures of the iron‑only end members (α‑NaFe₂(MoO₄)₃ and β‑NaFe₂(MoO₄)₃) and build the mixed‑metal models by replacing one Fe with the target M according to the most stable cation ordering. Relax only the atomic positions (keeping the experimental lattice parameters) for three sodium contents: fully sodiated (x=1), half‑sodiated (x=0.5), and fully desodiated (x=0). From the relaxed x=1 structures, extract the electronic band gap as the energy difference between the valence band maximum and conduction band minimum. Then compute the sodium extraction potentials V1 (x=1 → 0.5) and V2 (x=0.5 → 0) using the total energies of the relaxed phases and the chemical potential of body‑centred‑cubic sodium. The required Hubbard U parameters for Fe²⁺, Fe³⁺, Mn²⁺, Co²⁺, Ni²⁺ and Zn²⁺ are taken from a published first‑principles determination; no correction is applied to Zn.

## Reproduction target
Produce the following two CSV files inside `/app/outputs`:

- `band_gaps.csv`: one row per compound (α and β phases of NaMFe(MoO₄)₃ for M = Mn, Fe, Co, Ni, Zn; 10 rows total). Columns: `compound` (string, e.g. “α‑NaMnFe(MoO₄)₃”) and `band_gap_ev` (float, eV).
- `extraction_potentials.csv`: one row per compound, columns `compound` (string), `V1_ev` (float, eV) and `V2_ev` (float, eV), giving the potentials for the half‑ and full‑extraction steps defined above.

The CSV files must contain only the computed numbers; no additional columns or summary rows.

## Assets

- Crystal structures of α‑NaFe₂(MoO₄)₃ and β‑NaFe₂(MoO₄)₃ (Muessig et al., Acta Crystallogr. B 59, 611, 2003): https://www.ccdc.cam.ac.uk/
- Hubbard U parameters from first‑principles calculations (Linscott et al., Phys. Rev. B 98, 235157, 2018): 10.1103/PhysRevB.98.235157
- Quantum ESPRESSO (plane‑wave DFT code, open‑source): https://www.quantum‑espresso.org
- SSSP efficiency pseudopotentials (PBE PAW): https://www.materialscloud.org/discover/sssp/table/efficiency
- Body‑centered cubic Na (chemical potential reference)

## Workflow steps

### Step 1: Prepare input structures
- Role: process
- Action: Obtain the CIF files of α‑ and β‑NaFe₂(MoO₄)₃ (CSD 216108, 216109). For each phase, replace one Fe by M = Mn, Fe, Co, Ni, Zn according to the most favorable M/Fe ordering pattern (Fig. 1 of the paper and the related publication [44]). Generate input files for all ten NaMFe(MoO₄)₃ compounds.
- Evidence: none

### Step 2: Geometry optimization of NaMFe(MoO₄)₃ (x=1)
- Role: process
- Action: For each of the ten structures, perform spin‑polarized DFT+U geometry relaxation (ferromagnetic ordering) using the PBE functional and the specified Hubbard U parameters. Fix lattice parameters; relax only atomic positions until forces and energy converge. Save the relaxed total energies.
- Evidence: none

### Step 3: Compute band gaps of fully sodiated compounds
- Role: scored (load-bearing)
- Action: Using the relaxed structures from step_02, run a static DFT+U calculation (same settings) to obtain the total density of states. Extract the band gap as the energy difference between the top of the valence band and the bottom of the conduction band. Collect gaps for all ten compounds.
- Output file: `/app/outputs/band_gaps.csv`
- Format: csv
- Contract: CSV with columns: compound (string, e.g. 'α‑NaMnFe(MoO₄)₃'), band_gap_ev (float, eV). One row per compound (10 rows).
- Scoring: scored by hidden verifier

### Step 4: Prepare Na₀.₅ and Na₀ structures
- Role: process
- Action: From each relaxed NaMFe(MoO₄)₃ structure, create models for Na₀.₅MFe(MoO₄)₃ (remove half the Na atoms in a symmetric way) and MFe(MoO₄)₃ (remove all Na). Set up input files for these twenty new structures.
- Evidence: none

### Step 5: Geometry optimization of Naₓ phases (x=0.5, 0)
- Role: process
- Action: Relax the Na₀.₅ and Na₀ structures for all ten compounds using the same DFT+U settings as step_02. Fix lattice parameters; relax atomic positions. Save the relaxed total energies.
- Evidence: none

### Step 6: Compute sodium extraction potentials V1 and V2
- Role: scored
- Action: Collect the total energies from the relaxed Na (step_02), Na₀.₅ and Na₀ structures (step_05). Compute the energy per atom of bcc Na with the same DFT+U settings. Calculate V1 = –[E(Na) – E(Na₀.₅) – 0.5 μ(Na)] and V2 = –[E(Na₀.₅) – E(Na₀) – 0.5 μ(Na)] for all ten compounds. Report V1 and V2 in a CSV file.
- Output file: `/app/outputs/extraction_potentials.csv`
- Format: csv
- Contract: CSV with columns: compound (string), V1_ev (float, eV), V2_ev (float, eV). One row per compound (10 rows).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gaps.csv`
- `/app/outputs/extraction_potentials.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gaps.csv
- path: `/app/outputs/band_gaps.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Band gaps of the ten fully sodiated NaMFe(MoO₄)₃ compounds (α and β phases of M = Mn, Fe, Co, Ni, Zn).
- schema:
  - `type`: table
  - `required_columns`: `compound`, `band_gap_ev`
  - `units`:
    - `band_gap_ev`: eV

### extraction_potentials.csv
- path: `/app/outputs/extraction_potentials.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Sodium extraction potentials V1 (x=1→0.5) and V2 (x=0.5→0) for the same ten compounds.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `V1_ev`, `V2_ev`
  - `units`:
    - `V1_ev`: eV
    - `V2_ev`: eV

Notes: Monotonic trends of band gaps and potentials with the atomic number of M are also checked and contribute to the score.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gaps.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "band_gap_ev"
        ],
        "units": {
          "band_gap_ev": "eV"
        }
      },
      "description": "Band gaps of the ten fully sodiated NaMFe(MoO₄)₃ compounds (α and β phases of M = Mn, Fe, Co, Ni, Zn)."
    },
    {
      "file": "extraction_potentials.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "V1_ev",
          "V2_ev"
        ],
        "units": {
          "V1_ev": "eV",
          "V2_ev": "eV"
        }
      },
      "description": "Sodium extraction potentials V1 (x=1→0.5) and V2 (x=0.5→0) for the same ten compounds."
    }
  ],
  "notes": "Monotonic trends of band gaps and potentials with the atomic number of M are also checked and contribute to the score."
}
```

## How you are scored
A hidden verifier reads your two CSV files. It checks that every required value is present and compares your computed band gaps and extraction potentials to independently established reference values (using an appropriate numerical tolerance that accounts for differences between DFT implementations). Additionally, the verifier examines whether the reported band gaps and potentials follow the expected monotonic trends with the atomic number of the M cation within each phase. The final reward is a combination of the numerical accuracy on each quantity and the degree of trend adherence. The reward ranges from 0 (no match) to 1 (perfect agreement). Submitting only the paper's literature values without running the workflow is unlikely to satisfy the trend checks and tolerance constraints simultaneously.

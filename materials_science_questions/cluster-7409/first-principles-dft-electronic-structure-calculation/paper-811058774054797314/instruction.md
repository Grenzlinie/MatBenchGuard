# DFT calculation of defect formation energies and band gaps in BiOI with oxygen vacancy and iodine self-doping

## Problem background
The layered bismuth oxyiodide (BiOI) photocatalyst absorbs visible light due to its relatively narrow band gap. Introducing intrinsic point defects—an oxygen vacancy (Vo) or iodine self-doping—can further tune its electronic structure and optical response. Understanding which defect type yields the most favorable stability and how each defect alters the band gap is essential for assessing their potential to enhance photocatalytic performance. This task asks: among oxygen vacancy and two possible iodine substitution sites (substituting O or substituting Bi), which defect forms most readily, and how do their band gaps compare to that of defect-free BiOI? Answering these questions requires computing defect formation energies and electronic band gaps from first principles.

## Approach
Use plane-wave pseudopotential density functional theory (DFT) with the GGA-PBE exchange-correlation functional and ultrasoft pseudopotentials. Model a 2×2×1 tetragonal supercell of BiOI (space group P4/nmn) that contains 24 atoms. Create three defect structures from the relaxed pure supercell: one oxygen vacancy, one substitution of an oxygen atom by iodine (I-O doping), and one substitution of a bismuth atom by iodine (I-Bi doping). Relax all four supercells to obtain their total energies. Compute reference chemical potentials μ_O and μ_I as half the total energies of isolated O2 and I2 molecules in their ground states; derive μ_Bi from the total energy of the pure supercell and the elemental energies. Calculate the defect formation energy for each defect as the difference between the total energy of the defect supercell and that of the pure supercell, plus or minus the chemical potentials of the exchanged species. Finally, perform band structure calculations for all four relaxed systems along a suitable high-symmetry k-path and extract the indirect (or direct) band gap values.

## Reproduction target
Generate two JSON output files under /app/outputs:   
- defect_formation_energies.json: contains the formation energies (in eV) of oxygen vacancy, I-O doping, and I-Bi doping, labeled E_form1, E_form2, and E_form3 respectively.   
- band_gaps.json: contains the band gaps (in eV) of pure BiOI and the three defect systems, labeled pure_BG, Vo_BG, IO_BG, and IBi_BG.   
The formation energies must be derived from the DFT total energies and chemical potentials as described. The band gaps must be extracted from the band structure calculations. The verifier will compare these values against hidden reference results and may also check that certain ordering relations among the formation energies and band gaps hold.

## Assets

- Open-source plane-wave DFT code (e.g., Quantum ESPRESSO): https://www.quantum-espresso.org/
- Pseudopotentials (PBE, ultrasoft): https://www.materialscloud.org/discover/sssp/table
- BiOI crystal structure (P4/nmn)

## Workflow steps

### Step 1: Construct pure BiOI supercell
- Role: process
- Action: Build a 2×2×1 supercell (24 atoms, Bi8O8I8) using the tetragonal P4/nmn crystal structure with lattice parameters a=b=3.984 Å, c=9.128 Å. Output an initial structure file for DFT.
- Evidence: `/app/outputs/pure_supercell_initial.cif`

### Step 2: Relax pure BiOI supercell
- Role: process
- Action: Perform full geometry relaxation of the pure supercell using DFT (GGA-PBE, ultrasoft pseudopotentials). Obtain relaxed coordinates, lattice parameters, and total energy E(Bi8O8I8).
- Evidence: `/app/outputs/pure_relaxed.out`

### Step 3: Construct defect supercells
- Role: process
- Action: From the relaxed pure supercell, create three defect structures: (a) remove one O atom (site I) for oxygen vacancy (Bi8O7I8); (b) substitute one O atom (site I) with I for I-O doping (Bi8O7I9); (c) substitute one Bi atom (site II) with I for I-Bi doping (Bi7O8I9).
- Evidence: `/app/outputs/defect_initial_structures.tar`

### Step 4: Relax defect supercells
- Role: process
- Action: Perform full DFT relaxation for each defect supercell using the same settings as the pure case. Extract relaxed total energies: E(Bi8O7I8), E(Bi8O7I9), E(Bi7O8I9).
- Evidence: `/app/outputs/defect_relaxed_energies.txt`

### Step 5: Compute reference chemical potentials
- Role: process
- Action: Perform DFT calculations for an O2 molecule and an I2 molecule in the same pseudopotential/functional setup. Compute μ_O = 0.5*E(O2), μ_I = 0.5*E(I2). Derive μ_Bi from the total energy of the pure BiOI supercell and the elemental energies (implicitly, as described in the paper).
- Evidence: `/app/outputs/chemical_potentials.json`

### Step 6: Calculate defect formation energies
- Role: scored (load-bearing)
- Action: Compute the three defect formation energies using the formulas from the paper. Output a JSON file with the three values in eV.
- Output file: `/app/outputs/defect_formation_energies.json`
- Format: json
- Contract: JSON object with keys "E_form1", "E_form2", "E_form3" (each a float in eV).
- Scoring: scored by hidden verifier

### Step 7: Compute band structures and band gaps
- Role: scored
- Action: For each relaxed system (pure, Vo, I-O, I-Bi), perform a DFT band structure calculation along a suitable high-symmetry k-path and extract the band gap values. Output a JSON with the band gaps for the four systems in eV.
- Output file: `/app/outputs/band_gaps.json`
- Format: json
- Contract: JSON object with keys "pure_BG", "Vo_BG", "IO_BG", "IBi_BG" (each a float in eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/defect_formation_energies.json`
- `/app/outputs/band_gaps.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### defect_formation_energies.json
- path: `/app/outputs/defect_formation_energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Calculated defect formation energies for oxygen vacancy (E_form1), I-O doping (E_form2), and I-Bi doping (E_form3). The checker compares each value to the paper-reported gold within a hidden tolerance and verifies ordering.
- schema:
  - `type`: object
  - `required`:
    - `E_form1`: float (eV)
    - `E_form2`: float (eV)
    - `E_form3`: float (eV)

### band_gaps.json
- path: `/app/outputs/band_gaps.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Band gaps (indirect or direct) for pure BiOI, BiOI with oxygen vacancy, I-O doped BiOI, and I-Bi doped BiOI. The checker compares each value to the paper-reported gold within a hidden tolerance.
- schema:
  - `type`: object
  - `required`:
    - `pure_BG`: float (eV)
    - `Vo_BG`: float (eV)
    - `IO_BG`: float (eV)
    - `IBi_BG`: float (eV)

Notes: All values are compared against paper-reported reference values using absolute tolerances (formation energies ±0.2 eV, band gaps ±0.15 eV) plus ordering constraint E_form3 < E_form1 < E_form2. The agent must NOT know these tolerances; they are hidden.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "defect_formation_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "E_form1": "float (eV)",
          "E_form2": "float (eV)",
          "E_form3": "float (eV)"
        }
      },
      "description": "Calculated defect formation energies for oxygen vacancy (E_form1), I-O doping (E_form2), and I-Bi doping (E_form3). The checker compares each value to the paper-reported gold within a hidden tolerance and verifies ordering."
    },
    {
      "file": "band_gaps.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "pure_BG": "float (eV)",
          "Vo_BG": "float (eV)",
          "IO_BG": "float (eV)",
          "IBi_BG": "float (eV)"
        }
      },
      "description": "Band gaps (indirect or direct) for pure BiOI, BiOI with oxygen vacancy, I-O doped BiOI, and I-Bi doped BiOI. The checker compares each value to the paper-reported gold within a hidden tolerance."
    }
  ],
  "notes": "All values are compared against paper-reported reference values using absolute tolerances (formation energies ±0.2 eV, band gaps ±0.15 eV) plus ordering constraint E_form3 < E_form1 < E_form2. The agent must NOT know these tolerances; they are hidden."
}
```

## How you are scored
An automated hidden checker reads your output artifacts. Each workflow stage carries a weight, with the two scored output files (defect formation energies and band gaps) contributing most of the reward. The checker compares the values you submit to hidden reference values using predefined tolerances and may also verify structural constraints (such as relative ordering of the formation energies and band gap reductions). The checker does not have access to the source paper and does not reveal its tolerances. To score well you must run the full DFT pipeline faithfully; reporting numbers from elsewhere without performing the computations will not pass the hidden checks.

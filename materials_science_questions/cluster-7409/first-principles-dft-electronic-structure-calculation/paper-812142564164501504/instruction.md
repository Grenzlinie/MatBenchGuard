# Band structure and orbital population analysis of a rutile-type mixed oxide and its doped variant

## Problem background
Vanadium antimonate (VSbO4) in the rutile-type structure is an important catalyst for selective oxidation reactions. Understanding its electronic structure — the contributions of V, Sb and O orbitals, and the changes induced by substituting Sb with Ti — is essential for rational catalyst design. This task aims to compute the electronic band structure, density of states, charge distributions, and d‑orbital populations for pure VSbO4 and for a Ti‑doped variant, to determine how titanium doping affects the vanadium oxidation state and the V–O bonding.

## Approach
The calculations employ the semi‑empirical extended Hückel method as implemented in the open‑source package YAeHMOP. Atomic parameters (ionization potentials, Slater exponents, linear coefficients) are taken from the published literature for V, Sb, O, and Ti. Two periodic supercell models are constructed: a trirutile supercell for pure VSbO4 (lattice parameters a=b=4.636 Å, c'=3c with c=3.048 Å) and a corresponding cell where one Sb is replaced by Ti (nominal composition VSb0.83Ti0.17O4). For each structure, the 3D band structure, total density of states (DOS), crystal orbital overlap population (COOP) curves, and Mulliken population analysis are computed with a 40 k‑point sampling. The raw outputs are then parsed to extract the Fermi energy, the band energies along the high‑symmetry lines of the tetragonal Brillouin zone (c/a<1), the total DOS, the average Mulliken charges per element, and the average populations of the five V 3d components (x²−y², z², xy, xz, yz).

## Reproduction target
Produce four scored artifacts: (1) a JSON file (`pure_band_dos.json`) for pure VSbO4 containing the Fermi energy, band energies along the k‑path, and the total DOS curve; (2) a JSON file (`doped_band_dos.json`) with the same content for the Ti‑doped structure; (3) a CSV table (`mulliken_charges_table.csv`) of the average Mulliken charge for each element (V, Sb, O in the pure case; V, Sb, Ti, O in the doped case); (4) a CSV table (`v_orbital_populations.csv`) of the average V 3d orbital populations for both structures. These artifacts quantify the electronic differences — particularly the expected oxidation of vanadium and the depopulation of specific V 3d orbitals — induced by Ti doping.

## Assets

- YAeHMOP: http://www.overlap.chem.cornell.edu:8080/yaehmop.html

## Workflow steps

### Step 1: Build structural models and input files
- Role: process
- Action: Construct the trirutile supercell geometry for VSbO4 (lattice parameters a=b=4.636 Å, c'=3c with c=3.048 Å) and for the Ti‑doped variant (VSb0.83Ti0.17O4) using published crystallographic data for the trirutile structure. Prepare YAeHMOP input files with the atomic parameters from the paper's Table 1 (ionization potentials, Slater exponents, linear coefficients for V, Sb, Ti, O) and specify 40 k‑point sampling.
- Evidence: `/app/outputs/input_files_generated.txt`

### Step 2: Run extended Hückel for pure VSbO4
- Role: process
- Action: Execute YAeHMOP on the pure VSbO4 supercell input to compute 3D band structure, total DOS, COOP curves, and Mulliken populations.
- Evidence: `/app/outputs/pure_raw_output.txt`

### Step 3: Run extended Hückel for Ti‑doped VSbO4
- Role: process
- Action: Execute YAeHMOP on the Ti‑doped VSbO4 supercell input to compute 3D band structure, total DOS, COOP curves, and Mulliken populations.
- Evidence: `/app/outputs/doped_raw_output.txt`

### Step 4: Extract band structure and DOS for pure VSbO4
- Role: scored (load-bearing)
- Action: Parse the raw output of the pure calculation and produce a JSON file containing the Fermi energy, band energies along the selected k‑path (high‑symmetry lines of the tetragonal Brillouin zone with c/a<1), and the total DOS curve.
- Output file: `/app/outputs/pure_band_dos.json`
- Format: json
- Contract: JSON object with keys: 'fermi_energy' (float, eV), 'band_energies' (array of arrays, each sub-array [k_index, band_index, energy]), 'dos' (array of [energy, total_DOS] pairs).
- Scoring: scored by hidden verifier

### Step 5: Extract band structure and DOS for Ti‑doped VSbO4
- Role: scored
- Action: Parse the raw output of the Ti‑doped calculation and produce a JSON file with the same structure as for the pure case.
- Output file: `/app/outputs/doped_band_dos.json`
- Format: json
- Contract: JSON object with keys: 'fermi_energy' (float, eV), 'band_energies' (array of arrays, each sub-array [k_index, band_index, energy]), 'dos' (array of [energy, total_DOS] pairs).
- Scoring: scored by hidden verifier

### Step 6: Compile average Mulliken charges
- Role: scored
- Action: From the population analysis outputs of both calculations, compute the average Mulliken charge for each element (V, Sb, O in pure; V, Sb, Ti, O in doped) and write a CSV table.
- Output file: `/app/outputs/mulliken_charges_table.csv`
- Format: csv
- Contract: CSV with columns: 'structure' (string, 'pure' or 'doped'), 'atom_type' (string, e.g. 'V', 'Sb', 'Ti', 'O'), 'average_charge' (float).
- Scoring: scored by hidden verifier

### Step 7: Extract V 3d orbital populations
- Role: scored
- Action: From the orbital population data, compute the average occupation of the five 3d components (x²−y², z², xy, xz, yz) per vanadium atom for both structures and write a CSV.
- Output file: `/app/outputs/v_orbital_populations.csv`
- Format: csv
- Contract: CSV with columns: 'structure' (string, 'pure' or 'doped'), 'orbital' (string, e.g. '3d(x^2-y^2)', '3d(z^2)', '3d(xy)', '3d(xz)', '3d(yz)'), 'population' (float, average per V atom).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/pure_band_dos.json`
- `/app/outputs/doped_band_dos.json`
- `/app/outputs/mulliken_charges_table.csv`
- `/app/outputs/v_orbital_populations.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### pure_band_dos.json
- path: `/app/outputs/pure_band_dos.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Band structure and total density of states for pure VSbO4, from which the checker recomputes the Fermi level and verifies DOS peak positions.
- schema:
  - `type`: object
  - `required`:
    - `fermi_energy`: float (eV)
    - `band_energies`: array of arrays, each sub-array [k_index, band_index, energy]
    - `dos`: array of [energy, total_DOS] pairs

### doped_band_dos.json
- path: `/app/outputs/doped_band_dos.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Band structure and total density of states for Ti‑doped VSbO4, used by the checker to verify doping‑induced changes.
- schema:
  - `type`: object
  - `required`:
    - `fermi_energy`: float (eV)
    - `band_energies`: array of arrays, each sub-array [k_index, band_index, energy]
    - `dos`: array of [energy, total_DOS] pairs

### mulliken_charges_table.csv
- path: `/app/outputs/mulliken_charges_table.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Average Mulliken charges for each element in pure and doped structures, compared to the paper's reference values.
- schema:
  - `type`: table
  - `required_columns`: `structure`, `atom_type`, `average_charge`
  - `units`:
    - `average_charge`: e

### v_orbital_populations.csv
- path: `/app/outputs/v_orbital_populations.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: V 3d orbital populations for pure and doped structures, compared to the paper's reported depopulation trends.
- schema:
  - `type`: table
  - `required_columns`: `structure`, `orbital`, `population`
  - `units`:
    - `population`: electrons

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "pure_band_dos.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "fermi_energy": "float (eV)",
          "band_energies": "array of arrays, each sub-array [k_index, band_index, energy]",
          "dos": "array of [energy, total_DOS] pairs"
        }
      },
      "description": "Band structure and total density of states for pure VSbO4, from which the checker recomputes the Fermi level and verifies DOS peak positions."
    },
    {
      "file": "doped_band_dos.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "fermi_energy": "float (eV)",
          "band_energies": "array of arrays, each sub-array [k_index, band_index, energy]",
          "dos": "array of [energy, total_DOS] pairs"
        }
      },
      "description": "Band structure and total density of states for Ti‑doped VSbO4, used by the checker to verify doping‑induced changes."
    },
    {
      "file": "mulliken_charges_table.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "structure",
          "atom_type",
          "average_charge"
        ],
        "units": {
          "average_charge": "e"
        }
      },
      "description": "Average Mulliken charges for each element in pure and doped structures, compared to the paper's reference values."
    },
    {
      "file": "v_orbital_populations.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "structure",
          "orbital",
          "population"
        ],
        "units": {
          "population": "electrons"
        }
      },
      "description": "V 3d orbital populations for pure and doped structures, compared to the paper's reported depopulation trends."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier will independently inspect each of the four output files. For the band/DOS files it will recompute the Fermi level from the supplied DOS data and verify the positions of characteristic DOS peaks. For the charge and orbital population tables it will compare your values to reference numbers with tolerances appropriate for a re‑run using a different code. The final reward is a weighted sum of the stage‑level scores. Reporting numbers directly from the literature is not sufficient; the artifacts must be the output of your actual computational workflow, as the verifier checks for consistency and for the correct structural trends.

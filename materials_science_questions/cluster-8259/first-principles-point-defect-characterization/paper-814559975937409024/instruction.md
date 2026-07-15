# Electronic structure of Pb-based borate-carbonate with oxygen vacancy

## Problem background
The mixed borate-carbonate compound Pb7O(OH)3(CO3)3(BO3) is a non-centrosymmetric non-linear optical material that exhibits a large second-harmonic generation response. Its electronic structure, particularly the band gap and the projection of states onto individual atoms, is critical for understanding and tuning its optical properties. This work investigates the electronic structure of the pristine Pb7O(OH)3(CO3)3(BO3) (structure I) and its oxygen-vacancy variant Pb7(OH)3(CO3)3(BO3) (structure II) using first-principles density functional theory (DFT). The central questions are how the removal of an oxygen atom alters the band gap, the band-gap type (indirect or direct), and the atom-resolved integrated electron counts (obtained by integrating the projected density of states from -6 eV to the Fermi level).

## Approach
The electronic properties are computed with plane-wave DFT using pseudopotentials and an open-source code (Quantum ESPRESSO). Two exchange-correlation functionals are employed: the PBE-GGA functional and a hybrid functional (HSE06) that provides improved band gaps. The computational workflow is as follows:
- The pristine crystal structure (I) is relaxed using PBE-GGA to obtain the equilibrium geometry.
- A PBE-GGA band structure is then calculated along the high-symmetry path Γ-M-K-Γ-A-L-H-A to determine the band gap and its character (indirect/direct).
- An oxygen vacancy is introduced by removing two O(1) atoms from the unit cell (resulting in structure II), and a PBE-GGA band structure is similarly computed for the defective system.
- Hybrid functional (HSE06) calculations are performed for both I and II to obtain more accurate band gaps and angular-momentum-resolved projected density of states (PDOS).
- From the HSE06 PDOS, the total number of electrons (integrated from -6 eV up to the Fermi level) is extracted for each distinct atom type in both structures.
The final results are assembled into two JSON files: band_gaps.json (band gap values and types for both functionals) and integrated_pdos.json (integrated electron counts per atom).

## Reproduction target
Compute and report the band gaps and band-gap types (indirect or direct) for the pristine Pb7O(OH)3(CO3)3(BO3) (I) and the oxygen-vacancy Pb7(OH)3(CO3)3(BO3) (II) structures using both PBE-GGA and a hybrid functional proxy (e.g., HSE06). Additionally, compute the integrated number of electrons per atom (obtained by integrating the total PDOS from -6 eV to the Fermi level) for all unique atom types in both structures. Provide the results in two JSON files under /app/outputs:
- band_gaps.json, with entries for "PBE-GGA" and "mBJ_proxy" for each structure, each containing gap_eV (float) and type ("indirect" or "direct").
- integrated_pdos.json, with per-atom electron counts for the atoms of I (Pb1, Pb2, Pb3, O1, O2, O3, O4, O5, C1, B1, H1) and II (Pb1, Pb2, Pb3, O2, O3, O4, O5, C1, B1, H1).
The results must be obtained by executing the DFT workflow described in the steps; the hidden verifier compares your reported values to expected reference results with tolerances that allow for the use of a different hybrid functional and a different code relative to the original work.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotentials (efficiency or precision library): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Geometry optimization of Pb7O(OH)3(CO3)3(BO3) (I)
- Role: process
- Action: Perform variable-cell relaxation (atomic positions and cell parameters) of the pristine compound I using the PBE-GGA functional. Start from the experimental lattice parameters a=b=10.519 Å, c=8.900 Å, space group P6_3mc, and fractional atomic coordinates from the task description.
- Evidence: `/app/outputs/relaxed_I_structure.txt`

### Step 2: PBE-GGA band structure for I
- Role: process
- Action: Using the relaxed geometry of I, run a self-consistent DFT calculation with PBE-GGA to obtain the Kohn-Sham eigenvalues along the high-symmetry path Γ-M-K-Γ-A-L-H-A. Determine the band gap value and the band-gap type (indirect or direct). Retain the band structure and the extracted quantities for later assembly.
- Evidence: `/app/outputs/I_PBE_band_structure.dat`

### Step 3: Construct vacancy structure II
- Role: process
- Action: Build the defective unit cell for Pb7(OH)3(CO3)3(BO3) by taking the relaxed pristine cell and removing the two oxygen atoms that occupy the O(1) site (the site with fractional coordinates approximately (0.3333, 0.6667, z) and its symmetry-equivalent partner), where z is the relaxed coordinate. The resulting composition has one oxygen vacancy per formula unit.
- Evidence: none

### Step 4: PBE-GGA band structure for II
- Role: process
- Action: Using the constructed geometry of II, run a self-consistent PBE-GGA calculation to obtain the band gap and type. Retain the extracted values.
- Evidence: `/app/outputs/II_PBE_band_structure.dat`

### Step 5: Higher-level functional calculations for I and II
- Role: process
- Action: Perform DFT calculations for both I and II using a hybrid functional (e.g., HSE06) that improves the band gap over PBE. Use the relaxed geometry for I and the constructed geometry for II. Compute the band structures and the angular-momentum-resolved projected density of states (PDOS) for all atom types. Retain the band gap values and the PDOS raw data.
- Evidence: `/app/outputs/I_HSE_pdos.dat`

### Step 6: PDOS integration and electron counting
- Role: process
- Action: From the PDOS computed with the hybrid functional, integrate the total PDOS (sum over all orbitals) for each distinct atom type from -6 eV to the Fermi level (E_F) to obtain the number of electrons contributed by that atom. Perform the integration for I: Pb1, Pb2, Pb3, O1, O2, O3, O4, O5, B, C, H; and for II: Pb1, Pb2, Pb3, O2, O3, O4, O5, B, C, H. Retain the integrated electron counts.
- Evidence: none

### Step 7: Produce band_gaps.json
- Role: scored (load-bearing)
- Action: Create band_gaps.json containing the band gap values (in eV) and gap types ("indirect" or "direct") for both structures under the two levels of theory (PBE-GGA and hybrid functional proxy).
- Output file: `/app/outputs/band_gaps.json`
- Format: json
- Contract: {"I": {"PBE-GGA": {"gap_eV": "float", "type": "'indirect'|'direct'"}, "mBJ_proxy": {"gap_eV": "float", "type": "'indirect'|'direct'"}}, "II": {"PBE-GGA": {"gap_eV": "float", "type": "'indirect'|'direct'"}, "mBJ_proxy": {"gap_eV": "float", "type": "'indirect'|'direct'"}}}
- Scoring: scored by hidden verifier

### Step 8: Produce integrated_pdos.json
- Role: scored (load-bearing)
- Action: Create integrated_pdos.json containing the integrated electron counts (number of electrons per atom) for all atoms in structures I and II, integrated from -6 eV to the Fermi level.
- Output file: `/app/outputs/integrated_pdos.json`
- Format: json
- Contract: {"I": {"Pb1": "float", "Pb2": "float", "Pb3": "float", "O1": "float", "O2": "float", "O3": "float", "O4": "float", "O5": "float", "C1": "float", "B1": "float", "H1": "float"}, "II": {"Pb1": "float", "Pb2": "float", "Pb3": "float", "O2": "float", "O3": "float", "O4": "float", "O5": "float", "C1": "float", "B1": "float", "H1": "float"}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gaps.json`
- `/app/outputs/integrated_pdos.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gaps.json
- path: `/app/outputs/band_gaps.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Band gap values (in eV) and gap types for pristine I and defective II, computed with PBE-GGA and a hybrid functional (replacing mBJ).
- schema:
  - `type`: object
  - `required`:
    - `I`:
      - `PBE-GGA`:
        - `gap_eV`: number
        - `type`: string ("indirect" or "direct")
      - `mBJ_proxy`:
        - `gap_eV`: number
        - `type`: string ("indirect" or "direct")
    - `II`:
      - `PBE-GGA`:
        - `gap_eV`: number
        - `type`: string ("indirect" or "direct")
      - `mBJ_proxy`:
        - `gap_eV`: number
        - `type`: string ("indirect" or "direct")

### integrated_pdos.json
- path: `/app/outputs/integrated_pdos.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Integrated number of electrons (dimensionless) per atom from -6 eV to the Fermi level, for pristine I and defective II, obtained from hybrid-functional PDOS.
- schema:
  - `type`: object
  - `required`:
    - `I`:
      - `Pb1`: number
      - `Pb2`: number
      - `Pb3`: number
      - `O1`: number
      - `O2`: number
      - `O3`: number
      - `O4`: number
      - `O5`: number
      - `C1`: number
      - `B1`: number
      - `H1`: number
    - `II`:
      - `Pb1`: number
      - `Pb2`: number
      - `Pb3`: number
      - `O2`: number
      - `O3`: number
      - `O4`: number
      - `O5`: number
      - `C1`: number
      - `B1`: number
      - `H1`: number

Notes: The checker compares the reported values to the paper's results with tolerances appropriate for a different code (Quantum ESPRESSO vs WIEN2k) and a different hybrid functional (HSE06 vs mBJ).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gaps.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "I": {
            "PBE-GGA": {
              "gap_eV": "number",
              "type": "string (\"indirect\" or \"direct\")"
            },
            "mBJ_proxy": {
              "gap_eV": "number",
              "type": "string (\"indirect\" or \"direct\")"
            }
          },
          "II": {
            "PBE-GGA": {
              "gap_eV": "number",
              "type": "string (\"indirect\" or \"direct\")"
            },
            "mBJ_proxy": {
              "gap_eV": "number",
              "type": "string (\"indirect\" or \"direct\")"
            }
          }
        }
      },
      "description": "Band gap values (in eV) and gap types for pristine I and defective II, computed with PBE-GGA and a hybrid functional (replacing mBJ)."
    },
    {
      "file": "integrated_pdos.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "I": {
            "Pb1": "number",
            "Pb2": "number",
            "Pb3": "number",
            "O1": "number",
            "O2": "number",
            "O3": "number",
            "O4": "number",
            "O5": "number",
            "C1": "number",
            "B1": "number",
            "H1": "number"
          },
          "II": {
            "Pb1": "number",
            "Pb2": "number",
            "Pb3": "number",
            "O2": "number",
            "O3": "number",
            "O4": "number",
            "O5": "number",
            "C1": "number",
            "B1": "number",
            "H1": "number"
          }
        }
      },
      "description": "Integrated number of electrons (dimensionless) per atom from -6 eV to the Fermi level, for pristine I and defective II, obtained from hybrid-functional PDOS."
    }
  ],
  "notes": "The checker compares the reported values to the paper's results with tolerances appropriate for a different code (Quantum ESPRESSO vs WIEN2k) and a different hybrid functional (HSE06 vs mBJ)."
}
```

## How you are scored
A hidden verifier independently scores your submission. It reads the two output files band_gaps.json and integrated_pdos.json and checks their structure against the output contract. For band_gaps.json, it compares the band gap values and gap types for each structure/functional combination to the expected reference values; the band gaps must fall within an allowed tolerance, and the gap types must match exactly. For integrated_pdos.json, it compares the per-atom integrated electron counts to reference values using a relative tolerance. The band gap portion (values and types) carries 70% weight, and the integrated PDOS portion carries 30% weight. The final score is a weighted combination of the scores for each artifact. You must obtain the numbers by running the prescribed DFT calculations; the verifier does not recompute the raw data and directly evaluates the reported results.

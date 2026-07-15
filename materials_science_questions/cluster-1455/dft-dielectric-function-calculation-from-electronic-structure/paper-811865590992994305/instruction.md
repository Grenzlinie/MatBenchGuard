# DFT prediction of electronic, dielectric, dynamic, and elastic properties of a magnesium boron nitride compound

## Problem background
Magnesium nitridoboride (MgNB₉) is a relatively unexplored boron-rich compound that could be of interest for optoelectronic applications. Its electronic, dielectric, vibrational, and elastic properties have not been previously characterized, either experimentally or theoretically. This task aims to compute these fundamental physical properties from first-principles using density functional theory, thereby providing a set of benchmark predictions for the compound. By carrying out the calculations as described, the resulting quantities—band gap, dielectric tensors, Born charges, phonon frequencies, static dielectric response, elastic constants, and polycrystalline moduli—will characterize the material and allow comparison with known semiconductors.

## Approach
The task is a first-principles computational workflow based on density functional theory (DFT) and density functional perturbation theory (DFPT). The crystal structure of MgNB₉ (space group R‑3m) is constructed in the rhombohedral primitive cell at the experimental lattice parameters (a_rh = 7.4096 Å, α_rh = 43.539°). The electronic ground state is obtained with the PBE generalized gradient approximation and norm-conserving pseudopotentials. After a self-consistent field (SCF) calculation to converge the charge density, a non‑self‑consistent band‑structure run on the F–Γ–Z–L–Γ high‑symmetry path determines the indirect band gap. Next, DFPT linear‑response calculations yield the electronic dielectric tensor ε^∞ and the Born effective charge tensors for each symmetry‑inequivalent atom. The same DFPT framework is used to compute the dynamical matrix at the Γ point; diagonalizing it gives the zone‑center phonon frequencies. The LO–TO splitting for infrared‑active modes is obtained by combining the dynamical matrix with ε^∞ and the Born charges. Using the phonon eigenvectors, Born charges, and frequencies, the mode oscillator strengths are evaluated and the static dielectric tensor ε^0 is collected from the electronic and ionic contributions. A separate set of DFPT calculations under strain perturbations provides the relaxed‑ion elastic stiffness constants. Finally, the polycrystalline bulk and shear moduli are computed from the elastic constants via the Voigt approximation, and the Born stability criteria verify mechanical stability. The entire pipeline is executed with an open‑source plane‑wave pseudopotential code (ABINIT or an equivalent package that supports DFPT) and standard pseudopotentials from public libraries.

## Reproduction target
Produce a single JSON file, /app/outputs/results.json, that contains all of the following computed properties for the rhombohedral MgNB₉ crystal at the experimental lattice parameters (a_rh = 7.4096 Å, α_rh = 43.539°):

1. The indirect band gap (in eV).
2. The electronic dielectric tensor components ε⊥^∞ and ε∥^∞.
3. The Born effective charge tensors (3×3 matrices) for the five symmetry‑inequivalent atoms: Mg, N, B1, B2, and B3.
4. The zone‑center phonon frequencies with their irreducible representation labels and LO/TO characters (for infrared‑active modes) or a null label for silent modes.
5. The static dielectric tensor components ε⊥^0 and ε∥^0.
6. The relaxed‑ion elastic stiffness constants C11, C12, C13, C14, C33, and C44.
7. The bulk modulus B and shear modulus G (in GPa) obtained from the elastic constants via the Voigt approximation.

The results must be formatted exactly as specified in the output contract (see the ‘Output contract’ section).

## Assets

- ABINIT (or equivalent open-source plane-wave pseudopotential DFT code): https://www.abinit.org/
- Troullier-Martins norm-conserving pseudopotentials for Mg, N, B (PBE-GGA): https://www.abinit.org/downloads/pseudopotentials
- Crystal structure of MgNB9 (rhombohedral) from literature: 10.1107/S0108270102014887

## Workflow steps

### Step 1: Structure setup
- Role: process
- Action: Build the MgNB9 crystal structure in the rhombohedral unit cell using the experimental lattice parameters a_rh = 7.4096 Å, α_rh = 43.539° and the Wyckoff positions from the literature. Prepare the DFT input file with the structure and a standard k-point grid.
- Evidence: none

### Step 2: Ground-state SCF and band structure
- Role: process
- Action: Run a self-consistent field (SCF) DFT calculation to obtain the ground-state charge density and wavefunctions. Then perform a non-self-consistent band structure calculation on a denser k-path (F–Γ–Z–L–Γ) to determine the indirect band gap.
- Evidence: none

### Step 3: DFPT: electronic dielectric tensor and Born effective charges
- Role: process
- Action: Using density functional perturbation theory (DFPT), compute the electronic dielectric tensor ε^∞ and the Born effective charge tensors Z* for the symmetry-inequivalent atoms. Extract the diagonal components ε⊥^∞, ε∥^∞ and the 3×3 Z* matrices for Mg, N, and the three distinct B sites.
- Evidence: none

### Step 4: DFPT: zone-center phonon frequencies and LO-TO splitting
- Role: process
- Action: Perform a DFPT calculation of the dynamical matrix at the Γ point, diagonalize to obtain phonon eigenfrequencies and eigenvectors, and incorporate the LO-TO splitting using the previously obtained ε^∞ and Born charges. Classify frequencies by irreducible representation and record all TO and LO values for the infrared-active A₂ᵤ and Eᵤ modes, as well as silent mode frequencies.
- Evidence: none

### Step 5: Post-process: static dielectric tensor
- Role: process
- Action: Using the phonon eigenvectors, Born charges, and frequencies, compute the mode oscillator strengths and the ionic contribution to the static dielectric tensor ε^0 (dielectric constant parallel ε∥^0 and perpendicular ε⊥^0).
- Evidence: none

### Step 6: DFPT: elastic constants
- Role: process
- Action: Perform a DFPT calculation of the elastic tensor under strain perturbations to obtain the relaxed-ion elastic stiffness constants C11, C12, C13, C14, C33, and C44.
- Evidence: none

### Step 7: Post-process: mechanical stability and moduli
- Role: process
- Action: Verify the Born mechanical stability criteria for a trigonal structure using the computed elastic constants. Calculate the bulk modulus B and shear modulus G via the Voigt approximation.
- Evidence: none

### Step 8: Aggregated property output
- Role: scored (load-bearing)
- Action: Collect all computed quantities from the previous steps (indirect band gap, electronic dielectric tensor components, Born effective charge tensors, zone-center phonon frequencies with LO/TO labels, static dielectric tensor components, elastic stiffness constants, bulk modulus, and shear modulus) and write them to /app/outputs/results.json in the specified schema.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: object with keys: band_gap (float, eV), eps_inf_perp (float), eps_inf_par (float), born_charges (object: keys Mg, N, B1, B2, B3 each a 3x3 array of floats), phonon_frequencies (array of objects with keys: irrep (string), frequency (float, cm⁻¹), lo_or_to (string 'TO' | 'LO' | null)), eps0_perp (float), eps0_par (float), elastic_constants (object with keys C11, C12, C13, C14, C33, C44 as floats), bulk_modulus (float, GPa), shear_modulus (float, GPa).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Aggregated file containing all computed physical properties: band gap, electronic and static dielectric tensors, Born effective charges, zone-center phonon frequencies (with LO/TO labeling), elastic constants, and derived polycrystalline moduli.
- schema:
  - `type`: object
  - `required`:
    - `band_gap`: number (eV)
    - `eps_inf_perp`: number
    - `eps_inf_par`: number
    - `born_charges`:
      - `Mg`: 3x3 array of numbers
      - `N`: 3x3 array of numbers
      - `B1`: 3x3 array of numbers
      - `B2`: 3x3 array of numbers
      - `B3`: 3x3 array of numbers
    - `phonon_frequencies`:
      - `irrep`: string
      - `frequency`: number (cm⁻¹)
      - `lo_or_to`: string: 'TO', 'LO', or null
    - `eps0_perp`: number
    - `eps0_par`: number
    - `elastic_constants`:
      - `C11`: number (GPa)
      - `C12`: number
      - `C13`: number
      - `C14`: number
      - `C33`: number
      - `C44`: number
    - `bulk_modulus`: number (GPa)
    - `shear_modulus`: number (GPa)

Notes: All properties correspond to the rhombohedral MgNB9 crystal at experimental lattice parameters. Phonon frequencies include LO/TO splitting for IR-active modes. Elastic constants are for the relaxed-ion tensor.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "band_gap": "number (eV)",
          "eps_inf_perp": "number",
          "eps_inf_par": "number",
          "born_charges": {
            "Mg": "3x3 array of numbers",
            "N": "3x3 array of numbers",
            "B1": "3x3 array of numbers",
            "B2": "3x3 array of numbers",
            "B3": "3x3 array of numbers"
          },
          "phonon_frequencies": [
            {
              "irrep": "string",
              "frequency": "number (cm⁻¹)",
              "lo_or_to": "string: 'TO', 'LO', or null"
            }
          ],
          "eps0_perp": "number",
          "eps0_par": "number",
          "elastic_constants": {
            "C11": "number (GPa)",
            "C12": "number",
            "C13": "number",
            "C14": "number",
            "C33": "number",
            "C44": "number"
          },
          "bulk_modulus": "number (GPa)",
          "shear_modulus": "number (GPa)"
        }
      },
      "description": "Aggregated file containing all computed physical properties: band gap, electronic and static dielectric tensors, Born effective charges, zone-center phonon frequencies (with LO/TO labeling), elastic constants, and derived polycrystalline moduli."
    }
  ],
  "notes": "All properties correspond to the rhombohedral MgNB9 crystal at experimental lattice parameters. Phonon frequencies include LO/TO splitting for IR-active modes. Elastic constants are for the relaxed-ion tensor."
}
```

## How you are scored
A hidden verifier will read your /app/outputs/results.json and compare each entry to a set of hidden reference values derived from the original study. The comparison uses appropriate tolerances that account for legitimate method variation (different code, pseudopotential, or numerical settings) while still requiring that every property be computed genuinely. Each property category contributes a fraction of the total reward, with higher weight on the most critical results (band gap, dielectric tensors, phonon frequencies, elastic constants). Your final score is a weighted average of these per‑property scores.

Simply reporting numbers without actually running the DFT/DFPT pipeline will not yield a consistent set of results across the different properties, because the values are interdependent (e.g., the static dielectric constant depends on the electronic dielectric tensor, Born charges, and phonon frequencies). The verifier checks that the reported quantities are internally plausible for a genuine calculation. To succeed, you must carry out the entire workflow and write the resulting values into results.json.

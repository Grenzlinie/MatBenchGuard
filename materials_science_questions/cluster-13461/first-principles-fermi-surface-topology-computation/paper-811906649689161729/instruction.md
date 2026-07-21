# First-principles structural and electronic properties of cubic antifluorite compounds

## Problem background
This work investigates the structural and electronic properties of four cubic antifluorite-type (CaF₂) compounds: Be₂B and its ternary derivatives AlBeB, MgBeB, and NaBeB. These materials are of interest because they may exhibit superconductivity, and substituting Be with other light elements (Al, Mg, Na) could tune the electronic structure near the Fermi level. The goal is to compute equilibrium lattice constants, bulk moduli, and key electronic quantities—valence bandwidth, the Γ–X band gap, total density of states at the Fermi level, and B-p projected DOS at the Fermi level—for all four compounds using first‑principles density‑functional theory within the generalized gradient approximation (GGA). The computed quantities allow assessment of how chemical substitutions affect structural cohesion and the electronic density of states that governs potential superconducting behavior.

## Approach
Use a full‑potential linearized augmented plane wave (FP‑LAPW) code such as the open‑source ELK (http://elk.sourceforge.net/) or FLEUR, with the PBE‑GGA exchange‑correlation functional. This method expands the Kohn–Sham orbitals in atomic‑like orbitals inside muffin‑tin spheres and plane waves in the interstitial region, matching the methodology of the reference paper. For each compound, construct the cubic CaF₂‑type crystal structure (space group Fm‑3m) with B at (0,0,0) and Be at (0.25,0.25,0.25); for the ternary phases replace one Be atom with the substituting atom at the same site.

**Essential convergence parameters (from the paper):**  
- Muffin‑tin radii (in atomic units, bohr): Be = 1.5, B = 1.55, Mg = 1.7, Na = 1.75, Al = 1.8.  
- Basis cut‑off: RMT × Kmax = 8 (where Kmax is the plane‑wave cut‑off and RMT is the smallest muffin‑tin radius).  
- Maximum angular momentum for the wave‑function expansion inside spheres: lmax = 10.  
- k‑point mesh: 8 × 8 × 8 Monkhorst–Pack grid.  
- Self‑consistency threshold: total energy converged to 1 × 10⁻³ Ry.  

Carry out a series of self‑consistent field (SCF) calculations at different unit‑cell volumes to obtain the total energy as a function of volume. Fit these energy‑volume data to the Murnaghan equation of state to extract the equilibrium lattice constant and bulk modulus. Then, at the equilibrium volume, run a full SCF calculation followed by a band‑structure calculation along high‑symmetry paths and a density‑of‑states (DOS) calculation. From the band structure, extract the valence bandwidth (energy span from the bottom of the lowest valence band to the top of the valence band) and the Γ–X band gap (difference between the lowest conduction band at X and the highest valence band at Γ). From the DOS, extract the total DOS at the Fermi level and the B p‑projected DOS at the Fermi level. Compile all extracted values into a structured JSON file following the output contract.

## Reproduction target
Produce a single scored artifact `/app/outputs/computed_properties.json` containing an array of four objects, one for each compound in the fixed order: Be₂B, AlBeB, MgBeB, NaBeB. Each object must include the keys: `compound` (string), `lattice_constant_angstrom` (number), `bulk_modulus_GPa` (number), `valence_bandwidth_eV` (number), `band_gap_Gamma_X_eV` (number), `total_DOS_at_EF_states_per_eV_cell` (number), and `B_p_DOS_at_EF_states_per_eV_cell` (number). All values must be obtained from the PBE‑GGA FP‑LAPW workflow described above. No other output file is scored.

## Assets

- ELK FP‑LAPW code: http://elk.sourceforge.net/  
- ELK input reference: http://elk.sourceforge.net/elk_manual.pdf

## Workflow steps

### Step 1: Define crystal structures
- Role: process
- Action: Define the cubic CaF₂-type (space group Fm-3m) crystal structures for the four compounds: Be₂B, AlBeB, MgBeB, NaBeB. Specify atomic positions: Be at (0.25,0.25,0.25), B at (0,0,0); for the ternary phases, replace one Be atom with the substituting atom (Al, Mg, Na) at the same fractional coordinate.
- Evidence: none

### Step 2: Run DFT volume scans
- Role: process
- Action: Perform DFT self-consistent field (SCF) calculations using the FP-LAPW method with the PBE-GGA exchange-correlation functional for each compound at a series of unit-cell volumes to obtain total energy vs. volume data. Use the convergence parameters listed in the Approach section.
- Evidence: none

### Step 3: Fit equation of state and extract structural parameters
- Role: process
- Action: Fit the total-energy vs. volume data from step-02 to the Murnaghan equation of state. Extract the equilibrium lattice constant and bulk modulus for each compound.
- Evidence: none

### Step 4: Compute electronic structure at equilibrium volume
- Role: process
- Action: Using the equilibrium lattice constants from step-03, perform DFT SCF calculations at the equilibrium volume for each compound. Then compute the electronic band structure along high-symmetry lines and the density of states (DOS).
- Evidence: none

### Step 5: Extract electronic quantities
- Role: process
- Action: From the band structure obtained in step-04, extract the valence bandwidth (energy difference between the top of the valence band and the bottom of the lowest valence band) and the Γ–X band gap (lowest conduction band at X minus highest valence band at Γ). From the DOS, extract the total DOS at the Fermi level and the B p-projected DOS at the Fermi level for each compound.
- Evidence: none

### Step 6: Compile scored output
- Role: scored (load-bearing)
- Action: Read the structural parameters (from step-03) and electronic quantities (from step-05) and compile the final scored output file `computed_properties.json`, containing an array of four objects, one per compound (order: Be₂B, AlBeB, MgBeB, NaBeB). Each object must include the keys: compound, lattice_constant_angstrom, bulk_modulus_GPa, valence_bandwidth_eV, band_gap_Gamma_X_eV, total_DOS_at_EF_states_per_eV_cell, B_p_DOS_at_EF_states_per_eV_cell.
- Output file: `/app/outputs/computed_properties.json`
- Format: json
- Contract: Array of objects, each with keys: compound (string), lattice_constant_angstrom (number), bulk_modulus_GPa (number), valence_bandwidth_eV (number), band_gap_Gamma_X_eV (number), total_DOS_at_EF_states_per_eV_cell (number), B_p_DOS_at_EF_states_per_eV_cell (number). One entry per compound in the fixed order Be2B, AlBeB, MgBeB, NaBeB.
- Scoring: scored by hidden verifier

## Output files
Write the required artifact under `/app/outputs`:
- `/app/outputs/computed_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write the file under `/app/outputs` and follow its schema exactly.

### computed_properties.json
- path: `/app/outputs/computed_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Contains the six computed properties for each of the four antifluorite compounds. The checker compares each value to the paper's GGA reference using predefined relative tolerances.
- schema:
  - `type`: array
  - `description`: Array of four objects, one per compound, in the fixed order: Be2B, AlBeB, MgBeB, NaBeB.
  - `items`:
    - `type`: object
    - `required`: `compound`, `lattice_constant_angstrom`, `bulk_modulus_GPa`, `valence_bandwidth_eV`, `band_gap_Gamma_X_eV`, `total_DOS_at_EF_states_per_eV_cell`, `B_p_DOS_at_EF_states_per_eV_cell`
    - `properties`:
      - `compound`:
        - `type`: string
        - `description`: Name of the compound
      - `lattice_constant_angstrom`:
        - `type`: number
        - `units`: angstrom
        - `description`: Equilibrium lattice constant
      - `bulk_modulus_GPa`:
        - `type`: number
        - `units`: GPa
        - `description`: Bulk modulus from Murnaghan EOS fit
      - `valence_bandwidth_eV`:
        - `type`: number
        - `units`: eV
        - `description`: Valence bandwidth (top of valence band minus bottom of lowest valence band)
      - `band_gap_Gamma_X_eV`:
        - `type`: number
        - `units`: eV
        - `description`: Γ-X band gap (lowest conduction band at X minus highest valence band at Γ)
      - `total_DOS_at_EF_states_per_eV_cell`:
        - `type`: number
        - `units`: states/eV/cell
        - `description`: Total density of states at the Fermi level
      - `B_p_DOS_at_EF_states_per_eV_cell`:
        - `type`: number
        - `units`: states/eV/cell
        - `description`: B p-projected DOS at the Fermi level

Notes: Only GGA (PBE) results are required; the LDA values are not scored. The agent must use the FP‑LAPW methodology and the convergence parameters listed in the Approach section. The output order is fixed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "description": "Array of four objects, one per compound, in the fixed order: Be2B, AlBeB, MgBeB, NaBeB.",
        "items": {
          "type": "object",
          "required": [
            "compound",
            "lattice_constant_angstrom",
            "bulk_modulus_GPa",
            "valence_bandwidth_eV",
            "band_gap_Gamma_X_eV",
            "total_DOS_at_EF_states_per_eV_cell",
            "B_p_DOS_at_EF_states_per_eV_cell"
          ],
          "properties": {
            "compound": {
              "type": "string",
              "description": "Name of the compound"
            },
            "lattice_constant_angstrom": {
              "type": "number",
              "units": "angstrom",
              "description": "Equilibrium lattice constant"
            },
            "bulk_modulus_GPa": {
              "type": "number",
              "units": "GPa",
              "description": "Bulk modulus from Murnaghan EOS fit"
            },
            "valence_bandwidth_eV": {
              "type": "number",
              "units": "eV",
              "description": "Valence bandwidth (top of valence band minus bottom of lowest valence band)"
            },
            "band_gap_Gamma_X_eV": {
              "type": "number",
              "units": "eV",
              "description": "Γ-X band gap (lowest conduction band at X minus highest valence band at Γ)"
            },
            "total_DOS_at_EF_states_per_eV_cell": {
              "type": "number",
              "units": "states/eV/cell",
              "description": "Total density of states at the Fermi level"
            },
            "B_p_DOS_at_EF_states_per_eV_cell": {
              "type": "number",
              "units": "states/eV/cell",
              "description": "B p-projected DOS at the Fermi level"
            }
          }
        }
      },
      "description": "Contains the six computed properties for each of the four antifluorite compounds. The checker compares each value to the paper's GGA reference using predefined relative tolerances."
    }
  ],
  "notes": "Only GGA (PBE) results are required; the LDA values are not scored. The agent must use the FP‑LAPW methodology and the convergence parameters listed in the Approach section. The output order is fixed."
}
```

## How you are scored
A hidden verifier reads your `computed_properties.json` and compares every reported value to the paper’s GGA result for the same compound and quantity using domain-appropriate relative tolerances. The reward is the fraction of the 24 comparisons (6 quantities × 4 compounds) that fall within the tolerance. The comparison is directional: your result must be close to the reference value; being closer is better, and extreme outliers reduce the score. No other artifacts contribute to the final reward. You must actually run the FP‑LAPW pipeline; the verifier may also perform lightweight consistency checks on the process evidence files, but the primary score comes from the numeric comparisons.
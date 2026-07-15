# DFT Adsorption and C–H Bond Activation on Metal Dioxide Surfaces

## Problem background
Converting methane, the main component of natural gas, into valuable chemicals requires breaking its strong, nonpolar C–H bonds. Heterogeneous catalysts based on transition-metal oxides can facilitate this bond scission. The (110) surface of rutile-type IrO₂ has been shown to adsorb methane unusually strongly and to activate the C–H bond below room temperature. To understand the origin of this activity and to screen for other potentially superior catalysts, this task investigates the adsorption and C–H bond dissociation of methane on the stoichiometric (110) surfaces of three rutile-related metal dioxides: IrO₂, CrO₂, and β-PtO₂. The main questions are: how large are the adsorption energies and activation barriers, how much charge is transferred upon adsorption, and what is the strength of the metal–methyl bond formed after dissociation? Answering these questions requires first-principles calculations of the adsorption structures, reaction paths, and electronic structure.

## Approach
Periodic density functional theory (DFT) with the PBE functional is used, together with a Hubbard U correction for the Pt 5d states in β-PtO₂. The (110) surfaces are modelled as slabs with a vacuum gap. For each oxide a clean surface slab and an isolated methane molecule are computed as references. Methane is then placed on the surface and its geometry optimized to obtain the adsorption energy. Bader charge analysis quantifies the net electron transfer between methane and the surface. The minimum energy path for C–H bond cleavage is determined with the climbing-image nudged elastic band (CI-NEB) method, which yields both the true activation barrier and the heat of reaction. To understand the orbital interactions that control the catalytic activity, we rely on the projected crystal orbital Hamilton population (pCOHP) technique implemented in the LOBSTER package. The COHP for the metal–CH₃ bond in the dissociated state is integrated up to the Fermi level (ICOHP) to compare bond strengths. For the IrO₂ surface, the pCOHP of the elongated C–H bond in the adsorbed state is computed to reveal the bonding and antibonding features responsible for methane activation. The comparison across the three surfaces reveals how the energy of the metal dₓ² orbital and the radial extent of the d orbitals affect the catalytic activity.

## Reproduction target
For each of the three surfaces (IrO₂, CrO₂, β-PtO₂) you must compute and report:
1. The adsorption energy (E_ad, kcal/mol) and the Bader charge (e) of the adsorbed methane molecule.
2. The true activation energy (E_a, kcal/mol) and the heat of reaction (E_r, kcal/mol) for the first C–H bond dissociation.
3. The integrated crystal orbital Hamilton population (ICOHP, eV) for the metal–CH₃ bond at the dissociative final state.
In addition, for the IrO₂ surface only, you must produce:
4. The -pCOHP curve for the activated C–H bond as a function of energy relative to the Fermi level (range at least −15 to +5 eV).
5. The energies (eV) of the main occupied bonding peak (maximum -pCOHP below E_F) and any unoccupied bonding peak located between 1 and 2 eV.
These quantities are written to the specified output files; the numerical values must be computed using the slab geometries and computational settings described in the workflow steps.

## Assets

- Plane-wave DFT code with PBE functional and DFT+U capability (e.g., Quantum ESPRESSO): https://www.quantum-espresso.org
- LOBSTER (Local Orbital Basis Suite Towards Electronic-Structure Reconstruction): https://www.cohp.de
- Bader charge analysis code (Henkelman et al.): http://theory.cm.utexas.edu/bader/
- Crystal structures of IrO₂, CrO₂, and β-PtO₂ in rutile and distorted rutile forms: Materials Project: mp-20259 (IrO₂), mp-10124 (β-PtO₂), mp-15153 (CrO₂)

## Workflow steps

### Step 1: Bulk crystal structure optimization
- Role: process
- Action: Optimize the bulk crystal structures of IrO₂, CrO₂, and β-PtO₂ using plane-wave DFT with PBE functional (and DFT+U: U_eff=7.5 eV for Pt 5d in β-PtO₂). Use the CIF files obtained from Materials Project as starting geometries. Relax cell shape and ionic positions until forces converge. Save the final lattice parameters and relaxed coordinates.
- Evidence: `/app/outputs/bulk_optimization.log`

### Step 2: Surface slab construction and relaxation
- Role: process
- Action: From the optimized bulk structures, build slab models of the (110) surface for each dioxide: a p(3×1) supercell with 12 atomic layers (4 O–M–O trilayers) and a 15 Å vacuum gap. Fix the bottom 6 atomic layers. Relax the clean surface geometries (ions only) using DFT to obtain total energies and relaxed surface structures. Also perform a single-point calculation for an isolated CH₄ molecule placed in a large vacuum box (22 Å cubic cell) to obtain its total energy.
- Evidence: `/app/outputs/surface_relaxation.log`

### Step 3: CH₄ adsorption, NEB, and ICOHP computation
- Role: scored (load-bearing)
- Action: For each surface (IrO₂, CrO₂, β-PtO₂): (1) optimize the geometry of a methane molecule adsorbed on the surface; (2) compute the adsorption energy E_ad = E(CH₄/surf) – E(CH₄) – E(surf); (3) perform Bader charge analysis on the adsorbed CH₄; (4) use the climbing-image nudged elastic band (CI-NEB) method to locate the transition state and final state (co‑adsorbed CH₃ + H) for C–H bond dissociation; (5) from the NEB results, extract the true activation energy E_a and the heat of reaction E_r; (6) from the final-state wavefunction, compute the projected COHP and integrate ICOHP for the metal–CH₃ bond. Report all quantities in a CSV file.
- Output file: `/app/outputs/adsorption_results.csv`
- Format: csv
- Contract: Columns: surface (str), E_ad (float, kcal/mol), CH4_charge (float, electron charge), E_a (float, kcal/mol), E_r (float, kcal/mol), ICOHP_M-CH3 (float, eV). Write a header row. One row per surface.
- Scoring: scored by hidden verifier

### Step 4: pCOHP analysis of IrO₂ C-H bond
- Role: scored (load-bearing)
- Action: Using the adsorbed methane wavefunction on IrO₂(110) from Step 3, run LOBSTER to compute the projected crystal orbital Hamilton population (pCOHP) for the elongated C–H bond. Save the −pCOHP values as a function of energy relative to the Fermi level in a CSV (two columns, no header).
- Output file: `/app/outputs/pCOHP_IrO2_CH.csv`
- Format: csv
- Contract: Two-column CSV with no header row. Column 1: energy relative to Fermi level (eV). Column 2: -pCOHP (arbitrary units). Data must cover at least the range from -15 eV to +5 eV.
- Scoring: scored by hidden verifier

### Step 5: pCOHP peak information for IrO₂
- Role: scored
- Action: Extract from the pCOHP analysis the energies of the main occupied bonding peak (maximum -pCOHP below E_F) and the unoccupied bonding peak lying between 1 and 2 eV. Write a single line of text in the format: 'Occupied bonding peak at X.X eV; Unoccupied bonding peak at X.X eV.'
- Output file: `/app/outputs/pCOHP_peak_info.txt`
- Format: txt
- Contract: Plain text with the exact format: 'Occupied bonding peak at X.X eV; Unoccupied bonding peak at X.X eV.'
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/adsorption_results.csv`
- `/app/outputs/pCOHP_IrO2_CH.csv`
- `/app/outputs/pCOHP_peak_info.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### adsorption_results.csv
- path: `/app/outputs/adsorption_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Machine-readable table of computed adsorption energies, Bader charges, activation barriers, and metal–CH3 ICOHP for the three surfaces.
- schema:
  - `type`: table
  - `required_columns`: `surface`, `E_ad (kcal/mol)`, `CH4_charge (e)`, `E_a (kcal/mol)`, `E_r (kcal/mol)`, `ICOHP_M-CH3 (eV)`
  - `notes`: One row per surface. Values compared to hidden reference values with tolerances.

### pCOHP_IrO2_CH.csv
- path: `/app/outputs/pCOHP_IrO2_CH.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: The -pCOHP spectrum for the activated C-H bond on IrO₂(110).
- schema:
  - `type`: table
  - `header`: False
  - `columns`:
    - `index`: 0
    - `name`: energy
    - `unit`: eV
    - `description`: Energy relative to Fermi level
    - `index`: 1
    - `name`: neg_pCOHP
    - `unit`: arbitrary
    - `description`: Negative projected COHP value
  - `notes`: Data must cover at least -15 to +5 eV. Checker audits structural features (presence of bonding peak below E_F and unoccupied peak in 1-2 eV).

### pCOHP_peak_info.txt
- path: `/app/outputs/pCOHP_peak_info.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Plain-text statement of the key pCOHP peak energies.
- schema:
  - `type`: text
  - `pattern`: Occupied bonding peak at {value} eV; Unoccupied bonding peak at {value} eV.
  - `notes`: Peak energies compared to hidden reference within ±0.25 eV tolerance.

Notes: The adsorption_results.csv values are compared to the paper-reported figures with appropriate tolerances; relative trends are also enforced. The pCOHP curve is structurally audited, and peak positions are verified via the second file.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "adsorption_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "surface",
          "E_ad (kcal/mol)",
          "CH4_charge (e)",
          "E_a (kcal/mol)",
          "E_r (kcal/mol)",
          "ICOHP_M-CH3 (eV)"
        ],
        "notes": "One row per surface. Values compared to hidden reference values with tolerances."
      },
      "description": "Machine-readable table of computed adsorption energies, Bader charges, activation barriers, and metal–CH3 ICOHP for the three surfaces."
    },
    {
      "file": "pCOHP_IrO2_CH.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "header": false,
        "columns": [
          {
            "index": 0,
            "name": "energy",
            "unit": "eV",
            "description": "Energy relative to Fermi level"
          },
          {
            "index": 1,
            "name": "neg_pCOHP",
            "unit": "arbitrary",
            "description": "Negative projected COHP value"
          }
        ],
        "notes": "Data must cover at least -15 to +5 eV. Checker audits structural features (presence of bonding peak below E_F and unoccupied peak in 1-2 eV)."
      },
      "description": "The -pCOHP spectrum for the activated C-H bond on IrO₂(110)."
    },
    {
      "file": "pCOHP_peak_info.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "pattern": "Occupied bonding peak at {value} eV; Unoccupied bonding peak at {value} eV.",
        "notes": "Peak energies compared to hidden reference within ±0.25 eV tolerance."
      },
      "description": "Plain-text statement of the key pCOHP peak energies."
    }
  ],
  "notes": "The adsorption_results.csv values are compared to the paper-reported figures with appropriate tolerances; relative trends are also enforced. The pCOHP curve is structurally audited, and peak positions are verified via the second file."
}
```

## How you are scored
A hidden verifier independently inspects each scored artifact. The verifier compares your computed values against independently derived reference data using numerical tolerances appropriate for DFT reproducibility. The -pCOHP curve is checked for the presence of the required bonding features (a pronounced occupied peak below the Fermi level and a peak between 1–2 eV). The final score is a weighted sum of the scores from all scored stages. Simply reporting numbers found in the literature is insufficient; the verifier may also check internal consistency and relative trends among the three surfaces. Honest execution of the full DFT workflow is required to obtain full credit.

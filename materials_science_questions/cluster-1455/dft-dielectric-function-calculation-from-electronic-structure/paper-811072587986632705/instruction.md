# DFT and TD-DFT study of ferrocene: UV/Vis spectrum assignment and NBO donor-acceptor interactions

## Problem background
Ferrocene (FeC₁₀H₁₀) is a prototypical organometallic compound with a sandwich structure that exhibits interesting electronic and optical properties, making it relevant for molecular switches and semiconductor devices. Its experimental UV/Vis absorption spectrum shows several bands, but the precise electronic origin of these transitions—whether they are primarily metal-centered d–d or metal-to-ligand charge-transfer—has been discussed in the literature. The goal of this task is to use computational methods to assign the principal absorption bands of the monoclinic type‑I ferrocene crystal to specific orbital transitions and to quantify the covalent interactions between iron and the cyclopentadienyl (Cp) rings.

## Approach
The task follows a molecular DFT approach. Starting from the experimentally determined crystal structure of ferrocene type I (CCDC 2101933), the geometry is first optimized at the B3LYP level using a mixed basis set (an effective‑core potential for Fe and an all‑electron triple‑zeta basis for C and H). The optimized geometry is then used for two subsequent analyses:

1. **TD‑DFT UV/Vis calculation** – a time‑dependent DFT calculation of the lowest singlet excited states yields the absorption peaks and the dominant molecular‑orbital transitions that give rise to them.
2. **NBO analysis** – a Natural Bond Orbital analysis extracts second‑order perturbation energies for electron donation from Fe to the Cp rings and back‑donation from the rings to Fe, as well as natural atomic charges.

The calculations are performed with the open‑source quantum chemistry package ORCA. No external datasets are required; the only input is the publicly available CIF file.

## Reproduction target
For the monoclinic type‑I ferrocene crystal structure (CCDC 2101933), produce the following results:

- From the TD‑DFT calculation, report the two most intense singlet excitation wavelengths (in nm), their oscillator strengths, and the major molecular‑orbital transitions contributing to each band. Write these as rows in `uvvis_peaks.csv`.
- From the NBO analysis, report the second‑order perturbation energies E(2) (in kcal/mol) for the dominant donor‑acceptor interactions between Fe and the Cp rings, specifically Fe(d) → Cp LP* donations and Cp → Fe back‑donations, in `nbo_e2.csv`.
- Also from the NBO analysis, report the natural atomic charges for Fe, C, H, and the total charge on each Cp ring in `nbo_charges.csv`.

## Assets

- Ferrocene type I crystal structure (CCDC 2101933): https://www.ccdc.cam.ac.uk/structures/
- ORCA quantum chemistry program: https://orcaforum.kofo.mpg.de/
- Open Babel: openbabel

## Workflow steps

### Step 1: Molecular geometry optimization
- Role: process
- Action: Obtain the ferrocene type-I crystal structure (CCDC 2101933) and convert it to a molecular input. Perform geometry optimization at the B3LYP level using a suitable basis set (e.g., def2-SVP or LANL2DZ for Fe and 6-311++G(d,p) for C/H). First optimize only hydrogen positions while fixing non-hydrogen atoms, then perform a full unconstrained optimization. The optimized geometry is used by all subsequent steps.
- Evidence: `/app/outputs/optimization.log`

### Step 2: TD-DFT UV/Vis excitation calculation
- Role: scored (load-bearing)
- Action: Run a TD-DFT calculation on the optimized geometry at the B3LYP level with the same basis set, requesting the lowest 20 singlet excited states. Parse the output to extract the two most intense transitions (by oscillator strength), their wavelengths, and the dominant molecular-orbital transition contributions. Write the results to uvvis_peaks.csv.
- Output file: `/app/outputs/uvvis_peaks.csv`
- Format: csv
- Contract: wavelength_nm,oscillator_strength,transition_label
- Scoring: scored by hidden verifier

### Step 3: NBO second-order perturbation energies
- Role: scored
- Action: Using the optimized geometry, run an NBO analysis at the B3LYP level. Extract the second-order perturbation energies E(2) for the key donor-acceptor interactions between Fe and Cp rings: Fe(d) → Cp LP* donations and Cp → Fe back-donations. Report donor label, acceptor label, and E(2) (kcal/mol) in nbo_e2.csv.
- Output file: `/app/outputs/nbo_e2.csv`
- Format: csv
- Contract: donor,acceptor,E2_kcal_mol
- Scoring: scored by hidden verifier

### Step 4: NBO natural atomic charges
- Role: scored
- Action: From the same NBO calculation, extract the natural atomic charges for Fe, carbon, hydrogen, and the total charge on each Cp ring. Report atom/moiety and charge in nbo_charges.csv.
- Output file: `/app/outputs/nbo_charges.csv`
- Format: csv
- Contract: atom_or_moiety,natural_charge
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/uvvis_peaks.csv`
- `/app/outputs/nbo_e2.csv`
- `/app/outputs/nbo_charges.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### uvvis_peaks.csv
- path: `/app/outputs/uvvis_peaks.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Two rows with the main absorption peak wavelengths, oscillator strengths, and assigned orbital transitions.
- schema:
  - `type`: table
  - `required_columns`: `wavelength_nm`, `oscillator_strength`, `transition_label`
  - `units`:
    - `wavelength_nm`: nm
    - `oscillator_strength`: dimensionless

### nbo_e2.csv
- path: `/app/outputs/nbo_e2.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Second-order perturbation energies E(2) for key Fe–Cp donor-acceptor interactions.
- schema:
  - `type`: table
  - `required_columns`: `donor`, `acceptor`, `E2_kcal_mol`
  - `units`:
    - `E2_kcal_mol`: kcal/mol

### nbo_charges.csv
- path: `/app/outputs/nbo_charges.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Natural atomic charges from NBO analysis.
- schema:
  - `type`: table
  - `required_columns`: `atom_or_moiety`, `natural_charge`
  - `units`:
    - `natural_charge`: e

Notes: The task reproduces the molecular DFT part only; solid-state Wien2k calculations (band structure, dielectric function, magnetic moments) are excluded per task scope.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "uvvis_peaks.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "wavelength_nm",
          "oscillator_strength",
          "transition_label"
        ],
        "units": {
          "wavelength_nm": "nm",
          "oscillator_strength": "dimensionless"
        }
      },
      "description": "Two rows with the main absorption peak wavelengths, oscillator strengths, and assigned orbital transitions."
    },
    {
      "file": "nbo_e2.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "donor",
          "acceptor",
          "E2_kcal_mol"
        ],
        "units": {
          "E2_kcal_mol": "kcal/mol"
        }
      },
      "description": "Second-order perturbation energies E(2) for key Fe–Cp donor-acceptor interactions."
    },
    {
      "file": "nbo_charges.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "atom_or_moiety",
          "natural_charge"
        ],
        "units": {
          "natural_charge": "e"
        }
      },
      "description": "Natural atomic charges from NBO analysis."
    }
  ],
  "notes": "The task reproduces the molecular DFT part only; solid-state Wien2k calculations (band structure, dielectric function, magnetic moments) are excluded per task scope."
}
```

## How you are scored
The hidden verifier examines each of your output files independently and compares them to reference expectations with appropriate tolerances (accounting for the variability of a re‑run with a different code version). It does **not** re‑run any DFT calculations.

- For `uvvis_peaks.csv`, it checks that you report two main peaks with wavelengths close to expected values and oscillator strengths that are consistent. It also verifies that the listed orbital transitions follow the expected character.
- For `nbo_e2.csv`, it checks that the strongest Fe(d) → Cp LP* interactions have energies above a high‑threshold order of magnitude, and that back‑donation entries are present.
- For `nbo_charges.csv`, it checks that the charges fall within plausible ranges.

The three scores are combined, with the UV/Vis peak assignment carrying the largest weight. Meeting or exceeding these checks earns a higher reward. Report only the computed results; the verifier will compare them to its own hidden references.

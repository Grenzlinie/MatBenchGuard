# DFT Atom-in-Jellium Cohesive Energy and EMT Parameters

## Problem background
The atom-in-jellium model treats a single atom embedded in a homogeneous electron gas (jellium) and is a fundamental tool for studying bonding properties of solids. Solving the Kohn-Sham equations for the free atom and for the atom immersed in the jellium at various embedding densities yields the immersion energy, from which cohesive properties can be derived. A key question is how different approximations for the exchange-correlation (XC) energy affect the predicted cohesive behavior. This work computes the cohesive energy and related parameters for the first 30 elements (H through Zn, excluding noble gases) using two widely used XC functionals: the local-density approximation (LDA) and the generalized-gradient approximation of Perdew-Wang (GGA-PW91). The derived quantities serve as input for the effective-medium theory (EMT), a glue-type scheme for interatomic interactions in large systems.

## Approach
The core method is first‑principles density‑functional theory (DFT). For each element, two types of Kohn‑Sham calculations are performed: (i) a free-atom calculation with spin polarization, and (ii) an embedding calculation where the atom is placed in a spin‑compensated homogeneous electron gas at a range of background densities n̄. The immersion energy ΔE^hom(n̄) is obtained as the energy difference between the embedded system and the free atom plus jellium reference. The electrostatic attraction between the atom and the electron gas is computed via the Hartree potential integrated over the neutral sphere, giving the term α(n̄)n̄. The cohesive function E_c(n̄) = ΔE^hom(n̄) − α(n̄)n̄ encapsulates the binding behaviour. The whole procedure is carried out twice, once with the LDA XC functional and once with GGA-PW91, to compare the two approximations. From the cohesive functions, the minimum cohesive energy E0, the corresponding neutral‑sphere radius s0, and the curvature parameter E2 are determined. A decay constant η is extracted from the exponential relation between n̄ and s0, and the bulk modulus B is computed from B = E2 η² / (6π s0). The result is a table of these parameters for all 30 elements under both functionals, enabling a direct comparison of LDA and GGA-PW91 predictions.

## Reproduction target
Produce a CSV file with the atom-in-jellium and EMT parameters for the 30 elements from hydrogen to zinc, excluding the noble gases (He, Ne, Ar, Kr). For each element, compute the following quantities under both the LDA and GGA-PW91 functionals: the minimum cohesive energy E0 (eV), the neutral‑sphere radius s0 (Bohr), the decay parameter η (dimensionless), the curvature parameter E2 (eV), and the bulk modulus B (GPa). The file must contain one row per element and the columns: element, E0_LDA, E0_GGA, s0_LDA, s0_GGA, eta_LDA, eta_GGA, E2_LDA, E2_GGA, B_LDA, B_GGA. The computed numbers should allow a comparison of the two functionals for each quantity.

## Assets

- GPAW (DFT code with jellium support): https://wiki.fysik.dtu.dk/gpaw/
- libxc (exchange-correlation functionals library): https://www.tddft.org/programs/libxc/
- Python scientific stack (numpy, scipy, pandas): numpy scipy pandas

## Workflow steps

### Step 1: DFT Atom-in-Jellium LDA Calculations
- Role: process
- Action: For each of the 30 elements from H to Zn (excluding noble gases), solve the Kohn-Sham equations self-consistently for the free atom (spin-polarized) and for the atom embedded in a homogeneous electron gas (spin-compensated) at a range of embedding densities using the LDA exchange-correlation functional. Compute the immersion energy ΔE^hom and the electrostatic attraction αn̄.
- Evidence: `/app/outputs/lda_raw.json`

### Step 2: DFT Atom-in-Jellium GGA-PW91 Calculations
- Role: process
- Action: Repeat the same calculations as step01 for all 30 elements using the GGA-PW91 exchange-correlation functional, producing the corresponding immersion energy ΔE^hom and αn̄.
- Evidence: `/app/outputs/gga_raw.json`

### Step 3: Extract EMT Parameters and Bulk Modulus
- Role: scored (load-bearing)
- Action: From the raw data of steps 1 and 2, construct the cohesive function E_c(n̄) = ΔE^hom(n̄) − α(n̄)n̄ for each element and each functional. Determine the minimum cohesive energy E0 and the corresponding optimum embedding density n0; compute the neutral sphere radius s0 (Wigner-Seitz sphere where total charge vanishes); fit E_c(n̄) near the minimum to obtain the curvature parameter E2; extract the decay constant η from the exponential relation between n̄ and neutral sphere radius (Eq. 6); compute the bulk modulus B = E2 η² / (6π s0). Output a CSV table with these values for all 30 elements.
- Output file: `/app/outputs/atom_in_jellium_parameters.csv`
- Format: csv
- Contract: CSV with columns: element (string), E0_LDA (eV), E0_GGA (eV), s0_LDA (Bohr), s0_GGA (Bohr), eta_LDA (dimensionless), eta_GGA (dimensionless), E2_LDA (eV), E2_GGA (eV), B_LDA (GPa), B_GGA (GPa). One row per element (H to Zn, excluding noble gases).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/atom_in_jellium_parameters.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### atom_in_jellium_parameters.csv
- path: `/app/outputs/atom_in_jellium_parameters.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Table of cohesive energy, neutral sphere radius, EMT parameters and bulk modulus for 30 elements (H to Zn, excluding noble gases) computed under LDA and GGA-PW91.
- schema:
  - `type`: table
  - `required_columns`: `element`, `E0_LDA`, `E0_GGA`, `s0_LDA`, `s0_GGA`, `eta_LDA`, `eta_GGA`, `E2_LDA`, `E2_GGA`, `B_LDA`, `B_GGA`
  - `units`:
    - `E0_LDA`: eV
    - `E0_GGA`: eV
    - `s0_LDA`: Bohr
    - `s0_GGA`: Bohr
    - `eta_LDA`: dimensionless
    - `eta_GGA`: dimensionless
    - `E2_LDA`: eV
    - `E2_GGA`: eV
    - `B_LDA`: GPa
    - `B_GGA`: GPa

Notes: The reference values are taken from Table I of the source paper. Monotonic trends (E0_GGA > E0_LDA and s0_GGA > s0_LDA) are checked as part of verification.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "atom_in_jellium_parameters.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "element",
          "E0_LDA",
          "E0_GGA",
          "s0_LDA",
          "s0_GGA",
          "eta_LDA",
          "eta_GGA",
          "E2_LDA",
          "E2_GGA",
          "B_LDA",
          "B_GGA"
        ],
        "units": {
          "E0_LDA": "eV",
          "E0_GGA": "eV",
          "s0_LDA": "Bohr",
          "s0_GGA": "Bohr",
          "eta_LDA": "dimensionless",
          "eta_GGA": "dimensionless",
          "E2_LDA": "eV",
          "E2_GGA": "eV",
          "B_LDA": "GPa",
          "B_GGA": "GPa"
        }
      },
      "description": "Table of cohesive energy, neutral sphere radius, EMT parameters and bulk modulus for 30 elements (H to Zn, excluding noble gases) computed under LDA and GGA-PW91."
    }
  ],
  "notes": "The reference values are taken from Table I of the source paper. Monotonic trends (E0_GGA > E0_LDA and s0_GGA > s0_LDA) are checked as part of verification."
}
```

## How you are scored
A hidden verifier scores each workflow artifact independently and combines them by weight into the final reward. The primary scored artifact is the parameter table (`atom_in_jellium_parameters.csv`). The verifier compares the reported numeric values against a hidden reference and also checks that the results satisfy pre‑defined monotonic trend relations between the LDA and GGA entries. Reporting the correct numbers is necessary, but the verifier additionally inspects the raw intermediate outputs (`lda_raw.json`, `gga_raw.json`) to confirm that the parameter extraction was performed correctly. The reward is weighted most heavily on the parameter table, with smaller contributions from the structural integrity of the raw data. Mere presence of a table is insufficient; the values must match the reference within accepted bounds and obey the required trends.

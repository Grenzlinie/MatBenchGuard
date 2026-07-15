# First-principles characterization of structural, electronic, vibrational, elastic, thermodynamic, and nonlinear optical properties of zinc-blende InAs_xSb_{1-x} ternary alloys using DFT/DFPT/GW

## Problem background
The III-V zinc-blende semiconductors InAs and InSb are important for infrared optoelectronics, and their ternary alloys InAsxSb1−x offer tunable properties across the composition range. This task systematically computes the structural, electronic, elastic, dielectric, vibrational, thermodynamic, and nonlinear optical properties of these alloys using first-principles methods. The target is a comprehensive set of physical quantities as a function of As concentration, including lattice constants, band gaps (both LDA and quasiparticle-corrected), phonon frequencies, mechanical moduli, and nonlinear optical coefficients. The results help assess the role of In 4d semicore states in the optical response and provide reference data for materials design.

## Approach
Use the ABINIT plane-wave pseudopotential density functional theory (DFT) code with the local density approximation (LDA). Model the ternary alloys via the virtual crystal approximation (VCA) by linearly combining As and Sb pseudopotentials. Perform structural relaxations to obtain equilibrium lattice constants. Compute Kohn-Sham band structures to extract the direct Γ-point gap, then correct the gap with one-shot G0W0 quasiparticle calculations. Calculate linear-response properties—static dielectric constant, Born effective charges, LO and TO phonon frequencies—using density functional perturbation theory (DFPT). Derive the high-frequency dielectric constant from the Lyddane-Sachs-Teller relation. Evaluate elastic constants via total-energy calculations on strained unit cells, and from them deduce mechanical properties (bulk modulus, shear modulus, Pugh ratio, Cauchy pressure). Obtain thermodynamic quantities (specific heat at constant volume and entropy at 300 K) from the phonon density of states under the harmonic approximation. Finally, compute nonlinear optical properties—second-order susceptibility d36, Raman susceptibilities α(ωT) and α(ωL), and the total clamped electro-optic coefficient r63s—using the 2n+1 theorem within DFPT. Perform all calculations for five compositions x = 0, 0.25, 0.5, 0.75, 1, and for two pseudopotential families: HGH (norm-conserving, valence only) and FHI (Troullier–Martins-type, including In 4d semicore states). The concrete execution sequence is given in the numbered steps below.

## Reproduction target
Assemble all computed properties into a single JSON file (`calculated_properties.json`). This file must contain the following quantities, each expressed as a function of the five alloy compositions and, where applicable, for both pseudopotential schemes (HGH.LDA and FHI.LDA):
- lattice constant (Å)
- LDA band gap (eV)
- GW band gap (eV)
- static dielectric constant ε(0) (dimensionless)
- high-frequency dielectric constant ε(∞) (dimensionless)
- Born effective charge (dimensionless)
- transverse optical phonon frequency ωTO (cm⁻¹)
- longitudinal optical phonon frequency ωLO (cm⁻¹)
- elastic constants C11, C12, C44 (10¹¹ dyne/cm²)
- isotropic bulk modulus B (GPa)
- isotropic shear modulus G (Voigt–Reuss–Hill average, GPa)
- Pugh ratio B/G (dimensionless)
- Cauchy pressure C12−C44 (10¹¹ dyne/cm²)
- constant-volume specific heat Cv at 300 K (J/mol·K)
- entropy S at 300 K (J/mol·K)
- second-order optical susceptibility d36 (pm/V)
- Raman susceptibility α(ωT) (10⁻³ a.u.)
- Raman susceptibility α(ωL) (10⁻³ a.u.)
- total clamped electro-optic coefficient r63s (pm/V).
The file must follow the structure described in the output contract: top-level keys for each property type, each containing sub-objects for HGH.LDA and FHI.LDA with arrays of length 5 corresponding to the compositions in the order x = 0, 0.25, 0.5, 0.75, 1. The target is to produce these values through your own computation.

## Assets

- ABINIT: https://www.abinit.org/
- Hartwigsen-Goedecker-Hutter (HGH) pseudopotentials for In, As, Sb: abinit
- Troullier-Martins-type (FHI) pseudopotentials for In, As, Sb: abinit

## Workflow steps

### Step 1: VCA pseudopotential construction
- Role: process
- Action: Construct virtual crystal approximation (VCA) ionic pseudopotentials for InAs_xSb_{1-x} at compositions x=0, 0.25, 0.5, 0.75, 1 by mixing As and Sb pseudopotentials (V_VCA = x V_As + (1-x) V_Sb) for both HGH and FHI pseudopotential families.
- Evidence: `/app/outputs/vca_mixing.log`

### Step 2: Geometry optimization and lattice constants
- Role: process
- Action: Perform DFT-LDA structural relaxations for each composition and pseudopotential scheme using ABINIT. Extract the equilibrium zinc-blende lattice parameter a(x) for all five compositions under HGH.LDA and FHI.LDA.
- Evidence: `/app/outputs/relaxation_convergence.log`

### Step 3: LDA electronic band gap calculation
- Role: process
- Action: Using the relaxed structures, compute the Kohn-Sham band structure and extract the direct LDA band gap at the Γ point for both pseudopotential families.
- Evidence: `/app/outputs/lda_band_gaps.txt`

### Step 4: GW quasiparticle band gap correction
- Role: process
- Action: Perform one-shot G0W0 on top of LDA wavefunctions and eigenvalues for both HGH.LDA and FHI.LDA schemes, obtaining corrected band gaps.
- Evidence: `/app/outputs/gw_band_gaps.txt`

### Step 5: DFPT for phonons, dielectric constant, and Born effective charges
- Role: process
- Action: Perform density functional perturbation theory (DFPT) on a suitable q-point mesh to obtain dynamical matrices, LO and TO phonon frequencies at Γ, static dielectric constant ε(0), and Born effective charge tensors using the HGH.LDA relaxed structures.
- Evidence: `/app/outputs/dfpt_phonon_dielectric.dat`

### Step 6: High-frequency dielectric constant derivation
- Role: process
- Action: From ε(0) and the optical phonon frequencies, compute the high-frequency dielectric constant ε(∞) using the Lyddane-Sachs-Teller relation: ε(∞) = ε(0) * (ω_TO^2 / ω_LO^2).
- Evidence: `/app/outputs/eps_infinity.txt`

### Step 7: Elastic constants via energy‑strain fitting
- Role: process
- Action: For each composition using HGH.LDA, perform DFT total-energy calculations at small finite strains and extract the three independent elastic constants C11, C12, C44.
- Evidence: `/app/outputs/elastic_fit.log`

### Step 8: Mechanical properties derivation
- Role: process
- Action: From C11, C12, C44 compute the isotropic bulk modulus B, shear modulus G (Voigt–Reuss–Hill average), B/G ratio, and Cauchy pressure C12−C44.
- Evidence: `/app/outputs/mechanical_props.txt`

### Step 9: Thermodynamic properties from phonon DOS
- Role: process
- Action: Using the phonon density of states from DFPT, evaluate the harmonic expressions for constant-volume specific heat Cv and entropy S at 300 K for all compositions.
- Evidence: `/app/outputs/thermo_300K.txt`

### Step 10: Nonlinear optical properties (2n+1 theorem)
- Role: process
- Action: Within DFPT beyond the sum‑over‑states approximation (2n+1 theorem) and for both HGH.LDA and FHI.LDA, compute the second‑order susceptibility d36, Raman susceptibilities α(ω_T) and α(ω_L) at Γ, and the total clamped electro‑optic coefficient r63^s.
- Evidence: `/app/outputs/nonlinear_output.log`

### Step 11: Compile final scored properties
- Role: scored (load-bearing)
- Action: Assemble all computed quantities (lattice constants, LDA band gaps, GW band gaps, static and high-frequency dielectric constants, Born effective charges, LO/TO phonon frequencies, elastic constants, bulk and shear moduli, Pugh ratio, Cauchy pressure, specific heat, entropy, d36, Raman susceptibilities, electro‑optic coefficients) into a single JSON file covering all compositions and both pseudopotential schemes.
- Output file: `/app/outputs/calculated_properties.json`
- Format: json
- Contract: See paper Tables 1‑6 for the structure of each block. Units: lattice constants in Å, band gaps in eV, dielectric constants dimensionless, Born charge dimensionless, phonon frequencies in cm⁻¹, elastic constants in 10¹¹ dyne/cm², bulk and shear modulus in GPa, specific heat in J/(mol·K), entropy in J/(mol·K), d36 in pm/V, Raman susceptibilities in 10⁻³ a.u., electro‑optic coefficient in pm/V. Compositions: x in [0, 0.25, 0.5, 0.75, 1].
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/calculated_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### calculated_properties.json
- path: `/app/outputs/calculated_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Compilation of all calculated physical properties of InAsxSb1-x alloys for the five compositions and two pseudopotential schemes.
- schema:
  - `type`: object
  - `required`: `lattice_constants`, `band_gaps`, `dielectric_constants`, `born_effective_charges`, `phonon_frequencies`, `elastic_constants`, `bulk_modulus`, `shear_modulus`, `pugh_ratio`, `cauchy_pressure`, `specific_heat`, `entropy`, `d36`, `raman_susceptibilities`, `electro_optic_coefficients`
  - `description`: JSON object containing all computed properties. Each top-level key maps to an object with keys 'HGH.LDA' (and 'FHI.LDA' where applicable). Each such object contains a list of values for x = [0, 0.25, 0.5, 0.75, 1] (exact order), matching the paper's Tables 1–6. For details on sub-structure see those tables. Units: Å, eV, dimensionless, cm⁻¹, 10¹¹ dyne/cm², GPa, J/(mol·K), pm/V, 10⁻³ a.u., pm/V.

Notes: The single output file is a structured compilation of results from the preceding computation steps. The hidden checker will compare each reported value against the paper's reference values with property-specific tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "calculated_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "lattice_constants",
          "band_gaps",
          "dielectric_constants",
          "born_effective_charges",
          "phonon_frequencies",
          "elastic_constants",
          "bulk_modulus",
          "shear_modulus",
          "pugh_ratio",
          "cauchy_pressure",
          "specific_heat",
          "entropy",
          "d36",
          "raman_susceptibilities",
          "electro_optic_coefficients"
        ],
        "description": "JSON object containing all computed properties. Each top-level key maps to an object with keys 'HGH.LDA' (and 'FHI.LDA' where applicable). Each such object contains a list of values for x = [0, 0.25, 0.5, 0.75, 1] (exact order), matching the paper's Tables 1–6. For details on sub-structure see those tables. Units: Å, eV, dimensionless, cm⁻¹, 10¹¹ dyne/cm², GPa, J/(mol·K), pm/V, 10⁻³ a.u., pm/V."
      },
      "description": "Compilation of all calculated physical properties of InAsxSb1-x alloys for the five compositions and two pseudopotential schemes."
    }
  ],
  "notes": "The single output file is a structured compilation of results from the preceding computation steps. The hidden checker will compare each reported value against the paper's reference values with property-specific tolerances."
}
```

## How you are scored
A hidden verifier reads your `calculated_properties.json` and independently compares each reported value to a hidden reference for every property, composition, and pseudopotential scheme. Tolerances are set per property type to account for the expected variation between independent implementations, while ensuring that a genuine, correct computational reproduction earns full credit. The verifier then computes a weighted average: each property–composition–scheme combination that falls within the appropriate tolerance contributes to the score. The final reward is a number between 0 and 1, reflecting how many of the computed quantities match the hidden reference. Submitting the published numbers without performing the actual calculations is not sufficient; only your own computed results are evaluated.

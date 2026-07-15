# DFT Structural Stability and Generalized Stacking Fault Energies of β Ti–Nb Alloys

## Problem background
Beta-phase Ti-Nb alloys are candidate biomaterials due to their low stiffness and good biocompatibility. Their mechanical response, notably the deformation behavior and strength, is governed by the stability of the body-centered cubic (bcc) beta phase and the mobility of screw dislocations. The work investigates how the structural energy difference between the bcc and hexagonal close-packed (hcp) phases, the tetragonal shear modulus C', and the generalized stacking fault energies (GSFE) along the {110}<111> and {112}<111> slip systems vary with the Nb content (quantified by the valence electron number e/a). These quantities determine the tendency of 1/2<111> screw dislocations to split into partials and thus control the ease of dislocation glide. The task is to compute these properties from density functional theory for pure Nb and three Ti-Nb alloys with e/a=4.75, 4.5, and 4.25, and to evaluate the energy change ΔW associated with circular splitting of a screw dislocation into twelve partials following the Bobylev model.

## Approach
Use an open-source plane-wave DFT code with projector augmented wave pseudopotentials and the generalized gradient approximation for exchange-correlation. For each of the four compositions (pure Nb, Ti-75Nb, Ti-50Nb, Ti-25Nb), construct supercells for the bcc and hcp phases and perform total-energy calculations as functions of volume (and c/a for hcp). From these, determine the equilibrium energies and the bcc-hcp energy difference. Apply volume-conserving tetragonal and monoclinic strains to the equilibrium bcc supercells to derive the elastic constants C11 and C12, and compute the tetragonal shear modulus C' = (C11-C12)/2. For the GSFE, build periodic slabs with 12 atomic layers oriented with slip planes {110} and {112} and the <111> direction; shift the upper half relative to the lower half along <111>, fully relax atomic positions perpendicular to the slip plane, and record the total energy as a function of displacement. From the GSFE curves extract the unstable stacking fault energy γ_us for each slip system, and for the {110} system the energies at displacements b/6 and b/3 (where b = a/2<111>). Compute the ratio γ(b/3) / (2 * γ(b/6)). Obtain the shear modulus G and the equilibrium lattice constant a from the bcc calculations. Finally, use the Bobylev model for N=12 partial splitting, which combines an elastic self-energy term with the GSFE contribution, to define the energy change ΔW as a function of the splitting radius r. Numerically minimize ΔW(r) for each composition and record the minimum value as the dislocation core splitting energy. All derived quantities must be aggregated into a single JSON file results.json.

## Reproduction target
Compute for the four systems (pure Nb, Ti-75Nb, Ti-50Nb, Ti-25Nb) the following quantities and store them in /app/outputs/results.json: bcc-hcp energy difference ΔE (eV/atom) at the respective equilibrium volumes; tetragonal shear modulus C' (GPa); unstable stacking fault energies γ_us for {112}<111> and {110}<111> (J/m²); the GSFE values γ(b/3) and γ(b/6) for {110}<111> (J/m²) and their ratio γ(b/3)/(2·γ(b/6)); shear modulus G (GPa) and lattice constant a (nm) from the equilibrium bcc structure; and the minimum energy change ΔW_min (eV/nm) for 12-partial splitting obtained by minimizing the Bobylev expression with respect to the splitting radius r.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PAW pseudopotentials for Ti and Nb (SSSP efficiency set): https://www.materialscloud.org/discover/sssp/table/efficiency
- Python numpy, scipy: install via pip

## Workflow steps

### Step 1: Alloy supercell construction
- Role: process
- Action: Construct bcc, hcp, and slab supercells for pure Nb and Ti-Nb alloys with compositions corresponding to e/a=4.25, 4.5, 4.75, and 5.0 using elemental crystal structures. For hcp allow variable c/a ratio. For GSFE, build 12-layer periodic supercells with {110} and {112} slip plane orientations and the <111> direction.
- Evidence: none

### Step 2: DFT total-energy calculations for bcc and hcp phases
- Role: process
- Action: Using an open-source DFT code with PAW pseudopotentials and GGA exchange-correlation, compute total energies for bcc and hcp structures as functions of cell volume (and c/a for hcp) for each composition. Retain the energy-volume data.
- Evidence: none

### Step 3: DFT elastic-constant calculations for bcc phases
- Role: process
- Action: For each composition, apply volume-conserving tetragonal and monoclinic strains to the equilibrium bcc supercell and record the energy changes. Derive C11 and C12, then compute the tetragonal shear modulus C' = (C11-C12)/2.
- Evidence: none

### Step 4: DFT GSFE calculations for {110}<111> and {112}<111> slip systems
- Role: process
- Action: For each composition, perform DFT calculations on the slab supercells for {110}<111> and {112}<111> slip systems. Shift the upper half relative to the lower half along <111> and relax atoms perpendicular to the slip plane. Generate GSFE curves (energy vs displacement) and extract the unstable stacking fault energy γ_us, and the energies at displacements b/6 and b/3 (b = a/2<111>) for the {110} system.
- Evidence: none

### Step 5: Compile final structural stability, GSFE, and dislocation core energies
- Role: scored (load-bearing)
- Action: From the outputs of the previous steps, compute for each composition the following quantities and write them to results.json: (1) bcc-hcp energy difference (eV/atom) at equilibrium volumes; (2) tetragonal shear modulus C' (GPa); (3) unstable stacking fault energies γ_us for {112}<111> and {110}<111> (J/m^2); (4) for the {110}<111> system, the energies γ(b/3) and γ(b/6) (J/m^2) and the ratio γ(b/3) / (2 * γ(b/6)); (5) shear modulus G (GPa) and lattice constant a (nm) from the equilibrium bcc structure; (6) the minimum energy change ΔW_min (eV/nm) for 12-partial splitting, computed using the Bobylev model that combines elastic energy with the GSFE values, numerically minimized with respect to the splitting radius r.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with keys "pure_Nb", "Ti75Nb", "Ti50Nb", "Ti25Nb". Each value is an object containing the numeric fields: bcc_hcp_energy_difference (eV/atom), C_prime (GPa), gamma_us_112 (J/m^2), gamma_us_110 (J/m^2), gamma_b3 (J/m^2), gamma_b6 (J/m^2), ratio_gamma_b3_to_2gamma_b6 (dimensionless), G (GPa), lattice_constant_a (nm), Delta_W_min (eV/nm).
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
- target_policy: reference_match
- description: A single JSON file containing the computed structural energy difference, tetragonal shear modulus, unstable stacking fault energies, GSFE ratios, shear modulus, lattice constant, and minimum dislocation splitting energy for each alloy composition.
- schema:
  - `type`: object
  - `required`:
    - `pure_Nb`: object with required numeric fields as described
    - `Ti75Nb`: object with required numeric fields as described
    - `Ti50Nb`: object with required numeric fields as described
    - `Ti25Nb`: object with required numeric fields as described
  - `items`: object
  - `required_columns`:
  - `units`:
    - `bcc_hcp_energy_difference`: eV/atom
    - `C_prime`: GPa
    - `gamma_us_112`: J/m^2
    - `gamma_us_110`: J/m^2
    - `gamma_b3`: J/m^2
    - `gamma_b6`: J/m^2
    - `ratio_gamma_b3_to_2gamma_b6`: dimensionless
    - `G`: GPa
    - `lattice_constant_a`: nm
    - `Delta_W_min`: eV/nm

Notes: The checker will compare the submitted numeric values to paper-reported reference values with tolerances and verify that bcc-hcp energy difference and C' decrease monotonically with decreasing e/a, approach zero at e/a=4.25, the ratio γ(b/3)/2γ(b/6) increases monotonically, and ΔW_min is negative only for Ti-25Nb.

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
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "pure_Nb": "object with required numeric fields as described",
          "Ti75Nb": "object with required numeric fields as described",
          "Ti50Nb": "object with required numeric fields as described",
          "Ti25Nb": "object with required numeric fields as described"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "bcc_hcp_energy_difference": "eV/atom",
          "C_prime": "GPa",
          "gamma_us_112": "J/m^2",
          "gamma_us_110": "J/m^2",
          "gamma_b3": "J/m^2",
          "gamma_b6": "J/m^2",
          "ratio_gamma_b3_to_2gamma_b6": "dimensionless",
          "G": "GPa",
          "lattice_constant_a": "nm",
          "Delta_W_min": "eV/nm"
        }
      },
      "description": "A single JSON file containing the computed structural energy difference, tetragonal shear modulus, unstable stacking fault energies, GSFE ratios, shear modulus, lattice constant, and minimum dislocation splitting energy for each alloy composition."
    }
  ],
  "notes": "The checker will compare the submitted numeric values to paper-reported reference values with tolerances and verify that bcc-hcp energy difference and C' decrease monotonically with decreasing e/a, approach zero at e/a=4.25, the ratio γ(b/3)/2γ(b/6) increases monotonically, and ΔW_min is negative only for Ti-25Nb."
}
```

## How you are scored
The hidden verifier reads your results.json and scores it by comparing your reported values to reference values (the paper's published numbers) with tolerances that allow for legitimate differences due to implementation choices, pseudopotentials, and convergence settings. In addition, the checker verifies that certain expected physical trends among the compositions are present (e.g., the evolution of properties with the valence electron number e/a and the sign of the dislocation splitting energy for the different alloys). Each quantity and each trend contributes a partial score, and the final reward is a weighted sum in the range [0,1]. Simply reporting the paper's values is not sufficient; your workflow must genuinely compute these quantities from first principles, and the intermediate computational steps must be executed (the verifier will check the presence and structure of the output file).

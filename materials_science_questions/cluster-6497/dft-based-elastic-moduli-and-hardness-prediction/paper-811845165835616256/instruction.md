# DFT elastic constants and moduli of WC0.75N0.25

## Problem background
Tungsten carbonitride WC0.75N0.25 thin films can crystallise in either a cubic (Fm-3m) or hexagonal (P-6m2) phase, and their observed hardness depends on which phase is present. To investigate this dependence, first-principles DFT calculations of the single-crystal elastic constants and the derived isotropic bulk and shear moduli were performed for both phases. The central question is whether the hexagonal phase possesses a substantially higher shear modulus than the cubic phase while the bulk moduli remain comparable, which would explain differences in intrinsic hardness.

## Approach
The reproduction follows a three-stage compute workflow. First, the two 8-atom supercells are built — one for the cubic phase and one for the hexagonal phase — using the published lattice parameters and stoichiometry (WC0.75N0.25, achieved by replacing one carbon atom with nitrogen). Each structure is then fully relaxed with plane-wave DFT at the GGA-PW91 level using ultrasoft pseudopotentials. After optimisation, small finite strains are applied to the relaxed cells and the resulting stress tensors are computed, from which the single-crystal elastic stiffness constants c_ij are extracted. Finally, the Voigt-averaged isotropic bulk modulus B and shear modulus G are derived from the c_ij using the standard formulas for each crystal symmetry. The output is a JSON summary of all stiffness constants and derived moduli for both phases.

## Reproduction target
Compute the single-crystal elastic stiffness constants c_ij and the Voigt-averaged isotropic bulk modulus B and shear modulus G for both the cubic (Fm-3m) and hexagonal (P-6m2) phases of WC0.75N0.25. Write the results to a JSON file following the exact schema specified in the output contract. The hidden checker will compare the reported constants and moduli to independent reference values and will evaluate the physical consistency of the relationship between the two phases (e.g., whether the hexagonal shear modulus is convincingly larger than the cubic one while the bulk moduli are similar).

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotential library: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Crystal structure generation
- Role: process
- Action: Construct the two 8-atom supercells for cubic (Fm-3m) and hexagonal (P-6m2) WC0.75N0.25. Use the starting lattice parameters a=0.4240 nm for the cubic phase, and a=0.2901 nm, c=0.2836 nm for the hexagonal phase. In each cell replace one of the four carbon atoms by nitrogen to achieve WC0.75N0.25 stoichiometry. Write input structure files suitable for DFT relaxation.
- Evidence: `/app/outputs/initial_structures.txt`

### Step 2: DFT geometry optimisation
- Role: process
- Action: Perform full geometry optimisation (lattice parameters and internal coordinates) for each phase using plane-wave DFT with the GGA-PW91 functional and ultrasoft pseudopotentials, a plane-wave cutoff of at least 450 eV, and a sufficiently dense k-point mesh to converge stresses. Run the optimisation independently for the cubic and hexagonal cells.
- Evidence: `/app/outputs/relaxation.log`

### Step 3: Elastic constants and moduli
- Role: scored (load-bearing)
- Action: Using the relaxed structures, apply a set of small finite strains and compute the resulting stress tensor via DFT to extract the single-crystal elastic stiffness constants (c_ij). Then compute the Voigt-averaged isotropic bulk modulus B and shear modulus G using the appropriate formulas for each crystal system. Save all constants and moduli to a JSON file.
- Output file: `/app/outputs/elastic_constants.json`
- Format: json
- Contract: {"cubic": {"c11": float, "c12": float, "c44": float, "B": float, "G": float}, "hexagonal": {"c11": float, "c12": float, "c13": float, "c33": float, "c44": float, "c66": float, "B": float, "G": float}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/elastic_constants.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### elastic_constants.json
- path: `/app/outputs/elastic_constants.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed elastic stiffness constants and derived bulk (B) and shear (G) moduli (in GPa) for cubic and hexagonal WC0.75N0.25.
- schema:
  - `type`: object
  - `required`:
    - `cubic`:
      - `type`: object
      - `required_keys`: `c11`, `c12`, `c44`, `B`, `G`
      - `unit`: GPa
    - `hexagonal`:
      - `type`: object
      - `required_keys`: `c11`, `c12`, `c13`, `c33`, `c44`, `c66`, `B`, `G`
      - `unit`: GPa

Notes: The hidden checker performs a numerical comparison of each reported value against the paper's DFT results with a ±30% tolerance, and enforces structural relations: G(hex)/G(cubic) >= 1.5 and relative difference of bulk moduli <= 20%.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "elastic_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "cubic": {
            "type": "object",
            "required_keys": [
              "c11",
              "c12",
              "c44",
              "B",
              "G"
            ],
            "unit": "GPa"
          },
          "hexagonal": {
            "type": "object",
            "required_keys": [
              "c11",
              "c12",
              "c13",
              "c33",
              "c44",
              "c66",
              "B",
              "G"
            ],
            "unit": "GPa"
          }
        }
      },
      "description": "Computed elastic stiffness constants and derived bulk (B) and shear (G) moduli (in GPa) for cubic and hexagonal WC0.75N0.25."
    }
  ],
  "notes": "The hidden checker performs a numerical comparison of each reported value against the paper's DFT results with a ±30% tolerance, and enforces structural relations: G(hex)/G(cubic) >= 1.5 and relative difference of bulk moduli <= 20%."
}
```

## How you are scored
A hidden verifier inspects every required output file. It checks that files are well-formed and that the reported numerical values are physically plausible for the intended DFT workflow. For the load-bearing elastic constants, the verifier tests consistency with the expected results for the GGA-PW91 functional and ultrasoft pseudopotentials, and enforces structural relations (relative magnitudes of shear moduli and bulk moduli between the two phases) that a correct independent computation must satisfy. The verifier combines these checks into a final score between 0 and 1. Simply copying published values or fabricating numbers is not sufficient — the verifier is designed to reward genuine computations that respect the physical trends of the material.

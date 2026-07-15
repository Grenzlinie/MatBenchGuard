# Elastic Moduli and Debye Temperature of Defective Gd2Zr2O7 from DFT+U

## Problem background
Gadolinium zirconate pyrochlore (Gd2Zr2O7) is a candidate host matrix for nuclear waste immobilization due to its radiation resistance. Under self-irradiation, point defects such as vacancies, antisites, and interstitials can form and may significantly alter the material’s mechanical and thermal properties. This task investigates how individual defect types affect the elastic moduli, ductility, and lattice‑dynamical properties of Gd2Zr2O7 using density functional theory.

## Approach
The approach uses first-principles density functional theory with a Hubbard U correction (DFT+U) to obtain the total energies and relaxed structures of a pristine 2×2×2 supercell of Gd2Zr2O7 and of five distinct point-defect configurations—a single O vacancy (V_O48f), a Zr‑on‑Gd antisite (Zr_Gd), and three interstitials (Gd_int2, Zr_8a, O_8a)—that represent the most stable defects of their respective types. From each relaxed configuration the three independent cubic elastic constants (C11, C12, C44) are computed via a stress-strain or finite‑differences method. The Voigt–Reuss–Hill approximation is then applied to derive the bulk modulus, shear modulus, and Young’s modulus, and from the elastic moduli and density the Debye temperature is calculated. Additionally, defect formation energies are computed using the total energies of the defective and pristine supercells together with reference energies for the elemental phases.

## Reproduction target
Produce a single JSON file, results.json, containing for the pristine Gd2Zr2O7 supercell and for each of the five defect configurations (V_O48f, Zr_Gd, Gd_int2, Zr_8a, O_8a) the elastic constants C11, C12, C44 (in GPa), the Voigt–Reuss–Hill bulk modulus B_VRH, shear modulus G_VRH, and Young’s modulus E (in GPa), and the Debye temperature (in K). For the five defective entries, also include the defect formation energy (in eV). All values must be numeric and provided in the specified units and JSON schema.

## Assets

- Quantum ESPRESSO (or equivalent open-source DFT code with DFT+U and elastic constant capabilities): https://www.quantum-espresso.org
- Pseudopotentials for Gd, Zr, O (GGA-PBE): https://www.materialscloud.org/discover/sssp/table/efficiency
- Crystallographic data for Gd2Zr2O7 pyrochlore

## Workflow steps

### Step 1: Build supercells
- Role: process
- Action: Construct atomic structures for pristine Gd2Zr2O7 (2×2×2 supercell, 88 atoms) and five defective supercells: V_O48f (remove one O at 48f site), Zr_Gd (swap one Zr and Gd), Gd_int2 (insert Gd at int2 site (0.5,0.625,0.625)), Zr_8a (insert Zr at 8a site (0.375,0.375,0.875)), O_8a (insert O at 8a site). Use the known crystallographic data: space group Fd-3m, lattice constant a0=10.666 Å, and O48f positional parameter x=0.339.
- Evidence: `/app/outputs/supercells.json`

### Step 2: DFT+U relaxation and total energies
- Role: process
- Action: Perform DFT+U geometry optimizations for pristine and all defective supercells using an open-source DFT code with GGA-PBE functional and Hubbard U correction on Gd 4f orbitals. Relax atomic positions until forces are converged. Record relaxed lattice parameters and total energies.
- Evidence: `/app/outputs/relax_data.json`

### Step 3: Reference energies for elements
- Role: process
- Action: Compute DFT+U total energies of bulk Gd (hcp), Zr (hcp), and O (O2 molecule or solid α-O2) using the same functional and settings. Extract per-atom reference energies for Gd, Zr, and O.
- Evidence: `/app/outputs/ref_energies.json`

### Step 4: Defect formation energies
- Role: process
- Action: Calculate defect formation energies for V_O48f, Zr_Gd, Gd_int2, Zr_8a, and O_8a using the total energies from step_1 and reference energies from step_2. Use the standard formulas for vacancy, antisite, and interstitial defects.
- Evidence: `/app/outputs/formation_energies.json`

### Step 5: Elastic constants calculation
- Role: process
- Action: For pristine and each of the five defective configurations (using the relaxed structures from step_1), compute the three independent cubic elastic constants C11, C12, C44 using the stress-strain or finite-differences method available in the DFT code. Ensure the cubic mechanical stability criteria are satisfied.
- Evidence: `/app/outputs/elastic_constants.json`

### Step 6: Elastic moduli and Debye temperature (scored)
- Role: scored (load-bearing)
- Action: From the elastic constants obtained in step_4, calculate Voigt-Reuss-Hill bulk modulus B_VRH, shear modulus G_VRH, and Young's modulus E using the standard formulas for cubic symmetry. Compute density from the relaxed lattice constant and formula mass. Compute the average sound velocities (transverse and longitudinal) and the Debye temperature. Also compute Pugh's ratio B_over_G = B_VRH / G_VRH and Poisson's ratio using the standard formula for isotropic polycrystals. Combine with defect formation energies from step_3. Write all numeric results for pristine and the five defective configurations into results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: A JSON object with keys: 'pristine', 'V_O48f', 'Zr_Gd', 'Gd_int2', 'Zr_8a', 'O_8a'. Each value is an object containing: 'C11', 'C12', 'C44' (GPa, numbers), 'B_VRH', 'G_VRH', 'E' (GPa, numbers), 'B_over_G' (dimensionless number), 'Poisson_ratio' (dimensionless number), 'Debye_temperature' (K, number). For defective entries also include 'formation_energy' (eV, number). All fields must be present and of numeric type.
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
- description: Computed elastic constants, VRH moduli, Pugh's ratio, Poisson's ratio, Debye temperature, and defect formation energies for pristine and five defective configurations. The checker will recompute B_VRH, G_VRH, E from C11, C12, C44, compute B_over_G and Poisson_ratio from the moduli to verify internal consistency, and compare all quantities to paper-reported references.
- schema:
  - `type`: object
  - `required`:
    - `pristine`:
      - `C11`: number (GPa)
      - `C12`: number (GPa)
      - `C44`: number (GPa)
      - `B_VRH`: number (GPa)
      - `G_VRH`: number (GPa)
      - `E`: number (GPa)
      - `B_over_G`: number (dimensionless)
      - `Poisson_ratio`: number (dimensionless)
      - `Debye_temperature`: number (K)
  - `defective_keys`: `V_O48f`, `Zr_Gd`, `Gd_int2`, `Zr_8a`, `O_8a`
  - `defective_entry_fields`:
    - `C11`: number (GPa)
    - `C12`: number (GPa)
    - `C44`: number (GPa)
    - `B_VRH`: number (GPa)
    - `G_VRH`: number (GPa)
    - `E`: number (GPa)
    - `B_over_G`: number (dimensionless)
    - `Poisson_ratio`: number (dimensionless)
    - `Debye_temperature`: number (K)
    - `formation_energy`: number (eV)
  - `units`:
    - `C11`: GPa
    - `C12`: GPa
    - `C44`: GPa
    - `B_VRH`: GPa
    - `G_VRH`: GPa
    - `E`: GPa
    - `B_over_G`: dimensionless
    - `Poisson_ratio`: dimensionless
    - `Debye_temperature`: K
    - `formation_energy`: eV

Notes: The agent must execute all process steps (0–4) to obtain the data needed for step_5. The checker recomputes the VRH moduli and ductility metrics to verify internal consistency and compares the results against the paper's reported values.

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
          "pristine": {
            "C11": "number (GPa)",
            "C12": "number (GPa)",
            "C44": "number (GPa)",
            "B_VRH": "number (GPa)",
            "G_VRH": "number (GPa)",
            "E": "number (GPa)",
            "B_over_G": "number (dimensionless)",
            "Poisson_ratio": "number (dimensionless)",
            "Debye_temperature": "number (K)"
          }
        },
        "defective_keys": [
          "V_O48f",
          "Zr_Gd",
          "Gd_int2",
          "Zr_8a",
          "O_8a"
        ],
        "defective_entry_fields": {
          "C11": "number (GPa)",
          "C12": "number (GPa)",
          "C44": "number (GPa)",
          "B_VRH": "number (GPa)",
          "G_VRH": "number (GPa)",
          "E": "number (GPa)",
          "B_over_G": "number (dimensionless)",
          "Poisson_ratio": "number (dimensionless)",
          "Debye_temperature": "number (K)",
          "formation_energy": "number (eV)"
        },
        "units": {
          "C11": "GPa",
          "C12": "GPa",
          "C44": "GPa",
          "B_VRH": "GPa",
          "G_VRH": "GPa",
          "E": "GPa",
          "B_over_G": "dimensionless",
          "Poisson_ratio": "dimensionless",
          "Debye_temperature": "K",
          "formation_energy": "eV"
        }
      },
      "description": "Computed elastic constants, VRH moduli, Pugh's ratio, Poisson's ratio, Debye temperature, and defect formation energies for pristine and five defective configurations. The checker will recompute B_VRH, G_VRH, E from C11, C12, C44, compute B_over_G and Poisson_ratio from the moduli to verify internal consistency, and compare all quantities to paper-reported references."
    }
  ],
  "notes": "The agent must execute all process steps (0–4) to obtain the data needed for step_5. The checker recomputes the VRH moduli and ductility metrics to verify internal consistency and compares the results against the paper's reported values."
}
```

## How you are scored
A hidden verifier will check the submitted results.json by recomputing the VRH moduli from the reported elastic constants to verify internal consistency, and by comparing each computed quantity (elastic constants, moduli, Debye temperature, and formation energies) to independently established reference values within appropriate tolerances. Each workflow stage contributes a weighted portion to the final score; merely reporting literature values without performing the DFT computation will not produce the required internal consistency and will not pass.

# DFT Simulation of a Rectangular-Lattice Metallic Porous Carbon Monolayer

## Problem background
Two-dimensional carbon allotropes attract considerable interest for their unique electronic, mechanical, and optical properties. Propylenidene (PPD) is a newly proposed porous 2D carbon monolayer formed from bicyclopropylidene units, featuring a rectangular lattice with 3-, 8-, and 10-membered rings. Density functional theory (DFT) can be used to characterize its structural stability, metallic nature, mechanical anisotropy, and optical absorption, providing insight into its potential for energy storage and optoelectronics.

## Approach
The target material properties (structural, cohesive energy, phonon stability, electronic band gap, elastic constants, mechanical moduli, and optical absorption) are obtained from DFT simulations. The workflow begins with structural relaxation of the PPD unit cell using the PBE exchange-correlation functional and a DFT-D4 dispersion correction. From the relaxed geometry, compute the cohesive energy per atom, the phonon dispersion to check dynamical stability, the electronic band structure to determine the band gap, the elastic constants using the finite-strain method, and the derived mechanical moduli (Young's modulus, shear modulus, Poisson's ratio) for directional analysis. Finally, calculate the frequency-dependent dielectric function and absorption coefficients for xx and yy polarizations. All calculations are performed with a plane-wave basis and appropriate k-point sampling.

## Reproduction target
Perform a series of DFT calculations to compute the following properties of the PPD monolayer: relaxed lattice parameters, cohesive energy, phonon stability (absence of imaginary frequencies), electronic band gap, elastic constants (C11, C22, C12, C66), directional Young's modulus, shear modulus, and Poisson's ratio (minimum and maximum values), and optical absorption coefficients at 0.8 eV (xx polarization) and 2.3 eV (yy polarization). Compile all results into a single JSON file `/app/outputs/ppd_properties.json` according to the schema defined in the output contract.

## Assets

- Quantum ESPRESSO (or any open-source DFT package capable of PAW/PBE and phonon/optical calculations): https://www.quantum-espresso.org
- Phonopy: https://phonopy.github.io/phonopy/
- PBE pseudopotentials (e.g., SSSP efficiency library or GBRV): https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: Build initial PPD unit cell
- Role: process
- Action: Create the input structure file (e.g., POSCAR/CIF) for the rectangular unit cell from the given lattice parameters (a=6.70 Å, b=3.80 Å) and atomic fractional coordinates (C1 0.89746 0.0 0.0; C2 0.28464 0.81572 0.0; C3 0.60855 0.5 0.0).
- Evidence: `/app/outputs/ppd_initial.cif`

### Step 2: DFT structural relaxation
- Role: process
- Action: Relax the atomic positions and cell parameters using DFT with PBE functional and DFT-D4 dispersion correction. Extract the final total energy and relaxed lattice vectors.
- Evidence: `/app/outputs/relaxed_total_energy.txt`

### Step 3: Cohesive energy calculation
- Role: process
- Action: Use the relaxed total energy and the total energy of an isolated carbon atom (computed with the same DFT settings) to calculate the cohesive energy per atom: (E_tot - n_C * E_atom) / n_C.
- Evidence: `/app/outputs/cohesive_energy.txt`

### Step 4: Phonon stability check
- Role: process
- Action: Calculate phonon frequencies using density functional perturbation theory (DFPT) with Phonopy (or the DFT code's built-in tools). Check for the presence of any imaginary (negative) frequencies.
- Evidence: `/app/outputs/phonon_frequencies.dat`

### Step 5: Electronic band gap
- Role: process
- Action: Compute the electronic band structure and extract the band gap at the PBE level. Use the same converged charge density from the relaxation.
- Evidence: `/app/outputs/band_gap.txt`

### Step 6: Elastic constants
- Role: process
- Action: Apply small finite strains to the relaxed cell and compute the resulting stress tensor. Fit the stress-strain relation to obtain the 2D elastic stiffness constants C11, C22, C12, C66 (in N/m).
- Evidence: `/app/outputs/elastic_constants.txt`

### Step 7: Mechanical moduli
- Role: process
- Action: From the elastic constants, derive the angular-dependent Young's modulus, shear modulus, and Poisson's ratio. Extract the minimum and maximum values for each.
- Evidence: `/app/outputs/moduli.txt`

### Step 8: Optical absorption
- Role: process
- Action: Calculate the frequency-dependent dielectric function and derive the absorption coefficient for light polarized along x and y directions. Report the values at 0.8 eV (xx) and 2.3 eV (yy).
- Evidence: `/app/outputs/optical_absorption.txt`

### Step 9: Compile final properties
- Role: scored (load-bearing)
- Action: Collect all previously computed quantities into a single JSON file named ppd_properties.json.
- Output file: `/app/outputs/ppd_properties.json`
- Format: json
- Contract: {"relaxed_a":"float","relaxed_b":"float","cohesive_energy":"float","electronic_band_gap":"float","C11":"float","C22":"float","C12":"float","C66":"float","Young_modulus_min":"float","Young_modulus_max":"float","shear_modulus_min":"float","shear_modulus_max":"float","Poisson_ratio_min":"float","Poisson_ratio_max":"float","phonon_imaginary_frequencies":"bool","absorption_xx_at_0_8eV":"float","absorption_yy_at_2_3eV":"float"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/ppd_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### ppd_properties.json
- path: `/app/outputs/ppd_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Aggregated structural, electronic, mechanical, and optical properties of the 2D monolayer. The checker compares each numeric field against the paper’s reported values with tolerances appropriate for DFT code differences.
- schema:
  - `type`: object
  - `required`:
    - `relaxed_a`: float (Å)
    - `relaxed_b`: float (Å)
    - `cohesive_energy`: float (eV/atom)
    - `electronic_band_gap`: float (eV)
    - `C11`: float (N/m)
    - `C22`: float (N/m)
    - `C12`: float (N/m)
    - `C66`: float (N/m)
    - `Young_modulus_min`: float (N/m)
    - `Young_modulus_max`: float (N/m)
    - `shear_modulus_min`: float (N/m)
    - `shear_modulus_max`: float (N/m)
    - `Poisson_ratio_min`: float
    - `Poisson_ratio_max`: float
    - `phonon_imaginary_frequencies`: bool
    - `absorption_xx_at_0_8eV`: float (fraction)
    - `absorption_yy_at_2_3eV`: float (fraction)

Notes: The agent must perform all DFT simulations and compile the results. The checker uses a hidden reference (the paper’s values) to score the submitted properties per-field.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "ppd_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "relaxed_a": "float (Å)",
          "relaxed_b": "float (Å)",
          "cohesive_energy": "float (eV/atom)",
          "electronic_band_gap": "float (eV)",
          "C11": "float (N/m)",
          "C22": "float (N/m)",
          "C12": "float (N/m)",
          "C66": "float (N/m)",
          "Young_modulus_min": "float (N/m)",
          "Young_modulus_max": "float (N/m)",
          "shear_modulus_min": "float (N/m)",
          "shear_modulus_max": "float (N/m)",
          "Poisson_ratio_min": "float",
          "Poisson_ratio_max": "float",
          "phonon_imaginary_frequencies": "bool",
          "absorption_xx_at_0_8eV": "float (fraction)",
          "absorption_yy_at_2_3eV": "float (fraction)"
        }
      },
      "description": "Aggregated structural, electronic, mechanical, and optical properties of the 2D monolayer. The checker compares each numeric field against the paper’s reported values with tolerances appropriate for DFT code differences."
    }
  ],
  "notes": "The agent must perform all DFT simulations and compile the results. The checker uses a hidden reference (the paper’s values) to score the submitted properties per-field."
}
```

## How you are scored
A hidden verifier independently assesses each workflow step's output and aggregates a weighted score to produce the final reward. The primary check compares the computed values in `ppd_properties.json` against independent references (accounting for typical variability among DFT implementations). Intermediate evidence files are also checked for existence and consistency. Simply reporting the paper's reported numbers is insufficient; you must execute the computational workflow to produce artifacts that pass the checks. The final reward is a number between 0 and 1, with higher weight assigned to the main mechanical and electronic claims.

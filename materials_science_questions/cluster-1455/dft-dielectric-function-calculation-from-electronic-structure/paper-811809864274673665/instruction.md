# DFT calculation of mechanical and optical properties of delafossite CuAlO2

## Problem background
Delafossite CuAlO2 is a p-type transparent conducting oxide (TCO) with potential applications in transparent electrodes, solar cells, and UV optoelectronics. A complete picture of its mechanical, electronic, and optical properties is essential for device design, but many of these properties have not been computed from first principles. This task re‑creates a comprehensive density‑functional‑theory (DFT) study of CuAlO2 to predict the equilibrium crystal structure, bulk modulus, the full set of elastic constants, derived mechanical moduli (bulk, shear, Young’s), Poisson ratio, elastic anisotropy, sound velocities, Debye temperature, the indirect and direct band gaps, and the frequency‑dependent dielectric function for two polarization directions.

## Approach
We use plane‑wave pseudopotential DFT with the Perdew‑Wang 1991 (PW91) form of the generalized gradient approximation (GGA). The calculations are performed with an open‑source DFT code (Quantum ESPRESSO is a suitable choice). Starting from the experimentally reported hexagonal structure (space group R‑3m), we optimise the cell parameters and internal coordinate to find the ground‑state structure. The bulk modulus is obtained by fitting the energy‑volume data to the Birch‑Murnaghan equation of state. Elastic constants are extracted by applying small finite strains to the optimized cell and fitting the resulting stress‑energy relations to the hexagonal elastic energy formula. From the five independent elastic constants, all macroscopic mechanical properties are derived using the Reuss, Voigt, and Hill averaging schemes, together with sound velocities and the Debye temperature. The electronic band structure is computed along a high‑symmetry path to locate the valence‑band maximum and conduction‑band minimum, yielding the indirect and direct band gaps. Finally, the frequency‑dependent complex dielectric function is calculated for electric fields polarized in the (100) and (001) directions; the imaginary part ε2(ω) comes directly from the momentum matrix elements, and the real part ε1(ω) is obtained through the Kramers‑Kronig transformation.

## Reproduction target
Produce a single JSON file (`/app/outputs/results.json`) containing all computed quantities:

- Optimized lattice parameters a, c, and the internal parameter u (in Å).
- Bulk modulus B0 (in GPa).
- Five independent elastic constants C11, C12, C13, C33, C44 (in GPa).
- Derived mechanical properties (bulk, shear, and Young moduli, Poisson ratio, B/G ratio, and elastic anisotropy ratios) for the Reuss, Voigt, and Hill averaging schemes.
- Sound velocities (shear, compressional, and average, in m/s) and Debye temperatures (in K) for the three averaging schemes.
- Indirect band gap (F→Γ) and direct band gap (Γ) in eV.
- Static dielectric constants ε0 for the (100) and (001) polarizations.
- The full dielectric spectrum on a common energy grid: arrays for energy (eV) and for ε1, ε2 in the (100) and (001) directions.

The calculation must use a plane‑wave cutoff energy of 380 eV and a 10 × 10 × 10 Monkhorst–Pack k‑mesh. The structure must be initialized from the experimental delafossite phase (space group R‑3m, a = 2.858 Å, c = 16.958 Å, u = 0.1099) before relaxation. All values are to be reported in the exact keys and units specified in the output contract.

## Assets

- Quantum ESPRESSO (pw.x, ph.x, epsilon.x): https://www.quantum-espresso.org/
- GGA-PW91 pseudopotentials for Cu, Al, O: https://materialscloud.org/sssp
- Experimental crystal structure of CuAlO2: 10.1016/S0921-4526(97)00339-0

## Workflow steps

### Step 1: Prepare initial crystal structure
- Role: process
- Action: Build the CuAlO2 crystal structure in the delafossite phase (space group R-3m, hexagonal) using the experimental lattice parameters a=2.858 Å, c=16.958 Å, internal parameter u=0.1099. Generate the input file for the DFT code.
- Evidence: `/app/outputs/initial_structure.txt`

### Step 2: DFT geometry optimization
- Role: process
- Action: Perform a variable-cell relaxation of CuAlO2 using DFT with the GGA-PW91 exchange-correlation functional. Optimize the lattice constants and internal parameter to obtain the equilibrium structure. Fit the energy-volume data to an equation of state to determine the bulk modulus B0.
- Evidence: `/app/outputs/relaxed_structure.txt`

### Step 3: DFT elastic constants calculation
- Role: process
- Action: Apply finite-strain patterns to the optimized cell, compute the resulting stress and energy, and fit the data to the hexagonal elastic energy expression to extract the five independent elastic constants C11, C12, C13, C33, C44.
- Evidence: `/app/outputs/raw_elastic_constants.json`

### Step 4: DFT electronic structure calculation
- Role: process
- Action: Perform a self-consistent field (SCF) calculation followed by a non-SCF band-structure calculation along the high-symmetry path (Γ–F–Q–Z–Γ). Determine the indirect (F→Γ) and direct (Γ) band gaps.
- Evidence: `/app/outputs/band_structure.dat`

### Step 5: DFT dielectric function calculation
- Role: process
- Action: Using the SCF wavefunctions, compute the momentum matrix elements to obtain the frequency-dependent imaginary part ε2(ω) for electric fields polarized in the (100) and (001) directions. Apply the Kramers-Kronig transformation to derive the real part ε1(ω).
- Evidence: `/app/outputs/raw_epsilon.csv`

### Step 6: Compile all computed properties
- Role: scored (load-bearing)
- Action: Gather the optimized lattice parameters (a, c, u), bulk modulus B0, elastic constants, and derive the full set of mechanical properties: bulk, shear, and Young moduli (Reuss, Voigt, Hill averages), Poisson ratio, B/G ratio, elastic anisotropy ratios, sound velocities, and Debye temperature using the Voigt-Reuss-Hill averaging scheme. Include the indirect and direct band gaps, static dielectric constants (ε0 for (100) and (001) from the real part at ω=0), and the dielectric function spectra ε1(ω), ε2(ω) for both polarizations on a common energy grid. Write everything into a single JSON file.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with keys: lattice_parameters {a, c, u} (in Å), bulk_modulus_B0 (GPa), elastic_constants {C11, C12, C13, C33, C44} (GPa), derived_mechanical {B_R, B_V, B_H, G_R, G_V, G_H, E_R, E_V, E_H, v_R, v_V, v_H, B_G_Hill, Delta_p, Delta_s1, Delta_s2}, sound_velocities {vs_R, vs_V, vs_H, vp_R, vp_V, vp_H, vm_R, vm_V, vm_H} (m/s), Debye_temperature {Theta_R, Theta_V, Theta_H} (K), band_gaps {indirect_F_Gamma, direct_Gamma} (eV), static_dielectric_constants {epsilon0_100, epsilon0_001}, dielectric_spectrum {energy_array: [float], epsilon1_100: [float], epsilon2_100: [float], epsilon1_001: [float], epsilon2_001: [float]}.
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
- target_policy: metric_recompute
- description: Structured JSON containing all computed physical quantities and dielectric spectra.
- schema:
  - `type`: object
  - `required`: `lattice_parameters`, `bulk_modulus_B0`, `elastic_constants`, `derived_mechanical`, `sound_velocities`, `Debye_temperature`, `band_gaps`, `static_dielectric_constants`, `dielectric_spectrum`
  - `items`: object
  - `description`: Nested object; each key holds a sub-object as described in output_schema.

Notes: The dielectric spectrum arrays must share the same energy grid length. All scalar quantities and derived properties will be compared to hidden paper-reported values using appropriate tolerances. The dielectric spectrum will be evaluated by recomputed Pearson correlation against hidden reference arrays and by checking the static constants.

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
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "lattice_parameters",
          "bulk_modulus_B0",
          "elastic_constants",
          "derived_mechanical",
          "sound_velocities",
          "Debye_temperature",
          "band_gaps",
          "static_dielectric_constants",
          "dielectric_spectrum"
        ],
        "items": {},
        "description": "Nested object; each key holds a sub-object as described in output_schema."
      },
      "description": "Structured JSON containing all computed physical quantities and dielectric spectra."
    }
  ],
  "notes": "The dielectric spectrum arrays must share the same energy grid length. All scalar quantities and derived properties will be compared to hidden paper-reported values using appropriate tolerances. The dielectric spectrum will be evaluated by recomputed Pearson correlation against hidden reference arrays and by checking the static constants."
}
```

## How you are scored
A hidden verifier inspects your `results.json` and compares every entry to independently established reference data. For scalar quantities (lattice parameters, bulk modulus, elastic constants, mechanical moduli, sound velocities, Debye temperatures, band gaps, and static dielectric constants), the verifier checks the deviation against accepted tolerance margins; a deviation within tolerance earns full credit for that quantity. The dielectric spectrum is evaluated by structural similarity: the verifier cross‑correlates your ε2 arrays with reference spectra and checks that the static constants and peak positions are consistent. Your final reward is a weighted sum over all scored items, with the elastic, mechanical, dielectric, and band‑gap groups each contributing a meaningful share. You must actually run the DFT workflow to reproduce the numbers; simply reporting text‑book or paper‑look‑up values will not succeed because the tolerances are tailored to a legitimate re‑implementation with the specified functional and input protocol.

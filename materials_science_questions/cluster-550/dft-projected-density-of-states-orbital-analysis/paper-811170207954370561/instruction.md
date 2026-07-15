# First-Principles Prediction of Solar Radiation Shielding Properties of KB6

## Problem background
Metal hexaborides are of interest for solar radiation shielding applications because they can exhibit high visible-light transmittance while blocking near-infrared (NIR) radiation. Potassium hexaboride (KB6) is a candidate material whose structural, elastic, electronic, and optical properties have been predicted by first-principles calculations. However, the quantitative performance—especially the optical contrast between the visible and NIR regions—has not been extensively verified. This task aims to recompute the key properties of KB6 using density functional theory (DFT) to assess its potential as a solar radiation shielding material.

## Approach
The properties of KB6 are predicted using plane-wave pseudopotential DFT. The Perdew-Burke-Ernzerhof (PBE) exchange-correlation functional and ultrasoft pseudopotentials are employed. The workflow consists of: (1) geometry optimization to obtain the equilibrium lattice constant and internal atomic position; (2) computation of the single-crystal elastic constants via the stress-strain method; (3) self-consistent electronic structure calculation to obtain charge density, band structure, and density of states; (4) calculation of the frequency-dependent dielectric function within the independent-particle approximation, from which the absorption coefficient and reflectivity spectra are derived; (5) calculation of the theoretical transmittance of a compacted KB6 film by combining the reflectivity and absorption spectra with a film interference model. The overall goal is to evaluate the wavelength-dependent transmittance and determine whether KB6 shows the required optical contrast for solar radiation shielding.

## Reproduction target
The following quantities must be computed and reported as organized output artifacts:
- Optimized structural parameters: lattice constant a0, internal coordinate z, and inter- and intra-octahedron B–B bond lengths.
- Single-crystal elastic constants: C11, C12, and C44 for the cubic phase.
- Key features of the optical spectra: the energy and value of the main peak in the imaginary part of the dielectric function ε2, the energy and value of the principal absorption peak, and the energy and value of the reflectivity minimum (plasma edge).
- The theoretical transmittance spectrum T(λ) of a compacted KB6 film of thickness 100 nm over the wavelength range 200–2500 nm, calculated from the obtained reflectivity R(λ) and absorption coefficient α(λ) using the relation T = (1-R)² exp(-α d) / (1 - R² exp(-2α d)). The transmittance curve must be tabulated as a CSV file.

The reproduction target is to determine from these first-principles results whether KB6 can provide high visible transmittance and strong NIR suppression, i.e., the optical signature of an effective solar radiation shield.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotentials for K and B: https://www.materialscloud.org/discover/sssp/table
- Atomic Simulation Environment (ASE): ase
- Python scientific computing stack (numpy, scipy, matplotlib): numpy, scipy, matplotlib

## Workflow steps

### Step 1: DFT geometry optimization
- Role: scored
- Action: Relax the atomic positions and cell of KB6 (space group Pm-3m) using DFT (PBE, ultrasoft pseudopotentials, 400 eV cutoff, 20×20×20 k-point mesh, BFGS algorithm) until forces and stress converge. Start from the experimental geometry (a=4.2246 Å, z=0.1982). Extract the optimized lattice constant a0, internal coordinate z, and bond lengths B-B_in and B-B_out.
- Output file: `/app/outputs/step_01_structural_params.json`
- Format: json
- Contract: JSON object with keys: a0 (float, Å), z (float), B_B_in (float, Å), B_B_out (float, Å).
- Scoring: scored by hidden verifier

### Step 2: Elastic constants calculation
- Role: scored
- Action: Using the optimized geometry from Step 1, compute the elastic constants C11, C12, and C44 of cubic KB6 via the stress-strain method (apply small strains and compute stress).
- Output file: `/app/outputs/step_02_elastic_constants.json`
- Format: json
- Contract: JSON object with keys: C11 (float, GPa), C12 (float, GPa), C44 (float, GPa).
- Scoring: scored by hidden verifier

### Step 3: Electronic structure calculation
- Role: process
- Action: Perform a self-consistent DFT calculation on the optimized KB6 structure (same pseudopotentials, cutoff, and k-point mesh) to obtain the converged charge density. Then compute the electronic band structure along high-symmetry k-path and total/partial density of states (DOS). Archive the resulting charge density, wavefunction files, band structure data, and DOS data into electronic_structure_evidence.tar.gz.
- Evidence: `/app/outputs/electronic_structure_evidence.tar.gz`

### Step 4: Optical properties calculation
- Role: scored
- Action: Using the charge density and wave functions from Step 3, compute the frequency-dependent dielectric function (real ε1 and imaginary ε2) using the independent-particle approximation. Derive the absorption coefficient α(ω) and reflectivity R(ω). Extract the key optical features: ε2 peak energy and value, absorption peak energy and value, and reflectivity minimum energy and value (plasma edge).
- Output file: `/app/outputs/step_03_optical_properties.json`
- Format: json
- Contract: JSON object with keys: epsilon2_peak_energy (float, eV), epsilon2_peak_value (float, dimensionless), absorption_peak_energy (float, eV), absorption_peak_value (float, cm⁻¹), reflectivity_min_energy (float, eV), reflectivity_min_value (float, dimensionless).
- Scoring: scored by hidden verifier

### Step 5: Film transmittance calculation
- Role: scored (load-bearing)
- Action: For a compacted film of thickness d = 100 nm, calculate the theoretical transmittance T(λ) over the wavelength range 200–2500 nm using the formula T = (1-R)² exp(-αd) / (1 - R² exp(-2αd)), where R(λ) and α(λ) are obtained from Step 4. Report the transmittance curve as a CSV.
- Output file: `/app/outputs/step_04_transmittance_curve.csv`
- Format: csv
- Contract: CSV with columns: wavelength_nm (float), transmittance_fraction (float). Transmittance in the visible region should peak above 0.7.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_structural_params.json`
- `/app/outputs/step_02_elastic_constants.json`
- `/app/outputs/step_03_optical_properties.json`
- `/app/outputs/step_04_transmittance_curve.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_structural_params.json
- path: `/app/outputs/step_01_structural_params.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Optimized lattice parameter, internal coordinate, and bond lengths of KB6.
- schema:
  - `type`: object
  - `required`:
    - `a0`: float (Å)
    - `z`: float
    - `B_B_in`: float (Å)
    - `B_B_out`: float (Å)

### step_02_elastic_constants.json
- path: `/app/outputs/step_02_elastic_constants.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Single-crystal elastic constants of KB6.
- schema:
  - `type`: object
  - `required`:
    - `C11`: float (GPa)
    - `C12`: float (GPa)
    - `C44`: float (GPa)

### step_03_optical_properties.json
- path: `/app/outputs/step_03_optical_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Key peak energies and values of the dielectric function, absorption coefficient, and reflectivity.
- schema:
  - `type`: object
  - `required`:
    - `epsilon2_peak_energy`: float (eV)
    - `epsilon2_peak_value`: float (dimensionless)
    - `absorption_peak_energy`: float (eV)
    - `absorption_peak_value`: float (cm⁻¹)
    - `reflectivity_min_energy`: float (eV)
    - `reflectivity_min_value`: float (dimensionless)

### step_04_transmittance_curve.csv
- path: `/app/outputs/step_04_transmittance_curve.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Computed transmittance spectrum of a compacted KB6 film; curve shape (hanging bell), visible peak >0.7, and NIR trough <0.3 will be audited.
- schema:
  - `type`: table
  - `required_columns`: `wavelength_nm`, `transmittance_fraction`
  - `units`:
    - `wavelength_nm`: nm
    - `transmittance_fraction`: dimensionless

Notes: All outputs must be placed in /app/outputs. The transmittance curve must be computed from the reflectivity and absorption spectra; its shape and key features are verified against expected solar shielding behaviour.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_structural_params.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "a0": "float (Å)",
          "z": "float",
          "B_B_in": "float (Å)",
          "B_B_out": "float (Å)"
        }
      },
      "description": "Optimized lattice parameter, internal coordinate, and bond lengths of KB6."
    },
    {
      "file": "step_02_elastic_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "C11": "float (GPa)",
          "C12": "float (GPa)",
          "C44": "float (GPa)"
        }
      },
      "description": "Single-crystal elastic constants of KB6."
    },
    {
      "file": "step_03_optical_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "epsilon2_peak_energy": "float (eV)",
          "epsilon2_peak_value": "float (dimensionless)",
          "absorption_peak_energy": "float (eV)",
          "absorption_peak_value": "float (cm⁻¹)",
          "reflectivity_min_energy": "float (eV)",
          "reflectivity_min_value": "float (dimensionless)"
        }
      },
      "description": "Key peak energies and values of the dielectric function, absorption coefficient, and reflectivity."
    },
    {
      "file": "step_04_transmittance_curve.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "wavelength_nm",
          "transmittance_fraction"
        ],
        "units": {
          "wavelength_nm": "nm",
          "transmittance_fraction": "dimensionless"
        }
      },
      "description": "Computed transmittance spectrum of a compacted KB6 film; curve shape (hanging bell), visible peak >0.7, and NIR trough <0.3 will be audited."
    }
  ],
  "notes": "All outputs must be placed in /app/outputs. The transmittance curve must be computed from the reflectivity and absorption spectra; its shape and key features are verified against expected solar shielding behaviour."
}
```

## How you are scored
A hidden verifier inspects the artifacts you submit under /app/outputs. Each stage is assessed independently:
- Structural parameters (step_01_structural_params.json): compared to expected physical ranges; errors beyond accepted tolerances reduce the score.
- Elastic constants (step_02_elastic_constants.json): values are checked for mechanical stability and compared to reference data; deviations outside expected margins lower the score.
- Optical features (step_03_optical_properties.json): the reported peak energies and intensities are compared to the expected spectral features derived from the underlying electronic structure; mismatches in peak location or magnitude reduce the score.
- Transmittance curve (step_04_transmittance_curve.csv): the verifier audits the overall shape, particularly the presence of a pronounced maximum in the visible range and a deep minimum in the near-infrared, as well as the mutual consistency with the submitted absorption and reflectivity data. Failure to exhibit the characteristic solar-shielding contrast leads to a low score.

The final reward is a weighted sum of these sub-scores, with the transmittance curve carrying the largest weight. Simply reporting literature numbers without correct underlying calculations will not produce a high score; the verifier cross-checks self-consistency and expected physical trends.

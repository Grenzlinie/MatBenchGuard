# Computation of Net Orbital Magnetization and Antisymmetric Optical Conductivity in Orthorhombic Perovskites

## Problem background
In orthorhombic perovskite oxides with the chemical formula LaMO₃ (M=Cr, Mn, Fe), antiferromagnetic spin ordering coexists with significant lattice distortions. When spin–orbit coupling (SOC) is present, the combination of this spin order and the low‑symmetry crystal field can give rise to a net orbital magnetization and to optical nonreciprocity, manifesting as a magneto‑optical Kerr effect. Understanding whether such an effect can be substantial, how it depends on the type of antiferromagnetic ordering and the direction of the spin magnetization, and what its spectroscopic signature is requires a quantitative first‑principles investigation. This task aims to compute, from first principles, the net orbital magnetization vectors for the three compounds when the spin direction is aligned along each orthorhombic axis, as well as the antisymmetric part of the optical conductivity spectrum for the most stable magnetic configuration of each compound.

## Approach
The workflow is based on density‑functional theory (DFT) within the local‑spin‑density approximation (LSDA) with spin–orbit coupling treated self‑consistently. The experimental crystal structures of orthorhombic LaCrO₃, LaMnO₃, and LaFeO₃ are used without relaxation. For each compound, collinear antiferromagnetic spin arrangements are set up: G‑type (all nearest‑neighbor spins antiparallel) for Cr and Fe, and A‑type (ferromagnetic planes stacked antiferromagnetically) for Mn. The scalar‑relativistic LSDA calculation is performed first, followed by inclusion of SOC to obtain the spin–orbit‑coupled eigenstates and eigenvalues. This is done for spin directions e parallel to the a, b, and c axes of the orthorhombic cell.

From the SOC electronic structure, the orbital magnetic moment at each transition‑metal site is extracted by summing the expectation values of the angular momentum operators over the occupied states. The net orbital magnetization is then obtained by averaging over the four formula units in the unit cell using the symmetry operations appropriate for the given antiferromagnetic type; this averaging is essential because the local orbital moments are not collinear with the spin direction. The result is a vector (M_Lx, M_Ly, M_Lz) for each combination of compound and spin orientation.

For the lowest‑energy magnetic configuration of each compound (to be determined by comparing the magnetocrystalline anisotropy energy among the a, b, c directions), the optical conductivity tensor σ(ω) is computed from the interband transition matrix elements and the SOC eigenstates, using a phenomenological relaxation time corresponding to τ⁻¹ = 0.02 Ry. The antisymmetric part σ^A(ω) is extracted from the off‑diagonal elements of the tensor, and its imaginary part is reported as a function of photon energy from 0 to 8 eV.

## Reproduction target
Produce two scored CSV artifacts that together quantify the magneto‑optical response:

1. **Net orbital magnetization vectors**: a table containing, for each compound (LaCrO₃, LaMnO₃, LaFeO₃) and each spin orientation (a, b, c), the Cartesian components of the net orbital magnetic moment (M_Lx, M_Ly, M_Lz, in units of μB). The table must have exactly nine rows (3 compounds × 3 orientations).

2. **Antisymmetric optical conductivity spectrum**: a table containing, for the ground‑state magnetic configuration of each compound (LaCrO₃ with G‑type order and spin along c; LaMnO₃ with A‑type order and spin along b; LaFeO₃ with G‑type order and spin along a), the imaginary part of the antisymmetric conductivity Im[σ^A(ω)] as a function of photon energy. The energy axis must cover the interval 0–8 eV with a spacing of at most 0.1 eV. The conductivity is reported in units of 10³ Ω⁻¹ cm⁻¹.

Both artifacts must be written to the exact output paths specified in the workflow steps and must conform to the column schemas described in the output contract.

## Assets

- Quantum ESPRESSO (or equivalent open-source DFT+SOI code): https://www.quantum-espresso.org/
- Experimental crystal structures of orthorhombic LaMO3 (M=Cr, Mn, Fe): 10.1016/0022-3697(57)90190-7 and 10.1016/0022-5088(71)90163-4

## Workflow steps

### Step 1: DFT+SOI electronic structure calculations
- Role: process
- Action: Perform scalar-relativistic LSDA calculations and subsequent spin-orbit coupling (SOC) calculations for orthorhombic LaCrO3, LaMnO3, and LaFeO3 in their respective antiferromagnetic magnetic configurations (G-type for Cr and Fe, A-type for Mn) with spin directions e aligned along a, b, and c axes. Use experimental crystal structure parameters and a suitable pseudopotential/k-point mesh. Save self-consistent electron density and wavefunctions.
- Evidence: `/app/outputs/dft_calculation_log.txt`

### Step 2: Net orbital magnetization extraction
- Role: scored (load-bearing)
- Action: From the SOC electronic structure, compute the net orbital magnetic moment vector for each compound and each spin orientation (a, b, c). Use appropriate post-processing (e.g., summing orbital moments from the DFT output over all atoms). Output the results as a CSV file.
- Output file: `/app/outputs/step_02_net_orbital_magnetization.csv`
- Format: csv
- Contract: CSV with columns: compound (string, e.g., LaCrO3), spin_orientation (a|b|c), M_Lx (float), M_Ly (float), M_Lz (float)
- Scoring: scored by hidden verifier

### Step 3: Optical conductivity calculation
- Role: process
- Action: Using the SOC eigenstates and eigenvalues, compute the interband optical conductivity tensor σ(ω) for the ground-state magnetic configuration of each compound (LaCrO3: G-type, e||c; LaMnO3: A-type, e||b; LaFeO3: G-type, e||a). Use a phenomenological relaxation time with τ⁻¹ = 0.02 Ry. Obtain the full conductivity tensor as a function of photon energy from 0 to 8 eV with an energy spacing ≤ 0.1 eV.
- Evidence: `/app/outputs/conductivity_raw.txt`

### Step 4: Antisymmetric conductivity spectrum
- Role: scored
- Action: From the computed optical conductivity tensor, extract the antisymmetric part σ^A(ω) for each compound in its ground-state magnetic configuration. Output the imaginary part Im[σ^A(ω)] as a function of photon energy. Write the data to a CSV file.
- Output file: `/app/outputs/step_05_antisymmetric_conductivity.csv`
- Format: csv
- Contract: CSV with columns: compound (string, e.g., LaCrO3), energy_eV (float, photon energy in eV), imag_sigma_A (float, in 10³ Ω⁻¹ cm⁻¹)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_02_net_orbital_magnetization.csv`
- `/app/outputs/step_05_antisymmetric_conductivity.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_02_net_orbital_magnetization.csv
- path: `/app/outputs/step_02_net_orbital_magnetization.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Net orbital magnetization vectors for three compounds and three spin orientations. Checker compares to known reference values with tolerances.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `spin_orientation`, `M_Lx`, `M_Ly`, `M_Lz`
  - `units`:
    - `M_Lx`: μB
    - `M_Ly`: μB
    - `M_Lz`: μB

### step_05_antisymmetric_conductivity.csv
- path: `/app/outputs/step_05_antisymmetric_conductivity.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Antisymmetric part of optical conductivity for each compound's ground state. Checker compares spectra to reference curves (digitized from paper) allowing small energy shifts and scaling.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `energy_eV`, `imag_sigma_A`
  - `units`:
    - `energy_eV`: eV
    - `imag_sigma_A`: 10³ Ω⁻¹ cm⁻¹

Notes: The submitted orbital magnetization vectors and conductivity spectra will be compared against reference values derived from the paper's reported local tensors and digitized figure, with tolerances that account for inherent spread due to different DFT implementations and convergence settings. Trends in orientation dependence are also evaluated.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_02_net_orbital_magnetization.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "spin_orientation",
          "M_Lx",
          "M_Ly",
          "M_Lz"
        ],
        "units": {
          "M_Lx": "μB",
          "M_Ly": "μB",
          "M_Lz": "μB"
        }
      },
      "description": "Net orbital magnetization vectors for three compounds and three spin orientations. Checker compares to known reference values with tolerances."
    },
    {
      "file": "step_05_antisymmetric_conductivity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "energy_eV",
          "imag_sigma_A"
        ],
        "units": {
          "energy_eV": "eV",
          "imag_sigma_A": "10³ Ω⁻¹ cm⁻¹"
        }
      },
      "description": "Antisymmetric part of optical conductivity for each compound's ground state. Checker compares spectra to reference curves (digitized from paper) allowing small energy shifts and scaling."
    }
  ],
  "notes": "The submitted orbital magnetization vectors and conductivity spectra will be compared against reference values derived from the paper's reported local tensors and digitized figure, with tolerances that account for inherent spread due to different DFT implementations and convergence settings. Trends in orientation dependence are also evaluated."
}
```

## How you are scored
A hidden verifier will independently examine the two scored artifacts you produce (net orbital magnetization and antisymmetric conductivity). The verifier does not rely on any self‑reported summary; it reads the actual CSV tables you write. Each artifact contributes a weighted fraction to the final reward. The verifier compares your computed magnetization vectors to reference values derived from the published local orbital‑response tensors and symmetry relations, and it compares your conductivity spectra to reference digitised curves. The tolerances are chosen to accommodate legitimate differences arising from the choice of DFT code, pseudopotentials, and convergence settings, while still requiring that the essential physics — the orientation dependence of the orbital moment and the shape and relative amplitudes of the conductivity spectra — is correctly captured. Your task is to produce these quantities by faithfully executing the described computational procedure; merely copying numbers from a report will not pass the verification.

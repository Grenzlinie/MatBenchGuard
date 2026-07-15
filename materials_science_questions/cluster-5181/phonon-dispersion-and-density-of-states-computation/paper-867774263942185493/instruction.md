# Light-induced shear phonon mode renormalization and instability in bilayer graphene

## Problem background
Shear phonons in bilayer graphene are low-frequency, Raman-active vibrational modes that correspond to the lateral sliding of the two atomic layers against each other. These modes are doubly degenerate in the absence of external perturbations. Under irradiation by an intense, ultrafast optical pulse, the electronic structure is dynamically dressed, and nonlinear Raman forces can couple the light field to the phonon displacement. In particular, a third-order Raman mechanism—where the phonon displacement interacts quadratically with the light field—may renormalize the phonon frequencies, lift the degeneracy, and even cause a phonon softening that leads to a structural instability at a critical field amplitude. Determining the magnitude of this light-induced mode splitting and the critical field at which the lower-frequency mode vanishes, for a given set of material and laser parameters, is the central computational question addressed here.

## Approach
The calculation is based on the low-energy two-band model of bilayer graphene, which describes the quasiparticle dispersion near the K and K′ points. The light-induced renormalization of the shear phonons is captured by a phonon self-energy that arises from two contributions: an instantaneous part (Π^ins) from two-phonon–electron coupling, and a retarded part (Π^ret) from one-phonon–electron coupling dressed by photons. These susceptibilities are evaluated using diagrammatic perturbation theory, where the photon field enters through the paramagnetic current operator, and electron-phonon vertices include both one- and two-phonon couplings. With the susceptibilities in hand, the dynamical matrix of the shear phonons is constructed as a function of the incident electric field amplitude. For the regime where the laser frequency is much larger than the phonon frequency, the adiabatic approximation (setting the phonon frequency to zero in the dynamical matrix) is used to obtain the renormalized normal-mode frequencies by diagonalization. The critical field for instability is found by solving for the field amplitude at which the lower normal-mode frequency becomes zero. The workflow implements these steps numerically using the specified model parameters and laser conditions.

## Reproduction target
For bilayer graphene under a monochromatic, linearly polarized optical field with chemical potential μ = 200 meV, laser photon energy ℏω = 2μ = 400 meV, electronic temperature Te = 300 K, electron scattering rate ℏΓe = 5 meV, phonon damping ℏΓp = 0.1 meV, bare shear phonon frequency ℏΩ0 = 3.9 meV, and polarization angle θ = 0°, you must compute the light-induced renormalized shear phonon frequencies (Ω+ and Ω−) at three electric field amplitudes E0 = 0.05, 0.10, and 0.15 V/nm. Additionally, you must determine the critical electric field amplitude E_crit (in V/nm) at which the lower normal-mode frequency Ω− vanishes, signaling the onset of a structural instability. The results must be saved in the two CSV files described in the workflow steps.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Implement light-induced phonon self-energy formalism
- Role: process
- Action: Implement the analytical expressions for instantaneous (Π^ins) and retarded (Π^ret) light-induced phonon self-energy tensors for bilayer graphene using the low-energy two-band model. Encode the Hamiltonian, electron-phonon couplings, and light-matter vertices. Set the fixed model parameters: effective mass derived from monolayer velocity v=10^6 m/s and interlayer hopping γ1=-0.4 eV; one-phonon and two-phonon electron-phonon coupling constants; bare shear phonon frequency ℏΩ0=3.9 meV; mass density ρ; phonon damping ℏΓp=0.1 meV; electronic scattering rate ℏΓe=5 meV; spin-valley degeneracy Nf=4. This step produces the numerical routines used in subsequent steps.
- Evidence: none

### Step 2: Compute light-induced normal mode frequencies
- Role: scored (load-bearing)
- Action: Using the implemented susceptibility functions, for chemical potential μ=200 meV, laser frequency ℏω=2μ=400 meV, electronic temperature Te=300 K, and polarization angle θ=0°, construct the light-dressed phonon dynamical matrix for each electric field amplitude E0 ∈ {0.05, 0.10, 0.15} V/nm. Diagonalize the matrix and record the renormalized shear phonon frequencies Ω+ and Ω− in meV. Save the results to a CSV file.
- Output file: `/app/outputs/step_01_normal_modes.csv`
- Format: csv
- Contract: columns: E0_V_per_nm (float), Omega_plus_meV (float), Omega_minus_meV (float); three rows for E0=0.05, 0.10, 0.15 V/nm
- Scoring: scored by hidden verifier

### Step 3: Determine critical field amplitude for phonon instability
- Role: scored (load-bearing)
- Action: Using the same parameters and numerical model from previous steps, find the electric field amplitude E_crit (V/nm) at which the lower normal mode frequency Ω− vanishes (becomes zero within numerical accuracy). Output the critical field to a CSV file.
- Output file: `/app/outputs/step_02_critical_field.csv`
- Format: csv
- Contract: single row with column E_crit_V_per_nm (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_normal_modes.csv`
- `/app/outputs/step_02_critical_field.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_normal_modes.csv
- path: `/app/outputs/step_01_normal_modes.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Light-induced renormalized shear phonon frequencies at three electric field amplitudes.
- schema:
  - `type`: table
  - `required_columns`: `E0_V_per_nm`, `Omega_plus_meV`, `Omega_minus_meV`
  - `units`:
    - `E0_V_per_nm`: V/nm
    - `Omega_plus_meV`: meV
    - `Omega_minus_meV`: meV

### step_02_critical_field.csv
- path: `/app/outputs/step_02_critical_field.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Critical electric field amplitude at which the lower shear phonon mode vanishes, signaling a light-induced structural instability.
- schema:
  - `type`: table
  - `required_columns`: `E_crit_V_per_nm`
  - `units`:
    - `E_crit_V_per_nm`: V/nm

Notes: The checker compares the agent's reported values against hidden gold values extracted from the paper's figures, using relative tolerances appropriate for the numerical method (10% for frequencies, 20% for critical field). All model parameters and conditions are specified in the workflow steps.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_normal_modes.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "E0_V_per_nm",
          "Omega_plus_meV",
          "Omega_minus_meV"
        ],
        "units": {
          "E0_V_per_nm": "V/nm",
          "Omega_plus_meV": "meV",
          "Omega_minus_meV": "meV"
        }
      },
      "description": "Light-induced renormalized shear phonon frequencies at three electric field amplitudes."
    },
    {
      "file": "step_02_critical_field.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "E_crit_V_per_nm"
        ],
        "units": {
          "E_crit_V_per_nm": "V/nm"
        }
      },
      "description": "Critical electric field amplitude at which the lower shear phonon mode vanishes, signaling a light-induced structural instability."
    }
  ],
  "notes": "The checker compares the agent's reported values against hidden gold values extracted from the paper's figures, using relative tolerances appropriate for the numerical method (10% for frequencies, 20% for critical field). All model parameters and conditions are specified in the workflow steps."
}
```

## How you are scored
A hidden verifier will independently inspect each of your scored artifacts (the normal-mode CSV and the critical-field CSV) and compare the values you report against reference results derived from the original work. Each artifact is assigned a weight, and the verifier combines the per-artifact scores into a single reward between 0 and 1. The comparison accounts for reasonable numerical spread that arises from different implementations; it does not require exact bit-level agreement. The verifier never reveals the reference values or tolerances, so simply reporting a number without performing the required computation will not succeed.

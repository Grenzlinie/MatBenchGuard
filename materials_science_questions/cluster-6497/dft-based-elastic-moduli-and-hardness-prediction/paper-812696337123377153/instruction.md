# First-principles DFT study of alpha-Sn with non-local pseudopotential and spin-orbit coupling

## Problem background
Alpha-Sn (grey tin) is a zero-gap semiconductor whose electronic structure and ground-state properties are strongly influenced by non-local pseudopotential effects and spin-orbit coupling. Accurate first-principles prediction of its band dispersion, equilibrium lattice constant, total energy, and bulk modulus is important for understanding the fundamental physics of this material and for testing density-functional methods. Earlier self-consistent local pseudopotential calculations provided a baseline description, but non-local corrections (s and d channels) and spin-orbit interactions are expected to modify both the band eigenvalues and the derived equilibrium quantities.

## Approach
The electronic structure is obtained by solving the Kohn-Sham equations within the local-density approximation, using a plane-wave basis set and a non-local pseudopotential. The ionic pseudopotential is constructed with a local part (parametrized in reciprocal space) and angular-momentum-dependent non-local projectors for l=0 and l=2, plus a spin-orbit term. Exchange and correlation are treated in the Xα approximation. The equations are iterated to self-consistency, yielding converged wavefunctions and charge density.

From the self-consistent results, band energies are extracted at the high-symmetry k-points Γ, X, and L. The ground-state properties are determined within the momentum-space total-energy formalism. The total crystal energy per atom is computed for several lattice constants, with contributions from the kinetic energy, Hartree and exchange-correlation terms, the non-local and spin-orbit parts of the pseudopotential, a pseudo-atom correction, and the Ewald ion-ion energy. A polynomial fit to the energy-volume data locates the energy minimum (equilibrium lattice constant), and the second derivative at the minimum yields the bulk modulus.

## Reproduction target
Perform a series of self-consistent DFT calculations for α-Sn in the diamond structure using the specified non-local pseudopotential (including spin-orbit coupling) and the prescribed computational parameters. From the converged electronic structure, extract the band eigenvalues at the Γ, X, and L k-points and report them in eV relative to the valence band maximum. Separately, compute the total energy per atom for several lattice constants near the expected equilibrium value. Fit the resulting energy-versus-lattice-constant data to a polynomial, and from the fitting curve determine (i) the equilibrium lattice constant (in Å), (ii) the total energy at that minimum (in Ryd per atom), and (iii) the bulk modulus (in 10^11 dyn/cm²). All numerical outputs must be saved as band_eigenvalues.json and ground_state_properties.json following the output contract below.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- NumPy, SciPy: numpy, scipy

## Workflow steps

### Step 1: Self-consistent DFT calculation
- Role: process
- Action: Perform a self-consistent DFT calculation for α-Sn in the diamond structure using a plane-wave basis with a non-local pseudopotential. The pseudopotential must include local and non-local (l=0 and l=2) components and spin-orbit coupling. Use the pseudopotential parameters: local part b1=−0.565 Ryd, b2=1.087, b3=0.022, b4=0.018; non-local part α0=0, β0=−0.015, A2=−0.002 Ryd, model radius Rm=2 a.u.; spin-orbit form factor λ=0.011 Ryd. Employ a plane-wave kinetic energy cutoff sufficient to converge the results and a suitable k-point mesh for the irreducible Brillouin zone. Achieve self-consistency in the screening potential. This step produces the converged wavefunctions, charge density, and eigenvalues necessary for subsequent analysis.
- Evidence: `/app/outputs/dft_convergence.log`

### Step 2: Extract band eigenvalues at symmetry points
- Role: scored
- Action: From the self-consistent DFT results, extract the electronic eigenvalues at the high-symmetry k-points Γ, X, and L. Refer all energies to the valence band maximum and report them in eV. Save the extracted lists.
- Output file: `/app/outputs/band_eigenvalues.json`
- Format: json
- Contract: JSON object with keys 'Gamma', 'X', 'L'; each key maps to a list of floats (energies in eV).
- Scoring: scored by hidden verifier

### Step 3: Determine equilibrium ground-state properties
- Role: scored (load-bearing)
- Action: Using the same DFT framework and pseudopotential parameters as above, compute the total energy per atom of α-Sn (including the Ewald term and the momentum-space formalism) for several lattice constants near the expected equilibrium value. Perform a polynomial fit to the energy versus lattice-constant data to locate the minimum. Compute the second derivative at the minimum to obtain the bulk modulus. Output the equilibrium lattice constant (in Å), the total energy at that minimum (in Ryd per atom), and the bulk modulus (in 10^11 dyn/cm²).
- Output file: `/app/outputs/ground_state_properties.json`
- Format: json
- Contract: JSON object with keys: lattice_constant_A (float), total_energy_Ryd_per_atom (float), bulk_modulus_10^11_dyn_cm2 (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_eigenvalues.json`
- `/app/outputs/ground_state_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_eigenvalues.json
- path: `/app/outputs/band_eigenvalues.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Electronic band energies at high-symmetry points Γ, X, L produced by the self-consistent non-local pseudopotential calculation with spin-orbit coupling.
- schema:
  - `type`: object
  - `required`:
    - `Gamma`: array of numbers (energies in eV)
    - `X`: array of numbers (energies in eV)
    - `L`: array of numbers (energies in eV)
  - `units`:
    - `energies`: eV

### ground_state_properties.json
- path: `/app/outputs/ground_state_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Equilibrium lattice constant, total energy, and bulk modulus of α-Sn derived from DFT total energy calculations at multiple lattice constants and a polynomial fit.
- schema:
  - `type`: object
  - `required`:
    - `lattice_constant_A`: number
    - `total_energy_Ryd_per_atom`: number
    - `bulk_modulus_10^11_dyn_cm2`: number

Notes: The hidden checker compares the agent's submitted eigenvalues and equilibrium properties to reference values using appropriate tolerances. Scoring rewards honest reproduction of the computational procedure.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_eigenvalues.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "Gamma": "array of numbers (energies in eV)",
          "X": "array of numbers (energies in eV)",
          "L": "array of numbers (energies in eV)"
        },
        "units": {
          "energies": "eV"
        }
      },
      "description": "Electronic band energies at high-symmetry points Γ, X, L produced by the self-consistent non-local pseudopotential calculation with spin-orbit coupling."
    },
    {
      "file": "ground_state_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "lattice_constant_A": "number",
          "total_energy_Ryd_per_atom": "number",
          "bulk_modulus_10^11_dyn_cm2": "number"
        }
      },
      "description": "Equilibrium lattice constant, total energy, and bulk modulus of α-Sn derived from DFT total energy calculations at multiple lattice constants and a polynomial fit."
    }
  ],
  "notes": "The hidden checker compares the agent's submitted eigenvalues and equilibrium properties to reference values using appropriate tolerances. Scoring rewards honest reproduction of the computational procedure."
}
```

## How you are scored
An automated hidden verifier independently examines your two submitted artifacts: band_eigenvalues.json and ground_state_properties.json. Each artifact is compared against reference values that are consistent with a correct execution of the described protocol. The verifier produces a numerical score for each artifact and then combines them, with the ground-state-properties file carrying the larger weight, to compute a final reward between 0 and 1. The verifier does not inspect your code or intermediate logs; only the contents of the JSON files are assessed. To achieve a high score, your outputs must faithfully reflect the results of a genuine self-consistent non-local pseudopotential calculation with spin-orbit coupling as outlined in the workflow steps.

# Phonon Magnetic Moment from Hall Viscosity in Dirac Semimetal

## Problem background
Phonons in doped Dirac semimetals can carry unexpectedly large orbital magnetic moments, far exceeding simple ionic models. Experiments on Cd₃As₂ have revealed a significant magnetic moment for a chiral optical phonon mode, but the physical origin of this enhancement remains debated. This work proposes that optical phonons couple to the Dirac electrons as an emergent frame field, allowing the phonon motion to generate a Hall viscosity stress in the electron fluid. The resulting feedback produces a net phonon magnetic moment, linking the phonon magnetism directly to the electronic Hall viscosity. The primary goal is to evaluate this frame-field mechanism for the inversion-odd E_u optical mode in Cd₃As₂ by computing the phonon magnetic moment from first principles and comparing it to the experimentally observed magnitude.

## Approach
The approach treats the low-energy Dirac fermions of Cd₃As₂ in the presence of a frozen phonon distortion of the E_u mode. The distortion acts as a frame field that renders the Dirac cone elliptical, changing the Fermi velocity anisotropically and thereby coupling the phonon coordinate to the electrons. First-principles DFT calculations are used to obtain the equilibrium and distorted band structures. From these, the Fermi velocity v_F and the electron-phonon coupling parameter β/a are extracted. With v_F, the electron density and effective mass at a fixed Fermi energy ε_F = 0.1 eV are derived using free-fermion relations. Using the semiclassical formula for Hall viscosity in the presence of a magnetic field B and a transport lifetime τ, η_H is computed. Finally, the phonon magnetic moment μ_ph is obtained from the relation μ_ph = (ħ β² / (ρ_I a²)) (η_H / B), where a is the lattice constant and ρ_I the ion mass density, and the chiral phonon frequency splitting is calculated.

## Reproduction target
Reproduce the phonon magnetic moment of the E_u mode in Cd₃As₂ and the supporting parameters. Follow the ordered workflow: (1) prepare the crystal structure and pseudopotentials, (2) run a DFT ground-state calculation to obtain the unperturbed Dirac cone, (3) compute phonon dispersions and identify the E_u mode eigenvector, (4) run a frozen-phonon DFT calculation with a 1 Å displacement along the eigenvector, and (5) post-process the band structures to extract v_F and β/a, compute η_H, μ_ph, and the chiral frequency splitting. All results must be written to `/app/outputs/results.csv` with the columns parameter, value, unit, including exactly the rows: Eu_mode_frequency, beta_over_a, v_F, eta_H, mu_ph, omega_plus, omega_minus, and optionally tau and B. Use the fixed parameters ε_F = 0.1 eV, τ = 0.1 ps, B = 1 T, and ρ_I = 3.03×10³ kg/m³. The target is to produce values consistent with a self‑contained theoretical framework and the known experimental magnitude of the phonon magnetic moment.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org
- PHONOPY: https://phonopy.github.io/phonopy
- ONCV pseudopotentials for Cd and As: http://pseudopotentials.quantum-espresso.org/pslibrary
- Cd3As2 crystal structure from Ali et al. 2014: 10.1021/ic500558q

## Workflow steps

### Step 1: Prepare crystal structure and pseudopotentials
- Role: process
- Action: Obtain the crystal structure of Cd3As2 from the literature (DOI 10.1021/ic500558q) and prepare the necessary ONCV pseudopotential files for Cd and As for Quantum ESPRESSO.
- Evidence: `/app/outputs/setup.log`

### Step 2: DFT self-consistent ground-state calculation
- Role: process
- Action: Run a self-consistent field (SCF) DFT calculation for Cd3As2 using Quantum ESPRESSO with the PBE functional and a 2×2×2 k‑grid. From the converged charge density, compute the electronic band structure along the Γ‑Z direction and in‑plane kx,ky contours near the Dirac point.
- Evidence: `/app/outputs/scf_output.log`

### Step 3: Phonon calculation and Eu mode identification
- Role: process
- Action: Construct a supercell and compute force constants via finite displacements using Quantum ESPRESSO. Use these with PHONOPY to obtain phonon dispersions and eigenvectors. Identify the infrared‑active E_u optical mode at the Γ point and extract its eigenvector.
- Evidence: `/app/outputs/phonon_dispersion.dat`

### Step 4: Frozen‑phonon DFT calculation for E_u distortion
- Role: process
- Action: Construct a unit cell displaced along the E_u eigenvector with an amplitude of 1 Å. Run an SCF calculation with the same functional and k‑grid as in the equilibrium run. Output the distorted band structure and in‑plane energy contours near the Dirac point.
- Evidence: `/app/outputs/frozen_scf.log`

### Step 5: Post‑processing and calculation of phonon magnetic moment
- Role: scored (load-bearing)
- Action: From the equilibrium and frozen‑phonon band structures, extract the Fermi velocity v_F and the electron‑phonon coupling parameter β/a. At ε_F = 0.1 eV, compute n_e = ε_F³ / [3π² (ħ v_F)³] and m* = ε_F / v_F². Using τ = 0.1 ps and B = 1 T, calculate ω_c = eB/m*, ν_H = (v_F²/2) (ω_c τ²)/(1+4 ω_c² τ²), η_H = n_e m* ν_H. Compute μ_ph = (ħ β² / (ρ_I a²)) (η_H / B) with ρ_I = 3.03×10³ kg/m³ and lattice constant a from the literature. Compute chiral phonon frequencies ω_± = sqrt(ω₀² + δω²) ± δω, where ω₀ is the bare Eu phonon frequency and δω = η_H β² / (2 a² ρ_I). Write all quantities to /app/outputs/results.csv.
- Output file: `/app/outputs/results.csv`
- Format: csv
- Contract: CSV with header 'parameter,value,unit'. Required rows: Eu_mode_frequency (THz), beta_over_a (1/Ang), v_F (m/s), eta_H (kg/(m·s)), mu_ph (Bohr_magneton), omega_plus (THz), omega_minus (THz). Optional: tau (ps), B (T).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.csv
- path: `/app/outputs/results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Set of computed quantities derived from the DFT pipeline that constitute the phonon magnetic moment and its supporting parameters.
- schema:
  - `type`: table
  - `required_columns`: `parameter`, `value`, `unit`
  - `description`: CSV with rows for each computed quantity; value column holds the numeric result, unit column the corresponding unit. Expected parameter names: Eu_mode_frequency, beta_over_a, v_F, eta_H, mu_ph, omega_plus, omega_minus.

Notes: The checker will recompute mu_ph from the reported β/a, v_F, and η_H to verify internal consistency and will compare the final mu_ph to a hidden paper‑reported reference value with a tolerance. Other rows are audited for completeness.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "parameter",
          "value",
          "unit"
        ],
        "description": "CSV with rows for each computed quantity; value column holds the numeric result, unit column the corresponding unit. Expected parameter names: Eu_mode_frequency, beta_over_a, v_F, eta_H, mu_ph, omega_plus, omega_minus."
      },
      "description": "Set of computed quantities derived from the DFT pipeline that constitute the phonon magnetic moment and its supporting parameters."
    }
  ],
  "notes": "The checker will recompute mu_ph from the reported β/a, v_F, and η_H to verify internal consistency and will compare the final mu_ph to a hidden paper‑reported reference value with a tolerance. Other rows are audited for completeness."
}
```

## How you are scored
Each workflow stage's artefact is evaluated by a hidden verifier. The scored artefact is `/app/outputs/results.csv`. The verifier independently recomputes the magnetic moment from your reported β/a, v_F, and η_H using the same formulas, requiring internal consistency to better than 5%. It then compares your final μ_ph against a hidden reference value. In addition, it checks that the Eu mode frequency, β/a, and v_F lie within physically reasonable ranges expected from the DFT calculations. Partial credit is awarded for correct extraction of intermediate parameters. The final reward is a weighted combination of these checks; simply reporting plausible numbers without correctly executing the DFT workflow is insufficient to pass.

# First‑principles thermoelectric figure of merit of γ‑graphyne from full electron–phonon coupling

## Problem background
γ‑graphyne is a two‑dimensional carbon allotrope that contains both sp² and sp hybridised bonds, forming a planar hexagonal network. Unlike graphene, it possesses a direct band gap, making it a candidate for thermoelectric energy conversion. The thermoelectric performance of a material is measured by the dimensionless figure of merit ZT = S²σT/(κ_e + κ_ph), where S is the Seebeck coefficient, σ the electrical conductivity, T the absolute temperature, and κ_e, κ_ph the electronic and phonon thermal conductivities. Accurately predicting ZT from first principles requires more than a simplified deformation‑potential treatment: optical‑phonon contributions to carrier scattering can be significant and must be included through full electron–phonon coupling calculations. This task re‑computes the ZT of γ‑graphyne at an elevated temperature using a complete density‑functional‑theory‑based workflow and evaluates whether the material can achieve favourable thermoelectric performance.

## Approach
The approach is a first‑principles computational pipeline. First, density functional theory (DFT) is used to relax the crystal structure and obtain electronic states. Density functional perturbation theory (DFPT) then computes phonon frequencies and the electron–phonon (e‑ph) coupling matrix elements on a coarse reciprocal‑space mesh. Maximally localized Wannier functions are employed to interpolate these quantities onto a dense mesh, providing ultra‑fine sampling of the e‑ph coupling. From the interpolated matrix elements, the electron self‑energy and carrier relaxation times are evaluated. With the band energies, group velocities, and relaxation times, the semiclassical Boltzmann transport equation is solved for the electronic transport coefficients: Seebeck coefficient, electrical conductivity, and electronic thermal conductivity (the latter via the Wiedemann–Franz law using a computed Lorenz number). Separately, phonon thermal conductivity is obtained by solving the phonon Boltzmann transport equation using second‑ and third‑order interatomic force constants computed on a supercell. Finally, the thermoelectric figure of merit is assembled as ZT = S²σT/(κ_e + κ_ph). The calculations are performed at 600 K for two specific conditions: p‑type doping with transport along the x‑direction of the crystal, and n‑type doping with transport along the y‑direction.

## Reproduction target
Execute the full first‑principles workflow described in the steps below and compute the thermoelectric figure of merit ZT of γ‑graphyne at 600 K for (i) p‑type doping along the x‑direction and (ii) n‑type doping along the y‑direction. Write the two ZT values to a JSON file at `/app/outputs/zt_results.json`.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org
- EPW (electron‑phonon Wannier) code: https://epw-code.org
- ShengBTE: https://www.shengbte.org
- Norm‑conserving pseudopotential for carbon (PBE): https://www.quantum-espresso.org/pseudopotentials
- γ‑graphyne primitive cell crystal structure

## Workflow steps

### Step 1: DFT geometry optimization and electronic structure
- Role: process
- Action: Perform DFT geometry relaxation of the γ‑graphyne primitive cell (12 atoms) using Quantum ESPRESSO with norm‑conserving PBE pseudopotentials, a wavefunction cutoff of 80 Ry, a charge density cutoff of 800 Ry, and a 14 Å vacuum layer. Obtain the relaxed lattice constants, atomic positions, band energies, and group velocities.
- Evidence: `/app/outputs/optimized_geometry.json`

### Step 2: DFPT phonons and coarse electron–phonon coupling
- Role: process
- Action: Using the relaxed structure, run density‑functional perturbation theory (DFPT) on a coarse k/q mesh to compute phonon frequencies and electron–phonon coupling matrix elements. Verify dynamical stability (no imaginary modes).
- Evidence: `/app/outputs/phonon_coarse.json`

### Step 3: Wannier interpolation with EPW
- Role: process
- Action: Use the EPW code (maximally localized Wannier functions) to interpolate the coarse electron–phonon coupling, electronic bands, and phonon dispersion to a dense mesh.
- Evidence: `/app/outputs/epw_interpolation.log`

### Step 4: Relaxation time calculation
- Role: process
- Action: From the dense electron–phonon coupling matrix elements, compute the electron self‑energy and evaluate the carrier relaxation times τₙₖ using (τₙₖ)⁻¹ = 2 Im(Σₙₖ)/ħ.
- Evidence: `/app/outputs/relaxation_times.csv`

### Step 5: Electronic transport coefficients
- Role: process
- Action: Combine the band energies, group velocities, and relaxation times to solve the Boltzmann transport equations for electrons and holes, yielding the Seebeck coefficient S, electrical conductivity σ, and electronic thermal conductivity κₑ (via the Wiedemann–Franz law with computed Lorenz number) at 600 K.
- Evidence: `/app/outputs/transport_coefficients.csv`

### Step 6: Phonon thermal conductivity via ShengBTE
- Role: process
- Action: Construct a supercell from the relaxed primitive cell, compute second‑ and third‑order interatomic force constants, and use ShengBTE to solve the phonon Boltzmann transport equation to obtain the lattice thermal conductivity κ_ph at 600 K.
- Evidence: `/app/outputs/kappa_ph.json`

### Step 7: ZT evaluation
- Role: scored (load-bearing)
- Action: Compute the thermoelectric figure of merit ZT = S²σT / (κₑ + κ_ph) at 600 K for p‑type doping along the x‑direction and n‑type doping along the y‑direction, using the transport coefficients obtained in previous steps. Write the two values to zt_results.json.
- Output file: `/app/outputs/zt_results.json`
- Format: json
- Contract: {"ZT_x_p_600K": <float>, "ZT_y_n_600K": <float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/zt_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### zt_results.json
- path: `/app/outputs/zt_results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Thermoelectric figure of merit ZT at 600 K for γ‑graphyne: p‑type (x‑direction) and n‑type (y‑direction).
- schema:
  - `type`: object
  - `required`:
    - `ZT_x_p_600K`: number
    - `ZT_y_n_600K`: number

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "zt_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "ZT_x_p_600K": "number",
          "ZT_y_n_600K": "number"
        }
      },
      "description": "Thermoelectric figure of merit ZT at 600 K for γ‑graphyne: p‑type (x‑direction) and n‑type (y‑direction)."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier inspects `/app/outputs/zt_results.json` and compares your submitted ZT values against expected thresholds. The reward is continuous on a 0 – 1 scale: values that meet or exceed the expected performance earn full credit, while lower values receive proportionally less. The verifier may also check that the required intermediate evidence files (listed in each workflow step) are present to confirm that the computational pipeline was genuinely executed; missing evidence can result in a reduced or zero score. You must obtain the ZT values by running the described workflow — simply reporting a pre‑computed number without the pipeline will not receive credit.

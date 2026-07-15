# GAP potential training and thermal conductivity of crystalline and amorphous silicon

## Problem background
Predicting thermal conductivity of complex and disordered materials from first principles is challenging due to the prohibitive computational cost of capturing disordered structures and the frequent breakdown of the phonon quasiparticle picture. Machine learning interatomic potentials offer a promising route to combine ab-initio accuracy with the length and time scales accessible to molecular dynamics (MD). This work develops Gaussian approximation potentials (GAP) for crystalline silicon (c‑Si) and amorphous silicon (a‑Si) using efficient stochastic sampling of the potential energy surface, and uses equilibrium molecular dynamics with those potentials to obtain the room‑temperature thermal conductivity of both phases.

## Approach
The core idea is to train two separate GAP models — one for c‑Si and one for a‑Si — and then use them in equilibrium MD to extract the thermal conductivity via the Green‑Kubo formula. For c‑Si, harmonic lattice dynamics (DFT) provides normal‑mode eigenvectors used to stochastically generate uncorrelated atomic snapshots that sample the thermally accessible configurational space. DFT single‑point calculations on those snapshots produce a training database of energies and forces; a GAP with SOAP descriptors is regressed on that database using the hyperparameters specified in the workflow. For a‑Si, an initial amorphous network is created by a melt‑quench simulation with an empirical potential, relaxed with DFT, and then refined through an iterative training loop: trial eigenvectors from the empirical potential are used to generate snapshots, DFT targets are computed, a GAP is trained, new eigenvectors are obtained from the GAP, and the loop repeats until energy convergence and dynamical stability are achieved. Finally, both trained potentials are deployed in LAMMPS for equilibrium MD at 300 K, where the heat‑flux autocorrelation is integrated over long correlation times and averaged over multiple independent runs to yield the thermal conductivity of each phase.

## Reproduction target
The objective is to compute the room‑temperature thermal conductivity (in W/mK) of crystalline silicon and amorphous silicon using the Gaussian approximation potentials trained by the stochastic snapshot sampling workflow. The final result must be written to `/app/outputs/thermal_conductivity.csv`, containing one row per phase (phase identifier 'c‑Si' or 'a‑Si') and the corresponding thermal conductivity value ('kappa'). The computation is performed with equilibrium molecular dynamics at 300 K: after NPT equilibration, the heat flux is sampled every 5 fs in the NVE ensemble, the Green‑Kubo autocorrelation function is integrated up to 200 ps for c‑Si and 40 ps for a‑Si, and the reported conductivity is the average over 10 independent runs with different initial velocity distributions.

## Assets

- QUIP (GAP) package: https://github.com/libAtoms/QUIP
- LAMMPS: https://lammps.sandia.gov
- Phonopy: https://phonopy.github.io/phonopy/
- Quantum ESPRESSO: https://www.quantum-espresso.org
- Stillinger-Weber potential parameters for Si: https://lammps.sandia.gov/doc/2001/pair_sw.html
- Silicon pseudopotential (PBE): https://pseudopotentials.quantum-espresso.org/upf_files/Si.pbe-n-rrkjus_psl.1.0.0.UPF

## Workflow steps

### Step 1: Compute harmonic lattice dynamics for c-Si
- Role: process
- Action: Using an open-source DFT code (e.g., Quantum ESPRESSO) and Phonopy, perform finite-displacement calculations on a supercell of crystalline silicon (diamond structure). Solve the dynamical equation to obtain normal-mode frequencies and eigenvectors.
- Evidence: `/app/outputs/cSi_eigenvectors.json`

### Step 2: Generate stochastic training snapshots for c-Si
- Role: process
- Action: Using the eigenvectors from step_01 and the displacement formula (random uncorrelated atomic displacements based on normal-mode amplitudes), generate 100 uncorrelated atomic snapshots at 300 K and 100 at 600 K. Output configurations in an extended XYZ or similar format.
- Evidence: `/app/outputs/cSi_snapshots.xyz`

### Step 3: Compute DFT energies and forces for c-Si snapshots
- Role: process
- Action: For each snapshot from step_02, run a self-consistent field DFT calculation using the PBE functional and a plane-wave cutoff of at least 350 eV to obtain total energies and atomic forces. Collect results into a training database file.
- Evidence: `/app/outputs/cSi_training_db.json`

### Step 4: Train GAP model for crystalline silicon
- Role: process
- Action: Using the QUIP/GAP framework with SOAP descriptors and the hyperparameters from the paper (r_cut=4.5 Å, d=0.5 Å, σ_v(energy)=0.0001 eV/atom, σ_v(forces)=0.001 eV/Å, σ_w=1.0 eV, σ_a=0.5 Å, ζ=4, n_max=12, l_max=12), train a Gaussian approximation potential on the database from step_03. Output the trained potential file.
- Evidence: `/app/outputs/cSi_gap.xml`

### Step 5: Generate initial amorphous silicon structure via melt-quench MD
- Role: process
- Action: Using LAMMPS with the Stillinger-Weber potential, perform a melt-quench MD simulation on a 216-atom c-Si supercell: heat to 3000 K, quench to 1 K, and hold at low temperature. Output the final amorphous structure.
- Evidence: `/app/outputs/aSi_initial.xyz`

### Step 6: DFT relaxation of the a-Si structure
- Role: process
- Action: Relax the amorphous structure from step_05 using conjugate-gradient DFT optimization (open-source DFT) until atomic forces fall below 10⁻⁶ eV/Å. Output the relaxed configuration.
- Evidence: `/app/outputs/aSi_relaxed.xyz`

### Step 7: Iterative GAP training loop for amorphous silicon
- Role: process
- Action: Starting with trial eigenvectors from the SW potential on the relaxed structure, perform three iterations: (i) generate 50 random snapshots using the displacement formula with current eigenvectors, (ii) compute DFT energies/forces, (iii) train a GAP with the same SOAP hyperparameters as for c-Si, (iv) recompute eigenvectors from the GAP model. Stop when energy change per atom falls below 2×10⁻³ eV/atom and soft modes disappear. Output the final a-Si GAP model.
- Evidence: `/app/outputs/aSi_gap.xml`

### Step 8: Compute thermal conductivity via equilibrium MD
- Role: scored (load-bearing)
- Action: For c-Si (using the GAP from step_04) and a-Si (using the GAP from step_07), run equilibrium MD in LAMMPS: first NPT equilibration at 300 K for 400 ps (time step 0.5 fs); then switch to NVE and sample heat flux every 5 fs. Integrate the Green-Kubo autocorrelation function up to 200 ps for c-Si and 40 ps for a-Si. Average the thermal conductivity over 10 independent runs with different initial velocity distributions. Write the results to thermal_conductivity.csv with columns 'phase' (c-Si, a-Si) and 'kappa' (thermal conductivity in W/mK).
- Output file: `/app/outputs/thermal_conductivity.csv`
- Format: csv
- Contract: Two columns: 'phase' (string, 'c-Si' or 'a-Si') and 'kappa' (float, thermal conductivity in W/mK). One row per phase.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermal_conductivity.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermal_conductivity.csv
- path: `/app/outputs/thermal_conductivity.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Thermal conductivity of crystalline silicon (c-Si) and amorphous silicon (a-Si) at room temperature, computed by equilibrium molecular dynamics using trained GAP potentials.
- schema:
  - `type`: table
  - `required_columns`: `phase`, `kappa`
  - `units`:
    - `kappa`: W/mK

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermal_conductivity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "phase",
          "kappa"
        ],
        "units": {
          "kappa": "W/mK"
        }
      },
      "description": "Thermal conductivity of crystalline silicon (c-Si) and amorphous silicon (a-Si) at room temperature, computed by equilibrium molecular dynamics using trained GAP potentials."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier inspects your submitted artifacts under `/app/outputs`. Each scored step (including the final `thermal_conductivity.csv`) is checked for format correctness and the verifier compares your reported values against a hidden reference using an appropriate tolerance. The overall reward is a weighted sum of the scores from all scored stages. Executing the required process steps is necessary to produce correct downstream outputs, but only the scored artifacts contribute to the final reward; intermediate evidence files are not directly scored. The reward is determined solely by the verifier's evaluation of your submitted output files.

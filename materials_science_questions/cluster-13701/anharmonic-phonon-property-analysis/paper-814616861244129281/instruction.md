# Reproducing temperature-dependent lattice dynamics and thermal resistivity using the TDEP method

## Problem background
Lead telluride (PbTe) is a reference high-performance thermoelectric material. Its exceptionally low lattice thermal conductivity arises from strong anharmonic effects in phonon vibrations. Understanding how these anharmonic interactions renormalize phonon frequencies and lifetimes, and how they govern the temperature dependence of thermal transport, is central to rational design of improved thermoelectrics. This task addresses the challenge of computing the full anharmonic lattice dynamics of PbTe and deriving the resulting lattice thermal resistivity.

## Approach
The approach uses the temperature-dependent effective potential (TDEP) method.  
1. **Harmonic reference**: Compute interatomic force constants (IFCs) at T = 0 K from density functional theory (DFT) on the rock-salt structure using the AM05 exchange-correlation functional.  
2. **Force sampling**: Run *ab initio* molecular dynamics (AIMD) simulations at 300 K and 600 K for a 5×5×5 supercell to sample the potential energy surface. Recalculate forces on a subset of uncorrelated snapshots with higher accuracy.  
3. **TDEP fitting**: Extract temperature-dependent IFCs (up to third order) from these forces.  
4. **Phonon properties**: From the TDEP IFCs compute temperature-dependent harmonic frequencies and the third-order anharmonic self-energies (shifts and linewidths) on a dense q‑grid.  
5. **Derived observables**:   
   - Determine the anharmonic renormalized energy of the transverse optical (TO) mode at Γ at 300 K and 600 K.  
   - Calculate the inelastic neutron scattering (INS) cross‑section along the Γ–X direction at those temperatures.  
   - Solve the linearized phonon Boltzmann transport equation beyond the relaxation-time approximation, including isotope scattering, to obtain the lattice thermal resistivity from 100 K to 800 K.  
All DFT steps use Quantum ESPRESSO with publicly available pseudopotentials; TDEP and phono3py handle the effective potential extraction and transport solution.

## Reproduction target
Produce the following computed results:  
- **Phonon dispersion at 0 K** along the path Γ‑X‑W‑L‑Γ (frequencies per mode).  
- **TO mode energy at Γ** at 300 K and 600 K: harmonic frequency, anharmonic renormalized frequency, and the experimental reference value for comparison.  
- **INS cross‑section along Γ‑X at 300 K**: intensity as a function of energy transfer for each mode.  
- **INS cross‑section along Γ‑X at 600 K**: same format.  
- **Lattice thermal resistivity** from 100 K to 800 K in steps of 50 K.  
All outputs are CSV files written to `/app/outputs` with the exact column specifications given in the workflow steps.

## Assets

- Quantum ESPRESSO (DFT code): https://www.quantum-espresso.org/download
- TDEP (temperature-dependent effective potential code): https://github.com/hellman/tdep
- phono3py (Boltzmann transport solver for thermal conductivity): https://github.com/atztogo/phono3py
- PseudoDojo pseudopotentials (Pb and Te): http://www.pseudo-dojo.org/
- Python scientific stack (ASE, numpy, scipy): ase numpy scipy

## Workflow steps

### Step 1: T=0 harmonic interatomic force constants
- Role: process
- Action: Perform density functional theory (DFT) calculations on the PbTe rock-salt structure at equilibrium volume (6.462 Å) using Quantum ESPRESSO with PseudoDojo pseudopotentials and the AM05 exchange-correlation functional to obtain the harmonic interatomic force constants (IFCs).
- Evidence: none

### Step 2: 0 K phonon dispersion
- Role: scored
- Action: Compute the phonon dispersion from the harmonic IFCs along the path Γ–X–W–L–Γ and output the frequencies for each mode.
- Output file: `/app/outputs/step_01_phonon_dispersion_0K.csv`
- Format: csv
- Contract: Columns: q_point_label (string), mode_index (int), frequency_meV (float).
- Scoring: scored by hidden verifier

### Step 3: AIMD simulation for force sampling
- Role: process
- Action: Run Born-Oppenheimer ab initio molecular dynamics (AIMD) for a 5×5×5 supercell (250 atoms) of PbTe at 300 K and 600 K using Quantum ESPRESSO with the AM05 functional. Use Γ‑only k‑point grid, 250 eV plane‑wave cutoff, 1 fs time step. Equilibrate and run at least 30 ps of production dynamics in the canonical ensemble (Nosé thermostat). Store atomic positions and forces.
- Evidence: none

### Step 4: High‑accuracy force recalculations
- Role: process
- Action: Select a subset of uncorrelated AIMD snapshots and recalculate the forces with a 3×3×3 k‑point grid and a 300 eV cutoff to obtain accurate forces for the TDEP fit.
- Evidence: none

### Step 5: TDEP fitting of temperature‑dependent IFCs
- Role: process
- Action: Use the TDEP package to fit temperature‑dependent interatomic force constants (up to third order) from the high‑accuracy forces and corresponding atomic positions.
- Evidence: none

### Step 6: Compute TDEP harmonic phonon frequencies
- Role: process
- Action: Using the fitted temperature‑dependent IFCs, compute the harmonic phonon frequencies ω_qs(T) for the relevant temperatures (300 K, 600 K) on a dense q‑grid.
- Evidence: none

### Step 7: Compute anharmonic phonon self‑energies
- Role: process
- Action: From the TDEP IFCs, calculate the third‑order phonon self‑energies Δ_qs(Ω) and Γ_qs(Ω) by evaluating the perturbative integrals on a 31×31×31 q‑grid with a 0.1 meV Gaussian smearing.
- Evidence: none

### Step 8: TO mode energy vs. temperature
- Role: scored (load-bearing)
- Action: For the transverse optical (TO) mode at Γ, determine the anharmonic renormalized energy from the peak of the spectral function at 300 K and 600 K. Provide also the harmonic frequency (from T=0 IFCs) and the experimental reference for comparison.
- Output file: `/app/outputs/step_02_TO_energy_vs_T.csv`
- Format: csv
- Contract: Columns: temperature_K (int), harmonic_frequency_meV (float), anharmonic_renormalized_frequency_meV (float), experimental_frequency_meV (float).
- Scoring: scored by hidden verifier

### Step 9: INS cross‑section at 300 K
- Role: scored (load-bearing)
- Action: Calculate the inelastic neutron scattering (INS) cross‑section along the Γ–X direction at 300 K using the TDEP phonon frequencies and self‑energies. Output intensity as a function of energy transfer for each mode.
- Output file: `/app/outputs/step_03_INS_cross_300K.csv`
- Format: csv
- Contract: Columns: q_fractional (float), mode_label (string), energy_transfer_meV (float), intensity_arb (float).
- Scoring: scored by hidden verifier

### Step 10: INS cross‑section at 600 K
- Role: scored (load-bearing)
- Action: Calculate the INS cross‑section along the Γ–X direction at 600 K, analogous to the 300 K step.
- Output file: `/app/outputs/step_04_INS_cross_600K.csv`
- Format: csv
- Contract: Columns: q_fractional (float), mode_label (string), energy_transfer_meV (float), intensity_arb (float).
- Scoring: scored by hidden verifier

### Step 11: Lattice thermal resistivity
- Role: scored (load-bearing)
- Action: Solve the linearized phonon Boltzmann transport equation beyond the relaxation‑time approximation using the TDEP IFCs and self‑energies. Include isotope scattering. Compute the lattice thermal resistivity for temperatures from 100 K to 800 K in steps of 50 K.
- Output file: `/app/outputs/step_05_thermal_resistivity.csv`
- Format: csv
- Contract: Columns: temperature_K (float), resistivity_mK_per_W (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_phonon_dispersion_0K.csv`
- `/app/outputs/step_02_TO_energy_vs_T.csv`
- `/app/outputs/step_03_INS_cross_300K.csv`
- `/app/outputs/step_04_INS_cross_600K.csv`
- `/app/outputs/step_05_thermal_resistivity.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_phonon_dispersion_0K.csv
- path: `/app/outputs/step_01_phonon_dispersion_0K.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Phonon dispersion at T=0 K along high-symmetry path Γ-X-W-L-Γ.
- schema:
  - `type`: table
  - `required_columns`: `q_point_label`, `mode_index`, `frequency_meV`
  - `units`:
    - `frequency_meV`: meV

### step_02_TO_energy_vs_T.csv
- path: `/app/outputs/step_02_TO_energy_vs_T.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: TO mode energy at Γ for 300 K and 600 K, compared to experiment.
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `harmonic_frequency_meV`, `anharmonic_renormalized_frequency_meV`, `experimental_frequency_meV`
  - `units`:
    - `temperature_K`: K
    - `harmonic_frequency_meV`: meV
    - `anharmonic_renormalized_frequency_meV`: meV
    - `experimental_frequency_meV`: meV

### step_03_INS_cross_300K.csv
- path: `/app/outputs/step_03_INS_cross_300K.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: INS scattering cross-section along Γ-X at 300 K.
- schema:
  - `type`: table
  - `required_columns`: `q_fractional`, `mode_label`, `energy_transfer_meV`, `intensity_arb`
  - `units`:
    - `q_fractional`: 
    - `energy_transfer_meV`: meV
    - `intensity_arb`: arbitrary

### step_04_INS_cross_600K.csv
- path: `/app/outputs/step_04_INS_cross_600K.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: INS scattering cross-section along Γ-X at 600 K.
- schema:
  - `type`: table
  - `required_columns`: `q_fractional`, `mode_label`, `energy_transfer_meV`, `intensity_arb`
  - `units`:
    - `q_fractional`: 
    - `energy_transfer_meV`: meV
    - `intensity_arb`: arbitrary

### step_05_thermal_resistivity.csv
- path: `/app/outputs/step_05_thermal_resistivity.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Lattice thermal resistivity from 100 K to 800 K.
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `resistivity_mK_per_W`
  - `units`:
    - `temperature_K`: K
    - `resistivity_mK_per_W`: m K/W

Notes: All scored outputs are compared to hidden reference data from the paper's figures and tables.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_phonon_dispersion_0K.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "q_point_label",
          "mode_index",
          "frequency_meV"
        ],
        "units": {
          "frequency_meV": "meV"
        }
      },
      "description": "Phonon dispersion at T=0 K along high-symmetry path Γ-X-W-L-Γ."
    },
    {
      "file": "step_02_TO_energy_vs_T.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "harmonic_frequency_meV",
          "anharmonic_renormalized_frequency_meV",
          "experimental_frequency_meV"
        ],
        "units": {
          "temperature_K": "K",
          "harmonic_frequency_meV": "meV",
          "anharmonic_renormalized_frequency_meV": "meV",
          "experimental_frequency_meV": "meV"
        }
      },
      "description": "TO mode energy at Γ for 300 K and 600 K, compared to experiment."
    },
    {
      "file": "step_03_INS_cross_300K.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "q_fractional",
          "mode_label",
          "energy_transfer_meV",
          "intensity_arb"
        ],
        "units": {
          "q_fractional": "",
          "energy_transfer_meV": "meV",
          "intensity_arb": "arbitrary"
        }
      },
      "description": "INS scattering cross-section along Γ-X at 300 K."
    },
    {
      "file": "step_04_INS_cross_600K.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "q_fractional",
          "mode_label",
          "energy_transfer_meV",
          "intensity_arb"
        ],
        "units": {
          "q_fractional": "",
          "energy_transfer_meV": "meV",
          "intensity_arb": "arbitrary"
        }
      },
      "description": "INS scattering cross-section along Γ-X at 600 K."
    },
    {
      "file": "step_05_thermal_resistivity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "resistivity_mK_per_W"
        ],
        "units": {
          "temperature_K": "K",
          "resistivity_mK_per_W": "m K/W"
        }
      },
      "description": "Lattice thermal resistivity from 100 K to 800 K."
    }
  ],
  "notes": "All scored outputs are compared to hidden reference data from the paper's figures and tables."
}
```

## How you are scored
A hidden verifier independently inspects each scored output file. The verifier compares your computed values (phonon frequencies, TO mode energies, INS intensities, thermal resistivity) against reference data, assigning a score per file based on agreement. The per‑file scores are combined into a final reward in [0, 1]. You must faithfully execute the described computational pipeline to produce the required artifacts; simply reporting a memorized number will not suffice.

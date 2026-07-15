# DFT Formation Energies and Bulk Moduli of MgSi and AlMgSi Alloy Precipitates

## Problem background
Al–Mg–Si alloys derive their high strength from nanoscale precipitates that form during age hardening. The thermodynamic stability of these Mg–Si and Al–Mg–Si precipitate phases governs which structures appear and how they evolve through the precipitation sequence. A quantitative understanding of the relative formation energies, bulk moduli, and electronic structure of the precipitate phases is therefore crucial for guiding alloy design and processing. First-principles density‑functional theory (DFT) provides a direct route to compute these quantities without empirical fitting.

## Approach
We adopt a DFT total-energy approach using the GGA‑PBE exchange‑correlation functional. Elemental reference energies are obtained for hcp Mg, diamond‑cubic Si, and fcc Al. Static total energies are then computed for the precipitate phases: β (fluorite Mg₂Si), β″ (base‑centered monoclinic), U1 (trigonal), and U2 (orthorhombic), using experimental lattice parameters and the relaxed atomic positions supplied in the workflow steps. From these total energies, formation energies per atom are derived. Bulk moduli are obtained by fitting the Birch–Murnaghan equation of state to a series of total-energy calculations at varying volumes. For the β phase, the band structure is computed and the direct band gap at the Γ point extracted. The workflow uses open‑source DFT codes and standard pseudopotentials to ensure reproducibility.

## Reproduction target
Using DFT with the GGA‑PBE functional, compute the formation energies (mRy/atom) of the β, β″, U1, and U2 precipitate phases, their bulk moduli (GPa), and the direct band gap at Γ (eV) for the β phase. To obtain the formation energies, first calculate the per‑atom total energies of hcp Mg, diamond‑cubic Si, and fcc Al, and the total energy per unit cell of each compound at the geometries specified in the workflow steps. Then derive formation energy per atom as (E_compound − Σ x_i · E_ref_i)/N_atoms, where x_i is the element's stoichiometric count in the unit cell and N_atoms the total atom count. Bulk moduli are determined from at least five volume‑variation total‑energy points fitted to a Birch–Murnaghan equation of state. The band gap is extracted from a band‑structure calculation for β. All required output is assembled in the scored JSON file; the verifier will recompute the formation energies from the submitted raw total energies and compare all quantities to hidden reference values.

## Assets

- DFT code with GGA-PBE functional (e.g., Quantum ESPRESSO): https://www.quantum-espresso.org
- GGA-PBE Pseudopotentials for Mg, Si, Al: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Compute elemental reference energies
- Role: process
- Action: Perform DFT total energy calculations for hcp Mg, diamond-cubic Si, and fcc Al using the GGA-PBE functional. Extract the ground-state total energy per atom.
- Evidence: none

### Step 2: Compute compound total energies
- Role: process
- Action: Perform static DFT total energy calculations for the β phase (fluorite Mg₂Si, space group Fm3̄m, a=6.39 Å), β″ phase (base-centered monoclinic C2/m, a=15.16 Å, b=6.74 Å, c=4.05 Å, γ=105.3°, with relaxed fractional coordinates for inequivalent atoms from paper Table I: Mg1 (0.0, 0.0, 0.0), Mg2 (0.346, 0.071, 0.0), Mg3 (0.421, 0.063, 0.0), Si1 (0.055, 0.662, 0.0), Si2 (0.194, 0.250, 0.0), Si3 (0.209, 0.627, 0.0)), U1 phase (trigonal P3m1, a=b=4.05 Å, c=6.74 Å, fractional coordinates from paper Table II: Mg (0.0, 0.0, 0.0), Al (1/3, 2/3, 0.632), Si (1/3, 2/3, 0.243)), and U2 phase (orthorhombic Pnma, a=6.75 Å, b=4.05 Å, c=7.94 Å, fractional coordinates from paper Table III: Mg (0.034, 0.75, 0.327), Al (0.361, 0.25, 0.432), Si (0.239, 0.25, 0.120)). Record the total energy per unit cell.
- Evidence: none

### Step 3: Compute bulk moduli via equation of state
- Role: process
- Action: For each compound (β, β″, U1, U2), perform a series of total energy calculations at varying volumes (at least 5 points) and fit the Birch-Murnaghan equation of state to obtain the bulk modulus. Use the same DFT settings as for total energies.
- Evidence: none

### Step 4: Compute band gap for β phase
- Role: process
- Action: Calculate the band structure for the β phase using the same DFT settings and extract the direct band gap at the Γ point.
- Evidence: none

### Step 5: Compile final results
- Role: scored (load-bearing)
- Action: Assemble all computed quantities into a single JSON file: total energies of elemental references (eV/atom), total energies of compound phases (eV/unit cell), bulk moduli (GPa), and the direct band gap at Γ for β (eV).
- Output file: `/app/outputs/step_01_results.json`
- Format: json
- Contract: {"total_energies": {"Mg_hcp": float (eV/atom), "Si_diamond": float (eV/atom), "Al_fcc": float (eV/atom), "beta_phase": float (eV/unit cell), "beta_prime_prime_phase": float (eV/unit cell), "U1_phase": float (eV/unit cell), "U2_phase": float (eV/unit cell)}, "bulk_moduli": {"beta_phase": float (GPa), "beta_prime_prime_phase": float (GPa), "U1_phase": float (GPa), "U2_phase": float (GPa)}, "band_gap_beta": float (eV)}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_results.json
- path: `/app/outputs/step_01_results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Compiler of DFT outputs: raw total energies of elemental references and precipitate phases, fitted bulk moduli, and direct band gap at Γ for β. The checker recomputes formation energies per atom from these total energies and compares all quantities to hidden reference values.
- schema:
  - `type`: object
  - `required`:
    - `total_energies`: object with keys: Mg_hcp (eV/atom), Si_diamond (eV/atom), Al_fcc (eV/atom), beta_phase (eV/unit cell), beta_prime_prime_phase (eV/unit cell), U1_phase (eV/unit cell), U2_phase (eV/unit cell)
    - `bulk_moduli`: object with keys: beta_phase (GPa), beta_prime_prime_phase (GPa), U1_phase (GPa), U2_phase (GPa)
    - `band_gap_beta`: number (eV)

Notes: The scoring logic recomputes formation energies using the submitted total energies and compares each to the paper value; bulk moduli and band gap are compared directly. All comparisons use appropriate tolerances that respect toolchain spread.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "total_energies": "object with keys: Mg_hcp (eV/atom), Si_diamond (eV/atom), Al_fcc (eV/atom), beta_phase (eV/unit cell), beta_prime_prime_phase (eV/unit cell), U1_phase (eV/unit cell), U2_phase (eV/unit cell)",
          "bulk_moduli": "object with keys: beta_phase (GPa), beta_prime_prime_phase (GPa), U1_phase (GPa), U2_phase (GPa)",
          "band_gap_beta": "number (eV)"
        }
      },
      "description": "Compiler of DFT outputs: raw total energies of elemental references and precipitate phases, fitted bulk moduli, and direct band gap at Γ for β. The checker recomputes formation energies per atom from these total energies and compares all quantities to hidden reference values."
    }
  ],
  "notes": "The scoring logic recomputes formation energies using the submitted total energies and compares each to the paper value; bulk moduli and band gap are compared directly. All comparisons use appropriate tolerances that respect toolchain spread."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that reads the output file `step_01_results.json`. The verifier recomputes the formation energies per atom from the raw total energies you supply and compares each derived quantity (formation energies, bulk moduli, band gap) to pre‑established reference values. Comparison tolerances account for the typical spread between different DFT implementations and pseudopotential sets. The reward awarded for each reproduced quantity reflects how close your computed values are to the references; larger deviations reduce the score. The overall reward is a weighted combination of the scores for all quantities in the output file. Simply reporting a number without performing the required DFT calculations will not yield a passing reward because the verifier checks internal consistency and evaluates the derived numbers against a hidden target.

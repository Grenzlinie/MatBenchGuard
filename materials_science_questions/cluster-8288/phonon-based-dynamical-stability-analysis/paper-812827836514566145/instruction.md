# Phase stability, electronic structure, and lithium diffusion in Li2S2 from first principles

## Problem background
Lithium-sulfur (Li-S) batteries have high theoretical capacity, but their discharge mechanism involves intermediate polysulfide species, including lithium disulfide (Li₂S₂). Understanding the structural, electronic, and transport properties of Li₂S₂ is important for evaluating its role in battery performance. This work examines a high-pressure monoclinic phase of Li₂S₂ (space group P2₁/c) predicted by first-principles structure searching. The target is to compute its phase stability relative to the known tetragonal P4₂/mnm phase, its dynamical stability, electronic band gap, electrochemical discharge voltage, and lithium-ion diffusion characteristics — quantities that inform whether this phase could act as an intermediate product during battery operation.

## Approach
The procedure uses density functional theory (DFT) with the Perdew–Burke–Ernzerhof (PBE) functional and projector-augmented wave (PAW) pseudopotentials as implemented in Quantum ESPRESSO. 
- The phase transition pressure is located by calculating the enthalpy of both the P2₁/c and P4₂/mnm phases at several pressures in the 0–10 GPa range, relaxing cell shape and atomic positions.
- Dynamical stability is assessed through phonon dispersion, computed with the finite-displacement method using Phonopy.
- Electronic band gaps are extracted from band-structure calculations at the PBE level and with the screened hybrid functional HSE06.
- The discharge voltage for the reaction \(2\mathrm{Li}^+ + 2e^- + \mathrm{Li_2S_2} \rightarrow 2\mathrm{Li_2S}\) is derived from the total energies of P2₁/c Li₂S₂, body-centred-cubic Li metal, and antifluorite Li₂S.
- Lithium migration paths are studied with the climbing-image nudged elastic band (CI-NEB) method implemented in the Atomic Simulation Environment (ASE); migration energy barriers and hopping distances are obtained for six candidate hops.
All raw data and final derived quantities are assembled in a single results.json file.

## Reproduction target
Produce `/app/outputs/results.json` containing:
1. The interpolated phase-transition pressure (GPa) where the enthalpy of P2₁/c becomes lower than that of P4₂/mnm.
2. The phonon band structure and a boolean indicating whether the P2₁/c phase is dynamically stable (no imaginary frequencies).
3. The fundamental electronic band gap from a PBE calculation and from an HSE06 calculation (both in eV).
4. The discharge voltage (V) for the reaction \(2\mathrm{Li}^+ + 2e^- + \mathrm{Li_2S_2} \rightarrow 2\mathrm{Li_2S}\), computed from the total energies of the three materials.
5. For each of the six lithium diffusion paths: the migration barrier (eV), the hopping distance (Å), and the corresponding diffusion coefficient at 300 K (cm² s⁻¹), using \(D = d^2 \nu_0 \exp(-E_a/(k_B T))\) with \(\nu_0 = 10^{13}\) s⁻¹.
All intermediate raw data (enthalpy points, phonon frequencies, band energies, total energies, NEB path energies) must be included so that the derived quantities can be independently verified.

## Assets

- Structure prediction code (e.g., CALYPSO, USPEX, or AIRSS) for global optimisation of crystal structures with DFT.
- Structure of bcc lithium metal
- Structure of antifluorite Li2S
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PHONOPY: https://phonopy.github.io/phonopy/
- ASE (Atomic Simulation Environment): https://gitlab.com/ase/ase
- Pseudopotentials for Li and S: https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: Structure prediction of Li₂S₂
- Role: process
- Action: Using a global structure prediction method (e.g., CALYPSO, USPEX, or random structure searching) at pressures covering the 0–10 GPa range, generate candidate crystal structures for Li₂S₂, relax them with DFT (Quantum ESPRESSO), and identify the ground-state phases. Record all stable structures encountered, including the tetragonal P4₂/mnm phase if present, and any other phases that appear stable in this pressure range. For each stable phase, record its lattice parameters and Wyckoff positions. (The final determination of which phase is stable at a given pressure will be done from enthalpy data in a later step.)
- Evidence: `/app/outputs/structure_prediction_outcome.json`

### Step 2: Enthalpy vs pressure for Li₂S₂ phases
- Role: process
- Action: Perform DFT total-energy calculations for the monoclinic P2₁/c and tetragonal P4₂/mnm phases of Li₂S₂ at several pressures covering 0–10 GPa. For each pressure, relax the cell shape/volume and atomic positions, then record the total energy (enthalpy).
- Evidence: `/app/outputs/enthalpy_data.csv`

### Step 3: Phonon dispersion of P2₁/c structure
- Role: process
- Action: Generate supercells of the P2₁/c structure, compute forces via finite-displacement DFT calculations, and use Phonopy to obtain the phonon band structure. Output the dispersion data.
- Evidence: `/app/outputs/phonon_bands.csv`

### Step 4: Electronic band structure and band gaps
- Role: process
- Action: On the relaxed P2₁/c structure, run DFT non-self-consistent calculations to obtain the band structure. Perform both a GGA (PBE) and a hybrid functional (HSE06) calculation. Record the direct or indirect band gap values.
- Evidence: `/app/outputs/band_gaps_raw.json`

### Step 5: Energy calculations for discharge voltage
- Role: process
- Action: Compute DFT total energies of the relaxed P2₁/c Li₂S₂, body‑centred‑cubic Li metal, and antifluorite Li₂S. Store the energies in a file.
- Evidence: `/app/outputs/voltage_energies.json`

### Step 6: CI-NEB for six lithium diffusion paths
- Role: process
- Action: Identify six Li‑ion hops in the P2₁/c lattice. For each path, relax initial and final states, insert intermediate images, and run climbing‑image NEB calculations to extract the migration energy barrier and hopping distance.
- Evidence: `/app/outputs/neb_results.json`

### Step 7: Compile final results
- Role: scored (load-bearing)
- Action: From the intermediate outputs, determine the phase transition pressure by interpolating the enthalpy curves. Verify dynamical stability by confirming no phonon mode has an imaginary frequency. Compute the discharge voltage as V = [E(Li₂S₂) + E(Li) – 2E(Li₂S)] / 2e. For each diffusion path, calculate the diffusion coefficient D = d² ν₀ exp(–Ea/(k_B T)) with ν₀ = 10¹³ s⁻¹ and T = 300 K. Assemble all raw data and final quantities according to the output contract, including the discovered P2₁/c structure parameters.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: Aggregated results containing both raw data and the reproduced headline quantities.
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
- target_policy: reference_match
- description: Master result file containing the raw inputs and derived quantities for the paper’s main claims on phase transition, dynamical stability, band gaps, discharge voltage, and lithium diffusion. Also includes the discovered P2₁/c structure details.
- schema:
  - `type`: object
  - `required`:
    - `enthalpy_data`: array of objects with keys P (float, GPa), H_P21c (float, eV/f.u.), H_P42m (float, eV/f.u.)
    - `transition_pressure_GPa`: float, phase transition pressure where enthalpy curves cross
    - `phonon_band_data`: array of objects with keys q (array of floats) and frequency_cm1 (array of floats)
    - `phonon_stable`: bool, true if no imaginary frequencies within [-10,0] cm⁻¹
    - `pbe_bandgap_eV`: float, fundamental band gap from GGA-PBE calculation
    - `hse06_bandgap_eV`: float, band gap from HSE06 hybrid functional calculation
    - `voltage_V`: float, discharge voltage for the reaction 2Li⁺ + 2e⁻ + Li₂S₂ → 2Li₂S
    - `diffusion_paths`: array of objects with keys path_id (string), barrier_eV (float), hopping_distance_A (float), D_cm2_per_s (float)
    - `raw_energies`: object with keys E_Li2S2_eV (float), E_Li_eV (float), E_Li2S_eV (float)
    - `P21c_structure`: object containing keys: a (float), b (float), c (float), beta (float), sites (array of objects with atom (string), wyckoff (string), x (float), y (float), z (float))

Notes: The checker will recompute certain quantities (phase transition, phonon stability) from the raw data in this file and compare the reported values to hidden reference values from the literature. The newly added P21c_structure key is required to verify that the structure prediction step was correctly executed.

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
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "enthalpy_data": "array of objects with keys P (float, GPa), H_P21c (float, eV/f.u.), H_P42m (float, eV/f.u.)",
          "transition_pressure_GPa": "float, phase transition pressure where enthalpy curves cross",
          "phonon_band_data": "array of objects with keys q (array of floats) and frequency_cm1 (array of floats)",
          "phonon_stable": "bool, true if no imaginary frequencies within [-10,0] cm⁻¹",
          "pbe_bandgap_eV": "float, fundamental band gap from GGA-PBE calculation",
          "hse06_bandgap_eV": "float, band gap from HSE06 hybrid functional calculation",
          "voltage_V": "float, discharge voltage for the reaction 2Li⁺ + 2e⁻ + Li₂S₂ → 2Li₂S",
          "diffusion_paths": "array of objects with keys path_id (string), barrier_eV (float), hopping_distance_A (float), D_cm2_per_s (float)",
          "raw_energies": "object with keys E_Li2S2_eV (float), E_Li_eV (float), E_Li2S_eV (float)",
          "P21c_structure": "object containing keys: a (float), b (float), c (float), beta (float), sites (array of objects with atom (string), wyckoff (string), x (float), y (float), z (float))"
        }
      },
      "description": "Master result file containing the raw inputs and derived quantities for the paper’s main claims on phase transition, dynamical stability, band gaps, discharge voltage, and lithium diffusion. Also includes the discovered P2₁/c structure details."
    }
  ],
  "notes": "The checker will recompute certain quantities (phase transition, phonon stability) from the raw data in this file and compare the reported values to hidden reference values from the literature. The newly added P21c_structure key is required to verify that the structure prediction step was correctly executed."
}
```

## How you are scored
After your run, a hidden verifier will read `results.json`. It will inspect the raw data for consistency and then compare the derived quantities (transition pressure, phonon stability, band gaps, voltage, and diffusion barriers/coefficients) against reference values obtained from the paper’s own calculations. Each of these scored aspects contributes a weighted fraction to a final reward between 0 and 1. The verification also checks that the reported numbers are traceable to the raw data you include. A submission that provides only final numbers without supporting raw data, or that does not follow from the prescribed workflow steps, will receive a low score. The exact tolerances are not disclosed, but they are set to accommodate modest implementation-dependent differences while penalising results that are substantially incorrect.

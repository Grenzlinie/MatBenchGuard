# First-Principles Analysis of Lattice Instabilities in Metallic 2D Transition Metal Dichalcogenides

## Problem background
Metallic transition metal dichalcogenides in the 1T polymorph exhibit periodic lattice distortions whose mechanism remains a subject of debate. Two competing pictures exist: a weak‑coupling scenario based on Fermi‑surface nesting of the conduction electrons, and a strong‑coupling picture rooted in real‑space chemical bonding among the transition‑metal atoms. The filling of the t₂g subshell controls which of these mechanisms is dominant, leading to a possible crossover between the two regimes. This task investigates this crossover by performing first‑principles calculations for two representative monolayer disulfides with different t₂g occupancies: TaS₂ (t₂g¹) and WS₂ (t₂g²).

## Approach
The workflow uses density functional theory (DFT) within the generalized gradient approximation (PBE) and norm‑conserving pseudopotentials. For both monolayer 1T‑TaS₂ and 1T‑WS₂ you will:

1. Compute the electronic band structure of the undistorted 1T phase.
2. Evaluate the bare static susceptibility χ₀(q) along the Γ–M direction within the constant‑matrix‑element approximation, for the undoped case and for one hole‑doping level that rigidly shifts the Fermi energy.
3. Calculate the phonon dispersion along Γ–M using density‑functional perturbation theory (DFPT), monitoring the lowest acoustic phonon branch to identify soft modes.
4. For WS₂, construct a 2×1 supercell and relax the structure to the 1T′ distorted phase, recording the total energy gain and the shortened W–W bond distance.
5. Build maximally localized Wannier functions (MLWFs) for the t₂g manifold of both the 1T and 1T′ phases of WS₂, and extract the on‑site energies to obtain the bonding–antibonding t₂g splitting as well as the half‑bandwidth of the t₂g bands in the undistorted 1T phase.

The computed quantities are intended to reveal whether the lattice instability in each material is better described by nesting (sensitivity of the soft‑mode wave vector to doping and a correspondence with the susceptibility peak) or by strong Wannier‑function bonding (a large distortion energy, bond shortening, and t₂g level splitting exceeding the band width).

## Reproduction target
Produce a single JSON file, `/app/outputs/results.json`, containing the following ten numerical quantities obtained from your first‑principles calculations:

* `TaS2_q_ICDW_undoped` – incommensurate wave‑vector (units of b) that maximizes the bare susceptibility of undoped 1T‑TaS₂.
* `TaS2_q_ICDW_hole_doped` – same wave‑vector for hole‑doped TaS₂ at exactly 0.20 holes per formula unit (achieved by rigidly shifting the Fermi level by –0.20 eV).
* `TaS2_susceptibility_peak_value` – height of the bare‑susceptibility peak (arbitrary units) of undoped TaS₂.
* `TaS2_ph_d_phonon_freq_at_qICDW` – frequency (cm⁻¹) of the lowest acoustic phonon mode at the incommensurate wave‑vector for undoped TaS₂.
* `WS2_energy_gain` – total energy lowering (eV per formula unit) upon relaxation from 1T to the 1T′ phase of WS₂.
* `WS2_shortened_WW_distance` – shortest W–W distance (Å) in the relaxed 1T′ structure.
* `WS2_bonding_antibonding_splitting` – energy splitting (eV) between bonding and antibonding t₂g Wannier functions in the 1T′ phase.
* `WS2_half_bandwidth` – half‑bandwidth W/2 (eV) of the t₂g manifold in the undistorted 1T phase of WS₂.
* `WS2_susceptibility_at_M_point` – value of the bare susceptibility of undoped WS₂ at the M point.
* `WS2_ph_d_phonon_freq_at_M` – frequency (cm⁻¹) of the lowest acoustic phonon mode of undoped WS₂ at the M point.

All values must be floating‑point numbers expressed with at least three significant figures.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Wannier90: https://wannier.org/
- SG15 ONCV pseudopotentials: http://www.quantum-simulation.org/potentials/sg15_oncv/
- Crystal structures of monolayer 1T-TaS₂ and 1T-WS₂

## Workflow steps

### Step 1: DFT band‑structure calculation for undistorted 1T monolayers
- Role: process
- Action: Perform self‑consistent field (SCF) and non‑self‑consistent field (NSCF) band‑structure calculations using density functional theory (DFT) with the PBE functional and SG15 ONCV pseudopotentials for monolayer 1T‑TaS₂ and 1T‑WS₂. Save Kohn‑Sham eigenvalues and wavefunctions on a fine k‑point grid along high‑symmetry directions.
- Evidence: `/app/outputs/band_calc.log`

### Step 2: Bare static susceptibility calculation
- Role: process
- Action: Using the band energies from the previous DFT step, compute the bare static susceptibility χ₀(q) along the Γ–M direction in the constant‑matrix‑element approximation for undoped and hole‑doped TaS₂ and WS₂. Identify the incommensurate CDW wave vector as the position of the maximum for TaS₂, and record the susceptibility value at the M point for WS₂.
- Evidence: `/app/outputs/susceptibility_q.dat`

### Step 3: DFPT phonon dispersion calculation
- Role: process
- Action: Compute the phonon dispersion along Γ–M for the undistorted 1T monolayers of TaS₂ and WS₂ using density‑functional perturbation theory (DFPT) with Quantum ESPRESSO’s PHonon module, for undoped and hole‑doped cases. Record the lowest acoustic phonon frequency at the relevant wave vectors (incommensurate q for TaS₂ and at the M point for WS₂).
- Evidence: `/app/outputs/phonon_dispersion.dat`

### Step 4: Structural relaxation of the 1T′ phase of WS₂
- Role: process
- Action: Construct a 2×1 supercell of monolayer 1T‑WS₂ and perform a full DFT structural relaxation (PBE functional, SG15 ONCV pseudopotentials) to obtain the 1T′ distorted structure. Record the total energy gain per formula unit and extract the shortened W–W bond distance.
- Evidence: `/app/outputs/relax_1Tprime.out`

### Step 5: Maximally localized Wannier function construction for WS₂
- Role: process
- Action: Using the DFT wavefunctions from the undistorted 1T and relaxed 1T′ phases of WS₂, construct maximally localized Wannier functions (MLWFs) for the t₂g manifold with Wannier90. From the on‑site energies, extract the bonding–antibonding t₂g energy splitting, and compute the half‑bandwidth (W/2) of the t₂g manifold in the undistorted 1T phase.
- Evidence: `/app/outputs/wannier_energies.txt`

### Step 6: Collect all required numerical results
- Role: scored (load-bearing)
- Action: Extract the following ten quantities from the outputs of the preceding steps and write them into /app/outputs/results.json: TaS2_q_ICDW_undoped, TaS2_q_ICDW_hole_doped, TaS2_susceptibility_peak_value, TaS2_ph_d_phonon_freq_at_qICDW, WS2_energy_gain, WS2_shortened_WW_distance, WS2_bonding_antibonding_splitting, WS2_half_bandwidth, WS2_susceptibility_at_M_point, WS2_ph_d_phonon_freq_at_M. All values must be reported as floating‑point numbers with at least three significant figures.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with keys: TaS2_q_ICDW_undoped (number, units: b), TaS2_q_ICDW_hole_doped (number, units: b), TaS2_susceptibility_peak_value (number), TaS2_ph_d_phonon_freq_at_qICDW (number, units: cm⁻¹), WS2_energy_gain (number, units: eV), WS2_shortened_WW_distance (number, units: Å), WS2_bonding_antibonding_splitting (number, units: eV), WS2_half_bandwidth (number, units: eV), WS2_susceptibility_at_M_point (number), WS2_ph_d_phonon_freq_at_M (number, units: cm⁻¹).
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
- target_policy: exact_match
- description: JSON file containing the ten computed physical quantities that constitute the reproduction target; each field is a floating‑point number with appropriate physical units as specified.
- schema:
  - `type`: object
  - `required`: `TaS2_q_ICDW_undoped`, `TaS2_q_ICDW_hole_doped`, `TaS2_susceptibility_peak_value`, `TaS2_ph_d_phonon_freq_at_qICDW`, `WS2_energy_gain`, `WS2_shortened_WW_distance`, `WS2_bonding_antibonding_splitting`, `WS2_half_bandwidth`, `WS2_susceptibility_at_M_point`, `WS2_ph_d_phonon_freq_at_M`
  - `properties`:
    - `TaS2_q_ICDW_undoped`:
      - `type`: number
      - `units`: b
    - `TaS2_q_ICDW_hole_doped`:
      - `type`: number
      - `units`: b
    - `TaS2_susceptibility_peak_value`:
      - `type`: number
    - `TaS2_ph_d_phonon_freq_at_qICDW`:
      - `type`: number
      - `units`: cm⁻¹
    - `WS2_energy_gain`:
      - `type`: number
      - `units`: eV
    - `WS2_shortened_WW_distance`:
      - `type`: number
      - `units`: Å
    - `WS2_bonding_antibonding_splitting`:
      - `type`: number
      - `units`: eV
    - `WS2_half_bandwidth`:
      - `type`: number
      - `units`: eV
    - `WS2_susceptibility_at_M_point`:
      - `type`: number
    - `WS2_ph_d_phonon_freq_at_M`:
      - `type`: number
      - `units`: cm⁻¹

Notes: The hidden checker compares each value in results.json to the paper‑reported gold value using tolerances appropriate for the re‑run method (e.g., ±0.01 Å for distances, ±0.05 eV for energies, ±0.01 b for wave‑vectors, ±5 cm⁻¹ for phonon frequencies). Partial credit is proportional to the fraction of passing fields.

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
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "TaS2_q_ICDW_undoped",
          "TaS2_q_ICDW_hole_doped",
          "TaS2_susceptibility_peak_value",
          "TaS2_ph_d_phonon_freq_at_qICDW",
          "WS2_energy_gain",
          "WS2_shortened_WW_distance",
          "WS2_bonding_antibonding_splitting",
          "WS2_half_bandwidth",
          "WS2_susceptibility_at_M_point",
          "WS2_ph_d_phonon_freq_at_M"
        ],
        "properties": {
          "TaS2_q_ICDW_undoped": {
            "type": "number",
            "units": "b"
          },
          "TaS2_q_ICDW_hole_doped": {
            "type": "number",
            "units": "b"
          },
          "TaS2_susceptibility_peak_value": {
            "type": "number"
          },
          "TaS2_ph_d_phonon_freq_at_qICDW": {
            "type": "number",
            "units": "cm⁻¹"
          },
          "WS2_energy_gain": {
            "type": "number",
            "units": "eV"
          },
          "WS2_shortened_WW_distance": {
            "type": "number",
            "units": "Å"
          },
          "WS2_bonding_antibonding_splitting": {
            "type": "number",
            "units": "eV"
          },
          "WS2_half_bandwidth": {
            "type": "number",
            "units": "eV"
          },
          "WS2_susceptibility_at_M_point": {
            "type": "number"
          },
          "WS2_ph_d_phonon_freq_at_M": {
            "type": "number",
            "units": "cm⁻¹"
          }
        }
      },
      "description": "JSON file containing the ten computed physical quantities that constitute the reproduction target; each field is a floating‑point number with appropriate physical units as specified."
    }
  ],
  "notes": "The hidden checker compares each value in results.json to the paper‑reported gold value using tolerances appropriate for the re‑run method (e.g., ±0.01 Å for distances, ±0.05 eV for energies, ±0.01 b for wave‑vectors, ±5 cm⁻¹ for phonon frequencies). Partial credit is proportional to the fraction of passing fields."
}
```

## How you are scored
A hidden verifier reads your `/app/outputs/results.json` and compares each of the ten quantities to reference values obtained from the original work. Each field that lies within a pre‑defined tolerance earns credit. The tolerance accounts for the spread expected from legitimate differences in computational setup (choice of pseudopotentials, k‑point sampling, convergence criteria, etc.). Your final reward is the fraction of fields that pass, so a complete and accurate first‑principles reproduction will score highly even if small numerical differences arise from the toolchain. No credit is given for merely reporting numbers; the verifier checks that your computed values are physically plausible reconstructions of the target quantities.

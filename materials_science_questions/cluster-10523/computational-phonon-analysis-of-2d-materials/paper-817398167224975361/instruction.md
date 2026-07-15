# Computational investigation of energy difference and phonon modes in pristine and tungsten-doped vanadium dioxide

## Problem background
Vanadium dioxide (VO2) is a prototypical phase-change material that undergoes a reversible insulator-to-metal transition coupled with a structural transformation from monoclinic (M1) to rutile (R). Substitutional doping with tungsten (W) is known to alter the transition temperature and modify the lattice dynamics, but the precise microscopic mechanisms by which W doping affects the energy landscape and vibrational properties remain an active area of investigation. This task reproduces the density functional theory (DFT) calculations that quantify how W substitution changes the total energy differences between the M1 and R phases, shifts the estimated transition temperature, and introduces new phonon modes, serving as a benchmark for understanding doping-driven electronic and lattice dynamics in phase-change materials.

## Approach
The reproduction uses first-principles density functional theory (DFT) calculations. The computational workflow starts from the monoclinic (M1) and rutile (R) crystal structures of pristine VO2, obtained from public crystallographic databases. For W doping, a supercell with approximately 3 at.% W (WV31O64) is constructed by substituting one V atom with W in a 96-atom cell. DFT relaxations and total-energy calculations are performed within the generalized gradient approximation including a Hubbard U correction (GGA+U, with U = 4.0 eV and J = 0.7 eV) and using PAW pseudopotentials. The total energy differences between the M1 and R phases per formula unit are extracted for both pristine and doped systems. The phase-transition temperature for the doped system, T_c1, is estimated from the energy differences by assuming equal entropy change across the transition, using the experimental pristine transition temperature of 340 K as baseline: T_c1 = 340 × (ΔE_doped / ΔE_pristine). The reduction of transition temperature per atomic percent of W is then calculated as (340 − T_c1) / 3. Gamma-point phonon frequencies are computed via a finite-displacement method for larger supercells of the monoclinic phase, both pristine and W-doped, to reveal the effect of doping on the lattice vibrations.

## Reproduction target
Run the DFT workflow to produce a single scored artifact: the file `dft_results.json`. This file must contain the following quantities computed from the DFT results: (1) the total energy difference (in meV) between the monoclinic and rutile phases for pristine VO2; (2) the same energy difference for W-doped VO2; (3) the estimated phase-transition temperature for the doped system using the relation T_c1 = 340 × (ΔE_doped / ΔE_pristine) K; (4) the transition-temperature reduction per at.% W, computed as (340 − T_c1)/3; and (5) a list of phonon mode frequencies (in THz) at the Γ point, with descriptive labels for pristine and doped VO2, capturing the softening of a V–V mode and the appearance of new W–V modes.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotential library: https://www.materialscloud.org/discover/sssp/table/efficiency
- VO2 crystal structures
- Phonopy: https://phonopy.github.io/phonopy/

## Workflow steps

### Step 1: Construct pristine VO2 crystal structures
- Role: process
- Action: Build the monoclinic (M1) and rutile (R) unit cells of pristine VO2 using known crystallographic parameters from the literature. Use a double unit cell for the rutile phase to match the size of the M1 cell for consistent energy comparisons.
- Evidence: none

### Step 2: DFT relaxation and total energy of pristine VO2
- Role: process
- Action: Perform GGA+U DFT relaxations and self‑consistent total energy calculations for pristine M1 and R phases using an open‑source DFT code (e.g., Quantum ESPRESSO). Use PBE‑type functionals with Hubbard U and J parameters, PAW pseudopotentials, an appropriate plane‑wave cutoff and k‑point mesh, and converge forces on all atoms. Save the final total energies of the relaxed structures.
- Evidence: `/app/outputs/pristine_total_energies.json`

### Step 3: Construct W‑doped VO2 supercell
- Role: process
- Action: Build a 96‑atom supercell of formula WV₃₁O₆₄ (approximately 3 at.% W) for both M1 and R phases by substituting one V atom with W in the pristine unit cells.
- Evidence: none

### Step 4: DFT relaxation and total energy of W‑doped VO2
- Role: process
- Action: Perform GGA+U DFT relaxations and total energy calculations for the WV₃₁O₆₄ supercells in both M1 and R phases, using the same computational parameters as for pristine VO2. Save the final total energies.
- Evidence: `/app/outputs/doped_total_energies.json`

### Step 5: Construct supercells for phonon calculations
- Role: process
- Action: Build 3×3×3 supercells of the monoclinic M1 phase for pristine (V₁₀₈O₂₁₆) and W‑doped (WV₁₀₇O₂₁₆, ≈0.9 at.%) systems.
- Evidence: none

### Step 6: Relax phonon supercells
- Role: process
- Action: Relax the atomic positions of the 3×3×3 pristine and W‑doped M1 supercells using the same DFT settings as earlier.
- Evidence: none

### Step 7: Compute Γ‑point phonon frequencies – pristine VO2
- Role: process
- Action: Perform a Γ‑point phonon calculation on the relaxed pristine 3×3×3 supercell using the finite‑displacement method or DFPT. Extract all phonon frequencies.
- Evidence: `/app/outputs/pristine_phonon_frequencies.json`

### Step 8: Compute Γ‑point phonon frequencies – W‑doped VO2
- Role: process
- Action: Perform a Γ‑point phonon calculation on the relaxed W‑doped 3×3×3 supercell using the same method. Extract all phonon frequencies.
- Evidence: `/app/outputs/doped_phonon_frequencies.json`

### Step 9: Compile final DFT results
- Role: scored (load-bearing)
- Action: Read the total energies from pristine_total_energies.json and doped_total_energies.json, and the phonon frequencies from pristine_phonon_frequencies.json and doped_phonon_frequencies.json. Compute the total energy differences per formula unit: pristine ΔE₀ (M1 energy minus R energy) and doped ΔE₁. Estimate the transition temperature T_c1 = 340 × (ΔE₁ / ΔE₀) K, using the experimental pristine transition temperature of 340 K. Compute the reduction per at.% W as (340 − T_c1) / 3. Collect the phonon frequencies into lists with descriptive labels. Write all quantities into dft_results.json.
- Output file: `/app/outputs/dft_results.json`
- Format: json
- Contract: {"pristine_energy_diff_meV": number, "doped_energy_diff_meV": number, "estimated_Tc_K": number, "reduction_per_at_percent_K": number, "phonon_modes": [{"frequency_THz": number, "description": string}, ...]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dft_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dft_results.json
- path: `/app/outputs/dft_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Contains the computed total energy difference between M1 and R phases for pristine VO2 (meV) and W‑doped VO2 (meV), the estimated transition temperature (K), the reduction per at.% W (K/at.%), and a list of phonon mode frequencies (THz) with text descriptions for both pristine and doped systems. The hidden checker compares each numerical value to a reference within a tolerance and verifies that certain phonon frequency ranges are present.
- schema:
  - `type`: object
  - `required`:
    - `pristine_energy_diff_meV`: number
    - `doped_energy_diff_meV`: number
    - `estimated_Tc_K`: number
    - `reduction_per_at_percent_K`: number
    - `phonon_modes`: array

Notes: The agent must compute these values from first‑principles DFT using an open‑source code. The reference values are the paper’s reported numbers; the checker will compare the agent’s results to those references with appropriate tolerances. The phonon mode structural check ensures that softening of the ~6 THz mode and new modes near 4 THz are captured.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dft_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "pristine_energy_diff_meV": "number",
          "doped_energy_diff_meV": "number",
          "estimated_Tc_K": "number",
          "reduction_per_at_percent_K": "number",
          "phonon_modes": "array"
        }
      },
      "description": "Contains the computed total energy difference between M1 and R phases for pristine VO2 (meV) and W‑doped VO2 (meV), the estimated transition temperature (K), the reduction per at.% W (K/at.%), and a list of phonon mode frequencies (THz) with text descriptions for both pristine and doped systems. The hidden checker compares each numerical value to a reference within a tolerance and verifies that certain phonon frequency ranges are present."
    }
  ],
  "notes": "The agent must compute these values from first‑principles DFT using an open‑source code. The reference values are the paper’s reported numbers; the checker will compare the agent’s results to those references with appropriate tolerances. The phonon mode structural check ensures that softening of the ~6 THz mode and new modes near 4 THz are captured."
}
```

## How you are scored
A hidden verifier will independently inspect your output file against reference values and structural requirements. For each numerical field, the verifier compares your computed value to an expected value within an appropriate tolerance. For the phonon modes, the verifier checks that specific frequency ranges are present (e.g., a mode in the 5.5–6.5 THz range for pristine VO2 and a mode in the 3.6–4.8 THz range not present in pristine for W-doped VO2). The final score is a weighted combination of the results from all scored parts. Reporting a number that matches the paper is not enough; you must execute the DFT pipeline to derive the values.

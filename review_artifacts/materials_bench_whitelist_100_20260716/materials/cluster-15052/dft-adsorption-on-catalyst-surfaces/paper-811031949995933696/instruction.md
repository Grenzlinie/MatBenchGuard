# Density Functional Theory Study of K-Promoted Mo₂C Catalyst for CO₂ Activation

## Problem background
Potassium promotion of molybdenum carbide (Mo₂C) catalysts is experimentally known to improve CO₂ conversion. Density functional theory (DFT) can elucidate the atomic-level mechanism by comparing CO₂ adsorption and dissociation on pristine and K-promoted β‑Mo₂C(001) surfaces. This task asks you to perform plane‑wave DFT calculations to determine how the binding energies of CO₂ (in physisorbed, chemisorbed, and dissociated states), the activation barriers for CO₂ → CO + O, and the electronic charge donated by K differ between the two surfaces. The computed results constitute the reproduction target.

## Approach
You will construct a slab model of the Mo‑terminated β‑Mo₂C(001) surface, both pristine and with a single K atom placed on the top Mo layer. Using an open‑source plane‑wave DFT code together with the Atomic Simulation Environment (ASE), you will relax the clean surfaces and then optimize CO₂ in three adsorption configurations on each surface: physisorbed, chemisorbed (activated), and dissociated (CO + O). Binding energies are obtained from the relation BE = E(surface+adsorbate) – E(surface) – E(adsorbate), where adsorbate energies are computed for isolated CO₂, CO, and O. The reaction pathway for CO₂ dissociation is mapped with climbing‑image nudged elastic band (CI‑NEB) calculations to find the transition state and extract the activation barrier on each surface. Finally, a Bader charge analysis on the K‑promoted slab quantifies the charge lost by the K atom. The workflow replaces the proprietary VASP code with the GPAW DFT engine; the same PBE exchange‑correlation functional and PAW pseudopotentials are employed. The ordered steps that follow detail the full sequence of computations.

## Reproduction target
Compute, for the Mo‑terminated β‑Mo₂C(001) surface with and without a single K promoter, the following quantities (all energies in kcal mol⁻¹, charge in e):
- Binding energies of CO₂ in the physisorbed, chemisorbed, and dissociated states.
- Activation barrier for CO₂ dissociation (CO₂ → CO + O).
- Bader charge lost by the K atom.
Write the results as a JSON object to `/app/outputs/dft_results.json` with the keys specified in the output contract.

## Assets

- GPAW (grid-based projector augmented wave DFT code): https://wiki.fysik.dtu.dk/gpaw/
- Atomic Simulation Environment (ASE): ase
- Bader charge analysis code: http://theory.cm.utexas.edu/henkelman/code/bader/

## Workflow steps

### Step 1: Build and relax pristine β-Mo₂C(001) surface
- Role: process
- Action: Construct the Mo-terminated β-Mo₂C(001) slab as a 2×2 supercell (cell dimensions 10.50×12.15×14.55 Å, 4 atomic layers, 10 Å vacuum). Perform DFT geometry relaxation using PBE/PAW, 415 eV cutoff, 5×5×1 k‑points, electronic convergence 10⁻⁵ eV, force convergence 0.01 eV/Å. Keep the relaxed atomic structure and total energy.
- Evidence: none

### Step 2: Build and relax K‑promoted β-Mo₂C(001) surface
- Role: process
- Action: Starting from the optimized pristine slab, place one K atom on the top Mo layer. Relax the combined system with the same DFT parameters. Keep the relaxed structure and total energy.
- Evidence: none

### Step 3: Compute isolated molecule energies
- Role: process
- Action: Calculate the total energies of isolated CO2, CO, and O atom in an analogous computational setup (same DFT parameters, all in a large box to avoid periodic interaction).
- Evidence: none

### Step 4: Optimize CO2 adsorption states on pristine surface
- Role: process
- Action: On the relaxed pristine surface, place CO2 in physisorbed, chemisorbed (activated), and dissociated (CO + O) configurations. Optimize each geometry using the same DFT parameters and collect the total energies of the adsorbate + surface systems.
- Evidence: none

### Step 5: Optimize CO2 adsorption states on K‑promoted surface
- Role: process
- Action: Repeat the adsorbate optimizations of the three states on the relaxed K‑promoted surface with the same DFT parameters. Collect total energies.
- Evidence: none

### Step 6: CI‑NEB for CO2 dissociation on pristine surface
- Role: process
- Action: Using the physisorbed CO2 state as the initial image and the dissociated CO+O state as the final image, perform a climbing‑image nudged elastic band (CI‑NEB) calculation to locate the transition state for CO2 dissociation on the pristine surface. Extract the activation barrier and confirm the transition state has exactly one imaginary vibrational frequency.
- Evidence: none

### Step 7: CI‑NEB for CO2 dissociation on K‑promoted surface
- Role: process
- Action: Repeat the CI‑NEB calculation for CO2 dissociation using the K‑promoted surface states. Extract the activation barrier and verify the transition state.
- Evidence: none

### Step 8: Bader charge analysis on K‑promoted surface
- Role: process
- Action: Perform a Bader charge analysis on the charge density of the relaxed K‑promoted slab (without adsorbate) to determine the charge lost by the K atom (in units of e).
- Evidence: none

### Step 9: Compile final results
- Role: scored (load-bearing)
- Action: From the stored total energies, compute binding energies as BE(adsorbate) = E(surface+adsorbate) - E(surface) - E(adsorbate) for each state and each surface. Convert all energies to kcal mol⁻¹. Report the activation barriers from CI‑NEB and the K Bader charge. Write all values as a JSON object to /app/outputs/dft_results.json.
- Output file: `/app/outputs/dft_results.json`
- Format: json
- Contract: JSON object with keys: pristine_physisorbed_BE (number, kcal/mol), pristine_chemisorbed_BE, pristine_dissociated_BE, pristine_barrier, K_physisorbed_BE, K_chemisorbed_BE, K_dissociated_BE, K_barrier, K_Bader_charge (positive number, e).
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
- description: DFT-computed binding energies, activation barriers, and Bader charge for CO2 on pristine and K-promoted β-Mo2C(001) surfaces, compared to hidden paper reference values with tolerances.
- schema:
  - `type`: object
  - `required`:
    - `pristine_physisorbed_BE`: number (kcal/mol)
    - `pristine_chemisorbed_BE`: number (kcal/mol)
    - `pristine_dissociated_BE`: number (kcal/mol)
    - `pristine_barrier`: number (kcal/mol)
    - `K_physisorbed_BE`: number (kcal/mol)
    - `K_chemisorbed_BE`: number (kcal/mol)
    - `K_dissociated_BE`: number (kcal/mol)
    - `K_barrier`: number (kcal/mol)
    - `K_Bader_charge`: number (e)

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
          "pristine_physisorbed_BE": "number (kcal/mol)",
          "pristine_chemisorbed_BE": "number (kcal/mol)",
          "pristine_dissociated_BE": "number (kcal/mol)",
          "pristine_barrier": "number (kcal/mol)",
          "K_physisorbed_BE": "number (kcal/mol)",
          "K_chemisorbed_BE": "number (kcal/mol)",
          "K_dissociated_BE": "number (kcal/mol)",
          "K_barrier": "number (kcal/mol)",
          "K_Bader_charge": "number (e)"
        }
      },
      "description": "DFT-computed binding energies, activation barriers, and Bader charge for CO2 on pristine and K-promoted β-Mo2C(001) surfaces, compared to hidden paper reference values with tolerances."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier reads your `/app/outputs/dft_results.json`. It independently compares each reported quantity to expert reference values using appropriate numerical tolerances, and also verifies the relative trend that the activation barrier on the K‑promoted surface is lower than on the pristine surface. Each quantity and the trend carry a share of the total reward; reporting numbers without having run the DFT workflow is insufficient. The grading logic is entirely contained in the verifier; you do not need to know the reference values.

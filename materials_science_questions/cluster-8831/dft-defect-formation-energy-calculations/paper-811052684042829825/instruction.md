# DFT Charge Transport in Li₂S₂: Semiconducting Nature and Hole Polaron Conductivity

## Problem background
Lithium‑sulfur (Li‑S) batteries are promising for high‑capacity energy storage, but the solid discharge products that form on the cathode – particularly lithium persulfide (Li₂S₂) – exhibit poor electronic and ionic conductivity, limiting practical performance. Understanding the intrinsic charge transport mechanisms in crystalline Li₂S₂ is essential for designing strategies to mitigate surface passivation and reduce overpotentials. This task investigates whether and how charge carriers (electrons, holes, or ions) move through the p1 polymorph of Li₂S₂, by computing the electronic structure, the formation energies of native defects, the diffusion barriers for the most relevant carriers, and the resulting electrical conductivity at room temperature.

## Approach
The core idea is to use first‑principles density functional theory (DFT) to study charge transport in crystalline Li₂S₂ from a defect‑physics perspective. The workflow models the p1 Li₂S₂ crystal using hybrid‑functional (HSE06) DFT to obtain accurate band gaps, then constructs supercells to introduce native point defects (lithium vacancies, sulfur‑dimer vacancies, and polarons) and computes their formation energies under realistic chemical potentials. The diffusion of the most relevant charged defects is simulated with the climbing‑image nudged elastic band (CI‑NEB) method, and the resulting barriers are combined with the defect concentrations (from formation energies and the Boltzmann factor) and the Einstein relation to estimate the electronic and ionic conductivities at 300 K. The entire pipeline is re‑run with the open‑source plane‑wave code Quantum ESPRESSO and public pseudopotentials, so that the results can be independently reproduced and compared to the original work.

## Reproduction target
Produce the following four quantitative results, each written to its own text file under `/app/outputs`:

1. **Band gaps** (`step_01_bandgap.txt`): the band gap of pristine p1 Li₂S₂ computed with the GGA‑PBE functional (first line) and with the HSE06 hybrid functional (second line), both in eV.

2. **Defect formation energies** (`step_02_defect_formation_energies.txt`): the formation energy of the negatively charged lithium vacancy V_Li⁻ (first line) and of the hole polaron p⁺ (second line), both in eV, obtained from HSE06 total energies.

3. **p⁺ diffusion barrier** (`step_03_p_diffusion_barrier.txt`): the CI‑NEB energy barrier for a hole polaron migrating along the [001] crystallographic direction, in eV.

4. **Conductivity ratio** (`step_04_conductivity_ratio.txt`): the ratio of the electronic conductivity (due to p⁺) to the ionic conductivity (due to V_Li⁻) at T = 300 K, dimensionless.

All quantities must be derived from the p1 Li₂S₂ structure, using chemical potentials consistent with standard phase‑equilibrium references. The required computational protocol is described in the workflow steps.

## Assets

- Li₂S₂ p1 crystal structure: https://materialsproject.org/materials/mp-28552
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotentials (Li, S): https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: Fetch p1 Li₂S₂ crystal structure
- Role: process
- Action: Obtain the p1 Li₂S₂ primitive cell (e.g., from Materials Project mp-28552 or the Feng et al. CIF) and convert it to the input format required for a plane‑wave DFT code.
- Evidence: `/app/outputs/p1_structure.cif`

### Step 2: Build supercells and defect configurations
- Role: process
- Action: Generate a 3×3×2 supercell. Create initial structures for the pristine cell, neutral Li and S₂ vacancies, charged vacancies V_Li⁻, and the hole polaron p⁺ configuration with appropriate local distortions.
- Evidence: `/app/outputs/supercells.input`

### Step 3: DFT geometry optimization (HSE06)
- Role: process
- Action: Perform HSE06 geometry optimization on the pristine, neutral‑defect, and charged‑defect supercells to obtain equilibrium structures and total energies.
- Evidence: `/app/outputs/optimized_energies.txt`

### Step 4: Compute bandgaps
- Role: scored
- Action: Calculate the total density of states (DOS) for the pristine supercell with both GGA‑PBE and HSE06 functionals. Determine the bandgap from the VBM and CBM positions and write the two values (one per line) to step_01_bandgap.txt.
- Output file: `/app/outputs/step_01_bandgap.txt`
- Format: txt
- Contract: Two lines, each a floating‑point number in eV. No headers.
- Scoring: scored by hidden verifier

### Step 5: Calculate defect formation energies
- Role: scored (load-bearing)
- Action: Using the HSE06 total energies of pristine and defective supercells, together with the chemical potentials of Li and S, compute the formation energies of V_Li⁻ and p⁺. Write the two values to step_02_defect_formation_energies.txt.
- Output file: `/app/outputs/step_02_defect_formation_energies.txt`
- Format: txt
- Contract: Two lines, each a floating‑point number in eV. No headers.
- Scoring: scored by hidden verifier

### Step 6: Compute p⁺ diffusion barrier
- Role: scored (load-bearing)
- Action: Perform a climbing‑image nudged elastic band (CI‑NEB) calculation for the hole polaron p⁺ migrating along the [001] direction, using the optimized end‑point structures. Extract the energy barrier and write it to step_03_p_diffusion_barrier.txt.
- Output file: `/app/outputs/step_03_p_diffusion_barrier.txt`
- Format: txt
- Contract: Single floating‑point number in eV.
- Scoring: scored by hidden verifier

### Step 7: Estimate conductivity ratio
- Role: scored (load-bearing)
- Action: Compute the mobility of p⁺ and V_Li⁻ using the Einstein relation and the diffusion barriers. Estimate the carrier concentrations from the formation energies via the Boltzmann factor. Calculate the electronic (p⁺) and ionic (V_Li⁻) conductivities at 300 K and write their ratio to step_04_conductivity_ratio.txt.
- Output file: `/app/outputs/step_04_conductivity_ratio.txt`
- Format: txt
- Contract: Single floating‑point number (dimensionless).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_bandgap.txt`
- `/app/outputs/step_02_defect_formation_energies.txt`
- `/app/outputs/step_03_p_diffusion_barrier.txt`
- `/app/outputs/step_04_conductivity_ratio.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_bandgap.txt
- path: `/app/outputs/step_01_bandgap.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Bandgaps of pristine p1 Li₂S₂ computed with PBE and HSE06 functionals.
- schema:
  - `type`: text
  - `description`: Line 1: PBE bandgap (eV); Line 2: HSE06 bandgap (eV).

### step_02_defect_formation_energies.txt
- path: `/app/outputs/step_02_defect_formation_energies.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Formation energies of the dominant charged defects in p1 Li₂S₂.
- schema:
  - `type`: text
  - `description`: Line 1: formation energy of V_Li⁻ (eV); Line 2: formation energy of p⁺ (eV).

### step_03_p_diffusion_barrier.txt
- path: `/app/outputs/step_03_p_diffusion_barrier.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: CI-NEB energy barrier for hole polaron migration along the [001] direction.
- schema:
  - `type`: text
  - `description`: Single value: diffusion barrier of p⁺ along [001] in eV.

### step_04_conductivity_ratio.txt
- path: `/app/outputs/step_04_conductivity_ratio.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Estimated conductivity ratio at room temperature, quantifying the dominance of hole polaron transport.
- schema:
  - `type`: text
  - `description`: Single dimensionless number: ratio of electronic conductivity (p⁺) to ionic conductivity (V_Li⁻) at 300 K.

Notes: All values correspond to the p1 Li₂S₂ structure. Chemical potentials follow standard phase‑equilibrium references. Conductivity ratio uses the harmonic mean of diffusion barriers along the studied directions.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_bandgap.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "Line 1: PBE bandgap (eV); Line 2: HSE06 bandgap (eV)."
      },
      "description": "Bandgaps of pristine p1 Li₂S₂ computed with PBE and HSE06 functionals."
    },
    {
      "file": "step_02_defect_formation_energies.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "Line 1: formation energy of V_Li⁻ (eV); Line 2: formation energy of p⁺ (eV)."
      },
      "description": "Formation energies of the dominant charged defects in p1 Li₂S₂."
    },
    {
      "file": "step_03_p_diffusion_barrier.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "Single value: diffusion barrier of p⁺ along [001] in eV."
      },
      "description": "CI-NEB energy barrier for hole polaron migration along the [001] direction."
    },
    {
      "file": "step_04_conductivity_ratio.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "Single dimensionless number: ratio of electronic conductivity (p⁺) to ionic conductivity (V_Li⁻) at 300 K."
      },
      "description": "Estimated conductivity ratio at room temperature, quantifying the dominance of hole polaron transport."
    }
  ],
  "notes": "All values correspond to the p1 Li₂S₂ structure. Chemical potentials follow standard phase‑equilibrium references. Conductivity ratio uses the harmonic mean of diffusion barriers along the studied directions."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that reads only the four output files listed above. For each file the verifier compares your computed value(s) to the paper’s reference numbers (hidden gold) using tolerances that account for the typical spread between different DFT implementations. Each file contributes a fixed weight to the final score, which is a single float between 0 (all values far off) and 1 (all values within tolerance). The verifier does not inspect your intermediate steps, logs, or computational workflow; only the contents of the specified output files matter. The weights and tolerances are not disclosed.

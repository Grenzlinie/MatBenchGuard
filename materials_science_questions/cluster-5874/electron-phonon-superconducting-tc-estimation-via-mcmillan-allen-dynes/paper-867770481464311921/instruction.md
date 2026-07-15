# Electron-Phonon Superconducting Tc Estimation via McMillan-Allen-Dynes

## Problem background
Solid benzene is the simplest aromatic hydrocarbon. Potassium doping of polycyclic aromatic hydrocarbons (PAHs) induces superconductivity with reported transition temperatures up to 33 K, but the exact superconducting phase, required doping level, and underlying mechanism are unclear. This work investigates potassium-doped solid benzene K_xC_6H_6 (x = 1, 2, 3) to identify the stable phase and predict its superconducting transition temperature, establishing benzene as a minimal model system for organic superconductivity.

## Approach
We use first-principles density functional theory (DFT) within the local density approximation (LDA) to perform structural relaxations and total energy calculations of solid benzene, bulk potassium, and three potassium‑doped benzene compositions (x = 1, 2, 3). Formation energies are computed to determine the most stable doping. For the stable phase, the relaxed lattice constants and volume expansion relative to undoped benzene are extracted. Electron‑phonon coupling is then calculated with the same DFT framework to obtain the Eliashberg spectral function, the electron‑phonon coupling parameter λ, and the logarithmic average phonon frequency ω_log. Finally, the McMillan–Allen‑Dynes formula is applied to estimate the superconducting critical temperature Tc. All calculations are carried out with the open‑source Quantum ESPRESSO package using norm‑conserving pseudopotentials, replacing the proprietary VASP code used in the original study.

## Reproduction target
Using first‑principles DFT and electron‑phonon coupling calculations, determine the most stable K‑doped composition among x = 1, 2, 3 based on formation energy; for that most stable composition, compute the relaxed lattice constants (a, b, c in Å), the volume expansion percentage relative to undoped solid benzene, and the superconducting critical temperature Tc (in K) via the McMillan‑Allen‑Dynes formula with μ* = 0.10. Write each result to the corresponding scored output file.

## Assets

- Crystal structure of solid benzene (phase I, Pbca): https://www.crystallography.net/cod/9008000.html
- Crystal structure of bulk potassium (bcc): https://materialsproject.org/materials/mp-1018079/
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Pseudopotentials for C, H, K: https://www.materialscloud.org/discover/sssp

## Workflow steps

### Step 1: Optimize reference structures (solid benzene and bulk K)
- Role: process
- Action: Perform plane-wave DFT structural relaxation of solid benzene (orthorhombic Pbca) and bulk potassium (bcc) to obtain their total energies and equilibrium geometries. Use LDA functional with appropriate pseudopotentials.
- Evidence: `/app/outputs/reference_total_energies.json`

### Step 2: Construct and optimize K_xC_6H_6 structures (x=1,2,3)
- Role: process
- Action: Generate initial configurations for K-doped benzene by inserting K atoms at plausible intercalation sites into the solid benzene cell. For each composition x=1,2,3, perform structural relaxation using the same DFT settings as the reference steps. Identify the lowest-energy geometry for each stoichiometry.
- Evidence: `/app/outputs/kx_total_energies.json`

### Step 3: Formation energies and stability ordering
- Role: scored
- Action: Compute formation energies E_form = E(K_xC_6H_6) - E(C_6H_6) - x * E(K_bulk) for x=1,2,3. Write the three values (in eV) to a file.
- Output file: `/app/outputs/step_01_formation_energies.txt`
- Format: txt
- Contract: first line: <E_form_x=1> <E_form_x=2> <E_form_x=3>
- Scoring: scored by hidden verifier

### Step 4: Lattice constants of the most stable K-doped phase
- Role: scored (load-bearing)
- Action: From the optimized structure of the composition with the lowest formation energy, extract the orthorhombic lattice constants a, b, c (in Å). Write them to a file.
- Output file: `/app/outputs/step_02_lattice_constants.txt`
- Format: txt
- Contract: <a> <b> <c>
- Scoring: scored by hidden verifier

### Step 5: Volume expansion of the most stable K-doped phase
- Role: scored
- Action: Compute the volume expansion percentage of the lowest-energy K-doped phase relative to undoped solid benzene: 100 * (V_stable - V_benzene) / V_benzene. Write the result to a file.
- Output file: `/app/outputs/step_03_volume_expansion.txt`
- Format: txt
- Contract: <expansion_percent>
- Scoring: scored by hidden verifier

### Step 6: Electron-phonon coupling of the most stable K-doped phase
- Role: process
- Action: Using the optimized structure of the lowest-energy composition, perform electron-phonon coupling calculation with Quantum ESPRESSO: compute phonon frequencies and electron-phonon matrix elements on a suitable q-point mesh, then calculate the Eliashberg function, electron-phonon coupling parameter λ, and logarithmic average phonon frequency ω_log.
- Evidence: `/app/outputs/epc_lambda_omega.txt`

### Step 7: Superconducting Tc estimation
- Role: scored (load-bearing)
- Action: From the computed λ and ω_log, apply the McMillan-Allen-Dynes formula with a Coulomb pseudopotential μ* = 0.10. Write the resulting critical temperature Tc in Kelvin to a file.
- Output file: `/app/outputs/step_04_tc.txt`
- Format: txt
- Contract: <Tc_K>
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_formation_energies.txt`
- `/app/outputs/step_02_lattice_constants.txt`
- `/app/outputs/step_03_volume_expansion.txt`
- `/app/outputs/step_04_tc.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_formation_energies.txt
- path: `/app/outputs/step_01_formation_energies.txt`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Space-separated formation energies (x=1, x=2, x=3) in eV. The checker verifies that the most stable composition has the lowest formation energy and that the differences among compositions are consistent with phase stability.
- schema:
  - `type`: text
  - `units`:
    - `values`: eV

### step_02_lattice_constants.txt
- path: `/app/outputs/step_02_lattice_constants.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Three space-separated orthorhombic lattice constants a, b, c of the most stable K-doped phase in Å.
- schema:
  - `type`: text
  - `units`:
    - `values`: Å

### step_03_volume_expansion.txt
- path: `/app/outputs/step_03_volume_expansion.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Single float: volume expansion of the most stable K-doped phase relative to undoped solid benzene in percent.
- schema:
  - `type`: text
  - `units`:
    - `value`: percent

### step_04_tc.txt
- path: `/app/outputs/step_04_tc.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Superconducting critical temperature Tc of the most stable K-doped phase in Kelvin.
- schema:
  - `type`: text
  - `units`:
    - `value`: K

Notes: All scored artifacts are compared to hidden gold values/tolerances derived from the source paper. Volume expansion is cross-checked for self-consistency against submitted lattice constants where feasible.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_formation_energies.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "units": {
          "values": "eV"
        }
      },
      "description": "Space-separated formation energies (x=1, x=2, x=3) in eV. The checker verifies that the most stable composition has the lowest formation energy and that the differences among compositions are consistent with phase stability."
    },
    {
      "file": "step_02_lattice_constants.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "units": {
          "values": "Å"
        }
      },
      "description": "Three space-separated orthorhombic lattice constants a, b, c of the most stable K-doped phase in Å."
    },
    {
      "file": "step_03_volume_expansion.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "units": {
          "value": "percent"
        }
      },
      "description": "Single float: volume expansion of the most stable K-doped phase relative to undoped solid benzene in percent."
    },
    {
      "file": "step_04_tc.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "units": {
          "value": "K"
        }
      },
      "description": "Superconducting critical temperature Tc of the most stable K-doped phase in Kelvin."
    }
  ],
  "notes": "All scored artifacts are compared to hidden gold values/tolerances derived from the source paper. Volume expansion is cross-checked for self-consistency against submitted lattice constants where feasible."
}
```

## How you are scored
A hidden automated verifier reads your four scored output files. It compares each submitted value to a hidden reference (the paper’s own reported results) using appropriate tolerances that account for typical tool‑chain variation. The formation energies are checked for internal consistency: the most negative value determines the stable composition used in the subsequent steps. The lattice constants, volume expansion, and Tc are compared against the reference values with tolerance windows. The final reward is a weighted combination of these individual scores, giving full credit when your results meet or exceed the reference accuracy, and decreasing as deviations grow.

# First-Principles Electron-Phonon Coupling and Superconductivity Calculation for a Stacked Organic Radical Crystal

## Problem background
This task addresses the prediction of structural and electronic properties of a one-dimensional stacked organic radical crystal. First-principles calculations are used to investigate the inter-ring distance, electronic density of states at the Fermi level, dynamical stability, and electron-phonon coupling of a specific predicted phase. These quantities are key indicators of the material's metallicity and possible superconductivity. The goal is to reproduce these computed properties using open-source tools, given an initial crystal structure and a well-defined computational protocol.

## Approach
The workflow starts from the provided initial crystal structure. Using Quantum ESPRESSO with the PBE functional and Grimme D2 dispersion correction, a variable-cell geometry relaxation is performed to obtain the equilibrium structure. A static self-consistent field calculation followed by a density-of-states calculation extracts the DOS at the Fermi level. Dynamical stability is verified by computing phonon frequencies via density-functional perturbation theory (DFPT); the absence of imaginary modes confirms that the phase is stable. The electron-phonon coupling is then computed using the EPW code in conjunction with Wannier90. After constructing maximally localized Wannier functions, EPW interpolates the electronic and phonon properties to obtain the Eliashberg spectral function, the cumulative electron-phonon coupling constant λ, and the superconducting critical temperature Tc estimated with the McMillan-Allen-Dynes approximation (Coulomb pseudopotential μ*=0.1). Finally, the key results—inter-ring distance, DOS at EF, λ, Tc, and a dynamical stability flag—are collected into a single JSON file.

## Reproduction target
Starting from the initial crystal structure of the P6/mmm phase (provided as `/app/inputs/initial_structure.cif`), carry out the DFT and electron-phonon coupling workflow as described. Produce a JSON file `results.json` containing the following computed quantities:
- `inter_ring_distance`: shortest distance between stacked molecular planes (Å)
- `fermi_level_DOS`: electronic density of states at the Fermi level (states/eV/atom)
- `lambda`: electron-phonon coupling constant (dimensionless)
- `Tc`: superconducting critical temperature (K)
- `dynamic_stable`: boolean; true if the phonon spectrum shows no imaginary frequency modes.
The file must be written to `/app/outputs/results.json`.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/download
- EPW code: https://github.com/epw-code/epw
- Wannier90: https://github.com/wannier-developers/wannier90
- SSSP efficiency pseudopotential library: https://www.materialscloud.org/discover/sssp/table/efficiency
- Initial crystal structure (CIF): Bundled with the task at `/app/inputs/initial_structure.cif`

## Workflow steps

### Step 1: Geometry relaxation
- Role: process
- Action: Using Quantum ESPRESSO pw.x with PBE functional and Grimme D2 dispersion correction, perform a variable-cell geometry relaxation starting from the bundled CIF file at `/app/inputs/initial_structure.cif`. Ensure adequate convergence with respect to kinetic energy cutoff and k-point sampling.
- Evidence: `/app/outputs/geometry_relaxation.log`

### Step 2: Electronic density of states calculation
- Role: process
- Action: Perform a static self-consistent field (scf) calculation on the relaxed structure, then use dos.x to compute the total electronic density of states. Extract the DOS value at the Fermi level.
- Evidence: `/app/outputs/dos_output.txt`

### Step 3: Phonon dispersion and dynamical stability
- Role: process
- Action: Perform a DFPT phonon calculation with ph.x on a suitable q-grid to obtain the phonon spectrum. Verify that there are no imaginary frequency modes (i.e., the phase is dynamically stable).
- Evidence: `/app/outputs/phonon_frequencies.txt`

### Step 4: Electron-phonon coupling and superconductivity
- Role: process
- Action: Run a non-self-consistent calculation on a denser k-mesh, construct Wannier functions with Wannier90, and execute EPW to obtain the Eliashberg spectral function, cumulative λ, and the critical temperature Tc (McMillan-Allen-Dynes approximation with μ*=0.1).
- Evidence: `/app/outputs/epw_output.txt`

### Step 5: Compile final reproduction results
- Role: scored (load-bearing)
- Action: Extract from the preceding calculations: the inter-ring distance (shortest distance between stacked molecular planes, Å), the electronic DOS at the Fermi level (states/eV/atom), the electron-phonon coupling constant λ (dimensionless), the superconducting Tc (K), and a boolean dynamic_stable (true if no imaginary phonon modes). Write these five results into a JSON file.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with keys: inter_ring_distance (float, Å), fermi_level_DOS (float, states/eV/atom), lambda (float), Tc (float, K), dynamic_stable (bool).
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
- description: Final computed scalar results (inter-ring distance, DOS at Fermi level, electron-phonon coupling constant, critical temperature) and the dynamical stability flag.
- schema:
  - `type`: object
  - `required`:
    - `inter_ring_distance`: float
    - `fermi_level_DOS`: float
    - `lambda`: float
    - `Tc`: float
    - `dynamic_stable`: bool

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
        "required": {
          "inter_ring_distance": "float",
          "fermi_level_DOS": "float",
          "lambda": "float",
          "Tc": "float",
          "dynamic_stable": "bool"
        }
      },
      "description": "Final computed scalar results (inter-ring distance, DOS at Fermi level, electron-phonon coupling constant, critical temperature) and the dynamical stability flag."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier reads your `results.json` file and independently compares each numeric value and the boolean flag against expected reference values derived from the original study. The comparison uses predefined tolerances that account for the change in computational setup (different code, dispersion correction). The final reward is a weighted average of the agree-ment across the individual quantities, normalized to a float between 0 and 1. Only the final `results.json` contributes directly to the score; the intermediate log files are not graded.

# Electron-Phonon Superconducting Tc Estimation via McMillan-Allen-Dynes

## Problem background
Two-dimensional (2D) superconductors are highly desirable for both fundamental physics and applications, yet few exfoliable 2D materials are known to host robust superconductivity with high critical temperatures. Monolayer W2N3, which can be exfoliated from its van der Waals bulk parent, is a candidate material whose electron-phonon coupling properties suggest it could support a substantial superconducting critical temperature and a large superconducting gap. This task reproduces the key first-principles indicators of superconductivity in monolayer W2N3: the electron-phonon coupling constant, the superconducting critical temperature, and the gap, thereby assessing the material's potential as a high-performance 2D superconductor.

## Approach
The method relies on a hierarchy of first-principles calculations to obtain the electron-phonon coupling strength and solve the anisotropic Migdal-Eliashberg equations. Starting from the monolayer crystal structure (space group P-6m2, in-plane lattice constant a=2.864 Å), density-functional theory (DFT) with spin-orbit coupling is used to relax the lattice parameters. Phonon frequencies are then computed on a dense q-mesh using density-functional perturbation theory (DFPT), which also confirms dynamical stability. The electron-phonon coupling is calculated via Wannier interpolation with the EPW code, giving the Eliashberg spectral function α²F(ω), the cumulative coupling λ(ω), the total λ, and the logarithmic average phonon frequency ω_log. From these, the superconducting critical temperature Tc is estimated using the McMillan-Allen-Dynes formula with a Coulomb pseudopotential μ*=0.1, and independently by solving the anisotropic Migdal-Eliashberg equations, which also yield the momentum-resolved superconducting gap at low temperature.

## Reproduction target
Using the monolayer W2N3 crystal structure and full-relativistic pseudopotentials, carry out the workflow and produce the following scored artifacts:

1. **Dynamical stability**: Confirm that no imaginary phonon frequencies are present.
2. **EPC and superconducting properties**: Report the total electron-phonon coupling constant λ, the logarithmic average phonon frequency ω_log (meV), the superconducting critical temperature Tc from the McMillan-Allen-Dynes formula (using the computed λ, ω_log, and μ*=0.1), the Tc from the anisotropic Migdal-Eliashberg theory, and the superconducting gap at 6 K (meV).
3. **Eliashberg spectral function**: Provide the spectral function α²F(ω) and the cumulative λ(ω) over the full phonon energy range, enabling independent recomputation of the total λ.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- EPW: https://epw-code.org/
- Full relativistic pseudopotentials: https://www.materialscloud.org/discover/sssp/table/efficiency
- Monolayer W2N3 crystal structure

## Workflow steps

### Step 1: DFT structural relaxation
- Role: process
- Action: Using Quantum ESPRESSO with full-relativistic pseudopotentials and spin-orbit coupling, perform a variable-cell relaxation of monolayer W2N3 (space group P-6m2, a=2.864 Å) until forces < st convergence criterion. Save the relaxed structure for subsequent calculations.
- Evidence: none

### Step 2: Phonon calculation using DFPT
- Role: process
- Action: Compute phonon dispersion and density of states on a sufficiently dense q-mesh using density-functional perturbation theory (Quantum ESPRESSO ph.x). Save the phonon frequencies at all q-points to a file (e.g., 'phonon_frequencies.dat').
- Evidence: `/app/outputs/phonon_frequencies.dat`

### Step 3: EPC calculation with EPW
- Role: process
- Action: Using EPW, interpolate electron and phonon quantities onto fine k and q meshes. Compute the Eliashberg spectral function α²F(ω), cumulative EPC λ(ω), total λ, logarithmic average phonon frequency ω_log, and solve the anisotropic Migdal-Eliashberg equations to obtain momentum-resolved superconducting gap at low temperature (e.g., 6 K) and Tc from Eliashberg theory. Output the raw α²F(ω) and λ(ω) data, and the computed λ, ω_log, Tc, and gap.
- Evidence: `/app/outputs/epw_output.h5`

### Step 4: Dynamical stability check
- Role: scored
- Action: From the computed phonon frequencies, verify that no imaginary (negative) frequencies exist. Write the statement 'No imaginary frequencies found.' to step_01_phonon_stability.txt.
- Output file: `/app/outputs/step_01_phonon_stability.txt`
- Format: txt
- Contract: A plain-text file containing exactly the phrase 'No imaginary frequencies found.' (optionally followed by a newline).
- Scoring: scored by hidden verifier

### Step 5: Final EPC and superconducting properties
- Role: scored (load-bearing)
- Action: From the EPW results, extract or compute: total electron-phonon coupling constant λ, logarithmically averaged phonon frequency ω_log (meV), superconducting Tc from McMillan-Allen-Dynes formula (using λ, ω_log, and μ*=0.1), Tc from anisotropic Migdal-Eliashberg theory, and superconducting gap at 6 K. Save these in step_02_epc_properties.json.
- Output file: `/app/outputs/step_02_epc_properties.json`
- Format: json
- Contract: A JSON object with keys: 'total_EPC_lambda' (float), 'logavg_phonon_freq_omega_log' (float, meV), 'Tc_McMillan' (float, K), 'Tc_Eliashberg' (float, K), 'gap_6K' (float, meV).
- Scoring: scored by hidden verifier

### Step 6: Eliashberg spectral function data
- Role: scored
- Action: From the raw EPW output, extract or format the Eliashberg spectral function α²F(ω) and the cumulative EPC λ(ω) as a function of frequency. Write a JSON array of objects, each with 'frequency' (meV), 'a2F' (arbitrary units), and 'cumulative_lambda' (dimensionless), covering the full frequency range. Save to step_03_eliasberg_spectral_function.json.
- Output file: `/app/outputs/step_03_eliasberg_spectral_function.json`
- Format: json
- Contract: A JSON array of objects, each with numeric keys 'frequency' (meV), 'a2F' (arbitrary units), and 'cumulative_lambda' (dimensionless). The array must cover frequencies from 0 up to at least the highest phonon energy.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_phonon_stability.txt`
- `/app/outputs/step_02_epc_properties.json`
- `/app/outputs/step_03_eliasberg_spectral_function.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_phonon_stability.txt
- path: `/app/outputs/step_01_phonon_stability.txt`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Confirms that the phonon calculation produced no imaginary modes, affirming dynamical stability.
- schema:
  - `type`: text
  - `description`: Contains exactly the string 'No imaginary frequencies found.'

### step_02_epc_properties.json
- path: `/app/outputs/step_02_epc_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Aggregated superconducting properties derived from the full EPC pipeline. Checker compares to hidden paper-reported benchmarks.
- schema:
  - `type`: object
  - `required`: `total_EPC_lambda`, `logavg_phonon_freq_omega_log`, `Tc_McMillan`, `Tc_Eliashberg`, `gap_6K`
  - `units`:
    - `total_EPC_lambda`: dimensionless
    - `logavg_phonon_freq_omega_log`: meV
    - `Tc_McMillan`: K
    - `Tc_Eliashberg`: K
    - `gap_6K`: meV

### step_03_eliasberg_spectral_function.json
- path: `/app/outputs/step_03_eliasberg_spectral_function.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Eliashberg spectral function α²F(ω) and cumulative λ(ω). The checker recomputes the total EPC constant λ from this data.
- schema:
  - `type`: array
  - `items`:
    - `frequency`: float, meV
    - `a2F`: float, arbitrary units
    - `cumulative_lambda`: float, dimensionless

Notes: All scored artifacts are produced from previous process steps. The checker recomputes λ from the spectral function and compares the aggregated properties to hidden gold; tolerance accommodates reasonable method-dependent spread.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_phonon_stability.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "description": "Contains exactly the string 'No imaginary frequencies found.'"
      },
      "description": "Confirms that the phonon calculation produced no imaginary modes, affirming dynamical stability."
    },
    {
      "file": "step_02_epc_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "total_EPC_lambda",
          "logavg_phonon_freq_omega_log",
          "Tc_McMillan",
          "Tc_Eliashberg",
          "gap_6K"
        ],
        "units": {
          "total_EPC_lambda": "dimensionless",
          "logavg_phonon_freq_omega_log": "meV",
          "Tc_McMillan": "K",
          "Tc_Eliashberg": "K",
          "gap_6K": "meV"
        }
      },
      "description": "Aggregated superconducting properties derived from the full EPC pipeline. Checker compares to hidden paper-reported benchmarks."
    },
    {
      "file": "step_03_eliasberg_spectral_function.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "array",
        "items": {
          "frequency": "float, meV",
          "a2F": "float, arbitrary units",
          "cumulative_lambda": "float, dimensionless"
        }
      },
      "description": "Eliashberg spectral function α²F(ω) and cumulative λ(ω). The checker recomputes the total EPC constant λ from this data."
    }
  ],
  "notes": "All scored artifacts are produced from previous process steps. The checker recomputes λ from the spectral function and compares the aggregated properties to hidden gold; tolerance accommodates reasonable method-dependent spread."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that independently scores each of the three scored artifacts and combines their results to produce a final reward between 0 and 1. The verifier checks the stability statement for correct formatting and content. For the EPC properties, it compares your reported values for λ, ω_log, Tc, and gap against hidden reference benchmarks with appropriate tolerances; because these are directional metrics (a higher Tc or larger gap is not a worse result), meeting or exceeding the reference earns full credit, and only a result worse than reference is penalized. For the spectral function, the verifier recomputes the total λ by integrating your α²F(ω) data and compares it to a hidden reference. Merely reporting numbers without executing the required first-principles pipeline will not pass these hidden checks.

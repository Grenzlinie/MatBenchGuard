# Iodine adsorption and surface diffusion on Zr(0001) from first-principles DFT

## Problem background
Iodine-induced stress corrosion cracking (SCC) is a concern for zirconium alloy cladding in nuclear reactors. One proposed mechanism involves iodine adsorption and fast surface diffusion on zirconium, which could supply iodine to a moving crack tip and promote grain‑boundary weakening. First‑principles density‑functional calculations can quantify the thermodynamics and kinetics of this process, providing key materials properties — the dissociative adsorption energy of I₂, the coverage‑dependent chemical potential of adsorbed iodine, the resulting adsorption isotherms, and the surface diffusivity of atomic iodine on the Zr(0001) surface — that are difficult to measure separately by experiment. Your goal is to recompute these quantities from scratch using a modern DFT code and deliver them as scored output files.

## Approach
Use plane‑wave DFT with the Perdew–Burke–Ernzerhof (PBE) functional and projector‑augmented‑wave (PAW) or ultrasoft pseudopotentials to model the hexagonal Zr(0001) surface as a periodic 6‑layer slab with vacuum. The computational workflow has four main thrusts:

1. **I₂ dissociation:** Run a nudged elastic band (NEB) calculation for a di‑iodine molecule approaching the surface, dissociating, and chemisorbing as two separate iodine atoms on three‑fold hollow fcc sites. The energy profile yields the adsorption energy and reveals whether there is an activation barrier.
2. **Coverage‑dependent chemical potential:** For a set of iodine coverages (fraction of occupied fcc sites) in a suitable supercell, relax the slab with adsorbed iodine atoms and compute the electronic adsorption energy per I atom relative to half an isolated I₂ molecule and the clean surface. Fit these electronic chemical‑potential data to a polynomial in coverage and temperature.
3. **Adsorption isotherms:** Combine the fitted chemical potential of adsorbed iodine with a separately computed gas‑phase reference chemical potential (½ μ⁰ of I₂ gas, obtained by adding vibrational, rotational and translational free‑energy contributions to the DFT total energy of an isolated I₂ molecule) to calculate the standard free‑energy difference and equilibrium constant for dissociative adsorption. Use a Langmuir‑type site model for dissociative adsorption to compute the relation between iodine partial pressure and surface coverage at several temperatures.
4. **Surface diffusion:** Perform another NEB calculation for a single iodine atom hopping between adjacent three‑fold hollow (fcc and hcp) sites. Obtain the electronic energy profile and barrier, then compute the vibrational frequencies of the iodine atom at the minimum and at the saddle point. Apply Eyring’s transition‑state theory, including the site‑occupancy correction arising from the energy difference between fcc and hcp sites, to obtain the temperature‑dependent jump rate and effective diffusion coefficient. Fit the diffusion coefficient to an Arrhenius form to extract an effective activation energy and pre‑exponential factor.

All steps must be executed with an open‑source DFT code (e.g. Quantum ESPRESSO or GPAW), using the Atomic Simulation Environment (ASE) for structure building, NEB and vibrational calculations, and Python/NumPy/SciPy for fitting and isotherm generation.

## Reproduction target
You must produce the following scored output files, each containing a specific reproducible quantity:

- **dissociation_adsorption_energy.txt** — two key‑value lines: the adsorption energy (kJ mol⁻¹) for I₂ dissociation on Zr(0001) and the maximum energy barrier (kJ mol⁻¹) along the NEB path.
- **chemical_potential_coefficients.csv** — a CSV with columns “coefficient” and “value” containing the fitted coefficients c0–c6 (in kJ mol⁻¹) of the electronic chemical potential μᵢ,ads(θ,T) = c0 + c1 θ + c2 θ² + c3 θ³ + T (c4 T + c5 θ + c6).
- **isotherm_data.csv** — a CSV with columns “T(K)”, “P(bar)”, “theta” providing the computed iodine adsorption isotherms (coverage vs. iodine partial pressure) for at least three temperatures: 600 K, 800 K and 1000 K, with at least 10 points per temperature spanning the full coverage range.
- **diffusion_arrhenius_parameters.txt** — three key‑value lines: the raw electronic diffusion barrier (kJ mol⁻¹) from NEB, the effective activation energy Q (kJ mol⁻¹), and the pre‑factor D₀ (m² s⁻¹) obtained from an Arrhenius fit of the computed diffusion coefficient over 600–1000 K.

Submit all files exactly as specified under `/app/outputs`; the hidden verifier reads only these artifacts.

## Assets

- Quantum ESPRESSO or GPAW (open-source DFT): https://www.quantum-espresso.org/
- Python 3 with ASE, NumPy, SciPy: ase numpy scipy
- SSSP pseudopotential library (precision or efficiency): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Build Zr(0001) surface slab and supercells
- Role: process
- Action: Construct a periodic slab model of the hexagonal Zr(0001) surface: a 6-layer slab with a vacuum region, using bulk hcp Zr lattice parameters. Build supercells for NEB and coverage studies (e.g., a √3×√3 surface cell for coverage-dependent calculations).
- Evidence: none

### Step 2: DFT relaxation of clean Zr(0001) and isolated I₂ reference
- Role: process
- Action: Perform DFT relaxation (PBE functional) of the clean Zr(0001) slab to obtain a reference total energy. Also compute the total energy of an isolated I₂ molecule in a large cell to serve as the gas-phase energy reference.
- Evidence: none

### Step 3: NEB for I₂ dissociative adsorption
- Role: scored (load-bearing)
- Action: Run a nudged elastic band (NEB) calculation for the dissociation of an I₂ molecule on a Zr(0001) slab. Start from a physisorbed molecular state and end with two chemisorbed iodine atoms on three-fold hollow fcc sites. Extract the energy profile, determine the maximum barrier (if any) along the path, and compute the total adsorption energy (energy difference between the final adsorbed state and gas-phase I₂ molecule plus clean slab). Write two key-value lines to the output file.
- Output file: `/app/outputs/dissociation_adsorption_energy.txt`
- Format: txt
- Contract: Two lines: 'adsorption_energy (kJ/mol) = <value>' and 'max_barrier (kJ/mol) = <value>'. Both values are floating-point numbers.
- Scoring: scored by hidden verifier

### Step 4: Coverage-dependent DFT total energies
- Role: process
- Action: For iodine coverages θ = 0.11, 0.22, 0.33, 0.67, 0.89, 1.00 (fraction of occupied fcc hollow sites on a √3×√3 surface cell), compute the DFT total energy of the Zr(0001) slab with adsorbed iodine atoms, allowing surface relaxation. Determine the electronic adsorption energy per iodine atom relative to half an isolated I₂ molecule and the clean surface; these serve as the electronic chemical potential at each coverage.
- Evidence: `/app/outputs/coverage_energies.json`

### Step 5: Fit adsorbed-state chemical potential coefficients
- Role: scored
- Action: Using the coverage-dependent electronic energies from step 04, perform a polynomial least-squares fit to obtain the coefficients c0–c6 in the expression μ_I,ads(θ,T) = c0 + c1 θ + c2 θ² + c3 θ³ + T (c4 T + c5 θ + c6), where T is temperature in Kelvin. Write the fitted coefficients to the output CSV with columns 'coefficient' (e.g., 'c0') and 'value' (in kJ/mol).
- Output file: `/app/outputs/chemical_potential_coefficients.csv`
- Format: csv
- Contract: CSV with columns 'coefficient' and 'value'. The coefficient identifiers are c0, c1, c2, c3, c4, c5, c6. Values are in kJ/mol, reported as floating-point numbers.
- Scoring: scored by hidden verifier

### Step 6: Compute gas-phase reference chemical potential
- Role: process
- Action: Compute the standard chemical potential of atomic iodine in the gas phase, ½ μ⁰_{I₂,gas}(T), using DFT and statistical mechanics. Obtain the total energy of an isolated I₂ molecule, and add harmonic vibrational, rotational, and translational free energy contributions at standard pressure (1 bar). Provide a fitted polynomial in T (a quadratic) to be used in the isotherm calculation.
- Evidence: `/app/outputs/gas_phase_reference.json`

### Step 7: Compute adsorption isotherms
- Role: scored (load-bearing)
- Action: Using the fitted adsorbed chemical potential (step 05) and the gas-phase reference (step 06), calculate the standard free-energy difference ΔG⁰_I(θ,T), the equilibrium constant K = exp(-ΔG⁰_I/(RT)), and the dissociative-site coverage–pressure relation P = θ² / [K² (1−θ)²]. For temperatures 600 K, 800 K, and 1000 K, generate isotherm points (θ, P) covering the full coverage range. Write the data as CSV with columns 'T(K)', 'P(bar)', 'theta'.
- Output file: `/app/outputs/isotherm_data.csv`
- Format: csv
- Contract: CSV with columns 'T(K)', 'P(bar)', 'theta'. Provide at least 10 rows per temperature (600K, 800K, 1000K) covering the full coverage range.
- Scoring: scored by hidden verifier

### Step 8: NEB for I diffusion and vibrational analysis
- Role: process
- Action: Set up a nudged elastic band (NEB) calculation for a single iodine atom diffusing between FCC and HCP three-fold hollow sites on the relaxed Zr(0001) slab. Obtain the electronic energy profile and the energy barrier. Then compute vibrational frequencies of the iodine atom at the FCC minimum and at the saddle point using the finite-displacement method to obtain the attempt frequency and activation free energy for transition-state theory.
- Evidence: `/app/outputs/diffusion_frequencies.json`

### Step 9: Compute effective diffusion Arrhenius parameters
- Role: scored (load-bearing)
- Action: Using transition-state theory from the results of step 08, compute the jump rate and the effective diffusion coefficient D(T) across a temperature range (e.g., 600–1000 K), including the FCC/HCP site occupancy correction. Fit D(T) to an Arrhenius form D = D₀ exp(-Q/(RT)) to extract the effective activation energy Q and prefactor D₀. Also record the raw electronic energy barrier. Write three key-value lines to the output file.
- Output file: `/app/outputs/diffusion_arrhenius_parameters.txt`
- Format: txt
- Contract: Three lines: 'electronic_barrier (kJ/mol) = <value>', 'activation_energy_Q (kJ/mol) = <value>', 'prefactor_D0 (m^2/s) = <value>'. Values are floating-point numbers.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dissociation_adsorption_energy.txt`
- `/app/outputs/chemical_potential_coefficients.csv`
- `/app/outputs/isotherm_data.csv`
- `/app/outputs/diffusion_arrhenius_parameters.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dissociation_adsorption_energy.txt
- path: `/app/outputs/dissociation_adsorption_energy.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Adsorption energy of I₂ dissociation on Zr(0001) and the maximum NEB barrier.
- schema:
  - `type`: text
  - `decoding`: two key-value lines
  - `required_keys`: `adsorption_energy (kJ/mol)`, `max_barrier (kJ/mol)`
  - `units`: kJ/mol

### chemical_potential_coefficients.csv
- path: `/app/outputs/chemical_potential_coefficients.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Fitted coefficients c0–c6 for the electronic chemical potential of adsorbed iodine.
- schema:
  - `type`: table
  - `required_columns`: `coefficient`, `value`
  - `units`:
    - `value`: kJ/mol

### isotherm_data.csv
- path: `/app/outputs/isotherm_data.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed iodine adsorption isotherms: temperature, iodine partial pressure (bar), and surface coverage.
- schema:
  - `type`: table
  - `required_columns`: `T(K)`, `P(bar)`, `theta`
  - `column_types`:
    - `T(K)`: float
    - `P(bar)`: float
    - `theta`: float

### diffusion_arrhenius_parameters.txt
- path: `/app/outputs/diffusion_arrhenius_parameters.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Electronic diffusion barrier and effective Arrhenius parameters for iodine surface diffusion on Zr(0001).
- schema:
  - `type`: text
  - `decoding`: three key-value lines
  - `required_keys`: `electronic_barrier (kJ/mol)`, `activation_energy_Q (kJ/mol)`, `prefactor_D0 (m^2/s)`
  - `units`:
    - `electronic_barrier`: kJ/mol
    - `activation_energy_Q`: kJ/mol
    - `prefactor_D0`: m^2/s

Notes: All scored outputs are compared to the paper's reported values using appropriate tolerances. The agent must re-run the full computational pipeline; no pre-computed results are provided.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dissociation_adsorption_energy.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "decoding": "two key-value lines",
        "required_keys": [
          "adsorption_energy (kJ/mol)",
          "max_barrier (kJ/mol)"
        ],
        "units": "kJ/mol"
      },
      "description": "Adsorption energy of I₂ dissociation on Zr(0001) and the maximum NEB barrier."
    },
    {
      "file": "chemical_potential_coefficients.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "coefficient",
          "value"
        ],
        "units": {
          "value": "kJ/mol"
        }
      },
      "description": "Fitted coefficients c0–c6 for the electronic chemical potential of adsorbed iodine."
    },
    {
      "file": "isotherm_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T(K)",
          "P(bar)",
          "theta"
        ],
        "column_types": {
          "T(K)": "float",
          "P(bar)": "float",
          "theta": "float"
        }
      },
      "description": "Computed iodine adsorption isotherms: temperature, iodine partial pressure (bar), and surface coverage."
    },
    {
      "file": "diffusion_arrhenius_parameters.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "decoding": "three key-value lines",
        "required_keys": [
          "electronic_barrier (kJ/mol)",
          "activation_energy_Q (kJ/mol)",
          "prefactor_D0 (m^2/s)"
        ],
        "units": {
          "electronic_barrier": "kJ/mol",
          "activation_energy_Q": "kJ/mol",
          "prefactor_D0": "m^2/s"
        }
      },
      "description": "Electronic diffusion barrier and effective Arrhenius parameters for iodine surface diffusion on Zr(0001)."
    }
  ],
  "notes": "All scored outputs are compared to the paper's reported values using appropriate tolerances. The agent must re-run the full computational pipeline; no pre-computed results are provided."
}
```

## How you are scored
A hidden verifier independently scores each scored artifact (dissociation adsorption energy, chemical‑potential coefficients, isotherm data, and diffusion Arrhenius parameters) by comparing the values you report to a trusted reference obtained from the published literature. Each artifact receives a sub‑score, and the sub‑scores are combined by weight to produce the final reward (a number between 0 and 1). The comparison uses appropriate tolerances that account for the known sensitivity of DFT calculations to implementation details (e.g. pseudopotential library, k‑point sampling, energy cutoff) and for the numerical spread inherent in stochastic or iterative procedures; extreme accuracy beyond typical tool‑level variation is not expected. The verifier does not receive the paper, and you must not try to retrieve it; you must compute every quantity from first principles using the workflow described above. Delivering a qualitative description of the results or submitting numbers from the literature without performing the computations will not earn credit.

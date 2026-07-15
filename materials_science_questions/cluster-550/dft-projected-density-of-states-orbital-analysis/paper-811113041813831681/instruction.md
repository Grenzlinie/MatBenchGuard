# Reproduce Work Function of Clean and Cesiated W(001) via FLAPW Calculations

## Problem background
Lowering the work function of transition-metal surfaces by alkali-metal adsorption is important for applications such as thermionic energy conversion, ion sources, and electric propulsion. Tungsten (W) surfaces coated with cesium (Cs) are a prototypical system, but the detailed electronic mechanism behind the work function reduction has been challenging to capture with simple models. A quantitative understanding requires accurate, parameter-free electronic structure calculations that can describe the atomistic surface, the metal-adsorbate interaction, and the resulting electrostatic barrier. The goal of this task is to compute, via first-principles methods, the work function of clean W(001) and of Cs-covered W(001) as a function of the Cs–W distance, providing a numerical benchmark for the work function lowering effect.

## Approach
The work function is obtained from fully self-consistent, all-electron, full-potential linearized augmented plane wave (FLAPW) calculations. A five-layer slab model of W(001) (lattice constant a=3.161 Å) serves as the clean surface reference. A Cs c(2×2) overlayer is then added on top of the W(001) slab, and independent self-consistent calculations are performed for three different vertical separations between the Cs plane and the outermost W plane. For each system, the electronic structure is computed within density functional theory using the local density approximation and a relativistic treatment (fully relativistic core electrons, scalar-relativistic valence electrons). After convergence, the work function is extracted as the energy difference between the vacuum level and the Fermi energy. The computed work functions for the clean slab and for the three Cs/W separations constitute the primary reproducible result.

## Reproduction target
Produce a comma-separated values (CSV) file `work_function_results.csv` containing four rows, one for each system, with columns `system` (exact string identifier) and `work_function` (floating-point number in eV). The required system identifiers are: `clean_W_5layer` for the clean five-layer W(001) slab, and `Cs_W_2.6`, `Cs_W_2.75`, `Cs_W_2.9` for the Cs c(2×2)/W(001) overlayer at Cs–W plane separations of 2.6 Å, 2.75 Å, and 2.90 Å, respectively. The work function values must be obtained from fully self-consistent FLAPW calculations as described in the workflow steps.

## Assets

- Elk FLAPW code (or equivalent full-potential LAPW implementation): https://elk.sourceforge.io

## Workflow steps

### Step 1: Self-consistent FLAPW calculation for clean W(001) five-layer slab
- Role: process
- Action: Run a fully self-consistent all-electron FLAPW calculation for a five-layer bcc W(001) slab with lattice constant 3.161 Å. Use 19 irreducible k-points, approximately 2×450 LAPW basis functions per k-point for valence states, Wigner LDA exchange-correlation, fully relativistic treatment of core electrons, scalar-relativistic valence electrons, and convergence to an average potential difference <1.5 mRy. Save the self-consistent output (log, charge density, potential) for subsequent extraction of the work function.
- Evidence: `/app/outputs/clean_W_output.log`

### Step 2: Self-consistent FLAPW calculations for Cs c(2×2)/W(001) at three distances
- Role: process
- Action: For each Cs–W plane separation d = 2.6 Å, 2.75 Å, and 2.90 Å, run a fully self-consistent all-electron FLAPW calculation for a Cs c(2×2) overlayer on the same five-layer W(001) slab (12 atoms per unit cell). Use the identical computational parameters as for the clean W slab (19 irreducible k-points, ~2×450 LAPW basis functions, Wigner LDA, relativistic cores, scalar-relativistic valence, convergence to <1.5 mRy). Save the self-consistent outputs for extraction of the work function.
- Evidence: `/app/outputs/Cs_W_output.log`

### Step 3: Extract work functions and create scored CSV
- Role: scored (load-bearing)
- Action: From the self-consistent outputs of the clean W calculation and each of the three Cs/W calculations, extract the work function as the energy difference between the Fermi level and the vacuum level. Write a CSV file work_function_results.csv containing four rows with columns: system (string) and work_function (float, eV). The system identifiers must be exactly: clean_W_5layer, Cs_W_2.6, Cs_W_2.75, Cs_W_2.9.
- Output file: `/app/outputs/work_function_results.csv`
- Format: csv
- Contract: Columns: system (string, one of clean_W_5layer | Cs_W_2.6 | Cs_W_2.75 | Cs_W_2.9), work_function (float, eV)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/work_function_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### work_function_results.csv
- path: `/app/outputs/work_function_results.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Work function values for the clean W(001) five-layer slab and for Cs c(2×2)/W(001) at three Cs-W separations (2.6, 2.75, 2.90 Å). The checker compares the reported work_function values against reference results with appropriate tolerances.
- schema:
  - `type`: table
  - `required_columns`: `system`, `work_function`
  - `units`:
    - `work_function`: eV

Notes: The hidden checker performs a result-level comparison (T0) of the agent-reported work functions to the paper's calculated values, within a tolerance appropriate for different FLAPW implementations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "work_function_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "work_function"
        ],
        "units": {
          "work_function": "eV"
        }
      },
      "description": "Work function values for the clean W(001) five-layer slab and for Cs c(2×2)/W(001) at three Cs-W separations (2.6, 2.75, 2.90 Å). The checker compares the reported work_function values against reference results with appropriate tolerances."
    }
  ],
  "notes": "The hidden checker performs a result-level comparison (T0) of the agent-reported work functions to the paper's calculated values, within a tolerance appropriate for different FLAPW implementations."
}
```

## How you are scored
A hidden verifier will inspect your submitted `work_function_results.csv`. It will check that the file contains exactly four rows with the correct system identifiers and that each work function is a plausible numerical value. The verifier will then compare your reported work functions against reference results obtained from the same class of FLAPW calculations, within a tolerance that accounts for differences between implementations. A reward is assigned based on how well your computed values agree with the reference. Reporting the paper's numbers without performing the actual FLAPW calculations is not sufficient.

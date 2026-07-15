# Raman 2D peak shift model of strained graphene on Cu from DFT

## Problem background
Graphene's electronic properties can be tuned by uniform strain. When graphene is grown on a copper substrate by chemical vapor deposition (CVD), the difference in thermal expansion between graphene and copper can induce a compressive biaxial strain in the graphene layer. This work quantifies that strain through Raman spectroscopy: the shift of the 2D Raman peak is modelled using first-principles electronic structure calculations for a graphene monolayer on a Cu(111) surface. The computational challenge is to predict how the 2D peak position changes as a function of a prescribed biaxial strain, taking into account both the geometrical renormalisation of the phonon wavevector and the strain‑dependent electronic band structure.

## Approach
The 2D Raman peak originates from a double‑resonance process that depends on the electronic dispersion near the Dirac point and on the phonon dispersion along the high‑symmetry direction. The approach consists of two parts:
1. Density‑functional theory (DFT) calculations for a graphene monolayer on a Cu(111) slab (six Cu layers) under several values of biaxial strain. The electronic band structure is computed along the K–M direction. From the bands you extract, for a laser excitation of 2.412 eV, the wavevector δq of the photo‑excited electron and the valley separation KK'. These quantities are combined to obtain the phonon wavevector δk involved in the Raman process, accounting for the strain‑induced renormalisation of KK'.
2. Using the extracted δk values together with known equilibrium constants (equilibrium 2D frequency, Grüneisen parameter, and phonon band‑velocity) you evaluate the 2D Raman frequency as a function of strain according to a model that adds a linear phonon‑band‑structure term to the purely geometrical Grüneisen renormalisation. Two limit cases are examined: one that omits the band‑structure contribution (δk is held at its zero‑strain value) and one that includes it fully. The result is a set of frequencies at different strains that, when fitted linearly, yield a slope (cm⁻¹ per 1% strain) characterising the strain sensitivity of the 2D peak.

## Reproduction target
Produce a CSV file (`step_02_2D_frequencies.csv`) that contains, for at least five biaxial strain values between 0% and −1% (negative denotes compression), the computed 2D Raman peak frequency for two cases:
- Case labelled `'no_bandstructure'`: the phonon wavevector δk is equal to its equilibrium (zero‑strain) value, so the frequency shift comes only from the lattice‑Grüneisen renormalisation.
- Case labelled `'with_bandstructure'`: the phonon wavevector δk(ε) is obtained from the DFT electronic structure at the corresponding strain, thereby including the full band‑structure effect.
The CSV must contain columns: `strain` (float, in percent), `frequency` (float, in cm⁻¹), `case` (string, one of the two labels above). The verifier will read this file, perform a linear regression of frequency versus strain separately for each case, and compare the resulting slopes to the values expected from a consistent DFT‑based reproduction.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotential library: https://www.materialscloud.org/discover/sssp/table/efficiency
- Python scientific stack: numpy, pandas, scipy

## Workflow steps

### Step 1: DFT electronic structure of graphene/Cu(111) under biaxial strain
- Role: process
- Action: Perform DFT calculations for a graphene monolayer on a Cu(111) slab (6 Cu layers) using the LDA functional. Compute the electronic band structure along K–M for at least three biaxial strains (e.g., 0%, -0.5%, -1%). From the band structures, extract the electronic wavevector δq for a laser excitation energy of 2.412 eV, and determine the equilibrium KK' valley separation. Compute the phonon wavevector δk(ε) using the geometric relation δk² = (KK' + δq)² + 3δq² with KK' renormalized by (1+ε)⁻¹. Save the extracted δk(ε) and δk_eq for the next step.
- Evidence: `/app/outputs/dft_wavevectors.csv`

### Step 2: Compute Raman 2D peak frequencies and output CSV
- Role: scored (load-bearing)
- Action: Using the equilibrium 2D frequency 2678 cm⁻¹, Grüneisen parameter γ = 1.24, phonon band velocity v_iTO = 5.47×10⁻³ v_F (with v_F = 1×10⁶ m/s), compute the 2D Raman frequency ω²ᴰ(ε) for each strain ε (in percent, negative for compression) for two cases: (i) omitting the band-structure term (set δk(ε) = δk_eq) and (ii) including the full band-structure effect (using δk(ε) from DFT). Write a CSV file with columns: strain (numeric, percent), frequency (numeric, cm⁻¹), case (string: 'no_bandstructure' or 'with_bandstructure'). Include at least 5 strain points in the range 0 to -1% (inclusive).
- Output file: `/app/outputs/step_02_2D_frequencies.csv`
- Format: csv
- Contract: Columns: strain (float, percent), frequency (float, cm⁻¹), case (string: 'no_bandstructure' or 'with_bandstructure'). At least 5 strain points between 0 and -1% inclusive.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_02_2D_frequencies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_02_2D_frequencies.csv
- path: `/app/outputs/step_02_2D_frequencies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV with 2D Raman peak frequencies for two cases under biaxial strain. The checker will fit a linear function to frequency vs strain for each case, extract slopes, and compare with reference slopes within a tolerance.
- schema:
  - `type`: table
  - `required_columns`: `strain`, `frequency`, `case`
  - `units`:
    - `strain`: percent
    - `frequency`: cm⁻¹

Notes: The process step (DFT) is required but not scored; its evidence file is optional. The scored step is load-bearing because the correct δk(ε) values can only be obtained from a properly executed DFT calculation, preventing bypass.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_02_2D_frequencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain",
          "frequency",
          "case"
        ],
        "units": {
          "strain": "percent",
          "frequency": "cm⁻¹"
        }
      },
      "description": "CSV with 2D Raman peak frequencies for two cases under biaxial strain. The checker will fit a linear function to frequency vs strain for each case, extract slopes, and compare with reference slopes within a tolerance."
    }
  ],
  "notes": "The process step (DFT) is required but not scored; its evidence file is optional. The scored step is load-bearing because the correct δk(ε) values can only be obtained from a properly executed DFT calculation, preventing bypass."
}
```

## How you are scored
A hidden verifier inspects your submitted `step_02_2D_frequencies.csv`. First it checks the structural requirements: the file exists, has the correct columns and data types, and contains at least five strain points in the requested range for both cases. Then it computes separate linear regressions of frequency versus strain for the `'no_bandstructure'` and `'with_bandstructure'` cases. The resulting slopes are compared to reference slopes derived from the paper's ab initio model. The verifier also confirms that the slopes are negative and that the slope with band‑structure effect is more negative than the one without. The structural check carries a small weight; the quantitative comparison of slopes with the hidden references (with an appropriate tolerance that accounts for legitimate DFT‑code differences) constitutes the primary score. The two components are combined into a single reward between 0 and 1.

# Estimation of Relative Gibbs Free Energies from Phase Transition Data

## Problem background
The alkali fulleride RbC60 can adopt several crystalline modifications: a freely rotating face-centred cubic (fcc) phase, a polymer phase with covalently bonded chains, a dimer phase, and a hindered-rotation fcc (fccl) phase. The relative thermodynamic stability of these phases is not directly measured but can be estimated from the temperatures and enthalpies of the phase transformations, together with a reasonable assumption about the rotational heat capacity of the freely rotating fcc phase. This estimation yields a Gibbs free energy diagram that predicts which phase is the most stable at a given temperature.

## Approach
The relative Gibbs free energy of a phase with respect to the freely rotating fcc reference is expressed as ΔG = ΔH − T ΔS. The enthalpy and entropy differences at temperature T are obtained from the measured equilibrium temperature Teq and transformation enthalpy Q of the transition from that phase to the fcc phase, corrected for any specific-heat difference between the two phases.
The universal gas constant is **R = 8.314e‑3 kJ/(mol·K)** (equivalently 8.314 J/(mol·K)). The specific heat of all phases is assumed to be identical except for a rotational contribution of Crot = (3/2)R for the freely rotating fcc phase and zero for the dimer, polymer, and fccl phases. Thus, the specific heat difference when comparing to the fcc phase is **ΔCp = (3/2)R**.
The enthalpy and entropy differences are computed by integrating ΔCp from T to Teq:
  ΔH(T) = Q − ∫_T^Teq ΔCp dT
  ΔS(T) = Q/Teq − ∫_T^Teq (ΔCp / T) dT
With these, ΔG of each phase relative to fcc is evaluated over the temperature range of interest. The resulting curves are then compared to determine the temperature-dependent stability ordering.

## Reproduction target
Using the following transformation data:
  • dimer → fcc: Teq = 280 K, Q = 10.5 kJ/mol
  • fccl → fcc: Teq = 290 K, Q = 4.8 kJ/mol
  • polymer → fcc: Teq = 370 K, Q = 25.8 kJ/mol
and the heat-capacity assumption stated above, compute the relative Gibbs free energy differences ΔG of the fccl, dimer, and polymer phases with respect to the freely rotating fcc phase for temperatures T from 200 K to 500 K. Save the results as a CSV file with columns: T (temperature in K), G_fccl (kJ/mol), G_dimer (kJ/mol), G_polymer (kJ/mol). 

From these computed curves, deduce which phase has the lowest ΔG (i.e., is thermodynamically most stable) as a function of temperature. Write a concise plain-text summary indicating the stable phase(s) as temperature varies, and stating whether the dimer phase ever becomes more stable than the polymer.

## Assets

- numpy: numpy
- scipy: scipy
- pandas: pandas

## Workflow steps

### Step 1: Compute relative Gibbs free energies
- Role: scored (load-bearing)
- Action: Using the given transformation enthalpies (Q) and equilibrium temperatures (Teq) for the dimer→fcc, fccl→fcc, and polymer→fcc transitions, and the assumption that the specific heat difference ΔCp is (3/2)R when comparing to the freely rotating fcc phase and zero otherwise, compute the Gibbs free energy differences ΔG of the fccl, dimer, and polymer phases relative to the freely rotating fcc phase as a function of temperature T from 200 K to 500 K. Evaluate the thermodynamic integrals for ΔH and ΔS and write the results to gibbs_free_energies.csv.
- Output file: `/app/outputs/gibbs_free_energies.csv`
- Format: csv
- Contract: Header: T,G_fccl,G_dimer,G_polymer. Each subsequent row contains temperature in Kelvin (float) and Gibbs free energy differences in kJ/mol (float, at least 2 decimal places).
- Scoring: scored by hidden verifier

### Step 2: State phase stability ordering
- Role: scored
- Action: Analyze the computed Gibbs free energy curves to determine which phase has the lowest ΔG (i.e., is most stable) as a function of temperature. Write a concise text summary describing the temperature regimes of stability: which phase is stable at low temperatures, which phase is stable at high temperatures, and whether the dimer is ever the most stable phase relative to the polymer. Save this summary to stability_summary.txt.
- Output file: `/app/outputs/stability_summary.txt`
- Format: txt
- Contract: One or more sentences of plain text that reflect the temperature‑dependent stability ordering deduced from the computed ΔG curves.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/gibbs_free_energies.csv`
- `/app/outputs/stability_summary.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### gibbs_free_energies.csv
- path: `/app/outputs/gibbs_free_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV containing the temperature grid and the computed relative Gibbs free energies for the fccl, dimer, and polymer phases. The checker will recompute reference ΔG values at selected temperature points and compare within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `T`, `G_fccl`, `G_dimer`, `G_polymer`
  - `units`:
    - `T`: K
    - `G_fccl`: kJ/mol
    - `G_dimer`: kJ/mol
    - `G_polymer`: kJ/mol

### stability_summary.txt
- path: `/app/outputs/stability_summary.txt`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: A plain text summary of the phase stability ordering. The checker will verify that the statements are logically consistent with the submitted Gibbs free energy curves.
- schema:
  - `type`: text
  - `required`: object
  - `items`: object

Notes: All necessary numerical inputs (Q, Teq, heat capacity assumption, and R) are provided directly in the instruction. The agent must implement the thermodynamic integrals analytically or numerically. The checker will recompute ΔG at characteristic temperatures (e.g., 280, 290, 370, 400 K) using the same formulas and compare within a tolerance. The stability summary is checked for consistency with the CSV and the required qualitative ordering.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "gibbs_free_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "G_fccl",
          "G_dimer",
          "G_polymer"
        ],
        "units": {
          "T": "K",
          "G_fccl": "kJ/mol",
          "G_dimer": "kJ/mol",
          "G_polymer": "kJ/mol"
        }
      },
      "description": "CSV containing the temperature grid and the computed relative Gibbs free energies for the fccl, dimer, and polymer phases. The checker will recompute reference ΔG values at selected temperature points and compare within tolerance."
    },
    {
      "file": "stability_summary.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "required": {},
        "items": {}
      },
      "description": "A plain text summary of the phase stability ordering. The checker will verify that the statements are logically consistent with the submitted Gibbs free energy curves."
    }
  ],
  "notes": "All necessary numerical inputs (Q, Teq, heat capacity assumption, and R) are provided directly in the instruction. The agent must implement the thermodynamic integrals analytically or numerically. The checker will recompute ΔG at characteristic temperatures (e.g., 280, 290, 370, 400 K) using the same formulas and compare within a tolerance. The stability summary is checked for consistency with the CSV and the required qualitative ordering."
}
```

## How you are scored
A hidden, deterministic verifier will independently evaluate each of your submitted artifacts and combine the scores by weight into a final reward between 0 and 1.

For the CSV (gibbs_free_energies.csv), the verifier recomputes the expected ΔG values at several characteristic temperatures using exactly the same thermodynamic formulas and input parameters you were given. Each of your values is compared to the recomputed reference; a correct computation that stays within the verifier’s tolerance yields full credit for this stage.

For the stability summary (stability_summary.txt), the verifier checks whether the stated phase ordering is logically consistent with the ΔG curves you submitted in the CSV. A guess or a statement that contradicts your own CSV will not earn full marks.

No gold values, tolerances, or expected ordering are revealed here. Reporting only the paper's numbers without producing a correct, self-consistent computation will not be sufficient.
# Elastic anomalies in Al3Li from first‑principles electronic structure: role of d‑electrons

## Problem background
The intermetallic compound Al3Li exhibits mechanical properties that differ markedly from those of its constituent metals, aluminum and lithium. Despite lithium being a soft sp‑bonded metal, experimental observations indicate that the addition of lithium to aluminum leads to an increase in shear moduli, whereas the bulk modulus and lattice parameter decrease relative to pure aluminum. This is surprising given the larger atomic radius of lithium. Electronic‑structure calculations offer a way to probe the origin of these anomalies by examining the role of valence electron states, particularly whether d‑orbital occupation on lithium atoms contributes to the observed trends in the structural and elastic properties of Al3Li.

## Approach
The investigation uses self‑consistent density‑functional theory (DFT) within the local‑density approximation (LDA) for exchange and correlation. A linear muffin‑tin orbital (LMTO) method, or an equivalent all‑electron or pseudopotential implementation, is employed with s, p, and d valence states included for both aluminum and lithium. The workflow consists of several parts:  
- For pure Al (fcc), pure Li (bcc), and the ordered L1₂ phase Al3Li, compute total energies at a series of volumes around the expected equilibrium to obtain energy‑vs‑volume data sets.  
- Fit each energy‑volume set to a Birch–Murnaghan equation of state to extract the equilibrium lattice parameter (a₀) and bulk modulus (B).  
- Integrate the self‑consistent charge density inside atomic Wigner–Seitz spheres to obtain the s, p, and d electron occupations for Al3Li (and optionally for the pure elements).  
- Repeat the Al3Li calculation with the d‑orbital states on lithium explicitly removed from the basis, keeping all other settings identical, and derive the resulting a₀ and B from the no‑d volume scan.  
All steps are meant to be executed from scratch using public crystal structures and an open‑source DFT code; the computed results will be written to two structured output files for automatic verification.

## Reproduction target
The goal is to compute and report the following quantities in a single, coherent computational campaign:  
1. For pure aluminum, pure lithium, and the fully relaxed L1₂ Al3Li (full basis) — the equilibrium lattice parameter a₀ (in Å) and bulk modulus B (in GPa).  
2. The lattice mismatch between Al3Li and pure aluminum, defined as (a₀(Al3Li) − a₀(Al)) / a₀(Al).  
3. The enthalpy of formation of Al3Li per atom, (E(Al3Li) − 3 E(Al) − E(Li)) / (number of atoms), expressed in Ry/atom.  
4. The valence electron distribution inside the Li and Al atomic spheres in Al3Li, decomposed into s, p, and d contributions, written as a CSV table.  
5. For the calculation where lithium d‑orbitals are excluded, the resulting a₀ and B of Al3Li, which will be compared against the full‑basis results to probe the effect of d‑states.  
All results must be written to two files — `elastic_properties.json` and `charge_distribution.csv` — following the exact schema specified in the output contract.

## Assets

- Standard crystal structures for fcc Al, bcc Li, and L12 Al3Li
- Open‑source DFT or LMTO code (e.g., Questaal, ABINIT, Quantum ESPRESSO): https://www.questaal.org

## Workflow steps

### Step 1: Full DFT calculations for Al, Li, and Al3Li
- Role: process
- Action: Perform self‑consistent DFT (or LMTO) calculations for fcc Al, bcc Li, and L12 Al3Li using the Perdew–Zunger LDA exchange‑correlation functional. For each system, compute total energies at several volumes around the approximate equilibrium to generate total‑energy vs. volume data sets.
- Evidence: `/app/outputs/full_calc_EV_data.log`

### Step 2: DFT calculation for Al3Li without d‑states
- Role: process
- Action: Repeat the self‑consistent calculation for L12 Al3Li, but exclude the d‑orbital valence states on the Li atoms from the basis set. Keep all other settings identical. Generate a second total‑energy vs. volume data set.
- Evidence: `/app/outputs/nod_calc_EV_data.log`

### Step 3: Extract elastic and structural properties (scored)
- Role: scored (load-bearing)
- Action: From the energy‑volume data generated in steps 1 and 2, fit each set to a Birch–Murnaghan equation of state to determine the equilibrium lattice parameter a₀ and bulk modulus B for pure Al, pure Li, Al3Li (full basis), and Al3Li (no d‑states). Compute the lattice mismatch Δa/a between Al3Li and Al, and the enthalpy of formation of Al3Li. Write all results to elastic_properties.json.
- Output file: `/app/outputs/elastic_properties.json`
- Format: json
- Contract: JSON object with keys: Al (object with a0 in Å, B in GPa), Li (a0, B), Al3Li (a0, B), mismatch (dimensionless), enthalpy_formation (Ry/atom), Al3Li_no_d (a0, B). Example skeleton: {"Al":{"a0": <float>, "B": <float>}, "Li": {"a0": ..., "B": ...}, "Al3Li": {"a0": ..., "B": ...}, "mismatch": <float>, "enthalpy_formation": <float>, "Al3Li_no_d": {"a0": ..., "B": ...}}
- Scoring: scored by hidden verifier

### Step 4: Extract valence electron occupations (scored)
- Role: scored
- Action: From the self‑consistent charge density of the full Al3Li calculation, integrate the electron counts inside the Li and Al atomic (Wigner–Seitz) spheres, decomposed into s, p, d components. Compute reference occupations for pure Al and pure Li. Write a CSV table.
- Output file: `/app/outputs/charge_distribution.csv`
- Format: csv
- Contract: CSV with header: system,sphere,s,p,d. Rows: e.g., Al3Li,Li,<s>,<p>,<d> and Al3Li,Al,<s>,<p>,<d>. Optional rows: Al,Al,<s>,<p>,<d> and Li,Li,<s>,<p>,<d>.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/elastic_properties.json`
- `/app/outputs/charge_distribution.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### elastic_properties.json
- path: `/app/outputs/elastic_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Equilibrium lattice parameter and bulk modulus for pure Al, pure Li, Al3Li (full basis), and Al3Li (no d‑states), plus lattice mismatch and enthalpy of formation.
- schema:
  - `type`: object
  - `required`:
    - `Al`: object containing numeric keys a0 and B
    - `Li`: object containing numeric keys a0 and B
    - `Al3Li`: object containing numeric keys a0 and B
    - `mismatch`: number
    - `enthalpy_formation`: number
    - `Al3Li_no_d`: object containing numeric keys a0 and B
  - `units`:
    - `a0`: angstrom
    - `B`: GPa
    - `enthalpy_formation`: Ry/atom

### charge_distribution.csv
- path: `/app/outputs/charge_distribution.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Valence electron occupations inside atomic spheres for Al3Li, optionally also for pure Al and Li.
- schema:
  - `type`: table
  - `required_columns`: `system`, `sphere`, `s`, `p`, `d`

Notes: All values are to be derived from the DFT calculations. The hidden checker will compare the reported values to the paper’s gold numbers with appropriate tolerances; the no‑d values must show an overestimation trend relative to the full calculation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "elastic_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "Al": "object containing numeric keys a0 and B",
          "Li": "object containing numeric keys a0 and B",
          "Al3Li": "object containing numeric keys a0 and B",
          "mismatch": "number",
          "enthalpy_formation": "number",
          "Al3Li_no_d": "object containing numeric keys a0 and B"
        },
        "units": {
          "a0": "angstrom",
          "B": "GPa",
          "enthalpy_formation": "Ry/atom"
        }
      },
      "description": "Equilibrium lattice parameter and bulk modulus for pure Al, pure Li, Al3Li (full basis), and Al3Li (no d‑states), plus lattice mismatch and enthalpy of formation."
    },
    {
      "file": "charge_distribution.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "sphere",
          "s",
          "p",
          "d"
        ]
      },
      "description": "Valence electron occupations inside atomic spheres for Al3Li, optionally also for pure Al and Li."
    }
  ],
  "notes": "All values are to be derived from the DFT calculations. The hidden checker will compare the reported values to the paper’s gold numbers with appropriate tolerances; the no‑d values must show an overestimation trend relative to the full calculation."
}
```

## How you are scored
A hidden verifier inspects the submitted artifacts and compares the reported properties against reference values derived from the original study. The scoring is carried out independently for each workflow stage:  
- For `elastic_properties.json`, lattice parameters, bulk moduli, and the enthalpy of formation are compared with predetermined relative tolerances; the no‑d results are additionally evaluated against a structural trend that relates them to the full‑basis results.  
- For `charge_distribution.csv`, the s, p, d electron counts are compared with absolute tolerances.  
Each stage contributes to a weighted final reward, with the main elastic‑property and charge‑distribution stages carrying the highest weight. The verifier does not access your intermediate logs or environment; it only reads the specified output files. Submitting the expected numbers without having executed the full pipeline will not satisfy the evaluation, because the scoring relies on the self‑consistency and format of the artifacts produced by a genuine computational workflow.

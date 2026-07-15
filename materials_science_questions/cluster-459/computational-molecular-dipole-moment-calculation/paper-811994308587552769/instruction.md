# Computational Dipole Moment Calculation via Group-Decomposition Vector Addition

## Problem background
Insecticide development has benefited from understanding how molecular flexibility influences biological activity. In DDT-analogues of the form β,β,β-trichloro-α,α-bis-[X-aryl]-ethane, a hypothesis links contact insecticidal activity to the degree of rotational freedom of the aryl components. Determining the actual conformation and rotational freedom of these molecules requires comparing experimental dipole moment measurements with theoretical predictions. This task focuses on the theoretical side: computing the dipole moments of specific DDT-analogue molecules using a group-decomposition vector addition method, providing the necessary computed values for such a comparison.

## Approach
The molecule is conceptually decomposed into three components: a CH–CCl₃ group and two substituted aryl groups. The dipole moment of each component is known from literature values (provided below). The orientation of each dipole is determined by:
- The aryl group dipole orientation angle Θ relative to the C₁–C₄ axis, derived by vector addition of the moments of the parent substituted benzenes.
- The CH–CCl₃ group orientation angle σ, taken from tetrahedral geometry.
- The valence angles α (between the two aryl C₁–C₄ axes) and β (between one aryl axis and the CH–CCl₃ bond).

For fixed conformations (series dh' and hh'), the theoretical dipole moment is obtained by vector summation of the axis‑parallel components of the three groups. For the free‑rotation case, the mean‑square dipole is calculated using the relation μ̅² = μ₀² + Σ μₖ², where μ₀ are the axis‑parallel components and μₖ the perpendicular (rotating) components of the individual groups. The result is a set of dipole moments for specific molecule, conformation, and angle combinations that can be compared with experimental data.

## Reproduction target
Compute the theoretical dipole moments (in Debye) for the required seven combinations, listed in Step 2, and write them to `/app/outputs/dipole_moments.csv`. The file must contain exactly one row for each of the following:
- molecule `4-bromo-2-methyl`, conformation `dh`, alpha=110.0, beta=110.0
- molecule `4-bromo-2-methyl`, conformation `hh`, alpha=110.0, beta=110.0
- molecule `5-bromo-2-methyl`, conformation `dh`, alpha=114.0, beta=114.0
- molecule `5-bromo-2-methyl`, conformation `hh`, alpha=114.0, beta=114.0
- molecule `4-bromo-2-methyl`, conformation `free`, alpha=110.0, beta=110.0
- molecule `4-bromo-2-methyl`, conformation `free`, alpha=114.0, beta=114.0
- molecule `5-bromo-2-methyl`, conformation `free`, alpha=114.0, beta=114.0

All columns must follow the schema described in the output contract: molecule, conformation, alpha, beta, dipole_moment.

## Assets
All required physical constants, group dipole moments, and valence angles are provided directly in the workflow steps. No external datasets, models, or pretrained weights need to be downloaded.
- **Environment**: Python 3 with the `numpy` package for vector math (install via `pip`). Standard Python libraries suffice; the agent may install additional packages as needed.

## Workflow steps

### Step 1: Assemble group dipole moments and directional parameters
- Role: process
- Action: Gather the group dipole moments from the literature (values: 1,1,1-trichloroethane 1.77 D, toluene 0.35 D, bromobenzene 1.57 D, p-bromotoluene 1.94 D, m-bromotoluene 1.75 D, o-bromotoluene 1.44 D; C-H moment set to zero). Determine the directional parameters: the orientation angle Θ of each aryl group dipole relative to the C₁-C₄ axis by vector addition of the appropriate substituted benzene moments; the angle σ for the CH–CCl₃ group dipole from tetrahedral geometry; and note the given valence angles α and β (α=β=110° for the 4-bromo isomer, α=β=114° for the 5-bromo isomer). All parameters are derived using the method described in the paper.
- Evidence: `/app/outputs/parameters.txt`

### Step 2: Calculate theoretical dipole moments
- Role: scored (load-bearing)
- Action: Using the assembled parameters, compute the dipole moment for each target molecule/conformation/angle combination: (i) 4-bromo-2-methyl, dh', α=β=110°; (ii) 4-bromo-2-methyl, hh', α=β=110°; (iii) 5-bromo-2-methyl, dh', α=β=114°; (iv) 5-bromo-2-methyl, hh', α=β=114°; (v) 4-bromo-2-methyl, free, α=β=110°; (vi) 4-bromo-2-methyl, free, α=β=114°; (vii) 5-bromo-2-methyl, free, α=β=114°. For fixed conformations, compute the vector sum of rigid components; for free rotation, compute the mean-square dipole using the relation μ̅² = μ₀² + Σ μₖ², where μ₀ denotes axis-parallel components and μₖ the perpendicular components. Write all results to dipole_moments.csv.
- Output file: `/app/outputs/dipole_moments.csv`
- Format: csv
- Contract: Columns: molecule (string), conformation (one of 'dh', 'hh', 'free'), alpha (float, degrees), beta (float, degrees), dipole_moment (float, Debye). Molecule names: '4-bromo-2-methyl' and '5-bromo-2-methyl'. File must include exactly the seven rows defined in the action.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dipole_moments.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dipole_moments.csv
- path: `/app/outputs/dipole_moments.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Computed theoretical dipole moments for the seven specified molecule/conformation/angle combinations. The dipole moment values must match the paper's calculated values within a hidden tolerance.
- schema:
  - `type`: table
  - `required_columns`: `molecule`, `conformation`, `alpha`, `beta`, `dipole_moment`
  - `units`:
    - `alpha`: degrees
    - `beta`: degrees
    - `dipole_moment`: Debye

Notes: The group dipole moments (1,1,1-trichloroethane, toluene, bromobenzene, p/m/o-bromotoluene) and the valence angles α=β=110° and 114° are provided directly in the task instructions. The directional parameters Θ and σ are derived by the agent from these inputs using the vector addition method described. The process step produces a parameters.txt evidence file, but only dipole_moments.csv is scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dipole_moments.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "molecule",
          "conformation",
          "alpha",
          "beta",
          "dipole_moment"
        ],
        "units": {
          "alpha": "degrees",
          "beta": "degrees",
          "dipole_moment": "Debye"
        }
      },
      "description": "Computed theoretical dipole moments for the seven specified molecule/conformation/angle combinations. The dipole moment values must match the paper's calculated values within a hidden tolerance."
    }
  ],
  "notes": "The group dipole moments (1,1,1-trichloroethane, toluene, bromobenzene, p/m/o-bromotoluene) and the valence angles α=β=110° and 114° are provided directly in the task instructions. The directional parameters Θ and σ are derived by the agent from these inputs using the vector addition method described. The process step produces a parameters.txt evidence file, but only dipole_moments.csv is scored."
}
```

## How you are scored
After you submit `dipole_moments.csv`, a hidden verifier will read the file and check its format. For each of the seven required rows, the verifier will extract the `dipole_moment` value and compare it to an expected reference value derived from the paper's original calculations. A match is successful if the absolute difference is within a pre‑defined tolerance (which accounts for minor numerical implementation differences). Your overall score is the proportion of the seven rows that pass, expressed as a number between 0 and 1 (e.g., 7/7 = 1.0). The weighting is uniform across rows.

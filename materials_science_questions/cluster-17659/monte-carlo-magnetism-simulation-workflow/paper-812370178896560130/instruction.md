# Ferromagnetic three-spin Ising model: transition temperatures and configurational entropy from replica/cavity method

## Problem background
A finite-connectivity ferromagnetic Ising model with three-spin interactions can, in principle, exhibit both a ferromagnetically ordered crystalline phase and a glassy phase reminiscent of structural glasses. This task uses the replica/cavity method to determine, for the model defined on a Bethe hyper-lattice with connectivity k=3, the qualitative phase behavior by computing the temperatures at which ferromagnetic and glassy solutions appear and comparing their free energies, and to extract the configurational entropy at the dynamical glass transition. The quantities of interest are the spinodal temperature where a non-zero effective field first appears, the temperature where the ferromagnetic free energy becomes dominant, the dynamical and Kauzmann glass transition temperatures from a one-step replica-symmetry-breaking variational approximation, and the associated configurational entropy.

## Approach
The equilibrium properties are studied using the replica/cavity method. Three solutions are required:

- **Paramagnetic solution**: the free energy per spin at inverse temperature β is
  -β f_pm = ln 2 + (1/3)(k+1) ln cosh(β).
  For the connectivity k=3, this becomes -β f_pm = ln 2 + (4/3) ln cosh(β).

- **Ferromagnetic (replica-symmetric) solution**: a site-independent effective field h satisfies the self-consistency equation
  tanh(β h) = tanh(β) [tanh(β k h)]^2.
  The corresponding free energy is
  -β f_fm = ln 2 + (k+1)/3 ln[ cosh(β) cosh(β k h)^3 + sinh(β) sinh(β k h)^3 ] - k ln cosh(β (k+1) h).
  The spinodal temperature T_ms is the highest temperature where a non-trivial solution h ≠ 0 exists. The first-order transition temperature T_fm is found by locating the temperature below T_ms where f_fm < f_pm.

- **One-step replica-symmetry-broken (1-RSB) glassy solution**: the glassy phase is described by a distribution of local fields obtained from the cavity method. The order parameter is a functional of the field distribution, and the self-consistent equations are solved by population dynamics. The dynamical transition temperature T_c is the highest temperature at which a non-trivial glassy solution first emerges, and the Kauzmann temperature T_K is the temperature where the glassy free energy becomes lower than the paramagnetic one. The configurational entropy at T_c is the free energy difference between the paramagnetic and glassy states per spin.

## Reproduction target
For the ferromagnetic three-spin Ising model on a Bethe hyper-lattice with fixed connectivity k=3, use the replica-symmetric solutions and the exact one-step RSB solution to numerically compute: (i) the ferromagnetic spinodal temperature T_ms, (ii) the first-order ferromagnetic transition temperature T_fm, (iii) the dynamical glass transition temperature T_c and the Kauzmann temperature T_K, and (iv) the configurational entropy at T_c. Report each quantity in the specified output file.

## Assets

- numpy: numpy
- scipy: scipy
- matplotlib: matplotlib

## Workflow steps

### Step 1: Compute ferromagnetic spinodal temperature T_ms
- Role: scored
- Action: Solve the saddle-point equation for the effective field h as a function of temperature for connectivity k=3. Identify T_ms as the highest temperature where a nonzero solution h exists. Write the value to T_ms.txt.
- Output file: `/app/outputs/T_ms.txt`
- Format: txt
- Contract: Single float value on one line.
- Scoring: scored by hidden verifier

### Step 2: Compute first-order ferromagnetic transition temperature T_fm
- Role: scored
- Action: Using the ferromagnetic free-energy expression and the paramagnetic free-energy expression for k=3, find the temperature T_fm below T_ms at which the ferromagnetic free energy becomes lower than the paramagnetic one. Write the value to T_fm.txt.
- Output file: `/app/outputs/T_fm.txt`
- Format: txt
- Contract: Single float value on one line.
- Scoring: scored by hidden verifier

### Step 3: Determine glass transition temperatures T_c and T_K from exact 1-RSB solution
- Role: scored (load-bearing)
- Action: Implement the exact one-step RSB solution for k=3 using the cavity method and population dynamics of local fields. Determine the dynamical temperature T_c as the highest temperature where a non-trivial glassy solution exists, and the Kauzmann temperature T_K as the temperature where the glassy free energy becomes lower than the paramagnetic one. Write both values to T_c_and_T_K.txt in the format 'T_c <value> T_K <value>'.
- Output file: `/app/outputs/T_c_and_T_K.txt`
- Format: txt
- Contract: First line contains 'T_c <float> T_K <float>'.
- Scoring: scored by hidden verifier

### Step 4: Compute configurational entropy at T_c
- Role: scored (load-bearing)
- Action: From the exact 1-RSB free energy, compute the configurational entropy at T_c as the free-energy difference between the glassy and paramagnetic states. Write the value to S_conf_at_Tc.txt.
- Output file: `/app/outputs/S_conf_at_Tc.txt`
- Format: txt
- Contract: Single float value on one line.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/T_ms.txt`
- `/app/outputs/T_fm.txt`
- `/app/outputs/T_c_and_T_K.txt`
- `/app/outputs/S_conf_at_Tc.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### T_ms.txt
- path: `/app/outputs/T_ms.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: The ferromagnetic spinodal temperature T_ms.
- schema:
  - `type`: text
  - `description`: Single float value representing T_ms.

### T_fm.txt
- path: `/app/outputs/T_fm.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: The first-order ferromagnetic transition temperature T_fm.
- schema:
  - `type`: text
  - `description`: Single float value representing T_fm.

### T_c_and_T_K.txt
- path: `/app/outputs/T_c_and_T_K.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: The dynamical glass transition temperature T_c and Kauzmann temperature T_K from the 1-RSB variational approximation.
- schema:
  - `type`: text
  - `description`: First line contains 'T_c <float> T_K <float>'.

### S_conf_at_Tc.txt
- path: `/app/outputs/S_conf_at_Tc.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: The configurational entropy at T_c from the variational 1-RSB free energy.
- schema:
  - `type`: text
  - `description`: Single float value representing configurational entropy at T_c.

Notes: All outputs are text files containing numerical values derived from analytical equations. No Monte Carlo data is required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "T_ms.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "Single float value representing T_ms."
      },
      "description": "The ferromagnetic spinodal temperature T_ms."
    },
    {
      "file": "T_fm.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "Single float value representing T_fm."
      },
      "description": "The first-order ferromagnetic transition temperature T_fm."
    },
    {
      "file": "T_c_and_T_K.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "First line contains 'T_c <float> T_K <float>'."
      },
      "description": "The dynamical glass transition temperature T_c and Kauzmann temperature T_K from the 1-RSB variational approximation."
    },
    {
      "file": "S_conf_at_Tc.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "Single float value representing configurational entropy at T_c."
      },
      "description": "The configurational entropy at T_c from the variational 1-RSB free energy."
    }
  ],
  "notes": "All outputs are text files containing numerical values derived from analytical equations. No Monte Carlo data is required."
}
```

## How you are scored
A hidden verifier will independently read each of the four scored output files, extract the numeric results, and compare them against reference values using predetermined tolerances appropriate for numerical solutions of these mean-field equations. Each scored artifact carries a weight that contributes to the total reward. The verifier does not check whether your answer matches a published value exactly; it evaluates whether you have faithfully performed the required saddle-point solutions, free-energy comparisons, and variational optimizations. Reporting a number without executing the corresponding computation will not receive credit.

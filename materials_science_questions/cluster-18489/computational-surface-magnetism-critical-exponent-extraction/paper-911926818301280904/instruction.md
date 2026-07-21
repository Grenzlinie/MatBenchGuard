# Surface and Excitation Energies of a Quantum Spin Chain

## Problem background
The system under study is a one-dimensional quantum spin chain with many competing interactions: nearest-neighbor exchange, next-nearest-neighbor coupling, a chiral three-spin term, and Dzyaloshinskii–Moriya interactions, plus unparallel boundary magnetic fields that break U(1) symmetry. By using a zero-root parameterization of the transfer-matrix eigenvalue, the thermodynamic-limit properties of the chain can be captured by closed-form analytic expressions. This task focuses on computing four headline energy quantities that characterize the system: the surface energy induced by the boundaries in the antiferromagnetic regime, the bulk elementary excitation energy, the boundary excitation energy, and the surface energy in the ferromagnetic regime. Each quantity is a function of the model parameter a (pure imaginary) and one or more boundary / excitation parameters. The goal is to evaluate these expressions numerically for specified input values and thereby demonstrate the exact physical picture of the competing chain.

## Approach
The energies are given by analytic formulas that involve elementary functions and integrals. All computations are performed with standard open‑source Python libraries (numpy, scipy).

**Model parameter**: `a` is a pure imaginary number. It will be supplied as a string such as `'0'`, `'0.6i'`, `'0.8i'` representing `a = 0`, `a = 0.6 i`, `a = 0.8 i`. Convert it to a complex number accordingly; the formulas below use `a` as a complex quantity with `Re(a)=0`.

**Surface energy** (output `surface_energy.json`):
The surface energy in the antiferromagnetic regime is the sum of three contributions:

  E_b = e_b(p) + e_b(\bar{q}) + e_{b0} ,

where `\bar{q} = q / \sqrt{1+\xi^2}`. Each term is an integral over a real variable `k`:

  e_b(p) = (4a²−1)/4 ∫_{-∞}^{∞} (1 − e^{-|k|}) cosh(a k) * (e^{-|p k|} / (e^{-|k|/2} cosh(k/2))) dk ,

  e_b(\bar{q}) = same as e_b(p) with `p` replaced by `\bar{q}` ,

  e_{b0} = (4a²−1)/4 ∫_{-∞}^{∞} (1 − e^{-|k|}) cosh(a k) * ((e^{-|k|} − e^{-|k|/2}) / (e^{-|k|/2} cosh(k/2))) dk .

Because `a` is imaginary, `cosh(a k) = cos(|a| k)`; the integrals are convergent and can be evaluated numerically (e.g., `scipy.integrate.quad`).

**Bulk elementary excitation energy** (output `bulk_excitation.json`):

  δ_{e1}(z) = −(4a²−1) ( π / cosh(z + ia) + π / cosh(z − ia) ) .

Here `z` is a real variable and `a` is the same imaginary model parameter.

**Boundary elementary excitation energy** (output `boundary_excitation.json`):

  δ_{ep} = −π (4a²−1) ( csc( π(|p| + a) ) + csc( π(|p| − a) ) ) ,

where `csc(x) = 1 / sin(x)`. The formula is valid for `|p| < 1/2`; the input lists respect this regime.

**Ferromagnetic surface energy** (output `ferromagnetic_surface.json`):

  E_b^{ferr} = (4a²−1)/2 [ 2|p|/(p²−a²) + 2|\bar{q}|/(\bar{q}²−a²) + 2/(1−a²) − 1/(1/4−a²) ] ,

with `\bar{q} = q/\sqrt{1+\xi^2}` as before.

**Input parameter tuples**

The agent must evaluate the energies for the following lists of parameters (one tuple per line):

- For `surface_energy.json` and `ferromagnetic_surface.json` (same (a, p, q, ξ) set):
  a=0,   p=0.1, q=0.1, ξ=0.5
  a=0,   p=0.5, q=0.5, ξ=1.2
  a=0.6i, p=0.2, q=0.3, ξ=0.5
  a=0.6i, p=0.5, q=0.5, ξ=1.2
  a=0.6i, p=0.7, q=0.7, ξ=1.2
  a=0.8i, p=0.3, q=0.4, ξ=0.5
  a=0.8i, p=0.6, q=0.6, ξ=1.2
  a=0.8i, p=0.9, q=0.9, ξ=1.2

- For `bulk_excitation.json` (a, z):
  a=0, z=-2.0
  a=0, z=-1.0
  a=0, z=0.0
  a=0, z=1.0
  a=0, z=2.0
  a=0.6i, z=-2.0
  a=0.6i, z=-1.0
  a=0.6i, z=0.0
  a=0.6i, z=1.0
  a=0.6i, z=2.0
  a=0.8i, z=-2.0
  a=0.8i, z=-1.0
  a=0.8i, z=0.0
  a=0.8i, z=1.0
  a=0.8i, z=2.0

- For `boundary_excitation.json` (a, p) with |p| < 0.5:
  a=0,     p=0.1
  a=0,     p=0.3
  a=0,     p=0.45
  a=0.6i,  p=0.1
  a=0.6i,  p=0.25
  a=0.6i,  p=0.45
  a=0.8i,  p=0.1
  a=0.8i,  p=0.3
  a=0.8i,  p=0.45

These lists are exhaustive; the agent must write exactly one JSON object per tuple in the corresponding output file, in the order given. The hidden checker will compare the computed energy against a high‑precision reference for each tuple.

## Reproduction target
Produce four JSON files, each containing the numerically evaluated energies for the parameter tuples specified in the Approach section:
- `surface_energy.json` — array of {a (string), p (float), q (float), xi (float), E_b (float)} for each (a,p,q,ξ) tuple.
- `bulk_excitation.json` — array of {a (string), z (float), energy (float)} for each (a,z) pair.
- `boundary_excitation.json` — array of {a (string), p (float), energy (float)} for each (a,p) pair.
- `ferromagnetic_surface.json` — array of {a (string), p (float), q (float), xi (float), E_b_ferr (float)} for each (a,p,q,ξ) tuple.
The files must contain exactly the lists above, in the same order, with the five fields for surface and ferromagnetic, and three fields for excitation outputs. The energy values are computed directly from the analytic formulas using numerical integration where required. No training, data fetching, or intermediate artifacts are needed — the task is a pure numerical evaluation.

## Assets

- numpy: https://pypi.org/project/numpy/
- scipy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Compute surface energy
- Role: scored (load-bearing)
- Action: Implement the surface energy expression that depends on boundary parameters p, q, ξ and model parameter a, which involves integrals over a variable. For each tuple (a, p, q, ξ) from the provided list, compute the surface energy and store the results.
- Output file: `/app/outputs/surface_energy.json`
- Format: json
- Contract: Array of objects, each with keys: a (string), p (float), q (float), xi (float), E_b (float).
- Scoring: scored by hidden verifier

### Step 2: Compute bulk excitation energy
- Role: scored
- Action: Implement the bulk elementary excitation energy formula as a function of variable z and model parameter a. For each pair (a, z) from the provided list, compute the energy and store the results.
- Output file: `/app/outputs/bulk_excitation.json`
- Format: json
- Contract: Array of objects, each with keys: a (string), z (float), energy (float).
- Scoring: scored by hidden verifier

### Step 3: Compute boundary excitation energy
- Role: scored
- Action: Implement the boundary elementary excitation energy formula as a function of boundary parameter p and model parameter a. For each pair (a, p) from the provided list, compute the energy and store the results.
- Output file: `/app/outputs/boundary_excitation.json`
- Format: json
- Contract: Array of objects, each with keys: a (string), p (float), energy (float).
- Scoring: scored by hidden verifier

### Step 4: Compute ferromagnetic surface energy
- Role: scored
- Action: Implement the ferromagnetic surface energy formula that depends on a, p, q, ξ, where a quantity derived from q and ξ appears. For each tuple (a, p, q, ξ) from the provided list, compute the energy and store the results.
- Output file: `/app/outputs/ferromagnetic_surface.json`
- Format: json
- Contract: Array of objects, each with keys: a (string), p (float), q (float), xi (float), E_b_ferr (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/surface_energy.json`
- `/app/outputs/bulk_excitation.json`
- `/app/outputs/boundary_excitation.json`
- `/app/outputs/ferromagnetic_surface.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### surface_energy.json
- path: `/app/outputs/surface_energy.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed surface energy values for given parameter tuples.
- schema:
  - `type`: array
  - `items`:
    - `a`: string
    - `p`: float
    - `q`: float
    - `xi`: float
    - `E_b`: float

### bulk_excitation.json
- path: `/app/outputs/bulk_excitation.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed bulk elementary excitation energies for (a, z) pairs.
- schema:
  - `type`: array
  - `items`:
    - `a`: string
    - `z`: float
    - `energy`: float

### boundary_excitation.json
- path: `/app/outputs/boundary_excitation.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed boundary excitation energies for (a, p) pairs.
- schema:
  - `type`: array
  - `items`:
    - `a`: string
    - `p`: float
    - `energy`: float

### ferromagnetic_surface.json
- path: `/app/outputs/ferromagnetic_surface.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed ferromagnetic surface energies for given tuples.
- schema:
  - `type`: array
  - `items`:
    - `a`: string
    - `p`: float
    - `q`: float
    - `xi`: float
    - `E_b_ferr`: float

Notes: All four output files are independently scored by recomputing each energy from the agent's submitted parameter values within tolerance; the four scores are averaged equally.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "surface_energy.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "a": "string",
          "p": "float",
          "q": "float",
          "xi": "float",
          "E_b": "float"
        }
      },
      "description": "Computed surface energy values for given parameter tuples."
    },
    {
      "file": "bulk_excitation.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "a": "string",
          "z": "float",
          "energy": "float"
        }
      },
      "description": "Computed bulk elementary excitation energies for (a, z) pairs."
    },
    {
      "file": "boundary_excitation.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "a": "string",
          "p": "float",
          "energy": "float"
        }
      },
      "description": "Computed boundary excitation energies for (a, p) pairs."
    },
    {
      "file": "ferromagnetic_surface.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "a": "string",
          "p": "float",
          "q": "float",
          "xi": "float",
          "E_b_ferr": "float"
        }
      },
      "description": "Computed ferromagnetic surface energies for given tuples."
    }
  ],
  "notes": "All four output files are independently scored by recomputing each energy from the agent's submitted parameter values within tolerance; the four scores are averaged equally."
}
```

## How you are scored
A hidden verifier independently evaluates each of the four output files. For every tuple, it compares your computed energy against a pre‑computed reference value using an appropriate numerical tolerance. A tuple is considered correct if its energy is within the tolerance; otherwise it counts as a miss. The reward for each file is the fraction of its tuples that pass. The four scores are averaged equally to produce the final overall reward (a number between 0 and 1, written to /logs/verifier/reward.txt). Simply reporting a number is not sufficient — the checker reads your JSON files and performs the comparison itself.

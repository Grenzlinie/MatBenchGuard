# Derivation of Barrett's formula from a shell model

## Problem background
In quantum ferroelectrics the dielectric susceptibility deviates from the classical Curie-Weiss law at low temperatures. Barrett proposed a phenomenological four-parameter formula that describes this crossover. This task reproduces the theoretical derivation of Barrett's formula from a microscopic shell model of a perovskite linear chain. Using the renormalized harmonic approximation, the derivation expresses Barrett's empirical constants in terms of the underlying shell-model force constants and temperature. The target is a set of symbolic expressions that link the macroscopic susceptibility to the microscopic parameters.

## Approach
The derivation is carried out symbolically, relying only on the equations specified in the workflow steps. The shell-model Hamiltonian for a linear chain includes harmonic and anharmonic core-shell interactions. The relative shell-core displacement is introduced, and equations of motion are written under the adiabatic condition for the electronic shell. The renormalized harmonic approximation replaces the quartic term by its thermal-average linearized form, introducing a temperature-dependent effective coupling g_T. This g_T is expressed as an integral over wavevectors and then approximated analytically near the self-consistency temperature. The renormalized soft-mode frequency is obtained from the effective coupling. Finally, the resulting expression for the dielectric susceptibility is manipulated into Barrett's form to extract the four constants (A, B, T₁, T₀) as functions of the microscopic parameters. The entire workflow is executed as a chain of symbolic manipulations.

## Reproduction target
Produce three symbolic text files using the provided workflow:
1. The squared renormalized soft-mode frequency ω_F²(T) expressed in terms of ω₀, f, and the combined coupling g.
2. The approximated expression for g_T near the self-consistency temperature T₁, written in terms of G and the hyperbolic cotangent.
3. The four Barrett constants—A, B, T₁, T₀—each expressed in terms of the microscopic parameters ω₀, f, g₂, g₄, G, ℏ, and k.
The hidden verifier will parse these expressions and test their symbolic equivalence to the standard results obtained from the renormalized harmonic approximation of the shell model.

## Assets

- sympy: sympy

## Workflow steps

### Step 1: Set up shell-model Hamiltonian and equations of motion
- Role: process
- Action: Define the shell-model Hamiltonian (linear chain with nearest/next-nearest interactions and anharmonic oxygen-shell core coupling), introduce the shell-core relative displacement variable, and derive the equations of motion for the core displacements and the adiabatic condition for the shell. Do not write any output file.
- Evidence: none

### Step 2: Derive renormalized soft-mode frequency
- Role: scored (load-bearing)
- Action: Apply the renormalized harmonic approximation (replace the quartic term by its thermal-average linearized form), combine with the harmonic shell-core coupling, and obtain the renormalized frequency squared ω_F^2(T). Write the symbolic expression to the output file.
- Output file: `/app/outputs/renormalized_frequency.txt`
- Format: txt
- Contract: Single line containing a symbolic expression.
- Scoring: scored by hidden verifier

### Step 3: Approximate g_T from the mode integral
- Role: scored
- Action: Express g_T as a thermal-average integral over wavevectors, then approximate the integral near the self-consistency temperature T₁ by replacing it with its integrand and collecting multiplicative constants into G. Write the resulting analytic form to the output file.
- Output file: `/app/outputs/g_T_approximation.txt`
- Format: txt
- Contract: Single line containing a symbolic expression.
- Scoring: scored by hidden verifier

### Step 4: Derive Barrett-formula constants
- Role: scored
- Action: Insert the approximated g_T and the combined g into ω_F^2(T), manipulate the resulting susceptibility expression to obtain Barrett's formula, and extract the four constants A, B, T₁, T₀ in terms of the microscopic parameters. Write each constant on a separate line.
- Output file: `/app/outputs/barrett_constants.txt`
- Format: txt
- Contract: Four lines, each beginning with the constant name followed by '=' and the symbolic expression.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/renormalized_frequency.txt`
- `/app/outputs/g_T_approximation.txt`
- `/app/outputs/barrett_constants.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### renormalized_frequency.txt
- path: `/app/outputs/renormalized_frequency.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: The derived renormalized soft-mode frequency squared.
- schema:
  - `type`: text
  - `description`: Single line containing a symbolic expression for ω_F^2(T) in terms of ω₀, f, g (where g = g_T + g₂).

### g_T_approximation.txt
- path: `/app/outputs/g_T_approximation.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: The approximate expression for g_T from the mode integral near T₁.
- schema:
  - `type`: text
  - `description`: Single line containing the approximated symbolic expression for g_T.

### barrett_constants.txt
- path: `/app/outputs/barrett_constants.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: The Barrett-formula constants expressed in terms of microscopic shell-model parameters.
- schema:
  - `type`: text
  - `description`: Four lines, each a constant assignment: A = ..., B = ..., T₁ = ..., T₀ = ...

Notes: All expressions are symbolic and compared for equivalence with the paper after normalization using sympy.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "renormalized_frequency.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "Single line containing a symbolic expression for ω_F^2(T) in terms of ω₀, f, g (where g = g_T + g₂)."
      },
      "description": "The derived renormalized soft-mode frequency squared."
    },
    {
      "file": "g_T_approximation.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "Single line containing the approximated symbolic expression for g_T."
      },
      "description": "The approximate expression for g_T from the mode integral near T₁."
    },
    {
      "file": "barrett_constants.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "Four lines, each a constant assignment: A = ..., B = ..., T₁ = ..., T₀ = ..."
      },
      "description": "The Barrett-formula constants expressed in terms of microscopic shell-model parameters."
    }
  ],
  "notes": "All expressions are symbolic and compared for equivalence with the paper after normalization using sympy."
}
```

## How you are scored
A hidden verifier evaluates each scored output file independently. It parses the symbolic expression, normalises it with sympy, and compares for formal equivalence against the expected form for that artifact. Each artifact carries a weight; the final reward is the weighted sum of partial scores. Providing correct symbolic output that matches the derived forms yields full credit.

# Analytic Electron-Phonon Polarizability Calculation

## Problem background
In the electron-phonon model with an Einstein (dispersionless optical) phonon spectrum, earlier work using a ladder approximation predicted a pole in the irreducible electronic polarizability at the bare phonon frequency q0=ω, which would lead to a splitting of the optical mode into two branches. This work recalculates the polarizability to first order in a weak-coupling expansion to re-examine the presence of the pole and the resulting phonon renormalization. The core quantities to compute are the total irreducible polarizability P(q) including first-order corrections and the resulting renormalized optical phonon frequency.

## Approach
The evaluation is based on analytic loop integrals for a single-band electron gas (Fermi velocity vF, density of states N) coupled to a dispersionless Einstein phonon mode of bare frequency ω with coupling constant g.

Zeroth‑order polarizability (single loop) for |q| < q0/vF:
P^(0)(q) = N [ (q0 / (vF|q|)) ln((q0 + vF|q|) / (q0 − vF|q|)) − 2 ].

First‑order correction from self‑energy and vertex diagrams:
P^(1)(q) = 2 g^2 N^2 [ 1/(q0^2 − (vF|q|)^2) − 1/(2 vF|q|)^2 ln^2((q0 + vF|q|) / (q0 − vF|q|)) ] × [ ln(ω^2 / |ω^2 − q0^2|) − (q0/ω) ln |(ω + q0)/(ω − q0)| − iπ (|q0| − ω)/ω Θ(|q0| − ω) ].

Total irreducible polarizability: P(q) = P^(0)(q) + P^(1)(q).

Using this P(q), the renormalized optical phonon frequency ω̃ is obtained by solving the dressed phonon equation
q0^2 − ω^2 − g^2 P(q0, |q|) = 0
in the vicinity of q0 = ω. The solution yields ω̃ for the given momentum transfer |q|.

## Reproduction target
You are given the following model parameters (all in convenient dimensionless units):
- Fermi velocity vF = 1.0
- bare Einstein phonon frequency ω = 0.1
- electron‑phonon coupling constant g = 0.01
- density of states N = 1.0
- momentum vector q = (0.1, 0.0, 0.0).

Your task:
1. Implement the analytic expressions for P^(0)(q), P^(1)(q), and total P(q).
2. Evaluate the total irreducible polarizability at q0 = ω to obtain P_at_omega (the real part; the imaginary part vanishes at q0=ω).
3. Solve the dressed phonon equation q0^2 − ω^2 − g^2 P(q0, |q|) = 0 for q0 near ω to find the renormalized optical phonon frequency ω̃ (omega_tilde).
4. Output both results in the JSON file /app/outputs/results.json with keys "q", "P_at_omega", "omega_tilde".

## Assets

- Python 3: https://www.python.org/
- NumPy: numpy

## Workflow steps

### Step 1: Implement analytic polarizability expressions
- Role: process
- Action: Read the specified model parameters (Fermi velocity vF, bare Einstein phonon frequency omega, electron-phonon coupling constant g, density of states N) and the momentum q from the provided input. Implement the closed-form formulas for the zeroth-order polarizability P^(0)(q), the self-energy contribution A(q), the vertex correction B(q), assemble the first-order polarizability P^(1)(q) = A(q)+A(-q)+B(q), compute the total polarizability P(q) in the long-wave limit near q0=omega, and solve the dressed phonon equation to obtain the renormalized optical phonon frequency tilde-omega. This step performs all required analytical/numerical computations but does not produce a scored artifact.
- Evidence: none

### Step 2: Output final polarizability and renormalized frequency
- Role: scored (load-bearing)
- Action: Write a JSON file containing the computed total irreducible polarizability P(q) evaluated at q0=omega (denoted P_at_omega) and the renormalized optical phonon frequency tilde-omega (omega_tilde) for the given q vector. Save the file as results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"q": [float, float, float], "P_at_omega": float, "omega_tilde": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Final computed polarizability and renormalized phonon frequency. P_at_omega is the irreducible polarizability evaluated at q0=omega; omega_tilde is the renormalized optical phonon frequency from the Dyson equation.
- schema:
  - `type`: object
  - `required`:
    - `q`: list of 3 floats
    - `P_at_omega`: float
    - `omega_tilde`: float
  - `items`: object
  - `required_columns`:
  - `units`:
    - `q`: arbitrary
    - `P_at_omega`: same as density of states N
    - `omega_tilde`: energy (frequency)

Notes: The agent must derive all quantities from the given model parameters and momentum, not copy any pre-existing numbers. The checker will recompute the expected values from the same analytic formulas using the parameters specified in the instruction and compare within tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "q": "list of 3 floats",
          "P_at_omega": "float",
          "omega_tilde": "float"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "q": "arbitrary",
          "P_at_omega": "same as density of states N",
          "omega_tilde": "energy (frequency)"
        }
      },
      "description": "Final computed polarizability and renormalized phonon frequency. P_at_omega is the irreducible polarizability evaluated at q0=omega; omega_tilde is the renormalized optical phonon frequency from the Dyson equation."
    }
  ],
  "notes": "The agent must derive all quantities from the given model parameters and momentum, not copy any pre-existing numbers. The checker will recompute the expected values from the same analytic formulas using the parameters specified in the instruction and compare within tolerance."
}
```

## How you are scored
A hidden verifier independently recomputes the expected values of P_at_omega and omega_tilde from the same analytic formulas and the very same model parameters (vF, ω, g, N, q) that are provided to you. It compares your submitted values against these reference values using an absolute tolerance. If both quantities fall within the hidden tolerance, you earn full credit for that artifact; the reward degrades as the deviation increases. The final reward is the weighted fraction of the scored outputs that meet the tolerance threshold. Reporting a pre‑existing number without performing the computation yourself will not pass the comparison.

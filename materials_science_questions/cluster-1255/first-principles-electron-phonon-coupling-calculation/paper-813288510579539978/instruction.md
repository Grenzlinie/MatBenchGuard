# Analytic Electron-Phonon Polarizability Calculation

## Problem background
In the electron-phonon model with an Einstein (dispersionless optical) phonon spectrum, earlier work using a ladder approximation predicted a pole in the irreducible electronic polarizability at the bare phonon frequency \(q_0=\omega\), which would lead to a splitting of the optical mode into two branches. This work recalculates the polarizability to first order in a weak-coupling expansion and shows that there is no pole; instead the optical phonon undergoes a momentum-dependent hardening. The key quantities to compute are the total irreducible polarizability \(P(q)\) in the long-wave limit near \(q_0=\omega\) and the resulting renormalised optical phonon frequency \(\widetilde{\omega}\).

## Approach
The evaluation is based on analytic loop integrals for a single-band electron gas (Fermi velocity \(v_F\), density of states \(N\)) coupled to a dispersionless Einstein phonon mode of bare frequency \(\omega\) with coupling constant \(g\). The exact polarizability expressions involve logarithmic terms that diverge when \(v_F|\mathbf{q}| = q_0\). Because the parameters given below place us exactly at the singular point \(v_F|\mathbf{q}| = \omega\) when \(q_0=\omega\), the **long‑wave, near‑pole approximations derived in the paper (Eqs. 15 and 16) must be used** to obtain finite and physically meaningful results.

Define the dimensionless electron‑phonon coupling constant  
\[
\lambda \equiv \frac{g^2 N}{\omega^2}.
\]

In the long‑wave limit (\(|\mathbf{q}| \ll \omega/v_F\)) and for \(q_0\) close to \(\omega\), the total irreducible polarizability simplifies to

\[
P(q) \;\simeq\; \frac{2N}{3}\left(\frac{v_F|\mathbf{q}|}{\omega}\right)^{\!2}
\bigl(1 - 2\lambda\ln 2\bigr). \qquad (15)
\]

Using this polarizability, the dressed phonon propagator  
\[
\widetilde{D}^{-1}(q) = q_0^2 - \omega^2 - g^2 P(q)
\]
yields the renormalised optical phonon frequency

\[
\widetilde{\omega} \;\simeq\; \omega + \frac{\lambda}{3}\,\frac{(v_F|\mathbf{q}|)^2}{\omega}. \qquad (16)
\]

These two formulae are the ones you must implement; they are analytic, closed‑form, and free of the singularities that plague the exact expressions at the chosen parameters.

## Reproduction target
You are given the following model parameters (all in convenient dimensionless units):
- Fermi velocity \(v_F = 1.0\)
- bare Einstein phonon frequency \(\omega = 0.1\)
- electron‑phonon coupling constant \(g = 0.01\)
- density of states \(N = 1.0\)
- momentum vector \(\mathbf{q} = (0.1,\; 0.0,\; 0.0)\), whose magnitude is \(|\mathbf{q}| = 0.1\)

Using the long‑wave approximations **Eqs. (15) and (16)** above:
1. Compute the dimensionless coupling \(\lambda = g^2 N / \omega^2\).
2. Evaluate the polarizability at \(q_0 = \omega\) using Eq. (15); call this value `P_at_omega`.
3. Evaluate the renormalised phonon frequency using Eq. (16); call this value `omega_tilde`.
4. Output both results in the JSON file `/app/outputs/results.json` with keys `"q"`, `"P_at_omega"`, `"omega_tilde"`.

**Important:** The exact expressions \(P^{(0)}(q)\) and \(P^{(1)}(q)\) from the paper contain logarithmic singularities and a \(1/(q_0^2-(v_F|\mathbf{q}|)^2)\) factor that diverge for the assigned values. You must not attempt to evaluate those raw formulas; use only the long‑wave approximations given above.

## Assets
- Python 3: https://www.python.org/
- NumPy: numpy

## Workflow steps

### Step 1: Implement the analytic approximations
- Role: process
- Action: Read the model parameters (\(v_F\), \(\omega\), \(g\), \(N\)) and the momentum vector \(\mathbf{q}\). Compute the magnitude \(|\mathbf{q}|\) and \(\lambda\). Implement Eqs. (15) and (16) to obtain `P_at_omega` and `omega_tilde`. This step performs all required analytical/numerical computations but does not produce a scored artifact.
- Evidence: none

### Step 2: Output final polarizability and renormalized frequency
- Role: scored (load-bearing)
- Action: Write a JSON file containing the computed values. Save the file as `results.json`.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: `{"q": [float, float, float], "P_at_omega": float, "omega_tilde": float}`
- Scoring: scored by hidden verifier

## Output files
Write all artefacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract
Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Final computed polarizability and renormalized phonon frequency. `P_at_omega` is the irreducible polarizability evaluated at \(q_0=\omega\) using the long‑wave approximation; `omega_tilde` is the renormalized optical phonon frequency from the Dyson equation (also in the long‑wave limit).
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
    - `P_at_omega`: same as density of states \(N\)
    - `omega_tilde`: energy (frequency)

Notes: The agent must derive all quantities from the given model parameters and momentum using the approximations provided above. The checker will recompute the expected values from the same analytic approximations using the parameters specified in the instruction and compare within tolerance.

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
A hidden verifier independently recomputes the expected values of `P_at_omega` and `omega_tilde` from the same long‑wave analytic approximations and the very same model parameters (\(v_F\), \(\omega\), \(g\), \(N\), \(\mathbf{q}\)) that are provided to you. It compares your submitted values against these reference values using an absolute tolerance. If both quantities fall within the hidden tolerance, you earn full credit for that artifact; the reward degrades as the deviation increases. The final reward is the weighted fraction of the scored outputs that meet the tolerance threshold. Reporting a pre‑existing number without performing the computation yourself will not pass the comparison.
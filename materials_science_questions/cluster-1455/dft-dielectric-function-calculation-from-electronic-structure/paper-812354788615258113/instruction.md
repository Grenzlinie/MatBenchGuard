# TDDFT-LRC Static Dielectric Constant of Silicon

## Problem background
The optical and dielectric properties of semiconductors carry signatures of electron-hole interactions that are often inadequately described by standard approximations in time-dependent density functional theory (TDDFT). A simple adiabatic local-density approximation for the exchange-correlation kernel fails to capture the redistribution of oscillator strength and the intensity of the absorption features observed experimentally in many sp-bonded semiconductors. A computationally light alternative has been proposed that retains only the asymptotic static long-range part of the kernel, and it has been shown to recover a significant portion of the electron-hole attraction while retaining a computational cost comparable to a random-phase approximation calculation. The static electronic dielectric constant \(\varepsilon_\infty\) is a ground-state quantity that is sensitive to the choice of kernel, and evaluating it within this long-range corrected TDDFT approach provides a stringent test of the method and a well-defined numerical target.

## Approach
The workflow follows a sequential **DFT \(\rightarrow\) GW \(\rightarrow\) TDDFT** pipeline. A ground-state calculation within the local-density approximation (LDA) provides Kohn-Sham wavefunctions and eigenvalues for bulk silicon at its theoretical lattice constant. Quasiparticle corrections are then obtained from a GW calculation (or, with justification, a suitable scissor shift) to improve the band energies. Using these corrected eigenvalues together with the Kohn-Sham wavefunctions, the independent-particle response function \(\chi^0\) is constructed. The full density response is then obtained by solving the Dyson equation for \(\chi\) with a static long-range correction to the exchange-correlation kernel of the form \(f_{\mathrm{xc}}(\mathbf{q},\mathbf{G},\mathbf{G}') = -\alpha\,\delta_{\mathbf{G},\mathbf{G}'}/|\mathbf{q}+\mathbf{G}|^2\), where a fixed parameter \(\alpha = 0.2\) is used. From the macroscopic dielectric function derived from the solution, the zero-frequency real part yields the static dielectric constant \(\varepsilon_\infty\). All required codes (plane-wave DFT, GW, and TDDFT linear-response solvers) are available as open-source packages, and the silicon crystal structure is a standard public input. The task compares the computed \(\varepsilon_\infty\) against a hidden reference that corresponds to the value obtained by this approach with the same kernel parameter.

## Reproduction target
Produce the **static dielectric constant \(\varepsilon_\infty\)** of bulk silicon within the TDDFT long-range-correction scheme. The result must be computed from the fully self-consistent solution of \(\chi = \chi^0 + \chi^0 (v + f_{\mathrm{xc}}) \chi\) using the LRC kernel with \(\alpha = 0.2\) and GW-corrected eigenvalues, and it must be written as a JSON record containing the dimensionless scalar. The solution must start from a standard DFT-LDA ground state and a subsequent GW quasiparticle step; shortcuts that skip these stages will not satisfy the required workflow.

## Assets

- DFT code (Quantum ESPRESSO or ABINIT): https://www.quantum-espresso.org
- GW / TDDFT code (Yambo or BerkeleyGW): https://www.yambo-code.eu
- Norm-conserving pseudopotential for Si (e.g., from PseudoDojo): https://www.pseudo-dojo.org

## Workflow steps

### Step 1: DFT-LDA ground state
- Role: process
- Action: Perform a DFT-LDA ground-state calculation for bulk silicon using norm-conserving pseudopotentials and a plane-wave basis (e.g., with Quantum ESPRESSO or ABINIT). Use the theoretical lattice constant and obtain Kohn-Sham wavefunctions and eigenvalues. This generates the starting electronic structure for all subsequent steps.
- Evidence: none

### Step 2: GW quasiparticle energies
- Role: process
- Action: Compute GW quasiparticle corrections (or apply a scissor shift) for silicon starting from the DFT-LDA wavefunctions, using an open‑source GW implementation (Yambo/BerkeleyGW). This step provides the corrected eigenvalues needed for the independent-particle response function.
- Evidence: none

### Step 3: Build independent-particle response function
- Role: process
- Action: Construct the independent-particle response function χ⁰(q,G,G';ω) using DFT-LDA wavefunctions and GW quasiparticle eigenvalues, with an appropriate number of unoccupied bands and k‑point sampling to converge the subsequent optical calculations.
- Evidence: none

### Step 4: TDDFT-LRC and static dielectric constant
- Role: scored (load-bearing)
- Action: Solve the TDDFT linear‑response equation χ = χ⁰ + χ⁰(v + f_xc)χ using the long‑range corrected kernel f_xc(q) = -α/|q|² with α = 0.2. Compute the macroscopic dielectric function ε_M(ω) and evaluate its real part at ω=0 to obtain the static dielectric constant ε∞. Write the result to /app/outputs/epsilon_inf_si.json.
- Output file: `/app/outputs/epsilon_inf_si.json`
- Format: json
- Contract: {"epsilon_inf": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/epsilon_inf_si.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### epsilon_inf_si.json
- path: `/app/outputs/epsilon_inf_si.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Static dielectric constant ε∞ of silicon computed by TDDFT-LRC with α=0.2. The checker compares this value to the hidden reference with a tolerance reflecting legitimate toolchain spread.
- schema:
  - `type`: object
  - `required`:
    - `epsilon_inf`: float
  - `units`:
    - `epsilon_inf`: dimensionless

Notes: The hidden gold is the paper-reported ε∞ = 12.2 (dimensionless). An exact_match with tolerance is used because ε∞ is a fixed physical quantity; the tolerance absorbs differences due to pseudopotential, basis set, and k‑point sampling.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "epsilon_inf_si.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "epsilon_inf": "float"
        },
        "units": {
          "epsilon_inf": "dimensionless"
        }
      },
      "description": "Static dielectric constant ε∞ of silicon computed by TDDFT-LRC with α=0.2. The checker compares this value to the hidden reference with a tolerance reflecting legitimate toolchain spread."
    }
  ],
  "notes": "The hidden gold is the paper-reported ε∞ = 12.2 (dimensionless). An exact_match with tolerance is used because ε∞ is a fixed physical quantity; the tolerance absorbs differences due to pseudopotential, basis set, and k‑point sampling."
}
```

## How you are scored
A hidden verifier inspects the output file `/app/outputs/epsilon_inf_si.json` and reads the `epsilon_inf` value you wrote. It compares that value to an independently reproduced reference for the same physical quantity computed with the same underlying approach and kernel parameter. The score reflects how close your result is to the expected value, with a tolerance that accounts for legitimate spread due to differences in pseudopotentials, basis sets, k-point sampling, and implementation details. Reporting a number without executing the full DFT–GW–TDDFT pipeline will not recover the expected result. The total reward is the score from this single stage.

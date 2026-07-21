# Effective Hamiltonian Model of Tetragonality and Polarization in Ultrathin PbTiO3 Films

## Problem background
The persistence of ferroelectricity in perovskite films only a few unit cells thick is a fundamental question in nanoscale electronics. As film thickness decreases, depolarizing fields arising from incomplete charge screening at the interfaces can suppress the spontaneous polarization. In epitaxial PbTiO₃ films grown on SrTiO₃ substrates, the tetragonality ratio c/a serves as a proxy for the polarization through the strong polarization–strain coupling. This task explores the thickness-dependent behavior of the c/a ratio and spontaneous polarization using a first‑principles effective Hamiltonian model that accounts for a residual depolarizing field. The model enables one to compute, from first principles, whether and how the polarization survives down to 20–24 Å, and whether the tetragonality deviates from the paraelectric elastic limit.

## Approach
The thin‑film effective Hamiltonian is constructed by extending the bulk effective Hamiltonian of Waghmare & Rabe (1997) for PbTiO₃. The bulk model includes a double‑well soft‑mode energy, elastic energy, and a coupling between the soft‑mode amplitude and macroscopic strain. To describe thin films, a depolarizing‑field term is added that couples the polarization to an unscreened depolarizing field, characterized by an effective screening length λ_eff = 0.12 Å. The in‑plane strains are clamped to the SrTiO₃ substrate lattice constant (e_xx = e_yy = (a_STO − a_PTO,cubic)/a_PTO,cubic). The energy functional then depends only on the soft‑mode amplitude ξ_z and the out‑of‑plane strain e_zz. For each film thickness d (20–500 Å, step ≤10 Å), the functional is minimized with respect to ξ_z and e_zz. The spontaneous polarization P_z is obtained as P_z = Z* ξ_z / Ω₀ (using the soft‑mode effective charge Z* and unit cell volume Ω₀ from the bulk parameters). The tetragonality c/a is derived from the optimized strains. Because the bulk Hamiltonian overestimates the polarization–strain coupling, the computed c/a curve is rescaled to match the experimental c/a at 500 Å; the polarization values are not rescaled. All calculations are performed at T = 0.

## Reproduction target
Produce the theoretical c/a ratio versus film thickness and spontaneous polarization versus film thickness curves for an effective screening length λ_eff = 0.12 Å. For each film thickness from 20 to 500 Å (step ≤10 Å), minimise the thin‑film Hamiltonian and compute the c/a ratio and polarization. Write the results to /app/outputs/results.csv with columns: thickness (Å), c/a (dimensionless), polarization_Pz (C/m²). The output must exhibit physically reasonable behavior: the c/a ratio should decrease monotonically as the film becomes thinner, it should remain well above the paraelectric elastic limit, without collapsing to the paraelectric value, at 24 Å, and the polarization at 24 Å should remain nonzero. The verifier will check these structural properties together with a numerical comparison against a hidden reference.

## Assets

- Waghmare & Rabe (1997) effective Hamiltonian parameters for bulk PbTiO3: 10.1103/PhysRevB.55.6161

## Workflow steps

### Step 1: Construct the thin-film effective Hamiltonian
- Role: process
- Action: Implement the energy function for PbTiO3 thin films. Start from the bulk effective Hamiltonian of Waghmare & Rabe (1997), which contains a double-well soft-mode energy, elastic energy, and a coupling term between the soft-mode amplitude and macroscopic strain. Add the depolarizing-field correction that couples the polarization to an unscreened depolarizing field, using the effective screening length λ_eff = 0.12 Å. Fix the in-plane strain to enforce the SrTiO3 substrate constraint: e_xx = e_yy = (a_STO - a_PTO(cubic))/a_PTO(cubic), with a_STO = 3.905 Å and a_PTO(cubic) = 3.969 Å. The resulting Hamiltonian defines the energy as a function of the soft-mode amplitude ξ_z and out-of-plane strain e_zz, and will be minimised in the next step.
- Evidence: none

### Step 2: Run thickness-dependent simulations and produce c/a and polarization curves
- Role: scored (load-bearing)
- Action: For each film thickness d from 20 to 500 Å (step size ≤ 10 Å), minimise the thin-film effective Hamiltonian with respect to the soft-mode amplitude ξ_z and out-of-plane strain e_zz. From the minimised values compute the spontaneous polarization P_z = Z* ξ_z / Ω₀ (where Z* is the soft-mode effective charge and Ω₀ the unit cell volume) and the c/a ratio from the obtained strains (using the fixed in-plane strain). Then rescale the computed c/a curve such that at d = 500 Å the value equals 1.068, to remove the bulk overestimation of the Hamiltonian. Write the results to /app/outputs/results.csv with columns: thickness (Å), c/a (dimensionless), polarization_Pz (C/m²).
- Output file: `/app/outputs/results.csv`
- Format: csv
- Contract: columns: thickness (float, unit Å), c/a (float, dimensionless), polarization_Pz (float, unit C/m²)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.csv
- path: `/app/outputs/results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: The predicted thickness dependence of the tetragonality ratio and spontaneous polarization from the effective Hamiltonian model with depolarizing field correction and rescaling. The checker compares these values against a hidden reference implementation at a set of hidden thicknesses, also verifying monotonic decay of c/a and nonzero polarization down to 24 Å.
- schema:
  - `type`: table
  - `required_columns`: `thickness`, `c/a`, `polarization_Pz`
  - `units`:
    - `thickness`: Å
    - `c/a`: dimensionless
    - `polarization_Pz`: C/m²

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "thickness",
          "c/a",
          "polarization_Pz"
        ],
        "units": {
          "thickness": "Å",
          "c/a": "dimensionless",
          "polarization_Pz": "C/m²"
        }
      },
      "description": "The predicted thickness dependence of the tetragonality ratio and spontaneous polarization from the effective Hamiltonian model with depolarizing field correction and rescaling. The checker compares these values against a hidden reference implementation at a set of hidden thicknesses, also verifying monotonic decay of c/a and nonzero polarization down to 24 Å."
    }
  ],
  "notes": ""
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that reads /app/outputs/results.csv. The verifier compares your computed c/a and polarization values at a set of hidden thicknesses against reference values obtained from a trusted implementation of the same model, using tolerances on c/a and polarization. Additionally, it checks structural invariants: (i) c/a monotonically decreases with decreasing thickness, (ii) c/a at 24 Å is above the paraelectric elastic limit (~1.03), and (iii) polarization at 24 Å exceeds a small threshold. The final reward is a weighted combination of the numerical accuracy and the structural checks. Reporting the paper’s numbers without genuine computation will not satisfy these checks.

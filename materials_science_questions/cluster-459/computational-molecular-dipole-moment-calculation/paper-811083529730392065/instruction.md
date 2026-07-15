## Problem background

Second-harmonic generation (SHG) in push-pull polyenes is a key property for designing organic nonlinear optical (NLO) materials. Reliable predictions of molecular hyperpolarizabilities require a correlated-electron description that goes beyond mean-field theories. This task computes model-exact SHG coefficients for a series of all-trans di‑substituted polyenes within the Pariser–Parr–Pople (PPP) π‑electron Hamiltonian. The calculation uses full configuration interaction in a complete spin‑adapted valence‑bond (VB) basis and solves the first‑order linear‑response equations directly, without truncation of excited states. The results provide accurate benchmarks for the NLO response and its dependence on push‑pull strength, substitution position, chain length, and backbone twist.

## Approach

The underlying model is the PPP Hamiltonian for the π electrons of a conjugated polyene. Each carbon atom contributes one p_z orbital. The Hamiltonian consists of a non‑interacting Hückel part plus on‑site Hubbard U and inter‑site Ohno‑parametrized Coulomb repulsions V_{pp'}. Electron‑electron interactions are treated exactly by working in the complete spin‑adapted VB singlet space.

The ground state is obtained by exact full CI (direct diagonalisation of the Hamiltonian matrix). The first‑order perturbed wavefunctions φ^{(1)} are then computed by solving the inhomogeneous linear equation
(Ĥ − E_G − ħΩ) φ_i^{(1)}(Ω) = − μ̂_i φ_G^{(0)}
in the same full VB space, using a conjugate gradient algorithm. From φ^{(1)} the SHG tensor components β_{ijk} are evaluated via the direct‑response formula
β_{ijk}(Ω₁,Ω₂) = P ⟨φ_i^{(1)}(−Ω₁,−Ω₂)| μ̂_j | φ_k^{(1)}(−Ω₂)⟩ / 8,
and the tumbling‑averaged β_x is obtained from the appropriate combination of tensor components (including β_xzz for twisted geometries). The charge‑transfer (CT) excited state is identified from the eigenvalue spectrum, and the two‑state model SHG coefficient β^CT is computed for comparison. The size‑scaling exponent α is extracted from a log‑log fit of β_x versus chain length.

The procedure is repeated for the following conditions:
- Chain lengths N = 4, 6, 8, 10 with terminal push‑pull groups (sites 1 and N) at push‑pull strengths ε = 0.6 eV and 2.0 eV.
- All terminal‑pair substitution patterns on hexatriene (N=6) at ε = 2.0 eV.
- Hexatriene (N=6, ε = 2.0 eV) twisted about the central double bond for twist angles 0°, 15°, 30°, … , 165°, 180°.
- CT excitation gaps for N = 6, 8, 10 at ε = 0.4, 0.6, 0.8, 1.0, 1.5, 2.0 eV.

All numerical values are output in a single structured JSON file.

## Reproduction target

Produce a JSON file containing:
- charge‑transfer excitation gaps (eV) for varying chain length N and push‑pull strength ε;
- the tumbling‑averaged β_x (a.u.) and ground‑/excited‑state dipole moments (D) for all substitution positions of hexatriene at ε = 2.0 eV;
- the tumbling‑averaged β_x and two‑state β^CT (a.u.) for terminal‑substituted chains N = 4, 6, 8, 10 at ε = 0.6 and 2.0 eV;
- β_x versus twist angle for hexatriene at ε = 2.0 eV;
- the size‑scaling exponent α (dimensionless) for β_x at ε = 0.6 and 2.0 eV.

The hidden verifier checks each numeric field against reference values with appropriate tolerances and performs a structural check on the twist dependence (peak near 75° and 105°, minimum at 90°).

## Assets

- **NumPy** – array computing library. Obtain from PyPI: `numpy` (https://pypi.org/project/numpy/).
- **SciPy** – scientific computing library (sparse linear algebra, conjugate gradient). Obtain from PyPI: `scipy` (https://pypi.org/project/scipy/).

There are no external datasets, models, or proprietary tools required. All necessary model parameters are given below.

## Workflow steps

### Step 1: Build molecular systems and valence-bond basis
- Role: process
- Action: Generate the all‑trans polyene geometries (carbon coordinates) for chain lengths N = 4, 6, 8, 10. For the twist study, construct hexatriene with a rotatable central double bond. Place carbon atoms along the molecular axis with a uniform C–C spacing of 1.397 Å (a standard value for π‑conjugated systems). For twisted geometries, rotate the appropriate molecular fragment by the given twist angle θ and adjust the resonance integral of the central bond to t₀(1+δ) cos θ. Assign site energies: ε_p = +ε at the “pull” substitution site and ε_p = −ε at the “push” site, with the required ε values; all other sites have ε_p = 0. Construct the complete spin‑adapted valence‑bond basis for the singlet manifold for each system.
- Evidence: `/app/outputs/system_info.json`

### Step 2: Solve ground state via exact full configuration interaction
- Role: process
- Action: Build the PPP Hamiltonian matrix in the VB basis using the Ohno parametrization for inter‑site repulsions: V_{pp'} = 14.397 (1.6348 + r_{pp'}^2)^{-½} eV, where r_{pp'} is the distance in Å between carbon sites p and p'. Use the on‑site Hubbard U = 11.13 eV (if not obtainable from the Ohno formula at r=0) and the Hückel parameters t₀ = 2.4 eV, δ = 0.07. Diagonalise the Hamiltonian to obtain the ground‑state wavefunction φ_G^(0) and the full eigenvalue spectrum for every required system (all chain lengths, push‑pull strengths, substitution patterns, and twist angles).
- Evidence: `/app/outputs/eigenvalues.json`

### Step 3: Compute first‑order perturbed wavefunctions
- Role: process
- Action: For each system, construct the dipole displacement operator μ̂_i (i = x, y, z) using the carbon coordinates and the elementary charge e. For every required combination of ε, Ω (static and 1.167 eV), and dipole component, solve the inhomogeneous linear equation
(Ĥ − E_G − ħΩ) φ_i^(1)(Ω) = − μ̂_i φ_G^(0)
in the full VB singlet space using the conjugate gradient algorithm. Store the resulting perturbed wavefunctions needed for the SHG evaluation.
- Evidence: none

### Step 4: Compute SHG coefficients and output final results (load-bearing)
- Role: scored (load-bearing)
- Action: From the perturbed wavefunctions, evaluate the SHG tensor components β_{ijk} via the direct‑response formula and obtain the tumbling‑averaged β_x for each condition. From the eigenvalue spectrum and the dipole matrix elements, extract charge‑transfer excitation gaps E_CT, ground‑ and CT‑state dipole moments, and compute the two‑state model β^CT using the Oudar–Chemla formula. Perform a log‑log fit of β_x vs chain length L to obtain the size‑scaling exponent α for ε = 0.6 and 2.0 eV. Write all results (table1_CT_gaps, table2_position_dependence, table4_beta_exact, twist_dependence, alpha_exponent) to shg_results.json.
- Output file: `/app/outputs/shg_results.json`
- Format: json
- Contract: exact schema as defined in the output contract
- Scoring: scored by hidden verifier

## Output files

- `/app/outputs/system_info.json` (optional evidence)
- `/app/outputs/eigenvalues.json` (optional evidence)
- `/app/outputs/shg_results.json` (scored)

The scored artifact is `/app/outputs/shg_results.json`. It must be written even if intermediate evidence files are omitted.

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### shg_results.json
- path: `/app/outputs/shg_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Scored artifact containing the model-exact SHG coefficients, CT gaps, dipole moments, twist dependence, and size-scaling exponent.
- schema:
  - `type`: object
  - `required`:
    - `table1_CT_gaps`: array of {N:int, epsilon:float, CT_gap:float}
    - `table2_position_dependence`: array of {position:str, beta_x_exact:float, mu_gr:float, mu_ex:float}
    - `table4_beta_exact`: object with keys '4','6','8','10', each value object with keys 'eps0.6','eps2.0', each containing {beta_exact:float, beta_CT:float}
    - `twist_dependence`: array of {theta:int, beta_x_exact:float}
    - `alpha_exponent`: object with keys '0.6','2.0', values float
  - `description`: SHG coefficients and related quantities. All β values in atomic units (a.u.), energies in eV, dipole moments in Debye (D), α dimensionless.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "shg_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "table1_CT_gaps": "array of {N:int, epsilon:float, CT_gap:float}",
          "table2_position_dependence": "array of {position:str, beta_x_exact:float, mu_gr:float, mu_ex:float}",
          "table4_beta_exact": "object with keys '4','6','8','10', each value object with keys 'eps0.6','eps2.0', each containing {beta_exact:float, beta_CT:float}",
          "twist_dependence": "array of {theta:int, beta_x_exact:float}",
          "alpha_exponent": "object with keys '0.6','2.0', values float"
        },
        "description": "SHG coefficients and related quantities. All β values in atomic units (a.u.), energies in eV, dipole moments in Debye (D), α dimensionless."
      },
      "description": "Scored artifact containing the model-exact SHG coefficients, CT gaps, dipole moments, twist dependence, and size-scaling exponent."
    }
  ],
  "notes": ""
}
```

## How you are scored

A hidden verifier independently reads your `/app/outputs/shg_results.json` and compares each numeric field against reference values (the paper’s reported model‑exact results) and expected structural trends. The overall reward is a weighted combination of per‑field accuracy. Reporting a paper number without performing the computation will not pass the structural and consistency checks.

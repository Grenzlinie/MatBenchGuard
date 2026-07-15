# Atom-in-Jellium Cohesive Energy and Elastic Properties: LDA vs GGA-PW91 Comparison

## Problem background
The bonding properties of atoms in solids can be studied within the atom-in-jellium model: a single atom is embedded in a homogeneous electron gas (jellium) that approximates the extended valence states of a solid environment. Density-functional theory (DFT) provides the ground-state total energies, and the exchange-correlation (XC) part must be approximated. Two widely used approximations are the local-density approximation (LDA) and the generalized-gradient approximation of Perdew et al. (GGA-PW91). LDA uses only the local electron density, which leads to systematic overbinding of atoms in molecules and solids. GGA-PW91 additionally accounts for the density gradient, aiming to correct that overbinding. By computing the immersion energy of the atom as a function of the embedding density and adding an electrostatic attraction term, one obtains a cohesive-energy curve whose minimum yields the cohesive energy, the corresponding neutral-sphere radius, and the bulk modulus (from the curvature). Performing these calculations for elements from hydrogen to zinc (excluding noble gases) with both LDA and GGA-PW91 provides a quantitative characterisation of how the XC approximation affects bonding properties in this simplified model of solids.

## Approach
The core workflow is a series of DFT calculations that yield a set of cohesive parameters for each element and each XC functional. For every element (H to Zn, excluding He, Ne, Ar):

- Compute the total energy of the free atom using spin-polarized DFT.
- Perform self-consistent Kohn-Sham calculations for the atom embedded in a homogeneous electron gas at a range of embedding densities, using spin-compensated DFT.
- From the immersion energy (the difference between the embedded atom + jellium system and the separated subsystems) and the electrostatic attraction between the atom and the jellium, construct the cohesive energy as a function of embedding density.
- Locate the minimum of this cohesive energy curve; the minimum value is the cohesive energy E0, and the embedding density at the minimum is n0.
- The neutral-sphere radius s0 is derived through an exponential relation linking the neutral radius to the embedding density. Specifically, the embedding density at a neutral radius s is well approximated by n0 * exp(-η (s - s0)), which is inverted at the cohesive minimum to obtain s0.
- The bulk modulus B is computed from the curvature of the cohesive energy curve at the minimum, using the standard relation between B and the second derivative of the cohesive energy with respect to the neutral sphere volume.

All calculations are carried out with both the LDA and GGA-PW91 functionals, using an open-source DFT solver capable of performing spin-polarized free-atom calculations and spin-compensated embedded-atom calculations. The resulting parameters—E0, s0, and B—are compiled into a single output file. No external datasets are required; the problem is fully defined by the atomic numbers of the target elements and the two XC functionals.

## Reproduction target
For all elements from hydrogen to zinc (excluding the noble gases helium, neon, and argon), compute the following EMT parameters with both the LDA and GGA-PW91 exchange-correlation functionals:

- Minimum cohesive energy $E_0$ (eV)
- Optimum embedding density $n_0$ (a.u.)
- Neutral-sphere radius $s_0$ (Bohr radii, $a_0$)
- Atom-induced electrostatic potential $\alpha$ (a.u.)
- Quadratic and cubic cohesive-function fitting parameters $E_2$, $E_3$ (eV)
- Exponential density parameters $\eta$, $\eta_1$, $\eta_2$ (dimensionless)
- Bulk modulus $B$ (GPa)

The results must be written to a CSV table with one row per (element, functional) pair (60 rows total), containing the columns: element, functional (exactly 'LDA' or 'GGA-PW91'), E0_eV, n0, s0_a0, alpha, E2, E3, eta, eta1, eta2, B_GPa. The purpose is to provide a complete numerical record of the basic EMT parameters derived from the atom-in-jellium model.

## Assets

- GPAW (or other open-source DFT solver supporting LDA and GGA-PW91): https://wiki.fysik.dtu.dk/gpaw/

## Workflow steps

### Step 1: Atom-in-jellium calculations and parameter extraction
- Role: scored (load-bearing)
- Action: For each element from H to Zn (excluding He, Ne, Ar) and for both LDA and GGA-PW91 functionals: (1) Compute free-atom total energy using spin-polarized DFT. (2) Perform self-consistent Kohn-Sham calculations for the atom embedded in a homogeneous electron gas at a range of embedding densities. (3) From the immersion energy and the electrostatic attraction between the atom and the jellium, obtain the cohesive energy $E_c(\bar{n}) = \Delta E^{\mathrm{hom}}(\bar{n}) - \alpha(\bar{n})\bar{n}$. (4) Locate the minimum cohesive energy $E_0$ and the corresponding optimum embedding density $n_0$; extract the electrostatic parameter $\alpha$ evaluated at the minimum (or an averaged value). (5) Determine the neutral-sphere radius $s_0$ from the relation $\bar{n}(s) = n_0 \exp[-\eta (s - s_0)]$ using $\bar{n}=n_0$ at $s=s_0$, and compute the exponential parameters $\eta$, $\eta_1$, $\eta_2$ from the induced density tail. (6) Fit the cohesive function to the polynomial form $E_c(\bar{n}) = E_0 + E_2 ((\bar{n}/n_0)-1)^2 + E_3 ((\bar{n}/n_0)-1)^3$ to obtain $E_2$ and $E_3$. (7) Compute the bulk modulus $B$ from the curvature via $B = \frac{E_2 \eta^2}{6\pi s_0}$ (Eq. 15). (8) Compile all parameters into the output CSV.
- Output file: `/app/outputs/step_01_results.csv`
- Format: csv
- Contract: Columns: element (string), functional (string: 'LDA' or 'GGA-PW91'), E0_eV (float, eV), n0 (float, a.u.), s0_a0 (float, Bohr radius), alpha (float, a.u.), E2 (float, eV), E3 (float, eV), eta (float, dimensionless), eta1 (float, dimensionless), eta2 (float, dimensionless), B_GPa (float, GPa). One row per (element, functional) combination, 60 rows total, sorted by atomic number then functional.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_results.csv
- path: `/app/outputs/step_01_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Cohesive energy minima, optimum embedding density, neutral-sphere radii, electrostatic potential, cohesive-function fitting parameters, exponential density parameters, and bulk modulus computed for 30 elements with LDA and GGA-PW91.
- schema:
  - `type`: table
  - `required_columns`: `element`, `functional`, `E0_eV`, `n0`, `s0_a0`, `alpha`, `E2`, `E3`, `eta`, `eta1`, `eta2`, `B_GPa`
  - `units`:
    - `E0_eV`: eV
    - `n0`: a.u.
    - `s0_a0`: a0
    - `alpha`: a.u.
    - `E2`: eV
    - `E3`: eV
    - `eta`: dimensionless
    - `eta1`: dimensionless
    - `eta2`: dimensionless
    - `B_GPa`: GPa

Notes: The checker verifies agreement with hidden gold values and checks required physical trends without revealing them.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "element",
          "functional",
          "E0_eV",
          "n0",
          "s0_a0",
          "alpha",
          "E2",
          "E3",
          "eta",
          "eta1",
          "eta2",
          "B_GPa"
        ],
        "units": {
          "E0_eV": "eV",
          "n0": "a.u.",
          "s0_a0": "a0",
          "alpha": "a.u.",
          "E2": "eV",
          "E3": "eV",
          "eta": "dimensionless",
          "eta1": "dimensionless",
          "eta2": "dimensionless",
          "B_GPa": "GPa"
        }
      },
      "description": "Cohesive energy minima, optimum embedding density, neutral-sphere radii, electrostatic potential, cohesive-function fitting parameters, exponential density parameters, and bulk modulus computed for 30 elements with LDA and GGA-PW91."
    }
  ],
  "notes": "The checker verifies agreement with hidden gold values and checks required physical trends without revealing them."
}
```

## How you are scored
A hidden verifier independently inspects each workflow output artifact. It compares your computed E0, s0, and B values to expected reference values using predefined tolerances and structural trend checks (for example, verifying the relative ordering of GGA vs LDA values across the element series). The reward is monotonic in quality: results that are closer to the reference and that satisfy the required structural relationships earn higher credit. The exact tolerances, reference values, and trend checks are not disclosed; they are designed to accept physically meaningful answers produced by an honest re-implementation of the prescribed procedure. Reporting a number known from the literature is insufficient—you must produce the artifact through the specified calculation steps.

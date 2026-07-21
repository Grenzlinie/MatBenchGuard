# Computational study of CO2 adsorption on NaCl(100) surface

## Problem background
Understanding the adsorption of small molecules on ionic crystal surfaces is important for catalysis and surface science. This task investigates the adsorption of a CO₂ molecule on the (100) face of sodium chloride (NaCl). The interaction is governed by a combination of electrostatic, polarization, and dispersion-repulsion contributions. Different theoretical models—hard-sphere, softened pair potentials, and a cluster approach—have been used to describe this system. The goal is to compute the total adsorption energy and the vibrational frequency shifts of the ν₂ bending mode of CO₂ upon adsorption, and to compare the predictions of the three models.

## Approach
The NaCl(100) surface is modeled as a point-charge array of ±1 e charges located at the lattice sites of a 7×7×4 slab (NaCl lattice constant 2.814 Å). The CO₂ molecule (linear, C–O bond length 1.162 Å) is treated at the ab initio SCF level with the STO‑6G basis set. The electrostatic and polarization contribution to the adsorption energy, Δ_SCF, is obtained from SCF calculations of CO₂ placed in the external field of the point charges. The dispersion-repulsion term Δ_DR is added via a semi-empirical pair potential:

```
V_DR = – Σ (A^MN / R⁶) (1 – B / R⁶)
```

with A^MN = (3/2) [I_M I_N / (I_M + I_N)] α_M α_N, and B defined differently for each model. The required atomic parameters (ionization energies I, polarizabilities α, van der Waals radii R₀) are listed below:

| Atom/Ion | I (eV) | α (Å³) | R₀ (Å) |
|----------|--------|--------|--------|
| C        | 11.3   | 2.10   | 1.30   |
| O        | 13.61  | 0.89   | 1.40   |
| Na⁺      | 47     | 0.2    | 0.95   |
| Cl⁻      | 3.6    | 3.0    | 1.81   |

(Use these values to compute the London dispersion coefficients and repulsion parameters.)

Three models are considered:
- **Hard-sphere model (A₁):** B = ½ (R₀^MN)⁶ for R ≥ R₀^MN; repulsion is infinite for R < R₀^MN. The molecule–surface distance is fixed at the values given in the workflow steps.
- **Softened model (A₂):** B = ½ (λ R₀^MN)⁶ with a common softening parameter λ. For each λ, the distance z is optimized by minimizing the total energy.
- **Cluster model (B):** the (CO₂Cl₂)²⁻ cluster (charge –2, spin multiplicity 1, i.e. singlet) is treated in the field of the remaining point charges; the Cl⁻ ions are included explicitly in the SCF calculation. The position of the CO₂ molecule above the surface is optimized.

**Molecule–surface distance definition (z).** For all models, the z coordinate is defined as the distance from the plane of the surface ion nuclei (z = 0 Å) to the nucleus of the adsorbate atom that is closest to the surface:
- *Perpendicular orientation (case I):* the closest atom is the oxygen facing the surface; z is the distance from the surface plane to that oxygen nucleus.
- *Parallel orientation (case II):* all atoms of the linear CO₂ lie in a plane parallel to the surface, so the distance from the surface plane to any of the three nuclei is the same; z is that common distance.

**Vibrational analysis (non‑harmonic treatment).** The shifts of the ν₂ bending mode are obtained by constructing a one‑dimensional bending potential for both the in‑plane (ν_parallel) and out‑of‑plane (ν_perp) modes, including anharmonicity. The method is:
- For each model and each mode, generate a set of distorted geometries along the corresponding normal coordinate q (mass‑weighted displacement in Å·√(amu)).
- Compute the SCF energy for each distorted geometry, giving a potential curve V(q).
- Fit V(q) to a polynomial V(q) = ½ ω_h q² + γ q⁴, where ω_h is the harmonic frequency (in cm⁻¹) obtained from a separate harmonic frequency calculation (or from the quadratic fit coefficient). The coefficient ω_h must be converted to energy units consistent with q.
- Solve the one‑dimensional nuclear Schrödinger equation:
  ```
  (–ħ²/(2) d²/dq² + V(q)) ψ(q) = E ψ(q)
  ```
  numerically (e.g., with the Numerov algorithm) on a uniform grid of q, using the effective reduced mass μ = 1 (since q is mass‑weighted). Obtain the ground‑state energy E₀ and the first excited‑state energy E₁; the anharmonic vibrational frequency is ν = (E₁ – E₀) / (h c) in cm⁻¹.
- Apply exactly the same procedure to the isolated CO₂ molecule to obtain the reference ν₂ (gas‑phase) frequency, which should be consistent with the published STO‑6G value of approximately 601 cm⁻¹ (the exact value will depend on the computational details).

The necessary effective harmonic frequencies and the normal‑mode vectors can be obtained from an SCF frequency calculation (hessian) on the isolated molecule and on the adsorbate/substrate systems. When building the potential scan, displace the equilibrium geometry along each normal mode by multiples of a suitable step (e.g. Δq = 0.1 √amu Å) over the range –0.5 to +0.5, compute energies, and fit.

All SCF calculations use the STO‑6G basis set, as supplied by the Psi4 quantum chemistry package.

## Reproduction target
Produce the following files under `/app/outputs`:

- `point_charges.txt` – a human‑readable description of the 7×7×4 point‑charge array (one line per charge, containing ion type, coordinates in Å and charge in e).
- `iso_co2_energy.txt` – the total SCF energy (in Hartree) of the isolated CO₂ molecule together with the basis set and geometry used.
- `adsorption_energies.csv` – total adsorption energy Δ and equilibrium distance (if optimized) for all required cases.
- `vibrational_shifts.csv` – ν₂ frequency shifts (ν_perp–ν₂, ν_parallel–ν₂, ν_perp–ν_parallel, in cm⁻¹) for models A₁, A₂ (λ=1.26) and B.

The CSV files must follow the schema exactly as described in the workflow steps and the output contract below.

## Assets

- Psi4 quantum chemistry package: https://psicode.org/
- Python with NumPy and SciPy: `pip install numpy scipy`

## Workflow steps

### Step 1: Build point-charge slab model
- Role: process
- Action: Construct a 7×7×4 array of point charges (±1 e) at NaCl lattice sites with the NaCl lattice constant d+− = 2.814 Å, representing the (100) surface. The array is defined such that the (100) plane is the surface, with ions occupying a square grid (alternating Na⁺ and Cl⁻) in each layer. The exact ionic positions can be taken from the NaCl rocksalt structure: lattice vectors (d,0,0), (0,d,0), (0,0,d) with d = 2.814 Å. Use the standard convention where Na⁺ occupies the (0,0,0) corner and Cl⁻ occupies (d/2,0,0) etc. in the bulk, but for the surface layer place a Na⁺ at the origin and Cl⁻ at (d/2, d/2, 0) to have the usual (100) termination. (The sign convention does not affect the results as long as the alternation is correct.)
- Evidence: `/app/outputs/point_charges.txt` – write one line per point charge with columns: `type, x, y, z, charge`, where type is Na or Cl, coordinates in Å, charge in e (±1).

### Step 2: Isolated CO₂ SCF reference calculation
- Role: process
- Action: Perform a single‑point SCF calculation on an isolated CO₂ molecule (C–O bond length 1.162 Å, linear) using the STO‑6G basis set to obtain the reference total energy E_isolated (in Hartree), needed for Δ_SCF.
- Evidence: `/app/outputs/iso_co2_energy.txt` – write the SCF total energy on the first line; subsequent lines may contain the geometry and basis set information.

### Step 3: Compute adsorption energies for all models
- Role: scored (load‑bearing)
- Action: Using the point‑charge substrate and the isolated CO₂ reference energy, compute the total adsorption energy Δ = Δ_SCF + Δ_DR.
  - Δ_SCF = E(CO₂ in the field) – E_isolated, where E(CO₂ in the field) is the SCF energy of the CO₂ molecule (always with the same internal geometry: linear, d(C–O)=1.162 Å, unless otherwise stated) placed in the array of point charges. For model B, the SCF calculation includes the two explicit Cl⁻ ions and the remaining point charges.
  - Δ_DR is computed by summing the pairwise London‑repulsion potential over all CO₂‑atom/Na⁺ and CO₂‑atom/Cl⁻ pairs, using the parameters in the table. For R < R₀^MN in the hard‑sphere model, Δ_DR is set to +∞ (i.e. the configuration is excluded), but in practice the hard‑sphere distances provided are already ≥ R₀^MN.

  **Specific calculations required:**
  - **A₁ perpendicular (site 1):** Place CO₂ perpendicular to the surface above a Na⁺ ion, with the bottom oxygen at distance z = 2.35 Å from the plane of the surface nuclei (i.e. the oxygen nucleus at z=2.35 Å). The carbon lies directly above the Na⁺ at z=2.35 + 1.162 = 3.512 Å, and the top oxygen at z=4.674 Å. Compute Δ.
  - **A₁ parallel (site 2):** Place CO₂ parallel to the surface above a Na⁺–Na⁺ alignment, with the carbon atom above the centre of a Na₂Cl₂ square. The molecule–surface distance is z = 2.336 Å for all atoms. The CO₂ axis is oriented along the line connecting two surface Na⁺ ions. Compute Δ.
  - **A₂ parallel (site 2):** For λ ∈ {1.1, 1.2, 1.26, 1.3}, minimize the total energy Δ(z) with respect to z (the common distance of the molecule from the surface) by varying z and recomputing Δ_SCF and Δ_DR at each z. The internal geometry remains linear. Report the equilibrium z_m and the corresponding Δ.
  - **B cluster (parallel, site 2):** Construct the cluster (CO₂Cl₂)²⁻ by taking the CO₂ molecule in the parallel orientation (site 2) and adding the two nearest Cl⁻ ions from the surface layer as explicit atoms. The selection of the two Cl⁻ ions is based on their distance to the CO₂ atoms: identify the two surface Cl⁻ ions that are closest to any atom of the CO₂ molecule. Place these Cl⁻ ions at their bulk‑terminated positions (z=0) while the rest of the surface ions remain point charges. The cluster has total charge –2 and spin multiplicity 1 (singlet). Perform SCF calculations with the explicit Cl⁻ basis sets (STO‑6G for Cl) and the external point‑charge field (excluding the two explicit Cl⁻ from the point‑charge list to avoid double counting). Minimize the total energy with respect to z (the distance of the CO₂ molecule from the surface; the CO₂ internal geometry may also be allowed to relax, but note that the C–O bond length is expected to stay near 1.162 Å). At each step, recompute Δ_SCF as E(cluster+field) – (E(CO₂_isolated) + 2×E(Cl⁻_isolated)? Actually the reference energy is the isolated cluster's SCF energy, but the paper defines Δ as the adsorption energy relative to free CO₂ + substrate. For consistency, evaluate Δ by the same formula Δ = Δ_SCF + Δ_DR, where Δ_SCF is the energy difference between the cluster in the field and the isolated CO₂ + isolated Cl⁻ ions at infinite separation. For simplicity, you can take Δ_SCF = E(cluster+field) – E(CO₂_isolated) – 2×E(Cl⁻_isolated), where E(Cl⁻_isolated) is the SCF energy of a single Cl⁻ ion (also STO‑6G). The Δ_DR contribution for model B is not included because the explicit treatment of the neighbouring Cl⁻ already accounts for short‑range repulsion; follow the original paper: the cluster model total adsorption energy is simply the SCF‑derived Δ_SCF + a possible dispersion term? Actually from the paper: "The adsorption energy appears as Δ = Δ_SCF + Δ_DR" for all models. In the cluster model B, the SCF term includes the electrostatic and polarization contributions, and the Δ_DR is still added between the atoms of the adsorbate and the rest of the crystal ions (the point charges). But here the substrate is simulated by point charges and two explicit Cl⁻; the dispersion‑repulsion is between CO₂ atoms and the remaining point‑charge ions. So evaluate Δ_DR using only the CO₂ atoms and the point‑charge ions (excluding the two explicit Cl⁻ from the pair sums). Sum Δ_SCF and Δ_DR to get Δ. Minimise Δ with respect to z (and possibly internal coordinates). Report the final equilibrium z (distance to the surface) and Δ.
- Output file: `/app/outputs/adsorption_energies.csv`
- Format: csv
- Contract: Columns: Model (string, one of A1, A2, B), Orientation (string, 'perpendicular' or 'parallel'), Site (string, site label, e.g. "1" or "2"), Lambda (float or empty), z_equilibrium (float, Å), AdsorptionEnergy (float, kcal/mol). Required rows as listed in the output contract.
- Scoring: scored by hidden verifier

### Step 4: Compute ν₂ vibrational frequency shifts
- Role: scored
- Action: For each model (A₁, A₂ with λ=1.26, B), determine the anharmonic vibrational frequencies of the two bending modes of adsorbed CO₂.
  1. **Obtain the harmonic normal modes and frequencies.** Using the equilibrium geometry from the previous step, perform a harmonic frequency calculation (hessian) with the same SCF level (STO‑6G, point charges or explicit ions as appropriate). The CO₂ molecule has two degenerate bending modes in gas phase; under the surface field they split into in‑plane (ν_parallel) and out‑of‑plane (ν_perp). Identify the two modes from the displacement vectors.
  2. **Construct 1D bending potentials.** For each mode, keep all other coordinates fixed at equilibrium and displace the molecule along the normal coordinate q (mass‑weighted, in Å·√amu). Use the displacement vectors obtained from the harmonic calculation. Generate a series of displaced geometries q = –0.5, –0.4, …, +0.5. Compute single‑point SCF energies for each, subtract the equilibrium energy to obtain V(q). (Use a finer grid if needed.)
  3. **Fit to polynomial.** Fit V(q) to a quartic polynomial V(q) = c₂ q² + c₄ q⁴. (The linear and cubic terms should be zero by symmetry for the bending modes.) The coefficient c₂ is related to the harmonic frequency ω_h via c₂ = ½ ω_h² (in appropriate units; note that c₂ has dimension energy/(mass‑weighted length²) and ω_h is in energy units when q is mass‑weighted). Alternatively, use the harmonic frequency directly from the frequency calculation to fix the quadratic coefficient and fit only the quartic term.
  4. **Solve the 1D Schrödinger equation.** Use a numerical solver (e.g. Numerov method with a uniform grid of N points, Δq step, and particle mass μ = 1 amu⁻¹ · (ħ²) scaling). Set up the Hamiltonian:
     ```
     H = –(ħ²/(2μ)) d²/dq² + V(q)
     ```
     Since q is mass‑weighted, the kinetic energy operator simplifies to –½ d²/dq² (in atomic units). Solve for the lowest two eigenvalues E₀ and E₁ (the zero‑point energy and the first excited state). The anharmonic transition frequency is ν = (E₁ – E₀) / h c in cm⁻¹.
  5. **Compute shifts.** Perform the same procedure for the isolated CO₂ molecule (with its own harmonic modes) to obtain the gas‑phase ν₂ anharmonic frequency. Then for each mode: ν_perp – ν₂, ν_parallel – ν₂, ν_perp – ν_parallel.
  6. **Output results.**
- Output file: `/app/outputs/vibrational_shifts.csv`
- Format: csv
- Contract: Columns: Model (string, A1, A2, B), nu_perp_minus_nu2 (float, cm⁻¹), nu_parallel_minus_nu2 (float, cm⁻¹), nu_perp_minus_nu_parallel (float, cm⁻¹).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/point_charges.txt`
- `/app/outputs/iso_co2_energy.txt`
- `/app/outputs/adsorption_energies.csv`
- `/app/outputs/vibrational_shifts.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### point_charges.txt
- path: `/app/outputs/point_charges.txt`
- format: txt
- purpose: process
- description: Text file describing the constructed 7×7×4 point‑charge array used in the SCF calculations. Each line lists ion type (Na/Cl), x, y, z (Å) and charge (±1 e).

### iso_co2_energy.txt
- path: `/app/outputs/iso_co2_energy.txt`
- format: txt
- purpose: process
- description: Total SCF energy of the isolated CO₂ molecule in Hartree.

### adsorption_energies.csv
- path: `/app/outputs/adsorption_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Adsorption energies and equilibrium distances for CO₂ on NaCl(100) computed with three models (A₁ hard‑sphere, A₂ softened, B cluster).
- schema:
  - `type`: table
  - `required_columns`: `Model`, `Orientation`, `Site`, `Lambda`, `z_equilibrium`, `AdsorptionEnergy`
  - `units`:
    - `z_equilibrium`: Angstrom
    - `AdsorptionEnergy`: kcal/mol
  - `column_descriptions`:
    - `Model`: Model identifier (A1, A2, B)
    - `Orientation`: perpendicular or parallel
    - `Site`: Surface site label (e.g. "1", "2")
    - `Lambda`: Softening parameter (empty for A1 and B)
    - `z_equilibrium`: Equilibrium molecule–surface distance (as defined in Approach)
    - `AdsorptionEnergy`: Total adsorption energy

### vibrational_shifts.csv
- path: `/app/outputs/vibrational_shifts.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Vibrational frequency shifts for the ν₂ bending mode of CO₂ adsorbed on NaCl(100).
- schema:
  - `type`: table
  - `required_columns`: `Model`, `nu_perp_minus_nu2`, `nu_parallel_minus_nu2`, `nu_perp_minus_nu_parallel`
  - `units`:
    - `nu_perp_minus_nu2`: cm⁻¹
    - `nu_parallel_minus_nu2`: cm⁻¹
    - `nu_perp_minus_nu_parallel`: cm⁻¹
  - `column_descriptions`:
    - `Model`: Model identifier (A1, A2, B)
    - `nu_perp_minus_nu2`: Shift of out‑of‑plane bending frequency relative to gas‑phase ν₂
    - `nu_parallel_minus_nu2`: Shift of in‑plane bending frequency relative to gas‑phase ν₂
    - `nu_perp_minus_nu_parallel`: Frequency splitting

## Self-check before finishing (optional, not scored)
… (the existing self‑check JSON can stay unchanged) …
```json
{
  "outputs": [
    {
      "file": "adsorption_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Model",
          "Orientation",
          "Site",
          "Lambda",
          "z_equilibrium",
          "AdsorptionEnergy"
        ],
        "units": {
          "z_equilibrium": "Angstrom",
          "AdsorptionEnergy": "kcal/mol"
        },
        "column_descriptions": {
          "Model": "Model identifier (A1, A2, B)",
          "Orientation": "perpendicular or parallel",
          "Site": "Surface site label",
          "Lambda": "Softening parameter (empty for A1 and B)",
          "z_equilibrium": "Equilibrium molecule-surface distance",
          "AdsorptionEnergy": "Total adsorption energy"
        }
      },
      "description": "Adsorption energies and equilibrium distances for CO2 on NaCl(100) computed with three models (A1 hard-sphere, A2 softened, B cluster)."
    },
    {
      "file": "vibrational_shifts.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Model",
          "nu_perp_minus_nu2",
          "nu_parallel_minus_nu2",
          "nu_perp_minus_nu_parallel"
        ],
        "units": {
          "nu_perp_minus_nu2": "cm-1",
          "nu_parallel_minus_nu2": "cm-1",
          "nu_perp_minus_nu_parallel": "cm-1"
        },
        "column_descriptions": {
          "Model": "Model identifier (A1, A2, B)",
          "nu_perp_minus_nu2": "Shift of out-of-plane bending frequency relative to gas-phase ν2",
          "nu_parallel_minus_nu2": "Shift of in-plane bending frequency relative to gas-phase ν2",
          "nu_perp_minus_nu_parallel": "Frequency splitting"
        }
      },
      "description": "Vibrational frequency shifts for the ν2 bending mode of CO2 adsorbed on NaCl(100)."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier reads your CSV files and independently evaluates each scored stage … (unchanged)
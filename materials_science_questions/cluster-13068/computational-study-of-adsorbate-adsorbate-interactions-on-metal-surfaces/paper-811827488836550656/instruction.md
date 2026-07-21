# Hartree-Fock simulation and Fermi disks analysis of submonolayer 3He on graphite

## Problem background
Understanding the energetics and structure of submonolayer liquid helium films adsorbed on strong substrates is important for interpreting wetting, layering, and phase transitions. This work models a ^3He film on graphite using a nonlocal density-functional approach that accounts for motion perpendicular to the substrate. The goal is to determine how the total energy per particle and the quasiparticle effective mass depend on the areal coverage, and thereby to assess whether the film behaves as a collection of quasi-two-dimensional Fermi disks.

## Approach
The model uses a Hartree-Fock method with a Stringari-type density-dependent effective mass, local and gradient terms in the energy functional, and a softened Lennard-Jones interaction between helium atoms. The graphite substrate is described by a potential V_s(z) = A exp(-αz) - C3/z³ - C4/z⁴ with given constants. For each areal coverage ρ₂ in the range 0.002–0.07 Å⁻², solve the corresponding 1D Hartree-Fock equation self-consistently for the single-particle wave functions. From the converged solutions, evaluate the total energy per particle E/N by integrating the energy functional, and compute the disk effective mass m* as the weighted average of the inverse effective mass over the transverse density profile. The final outputs are tables of E/N and m* versus coverage.

## Reproduction target
Produce two CSV tables:

- table_energies.csv: columns coverage_A-2 (areal coverage in Å⁻²) and E_N_K (total energy per particle in K).
- table_effective_mass.csv: columns coverage_A-2 and m_star_mHe (effective mass in units of the bare ^3He mass).

The coverages should span at least 8 values distributed across the submonolayer range 0.002 to 0.07 Å⁻². The tables must be computed from scratch by solving the Hartree-Fock model; no precomputed data or external reference tables are provided.

## Assets

- Density functional parameters from Pricaupenko & Treiner (1994): 10.1103/PhysRevLett.72.2215
- Graphite substrate potential parameters: V_s(z) = A exp(-α z) - C_3/z^3 - C_4/z^4 with A = 226.7 K, α = 3.175 Å^{-1}, C_3 = 1830.9 K Å^3, C_4 = 10305.9 K Å^4
- Python packages (numpy, scipy): numpy scipy

## Workflow steps

### Step 1: Self-consistent Hartree-Fock simulation
- Role: process
- Action: Implement the nonlocal density functional with the density-dependent effective mass (Stringari form), local and gradient terms, softened Lennard-Jones two-body interaction, and the graphite substrate potential V_s(z)=A exp(-αz) - C3/z³ - C4/z⁴. Solve the 1D Hartree-Fock equation self-consistently for a set of submonolayer coverages between 0.002 and 0.07 Å⁻², obtaining converged single-particle wavefunctions, density profiles, and mean-field potentials. Log the convergence progress.
- Evidence: `/app/outputs/hf_simulation.log`

### Step 2: Compute total energy per particle
- Role: scored (load-bearing)
- Action: For each coverage, compute the total energy per particle E/N (in K) by evaluating the full density functional energy expression using the converged HF solution and dividing by the number of particles. Write the results as a CSV table with columns for coverage (in Å⁻²) and E/N.
- Output file: `/app/outputs/table_energies.csv`
- Format: csv
- Contract: columns: coverage_A-2, E_N_K
- Scoring: scored by hidden verifier

### Step 3: Compute effective mass
- Role: scored (load-bearing)
- Action: From the wavefunctions, compute the disk effective mass m* as the weighted average of the inverse effective mass over the transverse density profile. Write the results as a CSV table with columns for coverage (in Å⁻²) and effective mass (in units of bare ³He mass).
- Output file: `/app/outputs/table_effective_mass.csv`
- Format: csv
- Contract: columns: coverage_A-2, m_star_mHe
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/table_energies.csv`
- `/app/outputs/table_effective_mass.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### table_energies.csv
- path: `/app/outputs/table_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Total energy per particle as function of areal coverage. The checker compares the reported values to hidden gold values derived from the paper's Fig. 5 using a relative tolerance and monotonic trend check.
- schema:
  - `type`: table
  - `required_columns`: `coverage_A-2`, `E_N_K`
  - `units`:
    - `coverage_A-2`: Å^-2
    - `E_N_K`: K

### table_effective_mass.csv
- path: `/app/outputs/table_effective_mass.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Effective mass as function of areal coverage. The checker compares the reported values to hidden gold values derived from the paper's Fig. 4 using a relative tolerance and a lower bound check (m* > 1.0 m_He).
- schema:
  - `type`: table
  - `required_columns`: `coverage_A-2`, `m_star_mHe`
  - `units`:
    - `coverage_A-2`: Å^-2
    - `m_star_mHe`: dimensionless (units of bare 3He mass)

Notes: The two scored tables must be produced from the same set of coverages. The HF simulation (process step) must be executed by the agent; no pre-solved wavefunctions or energy values are provided.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "table_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "coverage_A-2",
          "E_N_K"
        ],
        "units": {
          "coverage_A-2": "Å^-2",
          "E_N_K": "K"
        }
      },
      "description": "Total energy per particle as function of areal coverage. The checker compares the reported values to hidden gold values derived from the paper's Fig. 5 using a relative tolerance and monotonic trend check."
    },
    {
      "file": "table_effective_mass.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "coverage_A-2",
          "m_star_mHe"
        ],
        "units": {
          "coverage_A-2": "Å^-2",
          "m_star_mHe": "dimensionless (units of bare 3He mass)"
        }
      },
      "description": "Effective mass as function of areal coverage. The checker compares the reported values to hidden gold values derived from the paper's Fig. 4 using a relative tolerance and a lower bound check (m* > 1.0 m_He)."
    }
  ],
  "notes": "The two scored tables must be produced from the same set of coverages. The HF simulation (process step) must be executed by the agent; no pre-solved wavefunctions or energy values are provided."
}
```

## How you are scored
The hidden verifier evaluates your submitted tables independently. Each table is checked for structural consistency: the verifier checks that the E/N values satisfy a plausible monotonic trend and that m* values satisfy a plausible bound. Additionally, the numerical values are compared against hidden reference values within appropriate tolerances. The final reward is a weighted combination of these stage scores.

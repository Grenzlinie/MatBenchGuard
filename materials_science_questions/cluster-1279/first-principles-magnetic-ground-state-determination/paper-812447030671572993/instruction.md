# Compute interlayer magnetic coupling energies in metallic superlattices via self-consistent tight-binding recursion

## Problem background
Metallic magnetic superlattices, in which ferromagnetic layers alternate with non-magnetic, nearly magnetic, or antiferromagnetic spacer layers, display interlayer exchange coupling. The sign, magnitude, and range of this coupling as a function of the spacer thickness fundamentally influence the design of spintronic devices. A self-consistent tight-binding model restricted to the d-electron subspace can capture the essential electronic structure and reveal how the coupling energy per atom evolves with spacer thickness for different spacer types. This task examines four model superlattice systems: Fe-V (bcc), Co-Pd (fcc (111)), Co-Ru (hcp (0001)), and Fe-Cr (bcc). The goal is to compute the total energy difference between states with ferromagnetically and antiferromagnetically aligned ferromagnetic layers for each spacer thickness and to characterize the resulting behaviour.

## Approach
The approach is based on a d-electron-only tight-binding Hamiltonian for perfect superlattices A_mB_n. The basic elements are:

- **Hopping integrals**: Slater-Koster law for d-orbitals between neighbours at distance R_i, given by dd(σ,π,δ)_i = (6,−4,1) ddδ_1 (R_1/R_i)^5. The first-neighbour parameter ddδ_1 is set to reproduce the known d-bandwidth of each element (e.g., from Andersen's LMTO results). For A-B bonds the Shiba approximation is used.
- **Self-consistent on-site energies**: The d-band centre ε_iσ is updated according to
  ε_iσ = ε_i⁰ + U_i ΔN_i − ε_inter − σ I_i M_i/2,
  where ΔN_i is the charge transfer, M_i the magnetic moment, U_i the intra-atomic Coulomb integral, I_i the exchange integral, and σ = ±1 for spin. The Coulomb and exchange parameters are taken as constant per element.
- **Recursion method**: The local density of states is obtained by the real-space recursion method with Beer-Pettifor termination. Number of exact levels: 6 for bcc structures, 8 for fcc and hcp structures.
- **Self-consistency**: Starting from an initial guess, ΔN_i, M_i are recomputed from the density of states, new ε_iσ are determined, and the cycle is iterated to convergence.
- **Energy difference**: Once self-consistent potentials are obtained for both ferromagnetic (F) and antiferromagnetic (AF) alignment of the magnetic layers, the total energy difference per interfacial atom ΔE_n = E_n(F) − E_n(AF) (in meV/atom) is computed.

The following system-specific parameters are provided:

**Lattice structure and constants**
- Fe-V: bcc (001), A=m=3, average lattice constant a = 2.948 Å.
- Co-Ru: hcp (0001), A=m=4 or 6, a = 2.710 Å, c_Ru/2 = 2.140 Å, c_Co/2 = 2.088 Å, c_Co-Ru/2 = 2.114 Å.
- Co-Pd: fcc (111), same geometrical assumptions as Co-Ru (same a and c values).
- Fe-Cr: bcc (001), A=m=3, average lattice constant a = 2.876 Å.

**Band fillings (number of d-electrons)**
- Fe: N⁰ = 7.0
- V: N⁰ = 4.0
- Co: N⁰ = 8.24
- Ru: N⁰ = 7.24
- Pd: N⁰ = 9.75
- Cr: N⁰ = 5.0 (half-filled)

**Exchange integrals I_i (eV)**
- Fe, Co: ≈ 0.9
- V (when non-zero): 0.42
- Pd (when nearly magnetic): 0.5; otherwise 0
- Ru: 0 (non-magnetic spacer)
- Cr: ≈ 0.7 (antiferromagnetic)

**Coulomb integrals U_i**
Use U_i ≈ 1.0 eV for all species; the inter-site Coulomb correction ε_inter can be neglected in a first approach. Small variations around these values do not alter the qualitative trends.

## Reproduction target
For each superlattice system (Fe-V, Co-Pd, Co-Ru, Fe-Cr) compute ΔE_n (in meV/atom) for every integer spacer thickness n starting from n = 1 up to at least the thickness where the coupling becomes negligible (e.g., n = 5 or more). The calculation must be performed for both ferromagnetic and antiferromagnetic alignment of the ferromagnetic layers. Write all results to the CSV file `/app/outputs/coupling_energies.csv` with columns: `system` (string, one of 'Fe-V', 'Co-Pd', 'Co-Ru', 'Fe-Cr'), `n` (integer), and `delta_E` (float, the total energy difference per atom in meV). The output must contain a separate row for each (system, n) pair. The energies must be obtained from the self-consistent tight-binding recursion method described in the approach.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Tight-binding model implementation and parameter setup
- Role: process
- Action: Implement the self-consistent tight-binding model using only d electrons and the real-space recursion method with Beer-Pettifor termination. Set up the crystal structures and tight-binding parameters for the four superlattice systems (Fe-V, Co-Pd, Co-Ru, Fe-Cr) for all required spacer thicknesses. Verify that a single self-consistent iteration completes successfully.
- Evidence: `/app/outputs/tb_model_ready.log`

### Step 2: Compute interlayer coupling energies
- Role: scored (load-bearing)
- Action: For each system (Fe-V, Co-Pd, Co-Ru, Fe-Cr) and for each spacer thickness n (from 1 up to at least the point where ΔE_n becomes negligible), run the self-consistent calculation for both ferromagnetic (F) and antiferromagnetic (AF) alignment of the magnetic layers. Compute the total energy difference per atom ΔE_n = E(F) - E(AF) in meV. Write the results to coupling_energies.csv.
- Output file: `/app/outputs/coupling_energies.csv`
- Format: csv
- Contract: Columns: system (string), n (int), delta_E (float, meV/atom). system is one of 'Fe-V', 'Co-Pd', 'Co-Ru', 'Fe-Cr'; n is the integer spacer layer thickness; delta_E is the total energy difference per atom in meV.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/coupling_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### coupling_energies.csv
- path: `/app/outputs/coupling_energies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Interlayer magnetic coupling energy per atom for four superlattice systems as a function of spacer thickness. The checker assesses whether the sequences follow the three qualitative coupling behaviors described in the paper.
- schema:
  - `type`: table
  - `required_columns`: `system`, `n`, `delta_E`
  - `units`:
    - `delta_E`: meV/atom

Notes: The scoring is based on structural trends, not numerical precision. The agent must faithfully implement the self-consistent tight-binding recursion method; exact parameter values (Slater-Koster integrals, lattice constants, band fillings, exchange/coulomb integrals) are provided in the method section of the instruction. No hidden gold value is required for numeric comparison.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "coupling_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "n",
          "delta_E"
        ],
        "units": {
          "delta_E": "meV/atom"
        }
      },
      "description": "Interlayer magnetic coupling energy per atom for four superlattice systems as a function of spacer thickness. The checker assesses whether the sequences follow the three qualitative coupling behaviors described in the paper."
    }
  ],
  "notes": "The scoring is based on structural trends, not numerical precision. The agent must faithfully implement the self-consistent tight-binding recursion method; exact parameter values (Slater-Koster integrals, lattice constants, band fillings, exchange/coulomb integrals) are provided in the method section of the instruction. No hidden gold value is required for numeric comparison."
}
```

## How you are scored
A hidden verifier reads `/app/outputs/coupling_energies.csv`. For each of the four systems it checks whether the sequence of ΔE_n values follows the physically expected behaviour for that spacer type. The verifier does not compare against a single numeric target but evaluates structural properties (e.g., sign pattern, decay character, oscillation period). Your reward is proportional to the number of systems that exhibit the correct qualitative trend; reporting a number without performing the underlying computation will not satisfy these trend checks. The evidence file from the model-setup step is not scored but must be present to confirm the pipeline was executed. The final score combines the results of this step only.

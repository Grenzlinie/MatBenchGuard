# Silicon Crystal Structure Stability from Tight-Binding Model and Recursion Method

## Problem background
Silicon is a fundamental semiconductor whose phase stability and crystal-structure energetics are critical for understanding phase transitions and for developing atomistic models of defects. This task examines the ability of a simple tight-binding Hamiltonian to predict the relative stability of several silicon crystal structures—diamond, wurtzite, white-tin, and close-packed structures—as a function of atomic volume. The total energy contains a band term (computed by Haydock's scalar recursion method from a Slater-Koster Hamiltonian) and a short-range repulsive pair potential. The model's single free repulsive parameter is fitted by requiring zero pressure at the experimental equilibrium volume of diamond silicon. The resulting energy curves and the equilibrium properties of the diamond phase (cohesive energy, bulk modulus, and s–p mixing ratio) are then obtained.

## Model definition

### Tight-binding Hamiltonian
The tight-binding Hamiltonian uses an orthogonal sp³ basis on each atom. The two-centre matrix elements are taken from the Chadi Slater-Koster parameterisation. The explicit on-site energies and hopping integrals are:

- On-site energies:
  - ε_s = -5.25 eV
  - ε_p =  1.00 eV
- Hopping integrals (at reference bond length r_ref = 2.3517 Å, corresponding to a diamond lattice constant of 5.43 Å):
  - V_ssσ = -2.08 eV
  - V_spσ =  2.48 eV
  - V_ppσ =  2.72 eV
  - V_ppπ = -1.07 eV

All two-centre Hamiltonian matrix elements scale with the bond length r as (r_ref / r)², i.e., H(r) = H(r_ref) · (r_ref / r)².

### Repulsive pair potential
The repulsive energy is given by a pair potential φ(r) = A / r⁴, where A is a parameter to be fitted. The repulsive energy is truncated at first neighbours for all structures except bcc, where second neighbours are also included. For white-tin the four-coordinated variant (white-tin(4)) is used; only first-neighbour interactions are retained.

### Total energy
The total binding energy per atom is

E_B = E_band + (1/2) ∑_{i≠j} φ(|R_j - R_i|) − E_free,

where E_band is the sum of occupied eigen-energies of the tight-binding Hamiltonian, evaluated using the recursion method described below. The constant E_free ensures that the binding energy approaches the free-atom limit at infinite separation (in practice the zero of energy is set by the on-site energies and the band energy of the free atoms, but this constant cancels in energy differences; the fitted A will enforce equilibrium conditions).

## Recursion method
The band energy is computed with Haydock's scalar recursion method using ten exact moments and a square-root terminator.

Procedure:
1. Choose a starting state. A suitable choice is one of the four orthogonal sp³ hybrid orbitals centered on an atom of the crystal. Because all sites are equivalent, the site-diagonal Greenian matrix element is independent of which orbital is used.
2. Build the Lanczos basis recursively:
   - |u_0⟩ = |φ⟩ (normalised)
   - |u_1⟩ = H |u_0⟩ − a_0 |u_0⟩, where a_0 = ⟨u_0|H|u_0⟩
   - Normalise |u_1⟩ and set b_0 = 0, b_1 = ⟨u_1|u_1⟩^{1/2}
   - For n ≥ 1:
     |v_{n+1}⟩ = H |u_n⟩ − a_n |u_n⟩ − b_n |u_{n-1}⟩,
     a_{n+1} = ⟨v_{n+1}|H|v_{n+1}⟩ / ⟨v_{n+1}|v_{n+1}⟩,
     b_{n+1} = ⟨v_{n+1}|v_{n+1}⟩^{1/2},
     |u_{n+1}⟩ = |v_{n+1}⟩ / b_{n+1}.
3. Continue the recursion until ten exact moments are generated (i.e. pairs (a_0,…,a_9) and (b_1,…,b_9) are obtained).
4. Assemble the continued-fraction representation of the diagonal Green function:
   G(E) = 1 / [E − a_0 − b_1² / [E − a_1 − b_2² / [E − a_2 − … ]]]
   The infinite fraction is terminated with a square-root terminator.
5. Square-root termination: assume that beyond the last exact level the asymptotic values a_∞ and b_∞ are reached. Obtain b_∞ from the average of the last few b_n, and set the terminator
   T(E) = 2 b_∞⁻² [ (E − a_∞) − i √(4b_∞² − (E − a_∞)²) ]
   for |E − a_∞| ≤ 2b_∞, and the analytic continuation outside the band. (The exact phase convention ensures correct analytic behaviour.)
   Then the terminated Green function is used to compute the local density of states:
   n(E) = −(2/π) Im G(E+iη), η→0⁺.
6. The band energy per atom is obtained by integrating the occupied states up to the Fermi level E_F (which is determined by the total number of valence electrons, four per atom):
   E_band = ∫^{E_F} E n(E) dE.

For the scalar recursion the procedure is applied atom by atom, and because all sites are equivalent the total band energy is N × (result from one site). The code may average over the four sp³ orbitals of one site to improve statistics.

## Repulsive parameter fit (Step 1)
The repulsive prefactor A is determined by requiring zero total pressure at the experimental diamond equilibrium condition:
- Lattice constant a₀ = 5.43 Å → atomic volume Ω₀ = a₀³/4 = (5.43×10⁻⁸ cm)³ / 4.
- Bond length r₀ = √3 a₀/4 ≈ 2.3517 Å.

The total pressure is P_total = P_band + P_rep. The repulsive contribution to the pressure for the diamond structure (where each atom has four first neighbours) is given analytically by

P_rep = (8 A) / (3 Ω₀ r₀⁴) .

(P_rep for other structures can be derived from the pair sum, but the equilibrium condition is enforced only for the diamond phase.)

P_band is obtained numerically by computing E_band(Ω) at a few volumes around Ω₀ and evaluating the derivative −dE_band/dΩ. Then A is chosen so that P_total(Ω₀) = 0.

Once A is fixed, the total energy model is completely defined and can be applied to the other crystal structures.

## Reproduction target
Produce binding energy versus normalized volume (Ω/Ω₀) curves for five silicon crystal structures: diamond, wurtzite (ideal axial ratio 1.633), white-tin(4) (axial ratio 1.5516, coordination 4), fcc, and bcc. Use the above tight-binding model with ten exact moments and square-root termination. Sample at least 10 volume points per structure around the equilibrium region. From the diamond curve, locate the equilibrium volume (minimum total binding energy) and compute the cohesive energy per atom, the bulk modulus, and the s–p mixing ratio (N_p / N_s) at that equilibrium.

## Workflow steps

### Step 1: Fit tight-binding model repulsive constant A
- Role: process
- Action: Fit the repulsive parameter A by requiring zero total pressure at the experimental diamond equilibrium atomic volume (lattice constant 5.43 Å). Use the tight-binding Hamiltonian and recursion method described above to compute E_band and its volume derivative. The repulsive contribution to the pressure for diamond is P_rep = 8A/(3Ω₀ r₀⁴). Determine A.
- Evidence: none

### Step 2: Compute binding energy vs volume for all crystal structures
- Role: scored (load-bearing)
- Action: Using the fitted model, compute the total binding energy per atom as a function of normalized atomic volume Ω/Ω₀ for the structures: diamond, wurtzite (ideal axial ratio 1.633), white-tin(4) (axial ratio 1.5516, coordination 4), fcc, and bcc. For bcc, include second-neighbour repulsive interactions as well as second-neighbour hopping (within the same tight-binding framework). Sample at least 10 volume points per structure. Write the data to `/app/outputs/binding_energies.csv`. **Important**: The values in the `structure` column must be exactly: `diamond`, `wurtzite`, `white-tin(4)`, `fcc`, `bcc` (all lowercase).
- Output file: `/app/outputs/binding_energies.csv`
- Format: csv
- Columns: structure (string), volume_norm (float), binding_energy (float, eV/atom)
- Scoring: scored by hidden verifier

### Step 3: Extract diamond equilibrium properties
- Role: scored
- Action: From the diamond binding-energy data in `binding_energies.csv`, locate the equilibrium volume (minimum total binding energy). At that volume compute:
  - Cohesive energy per atom (the value of the total binding energy at equilibrium).
  - Bulk modulus B = −V (dP/dV) at equilibrium. The total pressure derivative dP/dV can be obtained numerically, with the repulsive contribution given by B_rep = (56 A) / (9 Ω₀ r₀⁴) (derived analytically from the pair potential for the diamond structure).
  - The s–p mixing ratio N_p/N_s, which is the ratio of p to s orbital occupancies obtained from the integrated density of states up to the Fermi level at the equilibrium volume.
  Write these to `/app/outputs/diamond_properties.json`.
- Output file: `/app/outputs/diamond_properties.json`
- Format: json
- Contract: JSON object with keys: cohesive_energy_eV_per_atom (float), bulk_modulus_erg_cm3 (float), s_p_mixing_ratio (float), equilibrium_volume_norm (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/binding_energies.csv`
- `/app/outputs/diamond_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### binding_energies.csv
- path: `/app/outputs/binding_energies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Binding energy per atom for each crystal structure as a function of normalized volume. The checker evaluates the relative stability of the crystal phases.
- schema:
  - `type`: table
  - `required_columns`: `structure`, `volume_norm`, `binding_energy`
  - `units`:
    - `binding_energy`: eV/atom

### diamond_properties.json
- path: `/app/outputs/diamond_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Equilibrium properties of diamond silicon: cohesive energy, bulk modulus, s-p mixing ratio, and equilibrium volume. The checker compares these to expected values.
- schema:
  - `type`: object
  - `required`:
    - `cohesive_energy_eV_per_atom`: float
    - `bulk_modulus_erg_cm3`: float
    - `s_p_mixing_ratio`: float
    - `equilibrium_volume_norm`: float
  - `units`:
    - `cohesive_energy_eV_per_atom`: eV/atom
    - `bulk_modulus_erg_cm3`: erg/cm³

Notes: The agent must implement Haydock's scalar recursion method with ten exact moments and square-root termination as described in the Model definition section. Crystal structures should be generated from standard lattice parameters given in the text.

## How you are scored
Your submission is evaluated automatically by a hidden verifier. The verifier inspects the binding energy curves in `binding_energies.csv` for a specific structural stability ordering (a qualitative trend) and reads the diamond equilibrium properties from `diamond_properties.json`, comparing them to independently obtained reference values for this model. Each component contributes to the final reward: the structural ordering portion and the property‑agreement portion each carry a separate weight. Producing the correct ordering and numerical values within the expected accuracy is necessary for a high score.
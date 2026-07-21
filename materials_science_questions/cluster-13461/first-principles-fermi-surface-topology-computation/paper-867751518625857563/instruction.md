# Hartree-Fock Phase Diagram of Y₂Ir₂O₇ (111) Thin Films

## Problem background
Transition metal oxide heterostructures grown along the (111) direction offer a promising platform for realising topological phases, including time-reversal-invariant topological insulators (TI) and Chern insulators (CI). Thin films of the pyrochlore iridate Y₂Ir₂O₇, grown along (111), naturally form alternating planes of triangular and kagome lattices of Ir ions. Two film geometries are considered: a triangular‑kagome‑triangular (TKT) trilayer and a bilayer consisting of two coupled kagome layers. The key physics involves strong spin‑orbit coupling (SOC) and electron‑electron interactions. Your task is to compute, from a tight‑binding model, the Hartree‑Fock phase diagram of these (111) films as a function of the on‑site Hubbard interaction U relative to the hopping amplitude t.

## Model definition

### Crystal structure and lattice
We work in units where the Ir‑Ir nearest‑neighbour distance in the kagome plane is *a* = 1.
- **Kagome lattice basis** (used for the kagome layers):
  primitive vectors:
  **a**₁ = (1, 0),   **a**₂ = (1/2, √3/2).
  There are three sublattice sites per unit cell located at
  **δ**₁ = (0, 0),   **δ**₂ = **a**₁/2 = (1/2, 0),   **δ**₃ = **a**₂/2 = (1/4, √3/4).
- **Triangular lattice basis** (used for the triangular layers):
  same primitive vectors **a**₁, **a**₂, one sublattice per cell at **δ** = (0,0).
- **TKT trilayer**: layer 1 (top triangular), layer 2 (middle kagome), layer 3 (bottom triangular). The triangular layers are stacked directly above the kagome layer with the same in‑plane lattice but shifted such that a triangular site sits above the kagome unit‑cell centre (the “shifted” stacking). In the model, the triangular layer Ir ions are placed at positions **r** = (x, y, z₁) with z₁ = +c/2 for the top layer and z₃ = −c/2 for the bottom layer, where c = 1 is the interlayer separation (arbitrary, does not enter in‑plane hopping). The kagome layer is at z₂ = 0.
- **Bilayer**: two identical kagome layers stacked with a shift. Layer A (bottom) as defined above; layer B (top) has the same in‑plane lattice but its origin is shifted by **a**₁/2 + **a**₂/2 relative to layer A. Both layers are parallel to the xy‑plane.

### Electronic degrees of freedom
Only the Ir ions are kept. For each Ir site we consider the j = 1/2 Kramers doublet that originates from the t₂g manifold under strong SOC. It is described by a pseudospin index σ = ↑, ↓. Thus the model is a single‑orbital Hubbard model on each site, with effective hopping that already incorporates the effect of SOC.

### Tight‑binding Hamiltonian
Write the non‑interacting part as H₀ = H_tri + H_kag + H_inter.

#### Intra‑layer hopping
##### Triangular layer
- **Triangular layer**: nearest‑neighbour (NN) hopping
  H_tri = −t_p ∑_{⟨i,j⟩,σ} c†_{iσ} c_{jσ} + h.c.
  where the sum runs over NN bonds of the triangular lattice (six neighbours per site). The hopping parameter is
  t_p = (2/3) t,
  following the paper’s relation t_p = −2 t_s/3 with t_s = −t (see below).

##### Kagome layer
Each NN bond of the kagome lattice carries a spin‑dependent hopping matrix that combines a spin‑independent part and an intrinsic spin‑orbit term.  The Hamiltonian for the kagome layer is

\[
H_{\text{kag}} = \sum_{\langle i,j\rangle,\sigma,\sigma'} c_{i\sigma}^{\dagger} \; \bigl(t_s\,\delta_{\sigma\sigma'} + i\lambda\,\nu_{ij}\,(\sigma_z)_{\sigma\sigma'}\bigr) \; c_{j\sigma'} + \text{H.c.}
\]

Here
* \(t_s = -t\) (spin‑independent NN hopping amplitude),
* \(\lambda = 0.4\ \text{eV}\) is the spin‑orbit coupling strength in the kagome layer,
* \(\sigma_z\) is the Pauli matrix acting on pseudospin space,
* \(\nu_{ij} = +1\) for a clockwise hop around a triangle (sublattice sequence \(1\rightarrow 2\), \(2\rightarrow 3\), \(3\rightarrow 1\)) and \(\nu_{ij} = -1\) for the reverse direction, as illustrated below.

The three sublattices are labelled 1,2,3 according to **δ**₁, **δ**₂, **δ**₃.  The nearest‑neighbour bonds form corner‑sharing triangles; each triangle contains one link of each type (1‑2, 2‑3, 3‑1).  With the above sign convention, the spin‑orbit term \(i\lambda\,\nu_{ij}\,\sigma_z\) induces a net flux of \(2\pi\lambda\) (in units where the effective charge is 1) through each triangle, consistent with the intrinsic SOC required to gap the Dirac points of the kagome band structure.

**Important** – Only this SOC form must be used.  Do not replace it by a phase factor \(\exp(i\phi\sigma_z)\) or any other convention that would become independent of the physical parameter \(\lambda\).  The value \(\lambda=0.4\) is fixed and must enter the calculation exactly as shown.

##### Inter‑layer coupling (TKT trilayer)
Each triangular site couples vertically to its three nearest kagome sites. The coupling amplitude is denoted t_⊥. For simplicity we take t_⊥ = t_s (the same as the in‑plane kagome hopping). The vertical bonds connect a triangular site i to the kagome sites j that are directly below (or above) in the projected position; these bonds carry the same spin‑independent hopping t_⊥ (no additional SOC factor in the vertical direction). The Hamiltonian is
 H_inter = −t_⊥ ∑_{⟨i∈tri, j∈kag⟩,σ} c†_{iσ} c_{jσ} + h.c.
(In the bilayer geometry, inter‑layer hopping between the two kagome layers is of the same form, with t_⊥, and note the shift of layer B origin.)

#### Spin‑orbit coupling strength λ
The intrinsic SOC parameter λ entering the kagome layer is set to **λ = 0.4 eV**.  Use t = 1 eV as the unit of energy (so U/t gives U in eV when t = 1).  All energies are measured relative to t.

#### On‑site interaction
The full Hamiltonian includes a Hubbard on‑site repulsion for electrons in the j=1/2 manifold:
 H_U = U ∑_i n_{i↑} n_{i↓},
where n_{iσ} = c†_{iσ} c_{iσ}. The total Hamiltonian is H = H_0 + H_U.

### Hartree‑Fock mean‑field treatment
You will perform self‑consistent Hartree‑Fock calculations. The interaction is decoupled as
 n_{i↑} n_{i↓} → ⟨n_{i↑}⟩ n_{i↓} + ⟨n_{i↓}⟩ n_{i↑} − ⟨c†_{i↑} c_{i↓}⟩ c†_{i↓} c_{i↑} − ⟨c†_{i↓} c_{i↑}⟩ c†_{i↑} c_{i↓} − E_{HF},
where the expectation values are taken with respect to the mean‑field state. Both charge densities and spin off‑diagonal order parameters (which signal magnetic order) must be allowed. The mean‑field Hamiltonian becomes a single‑particle problem that depends on the order parameters; the Schrieffer loop iterates until convergence (energy or density matrix change < 10⁻⁶).

For each U/t value, initialise the self‑consistent field with a small random perturbation to break symmetry, or with a paramagnetic spin‑unpolarised ansatz. Since the phase diagram contains both non‑magnetic and magnetic phases, you may need to try several initial seeds (e.g. paramagnetic and canted AFM pattern) and select the converged solution with the lowest total energy.

### Phase classification
After obtaining the converged mean‑field band structure, classify the ground state at each U/t as follows:

- **M (metal)**: The band gap (direct gap at Fermi level) is zero (or < 1 meV) – there is a finite density of states at the Fermi energy.
- **I (trivial insulator)**: The system is gapped (band gap > 1 meV), it has no net magnetic moment (total spin magnetization per unit cell < 0.1 μ_B), the Chern number (for TKT) or Z₂ invariant (for bilayer) is zero.
- **TI (Z₂ topological insulator)**: Only relevant for the bilayer geometry. The system is gapped, non‑magnetic, and the Z₂ invariant equals 1. In a non‑magnetic, inversion‑symmetric system you may compute the Z₂ invariant from the parity eigenvalues at the time‑reversal‑invariant momenta (Γ, three M points). If the system lacks inversion symmetry, use the Pfaffian method or the Wilson‑loop approach.
- **MC (magnetic conductor)**: The system hosts a spontaneous magnetic moment (total magnetization > 0.1 μ_B per unit cell) but the band gap is zero.
- **MI (magnetic insulator)**: The system is gapped, has a spontaneous magnetic moment, and the topological invariants (Chern number for TKT, Z₂ for bilayer) are zero.
- **CI (Chern insulator)**: For the TKT trilayer, the system is gapped, may have a net magnetic moment (Chern insulator does not require zero magnetisation), and the Chern number is a non‑zero integer (typically ±1). The Chern number is computed by integrating the Berry curvature over the 2D Brillouin zone using the Fukui‑Hatsugai method on a k‑space mesh.

For the TKT trilayer, the topological invariant is the Chern number; for the bilayer it is the Z₂ invariant.

## Task deliverables
Produce two CSV files, placed under `/app/outputs`:
- `step_01_tkt_phase_diagram.csv` for the TKT trilayer, with columns `U_t` (float), `phase` (string, one of M, I, TI, MC, MI, CI), and `Chern_number` (integer).
- `step_02_bilayer_phase_diagram.csv` for the bilayer, with columns `U_t` (float), `phase` (string), and `Z2_invariant` (integer, 0 or 1).

Cover U/t from 0 to 6 with a step no larger than 0.5. Provide at least 10 data points per file. The phase labels must correspond to the self‑consistent Hartree‑Fock ground state determined at each U/t.

## Assets
- numpy
- scipy

## Workflow steps

### Step 1: Build tight‑binding model and Hartree‑Fock solver
- Role: process
- Action: Implement the tight‑binding Hamiltonian described above, including the TKT trilayer and bilayer geometries, with the given hopping parameters (t_s = −t, t_p = 2t/3), SOC strength λ = 0.4 eV (with t = 1 eV), and inter‑layer coupling t_⊥ = t_s. Develop a self‑consistent Hartree‑Fock mean‑field solver that allows charge and magnetic order.

### Step 2: TKT trilayer phase diagram
- Role: scored (load‑bearing)
- Action: For the TKT trilayer, run self‑consistent Hartree‑Fock for a range of U/t from 0 to 6 in steps of 0.5 (or finer, as long as the points cover the whole interval). At each U/t, classify the phase and compute the Chern number. Write the results to `step_01_tkt_phase_diagram.csv`.
- Output file: `/app/outputs/step_01_tkt_phase_diagram.csv`
- Format: csv
- Contract: columns `U_t` (float), `phase` (string as listed above), `Chern_number` (int)
- Scoring: scored by hidden verifier

### Step 3: Bilayer phase diagram
- Role: scored
- Action: For the bilayer geometry, run self‑consistent Hartree‑Fock for U/t from 0 to 6 (step 0.5). Determine the phase and compute the Z₂ invariant. Write results to `step_02_bilayer_phase_diagram.csv`.
- Output file: `/app/outputs/step_02_bilayer_phase_diagram.csv`
- Format: csv
- Contract: columns `U_t` (float), `phase` (string), `Z2_invariant` (int, 0 or 1)
- Scoring: scored by hidden verifier

## Output contract
Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_tkt_phase_diagram.csv
- path: `/app/outputs/step_01_tkt_phase_diagram.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Hartree‑Fock phase diagram for the TKT trilayer as a function of U/t, with phase labels and Chern numbers.
- schema:
  - `type`: table
  - `required_columns`: `U_t`, `phase`, `Chern_number`
  - `columns_descriptions`:
    - `U_t`: ratio U/t (float)
    - `phase`: phase label string (M, I, TI, MC, MI, CI)
    - `Chern_number`: Chern number (integer, may be negative)

### step_02_bilayer_phase_diagram.csv
- path: `/app/outputs/step_02_bilayer_phase_diagram.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Hartree‑Fock phase diagram for the bilayer as a function of U/t, with phase labels and Z₂ invariant.
- schema:
  - `type`: table
  - `required_columns`: `U_t`, `phase`, `Z2_invariant`
  - `columns_descriptions`:
    - `U_t`: ratio U/t (float)
    - `phase`: phase label string (M, I, TI, etc.)
    - `Z2_invariant`: Z₂ topological invariant (0 or 1)

Notes: The hidden verifier compares the agent’s reported phase sequence and topological invariants at each U/t to a gold reference derived from the paper’s Fig. 6, with tolerance on phase boundaries (±0.5 U/t). The verifier does **not** inspect the Hartree‑Fock code itself; it only checks the CSV outputs.
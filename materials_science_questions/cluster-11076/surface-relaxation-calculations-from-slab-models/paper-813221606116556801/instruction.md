# Reproduce SrTiO₃ (001) surface energies, relaxations, and charge transfers using a tight-binding variable-charge model

## Problem background
SrTiO₃ is a prototypical perovskite oxide that serves as a model system for surface science studies of metal oxides and as a technologically important substrate for thin-film growth and oxide electronics. The (001) surface can terminate in either SrO or TiO₂ planes, and the surface termination strongly influences surface structure, energetics, and charge distribution. Accurately predicting the equilibrium bulk lattice constant, the surface formation energies, as well as the atomic relaxations and charge transfers at the two terminations at low temperature is a critical test for interatomic potential models. This task reproduces the 0 K structural, energetic, and charge properties of SrTiO₃(001) surfaces using a variable-charge tight-binding model known as SMTB-Q, which captures both ionic and covalent bonding within a self-consistent charge-equilibration framework.

## Approach
The SMTB-Q model represents the total energy of an oxide as a sum of four contributions: an atomic ionization energy expanded to second order in the charges, a shielded Coulomb interaction between variable atomic charges, a covalent tight-binding energy that depends on the local environment and on the charges themselves, and a short-range repulsive pair term. The model parameters are determined by separate fits to the binary oxides SrO and TiO₂, and then transferred to the ternary SrTiO₃ using coordination-based scaling rules and a small empirical correction. The equilibrium charges are obtained by minimizing the total energy with respect to all atomic charges, leading to a non-linear charge-equilibration problem. The model is implemented with periodic boundary conditions.

To reproduce the surface properties, you will first compute the equilibrium lattice constant of bulk cubic SrTiO₃ by minimizing the total energy with respect to the lattice parameter. Using this constant, periodic slab models of the (001) surface are constructed with SrO and TiO₂ terminations; each slab has a vacuum gap and contains a sufficient number of atomic layers to converge surface properties. The slab is then relaxed via Monte Carlo moves at a low temperature of 2 K (≥ 400 Monte Carlo steps per atom) to reach the equilibrium atomic configuration and charge distribution for each termination. From the relaxed slab total energies and the bulk cohesive energy per SrTiO₃ unit, the surface formation energies are calculated. Atomic displacements along the surface normal are obtained by comparing the relaxed positions of selected surface and subsurface atoms to their ideal bulk-terminated locations. Charge transfers are computed as the difference between the relaxed atomic charges and the corresponding bulk reference charges. The final outputs are compared by a hidden verifier against reference values derived from the same model physics; you must implement the full SMTB-Q model and slab relaxation to obtain correct results.

## SMTB-Q model equations

The cohesive energy \(E_{\text{coh}}\) of an oxide \(M_n O_m\) (for a single binary oxide, or extended to a ternary system by distinguishing different metal types in the covalent term) is:

\[
E_{\text{coh}} = E_{\text{ion}} + E_{\text{coul}} + E_{\text{cov}} + E_{\text{rep}} \tag{1}
\]

with

\[
E_{\text{ion}} = \sum_A \left(E_A^0 + \chi_A^0 Q_A + \frac{1}{2} J_{AA}^0 Q_A^2\right) \tag{2}
\]

\[
E_{\text{coul}} = \sum_A \sum_{B<A} Q_A Q_B J_{AB} \tag{3}
\]

\[
E_{\text{cov}} = -\sum_{i(i\equiv M,O)} \left\{ \sum_{\substack{j(j\equiv O,M) \\ r_{ij}\le r_c}} \xi_M^2 \exp\left[-2q_M\left(\frac{r_{ij}}{r_{OM}^0}-1\right)\right] \Delta Q_M(i,j) \right\}^{1/2} \tag{4}
\]

\[
\begin{aligned}
E_{\text{rep}} =& \sum_{\substack{i(i\equiv M,O) \\ r_{OM}\le r_c}} \sum_{\substack{j(j\equiv O,M)}} A_M \exp\left[-p_M\left(\frac{r_{ij}}{r_{OM}^0}-1\right)\right] \quad (\text{metal–oxygen pairs}) \\
& + \frac{1}{2} \sum_O \sum_{\substack{O,r_{OO}\le r_c}} B \exp\left(-\frac{r_{OO}}{\rho}\right) \quad (\text{oxygen–oxygen pairs})
\end{aligned} \tag{5}
\]

- \(E_{\text{ion}}\): ionization energy expanded to second order; \(E_A^0\) is the energy of neutral atom \(A\) (an arbitrary constant that cancels in energy differences), \(\chi_A^0\) the electronegativity, \(J_{AA}^0\) the atomic hardness, and \(Q_A\) the variable charge on atom \(A\).
- \(E_{\text{coul}}\): electrostatic energy with shielded Coulomb integrals \(J_{AB}\) between unit charges. The integrals are computed from single s-type Slater orbitals:
  \[
  \rho_A(r)=N_n r^{n-1} \exp\!\left[-\frac{(2n+1)}{4R_A}\,r\right]
  \]
  where \(N_n\) is the normalization constant and \(n\) is the principal quantum number of the outer valence orbital. The values to be used are:
  \[
  n_{\text{Sr}} = 5,\qquad n_{\text{Ti}} = 4,\qquad n_{\text{O}} = 2.
  \]
  \(R_A\) is the effective radius of atom \(A\) (treated as an adjustable parameter, given in the tables below). These integrals replace the point‑charge \(1/r\) form and include short-range shielding.
- \(E_{\text{cov}}\): covalent energy derived from a second‑moment tight‑binding approximation. In a ternary system like SrTiO₃, two separate covalent contributions are summed, one for Sr–O bonds and one for Ti–O bonds, each with its own set of parameters \((\xi_M, q_M, r_{OM}^0, r_c)\). The factor \(\Delta Q_M(i,j)\) depends on the charges of the metal and oxygen involved. Its explicit form, derived from the paper’s Appendix A, is:
  \[
  \Delta Q_M(i,j) = Z_O^{(M)} \cdot \bigl(2 - |Q_{O_j}|\bigr) \cdot \bigl(n_{\text{cov}}^{(M)} - 2 + |Q_{O_j}|\bigr),
  \]
  where \(Q_{O_j}\) is the (negative) charge of the oxygen atom \(j\), \(|Q_{O_j}|\) is its absolute value, and \(Z_O^{(M)}\) and \(n_{\text{cov}}^{(M)}\) are the metal‑specific generalized oxygen coordination number and covalent number taken from the binary oxide fits:
  \[
  Z_O^{\text{Sr}} = 6.7,\quad n_{\text{cov}}^{\text{Sr}} = 6.7;\qquad
  Z_O^{\text{Ti}} = 3.12,\quad n_{\text{cov}}^{\text{Ti}} = 3.12.
  \]
  Note: the sum inside the square root in Eq. (4) runs over neighbours \(j\) of the opposite chemical species (O neighbours for a metal site, M neighbours for an oxygen site). Hence a given M–O bond contributes to both the metal’s sqrt term and the oxygen’s sqrt term, as required by the second‑moment approximation.
- \(E_{\text{rep}}\): short‑range repulsion between metal‑oxygen pairs and oxygen‑oxygen pairs. Cation‑cation repulsion is neglected because the outer orbitals are empty in the oxide. The parameters \(A_M, p_M, B, \rho\) are listed below. The O–O pair cutoffs use a consistent cutoff of \(r_c = 6.0\) Å throughout (this matches the Ti–O cutoff and avoids ambiguity when both Sr–O and Ti–O cutoffs are present).

### Charge equilibration

The equilibrium charges are those that minimise \(E_{\text{coh}}\). Setting \(\partial E_{\text{coh}} / \partial Q_A = 0\) for every atom \(A\) yields a set of non‑linear equations:

\[
\chi_A^0 + J_{AA}^0 Q_A + \sum_{B\neq A} J_{AB} Q_B + \frac{\partial E_{\text{cov}}}{\partial Q_A} = 0.
\]

Using the definition of \(\Delta Q_M\) above, the covalent derivative for an atom \(A\) is:

- If \(A\) is a metal \(M\):
  \[
  \frac{\partial E_{\text{cov}}}{\partial Q_M} = -\frac{1}{2S_M} \sum_{j\in O} \xi_M^2 s_{ij}\, \frac{\partial \Delta Q_M(i,j)}{\partial Q_M},
  \]
  where \(S_M = \bigl(\sum_{j} \xi_M^2 s_{ij} \Delta Q_M(i,j)\bigr)^{1/2}\), and \(\partial\Delta Q_M/\partial Q_M = 0\) because \(\Delta Q_M\) depends only on the oxygen charge. Therefore \(\partial E_{\text{cov}} / \partial Q_M = 0\) for a metal atom.

- If \(A\) is an oxygen atom \(O\):
  \[
  \frac{\partial E_{\text{cov}}}{\partial Q_O} = -\frac{1}{2S_O} \sum_{i\in M} \xi_M^2 s_{ij}\, \frac{\partial \Delta Q_M(i,j)}{\partial Q_O},
  \]
  with \(S_O = \bigl(\sum_{i} \xi_M^2 s_{ij} \Delta Q_M(i,j)\bigr)^{1/2}\) and
  \[
  \frac{\partial \Delta Q_M}{\partial Q_O} = Z_O^{(M)} \cdot \,\text{sgn}(Q_O) \cdot \bigl[ (n_{\text{cov}}^{(M)} - 2 + |Q_O|) - (2 - |Q_O|) \bigr]
  = Z_O^{(M)} \cdot \,\text{sgn}(Q_O) \cdot \bigl( n_{\text{cov}}^{(M)} - 4 + 2|Q_O| \bigr),
  \]
  where \(\text{sgn}(Q_O)\) is the sign of the oxygen charge (negative), and the sum over \(i\) includes both Sr and Ti neighbours that are closer than the respective cutoffs. In the ternary case the total covalent derivative at an oxygen atom is the sum of contributions from its Sr neighbours (using Sr parameters and \(Z_O^{\text{Sr}}, n_{\text{cov}}^{\text{Sr}}\)) and its Ti neighbours (using Ti parameters and \(Z_O^{\text{Ti}}, n_{\text{cov}}^{\text{Ti}}\)).

The system of equations can be solved self‑consistently, e.g. by Newton‑Raphson iteration, updating all charges until convergence. After convergence the full energy \(E_{\text{coh}}\) can be computed via Eqs. (1)–(5).

*Note*: For binary oxides this scheme reduces to the single equation (6) given in the paper, but the formulation above is valid for the ternary SrTiO₃ and must be used.

## Model parameters

### Binary oxides (SrO and TiO₂)

Table 1: SMTB‑Q parameters for bulk SrO and TiO₂ (from the paper). Oxygen parameters are the same for both oxides except where noted.

| Parameter | SrO | TiO₂ | Units / Notes |
|-----------|-----|------|---------------|
| \(\chi_O^0\) | 6.57 | 6.57 | eV |
| \(J_{OO}^0\) | 10.22 | 10.22 | eV |
| \(\chi_{M}^0\) | 4.9  | 0.0  | eV |
| \(J_{MM}^0\) | 3.56 | 10.572 | eV |
| \(R_O\)      | 0.52 | 0.543 | Å (SrO: \(Z_O=6\); TiO₂: \(Z_O=3\)) |
| \(R_M\)      | 0.767| 0.734 | Å |
| \(\xi_M\)     | 1.423| 1.087 | eV |
| \(q_M\)      | 1.935| 2.096 | dimensionless |
| \(A_M\)      | 0.342| 0.134 | eV |
| \(p_M\)      | 6.274| 12.61 | dimensionless |
| \(B\)        | 580.44| 580.44| eV |
| \(\rho\)      | 0.354| 0.354 | Å |
| \(r_{OM}^0\) | 2.58 | 1.95  | Å |
| \(r_c\)      | 8.0  | 6.0   | Å (cutoff for both M–O and O–O) |

### Transfer to SrTiO₃

The SrTiO₃ parameters are derived from the binary‑oxide parameters using coordination‑based scaling rules and a small empirical correction. The general scaling rule (Eq. (24) of the paper) for a metal \(M\) transferred from a binary oxide to the perovskite is:

\[
\xi_M^{\text{STO}} = \xi_M^{\text{bin}} \left( \frac{Z_O^{\text{STO}}}{Z_O^{\text{bin}}} \right)^{1/2}
\qquad
A_M^{\text{STO}} = A_M^{\text{bin}} \left( \frac{Z_O^{\text{STO}}}{Z_O^{\text{bin}}} \right)
\]

In SrTiO₃ each oxygen is surrounded by 2 Sr and 2 Ti, giving an oxygen generalized coordination number \(Z_O^{\text{STO}} = 4\). From the binary oxides, the Sr‑O coordination is \(Z_O^{\text{SrO}} = 6.7\) and the Ti‑O coordination is \(Z_O^{\text{TiO₂}} = 3.12\). Applying the rules and then adjusting to best reproduce bulk SrTiO₃ properties yields the following fitted parameters for the perovskite:

- Sr‑O bonds: \(\xi_{\text{Sr}} = 0.7987\) eV, \(A_{\text{Sr}} = 0.1574\) eV
- Ti‑O bonds: \(\xi_{\text{Ti}} = 0.3804\) eV, \(A_{\text{Ti}} = 0.124\) eV
- Effective oxygen radius: \(R_O = 0.504\) Å

All other parameters are directly inherited from the binary oxides without change. Specifically:

- QEq parameters for O, Sr, and Ti remain as in Table 1: \(\chi_O^0 = 6.57\) eV, \(J_{OO}^0 = 10.22\) eV; \(\chi_{\text{Sr}}^0 = 4.9\) eV, \(J_{\text{Sr}\text{Sr}}^0 = 3.56\) eV; \(\chi_{\text{Ti}}^0 = 0.0\) eV, \(J_{\text{Ti}\text{Ti}}^0 = 10.572\) eV.
- Sr radius \(R_{\text{Sr}} = 0.767\) Å, Ti radius \(R_{\text{Ti}} = 0.734\) Å.
- Bond exponents: \(q_{\text{Sr}} = 1.935\), \(q_{\text{Ti}} = 2.096\).
- Repulsive exponents: \(p_{\text{Sr}} = 6.274\), \(p_{\text{Ti}} = 12.61\).
- O‑O repulsion: \(B = 580.44\) eV, \(\rho = 0.354\) Å.
- Sr–O equilibrium bond length: \(r_{\text{SrO}}^0 = 2.58\) Å; Ti–O equilibrium bond length: \(r_{\text{TiO}}^0 = 1.95\) Å.
- Cutoff radii: for Sr–O interactions use \(r_c = 8.0\) Å; for Ti–O interactions use \(r_c = 6.0\) Å. O–O pair cutoffs use a consistent \(r_c = 6.0\) Å throughout the perovskite.

### Bulk reference charges for SrTiO₃

The bulk equilibrium charges obtained from the SMTB‑Q model for cubic SrTiO₃ are:

\[
Q_{\text{Sr}}^{\text{bulk}} = 1.72,\qquad
Q_{\text{Ti}}^{\text{bulk}} = 1.17,\qquad
Q_{\text{O}}^{\text{bulk}} = -0.963\ (\text{per oxygen}).
\]

These are the values that must be used as reference to compute charge transfers in the surface slabs: \(\Delta Q_i = Q_i^{\text{slab}} - Q_i^{\text{bulk}}\).

## Atom labeling for the (001) surface slabs

You will construct two symmetric slab models with vacuum (≥15 Å), each having an integer number of SrO and TiO₂ layers and terminating on one side by a SrO plane and on the other by a TiO₂ plane. To identify the atoms for which displacements and charge transfers are reported, use the following labeling derived from the paper’s layer‑by‑layer description (the numbers are layer indices counting from the outermost plane inward).

### SrO‑terminated slab
(outermost plane is SrO)

1. Outermost Sr layer – **Sr(9)**
2. First oxygen layer – **O(10)**
3. Subsurface Ti layer – **Ti(5)**
4. Second oxygen layer – **O(7)**
5. Second Sr layer – **Sr(6)** (the Sr plane just below O(7))

A sketch of the sequence (from surface to interior):
… SrO(Sr(9)–O(10)) – TiO₂(Ti(5)–O(7)) – SrO(Sr(6)–…) – …  
For the surface energy and relaxations you only need the positions and charges of these five atoms; the rest of the slab should contain enough layers to converge the surface properties (the paper used a slab thickness equivalent to about 10 nm; setting the total slab thickness ≥ 23 Å and ≥ 7 atomic layers is sufficient for this exercise).

### TiO₂‑terminated slab
(outermost plane is TiO₂)

1. Outermost Ti layer – **Ti(1)**
2. First oxygen layer – **O(3)**
3. Subsurface Sr layer – **Sr(2)**
4. Second oxygen layer – **O(4)**

The sequence is: TiO₂(Ti(1)–O(3)) – SrO(Sr(2)–O(4)) – …  
Report properties for these four atoms.

## Workflow steps

### Step 1: Implement SMTB‑Q model and simulation framework
- **Role**: process
- **Action**: Implement the SMTB‑Q total energy and charge equilibration (Eqs. 1‑5 and the charge‑equilibration equations given above) capable of periodic bulk and slab calculations, using the parameter set given above. The implementation must support Monte Carlo atomic relaxation and charge equilibration at every step.
- **Evidence**: none

### Step 2: Bulk SrTiO₃ equilibrium lattice constant
- **Role**: scored
- **Action**: Using the implemented model with the fitted SrTiO₃ parameters, perform energy minimization (e.g., scanning the cubic lattice parameter) to find the equilibrium lattice constant \(a_0\) of cubic SrTiO₃ at 0 K.
- **Output file**: `/app/outputs/bulk_lattice_constant.txt`
- **Format**: txt
- **Contract**: Single float, units: Å
- **Scoring**: scored by hidden verifier

### Step 3: Slab relaxation for SrO‑ and TiO₂‑terminated SrTiO₃(001) surfaces
- **Role**: process
- **Action**: Build periodic slab models of SrTiO₃(001) with SrO and TiO₂ terminations. Use a 1×1 surface supercell with the in‑plane lattice constant equal to \(a_0\) from step 2, a slab thickness ≥ 23 Å, and a vacuum gap of at least 15 Å. Set up the atoms so that the slab is symmetric (identical terminations on both sides) to avoid a spurious dipole; in a symmetric slab the central layer should be SrO for one termination and TiO₂ for the other — follow standard surface‑slab construction for perovskites. Run Monte Carlo relaxation at 2 K until equilibrium (≥ 400 moves per atom), with charge equilibration after each move. Save the final total energy per supercell, the relaxed atomic Cartesian coordinates, and the relaxed atomic charges for all atoms in a structured file.
- **Evidence**: `/app/outputs/relaxation_results.json` (JSON object containing the two terminations’ slab data — total energies, positions, charges — structured as you see fit for the next steps)

### Step 4: Surface energies
- **Role**: scored
- **Action**: For each termination, compute the surface formation energy using the relaxed slab total energy saved in `relaxation_results.json` and the bulk energy per SrTiO₃ formula unit. The bulk energy per formula unit must be obtained from the same SMTB‑Q model for a bulk SrTiO₃ unit at the equilibrium lattice constant \(a_0\). The surface energy is given by:
  \[
  \gamma = \frac{E_{\text{slab}} - n\,E_{\text{bulk}}}{2A}
  \]
  where \(E_{\text{slab}}\) is the total energy of the relaxed symmetric slab, \(n\) is the number of SrTiO₃ formula units in the slab, \(E_{\text{bulk}}\) is the cohesive (total) energy per formula unit of bulk SrTiO₃ (a negative number), and \(A\) is the area of one surface of the supercell (\(a_0^2\)). The factor 2 accounts for the two identical surfaces. Report the surface energies in J/m².
- **Output file**: `/app/outputs/surface_energies.json`
- **Format**: JSON object with keys `"SrO_terminated"` and `"TiO2_terminated"`; values are floats (units: J/m²).
- **Scoring**: scored by hidden verifier

### Step 5: Atomic displacements
- **Role**: scored
- **Action**: For each of the labelled atoms listed in the “Atom labeling” section, compute the displacement of the relaxed atomic position relative to the ideal bulk‑terminated position along the surface normal [001] direction. The ideal positions are obtained by assuming the slab is built from bulk‑like layers with the interlayer spacings of unrelaxed cubic SrTiO₃ (\(a_0/2\)). The sign convention is: **negative** = outward displacement towards the vacuum; **positive** = inward displacement towards the bulk.
- **Output file**: `/app/outputs/atomic_displacements.csv`
- **Format**: CSV file with header `termination,atom_label,displacement_A`. Each row corresponds to one atom label (e.g., `SrO,Sr(9),-0.32`). The displacement is in Å.
- **Scoring**: scored by hidden verifier

### Step 6: Charge transfers
- **Role**: scored
- **Action**: For each labelled atom, compute the charge transfer \(\Delta Q = Q_{\text{slab}} - Q_{\text{bulk}}\) using the relaxed charges from the slab and the bulk reference charges given above (\(Q_{\text{Sr}}^{\text{bulk}} = 1.72\), \(Q_{\text{Ti}}^{\text{bulk}} = 1.17\), \(Q_{\text{O}}^{\text{bulk}} = -0.963\)).
- **Output file**: `/app/outputs/charge_transfers.csv`
- **Format**: CSV file with header `termination,atom_label,charge_transfer`. Each row corresponds to one atom label (e.g., `TiO2,Ti(1),-0.18`).
- **Scoring**: scored by hidden verifier
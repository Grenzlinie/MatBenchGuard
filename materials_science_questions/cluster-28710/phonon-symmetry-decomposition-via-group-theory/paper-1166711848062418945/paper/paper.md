# Symmetries in zero and finite center-of-mass momentum excitons
Robin Bajaj$^{1}$, Namana Venkatareddy$^{1}$, H. R. Krishnamurthy$^{1,2}$ and Manish Jain$^{1*}$

$^{1}$Centre for Condensed Matter Theory, Department of Physics,
Indian Institute of Science, Bangalore 560012, India and
$^{2}$International Centre for Theoretical Sciences, Tata Institute of Fundamental Research, Bengaluru 560089, India

(Dated: December 12, 2025)

We present a symmetry-based framework for the analysis of excitonic states, incorporating both time-reversal and space-group symmetries. We demonstrate the use of time-reversal and space- group symmetries to obtain exciton eigenstates at symmetry-related center-of-mass momenta in the entire Brillouin zone from eigenstates calculated for center-of-mass momenta in the irreducible Brillouin zone. Furthermore, by explicitly calculating the irreducible representations of the little groups, we classify excitons according to their symmetry properties across the Brillouin zone. Using projection operators, we construct symmetry-adapted linear combinations of electron-hole product states, which block diagonalize the Bethe-Salpeter equation (BSE) Hamiltonian at both zero and finite exciton center-of-mass momenta. This enables a transparent organization of excitonic states and provides direct access to their degeneracies, selection rules, and symmetry-protected features. As a demonstration, we apply this formalism to monolayer MoS$_2$, where the classification of excitonic irreducible representations and the block structure of the BSE Hamiltonian show excellent agreement with compatibility relations derived from group theory. Beyond this material-specific example, the framework offers a general and conceptually rigorous approach to the symmetry classification of excitons, enabling significant reductions in computational cost for optical spectra, exciton-phonon interactions, and excitonic band structure calculations across a wide range of materials.

## I. INTRODUCTION

Symmetry principles lie at the heart of quantum physics, governing both fundamental laws and emergent phenomena. In quantum systems, the transformation properties of energy eigenstates under symmetry oper- ations [1–4] dictate degeneracies, selection rules, and re- sponses to external perturbations. In electronic struc- ture calculations, for instance, Bloch's theorem provides a powerful simplification by exploiting the lattice period- icity, restricting calculations to momenta within the first Brillouin zone (BZ). Additionally, space group symme- tries allow for further computational efficiency by identi- fying symmetry-equivalent points in the BZ, reducing the sampling space and enabling the classification of eigen- states into irreducible representations. These group- theoretical techniques are routinely employed in both one-electron and lattice dynamical problems to stream- line band structure calculations and enforce optical se- lection rules.

In one-electron as well as phonon band structures, eigenstates at a given point in the BZ are routinely la- beled by the irreducible representations of the little group at that point giving the symmetry classification of first- principles wave functions [2–4]. These symmetry-based insights are now deeply integrated into modern electronic structure workflows, providing both conceptual guidance and computational gains across condensed matter theory. Tools such as the Bilbao Crystallographic Server [5], SP- GREP package [6], and IRREP package [7] enable block di- agonalization of Hamiltonians, degeneracy classification, and compatibility relation tracking capabilities that are now central to high-throughput and symmetry-aware ma- terials discovery.

Despite their success in one-electron and phonon prob- lems, such symmetry-based approaches remain under- utilized in the context of excitons [8, 9]. Excitons fea- ture prominently in the optical response of semiconduc- tors and insulators [10, 11] and are particularly well de- scribed within the Bethe-Salpeter equation (BSE) for- malism [12–15]. The eigenstates of the BSE Hamiltonian, being two-particle bound states labeled by their center- of-mass (c.m.) momenta and dependent on relative mo- menta, differ from one-electron eigenstates in terms of the structure and the application of symmetry opera- tions. Recently, some studies have addressed the role of symmetry in excitons. For example, Reference [16] an- alyzes the excitonic band structure of monolayer MoS$_2$ and interprets the symmetry of low-lying excitons us- ing group theory. Ref. [17] reports measurements of the exciton fine structure in monolayer MoS$_2$, highlightling the irreducible representations of two optically active (bright) excitons with parallel spins, along with two spin- forbidden dark states. Galvani *et al.* [18] investigate the symmetry properties of excitons in a monolayer hBN by combining *ab initio* calculations with a tight-binding Wannier analysis in both real and reciprocal space. Simi- larly, Ref. [19] examines the influence of uniaxial strain on the symmetry classification of excitons in C$_3$N, employ- ing a tight-binding BSE framework. In another work fo- cused on excitonic $g$ factors in monolayer WSe$_2$ [20], the low-energy excitons are classified by tracking the com- patibility relations between the little group $C_{3h}$ at the K/K' points and the full point group $D_{3h}$ at the $\Gamma$ point. Furthermore, several studies [21, 22] highlight the role of symmetry classification in elucidating the interplay be-

*mjain@iisc.ac.in*

tween crystal symmetries and excitonic topology. While these studies provide valuable insights at specific high-symmetry points, a systematic symmetry-based classification of the eigenstates of the BSE across the Brillouin zone within an ab initio framework is still largely unexplored.

In addition to providing insight and understanding, symmetries can be used to reduce the computational cost of the calculations. In the context of one-electron states, most widely used electronic structure codes, such as VASP [23], QUANTUMESPRESSO [24], and ABINIT [25], routinely incorporate symmetry-based optimizations to reduce computational cost and ensure physically meaningful results. This is used by calculating the electronic states for momenta within the irreducible part of the BZ and using symmetry to transform them to states with momenta within the rest of the BZ. Furthermore, in the context of lattice dynamics, similar symmetry-based approaches are used. Codes such as PHONOPY [26] and PHONO3PY [27] leverage crystal symmetries to reduce the cost of calculating dynamical matrices. However, similar ideas to use symmetry to reduce the computational costs in problems where excitons at finite c.m. are essential have not yet been employed. Many important physical phenomena such as exciton-phonon scattering [28-33], indirect optical transitions [30], and exciton thermalization dynamics [34] require detailed knowledge of excitonic states for a dense c.m. momentum grid. Exciton-phonon coupling, in particular, determines linewidths and exciton thermalization dynamics [34]. In systems like ${\rm MoS_2}$ [28, 35], achieving convergence of calculations of the optical spectra demands fine sampling of the c.m. momenta in the BZ, especially near band extrema where small momentum shifts can strongly modulate coupling strength. Similarly, modeling exciton dynamics via the Boltzmann equation [34] and indirect optical spectra calculations in hBN, silicon, and bilayer ${\rm MoS_2}$ [30, 36-40] require extensive sampling of finite c.m. momenta excitonic states. However, performing BSE calculations across such fine c.m. momenta meshes is computationally prohibitive for most materials. This further underscores the need for a symmetry-adapted approach to excitons that is grounded in an ab initio framework.

In this work, we develop a comprehensive symmetry-based formalism for exciton calculations within an ab initio framework. By applying space group operations on exciton wave functions at finite c.m. momentum, $\mathbf{Q}$, we reconstruct the wave functions for momenta in the full BZ from computations for $\mathbf{Q}$ restricted to the irreducible wedge. We further classify excitonic eigenstates into irreducible representations, providing a rigorous symmetry-resolved picture of exciton physics. At $\mathbf{Q}=0$, we use symmetry-adapted bases to block diagonalize the BSE Hamiltonian, reducing both diagonalization time and memory usage.

By systematically incorporating crystal symmetry into excitonic theory, our approach delivers both conceptual and computational advances. It enables scalable BSE calculations for complex systems and provides a robust foundation for interpreting exciton phenomena through the lens of symmetry.

## II. THEORETICAL FORMALISM

### A. Preliminaries: Space group symmetries and time-reversal symmetry in one-electron wave functions

In periodic solids, the translational symmetry of the lattice ensures that the one-electron Hamiltonian $\hat{\mathcal{H}}$ commutes with the lattice translation operator, $\hat{T}_{\mathbf{R}}$, where $\mathbf{R}$ is a Bravais lattice vector. As a result, $\hat{\mathcal{H}}$ can be written as a direct sum of independent Hamiltonians at each crystal momentum $\mathbf{k}$ in the Brillouin zone,
$$
\hat{\mathcal{H}}=\bigoplus_{\mathbf{k}} \hat{\mathcal{H}}_{\mathbf{k}} \tag{1}
$$

This block-diagonal structure implies that the wave functions, $\phi_{n,\mathbf{k}}(\mathbf{r})$, can be chosen to be eigenstates of the translation operators, leading to the Bloch form
$$
\phi_{n,\mathbf{k}}(\mathbf{r})=e^{i \mathbf{k} \cdot \mathbf{r}} u_{n,\mathbf{k}}(\mathbf{r}) \tag{2}
$$
where $u_{n,\mathbf{k}}(\mathbf{r})$ is periodic with the lattice. The cell periodic part $u_{n,\mathbf{k}}(\mathbf{r})$ is commonly expanded in a plane-wave basis as
$$
u_{n,\mathbf{k}}(\mathbf{r})=\sum_{\mathbf{G}} c_{n,\mathbf{k}}(\mathbf{G}) e^{i \mathbf{G} \cdot \mathbf{r}} \tag{3}
$$
where $\mathbf{G}$ are reciprocal lattice vectors and $c_{n,\mathbf{k}}(\mathbf{G})$ are the expansion coefficients. This representation naturally incorporates translational symmetry and facilitates the treatment of additional crystal symmetries.

The symmetry properties of Bloch wave functions are central to understanding electronic band structures and the selection rules governing optical transitions. Due to the space-group symmetry of the underlying crystal lattice, Bloch wave functions are constrained to transform in specific ways under the corresponding symmetry operations. These transformations determine the irreducible representations associated with the wave functions.

Let $\hat{P}_{\{\mathcal{R}_{\mathbf{t}} | \mathbf{t}\}}$ represent a symmetry operator associated with $\{\mathcal{R}_{\mathbf{t}} | \mathbf{t}\} \in \mathcal{G}$, where $\mathcal{R}_{\mathbf{t}}$ denotes a point-group operation (such as rotation, mirror reflection, or inversion), $\mathbf{t}$ is a fractional translation, and $\mathcal{G}$ is the crystal space group. Due to the underlying symmetry of the lattice, $\hat{P}_{\{\mathcal{R}_{\mathbf{t}} | \mathbf{t}\}}$ commutes with the Hamiltonian, $[\hat{P}_{\{\mathcal{R}_{\mathbf{t}} | \mathbf{t}\}}, \hat{\mathcal{H}}]=0$. $\hat{P}_{\{\mathcal{R}_{\mathbf{t}} | \mathbf{t}\}}$ maps $\hat{\mathcal{H}}_{\mathbf{k}}$ to $\hat{\mathcal{H}}_{\mathcal{R}_{\mathbf{t}} \mathbf{k}}$ via $\hat{\mathcal{H}}_{\mathcal{R}_{\mathbf{t}} \mathbf{k}}=\hat{P}_{\{\mathcal{R}_{\mathbf{t}} | \mathbf{t}\}}^{-1} \hat{\mathcal{H}}_{\mathbf{k}} \hat{P}_{\{\mathcal{R}_{\mathbf{t}} | \mathbf{t}\}}^{-1}$ (See Appendix A). This implies that if a wavevector $\mathbf{k}$ is mapped to $\mathcal{R}_{\mathbf{t}} \mathbf{k}$ by a symmetry operation, the energy eigenvalues corresponding to $\mathbf{k}$ and $\mathcal{R}_{\mathbf{t}} \mathbf{k}$ remain same i.e. $\epsilon_{n, \mathcal{R}_{\mathbf{t}} \mathbf{k}}=\epsilon_{n, \mathbf{k}}$. The action of the symmetry operator on the Bloch wave function transforms it according to
$$
\hat{P}_{\{\mathcal{R}_{\mathbf{t}} | \mathbf{t}\}} \phi_{n,\mathbf{k}}(\mathbf{r})=\phi_{n,\mathbf{k}}\left(\mathcal{R}_{\mathbf{t}}^{-1}(\mathbf{r}-\mathbf{t})\right) \tag{4}
$$

Utilizing Bloch's form as defined in Eq. 2, the transformation becomes
$$\hat{P}_{\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\}} \phi_{n,\mathbf{k}}(\mathbf{r}) = u_{n,\mathcal{R}_{\mathbf{t}}\mathbf{k}}^{\mathbf{t}}(\mathbf{r}) e^{i \mathcal{R}_{\mathbf{t}} \mathbf{k}.(\mathbf{r}-\mathbf{t})} \tag{5}$$

Here the cell-periodic function $u_{n,\mathcal{R}_{\mathbf{t}} \mathbf{k}}^{\mathbf{t}}(\mathbf{r}) = u_{n,\mathbf{k}}(\mathcal{R}_{\mathbf{t}}^{-1}(\mathbf{r}- \mathbf{t}))$ and can be written as
$$u_{n,\mathcal{R}_{\mathbf{t}} \mathbf{k}}^{\mathbf{t}}(\mathbf{r}) = \sum_{\mathbf{G}} c_{n,\mathbf{k}}(\mathcal{R}_{\mathbf{t}}^{-1} \mathbf{G}) e^{-i \mathbf{G} \cdot \mathbf{t}} e^{i \mathbf{G} \cdot \mathbf{r}} \tag{6}$$

Substituting this into Eq. 5 yields the transformation rule for the plane-wave coefficients at $\mathcal{R}_{\mathbf{t}} \mathbf{k}$ in terms of those at $\mathbf{k}$:
$$c_{n,\mathcal{R}_{\mathbf{t}} \mathbf{k}}^{\mathbf{t}}(\mathbf{G}) = c_{n,\mathbf{k}}(\mathcal{R}_{\mathbf{t}}^{-1} \mathbf{G}) e^{-i (\mathbf{G} + \mathcal{R}_{\mathbf{t}} \mathbf{k}) \cdot \mathbf{t}} \tag{7}$$

This equation captures how the plane-wave components of the Bloch wave function transform under a space group operation. In systems without degeneracy and spin, this relation uniquely determines the coefficients at $\mathcal{R}_{\mathbf{t}} \mathbf{k}$, up to a common phase factor across all bands.

When spin degrees of freedom are included, the symmetry properties of Bloch wave functions must account for both spatial transformations and their induced effects on spinors. Although lattice symmetries act on spatial coordinates in $\mathbb{R}^3$, they also act on the spin degrees of freedom, which transform under SU(2), the double cover of the spatial rotation group SO(3).

A spinor Bloch wave function can be expressed as a two-component column vector:
$$\Phi_{n,\mathbf{k}}(\mathbf{r}) = \begin{bmatrix} \phi_{n,\mathbf{k},\uparrow}(\mathbf{r}) \\ \phi_{n,\mathbf{k},\downarrow}(\mathbf{r}) \end{bmatrix} = \begin{bmatrix} u_{n,\mathbf{k},\uparrow}(\mathbf{r}) e^{i \mathbf{k} \cdot \mathbf{r}} \\ u_{n,\mathbf{k},\downarrow}(\mathbf{r}) e^{i \mathbf{k} \cdot \mathbf{r}} \end{bmatrix} \tag{8}$$
where $u_{n,\mathbf{k},\sigma}(\mathbf{r})$ are periodic functions and $\sigma = \uparrow, \downarrow$ denotes the spin index.

A general symmetry operation involving spin can be written as the direct product of a spatial operation and a corresponding spinor transformation:
$$\hat{P}_{\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\}}^{sp} = \hat{P}_{\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\}} \otimes \hat{\mathcal{T}}_{\mathcal{R}_{\mathbf{t}}} \tag{9}$$
where $\hat{P}_{\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\}}^{sp}$ denotes the full operator that corresponds to the symmetry operation $\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\}$, and $\hat{P}_{\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\}}$ and $\hat{\mathcal{T}}_{\mathcal{R}_{\mathbf{t}}}$ denote its spatial and spin components, respectively. The dependence on $\mathbf{t}$ is dropped from $\hat{\mathcal{T}}_{\mathcal{R}_{\mathbf{t}}}$ since fractional translations do not affect the spinor representation. Let $\mathcal{T}_{\mathcal{R}_{\mathbf{t}}}^{\sigma, \sigma'}$ be the matrix elements of the SU(2) representation corresponding to $\hat{\mathcal{T}}_{\mathcal{R}_{\mathbf{t}}}$. Since spinors transform under the SU(2) representation of rotations, their behavior is governed by the homomorphism between SO(3) and SU(2), given by
$$\mathcal{T} : \text{SO}(3) \to \text{SU}(2) \tag{10}$$

This mapping is a two-to-one covering: each rotation $\mathcal{R}_{\mathbf{t}} \in \text{SO}(3)$ corresponds to two elements $\pm \mathcal{T}_{\mathcal{R}_{\mathbf{t}}} \in \text{SU}(2)$.

Consequently, under a full $2\pi$ rotation, a spinor acquires a phase of $-1$, reflecting the half-integer spin of electrons.

The action of the full symmetry operator $\hat{P}_{\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\}}^{sp}$ on the spinor Bloch wave function $\Phi_{n,\mathbf{k}}(\mathbf{r})$ is
$$\hat{P}_{\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\}}^{sp} \Phi_{n,\mathbf{k}}(\mathbf{r}) = \mathcal{T}_{\mathcal{R}_{\mathbf{t}}} \Phi_{n,\mathcal{R}_{\mathbf{t}} \mathbf{k}}^{\mathbf{t}}(\mathbf{r}) \tag{11}$$

Here the spinor wave function, $\Phi_{n,\mathcal{R}_{\mathbf{t}} \mathbf{k}}^{\mathbf{t}}(\mathbf{r})$ is defined as $\begin{bmatrix} \phi_{n,\mathcal{R}_{\mathbf{t}} \mathbf{k},\uparrow}^{\mathbf{t}}(\mathbf{r}) \\ \phi_{n,\mathcal{R}_{\mathbf{t}} \mathbf{k},\downarrow}^{\mathbf{t}}(\mathbf{r}) \end{bmatrix}$. The explicit form of the SU(2) spinor matrix, $\mathcal{T}_{\mathcal{R}_{\mathbf{t}}}$ for a rotation by an angle, $\theta$, about the $\hat{n}$ axis is
$$\mathcal{T}_{\mathcal{R}_{\mathbf{t}}} = \begin{bmatrix} \cos\left( \frac{\theta}{2} \right) - i n_z \sin\left( \frac{\theta}{2} \right) & \left( -n_y - i n_x \right) \sin\left( \frac{\theta}{2} \right) \\ \left( n_y - i n_x \right) \sin\left( \frac{\theta}{2} \right) & \cos\left( \frac{\theta}{2} \right) + i n_z \sin\left( \frac{\theta}{2} \right) \end{bmatrix} \tag{12}$$

This unitary transformation guarantees that the spinors are transformed correctly under spatial rotations. For a general rotation, the directions $\hat{n} = (n_x, n_y, n_z)$ and $\theta$ are chosen based on $\mathcal{R}_{\mathbf{t}}$. Because $\mathcal{T}_{\mathcal{R}_{\mathbf{t}}} \in \text{SU}(2)$, spinor wave functions obey a different transformation law from scalar wave functions. This leads to the emergence of half-integer representations and the necessity to use double groups with distinct irreducible representations.

A key consequence of the SU(2)-SO(3) homomorphism is the sign ambiguity in group multiplication. If two spatial rotations $(\mathcal{R}_{\mathbf{t}})_i$ and $(\mathcal{R}_{\mathbf{t}})_j$ combine to form $(\mathcal{R}_{\mathbf{t}})_k$, that is,
$$(\mathcal{R}_{\mathbf{t}})_i (\mathcal{R}_{\mathbf{t}})_j = (\mathcal{R}_{\mathbf{t}})_k \tag{13}$$
then their corresponding spin representations satisfy
$$(\mathcal{T}_{\mathcal{R}_{\mathbf{t}}})_i (\mathcal{T}_{\mathcal{R}_{\mathbf{t}}})_j = \pm (\mathcal{T}_{\mathcal{R}_{\mathbf{t}}})_k \tag{14}$$

The additional sign arises from the double cover nature of SU(2) over SO(3). Specifically, a $2\pi$ rotation changes the sign of a spinor wave function, a fundamental property underlying fermionic statistics, and the behavior of electrons in systems with spin-orbit coupling. This sign ambiguity is reflected in the group multiplication rules of double groups, where the symmetry elements remain the same, but the signs depend on the chosen branch of the SU(2) representation corresponding to a given SO(3) rotation.

So far, our discussion has been restricted to cases where the energy eigenstates are nondegenerate, both with and without spin-orbit coupling. However, the presence of degeneracies introduces an additional complexity in the symmetry analysis, since multiple wave functions may mix under the action of symmetry operations. Under a symmetry operation $\mathcal{R}_{\mathbf{t}}$, a Bloch state $|\phi_{m \mathbf{k}}\rangle$ can transform into a linear combination of states within the degenerate manifold. This transformation can be written as
$$\hat{P}_{\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\}} |m, \mathbf{k}\rangle = \sum_n \mathcal{D}_{\mathcal{R}_{\mathbf{t}} \mathbf{k}}^{n,m}(\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\}) |n, \mathcal{R}_{\mathbf{t}} \mathbf{k}\rangle \tag{15}$$

From this point onward, we use the simplified notation $|n, \mathbf{k}\rangle$ to represent one-particle Bloch states. The coefficients $\mathcal{D}_{\mathcal{R}_{\mathbf{t}} \mathbf{k}}^{n, m}(\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\})$ define a unitary transformation matrix associated with the symmetry operation $\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\}$ within the degenerate subspace. These elements are obtained from the overlap between the rotated wave functions and the original states:

$$
\mathcal{D}_{\mathcal{R}_{\mathbf{t}} \mathbf{k}}^{n, m}(\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\}) = \langle n, \mathcal{R}_{\mathbf{t}} \mathbf{k}|\hat{P}_{\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\}}|m, \mathbf{k}\rangle \tag{16}
$$

A particularly important case arises when $\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\} \in \mathcal{G}_{\mathbf{k}}$, where $\mathcal{G}_{\mathbf{k}}$ denotes the little group of the wave vector $\mathbf{k}$, i.e., the subset of the space group symmetry operations that leave $\mathbf{k}$ invariant modulo a reciprocal lattice vector $\mathbf{G}$, such that $\mathcal{R}_{\mathbf{t}} \mathbf{k} = \mathbf{k} \pm \mathbf{G}$. In this case, the transformation reduces to

$$
\mathcal{D}_{\mathcal{R}_{\mathbf{t}} \mathbf{k}}^{n, m}(\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\}) = \langle n, \mathbf{k}|\hat{P}_{\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\}}|m, \mathbf{k}\rangle = U_{\mathbf{k}}^{n, m}(\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\}), \tag{17}
$$

where $U_{\mathbf{k}}^{n, m}(\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\})$ corresponds to an irreducible representation of the symmetry $\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\}$ within the little group $\mathcal{G}_{\mathbf{k}}$. This result implies that, in the presence of degeneracies, symmetry operations act within the degenerate subspace according to irreducible representations of the little group.

For nondegenerate states, the symmetry representation simplifies to a one-dimensional character $e^{i\theta}$, reflecting the fact that the wave function transforms into itself up to a complex phase under $\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\}$. In contrast, for an $n$-fold degenerate manifold, arising, for instance, due to spin, crystal symmetries, or fundamental symmetries such as time reversal, the representation becomes $n$-dimensional. These higher-dimensional irreducible representations determine the structure of degeneracies in the band structure and restrict the allowed symmetry-adapted basis states.

In the case of nonspinor wave functions (i.e., in the absence of spin-orbit coupling), the irreducible representation of the symmetry operation $\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\}$ takes the form

$$
\begin{aligned}
U_{\mathbf{k}}^{m, n}(\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\}) &= \sum_{\mathbf{G}} c_{m, \mathbf{k}}^{*}(\mathcal{R}_{\mathbf{t}} \mathbf{k} - \mathbf{k} + \mathcal{R}_{\mathbf{t}} \mathbf{G}) c_{n, \mathbf{k}}(\mathbf{G}) \\
&\quad \times e^{-i(\mathcal{R}_{\mathbf{t}} \mathbf{k} + \mathcal{R}_{\mathbf{t}} \mathbf{G}) \cdot \mathbf{t}}
\end{aligned} \tag{18}
$$

When spin-orbit coupling is taken into account, the Bloch wave functions become spinors. The transformation properties must then include the spin rotation induced by the symmetry operation. In this case, the representation generalizes to:

$$
U_{\mathbf{k}}^{m, n}(\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\}) = \sum_{\sigma \sigma'} \mathcal{T}_{\mathcal{R}_{\mathbf{t}}}^{\sigma \sigma'} \langle m, \mathbf{k}, \sigma|\hat{P}_{\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\}}|n, \mathbf{k}, \sigma'\rangle \tag{19}
$$

where $\mathcal{T}_{\mathcal{R}_{\mathbf{t}}}^{\sigma \sigma'}$ denotes the matrix elements of the spinor representation corresponding to the point group operation $\mathcal{R}_{\mathbf{t}}$. This formulation captures the combined effect of spatial and spin rotations on the symmetry behavior of Bloch spinors.

We have discussed the action of space group symmetries on Bloch wave functions, where spatial symmetry operations act through unitary transformations representing the real-space rotations, reflections, and translations, along with their corresponding action in reciprocal space. We now turn to the role of time-reversal symmetry, which differs fundamentally from space group operations due to its anti-unitary nature.

Time-reversal symmetry, unlike space group operations, reverses both the momentum and spin of a system and involves complex conjugation. In the spinless case, the time-reversal symmetry operator, $\hat{P}_{\Theta}$, reduces to the complex conjugation operator $\hat{C}$ and relates Bloch states at $\mathbf{k}$ and $-\mathbf{k}$ through:

$$
\hat{P}_{\Theta}|n, \mathbf{k}\rangle = |n, -\mathbf{k}\rangle \tag{20}
$$

In position representation, using the identities $\hat{C}^{\dagger} \mathbf{r} \hat{C} = \mathbf{r}$ and $\hat{C}^{\dagger} \mathbf{k} \hat{C} = -\mathbf{k}$, this becomes:

$$
\hat{P}_{\Theta} \phi_{n, \mathbf{k}}(\mathbf{r}) = \phi_{n, -\mathbf{k}}(\mathbf{r}) = \phi_{n, \mathbf{k}}^{*}(\mathbf{r}) \tag{21}
$$

In the plane-wave basis, this implies the relation:

$$
c_{n, -\mathbf{k}}(\mathbf{G}) = c_{n, \mathbf{k}}^{*}(-\mathbf{G}) \tag{22}
$$

This relation allows wave functions at $-\mathbf{k}$ points in the BZ to be constructed from their time-reversal partners, $\mathbf{k}$, where they have been calculated explicitly. However, the $\boldsymbol{\Gamma}$, i.e. $\mathbf{k}=0$, is a special point, as at this point $\mathbf{k}=-\mathbf{k}$. While the numerically obtained wave functions carry an arbitrary diagonalization phase, $e^{i\alpha_{n, \mathbf{k}}}$ at any $\mathbf{k}$ point for a band index $n$, this phase causes Eq. 22 to not be automatically followed at the $\boldsymbol{\Gamma}$ point. In order to restore time-reversal symmetry at $\boldsymbol{\Gamma}$, one can compute the following representation for each band:

$$
\Theta_{n, \boldsymbol{\Gamma}} = \langle n, \boldsymbol{\Gamma}| \left( \hat{P}_{\Theta}|n, \boldsymbol{\Gamma}\rangle \right) = e^{-2i\alpha_{n, \boldsymbol{\Gamma}}} \tag{23}
$$

The resulting quantity $\Theta_{n, \boldsymbol{\Gamma}}$ is a phase which can be used to construct the time reversal symmetric wave function as $|n, \boldsymbol{\Gamma}\rangle^{TR} = \sqrt{\Theta_{n, \boldsymbol{\Gamma}}}|n, \boldsymbol{\Gamma}\rangle$. Hereafter, the action of time-reversal symmetry will be denoted without explicitly writing the brackets on the right, with the understanding that it represents the operation itself.

For systems with spin-orbit coupling, time-reversal symmetry acts on spinor Bloch wave functions through the operator $\hat{P}_{\Theta}^{sp} = -i\sigma_y \hat{C}$, where $\sigma_y$ is the Pauli matrix acting in spin space. Its action in position representation on the spinor wave function is:

$$
\begin{aligned}
\hat{P}_{\Theta}^{sp} \Phi_{n, \mathbf{k}}(\mathbf{r}) &= \begin{bmatrix}
\phi_{n, -\mathbf{k}, \uparrow}(\mathbf{r}) \\
\phi_{n, -\mathbf{k}, \downarrow}(\mathbf{r})
\end{bmatrix} = -i\sigma_y \hat{C} \begin{bmatrix}
\phi_{n, \mathbf{k}, \uparrow}(\mathbf{r}) \\
\phi_{n, \mathbf{k}, \downarrow}(\mathbf{r})
\end{bmatrix} \\
&= \begin{bmatrix}
-\phi_{n, \mathbf{k}, \downarrow}^{*}(\mathbf{r}) \\
\phi_{n, \mathbf{k}, \uparrow}^{*}(\mathbf{r})
\end{bmatrix}
\end{aligned} \tag{24}
$$

In the plane-wave basis, this leads to the following conditions:

$$
c_{n, -\mathbf{k}, \uparrow}(\mathbf{G}) = -c_{n, \mathbf{k}, \downarrow}^{*}(-\mathbf{G}) \ ; \ \ c_{n, -\mathbf{k}, \downarrow}(\mathbf{G}) = c_{n, \mathbf{k}, \uparrow}^{*}(-\mathbf{G}) \tag{25}
$$

To enforce this condition at the $\Gamma$ point, one computes the time-reversal representation for spinor states analogous to the spinless case, as described in Eq. 23. These symmetry constraints are essential for ensuring the correct transformation behavior of wave functions under time-reversal, particularly in systems with spin-orbit coupling and in the construction of time reversal symmetric excitonic states, which will be discussed next.

### B. Excitons and translational symmetry

The study of electron-hole excitations from the many-body ground state $|N,0\rangle$ to an excited state $|N,S\rangle$ can be rigorously formulated within the framework of the two-particle Green's function and its equation of motion, the Bethe-Salpeter equation (BSE) [41]. Here, $S$ labels the excitation, while $N$ denotes the conserved total number of electrons. Such excitations correspond to the creation of an electron in a conduction-band state and the removal of an electron from a valence-band state (equivalently, the creation of a hole).

Following the work of Strinati [41], the electron-hole amplitude is defined from the electron-hole correlation function as
$$
\Psi_{S}(\mathbf{x}, \mathbf{x}^{\prime})=-\langle N, 0|\hat{\Phi}^{\dagger}(\mathbf{x}^{\prime}) \hat{\Phi}(\mathbf{x})| N, S\rangle\qquad(26)
$$
where $\hat{\Phi}^{\dagger}(\mathbf{x}^{\prime})$ and $\hat{\Phi}(\mathbf{x})$ create and annihilate an electron at positions $\mathbf{x}^{\prime}$ and $\mathbf{x}$, respectively.

Within the Tamm-Dancoff approximation (TDA), $\Psi_{S}(\mathbf{x}, \mathbf{x}^{\prime})$ admits the expansion
$$
\Psi_{S}(\mathbf{x}, \mathbf{x}^{\prime})=\sum_{v}^{\text {occ }} \sum_{c}^{\text {empty }} A_{v c}^{S} \Phi_{v}^{*}(\mathbf{x}^{\prime}) \Phi_{c}(\mathbf{x})\qquad(27)
$$
where $\Phi_{v}(\mathbf{x}^{\prime})$ and $\Phi_{c}(\mathbf{x})$ are single-particle valence and conduction wave functions. The expansion coefficients are given by
$$
A_{v c}^{S}=\left\langle N, 0\left|\hat{b}_{c} \hat{a}_{v}\right| N, S\right\rangle\qquad(28)
$$
with $\hat{a}_{v}^{\dagger}$ creating a hole in state $v$ and $\hat{b}_{c}^{\dagger}$ creating an electron in state $c$.

In periodic systems, the BSE Hamiltonian respects lattice translational symmetry. As a result, the two-particle translational operator $\hat{T}_{\mathbf{R}}^{\text {ex }}$ commutes with the BSE Hamiltonian $\hat{\mathcal{H}}_{\text {BSE }}$ (see Appendix B). This allows the excitations to be labeled by a conserved total momentum $\mathbf{Q}$, which is a good quantum number. The electron-hole amplitude associated with the finite momentum $\mathbf{Q}$ can then be written as:
$$
\Psi_{S, \mathbf{Q}}(\mathbf{r}_{e}, \mathbf{r}_{h})=\sum_{v, c, \mathbf{k}} A_{v, c, \mathbf{k}}^{S, \mathbf{Q}} \Phi_{c, \mathbf{k}}(\mathbf{r}_{e}) \Phi_{v, \mathbf{k}-\mathbf{Q}}^{*}(\mathbf{r}_{h})\qquad(29)
$$
where $\Phi_{c, \mathbf{k}}(\mathbf{r}_{e})$ and $\Phi_{v, \mathbf{k}-\mathbf{Q}}(\mathbf{r}_{h})$ are Bloch wave functions evaluated at the electron and hole coordinates $\mathbf{r}_{e}$ and $\mathbf{r}_{h}$, respectively. From this point onward, we use the ket, $|S, \mathbf{Q}\rangle$, to represent the electron-hole amplitude state whose spatial representation is given in Eq. (29). Since the hole is generated by removing an electron at $\mathbf{k}-\mathbf{Q}$, its momentum is $-(\mathbf{k}-\mathbf{Q})=\mathbf{Q}-\mathbf{k}$. This allows it to be represented by the time reversal of the valence-band electron state $|v, \mathbf{k}-\mathbf{Q}\rangle$. The excited state can thus be expressed in the product basis as
$$
|S, \mathbf{Q}\rangle=\sum_{v, c, \mathbf{k}} A_{v, c, \mathbf{k}}^{S, \mathbf{Q}}|v, \mathbf{k}-\mathbf{Q} ; c, \mathbf{k}\rangle\qquad(30)
$$
with
$$
|v, \mathbf{k}-\mathbf{Q} ; c, \mathbf{k}\rangle=\hat{P}_{\Theta}^{h}|v, \mathbf{k}-\mathbf{Q}\rangle \otimes|c, \mathbf{k}\rangle\qquad(31)
$$

The excitonic Hilbert space is as a result a direct product of the electron and hole Hilbert spaces. Introducing center-of-mass and relative coordinates, $\mathbf{R}=\alpha \mathbf{r}_{e}+\beta \mathbf{r}_{h}$ (with $\alpha+\beta=1$) and $\mathbf{r}=\mathbf{r}_{e}-\mathbf{r}_{h}$, respectively, Eq. (29) takes the Bloch-periodic form
$$
\Psi_{S, \mathbf{Q}}(\mathbf{R}, \mathbf{r})=e^{i \mathbf{Q} \cdot \mathbf{R}} F_{S, \mathbf{Q}}(\mathbf{R}, \mathbf{r})\qquad(32)
$$
where the phase factor encodes the exciton's total momentum and $F_{S, \mathbf{Q}}(\mathbf{R}, \mathbf{r})$ contains the cell-periodic structure (see Appendix B). This generalizes the singleparticle Bloch theorem to the interacting two-particle excitonic case. The coefficients $A_{v, c, \mathbf{k}}^{S, \mathbf{Q}}$ and energies $\Omega_{S, \mathbf{Q}}$ are obtained by solving the BSE eigenvalue problem at fixed $\mathbf{Q}$:
$$
\begin{aligned}
& \left(\epsilon_{c, \mathbf{k}}-\epsilon_{v, \mathbf{k}-\mathbf{Q}}\right) A_{v, c, \mathbf{k}}^{S, \mathbf{Q}}+\sum_{v^{\prime}, c^{\prime}, \mathbf{k}^{\prime}}\left\langle v, \mathbf{k}-\mathbf{Q} ; c, \mathbf{k}\left|K^{e h}\right.\right. \\
& \left.\left|v^{\prime}, \mathbf{k}^{\prime}-\mathbf{Q} ; c^{\prime}, \mathbf{k}^{\prime}\right\rangle A_{v^{\prime}, c^{\prime}, \mathbf{k}^{\prime}}^{S, \mathbf{Q}}=\Omega_{S, \mathbf{Q}} A_{v, c, \mathbf{k}}^{S, \mathbf{Q}}\right.
\end{aligned}\qquad(33)
$$

### C. Excitons and time-reversal symmetry

We begin by defining the time-reversal operator for excitons as the tensor product of the time-reversal operators acting individually on the valence hole and conduction electron:
$$
\hat{P}_{\Theta}^{e x}=\hat{P}_{\Theta}^{h} \otimes \hat{P}_{\Theta}^{e}\qquad(34)
$$

Since the excitonic Hamiltonian commutes with the timereversal operator, the exciton eigenstates at momentum $\mathbf{Q}$ and $-\mathbf{Q}$ are related by time reversal symmetry (see Appendix C):
$$
\Omega_{S, \mathbf{Q}}=\Omega_{S,-\mathbf{Q}}, \quad \hat{P}_{\Theta}^{e x}|S, \mathbf{Q}\rangle=|S,-\mathbf{Q}\rangle\qquad(35)
$$

In the real-space representation, this relation resembles the transformation of single-particle wave functions under time-reversal and can be expressed as:
$$
\hat{P}_{\Theta}^{e x} \Psi_{S, \mathbf{Q}}\left(\mathbf{r}_{e}, \mathbf{r}_{h}\right)=\Psi_{S, \mathbf{Q}}^{*}\left(\mathbf{r}_{e}, \mathbf{r}_{h}\right)=\Psi_{S,-\mathbf{Q}}\left(\mathbf{r}_{e}, \mathbf{r}_{h}\right)\quad(36)
$$

We now derive the explicit transformation of the exciton expansion coefficients under time-reversal symmetry by

examining the action of $\hat{P}_{\Theta}^{ex}$ on the excitonic state. The transformation takes the form:
$$
\begin{aligned}
|S,-\mathbf{Q}\rangle & =\hat{P}_{\Theta}^{e x}|S, \mathbf{Q}\rangle \\
& =\sum_{v, c, \mathbf{k}}\left(A_{v, c, \mathbf{k}}^{S, \mathbf{Q}}\right)^{*}\left[\hat{P}_{\Theta}^{h} \hat{P}_{\Theta}^{h}|v, \mathbf{k}-\mathbf{Q}\rangle\right] \otimes\left[\hat{P}_{\Theta}^{e}|c, \mathbf{k}\rangle\right] \\
& (37)
\end{aligned}
$$

As $\hat{P}_{\Theta}^{e x}$ is an antilinear operator, it not only transforms the basis states but also complex conjugates the exciton coefficients.

Using the known time-reversal properties of the oneelectron Bloch states, namely
$$
\hat{P}_{\Theta}^{h}|v, \mathbf{k}-\mathbf{Q}\rangle=|v,-\mathbf{k}+\mathbf{Q}\rangle, \quad \hat{P}_{\Theta}^{e}|c, \mathbf{k}\rangle=|c,-\mathbf{k}\rangle \quad(38)
$$

Eq. 37 becomes
$$
\begin{aligned}
|S,-\mathbf{Q}\rangle & =\sum_{v, c, \mathbf{k}}\left(A_{v, c, \mathbf{k}}^{S, \mathbf{Q}}\right)^{*}\left[\hat{P}_{\Theta}^{h}|v,-\mathbf{k}+\mathbf{Q}\rangle\right] \otimes|c,-\mathbf{k}\rangle \\
& =\sum_{v, c, \mathbf{k}}\left(A_{v, c,-\mathbf{k}}^{S, \mathbf{Q}}\right)^{*}\left[\hat{P}_{\Theta}^{h}|v, \mathbf{k}+\mathbf{Q}\rangle\right] \otimes|c, \mathbf{k}\rangle \quad(39)
\end{aligned}
$$

By comparing this with the exciton state $|S,-\mathbf{Q}\rangle$ expressed in the product-state basis $\hat{P}_{\Theta}^{h}|v, \mathbf{k}+\mathbf{Q}\rangle \otimes|c, \mathbf{k}\rangle$, we identify the transformation law for the exciton wave function coefficients under time reversal:
$$
\tilde{A}_{v, c, \mathbf{k}}^{S,-\mathbf{Q}}=\left(A_{v, c,-\mathbf{k}}^{S, \mathbf{Q}}\right)^{*}
\tag{40}
$$

This result holds provided that the one-electron wave functions are constructed on a time-reversal symmetric $\mathbf{k}$ grid and are generated over the full Brillouin zone, ensuring time-reversal symmetry is preserved in both spinless and spinor systems. In particular, at $\mathbf{k}=0$, the wave functions must explicitly satisfy time-reversal symmetry (see subsection A). This typically requires removing the arbitrary diagonalization phases at $\Gamma$, which can be achieved by computing the time-reversal representation matrices $\Theta_{n, \Gamma}$, as discussed in Eq. 23.

### D. Excitons and space group symmetries

We define the action of a space group symmetry operation on the excitonic state as the tensor product of symmetry operators acting on the valence hole and conduction electron:
$$
\hat{P}_{\left\{\mathcal{R}_{\mathbf{t}} \mid \mathbf{t}\right\}}^{e x}=\hat{P}_{\left\{\mathcal{R}_{\mathbf{t}} \mid \mathbf{t}\right\}}^{h} \otimes \hat{P}_{\left\{\mathcal{R}_{\mathbf{t}} \mid \mathbf{t}\right\}}^{e}
\tag{41}
$$

Since the Bethe-Salpeter Hamiltonian commutes with the excitonic symmetry operator, i.e., $\left[\hat{P}_{\left\{\mathcal{R}_{\mathbf{t}} \mid \mathbf{t}\right\}}^{e x}, \hat{\mathcal{H}}_{\mathrm{BSE}}\right]=0$, and the electron-hole amplitudes exhibit Bloch periodicity under symmetry actions (see Appendix D), we obtain:
$$
\Omega_{S, \mathcal{R}_{\mathbf{t}} \mathbf{Q}}=\Omega_{S, \mathbf{Q}}, \quad\left|S, \mathcal{R}_{\mathbf{t}} \mathbf{Q}\right\rangle=\hat{P}_{\left\{\mathcal{R}_{\mathbf{t}} \mid \mathbf{t}\right\}}^{e x}|S, \mathbf{Q}\rangle \quad(42)
$$

This symmetry relation guarantees that excitonic eigenstates transform consistently under lattice symmetries, analogous to single-particle Bloch states.

Utilizing this framework, we can derive a relation between the coefficients $A_{v, c, \mathbf{k}}^{S, \mathbf{Q}}$ and those of the transformed state $\tilde{A}_{v, c, \mathbf{k}}^{S, \mathcal{R}_{\mathbf{t}} \mathbf{Q}}$, akin to the transformation properties of single-particle coefficients $c_{n, \mathbf{k}}(\mathbf{G})$ and $c_{n, \mathcal{R}_{\mathbf{t}} \mathbf{k}}^{\mathbf{t}}(\mathbf{G})$ as seen in Eq. 7.

The transformation of the excitonic state under symmetry becomes:
$$
\begin{aligned}
\left|S, \mathcal{R}_{\mathbf{t}} \mathbf{Q}\right\rangle & =\hat{P}_{\left\{\mathcal{R}_{\mathbf{t}} \mid \mathbf{t}\right\}}^{e x}|S, \mathbf{Q}\rangle= \\
\sum_{v, c, \mathbf{k}} A_{v, c, \mathbf{k}}^{S, \mathbf{Q}} & {\left[\hat{P}_{\left\{\mathcal{R}_{\mathbf{t}} \mid \mathbf{t}\right\}}^{h} \hat{P}_{\Theta}^{h}|v, \mathbf{k}-\mathbf{Q}\rangle\right] \otimes\left[\hat{P}_{\left\{\mathcal{R}_{\mathbf{t}} \mid \mathbf{t}\right\}}^{e}|c, \mathbf{k}\rangle\right] }
\end{aligned}
$$
(43)
and, expanding the action of these operators in their respective degenerate subspaces, we obtain
$$
\begin{aligned}
\left|S, \mathcal{R}_{\mathbf{t}} \mathbf{Q}\right\rangle= & \sum_{v^{\prime}, c^{\prime}, \mathbf{k}}\left[\sum_{v, c} A_{v, c, \mathcal{R}_{\mathbf{t}}^{-1} \mathbf{k}}^{S, \mathbf{Q}} \mathcal{L}_{\mathbf{k}-\mathcal{R}_{\mathbf{t}} \mathbf{Q}}^{v^{\prime}, v}\left(\left\{\mathcal{R}_{\mathbf{t}} \mid \mathbf{t}\right\}\right)\right. \\
& \left.\otimes \mathcal{D}_{\mathbf{k}}^{c^{\prime}, c}\left(\left\{\mathcal{R}_{\mathbf{t}} \mid \mathbf{t}\right\}\right)\right]\left|v^{\prime}, \mathbf{k}-\mathcal{R}_{\mathbf{t}} \mathbf{Q}\right\rangle \otimes\left|c^{\prime}, \mathbf{k}\right\rangle \quad(44)
\end{aligned}
$$
where the matrix elements for conduction and valence band transformations are defined as
$$
\mathcal{D}_{\mathbf{k}}^{c^{\prime}, c}\left(\left\{\mathcal{R}_{\mathbf{t}} \mid \mathbf{t}\right\}\right)=\left\langle c^{\prime}, \mathbf{k}\left|\hat{P}_{\left\{\mathcal{R}_{\mathbf{t}} \mid \mathbf{t}\right\}}^{e}\right| c, \mathcal{R}_{\mathbf{t}}{ }^{-1} \mathbf{k}\right\rangle\quad (45)
$$

$$
\begin{aligned}
\mathcal{L}_{\mathbf{k}-\mathcal{R}_{\mathbf{t}} \mathbf{Q}}^{v^{\prime}, v} & \left(\left\{\mathcal{R}_{\mathbf{t}} \mid \mathbf{t}\right\}\right)=\left\langle v^{\prime}, \mathbf{k}-\mathcal{R}_{\mathbf{t}} \mathbf{Q}\right| \hat{P}_{\Theta}^{h} \dagger \hat{P}_{\left\{\mathcal{R}_{\mathbf{t}} \mid \mathbf{t}\right\}}^{h} \\
& \times \hat{P}_{\Theta}^{h}\left|v, \mathcal{R}_{\mathbf{t}}^{-1}\left(\mathbf{k}-\mathcal{R}_{\mathbf{t}} \mathbf{Q}\right)\right\rangle=\left[\mathcal{D}_{\mathbf{k}-\mathcal{R}_{\mathbf{t}} \mathbf{Q}}^{v^{\prime}, v}\left(\left\{\mathcal{R}_{\mathbf{t}} \mid \mathbf{t}\right\}\right)\right]^{*} \quad(46)
\end{aligned}
$$

The transformed exciton coefficients are then given by
$$
\begin{aligned}
\tilde{A}_{v, c, \mathbf{k}}^{S, \mathcal{R}_{\mathbf{t}} \mathbf{Q}}= & \sum_{v^{\prime}, c^{\prime}} A_{v^{\prime}, c^{\prime}, \mathcal{R}_{\mathbf{t}}^{-1} \mathbf{k}}^{S, \mathbf{Q}} \\
& {\left[\mathcal{D}_{\mathbf{k}-\mathcal{R}_{\mathbf{t}} \mathbf{Q}}^{v, v^{\prime}}\left(\left\{\mathcal{R}_{\mathbf{t}} \mid \mathbf{t}\right\}\right)\right]^{*} \otimes \mathcal{D}_{\mathbf{k}}^{c, c^{\prime}}\left(\left\{\mathcal{R}_{\mathbf{t}} \mid \mathbf{t}\right\}\right) }
\end{aligned}
$$
(47)

This can be written compactly using matrix-vector multiplication, where the transformation matrix has elements
$$
\mathcal{M}_{v, c ; v^{\prime}, c^{\prime}}^{\mathbf{k}, \mathbf{Q}}\left(\left\{\mathcal{R}_{\mathbf{t}} \mid \mathbf{t}\right\}\right)=\left[\mathcal{D}_{\mathbf{k}-\mathcal{R}_{\mathbf{t}} \mathbf{Q}}^{v, v^{\prime}}\left(\left\{\mathcal{R}_{\mathbf{t}} \mid \mathbf{t}\right\}\right)\right]^{*} \otimes \mathcal{D}_{\mathbf{k}}^{c, c^{\prime}}\left(\left\{\mathcal{R}_{\mathbf{t}} \mid \mathbf{t}\right\}\right)
$$
(48)
and the matrix form becomes
$$
\begin{aligned}
{\left[\tilde{A}_{\mathbf{k}}^{S, \mathcal{R}_{\mathbf{t}} \mathbf{Q}}\right]_{v, c} } & =\sum_{v^{\prime}, c^{\prime}} \mathcal{M}_{v, c ; v^{\prime}, c^{\prime}}^{\mathbf{k}, \mathbf{Q}}\left(\left\{\mathcal{R}_{\mathbf{t}} \mid \mathbf{t}\right\}\right) A_{v^{\prime}, c^{\prime}, \mathcal{R}_{\mathbf{t}}^{-1} \mathbf{k}}^{S, \mathbf{Q}} \\
& =\left[\mathcal{M}^{\mathbf{k}, \mathbf{Q}}\left(\left\{\mathcal{R}_{\mathbf{t}} \mid \mathbf{t}\right\}\right) \cdot A_{\mathcal{R}_{\mathbf{t}}^{-1} \mathbf{k}}^{S, \mathbf{Q}}\right]_{v, c}
\end{aligned}
$$
(49)

Thus the transformation of the exciton coefficient vector at each $\mathbf{k}$-point simplifies to
$$
\tilde{A}_{\mathbf{k}}^{S, \mathcal{R}_{\mathbf{t}} \mathbf{Q}}=\mathcal{M}^{\mathbf{k}, \mathbf{Q}}\left(\left\{\mathcal{R}_{\mathbf{t}} \mid \mathbf{t}\right\}\right) \cdot A_{\mathcal{R}_{\mathbf{t}}^{-1} \mathbf{k}}^{S, \mathbf{Q}}
\tag{50}
$$

When dealing with spinor wave functions, the symme-
try operator $\hat{P}_{\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\}}^{h/e}$ must be replaced with the product
$\hat{P}_{\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\}}^{h/e} \otimes \hat{\mathcal{T}}_{\mathcal{R}_{\mathbf{t}}}^{v/c}$, where $\hat{\mathcal{T}}_{\mathcal{R}_{\mathbf{t}}}$ denotes the SU(2) rotation
corresponding to the SO(3) spatial symmetry $\mathcal{R}_{\mathbf{t}}$. This
ensures that spinor structure is correctly accounted for,
consistent with the spin representations corresponding to
Eq. 14.

### E. Symmetry classification of excitons
Exciton bands can be classified according to the irre-
ducible representations of the symmetry group, in anal-
ogy with single-particle bands. This classification is pos-
sible now that we have established how excitonic states
transform under symmetry operations. The definition of
the little group is also analogous, with the key distinc-
tion being that, for excitons, it is defined with respect
to the center-of-mass (c.m.) momentum $\mathbf{Q}$. The little
group $\mathcal{G}_{\mathbf{Q}}$ consists of all symmetry operations $\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\}$ that
leave $\mathbf{Q}$ invariant up to a reciprocal lattice vector, i.e.,
$\mathcal{R}_{\mathbf{t}}\mathbf{Q} = \mathbf{Q} \pm \mathbf{G}$. For any such $\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\} \in \mathcal{G}_{\mathbf{Q}}$, the excitonic
state $|S, \mathbf{Q}\rangle$ transforms as
$$
\hat{P}_{\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\}}^{ex}|S, \mathbf{Q}\rangle = \sum_{S'=1}^{N_{exc}} \mathcal{K}_{\mathbf{Q}}^{S',S}(\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\})|S', \mathbf{Q}\rangle \tag{51}
$$

Here, $\mathcal{K}_{\mathbf{Q}}(\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\})$ forms a representation of the little
group $\mathcal{G}_{\mathbf{Q}}$ within the invariant subspace spanned by the
excitonic states $\{|S, \mathbf{Q}\rangle\}_{N_{exc}}$. Its matrix elements are
given by
$$
\mathcal{K}_{\mathbf{Q}}^{S',S}(\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\}) = \langle S', \mathbf{Q}|\hat{P}_{\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\}}^{ex}|S, \mathbf{Q}\rangle \tag{52}
$$

The action of $\hat{P}_{\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\}}^{ex}$ on $|S, \mathbf{Q}\rangle$, using Eqs. 43 and 50,
leads to
$$
\hat{P}_{\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\}}^{ex}|S, \mathbf{Q}\rangle = \sum_{v',c',\mathbf{k}'} \tilde{A}_{v',c',\mathbf{k}'}^{S,\mathbf{Q}}[\hat{P}_{\Theta}^{h}|v', \mathbf{k}' - \mathbf{Q}\rangle] \otimes |c', \mathbf{k}'\rangle \tag{53}
$$

To compute the matrix elements of the representation,
we expand $|S', \mathbf{Q}\rangle$ in the electron-hole basis and evaluate
the overlap:
$$
\begin{aligned}
\mathcal{K}_{\mathbf{Q}}^{S',S}(\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\}) =& \sum_{v,c,v',c',\mathbf{k},\mathbf{k}'} \left(A_{v,c,\mathbf{k}}^{S',\mathbf{Q}}\right)^* \tilde{A}_{v',c',\mathbf{k}'}^{S,\mathbf{Q}} \\
& \langle v, \mathbf{k} - \mathbf{Q}|\hat{P}_{\Theta}^{h\dagger} \hat{P}_{\Theta}^{h}|v', \mathbf{k}' - \mathbf{Q}\rangle\langle c, \mathbf{k}|c', \mathbf{k}'\rangle
\tag{54}
\end{aligned}
$$

Using orthonormality of the electronic states and
$\hat{P}_{\Theta}^{h,\dagger} \hat{P}_{\Theta}^{h} = I$, this expression simplifies to
$$
\mathcal{K}_{\mathbf{Q}}^{S',S}(\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\}) = \sum_{v,c,v',c',\mathbf{k},\mathbf{k}'} \left(A_{v,c,\mathbf{k}}^{S',\mathbf{Q}}\right)^* \tilde{A}_{v',c',\mathbf{k}'}^{S,\mathbf{Q}} \delta_{v,v'} \delta_{c,c'} \delta_{\mathbf{k},\mathbf{k}'} \tag{55}
$$
yielding
$$
\mathcal{K}_{\mathbf{Q}}^{S',S}(\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\}) = \sum_{v,c,\mathbf{k}} \left(A_{v,c,\mathbf{k}}^{S',\mathbf{Q}}\right)^* \tilde{A}_{v,c,\mathbf{k}}^{S,\mathbf{Q}} \tag{56}
$$

Finally, using Eq. 50, we obtain a compact form:
$$
\begin{aligned}
& \mathcal{K}_{\mathbf{Q}}^{S',S}(\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\}) \\
& = \sum_{v,c,\mathbf{k}} \left[A_{\mathbf{k}}^{S',\mathbf{Q}}\right]_{v,c}^* \left[\mathcal{M}^{\mathbf{k},\mathbf{Q}}(\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\}) A_{\mathcal{R}_{\mathbf{t}}^{-1}\mathbf{k}}^{S,\mathbf{Q}}\right]_{v,c}
\tag{57}
\end{aligned}
$$

Each representation $\mathcal{K}_{\mathbf{Q}}$ is characterized by its trace,
known as the character:
$$
\mathcal{K}_{\mathcal{K}_{\mathbf{Q}}}(\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\}) = \mathrm{Tr}[\mathcal{K}_{\mathbf{Q}}(\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\})] = \sum_{S} \mathcal{K}_{\mathbf{Q}}^{S,S}(\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\}) \tag{58}
$$

In general, the invariant subspace spanned by
$\{|S, \mathbf{Q}\rangle\}_{N_{exc}}$ may decompose into a direct sum of
multiple irreducible representations. Therefore, the rep-
resentation $\mathcal{K}_{\mathbf{Q}}$ may be reducible and can be expressed
as
$$
\mathcal{K}_{\mathbf{Q}} = \oplus_n m_{\mathbf{Q}}^{\xi_n} \mathcal{K}_{\mathbf{Q}}^{\xi_n} \tag{59}
$$

Here, $\mathcal{K}_{\mathbf{Q}}^{\xi_n}$ is the $n^{\mathrm{th}}$ irreducible representation of $\mathcal{G}_{\mathbf{Q}}$
($n = 1, \dots, N_{\xi}$), with $N_{\xi}$ denoting the total number of
such representations. The coefficient $m_{\mathbf{Q}}^{\xi_n}$ indicates the
multiplicity of $\mathcal{K}_{\mathbf{Q}}^{\xi_n}$ in $\mathcal{K}_{\mathbf{Q}}$. This multiplicity can be com-
puted using
$$
m_{\mathbf{Q}}^{\xi_n} = \frac{1}{N_{\mathcal{G}_{\mathbf{Q}}}} \sum_{\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\} \in \mathcal{G}_{\mathbf{Q}}} \mathcal{K}_{\mathcal{K}_{\mathbf{Q}}}^*(\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\}) \mathcal{K}_{\xi_n}(\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\}) \tag{60}
$$
where $N_{\mathcal{G}_{\mathbf{Q}}}$ is the order of the group and $\mathcal{K}_{\xi_n}(\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\})$
is the character of the group element $\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\}$ in the $n^{\mathrm{th}}$
irreducible representation, which can be obtained from
symmetry tools such as SPGREP.

To assign each excitonic state to a specific irreducible
representation, we use the corresponding projection op-
erator:
$$
\hat{\mathcal{V}}_{ij;\mathbf{Q}}^{(\xi_n)} = \frac{d_{\xi_n}}{N_{\mathcal{G}_{\mathbf{Q}}}} \sum_{\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\} \in \mathcal{G}_{\mathbf{Q}}} \left[\Delta_{ij}^{(\xi_n)}(\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\})\right]^* \hat{P}_{\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\}}^{ex} \tag{61}
$$

Here, $\hat{\mathcal{V}}_{ij;\mathbf{Q}}^{(\xi_n)}$ projects onto the subspace transforming as
the irreducible representation $\xi_n$ with dimension $d_{\xi_n}$ and
$\Delta_{ij}^{(\xi_n)}(\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\})$ is the corresponding matrix representation
of the symmetry operation $\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\}$.

Symmetry-based classification of excitons provides sig-
nificant physical insight. States transforming under one-
dimensional irreducible representations are nondegener-
ate, whereas higher-dimensional irreducible representa-
tions give rise to degeneracies. These degeneracies can be
lifted by perturbations such as spin-orbit coupling or ex-
ternal fields. Moreover, the symmetry of excitonic states
plays a crucial role in determining optical selection rules
and polarization properties.

### F. Symmetry-adapted reduction in the BSE Hamiltonian
For space group operations $\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\} \in \mathcal{G}$, the excitonic
symmetry operator commutes with the Bethe-Salpeter

Hamiltonian, i.e., $\left[\hat{P}_{\{\mathcal{R}_{\mathbf{t}} \mid \mathbf{t}\}}^{e x}, \hat{\mathcal{H}}_{\mathrm{BSE}}\right]=0$. This invariance under symmetry operations implies (by arguments similar to those presented in Appendix A for Bloch states) that the Hamiltonian blocks at exciton center-of-mass momenta $\mathbf{Q}$ and $\mathcal{R}_{\mathbf{t}} \mathbf{Q}$ are related as
$$
\hat{P}_{\left\{\mathcal{R}_{\mathbf{t}} \mid \mathbf{t}\right\}}^{e x} \hat{\mathcal{H}}_{\mathbf{Q}}^{\mathrm{BSE}}\left(\hat{P}_{\left\{\mathcal{R}_{\mathbf{t}} \mid \mathbf{t}\right\}}^{e x}\right)^{-1}=\hat{\mathcal{H}}_{\mathcal{R}_{\mathbf{t}} \mathbf{Q}}^{\mathrm{BSE}}
\tag{62}
$$

This means that, for operations not in the little group $\mathcal{G}_{\mathbf{Q}}$, the symmetry connects different momentum sectors. However, when $\left\{\mathcal{R}_{\mathbf{t}} \mid \mathbf{t}\right\} \in \mathcal{G}_{\mathbf{Q}}$, i.e., they leave $\mathbf{Q}$ invariant, the Hamiltonian satisfies
$$
\hat{P}_{\left\{\mathcal{R}_{\mathbf{t}} \mid \mathbf{t}\right\}}^{e x} \hat{\mathcal{H}}_{\mathbf{Q}}^{\mathrm{BSE}}\left(\hat{P}_{\left\{\mathcal{R}_{\mathbf{t}} \mid \mathbf{t}\right\}}^{e x}\right)^{-1}=\hat{\mathcal{H}}_{\mathbf{Q}}^{\mathrm{BSE}}
\tag{63}
$$

Thus $\hat{\mathcal{H}}_{\mathbf{Q}}^{\mathrm{BSE}}$ transforms as a representation of the little group $\mathcal{G}_{\mathbf{Q}}$. In cases where this representation is reducible, as commonly happens at high-symmetry points like $\mathbf{Q}=0$ or others with less symmetries, the Hamiltonian can be block diagonalized into subspaces associated with irreducible representations, greatly simplifying the diagonalization.

We now outline the general formalism for constructing symmetry-adapted irreducible blocks of the Hamiltonian, valid at both zero and finite $\mathbf{Q}$. A key step involves using the projection operators [defined in Eq. 61], which were earlier used for exciton classification. Here, they serve to build symmetry-adapted product state bases that isolate irreducible subspaces of the Hilbert space, enabling block diagonalization.

By applying these projectors to the exciton product basis defined in Eq. 31, and using the transformation law in Eq. 15, we obtain the symmetry-adapted basis as follows. For each irreducible representation $\xi_{n}$, we construct $d_{\xi_{n}}^{2} N_{c} N_{v} N_{\mathbf{k}}$ linear combinations with $i, j=1, \ldots, d_{\xi_{n}}$ using Eq. 64 given below:
$$
\begin{aligned}
&\left|\psi_{(i, j) ; v, c, \mathbf{k}, \mathbf{Q}}^{\left(\xi_{n}\right)}\right\rangle=\hat{\mathcal{V}}_{i j ; \mathbf{Q}}^{\left(\xi_{n}\right)}|v, \mathbf{k}-\mathbf{Q} ; c, \mathbf{k}\rangle \\
&=\frac{d_{\xi_{n}}}{N_{\mathcal{G}_{\mathbf{Q}}}} \sum_{\left\{\mathcal{R}_{\mathbf{t}} \mid \mathbf{t}\right\} \in \mathcal{G}_{\mathbf{Q}}}\left[\Delta_{i j}^{\left(\xi_{n}\right)}\left(\left\{\mathcal{R}_{\mathbf{t}} \mid \mathbf{t}\right\}\right)\right]^{*} \hat{P}_{\left\{\mathcal{R}_{\mathbf{t}} \mid \mathbf{t}\right\}}^{e x}|v, \mathbf{k}-\mathbf{Q} ; c, \mathbf{k}\rangle \\
&=\frac{d_{\xi_{n}}}{N_{\mathcal{G}_{\mathbf{Q}}}} \sum_{\substack{v^{\prime}, c^{\prime}, \\\left\{\mathcal{R}_{\mathbf{t}} \mid \mathbf{t}\right\} \in \mathcal{G}_{\mathbf{Q}}}}\left[\Delta_{i j}^{\left(\xi_{n}\right)}\left(\left\{\mathcal{R}_{\mathbf{t}} \mid \mathbf{t}\right\}\right)\right]^{*}\left[\mathcal{D}_{\mathcal{R}_{\mathbf{t}} \mathbf{k}-\mathbf{Q}}^{v^{\prime}, v}\left(\left\{\mathcal{R}_{\mathbf{t}} \mid \mathbf{t}\right\}\right)\right]^{*} \\
& \otimes \mathcal{D}_{\mathcal{R}_{\mathbf{t}} \mathbf{k}}^{c^{\prime}, c}\left(\left\{\mathcal{R}_{\mathbf{t}} \mid \mathbf{t}\right\}\right)\left|v^{\prime}, \mathcal{R}_{\mathbf{t}} \mathbf{k}-\mathbf{Q} ; c^{\prime}, \mathcal{R}_{\mathbf{t}} \mathbf{k}\right\rangle
\end{aligned}
\tag{64}
$$

However, these linear combinations form a set containing null as well as linearly dependent vectors. Using SPGREP, we extract a linearly independent subset $\left\{\left|\psi_{(i, j) ; v, c, \mathbf{k}, \mathbf{Q}}^{\left(\xi_{n}\right)}\right\rangle\right\}$ by removing the redundant and null vectors. This subset constitutes the symmetry-adapted basis corresponding to the irreducible representation $\xi_{n}$. The number of vectors in this set are $l_{\mathbf{Q}}^{\xi_{n}}=d_{\xi_{n}} m_{\mathbf{Q}}^{\xi_{n}}$, the dimension times the multiplicity of the irreducible representation $\xi_{n}$ in the representation $\mathcal{K}_{\mathbf{Q}}$. By the orthogonality theorem, the bases constructed in this way for distinct irreducible representations are mutually orthogonal. Since the dimensions of the irreducible representations satisfy the relation $\sum_{n} d_{\xi_{n}}^{2}=N_{\mathcal{G}_{\mathbf{Q}}}$, the expected number of symmetry-adapted basis vectors $l_{\mathbf{Q}}^{\xi_{n}}$ associated with a given irreducible representation $\xi_{n}$ is approximately $d_{\xi_{n}}^{2} N_{c} N_{v} N_{\mathbf{k}} / N_{\mathcal{G}_{\mathbf{Q}}}$, where the approximation arises from the finite size of the basis. In all the cases we have studied (see Section IV on results and discussion), we find that $l_{\mathbf{Q}}^{\xi_{n}}$ is close to this estimate.

When the BSE Hamiltonian is expressed in this basis, it takes a block-diagonal form:
$$
\left[\begin{array}{ccccc}
\mathcal{H}^{(1)} & 0 & 0 & \cdots & 0 \\
0 & \mathcal{H}^{(2)} & 0 & \cdots & 0 \\
0 & 0 & \mathcal{H}^{(3)} & \cdots & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
0 & 0 & 0 & \cdots & \mathcal{H}^{\left(N_{\xi}\right)}
\end{array}\right]
\tag{65}
$$

Each block $\mathcal{H}^{(n)}$ represents an independent sector corresponding to the irreducible representation $\xi_{n}$ of $\mathcal{G}_{\mathbf{Q}}$.

This decomposition stems directly from group representation theory, where the exciton basis and symmetry operators form a reducible representation. Projection operators as discussed above allow one to isolate irreducible sectors, ensuring orthogonality and eliminating couplings between different symmetry blocks.

Physically, these blocks correspond to excitonic states categorized by their symmetry. This classification is useful for identifying bright and dark excitons depending on their symmetry behavior under optical transitions. Computationally, this structure enables solving several smaller eigenvalue problems rather than a single large one, making the BSE calculations more tractable and symmetry-respecting.

## III. COMPUTATIONAL DETAILS

For our calculations, we used the experimental in-plane lattice constants for monolayer $\mathrm{MoS}_{2}$ (3.168 Å, S-S distance of $3.133 \AA$ ). A vacuum spacing of $16 \AA$ was introduced along the out-of-plane direction to avoid spurious interactions between periodic images.

Density functional theory (DFT) calculations were performed with the QUANTUM ESPRESSO [24, 42] package using the PBE generalized gradient approximation (GGA) [43] for the exchange-correlation functional. The wave functions were expanded in plane waves up to an energy cutoff of 90 Ry. Spin-orbit coupling was explicitly included by using fully relativistic optimized norm-conserving Vanderbilt pseudopotentials [44] from the PSEUDODOJO [45] library. Self-consistent calculations [46] were performed on a $24 \times 24 \times 1 \mathbf{k}$ grid, resulting in DFT band gap of $1661.9 \mathrm{meV}$ for $\mathrm{MoS}_{2}$.

Quasiparticle energies were obtained within the $\mathrm{G}_{0} \mathrm{~W}_{0}$ [47] approximation using the BERKELEYGW package [8, 13, 15], starting from the DFT wave functions and eigenvalues computed with QUANTUM ESPRESSO.

We employed the spinor implementation of BERKE-
LEYGW [48], wherein spin-orbit coupling is included
non-perturbatively. The dielectric function was evalu-
ated using the generalized plasmon-pole model of Hy-
bertsen and Louie [47], with a $6 \times 6 \times 1$ $\mathbf{q}$ grid and 4000
occupied and unoccupied bands. Plane waves up to an
energy cutoff of 25 Ry were used in the computation of
dielectric function. The Brillouin-zone sampling was re-
fined near $\mathbf{q}=0$ using a nonuniform neck subsampling
(NNS) [49] scheme with a fine nonuniform sampling of 10
points. Coulomb truncation was applied along the out-of-
plane direction to eliminate interlayer interactions [50].
The resulting GW gap at the K point was 2553.9 meV
for $\text{MoS}_2$.

The Bethe-Salpeter equation (BSE) was solved
within the Tamm-Dancoff approximation using BERKE-
LEYGW [8, 13, 15, 48]. BSE calculations were performed
for finite-$\mathbf{Q}$ points along the path $\Gamma$-M-K-$\Gamma$ of the Bril-
louin zone. The electron-hole interaction kernel and ab-
sorption calculations were done on a $24 \times 24 \times 1$ $\mathbf{k}$ grid with
two valence and four conduction bands. The total prod-
uct basis size was therefore 4608. The dielectric matrix
was evaluated using plane waves up to the energy cut-
off of 5 Ry in the BSE kernel calculations. One-electron
wave functions at all the $\mathbf{k}$ points in the full Brillouin zone
were constructed by rotating the wave functions gener-
ated in the irreducible Brillouin zone to preserve phase
consistency at symmetry-related points.

## IV. RESULTS AND DISCUSSION

The formalism that we have developed in Sec. II is gen-
eral. We use monolayer $\text{MoS}_2$ as a prototypical example
to show the application of this formalism within an *ab ini-
tio* context. The nomenclature and labels used to repre-
sent the groups and their irreducible representations are
adopted from Ref. [51]. The crystal symmetry of mono-
layer $\text{MoS}_2$ is described by the point group $D_{3h}$. The
little group at the center of the Brillouin zone ($\mathbf{k}=\Gamma$),
$\mathcal{G}_{\Gamma}$, contains all the symmetry elements of the $D_{3h}$ group.
At other high-symmetry points in the Brillouin zone the
little groups contain fewer symmetry elements—for ex-
ample, at $\mathbf{k}=\text{M}$ the little group, $\mathcal{G}_{\text{M}}$, is $C_{2v}$, while at
$\mathbf{k}=\text{K}$, the little group, $\mathcal{G}_{\text{K}}$, is $C_{3h}$. In the absence of
spin-orbit coupling, the one-electron eigenstates are also
eigenstates of the spin angular momentum operator. As
a result, they can be labeled using the single-group irre-
ducible representations of the little groups listed above.
As our calculations include spin-orbit coupling, the one-
electron eigenstates are spinors as they are not eigen-
states of the spin angular momentum operator. Con-
sequently, the associated irreducible representations be-
long to the complex double groups, $D_{3h}^D$, $C_{2v}^D$, and $C_{3h}^D$
at the $\Gamma$, M, and K points in the Brillouin zone, respec-
tively. Figure 1(a) shows the quasiparticle band structure
obtained using the $G_0W_0$ approximation to the self en-
ergy. The bands are plotted along the high-symmetry
path $\Gamma-\text{M}-\text{K}-\Gamma$. We use the diagonal approximation
of $G_0W_0$ to calculate the quasiparticle energies. Within
this approximation, the quasiparticle wave functions are
assumed to be the same as the corresponding DFT wave
functions and the self-energy operator only corrects the
DFT eigenvalues to the corresponding quasiparticle en-
ergy. As a result, we use the DFT spinor wave functions
to calculate the irreducible representations of the corre-
sponding complex double groups at the high-symmetry
points. Figure 1(a) also shows the assignments of the ir-
reducible representations at the high-symmetry points to
the states that are closest to the band gap. For the first
two valence and four conduction states at the $\Gamma$ point,

![](./images/1166711848062418945_1.jpg)

FIG. 1: (a) GW electronic band structure of monolayer
$\text{MoS}_2$ along the high-symmetry path $\Gamma$-M-K-$\Gamma$ in the
Brillouin zone. The valence band maximum is set to
0 eV. The double-group spinor irreducible
representations associated with the bands are indicated
at the high-symmetry points. (b) Exciton band
structure of monolayer $\text{MoS}_2$ along the path $\Gamma$-M-K-$\Gamma$
in the Brillouin zone. The irreducible representations of
the excitonic bands are labeled at the high-symmetry
points $\Gamma$, M, and K. The irreducible representations at
the labeled points along the high symmetry lines are
tabulated in Table I. The evolution of the excitonic
states at the transition between symmetry lines and
high symmetry points illustrates the compatibility
relations.

the doubly degenerate states can be labeled by the irre- ducible representations $\Gamma_{7}$, $\Gamma_{7}$, and $\Gamma_{9}$ respectively. At the M point in the Brillouin zone, the labels are $M_{5}$ for each pair of doubly degenerate states. At the K point, the one-dimensional representations of the valence bands are $K_{12}$ and $K_{10}$, respectively, and the representations are $K_{7}$, $K_{8}$, $K_{11}$, and $K_{8}$ for the spin-orbit split, nonde- generate states in the conduction band manifold. These irreducible representations are the same as those calcu- lated from the IRREP package [7].

In contrast to quasiparticles, excitons are composite bosons. The excitonic states are written as a linear com- bination of basis states constructed from the tensor prod- uct of two fermionic states-electron and hole. In the ab- sence of spin-orbit coupling, the total spin angular mo- mentum of these basis states is given by the addition of the spin angular momenta of the constituent electron and hole states. This leads to the excitonic states being eigenstates of the total spin angular momentum opera- tor. They are characterized by the eigenvalues of the square of the total spin operator, $S^{2}$, ($2\hbar^{2}$ for triplets and $\hbar^{2}$ for singlets), and $S_{z}$, the spin projection opera- tor along the $z$ axis ($-1,0,1$ for triplets and 0 for sin- glets). In the presence of spin-orbit coupling, when the one-electron states are no longer eigenstates of the spin angular momentum operator, the resulting excitons are also no longer eigenstates of the total spin angular mo- mentum operator. Then, the excitonic eigenstates are linear combinations of singlet and triplet states. Never- theless, in both cases (in the presence or absence of spin orbit coupling), the symmetry classification of excitonic states is governed by the single-group irreducible repre- sentations of the little group at the center-of-mass mo- mentum $\mathbf{Q}$ of the exciton. Thus the relevant irreducible representations of the excitonic states are those of the single groups $D_{3h}$, $C_{2v}$, and $C_{3h}$ for $\mathbf{Q}=\Gamma$, $\mathbf{Q}=\mathrm{M}$ and $\mathbf{Q}=\mathrm{K}$, respectively.

We implemented the formalism for applying spatial and time-reversal symmetries to excitonic states, as de- scribed in Secs. IIC and IID. In order to test the implementation, as a first step, we calculated the exci- tonic states at a point $\mathbf{Q}$ in the irreducible Brillouin zone. Upon rotating these states by a space group symmetry operation, $\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\}$, we obtained the excitonic states at the point $\mathcal{R}_{\mathbf{t}}\mathbf{Q}$. We compared these states to the correspond- ing excitonic states directly calculated at the rotated mo- mentum $\mathcal{R}_{\mathbf{t}}\mathbf{Q}$. In an analogous manner, we compared the time-reversed exciton states at $\mathbf{Q}$ and $-\mathbf{Q}$. In both cases, we found exact agreement, up to an overall diagonaliza- tion phase, thereby confirming the correctness of our im- plementation of both space-group and time-reversal sym- metries.

Our implementation also allows for the direct compu- tation of irreducible representations of the invariant sub- spaces within the exciton manifold at a given $\mathbf{Q}$ and their characters from the excitonic states, using Eqs. 57 and 60 (Subsection IIF). Using this approach, we obtained the irreducible representations of excitonic bands along the high-symmetry path $\Gamma-\mathrm{M}-\mathrm{K}-\Gamma$ in the Brillouin zone, as shown in Fig. 1(b). Consider the case $\mathbf{Q}=0$: the $1s$- like A excitons $(\mathrm{A}_{1s})$ originate from the top valence band $(\mathrm{VB}_{1})$ and the two lowest conduction bands $(\mathrm{CB}_{1}$ and $\mathrm{CB}_{2})$, near the $\mathrm{K}/-\mathrm{K}$ valleys [52]. The complex double- group irreducible representations for $\mathrm{VB}_{1}$, $\mathrm{CB}_{1}$, and $\mathrm{CB}_{2}$ are $K_{10}$, $K_{7}$, and $K_{8}$ at the $\mathrm{K}$ valley (see Fig. 1), with conjugate irreducible representations $K_{9}$, $K_{8}$, and $K_{7}$ at the $-\mathrm{K}$ valley. The transitions between $\mathrm{CB}_{1}$ and $\mathrm{VB}_{1}$ at the $\mathrm{K}$ and $-\mathrm{K}$ valley yield direct product states with irreducible representations given as $\mathrm{K}_{7}^{*} \otimes \mathrm{K}_{10}=\mathrm{K}_{3}$ and $\mathrm{K}_{8}^{*}\otimes \mathrm{K}_{9}=\mathrm{K}_{2}$, respectively. If the exciton envelope func- tion of $1s$ excitonic states transforms as $\mathrm{K}_{1}$, the resulting irreducible excitonic states correspond to $\mathrm{K}_{3} \oplus \mathrm{K}_{2}$. The transitions involving $\mathrm{CB}_{2}$ and $\mathrm{VB}_{1}$ at the $\mathrm{K}$ and $-\mathrm{K}$ val- ley, we obtain the direct product states with irreducible representations as $\mathrm{K}_{8}^{*} \otimes \mathrm{K}_{10}=\mathrm{K}_{4}$ and $\mathrm{K}_{7}^{*} \otimes \mathrm{K}_{9}=\mathrm{K}_{4}$, respectively. As these transitions form the basis for exci- tons at the $\mathbf{Q}=\Gamma$ point in the excitonic band structure, we use the compatibility relation for $C_{3h} \to D_{3h}$. This compatibility relation maps these irreducible representa- tions at $\mathrm{K}$ to irreducible representations at $\mathbf{Q}=\Gamma$ as $\mathrm{K}_{3}\oplus \mathrm{K}_{2}\to \Gamma_{6}$ and $\mathrm{K}_{4}/\mathrm{K}_{4}\to \Gamma_{3}/\Gamma_{4}$. Hence the first four $\mathrm{A}_{1s}$ excitons transform as $\Gamma_{3}\oplus \Gamma_{4}\oplus \Gamma_{6}$. The classification obtained from our implementation is fully consistent with the physical and conceptual classification for $\mathrm{A}_{1s}$ excitons (see Fig. 1b and Table. I).

We next analyze the $1s$-like B excitons $(\mathrm{B}_{1s})$, which originate from the valence band $(\mathrm{VB}_{2})$ and the two low- est conduction bands $(\mathrm{CB}_{1}$ and $\mathrm{CB}_{2})$. The complex double-group irreducible representations for $\mathrm{VB}_{2}$ at the $\mathrm{K}$ and $-\mathrm{K}$ valley is $K_{10}$ and $K_{11}$, respectively. The ir- reducible representations of the direct product of states corresponding to the transitions between $\mathrm{CB}_{1}$ and $\mathrm{VB}_{2}$ at $\mathrm{K}$ and $-\mathrm{K}$ valley are $\mathrm{K}_{7}^{*}\otimes \mathrm{K}_{12}=\mathrm{K}_{5}$ and $\mathrm{K}_{8}^{*}\otimes \mathrm{K}_{11}=\mathrm{K}_{6}$, respectively. If the exciton envelope function of $1s$ trans- forms as $\mathrm{K}_{1}$, the corresponding direct product states are $\mathrm{K}_{5} \oplus \mathrm{K}_{6}$. For the transitions involving $\mathrm{CB}_{2}$ and $\mathrm{VB}_{2}$ at $\mathrm{K}$ and $-\mathrm{K}$ valley, we obtain $\mathrm{K}_{8}^{*} \otimes \mathrm{K}_{12}=\mathrm{K}_{3}$ and $\mathrm{K}_{7}^{*}\otimes \mathrm{K}_{11}=\mathrm{K}_{2}$, respectively, leading to the states belong- ing to $\mathrm{K}_{3} \oplus \mathrm{K}_{2}$. As discussed before, using the compati- bility relation for $C_{3h} \to D_{3h}$, this maps as $\mathrm{K}_{5}\oplus \mathrm{K}_{6}\to \Gamma_{5}$ and $\mathrm{K}_{3}\oplus \mathrm{K}_{2}\to \Gamma_{6}$. Therefore, the next four $\mathrm{B}_{1s}$ excitons at the $\mathbf{Q}=\Gamma$ transform as $\Gamma_{5} \oplus \Gamma_{6}$. The classification obtained from our symmetry formalism is fully consis- tent with the physical and conceptual classification for $\mathrm{B}_{1s}$ excitons, as well. (See Fig. 1b and Table. I).

Furthermore, we verified the validity of the irreducible representations at various finite center-of-mass momenta of excitons by explicitly tracking the compatibility rela- tions between transitions of different symmetry groups at the high-symmetry points and the connecting symmetry lines. For $\Sigma_{pt_{1}}$ on the symmetry line $\Sigma$, the symmetry elements that form the group are $\{E,C_{2},\sigma_{h},\sigma_{v}\}$, which is isomorphic to the $C_{2v}$ group with symmetry elements $\{E,C_{2},\sigma_{v},\sigma_{v}'\}$ and the same character table. This group has four one-dimensional irreducible representations, de- noted $\Sigma_{1},\Sigma_{2},\Sigma_{3},\Sigma_{4}$. The compatibility relations from

$D_{3 h} \to C_{2 v}$ are given by
$$
\Gamma_{3} \to \Sigma_{3}, \quad \Gamma_{4} \to \Sigma_{4}, \quad \Gamma_{6} \to \Sigma_{1} \oplus \Sigma_{2}, \quad \Gamma_{5} \to \Sigma_{3} \oplus \Sigma_{4},
$$
which is in exact agreement with the independent symmetry classification obtained from our implementation. Higher-lying states are expected to follow the order predicted by these compatibility relations. However, due to band crossings and the presence of nearly degenerate states, the ordering of irreducible representations can change. This highlights the advantage of an explicit symmetry classification of excitonic bands, as it allows one to consistently identify states belonging to the same irreducible representations and to track them reliably, especially in the case of fine $\mathbf{k}$-point sampling where significant exciton overlap occurs between nearby points. As one traverses the $\Sigma$ line toward $\Sigma_{p t_{2}}$, the ordering of the symmetry irreducible representations of the states changes. The irreducible representations obtained at $\Sigma_{p t_{2}}$ remain compatible with those at the M point, since the symmetry group is the same along the $\Sigma$ direction and $\mathbf{Q}=\mathrm{M}$. We then consider the T high-symmetry line from M to K. Along this path, from the M point to $\mathrm{T}_{p t_{1}}$, the group reduces as $C_{2 v} \to C_{s}=\left\{E, \sigma_{h}\right\}$. This group has two one-dimensional irreducible representations, with characters 1 and $-1$ under $\sigma_{h}$, labeled as $\mathrm{T}_{1}$ and $\mathrm{T}_{2}$. Since the characters of $\sigma_{h}$ for $\mathrm{M}_{3}$ and $\mathrm{M}_{4}$ are $-1$, while those for $\mathrm{M}_{1}$ and $\mathrm{M}_{2}$ are 1, the compatibility relations are
$$
\mathrm{M}_{3} / \mathrm{M}_{4} \to \mathrm{T}_{2}, \quad \mathrm{M}_{1} / \mathrm{M}_{2} \to \mathrm{T}_{1}.
$$

This relation holds for the first seven exciton states (see Table I), although the eighth and ninth states are accidentally degenerate in energy (i.e., not symmetry-protected). Consequently, the eighth exciton state at M is compatible with the ninth state at $\mathrm{T}_{p t_{1}}$.

Following these connectivities, the irreducible representations at $\mathrm{T}_{p t_{2}}$ are shown in Table. I. One observes that some states shift within the manifold to preserve compatibility relations at the transition from $\mathrm{T}_{p t_{2}}$ to $\mathrm{K}$, where the symmetry changes from $C_{2 v} \to C_{3 h}$. The little group at $\mathbf{Q}=\mathrm{K}$ is $C_{3 h}$, consisting of the symmetry elements $\left\{E, C_{3}, C_{3}^{-1}, \sigma_{h}, S_{3}, S_{3}^{-1}\right\}$. This group has six one-dimensional irreducible representations, labeled $\mathrm{K}_{1}$ through $\mathrm{K}_{6}$. The characters of $\sigma_{h}$ are $-1$ for $\mathrm{K}_{4}, \mathrm{~K}_{5}, \mathrm{~K}_{6}$, and $+1$ for $\mathrm{K}_{1}, \mathrm{~K}_{2}, \mathrm{~K}_{3}$. Thus, the compatibility relations between $\mathrm{T}_{p t_{2}}$ and $\mathrm{K}$ are
$$
\mathrm{K}_{4}, \mathrm{~K}_{5}, \mathrm{~K}_{6} \to \mathrm{T}_{2}, \quad \mathrm{~K}_{1}, \mathrm{~K}_{2}, \mathrm{~K}_{3} \to \mathrm{T}_{1}.
$$

This correspondence is observed in our computed classifications, with the exception of the eighth state at $\mathrm{K}$, which was found to be compatible with the ninth state at $\mathrm{T}_{p t_{2}}$, again because of similar reasons discussed before.

Along the $\Lambda$ line, one can similarly follow the compatibility relations from $C_{3 h} \to C_{s}$. From $\Lambda_{p t_{2}}$ to $\Gamma$, i.e., from $C_{s} \to D_{3 h}$, the characters of $\sigma_{h}$ are $-1,-1,2$ for $\Gamma_{3}, \Gamma_{4}, \Gamma_{6}$, respectively, and $1,1,-2$ for $\Gamma_{1}, \Gamma_{2}, \Gamma_{5}$, respectively. Therefore, the compatibility relations are
$$
\Gamma_{3}, \Gamma_{4} \to \Lambda_{2}, \quad \Gamma_{1}, \Gamma_{2} \to \Lambda_{1},
$$
$$
\Gamma_{5} \to \Lambda_{2} \oplus \Lambda_{2}, \quad \Gamma_{6} \to \Lambda_{1} \oplus \Lambda_{1}.
$$

![](./images/1166711848062418945_2.jpg)

FIG. 2: Panels (a) and (c) depict the full spinor BSE Hamiltonian constructed from two valence and four conduction bands on a $24 \times 24 \times 1$ $\mathbf{k}$-point grid, for exciton center-of-mass momenta $\mathbf{Q}=\Gamma$ and $\mathbf{Q}=\mathrm{K}$, respectively. Panels (b) and (d) show the corresponding block-diagonalized BSE Hamiltonians, resolved into blocks associated with the irreducible representations of the $D_{3 h}$ and $C_{3 h}$ symmetry groups at $\mathbf{Q}=\Gamma$ and $\mathbf{Q}=\mathrm{K}$, respectively. The dimensions of the blocks corresponding to each irreducible representation are indicated. The color bars represent the absolute values of the BSE Hamiltonian matrix elements for both the full and symmetry-adapted cases. For clarity, the diagonal matrix elements have been removed, and the color scale has been capped at a fixed maximum value to emphasize the block structure.

Our results are in excellent agreement with these predicted compatibility relations.

In addition to proposing and implementing a formalism for symmetry-based classification of excitonic states, we employed projection operators (see subsection II F) to construct the symmetry-adapted linear combinations of the electron-hole direct-product-state basis for every irreducible representation of the little group $\mathcal{G}_{\mathbf{Q}}$. This

procedure not only block diagonalizes the BSE Hamilto- nian at that $\mathbf{Q}$ point into smaller blocks corresponding to distinct irreducible representations, but also provides an independent route for characterizing the excitons. While this approach naturally highlights the role of symmetry, in the present work instead of directly constructing the BSE kernel in the symmetry-adapted basis from the out- set, we first compute the full kernel in the conventional electron–hole product basis and subsequently project it onto the symmetry-adapted basis. Consequently, the gain in computational efficiency in the current work arises mainly during the diagonalization step of the BSE Hamil- tonian, where the matrix becomes block diagonal in the symmetry-adapted basis. We depict this reduction ex- plicitly for $\mathbf{Q}=\Gamma$ and $\mathbf{Q}=\mathrm{K}$ in Fig. 2. For $\mathbf{Q}=\Gamma$, the little group has order $N_{\mathcal{G}_{\mathbf{Q}}}=12$, with $d_{\xi_{n}}=1$ for $\Gamma_{1}, \Gamma_{2}$, $\Gamma_{3}$, and $\Gamma_{4}$, and $d_{\xi_{n}}=2$ for $\Gamma_{5}$ and $\Gamma_{6}$. This results in approximately $384(=4608 / 12)$ and $1536(=4 \times 4608 / 12)$ symmetry-adapted basis states for the one-dimensional and two-dimensional irreducible representations, respec- tively. Similarly, for $\mathbf{Q}=\mathrm{K}$, we have $N_{\mathcal{G}_{\mathbf{Q}}}=6$ and $d_{\xi_{n}}=1$ for $\mathrm{K}_{1}-\mathrm{K}_{6}$, leading to 768 symmetry-adapted basis states. These numbers are in good agreement with the block sizes shown in Fig. 2, with a minor deviation attributed to the finite size of the basis. The exciton states obtained from diagonalization within each irre- ducible representation block coincide with those obtained through direct symmetry classification, confirming con- sistency between the two methods. The agreement of ex- citon irreducible representations with both the physical interpretation of compatibility relations and the block- diagonalization procedure establishes the robustness of our formalism.

Symmetries of excitons can also be used to examine optical selection rules. The optical selection rule for a transition from an excitonic state $S$ at momentum $\mathbf{Q}$ to another excitonic state $S'$ at momentum $\mathbf{Q}'$ via a phonon mode $\nu$ at momentum $\mathbf{q}$ , involves the irreducible repre- sentations of excitons $\xi_{S, \mathbf{Q}}, \xi_{S', \mathbf{Q}'}$ , and of the phonon $\xi_{\nu, \mathbf{q}}$, respectively [53]. It is given as

$$
\xi_{S, \mathbf{Q}} \otimes \xi_{\nu, \mathbf{q}} \supset \xi_{S', \mathbf{Q}'}.
$$

As an example, we show the selection rules for the optical transitions between exciton states of $\mathrm{MoS}_{2}$ at $\mathbf{Q}=\mathbf{Q}'=0$ via a $\Gamma$-point phonon $(\mathbf{q}=0)$. The se lection rule becomes $\xi_{S, \mathbf{0}} \otimes \xi_{\nu, \mathbf{0}} \supset \xi_{S', \mathbf{0}}$. For both $\mathbf{Q}=0$ and $\mathbf{q}=0$, the little group is $D_{3 h}$, identical to the crys tal symmetry group. This approach is similar to the ap- proach in Ref. [33], where selection rules were formulated to analyze resonant Raman scattering in $\mathrm{WSe}_{2} / \mathrm{hBN}$ het erostructures possessing $C_{3}$ symmetry at $\mathbf{q}=\mathbf{Q}=0$. For the $\mathrm{MoS}_{2}$ case, the Kronecker product table between the irreducible representations corresponding to the initial excitonic state and the phonon modes is shown in Ta- ble II. However, not all irreducible representations ap- pear at $\mathbf{q}=0$. The number of phonon modes for mono- layer $\mathrm{MoS}_{2}$ is 9 and these modes can be written as a direct sum of the irreducible representations as [54, 55]

$$
\Gamma_{1} \oplus 2 \Gamma_{4} \oplus 2 \Gamma_{6} \oplus \Gamma_{5},
$$

The phonon modes in the direct sum of irreducible rep- resentations are representated by a different notation in Ref. [55] as $A_{1}', A_{2}^{\prime \prime}, E'$, and $E^{\prime \prime}$, respectively. To define selection rules, as an example, we now consider the ir- reducible representations of the initial and final exciton states to be $\Gamma_{5}$ and $\Gamma_{6}$, respectively. These states cor respond to the transitions from the doubly degenerate lowest B excitation state to one of the doubly degenerate states in the A exciton. The following relations satisfy the selection rules:

$$
\begin{aligned}
& \Gamma_{5} \otimes \Gamma_{3}=\Gamma_{6} \\
& \Gamma_{5} \otimes \Gamma_{4}=\Gamma_{6} \\
& \Gamma_{5} \otimes \Gamma_{5}=\Gamma_{1} \oplus \Gamma_{2} \oplus \Gamma_{6} \supset \Gamma_{6}.
\end{aligned}
$$

As $\Gamma_{3}$ does not appear in the direct sum of phonon irre ducible representations, only the transitions via phonons with $\Gamma_{4}$ and $\Gamma_{5}$ are symmetry allowed, while transitions via $\Gamma_{1}$ and $\Gamma_{6}$ phonons are not symmetry allowed. Sim ilarly, if one takes the initial and final states to be $\Gamma_{5}$ and $\Gamma_{3}$ or $\Gamma_{4}$, respectively, corresponding to the tran sitions from the doubly degenerate lowest B excitation state to the other doubly degenerate state of the A ex- citon, the only symmetry allowed transition is via the $\Gamma_{6}$ phonon mode. This can be seen from the table as $\Gamma_{5} \otimes \Gamma_{6}=\Gamma_{3} \oplus \Gamma_{4} \oplus \Gamma_{5} \supset \Gamma_{3}$ and $\Gamma_{4}$. This analysis can be further extended to study the symmetry based selection rules for the initial and final excitonic states at arbitrary center-of-mass momenta.

## V. CONCLUSIONS

In summary, in this paper we have established a gen- eral symmetry-based framework for excitons, incorporat- ing both time-reversal and space-group operations. We showed how one can generate the excitonic states within the irreducible Brillouin zone and use space group sym- metry operations to obtain the states at other points in the full Brillouin zone. This method allows great reduc- tion in computational cost especially in problems where a fine sampling of the excitonic center-of-mass moemen- tum is needed. Furthermore, by explicitly calculating the irreducible representations of the little groups and classi- fying excitonic states accordingly, we demonstrated how symmetry governs their degeneracies and band connec- tivities. Moreover, using projection operators, we con- structed symmetry-adapted linear combinations of elec- tron–hole product states, which block diagonalize the BSE Hamiltonian and provide a transparent symmetry classification of excitonic states. The irreducible repre- sentations of the excitonic states obtained with both the procedures were found to be in agreement with those de- rived from compatibility relations, confirming the consis- tency of the formalism. This unified approach highlights

TABLE I: Irreducible representations of the first eight excitonic states at high-symmetry points and along high-symmetry lines in the Brillouin zone of monolayer MoS₂.

<table>
<thead>
<tr>
<th>Symmetry<br>line</th>
<th>Symmetry<br>points</th>
<th>Symmetry<br>group</th>
<th>Irreducible representations of the excitonic states</th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
<td>Γ</td>
<td>$D_{3h}$</td>
<td>$\Gamma_3 \oplus \Gamma_4 \oplus \Gamma_6 \oplus \Gamma_5 \oplus \Gamma_6$</td>
</tr>
<tr>
<td>Σ</td>
<td>$\Sigma_{pt_1}$</td>
<td>$C_{2v}$</td>
<td>$\Sigma_3 \oplus \Sigma_4 \oplus \Sigma_2 \oplus \Sigma_1 \oplus \Sigma_3 \oplus \Sigma_4 \oplus \Sigma_2 \oplus \Sigma_1$</td>
</tr>
<tr>
<td></td>
<td>$\Sigma_{pt_2}$</td>
<td>$C_{2v}$</td>
<td>$\Sigma_3 \oplus \Sigma_4 \oplus \Sigma_2 \oplus \Sigma_1 \oplus \Sigma_2 \oplus \Sigma_3 \oplus \Sigma_4 \oplus \Sigma_1$</td>
</tr>
<tr>
<td></td>
<td>M</td>
<td>$C_{2v}$</td>
<td>$\text{M}_3 \oplus \text{M}_4 \oplus \text{M}_2 \oplus \text{M}_1 \oplus \text{M}_2 \oplus \text{M}_3 \oplus \text{M}_4 \oplus \text{M}_1$</td>
</tr>
<tr>
<td>T</td>
<td>$\text{T}_{pt_1}$</td>
<td>$C_s$</td>
<td>$\text{T}_2 \oplus \text{T}_2 \oplus \text{T}_1 \oplus \text{T}_1 \oplus \text{T}_1 \oplus \text{T}_2 \oplus \text{T}_2 \oplus \text{T}_2$</td>
</tr>
<tr>
<td></td>
<td>$\text{T}_{pt_2}$</td>
<td>$C_s$</td>
<td>$\text{T}_2 \oplus \text{T}_1 \oplus \text{T}_2 \oplus \text{T}_1 \oplus \text{T}_2 \oplus \text{T}_2 \oplus \text{T}_1 \oplus \text{T}_1$</td>
</tr>
<tr>
<td></td>
<td>K</td>
<td>$C_{3h}$</td>
<td>$\text{K}_6 \oplus \text{K}_2 \oplus \text{K}_4 \oplus \text{K}_3 \oplus \text{K}_5 \oplus \text{K}_4 \oplus \text{K}_2 \oplus \text{K}_6$</td>
</tr>
<tr>
<td>Λ</td>
<td>$\Lambda_{pt_1}$</td>
<td>$C_s$</td>
<td>$\Lambda_2 \oplus \Lambda_1 \oplus \Lambda_2 \oplus \Lambda_1 \oplus \Lambda_2 \oplus \Lambda_2 \oplus \Lambda_1 \oplus \Lambda_1$</td>
</tr>
<tr>
<td></td>
<td>$\Lambda_{pt_2}$</td>
<td>$C_s$</td>
<td>$\Lambda_1 \oplus \Lambda_2 \oplus \Lambda_2 \oplus \Lambda_2 \oplus \Lambda_1 \oplus \Lambda_2 \oplus \Lambda_1 \oplus \Lambda_1$</td>
</tr>
<tr>
<td></td>
<td>$\Lambda_{pt_3}$</td>
<td>$C_s$</td>
<td>$\Lambda_1 \oplus \Lambda_2 \oplus \Lambda_2 \oplus \Lambda_1 \oplus \Lambda_2 \oplus \Lambda_2 \oplus \Lambda_1 \oplus \Lambda_1$</td>
</tr>
<tr>
<td></td>
<td>$\Lambda_{pt_4}$</td>
<td>$C_s$</td>
<td>$\Lambda_2 \oplus \Lambda_2 \oplus \Lambda_1 \oplus \Lambda_1 \oplus \Lambda_2 \oplus \Lambda_2 \oplus \Lambda_1 \oplus \Lambda_1$</td>
</tr>
<tr>
<td></td>
<td>Γ</td>
<td>$D_{3h}$</td>
<td>$\Gamma_3 \oplus \Gamma_4 \oplus \Gamma_6 \oplus \Gamma_5 \oplus \Gamma_6$</td>
</tr>
</tbody>
</table>

TABLE II: Kronecker product table between irreducible representations of $D_{3h}$

<table>
<thead>
<tr>
<th>$\xi_{s,\text{0}} \otimes \xi_{\nu,\text{0}}$</th>
<th>$\Gamma_1$</th>
<th>$\Gamma_2$</th>
<th>$\Gamma_3$</th>
<th>$\Gamma_4$</th>
<th>$\Gamma_5$</th>
<th>$\Gamma_6$</th>
</tr>
</thead>
<tbody>
<tr>
<td>$\Gamma_1$</td>
<td>$\Gamma_1$</td>
<td>$\Gamma_2$</td>
<td>$\Gamma_3$</td>
<td>$\Gamma_4$</td>
<td>$\Gamma_5$</td>
<td>$\Gamma_6$</td>
</tr>
<tr>
<td>$\Gamma_2$</td>
<td>$\Gamma_2$</td>
<td>$\Gamma_1$</td>
<td>$\Gamma_4$</td>
<td>$\Gamma_3$</td>
<td>$\Gamma_5$</td>
<td>$\Gamma_6$</td>
</tr>
<tr>
<td>$\Gamma_3$</td>
<td>$\Gamma_3$</td>
<td>$\Gamma_4$</td>
<td>$\Gamma_1$</td>
<td>$\Gamma_2$</td>
<td>$\Gamma_6$</td>
<td>$\Gamma_5$</td>
</tr>
<tr>
<td>$\Gamma_4$</td>
<td>$\Gamma_4$</td>
<td>$\Gamma_3$</td>
<td>$\Gamma_2$</td>
<td>$\Gamma_1$</td>
<td>$\Gamma_6$</td>
<td>$\Gamma_5$</td>
</tr>
<tr>
<td>$\Gamma_5$</td>
<td>$\Gamma_5$</td>
<td>$\Gamma_5$</td>
<td>$\Gamma_6$</td>
<td>$\Gamma_6$</td>
<td>$\Gamma_1 \oplus \Gamma_2 \oplus \Gamma_6$</td>
<td>$\Gamma_3 \oplus \Gamma_4 \oplus \Gamma_5$</td>
</tr>
<tr>
<td>$\Gamma_6$</td>
<td>$\Gamma_6$</td>
<td>$\Gamma_6$</td>
<td>$\Gamma_5$</td>
<td>$\Gamma_5$</td>
<td>$\Gamma_3 \oplus \Gamma_4 \oplus \Gamma_5$</td>
<td>$\Gamma_1 \oplus \Gamma_2 \oplus \Gamma_6$</td>
</tr>
</tbody>
</table>

the central role of symmetry in excitonic theory and provides a robust framework for analyzing optical selection rules and exciton band connectivities in a broad class of quantum materials.

## VI. DATA AVAILABILITY
The authors declare that the data supporting the findings of this study are availble within the main text and at [56]. Other relevant data are available from the corresponding author upon request.

## VII. ACKNOWLEDGEMENTS
We thank the Supercomputer Education and Research Centre (SERC) at the Indian Institute of Science (IISc) for providing the computational facilities. R.B. acknowledges the funding from the Prime Minister's Research Fellowship (PMRF), MHRD. M.J. and H.R.K. gratefully acknowledge the Nano mission of the Department of Science and Technology, India, and the Indian National Science Academy, India, for financial support under Grants No. DST/NM/TUE/QM-10/2019 and No. INSA/SP/SS/2023/, respectively.

## APPENDIX A: SYMMETRY TRANSFORMATION OF HAMILTONIAN
We consider $|n, \mathbf{k}\rangle$ as the $n^{\text{th}}$ electronic eigenstate at crystal momentum $\mathbf{k}$. Since $\hat{P}_{\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\}}$ commutes with $\hat{\mathcal{H}}$, we have
$$
\hat{P}_{\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\}} \hat{\mathcal{H}} |n, \mathbf{k}\rangle = \hat{\mathcal{H}} \hat{P}_{\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\}} |n, \mathbf{k}\rangle.
$$

The left-hand side becomes
$$
\hat{P}_{\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\}} \hat{\mathcal{H}} |n, \mathbf{k}\rangle = \hat{P}_{\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\}} \hat{\mathcal{H}}_{\mathbf{k}} |n, \mathbf{k}\rangle,
$$
while the right-hand side gives
$$
\begin{aligned}
\hat{\mathcal{H}} \hat{P}_{\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\}} |n, \mathbf{k}\rangle &= \hat{\mathcal{H}} |n, \mathcal{R}_{\mathbf{t}} \mathbf{k}\rangle = \hat{\mathcal{H}}_{\mathcal{R}_{\mathbf{t}} \mathbf{k}} |n, \mathcal{R}_{\mathbf{t}} \mathbf{k}\rangle \\
&= \hat{\mathcal{H}}_{\mathcal{R}_{\mathbf{t}} \mathbf{k}} \hat{P}_{\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\}} |n, \mathbf{k}\rangle.
\end{aligned}
$$

Therefore,
$$
\hat{P}_{\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\}} \hat{\mathcal{H}}_{\mathbf{k}} |n, \mathbf{k}\rangle = \hat{\mathcal{H}}_{\mathcal{R}_{\mathbf{t}} \mathbf{k}} \hat{P}_{\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\}} |n, \mathbf{k}\rangle,
$$
which leads to
$$
\hat{P}_{\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\}} \hat{\mathcal{H}}_{\mathbf{k}} \left( \hat{P}_{\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\}} \right)^{-1} = \hat{\mathcal{H}}_{\mathcal{R}_{\mathbf{t}} \mathbf{k}}.
$$

## APPENDIX B: TRANSLATIONAL SYMMETRY IN BETHE-SALPETER EQUATION (BSE) HAMILTONIAN
### A1. BSE Hamiltonian in real space
We begin with the Bethe-Salpeter equation (BSE) for the electron-hole amplitude $\Psi(\mathbf{r}_e, \mathbf{r}_h)$, where $\mathbf{r}_e$ and $\mathbf{r}_h$

are the electron and hole coordinates, respectively. In real space, the BSE Hamiltonian acts as a four-point kernel:

$$
\begin{aligned}
& \mathcal{H}_{\mathrm{BSE}}\left(\mathbf{r}_{e}, \mathbf{r}_{h} ; \mathbf{r}_{e}^{\prime}, \mathbf{r}_{h}^{\prime}\right)=\mathcal{H}_{e}\left(\mathbf{r}_{e}, \mathbf{r}_{e}^{\prime}\right) \delta\left(\mathbf{r}_{h}, \mathbf{r}_{h}^{\prime}\right) \\
& +\mathcal{H}_{h}\left(\mathbf{r}_{h}, \mathbf{r}_{h}^{\prime}\right) \delta\left(\mathbf{r}_{e}-\mathbf{r}_{e}^{\prime}\right)-W\left(\mathbf{r}_{e}, \mathbf{r}_{h}\right) \delta\left(\mathbf{r}_{e}-\mathbf{r}_{e}^{\prime}\right) \delta\left(\mathbf{r}_{h}-\mathbf{r}_{h}^{\prime}\right) \\
& +v\left(\mathbf{r}_{e}, \mathbf{r}_{h}^{\prime}\right) \delta\left(\mathbf{r}_{e}-\mathbf{r}_{h}\right) \delta\left(\mathbf{r}_{e}^{\prime}-\mathbf{r}_{h}^{\prime}\right)
\end{aligned}
\tag{66}
$$

where $\mathcal{H}_{e}(\mathbf{r}_{e}, \mathbf{r}_{e}')$ and $\mathcal{H}_{h}(\mathbf{r}_{h}, \mathbf{r}_{h}')$ are the electron quasiparticle and hole quasiparticle parts of the Hamiltonian. $W(\mathbf{r}_{e}, \mathbf{r}_{h})$ is the statically screened direct electron-hole interaction and $v(\mathbf{r}_{e}, \mathbf{r}_{h}')$ is the bare Coulomb exchange term.

### A2. Translational Invariance

In periodic crystals, the underlying crystal, ionic potentials, the Coulomb interactions, quasiparticle self-energy (in the GW approximation), and screening are invariant under translations by any Bravais lattice vector $\mathbf{R}$. Also, the one-particle lattice translation operator, $\hat{T}_{\mathbf{R}}^{e/h}$ commutes the one-particle Hamiltonians, $\mathcal{H}_{e/h}(\mathbf{r}, \mathbf{r}')$. These properties leads to the following

1.  The electron and hole quasiparticle Hamiltonians are invariant with respect to discrete lattice translations:
    $$
    \mathcal{H}_{e/h}(\mathbf{r}+\mathbf{R}, \mathbf{r}'+\mathbf{R})=\mathcal{H}_{e/h}(\mathbf{r}, \mathbf{r}')
    \tag{67}
    $$

2.  The interactions are invariant with respect to the discrete lattice translations as listed below:
    $$
    \begin{aligned}
    W(\mathbf{r}+\mathbf{R}, \mathbf{r}'+\mathbf{R}) &= W(\mathbf{r}, \mathbf{r}') \\
    v(\mathbf{r}+\mathbf{R}, \mathbf{r}'+\mathbf{R}) &= v(\mathbf{r}, \mathbf{r}')
    \end{aligned}
    \tag{68}
    $$

### A3. BSE Kernel invariance under simultaneous translations

We translate all four coordinates by the same Bravais vector $\mathbf{R}$ as follows:
$$
(\mathbf{r}_{e}, \mathbf{r}_{h}, \mathbf{r}_{e}', \mathbf{r}_{h}') \mapsto (\mathbf{r}_{e}+\mathbf{R}, \mathbf{r}_{h}+\mathbf{R}, \mathbf{r}_{e}'+\mathbf{R}, \mathbf{r}_{h}'+\mathbf{R})
$$

We examine each term in $H$:
$$
\begin{aligned}
& \mathcal{H}_{e}\left(\mathbf{r}_{e}+\mathbf{R}, \mathbf{r}_{e}^{\prime}+\mathbf{R}\right) \delta\left(\mathbf{r}_{h}+\mathbf{R}-\mathbf{r}_{h}^{\prime}-\mathbf{R}\right) \\
& =\mathcal{H}_{e}\left(\mathbf{r}_{e}, \mathbf{r}_{e}^{\prime}\right) \delta\left(\mathbf{r}_{h}-\mathbf{r}_{h}^{\prime}\right) \\
& \mathcal{H}_{h}\left(\mathbf{r}_{h}+\mathbf{R}, \mathbf{r}_{h}^{\prime}+\mathbf{R}\right) \delta\left(\mathbf{r}_{e}+\mathbf{R}-\mathbf{r}_{e}^{\prime}-\mathbf{R}\right) \\
& =\mathcal{H}_{h}\left(\mathbf{r}_{h}, \mathbf{r}_{h}^{\prime}\right) \delta\left(\mathbf{r}_{e}-\mathbf{r}_{e}^{\prime}\right), \\
& W\left(\mathbf{r}_{e}+\mathbf{R}, \mathbf{r}_{h}+\mathbf{R}\right) \delta\left(\mathbf{r}_{e}+\mathbf{R}-\mathbf{r}_{e}^{\prime}-\mathbf{R}\right) \\
& \times \delta\left(\mathbf{r}_{h}+\mathbf{R}-\mathbf{r}_{h}^{\prime}-\mathbf{R}\right) \\
& =W\left(\mathbf{r}_{e}, \mathbf{r}_{h}\right) \delta\left(\mathbf{r}_{e}-\mathbf{r}_{e}^{\prime}\right) \delta\left(\mathbf{r}_{h}-\mathbf{r}_{h}^{\prime}\right), \\
& v\left(\mathbf{r}_{e}+\mathbf{R}, \mathbf{r}_{h}^{\prime}+\mathbf{R}\right) \delta\left(\mathbf{r}_{e}+\mathbf{R}-\mathbf{r}_{h}+\mathbf{R}\right) \\
& \times \delta\left(\mathbf{r}_{e}^{\prime}+\mathbf{R}-\mathbf{r}_{h}^{\prime}+\mathbf{R}\right) \\
& =v\left(\mathbf{r}_{e}, \mathbf{r}_{h}^{\prime}\right) \delta\left(\mathbf{r}_{e}-\mathbf{r}_{h}\right) \delta\left(\mathbf{r}_{e}^{\prime}-\mathbf{r}_{h}^{\prime}\right).
\end{aligned}
\tag{69}
$$

Each term reproduces its unshifted form; therefore,
$$
\begin{aligned}
& \mathcal{H}_{\mathrm{BSE}}\left(\mathbf{r}_{e}+\mathbf{R}, \mathbf{r}_{h}+\mathbf{R} ; \mathbf{r}_{e}^{\prime}+\mathbf{R}, \mathbf{r}_{h}^{\prime}+\mathbf{R}\right) \\
& =\mathcal{H}_{\mathrm{BSE}}\left(\mathbf{r}_{e}, \mathbf{r}_{h} ; \mathbf{r}_{e}^{\prime}, \mathbf{r}_{h}^{\prime}\right)
\end{aligned}
\tag{70}
$$

This shows that the BSE Hamiltonian is invariant under simultaneous translations of all coordinates by any Bravais vector $\mathbf{R}$.

### A4. Translation operator commutes with the Hamiltonian

We define the two-particle translation operator $\hat{T}_{\mathbf{R}}^{ex}$ acting on a two-particle function, $\Psi(\mathbf{r}_{1}, \mathbf{r}_{2})$, as
$$
\left[\hat{T}_{\mathbf{R}}^{e x} \Psi\right]\left(\mathbf{r}_{1}, \mathbf{r}_{2}\right)=\Psi\left(\mathbf{r}_{1}-\mathbf{R}, \mathbf{r}_{2}-\mathbf{R}\right)
\tag{71}
$$

Applying the BSE Hamiltonian to the translated amplitude gives
$$
\begin{aligned}
& {\left[\hat{\mathcal{H}}_{\mathrm{BSE}} \hat{T}_{\mathbf{R}}^{e x} \Psi\right]\left(\mathbf{r}_{1}, \mathbf{r}_{2}\right)} \\
& =\iint d \mathbf{r}_{1}^{\prime} d \mathbf{r}_{2}^{\prime} \mathcal{H}_{\mathrm{BSE}}\left(\mathbf{r}_{1}, \mathbf{r}_{2} ; \mathbf{r}_{1}^{\prime}, \mathbf{r}_{2}^{\prime}\right) \Psi\left(\mathbf{r}_{1}^{\prime}-\mathbf{R}, \mathbf{r}_{2}^{\prime}-\mathbf{R}\right). \\
& =\iint d \mathbf{r}_{1}^{\prime} d \mathbf{r}_{2}^{\prime} \mathcal{H}_{\mathrm{BSE}}\left(\mathbf{r}_{1}-\mathbf{R}, \mathbf{r}_{2}-\mathbf{R} ; \mathbf{r}_{1}^{\prime}-\mathbf{R}, \mathbf{r}_{2}^{\prime}-\mathbf{R}\right) \\
& \times \Psi\left(\mathbf{r}_{1}^{\prime}-\mathbf{R}, \mathbf{r}_{2}^{\prime}-\mathbf{R}\right)
\end{aligned}
\tag{72}
$$

In the last equation, we have used the translational invariance of the Hamiltonian. Changing integration variables to $\mathbf{r}_{1}''=\mathbf{r}_{1}'-\mathbf{R}, \mathbf{r}_{2}''=\mathbf{r}_{2}'-\mathbf{R}$, one finds:
$$
\begin{aligned}
& {\left[\hat{\mathcal{H}}_{\mathrm{BSE}} \hat{T}_{\mathbf{R}}^{e x} \Psi\right]\left(\mathbf{r}_{1}, \mathbf{r}_{2}\right)} \\
& =\iint d \mathbf{r}_{1}^{\prime \prime} d \mathbf{r}_{2}^{\prime \prime} \mathcal{H}_{\mathrm{BSE}}\left(\mathbf{r}_{1}-\mathbf{R}, \mathbf{r}_{2}-\mathbf{R} ; \mathbf{r}_{1}^{\prime \prime}, \mathbf{r}_{2}^{\prime \prime}\right) \Psi\left(\mathbf{r}_{1}^{\prime \prime}, \mathbf{r}_{2}^{\prime \prime}\right) \\
& =\iint d \mathbf{r}_{1}^{\prime \prime} d \mathbf{r}_{2}^{\prime \prime}\left[\hat{T}_{\mathbf{R}} \mathcal{H}_{\mathrm{BSE}}\left(\mathbf{r}_{1}, \mathbf{r}_{2} ; \mathbf{r}_{1}^{\prime \prime}, \mathbf{r}_{2}^{\prime \prime}\right)\right] \Psi\left(\mathbf{r}_{1}^{\prime \prime}, \mathbf{r}_{2}^{\prime \prime}\right) \\
& =\left[\hat{T}_{\mathbf{R}}^{e x} \hat{\mathcal{H}}_{\mathrm{BSE}} \Psi\right]\left(\mathbf{r}_{1}, \mathbf{r}_{2}\right)
\end{aligned}
\tag{73}
$$

This leads to
$$
\hat{\mathcal{H}}_{\mathrm{BSE}} \hat{T}_{\mathbf{R}}^{e x}=\hat{T}_{\mathbf{R}}^{e x} \hat{\mathcal{H}}_{\mathrm{BSE}}.
\tag{74}
$$

Therefore, $\hat{\mathcal{H}}_{\mathrm{BSE}}$ commutes with the two-particle translation operator.

### A5. Bloch's Theorem for the Electron-Hole Amplitude

Since $\hat{\mathcal{H}}_{\mathrm{BSE}}$ commutes with $\hat{T}_{\mathbf{R}}^{ex}$, the electron-hole amplitudes are eigenfunctions of both $\hat{T}_{\mathbf{R}}^{ex}$ and $\mathcal{H}_{\mathrm{BSE}}$. Specifically,
$$
\hat{T}_{\mathbf{R}}^{e x} \Psi_{S, \mathbf{Q}}\left(\mathbf{r}_{e}, \mathbf{r}_{h}\right)=e^{i \mathbf{Q} \cdot \mathbf{R}} \Psi_{S, \mathbf{Q}}\left(\mathbf{r}_{e}, \mathbf{r}_{h}\right)
\tag{75}
$$

where $\mathbf{Q}$ is the total momentum of the two-particle exci-
tation state and $S$ is the state index. Thus translational
invariance ensures that two-particle excitains can be la-
beled by a well-defined crystal momentum $\mathbf{Q}$.

Now, we demonstrate the Bloch periodicity in the
product state basis used in the main text. We begin from
the electron-hole amplitude expansion of $\Psi_{S,\mathbf{Q}}(\mathbf{r}_{e},\mathbf{r}_{h})$
[Eq. 29] by simultaneously translating the electron and
hole coordinates by $\mathbf{R}$, i.e., $\mathbf{r}_{e}\mapsto\mathbf{r}_{e}+\mathbf{R}$ and $\mathbf{r}_{h}\mapsto\mathbf{r}_{h}+\mathbf{R}$
which leaves the relative coordinate $\mathbf{r}$ unchanged and
shifts the center-of-mass coordinate as $\mathbf{R}_{\mathrm{cm}}\mapsto\mathbf{R}_{\mathrm{cm}}+\mathbf{R}$.
Using the single-particle Bloch theorem and evaluating
amplitude at the translated arguments gives:

$$
\begin{aligned}
& \Psi_{S,\mathbf{Q}}(\mathbf{r}_{e}+\mathbf{R},\mathbf{r}_{h}+\mathbf{R}) \\
& =\sum_{v,c,\mathbf{k}}A_{v,c,\mathbf{k}}^{S,\mathbf{Q}}\Phi_{c,\mathbf{k}}(\mathbf{r}_{e}+\mathbf{R})\Phi_{v,\mathbf{k}-\mathbf{Q}}^{*}(\mathbf{r}_{h}+\mathbf{R}) \\
& =\sum_{v,c,\mathbf{k}}A_{v,c,\mathbf{k}}^{S,\mathbf{Q}}e^{i\mathbf{k}\cdot\mathbf{R}}\Phi_{c,\mathbf{k}}(\mathbf{r}_{e})\left(e^{i(\mathbf{k}-\mathbf{Q})\cdot\mathbf{R}}\Phi_{v,\mathbf{k}-\mathbf{Q}}(\mathbf{r}_{h})\right)^{*} \\
& =e^{i\mathbf{Q}\cdot\mathbf{R}}\sum_{v,c,\mathbf{k}}A_{v,c,\mathbf{k}}^{S,\mathbf{Q}}\Phi_{c,\mathbf{k}}(\mathbf{r}_{e})\Phi_{v,\mathbf{k}-\mathbf{Q}}^{*}(\mathbf{r}_{h}) \\
& =e^{i\mathbf{Q}\cdot\mathbf{R}}\Psi_{S,\mathbf{Q}}(\mathbf{r}_{e},\mathbf{r}_{h})
\end{aligned}
\tag{76}
$$

In center-of-mass and relative coordinates this reads
$$
\Psi_{S,\mathbf{Q}}(\mathbf{R}_{\mathrm{cm}}+\mathbf{R},\mathbf{r})=e^{i\mathbf{Q}\cdot\mathbf{R}}\Psi_{S,\mathbf{Q}}(\mathbf{R}_{\mathrm{cm}},\mathbf{r}) \tag{77}
$$

We define
$$
\mathbf{R}_{\mathrm{cm}}=\alpha\mathbf{r}_{e}+\beta\mathbf{r}_{h},\quad\mathbf{r}=\mathbf{r}_{e}-\mathbf{r}_{h},\quad\alpha+\beta=1
$$
so that $\mathbf{r}_{e}=\mathbf{R}_{\mathrm{cm}}+\beta\mathbf{r}$, $\mathbf{r}_{h}=\mathbf{R}_{\mathrm{cm}}-\alpha\mathbf{r}$, $\mathbf{k}_{h}=\mathbf{k}-\beta\mathbf{Q}$
and $\mathbf{k}_{e}=\mathbf{k}+\alpha\mathbf{Q}$

$$
\begin{aligned}
& \Psi_{S,\mathbf{Q}}(\mathbf{R}_{\mathrm{cm}},\mathbf{r})=e^{i\mathbf{Q}\cdot\mathbf{R}_{\mathrm{cm}}}\sum_{v,c,\mathbf{k}}A_{v,c,\mathbf{k}+\alpha\mathbf{Q}}^{S,\mathbf{Q}}e^{i\mathbf{k}\cdot\mathbf{r}} \\
& \quad\times u_{c,\mathbf{k}+\alpha\mathbf{Q}}(\mathbf{R}_{\mathrm{cm}}+\beta\mathbf{r})u_{v,\mathbf{k}-\beta\mathbf{Q}}^{*}(\mathbf{R}_{\mathrm{cm}}-\alpha\mathbf{r})
\end{aligned}
\tag{78}
$$

Including normalization factors, the Bloch periodic form
of the electron-hole amplitude can then be written as
$$
\Psi_{S,\mathbf{Q}}(\mathbf{R}_{\mathrm{cm}},\mathbf{r})=\frac{1}{\sqrt{N_{Q}}}e^{i\mathbf{Q}\cdot\mathbf{R}_{\mathrm{cm}}}F_{S,\mathbf{Q}}(\mathbf{R}_{\mathrm{cm}},\mathbf{r}) \tag{79}
$$
with the cell-periodic part
$$
\begin{aligned}
& F_{S,\mathbf{Q}}(\mathbf{R}_{\mathrm{cm}},\mathbf{r})=\frac{1}{\sqrt{N_{k}}}\sum_{v,c,\mathbf{k}}A_{v,c,\mathbf{k}+\alpha\mathbf{Q}}^{S,\mathbf{Q}}e^{i\mathbf{k}\cdot\mathbf{r}} \\
& \quad\times u_{c,\mathbf{k}+\alpha\mathbf{Q}}(\mathbf{R}_{\mathrm{cm}}+\beta\mathbf{r})u_{v,\mathbf{k}-\beta\mathbf{Q}}^{*}(\mathbf{R}_{\mathrm{cm}}-\alpha\mathbf{r})
\end{aligned}
\tag{80}
$$

Here, the cell-periodic part of two-particle excitation
is lattice periodic in the center-of-mass coordinate:
$$
F_{S,\mathbf{Q}}(\mathbf{R}_{\mathrm{cm}}+\mathbf{R},\mathbf{r})=F_{S,\mathbf{Q}}(\mathbf{R}_{\mathrm{cm}},\mathbf{r}). \tag{81}
$$

For the symmetric case $\alpha=\beta=\frac{1}{2}$, the conduction
and valence states carry momenta $\mathbf{k}+\frac{1}{2}\mathbf{Q}$ and $\mathbf{k}-\frac{1}{2}\mathbf{Q}$,
respectively. For the calculation within BERKELEYGW,
the form used in Eq. 29 is used, which is $\alpha=0$ and $\beta=1$.
The Bloch-periodic form expressed in these coordinates
was previously discussed in Ref. [57] and is included here
for completeness.

## APPENDIX C: TRANSFORMATION OF EXCITONS UNDER TIME-REVERSAL SYMMETRY

Let $\Theta$ denote the time-reversal operator acting on the
exciton amplitude $\Psi_{S,\mathbf{Q}}(\mathbf{r}_{e},\mathbf{r}_{h})$. Its action is defined as
$$
\left(\hat{P}_{\Theta}^{ex}\Psi_{S,\mathbf{Q}}\right)(\mathbf{r}_{e},\mathbf{r}_{h})=\Psi_{S,\mathbf{Q}}^{*}(\mathbf{r}_{e},\mathbf{r}_{h}) \tag{82}
$$
where the complex conjugation acts on the coefficients
and the single-particle spinor parts of the electron and
hole wave functions. Since time-reversal reverses all crys-
tal momenta, we have, at the single-particle operator
level,
$$
\hat{P}_{\Theta}^{ex}b_{n,\mathbf{k},s}^{\dagger}\hat{P}_{\Theta}^{ex-1}=\sum_{s'}(i\sigma_{y})_{ss'}b_{n,-\mathbf{k},s'}^{\dagger} \tag{83}
$$
and similarly for the hole creation operators; the same
transformation is inherited by the exciton amplitude co-
efficients in the Bloch basis.

Using the translation property defined in Eqs. 71 and
acting with $\hat{P}_{\Theta}^{ex}$ on the translated wave function gives:
$$
\begin{aligned}
& \left[\hat{P}_{\Theta}^{ex}\hat{T}_{\mathbf{R}}^{ex}\Psi_{S,\mathbf{Q}}\right](\mathbf{r}_{e},\mathbf{r}_{h}) \\
& =\hat{P}_{\Theta}^{ex}\left(\Psi_{S,\mathbf{Q}}(\mathbf{r}_{e}-\mathbf{R},\mathbf{r}_{h}-\mathbf{R})\right) \\
& =\Psi_{S,\mathbf{Q}}^{*}(\mathbf{r}_{e}-\mathbf{R},\mathbf{r}_{h}-\mathbf{R})
\end{aligned}
\tag{84}
$$

Because $\hat{P}_{\Theta}^{ex}$ is antiunitary it complex-conjugates the
phase factor, so applying it to the translation property
defined in Eq. 75 yields
$$
\begin{aligned}
\left[\hat{P}_{\Theta}^{ex}\hat{T}_{\mathbf{R}}^{ex}\Psi_{S,\mathbf{Q}}\right](\mathbf{r}_{e},\mathbf{r}_{h}) & =\left[\hat{P}_{\Theta}^{ex}\left(e^{i\mathbf{Q}\cdot\mathbf{R}}\Psi_{S,\mathbf{Q}}\right)\right](\mathbf{r}_{e},\mathbf{r}_{h}) \\
& =e^{-i\mathbf{Q}\cdot\mathbf{R}}\left[\hat{P}_{\Theta}^{ex}\Psi_{S,\mathbf{Q}}\right](\mathbf{r}_{e},\mathbf{r}_{h})
\end{aligned}
\tag{85}
$$

We compare this with the defining translation property
similar to Eq. 75 for the amplitudes at $-\mathbf{Q}$:
$$
\hat{T}_{\mathbf{R}}^{ex}\Psi_{S,-\mathbf{Q}}(\mathbf{r}_{e},\mathbf{r}_{h})=e^{-i\mathbf{Q}\cdot\mathbf{R}}\Psi_{S,-\mathbf{Q}}(\mathbf{r}_{e},\mathbf{r}_{h}) \tag{86}
$$

We therefore conclude that the time reversed exciton
amplitude $\left[\hat{P}_{\Theta}^{ex}\Psi_{S,\mathbf{Q}}\right](\mathbf{r}_{e},\mathbf{r}_{h})$ belongs to the momentum
block $-\mathbf{Q}$ and using the fact that the time-reversal com-
mutes with the BSE Hamiltonian, we get
$$
\hat{P}_{\Theta}^{ex}\mathcal{H}_{\mathbf{Q}}\hat{P}_{\Theta}^{ex-1}=\mathcal{H}_{-\mathbf{Q}} \tag{87}
$$

If $\mathcal{H}_{\mathbf{Q}}\Psi_{S,\mathbf{Q}}(\mathbf{r}_{e},\mathbf{r}_{h})=\Omega_{S,\mathbf{Q}}\Psi_{S,\mathbf{Q}}(\mathbf{r}_{e},\mathbf{r}_{h})$, then applying
$\hat{P}_{\Theta}^{ex}$ yields
$$
\begin{aligned}
\mathcal{H}_{-\mathbf{Q}}\left[\hat{P}_{\Theta}^{ex}\Psi_{S,\mathbf{Q}}\right](\mathbf{r}_{e},\mathbf{r}_{h}) & =\left[\hat{P}_{\Theta}^{ex}\mathcal{H}_{\mathbf{Q}}\Psi_{S,\mathbf{Q}}\right](\mathbf{r}_{e},\mathbf{r}_{h}) \\
& =\Omega_{S,\mathbf{Q}}\left[\hat{P}_{\Theta}^{ex}\Psi_{S,\mathbf{Q}}\right](\mathbf{r}_{e},\mathbf{r}_{h})
\end{aligned}
\tag{88}
$$

Thus the time-reversed amplitude is an eigenfunction in
the $-\mathbf{Q}$ block with the same eigenvalue:
$$
\Omega_{S, \mathbf{Q}}=\Omega_{S,-\mathbf{Q}}, \quad\left[\hat{P}_{\Theta}^{e x} \Psi_{S, \mathbf{Q}}\right]\left(\mathbf{r}_{e}, \mathbf{r}_{h}\right)=\Psi_{S,-\mathbf{Q}}\left(\mathbf{r}_{e}, \mathbf{r}_{h}\right)
\tag{89}
$$

Equivalently, in Dirac notation,
$$
\hat{P}_{\Theta}^{e x}|S, \mathbf{Q}\rangle=|S,-\mathbf{Q}\rangle,
\tag{90}
$$
which proves Eq. (35).

## APPENDIX D: TRANSFORMATION OF EXCITONS UNDER SPACE GROUP SYMMETRIES

We consider a space group operation $\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\}$. Its action on the exciton amplitude is defined by
$$
\left(\hat{P}_{\left\{\mathcal{R}_{\mathbf{t}} | \mathbf{t}\right\}}^{e x} \Psi_{S, \mathbf{Q}}\right)\left(\mathbf{r}_{e}, \mathbf{r}_{h}\right)=\Psi\left(\mathcal{R}_{\mathbf{t}}^{-1}\left(\mathbf{r}_{e}-\mathbf{t}\right), \mathcal{R}_{\mathbf{t}}^{-1}\left(\mathbf{r}_{h}-\mathbf{t}\right)\right)
\tag{91}
$$

First, we show that $\hat{P}_{\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\}}^{ex}|S,\mathbf{Q}\rangle$ belongs to the momentum block $\mathcal{R}_{\mathbf{t}}\mathbf{Q}$. We define the combined action of translations as defined in Eq. 71 along with space group operations as
$$
\begin{aligned}
& \hat{P}_{\left\{\mathcal{R}_{\mathbf{t}} | \mathbf{t}\right\}}^{e x} \hat{T}_{\mathbf{R}}^{e x}\left(\hat{P}_{\left\{\mathcal{R}_{\mathbf{t}} | \mathbf{t}\right\}}^{e x}\right)^{-1} \Psi_{S, \mathbf{Q}}\left(\mathbf{r}_{e}, \mathbf{r}_{h}\right) \\
& =\hat{T}_{\mathbf{R}}^{e x}\left(\hat{P}_{\left\{\mathcal{R}_{\mathbf{t}} | \mathbf{t}\right\}}^{e x}\right)^{-1} \Psi_{S, \mathbf{Q}}\left(\mathcal{R}_{\mathbf{t}}{ }^{-1}\left(\mathbf{r}_{e}-\mathbf{t}\right), \mathcal{R}_{\mathbf{t}}{ }^{-1}\left(\mathbf{r}_{h}-\mathbf{t}\right)\right) \\
& =\Psi_{S, \mathbf{Q}}\left(\mathcal{R}_{\mathbf{t}}\left(\mathcal{R}_{\mathbf{t}}{ }^{-1}\left(\mathbf{r}_{e}-\mathbf{t}\right)-\mathbf{R}\right)+\mathbf{t},\right. \\
& \mathcal{R}_{\mathbf{t}}\left(\mathcal{R}_{\mathbf{t}}{ }^{-1}\left(\mathbf{r}_{h}-\mathbf{t}\right)-\mathbf{R}\right)+\mathbf{t}) \\
& =\Psi_{S, \mathbf{Q}}\left(\mathbf{r}_{e}-\mathcal{R}_{\mathbf{t}} \mathbf{R}, \mathbf{r}_{h}-\mathcal{R}_{\mathbf{t}} \mathbf{R}\right) \\
& =\left(\hat{T}_{\mathcal{R}_{\mathbf{t}} \mathbf{R}}^{e x} \Psi_{S, \mathbf{Q}}\right)\left(\mathbf{r}_{e}, \mathbf{r}_{h}\right)
\tag{92}
\end{aligned}
$$

This gives the identity
$$
\hat{P}_{\left\{\mathcal{R}_{\mathbf{t}} | \mathbf{t}\right\}}^{e x} \hat{T}_{\mathbf{R}}^{e x}\left(\hat{P}_{\left\{\mathcal{R}_{\mathbf{t}} | \mathbf{t}\right\}}^{e x}\right)^{-1}=\hat{T}_{\mathcal{R}_{\mathbf{t}} \mathbf{R}}^{e x}
\tag{93}
$$

Now, using the translation property defined in Eq. 75, we evaluate
$$
\begin{aligned}
& \left(\hat{T}_{\mathbf{R}}^{e x} \hat{P}_{\left\{\mathcal{R}_{\mathbf{t}} | \mathbf{t}\right\}}^{e x} \Psi_{S, \mathbf{Q}}\right)\left(\mathbf{r}_{e}, \mathbf{r}_{h}\right) \\
& =\left(\hat{P}_{\left\{\mathcal{R}_{\mathbf{t}} | \mathbf{t}\right\}}^{e x} \hat{T}_{\mathcal{R}_{\mathbf{t}}{ }^{-1} \mathbf{R}}^{e x} \Psi_{S, \mathbf{Q}}\right)\left(\mathbf{r}_{e}, \mathbf{r}_{h}\right) \\
& =e^{i \mathbf{Q} \cdot \mathcal{R}_{\mathbf{t}}{ }^{-1} \mathbf{R}}\left(\hat{P}_{\left\{\mathcal{R}_{\mathbf{t}} | \mathbf{t}\right\}}^{e x} \Psi_{S, \mathbf{Q}}\right)\left(\mathbf{r}_{e}, \mathbf{r}_{h}\right) \\
& =e^{i\left(\mathcal{R}_{\mathbf{t}} \mathbf{Q}\right) \cdot \mathbf{R}}\left(\hat{P}_{\left\{\mathcal{R}_{\mathbf{t}} | \mathbf{t}\right\}}^{e x} \Psi_{S, \mathbf{Q}}\right)\left(\mathbf{r}_{e}, \mathbf{r}_{h}\right)
\tag{94}
\end{aligned}
$$
which implies that $\hat{P}_{\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\}}^{ex}|S,\mathbf{Q}\rangle$ lies in the momentum block labeled by $\mathcal{R}_{\mathbf{t}}\mathbf{Q}$. Also, the BSE Hamiltonian commutes with the symmetry operation. Therefore,
$$
\mathcal{H}_{\mathcal{R}_{\mathbf{t}} \mathbf{Q}} \hat{P}_{\left\{\mathcal{R}_{\mathbf{t}} | \mathbf{t}\right\}}^{e x}=\hat{P}_{\left\{\mathcal{R}_{\mathbf{t}} | \mathbf{t}\right\}}^{e x} \mathcal{H}_{\mathbf{Q}}
\tag{95}
$$

If $\mathcal{H}_{\mathbf{Q}}|S,\mathbf{Q}\rangle=\Omega_{S,\mathbf{Q}}|S,\mathbf{Q}\rangle$, then
$$
\begin{aligned}
& {\left[\hat{P}_{\left\{\mathcal{R}_{\mathbf{t}} | \mathbf{t}\right\}}^{e x} \mathcal{H}_{\mathbf{Q}}\right]|S, \mathbf{Q}\rangle=\Omega_{S, \mathbf{Q}}\left[\hat{P}_{\left\{\mathcal{R}_{\mathbf{t}} | \mathbf{t}\right\}}^{e x}|S, \mathbf{Q}\rangle\right]} \\
& \mathcal{H}_{\mathcal{R}_{\mathbf{t}} \mathbf{Q}}\left[\hat{P}_{\left\{\mathcal{R}_{\mathbf{t}} | \mathbf{t}\right\}}^{e x}|S, \mathbf{Q}\rangle\right]=\Omega_{S, \mathbf{Q}}\left[\hat{P}_{\left\{\mathcal{R}_{\mathbf{t}} | \mathbf{t}\right\}}^{e x}|S, \mathbf{Q}\rangle\right]
\end{aligned}
\tag{96}
$$

Hence the rotated state $\hat{P}_{\{\mathcal{R}_{\mathbf{t}}|\mathbf{t}\}}^{ex}|S,\mathbf{Q}\rangle$ is an eigenstate of $\mathcal{R}_{\mathbf{t}}\mathbf{Q}$ momentum block of the Hamiltonian with the same eigenvalue. So, the following holds:
$$
\Omega_{S, \mathcal{R}_{\mathbf{t}} \mathbf{Q}}=\Omega_{S, \mathbf{Q}}, \quad\left|S, \mathcal{R}_{\mathbf{t}} \mathbf{Q}\right\rangle=\hat{P}_{\left\{\mathcal{R}_{\mathbf{t}} | \mathbf{t}\right\}}^{e x}|S, \mathbf{Q}\rangle
\tag{97}
$$

[1] E. Wigner, Gruppentheorie und ihre Anwendung auf die Quantenmechanik der Atomspektren (Vieweg+Teubner Verlag Wiesbaden, 1931).

[2] M. S. Dresselhaus, G. Dresselhaus, and A. Jorio, Group Theory: Application to the Physics of Condensed Matter (Springer, 2008).

[3] M. Tinkham, Group Theory and Quantum Mechanics (Dover Publications, 2003).

[4] G. F. Bassani and G. P. Parravicini, Electronic States and Optical Transitions in Solids, International Series of Monographs in the Science of the Solid State, Vol. 8 (Pergamon Press, 1975).

[5] M. I. Aroyo, J. M. Perez-Mato, D. Orobengoa, E. Tasci, G. de la Flor, and A. Kirov, Crystallography online: Bilbao crystallographic server, Bulgarian Chemical Communications 43, 183 (2011).

[6] K. Shinohara, A. Togo, and I. Tanaka, spgrep: On-the-fly generator of space-group irreducible representations, Journal of Open Source Software 8, 5269 (2023).

[7] M. Iraola, J. L. Mañes, B. Bradlyn, M. K. Horton, T. Neupert, M. G. Vergniory, and S. S. Tsirkin, Irrep: Symmetry eigenvalues and irreducible representations of ab initio band structures, Computer Communications 272, 108226 (2022).

[8] J. Deslippe, G. Samsonidze, D. A. Strubbe, M. Jain, M. L. Cohen, and S. G. Louie, BerkeleyGW: A massively parallel computer package for the calculation of the quasiparticle and optical properties of materials and nanostructures, Computer Physics Communications 183, 1269 (2012).

[9] A. Marini, C. Hogan, M. Grüning, and D. Varsano, yambo: An ab initio tool for excited state calculations, Computer Physics Communications 180, 1392 (2009).

[10] Y. Li, A. Chernikov, X. Zhang, A. Rigosi, H. M. Hill, A. M. van der Zande, D. A. Chenet, E.-M. Shih, J. Hone, and T. F. Heinz, Measurement of the optical dielectric

function of monolayer transition-metal dichalcogenides:
$MoS_2$, $MoSe_2$, $WS_2$, and $WSe_2$, Phys. Rev. B 90, 205422
(2014).

[11] A. Chernikov, T. C. Berkelbach, H. M. Hill, A. Rigosi,
Y. Li, B. Aslan, D. R. Reichman, M. S. Hybertsen, and
T. F. Heinz, Exciton Binding Energy and Nonhydrogenic
Rydberg Series in Monolayer $WS_2$, Phys. Rev. Lett. 113,
076802 (2014).

[12] G. Onida, L. Reining, and A. Rubio, Electronic exci-
tations: density-functional versus many-body Green's-
function approaches, Rev. Mod. Phys. 74, 601 (2002).

[13] M. Rohlfing and S. G. Louie, Electron-hole excitations
and optical spectra from first principles, Phys. Rev. B
62, 4927 (2000).

[14] S. Albrecht, L. Reining, R. Del Sole, and G. Onida,
Ab initio Calculation of Excitonic Effects in the Opti-
cal Spectra of Semiconductors, Phys. Rev. Lett. 80, 4510
(1998).

[15] M. Rohlfing and S. G. Louie, Electron-Hole Excitations
in Semiconductors and Insulators, Phys. Rev. Lett. 81,
2312 (1998).

[16] F. Wu, F. Qu, and A. H. MacDonald, Exciton band struc-
ture of monolayer $MoS_2$, Phys. Rev. B 91, 075310 (2015).

[17] C. Robert, B. Han, P. Kapuscinski, A. Delhomme,
C. Faugeras, T. Amand, M. R. Molas, M. Bartos,
K. Watanabe, T. Taniguchi, B. Urbaszek, M. Potemski,
and X. Marie, Measurement of the spin-forbidden dark
excitons in $MoS_2$ and $MoSe_2$ monolayers, Nature Com-
munications 11, 4037 (2020).

[18] T. Galvani, F. Paleari, H. P. C. Miranda, A. Molina-
Sánchez, L. Wirtz, S. Latil, H. Amara, and F. m. c.
Ducastelle, Excitons in boron nitride single layer, Phys.
Rev. B 94, 125303 (2016).

[19] M. Zanfrognini, N. Spallanzani, M. Bonacci, E. Molinari,
A. Ruini, M. J. Caldas, A. Ferretti, and D. Varsano,
Effect of uniaxial strain on the excitonic properties of
monolayer $C_{3n}$: A symmetry-based analysis, Phys. Rev.
B 107, 045430 (2023).

[20] P. E. F. Junior, D. Hernangómez-Pérez, T. Amit,
J. Fabian, and S. Refaely-Abramson, Generalized many-
body exciton g-factors: magnetic hybridization and non-
monotonic rydberg series in monolayer $WSe_2$ (2025),
arXiv:2505.18468 [cond-mat.mes-hall].

[21] H. Davenport, J. Knolle, and F. Schindler, Interaction-
Induced Crystalline Topology of Excitons, Phys. Rev.
Lett. 133, 176601 (2024).

[22] H. Davenport, J. Knolle, and F. Schindler, Exci-
ton Berryology (2025), arXiv:2507.22983 [cond-mat.mes-
hall].

[23] G. Kresse and J. Furthmüller, Efficient iterative schemes
for ab initio total-energy calculations using a plane-wave
basis set, Phys. Rev. B 54, 11169 (1996).

[24] P. Giannozzi, S. Baroni, N. Bonini, M. Calandra, R. Car,
C. Cavazzoni, D. Ceresoli, G. L. Chiarotti, M. Cococ-
cioni, I. Dabo, A. Dal Corso, S. de Gironcoli, S. Fabris,
G. Fratesi, R. Gebauer, U. Gerstmann, C. Gougoussis,
A. Kokalj, M. Lazzeri, L. Martin-Samos, N. Marzari,
F. Mauri, R. Mazzarello, S. Paolini, A. Pasquarello,
L. Paulatto, C. Sbraccia, S. Scandolo, G. Sclauzero, A. P.
Seitsonen, A. Smogunov, P. Umari, and R. M. Wentz-
covitch, QUANTUM ESPRESSO: a modular and open-
source software project for quantum simulations of mate-
rials, Journal of Physics: Condensed Matter 21, 395502
(2009).

[25] X. Gonze, B. Amadon, P.-M. Anglade, J.-M. Beuken,
F. Bottin, P. Boulanger, F. Bruneval, D. Caliste, R. Cara-
cas, M. Côté, T. Deutsch, L. Genovese, P. Ghosez, M. Gi-
automassi, S. Goedecker, D. Hamann, P. Hermet, F. Jol-
let, G. Jomard, S. Leroux, M. Mancini, S. Mazevet,
M. Oliveira, G. Onida, Y. Pouillon, T. Rangel, G.-M.
Rignanese, D. Sangalli, R. Shaltaf, M. Torrent, M. Ver-
straete, G. Zerah, and J. Zwanziger, ABINIT: First-
principles approach to material and nanosystem prop-
erties, Computer Physics Communications 180, 2582
(2009).

[26] A. Togo and I. Tanaka, First principles phonon calcu-
lations in materials science, Scripta Materialia 108, 1
(2015).

[27] A. Togo, First-principles Phonon Calculations with
Phonopy and Phono3py, Journal of the Physical Society
of Japan 92, 012001 (2023).

[28] Y. H. Chan, J. B. Haber, M. H. Naik, J. B. Neaton, D. Y.
Qiu, F. H. da Jornada, and S. G. Louie, Exciton Lifetime
and Optical Line Width Profile via Exciton-Phonon In-
teractions: Theory and First-Principles Calculations for
Monolayer $MoS_2$, Nano Letters 23, 3971 (2023).

[29] Y. H. Chan, M. H. Naik, J. B. Haber, J. B. Neaton,
S. G. Louie, D. Y. Qiu, and F. H. da Jornada, Exciton-
Phonon Coupling Induces a New Pathway for Ultrafast
Intralayer-to-Interlayer Exciton Transition and Interlayer
Charge Transfer in $WS_2$-$MoS_2$ Heterostructure: A First-
Principles Study, Nano Letters 24, 7972 (2024).

[30] F. Paleari, H. P. C. Miranda, A. Molina-Sánchez, and
L. Wirtz, Exciton-Phonon Coupling in the Ultraviolet
Absorption and Emission Spectra of Bulk Hexagonal
Boron Nitride, Phys. Rev. Lett. 122, 187401 (2019).

[31] H.-Y. Chen, D. Sangalli, and M. Bernardi, Exciton-
Phonon Interaction and Relaxation Times from First
Principles, Phys. Rev. Lett. 125, 107401 (2020).

[32] G. Antonius and S. G. Louie, Theory of exciton-phonon
coupling, Phys. Rev. B 105, 085111 (2022).

[33] M. Nalabothula, L. Wirtz, and S. Reichardt, Origin of
Interlayer Exciton-Phonon Coupling in 2d Heterostruc-
tures, Nano Letters 25, 6160 (2025).

[34] Y. H. Chan, J. B. Haber, M. H. Naik, S. G. Louie,
J. B. Neaton, F. H. Da Jornada, and D. Y. Qiu, Ex-
citon thermalization dynamics in monolayer $MoS_2$: A
first-principles Boltzmann equation study, Phys. Rev. B
111, 184305 (2025).

[35] D. Y. Qiu, F. H. da Jornada, and S. G. Louie, Optical
spectrum of $MoS_2$: Many-body effects and diversity of
exciton states, Phys. Rev. Lett. 111, 216805 (2013).

[36] J. Noffsinger, E. Kioupakis, C. G. Van de Walle, S. G.
Louie, and M. L. Cohen, Phonon-Assisted Optical Ab-
sorption in Silicon from First Principles, Phys. Rev. Lett.
108, 167402 (2012).

[37] G. Marini, M. Calandra, and P. Cudazzo, Optical Ab-
sorption and Photoluminescence of Single-Layer Boron
Nitride from a First-Principles Cumulant Approach,
Nano Letters 24, 6017 (2024).

[38] K. F. Mak, C. Lee, J. Hone, J. Shan, and T. F. Heinz,
Atomically Thin $MoS_2$: A New Direct-Gap Semiconduc-
tor, Phys. Rev. Lett. 105, 136805 (2010).

[39] G. G. Macfarlane, T. P. McLean, J. E. Quarrington, and
V. Roberts, Fine Structure in the Absorption-Edge Spec-
trum of Si, Phys. Rev. 111, 1245 (1958).

[40] S. G. Louie, J. R. Chelikowsky, and M. L. Cohen, Local-
field effects in the optical spectrum of silicon, Phys. Rev.

Lett. 34, 155 (1975).

[41] G. Strinati, Dynamical Shift and Broadening of Core Excitons in Semiconductors, Phys. Rev. Lett. 49, 1519 (1982).

[42] P. Giannozzi, O. Andreussi, T. Brumme, O. Bunau, M. Buongiorno Nardelli, M. Calandra, R. Car, C. Cavaz- zoni, D. Ceresoli, M. Cococcioni, N. Colonna, I. Carn- imeo, A. Dal Corso, S. de Gironcoli, P. Delugas, R. A. DiStasio, A. Ferretti, A. Floris, G. Fratesi, G. Fugallo, R. Gebauer, U. Gerstmann, F. Giustino, T. Gorni, J. Jia, M. Kawamura, H.-Y. Ko, A. Kokalj, E. Küçükbenli, M. Lazzeri, M. Marsili, N. Marzari, F. Mauri, N. L. Nguyen, H.-V. Nguyen, A. Otero-de-la Roza, L. Paulatto, S. Poncé, D. Rocca, R. Sabatini, B. Santra, M. Schlipf, A. P. Seitsonen, A. Smogunov, I. Timrov, T. Thon- hauser, P. Umari, N. Vast, X. Wu, and S. Baroni, Ad- vanced capabilities for materials modelling with Quan- tum ESPRESSO, Journal of Physics: Condensed Matter 29, 465901 (2017).

[43] J. P. Perdew, K. Burke, and M. Ernzerhof, Generalized Gradient Approximation Made Simple, Phys. Rev. Lett. 77, 3865 (1996).

[44] D. R. Hamann, Optimized norm-conserving Vanderbilt pseudopotentials, Phys. Rev. B 88, 085117 (2013).

[45] M. van Setten, M. Giantomassi, E. Bousquet, M. Ver- straete, D. Hamann, X. Gonze, and G.-M. Rignanese, The PseudoDojo: Training and grading a 85 element optimized norm-conserving pseudopotential table, Com- puter Physics Communications 226, 39 (2018).

[46] W. Kohn and L. J. Sham, Self-Consistent Equations In- cluding Exchange and Correlation Effects, Phys. Rev. 140, A1133 (1965).

[47] M. S. Hybertsen and S. G. Louie, Electron correlation in semiconductors and insulators: Band gaps and quasipar- ticle energies, Phys. Rev. B 34, 5390 (1986).

[48] B. A. Barker, J. Deslippe, J. Lischner, M. Jain, O. V. Yazyev, D. A. Strubbe, and S. G. Louie, Spinor GW/Bethe-Salpeter calculations in BerkeleyGW: Imple- mentation, symmetries, benchmarking, and performance, Phys. Rev. B 106, 115127 (2022).

[49] F. H. da Jornada, D. Y. Qiu, and S. G. Louie, Nonuni- form sampling schemes of the Brillouin zone for many- electron perturbation-theory calculations in reduced di- mensionality, Phys. Rev. B 95, 035109 (2017).

[50] S. Ismail-Beigi, Truncation of periodic image interactions for confined systems, Phys. Rev. B 73, 233103 (2006).

[51] G. F. Koster, J. O. Dimmock, R. G. Wheeler, and H. Statz, Properties of the Thirty-Two Point Groups, Vol. 24 (MIT Press, 1963).

[52] D. Y. Qiu, T. Cao, and S. G. Louie, Nonanalyticity, Val- ley Quantum Phases, and Lightlike Exciton Dispersion in Monolayer Transition Metal Dichalcogenides: Theory and First-Principles Calculations, Phys. Rev. Lett. 115, 176801 (2015).

[53] A. A. Toropov, Y. E. Kitaev, T. V. Shubina, P. P. Paskov, J. P. Bergman, B. Monemar, and A. Usui, Polarization- resolved phonon-assisted optical transitions of bound ex- citons in wurtzite GaN, Phys. Rev. B 77, 195201 (2008).

[54] A. Molina-Sánchez and L. Wirtz, Phonons in single-layerand few-layer $MoS_{2}$ and $WS_{2}$, Phys. Rev. B 84, 155413(2011).

[55] N. Scheuschner, R. Gillen, M. Staiger, and J. Maultzsch, Interlayer resonant raman modes in few-layer $MoS_{2}$, Phys. Rev. B 91, 235409 (2015).

[56] R. Bajaj, N. Venkatareddy, H. R. Krishna- murthy, and M. Jain, Dataset for "Symmetries in zero and finite centre-of-mass momenta excitons" 10.6084/m9.figshare.30025483.v1 (2025).

[57] J. B. Haber, D. Y. Qiu, F. H. da Jornada, and J. B. Neaton, Maximally localized exciton Wannier functions for solids, Phys. Rev. B 108, 125118 (2023).
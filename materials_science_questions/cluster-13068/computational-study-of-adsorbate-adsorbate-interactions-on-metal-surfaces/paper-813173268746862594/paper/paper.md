# Short-chain model of chemisorption: Exact and approximate results*
Theodore L. Einstein†
Department of Physics, University of Pennsylvania, Philadelphia, Pennsylvania 19174
(Received 22 July 1974)

The binding energy of an adatom to a chain consisting of three atoms is obtained exactly by computer as a function of adatom Coulomb repulsion, adatom-substrate hopping, and substrate bandwidth. Three simple approximations are also plotted: (i) weak-binding limit, in which the binding energy is given by the expectation value of the adatom-bulk hopping Hamiltonian calculated in second-order perturbation theory; (ii) rebonded surface complex, in which the adatom forms a diatomic molecule with its nearest neighbor in the chain, and the dimer rebonds perturbatively to the indented chain; and (iii) Hartree-Fock, both restricted and unrestricted. The first two schemes can be joined smoothly by hand, and the resulting curve is much better than Hartree-Fock. The physics of all three cases is carefully studied. An appendix treats the surface diatom case of just a single bulk atom. Here the exact solution and unrestricted Hartree-Fock can be performed analytically. Comparison is also given with Brenig and Schönhammer's solution based on Green's-function formalism with matrix self-energy corrections.

## I. INTRODUCTION
The process of chemisorption has often been viewed from the model of an (extra) atom being joined to an end of a chain of atoms. $^{1,2}$ The obvious advantage of such a simplification is that the computations are correspondingly easier, often to the extent that analytic solutions are possible. In restricting himself to a one-dimensional substrate, Newns $^{2}$ argued that the key property of the surface density of states is its bandwidth, and that its detailed shape is relatively unimportant. In the moment method, $^{3}$ one views the adsorption process from the adatom's standpoint. The interaction with a three-dimensional substrate takes place not with individual atoms but rather with shells consisting of (the symmetric combination of) atoms in equivalent positions, effectively a linear chain. If the three-dimensional substrate is treated in a tight-binding model, then the effective hopping constant in the equivalent chain starts out as a fraction of the bulk hopping constant, but rapidly increases to this value. $^{4}$

We shall make the standard simplifying ansatz $^{1,2}$ of describing the electron orbital at each site by a single spherically-symmetric orbital. For a chain we note that the requirement that an orbital be spherically symmetric about a site could be relaxed to it being cylindrically symmetric about the chain axis and inversion symmetric with respect to the site. To maximize the reactivity and simplify some expressions, we assume a half-filled band, i.e., one electron per atom in the original chain and a single electron on the adatom attaching to its end.

The selection of chain length is governed by one's objectives in the calculations. Naturally a semi-infinite chain is ideal, since then the band states become quasicontinuous and boundary conditions are insignificant. Unfortunately such chains can only be dealt with in terms of an approximation such as Hartree-Fock, $^{2}$ unless one is able to resort to subtle renormalization-group techniques. $^{5}$ At the other extreme is the two-atom "chain." In such a model, one can evaluate the eigenvalues and eigenvectors of the Hamiltonian by hand. This model has been applied to studying Hamiltonians describing identical-site systems, in particular, the Hubbard model $^{6}$ and a three-parameter generalization of it. $^{7}$ In the present case, we are interested in an adatom of one sort attaching itself to a chain of atoms characterized by different parameters. With only one atom to represent the chain, it would be impossible to see the effects of bonding in the chain. Rather like Falicov and Harris, $^{7}$ our intention is to understand better the standard approximations used to characterize the binding process. We thus want a chain sufficiently short so that the approximate calculations can be performed easily by hand. Moreover, since we will obtain the "exact" ground-state energy by diagonalizing the Hamiltonian matrix, it is important to keep the matrix as small as possible. (In the $S_{z}=0$ manifold, a half-filled four-atom chain is represented by a 36 ×36 matrix, a six-atom chain by a 400 ×400 matrix, etc.)

In this paper we shall deal with a chain of four atoms: one representing the adatom, the other three the substrate. With a three-atom chain we can see the beginnings of a bulk band forming. Now (half-filled) chains of odd or even length lie in different $S_{z}$ manifolds, have different level-spacing characteristics, and even have differences in excitation energies in the infinite-length limit. $^{5}$

Hence the next longer chain we would consider in this series is six atoms long (one adatom plus five "bulk"). Indeed our program was set up to accom- modate chains up to eight atoms long, the only problem there being the diagonalization of a huge 4900×4900 matrix. For these longer chains, it would have been possible to invoke computer procedures which merely extract the lowest eigenvalue. $^{8}$ But we would find the approximate calculations far more difficult to perform, and would find little more in- formation to justify this effort. Computer studies of the thermodynamic properties of the Hubbard model have appeared which are based on calcula- tions of four atom rings and chains. $^{9-11}$ Of more relevance are Blyholder and Coulson's $^{12}$ Hückel calculations on short chains of various lengths. Their goal was to ascertain how far down the diag- onal (Coulomb) energy-level parameter of an end- atom has to be shifted (while its nearest-neighbor hopping was held to the bulk value) in order to form a localized (Tamm) state. They concluded that a six- atom chain essentially reproduced the results of a semi-infinite one: A localized state occurs when the unperturbed end-atom level lies below the bot- tom of the band; moreover, the bond order between the end-atom and its neighbor is practically the val- ue obtained for a semi-infinite chain molecular-or- bital calculation. From their Fig. 2 we note that even a four-atom length does reasonably well.

In Sec. II we present a discussion of the Anderson model $^{13}$ as applied to a short chain. After describ ing the procedure computing the binding energy of our prototype system, we present graphs of the exact results as a function of adatom-substrate hopping, for three values of the adatom intra-atom- ic Coulomb term. Also plotted on these graphs are three approximations, which are carefully de- scribed in Sec. III. These are the weak-binding limit, the rebounded surface complex, and Hartree- Fock (HF). Some further comments on the HF so- lution are deferred to the Appendix. In Sec. III we give further comments on the significance of our results and how to apply them to longer chains. The Appendix presents some exact results for a two-atom chain along with comparisons with our approximations. A preliminary account of partof this work has been previously given. $^{14,15}$ 

Our intention here has been to investigate simple approximations to the binding energy. The reader is also alerted to the work of Brenig and Schonham- mer, $^{16}$ which develops a Green's-function descrip tion using a (second-order) self-energy matrix formalism. Their scheme provides an excellent interpolation scheme, but their improved accuracy comes at a price in transparency and calculational facility; in the Appendix we shall apply their scheme to the two-atom chain. For most practical appli- cations, the simple approximations in Sec. III should suffice. In particular, our results suggest that a combination of the weak and rebonded-surface-com- plex curves gives a better picture of binding than does Hartree-Fock.

## II. MODEL AND EXACT RESULTS
The model we shall examine is essentially the Anderson model $^{13}$ for an impurity at the end of an N-1 atom chain; the chain, however, will be treat- ed from a tight-binding rather than free-electron viewpoint. The tight-binding approach is the moreappropriate basis for studying chemisorption $^{17,18}$  onto transition metals, where in fact the strongest binding of adatoms does occur. $^{19}$ Explicitly, we consider
$$
\begin{aligned}
\mathfrak{K}= & E_{a}^{0} \sum_{\sigma} n_{a \sigma}+U n_{a \uparrow} n_{a \downarrow}-V \sum_{\sigma}\left(c_{1 \sigma}^{\dagger} c_{a \sigma}+\text { H. c. }\right) \\
& -T \sum_{i=1}^{N-2} \sum_{\sigma}\left(c_{i \sigma}^{\dagger} c_{i+1, \sigma}+\text { H. c. }\right).
\end{aligned}\qquad(1)
$$

Here, $E_{a}^{0}$ is the energy level of the singly-occupied adatom (roughly the ionization level), U the intra- atomic Coulomb repulsion on the adatom, T the tight-binding hopping parameter for the chain (the atoms of which are numbered consecutively), and V the hopping between the adatom and the first atom of the chain. The diagonal energies of the chain atoms are taken as zero, fixing our energy zero as the center of the "bulk" states. For simplicity we shall restrict ourselves to the so-called Ander- son symmetric model, in which
$$E_{a}^{0}=-\frac{1}{2} U.\qquad(2)$$

This restriction gives us particle-hole symmetry, i.e., complete symmetry in energy (about the band center). For the half-filled band case we are con- sidering here, it also insures that the adatom as well as the bulk-atom orbitals are singly occupied, so that we need not worry about charge transfer between the adatom and the "bulk". Our para- metric choice thus optimizes the covalent (rather then ionic) binding strength.

As we remarked earlier, we will deal only with a chain of total $S_{z}=0$ , i. e., an equal number of spin-up and spin-down electrons. This ansatz gives us a closed-shell system, which generally characterizes stable chemical systems. This ansatz plus the half-filled band condition require that the number N of atoms in the full chain be even, so that there can be $\frac{1}{2} N$ spins in each direction.
The number of basis states in this manifold can be easily determined from combinatorical arguments in a second-quantized viewpoint: We have N spin- up slots into which to place $\frac{1}{2} N$ identical electrons. There are $(\begin{array}{c}N N / 2\end{array})$ such combinations. A similar argument applies to down electrons. Since these choices are independent, there are $[(\begin{array}{c}N N / 2\end{array})]^{2}$ possible states. This number is 4, 36, 400, and 4900 for

![](./images/813173268746862594_1.jpg)

FIG. 1. Interaction energy (negative of binding energy) vs hopping parameter $V$ for three values of the intraada- tomic Coulomb $U$: (a) 1.0, (b) 2.5, (c) 4.0. All energies are in units of $2T$, where $-T$ is the interatomic hopping parameter of the three-atom "bulk" chain. Each figure shows exact points derived by computer (x's), weak- limit results (solid curve), rebond surface complex (long-dashed curve), and unrestricted (short-dashed curve) and restricted (dash-dotted curve) Hartree-Fock. Small vertical line indicates where unrestricted solution reduces to the restricted one.

$N$ equalling 2, 4, 6, and 8, respectively. Thus for a four-atom chain, we can use any diagonalization routine$^{20}$; for any longer chain, one should employ a method which extracts only the lowest eigenvalue. $^{8}$

As mentioned above, we will focus on the inter- action energy (i.e., the negative of the binding energy) of the adatom with the chain. In our model, the desorbed energy (i.e., the $V=0$ case) is easily written down. The single electron on the adatom has energy $E_{a}^{0}=-\frac{1}{2}U$. The three-atom "bulk" chain, having no Coulomb terms, is correctly de- scribed by the sum of the energies of the occupied (one-electron) molecular orbitals. The MO energies are the eigenvalues of the bulk Hamiltonian matrix for a particular spin direction, this matrix being
$$
\begin{pmatrix}
0 & -T & 0 \\
-T & 0 & -T \\
0 & -T & 0
\end{pmatrix} \, \tag{3}
$$
and its roots $-\sqrt{2}T$, 0, and $+\sqrt{2}T$. This indicates a bandwidth $W_{b}$ of $2\sqrt{2}T$, but we shall take $W_{b}$ to have its infinite-chain limit, $4T$. We designate the associated eigenstates $|\psi_{-}\rangle$, $|\psi_{0}\rangle$, and $|\psi_{+}\rangle$, respectively. The ground state of the system is $|\psi_{-}\rangle$ doubly occupied and $|\psi_{0}\rangle$ singly occupied with spin opposite to the electron on the adatom, to maintain $S_{z}=0$. Thus we see that this unbonded ground state is doubly degenerate, and has energy
$$
E_{0}=-\frac{1}{2}U-2\sqrt{2}T \. \tag{4}
$$

In general, the exact chemisorbed ($V\neq0$) solution must be obtained by nonanalytic (computer) means. The interaction energy is then found by subtracting

$E_0$ from it. We have followed this procedure for several values of $V$ and for $U=1.0,2.5$, and 4.0 (in units where $T=\frac{1}{2}$, so that $U/W_b=\frac{1}{2},\frac{5}{4}$, and 2, respectively); the results are indicated by the $x$'s in Figs. 1a, 1b, and 1c, respectively. The middle value of $U$ corresponds roughly to hydrogen on tungsten, which is a good realization of a half- filled band. Hydrogen on nickel corresponds to a $U/W_b\sim\frac{11}{4}$. A transition metal on a transition metal might be represented by $U/W_b\sim\frac{1}{2}$.

In Fig. 1 we also plot three approximate results, which we shall discuss in detail in the next section. To preview, the first is the weak limit, in which we calculate the binding energy using second-order perturbation theory in $V$. For stronger $V$, the rebonded-surface-complex (RSC) picture is more appropriate. Here the end atom of the chain (called "one" above) separates from the chain to form essentially a diatomic molecule with adatom. The dimer then rebonds to the indented chain. Finally, we compute the restricted (RHF) and unrestricted (URHF) Hartree-Fock results. For all values of $U$, we see that there is a smooth transition from the regime where the weak limit holds to that where RSC is best; it would be easy to eyeball an interpolated curve. Moreover, this curve is far more accurate then the URHF curve. Furthermore, URHF requires an iterative solution, whereas here the weak and RSC curves can be determined exactly.

### III. APPROXIMATE METHODS
#### A. Weak limit
For weak hopping, i. e., $V^2\lesssim UT$, we can accurately describe the binding energy by calculating the second-order perturbation contribution of
$$
\mathcal{K}_V=-V \sum_{\sigma}\left(c_{1 \sigma}^{\dagger} c_{a \sigma}+\text { H. c. }\right)
\tag{5}
$$
to the eigensystem of the $V=0$ Hamiltonian. We recall that the ground state of the chain is doubly degenerate. Let us denote these two states as $|a\uparrow\rangle$ and $|a\downarrow\rangle$ indicating the spin direction of the adatom's electron; the electron in the MO has the opposite spin. The perturbation $\mathcal{K}_V$ lifts the degeneracy, but only in second order. The first-order term vanishes since two hops are required to depart from and return to $|a\uparrow\rangle$ or $|a\downarrow\rangle$. There are six singly excited states, which fall into three categories:

(a) Two states can be obtained by single hops from either $|a\uparrow\rangle$ or $|a\downarrow\rangle$-these have $|\psi_{-}\rangle$ and either $|\psi_{0}\rangle$ or the adatom doubly occupied. Their energies are $-2\sqrt{2}T$.

(b) Two states correspond to hopping an electron from the adatom to $|\psi_{\lrcorner}\rangle$. They have energy $-\sqrt{2}T$.

(c) Conversely, an electron can hop from $|\psi_{\lrcorner}\rangle$ to doubly occupy the adatom. The energy of these states, $-\sqrt{2}T+U+2E_a^0$, is degenerate with that of the two b states in the Anderson symmetric case we are considering.

In order to compute matrix elements, we must find the amplitudes of the three MO's on the end-atom orbital $|1\rangle$, since $\mathcal{K}_V$ connects the adatom to $|1\rangle$, not to the MO's directly. It is not hard to show
$$
\left|\psi_{0}\right\rangle=\frac{1}{\sqrt{2}}\left(\begin{array}{r}
1 \\
0 \\
-1
\end{array}\right) \quad\left|\psi_{\star}\right\rangle=\frac{1}{2}\left(\mp \frac{1}{\sqrt{2}} \underset{1}{2}\right),
\tag{6}
$$
where the elements of the column matrices are the amplitudes of the MO in the orbitals of atoms 1, 2, and 3, respectively. Thus $V_{a0}=V/\sqrt{2}$ while $V_{a*}=\frac{1}{2}V$.

In second-order perturbation theory, states $|a\uparrow\rangle$ and $|a\downarrow\rangle$ will both be lowered via the intermediate b and c states by
$$
2\left(\frac{1}{2} V\right)^{2} /\left(-\sqrt{2} T-\frac{1}{2} U\right),
\tag{7}
$$
where the factor of 2 denotes the number of b-c states entering, and $\frac{1}{2}$ shows that the hopping electron interacts with $|\psi_{\star}\rangle$. The degeneracy of $|a\uparrow\rangle$ and $|a\downarrow\rangle$ is lifted in second-order perturbation theory by their interaction through the a states. Both these states are invariant to spin inversion. We thus form the combinations of $|a\uparrow\rangle$ and $|a\downarrow\rangle$ which are symmetric and antisymmetric with respect to spin inversion; these are the singlet and triplet states, respectively. By symmetry, $|a\uparrow\rangle$ and $|a\downarrow\rangle$ contribute equally to each of these states, with a relative minus sign in one case and a plus sign in the other. The additional lowering the symmetric singlet state is
$$
2 V^{2}\left(2 \frac{1}{\sqrt{2}} \frac{1}{\sqrt{2}}\right)^{2} /\left(-\frac{1}{2} U\right).
\tag{8}
$$

The prefactor of 2 indicates two a states; the first $1/\sqrt{2}$ arises from the normalization of the singlet state, the second from the occupancy amplitude of $|\psi_{0}\rangle$ on site 1. The 2 within the parentheses arises from the equal contributions of $|a\uparrow\rangle$ and $|a\downarrow\rangle$ to the matrix element.

We thus find that the ground state in the weak limit is a singlet state with energy
$$
\Delta W_{w}=-V^{2} /(U+2 \sqrt{2} T)-4 V^{2} / U.
\tag{9}
$$

For $U\gg T$, we see $\Delta W_{w}\sim-5V^{2}/U$. For $U\ll T$, $\Delta W_{w}\sim-4V^{2}/U$ which is distinctly different from the $V\ll T$ limit of the RHF (restricted Hartree-Fock) solution, given in Sec. IIIC of $\frac{1}{4}U-2V$.

The weak-limit scenario is reminiscent of the Kondo problem, $^{21}$ where a spin-$\frac{1}{2}$ impurity couples to a spin-$\frac{1}{2}$ host through a rotationally invariant Hamiltonian to form states of total spin 0 and 1. Since the singlet state has lower energy, we have antiferromagnetic exchange. These observations

suggest an alternate derivation of our second-order result using the Schrieffer-Wolff transformation. $^{22}$ This canonical transformation removes the first-order term in $V$ from the Anderson Hamiltonian: It removes a manifold of excited states while preserving their influence on the lower lying states of interest by adding terms to the Hamiltonian. For $V$ suitably small (i.e., $U$ much greater than some measure of the adatom level width) it suffices to stop at the second-order addition to the Hamiltonian $\mathcal{K}_{2}$ which is of order $V^{2} / U$.

In the present instance, the bulk $k$ states of the Anderson model are replaced by our three MO's. Only those terms of $\mathcal{K}_{2}$ with both $k$'s identical, contribute. To make the correspondence, we define an $s$-$d$-type exchange parameter
$$
J_{k k}=2\left|V_{k a}\right|^{2}\left(\frac{1}{\epsilon_{k}-\frac{1}{2} U}-\frac{1}{\epsilon_{k}+\frac{1}{2} U}\right),
\tag{10}
$$
and a direct parameter
$$
W_{k k}=\left|V_{k a}\right|^{2} /\left(\epsilon_{k}+\frac{1}{2} U\right).
\tag{11}
$$

We take the expectation value of $\mathcal{K}_{2}$ with respect to the singlet ground state, making the standard decomposition into four components: (a) an exchange interaction
$$
\frac{3}{4} J_{00}=-3 V^{2} / U,
\tag{12a}
$$
(b) a direct interaction
$$
W_{00}+\frac{1}{4} J_{00}+2\left(W_{--}+\frac{1}{4} J_{--}\right)=\frac{V^{2}}{2}\left(\frac{1}{U-2 \sqrt{2} T}-\frac{1}{U+2 \sqrt{2} T}\right),
\tag{12b}
$$
(c) a shift term
$$
-\sum_{k} W_{k k}=-\frac{V^{2}}{U}-\frac{V^{2}}{2}\left(\frac{1}{U-2 \sqrt{2} T}+\frac{1}{U+2 \sqrt{2} T}\right), \ (12 \mathrm{c})
$$
and (d) a term transferring two charges, which does not contribute here. Adding these three contributions gives our previous weak-limit result of Eq. (9).

In Section IIID, we shall elaborate on the significance of this picture as we discuss the generalization of our results to longer chains.

### B. Rebonded surface complex (RSC)
The regime of strong binding is characterized by the formation of a surface complex. $^{2,18,23,24}$ In this case a single orbital-or an appropriate symmetrized group orbital-(here just the end-atom orbital) detaches from the substrate (the chain) to form a diatomic covalent molecule with the adatom. This dimer then rebonds (perturbatively) to the indented bulk, here the two-atom chain. We use the term "surface complex" rather than "surface molecule" to emphasize: (a) that the bulk contribution can be a group orbital rather than a single atom; (b) that the dimer will not be doubly occupied when the binding weakens, i.e. at the low end of the RSC regime.

The MO's for the indented chain are the eigenfunctions of the matrix
$$
\left(\begin{array}{cc}
0 & -T \\
-T & 0
\end{array}\right),
\tag{13}
$$
with eigenvalues $-T$ and $+T$; explicitly, they are
$$
(1 / \sqrt{2})\left(\begin{array}{l}
1 \\
1
\end{array}\right) \text { and }(1 / \sqrt{2})\left(\begin{array}{r}
1 \\
-1
\end{array}\right),
\tag{14}
$$
respectively. The neutral nonmagnetic two electron chain has energy $-2 T$, so that the energy of severing atom 1 from the chain is $E_{3-2}=2(\sqrt{2}-1) T$.

The neutral, nonmagnetic, two-atom surface complex can be treated exactly. The appropriate manifold is spanned by four basis vectors, i.e., the $\left[\left({ }_{N}^{N} / 2\right)\right]^{2}$ vectors for $N=2$ corresponding to one of the two electrons in each spin direction. They have been called $^{7}$ the Heitler-London neutral (HLN-one electron per site) and Heitler-London polar (HLP-one site doubly occupied) states. The resulting $4 \times 4$ matrix of the Anderson symmetric Hamiltonian has the four eigenenergies $0,-\frac{1}{2} U$, and $\frac{1}{2}\left\{-\frac{1}{2} U \pm\left[\left(\frac{1}{2} U\right)^{2}+16 V^{2}\right]^{1 / 2}\right\}$. From our discussion of the weak limit, it is not hard to see how these solutions arise. We recall that $\mathcal{K}_{V}$ couples only states which are symmetric with respect to spin inversion. Hence the first two eigenenergies correspond to antisymmetric combinations of the HLP and HLN pairs of states, respectively. The latter two energies are the antibonding and bonding combination of the symmetric combination of each of the pairs of Heitler-London states. We denote by $E_{S C}$ the most negative energy of the four; it gives the covalent binding of the surface complex.

Thus, if we neglect rebonding, we find
$$
\begin{aligned}
\Delta W_{S C} & =E_{S C}+E_{3-2} \\
& =\frac{1}{4} U-\left[\left(\frac{1}{4} U\right)^{2}+4 V^{2}\right]^{1 / 2}+2(\sqrt{2}-1) T. \quad(15)
\end{aligned}
$$

For $V \ll U$
$$
\Delta W_{S C}-2(\sqrt{2}-1) T-8 V^{2} / U+O\left(V^{4} / U^{3}\right). \quad(16)
$$

For small $V$, then, the binding gained in forming the surface dimer is insufficient to compensate the removal of atom 1 from the chain; the process is endothermic. For $V \gg U$
$$
\Delta W_{S C}--2 V+\frac{1}{4} U+2(\sqrt{2}-1) T-U^{2} / 64 V+O\left(1 / V^{2}\right),
\tag{17}
$$
which shows the formation of a surface dimer (two electrons lowered by $V$ ), with contervailing separation energy and the MO-like effect of the Coulomb term.

The rebonding of the surface complex to the chain is described by

$$
\mathcal{K}_{T}=-T \sum_{\sigma}\left(c_{1 \sigma}^{\dagger} c_{2 \sigma}+\text { H. c. }\right). \quad(18)
$$

Since the calculation of the second-order perturba- tional contribution of $\mathcal{K}_{T}$ is a rather tedious and not particularly enlightening chore, we shall merely describe the procedure before presenting the re- sult. As mentioned, the ground state of the dimer is a combination of the symmetric combination of the HLN states and that of the HLP states; the ratio of the two pairs is $|E_{S C}|$ to $2 V$ . By the spin sym metry of the ground state and $\mathcal{K}_{T}$ , we need consider only hopping by spin-up electrons, and then double the final result. The first-excited states are formed by hopping an electron off (onto) the dimer to (from) an MO of energy $+T(-T)$ . There are two basis states for the singly occupied spin-downdimer, corresponding to the adatom or atom 1 being occupied. The eigenvalues of the associated Hamiltonian matrix are
$$E_{ \pm}=\frac{1}{4}\left[-U \pm\left(U^{2}+16 V^{2}\right)^{1 / 2}\right].\qquad(19)$$

The eigenvector associated with $E_{-}$ is symmetriclike with a ratio of adatom component to atom 1 amplitude of $|E_{-}|$ to $V$ ; the $E_{+}$ eigenvector will be antisymmetric-like and orthogonal to the first. By particle-hole symmetry, the triply-occupied dimer will have the same eigenenergies and essentially identical eigenvectors.
Evaluating matrix elements straightforwardly, using second-quantized operators, one finds thatthe rebonding energy due to spin-up directions is $^{15}$ 
$$\begin{aligned}
\frac{1}{2} \Delta W_{R}=-T^{2} & \left(\frac{\left(E_{S C} E_{-}+2 V^{2}\right)^{2}}{2 E_{-}+T-E_{S C}\right)\left(E_{S C}^{2}+4 V^{2}\right)\left(E_{-}^{2}+V^{2}\right)} \\
& \left.+\frac{\left(E_{S C} E_{+}+2 V^{2}\right)^{2}}{2\left(E_{+}+T-E_{S C}\right)\left(E_{S C}^{2}+4 V^{2}\right)\left(E_{+}^{2}+V^{2}\right)}\right).
\end{aligned}\qquad(20)$$

In this expression $E_{ \pm}+T-E_{S C}$ is the energy de nominator for second-order perturbation theory, while the other terms come from mixing factors and normalizations. It is an interesting measureof the near symmetry (antisymmetry) of the $E_{-}(E_{+})$ state that the second term contributes at most $2 \%$  of the first term, and in general is two or three orders of magnitude smaller. It is more trans- parent to display the limiting values of the rebond-ing energy:
$$\begin{aligned}
\Delta W_{R} & \sim-T & V \ll U \\
& \sim-\frac{T^{2}}{V+T}, & V \gg U.
\end{aligned}\qquad(21)$$

These terms both arise solely from the $E_{-}$ term. The decrease in $\Delta W_{R}$ with increasing $V$ is smooth and monotonic. The limiting cases can be easily visualized as follows: For $V \ll U$ , there is virtually no bond between the adatom and atom 1. The ener- getics lock the dimer into HLN states, so that atom1 is always singly occupied but must have the op- posite spin to the adatom electron. Hence, we find a bonding interaction between atoms 1 and 2, but with the normal factor of 2 absent since the electron on atom 1 lacks freedom of spin direction. For $V \gg U$ , the dimer is locked firmly into a doubly occupied covalent bond. The expression shows a second-order perturbation situation, with the inter- mediate state characterized by the removal (addi-tion) of an electron from (to) a bonding (antibonding) orbital. Note also that in these limiting regimes of complete and zero correlation, the Coulomb $U$  vanishes from $\Delta W_{R}$ .

## C. HARTREE-FOCK
The Hartree-Fock approximation transforms the Hamiltonian of Eq. (1) into a one-electron prob- lem by replacing the two-body term by a one-body operator interacting with an effective field, which is determined self-consistently. Explicitly,
$$\mathcal{K}_{H F}=\mathcal{K}_{1}+\mathcal{K}_{t}-U\left\langle n_{a \uparrow}\right\rangle\left\langle n_{a \downarrow}\right\rangle,\qquad(22a)$$
 where
$$\mathcal{K}_{\sigma}=E_{a \sigma} n_{a \sigma}-V\left(c_{1 \sigma}^{\dagger} c_{a \sigma}+\text { H. c. }\right) \quad(22 b)$$
 and
$$E_{a \sigma}=E_{a}^{0}+U\left\langle n_{a,-\sigma}\right\rangle \text {. }\qquad(22c)$$

In the case of the Anderson symmetric model, the adatom stays neutral, and the self-consistency equation becomes
$$\left\langle n_{a \uparrow}\right\rangle+\left\langle n_{a \downarrow}\right\rangle=1.\qquad(23)$$

The general features of the Hartree-Fock solution are well known. $^{13}$ The spin-restricted ansatz
$$\left\langle n_{a \uparrow}\right\rangle=\left\langle n_{a \downarrow}\right\rangle=\frac{1}{2}\qquad(24)$$
 always provides a trivial solution to the coupled equations. For sufficiently small $V$ , two pairs ofsolutions come into existence:
$$\left\langle n_{a \sigma}\right\rangle=\frac{1}{2}+x, \quad\left\langle n_{a,-\sigma}\right\rangle=\frac{1}{2}-x, \quad 0<x<\frac{1}{2}. \quad(25)$$

The double degeneracy is clearly a consequence of the invariance of $H_{H F}$ to spin inversion. When the nontrivial solutions exist, they give the stable so- lution to problems, and the trivial solution is un- stable.
Combining Eqs. (22c) and (25), we find
$$E_{a \pm \sigma}=\mp U x \text {. } \quad(26)$$

Since the Hartree-Fock Hamiltonian is a one-elec- tron object, its ground state is given by the sum of the four lowest molecular-orbital energies, minus the Coulomb counter term. These four eigenener- gies are the two lowest eigenvalues of the two ma- trices

$$
\begin{pmatrix}
E_{aa} & -V & 0 & 0 \\
-V & 0 & -T & 0 \\
0 & -T & 0 & -T \\
0 & 0 & -T & 0
\end{pmatrix} \quad \text{.}
\tag{27}
$$

In the restricted (RHF) case, the two matrices become identical, the upper left-hand element vanishing in both. Then their eigenvalues are the roots of a double quadratic:
$$
\pm\left\{\frac{1}{2}\left[\left(V^{2}+2 T^{2}\right) \pm\left(V^{4}+4 T^{4}\right)^{1 / 2}\right]\right\}^{1 / 2}.
\tag{28}
$$

The two negative outer roots give the energies of the two doubly occupied MO's. From their sum we must subtract the Coulomb counter term $U(\frac{1}{2})^{2}$ and the energy of the dissociated system, given in Eq. (4). Hence the RHF interaction energy is
$$
\begin{aligned}
\Delta W_{\mathrm{RHF}}= & -\sqrt{2}\left\{\left(V^{2}+2 T^{2}\right)+\left(V^{4}+4 T^{4}\right)^{1 / 2}\right]^{1 / 2} \\
& +\left[\left(V^{2}+2 T^{2}\right)-\left(V^{4}+4 T^{4}\right)^{1 / 2}\right]^{1 / 2}-2 T\} \quad (29 \mathrm{a})
\end{aligned}
$$
$$
\sim-2 V+2(\sqrt{2}-1) T+\frac{1}{4} U-T^{2} / V+O\left(T^{3} / V^{2}\right) \quad (29 \mathrm{~b})
$$
$$
\text{for } V \gg T
$$
$$
\sim \frac{1}{4} U-\sqrt{2} V+O\left(V^{2} / T\right) \quad \text{for } V \ll T. \tag{29c}
$$

As Fig. 1 shows, RHF does fairly well for strong hopping parameters $V$. It differs from RSC only in the $1 / V$ terms, the RSC terms being $-U^{2} / 64 V-T^{2} /(V+T)$. On the other hand, RHF fails strikingly for small $V$. In this region the "preparation cost" of suppressing correlation effects on the adatom far exceeds the advantage to be realized in subsequently bonding. We expect RHF to be valid in the regime in which $U$ is less than the width of the end-atom "orbital" (i.e., the width of the surface density of states). For large (relative to the bandwidth) $V$ this width is of order $V$, since that is the order of the split between the bonding and the antibonding orbitals. For small $V$, we expect the level width to be proportional to the level broadening, which is of order $V^{2} / T .^{18}$ In the present chain calculation for small $V$, we will find that the RHF treatment is suitable for larger $U$ than predicted by these general arguments. The reason is that the chain energies are highly discrete rather than quasicontinuous. Hence the density of states cannot easily broaden slightly. The limit of validity of RHF is indicated in Fig. 1 by a small vertical slash, and we find that this point is more nearly linear than quadratic in $U$. (The exponent of $V$ is about $1.1^{*}$ in the range of $U$ displayed.)

The unrestricted Hartree-Fock solution (for $V$ small enough so that it does not reproduce RHF) also underestimates the binding energy, except in the limiting case of $V=0$, as Fig. 1 illustrates. This underestimation of the energy of the chemisorbed system is a consequence of the variational theorem, $^{25}$ since the Hartree-Fock solution can be derived variationally. The approximate treatment of correlation effects, from which the energy underestimation stems physically, makes the method suspect for calculating adatom occupation numbers such as magnetic moment. $^{26}$ Thus, while for very small $V$, URHF predicts the adatom will have nearly the moment of an unpaired electron, we know from experience in the Kondo problem $^{21}$ that such a moment is quenched by the antiferromagnetic coupling to the bulk. Nonetheless, URHF does give a reasonable and calculable qualitative account of the interaction energy, and it is therefore frequently invoked.

In order to compute the Hartree-Fock solution, we would ideally like to know the energy of the chain as a function of $x$ [as defined in Eq. (25)]. This function, which we shall call $\epsilon(x)$, is the sum of the two lowest eigenvalues of each of the two matrices of Eq. (27), minus the counter term $U\left(\frac{1}{4}-x^{2}\right)$. Since $x=0$ is always a solution to the Hartree-Fock equations, $\epsilon(x)$ will always be flat at $x=0$. Now we know there can exist at most one additional solution (extremum) for positive $x$, and that if such a solution exists, it must be the minimum. Hence, if $\epsilon(x)$ is decreasing at $x=0$ it must decrease monotonically until it passes through a minimum, and then increase monotonically. Thus, evaluating the second derivative at the origin (since $\epsilon(x)$ is flat there) tells us whether the RHF solution is the (stable) solution to the coupled equations. If it is not, we can find the stable solution by seeking the other zero of $d \epsilon / d x$ using the Newton-Raphson method. Since $x=0$ is a flat point, we start our computer interations at $x=\frac{1}{2}$. This technique was used to generate the URHF subcurve in Fig. 1. Further details appear in the Appendix, along with an explicit illustrative URHF solution of an adatom attached to a single bulk atom. In particular, we verify expressly for two atoms what we observe in Fig. 1 for four: That at the point where the RHF and URHF solutions join, their slopes (with respect to $V$) are the same.

### D. Dependence on chain length; more detailed approximations

In Fig. 1 we see that both the URHF and the weak solutions appear quadratic in $V$, but that the magnitude of the weak solution is greater. The Appendix shows $\Delta W_{\text {URHF }} \sim-4 V^{2} / U$ for an adatom attached to a single bulk atom. This dimer has a weak-limit interaction energy of $-8 V^{2} / U$. This number can be derived by doing second-order perturbation theory on the dimer ground state, viz., the singlet combination of the HLN states. As before, we can alternatively use the Schrieffer-Wolff transformation. For the dimer there is a single $k$ state, and the resultant energy expectation value is $J_{00}$. However, the $J_{00}$ is twice the $J_{00}$ for the four-atom chain, since $V_{0 a}$ is $V$ rather than $V / \sqrt{2}$. This approach

allows us to pin-point the source of the error in the URHF coefficient. In the dimer we have equal admixtures of the singlet and triplet in the MO state, corresponding to the choice of one of the HLN states as the ground state. The second-order (in $\mathcal{C}_{V}$) energy of either is $-4 V^{2} / U$. In forming the singlet combination, we double the binding energy of the dimer.

The Schrieffer-Wolff framework gives another perspective on the essence of the error in URHF: It destroys the rotational invariance of the Hamil- tonian and thereby misses the Kondo quenching of the adatom moment. The HF substitution of Eq.(21) amounts to the replacement $\vec{S}_{a} \cdot \vec{S}_{k} \to \vec{S}_{a}^{z} \vec{S}_{k}^{z}$, there by neglecting the $x$ and $y$ components in the exchange contribution; the direct contribution is unaffected. The HF exchange term therefore has the value $\frac{1}{4} J_{00}$ rather than $\frac{3}{4} J_{00}$. In other words, HF neglects an energy of $\frac{1}{2} J_{00}$ or $4 V^{2} / U$ divided by a squared normalization factor of order the length of the chain. As the chain length approached infinity, Joo vanishes, and the URHF energy approaches the weak result (which is exact in the small $V$ limit). Thus, the leading term in the binding energy in the Kondo problem is second-order in $J$, i.e., of order V4/U2T.21 This perturbation energy is based only on the exchange part of the Hamiltonian. If the lim- it is taken correctly, the moment will still be quenched in the weak (exact) solution, though not in URHF. The first-order perturbation term of the full (including the direct term, etc.) Kondo Hamil- tonian will be a good representation of the ground- state energy only if the second-order term is much smaller, i. e., $(V^{2} / U)^{2} / T \ll V^{2} / U$ or $V^{2} \ll U T$ . This is just the criterion we used to determine the up- per limit of validity for the weak result. For $U$  $=1.0,2.5$ , and $4.0, V=\sqrt{U T}$ is $0.707,1.178$ , and1.414, respectively, well above where the RSC curve takes over.

Our methods could be applied to compute the ex- act and approximate expressions for the excited state energies of a four-atom chain. In order to make contact with an infinitely long chain, we would then want to apply Wilson's exact solution to the Kondo problem. $^{5}$ However, although the trans formed form of his Hamiltonian looks seductively like a tight-binding model for the chain, the trans- formed states do not correspond to localized or- bitals in any way. $^{27}$ Hence, it is not at all obvious how to draw any correspondence, and we shall not pursue this project here.

## ACKNOWLEDGMENTS
It is a pleasure to thank Professor J. Robert Schrieffer for proposing this area of investigation and for providing numerous helpful suggestions in the course of many conversations about this re- search. During a valuable discussion with Profes- sor Henry Ehrenreich and Dr. C. D. Gelatt, Jr., they pointed out the existence of Ref. 7. Several enlightening conversations with Dr. Paul L. Norris are also gratefully acknowledged.

## APPENDIX
In the final paragraph of Sec. IIIC, we mentioned some aspects of the computer solution of the unre- stricted Hartree-Fock equations. In the following paragraph we give further details. We then turn to the dimer consisting of an adatom and a single bulk atom. We conclude by applying the techniques of Brenig and Schönhammer $^{16}$ to this dimer.

To find the roots comprising $\epsilon(x)$ , which we de fined in the last paragraph of Sec. IIIC, we must solve the characteristic equations of the matrices of Eq. (27). These characteristic polynomials have the form
$$f(E) \mp x g(E)=0, \quad \text { (A1) }$$
where
$$f(E)=E^{4}-\left(V^{2}+2 T^{2}\right) E^{2}+V^{2} T^{2} \quad \text { (A2) }$$
and
$$g(E)=U E\left(E^{2}-2 T^{2}\right). \quad \text { (A3) }$$

We note that $f(E)$ is even, while $g(E)$ is odd. Thus, the equation is invariant under the simultaneous transformations $E \to -E$ and $x \to -x$ . Consequently, the negative of the upper two roots of Eq. (A1) with one sign of $x g(E)$ are the same as the lower two roots of the equation with the opposite sign. Hence, we need to find the roots of only one quartic equa- tion. $^{28}$ Using implicit differentiation to determine the slope and curvature of $\epsilon$ , we find
$$\frac{d E_{i}}{d x}=\frac{-g\left(E_{i}\right)}{x g^{\prime}\left(E_{i}\right)+\operatorname{sgn}(i) f^{\prime}\left(E_{i}\right)}, \quad \text { (A4) }$$
 where $E_{i}$ is one of the four occupied eigenenergies and sgn $(i)$ is the sign of $x g(E)$ in the characteristic equation to which it is a lower root. Thus
$$\epsilon^{\prime}(x)=\sum_{i=1}^{4} \frac{d E_{i}}{d x}+2 U x. \quad \text { (A5) }$$

To find the second derivative $\epsilon$ , we merely dif ferentiate Eq. (A5), and ultimately Eq. (A4) with respect to $x$ , remembering that $E_{i}$ is a function of $x$ .

We can get a better understanding for the nature of the URHF solution by considering the extreme case of just a single atom representing the bulk, so that we are actually performing the surface dimer calculation in URHF. We can now find the MO en- ergies explicitly and can write
$$\epsilon_{[2]}(x)=-\left(U^{2} x^{2}+4 V^{2}\right)^{1 / 2}+U x^{2}-U / 4, \quad \text { (A6) }$$
 where the subscript indicates that this expression

applies to the dimer. $\epsilon_{[2]}(x)$ has its minimum at $x=\pm(U^{2}-16V^{2})^{1/2}/2U$ when $4V<U$. The corresponding equality gives the boundary between URHF and RHF. Note that here this boundary is linear in $V$ since there is no substrate level broadening whatsoever. We also can check explicitly that $x=0$ is always a flat point $-\epsilon$ is only a function of $x^{2}-$ and that $\epsilon$ gives the RHF solution for $V\geqslant\frac{1}{4}U$. Inserting the extremum value of $x$ into Eq. (A6), and then subtracting the energy of the dissociated chain (viz., $E_{a}^{0}=-\frac{1}{2}U$, we find

$$
\Delta W_{[2] \mathrm{URHF}}=-4 V^{2} / U \text { for } V \leq \frac{1}{4} U. \quad \text { (A7) }
$$

The corresponding restricted Hartree-Fock interaction energy is

$$
\Delta W_{[2] \mathrm{RHF}}=-2 V+\frac{1}{4} U. \quad \text { (A8) }
$$

At $V=\frac{1}{4} U$, these two energies are the same $\left(-\frac{1}{4} U\right)$, as required, and their derivatives with respect to $V$ are also identical (namely, $-2$).

The exact solution to the dimer is just the surface molecule we considered in Sec. III B. Its negative binding energy is just $E_{\mathrm{SC}}+\frac{1}{2} U$:

$$
\begin{aligned}
\Delta W_{[2] \text { exact }} & =\frac{1}{4} U-\left[\left(\frac{1}{4} U\right)^{2}+4 V^{2}\right]^{1 / 2} \\
& \sim-2 V+\frac{1}{4} U-U^{2} / 64 V \quad V \gg U \\
& \sim-8 V^{2} / U, \quad V \ll U. \quad(\mathrm{A} 9)
\end{aligned}
$$

Obviously, the surface-complex regime always holds for the dimer; there is nothing to which to rebond. We have already commented on the weak limit in the first paragraph of Sec. III D, noting how URHF loses the singlet ground state by discarding rotational invariance in spin.

We further note that the $4 \times 4$ matrix used in deriving $E_{S C}$ reduces to two $2 \times 2$ matrices along the diagonal when the occupation-number basis is rotated to the basis states which are eigenstates of total spin. The singlet and triplet matrices are

$$
\left(\begin{array}{cc}
0 & -2 V \\
-2 V & -\frac{1}{2} U
\end{array}\right) \text { and }\left(\begin{array}{cc}
0 & 0 \\
0 & -\frac{1}{2} U
\end{array}\right) \text {, }
$$

respectively, where in each case the first state is the HLP combination and the second the HLN. We see explicitly now that the mixing caused by $\mathcal{K}_{V}$ only affects the singlet combinations, and with an apparent strength twice the value for the diatomic occupation-number basis. Since the singlet state intrinsically has no local moment, we see that $\mathcal{K}_{V}$ will not create one, and that any such prediction by URHF is even qualitatively wrong, as shown more generally by Schrieffer and Mattis $^{26}$ and alluded to in Sec. III C.

As suggested in the introduction, the Green's-function formalism with matrix self-energy corrections as applied to the chain by Brenig and Schönhammer $^{16}$ (BS) provides a quite accurate but rather complicated approximation scheme. Since their paper gives few details of the application to a finite chain, we believe an explicit illustration of its use for the dimer will be of interest.

The interaction energy is calculated using a formula requiring only the adsorbate Green's function $^{29}$

$$
\Delta W=\frac{1}{2 \pi i} \int_{c}\left[E_{a}^{0}+z+\Gamma(z)-2 z \Gamma^{\prime}(z)\right] g_{a}(z) d z-E_{a}^{0}
$$

for the spin-degenerate cases we are considering. The contour will be discussed below. Here $g_{a}(z)$ is the fully perturbed adatom Green's function and

$$
\Gamma(z) \equiv \sum_{k}\left|V_{a k}\right|^{2}\left(z-\epsilon_{k}\right)^{-1}, \quad \text { (A11) }
$$

is the so-called one-body self-energy, and the $\epsilon_{k}$'s are the bulk eigenenergies, as in an Anderson analysis. $^{13,22}$ For the surface dimer, $\Gamma(z)$ takes the simple form $V^{2} / z$, with $z \Gamma^{\prime}(z)=-\Gamma(z)$ (which clearly does not hold for longer chains). For the Anderson symmetric case, $E_{a}^{0}=-\frac{1}{2} U$ and $\left\langle n_{a \sigma}\right\rangle=\frac{1}{2}$, so

$$
g_{a}(z)=\frac{z-\Gamma(z)-4 m(z)}{\left[z-\frac{1}{2} U-\Gamma(z)-2 m(z)\right]\left[z+\frac{1}{2} U-\Gamma(z)-2 m(z)\right]-4 m^{2}(z)}.
$$

The function $m(z)$ essentially gives the many-body corrections to the self-energy, i. e., those beyond $\Gamma(z)$. It is the major extension by BS beyond previous approximations $s^{30,31}$ to the Anderson model. It arises as the coefficient of the part of the $2 \times 2$ matrix self-energy that mixes the two atomic $(V=0)$ states of the adatom (i. e., the two eigenstates of the adatom Hamiltonian), onto which BS have projected the field-operator expansion coefficients referring to the adatom, as in the familiar analysis of the Hubbard model. $^{32}$

The lowest-order term in $m(z)$, as in $\Gamma(z)$, is of order $V^{2}$. BS find in fact that $m(z)$ is different in the weak and strong coupling limits. For the Anderson symmetric case, and with the bulk eigenstates symmetrically situated about the Fermi level (i.e., a half-filled symmetric band), we find that the BS parameters $\Delta$ and $\tilde{\Delta}$ vanish, leaving

$$
m(z)=\gamma \Gamma(z), \quad \text { (A13) }
$$

where $\gamma$ is $\frac{1}{2}$ in the weak-coupling limit and 2 in the

strong-coupling regime. Moreover, $\Gamma(z)$ is odd in $z$ for the symmetric bulk band just described. Combining Eqs. (A10)-(A13), we find that the integral we must perform for the dimer is

$$
\frac{1}{2 \pi i} \int_{c} \frac{\left[z^{2}-\frac{1}{2} U z+3 V^{2}\right]\left[z^{2}-(1+4 \gamma) V^{2}\right]}{\left[z^{2}-\frac{1}{2} U z-(1+2 \gamma) V^{2}\right]\left[z^{2}+\frac{1}{2} U z-(1+2 \gamma) V^{2}\right]-4 \gamma^{2} V^{4}} d z. \tag{A14}
$$

The contour is taken along the real axis, and closed by a semicircle at infinity in the upper half plane. Since we are dealing with a finite set of states, there will be discrete poles along the real axis. The prescription for time-ordered Green's functions is to replace $z$ by $z+i \delta \operatorname{sgn} z$. Thus, we enclose only the poles along the negative real axis; i. e., we sum over the occupied states.

The polynomial in the denominator of the integrand for an $N$-atom chain is of order $N^{2}$. For the Anderson-symmetric, half-filled symmetric bulk band, we find particle-hole symmetry which is manifested by the denominator reducing to a polynomial in $z^{2}$ that is order $N$ : All odd-power terms vanish. In general, then, to perform the energy integral we would determine the zeros of the denominator as a function of $z^{2}$, using Newton's method. The $N$ negative square roots of these zeros give the states below the Fermi level. We then divide out a factor of $z+\left(z_{i}^{2}\right)^{1 / 2}$ from the denominator and evaluate the remaining residue at $-\left(z_{i}^{2}\right)^{1 / 2}$.

For the dimer we find then that the quartic in the denominator reduces to a biquadratic. Summing the residues at the two occupied energy'levels, then carrying through a great deal of algebra, we find that the BS expression for the interaction energy of the dimer reduces to

$$
\Delta W_{[2] \mathrm{BS}}=\frac{1}{4} U-\left[\left(\frac{1}{2} U\right)^{2}+4(1+\zeta) V^{2}\right] /\left\{2\left[\left(z_{+}^{2}\right)^{1 / 2}+\left(z_{-}^{2}\right)^{1 / 2}\right]\right\}, \tag{A15}
$$

where $\zeta=(1+4 \gamma)^{1 / 2}$ and the factors under the radicals are the two roots of the quadratic in $z^{2}$ (corresponding to the two signs of the discriminant) in the denominator of Eq. (A14). For purposes of comparison it is convenient ot rewrite Eq. (A15) as

$$
\Delta W_{[2] \mathrm{BS}}=\frac{U}{4}-\left[\left(\frac{U}{4}\right)^{2}+4 V^{2}\right]^{1 / 2}\left[\left(1-\frac{4(2 \gamma+5-3 \zeta) V^{2} U^{2}}{U^{4}+8(2 \gamma+9+\zeta) V^{2} U^{2}+128(2 \gamma+1+\zeta) V^{4}}\right)\right]^{1 / 2}. \tag{A16}
$$

The modification of the exact result is thus cap-sulized by the second square-root factor in Eq. (A15). For the dimer, the strong-coupling limit always applies. Note that if we insert $\gamma=2$ into the modification factor, it vanishes, so that the square root becomes unity and $\Delta W_{[2] \mathrm{BS}}$ becomes exact. If we insert the weak coupling value of $\gamma=\frac{1}{2}$, we find that the binding energy is decreased, but the square-root modification is always less than a $2 \%$ effect. We also observe that the BS modification will change the energy to order $V^{2} / U$ or $U^{2} / V$ at most. Thus, for $V \ll U$ the factor of 8 in Eq. (A9) is replaced by $3+3(1+4 \gamma)^{1 / 2}-2 \gamma$, or $\sim 7.2$ when $\gamma=\frac{1}{2}$. The approximation of only onebody self-energy ${ }^{30,31}(\gamma=0)$ gives a value of 6 , halfway between the exact and the Hartree-Fock values. In the $V \gg U$ limit the factor of $\frac{1}{64}$ is replaced by $\frac{1}{64}$ times $\left[2(1+\gamma)(1+4 \gamma)^{1 / 2}-2-6 \gamma\right] / \gamma^{2}$, this extra factor having the value $\sim 0.784$ rather than unity when $\gamma$ is $\frac{1}{2}$.

*Work supported in part by the National Science Foundation and the Advanced Research Project Agency.
$\dagger$ Permanent address after January 1975: Dept. of Physics and Astronomy, University of Maryland, College Park, Md. 20742.
$^{1}$ T. B. Grimley, Proc. Phys. Soc. Lond. $\underline{72}, 103$ (1958).
$^{2}$ D. M. Newns, Phys. Rev. 178, 1123 (1969).
$^{3}$ R. Haydock, V. Heine, M. J. Kelly, and J. B. Pendry, Phys. Rev. Lett. 29, 868 (1972); R. Haydock, V. Heine, and M. J. Kelly, Solid State Phys. 5, 2845 (1972).
${ }^{4}$ Michael J. Kelly (private communication).
$^{5}$ K. G. Wilson, in *Collective Properties of Physical Systems*, edited by Bengt Lundqvist and Stig Lundqvist, Nobel Symposium 24 (Academic, New York, 1973), p. 68.
$^{6}$ J. Hubbard, Proc. R. Soc. Lond. A 276, 238 (1963).
$^{7}$ L. M. Falicov and Robert A. Harris, J. Chem. Phys. $\underline{51}, 3153$ (1969).
$^{8}$ R. K. Nesbet, J. Chem. Phys. 43, 311 (1965); I. Shavitt, C. F. Bender, A. Pipano, and R. P. Hosteny, J. Comput. Phys. 11, 90 (1973).
$^{9}$ D. Cabib and T. A. Kaplan, Phys. Rev. B $\underline{7}, 2199$ (1973).
$^{10}$ K. H. Heinig and J. Monecke, Phys. Status Solidi B $\underline{49}$, K139, K141 (1972).
$^{11}$ H. S. Shiba and P. Pincus, Phys. Rev. B $\underline{5}, 1966$ (1972).
$^{12}$ G. Blyholder and C. A. Coulson, Trans. Faraday Soc.63, 1782 (1967).
$^{13}$ P. W. Anderson, Phys. Rev. 124, 41 (1961).
$^{14}$ J. R. Schrieffer, *Proceeding of the Enrico Fermi International School of Physics, Course LVIII, Varenna*, 1973 (Academic, New York, to be published).
$^{15}$ Most of this paper also forms part of T. L. Einstein, thesis (University of Pennsylvania, 1973) (unpublished).
$^{16}$ W. Brenig and K. Schönhammer, Z. Phys. 267, 201 (1974).

$^{17}$F. M. Mueller, Phys. Rev. 153, 659 (1967).

$^{18}$J. R. Schrieffer, J. Vac. Sci. Technol. 9, 561 (1972);
T. L. Einstein and J. R. Schrieffer, Phys. Rev. B 7,
3629 (1973).

$^{19}$D. O. Hayward and B. M. Trapnell, *Chemisorption*, 2nd
ed. (Butterworth, London, 1964).

$^{20}$We use a routine written by Paul Soven.

$^{21}$J. Kondo, Solid State Phys. 23, 183 (1969).

$^{22}$J. R. Schrieffer and P. A. Wolff, Phys. Rev. 149, 491
(1966).

$^{23}$T. B. Grimley, J. Vac. Sci. Technol. 8, 31 (1971);
*Molecular Processes on Solid Surfaces*, edited by E.
Drauglis, R. D. Gretz, and R. I. Jaffee (McGraw-Hill,
New York, 1969), p. 299.

$^{24}$B. J. Thorpe, Surf. Sci. 33, 306 (1972).

$^{25}$See, e.g., Kurt Gottfried, *Quantum Mechanics* (Ben-
jamin, New York, 1966), Vol. I.

$^{26}$J. R. Schrieffer and D. C. Mattis, Phys. Rev. 140,
A1412 (1965).

$^{27}$Kenneth G. Wilson (private communication).

$^{28}$*Handbook of Mathematical Functions*, Natl. Bur. Stds.
Appl. Math. Ser. No. 55, edited by Milton Abramowitz
and Irene Stegun (U.S. GPO, Washington, D.C., 1965).
p. 17.

$^{29}$B. Kjöllerström, D. J. Scalapino, and J. R. Schrieffer,
Phys. Rev. 148, 665 (1966).

$^{30}$A. C. Hewson, Phys. Rev. 144, 420 (1966); A. C. Hew-
son and M. J. Zuckermann, Phys. Lett. 20, 219 (1966).

$^{31}$G. Kemeny, Phys. Rev. 150, 459 (1966).

$^{32}$J. Hubbard, Proc. R. Soc. Lond. A 281, 401 (1964).
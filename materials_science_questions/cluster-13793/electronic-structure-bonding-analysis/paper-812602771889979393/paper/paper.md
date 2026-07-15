# Structural stability of silicon in tight-binding models

This content has been downloaded from IOPscience. Please scroll down to see the full text.

1987 J. Phys. C: Solid State Phys. 20 L263

(http://iopscience.iop.org/0022-3719/20/14/001)

View the table of contents for this issue, or go to the journal homepage for more

Download details:

IP Address: 129.78.139.28
This content was downloaded on 07/09/2014 at 20:39

Please note that terms and conditions apply.

# LETTER TO THE EDITOR

# Structural stability of silicon in tight-binding models

A T Paxton†, A P Sutton† and C M M Nex‡

† Department of Metallurgy and Science of Materials, University of Oxford, Oxford OX1 3PH, UK
‡ Cavendish Laboratory, University of Cambridge, Cambridge CB3 0HE, UK

Received 12 February 1987

Abstract. A simple tight-binding Hamiltonian is used in the band model to calculate binding energies of crystal structures in silicon using the recursion method. The use of matrix orthogonal polynomials is described for efficient computation of the symmetry-preserving matrix Green functions. This provides the basis for a proposed rotationally invariant inter-atomic force algorithm.

We are motivated to calculate inter-atomic forces in Si in the tight-binding approximation [1], and apply these to the relaxation of extended defects by molecular statics. In a relaxation algorithm, it is essential that the observed crystal structure is in stable equilibrium and, more evidently, that forces be rotationally invariant. In the recursion method [2] this latter condition has very recently been shown to be violated [3]. As a preliminary to reporting on the atomic and electronic structure of grain boundaries in Si, we consider here those two pre-conditions, beginning with a description of the model.

The total binding energy, $E_{\text{B}}$, in an assembly of $\mathcal{N}$ atoms is written as the sum of an attractive band energy, which is a sum over occupied eigen-energies of the tight-binding Hamiltonian, $\hat{H}$, and a short-ranged repulsive pairwise energy $E_{\text{rep}}$. Thus

$$
E_{\text{B}} = E_{\text{band}} + \frac{1}{2} \sum_{i \neq j}^{\mathcal{N}} \varphi(|\boldsymbol{R}_{j} - \boldsymbol{R}_{i}|) + \text{constant}
$$

where $i$ and $j$ label atomic sites at vector positions $\boldsymbol{R}$. The constant establishes the zero of energy with respect to the free atoms. The band energy is calculated from a small cluster of atoms in real space by Haydock's recursion method [2] using the Slater-Koster Hamiltonian parametrised in [4]. In this Letter, we examine the efficacy of this model in predicting the stability of crystal structures in Si from just a few moments of the density of states. The work therefore has a close connection with the study of structural energies as a function of band filling across the transition-metal series [5], stability of non-metallic elements [6] and binary compounds [7, 8]. Moreover we briefly consider the question of rotational invariance of site-diagonal matrix elements of the Greenian, $\hat{G}(z) = (z - \hat{H})^{-1}$ since

$$
E_{\text{band}} = \sum_{i, \alpha} \int^{E_{\text{F}}} E n_{i \alpha i \alpha}(E) \, \text{d}E
$$

where

$$
n_{i \alpha j \beta}(E)=-(2 / \pi) \operatorname{Im} \lim _{\eta \rightarrow 0^{+}}\langle i \alpha|\hat{G}(E+i \eta)| j \beta\rangle
$$

is a spin-degenerate matrix element of the spectral density operator. When integrated to the Fermi energy, $E_{\mathrm{F}}$, this yields an element of the density matrix [9]. $\alpha$ and $\beta$ label orbitals.

Central to this work is the scaling of the two contributions to the binding energy with atomic volume. In the Chadi-Harrison scheme [4, 10], the two-centre Hamiltonian matrix elements scale with the inverse square of the bond length, $r$, and we follow [11] in constructing a pairwise energy of the form $\varphi(r)=A / r^{4}$ extending to first neighbours only. The parameters of the model are then the four two-centre hopping integrals, $V_{\mathrm{ss} \sigma}$, $V_{\mathrm{sp} \sigma}, V_{\mathrm{pp} \sigma}$ and $V_{\mathrm{pp} \pi}$; two s- and p-site energies, $\varepsilon_{\mathrm{s}}$ and $\varepsilon_{\mathrm{p}}$; and the parameter $A$, which is fitted to guarantee the equilibrium condition of zero pressure at the observed atomic volume of diamond cubic Si. We find that, qualitatively, the results are rather insensitive to choices of the hopping integral parameters, whereas the length scaling laws of the Hamiltonian matrix elements and pair potential are critical in reproducing the structural properties of Si. Furthermore, an important contribution to the binding energy is the degree of s-p mixing among the occupied states since bonding and anti-bonding states are permitted to couple through the Hamiltonian. This effect is clearly seen by writing the band energy as a sum of two terms, the bond energy, $E_{\text {bond }}$, and site energy, $E_{\text {site }}$ [9]:

$$
E_{\text {band }}=E_{\text {bond }}+E_{\text {site }}=\sum_{i, \alpha} \int^{E_{\mathrm{F}}}\left(E-\varepsilon_{\alpha}\right) n_{i \alpha i \alpha}(E) \mathrm{d} E+\mathcal{N} \sum_{\alpha} \varepsilon_{\alpha} N_{\alpha}
$$

where, since all sites, $i$, are equivalent, $N_{\alpha}$ is the occupancy of orbital $\alpha$. In the minimal basis set used here only $N_{\mathrm{p}}$ and $N_{\mathrm{s}}$ contribute to the site energy and their ratio, which we call the s-p mixing is a significant contribution to the binding energy. In the bond orbital model ([10]; for an application of the bond orbital model in the present context, see [12]), the s-p mixing is three since an s electron is promoted into a p state in the free atom and no valence-conduction-band mixing is allowed as the atoms are condensed onto the lattice. Although the Hamiltonian is conveniently represented in an $\mathrm{sp}^{3}$ basis this does not impose $\mathrm{sp}^{3}$ occupancy. At infinite atomic separation, the density of states is

$$
2 \sum_{\alpha} n_{\alpha}(E)=2 \operatorname{Tr} \delta(E-\hat{H})=2 \sum_{\alpha} \delta\left(E-\varepsilon_{\alpha}\right)
$$

that is, a sum of $\delta$-functions. In the $\mathrm{sp}^{3}$ representation, the infinite-volume density of states is therefore $2 \delta\left(E-\varepsilon_{\mathrm{s}}\right)+6 \delta\left(E-\varepsilon_{\mathrm{p}}\right)$, including spin degeneracy. With four electrons in the ground state, $N_{\mathrm{p}} / N_{\mathrm{s}}=1$. As the atoms are brought together onto the diamond lattice, the tendency to $\mathrm{sp}^{3}$ hybridisation and the broadening of the $\delta$-functions into bands causes $N_{\mathrm{p}} / N_{\mathrm{s}}$ to tend to three against the energy penalty incurred by occupying p rather than s states.

It is attractive to calculate the band energy using the recursion method firstly because of its connection with the earlier moments method and associated arguments on struc- tural stability [5, 13], and secondly because of the advantage of working in real space when modelling extended defects. Recently, however [3], it was found that the con- tinued-fraction expansion of the Green function introduced moments into the density of states that did not transform under a coordinate rotation with the same symmetry as the Hamiltonian. In [14] a very clear explanation of this anomaly has been given in terms of matrix moments [15] whose off-diagonal entries were neglected in the conventional,

scalar, recursion method. They show that a correctly transforming matrix Green function exists if the Hamiltonian is expressed in block form and a matrix, or block, recursion algorithm is used. The continued fraction is then written in terms of matrix chain parameters, $\mathbf{A}_i$ and $\mathbf{B}_i$, and the matrix Green function correct to $(2n+1)$ moments is [14-16]

$$
\mathbf{G}(z)=\mathbf{B}_{0}\left[\left(\mathbf{Z}-\mathbf{A}_{0}\right)-\mathbf{B}_{1}\left\{\ldots \mathbf{B}_{n-1}\left[\left(\mathbf{Z}-\mathbf{A}_{n-1}\right)-\mathbf{B}_{n} \mathbf{T}(z) \mathbf{B}_{n}^{\dagger}\right]^{-1} \mathbf{B}_{n-1}^{\dagger} \ldots\right\}^{-1} \mathbf{B}_{1}^{\dagger}\right]^{-1} \mathbf{B}_{0}^{\dagger}
$$

where $\mathbf{Z}=z \mathbf{1}$ and $\mathbf{T}(z)$ represents a terminator having the correct symmetry properties. In order to evaluate $\mathbf{G}$ we have used the matrix orthogonal polynomials of [15] (where the subscript agrees with the degree of the polynomial):

$$
\mathbf{B}_{i+1} \mathbf{P}_{i+1}=\left(\mathbf{Z}-\mathbf{A}_{i}\right) \mathbf{P}_{i}-\mathbf{B}_{i}^{\dagger} \mathbf{P}_{i-1}
$$

$$
\mathbf{B}_{i+1} \mathbf{Q}_{i}=\left(\mathbf{Z}-\mathbf{A}_{i}\right) \mathbf{Q}_{i-1}-\mathbf{B}_{i}^{\dagger} \mathbf{Q}_{i-2}.
$$

By employing the starting conditions and normalisation,

$$
\mathbf{P}_{-1}=\mathbf{0} \quad \mathbf{P}_{0}=\mathbf{B}_{0}^{-1}
$$

$$
\mathbf{Q}_{-1}=\mathbf{0} \quad \mathbf{Q}_{0}=\mathbf{B}_{1}^{-1} \mathbf{B}_{0}^{\dagger}
$$

it follows by induction that

$$
\mathbf{G}(z)=\left(\mathbf{P}_{n}-\mathbf{T} \mathbf{B}_{n}^{\dagger} \mathbf{P}_{n-1}\right)^{-1}\left(\mathbf{Q}_{n-1}-\mathbf{T} \mathbf{B}_{n}^{\dagger} \mathbf{Q}_{n-2}\right).
$$

The dependence on $z$ of the matrix polynomials has been left implicit. (We observe that monic matrix polynomials do not have a useful application in block recursion unlike their counterparts in scalar recursion.)

Under certain circumstances, the matrix chain parameters are diagonal and the scalar recursion method is correct for site-diagonal Greenian matrix elements. This is the case for s orbitals which are invariant under all rotations, and for sets of orbitals that generate identical chain models and are in orthogonal sub-spaces generated by the Hamiltonian. For example p orbitals in cubic point symmetry generate diagonal matrix chain parameters, but d orbitals do not since the $\mathrm{E}$ and $\mathrm{T}_{2}$ orbitals generate different chain models.

For the structural stability study the band edges were computed using a matching scheme [17] from 21 exact scalar moments, so errors due to rotational asymmetry are negligible. These were then used for square-root termination of the matrix continued fraction [16]. The model for all the structures is thus a single band with a volume-dependent band width. Integration is taken into the complex energy plane to account for $\delta$-functions outside the bands introduced by the termination.

The structural properties of Si have been calculated to great accuracy in [18] as a function of atomic volume. Here we expect only to be able to obtain the qualitative trends, but it is interesting to examine the strengths and limitations of the model in this way. The band energy in diamond Si is computed to a few exact moments in the recursion method as a function of atomic volume, $\Omega$, and the results numerically differentiated to obtain the band contribution to the pressure and bulk modulus. The contribution to the pressure from $E_{\text {rep }}$ is $8 A / 3 \Omega_{0} r_{0}^{4}$, where $\Omega_{0}$ and $r_{0}$ are the equilibrium atomic volume and bond length; the bulk modulus is $56 A / 9 \Omega_{0} r_{0}^{4}$. At the observed lattice constant of the diamond structure we find that the cohesive energy is $4.70 \mathrm{eV}$ per atom and the bulk modulus $3.4 \times 10^{11} \mathrm{erg} \mathrm{cm}^{-3}$ using 10 exact moments. (If an inverse-fifth-power repulsive energy is used, we obtain 6.33 and $6.5 \times 10^{11}$ respectively.) These may be compared with the experimental values [19] of 4.64 and $9.88 \times 10^{11}$.

Letter to the Editor

The inverse-square scaling of the Hamiltonian matrix elements would lead to a divergence in the binding energy if extended to infinity. The philosophy of Harrison's method is to truncate the interactions in both $E_{\text{band}}$ and $E_{\text{rep}}$ beyond first neighbours. In the present work, only first-neighbour interactions are non-zero for the diamond, wurtzite and FCC structures. In BCC, second-neighbour interactions are included. White tin has four first neighbours, and two second neighbours with just $6.35\%$ increased bond length; and we have calculated the binding energies by truncating contributions to both $E_{\text{band}}$ and $E_{\text{rep}}$ after first and after second neighbours. We denote these white-tin (4) and white-tin (6) to indicate the coordination in each case.

![](./images/812602771889979393_1.jpg)

Figure 1. The binding energy of silicon, from ten exact moments of the tight-binding density of states, as a function of atomic volume for the crystal structures considered. Numbers in brackets are coordination numbers for the white-tin structure (see the text). The curves are Chebyshev series fitted to the data.

Figure 1 shows the binding energy of Si in the diamond, wurtzite (ideal axial ratio), white-tin (axial ratio 1.5516), FCC and BCC structures as a function of normalised atomic volume, obtained from ten exact moments. In figure 2, we show the binding energy in Si wurtzite as a function of axial ratio at the atomic volume $\Omega_0$. The s-p mixing as a function of volume for three of the structures in figure 1 is shown in figure 3. We find that the structural trends are not significantly altered using just six moments, but that fewer moments are not sufficient to reproduce correctly the cohesive energy.

The curves in figure 1 show the possibility of a pressure-induced phase transformation to the white-tin structure as predicted in [18] and as observed experimentally. Moreover the minimum in the white-tin (4) energy-volume curve corresponds closely to that found in [18] although the energy difference is twice the size in our calculations. The diamond and wurtzite curves are in close agreement although the curvature is smaller in our case,

![](./images/812602771889979393_2.jpg)

Figure 2. The binding energy of silicon in the wurtzite structure as a function of the axial ratio at the equilibrium volume of the diamond structure (ten exact moments). The curve is a Chebyshev series fitted to the data.

![](./images/812602771889979393_3.jpg)

Figure 3. The ratio of p to s orbital occupancy as a function of atomic volume for diamond, FCC and white-tin with an assumed coordination of four (ten exact moments). The curves are Chebyshev series fitted to the data.

as reflected in the bulk modulus. We find an energy difference betwen diamond and wurtzite of 0.02 eV/atom compared with the local density functional result, 0.01 [20]. The axial ratio of wurtzite in our model is 1.633 compared to the experimental value of 1.635 [21] and the local density functional result, 1.65 [18]. The close-packed structures are not well reproduced, although they are sufficiently high in energy at all reasonable volumes not to cause stabilisation of high-coordination-number configurations as found in some recent classical potentials [22]. White-tin (6) unexpectedly gives poorer agree- ment than white-tin (4). This reflects the inability of the model to describe highly coordinated structures without explicitly including the coordination number in the Hamiltonian [23].

Qualitatively, the results for the three fourfold-coordinated structures are in agree- ment with the local density functional calculations in [18]. As pointed out in [18], a local orbital $sp^3$ basis will bias the results towards tetrahedral bonding and the minimal basis may fail to describe correctly the close-packed structures. In using the tight-binding model, other authors have included a term in the binding energy that is linear in the number of bonds [4] or a function of number of bonds and number of atoms in a few- atom cluster [23]. We have omitted this term as a first approximation for simplicity in the model. We have not yet tested this in a situation where Si is under-coordinated.

We have also investigated a second-neighbour model in which first- and second- neighbour two-centre Slater-Koster integrals were fitted to the band structure and scaled exponentially so as to be continuous between the two values. This leads to a much steeper scaling than inverse square, the advantage (particularly in a molecular dynamics calculation) being that there are no 'cut-off' discontinuities in the energy as atoms move into and out of each other's environments. Moreover the repulsive energy was an exponentially damped $1/r$ form. This model, although a 'more realistic' second-neigh- bour calculation, failed to distinguish in the band energy between diamond and wurtzite, and both white-tin and the close-packed structures had lower energy. The inverse-square scaling of the two-centre integrals seems essential in this context.

### Letter to the Editor

Although the inverse-fifth-power repulsive energy reproduces more closely the bulk modulus, the overall effect is to move the fourfold-coordinated structures down in energy by about 1.5 eV per atom, and to shift the energy-volume curves for the close-packed structures to lower volumes so that their minima coincide with the diamond and wurtzite structures: thus at equilibrium volume their energies are separated from diamond by only about 0.5 eV/atom. The inverse-fourth-power scaling of the repulsive energy as proposed in [11] on the grounds that the major contribution to $E_{\text{rep}}$ is due to non-orthogonality of the basis functions seems to be supported by the present work.

All the models indicate the importance of the s-p mixing to the cohesive properties. At equilibrium volume, in the diamond structure we find 1.7 for this mixing whereas in the close-packed structures it is close to 1.1. In the exponential second-neighbour model (which gave good results for the density of states in perfect Si and in defects such as an ideal vacancy where the bond lengths are unaltered) the s-p mixing in diamond Si was 2.1, which may be a more realistic figure considering the strong $\text{sp}^3$ character of the bonding; in the FCC structure, the s-p mixing was 1.0 at $\Omega_0$ and showed a less rapid increase with decreasing atomic volume. The s-p mixing represents the proportion of the cohesive energy contributed by the site energy as opposed to the contribution from the bond energy. Thus in the close-packed structures and to a lesser extent in white-tin, a large proportion of the binding energy comes from the site energy, whereas in diamond and wurtzite the structure is stabilised by the accumulation of bond charge against the energy penalty of s to p promotion. This is clearly seen in the charge-density plots of [18]. In the tight-binding models described here the effect is most markedly seen in the second-neighbour model. Conversely, this effect is absent in the bond orbital model [10]. Therefore, while the bond orbital model is appropriate for the description of $\text{sp}^3$-bonded Si, in cases where the geometry is strongly opposed to $\text{sp}^3$ bonding, the effect of s-p mixing must be accounted for. A more correct treatment of s-p mixing will include the volume dependence of the s-p *splitting*, $\varepsilon_{\text{p}} - \varepsilon_{\text{s}}$, which is neglected in the present model, but which is not insignificant [24].

The block recursion method is easily extended to calculating off-diagonal Greenian matrix elements, by including in the starting set appropriate basis states [25]. The off-diagonal elements are then given by the corresponding off-diagonal elements of the matrix continued fraction. This allows the calculation of atomic forces within the tight-binding model [9] in an arbitrary cluster of atoms. The scheme is now being used to compute the relaxed structures of stacking faults and grain boundaries in Si; the results will be presented in future publications.

We thank J Inoue and Y Ohta for a preprint of their paper, and D G Pettifor and M W Finnis for invaluable comments and advice. ATP is grateful for an SERC studentship. APS acknowledges the support of the Royal Society.

### References

[1] Slater J C and Koster G F 1954 *Phys. Rev.* **94** 1498
[2] Haydock R 1980 *Solid State Phys.* **35** 215 (New York: Academic)
[3] Ohta Y, Finnis M W, Pettifor D G and Sutton A P 1987 unpublished
[4] Chadi D J 1984 *Phys. Rev. B* **29** 785
[5] Ducastelle F and Cyrot-Lackmann F 1970 *J. Phys. Chem. Solids* **31** 1295
[6] Allan G and Lannoo M 1983 *J. Physique* **44** 1355
[7] Pettifor D G and Podloucky R 1986 *J. Phys. C: Solid State Phys.* **19** 315

[8] Majewski J A and Vogl P 1986 *Phys. Rev. Lett.* **57** 1366

[9] Finnis M W 1986 *AERE Report* TP 1196 (London: HMSO)

[10] Harrison W A 1980 *Electronic Structure* (San Francisco: Freeman)

[11] Harrison W A 1983 *Phys. Rev.* B **27** 3592

[12] Sankey O F and Allen R E 1986 *Phys. Rev.* B **33** 7164
Kohyama M, Yamamoto R and Doyama M 1986 *Phys. Status Solidi* b **136** 31

[13] Friedel J 1969 *The Physics of Metals 1. Electrons* ed. J M Ziman (Cambridge: CUP) p 340

[14] Inoue J and Ohta Y 1987 *J. Phys. C: Solid State Phys.* **20** 1947

[15] Graffi S and Grecchi V 1974 *Commun. Math. Phys.* **35** 235

[16] Mostoller M and Kaplan T 1979 *Phys. Rev.* B **19** 552

[17] Nex C M M 1985 *The Recursion Method and its Applications* ed. D G Pettifor and D L Weaire (Berlin:
Springer) p 52

[18] Yin M T and Cohen M L 1982 *Phys. Rev.* B **26** 5668

[19] Kittel C 1971 *Introduction to Solid State Physics* 4th edn (New York: Wiley) pp 96, 143

[20] Chang K J and Cohen M L 1985 *Phys. Rev.* B **31** 7819

[21] Pirouz P, Chaim R and Samuels J 1987 *Izv. Akad. Nauk Ser. Fiz.* to appear

[22] Hamann D R and Biswas R 1986 *AT and T Bell Laboratories Preprint*
Jones R 1986 private communication
Dodson B 1987 *Phys. Rev.* B **35** 2795

[23] Tomanek D and Schluter M A 1986 *Phys. Rev. Lett.* **56** 1055

[24] Robertson J 1983 *Phil. Mag.* B **47** L33

[25] Jones R and Lewis M W 1984 *Phil. Mag.* B **49** 95
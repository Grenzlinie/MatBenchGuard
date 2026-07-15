# The Relaxation of Molecular Crystal Structures Using a Distributed Multipole Electrostatic Model

D. J. WILLOCK and S. L. PRICE*
University College London, Chemistry Department, Christopher Ingold Laboratories,
20 Gordon Street, London, England, WC1H 0AJ

M. LESLIE
Daresbury Laboratory, Daresbury, Warrington, England, WA4 4AD

C. R. A. CATLOW
Davy Faraday Research Laboratory, The Royal Institution, 21 Albemarle Street, London, England,
W1X 4BS

Received 17 May 1993; accepted 8 September 1994

## ABSTRACT

We describe a method for minimizing the lattice energy of molecular crystal structures, using a realistic anisotropic atom-atom model for the intermolecular forces. Molecules are assumed to be rigid, and the structure is described by the center of mass positions and orientational parameters for each molecule in the unit cell, as well as external strain parameters used to optimize the cell geometry. The resulting program uses a distributed multipole description of the electrostatic forces, which consists of sets of atomic multipoles (charge, dipole, quadrupole, etc.) to represent the lone pair, $\pi$ electron density, and other nonspherical features in the atomic charge distribution. Such ab initio based, electrostatic models are essential for describing the orientation dependence of the intermolecular forces, including hydrogen bonding, between polar molecules. Studies on a range of organic crystals containing hydrogen bonds are used to illustrate the use of this new crystal structure relaxation program, DMAREL, and show that it provides a promising new approach to studying the crystal packing of polar molecules. © 1995 by John Wiley & Sons, Inc.

*Author to whom all correspondence should be addressed.

Journal of Computational Chemistry, Vol. 16, No. 5, 628-647 (1995)
© 1995 by John Wiley & Sons, Inc.
CCC 0192-8651 /95 /050628-20

RELAXING MOLECULAR CRYSTALS

### Introduction

The crystal packing of organic molecules affects many physical properties of the solid, such as solubility and bioavailability. Molecules with high nonlinear optical coefficients will form an inactive solid if the crystal structure is centrosymmetric. Thus, a method of predicting molecular crystal structures and the likelihood of polymorphism would provide valuable practical guidance for the development of molecular materials and pharmaceuticals, as well as providing fundamental information about the factors which control crystallisation. There have been consistent reports of success in modeling the crystal structures of hydrocarbons, as reviewed by Kitaigorodsky¹ in his treatise on the atom-atom potential method and its application to crystal structures. However, attempts to extend the isotropic atom-atom potential method to heteroatoms, particularly polar molecules, have only met with limited success.¹ The simple model of intermolecular interactions, assumed by current crystal modeling programs, "gives an approximate description but does not stress adequately many structure-defining interactions."² This conclusion has since been reinforced by the work of Filippini and Gavezzotti, who analyzed a large database of molecules which included some heteroatoms, but no strongly polar or hydrogen bonded molecules, seeking transferable 6-exp potentials.³ More recently they have extended this treatment⁴ to hydrogen-bonded systems, and these potentials are used as a benchmark and starting point for the development of a new approach to modeling hydrogen-bonded molecular crystals, which is developed in this article.

The electrostatic forces are relatively weak for hydrocarbons; and yet for aromatic hydrocarbons, a considerable improvement in the predicted crystal structures can be obtained by including small atomic charges ($q_{\text{C}} = -q_{\text{H}} = 0.153$ e).⁵ However, the electrostatic forces will dominate the lattice energy for polar molecules, particularly if hydrogen bonding interactions occur in the crystal structure. Hence, a realistic model for the electrostatic interaction will be important for any scheme using intermolecular potentials to predict the structures of polar molecules.

The electrostatic forces around a molecule can be accurately calculated from a distributed multipole representation of an *ab initio* wave function of the molecule. This represents the molecular charge distribution by a set of point multipoles (charge, dipole, quadrupole etc.), usually at every atomic site.⁶ These distributed multipoles provide an accurate representation even close to the van der Waals surface of the molecule (excluding penetration effects), because the expansion remains valid at such short distances, unlike a central multipole expansion. The higher atomic multipole moments represent the electrostatic effects of lone pair, $\pi$ electron, and other nonspherical features in the charge distribution. This is crucial to the success of the model in modeling the structures of van der Waals complexes of polar molecules, particularly when hydrogen bonding⁷ or $\pi-\pi$ interactions⁸ are involved, and also for predicting the preferred relative orientation of protein sidechains.⁹ Because molecular crystals also involve molecules in van der Waals contact, the use of distributed multipole electrostatic models is expected to be important for a generally successful approach to predcting crystal structures. Indeed, it has already been established¹⁰ that the lowest energy type of crystal packing for homonuclear diatomics can depend on whether the electrostatic model uses atomic dipoles or quadrupoles to represent the same total quadrupole moment. The anisotropy of the atomic charge distributions has also been shown to be important in determining the crystal structures of organic molecules: Berkovitch-Yellin and Leiserowitz have used experimental atomic multipoles to account for the packing characteristics of amides¹¹ and carboxylic acids,¹² and Williams and Cox¹³ found it necessary to introduce lone pair charge sites to model the crystal structures of a range of nonhydrogen-bonded azahydrocarbons.

Distributed multipole models have been successfully used to develop model potentials for benzene¹⁴ and chlorine¹⁵ by fitting to crystal structures. These potentials are capable of predicting the behavior of both solid and liquid phases at various temperatures. For these two high-symmetry molecules, however, the distributed multipole representation was simple. This article presents the background reasoning and mathematical structure used by the authors in the production of a static lattice minimization code (DMAREL), which allows the application of multipolar electrostatics to a general molecular geometry in an infinite crystal. The code is designed for use in investigations of crystal packing in molecular systems, particularly polar organic molecules, in which the influence of electrostatic interactions is paramount.

The practical utility of the code is then demonstrated by its use in predicting the crystal struc-

---
JOURNAL OF COMPUTATIONAL CHEMISTRY

WILLOCK ET AL.

tures of a diverse range of hydrogen-bonded molecular crystals, using a distributed multipole electrostatic model plus a simple transferable re- pulsion-dispersion model based on literature po- tentials. $^{3}$ The relaxed structures are sufficiently close to the observed structures to demonstrate that the distributed multipole model can provide a good descripton of hydrogen bonding in molecular crystals. This approach is being developed into an intermolecular potential scheme capable of quanti- tatively accounting for the crystal structures of a wide range of molecules, which will be describedin another publication. $^{16}$

## The Model

Unlike existing molecular crystal structuremodeling programs, such as WMIN $^{17}$ and PCK83, $^{18}$  DMAREL is not constrained to minimize within an assumed space group symmetry. Also, in contrast with programs such as THBREL, $^{19}$ which was de signed for ionic solids and thus treats each atom independently, DMAREL uses rigid molecules (or functional groups) to reduce the number of inde- pendent variables. These features require a more general mathematical description of the crystal structure, which is defined here and then applied to optimizing the lattice structure under anisotropic atom-atom intermolecular forces.

## REPRESENTATION OF THE STRUCTURE

The translational symmetry of a crystal lattice implies that any property, $\wp$ of the system is in variant under a translation equivalent to an integer multiple of the lattice period. That is,
$$\wp(\boldsymbol{r})=\mathfrak{P}(\boldsymbol{r}+\boldsymbol{t}) ; \quad \boldsymbol{t}=l \boldsymbol{a}+m \boldsymbol{b}+n \boldsymbol{c} \quad(1)$$
where $l, m, n$ are integers and $a, b, c$ are the smallest linearly independent vectors in their re- spective directions for which eq. (1) applies.

The unit cell, $P$ , can now be defined. $P$ contains all the translationally unique molecules within a parallelepiped whose edges are defined by $a, b$ , and $c$ , the cell vectors. The lattice, $L$ , can be constructed by copying $P$ to all possible points defined by translations such as $t$ .

To optimize a molecular crystal structure, we need to decide on a set of variables, each of which defines a degree of freedom for the system. If the set is complete, these variables can be used as orthogonal axes giving the phase space of the crystal, any point in which gives a unique struc- tural arrangement. Mapping the energy as a func- tion of the variable set leads to a surface in this phase space, a minimum on which can be expected to correspond to a possible crystal structure.

The initial geometry of the structure to be mini- mized can be taken from experimental X-ray or neutron diffraction data. As will be seen later, this approach serves mainly to verify the utility of the model and test the potential parameter set being used, but it can also provide useful information to identify the important atomic interactions in a given structure. For a more predictive approach, the initial geometry can be derived from other codes which generate likely crystal structures based on molecular geometry and common sym- metry operations (for example, see ref. 20). The starting point is then taken as our origin in phase space, and our structural variables need only de- scribe changes of the structure from this origin. We can then search for energy minima and take the phase space coordinates as the movement of the structure required to alter the starting structure to the minimum energy structure. Now we can turn to classical rigid body dynamics to give us the coordinates describing molecular position and ori- entation within the unit cell. For positional coordi- nates, we take the components of the centre of mass vector for each molecule, denoted $r_{I i}$ .

To describe the molecular orientation, we take the three components of a vector, $\Theta$ , which passes through the center of mass. The line of this vector describes an axis of rotation for the molecule, its direction gives the direction a right-handed screw would move on rotating around the axis, and its magnitude is the amount of rotation required. Changes of orientation are brought about by use of a quaternion rotation matrix, which operates on all vectors, $s$ , in the rotating molecule so that
$$\left(\begin{array}{l}
s_{1} \\
s_{2} \\
s_{3}
\end{array}\right)=\left(\begin{array}{ccc}
e_{0}^{2}+e_{1}^{2}-e_{2}^{2}-e_{3}^{2} & 2\left[e_{1} e_{2}-e_{0} e_{3}\right] & 2\left[e_{1} e_{3}+e_{0} e_{2}\right] \\
2\left[e_{1} e_{2}+e_{0} e_{3}\right] & e_{0}^{2}-e_{1}^{2}+e_{2}^{2}-e_{3}^{2} & 2\left[e_{2} e_{3}-e_{0} e_{1}\right] \\
2\left[e_{1} e_{3}-e_{0} e_{2}\right] & 2\left[e_{2} e_{3}+e_{0} e_{1}\right] & e_{0}^{2}-e_{1}^{2}-e_{2}^{2}+e_{3}^{2}
\end{array}\right) \cdot\left(\begin{array}{l}
s_{o 1} \\
s_{o 2} \\
s_{o 3}
\end{array}\right)\qquad(2)$$
where $s_{o}$ is the original vector. The four quater nion elements are linked to the three vector com-

RELAXING MOLECULAR CRYSTALS

ponents via $^{21}$

$$
\begin{aligned}
e_{0} & =\cos \left(\frac{|\Theta|}{2}\right) \\
e_{i} & =\frac{\Theta_{i}}{|\Theta|} \sin \left(\frac{|\Theta|}{2}\right), \quad i=1,2,3
\end{aligned} \quad(3)
$$

We also require external coordinates to describe the geometry of the unit cell. Here we choose to describe changes in the cell dimensions via a symmetric strain matrix, which gives the changes in all vectors in the lattice (including the cell vectors) under a geometric shape change of the unit cell:

$$
\left(\begin{array}{l}
r_{1} \\
r_{2} \\
r_{3}
\end{array}\right)=\left(\begin{array}{l}
r_{o 1} \\
r_{o 2} \\
r_{o 3}
\end{array}\right)+\left(\begin{array}{ccc}
E_{1} & \frac{1}{2} E_{6} & \frac{1}{2} E_{5} \\
\frac{1}{2} E_{6} & E_{2} & \frac{1}{2} E_{4} \\
\frac{1}{2} E_{5} & \frac{1}{2} E_{4} & E_{3}
\end{array}\right) \cdot\left(\begin{array}{l}
r_{o 1} \\
r_{o 2} \\
r_{o 3}
\end{array}\right) \quad(4)
$$

where $r_{o}$ is the vector before the strain matrix is applied and we have followed the common Voigt convention $^{19}$ in defining the matrix elements.

This set of variables gives us six coordinates per molecule in the unit cell and six strain matrix elements with which to describe changes in the crystal structure. Hence for a unit cell containing $N$ molecules, the structure is represented by a point in $6 N+6$ dimensional phase space.

To search for minima in the phase space, we use a modified Newton-Raphson procedure. Here the lattice energy, $U_{x t l}$, is considered as a second-order Taylor expansion in the structural variables, $x_{i}$,

$$
\begin{aligned}
U_{x t l}( & \left.x_{1}+\delta x_{1}, \ldots, x_{i}+\delta x_{i}, \ldots, x_{(6 N+6)}+\delta x_{(6 N+6)}\right) \\
= & U_{x t l}\left(x_{1}, \ldots, x_{i}, \ldots, x_{(6 N+6)}\right) \\
& +\sum_{i=1}^{(6 N+6)} \frac{\partial U_{x t l}}{\partial x_{i}} \delta x_{i} \\
& +\frac{1}{2} \sum_{i=1}^{(6 N+6)} \sum_{j=1}^{(6 N+6)} \delta x_{i} \frac{\partial^{2} U_{x t l}}{\partial x_{i} \partial x_{j}} \delta x_{j}
\end{aligned}
$$

At an energy minimum, the derivative of energy with respect to any element of the set of displacements $\boldsymbol{\delta} \boldsymbol{x}$ must be zero. That is,

$$
\begin{aligned}
\partial^{2} U_{x t l} \frac{\partial U_{x t l}}{\partial \delta x_{k}}= & \frac{\partial U_{x t l}}{\partial x_{k}} \\
& +\frac{1}{2} \sum_{j=1}^{(6 N+6)}\left(\frac{\partial^{2} U_{x t l}}{\partial x_{k} \partial x_{j}}+\frac{\partial^{2} U_{x t l}}{\partial x_{j} \partial x_{k}}\right) \delta x_{j}=0
\end{aligned}
$$

If we now write the second derivative matrix as $\boldsymbol{W}$, we find that

$$
\delta x_{p}=-2 \sum_{i=1}^{(6 N+6)}\left(W+W^{T}\right)_{p i}^{-1} \frac{\partial U_{x t l}}{\partial x_{i}}
$$

which gives the displacement from the current position to the minima. We have chosen to separate explicitly the second derivative matrix and its transpose (indicated by the superscript $T$ ) because in the problems to be discussed these need not be equivalent. Asymmetry in the matrix is introduced by the orientation-orientation second derivatives, as discussed later. Despite this asymmetry in $\boldsymbol{W}$, $\left(\boldsymbol{W}+\boldsymbol{W}^{\mathrm{T}}\right)$ will always be symmetric, and because we have shown that this is the correct matrix to use in the Newton-Raphson minimization, the displacement calculated remains unique for a given set of derivatives.

We calculate the step direction using eq. (7) subject to the constraint

$$
\sum_{p=1}^{3 N} \delta x_{p}=0
$$

where the first $3 N$ degrees of freedom are the center of mass position coordinates (i.e., the net translation of the cell is zero).

Because we have expanded to second order, eq. (7) is exact only for purely quadratic surfaces. Of course, this is not usually the case, but we can assume that the surface is at least locally quadratic and so the vector given by eq. (7) can be used as a search direction allowing an iterative procedure to find the nearest local minimum on the energy surface.

In general, the matrix $\left(\boldsymbol{W}+\boldsymbol{W}^{\mathrm{T}}\right)$ need only be calculated periodically, because updating algorithms for its inverse are available using the combined techniques of Fletcher et al. $^{22}$ and Broyden, ${ }^{23}$ as suggested by Fletcher. ${ }^{24}$ The use of these updating methods also allows a partially complete second-derivative matrix to be employed at the start of the iterative search because the correct matrix will be produced by updating based on the history of the first derivatives. For the results presented in the section titled "Example Application," we used an initial matrix which contained only the position-position and orientation-orientation contributions. The remaining diagonal elements (for strain-strain) were set to unity, and all other elements were set to zero. Subsequent improvement of the second-derivative matrix by the addition of the correct strain-strain elements gave no signifi-

JOURNAL OF COMPUTATIONAL CHEMISTRY

cant change in the minimum energy structures produced, but the rate of convergence was improved. In this article we give expressions for all elements of the second-derivative matrix for the multipole contribution to the lattice energy for completeness, because these will be required for calculating vibrational properties.

In DMAREL, the energy and derivatives are calculated on a pairwise atom-atom interaction basis and then mapped to the effective molecular quantities. The crystal energy is given by

$$
U_{x t l}=\sum_{I \in P} U_{I}=\sum_{I \in P} \sum_{i \in I} u_{i} \tag{9}
$$

so that the crystal energy is simply the sum of the Madelung energies, $U_{I}$, of each molecule in the unit cell, and in turn the molecular Madelung energies are the sum of site contributions, $u_{i}$. The site contributions themselves are calculated under the pairwise additive approximation so that

$$
u_{i}=\sum_{J \in L} \sum_{j \in J} u_{i j}, \quad \text { with } J \neq I \text { when } J \in P \quad (10)
$$

where $u_{i j}$ is the interaction energy of sites $i$ and $j$.

During the calculation of the energy for site $j$ in the unit cell, an equivalent contribution, $u_{j i}$, will occur. We capitalize on this feature by using each calculated interaction energy in both site sums. This reduces the number of calculations required by almost a factor of 2. However, it also introduces the special case of a site interacting with its own image when the energy contribution must be halved to avoid double counting.

In the summation scheme of eqs. (9) and (10), molecule $J$ can theoretically be anywhere in the infinite lattice. In practice, however, a cutoff radius for the summation is chosen by plotting the lattice energy as a function of cutoff and deciding on a reasonable degree of convergence. This whole molecule cutoff is applied to the center of mass separation of the molecular pair, such that pairs within the cutoff have all site-site interactions calculated irrespective of the site-site separation. This summation scheme is applied to all multipolar interactions except charge-charge, charge-dipole, and dipole-dipole interactions. In these latter cases, the sum converges only conditionally, and so an Ewald summation is used based on the technique of W. Smith. $^{25}$

The version of this electrostatic interaction model implemented in DMAREL allows the use of distributed multipole electrostatics at user-defined sites, each of which may contain multipoles up to the hexadecapole level. All multipole-multipole interaction energies which have a radial power dependence of -1 to -5 are summed into $u_{i j}$, as described earlier.

Contributions to $u_{i j}$ also arise from repulsion-dispersion interactions. Within DMAREL, these may be represented by any of several standard isotropic potential forms, such as Buckingham (6-exp), Lennard-Jones (12-6), etc. For these potential types, a direct summation method with a purely site-site distance cutoff is used.

# THE MULTIPOLE CONTRIBUTION TO THE ELECTROSTATIC ENERGY

In a series of articles $^{26-28}$ Stone et al. have described a procedure for representing the electrostatic potential of a molecule using a set of electrostatic multipoles positioned at arbitrary sites within the molecule's van der Waals surface. The multipole moments are calculated in spherical polar coordinates using the form

$$
Q_{l, k}=\int r^{2 l+1} I_{l, k}(\theta, \phi) \rho(r, \theta, \phi) d \tau \quad (11)
$$

where $\rho$ is the molecular charge density, $I_{l k}$ is an irregular solid harmonic, and $(r, \theta, \phi)$ are spherical polar coordinates with respect to an origin at the multipole center. $l$ is the order of the multipole ($l = 0$ for monopoles, 1 for dipoles, 2 for quadrupoles, etc.), and $k$ indexes the components of the multipole with $-l \leq k \leq l$. Equation (11) defines a complex set of multipolar moments. However, from the spherical harmonic property

$$
Q_{l, k}^{*}=(-1)^{k} Q_{l,-k} \tag{12}
$$

Stone defines the real multipolar elements:

$$
\begin{aligned}
Q_{l k_{c}} & =\left(\frac{1}{2}\right)^{1 / 2}\left((-1)^{k} Q_{l k}+Q_{l,-k}\right) \\
i Q_{l k_{s}} & =\left(\frac{1}{2}\right)^{1 / 2}\left((-1)^{k} Q_{l k}-Q_{l,-k}\right)
\end{aligned} \tag{13}
$$

This multipole representation can also be used to describe the electrostatic interaction of a pair of multipole sites belonging to separate molecules, $^{28}$ via the equation

$$
u_{i j}=\sum_{l_{i} l_{j} k_{i} k_{j}}\left[l_{i}, l_{j}\right] R^{-\left(l_{i}+l_{j}+1\right)} Q_{l_{i} k_{i}} Q_{l_{j} k_{j}} S_{l_{i} l_{j}\left(l_{i}+l_{j}\right)}^{k_{i} k_{j}} \quad (14)
$$

with $\left[l_{i}, l_{j}\right]=\left[\left(2 l_{i}+2 l_{j}+1\right) ! /\left(2 l_{i}\right) !\left(2 l_{j}\right) !\right]^{1 / 2}$.

The $S$ function contains information on the relative orientation of the two multipolar centers. This function can be expressed in terms of the separation vector, $R$, between the multipolar centers and the two sets of axes used to define the multipole

RELAXING MOLECULAR CRYSTALS

set for each molecule locally. We will refer to a general local axis vector ($x$, $y$, or $z$) as $w$. The local axis vectors are always of unit length. The use of a local axis system for each molecule allows the multipole parameters to be defined without regard to the molecular orientation in any external frame.

Using this $S$ function approach, the pair interaction energy can be expressed as a function of a set of 16 dot products involving the local axes vectors of each site and the intersite separation vector, so that

$$
u_{i j}=u_{i j}\left((\boldsymbol{R} \cdot \boldsymbol{R}),\left(\boldsymbol{w}_{l} \cdot \boldsymbol{R}\right),\left(\boldsymbol{w}_{J} \cdot \boldsymbol{R}\right),\left(\boldsymbol{w}_{l} \cdot \boldsymbol{w}_{J}\right)\right)
\tag{15}
$$

where vector $w_{I}$ is a general axis in molecule $I$ and $\boldsymbol{R}$ is the intersite separation vector. The multipole moments, $Q_{I k c}$ and $Q_{I k s}$, enter the expressions only as scaling factors and so may be ignored when examining the general functional form.

Equation (15) does not directly relate the multipolar interaction energy to the structural variables we defined earlier. However, we shall show the dependencies of each member of the dot product set on the structural variables, and so eq. (15) should be regarded as a composite function of the structural variables, with the dot product set being intermediate functions. In general, then, we may find the first and second derivatives of the energy with respect to the independent variables using the chain rules

$$
\frac{\partial u}{\partial x_{i}}=\sum_{\phi} \frac{\partial u}{\partial \phi} \frac{\partial \phi}{\partial x_{i}}
\tag{16}
$$

and

$$
\frac{\partial^{2} u}{\partial x_{i} \partial x_{j}}=\sum_{\phi} \frac{\partial u}{\partial \phi} \frac{\partial^{2} \phi}{\partial x_{i} \partial x_{j}}+\sum_{\phi \psi} \frac{\partial \phi}{\partial x_{i}} \frac{\partial^{2} u}{\partial \phi \partial \psi} \frac{\partial \psi}{\partial x_{j}}
\tag{17}
$$

respectively. Here $x_{i}$ represents the $i$th phase space coordinate. $\phi$ and $\psi$ represent the dot product set. The site indexes for the interaction energy have now been dropped for greater clarity. The derivatives of $u$ with respect to the dot products are easily obtained from the energy expressions in Price and Stone.²⁸ To complete the chain rule, we need only determine the derivatives of each dot product with respect to the structural variables. Although there are 16 dot products in our set, they are made up from combinations of only two vector types, the separation vector and the local axis vectors. It is the effect of any operator on the elements of these vectors which results in a dot product derivative. By looking at the vector elements rather than the dot products themselves, we are able to derive the second derivatives in a straightforward and consistent way. This can be seen by writing a general dot product between the vectors $A$ and $B$

$$
\phi=\sum_{i} A_{i} B_{i}
\tag{18}
$$

so that the first and second derivatives of $\phi$ with respect to any structural variable are given by

$$
\frac{\partial \phi}{\partial x_{m}}=\sum_{i}\left(A_{i} \frac{\partial B_{i}}{\partial x_{m}}+B_{i} \frac{\partial A_{i}}{\partial x_{m}}\right)
\tag{19}
$$

and

$$
\begin{aligned}
\frac{\partial^{2} \phi}{\partial x_{m} \partial x_{n}}= & \sum_{i}\left(\frac{\partial A_{i}}{\partial x_{m}} \frac{\partial B_{i}}{\partial x_{n}}+\frac{\partial A_{i}}{\partial x_{n}} \frac{\partial B_{i}}{\partial x_{m}}\right. \\
& \left.+A_{i} \frac{\partial^{2} B_{i}}{\partial x_{m} \partial x_{n}}+B_{i} \frac{\partial^{2} A_{i}}{\partial x_{m} \partial x_{n}}\right) \quad (20)
\end{aligned}
$$

respectively. Hence we need only find the derivatives of two vector types to obtain the derivatives of all 16 dot products. We consider separately the derivatives with respect to position, orientation, and strain for the first derivative and their combinations for the second derivatives.

First, however, we define the differential operators for each class of stuctural observable.

## DIFFERENTIAL OPERATORS FOR VECTOR COMPONENTS

### Positional Derivatives

Because the molecules in our model are considered to be rigid, a displacement of the molecular center of mass causes an equivalent translation of each atom in the molecule that leaves the center of mass to atom vectors unchanged, so that

$$
\frac{\partial r_{K i}}{\partial r_{L j}}=\delta_{K L} \delta_{i j}
\tag{21}
$$

is the only nonzero derivative. All vectors which describe the internal geometry of the molecule-vectors between the center of mass and atom sites and the local axis vectors-are by defi-

JOURNAL OF COMPUTATIONAL CHEMISTRY

WILLOCK ET AL.

nition independent of the center of mass position in the external frame and so have zero derivatives.

A second application of the operator defined in eq. (21) will always give zero, and so there are no second derivatives of the center of mass vector components.

### Orientational Derivatives

When the vector $\Theta$ in the finite rotation matrix, eq. (2), becomes vanishingly small tending to the infinitesimal vector, $d\Theta$, the rotation matrix reduces to

$$
\begin{aligned}
&\left(\begin{array}{ccc}
1 & -d \Theta_{3} & d \Theta_{2} \\
d \Theta_{3} & 1 & -d \Theta_{1} \\
-d \Theta_{2} & d \Theta_{1} & 1
\end{array}\right) \\
&=\left(\begin{array}{ccc}
1 & -d \Theta_{3} & 0 \\
d \Theta_{3} & 1 & 0 \\
0 & 0 & 1
\end{array}\right) \cdot\left(\begin{array}{ccc}
1 & 0 & d \Theta_{2} \\
0 & 1 & 0 \\
-d \Theta_{2} & 0 & 1
\end{array}\right) \\
& \cdot\left(\begin{array}{ccc}
1 & 0 & 0 \\
0 & 1 & -d \Theta_{1} \\
0 & d \Theta_{1} & 1
\end{array}\right)
\end{aligned}
$$

where we have expanded the matrix into a product of three rotations ignoring products of infinitesimals. This expansion indicates that the general infinitesimal rotation can be considered as the product of three rotations around the $z$, $y$, and $x$ axes in the global frame.

The change in vector coordinates when one of these single-axis rotations is applied can be conveniently written using the permutation symbol $\epsilon_{ijk}$ (which takes the value 1 for $i, j, k$, a cyclic permutation of 1,2,3; $-1$ for $i, j, k$, a reversed cyclic permutation of 1,2,3; and is zero otherwise), giving the general differential

$$
\frac{\partial A_{M i}}{\partial \Theta_{N j}}=\delta_{M N} \sum_{k} \epsilon_{i j k} A_{M k}
$$

where $A$ is a general vector which rotates with molecule $M$.

A second application of this rotation operator gives

$$
\frac{\partial^{2} A_{M i}}{\partial \Theta_{L l} \partial \Theta_{N j}}=\delta_{M N} \delta_{L M}\left(\delta_{j l} A_{M i}-\delta_{i l} A_{M j}\right) \quad(24)
$$

where we have made use of the property of the permutation symbol

$$
\sum_{k} \epsilon_{m n k} \epsilon_{i j k}=\delta_{m i} \delta_{n j}-\delta_{m j} \delta_{n i}
$$

As with the positional derivative, it should be remembered that this rotation affects only vectors associated with the rotating molecule. For instance, the axis of rotation always passes through the center of mass of the molecule, resulting in a zero derivative for the center of mass vector.

The second derivative given by eq. (24) is asymmetric in that reversing the order of differentiation changes the elements of $A$ which appear. This leads to asymmetry in the second-derivative matrix and is the reason for taking the sum of the second derivative and its transpose as the matrix used by the minimizer [eq. (7)].

### Strain Derivatives

The derivative of a vector component with respect to a strain coordinate can be found by considering the effect of a general infinitesimal strain on a vector, $v$, in the crystal

$$
v_{i}+d v_{i}=\sum_{j}\left(\delta_{i j}+d E_{i j}\right) v_{j}
$$

where we have temporarily disregarded the symmetry of the strain matrix given in eq. (4). From this, the derivative of the vector element is given by

$$
\frac{\partial v_{k}}{\partial E_{i j}}=\delta_{i k} v_{j}
$$

In this case, only the center of mass vectors and the translation vector, $t$, have nonzero derivatives with respect to strain because the internal geometry of the molecules is fixed. We now reintroduce the strain matrix symmetry to find the derivatives with respect to our six strain structural variables. From eqs. (4) and (27), we have

$$
\begin{aligned}
& \frac{\partial v_{k}}{\partial E_{p}}=\delta_{k p} v_{p} ; \quad p=1,2,3 \\
& \frac{\partial v_{k}}{\partial E_{p}}=\frac{1}{2} \Delta_{p k} v_{j:(p, k)} ; \quad p=4,5,6
\end{aligned}
$$

In the second case, the $\Delta_{p k}$ function is given by

$$
\Delta_{p k}=1-\delta_{p-3, k}
$$

634
VOL. 16, NO. 5

RELAXING MOLECULAR CRYSTALS

and the subscript $j:(p, k)$ indicates that the vector component $j$ is taken from the table

$$
k \begin{array}{r|rrr}
 & p & & \\
 & 4 & 5 & 6 \\
\hline 1 & - & 3 & 2 \\
2 & 3 & - & 1 \\
3 & 2 & 1 & -
\end{array} \tag{30}
$$

indexed with $p$ and $k$. From eq. (4), the vector elements are linear in the strain matrix coefficients, and so there are no second derivatives of vector elements concerning purely strain.

To complete this section on second derivatives, we must consider the mixed derivative terms such as $\partial^{2} A_{i} / \partial r_{K j} \partial \Theta_{L k}$. In this case, the derivatives of vector components are zero irrespective of the vector being considered. This arises from the fact that molecule fixed vectors have derivatives with respect to $\boldsymbol{\Theta}$ but not $\boldsymbol{r}$, and center of mass vectors have $\boldsymbol{r}$ derivatives but zero $\boldsymbol{\Theta}$ derivatives. Hence the first operation in a mixed $\boldsymbol{r} \boldsymbol{\Theta}$ derivative will always yield a quantity which has a zero derivative for the second operation. This argument also holds for $\mathbf{E} \boldsymbol{\Theta}$ mixed derivatives.

$\boldsymbol{r} \mathbf{E}$ derivatives, however, do give nonzero results. This occurs when the vector element being considered is a center of mass vector. Then, applying eq. (21) to eq. (28), we find

$$
\begin{aligned}
& \frac{\partial^{2} r_{K i}}{\partial r_{L q} \partial E_{p}}=\delta_{K L} \delta_{i p} \delta_{q p} ; \quad p=1,2,3 \\
& \frac{\partial^{2} r_{K i}}{\partial r_{L q} \partial E_{p}}=\frac{1}{2} \delta_{K L} \delta_{q j:(p, i)} \Delta_{i p} ; \quad p=4,5,6 \quad(31)
\end{aligned}
$$

We have now laid out the derivatives of vector components with respect to the structural variable types. It should be remembered that although the second derivatives of the vector components are often zero for given pairs of structural variables, this does not mean that the second-derivative matrix of the lattice energy will have corresponding zero elements. Equation (20), relating the vector element and dot product derivatives, contains products of first derivatives, and so a great many more dot product derivatives survive (see Appendixes I and II).

USE OF THE VECTOR DERIVATIVES

These results can now be applied to the general interaction of a pair of sites $m$ and $n$ belonging to separate molecules $I$ and $J$, respectively. Molecule $J$ can be anywhere within our summation cutoff at a lattice translation of $\boldsymbol{t}$ from the unit cell containing molecule $I$. This situation is illustrated in Figure 1.

From Figure 1, the intersite separation vector is a composite vector, so its general component, $R_{i}$, can be written

$$
R_{i}=t_{J i}+r_{J i}+s_{J n i}-r_{I i}-s_{I m i} \tag{32}
$$

where $\boldsymbol{r}_{I}$ is the center of mass coordinate of molecule $I$ in the unit cell, $\boldsymbol{s}_{I m}$ is the vector from the center of mass of molecule $I$ to its $m$ th atomic site, and $J$ subscripted quantities denote the corresponding vector elements for molecule $J$. The center of mass vectors are themselves part of our structural variable set and so give rise to positional derivatives for the separation vector. The site vectors are associated with the internal geometry of the molecule and so give a contribution to the rotation derivatives. The lattice displacement vector is only affected by a change in cell dimensions and so is involved, along with the center of mass vectors, in the strain derivative.

It is interesting to note from eq. (32) that a factor of -1 occurs for the vectors describing molecule $I$ when compared to the equivalent vector for molecule $J$. In the following text, we will often consider a differential with respect to a variable

![](./images/812309173109784576_1.jpg)

FIGURE 1. The geometry of the general site-site interaction. We have used a fictitious two-dimensional crystal for clarity. The cell vectors $\boldsymbol{a}$ and $\boldsymbol{b}$ are drawn as the edges of the unit cell, and cell boundaries are shown with dotted lines and molecular centers of mass with squares. Only a few molecules are represented. The interaction considered is between site $m$ of molecule $I$ and an image of site $n$ in molecule $J$ displaced by a lattice vector $\boldsymbol{t}_{J}=\boldsymbol{a}+\boldsymbol{b}$.

---
JOURNAL OF COMPUTATIONAL CHEMISTRY

describing the general molecule $K$, say, which can be either $I$ or $J$. The function

$$
\{K I\}=(-1)^{\delta(K I)} \tag{33}
$$

will then be of use.

The nonzero first derivatives of $\boldsymbol{R}$ are easily calculated from the results of the preceding section and eq. (32), giving

$$
\begin{aligned}
\frac{\partial R_{i}}{\partial r_{K j}} & =\{K I\} \delta_{i j} \\
\frac{\partial R_{i}}{\partial \Theta_{K j}} & =\{K I\} \sum_{k} \epsilon_{i j k} s_{I m k} \\
\frac{\partial R_{i}}{\partial E_{p}} & =\delta_{p i}\left(t_{I}+r_{I}-r_{I}\right)_{p} ; \quad p=1,2,3 \\
\frac{\partial R_{i}}{\partial \mathbf{E}_{p}} & =\frac{1}{2} \Delta_{p i}\left(t_{I}+r_{I}-r_{I}\right)_{j:(p, i)} ; \quad p=4,5,6
\end{aligned}
\tag{34}
$$

Likewise, the nonzero second derivatives are

$$
\begin{aligned}
\frac{\partial^{2} R_{i}}{\partial \Theta_{K j} \partial \Theta_{K k}} & =\{K I\}\left(\delta_{j k} s_{K i}-\delta_{i j} s_{K k}\right) \\
\frac{\partial^{2} R_{i}}{\partial r_{K q} \partial \mathbf{E}_{p}} & =\{K I\} \delta_{i p} \delta_{p q} ; \quad p=1,2,3 \\
\frac{\partial^{2} R_{i}}{\partial r_{K q} \partial \mathbf{E}_{p}} & =\frac{1}{2}\{K I\} \delta_{q j:(p, i)} \Delta_{p i} ; \quad p=4,5,6
\end{aligned}
\tag{35}
$$

The other vector type occurring in the dot product set is the local molecular axis vector. This is purely associated with the orientation of the molecule in the cell and hence has only $\Theta$ derivatives.

## RELATIONSHIPS BETWEEN DERIVATIVES

In Appendixes I and II, we have used the aforementioned vector component derivatives along with the product rules given in eqs. (19) and (20) to obtain all the nonzero first and second derivatives of the dot product set. It is now possible to use the pairwise summation formulas [eqs. (9) and (10)] to obtain the lattice energy and its derivatives and so search for minima. However, this direct route to the derivatives leads to some redundancy in the derivative formula because, as we shall show, there are relations between the rotational derivatives involving the intersite vector and the position coordinate derivatives. Consider the first-derivative formulae (AI.3) and (AI.4)—that is, those that contain terms arising from the rotational derivative of the separation vector. Each of these will make a contributon to the site-site energy derivative of the form

$$
\begin{aligned}
\frac{\partial u}{\partial(\boldsymbol{A} \cdot \boldsymbol{R})} \frac{\partial(\boldsymbol{A} \cdot \boldsymbol{R})}{\partial \Theta_{K j}} & \\
& =\sum_{i k} \epsilon_{i j k} s_{K m k}\left[\frac{\partial u}{\partial(\boldsymbol{A} \cdot \boldsymbol{R})}\{K I\} A_{i}\right] \quad(36)
\end{aligned}
$$

via the chain rule of eq. (16). Here we have used the permutation symbol property $\epsilon_{i j k}=-\epsilon_{j i k}=$ $-\epsilon_{k j i}=-\epsilon_{i k j}$, swapping any two indexes changes the sign. Comparing the quantity in square brackets to the equivalent general chain rule for positional derivatives,

$$
\frac{\partial u}{\partial(\boldsymbol{A} \cdot \boldsymbol{R})} \frac{\partial(\boldsymbol{A} \cdot \boldsymbol{R})}{\partial r_{K k}}=\frac{\partial u}{\partial(\boldsymbol{A} \cdot \boldsymbol{R})}\{K I\} A_{k} \quad(37)
$$

we arrive at the relation

$$
\frac{\partial u}{\partial(\boldsymbol{A} \cdot \boldsymbol{R})} \frac{\partial(\boldsymbol{A} \cdot \boldsymbol{R})}{\partial \Theta_{K j}}=\sum_{i k} \epsilon_{i j k} s_{K m k} \frac{\partial u}{\partial r_{K i}} \quad(38)
$$

In the special case of $\boldsymbol{A}=\boldsymbol{R}$, a factor of 2 enters both eqs. (36) and (37) because we then have two nonzero terms in the chain rule of eq. (16). However, eq. (38) remains the same.

This result means that we need only calculate the first positional derivatives of the lattice energy, and this will also give us the separation vector contributions to the first rotational derivatives. There are other contributions to this rotation derivative which arise from the local axis system vectors, and these are treated separately by the direct route laid out earlier. It may be expected that a similar interdependence could be found for the second derivatives, and indeed this is the case, as we discuss next.

To find the form of the relationship for the second derivatives, we consider the specific case of the contribution to the rotation-rotation second derivative arising from the $(\boldsymbol{R} \cdot \boldsymbol{R})$, dot product

RELAXING MOLECULAR CRYSTALS

alone. From eq. (20) and Appendixes I and II,

$$
\begin{aligned}
& \left(\frac{\partial^{2} u}{\partial \Theta_{K f} \partial \Theta_{L p}}\right)_{(\boldsymbol{R} \cdot \boldsymbol{R})} \\
& \quad=2\{K I\} \frac{\partial u}{\partial(\boldsymbol{R} \cdot \boldsymbol{R})} \\
& \quad \cdot\left[\delta_{f p} \sum_{t}\left(\{L I\} s_{K t} s_{L t}+\delta_{K L} R_{t} s_{K t}\right)\right. \\
& \left.\quad-\{L I\} s_{L f} s_{K p}-\delta_{K L} s_{K p} R_{f}\right] \\
& \quad+4\{L I\}\{K I\} \frac{\partial^{2} u}{\partial(\boldsymbol{R} \cdot \boldsymbol{R}) \partial(\boldsymbol{R} \cdot \boldsymbol{R})} \\
& \quad \times \sum_{i j k l} \epsilon_{i f j} \epsilon_{k p l} R_{i} R_{k} s_{K j} s_{L l}
\end{aligned}
$$

The position-position derivative chain rule contribution arising purely from the $(\boldsymbol{R} \cdot \boldsymbol{R})$ dot product has the form

$$
\begin{aligned}
& \left(\frac{\partial^{2} u}{\partial r_{K i} \partial r_{L k}}\right)_{(\boldsymbol{R} \cdot \boldsymbol{R})} \\
& \quad=\{K I\}\{L I\}\left[2 \frac{\partial u}{\partial(\boldsymbol{R} \cdot \boldsymbol{R})} \delta_{i k}\right. \\
& \left.\quad+4 \frac{\partial^{2} u}{\partial(\boldsymbol{R} \cdot \boldsymbol{R}) \partial(\boldsymbol{R} \cdot \boldsymbol{R})} R_{i} R_{k}\right] \quad(4
\end{aligned}
$$

A comparison of eqs. (39) and (40) suggests a substitution of

$$
4 \frac{\partial^{2} u}{\partial(\boldsymbol{R} \cdot \boldsymbol{R}) \partial(\boldsymbol{R} \cdot \boldsymbol{R})} R_{i} R_{k}
$$

from the position-position derivative into the rotation-rotation derivative. This gives rise to the extra term

$$
-2\{K I\}\{L I\} \sum_{i j k l} \epsilon_{i f j} \epsilon_{k p l} \frac{\partial u}{\partial(\boldsymbol{R} \cdot \boldsymbol{R})} \delta_{i k} s_{K j} s_{L l} \quad(42)
$$

Now the delta function in this term reduces the $i$ and $k$ sums to a single sum over $i$, say. This results in a repeated index in the $\epsilon_{i f j} \epsilon_{k p l}$ product, so we can further reduce the summations using eq. (25) to arrive at

$$
-2\{K I\}\{L I\} \frac{\partial u}{\partial(\boldsymbol{R} \cdot \boldsymbol{R})}\left[\delta_{f p} \sum_{j} s_{K j} s_{L j}-s_{K p} s_{L f}\right] \quad(43)
$$

which exactly cancels with those terms remaining in eq. (39) that contain products of $s$ vectors. The only other terms in eq. (39) involve products of the separation vector and the site vector, which can be replaced by comparison with the first positional derivative of eq. (37) to yield

$$
\begin{aligned}
& \left(\frac{\partial^{2} u}{\partial \Theta_{K f} \partial \Theta_{L p}}\right)_{(\boldsymbol{R} \cdot \boldsymbol{R})} \\
& =\delta_{K L}\left[\delta_{f p} \sum_{t} s_{K t}\left(\frac{\partial u}{\partial r_{K t}}\right)_{(\boldsymbol{R} \cdot \boldsymbol{R})}-s_{K p}\left(\frac{\partial u}{\partial r_{K f}}\right)_{(\boldsymbol{R} \cdot \boldsymbol{R})}\right] \\
& \quad+\sum_{i j k l} \epsilon_{i f j} \epsilon_{k p l} s_{K f} s_{L l}\left(\frac{\partial^{2} u}{\partial r_{K i} \partial r_{L K}}\right)_{(\boldsymbol{R} \cdot \boldsymbol{R})}
\end{aligned}
$$

There will also be contributions to the position-position derivatives from dot product pairs such as $(\boldsymbol{A} \cdot \boldsymbol{R})(\boldsymbol{B} \cdot \boldsymbol{R})$, where $\boldsymbol{A}$ may be any local axis vector and $\boldsymbol{B}$ can be any local axis vector or the intersite vector. The resulting orientation-orientation contributions from the derivatives of $\boldsymbol{R}$ which have not been accounted for earlier are

$$
\begin{aligned}
\frac{\partial u}{\partial \Theta_{K f} \partial \Theta_{L p}}= & \frac{\partial u}{\partial(\boldsymbol{A} \cdot \boldsymbol{R})} \delta_{K L}\{K I\} \\
& \times\left[\delta_{f p} \sum_{i} A_{i} s_{K i}-A_{f} s_{K p}\right] \\
& +\frac{\partial^{2} u}{\partial(\boldsymbol{A} \cdot \boldsymbol{R}) \partial(\boldsymbol{B} \cdot \boldsymbol{R})}\{K I\}\{L I\} \\
& \times \sum_{i j k l} \epsilon_{i f j} \epsilon_{l p k} s_{K j} s_{L k} A_{i} B_{l}
\end{aligned}
$$

The contribution to the position-position derivatives for the same dot product pair has the form

$$
\frac{\partial^{2} u}{\partial r_{K i} \partial r_{L l}}=\frac{\partial^{2} u}{\partial(\boldsymbol{A} \cdot \boldsymbol{R}) \partial(\boldsymbol{B} \cdot \boldsymbol{R})}\{K I\}\{L I\} A_{i} B_{l} \quad(46)
$$

This can be substituted into the second term of eq. (45). The first two terms are replaced from eq. (38) to give

$$
\begin{aligned}
\frac{\partial^{2} u}{\partial \Theta_{K f} \partial \Theta_{L p}}= & \delta_{K L}\left[\delta_{f p} \sum_{t} s_{K t} \frac{\partial u}{\partial r_{K t}}-s_{K p} \frac{\partial u}{\partial r_{K f}}\right] \\
& +\sum_{i j k l} \epsilon_{i f j} \epsilon_{k p l} s_{K j} s_{L l} \frac{\partial^{2} u}{\partial r_{K i} \partial r_{L k}}
\end{aligned}
$$

which is identical to eq. (44). Hence all contributions to the $\Theta_{K f} \Theta_{L p}$ derivatives which arise purely from derivatives of the $\boldsymbol{R}$ vector can be related to the $r_{K f}$ first and second derivatives by eq. (47). So, by storing the specific site contributions to the

JOURNAL OF COMPUTATIONAL CHEMISTRY

WILLOCK ET AL.

position derivatives, we can reduce the computation required for the orientational derivatives considerably.

Similar arguments can be used for the $R$ derivatives to the $r_{K f} \Theta_{L p}$ derivatives. In this case, we obtain

$$
\frac{\partial^{2} u}{\partial r_{K f} \partial \Theta_{L p}}=\sum_{i k} \epsilon_{i p k} s_{L k} \frac{\partial^{2} u}{\partial r_{K f} \partial r_{L i}} \quad(48)
$$

### Equivalent Molecules

We now consider two special cases of the general interaction which arise from the translational symmetry of the crystal structure. First, for a molecule interacting with its own image in a different cell, the center of mass vectors for both sites will be the same. In this case, the interaction vector reduces to

$$
R_{i}=t_{J i}+s_{I l i}-s_{I m i} \quad(49)
$$

This immediately tells us that there are no center of mass derivatives, which in turn means that the contributions to the $\Theta_{K f}$ derivatives which we have derived in terms of $r_{L p}$ derivatives are also zero.

In the even simpler case in which a site interacts with its own image in another cell, the interaction vector is a simple lattice translation and so only the strain derivatives of $R$ need be considered.

### TESTING OF DERIVATIVES

Two levels of testing were employed to check the implementation of the multipolar energy derivatives presented here. First, the derivatives of the energy with respect to each of the dot product sets were calculated from the analytic equations derived from the expressions in ref. $^{28}$ and compared to numerical values obtained using finite differences. By choosing a dummy data set that contained a limited number of finite multipoles, we were able to test systematically the rather bulky expressions in small sections. The second level of testing checked the chain rules themselves. This involved setting up a version of the code which was able to take a dummy data set and make small changes to one of the structural variables. The resulting change in lattice energy allowed the calculation of the first derivative with respect to that variable by a standard three-point finite difference method. The analytic result could then be compared with this value. Once it was established that the first derivatives were correctly coded, the required second derivatives [eqs. (AII.1) to (AII.7)] were tested using the finite difference method on the first derivative set.

The implementation of these derivatives and the extension of the Ewald summation method were the main innovations which had to be incorporated into the crystal structure relaxation code THBREL $^{19}$ to produce the new program DMAREL.

---

### Example Application

To demonstrate the use and value of the program DMAREL, we consider the importance of the distributed multipole electrostatic model in determining the crystal structures of hydrogen-bonded molecules. A diverse set of ten molecules whose crystal packing involves various $\mathrm{N}-\mathrm{H} \cdots \mathrm{O}$ or $\mathrm{N}-\mathrm{H} \cdots \mathrm{N}$ hydrogen bonds were considered. These molecules include nitro, amino, amide, and carbonyl groups and aromatic five- and six-membered heterocycles, to provide a variety of combinations of functional groups and hydrogen bonds (Table I).

The DMA provides a model for the electrostatic forces between molecules that automatically includes the differences in hybridization, anisotropy, and polarity between the atoms in different bonding environments. The repulsion and dispersion forces also need to be modeled within the crystal structure, and we looked to the molecular crystal structure modeling literature to find estimates of these potentials. The only set of empirical atom-atom potentials which have been fitted to a wide range of crystal structures with diverse functional groups, including C, H, N, and O atoms, were developed by Filippini and Gavezzotti. ${ }^{3}$ These potentials have recently been extended to hydrogen bonding interactions ${ }^{4}$ by the addition of new parameters for the polar hydrogens which are bonded to oxygen or nitrogen. These 6-exp potentials were fitted without any electrostatic term present, and thus the polar hydrogen atom $\left(\mathrm{H}_{\mathrm{p}}\right)$ interaction potentials had steep, deep potential wells, with minima at the separations found in hydrogen bonds. The electrostatic term makes a major attractive contribution to the hydrogen bond energy, and so when the electrostatic term is explicitly represented, the appropriate 6-exp parameters for polar hydrogen interactions will change dramatically. This is illustrated by the comparison of the 6-exp total $\mathrm{O} \cdots \mathrm{H}_{\mathrm{p}}$ potential with an estimate of the $\mathrm{O} \cdots \mathrm{H}_{\mathrm{p}}$ repulsion-dispersion poten-

---

VOL. 16, NO. 5

RELAXING MOLECULAR CRYSTALS

tial (Fig. 2). This latter potential was part of an isotropic atom-atom model fitted to the inter- molecular perturbation theory calculations of the repulsion + dispersion + polarization contribu- tion to the formamide-formaldehyde potential in the hydrogen bonding region. $^{29}$ Thus, the polar hydrogen parameters of the 6-exp model would not be appropriate for modeling the polar hydro- gen interactions in the presence of an electrostatic model, but the C, H, N, and O repulsion-disper- sion parameters should provide a reasonable start- ing point. Hence, the contrast between the two potentials (one with an accurate electrostatic model and the other with no explicit electrostatics), which only differ otherwise in the representation of the hydrogen bonding potentials, provides a test of whether the theoretically well-founded introduc- tion of a realistic electrostatic model is practically justified.

The atom-atom 6-exp potentials are used in the form

$$
U=\frac{\epsilon}{(\lambda-6)}\left[6 \exp (\lambda) \exp \left(-\lambda \frac{R}{R^{0}}\right)-\lambda\left(\frac{R^{0}}{R}\right)^{6}\right]
$$

where $\epsilon$ is the well depth, $R^{0}$ is the minimum energy separation, and $\lambda$ is a steepness parame ter (which is assumed to have the value 13.5 for all interactions $^{3}$ ). The work of Filippini and Gavezzotti $^{3,4}$ provides sets of these parameters for all homo- and heteroatomic interactions involving $C, H, N, O, S, Cl$ , and polar hydrogen atoms $H_{p}$ . These were determined by considering the atom-atom distances in the crystal structures, to give guidance on the $R^{0}$ values, and by fitting to a large database of crystal structures and lattice en- ergies. The resulting potentials were mainly as- sessed by their remarkable ability to predict the lattice energies of the diverse data set. This data set only included urea and formamide of the cur- rent set of hydrogen-bonded crystals and no hy- drogen bonds between different functional groups, unlike the set in Table I. The predicted structures and lattice energies for these compounds, using the potentials and protocol of ref. 4, are given in Table II.

The alternative approach, which requires the use of DMAREL, includes an electrostatic dis- tributed multipole model. This was obtained from a self-consistent field (SCF) wave function of each isolated molecule, using a $6-31 G^{* *}$ basis set $^{30}$ in

<table>
<caption>TABLE I. Data Set of Hydrogen-Bonded Crystals.</caption>
<thead>
<tr>
<th>Molecule name</th>
<th>CSDª[37]</th>
<th>Formula</th>
<th>Symmetry distinct hydrogen bonds present,<br>heavy atom separations (Å)</th>
<th>Space group</th>
</tr>
</thead>
<tbody>
<tr>
<td>Allopurinol</td>
<td>ALOPUR [38]</td>
<td>C₅H₄N₄O</td>
<td>N—Hₚ ··· N, 2.88, 2.88</td>
<td>P2₁/c</td>
</tr>
<tr>
<td>Cytosine</td>
<td>CYTSIN01 [39]</td>
<td>C₄H₅N₃O</td>
<td>N—Hₚ ··· N, 2.84, N—Hₚ ··· O═C, 2.98, 3.03</td>
<td>P2₁2₁2₁</td>
</tr>
<tr>
<td>Urea</td>
<td>UREAXX09 [40]</td>
<td>(NH₂)₂CO</td>
<td>N—Hₚ ··· O═C 2.98, 3.04</td>
<td>P4̅2₁m</td>
</tr>
<tr>
<td>Formamide</td>
<td>FORMAM [41]</td>
<td>HCONH₂</td>
<td>N—Hₚ ··· O═C 2.88, 2.935</td>
<td>P2₁/n</td>
</tr>
<tr>
<td>Aniline</td>
<td>BAZGOY [42]</td>
<td>C₆H₅NH₂</td>
<td>N—Hₚ ··· N 3.18, 3.73</td>
<td>P2₁/c</td>
</tr>
<tr>
<td>Imidazole</td>
<td>IMAZOL13 [43]</td>
<td>C₃H₄N₂</td>
<td>N—Hₚ ··· N 2.86</td>
<td>P2₁/c</td>
</tr>
<tr>
<td>3,5-Diamino-2,4,6-trinitro-benzamide</td>
<td>BICWEP [44]</td>
<td>C₆(NH₂)₂(NO₂)₃CONH₂</td>
<td>N—Hₚ ··· O═C 2.97 N—Hₚ ··· O═N 3.02, 3.17</td>
<td>P2₁/n</td>
</tr>
<tr>
<td>Uric acid</td>
<td>URICAC [45]</td>
<td>C₅H₄N₄O₃</td>
<td>N—Hₚ ··· O═C 2.73, 2.80, 2.81, 2.83</td>
<td>P2₁/a</td>
</tr>
<tr>
<td>1,3,5-Triamino-2,4,6-trinitro-benzene</td>
<td>TATNBZ [46]</td>
<td>C₆(NH₂)₃(NO)₃</td>
<td>N—Hₚ ··· O═N 2.93, 2.93, 2.95, 2.99, 2.99, 3.00</td>
<td>P1̅</td>
</tr>
<tr>
<td>Uracil</td>
<td>URACIL [47]</td>
<td>C₆H₄N₂O₂</td>
<td>N—Hₚ ··· O═C 2.86, 2.87</td>
<td>P2₁/a</td>
</tr>
</tbody>
<tfoot>
<tr>
<td colspan="5">ªReferences in brackets.</td>
</tr>
</tfoot>
</table>

JOURNAL OF COMPUTATIONAL CHEMISTRY

<table>
<caption>TABLE II. Crystal Structure Relaxations Using Empirical 6-exp Potentials.</caption>
<thead>
<tr>
<th rowspan="2">Substance</th>
<th colspan="4">Differences between relaxed and experimental structures<br>$\Delta P = 100\ (P(\text{relaxed}) - P(\text{exp.}))/P(\text{exp.})$</th>
<th colspan="2">Lattice energy$^{\text{a}}$<br>(kJ/mol)</th>
</tr>
<tr>
<td>$\Delta a$ (%)</td>
<td>$\Delta b$ (%)</td>
<td>$\Delta c$ (%)</td>
<td>$\Delta \beta^{\text{b}}$ (%)</td>
<td>$U_{\text{l}}$</td>
<td>$U_{\text{r}}$</td>
</tr>
</thead>
<tbody>
<tr>
<td>Allopurinol</td>
<td>$-5.28$</td>
<td>$0.79$</td>
<td>$0.30$</td>
<td>$-1.47$</td>
<td>$-109.1$</td>
<td>$-118.4$</td>
</tr>
<tr>
<td>Cytosine</td>
<td>$-1.13$</td>
<td>$-1.99$</td>
<td>$-6.63$</td>
<td>—</td>
<td>$-112.6$</td>
<td>$-129.5$</td>
</tr>
<tr>
<td>Urea</td>
<td>$-5.74$</td>
<td>$-5.74$</td>
<td>$-4.79$</td>
<td>—</td>
<td>$-92.1$</td>
<td>$-110.0$</td>
</tr>
<tr>
<td>Formamide</td>
<td>$-13.61$</td>
<td>$2.47$</td>
<td>$-10.53$</td>
<td>$-5.71$</td>
<td>$-65.4$</td>
<td>$-75.7$</td>
</tr>
<tr>
<td>Aniline</td>
<td>$0.40$</td>
<td>$-2.10$</td>
<td>$-2.69$</td>
<td>$-1.05$</td>
<td>$-61.8$</td>
<td>$-63.8$</td>
</tr>
<tr>
<td>Imidazole</td>
<td>$-1.87$</td>
<td>$-4.78$</td>
<td>$2.12$</td>
<td>$5.74$</td>
<td>$-51.4$</td>
<td>$-59.1$</td>
</tr>
<tr>
<td>BICWEP</td>
<td>$-4.88$</td>
<td>$-2.00$</td>
<td>$0.60$</td>
<td>$0.14$</td>
<td>$-181.6$</td>
<td>$-196.9$</td>
</tr>
<tr>
<td>Uric acid</td>
<td>$0.26$</td>
<td>$0.27$</td>
<td>$-0.67$</td>
<td>$-11.49$</td>
<td>$-188.3$</td>
<td>$-198.2$</td>
</tr>
<tr>
<td>TATNBZ</td>
<td>$-2.12$</td>
<td>$-2.13$</td>
<td>$-3.51$</td>
<td>$2.14,\ -0.77,\ -0.12$</td>
<td>$-190.6$</td>
<td>$-203.4$</td>
</tr>
<tr>
<td>Uracil</td>
<td>$4.75$</td>
<td>$-8.47$</td>
<td>$-5.71$</td>
<td>$0.30$</td>
<td>$-108.2$</td>
<td>$-119.3$</td>
</tr>
</tbody>
</table>

The procedures used by Gavezzotti and Filippini were used as far as they were specified in refs. 3 and 4. Thus, the heteroatomic interactions were given as in ref. 4 and not by combining rules. For BICWEP and TATNBZ, the $\text{O}\cdots\text{H}_{\text{p}}$ parameters used were explicitly calibrated for $\text{N}—\text{H}\cdots\text{O=N}$ hydrogen bonds.$^{48}$ An $\text{N}—\text{H}$ bond length of $1.00\ \mathring{\text{A}}$ was used. Lattice energies are calculated at $10\ \mathring{\text{A}}$ cutoff and divided by 0.97. The calculated lattice energies at the experimental structure given in ref. 4 are $-87.9$ kJ/mol for urea and $-65.3$ kJ/mol for formamide, with an error of up to $0.4$ kJ/mol introduced by conversion from kcal/mol.
$^{\text{a}}\text{U}_{\text{l}}$ refers to the experimental geometry, which was used as the starting point, and $\text{U}_{\text{r}}$ to the relaxed geometry.
$^{\text{b}}$The cell angle errors are quoted in the order $\alpha,\ \beta,\ \gamma$ for triclinic structures. None of the crystals changed lattice symmetry on relaxation.

the CADPAC program.$^{31}$ The DMA provided all atomic multipole moments up to hexadecapole at every atomic site. The molecular geometry was taken from the X-ray or neutron structure (Table I), with the intramolecular hydrogen bond lengths standardized to $1.08\ \mathring{\text{A}}$ for $\text{C}—\text{H}$ and $1.01\ \mathring{\text{A}}$ for $\text{N}—\text{H}_{\text{p}}$. The DMA electrostatic model was used in conjunction with the C, H, N, and O homoatomic 6-exp parameters,$^{3}$ imposing the commonly used$^{32}$ combining rules for this form of the potential, namely

$$
\epsilon_{\iota \kappa}=\left(\epsilon_{\iota \iota} \epsilon_{\kappa \kappa}\right)^{1 / 2}, \quad R_{\iota \kappa}^{0}=\frac{1}{2}\left(R_{\iota \iota}^{0}+R_{\kappa \kappa}^{0}\right) \quad(51)
$$

This reduces the number of independent parameters and is appropriate because Filippini and Gavezzotti$^{3}$ attributed the deviation of their heteroatomic $\epsilon$ values from the combining rules to the absorption of the electrostatic contribution. A new set of repulsion-dispersion parameters, which do not absorb the electrostatic contribution, were required for the polar hydrogen atom interactions ($\text{C/N/O}\cdots\text{H}_{\text{p}}$). The nonpolar hydrogen oxygen ($\text{H}\cdots\text{O}$) atom potential is similar to the $\text{O}\cdots\text{H}_{\text{p}}$ repulsion-dispersion estimate derived from perturbation theory calculations, though the repulsive wall is at a larger separation (Fig. 2). Thus, the $R^{0}$ value for the $\text{O}\cdots\text{H}_{\text{p}}$ potential was optimized, starting from the $\text{O}\cdots\text{H}$ value and keeping the well depth fixed at the $\text{O}\cdots\text{H}$ value. The three $R^{0}$ parameters (C, N, and O, with $\text{H}_{\text{p}}$) were simultaneously fitted (with the $\epsilon$ values fixed) by a least-squares method to the symmetry independent first derivatives of the lattice energy at the experimental structures and to the heats of sublimation (where available) of the 10 compounds, using an adapted verson of DMAREL.

The final set of repulsion-dispersion parameters, used in conjunction with the distributed multipole electrostatic model, is shown in Table III. The fitted minimum repulsion-dispersion energy separation $R^{0}$ for the hydrogen bonding contacts between O, N, or C and $\text{H}_{\text{p}}$ are all significantly shorter than the corresponding values for nonpolar hydrogen contacts. This is as expected from the negligible effective hydrogen bond van der Waals radius in the structures of hydrogen-bonded van der Waals complexes. The fitted $\text{O}\cdots\text{H}_{\text{p}}$ repulsion-dispersion potential has a minimum at $R^{0}=2.756\ \mathring{\text{A}}$, in excellent agreement with the value of $2.753\ \mathring{\text{A}}$ obtained by fitting to intermolecular perturbation theory results (IMPT, Fig. 2). There is also good agreement at the shorter $\text{O}\cdots\text{H}_{\text{p}}$ distances sampled in hydrogen bonds, where the repulsion is balanced by the strong electrostatic attraction. The gradient of the fitted $\text{O}\cdots\text{H}_{\text{p}}$ repulsion-dispersion potential at a typical $\text{O}\cdots\text{H}_{\text{p}}$ separation of $2\ \mathring{\text{A}}$ is $-14$ kJ/mol/$\mathring{\text{A}}$, which is much closer to the intermolecular perturbation theory


RELAXING MOLECULAR CRYSTALS

![](./images/812309173109784576_2.jpg)

FIGURE 2. Comparison of oxygen $\cdots$ hydrogen atom-atom potentials. The 6-exp potentials were empirically fitted $^{3,4}$ without any electrostatic forces present, giving a marked difference between the interactions of oxygen and nonpolar hydrogen atoms (O $\cdots$ H 6-exp) and the hydrogen bonding interactions between oxygen and polar hydrogen atoms (O $\cdots$ H$_{\text{p}}$ 6-exp). On this scale, the main difference between the O $\cdots$ H 6-exp potential fitted by Filippini and Gavezzotti$^{3}$ and that given by the combining rules (O $\cdots$ H combining rules) is the separation at which the repulsive interaction becomes important, being greater for the combining rule potential. This latter potential was used to provide $\epsilon$ and a starting point for the $R^{0}$ optimization of the repulsion-dispersion potential used in conjunction with a DMA electrostatic model in this work (O $\cdots$ H$_{\text{p}}$ fitted). The O $\cdots$ H$_{\text{p}}$ IMPT repulsion + dispersion + polarization potential was fitted to IMPT calculations$^{29}$ on the formamide/formaldehyde hydrogen bond.

repulsion-dispersion gradient of $-20$ kJ/mol/$\mathring{\text{A}}$ than it is to the gradient of the starting point O $\cdots$ H potential ($-98$ kJ/mol/$\mathring{\text{A}}$). Thus, although only three parameters have been empirically fitted to describe the hydrogen bonding interactions, the resulting potentials are physically reasonable.

The results of crystal structure relaxations for the DMA-based model potentials, calculated using DMAREL, are given in Table IV. They are contrasted in summary in Table V with the predictions of the empirical 6-exp potentials (details in Table II). The replacement of empirical deep hydrogen bonding potentials with a realistic electrostatic model for each molecule plus empirical, weak hydrogen bonding repulsion-dispersion potentials makes a major difference to the relaxed crystal structures. The empirical total hydrogen bonding potentials reproduce the lattice energies of urea and formamide well, but do less well for the lattice energies involving more complex hydrogen bonding. The relaxed structures show the general overall contraction in cell dimensins reported in ref. 3. Many of the hydrogen bond lengths contract by over 10% with the empirical hydrogen bonding potentials, whereas the electrostatic-based model holds most of the hydrogen bond lengths to within 5%, though in both cases some of the hydrogen bonds expand on relaxation. The minimum energy crystal structures for the DMA-based model potentials are generally much better, with the exceptions of aniline and 1,3,5-triamino-2,4,6-trinitrobenzene, with half this diverse range of structures having relaxed structures within a root mean square (rms) error of 2% of the experimental structure.

The structures which are poorly predicted by the DMA-based model potential are aniline, formamide, and 1,3,5-triamino-2,4,6-trinitrobenzene. In the aniline crystal structure, the amino groups are weakly hydrogen bonded, with N $\cdots$ N distances of $3.18$ $\mathring{\text{A}}$ and $3.37$ $\mathring{\text{A}}$, much longer than the N $\cdots$ N hydrogen bond separation in imidazole of $2.86$ $\mathring{\text{A}}$ (which is more typical of N$-$H $\cdots$ N hydrogen bonds$^{4}$). The phenyl rings are tilted with respect to each other, consistent with the avoidance of stacked sandwich structures shown by benzene and phenylalanine, which can be attributed to the electrostatic effects of the $\pi$ electrons.$^{8,33}$ 1,3,5-triamino-2,4,6-trinitrobenzene is a fully substituted benzene ring with alternating amino and nitro substituents. These molecules form hydrogen bonding sheets in the $a$-$b$ plane, with no interplane hydrogen bonding. It is interesting, then, that the large errors in this structure occur in the $c$-direction and in the $\alpha$ and $\beta$ cell angles, which describe the interlayer separation and the overlaying of molecules in different sheets. Similarly, formamide molecules pack as hydrogen-bonded dimers, with a further hydrogen bond holding the dimers in sheets. Once again, the overlaying of molecules between sheets, which determines the cell angle, is controlled by other interactions. Hence, in these cases the hydrogen bonds are being correctly described within the sheets, but the intersheet separation is dependent on other interactions which have not been considered in the fitting. Because we have not adapted the nonhydrogen-bonding repulsion-dispersion potentials to remove the implicit electrostatic interactions, such as those between $\pi$ systems, it is not surprising that the predictions for these three structures are poor.

Thus, a distributed multipole electrostatic model plus a simple repulsion-dispersion potential can account remarkably well for the hydrogen bonding

JOURNAL OF COMPUTATIONAL CHEMISTRY

WILLOCK ET AL.

<table>
<caption>TABLE III. Repulsion−Dispersion Potential Parameters Used in DMA-Based Model.</caption>
<thead>
<tr>
<th>Interaction</th>
<th>$\epsilon$<br>(kJ/mol)</th>
<th>$R^{0}$<br>(Å)</th>
<th>$\lambda$</th>
</tr>
</thead>
<tbody>
<tr>
<td>C$\cdots$C</td>
<td>0.3875</td>
<td>3.891</td>
<td>13.5</td>
</tr>
<tr>
<td>H$\cdots$H, H$_p$$\cdots$H$_p$</td>
<td>0.0414</td>
<td>3.367</td>
<td>13.5</td>
</tr>
<tr>
<td>N$\cdots$N</td>
<td>0.6260</td>
<td>3.699</td>
<td>13.5</td>
</tr>
<tr>
<td>O$\cdots$O</td>
<td>0.3347</td>
<td>3.610</td>
<td>13.5</td>
</tr>
<tr>
<td>All X$\cdots$Y</td>
<td>$(\epsilon_{XX}\epsilon_{YY})^{1/2}$</td>
<td>$(R_{XX}^{0} + R_{YY}^{0})/2$<br>except (C, N, O)$\cdots$H$_p$ as below</td>
<td>13.5</td>
</tr>
<tr>
<td colspan="4">Parameters fitted to hydrogen-bonded crystal structures.</td>
</tr>
<tr>
<th>Interaction</th>
<th>Initial value of $R^{0}$<br>(Å)</th>
<th>Optimized value $R^{0}$<br>(Å)</th>
<th>Change<br>(%)</th>
</tr>
<tr>
<td>N$\cdots$H$_p$</td>
<td>3.533</td>
<td>2.750</td>
<td>−22.2</td>
</tr>
<tr>
<td>O$\cdots$H$_p$</td>
<td>3.488</td>
<td>2.756</td>
<td>−21.0</td>
</tr>
<tr>
<td>C$\cdots$H$_p$</td>
<td>3.629</td>
<td>3.249</td>
<td>−10.5</td>
</tr>
</tbody>
</table>

in a diverse range of crystal structures. The relaxed structures are remarkably close to the experimental structures, in which the hydrogen bonding is dominant, and provide a promising starting point for the refinement of the repulsion-dispersion potentials, in which stacking between aromatic rings or hydrogen-bonded sheets also influences the crystal packing. This success of an accurate electrostatic model in describing hydrogen-bonded structures within crystals is analogous to its success in predicting the structures of hydrogen-bonded van der Waals complexes.⁷ This is presumably for the same reason—namely, that the electrostatic contribution tends to dominate the orientation dependence of the hydrogen bond.³⁴

The 6-exp potential scheme, with deep empirical potentials to constrain the hydrogen bonds, does provide reasonable estimates of the crystal structures in a cost-effective manner. However, as Gavezzotti and Filippini noted,⁴ these hydrogen bonds lack the directionality that appears to come from the electrostatic interactions, which will be needed for accurate structure predictions. The use of accurate, anisotropic electrostatic models, such as DMAs, allows the detailed electrostatic directionality to be included automatically.

<table>
<caption>TABLE IV. Crystal Structure Relaxations Using DMA-Based Potentials.</caption>
<thead>
<tr>
<th rowspan="2">Substance</th>
<th colspan="4">Differences between relaxed and experimental structures<br>$\Delta P = 100\ (P(\text{relaxed}) - P(\text{exp.}))/P(\text{exp.})$</th>
<th colspan="2">Lattice energy$^{\text{a}}$<br>(kJ/mol)</th>
</tr>
<tr>
<td>$\Delta a$ (%)</td>
<td>$\Delta b$ (%)</td>
<td>$\Delta c$ (%)</td>
<td>$\Delta \beta^{\text{b}}$ (%)</td>
<td>$U_{l}$</td>
<td>$U_{r}$</td>
</tr>
</thead>
<tbody>
<tr>
<td>Allopurinol</td>
<td>−0.47</td>
<td>−1.13</td>
<td>1.45</td>
<td>−1.74</td>
<td>−163.9</td>
<td>−169.6</td>
</tr>
<tr>
<td>Cytosine</td>
<td>−2.13</td>
<td>−0.74</td>
<td>4.01</td>
<td>—</td>
<td>−169.3</td>
<td>−171.4</td>
</tr>
<tr>
<td>Urea</td>
<td>−2.15</td>
<td>−2.15</td>
<td>0.69</td>
<td>—</td>
<td>−106.8</td>
<td>−107.5</td>
</tr>
<tr>
<td>Formamide</td>
<td>2.70</td>
<td>−2.04</td>
<td>−2.83</td>
<td>7.89</td>
<td>−85.0</td>
<td>−88.1</td>
</tr>
<tr>
<td>Aniline</td>
<td>−2.89</td>
<td>7.98</td>
<td>−1.48</td>
<td>1.09</td>
<td>−70.0</td>
<td>−74.3</td>
</tr>
<tr>
<td>Imidazole</td>
<td>1.87</td>
<td>−3.00</td>
<td>0.47</td>
<td>2.15</td>
<td>−87.9</td>
<td>−89.5</td>
</tr>
<tr>
<td>BICWEP</td>
<td>−0.80</td>
<td>−0.50</td>
<td>1.73</td>
<td>−0.91</td>
<td>−199.7</td>
<td>−201.8</td>
</tr>
<tr>
<td>Uric acid</td>
<td>1.09</td>
<td>4.22</td>
<td>−2.46</td>
<td>−1.51</td>
<td>−216.2</td>
<td>−218.3</td>
</tr>
<tr>
<td>TATNBZ</td>
<td>−1.00</td>
<td>−1.04</td>
<td>−5.93</td>
<td>−13.26, −8.34, 0.02</td>
<td>−191.0</td>
<td>−197.5</td>
</tr>
<tr>
<td>Uracil</td>
<td>0.96</td>
<td>1.78</td>
<td>1.28</td>
<td>1.68</td>
<td>−130.5</td>
<td>−133.3</td>
</tr>
<tr>
<td colspan="7">Lattice energies are calculated using a 20 Å cutoff with no scaling. By 20 Å the lattice energies are converged to within 1 kJ/mol.<br>$^{\text{a}}U_{l}$ refers to the experimental geometry, which was used as the starting point, and $U_{r}$ to the relaxed geometry.<br>$^{\text{b}}$The cell angle errors are quoted in the order $\alpha$, $\beta$, $\gamma$ for triclinic structures. None of the crystals changed lattice symmetry on relaxation.</td>
</tr>
</tbody>
</table>

642
VOL. 16, NO. 5

RELAXING MOLECULAR CRYSTALS

TABLE V.
Comparison of Minimum Lattice Energy and Errors in Relaxed Structures for Empirical 6-exp (Refs. 3 and 4)
and DMA-Based Model Potentials.

<table>
  <thead>
    <tr>
      <th rowspan="2">Substance</th>
      <th colspan="2">rmsª % differences between relaxed and experimental structures</th>
      <th colspan="3">Lattice energy for relaxed structure $-U_r$ (kJ/mol)</th>
    </tr>
    <tr>
      <th>Total 6-exp</th>
      <th>DMA based</th>
      <th>Total 6-exp</th>
      <th>DMA based</th>
      <th>$\Delta H_s$ (exp.)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Allopurinol</td>
      <td>2.77</td>
      <td>1.29</td>
      <td>118.4</td>
      <td>169.6</td>
      <td>—</td>
    </tr>
    <tr>
      <td>Cytosine</td>
      <td>4.05</td>
      <td>2.66</td>
      <td>129.5</td>
      <td>171.4</td>
      <td>176.0</td>
    </tr>
    <tr>
      <td>Urea</td>
      <td>5.29</td>
      <td>1.60</td>
      <td>110.0</td>
      <td>107.5</td>
      <td>98.6</td>
    </tr>
    <tr>
      <td>Formamide</td>
      <td>9.15</td>
      <td>4.52</td>
      <td>75.7</td>
      <td>88.1</td>
      <td>71.7</td>
    </tr>
    <tr>
      <td>Aniline</td>
      <td>1.80</td>
      <td>4.34</td>
      <td>63.8</td>
      <td>74.3</td>
      <td>—</td>
    </tr>
    <tr>
      <td>Imidazole</td>
      <td>3.99</td>
      <td>2.08</td>
      <td>59.1</td>
      <td>89.5</td>
      <td>75.4</td>
    </tr>
    <tr>
      <td>BICWEP</td>
      <td>2.65</td>
      <td>1.09</td>
      <td>196.9</td>
      <td>201.8</td>
      <td>—</td>
    </tr>
    <tr>
      <td>Uric acid</td>
      <td>5.76</td>
      <td>2.61</td>
      <td>198.2</td>
      <td>218.3</td>
      <td>—</td>
    </tr>
    <tr>
      <td>TATNBZ</td>
      <td>2.10</td>
      <td>6.86</td>
      <td>203.4</td>
      <td>197.5</td>
      <td>168.2</td>
    </tr>
    <tr>
      <td>Uracil</td>
      <td>5.63</td>
      <td>1.46</td>
      <td>119.3</td>
      <td>133.3</td>
      <td>131.0</td>
    </tr>
  </tbody>
</table>

Experimental heats of sublimation ($\Delta H_s$) taken from ref. 49. Where more than one experimental determination has been made, the most recent or largest was used (see ref. 3).
ªThe rms % error was calculated over the independent cell constants of the experimental structure.

## Conclusions

This article has set out the techniques needed to find energy minima for crystal structures comprised of rigid organic molecules, whose intermolecular interactions are described by realistic, distributed multipole electrostatic models. The approach can be extended to conformationally flexible molecules, by representing them as rigid units interacting by intramolecular potentials, and to other forms of anisotropic atom-atom potentials, such as anisotropic repulsion.³⁵ This theory has been implemented in the crystal structure relaxation program DMAREL, which is proving to be robust and practicable.

DMAREL enables molecular crystal structures to be modeled using accurate, distributed multipole electrostatic models. The sample results in this article show that the introduction of such a model and the physically reasonable introduction of a distinct repulsion-dispersion potential for polar hydrogens produce reasonable structure relaxations for a diverse set of highly hydrogen-bonded crystals. This suggests that an accurate electrostatic model, plus relatively simple transferable repulsion-dispersion potentials, could provide a reliable model for predicting the crystal structures of polar organic molecules. Such a model is currently being developed by the optimization of the repulsion-dispersion parameters by fitting and testing against a larger data set spanning an even wider range of polar organic molecules.¹⁶ Once a reliable potential set for modeling molecular crystal structures is established, DMAREL will be used for predicting the packing of molecules in which the crystal structure is unknown and investigating the problem of polymorphism.

## Acknowledgments

We are indebted to Dr. W. Smith (Daresbury Laboratory) and Drs. A. J. Stone and P. Popelier (Cambridge Universty) for many useful and enlightening discussions, and to Mr. D. S. Coombes (University College London) for data set preparation. The support of the SERC, MOD, and Wellcome Foundation Limited, through collaborative grants, is also gratefully acknowledged.

## Appendix I: List of First Differentials of Dot Products

In this appendix we present an exhaustive list of the nonzero first derivatives of the vector dot product set with respect to the structural observables. These are calculated by using the vector component derivatives given in this article using the chain rule given in eq. (19). For compactness, we again employ the function defined by eq. (33) to give the correct sign to terms arising from derivatives of the $\boldsymbol{R}$ vector as defined in Figure 1.

JOURNAL OF COMPUTATIONAL CHEMISTRY

WILLOCK ET AL.

Nonzero first derivatives with respect to the positional coordinates arise only from dot products containing the separation vector

$$
\begin{aligned}
\frac{\partial(\boldsymbol{R} \cdot \boldsymbol{R})}{\partial r_{K i}} & =\frac{\partial}{\partial r_{K i}} \sum_{j}\left[t_{J j}+r_{J j}+s_{J j}-r_{I j}-s_{I j}\right]^{2} \\
& =2\{K I\} R_{i} \quad \text { (AI.1) }
\end{aligned}
$$

$$
\begin{aligned}
\frac{\partial\left(\boldsymbol{w}_{L} \cdot \boldsymbol{R}\right)}{\partial r_{K i}} & =\frac{\partial}{\partial r_{K i}} \sum_{j} w_{L j}\left[t_{J j}+r_{J j}+s_{J j}-r_{I j}-s_{I j}\right] \\
& =\{K I\} w_{L i} \quad \text { (AI.2) }
\end{aligned}
$$

The complete set of nonzero first $\Theta$ derivatives is summarized next. It is shown in the main text that the parts of these expressions arising from derivatives of the separation vector can be replaced by expressions involving the first center of mass position derivative. The terms involved are eq. (AI.3) and the second term in eq. (AI.4). All other terms arise from the $\Theta$ dependence of the local axis vectors.

$$
\frac{\partial(\boldsymbol{R} \cdot \boldsymbol{R})}{\partial \theta_{K j}}=2\{K I\} \sum_{i k} \epsilon_{i j k} R_{i} s_{K k} \quad \text { (AI.3) }
$$

$$
\begin{aligned}
\frac{\partial\left(\boldsymbol{w}_{L} \cdot \boldsymbol{R}\right)}{\partial \theta_{K j}}=\sum_{i k} \epsilon_{i j k}\left(\delta_{K L} w_{L k} R_{i}+\{K I\} w_{L i} s_{I k}\right) & \\
& \text { (AI.4) }
\end{aligned}
$$

$$
\frac{\partial\left(\boldsymbol{w}_{I} \cdot \boldsymbol{w}_{J}\right)}{\partial \theta_{I j}}=\sum_{i k} \epsilon_{i j k} w_{I k} w_{J i} \quad \text { (AI.5) }
$$

Finally, we consider the strain derivatives of dot products. These have been fully expanded, using the strain drivatives of $\boldsymbol{R}$ given in eq. (34):

$$
\frac{\partial\left(\boldsymbol{w}_{I} \cdot \boldsymbol{w}_{J}\right)}{\partial \theta_{I j}}=\sum_{i k} \epsilon_{i j k} w_{I i} w_{J k} \quad \text { (AI.6) }
$$

$$
\frac{\partial(\boldsymbol{R} \cdot \boldsymbol{R})}{\partial \mathbf{E}_{p}}=2 R_{p}\left(t_{J}+r_{J}-r_{I}\right)_{p} ; \quad p=1,2,3
$$

$$
\begin{aligned}
\frac{\partial(\boldsymbol{R} \cdot \boldsymbol{R})}{\partial \mathbf{E}_{p}}=\sum_{i} \Delta_{p i} R_{i}\left(t_{J}+r_{J}-r_{I}\right)_{j:(p, i)} ; & \text { (AI.7) } \\
& p=4,5,6
\end{aligned}
$$

$$
\frac{\partial\left(\boldsymbol{w}_{K} \cdot \boldsymbol{R}\right)}{\partial \mathbf{E}_{p}}=w_{K p}\left(t_{J}+r_{J}-r_{I}\right)_{p} ; \quad p=1,2,3
$$

$$
\begin{aligned}
\frac{\partial\left(\boldsymbol{w}_{K} \cdot \boldsymbol{R}\right)}{\partial \mathbf{E}_{p}} & =\frac{1}{2} \sum_{i} \Delta_{p i} w_{K i}\left(t_{J}+r_{J}-r_{I}\right)_{j:(p, i)} ; \\
p & =4,5,6 \quad \text { (AI.8) }
\end{aligned}
$$

All other derivatives of the dot product set are zero by virtue of the dependencies of $w_{K}$ and $\boldsymbol{R}$ on the structural variables, as laid out in the main text.

### Appendix II: Second Derivatives of Dot Products

In this appendix we give results obtained using the vector component derivatives to obtain all the nonzero second derivatives of the dot product set. All symbols and functions used here are defined in the main text.

Because the local axis vector has no $r$ derivatives, the only surviving position-position derivative is

$$
\frac{\partial^{2}(\boldsymbol{R} \cdot \boldsymbol{R})}{\partial r_{K f} \partial r_{L p}}=2\{K I\}\{L I\} \delta_{f p} \quad \text { (AII.1) }
$$

The next two equations deal with $\Theta \Theta$ derivatives involving the separation vector. As discussed in the text, parts of the chain rule involving these derivatives are replaced by expressions involving the position first and second derivatives. The terms affected are all of eq. (AII.2) and the third term in eq. (AII.3).

$$
\begin{aligned}
\frac{\partial^{2}(\boldsymbol{R} \cdot \boldsymbol{R})}{\partial \Theta_{K f} \partial \Theta_{L p}} & \\
= & 2\{K I\}\{L I\}\left(\delta_{f p} \sum_{i} s_{K i} s_{L i}-s_{K p} s_{L f}\right) \\
& +2 \delta_{K L}\{K I\}\left(\delta_{f p} \sum_{i} R_{i} s_{K i}-R_{f} s_{K p}\right)
\end{aligned}
$$

$$
\begin{aligned}
& \frac{\partial^{2}\left(\boldsymbol{w}_{M} \cdot \boldsymbol{R}\right)}{\partial \Theta_{K f} \partial \Theta_{L p}} \\
& =\delta_{M K}\{L I\}\left(\delta_{f p} \sum_{i} w_{M i} s_{L k}-w_{M p} s_{L f}\right) \\
& \quad+\delta_{M L}\{K I\}\left(\delta_{f p} \sum_{i} w_{M i} s_{K i}-w_{M f} s_{K p}\right) \\
& \quad+\delta_{M K} \delta_{M L}\left(\delta_{f p} \sum_{i} w_{M i} R_{i}-w_{M p} R_{f}\right) \\
& \quad+\delta_{K L}\{K I\}\left(\delta_{f p} \sum_{i} w_{M i} s_{K i}-w_{M f} s_{K p}\right)
\end{aligned}
$$


RELAXING MOLECULAR CRYSTALS

$$
\begin{aligned}
\frac{\partial^{2}\left(\boldsymbol{w}_{M} \cdot \boldsymbol{w}_{N}\right)}{\partial \Theta_{K f} \partial \Theta_{L p}} & \\
& =\delta_{M K} \delta_{N L}\left(\delta_{f p} \sum_{i} w_{M i} w_{N i}-w_{M p} w_{N f}\right) \\
& +\delta_{M L} \delta_{M K}\left(\delta_{f p} \sum_{i} w_{M i} w_{N i}-w_{M f} w_{N p}\right) \\
& +\delta_{N K} \delta_{N L}\left(\delta_{f p} \sum_{i} w_{M i} w_{N i}-w_{M f} w_{N p}\right) \\
& +\delta_{M K} \delta_{M L}\left(\delta_{f p} \sum_{i} w_{M i} w_{N i}-w_{M p} w_{N f}\right) \\
& \quad \text { (AII.4) }
\end{aligned}
$$

For the second derivative with respect to the strain matrix elements, we again note that center of mass and lattice translation vectors have a linear dependence on the strain elements. Thus, the only nonzero derivatives are

$$
\frac{\partial^{2}(\boldsymbol{R} \cdot \boldsymbol{R})}{\partial E_{p} \partial E_{q}}=2 \delta_{p q}\left(t_{J}+r_{J}-r_{I}\right)_{p}^{2} ; \quad \begin{aligned}
& p=1,2,3 \\
& q=1,2,3
\end{aligned}
$$

$$
\begin{aligned}
\frac{\partial^{2}(\boldsymbol{R} \cdot \boldsymbol{R})}{\partial E_{p} \partial E_{q}}=\Delta_{q p}\left(t_{J}+r_{J}-r_{I}\right)_{p}\left(t_{J}+r_{J}-r_{I}\right)_{j:(q, p)} ; & \\
& \begin{aligned}
& p=1,2,3 \\
& q=4,5,6
\end{aligned}
\end{aligned}
$$

$$
\begin{aligned}
\frac{\partial^{2}(\boldsymbol{R} \cdot \boldsymbol{R})}{\partial E_{p} \partial E_{q}}=\frac{1}{2} \sum_{i} \Delta_{p i} \Delta_{q i}\left(t_{J}+r_{J}-r_{I}\right)_{j:(p, i)} & \\
& \times\left(t_{J}+r_{J}-r_{I}\right)_{l:(q, i)} ; \quad \begin{aligned}
& p=4,5,6 \\
& q=4,5,6
\end{aligned} \\
& \text { (AII.5) }
\end{aligned}
$$

We now list the nonzero mixed variable derivatives.

$$
\frac{\partial^{2}(\boldsymbol{R} \cdot \boldsymbol{R})}{\partial r_{K f} \partial \Theta_{L p}}=2\{K I\}\{L I\} \sum_{i} \epsilon_{f p i} s_{L i} \quad \text { (AII.6) }
$$

$$
\frac{\partial^{2}\left(\boldsymbol{w}_{M} \cdot \boldsymbol{R}\right)}{\partial r_{K f} \partial \Theta_{L p}}=\delta_{M L}\{K I\} \sum_{i} \epsilon_{f p i} w_{M i} \quad \text { (AII.7) }
$$

$$
\begin{aligned}
\frac{\partial^{2}(\boldsymbol{R} \cdot \boldsymbol{R})}{\partial r_{K q} \partial E_{p}}=4\{K I\} \delta_{p q} & \\
& \times\left(t_{J}+r_{J}-r_{I}+\frac{1}{2}\left(s_{J}-s_{I}\right)\right)_{p} ; \\
& p=1,2,3
\end{aligned}
$$

$$
\begin{aligned}
\frac{\partial^{2}(\boldsymbol{R} \cdot \boldsymbol{R})}{\partial r_{K q} \partial E_{p}}=2\{K I\} \Delta_{p q} & \\
& \times\left(t_{J}+r_{J}-r_{I}+\frac{1}{2}\left(s_{J}-s_{I}\right)\right)_{j:(p, q)} ; \\
& p=4,5,6 \quad \text { (AII.8) }
\end{aligned}
$$

$$
\frac{\partial^{2}\left(\boldsymbol{w}_{L} \cdot \boldsymbol{R}\right)}{\partial r_{K q} \partial E_{p}}=\{K I\} \delta_{p q} w_{L p} ; \quad p=1,2,3
$$

$$
\begin{aligned}
\frac{\partial^{2}\left(\boldsymbol{w}_{L} \cdot \boldsymbol{R}\right)}{\partial r_{K q} \partial E_{p}}=\frac{1}{2}\{K I\} \Delta_{p q} w_{L j:(p q)} ; & \\
& p=4,5,6 \\
& \text { (AII.9) }
\end{aligned}
$$

$$
\begin{aligned}
\frac{\partial^{2}(\boldsymbol{R} \cdot \boldsymbol{R})}{\partial \Theta_{K j} \partial E_{p}}=2\{K I\} \sum_{i} \epsilon_{p j l} s_{I m l}\left(t_{J}+r_{J}-r_{I}\right)_{p} ; & \\
& p=1,2,3
\end{aligned}
$$

$$
\begin{aligned}
\frac{\partial^{2}(\boldsymbol{R} \cdot \boldsymbol{R})}{\partial \Theta_{K j} \partial E_{p}}=\{K I\} \sum_{i l} \epsilon_{i j l} s_{I m l} \Delta_{p i}\left(t_{J}+r_{J}-r_{I}\right)_{j:(p, i)} ; & \\
& p=4,5,6 \quad \text { (AII.10) }
\end{aligned}
$$

$$
\begin{aligned}
\frac{\partial^{2}\left(\boldsymbol{w}_{L} \cdot \boldsymbol{R}\right)}{\partial \Theta_{K j} \partial E_{p}}=\delta_{L K} \sum_{k} \epsilon_{p j k} w_{L k}\left(t_{J}+r_{J}-r_{I}\right)_{p} ; & \\
& p=1,2,3
\end{aligned}
$$

$$
\begin{aligned}
\frac{\partial^{2}\left(\boldsymbol{w}_{L} \cdot \boldsymbol{R}\right)}{\partial \Theta_{K j} \partial E_{p}}=\frac{1}{2} \delta_{L K} \sum_{i k} \epsilon_{i j k} \Delta_{p i} w_{L k}\left(t_{J}+r_{J}-r_{I}\right)_{j:(p, i)} ; & \\
& p=4,5,6 \quad \text { (AII.11) }
\end{aligned}
$$

### Appendix III: Comparison with Classical Dynamics

In this appendix we compare the expressions derived in the main text with those in common use for treating the dynamics of rigid bodies. Throughout the main text, we refer to position and rotation derivatives with respect to the center of mass of a molecule arising from individual site-site interactions. These interactions lead to each site having a Madelung energy, $u_{i}$, which is summed into the Madelung energy of the molecule as a whole in eq. (9). In terms of dynamics the force on any site, $\mathbf{f}_{i}$, is given by the usual relation between force and energy gradient,

$$
\begin{aligned}
f_{i \alpha} & =-\frac{\partial u_{i}}{\partial r_{i \alpha}} \\
& =-\frac{\partial u_{i}}{\partial r_{I \alpha}} \text { for rigid molecules (AIII.1) }
\end{aligned}
$$

JOURNAL OF COMPUTATIONAL CHEMISTRY

WILLOCK ET AL.

where $\mathbf{r}_{i}$ refers to the position of the $i$th site and $\mathbf{r}_{I}$ is the position of the $I$th molecule's center of mass with respect to the global origin. We use Greek symbols to indicate the Cartesian component of the vector quantities. It follows that the braced quantity defined in eq. (33) implies that a given site-site interaction must generate equal and op- posite forces on the two molecules involved. For rigid molecules, the total force at the molecules' center of mass, $\mathbf{F}_{I}$, is the sum of these site contribu tions so that

$$
F_{I \alpha}=\sum_{i \in I} f_{i \alpha} \quad \text { (AIII.2) }
$$

We now turn to the molecular torque and its relation to the derivatives presented in the main text. For a rigid system composed of a set of point charges, the torque about the center of mass is given by

$$
T_{I \alpha}=\sum_{i \in I, \beta \gamma} \epsilon_{\alpha \beta \gamma} s_{i \beta} f_{i \gamma} \quad \text { (AIII.3) }
$$

When higher multipoles are introduced, we must also account for the torque arising from the tendency of the atomic multipoles to align along preferred axes. Physically this torque describes the action of local atomic moments due to asymmetry in the charge density. Consider Figure 3, which shows a schematic diagram of the charge distribu- tion associated with a typical atomic site. If the electric field at a position $\mathbf{v}$ relative to the atomic

![](./images/812309173109784576_3.jpg)

FIGURE 3. A schematic illustration of the charge density region $\tau$ associated with a site, $i$, of molecule $I$. In an electric field $E(v)$, this density generates a force at the center of mass, as given by eq. (AIII.4). The contribution to the torque at the center of mass from $i$ is the local torque at $i$ and the torque due to the total force at $i$. The spatial extent of the charge density is lost in a point multipole representation, and the local torque is replaced by torques on the point multipoles.

site is given by the function $E(v)$, then the force acting on the site is

$$
f_{i \alpha}=\int_{p_{i}} E_{\alpha}(\mathbf{v}) \rho(\mathbf{v}) d \tau \quad \text { (AIII.4) }
$$

where the volume integral limit indicates that the integral is over all charge density allocated to the atomic site. The total force at the center of mass is simply the sum of these site terms as before. For the torque, however, we now have the expression

$$
T_{I \alpha}=\sum_{i \in I, \beta \gamma} \epsilon_{\alpha \beta \gamma} \int_{p_{i}} \rho(\mathbf{v})\left(s_{i \beta}+v_{\beta}\right) E_{\gamma}(\mathbf{v}) d \tau \quad(\text { AIII.5) }
$$

which can be split into two contributions:

$$
T_{I \alpha}=\sum_{i \in I, \beta \gamma} \epsilon_{\alpha \beta \gamma}\left(s_{i \beta} f_{i \gamma}+\int_{p_{i}} \rho(\mathbf{v}) v_{\beta} E_{\gamma}(\mathbf{v}) d \tau\right)
$$

The first term is the familiar vector product of distance and force, and it can be seen that this term is directly analogous to eq. (38). The other term is related to those parts of the orientational derivatives which are calculated by the chain rule. These involve derivatives due to the reorientation of the local axis system during rotation (i.e., atom-site derivative), because this second term arises from atom-site torques. The local torque term depends on both the charge distribution around the site and the functional form of the crystal field. The simplest case is an isolated molecule in a uniform field. Here, for a molecule in which each site has no net charge, the total torque reduces to

$$
\sum_{i \in I, \beta \gamma} \epsilon_{\alpha \beta \gamma} E_{\gamma} \int_{p_{i}} \rho(\mathbf{v}) v_{\beta} d \tau=\sum_{\beta \gamma} \epsilon_{\alpha \beta \gamma} \mu_{\beta} E_{\gamma} \quad \text { (AIII.7) }
$$

where $\boldsymbol{\mu}$ is the molecular dipole. For molecules with site charges the same result is obtained, but now both terms in eq. (AIII.6) are active. This is the familiar result that the torque on a molecule in a uniform field is the vector product of its dipole moment with the field strength. For the more com- plex case in which the external field arises from a second multipole set, the equations of Stone and Price $^{8}$ account for the torque correctly (see, for example, ref. 36) because they are expressions for a site-site interaction.


RELAXING MOLECULAR CRYSTALS

# References

1. A. J. Pertsin and A. I. Kitaigorodsky, *The Atom-Atom Potential Method*, Springer-Verlag, Berlin, 1987.

2. G. R. Desiraju, *Crystal Engineering: The Design of Organic Solids*, Elsevier, Amsterdam, 1989, p. 56.

3. G. Filippini and A. Gavezzotti, *Acta Cryst.*, **B49**, 868 (1993).

4. A. Gavezzotti and G. Filippini, *J. Phys. Chem.*, **98**, 4831 (1994).

5. D. E. Williams and T. L. Starr, *Comp. Chem.*, **1**, 173 (1977).

6. A. J. Stone and M. Alderton, *Molec. Phys.*, **56**, 1047 (1984).

7. A. D. Buckingham and P. W. Fowler, *Canad. J. Chem.*, **63**, 2018 (1985).

8. S. L. Price and A. J. Stone, *J. Chem. Phys.*, **86**, 2859 (1987).

9. J. B. O. Mitchell, C. L. Nandi, J. M. Thornton, S. L. Price, J. Singh, and M. Snarey, *J. Chem. Soc. Farad. Trans.*, **89**, 2619 (1993).

10. S. L. Price, *Molec. Phys.*, **62**, 45 (1987).

11. Z. Berkovitch-Yellin and L. Leiserowitz, *J. Am. Chem. Soc.*, **102**, 7677 (1980).

12. Z. Berkovitch-Yellin and L. Leiserowitz, *J. Am. Chem. Soc.*, **104**, 4052 (1982).

13. D. E. Williams and S. R. Cox, *Acta Cryst.*, **B40**, 404 (1984).

14. S. Yashonath, S. L. Price, and I. R. McDonald, *Molec. Phys.*, **64**, 361 (1988).

15. R. J. Wheatley and S. L. Price, *Molec. Phys.*, **71**, 1381 (1990).

16. D. J. Willock, D. S. Coombes, S. L. Price, M. Leslie, and C. R. A. Catlow, in preparation.

17. W. R. Busing, *Oak Ridge National Laboratory Report* (ORNL-5747), 1981.

18. D. E. Williams, *PCK83, QCPE Program 548*, Quantum Chemistry Program Exchange, Chemistry Department, Indiana University, Bloomington, IN, 1983.

19. C. R. A. Catlow and M. J. Norjett, *Internal Report*, AERE Harwell, 1976.

20. A. Gavezzotti, *J. Am. Chem. Soc.*, **113**, 4622 (1991).

21. H. Goldstein, *Classical Mechanics*, Addison-Wesley, Reading, MA, 1980, p. 164.

22. R. Fletcher and M. J. D. Powell, *Computer J.*, **6**, 16 (1963).

23. C. G. Broyden, *J. Inst. Maths. Applns.*, **6**, 66 and 222 (1970).

24. R. Fletcher, *Computer J.*, **13**, 317 (1970).

25. W. Smith, *The Program MDMULP, CCP5 Program Library*, Daresbury Laboratory, 1982.

26. A. J. Stone, *Chem. Phys. Lett.*, **83**, 233 (1981).

27. A. J. Stone and M. Alderton, *Molec. Phys.*, **56**, 1047 (1984).

28. S. L. Price, A. J. Stone, and M. Alderton, *Molec. Phys.*, **52**, 987 (1984).

29. J. B. O. Mitchell and S. L. Price, *J. Comp. Chem.*, **11**, 1217 (1990).

30. P. C. Hariharan and J. A. Pople, *Theor. Chim. Acta*, **28**, 213 (1973).

31. CADPAC5: *The Cambridge Analytic Derivatives Package Issue 5*, a suite of quantum chemistry programs developed by R. D. Amos with contributions from I. L. Alberts, J. S. Andrews, S. M. Colwell, N. C. Handy, D. Jayatilaka, P. J. Knowles, R. Kobayashi, N. Koga, K. E. Laidig, P. E. Maslen, C. W. Murray, J. E. Rice, J. Sanz, E. D. Simandiras, A. J. Stone, and M.-D. Su, Cambridge University, 1992.

32. K. Mirsky, *Acta Cryst.*, **A32**, 199 (1976).

33. A. C. Hunter, J. Singh, and J. M. Thornton, *J. Mol. Biol.*, **218**, 837 (1991).

34. G. J. B. Hurst, P. W. Fowler, A. J. Stone, and A. D. Buckingham, *Int. J. Quant. Chem.*, **29**, 1223 (1986).

35. P. L. A. Popelier and A. J. Stone, *Molec. Phys.*, **82**, 411 (1994).

36. A. J. Stone and R. J. A. Tough, *Chem. Phys. Lett.*, **110**, 123 (1984).

37. F. H. Allen, J. E. Davies, J. J. Galloy, O. Johnson, O. Kennard, C. F. Macrae, and E. M. Mitchell, *J. Chem. Inf. Comp. Sci.*, **31**, 187 (1991).

38. P. Prusiner and M. Sundaralingham, *Acta Cryst.*, **B28**, 2148 (1972).

39. R. J. McClure and B. M. Craven, *Acta Cryst.*, **B29**, 1234 (1973).

40. H. Guth, G. Heger, S. Klein, W. Treutmann, and C. Scheringer, *Z. Krist.*, **153**, 237 (1980).

41. J. Ladell and B. Post, *Acta Cryst.*, **7**, 559 (1954).

42. M. Fukuyo, K. Hirotsu, and T. Higuchi, *Acta Cryst.*, **B38**, 640 (1982).

43. B. M. Craven, R. K. McMullan, J. D. Bell, and H. C. Freeman, *Acta Cryst.*, **B33**, 2585 (1977).

44. H. L. Ammon and S. K. Bhattacharjee, *Acta Cryst.*, **B38**, 2083 (1982).

45. H. Ringertz, *Acta Cryst.*, **20**, 397 (1966).

46. H. H. Cady and A. C. Larson, *Acta Cryst.*, **18**, 485 (1965).

47. R. F. Stewart, *Acta Cryst.*, **23**, 1102 (1967).

48. G. Filippini and A. Gavezzotti, *Chem. Phys. Lett.*, submitted.

49. J. S. Chickos, In *Molecular Structure and Energetics*, Vol. 2, J. F. Liebman and A. Greenberg, Eds., VCH, New York, 1987, p. 67.

---

JOURNAL OF COMPUTATIONAL CHEMISTRY
647
# A MODEL FOR THE CARBON ACTIVITY IN NONSTOICHIOMETRIC THORIUM CARBIDE *

G.E. MURCH and R.J. THORN

Chemistry Division, Argonne National Laboratory, Argonne, IL 60439, USA

Received 1 November 1978

The Rees formulation of nonstoichiometry is adopted together with a vacancy/single carbon atom/$\text{C}_2$ group model to calculate the hitherto largely unknown carbon activity in $\text{ThC}_x$ for $0.0 \lesssim x \lesssim 2.0$. The form of the carbon activity isotherms from $\text{ThC}_{0.9}$ to $\text{ThC}_{1.95}$ closely resembles the experimentally determined isotherms in the U/C system. Based on the occupation of two kinds of sites, the present formalism also generates an asymmetric shape of the miscibility gap between ThC and $\text{ThC}_2$ as found in both the real Th/C and U/C systems.

## 1. Introduction

There is considerable interest in thorium carbide as the fertile component of carbide-based fuel in breeder reactor systems. With this interest has come the need to have available comprehensive data on the thermodynamic and transport properties of $\text{ThC}_x(0.0 \leq x \leq$ 2.0). Of particular importance is information on the activity of carbon over wide ranges of composition and temperature. Such information is necessary for predicting not only the solid state chemistry of additives and fission products but also the possible carbon embrittlement of the cladding material.

There have been no direct measurements of the carbon activity in $\text{ThC}_x$. There have, however, been several EMF studies at low temperatures (1000 to $1223 \text{ K}$) and at compositions $\text{ThC}_{0.75}$ to $\text{ThC}_{0.95}$ [1, 2]. Such measurements give the thorium activities directly; the carbon activities may then be determined using the Gibbs-Duhem relation. However, the results of the two EMF studies are in serious disagreement and seem to be somewhat incompatible with the integral thermodynamic quantities [3].

In view of the extremely limited and conflicting experimental data we have formulated a statistical mechanical model to gain access to the carbon activity as a function of composition (from Th to $\text{ThC}_2$) and temperature (from 1173 to $2573 \text{ K}$).

## 2. Theory

It is now generally accepted that carbon forms a solid solution with thorium over an extensive composition and temperature range. Indeed, since the miscibility gaps between carbon saturated thorium and $\text{ThC}_{0.75}$ as well as between ThC and $\text{ThC}_2$ are both closed at high temperature it is possible to pass from Th to $\text{ThC}_2$ wholly within a single phase region [4]. At small carbon compositions, carbon is present essentially as single carbon atoms which occupy the octahedral interstices of the fcc lattice of thorium. As higher compositions are reached some introduced carbon atoms link with existing carbon atoms to form "$\text{C}_2$" groups. But these di-interstitials still occupy the octahedral interstices. When all possible sites are filled the composition corresponding to $\text{ThC}_2$, or very nearly, is attained. This situation suggests a statistical treatment originally formulated by Rees [5] and applied to the Zr/H system [6].

Carbon dissolution in thorium is considered in terms of a one component lattice gas of carbon atoms distributed over two types of sites. The number of sites of the second type accessible for occupation by carbon atoms depends on the number of sites of the first type already occupied by carbon atoms. An example will impact this fundamental assumption in the model. Let there be $N$ sites of the first type. The first carbon atom can therefore be placed in the lattice at any one of these $N$ sites. The second carbon atom

* Work performed under the auspices of the Division of Basic Energy Science of the US Department of Energy.

G.E. Murch, R.J. Thorn / C activity in $ThC_x$

can be placed at any one of the remaining $N-1$ sites as well as a new site immediately neighboring to the first carbon atom. This "created" site is a site of the second type. If in fact the second carbon atom were to be placed at this site a $C_2$ group would form.

It is considered that the second type of site is at a higher potential energy than a site of the first type. We also consider interactions between neighboring atoms on the first type of site as well as interactions between neighboring atoms on the second type of site. The statistical problem then involves the partitioning of the carbon atoms between the two types of site subject to the above conditions.

We consider a lattice gas consisting of $N_1$ indistinguishable carbon atoms distributed over $N$ sites of the first kind and $N_2$ indistinguishable carbon atoms distributed over $N_1$ sites of the second kind. We define $E_{11}$ as the interaction energy between nearest neighbor atoms on sites of the first type. Similarly, $E_{22}$ is the interaction energy between nearest neighbor atoms on sites of the second type ($E_{22}$ is identical to the interaction energy "$\epsilon_{cc}$" as defined in our thermodynamic study of $UC_x$ $1.0 < x < 2.0$ [7]). We define $E_1$ as the energy required to place a carbon atom, from infinity, on a site of the first kind. Similarly, $E_2$ is the energy required to place a carbon atom, from infinity, onto a site of the second kind *. Both sites just designated are considered in an isolated sense i.e., free from interaction effects with other carbon atoms.

In our treatment, we make use of the zeroth or Bragg-Williams approximation wherein the configurational degeneracy and the average nearest neighbor interaction energies are both treated on the basis of a completely random distribution of carbon atoms over the sites within a given site type. We write for the partition function in the petit canonical ensemble:

$$
\begin{aligned}
Q(N_1, N_2, N, T) &= \frac{N! q_1^{N_1} N_1! q_2^{N_2}}{N_1!(N - N_1)! N_2!(N_1 - N_2)!} \\
&\times \exp\left\{-\beta\left[N_1 E_1 + N_2 E_2 + \bar{N}_{11} E_{11} + \bar{N}_{22} E_{22}\right]\right\},
\end{aligned}
\tag{1}
$$

where $q_1$ and $q_2$ are the vibrational partition functions for a single carbon atom on a site of type 1 or 2, respectively. $\bar{N}_{11} E_{11}$ is the average interaction energy for carbon atoms on sites of type 1. On the basis of a random distribution, $\bar{N}_{11}=cN_1^2/2N$, where $c$ is the coordination number (12). Similarly, $\bar{N}_{22}=cN_2^2/2N_1$.

Making use of Stirling's approximation we write for the free energy, $F$:

$$
\begin{aligned}
-\beta F &= \ln Q \approx N \ln N - (N - N_1) \ln(N - N_1) \\
&+ N_1 \ln q_1 - N_2 \ln N_2 - (N_1 - N_2) \ln(N_1 - N_2) \\
&+ N_2 \ln q_2 - \beta N_1 E_1 - \beta N_2 E_2 \\
&- \frac{\beta c N_1^2 E_{11}}{2N} - \frac{\beta c N_2^2 E_{22}}{2N_1}.
\end{aligned}
\tag{2}
$$

The chemical potential of carbon atoms on sites of type 1 is given by:

$$
\mu_1 = \left(\frac{\partial F}{\partial N_1}\right)_{N_2, N, T},
\tag{3}
$$

and similarly:

$$
\mu_2 = \left(\frac{\partial F}{\partial N_2}\right)_{N_1, N, T}.
\tag{4}
$$

Making use of eq. (2) in eq. (3) we write for $\mu_1$:

$$
\begin{aligned}
\mu_1 &= -\beta^{-1} \left[\ln\left(\frac{N - N_1}{N_1}\right) + \ln\left(\frac{N_1}{N_1 - N_2}\right) + c\beta\left(\frac{N_2}{N_1}\right)^2 E_{22}\right. \\
&\left.+ \ln q_1 - \beta E_1 - \frac{c\beta N_1 E_{11}}{N_1}\right].
\end{aligned}
\tag{5}
$$

Eq. (5) may be further simplified since [5]:

$$
\ln\left(\frac{N_1 - N_2}{N_1}\right) \approx \frac{c\beta}{2}\left(\frac{N_2}{N_1}\right)^2 E_{22},
\tag{6}
$$

for small values of $N_2/N_1$ and $1 < \frac{1}{2}c\beta E_{22} < 4$ which are conditions appropriate here. It is noted that $N_1/N$ is close to unity before $N_2/N_1$ becomes appreciable and that the "$\mu_1$" isotherm contributes but little to the total isotherm for $x > 1.2$. Eq. (5) reduces to:

$$
\mu_1 = -\beta^{-1} \left[\ln\left(\frac{N - N_1}{N_1}\right) + \ln q_1 - \beta E_1 - \frac{c\beta N_1 E_{11}}{N}\right].
\tag{7}
$$

Substituting eq. (2) into eq. (4) we also write for $\mu_2$:

$$
\mu_2 = -\beta^{-1} \left[\ln\left(\frac{N_1 - N_2}{N_2}\right) + \ln q_2 - \beta E_2 - \frac{c\beta N_2 E_{22}}{N_1}\right].
\tag{8}
$$

* In actual fact, both carbon atoms in the $C_2$ group probably end up with the same potential energy. It is assumed that this is taken into account by the experimentally anchored value of $E_2$.

The relative partial molar free energy of carbon in
$\text{Th}C_x$ is given by
$$
F_{\mathrm{c}}^{\mathrm{M}}=N \mu-F_{\mathrm{c}}^{0}, \tag{9}
$$
where $N$ is Avogadro's number and $F_{\mathrm{c}}^{0}$ is the standard
free energy of carbon gas at the temperature $T$. De-
fining $\theta_{1}=N_{1} / N$ and $\theta_{2}=N_{2} / N$, we can express $F_{\mathrm{c}}^{\mathrm{M}}$
in terms of both $\theta_{1}$ and $\theta_{2} / \theta_{1}$ using eqs. (7) and (8).
We write for $F_{\mathrm{c}}^{\mathrm{M}}(\theta_{1})$:
$$
\begin{aligned}
F_{\mathrm{c}}^{\mathrm{M}}(\theta_{1}) &=-R T\left[\ln \left(\frac{1-\theta_{1}}{\theta_{1}}\right)+\ln q_{1}-E_{1} / R T\right. \\
&\left.-\frac{c \theta_{1} E_{11}}{R T}\right]-F_{\mathrm{c}}^{0}, \tag{10}
\end{aligned}
$$
where both $E_{1}$ and $E_{11}$ are redefined as gram-atomic
quantities. For $F_{\mathrm{c}}^{\mathrm{M}}(\theta_{2} / \theta_{1})$ we write:
$$
\begin{aligned}
F_{\mathrm{c}}^{\mathrm{M}}(\theta_{2} / \theta_{1}) &=-R T\left[\ln \left(\frac{1-\theta_{2} / \theta_{1}}{\theta_{2} / \theta_{1}}\right)+\ln q_{2}-E_{2} / R T-\right. \\
&\left.-\frac{c(\theta_{2} / \theta_{1}) E_{22}}{R T}\right]-F_{\mathrm{c}}^{0}, \tag{11}
\end{aligned}
$$
where both $E_{2}$ and $E_{22}$ are redefined as gram-atomic
quantities.

We now make the common assumption that both
$q_{1}$ and $q_{2}$ do not depend on the concentration of car-
bon atoms on the respective site type, and, further, do
not depend on temperature. Both $q_{1}$ and $q_{2}$ can then
be absorbed into constant vibrational contributions to
the respective entropies. Noting that the activity of
carbon, $a_{\mathrm{c}}$, is defined as:
$$
a_{\mathrm{c}}=\exp (F_{\mathrm{c}}^{\mathrm{M}} / R T) ; \tag{12}
$$
we therefore write finally for $a_{\mathrm{c}}$ in terms of both $\theta_{1}$
and $\theta_{2} / \theta_{1}$:
$$
\begin{aligned}
a_{\mathrm{c}}(\theta_{1}) &=\frac{\theta_{1}}{1-\theta_{1}} \exp \left(\frac{S_{\mathrm{c}}^{0}-S_{\mathrm{c}, 1}^{\mathrm{M}}(\mathrm{vib})}{R}\right) \\
& \times \exp \left(\frac{E_{1}-H_{\mathrm{c}}^{0}+c \theta_{1} E_{11}}{R T}\right), \tag{13}
\end{aligned}
$$
and
$$
\begin{aligned}
a_{\mathrm{c}}(\theta_{2} / \theta_{1}) &=\frac{\theta_{2} / \theta_{1}}{1-(\theta_{2} / \theta_{1})} \exp \left(\frac{S_{\mathrm{c}}^{0}-S_{\mathrm{c}, 2}^{\mathrm{M}}(\mathrm{vib})}{R}\right) \\
& \times \exp \left(\frac{E_{2}-H_{\mathrm{c}}^{0}+c(\theta_{2} / \theta_{1}) E_{22}}{R T}\right), \tag{14}
\end{aligned}
$$
where $H_{\mathrm{c}}^{0}-T S_{\mathrm{c}}^{0}=F_{\mathrm{c}}^{0}$ and $H_{\mathrm{c}}^{0}$ and $S_{\mathrm{c}}^{0}$ are defined anal-
ogously to $F_{\mathrm{c}}^{0}$ above. $S_{\mathrm{c}, 1}^{\mathrm{M}}(\mathrm{vib})$ and $S_{\mathrm{c}, 2}^{\mathrm{M}}(\mathrm{vib})$ are the
vibrational contributions to the entropy for carbon
atoms on sites of type 1 and 2 respectively.

Eqs. (13) and (14) must now be solved graphically
to obtain $a_{\mathrm{c}}(\theta_{1}+\theta_{2}, T)$ that is to say $a_{\mathrm{c}}(x, T)$. Firstly,
however values must be found for the quantities in
these equations.

There is now a considerable body of evidence which
demonstrates that at the composition $\text{Th}C_{0.75}$, carbon
vacancies (vacant sites of the first type) repel to the
extent that a superstructure on the carbon sublattice
develops with an order/disorder temperature of
approximately $830\ ^{\circ}\text{C}$ [8,10]. In a pair-wise additive
nearest neighbor model this implies repulsion between
carbon atoms (on sites of first type). Furthermore, the
partial molar enthalpy of carbon $H_{\mathrm{c}}^{\mathrm{M}}$ increases with
increasing $x$ ($x>0.75$) [1,2], a fact that can only be
accounted for in the Bragg-Williams approximation
by a repulsion between carbon atoms since from eq.
(10):
$$
H_{\mathrm{c}}^{\mathrm{M}} \approx E_{1}-H_{\mathrm{c}}^{0}+c x E_{11}, \quad x \lesssim 1.0. \tag{15}
$$

Yet the miscibility gap between carbon saturated
Th and $\text{Th}C_{0.75}$ closes, a fact which is often taken to
imply attraction between carbon atoms with the
resulting condensation into 2 phases. On the other
hand, for the nearest neighbor repulsion model in the
fcc lattice, one generates three ordered phases of the
well-known $\mathrm{A}_{3}\mathrm{B}$, $\mathrm{AB}$ and $\mathrm{AB}_{3}$ type. However, entry
to these phases from the disordered phase is now
thought to be via a first order transition when the
problem is solved at the tetrahedron approximation
of the cluster variation approach [11]. Thus the closed
miscibility gap may in fact be indicative of repulsion
between carbon atoms. While we do not suggest that
all three compounds of the type $\mathrm{Th}_{4}\mathrm{C}$, $\mathrm{Th}_{2}\mathrm{C}$ and
$\mathrm{Th}_{4}\mathrm{C}_{3}$ must inevitably exist within the composition
range $0.0<x<1.0$, this part of the phase diagram
would merit closer attention. Unfortunately, the dif-
fusivity of carbon may well be too low to attain true
equilibrium within a reasonable length of time.

At the Bragg-Williams approximation, it is possible
to trace out the boundary of the order/disorder tem-
perature by taking into account the long range order
parameter and the concomitant partitioning of carbon
atoms between two sublattices, both of which are

derived from *only* sites of the first type [12]. Using the observed maximum transition temperature, $T_{\rm c}$ of 1413 K as reported by Benz and Stone [4] we calculated $E_{11}$ to be $-3.918$ kJ/mol from the relation:

$$
E_{11}=-4kT_{\rm c}/c. \tag{16}
$$

Consideration of $E_{22}$ is more straightforward. We note firstly that $E_{22}$ is *attractive* in the very similar [9] $\rm UC_x$ $1.0<x<2.0$ system since (1) $H_{\rm c}^{\rm M}$ decreases with increasing $x$ [7,13], and (2) there is no evidence of superstructures at these compositions in either the U/C or Th/C systems. We note that the carbon diffusivity is certainly large enough at these compositions and temperatures for the sample to attain equilibrium rapidly [14]. We have calculated $E_{22}$ to be 5.887 kJ/mol from the relation:

$$
E_{22}=4kT_{\rm c}/c, \tag{17}
$$

where the critical temperature has been taken to be 2123 K [4]. Eq. (17) resulted from setting $(\partial\mu_2/\partial x)=$ 0 at $\theta_2/\theta_1=0.5$, which is approximately equal to $x=$ 1.5. Eq. (16), on the other hand, resulted from a Bragg-Williams treatment referred to earlier [12], where the long range order is lost at the transition temperature.

The phase diagram of Chiotti et al. [15,16] gives values of $T_{\rm c}$ for both gaps at significantly higher temperatures than do Benz and Stone [4]. A possible reason for this discrepancy is discussed by Benz and Stone. The calculated values of $a_{\rm c}$ are, however, quite insensitive to the choice made.

The terms $(S_{\rm c}^0-S_{\rm c,1}^{\rm M}(\text{vib}))$ and $(E_1-H_{\rm c}^0)$ in eq. (13) were found by fitting eq. (13) to the carbon activity at $x=0.8$ at two temperatures: 1100 and 1200 K. The carbon activity was calculated from a Gibbs-Duhem treatment of the recommended thorium activity [3] which was in turn deduced from low temperature thermal data. $(S_{\rm c}^0-S_{\rm c,1}^{\rm M}(\text{vib}))$ was found to be equal to $6.13\ \text{J/K·mol}$ while $(E_1-H_{\rm c}^0)$ was found to be equal to 154.3 kJ/mol.

The term $(S_{\rm c}^0-S_{\rm c,2}^{\rm M}(\text{vib}))$ was found by reference to the very similar U/C system which has been the subject of an experimental study of the carbon activity [13] and a theoretical study [7]. In this case, $S_{\rm c}^0-S_{\rm c,2}^{\rm M}(\text{vib})$ equals $44.17\ \text{J/K·mol}$. The second term $(E_2-H_{\rm c}^0)$ was found by requiring that the activity of carbon equals unity at $\rm ThC_{1.96}$ and a temperature of 600 K, i.e., the upper phase boundary. This takes advantage of the fact that (1) $\rm ThC_2$ is negligibly soluble in carbon and (2) $\theta_1\approx1.0$ at 600 K and at $\rm ThC_{1.96}$. $E_2-H_{\rm c}^0$ was found to be equal to 78.30 kJ/mol.

We are now finally in a position to compute the carbon activity as a function of $x$ and $T$. At equilibrium, eq. (13) must equal eq. (14). The quantity $a_{\rm c}(\theta_2)$ can be found graphically from eqs. (13) and (14). The functions $a_{\rm c}(\theta_1)$ and $a_{\rm c}(\theta_2)$ are then used to deduce, again by graphical means, $a_{\rm c}(\theta_1+\theta_2)(=a_{\rm c}(x))$.

## 3. Results

The computed carbon activity as a function of $x$ and $T$ is shown in fig. 1. The inflection in $a_{\rm c}$ upon entering and leaving the ordered regions cannot be generated from the present form of the partition function [eq. (1)] since long range order is specifically not included. Nonetheless, since the Bragg-Williams approximation gives, in that case, a zero long range order parameter above $T_{\rm c}$, [12] the activity isotherms will in fact be the same above $T_{\rm c}$ for both versions of the Bragg-Williams approximation. We have marked

![](./images/812414894958706690_1.jpg)

Fig. 1. The calculated activity of carbon as a function of composition and temperature in the thorium/carbon system.

the experimental $Th/ThC_{0.75}$ "diphasic" region with dashed lines on the activity isotherms.

For $0.9 < x < 1.9$, the activity isotherms are strikingly similar to those found in the U/C system by Tetenbaum and Hunt [13]. Our previous model in that system dealt with interaction of $C_2$ groups only and was thus unable to treat hypostoichiometric UC. The present formalism would be suitable, however, for dealing with the complete homogeneity range of $UC_x$.

It is interesting to note in fig. 1 that the boundary of the diphasic region $(ThC/ThC_2)$ is distorted toward compositions less than $x = 1.5$. Incidentally, this does not occur in the lattice gas with nearest neighbor interactions and a single type of site [7]; the diphasic region must then have a symmetry about $x = 1.5$. The real systems Th/C and U/C both exhibit a distorted diphasic region, a feature which may be taken as independent evidence of the essentially validity of the present model.

It is tempting to speculate on whether there is a connection between the temperature reversal of $a_c$ near ThC and the maximal melting temperature observed at this composition [4,16]. While the residues of the results of the present treatment are undoubtedly contained in the thermodynamics of the liquid phase, the present model, which is essentially a configurational lattice gas in nature, does not directly contain the physics to describe the melting transition.

## 4. Summary

We have developed a statistical mechanical model in order to provide access to the activity of carbon as a function of $x$ and $T$ in $ThC_x$. The results should be useful as a reliable guide for this quantity in the Th/C system. There is, however, a significant need for direct carbon activity measurements at high temperature in this system.

## Acknowledgements

We record our appreciation to Cathy Carbaugh for her able typing of the manuscript and to Elsie Klasek for her careful drawing of the diagram.

## References

[1] S. Aronson and J. Sadofsky, J. Inorg. Nucl. Chem. 27 (1965) 1769.
[2] T. Satow, J. Nucl. Mater. 21 (1967) 255.
[3] M.H. Rand, Thorium: Physico-Chemical Properties of its Compounds and Alloys, Atomic Energy Review Special Issue No. 5 (Vienna, IAEA, 1975).
[4] R. Benz and P.L. Stone, High Temp. Sci. 1 (1969) 114.
[5] A.L.G. Rees, Trans. Faraday Soc. 50 (1954) 335.
[6] A.L.G. Rees, Trans. Faraday Soc. 50 (1954) 343.
[7] G.E. Murch and R.J. Thorn, Phil. Mag. 34 (1976) 299.
[8] T. Satow, J. Nucl. Mater. 21 (1967) 343.
[9] C.E. Holley, J. Nucl. Mater. 51 (1974) 36.
[10] C.H. deNovion, B.E.F. Fender and W. Just, Fifth Int. Conf. Plutonium and Other Actinides, Baden Baden, Eds. H. Blank and R. Lindner (North Holland, Amsterdam, 1975).
[11] R. Kikuchi and H. Sato, Acta Met. 22 (1974) 1099.
[12] W. Shockley, J. Chem. Phys. 6 (1938) 130.
[13] M. Tetenbaum and P.D. Hunt, J. Nucl. Mater. 40 (1971) 104.
[14] G.E. Murch and R.J. Thorn, Phil. Mag. 35 (1977) 1441.
[15] P. Chiotti and R.W. White, J. Nucl. Mater. 23 (1967) 37.
[16] P. Chiotti, F.W. Korbitz and G.J. Dooley, J. Nucl. Mater. 23 (1967) 55.
# Bonding in a Cu (001) monolayer
G. S. Painter
Metals and Ceramics Division, Oak Ridge National Laboratory, Oak Ridge, Tennessee 37830
(Received 11 January 1978)

Results of a first-principles all-numerical linear variational energy-band calculation are presented for a Cu (001) monolayer. The electronic structure is discussed in terms of the changes in $d$ bonding which accompany the descent in symmetry in going from the bulk to the surface. The relation of the splittings and ordering of the levels to those of the bulk follow expectations based on simple $d$-bonding considerations. Results are compared with those from other studies and some discrepancies among earlier works are resolved.

In theoretical treatments of surface electronic structure, applications in thin-film approximations $^{1-5}$ are of particular interest. While models for quantitative work require a sufficient number of layers to properly describe the behavior of a physically realizable film, studies in the limit of a monolayer are also of interest since the essential physical effects of the surface perturbation are brought out and emphasized. As the extreme case of truncating the bulk and yet maintaining a surface, the results for the monolayer provide a first approximation to effects at real surfaces. Alterations from the bulk electronic structure in the monolayer limit represent an upper bound to the differences expected in the electronic structure of real thin films and the surface region of a solid. Shifts from the bulk electronic structure, which are not as easily perceived in results for thicker films, can be useful for interpretation of the differences measured in surface-sensitive spectroscopies.

In this communication, results of a first-principles linear variational calculation of the electronic structure of a Cu (001) monolayer are presented. Some discrepancies among results of earlier treatments $^{2-4}$ have led to some confusion regarding how the bulk $d$ levels are split and ordered by the surface perturbation. An analysis of the wave functions obtained in this work resolves these discrepancies. It is shown that the magnitude of the splitting of the levels for the descent in symmetry from bulk $(O_{h})$ to surface $(C_{4v})$ and the resultant level ordering is consistent with simple $d$-bonding considerations.

The fcc Cu (001) surface geometry is illustrated in Fig. 1. The orientation of the $x$ and $y$ axes is consistent with that usually chosen in the bulk, i.e., along directions to next-near neighbors (near neighbors lie in the $\langle 110\rangle$ directions). In the lower part of Fig. 1 appears the corresponding two-dimensional Brillouin zone with irreducible region shaded.

The discrete variational method, adapted to a thin-film geometry $^{5}$ and further modified for an all-numerical basis set, was used to calculate the monolayer band structure. Basis functions are defined in linear-combination-of-atomic-orbitals form by

$$
\chi_{j}(\vec{k}, \vec{r})=C_{j} \sum_{\nu} e^{i \vec{k} \cdot \vec{R}_{\nu}} \phi_{j}\left(\vec{r}-\vec{R}_{\nu}-\vec{\mu}_{l}\right), \quad(1)
$$

where $\vec{k}$ and $\vec{R}_{\nu}$ are vectors in the $x-y$ plane and the function $\phi_{j}$ is a bound-state solution of the equation

$$
\left[-\nabla^{2}+V_{\mathrm{MT}}^{l}(r)\right] \phi_{j}(\vec{r})=\epsilon_{j} \phi_{j}(\vec{r}), \quad(2)
$$

for the site defined by $\vec{\mu}_{l}$ within the central cell.
The potential function $V_{\mathrm{MT}}^{l}(r)$, which is used to define the basis $\{\phi_{j}(\vec{r})\}$ on site $l$ is chosen to approximate a spherically averaged site potential in the surface. With this potential the solutions of Eq. (2) are separable and the radial part of $\phi_{j}$ is determined directly from one-dimensional integration of the radial Schrödinger equation. This approach follows in spirit an energy-band method of using trial functions which are obtained as solutions of a Hamiltonian with a muffin-tin potential to carry out a variational calculation

![](./images/812640064902266882_1.jpg)

BONDING IN A Cu (001) MONOLAYER

with the full Hamiltonian. $^{6}$ It is an extension of an approach which has been developed by the author for cluster calculations. $^{7}$ The technique also resembles that developed independently by Averill and Ellis $^{8}$ for molecular calculations, however, there are differences in detail.

In its simplest form $V_{MT}^{l}(r)$ is just the local spherically averaged muffin-tin potential, but modifications are included to avoid the discon- tinuity in the potential at the muffin-tin radiusby matching to an exponential function outside. $^{9}$  For site $l$ ,
$$V_{\mathrm{MT}}^{l}(r)= \begin{cases}v_{l}(r), & r \leqslant b_{l} \\ v_{l}\left(b_{l}\right) \exp \left[-\lambda\left(r-b_{l}\right)\right], & r \geqslant b_{l},\end{cases}\qquad(3)$$
 where $b_{l}$ is the muffin-tin radius of site $l$ . Alter natively, the range over which the averaging is performed can extend over the region occupied by other atoms, and single-site self-consistency canbe included to approximate charge redistributions. $^{10}$ Procedures for choosing a more extended basisset have recently been discussed. $^{11}$ 

Variational freedom is introduced into the basis set by suitably scaling $V_{MT}(r)$ , e.g., by definition of the potential function outside the muffin tin as in Eq. (3) or by superimposing a screening poten- tial upon the site potential
$$V_{\mathrm{MT}}(r)=v_{j}(r)+q e^{-\lambda r} / r, \quad(4)$$
 where $q$ is constant. A useful and simple technique in this connection is to simply shift the potentialinside the muffin-tin radius by a constant $^{8,9}$ 
$$V_{\mathrm{MT}}(r)=v_{j}(r)+v_{c}. \quad(5)$$

This modification of the site potential can be used to bind excited states with a controlled degree of localization. With this choice, the solutions which are vanishingly small outside the muffin-tin radius are the true core solutions to the problem and are not altered by the shift.

Within this basis set the one-electron Schrodinger equation is solved using the full surface potential function with no constraints to muffin-tin form. Matrix elements of the Hamiltonian are conve- niently handled in this approach. In atomic units,
$$H_{i j}=\left\langle\chi_{i}\right|-\nabla^{2}+V(\overrightarrow{\mathrm{r}})\left|\chi_{j}\right\rangle, \quad(6)$$
 where $V(\overrightarrow{r})$ is the full crystal potential. From Eq.(2),
$$\begin{aligned}
-\nabla^{2} \chi_{j}= & -C_{j} \sum_{\nu} e^{i \overrightarrow{\mathrm{k}} \cdot \overrightarrow{\mathrm{R}}_{\nu}} \nabla^{2} \phi_{j}\left(\overrightarrow{\mathrm{r}}-\overrightarrow{\mathrm{R}}_{\nu}-\vec{\mu}_{l}\right) \quad(7) \\
= & C_{j} \sum_{\nu} e^{i \overrightarrow{\mathrm{k}} \cdot \overrightarrow{\mathrm{R}}_{\nu}}\left[\epsilon_{j}-V_{\mathrm{MT}}^{l}\left(\left|\overrightarrow{\mathrm{r}}-\overrightarrow{\mathrm{R}}_{\nu}-\vec{\mu}_{l}\right|\right)\right] \\
& \times \phi_{j}\left(\overrightarrow{\mathrm{r}}-\overrightarrow{\mathrm{R}}-\vec{\mu}_{l}\right)
\end{aligned}$$
 so that Eq. (6) becomes
$$H_{i j}=\left\langle\chi_{i}\left|\epsilon_{j}+V(\overrightarrow{\mathrm{r}})\right| \chi_{j}\right\rangle-\left\langle\chi_{i}\left|D_{j}\right\rangle,\right. \quad(9)$$
 where
$$\begin{aligned}
D_{j}(r)=C_{j} \sum_{\nu} e^{i \overrightarrow{\mathrm{k}} \cdot \overrightarrow{\mathrm{R}}_{\nu}} & V_{\mathrm{MT}}^{l}\left(\left|\overrightarrow{\mathrm{r}}-\overrightarrow{\mathrm{R}}_{\nu}-\vec{\mu}_{l}\right|\right) \\
& \times \phi_{j}\left(\overrightarrow{\mathrm{r}}-\overrightarrow{\mathrm{R}}_{\nu}-\vec{\mu}_{l}\right).
\end{aligned}\qquad(10)$$

Thus,
$$H_{i j}=\epsilon_{j} S_{i j}+V_{i j}-\left\langle\chi_{i} \mid D_{j}\right\rangle, \quad(11)$$
 where the last term in Eq. (11) brings in the cor- rections to shift from the generating potential to the full crystal potential. The technique has been tested in calculations for bulk copper, and the convergence to Korringa-Kohn-Rostoker results is very good over most of the band structure (to within small differences attributable to non-muf-fin-tin shifts, e.g., differences of less than 0.015 Ry in the $d$ bands).

To establish a connection with existing monolayer calculations, the Hartree-Fock-Slater one-elec- tron Hamiltonian was used with the crystal poten- tial constructed from superimposed atomic den- sities. A statistical exchange parameter value of 0.7 was chosen to simulate the potential function used in the work of Kar and Soven $^{4}$ (KS). Calcu lations in which the potential was averaged to muffin-tin form (as treated by KS) gave results qualitatively the same as those obtained in a treatment of the full potential, so only results from the latter model are presented.

The band structure along the $\Sigma$ direction is given in Fig. 2. The bands are in good agreement with those of KS, considering there are the differences in potential noted above. Good agreement also exists with the band structure of Cooper $^{2}$ for the case in which a boundary condition requiring the copper wave functions to vanish outside the nominal layer volume is imposed. For reasons that are not clear, Cooper's model representing the copper monolayer in vacuum is not in good agreement with this calculation or that of KS.

The narrowing of the $d$ band, the net upward shift of the center of gravity of the monolayer d band, and the increase in density of states at the $d$ -band center (resulting from the $\Gamma_{5} M_{5}$ band), are qualitatively consistent with recent angle-resolved photoemission results of Stöhr et al. $^{12}$  However, the lowering of the Fermi level sug- gested in Fig. 2 is an indication that the monolayer splittings are larger than expected at the realsurface. This effect was also obtained by Cooper $^{2}$  and would appear to be present in the results of KS. Coupling the monolayer to the underlying layer raises the Fermi level towards the bulk

![](./images/812640064902266882_2.jpg)

FIG. 2. Band structure along the $\Gamma M$ direction of the two-dimensional Brillouin zone for a Cu (001) monolayer. The splitting of the free-atom $d$ level in going to the bulk and the further splitting of the $\Gamma_{12}$ and $\Gamma_{25}'$ levels upon the descent in symmetry from the bulk $(O_{h})$ to the surface $(C_{4v})$ is indicated on left. Angular dependence of each $d$ state is noted by respective level.

value, as will be discussed later.

To show the origin of the monolayer band splittings, the free-atom $3d$ level and bulk zone-center $E_{g}(\Gamma_{12})$ and $T_{2g}(\Gamma_{25}')$ levels are shown in Fig. 2. These levels are split by the descent in symmetry at the surface to give four symmetry species. The bulk results were obtained with the same potential construction procedures as used for the monolayer. The angular dependence of each state is noted by the respective level at $\Gamma$. It is clear that, as a result of the magnitude and nonuniformity of the splittings, the ordering of levels of $E_{g}$ and $T_{2g}$ parentage become mixed for the monolayer. Although the zone-center symmetry labels imply good agreement with the results of KS, the discussion in the latter work states that the bulk levels remain grouped, but become reversed in order, in going to the monolayer. This discrepancy, as well as that noted by KS between their level orderings and those reported by Kasowski, $^{3}$ has been traced $^{7}$ to an inconsistency in coordinate systems used in the work of KS such that the identity of $d_{xy}$ and $d_{x^{2}-y^{2}}$ states are interchanged. Good agreement is obtained in all aspects with the results of KS when this inconsistency is corrected.

The bonding properties associated with the levels of Fig. 2 are in accord with the corresponding level splittings and ordering. For example, in the bulk each $T_{2g}$ level is characterized by constructive $dd\sigma$-type bonds between near neighbors in the $\langle 110\rangle$ directions along which the orbital lobes are aligned (each antibonds weakly with near neighbors in adjacent parallel planes). In going to the monolayer, the $d_{xz}$ and $d_{yz}$ orbital bonds between (001) planes are broken such that the $\Gamma_{5}$ level is destabilized by $\sim 2.1$ eV. On the other hand, the $d_{xy}$ orbitals are oriented parallel to the surface, so the $\Gamma_{3}$ level is not greatly perturbed by bulk truncation (the strong near-neighbor bonds are maintained).

Figures 3(a) and 4(a) illustrate the significant differences in bonding for these states of $T_{2g}$ parentage. The $\Gamma_{3}$ state, illustrated by the contour plot in the (001) plane in Fig. 3(a), is not greatly different from the $d_{xy}$ component of the $T_{2g}$ level in the bulk (or equivalently, the bulk $d_{xz}$ or $d_{yz}$ states plotted in the $x$-$z$ or $y$-$z$ plane, respectively). The large difference in orbital character between the $d_{xy}$ state in Fig. 3(a) and the component of the $\Gamma_{5}$ level plotted in the $x=y$ plane in Fig. 4(a) is a result of the surface perturbation. There is a clear correlation with the splitting of the $\Gamma_{25}'$ level shown in Fig. 2.

In the bulk, $d_{x^{2}-y^{2}}$ orbitals in a given (001) plane bond with $d_{x^{2}-y^{2}}$ orbitals on near-neighbor sites in adjacent (001) planes, and antibond with near neighbors within the same plane. Removal of adjacent layers in forming the monolayer results in a $\sim 1.4$ eV destabilization of the $\Gamma_{4}$ level so that it lies at the top of the $d$ band. A contour plot of this state in the $x$-$y$ plane appears in Fig. 3(b), and contrasts with the $d_{xy}$ state at the bottom of the $d$ band shown in Fig. 3(a). The state corresponding to the bottom of the $s$ band $(\Gamma_{1})$ is illustrated by the contour plot in the $x=y$ plane intersecting two copper sites in Fig. 5. The large $s$-like density between near-neighbor sites is related to the stability of this state.

In a Bloch representation, wave-vector modulation plays an important role in determining the bonding and level ordering of the different symmetry species. For example, the wave vector along the [100] direction, $\overrightarrow{\mathrm{k}}_{M}=(2\pi/a)(\frac{1}{2},0,0)$, reverses the sign on orbitals in alternate rows of atoms aligned perpendicular to the [100] direction. The lowering of the $M_{5}$ level below the $\Gamma_{5}$ is a direct result of the bonding differences associated with this phase factor, as illustrated by comparison of the $\Gamma_{5}$ and $M_{5}$ states in Fig. 4(a) and 4(b), respectively.

Similarly, the symmetry of the levels defining the $d$-band extremities is reversed in going from

![](./images/812640064902266882_3.jpg)

FIG. 3. Orbital contours in the monolayer plane with atomic sites at the center and corners of each plot. The $\Gamma_{3}\ (d_{xy})$ bonding state appears in (a), and the $\Gamma_{4}\ (d_{x^{2}-y^{2}})$ antibonding state in (b). Contour values are defined as follows: initial contour (one) is 0.0125 and successive contours are in the ratio of 1.75 with sign designated on contour. Wave functions have in- version symmetry through origin (center of plot).

$\Gamma$ to $M$. The bonding and antibonding character associated with the $d_{xy}$ and $d_{x^{2}-y^{2}}$ states at $\Gamma$ is reversed in going to $M$, as illustrated by comparison of the $\Gamma_{3}$ and $M_{3}\ (d_{xy})$ states in Figs. 3(a) and 6(a), respectively. The same behavior is found for the $\Gamma_{4}$ and $M_{4}(d_{x^{2}-y^{2}})$ states as shown in Figs. 3(b) and 6(b), respectively.

It is possible to estimate the shifts in the monolayer spectrum which occur in coupling the monolayer to underlying bulk layers. Interaction with

![](./images/812640064902266882_4.jpg)

FIG. 4. Orbital contours in the $x=y$ plane normal to the monolayer for one state of (a) the $\Gamma_{5}$ level and (b) the $M_{5}$ level. Contour magnitudes defined as in Fig. 3.

the atoms in the second layer will bring in bonding contributions to shift both the $\Gamma_{4}\ (d_{x^{2}-y^{2}})$ and $\Gamma_{5}\ (d_{xz},\ d_{yz})$ levels down towards the bulk $E_{F}$ and $T_{2g}$ levels, respectively. This lowering of the $\Gamma_{4}$ level will result in the Fermi level shifting into the $s$ band. The $\Gamma_{1}\ (d_{z^{2}})$ level, on the other hand, will be shifted somewhat higher due to antibonding with orbitals in the second layer (attractive terms in the potential will diminish this effect). The $\Gamma_{3}$ level will be only slightly destabilized. This net reduction of the overall level splitting, which is essential to avoid the Fermi level lying too near the $d$ band, demonstrates that results obtained for the monolayer represent an upper bound to the level shifts expected at the

![](./images/812640064902266882_5.jpg)

FIG. 5. Wave function contour plot in the $x=y$ plane normal to surface for the $\Gamma_{1} s$-like level at the bottom of the monolayer $s$ band.

surface of thick films. The orbital analysis indicates that the mechanism determining the electronic structure differences between surface and the bulk is the lowered coordination of the atoms at the surface. While it is apparent that at least a perturbative coupling of the monolayer to the bulk is called for in order to make a quantitative comparison with experimental data, the results obtained in the monolayer limit serve as a guide to the level shifts expected at real surfaces and thin films.

## ACKNOWLEDGMENT
This research was sponsored by the U.S. Depart- ment of Energy under contract with Union Carbide Corporation.

![](./images/812640064902266882_6.jpg)

FIG. 6. Contour plots in the (001) plane for states at the $M$ point in the Brillouin zone. The $M_{3}(d_{x y})$ orbital (a) originates from the $\Gamma_{3}$ level [Fig. 3(a)] while the $M_{4}$ state of $d_{x^{2}-y^{2}}$ symmetry (b) derives from the $\Gamma_{4}$ level [Fig. 3(b)].

$^{1}$J. G. Gay, J. R. Smith, and F. J. Arlinghaus, Phys. Rev. Lett. 38, 561 (1977), and references therein.
$^{2}$B. R. Cooper, Phys. Rev. Lett. 30, 1316 (1973).
$^{3}$R. V. Kasowski, Phys. Rev. Lett. 33, 83 (1974).
$^{4}$N. Kar and P. Soven, Phys. Rev. B 11, 3761 (1975).
$^{5}$G. S. Painter, Phys. Rev. B 17, 662 (1978), and refer- ences therein.
$^{6}$G. S. Painter, Phys. Rev. B 7, 3520 (1973).
$^{7}$G. S. Painter (unpublished).
$^{8}$F. W. Averill and D. E. Ellis, J. Chem. Phys. 59, 6412 (1973).
$^{9}$D. J. Newman and C. D. Taylor, J. Phys. B 5, 2332 (1972).
$^{10}$F. Borghese and P. Denti, Lett. Nuovo Cimento 2, 608 (1971).
$^{11}$A. Zunger and A. J. Freeman, Phys. Rev. B 15, 4716 (1977).
$^{12}$J. Stöhr, G. Apai, P. S. Wehner, F. R. McFeely, R. S. Williams, and D. A. Shirley, Phys. Rev. B 14, 5144 (1976).
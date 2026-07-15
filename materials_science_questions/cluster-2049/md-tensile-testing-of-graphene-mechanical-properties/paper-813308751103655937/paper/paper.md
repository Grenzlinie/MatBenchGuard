# Strain-engineered graphene through a nanostructured substrate. II. Pseudomagnetic fields

M. Neek-Amal$^{1,2}$ and F. M. Peeters$^{2}$

$^{1}$Department of Physics, Shahid Rajaee Teacher Training University, Lavizan, Tehran 16785-136, Iran
$^{2}$Departement Fysica, Universiteit Antwerpen, Groenenborgerlaan 171, B-2020 Antwerpen, Belgium

(Received 6 February 2012; revised manuscript received 23 April 2012; published 22 May 2012)

The strain-induced pseudomagnetic field in supported graphene deposited on top of a nanostructured substrate is investigated by using atomistic simulations. A step, an elongated trench, a one-dimensional barrier, a spherical bubble, a Gaussian bump, and a Gaussian depression are considered as support structures for graphene. From the obtained optimum configurations we found very strong induced pseudomagnetic fields which can reach up to $\sim$1000 T due to the strain-induced deformations in the supported graphene. Different magnetic confinements with controllable geometries are found by tuning the pattern of the substrate. The resulting induced magnetic fields for graphene on top of a step, barrier, and trench are calculated. In contrast to the step and trench the middle part of graphene on top of a barrier has zero pseudomagnetic field. This study provides a theoretical background for designing magnetic structures in graphene by nanostructuring substrates. We found that altering the radial symmetry of the deformation changes the sixfold symmetry of the induced pseudomagnetic field.

DOI: 10.1103/PhysRevB.85.195446
PACS number(s): 65.40.De

## I. INTRODUCTION

In most of the experiments on graphene, the 2D atomic layer is placed on top of a substrate, which at atomic scale is not flat. Geometrically structured substrates affect various properties of graphene$^{1,2}$ and can prevent the crumpling of graphene which occurs for freestanding graphene without support.$^{3}$ Recently, the modification of the properties of graphene on top of a substrate were investigated. It was found that substrates can induce corrugations, modify the electric conductance, and deform graphene.$^{4,5}$

Tomori *et al.* used pillars made of a dielectric material placed on top of a substrate which is then overlayed with graphene to generate nonuniform strain on a microscale.$^{6}$ Elastic deformations in graphene create a pseudomagnetic field which acts on graphene's massless charge carriers.$^{7-9}$ The resulting variation of the hopping energies can be viewed as an induced pseudomagnetic field which enters in the Dirac equation. Engineering the right topology of the induced pseudomagnetic field can provide magnetic confinement which confines electrons in specific regions in space.$^{10,11}$ It has been shown theoretically that inhomogeneous magnetic fields are able to confine massless Dirac fermions in a monolayer graphene sheet.$^{12}$ Pereira *et al.* investigated the influence of local strain on the electronic structure of graphene and showed that it can used to generate electron beam collimation, 1D channels, surface states, and confinement.$^{13}$

Here, we investigate several nanostructured substrates with different geometrical deformations. We carried out molecular dynamics simulations at $T=300$ K to minimize the energy and find the optimum profile of the deposited graphene on top of different nanostructured substrates. An elongated trench, a barrier, a bubble, a Gaussian bump, and a Gaussian depression are considered as examples of nanostructured substrates. The adhesion of the substrate to the deposited graphene can induce a very strong pseudomagnetic field which we found depends on the imposed boundary conditions on the graphene sheet. Strong pseudomagnetic fields ($\sim$1000 T) are found around the deformed regions in graphene. A substrate with (i) a step forms two magnetic barriers around the step with opposite sign, (ii) a trench forms two narrow magnetic barriers around the trench boundaries with the same sign and one with opposite sign within the trench, and (iii) a one-dimensional barrier forms two pairs of magnetic barriers around the barrier's wall. The magnetic confinement for a Gaussian depression in the substrate loses the sixfold symmetry of the pseudomagnetic field which is not the case for graphene on top of a Gaussian bump.

This paper is organized as follows. In Sec. II the details of the atomistic model are presented. In Sec. III we present the strain-induced gauge field model. In Sec. IV we present results for the gauge fields and the pseudomagnetic fields, for various nanostructured substrates. The results are summarized in Sec. V.

## II. ATOMISTIC MODEL

In order to find the optimum configuration of graphene (GE) on top of various nanostructured substrates we employed classical atomistic molecular dynamics simulation (MD). The second generation of Brenner's bond-order potential$^{14}$ is employed for carbon-carbon interaction and the van der Waals (vdW) interaction between GE and different substrates is modeled by employing the Lennard-Jones (LJ) potential, i.e.,

$$
u(r)=4\epsilon[(\sigma/r)^{12}-(\sigma/r)^{6}],\tag{1}
$$

where $r$ is the distance between the two particles, and $\epsilon$ and $\sigma$ are the "energy parameter" and the "length parameter," respectively (see Table I for a list of parameters used in the paper). To model the interaction between two different types of atoms such as the carbon atom (C) and the substrate atom (S), we adjust the LJ parameters using the equations $\epsilon_{T}=\sqrt{\epsilon_{C}\epsilon}$ and $\sigma_{T}=(\sigma_{C}+\sigma)/2$. For carbon we use the parameters $\sigma_{C}=3.369$ Å and $\epsilon_{C}=2.63$ meV. For the substrate atoms we set $\sigma=3.5$ Å and $\epsilon=10.0$ meV, which is typical, e.g., for a SiO$_2$ substrate.$^{15}$ The simulation is done for a GE sheet with dimension $l_{x}=19.17$ nm and $l_{y}=19.67$ nm at $T=300$ K. The number of substrate atoms is $M=6000$. In order to model the substrate, a (100) surface having a typical lattice parameter $\ell=3$ Å is assumed. The density of sites in the substrate is

<table>
<caption>TABLE I. A list of all relevant parameters used in the paper.</caption>
<tbody>
<tr>
<td>$l_x$,$l_y$</td>
<td>The graphene length and width</td>
</tr>
<tr>
<td>$\epsilon$,$\sigma$</td>
<td>The energy and length parameters in the van der Waals (vdW) potential for the substrate atoms, Eq. (1)</td>
</tr>
<tr>
<td>$\lambda$,$\theta(x)$</td>
<td>The wave length and the step function</td>
</tr>
<tr>
<td>$R$</td>
<td>The radius of the Gaussian bump or depression</td>
</tr>
<tr>
<td>$h_0$</td>
<td>The amplitude of sinusoidal waves or height (depth) of Gaussian bump/bubble/barrier (depression or trench)</td>
</tr>
<tr>
<td>$h_1$,$d$</td>
<td>A shift or vertical distance between graphene and substrate and the width of the trench/barrier</td>
</tr>
<tr>
<td>$u_{\alpha\beta}$,$\mathbf{A}$,$B$</td>
<td>Strain tensor, strain induced gauge field, and magnetic field</td>
</tr>
</tbody>
</table>

$\Sigma_S = \ell^{-2}$. The details of the found deformations are reported in our previous study. $^{16}$

## III. STRAIN-INDUCED PSEUDOMAGNETIC FIELD

Generalizing the Dirac equation, which governs the low-energy electronics of graphene, to curved surfaces is an interesting development which may model some cosmological problems. $^{8,9}$ The metric of the curved surface enters now into the Dirac equation. The origin of the deformations are external stresses which deform graphene so that the nearest-neighbor distances become nonequal. Notice that the external stresses can be induced by the substrate. The latter results in modified hopping parameters introduced in the tight-binding model which are now a function of the atomic positions $t(\mathbf{r})$. $^{17}$ Assuming small atomic displacements (i.e., $\mathbf{u} = \mathbf{r}_i' - \mathbf{r}_i < a_0$ where $a_0$ is the carbon-carbon bond length) and rewriting the Dirac Hamiltonian in the effective mass approximation with nonequal hopping parameters tells us that the strain induces an effective gauge field
$$
\mathbf{A} = \frac{2\beta\hbar}{3a_0 e}(u_{xx} - u_{yy}, -2u_{xy}), \tag{2}
$$
where $\beta$ ($\sim$2-3) is a constant and $u_{\alpha\beta}$ is the strain tensor including out-of-plane displacements. $^{8}$ The corresponding pseudomagnetic field perpendicular to the $x$-$y$ plane is obtained as
$$
B = \partial_y A_x - \partial_x A_y. \tag{3}
$$

This is the pseudomagnetic field which the electron experiences in the K valley. We will find $B$ by making the necessary differentiations numerically for longitudinally supported boundary conditions. Here we are mostly interested in the out-of-plane contributions of the pseudomagnetic field which mainly appears around the deformed parts of graphene. The other in-plane terms contribute less to the pseudomagnetic field around the deformed parts, particularly when the system is larger than the size of these deformed parts and is supported from boundaries. Notice that in order to perform the numerical differentiations [in Eq. (2) and Eq. (3)] one needs a reference graphene lattice $(\mathbf{r}_i)$ in order to compare the optimized lattice $(\mathbf{r}_i')$ with the reference system. We used the optimized graphene profile at the given temperature over a flat substrate as the reference system. However, when the boundaries are free there is considerable difference (at the boundaries and for some particular systems) between the optimized graphene over the deformed substrate and the reference system. This is due to the fact that at finite temperature the free edges of graphene over the substrate can vibrate and deform (due to the substrate induced strain) freely while they will not be deformed in the reference system. Therefore the reference system with free boundaries for some of the systems can be very different from the optimized graphene over the deformed substrate at finite temperature; hence the differentiation is not well defined. Therefore, in this paper we focused on systems with fixed boundaries, which were studied in our previous paper, $^{16}$ where we have a true reference system suitable for numerical differentiations.

## IV. RESULTS AND DISCUSSION

In this study we investigate several different geometries for the substrate which can be realized experimentally. For all studied cases we first obtained the optimum configuration of GE on top of the different nanostructured substrates using MD simulations (those results were presented in our previous work $^{16}$). Then, for the supported boundary condition, we calculate the corresponding gauge field from which we obtain the pseudomagnetic field.

### A. Step

An interesting substrate configuration is a step which was recently studied in an experiment to measure the electronic and morphology of deposited graphene $^{18}$
$$
h_S(x,y) = h_0\theta(x), \tag{4}
$$
where $\theta(x)$ is the Heaviside step function and $h_0 = 1$ nm is the height of the step. GE with armchair direction is put on top of the step. In Fig. 1 the optimum configuration of GE along the armchair direction with longitudinally supported boundary condition is shown when placed over a sharp step defined by Eq. (4).

The induced gauge field as obtained from Eq. (2) is averaged over the $y$ direction and is shown in Fig. 2(a). All atoms at the step region are stretched which results in considerable gauge fields around $x \approx 0$. Figure 2(b) shows the averaged

![](./images/813308751103655937_1.jpg)

FIG. 1. (Color online) The optimum configuration of armchair graphene over a step located at $x=0$ with supported longitudinal ends. The colors indicate the size of strain.

![](./images/813308751103655937_2.jpg)

FIG. 2. (Color online) The averaged gauge fields (a) and the induced pseudomagnetic fields (b) averaged over the $y$ direction for graphene on top of a step as shown in Fig. 1 which has been supported from the longitudinal ends while it can freely move along the $z$ direction.

pseudomagnetic field over the $y$ direction, $\langle B\rangle$, versus $x$. In order to calculate averages we made a histogram where $l_x$ is divided into 60 equal parts. Notice that the induced pseudomagnetic field is mostly concentrated beyond $x=0$ and consists of a positive and an adjacent negative barrier with total average zero. Because of thermal fluctuations (i.e., $T=300$ K) the positive and negative barrier are only approximately identical. The larger the curvature the larger the pseudomagnetic field. The large pseudomagnetic field around the step separates the GE sheet into a left- and a right-hand side, where "B" is small. Electrons will be trapped in this region into snake orbits and electrons passing perpendicular to this rectangular part will experience large pseudomagnetic fields. Notice that by changing the height of the step $(h_0)$, we are able to control the size of the magnetic barrier and consequently the magnetic confinement.

### B. Trench
The other important substrate that we study here is an elongated trench
$$
h_{S}(x, y)=h_{0} \theta\left(x^{2}-d^{2}\right), \tag{5}
$$
with two walls of height 1 nm located at $x=\pm d=\pm 1.5$ nm. In Fig. 3 we show the optimum configuration of armchair graphene with supported boundary condition on top of the trench defined by Eq. (5).

![](./images/813308751103655937_3.jpg)

FIG. 3. (Color online) The optimum configuration of armchair graphene over a trench located at $|x|<1.5$ nm where both longitudinal ends were supported in the $x$-$y$ plane. The colors indicate the size of the strain.

The absolute value of the induced gauge field as obtained from Eq. (2) is averaged over the $y$ direction and is shown in Fig. 4(a). All atoms at both sides are stretched toward the well region which results in a considerable gauge field around $x\approx\pm d$. Figure 4(b) shows the $y$-averaged pseudomagnetic field. Notice that there is a nonzero $\langle|\mathbf{A}|\rangle$ and $\langle B\rangle$ within the trench which is a consequence of the bent (nonflat) graphene

![](./images/813308751103655937_4.jpg)

FIG. 4. (Color online) The averaged gauge field (a) and the induced pseudomagnetic field (b) averaged over the $y$ direction for graphene on top of a well as shown in Fig. 3 which has been supported from the longitudinal ends while it can freely move along the $z$ direction.

![](./images/813308751103655937_5.jpg)

FIG. 5. (Color online) The optimum configuration of armchair graphene over an elongated cubic barrier with $|x| < 1.5$ nm where the zigzag edges were supported in the $x$-$y$ plane. The colors indicate the size of strain.

in the middle region. Notice that the pseudomagnetic fields are smaller than those obtained for a step profile. Indeed supporting GE longitudinally from two ends prevents GE from moving into the well and consequently there will be less variations in the heights. The magnetic field profile consists of a positive B barrier inside the trench and two negative barriers located at the steps. The total average magnetic field is also zero in this case.

### C. Barriers
A barrier in the middle of the substrate is the reverse situation of the previous case. An elongated barrier in the $y$ direction is parameterized as
$$
h_{S}(x,y)=h_{0}\theta(x^{2}-d^{2}), \tag{6}
$$
with two walls at $x=\pm d=\pm1.5$ nm of height of 1 nm. Figure 5 shows the optimum configuration of arm-chair GE in the case of supported boundary condition over the barrier.

The induced gauge field as obtained from Eq. (2) was averaged over the $y$ direction and is shown in Fig. 6(a). All atoms at both sides are stretched toward the barrier region which causes considerable gauge fields around $x\approx\pm d$. Figure 6(b) shows the averaged pseudomagnetic field over the $y$ direction which is less than 20 T. Both gauge and pseudomagnetic fields are comparable with those found for the substrate with a single step placed in the middle of the GE sheet. The main difference is the formation of a zero magnetic field channel in the region $|x|<d$. The electrons will be trapped in this rectangular channel which can be realized in experiments. On both sides of this magnetic channel there are two double magnetic barriers of similar shape. Because of thermal fluctuations the barriers are not identical.

### D. Spherical bubble
The next important deformation of the substrate that has been realized experimentally $^{19,20}$ is a bubble
$$
h_{S}(x_{i},y_{i})=\sqrt{R^{2}-\rho_{i}^{2}}+h_{1}, \tag{7}
$$
where $R$ is the radius of the bubble and $\rho_{i}^{2}=x_{i}^{2}+y_{i}^{2}$ is the radial distance of the $i$th atom from the center. In order to create an uniform discrete atomistic structure for the bubble, we set $h_{1}=-R/2$ where $R=2$ nm. The optimum configuration for the longitudinally supported graphene over the bubble substrate is shown in Fig. 7. Due to the supported end GE is elongated longitudinally along the supported direction; see inset in Fig. 7.

In Fig. 8(a) the induced gauge field (corresponding to the induced strain and around the central part) is illustrated by using Eq. (2). Figure 8(a) shows a vector plot of the induced gauge fields where the length of the vectors and the colors denote the absolute value of $\mathbf{A}$. The corresponding magnetic field is depicted in Fig. 8(b). Notice that both the gauge field and the pseudomagnetic field exhibit an approximate sixfold symmetry. $^{17,21}$ Because of thermal fluctuations the symmetry is not exact. Notice that there is a little elongation along the supported direction. We will discuss this symmetry in the next

![](./images/813308751103655937_6.jpg)

FIG. 6. (Color online) The averaged (a) gauge field and (b) the induced pseudomagnetic field averaged over the $y$ direction for a graphene on top of a barrier as shown in Fig. 5 which has been supported from the longitudinal ends while it can freely move along the $z$ direction.

![](./images/813308751103655937_7.jpg)

FIG. 7. (Color online) The optimum configuration of armchair graphene, with two longitudinal ends supported in the $x$-$y$ plane, on top of a bubble. The inset shows a different view indicating the elongation of the deformation of graphene along the $x$ direction, i.e., armchair direction. The colors indicate the size of the strain.

![](./images/813308751103655937_8.jpg)

FIG. 8. (Color online) (a) Vector plot of the gauge field and (b) the induced pseudomagnetic field for armchair graphene placed over a spherical bubble. The obtained deformation is shown in Fig. 7. Graphene was supported from the longitudinal ends while it can vibrate along the $z$ direction.

section. Notice that the induced magnetic fields are larger than those found for the step, trench, and barrier.

### E. Gaussian bump/depression
The Gaussian bump (protrusion)/depression $^{22,23}$ is parametrized as
$$
h_{S}(x_{i},y_{i})=\pm h_{0}\exp\left(-\rho_{i}^{2}/2\gamma^{2}\right),\qquad(8)
$$
where $+h_{0}$ ($-h_{0}$) ($=1$ nm) is the height (depth) of the Gaussian bump (depression), $\rho_{i}^{2}=x_{i}^{2}+y_{i}^{2}$ is the radial distance of the $i$th atom, and $\gamma=1$ nm is the variance of the Gaussian.

Since the optimum configuration of supported graphene over the Gaussian bump is similar to the one for a spherical bubble, we will not report them here. For supported graphene over a Gaussian depression the optimum configuration is not Gaussian (as was shown in Ref. 16).

The results of the gauge fields and pseudomagnetic fields for a graphene membrane with Gaussian deformation show a clear sixfold symmetry. $^{17,21}$ For a Gaussian deformation of the graphene membrane, Eq. (8), using Eq. (2) and Eq. (3) we found
$$
\mathbf{A}=-\frac{\rho^{2}h^{2}(\rho,\theta)}{2\gamma^{4}}[\cos(2\theta),\sin(2\theta)/2],\qquad(9)
$$
and for the corresponding pseudomagnetic field
$$
\mathbf{B}=\nabla\times\mathbf{A}=\frac{h^{2}(\rho,\theta)\rho^{2}}{\gamma^{6}}\sin(3\theta),\qquad(10)
$$
where $x=\rho\cos(\theta)$ and $y=\rho\sin(\theta)$. The well-known sixfold symmetry is due to the dependence of $B$ on $\sin(3\theta)$. Our atomistic results for $B$ [see Fig. 8(b)] are in good agreement with Eq. (10).

It is surprising that we found a sixfold symmetry for deformed graphene over a Gaussian bump but not for the Gaussian depression. This is due to the non-Gaussian profile of GE on top of a Gaussian depression. $^{16}$ Breaking the radial symmetry of graphene deformation reduces the symmetry in $\mathbf{B}$ [see Fig. 9(b)]. This particular symmetry affects also the energy eigenvalues and corresponding wave functions. $^{17}$

![](./images/813308751103655937_9.jpg)

FIG. 9. (Color online) (a) Vector plot of the gauge field and (b) the induced pseudomagnetic field for armchair graphene deposited over a Gaussian depression. Graphene has been supported from the longitudinal ends while it can vibrate along the $z$ direction.

In Fig. 9(a) the induced gauge fields for GE on top of a Gaussian depression is shown where the length of the vectors and the colors denote the absolute value of $\mathbf{A}$. Both gauge fields and pseudomagnetic fields are smaller than those found for the supported graphene over the bubble and the Gaussian bump. This is a consequence of the non-Gaussian profile for the optimum configurations which yields alteration in sixfold symmetry in the induced pseudomagnetic field.

### V. SUMMARY
We investigated systematically the induced pseudomagnetic field properties for graphene deposited on top of different nanostructured substrates by using molecular dynamics simulations at $T=300$ K. The van der Waals interaction between the substrate and graphene was modeled by a Lennard-Jones potential. We found that the induced magnetic field for graphene on top of a step consists of two magnetic barriers with different sign, while for a trench it forms two narrow magnetic barriers around the trench boundaries and one with opposite sign within the trench. The one-directional substrate barrier forms two sets of magnetic barriers around the barrier wall. The magnetic field for the Gaussian depression looses its sixfold symmetry (due to the non-Gaussian deformation of graphene) as compared to GE on top of the Gaussian bump/bubble. The strain induced strong pseudomagnetic fields. Controlling the pseudomagnetic field is possible by controlling the substrate pattern and the size of the deformation.

### ACKNOWLEDGMENTS
This work was supported by the Flemish Science Foundation (FWO-VI) and the ESF EUROCORE program Euro-GRAPHENE: CONGRAN.

$^{1}$K. S. Novoselov, A. K. Geim, S. V. Morozov, D. Jiang, Y. Zhang, S. V. Dubonos, I. V. Gregorieva, and A. A. Firsov, *Science* **306**, 666 (2004).

$^{2}$K. S. Novoselov, A. K. Geim, S. V. Morozov, D. Jiang, M. I. Katsnelson, I. V. Grigorieva, S. V. Dubonos, and A. A. Firsov, *Nature* (London) **438**, 197 (2005).

195446-5

$^3$D. Nelson, D. Piran, and S. Weinberg, *Statistical Mechanics of Membranes and Surfaces* (World Scientific, Singapore, 2004).

$^4$W. Bao, F. Miao, Z. Chen, H. Zhang, W. Jang, C. Dames, and C. Ning Lau, *Nature Nanotechnology* **4**, 562 (2009).

$^5$M. Ishigami, J. H. Chen, W. G. Cullen, M. S. Fuhrer, and E. D. Williams, *Nano Lett.* **7**, 1643 (2007).

$^6$H. Tomori, A. Kanda, H. Goto, Y. Ootuka, K. Tsukagoshi, S. Moriyama, E. Watanaba, and D. Tsuya, *Applied Physics Express* **4**, 075102 (2011).

$^7$F. Guinea, M. I. Katsnelson, and A. K. Geim, *Nature Physics* **6**, 30 (2010).

$^8$H. Castro Neto, F. Guinea, N. M. R. Peres, K. S. Novoselov, and A. K. Geim, *Rev. Mod. Phys.* **81**, 109 (2009).

$^9$F. Guinea, M. I. Katsnelson, and M. A. H. Vozmediano, *Phys. Rev. B* **77**, 075422 (2008).

$^{10}$J. Reijniers, F. M. Peeters, and A. Matulis, *Phys. Rev. B* **59**, 2817 (1999).

$^{11}$J. Reijniers and F. M. Peeters, *Phys. Rev. B* **63**, 165317 (2001); *J. Phys.: Condens. Matter* **12**, 9771 (2000).

$^{12}$A. De Martino, L. DellAnna, and R. Egger, *Phys. Rev. Lett.* **98**, 066802 (2007).

$^{13}$Vitor M. Pereira and A. H. Castro Neto, *Phys. Rev. Lett.* **103**, 046801 (2009).

$^{14}$D. W. Brenner, O. A. Shenderova, J. A. Harrison, S. J. Stuart, B. Ni, and S. B. Sinnot, *J. Phys.: Condens. Matter* **14**, 783 (2002).

$^{15}$Zhun-Yong Ong and Eric Pop, *Phys. Rev. B* **81**, 155408 (2010).

$^{16}$M. Neek-Amal and F. M. Peeters, *Phys. Rev. B* **85**, 195445 (2012).

$^{17}$K-J. Kim, Ya-M. Blanter, and K-H. Ahn, *Phys. Rev. B* **84**, 081401(R) (2011).

$^{18}$P. Lauffer, K. V. Emtsev, R. Graupner, Th. Seyller, L. Ley, S. A. Reshanov, and H. B. Weber, *Phys. Rev. B* **77**, 155426 (2008).

$^{19}$T. Georgiou1, L. Britnell, P. Blake, R. V. Gorbachev, A. Gholinia, A. K. Geim, C. Casiraghi, and K. S. Novoselov, *Appl. Phys. Lett.* **99**, 093103 (2011).

$^{20}$E. Stolyarova, D. Stolyarov, K. Bolotin, S. Ryu, L. Liu, K. T. Rim, M. Klima, M. Hybertsen, I. Pogorelsky, I. Pavlishin, K. Kusche, J. Hone, P. Kim, H. L. Stormer, V. Yakimenko, and G. Flynn, *Nano Lett.* **9**, 332 (2009).

$^{21}$S. P. Koenig, N. G. Boddeti, M. L. Dunn, and J. Scott Bunch, *Nature Nanotechnology* **6**, 543 (2011).

$^{22}$M. Neek-Amal and F. M. Peeters, *J. Phys.: Condens. Matter* **23**, 045002 (2011).

$^{23}$S. Viola Kusminskiy, D. K Campbell, A. H. Castro Neto, and F. Guinea, *Phys. Rev. B* **83**, 165405 (2011).
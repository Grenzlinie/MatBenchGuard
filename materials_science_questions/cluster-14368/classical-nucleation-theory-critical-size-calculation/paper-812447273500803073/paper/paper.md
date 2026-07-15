# AN ALGORITHM TO CALCULATE THE CONTACT ANGLE OF HETEROGENEOUS NUCLEATION

A. SEDEHI AND Z. H. MEIKSIN
Department of Electrical Engineering, University of Pittsburgh, Pittsburgh, PA 15261 (U.S.A.)

J. R. BLACHERE
Department of Metallurgical and Materials Engineering, University of Pittsburgh, Pittsburgh, PA 15261 (U.S.A.)

(Received December 5, 1980; accepted March 26, 1981)

We developed an algorithm to calculate the contact angle of evaporated silver and gold on alkali halide substrates. The algorithm differs from previous published work in that it uses the single-atom critical nucleus concept.

## 1. INTRODUCTION

In the heterogeneous nucleation of metals on alkali halide substrates it has been shown that the critical nucleus consists of a single atom $^{1-3}$. Therefore, the concept of the contact angle of the nucleus on the substrate, as defined by the capillarity theorem $^{4,5}$, must be modified. The modification, based on the atomistic theory of nucleation as developed by Walton and coworkers $^{6,7}$, is aimed at finding the critical adatom concentration and applying the information to the cap-shaped assumed critical nucleus $^{5,8}$ to obtain the contact angle. The link between the two theories is similar to the work of Lewis $^{9}$ who tried to find an agreement between the two theories, reasoning that the shape of a cluster of only a few atoms will assume the closest structure to the ideal cap shape. The algorithm to find the contact angle is similar to that of Gretz $^{8}$ who determined the contact angle of evaporated zinc, cadmium, silver, nickel and gold on a tungsten substrate. The inconsistency which he found between the theory and measured results is caused by the error in finding the critical supersaturation and surface energy values.

## 2. ALGORITHM

The nucleation rate of silver and gold on alkali halide substrates under typical deposition conditions is given by $^{2,10}$

$$
I=\frac{4 R^{2}}{v N_{0}} \exp \left(\frac{2 E_{\mathrm{a}}-E_{\mathrm{d}}}{k T}\right)
$$

where $R$ is the incident rate, $v$ the vibrational frequency, $N_{0}$ the density of substrate adsorption sites, $E_{\mathrm{a}}$ the binding energy of the atom to the substrate, $E_{\mathrm{d}}$ the activation energy for surface diffusion, $k$ Boltzmann's constant and $T$ the substrate temperature in kelvins. The source and target materials determine $E_{\mathrm{a}}, E_{\mathrm{d}}, v$ and $N_{0}$.

---
0040-6090/81/0000-0000/$02.50
© Elsevier Sequoia/Printed in The Netherlands

For the critical nucleation rate as defined previously $^{9.11} I=1$, and from eqn. (1) the critical incidence rate $R_{\text {crit }}$ is given by

$$
R_{\text {crit }}=\frac{v N_{0}}{4} \exp \left\{\left(\frac{-2 E_{\mathrm{a}}-E_{\mathrm{d}}}{k T}\right)^{12}\right\}
$$

The critical adatom concentration is $^{4}$

$$
N_{0}^{*}=R_{\text {crit }} T_{\text {s }}
$$

where the mean stay time $T_{s}$ is given as $^{4}$

$$
T_{\mathrm{s}}=\frac{1}{v} \exp \left(\frac{E_{\mathrm{a}}}{k T}\right)
$$

The number $n_{\mathrm{c}}$ of atoms for equilibrium vapour pressure is given by $^{4.5}$

$$
n_{\mathrm{c}}=\frac{P_{\mathrm{c}}}{(2 \pi M k T)^{1 / 2}} T_{\mathrm{s}}
$$

where $M$ is the molecular weight of the material. The equilibrium vapour pressure $P_{\mathrm{c}}$ is given as $^{12}$

$$
\log P_{\mathrm{c}}=C_{1}-C_{2} / R T
$$

where $R$ is the universal gas constant and $C_{1}$ and $C_{2}$ are empirical constants. The supersaturation $S$ is defined as $^{4.5 .8}$

$$
S=n_{0}^{*} / n_{\mathrm{c}}
$$

Using eqns. (3) and (4), $S$ can be found. The volume Gibbs free energy of formation is given by $^{4.5}$

$$
\Delta G_{\mathrm{v}}=\frac{-k T}{\Omega} \ln S
$$

where $\Omega$ is the volume of the condensate atom. The nucleation rate as given by the capillarity theory is given by $^{4.5 .8}$

$$
I=2 \pi r^{*} \sin \theta n_{1}^{*} a_{0} v N_{0} \exp \left\{\frac{-\left(\Delta G^{*}+E_{\mathrm{d}}\right)}{k T}\right\}
$$

where $r^{*}$ is the radius of the critical nucleus, $\theta$ the contact angle, $a_{0}$ the substrate lattice parameter, $n_{1}{ }^{*}$ the adatom concentration and $\Delta G^{*}$ the Gibbs free energy of formation. By introducing $I$ from eqn. (1) and letting $r^{*}$ be the radius of a single atom, $\Delta G^{*}$ can be found. The relation between the cluster vapor surface energy and the volume energy term is $^{5.8}$

$$
\gamma_{\mathrm{cv}}=\frac{-r^{*} \Delta G_{\mathrm{v}}}{2}
$$

The function $\phi(\theta)$ can be found from the equation $^{5.8}$

$$
\Delta G^{*}=\frac{16 \pi \gamma_{\mathrm{cv}}^{3}}{3 \Delta G_{\mathrm{v}}^{2}} \phi(\theta)
$$

where
$$
\phi(\theta)=\frac{2-\cos \theta+\cos ^{3} \theta}{4} \tag{12}
$$

## 3. NUMERICAL EXAMPLE

As an example we take the deposition from the vapor phase of gold onto vacuum-cleaved NaCl. The experimental data given by Walton et al. $^{7}$ and Stowell $^{2}$ are as follows: $E_{\mathrm{a}}=0.69 \mathrm{eV} ; E_{\mathrm{d}}=0.31 \mathrm{eV} ; N_{0}=4 \times 10^{14} \mathrm{~cm}^{-2} ; v=1.1 \times 10^{12} \mathrm{~s}^{-1}$. For a given set of parameters $(R=1.4 \times 10^{15} \mathrm{~cm}^{-2} \mathrm{~s}^{-1}$ and $T=150^{\circ} \mathrm{C})$ the computation is as follows: eqn. (1) for $I=1$ gives $R_{\text {crit }}=3.869 \times 10^{6} \mathrm{~cm}^{-2} \mathrm{~s}^{-1}$; eqn. (4) gives $T_{\mathrm{s}}=148 \mu \mathrm{s}$; eqn. (3) gives $n_{0}{ }^{*}=575 \mathrm{~cm}^{-2}$; eqn. (7) gives $S=3.595 \times 10^{15}$; eqn. (8) gives $\Delta G_{\mathrm{v}}=-1.278 \times 10^{23} \mathrm{eV} \mathrm{cm}^{-3}$; eqn. (9) for $n_{1}{ }^{*}=R T_{\mathrm{s}}, \sin \theta=1$, a one-atom critical nucleus and $r^{*}=1.4 \AA$ gives $\Delta G^{*}=0.2487 \mathrm{eV}$; eqn. (10) gives $\gamma_{\mathrm{cv}}=8.9 \times 10^{14} \mathrm{eV} \mathrm{cm}^{-2}\left(1432 \mathrm{erg} \mathrm{cm}^{-2}\right)$; eqn. (11) gives $\phi(\theta)=0.339$; finally eqn. (12) gives $\theta=78^{\circ}$.

## 4. EFFECT OF DEPOSITION PARAMETERS

The small-cluster energy data (adsorption energy, activation energy for surface diffusion and atom-substrate vibrational frequency) from different experimenters vary somewhat $^{1,3,10}$. The effect of variations in the empirical values was examined. It was found that the contact angle is a strong function of the adsorption energy and the activation energy for surface diffusion and a rather weak function of temperature and the remainder of the parameters.

## 5. CONCLUSIONS AND REMARKS

The algorithm developed here uses the concept of two-atom stable nuclei. We have avoided assigning any bulk properties to the cluster of a few atoms which was of major concern to previous investigators $^{4,5,13}$. The problem that arises, however, is the limit on physical meaning of extrapolating the macroscopic contact angle to the microscopic scale of a few atoms. The contact angle of a large cluster is generally given by the Young-Dupre relation in terms of surface energy values. Some researchers $^{8,14}$, employing the capillarity theory, have obtained the contact angle and critical radius for several deposition cases. Even if in all cases the value of the critical radius was found to be of atomic size, the investigators still considered it to be legitimate to call it a contact angle without any experimental confirmation. We examined the validity of the present algorithm by comparing it with an experimental investigation which gives the average contact angle of growing caps of gold deposited onto vacuum-cleaved NaCl as $86^{\circ}$ for the same deposition parameters $^{15}$. Although the contact angle was computed for small clusters and the experimental data were obtained from large clusters, the numbers come out reasonably close in comparison with the large difference between the theoretical and measured values presented before $^{8,16}$. The algorithm is applicable to growth modes that involve high mobility of surface atoms on the substrate, e.g. in the systems Ag/NaCl, Ag/KCl and $\mathrm{Ag} / \mathrm{KBr}$ using the data of Robinson and Robins $^{1}$ and the systems $\mathrm{Au} / \mathrm{NaCl}, \mathrm{Au} / \mathrm{KCl}$

and Au/KBr using the data of Stowell². For a high binding energy of the atom to the substrate, *e.g.* for Ag/Si(111), the silver grows in a Stranski-Krastanov (layer-plus-island) mode¹⁷. In this case the interaction of nuclei with the layer requires a modification of the formulae.

REFERENCES

1  V. N. E. Robinson and J. L. Robins, *Thin Solid Films*, 20 (1974) 155.
2  M. J. Stowell, *Thin Solid Films*, 21 (1974) 91.
3  J. A. Venables, *Philos. Mag.*, 27 (1973) 697.
4  K. L. Chopra, *Thin Film Phenomena*, McGraw-Hill, New York, 1969.
5  R. A. Sigsbee and G. M. Pound, *Adv. Colloid Interface Sci.*, 1 (1967) 335.
6  D. Walton, *J. Chem. Phys.*, 37 (1962) 2182.
7  D. Walton, T. N. Rhodin and R. W. Rollins, *J. Chem. Phys.*, 38 (1963) 2698.
8  R. D. Gretz, *Ph.D. Thesis*, Carnegie Institute of Technology, 1963.
9  B. Lewis, *Thin Solid Films*, 1 (1967) 85.
10 A. J. Donohoe and J. L. Robins, *Thin Solid Films*, 33 (1976) 363.
11 L. Yang, C. E. Birchenall, G. M. Pound and M. T. Simnand, *Acta Metall.*, 2 (1954) 462.
12 C. L. McCabe and C. E. Birchenall, *Trans. Am. Inst. Min. Metall. Eng.*, 197 (1953) 707.
13 D. W. Pashley, *Adv. Phys.*, 14 (1965) 327.
14 J. P. Hirth and K. L. Moazed, *Phys. Thin Films*, 4 (1967) 97.
15 K. Reichelt, B. Lampert and H. P. Siegers, *Surf. Sci.*, 93 (1980) 159-174.
16 B. K. Chakraverty and G. M. Pound, *Acta Metall.*, 12 (1964) 851.
17 J. A. Venables, J. Derrien and A. P. Janssen, *Surf. Sci.*, 95 (1980) 411-430.
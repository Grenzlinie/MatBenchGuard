# A study of the critical cluster size for water monolayer clusters on a model AgI basal substrate $^{\text{a)}}$

Richard C. Ward, Barbara N. Hale, and Sergio Terrazas

Department of Physics and Graduate Center for Cloud Physics Research, University of Missouri-Rolla, Rolla, Missouri 65401
(Received 13 September 1982; accepted 20 September 1982)

We present a formalism and estimate a critical cluster size for water monolayer formation on a (rigid) model AgI basal substrate. The formalism is modified from that developed for vapor clusters [B. N. Hale and R. C. Ward, J. Stat. Phys. 28, 487 (1982)] and uses a Metropolis Monte Carlo method developed by Squire and Hoover [J. Chem. Phys. 50, 701 (1969)] to determine (Helmholtz) free energy differences for clusters containing $n$ and $n-1$ molecules. Calculations for clusters of $n=1,2,3,4,6$, and 24 water molecules on a model AgI basal face at 265 K are used in a statistical mechanical formalism which assumes that the adsorbed clusters form a mixture of noninteracting ideal gases; the adsorbed monomer concentration is related to the vapor concentration at the same temperature. At water saturation and 265 K a critical cluster size of $n^{*}=3$ molecules and a steady state nucleation rate (for monolayer formation) of $10^{23}\ \text{cm}^{-2}\text{s}^{-1}$ is predicted. The implications of this for ice nucleation on the model AgI substrate under atmospheric conditions are discussed.

## I. INTRODUCTION

The motivation for this work is to study the critical size of embryos of the new phase (liquid or solid) forming on a substrate exposed to the vapor. The critical cluster has equal probability of gaining or losing one molecule and within the framework of steady state nucleation rate theory can be used to estimate the nucleation rate. $^{1,2}$ Recently, a technique, $^{3}$ originally developed by Bennett, $^{4}$ has been applied to an estimate of the critical cluster size $n^{*}$ for the homogeneous nucleation of argon from the vapor at 60 K-modeled with the Lennard-Jones 6-12 potential. In the present work we use a second technique developed by Squire and Hoover $^{5,6}$ to approximate the critical cluster size for the nucleation of a water monolayer on a model substrate. A $\text{H}_{2}\text{O}$-substrate potential $^{7,8}$ and the $\text{H}_{2}\text{O}-\text{H}_{2}\text{O}$ central force potentials of Stillinger and Rahman $^{9}$ are used to model the equilibrium properties of small monolayer water clusters on the (iodine exposed) basal face of hexagonal AgI. The water molecules are assumed to be rigid but otherwise are allowed to translate and rotate in a fully three dimensional system as they adsorb on the rigid AgI surface. The statistical mechanical formalism assumes that the adsorbed clusters form a mixture of noninteracting ideal gases with each gas consisting of clusters with $n$ molecules. The canonical partition function for the adsorbed cluster includes the $\text{H}_{2}\text{O}$-AgI interaction potential energy. $^{10}$ The monomer concentration on the substrate is related to the monomer concentration in the vapor and areal concentrations of adsorbed clusters are written in terms of the adsorbed monomer concentration. The application of this method to water monolayer formation on the model AgI substrate predicts a critical cluster size of three molecules at 265 K and water saturation. (In this case, water saturation implies a water vapor concentration at equilibrium with a liquid water surface at 265 K.) The corresponding steady state nucleation rate for water monolayer formation on the model substrate is $\simeq 10^{23}\ \text{cm}^{-2}\text{s}^{-1}$.

The formalism for obtaining the adsorbed cluster concentrations and the critical cluster size is given in Sec. II. The model system and the Monte Carlo technique are described in Sec. III and the results of the calculations at 265 K and water saturation are presented in Sec. IV. Comments and conclusions are given in Sec. V.

## II. FORMALISM FOR ESTIMATING CRITICAL CLUSTER SIZE

In the classical steady state nucleation rate formalism, the nucleation rate $J$ for heterogeneous nucleation is given by $^{11}$

$$
J=\left\{\sum_{n=1}^{n>n^{*}}\left[\frac{1}{\Gamma_{n} N_{n}^{s} / A}\right]\right\}^{-1}, \tag{1}
$$

where $\Gamma_{n}$ is the rate at which particles attach to a cluster of size $n$ and $N_{n}^{s}$ is the number of clusters of $n$ molecules on the substrate in the area $A$. To obtain an expression for $N_{n}^{s}$ we assume: (i) that the adsorbed clusters form a mixture of noninteracting ideal gases with each gas consisting of clusters of $n$ molecules; (ii) that the number of clusters of $n$ molecules on the rigid substrate $N_{n}^{s}$ is given by

$$
N_{n}^{s}=\left[N_{1}^{s} / Z^{s}(1)\right]^{n} Z^{s}(n), \tag{2}
$$

where $Z^{s}(n)$ is the canonical partition function for the $n$ cluster on the substrate and includes the substrate cluster interaction potential energy; (iii) that $Z^{s}(n)$ is related to the configurational integral $Q^{s}(n)$ by

$$
Z^{s}(n)=\Lambda^{n} \Lambda_{R}^{n}\left(V 8 \pi^{2}\right)^{n} Q^{s}(n) / n!. \tag{3}
$$

The $\Lambda=(2 \pi m k T / h^{2})^{3 / 2}$, $\Lambda_{R}=\Lambda(I_{1} I_{2} I_{3} / 4 m^{3})^{1 / 2}$, $m$ is the mass of the water molecule, $I_{i}$ is the $i$th principal moment of inertia of the rigid molecule, $k$ is Boltzmann's constant and $h$ is Plank's constant. The configurational integral is defined as

$^{\text{a)}}$This material is based upon work supported by the National Science Foundation under Grant No. ATM80-15790.

---

420
J. Chem. Phys. 78(1), 1 Jan. 1983
0021-9606/83/010420-04$02.10
© 1983 American Institute of Physics

![](./images/812417423721365505_1.jpg)

FIG. 2. Plot of $\lambda^{2/3}\langle\Delta U\rangle$ vs $\lambda^{1/3}$ for a monolayer cluster of $n=6$ water molecules on the model AgI basal substrate at 265 K. $C(6)$ is $-3/(kT)$ times the area under the curve drawn through the data points ($\boldsymbol{\bullet}$).

magnitude and an accurate result for $C(n)$ requires extensive Monte Carlo averaging. For the cluster sizes used in these calculations, however, the positive contribution is $\leq 2.0\%$ of the total area.

The technique of Bennett$^{4}$ is used to check the value of $C$ obtained for $n=6$ molecules. The application of this technique has been discussed. $^{3}$ It differs from that of Squire and Hoover in that two ensembles of particles are required; one ensemble uses $\lambda=1$ and the other ensemble uses a value of $\lambda=0.1$. The $C$ value obtained from the Bennett technique is $-3/(kT)$ times the area under the curve in Fig. 2 from $\lambda=1$ to $\lambda=0.1$. To obtain the correct value of $C$ one must add the contribution from the area under the curve below $\lambda=0.1$. Note that in the case of $n=6$ the latter area is approximately zero and the correction to the Bennett technique result is negligible.

## IV. RESULTS
Values of $C(n)$ for $n=1,2,3,4,6$, and 24 water molecule clusters on the model AgI basal substrate are obtained at $T=265$ K using the technique of Squire and Hoover. The results are shown in Fig. 3 where $C(n)$ is plotted vs $n^{-1/2}$. We plot $C(n)$ in this manner in order to compare the results to a model for $\Delta w^{s}(n)$ discussed below. The uncertainties on this curve indicate the range of $C(n)$ obtained from the maximum and minimum areas under the plot of $\lambda^{2/3}\langle\Delta U\rangle$ vs $\lambda^{1/3}$. The Bennett technique$^{4}$ ($n=6$ and $\lambda=0.1$) gives $C=18\pm 2$ and is consistent with the value $C=17\pm 1$ obtained using the technique of Squire and Hoover.

The solid line in Fig. 3 corresponds to $\ln[(n/V)/$ $(N_{1}^{p0}/V)]=10.5$, and its intersection with the data indicates an approximate value of $n^{*}=3$ at $S=1$ [see Eq. (9)]. A value of $P_{0}=(N_{1}^{p0}/V)kT=2.5$ mm Hg is used to determine $N_{1}^{p0}/V.^{13}$ Some preliminary calculations at $T=298$ K and $S=1$ also indicate a critical cluster size of $n^{*}\simeq 3$. Thus, at water saturation and for $265\leq T\leq$ $\leq 298$ K, the critical cluster size is small and apparently insensitive to temperature.

Using the values of $C(n)$ one can predict an approximate steady state nucleation rate for monolayer formation from Eqs. (1) and (6). To estimate $N_{1}^{s}/A$, we rewrite Eq. (5) as
$$N_{1}^{s}/A=S(N_{1}^{p0}/V)(V/A)_{n=1}\exp C(1). \tag{13}$$

The ratio of the constraining volume to the constraining area $V/A$ is $5.5\times 10^{-8}$ cm for $n=1$, $N_{1}^{p0}/V$ is $9.1\times 10^{16}$ cm$^{-3}$, and $C(1)$ is 10. Thus, for $S=1$, Eq. (13) gives $N_{1}^{s}/A\simeq 10^{14}$ cm$^{-2}$. The rate at which molecules attach to the $n$ cluster is $\Gamma_{n}=2\pi\beta a_{0}n^{1/2}(N_{1}^{s}/A)$, where $\beta N_{1}^{s}/A$ is the flux per unit length of (diffusing, adsorbed) $\mathrm{H}_{2}\mathrm{O}$ monomers onto the cluster perimeter. The $a_{0}$ is approximated by $(\pi\rho_{s})^{-1/2}$, where $\rho_{s}\simeq 10^{15}$ cm$^{-2}$ is a typical molecular density in the monolayer clusters. Using a typical jump distance of $d=3$ A, a diffusion barrier of 2.5 kcal/mol, $^{7}$ and a typical (adsorbed) molecular vibrational frequency of $6\times 10^{12}$ s$^{-1}$ a surface diffusion coefficient, $D_{s}=4d\beta\simeq 5\times 10^{-5}$ cm$^{-2}$s$^{-1}$, can be approximated. Substitution of these numbers and values of $N_{n}^{s}$ [from Eq. (6)] into Eq. (1) give a steady state nucleation rate for monolayer formation on the model substrate of $J\simeq 10^{23}$ cm$^{-2}$s$^{-1}$. This large nucleation rate at water saturation $(S=1)$ indicates that the water monolayer forms rapidly and suggests that the nucleation of ice (or amorphous solid water) on the model substrate occurs after the deposition of one or more water layers.

It is interesting to estimate an effective line tension for the adsorbed clusters and to use the present results to estimate a value for the Helmholtz free energy per molecule in an adsorbed layer. A simple classical cluster model in two dimensions for $\Delta w^{s}(n)$ is $2\pi a_{0}\gamma n^{1/2}/kT$ $-n\ln S+n(f^{s}-\mu)$ where $\gamma$ is an effective line tension $e^{-\mu}=Z^{v}(1)/N_{1}^{p0}$ and $f^{s}$ is the free energy per molecule in a large $(n\rightarrow\infty)$ cluster. Using this model for $\Delta w^{s}(n)$ and Eq. (8) $C(n)$ is predicted to decrease linearly with $n^{-1/2}$ and to provide an estimate of $f^{s}$ as $n\rightarrow\infty$. The present calculations give an effective line tension of $\simeq 10^{5}$ erg/cm and a value of $\simeq-40\pm 5$ for $f^{s}$. This approximate value for $\gamma$ is consistent with line tensions obtained for

![](./images/812417423721365505_2.jpg)

FIG. 3. $C$ vs $n^{-1/2}$ for $T=265$ K. The uncertainties indicate the range $\ln C$ obtained from the maximum and minimum areas under the curves indicated in Eq. (12). The solid line shows $\ln(n/N_{1}^{p0})=10.5$. Its intersections with the data for $C(n)$ locates an approximate value of $n^{*}=3$. The dashed line for $n>6$ indicates a possible straight line fit to the data for large clusters; the dot-dashed line guides the eye through the data points for small values of $n$.

other substances. $^{14}$ However, as can be seen in Fig. $3, \gamma$ (related to the slope of $C$ vs $n^{-1 / 2}$ ) and $f^{s}$ (related to the intercept at $n^{-1 / 2}=0$ ) are subject to the uncer tainties in $C$ for large $n$ . A more extensive study could improve these estimates or provide an argument for a revised classical model for $\Delta w^{s}(n)$ . Since we have been primarily concerned with the critical cluster size (which we find to be small) we have not pursued extensive cal- culations of $C$ for $n>6$ .

## V. COMMENTS AND CONCLUSIONS
In this paper we have used the (Metropolis Monte Carlo) method of Squire and Hoover, $^{5}$ to calculate $\ln \{Q^{s}(n)/Q^{s}(n-1)\}$ for $n$ molecule water cluster adsorbed on a model (rigid) AgI basal substrate at $265 ~K$ . Re sults for $n=1,2,3,4,6$ , and 24 are applied to a modified technique developed for vapor clusters, $^{3}$ and used to estimate a critical adsorbed cluster size $n^{*}=3$ at $265 ~K$  and $S=1$ . Preliminary work at $298 ~K$ indicates that the critical cluster size is insensitive to temperature in the range $265 \leq T \leq 298 ~K$ . However, from Eq. (9) and Fig. 3, one can see that the critical cluster size for monolayer formation is highly supersaturation dependent. At $S=1$ and $T=265 ~K$ the predicted steady state nuclea tion rate for monolayer formation is $\simeq 10^{23} ~cm^{-2} ~s^{-1}$ , with a monomer concentration of $\simeq 10^{14} ~cm^{-2}$ . The large nucleation rate at water saturation implies that the ad- sorbed water monolayer forms rapidly and suggests that questions concerning ice nucleation on the model substrate should be addressed to the structure and sta- bility of two or more water layers. We are presently studying two to eight water layers on the model substrate using periodic boundary conditions for the adsorbed layers. Also in progress are studies of critical cluster size for water adsorbed on a featureless substrate and on the model AgI surface with modified lattice param- eters. The long range goals of this work have been to examine the ice nucleating efficiency of substrates--with application to processes involved in atmospheric ice formation.

$^{1}$ N. H. Fletcher, The Physics of Rainclouds (Cambridge Uni versity, Cambridge, 1969), Chap. 3.
$^{2}$ J. J. Burton and C. L. Briant, in Nucleation Phenomena, edited by A. C. Zettlemoyer (Elsevier, New York, 1977), p.131.
$^{3}$ B. N. Hale and R. C. Ward, J. Stat. Phys. 28, 487 (1982).
$^{4}$ C. H. Bennett, J. Comput. Phys. 22, 245 (1976).
$^{5}$ D. R. Squire and W. G. Hoover, J. Chem. Phys. 50, 701(1969).
$^{6}$ F. F. Abraham, M. R. Mruzik, and G. Marshall Pound, Faraday Discuss. Chem. Soc. 61, 34 (1976); M. Mruzik, F. F. Abraham, and D. E. Schrieber, J. Chem. Phys. 64,481(1976).
$^{7}$ B. N. Hale and J. Kiefer, J. Chem. Phys. 73, 923 (1980).
$^{8}$ R. C. Ward, J. Holdman, and B. N. Hale, J. Chem. Phys.77,3198(1982).
$^{9}$ F. Stillinger and A. Rahman, J. Chem. Phys. 68, 666 (1978).
$^{10}$ B. H. Hale and J. Kiefer, J. Stat. Phys. 12, 437 (1975).
$^{11}$ F. F. Abraham, Homogeneous Nucleation Theory (Academic, New York, 1974), Chap. 5; N. Garcia and J. M. Soler Tor- roja, Phys. Rev. Lett. 47, 186 (1981).
$^{12}$ N. Metropolis, A. W. Rosenbluth, M. N. Rosenbluth, A. H. Teller, and E. Teller, J. Chem. Phys. 21, 1087 (1953).
$^{13}$ B. Smith, Department of Chemical Engineering, Washington, University, St. Louis, Missouri (private communication).
$^{14}$ Navascués and P. Tarazone, J. Chem. Phys. 75, 2441 (1981).
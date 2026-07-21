# Electron density near clean and alkali covered semiconductor surfaces

G. Bigun and Yu. Suchorski

Department of Physics, Technical University of Lviv, Mira St. 12, 290646 Lviv, USSR

Received 21 May 1990; accepted for publication 16 July 1990

The electron density near clean and alkali-covered semiconductor surfaces is calculated using the exact relationship between the electrostatic potential of an adsystem and the exchange-correlation energy of the semiconductor substrate.

The change in the work-function of a semiconductor surface as a function of the alkali adatom concentration is predicted on the basis of the calculated electron density. The inclusion of Coulomb correlation in this system makes it possible to obtain a more realistic description of the variation of the semiconductor surface properties with alkali adsorption.

## 1. Introduction

Our previous calculations of the properties of alkali-covered semiconductor surfaces [1] were carried out using a standard method [2,3]. The use of empirical parameters (electron affinities, e.g. ref. [1]) and taking into account only conduction band electrons (that is, only a small portion of the total number of electrons) are the principal drawbacks of such calculations, since every electron interacts with all the others. Therefore it is desirable to include the electron correlation in these calculations. Indeed, if Coulomb correlations are neglected, the calculation of semiconductor work-function is difficult and some experimental data (such as the weak dependence of the work-function on impurity changes) can be explained with difficulty.

The Inkson model [5,6] does take electron Coulomb correlation into account, and we propose using this model not only for bulk semiconductor calculations [5] but for clean semiconductor surface calculations as well [8,9].

In the Inkson model the valence electrons are considered as a many-electron system with density parameter $r_{\mathrm{s}}$ ($\frac{4}{3} \pi r_{\mathrm{s}}^{3}=\bar{n}^{-1}$), where $\bar{n}$ is the electron density. Many static and dynamic semiconductor properties can be described in terms of the static dielectric function $\epsilon(k)$.

This approach has been successfully applied to metals [10] but only recently to semiconductors [8].

Calculations of the bulk electron distribution have been carried out on the basis of Inkson's interpolation formula for $\epsilon(k)$ [5] but this formula does not agree with Lindhard's expression [10] for $k \rightarrow \infty$. Schultze and Unger [11] have corrected this shortcoming and the currently accepted form is
$$
\begin{aligned}
\epsilon(k)= & 1+(\kappa-1)\left[1+L^{2} k^{2}(\kappa-1)\right]^{-1} \\
& \times\left[1+\frac{3 k^{2}}{4 k_{\mathrm{F}}^{2}}\right]^{-1},
\end{aligned}
$$
where $\kappa$ is the semiconductor static dielectric constant, $k_{\mathrm{F}}$ is the Fermi wave-number, and $L$ is the Thomas-Fermi screening length. Eq. (1) serves as a basis for calculating the energy of the electron system using many-body theory, which can be expressed in the form [12]
$$
\begin{aligned}
E\left(r_{\mathrm{s}}\right)= & \frac{1.105}{r_{\mathrm{s}}^{2}}-\frac{0.4581}{\kappa r_{\mathrm{s}}}+0.042 \frac{\kappa}{\kappa-1} \ln r_{\mathrm{s}} \\
& -0.117\left(\frac{2 \kappa}{\kappa-1}-1\right).
\end{aligned}
$$

The first term represents the kinetic energy, the

second represents the Hartree-Fock exchange energy and the remainder represents the correlation energy for the semiconductor valence electron system.

Eq. (2) takes into account the electron correlation in the valence electron system of the semiconductor. This formula is analogous to the Nosières and Pines [10] interpolation formula in the case of a metal ($r_{\mathrm{s}}=1-6$). It is a direct generalization of many-body theory [10] for the semiconductor valence electron system.

We propose the following: the semiconductor surface bounds the many-electron valence system which is neutralized by the positive background created by the ion charges. This system is characterized by the parameters $r_{\mathrm{s}}$ and $\kappa$, and has ground-state energy $E(r_{\mathrm{s}})$. Our aim is to calculate the electron density $n(x)$ and the work-function $\Phi$ as a function of the alkali adatom concentration. This model has been applied successfully to calculate the electrostatic energy of charges near a clean semiconductor surface [8].

## 2. Uniform positive background model

Consider a semiconductor substrate occupying the region $x<0$, covered by an electropositive adsorbate. We replace the positive cores by the positive continuous charge distribution:

$$
n_{+}(x)=
\begin{cases}
\bar{n}, & x \leqslant 0 \\
\bar{n}_{\mathrm{a}}, & 0<x \leqslant d \\
0, & x>d
\end{cases}
\tag{3}
$$

similar to that used by Lang [13] for the case of a metal, where $\bar{n}=\left(\frac{4}{3} \pi r_{\mathrm{s}}^{3}\right)^{-1}$ is the average positive charge distribution in the substrate, and $\bar{n}_{\mathrm{a}}$ is that in the adlayer of thickness $d$. We consider one-valent adatoms of surface density $N_{\mathrm{a}}=\bar{n}_{\mathrm{a}} d$.

According to the density functional method, all quantities depend on the electron density $n(x)$. The self-consistent electrostatic potential $\phi(x)$ depends on the total charge density $n_{+}(x)-n(x)$ through Poisson's equation in the form

$$
\begin{aligned}
\phi(x)= & \phi(-\infty)+4 \pi \int_{-\infty}^{x} \mathrm{~d} x^{\prime}\left(x^{\prime}-x\right)\left[n\left(x^{\prime}\right)\right. \\
& \left.-n_{+}\left(x^{\prime}\right)\right].
\end{aligned}
\tag{4}
$$

We represent $n(x)$ by a family of exponentials with different slopes on the right and left sides. Using the continuity of $n(x)$ and $n^{\prime}(x)$ at $x=0$ and the electrical neutrality condition

$$
\int_{-\infty}^{\infty} \mathrm{d} x\left[n(x)-n_{+}(x)\right]=0
$$

makes it possible to express the exponential parameters $A, B, \beta_{1}, \beta_{2}$, in terms of $y=\beta_{2} d s$ ($s=\bar{n}_{\mathrm{a}} / \bar{n}$), whence we obtain

$$
n(x)=
\begin{cases}
\bar{n}-A \exp \left(\beta_{1} x\right), & x<0 \\
B \exp \left(-\beta_{2} x\right), & x \geqslant 0
\end{cases}
$$

$$
A=\bar{n} \frac{1-y}{2-y}, \quad B=\bar{n}(2-y)^{-1}
$$

$$
\beta_{1}=\frac{y}{d s(1-y)}, \quad \beta_{2}=\frac{y}{d s}. \tag{5}
$$

The work-function of the adsystem is defined as:

$$
\Phi=\Delta \phi-\mu, \tag{6}
$$

where $\mu$ is the chemical potential in the bulk relative to $\phi(-\infty)$

$$
\mu=\frac{\mathrm{d}(\bar{n} E(\bar{n}))}{\mathrm{d} \bar{n}}=E\left(r_{\mathrm{s}}\right)-\frac{1}{3} r_{\mathrm{s}} \frac{\mathrm{d} E\left(r_{\mathrm{s}}\right)}{\mathrm{d} r_{\mathrm{s}}}, \tag{7}
$$

with $E(r_{\mathrm{s}})$ given by (2).

It only remains to determine the variational parameter $y$, which we shall do on the basis of a sum rule.

## 3. Sum rule

A self-consistent surface structure analysis requires extensive numerical calculations, so that exact first-principles results are of considerable interest. Budd and Vanimenus [15] were the first to make use of such a relation in metal surface theory. They proved that in a jellium model the values of the electrostatic potential at the surface

and well inside the metal are connected by the relation [15]

$$
\phi(0)-\phi(-\infty)=\bar{n} \frac{\mathrm{d} E(\bar{n})}{\mathrm{d} \bar{n}}. \tag{8}
$$

This sum rule was used succesfully in variational metal surface calculation [16]. In order to for- mulate its analogue in the alkali layer-semicon- ductor substrate system, one must consider two features: the dielectric function discontinuity at $x=0$ and the presence of the positive adsorbate density $\bar{n}_{a}$. Also, the energy must correspond to the semiconductor. The sum rule modified in this way is [17]:

$$
\begin{aligned}
& \phi(0)-\phi(-\infty)+s(\phi(d)-\phi(0)) \\
& \quad=\bar{n} \frac{\mathrm{d} E(\bar{n})}{\mathrm{d} \bar{n}}-\frac{1}{\bar{n}} \int_{-\infty}^{\infty}\left(n(x)-n_{+}(x)\right) \phi^{\prime}(x) \mathrm{d} x
\end{aligned} \tag{9}
$$

with $E$ given by (2). Eq. (9) reduces to (8) for $\kappa=1$ (metal) and $s=0$ (no adsorbate) or $s=1$ (extra substrate layer).

## 4. Results and discussion

Let $r_{\mathrm{s}}=2.085$ and $\kappa=16$ (germanium [12]). Then, according to (2) and (7), $E=0.1906, \mu=$ 0.3480 (atomic units). Substituting (4) and (5) into (9) and integrating (9) using (2), we obtain

$$
\begin{aligned}
& \frac{1}{16}(1-y)^{3}-s\left(\mathrm{e}^{-y / s}-1\right) \\
& \quad-\frac{1}{2} y^{2}(2-y)\left(1+\frac{0.9512}{s^{2} d^{2}}\right)+\frac{15}{32} \frac{(1-y)^{4}}{2-y}=0,
\end{aligned} \tag{10}
$$

from which $y$ is determined. From (4), (7) and (8), we obtain

$$
\begin{aligned}
\Phi= & \frac{0.331 d^{2} s^{2}}{y^{2}(2-y)}\left[\frac{1}{16}(1-y)^{3}+1-\frac{1}{2} \frac{y^{2}}{s}(2-y)\right] \\
& -0.348.
\end{aligned} \tag{11}
$$

Hence, once the adsorbate layer thickness $d$ and relative adsorbate surface density $s$ are given, the distribution (4) and work-function can be calcu- lated. The results of calculating $n(x)$ are shown in fig. 1. Fig. 2 shows the calculated work-function versus adsorbate density for different values of the parameter $d$. These curves are similar to those for the metal substrate case, which have been mea- sured experimentally [1,18]. These curves have well defined minimum depending on $d$, i.e. on the adatom size and geometry.

![](./images/812449248481116161_1.jpg)

Fig. 1. Dependences of $n(x) / \bar{n}$ as a function of $x:$ (---) $r_{\mathrm{s}}=2.085, \quad N_{\mathrm{a}}=0 ; \quad(-) \quad r_{\mathrm{s}}=2.085, \quad N_{\mathrm{a}}=6.7 \times 10^{14}$ atoms $/ \mathrm{cm}^{2} ; d=7.13$ at. units.

![](./images/812449248481116161_2.jpg)

Fig. 2. Calculated values of semiconductor $(r_{\mathrm{s}}=2.085, \kappa=16)$ work-function $\Phi$ as a function of adsorbate surface density $N_{\mathrm{a}}$ for different values of the parameter $d:$ (1) $d=7$; (2) $d=6$; (3) $d=5$ at. units.

![](./images/812449248481116161_3.jpg)

Fig. 3. Work-function changes $\Delta \Phi$ as a function of surface density $N_{\mathrm{a}}$: (---) theoretical calculations (fig. 2); (——) experimental data for $\mathrm{Na}-\mathrm{Ge}(100)$ [1].

In comparing these results with experimental data, it is necessary to take into account that including electron Coulomb correlation permits us to obtain the clean semiconductor work-function value of about 5.0 eV, nearly independently of impurity effects (in agreement with experiment [4]). This agreement between theory and experiment is even better than in the metal case [14] (the work-function for the clean metal surface could not be obtained in this way).

We can examine the adsorption calculations by comparing $\Delta \Phi=\phi(0)-\phi\left(N_{\mathrm{a}}\right)$ with experiment [1,18]. Choosing the parameter $d$ on the basis of the location of the work-function minimum, we compare the theoretical and experimental values of $\Delta \phi$ for the $\mathrm{Na}-\mathrm{Ge}(100)$ system in fig. 3, where it is seen that the agreement is good. It is interesting to find the value $N_{\mathrm{a}}$ at which $n_{\mathrm{a}}$ equals the positive charge density in the bulk alkali metal, $n_{\mathrm{a}}^{*}\left(N_{\mathrm{a}}^{*}=n_{\mathrm{a}}^{*} d\right)$. The value obtained, $N_{\mathrm{a}} \cong 6 \times$ $10^{14} \mathrm{~cm}^{-2}$, agrees with the optimal surface density of $\mathrm{Na}$ on $\mathrm{Ge}(100)$, in accordance with the idea of adlayer "metalization" [19].

In conclusion, we find that considering electron Coulomb correlation in the uniform charge background model makes possible a realistic description of the dependence of semiconductor surface properties on adsorbed alkali atoms.

## References
[1] G.I. Bigun, I.D. Nabitovich and Yu.S. Suchorski, Fiz. Tverd. Tela 23 (1981) 2128.
[2] A.W. Rjanov, Electronic Processes on Semiconductor Surface (Nauka, Moscow, 1970).
[3] W.F. Kiselew, Surface Phenomena in Semiconductors and Dielectrics (Nauka, Moscow, 1970).
[4] P.G. Allen and G.W. Gobelli, Surf. Sci. 2 (1964) 402.
[5] I.C. Inkson, J. Phys. C 4 (1971) 591.
[6] I.C. Inkson, J. Phys. C 5 (1972) 2599.
[7] I.C. Inkson, J. Phys. C 6 (1973) L 181.
[8] A.M. Gabovich, L.G. Ilchenko and E.A. Pashitskii, Fiz. Tverd. Tela 21 (1979) 1683.
[9] A.M. Gabovich and A.I. Voitenko, Phys. Status Solidi (b) 110 (1982) 407.
[10] D. Pines, Elementary Excitation in Solids (New York, 1963).
[11] K.R. Schultze and K. Unger, Phys. Status Solidi (b) 66 (1974) 491.
[12] F. Oymerlich and J. Mula, J. Phys. C 9 (1976) 3217.
[13] N.D. Lang, Phys. Rev. B 4 (1971) 4234.
[14] N.D. Lang and W. Kohn, Phys. Rev. B 1 (1970) 4555.
[15] H.F. Budd and I. Vanimenus, Phys. Rev. Lett. 31 (1973) 1218.
[16] G.D. Mahan and W.L. Schaich, Phys. Rev. B 10 (1974) 2647.
[17] G.I. Bigun, G.M. Mikita and Yu.S. Suchorski, Fiz. Elektron. 38 (1989) 105.
[18] G.I. Bigun, I.D. Nabitovich and Yu.S. Suchorski, Izv. Acad. Nauk SSSR 46 (1982) 1256.
[19] K. Wojciechowski, Surf. Sci. 55 (1976) 246.
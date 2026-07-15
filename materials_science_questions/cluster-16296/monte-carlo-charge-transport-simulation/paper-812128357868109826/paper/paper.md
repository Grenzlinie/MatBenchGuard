# Effect of Intersubband Coulomb Interaction on Hot-Electron Transport in Two- and One-Dimensional Electron Systems

This content has been downloaded from IOPscience. Please scroll down to see the full text.

1998 Commun. Theor. Phys. 29 7

(http://iopscience.iop.org/0253-6102/29/1/7)

View [the table of contents for this issue], or go to the [journal homepage] for more

Download details:

IP Address: 130.237.29.138
This content was downloaded on 16/08/2015 at 09:15

Please note that [terms and conditions apply].

Commun. Theor. Phys. 29 (1998) pp. 7-12
© International Academic Publishers

Vol. 29, No. 1, January 30, 1998

# Effect of Intersubband Coulomb Interaction on
Hot-Electron Transport in Two- and One-Dimensional
Electron Systems

DONG Bing and LEI Xiaolin

Shanghai Institute of Metallurgy, Academia Sinica, Shanghai 200050, China

(Received April 26, 1996)

Abstract We study the hot-electron transport properties of model GaAs-based quasi-two-dimensional (quantum-well) and quasi-one-dimensional (quantum wire) systems having two occupied subbands by using the Lei-Ting balance-equations for two types of carriers. Both the intersubband electron-phonon interaction and intersubband Coulomb interaction are taken into account. Our numerical results show that when the electron density is high enough, the intersubband Coulomb interaction is substantially strong in thermalizing the electrons between the different subbands. As a consequence, the one-type-of-carriers model (OTCM) is a good approximation for electron transport. However, in the cases of the lower electron densities, the intersubband Coulomb interaction is not strong enough to fire the electrons in different subbands to share a common electron temperature and a more accurate two-types-of-carriers model (TTCM) must be used for analysis.

PACS numbers: 72.10.-d, 73.20.Dx

Key words: intersubband Coulomb interaction, hot-electron transport

## I. Introduction

Much experimental and theoretical attention has been paid to the transport properties of low-dimensional systems, such as quantum wells and quantum wires, under multisubband occupations of carriers.[¹⁻⁸] In most balance-equation investigations on these problems, electrons in different subbands are assumed to share a common electron temperature, chemical potential and average drift velocity even though an external electric field is added.[⁵⁻⁷] This presumption is based on the rapid thermalization of electrons among different subbands and may not be valid if the electron density is not high enough. Recently, C. Guillemot et al.[²] studied the electron-longitudinal-optical-phonon coupling and intersubband scattering in modulation-doped quantum wells by means of Lei-Ting balance-equation approach, assuming that electrons in the two subbands share a common electron temperature and average drift velocity but have different Fermi energies. WU and his coworkers[⁸] analyzed transport in quantum-wire system considering the lowest two subbands 0, 1 and its degenerate subband -1 occupied, using a description which is similar to the two-types-of-carriers model (TTCM) used to solve the transport problem of multi-valley bulk materials.[⁹] They assumed that the electrons in the 0 and ±1 subbands have their own electron temperatures, drift velocities and Fermi energies respectively. Their calculation, in which intersubband Coulomb interaction was included, showed a little difference from that of the one-type-of-carriers model (OTCM). They concluded that the OTCM is a good approximation for the quantum wires at the carrier density investigated. If this is generally true, the OTCM would be a much more attractive model for the low-dimensional device simulation[¹⁰] than the TTCM because the latter requires a much heavier CPU cost. However, the above favorite result is for a special system with a special carrier densities. The systematic theoretical investigation on the validity of the OTCM for low-dimensional multisubband systems is still lacking.

In principle, if intersubband scatterings, which effectively transfer energy between different subbands, are so strong that carriers are thermalized within a much more shorter time than the average momentum relaxation time under an external electric field, the validity of the OTCM can be established for these systems.[¹¹] The intersubband scatterings, including intersubband electron-impurity, electron-phonon and electron-electron Coulomb interactions, depend strongly on the dimensionality of the system and the density of the carriers.

Therefore it is desirable to systematically investigate the effect of intersubband scatter- ings, especially the intersubband electron-electron Coulomb interaction, on the transport properties for systems of different dimensionality and having different carrier densities of quasi-two-dimensional and quasi-one-dimensional electron systems. We employ the Lei-Ting balance-equation approach of two-types-of-carriers model (TTCM) $^{[9]}$ to treat the GaAs-based model systems having two subbands and composed of two types of carriers. The theoretical framework will be formulated in Sec. II, and the numerical calculation and discussion will be presented in the third section.

## II. Balance Equations for Forces, Energies and Particle Numbers
### 2.1. Quasi-Two-Dimensional Systems
Consider a GaAs quantum-well of width $d$ embedded in $Al_{x} Ga_{1-x} As$ as a model of quasi two-dimensional system. Assuming infinitely deep wells, we can write the electron wave- functions and energies as $\psi_{n k}^{2 D}=(1 / S^{1 / 2}) \zeta_{n}(z) e^{i k \cdot r_{\|}}, \varepsilon_{n k}=\varepsilon_{n}+(\hbar^{2} k^{2} / 2 m^{*})$, where $\varepsilon_{n}(=$  $\pi^{2} n^{2} / 2 m^{*} d^{2})$ is the $n$ th subband energy due to the quantized motion in the $z$ direction and $m^{*}$ the electron effective mass, $S$ is the area of the $2 D$ plane, $k=(k_{x}, k_{y})$ the two dimensional plane wave vector and $r_{\|}=(x, y)$ the $2 D$ coordinate. $\zeta_{n}(z)$ denotes the $n$ th sub band envelope wavefunction. For the lowest two subbands we have $\zeta_{0}(z)=\sqrt{2 / d} \sin (\pi z / d)$, $\zeta_{1}(z)=\sqrt{2 / d} \sin (2 \pi z / d)$.

In the second quantization representation the system can be described by the following Hamiltonian
$$
H=\sum_{n k \sigma} \varepsilon_{n k \sigma} c_{n k \sigma}^{\dagger} c_{n k \sigma}+\frac{1}{2} \sum_{\substack{m^{\prime} m, n^{\prime}, n \\ k, k_{1}, q \\ \sigma, \sigma_{1}}} V_{m^{\prime} m, n^{\prime} n}(q) c_{m^{\prime} k+q \sigma}^{\dagger} c_{n^{\prime} k_{1}-q-\sigma_{1}}^{\dagger} c_{n k_{1} \sigma_{1}} c_{m k \sigma} \quad(1)
$$
with $V_{m^{\prime} m, n^{\prime} n}(q)=(e^{2} / 2 \epsilon_{0} \kappa q) H_{m^{\prime} m, n^{\prime} n}(q)$ and
$$
H_{m^{\prime} m, n^{\prime} n}(q)=\int \mathrm{d} z_{1} \mathrm{~d} z_{2} \zeta_{m^{\prime}}^{*}\left(z_{1}\right) \zeta_{m}\left(z_{1}\right) \zeta_{n^{\prime}}^{*}\left(z_{2}\right) \zeta_{n}\left(z_{2}\right) \mathrm{e}^{-q\left|z_{1}-z_{2}\right|}, \quad(2)
$$
where $\kappa$ is the dielectric constant of GaAs; $q=(q_{x}, q_{y}). H_{m^{\prime} m, n^{\prime} n}$ are the form factors of the electron-electron Coulomb interactions $V_{m^{\prime} m, n^{\prime} n}$ describing the collision between an electron in subband $n$ and an electron in subband $m$, which are scattered into subband $n^{\prime}$ and subband $m^{\prime}$, respectively. They can be divided into three classes. The first class terms, $V_{00,00}$ and $V_{11,11}$, are the intrasubband Coulomb interactions of subbands 0 and 1. The second class terms, $V_{00,11}$ and $V_{11,00}(V_{00,11}=V_{11,00})$ , describe the behavior of the intersubband Coulomb scattering but no exchanging of electrons between different subbands. All other terms constitute the third class, which involves exchanging and transferring of electrons between the two subbands. Due to the orthogonality of the wavefunctions, the third class terms are small, as can be seen in Fig. 1, where the form factors $|H_{m^{\prime} m, n^{\prime} n}(q)|^{2}$ are plotted as function of $q$ . The thick lines represent the former two classes Coulomb form factors and thin lines correspond to those of the third class. The form factors of the third class are at least one order of magnitude smaller than those of other two classes (here $H_{00,01}$ and $H_{01,11}=0$ ). Therefore, we consider only the first and second class Coulomb interactions in our present calculation. The intrasubband interactions $V_{00,00}$ and $V_{11,11}$ are assumed strong enough to establish a unique electron temperature within each subband, and their further roles are treated through the dynamical screening. Our main interest is focused on the effect of the intersubband interactions $V_{00,11}$ and $V_{11,00}$ on hot electron transport properties. We will see that it is these terms that make each subband of the system approach a common electron temperature although we assume that different subbands possess different electron temperatures within the theoretical framework when the electron density is high enough.

Under the influence of a uniform electric field $E$ parallel to $z$-direction, balance equationsfor force, energy, and particle number in a steady-transport state are $^{[9]}$ 
$$N_{0} e \boldsymbol{E}+\boldsymbol{F}_{0}\left(v_{0}\right)+\boldsymbol{F}_{p}^{01}\left(v_{0}, v_{1}\right)+\boldsymbol{F}_{01}\left(v_{0}-v_{1}\right)=0, \quad(3)$$

$$N_{1} e \boldsymbol{E}+\boldsymbol{F}_{1}\left(v_{1}\right)+\boldsymbol{F}_{p}^{10}\left(v_{0}, v_{1}\right)-\boldsymbol{F}_{01}\left(v_{0}-v_{1}\right)=0,\qquad(4)$$

$$v_{0} \cdot \boldsymbol{F}_{0}\left(v_{0}\right)+W_{0}\left(v_{0}\right)+W_{p}^{01}\left(v_{0}, v_{1}\right)+W_{01}\left(v_{0}-v_{1}\right)=0,\qquad(5)$$

$$v_{1} \cdot \boldsymbol{F}_{1}\left(v_{1}\right)+\left(v_{0}-v_{1}\right) \cdot \boldsymbol{F}_{01}\left(v_{0}-v_{1}\right)+W_{1}\left(v_{1}\right)+W_{p}^{10}\left(v_{0}, v_{1}\right)-W_{01}\left(v_{0}-v_{1}\right)=0,\qquad(6)$$

$$X\left(v_{0}, T_{0 e}, \mu_{0}, v_{1}, T_{1 e}, \mu_{1}\right)=0.\qquad(7)$$

$N_{0}, v_{0}$ and $N_{1}, v_{1}$ are particle numbers and drift velocities of electrons in subbands 0 and 1 , respectively. $\boldsymbol{F}_{i}$ and $W_{i}(i=0,1)$ denote the frictional forces and energy-loss rates of electrons in subband $i$ due to intrasubband interactions, while $\boldsymbol{F}_{p}^{i j}$ and $W_{p}^{i j}(i, j=0,1)$ represent these terms due to intersubband electron-phonon interactions. $X$ function in Eq. (7) represents the rate of change of the particle number of the subband 0 due to intersubband electron-phonon couplings. Their detailed expressions can be found in Ref. [9] and we do not rewrite them here for simplicity. $\boldsymbol{F}_{01}$ and $W_{01}$, the force and energy-loss rate of the subband 0 due to intersubband Coulomb interaction, are terms of our main interest in this paper and are given by Eq. (A1) in the Appendix. Equations (3) $\sim(7)$, together with the constraint $N_{0}+N_{1}=N$ and the relations $N_{i}=\sum_{k \sigma} f((\varepsilon_{i k}-\mu_{i}) / T_{i e})$ with $(i=0,1),(f(x)=1 /(\exp (x)+1)$ represents the Fermi-Dirac distribution function), form a complete set of equations to determine the steady-state values of $v_{0}, v_{1}, T_{0 e}, T_{1 e}, \mu_{0}, \mu_{1}$ for given electric field $E$ , lattice temperature and total electron density $N$ .

![](./images/812128357868109826_1.jpg)

Fig. 1. Form factors of $e$-$e$ Coulomb interactions for $Al_xGa_{1-x}$As-GaAs quasi-2D quantum well with width 50 nm versus the plane wave vector $q$ are plotted. The thick solid line stands for $|H_{00,00}(q)|^{2}$ , the dashed line for $|H_{11,11}(q)|^{2}$ and the dotted-dashed line for $|H_{00,11}(q)|^{2}$ . Thin solid curves denote form factors of the third class of the $e$-$e$ Coulomb interactions.

### 2.2. Quasi-One-Dimensional System
We choose a cylinder GaAs quantum wire of radius $\rho$ embedded in $Al_{x} Ga_{1-x}$ As as model of quasi-1D system. The wavefunction and the energy of the quantum wire of length $L_{z}$ are $\psi_{n m k_{z}}^{1 D}=(1 / L_{z}^{1 / 2}) e^{i k_{z} z} \zeta_{n m}(z), \varepsilon_{n m k_{z}}=(k_{z}^{2} / 2 m^{*})+\varepsilon_{n m}$ . $\zeta_{n m}(z)$ is the envelope wavefunctions and $\varepsilon_{n m}$ is the subband energy due to the confinement. In the following, we consider only the ground subband $n=0, m=1$ and next two degenerate subbands: $n=1, m=1$ and $n=-1$ , m = 1, having wavefunctions and eigenenergies

$$\zeta_{01}\left(r_{\|}\right)=C_{1}^{0} J_{0}\left(x_{1}^{0} r_{\|} / \rho\right), \quad \zeta_{ \pm 11}\left(r_{\|}\right)= \pm C_{1}^{ \pm 1} J_{1}\left(x_{1}^{1} r_{\|} / \rho\right) \mathrm{e}^{ \pm \mathrm{i} \phi},\qquad(8)$$

$$
\varepsilon_{n m}=\left(x_{m}^{|n|}\right)^{2} / 2 m^{*} \rho^{2},
\tag{9}
$$
where $C_{m}^{n}=1 / \sqrt{\pi} y_{m}^{n} \rho$ is the normalization factor, $x_{m}^{|n|}$ is the $m$ th zero of the $n$th-order Bessel function, i.e. $J_{n}\left(x_{|n|}\right)=0$ and $y_{m}^{n}=J_{|n|+1}\left(x_{m}^{|n|}\right)$. The difference from the quasi-2D systems is that the $n=1$ subband has a degenerate one $n=-1$. Since $m=1$ for these three subbands, we omit this subscript for simplicity. In the framework of balance-equation approach of TTCM, the two degenerate subbands share a unique electron temperature, drift velocity and Fermi energy which may be different from those of the subband $n=0$. The electron Hamiltonian reads

$$
\begin{aligned}
H= & \sum_{n k_{z} \sigma} \varepsilon_{n k_{z} \sigma} c_{n k_{z} \sigma}^{\dagger} c_{n k_{z} \sigma}+\frac{1}{2} \times \\
& \sum_{\substack{m^{\prime} m, n^{\prime} n \\
k_{z}, k_{z}^{\prime}, q_{z} \\
\sigma, \sigma^{\prime}}} K_{m^{\prime} m, n^{\prime} n}\left(\left|q_{z}\right|\right) c_{m^{\prime} k_{z}+q_{z} \sigma}^{\dagger} c_{n^{\prime} k_{z}^{\prime}-q_{z}-\sigma^{\prime}}^{\dagger} c_{n k_{z}^{\prime} \sigma^{\prime}} c_{m k_{z} \sigma},
\end{aligned}
\tag{10}
$$

where

$$
K_{m^{\prime} m, n^{\prime} n}\left(\left|q_{z}\right|\right)=\frac{\mathrm{e}^{2}}{4 \pi \varepsilon_{0} \kappa} \int \mathrm{d} \boldsymbol{r}_{\|} \mathrm{d} \boldsymbol{r}_{\|}^{\prime} \zeta_{m^{\prime}}^{*}\left(\boldsymbol{r}_{\|}\right) \zeta_{m}\left(\boldsymbol{r}_{\|}\right) \zeta_{n^{\prime}}^{*}\left(\boldsymbol{r}_{\|}^{\prime}\right) \zeta_{n}\left(\boldsymbol{r}_{\|}^{\prime}\right) K_{0}\left(\left|q_{z}\right|\left|\boldsymbol{r}_{\|}-\boldsymbol{r}_{\|}^{\prime}\right|\right)
\tag{11}
$$

is the Coulomb interaction. $K_{0}(x)$ is the modified Bessel function of zeroth order. As in the case of the quasi-2D systems, the inter-subband Coulomb scatterings $K_{00,11}\left(=K_{00, \overline{1} \overline{1}}\right)$ are our main concern terms. The equations of force, energy and particle number balance in quantum wire system under a uniform electric field $\boldsymbol{E}$ along the $z$-direction are as follows:

$$
N_{0} e \boldsymbol{E}+\boldsymbol{F}_{0}\left(v_{0}\right)+2 \boldsymbol{F}_{p}^{01}\left(v_{0}, v_{1}\right)+2 \boldsymbol{F}_{01}\left(v_{0}-v_{1}\right)=0,
\tag{12}
$$

$$
2 N_{1} e \boldsymbol{E}+2 \boldsymbol{F}_{1}\left(v_{1}\right)+2 \boldsymbol{F}_{p}^{10}\left(v_{0}, v_{1}\right)-2 \boldsymbol{F}_{01}\left(v_{0}-v_{1}\right)=0,
\tag{13}
$$

$$
v_{0} \cdot \boldsymbol{F}_{0}\left(v_{0}\right)+W_{0}\left(v_{0}\right)+2 W_{p}^{01}\left(v_{0}, v_{1}\right)+2 W_{01}\left(v_{0}-v_{1}\right)=0,
\tag{14}
$$

$$
v_{1} \cdot 2 \boldsymbol{F}_{1}\left(v_{1}\right)+\left(v_{0}-v_{1}\right) \cdot 2 \boldsymbol{F}_{01}\left(v_{0}-v_{1}\right)+2 W_{1}\left(v_{1}\right)+2 W_{p}^{10}\left(v_{0}, v_{1}\right)-2 W_{01}\left(v_{0}-v_{1}\right)=0, \quad(15)
$$

$$
X\left(v_{0}, T_{0 e}, \mu_{0}, v_{1}, T_{1 e}, \mu_{1}\right)=0
\tag{16}
$$

and $N_{0}+2 N_{1}=N$. Here, $\boldsymbol{F}, W$ and $X$ functions have the same meanings as those of the above subsection. The expressions of $\boldsymbol{F}_{01}$ and $W_{01}$ for quantum wire system are given by Eq. (A2) in the Appendix.

### III. Numerical Results and Discussions

Numerical calculations were performed for GaAs-based quasi-2D quantum-well and quasi-1D quantum-wire systems with several different electron densities at lattice temperature $T=80 \mathrm{~K}$. Contributions of electron-impurities scattering, intra- and inter-subband electron-phonon scatterings (including polar-optical-phonon, deformation potential and piezoelectric couplings) and the inter-subband Coulomb interaction are included in the calculations. The material parameters used here for GaAs-AlGaAs are the following: density $d=5.31 \mathrm{~g} / \mathrm{cm}^{3}$, effective mass $m=0.069 m_{e}$, transverse sound velocity $v_{s l}=2.48 \times 10^{5} \mathrm{~cm} / \mathrm{s}$, longitudinal sound velocity $v_{s t}=5.29 \times 10^{5} \mathrm{~cm} / \mathrm{s}$, longitudinal-optical-phonon energy $\Omega_{\mathrm{LO}}=35.4 \mathrm{meV}$, low-frequency dielectric constant $\kappa=12.9$, optical dielectric constant $\kappa_{\infty}=10.8$, acoustic deformation potential $\Xi=8.5 \mathrm{eV}$, piezoelectric constant $e_{14}=1.41 \times 10^{9} \mathrm{~V} / \mathrm{m}$.

In Figs 2 and 3, we plot the calculated normalized electron temperatures $T_{e} / T$ and drift velocities $v_{0}$ and $v_{1}$ of two subbands as functions of the electric field for $\mathrm{Al}_{x} \mathrm{Ga}_{1-x}$As-GaAs quantum well systems of a well width $50 \mathrm{~nm}$ having carrier sheet densities $N_{s}=0.1$ and $5.0 \times 10^{11} \mathrm{~cm}^{-2}$, respectively. The solid curves are the values of the ground subband 0, long-dashed curves are those of the first excited subband 1 and shot-dashed lines correspond to the average drift velocities $v_{d}=\left(N_{0} v_{0}+N_{1} v_{1}\right) / N$. Generally, the electron temperatures and drift velocities in different subbands are not equal due to finiteness of the carrier intersubband Coulomb interaction. The difference of these quantities of different subbands depends on the

gap between the ground and first excited subbands and on the electron density. In the present paper, we will focus our attention on the effects of the electron density. It is believed that the higher the electron density the stronger the intercarrier Coulomb interaction. It is easily seen from Fig. 2 that in the case of electron density $N_s = 0.1 \times 10^{11}\ \text{cm}^{-2}$, there are great disparities of both the electron temperatures and drift velocities between two subbands. Figure 3 apparently shows that in the case of higher electron density, $N_s = 5.0 \times 10^{11}\ \text{cm}^{-2}$, however, these disparities are largely reduced. Similar conclusion can be drawn from the results of quantum-wire systems. In Figs 4 and 5 we plot electron temperatures and drift velocities of separate subbands, as well as the average drift velocity $v_d$ defined by $v_d = (N_0v_0 + 2N_1v_1)/N$ for quasi-1D quantum wires with radius $\rho = 9\ \text{nm}$ having electron line densities $N_l = 2.0$ and $5.0 \times 10^6\ \text{cm}^{-1}$, respectively. Significant change of electron temperatures and drift velocities behavior occurs in the quasi-1D case when the electron line density increases from $N_l = 2.0 \times 10^6\ \text{cm}^{-1}$ to $N_l = 5.0 \times 10^6\ \text{cm}^{-1}$.

In Figs 2 and 3, we plot the calculated normalized electron temperatures $T_e/T$ and $v_0, v_1$ of two subbands as functions of the electric field for $\text{Al}_x\text{Ga}_{1-x}\text{As-GaAs}$ quantum well systems of a well width $50\ \text{nm}$ having carrier sheet densities $N_s = 0.1$ and $5.0 \times 10^{11}\ \text{cm}^{-2}$, respectively. The solid curves are the values of the ground subband 0, long-dashed curves are those of the first excited subband 1 and shot-dashed lines correspond to the average drift velocities $v_d = (N_0v_0 + N_1v_1)/N$.

![](./images/812128357868109826_2.jpg)

Fig. 2. $T_e/T$ and $v_0, v_1$ are shown as a function of electric field at $T = 80\ \text{K}$ with $N_s = 0.1 \times 10^{11}\ \text{cm}^{-2}$, $d = 50\ \text{nm}$.

![](./images/812128357868109826_3.jpg)

Fig. 3. The same as Fig. 2 but for electron sheet density $N_s = 5.0 \times 10^{11}\ \text{cm}^{-2}$.

![](./images/812128357868109826_4.jpg)

Fig. 4. This is the result of the quasi-1D quantum wire with radius $9\ \text{nm}$ for electron line density $N_l = 2.0 \times 10^6\ \text{cm}^{-1}$.

![](./images/812128357868109826_5.jpg)

Fig. 5. The same as Fig. 4 but for electron line density $N_l = 5.0 \times 10^6\ \text{cm}^{-1}$

All these figures demonstrate that the intersubband Coulomb interaction plays a decisive

role in transport of systems having two occupied subbands. If the electron density is low, the intersubband Coulomb interactions are not strong enough to rapidly thermalize electrons among the different subbands. It is thus natural that electrons in different subbands possess different electron temperatures, drift velocities and Fermi levels when an external electric field is applied. This implies that the presumption of the OTCM is invalid for the case and the TTCM must be used to solve the transport problems for systems of low electron density. On the contrary, in the case of the high electron density, the electron thermalization between the first and second subbands is so rapid due to the strong intersubband Coulomb scatterings that electrons dwelling within different subbands share a common electron temperature after the system comes to a stationary state under a uniform external electric field. Obviously, OTCM is a good approximation for such systems. Therefore, it is the electron density that is the decisive factor of the validity of the simplified OTCM.

## Appendix
The force and energy-loss rate of electrons within subband 0 due to inter-subband Coulomb interaction are
$$
F_{01}^{2 D}=\sum_{q}\left|V_{00,11}(q)\right|^{2} q \int_{-\infty}^{\infty} \frac{\mathrm{d} \omega}{\pi}\left[n\left[\frac{\omega}{T_{0 e}}\right]-n\left[\frac{\omega-\omega_{01}}{T_{1 e}}\right]\right] \Pi_{2}^{(0)}(q, \omega) \Pi_{2}^{(1)}\left(q, \omega-\omega_{01}\right),
$$
$$
\begin{aligned}
W_{01}^{2 D}= & \sum_{q}\left|V_{00,11}(q)\right|^{2} \int_{-\infty}^{\infty} \frac{\mathrm{d} \omega}{\pi} \omega\left[n\left[\frac{\omega}{T_{0 e}}\right]-n\left[\frac{\omega-\omega_{01}}{T_{1 e}}\right]\right] \times \\
& \Pi_{2}^{(0)}(q, \omega) \Pi_{2}^{(1)}\left(q, \omega-\omega_{01}\right)
\end{aligned}
$$
with $\omega_{01} \equiv q \cdot\left(v_{0}-v_{1}\right)$, and
$$
F_{01}^{1 D}=\sum_{q_{z}}\left|K_{00,11}\left(\left|q_{z}\right|\right)\right|^{2} q_{z} \int_{-\infty}^{\infty} \frac{\mathrm{d} \omega}{\pi}\left[n\left[\frac{\omega}{T_{0 e}}\right]-n\left[\frac{\omega-\omega_{01}}{T_{1 e}}\right]\right] \Pi_{2}^{(0)}\left(q_{z}, \omega\right) \Pi_{2}^{(1)}\left(q_{z}, \omega-\omega_{01}\right),
$$
$$
\begin{aligned}
W_{01}^{1 D}= & \sum_{q_{z}}\left|K_{00,11}\left(\left|q_{z}\right|\right)\right|^{2} \int_{-\infty}^{\infty} \frac{\mathrm{d} \omega}{\pi} \omega\left[n\left[\frac{\omega}{T_{0 e}}\right]-n\left[\frac{\omega-\omega_{01}}{T_{1 e}}\right]\right] \times \\
& \Pi_{2}^{(0)}\left(q_{z}, \omega\right) \Pi_{2}^{(1)}\left(q_{z}, \omega-\omega_{01}\right),
\end{aligned}
$$
with $\omega_{01}=q_{z}\left(v_{0}-v_{1}\right)$.

In Eqs (A1) and (A2) $\Pi_{2}^{(i)}(q, \omega)$ and $\Pi_{2}^{(i)}\left(q_{z}, \omega\right)$ are the imaginary parts of the electron density-density correlation functions of the subband $i$ at temperature $T_{i e}$ for quasi-2D and quasi-1D systems, respectively. $n(x)$ is the Bose distribution function $(n(x)=1 /(\exp (x)-1))$.

## References
[1] C. Guillemot, F. Clérot, P. Auvry, M. Baudet, M. Gauneau and A. Regreny, Semicond. Sci. Technol. 4 (1989) 1142.
[2] C. Guillemot, F. Clérot and A. Regreny, Phys. Rev. B46 (1992) 10152.
[3] T. Yamada and J. Sone, Phys. Rev. B40 (1989) 6265.
[4] K.W. Kim, M. Stroscio, A. Bhatt, R. Mickevicius and V.V. Mitin, J. Appl. Phys. 70 (1991) 319.
[5] X.L. LEI, J.Q. ZHANG, J.L. Birman and C.S. TING, Phys. Rev. B33 (1986) 4382.
[6] X.F. WANG and X.L. LEI, Phys. Stat. Sol. (b) 175 (1993) 433.
[7] X.F. WANG and X.L. LEI, Phys. Rev. B47 (1993) 16612.
[8] M.W. WU, Z.G. YU and X.L. LEI, Phys. Stat. Sol. (b) 183 (1994) 529.
[9] X.L. LEI, D.Y. XING, M. LUI, C.S. TING and J.L. Birman, Phys. Rev. B36 (1987) 9134.
[10] C. Sala, W. Magnus and K. De Meyer, J. Appl. Phys. 69 (1991) 7689.
[11] L.Y. CHEN, C.S. TING and N.J.M. Horing, Phys. Rev. B42 (1990) 1129.
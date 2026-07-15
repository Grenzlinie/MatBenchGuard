# Energy transport model with full band structure for GaAs electronic devices

Matt Grupen

Published online: 28 May 2011
© Springer Science+Business Media LLC 2011

Abstract Electronic band structure is incorporated into a versatile energy transport model that treats heat flow be- tween mobile electron ensembles with the thermodynamic identity for ideal gases instead of an electron thermal con- ductivity. This alleviates the closure issue common to ther- mal conductivity models and is amenable to different forms of charge gas transport. This flexibility allows the model to accommodate band dispersions typical of semiconductors. A simulation scheme and the device equations for a gen- eralized band structure are presented. The model is then implemented for GaAs using a band structure calculated with the empirical pseudopotential method. Comparisons to Monte Carlo for certain bulk GaAs test cases indicate that the model may capture hot electron effects with sufficient accuracy and reduced computational cost suitable for larger scale device simulation and design.

Keywords Charge transport model · Ideal Fermi gas · Boltzmann equation

## 1 Introduction

Electron transport in semiconductors and semiconductor de- vices can be simulated in many different ways that vary con- siderably in their levels of physical detail as well as their computational efficiency. One extreme might be a rigorous, fully quantum mechanical, many body approach which is very computationally intensive and, therefore, restricted to microscopic scales and a relatively small number of par- ticles. At the other extreme could be an equivalent circuit model that replaces the transport physics with lumped pa- rameters, enabling numerical solutions efficient enough for large scale integrated circuit simulation. On the discrete mi- croelectronic component level, models lie somewhere be- tween these extremes. But even within this restricted scope, different models offer similar trade-offs between physical theory and numerical efficiency.

One approach to semiconductor device simulation is the semiclassical ensemble Monte Carlo (EMC) method. This highly effective algorithm tracks a number of individual electrons as each moves classically in an electromagnetic field and scatters quantum mechanically between states in momentum space. The stochastic procedures used to de- termine the time an electron drifts in the field, the type of scattering process it encounters, and its final state automati- cally produce electron distribution functions that satisfy the Boltzmann transport equation (BTE) [1]. In this way, EMC is a powerful mathematical representation of how electrons move within their phase space. Full electronic band struc- ture has been a common feature in EMC simulations since the pioneering work by Shichijo and Hess [2] and has since been identified as a principal determinant of the method’s accuracy [3]. However, the features that make EMC so pow- erful also make it highly computer intensive. Large num- bers (on the order of $10^4$) of electrons must be considered to reduce statistical noise. Likewise, stochastic scattering re- quires stepping through time in increments commensurate with the fastest scattering mechanisms. Both these concerns can increase CPU time. Furthermore, if full band structure is combined with anisotropic scattering, the selection of fi- nal states for all possible initial states in momentum space can lead to large memory requirements. As a result, apply- ing EMC to macroscopic simulation of realistic semicon-

M. Grupen ( )
Air Force Research Laboratory, 2241 Avionics Circle,
Wright-Patterson AFB, OH 45433, USA
e-mail: Matthew.Grupen@wpafb.af.mil

![](./images/811657061405294593_1.jpg)

ductor device geometries requires additional refinements of the method, such as optimizing the trade-offs between CPU and memory requirements [4] or adapting it for high perfor- mance parallel computing platforms [5].

A great deal of computation can be spared when the di- mensionality of the distribution function is reduced by ex- panding it into a series of spherical harmonics [6]. When inserted into the BTE, the coefficients of this spherical har- monic expansion (SHE) can be obtained by solving deter- ministic differential equations, avoiding stochastic methods' statistical noise issues. This approach has achieved accurate solutions for electron transport in semiconductors, includ- ing transistor level problem domains [7-10]. However, de- spite its reduced dimensionality compared with EMC, SHE still discretizes electron energy and can require very large amounts of computer memory, particularly when higher or- der harmonics are included for improved accuracy. There- fore, as with EMC, research on SHE continues to improve its computational efficiency and its utility for larger scale device simulation [11].

Still further reductions in computational cost have been achieved by replacing the discretization of momentum and energy with an assumed functional form for the electron dis- tribution, often a heated Maxwellian or Fermi-Dirac distri- bution. Defining the distribution then requires charge and energy conservation relations, expressed in terms of particle and energy fluxes. Approaches of this sort include hydro- dynamic models and are described more broadly as energy transport models. Their implementations of charge and en- ergy densities and fluxes vary considerably; Grasser et al. have provided a detailed review [12]. However, since these models presume a shape of the electron energy spectra, they all require an explicit treatment of heat flow between the ensembles of mobile electrons [13], something implicitly in- cluded in the momentum and energy discretizations of EMC and SHE, respectively. Furthermore, virtually all these mod- els represent this heat flow with some form of electron ther- mal conductivity and an electron temperature gradient. It is not completely clear why this interpretation is so ubiquitous, but it may be due to the seminal work by Stratton who chose it based on the Wiedemann-Franz-Lorentz law [14]. This use of an electron thermal conductivity may contribute to the closure problem that confronts many energy transport mod- els.

The closure issue refers to matching the numbers of equa- tions and unknowns when charge and energy conservation are derived from moments of the BTE. Inserting an as- sumed distribution function and integrating over all electron momenta is the zeroth moment of the BTE that conserves charge density. Multiplying by electron velocity and then in- tegrating over momentum is the first moment that produces the electron flux. The second and third moments produce energy conservation and kinetic energy flux, respectively.
![](./images/811657061405294593_2.jpg)

However, since the total energy flux also requires the heat flow, an additional equation is required. Expressing this heat flow by an electron thermal conductivity and temperature gradient may require additional moments of the BTE to suf- ficiently define the thermal conductivity, improve accuracy, and ensure numerical stability. This is one of the reasons moments of the BTE can produce fewer equations than un- knowns, which must be eliminated through appropriate clo- sure relations [12]. The choice of closure relation has im- portant implications for many facets of the model, includ- ing the total number of BTE moments it requires, its ability to incorporate energy band dispersions and scattering pro- cesses, as well as its accuracy and robustness. As a result, the closure issue has greatly increased the diversity of en- ergy transport models and has persisted as an active area of research [15, 16].

More recently it has been proposed that the closure prob- lem could be alleviated by replacing electron thermal con- ductivity with an alternative view of heat flow [13]. When any energy transport model computes charge flux from mo- ments of the BTE, it assumes electrons at one point in space, with a particular electron density and temperature, move to another point with different density and temperature. The thermalization process by which electrons from the initial ensemble assume the temperature of the final ensemble is the nature of heat flow. The amount of heat required can be computed from the thermodynamic identity for an ideal gas at constant volume [17],
$$
k_{B} T \Delta \sigma=\Delta E_{n}-F \Delta n,\qquad(1)
$$
where $k_{B}$ is Boltzmann's constant, $T$ is the electron gas tem perature, $\sigma$ is the entropy, $E_{n}$ is its kinetic energy density, $F$ is its chemical potential (Fermi level), and $n$ is its particle density. Integrating both sides from their initial to their final values gives the total heat $Q$ required to effect the tempera ture change,
$$
Q=E_{n}\left(T_{f}\right)-E_{n}\left(T_{i}\right)-F\left[n\left(T_{f}\right)-n\left(T_{i}\right)\right].\qquad(2)
$$

It has been posited [13] that any real space transport mech- anism that involves electron and energy exchanges between two Fermi gases, expressed as integrals over their distribu- tion functions, could be used to determine the correspond- ing heat flow. For example, if such an electron flux $J$ and the corresponding kinetic energy flux $K$ between two Fermi gases 1 and 2 can be expressed as,
$$
\begin{aligned}
J^{1 \rightarrow 2} & =J_{1}\left(T_{1}\right)-J_{2}\left(T_{2}\right) \\
K^{1 \rightarrow 2} & =K_{1}\left(T_{1}\right)-K_{2}\left(T_{2}\right),
\end{aligned}\qquad(3)
$$
then the corresponding heat flow $H$ is given by,

$$
\begin{aligned}
H^{1 \rightarrow 2}= & K_{1}\left(T_{1}\right)-K_{1}\left(T_{2}\right)-F_{1}\left[J_{1}\left(T_{1}\right)-J_{1}\left(T_{2}\right)\right] \\
& -K_{2}\left(T_{2}\right)+K_{2}\left(T_{1}\right)+F_{2}\left[J_{2}\left(T_{2}\right)-J_{2}\left(T_{1}\right)\right]. \quad(4)
\end{aligned}
$$

Closure is not an issue because all the fluxes needed by the thermodynamic identity are already determined by the first and third moments of the BTE; they are simply recomputed at different temperatures. This interpretation of heat was applied to both thermionic emission and moments of the BTE and was used to simulate a GaAs metal semiconductor field effect transistor [13]. The simulations proved numerically robust for a full range of bias conditions, and the resulting device currents showed a strong dependence on the electronic band structure available to the Fermi ensembles. This paper exploits the flexibility and robustness of the thermodynamic identity interpretation of heat flow to further investigate the role of the electron phase space and the potential accuracy of a charge transport model based on the kinetics of Fermi gases.

First, a method for applying Fermi kinetics to an arbitrary electronic band structure is proposed. This includes a simulation strategy and the equations for both real space transport and momentum space scattering. A procedure for extracting quantities required by the transport equations from electronic band structure isosurfaces is then presented. The resulting model is used to compute the average electron drift velocity in bulk GaAs and to simulate a GaAs $n^{+} n n^{+}$ structure. The solutions are compared with results from the literature produced by full band EMC.

## 2 Fermi-Dirac dynamics for arbitrary band structure

To model electron dynamics in a semiconductor device, the device geometry is tessellated with a mesh of discrete points in real space. Each real space point can be assigned a set of electron chemical potentials and temperatures that specify separate Fermi distributions for different regions of momentum space. To illustrate, Fig. 1 shows a schematic diagram in $\boldsymbol{k}$ space representing a semiconductor conduction band. Although energy bands for different semiconductors vary in many respects (e.g. the positions of the local minima and maxima, their curvatures, anisotropy, etc.), they generally form separate valleys, each containing closely spaced states whose energies are approximately continuous functions of momentum. Each continuous valley allows electrons to accelerate gradually in an electromagnetic field through small increments in their momenta and energies and, therefore, provides a natural set of states to which a Fermi distribution function can be assigned.

![](./images/811657061405294593_3.jpg)

Fig. 1 Schematic representation of a semiconductor electronic band structure consisting of three valleys in momentum space. Different Fermi-Dirac distributions $f$ are assigned to different portions of the valleys according to the energies of the valley minima and the lattice phonons

In addition to the gradual transitions between states within a valley induced by an applied field, electrons can also make more abrupt transitions between states through scattering mechanisms, particularly phonon scattering, including intervalley processes. As a result, electrons in the $\Gamma$ valley of Fig. 1 with energies greater than one phonon energy $\hbar \omega$ below the $L$ valley have an additional degree of freedom compared to the $\Gamma$ valley electrons at lower energies. This tends to drive the $\Gamma$ electrons in these two energy ranges significantly out of equilibrium and suggests they be assigned separate Fermi distributions. Similar arguments can be made for $\Gamma$ and $L$ valley electrons within a phonon energy of the $X$ valley. Therefore, a conduction band represented by $N$ valleys can be assigned $N^{2}-N(N-1) / 2$ separate Fermi distributions to approximate the occupation probabilities in momentum space.

Given a semiconductor structure suitably represented by a mesh of real space points, each containing a set of Fermi distributions representing the electron occupation of momentum space, the exchange of particles and energy between the separate Fermi gases must be considered to model the electron dynamics. This includes real space transport between gases at different mesh points as well as momentum space transport between gases occupying different parts of the energy band dispersion. To make this tractable, real space transport within a particular material can be assumed to occur only between Fermi distributions occupying the same regions of momentum space. Then, at each point in real space, the distribution functions defined there can exchange particles and energy through scattering in momentum space. To implement this model, these real and momentum space transport mechanisms must be derived in terms of Fermi distributions occupying nonparabolic energy valleys.

In the quasistatic approximation (i.e. no rotational electric and magnetic fields) electric field variations can be related to the spatial charge distribution through Gauss's law,

$$
\nabla \cdot \epsilon \boldsymbol{E}=q\left(p-n+N_{D}^{+}-N_{A}^{-}\right),
$$

![](./images/811657061405294593_4.jpg)

where $\epsilon$ is the dielectric constant, $\boldsymbol{E}$ is the conservative electric field, $q$ is the electron charge magnitude, and $n$, $p$, $N_D^+$, and $N_A^-$ are the electron, hole, ionized donor, and ionized acceptor densities, respectively. Since only $n$-type unipolar cases will be considered, $p$ and $N_A^-$ are neglected. The local electron density $n$ can be found by integrating its distribution function $f$ over all momentum vectors $\boldsymbol{k}$ [18],

$$
n = \frac{1}{4\pi^3} \int f d\boldsymbol{k} = \frac{1}{4\pi^3} \int \frac{1}{\exp\left(\frac{E-F}{k_B T}\right) + 1} d\boldsymbol{k} \tag{6}
$$

where $f$ has been approximated by a Fermi-Dirac distribution, depending only on the electron energy $E$ and the distribution's chemical potential $F$ and temperature $T$. As indicated in Fig. 1, each point in real space is represented by a set of Fermi distributions. Therefore, the total electron density is a summation over integrals with the form (6),

$$
\begin{aligned}
n &= \sum_i n_i = \frac{1}{4\pi^3} \sum_i \int_{\boldsymbol{k}_i} f_i d\boldsymbol{k} \\
&= \frac{1}{4\pi^3} \sum_i \int_{\boldsymbol{k}_i} \frac{1}{\exp\left(\frac{E-F_i}{k_B T_i}\right) + 1} d\boldsymbol{k},
\end{aligned} \tag{7}
$$

where the integration limits $\boldsymbol{k}_i$ span the range of momentum vectors over which each distribution function $f_i$ is defined.

The electronic band structure for a particular semiconductor determines the relationship between $E$ and $\boldsymbol{k}$. Since each $f_i$ depends only on $E$, the integrals (7) over the three-dimensional $\boldsymbol{k}$ vectors can be transformed into one-dimensional integrals over $E$,

$$
\begin{aligned}
n_i &= \frac{1}{4\pi^3} \int_{E_i} f_i(E) \left[ \int_{\boldsymbol{k}_i} \frac{\delta(E_k - E)}{|\nabla_{\boldsymbol{k}} E|} d\boldsymbol{k} \right] dE \\
&= \int_{E_i} f_i(E) \left[ \int_{\boldsymbol{k}_i} \rho_{\boldsymbol{k}}(E) d\boldsymbol{k} \right] dE \\
&= \int_{E_i} f_i(E) \rho_i(E) dE,
\end{aligned} \tag{8}
$$

where integration limit $E_i$ spans the energy range over which $f_i$ is defined and $\nabla_{\boldsymbol{k}} E$ is the gradient of electron energy in momentum space. The Dirac delta function reduces each bracketed term to the integral of $|\nabla_{\boldsymbol{k}} E|^{-1}$ over the area of an electron energy isosurface in $\boldsymbol{k}$ space. In principle, this could be performed numerically for any arbitrary band structure from which energy isosurfaces can be extracted. If the resulting density of states $\rho_i(E)$ can then be partitioned into separate energy ranges $[E_{a,ij}, E_{b,ij}]$, each approximated by a simple power law $\rho_{ij}(E) = A_{ij}(E - E_{\rho,ij})^{\alpha_{ij}}$, then the electron density of each distribution function can be expressed as,

$$
n_i = \sum_j n_{ij} = \sum_j A_{ij} \int_{E_{a,ij}}^{E_{b,ij}} \frac{(E - E_{\rho,ij})^{\alpha_{ij}}}{\exp\left(\frac{E-F_i}{k_B T_i}\right) + 1} dE. \tag{9}
$$

![](./images/811657061405294593_5.jpg)

It should be emphasized that no physical meaning is attributed by the parameters $E_{a,ij}$, $E_{b,ij}$, $A_{ij}$, $E_{\rho,ij}$, and $\alpha_{ij}$; they are simply numbers used to fit the $|\nabla_{\boldsymbol{k}} E|^{-1}$ isosurface integrals. To simplify the notation, please allow their subscripts $ij$ to be implied. The electron density $n_{ij}$ can then be expressed as,

$$
\begin{aligned}
n_{ij} &= A \int_{E_a}^{E_b} \frac{(E - E_{\rho})^\alpha}{\exp\left(\frac{E-F_i}{k_B T_i}\right) + 1} dE \\
&= A(k_B T_i)^{\alpha+1} \mathcal{F}_\alpha(\eta_i^\rho, a_i, b_i),
\end{aligned} \tag{10}
$$

where $\mathcal{F}_\alpha(\eta_i^\rho, a_i, b_i)$ is the incomplete Fermi integral of order $\alpha$ given by

$$
\begin{aligned}
\mathcal{F}_\alpha(\eta_i^\rho, a_i, b_i) &= \int_{a_i}^{b_i} \frac{\epsilon^\alpha}{e^{\epsilon-\eta_i^\rho} + 1} d\epsilon \\
\eta_i^\rho &\equiv \frac{F_i - E_\rho}{k_B T_i} \\
a_i &\equiv \frac{E_a - E_\rho}{k_B T_i} \\
b_i &\equiv \frac{E_b - E_\rho}{k_B T_i}.
\end{aligned} \tag{11}
$$

The corresponding electron energy density $E_{n,ij}$ is given by,

$$
E_{n,ij} = A(k_B T_i)^{\alpha+2} \mathcal{F}_{\alpha+1}(\eta_i^\rho, a_i, b_i). \tag{12}
$$

The incomplete Fermi integrals can be evaluated using the algorithm formulated and implemented by Goano [19]. Energy isosurface integrals like those in (8) will be shown to arise in all aspects of electron dynamics in the Fermi kinetics model. They are a means to represent the phase space that the ideal Fermi gases fill. The quantity $\rho_{\boldsymbol{k}}(E)$ has been introduced in (8) because it appears in all subsequent isosurface integrals.

To define the chemical potentials and electron temperatures required to evaluate (9), Gauss's law (5) must be coupled to equations defining the electron particle and energy densities for the distribution functions defined at each point in real space. As for most energy transport models, these equations are derived from moments of the BTE [18]. As outlined in Sect. 1, the zeroth moment produces electron continuity. However, since multiple Fermi distributions are assigned to a given point in real space, each requires a separate continuity equation,

$$
-\frac{dn_i}{dt} = \nabla \cdot \boldsymbol{J}_i + R_i^n + C_i^n, \tag{13}
$$

where $\boldsymbol{J}_i$ is the mobile electron flux, $R_i^n$ is the net electron-hole recombination rate, and $C_i^n$ is the net rate electrons scatter out of the distribution function. The second moment

of the BTE produces energy conservation for each distribu-
tion,
$$
-\frac{d E_{n, i}}{d t}=q \boldsymbol{E} \cdot \boldsymbol{J}_{i}+\nabla \cdot \boldsymbol{S}_{i}^{\mathrm{tot}}+R_{i}^{E}+C_{i}^{E}, \quad(14)
$$
where $\boldsymbol{S}_{i}^{\text {tot }}$ is the total mobile electron energy flux (kinetic plus heat), $R_{i}^{E}$ is the energy loss rate to recombination, and $C_{i}^{E}$ is the net loss due to scattering. Since only unipolar cases are being considered, $R_{i}^{n}$ and $R_{i}^{E}$ are currently ne glected. Further specifying (13) and (14) then requires de- riving the real space fluxes $\boldsymbol{J}_{i}$ and $\boldsymbol{S}_{i}^{\text {tot }}$ as well as the momentum space collision operators $C_{i}^{n}$ and $C_{i}^{E}$.

### 2.1 Real space transport
The electron flux $\boldsymbol{J}$ can be computed from the first moment of the BTE expressed in the momentum relaxation time approximation [18],
$$
\boldsymbol{J}+\bar{\tau}_{\boldsymbol{k}} \frac{d \boldsymbol{J}}{d t}=\frac{1}{4 \pi^{3}} \int_{\boldsymbol{k}} \boldsymbol{v} \tau_{\boldsymbol{k}}\left(\frac{q \boldsymbol{E}}{\hbar} \cdot \nabla_{\boldsymbol{k}} f-\boldsymbol{v} \cdot \nabla f\right) d \boldsymbol{k}, \quad(15)
$$
where $\tau_{k}$ is the momentum relaxation time and $\boldsymbol{v}$ is electron velocity. For simplicity, the Lorentz force has been neglected, and it will hereafter be assumed the momentum relaxation rate is much faster than the field and charge fluctuation rates, $\bar{\tau}_{m} d \boldsymbol{J} / d t \approx 0$. The relaxation time depends on the rate electrons scatter in momentum space and will be specified more precisely in Sect. 2.2. The electron flux can be generalized for arbitrary band structure by adopting the group velocity of an electron wave packet $\boldsymbol{v}=\nabla_{\boldsymbol{k}} E / \hbar$. Since the Fermi-Dirac distribution $f$ depends on electron energy, and not the direction of the momentum vector, its gradient in $\boldsymbol{k}$ space can be expressed as,
$$
\nabla_{\boldsymbol{k}} f=\frac{d f}{d E} \nabla_{\boldsymbol{k}} E=\frac{d f}{d E} \hbar \boldsymbol{v}. \quad(16)
$$

The electron flux then becomes,
$$
\begin{aligned}
\boldsymbol{J} & =\frac{1}{4 \pi^{3}} \int_{\boldsymbol{k}} \boldsymbol{v} \tau_{\boldsymbol{k}}\left(q \boldsymbol{E} \frac{d f}{d E}-\nabla f\right) \cdot \boldsymbol{v} d \boldsymbol{k} \\
& =\frac{1}{4 \pi^{3}} \int_{\boldsymbol{k}} \tau_{\boldsymbol{k}} \boldsymbol{v} \boldsymbol{v}^{T}\left(q \boldsymbol{E} \frac{d f}{d E}-\nabla f\right) d \boldsymbol{k}
\end{aligned}
$$

$$
\boldsymbol{v} \boldsymbol{v}^{T}=\left[\begin{array}{ccc}
v_{x}^{2} & v_{x} v_{y} & v_{x} v_{z} \\
v_{y} v_{x} & v_{y}^{2} & v_{y} v_{z} \\
v_{z} v_{x} & v_{z} v_{y} & v_{z}^{2}
\end{array}\right]. \quad(17)
$$

As with electron density (7), the total electron flux is the sum of contributions from the separate distributions $f_{i}$,
$$
\boldsymbol{J}=\frac{1}{4 \pi^{3}} \sum_{i} \int_{\boldsymbol{k}_{i}} \tau_{\boldsymbol{k}} \boldsymbol{v} \boldsymbol{v}^{T}\left(q \boldsymbol{E} \frac{d f_{i}}{d E}-\nabla f_{i}\right) d \boldsymbol{k}. \quad(18)
$$

Since the part of the integrand in parentheses depends only on electron energy, the integral over momentum can again be transformed into an integral over energy,
$$
\boldsymbol{J}_{i}=\int_{E_{i}}\left[\int_{\boldsymbol{k}_{i}} \tau_{\boldsymbol{k}} \boldsymbol{v} \boldsymbol{v}^{T} \rho_{\boldsymbol{k}}(E) d \boldsymbol{k}\right]\left(q \boldsymbol{E} \frac{d f_{i}}{d E}-\nabla f_{i}\right) d E, \quad(19)
$$
where $\rho_{k}(E)$ was defined in (8). In principle, all the terms of tensor $\tau_{\boldsymbol{k}} \boldsymbol{v} \boldsymbol{v}^{T} \rho_{\boldsymbol{k}}(E)$ can be numerically integrated over the electron energy isosurfaces of the band dispersion. However, to simplify, a cubically symmetric semiconductor will be assumed, and the Fermi distributions will be assigned to their respective ranges of momentum space such that $\tau_{k}$ and $|\nabla_{k} E|$ are even functions of $\boldsymbol{k}$ and each vector component of $\boldsymbol{v}=\nabla_{\boldsymbol{k}} E / \hbar$ is odd. These conditions cause the off-diagonal terms to integrate to zero and cause the integrals of the remaining diagonal terms to be equal. The resulting electron flux vector simplifies to,
$$
\boldsymbol{J}_{i}=\int_{E_{i}}\left[\int_{\boldsymbol{k}_{i}} \tau_{\boldsymbol{k}} \frac{v^{2}}{3} \rho_{\boldsymbol{k}}(E) d \boldsymbol{k}\right]\left(q \boldsymbol{E} \frac{d f_{i}}{d E}-\nabla f_{i}\right) d E, \quad(20)
$$
which requires a reduced number of isosurface integrals. The ramifications of exploiting the symmetry of momentum space in this way will be discussed at greater length in Sect. 5.3.

As for electron density (9), the isosurface integrals required by (20) can be more easily implemented if they can be partitioned into separate energy ranges each represented by a power law,
$$
\begin{aligned}
\mu_{i j} & =\left[\int_{\boldsymbol{k}_{i}} \tau_{\boldsymbol{k}} \frac{v^{2}}{3} \rho_{\boldsymbol{k}}(E) d \boldsymbol{k}\right]_{E_{c, i j}}^{E_{d, i j}} \\
& =D_{i j}\left(E-E_{J, i j}\right)^{\beta_{i j}}, \quad(21)
\end{aligned}
$$
where $E_{c, i j}, E_{d, i j}, D_{i j}, E_{J, i j}$, and $\beta_{i j}$ are the parameters chosen to approximate the numerically evaluated isosurface integrals. They are labeled to indicate no necessary relationship to the parameters used to describe the densities of states in (9). Using these power law approximations, the flux component for a particular Fermi distribution can be expressed as,
$$
\begin{aligned}
\boldsymbol{J}_{i}= & \sum_{j} D_{i j} \int_{E_{c, i j}}^{E_{d, i j}}\left(E-E_{J, i j}\right)^{\beta_{i j}} \\
& \times\left(q \boldsymbol{E} \frac{d f_{i}}{d E}-\nabla f_{i}\right) d E.
\end{aligned}
$$

To simplify the notation, let the parameters' subscripts $i j$ be implied such that,
$$
\boldsymbol{J}_{i j}=D \int_{E_{c}}^{E_{d}}\left(E-E_{J}\right)^{\beta}\left(q \boldsymbol{E} \frac{d f_{i}}{d E}-\nabla f_{i}\right) d E. \quad(23)
$$

![](./images/811657061405294593_6.jpg)

From this point, the electron flux derivation is similar to that detailed in [13] but generalized for incomplete Fermi integrals of arbitrary order. First, note from the definitions of the Fermi distribution (6) and the unitless parameter $\eta \equiv (F-E_0)/(k_B T)$ that

$$
\frac{d f}{d E}=-\frac{d f}{d F}=-\frac{1}{k_{B} T} \frac{d f}{d \eta}=-\frac{1}{k_{B} T} f^{\prime}.
\tag{24}
$$

Flux (23) can therefore be expressed as,

$$
\boldsymbol{J}_{i j}=-D \int_{E_{c}}^{E_{d}}\left(E-E_{J}\right)^{\beta}\left(\frac{q}{k_{B} T_{i}} \boldsymbol{E} f_{i}^{\prime}+\nabla f_{i}\right) d E. \quad(25)
$$

The integral over the drift term can be evaluated by using the definition of the incomplete Fermi integral,

$$
\begin{aligned}
\mathcal{F}_{\beta}\left(\eta_{i}^{J}, c_{i}, d_{i}\right) &=\int_{c_{i}}^{d_{i}} \frac{\epsilon^{\beta}}{e^{\epsilon-\eta_{i}^{J}}+1} d \epsilon \\
\eta_{i}^{J} &=\frac{F_{i}-E_{J}}{k_{B} T_{i}} \\
c_{i} &=\frac{E_{c}-E_{J}}{k_{B} T_{i}} \\
d_{i} &=\frac{E_{d}-E_{J}}{k_{B} T_{i}}
\end{aligned}
\tag{26}
$$

and the following identity [20],

$$
\begin{aligned}
\mathcal{F}_{\beta}^{\prime}\left(\eta_{i}^{J}, c_{i}, d_{i}\right)=& \frac{d}{d \eta_{i}^{J}} \mathcal{F}_{\beta}\left(\eta_{i}^{J}, c_{i}, d_{i}\right) \\
=& \beta \mathcal{F}_{\beta-1}\left(\eta_{i}^{J}, c_{i}, d_{i}\right) \\
&+\frac{c_{i}^{\beta}}{e^{c_{i}-\eta_{i}^{J}}+1}-\frac{d_{i}^{\beta}}{e^{d_{i}-\eta_{i}^{J}}+1}.
\end{aligned}
\tag{27}
$$

The resulting flux is,

$$
\boldsymbol{J}_{i j}=-q D\left\{\boldsymbol{E}\left(k_{B} T_{i}\right)^{\beta} \mathcal{F}_{\beta}^{\prime}+\frac{1}{q} \nabla\left[\left(k_{B} T_{i}\right)^{\beta+1} \mathcal{F}_{\beta}\right]\right\}, \quad(28)
$$

where the incomplete Fermi integrals are understood to be functions of $\eta_{i}^{J}, c_{i}$, and $d_{i}$ according to (26) and (27).

There may be a number of ways to discretize (28) suitable for simulation. The procedure chosen here emulates that used in [13] by recasting it as a first order differential equation for

$$
\mathcal{N}=\left(k_{B} T_{i}\right)^{\beta} \mathcal{F}_{\beta}^{\prime}\left(\eta_{i}^{J}, c_{i}, d_{i}\right)
\tag{29}
$$

and solving it in a form compatible with the Scharfetter-Gummel method [21, 22]. The resulting discretized flux along an edge joining nodes 1 and 2 of a mesh representing the simulation domain then becomes,

$$
\begin{aligned}
J_{i j}^{1 \rightarrow 2} & =-\frac{q D}{\mathcal{L}}\left(\mathcal{T}_{n}\right)_{\mathrm{av}}\left[B\left(\xi_{n}\right) \mathcal{N}_{1}-B\left(-\xi_{n}\right) \mathcal{N}_{2}\right] \\
& =J_{1, i j}\left(T_{i_{1}}, T_{i_{2}}\right)-J_{2, i j}\left(T_{i_{1}}, T_{i_{2}}\right),
\end{aligned}
\tag{30}
$$

where $\mathcal{L}$ is the length of the edge, $\mathcal{T}_{n}$ is the generalized Einstein coefficient,

$$
\mathcal{T}_{n}=\frac{\mathcal{F}_{\beta}}{\mathcal{F}_{\beta}^{\prime}} \frac{k_{B} T_{i}}{q},
\tag{31}
$$

$\mathcal{N}_{1(2)}$ is (29) evaluated at node 1(2), and $B(\xi_{n})$ is the Bernoulli function,

$$
B(\xi)=\frac{\xi}{\exp (\xi)-1}
\tag{32}
$$

evaluated for argument,

$$
\xi_{n}=\frac{1}{\left(\mathcal{T}_{n}\right)_{\mathrm{av}}}\left[\mathcal{L} E^{1 \rightarrow 2}+\Delta\left(\mathcal{T}_{n}\right)\right],
\tag{33}
$$

with $E^{1 \rightarrow 2}$ equal to the electric field along the edge. The notations $(x)_{\mathrm{av}}$ and $\Delta(x)$ indicate the following functions of quantity $x$ evaluated at nodes 1 and 2,

$$
\begin{aligned}
(x)_{\mathrm{av}} &=\left(x_{1}+x_{2}\right) / 2 \\
\Delta(x) &=x_{2}-x_{1}.
\end{aligned}
\tag{34}
$$

Each flux term $J_{1, i j}(T_{i_{1}}, T_{i_{2}})$ and $J_{2, i j}(T_{i_{1}}, T_{i_{2}})$ in (30) depends on both the chemical potentials $F_i$ and the temperatures $T_i$ of the Fermi distributions at nodes 1 and 2. However, the notation explicitly indicates the dependence on temperature because it is this dependence that will be subsequently manipulated to compute heat flux using the thermodynamic identity. Please refer to [13] for further details of the discretization procedure and its role in heat flow. Summing (30) over all the power series used to represent the isosurface integrals $\mu_{i j}$ for distribution function $f_i$ produces the total electron flux $\boldsymbol{J}_i$ required by the charge continuity equation (13).

The electron kinetic energy flux can be evaluated by first multiplying the integrand in (25) by electron energy $E$ and repeating the process. The result is,

$$
\begin{aligned}
K_{i j}^{1 \rightarrow 2}= & -\frac{q D}{\mathcal{L}}\left(\mathcal{T}_{E}\right)_{\mathrm{av}}\left[B\left(\xi_{E}\right) \mathcal{E}_{1}-B\left(-\xi_{E}\right) \mathcal{E}_{2}\right] \\
& +E_{J}\left[J_{1, i j}\left(T_{i_{1}}, T_{i_{2}}\right)-J_{2, i j}\left(T_{i_{1}}, T_{i_{2}}\right)\right] \\
= & K_{1, i j}\left(T_{i_{1}}, T_{i_{2}}\right)-K_{2, i j}\left(T_{i_{1}}, T_{i_{2}}\right),
\end{aligned}
\tag{35}
$$

where $\mathcal{T}_E$ is defined as,

$$
\mathcal{T}_{E}=\frac{\mathcal{F}_{\beta+1}}{\mathcal{F}_{\beta+1}^{\prime}} \frac{k_{B} T_{i}}{q},
\tag{36}
$$

$\mathcal{E}_{1(2)}$ is given by,

$$
\mathcal{E}=\left(k_{B} T_{i}\right)^{\beta+1} \mathcal{F}_{\beta+1}^{\prime}\left(\eta_{i}^{J}, c_{i}, d_{i}\right)
\tag{37}
$$

![](./images/811657061405294593_7.jpg)

evaluated at node 1(2), and the argument of the Bernoulli function is given by,

$$
\xi_{E}=\frac{1}{\left(\mathcal{T}_{E}\right)_{\mathrm{av}}}\left[\mathcal{L} E^{1 \rightarrow 2}+\Delta\left(\mathcal{T}_{E}\right)\right].
\tag{38}
$$

As with $J_{1, i j}$ and $J_{2, i j}$ in (30), (35) explicitly indicates the $T_{i}$ dependencies of $K_{1, i j}$ and $K_{2, i j}$ because they are key to the final flux required for the real space transport part of the model, which is the heat flow between Fermi gases $f_{i_{1}}$ and $f_{i_{2}}$ assigned to mesh nodes 1 and 2.

The heat flow between the distributions at nodes 1 and 2 is determined using the thermodynamic identity approach described in Sect. 1 and presented in more detail in [13]. With the electron particle and kinetic energy fluxes from (30) and (35), the heat flow can be readily evaluated as,

$$
\begin{aligned}
H_{i j}^{1 \rightarrow 2}= & K_{1, i j}\left(T_{i_{1}}, T_{i_{2}}\right)-K_{1, i j}\left(T_{i_{2}}, T_{i_{2}}\right) \\
& -F_{i_{1}}\left[J_{1, i j}\left(T_{i_{1}}, T_{i_{2}}\right)-J_{1, i j}\left(T_{i_{2}}, T_{i_{2}}\right)\right] \\
& -K_{2, i j}\left(T_{i_{1}}, T_{i_{2}}\right)+K_{2, i j}\left(T_{i_{1}}, T_{i_{1}}\right) \\
& +F_{i_{2}}\left[J_{2, i j}\left(T_{i_{1}}, T_{i_{2}}\right)-J_{2, i j}\left(T_{i_{1}}, T_{i_{1}}\right)\right].
\end{aligned}
\tag{39}
$$

The notations $J_{1, i j}\left(T_{i_{2}}, T_{i_{2}}\right)$ and $K_{1, i j}\left(T_{i_{2}}, T_{i_{2}}\right)$ simply mean evaluating these fluxes as they appear in (30) and (35) except replacing $T_{i_{1}}$, the temperature of the Fermi gas $f_{i_{1}}$ at node 1, with $T_{i_{2}}$, the temperature of $f_{i_{2}}$. The converse is true for the fluxes indicated by $J_{2, i j}\left(T_{i_{1}}, T_{i_{1}}\right)$ and $K_{2, i j}\left(T_{i_{1}}, T_{i_{1}}\right)$. Adding the resulting heat flow to the kinetic energy flux (35) and repeating for all the power series used to represent the isosurface integrals $\mu_{i j}$ for distribution function $f_{i}$ produces the total real space energy flux $S_{i}^{\text {tot }}$ required by the energy conservation equation (14).

### 2.2 Momentum space scattering

The real space fluxes presented in the previous section involve electron and energy exchanges between Fermi distributions at different real space coordinates but confined to the same ranges of momentum space. At each point in real space, the distribution functions defined there can exchange particles and energy through scattering. The initial implementation presented here considers optical phonon scattering. A general expression for the electron-phonon scattering rate from an initial electron momentum state $\boldsymbol{k}$ may be written as [18,23,24],

$$
\begin{aligned}
W_{\boldsymbol{k}}= & \int W_{\boldsymbol{k}, \boldsymbol{k}^{\prime}} \delta_{\boldsymbol{k} \mp \boldsymbol{q}-\boldsymbol{k}^{\prime}} \\
& \times\left(n_{q}+\frac{1}{2} \pm \frac{1}{2}\right) \delta\left(E_{\boldsymbol{k}^{\prime}}-E_{\boldsymbol{k}} \pm \hbar \omega\right) d \boldsymbol{k}^{\prime},
\end{aligned}
\tag{40}
$$

where $W_{\boldsymbol{k}, \boldsymbol{k}^{\prime}}$ is computed from Fermi's Golden Rule using a matrix element appropriate for the scattering mechanism, $\boldsymbol{q}$ is the phonon momentum vector, $n_{q}$ is its occupation number, $\hbar \omega$ is its energy, and $\boldsymbol{k}^{\prime}$ is the electron's final state momentum vector. The upper sign in (40) is for phonon emission and the lower is for absorption. Assuming a constant optical phonon energy independent of $\boldsymbol{q}$, a collision operator for net scattering from distribution $f_{i}$ to distribution $f_{f}$ due to phonon emission can be expressed as,

$$
\begin{aligned}
C_{i f}^{n}= & \frac{1}{4 \pi^{3}} \int_{\boldsymbol{k}_{i}} \int_{\boldsymbol{k}_{f}} W_{\boldsymbol{k}, \boldsymbol{k}^{\prime}} \delta\left(E_{\boldsymbol{k}^{\prime}}-E_{\boldsymbol{k}}+\hbar \omega\right) \\
& \times\left\{(n_{q}+1) f_{i}(\boldsymbol{k})\left[1-f_{f}\left(\boldsymbol{k}^{\prime}\right)\right]\right. \\
& \left.-n_{q} f_{f}\left(\boldsymbol{k}^{\prime}\right)\left[1-f_{i}(\boldsymbol{k})\right]\right\} d \boldsymbol{k}^{\prime} d \boldsymbol{k},
\end{aligned}
\tag{41}
$$

where the integrations are limited to $\boldsymbol{k}$ vectors for which $f_{i}$ and $f_{f}$ are defined. Another operator can be defined for the net scattering from $f_{i}$ to $f_{f}$ due to phonon absorption, but it is the negative of the net scattering from $f_{f}$ to $f_{i}$ from phonon emission $-C_{j i}^{n}$. Therefore, only the phonon emission operators will be considered. Neglecting the $\hbar \omega$ dependence on $\boldsymbol{q}$ is a reasonable assumption for the optical phonons considered here, but its dispersion must be addressed to include acoustic phonon scattering. Similarly, treating hot optical phonon effects would require a $\boldsymbol{q}$-dependent $n_{q}$ incorporated in the integrals over momentum space. However, hot optical phonons are not currently considered, and the phonon occupation number is determined by Bose-Einstein statistics,

$$
n_{q}=\frac{1}{\exp \left(\frac{\hbar \omega}{k_{B} T_{a}}\right)-1},
\tag{42}
$$

where $T_{a}$ is the local lattice, i.e. acoustic phonon, temperature.

Since distribution functions in the Fermi kinetics model depend only on the energies of the initial and final states, the collision operators can be transformed into integrals over initial state energy,

$$
\begin{aligned}
C_{i f}^{n}= & \int_{E_{i}}\left[\int_{\boldsymbol{k}_{i}} \rho_{\boldsymbol{k}}(E) \int_{\boldsymbol{k}_{f}} W_{\boldsymbol{k}, \boldsymbol{k}^{\prime}} \rho_{\boldsymbol{k}^{\prime}}(E-\hbar \omega) d \boldsymbol{k}^{\prime} d \boldsymbol{k}\right] \\
& \times\left\{(n_{q}+1) f_{i}(E)\left[1-f_{f}(E-\hbar \omega)\right]\right. \\
& \left.-n_{q} f_{f}(E-\hbar \omega)\left[1-f_{i}(E)\right]\right\} d E,
\end{aligned}
\tag{43}
$$

where the integration limit $E_{i}$ is restricted to energies for which both $f_{i}(E)$ and $f_{f}(E-\hbar \omega)$ are defined and $\rho_{\boldsymbol{k}}(E)$ was defined in (8). As for electron density and flux, the collision operators (43) can be more efficiently implemented by expressing the bracketed energy isosurface integrals by power laws defined over different energy ranges,

![](./images/811657061405294593_8.jpg)

$$
\begin{aligned}
W_{i f j} & =\left[\int_{\boldsymbol{k}_{i}} \rho_{\boldsymbol{k}}(E) \int_{\boldsymbol{k}_{f}} W_{\boldsymbol{k}, \boldsymbol{k}^{\prime}} \rho_{\boldsymbol{k}^{\prime}}(E-\hbar \omega) d \boldsymbol{k}^{\prime} d \boldsymbol{k}\right]_{E_{g, i f j}}^{E_{h, i f j}} \\
& =G_{i f j}\left(E-E_{s, i f j}\right)^{\gamma_{i f j}},
\end{aligned}
$$
where $G_{i f j}$, $E_{s, i f j}$, and $\gamma_{i f j}$ are the parameters used to approximate the integral for energies between $E_{g, i f j}$ and $E_{h, i f j}$. The net rate of electron transfer from $f_{i}$ to $f_{f}$ by phonon emission then becomes a summation over these power law approximations, $C_{i f}^{n}=\sum_{j} C_{i f j}^{n}$, with each expressed as,

$$
\begin{aligned}
C_{i f j}^{n}= & G \int_{E_{g}}^{E_{h}}\left(E-E_{s}\right)^{\gamma} \\
& \times\left\{\left(n_{q}+1\right) f_{i}(E)\left[1-f_{f}(E-\hbar \omega)\right]\right. \\
& \left.-n_{q} f_{f}(E-\hbar \omega)\left[1-f_{i}(E)\right]\right\} d E,
\end{aligned}
$$

where the subscripts $i f j$ for parameters $G$, $E_{s}$, $\gamma$, $E_{g}$, and $E_{h}$ are implied.

Bose-Einstein statistics for $n_{q}$ (42) and some useful identities (see Appendix A) allow (45) to be expressed with incomplete Fermi integrals when the initial and final distributions have the same temperature $T_{i}=T_{f}=T$,

$$
\begin{aligned}
C_{i f j}^{n}= & n_{q} \frac{\exp \left[\frac{\hbar \omega+F_{f}-F_{i}}{k_{\mathrm{B}} T}\right]-\exp \left[\frac{\hbar \omega}{k_{\mathrm{B}} T_{a}}\right]}{\exp \left[\frac{\hbar \omega+F_{f}-F_{i}}{k_{\mathrm{B}} T}\right]-1} \\
& \times G\left(k_{B} T\right)^{\gamma+1}\left[\mathcal{F}_{\gamma}\left(\eta_{i}^{s}, g, h\right)-\mathcal{F}_{\gamma}\left(\eta_{f+}^{s}, g, h\right)\right],
\end{aligned}
$$

where the incomplete Fermi integrals depend on the unitless parameters,

$$
\begin{aligned}
\eta_{i}^{s} & =\frac{F_{i}-E_{s}}{k_{\mathrm{B}} T} \\
\eta_{f+}^{s} & =\frac{F_{f}+\hbar \omega-E_{s}}{k_{\mathrm{B}} T} \\
g & =\frac{E_{g}-E_{s}}{k_{\mathrm{B}} T} \\
h & =\frac{E_{h}-E_{s}}{k_{\mathrm{B}} T}.
\end{aligned}
$$

This is generally true only when the initial and final distributions are the same. When they are different, $f_{i}$ and $f_{f}$ may be presumed much smaller than unity and (45) can be evaluated as,

$$
\begin{aligned}
C_{i f j}^{n}= & \left(n_{q}+1\right) G\left(k_{\mathrm{B}} T_{i}\right)^{\gamma+1} \mathcal{F}_{\gamma}\left(\eta_{i}^{s}, g_{i}, h_{i}\right) \\
& -n_{q} G\left(k_{\mathrm{B}} T_{f}\right)^{\gamma+1} \mathcal{F}_{\gamma}\left(\eta_{f+}^{s}, g_{f}, h_{f}\right),
\end{aligned}
$$

![](./images/811657061405294593_9.jpg)

where, in this case, the unitless parameters are given by,

$$
\begin{aligned}
\eta_{i}^{s} & =\frac{F_{i}-E_{s}}{k_{\mathrm{B}} T_{i}} \\
\eta_{f+}^{s} & =\frac{F_{f}+\hbar \omega-E_{s}}{k_{\mathrm{B}} T_{f}} \\
g_{i(f)} & =\frac{E_{g}-E_{s}}{k_{\mathrm{B}} T_{i(f)}} \\
h_{i(f)} & =\frac{E_{h}-E_{s}}{k_{\mathrm{B}} T_{i(f)}}.
\end{aligned}
$$

As suggested by Fig. 1, this presumption is reasonable when the conduction band minimum is sufficiently lower that the other valley minima. Under these conditions, only the lowest energy distribution function, $f_{\Gamma, 1}$ in Fig. 1, would be degenerate at high dopant densities. Since the initial and final distribution functions are the same for phonon emission from $f_{\Gamma, 1}$, (46) can be used, while (48) can be applied to scattering between higher energy states. Such is the case for GaAs, in which the satellite valleys are 0.29 eV and 0.48 eV above the conduction band minimum.

Summing the equations for $C_{i f j}^{n}$ over the isosurface integral power law approximations (44) gives the net rate $C_{i f}^{n}=\sum_{j} C_{i f j}^{n}$ that electrons are lost from $f_{i}$ to $f_{f}$ due to phonon emission. The total phonon emission and absorption collision operator required by the electron continuity equation (13) can then be written as,

$$
C_{i}^{n}=\sum_{f}\left(C_{i f}^{n}-C_{f i}^{n}\right).
$$

To find the collision operator $C_{i}^{E}$ required for energy conservation (14), the energy exchanges associated with the phonon scattering processes must be determined. In this respect, momentum space scattering might be considered simpler than real space transport. As described qualitatively in Sect. 1 and mathematically in Sect. 2.1, electrons moving in real space from one Fermi gas to another require a heat exchange between the gases to effect the change from initial to final electron temperature, and this heat flow is a crucial component of the total real space energy flux. For phonon scattering in momentum space, the corresponding heat is exchanged between each gas and the crystal lattice (thermal reservoir) instead of between the gases themselves. Each gas exchanges this heat with the lattice through emission and absorption of the phonons. This is not to say that the total flow of heat into and out of each gas is entirely determined by their interactions with the lattice reservoir; there is also a heat flow that produces the net increase in total entropy of the combined electron gas system. However, this component of heat is equal to the chemical work associated with the exchange of electrons between Fermi gases with different chemical potentials [17] and is included implicitly through

the conservation of particles and kinetic energy. Please refer to Appendix B for an illustrative example. Because of the roles of the crystal lattice thermal reservoir and chemical work, the collision operator $C_{i}^{E}$ required for energy conser vation (14) can be determined by considering just the gains and losses of kinetic energy by the initial and final Fermi distributions due to the scattering processes.

The net kinetic energy loss from Fermi distribution $f_{i}$ by phonon emission can be readily computed from the particle collision operator $C_{i f j}^{n}$ (45) by multiplying the integrand by electron energy $E$. For the degenerate case, which can be used when the initial and final distributions are the same, the result is,
$$
\begin{aligned}
C_{i i j}^{E}= & n_{q} \frac{\exp \left(\frac{\hbar \omega}{k_{\mathrm{B}} T_{i}}\right)-\exp \left(\frac{\hbar \omega}{k_{\mathrm{B}} T_{a}}\right)}{\exp \left(\frac{\hbar \omega}{k_{\mathrm{B}} T_{i}}\right)-1} \\
& \times G\left(k_{B} T_{i}\right)^{\gamma+2}\left[\mathcal{F}_{\gamma+1}\left(\eta_{i}^{s}, g, h\right)\right. \\
& \left.-\mathcal{F}_{\gamma+1}\left(\eta_{i+}^{s}, g, h\right)\right],
\end{aligned}\qquad(51)
$$
where $\eta_{i}^{s}, \eta_{i+}^{s}, g$, and $h$ are the same as (47) with $i=f$ and $T=T_{i}$. The nondegenerate case used for higher energy transitions is given by,
$$
\begin{aligned}
C_{i f j}^{E}= & \left(n_{q}+1\right) G\left(k_{\mathrm{B}} T_{i}\right)^{\gamma+2} \mathcal{F}_{\gamma+1}\left(\eta_{i}^{s}, g_{i}, h_{i}\right) \\
& -n_{q} G\left(k_{\mathrm{B}} T_{f}\right)^{\gamma+2} \mathcal{F}_{\gamma+1}\left(\eta_{f+}^{s}, g_{f}, h_{f}\right).
\end{aligned}\qquad(52)
$$

Summing $C_{i f j}^{E}$ over the power laws defined in (44) gives the net rate $f_{i}$ loses kinetic energy by scattering to $f_{f}$ through phonon emission. Summing over scattering between $f_{i}$ and all distributions $f_{f}$ gives,
$$
C_{i}^{E}=\sum_{f}\left(C_{i f}^{E}-C_{f i}^{E}+\hbar \omega C_{f i}^{n}\right),\qquad(53)
$$
where $C_{f i}^{E}$ is the loss of kinetic energy by $f_{f}$ from phonon emission and $\hbar \omega C_{f i}^{n}$ accounts for the amount of that energy lost to the crystal lattice. The result is the total loss of energy from optical phonon scattering required for energy conser- vation (14).

In addition to defining the electron particle and energy collision operators, the optical phonon scattering rates can also be used to estimate the momentum relaxation time. As used in the BTE, the relaxation time reflects the rate a nonequilibrium distribution changes its value in phase space through scattering [18]. In practice, its value can be esti- mated by comparing the momentum of an initial state $k$ to that of the possible final states $k^{\prime}[23,25]$. For the optical phonon scattering considered here, the change in momen- tum can be represented as,

![](./images/811657061405294593_10.jpg)

Fig. 2 The first Brillouin zone for a face centered cubic lattice and a conformal tetrahedral mesh of its irreducible wedge. The mesh is labeled with the corresponding crystal symmetry points

$$
\begin{aligned}
\frac{d \hbar \boldsymbol{k}}{d t}= & \int \hbar\left(\boldsymbol{k}^{\prime}-\boldsymbol{k}\right) W_{\boldsymbol{k}, \boldsymbol{k}^{\prime}} \\
& \times\left(n_{q}+\frac{1}{2} \pm \frac{1}{2}\right) \delta\left(E_{\boldsymbol{k}^{\prime}}-E_{\boldsymbol{k}} \pm \hbar \omega\right) d \boldsymbol{k}^{\prime} \\
= & -\frac{\hbar \boldsymbol{k}}{\tau_{\boldsymbol{k}}},
\end{aligned}\qquad(54)
$$
from which a momentum relaxation time can then be ex- pressed as,
$$
\begin{aligned}
\frac{1}{\tau_{\boldsymbol{k}}}= & \int\left(1-\frac{\boldsymbol{k}^{\prime} \cdot \boldsymbol{k}}{|\boldsymbol{k}|^{2}}\right) W_{\boldsymbol{k}, \boldsymbol{k}^{\prime}} \\
& \times\left(n_{q}+\frac{1}{2} \pm \frac{1}{2}\right) \delta\left(E_{\boldsymbol{k}^{\prime}}-E_{\boldsymbol{k}} \pm \hbar \omega\right) d \boldsymbol{k}^{\prime}.
\end{aligned}\qquad(55)
$$

This quantity is included in the isosurface integral (21) re- quired for the real space fluxes.

## 3 Band dispersion isosurface integrals for GaAs

The equations of the Fermi kinetics model presented in previous sections contain certain quantities integrated over the electron energy isosurfaces of the semiconductor's elec- tronic band structure. To find these isosurfaces, the irre- ducible wedge of the first Brillouin zone of the semiconduc- tor crystal lattice can be filled with a conformal tetrahedral mesh. Such a mesh of electron momentum space is shown in Fig. 2 for a face centered cubic lattice. Operating on the mesh with the 48 symmetry properties that form the point group of a cubic lattice [18] fills the entire Brillouin zone. Using a suitable band structure theory, eigenenergies corre- sponding to the electron energy bands can be assigned to each mesh point in $k$ space. The entire range spanned by the electron energies can then be divided into a set of evenly spaced energy levels, and each tetrahedron visited to find which energy levels it contains. Assuming the electron ener- gies vary piecewise linearly along the mesh edges, triangles

![](./images/811657061405294593_11.jpg)

![](./images/811657061405294593_12.jpg)

Fig. 3 The first GaAs conduction band computed by the empirical pseudopotential method for the mesh points in the irreducible wedge of the first Brillouin zone

![](./images/811657061405294593_13.jpg)

Fig. 4 Electron energy isosurfaces computed from the eigenenergies defined on the vertices of the tetrahedral mesh in the irreducible wedge

that approximate pieces of the energy isosurfaces can be extracted from each tetrahedron. This procedure is described in more detail in Appendix C. Computed in this way, triangles for the same energy form manifolds of contiguous facets that approximate the electron energy isosurfaces. These triangles represent a discretization of $k$ space that can be used to approximate the isosurface integrals of the densities of states, electron velocities, momentum relaxation times, and phonon scattering rates required by the equations presented in Sect. 2.

Figure 3 shows the electron eigenenergies corresponding to the first conduction band of GaAs computed by the empirical pseudopotential method [26] as presented and implemented by Harrison [27]. Figure 4 shows some of the corresponding electron energy isosurfaces. The isosurfaces used for the numerical integrals are more closely spaced in energy ($\Delta E < \hbar\omega$) than those shown; only a small fraction is displayed to produce a more clear figure. To find the surfaces corresponding to the $\Gamma$ valley, the mesh point with the maximum energy on the line segment between the $\Gamma$ and $L$ points is identified as $k_{\Gamma L}$. Likewise, maximum energy points $k_{\Gamma X}$ and $k_{\Gamma K}$ are identified on the line segments between the $\Gamma$ and $X$ points and between the $\Gamma$ and $K$ points, respectively. The four points $(\Gamma, k_{\Gamma L}, k_{\Gamma X}, k_{\Gamma K})$ form a tetrahedron. All isosurface triangles whose centroids lie within this tetrahedron are treated as parts of the $\Gamma$ valley. Similar procedures are used to identify the isosurfaces belonging to the $L$ and $X$ valleys. The form factors used here are only rough estimates [27]. As a result, the energies of the valley minima and their curvatures differ from their measured values. To partially compensate for this, the $L$ and $X$ valleys extracted from Fig. 4 are displaced in energy so that their minima match the experimental values. Otherwise, all quantities are computed from the energy isosurfaces as they appear in Fig. 4.

![](./images/811657061405294593_14.jpg)

Fig. 5 Isosurfaces for all $\Gamma$, $L$, and $X$ valleys in the first Brillouin zone of GaAs computed for three different electron energies. Electron energies in the irreducible wedge (IW) are also shown. The $\Gamma$, $L$, and $X$ valleys that intersect the IW are labeled. The others are obtained from the symmetry of the Brillouin zone, which results in one $\Gamma$, eight $L$, and six $X$ valleys

With electron energy isosurfaces sorted into the $\Gamma$, $L$, and $X$ valleys, Fermi distributions are assigned to them according to Fig. 1. This may be considered a coarse approximation because Fig. 5 shows that the first Brillouin zone contains eight $L$ valleys and six $X$ valleys. Yet the same two Fermi functions are applied to all $L$ valleys and the same single Fermi function to all $X$ valleys. This greatly simplifies real space transport by exploiting the symmetry of the Brillouin zone but can misrepresent electron velocity at high electron energies in GaAs. This approximation's implications will be discussed further in Sect. 5.

![](./images/811657061405294593_15.jpg)

![](./images/811657061405294593_16.jpg)

Fig. 6 Density of states spectra for conduction band valleys in GaAs extracted from numerical isosurface integrals of the inverse energy gradient (dashed) and approximated by power laws over different energy ranges (solid)

<table>
<caption>Table 1 The parameters used to approximate the L valley density of states spectrum shown in Fig. 6. The parameters are scaled such that they produce a density of states in MKS units m⁻³J⁻¹ when inserted into (57)</caption>
<thead>
<tr>
<th>Eₐ</th>
<th>Eᵦ</th>
<th>A₀</th>
<th>A</th>
<th>E<sub>ρ</sub></th>
<th>α</th>
</tr>
</thead>
<tbody>
<tr>
<td>0.29</td>
<td>0.4</td>
<td>0</td>
<td>6.45 × 10⁵⁵</td>
<td>0.29</td>
<td>0.5</td>
</tr>
<tr>
<td>0.4</td>
<td>1</td>
<td>4 × 10⁴⁵</td>
<td>2.6 × 10⁶⁵</td>
<td>0.29</td>
<td>1</td>
</tr>
<tr>
<td>1</td>
<td>1.55</td>
<td>4.5 × 10⁴⁶</td>
<td>−1.46 × 10⁶⁵</td>
<td>0.29</td>
<td>1</td>
</tr>
</tbody>
</table>

### 3.1 Density of states isosurface integrals

Since the Fermi kinetics model assigns different Fermi distributions to different valleys, a separate density of states spectrum is required for each valley. Using the method described in Appendix C, an energy gradient $
abla_{\boldsymbol{k}} E$ can be assigned to the centroid $\boldsymbol{c}$ of each triangle of each energy isosurface in each valley. This quantity can be used to assign a density of states $\rho^{t}$ to each triangle,

$$
\rho^{t}=\frac{A_{t}}{4 \pi^{3}\left|
abla_{\boldsymbol{k}} E\right|}, \tag{56}
$$

where $A_{t}$ is the surface area of the triangle. Summing the $\rho^{t}$ for all isosurfaces in each of the conduction band valleys produces the density of states spectra shown in Fig. 6. Also shown in the figure are the power laws used to implement the density spectra within the model. To show this more explicitly, Table 1 lists the parameters used to approximate the $L$ valley's density of states. Inserting these parameters into the following equation,

$$
\rho_{L}(E)=A_{0}+A\left[q\left(E-E_{\rho}\right)\right]^{\alpha}, \tag{57}
$$

produces the $L$ valley's density of states in the MKS unit system m⁻³J⁻¹, which is used in (9) and (10) to obtain the electron densities for the Fermi functions assigned to the $L$ valleys.

### 3.2 Collision operator isosurface integrals

The real space fluxes and collision operators for electron continuity (13) and energy conservation (14) require additional isosurface integrals of the forms shown in (21) and (44). Since the momentum relaxation time $\tau_{\boldsymbol{k}}$ in (21) is derived from $W_{\boldsymbol{k}, \boldsymbol{k}^{\prime}}$, the scattering rate isosurface integral will be discussed first. For this initial implementation of the Fermi kinetics model, only optical phonon scattering in GaAs is considered. These scattering processes can be approximated by computing polar optical mode scattering within the $\Gamma$ valley, intervalley optical deformation potential scattering between the $\Gamma$, $L$, and $X$ valleys, along with intravalley deformation potential scattering within the $L$ and $X$ valleys [2]. Although the optical phonon frequencies vary for these different processes [18], a single value of $\hbar \omega=36$ meV is used for simplicity. Also, the overlap integrals of the initial and final state wave functions are assumed to equal one.

With these assumptions, separate scattering rate spectra $W_{E}^{Y Z}$ can be computed for transitions from any valley $Y$ to any valley $Z$. Polar optical mode and optical deformation potential scattering can be used to evaluate the isosurface integral (44) by first setting,

$$
W_{\boldsymbol{k}, \boldsymbol{k}^{\prime}}=W_{\boldsymbol{k}, \boldsymbol{k}^{\prime}}^{p o}+W_{\boldsymbol{k}, \boldsymbol{k}^{\prime}}^{d p}, \tag{58}
$$

expressing the polar optical term as [27],

$$
W_{\boldsymbol{k}, \boldsymbol{k}^{\prime}}^{p o}=\frac{1}{2}\left(\frac{1}{\epsilon_{\infty}}-\frac{1}{\epsilon_{s}}\right) \frac{\pi q^{2} \omega}{\left|\boldsymbol{k}-\boldsymbol{k}^{\prime}\right|^{2}} \delta\left(E_{\boldsymbol{k}}-E_{\boldsymbol{k}^{\prime}}-\hbar \omega\right), \tag{59}
$$

where $\epsilon_{\infty(s)}$ is the high frequency (static) dielectric constant, and expressing the deformation potential term as [23],

$$
W_{\boldsymbol{k}, \boldsymbol{k}^{\prime}}^{d p}=\frac{\pi D_{Y Z}^{2}}{2 \rho_{m} \omega} \delta\left(E_{\boldsymbol{k}}-E_{\boldsymbol{k}^{\prime}}-\hbar \omega\right), \tag{60}
$$

where $D_{Y Z}$ is the deformation potential [18] for initial and final $\boldsymbol{k}$ vectors in the $Y$ and $Z$ valleys, respectively, and $\rho_{m}$ is the mass density of GaAs. Next, an initial triangle $t_{i}$ can be chosen from a $\Gamma$ valley isosurface with energy $E_{i}$, and it's centroid treated as the initial state momentum vector $\boldsymbol{k}=\boldsymbol{c}_{i}$. Then, after locating the $\Gamma$ valley isosurface with $E_{f}=E_{i}-\hbar \omega$, the numerical integral for polar optical mode scattering to this surface can be expressed as,

$$
\begin{aligned}
W_{\boldsymbol{k}_{\Gamma}}^{p o} & =\int_{\boldsymbol{k}_{\Gamma}} W_{\boldsymbol{k}_{\Gamma}, \boldsymbol{k}^{\prime}}^{p o} \rho_{\boldsymbol{k}^{\prime}}\left(E_{\boldsymbol{k}_{\Gamma}}-\hbar \omega\right) d \boldsymbol{k}^{\prime} \\
& =\frac{\pi q^{2} \omega}{2}\left(\frac{1}{\epsilon_{\infty}}-\frac{1}{\epsilon_{s}}\right) \sum_{f=f_{\Gamma}} \frac{\rho_{f}^{t}}{\left|\boldsymbol{c}_{i}-\boldsymbol{c}_{f}\right|^{2}}, \tag{61}
\end{aligned}
$$

where the subscript and integration limit $\boldsymbol{k}_{\Gamma}$ indicate the initial and final states are both in the $\Gamma$ valley, $\rho_{\boldsymbol{k}^{\prime}}(E)$ is defined in (8), the summation is over all triangles on the final

![](./images/811657061405294593_17.jpg)

![](./images/811657061405294593_18.jpg)

Fig. 7 Numerical (dashed) isosurface integrals required by the $\Gamma$ valley electron collision operators and their power law approximations (solid)

$\Gamma$ valley isosurface, $\rho_{f}^{t}$ is the final triangle's density of states given by (56), and $\boldsymbol{c}_{f}$ is its centroid. Multiplying by the initial triangle's density of states, and repeating for all initial $\Gamma$ valley isosurface triangles gives,
$$
W_{E}^{\Gamma \Gamma}=\int_{\boldsymbol{k}_{\Gamma}} W_{\boldsymbol{k}}^{p o} \rho_{\boldsymbol{k}}\left(E_{i}\right) d \boldsymbol{k}=\sum_{i=i_{\Gamma}} W_{\boldsymbol{k}_{\Gamma}}^{p o} \rho_{i}^{t},
\tag{62}
$$
which is one of the scattering isosurface integrals (44) required to determine the collision operators for a Fermi function assigned to the $\Gamma$ valley. Repeating the procedure for deformation potential scattering to triangles on $L$ and $X$ valley isosurfaces gives,
$$
\begin{aligned}
W_{\boldsymbol{k}_{\Gamma}}^{d p, L(X)} & =\int_{\boldsymbol{k}_{L(X)}} W_{\boldsymbol{k}_{\Gamma}, \boldsymbol{k}^{\prime}}^{d p, L(X)} \rho_{\boldsymbol{k}^{\prime}}\left(E_{\boldsymbol{k}_{\Gamma}}-\hbar \omega\right) d \boldsymbol{k}^{\prime} \\
& =\frac{\pi D_{\Gamma L(X)}^{2}}{2 \rho_{m} \omega} \sum_{f=f_{L(X)}} \rho_{f}^{t}.
\end{aligned}
\tag{63}
$$

Again summing over all initial $\Gamma$ isosurface triangles gives,
$$
\begin{aligned}
W_{E}^{\Gamma L(X)} & =\int_{\boldsymbol{k}_{\Gamma}} W_{\boldsymbol{k}}^{d p, L(X)} \rho_{\boldsymbol{k}}\left(E_{i}\right) d \boldsymbol{k} \\
& =\sum_{i=i_{\Gamma}} W_{\boldsymbol{k}_{\Gamma}}^{d p, L(X)} \rho_{i}^{t},
\end{aligned}
\tag{64}
$$
which are the other two scattering isosurface integrals required for phonon emission from $\Gamma$ valley Fermi functions. All three scattering isosurface integrals are shown in Fig. 7 along with their power law approximations. Analogous procedures are used to find the isosurface integrals required for phonon emission from $L$ and $X$ valleys.

### 3.3 Real space flux isosurface integrals

For real space fluxes, additional numerical isosurface integrals can be used to evaluate (21) using (55) for the momentum relaxation time. As for the scattering rate above, an initial triangle $t_{i}$ on an initial energy isosurface $E_{i}$ is selected. Then, other isosurfaces with energies $E_{i} \mp \hbar \omega$ are located. For each triangle on the final isosurfaces, a scattering rate $W_{\boldsymbol{k}, \boldsymbol{k}^{\prime}}$ is calculated using the appropriate polar optical mode and deformation potential scattering matrix elements and treating the centroid $\boldsymbol{c}_{i}$ of the initial triangle as $\boldsymbol{k}$ and the final triangle's centroid $\boldsymbol{c}_{f}$ as $\boldsymbol{k}^{\prime}$. The component of the relaxation time for a pair of initial and final triangles is then given by,
$$
\frac{1}{\tau_{i f}}=\left(1-\frac{\boldsymbol{c}_{f} \cdot \boldsymbol{c}_{i}}{\left|\boldsymbol{c}_{i}\right|^{2}}\right) W_{\boldsymbol{k}, \boldsymbol{k}^{\prime}}\left(n_{q}+\frac{1}{2} \pm \frac{1}{2}\right) \rho_{f}^{t},
\tag{65}
$$
where the upper sign is used for phonon emission to a lower energy isosurface and the lower sign for absorption to higher energy. Repeating this for all final triangles and summing the results determines the relaxation time for the initial triangle $\tau_{i}^{-1}=\sum_{f} \tau_{i f}^{-1}$. Next, the electron velocity $\boldsymbol{v}=\nabla_{\boldsymbol{k}} E / \hbar$ for the initial triangle is computed as described in Appendix C. Squaring any one component of the velocity, multiplying by $\tau_{i}$ and the density of states for the initial triangle $\rho_{i}^{t}$, and summing over all triangles on the initial isosurface produces the isosurface integral (21) required by the real space electron fluxes. Figure 8 shows the results for all three valleys along with the power law approximations used to implement them in the Fermi kinetics model. The large values for the $X$ valley at higher energies can be explained in terms of the total phonon scattering rates considered in the next section.

![](./images/811657061405294593_19.jpg)

Fig. 8 Numerical isosurface integrals (21) (dashed) and their power law approximations (solid) required to compute the real space electron fluxes in the $\Gamma, L$, and $X$ valleys

### 3.4 Total electron-phonon scattering rate

In addition to producing the various band structure spectra required by the device equations, numerical isosurface integrals can also be used to assess the scattering mechanisms currently considered in the Fermi kinetics model. A total phonon scattering rate can be interpreted as the phonon emission and absorption rates from all the scattering mechanisms for a given initial electron energy. This is similar

![](./images/811657061405294593_20.jpg)

![](./images/811657061405294593_21.jpg)

Fig. 9 Total electron-phonon scattering rate averaged over the area of the initial electron energy isosurface

to (65) without the initial and final momentum dot product $\boldsymbol{c}_{f} \cdot \boldsymbol{c}_{i}$. However, these emission and absorption rates can depend on the initial state momentum vector. Therefore, to obtain an energy dependent scattering rate, they are averaged over the area of the initial energy isosurface. Using the numerical integral techniques described in Appendix C and demonstrated above, the total scattering rate for an initial energy $E_{i}$ can be expressed as,

$$
\frac{1}{\tau_{\mathrm{tot}}}=\frac{\sum_{i} A_{i} \sum_{f=f_{\mp}} W_{\boldsymbol{c}_{i}, \boldsymbol{c}_{f}}\left(n_{q}+\frac{1}{2} \pm \frac{1}{2}\right) \rho_{f}^{t}}{\sum_{i} A_{i}},
\tag{66}
$$

where the subscript $i$ refers to all triangles on the initial isosurface $E_{i}$ and index $f$ includes all final triangles on isosurfaces both $\hbar \omega$ below (upper sign) and above (lower sign) the initial energy.

Averaging the total phonon scattering rates over the initial energy isosurfaces produces the spectrum shown in Fig. 9. The rates agree well with those computed by Shichijo and Hess [2] below about 0.5 eV. Above this energy, the rates in Fig. 9 are lower partly due to neglecting acoustic phonon scattering. The rapid decrease above 1.5 eV is also due to considering only one conduction band. States in the second conduction band are accessible at these high energies, and interband scattering is significant. The suppressed phonon scattering rate caused by omitting this band also produces a reduced collision operator and enhanced conductivity for electrons in the $X$ valley of GaAs, resulting in high values for its isosurface integral in Fig. 8. Consequently, the current implementation of the model will be less accurate at very high electron energies.

## 4 Numerical solution scheme

The numerical isosurface integrals (8), (21), and (44) shown in Figs. 6, 8, and 7, respectively, provide the electronic band structure information the Fermi kinetics model needs to represent the device equations. Each equation balances the divergence in a vector quantity with the density of one or more scalar quantities. The box integration method is used to represent this relationship [22]. First, a tetrahedral primary mesh is created to represent the device domain. Then its dual mesh, formed from the circumcenters of the primary tetrahedrons, is computed. The relationship between primary edges and the dual mesh is shown in Fig. 10. Each primary vertex is surrounded by a polyhedron consisting of planar dual facets each perpendicular to a primary edge. To approximate a divergence from the vertex, the vector quantity is evaluated at a primary edge's midpoint, multiplied by the area of its dual polygon, and summed over all edges to which the vertex belongs. The scalar density terms in the device equations are multiplied by the volume of the polyhedron.

![](./images/811657061405294593_22.jpg)

Fig. 10 The relationship between a primary vertex of a tetrahedral mesh, the primary edges it belongs to, and the dual polygons each intersects

For the GaAs simulations considered here, the box integration method implemented at each mesh point creates thirteen equations in the thirteen unknowns defined there. The discrete version of Gauss's law (5) defines the point's electrostatic potential, the six different electron continuity equations (13) define the chemical potentials for the point's Fermi distributions, and the six energy conservation equations (14) define their temperatures. The set of nonlinearly coupled, discretized equations for all the mesh points is solved iteratively using the full Newton method.

It should be noted that the Newton method requires exact derivatives of the device equations with respect to the solution variables to achieve quadratic convergence. The algorithms developed by Goano [19] were used to numerically approximate incomplete Fermi integrals. Even though

![](./images/811657061405294593_23.jpg)

the identity (27) relates a Fermi integral's derivative to an- other Fermi integral of different order, the Newton method requires the derivative of the actual equation used to approx- imate the integral. Therefore, Goano's functions were mod- ified to return, not only the values of the integrals, but also their derivatives with respect to the normalized Fermi level arguments $\eta$ and the integration limits.

## 5 Summary of simplifying approximations
The premise on which the Fermi kinetics model is based, assigning Fermi-Dirac distributions to ranges of electron momentum space, is itself a simplifying approximation de- signed to reduce computational cost by exploiting the kinet- ics of ideal gases. However, a number of additional simpli- fications were cited as the model was derived in the preced- ing sections. For clarity, several of these approximations are summarized here.

### 5.1 Electronic band structure
As noted by Harrison [27], the form factors used to com- pute the pseudopotential band structure are rough estimates. However, with knowledge of the measured valley minima, approximate valley dispersions sufficient for demonstrating the simulation method can be obtained. Only the $\Gamma$, $L$, and $X$ valleys for the first conduction band of GaAs are con- sidered. Since the $K$ valley and the higher energy conduc- tion bands can be accessed by high energy electrons (about $1$ eV above the $\Gamma$ valley minimum), accuracy will decrease when large applied fields heat electrons to high energies. Currently, only states within $2.5$ eV of the conduction band minimum are considered.

### 5.2 Scattering mechanisms
Intervalley optical deformation potential scattering rates are computed between $\Gamma$, $L$, and $X$ valleys. Intravalley optical deformation potential scattering rates are computed for $L$ and $X$ valleys, and polar optical mode scattering is treated in the $\Gamma$ valley only. Scattering rates depend only on interaction potentials; the wave function overlap between initial and fi- nal states is not explicitly considered. This can overestimate the scattering rates particularly when the band dispersion is highly nonparabolic [23]. At high applied fields/electron en- ergies, acoustic phonon and impact ionization scattering can be significant in GaAs, but they are not considered here. Al- though intervalley optical phonon energies differ [18], a sin- gle phonon energy of $36$ meV is assumed for all scatter- ing mechanisms. Umklapp processes between adjacent Bril- louin zones are also neglected.

![](./images/811657061405294593_24.jpg)

### 5.3 Satellite valley distribution functions
As shown in Fig. 5, the first Brillouin zone for GaAs con- tains one $\Gamma$ valley, eight $L$ valleys, and six $X$ valleys. This initial implementation of the model assigns Fermi distribu- tions to the valleys as depicted in Fig. 1. Three distributions represent different energy ranges in the $\Gamma$ valley, two rep- resent the $L$ valleys, and only one represents the $X$ valleys. Assigning the Fermi functions in this way causes quantities such as the density of states and the scattering lifetime to be even functions of the momentum vector over the distri- bution functions' energy isosurfaces and causes the electron velocity $\nabla_k E/\hbar$ to be odd. In this way, the assignment of the Fermi distributions significantly simplifies the real space transport fluxes. However, assigning the same Fermi func- tion to states that can be separated by more than a reciprocal lattice vector may be suspect.

In Sect. 2, it was argued that electrons in a range of states that form a near continuum in momentum space may be ap- proximated with a Fermi distribution. However, different $X$ valleys in GaAs are not close in momentum space. Treating them with a common distribution function tacitly assumes electrons in these valleys experience the same dynamics, causing their distribution functions to evolve in the same way. At thermal equilibrium, or in certain regions of a biased device such as ohmic contacts, all the $X$ valleys will con- tain the same Fermi-like (or Maxwellian since GaAs $X$ val- leys are high in energy) electron distributions. As they move through interior regions of a device where the carrier density is relatively low and the fields high, it is true that distribu- tions in separate $X$ valleys occupy the same energy depen- dent density of states, and they do experience the same scat- tering rates given the mechanisms considered here. How- ever, the directions of the velocity vectors $\nabla_k E/\hbar$ in differ- ent $X$ valleys are not the same. The differences in velocity will produce different electron fluxes from (17) and differ- ent field induced heating from $q \boldsymbol{E} \cdot \boldsymbol{J}$. For example, when a field is applied in the [100] direction, electrons in $X$ val- leys whose axes of symmetry are parallel to [100] will heat differently from those with symmetry axes parallel to [010] and [001]. Analogous arguments can be made for heating in different $L$ valleys.

Asymmetric heating can be treated by assigning multiple Fermi functions to valleys of the same type but at differ- ent locations in the Brillouin zone and by using the full ten- sor $\boldsymbol{v} \boldsymbol{v}^T$ in (17) to compute electron flux. This increases the number of solution variables and the number of energy iso- surface integrals required to represent the fluxes. However, for bulk GaAs the average electron drift velocity is dom- inated by electrons in the $\Gamma$ valley for fields below about $10$ or $15$ kV/cm because the $L$ and $X$ valley minima are $0.29$ and $0.48$ eV, respectively, above the conduction band minimum. Above these field strengths, the accuracy of the

simplified implementation presented here is expected to de- crease. Treating indirect band gap semiconductors, such as Si, would also require a more complete treatment of the elec- tron group velocity in (17).

## 6 Simulation results

### 6.1 Electron drift velocity in GaAs

A simple initial test of the Fermi kinetics model is the elec- tron drift velocity versus applied electric field in bulk GaAs. The pronounced velocity overshoot and subsequent satura- tion characteristic of this material system demonstrate the power of the full band EMC method [2] and provide a use- ful metric for a theory of electron transport in semicon- ductors. The EMC simulation of bulk drift velocity typi- cally assumes a constant applied electric field and transla- tional invariance. These assumptions necessarily set to zero all the divergences in the device equations, thereby effec- tively eliminating Gauss’s law and reducing charge and en- ergy conservation to electron dynamics in momentum space.

To implement this simplified problem, Gauss’s law (5) is replaced with a constant electric field, and the diffusive component of the electron flux (28) is omitted, leaving only the drift component,

$$
\boldsymbol{J}_{i}^{\mathrm{drift}}=\sum_{j} \boldsymbol{J}_{i j}^{\mathrm{drift}}=-q \boldsymbol{E} \sum_{j} D_{i j}\left(k_{B} T_{i}\right)^{\beta_{i j}} \mathcal{F}_{\beta_{i j}}^{\prime}. \tag{67}
$$

A specific electron density ($10^{13}\ \mathrm{cm}^{-3}$ for the results pre- sented here) is assigned to the electronic band structure by solving for the Fermi distribution that produces the correct concentration when integrated over the densities of states depicted in Fig. 6. Charge conservation balances electrons scattering into and out of each Fermi distribution, and en- ergy conservation balances the associated kinetic energy ex- changes with the loss of phonon energy to the lattice and the energy exchanged with the field $q \boldsymbol{E} \cdot \boldsymbol{J}$. Because only steady state results are presented here, the time derivatives in (13) and (14) are set to zero. The bulk GaAs is assumed to be undoped at a constant temperature of 300 K.

Solving these device equations produces different elec- tron densities and fluxes for each Fermi distribution consid- ered in the model. Summing all fluxes and dividing by the total electron density defines the average drift velocity plot- ted versus field in Fig. 11. Also plotted are drift velocities calculated by Fischetti and Laux using EMC [28] and by Saraniti et al. with the cellular automaton implementation of EMC [29].

Despite the approximate band structure and scattering used for this proof-of-concept, the Fermi kinetics model compares favorably to the Monte Carlo approaches. The overshoot peak appears at roughly the same electric field and velocity, and the subsequent velocity saturation is ev- ident. Although it would be satisfying to attribute the dis- crepancies to a few simple causes, the details of the bulk drift velocity curve are determined by the highly nonlinear interactions between the Fermi gases and their phase space. Consequently, there are no simple parameters to adjust for the desired result. For example, increasing the polar opti- cal mode scattering might be considered to reduce the maxi- mum velocity. However, this would decrease the momentum relaxation time, thereby reducing the electron flux and field induced heating, while also increasing the rate of electron cooling from phonon emission, all combining to increase the field at which the peak occurs. Therefore, improving the result in Fig. 11 requires addressing the issues outlined in Sect. 5, particularly the use of more accurate band disper- sions and scattering rates.

![](./images/811657061405294593_25.jpg)

Fig. 11 Average electron drift velocity as a function of electric field for GaAs at 300 K as computed with full band EMC by Fischetti (solid line), the full band cellular automaton (CA) method by Saraniti (trian- gles), and full band Fermi gas kinetics (dashed line)

While the Fermi kinetics and Monte Carlo models pro- duced similar electron drift velocities in bulk GaAs, the Fermi kinetics results came at a more modest computational cost. The Monte Carlo computations tracked large numbers of electrons (on the order of $10^{4}$) for many ($\sim 10^{3}$–$10^{4}$) small increments of time ($\sim$0.1–1 fs) until steady state was achieved [28, 29]. The Fermi kinetics model, on the other hand, grouped the carriers into six different Fermi distribu- tions and computed their dynamics deterministically. There- fore, each solution producing a steady state drift velocity required about three to six factorizations of a $12 \times 12$ Jaco- bian matrix. An unoptimized version of the model calculated 110 values for Fig. 11 in about 1.1 CPU seconds on a single 3.2 GHz Intel Xeon processor.

### 6.2 Device simulation

Although the bulk drift velocity simulations in the previous section are encouraging, they do not exercise some key ele- ments of the Fermi kinetics model. Section 1 described this

![](./images/811657061405294593_26.jpg)

model's use of the thermodynamic identity to express elec- tron heat flow in real space in terms of kinetic and free en- ergy fluxes evaluated at initial and final temperatures. It went on to suggest that this approach may offer greater flexibility and robustness than other energy transport models and may accommodate more detailed descriptions of electron phase space and scattering processes. However, the translational invariance of the bulk drift velocity calculations nullified all the real space flux divergences, including the thermody- namic identity treatment of heat flow. Therefore, testing the assertions made in Sect. 1 requires a device simulation that combines both the real space and momentum space transport mechanisms.

Virtually every functional semiconductor device includes intentional doping, usually nonuniform and often with high density regions. As a result, ionized impurity scattering is an important part of device simulation [30]. Also, the ran- domizing effects of electron-electron scattering can affect the momentum relaxation time. The roles of these mech- anisms in the Fermi kinetics model would be to alter the isosurface integrals, shown in Figs. 7 and 8, that determine electron scattering between distribution functions and the real space fluxes. They might be incorporated in an ad hoc fashion by scaling the isosurface integrals with an empir- ical factor used to fit low field mobility's dependence on dopant density [30]. A more rigorous way might be to in- vestigate changes in Figs. 7 and 8 when these mechanisms are included for different ionized impurity and electron den- sities. The separate power laws that represent the isosurface integrals might then be scaled by a density dependent fac- tor that accounts for these changes. However, this is beyond the scope of the present work. Device simulations are, there- fore, currently limited in accuracy but are nonetheless nec- essary to test the numerical consistency of the real space and momentum space dynamics and the robustness of heat flow based on the thermodynamic identity.

A simple $n^+nn^+$ GaAs structure, previously measured and simulated by Shiktorov et al. [31], was used to further test the Fermi kinetics model. It consists of a $7.5\ \mu$m re- gion with $10^{15}\ \text{cm}^{-3}$ $n$-type dopant density located between two $0.5\ \mu$m regions each with $2\times 10^{16}\ \text{cm}^{-3}$ $n$-type doping. Lossless ohmic contacts to the $n^+$ regions are assumed. This structure was chosen because its moderate dopant levels help mitigate the omission of ionized impurity and electron- electron scattering. Figure 12 shows the current density ver- sus applied voltage computed with the Fermi kinetics model along with the EMC results from the literature [31]. The model with fully coupled real and momentum space dy- namics remained numerically stable, exhibiting quadratic convergence over the voltage range considered. The com- puted current densities are in approximate agreement with the EMC results. A salient difference is the reduced curva- ture of the Fermi kinetics result. This implies a lower rate of carrier heating and is consistent with the result in Fig. 11, which showed the velocity overshoot peak at slightly higher electric field. Consequently, the device simulation accuracy may be expected to improve along with the bulk drift veloc- ity result by incorporating more accurate band structure and scattering rates.

![](./images/811657061405294593_27.jpg)

Fig. 12 Current density of an $n^+nn^+$ GaAs structure computed with the Fermi kinetics transport model (solid line) and EMC (diamonds). EMC data computed by Shiktorov et al. [31]

## 7 Conclusion
Currently, full band Monte Carlo is likely the most faithful model of semiclassical hot electron transport in semiconduc- tors. Its discretization of time as well as real and momentum space, along with its stochastic treatment of free flight fol- lowed by scattering, closely emulate the way an ensemble of identical charged particles is believed to explore its phase space. The resulting particle trajectories are the underlying mechanisms behind a host of thermal physics concepts such as diffusion, work, heat, and entropy. EMC's ability to sub- sume all these concepts implicitly in its stochastic algorithm is a testimony to its predictive power and elegance. For the same reasons, it also speaks to the power and elegance of the thermal physics concepts themselves. Instead of tracking individual particles between specific initial and final states, these concepts can make quantitative statements about the charge ensemble's collective behavior using a small num- ber of properties (e.g. chemical potential and temperature) assigned to the charges en masse. Exploiting this collective behavior, it may be possible to simulate hot electron effects in semiconductor devices at a much smaller computational cost but with accuracy sufficient for computer-aided engi- neering purposes.

A possible charge transport model based on Fermi gas kinetics was proposed. It involves assigning separate Fermi functions to different regions of a semiconductor's elec- tronic band structure. Regions over which electron energy is an almost continuous function of its momentum and over

![](./images/811657061405294593_28.jpg)

which electrons experience similar scattering potentials are assigned the same Fermi distributions. Electrons move in real space between distributions occupying the same ranges of momentum space. At each position in real space, they also scatter in momentum space between the different distributions defined there. Since the Fermi distributions only depend on electron energy, momentum-dependent terms in the device equations can be integrated over electron energy isosurfaces extracted from the electronic band structure. This produces energy spectra for quantities such as the densities of states, electron velocities, and scattering rates, over which the Fermi functions can be integrated to obtain electron concentrations as well as charge and energy fluxes in both real and momentum space. It is through the isosurface integrals that the Fermi kinetics model incorporates electronic band dispersion. The ability to include band structure in this way owes to an alternative treatment of electronic heat flow based on the thermodynamic identity for ideal gases. This alternative is a significant departure from the electron thermal conductivity approach common to most energy transport models, and it offers the versatility and robustness required to generalize charge and energy fluxes for arbitrary band dispersion.

To demonstrate the concept, an initial version of the Fermi kinetics model was implemented. It used a number of simplifications including an approximate GaAs conduction band consisting of three nonparabolic valleys, scattering limited to polar optical mode and optical deformation potential processes, and the allotment of Fermi distributions in momentum space to maximally exploit the symmetry of the Brillouin zone. Simplifying assumptions notwithstanding, the model produced results for bulk electron drift velocity and $n^+nn^+$ device currents similar to those produced by full band EMC. Revisiting some of the key approximations will be the focus of further research on a Fermi kinetics model for accurate and numerically efficient hot electron semiconductor device simulation.

Acknowledgements The author acknowledges Prof. Doug Yoder (Georgia Institute of Technology) and Dr. Stephan Badescu (AFRL/RYDD) for helpful discussions of Monte Carlo simulation and electron dynamics. This work was supported by AFOSR Grant No. LRIR 09RY04COR.

## Appendix A: Fermi integrals for electron scattering

The collision operator (45) requires an integral over energy that includes the term,

$$
\begin{aligned}
I_{C}= & \left(n_{q}+1\right) f_{i}(E)\left[1-f_{f}(E-\hbar \omega)\right] \\
& -n_{q} f_{f}(E-\hbar \omega)\left[1-f_{i}(E)\right],
\end{aligned}
\tag{A.1}
$$

with the Bose-Einstein distribution $n_{q}$ and the Fermi distributions $f_{i}$ and $f_{f}$. When the Fermi distributions have the same temperature $T$, the functional forms of the Bose-Einstein and Fermi-Dirac distributions can be used to simplify the integrand. First, the definitions of the distribution functions produce the following relationships,

$$
n_{q}+1=n_{q} e^{\frac{\hbar \omega}{k_{\mathrm{B}} T_{a}}}
\tag{A.2}
$$

$$
1-f(E)=f(E) e^{\frac{E-F}{k_{\mathrm{B}} T}}.
\tag{A.3}
$$

The latter relationship allows the phonon absorption term in (A.1) to be expressed as,

$$
\begin{aligned}
f_{f}(E-\hbar \omega)\left[1-f_{i}(E)\right]= & f_{i}(E)\left[1-f_{f}(E-\hbar \omega)\right] \\
& \times e^{\frac{\hbar \omega+F_{f}-F_{i}}{k_{\mathrm{B}} T}}.
\end{aligned}
\tag{A.4}
$$

Subtracting $f_{i}(1-f_{f})$ from both sides gives,

$$
\begin{aligned}
f_{f}(E-\hbar \omega)-f_{i}(E)= & f_{i}(E)\left[1-f_{f}(E-\hbar \omega)\right] \\
& \times\left[e^{\frac{\hbar \omega+F_{f}-F_{i}}{k_{\mathrm{B}} T}}-1\right].
\end{aligned}
\tag{A.5}
$$

This relationship combined with (A.2) can be used to express (A.1) as,

$$
\begin{aligned}
I_{C}= & n_{q} \frac{\exp \left(\frac{\hbar \omega+F_{f}-F_{i}}{k_{\mathrm{B}} T}\right)-\exp \left(\frac{\hbar \omega}{k_{\mathrm{B}} T_{a}}\right)}{\exp \left(\frac{\hbar \omega+F_{f}-F_{i}}{k_{\mathrm{B}} T}\right)-1} \\
& \times\left[f_{i}(E)-f_{f}(E-\hbar \omega)\right],
\end{aligned}
\tag{A.6}
$$

and the collision operator (45) becomes the difference between incomplete Fermi integrals of order $\gamma$.

## Appendix B: Balance of heat and work for a closed two electron gas system

To investigate the conversion of chemical work into heat, two conduction band valleys, labeled $\Gamma$ and $L$, are considered. Their density of states spectra are shown in Fig. 13. One Fermi distribution $f_{\Gamma}$ is assigned to the $\Gamma$ valley with an initial temperature of 300 K and an initial electron density of $10^{18}\,\text{cm}^{-3}$. A separate distribution $f_{L}$ is assigned to the $L$ valley with an electron temperature of 400 K and density of $10^{17}\,\text{cm}^{-3}$. An elastic scattering mechanism is defined such that its isosurface integrals over initial and final states have the energy spectrum shown in Fig. 14. These isosurface integrals are similar to (44), but since this scattering is elastic, $\hbar\omega=0$ and the initial and final energies are the same. Consequently, the Fermi gases $f_{\Gamma}$ and $f_{L}$ together form a closed system in which the total particle and energy densities must be conserved.

![](./images/811657061405294593_29.jpg)

![](./images/811657061405294593_30.jpg)

Fig. 13 Density of states spectra for two arbitrary conduction band valleys

![](./images/811657061405294593_31.jpg)

Fig. 14 The isosurface integrals of an elastic scattering mechanism that governs the exchange of electrons between distribution functions assigned to the valleys represented in Fig. 13

Under these conditions, the Fermi gases $f_{\Gamma}$ and $f_{L}$ are allowed to start mixing at $t=0$ by exchanging charges and energy according to the elastic scattering process and the collision operator (50). Incrementing through time, the amount of heat flowing into each gas is computed from the thermodynamic identity [17],

$$
\begin{aligned}
Q_{\Gamma(L)}(t) & =\int_{0}^{t} k_{\mathrm{B}} T_{\Gamma(L)} \frac{d \sigma_{\Gamma(L)}}{d t} d t \\
& =\int_{0}^{t}\left[\frac{d E_{n, \Gamma(L)}}{d t}-F_{\Gamma(L)} \frac{d n_{\Gamma(L)}}{d t}\right] d t,
\end{aligned} \quad \text { (B.1) }
$$

as well as the amount of chemical work required to exchange the electrons,

$$
W_{\mathrm{net}}(t)=\int_{0}^{t}\left(F_{L}-F_{\Gamma}\right) C_{\Gamma}^{n} d t, \quad \text { (B.2) }
$$

where $C_{\Gamma}^{n}$ is the collision operator (50) that determines the rate electrons are transferred between the gases. The result in Fig. 15 shows that the net flow of heat, $Q_{\Gamma}+Q_{L}$ needed to increase the entropy of the combined system is balanced by

![](./images/811657061405294593_32.jpg)

Fig. 15 The changes in heat content $Q$ and the net chemical work performed $W_{\text {net }}$ as separate Fermi gases, labeled $\Gamma$ and $L$, begin exchanging electrons and energy at $t=0$ and approach equilibrium. The initial $\Gamma$ electron density was $10^{18} \mathrm{~cm}^{-3}$ and the electron temperature was $300 \mathrm{~K}$; the initial $L$ density was $10^{17} \mathrm{~cm}^{-3}$ and the temperature was $400 \mathrm{~K}$

![](./images/811657061405294593_33.jpg)

Fig. 16 Electron energy isotriangle approximated from eigenenergies at the vertices of a tetrahedron in the irreducible wedge

the chemical work performed, and this balance is achieved through conservation of the charges and their kinetic energy.

### Appendix C: Computing electron energy isosurfaces

Using an appropriate band structure theory, electron eigenenergies can be computed for the $\boldsymbol{k}$ vectors that form a tetrahedral mesh of the Brillouin zone's irreducible wedge, such as that shown in Fig. 2. The range of eigenvalues can then be divided into a number of discrete energy levels, and each tetrahedron may include one or more of these levels. For example, imagine one of the levels is 1.7 eV, and the tetrahedron in Fig. 16 has vertices with energies ranging from 1.4 to 1.9 eV. Assuming the energies vary piecewise linearly along the edges, edge points corresponding to 1.7 eV can be located. These points can be joined to form a triangle

![](./images/811657061405294593_34.jpg)

(or sometimes two triangles) that approximates a piece of the 1.7 eV isosurface.

The triangles forming the energy isosurfaces can be used to numerically approximate surface integrals of various quantities, such as densities of states and scattering rates. To make this easier, certain quantities can be assigned to each isosurface triangle and treated as constant over its area. For example, some scattering rates depend on the initial and fi- nal $\boldsymbol{k}$, and implementing these rates in the electron transport equations generally requires a double integral over both these wave vectors. Provided the irreducible wedge's mesh is sufficiently refined to smoothly represent the isosurfaces, treating an isosurface triangle's centroid ($\boldsymbol{c}$ in Fig. 16) as the $\boldsymbol{k}$ vector representing the whole triangle is a reasonable ap- proximation that greatly simplifies integrating $\boldsymbol{k}$-dependent quantities over the initial and final surfaces.

Invariably, isosurface integrals required for the transport equations also include the densities of initial and final states. The density of states per unit energy represented by an iso- surface triangle (56) can be expressed in terms of its surface area and the gradient of energy in $\boldsymbol{k}$ space $\nabla_{\boldsymbol{k}} E$. Electron group velocity is also related to the energy gradient. There- fore, assigning a gradient to each isosurface triangle fur- ther expedites numerically evaluating the integrals. Again assuming piecewise linear energy, each mesh edge repre- sents the projection of the local energy gradient along its length. Since a vertex of a given tetrahedron belongs to three of its edges, the projections along those edges can be used to compute a three-dimensional gradient vector at the ver- tex. For the centroid $\boldsymbol{c}$ of an isoenergy triangle inside this tetrahedron, the gradient can be approximated by the linear interpolation of the gradients at the vertices,

$$
\left.\nabla_{\boldsymbol{k}} E\right|_{\boldsymbol{c}}=\sum_{i} \lambda_{i}\left.\nabla_{\boldsymbol{k}} E\right|_{i} \tag{C.1}
$$

where the summation is over the tetrahedron's vertices $\boldsymbol{k}_{i}$, $\lambda_{i}$ are the barycentric coordinates describing the position of $\boldsymbol{c}$ in terms of the positions of $\boldsymbol{k}_{i}$ [32], and $\left.\nabla_{\boldsymbol{k}} E\right|_{i}$ is the gradient at $\boldsymbol{k}_{i}$. Each $\lambda_{i}$ is simply $V_{i} / V_{\text {tot }}$, where $V_{i}$ is the volume of a tetrahedron formed from $\boldsymbol{c}$ and the other three vertices $\boldsymbol{k}_{j \neq i}$, and $V_{\text {tot }}$ is the volume of the original tetra- hedron. The resulting energy gradient at the centroid can then be assumed constant over the surface of the triangle, thereby simplifying numerical approximations of isosurface integrals involving densities of states and/or electron veloc- ities.

### References

1. Fawcett, W., Boardman, A., Swain, S.: Monte Carlo determination of electron transport properties in gallium arsenide. J. Phys. Chem. Solids **31**, 1963–1990 (1970)

2. Shichijo, H., Hess, K.: Band-structure-dependent transport and impact ionization in GaAs. Phys. Rev. B **23**(8), 4197–4207 (1981)

3. Abramo, A., et al.: A comparison of numerical solutions of the Boltzmann transport equation for high-energy electron transport silicon. IEEE Trans. Electron Devices **23**(9), 1646–1654 (1994)

4. Saraniti, M., Goodnick, S.: Hybrid fullband cellular automa- ton/Monte Carlo approach for fast simulation of charge transport in semiconductors. IEEE Trans. Electron Devices **47**(10), 1909–1916 (2000)

5. Zhang, W., Du, G., Zhang, A., Mo, Z., Liu, X., Zhang, P.: A 3D parallel Monte Carlo simulator for semiconductor devices. IEEE Int. Workshop Comput. Electron. **1**(1), 1–4 (2009)

6. Baraff, G.: Maximum anisotropy approximation for calculating electron distributions; application to high field transport in semi- conductors. Phys. Rev. **133**(1), 26–33 (1964)

7. Liang, W., Goldsman, N., Mayergoyz, I., Oldiges, P.: 2-D MOS- FET modeling including surface effects and impact ionization by self-consistent solution of the Boltzmann. Poisson, and hole- continuity equations. IEEE Trans. Electron Devices **44**(2), 257–267 (1997)

8. Vecchi, M., Mohring, J., Rudan, M.: An efficient solution scheme for the spherical-harmonics expansion of the Boltzmann transport equation. IEEE Trans. Comput.-Aided Des. Integr. Circuits Syst. **16**(4), 353–361 (1997)

9. Gnudi, A., Ventura, D., Baccarani, G.: Two-dimensional MOS- FET simulation by means of a multidimensional spherical har- monics expansion of the Boltzmann transport equation. Solid- State Electron. **36**(4), 575–581 (1993)

10. Jungemann, C., Hong, S.M., Matz, G.: High-order spherical har- monics solution of the Boltzmann equation and noise modeling. Int. Workshop Comput. Electron. **1**(1), 1–6 (2010)

11. Rupp, K., Jungel, A., Grasser, T.: Matrix compression for spheri- cal harmonics expansions of the Boltzmann transport equation for semiconductors. J. Comput. Phys. **229**(1), 8750–8765 (2010)

12. Grasser, T., Tang, T.W., Kosina, H., Selberherr, S.: A review of hydrodynamic and energy-transport models for semiconductor de- vice simulation. Proc. IEEE **91**(2), 251–274 (2003)

13. Grupen, M.: An alternative treatment of heat flow for charge trans- port in semiconductor devices. J. Appl. Phys. **106**(1), 123702–123708 (2009)

14. Stratton, R.: Diffusion of hot and cold electrons in semiconductor barriers. Phys. Rev. **126**(6), 2002–2014 (1962)

15. Trovato, M., Reggiani, L.: Maximum-entropy principle for static and dynamic high-field transport in semiconductors. Phys. Rev. B **73**(1), 245209–245225 (2006)

16. Vasicek, M., Cervenka, J., Wagner, M., Karner, M., Grasser, T.: A 2D non-parabolic six-moments model. Solid-State Electron. **52**(1), 1606–1609 (2008)

17. Kittel, C., Kroemer, H.: Thermal Physics (2nd ed.). Freeman, New York (1980)

18. Hess, K.: Advanced Theory of Semiconductor Devices. IEEE Press, Piscataway (2000)

19. Goano, M.: Algorithm 745: Computation of the complete and in- complete Fermi-Dirac integral. ACM Trans. Math. Softw. **21**(3), 221–232 (1995)

20. Goano, M.: Series expansion of the Fermi-Dirac integral $\mathcal{F}_{j}(x)$ over the entire domain of real $f$ and $x$. Solid-State Electron. **36**(2), 217–221 (1993)

21. Scharfetter, D., Gummel, H.: Large-signal analysis of a silicon read diode oscillator. IEEE Trans. Electron Devices **16**(1), 64–77 (1969)

22. Selberherr, S.: Analysis and Simulation of Semiconductor De- vices. Springer, New York (1984)

23. Ridley, B.: Quantum Processes in Semiconductors (2nd ed.). Clarendon Press, Oxford (1988)

24. Ashcroft, N., Mermin, N.: Solid State Physics. Harcourt Brace, New York (1976)

![](./images/811657061405294593_35.jpg)

25. Yu, P., Cardona, M.: Fundamentals of Semiconductors: Physics and Materials (3rd ed.). Springer, New York (2005)

26. Cohen, M., Bergstresser, T.: Band structures and pseudopotential form factors for fourteen semiconductors of the diamond and zincblende structures. Phys. Rev. **141**(2), 789–796 (1966)

27. Harrison, P.: Quantum Wells, Wires, and Dots. Wiley, New York (2000)

28. Fischetti, M., Laux, S.: Monte Carlo analysis of electron transport in small semiconductor devices including band-structure and space-charge effects. Phys. Rev. B **38**(14), 9721–9745 (1988)

29. Saraniti, M., Hu, Y., Goodnick, S., Wigger, S.: Overshoot velocity in ultra-broadband THz studies in GaAs and InP. Physica B **314**(1), 162–165 (2002)

30. Sotoodeh, M., Khalid, A., Rezazadeh, A.: Empirical low-field mobility model for III–V compounds applicable in device simulation codes. J. Appl. Phys. **87**(6), 2890–2900 (2000)

31. Shiktorov, P., Gružinskis, V., Starikov, E., Reggiani, L., Varani, L.: Noise temperature of $n^+nn^+$ GaAs structures. Phys. Rev. B **54**(12), 8821–8832 (1996)

32. Silvester, P., Ferrari, R.: Finite Elements for Electrical Engineers (3rd ed.). Cambridge University Press, Cambridge (1996)

![](./images/811657061405294593_36.jpg)
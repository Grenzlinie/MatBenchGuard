# Numerical simulation of transient phonon heat transfer in silicon nanowires and nanofilms

This content has been downloaded from IOPscience. Please scroll down to see the full text.

2007 J. Phys.: Conf. Ser. 92 012077

(http://iopscience.iop.org/1742-6596/92/1/012077)

View [the table of contents for this issue](the table of contents for this issue), or go to the [journal homepage](journal homepage) for more

Download details:

IP Address: 198.91.36.79
This content was downloaded on 21/02/2015 at 03:44

Please note that [terms and conditions apply.](terms and conditions apply.)

# Numerical simulation of transient phonon heat transfer in silicon nanowires and nanofilms

D Terris¹, K Joulain¹, D Lacroix² and D Lemonnier¹

¹Laboratoire d'études thermiques, ENSMA, B.P 109, 86961 Futuroscope Chasseneuil, France
²LEMTA, Université Henri Poincaré, 54506 Vandœuvre les Nancy, France

E-mail: karl.joulain@ensma.fr

**Abstract.** This work proposes a numerical simulation of heat conduction in silicon nanowires and nanofilms. Boltzmann equation for phonons is solved in the relaxation time approximation. The equation is integrated in an axisymmetric cylindrical two dimensional geometry. Solid angle integration is done by means of Discrete Ordinate Method. Moreover, in contrast to other models published in literature, spectral dependency of relaxation times and acoustic wave dispersion are taken into account in this numerical resolution. Consequently, thermal profiles are obtained for silicon nanowires and nanofilms in steady state allowing computation of thermal conductivity and/or thermal conductance. Besides, we solve the unsteady Boltzmann equation in order to obtain nanosystems temporal evolution. The results obtained with this code match nanofilms and nanowires already predicted thermal profiles in steady state. In unsteady condition, diffusive state (Fourier) is discussed for nanowires and nanofilms. At low temperatures, ballistic phenomenons are seen in nanofilms, whereas, in nanowires, due to boundary scattering, diffusion regime is observed.

## 1. Introduction
Silicon, due to its mechanic and electronic properties, is an essential element in high technology development. Electronic devices such as junctions are made of semiconductor stacks. Silicon nanowires enter now in parts of sensors [1], electronic [2] as well as field effect transistors [3, 4]. Moreover, the continuous development of nanotechnology has led to the development of new semiconductor structures in various fields such as computer chips or energy production by thermoelectric effects or solar concentration [5]. The knowledge of the temperature field in such structures is now critical in order to optimize the thermal cooling or the efficiency of such devices. At nanometer scale, even at ambient temperature, the phonons mean free path can be larger than the system size. The classical laws of thermal conduction such as the Fourier law has to be questionned. Indeed, the thermal transfer may be ballistic or semi-ballistic. The temporal thermal behaviour can also be important due to the fact that semiconductor components undergo high frequency cycles. In order to solve these problems, several methods can be considered such as molecular dynamics [6, 7, 8] or Boltzmann Transport Equation (BTE) for phonons in the relaxation time approximation. This last problem has already been adressed in the past [9, 10]. Analytical method [11, 12, 13], Monte-Carlo method [14] and direct integration [11] has produced interesting results. Yet, these works have neither been considered in the transient regime, nor have taken into account the wave dispersion in the medium.


A method of the BTE integration for phonons is presented in an axisymmetric cylindrical geometry. This symetry yields to a bidimensional system. Numerical calculations are first performed in steady state. The validation is done for bulk materials by setting phonon reflection to be specular at cylinder lateral boundaries. The transition between ballistic and Fourier's regime is exhibited for nanofilms. Therefore, the typical scale for which it is possible or not to talk about a thermal conductivity is calculated. In a second case, this method is applied to nanowires, where phonon reflection at lateral boundaries is set as purely diffuse. Typical thermal properties, that have been observed experimentally, are retrieved. Finally, the temperature evolution is calculated in the transient regime in silicon nanowires and nanofilms.

## 2. Numerical method
In this work, the BTE for phonons is solved in the relaxation time approximation, where all collision phenomenons are considerated. They tend to relax the system to an equilibrium solution. A specific intensity $I_{\omega,p}(\mathbf{r}, \boldsymbol{\Omega})$ [15] for phonons is introduced. It depends on the angular frequency $\omega$, on the phonon polarized branch $p$, and on the position $\mathbf{r}$ and direction $\boldsymbol{\Omega}$. The position reads in cylindrical coordinates $\mathbf{r} = (r, \theta, z)$ whereas the direction $\boldsymbol{\Omega}$ is determined by two angles $(\phi, \psi)$ or three direction cosines $(\mu, \eta, \xi)$. This phonon specific intensity represents the phonon energy flux per surface unit at position $\mathbf{r}$ in an elementary solid angle around direction $\boldsymbol{\Omega}$. In cylindrical coordinates and if the problem is axisymetric, the BTE reads

$$
\frac{1}{v g_{\omega, p}} \frac{\partial I_{\omega, p}}{\partial t}+\frac{\mu}{r} \frac{\partial\left(r I_{\omega, p}\right)}{\partial r}-\frac{1}{r} \frac{\partial\left(\eta I_{\omega, p}\right)}{\partial \phi}+\xi \frac{\partial I_{\omega, p}}{\partial z}+\kappa_{\omega, p} I_{\omega, p}=\kappa_{\omega, p} I_{\omega, p}^{0} \tag{1}
$$

In this expression, $v g_{\omega,p}$ is the phonon group velocity at the angular frequency and polarization considered, $\kappa_{\omega,p}$ is an equivalent phonon absorption coefficient and $I_{\omega,p}^0$ is an equilibrium phonon specific intensity. $I_{\omega,p}^0$ can be seen as the product of the phonon density of states, multiplied by the mean energy of a phonon at equilibrium temperature $T$, and by the group velocity over $4\pi$.

The equivalent phonon absorption coefficient can be expressed in terms of relaxation time $\kappa_{\omega,p} = 1/(v g_{\omega,p} \tau_{\omega,p})$ where $\tau_{\omega,p}$ is the total relaxation time. Note that the phonon dispersion is taken into account. Phonons interactions are done with impurities (modeled by a Rayleigh scattering expression $\tau_i \propto \omega^4$), normal anharmonic intercation ($\tau_N \propto \omega^2 T^3$) and umklapp anharmonic intercation ($\tau_U \propto \omega^2/\sinh(\hbar\omega/k_b T)$ at high frequencies). The total inverse relaxation time is obtained taking the sum of the inverse individual relaxation times (Matthiessen's rule). In this work, only acoustic phonon modes are focused. Indeed, in the case of silicon, taking into account only acoustic modes is sufficient to retrieve silicon thermal conductivity. Moreover, anisotropy is not taken into account in this work. The two acoustic branch expressions are outcome from the literature [16] where group velocity has been measured in the direction [100]. For each time step and position, the temperature is required to calculate specific intensities. The temperature is then calculated by solving the following implicit equation

$$
\sum_{p} \int_{0}^{\infty} d \omega \int d \Omega \kappa_{\omega, p} I_{\omega, p}(\mathbf{r}, \boldsymbol{\Omega})=\sum_{p} \int_{0}^{\infty} d \omega \int d \Omega \kappa_{\omega, p} I_{\omega, p}^{0}(T(\mathbf{r})) \tag{2}
$$

The cylinder is spatially discretized with a rectangular mesh in the $(r,z)$ plane. The angular discretization is done along the so called discrete ordinate directions [17]. The SN8 quadrature used here has 80 directions for which angular integration of (1) is performed.

Using the following boundary conditions, at $t=0$, a temperature at both ends of the cylinder is imposed. The lateral boundaries are adiabatic. If the phonon reflection is specular, the system is equivalent to a film due to the phonon momentum conservation. If the phonon reflection is diffuse, the system is a wire. In the case of a film, when the cylinder length is much larger than the phonon mean free path, one has to retrieve the classical heat conduction transfer behaviour.


![](./images/811946986369449986_1.jpg)
![](./images/811946986369449986_2.jpg)

**Figure 1.** Left: Thermal conductance of films versus thickness for different temperatures. Right: Nanowire thermal conductivity versus temperature for different diameters: 37 nm (lower curves), 56 nm (middle curves) and 115 nm (upper curves). Our simulation, experimental measurements [18] (triangle) and other models (Lacroix [14] and Chantrenne [19]).

At steady state, temperature varies linearly and heat flux reads as the Fourier's law $\mathbf{q} = -\lambda \nabla T$ where the conductivity $\lambda$ does not depend on the system size.

### 3. Heat flux in nanofilms and nanowires
New relaxation times have been computed to retrieve the bulk silicon thermal conductivity over the whole range of temperature. With these relaxation times, at steady state, the heat flux and the thermal conductance $(Q/\Delta T)$ of films are calculated for different thicknesses $d$ and at different temperatures $T$. For each $T$, the existence of three regimes can be noted. A low thickness regime where the heat flux does not depend on $d$, a transition regime and a high thickness regime where the heat flux decreases as $d^{-1}$. The first regime described is the ballistic regime where phonon mean free path is much larger than $d$ (Fig.1 left). On the contrary, in the high thickness regime, phonon mean free path is much lower than $d$ and the Fourrier law is valid. Temperature in the medium varies linearly and conductivity is $d$-independant. The intermediate regime occurs for thicknesses of the same order than phonon mean free path. In this so called mesoscopic regime, thermal behaviour is very similar to an absorbing medium in radiation transfer. Note that the concept of thermal conductivity has a meaning only in the Fourier regime. In silicon case, it can be seen that this regime is reached only for distances larger than the micrometer scale even at high temperature. Our method is compared with a simpler one developped by Yang et al. [10] based also on the discrete ordinate method but without any group velocity and relaxation times angular frequency dependence. A 30% deviation of the results produced by these methods shows the requirement of taking account such an angular frequency dependence.

The reflection of phonons at lateral boundaries is now setted as purely diffuse. Phonon mean free path is of the wire diameter order which is much lower than its length. Thus, a wire with purely diffuse reflection for phonons is always in the Fourier regime, where thermal conductivity is then a relevant quantity. At steady state, we have computed nanowire thermal conductivity and we have compared it with experimental measurements [18] as well as with other models [14, 19]. The comparison is shown in Fig.1 (right) and shows a good agreement between our simulation and experimental measurements [18].

### 4. Thermal temporal evolution of nanowire and films
Lets focus on temperature temporal evolution in nanostructures. At $t = 0$, a temperature $T_i$ is imposed on the cylinder left side different from the initial temperature $T_i$ of the entire cylinder at $t < 0$. $T_i$ is also imposed on the cylinder right side at any time. The case of a 1 m thick film is treated around a 10 K temperature and as well as the case of a 1 m long and 37 nm diameter

![](./images/811946986369449986_3.jpg)

Figure 2. Left: Temperature evolution of a $1\mu$m thick film around 10 K. Right: Temperature evolution of a $1\mu$m long and 37nm diameter nanowire around 10 K.

silicon nanowire. In the film case, a two steps temperature increasement appears (Fig.2 left). A fine analysis shows that these steps correspond to two ballistic phonon propagations, transverse acoustic phonon and longitudinal acoustic phonon propagations. The temperature evolution in the nanowire is very different (Fig.2 right). It looks like a typical temperature evolution in the Fourier regime. This is coherent with the previous discussion where we have noted that a nanowire is in Fourier's regime.

## 5. Conclusion
A numerical code has been developped to solve the BTE in nanofilms and nanowires based on the discrete ordinate method in steady states and in transient regimes. The knowledge of phonon dispersion relation and relaxation times is required. It has been shown that this code retrieves the classical thermal properties of silicon nanowires and nanofilms. It appears that the concept of thermal conductivity has to be used carefully when nanostructure dimensions reaches phonon mean free path. This code could be used in the future to treat the temporal thermal behaviour in nanostructures submitted to high frequency temperature excitations such as in electronic devices.

## References
[1] Fan Z and Lu J G 2005 *Appl. Phys. Lett.* **86** 123510
[2] Thelander C, Nilsson H A, Jensen I E and Samuleson L 2005 *Nano Lett.* **5** 635
[3] Ng H T, Han J, Yamada T, Nguyen P, Chen Y P and Meyyappan M 2004 *Nano Lett.* **4**(7) 1247-1252
[4] Schmidt V, Riel H, Senz S, Karg S, Riess W and Gösele U 2006 *Small* **2** 85-88
[5] Bett A W 2004 in *Next Generation Photovoltaics* IOP series in optics and optoelectronics, Ed. Marti A and Luque A
[6] Volz S and Chen G 1999 *Appl. Phys. Lett.* **75** 2056-2058
[7] Volz S and Chen G 2000 *Phys. Rev. B* **61** 2651-2656
[8] Gomes C J 2006 *ASME J. Heat. Transf.* **128** 1114-1121
[9] Majumdar A 1993 *ASME J. Heat. Transf.* **115** 7-16
[10] Yang R and Chen G 2005 *Nano Lett.* **5** 1111-1115
[11] Holland M 1963 *Phys. Rev.* **132** 2461
[12] Chen G 2001 *Phys. Rev. Lett.* **86** 2279-2300
[13] Prasher R 2006 *Appl. Phys. Lett.* **89** 063121
[14] Lacroix D, Joulain K and Lemonnier D 2005 *Phys. Rev. Lett.* **72** 064305
[15] Lemonnier D and Lallemand M 2000 *Heat and Technology* **18**
[16] Pop E, Dutton R W and Goodson K E 2004 *J. Appl. Phys* **96** 4998-5005
[17] Fiveland W A 1982 *ASME* 82-HT-20
[18] Li D, Wu Y, Kim P, Yang P and Majumdar A 2003 *Appl. Phys. Lett.* **83** 2934-2936
[19] Chantrenne P, Barrat J-L, Blase X and Gale J 2005 *J. Appl. Phys.* **97** 104318
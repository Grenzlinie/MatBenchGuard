GEOPHYSICAL RESEARCH LETTERS, VOL. 23, NO. 16, PAGES 2193-2196, AUGUST 1, 1996

# Particle simulation of the time-dependent interaction with the ionosphere of rapidly varying lightning EMP

Vyacheslav S. Glukhov
Center for Space Science and Astrophysics, Stanford University, Stanford, California

Umran S. Inan
Space, Telecommunications and Radioscience Laboratory, Stanford University, Stanford, California

**Abstract.** The interaction with the lower ionosphere of rapidly varying electromagnetic pulses (EMPs) produced by lightning discharges is studied. The nonlinear heating, ionization and optical emission production are modeled using the Monte Carlo technique, which allows for consideration of realistic lightning EMPs with a few $\mu$s rise times. Results indicate that the electron distribution function is highly anisotropic during the first few $\mu$s of the interaction, but subsequently develops into a near-isotropic quasi-stationary state. The peak optical emissions intensities are found to be highly dependent on the EMP waveform, while the altitude range at which the emissions occur is relatively independent of pulse shape. Results of the particle simulation are used to assess the range of applicability of the quasi-stationary models [*Taranenko et al.*, 1993; *Inan et al.*, 1996].

## Introduction

Interaction with the lower ionosphere of EMPs radiated by lightning discharges is believed to lead to ionization changes and optical emissions [*Inan et al.*, 1991; *Taranenko et al.*, 1993; *Rowland et al.*, 1995]. The most recent two dimensional modeling of the EMP-ionosphere interaction [*Inan et al.*, 1996] has revealed the space-time dynamics of the resulting optical emissions to be in the form of a thin cylindrical shell rapidly expanding in time and having a duration of few hundred microseconds. Recent high time resolution photometric measurements [*Fukunishi et al.*, 1996] have uncovered a transient (< 1 ms duration) type of optical flash occuring at ionospheric heights of > 80 km and having a lateral extent of ~ 300 km. The new type of flash, sometimes referred to as "elves", are quite distinct from the luminous glows, referred to as "sprites", occuring at 50 – 85 km altitudes above thunderclouds [*Sentman et al.*, 1995 and references therein]. Typical sprites have a columnar shape with 10 – 50 km lateral extent and last for a few to many tens of milliseconds, as opposed to the < 1 ms duration of elves. The observed aspects (temporal duration, spatial extent) of elves are consistent with heating of the lower ionosphere electrons by EMP [*Inan et al.*, 1996], while the sprites are believed to be produced via heating by quasi-electrostatic thundercloud fields [*Pasko et al.*, 1995]. In this paper we consider the interaction with the lower ionosphere of EMPs with rapidly varying features.

A 1-D quasi-stationary kinetic model of ionization changes and optical emissions due to heating of ambient electrons by lightning EMPs was developed by [*Taranenko et al.*, 1993]. The main assumption of this model was that the distribution function of electrons, and, therefore, all observable quantities such as ionization, attachment and optical emission rates, are determined by the instantaneous magnitude of the electric field $E(t)$. This assumption implied that the electric field of the EMP does not change significantly during the period of relaxation of the distribution function $f(x, v, t)$ to an equilibrium state. In the important altitude range of 80 – 90 km, the equilibrium state is typically established in less than $10\mu$s, so that it was necessary to limit the application of the quasistationary model to waveforms with spectral content below 50 kHz.

Ground-based observations of the shapes of EMPs associated with lightning discharges [*Uman*, 1987, p.110] indicate that the most common lightning EMP waveforms have two distinct parts – an initial surge reaching a peak value over a time scale $\approx 2\mu$s followed by a more gradual change over a time scale $\approx 100\mu$s. While the latter can be regarded as quasi-stationary with respect to the $\approx 10\mu$s relaxation time of $f(x, v, t)$, the $\approx 2\mu$s duration of the former is of the same magnitude as the collision time of ambient electrons at altitudes of interest, which raises questions about the applicability of the quasi-stationary model.

In this paper we develop and apply a simple fully-kinetic time-dependent model of the propagation of a lightning EMP through the lower ionosphere and present the results of the simulations for realistic EMP waveforms. This model allows us to determine the range of applicability of the quasi-stationary approach and to study the problem at or beyond these limits.

## Model

We consider a simple model of electron acceleration in a constant external electric field. The equation of motion for the electrons is given by

Copyright 1996 by the American Geophysical Union.
Paper number 96GL02185
0094-8534/96/96GL-02185$05.00

$$
\frac{dv}{dt} = -\frac{eE}{m_{\mathrm{e}}} - \nu v, \tag{1}
$$

where $v$ is the electron velocity; $e$ and $m_{\mathrm{e}}$ are the electron charge and mass, respectively; $E$ is the electric field, $\nu = N\sigma v$ is the collision frequency, $N$ is the density of neutrals, $\sigma$ is the total scattering cross section. The characteristic time scale for the nonlinear equation (1) is $\tau_{\mathrm{eq}} = \sqrt{eEN\sigma/m_{\mathrm{e}}}$, i.e., the time necessary to establish the equilibrium value of the electron velocity $v_{\mathrm{eq}} = -eE\tau_{\mathrm{eq}}/m_{\mathrm{e}}$. For a typical value $E = 50\mathrm{V/m}$ and $\sigma$ of order of $10^{-15}\mathrm{cm}^{-2}$ [Phelps, 1987] we obtain $\tau_{\mathrm{eq}} \approx 0.5\mu\mathrm{s}$ at $\approx 90\mathrm{km}$ altitude. This value is only slightly less than the $2\mu\mathrm{s}$ typical rise time of a lightning EMP [Uman, 1987, p.110]. Taking into account the time-dependence of the electric field we conclude that in reality $\tau_{\mathrm{eq}}$ can be several times larger than $0.5\mu\mathrm{s}$. During the time interval $0 < t < \tau_{\mathrm{eq}}$ the electrons gain energy without significant spread in velocity space. For this reason, the distribution function of electrons during this time interval is neither quasi-equilibrium nor quasi-isotropic.

In a weakly ionized collisional medium the response of free electrons to an external electric field depends on three basic processes: the momentum gain in the direction of the electric field, the momentum loss due to elastic collisions with neutrals, and the energy loss due to inelastic collisions with neutrals. Effective momentum transfer cross-sections and the energy loss function for electrons in air are fairly well known [Taranenko et al., 1993 and references therein]. In this article we simplify the solution of the Boltzmann equation for electrons by using the Monte Carlo method and by replacing numerous inelastic collision cross sections by a single "effective" inelastic cross section. The validity of this approximation is verified by comparing our results in the quasi-stationary limit with the results of quasi-stationary fully-kinetic simulations [Taranenko et al., 1993]. The Monte Carlo simulation methods have been used successfully for evaluating parameters of electron swarms [see, for example Liu and Govinda Raju, 1992]. It the following, we use this method to determine the time dependent evolution of the electron distribution function under the influence of lightning EMPs with rapidly varying features.

### Monte Carlo simulations; the algorithm

Our implementation of the Monte Carlo method involves the following steps.

The altitude range from 70 to 100 km is divided into a sufficiently large number of cells whose spatial scale depends on the shortest wavelength of EMP that we aim to resolve (300 m). The electric and magnetic fields are calculated by solving Maxwell's equations using the Lax-Wendroff [Potter, 1973] algorithm. At each cell, the following procedure is used to calculate the observable quantities:

1. Particle velocities $v_{\parallel}, v_{\perp}$ are distributed initially normally with a standard deviation corresponding to a given temperature. The number of particles ($10^4$ in our simulations) in each cell is taken to be large enough that the statistical variance of the current density (proportional to $N^{-1/2}$) is smaller than its average value.

2. For each particle $i$, $v_{\parallel i}$ is set to $v_{\parallel i} - eE\delta t/m_{\mathrm{e}}$, where $\delta t$ is the time step.

3. For each $i$, $P_i = N\sigma_{\mathrm{tot}}(\epsilon_i)v_i\delta t$ is calculated, where $P_i$ is the probability that the $i$th particle collides during $\delta t$, $N$ is the density of neutrals, $\epsilon_i, v_i$ are the energy and the absolute value of the particle velocity and $\sigma_{\mathrm{tot}}(\epsilon)$ is the energy-dependent total scattering cross section. We choose $\delta t$ to be so small that $P_i \ll 1$.

4. For each particle $i$ such that $P_i \geq p_i$, where random $p_i$s are uniform in [0,1], $v_i$ is set to $v_i\sqrt{1 - \sigma_{\mathrm{in}}(\epsilon_i)/\sigma_{\mathrm{tot}}(\epsilon_i)}$, $v_{\parallel i}$ and $v_{\perp i}$ are equaled to $v_i \cos\theta_i$ and $v_i \sin\theta_i$,respectively, where $\sigma_{\mathrm{in}} = F(\epsilon_i)/\epsilon_i v_i$, and $F(\epsilon_i)$ is the energy loss function for electrons in air [Taranenko et al., 1993]; random variables $\theta_i$ are uniform in $[0, 2\pi)$. At each time step the energy and momentum losses are calculated only for a small subset of particles defined by inequality $P_i \geq p_i$. In our case, this procedure significantly reduces the computational time.

5. Observable quantities (the current density, the average energy, the rates of ionization, attachment and optical excitations) are calculated as necessary.

6. The current density is fed back to the Lax-Wendroff code used for calculating the electric and magnetic fields for the next time step.

7. The optical emissions in the 1st and 2nd positive bands of $N_2$ are calculated using the known excitations, transition and quenching rates [Taranenko et al., 1993].

Figure 1 shows the evolution of the electron distribution function $f(v_{\parallel}, v_{\perp})$ in velocity space for a single simulation cell corresponding to 90 km altitude. The characteristic time over which $f(v_{\parallel}, v_{\perp})$ becomes isotropic is about $1\mu\mathrm{s}$, in good agreement with our crude estimates. Even after the distribution becomes isotropic ($t \simeq 1\mu\mathrm{s}$) $f(v_{\parallel}, v_{\perp})$ is still far from an equilibrium state and exhibits a ring-like structure with a gap corresponding to the first barrier of energy losses at $\epsilon \approx 2\mathrm{eV}$. The evolution of the moments of the distribution function $f_n = \|f(v\cos\theta, v\sin\theta)P_n(\cos\theta)\|$, where

![](./images/812370082775695360_1.jpg)

**Figure 1.** a,b,c: Distribution of electrons in the velocity space. Electric field $E = 50\mathrm{V/m}$ is turned on suddenly at $t = 0$, $v_{\parallel}, v_{\perp}$ are in $10^7\mathrm{cm/s}$. d: Normalized moments of the distribution function. Solid line $- f_0$, dotted $- f_1$, dashed $- f_2$, dot-dashed $- f_3$.

$\|\cdot\|$ denotes the norm so chosen that $\sum f_n = 1$, shows that the distribution can be termed to be truly quasi-stationary and near-isotropic only for $t > 1.5\mu\text{s}$.

In order to verify the accuracy of the Monte Carlo method we carried out a set of simulations with the same EMP parameters and ambient ionospheric conditions as in [Taranenko et al., 1993]. The results, not shown here for the sake of brevity, were found to be in excellent agreement.

## Results
### Dependence on the rise time of EMP

The following 3-parametric waveform was used to approximate the observed shapes of lightning EMPs:

$$
E(t) = E_{\text{max}} \cos\left(\frac{2\pi t}{T_1}\right) u(t, T_2) w(t, T_3)
$$

where $u(t, T_2) = 1-\exp(-t/T_2), w(t, T_3) = \exp(-t/T_3)$; $T_1$ is used to match the "zero-field crossing" time [Uman, 1987, p.110], usually several tens to a few hundreds of $\mu\text{s}$; $T_2$ is approximately the rise time of the pulse (typically $\geq 2\mu\text{s}$), and $T_3$ can be used to adjust the ratio of maximum positive to maximum negative value of the electric field in the EMP. With the proper choice of $T_1$,$T_2$ and $T_3$, a wide range of lightning EMP waveforms can be realized.

Figure 2 shows the results of the simulations for EMPs with the following parameters: $T_1 = 100\mu\text{s}, T_2 = 2,5,10,25\mu\text{s}$, $T_3 = 50\mu\text{s}$. By an appropriate choice of $E_{\text{max}}$, each EMP was made to carry the amount of energy equal to that of an EMP with parameters $T_1 = 100\mu\text{s}$, $T_2 \to 0\mu\text{s}$, $T_3 = 50\mu\text{s}$, $E_{\text{max}} = 50\text{V/m}$. The first column of Figure 2 shows the EMP waveforms in the lower ionosphere at different times. Comparison of the waveforms at $t = 70\mu\text{s}$ and at $t = 150\mu\text{s}$ indicates that a significant part of the energy of the EMP is deposited in the ionosphere. The maximum increase of the average energy of electrons (third column in Figure 2) and rates of optical emission in the 1st positive band of $N_2$ (second column in Figure 2) are in the ranges of altitudes from 85km to 95km, in which the EMPs are reflected.

Reflection of the EMPs creates interference patterns of the electric field which are reproduced in spatial and temporal patterns of optical emissions. Interference between the downward propagating "head" and the upward propagating "tail" of the EMP results in weak dependence of the maximum attainable absolute value of the electric field on the shape of the EMP. Such "constructive" interference yields almost equal emission rates (e.g. , at $t = 110\mu\text{s}$ in Figure 2). However, because of the highly nonlinear dependence of optical excitations on the absolute value of the electric field, the different EMP waveforms may lead up to an order of magnitude difference in optical emission rates for the time intervals when interference does not occur ($t = 70\mu\text{s}$ and $t = 150\mu\text{s}$ in Figure 2).

![](./images/812370082775695360_2.jpg)

Figure 2. EMP electric field, rate of optical emission in the 1st positive $N_2$ band and the average energy: 1st, 2nd and 3rd column, respectively. Solid, dashed, dotted, dot-dashed lines represent $T_2 = 2, 5, 10, 25\mu\text{s}$, respectively.

### Dependence on the pulse width

We now investigate the dependence of optical emissions on the width and the amplitude of the EMP. For this purpose we use EMPs with an artificial shape $E(t) \sim \cosh^{-1}(t/T_2)^2$, $T_2 = 5,7,10,20\mu\text{s}$, in order to eliminate effects of "constructive" interference between different parts of the pulse.

In Figure 3 we compare maximum, time-integrated, and altitude-integrated emission rates (rows from top to bottom, respectively) for realistic shapes of EMPs, considered in the previous subsection, and also including cosh-shapes of equal energy and cosh-shapes of equal amplitude (columns from left to right, respectively).

The maximum emission rates (first row in Figure 3) change only slightly for realistic EMPs and cosh-EMPs of equal amplitude, whereas for cosh-EMPs of equal energy the maximum emission rates are lower for lower amplitude, as expected. For the case of realistic EMPs (first column in Figure 3) the maximum amplitude of the electric field depends only weakly on the shape of the pulse. We conclude that the maximum emission rates are determined mainly by the maximum amplitude of the electric field of the reflected pulse.

Contrary to the maximum emission rates, the time-integrated emission rates (second row in Figure 3) depend on the total energy of the pulse. The only significant deviation from this rule is the widest ($20\mu\text{s}$) cosh-EMP of equal energy. A wider pulse must have lower reflection altitude and, there-

![](./images/812370082775695360_3.jpg)

Figure 3. Maximum emission rates, time-integrated emission rates, altitude-integrated emission rates and the EMP electric field: 1st, 2nd, 3rd, 4th row, respectively. Realistic EMPs, cosh-EMPs of equal energy, cosh-EMPs of equal amplitude: 1st, 2nd, 3rd column, respectively. $T_2$ for realistic EMPs are the same as in Figure 2. Solid, dashed, dotted, dot-dashed: $T_2 = 5,7,10,20\mu s$, respectively, for cosh-EMPs.

fore, the total energy brought to the 90km altitude, where most of the energy is deposited, is relatively smaller. Although the reflection altitude does not change much with frequency, several km difference in the reflection altitude yields several times difference in emission rates, due to the highly nonlinear nature of the interaction of EMPs with the ionosphere.

The altitude-integrated emission rates (third row in Figure 3) confirm our conjecture that interference play a significant role in determining the maximum emission rates. Double-peaked time dependence of the optical emissions (realistic EMPs, first column in Figure 3) mirrors the behavior or the electric field as the up going EMP interferes with its down going reflection in the altitude region where most of its energy is absorbed. Note that cosh-EMPs do not show any interference pattern, except for the widest $20\mu s$ pulses. This result indicates that the widest pulses suffer from "destructive" interference, that is, the "tail" of the pulse interferes with the reflected "head" of opposite sign. If the width of the pulse is sufficiently large, the "destructive" interference produces a gap in the time dependence of the altitude-integrated emission rates.

## Conclusion
Our results indicate that previously used [Taranenko et al., 1993; Inan et al., 1996] quasi-stationary simulations of the interaction with the lower ionosphere of lightning EMPs are applicable for EMP waveforms with spectral content below 50 kHz. Results of our more general treatment indicate that when the EMP has an initial rapid (a few $\mu s$) rise, the bulk features of the resultant optical emissions (e.g., altitude range of excitations, duration and optical pulse shapes) are very similar to those calculated using the quasi-stationary models.

The spatial and temporal patterns of optical emissions are determined by the structure of the electric field in the pulse. The maximum optical emission rates depend on the maximum attainable value of the EMP electric field. The total optical emission energy depends on the total energy of the pulse brought to the altitude $\approx 90$km. Interference play a significant role in determining the temporal patterns of optical emissions.

## Acknowledgments
This work was supported by NSF under grant ATM-9412287 to Stanford University. We appreciate consultations with our colleagues in the STAR Laboratory and with Y. Taranenko of LANL.

## References
Fukunishi, H.Y., Y. Takanashi, M. Kubota, K. Sakanoi, U.S. Inan and W.A. Lyons, Elves: Lightning-induced transient luminous events in the lower ionosphere, to apper in the August, 1st 1996 issue of the Geophys. Res. Lett.

Inan, U.S., W.A. Sampson and Y.N Taranenko, Space-time structure of optical flashes and ionization changes produced by lightning-EMP, Geophys. Res. Lett., 23, 133, 1996.

Liu,J. and G.R. Govinda Raju, Monte Carlo simulation of electron motion in mercury vapour, J. of Physics D, (Applied Physics), 25, 167, 1992.

Pasko, V.P., U.S. Inan, Y.N. Taranenko and T.F. Bell, Heating, ionization and upward discharges in the mesosphere due to intense quasi-electrostatic thundercloud fields, Geophys. Res. Lett., 22, 365, 1995.

Phelps, A.V., Excitation and ionization coefficients, Gaseous Dielectric,vol. 5, 1987.

Potter, D. Computational physics, London, New York, J.Wiley, 1973.

Rowland,H.L., R.F. Fernsler, J.D.Huba, and P.A. Bernhard, Lightning driven EMP in the upper Atmosphere, Geophys. Res. Lett., 22, 361, 1995.

Taranenko, Y.N., U.S. Inan and T.F. Bell, The interaction with the lower ionosphere of electromagnetic pulses from lightning: excitation of optical emissions, Geophys. Res. Lett., 20, 2675, 1993.

Uman, M.A., The lightning discharge, Academic Press, Orlando, 1987.

V.S. Glukhov, CSSA, Stanford University, Stanford, CA 94305
U.S. Inan, STAR Lab, Stanford University, Stanford, CA 94305

(received April 1, 1996; accepted July 1, 1996.)
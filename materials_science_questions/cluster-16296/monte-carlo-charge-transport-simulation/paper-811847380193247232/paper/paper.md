Variation of transport properties along the channel of a high electron mobility transistor: a quantum influence

This content has been downloaded from IOPscience. Please scroll down to see the full text.

1997 Semicond. Sci. Technol. 12 771

(http://iopscience.iop.org/0268-1242/12/7/003)

View the table of contents for this issue, or go to the journal homepage for more

Download details:

IP Address: 137.149.200.5
This content was downloaded on 04/09/2015 at 01:41

Please note that terms and conditions apply.

# Variation of transport properties along the channel of a high electron mobility transistor: a quantum influence

N Balakrishnan and R Venkat

Department of Electrical and Computer Engineering, University of Nevada,
Las Vegas, NV 89154-4026, USA

Received 30 October 1996, in final form 3 February 1997, accepted for publication
3 April 1997

**Abstract.** In the theoretical modelling of a high electron mobility transistor (HEMT), it is inherently assumed that there is little variation in quantum confinement along the channel from source to drain and therefore the transport properties are independent of the position and only dependent on the electric field along the channel. In this study, the scattering rates for bulk polar optical phonons, bulk acoustic phonons (through deformation potential) and ionized impurity scattering have been studied theoretically based on Fermi's Golden Rule as a function of position along the channel for a $Al_{0.5}Ga_{0.5}$As/GaAs HEMT. For operation in the sub-ohmic regime, it is observed that all three mechanisms exhibit a wide variation in the rates from source to drain due to a varying degree of quantum confinement. Some of the intersubband scattering processes involving a lower and higher subband, which are present at the drain end, are absent at the source end due to the variation of energy eigenvalue differences. A quantitative variation of 10–50% was observed in the scattering rates at room temperature such as 1 to 1 adsorption and emission of polar optical phonons. It is important to take into account such variation in scattering rates in a complete device model.

## 1. Introduction

The high electron mobility transistor (HEMT) has been the subject of numerous experimental and theoretical studies due to its many advantages over conventional FETs such as excellent microwave and millimetre wave characteristics, i.e. high gain at high frequencies and also excellent low noise characteristics. Thus, it finds numerous applications in oscillators and RF amplifiers operating from very low frequency to several hundred GHz.

The theoretical modelling of HEMTs falls into three categories: charge control models [1–4], Monte Carlo approach [5–9] and self-consistent numerical solution to BTE-Poisson equations [10–12]. Some of these approaches require the knowledge of transport properties such as mobilities, diffusion coefficients, dissipation factor and collision, momentum relaxation and energy relaxation times. Many of these parameters are usually obtained from a combination of scattering rate calculations including all the dominant scattering processes and a Monte Carlo procedure. In the past, theoretical models inherently neglected the variation of the transport properties along the channel due to variation in quantum confinement [10–12]. However, there are studies reported in the literature [13–17] which unambiguously indicate that the scattering rate for polar optical phonons (POP) depends on the effective well width. But the theoretical works presented in references [13–17] assume an infinite rectangular potential well for their analysis. In a realistic device, the conduction band edge profile is neither infinite nor rectangular, but it is a complicated profile dependent on the geometrical and material parameters and bias voltages of the device. The purpose of this work is to analyse the variation of transport properties using realistic conduction band edge profiles at various channel locations for the sub-ohmic regime of operation.

Many research reports on the importance of interface phonons in quantum wells, wires and dots [18–24] have appeared recently. Knipp *et al* [18] observed that the interface phonons are dominant over the unmodified bulk phonons for quantum dots and wires with dimensions less than 500 Å. They also suggest that the interface phonons are not as important as deformation potential in 2D quantum wells [18]. Even though a proper study of carrier transport should include the presence and influence of interface phonons, a macroscopic treatment of phonon scattering does provide reasonable rough estimates of the phonon scattering [19,20].

![](./images/811847380193247232_1.jpg)

Figure 1. A schematic picture of the HEMT device structure.

Table 1. Material parameters for the device structure
shown in figure 1.

<table>
  <thead>
    <tr>
      <th>Material</th>
      <th>Dopant density (cm⁻³)</th>
      <th>Thickness (nm)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>GaAs</td>
      <td>$N_D = 0.0$; $N_A = 1 \times 10^{15}$</td>
      <td>1000</td>
    </tr>
    <tr>
      <td>Al₀.₅Ga₀.₅As</td>
      <td>$N_D = 0.0$; $N_A = 1 \times 10^{14}$</td>
      <td>10</td>
    </tr>
    <tr>
      <td>Al₀.₅Ga₀.₅As</td>
      <td>$N_D = 5.0 \times 10^{17}$; $N_A = 1 \times 10^{14}$</td>
      <td>40</td>
    </tr>
  </tbody>
</table>

In this work, the scattering rates for bulk POP, acoustic phonons via deformation potential (AP) and ionized impurity scattering (II) have been studied as a function of position along the channel for a Al₀.₅Ga₀.₅As/GaAs HEMT for the sub-ohmic regime of operation. The effect of interface phonons is neglected in a quantum well, since their role is not clear in a broad quantum well such as that in a HEMT based on results of references [18–24]. This issue is addressed in section 3.4.

In section 2, the procedure employed to obtain the one-dimensional conduction band profiles at different points along the channel from the source to the drain using a Poisson solver [25] is discussed. The energy eigenvalues and their respective wavefunctions are obtained for each conduction band profile by solving the time-independent Schrödinger equation using the Numerov method [26]. In section 3, the two-dimensional scattering rates for POP, AP (via deformation potential) and II are obtained based on Fermi's Golden Rule. Results on their variation along the channel from the source to the drain for the sub-ohmic regime of operation are presented and discussed. Conclusions are presented in section 4.

## 2. Quantum confinement along the channel

The material parameters for the HEMT device structure are presented in table 1. A schematic picture of the device is shown in figure 1. The drain to source voltage, $V_{DS}$, and the gate to source voltage, $V_{GS}$, are assumed to be 0.6 V and 0.6 V (the gate is at a higher potential than the source), respectively. These voltages are carefully chosen such that the HEMT under study operates in the sub-ohmic regime. As in a field effect transistor, the potential difference between the gate and various points along the channel varies from $V_{GS}$ at the source to $(V_{GS} - V_{DS})$ at the drain. Thus, the gate to channel voltage $V_{GC}$ can vary in the range from 0.6 V at the source to 0.0 V at the drain.

![](./images/811847380193247232_2.jpg)

Figure 2. 1D $E_C$ profiles for various channel positions corresponding to various values of $V_{GC}$.

Since the device is chosen to operate in the sub-ohmic regime, the gradual channel approximation can be invoked. Thus, the two-dimensional potential function can be decoupled into two one-dimensional functions, one from the source to drain and the other from the gate to substrate. The potential variation from gate to substrate is expected to vary along the channel as the $V_{GC}$ varies in the range 0.0 to 0.6 V. A one-dimensional Poisson solver (FISH1D 2.2) [25] was employed to obtain the one-dimensional gate to channel conduction band edge profile for three locations along the channel each corresponding to a value of $V_{GC}$ between 0.0 V and 0.6 V. Note that since $V_{GC} = 0.0$ V and 0.6 V occur at the drain and the source then $V_{GC} = 0.3$ V will occur somewhere in between. For the purpose of this study, the exact location of this point is unnecessary. The conduction band edge profiles are shown in figure 2. The well width and depth are observed to be dependent on the channel location with a deeper and narrower well at the source end and a shallower and broader well at the drain end. This is indicative of a two-dimensional electron

Transport properties in a high electron mobility transistor

**Table 2.** Material constants for the scattering calculations.

| Material constant               | Symbol | Value                  |
|---------------------------------|--------|------------------------|
| Effective mass                  | $m^*$  | 0.065 $m_0$ $\dagger$  |
| Optical dielectric constant     | $\epsilon_\infty$ | 10.92 $\epsilon_0$ $\ddagger$ |
| Static dielectric constant      | $\epsilon_s$ | 12.90 $\epsilon_0$ $\ddagger$ |
| Polar optical phonon energy     | $\hbar\omega_0$ | 0.0354 eV              |
| Velocity of sound in GaAs       | $S_l$  | $5.24 \times 10^5$ cm s$^{-1}$ |
| Deformation potential of GaAs   | $D$    | 13.5 eV                |
| Density of GaAs                 | $\rho$ | 5.36 g cm$^{-3}$       |

$\dagger$ $m_0$ is the electron rest mass.
$\ddagger$ $\epsilon_0$ is the dielectric constant of vacuum.

gas at the source which becomes less confined along the channel towards the drain. This effect will be much more pronounced for a device under saturation conditions.

The conduction band edge profiles were used in the time-independent Schrödinger equation and the energy eigenvalues and the corresponding wavefunctions were obtained using the Numerov method [26]. In this study, the energy eigenvalues and wavefunctions were obtained for the first five subbands for the three channel locations. The subband energies and wavefunctions were observed to vary from the source end to the drain end due to varying quantum confinement. The energy eigenvalue difference between the $m$th and $n$th subbands, which is an important parameter in deciding the allowed absorption mechanisms for the POP scattering, shows considerable variation from source to drain with lower values at the drain. It was also noted that the wavefunction at the source end was sharper and narrower than at the drain end, indicative of more quantum confinement at the source end.

## 3. Results and discussion

### 3.1. Polar optical phonon scattering

POP scattering is one of the dominant scattering mechanisms in GaAs at room temperature (300 K). It can influence the room temperature transport properties and hence the performance of GaAs/AlGaAs HEMTs. If $\boldsymbol{k}_1$ and $\boldsymbol{k}_2$ are the initial and final wavevectors for the electron, the two-dimensional scattering rate for the POP mechanism can be obtained using Fermi's Golden Rule [5-7]. If $\boldsymbol{Q} = \pm(\boldsymbol{k}_1 - \boldsymbol{k}_2)$ and $\boldsymbol{q}$ are the phonon wavevector components, parallel and perpendicular to the layer interfaces, respectively, then the scattering rate is given by Fermi's Golden Rule as [5]

$$
\begin{aligned}
S_{mn}^{pop}(\boldsymbol{k}_1) &= \frac{e^2 \omega_0}{8 \pi \epsilon_0} \left( \frac{1}{\epsilon_\infty} - \frac{1}{\epsilon_s} \right) \left( N_q + \frac{1}{2} \pm \frac{1}{2} \right) \\
& \quad \times \int \frac{H_{mn}(Q)}{Q} \delta(E(\boldsymbol{k}_2) - E(\boldsymbol{k}_1) \pm \hbar \omega_0) \mathrm{d}\boldsymbol{k}_2
\end{aligned} \tag{1}
$$

with

$$
N_q = \left[ \exp \left( \frac{\hbar \omega_0}{k_B T} \right) - 1 \right]^{-1} \tag{2}
$$

where $\epsilon_\infty$ and $\epsilon_s$ are the optical and static dielectric constants, respectively, $N_q$ is the number of phonons, $\hbar \omega_0$ is the polar optical phonon energy and $T$ is the temperature in K. $H_{mn}(Q)$ is the multi-subband coupling coefficient and is given by

$$
H_{mn}(Q) = \iint \mathrm{d} z_1 \mathrm{d} z_2 \, F_{mn}(z_1) F_{mn}(z_2) \exp(-Q|z_1 - z_2|) \tag{3}
$$

with $Q = |\boldsymbol{Q}|$. In equation (3) $F_{mn}(z) = F_m(z) F_n(z)$, where $F_m(z)$ is the wave function of the $m$th subband.

![](./images/811847380193247232_3.jpg)

**Figure 3.** POP scattering rates as a function of energy for the 1 to 1 absorption mechanism.

The physical and material constants employed for the device are listed in table 2. Using equations (1)-(3), the POP scattering rates are obtained as a function of the incident energy of the electron for various possible intra- and intersubband scattering mechanisms for the three channel locations. Even though we obtained the scattering rates for all possible mechanisms within the first five subbands, we chose to show only a representative sample of them due to space limitation. In general, the variation of scattering rates with incident energy follows the trend reported in references [5, 6].

For the three channel locations, the scattering rate versus incident energy for 1 to 1 absorption and emission mechanisms are shown in figures 3 and 4, respectively. The rates at the source end are larger than those at the drain end by a maximum of 13% and 51% for adsorption and emission, respectively. The scattering rates for 1 to

![](./images/811847380193247232_4.jpg)

Figure 4. POP scattering rates as a function of energy for the 1 to 1 emission mechanism.

![](./images/811847380193247232_5.jpg)

Figure 5. POP scattering rates as a function of energy for the 1 to 2 absorption mechanism.

![](./images/811847380193247232_6.jpg)

Figure 6. POP scattering rates as a function of energy for the 1 to 2 emission mechanism.

![](./images/811847380193247232_7.jpg)

Figure 7. AP scattering rates as a function of energy for the 1 to 1 absorption mechanism.

2 absorption and emission are shown in figures 5 and 6, respectively, for the three channel locations. The rates at the source end are larger than those at the drain end by a maximum of 21% for both adsorption and emission. The scattering rate variations shown in figures 3–6 are attributed to an increase of the effective well width from source to drain which agrees with references [13–17].

Analysing the various possible scattering mechanisms among the five subbands, the highest values of maximum % difference in scattering rates between the source and the drain were found to be 107% (for 4 to 4 absorption) and 114% (for 5 to 2 emission). Due to the difference in the energy eigenvalue, $\Delta E_{31}=E_{3}-E_{1}$, exceeding the optical phonon energy, $\hbar \omega_{0}$, for the channel locations other than the drain end, the 1 to 3 absorption mechanism was not observed. It is noted that even though the 1 to 3 absorption mechanism exhibits a wide variation in scattering rate along the channel, because it is an order of magnitude smaller than the 1 to 1 mechanism, these mechanisms may not significantly influence the variation of transport properties along the channel.

### 3.2. Acoustic phonon scattering mechanism

The intrasubband scattering rate for AP (via deformation potential) for the $m$th subband for an electron with initial wave vector, $\boldsymbol{k}_{1}$, is given by [5]

$$
\begin{aligned}
S_{m m}^{a c p}\left(\boldsymbol{k}_{1}\right) & =\frac{D^{2}}{4 \pi \rho S_{l}} \int F_{m}^{4}(z) \mathrm{d} z \int \mathrm{d}^{2} Q Q \frac{N(Q)+\frac{1}{2} \pm \frac{1}{2}}{\epsilon^{2}(Q)} \\
& \times \delta\left(E\left(\boldsymbol{k}_{1}\right)-E\left(\boldsymbol{k}_{2}\right) \pm \hbar S_{l} Q\right)
\end{aligned} \tag{4}
$$

where $D$ is the deformation potential, $\boldsymbol{k}_{2}$ is the wave vector of the final state, $\rho$ is the density of the GaAs, $S_{l}$ is the longitudinal sound velocity in GaAs and $\epsilon(Q)$ is the screening function as defined in reference [5]. The

![](./images/811847380193247232_8.jpg)

Figure 8. AP scattering rates as a function of energy for the 1 to 1 emission mechanism.

material constants are listed in table 2 and the temperature is assumed to be 300 K.

Plots of scattering rate versus incident energy for 1 to 1 absorption and emission are shown in figures 7 and 8, respectively, for the three channel locations. These scattering rates are two orders of magnitude smaller than those of the corresponding POP scattering mechanisms. The variation of rate with the incident energy follows the behaviour described in reference [5]. As illustrated in figures 7 and 8, the rates at the drain end are 24% smaller than those at the source end for the both mechanisms. The highest maximum % difference between the source and the drain of 109% was observed for the 4 to 4 absorption mechanism. Even though the rates in this case also show a wide variation along the channel, due to their very low rates they may not influence the transport properties significantly.

### 3.3. Ionized impurity scattering mechanism

Yokoyama and Hess [5] have devised the following method of finding the scattering rate due to impurities using the approach of Stern et al [27]. If $\Phi(r,z)$ is the scattering potential due to impurities then
$$
\begin{aligned}
& \nabla^{2} \Phi(r, z)-2 \sum_{i} S_{i} g_{i}(z) \int \Phi(r, z) g_{i}\left(z_{1}\right) \mathrm{d} z_{1} \\
& \quad=\frac{-e}{\epsilon_{0} \epsilon_{S}} \delta(r) \delta\left(z-z_{0}\right)
\end{aligned}
$$
where $S_{i}=(e^{2}/2\epsilon_{0}\epsilon_{S})(N_{i}/E_{di})$, with
$$
\begin{aligned}
E_{d i}= & k_{B} T\left[1+\exp \left(-\frac{E_{F}-E_{i}}{k_{B} T}\right)\right] \\
& \times \ln \left[1+\exp \left(\frac{E_{F}-E_{i}}{k_{B} T}\right)\right].
\end{aligned}
$$

In equation (6) $S_{i}$ is the screening constant, $g_{i}(z)$ is the electron density function given by $F_{i}^{2}(z)$. $E_{d i}$ is the diffusion energy, $E_{F}$ is the Fermi level and $E_{i}$ is the energy level for the $i$th subband. $N_{i}$ is the 2D carrier density given by the expression
$$
N_{i}=\frac{m^{*} k_{B} T}{\pi \hbar^{2}} \ln \left[1+\exp \left(\frac{E_{F}-E_{i}}{k_{B} T}\right)\right].\qquad(7)
$$

In equation (5), the term $2 \sum_{i} S_{i} g_{i}(z) \int \Phi(r,z)g_{i}(z_{1})\mathrm{d}z_{1}$ represents the charges that are induced because of the presence of impurity atoms. The term on the right hand side of equation (5) describes the charge density due to ionized impurities. Screening of the impurity potential through the presence of the 2DEG is taken into account with the second term on the left hand side which involves $S_{i}$ and $g_{i}(z)$.

By solving equation (5) for $\Phi$, one can find the matrix element and the scattering rate due to impurity scattering. It can be shown that the scattering rate due to impurity scattering is given by the expression
$$
S_{m n}^{I M P}\left(\overline{\boldsymbol{k}}_{0}\right)=\frac{1}{2 \pi \hbar} \int\left|M_{m n}(Q)\right|^{2} \delta\left(E\left(\overline{\boldsymbol{k}_{0}^{\prime}}\right)-E\left(\overline{\boldsymbol{k}}_{0}\right)\right) \mathrm{d} \overline{\boldsymbol{k}}_{0}^{\prime}\ (8)
$$
where
$$
\left|M_{m n}(Q)\right|^{2}=\int M_{m n}^{2}\left(z_{0}\right) N_{I}\left(z_{0}\right) \mathrm{d} z_{0}\qquad(9)
$$
with
$$
M_{m n}\left(z_{0}\right)=\int e \Phi(Q,z)F_{m}(z)F_{n}(z)\mathrm{d}z.\qquad(10)
$$

In equations (8)-(10), $Q=2k_{0}\cos\theta$, where $k_{0}$ is the absolute value of $\overline{k}_{0}$ and $\theta$ is the angle between $Q$ (with $Q=\pm(\overline{k}_{0}-\overline{k_{0}^{\prime}})$) and $\overline{k}_{0}$ with $\overline{k}_{0}$ and $\overline{k_{0}^{\prime}}$ as the initial and final wavevectors of the electron, respectively. $N_{I}(z_{0})$ is the impurity concentration at $z=z_{0}$.

Plots of scattering rate versus incident energy for 1 to 1 and 2 to 2 are shown in figures 9 and 10, respectively. The maximum % difference between the source and drain is found to be 66% and 98%, for 1 to 1 and 2 to 2 mechanisms, respectively. The highest value of the maximum % difference was found to be for 5 to 5 and it is equal to 133%. Since the ionized impurity scattering rates are much smaller than the dominant POP, the wide variation observed in the rates even for 1 to 1 mechanisms will have minimal influence on the transport properties at room temperature.

### 3.4. Influence of quantum confinement on transport

As discussed in sections 3.1-3.3, the scattering rates exhibit a wide variation along the channel for all three mechanisms at 300 K. For higher temperature operations, the variation can be much more pronounced. The scattering rates not only exhibit a wide variation from source to drain (as much as 133%), but also some mechanisms which are present at the drain are found to be absent at other channel locations, especially at the source due to variation in the difference in the energy eigenvalue between subbands, $\Delta E_{ij}=E_{i}-E_{j}$, exceeding the phonon energies. The lower POP and AP rates at the drain end than at the source end are attributed to the broader and shallower well (less 2D confinement) at the drain end. This observation agrees well with results reported in literature [13-17].

![](./images/811847380193247232_9.jpg)

Figure 9. II scattering rates as a function of energy for the
1 to 1 mechanism.

![](./images/811847380193247232_10.jpg)

Figure 10. II scattering rates as a function of energy for
the 2 to 2 mechanism.

The scattering rates coupled with the carrier distribution
in energy in various subbands determine the macroscopic
transport properties such as the mobilities, the diffusion
coefficients, the relaxation times and the energy dissipation
parameters. At and below room temperature, the carriers
are expected to occupy the first two subbands. Under this
condition, a variation in the scattering rates of POP along
the channel is observed for the carriers in the first subband.
Such a variation in the scattering rates of carriers in the
densely populated first subband can result in a variation
in transport properties such as the mobility and diffusion
coefficient between the source and the drain, with the drain
exhibiting higher mobility if no other mechanism dominates
the transport.

At higher temperatures, higher subbands will be
populated and the variation in scattering rate and hence
the mobility and the diffusion coefficient will show much
more variation from the source to the drain. Thus, the
transport properties are clearly functions not only of the
electric field, but also of the quantum confinement which
can vary widely within a device from the source to the drain
under different bias conditions. We estimate that assuming
the transport parameters to be independent of the quantum
confinement can lead to an error in the computation of the
current which, in turn, can result in a similar error in the
design of an electronic circuit.

A discussion of the influence of interface phonons
in HEMTs is in order here. The results of references
[18–24] assume at least two heterointerfaces with two
potential barriers and a well, whereas the HEMT structure
we studied has only one GaAs/AlGaAs interface. The
effect of this difference in the number of interfaces is
not obvious. Additionally, Knipp *et al* [18] suggested
that the influence of the interface phonon is important in
quantum dots and wires. Also, the work of Lugli *et al* [19,
20] indicates that the macroscopic descriptions provide a
reasonable rough estimate of scattering rates. This is not
to say that the interface phonons are unimportant. Finally,
it is noted that the purpose of this work is only to bring
out the importance of quantum confinement on scattering
rates along the channel, but not to make any quantitative
conclusions on the variation of transport properties. A
proper quantitative study should include the influence of
the interface phonons.

All our analysis is performed in the sub-ohmic regime
of operation due to the need to invoke the gradual channel
approximation. Thus, our results are invalid in the
saturation regime even though qualitative aspects of the
results will stay the same. To obtain quantitative results,
one needs to run these simulations with a 2D Poisson
solver coupled with calculation the Schrödinger equation
and scattering rate and Boltzmann transport equation self-
consistently, which will be computationally expensive.
Additionally, our work should be extended to relate the
scattering rates to transport properties using density of states
and Fermi-Dirac statistics to study the actual variation of
the transport properties with the channel location for a
realistic device.

### 4. Conclusion

In this study, the scattering rates for bulk polar optical
phonons, acoustic phonons via deformation potential and
ionized impurity scattering have been studied theoretically
as a function of the incident energy of the electron and
the position along the channel for a $Al_{0.5}Ga_{0.5}As/GaAs$
HEMT operating in the sub-ohmic regime where the
gradual channel approximation is valid. All three scattering
mechanisms exhibit a wide variation in scattering rates for
various subband scatterings from source to drain due to
varying degree of quantum confinement. Some mechanisms
which are absent at the source are present at the drain due to
the variation in energy eigenvalue separations compared to
the phonon energies. The variation in transport properties
arising from the variation of quantum confinement should
be taken into account for a complete device modelling of
HEMTs.

Transport properties in a high electron mobility transistor

### Acknowledgment
The authors gratefully acknowledge the constructive criticisms of the referee.

### References
[1] Lee K, Shur M, Drummond T J and Morkoç H 1983
J. Appl. Phys. **54** 6432

[2] Shey A-J and Ku W H 1988 *IEEE Electron Devices Lett.* **9**

[3] Martin E A, Iliadis A A and Aina O A 1993 *IEEE Trans.*
Electron Devices **40** 466

[4] Delagebeaudeauf D and Link N T 1982 *IEEE Trans.*
Electron Devices **29** 955

[5] Yokoyama K and Hess K 1986 *Phys. Rev.* B **33** 5595

[6] Artaki M and Hess K 1988 *Phys. Rev.* B **37** 2933

[7] Park D H and Brennan K F 1990 *IEEE Trans. Electron*
Devices **37** 618

[8] Tomizawa K and Hashizume N 1988 *IEEE Trans. Electron*
Devices **35** 849

[9] Kim Ki Wook, Tian Hong and Littlejohn M A 1991 *IEEE*
Trans. Electron Devices **38** 1737

[10] Widiger D, Hess K and Coleman J J 1984 *IEEE Electron*
Devices Lett. **5** 266

[11] Widiger D, Kizilyalli I C, Hess K and Coleman J J 1985
*IEEE Trans. Electron Devices* **32** 1092

[12] Ng Sze-Him, Khoie R and Venkat R 1991 *IEEE Trans.*
Electron Devices **38** 852

[13] Price P J 1981 *Ann. Phys.* **133** 617

[14] Chiu L C, Margalit S and Yariv A 1983 *Japan. J. Appl.*
Phys. **22** L82

[15] Hess K 1979 *Appl. Phys. Lett.* **35** 484

[16] Leburton J P 1984 *J. Appl. Phys.* **56** 2850

[17] Ferry D K 1978 *Surf. Sci.* **75** 85

[18] Knipp P A and Reinecke T L 1995 *Phys. Rev.* B **52** 5923

[19] Lugli P, Molinari E and Rucker H 1991 *Superlatt. and*
Microstruct. **10** 471

[20] Rucker H, Molinari E and Lugli P 1991 *Phys. Rev.* B **44**

[21] Rossi F, Bungaro C, Rota L, Lugli P and Molinari E 1994
*Solid-State Electron.* **37** 761

[22] McIntyre C R and Reinecke T L 1994 *Superlatt. and*
Microstruct. **16** 327

[23] Knipp P A and Reinecke T L 1993 *Phys. Rev.* B **48** 5700

[24] Knipp P A and Reinecke T L 1996 *Solid-State Electron.* **40**

[25] *FISH1D User's Manual* 1989 (Indiana: Purdue University)

[26] Chow P C 1972 *Am. J. Phys.* **40** 730

[27] Stern F and Howard W E 1967 *Phys. Rev.* **163** 816

777
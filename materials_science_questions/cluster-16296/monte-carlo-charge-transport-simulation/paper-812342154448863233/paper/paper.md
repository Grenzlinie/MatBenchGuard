![](./images/812342154448863233_1.jpg)

Hot-phonon-induced velocity saturation in GaN

B. K. Ridley, W. J. Schaff, and L. F. Eastman

Citation: *Journal of Applied Physics* **96**, 1499 (2004); doi: 10.1063/1.1762999
View online: http://dx.doi.org/10.1063/1.1762999
View Table of Contents: http://scitation.aip.org/content/aip/journal/jap/96/3?ver=pdfcov
Published by the AIP Publishing

Articles you may be interested in
Hot phonon-plasmon modes in GaN
J. Appl. Phys. **108**, 104504 (2010); 10.1063/1.3500329

Hot phonons in Si-doped GaN
Appl. Phys. Lett. **89**, 202117 (2006); 10.1063/1.2388866

Optical study of hot electron transport in GaN: Signatures of the hot-phonon effect
Appl. Phys. Lett. **88**, 022103 (2006); 10.1063/1.2163709

Theory of the GaN crystal diode: Negative mass negative differential resistance
J. Appl. Phys. **97**, 094503 (2005); 10.1063/1.1889235

Hot-phonon bottleneck in the photoinjected plasma in GaN
Appl. Phys. Lett. **82**, 2455 (2003); 10.1063/1.1566467

![](./images/812342154448863233_2.jpg)

# Hot-phonon-induced velocity saturation in GaN

B. K. Ridley, $^{a)}$ W. J. Schaff, and L. F. Eastman
Department of Electrical and Computer Engineering, Cornell University, Ithaca, New York 14853

(Received 9 March 2004; accepted 23 April 2004)

In highly polar semiconductors with electron densities typically found in heterostructure field-effect transistors (HFETs), transport cannot be described without taking hot phonons into account. Here we describe a simple analytical model applied to the case of bulk GaN, taking the nonparabolicity of the conduction band into account, and show that the production of longitudinal optical (LO) phonons reduces the mobility and causes the drift velocity to saturate at a value around $10^{7}$ cm/s, depending on the density of electrons. Transfer of electrons to higher valleys is expected to be delayed to much higher fields than commonly predicted. The effect of possible hot products of the LO decay is also considered. We relate the results for bulk material to the situation in HFETs, in which real-space transfer is inhibited, by considering the effect of spatial spreading of the channel electrons. © 2004 American Institute of Physics. [DOI: 10.1063/1.1762999]

## I. INTRODUCTION

The drift velocity of electrons in a GaN heterostructure field-effect transistor (HFET) is significantly lower than expected from Monte Carlo simulations of hot-electron transport. $^{1,2}$ These Monte Carlo calculations employ sophisticated GaN band-structure models and predict maximum velocities between $2×10^{7}$ and $3×10^{7}$ cm/s. $^{3,4}$ Some take into account the structure of a real HFET and the effects of real-space transfer to AlGaN barriers [e.g., Ref. 3], but still predicts a high velocity. Predictions in bulk material tend to be confirmed in experiment using optical excitation, but observed velocities in real devices rarely exceed $1×10^{7}$ cm/s. The obvious difference between theory and experiments involving optical excitation on the one hand, and device characteristics on the other, is in the electron densities—implicitly small in theoretical simulations, typically small in optical experiments, but very large in devices. The large densities in devices suggest that the inevitable, copious production of optical phonons at high fields is responsible for the observed velocity saturation. The effects of hot phonons on the energy-relaxation rate have been observed in a number of experiments. $^{5-7}$ It would be useful to have an analytical model of velocity saturation in order to understand and manipulate the transport properties of devices without massive computation, and it is the purpose of this report to describe such a model.

## II. THEORY

A full treatment of transport involving hot electrons and hot phonons in a HFET channel would involve the consideration of nonparabolicity, sub-band scattering, spatial spreading, real-space transfer, and the separate description of half-space bulk phonon modes, interface modes and half-space barrier modes plus their hybridization at the interface. The situation in bulk material is much simpler to deal with and sufficient for our purpose. Here, we present a simple theoretical model of hot-electron transport in bulk material that confirms that hot phonons can indeed cause the velocity to saturate.

In fact, a treatment of hot-electron transport in a quasi-two-dimensional (2D) channel using a bulk model is not as outrageous as at first sight it may seem. In a quasi-2D channel at a single heterostructure, electrons are scattered, at room temperature, principally by polar-optical phonons, impurities, and other imperfections. The phonons are of two types: half-space bulk modes and interface modes. It has been shown that, to a good approximation, the sum effect of these two types is equal to the scattering rate obtained by assuming a bulklike phonon spectrum. $^{8}$ So using a bulk phonon spectrum is justified to some extent. At high electron temperatures (and the high electron densities allow us reasonably to assume that an electron temperature exists) scattering will involve many sub-bands, which will make the scattering bulklike. In many devices the barrier is high enough for us to neglect effects of real-space transfer. We can assume, therefore, that any spatial spreading is principally into the bulk GaN buffer. Apart from this spatial spreading, which dilutes the electron gas and therefore the hot-phonon effect, the adoption of a bulk model for our purposes is therefore a reasonable practical choice. A consideration of the effect of spatial spreading will be made later in this paper.

Another advantage of dealing with hot electrons is that at high electron temperatures the effects of degeneracy can be assumed to be small, which allows us to use a Maxwell-Boltzmann distribution characterized by an electron temperature to describe the occupancy of states. The nonparabolicity of the conduction band is taken into account by assuming a $\mathbf{k\cdot p}$-like form
$$
\frac{\hbar^{2}k^{2}}{2m^{*}}=E(1+E/E_{g})=\gamma(E), \tag{1}
$$
where $k$ is the electron wave vector, $m^{*}$ is the band-edge effective mass, $E$ is the energy, and $E_{g}$ is the band gap.

$^{a)}$Present address: Department of Electronic Engineering Science, University of Essex, Colchester CO4 3SQ, United Kingdom.

Comparison with the results of the band-structure calculated by the empirical pseudopotential model⁴ shows that this works reasonably well up to 0.8–1.0 eV.

The first part of the calculation is to estimate the power dissipated per electron by emitting longitudinal-optical (LO) polar phonons. The occupation of a phonon state with wave vector $q$ is determined by the mode rate equation

$$
\frac{dn(q)}{dt}=G(q)-\frac{n(q)-n(T_L)}{\tau_p}. \tag{2}
$$

Here, $n(q)$ is the phonon number, $G(q)$ is the total rate of emission of phonons with wave vector $q$, $n(T_L)$ is the thermodynamic-equilibrium number at the lattice temperature and $\tau_p$ is the phonon lifetime. The net emission rate is

$$
G(q)=W_{em}(q)[n(q)+1]-W_{abs}n(q). \tag{3}
$$

Following Artaki and Price⁹ we relate the rates in Eq. (3) using the principle of detailed balance:

$$
W_{abs}=W_{em}\frac{n(T_e)+1}{n(T_e)}. \tag{4}
$$

Where $n(T_e)$ is the phonon number at the electron temperature (independent of $q$ since we assume that all LO modes have the same frequency). The phonon number is then

$$
n(q)=n(T_e)\frac{n(T_L)+\lambda(q)}{n(T_e)+\lambda(q)} \tag{5}
$$

and the power dissipated per electron is

$$
P=\frac{\hbar\omega}{\tau_p}\frac{n(T_e)-n(T_L)}{N}\int\frac{\lambda(q)}{n(T_e)+\lambda(q)}d^3\mathbf{q}, \tag{6}
$$

where $\hbar\omega$ is the phonon energy and $N$ is the number of electrons. The hot-phonon factor is

$$
\lambda(q)=W_{em}\tau_p, \tag{7}
$$

where $W_{em}$ is the total spontaneous emission rate, obtained by summing over the electron distribution

$$
\begin{aligned}
W_{em}=&\frac{1}{2}W_0\left(\frac{\hbar\omega}{E_q^3}\right)^{1/2}\int_{E_1}^{\infty}\exp\{(E_F-E)/k_BT_e\} \\
&\times\left(\frac{d\gamma}{dE}\right)'\left(\frac{d\gamma}{dE}\right)dE,
\end{aligned} \tag{8}
$$

where

$$
\begin{gathered}
W_0=\frac{e^2}{4\pi\hbar}\left(\frac{2m^*\omega}{\hbar}\right)^{1/2}\left(\frac{1}{\epsilon_\infty}-\frac{1}{\epsilon_s}\right) \\
E_q=\frac{\hbar^2q^2}{2m^*} \quad \text{and} \quad E_1=\frac{(\gamma-\gamma'+E_q)^2}{4E_q}.
\end{gathered} \tag{9}
$$

Nonparabolicity is taken into account via $\hbar^2k^2/2m^*=\gamma(E)$ [see Eq. (1)]. The prime indicates the state after emission. $E_F$ is the Fermi energy and $\epsilon_\infty$, $\epsilon_s$ are the high frequency and static permittivities, respectively (Fig. 1).

In order to calculate the power dissipation we assume the following values for GaN: $\hbar\omega$=0.091 eV, $\tau_p$=3 ps (Ref. 10) (this room-temperature value is consistent with 5 ps measured at 25 K (Ref. 10), $m^*$=0.21$m_0$, $\epsilon_s$=9.7$\epsilon_0$, $\epsilon_\infty$=5.28$\epsilon_0$, $T_L$=300 K. The result is shown in Fig. 1.

![](./images/812342154448863233_3.jpg)

FIG. 1. Power dissipated per electron.

When the hot-phonon factor [Eq. (7)] is large (high density, strong polar interaction, long phonon lifetime), the phonon number becomes close to being determined by the electron temperature [$n(q)$=$n(T_e)$]. Assuming that this is the case simplifies the calculation of the hot-electron mobility, which is the next task. An expression for the momentum-relaxation rate associated with polar-optical-phonon (POP) scattering in a nonparabolic band has been given by Conwell and Vassel¹¹ and we use this to obtain the momentum-relaxation time averaged in the usual way over the electron distribution and subsequently the POP mobility as a function of electron temperature. The contribution from other scattering mechanisms is embodied, for simplicity, in terms of a temperature independent mobility chosen to give the low-field mobility as 1200 cm²/Vs.

The electric field, $F$, as a function of temperature is obtained from

$$
e\mu F^2=P \tag{10}
$$

and the drift velocity $v$ from $v$=$\mu F$. Figure 2 shows the velocity field curves for various densities between 0.5 ×10¹⁸ and 5×10¹⁸ cm⁻³. This range of densities was chosen to be high enough to correspond roughly with modest densities in FETs without compromising the assumption of nondegeneracy at high fields. Without hot-phonon effects the velocity would be well above 2×10⁷ cm/s at fields beyond 50 kV/cm. Hot-phonon velocity saturation appears to be unavoidable at high densities.

We have limited our calculations to electron temperatures no higher than 5000 K, corresponding to an average energy of 0.65 eV, well within the limit of our nonparabolicity approximation and well below energies at which intervalley processes can occur [the lowest energy predicted for the $U$ valley is 1.34 eV (Ref. 12)]. Hot-phonon effects will therefore tend to shift the field at which intervalley transfer occurs to much higher fields than predicted by Monte Carlo predictions.

### III. DISCUSSION
The velocity saturation here predicted was obtained assuming that all phonons, whatever their wave vector, were forced to be in thermal equilibrium with the electron gas. This will be a reasonable approximation only for the most

![](./images/812342154448863233_4.jpg)

FIG. 2. Density dependence. (a) Velocity-field curves, (b) velocity at 250 kV/cm.

strongly interactive modes; the polar interaction is strongest for small $q$ and so the production rate for large $q$ modes will be too small for equilibrium to be established. Our estimate of hot-phonon effects is bound to be an overassessment. Fig- ure 3(a) shows the typical spectrum of emission. Some quan- tifiable indication of error can be obtained by calculating actual phonon numbers for the most strongly coupled modes, i.e., those modes with wave vectors such that $E_{q} \leqslant \hbar \omega$ (see Eq. (9) for the definition of $E_{q}$ ). Equation (5) has been used to provide the results for the ratio $n(q) / n(T_{e})$ in Fig. 3(b) for a particular density and the density dependence for $u$ $=E_{q} / \hbar \omega=0.5$ and 1 is shown in Fig. 3(c). The validity of our assumption of unity for this ratio weakens towards low densities (not surprisingly) and towards high electron tem- peratures, this because of the increasing number of modes that satisfy energy and momentum conservation. Any error in the ratio is nevertheless diluted in its rôle in determining the momentum-relaxation rate since the emphasis is always on spontaneous emission rather than stimulated emission or ab- sorption. We conclude that the error generated by our as- sumption of equal temperatures for electrons and phonons will not seriously invalidate our main findings.

Another assumption made is the constancy of the pho- non lifetime. The anharmonic process, responsible for pho- non decay, suggests a decay producing a short-wave transverse-optical (TO) mode plus a short-wave longitudinal- acoustic (LA) mode viz: LO$\rightarrow$TO+LA. $^{13}$ [Depending on LO dispersion there may be also a channel involving a short- wave LO mode as for GaAs (Ref. 14).] The question arises: How fast do these daughter modes decay? Our assumption of constant LO lifetime assumes that short-wave TO and LA modes decay much faster than LO modes so that the phonon occupancy of these modes remain determined by the lattice temperature. If, on the other hand, these modes become hot, they will stimulate the decay of the LO mode: the LO life- time will then decrease with electron temperature and the hot-phonon, effect, though remaining, will weaken. We are not aware that the decay of short-wavelength phonon modes has been measured, but the high frequencies involved and the possibility of umklapp processes suggests the availability of a high density of states for decay products will, in conse- quence, produce a lifetime significantly shorter than the LO lifetime. If this is so, our assumption of a constant, temperature-independent lifetime will be valid. Experiments based on noise measurements support this assumption, $^{7}$ but these experiments, which are on HFETs, suggest phonon life- times much less than 3 ps, though a mechanism for this is unknown.

![](./images/812342154448863233_5.jpg)

FIG. 3. Elements of phonon production. (a) Emission rate for a density of $3 \times 10^{18} \mathrm{~cm}^{-3}$ at $1000 \mathrm{~K}, 3000 \mathrm{~K}$, and $5000 \mathrm{~K}$ as a function of $u$ $=E_{q} / \hbar \omega\left(E_{q}=\hbar^{2} q^{2} / 2 m^{*}\right)$, (b) associated phonon number ratio; (c) density dependence of the phonon number ratio at $1000 \mathrm{~K}$ and $3000 \mathrm{~K}$ for $u=0.5$ and 1.0.

Returning to the problem of spatial spreading in the HFET case, we approximate the effect in our bulk model by relating the areal density in the channel to a volume density via the Debye length. We assume also that real-space transfer

![](./images/812342154448863233_6.jpg)

FIG. 4. Velocity-field curves taking into account spatial spreading.

is inhibited either by having an AlGaN barrier containing a high percentage of Al or by including a thin "interbarrier" of AlN in the structure. In this case, roughly, the hot channel electrons will be confined within two Debye lengths from the interface. Thus, if $N_{s}$ is the areal density, the corresponding volume density is $N_{v}=N_{s} / 2 L_{D}$ with $L_{D}=\sqrt{\epsilon k_{B} T_{e} /\left(N_{v} e^{2}\right)}$ so $N_{v}=N_{s}^{2} e^{2} /\left(4 \epsilon k_{B} T_{e}\right)$, and the volume density becomes inversely proportional to the electron temperature. The result is shown in Fig. 4, which shows a much weaker approach to saturation than in the bulk. The velocity is, nevertheless, far below the prediction in the absence of hot phonons.

On the basis of this discussion we conclude that the electron velocity in a FET, designed to inhibit real-space transfer, should increase near pinchoff. Predicting the effect of this on the performance of the device is more problematic, given the nonuniform fields associated with the gate and the longer paths between source and drain implied by deconfinement.

In conclusion, we have presented an analytical model of the effects of hot phonons on the high-field transport properties of electrons in bulk GaN that illustrates the phenomenon of velocity saturation. An application of the model to the HFET case suggests a somewhat weaker approach to velocity saturation should occur.

## ACKNOWLEDGMENT

We are grateful for the support of the Office of Naval Research via Grant No. N00014-99-1-0714 sponsored by Dr. Colin Wood.

$^{1}$ L. Ardaravicius, A. Matulionis, J. Liberis, O. Kiprijanovic, M. Ramonas, L. F. Eastman, J. R. Shealy, and A. Vertiatchikh, Appl. Phys. Lett. 83, 4038 (2003).
$^{2}$ M. Ramonas, A. Matulionis, and L. Rota, Semicond. Sci. Technol. 18, 118 (2003).
$^{3}$ T.-H. Yu and K. F. Brennan, J. Appl. Phys. 91, 3730 (2002).
$^{4}$ C. Bulutay, B. K. Ridley, and N. A. Zakhlenuik, Phys. Rev. B 68, 115205 (2003).
$^{5}$ N. Balkan, M. C. Arikan, S. Gokden, V. Tilak, W. J. Schaff, and J. R. Shealy, J. Phys.: Condens. Matter 14, 3457 (2002).
$^{6}$ A. Matulionis, J. Liberis, L. Ardaravicius, M. Ramonas, I. Matulioniene, and J. Smart, Semicond. Sci. Technol. 17, L9 (2002).
$^{7}$ A. Matulionis, J. Liberis, I. Matulioniene, M. Ramonas, L. F. Eastman, J. R. Shealy, V. Tilak, and A. Vertiatchikh, Phys. Rev. B 68, 035338 (2003).
$^{8}$ N. Mori and T. Ando, Phys. Rev. B 40, 6175 (1989).
$^{9}$ M. Artaki and P. J. Price, J. Appl. Phys. 65, 1317 (1989).
$^{10}$ K. T. Tsen, R. P. Joshi, D. K. Ferry, A. Botchkarev, B. Sverdlov, A. Salvador, and H. Morkoç, Appl. Phys. Lett. 72, 2132 (1998).
$^{11}$ E. M. Conwell and M. O. Vassell, Phys. Rev. 166, 797 (1968).
$^{12}$ C. Bulutay, B. K. Ridley, and N. A. Zakhlenuik, Phys. Rev. B 62, 15754 (2000).
$^{13}$ B. K. Ridley, J. Phys.: Condens. Matter 8, L511 (1996).
$^{14}$ F. Vallée and F. Bogani, Phys. Rev. B 43, 12049 (1991).
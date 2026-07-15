![](./images/812570344928837633_1.jpg)

Nuclear Inst. and Methods in Physics Research, A

journal homepage: www.elsevier.com/locate/nima

![](./images/812570344928837633_2.jpg)

# SCENA: A simulation tool for radiation-induced gas scintillation

M. Lamotte *, G. De Izarra, C. Jammes

CEA, DES, IRESNE, DER, Instrumentation Sensors and Dosimetry Laboratory, Cadarache, F-13108 Saint-Paul-lez-Durance, France

![](./images/812570344928837633_3.jpg)

## ARTICLE INFO

**Keywords:**
Fission chambers
Radiation-hard detectors
Gaseous detectors
Gas scintillation

## ABSTRACT

Within the framework of the dependable neutron flux instrumentation development for Sodium-cooled Fast Reactor (SFR) of Generation IV, the French Alternative Energies and Atomic Energy Commission (CEA) is investigating an innovative technology based on optical signals produced within an ionization chamber. In such gaseous detectors, neutrons interact with a fissile material, releasing heavy ions in the MeV-range, eventually leading to spontaneous photon emission in the ultraviolet to infrared range. In this paper, the process of light generation is analyzed through a newly-developed computer code named SCENA. Semi-empirical models for ion-to-gas energy exchange and secondary electron production are assessed. The output of the SCENA subroutines are satisfactory checked against other electron swarm simulation tools, experimental data and a theoretical gas model. SCENA is able to follow the cold-plasma created along a heavy ion slowing-down in space and time evolution. This performance is a key point in the development of optical ionization chambers.

## 1. Introduction

The French Alternative Energies and Atomic Energy Commission (CEA) proposes a new generation of neutron detectors for the neutron flux monitoring of Sodium-cooled Fast Reactors (SFR). These detectors are based on the luminescence of rare gases excited by charged particles [1–3]. The photons emitted in the near-infrared region can be then channeled into an optical fiber in a harsh radiation environment over a long distance. Experiencing a low attenuation in silica fibers [4] the near-infrared light signal finally feeds either a solid-state photon counter or spectrometer. The simulation of such a signal is an important step for the development of an optical fission chamber for SFR. This is the reason why a computer code called SCENA, which stands for Simulation of Collisions Electrons-Neutrals in Atmospheres, has been developed in the Octave interpreted programming language. SCENA is an unique tool, capable of simulating the heavy ion interactions in a mono-atomic gas with or without an electric field, delta electron generation, gas excitation. All these computed physical quantities make it possible to estimate an optical emission spectrum and absolute yield. This paper starts with a presentation of the main functions of the SCENA code, models embedded and their domain of validity. The code validation is then addressed using experimental data and results from other Boltzmann codes.

## 2. Methods

The present section details the physical models implemented in SCENA to simulate the numerous phenomena encountered in the heavy-ion-induced mono-atomic gas ionization. The time sequence of those phenomena depicted in Fig. 1 is as follows:

1.  A heavy ion emitted from a neutron-sensitive coating slows down and ionizes a filling gas, leading to the production of delta electrons.
2.  Those electrons impact the gas atoms, what comes to generate secondary electrons and populate excited levels.
3.  The so-excited gas atoms then undergo a radiative decay, emitting photons at discrete wavelengths in an optically thin medium.

### 2.1. Heavy ion slowing down

In ionization chambers, heavy ions are emitted from a micron-thick neutron-sensitive layer, made of various materials, e.g., $^{235}$U, $^{239}$Pu, $^{10}$B. A heavy ion undergoes a competition between electron gain and loss [5]. As shown by the well-known Bethe–Bloch formula [6], this change in their effective charge directly and continuously impacts their stopping power. This is the reason why the effective charge of a heavy ion is periodically updated in the SCENA code.

One also assumes both the Continuous Slowing Down Approximation (CSDA) and dominance of the electronic stopping. In other words, every heavy ion slows down along a straight track due to the inelastic collisions with bound electrons in the medium, neglecting the nuclear collisions which are not likely to occur at a kinetic energy high enough, above 3 MeV for light fission fragments.

The CSDA validity was confirmed by computing the most probable Light Fission Fragments (LFF) straggling in a rare gas with the more accurate PRAL model [7]: the straggling turns out to be around 4.5% of the range in argon [8]. Finally, since the kinetic energy of heavy ions

* Corresponding author.
E-mail address: maxime.lamotte@cea.fr (M. Lamotte).

https://doi.org/10.1016/j.nima.2020.164576
Received 6 May 2020; Received in revised form 27 July 2020; Accepted 19 August 2020
Available online 2 September 2020
0168-9002/© 2020 Elsevier B.V. All rights reserved.

### Nomenclature

$a_0$
Bohr radius: $a_0 = 5.9\text{E-}11$ m

$A_{ji}$
Einstein coefficient for transition from $j$ to $i$ level

amu
atomic mass unit equal to $1.66\text{E-}27$ kg

$BR_e$
Inner sheath electron breeding ratio

$c$
Speed of light: $c = 2.99\text{E8}$ m/s

$D$
Transverse diffusion coefficient

$\overline{E}$
Mean electron energy in eV

$\overline{E}_\delta$
Mean delta electron energy in eV

$E/N$
Reduced electric field in Td

$E_p$
Projectile kinetic energy in eV

$\epsilon$
Ejected electron kinetic energy in eV

$\eta$
Random number from a uniform distribution between 0 and 1

$f_M$
Maxwell Electron Energy Distribution Function (EEDF)

$h$
Planck's constant: $h = 6.63\text{E-}34$ J s

$I_b$
Electron-binding energy in eV

$I_{ij}$
Intensity of transition between $j$ to $i$ atomic levels

$k_i$
Collision frequency for collision type $i$

$K_i$
Collision rate for collision type $i$

$m_e$
Mass of an electron: $m_e = 9.11\text{E-}31$ kg

$m_p$
Mass of the projectile in kg

$N$
Atomic density in m$^{-3}$

$n_\delta$
Average number of delta electrons

$n_e$
Inner sheath electron density

$N_j$
Density of atomic level $j$

$N_e$
Electron density

$v_{ij}$
Wavelength of photon emission from level $j$ to $i$ transition

$p_k$
Electron Energy Probability Function (EEPF)

$P_i$
Cumulative collision probability of collision type $i$

$Ry$
Rydberg energy: $Ry = 13.6$ eV

$S$
Total stopping power

$\sigma_{ion}$
Ionization singly-differential cross section (SDCS) in cm$^{-2}$,eV$^{-1}$

$\overline{s}$
SDCS-derived stopping power

$T_p$
Projectile reduced kinetic energy: $T_p = E_p\frac{m_e}{m_p}$

$\Delta t$
Time resolution for the slowing-down process

$\delta t$
Monte Carlo sampling time

$U$
Excitation potential energy in eV

$v_e$
Electron velocity in m s$^{-1}$

$v_d$
Bulk drift velocity in m s$^{-1}$

$v_p$
Projectile velocity in m s$^{-1}$

$v_r$
Reduced projectile velocity $=\sqrt{T_p/Ry}$

$x_p$
Projectile position

$Z_p$
Projectile charge

$Z_{eff}$
Effective projectile charge

$\zeta$
Random number from a uniform distribution between 0 and 1

amounts to about 1 MeV/nucleon, no relativistic correction has to be applied.

![](./images/812570344928837633_4.jpg)

Fig. 1. Overview the various phenomena implemented in SCENA.

As a reminder, the total stopping power $S$ is defined as the opposite of the ratio of the kinetic energy loss $dE$ to the variation of the heavy ion range $dx$

$$
S=-\frac{dE}{dx} \tag{1}
$$

It is also noteworthy that $S$ is a mesoscopic quantity that can be regarded as a friction force. As a result, one can compute the heavy ion velocity $v_p$ and position $x_p$ along the straight track by solving Newton's second law of motion with the first-order explicit Euler method. For the ith time step, it gives:

$$
v_{p,i+1}=v_{p,i}-\frac{S(v_{p,i},Z_{eff,i})}{m_p}\Delta t \tag{2}
$$

$$
x_{p,i+1}=x_{p,i}+v_{p,i}\Delta t \tag{3}
$$

the time resolution $\Delta t$ is as small as tenths of picoseconds. The stopping power $S$ is preferably estimated with the code SRIM [7], even though the Bethe-Bloch formula [6,9] or tabulated experimental data of ICRU-73 [10,11] or other codes such as MSTAR [12] or PASS [13] can be used instead.

Independently of the chosen stopping power source or model, at each time step $i$, the heavy ion effective charge $Z_{eff}$ is computed with the Barkas formula [20]. This entity is of prime interest for computing the stopping-power $S$, as a $Z_{eff}^2$ factor appears in the Bethe-Bloch formula or its variants, but also for later estimation of the delta electrons energy spectrum. In the case of fission chambers, electronic stripping of a heavy ion leaving the fissile layer strongly influences its

![](./images/812570344928837633_5.jpg)

Fig. 2. Experimental and theoretical estimations of the single differential cross section (SDCS) of delta-electron emission from 1 MeV protons impacting argon atoms: HKS-Bernal et al. [14], HKS-ICRU55 [15], HKS-revision 1997 [16], Rutherford [16], Stolterfoht 1997 [16], Gryzinski 1965 [17], Rudd 1992 [18], Toburen 1979 [19] (experiment). A good agreement is noticed between the experimental data (Toburen 1979) and the two revised HKS models (HKS-ICRU55, HKS-revision 1997). In SCENA, the HKS-revision model is employed only. It matches the HKS-ICRU55 model in high energy domain.

stopping power [21]. As recommended in Ref. [22], the initial charges of fission fragments were considered to be 14-15 for LFF, and 12-13 for HFF (most probable Heavy Fission Fragment) in the case of a less-than-1-μ m thick Californium layer. Adjustments of initial effective charges $Z_{eff}$ based on comparing with the values obtained from the Barkas equation lead to an initial charge of +13.6 for HFF and another of +16 for LFF escaping a $^{235}$U layer.

In SCENA, every heavy ion track is split into 1-mm segments know- ing that a total path length is about 45 mm at most in Neon at 1 atm. Fig. 3 shows the evolution of projectile heavy-ion's parameters along these mm-long segments. Simulation of the scintillation track along mm-long segments allows averaging of seed delta electrons profiles, but also to estimate a space-dependent optical emission spectra. For subsequent light emission spectrum calculations, the mean values of the heavy ion stopping power $\bar{S}$, effective charge $\overline{Z}_{eff}$ and kinetic energy $\overline{E}_{p}$ are estimated over each segment and stored.

### 2.2. Delta electron emission

The main part of the heavy ion energy loss in the filling gas contributes to the emission of the delta electrons responsible for the subsequent excitation of the gas atoms [23-26]. It is noteworthy that a direct excitation by heavy ions themselves is much less significant and can be neglected [27].

In this section, we aim to estimate the energy distribution of these delta electrons only since the angular distribution is of no interest in the case of ionization chamber. Indeed, an impinging heavy ion travels along any direction and delta electrons are then likewise emitted in any direction.

A satisfactory expression of this energy distribution is provided by the single differential cross section (SDCS) initially derived by Hansen- Kocbach-Stolterfoht (HKS) and then revised by Stolterfoht [16,28]. This derivation is based on various model assumptions including the semi-classical approximation that describes the kinematics quantities after a classical approach while the cross section is derived using quantum physics. The free electron approximation is also employed and allows for modeling the outgoing electron with a plane wave. At last, an empirical revision prevents the cross section singularity that happens when the electron energy tends to zero [16,18].

Fig. 2 shows various experimental and theoretical estimations of the SDCS of delta-electron emission from 1 MeV protons impacting argon atoms. A good agreement is met between experimental data and the two HKS models [15,16] for low electron energy. Likewise, an acceptable discrepancy of about 30% with experimental data at high electron energy (greater than 100 eV) is observed, though the measurement uncertainties are unknown. As a result, we made the decision to implement in our SCENA code the HKS model revised by Stolterfoht [16] (see Fig. 3).

For the sake of clarity, it is important to note that the kinetic energy $E_{p}$ of a heavy ion of mass $m_{p}$ is turned into a reduced quantity $T_{p}$:
$$
T_{p}=E_{p} \frac{m_{e}}{m_{p}} \tag{4}
$$

This way, the projectile is viewed as an electron of mass $m_{e}$ with the same velocity. As in Ref. [15], one also defines the dimensionless reduced velocity $v_{r}$ normalized w.r.t. the Rydberg energy $Ry$:
$$
v_{r}=\sqrt{T_{p} / R y} \tag{5}
$$

The ionization SDCS of a target-electron with a binding-energy $I_{b}$ is not only a function of its escaping kinetic energy $\epsilon$, but also dependent of the heavy ion effective charge $Z_{eff}$ and reduced velocity $v_{r}$ [15]:
$$
\begin{aligned}
\frac{d \sigma_{i o n}}{d \epsilon}\left(\epsilon ; I_{b}, Z_{e f f}, T_{p}\right)=& \frac{8}{3} \frac{a_{0}^{2} Z_{e f f}^{2}}{R y v_{r}^{2} k_{c}^{3} \alpha \tilde{k}} × \\
& {\left[\arctan \left(\frac{2 \tilde{k}}{1+\tilde{K}_{m}^{2}-\tilde{k}^{2}}\right)+f\left(\tilde{K}_{m}+\tilde{k}\right)-f\left(\tilde{K}_{m}-\tilde{k}\right)\right] }
\end{aligned} \tag{6}
$$
with the rational function
$$
f(u)=\frac{5 u+3 u^{3}}{2\left(1+u^{2}\right)^{2}} \tag{7}
$$
and the average velocity $\alpha$ of the target bound electron, the two normalized momenta $\tilde{K}_{m}$ and $\tilde{k}$, the minimum reduced momentum transfer $K_{m}$ and the reduced momentum of the ejected electron $k$
$$
\alpha=\sqrt{I_{b} / R y}, \quad \tilde{K}_{m}=\frac{K_{m}}{\alpha}, \quad \tilde{k}=\frac{k}{\alpha}, \quad K_{m}=\frac{\alpha^{2}+k^{2}}{2 v_{r}}, \quad k=\sqrt{\epsilon / R y} \tag{8}
$$

The semi-empirical form of the reduced momentum $k_{c}$, which prevents from a singularity in the low electron energy domain due to the peaking approximation ($k_{c}=k$) that neglects the momentum of the bound electron, is given by [16]
$$
k_{c}=\left[k^{2}+\alpha^{2} \frac{3}{2}\left(\ln \frac{2 v_{r}^{2}}{\alpha^{2}}\right)^{-2 / 3}\right]^{1 / 2} \tag{9}
$$

As aforementioned in the previous section, SCENA estimates the delta electron production for every 1-mm heavy ion track segment. The so-obtained average SDCS is then
$$
\frac{d \bar{\sigma}_{i o n}}{d \epsilon}\left(\epsilon ; I_{b}, \overline{Z}_{e f f}, \bar{T}_{p}\right) \tag{10}
$$

![](./images/812570344928837633_6.jpg)

Fig. 3. Ionization data computed with SCENA along a heavy ion track: (a) number of $\delta$-electrons $n_{\delta}$, (b) average $\delta$-electron energy $\overline{E}_{\delta}$, (c) heavy ion energy loss $\overline{s}$ and (d) heavy ion effective charge $Z_{eff}$. Results are presented for a theoretical heavy fission fragment of mass number 130, charge 54, emitted at 68 MeV with an effective charge of 13.6 into a 1-atm and 300-K argon gas.

Integrating over $\epsilon$ likewise yields the average Total Integrated Cross Section (TICS) for the ionization of a single bound electron

$$
\overline{\sigma}_{ion}(I_{b}, \overline{T}_{p}, \overline{Z}_{eff}) = \int_{0}^{\infty} \frac{d\overline{\sigma}_{ion}}{d\epsilon} d\epsilon \tag{11}
$$

The average energy of a delta electron can be also defined

$$
\overline{E}_{\delta} = \frac{1}{\overline{\sigma}_{ion}} \int_{0}^{\infty} \epsilon \frac{d\overline{\sigma}_{ion}}{d\epsilon} d\epsilon \tag{12}
$$

For each 1-mm track segment ($\delta x = 1$ (mm)), the number $n_{\delta}$ of ejected delta electrons

$$
n_{\delta} = \delta x \, N \sum_{i \in \text{bound } e^{-}} \overline{\sigma}_{ion}(I_{b,i}, \overline{T}_{p}, \overline{Z}_{eff}) \tag{13}
$$

where $I_{b,i}$ is the binding energy of the electron number $i$ of all the gas atom shells, and $N$ the atomic density of the gas itself.

Likewise, an alternative estimation $\overline{s}$ of the ionization energy loss summed over all the bound electrons can be derived

$$
\overline{s} = \left. \frac{\delta \overline{E}_{p}}{\delta x} \right|_{\delta x=1\ \text{mm}} = -N \sum_{i \in \text{bound } e^{-}} \int_{0}^{\infty} (\epsilon + I_{b,i}) \frac{d\overline{\sigma}_{ion}(I_{b,i}, \overline{T}_{p}, \overline{Z}_{eff})}{d\epsilon} d\epsilon \tag{14}
$$

$\overline{s}$ can be compared and normalized to tabulated experimental data so that one can ensure a coherent slowing-down profile along the heavy ion track.

### 2.3. Electron cascade

Primary electrons have enough energy to trigger further electron-impact ionizations in a rare gas. In this section, the cascade model describing the birth, interactions and death of these so-generated electrons is presented. A Monte Carlo approach featuring two methods is adopted. The former is the counting method adapted to plasmas with a low ionization degree such as optical unbiased ionization chambers. This main method of SCENA, detailed hereafter and depicted in Fig. 4, outputs the density $n_{e}$ of the delta electrons generated along the heavy ion track as well as that of excited gas atoms responsible for scintillation. The latter is the convolution method that can be used to simulate only plasmas energized by an electric field, which feature a higher ionization degree. In SCENA, this is an optional method for test purpose only, which outputs reaction rates for comparisons with other codes.

#### 2.3.1. Cross-sections

Cross-section data $\sigma_{i}(\epsilon)$ for any collision type $i$ can be downloaded from the open-source database repository LX-cat, hosted by IST-Lisbon [29]. Their energy range is from 1E-4 to 100 or 1000 eV, whereas it has to span up to a few keV. Indeed, after the binary encounter theory, the maximum energy of delta electrons is given by [16]

$$
\epsilon_{BE} = 4T_{p}cos^{2}\theta, \quad 0 \leq \theta \leq 90^{\circ} \tag{15}
$$

where $\theta$ is the electron emission angle. As an example, a direct collision between a bound electron and a 5 MeV alpha particle can eject a delta electron with an energy up to 2.7 keV. The extension of cross section data $\sigma_{i}(\epsilon)$ in the keV range can be obtained using a fitting model based on the Lotz empirical formula [30]:

$$
\sigma_{i}(\epsilon) \propto \frac{log(\epsilon)}{\epsilon} \quad \text{for} \quad \epsilon \gg I_{b} \tag{16}
$$

#### 2.3.2. Collision frequencies

Since the occurrence of any collision type $i$ is described by a Poisson process, the random time between two collisions has an exponential distribution, the rate parameter of which is the collision frequency $\kappa_{i}$

$$
\kappa_{i}(\epsilon) = N \sigma_{i}(\epsilon) v_{e} \tag{17}
$$

![](./images/812570344928837633_7.jpg)

Fig. 4. Flowchart of the counting method implemented in SCENA for the electron cascade Monte Carlo simulation.

The definition of the total collision $\kappa_{total}$ frequency is required to implement the Monte Carlo technique. It is the sum of $k$ processes collision frequencies of type $i$.

$$
\kappa_{total}(\epsilon)=\sum_{i=1}^{k} \kappa_{i}(\epsilon)
\tag{18}
$$

In order to enhance computing accuracy, a fictitious collision for the free flight between any real collisions is introduced [31-33]. Its collision frequency is defined by

$$
\kappa_{0}(\epsilon)=\kappa_{max}-\kappa_{total}(\epsilon)
\tag{19}
$$

with the maximum collision frequency $\kappa_{max}$ given by

$$
\kappa_{max}=\max _{\epsilon} \kappa_{total}(\epsilon)
\tag{20}
$$

An electron undergoing a null-collision will keep moving under the effect of its own inertia or an external force. It is noteworthy that the maximum collision frequency $\kappa_{max}$, which is energy-independent, can be regarded as the sum of all collision types, including the null-collision one

$$
\kappa_{max}=\sum_{i=1}^{k} \kappa_{i}(\epsilon)
\tag{21}
$$

### 2.3.3. Sampling time
During a free flight, the new electron position is derived from the random sampling time $\delta t$, also called census time, which is given by

$$
\delta t=-\frac{1}{\kappa_{\max }} \ln (1-\zeta)
\tag{22}
$$

where $\zeta$ is a random number uniformly distributed between 0 and 1. The reciprocal of the maximum collision frequency $\kappa_{max}$ is a fixed value about 100 fs for all Monte Carlo cycles. An increase in computation time may be brought by fixing $\kappa_{max}$ as many null-collisions may occur, but its update at each cycle may have led to some unwanted errors.

### 2.3.4. Selection of collision type
For each Monte Carlo cycle, a collision type $j$ (null, ionization, excitation or elastic) is selected if the random number $\eta$ uniformly distributed between 0 and 1 satisfies the following inequality

$$
0<\eta \leq P_{i}(\epsilon) \quad \text { with } \quad i=0, \quad P_{i-1}(\epsilon)<\eta \leq P_{i}(\epsilon) \quad \text { with } \quad i \neq 0
\tag{23}
$$

where $P_{i}(\epsilon)$ is the cumulative collision probability

$$
P_{i}(\epsilon)=\frac{1}{\kappa_{\max }} \sum_{j=0}^{i} \kappa_{j}(\epsilon)
\tag{24}
$$

Each electron is fully described in SCENA by a matrix row containing its position in Cartesian and cylindrical coordinate systems and its

velocity components. In the case of an excitation event, an atomic level to be populated is also randomly determined using the corresponding cross-section for the given electron energy.

### 2.3.5. Electric field and swarm size
An electric field can be applied not only to mock processes taking place in a standard voltage-biased ionization chamber, but also to make possible a comparison with other codes such as BOLSIG+ [34,35], LoKi- B [36] or METHES [37]. Unlike SCENA, these codes simulate only low temperature plasmas excited by an external source like an uniform and constant electric field.

In the case of a strong electric field of several tens of Townsend, an electron avalanche due to high ionization rates may dramatically increase the electron swarm size resulting in a larger computation time and possible memory overflow. Without electric field, the ionization due to a heavy ion of about 1 MeV/nucleon causes the multiplication of the electron swarm by a factor of 2 or 3 due to rare occurrences of keV-ranged delta electrons. Such a case does not require a swarm size control.

### 2.3.6. Termination and output
The Monte Carlo simulation is terminated in various cases: (a) when all the free electron kinetic energies fall below the first excitation potential of the target atom, (b) after a fixed time or (c) any other condition set by the user. The mean distance between the original heavy ion track and electron final locations is computed and referred as to the plasma tube radius $r$. The breeding ratio between the total numbers of electrons at the end $(t_{f})$ and start (t=0 s) of the simulation, respectively, is computed

$$
B R_{e}=\frac{N_{e}\left(t_{f}\right)}{N_{e}(t=0)} \tag{25}
$$

Finally, the total electron density in a 1-mm long plasma tube $n_{e}$ is provided

$$
n_{e}=\frac{N_{e}(0) B R_{e}}{\pi r^{2}} \tag{26}
$$

Another important output is the density $n_{i}$ of the excited gas atoms in the levels $i$, which are recorded in a file to be used by the SCENA gas scintillation subroutine or any other cold-plasma simulation code.

### 2.3.7. Optional convolution method
When an electron swarm is energized by an external electric field, a high ionization degree causes the cold plasma to reach a steady state. This way, the cascade electron energies can be binned into a normalized histogram, namely the Electron Energy Probability Function (EEPF) $p_{k}$, that grows quick enough to get good statistics [38]. As a result, the collision rate $K_{i}$ of a collision type $i$ [33] over the whole electron energy domain $D_{e}$ can be computed using the following convolution:

$$
K_{i}=N \sum_{k \in D_{e}} v_{e} \sigma_{i}(\varepsilon) p_{k} \tag{27}
$$

When a steady state begins at the time $t_{s}$, the swarm center-of-mass position $r_{f}$ is recorded. The simulation is then stopped at the final time $t_{f}$ when the electron swarm median energy does not fluctuate more than 10% for at least 5 cycles. The new swarm center-of-mass position $r_{f}$ is recorded and the bulk drift velocity is estimated

$$
v_{d}=\frac{r_{f}-r_{s}}{t_{f}-t_{s}} \tag{28}
$$

The transverse diffusion coefficient $D$ is defined by [39]

$$
D=\frac{1}{2} \frac{\left\langle\left(r_{f, k}-\left\langle r_{f, k}\right\rangle\right)^{2}\right\rangle}{t_{f}-t_{s}} \tag{29}
$$

where the average $\langle-\rangle$ is carried out over all the electron positions $r_{f, k}$ at $t_{f}$. As already aforementioned, the convolution method with its specific outputs is employed for validation purpose only, using either experimental reference values or data obtained with other codes.

![](./images/812570344928837633_8.jpg)

Fig. 5. Mechanisms considered in our simplified cold-plasma model to estimate relative emission line ratios of an optical ionization chamber.

### 2.4. Gas scintillation
In the case of a typical optical fission chamber filled with Argon, the relaxation times of electrons and excited gas atoms are equal to about 0.1 and 10 ns, respectively. As a result, the gas scintillation simulation can be uncoupled from that of the heavy-ion and electron transport. Depending on the previously computed electron density (see Section 2.3.6), either the corona, collisional-radiative or customized cold-plasma model is used to compute an optical emission spectrum. Since the gas scintillation happens merely at the end of the electron cascade, the free electron density is as low as about $10E12\ \mathrm{cm}^{-3}$. This way, the relaxation mechanism can be solely modeled by the spontaneous photon emission depicted in Fig. 5. At such a low ionization degree, the plasma chemistry can be neglected as well. This is the reason why neither the excimer molecule formation nor inter-species electron transfers are taken into account.

After all these assumptions, the relative time-integrated intensity of gas-atom emission lines at the wavelength $v_{j i}$ corresponding to the decay from the upper level $i$ down to the lower level $j$ is given by

$$
I_{i j} \propto N_{j} A_{j i} h v_{i j} \tag{30}
$$

where $n_{j}$ is the density of the excited gas atoms in the levels $j$, provided by the SCENA cascade subroutine (see Section 2.3.6). The NIST Atomic spectra database [40] provides wavelengths $v_{j i}$ and emission probabilities $A_{j i}$, also known Einstein coefficients.

## 3. Code validation
SCENA is capable of producing physical data to be checked against experimental values and other numerical methods. Stopping powers, SDCS, TICS, cold-plasma reaction rates, EEDF can be retrieved among other parameters relevant for optical ionization chamber studies and future model implementations. More peculiarly, SCENA differs from other Boltzmann codes in the fact that, as shown in Fig. 6, it can simulate the evolution of an electron swarm resulting from the gas ionization of a heavy ion in the absence of an electric field.

This section will bring some evidence of the SCENA validation using both experimental and computed data found in the literature.

### 3.1. Heavy ion transport
Fig. 7 shows the comparison between the stopping power values provided by SRIM and SCENA. The former are derived from experimental data, whereas the latter from the SDCS (Section 2.2). The stopping

![](./images/812570344928837633_9.jpg)

Fig. 6. 3-dimension views of the electron swarm energy distribution (colour circles) produced at 100 ps after the emission of a fission fragment (thick red line) without (left) and with (right) an external electric field. X-axis in labeled in mm, y and z-axis in $\mu$m. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

![](./images/812570344928837633_10.jpg)

Fig. 7. SRIM total(dotted line) and SCENA SDCS-integrated (solid line) stopping powers for a heavy fission fragment in 1-atm argon (left) and an alpha particle in 1-atm neon (right) using Eq. (14).

![](./images/812570344928837633_11.jpg)

Fig. 8. Singly-Differential Cross-Section for various projectile-target combinations. The HKS-computed data obtained with SCENA are denoted with lines. The experimental data references are: 1 MeV proton in argon from Rudd et al. [19], 72 MeV bare carbon ion in water vapor from Champion [41], 48 MeV oxygen ion in water vapor from Bhattacharjee et al. [42], and fission fragments in helium from Dyachenko [43]. For that combination, an average-like fission fragment is used.

power for a HFF and that for an alpha particle are displayed. The HFF releases much more energy before reaching the Bragg peak that is only apparent with the SRIM stopping power values. It is important to remind that SCENA aims to estimate the delta electron generation along the track of a heavy ion. This way, one is interested in the energy domain where the ionization process is preponderant, what corresponds to energies greater than about 10 MeV, at the left side of the Bragg peak. The noticed discrepancy goes from 20% down to less than 1%.

For the alpha particle, the Bragg peak is much more apparent since the smaller energy release within the gas will accordingly generates a smaller amount of delta electrons. For energies greater than 2 MeV, the observed discrepancy is about 5%. It is noteworthy that this overall good agreement in the stopping power within the ionization energy domain implicitly validates the computation of the SDCS performed by SCENA.

![](./images/812570344928837633_12.jpg)

Fig. 9. Drift velocity (left top), ionization rate (right top) and mean electron energy (left bottom) as function of the reduced electric field. EEDF (right bottom) of argon excited by a 100 Td reduced electric field. All results are presented for argon at 1 atm using IST-Lisbon cross sections, with a swarm population of 1E5 in SCENA. Secondary electron energy were emitted using cross sections from Green and Opal.

![](./images/812570344928837633_13.jpg)

Fig. 10. Population of neutral Argon levels in a 5.5 MeV alpha particle induced plasma along its track. The Bragg peak segment is located 19 to 20 mm from the alpha particle emission point. Pressure is 2 atm, room temperature.

### 3.2. Delta electron emission

Fig. 8 displays a comparison between the HKS model and experimental data for various combinations of heavy ions and gas atoms. For each combination, the HKS-computed SDCS somehow resembles their experimental counterpart. Even in the extreme case of the 72-MeV fully-stripped carbon ion in water vapor, a good agreement of a factor 2 is obtained. Remarkably, this discrepancy is less than the measurement uncertainties given in Ref. [41].

The case for fission-fragments is less successful. In Ref. [43], Dyachenko measured the SDCS obtained from the slowing-down of $^{252}$Cf-spontaneous-fission fragments in helium. The comparison with a simulation is made much more intricate since this is not only one projectile that causes the gas ionization. In spite of the use of an average-like fission fragment as proposed by Rykov [5], the HKS-computed SDCS has exhibited no further improvement, especially at energies below 30 eV and above 80 eV. Dyachenko came to the same result when comparing these experimental data with a Gryzinski model for SDSC [43]: a discrepancy up to an order of magnitude was observed.

![](./images/812570344928837633_14.jpg)

Fig. 11. Theoretical optical emission spectrum in the visible to near-infrared range of a 2 atm Argon and 3.5 atm Neon plasma along the first mm of the projectile heavy-ion, both excited by a 5.5 MeV alpha particle having a range of about 20 mm. No line broadening mechanisms are considered and the sole spontaneous radiative mechanism is responsible of de-excitations.

Luckily, an extensive data collection checked against recent experiments in various fields of application and over a large set of projectile-target combinations seems to confirm the HKS model as reliable [44,45].

### 3.3. Electron cascade generation

The secondary electron cascade model implemented in SCENA is compared to well-know codes developed for electric-field-driven cold-plasmas. This comparison shown in Fig. 9 is carried out using the following premises: (a) initial electrons at rest, (b) electron swarm set to origin, (c) electric field constant along the z-direction, (d) simulation stopped at steady state (Section 2.3.7). The ionization, excitation and elastic scattering cross-sections were downloaded in July 2019 from the LXcat database project [46]. Some cross-sections from the IST-Lisbon were selected for test cases in single atomic-gas configuration [47]. This recently-updated database includes computed and experimental values from several authors, which were validated by solving the homogeneous two-term Boltzmann equation. About 40 levels were evaluated for both argon and neon. The SCENA electron average energy over the tested domain exhibits low discrepancies of about 2% from values obtained with the BOLSIG+ and METHES codes. The drift velocity discrepancy goes from 2% to 5%. The ionization rate exhibits higher discrepancies from 5% to 50%, especially in the low energy range. The EEDF (Electron Energy Distribution Function) case is not of high importance, even though the discrepancy goes up to 10% at most. For the sake of understanding, the EEDF is derived from the EEPF given in Section 2.3.7. In addition, one can note that the two Monte Carlo codes SCENA and METHES need more time to get a steady state in the case of a low reduced electric field $E/N$ less than 1 Td.

In order to complement the SCENA validation, its accuracy was assessed by means of the theoretical gas model proposed by Reid [48] and described by two cross sections. The first one is a constant elastic cross-section, whereas the second one is a linear energy-dependent excitation cross-section. The mean electron energies and drift velocities in various reduced electrical fields are reported in Table 1. Reid computed the mean electron energy $\overline{\epsilon}$, bulk drift velocity $v_d$ and transverse diffusion coefficient $D$ using two alternative methods, namely a Monte Carlo method and a two-term-approximation method. The discrepancies between the SCENA and Reid's Monte Carlo estimated values are less than 5% at most. A comparison with Reid's two-term-approximation estimated values yields similar discrepancies but for the transverse diffusion coefficient with a discrepancy up to about 20% at high reduced electric field $E/N$. As suggested by Reid and shown in Fig. 9, this comes from the fact that a Monte-Carlo approach leads to a higher electron energy distribution in the low energy domain, especially at high reduced electric fields.

<table>
<caption>Table 1: Comparison with Reid's computed data in the case of a theoretical gas model: mean delta-electron energy $\overline{\epsilon}$ (eV), bulk drift velocity $v_d$ (1E6 cm/s) and diffusion coefficient $D$ (1E5 cm²/s) obtained for various reduced electric field $E/N$ values. Monte-Carlo (MC) and two-term approximation (TT) results from [48], SCENA (S) simulation of a 1E6-electron fixed-size swarm for 1E−6 s.</caption>
<thead>
<tr>
<th rowspan="2"></th>
<th colspan="3">$E/N = 1$ Td</th>
<th colspan="3">$E/N = 10$ Td</th>
<th colspan="3">$E/N = 20$ Td</th>
</tr>
<tr>
<th>$\overline{\epsilon}$</th>
<th>$v_d$</th>
<th>$D$</th>
<th>$\overline{\epsilon}$</th>
<th>$v_d$</th>
<th>$D$</th>
<th>$\overline{\epsilon}$</th>
<th>$v_d$</th>
<th>$D$</th>
</tr>
</thead>
<tbody>
<tr>
<td>MC</td>
<td>0.101</td>
<td>1.25</td>
<td>0.986</td>
<td>0.245</td>
<td>6.27</td>
<td>1.175</td>
<td>0.368</td>
<td>8.37</td>
<td>1.197</td>
</tr>
<tr>
<td>TT</td>
<td>0.102</td>
<td>1.27</td>
<td>0.990</td>
<td>0.247</td>
<td>6.45</td>
<td>1.343</td>
<td>0.371</td>
<td>8.64</td>
<td>1.431</td>
</tr>
<tr>
<td>S</td>
<td>0.101</td>
<td>1.28</td>
<td>0.978</td>
<td>0.239</td>
<td>6.26</td>
<td>1.115</td>
<td>0.361</td>
<td>8.55</td>
<td>1.151</td>
</tr>
</tbody>
</table>

### 3.4. Photon emission spectrum

Filling gas excited levels population can be recorded over mm-long segments, as the delta electron spectrum varies greatly along the heavy-ion track. Fig. 10 presents the exited level population of 1 atm neutron Argon at the beginning and end of a 5.5 MeV alpha particle track. Levels at Bragg peak get populated with a higher yield with respect to initial segment, despite a softer electron energy spectrum. No strong modifications of the buffer gas excited level population repartition mechanism are observed on most levels, translating *a priori* conservation of visible and near-infrared emission line ratios along the heavy-ion track.

If a corona plasma model is selected, optical emission spectra of rare gases consist of discrete lines with various intensities, as shown on Fig. 11: The corona model, despite its simplicity and neglection of plasma chemistry, outputs a plausible optical emission spectrum, as our research group [2,3] observed corresponding predominant emission lines in neutral Argon, without continuum component. No direct comparisons between experimental and SCENA-computed spectra can be performed due to the lack of Abel transform on such weak light source.

The use of a well collimated alpha particle source or spectral acquisitions over extended times will contribute to further validation of SCENA corona cold-plasma model.

### 4. Conclusion

The present paper has detailed models and functions of the SCENA code developed for heavy ion induced gas-scintillation studies. Physical models required for ionization singly-differential cross-section computation have been selected. The validation of the main SCENA subroutines has been performed through comparisons against experimental

data and standard test-cases. Electron Energy Distribution Functions, drift velocities and reaction rates are in good agreement with other computer codes. The electron cascade generated by the slowing-down of heavy ions has been implemented to allow for the estimation of gas excited level densities with respect to both the time and space evolution of a fission fragment. In near future, Optical Emission Spectrum of gas- based scintillation neutron detectors will be checked against results from SCENA, enabling the selection of cold-plasma models required for radiative spectrum estimation.

CRediT authorship contribution statement

M. Lamotte: Conceived and designed the analysis, Collected the data, Contributed data or analysis tools, Performed the analysis, Wrote the paper. G. De Izarra: Conceived and designed the analysis, Collected the data, Contributed data or analysis tools, Performed the analysis, Wrote the paper. C. Jammes: Conceived and designed the analysis, Collected the data, Contributed data or analysis tools, Performed the analysis, Wrote the paper.

Declaration of competing interest

The authors declare that they have no known competing finan- cial interests or personal relationships that could have appeared to influence the work reported in this paper.

References

[1] M. Lamotte, G. De Izarra, C. Jammes, Design and irradiation test of an innovative optical ionization chamber technology, Nucl. Instrum. Methods Phys. Res. A (2020) 163945.

[2] M. Lamotte, G. de Izarra, C. Jammes, Development and first use of an experimen- tal device for fission-induced spectrometry applied to neutron flux monitoring, Nucl. Instrum. Methods Phys. Res. A (2019) 163236.

[3] M. Lamotte, G. De Izarra, C. Jammes, Heavy-ions induced scintillation experiments, J. Instrum. 14 (09) (2019) C09024.

[4] Guy Cheymol, Herve Long, Jean Francois Villard, Benoit Brichard, High level gamma and neutron irradiation of silica optical fibers in CEA OSIRIS nuclear reactor, IEEE Trans. Nucl. Sci. 55 (4) (2008) 2252-2258.

[5] V. Rykov, Charge equilibrium of fission fragments after emergence from a solid into gas, At. Energy 83 (1) (1997) 488-492.

[6] H. Bethe, Zur theorie des durchgangs schneller korpuskularstrahlen durch materie, Ann. Phys. 397 (3) (1930) 325-400, http://dx.doi.org/10.1002/andp. 19303970303.

[7] J.F. Ziegler, M.D. Ziegler, J.P. Biersack, SRIM - THe stopping and range of ions in matter (2010), Nucl. Instrum. Methods Phys. Res. 268 (2010) 1818-1823, http://dx.doi.org/10.1016/j.nimb.2010.02.091.

[8] G. de Izarra, M. Lamotte, S. Bréaud, A. Pépino, P. Filliatre, C. Jammes, Cosicaf, a fission chamber simulation tool for academic purposes, in: EPJ Web of Conferences, vol. 225, EDP Sciences, 2020, p. 10003.

[9] F. Bloch, Zur bremsung rasch bewegter teilchen beim durchgang durch ma- terie, Ann. Phys. 408 (3) (1933) 285-320, http://dx.doi.org/10.1002/andp. 19334080303.

[10] I.C. on Radiation Units, Stopping of Ions Heavier than Helium, vol. 73, Oxford University Press, 2005.

[11] P. Sigmund, A. Schinner, H. Paul, Errata and addenda for icru report 73, stopping of ions heavier than helium, J. ICRU 5 (1) (2009) 1-10.

[12] H. Paul, A. Schinner, Judging the reliability of stopping power tables and programs for heavy ions, Nucl. Instrum. Methods Phys. Res. B 209 (2003) 252-258.

[13] P. Sigmund, A. Schinner, Binary theory of electronic stopping, Nucl. Instrum. Methods Phys. Res. B 195 (1-2) (2002) 64-90.

[14] M. Bernal, J. Liendo, The hks model for electron production in liquid water by light ions, Nucl. Instrum. Methods Phys. Res. B 251 (1) (2006) 171-176.

[15] M.E. Rudd, Y.-K. Kim, T. Märk, J. Schou, N. Stolterfoht, L.H. Toburen, Report55, J. Int. Comm. Radiat. Units Meas. os28 (2) (2016) NP-NP. http://dx.doi.org/10.1093/jicru/os28.2.Report55.

[16] N. Stolterfoht, R.D. DuBois, R. DuBois, R.D. Rivarola, Electron Emission in Heavy Ion-Atom Collisions, vol. 20, Springer Science & Business Media, 1997.

[17] M. Gryziński, Classical theory of atomic collisions. i. theory of inelastic collisions, Phys. Rev. 138 (2A) (1965) A336.

[18] M.E. Rudd, Y.-K. Kim, D.H. Madison, T.J. Gay, Electron production in proton collisions with atoms and molecules: energy distributions, Rev. Modern Phys. 64 (2) (1992) 441.

[19] M. Rudd, L. Toburen, N. Stolterfoht, Differential cross sections for ejection of electrons from argon by protons, At. Data Nucl. Data Tables 23 (5) (1979) 405-442.

[20] W. Barkas, D. Evans, Nuclear Research Emulsions, in: Nuclear Research Emul- sions, vols. 1-2, Academic Press, 1963, URL https://books.google.fr/books?id= IPqmnQAACAAJ.

[21] Y.-K. Kim, K.-t. Cheng, Stopping power for partially stripped ions, Phys. Rev. A 22 (1) (1980) 61.

[22] V. Khryachkov, I. Dunaeva, M. Dunaev, N. Semenova, A new method for measuring specific energy losses of fission fragments, Instrum. Exp. Tech. 46 (1) (2003) 19-25.

[23] E. Surdutovich, O. Obolensky, E. Scifoni, I. Pshenichnov, I. Mishustin, A. Solov'Yov, W. Greiner, Ion-induced electron production in tissue-like media and dna damage mechanisms, Eur. Phys. J. D 51 (1) (2009) 63-71.

[24] A.V. Solov'yov, Nanoscale Insights Into Ion-Beam Cancer Therapy, Springer, 2016.

[25] A.V. Solov'yov, E. Surdutovich, E. Scifoni, I. Mishustin, W. Greiner, Physics of ion beam cancer therapy: A multiscale approach, Phys. Rev. E 79 (2009) 011909, http://dx.doi.org/10.1103/PhysRevE.79.011909.

[26] A. Kling, F.J. Barao, M. Nakagawa, L. Tavora, P. Vaz, Advanced Monte Carlo for Radiation Physics, Particle Transport Simulation and Applications: Proceedings of the Monte Carlo 2000 Conference, Lisbon, 23-26 2000, Springer Science & Business Media, 2014.

[27] R. Platzman, Total ionization in gases by high-energy particles: An appraisal of our understanding, Int. J. Appl. Radiat. Isot. 10 (2) (1961) 116-127, http://dx. doi.org/10.1016/0020-708X(61)90108-9, URL http://www.sciencedirect.com/ science/article/pii/0020708X61901089.

[28] C. Champion, M.E. Galassi, P. Weck, C. Abdallah, Z. Francis, M. Quinto, O. Fojón, R.D. Rivarola, J. Hanssen, Y. Iriki, et al., Ionization induced by protons on isolated molecules of adenine: theory, modelling and experiment, J. Phys. Conf. Ser. 488 (2014) 012038.

[29] L. Alves, The ist-lisbon database on Ixcat, J. Phys. Conf. Ser. 565 (2014) 012007.

[30] W. Lotz, An empirical formula for the electron-impact ionization cross-section, Z. Phys. 206 (2) (1967) 205-211.

[31] H. Skullerud, The stochastic computer simulation of ion motion in a gas subjected to a constant electric field, J. Phys. D: Appl. Phys. 1 (11) (1968) 1567.

[32] M.J. Brennan, A.M. Garvie, L.J. Kelly, A monte carlo investigation of e x b discharges in molecular nitrogen, Aust. J. Phys. 43 (1) (1990) 27-44.

[33] M.J. Kushner, Monte Carlo methods for electron transport, PowerPoint presen- tation, 2002, http://uigelz.eecs.umich.edu/pub/short_courses/MCSHORT_0502. pdf.

[34] G. Hagelaar, Bolsig+ electron boltzmann equation solver, 2010.

[35] G. Hagelaar, L. Pitchford, Solving the boltzmann equation to obtain electron transport coefficients and rate coefficients for fluid models, Plasma Sources. Sci. Technol. 14 (4) (2005) 722.

[36] A. Tejero-del Caz, V. Guerra, D. Gonçalves, M.L. da Silva, L. Marques, N. Pinhao, C. Pintassilgo, L. Alves, The lisbon kinetics boltzmann solver, Plasma Sources. Sci. Technol. 28 (4) (2019) 043001.

[37] M. Rabie, C.M. Franck, Methes: A monte carlo collision code for the simulationof electron transport in low temperature plasmas, Comput. Phys. Comm. 203(2016) 268-277.

[38] V. Georgieva, A. Bogaerts, R. Gijbels, Particle-in-cell/monte carlo simulation of a capacitively coupled radio frequency ar/cf 4 discharge: effect of gas composition, J. Appl. Phys. 93 (5) (2003) 2369-2379.

[39] A. Nolan, M.J. Brennan, K. Ness, A. Wedding, A benchmark model for analysisof electron transport in non-conservative gases, J. Phys. D: Appl. Phys. 30 (20)(1997) 2865.

[40] A. Kramida, Yu. Ralchenko, J. Reader, NIST ASD Team, NIST Atomic spectra database, National Institute of Standards and Technology, Gaithersburg, MD, ver.5.6.1, 2018, [Online]. Available: https://physics.nist.gov/asd. [2016, January31].

[41] C. Champion, C.D. Cappello, Theoretical investigations of electron emission after water vapour ionization by light ion impact, in: Proceedings of the Seventh Inter- national Symposium on Swift Heavy Ions in Matter, Nucl. Instrum. Methods Phys. Res. B 267 (6) (2009) 881-884, http://dx.doi.org/10.1016/j.nimb.2009.02.040, URL http://www.sciencedirect.com/science/article/pii/S0168583X09002201.

[42] S. Bhattacharjee, S. Biswas, C. Bagdia, M. Roychowdhury, S. Nandi, D. Misra, J.M. Monti, C.A. Tachino, R.D. Rivarola, C. Champion, et al., Double differential distribution of electron emission in the ionization of water molecules by fast bare oxygen ions, J. Phys. B: At. Mol. Opt. Phys. 49 (6) (2016) 065202.

[43] P. Dyachenko, Experimental and theoretical works performed by the institute of physics and power engineering on the physics of nuclear-induced plasmas, Laser Part. Beams 11 (4) (1993) 619-634.

[44] O. Obolensky, E. Surdutovich, I. Pshenichnov, I. Mishustin, A. Solov'yov, W. Greiner, Ion beam cancer therapy: Fundamental aspects of the problem, Nucl. In-strum. Methods Phys. Res. B 266 (8) (2008) 1623-1628, ion Beam Analysis. http://dx.doi.org/10.1016/j.nimb.2007.11.054, URL http://www.sciencedirect.com/ science/article/pii/S0168583X0701717X.


[45] R. Rechenmann, E. Wittendorp-Rechenmann, B. Senger, Various aspects of heavy charged particle track structures in nuclear emulsion: a starting point for the description of track patterns in tissue-like media, Radiat. Prot. Dosim. 13 (1-4) (1985) 53-59.

[46] L.C. Pitchford, L.L. Alves, K. Bartschat, S.F. Biagi, M.-C. Bordage, I. Bray, C.E. Brion, M.J. Brunger, L. Campbell, A. Chachereau, et al., Lxcat: an open-access, web-based platform for data needed for modeling low temperature plasmas, Plasma Process. Polym. 14 (1-2) (2017) 1600098.

[47] A. Yanguas-Gil, J. Cotrino, L.L. Alves, An update of argon inelastic cross sections for plasma discharges, J. Phys. D: Appl. Phys. 38 (10) (2005) 1588.

[48] I.D. Reid, An investigation of the accuracy of numerical solutions of boltzmann's equation for electron swarms in gases with large inelastic cross sections, Aust. J. Phys. 32 (3) (1979) 231-254.
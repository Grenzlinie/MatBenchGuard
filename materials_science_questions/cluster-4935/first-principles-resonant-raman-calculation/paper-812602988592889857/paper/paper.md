**Optical resonance shift spin-noise spectroscopy**

D. S. Smirnov $^{1,*}$ and K. V. Kavokin $^{2}$

$^{1}$Ioffe Institute, 194021 St. Petersburg, Russia
$^{2}$Spin Optics Laboratory, Saint Petersburg State University, 198504 St. Petersburg, Russia

![](./images/812602988592889857_1.jpg)
(Received 2 March 2020; accepted 18 May 2020; published 8 June 2020)

Quantum spin fluctuations provide a unique way to study spin dynamics without system perturbation. Here we put forward an optical resonance shift spin noise spectroscopy as a powerful tool to measure the spin noise of various systems from magnetic impurities in solids to free atoms and molecules. The quantum spin fluctuations in these systems can shift the optical resonances by more than the homogeneous linewidth and produce huge Faraday rotation noise. We demonstrate that the resonance shift spin noise spectroscopy gives access to the high-order spin correlators, which contain complete information about the spin dynamics in contrast with the second-order correlator measured by conventional Pauli-blocking spin noise spectroscopy. The high-order quantum spin correlators manifest themselves as a comb of peaks in the Faraday rotation noise spectra in a transverse magnetic field. This effect is closely related to the multispin flip Raman scattering observed in the Mn-doped nanostructures.

DOI: 10.1103/PhysRevB.101.235416

### I. INTRODUCTION

The quantum spin fluctuations were first predicted by Felix Bloch back in 1946 [1]. With the development of the experimental techniques, the optical spin noise spectroscopy appeared and eventually became a powerful tool for the spin dynamics investigation in a broad class of paramagnetic media, from atomic gases to semiconductors [2,3]. In typical experiments, the spin fluctuations within the small volume of a paramagnetic material produce a stochastic Faraday rotation of the linearly polarized light, which probes the system, and the spin noise spectra are obtained by the Fourier transformation of the time-dependent Faraday rotation.

In a magnetic field perpendicular to the probe beam, the spin noise spectrum shows peaks at the Larmor frequencies of the studied spins, similar to the optically detected magnetic resonance. Quantum-mechanically the spin noise signal can be considered as a result of the interference of the probe beam with the light emission caused by spin-flip forward scattering of the probe light [4,5].

In atomic gases, the dependence of the light scattering amplitude on the spin state of an atom is provided by the Pauli blocking of the optical transitions in certain polarizations, defined by the probed spins orientation. This scenario is also realized for electrons and holes in semiconductors with the pronounced spin-orbit interaction, such as GaAs or CdTe [6]. In the charged quantum dots (QDs), for example, for the electron spin-up or spin-down state, the optical transitions to the singlet heavy hole trion state are possible for $\sigma^{+}$ or $\sigma^{-}$-polarized light only, respectively. In thermal equilibrium, the number of spin-up and spin-down electrons is the same on average, but stochastic spin fluctuations produce a weak Gaussian Faraday rotation noise, which is measured. This type of experiments can be called “Pauli-blocking spin noise spectroscopy.”

The small Faraday rotation angles in Pauli-blocking spin noise spectroscopy make it difficult to detect the spin correlation functions of the orders higher than two [7,8]. In the same time, the complete information about the spin dynamics including its intrinsic quantum properties can be obtained from the complete set of the spin correlators of all orders only [9–11]. As a minimal extension of the standard theories the weak measurements of the third- and fourth-order spin correlators were described [12,13].

An alternative connection between the spin system and the light polarization is realized, for example, in diluted magnetic semiconductors [14]. In this case, the probed spins belong to the $d$-shell electrons of $Mn^{2+}$ ions, embedded into the crystal lattice. Mn atoms do not create localized charge carrier states, and their spins do not affect interband optical transitions directly. However, their spins are coupled to the spins of the conduction electrons and holes by the $sp$-$d$ exchange interaction. The corresponding coupling constant is very large, of the order of 1 eV. Due to this interaction, fluctuations of the magnetic-ion spins modulate the energies of the interband optical transitions (most often involving localized excitons), and this creates a polarization noise of the probe light, so we call this type of experiments “resonance shift spin noise spectroscopy.” The resonance shifts for typical $Mn^{2+}$ concentrations are of the order of a few millielectronvolts. Atomic-like hyperfine structure of $Mn^{2+}$ spin levels was resolved in such experiments with the very diluted CdMnTe quantum wells in weak magnetic fields [15]. The same mechanism is responsible for the observation of the nuclear spin noise in GaAs [16,17]. Moreover the resonance shift spin noise spectroscopy can be applied to any impurities in the semiconductors or to the spins of nuclei of free atoms and molecules.

*smirnov@mail.ioffe.ru

The general arguments, which followed the first Pauli-blocking spin noise measurement [4] establish the relation between the spin noise spectrum and the spin flip Raman spectrum. In the case of the resonance shift spectroscopy, this relation apparently breaks down. Indeed, there exists a phenomenon of the multi-spin-flip scattering, when the resonant Raman spectrum of Mn doped nanostructures shows a comb of up to 15 equally spaced peaks [18–20]. These spectra are explained by the scattering via the virtual magnetic-polaron states, and the observed phenomenon is therefore essentially quantum [21,22]. On the other hand, the Larmor precession of the spin fluctuation of one, several or many $Mn^{2+}$ ions induces the peak in the spin noise spectrum at the single Larmor frequency only, and not at its multiplies.

In this work, we show that the multispin flip Raman scattering in diluted-magnetic structures is a counterpart of the high-order quantum spin noise spectra, which can be observed by means of resonance shift spin spectroscopy. We develop a general theory of the resonance shift quantum spin noise spectroscopy and describe in a unified way the spin noise and Raman spectra. We demonstrate that the shape of the spectra is different for the thermal and quantum spin noise. Detection of the high-order spin correlators allows one to completely describe the spin dynamics, and to distinguish between Gaussian and nonnormal spin fluctuations. In particular, we show that for deep impurities in semiconductors and in atomic systems the spin noise spectra strongly differ from the Gaussian noise spectra.

The paper is organized as follows. In Sec. II, we derive the general expression for the Faraday rotation noise spectrum in the framework of the resonance shift spin noise spectroscopy. In Sec. III, we present a model of the semimagnetic quantum wells and QDs, where we anticipate experimental measurement of the higher-order spin correlators. In Sec. IV, we establish the relation between the Faraday rotation noise and Raman spin-flip spectra in different polarizations for this specific system. In Sec. V, we calculate and describe the spectra for the Gaussian spin noise and in Sec. VI, we describe the nonnormal spin noise. Finally, we discuss the applications of our theory to the different spin systems from the solid state to free atoms and summarize our findings in Sec. VII.

## II. GENERAL THEORY

Here we derive the most general expressions for the optical signals in the resonance shift spin noise spectroscopy. We denote the Hamiltonian of the spin system under study by $\mathcal{H}_{0}$, which can include the interaction with external magnetic fields and with the environment. The spin system interacts with the excited states of the system described by the Hamiltonian $\mathcal{H}_{\text{exc}}$, and we denote the interaction Hamiltonian by $\mathcal{H}_{\text{int}}$. Thus the total Hamiltonian has the form
$$
\mathcal{H}(t)=\mathcal{H}_{0}+\mathcal{H}_{\text{exc}}+\mathcal{H}_{\text{int}}+\mathcal{V}(t), \tag{1}
$$
where
$$
\mathcal{V}=-\boldsymbol{P}^{\dagger} \boldsymbol{E} e^{-i \omega_{p} t}+\text { H.c., } \tag{2}
$$
describes the optical excitation of the excited states. Here, $\boldsymbol{P}$ is the dipole moment operator (in the Schrödinger representation), $\omega_{p}$ is the probe frequency, and $\boldsymbol{E}$ is the amplitude of the incident electric field. The probe light induces a dipole polarization, which is described by the Heisenberg time-dependent operator $\boldsymbol{P}(t)$. In Appendix A, we demonstrate that it has the form $\boldsymbol{P}(t)=\boldsymbol{P} \psi(t)$, where $\psi(t)$ is a dimensionless operator, which satisfies the transparent equation
$$
\frac{d \psi(t)}{d t}=\frac{i}{\hbar} \boldsymbol{P}^{\dagger} \boldsymbol{E} e^{-i \omega_{p} t}-\frac{i}{\hbar}\left[\mathcal{H}_{\mathrm{exc}}+\tilde{\mathcal{H}}_{\mathrm{int}}(t)\right] \psi(t)-\gamma \psi(t).
\tag{3}
$$

Here we introduced the interaction Hamiltonian in the interaction representation
$$
\tilde{\mathcal{H}}_{\mathrm{int}}(t)=e^{i \mathcal{H}_{0} t / \hbar} \mathcal{H}_{\mathrm{int}} e^{-i \mathcal{H}_{0} t / \hbar} \tag{4}
$$
and an optical transition dephasing rate $\gamma$. Equation (3) can be formally integrated, and the result for the time-dependent exciton polarization reads $^{1}$
$$
\begin{aligned}
\boldsymbol{P}(t)= & \frac{i}{\hbar} \boldsymbol{P} \int_{0}^{\infty} e^{-i \omega_{p}(t-\tau)-\gamma \tau} \\
& \times \mathcal{T} \exp \left[-\frac{i}{\hbar} \int_{0}^{\tau} \mathcal{H}_{\mathrm{exc}}^{\prime}\left(t-\tau^{\prime}\right) d \tau^{\prime}\right] d \tau\left(\boldsymbol{P}^{\dagger} \boldsymbol{E}\right). \quad(5)
\end{aligned}
$$

Here, $\mathcal{T}$ exp denotes the normal time ordered exponential (later times on the left) and $\mathcal{H}_{\mathrm{exc}}^{\prime}(t)=\mathcal{H}_{\mathrm{exc}}+\tilde{\mathcal{H}}_{\mathrm{int}}(t)$ is an effective time-dependent Hamiltonian of the excited states. It is this part of the expression that contains information about parameters of spin dynamics $(\mathcal{H}_{0})$. The obtained general expression allows one to describe various physical systems and experimental conditions. In the next section, we consider a specific case, when this expression is greatly simplified.

The spin noise spectra are typically measured using the linearly polarized light,
$$
\boldsymbol{E}=E_{0} \boldsymbol{e}_{x}, \tag{6}
$$
where $E_{0}$ is an amplitude of the probe light, and $\boldsymbol{e}_{x}$ is a unit vector along $x$ axis. The optical Faraday and ellipticity signals, $\mathcal{F}$ and $\mathcal{E}$, respectively, are measured in the transmission or reflection geometry. They are given by the real and imaginary parts of the complex value [23]
$$
\mathcal{F}-i \mathcal{E}=E_{x}^{\prime *} E_{y}^{\prime}. \tag{7}
$$

Here, $E^{\prime}$ is the amplitude of the emitted (or scattered) light. It consists of the contribution from the elastic scattering and the secondary emission by the exciton dipole polarization:
$$
\boldsymbol{E}^{\prime}=a \boldsymbol{E}+b \boldsymbol{P}(t), \tag{8}
$$
where $a$ and $b$ are complex coefficients, which depend on the geometry of the structure [17].

The Faraday rotation angle of the probe polarization plane and the ellipticity angle are given by
$$
\theta_{F}-i \theta_{E}=\frac{\mathcal{F}-i \mathcal{E}}{\mathcal{I}}, \tag{9}
$$
where $\mathcal{I}=|E_{x}^{\prime}|^{2}$ is proportional to the intensity of the detected light. Here we assume that the angles are small, $\theta_{F,E} \ll 1$

$^{1}$This polarization operator is projected on ground state of $\mathcal{H}_{\mathrm{exc}}$.

or, equivalently, $|E_{y}^{\prime}| \ll |E_{x}^{\prime}|$. Usually the scattering is weak, $bP_{x} \ll aE_{0}$, so by virtue of Eq. (8) we arrive to
$$
\theta_{F}+i \theta_{E}=\frac{E_{y}^{\prime}}{E_{x}^{\prime}}=\frac{b}{a E_{0}} P_{y}. \quad(10)
$$

This expression shows that the spin signals are proportional to the exciton polarization along $y$ axis.

The optical signals noise spectra are defined as the Fourier transform of the correlation functions:
$$
\left(\theta_{F, E}^{2}\right)_{\Omega}=\int_{-\infty}^{\infty}\left\langle\theta_{F, E}(t) \theta_{F, E}(t+\tau)\right\rangle_{s} e^{i \Omega \tau} d \tau. \quad(11)
$$

Here the angular brackets denote quantum mechanical averaging and the subscript " $s$ " denotes the symmetrized correlation function
$$
\langle\theta(0) \theta(\tau)\rangle_{s}=\frac{\langle\theta(0) \theta(\tau)+\theta(\tau) \theta(0)\rangle}{2}. \quad(12)
$$

In the steady state, the averages do not depend on time $t$, so for the rest of the paper, we set $t=0$ in the correlation functions. The symmetrization is related to the fact that the detected light is almost classical and the optical spin signals are selfhomodyned [24-26]. From Eqs. (10) and (11), one can see that the Faraday and ellipticity noise spectra are determined by the Fourier transform of the correlation function of $P_{y}$. In Pauli-blocking spin noise spectroscopy, this correlator is simply proportional to the spin noise spectrum. However, in the case of the resonance shift spin noise spectroscopy, there is no direct relation between them.

At the same time, the Raman spectrum of the scattered light in polarization $\alpha$ is given by
$$
S_{\mathrm{tot}}(\omega)=\int_{-\infty}^{\infty}\left\langle E_{\alpha}^{\prime *}(t) E_{\alpha}^{\prime}(t+\tau)\right\rangle e^{i \omega \tau} d \tau. \quad(13)
$$

In the general case the Raman spectrum consists of a $\delta$-peak at $\omega=\omega_{p}$, which does not carry information about the spin system, and the rest of the spectrum $S(\omega)$. It can be presented as
$$
S\left(\Omega+\omega_{p}\right)=|b|^{2} \int_{-\infty}^{\infty}\left\langle P_{\alpha}^{*}(0) P_{\alpha}(\tau)\right\rangle e^{i \Omega \tau} d \tau. \quad(14)
$$

Thus we arrive again at the Fourier transform of the polarization correlation function.

The Faraday rotation noise spectra and Raman spin flip spectra are generally expressed through the polarization correlation functions [see Eqs. (10), (11), and (14)], while the polarization is given by the general Eq. (5). In the next section we formulate a specific model, where these spectra can be easily measured.

### III. MODEL

Let us specify the system, which we are going to study in detail to obtain the specific expressions for the polarization, which can be used to calculate Faraday rotation noise spectra and Raman spin flip spectra.

As a model system for the resonance shift spin noise spectroscopy we consider a II-VI semiconductor quantum well doped with manganese. The spins of $\mathrm{Mn}^{2+}$ atoms can be optically monitored via a localized exciton resonance. We assume that the excitons are localized at defects, in QDs, or at imperfections of the interfaces of a quantum well. In this case in Eq. (1), $\mathcal{H}_{0}$ is the Hamiltonian of $\mathrm{Mn}^{2+}$ spin system, $\mathcal{H}_{\text {exc }}$ is the exciton Hamiltonian, $\mathcal{H}_{\text {int }}$ describes the interaction between exciton and $\mathrm{Mn}^{2+}$ spins. The Hamiltonian $\mathcal{H}_{\text {exc }}$ describes the whole fine structure of the excitonic levels, and includes the electron-hole exchange interaction. The spindependent part of the interaction of magnetic atoms with excitons stems from the exchange interaction with electron and hole in the exciton. The general form of this interaction is [27]
$$
\mathcal{H}_{\mathrm{int}}=\hbar \sum_{i}\left[\omega_{\mathrm{ex}, i}^{e} S^{e} \boldsymbol{I}_{i}+\sum_{\alpha} \omega_{\mathrm{ex}, i}^{h, \alpha} S_{\alpha}^{h} I_{i, \alpha}\right], \quad(15)
$$
where $i$ enumerates $\mathrm{Mn}^{2+}$ spins $\boldsymbol{I}_{i}, \boldsymbol{S}^{e}$ and $\boldsymbol{S}^{h}$ are the electron and hole spins in the given exciton, respectively, $\omega_{\mathrm{ex}, i}^{e}$ and $\omega_{\mathrm{ex}, i}^{h, \alpha}$ are the corresponding exchange interaction constants with the Cartesian index $\alpha=x, y, z$. Due to the different symmetry of the electron and hole Bloch wave functions in the $\Gamma$ valley, the electron exchange interaction is isotropic, while for the heavy hole it is not. This anisotropy plays an important role for this system and has the same origin as the anisotropy of the effective $g$ factor.

We focus on the Voigt geometry, when external magnetic field is applied along $x$ direction, perpendicular to the optical axis $z$. The $\mathrm{Mn}^{2+}$ spin Hamiltonian takes a form
$$
\mathcal{H}_{0}=\hbar \Omega_{L} I_{x}, \quad(16)
$$
where
$$
\boldsymbol{I}=\sum_{i=1}^{N} \boldsymbol{I}_{i} \quad(17)
$$
is the total spin of $N$ Mn atoms in the exciton localization volume and $\Omega_{L}=g \mu_{B} B / \hbar$ is the Larmor precession frequency in the magnetic field $B$ with $g$ being the $g$ factor and $\mu_{B}$ being the Bohr magneton. We assume the Mn concentration to be small enough to neglect their exchange interaction. This corresponds to the Mn concentration of a few percent or less.

We stress that we consider here the optical transitions to the localized exciton state, while other types of transitions, e.g., to the trion or to the biexciton state can be described in a similar way. Let us make some other simplifying assumptions, which make the theory transparent and the results very illustrating. First, we neglect the transverse hole $g$ factor, which is usually very small [28]. Second, we assume that the $x$ projection of the electron spin does not change. This means that the magnetic field is not weak, and the electron Zeeman energy exceeds the interaction strength with the random spin components $I_{i, y}$ and $I_{i, z}$. In fact, $\mathrm{Mn}^{2+}$ spins can be partially polarized along the magnetic field at low temperatures, and can create the effective exchange magnetic field along the same direction, which can greatly exceed the external magnetic field for electrons. Below for simplicity we consider only one electron spin state (say, $S_{x}=+1 / 2$ ). This implicitly assumes that the splitting of the electron spin sublevels exceeds the homogeneous and inhomogeneous widths of the optical resonance. Under these assumptions we arrive to the optical V-scheme, which is shown in Fig 1. Here the exciton vacuum state $|g\rangle$ can be

![](./images/812602988592889857_2.jpg)

FIG. 1. Quantum fluctuations of the $Mn^{2+}$ spins (magenta arrows) in the exciton localization volume (green) randomly shift the exciton transitions energies. The states are characterized by the heavy hole spin (red arrow) $J_{z}=\pm 3/2$, while the projection of the electron spin (blue arrow) on the magnetic field does not change.

excited by $\sigma^{+}$ or $\sigma^{-}$ polarized light to the exciton state with the heavy hole spin $J_{z}=\pm 3/2$, respectively.

Without the exchange interaction with the magnetic impurities the two excitonic states are degenerate, so that the exciton Hamiltonian reads
$$
\mathcal{H}_{\text{exc}}=\hbar \omega_{0}n_{\text{exc}},\tag{18}
$$
where $\omega_{0}$ is the resonance frequency and $n_{\text{exc}}$ is the occupancy of both exciton states. The exchange interaction leads to the splitting of the two resonances, which we describe by
$$
\mathcal{H}_{\text{int}}=\hbar \omega_{ex}\frac{2}{3}S_{z}^{h}I_{z}.\tag{19}
$$

Here we neglect the total shift of the two resonances due to the exchange interaction with electron $(\omega_{\text{exc},i}^{e}=0)$ and consider the hole exchange interaction along the $z$ axis only [27]. Also for the simplicity we use the "box" model, setting equal exchange interaction constants for all $Mn^{2+}$ spins within the localization radius of the exciton: $\omega_{\text{exc},i}^{h,\alpha}=(2/3)\omega_{ex}\delta_{\alpha,z}$.

Under these assumptions, the two excitonic states are not mixed. As a results, the circularly polarized $\sigma^{\pm}$ probe light induces the exciton dipole polarization with the same helicity $P_{\pm}(t)=[\mp P_{x}(t)-iP_{y}(t)]/\sqrt{2}$. From Eq. (3) we find that
$$
\frac{dP_{\pm}(t)}{dt}=-i[\omega_{0}\pm \omega_{ex}I_{z}(t)-i\gamma]P_{\pm}(t)+\frac{i}{\hbar}|d|^{2}E_{\pm}e^{-i\omega_{p}t},\tag{20}
$$
where $d$ is the optical transition dipole moment (see Appendix A). This equation clearly shows that the spin polarization $I_{z}(t)$ shifts the exciton resonance energy $\omega_{0}$, which allows one to optically monitor $Mn^{2+}$ spin fluctuations. In fact, it follows from Eqs. (4) and (16) that $I_{z}(t)=\cos(\Omega_{L}t)I_{z}+\sin(\Omega_{L}t)I_{y}$, but we prefer to keep the general notation $I_{z}(t)$, which is valid for arbitrary spin Hamiltonian $\mathcal{H}_{0}$.

It is useful to solve Eq. (20) in the adiabatic approximation. Provided $\Omega_{L}\ll \gamma$ the Mn spin dynamics is slow as compared with the exciton polarization relaxation. In this case one can consider $I_{z}(t)$ as a parameter, which yields
$$
P_{\pm}(t)=\frac{|d|^{2}E_{\pm}}{\hbar}\frac{e^{-i\omega_{p}t}}{\omega_{0}\pm \omega_{ex}I_{z}(t)-\omega_{p}-i\gamma}.\tag{21}
$$

This expression shows that (i) Mn spin polarization shifts the exciton resonance frequency, and (ii) the relation between Mn spin polarization and the exciton dipole polarization is nonlinear. The latter makes it possible to detect high-order spin correlators using the resonance shift spin spectroscopy. Indeed the correlation functions of the polarization have the form
$$
\langle P_{+}^{\dagger}(0)P_{\pm}(\tau)\rangle=E_{+}^{*}E_{\pm}e^{-i\omega_{p}\tau}\sum_{n,n'=0}^{\infty}(\pm 1)^{n'}C_{nn'}\langle I_{z}^{n}(0)I_{z}^{n'}(\tau)\rangle,\tag{22}
$$
where
$$
C_{nn'}=\frac{|d|^{4}}{\hbar^{2}}\frac{(-\omega_{ex})^{n+n'}}{(\omega_{0}-\omega_{p}+i\gamma)^{n+1}(\omega_{0}-\omega_{p}-i\gamma)^{n'+1}}.\quad (23)
$$

One can see that the second-order correlation function contains the contributions from the spin correlation functions of the high orders. So do the Faraday rotation correlation function and Raman spin flip spectra. This gives the experimental access to the high-order spin noise spectra.

Generally, $I_{z}(t)$ in Eq. (21) should be considered as the Heisenberg operator. Only when $I$ is a large classical vector, the corresponding operator can be replaced with its expectation value.

The adiabatic approximation can be often violated (see Sec. VC), making one to use the general expression (5) for the polarization. For $Mn^{2+}$ spin system it reduces to
$$
\begin{aligned}
P_{\pm}(t)=&i\frac{|d|^{2}}{\hbar}E_{\pm}e^{-i\omega_{p}t}\int_{0}^{\infty}e^{i(\omega_{p}-\omega_{0})\tau-\gamma \tau}\\
&\times \mathcal{T}\exp\left[i\omega_{ex}\int_{0}^{\tau}I_{z}(t-\tau')d\tau'\right]d\tau.\quad (24)
\end{aligned}
$$

Here the inner integral can be solved as described in Appendix A, but for the calculation of the spectra of the secondary emitted light this expression is more convenient.

In this section, we expressed the exciton polarization as a function of the $Mn^{2+}$ spins [see Eq. (24)]. In the next section, this expression will be used to derive the Faraday rotation noise spectra and the Raman spin flip spectra.

## IV. SPIN CORRELATION FUNCTIONS AND RESONANCE SHIFT OPTICAL RESPONSE

The exciton polarization is given by Eq. (24), which implicitly depends on $Mn^{2+}$ spin fluctuations. Now let us express the polarization correlation functions through the spin correlation functions.

It is convenient to introduce the dimensionless exciton polarization
$$
\boldsymbol{p}(t)=-\frac{\hbar \gamma}{|d|^{2}E_{0}}\boldsymbol{P}(t)e^{i\omega_{p}t},\tag{25}
$$

where $E_0$ is the amplitude of the incident light. Then we rewrite Eq. (24) as
$$
p_{\pm}(t)=\frac{E_{\pm}}{E_0} \int_{0}^{\infty} e^{-i \delta k-k} \mathcal{T} \exp [\mp i \mathcal{J}(t)] d k,\qquad(26)
$$
where
$$
\delta=\left(\omega_{0}-\omega_{p}\right) / \gamma\qquad(27)
$$
is a dimensionless detuning and
$$
\mathcal{J}(t)=\int_{0}^{k} m\left(t-k^{\prime} / \gamma\right) d k^{\prime}\qquad(28)
$$
with
$$
m(t)=\frac{\omega_{\mathrm{ex}}}{\gamma} I_{z}(t)\qquad(29)
$$
being a dimensionless splitting of the resonance. Further, we note that for the localized excitons, the inhomogeneous broadening usually exceeds by far the homogeneous one (see, e.g., Ref. [18]). Therefore the spin noise and Raman spin flip spectra should be averaged over the detuning as
$$
\overline{\left\langle p_{\alpha}^{*}(0) p_{\alpha}(\tau)\right\rangle}=\frac{1}{2 \pi} \int_{-\infty}^{\infty}\left\langle p_{\alpha}^{*}(0) p_{\alpha}(\tau)\right\rangle d \delta.\qquad(30)
$$

Here we introduced the factor $1/(2\pi)$ to shorten the following expressions.

### A. Spectrum in circular polarization
In this section, we consider an auxiliary problem of $\sigma^{+}$ incident light, so the scattered light has the same polarization, $\alpha=+$. In this case the noise spectrum of $p_{+}(t)$ is proportional to the Raman spin flip spectrum in $\sigma^{+}$ polarization, see Eq. (14). The spectrum in $\sigma^{-}$ polarization is the same.

We substitute in Eq. (30) the exciton polarization from Eq. (26) and obtain the averaged correlation function
$$
\overline{\left\langle p_{+}^{*}(0) p_{+}(\tau)\right\rangle}=\int_{0}^{\infty} e^{-2 k}\left\langle\left[\overline{\mathcal{T}} e^{i \mathcal{J}(0)}\right]\left[\mathcal{T} e^{-i \mathcal{J}(\tau)}\right]\right\rangle d k,\quad(31)
$$
where $\overline{\mathcal{T}}$ denotes the reversed time ordering. The correlator in this expression can be calculated using the cumulant expansion.

Generally, the quantum noise statistics is completely described by the series of cumulants of the random variable [29-31]. In Appendix B, we obtain the general expressions for the polarization correlation function and simplify it for the Gaussian spin noise. To obtain a simple expression for the polarization correlator let us consider again the adiabatic approximation, $\Omega_{L} \ll \gamma$. In this case one can replace $m(t-k'/\gamma)$ in Eq. (28) with $m(t)$. Then from Eq. (31) we obtain
$$
\overline{\left\langle p_{+}^{*}(0) p_{+}(\tau)\right\rangle}=\sum_{n=0}^{\infty} \sum_{l=0}^{2 n} \frac{(-1)^{n+l}}{2^{2 n+1}}\left(\begin{array}{c}
2 n \\
l
\end{array}\right)\left\langle m^{l}(0) m^{2 n-l}(\tau)\right\rangle,
$$
where $\binom{2n}{l}$ is the binomial coefficient. This expression shows again that the polarization correlator and Faraday rotation noise spectra are determined by the spin correlation functions of all orders because of the nonlinear relation between the exciton polarization and the total $\mathrm{Mn}^{2+}$ spin in the limit $I_z \gg 1$ [see, e.g., Eq. (21)].

For Gaussian spin noise, using Eq. (B7), we obtain
$$
\overline{\left\langle p_{+}^{*}(0) p_{+}(\tau)\right\rangle}=\int_{0}^{\infty} e^{-k^{2} \Delta m^{2}(\tau)} e^{-2 k} d k,\qquad(33)
$$
where we introduced
$$
\Delta m^{2}(\tau)=\left\langle m^{2}\right\rangle-\langle m(0) m(\tau)\rangle.\qquad(34)
$$

This integral can be solved as
$$
\overline{\left\langle p_{+}^{*}(0) p_{+}(\tau)\right\rangle}=\frac{1}{2} \sqrt{\frac{\pi}{\Delta m^{2}(\tau)}} e^{1 / \Delta m^{2}(\tau)} \operatorname{erfc}\left(\frac{1}{\sqrt{\Delta m^{2}(\tau)}}\right),
$$
where
$$
\operatorname{erfc}(x)=\frac{2}{\sqrt{\pi}} \int_{x}^{\infty} e^{-y^{2}} d y
$$
is the complimentary error function.

If exchange interaction is weak, $m(t) \ll 1$ one can use the asymptotic expansion
$$
\overline{\left\langle p_{+}^{*}(0) p_{+}(\tau)\right\rangle}=\frac{1}{2} \sum_{n=0}^{\infty}\left[-\frac{\Delta m^{2}(\tau)}{2}\right]^{n}(2 n-1)!!.\quad(36)
$$

This expression directly relates the spin correlation function $\Delta m^{2}(\tau)$ with the polarization correlator.

### B. Faraday rotation noise spectra and Raman spectra in linear polarizations
Let us return to the linearly polarized probe light, Eq. (6). Similarly to Eq. (26), the dimensionless exciton polarization in this case reads
$$
p_{x}(t)=\int_{0}^{\infty} e^{-i \delta k-k} \mathcal{T} \cos [\mathcal{J}(t)] d k,\qquad(37a)
$$
$$
p_{y}(t)=-\int_{0}^{\infty} e^{-i \delta k-k} \mathcal{T} \sin [\mathcal{J}(t)] d k,\qquad(37b)
$$
where we introduced the notations
$$
\mathcal{T} \cos (x)=\frac{\mathcal{T} e^{i x}+\mathcal{T} e^{-i x}}{2}, \quad \mathcal{T} \sin (x)=\frac{\mathcal{T} e^{i x}-\mathcal{T} e^{-i x}}{2 i}.
$$

Then one can perform the calculations following the lines of the previous subsection. For simplicity, we give the final result for the adiabatic limit [cf. Eq. (33)]:
$$
\left[\begin{array}{l}
\overline{\left\langle p_{x}^{*}(0) p_{x}(\tau)\right\rangle} \\
\overline{\left\langle p_{y}^{*}(0) p_{y}(\tau)\right\rangle}
\end{array}\right]=\int_{0}^{\infty} d k e^{-2 k-k^{2}\left\langle m^{2}\right\rangle}\left[\begin{array}{l}
\cosh \left(k^{2}\langle m(0) m(\tau)\rangle\right) \\
\sinh \left(k^{2}\langle m(0) m(\tau)\rangle\right)
\end{array}\right].
$$

These expressions along with Eq. (14) allow one to directly calculate the Raman spectrum for the given Mn spin correlation function. Here the integrals can be expressed through the error function, and its asymptotic expansions can be found. However, these expressions are cumbersome, and will not be further needed.

As a first step towards the relation between Raman and spin noise spectrum, we consider the Raman spectrum in crossed (y) polarization in the limit $\langle m(t) m(t+\tau)\rangle \ll 1$. In this case, the relation between the exciton dipole polarization and Mn

spin polarization it linear, so from Eq. (39), we obtain the spectrum
$$
S(\omega)=\left|b \frac{|d|^{2} E_{0} \omega_{e x}}{\hbar \gamma^{2}}\right|^{2}\left(I_{z}^{2}\right)_{\omega-\omega_{p}},\qquad(40)
$$
where the spin noise spectrum of $\mathrm{Mn}^{2+}$ ions is given by
$$
\left(I_{z}^{2}\right)_{\Omega}=\int_{-\infty}^{\infty}\left\langle I_{z}(0) I_{z}(\tau)\right\rangle e^{i \Omega \tau} d \tau.\qquad(41)
$$

An analogous relation between the Raman spin flip and the spin noise spectra was derived by Gorbovitskii and Perel for Pauli-blocking spin noise spectroscopy [4]. Below we demonstrate that generally a similar relation holds between the multispin flip spectrum and the Faraday rotation noise spectrum instead of the spin noise spectrum.

From Eq. (10), we obtain the correlation functions of the Faraday rotation and ellipticity angles
$$
\left\langle\theta_{F}(0) \theta_{F}(\tau)\right\rangle=\left|\frac{|d|^{2} b}{\hbar \gamma a}\right|^{2}\left\langle p_{y}^{\prime \prime}(0) p_{y}^{\prime \prime}(\tau)\right\rangle_{s},\qquad(42a)
$$

$$
\left\langle\theta_{E}(0) \theta_{E}(\tau)\right\rangle=\left|\frac{|d|^{2} b}{\hbar \gamma a}\right|^{2}\left\langle p_{y}^{\prime}(0) p_{y}^{\prime}(\tau)\right\rangle_{s},\qquad(42b)
$$
where one and two primes denote the real and imaginary parts of the polarization, respectively. Similarly to Eq. (31), we average the correlation functions of $p_{y}^{\prime}(\tau)$ and $p_{y}^{\prime \prime}(\tau)$ over the detuning making use of Eq. (37b), and obtain
$$
\overline{\left\langle p_{y}^{\prime \prime}(0) p_{y}^{\prime \prime}(\tau)\right\rangle_{s}}=\overline{\left\langle p_{y}^{\prime}(0) p_{y}^{\prime}(\tau)\right\rangle_{s}}=\frac{1}{2} \overline{\left\langle p_{y}^{*}(0) p_{y}(\tau)\right\rangle_{s}}.\qquad(43)
$$
This expression differs from the second line of Eq. (39) by a factor and symmetrization.

Thus, the noise spectra of the Faraday rotation and el- lipticity angles can be calculated as a symmetrized Raman spectrum in crossed linear polarizations. In the next section, we calculate and describe these spectra.

## V. FARADAY ROTATION NOISE SPECTRUM IN VOIGT GEOMETRY
In order to calculate the Faraday rotation noise and Raman spin flip spectra one has to (i) find the spin correlation func- tions and (ii) use them to calculate the spectra using Eq. (39).

### A. Spin correlation functions
Here we calculate the correlation functions for the case of Zeeman interaction given by Eq. (16).

The average Mn spin is oriented along $\boldsymbol{B}$ and equals to
$$
\left\langle I_{x}\right\rangle=N s \mathcal{B}_{s}\left(\frac{g \mu_{B} B s}{k_{B} T}\right),\qquad(44)
$$
where $s=5 / 2$ is a single $\mathrm{Mn}^{2+}$ spin, $\mathcal{B}_{s}(x)$ is the Bril- louin function, $k_{B}$ is the Boltzmann constant, and $T$ is the temperature. Using the commutation relations for the spin components, we find also the correlators
$$
\left\langle I_{y} I_{z}\right\rangle=-\left\langle I_{z} I_{y}\right\rangle=\frac{i}{2}\left\langle I_{x}\right\rangle,\qquad(45a)
$$

$$
\left\langle I_{z}^{2}\right\rangle=\left\langle I_{y}^{2}\right\rangle=\frac{N}{2}\left[s(s+1)-\left\langle s_{x}^{2}\right\rangle\right].\qquad(45b)
$$
Notably the first of these two equations is responsible for the quantum part of the spin correlation functions. Indeed, for classical noise the correlation functions do not depend on the order, in which the fluctuating quantities are multiplied. Moreover, Eq. (45b) shows that even at zero temperature, when $\langle s_{x}^{2}\rangle=s^{2}$ , zero-point spin fluctuations $\langle I_{z}^{2}\rangle=N s / 2$ are present.

The time correlation functions for $\tau>0$ obey the equa tions
$$
\frac{d}{d \tau}\left\langle I_{z}(0) I_{z}(\tau)\right\rangle=\Omega_{L}\left\langle I_{z}(0) I_{y}(\tau)\right\rangle-\frac{\left\langle I_{z}(0) I_{z}(\tau)\right\rangle}{\tau_{s}},\qquad(46a)
$$

$$
\frac{d}{d \tau}\left\langle I_{z}(0) I_{y}(\tau)\right\rangle=-\Omega_{L}\left\langle I_{z}(0) I_{z}(\tau)\right\rangle-\frac{\left\langle I_{z}(0) I_{y}(\tau)\right\rangle}{\tau_{s}},\qquad(46b)
$$
where $\tau_{s}$ is a transverse spin relaxation time (we assume that $\hbar / \tau_{s} \ll k_{B} T)$ . The solution of these equations with the initial conditions (45) reads
$$
\begin{aligned}
\left\langle I_{z}(0) I_{z}(\tau)\right\rangle= & \frac{1}{2}\left[\left(\left\langle I_{z}^{2}\right\rangle+\frac{\left\langle I_{x}\right\rangle}{2}\right) e^{i \Omega_{L} \tau}\right. \\
& \left.+\left(\left\langle I_{z}^{2}\right\rangle-\frac{\left\langle I_{x}\right\rangle}{2}\right) e^{-i \Omega_{L} \tau}\right] e^{-|\tau| / \tau_{s}}. \quad(47)
\end{aligned}
$$

Then using the definition (29) we find the dimensionless correlation function
$$
\langle m(0) m(t)\rangle=\left(\mu_{+} e^{-i \Omega_{L} \tau}+\mu_{-} e^{i \Omega_{L} \tau}\right) e^{-|\tau| / \tau_{s}},\qquad(48)
$$
where we introduced
$$
\mu_{ \pm}=\frac{\omega_{e x}^{2}}{2 \gamma^{2}}\left(\left\langle I_{z}^{2}\right\rangle \mp \frac{\left\langle I_{x}\right\rangle}{2}\right).\qquad(49)
$$

The correlator $\langle m(0) m(t)\rangle$ ultimately defines the noise spectra of Faraday rotation and ellipticity, which we analyze in the next subsection.

### B. Faraday rotation noise and Raman spectra
Similarly to Sec. IV, it is convenient to start from the anal- ysis of the exciton dipole polarization correlation function in circular polarizations, which define the corresponding Raman spectra.

To shorten the notation we introduce the scaled spectrum [cf. Eq. (14)]
$$
S_{++}(\Omega)=\int_{-\infty}^{\infty} \overline{\left\langle p_{+}^{*}(0) p_{+}(\tau)\right\rangle} e^{i \Omega \tau} d \tau.\qquad(50)
$$

From Eqs. (36) and (48), one can see that the spectrum consists of the peaks at frequencies $n \Omega_{L}$ , where $n$ is an integer. The general form of the spectrum of circularly polarized exciton dipole polarization is
$$
S_{++}(\Omega)=\sum_{n=1}^{\infty} \sum_{ \pm} \mathcal{P}_{n}^{ \pm}\left(\Omega \mp n \Omega_{L}\right),\qquad(51)
$$
where $P_{n}^{ \pm}(\Omega)$ are even functions peaked at zero and we neglect the peak at zero frequency. The explicit expressions for them are given in Appendix C. An example of the Raman spectrum is shown in Fig. 2 by the green line.

![](./images/812602988592889857_3.jpg)

FIG. 2. The noise spectrum of Faraday rotation, $S_{FR}(\Omega)$, (black line), and multispin flip Raman spectra $S_{xx}(\Omega)$ (blue line with filling), $S_{xy}(\Omega)$ (red line with filling), and $S_{++}(\Omega)$ (green line), calculated after Eqs. (51), (60), and (61). The yellow stripe covers the zero frequency peak, which does not carry information about the spin dynamics. The parameters of the calculation are $T = 0$, $\sqrt{N}\omega_{ex}/\gamma \gg 1$, and $\tau_{s}\Omega_{L}=20$. The peaks correspond to the multiple flips of Mn$^{2+}$ spins (magenta arrows in the sketch) mediated by the exchange interaction with the heavy hole spin (red arrow) in the exciton localization area (green).

In the illustrative case of $m(t)\ll 1$ one can substitute Eq. (48) in the asymptotic Eq. (36), which yields

$$
S_{++}(\Omega)=\sum_{n=1}^{\infty} \sum_{\pm} \frac{(2 n-1)!!}{2^{n}} \mu_{\pm}^{n} \frac{\tau_{s} / n}{1+\left[(\Omega / n \mp \Omega_{L}) \tau_{s}\right]^{2}}.
\tag{52}
$$

One can see that the spectrum consists of Lorentzian peaks at the frequencies $\mp n\Omega_{L}$ with the areas (divided by $2\pi$)

$$
A_{n}^{\pm}=\frac{(2 n-1)!!}{2^{n+1}} \mu_{\pm}^{n}
\tag{53}
$$

and the widths $n/\tau_{s}$. We stress that the second-order spin correlation function (47) contains the spin precession frequencies $\pm\Omega_{L}$ only. Therefore the appearance of the overtones is a fingerprint of the contributions of the higher-order spin correlators.

For high-order contributions, $n\gg 1$, Eq. (52) diverges, and the above analysis is inapplicable. Generally, one has to start from Eq. (33), where

$$
\Delta m^{2}(\tau)=\sum_{\pm} \mu_{\pm}\left(1-e^{\mp i \Omega_{L} \tau} e^{-|\tau| / \tau_{s}}\right)
\tag{54}
$$

according to Eq. (48). Thus we obtain

$$
\begin{aligned}
\overline{\left\langle p_{+}^{*}(0) p_{+}(\tau)\right\rangle}=& \int_{0}^{\infty} e^{-2 k} e^{-k^{2}\left(\mu_{+}+\mu_{-}\right)} \\
& \times \exp \left[k^{2}\left(\mu_{+} e^{-i \Omega_{L} \tau}+\mu_{-} e^{i \Omega_{L} \tau}\right) e^{-|\tau| / \tau_{s}}\right] d k.
\end{aligned}
\tag{55}
$$

The exponential in the second line can be expanded in the Taylor series as

$$
\begin{aligned}
\overline{\left\langle p_{+}^{*}(0) p_{+}(\tau)\right\rangle}=& \int_{0}^{\infty} e^{-2 k} e^{-k^{2}\left(\mu_{+}+\mu_{-}\right)} \\
& \times \sum_{n=0}^{\infty} \frac{k^{2 n}}{n!}\left(\mu_{+} e^{-i \Omega_{L} \tau}+\mu_{-} e^{i \Omega_{L} \tau}\right)^{n} e^{-n|\tau| / \tau_{s}} d k.
\end{aligned}
\tag{56}
$$

Again the correlation function contains harmonics $\propto e^{\mp i n \Omega_{L} \tau}$, so the spectrum consists of the peaks at the frequencies $\pm n\Omega_{L}$. Similarly, we expect that the high harmonics can be observed in the pump-probe experiments.

One general property follows from the ratio of prefactors in Eq. (48). From the definition (41) (without symmetrization) one can see that

$$
\frac{\left\langle I_{z}^{2}\right\rangle_{\Omega_{L}}}{\left\langle I_{z}^{2}\right\rangle_{-\Omega_{L}}}=e^{-\hbar \Omega_{L} /\left(k_{B} T\right)}.
\tag{57}
$$

Generally, this relation is inherited by the polarization spectra [Eq. (50)] in the form

$$
\frac{S_{++}(\Omega)}{S_{++}(-\Omega)}=e^{-\hbar \Omega /\left(k_{B} T\right)},
\tag{58}
$$

which is well known for the Raman spectra.

The Raman spin flip spectra in $\sigma^{+}$ and in $\sigma^{-}$ polarizations coincide and are given by Eq. (51):

$$
S_{--}(\Omega)=S_{++}(\Omega).
\tag{59}
$$

We recall that the two circular polarizations are independent in the lowest order in the incident electric field, so the cross-polarized spectra in circular polarizations vanish: $S_{\pm \mp}(\Omega)=0$.

The Raman spin flip spectra in linear polarizations and Faraday rotation and ellipticity noise spectra can be calculated using Eqs. (39) and (43) for the adiabatic regime. Similarly to Eq. (51) the Raman spectra take the form

$$
S_{x x}(\Omega)=S_{y y}(\Omega)=\sum_{k=1}^{\infty} \sum_{\pm} \mathcal{P}_{2 k}^{ \pm}\left(\Omega \mp 2 k \Omega_{L}\right),
\tag{60a}
$$

$$
S_{x y}(\Omega)=S_{y x}(\Omega)=\sum_{k=0}^{\infty} \sum_{\pm} \mathcal{P}_{2 k+1}^{ \pm}\left(\Omega \mp(2 k+1) \Omega_{L}\right).
\tag{60b}
$$

The Faraday rotation (and ellipticity) noise spectra are given by

$$
S_{F R}(\Omega)=\frac{S_{x y}(\Omega)+S_{x y}(-\Omega)}{2}
\tag{61}
$$

[see Eq. (43)], which differs from $\overline{\left\langle\theta_{F}^{2}\right\rangle}_{\Omega}$ (and $\overline{\left\langle\theta_{E}^{2}\right\rangle}_{\Omega}$) by a factor.

In Fig. 2, we compare the different spectra in the limit of zero temperature $T=0$ and strong exchange interaction $\sqrt{N}\omega_{ex}\gg\gamma$. All the spectra show the comb of peaks at frequencies, which are multiples of the Larmor spin precession frequency. The peaks in the Raman spectra correspond to the multiple spin flips mediated by the excitonic state, as shown in the top of the figure. Importantly, multiple spin flips take place in one process due to the RKKY-type exchange

interaction between $Mn^{2+}$ spins mediated by the heavy hole spin. The same mechanism can also lead to the double spin flips of donor bound electrons [32] and of electrons confined in the nanoplatelets [33]. In the Faraday rotation noise spectra, the peaks at frequencies $\pm n\Omega_{L}$ reflect the contributions of quantum spin noise correlation functions of the order $2n$. We recall that the average spin polarization along $z$ axis is absent, so the correlators of the odd orders vanish.

In the limit of zero temperature the spectrum contains the Stokes components only. In this limit $\mu_{+}=0$ and $A_{n}^{-}$ decay very slowly obeying the power law:
$$
A_{n}^{-} \propto 1/\sqrt{n}. \tag{62}
$$

The Raman spin flip spectra in Fig. 2 are asymmetric (contain only the peaks at negative frequencies) because the energy can not be absorbed from the zero-point spin fluctuations. Alternatively one can say that the $Mn^{2+}$ spins are all oriented along $x$ axis and can be flipped only in the opposite direction. The Raman spectra in linear polarizations are similar, but co-polarized (blue curve) and cross-polarized (red curve) spectra consist of the peaks at even and odd frequencies only, respectively, see Eqs. (60). In the same time, the Faraday rotation noise spectrum (black curve) is symmetric and contains the odd peaks only, as it follows from Eq. (61).

In the limit of zero temperature, the expressions for the spectra are particularly simple even beyond the adiabatic approximation. From the spin correlation function (48) and Eqs. (B8) we find the areas of the peaks in the form [18,21,22]
$$
A_{n}^{-}=\frac{1}{2 \tau_{0}} \int_{0}^{\infty} e^{-t / \tau_{0}} \frac{\Delta I_{x}^{n}(t)}{n!} e^{-\Delta I_{x}(t)} d t. \tag{63}
$$

Here we introduced the notations $t=k/\gamma$, $\tau_{0}=1/(2\gamma)$ and $^{2}$
$$
\Delta I_{x}(t)=I \frac{\omega_{e x}^{2}}{\Omega_{\text {tot }}^{2}}\left[1-\cos \left(\Omega_{\text {tot }} t\right)\right] \tag{64}
$$
with $I=Ns$ and $\Omega_{\text {tot }}=\sqrt{\omega_{e x}^{2}+\Omega_{L}^{2}}$. Physically, $\Delta I_{x}(t)$ is the change of $I_{x}$ during the spin precession in the sum of the exchange and external magnetic fields for the time $t$. The integrand in Eq. (63) has a form of the probability of the change of $I_{x}$ by $n$ in the Poisson distribution with the average $\Delta I_{x}(t)$. The integration describes the average of this probability during the exponential exciton decay described by $e^{-t/\tau_{0}}$. Thus, in this particular case, we have arrived to the expression obtained in Refs. [21,22] in the model of scattering via virtual magnetic polaron states.

Figure 3 shows the spectra for different temperatures, or equivalently for different magnetic fields. For better visibility, we focus on the Raman spectrum $S_{++}(\Omega)$, while the Faraday rotation noise spectrum can be obtained by selecting the odd numbered peaks and symmetrizing them in frequency, see Eq. (61). At high temperature (red curve), the spectrum is symmetric, which corresponds to purely thermal spin fluctuations. In the limit $\omega_{ex}\sqrt{N}\gg\gamma$, the peaks are very broad and strongly overlap. At high frequencies, the spectrum is described by
$$
S_{++}(\Omega)=\frac{\pi \gamma}{\omega_{\mathrm{ex}}} \sqrt{\frac{3 \tau_{s}}{2 N s(s+1)|\Omega|}}. \tag{65}
$$

![](./images/812602988592889857_4.jpg)

FIG. 3. Circular dipole polarization noise spectra, $S_{++}(\Omega)$, calculated after Eq. (51) in the limit of strong exchange interaction $(\sqrt{N}\omega_{ex}/\gamma\gg1)$ for $\tau_{s}\Omega_{L}=20$ and for different temperatures, as indicated in the plot.

The fact that $S_{++}(\Omega)$ decreases with increase of $\omega_{\text{ex}}$ is caused by the large splitting of the two excitonic resonances in this limit and a small range of values of $\delta I_{z}$, which produce sizable Faraday rotation, see Eq. (21). With decrease of the temperature the spectrum becomes asymmetric, which evidences the increasing role of noncommutativity of spin components.

Observation of high-order spin correlators is possible due to the nonlinear relation between dipole polarization and the total $Mn^{2+}$ spin. Similarly, noise of the linear birefringence was recently shown to produce the peak at the double Larmor frequency for cesium atoms [34]. Additional satellite lines in the spin noise spectra can also appear under the $ac$ driving of the system [35–38]. Here by contrast we consider the static magnetic field only.

### C. Favorable conditions for the measurement of the high-order correlators

To successfully apply the resonance shift spin noise spectroscopy the exchange interaction should be quite strong. Indeed, in the opposite limit of weak interaction, $\mu_{\pm}\ll1$, the area of the $n$-th peak is given by Eq. (53) and is proportional to $\omega_{\text{ex}}^{2n}$. Therefore the exchange interaction should be strong, which is easily realized in semimagnetic semiconductors and many other systems, see Sec. VII.

Experimentally, it is easier to measure the Faraday rotation noise spectra in the sub-GHz frequency range, which corresponds to the weak magnetic fields $B\lesssim40$ mT. In this case, the average spin polarization is small, and we find from Eq. (48) the dimensionless spin correlation function
$$
\langle m(0)m(\tau)\rangle=\frac{35N\omega_{\text{ex}}^{2}}{12\gamma^{2}}\cos(\Omega_{L}\tau)e^{-|\tau|/\tau_{s}}. \tag{66}
$$

$^{2}$The integral in Eq. (63) converges at $\Delta I_{x}(t)\lesssim1$. Since $N\gg1$ one has either $\omega_{ex}\ll\Omega_{L}$ or $\Omega_{L}t\ll1$, so one can replace $\Omega_{\text{tot}}$ with $\Omega_{L}$ and find $\Delta I_{x}(t)=\langle\mathcal{J}^{2}(0)\rangle_{s}$.

235416-8

![](./images/812602988592889857_5.jpg)

FIG. 4. Faraday rotation noise spectra calculated after Eq. (C3) for the typical experimental parameters: $T=2$ K, $N=50$, $B_{\text{exch}}=\hbar\omega_{\text{ex}}/(\mu_B g)=1.5$ T with $g=2$, $\hbar\gamma=0.33$ meV, and $\Omega_L\tau_s=20$. The black and red curves correspond to the strong ($B=6$ T, $\Omega_L/(2\pi)=168$ GHz) and moderate ($B=40$ mT, $\Omega_L/(2\pi)=1.1$ GHz) external magnetic field, respectively. The inset compares Gaussian noise spectrum (black curve) with the Faraday rotation noise for a single spin $I=1/2$ (blue curve) and $I=5/2$ (magenta curve) in the limit $T\rightarrow0$ and $\omega_{\text{ex}}\rightarrow\infty$ for $\Omega_L\tau_s=30$.

The areas of the peaks decay quickly in this limit even despite the strong exchange interaction. The Faraday rotation noise spectrum for the typical experimental conditions for $B=40$ mT is shown in Fig. 4 by red curve. One can see that the peak at the frequency $3\Omega_L$ is much smaller, than the peak at $\Omega_L$, and the peak at $5\Omega_L$ is hardly visible in this limit.

More favorable conditions for the measurement of the high-order spin correlations are realized in strong magnetic fields, when the spin polarization is large, but the adiabatic approximation can be violated in this case. The spin noise spectrum for $B=6$ T is shown by the blue curve in Fig. 4, where one can distinctly see many peaks at the odd multiples of $\Omega_L$. In this case, we obtain from Eq. (48)

$$
\langle m(0)m(\tau)\rangle=\frac{5N\omega_{\text{ex}}^2}{4\gamma^2}e^{i\Omega_L\tau}e^{-|\tau|/\tau_s}.\tag{67}
$$

The areas of the peaks decay slowly in this case as described by Eq. (62). This limit corresponds to the dominance of the quantum spin fluctuations over the classical ones, and was not reached nor approached yet. To measure the Faraday rotation noise in the high frequency range one has to use special techniques, such as pulse trains [39] or heterodyne detection [40]. Nevertheless, we believe that this experimental challenge will be dealt with in the nearest future.

## VI. NON-GAUSSIAN SPIN NOISE

In the previous sections, we described the Faraday rotation noise spectra, and demonstrated that they give access to the high-order quantum spin correlation functions. However, under the assumption of many independent $\text{Mn}^{2+}$ spins in the exciton localization volume, the high-order spin correlation functions all can be reduced to the second-order correlator. So it is interesting to go beyond this approximation and to study the non-Gaussian spin noise.

Generally, the noise spectrum is defined by Eq. (11), where the Faraday rotation and the ellipticity angles are related to the exciton polarization by Eq. (10). Using the averaged polarization correlation function (43) we find the Faraday rotation noise spectrum in the form

$$
S_{FR}(\Omega)=\int_{-\infty}^{\infty}\overline{\langle p_y^{*}(0)p_y(\tau)\rangle}_s e^{i\Omega\tau}d\tau,\tag{68}
$$

where the dimensionless polarization is given by Eq. (37b). In the adiabatic approximation, $\Omega_L\ll\gamma$, using the definition (28), we obtain

$$
p_y(t)=-\int_{0}^{\infty}e^{-i\delta k-k}M(t)dk,\tag{69}
$$

where we introduced the operator

$$
M(t)=\sin[km(t)].\tag{70}
$$

Then we perform averaging over the detuning, as defined in Eq. (30) and obtain the spectrum

$$
S_{FR}(\Omega)=\int_{-\infty}^{\infty}d\tau e^{i\Omega\tau}\int_{0}^{\infty}dke^{-2k}\langle M(0)M(\tau)\rangle_s.\tag{71}
$$

For non-Gaussian spin noise, the cumulants of $m(0)$ and $m(t)$ allow one to calculate this correlation function similarly to Appendix B.

For example, in the presence of the resident charge carriers, $\text{Mn}^{2+}$ spins are coupled with the carrier-mediated exchange RKKY interaction, which may eventually lead to the transition into the ferromagnetic phase [41]. For the $\text{Mn}^{2+}$ concentration approaching the paramagnetic-ferromagnetic transition, their spins are no longer independent, and the spin noise in non-Gaussian. The spin fluctuations in this case can be described theoretically using the Landau theory [42,43], effective polaron Hamiltonian [44,45], dynamical mean field theory [46,47], or using more sophisticated approaches [48,49]. In the vicinity of the phase transition the effective Larmor frequency decreases [50] and role of higher-order cumulants increases [51].

However, in view of the application of the resonance shift spin noise spectroscopy to other systems we consider another situation. Namely, let us study the Faraday rotation noise induced by a single spin $\boldsymbol{I}$ ($N=1$) coupled to the optical resonance. In this case, all the cumulants are equally important [see Eq. (B5)], so that the spin noise is strongly non-Gaussian. This limit can be realized, e.g., for deep impurities or atomic systems, see the next section.

For a single spin, it is easier to calculate the Faraday rotation noise spectrum directly using the spin density matrix formalism, than using the cumulant expansion. We find the operator $M(t)$ from the equation of motion

$$
\frac{dM(\tau)}{d\tau}=\frac{i}{\hbar}[\mathcal{H}_0,M(\tau)]+\mathcal{L}\{M(\tau)\},\tag{72}
$$

where $\mathcal{H}_0$ is defined in Eq. (16) and $\mathcal{L}$ is the Lindblad operator, describing the spin relaxation. Provided the transverse spin relaxation time $\tau_s$ is much shorter than the longitudinal one

$(T_1)$, we write the Lindblad operator in the form
$$
\mathcal{L}\{M(\tau)\}=\frac{1}{\tau_{s}}\left[2 I_{x} M(\tau) I_{x}-I_{x}^{2} M(\tau)-M(\tau) I_{x}^{2}\right]. \quad(73)
$$

For the strong probe light (in higher orders in $E_0$), the quantum back action should be taken into account by the additional term $\lambda/2[I_z,[I_z,M(\tau)]]$, where $\lambda$ describes the strength of the measurements [52,53]. This allows one to describe the quantum Zeno effect [54,55] and to trace the transition to the telegraph spin noise with increase of the intensity of the probe light.

The kinetic equation has a trivial initial condition $M(0) = \sin(km)$, where $m$ is the Schrodinger operator defined in Eq. (29). Finally, the correlation function in Eq. (71) should be calculated using the steady-state density matrix
$$
\rho=e^{-\mathcal{H}_{0} /\left(k_{B} T\right)} / \operatorname{Tr}\left(e^{-\mathcal{H}_{0} /\left(k_{B} T\right)}\right). \quad(74)
$$

As an example, let us consider $I=1/2$. In this case,
$$
\sin (k m)=2 \sin \left(\frac{k \omega_{\mathrm{ex}}}{2 \gamma}\right) I_{z}. \quad(75)
$$

Then the solution of Eq. (72) simply reads
$$
M(\tau)=2 \sin \left(\frac{k \omega_{\mathrm{ex}}}{2 \gamma}\right)\left[I_{z} \cos \left(\Omega_{L} \tau\right)+I_{y} \sin \left(\Omega_{L} \tau\right)\right] e^{-\tau / \tau_{s}}.
$$

For any temperature, the correlation function is the same:
$$
\langle M(0) M(\tau)\rangle_{s}=\sin ^{2}\left(\frac{k \omega_{\mathrm{ex}}}{2 \gamma}\right) \cos \left(\Omega_{L} \tau\right) e^{-|\tau| / \tau_{s}}. \quad(77)
$$

Substituting this function in Eq. (71), we find the non-Gaussian Faraday rotation noise spectrum for $I=1/2$:
$$
S_{\mathrm{FR}}(\Omega)=\frac{1}{8} \frac{\omega_{\mathrm{ex}}^{2}}{\omega_{\mathrm{ex}}^{2}+4 \gamma^{2}}\left[\mathcal{P}_{1}(\Omega)+\mathcal{P}_{1}(-\Omega)\right]. \quad(78)
$$

This spectrum is shown by the blue curve in the Fig. 4. Here the main difference with the normal spin noise is the appearance of the peaks at the frequencies $\pm\Omega_L$ only instead of the comb of the peaks. Note that the shape of the spectrum in this case formally coincides with the spectrum of spin fluctuations [Eq. (41)], which is usually measured by the Pauli-blocking spin noise spectroscopy.

For larger $I$, $\sin(km)$ can be presented as a linear combination of the operators $I_z^n$ with odd $n\leqslant 2I$. As a result, the high-order spin correlators can be reduced to a few lower orders, and the spectrum consists of a finite number of peaks. The maximum number is $n_{\text{max}}=2[I-1/2]+1$, where square brackets denote the integer part. Similarly, in the multispin flip Raman spectra in circular polarization the maximum number of peaks is $2I$, which corresponds to the fact that a single spin can not be flipped more than $2I$ times in one direction.

The Faraday rotation noise spectrum for a single spin $I=5/2$ (in the limit $T=0$) is shown in the inset in Fig. 4 by a magenta curve. One can see that the frequency of the last peak is $5\Omega_L$, and the peaks are much broader, than for the Gaussian spin noise. This indicates that the higher-order spin correlators generally contain more information than the second-order one.

## VII. DISCUSSION AND CONCLUSION

In the heterostructures with the resident charge carriers, the Faraday rotation noise spectra can contain the two contributions provided by the Pauli-blocking and optical resonance shift mechanisms, which originate from charge carrier spins and spins of magnetic impurities (or nuclei), respectively. Typically, the corresponding effective $g$ factors are different, and therefore these contributions are separated in the frequency domain. In the same way, the contributions of these two mechanisms to the Raman spin flip spectra can be separated [19]. Moreover, if the inhomogeneous broadening is smaller, than the homogeneous one, the Pauli-blocking and resonance shift contributions can be distinguished by their dependence on the optical frequency of the probe light, $\omega_0$. This approach is known as the optical spectroscopy of spin noise [56] and was used to separate the spin and charge related contributions to the Faraday rotation noise spectra for a single QD [57,58]. For example, in the case of Pauli-blocking mechanism, the power of Faraday rotation noise reaches its minimum exactly at the optical resonance [56], while in case of the resonance-shift mechanism it should have a maximum (the ellipticity noise demonstrates the opposite behavior).

To detect the higher-order spin correlators, the ratio between the exchange broadening of the exciton resonance $\sqrt{N}\omega_{\text{ex}}$ should be comparable to or larger than the homogeneous linewidth $\gamma$, as discussed in Sec. V C. This condition is easily satisfied in Mn-doped QWs [18] and QDs [20], where up to 15 peaks in the Raman spin flip spectra are visible. For these structures $\sqrt{N}\hbar\omega_{\text{ex}}\sim 2$ meV and $\hbar\gamma\sim 1$ meV.

For Mn-doped nanosystems, the number of the probed spins is typically very large $N\gtrsim 100$, and the total spin noise is almost Gaussian. However with increase of the $\text{Mn}^{2+}$ concentration a limited number of closely located pairs of magnetic atoms appears. The strength of the exchange interaction in a pair can be of the order of 0.5 meV [59–61], and the ground state of the pair is the singlet spin state. The difference between the interaction constants with the heavy hole in the localized exciton for the two spins in a pair leads to the mixing between singlet and triplet states. We expect that it will manifest itself as another comb of peaks with the frequencies a bit larger than $n\Omega_L$ in Faraday rotation noise spectrum. Due to the small number of pairs their contribution is non-Gaussian, and therefore contains detailed information about the spin dynamics of the pair of strongly coupled spins.

Importantly, the resonance shift quantum spin noise spectroscopy can be applied to a very broad class of spin systems. For example, it can be applied to measure the nuclear spin fluctuations in QDs. In this case the main requirement for the detection of high-order spin correlators is the sizable hyperfine interaction strength as compared with the inverse lifetime of the excited state. For example, in GaAs-based QDs the hyperfine interaction constant for electrons is $A\approx 100$ $\mu$eV [17,62,63], so for small QDs with $N\sim 10^4$ one has $\sqrt{N}\hbar\omega_{\text{ex}}\sim A/\sqrt{N}\sim 1$ $\mu$eV, which is the typical exciton homogeneous linewidth [64]. Thus we expect that the higher-order nuclear spin correlators can be measured for small QDs as well as for the small colloidal nanocrystals.

Resonance shift spin noise spectroscopy is particularly useful, when the number of probed spins is small, because in this

case the high-order spin correlators can not be reduced to the lower orders. To measure these correlation functions, the spin-related (e.g., hyperfine) structure of individual optical transitions should be visible. There are many examples of such systems: For NV⁻ centers in diamond, the hyperfine interaction constant with the nearest C¹³ atom can reach 0.1 μeV [65], which is approximately two times larger, than the homogeneous linewidth at liquid helium temperatures [66]. For rare earth ions, A can reach 10 μeV, while the homogeneous linewidth is a few times smaller [67]. In the past few years the van der Waals heterostructures are under intense investigation. For localized spatially indirect excitons, the hyperfine interaction induced spin relaxation time is predicted to be $T_{2}^{*} \sim 1 /(\sqrt{N} \omega_{\text {ex }}) \sim 1$ ns [68,69], which is an order of magnitude shorter, than the exciton lifetime $1 / \gamma=10$ ns [70], so that the nuclear related broadening of the optical transition exceeds its linewidth by an order of magnitude. The similar situation is realized for the lead halide perovskites where $T_{2}^{*}$ is comparable with $1 / \gamma$ [71]. So, these systems can be efficiently studied with the resonance shift nuclear spin noise spectroscopy. Apart from the solid state physics, the hyperfine structure of optical transitions is quite routinely observed for atoms, such as K, Na, Rb, Cs; and for simple molecules, such as I₂ [72]. Therefore these systems are also promising for the resonance shift spin noise spectroscopy.

In conclusion, we have developed a theory of a class of optical phenomena that occur in optically transparent solids with localized spins (e.g., Mn²⁺ spins in diluted magnetic semiconductors), forming a basis for a set of experimental methods, which can be generically called resonance shift spin noise spectroscopy. The distinctive feature of these phenomena is that the spins do not directly participate in the probed optical transitions (e.g., excitonic ones), but they shift such transitions via the spin-spin interactions. To demonstrate the universality and power of this approach, we obtained the expressions for multispin flip Raman spectra in dilutedmagnetic quantum wells and calculated the Faraday rotation noise spectra. We predict multiple overtones of the Larmor frequency in the spectra, which reflect the contributions of the high-order correlation functions of the spin fluctuations. Our predictions open a way for the experimental investigation of high-order spin noise, including quantum noise. Our approach is directly extendable to a wide range of solid-state and atomic systems.

## ACKNOWLEDGMENTS
We gratefully acknowledge the fruitful discussions with M. M. Glazov and D. Scalbert and the partial financial support by the RF President Grant No. MK-1576.2019.2 and the Basis Foundation. K.V.K. was supported by a grant No. 51125686 from Saint-Petersburg State University and by the Russian Science Foundation Grant No. 19-52-12054. The calculations of the Faraday rotation noise spectra by D.S.S. were supported by the Russian Science Foundation Grant No. 19-72-00081.

## APPENDIX A: CALCULATION OF THE POLARIZATION
We start from the general form of the Hamiltonian (1). Its Hilbert space is a direct product of the states of the spin system and the excitonic states including exciton vacuum state. For heavy hole excitons there are four states, which can be labeled by the electron spin projection $S_{z}^{e}= \pm 1 / 2$ and the hole spin $S_{z}^{h}= \pm 3 / 2$. The excitonic states can be denoted as $|k\rangle$, where $k=1,2, \ldots$ In the first order in the incident field amplitude, one can consider a single exciton states only, so the exciton Hamiltonian has the form

$$
\mathcal{H}_{\mathrm{exc}}=\sum_{k} \mathcal{H}_{\mathrm{exc}}^{k^{\prime} k} c_{k^{\prime}}^{\dagger} c_{k}, \quad \text { (A1) }
$$

where $c_{k}$ ($c_{k}^{\dagger}$) are the annihilation (creation) operators for the states $|k\rangle$. This Hamiltonian describes the fine structure of the excitonic levels and exciton interaction with the external magnetic field.

The coherent exciton generation is described by Eq. (2), where

$$
\boldsymbol{P}=\sum_{k} \boldsymbol{d}_{k} c_{k} \quad \text { (A2) }
$$

with $\boldsymbol{d}_{k}$ being the dipole moments of the excitonic states. In the particular model, which is used in the derivation of Eq. (20), there are two excitonic states with the dipole moments $\boldsymbol{d}_{ \pm}=d\left(-\boldsymbol{e}_{x} \mp i \boldsymbol{e}_{y}\right) / \sqrt{2}$, where $\boldsymbol{e}_{\alpha}$ are the unit vectors along the corresponding axes.

The Hamiltonian $\mathcal{H}_{0}$ describes the magnetic spin system only and does not contain operators $c_{k}$ and $c_{k}^{\dagger}$. Moreover, the Hamiltonian of the spin-exciton exchange interaction has the form

$$
\mathcal{H}_{\mathrm{int}}=\sum_{k, k^{\prime}, i} \boldsymbol{I}_{i} \mathcal{H}_{\mathrm{int}}^{k k^{\prime}} c_{k}^{\dagger} c_{k^{\prime}}. \quad \text { (A3) }
$$

Note that this Hamiltonian contains off diagonal terms (with $k \neq k^{\prime}$) and coincides with Eq. (15).

The operator of the system evolution is

$$
U=\mathcal{T} \exp \left[-\frac{i}{\hbar} \int_{0}^{t} \mathcal{H}\left(t^{\prime}\right) d t^{\prime}\right], \quad \text { (A4) }
$$

and the Heisenberg polarization operator is

$$
\boldsymbol{P}^{(0)}(t)=U^{\dagger} \boldsymbol{P} U. \quad \text { (A5) }
$$

We are interested in the contribution $\boldsymbol{P}(t)$ to $\boldsymbol{P}^{(0)}(t)$ only, which is linear in the amplitude of the probe light $\boldsymbol{E}$. This operator acts only in the Hilbert space of the exciton vacuum state, so it is given by

$$
\boldsymbol{P}(t)=e^{\frac{i}{\hbar} \mathcal{H}_{0} t} \boldsymbol{P} \int_{0}^{t} e^{-\frac{i}{\hbar}\left(\mathcal{H}_{0}+\mathcal{H}_{\mathrm{exc}}+\mathcal{H}_{\mathrm{int}}\right) \tau} \frac{i}{\hbar}\left(\boldsymbol{P}^{\dagger} \boldsymbol{E}\right) e^{-\frac{i}{\hbar} \mathcal{H}_{0}(t-\tau)} d \tau.
$$

Since the spin Hamiltonian $\mathcal{H}_{0}$ commutes with $\boldsymbol{P}$, this expression can be written as

$$
\boldsymbol{P}(t)=\frac{i}{\hbar} \boldsymbol{P} \int_{0}^{t} \Phi(t, \tau) d \tau\left(\boldsymbol{P}^{\dagger} \boldsymbol{E}\right), \quad \text { (A7) }
$$

where

$$
\Phi(t, \tau)=e^{\frac{i}{\hbar} \mathcal{H}_{0} t} e^{-\frac{i}{\hbar}\left(\mathcal{H}_{0}+\mathcal{H}_{\mathrm{exc}}+\mathcal{H}_{\mathrm{int}}\right) \tau} e^{-\frac{i}{\hbar} \mathcal{H}_{0}(t-\tau)}. \quad \text { (A8) }
$$

To simplify this expression, we note that

$$
\frac{\partial \Phi(t, \tau)}{\partial \tau}=-\frac{i}{\hbar} \Phi(t, \tau)\left[\mathcal{H}_{\mathrm{exc}}+\tilde{\mathcal{H}}_{\mathrm{int}}(t-\tau)\right] \quad \text { (A9) }
$$


with $\tilde{\mathcal{H}}_{\text{int}}(t)$ given by Eq. (4). One can readily see that $\Phi(t,0)=1$, so the solution of this equation is
$$
\Phi(t, \tau)=\mathcal{T} \exp \left\{-\frac{i}{\hbar} \int_{0}^{\tau}\left[\mathcal{H}_{\mathrm{exc}}+\tilde{\mathcal{H}}_{\mathrm{int}}\left(t-\tau^{\prime}\right)\right] d \tau^{\prime}\right\}.
\tag{A10}
$$

Substituting this expression in Eq. (A7) we see that $\boldsymbol{P}(t)=$ $\boldsymbol{P} \psi$, where
$$
\psi=\frac{i}{\hbar} \int_{0}^{t} \mathcal{T} \exp \left\{-\frac{i}{\hbar} \int_{0}^{\tau}\left[\mathcal{H}_{\mathrm{exc}}+\tilde{\mathcal{H}}_{\mathrm{int}}\left(t-\tau^{\prime}\right)\right] d \tau^{\prime}\right\} d \tau\left(\boldsymbol{P}^{\dagger} \boldsymbol{E}\right)
\tag{A11}
$$
in agreement with Eq. (5). One can readily check that it satisfies Eq. (3) indeed.

## APPENDIX B: CUMULANT EXPANSION

The generating function for the cumulants of $\mathcal{J}(0)$ and $\mathcal{J}(\tau)$ can be taken in the following form:
$$
\mathcal{K}=\ln \left\langle e^{i \alpha \mathcal{J}(0)-i \beta \mathcal{J}(\tau)}\right\rangle.
\tag{B1}
$$

Its Tailor series defines the cumulants $\kappa\left(\mathcal{J}^{l}(0), \mathcal{J}^{(n-l)}(\tau)\right)$ as
$$
\mathcal{K}=\sum_{n=1}^{\infty} \sum_{l=0}^{n}\left(\begin{array}{l}
n \\
l
\end{array}\right) \alpha^{l}(-\beta)^{n-l} \kappa\left(\mathcal{J}^{l}(0), \mathcal{J}^{(n-l)}(\tau)\right). \tag{B2}
$$

Comparing this expression with the correlator in Eq. (31), we find
$$
\begin{aligned}
& \left\langle\left[\overline{\mathcal{T}} e^{i \mathcal{J}(0)}\right]\left[\mathcal{T} e^{-i \mathcal{J}(\tau)}\right]\right\rangle \\
& \quad=\exp \left\{\sum_{n=1}^{\infty} \sum_{l=0}^{2 n} \frac{(-1)^{n+l}}{(2 n-l)! l!} \kappa\left(\mathcal{J}^{l}(0), \mathcal{J}^{(2 n-l)}(\tau)\right)\right\}, \text { (B3) }
\end{aligned}
$$
where we took into account that the cumulants of the odd orders vanish in the absence of the spin polarization along the $z$ axis $(\langle m(t)\rangle=0)$. The cumulants of the operators should be calculated using the normal time ordering for the powers of $\mathcal{J}(\tau)$, reverse time ordering for $\mathcal{J}(0)$ and putting $\mathcal{J}(0)$ always to the left of $\mathcal{J}(\tau)$.

To simplify the following, we assume that the $\mathrm{Mn}^{2+}$ spins, $\boldsymbol{I}_{i}$ in Eq. (17), are independent. In this case $\mathcal{J}(t)$, as defined in Eq. (28) also consists of $N$ independent contributions $\mathcal{J}_{i}(t) \propto$ $1 / N$. Then a cumulant of the sum of independent variables takes the form [31]
$$
\kappa\left(\mathcal{J}^{l}(0), \mathcal{J}^{(2 n-l)}(\tau)\right)=\sum_{i=1}^{N} \kappa\left(\mathcal{J}_{i}^{l}(0), \mathcal{J}_{i}^{(2 n-l)}(\tau)\right). \quad(\mathrm{B} 4)
$$

From this relation one can see the scaling law for the cumulants
$$
\kappa\left(\mathcal{J}^{l}(0), \mathcal{J}^{(2 n-l)}(\tau)\right) \propto 1 / N^{2 n-1}. \tag{B5}
$$

The larger is $N$ the less important are the cumulants of the high orders.

In the limit of many independent $\mathrm{Mn}^{2+}$ spins, $N \gg 1$, one can neglect all the cumulants except for $n=1$ (the second-order one). This corresponds to the normal or Gaussian spin noise. In this case Eq. (B3) reduces to
$$
\left\langle\overline{\mathcal{T}} e^{i \mathcal{J}(0)} \mathcal{T} e^{-i \mathcal{J}(\tau)}\right\rangle=\exp \left(\langle\mathcal{J}(0) \mathcal{J}(\tau)\rangle-\left\langle\mathcal{J}^{2}(0)\right\rangle_{s}\right), \quad(\mathrm{B} 6)
$$
and from Eq. (31), we obtain
$$
\overline{\left\langle p_{+}^{*}(0) p_{+}(\tau)\right\rangle}=\int_{0}^{\infty} e^{-2 k+\langle\mathcal{J}(0) \mathcal{J}(\tau)\rangle-\left\langle\mathcal{J}^{2}(0)\right\rangle_{s}} d k. \quad \text { (B7) }
$$

The second-order correlator of $\mathcal{J}(t)$ can be presented as a double integral using its definition (28). The correlation function $\langle m(t_{1}) m(t_{2})\rangle$ depends on $t_{1}-t_{2}$ only, so the double integral can be reduced to a single integral as follows:
$$
\langle\mathcal{J}(0) \mathcal{J}(\tau)\rangle=\int_{-k}^{k}\left(k-\left|k^{\prime}\right|\right)\langle m(0) m(\tau+k^{\prime} / \gamma)\rangle d k^{\prime}, \quad(\mathrm{B} 8 \mathrm{a})
$$

$$
\left\langle\mathcal{J}^{2}(0)\right\rangle_{s}=2 \int_{0}^{k}\left(k-k^{\prime}\right)\langle m(0) m\left(k^{\prime} / \gamma\right)\rangle_{s} d k^{\prime}. \quad(\mathrm{B} 8 \mathrm{~b})
$$

Substitution of these expressions in Eq. (B7) yields the polarization correlation function, which defines, for example, the Raman spin flip spectrum, see Eq. (50).

In order to describe the spectra beyond the adiabatic approximation in the zero temperature limit we use Eqs. (48) and (B8) to obtain
$$
\langle\mathcal{J}(0) \mathcal{J}(\tau)\rangle=\left\langle\mathcal{J}^{2}(0)\right\rangle_{s} e^{i \Omega_{L} \tau-|\tau| / \tau_{s}}, \quad \text { (B9a) }
$$

$$
\left\langle\mathcal{J}^{2}(0)\right\rangle_{s}=N s \frac{\omega_{\mathrm{ex}}^{2}}{\Omega_{L}^{2}}\left[1-\cos \left(\Omega_{L} k / \gamma\right)\right], \quad(\mathrm{B} 9 \mathrm{~b})
$$
where we took into account that $\tau_{s} \gamma \gg 1$. Substitution of these expressions in the polarization correlation function (B7) yields Eq. (63).

## APPENDIX C: SHAPE OF THE PEAKS

In the realistic limit $\tau_{s} \gamma \gg 1$ using Eq. (47), we obtain from Eq. (B8)
$$
\langle\mathcal{J}(0) \mathcal{J}(\tau)\rangle=\left(\mathcal{J}_{+} e^{-i \Omega_{L} \tau}+\mathcal{J}_{+} e^{i \Omega_{L} \tau}\right) e^{-|\tau| / \tau_{s}} \quad(\mathrm{C} 1)
$$
and $\langle\mathcal{J}^{2}(0)\rangle_{s}=\langle\mathcal{J}^{2}(0)\rangle$ with
$$
\mathcal{J}_{ \pm}=\frac{\omega_{\mathrm{ex}}^{2}}{\Omega_{L}^{2}}\left(\left\langle I_{z}^{2}\right\rangle \mp \frac{\left\langle I_{x}\right\rangle}{2}\right)\left[1-\cos \left(\frac{\Omega_{L}}{\gamma} k\right)\right]. \quad(\mathrm{C} 2)
$$

Substituting these expressions in Eq. (B7) and decomposing the exponent into series we find
$$
\begin{aligned}
\overline{\left\langle p_{+}^{*}(0) p_{+}(\tau)\right\rangle}= & \sum_{n=0}^{\infty} \sum_{l=0}^{n} \frac{e^{i(2 l-n) \Omega_{L} \tau-n|\tau| / \tau_{s}}}{l!(n+l)!} \\
& \times \int_{0}^{\infty} \mathcal{J}_{+}^{l} \mathcal{J}_{-}^{n-l} e^{-2 k-\mathcal{J}_{+}-\mathcal{J}_{-}} d k. \quad(\mathrm{C} 3)
\end{aligned}
$$

In the adiabatic approximation $\left(\Omega_{L} \ll \gamma\right)$, Eq. (C2) re- duces to $\mathcal{J}_{ \pm}=k^{2} \mu_{ \pm}$, so from Eq. (C3), we obtain
$$
\begin{aligned}
\overline{\left\langle p_{+}^{*}(0) p_{+}(\tau)\right\rangle}= & \sum_{n=0}^{\infty} \sum_{l=0}^{n} \frac{\mu_{+}^{l} \mu_{-}^{n-l}}{l!(n+l)!} e^{i(2 l-n) \Omega_{L} \tau-n|\tau| / \tau_{s}} \\
& \times \int_{0}^{\infty} e^{-2 k-k^{2}\left(\mu_{+}+\mu_{-}\right)} k^{2 n} d k. \quad(\mathrm{C} 4)
\end{aligned}
$$

In the next step, we introduce $n^{\prime}=n-2 l$ and $l^{\prime}=l$ for $n^{\prime} \geqslant 0$ and $l^{\prime}=n-l$ otherwise. Then we rewrite this

expression as
$$
\begin{aligned}
& \overline{\left\langle p_{+}^{*}(0) p_{+}(\tau)\right\rangle} \\
& \quad=\sum_{n^{\prime}=-\infty}^{\infty} \sum_{l^{\prime}=0}^{\infty} \frac{\mu_{\operatorname{sign}\left(n^{\prime}\right)}^{l^{\prime}} \mu_{-\operatorname{sign}\left(n^{\prime}\right)}^{\left|n^{\prime}\right|+l^{\prime}}}{l^{\prime}!\left(\left|n^{\prime}\right|+l^{\prime}\right)!} e^{-i n^{\prime} \Omega_{L} \tau-\left(\left|n^{\prime}\right|+2 l^{\prime}\right)|\tau| / \tau_{s}} \\
& \quad \times \int_{0}^{\infty} e^{-2 k-k^{2}\left(\mu_{+}+\mu_{-}\right)} k^{2\left(\left|n^{\prime}\right|+2 l^{\prime}\right)} d k,
\end{aligned}
$$
where we assume $\operatorname{sign}(0) \equiv 1$ to be specific. Finally, the Fourier transform of this expression [see Eq. (50)] yields
Eq. (51), where
$$
\begin{aligned}
\mathcal{P}_{n}^{ \pm}(\Omega)= & \sum_{l=0}^{\infty} \int_{0}^{\infty} e^{-2 k} e^{-k^{2}\left(\mu_{+}+\mu_{-}\right)} k^{2(n+2 l)} \\
& \times \frac{\mu_{ \pm}^{l} \mu_{\mp}^{n+l}}{l!(n+l)!} \frac{2 \tau_{s}(n+2 l)}{(n+2 l)^{2}+\left(\Omega \tau_{s}\right)^{2}} d k. \quad(\mathrm{C} 6)
\end{aligned}
$$

Here we omitted the primes for the brevity and neglected the terms with $n=0$.

[1] F. Bloch, Nuclear induction, *Phys. Rev.* **70**, 460 (1946).

[2] V. S. Zapasskii, Spin-noise spectroscopy: from proof of principle to applications, *Adv. Opt. Photonics* **5**, 131 (2013).

[3] J. Hübner, F. Berski, R. Dahbashi, and M. Oestreich, The rise of spin noise spectroscopy in semiconductors: From acoustic to GHz frequencies, *Phys. Status Solidi B* **251**, 1824 (2014).

[4] B. M. Gorbovitskii and V. I. Perel, Aleksandrov and Zapasskii experiment and the Raman effect, *Opt. Spectrosc.* **54**, 229 (1983).

[5] M. M. Glazov and V. S. Zapasskii, Linear optics, Raman scattering, and spin noise spectroscopy, *Opt. Express* **23**, 11713 (2015).

[6] E. L. Ivchenko, *Optical Spectroscopy of Semiconductor Nanostructures* (Alpha Science, Harrow UK, 2005).

[7] F. Li, S. A. Crooker, and N. A. Sinitsyn, Higher-order spin-noise spectroscopy of atomic spins in fluctuating external fields, *Phys. Rev. A* **93**, 033814 (2016).

[8] A. Bechtold, F. Li, K. Müller, T. Simmet, P.-L. Ardelt, J. J. Finley, and N. A. Sinitsyn, Quantum Effects in Higher-Order Correlators of a Quantum-Dot Spin Qubit, *Phys. Rev. Lett.* **117**, 027402 (2016).

[9] R.-B. Liu, S.-H. Fung, H.-K. Fung, A. N. Korotkov, and L. J. Sham, Dynamics revealed by correlations of time-distributed weak measurements of a single spin, *New J. Phys.* **12**, 013018 (2010).

[10] A. Bednorz, W. Belzig, and A. Nitzan, Nonclassical time correlation functions in continuous quantum measurement, *New J. Phys.* **14**, 013009 (2012).

[11] D. Hägele and F. Schefczik, Higher-order moments, cumulants, and spectra of continuous quantum noise measurements, *Phys. Rev. B* **98**, 205143 (2018).

[12] P. Schad, B. N. Narozhny, G. Schön, and A. Shnirman, Nonequilibrium spin noise and noise of susceptibility, *Phys. Rev. B* **90**, 205419 (2014).

[13] F. Li and N. A. Sinitsyn, Universality in Higher Order Spin Noise Spectroscopy, *Phys. Rev. Lett.* **116**, 026601 (2016).

[14] J. A. Gaj and J. Kossut, *Introduction to the Physics of Diluted Magnetic Semiconductors* (Springer Science & Business Media, 2011), Vol. 144 .

[15] S. Cronenberger, D. Scalbert, D. Ferrand, H. Boukari, and J. Cibert, Atomic-like spin noise in solid-state demonstrated with manganese in cadmium telluride, *Nat. Commun.* **6**, 8121 (2015).

[16] F. Berski, J. Hübner, M. Oestreich, A. Ludwig, A. D. Wieck, and M. M. Glazov, Interplay of Electron and Nuclear Spin Noise in $n$-Type GaAs, *Phys. Rev. Lett.* **115**, 176601 (2015).

[17] M. M. Glazov, *Electron and Nuclear Spin Dynamics in Semiconductor Nanostructures* (Oxford University Press, Oxford, 2018).

[18] J. Stühler, G. Schaack, M. Dahl, A. Waag, G. Landwehr, K. V. Kavokin, and I. A. Merkulov, Multiple $\mathrm{Mn}^{2+}$-Spin-Flip Raman Scattering at High Fields via Magnetic Polaron States in Semimagnetic Quantum Wells, *Phys. Rev. Lett.* **74**, 2567 (1995).

[19] J. M. Bao, A. V. Bragas, J. K. Furdyna, and R. Merlin, Control of spin dynamics with laser pulses: Generation of entangled states of donor-bound electrons in a $\mathrm{Cd}_{1-x} \mathrm{Mn}_{x}$ Te quantum well, *Phys. Rev. B* **71**, 045314 (2005).

[20] N. V. Kozyrev, R. R. Akhmadullin, B. R. Namozov, Yu. G. Kusrayev, I. V. Sedova, S. V. Sorokin, and S. V. Ivanov, Multiple spin-flip Raman scattering in CdSe/ZnMnSe quantum dots, *Phys. Rev. B* **99**, 035301 (2019).

[21] J. Stühler, G. Schaack, M. Dahl, A. Waag, G. Landwehr, K. V. Kavokin, and I. A. Merkulov, Polarization properties of multiple $\mathrm{Mn}^{2+}$-spin-flip Raman scattering in semimagnetic quantum wells, *J. Cryst. Growth* **159**, 1001 (1996).

[22] K. V. Kavokin and I. A. Merkulov, Multispin Raman paramagnetic resonance: Quantum dynamics of classically large angular momenta, *Phys. Rev. B* **55**, R7371 (1997).

[23] M. M. Glazov, Coherent spin dynamics of electrons and excitons in nanostructures (a review), *Phys. Solid State* **54**, 1 (2012).

[24] L. D. Landau and E. M. Lifshitz, *Quantum Mechanics: Nonrelativistic Theory*, Course of Theoretical Physics Vol. 3 (Butterworth-Heinemann, Oxford, 1977).

[25] A. A. Clerk, M. H. Devoret, S. M. Girvin, F. Marquardt, and R. J. Schoelkopf, Introduction to quantum noise, measurement, and amplification, *Rev. Mod. Phys.* **82**, 1155 (2010).

[26] D. S. Smirnov, B. Reznychenko, A. Auffèves, and L. Lanco, Measurement back action and spin noise spectroscopy in a charged cavity QED device in the strong coupling regime, *Phys. Rev. B* **96**, 165308 (2017).

[27] I. A. Merkulov and A. V. Rodina, Exchange interaction between carriers and magnetic ions in quantum size heterostructures, in *Introduction to the Physics of Diluted Magnetic Semiconductors* (Springer, Berlin, Heidelberg, 2010), p. 65.

[28] X. Marie, T. Amand, P. Le Jeune, M. Paillard, P. Renucci, L. E. Golub, V. D. Dymnikov, and E. L. Ivchenko, Hole spin quantum beats in quantum-well structures, *Phys. Rev. B* **60**, 5811 (1999).

[29] R. Kubo, Generalized Cumulant Expansion Method, *J. Phys. Soc. Jap.* **17**, 1100 (1962).
235416-13

[30] J. M. Mendel, Tutorial on higher-order statistics (spectra) in signal processing and system theory: theoretical results and some applications, *Proc. IEEE* **79**, 278 (1991).

[31] C. Gardiner, *Stochastic Methods* (Springer Berlin, 2009), Vol. 4.

[32] J. F. Scott and T. C. Damen, Anomalous Double Spin-Flip Raman Scattering in CdS, and a Visible Spin-Flip Laser, *Phys. Rev. Lett.* **29**, 107 (1972).

[33] D. Kudlacik, V. F. Sapega, D. R. Yakovlev, I. V. Kalitukha, E. V. Shornikova, A. V. Rodina, E. L. Ivchenko, G. S. Dimitriev, M. Nasilowski, B. Dubertret, and M. Bayer, Single and Double Electron Spin-Flip Raman Scattering in CdSe Colloidal Nanoplatelets, *Nano Lett.* **20**, 517 (2020).

[34] A. A. Fomin, M. Yu. Petrov, G. G. Kozlov, M. M. Glazov, I. I. Ryzhov, M. V. Balabas, and V. S. Zapasskii, Spin-alignment noise in atomic vapor, *Phys. Rev. Res.* **2**, 012008(R) (2020).

[35] M. Braun and J. König, Faraday-rotation fluctuation spectroscopy with static and oscillating magnetic fields, *Phys. Rev. B* **75**, 085310 (2007).

[36] P. Glasenapp, N. A. Sinitsyn, Luyi Yang, D. G. Rickel, D. Roy, A. Greilich, M. Bayer, and S. A. Crooker, Spin Noise Spectroscopy Beyond Thermal Equilibrium and Linear Response, *Phys. Rev. Lett.* **113**, 156601 (2014).

[37] Z. Yue and M. E. Raikh, Evolution of inhomogeneously broadened spin-noise spectrum with ac drive, *Phys. Rev. B* **91**, 155301 (2015).

[38] A. V. Poshakinskiy and S. A. Tarasenko, Spin noise at electron paramagnetic resonance, *Phys. Rev. B* **101**, 075403 (2020).

[39] F. Berski, H. Kuhn, Jan G. Lonnemann, J. Hübner, and M. Oestreich, Ultrahigh Bandwidth Spin Noise Spectroscopy: Detection of Large g-Factor Fluctuations in Highly-n-Doped GaAs, *Phys. Rev. Lett.* **111**, 186602 (2013).

[40] S. Cronenberger and D. Scalbert, Quantum limited heterodyne detection of spin noise, *Rev. Sci. Instrum.* **87**, 093111 (2016).

[41] T. Dietl, A. Haury, and Y. Merle d'Aubigne, Free carrier-induced ferromagnetism in structures of diluted magnetic semiconductors, *Phys. Rev. B* **55**, R3347 (1997).

[42] H. E. Stanley, *Phase Transitions and Critical Phenomena* (Clarendon Press, Oxford, 1971).

[43] A. Z. Patashinskii and V. L. Pokrovskii, *Fluctuation Theory of Phase Transitions* (Pergamon Press, Oxford, 1979).

[44] T. Dietl and J. Spałek, Effect of Fluctuations of Magnetization on the Bound Magnetic Polaron: Comparison with Experiment, *Phys. Rev. Lett.* **48**, 355 (1982).

[45] V. M. Galitski, A. Kaminski, and S. Das Sarma, Griffiths Phase in Diluted Magnetic Semiconductors, *Phys. Rev. Lett.* **92**, 177203 (2004).

[46] F. Popescu, Y. Yildirim, G. Alvarez, A. Moreo, and E. Dagotto, Critical temperatures of the two-band model for diluted magnetic semiconductors, *Phys. Rev. B* **73**, 075206 (2006).

[47] D.-H. Bui, Q.-H. Ninh, H.-N. Nguyen, and V.-N. Phan, Ferromagnetic transition and spin fluctuations in diluted magnetic semiconductors, *Phys. Rev. B* **99**, 045123 (2019).

[48] G. Alvarez, M. Mayr, and E. Dagotto, Phase Diagram of a Model for Diluted Magnetic Semiconductors Beyond Mean-Field Approximations, *Phys. Rev. Lett.* **89**, 277202 (2002).

[49] G. Rohringer, H. Hafermann, A. Toschi, A. A. Katanin, A. E. Antipov, M. I. Katsnelson, A. I. Lichtenstein, A. N. Rubtsov, and K. Held, Diagrammatic routes to nonlocal correlations beyond dynamical mean field theory, *Rev. Mod. Phys.* **90**, 025003 (2018).

[50] C. Kehl, G. V. Astakhov, K. V. Kavokin, Yu. G. Kusrayev, W. Ossau, G. Karczewski, T. Wojtowicz, and J. Geurts, Observation of the magnetic soft mode in (Cd,Mn)Te quantum wells using spin-flip Raman scattering, *Phys. Rev. B* **80**, 241203(R) (2009).

[51] F. Li, A. Saxena, D. Smith, and N. A. Sinitsyn, Higher-order spin noise statistics, *New J. Phys.* **15**, 113038 (2013).

[52] C. M. Caves and G. J. Milburn, Quantum-mechanical model for continuous position measurements, *Phys. Rev. A* **36**, 5543 (1987).

[53] C. Presilla, R. Onofrio, and U. Tambini, Measurement Quantum Mechanics and Experiments on Quantum Zeno Effect, *Ann. Phys.* **248**, 95 (1996).

[54] L. A. Khalfin, Contribution to the decay theory of a quasi-stationary state, *Sov. Phys. JETP* **6**, 1053 (1958).

[55] B. Misra and E. C. G. Sudarshan, The Zeno's paradox in quantum theory, *J. Math. Phys.* **18**, 756 (1977).

[56] V. S. Zapasskii, A. Greilich, S. A. Crooker, Yan Li, G. G. Kozlov, D. R. Yakovlev, D. Reuter, A. D. Wieck, and M. Bayer, Optical Spectroscopy of Spin Noise, *Phys. Rev. Lett.* **110**, 176601 (2013).

[57] J. Wiegand, D. S. Smirnov, J. Hübner, M. M. Glazov, and M. Oestreich, Spin and reoccupation noise in a single quantum dot beyond the fluctuation-dissipation theorem, *Phys. Rev. B* **97**, 081403(R) (2018).

[58] J. Wiegand, D. S. Smirnov, J. Osberghaus, L. Abaspour, J. Hübner, and M. Oestreich, Hole-capture competition between a single quantum dot and an ionized acceptor, *Phys. Rev. B* **98**, 125426 (2018).

[59] B. E. Larson, K. C. Hass, and R. L. Aggarwal, Effects of internal exchange fields on magnetization steps in diluted magnetic semiconductors, *Phys. Rev. B* **33**, 1789 (1986).

[60] A. V. Koudinov, A. Knapp, G. Karczewski, and J. Geurts, Series of "fractional" peaks in multiple paramagnetic resonance Raman scattering by (Cd,Mn)Te quantum wells, *Phys. Rev. B* **96**, 241303(R) (2017).

[61] R. V. Cherbunin, V. M. Litviak, I. I. Ryzhov, A. V. Koudinov, S. Elsässer, A. Knapp, T. Kiessling, J. Geurts, S. Chusnutdinow, T. Wojtowicz, and G. Karczewski, High-resolution resonance spin-flip Raman spectroscopy of pairs of manganese ions in a CdTe quantum well, arXiv:1903.01276 [Phys. Rev. B (to be published)].

[62] E. A. Chekhovich, A. Ulhaq, E. Zallo, F. Ding, O. G. Schmidt, and M. S. Skolnick, Measurement of the spin temperature of optically cooled nuclei and GaAs hyperfine constants in GaAs/AlGaAs quantum dots, *Nat. Mater.* **16**, 982 (2017).

[63] A. V. Shchepetilnikov, D. D. Frolov, Yu. A. Nefyodov, I. V. Kukushkin, D. S. Smirnov, L. Tiemann, C. Reichl, W. Dietsche, and W. Wegscheider, Nuclear magnetic resonance and nuclear spin relaxation in AlAs quantum well probed by ESR, *Phys. Rev. B* **94**, 241302(R) (2016).

[64] R. J. Warburton, Single spins in self-assembled quantum dots, *Nat. Mater.* **12**, 483 (2013).

[65] B. Smeltzer, L. Childress, and A. Gali, $^{13}$C hyperfine interactions in the nitrogen-vacancy center in diamond, *New J. Phys.* **13**, 025021 (2011).

[66] Ph. Tamarat, T. Gaebel, J. R. Rabeau, M. Khan, A. D. Greentree, H. Wilson, L. C. L. Hollenberg, S. Prawer, P. Hemmer, F. Jelezko, and J. Wrachtrup, Stark Shift Control of Single Optical Centers in Diamond, *Phys. Rev. Lett.* **97**, 083002 (2006).

235416-14

[67] R. M. Macfarlane and R. M. Shelby, *Coherent Transient and Holeburning Spectroscopy of Rare Earth Ions in Solids*, in *Spectroscopy of Solids Containing Rare Earth Ions*, edited by A. A. Kaplyanskii and R. M. Macfarlane, Modern Problems in Condensed Matter Sciences Vol. 21, (Elsevier, Amsterdam, 1987), p. 51.

[68] Y. Wu, Q. Tong, G.-B. Liu, H. Yu, and W. Yao, Spin-valley qubit in nanostructures of monolayer semiconductors: Optical control and hyperfine interaction, *Phys. Rev. B* **93**, 045313 (2016).

[69] I. D. Avdeev and D. S. Smirnov, Hyperfine interaction in atomically thin transition metal dichalcogenides, *Nanoscale Adv.* **1**, 2624 (2019).

[70] E. V. Calman, L. H. Fowler-Gerace, D. J. Choksy, L. V. Butov, D. E. Nikonov, I. A. Young, S. Hu, A. Mischenko, and A. K. Geim, Indirect excitons and trions in $MoSe_2/WSe_2$ van der Waals heterostructures, *Nano Lett.* **20**, 1869 (2020).

[71] V. V. Belykh, D. R. Yakovlev, M. M. Glazov, P. S. Grigoryev, M. Hussain, J. Rautert, D. N. Dirin, M. V. Kovalenko, and M. Bayer, Coherent spin dynamics of electrons and holes in $CsPbBr_3$ perovskite crystals, *Nat. Commun.* **10**, 673 (2019).

[72] S. C. Xu, R. van Dierendonck, W. Hogervorst, and W. Ubachs, A Dense Grid of Reference Iodine Lines for Optical Frequency Calibration in the Range 595-655 nm, *J. Mol. Spec.* **201**, 256 (2000).
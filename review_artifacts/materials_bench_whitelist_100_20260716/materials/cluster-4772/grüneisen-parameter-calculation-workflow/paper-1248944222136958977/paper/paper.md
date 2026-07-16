# When waves meet rays: Seismic vibrations and cosmic showers to test gravity

Aneta Wojnar¹, ∗

¹Institute of Theoretical Physics, University of Wrocław, pl. Maxa Borna 9, 50-206 Wrocław, Poland

We propose a novel laboratory test of gravity combining seismic-wave measurements with cosmic-ray muon detections. Quantum-gravity corrections to the anharmonic Debye model are derived, yielding a modified bulk modulus that encodes deviations from standard gravity. The usual dependence on density, a dominant source of uncertainty, is removed via muon tomography and seismic velocities measurement. We show that this setup can constrain gravity parameters at a level comparable to current laboratory experiments. Prospects for further improvements are briefly discussed.

A wide class of phenomenological approaches to quantum gravity, as well as classical gravity frameworks, predict corrections to microscopic physical quantities [1–9]. Incorporating the quantum structure of space-time typically leads to generalizations of the Heisenberg uncertainty principle, which may give rise to observable effects [10–12]. In this context, the generalized uncertainty principle (GUP) has emerged as a powerful tool for capturing quantum-gravity-induced modifications [13–18]. A common feature of such models is the appearance of a minimal length scale, typically associated with the Planck length, $L_P \sim \sqrt{\frac{\hbar G}{c^3}}$ [19–21].

Within this framework, the GUP modifies the classical phase-space structure. In particular, the phase-space volume element is no longer trivial in order to remain invariant under time evolution. This deformation leads to a modified density of states [22]. As a result, fundamental statistical quantities are affected: the partition function must be redefined using the deformed measure, which in turn induces corrections to thermodynamic potentials, such as the Helmholtz free energy. These modifications propagate to observable quantities, altering the equation of state and other thermodynamic properties.

This feature opens the possibility of probing such effects in laboratory settings by analyzing the properties of materials, in particular solids. In what follows, we consider a Debye crystal at finite temperature, whose vibrational contribution to the Helmholtz free energy is given by

$$
\mathcal{F}_{\mathrm{vib}} = E_0 + 9pRT \left( \frac{T}{\theta_D} \right)^3 \int_0^{\frac{\theta_D}{T}} \frac{x^2\ln(1 - e^{-x})}{1 + \bar{\alpha}(x)} dx, \quad (1)
$$

where $E_0 = \frac{1}{2}\sum_{j=1}^{3pN} \hbar\omega_j$ is the zero-point vibrational energy within the harmonic approximation, $p$ denotes the number of modes, $\theta_D = \hbar\omega_D/k_B$ is the Debye temperature, and $x = \frac{\hbar\omega}{k_B T}$. Other symbols have their usual meaning. The total Helmholtz free energy is then given by

$$
\mathcal{F} = E_{\mathrm{st}} + \mathcal{F}_{\mathrm{vib}}, \quad (2)
$$

where $E_{\mathrm{st}}$ is the static lattice energy at $T=0$.

On the other hand, $\bar{\alpha}(x)$ is, in general, an arbitrary function encoding corrections arising from a given model of gravity [23]. These corrections, following from the Liouville theorem, are incorporated into $\bar{\alpha}(x)$ and originate from a deformation of the elementary phase-space cell. This can be interpreted as a momentum-dependent modification of the unit cell associated with a particle if the correction is momentum-dependent. For generalizations, see [22].

In the following, we restrict to the case where $\bar{\alpha}$ is a quadratic function of $\omega$, as this captures the most commonly studied modifications in the literature [24], giving rise to the quadratic GUP [25]

$$
\Delta\mathcal{X}\Delta\mathcal{P} \geq \frac{\hbar}{2}(1 + \beta_0\mathcal{P}^2), \quad (3)
$$

where $\Delta\mathcal{X}$ and $\Delta\mathcal{P}$ denote position and momentum deviations, respectively, while $\beta_0$ is a gravity model parameter with the unit of inverse quadratic momentum. Then, the zero vibrational energy $E_0$ arising from the harmonic approximation is also modified and takes the form [26]

$$
E_0 = \frac{9}{8}Rp\theta_D \left( 1 - \frac{2}{3}\alpha Np \left( \frac{2\theta_D k_B}{\hbar} \right)^2 \right), \quad (4)
$$

where the last term is the effect of the deformed momentum phase. Similarly, one can distinguish the unmodified part of the Helmholtz vibrational energy,

$$
\mathcal{F}_{\mathrm{vib}} = RpT \left[ \frac{9}{8}\frac{\theta_D}{T} + 3\ln(w) - D(y) \right], \quad (5)
$$

where $w = e^{-y}$, $y = \frac{\theta}{T}$, and

$$
D(y) = 3 \left( \frac{T}{\theta_D} \right)^3 \int_0^{\theta_D/T} \frac{z^3 dz}{e^z - 1} \quad (6)
$$

is the Debye function, from the modified contribution, $\mathcal{F}_{\mathrm{vib}}^{\mathrm{mod}}$, given by

$$
\begin{aligned}
\mathcal{F}_{\mathrm{vib}}^{\mathrm{mod}} =& -\frac{9pR\alpha}{\theta^3} \bigg[ \frac{k_B^2\theta^6}{12\hbar^2} + \frac{k_B^2 T^2}{\hbar^2} \big( \theta^4\mathrm{Li}_2(w) + 4\theta^3 T\mathrm{Li}_3(w) \\
&+ 12\theta^2 T^2\mathrm{Li}_4(w) + 24\theta T^3\mathrm{Li}_5(w) + 24T^4\mathrm{Li}_6(w) \big) \bigg],
\end{aligned}
\tag{7}
$$

where $\mathrm{Li}_s(w) = \sum_{n=1}^{\infty} \frac{w^n}{n^s}$ are the polylogarithm functions.

Note that under the Debye's approximation, $\omega$ is a function of the volume $V$ providing that $\theta = \theta(V)$. Then, we can then easily find the pressure

$$
\begin{aligned}
P &= -\left(\frac{\partial F}{\partial V}\right)_{T}=P_{0} \\
&+\frac{p R \gamma}{V}\left(\frac{9}{8} \theta+3 T D\left(\frac{\theta}{T}\right)\right)+\alpha P_{\mathrm{mod}},
\end{aligned}
\tag{8}
$$

where $P_0$ is the pressure at $T=0$, $P_{\text{mod}}$ is a combination of the logarithmic and polylog functions of $\theta$ and $T$ while

$$
\gamma=\gamma(V)=\frac{\partial \ln \theta}{\partial \ln V}
\tag{9}
$$

is the Grüneisen parameter quantifying the relationship between the thermal and elastic properties of a solid.

It is now straightforward to derive the isothermal bulk modulus

$$
\begin{aligned}
K &=-V\left(\frac{\partial P}{\partial V}\right)_{T} \\
&=K_{0}+p R \frac{\gamma}{V}\left[(1-q+\gamma)\left(3 T D\left(\frac{\theta}{T}\right)+\frac{9 \theta}{8}\right)\right. \\
&\left.-12 T D\left(\frac{\theta}{T}\right) \gamma+\frac{9 \gamma \theta\left(1-(\theta / T)^{2} \alpha\right)}{e^{\theta / T}-1}+\alpha L_{\mathrm{mod}}\right],
\end{aligned}
\tag{10}
$$

where $K_0$ is the bulk modulus at $T=0$, $q$ encondes the volume dependence of anharmonic effects in the lattice and it is given by

$$
q=\frac{\partial \ln \gamma}{\partial \ln V},
$$

while

$$
L_{\mathrm{mod}}=\frac{9}{4}\left((q-1-3 \gamma)\left(L_{\mathrm{Li}}-\frac{k_{B}^{2} \theta^{3}}{\hbar^{2}}\right)+L_{\mathrm{Ln}}\right)
\tag{11}
$$

with

$$
\begin{aligned}
L_{\mathrm{Li}}= &-12 \frac{k_{B}^{2} T^{2} \theta}{\hbar^{2}}\left[\operatorname{Li}_{2}(w)+\frac{4}{y} \operatorname{Li}_{3}(w)+\frac{12}{y^{2}} \operatorname{Li}_{4}(w)\right. \\
& \left.+\frac{24}{y^{3}} \operatorname{Li}_{5}(w)+\frac{24}{y^{4}} \operatorname{Li}_{6}(w)\right],
\end{aligned}
\tag{12}
$$

$$
L_{\mathrm{Ln}}=4 \frac{k_{B}^{2} T^{2} \theta}{\hbar^{2}}(q-1+\gamma) \ln (1-w).
\tag{13}
$$

On the other hand, the bulk modulus can be obtained experimentally, as described in [27]. Let us consider a linear isotropic elastic material. Then, one can relate the material properties, such as bulk $K$ and shear $S$ moduli, together with its density $\rho$, to the $P$-wave velocity $v_{P}$ and $S$-wave velocity $v_{S}$, respectively:

$$
v_{P}=\sqrt{\frac{K+4 S / 3}{\rho}},
\tag{14}
$$

$$
v_{S}=\sqrt{\frac{S}{\rho}},
\tag{15}
$$

which can be rewritten as

$$
K=\rho\left(v_{P}^{2}-\frac{4}{3} v_{S}^{2}\right).
\tag{16}
$$

Although $P$- and $S$-wave velocities can be measured, the equations (14) and (15) alone are insufficient to uniquely determine $K$, $S$, and $\rho$, as they constitute a system of two equations with three unknowns. Knowledge of $\rho$ remains essential for extracting the remaining mechanical parameters.

Most standard methods for determining material density rely, either directly or indirectly, on gravitational effects. Techniques based on weighing, such as geometric measurements or Archimedes' principle, explicitly depend on the gravitational acceleration, while even indirect approaches may involve quantities (e.g., pressure or elastic moduli) influenced by the gravitational environment. In particular, if pressure is used as a control or calibration variable, or if elastic properties (such as Young's modulus, bulk modulus, or shear modulus) enter the inference scheme, these quantities may themselves depend on the local effective gravitational field or on the underlying gravitational model through their coupling to stress distributions and equilibrium conditions. As a result, any gravity-induced modification of internal stresses or boundary conditions can propagate into the effective material response. Consequently, the inferred density may carry an implicit dependence on the underlying gravitational model, motivating the need for independent measurement strategies.

One of such a strategy could be potentially muography. Muons, which are the relevant particles in this technique, have a mass of approximately $\sim 10^{-28}$ kg, making them so light that gravitational effects on their propagation can, for the purposes of current applications, be safely neglected (see, however, the discussion below). As a result, muography is a method that is independent of gravity: it relies solely on electromagnetic muon-matter interactions, well described by the Bethe-Bloch equation [28], rather than on measurements of gravitational forces.

In [27], the bulk modulus (16) of aluminum was determined as $K = 65.99$ GPa, using only the average density inferred from muon detection together with the $P$- and $S$-wave velocity measurements obtained from ultrasonic experiments on aluminum blocks [29]. However, since the experiment was likely performed at ambient temperature $T = 300$ K, we instead adopt the experimental reference value $K_0(V) = 81.3$ GPa reported in [30].

Apart from this, we also calculated the Debye temperature for aluminium using the experimental data reported in [27], in order to avoid relying on additional datasets obtained under different experimental conditions:

$$
\theta_{D}=\frac{\hbar v_{m}}{k_{B}}\left(6 \pi^{2} n\right)^{\frac{1}{3}},
\tag{17}
$$

where $n = M\rho/N_A$, and $v_m$ denotes the mean sound velocity, determined from the measured $P$- and $S$-wave

velocities as:

$$
v_{m}=v_{S}\left(\frac{3}{2+\left(\frac{v_{S}}{v_{P}}\right)^{3}}\right)^{\frac{1}{3}}. \tag{18}
$$

The Debye temperature resulting from these experiments is $396 \pm 6$ K. It is worth noting that the Debye temperature is usually obtained experimentally from the specific heat curve at low temperatures [31], which, however, may also depend on gravity, see e.g. [32, 33]. Another approach to determining the Debye temperature is temperature-dependent X-ray diffraction via the Debye-Waller factor [34]; however, this method relies on solving the Schrödinger equation for a quantum oscillator, which acquires quantum gravitational corrections [35]. This illustrates that muography, together with measurements of seismic vibrations, can be used to extract gravity-independent thermodynamic characteristics. We will use our value for $\theta_{D}$ to account for measurement uncertainties.

It is straightforward to determine the value of the parameter from (10). At ambient temperature, $T=300$K, and accounting for the experimental uncertainties, one obtains $\alpha=(1.438 \pm 2.94) \times 10^{-25} \mathrm{~s}^{2}$, which corresponds to $\beta_{0} \approx 1.53 \times 10^{50} \mathrm{~s}^{2} \mathrm{~kg}^{-2} \mathrm{~m}^{-2}$. The obtained value can be compared with results from other experiments, see, e.g., [25].

On the other hand, since in the temperature range 0 – 300K no significant variations in (10) are expected, we also consider, for instance, $T=10$K, for which we find $\alpha=(8.11 \pm 1.66) \times 10^{-24} \mathrm{~s}^{2}$, corresponding to $\beta_{0} \approx 8.64 \times 10^{50} \mathrm{~s}^{2} \mathrm{~kg}^{-2} \mathrm{~m}^{-2}$.

In Fig. 1, we illustrate this behavior, showing how the constrained value of the parameter $\alpha$ evolves with temperature. The sensitivity of the gravity parameter

![](./images/1248944222136958977_1.jpg)

FIG. 1. Expected values of the gravitational parameter $\alpha$ in low-temperature regime $(T<\theta_{D})$ for aluminum from the experiments performed in [27].

to the energy/temperature regime has already been discussed in [11, 33, 36, 37]. The difference of nearly two orders of magnitude - partially also depending on the numerical precision - observed here (with a stronger bound at higher temperature), and potentially even larger at temperatures beyond those considered [38] may admit a physical interpretation.

One possible explanation is that, at higher temperatures, as particles vibrate more rapidly, phonons may effectively acquire a mass, in the sense that correction terms appear in a momentum-dependent redefinition of the mass (see e.g. [39]). A similar phenomenon is known for photons (see e.g. [40]). Alternatively, this behaviour can be interpreted in terms of a deformation of phase-space cells, which becomes more pronounced at higher momenta. This effect may be also reformulated in terms of a modified dispersion relation [41]. Such modifications are often motivated by attempts to describe quantum properties of spacetime [42, 43], e.g. through noncommutativity [44–46]. A key phenomenological implication concerns the fate of relativistic symmetries [47], leading in particular to scenarios of Lorentz Invariance Violation (LIV), in which modified dispersion relations are not preserved under standard Lorentz transformations.

The impact of LIV on cosmic showers has been investigated in [48]. It was shown that LIV affects the number of muons produced in the atmosphere, while leaving their energy essentially unchanged, which could directly influence the inferred densities of the aluminum block. Therefore, muography can still be regarded as a gravity-independent method for determining densities and other elastic properties of materials.

Nevertheless, in order to fully exploit the potential of the proposed method, the experiment described in [27] requires further development and refinement. First, the setup should be improved by significantly increasing the number of detection channels (only 3 are used in [27]), thereby enabling a much higher measurement resolution. In addition, implementing a multilayer detector with signal readout from both ends of each segment would allow for precise reconstruction of the particle trajectory, leading to a more accurate determination of its direction as well as improved timing measurements [49–51]. Altogether, these upgrades would enhance the determination of density and elastic moduli.

Moreover, it is important to account for previously unreported uncertainties in the seismic velocity measurements which we use here, which directly affect the inferred thermodynamic properties of the material. Another relevant improvement would be to perform the experiment under controlled environmental conditions, for instance by integrating the cosmic-ray detector setup with a climatic chamber, allowing measurements to be systematically repeated at different temperatures. This is particularly relevant, as observing an effect such as the one shown in Fig. 1 could potentially indicate sensitivity to quantum gravity effects.

## ACKNOWLEDGEMENTS

For those who wander the thin line between dream and abyss: may courage guide us to a quiet shore.

AW thanks Juan Ángel Sans Tresserras and Marcin Bielewicz for interesting discussions.

This article is based upon work from COST Action FuSe, CA24101, supported by COST (European Cooperation in Science and Technology).

* Corresponding author;
E-mail: aneta.wojnar@uwr.edu.pl

[1] M. Moussa, Advances in High Energy Physics **2015** (2015).
[2] R. Rashidi, Annals of Physics **374**, 434 (2016).
[3] I. H. Belfaqih, H. Maulana, and A. Sulaksono, International Journal of Modern Physics D **30**, 2150064 (2021).
[4] A. Mathew and M. K. Nandy, Royal Society open science **8**, 210301 (2021).
[5] B. Hamil and B. Lütfüoğlu, International Journal of Theoretical Physics **60**, 2790 (2021).
[6] D. Gregoris and Y. C. Ong, arXiv preprint arXiv:2202.13904 (2022).
[7] A. Wojnar, Physical Review D **107**, 044025 (2023).
[8] A. Wojnar, Physical Review D **109**, 024011 (2024).
[9] A. Wojnar and D. A. Gomes, Universe **10**, 217 (2024).
[10] A. Pachoł and A. Wojnar, The European Physical Journal C **83**, 1097 (2023).
[11] A. Pachoł and A. Wojnar, Class. Quant. Grav. **40**, 195021 (2023).
[12] A. Kozak, A. Pachoł, and A. Wojnar, Annals of Physics **481**, 170136 (2025).
[13] A. Kempf, G. Mangano, and R. B. Mann, Physical Review D **52**, 1108 (1995).
[14] M. Maggiore, Physics Letters B **304**, 65 (1993).
[15] M. Maggiore, Physical Review D **49**, 5182 (1994).
[16] L. N. Chang, D. Minic, N. Okamura, and T. Takeuchi, Physical Review D **65**, 125027 (2002).
[17] L. N. Chang, D. Minic, N. Okamura, and T. Takeuchi, Physical Review D **65**, 125028 (2002).
[18] A. F. Ali, Classical and Quantum Gravity **28**, 065013 (2011).
[19] M. Bishop, J. Lee, and D. Singleton, Physics Letters B **802**, 135209 (2020).
[20] M. Bishop, J. Contreras, and D. Singleton, universe **8**, 192 (2022).
[21] S. Segreto and G. Montani, The European Physical Journal C **83**, 385 (2023).
[22] A. Pachoł, Nucl. Phys. B **1010**, 116771 (2025).
[23] A. F. Ali, S. Das, and E. C. Vagenas, Physics Letters B **678**, 497 (2009).
[24] That is, we focus on the quadratic momentum corrections to the Heisenberg Uncertainty Principle.
[25] P. Bosso, G. G. Luciano, L. Petruzziello, and F. Wagner, Class. Quant. Grav. **40**, 195014 (2023).
[26] $\alpha\omega^{2}=\beta_{0}\hbar^{2}/v_{m}^{2}\mathcal{P}^{2}$, where $\beta_{0}$ is the quantum gravity parameter with the unit of inverse quadratic momentum, $v_{m}$ is the mean sound velocity, while $\mathcal{P}$ is the phonon momentum.
[27] J. Matsushima, M. Kodama, M. Y. Ali, F. Bouchaala, H. K. Tanaka, T. Kin, H. Basiri, T. Yokota, and M. Suzuki, Geophysical Journal International **239**, 1821 (2024).
[28] H. A. Bethe and J. Ashkin, E. Segre **1** (1953).
[29] The errors were not provided apart from the density $\rho=2.58\pm0.12$ g cm$^{-3}$. According to our analysis, $K=(65.8\pm3.1)$, GPa solely from the density uncertainty.
[30] R. Gaudoin and W. Foulkes, Physical Review B **66**, 052104 (2002).
[31] C. Kittel and P. McEuen, *Introduction to solid state physics* (John Wiley & Sons, 2018).
[32] S. Riasat and B. P. Mandal, The European Physical Journal Plus **138**, 1 (2023).
[33] A. Pachoł and A. Wojnar, in preparation (2026).
[34] R. Horning and J.-L. Staudenmann, Foundations of Crystallography **44**, 136 (1988).
[35] L. N. Chang, D. Minic, N. Okamura, and T. Takeuchi, Phys. Rev. D **65**, 125027 (2002).
[36] A. Kozak and A. Wojnar, The European Physical Journal C **81**, 1 (2021).
[37] E. Lope-Oter and A. Wojnar, JCAP **02**, 017 (2024).
[38] Although the Debye model ceases to reliably describe crystal behaviour above the Debye temperature.
[39] M. Visser and S. Weinfurtner, Phys. Rev. D **72**, 044020 (2005).
[40] M. Füllekrug, Physical review letters **93**, 043901 (2004).
[41] S. Hossenfelder, Classical and Quantum Gravity **23**, 1815 (2006).
[42] G. Amelino-Camelia, Living Reviews in Relativity **16**, 5 (2013).
[43] A. Addazi, J. Alvarez-Muniz, R. A. Batista, G. Amelino-Camelia, V. Antonelli, M. Arzano, M. Asorey, J.-L. Atteia, S. Bahamonde, F. Bajardi, *et al.*, Progress in Particle and Nuclear Physics **125**, 103948 (2022).
[44] A. Borowiec and A. Pachoł, SIGMA **6**, 086 (2010).
[45] P. Aschieri, A. Borowiec, and A. Pacho, JCAP **04**, 025 (2021).
[46] P. Aschieri, A. Borowiec, and A. Pachoł, JHEP **10**, 152 (2017).
[47] G. Amelino-Camelia, J. Ellis, N. Mavromatos, D. V. Nanopoulos, and S. Sarkar, Nature **393**, 763 (1998).
[48] C. Trimarelli, R. Alves Batista, F. Canfora, S. de Jong, G. De Mauro, H. Falcke, T. Fodran, C. Galea, U. Giac-cari, J. Hörandel, *et al.*, (2022).
[49] M. Bielewicz, A. Bancer, M. Barabanov, A. Chlopik, M. Czarnynoga, D. Dabrowski, A. Dudzinski, A. Dziedzic, M. Grodzicka-Kobylka, J. Grzyb, *et al.*, Journal of Instrumentation **16**, P11035 (2021).
[50] M. Bielewicz, A. Bancer, A. Dziedzic, J. Grzyb, E. Jaworska, G. Kasprowicz, M. Kiecana, P. Kolasinski, M. Kuc, M. Kuklewski, *et al.*, Electronics **12**, 1492 (2023).
[51] M. Bielewicz, M. Grodzicka-Kobylka, S. Mianowski, P. Sibczynski, L. Swiderski, T. Szczesniak, M. Linczuk, D. Wielanek, A. Kisiel, G. Kasprowicz, *et al.*, in *Photonics Applications in Astronomy, Communications, Industry, and High-Energy Physics Experiments 2018*, Vol. 10808 (SPIE, 2018) pp. 1268–1275.
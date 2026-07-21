# Resonant Subterahertz Coherent Acoustic Waves Excitation by Josephson Junction

Natalia I. Polzikova, Georgy D. Mansfeld, Yury S. Tokpanov, and Valery P. Koshelets
Kotel'nikov Institute of Radio-Engineering and Electronics, Russian Academy of Science
Moscow, Russia
polz@mail.cplire.ru

Abstract—A superfine resonant structure with a voltage spacing of about 19 nV (corresponding frequency 9 MHz) and an extremely low differential resistance has been observed in the Josephson Flux Flow Oscillator (FFO) IVCs. We have analyzed coherent phonon radiation and detection due to the interaction of Josephson's electromagnetic oscillations with mechanical displacement field caused by piezoelectric effect or electrostriction effect. In contrast to the other works we consider sound generation in the Josephson tunneling structure, deposited on the rather thick substrate. This layered structure plays the role of high overtone composite resonator for bulk acoustic waves propagating normally to the layers.

## I. INTRODUCTION

The spectrum of acoustic phonons covers frequencies up to several terahertz. So the excitation of coherent acoustic waves (AW) with subterahertz frequencies is a problem of great importance. As attenuation of AW is reduced at liquid helium temperatures, in 1970s and later the superconducting tunnel junctions have been used to generate and also to detect both incoherent and coherent AW above 100 GHz [1-4]. The possibility of AW generation in high $T_c$ Josephson junctions has been considered in [5, 6]. Recently, phonon radiation in the Josephson junctions as a reason for decoherence of superconducting quantum bits is also discussed [7]. Most of the papers mentioned above deal with interaction of AW with electromagnetic fields in the junction via piezoelectric coupling.

In the present paper the possibility of AW generation due to electromagnetic wave, accompanying Josephson vortex motion, is considered. The Josephson flux flow oscillator (FFO) based on unidirectional flow of vortices in a long tunnel junction is shown in Fig.1. Usually in these structures with low dumping the step-like current-voltage characteristics, so called Fiske steps (FS), are occurred. The position of the steps depends upon Josephson junction resonant frequencies defined by junction length. We'll consider AW generation in the tunneling structure, deposited on the relatively thick flat substrate with double side polished parallel surfaces. This layered structure plays the role of high overtone composite resonator for bulk AW propagating normally to the layers. The resonant generation and detection of AW are displayed on I-V curve (IVC) as a series of additional steps on the top of the ordinary FS series. The experiments carried out on Nb-AlO$_x$-Nb junction on Si substrate revealed the fine structure of IVC with steps separation and low differential resistance, which is pointing out AW generation [8].

## II. THEORY

### A. Dynamics of long Josephson junction

Consider two superconductors biased at the constant voltage and spaced by dielectric layer of thickness $d$. External magnetic field lies in the interface along the x axis (Fig. 1). This structure is deposited on a substrate of thickness $D$. The current flowing in the dielectric interlayer will be in the form $j_y = j_{s,y} + j_{n,y} = j_1 \sin \varphi(z,t)+\sigma_T e_y^0$. Here $j_{s,y}$ and $j_{n,y}$ are, respectively, Josephson tunneling current of Cooper pairs with amplitude $j_1$ and normal electrons current with tunnel conductivity $\sigma_T$, $\varphi(z,t)$ is the difference of SC wave functions.

![](./images/811637272112791553_1.jpg)

Figure 1. Schematics of the structure: 1- the Si substrate, 2-long Josephson junction Nb-AlO$_x$-Nb, the black area – the AlO$_x$ insulator film.

In linear approximation upon field amplitudes one can write down the expression for phase difference $\varphi=\varphi_{0}+\varphi_{1}$, where $\varphi_{0}=\omega t-q z$. Hereafter upper subscript (0) denotes the values integrated on dielectric layer thickness. The Josephson relations $\omega=\partial \varphi_{0} / \partial t=2 e V_{0} / \hbar, \quad q=\partial \varphi_{0} / \partial z=2 e \bar{d} H_{0} / h c$ connect the frequency $\omega$ and the wave vector $q$ with constant voltage $V_{0}$ and magnetic field $H_{0}$. Here $\bar{d}=d+2 \lambda_{L}$ is an effective size of magnetic field localization, $\lambda_{L}$ is a London penetration depth. The phase addition $\varphi_{1}$ is connected with ac voltage on the junction $v_{1}=e_{y}^{0} d$ as $\partial \varphi_{1} / \partial t=(2 e / \hbar) v_{1}$ [9].

The interaction of Josephson's electromagnetic oscillations in the junction with mechanical displacement field $\vec{u}$ caused by piezoelectric effect or electrostriction effect produces a polarization density $\vec{p}$ and contributes to an electrical displacement $d_{y}^{0}(z)=\varepsilon_{d} e_{y}^{0}(z)+4 \pi p_{(U) y}^{0}(z)$. By standard integration of Maxwell equations the generalized Josephson relationship between phase gradient and polarization can be deduced in the form

$$
\frac{\partial^{2} \varphi_{1}}{\partial z^{2}}-\frac{1}{\widetilde{c}^{2}}\left(\frac{\partial^{2} \varphi_{1}}{\partial t^{2}}+\Gamma \frac{\partial \varphi_{1}}{\partial t}+\frac{8 \pi e d}{\hbar \varepsilon_{d}} \frac{\partial p_{(U) y}}{\partial t}\right)=\frac{1}{\lambda_{J}^{2}} \sin \varphi_{0}, \quad(1)
$$

with a Swihart electromagnetic wave velocity $\widetilde{c}=c \sqrt{d /\left(\varepsilon_{d} \bar{d}\right)}$, a Josephson penetration depth $\lambda_{J}^{2}=\hbar c^{2} /\left(8 \pi e \bar{d} j_{1}\right)$, a Maxwell relaxation frequency $\Gamma$. For typical Nb- $AlO_x$-Nb junction with $2 \lambda_{L} \sim 170 \mathrm{~nm}$, d~1-2 nm, $\varepsilon_{d}$~10 the estimation gives a wave slowing-down $\widetilde{c} / c \approx 0.03$. In spite of this, electromagnetic wave velocity in the Josephson junction is much greater than AW velocity.

### B. Equations for elastic displacements

Effective piezoelectric constants $\widetilde{\beta}_{i, k l}=\beta_{i, k l}+a_{i m k l} E_{m} / 4 \pi$ describe both normal piezzoeffect and the induced one by the electrostriction. In linear approximation the electric field in dielectric layer is uniform $E_{m}=V_{0} / d$. Piezoelectric interaction contributions to stress tensor and electric polarization are $\Delta T_{i j}=\widetilde{\beta}_{l, i j} e_{l}$ and $p_{i}=-4 \pi \widetilde{\beta}_{i k l} u_{k l}$ respectively. While the piezoelectric effect is absent in bulk dielectrics with inversion symmetry, it is not possible to eliminate this coupling at the superconductor- insulator boundary where this symmetry is always broken. Assuming that electromechanical coupling tensor has 4mm symmetry with axis lying in the interface, one can obtain the desired polarization as $p_{2}^{0}=-4 \pi \beta_{24}\left(\partial u_{2}^{0} / \partial z\right)$.

After integration of the equation of motion for elastic medium along dielectric thickness we get

$$
\rho \frac{\partial^{2} u_{2}^{0}}{\partial t^{2}}=\frac{T_{2}(d)-T_{2}(0)}{d}+C_{44} \frac{\partial^{2} u_{2}^{0}}{\partial z^{2}}+\beta_{24} \frac{\partial e_{2}^{0}}{\partial z} \quad(2)
$$

The boundary conditions for elastic displacements and stresses at the dielectric layer surfaces are $T_{2}(0)=T_{2}^{(1)}(0)$, $T_{2}(d)=T_{2}^{(2)}(d), u_{2}(0)=u_{2}^{(1)}(0), u_{2}(d)=u_{2}^{(2)}(d)$, where the quantities with superscripts 0, (1), (2) refer to dielectric layer and surrounding media. If we assume that elastic displacements slightly vary along the thickness of dielectric, then we can easily obtain the following relationships

$$
u_{2}(0)=u_{2}^{0}+\frac{d}{2 C_{11}} Z_{1} \frac{\partial u_{2}^{(1)}(0)}{\partial t}, \quad u_{2}(d)=u_{2}^{0}-\frac{d}{2 C_{11}} Z_{2} \frac{\partial u_{2}^{(1)}(d)}{\partial t}.
$$

Here $Z_{1,2}$ are acoustic impedances of the surfaces $y=0, d$ respectively. For perfectly reflecting lower surface of the substrate $(y=-D) \quad Z_{1} \approx i Z_{0} \tan k D, \quad$ where $k=\omega / v_{l}$, $v_{l}$ - longitudinal AW velocity in the substrate, $Z_{0}=v_{l} \rho_{s}$ - acoustic impedance of the substrate. If the upper surface of the structure (Fig. 1) is not perfectly reflecting, the impedance $Z_{2}$ contributes to acoustic losses.

### C. Dispersion equation and current-voltage characteristics

For harmonic dependence of all variables on time and coordinates $\exp i\left(k_{y} y+q z-\omega t\right)$ one can get the dispersion relation $\omega^{2}=q^{2} \widetilde{c}^{2}\left(\varepsilon / \varepsilon^{*}\right)$ for coupled electroacoustic oscillations in the form

$$
\omega^{2}=q^{2} \widetilde{c}^{2}\left(1+\frac{4 \pi \widetilde{\beta}_{24}^{2}}{\varepsilon \rho \widetilde{c}^{2}} \frac{1}{1+i\left(Z_{2}^{\prime}-Z_{1}^{\prime}\right) /(\omega d \rho)-q^{2}\left(v_{\perp} / \widetilde{c}\right)^{2}}\right)(3)
$$

with $Z_{1,2}^{\prime}=Z_{1,2} /\left(1 \pm i d \omega Z_{1,2} / C_{11}\right), \quad v_{\perp}=\sqrt{C_{44} / \rho}$. The last term in the denominator of (3) may be ignored owing to inequality $v_{\perp}<<\tilde{c}$.

According to standard procedure [9] one can find the uniform component of Josephson current. For the case of long junction the following expression can be obtained

$$
j_{0}\left(V_{0}, H_{0}\right)=-\widetilde{j}_{0} \Omega_{n}^{2} \operatorname{Im}\left[\omega^{2}+i \bar{\Gamma} \omega-q^{2} \widetilde{c}^{2}\left(\varepsilon / \varepsilon^{*}\right)\right]^{-1} \quad(4)
$$

where $\widetilde{j}_{0}=j_{1} \widetilde{c}^{2} /\left(2 \lambda_{J}^{2} \Omega_{n}^{2}\right), \Omega_{n}=\pi n v_{l} / D$ - the frequency of $n$-th mode of high overtone resonator. The value $\bar{\Gamma}=\Gamma_{E}+\Gamma_{A W}$ describes electromagnetic losses and nonresonance AW radiation. For the frequencies from 100 to 700 GHz mode numbers of excited AW fall in the range of $\left(10^{3}-10^{4}\right)$. As shown in Fig. 2, there are several bumps of current at AW resonance frequencies $\omega=\Omega_{n+m}$ against a background of usual Lorentz form of one of the FS, corresponding to the voltages $V_{n+m}=\Omega_{n+m} \hbar /(2 e)$.

![](./images/811637272112791553_2.jpg)

Figure 2. Calculated dependence of relative current $j_0 / \widetilde{j}_0$ versus relative frequency $\omega / \Omega_n$ or relative voltage $\hbar\omega/(2e\Omega_n)$ at the electromechanical coupling constant $\delta=4\pi\widetilde{\beta}_{24}{}^2/(\varepsilon\widetilde{c}{}^2)$=$2.510^{-7}$,
$\overline{\Gamma}=3\cdot10^{-2}\Omega_n$, $\text{Im}k/\text{Re}k=10^{-6}$.

![](./images/811637272112791553_3.jpg)

Figure 3. Reconstructed IVC of the FFO. Data marked “I<sub>CL-1,2</sub>” are measured at a slightly different currents I<sub>CL</sub> that flow under the FFO and induce magnetic field.

### III. SUPERFINE RESONANT STRUCTURE

Flux flow oscillator on the base of Nb-AlO<sub>x</sub>-Nb superconducting tunnel junction was fabricated on double side polished Si substrate (350 μm). The thicknesses of the junction layers were correspondingly 1-2 nm for AlO<sub>x</sub>, 200 nm and 500 nm for base and top Nb electrodes. By measuring the frequency of the FFO radiation emission [10], its IV-curve can be reconstructed with accuracy better than 1 nV [8]. From Fig. 3 one can see that the FFO IVC consists of a set of separate steps rather than being a continuous curve. The differential resistance on these steps is extremely low, $R_d^B(\text{res})=0.00037\,\Omega$. It is important to note that this value is considerably lower than the average value on the FS ($R_d^B=0.0016\,\Omega$).

The voltage spacing of 19 nV, corresponding to a separation of 9 MHz, coincides with difference between the acoustic modes frequencies of the resonator structure consisting of substrate plate and the covering FFO layers

$$
v_l/(2D)=(\Omega_{n+1}-\Omega_n)/(2\pi).
$$

The value of voltage (frequency) spacing and separate steps with low differential resistance show a good agreement with theoretical treatment.

### IV. CONCLUSION

The superfine resonant structure of the FFO IVC with step separation that coincide with acoustic modes frequency spacing may be attributed to acoustic wave generation by the FFO and propagation in thick Si substrate as in acoustic resonator. So the generation and detection of coherent acoustic waves with frequencies up to 700 GHz due to piezoelectric effect in dielectric interface in superconductor junction may be achieved.

### REFERENCES

[1] W.Eisenmenger and A.H.Dayem, "Quantum generation and detection of incoherent phonons in superconductors", Phys. Rev. Lett., vol 18, pp.125-127, January1967.

[2] H.Kinder, "Spectroscopy with phonons on Al<sub>2</sub>O<sub>3</sub>: V<sup>3+</sup> using the phonon bremsstrahlung of a superconducting tunneling junction", Phys. Rev. Lett., vol 28, pp.1564-1567, June 1972.

[3] P.Berberich, R.Buemann, and H.Kinder, "Monochromatic phonon generation by Josephson effect", Phys. Rev. Lett., vol 49, pp.1500-1503, November 1982.

[4] E.H.Jacobsen, "Generation and detection of ultrasonic waves beyond 100GHz", J.de Phys. Colloq., vol 33/C6, pp.C6-25--C6-31, November 1972.

[5] T. Hristov and A. Groshev, " Coupled Josephson and piezo oscillators. The effects of capacitance, noise and quality" Physica C, vol 175, pp. 600-602, May 1991.

[6] A. Groshev and T. Hristov, "Shapiro steps without RF source by coupling of Josephson and piezooscillators", Physica C, vol 160, pp. 317-319, September 1989.

[7] L. B. Ioffe, V. B. Geshkenbein, Ch. Helm, and G. Blatter, "Decoherence in superconducting quantum bits by phonon radiation", Phys. Rev. Lett, vol 93. pp. 057001-057004, July 2004.

[8] V.P. Koshelets, A.B.Ermakov, S.V.Shitov, P.V.Dmitriev, L.V.Fillipenko, A.M.Baryshev, et al. "Superfine resonant structure on IVC of long Josephson junctions and its influence on flux flow oscillator linewidth", IEEE Trans. on Appl. Supercond., vol 11, pp. 1211-1214, January 2001.

[9] A.Barone, G.Paternò, Physics and Applications of Josephson Effect, New York: John Wiley & Sons, Inc., 1982.

[10] V.P. Koshelets, S.V. Shitov, L.V. Filippenko, V.L. Vaks, J. Mygind, A.B. Baryshev, W. Luinge, N. Whyborn, " Phase Locking of 270-440 GHz Josephson Flux Flow Oscillator", Rev. of Sci. Instr., vol 71, pp. 289-293, January 2000.
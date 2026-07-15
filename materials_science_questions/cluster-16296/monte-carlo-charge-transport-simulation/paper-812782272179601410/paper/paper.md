![](./images/812782272179601410_1.jpg)

Monte Carlo modeling of electron velocity overshoot effect in quantum well
infrared photodetectors

M. Ryzhii, V. Ryzhii, and M. Willander

Citation: J. Appl. Phys. 84, 3403 (1998); doi: 10.1063/1.368499
View online: http://dx.doi.org/10.1063/1.368499
View Table of Contents: http://jap.aip.org/resource/1/JAPIAU/v84/i6
Published by the American Institute of Physics.

Additional information on J. Appl. Phys.
Journal Homepage: http://jap.aip.org/
Journal Information: http://jap.aip.org/about/about_the_journal
Top downloads: http://jap.aip.org/features/most_downloaded
Information for Authors: http://jap.aip.org/authors

ADVERTISEMENT

![](./images/812782272179601410_2.jpg)

# Monte Carlo modeling of electron velocity overshoot effect in quantum well infrared photodetectors

M. Ryzhii,${}^{\mathrm{a}),\mathrm{b)}}$ V. Ryzhii,${}^{\mathrm{b)}}$ and M. Willander
Department of Microelectronics and Nanoscience, Chalmers University of Technology and Gothenburg University, Gothenburg S-412 96, Sweden

(Received 24 March 1998; accepted for publication 9 June 1998)

Transient response of n-type AlGaAs/GaAs and InP/InGaAs quantum well infrared photodetectors (QWIPs) has been studied using an ensemble Monte Carlo particle method. It has been shown that the photocurrent initiated by an ultrashort pulse of infrared radiation reveals a sharp peak associated with the electron velocity overshoot effect. The existence of the photocurrent peak results in a plateaulike region in the QWIP frequency-dependent responsivity in the terahertz range. This effect can be used for heterodyne detection in QWIP-based mixers at terahertz frequencies and for generation of terahertz radiation. Larger intervalley separation and, consequently, more pronounced electron velocity overshoot in InP-based QWIPs in comparison with QWIPs with AlGaAs barriers lead to higher performance of the former in the terahertz range of spectrum. © 1998 American Institute of Physics. [S0021-8979(98)02318-4]

## I. INTRODUCTION

Quantum well infrared photodetectors (QWIPs) utilizing electron intersubband transitions have a great potential as ultrahigh-speed/high-frequency devices. Promising high-frequency performance has recently been demonstrated for AlGaAs/GaAs QWIPs. $^{1-3}$ It has been shown theoretically $^{4,5}$ that transit-time effect limited bandwidth in excess of 100 GHz can be obtained in QWIPs. Recently it was predicted using an ensemble Monte Carlo particle modeling $^{6,7}$ that the QWIP frequency-dependent responsivity can reveal very slow decay in the range of frequencies far beyond the reciprocal electron transit time. This is due to the velocity overshoot effect $^{8,9}$ being exhibited by photoexcited electrons just after their photoexcitation from QWs. The electron velocity overshoot effect can provide the QWIP operation in the terahertz range of spectrum. Although the value of the QWIP responsivity in the above range can be markedly smaller than that in the gigahertz range, QWIPs can be used as terahertz devices, for example for heterodyne detection and generation of terahertz radiation. In this paper a self-consistent ensemble Monte Carlo particle simulator $^{6}$ is used in order to investigate transient electron transport in $n$-type AlGaAs/ GaAs and InP/InGaAs QWIPs and estimate their potentials in the terahertz range of signal frequencies. We consider conventional QWIPs consisting of a multiple QW structure with thin doped narrow-gap layers forming QWs and relatively thick undoped wide-gap barrier layers. The structure is sandwiched between doped contact layers playing the role of the emitter and the collector. $^{10}$

The model of QWIPs takes into account electron excitation from bound states in the QWs into continuum states, injection of electrons from the emitter through the extreme barrier, capture of the electrons into QWs, transport of the electrons across the QW structure and their escape to the collector in the self-consistent electric field, i.e., the processes responsible for the QWIP operation under illumination by infrared radiation. $^{6,7}$ The band diagram of a QWIP under biasing voltage and main electron processes is shown in Fig. 1. The response of QWIPs which are initially in steady-state condition to ultrashort pulses of infrared radiation is studied using the model in question. The Fourier transform of the calculated transient photocurrent yields the frequency-dependent responsivity of the QWIPs under consideration. We compare the QWIPs made of AlGaAs/GaAs and InP/InGaAs with AlGaAs and InP barriers, respectively.

In Sec. II we present some details of the modeling under consideration. In Sec. III we present calculated using the Monte Carlo method spatial distributions of the photoexcited electrons arisen due to illumination by $\delta$-like pulses of infrared radiation. Then we demonstrate temporal dependences of the photocurrent. The Fourier transform of the calculated response is used for the calculation of the QWIP frequency-dependent responsivity. An analytical model of the frequency-dependent response is considered and used to approximate the characteristics obtained by the Monte Carlo modeling in Sec. IV.

## II. MODELING DETAILS

We have used the Monte Carlo particle modeling described previously $^{6,7}$ to calculate the transient response of QWIPs to $\delta$-like probing pulses of infrared radiation:

$$
I=I_{0}+\left(\frac{Q}{\hbar \Omega}\right) \cdot \delta(t). \tag{1}
$$

Here $I_{0}$ is the steady state component of the infrared photon flux, $Q$ is the energy of the pulse, $\hbar \Omega$ is the energy of infrared photons, and $\delta(t)$ is the Dirac $\delta$ function. Assuming that

$$
\varepsilon_{i}<\hbar \Omega<\varepsilon_{i}+\Delta_{\Gamma L}, \varepsilon_{i}+\Delta_{\Gamma X}, \tag{2}
$$

${}^{\mathrm{a})}$Electronic mail: ryzhii@hotmail.com
${}^{\mathrm{b})}$Permanent address: Computer Solid State Physics Laboratory, University of Aizu, Aizu-Wakamatsu 965-80, Japan.


![](./images/812782272179601410_3.jpg)

FIG. 1. QWIP band diagram. Arrows schematically show the electron transitions.

where $\varepsilon_{i}$ is the QW ionization energy and $\Delta_{\Gamma L}$, $\Delta_{\Gamma X}$ are the intervalley separations, we consider the photoexcitation of the electrons from the bound states in the QW into the continuum states in the $\Gamma$ valley. Taking into account inequality (2) the function $\delta G(\varepsilon, t, x)$ characterizing the generation of the photoelectrons in the continuum states of the $\Gamma$ valley, i.e., the photoelectron initial energy and spatial distribution was chosen in the form: $^{6}$

$$
\delta G(\varepsilon, t, x) \propto \delta(t) \cdot \delta\left(\varepsilon-\hbar \Omega+\varepsilon_{i}\right) \cdot \sum_{n=1}^{N} \delta(x-n L). \quad (3)
$$

Here $\varepsilon$ and $x$ are the electron energy with respect to the bottom of the continuum states and the distance from the emitter contact, $N$ is the number of the QWs and $L=L_{w}$ $+L_{b}$ is the period of the QW structure, where $L_{w}$ and $L_{b}$ are

![](./images/812782272179601410_4.jpg)

FIG. 2. Spatial distributions of photoexcited electron concentrations in the $\Gamma, L$ and $X$ valleys at different moments in AlGaAs/GaAs QWIP.

![](./images/812782272179601410_5.jpg)

FIG. 3. Spatial distributions of photoexcited electron concentrations in the $\Gamma, L$ and $X$ valleys at different moments in InP/InGaAs QWIP.

the width of the QW and the barrier, respectively $(L_{w}$ $\ll L_{b}$). The initial steady-state potential distributions under constant applied voltage $V$ and intensity of infrared radiation $I_{0}$ were calculated using the developed analytical model. $^{11}$ The pulse power $Q$ was supposed to be low enough that the photoexcitation does not significantly disturb the steady-state potential distribution. The modeling time was chosen to be longer than the lifetime of the photoexcited electrons in the QW structure. This time is defined by the processes of the capture of the electrons and their escape to the collector. More slow processes associated with the QW structure recharging were beyond our study. The QWIPs with the number of the QWs $N=4$, 16 and 64, the periods of the QW structure $L=35-75$ nm, under biasing voltages $V$ corresponding to the average electric field $E=V / W$ $=20-80$ kV/cm $[W=(N+1) L$ is the thickness of the QW structure] at the temperature $T=77$ K were considered. The donor sheet concentration in each QW $\Sigma_{d}$, the photoexcitation cross section $\sigma$, and the initial energy of the photoexcited electrons with respect to the bottom of the continuum states subband $\Delta=\hbar \Omega-\varepsilon_{i}$ were chosen to be $\Sigma_{d}$ $=10^{12} \mathrm{~cm}^{-2}, \sigma=2 \times 10^{-15} \mathrm{~cm}^{-2}$ and $\Delta=0.01$ eV.

The band structure and the scattering mechanisms parameters for $\mathrm{Al}_{0.3} \mathrm{Ga}_{0.7} \mathrm{As}$ and $\mathrm{InP}$ as the materials for the QWIP barriers were taken from Refs. 12 and 13. The capture

![](./images/812782272179601410_6.jpg)

FIG. 4. Peak velocity and peak kinetic energy of photoexcited electrons versus average electric field.

of the electrons with the energies less than the optical pho- non energy into the QWs can be characterized by the prob- ability $c$, which was assumed to be in the range $^{14} c$ $=0.25-0.75$.

![](./images/812782272179601410_7.jpg)

FIG. 5. Transient photocurrent in AlGaAs/GaAs QWIPs.

![](./images/812782272179601410_8.jpg)

FIG. 6. Transient photocurrent in InP/InGaAs QWIPs.

### III. FREQUENCY-DEPENDENT RESPONSIVITY

The spatial distributions of the photoexcited electron ($\Gamma$, $L$, and $X$ electrons) concentrations at different moments cal- culated by the Monte Carlo method assuming (1)-(3) are

![](./images/812782272179601410_9.jpg)

FIG. 7. Responsivity vs signal frequency for AlGaAs/GaAs QWIPs.

![](./images/812782272179601410_10.jpg)

FIG. 8. Responsivity vs signal frequency for InP/InGaAs QWIPs.

shown in Figs. 2 and 3. Figure 2 demonstrates that in QWIPs with AlGaAs barriers at the initial stage almost all photoexcited electrons are concentrated in the $\Gamma$ valley. After a rather short period of time these photoelectrons that are accelerated in the electric field acquire high kinetic energy and transfer into $L$ and $X$ valleys. As it is seen in Fig. 2 for times t⩾0.2 ps the $L$ and $X$ electrons dominate and the photocurrent is associated primarily with the latter. In contrast, in InP-based QWIPs the role of the upper valleys is insignificant (see Fig. 3), at least at the biases under consideration. Such an effect is associated with relatively large intervalley separation in InP. This results in a higher value of the peak velocity $v_{\text{peak}}$ of the photoelectrons in InP/InGaAs QWIPs in comparison with AlGaAs/GaAs QWIPs (see Fig. 4).

![](./images/812782272179601410_11.jpg)

FIG. 9. Comparison of the frequency-dependent responsivity of AlGaAsand InP-based QWIPs.

The frequency-dependent responsivity $R(\omega)$ calculated using the Fourier transform of the dependencies of Figs. 5 and 6 for AlGaAs- and InP-based QWIPs are shown in Figs. 7 and 8. Their comparison (see Fig. 9) shows a higher value of $R(\omega)$ exhibited by InP/InGaAs QWIPs compared with AlGaAs-based QWIPs. The frequency-dependent responsivity for QWIPs with different periods of the QW structure $L$ and fixed number of the QWs $N$ is shown in Fig. 10. Figure 10 clearly demonstrates the increase of the responsivity with decreasing period of the QW structure (see also Fig. 11). However the validity of the obtained results is limited by not too small values of the QW structure period due to overlapping of the wave functions of neighboring QWs if their period (and consequently, spacing) becomes too small.

![](./images/812782272179601410_12.jpg)

FIG. 10. Responsivity vs signal frequency for AlGaAs/GaAs and InP/InGaAs QWIPs with different QW structure periods.

## IV. ANALYTICAL APPROXIMATION

Taking into account the fact that the behavior of the frequency-dependent responsivity $R(\omega)$ in the range of not too low frequencies is determined by the electron transit time and the velocity overshoot effect one may obtain:⁷

![](./images/812782272179601410_13.jpg)

FIG. 11. Responsivity as a function of the QW structure period at different fixed signal frequencies.

$$
R(\omega)=R_{0} N, \tag{4}
$$
if
$$
\omega<\tau_{t r}^{-1} \leqslant \tau_{o s}^{-1},
$$

$$
|R(\omega)| \simeq \frac{2 R_{0} N b}{1+\omega^{2} \tau_{t r}^{2}}, \tag{5}
$$

$$
\tau_{\mathrm{tr}}^{-1}<\omega \leqslant \tau_{\mathrm{os}}^{-1},
$$
and
$$
|R(\omega)| \simeq \frac{2 R_{0} N b}{1+\omega^{2} \tau_{\mathrm{os}}^{2}} \tag{6}
$$
in the range $\omega \geqslant \tau_{\mathrm{tr}}^{-1}$. Here $R_{0}=e \sigma \Sigma_{d} / 2 \hbar \Omega$ is the characteristic value of the QWIP responsivity, $\tau_{\mathrm{tr}}=W / v_{s}$ is the electron transit time across the QW structure, $\tau_{\text {os }}$ $=2.718\left(m v_{\text {peak }} / e E\right)$ is the characteristic time of the velocity overshoot effect, and $b=7.39 m v_{\text {peak }}^{2} / e E W$ $=14.78 \varepsilon_{\text {peak }} / e E W$, where $e$ and $m$ are the electron charge and effective mass (in the $\Gamma$ valley), $\hbar \Omega$ is the photon energy, and $\varepsilon_{\text {peak }}=m v_{\text {peak }}^{2} / 2$ is the peak kinetic energy.

Formula (2) can be rewritten as
$$
|R(\omega)| \simeq \frac{14.78 R_{0} \varepsilon_{\text {peak }}}{e L E} \cdot \frac{1}{1+\omega^{2} \tau_{\text {os }}^{2}}. \tag{7}
$$

It is seen from formula (7) that $|R(\omega)|$ increases with increasing $v_{\text {peak }}$ and decreasing $L$: $|R(\omega)| \sim \varepsilon_{\text {peak }} / L E$ and it does not depend on the number of the QWs. This is in good agreement with the results obtained using the Monte Carlo modeling (see, for example, Fig. 9).

Figure 11 demonstrates the calculated dependences of the frequency-dependent responsivity on the QW structure period $L$, which are also in agreement with formula (7).

The increase of $R(\omega)$ with decreasing $L$ is associated with the increase of the photoelectron contribution to the thermal (induced) current during the time when their velocity is large if $L$, and, consequently, the total width of the QW structure $W$, decreases ( $N$ is fixed). Thus, analytical formulas (4)-(7) yield a satisfactory approximation of the QWIP responsivity as a function of the signal frequency in the range of high values of the latter.

Using formula (7) one may estimate the characteristic value of the responsivity in the range of frequencies $\tau_{\mathrm{tr}}^{-1}$ $<\omega<\tau_{\text {os }}^{-1}$. Assuming $\hbar \Omega=0.1 \mathrm{eV}$ (so that for $\sigma=2$ $\times 10^{-15} \mathrm{~cm}^{2}$ and $\Sigma_{d}=10^{12} \mathrm{~cm}^{-2}$, one has $R_{0}=10^{-2} \mathrm{~A} / \mathrm{W}$ ), $L=55 \mathrm{~nm}, E=50 \mathrm{kV} / \mathrm{cm}$, and using the values for $\varepsilon_{\text {peak }}$ from Fig. 4, we obtain $|R| \simeq 0.05 \mathrm{~A} / \mathrm{W}$ and $0.06 \mathrm{~A} / \mathrm{W}$ for AlGaAs- and InP-based QWIPs, respectively.

One may estimate the gain-bandwidth efficiency product $^{15,16} G$ of QWIPs operating in the regime utilizing the velocity overshoot of the photoexcited electrons using formula (7) (i.e., ignoring the range of relatively low frequencies) as follows:
$$
G \sim R_{0} \frac{v_{\text {peak }}}{L}=G_{\text {os }}. \tag{8}
$$

Assuming $R_{0}=10^{-2} \mathrm{~A} / \mathrm{W}, \quad L=55 \mathrm{~nm}, \quad$ and $\quad v_{\text {peak }}=6$ $\times 10^{7} \mathrm{~cm} / \mathrm{s}$ from (8) one has $G_{\text {os }} \sim 100 \mathrm{~A} / \mathrm{W}$ GHz. Comparing the gain-bandwidth efficiency product due to the velocity overshoot effect $G_{\text {os }}$ and $G$ calculated taking into account the transit-time effect limitation we obtain
$$
\frac{G_{\text {os }}}{G} \sim \frac{v_{\text {peak }}}{v_{s}} \gg 1. \tag{9}
$$

These estimates show that the velocity overshoot effect can provide rather effective operation of QWIPs in the terahertz range of spectrum despite a relatively small absolute value of the frequency-dependent responsivity. This is primarily due to the very short characteristic time of the overshoot effect $\tau_{\text {os }}$ and coherent contribution of the electrons photoexcited from all QWs.

## V. CONCLUSION
An ensemble Monte Carlo particle method is used to study transient response and ultrahigh frequency performance of $n$-type AlGaAs/GaAs and InP/InGaAs QWIPs. It has been found that due to the velocity overshoot of the photoexcited electrons the photocurrent reveals very fast transient resulting in relatively large frequency-dependent responsivity in the terahertz region of spectrum. The estimates have shown that $n$-type AlGaAs/GaAs and, especially, InP/InGaAs QWIPs can be effectively used for heterodyne detection of infrared signals and generation of terahertz radiation.

${ }^{1}$ C. G. Bethea, B. F. Levine, G. Hasnian, J. Walker, and R. J. Malik, J. Appl. Phys. 66, 963 (1989).
${ }^{2}$ E. R. Brown, K. A. McIntosh, F. W. Smith, and M. J. Manfra, Appl. Phys. Lett. 62, 1513 (1993).

$^{3}$H. C. Liu, J. Li, E. R. Brown, K. A. McIntosh, K. B. Nichols, and M. J. Manfra, Appl. Phys. Lett. 67, 1594 (1995).

$^{4}$V. Ryzhii, I. Khmyrova, and M. Ryzhii, Jpn. J. Appl. Phys., Part 1 36, 2596 (1997).

$^{5}$V. Ryzhii, I. Khmyrova, and M. Ryzhii, IEEE Trans. Electron Devices 45, 293 (1998).

$^{6}$M. Ryzhii and V. Ryzhii, Appl. Phys. Lett. 72, 842 (1998).

$^{7}$M. Ryzhii, I. Khmyrova, and V. Ryzhii, Jpn. J. Appl. Phys., Part 1 37, 78 (1998).

$^{8}$M. Shur, *GaAs Devices and Circuits* (Plenum, New York, 1987).

$^{9}$J. Pozela, *Physics of High-Speed Transistors* (Plenum, New York, 1993).

$^{10}$B. F. Levine, J. Appl. Phys. 74, R1 (1993).

$^{11}$V. Ryzhii, J. Appl. Phys. 81, 6442 (1997).

$^{12}$K. F. Brennan, N. Mansour, and Y. Wang, Comput. Phys. Commun. 67, 73 (1991).

$^{13}$S. Adachi, *Physical Properties of III-V Semiconductor Compounds* (Wiley, New York, 1992).

$^{14}$J. M. Gerard, E. Deveaud, and A. Regeny, Appl. Phys. Lett. 63, 240 (1993).

$^{15}$J. E. Bowers and C. A. Barrus, J. Lightwave Technol. LT-5, 1339 (1987).

$^{16}$T. S. Moise, Y.-C. Kao, C. L. Goldsmith, C. L. Schow, and J. C. Campbell, IEEE Photonics Technol. Lett. 9, 803 (1997).
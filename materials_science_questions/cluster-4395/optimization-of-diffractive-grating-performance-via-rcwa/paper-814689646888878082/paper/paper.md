# The Extension of the Operation Frequency Range of the Resonant BWOs by Use of the Multistage Gratings

S.S. Ponomarenko, S.A. Kishko, E.M. Khutoryan, A.N. Kuleshov and B.P. Yefimov

Vacuum electronics department
O. Ya. Usikov Institute for Radiophysics and Electronics of NAS of Ukraine
Kharkiv, Ukraine
sergyponomarenko@gmail.com

Abstract—The problem of the operation frequency range extension in resonant BWO's is discussed. The methods of the multistage grating analysis are presented. The carried out theoretical and experimental investigations show the possibility of the broad band operation with low start currents at the $2^{nd}$ pass band of the 3-stage grating. The preliminary design of the slow-wave structure for operation at 220 GHz with 7 % frequency tuning range is carried out.

Index Terms—bakward wave oscillator, multistage grating, volume-surface waves, terahertz radiation.

## I. INTRODUCTION

Nowadays the terahertz radiation is applied in various branches of science and technology such as plasma diagnostics, dynamic nuclear polarization spectroscopy, THz imaging etc [1-3]. The table-top sources that could operate in wide frequency range with reasonable output power (0,1 – 1 W) is requested for these cases. Thus, the great potential for these applications have backward wave oscillators (BWO). But the capabilities of BWO’s in generation of medium-power coherent terahertz radiation is limited by several obstacles caused by fast decay of RF field from the grating surface and by high ohmic loses [4-6]. Hence the optimization of BWOs is focused on increasing of current density and optimization of the electro-dynamic system [7,8]. Besides the appreciable result in start current reduction and enhancement of output power are achieved in clinotrons [9,10,11] – a kind of resonant BWO [12,13].

In terahertz range the ohmic loses provides a dissipation of both forward harmonic reflected from the gun-end and backward one. Thus, the output power achieved in clinortons is limited by several hundreds milliwatts at 300 GHz [10]. Significant reduction of ohmic losses is achieved using volume modes of the open cavity in oscillators on diffraction radiation (DRO) and orotrons [14]. Similarly, the use of multistage gratings with leaky modes can reduce ohmic losses [15]. Also open multistage gratings may be used for optimization of RF output.

## II. CLINOTRONS WITH MULTISTAGE GRATINGS

Operation of electron beam with the self modes of a multistage grating is used to produce an extended quasi-optical output in clinotrons [16,17]. In opposite to uniform grating the dispersion curve of natural mode of the multistage grating splits up to several components $Q$ and has fast and slow harmonics in own spectrum. Thus, the energy transporting occurs by slow harmonics as well as fast one. Also the coupling impedance of natural harmonics of the multistage grating may be higher than that for uniform one. High radiation losses existing in clinotrons with quasi-optical output makes impossible the resonant excitation of the oscillator, causing increasing of start currents.

However, if the reflection plate is placed above the multistage grating it is possible to reach the conditions of the feedback loop by natural fast grating’s harmonic in additional to the loop by slow backward harmonic. The analysis of the oscillations excited at such system shows that the specific modes of volume-surface waves are possible [18]. It is reasoned by resonant transformation of the falling volume wave into the natural leaky wave of the multistage grating [19]. The localization of electric field both near the grating and at the space between the plate and the gating is inherent to these modes. Because of two channels of energy transporting it is possible to reduce the energy losses caused by surface effects during the operation in the terahertz frequency range. The operation rage from 0 to $\pi$ mode is achieved by displacement of the multistage grating at the cavity resonator.

![](./images/814689646888878082_1.jpg)

Figure 1. The waveguide system with a multistage grating with $Q$=5.

The theoretical analysis of the spectral properties of the proposed system is performed by mode matching technique. The basic parameters are shown in Fig. 1. The total field above the grating is expanded in Fourier series by spatial harmonics with period $L$ (1), and represented as the series of waveguide modes in slots (2). It is assumed, that the bunched electron beam with modulation frequency $\omega/2\pi$ moves above the grating with predetermined current density (3) and velocity $v_0$. The ohmic losses are simulated by the dielectric with predetermined $\tan\delta$ that is placed at the grating's slots.

The work was partly supported by Projects CRDF UKP1-9126-KH-13,
and the Project of the State Agency on Science, Innovations and
Informatization of Ukraine M/305-2013 and also RFBR 13-08-90910

$$
H_{x}=e^{i k_{0} y} \sum_{r=-\infty}^{\infty} A_{r} e^{i r \frac{2 \pi}{L} y} e^{i q_{r} z}
\tag{1}
$$

$$
H_{x}=\sum_{n=0}^{\infty} D_{n q} \sqrt{\varepsilon} \cos \sqrt{k^{2}-\left(\frac{n \pi}{d}\right)^{2}}\left(z+h_{p}\right)
\tag{2}
$$

were $\varepsilon$ - electric permittivity of the losses material in slots, $p=1 \ldots Q$, $y=q l \div q l+d$, $k_{0}=\omega / v_{e}$, $q_{r}=\sqrt{k^{2}-k_{r}^{2}}$, $k=\omega / c$, $k_{r}=k_{0}+r 2 \pi / L$.

$$
j=I_{0} \delta(z) e^{i\left(\frac{\omega}{v_{e}} y-\alpha t\right)}
\tag{3}
$$

were $\delta(z)$ - delta function, and amplitude $I_{0}$ is connected with
the beam current $I_{e}$ as $I_{0}=I_{e} e^{h_{e} a_{0}} \int_{a_{0}}^{a_{0}+a} e^{-h_{e} z} d z$. The coefficients of
field decomposition in the long wavelength assumption $(d<<\lambda)$
are defined by the method of reexpansion

$$
\begin{gathered}
\sum_{p_{0}=1}^{Q} D_{p_{0}}\left[\delta_{p}^{p_{0}} \cos \left(\sqrt{\varepsilon} k h_{p}\right)+\frac{k d}{L} \sin \left(\sqrt{\varepsilon} k h_{p_{0}}\right) ×\right. \\
\left.× \sum_{r=-\infty}^{\infty}\left(\frac{\sin \left(k_{r} d / 2\right)}{k_{r} d / 2}\right)^{2} \frac{e^{i k_{r}\left(p-p_{0}\right) l}}{\tan \left(q_{r} D\right) q_{r}}\right]=j_{0} e^{i p l}
\end{gathered}
\tag{4}
$$

Equation (4) transforms into the dispersion equation of the shielded multistage grating when right side is equal to zero. The power of interaction of the modulated electron beam with the fields that it exited is found as

$$
P=\int_{V} \vec{j}(t) \vec{E} e^{i \omega t} d V
\tag{5}
$$

where $E$ - is electric field, $V$ - volume of the electron beam. The power of interaction was estimated at resonant wave numbers $k$.

### A. 94-GHz clinorton with 3-stage grating

The $2^{\text {nd }}$ pass band of the 3-stage grating is assumed as the operation region of the proposed device. The geometrical parameters of the system are defined with respect to the frequency range of the $2^{\text {nd }}$ pass band and power of the electron beam-wave interaction. The dispersion curves for the system with $h=0.6 \mathrm{~mm}$, $h_{3}=0.78 \mathrm{~mm}$, $D=0.8 \mathrm{~mm}$, $l=0.28 \mathrm{~mm}$ are shown if Fig. 2. There are several operation modes possible at the $2^{\text {nd }}$ pass band: regime of surface mode $\left(v_{\mathrm{ph}}<0\right)$ and regime of volume-surface mode $\left(v_{\mathrm{ph}}>0\right)$. At the volume-surface mode operation the electro-mechanically frequency tuning about $10 \%$ is achieved by adjusting the reflection plate within $D=1.0 \ldots 3.0 \mathrm{~mm}$. The surface mode operation takes place at the beam velocities $0,094 c . .0,113 c$.

Certain operation zones could be observed because of the low dissipations of the waves reflected from the ends of the tube at this frequency range. The frequency tuning and interaction power were estimated for these zones according to the calculated resonant wave numbers. The calculation shows that the range of electronically frequency tuning for operation at surface mode is equal to $3 \%$ (Fig. 3) and practically not depended on parameter $D$. Numerical simulations performed by PIC code show the electronic efficiency about $10 \%$ in excitation of electromagnetic oscillations at $96.8 \mathrm{GHz}$.

![](./images/814689646888878082_2.jpg)

Figure 2. The dispersion diagram of self modes of the 3-stage grating
$D=0.8 \mathrm{~mm}, h_{3} / h_{1}=1.3$, beam lines with $v_{e}: 1-0,113 c, 2-0,108 c, 3-0,102 c$.

![](./images/814689646888878082_3.jpg)

Figure 3. Frequency tunning by accelerating volage for operating zones at
the $2^{\text {nd }}$ band pass of the 3-stage grating (surfase mode operation $v_{\mathrm{ph}}<0$ ).

### B. 220-GHz clinorton with 3-stage grating

Applying the methods described before, we have developed the slow-wave structure for the $220 \mathrm{GHz}$ application. The dimensions of the grating are $h_{3} / h_{1}=1.3$, $h=0.252 \mathrm{~mm}$, $l=0.135 \mathrm{~mm}$, $D=0.5 \mathrm{~mm}$. The calculated frequency dependence on beam velocity for operation zones is presented in Fig. 4. The appropriate power of interaction of the bunched electron beam with the fields of the operating zones is shown in Fig. 5. The results show that operation at the $2^{\text {nd }}$ pass band of the 3-

stage grating provides no gap operation frequency range about7 % at 220-GHz. The maximum value of the interaction power is reached at 218.5 GHz while the deviation of the interaction power from the maximum value does not exceed 60 %.

![](./images/814689646888878082_4.jpg)

Figure 4. Frequency tunning of the operating zones at the $2^{nd}$ band pass of the 3-stage grating. (for phase shift per period $l$ 4,188…5,235 rad only)

![](./images/814689646888878082_5.jpg)

Figure 5. Power of interaction with the operating zones at the $2^{nd}$ band pass of the 220 GHz 3-stage grating.

## III. EXPERIMENTAL STUDY OF THE SURFACE MODE

To investigate the physical effect of the frequency range extension by operation at high order pass bands of the multistage gratings the experiment with 94-GHz clinotron was carried out.

### A. Experrimental setup and metods

The Fig. 6 shows a schematic view of the experimental assembly. The oscillator under study has two waveguide outputs for the forward harmonic and backward one. Also, the diffraction output is applied for studying the fast harmonics of the surface-volume operation modes. The results of surface- volume modes investigation will be published soon.

The high perveance electron gun is used in the oscillator. It forms the sheet electron beam with cross section2.5 x 0.14 mm². The electron beam is focused by a laboratory magnetic system with magnetic induction 0.5 T. The beam voltage and current are 1-5 kV and 10-60 mA, correspondingly. Frequency measurements were made in a sine-pulsed mode of the accelerating voltage with 10-ms-long pulses with the repetition frequency 100 Hz. The output power was measured by comparing signals from a microwave diode powered by studied oscillator and by the bolometer in continuous mode.

![](./images/814689646888878082_6.jpg)

Figure 6. Schematic of the experimental system for the 94-GHz clinotron with 3-stage grating (1 - oscillator, 2 - directed coupler, 3 - microwave detectors, 4 - oscilloscopes, 5 - wavelegth meter, 6 - watt meter).

![](./images/814689646888878082_7.jpg)

Figure 7. Typical envelope of the output signal trace from the microwave detector. (1 - the first pass band of the 3-stage grating, 2 - oscillations related with the base uniiiform grating, 3 - the second pass band of the 3-stage grating)

### B. Result of the frequency analysys

The dispersion of the system under studying corresponds to surface mode operation ($D = 0.8$ mm). As it is shown in the Fig. 2 the volume waves do not cross the natural grating's modes and the regions of intertype coupling are absent. The excitation of the electromagnetic oscillations in the surface mode was observed at the all natural modes of the 3-stage grating at phase shifts per period $l$ close to $0.25 - 0.37\pi$. This

region corresponds to the optimal operation range of the clinotrons with uniform grating [10].

The typical envelope of the output signal of the oscillator is shown in Fig. 7. The appropriate operation modes are marked with the numbers. It should be mentioned that the electronical frequency tuning by the accelerating voltage at the range of 3.01 - 3.52 kV shows that there are no gaps at the frequency band of the second pass band of the studied 3-stage grating. The band width of this region is about 2.2 GHz that is close to calculated value. The excitation of the oscillation at the unexpected frequencies 89-93 GHz also was observed (region 2 in Fig. 7). This region corresponds to the electron beam interaction with the -1st spatial harmonic of the surface wave of the base uniform grating.

### C. Power characteristics
The starting currents for all operation modes are about 35-55 mA. The minimum values of the starting currents are achieved at the areas where the dispersion characteristic is kinked. That is explained by the high coupling impedance at these regions.

The dependence of output power on accelerating voltage and the operating frequency is shown in Fig. 8. The maximum output power of 560 mW is achieved at the 2nd pass band. The low level of excited oscillations is explained by small relation of the operation current to the start one (approximately 1.1), caused by non-stable operation of the electron gun at accelerating voltages higher than 2.5 kV. This characteristic shows that resonant excitation occurs at the 1st pass band (75-80.5 GHz). However the 2nd pass band has higher level of output power and smoothest frequency response.

![](./images/814689646888878082_8.jpg)

Figure 8. Results of the experemental mesurements of the operation frequency and output power.

### IV. SUMMARY
The operation frequency range about 2.3 % at the 96 GHz is achieved without gaps in surface mode operation at the clinotron with 3-stage grating. The proposed electrodynamic system provides lower starting currents than that is achievable at clinotrons with the extended quasi-optical output. The idea of frequency expansion by multistage grating is theoretically proved at sub-THz frequencies.

## ACKNOWLEDGMENTS
The authors gratefully acknowledge the technical support and useful discussion of V. V. Zavertanniy, A. F. Zabrodsky, L. A. Kirichenko, T. V. Kudinova and I. V. Lopatin.

## REFERENCES
[1] G. Gruner, "Millimeter an submillimeter wave spectroscopy of solids," Berlin Heidelberg: Springer- Verlag, 1998.
[2] G.A. Komandin et.al., "BWO Generators for THz Dielectric Measurements," IEEE Trans. Terahertz Science And Tech., vol. 3, no. 4. pp.440-444, 2013.
[3] P. Siegel, "THz technology: An overview," Int. Journal of High Speed Electronics and Systems, vol. 13, no. 2. – pp. 351-394, 2003
[4] R. J. Temkin, "Vacuum electronic high power terahertz sources," IEEE Trans. Terahertz Science And Tech., no. 1, pp. 54, 2011.
[5] Yun-Shik Lee, "Principles of Terahertz Science and Technology," Springer, 2009.
[6] J. H. Booske et al., "Plasma physics and related challenges of millimeter-wave-toterahertz and high power microwave generation," Phsys. Plasmas, vol. 15, no. 5., 055502, January 2011.
[7] M. Mineo and C. Paoloni, "Double Corrugation Rectangular Waveguide Slow-wave Structure for THz Vacuum Devices," IEEE Trans. Electron Devices, vol. 57, no. 11, pp. 3169-3147, November 2010.
[8] S. Bhattacharje, J.H. Booske, C.L. Kory, D.W. van der Weide, S. Limbach, S. Gallagher, J.D. Welter, M.R. Lopez, R.M. Gilgenbach, R. L. Ives, M.E. Read, R. Divan, D.C. Mancini, "Folded Waveguide Traveling-Wave Tube Sources for Terahertz Radiation," IEEE Trans. on Plasma Science,. vol. 32, no. 3., pp. 1002-1014, 2004.
[9] K. Schunemann and D. M. Vavriv, "Theory of the clinotron: A grating backward-wave oscillator with inclined electron beam," IEEE Trans. Electron Device, vol. 46, no. 11, pp. 2245-2252, November 1999.
[10] G.Ya.Levin, A.I. Borodkin, A.Ya. Kirichenko, S.A Churilova, A.Ya. Usikov, "Clinotron", Kyiv: Nanukova dumka, 1992. (in Russian)
[11] S.S. Ponomarenko S.A. Kishko, E.M. Khutoryan, A.N. Kuleshov,V.V. Zavertanniy, I.V. Lopatin, B.P. Yefimov, "400 GHz Continuous-Wave Clinotron Oscillator," IEEE Transactions on Plasma Science, vol. 41, no 1., pp. 82 – 86, 2013.
[12] G.S. Nusinovich, Yu.P. Bliokh, "Mode Interaction in Backward-Wave Oscillators with Strong End. Reflections", Phys. Plasmas, Vol. 7, No.4, pp.1294-1301, 2000
[13] B. Levush, T.M. Antonsen, A. Bromborsky, W.R. Lou, Y. Carmel, "Theory of relativistic backward wave oscillator with end reflections," IEEE Trans. Plasma Sci., Vol.20, No.3, pp.263-280, 1992.
[14] V. L. Bratman, et. al., "Terahertz orotrons and oromultipliers," IEEE Trans. on Plasma Sci., vol.38, no. 6, pp. 1466-1471, June 2013.
[15] R. A. Silin, V. P. Sazonov, "The Slow-wave structures," Moscow: Izd. Sov. Radio, 1966. (in Russian)
[16] E.E. Lysenko, O.F. Pishko, S.A. Churilova, "Experimental investigation of the clinotron with extended evasioptic output,," Radiophysics and radioastronomy, vol.4, no. 1, pp. 13-19, 1999. (in Russian)
[17] D.M. Vavriv, "Potential of the Clinotron for THz Generation", AIP Conf. Proc., vol. 807, pp.367-372, 2006.
[18] E. M. Khutoryan, S. S. Ponomarenko, S. A. Kishko, A. N. Kuleshov, K. A. Lukin, B. P. Yefimov, "Autooscillations in O-type oscillator at excitation of space-surface mode in resonator with a periodically inhomogeneous grating," Izvesiya VUZov. Applied nonlinear dynamics, vol.21, no. 2, pp. 9-19, 2013. (in Russian)
[19] V.P. Shestopalov, Yu.K. Sirenko, "The Dynamic theory of gratings," Kiev: Nauk. Dumka, 1989. (in Russian)
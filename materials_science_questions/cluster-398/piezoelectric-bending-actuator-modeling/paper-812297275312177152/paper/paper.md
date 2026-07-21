# The Transfer Function of the Thin Shell PZT Ceramic Cylinder as a Phase Modulator in Fiber Optic Sensors

Wuu-Wen Lin\*, Sung-Tsun Shih\*\*, Mao-Hsiung Chen\*\*, and Shih -Chu Huang\*\*

*: Chung-Shan Institute of Science and Technology
P. O. Box 90008-19, Tso-Ying, Kao-Hsiung, Taiwan, ROC

**: National Sun Yat-Sen University
Department of Electrical Engineering, National Sun Yat-
Sen University, Kao-Hsiung, Taiwan, ROC

## ABSTRACT

An optical fiber PZT cylinder phase modulator is frequently used in an optical fiber interferometric sensor for demodulating sensing singals. In this paper, we combine the piezoelectric equations and the fiber phase shift relations to deliver a thorough description of the phase response of the optical fiber PZT cylinder phase modulator. We also design an experiment to verify our derivation. The results is quite compatible with published data.

## 1.INTRODUCTION

Fiber optical interferometric sensors, having the advantages of geometric versatility of the sensing element, wide dynamic range and high sensitivity, do not suffer from electromagnetic wave interference. Those sensors are generally useful for measuring sound¹, temperature², pressure, rotation³⁴⁵ and magnetic field³⁴ etc.. Among the components of a fiber optical interferometric sensor, the phase modulator is frequently adopted for demodulating interferent sensing signal.

There are many kinds of fiber phase modulator, for example, PZT phase modulator³, optical guide wave phase modulator, PVDF modulator¹⁰ etc.. Among these PZT phase modulators, the cylindrical shell type is quite popular. It is attributed to their geometric simple, easily manfacturing, and cheapness. Except that, the wide dynamic range makes it extremely useful in stability controller¹⁰.

Because that the previous publication¹⁰ does not have a thorough description of the transfer function of the PZT cylindrical thin shell phase modulator, we are interesting in deriving this transfer function. Our approach is by considering the interaction between the vibration mode of the PZT ceramic and the sensing mechanism of optical fiber. Moreover, the frequency response, phase delay, and output voltage can be solved accordingly. Some experimental data are shown for comparison with the theoretic results.

The advantages and disadvantages of using such a hollow PZT ceramic cylinder will also be discussed.

## 2.TRANSFER FUNCTION OF A PHASE MODULATOR

The fiber-wound mandrel modulator is of interest due to its ease of fabracation and its high sensitivity. It is made by winding the fiber tightly around a hollow cylindrical piezoelectric ceramic, for example PZT. Assuming that the fiber phase response is solely driven by the mandrel response, it is clear that a circumferential change of the mandrel couples directly to a length change of the fiber. Since the circumferential change of the mandrel is directly proportional to its radial change, the radial strain induced in this PZT mandrel by the electric field must be calculated first.

For radially symmetric mode in thin ceramic rings, assume the electroded surface form an equipotential surface between inner and outer surfaces, as shown in Fig.1(a). We have

$$E_1 = E_2 = 0\ ;\ E_3 = E$$

$$T_2 = T_3 = 0\ ;\ T_1 = T$$

From Piezoelectric equation⁷·⁸ :

$$S_1 = C_{11}^E T_1 + d_{31} E_3 \tag{1}$$

$$D_3 = d_{31} T_1 + \epsilon_{33}^T E_3 \tag{2}$$

where $S_1$ and $T_1$ are the strain and stress in the circumferential direction, $D_3$ and $E_3$ are the displacement and electric field in the radial direction, $C_{11}^E$ is the modulus of elasticity, $d_{31}$ is the piezoelectric constant, and $\epsilon_{33}^T$ is the dielectric constant. From the force diagram, as shown in Fig.1(b), we have

$$F_x = (2F)\ (\frac{1}{2} \delta\theta) = F\delta\theta = T_1 t\Delta h\delta\theta \tag{3}$$

From Newton's second law,

$$
\rho t \Delta h r \delta \theta \frac{\partial^{2} \xi}{\partial t^{2}}=-T_{1} t \Delta h \delta \theta
$$
(4)

where $\rho$ is the density of PZT, $r$ is the mean radius, $t$ is the thickness of the cylinder, $\xi$ is the radial displacement. Since the circumferential change is directly proportional to the radial change, the circumferential strain is equal to the radial strain. We have

$$
S_{1}=\frac{\xi}{r}
$$
(5)

From (1) and (4), after some manipulation, the equation for the radial displacement under an applied electric field can be expressed as :

$$
\frac{\partial^{2} \xi}{\partial t^{2}}+\frac{1}{\rho r^{2} C_{11}^{E}} \xi=\frac{1}{\rho r} \frac{d_{31}}{C_{11}^{E}} E_{3}
$$
(6)

For free loading ring $(E_{3}=0)$, the resonant angular frequency $\omega_{0}$ will be

$$
\omega_{0}^{2}=\frac{1}{\rho r^{2} C_{11}^{E}}=\frac{\left(V_{1}^{E}\right)^{2}}{r^{2}}
$$
(7)

where $V_{1}^{E}$ is the longitudinal wave velocity, and

$$
\left(V_{1}^{E}\right)^{2}=\frac{1}{\rho C_{11}^{E}}
$$
(8)

If the damping of the ceramic is considered, then (6) can be rewritten as

$$
\frac{\partial^{2} \xi}{\partial t^{2}}+\frac{\alpha}{m} \frac{\partial \xi}{\partial t}+\frac{1}{\rho r^{2} C_{11}^{E}} \xi=\frac{d_{31}}{\rho r C_{11}^{E}} E_{3}
$$
(9)

where $\alpha$ and $m$ are damping coefficient and mass of the ceramic respectively. Let the driving field be harmonic, i.e., $E_{3}=E_{\mathrm{o}} e^{j \omega t}$. Then, the steady state solution of the displacement $\xi$ can be solved as

$$
\xi=\frac{1}{\left(\omega_{0}^{2}+j \frac{\omega \alpha}{m}-\omega^{2}\right)} \frac{d_{31}}{\rho r C_{11}^{E}} E_{3}
$$
(10)

From the definition of mechanical quality factor,

$$
Q = \frac{\omega_{0}m}{\alpha} \tag{11}
$$

We have

$$
\xi = \frac{1}{\left(\omega_{0}^{2} + j\frac{\omega\omega_{0}}{Q} - \omega^{2}\right)} \frac{d_{31}}{\rho r C_{11}^{E}} E_{3} \tag{12}
$$

Assume $\phi$ is the optical phase of light propagating through a fiber, then $\phi$ may be defined in terms of the wave propagation constant $\beta$, and length of the fiber L, that is, $\phi = \beta\text{L} = \text{nkL}$, where k is the wave number of the light beam in free space. Hence, the phase change of light in fiber can be represented by

$$
\Delta\phi = \beta\Delta L + L\Delta\beta \tag{13}
$$

where the first term represents the effects of the physical change of length due to the strain, that is, $\Delta\text{L}$ $= \epsilon_{z}\text{L}$, the second term comes about from two effects: the strain-optic effect whereby the strain changes the refraction index n of the fiber, and a waveguide mode dispersion effect due to a change in fiber diameter D produced by the strain, that is$^{2,6}$

$$
L\Delta\beta=L\frac{d\beta}{dn}\Delta n+L\frac{d\beta}{dD}\Delta D \tag{14}
$$

The change in the waveguide mode propagation constant due to a change in fiber diameter, can be negligible compared with the first term.$^{2}$ Thus, the phase change can be expressed as$^{2,5,6}$

$$
\frac{\Delta\phi}{\phi} = \epsilon_{z} - \frac{n^{2}}{2}\left[(P_{11} + P_{12})\epsilon_{r} + P_{12}\epsilon_{z}\right] \tag{15}
$$

where, $P_{11}$ and $P_{12}$ are the elasto-optic coefficients of the core, $\epsilon_{r}$ and $\epsilon_{z}$ are the radial strain and longitudinal strain, respectivity. By the definition of Poisson's ratio$^{9}$, (15) resulting in

$$
\Delta \phi=\epsilon_{z}\left\{1+\frac{n^{2}}{2}\left[\left(P_{11}+P_{12}\right) \mathrm{v}-P_{12}\right]\right\} \phi \tag{16}
$$

where $\nu$ is the Poisson's ratio of the fiber. Since the fiber core axial strain $\epsilon_{z}$ is the same as the mandrel circumferential strain $S_{1}=\xi / \mathrm{r}$. From (12) and (16), we have

$$
\frac{\Delta \phi}{E}=\frac{\left\{1+\frac{n^{2}}{2}\left[\left(P_{11}+P_{12}\right) \mathrm{v}-P_{12}\right]\right\} d_{31}}{\left(\omega_{0}^{2}+j \frac{\omega \omega_{0}}{Q}-\omega^{2}\right) \rho r^{2} C_{11}^{E}} \frac{2 \pi}{\lambda} n L \tag{17}
$$

For equipotential condition, $\mathrm{E}=\mathrm{V} / \mathrm{t}$, then

$$
\frac{\Delta \phi}{V}=\frac{\Delta \phi}{E \cdot t}=\frac{\left\{1+\frac{n^{2}}{2}\left[\left(P_{11}+P_{12}\right) \mathrm{v}-P_{12}\right]\right\}}{\left(\omega_{0}^{2}+j \frac{\omega \omega_{0}}{Q}-\omega^{2}\right)} \frac{d_{31}}{\rho r^{2} C_{11}^{E} t} \frac{2 \pi}{\lambda} n L \tag{18}
$$

The delay angle of the PZT phase response can be derived from the complex term in (18), that is

$$
\tau=-\tan ^{-1} \frac{\omega \omega_{0}}{Q\left(\omega_{0}^{2}-\omega^{2}\right)} \tag{19}
$$

The phase delay angle would be $-90^{\circ}$ at resonant frequency. For low frequency, that is $\omega \ll \omega_{0}$, Equation (18) can be simplified to

$$
\frac{\Delta \phi}{V}=\frac{2 \pi}{\lambda t} n L d_{31}\left\{1+\frac{n^{2}}{2}\left[\left(P_{11}+P_{12}\right) \mathrm{v}-P_{12}\right]\right\} \tag{20}
$$

The transfer function $\mathrm{G}_{\mathrm{pm}}(\mathrm{S})$ of the PZT phase modulator can be obtained by replacing $\omega^{2}$ with $-\mathrm{S}^{2}$ in (18) as following:

$$
G_{p m}(S)=\frac{\left\{1+\frac{n^{2}}{2}\left[\left(P_{11}+P_{12}\right) \mathrm{v}-P_{12}\right]\right\} d_{31}}{\left(\omega_{0}^{2}+\frac{S \omega_{0}}{Q}+S^{2}\right) \rho r^{2} C_{11}^{E} t} \frac{2 \pi}{\lambda} n L \tag{21}
$$

For Mach-Zehnder fiber interferometer, the operation frequency always far below the resonant

frequency of the PZT mandrel. Since $\omega_0 \gg |S|$ and from (7), $\mathrm{G}_{\mathrm{pm}}(\mathrm{S})$ can be simplified without dependence on $\mathrm{S}$ :

$$
G_{p m}=\frac{2 \pi}{\lambda t} n L d_{31}\left\{1+\frac{n^{2}}{2}\left[\left(P_{11}+P_{12}\right) v-P_{12}\right]\right\} \tag{22}
$$

In the demodulation system of Mach-Zehnder interferometer, if the operation frequency near the resonant frequency of the PZT phase modulator, the electrical circuit would be resonated. But for some other interferometer ( for example, Sagnac) or for some other reasons if a fixed frequency or phase is needed, the frequency near or even higher than the resonant frequency of the PZT phase modulator maybe used. In those cases, eqs.(18) could be applied.

### 3.EXPERIMENT

In order to verify the above derivation, we design an experimental case. The basic principle for using a Mach-Zehnder interferometer to measure this PZT fiber phase modulator response is stated as following :

At first, a phase signal $\mathrm{C} \cdot \cos \omega_{\mathrm{o}} \mathrm{t}$ is generated on the phase modulator by HP3562A Dynamical signal generator, then the output interferent signal of the Mach-Zehnder interometer can be written as $^{11}$

$$
I=A+B \gamma \cos \left(C \cos \omega_{o} t+\phi(t)\right) \tag{23}
$$

where the constant $\mathrm{A}$ and $\mathrm{B}$ are proportional to the input optical power. The mixing efficiency $\gamma$ is dependent on the polarization state (its variation is called polarization fading). $\phi(t)$ is the phase difference between the signal and reference arms. The Equation (23) can be expanded as $^{11}$

$$
\begin{aligned}
I=A & +B \gamma\left\{\left[J_{o}(C)+2 \sum_{k=1}^{\infty}(-1)^{k} J_{2 k}(C) \cos 2 k \omega_{o} t\right] \cos \phi(t)\right. \\
& \left.-\left[2 \sum_{k=0}^{\infty}(-1)^{k} J_{2 k+1}(C) \cos (2 k+1) \omega_{o} t\right] \sin \phi(t)\right\}
\end{aligned} \tag{24}
$$

When the variable $\mathrm{C}$ is increased gradually until $\mathrm{C}$ equals to $3.054^{12}$, the amplitude of the harmonic components $\omega_{0}$ and $3 \omega_{0}$ are equal, that is, $\mathrm{J}_{1}(\mathrm{C})=\mathrm{J}_{3}(\mathrm{C})$. $\mathrm{C}$ is changed proportional to the variation of $\phi(t)$. Based on this characteristic, the response of the phase modulator can be measured. The instrumental layout of this experiment is shown in Fig.2.

The Mach-Zehnder fiber interferometer is organized by a GaAlAs single longitudinal mode laser

diode from the Laser Diode Inc., single mode fiber (outer diameter 0.23mm) and couplers from York Inc., single mode fiber polarization controller and a PZT phase modulator also. The end of the fiber was cut to $6^{\circ}$ skew angle in order to avoid reflection. The output optical signal is transfered to electrical signal by a 1500XP optical waveform analyzer from Photodyne Inc.. The HP3562A Dynamical signal analyzer was used as a signal generator and spectrum analyzer for the analysis of the interferent signals. The Tektronix 7854 Oscilloscope was used as an instrument for testing the output signal voltage and as a monitor for the interferent signal.

The procedure of the experiment is stated as following: An sinusodial signal $Ucos\omega_{0}t$ was generated by the HP3562A, the amplitude U was increased gradually until the interferent signals of the components $\omega_{0}$ and $3\omega_{0}$ are equal, then from the readout on HP3562A, recording the output signal peak to peak voltage value $V_{\omega(p-p)}$, then the amplitude U would be half the value of $V_{\omega(p-p)}$. In this case, the phase response $G_{pm}(\omega)$ at angular frequency $\omega$ on the phase modulator should be

$$
G_{pm}(\omega)=\frac{3.054}{U}=\frac{6.108}{V_{\omega(p-p)}} \quad rad/volt \tag{25}
$$

In our experiment, there are two samples of PZT phase modulator. Sample I is made of PZT-4 with outer diameter OD=1.5", thickness t=0.19cm and height h=2.54cm as the mandrel. Sample II is made of PZT-5A with outer diameter OD=1.5", thickness t=0.326cm, and height h=5.7cm as the mandrel. The fiber was wrapped around the PZT ceramic shell to form a phase modulator as shown in Fig.1(a). The theoretical data are compared with the experimental results which are shown in Fig.3 (for sample I), and Fig.4 (for sample II).

### 4.DISCUSSION

For low frequency, the theoretical value of the response of the phase modulator will be

$$
\begin{aligned}
G_{pm}\ (\omega < \omega_{0}) &= 0.068\ rad/(volt-turn) && \text{for Sample } I\ (PZT-4) \\
&= 0.055\ rad/(volt-turn) && \text{for Sample } II\ (PZT-5A)
\end{aligned}
$$

and the measured value will be

$$
\begin{aligned}
G_{pm} &= 0.051\ rad/(volt-turn) && \text{for Sample } I \\
&= 0.043\ rad/(volt-turn) && \text{for Sample } II
\end{aligned}
$$

which are very close to the data 0.06-0.08 radian/(volt-turn) for PZT-5H reported in De Paula's paper¹⁰. The difference between theoretical and experimental results may attribute to the following reasons:

(1) Epoxy that stick those fiber on the PZT mandrel is not rigid.
(2) Aging rate of the PZT used, so that $d_{31}$ is smaller than that given on data sheet.
(3) The compliant effect of the plastic jacket of the fiber.

In De paula's paper¹⁰, the phase response of a PZT cylinder modulator was expressed as

$$
\phi=2 \pi k_{0} n V N d_{33}\left\{1-\frac{n^{2}}{2}\left[p_{11}-\left(p_{11}+p_{12}\right) v\right]\right\}
$$

which does not show the dependence on the fiber length and the thickness of the PZT cylinder. However, in our study, we combine PZT piezoelectric equations and fiber phase shift relation to a result shown in Equation (18). In which we found that the piezoelectric constant should be $d_{31}$ instead of $d_{33}$.

In our study, these size of PZT phase modulator with 100 turns of optical fiber and $\pm 15 \mathrm{~V}$ driving voltage can deliver up to $\pm 105$ radians of optical phase shift. If this PZT-5A is replaced by a PZT-5H, then \pm 150 radians is expectable, which is comparable with that mentioned in De paula's paper¹⁰.

Because of this wide dynamic range of phase shift, it makes the PZT phase modulator extremely useful for the optical interferometric sensors. However, in our experiment, we found that if the largest diamension of the PZT shell were not larger than 2 times of the other two diamensions, then, there would be some coupling among vibrated modes of this PZT shell. If this coupling phenomena were induced, then the operation frequencies of the optical sensor will be limited.

## 5.CONCLUSION

The optical fiber PZT cylindrical phase modulator has the advantage of wide dynamic range, easily manifacturing which has attributed a lot of attention in the past. Although Roman's approach is quite helpful, our formulae shown that two more factors including length of fiber and thickness of PZT cylinder should be considered, also, the piezoelectric constant $d_{31}$ is better to explain the physical phenomena of this device. Our experiments have verified this viewpoint.

## 6. ACKNOWLEDGMENTS

One of the authors (Lin) wishes to thank Chung-Shan Institute of Science and Technology for financial support. The others would like to express their appreciation for sharing the resources and facilities from National Sun-Yat Sen University.

### 7.REFERENCE

1. J. A. Bucaro and T. R. Hickman, "Measurement of sensitivity of optical fibers for acoustic detection," Applied Optics, Vol. 18, No. 6, pp. 938-940, Mar. 1979.

2. G. B. Hocker, "Fiber-optic sensing of pressure and temperature," Applied Optics, Vol. 18, No. 9, pp. 1445-1448, May 1979.

3. T. G. Giallorenzi, J. A. Bucaro, A. Danaridge, G. H. Sigel "Optical fiber sensor technology," IEEE J. of Quan. Elec., Vol. QE-18, No. 4, pp. 626-665, April 1982.

4. A. Dandridge and A. D. Kersey, "Overview of Mach-Zehnder sensor technology and applications," SPIE Vol. 985, Fiber Optic and Laser Sensors VI, pp. 34-52, 1988.

5. J. A. Bucaro, N. Lagakos, J. H. Cole, and T. G. Giallorenzi, "Fiber optic acoustic Transduction," in Physical Acoustics, Vol. 16, pp. 385-457, (Academic Press, N.Y.) 1982.

6. G. B. Hocker, "Fiber optic acoustic sensors with composite structure : an analysis," Applied Optics, Vol. 18, No. 21, pp. 3679-3683, Nov. 1979.

7. D. A. Berlincourt, D. R. Curran, and H. Jaffe, "Piezoelectric and Piezomagnetic materials and their function in transducers," in Physical Acoustics, Part A1, pp.170-267, 1964.

8. J. F. Nye, Physical Properties of Crystals, Chap.8 Clarendon Press, Oxford, 1985.

9. S. P. Timoshenko and J. N. Goodier, Theory of Elasticity, Chap. 4, McGraw-Hill, New York, 1970.

10. R. P. De Paula and E. L. More, "Review of all-fiber and Polarization modulators," SPIE Vol.478, Fiber Optic and Laser Sensors II, pp. 3-11, 1984.

11. A. Dandridge, A. B. Tveten and T. G. Giallorenzi, "Homodyne demodulation scheme for fiber-optic sensor using phase generated carrier," IEEE J. Quantum Electron., Vol. 18, p.1647, 1982.

12. S. C. Huang, Unpublished data.

![](./images/812297275312177152_1.jpg)

Fig. 1. (a) The configuration of a PZT phase modulator, (b) The force diagram of a PZT ceramic shell.

![](./images/812297275312177152_2.jpg)

Fig. 2. The experimental layout for measurement of the response of the phase modulator.

![](./images/812297275312177152_3.jpg)

Fig. 3. The experimental data and theoretically caculated results for Sample I (PZT-4).

![](./images/812297275312177152_4.jpg)

Fig. 4. The experimental data and theoretically caculated results for Sample II (PZT-5A).
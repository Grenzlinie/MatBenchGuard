# Phase characteristics of thick metal gratings

A.D.Chuprin
E.A.Parker
A.D.Shatrov
A.N.Sivov
V.S.Solosin
A.S.Zubov
R.J.Langley

Indexing terms: Antennas, Electromagnetic waves, Filters, Frequency selective surfaces

**Abstract:** A theoretical and experimental study of the phase characteristics of thick conducting gratings is presented. The frequency and angular behaviour of the reflection coefficient phase is investigated. Depending on the cross-section of the conductors, the grating periodicity can be chosen such that, over a wide frequency range, the phase of the reflection and transmission coefficients remains constant. Angular dependence of the reflection and transmission coefficients for these gratings also disappears within this frequency range. The phenomenon occurs only for the case with the electric vector parallel to the grating conductors.

## 1 Introduction

Thick infinite gratings of parallel conductors have been studied extensively over the last few decades [1]. The gratings are known to demonstrate essentially different features for different orientations of the electric vector of linearly polarised incident waves. Electromagnetic waves with the electric vector parallel to the conductors are referred to here as E-polarised waves. Special atten- tion is paid to the case of diffraction from a thick metal grating over the frequency range below the onset of the first grating mode. In this paper, we show that, for the low-frequency range, the phase of the diffracted E-polarised wave can behave quite unexpectedly for a special choice of grating parameters. For a given shape of the grating conductors, an appropriate set of the grating geometrical parameters exists such that the phases of the reflection and transmission coefficients are independent of the frequency and the incident angle, or at least depend much less than for any other set of grating parameters. Moreover, the phase shift for the transmitted wave is $90^{\circ}$ and for the reflected wave $180^{\circ}$; the same as for a metal plate if the reference plane coincides with the symmetry plane of the grating conductors.

This phase independence phenomenon was first described as a hypothesis [2, 3]; it was empirically found that, in a quasistatical approach, for some grat- ing parameters the frequency and angular dependence of the phase disappears completely. It was also assumed that this could occur for any shape of metal grating conductors. Some numerical estimations of the grating geometry for several conductor shapes were presented. However, no rigorous calculations nor meas- urements were performed to verify this hypothesis, and no satisfactory explanation of the phenomenon was provided.

In this paper, the electromagnetic problem is formu- lated and methods of its solution are briefly discussed. The phase behaviour is investigated first for low fre- quencies using an equivalent-circuit approach [4]. This provides a simple, but very useful, explanation of the phenomenon and is a technique for obtaining the grat- ing geometry of interest. The frequency and angular behaviour of the phase characteristics of diffracted E- polarised plane electromagnetic waves for various thick gratings is studied in detail, using well known rigorous numerical techniques such as the multiple-scattering technique [5, 6], method of integral equations [7], and a mode-expansion method [8]. Measurement results for the reflection coefficient phase of a normally incident wave over a wide frequency range are also presented, and possible applications of this phase behaviour are discussed.

## 2 Problem formulation and equivalent-circuit description

### 2.1 Problem formulation and methods of solution
Consider the diffraction of a plane electromagnetic wave incident at an angle $\Theta$ on an infinite grating com posed of parallel conductors, with the electric vector of the incident wave parallel to the conductors, as in Fig. 1. Since there is no z-dependence, the problem is two- dimensional. In this study, we are only interested in the case when the wavelength $\lambda$ is greater than $p/2$. This means, in particular, that outside the local wave region, only the zeroth order mode arises, i.e. we restrict our- selves here to only the specular mode situation. The problem is easy to solve numerically for several simple

© IEE, 1998
IEE Proceedings online no. 19982244
Paper first received 22nd September 1997 and in revised form 22nd June 1998
A.D. Chuprin is with the Electronic Engineering Laboratory, UKC and the Institute of Radio Engineering and Electronics, RAS
E.A. Parker and R.J. Langley are with the Electronic Engineering Labo- ratory, University of Kent, Canterbury, Kent, CT2 7NT, UK
A.D. Shatrov, A.N. Sivov, V.S. Solosin and A.S. Zubov are with the Institute of Radio Engineering and Electronics of Russian Academy of Sciences, 1 Vvedenskogo squ., Fryazino, Moscow, 141120 Russia

IEE Proc.-Microw. Antennas Propag., Vol. 145, No. 5, October 1998

shapes of cross-section, in particular circular and rectangular, using the methods mentioned above [5-8]. For an arbitrary cross-section, we can use, for instance, the integral-equation [7].

![](./images/812756031770722308_1.jpg)

Fig.1 Geometry of array of conductors of arbitrary cross-section

Calculations have been performed for both circular and rectangular conductor shapes. Each case has been evaluated by at least two independent methods: the multiple-scattering technique for circular conductors, the mode-expansion method for rectangular ones, and the integral-equation technique for both shapes. Comparisons with other work [1, 5, 7, 8] have been made. All the test results were in very close agreement with each other and with the references cited above. A comparative example is presented in Section 3. First, however, we focus on a simplified but very useful long-wave approximation, i.e. the case where $p << \lambda$.

![](./images/812756031770722308_2.jpg)

Fig.2 Equivalent circuit for array of conducting rods at low frequencies

### 2.2 Equivalent circuit
Fig. 2 shows the equivalent circuit for a grating composed of elliptical or rectangular conductors, illuminated by an E-polarised plane wave within the long-wave frequency range [4]. With this circuit representation, the reflection coefficient (at the reference plane $y = 0$) from such a grating has the form

$$
R = A + jB(X_a - X_b) \tag{1}
$$

where $A$ and $B$ are finite real values defined by the grating geometry. Expressions for the normalised values of $X_a$ and $X_b$ for inductive gratings composed of elliptical (including circular) or rectangular conductors are given elsewhere [4]:

$$
X_a \simeq \frac{p \cos \Theta}{\lambda} \left[ \ln \frac{p}{2 \pi r_0} + 0.601 \left(3 - 2 \cos^2 \Theta \right) \left( \frac{p}{\lambda} \right)^2 \right] \tag{2}
$$

$$
X_b = \frac{p \cos \Theta}{\lambda} \left( \frac{2 \pi r_1}{p} \right)^2 \tag{3}
$$

where $r_{0,1}$ depend only on the grating geometry. For $p << \lambda$, the second term in the square brackets in eqn. 2 vanishes. If we require

$$
X_a - X_b = 0 \tag{4}
$$

the reflection coefficient (eqn. 1) becomes real. The phase of the reflection coefficient becomes $\pi n$, $n = 0, \pm 1, \pm 2, \dots$ and is therefore frequency-independent. It follows from eqns. 2 and 3, taking into account $p << \lambda$, that

$$
X_a - X_b = \frac{p \cos \Theta}{\lambda} \left[ \ln \frac{p}{2 \pi r_0} - \left( \frac{2 \pi r_1}{p} \right)^2 \right] \tag{5}
$$

The expression in the square brackets includes only parameters of the grating geometry. When they are chosen so that this expression becomes zero, the entire imaginary part of the reflection coefficient disappears for all wavelengths and incident angles.

## 3 Numerical and experimental results

Before discussing the numerical results and examining how far in frequency the phenomenon extends, it would be helpful to recall the 'conservation of phase' theorem [9]: this implies that for any grating composed of conductors that are symmetrical relative to a reference plane ($y = 0$ in our case), the reflected and transmitted waves are always $90^\circ$ out of phase. Thus, we need deal with only one of the phases $\varphi_R$ or $\varphi_T$.

The simplest way to obtain the grating geometry of interest is to solve the transcendental equation

$$
\ln \frac{p}{2 \pi r_0} - \left( \frac{2 \pi r_1}{p} \right)^2 = 0 \tag{6}
$$

where the parameters $r_{0,1}$ [4] depend on the cross-section shape chosen. However, it turns out to be easier to calculate the geometry directly using computer codes for the grating diffraction problem, based on an appropriate technique [5-8]. We choose an incident angle, e.g. $\Theta = 0$ (normal incidence), a reasonably small ratio of $p/\lambda$, e.g. 0.1, and any desirable value of the normalised conductor thickness $t/p$. Then, varying the aspect ratio (AR) $w/p$ (conductor width normalised to the period) from 0 to 1, and observing the phase behaviour (either $\varphi_R$ or $\varphi_T$), gives the optimal value of $w/p$ that corresponds to the case $\varphi_R = 180^\circ$ (or $\varphi_T = 90^\circ$).

The calculations have been performed for two kinds of gratings; circular metal cylinders and rectangular rods. The conductors are taken to be lossless. All numerical results below are for E-polarised waves, and the wave incidence is taken as normal except for the cases presented in Figs. 3, 4 and 8.

![](./images/812756031770722308_3.jpg)

Fig.3 Transmission response of a thick grating at $30^\circ$ incidence
specular mode
1st grating mode
2nd grating mode

---

IEE Proc.-Microw. Antennas Propag., Vol. 145, No. 5, October 1998

![](./images/812756031770722308_4.jpg)

Fig.4 (a) Reflection phase and (b) transmission coefficient for array of conducting rods with circular cross-section at $30^{\circ}$ incidence
$w/p=0.22$
$w/p=0.27$
$w/p=0.32$

First, to demonstrate the close agreement of the computer predictions with other results, Fig. 3 compares transmission responses computed for a grating analysed previously [1]. The conductor cross-section was square with $w/p=0.4$, and the angle of incidence was $30^{\circ}$. Fig. 3 shows the powers in the fundamental (specular) propagating mode and also in the first two grating responses, over a wide range of $p/\lambda$. Values plotted as discrete points have been extracted from the previous work (Fig. $7a$ [1]), whereas the continuous curves show our results.

Fig. $4a$ presents the frequency dependence of the reflection coefficient phase calculated for the grating composed of circular cylinders, with the optimal aspect ratio $w/p=0.27$ and with two slightly different $(\pm 20\%)$ AR values: 0.22 and 0.32. Strong phase frequency independence for the optimal case occurs only when $p/\lambda \leq$ 0.2, i.e. the condition $p << \lambda$ holds. However, even for greater $p/\lambda$, phase deviation for the optimal grating is much less than for the others. Fig. $4b$ shows the transmitted power for the same grating. The characteristics are typical for inductive grids.

For gratings composed of rectangular conductors, the solution of the frequency independence problem can be presented as a curve, where for any value of the aspect ratio $0 \leq w/p \leq 1$, there exists a unique value of $t/p$, the thickness normalised to the period, which satisfies the frequency independence condition. It lies within the range $0 \leq t/p \leq 0.46$. Fig. $5a$ presents this continuous set of geometrical grating parameters $\{w/p, t/p\}$ that give phase frequency independence. Each shape of the rectangular conductors is characterised by its own transmitting properties. The curves in Fig. $5b$ indicate the transmitted power against $w/p$ for grids with $t/p$ in the necessary range, for a few illustrative values of the normalised period $p/\lambda$. In Fig. 5, the periodic structure composed of infinitesimally thin vertical ribbons $(w/p=$ $0, t/p=0.46)$ has the best transmittivity among all the rectangular gratings of this kind, whereas the opposite case $(w/p=1, t/p=0)$ corresponds to a horizontal tape array that has degenerated into an infinitesimally thin conducting plane. Thus, conductor thickness is required to produce the phase independence property: computer models of grids using a zero thickness approximation cannot demonstrate this effect. The value of the phase $\varphi_{T}=90^{\circ}$.

![](./images/812756031770722308_5.jpg)

Fig.5 Rectangular cross-section
a grating parameters for phase frequency independence
b power transmission coefficient
$p/\lambda=0.1$
$p/\lambda=0.2$
$p/\lambda=0.3$
$p/\lambda=0.4$

Fig. 6 displays the phase of the wave reflected from arrays of rectangular conductors, with the thickness $t=$ $0.95mm$ and periodicity $p=6.3mm$ for a set of conductor widths. The grating with the optimal width $w=$ $2.3mm$ has been manufactured in brass, and its plane wave reflection performance measured for normal incidence in a reflectometer [10]. Fabrication required machining to a dimensional tolerance of $\pm 0.05mm$. The results are shown by the continuous curve in Fig. 6 and are in close agreement with the calculated values. They converge, as expected, on the phase angle $180^{\circ}$ at zero frequency. The error in the measured phase at a given frequency was $\pm 1.5^{\circ}$, estimated from the instrumental noise and also from the repeatability of the results when the equipment was realigned, and when calibrated against a flat metal plate.

Further analysis indicates that including dielectric in the grating does not prevent it from being phase frequency independent. Fig. 7 shows the reflection coefficient phase against $p/\lambda$ for gratings composed of alternate contiguous metal and dielectric rods for three values of $w/p$ for the conductors. The relative thickness

IEE Proc.-Microw. Antennas Propag., Vol. 145, No. 5, October 1998

is $t/p = 0.15$, and the dielectric has $\varepsilon_r = 2$. The wave incidence is normal. The optimal value of $w/p$ in this case is 0.38. There are no essential differences from the previous case of entirely metal gratings. However, no pure dielectric grating can reflect/transmit an electromagnetic wave with the phase being frequency-independent. This is easily explained by the well known fact that electromagnetic properties of such a grating within the frequency range of interest (i.e. before the onset of grating responses) are practically the same as those of a dielectric layer of the same thickness with the equivalent (average) dielectric permittivity.

![](./images/812756031770722308_6.jpg)

Fig.6 Reflection phase for arrays of conductors of rectangular cross-section
thickness $t = 0.95$mm, periodicity $p = 6.3$mm, measured values are for $w = 2.3$mm
$w = 1.5$mm
$w = 2.0$mm
$w = 2.3$mm
$w = 3.0$mm
$w = 3.5$mm
$w = 2.3$mm (measured)

![](./images/812756031770722308_7.jpg)

Fig.7 Computed reflection phase for array of contiguous metal and dielectric rectangular rods of normalised thickness $t/p= 0.15$
$w/p = 0.2$
$w/p = 0.38$
$w/p = 0.50$

Finally, Fig. 8 shows the calculated angular dependence of the reflection phase of the gratings with the parameters presented in Fig. 4 for $p/\lambda = 0.2$. Thus, phase angular independence is now numerically established for the same structure that gives frequency independence.

![](./images/812756031770722308_8.jpg)

Fig.8 Angular dependence of reflection phase for array of conducting rods with circular cross-section with $p/\lambda = 0.2$
$w/p = 0.22$
$w/p = 0.27$
$w/p = 0.32$

## 4 Conclusions

The above analysis is rigorous and the frequency independence of the phase is clearly demonstrated. Moreover, the experimental results show that there are no impracticable tolerances to be met in manufacturing the grating before the phase frequency independence phenomenon can be observed.

Calculations performed for gratings illuminated by an $H$-polarised wave demonstrate that this phase independence, either with frequency or angle, does not occur.

The numerical results describe a special electromagnetic property of an important class of microwave and optical structures: thick conducting gratings with properly chosen dimensions. Over a wide frequency and angular range, they have almost the same reflectivity phase properties as a conducting sheet placed in the grating symmetry plane and might therefore be called 'quasimetal surfaces'.

The frequency and angular independence of the phase may be useful in designing wideband devices: polarisation rotators, power dividers and other structures sensitive to the phase. The well defined reflecting phase reference surface would help in the design of sheath helices (helically conducting cylinder) [11]. Such gratings may also be very useful as semi-transparent walls in transmission-type resonators [12].

The results for grids composed of alternate metal and dielectric rods relate to the use of such gratings as reinforcing structures, in the development of materials and construction techniques for modern buildings, where transmission properties are a design parameter.

## 5 Acknowledgments

The authors acknowledge the financial support of the UK Engineering and Physical Sciences Research Council, and they would like to thank Professor B.Z. Katsenelenbaum of the Moscow Institute of Radio Engineering and Electronics of the the Russian Academy of Sciences for helpful discussions.

## 6 References

1 GEDNEY, S., and MITTRA, R.: 'Analysis of the electromag- netic scattering by thick gratings using a combined FEM/MoM solution', *IEEE Trans.*, 1991, **AP-39**, pp. 1605-1614

2 SIVOV, A.N., CHUPRIN, A.D., and SHATROV, A.D.: 'Phe- nomenon of frequency independence of the phase of reflection and transmission coefficients for small-period gratings', *Radi- otekhnika i Electronika*, 1994, **39**, pp. 1276-1278 (in Russian)

3 SIVOV, A.N., CHUPRIN, A.D., and SHATROV, A.D.: 'On phase characteristics of short-period gratings'. Proc. Mathemati- cal Methods in Electromagnetic Theory Conf., MMET '94, Kharkov, Ukraine, 1994, pp. 403-405

4 MARCUVITZ, N.: 'Waveguide handbook' (MIT Radiation Lab- oratory Series, vol. 10, McGraw-Hill Book Company, Inc., NewYork, 1951)

5 TWERSKY, V.: 'On scattering of waves by an infinite grating of parallel perfectly conducting circular cylinders', *IRE Trans.*, 1962,**AP-10**, pp. 737-765

6 WASYLKIWSKYJ, W.: 'On the transmission coefficient of an infinite grating of parallel perfectly conducting circular cylinders',*IEEE Trans.*, 1971, **AP-19**, pp. 704-708

7 KALHOR, H.A., and ARMAND, A.: 'Scattering of waves by gratings of conducting cylinders', *IEE Proc. H*, 1975, **122**, pp.245-248

8 KALHOR, H.A., and SHAHINPOOR, M.: 'Diffraction of plane electromagnetic waves from arrays of conducting rectangular cyl-inders', *IEE Proc. H*, 1976, **123**, pp. 203-206

9 TWERSKY, V.: 'Scattering theorems for bounded periodic struc-tures', *J. Appl. Phys.*, 1956, **27**, pp. 1118-1122

10 APLETALIN, V.N., DYAKONOVA, O.A., KAZANTSEV,Y.N., SIMONYAN, D.E., SOLOSIN, V.S., and ZUBOV, A.S.:'New methods for the measurement of microwave and millimeter wave absorbing and radiotransparent materials'. Proc. Joint 3rd Int. Electromagnetics in Aerospace Applications Conf. and 7th European Electromagnetic Structures Conf., Torino, Italy, 1993,pp. 253-258

11 ZUBOV, A.S., SIVOV, A.N., SOLOSIN, V.S., CHUPRIN, A.D., and SHATROV, A.D.: 'Wave scattering by sheath helices and simulation of electromagnetic properties of multifilar wire helices with the help of such cylinders', *Radiotekhnika i Elec-tronika*, 1996, **41**, pp. 1434-1437 (in Russian)

12 SHATROV, A.D., CHUPRIN, A.D., and SIVOV, A.N.: 'Con- structing the phase converters consisting of arbitrary number of translucent surfaces', *IEEE Trans.*, 1995, **AP-43**, pp. 109-113

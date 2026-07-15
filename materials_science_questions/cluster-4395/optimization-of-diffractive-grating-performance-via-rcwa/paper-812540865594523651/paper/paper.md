# ENGINEERING SCIENCES

## A Bandpass Filter Based on Dielectric Layers with a Strip Conductor Subwavelength Grating at Their Interfaces

B. A. Belyaev$^{a,b,c,*}$, V. V. Tyurnev$^{a}$, A. S. Voloshin$^{a,b,c}$, An. A. Leksikov$^{a}$, R. G. Galeev$^{c}$, and Academician V. F. Shabanov$^{a,c}$

Received June 30, 2020; revised June 30, 2020; accepted July 10, 2020

**Abstract**—The design of a multilayer bandpass filter has been investigated, in which each of the half-wavelength resonators consists of two dielectric layers with outer strip conductor gratings in the form of square grids and inner ones in the form of square patches. The grids serve as mirrors with specified reflective properties, which ensure optimal couplings of the outer resonators with free space and optimal coupling between the resonators. The patch gratings make it possible to tune the resonator eigenfrequency during the filter synthesis. The efficiency of the quasi-static calculation of the frequency response for the layered structure is shown for the case of a lattice period smaller than the wavelength in the dielectric and much smaller than the layer thickness. Since the calculation does not require much computing power, the parametric synthesis of the device can be performed on a conventional personal computer. The measured characteristics of the prototype of the synthesized third-order filter with a fractional passband width of $\sim$10% and a central passband frequency of $\sim$10.6 GHz are in good agreement with the calculation. The proposed design allows one to fabricate multilayer panels radio transparent in a certain frequency band for hiding microwave antennas.

**Keywords:** frequency response, return loss, passband filter, insertion loss

DOI: 10.1134/S1028335820090013

At present, the features of transmission and reflection of electromagnetic waves falling onto structures consisting of dielectric layers with strip conductor periodic structures (2D gratings) formed on their surfaces are intensively being studied [1–4]. The interest in such structures is due to the possibility of their use to create frequency selective surfaces serving as bandpass filters operating in the ranges from decimeter to submicron wavelengths. Strip elements forming a 2D periodic structure, for example, metal patches or metal grid cells, exhibit the properties of parallel or series oscillating circuits, which allows one to create bandpass filters using multilayer structures consisting of interacting resonant structures. It is important that, at high frequencies, the unloaded $Q$ factor of strip resonators decreases with a decrease in the skin depth and an increase in the value of the substrate roughness effect. Therefore, the multilayer filters based on the strip conductor resonant structures have a relatively high passband loss.

The filter designs in which the dielectric layers serve as high-$Q$ resonators and the 1D or 2D strip conductor structures formed on their surfaces work as mirrors with a specified reflectivity have the much lower loss [5, 6]. To expand the high-frequency stopband in such structures, the strip structure period should be much shorter than the wavelength in the dielectric; then, their resonant frequencies are much higher than the filter passband. However, the most promising designs are those, in which the resonators consist of not one, but two dielectric layers with outer 2D strip conductor gratings, e.g., in the form of square grids, and with inner ones in the form of square patches [7]. Such designs not only have higher frequency-selective properties, but also make it possible to change the filter passband center frequency in a wide range at a specified permittivity of the layers and their fixed thickness. It should be noted that bilayer resonators were used in the original designs of filterpolarizes [8, 9] with 1D strip conductor gratings crossed between adjacent layers in a multilayer structure.

---

$^{a}$ *Kirensky Institute of Physics, Krasnoyarsk, 660036 Russia*
$^{b}$ *Siberian Federal University, Krasnoyarsk, 660041 Russia*
$^{c}$ *Siberian State University of Science and Technology, Krasnoyarsk, 660014 Russia*
*e-mail: belyaev@iph.krasn.ru*

## BILAYER RESONATOR-BASED FILTER DESIGN

The resonators forming a filter consist of two identical dielectric layers with thickness $h$ (Fig. 1a) with strip conductor gratings in the form of grids with win-

![](./images/812540865594523651_1.jpg)

Fig. 1. (a) Design of a resonator consisting of two dielectric layers with strip conductor gratings, (b) bilayer resonator-based third-order filter, and (c) its equivalent circuit.

dow width $s_{Li}$ on their outer surfaces and a grating of square strip conductors (patches) with width $w_{Ci}$ placed between the layers. The gratings have the same period $T$ and are subwavelength; i.e., $T$ is much shorter than the wavelength at the eigenfrequency of the resonator oscillation first mode. Figure 1b shows a cross section of the third-order filter, and Fig. 1c, its equivalent circuit for an electromagnetic wave incident from free space. The electric thickness $\theta$ of the dielectric layers is determined by their thickness $h$ and permittivity $\varepsilon$. The conductors on the resonator outer layers are inductances $L_{1,2}$, and the strip conductors on the inner layers form capacitances $C_{1,2}$. The inductive gratings ensure the optimal couplings of the outer resonators with free space and the resonators with each other; the eigenfrequency of the resonators decreases with the conductor width. The capacitive gratings make it possible to vary the resonator eigenfrequencies in a wide range, lowering them with increasing $w_{Ci}$.

According to the specified frequency response, the filter is tuned for a chosen layer thickness and permittivity by only tuning the gaps of the outer $(s_{L1})$ and inner $(s_{L2})$ inductive grids and the patch width $(w_{C1}$, $w_{C2})$ in the capacitive gratings of the outer and central resonators.

## QUASI-STATIC MATRIX CALCULATION OF THE FILTER FREQUENCY RESPONSE

The quasi-static approximation used in calculating the frequency response of the investigated layered structure assumes that the grating period $T$ is much shorter than the wavelength in a dielectric at the center frequency $f_0$ of the filter passband and, simultaneously, shoter than the layer thickness $h$. The layered structure is assumed to be a cascade connection of two-port networks corresponding to the dielectric layers and strip conductor gratings, the properties of which are described by transmission $ABCD$ matrix and scattering $S$ matrix. $ABCD$ matrix of the structure is determined by multiplying the $ABCD$ matrices of all the two-port networks [10]. $ABCD$ matrix of a two-port network connected to the ports relates the voltages and input currents in the ports by the equation [10]

$$
\begin{pmatrix}
U_1 \\
I_1
\end{pmatrix}
=
\begin{pmatrix}
A & B \\
C & D
\end{pmatrix}
\begin{pmatrix}
U_2 \\
I_2
\end{pmatrix}, \tag{1}
$$

where indices 1 and 2 are the port numbers. In the investigated model, the two-port network ports are the strip grating surfaces. Therefore, Eq. (1) takes the form

DOKLADY PHYSICS Vol. 65 No. 9 2020

$$
\begin{pmatrix}
E_{1x} \\
H_{1y}
\end{pmatrix}
=
\begin{pmatrix}
A & B \\
C & D
\end{pmatrix}
\begin{pmatrix}
E_{2x} \\
-H_{2y}
\end{pmatrix},
\tag{2}
$$

where indices $x$ and $y$ denote the components of the electric and magnetic field strength vectors under the assumption of the $z$ axis directed along the normal to the layered structure surface and the $x$ axis directed along the electric field of the incident wave.

The scattering matrix $(S)$ relates the normalized amplitudes $b_n$ of the outgoing waves to the normalized amplitudes $a_n$ of the incident waves as [10]

$$
\begin{pmatrix}
b_1 \\
b_2
\end{pmatrix}
=
\begin{pmatrix}
S_{11} & S_{12} \\
S_{21} & S_{22}
\end{pmatrix}
\begin{pmatrix}
a_1 \\
a_2
\end{pmatrix}.
\tag{3}
$$

The normalized amplitudes are determined using the formulas

$$
a_n = \frac{E_{nx}^{\text{inc}}}{\sqrt{Z_n}}, \quad b_n = \frac{E_{nx}^{\text{out}}}{\sqrt{Z_n}},
\tag{4}
$$

where $Z_n = Z_0/\sqrt{\varepsilon_n}$ and $\varepsilon_n$ are the characteristic impedance and permittivity of the medium adjacent to port $n$, respectively, and $Z_0 = \sqrt{\mu_0/\varepsilon_0}$ is the characteristic impedance of free space. The matrix elements $S_{11}$ and $S_{22}$ are the complex reflectivities, and $S_{21}$ and $S_{12}$ are the complex transmittances. Their arguments describe the phases of the reflected and transmitted waves. The investigated structure contains no gyrotropic media; therefore, the structure and each of its elements are described by mutual two-port networks, for which the equalities $S_{21} = S_{12}$ and $AD - BC = 1$ are valid [10].

The $ABCD$ and $S$ matrices are interrelated. Their interrelation is expressed in the formulas

$$
\begin{aligned}
A &= \frac{\left(1 + S_{11} - S_{22} - \Delta S\right)\sqrt{Z_1/Z_2}}{2S_{21}}, \\
B &= \frac{\left(1 + S_{11} + S_{22} + \Delta S\right)\sqrt{Z_1Z_2}}{2S_{21}}, \\
C &= \frac{\left(1 - S_{11} - S_{22} + \Delta S\right)}{\sqrt{Z_1Z_2}2S_{21}}, \\
D &= \frac{\left(1 - S_{11} + S_{22} - \Delta S\right)\sqrt{Z_2/Z_1}}{2S_{21}},
\end{aligned}
\tag{5}
$$

where $\Delta S = S_{11}S_{22} - S_{21}S_{12}$, and the formulas

$$
\begin{aligned}
S_{11} &= \frac{AZ_2 + B - CZ_1Z_2 - DZ_1}{AZ_2 + B + CZ_1Z_2 + DZ_1}, \\
S_{12} &= \frac{2(AD - BC)\sqrt{Z_1Z_2}}{AZ_2 + B + CZ_1Z_2 + DZ_1}, \\
S_{21} &= \frac{2\sqrt{Z_1Z_2}}{AZ_2 + B + CZ_1Z_2 + DZ_1}, \\
S_{22} &= \frac{-AZ_2 + B - CZ_1Z_2 + DZ_1}{AZ_2 + B + CZ_1Z_2 + DZ_1}.
\end{aligned}
\tag{6}
$$

An $ABCD$ matrix of the electromagnetic wave falling onto a dielectric layer with thickness $h$, the time dependence of which is described by the factor $\exp(-i\omega t)$, is well-known:

$$
\begin{pmatrix}
A & B \\
C & D
\end{pmatrix}_h
=
\begin{pmatrix}
\cos\theta & -i\frac{Z_0}{\sqrt{\varepsilon}}\sin\theta \\
-i\frac{\sqrt{\varepsilon}}{Z_0}\sin\theta & \cos\theta
\end{pmatrix},
\tag{7}
$$

where $\varepsilon$ is the permittivity of the dielectric and $\theta = \frac{\omega\sqrt{\varepsilon}h}{c}$ is the phase thickness of a layer at frequency $\omega$.

The $S$ matrices for the strip conductor gratings in the form of square grids [11] or square patches [12] located at the interface between two media with permittivities $\varepsilon_1$ and $\varepsilon_2$ have the same form

$$
\mathbf{S} =
\begin{pmatrix}
\frac{\sqrt{\varepsilon_1} - \sqrt{\varepsilon_2} - Z_0Y}{\sqrt{\varepsilon_1} + \sqrt{\varepsilon_2} + Z_0Y} & \frac{2\sqrt[4]{\varepsilon_1\varepsilon_2}}{\sqrt{\varepsilon_1} + \sqrt{\varepsilon_2} + Z_0Y} \\
\frac{2\sqrt[4]{\varepsilon_1\varepsilon_2}}{\sqrt{\varepsilon_1} + \sqrt{\varepsilon_2} + Z_0Y} & \frac{\sqrt{\varepsilon_2} - \sqrt{\varepsilon_1} - Z_0Y}{\sqrt{\varepsilon_1} + \sqrt{\varepsilon_2} + Z_0Y}
\end{pmatrix},
\tag{8}
$$

where $Y$ is the conductivity of the grating related to the inductance and capacitance of the conductors of its unit cell by the formula

$$
Y = \frac{i}{\omega L} - i\omega C.
\tag{9}
$$

For the inductive grating in the form of a grid with period $T$ and square gap side $s$, the grating conductivity $Y_L$ is determined by the formula [11]

$$
\begin{aligned}
Y_L &= \frac{2\pi i}{\omega\mu_0 s \ln\sec\left(\frac{\pi s}{2T}\right)} \\
&- i\omega\varepsilon_0 T \frac{\varepsilon_1 + \varepsilon_2}{\pi} \ln\operatorname{cosec}\left(\frac{\pi s}{2T}\right).
\end{aligned}
\tag{10}
$$

The first term in Eq. (10) describes the inductive part of the conductivity, and the second term, its capacitive part. It can be seen that, at low frequencies, the inductive part of the conductivity prevails over the capacitive one.

For the capacitive grating, the conductivity $Y_C$ can be calculated using Eq. (9), in which the inductance and capacitance of the conductors are expressed as [12]

$$
C = \varepsilon_0 \frac{\varepsilon_1 + \varepsilon_2}{\pi} T \ln\sec\left(\frac{\pi w}{2T}\right),
\tag{11}
$$

$$
L = \frac{\mu_0 T}{4\pi}
\left[
\ln\left(\operatorname{cosec}\left(\frac{\pi w}{2T}\right)\right) + \frac{\frac{\pi^2 w^2}{12T^2} - \frac{2}{\pi} X\left(\frac{\pi w}{2T}\right)}{\ln\left(\sec\left(\frac{\pi w}{2T}\right)\right)}
\right], \quad (12)
$$

![](./images/812540865594523651_2.jpg)

Fig. 2. Frequency responses of the third-order filter synthesized using the formulas (solid lines) and obtained by the numerical electromagnetic calculation of a 3D model with the parameters of the synthesized filter (dashed lines).

where $T$ is the lattice period, $w$ is the side of its square conductors, and function $X(a)$ denotes the double integral

$$
X(a) = \int_{\zeta=0}^{a} \left[ \int_{\xi=\zeta}^{a} \arcsin\left( \frac{\sin \xi}{\sin x} \right) d\xi \right] d\zeta. \tag{13}
$$

Note that, at low frequencies, the capacitive contribution to the conductivity $Y_C$ dominates.

The frequency response of the bilayer resonator-based filter, i.e., its scattering matrix $\mathbf{S}$, is calculated as follows. First, the scattering matrices for each grating in the layered structure are calculated using Eq. (8). Then, using Eq. (5) the corresponding $ABCD$ matrices are calculated. The $ABCD$ matrix of the identical dielectric layer is calculated using Eq. (7). The $ABCD$ matrix of the entire structure is calculated by the sequential multiplication of the $ABCD$ matrices of all planar elements, starting with the inductive grating on port 1 and finishing with the grating on port 2. The obtained $ABCD$ matrix is used to calculate the desired $S$ matrix using Eq. (6).

The investigations showed that the presented quasi-static calculation of the characteristics of a multilayer filter is in good agreement with the electromagnetic calculation of its 3D model, the results of which, as is known, almost coincide with the experiment. However, the agreement is only observed when the above design requirements are met; specifically, the grating period $T$ should be much shorter than the wavelength in the dielectric at the filter passband center frequency $f_0$ and, simultaneously, smaller than the layer thickness $h$. Therefore, it is interesting to estimate the accuracy of the calculation of the frequency response using the formulas derived when these requirements are not met. Figure 2 (solid lines) shows the frequency dependences of the insertion loss $S_{21}$ and return loss $S_{11}$ of the third-order filter with a passband center frequency of $f_0 = 16$ GHz and a relative passband width of $-3$ dB $\Delta f/f_0 = 10\%$ synthesized using the above formulas. In the calculation, the thickness of the layers was $h = 1.5$ mm, their permittivity was $\varepsilon = 2.2$, and the period of all the gratings was chosen to be twice as much as the layer thickness, i.e., $T = 3$ mm, which violates the condition for applicability of the quasi-static approach. The filter was tuned by fitting the grid gaps $s_{L1}$ and $s_{L2}$ and the patch widths $w_{C1}$ and $w_{C2}$ in the layered structure such that the maximum of the reflections in the passband were at the level of $-15$ dB. The obtained tuning parameters of the structure are given in Table 1 (upper row).

The tuning parameters determined were used in a 3D filter model, the frequency responses of which obtained by the numerical electrodynamic calculation in the CST Microwave Studio are shown in Fig. 2 (dashed lines). The relatively small difference between the corresponding pairs of characteristics indicates that even if the quasi-static approximation conditions are violated, the formulas proposed make it possible to find the design parameters of the structure that can be used as seed ones in its 3D model at the initial stage of optimization. This multiply accelerates designing of the filters in the electromagnetic software packages, which, as is known, require much computing time. For comparison, Table 1 (second row) gives the optimal design parameters of the gratings of the layered structure after its tuning using the numerical electromagnetic 3D simulation. In this case, the frequency response of the tuned filter fully coincides with those shown in Fig. 2 by solid lines.

Table 1. Widths of the square gaps and strip conductors of the gratings of a third-order multilayer filter with a passband center frequency of 16 GHz

| Calculation technique | $s_{L1}$, mm | $w_{C1}$, mm | $s_{L2}$, mm | $w_{C2}$, mm |
|-----------------------|--------------|--------------|--------------|--------------|
| Quasi-static          | 2.785        | 2.529        | 1.831        | 2.725        |
| Electromagnetic       | 2.857        | 2.556        | 1.709        | 2.732        |

# STUDY OF THE MULTILAYER FILTER PROTOTYPE

To check the operability of the bandpass filter based on bilayer resonators, we fabricated a third-order filter prototype consisting of six dielectric layers with an area of $300 \times 300$ mm. The strip conductor gratings were formed on metallized RO3010 plates (Rogers Corporation) with a thickness of $h = 1.29$ mm, a permittivity of $\varepsilon = 11.2$, and a dissipation factor of $\tan\delta = 2.2 \times 10^{-3}$. The dielectric plates were stacked in

DOKLADY PHYSICS  Vol. 65  No. 9  2020

**Table 2.** Widths of square gaps and strip conductors of the gratings of a third-order multilayer filter with a fractional passband of $\Delta f/f_0 = 10\%$ and a passband center frequency of $f_0 = 10.5$ GHz

| $s_{L1}$, mm | $w_{C1}$, mm | $s_{L2}$, mm | $w_{C2}$, mm |
|--------------|--------------|--------------|--------------|
| 2.846        | 1.770        | 1.570        | 2.205        |

a monolithic structure with a RO4450B prepreg (Rogers Corporation) having a thickness of 0.127 mm, permittivity of $\varepsilon = 3.54$, and a dissipation factor of $\tan\delta = 4.0 \times 10^{-3}$ using the multilayer printed circuit board technology. The photographs of the device and fragments of its outer and inner strip conductor gratings are shown in Fig. 3. For definiteness, the periods of the inductive and capacitive strip conductor gratings for all the resonators were specified to be the same ($T = 3.0$ mm). Preliminarily, the device was synthesized using the formulas obtained for a passband center frequency of $f_0 = 10.5$ GHz and a relative passband width of $\Delta f/f_0 = 10\%$; then, the grating parameters determined were used as seed ones in the 3D model for synthesizing the filter in the CST Microwave Studio. The parameters of the gratings of the synthesized filter are given in Table 2, and its calculated frequency responses are shown by solid and dashed lines in Fig. 3.

![](./images/812540865594523651_3.jpg)

![](./images/812540865594523651_4.jpg)

**Fig. 3.** Calculated frequency responses of the third-order filter prototype: insertion loss (solid line), return loss (dashed line), and measured frequency dependence of the insertion loss (dots). (a) Filter photograph (on the top) and fragments of its (b) outer and (c) inner strip conductor gratings.

The characteristics of the fabricated filter prototype were measured with an R&S ZVA 40 vector analyzer using miniature broadband horn antennas. Taking into account the relatively small filter sizes, the distance between the transmitting and receiving antennas was chosen to be minimum, but without destruction of the plane wave. The measurement data are shown in Fig. 3 (dots). Note that the calculated minimum loss in the passband of the device was ~0.3 dB and the loss measured on the prototype was ~0.6 dB. The measured fractional passband width $\Delta f/f_0 = 10\%$ of the prototype and the passband center frequency $f_0 = 10.6$ GHz agree fairly well with the numerical electrodynamic calculation of the filter 3D model.

## CONCLUSIONS

Thus, in this study, we made a quasi-static calculation of the design of a multilayer bandpass filter, in which each of the half-wavelength resonators consists of two dielectric layers with outer strip conductor gratings in the form of square grids and inner ones in the form of square patches. All the gratings in the structure are subwavelength; i.e., their period is much shorter than the wavelength. Therefore, the resonant properties of the gratings manifest themselves at frequencies much higher than the passband. The unloaded $Q$ factor of the bilayer resonators is high, since it is mainly determined by the $Q$ factor of the dielectric layers. The metal grids serve as mirrors with specified reflective properties and ensure the optimal couplings of the outer resonators with free space and the optimal couplings between the resonators; therefore, they have a weaker affect on the $Q$ factor of the resonators. The patch gratings allow one to change the eigenfrequency of the resonators within a wide range, which makes it possible to vary easily the center frequency of the filter passband and adjust the resonator frequencies independently when tuning it. We demonstrated the high efficiency of the quasi-static calculation of the frequency response of the layered structure not only at the satisfied conditions of applicability of the quasi-static approximation, when the grating period is

shorter than the wavelength in the dielectric and much smaller than the layer thickness, but also when these conditions are strongly violated. Since the high-speed quasi-static calculation does not require much com- puting time, the parametric synthesis of the devices can be performed in a record-short time on a conven- tional personal computer. The relatively small differ- ence between the frequency responses of the investi- gated layered structure obtained by the electromag- netic and quasi-static calculations allows one, using the formulas obtained, to find the design parameters of the structure, which can be used as seed ones in its3D model at the initial stage of optimization. This multiply accelerates designing of the filters in electro- magnetic simulation software packages.

## FUNDING

This study was supported by the Ministry of Science and Higher Education of the Russian Federation, state assign- ment no. FEFE-2020-0013 "Development of the Theory of Self-Configurable Machine-Learning Algorithms for Sim- ulating and Predicting Characteristics of Complex Sys- tems."

## REFERENCES

1. A. M. Melo, M. A. Kornberg, P. Kaufmann, M. H. Pi- azzetta, E. C. Bortolucci, M. B. Zakia, O. H. Bauer, A. Poglitsch, and A.M.P. Alves da Silva, Appl. Opt. 47(32), 6064 (2008).
2. F. J. Garcia-Vidal, L. Martin-Moreno, T. W. Ebbesen, and L. Kuipers, Rev. Mod. Phys. 82 (1), 729 (2010).
3. R. S. Anwar, L. Mao, and H. Ning, Appl. Sci. 8 (9),1689 (2018).
4. S. Sui, H. Ma, J. Wang, Y. Pang, J. Zhang, Z. Xu, S. Qu,Int. J. RF Microwave Comput.-Aided Eng. 29 (1), e21491(2019).
5. B. A. Belyaev and V. V. Tyurnev, Opt. Lett. 40 (18),4333-4335 (2015).
6. B. A. Belyaev, V. V. Tyurnev, A. S. Voloshin, and R. G. Galleev, Tech. Phys. Lett. 44, 408-411 (2018).
7. M. A. Al-Joumayly and N. Behdad, IEEE Trans. An- tennas Propag. 58 (12), 4033-4041 (2010).
8. B. A. Belyaev and V. V. Tyurnev, Microw. Opt. Tech.Lett. 60 (3), 630-634 (2018)https://doi.org/10.1002/mop.31021
9. B. A. Belyaev, V. V. Tyurnev, A. S. Voloshin, An. A. Lek-sikov, R. G. Galeev, and V. F. Shabanov, Dokl. Phys. 65(7),1-5(2020).
10. K. C. Gupta, R. Garg, and R. Chadha, Computer-Aided Design of Microwave Circuits (Artech, Dedham, MA,1981; Radio i Svyaz', Moscow, 1987).
11. B. A. Belyaev and V. V. Tyurnev, J. Commun. Technol. Electron. 62 (7), 750-758 (2017).
12. B. A. Belyaev, V. V. Tyurnev, and N. V. Volkov, J. Com- mun. Technol. Electron. 64 (7), 664-674 (2019).

Translated by E. Bondareva

---

DOKLADY PHYSICS Vol. 65 No. 9 2020
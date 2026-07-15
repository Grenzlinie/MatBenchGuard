# The effects of transition element doping on the thermoelectric properties of $\beta$-Zn₄Sb₃

Mian Liu $^{a,b}$, Kun Xu $^{a}$, Xiaoying Qin $^{b,**}$, Changsong Liu $^{b}$, Zhe Li $^{a,*}$

$^{a}$ Center for Magnetic Materials and Devices and Key Laboratory for Advanced Functional and Low Dimensional Materials of Yunnan Higher Education Institute, Qujing Normal University, Qujing, 655011, China
$^{b}$ Key Laboratory of Materials Physics, Institute of Solid State Physics, Chinese Academy of Sciences, P.O. Box 1129, Hefei, 230031, China

---

## ARTICLE INFO

**Article history:**
Received 18 January 2019
Received in revised form
12 April 2019
Accepted 15 April 2019
Available online 16 April 2019

**Keywords:**
Thermoelectric materials
$\beta$-Zn4Sb3
Thermoelectric properties
Electron density of states resonance

---

## ABSTRACT

The effects of transition elements Fe, Co, and Ni on the electronic structure and thermoelectric properties of $\beta$-Zn₄Sb₃ were investigated by performing self-consistent ab initio electronic structure calculations within density functional theory and solving the Boltzmann transport equations within the relaxation time approximation. The results demonstrate that these transition elements with $3d$ orbitals could introduce giant sharp resonant peaks in the electronic density of states (DOS) near the host valence band maximum or conduction band minimum in energy. And these deliberately engineered DOS peaks result in a sharp increase of the room-temperature Seebeck coefficient of $\beta$-Zn₄Sb₃ by a factor of nearly 60, 80 and 130, respectively. Additionally, with the simultaneous decline of carrier thermal conductivity upon Co/Ni doping, potentially, at least, 1.21/1.13-fold increase in thermoelectric figure of merit of $\beta$-Zn₄Sb₃ at room temperature are achieved, indicating that the substitution of Co and Ni for Zn can effectively elevate thermoelectric performance of $\beta$-Zn₄Sb₃.

© 2019 Elsevier B.V. All rights reserved.

---

## 1. Introduction

Currently, there has been a renewed interest toward thermoelectric materials for energy conversion and power generation driven by energy crisis and the environment issues [1–6]. The thermoelectric potential of a material at an operating temperature $T$ is assessed with the figure of merit of $ZT$ defined as $ZT = S^{2}\sigma T/\lambda$ (here $S$ is the Seebeck coefficient, $\sigma$ is the electrical conductivity, $\lambda(=\lambda_{C}+\lambda_{L})$ is thermal conductivity with both the carrier ($\lambda_{C}$) and lattice ($\lambda_{L}$) contributions, and $T$ is the absolute temperature). Among the good thermoelectric materials known, $\beta$-Zn₄Sb₃ emerged as a prospective thermoelectric material for commercial application in the moderate temperature range because of the prominent high thermoelectric performance, $ZT = 1.3$ at 670 K, which primarily arises from its extraordinarily low thermal conductivity (~0.7 Wm⁻¹ K⁻¹ at 650 K) [7]. Such extraordinarily low thermal conductivity can be likened to a "phonon glass-electron crystal" thermoelectric property [8], characteristic of an ideal thermoelectric material, and was recognized originating at least in part from the complex and substantially disordered crystal structure with vacancies and interstitial Zn atoms [9,10], or due to the low frequency rattling motion of the Sb dimers in the crystal structure [11].

The $ZT$ value of $\beta$-Zn₄Sb₃ has been elevated through many approaches, such as developing new synthesis methods [12], elemental doping and nano-structuring [13,14]. The traditional strategy for boosting $ZT$ of $\beta$-Zn₄Sb₃ is to adjust the carrier concentration and lower thermal conductivity simultaneously by doping. For instance, dopants such as Pb, Bi, Mg, Cu, Sn, In, Cd, Al, Ga, Nb, Hg, Co, Te, I, Se, Fe and Ag have been investigated so far [15–33]. However, the results showed that although the individual parameters were affected by doping, there was a little or no overall improvement of its thermoelectric performance. The main reasons lie in the following factors: (i) thermal conductivity of $\beta$-Zn₄Sb₃ is very low (<1 W m⁻¹ K⁻¹) [7,24,34] which is close to the practical lower limit for the thermal conductivity in solids [9]; this means that there is no much room in lowering its thermal conductivity; (ii) the hole concentration of pristine $\beta$-Zn₄Sb₃ is in the order of $10^{24}$~$10^{25}$ m⁻³ [7,35,36], which indicates that its carrier concentration has already been close to the optimum. These characters of $\beta$-Zn₄Sb₃ mentioned here suggest that it is difficult to enhance its thermoelectric performance remarkably through doping, unless

---

* Corresponding author.
** Corresponding author.
E-mail addresses: xyqin@issp.ac.cn (X. Qin), zheli@mail.qjnu.edu.cn (Z. Li).

https://doi.org/10.1016/j.jallcom.2019.04.156
0925-8388/© 2019 Elsevier B.V. All rights reserved.

The Seebeck coefficient S can be extra elevated upon doping. This is extremely important to the material system since the Seebeck coefficient of β-Zn₄Sb₃ is relatively small (around 100 μV/K at room temperature [7,8,24–26,35,37–39]), and only when large S is achieved can the thermoelectric performance of β-Zn₄Sb₃ be improved substantially.

Recently, Heremans and his coworkers [40] demonstrated experimentally that ZT of Tl-doped PbTe doubled, which results from an increase in S and is caused by additional Tl-induced peaks in the electronic density of states (DOS). Similar phenomenon was also observed in Bi₂Te₃ doped with Sn [41]. The key issue to be settled here is whether there exits analogous elements that can cause a resonance-like peak in DOS of β-Zn₄Sb₃, just as Tl acts in PbTe. As we know, the valence electrons of transition elements are filled in 3d orbitals of the sub-outer layer in turn. If the 3d levels of these elements overlap or hybridize with the host band and to form resonate peaks close to the Femi level in DOS, great enhancement in Seebeck coefficient can be expected in such doped material systems as predicted theoretically by Mahan and Sofo [42]. It is thus particularly interesting to understand and explore possibilities of transition-dopant-induced resonance-like distortion peaks in the DOS with a view of improving thermoelectric efficiency, which could provide us a promising avenue for designing high-performance thermoelectric materials.

Based on our preliminary investigation on the structural and thermoelectric properties of β-Zn₄Sb₃, in the present work we focused our attention on the change behavior of the electronic states and thermoelectric properties after doping of transition elements (here Fe, Co and Ni) in β-Zn₄Sb₃. Through combinations of ab initio calculations with analytic calculations we tried to extract some important information which would help us to understand the effects of transition-element doping on the thermoelectric properties of β-Zn₄Sb exploring a possible path to enhancing its thermoelectric performance ultimately.

## 2. Computational methods

Our calculations are performed within the framework of the density-functional theory, with the PBE generalized gradient approximation to the exchange correlation energy, and the valence electron-ion interaction was modeled by the projector augmented wave potential, as implemented in the Vienna ab initio simulation package (VASP) [43–45]. The atoms of system were put in a unit cell with periodical boundary condition. The plane wave cutoff and k-point density, obtained using the Monkhorst-Pack method, were both checked for convergence for each system to be within 0.001 eV per atom. Following a series of test calculations, a plane wave cutoff of 350 eV was adopted. The structural optimization is truncated when the forces converge to less than 0.001 eV/Å. Structural relaxations have been performed by using the conjugate gradient algorithm. The ionic coordinates and the unit cell's size and shape were optimized simultaneously to eliminate structures with internal stress. For simplicity, in the present work we utilized the crystal structure of a hypothetical disorder-free β-Zn₄Sb₃ with a framework of Zn₃₆Sb₃₀ as shown in Fig. 1, one of basic structures in Cargnoni's model [9]. Please refer to our earlier work [46] for more details on this model. Then ab initio electrical structure calculations were carried out for the Zn-substituted compounds MZn₃₅Sb₃₀ (M=Fe/Co/Ni).

![](./images/812783364976148481_1.jpg)

Fig. 1. Crystal structures of Zn₃₆Sb₃₀. Sb(1)³⁻ atoms (red); Sb(2)²⁻ atoms (purple); Zn atoms (cyan). (For interpretation of the references to colour in this figure legend, the reader is referred to the Web version of this article.)

In order to understand the effects of transition element doping on the thermoelectric properties, $\sigma$, $S$ and $\lambda_{C}$ were computed according to the ab initio calculation results, from the solution of the Boltzmann transport equation within the relaxation time approximation with the following expressions [47]:

$$
\sigma=e^{2} L^{(0)} \tag{1a}
$$

$$
S=-L^{(1)} /\left(e T L^{(0)}\right) \tag{1b}
$$

$$
\lambda_{C}=1 / T L^{(2)}-S^{2} \sigma T \tag{1c}
$$

where $e$ is the electron charge, and the integrals $L^{(a)}$ is defined as:

$$
L^{(a)}=\int_{-\infty}^{+\infty} d E\left(-\frac{\partial f_{0}}{\partial E}\right) g(E) v(E)^{2} \tau(E)\left(E-E_{f}\right)^{a} \tag{1d}
$$

where $f_{0}$ is Fermi distribution function $(=\{1+\exp([E-E_{f}]/k_{B}T)\}^{-1})$, $E_{f}$ is the Fermi energy, $v(E)$ is the electron velocity $(=1/\hbar\times\nabla_{k}E(k))$, $k$ is the electron wave vector, $g(E)$ is the density of states, and $\tau$ is the total relaxation time with three dominant contributions considered here: scattering by the deformation potential of acoustic and optical phonons, and polar scattering by optical phonons. The expressions for these scattering mechanisms [48,49] were listed below in Eqs. (2a)-(2d). Then the total relaxation time $\tau$ was determined using the Matthiessen's rule ($\tau^{-1}=\tau_{\text{po}}^{-1}+\tau_{\text{o}}^{-1}+\tau_{\text{a}}^{-1}$),

$$
\tau_{p o}=\frac{\left(E+E^{2} / E_{g}\right)^{1 / 2}}{e^{2}\left(2 m^{*}\right)^{1 / 2} k_{B} T\left(\varepsilon_{\infty}^{-1}-\varepsilon_{0}^{-1}\right)\left(1+2 E / E_{g}\right)}\left(1-\delta \ln \left(1+\delta^{-1}\right)-\frac{2 E\left(E+E_{g}\right)}{\left(2 E+E_{g}\right)^{2}}\left[1-2 \delta+2 \delta^{2} \ln \left(1+\delta^{-1}\right)\right]\right)^{-1} \tag{2a}
$$

$$
\tau_{o}=\frac{2 \hbar^{2} a^{2} \rho\left(\hbar \omega_{0}\right)^{2}\left(E+E^{2} / E_{g}\right)^{-1 / 2}}{\pi E_{o c}^{2} k_{B} T\left(2 m^{*}\right)^{3 / 2}\left(1+2 E / E_{g}\right) \Theta} \tag{2b}
$$

$$
\tau_{a}=\frac{2 \pi \hbar^{4} C_{l}\left(E+E^{2} / E_{g}\right)^{-1 / 2}}{E_{a c}^{2} k_{B} T\left(2 m^{*}\right)^{3 / 2}\left(1+2 E / E_{g}\right) \Theta}
\tag{2c}
$$

$$
\Theta=1-\frac{8 E / E_{g}\left(1+E / E_{g}\right)}{3\left(1+2 E / E_{g}\right)^{2}}
\tag{2d}
$$

In these equations, $m^{*}$ is the density-of-states effective mass, $\varepsilon_{\infty}$ and $\varepsilon_{0}$ are the high-frequency and static permittivity values, respectively, $E_{g}$ is the band gap, $a$ is the lattice constant, $\rho$ is the material density, $\omega_{0}$ is the optical phonon frequency, $C_{l}$ is the average elastic constant, $E_{a c}$ and $E_{o c}$ are the acoustic and optical deformation potential constants, respectively. In addition, $\delta=\left(2 k r_{\infty}\right)^{-2}$, where $r_{\infty}$ is the screening length given by $r_{\infty}^{-2}=\frac{e^{2}}{\varepsilon_{\infty}} \int_{0}^{\infty}\left(-\frac{\partial f}{\partial E}\right) g(E) d E$. Values for material constants used in these equations are given in Table 1. These values were obtained by fitting the curves of experimentally measured transport properties of pristine $\beta$-Zn$_{4}$Sb$_{3}$ as a function of temperature [7] with a two-band Kane energy dispersion relation [48], except for the values of $\rho$, $E_{g}$, $a$, and $\varepsilon_{\infty}$ that were taken directly from the literature [7,15].

### 3. Results and discussions

According to our calculation, as presented in Fig. 2, the DOS of Zn$_{36}$Sb$_{30}$ system is partitioned into Sb-s and Zn-$d$ bands, which are bonding inactive, and the valence band (VB) and conduction band (CB) primarily composed of Zn-$s$, $p$ and Sb-$p$ states; The Fermi energy is ~0.35 eV below the VB top with a band gap of about 0.52 eV, which are consistent with the earlier model calculations [47]. The energy origin is chosen to be the top of the valence band of Zn$_{36}$Sb$_{30}$. And for the sake of comparison, the DOS of MZn$_{35}$Sb$_{30}$ (M = Fe/Co/Ni) was shifted by a small amount (~0.4/0.27/0.3 eV) so that the core bands at the lower edge of the valence band DOS of the systems with and without Fe/Co/Ni can match perfectly. It was found that Fe affects the host band greatly and introduce high double resonant peaks in the DOS near the valence band maximum (VBM), as expected, which can be seen clearly in Fig. 2 (a); the two sharp peaks appear at 0.012 eV and 0.269 eV above the VBM. From the calculated total energies one can deduce the formation energies $E_{form}$ of the Fe point defects is ~ −3.58 eV/atom which is defined as [26]:

$$
E_{form}=E_{doped}+\mu_{Zn}-E_{undoped}-\mu_{Fe / Co / Ni}
\tag{3}
$$

here $E_{doped}$ is the total free energy for the supercell containing the dopant (Fe/Co/Ni), $E_{undoped}$ the total free energy for the undoped supercell, and$\mu$ is the chemical potentials of the constituent elements. The partial DOS as shown in Fig. 2 (b) further reveals that the two sharp peaks are both caused mainly by the unique $d$ levels of the Fe atoms which are located at the DOS peaks in energy. In contrast, Co doping, which corresponds to formation energy −3.53 eV/atom, has a little increased density of states near the VBM; while a sharp peak appears near conduction band minimum (CBM), which leads to a considerable enhancement in DOS at 0.658 eV near the CBM. Similarly, after Ni-doping, the DOS has a slightly increased density of states near the VBM and a sharp peak at 0.465 eV appears near the CBM, which shows a very similar behavior to the case with Co doping.

![](./images/812783364976148481_2.jpg)

Fig. 2. The total ((a), (c), and (d)) and partial (b) DOS of Zn$_{36}$Sb$_{30}$ with and without M (M = Fe/Co/Ni). The energy is in respect to the host valence band maximum.

Fig. 3 shows the calculated Seebeck coefficient $S$ and electrical conductivity $\sigma$ of Zn$_{36}$Sb$_{30}$ at T = 300 K as a function of carrier concentration $n$. It can be clearly seen that the calculated $S$ and $\sigma$ agree well with experimentally measured values for pristine $\beta$-Zn$_{4}$Sb$_{3}$ [7,26,49], which indicates that the model applied in the theoretical simulation is reasonable and the predicted transport properties can reflect the reality with enough reliability.

Fig. 4 shows the calculated Seebeck coefficient $S$, electrical

| Table 1 | | | |
| --- | --- | --- | --- |
| Material parameters used to calculate the relaxation times for bulk $\beta$-Zn$_{4}$Sb$_{3}$. $m_{e}$ is the free electron mass. | | | |
| Parameter | Value | Parameter | Value |
| $E_{ac}$ | 30 eV | $\varepsilon_{0}$ | $25.6410 \times 8.85 \times 10^{-12}$ F/m |
| $E_{oc}$ | 30 eV | $\varepsilon_{\infty}$ | $21 \times 8.85 \times 10^{-12}$ F/m |
| $C_{l}$ | $8.1968 \times 10^{10}$ N/m$^{2}$ | $\omega_{0}$ | $2.06 \times 10^{13}$ s$^{-1}$ |
| $m^{*}$ | $0.9\ m_{e}$ | $a$ | $12.231$ Å |
| $E_{g}$ | 1.2 eV | $\rho$ | $6077$ kg/m$^{3}$ |

![](./images/812783364976148481_3.jpg)

Fig. 3. Carrier concentration dependence of the calculated Seebeck coefficient and electrical conductivity for Zn$_{36}$Sb$_{30}$ at T = 300 K; therein the experimental data (solid squares) for $\beta$-Zn$_{4}$Sb$_{3}$ reported in literature [7,23,45] are compared with our calculated results.

![](./images/812783364976148481_4.jpg)

Fig. 4. The variation of thermoelectric properties with carrier concentration at room temperature for $\beta$-Zn₄Sb₃ doped with Fe/Co/Ni. (a) Seebeck coefficient, (b) electrical conductivity, and (c) power factor.

conductivity $\sigma$, and power factor $S^{2}\sigma$ of $\text{MZn}_{35}\text{Sb}_{30}$ ($\text{M} = \text{Fe/Co/Ni}$) as a function of carrier concentration $n$. One can see from Fig. 4 (a) that Seebeck coefficient $S$ for all the compounds increase as carrier concentration decreases, except for the three Fe/Co/Ni-doped cases whose $S$ change their signs as $n < 1.23 \times 10^{27}\text{m}^{-3}$, $n < 0.32 \times 10^{27}\text{m}^{-3}$, and $n < 0.003 \times 10^{27}\text{m}^{-3}$ respectively. However, $S$ of Fe/Co/Ni-doped systems is significantly larger than that of undoped $\beta$-Zn₄Sb₃ in the interesting carrier concentration range. Especially for the three Fe/Co/Ni-doped cases, the maximum $S$ is nearly 60/80/130 times as large as that of $\beta$-Zn₄Sb₃ at $n \approx 1.3 \times 10^{27}\text{m}^{-3}$, $n \approx 0.36 \times 10^{27}\text{m}^{-3}$, and $n \approx 0.004 \times 10^{27}\text{m}^{-3}$ respectively. Certainly, it might be rather difficult and even impossible to obtain so great enhancement in the actual experiments due to the small solubility limit of impurities in $\beta$-Zn₄Sb₃. However, it is not completely impossible because the peaks induced by Fe/Co/Ni doping would be more and more $\delta$-function-like in the DOS as Fe/Co/Ni concentration decreases which could lead to a sharper increase in $S$ according to Mott formula [50]. Anyhow, these results suggest that modifying electronic structure via doping transition elements with $d$ electrons could be an important direction to design new materials with substantially improved thermoelectric performance.

Roughly speaking, electrical conductivity $\sigma$ for four cases all increase as carrier concentration increases as shown in Fig. 4 (b). It was found that electrical conductivity of three doped systems degrades greatly compared with that of undoped $\beta$-Zn₄Sb₃ in the interesting carrier concentration range. Especially for the Fe-doped case, $\sigma$ is nearly less than half that of $\beta$-Zn₄Sb₃ at $n \approx 4 \times 10^{27}\text{m}^{-3}$. Just because of this, Fe doping system achieves a roughly equal optimizing power factor with undoped system as shown in Fig. 4 (c). While for two other Co/Ni doping cases, their optimizing power factors, both enhanced by a factor of almost 1.18/1.12 compared to that of undoped system, occur at $n \approx 1.03 \times 10^{27}\text{m}^{-3}$, and $n \approx 0.33 \times 10^{27}\text{m}^{-3}$, respectively.

The calculated carrier thermal conductivity $\lambda_{C}$ of $\text{MZn}_{35}\text{Sb}_{30}$ ($\text{M} = \text{Fe/Co/Ni}$) is shown in Fig. 5(a). One can see that $\lambda_{C}$ of $\text{MZn}_{35}\text{Sb}_{30}$ ($\text{M} = \text{Fe/Co/Ni}$) has similar change behavior with carrier concentration to that of the electrical conductivity: (a) $\lambda_{C}$ for three doped compounds all increase with carrier concentration increasing; (b) $\lambda_{C}$ of Fe-doped system degrades greatly compared with that of undoped $\beta$-Zn₄Sb₃. Just relying on this point, Fe doping system achieves a roughly equal and high maximum $ZT$ with undoped system as shown in Fig. 5 (b).

Giant peaks in the DOS of Co/Ni-doped compounds bring great enhancement of the Seebeck coefficient and power factor which consequently would result in a sharp increase in the $ZT$. As shown in Fig. 5(b), it is true that the $ZT$ assuming $\lambda_{L} = 0.6\text{Wm}^{-1}\text{K}^{-1}$ (an average experimental value for pristine $\beta$-Zn₄Sb₃) of Co/Ni-doped systems are improved greatly as expected. The maximum $ZT$ for the Co-doped case, appears at $n \approx 1.03 \times 10^{27}\text{m}^{-3}$ near the optimal value of $n$ for maximum power factor, owing to the raising of power factor and the simultaneous declining of carrier thermal conductivity. While the peak of $ZT$ for Ni doping has a large shift to a smaller carrier concentration $3.3 \times 10^{26}\text{m}^{-3}$, which locates just in the range of increased power factor and degraded carrier thermal conductivity. However, the largest room temperature $ZT$ values for Co and Ni doping are still encouraging, which can reach up to 0.18 and 0.17 at $n \approx 1.03 \times 10^{27}\text{m}^{-3}$ or $3.3 \times 10^{26}\text{m}^{-3}$, about 1.21 and 1.13 times larger than the maximum $ZT$ value of undoped system ($ZT \approx 0.15$ at $n \approx 4.5 \times 10^{25}\text{m}^{-3}$), respectively. Therefore, it is

![](./images/812783364976148481_5.jpg)

Fig. 5. Carrier concentration dependence of room temperature thermoelectric parameters for $\beta$-Zn₄Sb₃ doped with Fe/Co/Ni. (a) electronic thermal conductivity, (b) ZT with $\lambda_{L}=$
$0.6\ \text{Wm}^{-1}\text{K}^{-1}$.

reasonable to believe that one can further obtain systems with significant $ZT$ enhancement when combining with other mechanisms (such as alloy scattering or nanostructure [51]) that reduce lattice thermal conductivity.

Taken together, these results suggest that Co-doping is most helpful to enhance the thermoelectric performance of $\beta$-Zn₄Sb₃. To further clarify the details of thermoelectric performance evolution during Fe/Co/Ni doping, the Fermi energy dependence of room temperature carrier concentration $n(E_{\text{F}})$ for MZn35Sb30 (M = Fe/ Co/Ni) are shown in Fig. 6. As the carrier concentration is given by $n(E)=\int g(E)f(E)dE$, where $g(E)$ and $f(E)$ are the carrier density of states (DOS) and the Fermi distribution function, respectively. Thus, carrier concentration $n$ increase with the upward shift of $E_{\text{F}}$ into the valence bands normally originating from an increased DOS of the deeper lying valence bands. In the energy range studied, carrier concentration $n(\text{Fe})>n(\text{Co})>n(\text{Ni})$ for a same $E_{\text{F}}$. From which we can derive $\text{DOS}(\text{Fe})>\text{DOS}(\text{Co})>\text{DOS}(\text{Ni})$ for a same E, in good agreement with those obtained in the above-mentioned DOS calculation (Fig. 2). When room temperature $ZT$ of three compounds MZn35Sb30 (M = Fe/Co/Ni) reach their highest values at $n\approx1.3\times10^{27}\ \text{m}^{-3}$, $n\approx1.03\times10^{27}\ \text{m}^{-3}$ and $3.3\times10^{26}\ \text{m}^{-3}$, respectively, it is found that their corresponding $E_{\text{F}}$ sites are as follows: $E_{\text{F}}(\text{Fe})=0.02\text{eV}$, $E_{\text{F}}(\text{Co})=0.01\text{eV}$ and $E_{\text{F}}(\text{Ni})=0\ \text{eV}$. Their optimal $E_{\text{F}}$ are all located near the host valence band maximum. This condition is consistent with that found to maximize the $ZT$ through introducing resonant states as mentioned in recent research articles [52,53].

![](./images/812783364976148481_6.jpg)

Fig. 6. The dependence of Fermi energy on carrier concentration at room temperature for MZn₃₅Sb₃₀ (M = Fe/Co/Ni). The energy is in respect to the host valence band maximum. Arrows indicate where the best thermoelectric performance is achieved.

## 4. Conclusions

In summary, we have investigated the electronic structure and thermoelectric properties of $\beta$-Zn₄Sb₃ system doped with transition impurities Fe, Co and Ni through self-consistent ab initio electronic structure calculations within density functional theory and the Boltzmann transport equation within the relaxation time approximation. The calculations for Fe/Co/Ni-doped systems indicated that these atoms with $d$-electrons could introduce high sharp resonant peaks in the DOS near the valence band maximum or conduction band minimum, which could result in a boost Seebeck coefficient and a significantly suppressed conductivity. And consequently, significant reduction in carrier thermal conductivity leads to the enhancement of thermoelectric performance for $\beta$-Zn₄Sb₃ system. Moreover, the corresponding $E_{\text{F}}$ of the maximal $ZT$ are all located near the host valence band maximum. We expect that further enhancement would be achieved by combining with other mechanisms (such as double-element-doping) that can further increase the conductivity.

## Acknowledgments

This work was supported by the National Natural Science Foundation of China (Grants No. 11674322, No. 51672278), Program for Innovative Research Team (in Science and Technology) in University of Yunnan Province, and the Center for Computational Science, Hefei Institutes of Physical Sciences.

## References

[1] B.C. Sales, D. Mandrus, R.K. Williams, Science 272 (1996) 1325.
[2] Rama Venkatasubramanian, Edward Siivola, Thomas Colpitts, O'Quinn Brooks, Nature 413 (2001) 597.
[3] G. Mahan, B. Sales, J. Sharp, Phys. Today 50 (3) (1997) 42.
[4] a Terry M. Tritt, Science 272 (1996) 1276;
b Terry M. Tritt, Science 283 (1999) 804.
[5] Sabah K. Bux, Richard G. Blair, Pawan K. Gogna, Hohyun Lee, Gang Chen, Mildred S. Dresselhaus, Richard B. Kaner, Jean-Pierre Fleurial, Adv. Funct. Mater. 19 (2009) 2445.
[6] a Franck Gascoin, Sandra Ottensmann, Daniel Siossina M. Haïle, G. Jeffrey Snyder, Adv. Funct. Mater. 15 (2005) 1860;
b Yanzhong Pei, Jessica Lensch-Falk, Eric S. Toberer, Douglas L. Medlin, G. Jeffrey Snyder, Adv. Funct. Mater. 21 (2011) 241.
[7] T. Caillat, J.-P. Fleurial, A. Borshchevsky, J. Phys. Chem. Solids 58 (1997) 1119.
[8] Yang Wu, Johanna Nylén, Naseyowma Craig, N. Newman, J. Francisco, Garcia-Garcia, Ulrich Häussermann, Chem. Mater. 21 (2009) 151.
[9] G.J. Snyder, M. Christensen, E. Nishibor, T. Caillat, B.B. Iversen, Nat. Mater. 3 (2004) 458.
[10] F. Cargnoni, E. Nishibori, P. Rabiller, L. Bertini, G.J. Snyder, M. Christensen, C. Gatti, B.B. Iversen, Chem. Eur. J. 10 (2004) 3861.
[11] W. Schweika, R.P. Hermann, M. Prager, J. PerrSon, V. Keppens, Phys. Rev. Lett. 99 (2007), 125501.

[12] S.C. Ur, P. Nash, I.H. Kim, J. Mater. Sci. 38 (2003) 3553.

[13] T.H. Zou, X.Y. Qin, D. Li, G.L. Sun, Y.C. Dou, Q.Q. Wang, B.J. Ren, J. Zhang, H.X. Xin, Y.Y. Li, Appl. Phys. Lett. 104 (2014), 013904.

[14] Duc-The Ngo, Le Thanh Hung, Ngo Van Nong, ChemPhysChem 19 (2018) 108.

[15] A.P. Litvinchuk, J. Nylén, B. Lorenz, A.M. Guloy, U. Häussermann, J. Appl. Phys. 103 (2008), 123524-1.

[16] T. Koyanagi, K. Hino, Y. Nagamoto, H. Yoshitake, K. Kishimoto, in: 16th In- ternational Conference on Thermoelectrics, 1997, p. 463.

[17] Thierry Caillat, Jean-Pierre Fleurial, IEEE 2 (1996) 905.

[18] Kyung-Wook Jang, Il-Ho Kim, Jung-Il Lee, Good-Sun Choi, Int. Conf. Thermo- electr. 129 (2005).

[19] J.L. Cui, L.D. Mao, D.Y. Chen, X. Qian, X.L. Liu, W. Yang, Curr. Appl. Phys. 9 (2008) 713.

[20] J.L. Cui, H. Fu, D.Y. Chen, L.D. Mao, X.L. Liu, W. Yang, Mater. Char. 60 (2009) 824.

[21] D. Li, H.H. Hong, J. Ma, X.Y. Qin, J. Mater. Res. 24 (2009) 430.

[22] a F. Liu, X.Y. Qin, D. Li, J. Phys. D Appl. Phys. 40 (2007) 4974;
b F. Liu, X.Y. Qin, H.X. Xin, J. Phys. D Appl. Phys. 40 (2007) 7811.

[23] G. Nakamotom, T. Souma, M. Yamaba, M. Kurisu, J. Alloys Compd. 377 (2004) 59.

[24] B.L. Pedersen, H. Birkedal, E. Nishibori, A. Bentien, M. Sakata, M. Nygren, P.T. Frederiksen, B.B. Iversen, Chem. Mater. 19 (2007) 6304.

[25] B.L. Pedersen, H. Birkedal, M. Nygren, P.T. Frederiksen, B.B. Iversen, J. Appl. Phys. 105 (2009) 013517.

[26] a M. Liu, X.Y. Qin, C.S. Liu, L. Pan, H.X. Xin, Phys. Rev. B 81 (2010), 245215;
b X.Y. Qin, M. Liu, L. Pan, H.X. Xin, J.H. Sun, Q.Q. Wang, J. Appl. Phys. 109 (3) (2011), 033714.

[27] Tianhua Zou, Xiaoying Qin, Yongsheng Zhang, Xiaoguang Li, Zhi Zeng, Di Li, Jian Zhang, Hongxing Xin, Wenjie Xie & Anke Weidenkaff, Sci. Rep., 5, 17803.

[28] W. Li, L.M. Zhou, Y.L. Li, J. Jiang, G.J. Xu, J. Alloys Compd. 486 (2009) 335.

[29] D. Li, X.Y. Qin, Intermetallics 19 (2011) 1651.

[30] L. Pan, X.Y. Qin, M. Liu, Solid State Commun. 150 (2010) 346.

[31] L. Pan, X.Y. Qin, M. Liu, Solid State Sci. 12 (2010) 257.

[32] L. Pan, X.Y. Qin, H.X. Xin, D. Li, J.H. Sun, J. Zhang, C.J. Song, R.R. Sun, In- termetallics 18 (2010) 1106.

[33] Lirong Song, Anders B. Blichfeld, Jiawei Zhang, Hidetaka Kasaic, Bo B. Iversen, J. Mater. Chem. A 6 (2018) 4079.

[34] J. Nylén, S. Lidin, M. Andersson, B.B. Iversen, H. Liu, N. Newman, U. Häussermann, Chem. Mater. 19 (2007) 834.

[35] S. Bhattacharya, R.P. Hermann, V. Keppens, T.M. Tritt, G.J. Snyder, Phys. Rev. B 74 (2006), 134108.

[36] Soon-Chul Ura, Il-Ho Kima, Philip Nash, Mater. Lett. 58 (2004) 2132.

[37] B.L. Pedersen, H. Birkedal, B.B. Iversena, M. Nygren, P.T. Frederiksen, Appl. Phys. Lett. 89 (2006), 242108.

[38] Y. Mozharivskyj, Y. Janssen, J.L. Harringa, A. Kracher, A.O. Tsokol, G.J. Miller, Chem. Mater. 18 (2006) 822.

[39] Go Nakamoto, K. Kinoshita, M. Kurisu, J. Appl. Phys. 105 (2009), 013713.

[40] J.P. Heremans, V. Jovovic, E.S. Toberer, A. Saramat, K. Kurosaki, A. Charoenphakdee, S. Yamanaka, G.J. Snyder, Science 321 (2008) 554.

[41] C.M. Jaworski, V. Kulbachinskii, J.P. Heremans, Phys. Rev. B 80 (2009), 233201.

[42] G.D. Mahan, J.O. Sofo, Proc. Natl. Acad. Sci. U.S.A. 93 (1996) 7436.

[43] P.E. Blöchl, Phys. Rev. B 50 (1994) 17953.

[44] G. Kresse, D. Joubert, Phys. Rev. B 59 (1999) 1758.

[45] J.P. Perdew, K. Burke, M. Ernzerhof, Phys. Rev. Lett. 77 (1996) 3865.

[46] a D.M. Rowe, C.M. Bhandari, Modern Thermoelectrics, Holt Saunders, London, 1983;
b Jiong Yang, Huanming Li, Ting Wu, Wenqing Zhang, Lidong Chen, Jihui Yang, Adv. Funct. Mater. 18 (2008) 2880.

[47] B.R. Nag, Electron Transport in Compound Semiconductors, Springer-Verlag, Berlin, 1980, pp. 93-128.

[48] G.S. Nolas, J.W. Sharp, H.J. Goldsmid, Thermoelectrics: Basics Principles and New Materials Developments, Springer-Verlag, Heidelberg, 2001.

[49] Eric S. Toberer, a Protima Rauwel, b Sylvain Gariel, a J. Taftøb, G. Jeffrey Snyder, J. Mater. Chem. 20 (2010) 9877.

[50] N.F. Mott, E.A. Davis, Electronic Process is in Noncrystalline Materials, Clar- endon, Oxford, 1971.

[51] a Jiaqing He, Steven N. Girard, Mercouri G. Kanatzidis, Vinayak P. Dravid, Adv. Funct. Mater. 20 (2010) 764;
b Bruce A. Cook, Matthew J. Kramer, Joel L. Harringa, Mi-Kyung Han, Duck- Young Chung, Mercouri G. Kanatzidis, Adv. Funct. Mater. 19 (2009) 1254.

[52] M. Liu, X.Y. Qin, C.S. Liu, Z. Zeng, Appl. Phys. Lett. 99 (2011), 062112.

[53] S. Thebaud, Ch. Adessi, S. Pailhes, G. Bouzerar, Phys. Rev. B 96 (2017), 075201.
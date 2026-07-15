![](./images/811845070704607234_1.jpg)

# The optimum lead thickness for lead-activation detectors

Si Fenni *, Hu Qingyuan

Institute of Nuclear Physics and Chemistry, China Academy of Engineering Physics, Mianyang 621900, China

---

## ARTICLE INFO

**Article history:**
Received 6 May 2009
Received in revised form 11 June 2009
Available online 23 June 2009

**PACS:**
25.40.Ep
25.20.Dc
25.30.Fj
24.10.Lx

**Keywords:**
The optimum lead thickness
Lead-activation detector
MCNP5
Mathematical estimation

---

## ABSTRACT

The optimum lead thickness for lead-activation detectors has been studied in this paper. First existence of the optimum lead thickness is explained theoretically. Then the optimum lead thickness is obtained by two methods, MCNP5 calculation and mathematical estimation. At last factors which affect the optimum lead thickness are discussed. It turns out that the optimum lead thickness is irrelevant to incident neutron energies. It is recommended 2.5 cm generally.

© 2009 Elsevier B.V. All rights reserved.

---

## 1. Introduction

The activation technique has been used widely to measure influence of pulsed neutron sources [1–9]. Many elements can be chosen as active materials [10]. Lead-activation detector, with the advantages of high sensitivity, large dynamical range, appropriate threshold and quick operating speed field, is designed to measure yield of pulsed neutron sources [1,2,11]. The lead-activation detectors are especially used to measure neutron yield of DPF device. DPF (dense plasma focus) device is a pulsed neutron source produced by D(d,n)He³ (or D(d,n)He⁴) reactions. The detecting process of the lead-activation detector is: incident neutrons interact with Pb, resulting radioactive nuclide. The radioactive nuclide decay $\gamma$ rays, which are counted by the lead-activation detector. At the same time Pb captures $\gamma$ rays greatly, for which it is usually used to shield $\gamma$ rays. Spencer's experiment has shown that there exists an optimum lead thickness at which the lead-activation detector encounters its highest efficiency [2]. When the lead thickness is bigger or smaller than the optimum, the detection efficiency decreases. The lead thickness is very important as it affects the detection sensitivity greatly. Ruby's paper has given a set of ordinary differential equations to find the optimum lead thickness for 14 MeV neutrons [1]. However, Spencer and Ruby have only considered the 14 MeV neutrons. Ruby neither has described the detailed physical process of deriving the equations, nor has given the initial conditions of the equations.

What's more, there is no paper calculating the optimum lead thickness for lead-activation detectors in a wide range of neutron energies (except 14 MeV). MCNP calculations can supply this gap. MCNP is a popular code to solve the transportation of neutrons, photos, electrons and coupled particles [12–15]. In this paper MCNP, version 5, is used to do calculations.

This paper is a further study of the lead-activation detector designed by Spencer. The existence and relevant properties of the optimum lead thickness for 14 MeV neutrons are first studied by MCNP5 calculations and mathematical estimation. At last the optimum lead thickness is calculated by MCNP5 for neutrons with a wide range of energies.

## 2. Theoretical analysis of the optimum lead thickness

There are mainly four kinds of reactions when the natural lead is irradiated by neutrons. Pb²⁰⁴(n,n')Pb²⁰⁴ᵐ (68 min half-time), Pb²⁰⁶(n,2n)Pb²⁰⁵ᵐ (5 ms half-time), Pb²⁰⁷(n,n')Pb²⁰⁷ᵐ (1.6 MeV threshold, 0.84 s half-time) and Pb²⁰⁸(n,2n)Pb²⁰⁷ᵐ (8 MeV threshold, 0.84 s half-time). The counting interval of the lead-activation detector is started 20 ms after the neutron pulse and extends for a period of 2.4 s. Counts of Pb²⁰⁴(n,n')Pb²⁰⁴ᵐ and Pb²⁰⁶(n,2n)Pb²⁰⁵ᵐ can be neglected. The lead-activation detector essentially measures

---

* Corresponding author.
E-mail address: sifenni@gmail.com (S. Fenni).

0168-583X/$ - see front matter © 2009 Elsevier B.V. All rights reserved.
doi:10.1016/j.nimb.2009.06.108

![](./images/811845070704607234_2.jpg)

neutron yield by counting $\gamma$ rays of $\text{Pb}^{207m}$. $\text{Pb}^{207m}$ has two levels, 1.635 MeV and 0.571 MeV, thereby producing $\gamma$ rays of 1.064 and 0.571 MeV. These two kinds of $\gamma$ rays are attenuated greatly in the lead. There are mainly three kinds of reactions when the lead are irradiated by the two kinds of $\gamma$ rays, photoemission, compton absorbtion and pair production. All these reactions can cause 1.064 and 0.571 MeV $\gamma$ rays lost greatly. However, photoemission, comp- ton absorbtion and pair production all can produce electrons, which creates $\gamma$ rays through bremsstrahlung and $p$-annihilation. On all accounts, counts of the lead-activation detector are contrib- uted by $\gamma$ decays of $\text{Pb}^{207m}$ and bremsstrahlung of sub-electrons.

## 3. MCNP5 calculations of the optimum lead thickness for 14 MeV neutrons

The geometrical construction of the lead-activation detector for MCNP5 simulations in this paper is shown in Fig. 1. It is derived from the detector designed by Spencer. The lead sheath is practi- cally a cylinder of 22 cm long and 12 cm inner diameter. It consists of three parts, the front window, the side window and the back window. The neutron source is located 15 cm far away normal to the front window.

During MCNP5 calculations, Mn card is filled with the natural lead. The point detector F5, located at the center of the lead sheath, is used to count $\gamma$ rays. The neutron source is an isotropic 14 MeV point source and has a standard Gaussian distribution in time whose FWHM is 20 ns. NPS is $10^7$.

First, contribution of the back window is calculated. Results show that the back window contributes little to the total counts, about 1%. So contribution of the back window is ignored during MCNP5 calculations. Thus the geometrical model of the lead detec- tor is simplified as Fig. 2 in the following calculations.

Next, contribution by bremsstrahlung of sub-electrons is calcu- lated. This is carried out by defining the PHYS card in MCNP5. Re- sults show that contribution by bremsstrahlung of sub-electrons is no more than 3% of the total counts. When bremsstrahlung of sub- electrons is considered in MCNP5 calculation, it takes more than 4 h to finish $10^7$ NPS. On contrary, if it is ignored, only 3 min are needed to finish the same $10^7$ NPS. We mainly focus on the opti- mum thickness of the lead sheath, which corresponds to the high- est efficiency of the lead-activation detector. As long as the relative efficiencies of different thicknesses are known, the optimum lead thickness can be obtained. So bremsstrahlung of sub-electrons is ignored during MCNP5 calculations in the following.

At last, the optimum thickness of the lead sheath for 14 MeV neutrons is calculated, shown in Fig. 3. Efficiencies for different thicknesses of lead are normalized by regarding the maximum effi- ciency as 1. The horizontal axis is the thickness of lead, and the ver- tical axis is the normalized efficiency $\epsilon$. It is obvious to see that there exists an critical point, shown as the big black point, in Fig. 3. The critical point indicates the maximum detection effi- ciency, corresponding to which is the optimum lead thickness. In this paper, the optimum lead thickness is 2.5 cm for 14 MeV neu- trons calculated by MCNP5.

![](./images/811845070704607234_3.jpg)

Fig. 1. Geometrical structure of the lead-activation detector.

![](./images/811845070704607234_4.jpg)

Fig. 2. Calculated geometrical structure of the lead-activation detector.

![](./images/811845070704607234_5.jpg)

Fig. 3. MCNP5 calculations of the optimum lead thickness for 14 MeV neutrons.

## 4. Mathematical estimation of the optimum lead thickness

The above sections, both theoretical analysis and MCNP5 calcu- lations, show that there exists an optimum lead thickness. And MCNP5 calculations have given the value of the optimum lead thickness. In this section the optimum lead thickness will be esti- mated mathematically. The incident neutrons with total inelastic cross section $\Sigma_n$ interact with a cross section $\Sigma_3$ to form $\text{Pb}^{207m}$, which produces 0.571 and 1.064 MeV $\gamma$ rays of attenuation coeffi- cient $\Sigma_1$ (0.57 MeV) and $\Sigma_2$ (1.064 MeV). Bremsstrahlung of the sub-electrons is neglected as its contribution is very small (see MCNP5 calculations section). Detection efficiency of the two $\gamma$ rays is assumed to be equal. As a result the following ordinary differen- tial equations are created:

$$
\frac{dN_n}{dx} = -\Sigma_n N_n, \tag{1}
$$

$$
\frac{dN_1}{dx} = -\Sigma_3 N_n - \Sigma_1 N_1, \tag{2}
$$

$$
\frac{dN_2}{dx} = -\Sigma_3 N_n - \Sigma_2 N_2, \tag{3}
$$

with initial conditions,

$$
\begin{cases}
N_n(0) = N_0, \\
N_1(0) = 0, \\
N_2(0) = 0,
\end{cases} \tag{4}
$$

where $N_n$ is the number of incident neutrons. $N_1$ and $N_2$ are the number of 0.57 and 1.064 MeV $\gamma$ rays, respectively. $x$ is the lead thickness.

![](./images/811845070704607234_6.jpg)

Solutions of Eqs. (1)-(3) are:
$$
N_{n}=N_{0}e^{-\Sigma_{n}x}, \tag{5}
$$

$$
\epsilon_{1}=\frac{\Sigma_{3}}{\Sigma_{n}-\Sigma_{1}}\left(e^{-\Sigma_{1}x}-e^{-\Sigma_{n}x}\right), \tag{6}
$$

$$
\epsilon_{2}=\frac{\Sigma_{3}}{\Sigma_{n}-\Sigma_{2}}\left(e^{-\Sigma_{2}x}-e^{-\Sigma_{n}x}\right), \tag{7}
$$

where $\epsilon_{1}=\frac{N_{1}}{N_{0}}$ and $\epsilon_{2}=\frac{N_{2}}{N_{0}}$, $\epsilon=\epsilon_{1}+\epsilon_{2}$ is defined, which is just the efficiency of the lead-activation detector.

Eqs. (5)-(7) are plotted in Fig. 4, which shows how the detection efficiency varies with the lead thickness. From Fig. 4, there must exists an optimum lead thickness at which the detection efficiency reaches its maximum.

The optimum lead thickness is decided by the condition Eq. (8). Add Eq. (8) to Eqs. (5)-(7) and (9) is generated. The optimum lead thickness is just obtained from Eq. (9). For 14 MeV neutrons, cross sections and attenuation coefficients are shown in Eq. (10). The optimum lead thickness for 14 MeV neutrons is 2.8 cm.
$$
\frac{d\left(\epsilon_{1}+\epsilon_{2}\right)}{dx}=0, \tag{8}
$$

$$
\frac{\Sigma_{n}e^{-\Sigma_{n}x}-\Sigma_{1}e^{-\Sigma_{1}x}}{\Sigma_{n}-\Sigma_{1}}+\frac{\Sigma_{n}e^{-\Sigma_{n}x}-\Sigma_{2}e^{-\Sigma_{2}x}}{\Sigma_{n}-\Sigma_{2}}=0, \tag{9}
$$

$$
\begin{cases}
\Sigma_{n}=0.085\ \text{cm}^{-1}, \\
\Sigma_{3}=0.0185\ \text{cm}^{-1}, \\
\Sigma_{1}=1.83\ \text{cm}^{-1}, \\
\Sigma_{2}=0.77\ \text{cm}^{-1}.
\end{cases} \tag{10}
$$

There are minor differences of the results between MCNP5 calculations and mathematical estimation, which is because that mathematical estimation has some assumptions. First, it assumes the equal detection efficiency of 0.57 and 1.064 MeV $\gamma$ rays. Second, it doesn't consider the detailed construction of the lead-activation detector. Third, it assumes that incident neutrons are homogeneously distributed in the lead. On all acounts MCNP5 calculations and mathematical estimation agree well in obtaining the optimum lead thickness.

## 5. The optimum lead thickness for 2-14 MeV neutron sources

Eq. (9) indicates that the optimum lead thickness is decided by just three factors, $\Sigma_{n}$, $\Sigma_{1}$ and $\Sigma_{2}$. Whatever energy of the incident neutrons, only 0.571 and 1.064 MeV gamma decays of Pb$^{207m}$ contribute to the final counts of the lead-activation detector, so $\Sigma_{1}$ and $\Sigma_{2}$ are constant for different neutron energies. The optimum lead thickness is only decided by $\Sigma_{n}$ which is closely pertinent to neutron energies. Consequently, the optimum lead thickness is only decided by the incident neutron energy for a formed lead-activation detector.

Fig. 5 shows the relationship between the optimum lead thickness $x^{*}$ and the neutron cross section $\Sigma_{n}$, deriving from Eq. (9). When $\Sigma_{n}$ is between 0 and 0.02, the optimum lead thickness changes greatly. While $\Sigma_{n}$ is bigger than 0.02, the optimum lead thickness varies little and tends to a constant.

At last the optimum lead thicknesses for 2-14 MeV neutrons are calculated by MCNP5, shown in Fig. 6. The optimum lead thickness is irrelevant to incident neutron energies. It is a constant of 2.5 cm for different neutron energies. Hence, we are delighted and fortunate to conclude that once the lead-activation detector is established, its size can be confirmed to detect neutron sources with different energies.

## 6. Summary and concluding remarks

This paper mainly focuses on the optimum lead thickness of the lead-activation detector. The simplified geometrical structure of the detector is derived from the one designed by Spencer [2]. First existence of the optimum lead thickness is explained theoretically. Then two methods are used to obtain the optimum lead thickness, MCNP5 calculation and mathematical estimation. Discarding dif-

![](./images/811845070704607234_7.jpg)

![](./images/811845070704607234_8.jpg)

ferent assumptions and abbreviations, results of the two methods agree well. At last factors affecting the optimum lead thickness are discussed. It turns out that the optimum lead thickness is irrel- evant to incident neutron energies and only decided by the inelas- tic neutron cross section $\Sigma_{n}$. The optimum lead thickness is recommended 2.5 cm generally. Once the lead-activation detector is established, the size can be fixed to detect neutron sources with different energies.

## References

[1] L. Ruby, J.B. Rechen, Nucl. Instrum. Meth. 15 (1962) 74.
[2] C.E. Spencer, E.L. Jacobs, Nucl. Instrum. Meth. 15 (1965) 407.
[3] L. Ruby, J.B. Rechen, Nucl. Instrum. Meth. 53 (1967) 290.
[4] R.H. Howell, Nucl. Instrum. Meth. 148 (1978) 39.

[5] D.R. Slaugher, W.L. Pickles, Nucl. Instrum. Meth. 160 (1979) 87.
[6] I. Tiseanu, N. Mandache, V. Zambreanu, Plasma Phys. Controlled Fusion 36 (1994) 417.
[7] R.K. Rout, A. Shyam, V. Chitra, Ann. Nucl. Eng. 18 (1991) 357.
[8] E.J.T. Burns, S.M. Falacy, R.A. Hill, et al., Nucl. Instrum. Meth. 40 (1989) 1248.
[9] M. Tobin, P. Song, UCRL-JC-155366, in: Third International Conference on Inertial Fusion Sciences and Applications, 2003.
[10] K. Boyer, W.C. Elmore, E.M. Little, W.E. Quinn, J.L. Tuck, Phys. Rev. 119 (1960) 831.
[11] C. Yang, J. Feng, C. Su, et al., in: 33rd IEEE International Conference on Plasma Science, Vol. 4, 2006, p. 232.
[12] T. Bouassoule, F. Fernandez, M. Tomas, et al., Radiat. Meas. 34 (2001) 199.
[13] K. Shtejer-Diaz, C.B. Zamboni, G.S. Zahn, J.Y. Zevallos-Chavez, Appl. Radiat. Isot. 59 (2003) 263.
[14] C.J. Evans, S.J.S. Ryde, D.A. Hancock, F. Al-agel, Appl. Radiat. Isot. 49 (1998) 541.
[15] L.C.-A. Bourva, S. Croft, H. Ottmar, D.R. Weaver, Nucl. Instrum. Meth. A 426 (1999) 503.
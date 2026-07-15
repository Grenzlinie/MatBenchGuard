Accepted Manuscript

Research paper

Heterogeneous nucleation and dendritic growth within undercooled liquid niobi-
um under electrostatic levitation condition

S.J. Yang, L. Hu, L. Wang, B. Wei

![](./images/813124643761160193_1.jpg)

| PII:          | S0009-2614(17)30600-0                                                                 |
|---------------|---------------------------------------------------------------------------------------|
| DOI:          | http://dx.doi.org/10.1016/j.cplett.2017.06.046                                        |
| Reference:    | CPLETT 34908                                                                          |
| To appear in: | *Chemical Physics Letters*                                                             |
| Received Date:| 5 June 2017                                                                           |
| Revised Date: | 19 June 2017                                                                          |
| Accepted Date:| 22 June 2017                                                                          |

Please cite this article as: S.J. Yang, L. Hu, L. Wang, B. Wei, Heterogeneous nucleation and dendritic growth within undercooled liquid niobium under electrostatic levitation condition, *Chemical Physics Letters* (2017), doi: http://dx.doi.org/10.1016/j.cplett.2017.06.046

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Heterogeneous nucleation and dendritic growth within undercooled liquid niobium under electrostatic levitation condition

S. J. Yang, L. Hu, L. Wang, B. Wei¹

Department of Applied Physics, Northwestern Polytechnical University, Xi'an 710072, China

Abstract: The physical mechanisms of crystal nucleation and dendritic growth within undercooled niobium were systematically studied by electrostatic levitation and molecular dynamics methods. The maximum undercooling was achieved as 454 K (0.16$T_\text{m}$), while the hypercooling limit was determined as 706 K (0.26$T_\text{m}$). The undercooling probability displayed Poisson distribution and indicated the occurrence of heterogeneous nucleation. The calculated critical nucleus size reduced rapidly with undercooling and the solid-liquid interface energy was deduced to be 0.367 J m⁻². In addition, the dendritic growth velocity of pure niobium exhibited a power relation versus undercooling, and reached 41 m s⁻¹ at the maximum undercooling.

Keywords: Crystal nucleation; Dendritic growth; Liquid undercooling; Refractory metal

## 1. Introduction

Crystal nucleation and dendritic growth, which are the most fundamental stages of solidification process, have aroused great research interests due to their important roles on controlling the phase constitutions and structural morphologies of metallic materials. ¹⁻⁵ Thermodynamically, nucleation and subsequent dendritic growth from metallic melt both need undercooling as the driving force. ⁶ With the undercooling increase, the Gibbs free energy of the undercooled melt remarkably departs away from that in equilibrium state. Therefore, the nucleation and dendrite growth kinetics must display different physical laws with the change of undercooling status.

Since the undercooling state is very sensitive to the external heterogeneous sites, i.e., container and oxidation

---

¹ Corresponding author
E-mail address: bwei@nwpu.edu.cn (B. Wei)

products. The containerless processing techniques have been adopted to achieve the undercooled state of liquid metals.

Although studies on high temperature metals and alloys have been performed by means of levitation methods, $^{5,7-9}$ more work still needs to be done to better understand their basic mechanisms for refractory metals. Among the refractory metals, only the nucleation mechanism of undercooled pure Zr has been systematically researched. Morton et al $^{10}$ studied the nucleation of undercooled Zr by statistical approach in electrostatic levitation, electromagnetic levitation and drop tube, which suggest the same heterogeneous nucleation mechanism in all the three methods. In the aspect of the thermodynamics, the nucleation rate and dendritic growth velocity are important to explore the nucleation and dendritic growth mechanism under containerless state. Besides, because nucleation and dendritic growth both take place at the solid-liquid interface, the solid-liquid interface energy is a fundamental physical parameter for revealing the nucleation process and growth kinetics as well. However, it is extremely difficult to be measured by experiments.

The objective of this work is to investigate the nucleation mechanisms and dendritic growth kinetics within undercooled refractory niobium by electrostatic levitation (ESL) experiments. Moreover, the critical nucleus size and the solid-liquid interface energy are calculated based on the molecular dynamics (MD) simulations with the potential function verified by the measured and calculated thermophysical properties of liquid niobium.

## 2. Material and methods

The experiments were carried out by electrostatic levitation technique under high vacuum environment $(10^{-5}\ \text{Pa})$. The details of our ESL facility are described elsewhere. $^{11,12}$ The samples of pure Nb (99.95% in purity) about 2.5 mm in diameter were levitated by the electrostatic force and then heated by a SPI SP300 fiber laser. The temperature of sample was monitored by a CellaTemp PA40 pyrometer and calibrated with the melting point of Nb. A typical temperature-time curve of one heating-cooling cycle is shown in Fig. 1(a). When the temperature of levitated sample reached 2750 K, a melting plateau appeared and then the sample turned into molten state. After overheated for a few seconds, the sample was cooled down by turning off the heating laser. In the cooling process, the images of levitated sample were recorded by

![](./images/813124643761160193_2.jpg)

Fig. 1 Containerless processing of pure Nb in ESL experiments: (a) typical temperature-time curve; (b) the probability distribution of undercooling for pure Nb from 200 heating-cooling cycles; (c) the relationship between $F$ and undercooling; (d) measured solidification plateau time versus undercooling.

a black/white camera with a background light source to calculate the density of Nb. As the sample temperature decreased

below the melting point, nucleation and recalescence phenomena occurred at a certain undercooling $\Delta T$. The recalescence

process was captured by a Redlake HG-100K high speed camera to measure the dendritic growth velocity. The

subsequent plateau demonstrates the solidification of residual melts. Afterwards, the sample was totally solidified and the next cycle was prepared.

The simulations were executed by molecular dynamics method with the EAM potential function of pure Nb, which was created by Fellinger et al. $^{13}$ In order to verify if this EAM potential is valid to determine the liquid properties of pure Nb, the melting point and density of Nb in liquid state were calculated firstly. The melting point was obtained by sandwich model with a solid-liquid-solid interface structure. The liquid density of pure Nb was calculated from the volume of a supercell containing 16,000 atoms. Initially, the system was turned into liquid state at 4000 K, which was far beyond the melting point. Then it was cooled down step by step from 4000 K to 1400 K with the interval of 100 K. At each temperature step, the system was equilibrated about 200 ps to obtain the volume. Afterwards, the nucleation process was carried out to determine the critical nucleus size of undercooled liquid Nb at different undercoolings. The system of a nucleus surrounded by undercooled liquid was constructed, which consisted of 16,000 atoms. In the thermal relaxation process at a certain temperature below the melting point, the number of atoms in the prepared crystal nucleus was added one by one. When the number reached a critical value, the system transformed into ordered solid. This value was just the number of atoms in the critical nucleus and the solid-liquid interface energy is derived from it. All the calculations were employed by the LAMMPS code package$^{14}$. The isothermal-isobaric (NPT) ensemble and periodic boundary condition were used in the simulation process with the time step of 2 fs.

## 3. Results and discussion

### 3.1 Crystal nucleation and dendritic growth

In ESL experiments, the crystal nucleation from undercooled liquid Nb is a random process, which obeys the Poisson distribution. Fig. 1(b) shows the statistical result from 200 heating-cooling cycles. It is found that majority of undercoolings lie in the range of 414-454 K with the most probable value of 438 K. Within the undercooling range from 0 to 414 K, the nucleation takes place only 10 times. It agrees with the classical nucleation theory that the probability of

nucleation event is particularly little at small undercoolings.

From the statistical result, the parameters in the nucleation rate function $I$ can be derived. The form of $I$ is expressed as⁶

$$
I=K_{\mathrm{v}} \exp \left(-\frac{\Delta G^{*}}{k_{\mathrm{B}} T}\right) \tag{1}
$$

where $K_{\mathrm{V}}$ is the pre-exponential factor, $\Delta G^{*}$ is the activation energy of nucleation, $k_{\mathrm{B}}$ is the Boltzmann constant, and $T$ is the temperature.

Because the nucleation phenomenon in ESL is under non-isothermal conditions, its probability density function is described as¹⁰,¹⁵

$$
\omega=\frac{I V}{R_{\mathrm{c}}} \exp \left(\int_{T_{\mathrm{m}}}^{T} \frac{I V}{R_{\mathrm{c}}} \mathrm{d} T\right) \tag{2}
$$

where $\omega$ is the probability for one nucleation event in the temperature interval $T$ and $T+\delta T, V$ is the sample volume, $R_{\mathrm{c}}$ is the cooling rate, which is defined as -d$T$/d$t$ and calculated from the cooling curve. Then the cumulative distribution function $F$ is obtained from Eq. (2) with the assumption that $K_{\mathrm{V}}$ insensitively depends on temperature and the volume free energy have a linear relation with temperature¹⁶,

$$
F=1-\exp \left[-\frac{V K_{\mathrm{V}} \Delta T^{3} T^{2}}{K R_{\mathrm{c}}\left(3 T-T_{m}\right)} \exp \left(-\frac{K}{\Delta T^{2} T}\right)\right] \tag{3}
$$

where $T_{\mathrm{m}}$ is the melting point of Nb, and $K$ is a constant.

As displayed in Fig. 1(c), the plot of $\ln[-\ln(1-F)]$ versus $1/(\Delta T^{2}T)$ yields to a linear relationship in the undercooling range of 414-454 K, which indicates a single nucleation mechanism. The values of $K$ can be determined from the slope. Meanwhile, $K_{\mathrm{V}}$ and $\Delta G^{*}$ are derived from the intercept of fitted line at the most probable nucleation undercooling $\Delta T_{\mathrm{P}}$ of 438 K. In present work, the obtained $K_{\mathrm{V}}$ and $\Delta G^{*}$ are $1.02×10^{30}\ \text{m}^{-3}\ \text{s}^{-1}$ and $47.73k_{\mathrm{B}}T$, respectively. With the two values, the probability density function $\omega$ is plotted in Fig. 1(b), and it provides a good description of the undercooling distribution data.

Morton et al. $^{10}$ have also investigated the nucleation phenomena of pure Nb with the statistical approach by drop tube. The undercooling distributes in the range of 414-438 K with $\Delta T_{\mathrm{p}}$ of 428 K. The values of $K_{\mathrm{V}}$ and $\Delta G^{*}$ that they obtained are $10^{31} \mathrm{~m}^{-3} \mathrm{~s}^{-1}$ and $73.2 k_{\mathrm{B}} T$, correspondingly. For comparison, the present $\Delta G^{*}$ is smaller than theirs, but the values of $K_{\mathrm{V}}$ are close to each other.

Based on the theory of Turnbull $^{16}$, the pre-exponential factor $K_{\mathrm{V}}$ is about $10^{39} \mathrm{~m}^{-3} \mathrm{~s}^{-1}$ for homogeneous nucleation. It is obvious that our result is far away from that value, and it indicates that heterogeneous nucleation may be the dominating crystallization mechanism during the present ESL experiments. According to the observation of recalescence process captured by the high speed camera in Fig. 2(b), the onset of recalescence appears on the surface of sample, which manifests the heterogeneous nucleus site.

On the other hand, a solidification plateau time about 0.4 s appears after recalescence, as shown in Fig. 1(a). It reveals that the experimental undercooling level is far below the hypercooling limit $\Delta T_{\mathrm{h}}$, at which the solidification plateau time $\Delta t_{\mathrm{p}}$ is zero. A method applied to derive the $\Delta T_{\mathrm{h}}$ is to establish the relation between solidification plateau time and undercooling. As illustrated in Fig. 1(d), $\Delta T_{\mathrm{h}}$ is determined to be 706 K, which is about 252 K larger than the maximum undercooling of 454 K. Moreover, $\Delta T_{\mathrm{h}}$ can be used to estimate the liquid heat capacity $C_{\mathrm{pL}}$ of pure Nb by $C_{\mathrm{pL}}=\Delta H_{\mathrm{m}} / \Delta T_{\mathrm{h}}$. If $C_{\mathrm{pL}}$ is assumed to not change with temperature and $\Delta H_{\mathrm{m}}$ is $2.72 \times 10^{3} \mathrm{~kJ} \mathrm{~mol}^{-1},{ }^{17}$ the averaged $C_{\mathrm{pL}}$ is 41.5 $\mathrm{J} \mathrm{mol}^{-1} \mathrm{~K}^{-1}$. It is very close to the value of $41.8 \mathrm{~J} \mathrm{~mol}^{-1} \mathrm{~K}^{-1}$ in Ref. [18].

After nucleation, dendrite rapidly propagates through the whole sample from nucleus to undercooled liquid during the recalescence, as demonstrated in Figs. 2(a)-(h). The dendritic growth velocities of liquid Nb at different undercoolings are obtained, and approximately display a power law relationship versus undercooling, as shown in Fig. 2(i):

$$
v_{t}=4.87 \times 10^{-4} \Delta T^{1.85} \mathrm{~m} \mathrm{~s}^{-1} \tag{4}
$$

At the smallest undercooling, the velocity is only about $0.3 \mathrm{~m} \mathrm{~s}^{-1}$, while the value increases to $41 \mathrm{~m} \mathrm{~s}^{-1}$ at the maximum

![](./images/813124643761160193_3.jpg)

Fig. 2 Dendrite growth in undercooled liquid pure Nb:
(a-h) high speed video graphs of recalescence process at
the rate of $10^{4}$ fps for Nb sample undercooled by 442 K;
(i) thermal dendritic growth velocity versus
undercooling.

undercooling of 454 K. For pure metals, only thermal dendrites exist during solidification, the kinetic process of which can be predicted by the LKT/BCT rapid dendrite growth model. $^{19}$ The dashed line in Fig. 2(i) is the calculated result, and it is consistent with the experimental result at small undercoolings, below 100 K. As the undercooling increases, the calculated values become larger than the experimental values, but they are still close to each other. As a result, the thermal dendritic growth in undercooled liquid Nb is well understood by LKT/BCT model.

### 3.2 Density and emissivity at liquid and solid states

In order to further comprehend the nucleation and dendritic growth mechanisms, the thermophysical properties of liquid Nb were measured. The densities of pure Nb in liquid and solid state are displayed in Fig. 3(a). The density in liquid state shows linear relationship with temperature:

$$
\rho_{L, \exp }=7.66-5.33 \times 10^{-4}\left(T-T_{m}\right) \quad \mathrm{g} \mathrm{cm}^{-3} \tag{5}
$$

At melting point, the density value is $7.66 \mathrm{~g} \mathrm{~cm}^{-3}$ and the fitted temperature coefficient is $-5.33 \times 10^{-4} \mathrm{~g} \mathrm{~cm}^{-3} \mathrm{~K}^{-1}$ from 2323 K to 2966 K with an undercooling of 427 K. The density in solid state also decreases as the temperature increases,

![](./images/813124643761160193_4.jpg)

Fig. 3 Thermophysical properties of liquid and solid Nb versus temperature: (a) measured and calculated densities; (b) hemispherical emissivity versus undercooling.

$$
\rho_{s, \text { exp }}=7.92-3.98 \times 10^{-4}\left(T-T_{m}\right) \quad \mathrm{g} \mathrm{cm}^{-3} \tag{6}
$$

The density value and temperature coefficient at the melting point is $7.92 \mathrm{~g} \mathrm{~cm}^{-3}$ and $-3.98 \times 10^{-4} \mathrm{~g} \mathrm{~cm}^{-3} \mathrm{~K}^{-1}$, respectively.

The liquid density measured by Ishikawa et al. $^{20}$ is referred in Fig. 3(a) as well. It can be seen that their data is slightly higher than ours. The density value at the melting point is $7.73 \mathrm{~g} \mathrm{~cm}^{-3}$, which is only $0.07 \mathrm{~g} \mathrm{~cm}^{-3}$ larger than the present result.

On the other hand, since the sample is cooled down only by thermal radiation, the hemispherical emissivity $\varepsilon_{\mathrm{L}}$ can be expressed as

$$
\varepsilon_{\mathrm{L}}=-\frac{C_{\mathrm{p}} \rho V R_{\mathrm{c}}}{A \sigma_{\mathrm{SB}}\left(T^{4}-T_{\mathrm{s}}^{4}\right)} \tag{7}
$$

where $A$ is the surface area of levitated sample, $\sigma_{\mathrm{SB}}$ is the Stefan-Boltzmann constant, and $T_{\mathrm{s}}$ is the environment temperature. Using the previous $C_{\mathrm{pL}}$ value of $41.5 \mathrm{~J} \mathrm{~mol}^{-1} \mathrm{~K}^{-1}$ in this work, $\varepsilon_{\mathrm{L}}$ is derived. As displayed in Fig. 3(b), the temperature dependence of $\varepsilon_{\mathrm{L}}$ is fitted linearly by

$$
\varepsilon_{\mathrm{L}}=0.294+9.31 \times 10^{-5}\left(T-T_{m}\right) \tag{8}
$$

$\varepsilon_{\mathrm{L}}$ increases gradually with temperature, and is about 0.294 at the melting point, which is very close to the value of 0.29 measured by Sakata et al. $^{21}$

### 3.3 Critical nucleus size and solid-liquid interface energy

To study the critical nucleus size and solid-liquid interface energy, the melting temperature and density are calculated to verify the applied potential function in MD simulation. The calculated melting point of pure Nb is 2689 K, which is only 3 K larger than the value calculated by Fellinger et al. $^{13}$, and 61 K lower than the experimental value of 2750 K. The computed density at liquid state also linearly depends on temperature, as shown in Fig. 3(a):

$$
\rho_{L, \mathrm{MD}}=7.62-3.16 \times 10^{-4}\left(T-T_{m}\right) \mathrm{g} \mathrm{cm}^{-3} \tag{9}
$$

At the melting point, the calculated density is $7.62 \mathrm{~g} \mathrm{~cm}^{-3}$, which is very close to the present experiment value of $7.66 \mathrm{~g}$ $\mathrm{cm}^{-3}$. Therefore, this potential function of $\mathrm{Nb}$ is reasonable for the application of calculating the physical properties of liquid $\mathrm{Nb}$.

For the critical nucleus size simulation, Fig. 4 shows the structural evolution at the undercooling of 689 K. When the number of atoms in the embedded nucleus is 201, the ordered nucleus will be dissolved, as displayed in Figs. 4(a1)-(a3). The PDFs at different time steps in Fig. 4(a4) also indicate that the simulated system is in a disordered liquid state. If the number of atoms in the embedded nucleus increases to 202, the system finally changes into ordered solid after relaxation for a period of time. Meanwhile, the curves of PDFs transform from liquid shape to solid shape, as illustrated in Fig. 4(b). From the above analysis, the number of atoms in the critical nucleus $n^{*}$ is determined to be 202 at $\Delta T=689 \mathrm{~K}$.

![](./images/813124643761160193_5.jpg)

Fig. 4 Atomic-scale structure evolution for critical nucleus size simulation at $\Delta T$=689 K: (a) $n$=201; (b) $n$=202.

As demonstrated in Fig. 5(a), the calculated $n^{*}$ decreases monotonously as a function of undercooling. The value of $n^{*}$ is 202 at the undercooling of 689 K ($T$=2000 K), while it adds to 2447 when the undercooling reduces to 239 K ($T$=2450 K). According to the classical nucleation theory (CNT) $^{6}$, $n^{*}$ is derived from

$$
n^{*}=\left(\frac{32 \pi}{3 V_{\mathrm{a}}}\right)\left(\frac{\sigma}{\Delta G_{\mathrm{v}}}\right)^{3} \tag{10}
$$

where $V_{\mathrm{a}}$ is the volume of a single atom, $\sigma$ is the solid-liquid interface energy, and $\Delta G_{\mathrm{V}}$ is the Gibbs free energy difference per unit volume between solid and liquid phases. In addition, there is a linear relationship between $n^{* 1 / 3}$ and $1 / \Delta T$, as displayed in Fig. 5(b). The solid-liquid interface energy $\sigma$ can be obtained from the slope $k$ of fitted line with the equation $^{22}$

$$
k=\sqrt[3]{\frac{32 \pi}{3 V_{\mathrm{a}}}}\left(\frac{T_{m} \sigma}{\Delta H_{\mathrm{m}}}\right) \tag{11}
$$

The value of $k$ is 3518. For pure Nb, $V_{\mathrm{a}}$ and $\Delta H_{\mathrm{m}}$ can also be derived from MD simulation, which is $19.2 \times 10^{-30} \mathrm{~m}^{-3}$ and $3.37 \times 10^{9} \mathrm{~J} \mathrm{~m}^{-3}$. Then $\sigma$ is calculated to be $0.367 \mathrm{~J} \mathrm{~m}^{-2}$ according to Eq. (11). This value is only 0.03 larger than that obtained by Kang et al. $^{23}$ It should be noted that as the limitation of this method, the determined $\sigma$ here is an average value of different crystal orientations and a broad range of undercoolings.

![](./images/813124643761160193_6.jpg)

Fig. 5 The calculated critical nucleus size of pure Nb:
(a) the number of atoms in critical nucleus versus
undercooling; (b) the linear fit of $n^{*1/3}$ versus $1/\Delta T$.

## 4. Conclusions

In summary, the mechanism of crystal nucleation and dendritic growth in undercooled liquid pure Nb are investigated by combining electrostatic levitation technique and molecular dynamics simulation. The maximum undercooling of liquid Nb is 454 K $(0.16T_{\text{L}})$ and almost all the undercooling values lie in the range of 414-454 K from 200 experimental cycles. With the classical nucleation theory, the activation energy of nucleation and pre-exponential factor in nucleation rate equation are determined to be $47.73k_{\text{B}}T$ and $1.02\times10^{30}\ \text{m}^{-3}\text{s}^{-1}$. The nucleation mechanism in liquid Nb is congruently identified as heterogeneous nucleation and further confirmed by high speed videographic observations. In addition, the hypercooling limit of 706 K is deduced by the linear relation of solidification time to undercooling. On the basis of measured and calculated thermophysical properties of liquid Nb, the applied potential function is verified to be appropriate in MD simulation. Meanwhile, the average liquid heat capacity and the relationship between emissivity and temperature of liquid Nb are obtained as well. From MD simulation, the number of atoms in

critical nucleus of homogeneous nucleation decrease rapidly as undercooling increases from 200 to 700 K. The average solid-liquid interface energy is derived to be $0.367\ \text{J m}^{-2}$. According to the recalescence process captured by high speed camera, the thermal dendritic growth velocity rises with increasing undercooling and reaches $41\ \text{m s}^{-1}$ at the maximum undercooling.

### Acknowledgement
The authors would like to thank Mr. Y. H. Wu and Mr. P. Lv for their helpful discussion. This work was financially supported by the National Natural Science Foundation of China (Grant Nos., 51327901, 51401169, and 51271150).

### Reference
$^1$G. W. Lee, Y. C. Cho, B. Lee, and K. F. Kelton, Phys. Rev. B **95**, 054202 (2017).

$^2$D. G. Quirinale, G. E. Rustan, A. Kreyssig, S. H. Lapidus, M. J. Kramer, and A. I. Goldman, J. Appl. Phys. **120**, 175104 (2016).

$^3$C. Tang and P. Harrowell, Nature Mater. **12**, 507-511 (2013).

$^4$X. Yang, K. Fujiwara, K. Maeda, J. Nozawa, H. Koizumi, and S. Uda, Appl. Phys. Lett. **98**, 012113 (2011).

$^5$J. Bokeloh, R. E. Rozas, J. Horbach, and G. Wilde, Phys. Rev. Lett. **107**, 145701 (2011).

$^6$K. Fisher and W. Kurz, Trans. Tech. Publications (1986).

$^7$G. W. Lee, S. Jeon, C. Park, and D. H. Kang, J. Chem. Thermodyn. **63**, 1-6 (2013).

$^8$L. Hu, W. L. Wang, S. J. Yang, L. H. Li, D. L. Geng, L. Wang, and B. Wei, J. Appl. Phys. **121**, 085901 (2017).

$^9$G. Wilde, J. Sebright, and J. Perepezko, Acta Mater. **54**, 4759-4769 (2006).

$^{10}$C. Morton, W. Hofmeister, R. Bayuzick, and M. Robinson, Mater. Sci. Eng. A **178**, 209-215 (1994).

$^{11}$H. P. Wang, S. J. Yang, L. Hu, and B. Wei, Chem. Phys. Lett. **653**, 112-116 (2016).

$^{12}$L. Hu, L. H. Li, S. J. Yang, and B. Wei, Chem. Phys. Lett. **621**, 91-95 (2015).

$^{13}$M. R. Fellinger, H. Park, and J. W. Wilkins, Phys. Rev. B **81**, 144119 (2010).

$^{14}$S. Plimpton, J. Comput. Phys. 117, 1-19 (1995).

$^{15}$V. P. Skripov, *Material Science, Crystal Growth and Materials* (North Holland, Amsterdam, 1977).

$^{16}$D. Turnbull, J. Chem. Phys. 20, 411-424 (1952).

$^{17}$W. F. Gale and T. C. Totemeier, *Smithells Metals Reference Book*, 8-2 (Butterworth-Heinemann, 2003).

$^{18}$T. Iida and R. I. Guthrie, *The Thermophysical Properties of Metallic Liquids*, 520 (Oxford University Press, USA, 2015) .

$^{19}$J. Lipton, W. Kurz, and R. Trivedi, Acta Metall. 35, 957-964 (1987).

$^{20}$T. Ishikawa and P. F. Paradis, J. Electron. Mater. 34, 1526-1532 (2005).

$^{21}$K. Sakata, Y. Watanabe, J. T. Okada, M. V. Kumar, P. F. Paradis, and T. Ishikawa, J. Chem. Thermodyn. 91, 116-120 (2015).

$^{22}$X. M. Bai and M. Li, J. Chem. Phys. 124, 124707 (2006).

$^{23}$D. H. Kang, S. Jeon, H. Yoo, T. Ishikawa, J. T. Okada, P. F. Paradis, and G. W. Lee, Cryst. Growth Des. 14, 1103-1109 (2014).

**Figure Captions:**

Fig. 1 Containerless processing of pure Nb in ESL experiments: (a) typical temperature-time curve; (b) the probability distribution of undercooling for pure Nb from 200 heating-cooling cycles; (c) the relationship between $F$ and undercooling; (d) measured solidification plateau time versus undercooling.

Fig. 2 Dendrite growth in undercooled liquid pure Nb: (a-h) high speed video graphs of recalescence process at the rate of $10^4$ fps for Nb sample undercooled by 442 K; (i) thermal dendritic growth velocity versus undercooling.

Fig. 3 Thermophysical properties of liquid and solid Nb versus temperature: (a) measured and calculated densities; (b) hemispherical emissivity versus undercooling.

Fig. 4 Atomic-scale structure evolution for critical nucleus simulation at $\Delta T$=689 K: (a) $n$=201; (b) $n$=202.

Fig. 5 The calculated critical nucleus size of pure Nb: (a) the number of atoms in critical nucleus versus undercooling; (b) the linear fit of $n^{*1/3}$ versus $1/\Delta T$.

![](./images/813124643761160193_7.jpg)

Graphical abstract

### Highlights

1.  The crystal nucleation mechanism of liquid niobium was studied under ESL;
2.  The dendritic growth velocity versus undercooling of Nb was measured;
3.  Critical nucleus size and solid-liquid interface energy was calculated by MD.
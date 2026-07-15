![](./images/812536991877955585_1.jpg)

![](./images/812536991877955585_2.jpg)

![](./images/812536991877955585_3.jpg)

Original Article

# First-principle computations of ferromagnetic $\text{HgCr}_2\text{Z}_4$ ($\text{Z} = \text{S}$, Se) spinels for spintronic and energy storage system applications

Asif Mahmood $^{a,**}$, Shahid M. Ramay $^{c,*}$, Waheed Al-Masry $^{a}$, Charles. W. Dunnill $^{b}$, Najib Y.A. Al-Garadi $^{a}$

$^{a}$ College of Engineering, Chemical Engineering Department, King Saud University Riyadh, Saudi Arabia
$^{b}$ Energy Safety Institute (ESRI), Swansea University Bay Campus, Swansea, SA1 8EN, UK
$^{c}$ Department of Physics and Astronomy, College of Science, King Saud University, Riyadh, 11451, Saudi Arabia

![](./images/812536991877955585_4.jpg)

## ARTICLE INFO

Article history:
Received 25 September 2020
Accepted 21 November 2020
Available online 27 November 2020

Keywords:
Density functional theory
Spin polarization
Ferromagnetism
Exchange splitting mechanism
Figure of merit (ZT)
Energy storage system applications

## ABSTRACT

We explored electronic spin-dependent physical aspects of ferromagnetic $\text{HgCr}_2\text{Z}_4$ (Z = S, Se) spinels using density functional theory (DFT) for spintronic and energy storage applications. In calculations of structural, electronic, magnetic, and transport aspects, we used Perdew-Burke-Ernzerhof generalized gradient approximation (PBEsol GGA) plus modified Becke-Johnson (mBJ) potential. To calculate structural parameters, we optimized both spinels in the ferromagnetic phase and our predicted data of structural parameters show good comparison with existing experimental data. Also, the calculated negative formation energy confirms the structural stability of the studied spinels. Analyzing ferromagnetic nature of studied spinels based on exchange splitting energy and magnetic parameters, we used mBJ potential to calculate band structure (BS) and density of states (DOS). By exploring DOS, we found the dominant role of electrons spin has been shown by negative indirect exchange energy $\Delta_{\text{x}}(pd)$ values and the fulfillment of the condition $\Delta_{\text{x}}(\text{d}) > \Delta\text{E}_{\text{cry}}$. In addition, exchange constants ($\text{N}_0\alpha$ and $\text{N}_0\beta$) and magnetic moments were also calculated to ensure their ferromagnetism in studied spinels. Further, the exploration for the influence of electrons spin on electronic transport aspects has been done by investigating electrical and thermal conductivities, Seebeck coefficient, and power factor by using classical Boltzmann transport theory.

© 2020 The Authors. Published by Elsevier B.V. This is an open access article under the CC BY-NC-ND license (http://creativecommons.org/licenses/by-nc-nd/4.0/).

* Corresponding author.
** Corresponding author.
E-mail addresses: ahayat@ksu.edu.sa (A. Mahmood), schaudhry@ksu.edu.sa, smramay@yahoo.com (S.M. Ramay).
https://doi.org/10.1016/j.jmrt.2020.11.063
2238-7854/© 2020 The Authors. Published by Elsevier B.V. This is an open access article under the CC BY-NC-ND license (http://creativecommons.org/licenses/by-nc-nd/4.0/).

### 1. Introduction

Control of spin of electron brought a revolution in the electronic industry and introduced a new class called spintronic. For spintronic devices, we need to inject the spin of electrons in semiconducting materials. This injection of spin opens a new way in device fabrication. This is because of its low lost engineering, high efficiency, and nonvolatile storage capacity [1-3]. For this purpose, we need magnetic semiconductor and half-metallic semiconductor materials. Since most of the magnetic semiconductors are insulators and thus have advantageous. The barrier height of these insulators smoothen the spin-polarized tunneling current and thus eliminates the need for half-metallic semiconductors as an electrode material. Owing to their outstanding physical properties like giant magneto-resistance and anomalous Hall effect [4-6], ferromagnetic chalcogenide spinels like $CdCr_2X_4$ ($X-S$, Se) and $HgCr_2X_4$ ($X = S$, Se) are emerging as a potential candidate for spintronic device applications.

To exploit the potential of different compositions of spinels for various applications, we need to have a better understanding of its response towards different fields. To date, there are very limited reports on the synthesis and characterizations of ferromagnetic chalcogenide spinel $HgCr_2S_4$ especially their thin films. In the recent past, some techniques like chemical vapor deposition, non-reactive sputtering, chemical bath deposition (CBD) are used to deposit the thin films of ferromagnetic chalcogenide spinels on different substrates [7]. Among these techniques, CBD is one of the easy ways to deposit thin films because it does not require any expensive equipment for example required in chemical vapor deposition. Using CBD, one can easily deposit the thin films of typical thickness ranging from 0.02 to $1\ \mu$m thickness. This could be achieved just by dipping the substrate in dilute baths containing metals ions and a source of selenium and sulfide ions [8].

![](./images/812536991877955585_5.jpg)

Fig. 1 - Crystal structure of spinels $HgCr_2Z_4$ ($Z = S$, Se). Pink, blue and green spheres represent Hg, Cr, and S/Se atoms, respectively. (For interpretation of the references to color in this figure legend, the reader is referred to the Web version of this article.)

The high ferromagnetic transition temperature (106 K) of $HgCr_2Se_4$ also shows its potential for spintronic device applications [9,10]. It crystallizes in normal cubic form where Cr ions are octahedrally surrounded by Se ions giving rise to the half-filled $t_{2g}$ states of $S = 3/2$. Mane et al. [11], explored optical characteristics of $CdCr_2S_4$ and $HgCr_2S_4$ thin films and they find both spinel films have n-type nature with an estimated bandgap energy Eg of 2.6 eV/2.7 eV, respectively. The crystal and magnetic interaction of $ZnCr_2S_4$ spinel is investigated by Hamedoun et al. [12] and their results show good comparison obtained between a polycrystal and a single crystal. Lattice dynamical calculations of $ACr_2X_4$ spinel-type chromium chalcides $CoCr_2S_4$, $ZnCr_2S_4$, $(CdCr_2S_4)$, $ZnCr_2Se_4$, $CdCr_2Se_4$, and $HgCr_2Se_4$ were executed by Zwinscher et al. [13], using short-range (SRM), rigid ion (RIM) and polarizable-ion models (PIM) with structure data and calculate force constants due to the tetrahedral A-X bonds are in the order $CoCr_2S_4 < ACr_2S_4 < ACr_2Se_4$ ($A = Zn$, Cd, Hg). Some exceptional properties like high magneto-resistance, high hall coefficients with the red shift in optical absorption edge have further made this a ferromagnetic spinel and play a vital role for spintronic device applications [13-15]. Other theoretical literature on $HgCr_2Se_4$ represented ferromagnetism by employing the local density approximation (LDA + U) to study the exchange coupling constants [16]. Theoretically, Xu et al. [17], explored $HgCr_2Se_4$ spinel to predict the quantized anomalous Hall Effect, which was anticipated as Chern semimetal.

According to our best information, no theoretical investigation on ferromagnetism and transport aspects has been conducted on $HgCr_2Z_4$ ($Z = S$, Se) so far. As far as the theoretical investigation is concerned, it is very limitedly available on $HgCr_2Se_4$ in the reported literature. Therefore, in the current study, we conducted a detailed theoretical investigation on the electronic, magnetic, and transport aspects of $HgCr_2Z_4$ ($Z = S$, Se). For this, DFT based technique revised by modified Becke and Johnson (as implemented in Wein2K code) has been applied in our study [18]. This technique in turn produced the exact electronic structures of the spinels with accurate bandgaps. For the judgment of the consistency in transport aspects, the computed electronic structures were integrated with BoltzTraP code [19]. The revealed structural stability in the ferromagnetic phase and computed transport aspects of studied spinels demonstrated them useful in the applications related to spintronic and energy storage devices.

### 2. Method of calculation

In this paper, we employed a spin-polarized DFT computational method to investigate the electronic, magnetic, and transport aspects of $HgCr_2Z_4$ ($Z = S$, Se), where similar systems are already theoretically reported [20-23]. The method used for all studied calculations is full-potential linearized augmented plane wave plus local orbital (FP-LAPW + lo), which is implemented in Wien2k software [24]. PBEsol generalized gradient approximation of Perdew et al. [18], was adopted for the computation of the ground-state energies and

![](./images/812536991877955585_6.jpg)

Fig. 2 – The energy versus volume plots of (a) $HgCr_2S_4$ and (b) $HgCr_2Se_4$ spinels in FM and NM phases.

structural parameters, in particular with exchange-correlation functionals. The structures were continued to be optimized until all the forces on each atom fall to zero. Further, the Tran–Blaha-modified Becke–Johnson (TB-mBJ) [25] exchange potential has also been brought into use for the investigation of the electrons spin-dependent ferromagnetic and transport aspects. Because, literatures show that TB-mBJ potential is useful as exchange-correlation functionals in predicting the electronic band structure [26,27]. The muffin-tin radius ($R_{MT}$) and the maximum value of the wave vector ($K_{max}$) are multiplied as $R_{MT} \times K_{max} = 8$ in reciprocal lattice for the convergence of the energy. So for better convergence, we take $R_{MT} \times K_{max} = 8$ for all calculations.

In addition, we set muffin-tin radii as 2.37 a.u. for Cu, 2.5 a.u. for Cr, 1.85 a.u. for S, and 2.1 a.u for Se. The default value (-6Ry) of cut off energy was employed. Furthermore, the angular momentum vector ($l_{max}$) and Gaussian factor ($G_{max}$) have been kept at 10 Ry and 18 Ry respectively. The primary and essential point of methodology is the selections of k-points, which are chosen by selecting the number of k-points pairs for the best conversion of energy. For best energy convergence, 1000 k-points are selected because, after these k points, energy optimizations become constant. For transport aspects, the semi-classical Boltzmann transport theory has been employed to compute the $HgCr_2Z_4$ (Z = S, Se) [28,29]. Moreover, for the transport aspects, all the calculations related to the electronic structure of the spinels have been used within the BotlzTraP code [19]. For all the BoltzTrap calculations, a larger value of k points is used in this study, and electrical ($\sigma$) and thermal ($\kappa$) conductivities, Seebeck coefficient (S), and figure of merit (ZT) have been investigated against the temperature range 200 K–600 K.

### 3. Results and discussion

#### 3.1. Structural and electronic properties

The cubic spinels $HgCr_2Z_4$ (Z = S, Se) that possess space group Fd-3m#227 (see Fig. 1) and are of ordered crystalline structures have been converged with reference of energy for the minimization of their ground state energies in non-magnetic (NM) and ferromagnetic (FM) states. The plots of the energy (Ry) versus volume (a.u.) in terms of NM and FM states have been shown in Fig. 2 (a, b). It is clear from the comparative analysis that FM state is responsible for higher energy release than that of NM State. This confirms the more stability of FM than that of NM states. From Refs. [30,31], we can see that the studied compounds are experimentally found to be ferromagnetic. In order to justify that our calculations agree with the experimental results, we have only considered nonmagnetic and ferromagnetic configurations of the spins. As evident from our calculations, DFT also predicts $HgCr_2Z_4$ to be stable ferromagnetic compounds. In addition, the enthalpy of formation ($\Delta H_f$) is computed to find out the thermodynamic stability of the said cubic spinels. $\Delta H_f$ can be found by using the following expression [32]:

$$
\Delta H_{f}=E_{Total}\left(Hg_{l}Cr_{m}Z_{n}\right)-lE_{Hg}-mE_{Cr}-nE_{Z} \tag{1}
$$

here, $E_{Total}(Hg_lCr_mZ_n)$ is the total calculated ground state energy of studied spinels, while $E_{Hg}$ $E_{Cr}$ $E_Z$, represents their individual atoms energies. The letters l, m, and n represent the number of atoms of Hg, Cr, and S/Se per their unit cell volume, correspondingly. Referred to Table 1, our calculated values of $\Delta H_f$ represent negative values. It means that studied spinels with negative values thermodynamically stable. The decrease in the stability happens when S is replaced with Se.

To find the ground states lattice parameters such as the lattice constant ($a_o$) and bulk modulus $B_0$, we done volume optimization in FM phase. From the minimum volume of the unit cell, we calculate $a_o$ and $B_0$ using Murnaghan's equation of state [33] with PBEsol-GGA. The results of both parameters are tabulated and noted that the calculated value of $a_o$ for both spinels are closely related to experimental values [34]. The

<table>
<caption>Table 1 – The calculated lattice constant $a_0$ (Å), bulk modulus $B_0$ (GPa) ground state energy difference ($\Delta E = E_{NM} - E_{FM}$), enthalpy of formation $\Delta H$ (eV) for $HgCr_2Z_4$ ($Z = S, Se$).</caption>
<thead>
<tr>
<th>Spinels</th>
<th>$a_0$ (Å)</th>
<th>$B_0$ (GPa)</th>
<th>$\Delta E$ (eV)</th>
<th>$\Delta H$ (eV)</th>
</tr>
</thead>
<tbody>
<tr>
<td>$HgCr_2S_4$</td>
<td>10.37</td>
<td>90.15</td>
<td>5.21</td>
<td>–0.98</td>
</tr>
<tr>
<td>Exp.</td>
<td>10.24ª</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>$HgCr_2Se_4$</td>
<td>10.89</td>
<td>72.83</td>
<td>6.64</td>
<td>–0.84</td>
</tr>
<tr>
<td>Exp.</td>
<td>10.75ª</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="5">ª Ref [34].</td>
</tr>
</tbody>
</table>

![](./images/812536991877955585_7.jpg)

Fig. 6 – The computed (a) electrical conductivity $(\sigma/\tau)$, (b) Seebeck coefficients, (c) electronic thermal conductivity $(\mathfrak{k}_\mathfrak{e}/\tau)$ and (d) power factors $(S^2\sigma/\tau)$ plot versus temperature of $HgCr_2S_4$ and $HgCr_2Se_4$ spinels.

flow in more heat. However, $HgCr_2Se_4$ has the least $\kappa/\tau$ at 600 K, whereas at the same temperature range, $HgCr_2S_4$ achieves the highest level of it (see Fig. 6c). There must be a very low ration of $\kappa/\tau$ to $\sigma/\tau$ (Weidman-Franz law (LT = $\kappa/\sigma$)) against temperature to be the best thermoelectric materials. Its value is of the order of $10^{-6}$ indicating the compounds useful in thermoelectric applications.

The calculation of the temperature gradient of potential is done as the See back coefficient (S) between two dissimilar metals. Fig.6b shows the computed value of S of the materials. It has a small value for $HgCr_2Se_4$ and a large one for $HgCr_2S_4$ at 200 K. Further, the Seebeck coefficient has convergence at 250 K whereas it has divergence up to 600 K for both spinels under experiment. $HgCr_2S_4$ secured maximum value whereas $HgCr_2Se_4$ attained minimum value from all the materials. In addition, the p-type behavior of the studied spinels becomes clear from the positive value of See back coefficient. The thermoelectric efficiency is measured by the power factor $(S^2\sigma/\tau)$. It does not include thermal conductivity because of which its resulted values are overestimated, but at the same time, the trends have accuracy. There was an increase in the value of power factor up to 600 K for both spinels. For both spinels $HgCr_2Se_4$ and $HgCr_2S_4$, its value becomes constant on the same temperature range. On the other hand, its value continued to increase linearly up to 600 K for $HgCr_2S_4$, (see Fig. 6d). The small Seebeck coefficient causes an increase in the power factor at higher temperatures [46,47]. Lastly, we also investigate the figure of merit (ZT) using the known values of $\sigma$, S, and $k_e$ and found linear variation with temperature range (200 K–600 K). From Fig. 7, a ZT value with temperature varies directly and recorded maximum values at 600 K for both spinels $HgCr_2S_4$ and $HgCr_2Se_4$.

![](./images/812536991877955585_8.jpg)

Fig. 7 – The computed figure of merit (ZT) plot versus temperature of $HgCr_2S_4$ and $HgCr_2Se_4$ spinels.

## 4. Conclusions

In the current study, BoltzTraP code and Wien2k code have been brought into use for the electronic transport and ferromagnetism aspects of $HgCr_2Z_4$ (Z = S, Se). More energy was released in FM than that of NM State during the optimizing process where the ferromagnetism has further been assured by negative values of $\Delta H_f$. The ground state parameters such as $B_0$ decrease whereas there is an increase in $a_0$ from $HgCr_2S_4$

to $HgCr_2Se_4$ in FM phase and noted that our calculated values of $a_0$ good comparable to experimental value. The DOS and the electronic BS of the studied spines prove them to be ferro- magnetic semiconductors. From DOS, we calculate the ex- change interactions and found strong hybridization that ensures the ferromagnetism tempted by electrons spin. Our predicted results of exchange parameters indicate that comparatively greater values of $\Delta(d)$ are favorable for the ferromagnetism than $(\Delta_{CF})$. In addition, the exchange con- stant $(N_{0} \delta)$ and the negative value of-exchange energy are the cause of reduction in energy in the down spin channel. Another evidence for p-d hybridization/exchange interaction is the decrease of $\mu_{B}$ at Cr site and increase of $\mu_{B}$ on other sites. The $\kappa / \sigma$ ratio and power factor prove that more thermoelectric efficiency is possessed by $HgCr_2S_4$ than $HgCr_2Se_4$.

## Declaration of Competing Interest

There is no conflict of interest.

## Acknowledgment

The authors extend their appreciation to the Deputyship of Research & Innovation, "Ministry of Education" in Saudi Ara- bia for funding this research work through project No. IFK- SURG-311.

## REFERENCES

[1] Biswas P, Mamatha S, Naskar S, Rao YS, Johnson R, Padmanabham G. J Alloys Compd 2019;770:419-23.
[2] Canepa P, Bo SH, Gautam GS, Key B, Richards WD, Shi T, et al. Nat Commun 2017;24:1-8.
[3] Pang C, Srivastava A, Lockart MM, Mewes T, Bowman MK, Bao N, et al. ACS Appl Electron Mater 2019;1:424-32.
[4] Solin NI, Chebotaev NM. Phys Solid State 1997;39:754.
[5] Solin NI, Ustinov VV, Naumov SV. Phys Solid State 2008;50:901.
[6] Mane RS, Lokhande CD. Mater Chem Phys 2000;65:1.
[7] Deshmukh LP, Holikatti SG, Rane BP, Belle MI, Hankare PP. Bull Electrochem 1993;9:237.
[8] Mane RS, Todkar VV, Lokhande CD, Kalea SS, Han Sung- Hwan. Vacuum 2006;80:962-6.
[9] Lehmann W, Emmenegger FP. Solid State Commun 1969;79:65.
[10] Solin NI, Ustinov VV, Naumov SV. Phys SolidState 2008;50:901.
[11] Mane RS, Sankapal BR, Gadave KM, Lokhande CD. Mater Res Bull 1999;34:2035.
[12] Hamedoun M, Hourmatallah A, Sayouri S, Chatwiti A. J Phys Condens Matter 1995;7:5359.
[13] Zwinscher J, Lutz HD. J Solid State Chem 1995;118:43-52.
[14] Solin NI, Chebotaev NM. Phys Solid State 2008;39:754.

[15] Arai T, Wakaki M, Onari S, Kubdo K, Satoh T, Tsushima T. J Phys Soc Jpn 1973;34:68.
[16] Yaresko AN. Phys Rev B 2008;77:115106.
[17] Xu G, Weng HM, Wang ZJ, Dai X, Fang Z. Rev Lett2011;107:186806.
[18] Tran F, Blaha P. Phys Rev Lett 2009;102:22640.
[19] Madsen GK, Singh DJ. Comput Phys Commun 2006;175:67.
[20] Yang Juntao, Zhou Yong, Dedkov Yuriy, Elena Voloshina. Adv Theory Simul 2020;3:2000228.
[21] Yanga Juntao, Zhou Yong, Guo Qilin, Dedkov Yuriy, Elena Voloshina. RSC Adv 2020;10:851.
[22] Li Xingxing, Wu Xiaojun, Yang Jinlong. J Am Chem Soc2014;136(31):11065-9.
[23] Zhang X, Zhao X, WuYu D, Zhen Zhou J. Adv Sci2016;3:1600062.
[24] Blaha P, Schwarz K, H Madsen GK, Kvasnicka D, Luitz J. WIEN2k; an augmented planewave plus local orbital program for calculating crystal properties. Austria: Vienna University ofTechnology; 2001.
[25] Perdew P, Ruzsinszky A, Csonka GI, Vydrov OA, Scuseria GE, Constantin LA, et al. Phys Rev Lett 2008;100:136406.
[26] Noor NA, Ali S, Murtaza G, Sajjad M, Alay-e-Abbas SM, Shaukat A. Comput Mater Sci 2014;93:151-9.
[27] Noor NA, Rashid M, Alay-e-Abbas SM, Raza M, Mahmood A, Ramay SM. Mater Sci Semicond Process 2016;49:40-7.
[28] Nag BR. Electron transport in compound semiconductors, vol. 11. Springer Science & Business Media; 2012.
[29] Scheidemantel T, Ambrosch-Draxl C, Thonhauser T, Badding J, Sofo J. Phys Rev B 2003;68:125210.
[30] Lehmann HW, Emmenegger FP. Solid State Commun1969;7:965-8.
[31] Hastings JM, Corliss LM. J Phys Chem Solid 1968;29:9-14.
[32] Mahmood Q, Noor NA, Jadan M, Addasi Jihad S, Mahmood Asif, Ramay ShahidM. J Solid State Chem2020;285:121261.
[33] Murnaghan FD. Proc Natl Acad Sci USA 1944;30:244-7.
[34] Konopka D, Kozlowska I, Chelkowski A. Phys Lett A1973;44:289-90.
[35] Walsh A, Wai SH, Yan Y, Al-Jassim MM, Turner JA. Phys Rev B 2007;76:165119.
[36] Choi HC, Shim JH, Min BI. Phys Rev B 2006;74:172103.
[37] Kumar A, Fennie CJ, Rabe KM. Phys Rev B 2012;86:184429.
[38] Hassan M, Arshad I, Mahmood Q, Semicond. Sci Technol2017;32:115002.
[39] Noor NA, Ali S, Tahir W, Shaukat A, Reshak AH. J Alloys Compnd 2011;509(32):8137-43.
[40] Mahmood Q, Rashid,Qurat-ul-Ain M, Noor NA, GulBaharArshiq M, Ramay ShahidM, Mahmood A. J Mol Graph Model 2019;88:168-73.
[41] Kant C, Deisenhofer J, Tsurkan V, Loidl A. J Phys: Conf Seri2010;200:032032.
[42] Ali S, Rashid M, Hassan M, Noor NA, Mahmood Q, Laref A, et al. Phys B Condens Matter 2018;537:329-35.
[43] Majid Farzana, Hassan MTauqeerm, Arshad I, Mahmood Q. Semicond Sci Technol 2017;32:115002.
[44] Nasir EmanAlgrafy, Sajjad Muhammad, Noor NA, Mahmood Asif, Ramay ShahidM. J Mater Res Technol2020;9:6135-42.
[45] Noor NA, Anwar U, Mahmood A. Chem Phys Lett2020;739:137031.
[46] Bilal, Saifullah M, Shafig M, Khan B, Aliabad HAR, Asadabadi SJ, Ahmed R, et al. Phys Lett A 2015;379:206-10.
[47] Liu C, Morelli DT. J Electron Mater 2011;40(5).
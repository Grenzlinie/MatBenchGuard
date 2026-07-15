# Role of oxygen vacancies in the resistive switching of $SrZrO_3$ for resistance random access memory

Zhonglu Guo $^{a}$, Baisheng Sa $^{a}$, Jian Zhou $^{a}$, Zhimei Sun $^{a,b,*}$

$^{a}$ Department of Materials Science and Engineering, College of Materials, Xiamen University, 361005 Xiamen, China
$^{b}$ Fujian Provincial Key Laboratory of Theoretical and Computational Chemistry, Xiamen University, 361005 Xiamen, China

---

## ARTICLE INFO

Article history:
Received 5 March 2013
Received in revised form 6 May 2013
Accepted 6 May 2013
Available online 14 May 2013

Keywords:
Resistive switching
RRAM
$SrZrO_3$
Oxygen vacancies

## ABSTRACT

$SrZrO_3$ (SZO) is an important recording material for resistance random access memory (RRAM), which is attracted increasing interest for future nonvolatile memory applications. However, the resistive switching (RS) mechanism is not yet fully understood. In this work, by first principles calculations based on the density functional theory, we have investigated the structure and properties of bulk SZO with ordered and disordered oxygen vacancies ($V_O$). Our results show that the formation of oxygen vacancy row ($V_O$-row) results in the defect assisted conduction channel, which is the "ON"-state of SZO RRAM, while the disruption of the ordered $V_O$-row breaks this conduction channel and hence this structure is the "OFF"-state of SZO RRAM. The formation and disruption of $V_O$-row is triggered by the applied electric field through electron injection and removal.

© 2013 Elsevier B.V. All rights reserved.

---

## 1. Introduction

Resistance random access memory (RRAM) is based on the current pulse induced resistive switching (RS) phenomenon to record the information. Due to the simple structure, low power consumption, long retention nondestructive readout, good complementary metal oxide semiconductor (CMOS) compatibility and high density integration, RRAM is considered as a promising candidate for the next-generation nonvolatile memory [1,2]. The basic structure of a RRAM device is the combination of metal-insulator-metal (M-I-M). The insulators such as perovskites [3-6], binary metal oxides [7-9], solid-state electrolytes [10] and organic molecular materials [11] have been investigated as RS materials for RRAM devices. However, the low endurance and device yield limit the practical applications of RRAM. A deeper understanding of the resistive switching mechanism from the atomic scale point of view is helpful to overcome these problems. Several models of the mechanism have been suggested, including the modulation of bulk and interface resistivity achieved by trapping and detrapping of defects or carriers [12,13], the modulation of Schottky barrier [14], or the formation of conduction channel through the rearrangement of oxygen vacancies [15-17]. Yang et al. [17] demonstrated that the switching involved changes of the electronic barrier at the Pt/$TiO_2$ interface due to the drift of positively charged oxygen vacancies under an applied electric field. Furthermore, the same group has also observed that applying an electrical bias can generate an ordered $Ti_4O_7$ Magnéli phase and control oxygen vacancies moving into and out of this sub-oxide phase, thus modulating a transport barrier and resulting in changes in the conductivity [18]. Lin et al. [19] have shown that the double-layer $SrZrO_3$ (SZO) memory devices fabricated by an oxygen flow control process exhibited excellent RS performance, which is in consistent with Yang's experimental results [20]. As reported by Wu et al. [12], the switching endurance of SZO thin films could be enhanced significantly by introducing oxygen vacancies by making Zr-deficient films. More recently, Li et al. [5] found that more oxygen vacancies could be generated in the presence of Cu modulation layer, which improves the switching properties of the Pt/Cu/Nb:SZO/Ag/Pt structure. Nevertheless, the role of oxygen vacancies is still an open issue and needs further exploration.

However, it is a great challenge to direct observe the oxygen vacancies in experiments due to their insensitivity to conventional measurement techniques. Fortunately, in this respect, first principles calculation can provide very useful information. As SZO shows great promising RRAM applications among the investigated RS materials, in this work, we use SZO as an example to investigate the role of oxygen vacancies and the RS mechanism by means of first principles calculations.

## 2. Computational methods and structure construction

Our calculations are based on density functional theory (DFT) in conjunction with projector augmented wave (PAW) potentials, as

---

* Corresponding author at: Department of Materials Science and Engineering, College of Materials, Xiamen University, 361005 Xiamen, China. Tel./fax: +86 592 2186664.
E-mail addresses: zmsun@xmu.edu.cn, zhmsun2@yahoo.com (Z. Sun).

0925-8388/$ - see front matter © 2013 Elsevier B.V. All rights reserved.
http://dx.doi.org/10.1016/j.jallcom.2013.05.030

implemented in the Vienna ab initio simulation package [21]. For the exchange-correlation functional the generalized gradient approximations (GGA) [22] of Perdew-Burke-Ernzerhof (PBE) [23] were used. The strontium $4s^{2}4p^{6}5s^{2}$, zirconium $4d^{2}5s^{2}$ and oxygen $2s^{2}2p^{4}$ electrons are treated as valence electrons. The tetrahedron method with Blöchl corrections was used for cohesive energy calculations [24]. Convergence with respect to self-consistent iterations was achieved when the total energy difference between cycles was less than $10^{-5}$ eV. The k-points of $2 \times 2 \times 2$ and $4 \times 4 \times 4$ automatically generated with Monkhorst-Pack scheme [25] were used for structure optimization and static self-consistent calculations, respectively. The energy cut-off was 500 eV. The electron localization function (ELF) [26] was analyzed by the VESTA [27] code. SZO has an orthorhombic structure below 970 K [28] that is typically present in the RRAM devices [4,5,19]. In this work, a $2 \times 2 \times 1$ supercell containing 80 atoms was used, which is built from the conventional 20-atom orthorhombic unit cell. Oxygen vacancies (V$_O$s) were created by removing oxygen atoms from the supercell. The formation energy of charged defects $E_{form}(nV_O^q)$ was calculated by introducing a uniform background charges to keep the supercell in neutral state.

## 3. Results and discussion
Table 1 lists the calculated results for ideal SZO, where the available experimental results [29] have also been included for comparison. It is seen that our calculated lattice constants by PAW-GGA calculation agree well with the experimental ones with in less than 1.5% deviations. Therefore, the GGA approximation is able to provide reliable results for the equilibrium lattice constants of the present system.

Fig. 1 shows the band structure and density of states (DOS) for defect-free SZO, which is in good agreement with previous calculations [30,31]. The present calculated band gap for SZO is 3.8 eV as seen in Fig. 1a, which is lower than the experimental value of 5.6 eV by optical conductivity analysis of the polycrystalline sample at room temperature [32]. The underestimation of band gap energy is a typical problem of DFT calculations in the GGA approximation. Nevertheless, the present calculations properly reproduce the good insulating character of ideal SZO. As seen in Fig. 1b, the upper valence bands (VB) consist of O 2p states with some contributions from Zr 4d states, while the lower conduction bands (CB) are mainly the Zr 4d states. In order to investigate the possibility to form $n$ oxygen vacancies (V$_O$s), we have calculated the formation energy ($E_{form}(nV_O^q)$) by the following equation [33]:

$$
E_{form}(nV_O^q)=E(nV_O^q)-E(\text{SrZrO}_3)+\frac{n}{2}E(\text{O}_2)+nqE_F \tag{1}
$$

where $E(nV_O^q)$ and $E(\text{SrZrO}_3)$ are the total energies for the optimized supercell containing $n$V$_O$ with the charge state $q$ and the perfect crystal supercell, respectively. $E(\text{O}_2)$ is the total energy for the ground state of an optimized oxygen molecule in the gas state and $\frac{n}{2}E(\text{O}_2)$ is the chemical potential of $n$ oxygen atoms. $E_F$ is the Fermi energy referenced to the valence-band maximum (VBM) of the defect-free supercell. The calculated formation energies for one V$_O$ in SZO (structure illustrated in Fig. 2a) are shown in Fig. 2f. It is clear that one $V_O^{2+}$ is stable in the energy range of $0 < E_F < 4.6$ eV and one $V_O^0$ is stable at $4.6 < E_F < 5.6$ eV. It has been experimentally reported [4,5,19] that the conducting channel consists of a large density of V$_O$s, which cannot be explained by the isolated single V$_O$. Therefore, we have calculated and analyzed the cases of SZO with two oxygen vacancies within the unit supercell (divacancy-model) in order to address the possible vacancy-vacancy interaction [34]. Generally there are three configurations for the arrangements of the two vacancies, i.e., vacancies separate far away and there is no interaction between them (divacancy-I, Fig. 2b), vacancies are connected by one Zr atom having the V$_O$-Zr-V$_O$ form (divacancy-II, Fig. 2c), the two vacancies are directly connected (divacancy-III, Fig. 2d). As seen from the formation energies for the three configurations shown in Fig. 2g-i, $E_{form}(2V_O^{2+})$ at $E_F=0$ eV of model divacancy-II is about 2 eV higher than that of divacancy-I and divacancy-III. The results show that as remotely separated oxygen vacancies migrate closer to form oxygen vacancy clusters, an extra energy supplied by an external electric field is necessary to overcome the energy barrier of around 2 eV. Hence the V$_O$-Zr-V$_O$ configuration could be the barrier for the drift of V$_O$s to form V$_O$-clusters. The above results may explain the observed relatively high turn-on voltage in SZO RRAM devices [4,5,19]. Furthermore, for higher defect densities, we created another two V$_O$s besides the divacancy in Fig. 2d, forming an oxygen-vacancy-row (V$_O$-row model) as illustrated in Fig. 2e. In this V$_O$-row model, the charge-state transitions (2+/1+) and (1+/0) occur at $E_F=4.60$ and 4.92 eV, respectively. It is obvious that ordered V$_O$s in SZO have the intrinsic state $V_O^{2+}$ in the Fermi energy range of $0 < E_F < 4.60$ eV, and take the one-electron-captured state ($V_O^{1+}$) at $4.60 < E_F < 4.92$ eV and the two-electron-captured state ($V_O^0$) at above 4.92 eV.

Further analysis on the electronic structure and electron localization functions (ELFs) [26] unravels the mechanism of the resistive switching in SZO. As seen in Fig. 3a, the presence of V$_O$-row introduces intermediate states within the band gap of bulk SZO. The defect states are dispersed and merged with the CB, resulting in a metallic character with the Fermi energy falling into a continuum of energy states. The defect states are mainly attributed to 4d orbitals from Zr atoms with weak hybridization with O 2p orbitals, as seen in Fig. 3b. The presence of V$_O$-row results in the formation of metallic Zr ions, which increases the conductivity of the bulk SZO. Fig. 3c shows the ELF contour plots projected on the (001) planes of the V$_O$-row model in SZO. It is clearly seen that high density of electrons are trapped at the positions of adjacent V$_O$s, forming a conduction channel. Electrons can be transported through the V$_O$-row under an applied external electrical field. This is a rather direct evidence for the formation of conduction channel around the vicinity of the oxygen vacancy row. It changes the electrical conductivity of the bulk SZO. Therefore, the Vo-row can form the

<table>
<caption>Table 1
The calculated structural results for orthorhombic SrZrO₃. The experimental results are also included for comparison.</caption>
<thead>
<tr>
<th></th>
<th>A (Å)</th>
<th>B (Å)</th>
<th>C (Å)</th>
<th>V (Å³)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Ideal-SZO</td>
<td>5.840</td>
<td>5.902</td>
<td>8.289</td>
<td>285.720</td>
</tr>
<tr>
<td>Experimental [29]</td>
<td>5.796</td>
<td>5.817</td>
<td>8.205</td>
<td>–</td>
</tr>
</tbody>
</table>

![](./images/813223664836149248_1.jpg)

Fig. 1. The calculated (a) band structures and (b) density of states (DOS) of SrZrO₃ for defect-free cell.

![](./images/813223664836149248_2.jpg)

Fig. 2. The schematic view of $SrZrO_3$ (Zr: big black balls; O: medium red balls; Sr: small green balls) of the (a) isolated-$V_O$ model, (b) divacancy-I model, (c) divacancy-II model, (d) divacancy-III model and (e) $V_O$-row model. Their corresponding defect formation energy diagrams are shown in (f-j), respectively. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)

![](./images/813223664836149248_3.jpg)

Fig. 3. The calculated (a) band structures, (b) density of states (DOS) and (c) ELF contour plots projected on the (001) plane of $SrZrO_3$ for the $V_O$-row models.

conduction channel for electron transportation and this state may represent the "ON"-state (low-resistance-state) of SZO RRAM devices. Similar calculations have been performed to investigate the effect of oxygen-vacancy ordering on the formation of a conductive filament in $TiO_2$ [35]. Zheng et al. have demonstrated that $HfO_2$ was more prone to the formation of oxygen vacancies than metal vacancies in low oxygen chemical potential [36]. More recently, tetragonal semimetallic $Hf_2O_3$ in the O-deficient $HfO_x$ form has been predicted as a possible explanation for the conductive state of hafnium-based RRAM [37].

Under applied electric field, the $V_O$-row structure may be disrupted by some oxygen vacancies moving into the nearest oxygen positions, or some oxygen ions moving into the vacancy positions of ordered row. The simplest situation is that one $V_O$ switches position with its nearest oxygen atom as illustrated in Fig. 4a (disrupted-row-I model). When two $V_O$s in the $V_O$-row migrate into

![](./images/813223664836149248_4.jpg)

Fig. 4. The schematic view of $SrZrO_3$ (Zr: big black balls; O: medium red balls; Sr: small green balls) for the (a) disrupted-row-I model, (b) disrupted-row-II model and (c) the energy difference ($\Delta E$) between disrupted-row models and $V_O$-row model as a function of the charge state $q$ for the $V_O$s. The solid lines were drawn to attract the eyes, while the transverse red line at 0 eV is the energy of the $V_O$-row model. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)

![](./images/813223664836149248_5.jpg)

Fig. 5. The calculated band structures of SrZrO₃ for the (a) disrupted-row-I model and (b) disrupted-row-II model. The ELF contour plots projected on the (001) planes for the disrupted-row-I and disrupted-row-II are shown in (c and d), respectively.

the nearest oxygen positions, there are two different configurations. As the energy difference between these two configurations is very small, we here only present one typical configuration (referred to as disrupted-row-II model) as illustrated in Fig. 4b. The energy differences ($\Delta E$) between disrupted-row and $V_O$-row models are shown in Fig. 4c. As seen in Fig. 4c, it is energetically favorable for $V_O$s to diffuse away from the $V_O$-row if the charge state of the vacancy is neutral. For the charge state of $V_O$s being 1+, $V_O$s are energetically favorable to migrate back to the vacancy row. Therefore, the formation and rupture of $V_O$-row can be triggered by the applied electric field through electron injection and removal.

The conductivity of the two models of Fig. 4a and b is investigated by calculating their band structures shown in Fig. 5a and b, respectively. For the disrupted-$V_O$ models, the defect states are flat and electrons are localized. As oxygen atoms move into the ordered row of vacancies under applied electric field, small band gaps around the Fermi level are observed in their band structures. For the electron localization function shown in Fig. 5c and d, it is clearly seen that the connection between the $V_O$s are disrupted by the oxygen atoms, which damaged the electron transportations via the $V_O$-row. Therefore, the conduction of the disrupted-$V_O$ models is significantly reduced compared to the $V_O$-row model. Therefore, disrupted-$V_O$ models may correspond to the "OFF"-state (high-resistance-state) observed experimentally in SZO RRAM.

## 4. Conclusions

By means of DFT calculations, we investigated the structural and property changes in SZO with and without oxygen vacancies. By analyzing the formation energies, electronic band structures and ELF, it is found that the formation of oxygen vacancy row in SZO results in a conductive channel which leads to the dramatic change in electrical conductivities. We have also calculated the models with different charge states. Our results show that $V_O^{1+}$s tend to be ordered, while $V_O^0$s have a disordered tendency. As the ordering of $V_O$s decreases, the conductivity of the disrupted-row models decreases which corresponds to the "OFF"-state in RRAM devices. The applied electric field can change the charge state of $V_O$ through electron injection and removal, so as to control the formation and rupture of $V_O$-row. The present results contribute to the understanding of resistive switching mechanism and hence benefit to optimize RRAM characteristics.

## Acknowledgements

This work is supported by National Science Foundation of Distinguished Young Scientists of China (51225205), National Natural Science Foundation of China (60976005 and 61274005), and the Outstanding Young Scientists Foundation of Fujian Province of China (2010J06018).

## References

[1] R. Waser, R. Dittman, G. Staikov, K. Szot, Adv. Mater. 21 (2009) 2632.
[2] J.J. Yang, D.B. Strukov, D.R. Stewart, Nat. Nanotechnol. 8 (2013) 13.
[3] J.G. Wu, X.P. Wang, B.Y. Zhang, J.G. Zhu, D.Q. Xiao, J. Alloys Comp. 569 (2013) 126.
[4] M.H. Lin, M.C. Wu, C.H. Lin, T.Y. Tseng, J. Appl. Phys. 107 (2010) 124117.
[5] M.X. Li, J. Miao, S.Z. Wu, Q.L. Liu, Y. Jiang, H. Yang, L.J. Qiao, J. Alloys Comp. 548 (2013) 1.
[6] M.A. Ramireza, A.Z. Simõesb, A.A. Felixa, R. Tararama, E. Longoa, J.A. Varela, J. Alloys Comp. 509 (2009) 9930.
[7] X. Cao, X.M. Li, W.D. Yu, Y.W. Zhang, R. Yang, X.J. Liu, J.F. Kong, W.Z. Shen, J. Alloys Comp. 486 (2009) 458.
[8] C.H. Jia, Q.C. Dong, W.F. Zhang, J. Alloys Comp. 520 (2012) 250.
[9] Y.E. Syu, T.C. Chang, J.H. Lou, T.M. Tsai, K.C. Chang, M.J. Tsai, Y.L. Wang, M. Liu, S.M. Sze, Appl. Phys. Lett. 102 (2013) 172903.
[10] S.J. Choi, G.S. Park, K.H. Kim, S. Cho, W.Y. Yang, X.S. Li, J.H. Moon, K.J. Lee, K. Kim, Adv. Mater. 23 (2011) 3272.
[11] K. Mohanta, J. Rivas, R.K. Pai, J. Phys. Chem. C 117 (2013) 124.
[12] J.X. Wu, Z. Wen, D. Wu, H.F. Zhai, A.D. Li, J. Alloys Comp. 509 (2011) 2050.
[13] S.Y. Wang, D.Y. Lee, T.Y. Tseng, C.Y. Lin, Appl. Phys. Lett. 95 (2009) 112904.
[14] X.M. Chen, H. Zhang, K.B. Ruan, W.Z. Shi, J. Alloys Comp. 529 (2012) 108.
[15] A. Sawa, Mater. Today 11 (2008) 28.
[16] Q. Liu, J. Sun, H.B. Lv, S.B. Long, K.B. Yin, N. Wan, Y.T. Li, L.T. Sun, M. Liu, Adv. Mater. 24 (2012) 1844.
[17] J.J. Yang, M.D. Pickett, X. Li, D.A.A. Ohlberg, D.R. Stewart, R.S. Williams, Nat. Nanotechnol. 3 (2008) 429.
[18] J.P. Strachan, M.D. Pickett, J.J. Yang, S. Aloni, A.L.D. Kilcoyne, G. Medeiros-Ribeiro, R.S. Williams, Adv. Mater. 22 (2010) 3573.
[19] M.H. Lin, M.C. Wu, C.Y. Huang, C.H. Lin, T.Y. Tseng, J. Phys. D: Appl. Phys. 43 (2010) 295404.
[20] J.J. Yang, F. Miao, M.D. Pickett, D.A.A. Ohlberg, D.R. Stewart, C.N. Lau, R.S. Williams, Nanotechnology 20 (2009) 215201.
[21] J. Hafner, J. Comput. Chem. 29 (2008) 2044.
[22] J.P. Perdew, Y. Wang, Phys. Rev. B 45 (1992) 13244.
[23] J.P. Perdew, K. Burke, Y. Wang, Phys. Rev. B 54 (1996) 16533.
[24] P.E. Blöchl, Phys. Rev. B 50 (1994) 17953.
[25] H.J. Monkhorst, J.D. Pack, Phys. Rev. B 13 (1976) 5188.
[26] B. Silvi, A. Savin, Nature 371 (1994) 683.
[27] K. Momma, F. Izumi, J. Appl. Cryst. 41 (2008) 653.
[28] D. Deligny, P. Richet, Phys. Rev. B 53 (1996) 3013.
[29] B.J. Kennedy, C.J. Howard, B.C. Chakoumakos, Phys. Rev. B 59 (1999) 4023.
[30] R. Vali, Solid State Commun. 145 (2008) 497.
[31] S. Amisi, E. Bousquet, K. Katcho, P. Ghosez, Phys. Rev. B 85 (2012) 064112.
[32] Y.S. Lee, J.S. Lee, T.W. Noh, D.Y. Byun, K.S. Yoo, K. Yamaura, E. Takayama-Muromachi, Phys. Rev. B 67 (2003) 113101.
[33] C.G. Van De Walle, J. Neugebauer, J. Appl. Phys. 95 (2004) 3851.
[34] D.D. Cuong, B. Lee, K.M. Choi, H.S. Ahn, S. Han, J. Lee, Phys. Rev. Lett. 98 (2007) 115503.
[35] S.-G. Park, B. Magyari-Köpe, Y. Nishi, IEEE Electron. Dev. Lett. 32 (2011) 197.
[36] J.X. Zheng, G. Ceder, T. Maxisch, W.K. Chim, W.K. Choi, Phys. Rev. B 75 (2007) 104112.
[37] K.-H. Xue, P. Blaise, L.R.C. Fonseca, Y. Nishi, Phys. Rev. Lett. 110 (2013) 065502.
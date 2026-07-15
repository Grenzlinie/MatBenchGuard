![](./images/811607504344580096_1.jpg)

Nonlinear thermal transport and negative differential thermal conductance in graphene
nanoribbons

Jiuning Hu, Yan Wang, Ajit Vallabhaneni, Xiulin Ruan, and Yong P. Chen

Citation: *Applied Physics Letters* **99**, 113101 (2011); doi: 10.1063/1.3630026
View online: http://dx.doi.org/10.1063/1.3630026
View Table of Contents: http://scitation.aip.org/content/aip/journal/apl/99/11?ver=pdfcov
Published by the AIP Publishing

Articles you may be interested in
The effect of defects on negative differential thermal resistance in symmetric graphene nanoribbons
Appl. Phys. Lett. **104**, 013106 (2014); 10.1063/1.4861472

Tuning the thermal conductivity of graphene nanoribbons by edge passivation and isotope engineering: A
molecular dynamics study
Appl. Phys. Lett. **97**, 133107 (2010); 10.1063/1.3491267

Topological effect on thermal conductivity in graphene
J. Appl. Phys. **108**, 064307 (2010); 10.1063/1.3481677

Isotopic effects on the thermal conductivity of graphene nanoribbons: Localization mechanism
J. Appl. Phys. **107**, 054314 (2010); 10.1063/1.3329541

Thermal conductivity of graphene nanoribbons
Appl. Phys. Lett. **95**, 163103 (2009); 10.1063/1.3246155

![](./images/811607504344580096_2.jpg)

This article is copyrighted as indicated in the article. Reuse of AIP content is subject to the terms at: http://scitation.aip.org/termsconditions. Downloaded to IP:
120.117.138.77 On: Mon, 15 Dec 2014 01:15:40

# Nonlinear thermal transport and negative differential thermal conductance in graphene nanoribbons

Jiuning Hu, $^{1,2,a)}$ Yan Wang, $^{3}$ Ajit Vallabhaneni, $^{3}$ Xiulin Ruan, $^{2,3}$ and Yong P. Chen $^{1,2,4,b)}$

$^{1}$School of Electrical and Computer Engineering, Purdue University, West Lafayette, Indiana 47907, USA
$^{2}$Birck Nanotechnology Center, Purdue University, West Lafayette, Indiana 47907, USA
$^{3}$School of Mechanical Engineering, Purdue University, West Lafayette, Indiana 47907, USA
$^{4}$Department of Physics, Purdue University, West Lafayette, Indiana 47907, USA

(Received 1 April 2011; accepted 8 August 2011; published online 12 September 2011)

We employ classical molecular dynamics to study the nonlinear thermal transport in graphene nanoribbons (GNRs). For GNRs under large temperature biases beyond linear response regime, we have observed the onset of negative differential thermal conductance (NDTC). NDTC is tunable by varying the manner of applying the temperature biases. NDTC is reduced and eventually disappears when the length of the GNR increases. We have also observed NDTC in triangular GNRs, where NDTC exists only when the heat current is from the narrower to the wider end. These effects may be useful in nanoscale thermal managements and thermal signal processing utilizing GNRs. © 2011 American Institute of Physics. [doi:10.1063/1.3630026]

Graphene, $^{1,2}$ an atomic monolayer of graphite, has emerged as one of the most interesting materials in condensed matter physics and nanotechnology. Besides its unusual electronic properties, $^{2}$ graphene also has unique thermal properties, e.g., high thermal conductivities $(\sim 600$–5000 W/m-K). $^{3–7}$ Graphene nanoribbons (GNRs) are promising in many applications, such as their electronic band-gap tunability $^{8}$ and edge chirality dependent thermal transport. $^{9}$ So far, little attention has been paid to nonlinear thermal transport in GNRs, though these nonlinear effects have been explored in ideal atomic chains, $^{10–14}$ molecular junctions, $^{15}$ and quantum dots. $^{16}$ Here, we demonstrate negative differential thermal conductance (NDTC) in GNRs. Analogous to the electronic counterpart, $^{17}$ NDTC is a useful ingredient in developing GNR-based thermal management and signal manipulation devices, such as the thermal amplifiers $^{10}$ and thermal logic gates. $^{18}$

We study the thermal transport in GNRs using classical molecular dynamics (MD) simulations. The many-body empirical Brenner potential $^{19}$ is employed to describe the carbon-carbon interactions. This method have been applied in many graphene-based systems. $^{9,20–22}$ The structures of GNRs in this study are shown in the inset (rectangular GNR) of Fig. 1 and the inset (triangular GNR) of Fig. 3. The atoms denoted by squares are fixed in position, while those denoted by left- and right-pointing triangles are placed in two Nosé-Hoover $^{23,24}$ thermostats set at temperatures $T_{L}$ and $T_{R}$, respectively. The equations of motion for atoms without position being fixed are

$$
\frac{d}{dt}\mathbf{p}_{i}=\mathbf{F}_{i}-\gamma_{i}\mathbf{p}_{i},
\tag{1}
$$

where $\mathbf{p}_{i}$ is the momentum of the $i$-th atom, $\mathbf{F}_{i}$ is the total force acting on the $i$-th atom, and $\gamma_{i}$ is the Nosé-Hoover dynamic parameter. For the atoms denoted by circles, $\gamma_{i}\equiv 0$, and it recovers the NVE (constant number of atoms, volume, and energy) ensemble. For the atoms in the left and right thermostats, $\gamma_{i}$ obeys the equation

$$
\frac{d}{dt}\gamma_{i}=\frac{\left[\frac{2}{3N_{L(R)}k_{B}}\sum_{i\in L(R)}\frac{\mathbf{p}_{i}^{2}}{2m}\right]-T_{L(R)}}{\tau^{2}T_{L(R)}},
\tag{2}
$$

where $\tau$ is the thermostat relaxation time, $N_{L(R)}$ is the number of atoms in the thermostat, $k_{B}$ is the Boltzmann constant, and $m$ is the mass of the carbon atom. More details on our numerical calculation method can be found elsewhere. $^{9,25}$

First, we study the thermal transport in a rectangular GNR with armchair top and bottom edges shown in the inset of Fig. 1 (we have obtained qualitatively similar conclusions for GNRs with zigzag edges). Since the GNR is symmetrical, we only consider $T_{L}\leq T_{R}$ and define the temperature difference $\Delta T\equiv T_{R}-T_{L}$. The temperature $T_{R}$ is kept as a constant.

![](./images/811607504344580096_3.jpg)

FIG. 1. (Color online) Thermal current (left vertical axis) and average temperature (right vertical axis) vs. temperature difference $\Delta T$. The dashed boxes highlight NDTC. The inset shows the structure of the GNR $(\sim 1.5$ nm × 6 nm). $\blacksquare$ denotes fixed boundary atoms. $\blacktriangleleft$ ($\triangleright$) denotes atoms in the left (right) thermostat. $\bigcirc$ denotes the remain atoms in the bulk.

$^{a)}$Electronic mail: hu49@purdue.edu.
$^{b)}$Electronic mail: yongchen@purdue.edu.

![](./images/811607504344580096_4.jpg)

FIG. 2. (Color online) Thermal current (left vertical axis) and average temperature (right vertical axis) vs. temperature difference $\Delta T$ in GNRs with the similar structure as the GNR in the inset of Fig. 1, except for different lengths. In all these plots, $T_R=300$ K and $T_L$ is varied from 300 K to 30 K.

As we can see from both curves in Fig. 1, for small temperature difference (e.g., $\Delta T<60$ K for $T_R=300$ K and $\Delta T<150$ K for $T_R=600$ K), the thermal current increases approximately linearly as $\Delta T$ increases, as expected from Fourier's law. Interestingly, for some range of higher $\Delta T$, the thermal current decreases as $\Delta T$ increases (the dashed boxes in Fig. 1), indicating the onset of NDTC. It is a reasonable approximation to consider thermal current as proportional to the product of thermal conductivity $\kappa$ of the GNR and $\Delta T$. Our previous study $^9$ has shown that $\kappa$ increases with the average temperature $\bar{T}\equiv (T_L+T_R)/2=T_R-\Delta T/2$. We have plotted $\bar{T}$ (labeled at the right vertical axis and indicated by the right-pointing arrows for Figs. 1-3 and in the subplot of Fig. 4(b)) as a function of $\Delta T$ in all figures (note the $\bar{T}$ and $\Delta T$ plotted in Figs. 1-4 are based on MD calculated values for $T_R$ and $T_L$, which are close but may slightly differ from their set values). Since $\bar{T}$ decreases with $\Delta T$, $\kappa$ decreases with increasing $\Delta T$. The resulting trend of the thermal current as a function of $\Delta T$ is thus a competition between decreasing $\kappa$ and increasing $\Delta T$. In the $\Delta T$ range displaying NDTC, the decrease of $\kappa$ with $\Delta T$ dominates. We have found that there is no NDTC (shown in Fig. 4) if $T_L$ is larger than the constant $T_R$, i.e., if $\bar{T}$ increases with $\Delta T$ (thus without the above competition). Note that for large $\Delta T$ beyond linear response, strictly speaking thermal conductivity is not well defined. Thus, in the above explanation, $\kappa$ is considered to be an effective, average thermal conductivity. Similar arguments have been applied in analysing thermal transport in 1D atomic chains. $^{14}$

![](./images/811607504344580096_5.jpg)

FIG. 3. (Color online) Thermal current (left vertical axis) and average temperature (right vertical axis) vs. temperature difference $\Delta T$ in triangular GNR shown in the inset. The labels for the GNR structure have the same meaning as that in the inset in Fig. 1. The dashed box highlights NDTC.

Second, we study the length dependence of NDTC in GNRs. For all three GNRs of different lengths in Fig. 2, $T_R=300$ K while $T_L$ is varied from $T_R$ to 30 K. As the GNR length is increased, the $\Delta T$ value for the onset of NDTC increases and the $\Delta T$ range, where NDTC exists, shrinks. We thus suggest that NDTC will eventually disappear if the length of GNR exceeds some critical value. We have verified this using LAMMPS package $^{26}$ and velocity scaling $^{27}$ MD and found no NDTC in a 50 nm long GNR with similar structure as that studied in Fig. 1.

Besides these nonlinear effects in symmetrical GNRs, we also explore the possibility of NDTC in an asymmetrical triangular GNR, as shown in the inset of Fig. 3. Our previous study has pointed out that thermal rectification exists in this asymmetrical GNR. $^9$ As we see from Fig. 3, here the nonlinear thermal transport is also direction-dependent. NDTC appears when the temperature of the narrower end is held at $T_L=300$ K and the temperature $T_R$ of the wider end is varied from 300 K to 30 K (solid line in Fig. 3). However, there is no NDTC when the values of $T_L$ and $T_R$ are interchanged (dashed line in Fig. 3). This provides another possibility to control the nonlinear thermal transport and NDTC in GNRs by engineering the shape of GNRs.

In general, the way to tune the thermal current in the two-terminal thermal devices is very different from that in any two-terminal electronic devices. In the latter case, only the voltage difference matters. However, in thermal devices, the average temperature $\bar{T}$ is as important as the temperature difference $\Delta T$ in controlling the thermal current. For example, consider $\bar{T}=\alpha\Delta T+T_0$ with constants $\alpha$ and $T_0$, and we have $T_L=(\alpha-\frac{1}{2})\Delta T+T_0$ and $T_R=(\alpha+\frac{1}{2})\Delta T+T_0$. The thermal currents and average temperature $\bar{T}$ as a function of

![](./images/811607504344580096_6.jpg)

FIG. 4. (Color online) Thermal current (a) and average temperature (b) vs. temperature difference $\Delta T$ for different values of $\alpha$ for the GNR shown in the inset of Fig. 1. Note that $\alpha=0.5$ (-0.5) corresponds to $T_{L(R)}$ fixed at 300 K while $T_{R(L)}$ is varied.

$\Delta T$ are plotted in Fig. 4 for the rectangular GNR shown in the inset in Fig. 1, where $T_0=300$ K and $\alpha$ is tuned from $-0.5$ to $0.5$ (indicated by the dashed curved arrow in Fig. 4). The solid curve in Fig. 1 corresponds to $\alpha=-0.5$. For small temperature difference in the linear response regime, the slope of thermal current vs. $\Delta T$ is independent of $\alpha$. In the nonlinear response regime (large $\Delta T$), the system transitions from a regime with NDTC to a regime without NDTC when $\alpha$ is tuned from negative to positive values. We can see a strong correlation between the trend of the thermal current and that of the average temperature for different values of $\alpha$ in the range of $\Delta T$ from 100 K to 250 K where NDTC occurs for negative $\alpha$. For negative $\alpha$, since $\bar{T}$ decreases with $\Delta T$, the effective $\kappa$ decreases with $\Delta T$, and the occurrence of NDTC can be similarly explained as that for Fig. 1.

There are two independent parameters to control the thermal transport in two-terminal devices, either $(T_L,T_R)$ or $(\Delta T,\bar{T})$. Two-terminal thermal devices are actually analogous to three-terminal electronic devices. In the language of electronic transport of field effect transistors (FETs), $\Delta T$ plays the role of the drain-source voltage difference in FETs, while $\alpha$ plays the role of the gate voltage. Fig. 4 shows the ability to realize the FET-like behaviour in GNRs.

In summary, we have studied the nonlinear thermal transport in rectangular and triangular GNRs under large temperature biases. We find that in short ($\sim6$ nm) rectangular GNRs, the NDTC exists in a certain range of applied temperature difference. As the length of the rectangular GNR increases, NDTC gradually weakens. In triangular GNRs, NDTC only exists in the thermal current direction from the narrower to the wider end. The ability to tune and control NDTC by temperature parameters and GNR shapes provides potential ways to manage heat and manipulate thermal signals at the nanoscale.

This work is partially supported by the Semiconductor Research Corporation (SRC)—Nanoelectronics Research Initiative (NRI) via Midwest Institute for Nanoelectronics Discovery (MIND) and the Cooling Technologies Research Center (CTRC).

$^{1}$A. K. Geim and K. S. Novoselov, *Nature Mater.* **6**, 183 (2007).
$^{2}$A. H. C. Neto, F. Guinea, N. M. R. Peres, K. S. Novoselov, and A. K. Geim, *Rev. Mod. Phys.* **81**, 109 (2009).
$^{3}$A. Balandin, S. Ghosh, W. Bao, I. Calizo, D. Teweldebrhan, F. Miao, and C. N. Lau, *Nano Lett.* **8**, 902 (2008).
$^{4}$W. Cai, A. L. Moore, Y. Zhu, X. Li, S. Chen, L. Shi, and R. S. Ruoff, *Nano Lett.* **10**, 1645 (2010).
$^{5}$C. Faugeras, B. Faugeras, M. Orlita, M. Potemski, R. R. Nair, and A. K. Geim, *ACS Nano* **4**, 1889 (2010).
$^{6}$L. A. Jaureguia, Y. Yue, A. N. Sidorov, J. Hu, Q. Yu, G. Lopez, R. Jalilian, D. K. Benjamin, D. A. Delk, W. Wu, Z. Liu, X. Wang, Z. Jiang, X. Ruan, J. Bao, S. S. Pei, and Y. P. Chen, *ECS Trans.* **28**, 73 (2010).
$^{7}$J. H. Seol, I. Jo, A. L. Moore, L. Lindsay, Z. H. Aitken, M. T. Pettes, X. Li, Z. Yao, R. Huang, D. Broido, N. Mingo, R. S. Ruoff, and L. Shi, *Science* **328**, 213 (2010).
$^{8}$M. Y. Han, B. Ozyilmaz, Y. Zhang, and P. Kim, *Phys. Rev. Lett.* **98**, 206805 (2007).
$^{9}$J. Hu, X. Ruan, and Y. P. Chen, *Nano Lett.* **9**, 2730 (2009).
$^{10}$B. Li, L. Wang, and G. Casati, *Appl. Phys. Lett.* **88**, 143501 (2006).
$^{11}$W.-R. Zhong, P. Yang, B.-Q. Ai, Z.-G. Shao, and B. Hu, *Phys. Rev. E* **79**, 050103 (2009).
$^{12}$D. He, S. Buyukdagli, and B. Hu, *Phys. Rev. B* **80**, 104302 (2009).
$^{13}$E. Pereira, *Phys. Rev. E* **82**, 040101 (2010).
$^{14}$D. He, B.-Q. Ai, H.-K. Chan, and B. Hu, *Phys. Rev. E* **81**, 041131 (2010).
$^{15}$D. Segal, *Phys. Rev. B* **73**, 205415 (2006).
$^{16}$D. M.-T. Kuo and Y.-C. Chang, *Jpn. J. Appl. Phys.* **49**, 064301 (2010).
$^{17}$L. Esaki, *Phys. Rev.* **109**, 603 (1958).
$^{18}$L. Wang and B. Li, *Phys. Rev. Lett.* **99**, 177208 (2007).
$^{19}$D. W. Brenner, *Phys. Rev. B* **42**, 9458 (1990).
$^{20}$C. Y. Wang, K. Mylvaganam, and L. C. Zhang, *Phys. Rev. B* **80**, 155445 (2009).
$^{21}$Z.-Y. Ong and E. Pop, *Phys. Rev. B* **81**, 155408 (2010).
$^{22}$J. Hu, S. Schiffli, A. Vallabhaneni, X. Ruan, and Y. P. Chen, *Appl. Phys. Lett.* **97**, 133107 (2010).
$^{23}$S. Nosé, *J. Chem. Phys.* **81**, 511 (1984).
$^{24}$W. G. Hoover, *Phys. Rev. A* **31**, 1695 (1985).
$^{25}$J. Hu, X. Ruan, Z. Jiang, and Y. P. Chen, *AIP Conf. Proc.* **1173**, 135 (2009).
$^{26}$S. Plimpton, *J. Comput. Phys.* **117**, 1 (1995).
$^{27}$Z. Huang and Z. Tang, *Physica B* **373**, 291 (2006).
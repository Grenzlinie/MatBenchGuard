# Atomistic simulations of hydrogen embrittlement

Ryosuke Matsumoto $^{a,b}$, Shinya Taketomi $^{a,b}$, Sohei Matsumoto $^{a}$, Noriyuki Miyazaki $^{a,b,*}$

$^{a}$ Department of Mechanical Engineering and Science, Kyoto University, Yoshida-Honmachi, Sakyo-ku, Kyoto 606-8501, Japan
$^{b}$ National Institute of Advaned Industrial Science and Technology (AIST), 744 Motooka, Nishi-ku, Fukuoka 819-0395, Japan

---

## ARTICLE INFO

**Article history:**
Received 29 May 2009
Received in revised form
12 September 2009
Accepted 19 September 2009
Available online 16 October 2009

**Keywords:**
Hydrogen embrittlement
Atomistic simulation
Molecular dynamics method
Molecular statics method
Crack propagation
Dislocation

---

## ABSTRACT

It is well known that hydrogen weakens strengths of metals, and this phenomenon is called hydrogen embrittlement. Despite the extensive investigation concerning hydrogen related fractures, the mechanism has not been enough clarified yet. In this study, we applied the molecular dynamics method to the mode I crack growth in $\alpha$-Fe single crystals with and without hydrogen, and analyzed the hydrogen effects from atomistic viewpoints. We estimated the hydrogen trap energy in the vicinity of an edge dislocation in order to clarify the distribution of hydrogen atoms, using the molecular statics method. We also evaluated the energy barrier for dislocation motion under a low hydrogen concentration. Based on these results, we propose a mechanism for hydrogen embrittlement of $\alpha$-Fe under monotonic loading.

© 2009 Professor T. Nejat Veziroglu. Published by Elsevier Ltd. All rights reserved.

---

### 1. Introduction

Metals absorbing hydrogen show the reduction of ductility due to hydrogen [1] and the acceleration of fatigue crack growth [2]. This phenomenon is known as hydrogen embrittlement. Much attention has been paid to hydrogen as a clean energy source to solve environmental problems and to cope with the global warming problem. Increase in hydrogen use would result in increase of failure accidents related with hydrogen embrittlement.

Various mechanisms for hydrogen embrittlement have been proposed so far. Among them, the hydrogen enhanced decohesion (HEDE) [3,4] and the hydrogen enhanced localized plasticity (HELP) [5] are typical ones. In the HEDE mechanism, the bonds of metal atoms are weakened by hydrogen atoms. It has been, however, supposed that a hydrogen concentration is too low to weaken the bonds. In the HELP mechanism, a plastic behavior of a material is affected by hydrogen atoms. This mechanism is supported by experimental results. For example, increase in dislocation mobility is observed in *in situ* TEM observations [6–8]. It is also observed that slip bands are localized in the vicinity of a crack tip in fatigue tests using hydrogen-charged test specimens [2]. The fracture phenomenon caused by hydrogen embrittlement cannot be explained only by the HELP mechanism.

Despite a lot of experimental works concerning hydrogen embrittlement, for example Refs. [9] and [10], the mechanism of hydrogen embrittlement is not fully understood. Hydrogen has a high diffusivity and a low concentration in metal. It is, therefore, difficult to perform direct observation of hydrogen and to answer the question from experimental results what is a correct mechanism for hydrogen embrittlement. Atomistic simulations

---

* Corresponding author at: Department of Mechanical Engineering and Science, Kyoto University, Yoshida-Honmachi, Sakyo-ku, Kyoto 606-8501, Japan. Tel.: +81 75 753 5213; fax: +81 75 753 5719.
E-mail address: miyazaki@mech.kyoto-u.ac.jp (N. Miyazaki).
0360-3199/$ – see front matter © 2009 Professor T. Nejat Veziroglu. Published by Elsevier Ltd. All rights reserved.
doi:10.1016/j.ijhydene.2009.09.052

### Nomenclature

**Roman symbols**
| Symbol | Definition |
|--------|------------|
| $b$ | Magnitude of Burger's vector, m |
| $K_{\text{I}}$ | Mode I stress intensity factor, $\text{MPa}\sqrt{m}$ |
| $R$ | Gas constant, $\text{J/mol K}$ |
| $t$ | Time, s |
| $T$ | Absolute temperature, K |
| $x_{\text{eq}}$ | Hydrogen concentration expressed by the atomic ratio - |
| $x^0$ | Hydrogen concentration expressed by the atomic ratio without hydrostatic stress, - |

**Greek symbols**
| Symbol | Definition |
|--------|------------|
| $\delta\Omega_{\text{H}}$ | Partial molar volume of hydrogen, $\text{m}^3/\text{mol}$ |
| $\varepsilon$ | Ratio of number of hydrogen atoms to the number of iron atoms, - |
| $\sigma^{\text{hyd}}$ | Hydrostatic stress, MPa |

such as the molecular dynamics method, the molecular statics method and so on are powerful tools to study the mechanism for hydrogen embrittlement.

In the present study, after choosing an adequate interatomic potential for $\alpha$-Fe and hydrogen system (hereafter abbreviated as $\alpha$Fe–H system), we perform several kinds of atomistic simulations for such a system, that is, the molecular dynamics analyses of crack propagation and the molecular statics analyses of the interaction between dislocation and hydrogen atoms, and we propose a mechanism for hydrogen embrittlement of $\alpha$-Fe under monotonic loading, based on the results of the atomistic simulations.

## 2. Interatomic potential for $\alpha$Fe–H system

Adequate selection of an interatomic potential is of crucial importance for molecular dynamics and molecular statics calculations. Only three kinds of interatomic potential have been proposed so far for the $\alpha$Fe–H system. They are the embedded-atom-method (EAM) potential by Ruda et al. (abbreviated as EAM-R) [11], the Morse type potential by Hu et al. (abbreviated as Morse) [12] and the EAM potential by Wen et al. (abbreviated as EAM-W) [13]. EAM-W was formulated by improving EAM-R so as to reproduce more properties of the $\alpha$Fe–H system accurately. Thus, EAM-W is superior to EAM-R. In comparison with Morse, EAM-W provides accurate results for elastic constants of $\alpha$-Fe and the properties of hydrogen in $\alpha$-Fe, as shown in Tables 1 and 2. The elastic constants of $\alpha$-Fe calculated from EAM-W and Morse are shown in Table 1, compared with the experimental results [14]. The experimental results agree well with the calculated results using EAM-W. The heat of solution and migration energy of hydrogen in $\alpha$-Fe are shown in Table 2. They are also compared with experimental results [15,16]. Again EAM-W provides better results than Morse in comparison with the experimental results. Morse neglects H–H interactions. Moreover it takes account of the long-range (about 1 nm) interaction between iron and hydrogen atoms, so that it requires a large amount of computational time for a molecular dynamics calculation despite a pair potential. Because of the above reasons, we selected EAM-W as the best interatomic potential for the $\alpha$Fe–H system and employed it in the subsequent atomistic simulations.

<table>
<caption>Table 1 – Elastic constants of $\alpha$-iron.</caption>
<thead>
<tr>
<th></th>
<th>Exp. [14]</th>
<th>EAM-W</th>
<th>Morse</th>
</tr>
</thead>
<tbody>
<tr>
<td>$C_{11}$ (GPa)</td>
<td>243.1</td>
<td>230.2</td>
<td>244.3</td>
</tr>
<tr>
<td>$C_{12}$ (GPa)</td>
<td>138.3</td>
<td>135.8</td>
<td>80.7</td>
</tr>
<tr>
<td>$C_{44}$ (GPa)</td>
<td>138.1</td>
<td>116.7</td>
<td>80.7</td>
</tr>
</tbody>
</table>

## 3. Molecular dynamics analyses of crack propagation

We applied molecular dynamics simulations to the mode I crack propagation in $\alpha$-Fe single crystal with and without hydrogen for several analysis conditions, i.e. two kinds of crystal orientation and two levels of temperature.

### 3.1. Analysis model

Fig. 1 shows an analysis model whose shape is a circular disk with 9.7 nm in radius, 2.8 nm in thickness and 0.7 nm in thickness of the boundary region. The displacements corresponding to $K_{\text{I}}$ of $0.9\ \text{MPa}\sqrt{m}$ are prescribed to all atoms to introduce an initial crack. The origin is set at the crack tip and the $x$-axis and $z$-axis correspond to the forward direction of the initial crack and the thickness direction, respectively. This analysis model is a quasi three-dimensional model consisting of about 71,000 atoms, on which a periodic boundary condition in the $z$-direction is imposed.

According to Ref. [17], stable locations of hydrogen atoms are tetrahedral sites (T-sites), and a hydrogen distribution depends on the hydrostatic stress. Thus, hydrogen atoms are introduced at the T-sites in iron atoms in accordance with the following equations [18], using random numbers:

$$
x_{\text{eq}} =
\begin{cases}
x^0\exp\left(\frac{\sigma^{\text{hyd}}(X)\delta\Omega_{\text{H}}}{RT}\right) & (|X| \geq |r_0|) \\
x^0\exp\left(\frac{\sigma^{\text{hyd}}(r_0)\delta\Omega_{\text{H}}}{RT}\right) & (|X| < |r_0|)
\end{cases} \tag{1}
$$

where $x_{\text{eq}}$ is the hydrogen concentration expressed by the atomic ratio at a location $\boldsymbol{X}$, $x^0$ the hydrogen concentration without hydrostatic stress $\sigma^{\text{hyd}}$, $\delta\Omega_{\text{H}}$ the partial molar volume of hydrogen in $\alpha$-Fe, $R$ the gas constant and $T$ is the absolute

<table>
<caption>Table 2 – Heat of solution and migration energy of hydrogen atom.</caption>
<thead>
<tr>
<th></th>
<th>Exp.</th>
<th>EAM-W</th>
<th>Morse</th>
</tr>
</thead>
<tbody>
<tr>
<td>heat of solution (eV)</td>
<td>0.30 [15]</td>
<td>0.28</td>
<td>–</td>
</tr>
<tr>
<td>migration energy (eV)</td>
<td>0.035 [16]</td>
<td>0.037$^{\text{a}}$</td>
<td>0.05$^{\text{a}}$</td>
</tr>
<tr>
<td colspan="4">$^{\text{a}}$ a potential energy difference between hydrogen atoms at a tetrahedral site and an octahedral site.</td>
</tr>
</tbody>
</table>

![](./images/811828360945598464_1.jpg)

Fig. 1 - Analysis model.

temperature. We used $\delta\Omega_{\mathrm{H}}$ of $1.2 \times 10^{-6} \mathrm{~m}^{3} / \mathrm{mol}$ [18]. We selected $|r_{0}|=5.0 \times 10^{-10} \mathrm{~m}$ to avoid an infinite quantity of the hydrogen concentration at a crack tip. In the present study, we changed the hydrogen concentration $x^{0}$ from 0 (no hydrogen atom) to $5.0 \times 10^{-4}$ as an analysis parameter. The initial distribution of hydrogen atoms is shown in Fig. 2 for $x^{0}=3.0 \times 10^{-4}$ ( $\approx 5.4$ mass ppm) and $400 \mathrm{~K}$, where red points and blue points denote iron atoms and hydrogen atoms, respectively. It is found from the figure that the hydrogen concentration is higher around the crack tip than in the periphery of the analysis model because of stress concentration around the crack tip.

### 3.2. Analysis conditions

Crack propagation analyses were performed for two kinds of crystal orientation, crystal orientations (A) and (B), as shown in Fig. 3, in which the gray planes indicate the {112} slip planes of $\alpha$-Fe. In the crystal orientation (A), the crack plane is the (112) plane, and the forward direction of the initial crack is the [1$\overline{1}$0] direction. In this case, there is no slip plane in the xy-plane, and we can expect no dislocation emission from the crack tip. In the crystal orientation (B), the crack plane is the (110) plane, and the forward direction of the initial crack is the [001] direction. In this case, there exists {112} slip planes in the xy-plane, and we can expect the emissions of dislocations from the crack tip.

Although the ductile-brittle transition temperature (DBTT) for $\alpha$-Fe is less than $100 \mathrm{~K}$, the DBTT calculated using EAM-W is between $200 \mathrm{~K}$ and $300 \mathrm{~K}$. In the crystal orientation (B) where dislocation emissions are expected, we performed the crack propagation analyses at the initial temperature of $400 \mathrm{~K}$, which is above the DBTT, and that of $100 \mathrm{~K}$, which is below the DBTT. Dislocation emissions are expected at $400 \mathrm{~K}$, and no dislocation emission is expected at $100 \mathrm{~K}$. In the crystal orientation (A), no dislocation emission is expected at any temperature, so that we performed the crack propagation analyses only at the initial temperatures of $400 \mathrm{~K}$. We can discuss the effect of dislocations on the crack growth behavior by comparing the result of the crystal orientation (A) at $400 \mathrm{~K}$ with that of the crystal orientation (B) at $400 \mathrm{~K}$. In the present analyses, we did not control the temperature of the analysis system to keep the temperature at a constant value during crack propagation.

The crack propagation analyses were performed by imposing the displacement rate corresponding to the rate of

![](./images/811828360945598464_2.jpg)

Fig. 2 - Initial distribution of hydrogen atoms ($\mathrm{x}^{0}=3.0 \times 10^{-4}$).

![](./images/811828360945598464_3.jpg)

Fig. 3 - Arrangement of [112] slip planes. (a) Crystal orientation (A) (b) Crystal orientation (B).

![](./images/811828360945598464_4.jpg)

Fig. 4 - Snapshots of crack propagation behavior for the crystal orientation (A) at 400 K ($x^0 = 0$).

stress intensity factor $dK_{I}/dt=5.0\times10^{9}\mathrm{MPa}\sqrt{m}/\mathrm{s}$ on the atoms in the boundary region of the analysis model. This analysis condition is equivalent to the crack opening velocity of 0.4 m/s, which is very slow for a molecular dynamics analysis. In the present analyses, we performed several numbers of analyses with different initial locations of hydrogen atoms and different initial velocities of iron and hydrogen atoms for the respective analysis conditions by changing random numbers in order to avoid the effect of initial conditions.

### 3.3. Results and discussion

#### 3.3.1. The cases without dislocation emission
In the crystal orientation (A), crack propagation analyses were performed for four cases of the initial hydrogen concentration, $x^0$=0 (no hydrogen atom), $1.0\times10^{-4}$, $3.0\times10^{-4}$ and $5.0\times10^{-4}$ at the initial temperature of 400 K. A crack propagation behavior is shown for the case without hydrogen ($x^0=0$) in Fig. 4, where a green part indicates the bcc crystal structure and a black one other crystal structures. In this case, a crack propagates straight without dislocation emission. Although the figures are omitted here, similar crack propagation behaviors were also obtained for the cases with hydrogen atoms ($x^0=1.0\times10^{-4}, 3.0\times10^{-4}$ and $5.0\times10^{-4}$). Fig. 5 shows the time evolution of crack growth length in the crystal orientation (A) at 400 K. Significant differences in the initiation time for crack growth and the crack growth velocity are not observed among the respective hydrogen concentrations.

In the crystal orientation (B), crack propagation analyses were performed for $x^0=0$ (no hydrogen atom), $1.0\times10^{-4}$ and $2.0\times10^{-4}$ at the initial temperature of 100 K. Fig. 6 shows a crack propagation behavior for $x^0=1.0\times10^{-4}$. As expected, no dislocation emission is observed because of a lower temperature than the DBTT, and a crack propagates nearly straight. No meaningful difference is observed between the cases with and without hydrogen atom.

#### 3.3.2. The cases with dislocation emissions
In the crystal orientation (B), crack propagation analyses were performed for five cases of the initial hydrogen concentration, $x^0=0$ (no hydrogen atom), $0.5\times10^{-4}$, $1.0\times10^{-4}$, $3.0\times10^{-4}$ and $5.0\times10^{-4}$ at the initial temperature of 400 K. The distributions of hydrogen atoms around dislocation cores are shown for $x^0=3.0\times10^{-4}$ in Fig. 7, where a grey circle and a black one denote an iron atom and a hydrogen atom, respectively. It is found from the figure that hydrogen atoms are trapped around dislocation cores within 100ps. Detailed discussion on the interaction between dislocations and hydrogen atoms will be given in the following section.

Figs. 8(a), (b) and (c) respectively represent the crack propagation behaviors for three cases of hydrogen concentration, that is, (a) $x^0=1.0\times10^{-4}$, (b) $x^0=3.0\times10^{-4}$ and (c) $x^0=0$ (no hydrogen atom). As shown in Figs. 8(a) and (b), not only dislocation emissions from the crack tip but also crack propagation along the {112} slip planes are observed in high frequency in the cases with hydrogen atoms. On the other hand, as shown in Fig. 8(c), only crack tip blunting caused by dislocation emissions tends to be observed without crack propagation in the case where no hydrogen atom is included. The fracture in the slip plane is observed in only one case in the case without hydrogen atom and in three cases in the cases with hydrogen atoms out of four cases with different initial conditions.

Figs. 9(a) and (b) show the enlarged figures near the crack tip during slip plane fracture. It is found that hydrogen atoms gather on the {112} slip planes, from which slip plane fracture occurs. The hydrogen atoms trapped near dislocation cores seem to promote the crack propagation along the slip plane.

In the molecular dynamic analysis, we can deal with atomic motion for only a very short period of pico-second order. In actual, a lot of hydrogen atoms would be trapped for a long period of time, and hydrogen atoms trapped with high

![](./images/811828360945598464_5.jpg)

Fig. 5 - Time evolution of crack growth length in the crystal orientation (A) at 400k.

![](./images/811828360945598464_6.jpg)

Fig. 6 - Snapshots of crack propagation behavior for the crystal orientation (A) at 100 K $(x^{0}=1.0\times 10^{-4})$.

density at the dislocations emitted from a crack tip would induce the fracture in the slip plane easier than expected in the molecular dynamics simulations.

## 4. Molecular statics analyses of interaction between dislocation and hydrogen

In section 3, we presented the results of the molecular dynamics analyses showing that hydrogen atoms gather around the cores of edge dislocations on the {112} slip planes. Here we will deal with this phenomenon in detail using the molecular statics method. We will also show how hydrogen atom affects dislocation motion. We have already published the paper concerning these phenomena [19]. So we will show the results briefly.

### 4.1. Hydrogen occupation sites around dislocation core

We consider the interaction between an edge dislocation on the {112} slip planes and hydrogen atoms. Fig. 10 shows an analysis model, in which the (112)[111] edge dislocation is introduced on the xz-plane by removing an atomic plane and relaxing the atomic structure using the conjugate gradient (CG) method. The analysis model contains 8054 iron atoms, and the dimensions of the unit cell are 11.05 nm in the x-direction, 4.91 nm in the y-direction and 2.02 nm in the z-direction. A periodic boundary condition was imposed on the x- and z-directions. The dislocation density in this system is approximately $0.018nm^{-2}$. We used EAM-W as the interatomic potential for the $\alpha$Fe-H system. A hydrogen atom was allocated either at the T-site or the O-site near the dislocation core, and then the positions of iron and hydrogen atoms were relaxed to minimize the total potential energy using the CG method. The hydrogen trap energy at each occupation site is shown in Fig. 11. We can observe three regions with strong hydrogen trap energy. The hydrogen trap energy is strongest around the dislocation core. It is also relatively strong around a high hydrostatic stress region (region A in Fig. 11) and along a slip plane (region B in Fig. 11). It should be noted that the region B has strong hydrogen trap energy. This could not be predicted by the theory of elasticity that hydrogen and dislocation interact mechanically as a result of lattice dilatation caused by hydrostatic stress. Furthermore, the result suggests that a lot of hydrogen atoms accumulate on the slip plane around the dislocation core.

### 4.2. Effect of hydrogen on dislocation mobility

In situ TEM observation performed by Robertson et al. [6-8] revealed that the distance between dislocations decreases when hydrogen gas is introduced during TEM observation. This fact indicates increase in dislocation mobility by hydrogen atoms. The elastic analysis performed by Sofronis and Birnbaum [20] showed that the shear stress acting on dislocation decreases with increase in hydrogen concentration. This

![](./images/811828360945598464_7.jpg)

Fig. 7 - Hydrogen distributions during cleavage in the slip plane for the crystal orientation (B) at 400 K. $(x^{0}=3.0\times 10^{-4})$.

![](./images/811828360945598464_8.jpg)

Fig. 8 - Snapshots of crack propagation behavior for the crystal orientation (B) at 400 K. (a) $x^0 = 1.0 \times 10^{-4}$ (b) $x^0 = 3.0 \times 10^{-4}$ (c) $x^0 = 0$.

phenomenon is called the hydrogen-induced shielding effect.
They concluded that the hydrogen-induced shielding effect causes increase in dislocation mobility. Their conclusion needs to be examined, because they did not consider the effect of hydrogen atoms at a dislocation core and dealt with extremely high hydrogen concentrations such as $\varepsilon$ (the ratio of the number of hydrogen atoms to the number of iron atoms) of 0.1 and 0.01. It is not confirmed whether the hydrogen-induced

![](./images/811828360945598464_9.jpg)

Fig. 9 - Enlarged views near the crack tip during cleavage in the slip plane for the crystal orientation (B) at 400 K.
(a) $x^0 = 1.0 \times 10^{-4}$ (b) $x^0 = 3.0 \times 10^{-4}$.

![](./images/811828360945598464_10.jpg)

Fig. 10 - Analysis model for molecular statics analyses of interaction between dislocation and hydrogen.

shielding effect holds for a low hydrogen concentration. Therefore we study the effect of hydrogen from the viewpoint of energy barrier for dislocation motion.

According to the hydrogen trap energy obtained in 4.1, it is the highest at a dislocation core. Thus the probability of hydrogen occupation is the highest at the dislocation core. From this reason, we placed hydrogen atoms at the disloca- tion core. We used the same analysis model shown in Fig. 10. We evaluated the energy barrier for the edge dislocation motion of $1b$ (b: the magnitude of Burger's vector) with and without hydrogen, using the nudged elastic band (NEB) method [21]. We obtained the energy barrier for the following three cases; (a) without hydrogen atom, (b) with a hydrogen atom at the dislocation core in the initial state and the dislo- cation moving forward by $1b$, and (c) with a hydrogen atom $1b$ ahead of the initial dislocation and the dislocation moving to the hydrogen atom. The hydrogen concentration of this system is 2.24 mass ppm, and the number of hydrogen atoms per unit length of a dislocation line is $0.49nm^{-1}$. The variations of energy barrier with dislocation motion are shown in Fig. 12 for the case without a hydrogen atom and two cases with a hydrogen atom. As shown in Fig. 12, the energy barrier for dislocation motion is $2.65×10^{-20}J$ for the case without a hydrogen atom, while it decreases to $2.35×10^{-20}J$ for the case (b) with a hydrogen atom and $1.18×10^{-20}J$ for the case (c) with a hydrogen atom. It is concluded that the energy barrier for dislocation motion decreases due to hydrogen atoms.

![](./images/811828360945598464_11.jpg)

Fig. 11 - Distribution of hydrogen trap energy at each site of hydrogen.

![](./images/811828360945598464_12.jpg)

Fig. 12 - Variations of the energy barrier for dislocation motion.

Next we performed atomistic analyses in order to examine whether the hydrogen-induced shielding effect holds under a low hydrogen concentration. We obtained the stress field around an edge dislocation based on atomistic model shown in Fig. 10. The stress field around the dislocation is calculated using the molecular statics method both for the case without a hydrogen atom and for the case with hydrogen atoms. Fig. 13 shows the shear stress distributions along the slip plane near a dislocation core. It is found from the figure that the shear stress distribution is not affected by hydrogen atoms. Even if the number of hydrogen atoms per unit length of a dislocation line is increased up to $7.35nm^{-1}$, no significant difference in the stress distribution is observed. So the hydrogen-induced shielding effect is not observed under low hydrogen concen- tration conditions.

![](./images/811828360945598464_13.jpg)

Fig. 13 - Shear stress distributions along the slip plane near a dislocation core.

![](./images/811828360945598464_14.jpg)

Fig. 14 - Effect of hydrogen atoms on the surface energy.

It is shown that hydrogen at a dislocation core reduces the energy barrier for dislocation motion. It is also shown that the hydrogen-induced shielding effect is very small. It is therefore suggested that one reason for increase in dislocation mobility under low hydrogen concentration conditions is not the hydrogen shielding effect but the reduction of the energy barrier for dislocation motion due to hydrogen.

## 5. Mechanism for hydrogen embrittlement

The molecular statics analysis using EAM-W provides the result that hydrogen atoms existing on a slip plane promote the separation of the slip plane because of decrease in its surface energy caused by hydrogen atoms. Fig. 14 shows the effect of hydrogen atoms on the surface energy of $\alpha$-Fe for {100}, {110} and {112} surfaces. Considering this fact and the results shown in sections 3 and 4, we can propose the following mechanism for hydrogen embrittlement of $\alpha$-Fe under monotonic loading, as follows:

(1) Dislocations are emitted from a crack tip and they exist along a slip plane.
(2) A lot of hydrogen atoms are trapped at dislocation cores and along a slip plane in the vicinity of a dislocation core.
(3) The hydrogen atoms at a dislocation core reduce the energy barrier for dislocation motion and increases dislocation mobility. Thus the distance between dislocations is reduced.
(4) Separation of a slip plane is caused due to the hydrogen atoms trapped by a dislocation, and such separation is connected among pile-up dislocations.

Our proposed mechanism is a hybrid of the HELP and the HEDE. The fracture is associated with the HELP mechanism in that plastic deformation with dislocations is needed prior to the fracture. On the other hand, the fracture is associated with the HEDE mechanism in that the fracture results from the separation of a slip plane.

Our proposed mechanism for the hydrogen embrittlement agrees well with several experimental observations [22,23] showing that the fracture of a hydrogen-charged test specimen occurs at {110} or {112} slip planes.

## 6. Concluding remarks

We chose EAM-W as the best interatomic potential for the $\alpha$Fe-H system. We performed the molecular dynamics analyses of crack propagation in $\alpha$-Fe including hydrogen atoms under monotonic loading. We estimated the hydrogen trap energy in the vicinity of a (112)[111] edge dislocation in order to clarify the distribution of hydrogen atoms. We also evaluated the energy barrier for dislocation motion under a low hydrogen concentration. Based on the above results, we have proposed a mechanism for hydrogen embrittlement of $\alpha$-Fe under monotonic loading. Our proposed mechanism agrees well with several experimental observations.

## Acknowledgements

This research was performed as a part of the Fundamental Research Project on Advanced Hydrogen Science funded by the New Energy and Industrial Technology Development Organization (NEDO).

## REFERENCES

[1] Han G, He J, Fukuyama S, Yokogawa K. Effect of strain-induced martensite on hydrogen environment embrittlement of sensitized austenitic steels at low temperatures. Acta Mater 1998;46:4559-70.
[2] Murakami Y. The effect of hydrogen on fatigue properties of metals used for fuel cell system. Int J Fract 2006;138:167-95.
[3] Steigerwald EA, Schaller FW, Troiano AR. The role of stress in hydrogen induced delayed failure. Tran Am Inst Mining Metall Engrs 1960;218:832-41.
[4] Oriani RA, Josephic PH. Equilibrium aspects of hydrogen-induced cracking of steels. Acta Metall 1974;22:1065-9.
[5] Beachem CD. A new model for hydrogen-assisted cracking (Hydrogen "embrittlement"). Metall Trans 1972;3:437-51.
[6] Ferreira PJ, Robertson IM, Birnbaum HK. Hydrogen effects on the interaction between dislocations. Acta Mater 1998;46:1749-57.
[7] Ferreira PJ, Robertson IM, Birnbaum HK. Hydrogen effects on the character of dislocations in high-purity aluminum. Acta Materialia 1999;47:2991-8.
[8] Sofronis P, Robertson IM. Transmission electron microscopy observations and micromechanical continuum models for the effect of hydrogen on the mechanical behaviour of metals. Phil Magazine A 2002;82:3405-13.
[9] Kanezaki T, Narazaki C, Mine Y, Matsuoka S, Murakami Y. Effects of hydrogen on fatigue crack behavior of austenitic stainless steel. Int J Hydrogen Energy 2008;33:2604-19.
[10] Mine Y, Narazaki C, Murakami K, Matsuoka S, Murakami Y. Hydrogen transport in solution-treated and pre-strained

stainless steels and its role in hydrogen-enhanced fatigue crack growth. Int J Hydrogen Energy 2009;34:1097-107.

[11] Ruda M, Farkas D, Abriata J. Embedded-atom interatomic potentials for hydrogen in metals and intermetallic alloys. Phys Rev B 1996;54:9765-74.

[12] Hu Z, Fukuyama S, Yokogawa K, Okamoto S. Hydrogen embrittlement of a single crystal of iron on a nanometre scale at a crack tip by molecular dynamics. Model Simul Mater Sci 1999;7:541-51.

[13] Wen M, Xu XJ, Fukuyama S, Yokogawa K. Embedded-atom- method functions for the body-centered-cubic iron and hydrogen. J Mater Res 2001;16:3496-502.

[14] Simmons G, Wang H. Single crystal elastic constants and calculated aggregate properties: a handbook. 2nd ed. Cambridge: MIT Press; 1971.

[15] Wipf H. Hydrogen in metals III: topics in applied physics, vol. 73. Berlin: Springer-Verlag; 1997. p. 51.

[16] Hirth JP. Effects of hydrogen on the properties of iron and steel. Metall Trans A 1980;11A:861-90.

[17] Fukai Y. Site preference of interstitial hydrogen in metals. J Less-Common Metals 1984;101:1-16.

[18] Fukai Y, Tanaka K, Uchida H. Suiso to kinzoku (Hydrogen and metals). Tokyo: Uchida Rokakuho; 1998. p. 193-226.

[19] Taketomi S, Matsumoto R, Miyazaki N. Atomistic simulation of the effects of hydrogen on the mobility of edge dislocation in alpha iron. J Mater Sci 2008;43:1166-9.

[20] Sofronis P, Birnbaum HK. Mechanics of the hydrogen- dislocation-impurity interactions 1. Increasing shear modulus. J Mech Phys Solids 1995;43:49-90.

[21] Henkelmann G, Jónsson H. Improved tangent estimate in the nudged elastic band method for finding minimum energy paths and saddle points. J Chem Phys 2000;113:9978-85.

[22] Bernstein IM. Hydrogen-induced cracking in iron - Morphology and crack path dependence. Metall Trans 1970;1:3143-50.

[23] Nagumo M, Miyamoto K. Microscopic process of failure and mechanism of hydrogen embrittlement of iron. J Jpn Inst Metals 1981;45:1309-17.
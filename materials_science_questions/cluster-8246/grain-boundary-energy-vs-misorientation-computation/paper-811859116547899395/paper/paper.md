# Investigation on quenching at a high-angle Cu grain boundary on an atomic scale

This content has been downloaded from IOPscience. Please scroll down to see the full text.

2006 Chinese Phys. 15 610

(http://iopscience.iop.org/1009-1963/15/3/028)

View [the table of contents for this issue], or go to the [journal homepage] for more

Download details:

IP Address: 128.111.121.42
This content was downloaded on 28/08/2015 at 10:26

Please note that [terms and conditions apply].

# Investigation on quenching at a high-angle Cu grain boundary on an atomic scale*

Zhang Lin(张 林)${}^{\text{a})\dagger}$, Wang Shao-Qing(王绍青)${}^{\text{b)}}$, and Ye Heng-Qiang(叶恒强)${}^{\text{b)}}$

${}^{\text{a)}}$College of Science, Northeastern University, Shenyang 110004, China
${}^{\text{b)}}$Shenyang National Laboratory for Materials Science, Institute of Metal Research,
Chinese Academy of Sciences, Shenyang 110016, China

(Received 16 June 2005; revised manuscript received 21 December 2005)

We have performed molecular dynamics simulations of structural changes due to quenching the melting interface at a Cu $\Sigma5(310)/[001]$ symmetrical tilt grain boundary. The simulation results suggest that the grain boundary structures due to quenching are different from those due to heating up to the same temperature. The calculated atom density profiles show that the grain boundary structures can be significantly changed as they are quenched to quite low temperatures.

Keywords: molecular dynamics, solidification, crystal, interface

PACC: 6185, 6470D, 6848, 6800

## 1. Introduction

The role of grain boundaries (GBs) in understanding mechanical and thermal properties of bulk polycrystalline materials has aroused the interest at material researchers over the last several decades.${}^{[1-10]}$ Nevertheless, since the relevant spatial regions for the grain boundaries are usually only a few atomic layers thick, problems concerning the grain boundaries are difficult to study experimentally. Therefore, simulation can serve as an important tool to study the effect of the interface region on the material properties on an atomic scale.${}^{[11-18]}$ In fact, simulations, based on molecular dynamics (MD) and Monte Carlo methods, have been performed to investigate GB structures, in particular, the high-temperature structures of the GBs.${}^{[19-25]}$ The recent results of MD simulations have suggested that a high angle grain boundary with high-energy, such as a $\Sigma5(310)/[001]$ (reciprocal density of coincidence site lattice $=5(310)/[001]$) symmetric tilt Cu grain boundary, may undergo a definite melting transition at a temperature significantly below its bulk melting point.${}^{[26-28]}$ Then, the following question arises. If the GB region, that has become liquid at a temperature significantly below the bulk melting point of the studied metal, is quenched, how does the structure of the GB region change?

In the present paper, we report on molecular dynamics calculations in which we determine the structural changes by quenching the melting interface of a $\Sigma5(310)/[001]$ symmetric tilt Cu grain boundary using an Embedded-Atom-Method (EAM) potential.

## 2. System and simulation method

### 2.1. Simulation cell

The configuration of the simulated GB cell is illustrated in Fig.1. It is constructed by making crystallographic planes (310) parallel to the desired GB plane, and subsequently rotating through $180^{\circ}$ one grain relative to the other about the direction normal to the GB plane. This rotation produces a symmetric tilt coincident-site-lattice (CSL) GB with the reciprocal density of coincident sites $\Sigma5(310)/[001].{}^{[2]}$ There are 12 CSL units in the $X$ axis, and $10a_{0}$ in the $Z$ axis, where $a_{0}$ is the lattice constant of Cu. In the $Y$ axis, to avoid the influences of the borders on grain boundary calculations, the space scale should be much larger than that in the $X$ or $Z$ axis, and it is $44\ a_{0}$ in this simulation. Hence, a bicrystalline GB represented by a rectangular cell containing 33480 atoms is created.

---
*Project supported by the Special Foundation for State Major Basic Research Program of China (Grant No G2000067104)
${}^{\dagger}$E-mail:gsj-cn@tom.com
http://www.iop.org/journals/cp

![](./images/811859116547899395_1.jpg)

Fig.1. A schematics geometry of the simulation cell of the bicrystal with a Σ5(310)/[001] tilt symmetric boundary.

In our MD simulations of the bicrystalline GB, two dimensional periodic border conditions are imposed in $X$ and $Z$ axes. In the $Y$ axis, which is normal to the GB plane, the free (dynamic) atoms, corresponding to the up_crystal and down_crystal parts, are sandwiched between two rigid slabs of fixed (static) atoms, corresponding to the up_border and down_border parts as shown in Fig.1. The thickness of each rigid slab is about $3a_{0}$, which is twice the cutoff radius of atomic interaction. At any given temperature, the fixed atoms occupy ideal lattice positions, but each rigid slab is permitted to move as a whole in response to the total force exerted by the up_crystal and down_crystal parts.$^{[29,30]}$

### 2.2. Interatomic potential

The interatomic potential plays a crucial role in molecular dynamics simulations. The EAM potential of Cu given by J. Mei *et al* will be used throughout this study. This potential is known to provide a good description of the thermodynamic properties of fcc transition metals.$^{[31,32]}$ In the frame of EAM, the total energy of an N-atom system takes the following form:

$$
E_{\mathrm{tot}}=\sum_{i} F_{i}\left(\rho_{\mathrm{e}}\right)+\frac{1}{2} \sum_{\substack{m=n \\ m}} \phi_{i j}\left(r_{i j}\right), \tag{1}
$$

where $\phi_{i j}(r_{i j})$ is a two-body central potential between atoms $i$ and $j$ with a separation of $r_{i j}$ in between, and $F_{i}(\rho_{\mathrm{e}})$ is the embedding energy of atom $i$ with the electron density $\rho_{\mathrm{e}}$. The two-body potential and atomic density are both cut off at about $5.0 \mathring{A}$. In terms of this EAM potential, the lattice constant $a_{0}$ of Cu is $3.615 \mathring{A}$. The forms of the two-body potential, the electron density, and the embedded energy can be found in Ref.[31]. Throughout the calculation, a time step of $1.6 \times 10^{-15}$ s is used.

### 2.3. Molecular dynamics calculations

In calculating the structural changes of the grain boundary at different temperatures, the simulation cell is divided into some layers along the $Y$ direction, and the following values are determined:

$$
S_{L_{\mathrm{s}}}=\left\langle\frac{1}{N_{L_{\mathrm{s}}}^{2}}\left|\sum_{m \in L_{\mathrm{s}}} \exp \left(\mathrm{i} \boldsymbol{k} \cdot \boldsymbol{r}_{\mathrm{m}}\right)\right|^{2}\right\rangle, \tag{2}
$$

$$
g_{L_{\mathrm{g}}}(r)=\frac{V}{N}\left\langle\sum_{i \in L_{\mathrm{g}}} \sum_{j \neq i \in L_{\mathrm{g}}} \delta\left(\boldsymbol{r}-\boldsymbol{r}_{i j}\right)\right\rangle, \tag{3}
$$

$$
\rho\left(Y_{i}\right)=\left\langle N_{i}\right\rangle / V_{i}, \tag{4}
$$

$$
\hat{e}_{L}(Y)=\left\langle\sum_{i \in L} e_{i} / N_{\mathrm{L}}\right\rangle, \tag{5}
$$

where the angular brackets represent time average, $S_{L_{\mathrm{s}}}$ is the static structure factor in the region $L_{\mathrm{s}}$, $\boldsymbol{r}_{\mathrm{m}}$ the position of the atom $m$, $N_{L_{\mathrm{s}}}$ the number of atoms in the layer $L_{\mathrm{s}}$, and summation is performed over these atoms. $\boldsymbol{k}(=0,0,4 \pi / a)$ is chosen such that $S$ is equal to unity at zero temperature, and when the structure completely loses the long-range order, $S$ should be close to zero. $g_{L_{\mathrm{g}}}(r)$ is the pair distribution function in the layer $L_{\mathrm{g}}$, $V$ is the volume of the simulated MD cell, and $N$ is the atom number in this cell. The pair distribution function gives the probability of finding a pair of atoms at a distance $r$ apart, relative to the probability expected for a completely random distribution at the same density. The density profile $\rho(Y_{i})$ is calculated by dividing the system into some layers along the $Y$ axis and accumulating a histogram of the number $N_{i}$ of atoms in each layer, where $<N_{i}>$ is the average number of atoms in the layer $i$ of volume $V_{i}$, $Y_{i}$ being taken as the centre of this layer. $\hat{e}_{L}$ is the energy per atom in the layer $L$, $e_{i}$ the energy of the $i$th atom of this layer, and $N_{L}$ the number of atoms in this layer.

## 3. Results and discussion

In order to investigate the structural changes of grain boundaries due to quenching, a melting region in the grain boundary needs constructing. Hence, we first consider a heating series. This run starts at 300K and in each successive run the temperature is increased by an increment of 100K (up to 1200K). At each temperature, the initial runs take about 100,000 time steps to reach equilibration, and the subsequent

20,000 time steps to record the atomic trajectories that are used to study the physical properties of the simulated system. The temperature is kept constant by rescaling the atomic velocities once every 50 time-steps.

![](./images/811859116547899395_2.jpg)

Fig.2. The static structure factor profiles.

![](./images/811859116547899395_3.jpg)

Fig.3. The atom density profile at 300K.

Since the structure factor $S$ defined above provides a convenient quantitative measure for the overall degree of crystallinity or, conversely, of long-range structural disorder, the simulation cell is divided into 90 layers along the $Y$ direction. In Fig.2 the layer-by-layer structural factor profiles at two temperatures 300K and 1100K are compared. At 300K the interfacial region of this simulated cell is apparently different from its bulk region, as evidenced by the low values in this region as shown in this figure. It indicates that the interfacial region is less ordered than in bulk. At 1100K, $S$ in the centre of the simulated bicrystal decreases down to zero, which implies that the complete disorder appears in this region. Figure 3 shows the density profile of this simulated cell along the $Y$ axis at the temperature 300K. The most characteristic feature of the density profile is the exceed-ingly high density at the centre of this cell corresponding to the grain boundary, and inter-peak spacing at the centre is apparently larger than that in the bulk. Near to the centre, there are two oscillation regions of the density, but the inter-peak spacing remains constant. Next to these oscillation regions (along the $Y$ direction), both the density and inter-peak spacing almost remain constant as shown in this figure. Therefore, the density profiles can be divided into three distinct regions: grain boundary region I, oscillation regions II_up and II_down, and bulk regions III_up and III_down, where "up" and "down" refer to the up_crystal and down_crystal in Fig.1. In these oscillation regions as shown in Fig.3, although the inter-peak spacing is the same as that in each bulk region, their density peaks have different values and they apparently are smaller than those in the bulk regions.

Figure 4 illustrates the internal-energy per atom in the region of $21.5a_0-22.5a_0$ along the $Y$ axis corresponding to the grain boundary region in Fig.3 owing to the heating series. The internal-energy changes following a straight-line behaviour up to 1000K, whereas at 1100K the energy increases to a distinctly higher value as the system becomes structurally disordered as indicated by $S$ in Fig.2. This behaviour can be regarded as melting, and the melting transition occurs at about 1088K as will be indicated by a further calculation.

![](./images/811859116547899395_4.jpg)

Fig.4. Variation of energy per atom with temperature.

It is shown in Fig.5 that when the temperature is increased up to 1100K, the density profiles at this temperature exhibit a feature of the oscillations as they

decay to a constant density value. Therefore, it is a proof that the GB region has become liquid at this temperature. Figure 5(b) shows the magnified region $14a_0$-$20a_0$ of Fig.5(a), where the density decreases, in traversing the interface, from the crystal to the liquid due to reducing the number of atoms per layer.

Figure 6 shows the pair distributions of these regions at 1100K, where the pair distribution of II_up region still shows the fcc-crystal ordered behaviour, whereas in region I the second peak disappears and the third peak also is broadened, which shows the liquid-like behaviour.

![](./images/811859116547899395_5.jpg)

Fig.5. The atom density profile at the temperature 1100K. Fig.5(b) shows the magnified part from $14a_0$ to $20a_0$ in Fig.5(a).

![](./images/811859116547899395_6.jpg)

Fig.6. Pair functions of different regions.

After obtaining the melting interface at the temperature 1100K, we consider the structural changes due to quenching. Temperatures used in the quenching procedure are 1090K (100000 steps), 1000K (75000 steps), 900K (55000 steps), 800K (55000 steps), 700K (55000 steps), 600K (55000 steps), 500K (55000 steps), 400K (55000 steps), and 300K (55000 steps). The numbers in parentheses refer to the time steps used for the simulations. As mentioned above, the interface melting occurs at the temperature 1088K, hence these temperatures for quenching can be regarded as the temperature differences +2K, -88K, -188K, -288K, -388K, -488K, -588K, -688K, -788K, and -888K. Figures 7(a) and 7(b) shows the atom density profiles respectively with heating and quenching at the temperature 1090K. From which it can be found that the structure due to quenching is different from that due to heating at the temperature 1090K, where the melting region with quenching is apparently larger than that with heating. Comparing the atom density profiles in Fig.7 with those in Fig.5 at the temperature 1100K shows that the interface of melting-crystal does not apparently move because of quenching from 1100K to 1090K. The structure at this temperature in the quenching procedure is greatly similar to that at 1100K. Hence, these imply that there appears no crystal growth if the quenching temperature is higher than the interface melting temperature. Then, will the structures of grain boundaries change when the quenching temperatures are lower than the interface melting temperature?

![](./images/811859116547899395_7.jpg)

Fig.7. The atom density profiles with heating and quenching at the temperature 1090K separately.

![](./images/811859116547899395_8.jpg)

Fig.8. Energy per atom versus time in quenching.

Figure 8 shows that the energy per atom in the simulated cell varies with time at the temperature differences $(\Delta T)$ -88K, -188K, -288K, -388K, -488K, -588K, -688K, and -788K, which correspond respectively to Lines 1 to 8. This figure shows that these energy changes have a common feature that they decrease down to their corresponding constant values. It results from the fact that these atoms in the simulation cell have appeared in the vicinity of their final positions in the crystal as the energy per atom arrives at an equilibrium value. The falling stages of these lines correspond to the period of crystal growth, and the stable stages imply that the growth from up_and down_crystals is ended. Figure 9 clearly clarifies the dependence of the time steps of crystal growth ending on the temperature differences. This figure illustrates that as the temperature difference increases from -88K to -788K, the time of crystal growth ending decreases. The time step of crystal growth ending is obtained by the turning point of each line from the falling stage to stable stage in Fig.8.

![](./images/811859116547899395_9.jpg)

Fig.9. Time of reaching the equilibrium versus temperature difference.

Figure 10 provides a visual insight into growth from crystal to melting at the temperature difference -788K (or the quenching temperature 300K correspondingly) by use of the instantaneous atom projection of grain boundary at the time steps 100, 6000 and 12000 steps.

![](./images/811859116547899395_10.jpg)

Fig.10. The projections of atom configuration on $X$-$Y$ plane of the constructed GB with quenching at the temperature 300K at different time steps: 100 (a), 6000 (b), 12000 (c).

Figure 11 shows the atom density profiles at the temperatures 1000K, 900K, 800K, 500K, and 300K, where Figs.11(a1-a5) and Figs.11(b1-b5) respectively correspond to the atom density profiles with heating and quenching at these temperatures. The profiles in Figs.11(b1-b4) with quenching indicate that at these temperatures the structure changes are slightly different from those of Figs.11(a1-a4) with heating. However at the temperature 300K, the central peak of the atom density profile with quenching, apparently decreases compared with that with heating as shown in Figs.11(b5) and 11(a5). Therefore this implies that the grain boundary structures can be largely changed if the temperature is abruptly falls down to quite a low temperature by quenching. In addition, these figures show that the central peaks of atom density profiles with quenching, corresponding to the grain boundary region, sometimes are not located at these original positions with heating at these temperatures. It suggests that the growth rates of crystal-liquid interfaces at up_crystal and down_crystal cannot always remain the same values. If the growth rate of crystal-liquid interface at down_crystal is larger than that at up_crystal, the grain boundary region will lie by the side of up_crystal as shown in Fig.11(b2).

![](./images/811859116547899395_11.jpg)

Fig.11. The atom density profiles with heating and quenching at the temperatures 1000K,
900K, 800K, 500K, and 300K respectively.

### 4. Conclusions

In this paper, we have performed atomic simulations of structural changes due to quenching the melting interface of a Cu $\Sigma5(310)/[001]$ symmetrical tilt grain boundary. The melting interface is obtained by increasing the temperature to a temperature significantly below the bulk melting point of copper, and then it is quenched to different temperatures. The atom density profiles as a function of temperature are studied. The atom density profiles in the GB regions are shown apparently to be different from those near the regions with ordered structure, hence they provide an effective means to demonstrate the existence of GB.

As the quenching temperature is higher than the interface melting temperature, the quenching procedure has little influence on the structures of grain boundaries. Nevertheless, as the quenching temperature is lower than the interface melting temperature, there exists crystal growth from bulk crystal to the melting, and the temperature difference has a great influence on these resulting structures of grain boundaries. As the temperature difference is not very large, the resulting GB structure with quenching is greatly similar to that with heating at the same temperature. But as the temperature difference is quite large, the GB structure greatly changes with quenching. In addition, the growth rates of up_crystal and down_crystal may be different, and it can result in changing the position of the GB with quenching.

---

### References

[1] Gutierrez G, Kiwi M and Ramirez R 1996 *Phys. Rev. B* **54** 11701

[2] Sorensen M. R, Mishin Y and Voter A F 2000 *Phys. Rev. B* **62** 3658

[3] Merkle K L, Thompson L J and Phillipp F 2002 *Phys. Rev. Lett.* **88** 225501

[4] Creuze J, Berthier F, Tetot R and Legrand B 2001 *Phys. Rev. Lett.* **86** 5735

[5] Ashkenazy Y, Averback R S and Albe K 2001 *Phys. Rev. B* **64** 205409

[6] Swygenhoven H V and Derlet P M 2001 *Phys. Rev. B* **64** 224105

[7] Ballo P and Slugen V 2001 *Phys. Rev. B* **65** 012107

[8] Ballo P, Kioussis N and Lu G 2001 *Phys. Rev. B* **64** 024104

[9] Swygenhoven H. V, Farkas D and Caro A 2000 *Phys. Rev. B* **62** 831

[10] Keblinski P, Phillpot S R, Wolf D and Gleiter H 1997 *Acta Mater.* **45** 987

[11] Qiao Y H and Wang S Q 2005 *Acta Phys. Sin.* **54** 4827

[12] Zheng L B and Wang C Y 2005 *Acta Phys. Sin.* **54** 527

[13] Zhang J M, Wei X W and Xing H 2005 *Chin. Phys.* **14** 1015

[14] Wang D, Zhou F X and Liu Y W 2002 *Chin. Phys.* **11** 139

[15] Liu Z J, Cheng X L, Zhang H and Cai L C 2004 *Chin. Phys.* **13** 384

[16] Dai Y B, Shen H S, Zhang Z M, He X X, Hu X J and Shun F H 2001 *Acta Phys. Sin.* **50** 244

[17] Tu X W and Yi Z 2001 *Acta Phys. Sin.* **50** 2439

[18] Zhang L, Wang S Q and Ye H Q 2004 *Acta Phys. Sin.* **53** 2497

[19] Chan S W, Liu J S and Balluffi R W 1985 *Script. Metall.* **19** 1251

[20] Balluffi R W and Maurer R 1988 *Script. Metall.* **22** 709

[21] Fan W, He Y and Gong X G 1999 *Phil. Mag. A* **79** 1321

[22] Keblinsk P, Wolf D, Phillpot S R and Gleiter H 1999 *Phil. Mag. A* **79** 2735

[23] Deymier P, Taiwo A and Kalonji G 1987 *Acta. Metall.* **35** 2719

[24] Nguyen T, Ho P S, Kwok T, Nitta C and Yip S 1986 *Phys. Rev. Lett.* **57** 1919

[25] Demianczuk D W and Aust K T 1975 *Acta Metall.* **23** 1149

[26] Keblinsk P, Phillpot S R, Wolf D and Gleiter H 1997 *Phys. Rev. Lett.* **77** 2965

[27] Keblinsk P, Phillpot S R, Wolf D and Gleiter H 1997 *Phil. Mag. Lett.* **76** 143

[28] Zhao S J, Cheng D Y, Wang S Q and Ye H Q 2001 *J. Phys. Soc. Jpn.* **70** 733

[29] Kutsk J F, Wolf D, Yip S, Phillpot S R and Nguyen T 1998 *Phys. Rev. B* **36** 11572

[30] Parrinello M and Rahman A 1981 *J. Appl. Phys.* **52** 7182

[31] Mei J, Davenport J W and Fernado G W 1991 *Phys. Rev. B* **43** 4653

[32] Chen K Y, Liu H B, Li X P, Han Q Y and Hu Z Q 1995 *J. Phys C: Solid State Phys.* **7** 2397
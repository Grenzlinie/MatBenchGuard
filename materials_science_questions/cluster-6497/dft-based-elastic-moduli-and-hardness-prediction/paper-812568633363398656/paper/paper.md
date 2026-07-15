# Insight into Phase Stability in the Mg-Pd System: The Ab Initio Calculations

Wojciech Gierlotka¹ · Adam Dębski² · Sylwia Terlicka² · Władysław Gąsior² · Magda Pęska³ · Marek Polański³

Submitted: 8 June 2020/in revised form: 2 July 2020
© ASM International 2020

**Abstract** Thermodynamic properties of all reported up to date intermetallic phases in Mg-Pd equilibrium system are reported in this work. Ab initio method was applied to calculate formation energies, relaxed lattice constants and bulk moduli. The consistent set of data was obtained, including formation energies and bulk moduli of Mg₆Pd and Mg₉Pd₁₁ that were calculated for the first time. The obtained energies of formation can be used for future thermodynamic optimization of promising hydrogen storage material Mg-Pd.

**Keywords** ab initio calculations · intermetallics · magnesium alloys · thermodynamics

## 1 Introduction

Hydrogen is still considered as a fuel of the future, but its practical application requires effective storage, detection and catalysts for its splitting in fuel cells. By these reasons, the mechanisms of its interaction with different materials, including precious metals and their alloys, are still being investigated to find cheaper and more effective substitutes for materials currently applied in hydrogen technology. Magnesium palladium alloys are within the interest of researchers due to their well-known ability to interact with hydrogen¹¹ being in the same time cheaper than pure palladium or platinum. Unfortunately, a phase diagram of the Mg-Pd system that is necessary for understanding of phase stability, phase equilibrium, and phase transformations does not have a mathematical model yet due to the lack of thermodynamic information that is necessary for numerical modeling. In order to fill that gap, it was decided to calculate formation energies of all intermetallic compounds (IMC) reported in literature of Mg-Pd system² using Density Functional Theory (DFT).³

## 2 Technique

The calculations were done by ab initio method within the DFT that was implemented in Quantum Espresso.⁴ The calculation used General Gradient Approximation pseudopotential functional parameterized by Padrew, Burke, and Ernzerhof revised for solids approach (GGA BPESol).⁵

For all the calculation cut-off energies and k-point distance were set to 680 eV and 0.20 1/Å, respectively. Before performing the final calculation, the convergence test with respect to cut-off energy and k-point density was done. The structures of all phases were taken from the Crystallography Open Database.⁶ During the calculation, structures were fully relaxed using Broyden-Fletcher-Goldfarb-Shanno (BFGS) algorithm with the convergence threshold equal 0.5 kbar. The energies obtained by self-consistent-field (scf) calculations were used for deriving of IMCs formation energies using the following equation:

---

⊡ Wojciech Gierlotka
wojtek@gms.ndhu.edu.tw

¹ Materials Science and Engineering Department, National Dong Hwa University, Hualien, Taiwan
² Institute of Metallurgy and Materials Science, Polish Academy of Sciences, 25 Reymonta Street, 30-059 Kraków, Poland
³ Military University of Technology, 2 Kaliskiego Street, 00-908 Warsaw, Poland

<br>

![](./images/812568633363398656_1.jpg)
![](./images/812568633363398656_2.jpg)

$$
\Delta E^{0}=\left(E_{\mathrm{Mg}_{n} \mathrm{Pd}_{m}}^{0}-m E_{\mathrm{Pd}}^{0}-n E_{\mathrm{Mg}}^{0}\right) /(m+n) \qquad (\text{Eq 1})
$$

where $\Delta E^{0}$ is a formation energy per atom, $E_{\mathrm{Mg}_{n} \mathrm{Pd}_{m}}^{0}$ is the energy of phase, $E_{\mathrm{Mg}}^{0}$ and $E_{\mathrm{Pd}}^{0}$ are energies of Mg in $R \overline{3} m$ and Pd in $F m \overline{3} m$, respectively, $n$ and $m$ are the numbers of atoms Mg and Pd, respectively.

The bulk modulus was calculated based on the pressure and volume obtained in the SCF calculations, according to the Eq 2:

$$
K=-V \frac{\mathrm{d} P}{\mathrm{~d} V} \qquad (\text{Eq 2})
$$

where K is a bulk modulus, V is volume, dP/dV is a derivative of pressure with respect to volume.

## 3 Results

First, the ab initio energies of pure elements were calculated. Since the absolute values of ab initio energies have no physical meaning, their values are omitted. In addition, the bulk moduli were calculated and the obtained values were equal to 35.9 GPa for Mg and 169.1 GPa for Pd. The calculation reveals that $R \overline{3} m$ structure of Mg has $-0.0367$ eV/atom more negative energy than the $P 63 /$ $m m c$ at 0 K, therefore $R \overline{3} m$ was used as a reference state for magnesium in all calculations. Relaxed lattice constants of $R \overline{3} m$ cell were equal $\mathrm{a}=\mathrm{b}=\mathrm{c}=7.9734 \AA$ with the angles $\alpha=\beta=\gamma=23.086^{\circ}$. The comparison of this result with literature data $^{[7]}$ $\mathrm{a}=\mathrm{b}=\mathrm{c}=7.8639 \AA$ and $\alpha=\beta=\gamma=23.562^{\circ}$ shows that distances between atoms obtained in this work are slightly bigger than in $^{[7]}$ with a bit smaller values of angles between crystallographic vectors in the same time.

The calculated primitive cell vectors of Pd in $F m \overline{3} m$ are equal to $\mathrm{a}=\mathrm{b}=\mathrm{c}=2.7394 \AA$ what is slightly less than the value reported in Materials Project $^{[7]}$ (2.7954 $\AA$).

Having calculated energies of pure elements, as well as, energies of IMCs it was possible to determine formation energies and bulk moduli according to Eq. 1 and 2, respectively. Obtained values of these properties along with relaxed lattice constants and available literature data are gathered in Table 1. Due to the limited space of the paper, the detailed discussion will be made on $\mathrm{Mg}_{6} \mathrm{Pd}$ and $\mathrm{Mg}_{9} \mathrm{Pd}_{11}$ phases, because only these phases show mixed occupation on some Wyckoff positions what made the calculations more complicated. Other intermediate phases included in this work do not exhibit mixed occupation and all the necessary information can be easily read from Table 1.

The $\mathrm{Mg}_{6} \mathrm{Pd}$ phase belongs to complex $\mathrm{A}_{6} \mathrm{~B}$ structure that is recognized as quasicrystal $^{[8]}$ The conventional cell of this phase includes 396 atoms arranged within $F m \overline{3} m$ symmetry. According to Samson, $^{[9]}$ the Wyckoff position 16(e) is occupied by Mg in 51% and by Pd in 49%; therefore, it was necessary to use a special technique to obtain randomly occupied position 16(e). To do it, the Supercell code $^{[10]}$ was used to get all possible permutations of the mentioned occupations, and next the GULP $^{[11]}$ code was applied for choosing the most probable occupation according to the special quasirandom structure (SQS) theory. $^{[12]}$ The occupation reported by Samson $^{[9]}$ gives composition of $\mathrm{Mg}_{6} \mathrm{Pd}$ phase equal to 0.14 mol fraction of Pd. The nonstoichiometry reported in phase diagram $^{[2]}$ at room temperature can be explained by thermal triggered mixing of atoms on different sublattices. Calculated energy of formation is equal $-0.254$ eV/atom and relaxed crystal lattice is determined as $19.968 \AA$ what is slightly less than $20.108 \AA$ reported by Samson. $^{[9]}$ In addition, a bulk modulus was calculated and the result is equal to 58.0 GPa. Since the energy of formation and bulk modulus of the $\mathrm{Mg}_{6} \mathrm{Pd}$ was not calculated before, it is impossible to compare results obtained in this work with calculation reported in literature. However, Delsante et al. $^{[13]}$ reported high temperature direct reaction calorimetry (HTDRC) measurement of $\mathrm{Mg}_{6} \mathrm{Pd}$ heat formation equal to $-0.27 \pm 0.013$ at 300 K and composition $\mathrm{x}(\mathrm{Pd})=0.15$ in a first measurement, and $-0.29 \pm 0.01$ eV at 300 K and composition $\mathrm{x}(\mathrm{Pd})=0.16$ in a second measurement. Despite different composition and higher temperature the results obtained in this work agrees well with measured value.

The crystal structure of $\mathrm{Mg}_{9} \mathrm{Pd}_{11}$ phase was experimentally determined by Kripyakevich and Gladyshevskii $^{[14]}$ as $P 4 / m m m$. According to their determination, Wyckoff positions 1(a) and 1(c) are occupied by Pd and Mg in a ratio 1/9. The cell used for calculation contained 20 atoms and occupation of 1(a) and 1(c) positions were determined within SQS approach. $^{[12]}$ Calculated lattice constants are equal $\mathrm{a}=\mathrm{b}=4.2110 \AA$ and $\mathrm{c}=3.4749 \AA$ what shows more elongated unit cell compared to $\mathrm{a}=$ $\mathrm{b}=4.2799 \AA$ and $\mathrm{c}=3.4199 \AA$ reported by Kripyakevich and Gladyshevskii. $^{[14]}$ The calculated energy of formation is equal to $-0.6778$ eV/atom. This value cannot be compared with literature data because the energy of the formation of $\mathrm{Mg}_{9} \mathrm{Pd}_{11}$ phase was not reported before. The bulk modulus determined in this work was found to be equal to 114.8 GPa.

As it was written before, Table 1 collects experimental and theoretical data on phases in the Mg-Pd system. Its analysis allows for some general conclusions:

![](./images/812568633363398656_3.jpg)

<table><caption>Table 1 Results obtained in this work compared with literature data</caption>
<thead>
<tr>
<th>Phase</th>
<th>Structure</th>
<th>Formation energy at 0 K, eV/atom</th>
<th>a, Å</th>
<th>B, Å</th>
<th>c, Å</th>
<th>Bulk modulus, GPa</th>
<th>Reference</th>
</tr>
</thead>
<tbody>
<tr>
<td>Mg</td>
<td>$R\overline{3}m$</td>
<td>0</td>
<td>7.9734</td>
<td>7.9734</td>
<td>7.9734</td>
<td>35.9</td>
<td>This work</td>
</tr>
<tr>
<td></td>
<td></td>
<td>0</td>
<td>7.8639</td>
<td>7.8639</td>
<td>7.8639</td>
<td>…</td>
<td>[7]calc.</td>
</tr>
<tr>
<td>Pd</td>
<td>$Fm\overline{3}m$</td>
<td>0</td>
<td>2.7394</td>
<td>2.7394</td>
<td>2.7394</td>
<td>169.1</td>
<td>This work</td>
</tr>
<tr>
<td></td>
<td></td>
<td>0</td>
<td>2.7954</td>
<td>2.7954</td>
<td>2.7954</td>
<td>160.0</td>
<td>[7]calc.</td>
</tr>
<tr>
<td>Mg₆Pd</td>
<td>$Fm\overline{3}m$</td>
<td>− 0.254</td>
<td>19.968</td>
<td>19.968</td>
<td>19.968</td>
<td>58.0</td>
<td>This work</td>
</tr>
<tr>
<td></td>
<td></td>
<td>…</td>
<td>20.108</td>
<td>20.108</td>
<td>20.108</td>
<td>…</td>
<td>[9]exp.</td>
</tr>
<tr>
<td></td>
<td></td>
<td>− 0.22</td>
<td>…</td>
<td>…</td>
<td>…</td>
<td>…</td>
<td>[19]Miedema</td>
</tr>
<tr>
<td>Mg₃Pd</td>
<td>$P6_{3}cm$</td>
<td>− 0.414</td>
<td>7.9136</td>
<td>7.9136</td>
<td>8.3638</td>
<td>59.7</td>
<td>This work</td>
</tr>
<tr>
<td></td>
<td></td>
<td>− 0.430</td>
<td>8.042</td>
<td>8.042</td>
<td>8.410</td>
<td>59.0</td>
<td>[7]calc.</td>
</tr>
<tr>
<td></td>
<td></td>
<td>− 0.434</td>
<td>…</td>
<td>…</td>
<td>…</td>
<td>…</td>
<td>[15]calc.</td>
</tr>
<tr>
<td></td>
<td></td>
<td>− 0.438</td>
<td>…</td>
<td>…</td>
<td>…</td>
<td>…</td>
<td>[16]calc.</td>
</tr>
<tr>
<td></td>
<td></td>
<td>…</td>
<td>7.987</td>
<td>7.987</td>
<td>8.422</td>
<td>…</td>
<td>[20]exp.</td>
</tr>
<tr>
<td></td>
<td></td>
<td>− 0.4</td>
<td>…</td>
<td>…</td>
<td>…</td>
<td>…</td>
<td>[19]Miedema</td>
</tr>
<tr>
<td>Mg₅Pd₂</td>
<td>$P63/mmc$</td>
<td>− 0.4642</td>
<td>8.614</td>
<td>8.614</td>
<td>8.1364</td>
<td>62.6</td>
<td>This work</td>
</tr>
<tr>
<td></td>
<td></td>
<td>− 0.481</td>
<td>8.713</td>
<td>8.713</td>
<td>8.233</td>
<td>62.0</td>
<td>[7]calc.</td>
</tr>
<tr>
<td></td>
<td></td>
<td>− 0.490</td>
<td>…</td>
<td>…</td>
<td>…</td>
<td>…</td>
<td>[16]calc.</td>
</tr>
<tr>
<td></td>
<td></td>
<td>…</td>
<td>8.671</td>
<td>8.671</td>
<td>8.164</td>
<td>…</td>
<td>[21]exp.</td>
</tr>
<tr>
<td></td>
<td></td>
<td>…</td>
<td>8.644</td>
<td>8.644</td>
<td>8.160</td>
<td>…</td>
<td>[22]exp.</td>
</tr>
<tr>
<td></td>
<td></td>
<td>− 0.456</td>
<td>…</td>
<td>…</td>
<td>…</td>
<td>…</td>
<td>[19]Miedema</td>
</tr>
<tr>
<td>MgPd</td>
<td>$Pm\overline{3}m$</td>
<td>− 0.7088</td>
<td>3.1405</td>
<td>3.1405</td>
<td>3.1405</td>
<td>93.7</td>
<td>This work</td>
</tr>
<tr>
<td></td>
<td></td>
<td>− 0.729</td>
<td>3.189</td>
<td>3.189</td>
<td>3.189</td>
<td>94.0</td>
<td>[7]calc.</td>
</tr>
<tr>
<td></td>
<td></td>
<td>− 0.742</td>
<td>…</td>
<td>…</td>
<td>…</td>
<td>…</td>
<td>[15]calc.</td>
</tr>
<tr>
<td></td>
<td></td>
<td>− 0.747</td>
<td>…</td>
<td>…</td>
<td>…</td>
<td>…</td>
<td>[16]calc.</td>
</tr>
<tr>
<td></td>
<td></td>
<td>− 0.762</td>
<td>…</td>
<td>…</td>
<td>…</td>
<td>98.6</td>
<td>[17]calc.</td>
</tr>
<tr>
<td></td>
<td></td>
<td>…</td>
<td>3.12</td>
<td>3.12</td>
<td>3.12</td>
<td>…</td>
<td>[23]exp.</td>
</tr>
<tr>
<td></td>
<td></td>
<td>…</td>
<td>3.16</td>
<td>3.16</td>
<td>3.16</td>
<td>…</td>
<td>[24]exp.</td>
</tr>
<tr>
<td></td>
<td></td>
<td>− 0.649</td>
<td>…</td>
<td>…</td>
<td>…</td>
<td>…</td>
<td>[19]Miedema</td>
</tr>
<tr>
<td></td>
<td></td>
<td>− 0.6778</td>
<td>4.2110</td>
<td>4.2110</td>
<td>3.4749</td>
<td>114.8</td>
<td>This work</td>
</tr>
<tr>
<td>Mg₉Pd₁₁</td>
<td>$P4/mmm$</td>
<td>…</td>
<td>4.2799</td>
<td>4.2799</td>
<td>3.4199</td>
<td>…</td>
<td>[14]exp.</td>
</tr>
<tr>
<td></td>
<td></td>
<td>− 0.638</td>
<td>…</td>
<td>…</td>
<td>…</td>
<td>…</td>
<td>[19]Miedema</td>
</tr>
<tr>
<td></td>
<td></td>
<td>− 0.6202</td>
<td>5.4378</td>
<td>10.6638</td>
<td>4.1722</td>
<td>110.8</td>
<td>This work</td>
</tr>
<tr>
<td>Mg₃Pd₅</td>
<td>$Pbam$</td>
<td>− 0.651</td>
<td>5.516</td>
<td>10.594</td>
<td>4.347</td>
<td>…</td>
<td>[7]calc.</td>
</tr>
<tr>
<td></td>
<td></td>
<td>− 0.652</td>
<td>…</td>
<td>…</td>
<td>…</td>
<td>…</td>
<td>[15]calc.</td>
</tr>
<tr>
<td></td>
<td></td>
<td>…</td>
<td>5.427</td>
<td>10.588</td>
<td>4.1304</td>
<td>…</td>
<td>[25]exp.</td>
</tr>
<tr>
<td></td>
<td></td>
<td>− 0.579</td>
<td>…</td>
<td>…</td>
<td>…</td>
<td>…</td>
<td>[19]Miedema</td>
</tr>
</tbody>
</table>

![](./images/812568633363398656_4.jpg)

**Table 1 continued**

<table>
  <thead>
    <tr>
      <th>Phase</th>
      <th>Structure</th>
      <th>Formation energy at 0 K, eV/atom</th>
      <th>a, Å</th>
      <th>B, Å</th>
      <th>c, Å</th>
      <th>Bulk modulus, GPa</th>
      <th>Reference</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="8">MgPd₂</td>
      <td rowspan="8">Pnma</td>
      <td>− 0.5802</td>
      <td>5.4545</td>
      <td>4.0815</td>
      <td>8.11262</td>
      <td>119.9</td>
      <td>This work</td>
    </tr>
    <tr>
      <td>− 0.607</td>
      <td>5.526</td>
      <td>4.194</td>
      <td>8.194</td>
      <td>115.0</td>
      <td>[7] calc.</td>
    </tr>
    <tr>
      <td>− 0.610</td>
      <td>…</td>
      <td>…</td>
      <td>…</td>
      <td>…</td>
      <td>[15] calc.</td>
    </tr>
    <tr>
      <td>− 0.613</td>
      <td>…</td>
      <td>…</td>
      <td>…</td>
      <td>…</td>
      <td>[16] calc.</td>
    </tr>
    <tr>
      <td>− 0.627</td>
      <td>…</td>
      <td>4.1673</td>
      <td>8.0129</td>
      <td>121.64</td>
      <td>[17] calc.</td>
    </tr>
    <tr>
      <td>…</td>
      <td>5.4421</td>
      <td>…</td>
      <td>…</td>
      <td>…</td>
      <td>[25] exp.</td>
    </tr>
    <tr>
      <td>− 0.529</td>
      <td>…</td>
      <td>3.9053</td>
      <td>…</td>
      <td>…</td>
      <td>[19] Miedema</td>
    </tr>
    <tr>
      <td>− 0.4724</td>
      <td>3.9053</td>
      <td>3.977</td>
      <td>15.6214</td>
      <td>130.2</td>
      <td>This work</td>
    </tr>
    <tr>
      <td rowspan="6">MgPd₃</td>
      <td rowspan="6">I4/mmm</td>
      <td>− 0.491</td>
      <td>3.977</td>
      <td>3.977</td>
      <td>15.897</td>
      <td>130.0</td>
      <td>[7] calc.</td>
    </tr>
    <tr>
      <td>− 0.493</td>
      <td>…</td>
      <td>…</td>
      <td>…</td>
      <td>…</td>
      <td>[16] calc.</td>
    </tr>
    <tr>
      <td>…</td>
      <td>…</td>
      <td>…</td>
      <td>15.6527</td>
      <td>…</td>
      <td>[25] exp.</td>
    </tr>
    <tr>
      <td>− 0.406</td>
      <td>3.92263</td>
      <td>3.92263</td>
      <td>…</td>
      <td>…</td>
      <td>[19] Miedema</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>…</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>…</td>
      <td></td>
    </tr>
  </tbody>
</table>

1.  For the first time energies of formation and bulk moduli were calculated for Mg₆Pd and Mg₉Pd₁₁ phases.

2.  Obtained energies of formation are slightly less negative than can be found in Materials Project⁽⁷⁾, AFLOW⁽¹⁵⁾, and OQMD⁽¹⁶⁾ databases.

3.  Lattice constants calculated in this work show better agreement with experimental data than those listed in Materials Project⁽⁷⁾ database.

The difference between the results of calculations achieved in this work and reported in databases⁽⁷,¹⁵,¹⁶⁾ is likely caused by application of difference pseudopotentials. In a case of this work, the GGA PBESol pseudopotentials were used. In contrast, the information provided in⁽⁷,¹⁵,¹⁶⁾ shows that the GGA without revision for solids pseudopotentials were used.

The formation energies of IMCs in Mg-Pd system are shown in the form of a convex hull in Fig. 1. One can observe that all the energies are located on the hull, which indicates the stability of the compounds at 0 K. The same figure displays formation energies found in Materials Project,⁽⁷⁾ AFLOW,⁽¹⁵⁾ OQMD,⁽¹⁶⁾ and JARVIS⁽¹⁷⁾ databases that are a bit lower in comparison to these determined in this study. For a sake of curiosity, the energies of formation for all IMCs were also calculated using Miedema's model.⁽¹⁸,¹⁹⁾ The results of these calculations were placed along with other⁽⁷,¹⁵,¹⁶⁾ in Table 1. It can be easily seen that formation energies estimated from Miedema's model⁽¹⁸⁾ are less negative than determined from ab initio method. It can be also seen that the discrepancy between ab initio calculations and estimations increases with increasing concentration of palladium.

![](./images/812568633363398656_5.jpg)

Fig. 1 Convex hull obtained in this work at 0 K. Literature information from Materials Project,⁽⁷⁾ AFLOW,⁽¹⁵⁾ OQMD⁽¹⁶⁾, and JARVIS⁽¹⁷⁾ are placed for comparison

![](./images/812568633363398656_6.jpg)

Fig. 2 Calculated bulk moduli superimposed with data collected in Materials Project $^{[17]}$ and JARVIS $^{[17]}$ databases

Figure 2 shows calculated bulk moduli for the IMCs involved in this work, as well as for the pure palladium and magnesium. It is easy to notice that the bulk modulus changes almost lineary with increasing concentration of palladium. However, there are two exceptions from that trend: $Mg_6Pd$ and $Mg_9Pd_{11}$, which bulk moduli are located above the linear trend. Interesting, both intermetallic compounds have mixed occupation on some Wyckoff position what can be explanation of this phenomenon. In the same Fig. 2 the bulk moduli available in Materials Project $^{[7]}$ and JARVIS $^{[17]}$ are placed. It can be easy noticed that calculated bulk moduli for $Mg_3Pd$, $Mg_5Pd_2$, $MgPd$, $MgPd_2$, and Pd shows almost the same values. Therefore, it can be concluded that bulk moduli calculated for Mg, $Mg_6Pd$, $Mg_9Pd_{11}$, $Mg_3Pd_5$ show trustable values.

## 4 Conclusions

A complex ab initio calculations of all phases reported in Mg-Pd phase diagram were done in this work. For the first time formation energies and bulk moduli were calculated for $Mg_6Pd$ and $Mg_9Pd_{11}$ phases. Relaxed lattice constants determined in this work are in very good agreement with experimental data. Formation energies in this study show slightly less negative values compared to those reported in the literature and they can be used for further modeling of the phase equilibria in the Mg-Pd system.

Acknowledgments This work is supported by the National Science Centre, Poland, for funding Project No. 2018/31/B/ST8/01371 in the years 2019-2022. This research was supported in part by PLGrid Infrastructure. The work was supported by Ministry of Science and Technology (Taiwan) under grant no. 109-2221-E259-005.

## References

1. Y. Kume and A. Weiss, On the Interaction of Hydrogen with the Intermetallic Phase Mg6Pd, *J. Less. Common Met.*, 1987, **136**, p 51-54
2. A.A. Nayeb-Hashemi and J.B. Clark, The Mg-Pd (Magnesium- Palladium) System, *Bull. Alloys Phase Diagr.*, 1985, **6**, p 164-167
3. D.S. School and J.A. Steckel, *Density Functional Theory*, Wiley, NJ, 2009
4. P. Giannozzi, S. Baroni, N. Bonini, C.R. Calandra, C. Cavazzoni, D. Ceresoli, G.L. Chiarotti, M. Cococcioni, I. Dabo, A. Dal Corso, S. de Gironcoli, S. Fabris, G. Fratesi, R. Gebauer, U. Gerstmann, C. Gougoussis, A. Kokalj, M. Lazzeri et al., Quantum ESPRESSO: A Modular and Open-Source Software Project for Quantum Simulations of Materials, *J. Phys. Condens. Matter*, 2009, **21**, p 395502
5. J.P. Padrew, K. Burke, and M. Ernzerhof, Generalized Gradient Approximation Made Simple, *Phys. Rev. Lett.*, 1996, **77**, p 3865
6. Crystallography Open Database. (n.d.). Retrieved Oct 20, 2019, from http://www.crystallography.net/cod/
7. Materials Project. (n.d.). Retrieved Oct 20, 2019, from https:// materialsproject.org
8. J.P. Makongo, Y. Prost, U. Burkhardt, R. Niewa, C. Kudla, and G. Kreiner, A Case Study of Complex Metallic Alloy Phase: Structure and Disorder Phenomena of Mg-Pd Compounds, *Phi- los. Mag. Philos. Mag. Lett.*, 2006, **86**, p 427-433
9. S. Samson, Complex Cubic A6B Compounds. II. The Crystal Structure of Mg6Pd, *Acta Cryst.*, 1972, **B28**, p 939-945
10. K. Okhotnikov, T. Charpentier, and S. Cadars, Supercell Pro- gram: A Combinatorial Structure-Generation Approach for the Local-Level Modeling of Atomic Substitutions and Partial Occupancies in Crystals, *J. Cheminform.*, 2016, **8**, p 17
11. J.D. Gale, GULP—A Computer Program for the Symmetry Adapted Simulation of Solids, *JCS Faraday Trans.*, 1997, **93**, p 629
12. A. Zunger, S.-H. Wei, L.G. Ferreira, and J.E. Bernard, Special Quasirandom Structures, *Phys. Rev. Lett.*, 1990, **65**, p 353-356
13. S. Delsante, R. Novakovic, A. Gagliolo, and G. Borzone, Ther- modynamic Investigation on the Mg-Pd Intermetallic Phases, *J. Chem. Thermodyn.*, 2019, **139**, p 1-8
14. P. Kripyakevich and E. Gladyshevskii, Crystal Structures of Some Compounds of Palladium with Magnesium, *Sov. Phys. Crystallogr. Kristallografiya*, 1960, **5**, p 552-554
15. AFLOW Automatic Flow for Materials Design. (n.d.). Retrieved from http://aflowlib.org
16. The Open Quantum Materials Database. (n.d.). Retrieved from http://www.oqmd.org
17. NIST. (n.d.). *JARVIS DFT*. Retrieved June 05, 2020, from https:// www.ctcms.nist.gov/~knc6/JVASP.html
18. F.R. de Broer, R. Boom, W.C. Mattens, A.R. Miedema, and A.K. Niessen, *Cohesion n Metals: Transition Metal Alloys*, North- Holland, Amsterdam, 1983
19. A. Dębski, R. Dębski, and W. Gąsior, *Arch. Metall. Mater.*, 2014, **59**, p 1337-1343
20. J.P. Makongo, C. Kudla, Y. Prots, R. Niewa, U. Burkhardt, and G. Kreiner, Crystal Structure of Trimagnesium Monopalladium, Mg3Pd, *Zeitschrift fur Kristallographie New Cryst. Struct.*, 2005, **220**, p 289-292
21. V. Hlukhyy and R. Poettgen, Ricerche sulle leghe dei metalli nobili con gli elementi piu electropositivi. IV. Le fasi gamma dei sistemi Mg-Rh e Mg-Pd. Atti della Accademia Nazionale dei Lincei, Classe di Scienze Fisiche, Matematiche e Naturali, *Ren- diconti*, 1960, **29**, p 70-73
22. R. Ferro, Ricerche sulle leghe dei metalli nobili con gli elementi piu electropositivi. IV. Le fasi gamma dei sistemi Mg-Rh e Mg-

![](./images/812568633363398656_7.jpg)

Pd, Atti della Accademia Nazionale dei Lincei, Classe di Scienze Fisiche, Matematiche e Naturali, Rendiconti, Serie, 1960, 8(29), p 70-73

23. H. Stadelmaier and W. Hardy, Ternaere Kohlenstofflegierungen von Palladium und Platin mit Mg, Al, Zn, Ga, Ge, Cd, In, Sn, Hg, Tl und Pb, Z. Metallkd., 1961, 52, p 391-396

24. R. Ferro, Research on the Alloys of Noble Metals with the More Electropositive Elements II. Micrographic and Roentgenographic Examination of the Magnesium-Palladium Alloys, J. Less Com- mon Met., 1959, 1, p 424-438

25. C. Wannek and B. Harbrecht, Structure and Thermal Stability of the New Intermetallics MgPd2, MgPd3, and Mg3Pd5 and the Kinetics of the Iodine-Catalyzed Formation of MgPd2, J. Solid State Chem., 2001, 159, p 113-120

**Publisher's Note** Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

![](./images/812568633363398656_8.jpg)
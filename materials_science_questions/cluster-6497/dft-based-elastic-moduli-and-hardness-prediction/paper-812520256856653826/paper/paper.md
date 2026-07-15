ORIGINAL PAPER

# Structural and mechanical properties of antimonene monolayers doped with transition metals: a DFT-based study

Peyman Aghdasi¹ · Shayesteh Yousefi¹ · Reza Ansari¹

Received: 22 August 2020 / Accepted: 8 November 2020 / Published online: 6 January 2021
© Springer-Verlag GmbH Germany, part of Springer Nature 2021

## Abstract
In the current study, the elastic and plastic properties of the $2 \times 2$ and $3 \times 3$ pristine and transition metal (TM)-doped antimonene are studied through DFT calculations. Sc, Ti, V, Cr, Fe, Co, Ni, Cu, and Zn atoms are selected as the doping atoms. It was observed that Young's and bulk moduli of both $2 \times 2$ and $3 \times 3$ pristine structure would decrease while affected by the doping atoms. The highest reduction in the Young's and bulk moduli of the $2 \times 2$ nanosheets has occurred in the Cr- and Ti-doped structures, respectively, while the same reduction was observed in the V- and Ti-doped structures in the $3 \times 3$ nanosheets. In addition, it was shown that all of the investigated structures express isotropic behavior since the obtained Young's moduli of these nanostructures have negligible difference along armchair and zigzag directions. Finally, the loading is further increased to investigate the plastic behavior of these structures. The results showed that except for $2 \times 2$ Sc-doped structure under biaxial loading, the yield strain of all doped nanosheets would decrease under uniaxial and biaxial loadings. The highest reduction in the yield strain of the $2 \times 2$ nanosheets under biaxial loading has been observed in Cu-doped nanosheet while in $3 \times 3$ nanosheets, the highest reduction has occurred in Cu-, Fe-, and Zn-doped nanosheets under the same condition. As for the yield strain of the doped $2 \times 2$ nanosheets while affected by the uniaxial loading, Cu- and Zn-doped nanosheets experienced the highest reduction while in $3 \times 3$ nanosheets, the highest reduction has been observed for Cr-doped nanosheet under the same condition.

Keywords Density functional theory · Antimonene · Atomic doping · 2D material

## Introduction
The outstanding properties and use of two-dimensional (2D) materials have attracted a great deal of attention during the recent years [1–3]. One of the most popular 2D structure material, which is an ideal carrier for composite materials due to its great chemical stability, high surface area, perfect thermal conductivity, and unique quantum Hall effect, is graphene [4, 5]. However, graphene has its limitation when used in electronic and optoelectronic devices because of its zero band gap [6]. After graphene, experimentalists and theoreticians started to search for other low-dimensional materials with outstanding properties such as phosphorene [7, 8], arsenene [9, 10], bismuthene [11, 12], antimonene [13], silicene [14–16], and germanene [17] to be used as an alternative of graphene. In the recent years, the interest in the group V elemental monolayers has increased drastically after the successful experimental fabrication of black phosphorus [7], which was predicted as an ideal candidate to be used in nano-electronics and nano-photonics due to its excellent charge-carrier mobility and current on/off ratios. However, it was later discovered that the black phosphorus could not be developed for real applications due to its instability [18–21]. On the contrary, antimonene, which is the monolayer of antimony and is also from the group V of periodic table, was proven to be stable under ambient conditions with the band gap of 1.8–2.4 eV. In addition to the isolation of antimonene by both liquid phase [22] and mechanical exfoliation [23], theoretical studies predicted that antimonene has outstanding physical properties such as strain-induced band transition [24], high thermal conductivity [13], and carrier mobility [25] compared to other materials. Hence, antimonene could be introduced as a fitting candidate for optoelectronic applications [26, 27], energy storage and conversion [28], spintronics [29], biomedicine [30], and high-performance sensors [31].

![Reza Ansari](./images/812520256856653826_1.jpg)
Reza Ansari
r_ansari@guilan.ac.ir

¹ Faculty of Mechanical Engineering, University of Guilan,
P.O. Box 3756, Rasht, Iran

![](./images/812520256856653826_2.jpg)

Nagarajan et al. [32] investigated the electronic properties of zigzag and armchair antimonene nanotubes and nanoribbons while affected by the hydrogenation along their boundaries by employing DFT calculations. In addition to confirming the structural stability of antimonene by computing the formation energy, they indicated that these properties could be changed and used as chemical sensor and for spintronic devices by modifying the width, orientation of the edges, and passivation with hydrogen. Moreover, phonon transport property of $\beta$-phase antimonene was investigated by Wang et al. [33] through employing $ab$ $initio$ calculations combined with Boltzmann transport equation (BTE) formalism. Their findings showed that at a temperature of 300 K, antimonene would have a low lattice thermal conductivity (15.1 W/mK), which is due to the large buckling height, low Debye temperature, and small group velocities of antimonene. In addition to mono-elemental structures, hetero-elemental motifs of antimonene have also been attracted much attention in recent years. Among these are Van-der Waals heterobilayers, binary compounds, adsorbed nanosheets, and doped (decorated) structures. Especially, important studies have been conducted on TM-doped antimonene, suggesting very interesting electronic and magnetic properties. For instance, using spin-polarized first-principles calculations, Yang et al. [29] studied the electronic and magnetic properties of TM-doped antimonene as well as their geometric structure. They indicated that while covalent bond exists between Sb atoms, the TM atoms would exhibit strong orbital hybridization with Sb atoms. Moreover, doping Ti, V, and Mn atoms causes half-metallic states in antimonene while doping Cr atom would result in a spin-polarized semiconducting state. They predicted that the doped structures that exhibit half-metallic characters with high spin polarization would have the potential to be used in spintronics. Using molecular beam, epitaxy, Niu et al. [34] investigated the direct synthesis of high-quality antimonene, on dielectric copper oxide substrate. Their tunneling microscopy imaging showed a segregation growth process on Cu3O2/Cu(111), and strain-modulated band structures have been demonstrated by first-principles calculations. Adsorption of CO2 and NH3 gas molecules on armchair and zigzag antimonene nanoribbons has been examined by Srivastava et al. [35] using first-principles calculations. They predicted that by modifying the structural and electronic properties of antimonene nanoribbons, the adsorption of CO2 and NH3 gas molecules could be sensed. Hu et al. [36] utilized first-principles calculations to tune the energy band structure of antimonene with an electrochemical sodium-doping strategy. They demonstrated that in 5.55% Na-doped antimonene, a direct band gap of 0.88 eV could be formed while pristine antimonene had the indirect band gap of 2.38 eV. The effects of fluorination on antimonene have been investigated by Zhang et al. [37] through both first-principles calculation and ionic liquid-assisted electrochemical exfoliation. It was shown that fluorinated antimonene could be used as saturable absorber, and unlike antimonene, fluorinated antimonene has a direct band gap which indicates the potential of fluorinated antimonene to be used as optical devices. Ersan et al. [38] performed first-principles calculations based on the density functional theory to study 2D single-layer structures based on P, As, Sb, and Bi elements, consisting of buckled square and octagon rings. It was shown that these structures are dynamically and thermally stable and suitable for applications at room temperature and higher temperature. They proved this stability by extensive analysis of the mechanical properties, vibration frequencies, and finite temperature through $ab$ $initio$ molecular dynamics. In addition, they demonstrated that all these structures are semiconductors with a fundamental band gap, which is wide for P but this band gap decreases with increasing the row number of the periodic table. The effect of the spin-orbit coupling decreases the band gap and is also found to be crucial for Sb and Bi. Kripalani et al. [39] investigated the mechanical and electronic properties of monolayer antimonene in its most stable $\beta$-phase using first-principles calculations. They stated that the upper region of antimonene valence band solely consists of one pair p-orbital states, which are by nature more delocalized than the d-orbital states in transition metal dichalcogenides. Young's and shear moduli of $\beta$-antimonene are observed to be ~ 25% higher than those of bulk antimony, while the hexagonal lattice constant of the monolayer reduces significantly (~ 5%) from that in bulk. They also found that the nature of the band gap remains insensitive to strain in the zigzag direction, while strain in the armchair direction activates an indirect-direct band gap transition at a critical strain of 4%, owing to a band switching mechanism. Hu et al. [40] performed $ab$ $initio$ calculations to investigate the geometric and electronic properties of arsenene and antimonene doped by group-VA atoms. They found that the group-VA atom dopings in arsenene and antimonene cause different local deformations. They stated that the introduction of a group-VA atom in freestanding arsenene or antimonene breaks the original symmetry and results in a band gap decrease in electronic band structure. The calculation results of difference charge density revealed that the group-VA atom doping in freestanding arsenene and antimonene inevitably leads to local deformations.

Despite the importance of mechanical properties for better understanding of a novel system, these are not studied for the TM-doped antimonenes yet. Therefore, herein, we investigated the influence of transition metal doping

![](./images/812520256856653826_3.jpg)

![](./images/812520256856653826_4.jpg)

Fig. 1 Schematic atomic positions and unit cell of the (a) top and (b) side view of $2 \times 2$ doped antimonene and (c) top and (d) side view of $3 \times 3$ doped antimonene

on the structural and mechanical properties, such as Young's and bulk moduli, as well as the plastic behavior of $2 \times 2$ and $3 \times 3$ antimonene nanosheets based on DFT calculations. Furthermore, the isotropic behavior of these nanosheets is examined through comparison between the obtained in-plane Young's moduli in longitudinal and transverse directions.

## Simulation details

In the current study, first-principle DFT calculations is employed through Spanish Initiative for Electronic Simulations with Thousands of Atoms (SIESTA) [41, 42] code in order to investigate the structural and mechanical properties of $2 \times 2$ and $3 \times 3$ pristine and transition metal-doped antimonene. In order to treat correlation effects and perform geometrical optimizations, we performed generalized gradient approximation (GGA) function as defined by Perdew-Burke-Ernzerhof (PBE) [43]. In the overall procedure, double-$\zeta$ plus polarization orbitals (DZP) has been selected for the atomic orbital basis sets with an energy shift of 50 meV along with the split norm of 0.3 and the atomic positions were relaxed until the time that the residual forces on any atom were less than $0.015\ \text{eVA}^{-1}$. The density functional theory requires approximations for the exchange-correlation (xc) energy as a functional of the density. The simplest approximations are the local density approximation (LDA) and the local spin density (LSD) approximation, which employ the xc energy of the uniform electron gas (both spin-unpolarized and spin-polarized types) as an input. Generalized gradient approximations (GGA) go beyond the LDA and LSD descriptions by including density gradients, and improve calculated results significantly [44]. This is the reason why the GGA function is used in the

<table>
<caption>Table 1 Values of bond length (d), bond length of doped atom (d'), and height of doped atom (h) for $2 \times 2$ nanosheets</caption>
<thead>
<tr>
<th>Structure</th>
<th>a (Å)</th>
<th>d (Å)</th>
<th>d' (Å)</th>
<th>h (Å)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Pristine</td>
<td>8.282</td>
<td>2.886–2.887</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>Cr-doped</td>
<td>8.125</td>
<td>2.841–2.906</td>
<td>2.598</td>
<td>1.271</td>
</tr>
<tr>
<td>Cu-doped</td>
<td>8.207</td>
<td>2.841–2.855</td>
<td>2.621</td>
<td>0.762</td>
</tr>
<tr>
<td>Sc-doped</td>
<td>8.206</td>
<td>2.867–2.885</td>
<td>2.882</td>
<td>1.634</td>
</tr>
<tr>
<td>Fe-doped</td>
<td>8.083</td>
<td>2.841–2.894</td>
<td>2.541</td>
<td>1.193</td>
</tr>
<tr>
<td>Ni-doped</td>
<td>8.042</td>
<td>2.832–2.868</td>
<td>2.547</td>
<td>1.155</td>
</tr>
<tr>
<td>V-doped</td>
<td>8.125</td>
<td>2.844–2.889</td>
<td>2.678</td>
<td>1.373</td>
</tr>
<tr>
<td>Zn-doped</td>
<td>8.360</td>
<td>2.858–2.890</td>
<td>2.664</td>
<td>0.559</td>
</tr>
<tr>
<td>Ti-doped</td>
<td>8.132</td>
<td>2.843–2.892</td>
<td>2.753</td>
<td>1.509</td>
</tr>
</tbody>
</table>

<table>
<caption>Table 2 Values of bond length (d), bond length of doped atom (d'), and height of doped atom (h) for $3 \times 3$ nanosheets</caption>
<thead>
<tr>
<th>Structure</th>
<th>a (Å)</th>
<th>d (Å)</th>
<th>d' (Å)</th>
<th>h (Å)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Pristine</td>
<td>12.423</td>
<td>2.886–2.888</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>Cr-doped</td>
<td>12.285</td>
<td>2.866–2.908</td>
<td>2.598</td>
<td>1.233</td>
</tr>
<tr>
<td>Cu-doped</td>
<td>12.187</td>
<td>2.825–2.903</td>
<td>2.599</td>
<td>0.799</td>
</tr>
<tr>
<td>Sc-doped</td>
<td>12.333</td>
<td>2.867–2.897</td>
<td>2.877</td>
<td>1.591</td>
</tr>
<tr>
<td>Fe-doped</td>
<td>12.262</td>
<td>2.863–2.905</td>
<td>2.539</td>
<td>1.161</td>
</tr>
<tr>
<td>Ni-doped</td>
<td>12.212</td>
<td>2.859–2.898</td>
<td>2.548</td>
<td>1.158</td>
</tr>
<tr>
<td>V-doped</td>
<td>12.324</td>
<td>2.871–2.899</td>
<td>2.664</td>
<td>1.287</td>
</tr>
<tr>
<td>Zn-doped</td>
<td>12.406</td>
<td>2.840–2.897</td>
<td>2.646</td>
<td>0.596</td>
</tr>
<tr>
<td>Ti-doped</td>
<td>12.236</td>
<td>2.860–2.881</td>
<td>2.756</td>
<td>1.435</td>
</tr>
</tbody>
</table>

![](./images/812520256856653826_5.jpg)

![](./images/812520256856653826_6.jpg)

Fig. 2 Bond length of doped atom in (a) $2\times2$ and (b) $3\times3$ nanosheets

current work. Furthermore, vacuum widths are considered
17 Å to ensure that interactions between the adjacent im-
ages of the supercell are omitted. Monkhorst-Pack grid for
the k-point sampling of the Brillouin zone was set to $10\times$
$10\times1$ and $7\times7\times1$ for $2\times2$ and $3\times3$ nanosheets, respec-
tively, and the mesh cutoff is considered as 325 $Ry$
and 275 $Ry$ for the mentioned nanosheets, respectively.

# Results and discussion

## Structural and geometrical properties

In the current study, the smallest unit cell obtained in ref
[45], with the lattice constant of 4.14 Å, is used to con-
struct the $2\times2$ and $3\times3$ pristine antimonene nanosheets.
The lattice parameters are obtained 8.28 and 12.42 Å for
the $2\times2$ and $3\times3$ pristine antimonene nanosheets, re-
spectively. The doped nanosheets investigated in this
study are created by substitution of a single transition
metal atom with an antimony atom which results in the
doping percentage of 12.5% (1/8) and 5.55% (1/18) for
the mentioned nanosheets. In Fig. 1, the schematic figures
of $2\times2$ and $3\times3$ doped structures are presented and the
associated parameters are given in Tables 1 and 2 for the
mentioned nanostructures, respectively. The results
showed that the lowest Sb-Sb bond length is associated
to the antimony atoms that are connected to the three
atoms surrounding the doped atom. Figure 2 is also added
to better visualize the changes in the bond length of doped
atom (d') in $2\times2$ and $3\times3$ structures. According to this
figure, the bond length decreases from Sc to Fe, the bond
length decreases from 2.621 (Sc) to 2.541 Å (Fe), and
then it goes up from 2.541 (Fe) to 2.678 Å (V) in $2\times2$
nanosheets. Similarly, in $3\times3$ nanosheets, the bond
length decreases from 2.877 (Sc) to 2.539 Å (Fe), then
it goes up from 2.539 (Fe) to 2.548 Å (Ni).

## In-plane Young's modulus

In order to calculate the Young's moduli $(Y_s)$ of the pris-
tine and doped structures, uniaxial compressive and ten-
sile loadings are applied to the unit cell (see Fig. 3) be-
tween the range of $-5$ and 5% with paces of 1%. When

![](./images/812520256856653826_7.jpg)

Fig. 3 Schematic view of the unit cell subjected to (a) biaxial, (b) longitudinal uniaxial, and (c) transverse uniaxial loadings

![](./images/812520256856653826_8.jpg)

![](./images/812520256856653826_9.jpg)

Fig. 4 Strain energy of the $2 \times 2$ pristine and doped antimonene against the longitudinal uniaxial loading

![](./images/812520256856653826_10.jpg)

![](./images/812520256856653826_11.jpg)

Fig. 5 Strain energy of the $3 \times 3$ pristine and doped antimonene against the longitudinal uniaxial loading

![](./images/812520256856653826_12.jpg)

![](./images/812520256856653826_13.jpg)

Fig. 6 Strain energy of the $2\times2$ pristine and doped antimonene against the transverse uniaxial loading

![](./images/812520256856653826_14.jpg)

Fig. 7 Strain energy of the $3 \times 3$ pristine and doped antimonene against the transverse uniaxial loading

![](./images/812520256856653826_15.jpg)

Table 3 Young's modulus of the
2 × 2 pristine and doped
antimonene along the
longitudinal and transverse
directions

<table>
<thead>
<tr>
<th>Structure</th>
<th>Longitudinal Young's modulus (N/m)</th>
<th>Reduction percentage (%)</th>
<th>Transverse Young's modulus (N/m)</th>
<th>Reduction percentage (%)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Pristine</td>
<td>41.54</td>
<td>-------</td>
<td>41.55</td>
<td>-------</td>
</tr>
<tr>
<td>Cr-doped</td>
<td>16.15</td>
<td>− 61.12</td>
<td>16.20</td>
<td>− 60.99</td>
</tr>
<tr>
<td>Cu-doped</td>
<td>24.78</td>
<td>− 40.34</td>
<td>24.85</td>
<td>− 40.19</td>
</tr>
<tr>
<td>Sc-doped</td>
<td>21.67</td>
<td>− 47.82</td>
<td>21.89</td>
<td>− 47.31</td>
</tr>
<tr>
<td>Fe-doped</td>
<td>27.66</td>
<td>− 33.42</td>
<td>27.58</td>
<td>− 33.61</td>
</tr>
<tr>
<td>Ni-doped</td>
<td>30.98</td>
<td>− 25.41</td>
<td>31.01</td>
<td>− 25.37</td>
</tr>
<tr>
<td>V-doped</td>
<td>25.89</td>
<td>− 37.66</td>
<td>25.88</td>
<td>− 37.71</td>
</tr>
<tr>
<td>Zn-doped</td>
<td>26.82</td>
<td>− 35.43</td>
<td>26.58</td>
<td>− 36.03</td>
</tr>
<tr>
<td>Ti-doped</td>
<td>20.85</td>
<td>− 49.80</td>
<td>20.80</td>
<td>− 49.93</td>
</tr>
</tbody>
</table>

the unit cell undergoes the longitudinal uniaxial loading
(X direction), the other side of the unit cell is fixed, which
is reversed while the in-plane Young's modulus of other
side is being investigated. However, the atoms are still
relaxed in all positions and are not fixed in any direction.
Then, by plotting the recorded energies $(E_{s})$ with respect
to the strain $(\varepsilon)$ and obtaining its second derivative $(\frac{\partial^{2}E_{s}}{\partial\varepsilon^{2}})$
from these curves, the following equation could be used
to obtain the $Y_{s}$ [46, 47]:

$$
Y_{s}=\frac{1}{A_{0}} \frac{\partial^{2} E_{s}}{\partial \varepsilon^{2}} \tag{1}
$$

where $A_{0}$ is the equilibrium area of the optimized system. The
reason we used in-plane Young's modulus instead of conven-
tional of Young's modulus is to omit the effect of the thickness
in the calculation process since various values are given by
different researchers for similar structure and this would cause
a great chaos. The obtained curves are plotted in Figs. 4 and 5
for the longitudinal direction and Figs. 6 and 7 for the transverse
direction of $2 \times 2$ and $3 \times 3$ nanosheets, respectively. The in-
plane Young's moduli of the structures, which are obtained
through the interpreted method, are presented in Tables 3 and
4 for $2 \times 2$ and $3 \times 3$ nanosheets, respectively. It can be seen that
the in-plane Young's moduli of pristine $2 \times 2$ and $3 \times 3$ nano-
sheets are obtained 41.54 N/m and 41.77 N/m, respectively,
which are in good agreement with previous study obtained by
Akturk et al. [48] with the value of 41 N/m. This comparison
proves that the change in the results is not significant with
increasing the unit cell dimension [49, 50]. In addition, since
the in-plane Young's moduli have negligible difference in two
directions in all the structures, it can be concluded that the
structures studied in this work behave isotropically.
Moreover, it can be seen from Tables 3 and 4 that Young's
moduli of both $2 \times 2$ and $3 \times 3$ nanosheets would decrease
while they undergo the doping procedure. The highest reduc-
tion percentage in $2 \times 2$ structures occurs in Cr-doped nano-
sheet while the lowest reduction percentage is observed in Ni-
doped nanosheet. As for $3 \times 3$ nanosheets, V-doped and Fe-
doped nanosheets had the highest and lowest reduction percent-
ages, respectively.

Bulk modulus

In order to evaluate the bulk modulus of the structures,
biaxial compressive and tensile loading is applied to the

Table 4 Young's modulus of the
3 × 3 pristine and doped
antimonene along the
longitudinal and transverse
directions

<table>
<thead>
<tr>
<th>Structure</th>
<th>Longitudinal Young's modulus (N/m)</th>
<th>Reduction percentage (%)</th>
<th>Transverse Young's modulus (N/m)</th>
<th>Reduction percentage (%)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Pristine</td>
<td>41.77</td>
<td>-------</td>
<td>41.81</td>
<td>-------</td>
</tr>
<tr>
<td>Cr-doped</td>
<td>30.42</td>
<td>− 27.18</td>
<td>30.47</td>
<td>− 27.12</td>
</tr>
<tr>
<td>Cu-doped</td>
<td>29.69</td>
<td>− 28.91</td>
<td>30.17</td>
<td>− 27.83</td>
</tr>
<tr>
<td>Sc-doped</td>
<td>31.50</td>
<td>− 24.60</td>
<td>31.51</td>
<td>− 24.62</td>
</tr>
<tr>
<td>Fe-doped</td>
<td>35.76</td>
<td>− 14.38</td>
<td>35.80</td>
<td>− 14.37</td>
</tr>
<tr>
<td>Ni-doped</td>
<td>35.49</td>
<td>− 15.04</td>
<td>35.42</td>
<td>− 15.28</td>
</tr>
<tr>
<td>V-doped</td>
<td>17.14</td>
<td>− 58.97</td>
<td>17.20</td>
<td>− 58.84</td>
</tr>
<tr>
<td>Zn-doped</td>
<td>31.85</td>
<td>− 23.74</td>
<td>32.04</td>
<td>− 23.37</td>
</tr>
<tr>
<td>Ti-doped</td>
<td>22.22</td>
<td>− 46.81</td>
<td>22.75</td>
<td>− 45.58</td>
</tr>
</tbody>
</table>

![](./images/812520256856653826_16.jpg)

![](./images/812520256856653826_17.jpg)

Fig. 8 Strain energy of the $2 \times 2$ pristine and doped antimonene against the biaxial loading

![](./images/812520256856653826_18.jpg)

![](./images/812520256856653826_19.jpg)

Fig. 9 Strain energy of the $3 \times 3$ pristine and doped antimonene against the biaxial loading

<table>
 <thead>
  <tr>
   <th colspan="3">
    Table 5 Bulk moduli of the $2 \times 2$ pristine and doped antimonene
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>
    Structure
   </td>
   <td>
    Bulk modulus(N/m)
   </td>
   <td>
    Difference with respect to the pristine structure (%)
   </td>
  </tr>
  <tr>
   <td>
    Pristine
   </td>
   <td>
    $24.25$
   </td>
   <td>
    --------
   </td>
  </tr>
  <tr>
   <td>
    Cr-doped
   </td>
   <td>
    $12.12$
   </td>
   <td>
    $- 50.00$
   </td>
  </tr>
  <tr>
   <td>
    Cu-doped
   </td>
   <td>
    $17.68$
   </td>
   <td>
    $- 27.12$
   </td>
  </tr>
  <tr>
   <td>
    Sc-doped
   </td>
   <td>
    $14.60$
   </td>
   <td>
    $- 39.78$
   </td>
  </tr>
  <tr>
   <td>
    Fe-doped
   </td>
   <td>
    $17.19$
   </td>
   <td>
    $- 29.14$
   </td>
  </tr>
  <tr>
   <td>
    Ni-doped
   </td>
   <td>
    $20.72$
   </td>
   <td>
    $- 14.57$
   </td>
  </tr>
  <tr>
   <td>
    V-doped
   </td>
   <td>
    $17.83$
   </td>
   <td>
    $- 26.49$
   </td>
  </tr>
  <tr>
   <td>
    Zn-doped
   </td>
   <td>
    $20.76$
   </td>
   <td>
    $- 14.42$
   </td>
  </tr>
  <tr>
   <td>
    Ti-doped
   </td>
   <td>
    $12.10$
   </td>
   <td>
    $- 50.11$
   </td>
  </tr>
 </tbody>
</table>

unit cell (see Fig. 3) between the range of $- 5$ and $5\%$ with paces of $1\%$. Then, by plotting the recorded energies ($E_{s}$) with respect to the instantaneous cross-sectional area and obtaining its second derivative ($\frac{\partial^{2}E_{s}}{\partial A^{2}}$) from these curves, the following equation could be used to obtain the $B$ [51–53]:

$$
B = A_{0}\frac{\partial^{2}E_{s}}{\partial A^{2}} \tag{2}
$$

Here, $A_{0}$ is the equilibrium area of the optimized unit cell. The obtained curves are plotted in Figs. 8 and 9 for $2 \times 2$ and $3 \times 3$ nanosheets, respectively. In addition, the bulk moduli of these nanosheets are given in Tables 5 and 6, respectively. According to these tables, bulk moduli have been reduced while doping is applied which has previously been seen for the Young’s moduli of doped structures. In addition, the largest reduction in the bulk modulus is caused by doping Ti atom in both $2 \times 2$ and $3 \times 3$ nanosheets while Zn-doped nanosheets experienced the lowest reduction in their bulk moduli among the doped nanosheets. By comparing the reduction percentage obtained in this section with the previous section, one can conclude that doped structures are more sensitive to uniaxial loading in comparison with the biaxial loading.

<table>
 <thead>
  <tr>
   <th colspan="3">
    Table 6 Bulk moduli of the $3 \times 3$ pristine and doped antimonene
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>
    Structure
   </td>
   <td>
    Bulk modulus(N/m)
   </td>
   <td>
    Difference with respect to the pristine structure (%)
   </td>
  </tr>
  <tr>
   <td>
    Pristine
   </td>
   <td>
    $24.28$
   </td>
   <td>
    --------
   </td>
  </tr>
  <tr>
   <td>
    Cr-doped
   </td>
   <td>
    $19.97$
   </td>
   <td>
    $- 17.76$
   </td>
  </tr>
  <tr>
   <td>
    Cu-doped
   </td>
   <td>
    $20.76$
   </td>
   <td>
    $- 14.50$
   </td>
  </tr>
  <tr>
   <td>
    Sc-doped
   </td>
   <td>
    $18.81$
   </td>
   <td>
    $- 22.53$
   </td>
  </tr>
  <tr>
   <td>
    Fe-doped
   </td>
   <td>
    $21.58$
   </td>
   <td>
    $- 11.12$
   </td>
  </tr>
  <tr>
   <td>
    Ni-doped
   </td>
   <td>
    $22.50$
   </td>
   <td>
    $- 7.32$
   </td>
  </tr>
  <tr>
   <td>
    V-doped
   </td>
   <td>
    $18.98$
   </td>
   <td>
    $- 21.84$
   </td>
  </tr>
  <tr>
   <td>
    Zn-doped
   </td>
   <td>
    $22.64$
   </td>
   <td>
    $- 6.78$
   </td>
  </tr>
  <tr>
   <td>
    Ti-doped
   </td>
   <td>
    $18.66$
   </td>
   <td>
    $- 23.15$
   </td>
  </tr>
 </tbody>
</table>

### Plastic properties

In order to obtain plastic properties of structures, the loading is further increased which results in appearance of three different sections. These sections are separated by two different strains, i.e., first, $\varepsilon_{c1}$, and second, $\varepsilon_{c2}$, critical strains. The first critical strain is where ${dE_{T}{(\varepsilon)}}/{d\varepsilon}$ has its maximum value and the region before it is named as the harmonic region. The second critical strain ($\varepsilon_{c2}$) is the point that either the strain energy possesses its maximum value or no more increase is observed. Furthermore, the region between $\varepsilon_{c1}$ and $\varepsilon_{c2}$ can be defined as the inharmonic region. The sum of the harmonic and inharmonic region is named as the elastic region. Finally, for the strains larger than the second critical strain, the nanosheet enters the plastic region.

The critical strains obtained through the explained method are presented in Figs. 10 and 11, for $2 \times 2$ and $3 \times 3$ nanosheets under the uniaxial loadings, and extracted values are presented in Tables 7 and 8 for these nanosheets. It can be seen that doping results in the reduction of the harmonic area in some structures while in others, it leads to increasing the harmonic area. In $2 \times 2$ doped structures compared to the pristine structure, Cu-, Fe-, Zn-, and Ti-doped structures had experienced reduction in their harmonic region while Sc-doped structure experienced the opposite result and no change was seen in the harmonic region of Ni and V-doped structures. In $3 \times 3$ doped structures compared to the pristine structure, Cr-doped structure had experienced reduction in their harmonic region while Sc- and Ti-doped structures experienced the opposite result and no change was seen in the harmonic region of Cu-, Fe-, Ni-, V-, and Zn-doped structures. However, the yield strain of both $2 \times 2$ and $3 \times 3$ structures expressed no unique behavior and all of these structures experienced reduction in their second critical strain after undergoing the doping procedure. The same investigation is done for these nanosheets under the biaxial loading. It can be seen that for $2 \times 2$ nanosheets, doping Sc atom would result in increasing the both first and critical strain while doping Cr, Cu, Fe, V, and Zn had the opposite effect and no changes were observed in the first and second critical strains of Ni- and Ti-doped structures. $3 \times 3$ nanosheets expressed no unique behavior under the biaxial loading which means that the first and second critical strain was reduced in all of the doped structures. These results are given in Tables 9 and 10 along with

![](./images/812520256856653826_20.jpg)

![](./images/812520256856653826_21.jpg)

Fig. 10 Strain energy and first derivative of the strain energy with respect to the strain for the $2\times2$ pristine and doped antimonene under uniaxial loading

![](./images/812520256856653826_22.jpg)

Fig. 11 Strain energy and first derivative of the strain energy with respect to the strain for the $3 \times 3$ pristine and doped antimonene under uniaxial loading

Table 7 First and second
critical strains of the $2 \times$
2 pristine and doped
antimonene under the
uniaxial loading

| Structure   | $\varepsilon_{C_1}$ | $\varepsilon_{C_2}$ |
|-------------|---------------------|---------------------|
| Pristine    | 0.15                | 0.57                |
| Cr-doped    | 0.09                | 0.18                |
| Cu-doped    | 0.12                | 0.15                |
| Sc-doped    | 0.21                | 0.27                |
| Fe-doped    | 0.12                | 0.21                |
| Ni-doped    | 0.15                | 0.18                |
| V-doped     | 0.15                | 0.18                |
| Zn-doped    | 0.12                | 0.15                |
| Ti-doped    | 0.12                | 0.21                |

Table 9 First and second
critical strains of the $2 \times$
2 pristine and doped
antimonene under the
biaxial loading

| Structure   | $\varepsilon_{C_1}$ | $\varepsilon_{C_2}$ |
|-------------|---------------------|---------------------|
| Pristine    | 0.24                | 0.27                |
| Cr-doped    | 0.18                | 0.24                |
| Cu-doped    | 0.09                | 0.12                |
| Sc-doped    | 0.27                | 0.33                |
| Fe-doped    | 0.21                | 0.24                |
| Ni-doped    | 0.24                | 0.27                |
| V-doped     | 0.12                | 0.24                |
| Zn-doped    | 0.12                | 0.21                |
| Ti-doped    | 0.24                | 0.27                |

Figs. 12 and 13 for $2 \times 2$ and $3 \times 3$ nanosheets, respectively. To sum up, the highest reduction in the yield strain of the $2 \times 2$ nanosheets under biaxial loading has been observed in Cu-doped nanosheet while in $3 \times 3$ nanosheets, the highest reduction has occurred in Cu- and Fe-doped nanosheets under the same condition. As for the yield strain of the $2 \times 2$ doped nanosheets under the uniaxial loading, Cu- and Zn-doped structure experienced the highest reduction while in $3 \times 3$ nanosheets, the highest reduction has been observed for Cr-doped nanosheet under the same condition. Since the plastic deformation, which occurs at large strains, would result in the brakeage of the bond (micro crack) and atomic displacement, the plastic deformation figures are provided in the supplementary information to better visualize these changes.

## Conclusions

In summary, we have investigated the structural and mechanical properties of TM-doped antimonene nanosheets by the means of DFT calculations. Cr, Co, Cu, Mn, Ti, V, Zn, and Ni atoms are selected as the doping atoms. Our calculations demonstrated that doping silicene nanosheets with these atoms would result in the reduction of its in-plane Young's and bulk moduli. The highest reduction in the in-plane Young's and bulk moduli of the $2 \times 2$ nanosheets has occurred in the Cr- and Ti-doped structures, respectively, while the same reduction was observed in the V- and Ti-doped structures in the $3 \times 3$ nanosheets. In addition, it was shown that all of the investigated structures express isotropic behavior since the obtained Young's moduli of these nanostructures have negligible difference along longitudinal and transverse directions. Finally, by extending the loading, the plastic behavior of these monolayers was investigated. Our calculations showed that except for $2 \times 2$ Sc-doped structure under biaxial strain, the second critical strain of all doped monolayers would reduce under uniaxial and biaxial loadings. The highest reduction in the yield strain of the $2 \times 2$ nanosheets under biaxial loading has been observed in Cu-doped nanosheet while in $3 \times 3$ nanosheets, the highest reduction has occurred in Cu-, Fe-, and Zn-doped nanosheets under the same condition. As for the yield strain of the doped $2 \times 2$ nanosheets while affected by the uniaxial loading, Cu- and Zn-doped nanosheets experienced the highest reduction while in $3 \times 3$ nanosheets, the highest reduction has been observed for Cr-doped nanosheet under the same condition.

Table 8 First and second
critical strains of the
$3 \times 3$ pristine and doped
antimonene under the
uniaxial loading

| Structure   | $\varepsilon_{C_1}$ | $\varepsilon_{C_2}$ |
|-------------|---------------------|---------------------|
| Pristine    | 0.15                | 0.57                |
| Cr-doped    | 0.09                | 0.12                |
| Cu-doped    | 0.15                | 0.18                |
| Sc-doped    | 0.18                | 0.21                |
| Fe-doped    | 0.15                | 0.18                |
| Ni-doped    | 0.15                | 0.18                |
| V-doped     | 0.15                | 0.18                |
| Zn-doped    | 0.15                | 0.27                |
| Ti-doped    | 0.18                | 0.21                |

Table 10 First and
second critical strains of
the $3 \times 3$ pristine and
doped antimonene under
the biaxial loading

| Structure   | $\varepsilon_{C_1}$ | $\varepsilon_{C_2}$ |
|-------------|---------------------|---------------------|
| Pristine    | 0.24                | 0.27                |
| Cr-doped    | 0.18                | 0.21                |
| Cu-doped    | 0.12                | 0.15                |
| Sc-doped    | 0.18                | 0.21                |
| Fe-doped    | 0.12                | 0.15                |
| Ni-doped    | 0.18                | 0.21                |
| V-doped     | 0.18                | 0.21                |
| Zn-doped    | 0.12                | 0.15                |
| Ti-doped    | 0.21                | 0.24                |

![](./images/812520256856653826_23.jpg)

![](./images/812520256856653826_24.jpg)

Fig. 12 Strain energy and first derivative of the strain energy with respect to the strain for the $2\times2$ pristine and doped antimonene under biaxial loading

![](./images/812520256856653826_25.jpg)

![](./images/812520256856653826_26.jpg)

Fig. 13 Strain energy and first derivative of the strain energy with respect to the strain for the $3 \times 3$ pristine and doped antimonene under biaxial loading

![](./images/812520256856653826_27.jpg)

Supplementary Information The online version contains supplementary material available at https://doi.org/10.1007/s00894-020-04604-0.

Authors' contributions Peyman Aghdasi: conceptualization, methodolo- gy, software, writing -original draft. Shayesteh Yousefi: methodology, software. Reza Ansari: supervision, conceptualization, writing - review and editing.

Data availability The raw/processed data required to reproduce these findings cannot be shared at this time due to technical or time limitations.

# Compliance with ethical standards
Conflict of interest The authors declare that they have no conflict of interest.

Ethics approval N/A.

Consent to participate N/A.

Consent for publication N/A.

Code availability The code required to reproduce these findings cannot be shared at this time due to technical or time limitations.

# References
1. Ferrari AC et al (2015) Science and technology roadmap for graphene, related two-dimensional crystals, and hybrid systems. Nanoscale 7(11):4598-4810
2. Bonaccorso F et al (2015) Graphene, related two-dimensional crys- tals, and hybrid systems for energy conversion and storage. Science 347(6217):1246501
3. Geim AK, Grigorieva IV (2013) Van der Waals heterostructures. Nature 499(7459):419-425
4. Geim AK, Novoselov KS (2009) The rise of graphene. Nanoscience and Technology 11-19. https://doi.org/10.1142/9789814287005_0002
5. Neto AC, Guinea F, Peres NM, Novoselov KS, Geim AK (2009) The electronic properties of graphene. Rev Mod Phys 81(1):109
6. Dai S, Zhou W, Liu Y, Lu Y-L, Sun L, Wu P (2018) Tunable electronic and magnetic properties of antimonene system via Fe doping and defect complex: a first-principles perspective. Appl Surf Sci 448:281-287
7. Li L et al (2014) Black phosphorus field-effect transistors. Nat Nanotechnol 9(5):372
8. Liu H et al (2014) Phosphorene: an unexplored 2D semiconductorwith a high hole mobility. ACS Nano 8(4):4033-4041
9. Kamal C, Ezawa M (2015) Arsenene: two-dimensional buckledand puckered honeycomb arsenic systems. Phys Rev B 91(8):085423
10. Aghdasi P, Ansari R, Rouhi S, Goli M, Gilakjani HA (2019) Investigating the effects of H and F adsorption on the elastic and plastic properties of arsenene nanosheets. Phys B Condens Matter574:411672
11. Aktürk E, Aktürk OÜ, Ciraci S (2016) Single and bilayer bismuthene: stability at high temperature and mechanical and elec-tronic properties. Phys Rev B 94(1):014115
12. Aghdasi P, Ansari R, Rouhi S, Goli M (2019) On the elastic and plastic properties of the bismuthene adsorbed by H, F, CI and Bratoms. Superlattice Microst 135:106242

13. Wang G, Pandey R, Karna SP (2015) Atomically thin group V elemental films: theoretical investigations of antimonene allotropes.ACS Appl Mater Interfaces 7(21):11490-11496
14. Le Lay G et al (2009) Physics and chemistry of silicene nano-ribbons. Appl Surf Sci 256(2):524-529
15. Aufray B et al (2010) Graphene-like silicon nanoribbons on Ag(110): a possible formation of silicene. Appl Phys Lett 96(18):183102
16. Lalmi B et al (2010) Epitaxial growth of a silicene sheet. Appl PhysLett 97(22):223109
17. Bianco E, Butler S, Jiang S, Restrepo OD, Windl W, Goldberger JE(2013) Stability and exfoliation of germanane: a germaniumgraphane analogue. ACS Nano 7(5):4414-4421
18. Wood JD et al (2014) Effective passivation of exfoliated black phosphorus transistors against ambient degradation. Nano Lett14(12):6964-6970
19. Island JO, Steele GA, van der Zant HS, Castellanos-Gomez A(2015) Environmental instability of few-layer black phosphorus.2D Materials 2(1):011002
20. Favron A et al (2015) Photooxidation and quantum confineementeffects in exfoliated black phosphorus. Nat Mater 14(8):826-832
21. Hanlon D et al (2015) Liquid exfoliation of solvent-stabilized few- layer black phosphorus for applications beyond electronics. NatCommun 6(1):1-11
22. Gibaja C et al (2016) Few-layer antimonene by liquid-phase exfo-liation. Angew Chem Int Ed 55(46):14345-14349
23. Ares P et al (2016) Mechanical isolation of highly stable antimonene under ambient conditions. Adv Mater 28(30):6332-6336
24. Zhao M, Zhang X, Li L (2015) Strain-driven band inversion andtopological aspects in antimonene. Sci Rep 5:16108
25. Zhang S et al (2016) Semiconducting group 15 monolayers: a broad range of band gaps and high carrier mobilities. Angew Chem Int Ed55(5):1666-1669
26. Singh D, Gupta SK, Sonvane Y, Lukačevic I (2016) Antimonene: a monolayer material for ultraviolet optical nanodevices. J MaterChem C 4(26):6386-6390
27. Lu L et al (2017) Broadband nonlinear optical response in few-layer antimonene and antimonene quantum dots: a promising optical Kerr media with enhanced stability. Advanced Optical Materials5(17):1700301
28. Gu J, Du Z, Zhang C, Ma J, Li B, Yang S (2017) Liquid-phase exfoliated metallic antimony nanosheets toward high volumetricsodium storage. Adv Energy Mater 7(17):1700447
29. Yang L, Song Y, Mi W, Wang X (2016) Prediction of spin- dependent electronic structure in 3 d-transition-metal dopedantimonene. Appl Phys Lett 109(2):022103
30. Tao W et al (2017) Antimonene quantum dots: synthesis and ap- plication as near-infrared photothermal agents for effective cancertherapy. Angew Chem Int Ed 56(39):11896-11900
31. Meng R-S et al (2016) First principles investigation of small mol- ecules adsorption on antimonene. IEEE Electron Device Letters38(1):134-137
32. Nagarajan V, Chandiramouli R (2018) First-principles investiga- tion on structural and electronic properties of antimonene nanoribbons and nanotubes. Physica E: Low-dimensionalSystems and Nanostructures 97:98-104
33. Wang S, Wang W, Zhao G (2016) Thermal transport properties ofantimonene: an ab initio study. Phys Chem Chem Phys 18(45):31217-31222
34. Niu T et al (2020) Large-scale synthesis of strain-tunable semicon-ducting antimonene on copper oxide. Adv Mater 32(4):1906873
35. Srivastava P, Abhishek, Jaiswal NK (2020) First-principles inves- tigation of CO2 and NH3 adsorption on antimonene nanoribbons.Materials Today: Proceedings 28:65-69

![](./images/812520256856653826_28.jpg)

36. Hu L et al (2020) Direct bandgap opening in sodium-doped antimonene quantum dots: an emerging 2D semiconductor. Materials Horizons 7(6):1588–1596

37. Zhang G et al (2019) 2D group-VA fluorinated antimonene: syn- thesis and saturable absorption. Nanoscale 11(4):1762–1769

38. Ersan F, Aktürk E, Ciraci S (2016) Stable single-layer structure of group-V elements. Phys Rev B 94(24):245417

39. Kripalani DR, Kistanov AA, Cai Y, Xue M, Zhou K (2018) Strain engineering of antimonene by a first-principles study: mechanical and electronic properties. Phys Rev B 98(8):085410

40. Hu Y, Shu T, Mao C, Xue L, Yan Z, Wu Y (2019) Arsenene and antimonene doped by group-VA atoms: first-principles studies of the geometric structures, electronic properties and STM images. Phys B Condens Matter 553:195–201

41. Ordejón P, Artacho E, Soler JM (1996) Self-consistent order-N density-functional calculations for very large systems. Phys Rev B 53(16):R10441

42. Soler JM et al (2002) The SIESTA method for ab initio order-N materials simulation. J Phys Condens Matter 14(11):2745

43. Perdew JP, Burke K, Ernzerhof M (1996) Generalized gradient approximation made simple. Phys Rev Lett 77(18):3865

44. Ziesche P, Kurth S, Perdew JP (1998) Density functionals from LDA to GGA. Comput Mater Sci 11(2):122–127

45. Aghdasi P, Ansari R (2020) Structural and mechanical properties of Sb and SbX (X=H, F, Cl and Br) monolayers. Solid State Commun 311:113849

46. Goli M, Ansari R, Rouhi S, Aghdasi P, Mozvashi SM (2020) Influence of F and H adsorption on the elasto-plastic properties of silicene: a DFT investigation. Physica E: Low-dimensional Systems and Nanostructures 119:113984

47. Aghdasi P, Ansari R, Rouhi S, Yousefi S (2020) A DFT-based finite element approach for studying elastic properties, buckling and vibration of the arsenene. J Mol Graph Model 101:107725

48. Aktürk OÜ, Özçelik VO, Ciraci S (2015) Single-layer crystalline phases of antimony: antimonenes. Phys Rev B 91(23):235446

49. Topsakal M, Cahangirov S, Ciraci S (2010) The response of me- chanical and electronic properties of graphane to the elastic strain. Appl Phys Lett 96(9):091912

50. Mirnezhad M, Ansari R, Rouhi H (2012) Effects of hydrogen ad- sorption on mechanical properties of chiral single-walled zinc oxide nanotubes. J Appl Phys 111(1):014308

51. Aghdasi P, Ansari R, Yousefi S, Goli M (2020) Structural and mechanical properties of pristine and adsorbed puckered arsenene nanostructures: a DFT study. Superlattice Microst 139:106414

52. Yousefi S, Ansari R, Aghdasi P, Mozvashi SM (2020) Structural and mechanical properties characterization of arsenene nanosheets under doping effect of transition metals: a DFT study. Physica E: Low-dimensional Systems and Nanostructures 124:114349

53. Aghdasi P, Ansari R, Rouhi S, Yousefi S, Goli M, Soleimani HR (2020) Investigating elastic and plastic characteristics of monolayer phosphorene under atomic adsorption by the density functional theory. Phys B Condens Matter 600:412603. https://doi.org/10.1016/j.physb.2020.412603

![](./images/812520256856653826_29.jpg)
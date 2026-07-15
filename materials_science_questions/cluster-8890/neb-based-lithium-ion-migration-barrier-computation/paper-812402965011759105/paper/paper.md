# STRUCTURAL AND DYNAMICAL PROPERTIES OF SOME LITHIUM BORATE GLASSES

W. SOPPE, C. VAN DER MAREL * and H.W. DEN HARTOG

Solid State Physics Laboratory, State University of Groningen, Melkweg 1, 9718 EP Groningen, The Netherlands

Received 24 August 1987
Revised manuscript received 23 October 1987

Structural and dynamical properties of some lithium borate glasses have been investigated by means of X-ray diffraction studies and molecular dynamics (MD) calculations. The structure of lithium borate glasses appears to consist of randomly connected planar $BO_{3}$ triangles and $BO_{4}$ units. A comparison of the slowly quenched glasses (studied by X-ray diffraction) and fastly quenched glasses (studied by MD simulations) leads to the conclusion that a small quench rate leads to a preponderance for the B-O-B angles of adjacent $BO_{3}$ triangles to $120^{\circ}$. The frequency spectra of B-O vibrations in the MD simulations agree qualitatively with infrared transmission spectra.

## 1. Introduction
In this paper we will present the results of molecular dynamics (MD) calculations of vitreous $\mathrm{B}_{2} \mathrm{O}_{3}, \quad\left(\mathrm{~B}_{2} \mathrm{O}_{3}\right)_{0.9}\left(\mathrm{Li}_{2} \mathrm{O}\right)_{0.1}$ and $\left(\mathrm{B}_{2} \mathrm{O}_{3}\right)_{0.8}\left(\mathrm{Li}_{2} \mathrm{O}\right)_{0.2}$. We will compare these results with the results of X-ray diffraction studies, performed at our own laboratory and with infrared transmission spectra as observed by Wong [1].

In a previous paper [2], we have shown that the structure of $\mathrm{v}-\mathrm{B}_{2} \mathrm{O}_{3}$ can be studied quite well by MD simulations, provided that the quench rate of the obtained glass is taken into account. In this paper we will show that this is also true for Li borate glass.

During the last decade numerous simulation studies of glass structure and other properties of glasses, using Monte Carlo (MC) and MD tech- niques have been reported. The advantage of MD calculations above MC calculations is the possibil- ity to analyse the dynamics of the glass system.

Until now most attention in this respect has been paid to the diffusion coefficients [3]. Unfor- tunately the diffusion processes are very slow on the time scale of MD simulations. Therefore, in order to study transport properties, very high tem- peratures (up to 20000 K) have to be used.

Less attention has been paid to the vibrational properties of glasses by means of MD simulations. In order to gain a better understanding of the Raman and infrared spectra of borate glasses, we have analysed the vibrations of B-O, B-B and O-O nearest-neighbour pairs during MD simula- tions. The B-O pairs appear to be quasi-harmonic oscillators giving rise to a Fourier-analysed spec- trum, which agrees qualitatively quite well with IR spectra. Apart from the structural results, this provides another argument for the reliability of the atomic interactions we have used in the MD simulations.

## 2. Structure of alkali borate glasses
### 2.1. X-ray diffraction
We have prepared for our experiments samples of pure $\mathrm{v}-\mathrm{B}_{2} \mathrm{O}_{3}$, and $\mathrm{v}-\mathrm{B}_{2} \mathrm{O}_{3}$ containing 10 and $20 \%$ $\mathrm{Li}_{2} \mathrm{O}$ as described by Soppe et al. [2,4,5]. The quench rate of the glasses was $10^{3} \mathrm{~K} / \mathrm{s}$.

The X-ray diffraction spectra were measured between $k=0$ and $k=13 \AA^{-1}$ using Mo $\mathrm{K} \alpha$ radiation. The radiation was monochromated by a

* Present address: Philips Elcoma, CLE/BL 67, P.O. Box 218, 5600 MD Eindhoven, The Netherlands.

0022-3093/88/$03.50 © Elsevier Science Publishers B.V.
(North-Holland Physics Publishing Division)

<table>
<caption>Table 1
Weight factors for X-ray scattering</caption>
 <thead>
  <tr>
   <th>Li₂O
(mol%)</th>
   <th>W<sub>LiLi</sub></th>
   <th>W<sub>LiO</sub></th>
   <th>W<sub>LiB</sub></th>
   <th>W<sub>BB</sub></th>
   <th>W<sub>BO</sub></th>
   <th>W<sub>OO</sub></th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <th>0</th>
   <td>–</td>
   <td>–</td>
   <td>–</td>
   <td>0.110</td>
   <td>0.450</td>
   <td>0.440</td>
  </tr>
  <tr>
   <th>10</th>
   <td>0.004</td>
   <td>0.078</td>
   <td>0.039</td>
   <td>0.098</td>
   <td>0.391</td>
   <td>0.390</td>
  </tr>
  <tr>
   <th>20</th>
   <td>0.008</td>
   <td>0.110</td>
   <td>0.054</td>
   <td>0.090</td>
   <td>0.366</td>
   <td>0.373</td>
  </tr>
 </tbody>
</table>

curved quartz crystal. The spectra were corrected for absorption, inelastic (Compton) and multiple scattering.

The resulting radial distribution function is the sum of six partial distribution functions:

$$
\begin{aligned}
g_{\exp }(r) & =W_{\mathrm{LiLi}} g_{\mathrm{LiLi}}(r)+W_{\mathrm{LiO}} g_{\mathrm{LiO}}(r) \\
& +W_{\mathrm{LiB}} g_{\mathrm{LiB}}(r)+W_{\mathrm{BB}} g_{\mathrm{BB}}(r) \\
& +W_{\mathrm{BO}} g_{\mathrm{BO}}(r)+W_{\mathrm{OO}} g_{\mathrm{OO}}(r).
\end{aligned}
\tag{1}
$$

The weight factors $W$ are presented in table 1.

The scattering of the Li and B atoms is very small compared with that of the O atoms, so that we may neglect the first four terms.

### 2.2. Molecular dynamics calculations

The MD calculations were performed on the Amsterdam CYBER 205 vectorprocessor (1 pipe), using the computer program library GROMOS [2]. The Born-Mayer-Huggins potential was used to calculate the atomic interactions:

$$
\begin{aligned}
V_{i j}(r)= & A_{i j} \exp (-r / \sigma)+z_{i} \cdot z_{j} \cdot e^{2} / r \\
& \cdot \operatorname{erfc}\left(r /\left(\eta \cdot R_{\text {box }}\right)\right)
\end{aligned}
\tag{2}
$$

with

$$
\begin{aligned}
A_{i j}= & 20.3545 \mathrm{~kJ} / \mathrm{mol} \cdot\left(1+z_{i} / n_{i}+z_{j} / n_{j}\right) \\
& \cdot \exp \left(\left(r_{i}+r_{j}\right) / \sigma\right).
\end{aligned}
\tag{3}
$$

The details of the simulation parameters are given in table 2. The ionic radii are according to Tosi and Fumi [6] and Soules [7].

We have started the simulation of each glass with a run of 1000 timesteps of 1 fs at a (fictive) temperature of 6000 K. Then the glass system was cooled to 300 K by scaling the velocities of the ions [2]. The volume of the glass system was kept constant, in accordance with the experimental

<table>
<caption>Table 2(a)
Parameters of the Born-Mayer-Huggins potential</caption>
 <thead>
  <tr>
   <th>   </th>
   <th>$r_{i}$ (Å)</th>
   <th>$n_{i}$</th>
   <th>$z_{i}$</th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>B</td>
   <td>0.74</td>
   <td>2</td>
   <td>+ 3</td>
  </tr>
  <tr>
   <td>O</td>
   <td>1.42</td>
   <td>8</td>
   <td>– 2</td>
  </tr>
  <tr>
   <td>Li</td>
   <td>0.93</td>
   <td>2</td>
   <td>+ 1</td>
  </tr>
 </tbody>
</table>

<table>
<caption>Table 2(b)
Simulation parameters for $(B_{2}O_{3})_{1 - x}(Li_{2}O)_{x}$</caption>
 <thead>
  <tr>
   <th>Composition
$x$</th>
   <th colspan="3">Number of ions</th>
   <th>$R_{\text{box}}$
(Å)</th>
   <th>Density
(g/cm³)</th>
  </tr>
  <tr>
   <th>   </th>
   <th>B</th>
   <th>O</th>
   <th>Li</th>
   <th>   </th>
   <th>   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>0</td>
   <td>672</td>
   <td>1008</td>
   <td>0</td>
   <td>27.46</td>
   <td>1.84</td>
  </tr>
  <tr>
   <td>0.1</td>
   <td>648</td>
   <td>1008</td>
   <td>72</td>
   <td>27.20</td>
   <td>1.95</td>
  </tr>
  <tr>
   <td>0.2</td>
   <td>576</td>
   <td>936</td>
   <td>144</td>
   <td>25.78</td>
   <td>2.15</td>
  </tr>
 </tbody>
</table>

<table>
<caption>Table 3(a)
Pair distances in some borate glasses</caption>
 <thead>
  <tr>
   <th>   </th>
   <th colspan="2">B₂O₃ pure</th>
   <th colspan="2">$(B_{2}O_{3})_{0.9}$
$(Li_{2}O)_{0.1}$</th>
   <th colspan="2">$(B_{2}O_{3})_{0.8}$
$(Li_{2}O)_{0.2}$</th>
  </tr>
  <tr>
   <th>   </th>
   <th>MD</th>
   <th>X-ray</th>
   <th>MD</th>
   <th>X-ray</th>
   <th>MD</th>
   <th>X-ray</th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>BB-I</td>
   <td>2.71</td>
   <td>   </td>
   <td>2.73</td>
   <td>   </td>
   <td>2.74</td>
   <td>   </td>
  </tr>
  <tr>
   <td>BB-II</td>
   <td>4.48</td>
   <td>   </td>
   <td>4.49</td>
   <td>   </td>
   <td>4.50</td>
   <td>   </td>
  </tr>
  <tr>
   <td>BB-III</td>
   <td>6.88</td>
   <td>   </td>
   <td>6.87</td>
   <td>   </td>
   <td>6.86</td>
   <td>   </td>
  </tr>
  <tr>
   <td>OO-I</td>
   <td>2.46</td>
   <td>2.37</td>
   <td>2.47</td>
   <td>2.35</td>
   <td>2.48</td>
   <td>2.37</td>
  </tr>
  <tr>
   <td>OO-II</td>
   <td>4.28</td>
   <td>4.41</td>
   <td>4.28</td>
   <td>4.32</td>
   <td>4.29</td>
   <td>4.41</td>
  </tr>
  <tr>
   <td>OO-III</td>
   <td>6.76</td>
   <td>   </td>
   <td>6.76</td>
   <td>   </td>
   <td>6.76</td>
   <td>   </td>
  </tr>
  <tr>
   <td>BO-I</td>
   <td>1.39</td>
   <td>1.38</td>
   <td>1.41</td>
   <td>1.38</td>
   <td>1.44</td>
   <td>1.42</td>
  </tr>
  <tr>
   <td>BO-II</td>
   <td>3.59</td>
   <td>3.14,
3.70</td>
   <td>3.59</td>
   <td>3.05,
3.70</td>
   <td>3.57</td>
   <td>3.14,
3.74</td>
  </tr>
  <tr>
   <td>BO-III</td>
   <td>5.81</td>
   <td>   </td>
   <td>5.82</td>
   <td>   </td>
   <td>5.83</td>
   <td>   </td>
  </tr>
  <tr>
   <td>LiO-I</td>
   <td>   </td>
   <td>   </td>
   <td>2.48</td>
   <td>   </td>
   <td>2.48</td>
   <td>   </td>
  </tr>
  <tr>
   <td>LiO-II</td>
   <td>   </td>
   <td>   </td>
   <td>4.12</td>
   <td>   </td>
   <td>4.11</td>
   <td>   </td>
  </tr>
  <tr>
   <td>LiO-III</td>
   <td>   </td>
   <td>   </td>
   <td>6.16</td>
   <td>   </td>
   <td>6.16</td>
   <td>   </td>
  </tr>
 </tbody>
</table>

<table>
<caption>Table 3(b)
Bond angles and coordination numbers (MD results)</caption>
 <thead>
  <tr>
   <th>   </th>
   <th>B₂O₃ pure</th>
   <th>$(B_{2}O_{3})_{0.9}$
$(Li_{2}O)_{0.1}$</th>
   <th>$(B_{2}O_{3})_{0.8}$
$(Li_{2}O)_{0.2}$</th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>O<sub>coor</sub></td>
   <td>1.97</td>
   <td>2.04</td>
   <td>2.07</td>
  </tr>
  <tr>
   <td>BOB angle</td>
   <td>160</td>
   <td>154</td>
   <td>144</td>
  </tr>
  <tr>
   <td>B<sub>coor</sub></td>
   <td>2.96</td>
   <td>3.17</td>
   <td>3.37</td>
  </tr>
  <tr>
   <td>OBO angle</td>
   <td>120</td>
   <td>117</td>
   <td>114</td>
  </tr>
  <tr>
   <td>OBO angle
(X-ray)</td>
   <td>118</td>
   <td>117</td>
   <td>113</td>
  </tr>
 </tbody>
</table>

![](./images/812402965011759105_1.jpg)

densities of the glasses. The quench rate of these glasses was about $10^{12}$ K/s.

### 2.3. Results
The interatomic pair distances for the investi- gated glass systems $(B_{2}O_{3})_{1-x}(L_{i2}O)_{x}$ are given in table 3 as they result from both the X-ray studies and the MD simulation studies.

The first peak that can be observed in the X-ray spectra is a boron-oxygen peak revealing a B-O distance that increases from $1.38\ \mathring{A}$ for $x=0$ to $1.42\ \mathring{A}$ for $x=0.2$.

The MD simulations result in a somewhat larger B-O distance: 1.39 to $1.44\ \mathring{A}$. The coordination number of the oxygen atoms increases slightly with increasing $Li_{2}O$ content whereas the boron coordination number increases from 2.96 for $x=0$ to 3.17 for $x=0.1$ and 3.37 for $x=0.2$. This implies that the $NBO_{4}$ fraction is 0.0 in pure $B_{2}O_{3}$, 0.15 for $x=0.1$ and 0.35 for $x=0.20$.

We may compare these results with NMR mea- surements obtained by Feller et al. [8]. These authors found the fraction of four coordinated boron atoms in $B_{2}O_{3})_{1-x}(Li_{2}O)_{x}$ to increase lin early with $R$, where $R=x/(1-x)$ [8]. This re sults in a $NBO_{4}$ fraction of 0.0, 0.11 and 0.25 for respectively $x=0.0$, $x=0.10$ and $x=0.20$.

The second peak, observed in the X-ray spectra is an oxygen-oxygen peak and its position is almost independent of the $Li_{2}O$ content. Although

![](./images/812402965011759105_2.jpg)

Fig. 2. Potential energy versus temperature for borate glasses simulated by MD calculations.

this O-O distance (2.37 Å) is smaller than the O-O distance found in the MD simulations (2.46-2.48 Å), the resulting mean O-B-O angles correspond well with one another.

The next peak in the X-ray spectra is situated at 3.1 Å. In a previous article [2] we have shown that this peak makes a glass structure containing large numbers of so-called boroxol rings very im- probable.

The peak at 3.1 Å, together with the peak at 3.7 Å however, can well be assigned to a boron-next-oxygen pair which forms part of two adjacent $BO_3$ triangles with a B-O-B angle of $120^{\circ}$, provided that the second B atom is out of the plane of the first $BO_3$ triangle as a far as possible (see fig. 1).

For the MD simulated glasses we only find one BO-II peak at 3.6 Å. The structure of these glasses consists of randomly connected $BO_3$ and $BO_4$ units. The realization of structural groupings of fig. 1 is apparently prevented by the very large quench rate of these glasses. The boron-boron and lithium-oxygen distances, which can only be observed by MD simulations appear to be inde- pendent of the lithium oxide content.

The radial distribution functions involving the lithium atoms do hardly show any structure be- yond the (weak) nearest neighbour peaks. Visual inspection of the structure by means of stereo- scopic pictures confirms the thesis that the lithium ions are bound very weakly to the negatively charged $BO_4$ groups and reside predominantly in voids of the boron-oxygen network.

In fig. 2 we show the potential energy versus temperature of the MD simulated glasses. We have fitted the data with:
$$
E_{\mathrm{pot}}=E_{0}+C \cdot T, \tag{4}
$$
and obtained $C=12\ \mathrm{J/(K \cdot mol)}$ at room temperature for all three glass systems. The resulting heat capacity of the glasses is $C_{\mathrm{v}}=C+\frac{3}{2}N \cdot k=24.5\ \mathrm{J/(K \cdot mol)}$.

## 3. Dynamical properties
### 3.1. Diffusion

In fig. 3 we show the trajectories of boron, oxygen and lithium atoms in $v$-(B₂O₃)₀.₉(Li₂O)₀.₁ at 3000 and 1250 K.

![](./images/812402965011759105_3.jpg)

Fig. 3. Atomic trajectories during a MD simulation. (a) Li atoms; (b) O atoms; (c) B atoms.

We see that, on the time scale of MD simula- tion studies the glass is transferred from a liquid state into a solid state if the temperature is de- creased from 3000 K to 1250 K. Below the latter temperature, the atoms carry out random oscilla- tions around their origins.

The motions of the atoms can be analyzed through the time-dependent self-correlation func- tion $G_{\mathrm{s}}(r,t)$ [10]. We therefore define:
$$
\left\langle r^{2n}\right\rangle=\sum_{i}\left(r_{i}(t)-r_{i}(0)\right)^{2n}, \tag{5}
$$
and
$$
\left\langle r^{2n}\right\rangle=\int r^{2n}G_{\mathrm{s}}(r,t)\ \mathrm{d}r. \tag{6}
$$

The physical interpretation of the function $G_{\mathrm{s}}(r,t)$ is that $4\pi r^{2} \cdot G_{\mathrm{s}}(r,t)$ is the probability at time $t$

of a particle being at a distance between $r$ and $r+\mathrm{d} r$ from its position at $t=0$.

If $G_{\mathrm{s}}(r, t)$ has a Gaussian dependence on $r$:
$$
G_{\mathrm{s}}(r, t)=[4 \pi \sigma(t)]^{-3 / 2} \cdot \exp \left[-r^{2} / 4 \sigma(t)\right], \quad(7)
$$
then one has the following relations:
$$
\left\langle r^{2}\right\rangle=6 \sigma(t),\qquad(8)
$$

$$
\left\langle r^{2 n}\right\rangle=C_{n}\left\langle r^{2}\right\rangle^{n},\qquad(9)
$$
where
$$
C_{n}=1 * 3 * 5 * \cdots(2 n+1) / 3^{n}.\qquad(10)
$$

For a Gaussian $G_{\mathrm{s}}(r, t)$ the moments ratio
$$
P_{n}=\left\langle r^{2 n}\right\rangle / C_{n}\left\langle r^{2}\right\rangle^{n}\qquad(11)
$$
will be equal to 1.

$G_{\mathrm{s}}(r, t)$ will have a Gaussian dependence on $r$ in case of a random walk diffusion in a liquid, but not in case of jump diffusion. Therefore the parameter $P_{n}$ is a helpful tool in the determination of the nature of the diffusion.

Figure 4 shows plots of $P_{2}$, which is called $P_{\alpha}$ after Moscinski and Jacobs [10], for a lithium borate glass at $T=6000 \mathrm{~K}$ and $T=300 \mathrm{~K}$.

At high temperatures, $P_{\alpha}=1$ for all the three atom species but at lower temperatures $(T<1000$ K) the plots of $P_{\alpha}$ show deviations from $P_{\alpha}=1$. These deviations indicate that at temperatures be- low the point of congelation, the motion of the $\mathrm{Li}^{+}$ions has non-random characteristics. The dif- fusion of the $\mathrm{Li}^{+}$ions in borate glasses at low temperatures probably occurs by a hopping mech- anism, with the $\mathrm{Li}^{+}$jumping from one interstitial position to another [4]. Figure 5 shows the poten- tial energy of a $\mathrm{Li}^{+}$in an arbitrary layer in the glass network of $(\mathrm{B}_{2} \mathrm{O}_{3})_{0.9} \cdot(\mathrm{Li}_{2} \mathrm{O})_{0.1}$ calculated in $20 * 20 * 20$ grid.

The potential is high (up to $2000 \mathrm{~kJ} / \mathrm{mol}$) in the vicinity of boron atoms and $\mathrm{Li}^{+}$ions and is low $(-100 \mathrm{~kJ} / \mathrm{mol})$ in the vicinity of oxygen atoms. The valleys in this energy landscape allow the $\mathrm{Li}^{+}$ions to move easily through the glass network.

### 3.2. Dynamical structure factor

The dynamical structure factor (DSF) has been used in MD simulation studies of crystalline materials in order to obtain information on the phonon frequencies [10,11]. The DSF represents the spectrum of density fluctuations at wavevector $\boldsymbol{q}$. The DSF for the correlation between atoms of type $\alpha$ and type $\beta$ is defined as
$$
\begin{aligned}
& S_{\alpha \beta}(\boldsymbol{q}, \omega) \\
& \quad=\frac{1}{2 \pi} \int \exp (i \omega t)\left\langle\rho_{\alpha}(\boldsymbol{q}, t) \rho_{\beta}(\boldsymbol{q}, 0)^{*}\right\rangle \mathrm{d} t, \quad(12)
\end{aligned}
$$
where
$$
\rho_{\alpha}(\boldsymbol{q})=\frac{1}{\sqrt{N_{\alpha}}} \sum_{i} \exp \left(\mathrm{i} \boldsymbol{q} \cdot \boldsymbol{r}_{\alpha i}\right)\qquad(13)
$$
represents the density of ions of type $\alpha$ associated with wavevector $\boldsymbol{q}$.

![](./images/812402965011759105_4.jpg)

Fig. 4. $P_{\alpha}$ for the three atomic species. $\longrightarrow$ Li atoms, - - - O atoms, - - - - B atoms. (a) $T=6000 \mathrm{~K}$; (b) $T=300 \mathrm{~K}$.

![](./images/812402965011759105_5.jpg)

Fig. 5. Potential energy of a $Li^{+}$ ion in an arbitrary layer in the glass network of $(B_{2}O_{3})_{0.8}(Li_{2}O)_{0.2}$.

![](./images/812402965011759105_6.jpg)

Fig. 6. DSF for $(B_{2}O_{3})_{0.8}(Li_{2}O)_{0.2}$ at 300 K. Wavevector $q=2\pi/R_{\text{box}}$, where $R_{\text{box}}$ is the boxlength.

![](./images/812402965011759105_7.jpg)

Fig. 7. B-O distance of a nearest neighbour pair during 10 fs.

In an isotropic structure eq. (13) reduces to
$$
\rho_{\alpha}(q)=\frac{1}{\sqrt{N_{\alpha}}} \sum_{i} \frac{\sin \left(q \cdot r_{\alpha i}\right)}{q \cdot r_{\alpha i}}, \tag{14}
$$
and the DSF becomes
$$
\begin{aligned}
S_{\alpha \beta}(q, \omega)= & \mathrm{FT}\left(\frac{1}{\sqrt{N_{\alpha} N_{\beta}}} \sum_{i} \frac{\sin \left(q \cdot r_{\alpha i}(t)\right)}{q \cdot r_{\alpha i}(t)}\right. \\
& \left.\times \sum_{j} \frac{\sin \left(q \cdot r_{\beta j}(0)\right)}{q \cdot r_{\beta j}(0)}\right), \tag{15}
\end{aligned}
$$
where FT is the Fourier Transform operator.

In fig. 6 we show the DSF for $(B_{2} O_{3})_{0.8}(Li_{2} O)_{0.2}$ at $T=300 ~K$ . The spectra associated with the depicted atom pairs only show a peak centered at zero frequency. Other pair combinations give rise to similar results. This peak is associated with anharmonic movements of the atoms. The absence of peaks at non-zero frequencies indicates that the glass structure does not perform harmonical den- sity fluctuations.

### 3.3. B-O vibrations
Fig. 7 shows the distance $R_{B-O}(t)$ between an adjacent boron-oxygen pair in a period of 10 fs during a MD simulation at $300 ~K$ . We see that the B-O distance oscillates around a value of $1.38 \AA$ .

The frequency spectrum of these oscillations can be obtained by a Fourier transformation of $R_{B-O}(t)$ for all nearest neighbour $R-O$ pairs. A certain fraction of the B-O pairs splits up during the simulations, we have deleted these pairs in our analyses.

In fig. 8 we show the results of the Fourier analyses for the three glass systems considered in this study. For $v-B_{2} O_{3}$ the spectrum reveals an intense and narrow band at $1100 ~cm^{-1}$ and two weaker bands at $1300 ~cm^{-1}$ and $1600 ~cm^{-1}$ . The addition of $Li_{2} O$ leads to a broadening and a shift of the main peak towards lower frequencies.

This shift is due to an increase of the B-O distance (see table 3(a)). The broadening of the main band can be explained by the increased width of the distribution of $B-O$ distances. The bandwidths of the first $B-O$ peak in the pair distribution spectra of MD simulated $(B_{2} O_{3})_{1-x}$  $(Li_{2} O)_{x}$ are $0.06 \AA, 0.09 \AA$ and $0.11 \AA$ for respec tively $x=0.0, x=0.1$ and $x=0.2$ .

![](./images/812402965011759105_8.jpg)

Fig. 8. Fourier spectrum of vibrations of B-O nearest neighbour pairs at $300 ~K$ for $(B_{2} O_{3})_{1-x}(Li_{2} O)_{x}$ .

We shall now compare these results with those of spectroscopy studies, e.g. Raman and IR ex- periments.

The main features of the Raman spectra, de- picted in fig. 9, consist of an intense and narrow band at $800 ~cm^{-1}$ for pure $v-B_{2} O_{3}$ plus a similar band at $780 ~cm^{-1}$ for lithium borate glass which increases at the expense of the $800 ~cm^{-1}$ band as the lithium content is increased. The small band- width indicates that the vibrational modes associ- ated with these peaks are decoupled almost com- pletely from the rest of the network. In general these bands are attributed to breathing modes of boroxol rings and borate rings [5].

Another feature of the Raman spectrum of $v-B_{2} O_{3}$ is the presence of a band at $1250 ~cm^{-1}$ . This band can also be observed in the infrared transmission spectrum (see fig. 10). This band is

![](./images/812402965011759105_9.jpg)

Fig. 9. Raman spectra of three lithium borate glasses of type $(B_{2}O_{3})_{1-x}(Li_{2}O)_{x}$.

attributed to a B-O bond stretch motion. The lack of symmetry of this vibrational mode allows in- frared and Raman activity.

![](./images/812402965011759105_10.jpg)

Fig. 10. IR spectrum of v-$B_{2}O_{3}$ according to Wong [1].

If we compare the MD simulation spectrum of fig. 8 with these spectra, the overall resemblance with the IR spectrum is salient. Although the positions of the bands do not agree exactly, we see that the main features of the IR spectrum, a relatively narrow band at $1250\ cm^{-1}$ and a shoulder at $1300\ cm^{-1}$, can be reproduced by MD simulation studies.

The reason for the major bands in the MD simulation spectra to occur at lower frequencies than those of the IR spectrum is probably found in the fact that the MD simulated glasses have a less ordered structure than laboratory glasses. This lower ordering is due to the high quench rates and is expressed in the somewhat larger atomic pair distances (see table 3(a)) and in the appreciably lower heat capacity of the MD simulated glasses.

## 4. Discussion

Lithium borate glasses are of great interest because of their good ionic conductance proper- ties. In an attempt to understand this superionic conductivity we have investigated the influence of the $Li_{2}O$ content on the glass structure by means of X-ray spectroscopy and MD calculations.

The interpretation of X-ray spectra cannot be unique because always more than one structural model can be used to explain the results. MD simulations do provide a unique glass structure; it is not certain, however, that this structure repre- sents the real glass because of the limitations (inevitable high quench rate) and approximations (non-quantum-mechanical approach, application of two-particle interactions) of the method.

The combined analysis of the results of the two methods may diminish the disadvantages men- tioned above.

We have compared the X-ray diffraction spec- tra with the radial distribution functions obtained by MD calculations and come to the conclusion that the structure of lithium borate glass predomi- nantly consists of more or less randomly con- nected $BO_{3}$ and $BO_{4}$ units. As for pure v-$B_{2}O_{3}$ [2] the quench rate is an important factor for the final glass structure. The differences found between the slowly and the fastly quenched glasses can be

explained quite well assuming a preponderance for the B-O-B angles to $120^{\circ}$ as the quench rate is decreased. This preferential angle however does not necessarily lead to the formation fo six-membered boroxol and borate rings. The existence of these structural groupings in borate glasses is not excluded but we think that at most a few percent of the atoms are involved in these structures.

We are aware of the fact that his picture of the glass structure is not in line with the generally accepted Krogh-Moe model [12]. It has to be pointed out that it has been shown before that the radial distribution functions of pure $v-B_{2} O_{3}$ obtained by X-ray diffraction studies and by neutron scattering experiments can be explained very well by a structural model consisting solely of triangular $BO_{3}$ units [13-15].

In this paper we have shown that the NMR data are also in agreement with our structural model. In fact the only clue for the existence of boroxol and borate rings is found in the Raman spectra of borate glasses. Because Raman spectra do not provide information on the absolute scattering intensity of the glass, the strong Raman bands at 800 and $780 \mathrm{~cm}^{-1}$ may result from structural groupings (e.g. boroxol rings and borate rings) which only form a very minor fraction of the total glass structure.

As pointed out before, MD calculations have limited value for the simulation of diffusion processes in glass at ambient temperatures. The computational speed of todays fastest computers is many orders of magnitude to slow for a reliable simulation of these processes. At $6000 \mathrm{~K}$ we observe the diffusion constant $D$ to be $D=0.3$ $\mathrm{nm}^{2} / \mathrm{ps}$ for $\mathrm{Li}^{+}$ions and $0.06 \mathrm{~nm}^{2} / \mathrm{ps}$ for $\mathrm{B}$ and $\mathrm{O}$ atoms. Assuming the diffusion constant to vary with temperature as

$$
D=D_{0} \exp (-E / k T), \tag{16}
$$

then $D$ will have at $T=300 \mathrm{~K}$ a magnitude of about $10^{-30} \mathrm{~nm}^{2} / \mathrm{ps}$, where we have used a typical value of $E=200 \mathrm{~kJ} / \mathrm{mol}(2.1 \mathrm{eV})$.

Although a simulation of the atomic transport processes at ambient temperatures is still a dream, even so something can be said about the nature of these processes. The deviation from $P_{\alpha}=1$ for $\mathrm{Li}^{+}$ions at $T=300 \mathrm{~K}$ endorses the ionic conductivity models in which the $\mathrm{Li}^{+}$ions are assumed to be weakly bound to $\mathrm{BO}_{4}$ groups and to hop easily from one interstitial position to another.

The vibrational properties of borate glasses have, by our knowledge, not been investigated before by MD calculations. Soules [3] reports the vibrational frequencies of some atoms in MD simulations but these data only represents the rate at which atoms change direction.

The calculated dynamical structure factors (fig. 6) do not open much perspective to more knowledge about the vibrational properties of borate glasses. As far as there exist any non-zero-frequency phonons in the simulated glasses, their presence is overshadowed by the anharmonical oscillations of the atoms involved. These results might be improved if the duration of the simulations is prolonged to 10 or 100 ps.

A direct analysis of the vibrations of nearest-neighbour atom pairs however appears to be more successful. Where the density of states spectra of B-B pairs and O-O pairs show one broad band between 0 and $1500 \mathrm{~cm}^{-1}$, the B-O spectrum agrees qualitatively with IR spectra.

This work forms part of the research program of the "Stichting Fundamenteel Onderzoek der Materie - FOM" and is financially supported by the "Nederlandse Organisatie voor Zuiver Wetenschappelijk Onderzoek" (Netherlands Organisation for the Advancement of Pure Research - ZWO). The MD simulations on the Amsterdam CYBER 205 were made possible by financial support from the "Werkgroep Gebruik Supercomputers".

## References

[1] J. Wong, in: Borate Glasses, Structure, Properties, Applications, eds. L.D. Pye et al. (Plenum, New York, 1978) p. 297.
[2] W. Soppe, C. van der Marel, W.F. van Gunsteren and H.W. den Hartog, J. Non-Cryst. Solids, to be published.
[3] T.F. Soules, J. Non-Cryst. Solids 49 (1982) 29.
[4] W. Soppe, F. Aldenkamp and H.W. den Hartog, J. Non-Cryst. Solids 91 (1987) 351.
[5] W. Soppe, J. Kleerebezem and H.W. den Hartog, J. Non-Cryst. Solids 93 (1987) 142.

[6] M.P. Tosi and F.G. Fumi, J. Phys. Chem. Solids 25 (1964) 45.

[7] T.F. Soules, J. Chem. Phys. 73 (1980) 4032.

[8] S.A. Feller et al., J. Non-Cryst. Solids 51 (1982) 21.

[9] A. Rahman, Phys. Rev. 136 (1964) 405.

[10] J. Moscinski and P.W.M. Jacobs, Physica 131B (1985) 175.

[11] M.J. Gillan, Physica 131B (1985) 157.

[12] D.L. Griscom, in: Borate Glasses, Structure, Properties,
Applications", eds L.D. Pye et al. (Plenum, New York, 1978) p. 11.

[13] S.R. Elliot, Phil. Mag. B37 (1978) 435.

[14] S.J. Williams and S.R. Elliot, in: The Structure of Non-Crystalline Materials, eds. P.H. Gaskell et al. (Taylor and Francis, London, 1983) p. 407.

[15] M. Amini, S.K. Mitra and R.W. Hockney, J. Phys. C 14 (1981) 3689.
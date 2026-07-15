![](./images/812677210228916224_1.jpg)

Philosophical Magazine

ISSN: 1478-6435 (Print) 1478-6443 (Online) Journal homepage: https://www.tandfonline.com/loi/tphm20

First-principles study of structural, elastic,
electronic and optical properties of RDX under
pressure

Sheng-Hai Zhu, Han Qin, Wei Zeng, Fu-Sheng Liu, Bin Tang, Qi-Jun Liu, Ruo-Xi
Li & Yun-Dan Gan

To cite this article: Sheng-Hai Zhu, Han Qin, Wei Zeng, Fu-Sheng Liu, Bin Tang, Qi-Jun Liu,
Ruo-Xi Li & Yun-Dan Gan (2020): First-principles study of structural, elastic, electronic and optical
properties of RDX under pressure, Philosophical Magazine, DOI: 10.1080/14786435.2020.1725679

To link to this article: https://doi.org/10.1080/14786435.2020.1725679

![](./images/812677210228916224_2.jpg)
View supplementary material

![](./images/812677210228916224_3.jpg)
Published online: 15 Feb 2020.

![](./images/812677210228916224_4.jpg)
Submit your article to this journal

![](./images/812677210228916224_5.jpg)
View related articles

![](./images/812677210228916224_6.jpg)
View Crossmark data

Full Terms & Conditions of access and use can be found at
https://www.tandfonline.com/action/journalInformation?journalCode=tphm20

First-principles study of structural, elastic, electronic and
optical properties of RDX under pressure

Sheng-Hai Zhu ${ }^{a,b}$, Han Qin ${ }^{a,b}$, Wei Zeng ${ }^{c}$, Fu-Sheng Liu ${ }^{a,b}$, Bin Tang ${ }^{d}$,
Qi-Jun Liu ${ }^{a,b}$, Ruo-Xi Li ${ }^{a}$ and Yun-Dan Gan ${ }^{e}$

${ }^{a}$ School of Physical Science and Technology, Southwest Jiaotong University, Key Laboratory of
Advanced Technologies of Materials, Ministry of Education of China, Chengdu, People's Republic of
China; ${ }^{\mathrm{b}}$ Bond and Band Engineering Group, Sichuan Provincial Key Laboratory (for Universities) of High
Pressure Science and Technology, Southwest Jiaotong University, Chengdu, People's Republic of
China; ${ }^{\mathrm{c}}$ Teaching and Research Group of Chemistry, College of Medical Technology, Chengdu
University of Traditional Chinese Medicine, Chengdu, People's Republic of China; ${ }^{\mathrm{d}}$ State Key
Laboratory of Solidification Processing, Northwestern Polytechnical University, Xi'an, People's Republic
of China; ${ }^{\mathrm{e}} \mathrm{Xi}$ 'an Modern Chemistry Research Institute, Xi'an, People's Republic of China

**ABSTRACT**
The influences of pressure on structural, elastic, electronic and
optical properties of $\alpha$-RDX under pressure from 0 to 40 GPa
have been investigated by performing first-principles
calculations. The obtained structural parameters based on
the GGA-PBE+G calculations are consistent with previous
experimental values. The results of $B/G$, $C_{12}$-$C_{44}$ and
Poisson's ratio show that $\alpha$-RDX has changed to ductility
under pressure between 0 and 5 GPa. The obvious rotation
of $\text{NO}_2$ group in the equatorial position appears, especially
in the range of pressure from 10 to 15 GPa, which influences
the elastic and mechanical properties of $\alpha$-RDX. Moreover,
we find that the electrons of $\alpha$-RDX become more active
under higher pressure by comparing the curves of DOS
under different pressure. Furthermore, the anisotropy of
optical properties under different pressures has been shown.

**ARTICLE HISTORY**
Received 7 March 2019
Accepted 28 January 2020

**KEYWORDS**
RDX; first-principles
calculations; mechanical
properties; electronic
structure; optical properties

## 1. Introduction

RDX is one of frequently used high explosives [1–3], which can also be used in
high-energy propellants and mixed explosives such as plastic explosives [4]. In
the fields of industrial and civil applications, they have penetrated into various
products such as detonators, detonating cords, perforating bullets, etc.

From experimental and theoretical researches on RDX, we have known that
there are six crystal phases including $\alpha$, $\beta$, $\gamma$, $\delta$, $\varepsilon$ and $\zeta$ [5–12]. Among them,
$\alpha$-RDX is a room temperature and ambient-pressure phase, which has

**CONTACT** Han Qin hanqin1108@163.com School of Physical Science and Technology, Southwest Jiaotong
University, Chengdu, Sichuan 610031, People's Republic of China; Qi-Jun Liu qijunliu@home.swjtu.edu.cn
School of Physical Science and Technology, Southwest Jiaotong University, Chengdu, Sichuan 610031, People's
Republic of China

Supplemental data for this article can be accessed https://doi.org/10.1080/14786435.2020.1725679
© 2020 Informa UK Limited, trading as Taylor & Francis Group

orthorhombic structure with space group $Pbca$ and eight molecules including 168 atoms. According to the position of the nitro group relative to the ring, the molecular configuration of $\alpha$-RDX is defined as AAE conformation [5-7]. $\beta$-RDX is a metastable phase with the AAA conformation, which can be obtained by solution deposition or sublimation recrystallisation [8,9]. It can be easily converted to $\alpha$-RDX under contact with $\alpha$-RDX or by needle contact [8-11]. $\beta$-RDX was once considered as the HP-HT polymorph [10], but Dreger et al. used Raman spectroscopy to study the HP-HT polymorph of RDX and obtained different results [11]. By comparing the Raman spectra of $\beta$-RDX and HP-HT polymorph, they found that the Raman spectrum of $\beta$-RDX and HP-HT polymorph were quite different, especially the lattice vibration modes. The generated phase at HP-HT (4.2 GPa, 489 K) has been named $\varepsilon$-RDX [11]. Ciezak et al. successfully obtained Raman and Infrared spectroscopy of RDX under high pressure [5]. They found that the Raman peak of RDX would show significant changes such as large frequency shift, mode split or intensity change when the pressure reached 4 GPa, indicating that RDX was changed from $\alpha$-form to $\gamma$-form. $\gamma$-RDX can be stable below 18 GPa, but there is a new Raman peak between 17.8 and 18.8 GPa along with the emergence of a new phase. The structure of new phase is similar to $\beta$-form, but has slightly different in the C-H stretch vibration mode region, confirming that the transition from $\gamma$-RDX to $\delta$-RDX occurs at around 18 GPa [5]. In addition, Gao et al. found a new phase ($\zeta$) at around 28 GPa with evidence of new $\mathrm{NO_2}$ rotation, C-H stretch, molecular bend and ring vibration modes. They also suggested that another new phase ($\eta$-RDX) might exist above 38 GPa, but it would need further confirmation [12].

Due to some important properties are experimentally difficult to gain under pressure, the theoretical investigations have been used to make a better understanding of the effects of pressure on RDX. Sorescu et al. performed theoretical predictions of the responses to the lattice parameters to pressure for 10 energetic molecular crystals, including $\alpha$-RDX and $\gamma$-RDX [13]. They concluded that the DFT-D (dispersion-corrected density functional theory) method as parameterisation by Grimme [14] which provided effective improvements for the characterisation of intermolecular interactions in crystals relative to conventional DFT at high pressure. In a subsequent study, DFT-D was also recommended by Fan et al. as the most reliable method for DFT calculations of energetic materials [15]. The following issue is necessary to understand its performances under ambient conditions or extreme conditions such as detonation pressure and chemical decomposition conditions. Knowledge of the mechanical response of RDX to dynamic loading is important due to that chemical decomposition and structural deformation are interdependent. In addition, the electronic structure can be affected by external pressure [16,17]. It is well known that the optical properties of crystals are related to their electronic structures, which are obtained by employing optical methods [18,19]. Herein, we focus on the structural, elastic, electronic and optical properties of $\alpha$-RDX in the pressure range of 0-40 GPa.

## 2. Computational methods

First-principles calculations were carried out with the norm-conserving pseudo-potential method. Cambridge Serial Total Energy Package code (CASTEP) [20] based on DFT was employed for the calculations. Generalised gradient approximation (GGA) with Perdew-Burke-Ernzerhof (PBE) [21] was used to trace the exchange-correlation energy function. The C $2s^22p^2$, N $2s^22p^3$, O $2s^22p^4$ and H $1s^1$ electrons were particularly treated as the valence shells. The plane wave cut-off energy of 830 eV was adopted. Brillouin-zone integrations were modelled by using a Monkhorst-Pack k-point mesh [22]. The convergence criterion of the change in total energy was less than $5.0 \times 10^{-6}$ eV/atom. The DFT-D method was employed to solve the van der Waals interactions in molecular crystals, where the G (Grimme) [14] corrections to GGA-PBE have been applied.

## 3. Results and discussion

### 3.1. The structural parameters

Orthorhombic α-RDX with Pbca space group includes eight molecules (168 atoms) per unit cell, whose crystal structure is shown in Figure 1. The calculated structural volume [23] of solid RDX is depicted in Figure 2 along with the previous theoretical and experimental data [2,13,24–31]. The anastomotic value of the experiments [24,25] shows the accuracy of the present structure calculations. Moreover, the calculated lattice constants of α-RDX together with the available experimental data and other theoretical data are tabulated in Table 1 [2,13,24–

![](./images/812677210228916224_7.jpg)

Figure 1. Crystal structures of α-RDX (The order of atomic radius from small to large is H-C-N-O).

![](./images/812677210228916224_8.jpg)

Figure 2. Calculated structural volume of α-RDX along with the previous experimental and theoretical data [2,13,24–31].

<table>
<caption>Table 1. Calculated lattice constants of α-RDX together with the available experimental data and other theoretical data [2,13,24–31].</caption>
<thead>
<tr>
<th></th>
<th>$a$ (Å)</th>
<th>$b$ (Å)</th>
<th>$c$ (Å)</th>
</tr>
</thead>
<tbody>
<tr>
<td>This work</td>
<td>11.5003</td>
<td>10.7929</td>
<td>13.3680</td>
</tr>
<tr>
<td>Exp. [25]</td>
<td>11.4195</td>
<td>10.5861</td>
<td>13.1401</td>
</tr>
<tr>
<td>Exp. [24]</td>
<td>13.182</td>
<td>11.574</td>
<td>10.709</td>
</tr>
<tr>
<td>Ref. [26]</td>
<td>13.353</td>
<td>11.455</td>
<td>10.794</td>
</tr>
<tr>
<td>Ref. [26]</td>
<td>13.164</td>
<td>11.532</td>
<td>10.593</td>
</tr>
<tr>
<td>Ref. [13]</td>
<td>13.237</td>
<td>11.391</td>
<td>10.770</td>
</tr>
<tr>
<td>Ref. [27]</td>
<td>13.282</td>
<td>11.419</td>
<td>10.736</td>
</tr>
<tr>
<td>Ref. [28]</td>
<td>13.330</td>
<td>11.497</td>
<td>10.532</td>
</tr>
<tr>
<td>Ref. [29]</td>
<td>13.688</td>
<td>11.933</td>
<td>11.538</td>
</tr>
<tr>
<td>Ref. [2]</td>
<td>13.778</td>
<td>12.03</td>
<td>10.961</td>
</tr>
<tr>
<td>Ref. [30]</td>
<td>13.904</td>
<td>12.044</td>
<td>10.896</td>
</tr>
<tr>
<td>Ref. [31]</td>
<td>13.341</td>
<td>11.506</td>
<td>10.791</td>
</tr>
</tbody>
</table>

31]. It is worth noting that our geometrically optimised crystal structure is based on the experimental structure of Ref. [25], the axes of a, b and c of our model correspond to the axes of b, c and a of other previous study, respectively.

The effects of pressure on lattice parameters are shown in Figure 3(a). We can observe that the compression used on the crystal decreases the lattice parameters monotonically. The normalised lattice parameters as functions of pressure are also depicted in Figure 3(a), it is distinct that the compressibility along the c-axis is weaker than that along the a/b-axis. The compressibility from 0 to 10 GPa along the b-axis is stronger than that along the a-axis, but it is contrary from 15 to 40 GPa. As a result, the lattice parameter of a-axis is infinitely close to that of b-axis at 40 GPa. The different level of compressibility is related to

![](./images/812677210228916224_9.jpg)

Figure 3. (a) Calculated lattice parameters and normalised lattice parameters and (b) XRD patterns of RDX under pressure from 0 to 40 GPa.

different resistances under pressure. The high compressibility in the a-axis direction under high pressure indicates the weaker resistance and the more malleable direction. On the contrary, the c-axis direction shows the highest stiffness. Moreover, the calculated XRD (X-ray diffraction) patterns of RDX under high pressures up to 40 GPa are shown in Figure 3(b). With compression loading, some new peaks occur at 5 GPa. This indicates that new phase emerges under pressure

from 0 to 5 GPa, which corresponds to the phase transition in the XRD patterns of Gao et al. [12].

In order to directly study the influence of pressure on atoms, we plot the atomic motion path in the three-dimensional image under compression in Figure 4. The most obvious movement is the rotation of $\text{NO}_2(\text{E})$ group ($\text{NO}_2$ group in the equatorial position). The preliminary rotation is comparatively easy, especially between 10 and 15 GPa. When the pressure is higher than 15 GPa, the rotation becomes more and more difficult with the increasing pressure. Further analysis of the 3D image, with the increasing pressure, other groups also have a similar moving trend as the $\text{NO}_2(\text{E})$ group, but the moving distance of each group is different. The larger value of the moving distance is, the stronger sensitivity of the atoms to pressure is. As shown in Figure 4, H2B and H3B exhibit more intense sensitivity than other atoms except O6, O5 and N6.

### 3.2. Elastic and mechanical properties

The elastic and mechanical properties are important to study the effects of external conditions on the reaction of crystal RDX. Orthorhombic structure of solid RDX has nine independent elastic constants, named $\text{C}_{11}$, $\text{C}_{12}$, $\text{C}_{13}$, $\text{C}_{22}$, $\text{C}_{23}$, $\text{C}_{33}$, $\text{C}_{44}$, $\text{C}_{55}$ and $\text{C}_{66}$. The calculated elastic constants of $\alpha$-RDX under pressure from 0 to 40 GPa are listed in Table 2 [23]. When its strain energy is positive against any homogeneous elastic deformation, the material is mechanical stability [32,33]. For orthorhombic crystals, the mechanical stability criterion under pressure can be expressed as follows [34,35]:

$$
\begin{aligned}
&\mathrm{C}_{11}-P>0, \mathrm{C}_{22}-P>0, \mathrm{C}_{33}-P>0, \mathrm{C}_{44}-P>0, \mathrm{C}_{55}-P>0, \mathrm{C}_{66}-P>0, \\
&\mathrm{C}_{11}+\mathrm{C}_{22}+\mathrm{C}_{33}+2\left(\mathrm{C}_{12}+\mathrm{C}_{13}+\mathrm{C}_{23}\right)+3 P>0, \mathrm{C}_{11}+\mathrm{C}_{22}-2 \mathrm{C}_{12}-4 P>0, \\
&\mathrm{C}_{11}+\mathrm{C}_{33}-2 \mathrm{C}_{13}-4 P>0, \mathrm{C}_{22}+\mathrm{C}_{33}-2 \mathrm{C}_{23}-4 P>0
\end{aligned}
$$

![](./images/812677210228916224_10.jpg)

Figure 4. Atomic motion path in 3D image under compression.

**Table 2.** The calculated elastic constants of α-RDX under pressure from 0 to 40 GPa.

<table>
  <thead>
    <tr>
      <th rowspan="2">Pressure(GPa)</th>
      <th colspan="9">Cᵢⱼ (GPa)</th>
    </tr>
    <tr>
      <th>C₁₁</th>
      <th>C₁₂</th>
      <th>C₁₃</th>
      <th>C₂₂</th>
      <th>C₂₃</th>
      <th>C₃₃</th>
      <th>C₄₄</th>
      <th>C₅₅</th>
      <th>C₆₆</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>30.94</td>
      <td>5.06</td>
      <td>10.26</td>
      <td>30.48</td>
      <td>4.58</td>
      <td>34.34</td>
      <td>8.45</td>
      <td>11.73</td>
      <td>7.61</td>
    </tr>
    <tr>
      <td>5</td>
      <td>74.51</td>
      <td>35.47</td>
      <td>35.14</td>
      <td>70.60</td>
      <td>24.68</td>
      <td>94.93</td>
      <td>14.41</td>
      <td>16.38</td>
      <td>22.38</td>
    </tr>
    <tr>
      <td>10</td>
      <td>81.85</td>
      <td>58.86</td>
      <td>52.65</td>
      <td>106.92</td>
      <td>43.23</td>
      <td>133.72</td>
      <td>18.90</td>
      <td>25.47</td>
      <td>29.36</td>
    </tr>
    <tr>
      <td>15</td>
      <td>122.07</td>
      <td>84.12</td>
      <td>66.12</td>
      <td>143.97</td>
      <td>60.15</td>
      <td>174.72</td>
      <td>28.93</td>
      <td>43.39</td>
      <td>38.45</td>
    </tr>
    <tr>
      <td>20</td>
      <td>145.78</td>
      <td>105.65</td>
      <td>81.91</td>
      <td>180.46</td>
      <td>76.90</td>
      <td>204.22</td>
      <td>32.72</td>
      <td>50.40</td>
      <td>42.85</td>
    </tr>
    <tr>
      <td>25</td>
      <td>174.00</td>
      <td>129.16</td>
      <td>100.10</td>
      <td>209.45</td>
      <td>96.08</td>
      <td>236.17</td>
      <td>33.93</td>
      <td>57.41</td>
      <td>50.33</td>
    </tr>
    <tr>
      <td>30</td>
      <td>202.16</td>
      <td>146.86</td>
      <td>112.63</td>
      <td>238.75</td>
      <td>110.56</td>
      <td>265.79</td>
      <td>36.18</td>
      <td>63.05</td>
      <td>58.43</td>
    </tr>
    <tr>
      <td>35</td>
      <td>224.41</td>
      <td>166.45</td>
      <td>127.17</td>
      <td>269.42</td>
      <td>129.90</td>
      <td>290.82</td>
      <td>37.80</td>
      <td>68.10</td>
      <td>64.98</td>
    </tr>
    <tr>
      <td>40</td>
      <td>248.15</td>
      <td>184.48</td>
      <td>140.31</td>
      <td>294.96</td>
      <td>142.12</td>
      <td>317.50</td>
      <td>39.71</td>
      <td>73.04</td>
      <td>73.04</td>
    </tr>
  </tbody>
</table>

As shown in Table 2, the calculated independent elastic constants of α-RDX under pressure satisfy the above corresponding criteria, indicating that it is mechanically stable from 0 to 40 GPa. Moreover, the principal elastic constants $C_{11}$, $C_{22}$, and $C_{33}$ of crystals are related to the compression along the crystal axes a, b and c, respectively. From Table 2, the calculated $C_{33}$ is obviously larger than $C_{11}$ and $C_{22}$ in the pressure range of 0–40 GPa, indicating that the stiffest direction is along the c-axis. In previous experiments and calculations, there are fewer researches on the elastic constant of α-RDX under high pressure, $C_{11}$ is the largest of the three constants under ambient conditions [36–41], demonstrating that along the a-axis in these experiments and calculations is the stiffest direction. As mentioned in 3.1, the c-axis of our RDX model corresponds to the a-axis of other previous study, showing that our calculations of elastic constants are consistent with the previous researches. This conclusion is in good agreement with the above argumentum of compressibility in α-RDX. In order to observe the variation tendency of these elastic constants clearly with increasing pressure, we depict the calculated elastic constants of α-RDX as functions of pressure in Fig. S1. As shown in Fig. S1, all the independent elastic constants increase with the increasing pressure. Further analysis of $C_{11}$ and $C_{22}$, the calculated $C_{11}$ is slightly larger than $C_{22}$ in the pressure range of 0–5 GPa, but it is opposite from 5 to 40 GPa. The results indicate that the compressibility along the a-axis is more compressible than that along the b-axis under the pressure above 5 GPa. For the other diagonal elastic constants, the order of $C_{55} > C_{44} > C_{66}$ under zero pressure indicates the stiffest and the softest shear transformations along the (010) and (001) directions at ambient conditions. As the pressure increases, the softest direction of shear transformations changes to the a-axis. For the stiffest direction, $C_{55}$ and $C_{66}$ exchange the leading position twice with increasing pressure. Coincidentally, the point of $C_{55}$ and $C_{66}$ exactly overlap under 40 GPa.

According to the obtained independent elastic constants, we calculate the mechanical properties of α-RDX including bulk modulus (B), shear modulus (G), Young's modulus (E) and Poisson's ratio (v). The modulus is evaluated

by the Voigt method and the Reuss method [33]. They are given by

$$
B_{V}=\frac{C_{11}+C_{22}+C_{33}+2\left(C_{12}+C_{13}+C_{23}\right)}{9}
$$

$$
G_{V}=\frac{C_{11}+C_{22}+C_{33}-C_{12}-C_{13}-C_{23}+3\left(C_{44}+C_{55}+C_{66}\right)}{15}
$$

$$
B_{R}=\frac{1}{S_{11}+S_{22}+S_{33}+2\left(S_{12}+S_{13}+S_{23}\right)}
$$

$$
G_{R}=\frac{15}{4\left(S_{11}+S_{22}+S_{33}\right)-4\left(S_{12}+S_{13}+S_{23}\right)+3\left(S_{44}+S_{55}+S_{66}\right)}
$$

where the $S_{ij}$ is elastic compliance constants. The arithmetic average of the Voigt and the Reuss values is called Voigt-Reuss-Hill (VRH) average [33,42]. It can be expressed as

$$
B_{H}=\frac{1}{2}\left(B_{V}+B_{R}\right)
$$

$$
G_{H}=\frac{1}{2}\left(G_{V}+G_{R}\right)
$$

Besides, Young's modulus ($E$) and Poisson's ratio ($v$) are obtained according to the following formula [42]:

$$
E=\frac{9 B G}{3 B+G}
$$

$$
v=\frac{3 B-2 G}{2(3 B+G)}
$$

The calculated results of α-RDX under pressure up to 40 GPa are tabulated in Table 3. The bulk modulus, shear modulus and Young's modulus are usually considered as a measurement of resistance deformation capacity, resistance shear deformation capacity and rigidity of the materials, respectively [33,43]. The larger value is, the stronger capacity is [43]. In order to observe the change of modulus with the increasing pressure clearly, the curves of bulk modulus, shear modulus and Young's modulus under pressure up to 40 GPa

Table 3. The bulk modulus (B, GPa), shear modulus (G, GPa), B/G, Young's modulus (E, GPa), Poisson's ratio (v) and $C_{12}$-$C_{44}$ of α-RDX under pressure from 0 to 40 GPa.

<table>
<thead>
  <tr>
    <th></th>
    <th>B<sub>H</sub></th>
    <th>G<sub>H</sub></th>
    <th>B<sub>H</sub>/G<sub>H</sub></th>
    <th>E</th>
    <th>v</th>
    <th>C<sub>12</sub>-C<sub>44</sub></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>0</td>
    <td>14.98</td>
    <td>10.34</td>
    <td>1.45</td>
    <td>25.22</td>
    <td>0.22</td>
    <td>–3.39</td>
  </tr>
  <tr>
    <td>5</td>
    <td>47.55</td>
    <td>19.61</td>
    <td>2.42</td>
    <td>51.72</td>
    <td>0.32</td>
    <td>21.06</td>
  </tr>
  <tr>
    <td>10</td>
    <td>69.46</td>
    <td>24.59</td>
    <td>2.82</td>
    <td>65.98</td>
    <td>0.34</td>
    <td>39.96</td>
  </tr>
  <tr>
    <td>15</td>
    <td>95.38</td>
    <td>36.00</td>
    <td>2.65</td>
    <td>95.93</td>
    <td>0.33</td>
    <td>55.19</td>
  </tr>
  <tr>
    <td>20</td>
    <td>117.15</td>
    <td>41.17</td>
    <td>2.85</td>
    <td>110.56</td>
    <td>0.34</td>
    <td>72.93</td>
  </tr>
  <tr>
    <td>25</td>
    <td>140.61</td>
    <td>45.74</td>
    <td>3.07</td>
    <td>123.80</td>
    <td>0.35</td>
    <td>95.23</td>
  </tr>
  <tr>
    <td>30</td>
    <td>160.25</td>
    <td>51.56</td>
    <td>3.11</td>
    <td>139.70</td>
    <td>0.35</td>
    <td>110.68</td>
  </tr>
  <tr>
    <td>35</td>
    <td>180.48</td>
    <td>55.59</td>
    <td>3.25</td>
    <td>151.24</td>
    <td>0.36</td>
    <td>128.65</td>
  </tr>
  <tr>
    <td>40</td>
    <td>198.61</td>
    <td>60.28</td>
    <td>3.29</td>
    <td>164.23</td>
    <td>0.36</td>
    <td>144.77</td>
  </tr>
</tbody>
</table>

are depicted in Fig. S2. As shown in Fig. S2, these values of mechanical properties increase with increasing pressure, which indicates that all of the resistance to deformation capacity, resistance to shear deformation capacity and rigidity of the materials are stronger under high pressure. Moreover, the curves demonstrate that bulk modulus has the largest rate of increase, and then followed by Young's modulus and shear modulus. From Table 3, the increases of the $B$, $G$ and $E$ of $\alpha$-RDX are about 1225.83%, 482.98% and 551.23% from 0 to 40 GPa, respectively. Furthermore, Poisson's ratio ($v$) and the ratio of bulk modulus to shear modulus ($B/G$) of polycrystalline phases are used to predicate the ductile and brittle behaviours of materials [43-45]. The larger value of Poisson's ratio is, the better plasticity is [43]. The critical value used to separate brittleness from ductility of $v$ is about 0.26 [44]. If $v > 0.26$, the material shows a ductile manner, otherwise it is brittle. The critical value of $B/G$ is 1.75, which distinguishes between brittle and ductile phase [45]. A high value of $B/G$ is associated with ductility, whereas low value exhibits brittleness. The calculated Poisson's ratio ($v$) and $B/G$ of $\alpha$-RDX as functions of pressure are depicted in Figure 5. As we can see, both $v$ and $B/G$ are lower than their respective critical value at 0 GPa, which indicate that $\alpha$-RDX is brittle at ambient conditions. On the overall trend, these values increase with the increasing pressure. As shown in Figure 5, starting before 5 GPa, $\alpha$-RDX has transformed from brittleness to ductility. It is notable that the values of $v$ and $B/G$ all decrease exceptionally from 10 to 15 GPa, and we attribute this anomaly to the marked rotation of $\mathrm{NO}_{2}(\mathrm{E})$ group between 10 and 15 GPa. In addition, the value of $\mathrm{C}_{12}$-$\mathrm{C}_{44}$ can also define the ductility (brittleness) of crystal [46]. If the value is positive, indicating that the phase is ductile, otherwise it shows a brittle manner. From Table 3, the $\mathrm{C}_{12}$-$\mathrm{C}_{44}$ value of $\alpha$-RDX is negative at 0 GPa, while it is positive under pressure

![](./images/812677210228916224_11.jpg)

Figure 5. Calculated Poisson's ratio ($v$) and $B/G$ of $\alpha$-RDX as functions of pressure.

above 5 GPa. Therefore, α-RDX has changed to ductility under pressure between 0 and 5 GPa. And the findings also support the above discussion.

### 3.3. Electronic structures

The effects of pressure on energy bands of α-RDX based on the GGA-PBE + G are calculated and are depicted in Figure 6. The entire valence-band maximum is 0 eV appearing on the X point under pressure from 0 to 40 GPa, and the conduction-band minimum is 3.444 eV appearing on the direction of S→X at 0 GPa [23]. The obtained bandgap of 3.444 eV is quite close to the experimental data 3.40 eV [18] reported by Marinkas. As shown in Figure 6, the bandgap of α-RDX decreases with the increasing pressure, and the obtained value at 40 GPa equals 2.614 eV, indicating that the electron transitions of α-RDX become easier under higher pressure.

The calculated total densities of states (TDOS) of α-RDX under pressure from 0 to 40 GPa are depicted in Figure 7 and the partial densities of states (PDOS) at 0 GPa with 40 GPa are plotted in Figure 8, respectively. Comparing the curves from 0 to 40 GPa, the TDOS dispersion of α-RDX increases with the increasing hydrostatic pressure while the peaks of TDOS decrease on the whole trend, which also indicates the electrons of α-RDX are more active under hydrostatic pressure. It is noticeable that the peaks near −21 eV, −13 eV, −10 and 4 eV decrease exceptionally from 10 to 15 GPa, as shown in Figure 8, these regions are dominated by the N-p and O-s/p states. Therefore, these abnormal changes are attributed to the obvious rotation of NO₂(E) group between 10 and 15 GPa as mentioned above. Further analysis of the curves of PDOS, the lower region is dominated by the N (4,5,6)-s and O (1~6)-s states. The second zone around the peak at −20 eV is mainly consisted of d states of O (1~6)-s and N (4,5,6)-p. The third peak near −19 eV is dominated by the s orbital of N (1,2,3) and C (1,2,3). The fourth peak near −17 eV is mainly consisted of N (1,2,3)-s, N (4,5,6)-p and C (1,2,3)-s/p. The fifth peak at −12.5 eV

![](./images/812677210228916224_12.jpg)

Figure 6. Effects of pressure on energy bands of α-RDX.

![](./images/812677210228916224_13.jpg)

Figure 7. The total densities of states (TDOS) of α-RDX under pressure from 0 to 40 GPa.

is dominated by the C (1,2,3)-s and N (1~6)-p with contributions of s orbital of H, O and N atoms. The next region from −10 eV to −6 eV is dominated by the p orbital of C, O and N atoms with contributions of the s orbital of C, H, O and N atoms. The seventh zone from −6 eV to −3 eV is mainly consisted of C (1,2,3)-p and H-s states. The eighth region from −2.5 eV to Fermi level is dominated by the p orbital of O and N atoms. The peak in conduction band near the Fermi level is mainly contributed by the p orbital of O and N atoms. Comparing the curves of PDOS at 0 and 40 GPa, it can be seen that the rate of curve superposition of similar atoms is higher at 0 GPa. We attribute this phenomenon to the rotation of the atomic groups under high pressure, which destroys the atomic symmetry inside the crystal of α-RDX.

### 3.4. Optical properties

The calculated optical properties of α-RDX under compression are plotted in Figs. S3-S7 and Figure 9. It is well known that the space group of RDX allows one to evaluate three independent components, the polarisation direction (100) component, the polarisation direction (010) component and the polarisation direction (001) component, which indicates the optical anisotropy for α-RDX.

The real part and imaginary part of the obtained dielectric functions of α-RDX under pressure are shown in Fig. S3. The real part $\varepsilon_{1(100)}$ has two main peaks. When the hydrostatic pressure increases from 0 to 40 GPa, the photon energy of the maximal peak of the polarisation direction (100) decreases from 3.58 to 2.98 eV, and the corresponding intensity increases from 4.61 to 6.41. For the imaginary part $\varepsilon_{2(100)}$, when the hydrostatic pressure varies from 0 to 40 GPa, the photon energy of the maximal peak of the polarisation direction

![](./images/812677210228916224_14.jpg)

![](./images/812677210228916224_15.jpg)

Figure 8. The partial densities of states (PDOS) at 0 GPa (a) with 40 GPa (b).

![](./images/812677210228916224_16.jpg)

Figure 9. The absorption coefficient of α-RDX for polarisation direction (100), (010) and (001) under pressure from 0 to 40 GPa.

(100) decreases from 4.51 to 3.98 eV, and its intensity increases from 2.97 to 4.52. This indicates that the pressure has an effect on photon energy and electron transition. Further analysis of the polarisation direction (010) component and the polarisation direction (001) component, their variation differs from that of direction (100), but the trend is generally similar.

The complex refractive indexes of α-RDX crystal under compression are shown in Fig. S4. The curves of refractive index are similar to that of real dielectric function. When the pressure increases from 0 to 40 GPa, the static refractive index n₍₁₀₀₎(0), n₍₀₁₀₎(0) and n₍₀₀₁₎(0) increase from 1.74 to 2.10, from 1.73 to 2.21 and from 1.77 to 2.20, respectively. Meanwhile, the photon energy of the maximal peaks of the polarisation direction (100), (010) and (001) decrease from 3.67 to 3.11 eV, from 4.40 to 3.48 eV and from 3.67 to 3.36 eV, and their intensities increase from 2.17 to 2.57, from 2.09 to 2.61 and from 2.22 to 2.65, respectively.

The calculated results of optical reflectivity R(ω) for α-RDX under different pressure are depicted in Fig. S5. It can be seen that all the curves have a strong peak near 4.2, 5.1 and 4.3 eV for the polarisation direction (100), (010) and (001), respectively. As shown in Figure 9, the rising edges of the peaks of

absorption spectrum under pressure of different levels occur at circa 3.0 eV, which are consistent with the experimental results by Whitley [19]. Figures S6 and S7 show the obtained energy-loss spectrum L(ω) and the complex conductivity function σ(ω) under different pressure, respectively. In general terms, the intensities of the maximal peaks increase with the increasing pressure. And we can observe that there is an optical anisotropy and the obtained values correspond to the space group of α-RDX.

## 4. Conclusions

In summary, we have investigated the influences of pressure on structural, elastic, electronic and optical properties by employing the first-principles method based on density-functional theory. The structural parameters and atomic-movement paths are obtained with the increasing pressure. The calculated structural volume under 0 GPa are in good agreement with previous experimental and theoretical values. As the pressure increases, the appearance of rotation of NO₂ group in the equatorial position has an influence on the physical properties of α-RDX, especially in the range of 10–15 GPa. The elastic and mechanical properties including independent elastic constants, mechanical stability, bulk modulus, shear modulus, Young’s modulus, Poisson’s ratio, C₁₂-C₄₄ and ratio of B/G under different pressure have been obtained and discussed. Moreover, comparing the DOS under pressure from 0 to 40 GPa, the electrons of α-RDX become more active under higher pressure. Finally, the intensities of the maximal peaks of six optical properties increase with the increasing pressure. And we can observe the existence of optical anisotropy.

## Disclosure statement

No potential conflict of interest was reported by the author(s).

## Funding

This work was supported by the National Natural Science Foundation of China [grant number 11574254], the Fundamental Research Funds for the Central Universities [grant number 2682019LK07], the fund of the State Key Laboratory of Solidification Processing in NWPU [grant number SKLSP201843], the Doctoral Innovation Fund Program of Southwest Jiaotong University [grant number D-CX201735], the Doctoral Students Top-notch Innovative Talent Cultivation of Southwest Jiaotong University, the 18th Laboratory Open Project of Southwest Jiaotong University [grant number ZD201918082].

## ORCID

Sheng-Hai Zhu http://orcid.org/0000-0001-7863-8651

Han Qin http://orcid.org/0000-0002-8719-9707

### References

[1] A.J. Davidson, I.D.H. Oswald, D.J. Francis, A.R. Lennie, W.G. Marshall, D.I.A. Millar, C.R. Pulham, J.E. Warren, and A.S. Cumming, *Explosives under pressure—the crystal structure of $\gamma$-RDX as determined by high-pressure X-ray and neutron diffraction*. Cryst. Eng. Comm. 10 (2008), pp. 162–165.

[2] A. Strachan, A.C.T. van Duin, D. Chakraborty, S. Dasgupta, and W.A. Goddard III, *Shock waves in high-energy materials: the initial chemical events in nitramine RDX*. Phys. Rev. Lett. 91 (2003), p. 098301.

[3] T.L. Andrew and T.M. Swager, *A fluorescence turn-on mechanism to detect high explosives RDX and PETN*. J. Am. Chem. Soc. 129 (2007), pp. 7254–7255.

[4] A. Elbeih, M. Jungova, S. Zeman, P. Vávra, and Z. Akštein, *Explosive strength and impact sensitivity of several PBXs based on attractive cyclic nitramines*. Propellants, Explos., Pyrotech. 37 (2012), pp. 329–334.

[5] J.A. Ciezak, T.A. Jenkins, Z. Liu, and R.J. Hemley, *High-pressure vibrational spectroscopy of energetic materials: Hexahydro-1, 5-trinitro-1, 3, 5-triazine*. J. Phys. Chem. A 111 (2007), pp. 59–63.

[6] Z.A. Dreger, M.D. McCluskey, and Y.M. Gupta, *High pressure–high temperature decomposition of $\gamma$-Cyclotrimethylene Trinitramine*. J. Phys. Chem. A 116 (2012), pp. 9680–9688.

[7] D.I.A. Millar, *Structural Studies of RDX, Energetic Materials at Extreme Conditions*, Springer, Berlin, Heidelberg, 2012.

[8] A.M. Figueroa-Navedo, J.L. Ruiz-Caballero, L.C. Pacheco-Londono, and S.P. Hernandez-Rivera, *Characterization of $\alpha$-and $\beta$-RDX polymorphs in crystalline deposits on stainless steel substrates*. Cryst. Growth Des. 16 (2016), pp. 3631–3638.

[9] C. Gao, L. Yang, Y. Zeng, X. Wang, C. Zhang, R. Dai, Z. Wang, X. Zheng, and Z. Zhang, *Growth and characterization of $\beta$-RDX single-crystal particles*. J. Phys. Chem. C 121 (2017), pp. 17586–17594.

[10] J.A. Ciezak and T.A. Jenkins, *The low-temperature high-pressure phase diagram of energetic materials: I. Hexahydro-1, 3, 5-Trinitro-s-Triazine*. Propellants, Explos., Pyrotech. 33 (2008), pp. 390–395.

[11] Z.A. Dreger and Y.M. Gupta, *Raman spectroscopy of high-pressure– high-temperature polymorph of Hexahydro-1, 3, 5-trinitro-1, 3, 5-triazine ($\varepsilon$-RDX)*. J. Phys. Chem. A 114 (2010), pp. 7038–7047.

[12] C. Gao, X. Zhang, C. Zhang, Z. Sui, M. Hou, R. Dai, Z. Wang, X. Zheng, and Z. Zhang, *Effect of pressure gradient and new phases for 1, 3, 5-trinitrohexahydro-s-triazine (RDX) under high pressures*. Phys. Chem. Chem. Phys 20 (2018), pp. 14374–14383.

[13] D.C. Sorescu and B.M. Rice, *Theoretical predictions of energetic molecular crystals at ambient and hydrostatic compression conditions using dispersion corrections to conventional density functionals (DFT-D)*. J. Phys. Chem. C 114 (2010), pp. 6734–6748.

[14] S. Grimme, *Semiempirical GGA-type density functional constructed with a long-range dispersion correction*. J. Comput. Chem. 27 (2006), pp. 1787–1799.

[15] J.Y. Fan, Z.Y. Zheng, Y. Su, and J.J. Zhao, *Assessment of dispersion correction methods within density functional theory for energetic materials*. Mol. Simul. 43 (2017), pp. 568–574.

[16] K.F. Grebenkin and A.L. Kutepov, *Band gap estimation for a triaminotrinitrobenzene molecular crystal by the density-functional method*. Semiconductors 34 (2000), pp. 1161–1162.

[17] H.L. Cui, G.F. Ji, X.R. Chen, W.H. Zhu, F. Zhao, Y. Wen, and D.Q. Wei, *First-principles study of high-pressure behavior of solid $\beta$-HMX*. J. Phys. Chem. A 114 (2010), pp. 1082–1092.

[18] P.L. Marinkas, *Luminescence of solid cyclic polynitramines*. J. Lumin. 15 (1977), pp. 57-67.

[19] S. Kakar, A.J. Nelson, R. Treusch, C. Heske, T. van Buuren, I. Jiménez, P. Pagoria, and L.J. Terminello, *Electronic structure of the energetic material 1, 3, 5-triamino-2, 4, 6-trinitrobenzene*. Phys. Rev. B 62 (2000), pp. 15666.

[20] S.J. Clark, M.D. Segall, C.J. Pickard, P.J. Hasnip, M.J. Probert, K. Refson, and M.C. Payne, *First principles methods using CASTEP*. Z. fuer Kristallogr 220 (2005), pp. 567-570.

[21] J.P. Perdew, K. Burke, and M. Ernzerhof, *Generalized gradient approximation made simple*. Phys. Rev. Lett. 77 (1996), pp. 3865.

[22] H.J. Monkhorst and J.D. Pack, *Special points for Brillouin-zone integrations*. Phys. Rev. B 13 (1976), pp. 5188.

[23] M. Zhong, H. Qin, Q.J. Liu, Z. Jiao, F. Zhao, H.L. Shang, F.S. Liu, and Z.T. Liu, *Influences of different surfaces on anisotropic impact sensitivity of hexahydro-1, 3, 5-trinitro-1, 3, 5-triazine*. Vacuum 139 (2017), pp. 117-121.

[24] C.S. Choi and E. Prince, *The crystal structure of cyclotrimethylenetrinitramine*. Acta Crystallogr. B 28 (1972), pp. 2857-2862.

[25] P. Hakey, W. Ouellette, J. Zubieta, and T. Korter, *Redetermination of cyclo-trimethylenetrinitramine*. Acta Crystallogr., Sect. E: Struct. Rep. 64 (2008), pp. o1428.

[26] J. Yuan, G. Ji, X. Chen, D. Wei, F. Zhao, and Q. Wu, *Phase transition, thermodynamics properties and IR spectrum of $\alpha$-and $\gamma$-RDX: first principles and MD studies*. Chem. Phys. Lett. 644 (2016), pp. 250-254.

[27] S. Hunter, T. Sutinen, S.F. Parker, C.A. Morrison, D.M. Williamson, S. Thompson, P.J. Gould, and C.R. Pulham, *Experimental and DFT-D studies of the molecular organic energetic material RDX*. J. Phys. Chem. C 117 (2013), pp. 8062-8071.

[28] L.Q. Zheng and D.L. Thompson, *Molecular dynamics simulations of melting of perfect crystalline hexahydro-1,3,5-trinitro-1,3,5-s-triazine*. J. Chem. Phys. 125 (2006), pp. 084505.

[29] E.C.F. Byrd and B.M. Rice, *Ab initio study of compressed 1,3,5,7-Tetranitro-1,3,5,7-tetraazacyclooctane (HMX), Cyclotrimethylenetrinitramine (RDX), 2,4,6,8,10,12-Hexanitrohexaazaisowurzitane (CL-20), 2,4,6-Trinitro-1,3,5-benzenetriamine (TATB), and Pentaerythritol Tetranitrate (PETN)*. J. Phys. Chem. C 111 (2007), pp. 2787-2796.

[30] P.M. Agrawal, B.M. Rice, L.Q. Zheng, and D.L. Thompson, *Molecular dynamics simulations of Hexahydro-1,3,5-trinitro-1,3,5-s-triazine (RDX) using a combined Sorescu-Rice-Thompson AMBER Force Field*. J. Phys. Chem. B 110 (2006), pp. 26185-26188.

[31] J. Fan, Y. Su, Z. Zheng, Q. Zhang, and J. Zhao, *The pressure effects and vibrational properties of energetic material: Hexahydro-1,3,5-trinitro-1,3,5-triazine ($\alpha$-RDX)*. J. Raman Spectrosc. 50 (2019), pp. 889-898.

[32] D.C. Wallace, *Thermodynamics of Crystals*, Wiley, New York, 1972.

[33] J.H. Westbrook and R.L. Fleischer, *Basic Mechanical Properties and Lattice Defects of Intermetallic Compounds*, Wiley, New York, 2000.

[34] G.V. Sin'ko and N.A. Smirnov, *On elasticity under pressure*. J. Phys.: Condens. Matter 16 (2004), pp. 8101.

[35] Q.J. Liu, Z. Ran, F.S. Liu, and Z.T. Liu, *Phase transitions and mechanical stability of TiO2 polymorphs under high pressure*. J. Alloys Compd. 631 (2015), pp. 192-201.

[36] R.B. Schwarz, D.E. Hooks, J.J. Dick, J.I. Archuleta, and A.R. Martinez, *Resonant ultra-sound spectroscopy measurement of the elastic constants of cyclotrimethylene trinitramine*. J. Appl. Phys. 98 (2005), pp. 056106.

[37] S. Haussühl, *Elastic and thermoelastic properties of selected organic crystals: acenaphthene, trans-azobenzene, benzophenone, tolane, trans-stilbene, dibenzyl, diphenyl*

sulfone, 2, 2'-biphenol, urea, melamine, hexogen, succinimide, pentaerythritol, urotro- pine, malonic acid, dimethyl malonic acid, maleic acid, hippuric acid, aluminium acet- ylacetonate, iron acetylacetonate, and tetraphenyl silicon. Z. Kristallogr. 216 (2001), pp. 339-353.

[38] S. Ye, K. Tonokura, and M. Koshi, *Theoretical calculations of lattice properties of sec- ondary explosives*. J. Jpn. Expl. Soc. 63 (2002), pp. 104-115.

[39] T.D. Sewell and C.M. Bennett, *Monte Carlo calculations of the elastic moduli and pressure-volume-temperature equation of state for hexahydro-1, 3, 5-trinitro-1, 3, 5-tria- zine*. J. Appl. Phys. 88 (2000), pp. 88-95.

[40] L.B. Munday, P.W. Chung, B.M. Rice, and S.D. Solares, *Simulations of high-pressure phases in RDX*. J. Phys. Chem. B 115 (2011), pp. 4378-4386.

[41] J. Fan, Y. Su, Q. Zhang, and J. Zhao, *Determination of second- and third-order elastic constants for energetic materials*. Comput. Mater. Sci. 161 (2019), pp. 379-384.

[42] R. Hill, *The elastic behaviour of a crystalline aggregate*. Proc. Phys. Soc. Sect. A 65 (1952), pp. 349-354.

[43] J.F. Nye, *Physical Properties of Crystals*, Clarendon Press, Oxford, 1964.

[44] M.A. Ali, M.M. Hossain, N. Jahan, A.K.M.A. Islam, and S.H. Naqib, *Newly synthesized Zr2AlC, Zr2 (Al0. 58Bi0. 42) C, Zr2 (Al0. 2Sn0. 8) C, and Zr2 (Al0. 3Sb0. 7) C MAX phases: a DFT based first-principles study*. Comput. Mater. Sci. 131 (2017), pp. 139-145.

[45] S.F. Pugh, *XCII. Relations between the elastic moduli and the plastic properties of poly- crystalline pure metals*. Philos. Mag. 45 (1954), pp. 823-843.

[46] C.L. Fu, X.D. Wang, and Y.Y. Ye, *Phase stability, bonding mechanism, and elastic con- stants of Mo5Si3 by first-principles calculation*. Intermetallics 7 (1999), pp. 179-184.
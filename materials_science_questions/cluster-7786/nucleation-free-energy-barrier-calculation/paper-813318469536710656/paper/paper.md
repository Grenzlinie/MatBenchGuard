![](./images/813318469536710656_1.jpg)

Available online at www.sciencedirect.com
SciVerse ScienceDirect
Acta Materialia 60 (2012) 3590-3603

![](./images/813318469536710656_2.jpg)

# Temperature dependence of the crystal-melt interfacial energy of metals

Zengyun Jian $^{a,*}$, Na Li $^{a}$, Man Zhu $^{a}$, Ji Chen $^{a}$, Fange Chang $^{a}$, Wanqi Jie $^{b}$

$^{a}$ School of Materials and Chemical Engineering, Xi'an Technological University, Xi'an 710032, People's Republic of China
$^{b}$ State Key Laboratory of Solidification Processing, Northwestern Polytechnical University, Xi'an 710072, People's Republic of China

Received 20 January 2012; received in revised form 16 February 2012; accepted 18 February 2012
Available online 7 April 2012

## Abstract
A model to express the dependence of the crystal-melt interfacial energy on the temperature for metals is proposed. The crystal-melt interfacial energies, the homogeneous nucleation undercoolings and the critical cooling rates to form ideal metallic glasses of silver, copper and nickel have been predicted according to the present model and simulated by the molecular dynamics method. The results show that the crystal-melt interfacial energy of metals increases nonlinearly with temperature. Over a wide temperature range from the melting point to the glass transition temperature the predicted results for the crystal-melt interfacial energy, the homogeneous nucleation undercooling and the critical cooling rate to form ideal metallic glasses from the present crystal-melt interfacial energy model are in good agreement with the experimental results reported, as well as the results of molecular dynamics simulations based on different EAM potentials of the metals.
© 2012 Acta Materialia Inc. Published by Elsevier Ltd. All rights reserved.

Keywords: Interface structure; Surface energy; Homogeneous nucleation of phase transformations; Simulation; Molecular dynamics

## 1. Introduction
The crystal-melt interfacial energy plays a key role in a wide range of metallurgical and materials phenomena, from wetting and sintering to solidification. Without a clear knowledge of the crystal-melt interfacial energy it is impossible to completely comprehend the solidification behaviour, such as the nucleation rate [1-5], the growth rate [5-8] and the growth mode [9,10] of crystals, and thereby effectively control the structures and properties of materials.
Measurement of the crystal-melt interfacial energy $\sigma^{T}$ is generally carried out by the maximum nucleation undercooling (MU) technique [1-5], based on homogeneous nucleation theory, which is used to measure the crystal-melt interfacial energy at the homogeneous nucleation temperature. In the seminal work of Turnbull [1] in 1950 the first measurements of $\sigma^{T}$ were derived from nucleation studies in undercooled melts. Turnbull [1] demonstrated a strong correlation between the crystal-melt interfacial energy and the ratio of the latent heat of melting ($L$, per atom) to the average interfacial area ($V_{a}^{2/3}$, per atom): $\sigma^{T}=CL/V_{a}^{2/3}$, where $C$ is termed the Turnbull coefficient and was originally reported to have a value of approximately 0.45 for metals. As more experimental data for $\sigma^{T}$ became available the value of the Turnbull coefficient has been refined. From maximum undercoolings in silver [11,12], copper [13,14] and nickel [13,15] $C$ was determined to be in the region 0.46-0.52 for face-centered cubic (fcc) metals. In addition, in a compilation of 26 maximum undercooling studies, Kelton [3] found $C=0.49\pm0.08$ for metals.
The dihedral angle (DA), the contact angle (CA) and the grain boundary groove (GBG) techniques [16-25] are used to measure the crystal-melt interfacial energy at the melting point. From a survey of solid-liquid dihedral angle measurements in fcc metals [16] Granasy et al. [17] derived a value for $C$ of approximately 0.6. According to the data for crystal-melt interfacial energies for fcc metals based on the CA technique [19,20] the derived value of $C$ is found to be in the region 0.63-0.68. In terms of the data for crystal-melt interfacial energies measured by the GBG technique $C$

* Corresponding author. Tel.: +86 029 83208079; fax: +86 029 83208078.
E-mail address: jianzengyun@yahoo.com (Z. Jian).

1359-6454/$36.00 © 2012 Acta Materialia Inc. Published by Elsevier Ltd. All rights reserved.
doi:10.1016/j.actamat.2012.02.038

was determined to be in the region 0.57-0.68 for aluminum alloys (Al-Si [21], Al-Cu [21], Al-Mg [22], Al-Ni [23], Al- Ti [23] and Al-Ag [24]). Also, the crystal-melt interfacial energy at the melting point can also be determined by atomistic simulation. Since the pioneering work of Brough- ton and Gilmer [25], atomistic simulations have been applied extensively in calculations of $\sigma^{T}$ for a variety of systems [5,26,27]. The average value of $C=0.55$ at the melting point for fcc metals can be derived from the atomistic sim- ulations [2].

Comparing the magnitudes of $C$ obtained via different techniques it is noteworthy that the MU data tend to be lower than those derived by the DA, CA and GBG meth- ods. This trend has been previously noted by a number of authors and it can be rationalized based on the fact that MU data provide values of $\sigma^{T}$ at nucleation temperatures that are typically a few hundred degrees below the melting point $(T_{m})$ , whereas DA, CA and GBG measurements are performed near the $T_{m}$ . This means that the crystal-melt interfacial energy varies with temperature. The lower val- ues of $\sigma^{T}$ derived from MU measurements would thus be consistent with a positive temperature dependence for the crystal-melt interfacial energy. As is well known, a certain amount of undercooling is needed for all solidification pro- cesses. So the crystal-melt interfacial energy in the undercooled state is more important in the study of solid- ification behaviour. Unfortunately, with the exception of the homogeneous nucleation temperature and the melting point, the crystal-melt interfacial energy at temperatures between the melting point and the homogeneous nucle- ation temperature cannot be measured. Therefore, it is nec- essary to explore the correlation between the crystal-melt interfacial energy and temperature.

At present the most widely used model for correlating the crystal-melt interfacial energy with temperature is that proposed by Spaepen [28,29]. In this theory the crystal- melt interfacial energy of metals was proposed to increase linearly with temperature. A value of $C=0.86$ is derived for fcc crystals under the assumption that the liquid struc- ture is characterized by tetrahedral packing. This value has been widely applied in modeling experimental nucleation data [2]. However, the crystal-melt interface in Spaepen's model is assumed to be perfectly smooth, whereas the real interface is rough. Consequently the results for the crystal- melt interfacial energy predicted from Spaepen's model are much higher than the data obtained by the MU [1-5,11-15], DA [16-18], CA [19,20] and GBG [21-24] techniques and atomistic simulations [5,26,27].

Recently Jian et al. [10,30,31] proposed a model to express the correlation between the crystal-melt interfacial energy and temperature for faceted materials. In this model the crystal-melt interfacial energy of a faceted material is predicted according to the critical growth transition under- coolings (i.e. the critical undercooling for a faceted material to grow from lateral to intermediary mode and the critical undercooling for a faceted material to grow from interme- diary to continuous mode). It is found that the results for the crystal-melt interfacial energies predicted from the crit- ical growth transition undercoolings for silicon [10,30,31], germanium [10] and bismuth [32] are consistent not only with the experimental results for the undercooled state according to the MU technique [33,34] but also with that at the melting point using the GBG technique [21]. How- ever, this model cannot be used to predict the crystal-melt interfacial energy of metals.

The purposes of this paper are, through modeling and molecular dynamics simulation of the crystal-melt interfa- cial energy of fcc metals, to determine the dependence of the crystal-melt interfacial energy on temperature and introduce a useful method which can be used to predict the crystal-melt interfacial energies of metals at the melting point and the homogeneous nucleation temperature as well as the temperature difference between the melting point and the homogeneous nucleation temperature.

## 2. Modeling the crystal-melt interfacial energy of metals
First, this study focuses on the crystal-melt interfacial energy of a perfectly smooth interface at the melting point. For a perfectly smooth crystal-melt interface, as shown in Fig. 1a, the entropy of the melt phase $S_{1}$ is greater than that of the crystal phase $S_{s}$ . The difference between $S_{1}$ and $S_{s}$ is the entropy of fusion. For a metal the entropy of fusion is composed of a configurational part, $\Delta S_{c}$ , and a vibrational part, $\Delta S_{v}$ .

Because the bond strength between the atoms of a crys- tal and its melt is greater than that between the atoms of the melt, the atoms of the melt in layer B (i.e. the atoms of the melt that directly adjoin the atoms of the crystal in the interface) cannot freely configure in the same way as the atoms of the bulk melt can, as shown in Fig. 1a. Thus the configuration of the atoms of the melt in layer B depends on that of the atoms of the crystal in layer A. In other words, the configuration of the atoms in layer B should correspond with that of the atoms in layer A. Hence the configurational entropy of the atoms in layer B should be approximately equal to that of the atoms in layer A, because the configurational entropy is dependent on the configuration. Consequently, the configurational entropy of fusion for the atoms in layer B, $\Delta S_{ci}$ , should be approx imately equal to zero (i.e. $\Delta S_{ci}=0$ ).

Thus if the vibrational entropy of fusion at the melting point for the atoms of the melt in layer B is represented by $\Delta S_{vi}$ (Fig. 1a) the relationship between $\Delta S_{vi}, \Delta S_{f}$ and $\sigma_{0}$ is given by:
$$\sigma_{0} A_{\mathrm{s}}+\Delta S_{\mathrm{vi}} T_{\mathrm{m}}=\Delta S_{\mathrm{f}} T_{\mathrm{m}}\qquad(1)$$

$$A_{\mathrm{s}}=b \sqrt[3]{V_{\mathrm{s}}^{2} N_{\mathrm{A}}}\qquad(2)$$
where $\sigma_{0}$ is the crystal-melt interfacial energy for a per fectly smooth interface at the melting point, $\Delta S_{f}$ is the en tropy of fusion, $A_{s}$ is the molar surface area of the crystal, $b$ is a constant that depends on the structure of the crystal and $N_{A}$ is the Avogadro constant.

![](./images/813318469536710656_3.jpg)

Fig. 1. Schematic representation of the interfacial energy, entropy of fusion, and vibrational entropy of fusion at the crystal-melt interface. (a) A perfectly smooth crystal-melt interface at $T_{\mathrm{m}}$; (b) a real crystal-melt interface at $T$.

If the atoms in both the crystal and melt are vibrating about a fixed average position, for a close packed metal, the difference between the molar vibrational entropy of the melt phase and that of the crystal phase is determined by the equation [28,29]:

$$
\Delta S_{\mathrm{v}}=3 \gamma R \ln \frac{V_{1}}{V_{\mathrm{s}}}
\tag{3}
$$

where $\Delta S_{\mathrm{v}}$ is the vibrational entropy of fusion, $R$ is the gas constant, $\gamma$ is the Grüneisen constant and $V_{1}$ and $V_{\mathrm{s}}$ are the molar volumes of the melt and the crystal, respectively. The molar volume of the atoms of the melt in layer B, $V_{\mathrm{i}}$, should be between $V_{\mathrm{s}}$ and $V_{1}$. Thus the vibrational entropy of fusion for the atoms of the melt in layer B, $\Delta S_{\mathrm{vi}}$, can be written as:

$$
\Delta S_{\mathrm{vi}}=3 \gamma R \ln \frac{V_{\mathrm{i}}}{V_{\mathrm{s}}}=3 \gamma R \ln \frac{\xi\left(V_{1}+V_{\mathrm{s}}\right)}{V_{\mathrm{s}}}
\tag{4}
$$

where $\xi$ is a coefficient.

Substituting Eq. (4) into Eq. (1) the following equation can be obtained:

$$
\phi_{0}=\frac{\sigma_{0} A_{\mathrm{s}}}{T_{\mathrm{m}} \Delta S_{\mathrm{f}}}=1-\frac{3 \gamma R}{\Delta S_{\mathrm{f}}} \ln \frac{\xi\left(V_{1}+V_{\mathrm{s}}\right)}{V_{\mathrm{s}}}
\tag{5}
$$

where $\phi_{0}$ is the non-dimensional crystal-melt interfacial energy for a perfectly smooth interface at the melting point.

In the undercooled state the crystal-melt interfacial energy of a perfectly smooth interface can be expressed in a form similar to Eq. (1) as follows:

$$
\sigma_{0}^{T} A_{\mathrm{s}}^{T}+\Delta S_{\mathrm{vi}}^{T} T=\Delta S_{\mathrm{f}}^{T} T
\tag{6}
$$

$$
\Delta S_{\mathrm{f}}^{T}=S_{1}^{T}-S_{\mathrm{s}}^{T}
\tag{7}
$$

where $T$ is the temperature, $\sigma_{0}^{T}, A_{\mathrm{s}}^{T}, \Delta S_{\mathrm{vi}}^{T}, \Delta S_{\mathrm{f}}^{T}, S_{1}^{T}$ and $S_{\mathrm{s}}^{T}$ are, respectively, the crystal-melt interfacial energy of a perfectly smooth interface, the molar surface area of the crystal, the vibrational entropy of fusion for the atoms of the melt in layer B, the entropy of fusion, the entropy of the melt and the entropy of the crystal at $T$.

For a metal $\Delta S_{\mathrm{f}}^{T}$ is determined by the equation

$$
\Delta S_{\mathrm{f}}^{T}=\Delta S_{\mathrm{f}}+\int_{T_{\mathrm{m}}}^{T} \frac{c_{\mathrm{pl}}-c_{\mathrm{ps}}}{T} d T
\tag{8}
$$

where $c_{\mathrm{ps}}$ and $c_{\mathrm{pl}}$ are the heat capacities at constant pressure for the crystal and melt, respectively.

The values of thermal expansivity (the thermal expansivity is in the form $(\mathrm{d} V^{T} / \mathrm{d} T) / V^{T}$, where $V^{T}$ is the molar volume at $T$) for silver, copper and nickel are $97 \times 10^{-6}$, $100 \times 10^{-6}$ and $142 \times 10^{-6} \mathrm{~K}^{-1}$ [35], respectively. Obviously, the variation in $V T$ with $T$ is negligibly small. Therefore, $A_{\mathrm{s}}^{T} T$ and $\Delta S_{\mathrm{vi}}^{T}$ in Eq. (6) can be replaced by $A_{\mathrm{s}}$ and $\Delta S_{\mathrm{vi}}$, respectively.

Thus from Eqs. (5)-(7) the following equation can be obtained:
$$
\phi_{0}^{T}=\frac{\sigma_{0}^{T} A_{\mathrm{s}}}{T \Delta S_{\mathrm{f}}}=\phi_{0}+\frac{\Delta S_{\mathrm{f}}^{T}-\Delta S_{\mathrm{f}}}{\Delta S_{\mathrm{f}}}
\tag{9}
$$
where $\phi_{0}^{T}$ is the non-dimensional crystal-melt interfacial energy for a perfectly smooth interface at $T$.

However, the equilibrium crystal-melt interface is not smooth for metals such as silver, copper and nickel. Therefore, the above model needs to be revised to make it agree with the real crystal-melt interface structure of metals. The equilibrium structure of the crystal-melt interface should be related to the state when the Gibbs energy at the interface is at a minimum. By studying the variation in Gibbs energy after the addition of atoms of a crystal to a smooth crystal-melt interface the equilibrium structure of a crystal-melt interface can be obtained. When atoms of a crystal are randomly added to a smooth crystal-melt interface a new configurational entropy, $S_{\mathrm{n}}$, and new bonds between the atoms of the crystal and melt, $N_{\mathrm{n}}$, will be produced. The total variation in Gibbs energy is represented as:
$$
\Delta G_{\mathrm{n}}=N_{\mathrm{n}} \sigma_{0}^{T *}-T S_{\mathrm{n}}
\tag{10}
$$
where $\Delta G_{\mathrm{n}}$ is the total variation in Gibbs energy after adding atoms of the crystal to the smooth crystal-melt interface and $\sigma_{0}^{T *}$ is the interfacial energy for one bond between atoms of the crystal and melt in a perfectly smooth crystal-melt interface. The value of $\sigma_{0}^{T *}$ can be obtained from the equation:
$$
\sigma_{0}^{T *}=\frac{\sigma_{0}^{T} A_{\mathrm{s}}}{N_{\mathrm{A}} Z_{\mathrm{n}}}
\tag{11}
$$
where $Z_{\mathrm{n}}$ is the number of atoms in layer A adjoining an atom in layer B.

When the number of lattice points in layer B equals $N_{\mathrm{A}}$, the number of bonds produced in layer B between atoms of the crystal and the melt can be written as:
$$
N_{\mathrm{n}}=N_{\mathrm{A}} Z_{\mathrm{i}} x(1-x)
\tag{12}
$$
where $Z_{\mathrm{i}}$ is the number of atoms in layer B adjoining an atom in layer B and $x$ is the fraction of atoms of the crystal in the interface.

The resultant configurational entropy is determined by the equation:
$$
\begin{aligned}
S_{\mathrm{n}} & =-k N_{\mathrm{A}}[x \ln x+(1-x) \ln (1-x)] \\
& =-R[x \ln x+(1-x) \ln (1-x)]
\tag{13}
\end{aligned}
$$
where $k$ is the Boltzmann constant.

Substituting Eqs. (11)-(13) into Eq. (10) gives the following equation:
$$
\Delta G_{\mathrm{n}}=R T\left[\alpha^{T} x(1-x)+x \ln x+(1-x) \ln (1-x)\right]
\tag{14}
$$
where
$$
\alpha^{T}=\frac{\sigma_{0}^{T} A_{\mathrm{s}} \psi}{R T}
\tag{15}
$$
$$
\psi=\frac{Z_{\mathrm{i}}}{Z_{\mathrm{n}}}
\tag{16}
$$

Plotting $\Delta G_{\mathrm{n}} / R T$ and $x$ in Eq. (14) on the $y$-axis and $x$-axis, respectively, curves representing the dependence of $\Delta G_{\mathrm{n}} / R T$ on $x$ can be obtained (Fig. 2). The results show that the curves have minima. For convenience we represent the minimum of $\Delta G_{\mathrm{n}}$ as $\Delta G_{\mathrm{n}}^{*}$ and the value of $x$ corresponding to $\Delta G_{\mathrm{n}}^{*} / R T$ as $x^{*}$. As shown in Fig. 2, the value of $x^{*}$ depends on $\alpha^{T}$.

When $\alpha^{T}$ is not greater than $2, x^{*}$ is equal to 0.5 , i.e.
$$
x^{*}=0.5 .\left(a^{T} \leq 2\right)
\tag{17}
$$

When $\alpha^{T}$ is greater than $2, x^{*}$ deviates from 0.5 and can be determined by differentiating Eq. (14) and letting it be equal to zero:
$$
\frac{\ln \left(1-x^{*}\right)-\ln x^{*}}{1-2 x^{*}}=\frac{\psi \phi_{0}^{T} \Delta S_{\mathrm{f}}}{R}=\alpha^{T} \cdot\left(a^{T}>2\right)
\tag{18}
$$

Substituting $x^{*}$ into Eq. (14) we can obtain $\Delta G_{\mathrm{n}}^{*}$:
$$
\Delta G_{\mathrm{n}}^{*}=R T\left[\alpha^{T} x^{*}\left(1-x^{*}\right)+x^{*} \ln x^{*}+\left(1-x^{*}\right) \ln \left(1-x^{*}\right)\right]
\tag{19}
$$

The equilibrium crystal-melt interfacial energy is related to the state when $\Delta G$ in Eq. (14) is at the minimum $\Delta G^{*}$. If the equilibrium crystal-melt interfacial energy is expressed as $\sigma^{T}$, as shown in Fig. 1b, the relationship between $\sigma^{T}, \sigma_{0}^{T}$ and $\Delta G_{\mathrm{n}}^{*}$ should be:
$$
\sigma^{T} A_{\mathrm{s}}-\Delta G_{\mathrm{n}}^{*}=\sigma_{0}^{T} A_{\mathrm{s}}
\tag{20}
$$

Using Eqs. (5, 9, 19, and 20), we can obtain the equilibrium crystal-melt interfacial energy:
$$
\begin{aligned}
\sigma^{T}= & \sigma_{0}\left\{\left(1+\frac{\Delta S_{\mathrm{f}}^{T}-\Delta S_{\mathrm{f}}}{\phi_{0} \Delta S_{\mathrm{f}}}\right)\left[1+\psi x^{*}\left(1-x^{*}\right)\right]\right. \\
& \left.+\frac{R}{\phi_{0} \Delta S_{\mathrm{f}}}\left[x^{*} \ln x^{*}+\left(1-x^{*}\right) \ln \left(1-x^{*}\right)\right]\right\} \frac{T}{T_{\mathrm{m}}}
\tag{21}
\end{aligned}
$$
$$
\begin{aligned}
\phi^{T}= & \frac{\sigma^{T} A_{\mathrm{s}}}{T \Delta S_{\mathrm{f}}}=\phi_{0}\left\{\left(1+\frac{\Delta S_{\mathrm{f}}^{T}-\Delta S_{\mathrm{f}}}{\phi_{0} \Delta S_{\mathrm{f}}}\right)\left[1+\psi x^{*}\left(1-x^{*}\right)\right]\right. \\
& \left.+\frac{R}{\phi_{0} \Delta S_{\mathrm{f}}}\left[x^{*} \ln x^{*}+\left(1-x^{*}\right) \ln \left(1-x^{*}\right)\right]\right\}
\tag{22}
\end{aligned}
$$

![](./images/813318469536710656_4.jpg)

Fig. 2. Effect of $\alpha^{T}$ on the dependence of $\Delta G_{\mathrm{n}} / R T$ on $x$ (where $x$ is the fraction of atoms of the crystal in the interface).

<table>
<caption>Table 1<br>Physical parameters of silver, copper and nickel.</caption>
<thead>
<tr>
<th>Metal</th>
<th>$\gamma$ [28,29]</th>
<th>$V_{\mathrm{s}} \times 10^{6}$<br>($\mathrm{m}^{3} \mathrm{~mol}^{-1}$) [35]</th>
<th>$V_{\mathrm{l}} \times 10^{6}$<br>($\mathrm{m}^{3} \mathrm{~mol}^{-1}$) [35]</th>
<th>$E_{\mathrm{d}} \times 10^{20}$<br>(J) [36]</th>
<th>$D_{0} \times 10^{8}$<br>($\mathrm{m}^{2} \mathrm{~s}^{-1}$) [36,35]</th>
<th>$a_{0} \times 10^{10}$<br>(m) [37]</th>
<th>$E_{\eta} \times 10^{-4}$<br>($\mathrm{J} \mathrm{mol}^{-1}$) [36]</th>
<th>$\eta_{0} \times 10^{4}$<br>(Pas) [36]</th>
</tr>
</thead>
<tbody>
<tr>
<td>Silver</td>
<td>2.40</td>
<td>11.16</td>
<td>11.54</td>
<td>5.21</td>
<td>5.80</td>
<td>3.20</td>
<td>2.22</td>
<td>4.47</td>
</tr>
<tr>
<td>Copper</td>
<td>1.96</td>
<td>7.61</td>
<td>7.91</td>
<td>6.76</td>
<td>14.60</td>
<td>2.70</td>
<td>3.06</td>
<td>2.73</td>
</tr>
<tr>
<td>Nickel</td>
<td>2.01</td>
<td>7.11</td>
<td>7.56</td>
<td>7.93</td>
<td>3.63</td>
<td>2.70</td>
<td>4.12</td>
<td>2.61</td>
</tr>
</tbody>
</table>

<table>
<caption>Table 2<br>Thermodynamic parameters of silver, copper and nickel.</caption>
<thead>
<tr>
<th>Metal</th>
<th>$T_{\mathrm{m}}(\mathrm{K})$ [37]</th>
<th>$\Delta S_{\mathrm{f}}\left(\mathrm{J} \mathrm{mol}^{-1} \mathrm{~K}^{-1}\right)$ [37]</th>
<th>$c_{\mathrm{pl}}\left(\mathrm{J} \mathrm{mol}^{-1} \mathrm{~K}^{-1}\right)$ [36,38]</th>
<th>$c_{\mathrm{ps}}\left(\mathrm{J} \mathrm{mol}^{-1} \mathrm{~K}^{-1}\right)$ [36,39]</th>
</tr>
</thead>
<tbody>
<tr>
<td>Silver</td>
<td>1234</td>
<td>9.16</td>
<td>30.56</td>
<td>$21.31+8.54 × 10^{-3} T+1.51 × 10^{5} T^{-2}$</td>
</tr>
<tr>
<td>Copper</td>
<td>1356</td>
<td>9.59</td>
<td>33.00</td>
<td>$22.65+6.28 × 10^{-3} T$</td>
</tr>
<tr>
<td>Nickel</td>
<td>1728</td>
<td>10.22</td>
<td>38.52</td>
<td>$-10.87+54.67 × 10^{-3} T+56.48 × 10^{5} T^{-2}$<br>$-16.49 × 10^{-6} T^{2}$ (700–1400 K)<br>36.19 (1400–1728 K)</td>
</tr>
</tbody>
</table>

where $\phi^{T}$ is the non-dimensional crystal–melt interfacial energy.

The relationship between $\sigma^{T}$ and $C$ is:
$$
\begin{aligned}
C= & \frac{\sigma^{T} A_{\mathrm{s}}}{b \Delta S_{\mathrm{f}} T_{\mathrm{m}}}=\frac{\phi_{0} T}{b T_{\mathrm{m}}}\left\{\left(1+\frac{\Delta S_{\mathrm{f}}^{T}-\Delta S_{\mathrm{f}}}{\phi_{0} \Delta S_{\mathrm{f}}}\right)\left[1+\psi x^{*}\left(1-x^{*}\right)\right]\right. \\
& \left.+\frac{R}{\phi_{0} \Delta S_{\mathrm{f}}}\left[x^{*} \ln x^{*}+\left(1-x^{*}\right) \ln \left(1-x^{*}\right)\right]\right\}
\end{aligned}
$$
(23)

With the exception of $\psi$, $b$ and $\xi$, other physical and thermodynamic parameters in Eqs. (21)–(23) are available. The physical and thermodynamic parameters for silver, copper and nickel [28,29,35–39] are listed in Tables 1 and 2.

## 3. Determinations of $\psi$, $b$ and $\xi$

### 3.1. Determinations of $\psi$ and $b$

The values of $\psi$ and $b$ depend on the crystal structure and orientation of the crystal–melt interface. When the crystal structure is known we can easily calculate the value of $\psi$. Table 3 lists the calculated values of $\psi$ for fcc and body-centered cubic (bcc) crystals.

The value of $b$ can be determined by the equation:
$$
b=\frac{A_{\mathrm{s}}^{*}}{\sqrt[3]{V_{\mathrm{s}}^{* 2}}} \frac{\sqrt[3]{n_{\mathrm{b}}^{2}}}{n_{\mathrm{s}}}
$$
(24)

<table>
<caption>Table 3<br>Structural parameters of fcc and bcc metals (where $a$ is the lattice constant).</caption>
<thead>
<tr>
<th>Metal</th>
<th>Crystal plane</th>
<th>$Z_{\mathrm{i}}$</th>
<th>$Z_{\mathrm{n}}$</th>
<th>$\psi$</th>
<th>$n_{\mathrm{b}}$</th>
<th>$n^{\mathrm{s}}$</th>
<th>$A_{\mathrm{s}}^{*}$</th>
<th>$V_{\mathrm{s}}^{*}$</th>
<th>$b$</th>
</tr>
</thead>
<tbody>
<tr>
<td>fcc</td>
<td>{111}</td>
<td>6</td>
<td>3</td>
<td>2</td>
<td>4</td>
<td>2</td>
<td>$\sqrt{3} a^{2} / 2$</td>
<td>$a^{3}$</td>
<td>1.0911</td>
</tr>
<tr>
<td></td>
<td>{100}</td>
<td>4</td>
<td>4</td>
<td>1</td>
<td>4</td>
<td>2</td>
<td>$a^{2}$</td>
<td>$a^{3}$</td>
<td>1.2598</td>
</tr>
<tr>
<td>bcc</td>
<td>{110}</td>
<td>4</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>$\sqrt{2} a^{2}$</td>
<td>$a^{3}$</td>
<td>1.1223</td>
</tr>
<tr>
<td></td>
<td>{100}</td>
<td>4</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>1</td>
<td>$a^{2}$</td>
<td>$a^{3}$</td>
<td>1.5874</td>
</tr>
</tbody>
</table>

where $A_{\mathrm{s}}^{*}$ is the surface area of a crystal plane in a unit cell, $n_{\mathrm{s}}$ is the number of atoms in the crystal plane of a unit cell, $V_{\mathrm{s}}^{*}$ is the volume of a unit cell and $n_{\mathrm{b}}$ is the number of atoms in a unit cell. Table 3 lists the calculated values of $b$ for fcc and bcc metals. The values of $b$ for the most closely packed planes of fcc and bcc crystals are 1.0911 and 1.1223, respectively.

### 3.2. Determination of $\xi$

The value of $\xi$ can be predicted from the homogeneous nucleation undercooling. Supposing that the homogeneous nucleation undercooling $\Delta T_{\mathrm{v}}$ is the one at which the first nucleus forms in a melt, $\Delta T_{\mathrm{v}}$ can be determined using the equation:
$$
\int_{0}^{\Delta T_{\mathrm{v}}} I_{\mathrm{v}} V \frac{1}{R_{\mathrm{c}}} d \Delta T=1
$$
(25)

where $V$ is the sample volume, $R_{\mathrm{c}}$ is the cooling rate and $I_{\mathrm{v}}$ is the homogeneous nucleation rate. $I_{\mathrm{v}}$ can be expressed as [1]:
$$
I_{\mathrm{v}}=\frac{N_{\mathrm{A}} k T}{V_{1} h} \exp \left[-\frac{\Delta G_{\mathrm{d}}}{k T}\right] \exp \left[-\frac{\beta \sigma^{T 3} V_{1}^{2}}{k \Delta S_{\mathrm{f}}^{2} T \Delta T^{2}}\right]
$$
(26)

where $h$ is the Planck constant, $E_{\mathrm{d}}$ is the free energy of activation for transportation of an atom across the crystal–melt interface and $\beta$ is a factor determined by the shape of the nucleus ($\beta = 16\pi/3$ for a spherical nucleus). If the homogeneous nucleation undercooling is known the crystal–melt interfacial energy can be determined in terms of Eqs. (25) and (26). Thus, substituting the determined crystal–melt interfacial energy into Eq. (21), we can determine $\xi$.

The homogeneous nucleation undercoolings for silver, copper and nickel were simulated by applying the molecular dynamics (MD) method. The simulations were carried out using the July 2009 version of LAMMPS (the large-scale atomic/molecular massively parallel simulator) [40]. Two EMA potentials were selected for each metal, silver

![](./images/813318469536710656_5.jpg)

Fig. 3. Crystal-melt coexistence simulation of the melting point of silver according to the EAM potential obtained by Williams et al. [41].

[41,42], copper [41,43] and nickel [43,44]. The crystal-melt coexistence method was applied to simulate the melting point. Fig. 3 shows the results for the melting point deter- mined using the crystal-melt coexistence method for silver based on the EMA potential of Williams et al. [41]. The Nosé-Hoover thermostat was applied to adjust the temper- ature. The MD time step was 0.002 ps. The simulation con-sisted of three procedures:

- heating the system at a temperature 300 K above the melting point until the crystal had completely melted,which was judged by observing snapshots of the system;
- holding the melted system at this temperature for6000 ps;
- cooling the melted system to 600 K at different cooling rates.

The nucleation temperature was determined based on the potential curve as a function of the temperature. Fig. 4 shows the curves of the potential as a function of the temperature for two silver samples based on the EMA potential of Williams et al. [41]. From the simulated nucleation temperature and melting point we can deter- mine the nucleation undercooling. By substituting the determined nucleation undercooling and the appropriateparameters for the metals in Tables 1-3 into Eqs. (25) and (26) we can predict the crystal-melt interfacial energy. Then, substituting the determined crystal-melt interfacial energy into Eq. (21) we can calculate the value of $\xi$ . Table4 presents the determined results for nucleation undercool- ing, the crystal-melt interfacial energy and $\xi$ based on the different potentials of silver [41,42], copper [41,43] and nickel [43,44]. It can be seen that the predicted results for $\xi$ for silver, copper and nickel are approximately equal to0.5, which indicates that the molar volume of atoms in layer B in the crystal-melt interface is approximately equal to the average of the molar volumes of the crystal and the melt. So we can assume that $\xi$ is approximately equal to 0.5 for metals.

It should be noted that the values of $\xi$ for silver, copper and nickel in Table 4 are determined according to the val- ues of $\psi$ and b for the {111} plane, which is the most clo sely packed one. The reason for this is that the nucleation and growth of a crystal is controlled by the most closely packed plane. Since the value of $\xi(\xi=0.5)$ is determined from the homogeneous nucleation undercooling simulation the predicted result for $\sigma^{T}$ based on $\xi=0.5$ is the effective crystal-melt interfacial energy, which is composed of a vibrational, a configurational and an electrostatic part. Tournier [45] introduced a method to predict the electro- static part of the crystal-melt interfacial energy.

## 4. Comparisons and discussions

### 4.1. Comparison of the experimental and the simulated crystal-melt interfacial energy with the results of the present crystal-melt interfacial energy model

When the values of $\psi, b$ and $\xi$ are known the crystal-melt interfacial energy $(\sigma^{T})$ , the non-dimensional crystal-melt interfacial energy $(\phi^{T})$ and Turnbull coeffi cient (C) at a given temperature can be predicted using Eqs. (21)-(23), respectively. The predicted results for $\sigma^{T}$ , $\phi^{T}$ and C at the melting point for silver, copper and nickel are listed in Table 5. For the purposes of comparison the

![](./images/813318469536710656_6.jpg)

Fig. 4. Dependence of the potential on temperature for silver according to the EAM potential obtained by Williams et al. [41].

### Table 4
The simulated results of the homogeneous nucleation undercooling and the predicted results of the crystal-melt interfacial energy and $\xi$ for metals ($\bar{\xi}$ is the mean value of $\xi$).

<table>
  <thead>
    <tr>
      <th>Metal</th>
      <th>EAM potential</th>
      <th>$T_{\text{m}}$ (K)</th>
      <th>$V$ ($\text{m}^3$)</th>
      <th>$R_{\text{c}}$ (K/s)</th>
      <th>$V/R_{\text{c}}$($\text{m}^3\,\text{K}^{-1}\text{s}$)</th>
      <th>$\Delta T_{\text{v}}$ (K)</th>
      <th>$\sigma^{T}$($\text{J}\,\text{m}^{-2}$)</th>
      <th>$\xi$</th>
      <th>$\bar{\xi}$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Silver</td>
      <td>[41]</td>
      <td>1269.8</td>
      <td>$10^{-25.4}$</td>
      <td>$10^{9.7}$</td>
      <td>$10^{-35.1}$</td>
      <td>452.6</td>
      <td>0.1031</td>
      <td>0.4998</td>
      <td>0.5002</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>$10^{-24.4}$</td>
      <td>$10^{11.0}$</td>
      <td>$10^{-35.4}$</td>
      <td>456.2</td>
      <td>0.1011</td>
      <td>0.5021</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>$10^{-25.8}$</td>
      <td>$10^{9.7}$</td>
      <td>$10^{-35.5}$</td>
      <td>457.4</td>
      <td>0.1012</td>
      <td>0.5009</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>$10^{-26.1}$</td>
      <td>$10^{9.7}$</td>
      <td>$10^{-35.8}$</td>
      <td>470.0</td>
      <td>0.1005</td>
      <td>0.4997</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>$10^{-24.4}$</td>
      <td>$10^{12.0}$</td>
      <td>$10^{-36.4}$</td>
      <td>489.9</td>
      <td>0.0981</td>
      <td>0.4984</td>
      <td></td>
    </tr>
    <tr>
      <td>Silver</td>
      <td>[42]</td>
      <td>1268.4</td>
      <td>$10^{-24.5}$</td>
      <td>$10^{11.8}$</td>
      <td>$10^{-36.3}$</td>
      <td>478.9</td>
      <td>0.0981</td>
      <td>0.5000</td>
      <td>0.4989</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>$10^{-24.5}$</td>
      <td>$10^{11.9}$</td>
      <td>$10^{-36.4}$</td>
      <td>487.7</td>
      <td>0.0981</td>
      <td>0.4987</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>$10^{-24.5}$</td>
      <td>$10^{12.0}$</td>
      <td>$10^{-36.5}$</td>
      <td>490.7</td>
      <td>0.0976</td>
      <td>0.5000</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>$10^{-24.5}$</td>
      <td>$10^{12.1}$</td>
      <td>$10^{-36.6}$</td>
      <td>489.4</td>
      <td>0.0978</td>
      <td>0.4968</td>
      <td></td>
    </tr>
    <tr>
      <td>Copper</td>
      <td>[41]</td>
      <td>1327.0</td>
      <td>$10^{-24.5}$</td>
      <td>$10^{11.0}$</td>
      <td>$10^{-35.5}$</td>
      <td>439.9</td>
      <td>0.1393</td>
      <td>0.4986</td>
      <td>0.4989</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>$10^{-25.8}$</td>
      <td>$10^{11.5}$</td>
      <td>$10^{-35.8}$</td>
      <td>433.4</td>
      <td>0.1382</td>
      <td>0.4992</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>$10^{-24.5}$</td>
      <td>$10^{11.7}$</td>
      <td>$10^{-36.2}$</td>
      <td>449.8</td>
      <td>0.1347</td>
      <td>0.4989</td>
      <td></td>
    </tr>
    <tr>
      <td>Copper</td>
      <td>[43]</td>
      <td>1314.4</td>
      <td>$10^{-25.3}$</td>
      <td>$10^{11.0}$</td>
      <td>$10^{-36.3}$</td>
      <td>439.5</td>
      <td>0.1323</td>
      <td>0.5005</td>
      <td>0.4998</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>$10^{-25.3}$</td>
      <td>$10^{11.5}$</td>
      <td>$10^{-36.8}$</td>
      <td>448.9</td>
      <td>0.1290</td>
      <td>0.5005</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>$10^{-25.3}$</td>
      <td>$10^{12.0}$</td>
      <td>$10^{-37.3}$</td>
      <td>477.3</td>
      <td>0.1274</td>
      <td>0.4984</td>
      <td></td>
    </tr>
    <tr>
      <td>Nickel</td>
      <td>[43]</td>
      <td>1820.0</td>
      <td>$10^{-24.3}$</td>
      <td>$10^{11.0}$</td>
      <td>$10^{-35.3}$</td>
      <td>570.6</td>
      <td>0.1949</td>
      <td>0.4994</td>
      <td>0.4985</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>$10^{-24.3}$</td>
      <td>$10^{12.0}$</td>
      <td>$10^{-36.3}$</td>
      <td>591.7</td>
      <td>0.1915</td>
      <td>0.4985</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>$10^{-24.5}$</td>
      <td>$10^{12.0}$</td>
      <td>$10^{-36.5}$</td>
      <td>606.9</td>
      <td>0.1910</td>
      <td>0.4976</td>
      <td></td>
    </tr>
    <tr>
      <td>Nickel</td>
      <td>[44]</td>
      <td>1778.4</td>
      <td>$10^{-24.5}$</td>
      <td>$10^{11.2}$</td>
      <td>$10^{-35.7}$</td>
      <td>577.0</td>
      <td>0.1961</td>
      <td>0.4987</td>
      <td>0.4998</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>$10^{-24.5}$</td>
      <td>$10^{12.2}$</td>
      <td>$10^{-36.7}$</td>
      <td>610.1</td>
      <td>0.1892</td>
      <td>0.4976</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>$10^{-24.5}$</td>
      <td>$10^{11.8}$</td>
      <td>$10^{-36.8}$</td>
      <td>590.0</td>
      <td>0.1851</td>
      <td>0.5001</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Table 5
Predicted results for the crystal-melt interfacial energy of metals at the melting points ($C_{\text{E}}$ is the experimental result for $C$ by DA or CA).

<table>
  <thead>
    <tr>
      <th>Metal</th>
      <th>$\sigma_{0}$ ($\text{J}\,\text{m}^{-2}$)</th>
      <th>$\phi_{0}$</th>
      <th>$\sigma$ ($\text{J}\,\text{m}^{-2}$)</th>
      <th>$\phi$</th>
      <th>$C$</th>
      <th>$C_{\text{E}}$</th>
      <td>$(C_{\text{E}}-C)/C_{\text{E}}(\%)$</td>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Silver</td>
      <td>0.2212</td>
      <td>0.8897</td>
      <td>0.1752</td>
      <td>0.7123</td>
      <td>0.6535</td>
      <td>0.6417 (DA [16])</td>
      <td>1.81</td>
    </tr>
    <tr>
      <td>Copper</td>
      <td>0.3279</td>
      <td>0.8984</td>
      <td>0.2724</td>
      <td>0.7464</td>
      <td>0.6841</td>
      <td>0.6787 (CA [19])</td>
      <td>0.79</td>
    </tr>
    <tr>
      <td>Nickel</td>
      <td>0.4400</td>
      <td>0.8479</td>
      <td>0.3668</td>
      <td>0.7069</td>
      <td>0.6486</td>
      <td>0.6418 (DA [16])</td>
      <td>1.05</td>
    </tr>
  </tbody>
</table>

experimental Turnbull coefficient results, $C_{\text{E}}$, for the metals obtained by the DA [16] and CA [19] techniques are also listed in Table 5. It can be seen that the Turnbull coefficients predicted from the present crystal-melt interfacial energy model for silver, copper and nickel are almost equal to the experimental results obtained by the DA [16] and CA [19] techniques. The relative errors of $C$ and $C_{\text{E}}$ for silver, copper and nickel are as small as 1.81%, 0.79% and 1.05%, respectively.

Fig. 5 shows the dependence of the crystal-melt interfacial energy on temperature, as predicted from Eq. (21) for silver, copper and nickel. In Fig. 5 the solid and open squares are the results for solid-liquid interfacial energies determined using the experimental undercoolings [10-15], which are listed in Table 6. These are the maximum undercoolings obtained for silver, copper and nickel. The solid triangles are the results for solid-liquid interfacial energies determined by the DA technique [16]. The solid upside down triangle is the result for solid-liquid the interfacial energy determined using the CA technique [19]. The open and solid circles are the results for solid-liquid interfacial energies determined from our simulated homogeneous nucleation undercoolings (HU) based on the different potentials of silver [41,42], copper [41,43] and nickel [43,44]. The results show that the curves for the solid-liquid interfacial energies as a function of temperature for silver, copper and nickel, as predicted by the present solid-liquid interfacial energy model, are in good agreement not only with the experimental results using the DA and CA techniques at the melting point but also with the experimental results determined using the MU technique at the maximum nucleation temperature and the simulated results using the HU technique at the homogeneous nucleation temperature.

Fig. 6 shows the curves for $\phi^{T}$ as a function of $T/T_{\text{m}}$ for silver, copper and nickel. The results show that $\phi^{T}$ increases nonlinearly with $T/T_{\text{m}}$, which indicates that the relationship between the crystal-melt interfacial energy and temperature is nonlinear.

Fig. 7 shows the dependencies of $C$ on $T/T_{\text{m}}$ for silver, copper and nickel. The results show that the Turnbull coefficient $C$ varies with temperature. And, obviously, the data for the Turnbull coefficient $C$ predicted by the present solid-liquid interfacial energy model for silver, copper and nickel also agree well with the experimental results using the DA and CA techniques at the melting point

![](./images/813318469536710656_7.jpg)

Fig. 5. Dependence of the crystal-melt interfacial energy on temperature for silver, copper and nickel.

<table>
<thead>
<tr>
<th colspan="9">Table 6</th>
</tr>
<tr>
<th colspan="9">The experimental maximum nucleation undercoolings and the predicted results for the crystal-melt interfacial energies of metals ($\sigma_{\text{E}}^{T}$ is the experimental result for $\sigma^{T}$ and $C_{\text{E}}$ is the experimental result for $C$).</th>
</tr>
<tr>
<th>Metal</th>
<th>Method</th>
<th>$V/R_{\text{c}}$ ($\text{m}^{3}\text{K}^{-1}\text{s}$)</th>
<th>$\Delta T$ (K)</th>
<th>$C_{\text{E}}$</th>
<th>$\sigma_{\text{E}}^{T}$ ($\text{J}\text{m}^{-2}$)</th>
<th>$\sigma^{T}$ ($\text{J}\text{m}^{-2}$)</th>
<th>$(\sigma_{\text{E}}^{T}-\sigma^{T})/\sigma_{\text{E}}^{T}$ (%)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Silver</td>
<td>Fluxing [11]</td>
<td>$10^{-3.73}$</td>
<td>251</td>
<td>0.5205</td>
<td>0.1395</td>
<td>0.1417</td>
<td>$-1.58$</td>
</tr>
<tr>
<td></td>
<td>Fluxing [12]</td>
<td>$10^{-5.45}$</td>
<td>256</td>
<td>0.5182</td>
<td>0.1389</td>
<td>0.1409</td>
<td>$-1.44$</td>
</tr>
<tr>
<td></td>
<td>Fluxing [12]</td>
<td>$10^{-6.17}$</td>
<td>260</td>
<td>0.5194</td>
<td>0.1392</td>
<td>0.1402</td>
<td>$-0.72$</td>
</tr>
<tr>
<td>Copper</td>
<td>Levitation [13]</td>
<td>$10^{-8.88}$</td>
<td>266</td>
<td>0.4766</td>
<td>0.1896</td>
<td>0.1919</td>
<td>$-1.21$</td>
</tr>
<tr>
<td></td>
<td>Dispersion [14]</td>
<td>$10^{-13.17}$</td>
<td>277</td>
<td>0.4650</td>
<td>0.1850</td>
<td>0.1884</td>
<td>$-1.84$</td>
</tr>
<tr>
<td>Nickel</td>
<td>Levitation [13]</td>
<td>$10^{-8.88}$</td>
<td>341</td>
<td>0.4627</td>
<td>0.2617</td>
<td>0.2649</td>
<td>$-1.22$</td>
</tr>
<tr>
<td></td>
<td>Dispersion [15]</td>
<td>$10^{-13.01}$</td>
<td>366</td>
<td>0.4606</td>
<td>0.2605</td>
<td>0.2575</td>
<td>$1.15$</td>
</tr>
</tbody>
</table>

[16,19], the experimental results using the MU technique at the maximum nucleation temperature [10-15] and the simulated results using the HU technique at the homogeneous nucleation temperature based on the different potentials of silver [41,42], copper [41,43] and nickel [43,44].

### 4.2. Comparison of the experimental and the simulated homogeneous nucleation undercoolings with the results of the present crystal-melt interfacial energy model

If the crystal-melt interfacial energy is known the homogeneous nucleation undercooling, $\Delta T_{\text{v}}$, can be predicted according to Eqs. (25) and (26). The dependencies of $\Delta T_{\text{v}}$ on $V/R_{\text{c}}$ for silver, copper and nickel are shown in Fig. 8.

In Fig. 8a the solid and open squares represent the undercoolings of bulk silver encased in soda lime glass [11] and slag consisting of soda lime glass and $\text{Na}_{2}\text{CO}_{3}$ [12], respectively, while the solid and open circles are our simulated undercoolings based on two EAM potentials [41,42] of silver. The solid and open squares in Fig. 8b are the experimental undercoolings of copper obtained by means of the electromagnetic levitation [13] and the dispersion [14] techniques, while the open and solid circles are our simulated undercoolings based on two EAM potentials [41,43] of copper. In Fig. 8c the squares and circles are the experimental undercoolings obtained using the electromagnetic levitation method [13], the dispersion method [15] and our simulated results based on two EAM potentials [43,44] of nickel, respectively.

The blank solid curves in Fig. 8 are the predicted results for $\Delta T_{\text{v}}$ as a function of $V/R_{\text{c}}$ according to Eq. (21) for silver, copper and nickel. Obviously, the black solid curves predicted from the present crystal-melt interfacial energy model in Eq. (21) agree well with the experimental and simulated results for silver, copper and nickel.

The grey solid curve in Fig. 8 is the predicted result for $\Delta T_{\text{v}}$ according to the crystal-melt interfacial energy model of Spaepen et al. [28,29]. We can see that they are higher than the experimental and simulated results. The reason for this is that the crystal-melt interface for metals in the model of Spaepen et al. is considered to be smooth, whereas the real crystal-melt interface of metals is rough.

![](./images/813318469536710656_8.jpg)

Fig. 6. Dependence of $\phi^T$ on $T/T_{\text{m}}$ for silver, copper and nickel.

The black dashed curve in Fig. 8 is the predicted result for $\Delta T_{\text{v}}$ according to Turnbull's experimental results for crystal-melt interfacial energy [1]. Here a constant crystal-melt interfacial energy was applied in the temperature region. Obviously, the curve is lower than the experimental undercooling obtained in the high $V/R_{\text{c}}$ region, while it is higher than the simulated undercoolings obtained in the low $V/R_{\text{c}}$ region. Moreover, we find that if it is assumed that the crystal-melt interfacial energy does not vary with temperature we cannot make the curve for $\Delta T_{\text{v}}$ as a function of $V/R_{\text{c}}$ agree with the experimental results or the simulated results, no matter how we adjust the crystal-melt interfacial energy. This indicates that it is incorrect to assume that the crystal-melt interfacial energy does not vary with temperature.

### 4.3. Comparison of the simulated critical cooling rate to form the ideal metallic glass with the results of the present crystal-melt interfacial energy model

To further examine the accuracy of the crystal-melt interfacial energy model proposed in this study the values of the critical cooling rate to form an ideal metallic glass (i.e. nucleation does not take place during the solidification process), $R_{\text{ig}}$, for silver, copper and nickel were predicted using the present crystal-melt interfacial energy model and simulated using the EAM potential method.

#### 4.3.1. Prediction of $R_{ig}$ according to the present crystal-melt interfacial energy model

In order to discuss the critical cooling rate to form an ideal metallic glass the diffusion term in Eq. (25) should be replaced by a viscosity term. The relation between viscosity and the diffusion coefficient is determined using the Stokes-Einstein equation:
$$
D \eta=\frac{k T}{6 \pi a_{0}}
\tag{27}
$$
where $\eta$ is the viscosity, $D$ is the diffusion coefficient and $a_{0}$ is the atom diameter.

![](./images/813318469536710656_9.jpg)

Fig. 7. Dependences of $C$ on $T/T_{\text{m}}$ for silver, copper and nickel.

The diffusion coefficient and the viscosity can be expressed as:
$$
D=D_{0} \exp \left(-\frac{E_{\mathrm{d}}}{k T}\right)
\tag{28}
$$

$$
\eta=\eta_{0} \exp \left(\frac{E_{\eta}}{R\left(T-T_{\mathrm{g}}\right)}\right)
\tag{29}
$$

![](./images/813318469536710656_10.jpg)

Fig. 8. Dependence of homogeneous nucleation undercooling on the ratio of sample volume to the cooling rate for silver, copper and nickel.

where $D_0$ is a constant, $\eta_0$ is a constant, $E_\eta$ is the viscous activation energy and $T_\mathrm{g}$ is the critical temperature to form a metallic glass, which is equal to $0.25T_\mathrm{m}$ for metals [46].

From Eqs. (27)-(29) we can obtain the equation:

$$
\exp \left(-\frac{E_{\mathrm{d}}}{k T}\right)=\frac{k T}{6 \pi a_{0} D_{0} \eta_{0}} \exp \left(-\frac{E_{\eta}}{R\left(T-T_{\mathrm{g}}\right)}\right) \tag{30}
$$

Substituting Eq. (30) into Eq. (26) we can obtain the equation:

$$
I_{\mathrm{v}}=\frac{N_{\mathrm{a}}(k T)^{2}}{6 \pi a_{0} h V_{1} D_{0} \eta_{0}} \exp \left(-\frac{E_{\eta}}{R\left(T-T_{\mathrm{g}}\right)}\right) \exp \left[-\frac{\beta \sigma^{T 3} V_{1}^{2}}{k \Delta S_{\mathrm{f}}^{2} T \Delta T^{2}}\right] \tag{31}
$$

![](./images/813318469536710656_11.jpg)

Fig. 9. Dependence of the homogeneous nucleation temperature on the cooling rate according to the EAM potentials of silver [41], copper [43] and nickel [43].

From Eqs. (31), (25), and (21) we can obtain the dependence of the homogeneous nucleation temperature $T_{\mathrm{v}}$ on the cooling rate. Figs. 9 and 10 show the curves of $T_{\mathrm{v}}/T_{\mathrm{m}}$ as a function of $R_{\mathrm{c}}$ for silver, copper and nickel. It can be seen that $T_{\mathrm{v}}/T_{\mathrm{m}}$ decreases with increasing $R_{\mathrm{c}}$ when $R_{\mathrm{c}}$ is lower than $R_{\mathrm{ig}}$. When $R_{\mathrm{c}}$ is equal to $R_{\mathrm{ig}}$ the curve of $T_{\mathrm{v}}/T_{\mathrm{m}}$ as a function of $R_{\mathrm{c}}$ is a vertical line. This means that nucleation cannot take place when the the cooling rate is larger than $R_{\mathrm{ig}}$. So $R_{\mathrm{ig}}$ is the critical cooling rate to form an ideal metallic glass. The values of $R_{\mathrm{ig}}$ predicted from the present model for silver, copper and nickel, as shown in Table 7, are $10^{13.8}$, $10^{14.2}$ and $10^{14.7}\ \mathrm{K\ s^{-1}}$, respectively.

It should be pointed out the cooling rate to form an industrial metallic glass is lower than $R_{\mathrm{ig}}$. For comparison, we can introduce a critical cooling rate $R_{\mathrm{cg}}$, which is the largest cooling rate to form a simple crystal. As shown in Fig. 10, in the cooling rate region between $R_{\mathrm{cg}}$ and $R_{\mathrm{ig}}$, although nucleation can take place in the undercooled melt when the temperature is lower than $T_{\mathrm{v}}$, a completely crystalline structure cannot be obtained as the growth rate of

![](./images/813318469536710656_12.jpg)

Fig. 10. The predicted critical cooling rate to form ideal metallic glass in a silver sample with 23,328 atoms (where $C$ represents the crystal, as shown in Fig. 11b, CG represents part glass and part crystal, as shown in Fig. 11d and IG represents the ideal glass, as shown in Fig. 11c).

<table>
<caption>Table 7
The predicted and simulated results for the critical cooling rate to form metallic glasses in silver, copper and nickel (where $R_{\text{ig}}$ is the predicted result from the present crystal–melt interfacial energy model and $R_{\text{igs}}$ is the simulated result).</caption>
<thead>
<tr>
<th>Metal</th>
<th>$V$ ($\text{m}^3$)</th>
<th>$R_{\text{cg}}$
(K s$^{-1}$)</th>
<th>$R_{\text{ig}}$
(K s$^{-1}$)</th>
<th>$R_{\text{igs}}$
(K s$^{-1}$)</th>
<th>EAM
potential</th>
</tr>
</thead>
<tbody>
<tr>
<td>Silver</td>
<td>$10^{-24.4}$</td>
<td>$10^{12.0}$</td>
<td>$10^{13.8}$</td>
<td>$10^{14.0}$</td>
<td>[41]</td>
</tr>
<tr>
<td>Copper</td>
<td>$10^{-24.7}$</td>
<td>$10^{12.2}$</td>
<td>$10^{14.2}$</td>
<td>$10^{14.4}$</td>
<td>[43]</td>
</tr>
<tr>
<td>Nickel</td>
<td>$10^{-24.7}$</td>
<td>$10^{12.4}$</td>
<td>$10^{14.7}$</td>
<td>$10^{14.6}$</td>
<td>[43]</td>
</tr>
</tbody>
</table>

the crystal is very small at that temperature. In other words, when the cooling rate is lower than $R_{\text{ig}}$ but higher than $R_{\text{cg}}$ the solidification structure consists of glass and crystal, as shown in Fig. 11d. So the cooling rate to form an industrial metallic glass should be larger than $R_{\text{cg}}$ but smaller than $R_{\text{ig}}$. The results for $R_{\text{cg}}$ simulated by us based on the EAM potentials of silver [41], copper [43] and nickel [43] are listed in Table 7.

### 4.3.2. Simulation of the critical cooling rate to form an ideal metallic glass

The bond orientational order parameter (BOP), radial distribution function and potential analyses were used to simulate the critical cooling rates to form ideal metallic glasses of silver, copper and nickel. The processing procedures were as follows:

- heating the sample at a temperature 300 K higher than the melting point until the solid had completely melted;
- holding the melted sample at the temperature for 6000 ps;
- cooling the melted sample to 50 K at different cooling rates;
- relaxing the sample at 50 K for 2000 ps.

Fig. 11 shows snapshots of cross-sectional views of silver samples with 23,328 atoms under different conditions. Different colored balls denote atoms with different BOP values. The color varies in the visible spectrum from blue to red, and the corresponding BOP is in the region 0.61–0.13. When silver is heated at 1567 K, which is higher than the melting point, as shown in Fig. 11a a homogeneous structure formed of atoms with different BOP values (different colors) is obtained. At this temperature silver is in the liquid state, which is a non-crystalline form. When silver is cooled from 1567 to 50 K at a rate of $10^{12.0}$ K s$^{-1}$ as shown in Fig. 11b a uniform structure formed of atoms

![](./images/813318469536710656_13.jpg)

Fig. 11. Snapshots of a cross-sectional view when a silver sample with 23,328 atom was cooled from 1567 to 50 K and relaxed at 50 K for 2000 ps (BOP is the bond orientational order parameter). (a) 1567 K; (b) $R_{\text{c}}=10^{12.0}$ K s$^{-1}$; (c) $R_{\text{c}}=10^{14.0}$ K s$^{-1}$; (d) $R_{\text{c}}=10^{13.0}$ K s$^{-1}$.

with the maximum BOP value is obtained. The maximum BOP corresponds to the crystalline state. This indicates that when the cooling rate is $10^{12.0}\ \text{K s}^{-1}$ silver is transformed from a non-crystalline form to a crystalline form. In other words, the value of $T_{\text{cg}}$ for the silver sample is $10^{12.0}\ \text{K s}^{-1}$. When the cooling rate is $10^{14.0}\ \text{K s}^{-1}$ as shown in Fig. 11c a homogeneous structure is formed of atoms with different BOP values (different colors). This structure is similar to that in Fig. 11a (a non-crystalline form), therefore, it can be predicted that silver should be in a non-crystalline form when the cooling rate is $10^{14.0}\ \text{K s}^{-1}$. This non-crystalline form should be a glass because the relaxation temperature (50 K) is much lower than the critical glass transition temperature ($0.25T_{\text{m}}$ [46]). When silver is cooled at a cooling rate ranging from $10^{12.0}$ to $10^{14.0}\ \text{K s}^{-1}$ as shown in Fig. 11d a heterogeneous structure composed of two types of phases is obtained. One is the continuous phase formed by atoms with different BOP values (different colors), which is identical to that in Fig. 11c, and the other is the discontinuous phase formed by atoms with high BOP values (the blue colored balls), which is the same as that in Fig. 11b. These results show that when the cooling rate ranges from $10^{12.0}$ to $10^{14.0}\ \text{K s}^{-1}$ nucleation and part crystallisation should have occurred in the system. From the above results from BOP analysis it can be concluded that the value of $R_{\text{ig}}$ for the silver sample is not higher than $10^{14.0}\ \text{K s}^{-1}$, while the value of $R_{\text{cg}}$ is not lower than $10^{12.0}\ \text{K s}^{-1}$.

Fig. 12 shows the effect of the cooling rate on the radial distribution function of the silver sample with 23,328 atoms. When the cooling rate is $10^{12.0}\ \text{K s}^{-1}$ the radial distribution function shows the typical features of a crystal, which implies that nucleation and crystallisation should have occurred in the system. This is in agreement with the results of the BOP analysis shown in Fig. 11b. When the cooling rate is not less than $10^{13.0}\ \text{K s}^{-1}$ the radial distribution function shows the typical features of an amorphous material, which means that the system is now principally composed of the amorphous phase. Because the effects of the crystal phase on the radial distribution function are atypical when the ratio of the crystalline phase to the amorphous phase is lower than a certain value the absence of nucleation and crystallisation in the sample when the cooling rate is not less than $10^{13.0}\ \text{K s}^{-1}$ cannot be ascertained. In other words, it cannot be concluded that the value of $R_{\text{ig}}$ for the silver sample is $10^{13.0}\ \text{K s}^{-1}$.

In order to determine an accurate value of $R_{\text{ig}}$ for the silver sample the potential of the silver sample was studied. Because the potential of the crystal should be lower than that of the melt and because there is no energy variation in the transformation process from the melt to the glass the potential of the glass should be higher than that of the crystal. Thus the potential of the mixture of glass and crystal should be lower than that of the simple glass. Moreover, the potential of the mixture of glass and crystal should vary with the cooling rate, because the cooling rate can influence the ratio of glass to crystal. In contrast, if the system is entirely composed of glass, the potential of the system should not vary with the cooling rate.

Fig. 13 shows typical potential curves as a function of the relaxation time for the silver sample cooled from 1567 to 50 K at different cooling rates and relaxed at 50 K for 2000 ps. In the cooling rate region $10^{12.0}$–$10^{14.0}\ \text{K s}^{-1}$ the potential increases with increasing cooling rate, indicating that the system is composed of glass and crystal. In other words, nucleation and part crystallisation should have occurred in the system when the cooling rate is in the region $10^{12.0}$–$10^{14.0}\ \text{K s}^{-1}$. When the cooling rate is increased to $10^{14.0}\ \text{K s}^{-1}$ the potential reached close to the maximum value of $-64375\ \text{eV}$. Moreover, the potential does not change with cooling rate when the cooling rate is increased above $10^{14.0}\ \text{K s}^{-1}$. This means that when the cooling rate is above $10^{14.0}\ \text{K s}^{-1}$ the system is entirely composed of glass. Consequently it can be deduced that the critical cooling rate that precludes nucleation in the

![](./images/813318469536710656_14.jpg)

Fig. 12. Effect of cooling rate on the radial distribution function after a silver sample with 23,328 atoms was cooled from 1567 to 50 K and then relaxed at 50 K for 2000 ps.

![](./images/813318469536710656_15.jpg)

Fig. 13. Dependence of the potential on the relaxation time after a silver sample with 23,328 atoms was cooled from 1567 to 50 K and then relaxed at 50 K for 2000 ps.

silver sample (i.e. the critical cooling rate to form an ideal metallic glass) is $10^{14.0}\ \text{K s}^{-1}$. According to the crystal-melt interfacial energy model proposed in this study the value of $R_{\text{ig}}$ for the silver sample, as listed in Table 7, is predicted to be $10^{13.7}\ \text{K s}^{-1}$. Therefore, the value of $R_{\text{ig}}$ for the silver sample, as predicted from the present crystal-melt interfacial energy model, is in good accord with the simulated results.

Using the same method, the values of $R_{\text{ig}}$ and $T_{\text{cg}}$ for copper and nickel samples with 14,440 atoms were also simulated from BOP analysis, the radial distribution function and potential analyses. Table 7 lists the simulated results for $T_{\text{ig}}$ and $T_{\text{cg}}$ for the copper and nickel samples. As listed in Table 7, the simulated value of $R_{\text{ig}}$ for the copper sample is $10^{14.4}\ \text{K s}^{-1}$, which is almost equal to the predicted result from the crystal-melt interfacial energy model proposed in this study, $10^{14.2}\ \text{K s}^{-1}$. For the nickel sample the simulated result for $R_{\text{ig}}$ and the predicted result from the present crystal-melt interfacial energy model are $10^{14.6}$ and $10^{14.7}\ \text{K s}^{-1}$, respectively. Clearly, the difference between them is very small, so the critical cooling rates to form an ideal metallic glass of copper and nickel predicted from the present crystal-melt interfacial energy model also agree well with the simulated results.

Thus over a wide temperature range from the melting point to the glass transition temperature the predicted results from the present crystal-melt interfacial energy model agree well with the experimental and simulated results for crystal-melt interfacial energy, homogeneous nucleation undercooling and the critical cooling rate to form ideal metallic glasses of silver, copper and nickel. Finally, it is worth noting that the present crystal-melt interfacial energy model can be developed to predict the crystal-melt interfacial energy of alloys. The predicted results of the crystal-melt interfacial energy determined using the developed model are in good agreement with the experimental data obtained using the GBG technique for Al-Si [21], Al-Cu [21], Al-Mg [22], Al-Ni [23], Al-Ti [23], Al-Ag [24], Sn-Pb [21], Sn-Ag [24], Sn-Cd [47], Bi-Cd [48,49], Cu-Zn [50] and Zn-Mg [51] alloys. The work in the crystal-melt interfacial energy of alloys will be published later.

Studies [52,53] have shown that liquid at a crystal interface exhibits crystal-induced ordering in the first three to four layers. In this study the description of the crystal-melt interface is based on the first crystal layer A, the crystal-melt layer B and the first liquid layer C. In spite of this simplification of the crystal-liquid interface in this paper, the predicted results for the crystal-melt interfacial energy, the homogeneous nucleation undercooling and the critical cooling rate to form an ideal metallic glass determined using the present crystal-melt interface model are in good agreement with the reported experimental results and simulated results based on the EAM potentials of the metals. These indicate that only atoms of the melt in layers B and C, which directly adjoin the atoms of the crystal in the crystal-melt interface, play decisive roles in the crystal-melt interfacial energy. The other melt atoms that do not directly adjoin the atoms of the crystal at the crystal-melt interface, such as the atoms in the second and third liquid layers, have a very weak influence on the crystal-melt interfacial energy. Thus the nucleus radius should be defined from the position of layer C.

## 5. Conclusions
1. The model proposed in this study can be used to predict the crystal-melt interfacial energy at the melting point and in the undercooled state. The crystal-melt interfacial energy increases nonlinearly with temperature. The crystal-melt interfacial energies for silver, copper and nickel, as determined from the present crystal-melt interfacial energy model, are in good agreement not only with the experimental results determined using the DA and CA techniques at the melting point but also with the experimental results determined using MU and the simulated results determined using HU at the homogeneous nucleation temperature.
2. The homogeneous nucleation undercoolings predicted using the present crystal-melt interfacial energy model for silver, copper and nickel agree well with the simulated and experimental results.
3. The critical cooling rates to form ideal metallic glasses simulated by the MD method are identical to the predicted results from the present crystal-melt interfacial energy model for silver, copper and nickel.

## Acknowledgements
This work was supported by the National Basic Research Program (Project 973) of China (Grant No. 2011CB610403), the National Natural Science Foundation of China (Grants Nos. 51071115, 51171136 and 50671075) and the Program for Innovative Science and Research Team of Xi'an Technological University (Solidification and Functional Materials).

## References
[1] Turnbull D. J Appl Phys 1950;21:1022.
[2] Asta M, Beckermann C, Karma A, Kurz W, Napolitano R, Plapp M, et al. Acta Mater 2009;57:941.
[3] Kelton KF. Solid State Phys 1991;45:75.
[4] Perepezko JH. Mater Sci Eng 1984;65:125.
[5] Hoyt JJ, Asta M, Karma A. Mater Sci Eng R 2003;41:121.
[6] Kurz W, Fisher DJ. Acta Metall 1981;29:11.
[7] Trivedi R, Lipton J, Kurz W. Acta Metall 1987;35:957.
[8] Kurz W, Trivedi R. Acta Metall Mater 1990;38:1.
[9] Li D, Herlach DM. Phys Rev Lett 1996;77:1801.
[10] Jian Z, Kuribayashi K, Jie W. Acta Mater 2004;52:3323.
[11] Powell GLF. J Aust Inst Metals 1965;10:223.
[12] Jian Z, Jie W. Metall Mater Trans A 2001;31:391.
[13] Willnecker R, Herlach DM, Feuerbacher B. Mater Sci Eng 1988;98:85.

[14] Skripov VE. In: Kaldis E, Scheel HJ, editors. Current topics in materials science. Amsterdam: North-Holland; 1977.

[15] Flemings MC, Shiohara Y. Mater Sci Eng 1984;65:157.

[16] Waseda Y, Miller WA. Trans Jpn Inst Met 1978;19:546.

[17] Granasy L, Borzsonyi T, Pusztai T. Phys Rev Lett 2002;88:206105.

[18] Eustathopoulos N, Coudurier L, Joud JC, Desre P. J Cryst Growth 1976;33:105.

[19] Wenzl H, Fattah A, Velhoff W. J Cryst Growth 1976;36:319.

[20] Naidich YV, Perevert VM, Lebovich EM, Obushcha LP, Grigoren NF. Zh Fiz Chem 1973;47:1574.

[21] Gündüz M, Hunt JD. Acta Metall 1985;33:1651.

[22] Gündüz M, Hunt JD. Acta Metall 1988;37:1839.

[23] Marasli N, Hunt JD. Acta Mater 1996;44:1085.

[24] Engin S, Böyük U, Maraşlı N. J Alloys Compd 2009;488:138.

[25] Broughton JQ, Gilmer GH. J Chem Phys 1986;84:5759.

[26] Hoyt JJ, Asta M, Haxhimali T, Karma A, Napolitano RE, Trivedi R. MRS Bull 2004;29:935.

[27] Davidchack RL, Laird BB. J Phys Chem B 2005;109:17802.

[28] Spaepen F. Acta Metall 1975;23:729.

[29] Spaepen F, Meyer RB. Scipta Metall 1976;10:257.

[30] Jian Z, Kuribayashi K, Jie W. Acta Mater 2006;54:3323.

[31] Jian Z, Yang X, Chang F, Jie W. Metall Mater Trans A 2010;41:1826.

[32] Jian Z, Chen J, Chang F, Jie W. Metall Mater Trans A 2011;42:3785.

[33] Stiffler SR, Thompson MO, Peercy PS. Phys Rev Lett 1988;60:2519.

[34] Devaud G, Turnbull D. Acta Metall 1987;35:765.

[35] Turkdogen ET. Physical chemistry of high temperature technol- ogy. New York: Academic Press; 1980.

[36] Brandes EA, Brook GB. Smithells metals reference book. 7th ed. Oxford: Butterworth; 1992.

[37] David R. CRC handbook of chemistry and physics. Tokyo: CRC Press; 1989.

[38] Guthrie RIL, Iida T. Mater Sci Eng A 1994;178:35.

[39] Barin I, Knacke O. Thermochemical properties of inorganic sub- stances. Berlin: Springer-Verlag; 1973.

[40] Plimpton SJ. J Comput Phys 1995;117:1.

[41] Williams P, Mishin Y, Hamilton J. Mater Sci Eng 2006;14:817.

[42] Ackland GJ, Tichy GI, Vitek V, Finnis MW. Phil Mag 1987;56:735.

[43] Adams JB, Foiles SM, Wolfer WG. J Mater Res 1989;4:102.

[44] Foiles S. Phys Rev B 1985;32:7685.

[45] Tournier RF. Phys B 2007;392:79.

[46] Thomopson CV, Spaepen F. Acta Metall 1983;31:2021.

[47] Saatçi B, Çimen S, Pamuk H, Gündüz M. J Phys Condense Matter 2007;19:326219.

[48] Erol M, Maraslı N, Keslioğlu K, Gündüz M. Scripta Mater 2004;51:131.

[49] Keslioğlu K, Erol M, Maraslı N, Gündüz M. J Alloys Compd 2004;385:207.

[50] Kaygısız Y, Akbulut S, Ocak Y, Keslioğlu K, Maraslı N, Cadırlı E, et al. J Alloys Compd 2009;487:103.

[51] Erol M, Keslioğlu K, Maraslı N. Metall Mater Trans A 2007;38:1539.

[52] Reedjik M F, Arsic J, Hollander FFA, De Vries SA, Vlieg E. Phys Rev Lett 2003;90:066103.

[53] Davidchack RL, Laird BB. J Chem Phys 1998;108:9452.
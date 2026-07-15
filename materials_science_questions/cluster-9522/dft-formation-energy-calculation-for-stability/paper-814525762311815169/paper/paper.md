# Effect of Ni and Pd Addition on Mechanical, Thermodynamic, and Electronic Properties of $\boldsymbol{\mathrm{AuSn_4}}$-Based Intermetallics: A Density Functional Investigation

YALI TIAN, $^{1,2}$ WEI ZHOU, $^{1}$ and PING WU $^{1,3}$

1.—Department of Applied Physics, Institute of Advanced Materials Physics, Tianjin Key Laboratory of Low Dimensional Materials Physics and Preparing Technology, Faculty of Science, Tianjin University, Tianjin 300072, People's Republic of China. 2.—Department of Applied Physics, Tianjin University of Commerce, Tianjin 300134, People's Republic of China. 3.—e-mail: pingwu@tju.edu.cn

The effects of Ni and Pd addition on the mechanical, thermodynamic, and electronic properties of $\mathrm{AuSn_4}$-based intermetallic compounds (IMCs) have been investigated by first-principles calculations to reveal the essence of Au embrittlement. Three kinds of doped (namely Ni-doped, Pd-doped, and Ni/Pd-codoped) IMCs are considered in this work. The polycrystalline elastic properties are deduced from single-crystal elastic constants. It is found that the doped systems together with nondoped $\mathrm{AuSn_4}$ are all ductile phases. For Ni-doped $\mathrm{AuSn_4}$, the modulus, hardness, brittleness, Debye temperature, and minimum thermal conductivity increase with the Ni fraction, but this is not the case for the Pd-doped material, since $\mathrm{Au_{0.75}Pd_{0.25}Sn_4}$ is the more brittle phase. For $\mathrm{Au_{0.5}Pd_{0.25}Ni_{0.25}Sn_4}$, the mechanical, thermodynamic, and electronic properties are similar to those of $\mathrm{Au_{0.5}Pd_{0.5}Sn_4}$.

**Key words:** Intermetallic compounds, *ab initio* calculations, mechanical properties, brittleness, ductility

## INTRODUCTION

In electronics packaging, intermetallic compounds (IMCs) produced between solder and solder pads critically affect the reliability of surface-mounted assemblies. $^{1,2}$ Due in part to the microstructural mismatch of the IMCs with the solder and substrate, a thick layer of IMCs often causes the interface of the solder joint to become more sensitive to stress. Another important factor influencing solder joint reliability is the board finish selected for solder application. In ball grid array packaging, the contact pads for solder balls usually have $\mathrm{Au/Ni}$ surface finish. $^{3,4}$ The surface layer of $\mathrm{Au}$, which is always $0.2\ \mu\mathrm{m}$ to $1.0\ \mu\mathrm{m}$ thick, prevents oxidation of the Ni layer and retains good wettability, while the surface layer of $\mathrm{Ni}$, which is about $5\ \mu\mathrm{m}$ to $10\ \mu\mathrm{m}$ thick, is used as a diffusion barrier to prevent the otherwise rapid reaction between the solder and the $\mathrm{Cu}$ substrate. During the reflow process, the $\mathrm{Au}$ layer disappears from the interface, leaving the $\mathrm{Ni}$ layer exposed to solder; the entire $\mathrm{Au}$ layer is converted to $\mathrm{AuSn_4}$. However, $\mathrm{AuSn_4}$ is not a pure binary compound, since $\mathrm{Ni}$ atoms can enter the $\mathrm{AuSn_4}$ lattice to substitute for $\mathrm{Au}$ atoms. An appreciable amount of $\mathrm{Ni}$ dissolves in the $\mathrm{AuSn_4}$, forming $(\mathrm{Au,Ni})\mathrm{Sn_4}$ ternary compounds that make the interface susceptible to fracture. Electroless nickel electroless palladium immersion gold (ENEPIG), a trilayer structure composed of electroless $\mathrm{Ni}$, electroless $\mathrm{Pd}$, and immersion $\mathrm{Au}$, has nowadays become the most popular surface finish for $\mathrm{Cu}$ substrate and is widely used in three-dimensional integrated-circuit interconnects $^{5,6}$ and high-end electronics applications. $^{7}$ In such packaging, the $\mathrm{Au}$ layer always has thickness of $0.1\ \mu\mathrm{m}$, the $\mathrm{Pd}$ layer is $0.2\ \mu\mathrm{m}$ thicker than the $\mathrm{Au}$, and the $\mathrm{Ni}$ layer is usually $7\ \mu\mathrm{m}$ thick. $^{8}$ The $\mathrm{Pd}$ layer between the $\mathrm{Au}$ and $\mathrm{Ni}$ layers is also used as a

(Received December 8, 2015; accepted April 27, 2016)

Published online: 10 May 2016

diffusion barrier to protect the Ni layer from corrosion and prevent its diffusion into the Au surface. During the reflow process, dissolved Au and Pd atoms enter the molten solder and subsequently precipitate out as (Au,Pd)Sn₄ particles. Furthermore, such (Au,Pd)Sn₄ particles migrate to the Ni surface to form a continuous (Au,Pd,Ni)Sn₄ layer, which also results in inferior mechanical stability.⁷

A number of studies have focused on the crystal structure and phase stability of Au–Ni–Sn ternary IMCs. For example, Alexandra et al. examined the Au–Ni–Sn phase relations using experimental methods such as powder x-ray diffraction analysis, metallography, and electron microprobe analysis, obtaining evidence for the existence of AuNi₂Sn₄.⁹ Ho et al. discovered the AuₓNi₁₋ₓSn₄ phase between eutectic Pb–Sn solder and solder ball pads with Au/ Ni surface finish and indicated a value of x between 0.99 and 0.75.³ According to Zavalij's work, approximately 50% of the Au atoms can be substituted by Ni atoms in the AuSn₄ lattice.¹⁰ Yoon et al. experimentally evaluated the mechanical reliability of Au-Sn/Ni flip-chip solder bumps and found the existence of the (Ni,Au)₃Sn₄ phase.¹¹ Recently, Dong calculated the Au–Ni–Sn ternary solubility using the Calphad method based on available experimental results for the Au–Sn and Ni–Sn systems, deriving that Ni can dissolve in AuSn₄ to a level of about 10.4 at.%.¹² The Ni content in AuSn₄ varies according to the location of the intermetallics, ranging from 5% to 10.5%, as reported in different experimental works.¹⁰ However, the (Au,Ni)Sn₄ layer is extremely brittle and fragile, which might significantly deteriorate the mechanical properties of solder joints and lower their reliability.¹³ Similarly, (Au,Pd)Sn₄ together with (Au,Pd,Ni)Sn₄ also show the same problem of inferior mechanical performance as (Au,Ni)Sn₄. This phenomenon is often called Au embrittlement. Many research groups have devoted themselves to elimination of such Au embrittlement by circumventing the continuous layer of (Au,Ni)Sn₄ at the solder interface. A sufficient approach is to add a relatively large amount of Cu into the microjoints, so that the Cu pillar is in direct contact with the solder, avoiding formation of the compounds responsible for embrittlement.⁷ Another successful approach used in past decades was to limit the Au and Pd concentration to typically 0.1 wt.% to avoid brittle compounds.⁷

As mentioned above, both Ni and Pd layers are used as diffusion barriers, and both Ni and Pd atoms can enter the AuSn₄ lattice, leading to inferior stability. Although study of Au embrittlement has attracted increasing attention from researchers, systematic exploration of the (Au,Ni)Sn₄, (Au,Pd)Sn₄, and (Au,Pd,Ni)Sn₄ compounds has not been undertaken to date. However, such research should continue because the essence of Au embrittlement has still not been revealed. In this work, to address this question, the structural, elastic, thermodynamic, and electronic properties of Au₁₋ₓMₓSn₄ (M = Ni and Pd; x = 0, 0.25, 0.5) compounds were studied by first-principles calculations based on density functional theory with a view of providing a more fundamental interpretation of the origin of Au embrittlement.

## CALCULATION DETAILS

AuSn₄ has been shown to have orthorhombic PdSn₄ structure in noncentrosymmetric space group *Aba2* (no. 41).¹⁴ The ternary compound (Au,Ni)Sn₄ has the same crystal structure as AuSn₄.¹⁵,¹⁶ Moreover, it has been reported that NiSn₄ (where all of the Au atoms in the AuSn₄ lattice are substituted by Ni atoms) formed during solidification of Sn-Ni alloy has crystal structure isomorphous to PtSn₄.¹⁷ We know that PtSn₄ has the same crystal prototype as AuSn₄. So, it is rational to claim that Au₁₋ₓNiₓSn₄ will retain a crystallographic structure similar to AuSn₄. The crystal structure of AuSn₄ (Fig. 1) consists of 20 atoms (4 Au and 16 Sn atoms). That is to say, AuSn₄ in fact should be Au₄Sn₁₆. When one Au atom is replaced by a Ni atom, the cell becomes Au₃NiSn₁₆ (namely Au₀.₇₅Ni₀.₂₅Sn₄, corresponding to 5% Ni solubility in the AuSn₄ lattice). When two Au atoms are replaced by Ni atoms, it becomes Au₂Ni₂Sn₁₆ (namely Au₀.₅Ni₀.₅Sn₄, corresponding to 10% Ni solubility in the AuSn₄ lattice). It has been reported that substitution of approximately one-half of the Au atoms with Ni corresponds to the solubility limit.¹⁰ In addition, the reported experimental product (Au,Ni)Sn₄ has two constituents, namely Au₀.₇₅Ni₀.₂₅Sn₄ and Au₀.₅Ni₀.₅Sn₄. So, the gradient of Ni in AuSn₄ is only described by two compositions of Au₁₋ₓNiₓSn₄ (x = 0.25, 0.5), and the models for these compounds can be established based on the conventional AuSn₄ cell to achieve accurate results. We could not find any literature reports on the crystal structure of (Au,Pd)Sn₄ or (Au,Pd,Ni)Sn₄ in the Inorganic Crystal Structure Database. However, PdSn₄, where all of the Au atoms in AuSn₄ are replaced by Pd atoms, has the same crystal structure as AuSn₄. Therefore, the (Au,Pd)Sn₄ and (Au,Pd,Ni)Sn₄ structures are all established according to the AuSn₄ structure. The experimental lattice constants $a = 6.51$ Å, $b = 6.52$ Å, and $c = 11.71$ Å at room pressure and temperature are used for AuSn₄. The AuSn₄ structure highlighting the four different positions occupied by Au atoms is shown in Fig. 1. For Au₁₋ₓMₓSn₄ (M = Ni and Pd; x = 0.25, 0.5) structures, the Ni and Pd atoms can replace Au atoms in random fashion at these different positions.¹⁰

All calculations were performed using the Vienna *ab initio* simulation package. The exchange-correlation functional was treated with the Perdew–Burke–Ernzerhof generalized gradient approximation. Brillouin-zone integrations were performed using $2 \times 4 \times 4$ Monkhorst–Pack $\mathbf{k}$-point meshes, and electronic occupancies were determined

according to the Methfessel–Paxton technique with 0.1-eV smearing. The valence atomic configurations were $5d^{10}6s^{1}$ for Au, $3d^{8}4s^{2}$ for Ni, $5s^{2}5p^{2}$ for Sn, and $4d^{10}$ for Pd, and the cutoff energy was 360 eV. The convergence threshold for the total energy was set to less than $5\times 10^{-6}$ eV/atom.

# RESULTS AND DISCUSSION
## Structure and Phase Stability

For AuSn₄, the optimized lattice constants together with the available experimental data are presented in Table I. The calculated values have very small errors compared with the experimental results, proving the rationality of the computational method used in this work.

![](./images/814525762311815169_1.jpg)

Fig. 1. Crystal structure of AuSn₄ (tin atoms are grey, gold atoms are yellow) (Color figure online).

The energetically favorable sites for Ni atom substitution in the $\mathrm{Au_{1-x}Ni_{x}Sn_{4}}$ ($x = 0.25$, $0.5$) structures were analyzed based on the following compositionally averaged energy of formation $(\Delta H)^{18}$:

$$
\Delta H=\frac{1}{5}\left[E_{\mathrm{Au}_{1-x}\mathrm{Ni}_{x}\mathrm{Sn}_{4}}-\left(xE_{\mathrm{Ni}}+(1-x)E_{\mathrm{Au}}+4E_{\mathrm{Sn}}\right)\right],
\tag{1}
$$

where $E_{\mathrm{Au}_{1-x}\mathrm{Ni}_{x}\mathrm{Sn}_{4}}$ denotes the total energy of the compound $\mathrm{Au_{1-x}Ni_{x}Sn_{4}}$ at the equilibrium lattice constant, and $E_{\mathrm{Au}}$, $E_{\mathrm{Ni}}$, and $E_{\mathrm{Sn}}$ are the energies per atom of Au and Ni with face-centered cubic structure and $\beta$-Sn with tetragonal structure in solid state, respectively.

To derive the most stable structure of the Ni-doped IMCs, the energy of formation for a total of ten different substitution sites (four for $\mathrm{Au_{0.75}Ni_{0.25}Sn_{4}}$ and six for $\mathrm{Au_{0.5}Ni_{0.5}Sn_{4}}$) including AuSn₄ were considered in this work. The calculated most stable structures are listed in Table I. For AuSn₄, the calculated energy of formation is $-10.19$ kJ/mol atoms, which is very close to the value of $-9.71$ kJ/mol atoms from Yang's first-principles calculations,¹⁸ but represents a small deviation from the experimental results quoted by Gosh; For example, Misra et al. derived an energy of formation of $-7.744\pm 0.126$ kJ/mol atoms, while Kleppa's result was $-6.902\pm 0.500$ kJ/mol atoms.¹⁹ In addition, Calphad results are different, including $-7.439$ kJ/mol atoms, $-9.770$ kJ/mol atoms, and $-7.117$ kJ/mol atoms. The experimental and Calphad values are all room-temperature results. The small differences between our first-principles results and the experimental values mean that the structure of AuSn₄ is reliable. Considering the different occupation sites for the Ni-doped IMCs, we found that the $\mathrm{Au_{0.75}Ni_{0.25}Sn_{4}}$ structure with the Ni atom at the Au2 site has the largest negative energy of formation. For the $\mathrm{Au_{0.5}Ni_{0.5}Sn_{4}}$ structure with the Ni solubility in AuSn₄ increased to 10 at.%, the structure with Ni atoms at the Au1 + Au4 sites has the maximum negative energy of formation, corresponding to the most thermodynamic stable structure. In the next section, we present first-principles calculations on the two most stable structures of $\mathrm{Au_{0.75}Ni_{0.25}Sn_{4}}$ (Ni

<table>
<thead>
<tr>
<th colspan="2">Table I. Calculated lattice constants (Å), volume (Å³), and energy of formation $\Delta H$ (kJ/mol atoms) for nondoped and impurity-doped AuSn₄ IMCs</th>
<th></th>
<th></th>
<th></th>
</tr>
<tr>
<th>IMC</th>
<th>Occupied site</th>
<th>Lattice constants</th>
<th>Volume</th>
<th>$\Delta H$</th>
</tr>
</thead>
<tbody>
<tr>
<td>AuSn₄</td>
<td>–</td>
<td>6.67, 6.52, 12.00</td>
<td>521.51</td>
<td>$-10.19$</td>
</tr>
<tr>
<td>Experiment</td>
<td>–</td>
<td>6.51, 6.52, 11.71</td>
<td>496.78</td>
<td>$-7.74^{16}$</td>
</tr>
<tr>
<td>$\mathrm{Au_{0.75}Ni_{0.25}Sn_{4}}$</td>
<td>Au₂</td>
<td>6.55, 6.55, 11.82</td>
<td>507.46</td>
<td>$-11.38$</td>
</tr>
<tr>
<td>$\mathrm{Au_{0.5}Ni_{0.5}Sn_{4}}$</td>
<td>Au₁ + Au₄</td>
<td>6.49, 6.53, 11.65</td>
<td>493.43</td>
<td>$-12.65$</td>
</tr>
<tr>
<td>$\mathrm{Au_{0.75}Pd_{0.25}Sn_{4}}$</td>
<td>Au₂</td>
<td>6.59, 6.57, 11.86</td>
<td>513.78</td>
<td>$-29.85$</td>
</tr>
<tr>
<td>$\mathrm{Au_{0.5}Pd_{0.5}Sn_{4}}$</td>
<td>Au₁ + Au₄</td>
<td>6.54, 6.60, 11.75</td>
<td>506.66</td>
<td>$-18.96$</td>
</tr>
<tr>
<td>$\mathrm{Au_{0.5}Pd_{0.25}Ni_{0.25}Sn_{4}}$</td>
<td>Au₁ + Au₄</td>
<td>6.51, 6.56, 11.71</td>
<td>500.22</td>
<td>$-15.83$</td>
</tr>
</tbody>
</table>

atom occupying Au2 site) and $Au_{0.5}Ni_{0.5}Sn_4$ (Ni atoms occupying Au1 + Au4 sites) to reveal the essence of Au embrittlement. It can be found that the absolute energy of formation increases with the Ni fraction, indicating that substitution leads to more thermodynamically stable structures than $AuSn_4$, and that the $Au_{0.5}Ni_{0.5}Sn_4$ structure is more stable than $Au_{0.75}Ni_{0.25}Sn_4$. For the $(Au,Pd)Sn_4$ structure, we considered the same substitution site for Pd as for Ni in the $(Au,Ni)Sn_4$ lattice, to simplify the calculation procedure. For the quaternary $(Au,Pd,Ni)Sn_4$ structure, we specified the Au1 site for substitution by Ni and the Au4 site for occupation by Pd. The energies of formation for these doped $AuSn_4$ IMCs are all summarized in Table I. The result is that the structures of the Pd-doped IMCs are more stable than the Ni-doped materials, with $Au_{0.75}Pd_{0.25}Sn_4$ being the most stable phase among them.

For the doped $AuSn_4$ IMCs, the calculated lattice constants and cell volume are also listed in Table I. The lattice constants $a$ and $c$ all decreased while the constant $b$ increased on doping with impurities. For the Ni-doped system, the cell volume shrank with increasing Ni concentration due to the smaller atomic radius of Ni compared with Au. Such decrease of the cell volume would decrease the distance between the different atoms and further enhance the atomic interaction. For the Pd-doped system, the atomic radius of Pd is $1.79$ Å, exactly equal to that of Au, but the cell volume also decreases with increasing Pd concentration, with both compounds having lower values compared with the parent $AuSn_4$. This implies that strong bonding exists in $Au_{1-x}Pd_xSn_4$.

## Elastic Properties

The elastic constants such as the bulk modulus, Young's modulus, and Poisson's ratio are very important indicators of the mechanical properties for industrial applications of a material. To estimate the mechanical properties of the doped $AuSn_4$ IMCs, a stress-strain approach for the optimized structure was used to calculate the elastic stiffness. $^{20-22}$ Strain of $\delta \leq 2\%$ in steps of $0.005$ was applied to the equilibrium lattice to determine the change in total energy. The second-order elastic constants were deduced from a polynomial fit to the strain energy for specific deformation to the cell of orthorhombic $Au_{1-x}M_xSn_4$ (M = Ni, Pd; $x = 0, 0.25$, $0.5$). The nine independent elastic constants for single crystals are $C_{11}$, $C_{22}$, $C_{33}$, $C_{44}$, $C_{55}$, $C_{66}$, $C_{12}$, $C_{13}$, and $C_{23}$, the values of which are all summarized in Table II. The mechanical stability criteria for the orthorhombic crystal system are given by the following expressions:

$$
\begin{aligned}
&C_{ii}>0(i=1-6),\quad C_{11}+C_{22}>2C_{12}, \\
&C_{22}+C_{33}>2C_{23},\quad C_{11}+C_{33}>2C_{13}, \\
&C_{11}+C_{22}+C_{33}+2C_{12}+2C_{13}+2C_{23}>0.
\end{aligned} \tag{2}
$$

As shown in Table II, the calculated values of the elastic constants meet the mechanical stability criteria in Eq. 2, confirming that the structures of the doped $AuSn_4$ IMCs together with the parent phase are elastically stable. Based on the elastic stiffness constants, the polycrystalline elastic properties such as the bulk modulus $K$, shear modulus $G$, Young's modulus $E$, and Poisson's ratio $v$ can be estimated according to the following Voigt-Reuss-Hill (VRH) approximation. $^{20}$ For the orthorhombic system, the upper (Voigt) and lower (Reuss) bounds of the polycrystalline elastic modulus are:

$$K_{\mathrm{V}}=\frac{1}{9}\left[\left(C_{11}+C_{22}+C_{33}\right)+2\left(C_{12}+C_{13}+C_{23}\right)\right], \quad(3)$$

$$K_{\mathrm{R}}=\left[S_{11}+S_{22}+S_{33}+2\left(S_{12}+S_{13}+S_{23}\right)\right]^{-1}, \quad(4)$$

$$
\begin{aligned}
G_{\mathrm{V}}= & \frac{1}{15}\left[C_{11}+C_{22}+C_{33}-\left(C_{12}+C_{13}+C_{23}\right)\right. \\
& \left.+3\left(C_{44}+C_{55}+C_{66}\right)\right],
\end{aligned} \quad(5)
$$

$$
\begin{aligned}
G_{\mathrm{R}}= & 15\left[4\left(S_{11}+S_{22}+S_{33}\right)-4\left(S_{12}+S_{13}+S_{23}\right)\right. \\
& \left.+3\left(S_{44}+S_{55}+S_{66}\right)\right]^{-1}.
\end{aligned} \tag{6}
$$

Here, the subscripts "V" and "R" indicate the upper (Voigt) and lower (Reuss) bounds of the polycrystalline elastic modulus. The $S_{ij}$ are the elastic compliance constants, forming the inverse matrix of the elastic constants $C_{ij}$. The arithmetic average of the Voigt and Reuss results given by the

<table>
<caption>Table II. Calculated elastic stiffness ($C_{ij}$) of nondoped and impurity-doped $AuSn_4$ IMCs (units of GPa)</caption>
<thead>
  <tr>
    <th>IMC</th>
    <th>$C_{11}$</th>
    <th>$C_{22}$</th>
    <th>$C_{33}$</th>
    <th>$C_{44}$</th>
    <th>$C_{55}$</th>
    <th>$C_{66}$</th>
    <th>$C_{12}$</th>
    <th>$C_{13}$</th>
    <th>$C_{23}$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>$AuSn_4$</td>
    <td>79.5</td>
    <td>84.4</td>
    <td>70.5</td>
    <td>9.2</td>
    <td>2.3</td>
    <td>31.9</td>
    <td>29.1</td>
    <td>43.2</td>
    <td>58.7</td>
  </tr>
  <tr>
    <td>$Au_{0.75}Ni_{0.25}Sn_4$</td>
    <td>96.3</td>
    <td>93.6</td>
    <td>79.7</td>
    <td>12.7</td>
    <td>6.4</td>
    <td>42.0</td>
    <td>31.2</td>
    <td>34.5</td>
    <td>51.3</td>
  </tr>
  <tr>
    <td>$Au_{0.5}Ni_{0.5}Sn_4$</td>
    <td>105.6</td>
    <td>106.5</td>
    <td>95.3</td>
    <td>23.8</td>
    <td>14.6</td>
    <td>31.9</td>
    <td>39.8</td>
    <td>23.3</td>
    <td>38.2</td>
  </tr>
  <tr>
    <td>$Au_{0.75}Pd_{0.25}Sn_4$</td>
    <td>103.1</td>
    <td>92.3</td>
    <td>94.2</td>
    <td>18.5</td>
    <td>18.7</td>
    <td>35.9</td>
    <td>42.4</td>
    <td>25.4</td>
    <td>42.8</td>
  </tr>
  <tr>
    <td>$Au_{0.5}Pd_{0.5}Sn_4$</td>
    <td>94.6</td>
    <td>101.4</td>
    <td>85.4</td>
    <td>21.8</td>
    <td>15.0</td>
    <td>26.8</td>
    <td>43.4</td>
    <td>32.5</td>
    <td>42.5</td>
  </tr>
  <tr>
    <td>$Au_{0.5}Pd_{0.25}Ni_{0.25}Sn_4$</td>
    <td>93.0</td>
    <td>103.5</td>
    <td>83.9</td>
    <td>21.2</td>
    <td>15.5</td>
    <td>25.4</td>
    <td>42.4</td>
    <td>35.5</td>
    <td>44.1</td>
  </tr>
</tbody>
</table>

VRH approximation is often used to estimate the theoretical polycrystalline elastic modulus,²¹ the expression for which is written in the following form:

$$
K = \frac{K_{\mathrm{V}} + K_{\mathrm{R}}}{2}, \tag{7}
$$

$$
G = \frac{G_{\mathrm{V}} + G_{\mathrm{R}}}{2}. \tag{8}
$$

Then, the polycrystalline Young's modulus $E$, Poisson's ratio $v$, and hardness $H$ of the doped AuSn₄ IMCs together with nondoped AuSn₄ can be calculated based on the following expressions²²:

$$
E = \frac{9KG}{3K + G}, \tag{9}
$$

$$
v = \frac{3K - 2G}{2(3K + G)}, \tag{10}
$$

$$
H = \frac{(1 - 2v)E}{6(1 + v)}. \tag{11}
$$

The derived elastic modulus is presented in Table III. Since there are no available experimental data for the bulk or shear modulus of these impurity-doped materials, our calculation results cannot be verified. However, the Young's modulus from our calculations can be compared with some reported values. In our work, the Young's modulus of AuSn₄ is 31.0 GPa. In Chromik's work, it is $39 \pm 4$ GPa, as derived by interfacial layer and nanoindentation methods.²³ Recently, Wang et al. reported a value of 35.6 GPa, also obtained by nanoindentation.²⁴ However, in Gosh's research, the Young's modulus obtained by bulk resonance was 71.1 GPa.²⁵ The large discrepancy between the experimental values obtained by resonance versus nanoindentation may be due to the significant anelasticity exhibited by AuSn₄, because the unloading rate during nanoindentation varied in the range from 0.01 mN/s to 2.0 mN/s, making the results sensitive to anelasticity and resulting in lower modulus for lower unloading rate.²³ However, nanoindentation gave a relatively minor difference with our calculation.

This small deviation may be because lattice defects and anisotropy of AuSn₄ were not ruled out during all the experimental measurements. Through these comparisons, it can be said that our calculation result for the Young's modulus of AuSn₄ is reliable. For the (Au,Ni)Sn₄ structure, Chromik et al. obtained a Young's modulus of $48 \pm 3$ GPa by nanoindentation.²⁴ However, the exact composition of (Au,Ni)Sn₄ was not known. In this work, we found Young's moduli of 56.61 GPa and 68.28 GPa for Au₀.₇₅Ni₀.₂₅Sn₄ and Au₀.₅Ni₀.₅Sn₄, respectively. So, it can be deduced that the (Au,Ni)Sn₄ compound in Chromik's work was probably Au₀.₇₅Ni₀.₂₅Sn₄. Since no experimental or theoretical data for the elastic modulus of the Pd-doped compounds could be found in literature, our calculations for the Pd-doped AuSn₄ IMCs provide good support for future work.

The correlation between the elastic modulus and the doping impurity fraction is depicted in Fig. 2a–c. One can see that substitution of Au by Ni or Pd leads to an obvious increase of the shear modulus and Young's modulus of AuSn₄. However, the increment of the bulk modulus is very small, only 1.51 GPa and 1.72 GPa for Au₀.₇₅Ni₀.₂₅Sn₄ and Au₀.₅Ni₀.₅Sn₄, and 2.40 GPa and 2.95 GPa for Au₀.₇₅Pd₀.₂₅Sn₄ and Au₀.₅Pd₀.₅Sn₄, respectively. The different variation trends of the elastic modulus are due to the fact that the stress imposed in the different directions of the lattice caused different strain, indicating that the doped AuSn₄ IMCs are anisotropic materials.

The Zener anisotropy factor, $A_{\mathrm{Z}}$, is widely used to quantitatively analyze the degree of elastic anisotropy of a crystal. For noncubic crystal systems, the following expression is most popular among researchers²⁶:

$$
A_{\mathrm{Z}} = \frac{2C_{44}}{C_{11} - C_{12}}. \tag{12}
$$

$A_{\mathrm{Z}} = 1$ means that the nanostructure of the material is isotropic; otherwise, the material is anisotropic, and a larger deviation from unity indicates greater elastic anisotropy. According to the results in Table III, the investigated compounds are all anisotropic. However, $A_{\mathrm{Z}}$ becomes closer to unity as the doped atom fraction increases, meaning that these structures are very close to being

<table>
<caption>Table III. Polycrystalline elastic properties of nondoped and impurity-doped AuSn₄ IMCs; all units are GPa, except for $v$ and $K/G$ (dimensionless)</caption>
<thead>
<tr>
<th>IMC</th>
<th>$K$</th>
<th>$G$</th>
<th>$E$</th>
<th>$v$</th>
<th>$A_{\mathrm{Z}}$</th>
<th>$K/G$</th>
<th>$H$</th>
</tr>
</thead>
<tbody>
<tr>
<td>AuSn₄</td>
<td>54.40</td>
<td>11.12</td>
<td>30.03</td>
<td>0.404</td>
<td>0.36</td>
<td>4.89</td>
<td>0.70</td>
</tr>
<tr>
<td>Au₀.₇₅Ni₀.₂₅Sn₄</td>
<td>55.91</td>
<td>21.26</td>
<td>56.61</td>
<td>0.331</td>
<td>0.39</td>
<td>2.63</td>
<td>2.40</td>
</tr>
<tr>
<td>Au₀.₅Ni₀.₅Sn₄</td>
<td>56.12</td>
<td>26.32</td>
<td>68.28</td>
<td>0.297</td>
<td>0.73</td>
<td>2.13</td>
<td>3.56</td>
</tr>
<tr>
<td>Au₀.₇₅Pd₀.₂₅Sn₄</td>
<td>56.80</td>
<td>25.40</td>
<td>66.32</td>
<td>0.305</td>
<td>0.61</td>
<td>2.24</td>
<td>3.30</td>
</tr>
<tr>
<td>Au₀.₅Pd₀.₅Sn₄</td>
<td>57.35</td>
<td>22.91</td>
<td>60.65</td>
<td>0.324</td>
<td>0.85</td>
<td>2.50</td>
<td>2.69</td>
</tr>
<tr>
<td>Au₀.₅Pd₀.₂₅Ni₀.₂₅Sn₄</td>
<td>57.86</td>
<td>22.46</td>
<td>59.66</td>
<td>0.328</td>
<td>0.84</td>
<td>2.58</td>
<td>2.57</td>
</tr>
</tbody>
</table>

![](./images/814525762311815169_2.jpg)

Fig. 2. Variation of (a) bulk modulus (K), (b) shear modulus (G), (c) Young's modulus (E), and (d) Poisson's ratio (v, dimensionless) with the doped impurity fraction for AuSn₄-based IMCs.

elastically isotropic. Our finding of $A_Z = 0.73$ for $\text{Au}_{0.5}\text{Ni}_{0.5}\text{Sn}_4$ is in good agreement with Chromik's nanoindentation response for a bulk ingot of $\text{Au}_{0.5}\text{Ni}_{0.5}\text{Sn}_4$.²³

In addition, the Poisson's ratio $v$ and Pugh's criteria are two different rules typically used to estimate the brittle or ductile nature of materials. A Poisson's ratio $v$ larger than $0.26^{27,28}$ indicates that the material will behave in a ductile manner; otherwise, it will be brittle. Also, the larger the Poisson's ratio, the greater the plasticity. Pugh's criterion²⁹ roughly uses the ratio of the shear to bulk modulus to predict the brittle and ductile nature of a crystalline phase, with a high value of $K/G$ being associated with good ductility, while a low value indicates brittle nature. The critical value is 1.75. From the results in Table III, one can see that the Poisson's ratio $v$ values are all above 0.26, while $K/G$ is above 1.75, meaning that the doped systems together with the parent phase are all ductile materials. However, Ni doping causes the Poisson's ratio to decrease from 0.404 for $\text{AuSn}_4$ to 0.331 for $\text{Au}_{0.75}\text{Ni}_{0.25}\text{Sn}_4$ or 0.297 for $\text{Au}_{0.5}\text{Ni}_{0.5}\text{Sn}_4$, while $K/G$ decreases from 4.89 for $\text{AuSn}_4$ to 2.63 for $\text{Au}_{0.75}\text{Ni}_{0.25}\text{Sn}_4$ or 2.13 for $\text{Au}_{0.5}\text{Ni}_{0.5}\text{Sn}_4$. This hints that introduction of Ni into the $\text{AuSn}_4$ lattice decreases the ductility but conversely increases the brittleness. Here, we note that the Poisson's ratio value of 0.33 estimated by Chromik for $(\text{Au,Ni})\text{Sn}_4^{23}$ is well consistent with our calculated result for $\text{Au}_{0.75}\text{Ni}_{0.25}\text{Sn}_4$, again supporting our aforementioned guess regarding this material. The trend of the variation in the Poisson's ratio with impurity fraction is illustrated in Fig. 2d. From this, one can see that the $\text{Au}_{0.5}\text{Ni}_{0.5}\text{Sn}_4$ structure is more brittle than $\text{Au}_{0.75}\text{Ni}_{0.25}\text{Sn}_4$. For the Pd-doped system, introduction of Pd into the $\text{AuSn}_4$ lattice also resulted in brittle nature. However, the

![](./images/814525762311815169_3.jpg)

![](./images/814525762311815169_4.jpg)

![](./images/814525762311815169_5.jpg)

![](./images/814525762311815169_6.jpg)

![](./images/814525762311815169_7.jpg)

![](./images/814525762311815169_8.jpg)

Fig. 3. Total density of state (TDOS) and partial density of state (PDOS) of (a) AuSn₄, (b) Au₀.₇₅Ni₀.₂₅Sn₄, (c) Au₀.₅Ni₀.₅Sn₄, (d) Au₀.₇₅Pd₀.₂₅Sn₄, (e) Au₀.₅Pd₀.₅Sn₄, and (f) Au₀.₅Pd₀.₂₅Ni₀.₂₅Sn₄ (dashed lines at 0 eV denote the Fermi level $E_F$).

$Au_{0.75}Pd_{0.25}Sn_4$ structure is more brittle than $Au_{0.5}Pd_{0.5}Sn_4$.

According to the values of the Young's modulus and Poisson's ratio, we also estimated the hardness of the doped systems based on Eq. 11. The results are also listed in Table III. Ghosh reported a hardness value of $0.63\pm0.06$ GPa for AuSn₄ measured by the Vickers method.²⁵ Compared with our first-principles calculation of 0.70 GPa, it appears there is good agreement with this value. However, it

has long been known that solder joints with a significant amount of Au can cause serious mechanical instability, especially for Ni/Au pad metallurgies, which is attributed to formation of (Au,Ni)Sn₄. Chromik found a hardness value for (Au,Ni)Sn₄ of 1.8 ± 0.1 GPa. Unfortunately, the exact composition of that compound was not shown clearly. So, we estimated the hardness of (Au,Ni)Sn₄ based on our calculated elastic modulus. It can be seen that Ni doping increases the hardness of the ternary (Au, Ni)Sn₄ system. For example, the hardness is 2.40 GPa and 3.56 GPa for the Au₀.₇₅Ni₀.₂₅Sn₄ and Au₀.₅Ni₀.₅Sn₄ structures, respectively. When excess IMCs form between the solder and substrate, Au₀.₅Ni₀.₅Sn₄ would be more susceptible to fracture than Au₀.₇₅Ni₀.₂₅Sn₄ due to its higher stiffness. Meanwhile, for the Pd-doped system, the hardness of the Au₀.₇₅Pd₀.₂₅Sn₄ structure is greater than for the other materials, indicating that mechanical instability would most likely appear in the Au₀.₇₅Pd₀.₂₅Sn₄ layer. In fact, the (Au,Ni)Sn₄ compound layer formed between the solder and pad consists of nanocrystals with many fine pores arranged in a larger grain-like morphology. Perhaps due to the temperature gradient along the IMCs during the soldering process and its speed, it is possible that there are polycrystalline regions within the IMCs. This would also contribute to Au embrittlement.

## Thermodynamic Properties

The Debye temperature is an important thermodynamic parameter of a material, related to the vibrational modes and heat capacity of the crystal and the interatomic bonding. Higher Debye temperature often indicates stronger interatomic bonding, which would cause higher hardness of the material. The Debye temperature can be calculated based on the following expression³⁰:

$$
\theta_{\mathrm{D}}=\frac{h}{k_{\mathrm{B}}}\left(\frac{3nN_{\mathrm{A}}\rho}{4\pi M}\right)^{\frac{1}{3}}v_{\mathrm{m}}, \tag{13}
$$

where $h$, $k_{\mathrm{B}}$, and $N_{\mathrm{A}}$ are three constants, namely Planck's constant, Boltzmann's constant, and Avogadro's constant, respectively, and $\rho$ is the material density. $M$ is the molar mass, $n$ is the total number of atoms in the molecular formula, and $v_{\mathrm{m}}$ is the averaged elastic wave velocity, defined as

$$
v_{\mathrm{m}}=\left[\frac{1}{3}\left(\frac{2}{v_{\mathrm{t}}^{3}}+\frac{1}{v_{\mathrm{l}}^{3}}\right)\right]^{-\frac{1}{3}}, \tag{14}
$$

where $v_{\mathrm{t}}$ and $v_{\mathrm{l}}$ are the transverse and longitudinal elastic wave velocities, which can be derived from the bulk modulus and shear modulus according to the following expressions:

$$
v_{\mathrm{t}}=\left(\frac{G}{\rho}\right)^{\frac{1}{2}}, \tag{15}
$$

$$
v_{\mathrm{l}}=\left(\frac{3K+4G}{3\rho}\right)^{\frac{1}{2}}. \tag{16}
$$

The density, elastic wave velocities, and Debye temperature for the impurity-doped AuSn₄ IMCs together with the parent phase are presented in Table IV. In general, the density, elastic wave velocities, and Debye temperature increase after doping. The longitudinal elastic wave velocities are higher than the transverse ones, and the Debye temperatures are below room temperature. However, for the Ni-doped system, the Debye temperature and sound velocity increase with the Ni fraction. Meanwhile, for the Pd-doped system, the Debye temperature and sound velocity of Au₀.₇₅Pd₀.₂₅Sn₄ are higher than for Au₀.₅Pd₀.₅Sn₄ due to its higher shear modulus. For the Pd/Ni-codoped AuSn₄, the Debye temperature is close to that of Au₀.₅Pd₀.₅Sn₄. Based on the Debye temperature, one can deduce that the hardness of the impurity-doped AuSn₄ IMCs lies in the following order: Au₀.₅Ni₀.₅Sn₄ > Au₀.₇₅Pd₀.₂₅Sn₄ > Au₀.₅Pd₀.₅Sn₄ > Au₀.₅Pd₀.₂₅Ni₀.₂₅Sn₄ > Au₀.₇₅Ni₀.₂₅Sn₄, showing good consistency with our calculated hardness results. As is well know, the higher the Debye temperature, the better the thermal conductivity. Therefore, it can be said that doping with Ni or Pd can improve the thermal conductivity of AuSn₄. Among these materials, Au₀.₅Ni₀.₅Sn₄ should exhibit good thermal conductivity.

The thermal conductivity coefficient of a material quantifies its ability to transfer heat. To clarify

<table>
<caption>Table IV. Density (kg/m³), elastic wave velocity (m/s), Debye temperature (K), and minimum thermal conductivity (W/m-K) at 0 K and 0 GPa for nondoped and impurity-doped AuSn₄ IMCs</caption>
<thead>
<tr>
<th>IMC</th>
<th>$\boldsymbol{\rho}$</th>
<th>$\boldsymbol{v_{\mathrm{t}}}$</th>
<th>$\boldsymbol{v_{\mathrm{l}}}$</th>
<th>$\boldsymbol{v_{\mathrm{m}}}$</th>
<th>$\boldsymbol{\theta_{\mathrm{D}}}$</th>
<th>$\boldsymbol{k_{\mathrm{min}}}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>AuSn₄</td>
<td>6049</td>
<td>1355</td>
<td>3382</td>
<td>1535</td>
<td>137</td>
<td>0.306</td>
</tr>
<tr>
<td>Au₀.₇₅Ni₀.₂₅Sn₄</td>
<td>8343</td>
<td>1596</td>
<td>3178</td>
<td>1790</td>
<td>181</td>
<td>0.410</td>
</tr>
<tr>
<td>Au₀.₅Ni₀.₅Sn₄</td>
<td>8115</td>
<td>1801</td>
<td>3352</td>
<td>2011</td>
<td>206</td>
<td>0.456</td>
</tr>
<tr>
<td>Au₀.₇₅Pd₀.₂₅Sn₄</td>
<td>8395</td>
<td>1739</td>
<td>3286</td>
<td>1944</td>
<td>196</td>
<td>0.432</td>
</tr>
<tr>
<td>Au₀.₅Pd₀.₅Sn₄</td>
<td>8215</td>
<td>1670</td>
<td>3271</td>
<td>1871</td>
<td>190</td>
<td>0.427</td>
</tr>
<tr>
<td>Au₀.₅Pd₀.₂₅Ni₀.₂₅Sn₄</td>
<td>8163</td>
<td>1659</td>
<td>3280</td>
<td>1860</td>
<td>189</td>
<td>0.429</td>
</tr>
</tbody>
</table>

whether a material can be used as an intrinsic thermal barrier coating or not, the thermal conductivity should be revealed. At high temperatures, the thermal conductivity will decrease with increasing temperature. Thus, it is important to determine the minimum value at high temperatures in order to explore the application of the material under extreme conditions. The minimum thermal conductivity can be derived according to the criterion of Cahill and Pohl³¹⁻³³:

$$
k_{\min }=\frac{k_{\mathrm{B}}}{2.48} n^{\prime \frac{2}{3}}\left(2 v_{\mathrm{t}}+v_{\mathrm{l}}\right), \tag{17}
$$

where $k_{\mathrm{B}}$, $v_{\mathrm{t}}$, and $v_{\mathrm{l}}$ have the same meanings as in Eqs. 13, 15, and 16, and $n'$ is the number of atoms per unit volume. From the results in Table IV, one can see that the minimum thermal conductivity increases after Ni or Pd addition, and $\mathrm{Au}_{0.5}\mathrm{Ni}_{0.5}\mathrm{Sn}_{4}$ possesses the largest value of 0.46 W/m-K among them, but they are still relatively small, lower than 0.5 W/m-K; That is to say, thin and continuous $(\mathrm{Au},\mathrm{M})\mathrm{Sn}_{4}$ ($\mathrm{M} = \mathrm{Ni}$, $\mathrm{Pd}$) IMCs would assist the reliability of solder with pad. However, during aging treatment, ternary or quaternary compounds would grow at a faster rate than $\mathrm{AuSn}_{4}$, and heat could not be easily transfered from the solder to pad, causing heat concentration, with most fractures occurring at the interface.

## Electronic Structure

To further explore the bonding mechanisms on a physical basis to investigate the stabilization effect, the electronic properties of the impurity-doped $\mathrm{AuSn}_{4}$ IMCs were analyzed based on the total density of states (TDOS) and partial density of states (PDOS), presented in Fig. 3. All of the compounds showed metallic character due to the finite value of the Fermi level. It can be found that the energy range from $-11.0$ eV to 4.0 eV for $\mathrm{AuSn}_{4}$ was shifted to a lower energy range of $-11.0$ eV to 2.5 eV after doping, indicating stability.³⁴ For the Ni-doped system, two main bonding peaks appear at the energy range from about $-5.7$ eV to $-4.0$ eV and $-4.0$ eV to the Fermi energy, in which Ni $d$ and Sn $p$ electrons are the main contributors to the higher energy range, while Au $d$ electrons are the main contributor to that at lower energy. For the $\mathrm{Au}_{0.5}\mathrm{Ni}_{0.5}\mathrm{Sn}_{4}$ structure, the two peaks are close to each other, indicating stronger atomic interaction. For the Pd-doped system, the main bonding peak at the energy range from about $-5.8$ eV to $-4.0$ eV for $\mathrm{Au}_{0.75}\mathrm{Pd}_{0.25}\mathrm{Sn}_{4}$ is higher than for $\mathrm{Au}_{0.5}\mathrm{Pd}_{0.5}\mathrm{Sn}_{4}$, with Au $d$ electrons being the main contributor, slightly hybridized with some Sn $p$ electrons. Hybridization causes more stable bonds between Au and Sn atoms, which may be related to the greater mechanical stability of $\mathrm{Au}_{0.75}\mathrm{Pd}_{0.25}\mathrm{Sn}_{4}$, as indicated by the energy of formation results.

Meanwhile, Pd $d$ and Sn $p$ electrons are the main contributors to the TDOS from about $-4$ eV to the Fermi energy for these Pd-doped IMCs. For the Ni/ Pd-codoped system, the shape of the TDOS is similar to that of $\mathrm{Au}_{0.5}\mathrm{Pd}_{0.5}\mathrm{Sn}_{4}$, probably as Ni and Pd lie in the same group of the Periodic Table, which is in agreement with their similar mechanical character. Moreover, the calculated integrated density of state (DOS) at the Fermi level ($N_{\mathrm{Ef}}$) was 44.92 electrons/eV for $\mathrm{AuSn}_{4}$, 37.02 electrons/eV for $\mathrm{Au}_{0.75}\mathrm{Ni}_{0.25}\mathrm{Sn}_{4}$, 36.59 electrons/eV for $\mathrm{Au}_{0.5}\mathrm{Ni}_{0.5}\mathrm{Sn}_{4}$, 32.21 electrons/eV for $\mathrm{Au}_{0.75}\mathrm{Pd}_{0.25}\mathrm{Sn}_{4}$, 32.28 electrons/eV for $\mathrm{Au}_{0.5}\mathrm{Pd}_{0.5}\mathrm{Sn}_{4}$, and 32.67 electrons/eV for $\mathrm{Au}_{0.5}\mathrm{Pd}_{0.25}\mathrm{Ni}_{0.25}\mathrm{Sn}_{4}$. Lower $N_{\mathrm{Ef}}$ corresponds to a more stable phase.³⁴,³⁵ We found $N_{\mathrm{Ef}}$ to increase in the order: $\mathrm{Au}_{0.75}\mathrm{Pd}_{0.25}\mathrm{Sn}_{4} < \mathrm{Au}_{0.5}\mathrm{Pd}_{0.5}\mathrm{Sn}_{4} < \mathrm{Au}_{0.5}\mathrm{Pd}_{0.25}\mathrm{Ni}_{0.25}\mathrm{Sn}_{4} < \mathrm{Au}_{0.5}\mathrm{Ni}_{0.5}\mathrm{Sn}_{4} < \mathrm{Au}_{0.75}\mathrm{Ni}_{0.25}\mathrm{Sn}_{4} < \mathrm{AuSn}_{4}$, in agreement with the change in the energy of formation of the $\mathrm{AuSn}_{4}$-based IMCs. Therefore, $\mathrm{Au}_{0.75}\mathrm{Pd}_{0.25}\mathrm{Sn}_{4}$ is the most stable phase among these IMCs.

## CONCLUSIONS

The effects of substitution of Ni and Pd for Au in $\mathrm{AuSn}_{4}$ on the mechanical, thermodynamic, and electronic properties were investigated based on first-principles calculations. Doping with impurities led to more stable structures than the parent phase. For the Ni-doped system, $\mathrm{Au}_{0.5}\mathrm{Ni}_{0.5}\mathrm{Sn}_{4}$ was more stable than $\mathrm{Au}_{0.75}\mathrm{Ni}_{0.25}\mathrm{Sn}_{4}$. For the Pd-doped system, $\mathrm{Au}_{0.75}\mathrm{Pd}_{0.25}\mathrm{Sn}_{4}$ was more stable than $\mathrm{Au}_{0.5}\mathrm{Pd}_{0.5}\mathrm{Sn}_{4}$. Based on the elastic modulus results, doping with Ni or Pd increased the elastic modulus and hardness, but decreased the Poisson's ratio. The doped $\mathrm{AuSn}_{4}$ IMCs together with the parent $\mathrm{AuSn}_{4}$ were all ductile phases, but Ni addition led to increased brittleness. The structure of $\mathrm{Au}_{0.5}\mathrm{Ni}_{0.5}\mathrm{Sn}_{4}$ was more brittle than $\mathrm{Au}_{0.75}\mathrm{Ni}_{0.25}\mathrm{Sn}_{4}$. For the Pd-doped system, $\mathrm{Au}_{0.75}\mathrm{Pd}_{0.25}\mathrm{Sn}_{4}$ was more brittle than $\mathrm{Au}_{0.5}\mathrm{Pd}_{0.5}\mathrm{Sn}_{4}$. With increasing doped impurity fraction, the structures became closer to being elastically isotropic according to the Zener anisotropy factor. The Debye temperature and minimum thermal conductivity coefficient of all the doped $\mathrm{AuSn}_{4}$ IMCs were higher than for the parent phase and exhibited the same variation trend, indicating the good thermal conductivity of the doped systems. Among them, $\mathrm{Au}_{0.5}\mathrm{Ni}_{0.5}\mathrm{Sn}_{4}$ possessed the highest minimum thermal conductivity value of 0.46 W/m-K, indicating the best thermal conductivity. Furthermore, the electronic density of states was employed to analyze the stability of the $\mathrm{AuSn}_{4}$-based IMCs. The highest stability was found for $\mathrm{Au}_{0.75}\mathrm{Pd}_{0.25}\mathrm{Sn}_{4}$, which can be attributed to its highest electron density at the Fermi level. Thus, the effects of doping with Ni or Pd on the brittleness of $\mathrm{AuSn}_{4}$ are clarified by this research work. These findings provide a good reference for future applications of these materials.

## ACKNOWLEDGEMENTS

This work was supported by the National Natural Science Foundation of China (51572190), and the supercomputing resources were supported by the High Performance Computing Center of Tianjin University, China.

## REFERENCES

1.  C.E. Ho, W.T. Chen, and C.R. Kao, *J. Electron. Mater.* 30, 379 (2001).
2.  C. Yu, J.Y. Liu, H. Lu, P.L. Li, and J.M. Chen, *Intermetallics* 15, 1471 (2007).
3.  C.E. Ho, R. Zheng, G.L. Luo, A.H. Lin, and C.R. Kao, *J. Electron. Mater.* 29, 1175 (2000).
4.  T.J. Chung, W.H. Moon, Y.G. Park, M.C. Kim, and C.K. Choi, *Intermetallics* 18, 1228 (2010).
5.  C.E. Ho, Y.C. Lin, and S.J. Wang, *Thin Solid Films* 544, 551 (2013).
6.  C.E. Ho, W.H. Wu, L.H. Hsu, and C.S. Lin, *J. Electron. Mater.* 41, 11 (2012).
7.  Y.J. Chen, T.L. Yang, and J.J. Yu, *Mater. Lett.* 110, 13 (2013).
8.  C.E. Ho, C.W. Fan, and W.Z. Hsieh, *Surf. Coat. Technol.* 259, 244 (2014).
9.  Alexandra Neumann, A. Kjekshus, and E. Røst, *J. Solid State Chem.* 123, 203 (1996).
10. L. Zavalij, A. Zribi, R.R. Chromik, S. Pitely, P.Y. Zavalij, and E.J. Cotts, *J. Alloys Compd.* 334, 79 (2002).
11. J.W. Yoon, H.S. Chun, B.I. Noh, and S.B. Jung, *Microelectron. Reliab.* 48, 1857 (2008).
12. H.Q. Dong, V. Vuorinen, T. Laurila, and M. Paulasto-Kröckel, *CALPHAD* 43, 61 (2013).
13. J.A. Davis, M.J. Bozack, and J.L. Evans, *IEEE Trans. Compon. Packag. Technol.* 30, 32 (2007).
14. R. Kubiak and M. Wolcyrz, *J. Less-Common. Met.* 97, 265 (1984).

15. J.H. Lee, J.H. Park, Y.H. Lee, and Y.S. Kim, *J. Mater. Res.* 16, 1249 (2001).
16. A.M. Minor and J.W. Morris, *Metall. Mater. Trans. A* 31, 798 (2000).
17. S.A. Belyakov and C.M. Gourlay, *Intermetallics* 25, 48 (2012).
18. Y. Yang, Y.Z. Li, H. Lu, C. Yu, and J.M. Chen, *Comput. Mater. Sci.* 65, 490 (2012).
19. G. Ghosh, *J. Mater. Res.* 23, 1398 (2008).
20. Y.F. Wu, B. Wu, and Z.Y. Wei, *Intermetallics* 53, 26 (2014).
21. W. Zhou, L.J. Liu, B.L. Li, and P. Wu, *Comput. Mater. Sci.* 46, 921 (2009).
22. H.-C. Cheng, C.-F. Yu, and W.-H. Chen, *J. Alloys Compd.* 546, 286 (2013).
23. R.R. Chromik, D.N. Wang, A. Shugar, L. Limata, M. Notis, and R. Vinci, *J. Mater. Res.* 20, 2161 (2005).
24. Y.K. Wang, W.S. Liu, Y.F. Huang, Y. Tang, F. Cheng, Q. Yu, and Y.Z. Man, *Mater. Sci. Eng. A* 610, 161 (2014).
25. G. Ghosh, *J. Mater. Res.* 19, 1439 (2004).
26. H.-C. Cheng, C.-F. Yu, and W.-H. Chen, *Comput. Mater. Sci.* 81, 146 (2014).
27. X.D. Zhang, C.H. Ying, and Z.J. Li, *Superlattices Microstruct.* 52, 459 (2012).
28. C.M. Li, S.M. Zeng, and Z.Q. Chen, *Comput. Mater. Sci.* 93, 210 (2014).
29. F. Pugh XCII, *Philos. Mag.* 45, 823 (1954).
30. A. Bouhemadou, *Solid State Sci.* 11, 1875 (2009).
31. D.G. Cahill and R.O. Pohl, *Annu. Rev. Phys. Chem.* 39, 93 (1988).
32. H.C. Chen, L.J. Yang, and J.P. Long, *Superlattices Microstruct.* 79, 156 (2015).
33. J. Ao, Q. Hui, C.M. Li, F. Li, and Z.Q. Chen, *Comput. Mater. Sci.* 88, 103 (2014).
34. D.-H. Wu, H.-C. W., L.-T. Wei, R.-K. Pan, and B.-Y. Tang, *J. Magnesium Alloys* 2, 165 (2014).
35. C.L. Fu, X. Wang, Y.Y. Ye, and K.M. Ho, *Intermetallics* 7, 179 (1999).

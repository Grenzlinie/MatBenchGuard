# Superhard and Superconducting Bilayer Borophene

Chengyong Zhong $^{1}$D, Minglei Sun $^{2,*,}$ Tariq Altalhi $^{3}$D and Boris I. Yakobson $^{3,4,*}$

1 College of Physics and Electronic Engineering, Chongqing Normal University, Chongqing 401331, China; zhongcy90@126.com
2 Department of Materials Science and Nanoengineering, Rice University, Houston, TX 77005, USA
3 Chemistry Department, Taif University, Taif 21974, Saudi Arabia; ta.altalhi@tu.edu.sa
4 Department of Chemistry, Rice University, Houston, TX 77005, USA
* Correspondence: minglei.sun@rice.edu (M.S.); biy@rice.edu (B.I.Y.)

**Abstract:** Two-dimensional superconductors, especially the covalent metals such as borophene, have received significant attention due to their new fundamental physics, as well as potential applications. Furthermore, the bilayer borophene has recently ignited interest due to its high stability and versatile properties. Here, the mechanical and superconducting properties of bilayer-$\delta_6$ borophene are explored by means of first-principles computations and anisotropic Migdal–Eliashberg analytics. We find that the coexistence of strong covalent bonds and delocalized metallic bonds endows this structure with remarkable mechanical properties (maximum 2D-Young’s modulus of ~570 N/m) and superconductivity with a critical temperature of ~20 K. Moreover, the superconducting critical temperature of this structure can be further boosted to ~46 K by applied strain, which is the highest value known among all borophenes or two-dimensional elemental materials.

**Keywords:** bilayer borophene; superhard; anisotropic superconductivity; electron–phonon coupling; strain effect; first-principles calculations

## 1. Introduction

Superconductivity in two-dimensional (2D) materials has attracted perennial and ever-increasing attention over past decades, owing both to fundamental scientific interest and tantalizing applications [1–5]. One of the most important goals in superconductivity research is raising the superconducting transition temperature, $T_c$. In general, superconducting materials can be classified into two categories: low-temperature superconductors, characterized by critical temperatures ($T_c$) below 30 K, such as Nb-Ge films [6], and high-temperature superconductors with $T_c$ exceeding 30 K, exemplified by Cu-based oxides [7–9]. Within the framework of the conventional Bardeen–Cooper–Schrieffer (BCS) theory [10], it is reasonably anticipated that metals composed of light elements have a better chance to induce a high $T_c$, because the Debye temperatures within such metals are usually high enough to trigger a strong phonon-mediated superconducting pairing. More specifically, according to the celebrated McMillan–Allen–Dynes (MAD) formula [11,12]:

$$
T_{\mathrm{c}}=\frac{\omega_{log}}{1.20}exp\left[\frac{-1.04(1+\lambda)}{\lambda-\mu^{*}(1+0.62\lambda)}\right] \tag{1}
$$

$T_c$ should be elevated by increasing the log-averaged characteristic phonon frequency ($\omega_{log}$) and the electron–phonon coupling (EPC) parameter, $\lambda$. The light elemental materials typically have high frequency phonon modes, enlarging $\omega_{log}$ and thus increasing $T_c$. Furthermore, large phonon frequency and EPC potential $V = \frac{\lambda}{N(E_f)}$ induced by strong covalent bonding in light elemental material, together with $N\left(E_{f}\right)$, and the electronic density of states (DOS) at the Fermi level [13], should result in a higher $T_c$. In fact, the metals with strong covalent bonding can be grouped as “covalent metals” [13] and their potential

![](./images/990432410296385558_1.jpg)

Citation: Zhong, C.; Sun, M.; Altalhi, T.; Yakobson, B.I. Superhard and Superconducting Bilayer Borophene. *Materials* 2024, 17, 1967. https://doi.org/10.3390/ma17091967

Academic Editor: Yong Seung Kwon

Received: 17 March 2024
Revised: 14 April 2024
Accepted: 19 April 2024
Published: 24 April 2024

![](./images/990432410296385558_2.jpg)

Copyright: © 2024 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https://creativecommons.org/licenses/by/4.0/).

to harbor a high $T_c$ in 2D form have been confirmed, e.g., hydrogenated monolayer $MgB_2$ (67 K) [14], doped graphene (8.1 K~30 K) [15-17], hydrogenated monolayer borophene (32.4 K) [5] and especially 2D metal borides (1.4 K~72 K) [18-22].

Among covalent metals, 2D boron sheets (borophenes) recently came to the fore of superconducting research, motivated by their inherent metallicity, light weight and significant experimental progress on their synthesis [23-25]. Based on the first-principles calculations and MAD formula, Penev et al. [26] reported early on the $T_c$ of the (experimentally synthesized $\delta_6$, $\beta_{12}$ and $\chi_3$ borophenes) to be in the range of 11.5 K~20.5 K and Gao et al. [27] found them to span 18.7 K-24.7 K. Using a more accurate and sophisticated anisotropic Migdal-Eliashberg (ME) equation, Zhao et al. [28] found the $T_c$ in those borophenes in 26.2 K-33 K. Apart from intrinsic metallicity and light weight, another impetus for searching high-temperature superconductivity in borophenes is their vast polymorphs and superior mechanical properties, which provide a great benefit to potential superconductors, suggesting effective ways to modulate the superconductivity [29].

The monolayer borophenes have been intensively studied; however, the investigations are scarce [30-32] for bilayer or multilayer borophenes, where more intriguing properties and tunability could be manifested, compared to their monolayer counterparts. Very recently, the realization of bilayer borophenes were reported [33,34]. Unfortunately, the first reported bilayer $\alpha$-borophene is expected to be unstable if peeled off from the metal substrate [35], and the $\beta_{12}$-like bilayer synthesized on Cu(111) surface appears complicated due to ambiguity (with more than three hundred atoms in its unit cell and the atomic structure still in debate), preventing an exploration of its properties or further application. It can be anticipated that more stable and versatile bilayer borophenes are still to be unveiled for research.

In this work, we investigate the mechanical and superconducting properties of a bilayer composed of two covalently bonded $\delta_6$ borophene monolayers, "(BL)-$\delta_6$" in Figure 1a-c. The compact atomic structure endows BL-$\delta_6$ with remarkable stability and tantalizing properties compared to its monolayer counterparts. Its computed high Young's modulus of 570 N/m is even higher than 346 N/m for graphene (or near 280 N/m "per layer", for a fair comparison). Based on the anisotropic ME equation, we find its $T_c$ = 20 K and can be boosted to 46 K by strain effect, reaching the highest $T_c$ found among all borophenes or elemental 2D materials known to date. The coexistence of superhard (in basal plane direction) and superconducting properties in one material is rare, making BL-$\delta_6$ a fascinating superconductor for emergent nanoscale devices such as quantum interferometers, superconducting transistors, superconducting qubits, and wear-resistant parts of superconducting devices [3,36,37].

![](./images/990432410296385558_3.jpg)

Figure 1. (a) Planar and (b,c) side views of the atomic structure of BL-$\delta_6$. The yellow shaded region is its unit cell, and the green shaded region is the unit cell of $\delta_6$. There are three irreducible boron atoms colored as B1 (green), B2 (blue), and B3 (pink). The direction dependence of (d) Young's modulus and (e) Poisson's ratio of BL-$\delta_6$. (f) Stress-strain curves of BL-$\delta_6$, the vertical blue and red dashed lines denote the fractured stress along the $a$ and $b$ directions, respectively.

## 2. Results and Discussion
### 2.1. Atomic Structure and Mechanical Properties

BL-$\delta_6$ and $\delta_6$ share the same top view (Figure 1a), and BL-$\delta_6$ can be viewed as AB stacking of two $\delta_6$ monolayers bonded via interlayer covalent bonds (side view in Figure 1b,c). The unit cell of BL-$\delta_6$ is a rectangle with lattice constants $a = 3.243$ Å, $b = 2.883$ Å (Table 1), which is obtained with a Vienna ab initio Simulation Package [38,39] (computational details can be found in Supplementary Note S1). The total energy of BL-$\delta_6$ is computed to be lower than all experimental synthesized monolayers, due to the interlayer bonding: $-6.38$ eV/atom, which is 0.171 eV/atom, 0.125 eV/atom and 0.113 eV/atom lower than that of the synthesized $\delta_6$, $\beta_{12}$ and $\chi_3$, respectively (see Table 1, for atomic structures see Figure S2). Moreover, the slight dynamical instability of $\delta_6$ is also eliminated by the interlayer bonding of BL-$\delta_6$. The energetic stability of BL-$\delta_6$ was also confirmed by an ab initio evolutionary global structure search in our prior work [40] and reported by Zhou et al. [41]. Given that the monolayer $\delta_6$ has been fabricated on a Ag(111) substrate, the thermal stability of BL-$\delta_6$ is also tested on Ag(111) substrate by an AIMD simulation at 500 K, and one can observe that its whole structure is well maintained after 5 ps with a timestep of 1 fs under such a high temperature (Figure S3). Therefore, it is well-expected that BL-$\delta_6$ will be accessed experimentally, supported by its outstanding energetic and thermal stability, and the progress in bilayer borophene synthesis [42,43].

<table>
<thead>
  <tr>
    <th>System</th>
    <th>Space Group</th>
    <th>$a$</th>
    <th>$b$</th>
    <th>$C_{11}$</th>
    <th>$C_{22}$</th>
    <th>$C_{12}$</th>
    <th>$C_{44}$</th>
    <th>$Y_a$</th>
    <th>$Y_b$</th>
    <th>$v_a$</th>
    <th>$v_b$</th>
    <th>$E_c$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>BL$-\delta_6$</td>
    <td>Pmmm</td>
    <td>3.243</td>
    <td>2.883</td>
    <td>570.0</td>
    <td>322.0</td>
    <td>22.0</td>
    <td>146.0</td>
    <td>569.4</td>
    <td>321.4</td>
    <td>0.038</td>
    <td>0.068</td>
    <td>$-6.380$</td>
  </tr>
  <tr>
    <td>$\delta_6$</td>
    <td rowspan="2">Pmmn</td>
    <td>1.614</td>
    <td>2.874</td>
    <td>398.6</td>
    <td>171.8</td>
    <td>$-4.0$</td>
    <td>93.9</td>
    <td>398.6</td>
    <td>171.8</td>
    <td>$-0.01$</td>
    <td>$-0.02$</td>
    <td>$-6.209$</td>
  </tr>
  <tr>
    <td>$\delta_6$ [24]</td>
    <td>1.617</td>
    <td>2.865</td>
    <td>398.0</td>
    <td>170.0</td>
    <td>$-7.0$</td>
    <td>94.0</td>
    <td>398.0</td>
    <td>170.0</td>
    <td>$-0.04$</td>
    <td>$-0.02$</td>
    <td></td>
  </tr>
  <tr>
    <td>$\beta_{12}$</td>
    <td rowspan="2">Pmmm</td>
    <td>2.931</td>
    <td>5.065</td>
    <td>187.0</td>
    <td>218.6</td>
    <td>36.8</td>
    <td>62.7</td>
    <td>180.8</td>
    <td>211.4</td>
    <td>0.168</td>
    <td>0.197</td>
    <td>$-6.255$</td>
  </tr>
  <tr>
    <td>$\beta_{12}$ [44]</td>
    <td></td>
    <td></td>
    <td>185.5</td>
    <td>210.5</td>
    <td>37.0</td>
    <td>68.5</td>
    <td>179.0</td>
    <td>203.1</td>
    <td>0.176</td>
    <td>0.199</td>
    <td></td>
  </tr>
  <tr>
    <td>$\chi_3$</td>
    <td rowspan="2">Cmmm</td>
    <td>8.407</td>
    <td>2.912</td>
    <td>207.3</td>
    <td>198.5</td>
    <td>28.2</td>
    <td>60.0</td>
    <td>203.3</td>
    <td>194.7</td>
    <td>0.135</td>
    <td>0.142</td>
    <td>$-6.267$</td>
  </tr>
  <tr>
    <td>$\chi_3$ [44]</td>
    <td></td>
    <td></td>
    <td>201.0</td>
    <td>185.0</td>
    <td>21.5</td>
    <td>60.5</td>
    <td>198.5</td>
    <td>182.7</td>
    <td>0.116</td>
    <td>0.107</td>
    <td></td>
  </tr>
  <tr>
    <td>Graphene</td>
    <td rowspan="2">P6/mmm</td>
    <td>2.468</td>
    <td></td>
    <td>356.9</td>
    <td></td>
    <td>62.2</td>
    <td>147.3</td>
    <td>346.1</td>
    <td></td>
    <td>0.174</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Graphene [45]</td>
    <td>2.470</td>
    <td></td>
    <td>352.7</td>
    <td></td>
    <td>60.9</td>
    <td>145.9</td>
    <td>342.2</td>
    <td></td>
    <td>0.173</td>
    <td></td>
    <td></td>
  </tr>
</tbody>
</table>
Table 1. The space group, lattice constants (Å), elastic constants (N/m), Young’s moduli (N/m), Poisson’s ratios, and cohesive energies (eV/atom) of BL-$\delta_6$, $\delta_6$, $\beta_{12}$, $\chi_3$.

We obtain the four independent elastic constants for BL-$\delta_6$: $C_{11}=570$ N/m, $C_{22}=322$ N/m, $C_{12}=22$ N/m, and $C_{44}=146$ N/m, which apparently satisfy the Born-Huang criteria [46]: $C_{11}C_{22}-C_{12}^2>0$ and $C_{44}>0$, demonstrating the mechanical stability of BL-$\delta_6$. The $\theta$ dependence of in-plane Young’s modulus $Y$ and Poisson’s ratio $v$ of BL-$\delta_6$ are plotted with polar coordinates in Figure 1d,e (computational details can be found in Supplementary Note S2 and Figures S5 and S6). We find that the in-plane Young’s moduli and the Poisson’s ratios of BL-$\delta_6$ are highly anisotropic. For comparison, the values of elastic constants, Young’s moduli, Poisson’s ratios of $\delta_6$, $\beta_{12}$, $\chi_3$ and graphene are summarized in Table 1. The introduced B-B3 bonds in BL-$\delta_6$ boost the $Y_a$ and $Y_b$ to 570 N/m and 321 N/m, respectively. Although graphene is well-known as the strongest 2D material, along the armchair direction $Y_a=570$ N/m exceeds the $Y_a=364$ N/m of graphene, partially due to the strong directional B-B $\sigma$-bonds, making it stand out among 2D materials. In contrast, the $Y_b=321$ N/m (still comparable to graphene) is lower, due to the much weaker multicenter bonds involved in the zigzag direction.

We find the fracture strain is 13% along the $a$ and 8% along the $b$ direction, according to the strained phonon spectra (Figure S4), before reaching the elastic maximum of 16% and 14% (Figure 1f). Thus, the failure mechanism of BL-$\delta_6$ is phonon instability, for both directions, which is different from that of $\delta_6$ (elastic instability in the zigzag direction and phonon instability in the armchair direction) [47]. The fracture strengths of BL-$\delta_6$ are 43 and 23 N/m along the $a$ and $b$ directions, much above that of $\delta_6$ (20.26 and 12.98 N/m) [47],

black phosphorene (9.99 and 4.44 N/m) [48], and even graphene (40.41 and 36.74 N/m) [49] along the zigzag direction. Considering the ultrahigh Young's moduli and large fracture strength, one can judge the BL-$\delta_6$ being in-plane superhard.

### 2.2. Electronic Properties

The electronic structure of BL-$\delta_6$ is summarized in Figure 2. Three bands cross the Fermi level and form the Fermi surface, of which one forms a small electron pocket cen- tered around the corner of the first BZ and the other two contribute to the rest of Fermi surface (Figure 2b). The atomic- and orbital-resolved band structures suggest that the main contribution near the Fermi level is from the $p_y$ orbital of B1/B3 atoms and the $p_z$ orbital of all B atoms (Figure 2f,g, more details in Figure S7), which is also confirmed by the charge distribution in the states within $\pm 0.3$ eV from the Fermi level (Figure 2c-e). Using Wan- nier90 (v 3.1.0) code [50], the Wannier-interpolated band structures are also provided and show excellent agreement with those by first-principles calculations (Figure 2a), which lays a clear ground for subsequent anisotropic superconductivity calculations, as implemented in electron-phonon Wannier (EPW v 5.4) code [51].

![](./images/990432410296385558_4.jpg)

Figure 2. (a) Electronic band structures of BL-$\delta_6$ by DFT (red solid lines) and Wannier90 (blue dashed lines). (b) Fermi surface, (c-e) top and side views of the charge density corresponding to the energy range shaded green in (a), and electronic band structures weighted by the $p_y$ orbital of B1 and B3 atoms (f) and the $p_z$ orbital contributions of all boron atoms (g) of BL-$\delta_6$.

### 2.3. Isotropic and Anisotropic Superconducting Properties

In the phonon spectrum of BL-$\delta_6$ (Figure 3a), we find no negative frequencies, demon- strating its dynamic stability. This is in stark contrast to $\delta_6$, a layer whose phonon dispersion displays small imaginary frequency near the $\Gamma$ point [24]. Mechanically intuitive, the BL-$\delta_6$ is stabilized by the covalent B3-B3 bonds. The ($v$) mode- and ($q$) momentum-resolved EPC $\lambda_{qv}$ is also given, calculated by the following equation:

$$
\lambda_{\mathrm{qv}}=\frac{2}{\hbar N(f) N_{k}} \sum_{n m k} \frac{1}{\omega_{q v}}\left|g_{k, q v}^{n m}\right|^{2} \delta\left(\epsilon_{k}^{n}\right) \delta\left(\epsilon_{k+q}^{m}\right), \tag{2}
$$

where $N_k$ represents the total number of $k$ points in the $k$ space, $g_{k,qv}^{nm}$ is an EPC matrix element, $n/m$ and $v$ represent the indices of electronic bands and phonon mode, $\epsilon_{k}^{n}$ and $\epsilon_{k+q}^{m}$

are the eigenvalues with respect to the Fermi level, and $\omega_{qv}$ is the phonon frequency. We found three modes ($B_{2u}$ and two $A_{g}$) have comparatively large EPC near the $\Gamma$ point (left panel of Figure 3a). In the $B_{2u}$ shear mode at 39.3 meV, the B1 and B2 atoms move in one direction and the B3 atoms move in the opposite (Figure 3b). The first $A_{g}$ mode at 102.6 meV corresponds to a bond stretching contributed by B3 atoms (Figure 3c). The second $A_{g}$ mode at 168.7 meV is also a stretch mode, but predominantly contributed by B1 atoms (Figure 3d). The vibrational contribution of these three modes can also be inferred from the phonon density of states (right panel of Figure 3a). The Eliashberg spectral function $\alpha^{2}F(\omega)$ is a key quantity, which determines the total EPC $\lambda$ by the following equation:

$$
\lambda = \sum_{qv} \lambda_{qv} = 2 \int \frac{\alpha^{2}F(\omega)}{\omega} d\omega \tag{3}
$$

![](./images/990432410296385558_5.jpg)

Figure 3. (a) From left to right: phonon band structure of BL-$\delta_{6}$ weighted by EPC $\lambda_{qv}$ with purple circles, isotropic Eliashberg function $\alpha^{2}F$ and EPC $\lambda(\omega)$, and phonon density of states contributed by different kinds of boron atoms. (b-d) Vibrational modes of the $B_{2u}$ mode and the two $A_{g}$ modes at $\Gamma$, as labeled in (a).

Accordingly, the $\alpha^{2}F(\omega)$ and cumulative EPC $\lambda(\omega)$ are calculated (middle panel of Figure 3a). We observe three sharp peaks mainly contributed by the three phonon modes analyzed above. Correspondingly, the EPC strength $\lambda$ calculated by Equation (3) is 0.59 and the $T_{c}$ of BL-$\delta_{6}$ within the MAD approximation calculated by Equation (1) is 10.1 K.

Akin to structure and mechanics anisotropy, the Fermi surface of BL-$\delta_{6}$, formed by multiple bands with different orbital contributions ($p_{y}$ and $p_{z}$ orbitals, Figure 2f,g) is also significantly anisotropic. For such a system with a complicated Fermi surface, using the anisotropic ME equation is essential, in order to obtain an anisotropic EPC, and an accurate Tc, compared with the isotropic superconductivity calculated from the MAD formula using an isotropic EPC [28]. As shown in Figure 4a,b, the variation in momentum-dependent EPC parameter $\lambda_{k}$ and the superconducting gap $\Delta_{k}$ at 10 K displays similar anisotropy, i.e., the maximum along the $\Gamma - X$ direction and the minimum along the $\Gamma - Y$ direction. We find the superconducting gap ratio $\Delta^{aniso} = (\Delta^{max} - \Delta^{min}) / \Delta^{ave} = (2.499 - 0.444)/1.470 \approx 140\%$, a measure of its strong anisotropy at the Fermi surface, also signifying that the anisotropic

ME formula is indispensable for predicting $T_c$. Figure 4c shows the evolution of the superconducting gap as a function of temperature, based on the ME equations solved in either isotropic or fully anisotropic approximations. The $T_c$ is identified as the lowest temperature at which the vanishing gap is observed. Under the isotropic approximation $T_c$ = 12 K, comparable to the value (10 K) obtained by the MAD formula but is much lower than the value calculated with the fully anisotropic approximation (20 K), further attesting to the anisotropic superconducting nature of BL-$\delta_6$, omitted previously [32].

![](./images/990432410296385558_6.jpg)

Figure 4. (a) Momentum-dependent EPC $\lambda_k$ across the full BZ and (b) momentum-dependent superconducting band gap $\Delta_k$ at 10 K and projected onto the Fermi surface. (c) Variation in the superconducting gap $\Delta_k$ with temperature, calculated by solving the ME equations in the isotropic approximation (yellow dots and dashed line interpolated) and with the fully anisotropic solution, where the purple shadowed regions indicate the magnitude distribution of the $\Delta_k$ and the light green dots connected with the dashed line represents the average value of the entire anisotropic $\Delta_k$.

The mechanical robustness of BL-$\delta_6$ permits a consideration of whether the tensile strain could enhance the $T_c$, motivated mainly by two reasons. First, according to Equation (2), it can be seen that EPC $\lambda_{qv}$ is inversely proportional to the phonon frequency $\omega_{qv}$, which would be helpful to lower, perhaps by tension, weakening the atomic force constants and thus softening the phonon modes. Second, the atomic orbitals overlap is reduced so that the electronic bands become less dispersive, enlarging the $N(E_f)$, which provides more electrons susceptible to pairing interactions, mediated by dynamic phonons, to certainly contribute to the $T_c$ rise.

To examine the effect of strain on the BL-$\delta_6$ superconductivity, the evolution of EPC $\lambda$, the log and maximum frequencies $\omega_{log}$ and $\omega_{max}$, as well as $T_c$, are all calculated within three approximations (i.e., MAD, isotropic ME, anisotropic ME), as a function of tensile strain along the $a$ direction, and presented in Figure 5a,b (for details see Figures S8-S11). As expected, the increment in $T_c$ is accompanied by a decrease in frequency-dependent $\omega_{log}/\omega_{max}$ and an increase in EPC $\lambda$ (Figure 5b). The phonon spectrum under a 13% tension along $a$ (near fracture strain) weighted by $\lambda_{qv}$, the Eliashberg spectral function $\alpha^2F(\omega)$ and EPC $\lambda(\omega)$ are shown in Figure 5c,d. The red shift of phonon frequency can be clearly observed and the enhanced EPC $\lambda_{qv}$ due to the phonon softening can be seen in all frequency ranges (Figure 5d). In addition, the contribution of low-frequency part becomes more dominant. In particular, four largely softened phonon Kohn anomalies with considerable EPCs around 15 meV appear on the path of X-M-Y. Eventually, these combined effects lead to a significant increase, by strain, in $\lambda$ from 0.59 to 1.33 and $T_c$ from 20 K to 46 K.

It should be emphasized that 46 K is the highest Tc among all borophenes and elemental 2D materials (Table 2). It should be noted that for bilayer or multilayer materials with positive Poisson ratios, such as BL-δ₆, the tensile strain would lead to vertical shrinking (Figure 5a), suggesting that the vertical pressure may also be an effective way to enhance the Tc of BL-δ₆, as the tensile strain does.

![](./images/990432410296385558_7.jpg)

Figure 5. (a) Evolution with tensile strain along the $a$ direction, of the $T_c$ at three approximations (MAD, circles; isotropic ME, triangles; anisotropic ME, squares) and the distance between $\delta_6$ planes measured as B3-B3 bond length $d$. (b) Evolution of EPC $\lambda$ (solid crosses), the log-weighted frequency $\omega_{log}$, (circles) and maximum phonon frequency $\omega_{max}$ (triangles) versus the strain. (c) Phonon band structure weighted by EPC $\omega_{qv}$ under 13% strain. (d) Isotropic Eliashberg $\alpha_2 F$ and EPC $\lambda$ with 13% tensile strain along the $a$ direction. Data with no strain are shown in gray, for comparison.

<table>
<thead>
<tr>
<th>System</th>
<th>$\lambda$</th>
<th>$T_{c}^{MAD}$<br>($K, \mu^{*} = 0.1$)</th>
<th>$T_{c}^{aniso}$<br>($K, \mu^{*} = 0.1$)</th>
</tr>
</thead>
<tbody>
<tr>
<td>$\delta_6$ [26]</td>
<td>1.10</td>
<td>20.5</td>
<td></td>
</tr>
<tr>
<td>$\delta_6$ [28]</td>
<td>0.82</td>
<td></td>
<td>27.0</td>
</tr>
<tr>
<td>$\beta_{12}$ [26]</td>
<td>0.80</td>
<td>16.1</td>
<td></td>
</tr>
<tr>
<td>$\beta_{12}$ [27]</td>
<td>0.89</td>
<td>18.7</td>
<td></td>
</tr>
<tr>
<td>$\beta_{12}$ [28]</td>
<td>1.01</td>
<td></td>
<td>33.0</td>
</tr>
<tr>
<td>$\chi_3$ [26]</td>
<td>0.60</td>
<td>11.5</td>
<td></td>
</tr>
<tr>
<td>$\chi_3$ [27]</td>
<td>0.95</td>
<td>24.7</td>
<td></td>
</tr>
<tr>
<td>$\chi_3$ [28]</td>
<td>0.79</td>
<td></td>
<td>26.2</td>
</tr>
<tr>
<td>Graphene (Li deposition) [15]</td>
<td>0.61</td>
<td>8.1</td>
<td></td>
</tr>
<tr>
<td>BL $-$ $\delta_6$</td>
<td>0.59</td>
<td>10.1</td>
<td>20</td>
</tr>
<tr>
<td>BL $-$ $\delta_6$ [32]</td>
<td>0.61</td>
<td>11.9</td>
<td></td>
</tr>
<tr>
<td>BL $-$ $\delta_6$ (13%)</td>
<td>1.33</td>
<td>30.78</td>
<td>46</td>
</tr>
</tbody>
</table>

Before concluding, a few remarks need to be addressed. Superhard materials are usually semiconductors with large bandgaps or insulators, because the majority of electrons are bound into covalent bonds, depleting any excess electrons from electron transport. For instance, diamond is an insulator and the hardest material known. It may seem that metallicity and superhardness cannot coexist in one covalent material. However, this dilemma can be resolved in 2D borophenes, because the electron deficiency nature of boron

atom enables strong localized covalent bonds and delocalized multicenter metal bonds in one system, which endows the system with superb mechanical performance and excellent metallicity, as evidenced by the high Young's moduli and metallicity in BL-$\delta_6$.

It is worth mentioning that research on BL borophenes is still in its infancy and has just been ignited by two recent independent experimental investigations. We would also like to point out that in addition to the striking mechanical properties and superconductivity studied in this work, BL-$\delta_6$ is expected to possess other interesting properties, such as anisotropic plasmonics [52] and ultrahigh thermal conductivity [53], awaiting more research. On the other hand, the excellent mechanical stability is also beneficial for BL-$\delta_6$ transfer to or even growth on some inert substrates [54], for convenience of characterization. Our results also show that the interlayer bonds, while strengthening the bilayer, do not destroy the $\sigma$-bond resonance nor the conducting $\pi$-bonds [55], adding a fine tuning-knob to the properties. This also highlights the potential of covalent metals in the quest for high $T_c$ superconductors.

In our investigation, the tensile strain is applied to enhance the superconducting temperature of bilayer borophene. In addition to strain, the phenomenon of disorder, particularly correlated disorder, can also significantly enhance the superconductivity in a material [56,57]. In bilayer borophene, manipulating disorder could pave new paths to enhance superconducting performance. On the other hand, a caveat common for all $\leq$2D materials, due to the Mermin-Wagner theorem, must be mentioned, since it restricts the stability, both merely structural and of the superconducting phase. Nevertheless, in any BL borophene realization, the sample finite size (and support by a 3D-substrate) should mitigate these concerns, although quantifying the size limitation is far beyond the scope of the present study.

## 3. Conclusions

In conclusion, we comprehensively investigated mechanical and superconducting properties of a bilayer borophene (BL-$\delta_6$), which can be viewed as AB stacking, with interlayer covalent bonding, of earlier realized $\delta_6$ borophene. The original good stability of $\delta_6$ and the introduced covalent bond endows BL-$\delta_6$ with very prominent energy—thermodynamic, thermal, and mechanical stability, suggesting that it has a high chance of occurrence in experiments. The strong directional $\sigma$ B-B bonds and very compact atomic configuration give BL-$\delta_6$ a 2D Young's modulus along the $a$ direction (569.4 N/m) higher than graphene (346.1 N/m), while ensuring that BL-$\delta_6$ can sustain an ultimate 13% and 8% tensile strain along the $a$ and $b$ directions, respectively. Furthermore, according to a fully anisotropic solution of the ME equation, we predict BL-$\delta_6$ is a conventional phonon-mediated 2D superconductor with $T_c$ as high as 20 K. We also highlighted the effects of tensile strain on EPCs and found that the $T_c$ can be boosted to 46 K at a 13% tensile strain along the $a$ direction. To the best of our knowledge, it is the highest value currently known for borophene or elemental 2D materials. Our findings also consolidated the justification that covalent metals, such as borophene, should benefit the search for high $T_c$ superconductors. The concurrent superior mechanical performance and excellent superconductivity is scarce; thus, promising BL-$\delta_6$ many potential applications, such as quantum interferometers, superconducting transistors, superconducting qubits, and even wear-resistant parts for superconducting devices.

Supplementary Materials: The following supporting information can be downloaded at: https://www.mdpi.com/article/10.3390/ma17091967/s1. Figure S1: The evolution of $T_c$ with different $k$ and $q$ meshes. Figure S2: The atomic structures of (a) $\delta_6$, (b) $\beta_{12}$ and (c) $\chi_3$. Figure S3: (a) The total potential energy fluctuation of BL-$\delta_6$ during AIMD simulation at 500 K. (b) The top view and (c) side view of the atomic configuration of BL-$\delta_6$ on Ag (111) surface after 5 ps of AIMD simulation at 500 K. Figure S4: The phonon spectra of strains under (a) 13% and (b) 14% along a axis, (c) 8% and (d) 9% along b axis. Figure S5: The strain energy per area under different kinds of strains for BL-$\delta_6$. Figure S6: The strain energy per area under different kinds of strains for (a) $\delta_6$, (b) $\beta_{12}$, (c) $\chi_3$ and (d) graphene. Figure S7: The atomic and orbital resolved band structures of BL-$\delta_6$. Figure S8: (a) The electronic band properties of BL-$\delta_6$ under 3% tensile strain along a direction, red line and blue dashed line denote the results

calculated from DFT and Wannier90, respectively. (b) Phonon band structure of BL-$\delta_6$ weighted by EPC $\lambda_{qv}$ with purple circles, isotropic Eliashberg function $\alpha^2F$ and EPC $\lambda(\omega)$, PHDOS from different kinds of boron atoms' contribution. (c) Evolution of the superconducting gap $\Delta_k$ as a function of temperature, calculated by solving the ME equations in the isotropic approximation (yellow dots and dashed line interpolation) and with a fully anisotropic solution where the purple shadowed regions indicate the magnitude distribution of the $\Delta_k$ and the light green dots connected with dashed line represents the average value of the entire anisotropic $\Delta_k$. Figure S9: The results of BL-$\delta_6$ under 6% tensile strain along a direction. The meaning of (a–c) are the same as Figure S8. Figure S10: The results of BL-$\delta_6$ under 10% tensile strain along a direction. The meaning of (a–c) are the same as Figure S8. Figure S11: The results of BL-$\delta_6$ under 13% tensile strain along a direction. The meaning of (a–c) are the same as Figure S8. Refs. [38,39,50,51,58–65] are cited in the Supplementary Materials.

Author Contributions: Conceptualization, C.Z. and B.I.Y.; Methodology, M.S.; Investigation, C.Z. and M.S.; Resources, C.Z., T.A. and B.I.Y.; Writing—original draft, C.Z. and M.S.; Writing—review & editing, T.A. and B.I.Y. All authors have read and agreed to the published version of the manuscript.

Funding: C.Z. acknowledges the financial support from the Scientific and Technology Research Program of Chongqing Municipal Education Commission (KJQN202300515) and the Foundation of Chongqing Normal University (23XLB001). T.A. and B.I.Y. acknowledge the Taif University Research Support Project (TURSPHC2024/1, Saudi Arabia). Work at Rice was supported by the US Office of Naval Research (N00014-22-1-2753).

Institutional Review Board Statement: Not applicable.

Informed Consent Statement: Not applicable.

Data Availability Statement: Data are contained within the article.

Conflicts of Interest: The authors declare no conflicts of interest.

## References
1.  Saito, Y.; Nojima, T.; Iwasa, Y. Highly crystalline 2D superconductors. *Nat. Rev. Mater.* 2016, 2, 16094. [CrossRef]
2.  Li, W.; Huang, J.; Li, X.; Zhao, S.; Lu, J.; Han, Z.V.; Wang, H. Recent progresses in two-dimensional Ising superconductivity. *Mater. Today Phys.* 2021, 21, 100504. [CrossRef]
3.  Qiu, D.; Gong, C.; Wang, S.; Zhang, M.; Yang, C.; Wang, X.; Xiong, J. Recent Advances in 2D Superconductors. *Adv. Mater.* 2021, 33, e2006124. [CrossRef] [PubMed]
4.  Lilia, B.; Hennig, R.; Hirschfeld, P.; Profeta, G.; Sanna, A.; Zurek, E.; Pickett, W.E.; Amsler, M.; Dias, R.; Eremets, M.I.; et al. The 2021 room-temperature superconductivity roadmap. *J. Phys. Condens. Matter* 2022, 34, 183002.
5.  Zhong, C.; Li, X.; Yu, P. Strain-tunable Dirac semimetal phase transition and emergent superconductivity in a borophane. *Commun. Phys.* 2024, 7, 38. [CrossRef]
6.  Gavaler, J.R. Superconductivity in Nb-Ge films above 22 K. *Appl. Phys. Lett.* 1973, 23, 480–482. [CrossRef]
7.  Wu, M.K.; Ashburn, J.R.; Torng, C.J.; Hor, P.H.; Meng, R.L.; Gao, L.; Huang, Z.J.; Wang, Y.Q.; Chu, C.W. Superconductivity at 93 K in a new mixed-phase Y-Ba-Cu-O compound system at ambient pressure. *Phys. Rev. Lett.* 1987, 58, 908–910. [CrossRef] [PubMed]
8.  Peczkowski, P.; Zachariasz, P.; Kowalik, M.; Tokarz, W.; Kumar Naik, S.P.; Żukrowski, J.; Jastrzębski, C.; Dadiel, L.J.; Tabiś, W.; Gondek, Ł. Iron diffusivity into superconducting $\text{YBa}_2\text{Cu}_3\text{O}_{7-\delta}$ at oxygen-assisted sintering: Structural, magnetic, and transport properties. *J. Eur. Ceram. Soc.* 2021, 41, 7085–7097. [CrossRef]
9.  Peczkowski, P.; Kowalik, M.; Zachariasz, P.; Jastrzębski, C.; Jaegermann, Z.; Szterner, P.; Woch, W.M.; Szczytko, J. Synthesis and Physicochemical Properties of Nd-, Sm-, Eu-Based Cuprate High-Temperature Superconductors. *Phys. Status Solidi A* 2018, 215, 1700888. [CrossRef]
10. Bardeen, J.; Cooper, L.N.; Schrieffer, J.R. Theory of Superconductivity. *Phys. Rev.* 1957, 108, 1175–1204. [CrossRef]
11. McMillan, W.L. Transition Temperature of Strong-Coupled Superconductors. *Phys. Rev.* 1968, 167, 331–344. [CrossRef]
12. Allen, P.B.; Dynes, R.C. Transition temperature of strong-coupled superconductors reanalyzed. *Phys. Rev. B* 1975, 12, 905–922. [CrossRef]
13. Blase, X.; Bustarret, E.; Chapelier, C.; Klein, T.; Marcenat, C. Superconducting group-IV semiconductors. *Nat. Mater.* 2009, 8, 375–382. [CrossRef]
14. Bekaert, J.; Petrov, M.; Aperis, A.; Oppeneer, P.M.; Milosevic, M.V. Hydrogen-Induced High-Temperature Superconductivity in Two-Dimensional Materials: The Example of Hydrogenated Monolayer $\text{MgB}_2$. *Phys. Rev. Lett.* 2019, 123, 077001. [CrossRef] [PubMed]
15. Profeta, G.; Calandra, M.; Mauri, F. Phonon-mediated superconductivity in graphene by lithium deposition. *Nat. Phys.* 2012, 8, 131–134. [CrossRef]

16. Lu, H.-Y.; Yang, Y.; Hao, L.; Wang, W.-S.; Geng, L.; Zheng, M.; Li, Y.; Jiao, N.; Zhang, P.; Ting, C.S. Phonon-mediated superconduc- tivity in aluminum-deposited graphene $AlC_8$. *Phys. Rev. B* **2020**, *101*, 214514. [CrossRef]

17. Si, C.; Liu, Z.; Duan, W.; Liu, F. First-principles calculations on the effect of doping and biaxial tensile strain on electron-phonon coupling in graphene. *Phys. Rev. Lett.* **2013**, *111*, 196802. [CrossRef]

18. Zhao, Y.; Lian, C.; Zeng, S.; Dai, Z.; Meng, S.; Ni, J. Two-gap and three-gap superconductivity in $AlB_2$-based films. *Phys. Rev. B* **2019**, *100*, 094516. [CrossRef]

19. Bo, T.; Liu, P.-F.; Yan, L.; Wang, B.-T. Electron-phonon coupling superconductivity in two-dimensional orthorhombic $MB_6$ (M = Mg, Ca, Ti, Y) and hexagonal $MB_6$ (M = Mg, Ca, Sc, Ti). *Phys. Rev. Mater.* **2020**, *4*, 114802. [CrossRef]

20. Zhao, Y.; Lian, C.; Zeng, S.; Dai, Z.; Meng, S.; Ni, J. $MgB_4$ trilayer film: A four-gap superconductor. *Phys. Rev. B* **2020**, *101*, 104507. [CrossRef]

21. Sevik, C.; Bekaert, J.; Petrov, M.; Milošević, M.V. High-temperature multigap superconductivity in two-dimensional metal borides. *Phys. Rev. Mater.* **2022**, *6*, 024803. [CrossRef]

22. Wang, Z.; Zeng, S.; Zhao, Y.; Wang, X.; Ni, J. Three-gap superconductivity in two-dimensional $InB_2$/InB₄ films. *Phys. Rev. B* **2021**, *104*, 174519. [CrossRef]

23. Kaneti, Y.V.; Benu, D.P.; Xu, X.; Yuliarto, B.; Yamauchi, Y.; Golberg, D. Borophene: Two-dimensional Boron Monolayer: Synthesis, Properties, and Potential Applications. *Chem. Rev.* **2022**, *122*, 1000–1051. [CrossRef] [PubMed]

24. Mannix, A.J.; Zhou, X.-F.; Kiraly, B.; Wood, J.D.; Alducin, D.; Myers, B.D.; Liu, X.; Fisher, B.L.; Santiago, U.; Guest, J.R.; et al. Synthesis of borophenes: Anisotropic, two-dimensional boron polymorphs. *Science* **2015**, *350*, 1513–1516. [CrossRef]

25. Feng, B.; Zhang, J.; Zhong, Q.; Li, W.; Li, S.; Li, H.; Cheng, P.; Meng, S.; Chen, L.; Wu, K. Experimental realization of two- dimensional boron sheets. *Nat. Chem.* **2016**, *8*, 563–568. [CrossRef]

26. Penev, E.S.; Kutana, A.; Yakobson, B.I. Can Two-Dimensional Boron Superconduct? *Nano Lett.* **2016**, *16*, 2522–2526. [CrossRef] [PubMed]

27. Gao, M.; Li, Q.-Z.; Yan, X.-W.; Wang, J. Prediction of phonon-mediated superconductivity in borophene. *Phys. Rev. B* **2017**, *95*, 024505. [CrossRef]

28. Zhao, Y.; Zeng, S.; Lian, C.; Dai, Z.; Meng, S.; Ni, J. Multigap anisotropic superconductivity in borophenes. *Phys. Rev. B* **2018**, *98*, 134514. [CrossRef]

29. Zhang, Z.; Penev, E.S.; Yakobson, B.I. Two-dimensional materials: Polyphony in B flat. *Nat. Chem.* **2016**, *8*, 525–527. [CrossRef]

30. Gao, N.; Wu, X.; Jiang, X.; Bai, Y.; Zhao, J. Structure and stability of bilayer borophene: The roles of hexagonal holes and interlayer bonding. *FlatChem* **2017**, *7*, 48–54. [CrossRef]

31. Zhong, H.; Huang, K.; Yu, G.; Yuan, S. Electronic and mechanical properties of few-layer borophene. *Phys. Rev. B* **2018**, *98*, 054104. [CrossRef]

32. Yan, L.; Ku, R.; Zou, J.; Zhou, L.; Zhao, J.; Jiang, X.; Wang, B.-T. Prediction of superconductivity in bilayer borophenes. *RSC Adv.* **2021**, *11*, 40220–40227. [CrossRef] [PubMed]

33. Liu, X.; Li, Q.; Ruan, Q.; Rahn, M.S.; Yakobson, B.I.; Hersam, M.C. Borophene synthesis beyond the single-atomic-layer limit. *Nat. Mater.* **2022**, *21*, 35–40. [CrossRef]

34. Chen, C.; Lv, H.; Zhang, P.; Zhuo, Z.; Wang, Y.; Ma, C.; Li, W.; Wang, X.; Feng, B.; Cheng, P.; et al. Synthesis of bilayer borophene. *Nat. Chem.* **2022**, *14*, 25–31. [CrossRef] [PubMed]

35. Ma, Y.-Y.; Zhao, X.-Y.; Zan, W.; Mu, Y.; Zhang, Z.; Li, S.-D. Prediction of freestanding semiconducting bilayer borophenes. *Nano Res.* **2022**, *15*, 5752–5757. [CrossRef]

36. Liu, X.; Hersam, M.C. 2D materials for quantum information science. *Nat. Rev. Mater.* **2019**, *4*, 669–684. [CrossRef]

37. Liu, P.; Lei, B.; Chen, X.; Wang, L.; Wang, X. Superior carrier tuning in ultrathin superconducting materials by electric-field gating. *Nat. Rev. Phys.* **2022**, *4*, 336–352. [CrossRef]

38. Kresse, G.; Furthmüller, J. Efficiency of ab-initio total energy calculations for metals and semiconductors using a plane-wave basis set. *Comp. Mater. Sci.* **1996**, *6*, 15–50. [CrossRef]

39. Kresse, G.; Furthmüller, J. Efficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set. *Phys. Rev. B* **1996**, *54*, 11169–11186. [CrossRef] [PubMed]

40. Sun, M.; Luo, Y.; Yan, Y.; Schwingenschlögl, U. Ultrahigh Carrier Mobility in the Two-Dimensional Semiconductors $B_8Si_4$, $B_8Ge_4$, and $B_8Sn_4$. *Chem. Mater.* **2021**, *33*, 6475–6483. [CrossRef]

41. Zhou, X.-F.; Dong, X.; Oganov, A.R.; Zhu, Q.; Tian, Y.; Wang, H.-T. Semimetallic Two-Dimensional Boron Allotrope with Massless Dirac Fermions. *Phys. Rev. Lett.* **2014**, *112*, 085502. [CrossRef]

42. Ebrahimi, M. The birth of bilayer borophene. *Nat. Chem.* **2022**, *14*, 3–4. [CrossRef] [PubMed]

43. Božović, I. Doubling down on borophene electronics. *Nat. Mater.* **2022**, *21*, 11–12. [CrossRef] [PubMed]

44. Wang, Z.; Lü, T.-Y.; Wang, H.-Q.; Feng, Y.P.; Zheng, J.-C. High anisotropy of fully hydrogenated borophene. *Phys. Chem. Chem. Phys.* **2016**, *18*, 31424–31430. [CrossRef] [PubMed]

45. Andrew, R.C.; Mapasha, R.E.; Ukpong, A.M.; Chetty, N. Mechanical properties of graphene and boronitrene. *Phys. Rev. B* **2012**, *85*, 125428. [CrossRef]

46. Nye, J.F. *Physical Properties of Crystals*; Clarendon Press: Oxford, UK, 1985.

47. Wang, H.; Li, Q.; Gao, Y.; Miao, F.; Zhou, X.-F.; Wan, X.G. Strain effects on borophene: Ideal strength, negative Possion’s ratio and phonon instability. *New J. Phys.* **2016**, *18*, 073016. [CrossRef]

48. Wei, Q.; Peng, X. Superior mechanical flexibility of phosphorene and few-layer black phosphorus. *Appl. Phys. Lett.* 2014, 104, 251915. [CrossRef]

49. Liu, F.; Ming, P.; Li, J. Ab initio calculation of ideal strength and phonon instability of graphene under tension. *Phys. Rev. B* 2007, 76, 064120. [CrossRef]

50. Pizzi, G.; Vitale, V.; Arita, R.; Blügel, S.; Freimuth, F.; Géranton, G.; Gibertini, M.; Gresch, D.; Johnson, C.; Koretsune, T.; et al. Wannier90 as a community code: New features and applications. *J. Phys. Condens. Matter* 2020, 32, 165902. [CrossRef]

51. Noffsinger, J.; Giustino, F.; Malone, B.D.; Park, C.-H.; Louie, S.G.; Cohen, M.L. EPW: A program for calculating the electron-phonon coupling using maximally localized Wannier functions. *Comput. Phys. Commun.* 2010, 181, 2140-2148. [CrossRef]

52. Huang, Y.; Shirodkar, S.N.; Yakobson, B.I. Two-Dimensional Boron Polymorphs for Visible Range Plasmonics: A First-Principles Exploration. *J. Am. Chem. Soc.* 2017, 139, 17181-17185. [CrossRef]

53. Xiao, H.; Cao, W.; Ouyang, T.; Guo, S.; He, C.; Zhong, J. Lattice thermal conductivity of borophene from first principle calculation. *Sci. Rep.* 2017, 7, 45986. [CrossRef] [PubMed]

54. Ruan, Q.; Wang, L.; Bets, K.V.; Yakobson, B.I. Step-Edge Epitaxy for Borophene Growth on Insulators. *ACS Nano* 2021, 15, 18347-18353. [CrossRef] [PubMed]

55. Qiu, L.; Zhang, X.; Kong, X.; Mitchell, I.; Yan, T.; Kim, S.Y.; Yakobson, B.I.; Ding, F. Theory of sigma bond resonance in flat boron materials. *Nat. Commun.* 2023, 14, 1804. [CrossRef] [PubMed]

56. Neverov, V.D.; Lukyanov, A.E.; Krasavin, A.V.; Vagov, A.; Croitoru, M.D. Correlated disorder as a way towards robust superconductivity. *Commun. Phys.* 2022, 5, 177. [CrossRef]

57. Ghosal, A.; Randeria, M.; Trivedi, N. Inhomogeneous pairing in highly disordered s-wave superconductors. *Phys. Rev. B* 2001, 65, 014501. [CrossRef]

58. Perdew, J.P.; Chevary, J.A.; Vosko, S.H.; Jackson, K.A.; Pederson, M.R.; Singh, D.J.; Fiolhais, C. Atoms, molecules, solids, and surfaces: Applications of the generalized gradient approximation for exchange and correlation. *Phys. Rev. B* 1992, 46, 6671-6687. [CrossRef]

59. Blöchl, P.E. Projector augmented-wave method. *Phys. Rev. B* 1994, 50, 17953-17979. [CrossRef] [PubMed]

60. Evans, D.J.; Holian, B.L. The Nose-Hoover thermostat. *J. Chem. Phys.* 1985, 83, 4069-4074. [CrossRef]

61. Nosé, S. A unified formulation of the constant temperature molecular dynamics methods. *J. Chem. Phys.* 1984, 81, 511-519. [CrossRef]

62. Giannozzi, P.; Andreussi, O.; Brumme, T.; Bunau, O.; Nardelli, M.B.; Calandra, M.; Car, R.; Cavazzoni, C.; Ceresoli, D.; Cococcioni, M.; et al. Advanced capabilities for materials modelling with Quantum ESPRESSO. *J. Phys. Condens. Matter* 2017, 29, 465901. [CrossRef] [PubMed]

63. Baroni, S.; de Gironcoli, S.; Dal Corso, A.; Giannozzi, P. Phonons and related crystal properties from density-functional perturbation theory. *Rev. Mod. Phys.* 2001, 73, 515-562. [CrossRef]

64. Zhong, C.; Wu, W.; He, J.; Ding, G.; Liu, Y.; Li, D.; Yang, S.A.; Zhang, G. Two-dimensional honeycomb borophene oxide: Strong anisotropy and nodal loop transformation. *Nanoscale* 2019, 11, 2468-2475. [CrossRef] [PubMed]

65. Cadelano, E.; Palla, P.L.; Giordano, S.; Colombo, L. Elastic properties of hydrogenated graphene. *Phys. Rev. B* 2010, 82, 235414. [CrossRef]

Disclaimer/Publisher's Note: The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content.
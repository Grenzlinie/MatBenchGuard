# A DFT+U study on the thermodynamic properties of defective $\mathbf{Gd_2Zr_2O_7}$ pyrochlore

Menglu Li$^{a,1}$, Pengcheng Li$^{a,1}$, Haiyan Xiao$^{a,*}$, Haibin Zhang$^{b,*}$, Xiaotao Zu$^{a}$

$^{a}$ School of Physics, University of Electronic Science and Technology of China, Chengdu 610054, China
$^{b}$ Institute of Nuclear Physics and Chemistry, Chinese Academy of Engineering Physics, Mianyang 621900, China

---

## ARTICLE INFO
**Article history:**
Received 12 March 2020
Revised 28 June 2020
Accepted 26 July 2020
Available online xxx

**Keywords:**
Pyrochlores
First-principles calculations
Mechanical and thermal properties

## ABSTRACT
With many technologies and applications downscaling to nanometer dimensions, single point defects can modify the physical properties of compounds significantly, and advancing the fundamental understanding is critical to defect engineering and control of material properties. In the present study, first-principles calculations based on density functional theory (DFT) are carried out to study how the presence of point defects (vacancy, interstitial and antisite) affects the mechanical and thermal properties of $\text{Gd}_2\text{Zr}_2\text{O}_7$ pyrochlore. As compared with the pure $\text{Gd}_2\text{Zr}_2\text{O}_7$, the defective states exhibit smaller elastic moduli and better ductility. The Debye temperatures for the defective $\text{Gd}_2\text{Zr}_2\text{O}_7$ are generally lower than those for pristine compound, indicating that the defective states have larger thermal expansion coefficient. This study suggests that under irradiation the thermomechanical properties of pyrochlores are influenced significantly, and intentional controlling of the point defects may benefit to improve their mechanical stability.

© 2020 Elsevier B.V. All rights reserved.

---

## 1. Introduction
Pyrochlore compounds, with general formula $\text{A}_2\text{B}_2\text{O}_7$ (A=Y or lanthanide elements; B=Sn, Ti, Zr or Hf), are taken as attractive candidates for a variety of applications, including hosts for oxidation catalysts, solid electrolytes in high temperature fuel cells and ceramic thermal barrier coatings, due to their enormous range of physical, chemical and electronic properties such as low thermal conductivity, high thermal stability as well as high melting point [1,2]. Especially, there has been a great interest in using pyrochlore materials as host matrices for nuclear wastes, particularly for long half-life and high radioactivity actinides [3-8]. However, self-radiation from actinide decay may result in atomic defects, lattice disorder and even structural amorphization, and their mechanical properties and performance may be affected significantly.

As a typical member of $\text{A}_2\text{B}_2\text{O}_7$ pyrochlores, $\text{Gd}_2\text{Zr}_2\text{O}_7$ is of special interest due to its strong resistance to radiation-induced amorphization. Experimentally, Sattonnay et al. have investigated the irradiation response of $\text{Gd}_2\text{Zr}_2\text{O}_7$ by 92 MeV Xe ions and found that $\text{Gd}_2\text{Zr}_2\text{O}_7$ is transformed into a radiation-resistant anion-deficient fluorite structure [9]. Lang et al. analyzed the structure of the ion tracks created by irradiation (1.43 GeV Xe ions) and reported that no amorphous tracks are produced along the ion trajectory in $\text{Gd}_2\text{Zr}_2\text{O}_7$ [10,11]. Kumari et al. reported that the $\text{Gd}_2\text{Zr}_2\text{O}_7$ pyrochlore with relatively low $r_\text{A}/r_\text{B}$ ratio is more radiation resistant than other pyrochlores [12,13]. Meanwhile, a number of theoretical calculations have been carried out to investigate the relationship between defect stability and radiation resistance [14-21]. Sickafus et al. have calculated the cation antisite defect formation energy of a series of pyrochlores and determined the defect formation energy for $\text{Gd}_2\text{Zr}_2\text{O}_7$ to be about 3.6 eV. They reported that compounds with similar cation radii should behave robustly in a radiation environment [21]. Minervini et al. calculated disorder reaction energies across a wide variety of $\text{A}_2\text{B}_2\text{O}_7$ pyrochlore oxides and reported that the association of anion Frenkel pairs and cation antisite disorder is important to the radiation resistance of pyrochlores [20]. Sattonnay and Tétot investigated the properties of oxygen Frenkel pairs, cation antisite defects and cation Frenkel pairs in $\text{Gd}_2\text{Ti}_2\text{O}_7$ and $\text{Gd}_2\text{Zr}_2\text{O}_7$ to determine the role played by the defect stability in the radiation tolerance of these compounds. They proposed that the defect stability in $\text{A}_2\text{B}_2\text{O}_7$ depends on the ability of B atoms to accommodate high coordination number [19]. Obviously, the defect stability in pyrochlores has significant impact on their radiation tolerance.

In addition, defects in materials can also influence the thermodynamic stability of materials. For instance, Wan et al. have investigated the effect of point defects on the thermal transport properties of $(\text{La}_x\text{Gd}_{1-x})_2\text{Zr}_2\text{O}_7$ and found that the introduction of

---

* Corresponding authors.
E-mail addresses: hyxiao@uestc.edu.cn (H. Xiao), hbzhang@imr.ac.cn (H. Zhang).
$^{1}$ These authors contributed equally to this work.

https://doi.org/10.1016/j.jnucmat.2020.152425
0022-3115/© 2020 Elsevier B.V. All rights reserved.

![](./images/812579376133570561_1.jpg)

Fig. 1. Variation of band gap and bulk modulus of $Gd_2Zr_2O_7$ with the $U_{eff}$ values for Gd 4f electrons. $^{a}$Ref.[55]. $^{b}$Ref.[56] . $^{c}$Ref.[48] . $^{d}$Ref.[57] . $^{e}$Ref.[58] . $^{f}$Ref.[59].

point defects can decrease the thermal conductivity of the solid solution [22]. Zhao et al. have reported that incorporation of Nd into Zr-site of $Gd_2Zr_2O_7$ results in smaller Young's modulus, better ductility, stronger elastic anisotropy and lower Debye temperature than pure state [23]. Therefore, understanding and predicting the physical properties of defective compounds are key to the devel- opment of advanced materials, particularly those that find appli- cations in extreme environments where defects may prevail. Thus far, it still remains unknown that how the existence of point de- fects affects the thermodynamic properties of $Gd_2Zr_2O_7$, both ex- perimentally and theoretically. In order to better understand the behaviors of $Gd_2Zr_2O_7$ under radiation environment, it is of vital importance to perform a detailed and in-depth investigation of the mechanical and thermal properties of the defective $Gd_2Zr_2O_7$. In the present work, we employ first-principles calculations based on density functional theory to investigate how the presence of point defects, i.e., vacancy, antisite and interstitial defects, influences the thermodynamic properties of $Gd_2Zr_2O_7$. The thermodynamic prop- erties of defective $Gd_2Zr_2O_7$ are systematically described, including elastic constants, elastic modulus, ductility and Debye temperature. The presented results provide an atomic-level insight into the ef- fect of point defects on the mechanical and thermal properties of $Gd_2Zr_2O_7$, and will be useful for promoting further experimental and theoretical investigations to enhance the mechanical stability of pyrochlores under irradiation.

## 2. Computational details

Our calculations are carried out within the DFT framework us- ing the projector augmented wave (PAW) method [24], as imple- mented in the Vienna Ab Initio Simulation Package (VASP) [25]. For the exchange-correlation functional, the Perdew-Burke-Ernzerhof functional under the generalized gradient approximation (GGA) is used [26]. The kinetic energy cutoff is set to be 600 eV and a $2 \times 2 \times 2$ Monkhorst-Pack k-point mesh is employed. The Hub- bard U correction proposed by Dudarev et al. [27] is introduced to modify the strongly correlated Gd 4f electrons. A series of test cal- culations have been carried out to explore the effects of $U_{eff}$ values on lattice parameters, band gap and bulk modulus of $Gd_2Zr_2O_7$. It is found that consideration of Hubbard U correction has negligi- ble influences on the lattice parameters. Variation of band gap and bulk modulus of $Gd_2Zr_2O_7$ with the $U_{eff}$ values are illustrated in Fig. 1. It is shown that the employment of $U_{eff}$=4 eV yields good agreement with the experimental values for both band gap and bulk modulus [48,55-59], which is consistent with the literature value reported by Alaydrus et al. [28]. Therefore, a $U_{eff}$=4 eV is employed in the subsequent calculations. Fig. 2 presents the pro- jected and total density of state distribution for $Gd_2Zr_2O_7$ obtained by DFT and DFT+U methods, along with the calculated lattice pa- rameters. It is shown that consideration of Hubbard U correction affects the structural parameters for $Gd_2Zr_2O_7$ very slightly, while it makes the itinerant Gd 4f electrons more localized. Consider- ing that Gd is a heavy metal element, we carry out test calcula- tions to investigate if it is necessary to take into account spin or- bit coupling (SOC) effects in this study. A comparison of the lat- tice constants, oxygen positional parameter $x_{O48f}$ and elastic con- stants obtained by DFT+U and DFT+U+SOC methods is presented in Table 1. It is found that the SOC effects affect the structural pa- rameters and elastic constants slightly. Such effects, thus, are not considered in all the subsequent calculations.

Table 1
A comparison of the lattice parameters and elastic constants for $Gd_2Zr_2O_7$ ob- tained by DFT+U and DFT+U+SOC methods.

<table>
<thead>
<tr>
<th rowspan="2"></th>
<th colspan="2">Lattice parameters</th>
<th colspan="3">Elastic constants</th>
</tr>
<tr>
<th>$a_0$ (Å)</th>
<th>$x_{O48f}$</th>
<th>$C_{11}$ (GPa)</th>
<th>$C_{12}$ (GPa)</th>
<th>$C_{44}$ (GPa)</th>
</tr>
</thead>
<tbody>
<tr>
<td>DFT+U</td>
<td>10.666</td>
<td>0.339</td>
<td>285.1</td>
<td>102.5</td>
<td>82.1</td>
</tr>
<tr>
<td>DFT+U+SOC</td>
<td>10.665</td>
<td>0.339</td>
<td>284.2</td>
<td>101.7</td>
<td>82.4</td>
</tr>
</tbody>
</table>

The point defects taken into account in the simulations include vacancy, interstitial and antisite defects, corresponding to a con- centration of 1.14 % for each defect. Under irradiation, a number of defects or defect clusters are often created. For example, when the Zr is irradiated by 1.33 MeV electrons (corresponding to thresh- old displacement energy of 39 eV) along the [100] direction in $Gd_2Zr_2O_7$, one Zr vacancy, one $Zr_{Gd}$ antisite defect, one Gd inter- stitial, two oxygen vacancies and two oxygen interstitials are cre- ated [29]. When the Gd is irradiated by 2.04 MeV electrons (cor- responding to threshold displacement energy of 56 eV) along the [100] direction in $Gd_2Zr_2O_7$, one Gd vacancy, one $Gd_{Zr}$ antisite and one Zr interstitial are generated [30]. Generally, in different cases different types of defects are generated and these defects interact strongly with each other, which makes it difficult to understand how each type of defect influences the structural, electronic and mechanical properties of the materials. The focus of this study is to investigate how each type of defect influences the thermodynamic properties of $Gd_2Zr_2O_7$. Hence, isolated defects are considered in this work. The geometrical configurations of considered point de- fects are illustrated in Fig. 3.

## 3. Results and discussion

### 3.1. The defect formation energies for $Gd_2Zr_2O_7$

To investigate the stability of point defects, we calculate the de- fect formation energies based on the optimized structures. The de- fect formation energies $(E_F)$ of vacancies, interstitial and antisite defects are calculated by the following three equations, respec- tively [31,32]:

$$
E_{F}^{VacX}=E^{VacX}-E_{tot}+E_{X}, \tag{1}
$$

$$
E_{F}^{IntX}=E^{IntX}-E_{tot}-E_{X}, \tag{2}
$$

$$
E_{F}^{X_{Y}}=E^{X_{Y}}-E_{tot}-E_{X}+E_{Y}, \tag{3}
$$

where $E^{VacX}$, $E^{IntX}$, and $E^{X_{Y}}$ are the total energies of the defective $Gd_2Zr_2O_7$ after relaxation,$E_{tot}$ is the total energy of the relaxed ideal supercell and $E_{X(Y)}$ is the energy per atom of each chemical species in its reference state. The value of $E_{X(Y)}$ is obtained under X(Y)-rich conditions, i.e., $E_{X(Y)} \approx E_{X(Y)}^{bulk}$, where $E_{X(Y)}^{bulk}$ is the total en- ergy of bulk X(Y). Our results are tabulated in Table 2. Among the vacancy defects, the $V_{O48f}$ ($O_{48f}$ vacancy) defect has the lowest for-

![](./images/812579376133570561_2.jpg)

Fig. 2. The total and projected density of state distribution for $Gd_2Zr_2O_7$ obtained by the (a) DFT and (b) DFT+U methods. The Fermi level is located at 0 eV.

<table>
<caption>Table 2<br>The defect formation energies (eV) for $Gd_2Zr_2O_7$. $V_X$ ($X=$ Gd, Zr, $O_{48f}$ or $O_{8b}$): X vacancy; $X_Y$ ($X=$ Gd or Zr, $Y=$ Zr, Gd or $O_{48f}$): X occupying the Y lattice site; $X_{8a}$ ($X=$ Gd, Zr, O): X interstitial occupying the 8a site; $X_{intN}$ ($X=$ Gd, Zr or O, $N=1,2,3$): X interstitial occupying the int1 (0.5, 0.375, 0.625), int2 (0.5, 0.625, 0.625) and int3 (0.5, 0.125, 0.375), respectively.</caption>
<thead>
<tr>
<th>Defect type</th>
<th>Defect formation energy</th>
<th>Defect type</th>
<th>Defect formation energy</th>
</tr>
<tr>
<th colspan="2">Vacancy</th>
<th colspan="2">Interstitial</th>
</tr>
</thead>
<tbody>
<tr>
<td>$V_{Gd}$</td>
<td>12.65</td>
<td>$Zr_{8a}$</td>
<td>3.30</td>
</tr>
<tr>
<td>$V_{Zr}$</td>
<td>15.16</td>
<td>$Zr_{int1}$</td>
<td>4.60</td>
</tr>
<tr>
<td>$V_{O48f}$</td>
<td>4.67</td>
<td>$Zr_{int2}$</td>
<td>3.45</td>
</tr>
<tr>
<td>$V_{O8b}$</td>
<td>6.7</td>
<td>$Zr_{int3}$</td>
<td>4.56</td>
</tr>
<tr>
<td>$Gd_{Zr}$</td>
<td>2.73</td>
<td>$O_{8a}$</td>
<td>0.32</td>
</tr>
<tr>
<td>$Zr_{Gd}$</td>
<td>2.32</td>
<td>$O_{int1}$</td>
<td>1.79</td>
</tr>
<tr>
<td>$Gd_{O48f}$</td>
<td>13.23</td>
<td>$O_{int2}$</td>
<td>0.52</td>
</tr>
<tr>
<td></td>
<td></td>
<td>$O_{int3}$</td>
<td>1.81</td>
</tr>
<tr>
<td></td>
<td></td>
<td>$Gd_{8a}$</td>
<td>4.65</td>
</tr>
<tr>
<td></td>
<td></td>
<td>$Gd_{int1}$</td>
<td>3.74</td>
</tr>
<tr>
<td></td>
<td></td>
<td>$Gd_{int2}$</td>
<td>2.73</td>
</tr>
<tr>
<td></td>
<td></td>
<td>$Gd_{int3}$</td>
<td>3.75</td>
</tr>
</tbody>
</table>

mation energy of 4.67 eV. The next favorable defect is $V_{O8b}$, as indicated by the formation energy of 6.7 eV. The $V_{Zr}$ is found to be the most unfavorable, as indicated by the high formation energy of 15.16 eV. The defect stability follows the trend of $V_{Zr}<V_{Gd}<V_{O48f}$, and similar trend has been observed for $A_2Zr_2O_7$ like $La_2Zr_2O_7$ [33] and $Y_2Zr_2O_7$ [32]. For the antisite defects, the $Zr_{Gd}$ (Zr occupying the Gd lattice site) antisite defect is found to be energetically the most favorable, as indicated by the smallest formation energy of 2.32 eV. The next favorable defect is the $Gd_{Zr}$ antisite defect (Gd occupying the Zr lattice site), with the formation energy of 2.73 eV. Among the considered antisite defects, the $Gd_{O48f}$ (Gd occupying the $O_{48f}$ lattice site) has the largest formation energy of 13.23 eV, suggesting that it is more difficult to form than other antisite defects. The interstitial is another important type of point defect in the zirconate pyrochlores. In the present study, we firstly consider four different interstitial sites, including the 8a (0.375, 0.375, 0.875), int1 (0.5, 0.375, 0.625), int2 (0.5, 0.625, 0.625) and int3 (0.5, 0.125, 0.375) sites, which have been revealed from ab initio molecular dynamics simulation of ion-solid interaction in pyrochlores [29,34]. Three kinds of atoms (Gd, Zr and O) are introduced into the four different interstitial sites without considering their corresponding vacancies. The defect formation energies of Gd, Zr and O interstitial occupying four different sites are listed in Table 2. The $Gd_{int2}$, $Zr_{8a}$ and $O_{8a}$ defects are determined to be the most favorable defects for the Gd, Zr and O interstitials, respectively. This is because the $Gd_{int2}$, $Zr_{8a}$ and $O_{8a}$ defects have the smallest for-

<table>
<caption>Table 3
The calculated lattice constant a₀ (Å) and O₄₈բ positional parameter x for ideal and defective Gd₂Zr₂O₇ (GZO).V₀₄₈բ: O₄₈բ vacancy; Zr<sub>Gd</sub>: Zr occupying the Gd lattice site; Gd<sub>int2</sub>: Gd interstitial occupying the int2 (0.5, 0.625, 0.625); Zr<sub>8a</sub>: Zr interstitial occupying the 8a site; O<sub>8a</sub>: O interstitial occupying the 8a site.</caption>
<thead>
<tr>
<th colspan="2"></th>
<th>Ideal GZO</th>
<th colspan="5">Defective GZO</th>
</tr>
<tr>
<th colspan="2"></th>
<th></th>
<th>V₀₄₈բ</th>
<th>Zr<sub>Gd</sub></th>
<th>Gd<sub>int2</sub></th>
<th>Zr<sub>8a</sub></th>
<th>O<sub>8a</sub></th>
</tr>
</thead>
<tbody>
<tr>
<td>a₀ (Å)</td>
<td>Our Cal.</td>
<td>10.666</td>
<td>10.646</td>
<td>10.630</td>
<td>10.695</td>
<td>10.696</td>
<td>10.664</td>
</tr>
<tr>
<td></td>
<td>Other Cal. [35]</td>
<td>10.660</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td>Exp. [36]</td>
<td>10.540</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>x₀₄₈բ</td>
<td>Our Cal.</td>
<td>0.339</td>
<td>0.340</td>
<td>0.342</td>
<td>0.338</td>
<td>0.341</td>
<td>0.341</td>
</tr>
<tr>
<td></td>
<td>Other Cal. [35]</td>
<td>0.339</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td>Exp. [37]</td>
<td>0.345</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

![](./images/812579376133570561_3.jpg)

Fig. 3. Schematic view of geometrical structures of ideal and defective Gd₂Zr₂O₇: (a) ideal state; (b) vacancy defective states; (c) antisite defective states; (d)interstitial defective states. The blue, brown and grey spheres represent the Gd, Zr and O atoms, respectively. V<sub>X</sub> (X = Gd, Zr, O₄₈բ or O<sub>8b</sub>): X vacancy; X<sub>Y</sub> (X = Gd or Zr, Y = Zr, Gd or O₄₈բ): X occupying the Y lattice site; X<sub>8a</sub> (X= Gd, Zr or O): X interstitial occupying the 8a site; X<sub>intN</sub> (X= Gd, Zr or O, N = 1, 2, 3): X interstitial occupying the int1 (0.5, 0.375, 0.625), int2 (0.5, 0.625, 0.625) and int3 (0.5, 0.125, 0.375), respectively. The yellow, green and red spheres represent the vacancy, antisite and interstitial defects, respectively.

mation energy of 2.73, 3.30 and 0.32 eV for the Gd, Zr and O interstitials, respectively. Comparing the defect stability in Gd₂Zr₂O₇, we find that the V₀₄₈բ, Zr<sub>Gd</sub>, Gd<sub>int2</sub>, Zr<sub>8a</sub>, and O<sub>8a</sub> defects are energetically more preferable than other considered vacancies, antisites and interstitials. These defects, thus, are considered in the subsequent calculations, and how the presence of these defects influences the structural and thermodynamic properties of Gd₂Zr₂O₇ are further investigated.

### 3.2. The structural properties of ideal and defective Gd₂Zr₂O₇

In order to study the influence of defects (V₀₄₈բ, Zr<sub>Gd</sub>, Gd<sub>int2</sub>, Zr<sub>int2</sub>, and O<sub>8a</sub> defects) on the thermal and mechanical properties in Gd₂Zr₂O₇, we first analyze the structural properties of ideal and defective Gd₂Zr₂O₇. The optimized lattice constants and positional parameter x₀₄₈բ are listed in Table 3, together with available experimental and theoretical data [35-37]. For ideal Gd₂Zr₂O₇, the calculated lattice constant of 10.666 Å is slightly larger than the experimental value of 10.540 Å, while in good agreement with other calculations of 10.660 Å [35,36]. As compared with the pristine state, the a₀ value of 10.646 Å for Gd₂Zr₂O₇ containing V₀₄₈բ defect is slightly reduced. In the case of Zr occupying the Gd-site, the lattice constant is calculated to be 10.63 Å. This is because the effective ionic radius of 0.84 Å for Zr³⁺(eight-coordinated) [38], is smaller than that of 1.053 Å for Gd³⁺(eight-coordinated) [38], which leads to decreased lattice constant for Gd₂Zr₂O₇ with Zr<sub>Gd</sub> defect. It is noted that the Gd<sub>int2</sub> and Zr<sub>8a</sub> defects increase the lattice constant slightly, as indicated by the values of 10.695 Å for Gd<sub>int2</sub> and 10.696 Å for Zr<sub>8a</sub>. As for O<sub>8a</sub> defect, the lattice constant is comparable to that of ideal phase.

The positional parameter x₀₄₈բ is often used to predict the degree of disorder in A₂B₂O₇ pyrochlores [36]. Generally, pyrochlores with x₀₄₈բ closer to 0.375 tend to undergo a transition from pyrochlore to defect-fluorite structure [33,39]. The calculated x₀₄₈բ of ideal Gd₂Zr₂O₇ is 0.339, in reasonable agreement with the experimental and theoretical results [35,40]. As defects (V₀₄₈բ, Zr<sub>Gd</sub>, Gd<sub>int2</sub>, Zr<sub>int2</sub>, and O<sub>8a</sub> defects) are introduced to Gd₂Zr₂O₇, the x₀₄₈բ values change slightly, i.e., varying from 0.338 to 0.342. The slight changes indicate that Gd₂Zr₂O₇ with considered point defects still remain ordered pyrochlore structure.

<table>
<caption>Table 4
The elastic constants (Gpa), bulk modulus B (Gpa), shear modulus G (Gpa) and Young's modulus E (Gpa) for pristine Gd₂Zr₂O₇.</caption>
<thead>
<tr>
<th></th>
<th>C₁₁</th>
<th>C₁₂</th>
<th>C₄₄</th>
<th>B<sub>VRH</sub></th>
<th>G<sub>VRH</sub></th>
<th>E</th>
</tr>
</thead>
<tbody>
<tr>
<td>Our Cal.</td>
<td>285.1</td>
<td>102.5</td>
<td>82.1</td>
<td>163.4</td>
<td>85.7</td>
<td>218.8</td>
</tr>
<tr>
<td>Other Cal. [42]</td>
<td>289</td>
<td>103</td>
<td>85</td>
<td>165</td>
<td>88</td>
<td>224</td>
</tr>
<tr>
<td>Exp.</td>
<td></td>
<td></td>
<td></td>
<td>153<sup>36,37</sup>
174<sup>44</sup></td>
<td>80<sup>36,37</sup>
92<sup>44</sup></td>
<td>205<sup>36,37</sup>
236<sup>44</sup></td>
</tr>
</tbody>
</table>

### 3.3. The elastic constants and elastic moduli of ideal and defective Gd₂Zr₂O₇

The elastic constants (C<sub>ij</sub>) determine the response of the crystal to external forces, and provide important information about the stability, stiffness and hardness of materials. For cubic systems, there are three independent elastic constants, i.e., C₁₁, C₁₂ and C₄₄, where C₁₁ represents the uniaxial deformation along the [001] direction, C₁₂ is the pure shear stress at (110) crystal plane along the [110] direction and C₄₄ corresponds to the pure shear deformation on the (100) crystal plane [41]. The calculated elastic constants for ideal Gd₂Zr₂O₇ are summarized in Table 4, along with other theoretical values for comparison [42]. It is shown that the calculated results of C₁₁=285.1 GPa, C₁₂=102.5 GPa and C₄₄=82.1 GPa are comparable with other theoretical results [42].

Based on the optimized structures, the elastic constants for defective Gd₂Zr₂O₇ are calculated and summarized in Table 5. The calculated elastic constants satisfy the generalized elastic stability criteria for cubic crystals, i.e., C₁₁+2C₁₂>0; C₄₄>0; C₁₁ - C₁₂>0 [41],

<table><caption>Table 5
The elastic constants ($C_{11}$, $C_{12}$ and $C_{44}$ in Gpa) for ideal and defective $Gd_2Zr_2O_7$ (GZO). $V_{O48f}$: $O_{48f}$ vacancy; $Zr_{Gd}$: Zr occupying the Gd lattice site; $Gd_{int2}$: Gd interstitial occupying the int2 (0.5, 0.625, 0.625); $Zr_{8a}$: Zr interstitial occupying the 8a site; $O_{8a}$: O interstitial occupying the 8a site.</caption>
<thead>
  <tr>
    <th rowspan="2"></th>
    <th>Ideal GZO</th>
    <th colspan="5">Defective GZO</th>
  </tr>
  <tr>
    <th></th>
    <th>$V_{O48f}$</th>
    <th>$Zr_{Gd}$</th>
    <th>$Gd_{int2}$</th>
    <th>$Zr_{8a}$</th>
    <th>$O_{8a}$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>$C_{11}$</td>
    <td>285.1</td>
    <td>281.5</td>
    <td>293.4</td>
    <td>274.8</td>
    <td>275.8</td>
    <td>269.5</td>
  </tr>
  <tr>
    <td>$C_{12}$</td>
    <td>102.5</td>
    <td>102.4</td>
    <td>104.5</td>
    <td>91.7</td>
    <td>101.1</td>
    <td>113.5</td>
  </tr>
  <tr>
    <td>$C_{44}$</td>
    <td>82.1</td>
    <td>74.3</td>
    <td>76.3</td>
    <td>51.3</td>
    <td>40.3</td>
    <td>76.7</td>
  </tr>
</tbody>
</table>

meaning that all the considered defective $Gd_2Zr_2O_7$ compositions are mechanically stable. The $Gd_{int2}$ and $Zr_{8a}$ defects decrease the $C_{44}$ significantly, i.e., 37.5 % and 50.9 %, respectively. The existence of $Gd_{int2}$ interstitial defect also decreases the $C_{12}$ value by 10.5 %. Obviously, the defects of $Gd_{int2}$ and $Zr_{8a}$ affect the elastic constants of $Gd_2Zr_2O_7$ remarkably. On the other hand, the $C_{12}$ value of $Gd_2Zr_2O_7$ containing $O_{8a}$ interstitial defect is increased by 10.7 %. The existence of $Zr_{Gd}$ antisite defect increases the $C_{11}$ and $C_{12}$ values relatively slightly, i.e., 2.9 % and 1.9 %, respectively. These results suggest that the $Gd_{int2}$ and $Zr_{8a}$ defects generally weaken the resistance to uniaxial and shear deformation.

The bulk, shear and Young's moduli can be estimated using Voigt-Reuss-Hill (VRH) approximation, which is an average of the lower bound of Voigt and upper bound of Reuss, and can provide a good estimation of the mechanical properties from the elastic constants [43-45]. For $Gd_2Zr_2O_7$ pyrochlore, it belongs to Fd3m space group (No. 227) with face-centered cubic structure. The elastic moduli and Poisson's ratio can be defined as follows [40]:

$$
B_V = B_R = \frac{1}{3}(C_{11} + 2C_{12}), \tag{4}
$$

$$
G_V = \frac{1}{5}(C_{11} - C_{12} + 3C_{44}), \tag{5}
$$

$$
G_R = \frac{5(C_{11} - C_{12})C_{44}}{4C_{44} + 3(C_{11} - C_{12})}, \tag{6}
$$

$$
B_{VRH} = \frac{1}{2}(B_V + B_R), \tag{7}
$$

$$
G_{VRH} = \frac{1}{2}(G_V + G_R), \tag{8}
$$

$$
E = \frac{9B_{VRH}G_{VRH}}{(3B_{VRH} + G_{VRH})}, \tag{9}
$$

$$
\nu = \frac{(3B_{VRH} - 2G_{VRH})}{\left[2(3B_{VRH} + G_{VRH})\right]}. \tag{10}
$$

Here, $G_V$ ($B_V$), $G_R$ ($B_R$) and $G_{VRH}$ ($B_{VRH}$) are the shear (bulk) modulus calculated by Voigt, Reuss and Voigt-Reuss-Hill approximation, respectively, $E$ is the Young's modulus, and $\nu$ is the Poisson's ratio. Our calculated $B_{VRH}$, $G_{VRH}$ and $E$ for ideal $Gd_2Zr_2O_7$ together with available theoretical and experimental results [42,46-48] are summarized in Table 4. For $Gd_2Zr_2O_7$, our calculated results are $B_{VRH}$=163.4 Gpa, $G_{VRH}$=85.7 Gpa, $E$=218.8 Gpa. In the literature, Lan et al. employed a similar calculational method and determined the elastic moduli of $Gd_2Zr_2O_7$ to be 165, 88 and 224 Gpa for $B$, $G$ and $E$ [42], respectively, which are comparable with our results. Experimentally, Shimamura et al. reported similar results, i.e., $B$=174 Gpa, $G$=92 Gpa and $E$=236 Gpa [48]. Our results are not in great agreement with the experimental data, which mainly results from the different methods between our study and experimental work. In our study, the elastic moduli are calculated by employing Voigt-Reuss-Hill approximation. Experimentally, Shimamura and co-workers carried out ultrasound pulse-echo measurements to estimate the elastic moduli of $Gd_2Zr_2O_7$, i.e., the elastic moduli were determined from the longitudinal and transverse ultrasound sound velocities [48].

<table><caption>Table 6
The bulk modulus $B_{VRH}$ (GPa), shear modulus $G_{VRH}$ (GPa), Young's modulus $E$ (GPa) for ideal and defective $Gd_2Zr_2O_7$ (GZO), along with the relative change of the bulk modulus ($\Delta B_{VRH}$), shear modulus ($\Delta G_{VRH}$) and Young's modulus ($\Delta E$). $V_{O48f}$: $O_{48f}$ vacancy; $Zr_{Gd}$: Zr occupying the Gd lattice site; $Gd_{int2}$: Gd interstitial occupying the int2 (0.5, 0.625, 0.625); $Zr_{8a}$: Zr interstitial occupying the 8a site; $O_{8a}$: O interstitial occupying the 8a site.</caption>
<thead>
  <tr>
    <th></th>
    <th>Ideal GZO</th>
    <th colspan="5">Defective GZO</th>
  </tr>
  <tr>
    <th></th>
    <th></th>
    <th>$V_{O48f}$</th>
    <th>$Zr_{Gd}$</th>
    <th>$Gd_{int2}$</th>
    <th>$Zr_{8a}$</th>
    <th>$O_{8a}$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>$B_{VRH}$</td>
    <td>163.4</td>
    <td>162.1</td>
    <td>167.5</td>
    <td>152.7</td>
    <td>159.3</td>
    <td>165.5</td>
  </tr>
  <tr>
    <td>$\Delta B_{VRH}$ (%)</td>
    <td></td>
    <td>-0.8</td>
    <td>2.5</td>
    <td>-6.5</td>
    <td>-2.5</td>
    <td>1.3</td>
  </tr>
  <tr>
    <td>$G_{VRH}$</td>
    <td>85.7</td>
    <td>80.1</td>
    <td>83.1</td>
    <td>64.8</td>
    <td>55.2</td>
    <td>77.2</td>
  </tr>
  <tr>
    <td>$\Delta G_{VRH}$ (%)</td>
    <td></td>
    <td>-6.5</td>
    <td>-3.0</td>
    <td>-24.4</td>
    <td>-35.6</td>
    <td>-9.9</td>
  </tr>
  <tr>
    <td>$E$</td>
    <td>218.8</td>
    <td>206.2</td>
    <td>213.9</td>
    <td>170.4</td>
    <td>148.6</td>
    <td>200.5</td>
  </tr>
  <tr>
    <td>$\Delta E$ (%)</td>
    <td></td>
    <td>-5.8</td>
    <td>-2.2</td>
    <td>-22.1</td>
    <td>-32.1</td>
    <td>-8.4</td>
  </tr>
</tbody>
</table>

![](./images/812579376133570561_4.jpg)

Fig. 4. The calculated elastic moduli for ideal and defective $Gd_2Zr_2O_7$. $V_{O48f}$: $O_{48f}$ vacancy; $Zr_{Gd}$: Zr occupying the Gd lattice site; $Gd_{int2}$: Gd interstitial occupying the int2 (0.5, 0.625, 0.625); $Zr_{8a}$: Zr interstitial occupying the 8a site; $O_{8a}$: O interstitial occupying the 8a site.

The elastic moduli for defective $Gd_2Zr_2O_7$ are shown in Table 6, along with the relative change of respective elastic modulus. The most significant change is found for the $Zr_{8a}$ defect, for which the decreases are as large as 35.6 % for shear modulus and 32.1 % for Young's modulus. Another defect that influences the elastic moduli obviously is the $Gd_{int2}$ defect, for which the shear modulus of 64.8 Gpa and Young's modulus of 170.4 Gpa are remarkably smaller than the respective values of 85.7 Gpa and 218.8 Gpa for the ideal state. The bulk modulus is also decreased by 6.5 % by the presence of $Gd_{int2}$ defect. In the case of $O_{48f}$ vacancy and $O_{8a}$ interstitial defects, they cause the shear and Young's modulus to decrease by 6.5-9.9 % and 5.8-8.4 %, respectively. As for the $Zr_{Gd}$ antisite defect, the influences on the elastic moduli are much smaller. The variation of the elastic moduli for the ideal and defective $Gd_2Zr_2O_7$ is illustrated in Fig. 4. It is noted that the effect of point defects on the bulk modulus is relatively slight. As for the shear and Young's modulus, the most significant changes are found for $Gd_2Zr_2O_7$ with $Zr_{8a}$ interstitial defect. The total stiffness of $Gd_2Zr_2O_7$ pyrochlore is mainly dependent on the strength of &lt;Zr-O&gt; bonds, because the corner-sharing $ZrO_6$ octahedra constitutes its backbone, and the $Gd^{3+}$ fills the interstices. As $Zr_{8a}$ defect is introduced into $Gd_2Zr_2O_7$, the average &lt;Zr-O&gt; bond length is decreased, and the bonding interaction becomes stronger. Consequently, the $Zr_{8a}$ defect affects the elastic moduli significantly.

<table>
<caption>Table 7
The Pugh's indicator ($B_{VRH}/G_{VRH}$) and Poisson's ratio ($\nu$) for ideal and defective $Gd_2Zr_2O_7$ (GZO). $V_{O48f}$: $O_{48f}$ vacancy; $Zr_{Gd}$: Zr occupying the Gd lattice site; $Gd_{int2}$: Gd interstitial occupying the int2 (0.5, 0.625, 0.625); $Zr_{8a}$: Zr interstitial occupying the 8a site; $O_{8a}$: O interstitial occupying the 8a site.</caption>
<thead>
<tr>
<th rowspan="2"></th>
<th rowspan="2"></th>
<th>Ideal GZO</th>
<th colspan="5">Defective GZO</th>
</tr>
<tr>
<th></th>
<th>$V_{O48f}$</th>
<th>$Zr_{Gd}$</th>
<th>$Gd_{int2}$</th>
<th>$Zr_{8a}$</th>
<th>$O_{8a}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>$B_{VRH}/G_{VRH}$</td>
<td>Our Cal.</td>
<td>1.907</td>
<td>2.024</td>
<td>2.016</td>
<td>2.356</td>
<td>2.886</td>
<td>2.144</td>
</tr>
<tr>
<td></td>
<td>Other Cal.</td>
<td>2.004 [52]</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td>Exp.</td>
<td>1.913 [46,47]</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>1.891 [48]</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>$\nu$</td>
<td>Our Cal.</td>
<td>0.277</td>
<td>0.287</td>
<td>0.287</td>
<td>0.315</td>
<td>0.346</td>
<td>0.299</td>
</tr>
<tr>
<td></td>
<td>Other Cal.</td>
<td>0.276 [46,47]</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>0.274 [48]</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td>Exp.</td>
<td>0.286 [52]</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>0.273 [42]</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<caption>Table 8
The average sound wave velocity $\nu_m$ (m/s), Debye temperature $\theta_D$ (K) for ideal and defective $Gd_2Zr_2O_7$ (GZO). $V_{O48f}$: $O_{48f}$ vacancy; $Zr_{Gd}$: Zr occupying the Gd lattice site; $Gd_{int2}$: Gd interstitial occupying the int2 (0.5, 0.625, 0.625); $Zr_{8a}$: Zr interstitial occupying the 8a site; $O_{8a}$: O interstitial occupying the 8a site.</caption>
<thead>
<tr>
<th rowspan="2"></th>
<th rowspan="2"></th>
<th>Ideal GZO</th>
<th colspan="5">Defective GZO</th>
</tr>
<tr>
<th></th>
<th>$V_{O48f}$</th>
<th>$Zr_{Gd}$</th>
<th>$Gd_{int2}$</th>
<th>$Zr_{8a}$</th>
<th>$O_{8a}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>$\nu_m$</td>
<td>Our Cal.</td>
<td>4666.0</td>
<td>4556.0</td>
<td>4643.9</td>
<td>4087.9</td>
<td>3850.1</td>
<td>4476.9</td>
</tr>
<tr>
<td></td>
<td>Other Cal.</td>
<td>4833.5 [52]</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>$\theta_D$</td>
<td>Our Cal.</td>
<td>580.2</td>
<td>564.4</td>
<td>579.1</td>
<td>508.9</td>
<td>479.3</td>
<td>558.8</td>
</tr>
<tr>
<td></td>
<td>Other Cal.</td>
<td>612.9 [52]</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td>Exp.</td>
<td>513.3 [47]</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Generally, a small bulk or Young's modulus is beneficial for the elastic compliance. For example, a small Young's modulus may produce small residual stresses in the coating system under working conditions, thus resulting in better thermo-physical stability [49,50]. These results suggest that the $Gd_2Zr_2O_7$ with the presence of $Zr_{8a}$ defect may have better elastic compliance and thermo-physical stability than ideal $Gd_2Zr_2O_7$.

### 3.4. Ductility and Poisson's ratio of ideal and defective $Gd_2Zr_2O_7$

Pugh has proposed that the ratio of $B_{VRH}/G_{VRH}$ can be used to empirically predict the ductility of material [51]. The critical value which separates ductile and brittle materials is around 1.75, i.e., if $B_{VRH}/G_{VRH}$ ratio is smaller than 1.75, the material demonstrates brittleness; otherwise, it behaves in a ductile manner [51]. The calculated $B_{VRH}/G_{VRH}$ ratio for the ideal and defective $Gd_2Zr_2O_7$ are presented in Table 7. The $B_{VRH}/G_{VRH}$ ratio of 1.907 for $Gd_2Zr_2O_7$ is comparable with the theoretical value of 2.004 reported by Zhang et al. [52], and the experimental values of 1.913 and 1.891 [46-48]. It is noted that the $B_{VRH}/G_{VRH}$ ratios for defective $Gd_2Zr_2O_7$ are generally lager than the value of 1.907. Especially, the $Gd_{int2}$ and $Zr_{8a}$ interstitial defects increase the $B_{VRH}/G_{VRH}$ ratios by 23.5 % and 51.3 %, respectively. These results indicate that the introduction of point defects in $Gd_2Zr_2O_7$ can enhance its ductility.

The Poisson's indicator ($\nu$) can also be employed to evaluate the relative ductility of materials [53]. When $\nu$ is around 0.1, the material shows brittle properties; as $\nu$ is larger than 0.25, it exhibits ductile properties. As shown in Table 7, the calculated Poisson's ratio of 0.277 is in good agreement with the experimental and other calculated results [42,46-48,52]. As compared with the value of 0.277 for ideal $Gd_2Zr_2O_7$, the Poisson's ratios for $Gd_2Zr_2O_7$ with point defects are generally larger, i.e., the defective states are more ductile than the pure $Gd_2Zr_2O_7$. This is consistent with the results of Pugh's indicator.

### 3.5. Debye temperature of ideal and defective $Gd_2Zr_2O_7$

The Debye temperature, which relates to the hardness and thermal expansion coefficient of a material, can be calculated by the following form [54]:

$$
\theta_{D}=\frac{h}{k}\left[\frac{3 n}{4 \pi}\left(\frac{N_{A} \rho}{M}\right)\right]^{\frac{1}{3}} \nu_{m}, \tag{11}
$$

where $\theta_D$ is the Debye temperature, $h$ and $k$ are the Planck's and Boltzmann's constant, respectively, $n$ is the number of atoms per unit cell, $N_A$ is the Avogadro's number, $M$ is the unit-cell molecular weight and $\rho$ is the density, and $\nu_m$ is the average sound wave velocity. The $\nu_m$ is calculated using $\nu_m=\left[\frac{1}{3}\left(\frac{2}{\nu_{s}^{3}}+\frac{1}{\nu_{l}^{3}}\right)\right]^{-\frac{1}{3}}$, in which $\nu_s$ is the transverse sound wave velocity and $\nu_l$ is the longitudinal sound wave velocity [54]. The $\nu_s$ and $\nu_l$ can be obtained by the following empirical formula [54], i.e., $\nu_s=\sqrt{G/\rho}$ and $\nu_l=\sqrt{(B+4/3G)/\rho}$. The calculated average sound wave velocity and Debye temperature for pristine and defective $Gd_2Zr_2O_7$ are shown in Table 8, together with the experimental and theoretical results [48,52]. The average sound velocity for ideal $Gd_2Zr_2O_7$ is 4666.0 m/s, which is comparable with other calculated value of 4833.5 m/s [52]. It is noted that the negative effects of $Gd_{int2}$ and $Zr_{8a}$ interstitial defects on the average sound wave velocity are the most pronounced, as indicated by the decrease of velocity from 4666.0 to 4087.9 m/s and 3850.1 m/s, respectively. For ideal $Gd_2Zr_2O_7$, the Debye temperature is determined to be 580.2 K, which is consistent with other calculated result of 612.9 K [52] and larger than the experimental result of 513.3 K [48]. It is noticeable that the presence of point defects generally decreases the Debye temperature except the $Zr_{Gd}$ antisite defect. In particular, the $Gd_{int2}$ and $Zr_{8a}$ interstitial defects cause reduction of 71.3 and 100.9 K in the Debye temperature, respectively. Generally, the material with lower Debye temperature has weaker interatomic binding force and larger thermal expansion coefficient. Since the introduction of point defects results in generally smaller Debye temperature in $Gd_2Zr_2O_7$, it is suggested that the defective $Gd_2Zr_2O_7$ will have larger thermal expansion coefficient than the pristine state.

### 4. Conclusion

In this work, a density functional theory study is performed to compare the mechanical and thermal properties of pure and defec-

tive $Gd_2Zr_2O_7$. The calculated defect formation energies show that the $V_{O4f}$, $Zr_{Gd}$, $Gd_{int2}$, $Zr_{8a}$ and $O_{8a}$ defects are favorable under ir- radiation. Besides, the $Gd_2Zr_2O_7$ with point defects remain ordered pyrochlore structure and are mechanically stable. Further calcula- tions show that the effects of point defects on the elastic moduli, especially shear modulus and Young's modulus, are generally large. The Pugh's indicator and Poisson's indicator suggest that the defec- tive states are more ductile than the pure $Gd_2Zr_2O_7$. On the other hand, the presence of point defects generally decreases the Debye temperature except the $Zr_{Gd}$ antisite defect. These results suggest that the $Gd_2Zr_2O_7$ with point defects have better elastic compli- ance, better ductility, as well as larger thermal expansion coeffi- cient than pure $Gd_2Zr_2O_7$.

## Declaration of Competing Interest
The authors declare that they have no known competing finan- cial interests or personal relationships that could have appeared to influence the work reported in this paper.

## CRediT authorship contribution statement
Menglu Li: Methodology, Investigation, Writing - original draft.
Pengcheng Li: Investigation, Writing - review & editing.
Haiyan Xiao: Software, Supervision, Writing - review & editing.
Haibin Zhang: Writing - review & editing.
Xiaotao Zu: Supervision, Writ- ing - review & editing.

## Acknowledgement
H.Y. Xiao was supported by the NSAF Joint Foundation of China (Grant No.U1930120). The theoretical calculations are performed using the supercomputer resources at TianHe-1 located at National Supercomputer Center in Tianjin.

## Supplementary materials
Supplementary material associated with this article can be found, in the online version, at doi:10.1016/j.jnucmat.2020.152425.

## References
[1] R. Vassen, X.Q. Cao, F. Tietz, D. Basu, D. Stover, Zirconates as new materials for thermal barrier coatings, J. Am. Ceram. Soc. 83 (8) (2000) 2023-2028.
[2] G. Suresh, G. Seenivasan, M.V. Krishnaiah, P.S. Murti, Investigation of the ther- mal conductivity of selected compounds of gadolinium and lanthanum, J. Nu- clear Mater. 249 (2-3) (1997) 259-261.
[3] R.C. Ewing, W.J. Weber, J. Lian, Nuclear waste disposal-pyrochlore $(A_2B_2O_7)$: Nuclear waste form for the immobilization of plutonium and "minor" ac- tinides, J. Appl. Phys. 95 (11) (2004) 5949-5971.
[4] B.P. Mandal, M. Pandey, A.K. Tyagi, $Gd_2Zr_2O_7$ pyrochlore Potential host matrix for some constituents of thoria based reactor's waste, J. Nuclear Materi. 406 (2) (2010) 238-243.
[5] S.S. Shoup, C.E. Bamberger, R.G. Haire, Novel plutonium titanate compounds and solid solutions $Pu_2Ti_2O_7-Ln_2Ti_2O_7$: Relevance to nuclear waste disposal, J. Am. Ceram. Soc. 79 (6) (1996) 1489-1493.
[6] S.X. Wang, B.D. Begg, L.M. Wang, R.C. Ewing, W.J. Weber, K.V.G. Kutty, Radia- tion stability of gadolinium zirconate: a waste form for plutonium disposition, J. Mater. Res. 14 (12) (1999) 4470-4473.
[7] K.V.G. Kutty, R. Asuvathraman, R.R. Madhavan, H. Jena, Actinide immobiliza- tion in crystalline matrix: a study of uranium incorporation in gadolinium zir- conate, J. Phys. Chem. Solids 66 (4) (2005) 596-601.
[8] C. Nastren, R. Jardin, J. Somers, M. Walter, B. Brendebach, Actinide incorpora- tion in a zirconia based pyrochlore $Nd_{1.8}An_{0.2}Zr_2O_{7+x}$ (An = Th, U, Np, Pu, Am), J. Solid State Chem 182 (1) (2009) 1-7.
[9] G. Sattonnay, L. Thome, N. Sellami, I. Monnet, C. Grygiel, C. Legros, R. Tetot, Experimental approach and atomistic simulations to investigate the radiation tolerance of complex oxides: application to the amorphization of pyrochlores, Nucl. Instrum. Methods Phys. Res. Sect. B Beam Interact. Mater. Atoms. 326 (2014) 228-233.
[10] M. Lang, F.X. Zhang, R.C. Ewing, J. Lian, C. Trautmann, Z.W. Wang, Structural modifications of $Gd_2Zr_{2-x}Ti_xO_7$ pyrochlore induced by swift heavy ions: Disor- dering and amorphization, J. Mater. Res. 24 (4) (2009) 1322-1334.
[11] M. Lang, J. Lian, J.M. Zhang, F.X. Zhang, W.J. Weber, C. Trautmann, R.C. Ewing, Single-ion tracks in $Gd_2Zr_{2-x}Ti_xO_7$ pyrochlores irradiated with swift heavy ions, Phys. Rev. B 79 (22) (2009) 9.
[12] M.K. Patel, V. Vijayakumar, S. Kailas, D.K. Avasthi, J.C. Pivin, A.K. Tyagi, Struc- tural modifications in pyrochlores caused by ions in the electronic stopping regime, J. Nuclear Mater. 380 (1-3) (2008) 93-98.
[13] M.K. Patel, V. Vijayakumar, D.K. Avasthi, S. Kailas, J.C. Pivin, V. Grover, B.P. Man- dal, A.K. Tyagie, Effect of swift heavy ion irradiation in pyrochlores, Nucl. In- strum. Methods Phys. Res. Sect. B Beam Interact. Mater. Atoms. 266 (12-13) (2008) 2898-2901.
[14] D.S.D. Gunn, N.L. Allan, H. Foxhall, J.H. Harding, J.A. Purton, W. Smith, M.J. Stein, I.T. Todorov, K.P. Travis, Novel potentials for modelling defect for- mation and oxygen vacancy migration in $Gd_2Ti_2O_7$ and $Gd_2Zr_2O_7$ pyrochlores, J. Mater. Chem. 22 (11) (2012) 4675-4680.
[15] J.A. Purton, N.L. Allan, Displacement cascades in $Gd_2Ti_2O_7$ and $Gd_2Zr_2O_7$: a molecular dynamics study, J. Mater. Chem. 12 (10) (2002) 2923-2926.
[16] R.E. Williford, W.J. Weber, R. Devanathan, J.D. Gale, Effects of cation disor- der on oxygen vacancy migration in $Gd_2Ti_2O_7$, J. Electroceram 3 (4) (1999) 409-424.
[17] P.J. Wilde, C.R.A. Catlow, Defects and diffusion in pyrochlore structured oxides, Solid State Ion 112 (3-4) (1998) 173-183.
[18] J.W. Wang, F.X. Zhang, J. Lian, R.C. Ewing, U. Becker, Energetics and concen- tration of defects in $Gd_2Ti_2O_7$ and $Gd_2Zr_2O_7$ pyrochlore at high pressure, Acta Mater. 59 (4) (2011) 1607-1618.
[19] G. Sattonnay, R. Tetot, Atomic scale simulations of pyrochlore oxides with a tight-binding variable-charge model: implications for radiation tolerance, J. Phys. Condes. Matter 26 (5) (2014) 10.
[20] L. Minervini, R.W. Grimes, K.E. Sickafus, Disorder in pyrochlore oxides, J. Am. Ceram. Soc. 83 (8) (2000) 1873-1878.
[21] K.E. Sickafus, L. Minervini, R.W. Grimes, J.A. Valdez, M. Ishimaru, F. Li, K.J. Mc- Clellan, T. Hartmann, Radiation tolerance of complex oxides, Science 289 (5480) (2000) 748-751.
[22] C.L. Wan, W. Pan, Q. Xu, Y.X. Qin, J.D. Wang, Z.X. Qu, M.H. Fang, Effect of point defects on the thermal transport properties of $(La_xGd_{1-x})_2Zr_2O_7$: experiment and theoretical model, Phys. Rev. B 74 (14) (2006) 9.
[23] F.A. Zhao, H.Y. Xiao, M. Bai, Z.J. Liu, X.T. Zu, Effects of Nd doping on the mechanical properties and electronic structures of $Gd_2Zr_2O_7$: a first-princi- ples-based study, J. Mater. Sci. 53 (24) (2018) 16423-16438.
[24] P.E. Blochl, Projector augmented-wave method, Phys. Rev. B 50 (24) (1994) 17953-17979.
[25] G. Kresse, J. Furthmuller, Efficient iterative schemes for ab initio total-en- ergy calculations using a plane-wave basis set, Phys. Rev. B 54 (16) (1996) 11169-11186.
[26] G. Kresse, D. Joubert, From ultrasoft pseudopotentials to the projector aug- mented-wave method, Phys. Rev. B 59 (3) (1999) 1758-1775.
[27] S.L. Dudarev, G.A. Botton, S.Y. Savrasov, C.J. Humphreys, A.P. Sutton, Elec- tron-energy-loss spectra and the structural stability of nickel oxide: An LSDA+U study, Phys. Rev. B 57 (3) (1998) 1505-1509.
[28] M. Alaydrus, M. Sakaue, H. Kasai, A DFT plus U study on the contribution of 4f electrons to oxygen vacancy formation and migration in Ln-doped $CeO_2$, Phys. Chem. Chem. Phys. 18 (18) (2016) 12938-12946.
[29] X.J. Wang, H.Y. Xiao, X.T. Zu, Y. Zhang, W.J. Weber, Ab initio molecular dynam- ics simulations of ion-solid interactions in $Gd_2Zr_2O_7$ and $Gd_2Ti_2O_7$, J. Mater. Chem. C 1 (8) (2013) 1665-1673.
[30] R. Devanathan, W.J. Weber, Insights into the radiation response of pyrochlores from calculations of threshold displacement events, J. Appl. Phys. 98 (8) (2005) 3.
[31] M. Freyss, First-principles study of uranium carbide: Accommodation of point defects and of helium, xenon, and oxygen impurities, Phys. Rev. B 81 (1) (2010).
[32] H.Y. Xiao, F. Gao, W.J. Weber, Threshold displacement energies and defect for- mation energies in $Y_2Ti_2O_7$, J. Phys. Condes. Matter 22 (41) (2010).
[33] A. Chartier, C. Meis, W.J. Weber, L.R. Corrales, Theoretical study of disorder in Ti-substituted $La_2Zr_2O_7$, Phys. Rev. B 65 (13) (2002).
[34] H.Y. Xiao, F. Gao, W.J. Weber, Threshold displacement energies and defect for- mation energies in $Y_2Ti_2O_7$, J. Phys. Condes. Matter 22 (41) (2010) 9.
[35] X.J. Wang, H.Y. Xiao, X.T. Zu, W.J. Weber, Study of cerium solubility in $Gd_2Zr_2O_7$ by DFT + U calculations, J. Nuclear Mater. 419 (1-3) (2011) 105-111.
[36] B.P. Mandal, A. Banerji, V. Sathe, S.K. Deb, A.K. Tyagi, Order-disorder transition in $Nd_{2-y}Gd_yZr_2O_7$ pyrochlore solid solution: An X-ray diffraction and Raman spectroscopic study, J. Solid State Chem. 180 (10) (2007) 2643-2648.
[37] J. Chen, J. Lian, L.M. Wang, R.C. Ewing, R.G. Wang, W. Pan, X-ray photoelectron spectroscopy study of disordering in $Gd_2(Ti_{1-x}Zr_x)_2O_7$ pyrochlores, Phys. Rev. Lett. 88 (10) (2002).
[38] R. Shannon, Revised effective ionic radii and systematic studies of interatomic distances in halides and chalcogenides, Acta Crystallographica Section A 32 (5) (1976) 751-767.
[39] F.A. Zhao, H.Y. Xiao, M. Jiang, Z.J. Liu, X.T. Zu, A DFT plus U study of Pu immo- bilization in $Gd_2Zr_2O_7$, J. Nuclear Mater. 467 (2015) 937-948.
[40] J. Lian, X.T. Zu, K.V.G. Kutty, J. Chen, L.M. Wang, R.C. Ewing, Ion-irradiation-in- duced amorphization of $La_2Zr_2O_7$ pyrochlore, Phys. Rev. B 66 (5) (2002).
[41] J.H. Wang, S. Yip, S.R. Phillpot, D. Wolf, CRYSTAL INSTABILITIES AT FINITE STRAIN, Phys. Rev. Lett. 71 (25) (1993) 4182-4185.
[42] G.Q. Lan, B. Ouyang, J. Song, The role of low-lying optical phonons in lattice thermal conductance of rare-earth pyrochlores: a first-principle study, Acta Mater. 91 (2015) 304-317.

[43] A. Reuss, Z. Angew, Berechnung der Fließgrenze von Mischkristallen auf Grund der Plastizitatsbedingung für Einkristalle, Math Phys 9 (1929) 49.

[44] R. Hill, The elastic behaviour of a crystalline aggregate, Proc. Phys. Soc. A 65 (1952) 349.

[45] W. Voigt, Über die Beziehung zwischen den beiden Elasticitätsconstanten isotroper Körper, Ann. Phys. 274 (1889) 573.

[46] M.P. van Dijk, K.J. de Vries, A.J. Burggraaf, Oxygen ion and mixed conductiv- ity in compounds with the fluorite and pyrochlore structure, Solid State Ion 9 (1983) 913.

[47] J. Wu, X.Z. Wei, N.P. Padture, P.G. Klemens, M. Gell, E. Garcia, P. Miranzo, M.I. Osendi, Low-thermal-conductivity rare-earth zirconates for potential ther- mal-barrier-coating applications, J. Am. Ceram. Soc. 85 (12) (2002) 3031–3035.

[48] K. Shimamura, T. Arima, K. Idemitsu, Y. Inagaki, Thermophysical properties of rare-earth-stabilized zirconia and zirconate pyrochlores as surrogates for ac- tinide-doped zirconia, Int. J. Thermophys. 28 (3) (2007) 1074–1084.

[49] F.A. Zhao, H.Y. Xiao, Z.J. Liu, S. Li, X.T. Zu, A DFT study of mechanical prop- erties, thermal conductivity and electronic structures of Th-doped $Gd_2Zr_2O_7$, Acta Mater. 121 (2016) 299–309.

[50] P.K. Schelling, S.R. Phillpot, R.W. Grimes, Optimum pyrochlore compositions for low thermal conductivity, Philos. Mag. Lett. 84 (2) (2004) 127–137.

[51] S.F.X. Pugh, Relations between the elastic moduli and the plastic properties of polycrystalline pure metals, Te London, Edinburgh, and Dublin Philos. Mag. J. Sci. 45 (1954) 823.

[52] S. Zhang, H.B. Zhang, F.A. Zhao, M. Jiang, H.Y. Xiao, Z.J. Liu, X.T. Zu, Impact of isovalent and aliovalent substitution on the mechanical and thermal properties of $Gd_2Zr_2O_7$, Sci. Rep. 7 (2017).

[53] M.E. Fine, L.D. Brown, H.L. Marcus, Elastic constants versus melting tempera- ture in metals, Scr. Metallur. 18 (1984) 951.

[54] J. Feng, B. Xiao, C.L. Wan, Z.X. Qu, Z.C. Huang, J.C. Chen, R. Zhou, W. Pan, Elec- tronic structure, mechanical properties and thermal conductivity of $Ln_2Zr_2O_7$ (Ln = La, Pr, Nd, Sm, Eu and Gd) pyrochlore, Acta Mater. 59 (4) (2011) 1742–1760.

[55] F.X. Zhang, J. Lian, U. Becker, R.C. Ewing, J.Z. Hu, S.K. Saxena, High-pressure structural changes in the $Gd_2Zr_2O_7$ pyrochlore, Phys. Rev. B 76 (21) (2007) 5.

[56] A.J.B.M.P. van DIJK, Defect structures and migration mechanisms in oxide py- rochlore, Solid State Ion. 17 (1985) 159–167.

[57] N.R. Sanjay Kumar, N.V. Chandra Shekar, P.C. Sahu, Pressure induced structural transformation of pyrochlore $Gd_2Zr_2O_7$, Solid State Commun. 147 (9-10) (2008) 357–359.

[58] S. Surblé, S. Heathman, P.E. Raison, D. Bouëxière, K. Popa, R. Caciuffo, Pres- sure-induced structural transition in $Ln_2Zr_2O_7$ (Ln = Ce, Nd, Gd) pyrochlores, Phys. Chem. Miner. 37 (10) (2010) 761–767.

[59] S. Solomon, A. George, J.K. Thomas, A. John, Preparation, characterization, and ionic transport properties of nanoscale $Ln_2Zr_2O_7$ (Ln = Ce, Pr, Nd, Sm, Gd, Dy, Er, and Yb) energy materials, J. Electron. Mater. 44 (1) (2014) 28–37.
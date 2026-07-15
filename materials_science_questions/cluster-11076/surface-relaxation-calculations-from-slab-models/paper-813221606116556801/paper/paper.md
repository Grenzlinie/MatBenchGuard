# SrTiO₃ (001) surface and strained thin films: Atomic simulations using a tight-binding variable-charge model

R. Tétot *, N. Salles, S. Landron, E. Amzallag

ICMMO (LEMHE), UMR 8182 CNRS-Univ. Paris-Sud 11, Bât 410, F91405 Orsay Cedex, France

---

## ARTICLE INFO

Article history:
Received 12 December 2012
Accepted 22 May 2013
Available online 30 May 2013

Keywords:
Strontium titanate
Surface energy
Surface relaxation
Strained thin films
Variable-charge model
Density functional calculations

## ABSTRACT

The tight-binding variable-charge model SMTB-Q was used to study the properties of the (001) surfaces and ultra-thin films of the SrTiO₃ perovskite. First, the bulk properties of SrTiO₃ were successfully reproduced from a set of parameters independently determined for bulk SrO and TiO₂. The formation energies, atomic relaxations and charge transfer for SrO- and TiO₂-terminated SrTiO₃ (001) surfaces were then derived from 0 to 1200 K. The TiO₂-terminated surface is more stable than the SrO-terminated surface by about 0.15 j m⁻² under 500 K. This difference decreases by a factor 3 at higher temperature. At 0 K, the surface energies ($E_{TiO2}=1.10$ j m⁻² and $E_{SrO}=1.20$ j m⁻²) are in accordance with the mean value yielded by ab initio calculations. A strong Sr displacement towards the SrO-terminated surface (0.33 Å) was observed in agreement with both experimental data and DFT calculations. In contrast, the other atomic relaxations included the Ti displacement towards the TiO₂-terminated surface (0.13 Å), are in good agreement with ab initio results but strongly differ from experimental data ($\approx$0.00 Å). The displacements of surface oxygen planes being small, one observes a splitting of the SrO and TiO₂ surface planes by 0.30 and 0.13 Å respectively. Moreover, the distance between the Sr and Ti planes is reduced by 19%. The charge transfers at the TiO₂-terminated surface are comparable to those at the pure TiO₂ surfaces ($-$0.18 and +0.14, for titanium and oxygen atoms respectively) leading to the increase of the Ti-O bond covalency near the surface. At the SrO-terminated surface, we found negligible charge transfers as at the pure SrO(100) surface. Moreover, we studied the effect of a 1.66% compressive strain (corresponding to the STO/Si(001) lattice mismatch) on the relaxation of thin films from 2 to 40 nm at 273 K. The atomic surface relaxations are not significantly modified apart from the Sr-Ti (resp. Ti-Sr) distances which relaxed by 25%. The ratio between out-of-plane and in-plane lattice parameters is in good agreement with the elasticity theory for a thickness up to 5 nm. Beyond 20 nm thick the film is almost fully relaxed.

© 2013 Elsevier B.V. All rights reserved.

---

## 1. Introduction

The SrTiO₃ (STO) surfaces, like TiO₂ surfaces, constitute a model system in the surface science of metal oxides [1] and a very important system for technological applications. Thin STO films play a major role in electronic devices and related applications due to their desirable properties, such as high dielectric constant and chemical stability; consequently when deposited on silicon they are frequently used as the substrate material for high Tc superconducting films [2,3]. Therefore, many experimental and theoretical studies have been focused on STO surfaces. Particularly, the structure of the STO(001) surface, which can terminate in either SrO or TiO₂ planes, has been investigated by means of low-energy electron diffraction (LEED) [4], medium-energy ion scattering (MRIS) [5] and surface X-ray diffraction [6,7]. Concurrently, theoretical studies have been performed, from first-principles with different methods and Hamiltonians: density functional theory (DFT) with the local density approximation (LDA) [8-10], the generalized gradient approximation (GGA) [11], hybrid DFT [12], full-potential linear muffin-tin orbital method (FP-LMTO) [13] and from empirical shell-model [14,15]. Here, the STO(001) surface structure was studied by means of a recent variable-charge model, the so-called SMTB-Q model (Second-Moment Tight-Binding QEq) [16,17], based on a quantum description of oxides proposed by Goniakovski and Noguera [18,19]. The equilibrium charges are determined by a self consistent charge equilibration following the QEq approach [20]. The QEq formalism allows charges to vary in response to changes in the local environment of ions, which is a real progress compared with the fixed-charge shell-model. Note that it is the first time, to our knowledge, that variable-charge simulations are performed for such complex oxide. Moreover, in the SMTB-Q model, the iono-covalent metal-oxygen bond is described by means of the tight-binding formalism which takes into account the electronic structure of the oxide, in contrast to other variable-charge models [21-24]. In this approach, the covalent energy is a function of the ionic charges, which results in a great stability of the model with respect to charge transfers. This is particularly crucial when the crystal is submitted to strain or to the lack of periodicity in one direction by the presence of a surface. The parameters of the model are determined independently

* Corresponding author. Tel.: +33 6 71 95 25 08.
E-mail address: Robert.tetot@u-psud.fr (R. Tétot.)

0039-6028/$ - see front matter © 2013 Elsevier B.V. All rights reserved.
http://dx.doi.org/10.1016/j.susc.2013.05.015

for the two binary oxides SrO and TiO₂ and then are used to derive bulk and surface properties of STO after a small correction, taking advantage of the transferability of the SMTB-Q model. Moreover, the effect of strain on thin films from 2 to 40 nm-thick was studied at 273 K. More precisely we applied a 1.66% compressive strain parallel to the (001) surface which corresponds to the lattice mismatch between STO and Si(001) in assuming that the silicon substrate imposes a clamping effect to the STO film deposited on it.

The paper is organized as follows. In Section 2, the SMTB-Q model is shortly described (Section 2.1) and the parameters of the model are determined for bulk SrO and TiO₂ (Section 2.2). In Section 2.3, the transferability of the model is discussed and the bulk properties of STO were derived. In Section 3, surface properties of SrO, TiO₂ and STO (energetic, atomic relaxations and charge transfer) are studied and the results are compared with ab initio calculations performed with the CRYSTAL06 code [25], and with experimental data when available. In Section 4, the effect of a strain on the relaxations of thin films is investigated. Section 5 contains our conclusions.

## 2. Bulk SrO, TiO₂ and SrTiO₃

### 2.1. The SMTB-Q model

In this model, the cohesive energy, \(E_{\text{coh}}\), of a simple binary oxide \(M_nO_m\) is the sum of four terms:
$$
E_{\text{coh}} = E_{\text{ion}} + E_{\text{coul}} + E_{\text{cov}} + E_{\text{rep}},
\tag{1}
$$
with:
$$
E_{\text{ion}} = \sum_A \left(E_A^0 + \chi_A^0 Q_A + \frac{1}{2} J_{AA}^0 Q_A^2\right)
\tag{2}
$$

$$
E_{\text{coul}} = \sum_A \sum_{B < A} Q_A Q_B J_{AB}
\tag{3}
$$

$$
E_{\text{cov}} = -\sum_{i(i\equiv M,O)} \left\{ \sum_{\substack{j(j\equiv O,M) \\ r_{ij} \leq r_c}} \xi_M^2 \exp\left[-2q_M\left(\frac{r_{ij}}{r_{OM}^0}-1\right)\right] \Delta Q_M \right\}^{1/2}
\tag{4}
$$

$$
\begin{aligned}
E_{\text{rep}} =& \sum_{\substack{i(i\equiv M,O) \\ r_{OM} \leq r_c}} \sum_{\substack{j(j\equiv O,M)}} A_M \exp\left[-p_M\left(\frac{r_{ij}}{r_{OM}^0}-1\right)\right] \ (\text{metal}-\text{oxygen pairs}) \\
& + \frac{1}{2} \sum_O \sum_{\substack{O,r_{OO} \leq r_c}} B \exp\left(\frac{r_{OO}}{\rho}\right) \ (\text{oxygen}-\text{oxygen pairs}).
\tag{5}
\end{aligned}
$$

\(E_{\text{ion}}\) (Eq. (2)) is the ionization energy developed up to the second order with respect to the charges \(Q_A\) on atom \(A\), \(E_A^0\) is the energy of the neutral atom and \(\chi_A^0\) and \(J_{AA}^0\) are the electronegativity and the hardness of the atom \(A\) respectively. \(E_{\text{coul}}\) (Eq. (3)) is the electrostatic energy. \(J_{AB}\) is the Coulomb interaction between the unit charges on centers \(A\) and \(B\). Following Rappé and Goddard [20], \(J_{AB}\) are Coulomb integrals between two single s-type Slater orbitals \(\rho_A(r)=N_n r^{n-1} e^{-(2n+1)/4R_A}\), where \(N_n\) is the normalization constant, \(n\) is the quantum number of the outer valence orbital and \(R_A\) is the covalent radius of atom \(A\) in the original QEq formulation [20]. In fact, the real significance of \(R_A\) is a little more complex in a solid, because it must depends both on the coordination number of the atom and on the interatomic distance and is then considered as an adjustable parameter. At short distance, the Coulomb interaction is shielded, leading to a decrease of the absolute value of the electrostatic energy compared with the one obtained with point-charge models. The expression of the covalent energy, \(E_{\text{cov}}\) (Eq. (4)), is derived from the quantum model developed by Noguera and Goniakowski [18,19], recalled in the Appendix A. This expression is obtained from Eq. (A5) by extending the covalent interaction over all neighbors of every atom (\(M\) or \(O\)) up to the second-moment cut-off radius \(r_c\) generally located between the 4th and 5th neighbors [27]. \(r_{OM}^0\) is the equilibrium first neighbor OM distance, \(\xi_M\) and \(q_M\) are adjustable parameters. Eq. (5) represents the short-range pair repulsion between ions. \(A_M, p_M, B\) and \(\rho\) are adjustable parameters. Cation-cation short-range interactions are neglected because the \(M\) outer orbitals are empty in an insulator. Note that the extension of Eqs. (1)–(5) to ternary systems is straightforward, Eq. (A6) that must be used at the place of Eq. (A5).

According to the QEq scheme [20], the equilibrium ionic charges in the crystal are those which minimize \(E_{\text{coh}}\) (more exactly, the part of \(E_{\text{coh}}\) which depends on the charges), and we obtain (see Appendix B):
$$
\left(\chi_O^0 - \chi_M^0\right) + J^{\Sigma} Q = 2m\beta\sqrt{Z_O} \frac{\left(n_{\text{cov}}-4+2Q\right)}{\sqrt{(2-Q)(n_{\text{cov}}-2+Q)}},
\tag{6}
$$
where the expression (A4) for \(E_{\text{cov}}\) were used for sake of simplicity of the writing (the use of Eq. (4) is straightforward). In contrast, in previous variable-charge models [21–24], the covalent energy does not depend on the charges, and the equilibrium oxygen charge is simply given by:
$$
Q = \frac{\left(\chi_M^0 - \chi_O^0\right)}{J^{\Sigma}}.
\tag{7}
$$

### 2.2. Parameters of the model for bulk SrO and TiO₂

For a particular oxide, the parameters of the model are adjusted in order to reproduce the lattice parameters, the cohesive energy and the elastic properties. These parameters can be separated into two groups. The first group, the QEq parameters, includes the electronegativity \(\chi_A^0\), the hardness \(J_{AA}^0\) (Eq. (2)) and the effective radius of the Slater orbitals, \(R_A\) of each species (\(A = M, O\)). \(\chi_O^0\) and \(J_{OO}^0\) are adjusted to electron affinity of oxygen. \(\chi_M^0\) and \(J_{MM}^0\) are adjustable parameters and must be reasonably compatible with the ionization energies of \(M\). The second group, the short-range (SR) parameters, includes \(\xi_M, q_M\) (Eq. (4)), \(A_M, p_M, B\) and \(\rho\) (Eq. (5)). The values of the two sets of parameters for SrO and TiO₂ are reported in Table 1. Note that oxygen parameters are the same in the two cases, apart \(R_O\) which slightly depends on \(Z_O\) (6 in SrO, 3 in TiO₂).

In Table 2, the calculated and experimental properties are compared. Lattice parameters, cohesive energies and bulk modulus are very well reproduced and the elastic constants fit satisfactorily, the maximum deviations being 36% for \(C_{12}\) of SrO and 22% for \(C_{33}\) of TiO₂. It is necessary, here, to emphasize a point. To select a set of parameters to describe some properties of a compound is always a compromise. There are several satisfactory sets of parameters (which are not very different from each other) according to the accuracy wanted on any particular

<table>
<caption>Table 1<br>Parameters of the SMTB-Q model for SrO and TiO₂. The second column of results is relative to this work and the third column to a previous work on TiO₂ [17].</caption>
<thead>
<tr>
<th></th>
<th>SrO</th>
<th>TiO₂</th>
<th>TiO₂ [17]</th>
</tr>
</thead>
<tbody>
<tr>
<td>\(\chi_O^0\) (eV)</td>
<td>6.57</td>
<td>6.57</td>
<td>7.543</td>
</tr>
<tr>
<td>\(J_{OO}^0\)(eV)</td>
<td>10.22</td>
<td>10.22</td>
<td>12.162</td>
</tr>
<tr>
<td>\(\chi_M^0\) (eV)</td>
<td>4.9</td>
<td>0.0</td>
<td>0.0</td>
</tr>
<tr>
<td>\(J_{MM}^0\) (eV)</td>
<td>3.56</td>
<td>10.572</td>
<td>10.572</td>
</tr>
<tr>
<td>\(R_O\) (Å)</td>
<td>0.52</td>
<td>0.543</td>
<td>0.617</td>
</tr>
<tr>
<td>\(R_M\) (Å)</td>
<td>0.767</td>
<td>0.734</td>
<td>0.6933</td>
</tr>
<tr>
<td>\(\xi_M\) (eV)</td>
<td>1.423</td>
<td>1.087</td>
<td>1.12</td>
</tr>
<tr>
<td>\(\beta\) (eV)</td>
<td>1.423</td>
<td>0.928</td>
<td>0.956</td>
</tr>
<tr>
<td>\(q_M\)</td>
<td>1.935</td>
<td>2.096</td>
<td>2.16</td>
</tr>
<tr>
<td>\(A_M\) (eV)</td>
<td>0.342</td>
<td>0.134</td>
<td>0.1</td>
</tr>
<tr>
<td>\(p_M\)</td>
<td>6.274</td>
<td>12.61</td>
<td>15.48</td>
</tr>
<tr>
<td>\(B\) (eV)</td>
<td>580.44</td>
<td>580.44</td>
<td>580.44</td>
</tr>
<tr>
<td>\(\rho\)</td>
<td>0.354</td>
<td>0.354</td>
<td>0.354</td>
</tr>
<tr>
<td>\(r_{OM}^0, r_c\) (Å)</td>
<td>2.58, 8.0</td>
<td>1.95, 6.0</td>
<td>1.95, 6.0</td>
</tr>
</tbody>
</table>

<table><caption>Table 2
Lattice parameters, cohesive energy, elastic properties, generalized coordination number of oxygen (see Eq. (25)), oxygen charge (absolute value), ionic factor $f_P$, $\delta=\varepsilon_M-\varepsilon_O$, and electronic gap $(E_G)$ calculated with the SMTB-Q model for SrO and $TiO_2$. The calculated values are compared with experimental data in brackets (references are also indicated). The second column of results is relative to this work and the third column to a previous work on $TiO_2$ [17].</caption>
<tbody><tr><td></td><td>SrO</td><td>TiO$_2$</td><td>TiO$_2$ [17]</td></tr>
<tr><td>$a$ (Å)</td><td>5.157 (5.160 [28])</td><td>4.594 (4.594 [31])</td><td>4.594</td></tr>
<tr><td>$c$ (Å)</td><td></td><td>2.9593 (2.9590 [31])</td><td>2.958</td></tr>
<tr><td>$u$</td><td></td><td>0.3033 (0.3050)</td><td>0.303</td></tr>
<tr><td>$E_{coh}$ (eV)</td><td>$- 10.53$ ($- 10.45$ [28])</td><td>$- 19.9$ ($- 19.9$ [32])</td><td>$- 19.9$</td></tr>
<tr><td>$B$ (GPa)</td><td>98.1 (90.6 [29,30])</td><td>210.6 (211. [33])</td><td>219.</td></tr>
<tr><td>$C_{11}$ (GPa)</td><td>171.2 (183. [29,30])</td><td>288.5 (268. [33])</td><td>289.7</td></tr>
<tr><td>$C_{12}$ (GPa)</td><td>64.1 (47.)</td><td>171.8 (175.)</td><td>177.5</td></tr>
<tr><td>$C_{44}$ (GPa)</td><td>52.3 (58.)</td><td>115.4 (124.)</td><td>117.6</td></tr>
<tr><td>$C_{66}$ (GPa)</td><td></td><td>154. (190.)</td><td>167.</td></tr>
<tr><td>$C_{33}$ (GPa)</td><td></td><td>374.6 (484.)</td><td>399.</td></tr>
<tr><td>$C_{23}$ (GPa)</td><td></td><td>150.6 (147.)</td><td>160.</td></tr>
<tr><td>$Z_O$</td><td>6.7</td><td>3.12</td><td></td></tr>
<tr><td>$Q$</td><td>1.8 (1.83$^{\text{a}}$)</td><td>1.265 (1.20$^{\text{a}}$)</td><td>1.016</td></tr>
<tr><td>$f_P$</td><td>0.645</td><td>0.5</td><td></td></tr>
<tr><td>$\delta$ (eV)</td><td>8.8</td><td>3.3</td><td></td></tr>
<tr><td>$E_G$ (eV)</td><td>11.4 (9.$^{\text{a}}$)</td><td>4.7 (3.6$^{\text{a}}$)</td><td></td></tr>
<tr><td colspan="4">$^{\text{a}}$ Ab initio (see Table 3).</td></tr>
</tbody></table>

property. This is illustrated in the case of $TiO_2$ in Tables 1-2 in which the last column is relative to a previous work [17]. It can be seen (Table 2) that the calculated properties are as satisfactory as those obtained in this work, with non equal, but comparable parameters.

Why then change parameters? The first reason concerns $\chi_O^0$ and $f_{P}^{0}$. The previous values had been taken from a work by Thomas et al. [34] who used the fit presented in Fig. 1 (dotted line). This fit is not accurate between $Q_O=-1$ and $-2$, which is however the range of interest for oxides. In this work we used the fit represented in Fig. 1 (solid line). The second reason relates to the value $Q = 1.016$ obtained in the previous work, which is distant from our ab initio Mulliken charge ($Q = 1.20$, see Table 3). Here again, a point must be emphasized. The Mulliken charges obtained from ab initio calculations constitute a very useful indication but rather arbitrary. As a matter of fact, the Mulliken charges depend on the standard basis set and on the functional used in the DFT calculations. Thus, the Ti basis set used to stabilize STO leads to $Q = 1.20$ in $TiO_2$ (B3LYP functional) while another Ti basis set used previously for $TiO_2$ [28] led to $Q = 1.065$ with B3LYP functional and to $Q = 1.114$ in the GGA approximation [17]. In this study involving STO, we tried to obtain a nearby value of $Q = 1.20$.

The SMTB-Q model allows estimating some properties related to the electronic structure of oxides. From Eq. (A1), we can calculate the so-called Phillips's ionic factor defined as [35]:

$$
f_{P}=\frac{\left(\varepsilon_{M}-\varepsilon_{O}\right)^{2}}{\left(\varepsilon_{M}-\varepsilon_{O}\right)^{2}+4 Z_{O} \beta^{2}}=\left[1-\frac{m}{n_{0}}(2-Q)\right]^{2}.\qquad(8)
$$

![](./images/813221606116556801_1.jpg)

Fig. 1. Atomic self-energy of oxygen ions as a function of charges.

<table><caption>Table 3
Lattice parameters, gap $(E_C)$ and Mulliken charges $(Q_i)$ for bulk SrO, $TiO_2$ and $SrTiO_3$ calculated using the CRYSTAL06 code and the B3LYP functional. The calculated values are compared with experimental data in brackets.</caption>
<tbody><tr><td></td><td>SrO</td><td>TiO$_2$</td><td>SrTiO$_3$</td></tr>
<tr><td>$a$ (Å)</td><td>5.107 (5.16 [28])</td><td>4.633 (4.594 [31])</td><td>3.921 (3.903 [45])</td></tr>
<tr><td>$c$ (Å)</td><td></td><td>2.979 (2.959[31])</td><td></td></tr>
<tr><td>$u$</td><td></td><td>0.306 (0.305)</td><td></td></tr>
<tr><td>$E_{G}$ (eV)</td><td>9.07 (5.9 [28])</td><td>3.62 (3.06 [44])</td><td></td></tr>
<tr><td>$Q$</td><td>1.829</td><td>1.202</td><td>1.449</td></tr>
<tr><td>$Q_{Sr}$</td><td>1.829</td><td></td><td>1.856</td></tr>
<tr><td>$Q_{Ti}$</td><td></td><td>2.404</td><td>2.486</td></tr>
</tbody></table>

The values reported in Table 2 shows that SrO is more ionic than $TiO_2$, as expected. From Eq. (8), we can calculate the energy difference between the atomic orbitals $\delta=\varepsilon_M-\varepsilon_O$:

$$
\delta=\varepsilon_{M}-\varepsilon_{O}=\frac{2 \sqrt{Z_{O}} \beta}{\sqrt{1 / f_{P}-1}},\qquad(9)
$$

and the gap:

$$
E_{G}=\sqrt{\delta^{2}+4 Z_{O} \beta^{2}}.\qquad(10)
$$

The calculated gaps are only qualitative. They are overestimated by about 25% with respect to ab initio values (Table 2), which is acceptable for such a model. As a matter of fact, in the ALM approach (Appendix A), the electron delocalization between oxygen is not taken into account which results in the narrowing of the bands and in the broadening of the gap. The gap is also broadened by neglecting the crystal field splitting.

For SrO (MgO...), $n_{cov}=2$ and for $TiO_2$ (ZrO$_2$...), $n_{cov}=5$. Eq. (6) becomes:

$$
\left(\chi_{O}^{0}-\chi_{S r}^{0}\right)+J^{\Sigma} Q=2 m \beta \sqrt{Z_{O}} \frac{2(Q-1)}{\sqrt{Q(2-Q)}}\qquad(11a)
$$

for SrO and:

$$
\left(\chi_{O}^{0}-\chi_{T i}^{0}\right)+J^{\Sigma} Q=2 m \beta \sqrt{Z_{O}} \frac{(2 Q+1)}{\sqrt{(2-Q)(3+Q)}}\qquad(11b)
$$

for $TiO_2$. The root Q of Eqs. (11a) and (11b), corresponds to the intersection of the two functions of both sides of the equal sign (named Fcoul at the left side and Fcov at the right side). Fig. 2(a,b) represents the graphical solutions of Eq. (11a) and (11b). The two functions Fcoul and Fcov intersect in $Q = 1.8$ for SrO and in $Q = 1.265$ for $TiO_2$, values which compare rather well with the Mulliken charges obtained from DFT calculation (see Table 3). Moreover, it can be seen in Fig. 2 that Q is always limited to the maximum value of 2 by the function Fcov, independently of the values of the parameters, which can change significantly during the fitting procedure. This is the case even in the ionic limit, when $\beta\rightarrow0$. Moreover, Q is not very sensitive to a change of the slope $J^{\Sigma}$ of Fcoul, which ensures the charge stability when the crystal is subjected to a strain ($J^{\Sigma}$ is dependent on the lattice parameters). This is an important feature in contrast to previous models, in which the covalent energy does not depend on the charge. In this last case, Q is given by Eq. (7) and, as shown in Fig. 2 (a,b) (dotted lines), Fcoul must cross the Q axis at the Q equilibrium value. Some variations of $J^{\Sigma}$, either during the fitting procedure or by application of a strain may lead to a value of $Q > 2$, and even to $Q < 0$ if $J^{\Sigma}$ becomes negative. This behavior is all the more likely for strongly ionic systems for which the value of $\chi_O^0-\chi_M^0$ is small and Q close to 2, as for SrO for example. Such a pathological behavior has been discussed in the paper by Zhou et al. [36] on the Streitz and Mintmire model for $Al_2O_3$ [23].

![](./images/813221606116556801_2.jpg)

Fig. 2. Graphical solutions of QEq Eqs. (11a) and (11b) of the SMTB-Q model for SrO (a) and TiO₂ (b).

To illustrate this important point, the charge $Q$ and the cohesive energy $E_{coh}$ of SrO are plotted in Fig. 3 as a function of isotropic strain defined as $\varepsilon=(a - a_0)/a_0$, where $a_0$ represents the equilibrium lattice constant and $a$ is the lattice constant after a hydrostatic volume change.

No pathological behavior is observed up to a strain of $\pm0.30$ which proves the stability of the model. Note that for a compression beyond $-0.23$, the crystal becomes unstable due to strong short range repulsions.

### 2.3. Properties of bulk SrTiO₃

The question of the transferability of empirical potential over a large range of structures, coordination numbers and valence states is an old controversial topic [21,22,37-39]. In a general point of view, there is no reason that the same set of parameters of a given model could account for chemical bonds of different nature, as for example the Ti-O bond in the titanium oxides series: TiO₂ (an insulator with a 3 eV gap), Ti₂O₃ (a semiconductor with a small gap) and TiO (a semimetal). On the other hand, when the electronic behavior of different structures is comparable, the transferability should be possible. Here, we checked the transferability of the SMTB-Q model from SrO and TiO₂ to SrTiO₃ ($=$ SrO + TiO₂). In Fig. 4 (a-c), the local density

![](./images/813221606116556801_3.jpg)

Fig. 3. Variations of charge and cohesive energy versus isotropic strain for SrO structure.

of states (LDOS) of bulk SrO, TiO₂ and SrTiO₃ calculated using density functional theory as implemented in the CRYSTAL06 code [25], are represented (details of ab initio calculations performed in this work are reported in the Appendix C).

In Table 3, the optimized crystallographic parameters, as well as the band gap and the Mulliken charges for SrO, TiO₂ and STO are reported.

Except for gaps which are overestimated (as usual for these type of calculations), the properties compare well with the experimental data. The charges are in good agreements with the study by Piskunov et al. [12] ($Q = 1.41$, $Q_{Sr}=1.87$, $Q_{Ti}=2.35$). In contrast, the Mulliken charges from [10] ($Q = 0.71$, $Q_{Sr}=1.33$, $Q_{Ti}=0.81$) are not relevant. Fig. 4(a-b) show that the top of the valence band (VB) is essentially composed of $O_{2p}$ states with a small contribution from $Sr_{5s}$ states and

![](./images/813221606116556801_4.jpg)

Fig. 4. Local densities of states (LDOS) of bulk SrO, TiO₂ and SrTiO₃.

$Ti_{3d}$ states respectively. In $TiO_{2}$ the lowest part of the conduction band (CB) corresponds mainly to $Ti_{3d}$ states (note the splitting between $t_{2g}$ and $e_{g}$ states). In SrO a more important hybridization between $Sr_{5s}$ and $O_{2p}$ states is observed. The LDOS of STO (Fig. 4(c)) is a superposition of the LDOS of SrO and $TiO_{2}$. Moreover, it can be observed that the ionic charges of Sr and Ti reported in Table 3 are very close in the binary oxides SrO and $TiO_{2}$ and in STO. From these observations we shall assume that the atomic orbital energies $\varepsilon_{Sr}, \varepsilon_{Ti}, \varepsilon_{O}$ are almost unchanged from the binary oxides to STO despite the fact that the environment of each species is modified, as shown in Table 4. Which are then the consequences on the parameters of the model? The (almost) equality of the cation charges in the binary oxides and in STO implies that each cation $i$ ($i = Sr, Ti$) receives the same amount of electrons $\delta Q_{i} = x_{i}Z_{i}^{O}$ from surrounding oxygen atoms in the binary and in the ternary oxide, where $x_{i}$ is the electron transfer per bond and $Z_{i}^{O}$ the coordination number of the cation $i$ with oxygen. Using the relation $n_{i}Z_{i}^{O} = mZ_{O}^{i}$ ($n_{i}$ is the stoichiometry of the cation $i$ and $m$ the stoichiometry of oxygen respectively, see Table 4), the condition to be fulfilled to preserve the cationic charges is $\delta Q_{i} = m/n_{i}x_{i}Z_{O}^{i} = cste$. The charge transfer per oxygen atom to cation $i$, $x_{i}Z_{O}^{i} = \delta Q_{O_{i}}$ is given by Eq. (A1):

$$
\delta Q_{O_{i}}=\frac{n_{O_{i}}}{m}\left(1-\frac{\varepsilon_{i}-\varepsilon_{O}}{\sqrt{\left(\varepsilon_{i}-\varepsilon_{O}\right)^{2}+4 Z_{O}^{i} \beta_{i}^{2}}}\right),\qquad(22)
$$

It is assumed here that each cation Sr and Ti forms an alternating lattice with oxygen in STO. The cohesive energy has the same form than in Eqs. (1)-(5). There are two covalent terms and two repulsive terms for Ti-O and Sr-O bonds and no short-range interaction between Sr and Ti atoms as their outer orbitals are empty. We obtain the condition:

$$
\frac{n_{O_{i}}}{n_{i}}\left(1-\frac{\varepsilon_{i}-\varepsilon_{O}}{\sqrt{\left(\varepsilon_{i}-\varepsilon_{O}\right)^{2}+4 Z_{O}^{i} \beta_{i}^{2}}}\right)=c s t e.\qquad(23)
$$

Since the ratio $n_{O_{i}}/n_{i}$ is equal in the binary oxides and in STO (see Table 4), and assuming that $\varepsilon_{i}-\varepsilon_{O}$ is unchanged, the condition to preserve the cationic charges is simply: $\beta_{i}\sqrt{Z_{O}^{i}} = cste$ for each cation $i$. Therefore (see Table 4):

$$
\begin{aligned}
& \beta_{\mathrm{Sr}(S T O)}=\sqrt{6} / \sqrt{4} \times \beta_{\mathrm{Sr}(S r O)}=1.743 \\
& \beta_{\mathrm{Ti}(S T O)}=\sqrt{3} / \sqrt{2} \times \beta_{\mathrm{Ti}\left(\mathrm{TiO}_{2}\right)}=1.135 \\
& \xi_{\mathrm{Sr}(S T O)}=0.737 \\
& \xi_{\mathrm{Ti}(S T O)}=0.478.
\end{aligned}\qquad(24)
$$

The structural, energetic and elastic properties of STO reported in Table 5 (2nd column) were calculated using the parameters of Table 1 except for $\xi_{i}$ given by Eq. (24). Note that we used $R_{O}=0.52$ Å, because the total coordination number of oxygen is equal to 6 in STO as in SrO.

<table>
<caption>Table 4<br>First neighbor coordination numbers, experimental M-O distances (in Å), stoichiometry coefficients and $n_{0}$ in bulk SrO, $TiO_{2}$ and $SrTiO_{3}$.</caption>
<thead>
<tr>
<th></th>
<th>SrO</th>
<th>$TiO_{2}$</th>
<th>$SrTiO_{3}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>$Z_{Sr}^{O},Z_{Sr}^{S}$</td>
<td>6, 6</td>
<td></td>
<td>4, 12</td>
</tr>
<tr>
<td>$Z_{Ti}^{O},Z_{Ti}^{S}$</td>
<td></td>
<td>3, 6</td>
<td>2, 6</td>
</tr>
<tr>
<td>$d_{Sr-O}$</td>
<td>2.5</td>
<td></td>
<td>2.7</td>
</tr>
<tr>
<td>$d_{Ti-O}$</td>
<td></td>
<td>1.95</td>
<td>1.95</td>
</tr>
<tr>
<td>$m$</td>
<td>1</td>
<td>2</td>
<td>3</td>
</tr>
<tr>
<td>$n_{Sr}$</td>
<td>1</td>
<td></td>
<td>1</td>
</tr>
<tr>
<td>$n_{Ti}$</td>
<td></td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>$n_{0_{Sr}}$</td>
<td>1</td>
<td></td>
<td>1</td>
</tr>
<tr>
<td>$n_{0_{Ti}}$</td>
<td></td>
<td>5</td>
<td>5</td>
</tr>
</tbody>
</table>

<table>
<caption>Table 5<br>Lattice parameter, cohesive energy, elastic properties and ionic charges of bulk $SrTiO_{3}$. First column: experimental data, second column: calculated with the SMTB-Q model without fitting, third column: calculated with the SMTB-Q model with fitting. The deviations (%) with experimental data are in brackets.</caption>
<thead>
<tr>
<th></th>
<th>Exp.</th>
<th>$SrTiO_{3}$ (raw)</th>
<th>$SrTiO_{3}$ (fitted)</th>
</tr>
</thead>
<tbody>
<tr>
<td>$a$ (Å)</td>
<td>3.903 [45]</td>
<td>4.027 (3.2%)</td>
<td>$3.87\left(-0.8\%\right)$</td>
</tr>
<tr>
<td>$E_{coh}$ (eV)</td>
<td>$-31.7$ [18]</td>
<td>$-30.6\left(-3.4\%\right)$</td>
<td>$-31.8$ (0.3%)</td>
</tr>
<tr>
<td>$B$ (GPa)</td>
<td>183. [46]</td>
<td>$155.5\left(-15\%\right)$</td>
<td>$182.\left(0.5\%\right)$</td>
</tr>
<tr>
<td>$C_{11}$ (GPa)</td>
<td>334. [46]</td>
<td>$244.\left(-26.8\%\right)$</td>
<td>$326.\left(-2.4\%\right)$</td>
</tr>
<tr>
<td>$C_{12}$ (GPa)</td>
<td>105.</td>
<td>$111.\left(5.6\%\right)$</td>
<td>$111.\left(5.7\%\right)$</td>
</tr>
<tr>
<td>$C_{44}$ (GPa)</td>
<td>127.</td>
<td>$100.\left(-21.3\%\right)$</td>
<td>$102.\left(-20\%\right)$</td>
</tr>
<tr>
<td>Q</td>
<td>$1.45^{\mathrm{a}}$</td>
<td>1.513</td>
<td>1.63</td>
</tr>
<tr>
<td>$Q_{Sr}$</td>
<td>$1.86^{\mathrm{a}}$</td>
<td>1.83</td>
<td>1.85</td>
</tr>
<tr>
<td>$Q_{Ti}$</td>
<td>$2.49^{\mathrm{a}}$</td>
<td>2.71</td>
<td>3.05</td>
</tr>
</tbody>
<tfoot>
<tr>
<td colspan="4">$^{\mathrm{a}}$ Ab initio (see Table 3).</td>
</tr>
</tfoot>
</table>

As no parameter is adjusted, the results are rather good. One observes that the ionic charges are close in binary and ternary oxides and very close to those obtained from ab initio calculations. The agreement between calculated and experimental lattice parameter, cohesive energy and bulk modulus can be improved by adjusting the four energetic parameters involved in the $M-O$ bonding, e.g. $\xi_{i}$ and $A_{i}$ (see Table 1) and $R_{O}$. With the following values: $\xi_{Sr(STO)} = 0.7987$, $A_{Sr} = 0.1574$, $\xi_{Ti(STO)}^{0} = 0.3804$, $A_{Ti} = 0.124$, and $R_{O} = 0.504$, the results reported in Table 5 (3rd column) are obtained. The lattice parameter, the cohesive energy and the bulk modulus are now well reproduced. Note that the fitted parameters are not very different from their starting values.

Calculations up to 1200 K yield thermal expansion from $\alpha_{V} = 3. \times 10^{-5}K^{-1}$ at 273 K to $\alpha_{V} = 4.1 \times 10^{-5}K^{-1}$ at 1200 K which compares well with the experimental value $\alpha_{V} = 3.23 \times 10^{-5}K^{-1}$ in the whole temperature range [47].

At this stage, let us compare the SMTB-Q model with the most widely used classical model in oxides based on the modified Buckingham potential,

$$
U_{i j}=A \exp \left(-r_{i j} / \rho\right)-\frac{C_{6}}{r_{i j}^{6}}+\frac{Q_{i} Q_{j}}{r_{i j}}.
$$

As an example, we chose the most recent model of this type by Thomas et al. [48] cited in Benedek et al. [49] as the best one to predict some properties of a grain boundary in STO. The authors claimed that their model well predicted the bulk properties of STO, which is exact apart for the cohesive energy for which they do not give a value. Using their parameters, we obtained $E_{coh}=-74$ eV which is more than twice the experimental value ($-31.7$ eV). This illustrates the general fact, easily verifiable, that it is impossible to obtain at the same time good lattice properties and the good cohesive energy with such a model. So the absolute value of the cohesive energy is 30 eV instead of 10 eV for SrO and 46 eV instead of 20 eV for $TiO_{2}$. The reason is that such a model, which can be efficient for pure ionic compounds, fail to describe the chemical bonding in oxides.

### 3. $SrO, TiO_{2}$ and $SrTiO_{3}$ surfaces

In heterogeneous systems (presence of a defect), the charge on each ion $i$ depends on its environment, which includes the contributions of both the number and the atomic relaxations of neighbors (up to $r_{c}$). The numerical resolution of the system of inhomogeneous equations such as Eq. (6) is not trivial and time consuming when dealing with many different charges. Nevertheless, all atoms having the same crystallographic environment must have the same charge; therefore there is no need to calculate the charges on all the atoms. Moreover, it is known that the modification of charges around a defect is a local effect that does not extend beyond few Å. Therefore,

practically, we proceed as follows. Let us define the generalized coordination number:

$$
Z_{i(i=O, M)}=\sum_{j(j=M, O)\left(r<r_{c}\right)} \exp \left[-2 q_{M}\left(\frac{r_{i j}}{r_{O M}^{0}}-1\right)\right]. \tag{25}
$$

$Z_{O(M)}$ comprises both the number of neighbors of an $O(M)$ atom and their relaxations and is equal to the coordination number of $O(M)$ if only first neighbors are considered. Atoms for which $Z_{O(M)}$ differ by less than a tolerance $tol_{Z}$ are gathered in what we call a sublattice (SL). All atoms in a given SL have the same charge $Q_{SL}$. The anions and cations belonging to the host bulk SL keep their bulk charges. The energy $E(Q_{i})$ is then minimized with respect to other $Q_{SL}$ whereas the system is fully relaxed by Metropolis Monte Carlo algorithm.

We are mainly interested here by the properties of the $\mathrm{SrTiO}_{3}$ (001) surface, and, in order to compare with the surfaces of the binary oxides, we report also results on SrO (001) and on the three low index surfaces (110), (100) and (001) of $\mathrm{TiO}_{2}$.

The surface energies $\left(E_{S}\right)$ are computed using the following expression:

$$
E_{S}=\frac{1}{2 A_{S}}\left(E_{N}-N E_{c o h}\right), \tag{26}
$$

where $E_{N}$ is the total energy of a sample containing $N$ oxide units, $E_{c o h}$ is the cohesive energy and $A_{S}$ is the area of the total surface of the sample. The 1/2 factor takes into account the existence of two free surfaces for a slab (it must be suppressed for a semi infinite system).

### 3.1. SrO (001)

SrO has a NaCl structure and each atom is sixfold coordinated. At the (001) surface, atoms are fivefold coordinated. Calculations are performed on a $40 \times 40 \times 40 \AA^{3}$ slab containing 1728 atoms ($6 \times 6 \times 6$ elementary cubes of 4 SrO units) with periodic conditions on [100] and [010] directions. After 400 Monte Carlo steps per atoms, the equilibrium is reached, what takes approximately 10 min on one processor of a modern workstation. The calculated surface energy (using the parameters of Table 1) is $E_{S}=0.72 \mathrm{j} \mathrm{m}^{-2}$. A small Sr displacement towards the SrO surface of $0.04 \AA$ is observed, whereas the displacements of other atoms are negligible. The charge transfer (the difference between the charge of an atom at the surface and the charge of the same type of atom in the bulk) is negligible, and $\mathrm{Q}=1.80( \pm 0.01)$ everywhere in the slab.

### 3.2. $\mathrm{TiO}_{2}$ (110), (100) and (001)

A recent study on the three low index $\mathrm{TiO}_{2}$ surfaces concerning energetic, atomic relaxations and charge transfer can be found elsewhere [17]. This study had been achieved with the set of parameters reported in the last column, Table 1. The energies of the three surfaces $(E_{(110)}=0.42, E_{(100)}=0.49$ and $E_{(001)}=1.26 \mathrm{j} \mathrm{m}^{-2})$ were in satisfactory agreements with our ab initio calculations $(E_{(110)}=0.48$, $E_{(100)}=0.68$ and $E_{(001)}=1.36 \mathrm{j} \mathrm{m}^{-2})$. Overall the atomic relaxations were also in good agreements with ab initio calculations and experimental data. The results obtained in the present study, with the parameters of the second column, Table 1, are almost identical as the previous ones following the example of the formation energies: $(E_{(110)}=0.40, E_{(100)}=0.50$ and $E_{(001)}=1.39 \mathrm{j} \mathrm{m}^{-2})$. The two surfaces (110) and (100) have the same number of broken bonds, which explains the small difference between their formation energies. They contain both twofold coordinated oxygen atoms and fivefold coordinated titanium atoms. The surface charge transfer is $+0.20(+0.13)$ for oxygen atoms and $-0.16(-0.13)$ for titanium atoms at the (110) and (100) surface respectively. The (001) surface contains fourfold titanium atoms and twofold oxygen atoms, which causes a higher surface energy. The surface charge transfer is 0.10 for oxygen atoms and $-0.32$ for titanium atoms. For atomic relaxations at the various surfaces the reader is referred to [17].

### 3.3. $\mathrm{SrTiO}_{3}(001) 1 \times 1$

Fig. 5 contains a model of both SrO- and $\mathrm{TiO}_{2}$-terminations of STO (001). The atoms labeled in Fig. 5 are those for which the atomic displacement along the [001] direction was computed. We adopted here the nomenclature used by Charlton et al. [6].

The atoms Sr (9) and O (10) of the SrO-terminated surface lost 4 bonds ($Z=8$ instead of 12) and 1 bond ($Z=5$ instead of 6) respectively. At the $\mathrm{TiO}_{2}$-terminated surface, Ti (1) and O (3) lost 1 and 2 bonds respectively. Two types of calculations were performed with the SMTB-Q model. For the first one, the box is a $23 \times 23 \times Z_{\mathrm{L}} \AA^{3}$ slab $(Z_{\mathrm{L}}=23,50,100 \AA)$ containing 1080,2340 and 4680 atoms $(6 \times 6 \times \mathrm{L}_{\mathrm{Z}}, \mathrm{L}_{\mathrm{Z}}=6,13,26, \mathrm{SrTiO}_{3}$ units) with periodic conditions on [100] and [010] directions, leading to the average formation energy of the two surfaces. The size of the cell in these two directions $(\mathrm{L}_{\mathrm{X}}=$ $\mathrm{L}_{\mathrm{Y}}=6$ ) is chosen in such a way that it is larger than twice the cut-off radius used for the calculation of Coulomb interactions $(\approx 10 \AA)$. The second type of calculations is made on semi infinite systems, leading to the formation energy of each surface (SrO- and $\mathrm{TiO}_{2}$-terminated) independently. The semi infinite box $(\mathrm{L}_{\mathrm{X}}=\mathrm{L}_{\mathrm{Y}}=6)$ contains three zones

![](./images/813221606116556801_5.jpg)

Fig. 5. Model of $\mathrm{SrTiO}_{3}(001)$ showing the SrO-terminated surface (left-hand side of diagram) and the $\mathrm{TiO}_{2}$-terminated surface (right-hand side).

parallel to the surface. The first one is the surface zone of thickness about 15 Å (1.5 times the cut-off radius) where the Monte Carlo relaxations are performed. Under this zone, there are two 10 Å thick zones of fixed atoms maintained at the bulk parameter. The second zone allows the first zone to be bound to a bulk zone and the energy of the box ($EN$ in Eq. (26)) is the energy of the two first zones (which is equivalent to half a slab). The third zone is a buffer zone used only to calculate the energy of each atom of the second zone. The convergence of the surface energy can be checked by increasing the thickness of the first zone. Our ab initio calculations were performed on a slab containing $1 \times 1 \times 6$ SrTiO₃ units.

### 3.3.1. Surface energies
The calculations performed at 2 K on semi infinite systems led to $E_{SrO}=1.20$ j m⁻², $E_{TiO2}=1.09$ j m⁻², and $<E>=1.145$ j m⁻². The TiO₂-terminated surface is more stable by 0.11 j m⁻² than the SrO-terminated surface. Qualitatively, this can be explained by observing that the formation of the SrO-terminated surface involves more M–O broken bonds than the TiO₂-terminated surface. Shell-model simulations by Chen [14] follow the same trend ($E_{TiO2}=0.62$ j m⁻², $E_{SrO}=0.76$ j m⁻²), in contrast with other shell-model simulations ($E_{TiO2}=1.37$ j m⁻², $E_{SrO}=1.33$ j m⁻² [15]) and with ab initio calculations performed on non-stoichiometric slabs ($E_{TiO2}=1.23$ j m⁻², $E_{SrO}=1.15$ j m⁻² [12]). Note that the energy of the SrO-terminated surface is much higher than the energy of the SrO (100) surface ($E_{s}=0.72$ j m⁻²) and that the energy of the TiO₂-terminated surface is much higher than the energy of the most stable TiO₂ (110) and (100) surfaces ($E_{s} \sim 0.50$ j m⁻²). Again, this can be explained by considering the number of M–O broken bonds involved in the formation of each surface. The average energy $<E>=1.145$ j m⁻² found here compares well with ab initio calculations ($<E>=1.19$ j m⁻² [12], $1.21$ j m⁻² [9], $1.26$ [8] j m⁻², $1.38$ j m⁻², this work). The calculations performed at 2 K on slabs with thickness $Z_{L}=23$, 50, 100 Å led to $<E>=1.115$ j m⁻², $1.20$ j m⁻² and $1.16$ j m⁻² respectively.

The variations of the two surface energies with temperature up to 1200 K are shown in Fig. 6. The trend is an increase of the surface energies up to 500 K and then a decrease. The difference between the two energies ($\approx 0.15$ j m⁻²) decreases by a factor of 3 above 600 K. Therefore, for these temperatures, the two surfaces have appreciably the same probability to form.

### 3.3.2. Surface relaxations
The atomic relaxations calculated with the SMTB-Q model are presented in Fig. 7 and compared with our ab initio calculations and experimental data from [6]. For each termination, we limit the presentation to the surface M–O atoms and subsurface M′ atom, e.g. Sr(9), O(10), Ti(5) on the one hand and Ti(1), O(3), Sr(2) on the other hand, because, for other atoms, experimental error are too important to allow some comparison. Theoretical and experimental results are in good agreement only for Sr(9) and there is a large discrepancy for other atoms. Particularly, experimental results show very large displacements of surface O atoms towards the surfaces (with large error bars however), whereas theoretical calculations predict only very small displacements. For subsurface M′ atoms, experimental and theoretical results are at variance concerning the direction of the displacement. On the other hand, SMTB-Q results compare well with ab initio calculations, the greatest difference being for Sr(9).

![](./images/813221606116556801_6.jpg)

Fig. 6. Formation energies of the SrTiO₃(001) SrO- and TiO₂-terminated surfaces versus temperature.

![](./images/813221606116556801_7.jpg)

Fig. 7. Atomic relaxations along the [001] direction at SrTiO₃(001) surfaces for atoms labeled in Fig. 5. Experimental error bars are also shown.

In Table 6 calculated atomic relaxations obtained on semi-infinite systems and slabs are compared with other theoretical calculations. On the whole, there is a good agreement between all results although our SMTB-Q evaluation concerning the Sr(9) plane is somewhat overestimated. Note however that it is compatible with the experimental result.

To summarize, the following important effects were observed for surface atomic relaxations:

- The displacements of surface oxygen planes are very small,
- There are large displacements of surface metal planes inwards, giving rise to the splitting of SrO and TiO₂ planes into metal and

<table>
<caption>Table 6
Atomic relaxations for two SrO and two TiO₂ planes along the [001] direction at SrTiO₃(001) surfaces.</caption>
<tbody><tr><th rowspan="2"></th><th colspan="3">SMTB-Q</th><th colspan="4">Ab initio</th><th>SM</th></tr>
<tr><th>Slab (2 nm)</th><th>Slab (10 nm)</th><th>Surface</th><th>This study</th><th>Ab initio [8]</th><th>Ab initio [12]</th><th>Ab initio [9]</th><th>[15]</th></tr>
<tr><th colspan="9">SrO-terminated</th></tr>
<tr><td>Sr(9)</td><td>−0.32</td><td>−0.34</td><td>−0.33</td><td>−0.17</td><td>−0.22</td><td>−0.18</td><td>−0.26</td><td>−0.27</td></tr>
<tr><td>O(10)</td><td>−0.02</td><td>−0.03</td><td>−0.04</td><td>−0.02</td><td>0.00</td><td>0.03</td><td>0.04</td><td>0.04</td></tr>
<tr><td>Ti(5)</td><td>0.02</td><td>0.02</td><td>0.02</td><td>0.04</td><td>0.05</td><td>0.07</td><td>0.07</td><td>0.06</td></tr>
<tr><td>O(7)</td><td>0.05</td><td>0.04</td><td>0.04</td><td>0.00</td><td>0.00</td><td>0.03</td><td>0.01</td><td>0.03</td></tr>
<tr><td>Sr(6)</td><td>−0.10</td><td>−0.12</td><td>−0.11</td><td>−0.04</td><td>−0.05</td><td></td><td>−0.06</td><td>−0.05</td></tr>
<tr><td>O(8)</td><td>0.04</td><td>0.02</td><td>0.02</td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>Ti</td><td>0.01</td><td>0.00</td><td>0.00</td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>O</td><td>0.03</td><td>0.02</td><td>0.01</td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><th colspan="9">TiO₂-terminated</th></tr>
<tr><td>Ti (1)</td><td>−0.13</td><td>−0.14</td><td>−0.18</td><td>−0.13</td><td>−0.13</td><td>−0.08</td><td>−0.08</td><td>−0.11</td></tr>
<tr><td>O(3)</td><td>0.00</td><td>0.00</td><td>−0.04</td><td>−0.04</td><td>−0.06</td><td>−0.05</td><td>−0.05</td><td>−0.07</td></tr>
<tr><td>Sr(2)</td><td>0.10</td><td>0.10</td><td>0.06</td><td>0.09</td><td>0.09</td><td>0.14</td><td>0.18</td><td>0.13</td></tr>
<tr><td>O(4)</td><td>−0.03</td><td>−0.04</td><td>−0.07</td><td>−0.01</td><td>−0.02</td><td>0.02</td><td>0.03</td><td>−0.08</td></tr>
<tr><td>Ti</td><td>−0.02</td><td>−0.03</td><td>0.02</td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>O</td><td>0.00</td><td>0.00</td><td>0.04</td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>Sr</td><td>0.01</td><td>0.01</td><td>0.04</td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>O</td><td>−0.01</td><td>0.00</td><td>0.05</td><td></td><td></td><td></td><td></td><td></td></tr>
</tbody>
</table>

oxygen planes separated by 0.30 and 0.13 Å respectively and the appearance of a surface induced dipole moment. This effect con- tinues, in lessening, for deeper SrO planes, whereas it is negligible for non-surface TiO₂ planes.
- The distance between Sr and Ti planes (resp. Ti and Sr) is shortened by 19% (resp. 12%) at the SrO (resp. TiO₂) surface.

### 3.3. Charge transfers
The charge transfer at the Sr−O and TiO₂-terminated SrTiO₃ (001) surfaces calculated by the SMTB-Q model and evaluated from ab initio calculations of Mulliken charges is reported in Table 7.

As explained in the introduction of Section 3, the SMTB-Q results were obtained with 3 strontium sublattices (SL), 3 titanium SL and 4 oxygen SL, which correspond to the minimum numbers of SL leading to convergent values of charges (the maximum numbers of SL compat- ible with the second-moment cut-off radius r_c, are 4, 4, 7). The first SL of each species has the generalized coordination number (Eq. (25)) and the charge of the bulk (Z_Sr = 8.85, Q_Sr = 1.83; Z_Ti = 5.34, Q_Ti = 2.71; Z_O = 4.73, Q_Ti = −1.513). The energy E(Q_i) is then minimized with re- spect to the 7 remaining SL, what is very fast. The two other SL of Sr and Ti correspond to the atoms Sr(2) and Sr(9) on the one hand and to Ti(1) and Ti(5) on the other hand. The three other SL of oxygen correspond to O(3), O(4)−O(7) and O(10) respectively. The generalized coordination numbers of SL are reported in Table 7. Note that O(4) and O(7) are gath- ered in the same SL because their coordination numbers are almost equal to the bulk one. Consequently, the charge transfer on these atoms is negligible. Only SL having a generalized coordination number rather different from that of the bulk can be subject to a significant charge transfer and the more the bonding is covalent, the more the charge transfer is important. It is what is observed for Sr and Ti atoms. The charge transfers obtained by the SMTB-Q model are in very good agreement with our ab initio results for the most stable TiO₂-terminated surface. One notes a discrepancy between our results and that from [12] for Ti(1), which is probably due to the difference of thicknesses be- tween the slabs used in the two studies (4 STO units in [12] and 6 in our work). In contrast, there are discrepancies between SMTB-Q and ab initio results for the SrO-terminated surface, especially for O(10) atoms. The SMTB-Q results are in agreement with those of the pure SrO(100) surface, e.g. a negligible charge transfer. The ab initio results are surprising at first sight because all charge transfers are negative close to the SrO surface and do not seem to be locally compensate. It is noteworthy, however, that the oxygen atoms never recover exactly their bulk charges (see Table 3 for bulk values) into the slab, what is not the case with the SMTB-Q model.

<table>
<caption>Table 7 Charge transfer at SrTiO₃(001) surfaces for atoms labeled in Fig. 5. The second column is the generalized coordination number of the labeled atoms (the bulk values are: Z_Sr = 8.85, Z_Ti = 5.34, Z_O = 4.73).</caption>
<thead>
<tr>
<th></th>
<th>SMTB-Q (3 3 4)ᵃ</th>
<th>Z_O(M)</th>
<th>Ab initio This study</th>
<th>Ab initio [12]</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="5">SrO-terminated</td>
</tr>
<tr>
<td>Sr(9)</td>
<td>0.05</td>
<td>5.77</td>
<td>−0.03</td>
<td>−0.03</td>
</tr>
<tr>
<td>O(10)</td>
<td>0.0</td>
<td>3.72</td>
<td>−0.12</td>
<td>−0.12</td>
</tr>
<tr>
<td>Ti(5)</td>
<td>−0.04</td>
<td>5.32</td>
<td>0.01</td>
<td>0.01</td>
</tr>
<tr>
<td>O(7)</td>
<td>−0.03</td>
<td>4.71</td>
<td>−0.02</td>
<td>−0.04</td>
</tr>
<tr>
<td colspan="5">TiO₂-terminated</td>
</tr>
<tr>
<td>Ti(1)</td>
<td>−0.18</td>
<td>4.43</td>
<td>−0.16</td>
<td>−0.04</td>
</tr>
<tr>
<td>O(3)</td>
<td>0.14</td>
<td>3.24</td>
<td>0.14</td>
<td>0.08</td>
</tr>
<tr>
<td>Sr(2)</td>
<td>−0.03</td>
<td>8.71</td>
<td>−0.02</td>
<td>−0.02</td>
</tr>
<tr>
<td>O(4)</td>
<td>−0.03</td>
<td>4.61</td>
<td>0.09</td>
<td>0.05</td>
</tr>
</tbody>
<tfoot>
<tr>
<td colspan="5">ᵃ Number of Sr, Ti and O SL.</td>
</tr>
</tfoot>
</table>

<table>
<caption>Table 8 Effect of strain on the atomic relaxations on 2 nm- and 40 nm-thick thin films at 273 K. d (M−O) is the distance between M and O planes. δ d (Sr−Ti) is the difference between d (Ti−Sr) in the film and d (Sr−Ti) in the perfect bulk. All distances are in Å.</caption>
<thead>
<tr>
<th>Thickness</th>
<th colspan="3">2 nm</th>
<th colspan="3">40 nm</th>
</tr>
<tr>
<td>σ (%)</td>
<td>−1.66</td>
<td>0</td>
<td>+1.66</td>
<td>−1.66</td>
<td>0</td>
<td>+1.66</td>
</tr>
</thead>
<tbody>
<tr>
<td colspan="7">SrO-terminated</td>
</tr>
<tr>
<td>d (Sr−O)</td>
<td>−0.28</td>
<td>−0.30</td>
<td>−0.32</td>
<td>−0.29</td>
<td>−0.31</td>
<td>−0.32</td>
</tr>
<tr>
<td>d (Ti−O)</td>
<td>−0.01</td>
<td>−0.02</td>
<td>−0.02</td>
<td>−0.02</td>
<td>−0.02</td>
<td>−0.01</td>
</tr>
<tr>
<td>d (Sr−O)</td>
<td>−0.11</td>
<td>−0.14</td>
<td>−0.15</td>
<td>−0.13</td>
<td>−0.14</td>
<td>−0.16</td>
</tr>
<tr>
<td>d (Ti−O)</td>
<td>−0.02</td>
<td>−0.02</td>
<td>−0.02</td>
<td>−0.02</td>
<td>−0.02</td>
<td>−0.01</td>
</tr>
<tr>
<td>δ d (Sr−Ti)</td>
<td>−0.27</td>
<td>−0.35</td>
<td>−0.43</td>
<td>−0.27</td>
<td>−0.36</td>
<td>−0.43</td>
</tr>
<tr>
<td colspan="7">TiO₂-terminated</td>
</tr>
<tr>
<td>d (Ti−O)</td>
<td>−0.14</td>
<td>−0.14</td>
<td>−0.13</td>
<td>−0.14</td>
<td>−0.14</td>
<td>−0.16</td>
</tr>
<tr>
<td>d (Sr−O)</td>
<td>+0.11</td>
<td>+0.14</td>
<td>+0.16</td>
<td>+0.09</td>
<td>+0.14</td>
<td>+0.15</td>
</tr>
<tr>
<td>d (Ti−O)</td>
<td>−0.02</td>
<td>−0.02</td>
<td>−0.01</td>
<td>−0.02</td>
<td>−0.03</td>
<td>−0.04</td>
</tr>
<tr>
<td>d (Sr−O)</td>
<td>0.0</td>
<td>0.02</td>
<td>0.03</td>
<td>−0.01</td>
<td>0.01</td>
<td>0.01</td>
</tr>
<tr>
<td>δ d (Ti−Sr)</td>
<td>−0.17</td>
<td>−0.23</td>
<td>−0.31</td>
<td>−0.14</td>
<td>−0.24</td>
<td>−0.30</td>
</tr>
</tbody>
</table>

## 4. SrTiO₃ thin films
We studied here the effect of a strain on the relaxations of thin films of thicknesses from 2 to 40 nm at 273 K. STO/Si(001) is the prototypical system for integration of oxide electronics on silicon since most func- tional oxide heterostructures are grown on STO(001) substrate [2]. In an ideal pseudomorphic and single domain growth of STO on Si(001), the <100> directions of the STO structure are aligned to the <110> di- rection of the Si surface. This epitaxial relationship leads to a lattice mismatch of −1.66%. In order to compare with a positive lattice mismatch, we applied also a symmetrical tensile strain of 1.66%. Calcu- lations were performed for 2, 5, 10, 20 and 40 nm thick films. The inter-plane relaxations did not depend on the thickness and only the re- sults for 2 and 40 nm are reported in Table 8. We observe that the split- ting of the surface SrO plane increased very slightly with the strain and that the splitting of the surface TiO₂ plane is constant. On the other hand, the distance between Sr and Ti planes (resp. Ti and Sr) significant- ly decreased (relaxed) with a compressive strain and increased with a tensile strain.

In Table 9 the out-of-plane lattice parameter (a_⊥) of STO thin films calculated for different thicknesses and strains are reported and the ratio a_⊥/a_// are shown in Fig. 8. According to the elasticity theory, the relationship between in-plane (a_//) and out-of-plane lattice pa- rameter is given by:
$$
\frac{a_{\perp}-a_{0}}{a_{0}}=-2 \frac{C_{12}}{C_{11}} \times \frac{a_{/ /}-a_{0}}{a_{0}},\qquad(27)
$$
where $\frac{a_{/ /}-a_{0}}{a_{0}}=\sigma$ is the strain applied to the film. It follows that:
$$
\frac{a_{\perp}}{a_{/ /}}=2 \frac{C_{12}}{C_{11}}+\left(\frac{1-2 C_{12} / C_{11}}{1+\sigma}\right).\qquad(28)
$$

We obtained $(a_{\perp}/a_{//})_{Elas}=1.028$ and $(a_{\perp}/a_{//})_{Elas}=0.973$ for a strain of −1.66% and +1.66% respectively (represented by horizontal dashed lines in Fig. 8). Thus, the elasticity theory applies well only to

<table>
<caption>Table 9 Out-of-plane lattice parameter of STO thin films as functions of thickness and strain at 273 K.</caption>
<thead>
<tr>
<th>Thickness (nm):</th>
<th></th>
<th>2</th>
<th>5</th>
<th>10</th>
<th>20</th>
<th>40</th>
</tr>
<tr>
<th>Strain</th>
<th>a_// (Å)</th>
<th>a_⊥ (Å)</th>
<th>a_⊥ (Å)</th>
<th>a_⊥ (Å)</th>
<th>a_⊥ (Å)</th>
<th>a_⊥ (Å)</th>
</tr>
</thead>
<tbody>
<tr>
<td>−1.66%</td>
<td>3.812</td>
<td>3.920</td>
<td>3.912</td>
<td>3.891</td>
<td>3.838</td>
<td>3.824</td>
</tr>
<tr>
<td>+1.66%</td>
<td>3.941</td>
<td>3.824</td>
<td>3.823</td>
<td>3.834</td>
<td>3.870</td>
<td>3.890</td>
</tr>
</tbody>
</table>

![](./images/813221606116556801_8.jpg)

Fig. 8. Ratio $a_{\perp}/a_{\parallel}$ of STO thin films as functions of thickness and strain at 273 K. Horizontal dashed lines are values yielded by the elasticity theory.

very thin films of few nm thick. Beyond 20 nm, the films are almost fully relaxed.

## 5. Conclusions

In this paper, variable-charge atomic simulations were performed to calculate the properties of the two possible terminations of the $SrTiO_3(001)$ surface. The SMTB-Q model that captures new physics with regards to previous semiempirical models was used. The parameters of the model employed for the description of $SrTiO_3$ were extracted from independent parameter sets for $SrO$ and $TiO_2$ showing the good transferability of the model. The SMTB-Q model shown that it is capable of describing oxide surfaces (energetic, atomic relaxations and charge transfer) of complex oxides and that the obtained results are reliable, in very good agreement with ab initio calculations. Moreover, the local treatment of charges makes possible large scale simulations with very small CPU resources.

The main results obtained on the $SrTiO_3(001)$ surfaces are the following:
- The $TiO_2$-terminated surface is more stable by about $0.15\ \text{J}\ \text{m}^{-2}$ than the SrO-terminated surface up to 500 K. At higher temperature this difference decreases by a factor 3. Each surface has a higher energy than the equivalent surface in the binary oxides that is consistent with the number of broken bonds involved in the formation of the various surfaces.

- There are large displacements of metal surface atoms towards the surfaces and smaller upward displacements of subsurface metal atoms. These displacements are much larger than the displacement of oxygen atoms, which results in a large rumpling of the surfaces due to the splitting of the $SrO$ and $TiO_2$ surface planes. The distance between the first Sr and Ti planes (resp. Ti and Sr) is shortened by 19% (resp. 12%) at the SrO (resp. $TiO_2$) surface.
- The charge transfers at the $TiO_2$-terminated surface are comparable with those at $TiO_2$ surfaces, showing an increase of the Ti–O bond covalency near the surface. In contrast, the charge transfer for the SrO-terminated surface is negligible for Sr atoms, as at the pure $SrO(001)$ surface, which is consistent with the high degree of ionicity of the Sr–O bond.

Finally, the application of a strain ($\pm 1.66\%$) on thin STO films from 2 to 40 nm does not significantly modify the atomic surface relaxations a part for the Sr–Ti (resp. Ti–Sr) distance. The ratio between out-of-plane and in-plane lattice parameters follows the elasticity theory prediction for a thickness up to $\approx 5$ nm and the film is almost fully relaxed from 20 nm thick.

## Appendix A. Alternating lattice model (ALM)

The ALM developed by Goniakovski and Noguera [18,19] applies to a simple non-correlated oxide $M_nO_m$ in which the anions and cations belong to alternating sublattices (oxygen anions O are surrounding by cations M and vice versa). The tight-binding approach finds eigenfunctions of $M_nO_m$ as a linear combination of atomic orbitals. Two fundamental assumptions are made: i) the outer atomic orbitals on each type of atoms are assumed to be degenerated with the energy $\varepsilon_M(\varepsilon_O)$ for cations and anions respectively (this means that the crystal field splitting is neglected), ii) the probability of hopping of electrons, $\beta$, is considered only from one sublattice to the other (the small hopping between anions is not accounted in this model). The number of coupled electronic states between cation and anion sublattices is $n_0=\min(nd_M, md_O)$, where $d_M$ (resp. $d_O$) is the degeneracy of the cation (resp. oxygen) outer orbitals. The properties of interest (ionic charges, covalent energy) being integrated quantities over the valence band, a very simplified form for the density of states (DOS) $N(E)$ can be chosen to describe the band structure. The simplest choice consists in two Dirac functions, each representing the valence band (VB) and the conduction band (CB) respectively, separated by an energy gap $E_G=\sqrt{(\varepsilon_M-\varepsilon_O)^2+4Z_O\beta^2}$, where $Z_O$ is the coordination number of oxygen. The integral of the local DOS (LDOS) of anions over the VB yields the number of electrons on anions and the absolute value of the oxygen charge $Q=|Q_O|$:

$$
Q=2-\frac{n_0}{m}\left(1-\frac{\varepsilon_M-\varepsilon_O}{\sqrt{(\varepsilon_M-\varepsilon_O)^2+4Z_O\beta^2}}\right), \tag{A1}
$$

and the integral of $EN(E)$ over VB yields the covalent energy:

$$
E_{\text{cov}}=-4n_0\frac{Z_O\beta^2}{\sqrt{(\varepsilon_M-\varepsilon_O)^2+4Z_O\beta^2}}, \tag{A2}
$$

The Eq. (A2) coupled with Eq. (A1), leads to:

$$
E_{\text{cov}}=-2m\beta\sqrt{Z_O}\sqrt{\delta Q_O\left(2\frac{n_0}{m}-\delta Q_O\right)} \tag{A3}
$$

$E_{\text{cov}}$ is a function of $\beta\sqrt{Z_O}$ as in metals [26] and of the oxygen-cation electron transfer $\delta Q_O=2-Q$. $\delta Q_O$ is a decreasing function of the ratio $\beta/(\varepsilon_M-\varepsilon_O)$. When $\beta/(\varepsilon_M-\varepsilon_O)=0$, the oxide is fully ionic, $Q=|Q_O|=2$, and $E_{\text{cov}}=0$. On the contrary, when $(\varepsilon_M-\varepsilon_O)/\beta=0$, $Q=0$, all the atoms are identical and the compound purely covalent.

Let define $n_{\text{cov}}=2\frac{n_0}{m}$ and $\Delta Q_O=\delta Q_O(n_{\text{cov}}-\delta Q_O)$. Eq. (A3) is rewritten:

$$
E_{\text{cov}}=-2m\beta\sqrt{Z_O}\sqrt{\Delta Q_O}. \tag{A4}
$$

When dealing with heterogeneous systems or several cations, as in STO, $E_{\text{cov}}$ must be rewritten on each sublattice metal and oxygen. For a binary oxide, $M_nO_m$, this leads to:

$$
E_{\text{cov}}=-\xi_O\sqrt{\Delta Q_O}\left(m\sqrt{Z_O}+n\sqrt{Z_M}\right)\ \text{with}\ \xi_O=2\beta\left(\frac{1}{(1+\sqrt{n/m})}\right),
$$

or equivalently to:

$$
E_{\text{cov}}=-\xi_M\sqrt{\Delta Q_M}\left(m\sqrt{Z_O}+n\sqrt{Z_M}\right) \tag{A5}
$$

with $\xi_M=\frac{n}{m}\xi_O=2\beta\frac{n}{m}\left(\frac{1}{(1+\sqrt{n/m})}\right)$ and $\Delta Q_M=\left(\frac{m}{n}\right)^2\Delta Q_O$.

For a ternary oxide $A_{n_1}B_{n_2}O_m$, it becomes:

$$
\begin{aligned}
E_{\mathrm{cov}}= & -\xi_{1} \sqrt{\Delta Q_{1}}\left(m \sqrt{Z_{0}^{1}}+n_{1} \sqrt{Z_{1}^{0}}\right)-\xi_{2} \sqrt{\Delta Q_{2}}\left(m \sqrt{Z_{0}^{2}}+n_{2} \sqrt{Z_{2}^{0}}\right). \\
& \text { (A6) }
\end{aligned}
$$

## Appendix B. QEq expression for the SMTB-Q model

In the QEq scheme, $E_{coh}$ is minimized with respect to the charges $Q_A$, which leads to the system of non-linear equations:

$$
\frac{\partial E_{c o h}}{\partial Q_{A}}=\chi_{A}\left(Q_{i}\right)=\chi=\chi_{A}^{0}+\sum_{B} J_{A B} Q_{B}+\chi_{A}^{\mathrm{cov}},
\tag{B1}
$$

with $\chi_{A}^{\mathrm{cov}}=\frac{\partial\left(E_{\mathrm{cov}}\right)}{\partial Q_{A}}$.

For the perfect crystal $M_nO_m$, there are only two different charges $Q_M$ and $Q_O$ related through the electroneutrality condition $mQ = nQ_M$ ($Q = |Q_O|$). The equalization of chemical potentials leads to:

$$
\chi_{M}^{0}-\chi_{O}^{0}=\sum_{O}\left(J_{O O}-J_{M O}\right) Q_{O}+\sum_{M}\left(J_{O M}-J_{M M}\right) Q_{M}+\left(\chi_{O}^{\mathrm{cov}}-\chi_{M}^{\mathrm{cov}}\right)
\tag{B2}
$$

or:

$$
\chi_{M}^{0}-\chi_{O}^{0}=J^{\Sigma}+\left(\chi_{O}^{\mathrm{cov}}-\chi_{M}^{\mathrm{cov}}\right)
\tag{B3}
$$

with $J^{\Sigma}$ the total Coulomb interaction:

$$
J^{\Sigma}=\sum_{O}\left(J_{M O}-J_{O O}\right)+\frac{m}{n} \sum_{M}\left(J_{O M}-J_{M M}\right).
\tag{B4}
$$

From Eq. (A4), we obtain:

$$
\chi_{O}^{\mathrm{cov}}=-2 m \beta \sqrt{Z_{O}} \frac{\partial(\sqrt{\Delta Q})}{\partial Q_{O}} \text { and } \chi_{M}^{\mathrm{cov}}=-2 m \beta \frac{Z_{M}}{\sqrt{Z_{O}}}\left(\frac{\partial \sqrt{\Delta Q}}{\partial Q_{M}}\right)
\tag{B5}
$$

$$
\chi_{M}^{\mathrm{cov}}-\chi_{O}^{\mathrm{cov}}=2 m \beta \sqrt{Z_{O}}\left[\left(\frac{\partial \sqrt{\Delta Q}}{\partial Q_{O}}\right)-\frac{Z_{M}}{Z_{O}}\left(\frac{\partial \sqrt{\Delta Q}}{\partial Q_{M}}\right)\right].
$$

Using the relations:

$$
z_{M} / z_{o}=m / n \text { and } \frac{d \sqrt{\Delta Q}}{d Q_{O}}=\frac{\partial \sqrt{\Delta Q}}{\partial Q_{O}}-\frac{m}{n}\left(\frac{\partial \sqrt{\Delta Q}}{\partial Q_{M}}\right),
$$

one finally obtains:

$$
\chi_{M}^{\mathrm{cov}}-\chi_{O}^{\mathrm{cov}}=2 m \beta \sqrt{Z_{O}} \frac{d \sqrt{\Delta Q}}{d Q_{O}}=2 m \beta \sqrt{Z_{O}} \frac{\left(n_{\mathrm{cov}}-4+2 Q\right)}{\sqrt{(2-Q)\left(n_{\mathrm{cov}}-2+Q\right)}},
$$

and

$$
\left(\chi_{O}^{0}-\chi_{M}^{0}\right)+J^{\Sigma} Q=2 m \beta \sqrt{Z_{O}} \frac{\left(n_{\mathrm{cov}}-4+2 Q\right)}{\sqrt{(2-Q)\left(n_{\mathrm{cov}}-2+Q\right)}}.
\tag{B6}
$$

## Appendix C. ab initio calculation details

In the CRYSTAL06 code, the crystalline orbitals are expanded in terms of localized atomic Gaussian basis set. The B3LYP functional (based on Becke's three parameters adiabatic connection exchange functional [40] in combination with Lee-Yang-Parr's correlation functional [41]) have been used in this work. Atoms were treated at an all-electron level. The standard basis sets (8-6411-41 for titanium, HAYWSC 311(1d) G for strontium, and 8-411d1 for oxygen) were used for orbital expansion when solving the DFT-SCF equation iteratively [50]. The number of k points in the first irreducible Brillouin zone (Pack-Monkorst lattice) [42] at which the Hamiltonian matrix is diagonalized is equal to 40. In optimizing the geometry, we allowed the relaxation of all atoms. A modified conjugated gradient algorithm [43] has been implemented in the CRYSTAL06 code to optimize cell parameters and fractionnary atomic coordinates. In geometry optimization, the criterion for convergence on the total energy is set to $10^{-8}$ Hartree.

## References

[1] U. Diebold, Nat. Mater. 9 (2010) 245.
[2] C. Merckling, G. Saint-Girons, G. Delhaye, G. Patriarche, L. Largeau, V. Favre-Nicollin, M. El-Kazzi, P. Regreny, B. Vilquin, O. Marty, C. Botella, M. Gendry, G. Grenet, Y. Robach, G. Hollinger, Thin Solid Films 517 (2008) 197.
[3] M. Kubo, Y. Oumi, R. Miura, A. Stirling, A. Miyamoto, M. Kawasaki, M. Yoshimoto, H. Koinuma, J. Chem. Phys. 109 (1998) 8601.
[4] N. Bickel, G. Schmidt, K. Heinz, K. Müller, Phys. Rev. Lett. 62 (1989) 2009.
[5] A. Ikeda, T. Nishimura, T. Morishita, Y. Kido, Surf. Sci. 433-435 (1999) 520.
[6] G. Charlton, S. Brennan, C.A. Mury, R. McGrath, D. Norman, T.S. Turner, G. Thornton, Surf. Sci. 457 (2000) 376.
[7] V. Vonk, S. Konings, G.J. van Hummel, S. Harkema, H. Graafsma, Surf. Sci. 595 (2005) 183.
[8] J. Padilla, D. Vanderbuilt, Surf. Sci. 418 (1998) 64.
[9] C. Cheng, K. Kunc, M.H. Lee, Phys. Rev. B 62 (2000) 10409.
[10] H.J. Zhang, G. Chen, Z.H. Li, Appl. Surf. Sci. 253 (2007) 8345.
[11] Zhi-Qiang Li, Jia-Lin Zhu, C.Q. Wu, Z. Tang, Y. Kawazoe, Phys. Rev. B 5 (8) (1998) 8075.
[12] S. Piskunov, E.A. Kotomin, E. Heifets, J. Maier, R.I. Eglitis, G. Borstel, Surf. Sci. 575 (2005) 75.
[13] K. Johnston, M.R. Castell, A.T. Paxton, M.W. Finnis, Phys. Rev. B 70 (2004) 85415.
[14] S.P. Chen, J. Mater. Res. 13 (1997) 1848.
[15] E. Heifets, E.A. Kotomin, J. Maier, Surf. Sci. 462 (2000) 19.
[16] R. Tétot, A. Hallil, J. Creuze, I. Braems, EPL 83 (2008) 4000.
[17] A. Hallil, E. Amzallag, S. Landron, R. Tétot, Surf. Sci. 605 (2011) 738.
[18] J. Goniakowski, C. Noguera, Surf. Sci. 319 (1994) 81.
[19] C. Noguera, Physics and Chemistry of Oxide surfaces, Cambridge University Press, 1996.
[20] A.K. Rappé, W.A.I.I.I. Goddard, J. Phys. Chem. 95 (1991) 3358.
[21] V. Swamy, J.D. Gale, Phys. Rev. B 62 (2000) 5406.
[22] A. Hallil, R. Tétot, F. Berthier, I. Braems, J. Creuze, Phys. Rev. B 7 (3) (2006) 165406.
[23] F.H. Streitz, J.W. Mintmire, Phys. Rev. B 50 (1994) 11996.
[24] T.-R. Shan, B.D. Devine, T.W. Kemper, S.B. Sinnott, S.R. Phillpot, Phys. Rev. B 81 (2010) 125538.
[25] V.R. Saunders, R. Dovesi, C. Roetti, R. Orlando, C.M. Zicovich-Wilson, N.M. Harisson, K. Doll, B. Civalleri, I.J. Bush, P. D'Arco, M. Llunell, CRYSTAL03 user's manual, Università di Torino, Torino, 2003.
[26] F. Ducastelle, J. Phys. Paris 31 (1970) 1055.
[27] J. Creuze, F. Berthier, R. Tétot, B. Legrand, Phys. Rev. B 62 (2000) 2813.
[28] G. Cappellini, F. Finocchi, S. Bouette-Russo, C. Noguera, Comput. Mater. Sci. 20 (2001) 401.
[29] P.R. Son, R.A. Bartels, J. Phys. Chem. Solids 33 (1972) 819.
[30] F. Michard, M.A. Zarembowitch, C. R. Acad. Sci. Paris B 269 (1969) 30.
[31] C.J. Howard, T.M. Sabine, F. Dickson, Acta Crystallogr. B Struct. Sci. 47 (1991) 462.
[32] In: D.R. Lide (Ed.), CRC handbook of Chemistry and Physics, 83rd edition, CRC, Boca Raton, Fla, 2002, (Sect. 5).
[33] D.G. Isaak, J.D. Cares, H. Cynn, E. Hake, Phys. Chem. Miner. 26 (1998) 31.
[34] B.S. Thomas, N.A. Marks, B.D. Begg, Phys. Rev. B 69 (2004) 144122.
[35] J.C. Phillips, Rev. Mod. Phys. 42 (1970) 317.
[36] X.W. Zhou, H.N.G. Wadley, J.-S. Filhol, M.N. Neurock, Phys. Rev. B 69 (2004) 35402.
[37] H. le Roux, L. Glasser, J. Mater. Chem. 7 (1997) 843.
[38] B.S. Thomas, N.A. Marks, Phys. Rev. B 76 (2007) 167401.
[39] A. Hallil, R. Tétot, F. Berthier, I. Braems, J. Creuze, Phys. Rev. B 7 (6) (2007) 167402.
[40] A.D. Becke, J. Chem. Phys. 98 (1993) 5648.
[41] C. Lee, W. Yang, R.G. Parr, Phys. Rev. B 37 (1988) 785.
[42] H.J. Monkhorst, J.D. Pack, Phys. Rev. B 13 (1976) 5188.
[43] H.B.J. Schlegel, Comput. Chem. 3 (1982) 214.
[44] J. Pascual, J. Camassel, H. Mathieu, Phys. Rev. B 18 (1978) 5606.
[45] R.L. Moreira, A. Dias, J. Phys. Chem. Solids 68 (2007) 1617.
[46] R.O. Bell, G. Rupprecht, Phys. Rev. 129 (1962) 90.
[47] D. de Ligny, P. Richet, Phys. Rev. 53 (6) (1996) 3013.
[48] B.S. Thomas, N.A. Marks, B.D. Begg, Nucl. Instrum. Methods Phys. Res. B228 (2005) 288.
[49] N.A. Benedek, A.L.-S. Chua, C. Elssässer, A.P. Sutton, M.W. Finnis, Phys. Rev. 78 (2008) 064110.
[50] S. Piskunov, E. Heifets, R.I. Eglitis, G. Borstel, Comput. Mater. Sci. 29 (2004) 178.
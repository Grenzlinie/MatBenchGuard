# Journal Pre-proof

![](./images/812746361601523712_1.jpg)

Structural and physical properties of intermetallic compounds $Re_3Pd_2Sn_2$, (Re= Yb, Eu)

Noureddine Mounis, Mohamed Maachou, Houari Khachai, Abderrahmane Reggad, Bakhtiar ul Haq

| PII: | S2352-2143(19)30268-0 |
|---|---|
| DOI: | https://doi.org/10.1016/j.cocom.2019.e00422 |
| Reference: | COCOM 422 |

To appear in: *Computational Condensed Matter*

Received Date: 10 December 2018

Revised Date: 26 July 2019

Accepted Date: 27 July 2019

Please cite this article as: N. Mounis, M. Maachou, H. Khachai, A. Reggad, B.u. Haq ., Structural and physical properties of intermetallic compounds $Re_3Pd_2Sn_2$, (Re= Yb, Eu), *Computational Condensed Matter*, https://doi.org/10.1016/j.cocom.2019.e00422.

This is a PDF file of an article that has undergone enhancements after acceptance, such as the addition of a cover page and metadata, and formatting for readability, but it is not yet the definitive version of record. This version will undergo additional copyediting, typesetting and review before it is published in its final form, but we are providing this version to give early visibility of the article. Please note that, during the production process, errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

© 2019 Elsevier B.V. All rights reserved.

# Structural and physical properties of intermetallic compounds $Re_3Pd_2Sn_2$, (Re= Yb, Eu).

Noureddine MOUNIS¹, Mohamed MAACHOU¹, Houari KHACHAI²,
Abderrahmane Reggad³⁴, Bakhtiar ul Haq⁵.

¹Université de Sidi Bel Abbés, Département de physique, BP 89 Cité Ben M 'hidi, 22000 Sidi Bel Abbés, Algeria.
²Laboratoire d'Etude des Matériaux et Instrumentations optiques, Djilali Liabés University, 22000 Algeria.
³Engineering Physics Laboratory, Faculty of Material Sciences, Ibn Khaldoun University, Tiaret 14000, Algeria.
⁴Modeling and Simulation in Materials Science Laboratory, Physics Department, University of Sidi Bel-Abbes, Algeria.
⁵Advanced Functional Materials & Optoelectronics Laboratory (AFMOL), Department of Physics, Faculty of Science, King Khalid University, P.O. Box 9004, Abha, Saudi Arabia.

## Abstract
Using the full Potential linearized augmented plane wave (FP-LAPW) method based on functional density theory (DFT) implemented in Wien2k code, structural, electronic and magnetic properties of intermetallic compounds $Re_3Pd_2Sn_2$ (Re=Yb, Eu) are calculated. The local (spin) density approximation L(S)DA and L(S)DA+U are used in the exchange-correlation term to compute lattice parameters, bulk modulus and its first derivative. The Coulomb interaction constant U is obtained using constrained DFT method for both Yb and Eu ions. The hybrid functionals (HF) as a useful method for strongly correlated systems was used to calculate density of states (DOS) and magnetic properties. We find good agreement between calculated structural properties and experimental ones. The density of states DOS shows metallic behavior for both compounds. We find that the $Eu_3Pd_2Sn_2$ compound is magnetically ordered, whereas the $Yb_3Pd_2Sn_2$ compound is not.

**Keywords:** Intermetallic compounds, $Yb_3Pd_2Sn_2$, $Eu_3Pd_2Sn_2$, DFT, effective U.

### 1. Introduction:

Rare earth intermetallic compounds present a real diversity of materials which are used in many applications such as magnets, actuators, magneto-optical data storage, cryogenerators etc... [1].

In this paper, physical properties of ternary intermetallic compounds of type $Re_3Pd_2Sn_2$, $Re=Yb$, $Eu$, are studied. In general, Europium and ytterbium behave as divalent atom, in a way similar to that of alkaline-earths (calcium $Ca$, strontium $Sr$, barium $Ba$) [1]. Unusually, in two or more inequivalent crystallographic sites, lanthanides $Yb$ and $Eu$, in some intermetallic compounds, exist in both divalent state; $Yb^{2+}([Xe] 4f^{14})$, $Eu^{2+}([Xe] 4f^{7})$ and trivalent state; $Yb^{3+}([Xe] 4f^{13})$, $Eu^{3+}([Xe] 4f^{6})$; this case is called *heterogeneous mixed-valence*; another case is that of every lanthanide-ion in the system that has the same *intermediate non-integer* valence due to the hybridization of $4f$ electrons [2].

Recently, in their study of structural and physical properties of $Eu_3Pd_2Sn_2$ and $Yb_3Pd_2Sn_2P$ compounds, Solokha *et al* [3] found that the results of powder X-ray diffraction at room temperature shows that these ternary compounds crystallize in orthorhombic structure *Pbcm (57)*, where lattice parameters are $a=0.60335$, $b=0.87554$, $c=1.41087\ nm$ for $Eu_3Pd_2Sn_2$, and $a=0.58262$, $b=1.68393, c=1.38735\ nm$ for $Yb_3Pd_2Sn_2$. The number of chemical formula per unit cell equals to 4 for $Eu_3Pd_2Sn_2$ and 8 for $Yb_3Pd_2Sn_2$. Moreover, the study shows that both compounds structure is composed of a polyanionic network $\infty[Pd_2Sn_2]^{\delta-}$ in which $Eu$ and $Yb$ ions are embedded. Thus, DC susceptibility and Mössbauer spectroscopic measurements show a close-to divalent $Yb$ ($Yb^{2+}$) and exact divalent $Eu$ ($Eu^{2+}$) behaviors. Moreover, DFT calculations, worked out by P.Solokha *et al*, showed $Yb_3Pd_2Sn_2$ compound metallic behavior. Concerning magnetic properties, $Yb_3Pd_2Sn_2$temperature dependence measurements of heat capacity show a simple behavior without tendency to magnetic ordering [3], thus $Yb_3Pd_2Sn_2$ compound is an ordinary metal with no sign of phase transition; on the other hand, for $Eu_3Pd_2Sn_2$, recent experimental work about new Eu-Pd-Sn Compounds done by Curlík *et al* [4], confirms the divalent behavior of Eu ions in $Eu_3Pd_2Sn_2$ compound and shows that the compound is magnetically ordered according to magnetic susceptibility measurement. Paramagnetic Weiss temperature was found to be negative (-5 K) and the magnetic moment equals to $7.95\mu_B$, close to the theoretical $Eu^{2+}$ free ion value $7.94\ \mu_B$.

In this paper, we calculate intermetallic compounds $Eu_3Pd_2Sn_2$ and Yb3Pd2Sn2, structural, electronic and magnetic properties. Density functional theory (DFT) [5], based on Linearized Augmented Plane Wave (LAPW) method, employed in wien2k code [6], were used to determine structural and electronic properties. The Local (spin) Density Approximation [7] L(S)DA was used as exchange and correlation potential. Moreover, simplest correction for DFT; L(S)DA+U approximation [8-9], was used. As a result; volume, bulk

modulus, first derivative of bulk modulus, $c/a$ fraction and $b/a$ ratio at equilibrium were computed; therefore, lattice parameters for each compound were concluded. The Self Consistent Field (SCF) was run to determine the density of states (DOS) and magnetic moments. LSDA and LSDA+U approximations were used to determine magnetic behavior of our compounds. For both compounds, we calculated the magnetic moments in Yb/Eu sites. In addition, Onsite Hybrid Functionals (HF) method [10] was used to compute DOS and magnetic moments in order to compare the used methods accuracies. For $Eu_3Pd_2Sn_2$ compound magnetic ground state, we suggested four antiferromagnetic configurations and one ferromagnetic configuration; for each configuration total energy versus volume were calculated using LSDA+U method and then the results were compared to predict the magnetic ground state.

2. Computational methods:

2.1. DFT and WIEN2K code:

Quantum mechanics governs the electronic structure that is responsible for properties such as relative stability, chemical bonding, relaxation of the atoms, phase transitions, electrical, mechanical, optical or magnetic behavior, etc [11] ... In solids, Schrödinger's equation solution gives the main access to the electronic structure. Till now, the exact analytical solution of Schrödinger equations are only possible with the angular momentum $l$=0 for some potential models. However, when $l \neq 0$, the Schrödinger equation can only be solve approximately for some potential models [12]. The solution accuracy depends on these approximations. In Density Functional Theory (DFT), many-body problem of interacting electrons and nuclei is mapped to a series of one electron equations, the so-called Kohn-Sham (KS) equations. For KS equations solution, several methods have been developed, with linearized augmented plane wave (LAPW) method being among the most accurate [11]. Peter Blaha *et al* [13] developed the well known computer code WIEN2K (see www.wien2k.at ). WIEN2K implements the full-potential augmented plane wave plus local orbitals (APW+LO) and (LAPW+LO) methods based on DFT to calculate electronic structure in solids and then conclude its properties at 0 K temperature.

The Total Energy $E$ of an interacting inhomogeneous electron gas in the presence of an external potential (given by the nuclei) is a functional of the electron density $\rho$ [14].

$$
\begin{aligned}
E_{t o t}= & T_{s}[\rho]+\int V_{e x t} \rho(\vec{r}) d \vec{r}+\frac{1}{2} \iint \frac{\rho(\vec{r}) \rho\left(\vec{r}^{\prime}\right)}{\left|\vec{r}^{\prime}-\vec{r}\right|} d \vec{r} d \vec{r}^{\prime}+\sum_{\substack{A, B \\
A \neq B}} \frac{Z_{A} Z_{B}}{\left|R_{A}-R_{B}\right|} \\
& +E_{x c}[\rho] \ldots \ldots(1)
\end{aligned}
$$

The five terms correspond to the non-interacting electrons kinetic energy, the nucleus-electron electrostatic Coulomb energy $E_{n e}$, the electron-electron electrostatic Coulomb energy $E_{e e}$, the nucleus-nucleus electrostatic Coulomb energy $E_{n n}$ and the exchange-correlation energy $E_{x c}$,

Minimization of $E_{t o t}$ gives The Kohn-Sham (KS) Schrödinger equations: [14]
$$
\left[-\frac{1}{2} \nabla^{2}+V_{e x t}(\vec{r})+V_{c}[\rho(\vec{r})]+V_{x c}[\rho(\vec{r})]\right] \psi_{i}(\vec{r})=\varepsilon_{i} \psi_{i}(\vec{r}) \ldots \ldots(2),
$$

Where the terms of $\boldsymbol{E q . 2}$ from left to right are; the kinetic energy operator, the external potential from the nucleus, the electron-electron Coulomb potential, and the exchange-correlation $(X C)$ potential $V_{x c}$.

In the KS scheme, the electron density is obtained by summing over all occupied states,
$$
\rho(\vec{r})=\sum_{i}^{o c c}\left[\phi_{i}(\vec{r})\right]^{2} \ldots \ldots(3).
$$

To solve the (Eq.2), we need to know the term of exchange-correlation potential, so one need to make approximations. Modern approximations used in DFT are; general gradient approximation [15] (GGA), local density approximation (LDA). For the highly correlated systems, simple GGA and LDA become insufficient and it's better to use DFT+U approximation, which is a combination between a Hubbard U and LDA/GGA, for $f$-electrons or late transition metal d-orbitals [14]. In this approximation, the total energy is given by: [16]
$$
E_{D F T+U}[\rho]=E_{D F T}[\rho]+E_{U}\left[n_{m}^{I, \sigma}\right]-E_{d c}\left[n^{I, \sigma}\right] \ldots \ldots(4)
$$
where $E_{D F T}[\rho]$ is the DFT (LDA or GGA) energy term given by $\boldsymbol{E q . 1}$, $E_{U}\left[n_{m m^{\prime}}^{I, \sigma}\right]$ is the term that contains the Hubbard Hamiltonian to model correlated states, $n_{m}^{I, \sigma}$ is the atomic-orbital occupations with spin $\sigma$ for correlated atom $I$ and $E_{d c}\left[n^{I, \sigma}\right]$ is the double counting term that model the contribution of correlated electrons to DFT total energy.

Another approach is the hybrid functionals (HF). It includes onsite exactexchange (i.e., Hartree-Fock), which is very useful for strongly correlated systems [17]. For example, Moreira et al [18] proposed a hybrid functionals given by $\boldsymbol{E q . 5}$. For more details about $E_{X C}$ approximations, their accuracy and cost, one can see Jacob's ladder. [19]
$$
E_{x c}^{\text {onsite-hybrid }}[\rho]=E_{x c}^{L D A}[\rho]+\alpha\left(E_{x}^{h f}\left[\psi_{s e l}\right]-E_{x}^{L D A}\left[\rho_{s e l}\right]\right) \ldots \ldots(5)
$$
where $E_{x c}^{L D A}[\rho]$ is the LDA exchange-correlation energy functional term, $E_{x}^{h f}\left[\psi_{c o r r}\right]$ is the Hartree-Fock exact-exchange energy functional term, $E_{x}^{L D A}\left[\rho_{s e l}\right]$ is the LDA exchange energy functional term, $\rho$ is the electronic

density, $\psi_{sel}$ and $\rho_{sel}$ are the wave function and the corresponding electronic density of the selected electrons and $\alpha$ is a fraction.

### 2.2. Computational details:

This work is done using WIEN2K. We determined the structural and physical properties of our intermetallic compounds at 0 K, where the full potentials LAPW+LO and APW+LO based on DFT is employed. For the approximations, we used L(S)DA, L(S)DA+U and HF.

The following parameters of convergence was set to run the calculation under WIEN2K code and its kept constant for comparing accuracy between approximations used. The plane-wave cutoff was set to 8, defined by the product of the smallest atomic sphere radius times the magnitude of the largest reciprocal-lattice vector $R_{MT}*K_{MAX}$. The values of RMT (Radii of Muffin-Tin) were set to 2.50 *au* (atomic unit) for Yb, 2.27 *au* for both Pd and Sn in $\text{Yb}_3\text{Pd}_2\text{Sn}_2$, and 2.50 *au* for Eu and 2.42 *au* for both Pd and Sn in $\text{Eu}_3\text{Pd}_2\text{Sn}_2$. The maximum $l$ value for partial waves used inside atomic spheres was set to $l_{\text{max}}$=10. The largest vector magnitude in the charge-density Fourier expansion $G_{\text{max}}$ was set to 12 $(a.u)^{-1}$. A k-mesh of 36 and 72 special k-points was generated for $\text{Yb}_3\text{Pd}_2\text{Sn}_2$ and $\text{Eu}_3\text{Pd}_2\text{Sn}_2$ respectively in the irreducible wedge of the Brillouin zone (IBZ); equivalent to 200 and 400 k-points for $\text{Yb}_3\text{Pd}_2\text{Sn}_2$ and $\text{Eu}_3\text{Pd}_2\text{Sn}_2$ respectively. The energy convergence criterion was set to 0.0001 Ry.

Since simple LDA can't describe sufficiently strong onsite correlation between Eu/Yb 4f-electrons, we use L(S)DA+U. For that, we estimated effective Coulomb interaction for Yb/Eu divalent state, $\text{U}_{eff}$ = U- J (Coulomb and exchange parameters, U and J), using constraint DFT method provided by Madsen and Novak [20]; where 4f-electrons are treated as core electrons to switch off any hybridization with other electrons. Accordingly, we break symmetry to treat atoms individually and modify the 4f-occupation numbers for one atom Yb/Eu, which considered as impurity, to add electron in one of two windows calculation and remove electron from the other. Thus, by setting the energy linearization far above Fermi level, the 4f-states were removed from the APWs basis at impurity sites. For our compounds, two calculation were performed with 1x1x1 supercells where the 4f configuration of the considered impurity atom was forced to satisfy equation *Eq.6* derived by Anisimov and Gunnarsson [14];

$$
\begin{aligned}
U_{e f f}= & \left\{\epsilon_{4 f \uparrow}[(n+1) / 2, n / 2]-\epsilon_{F}\left[\frac{n+1}{2}, \frac{n}{2}\right]\right\}-\left\{\epsilon_{4 f \uparrow}\left[\frac{n+1}{2}, \frac{n}{2}-1\right]-\right. \\
& \left.\epsilon_{F}\left[\frac{n+1}{2}, \frac{n}{2}-1\right]\right\} \ldots....(6)
\end{aligned}
$$

where each two terms in curly brackets refer to the difference between $4 f$ spin-up eigenvalue and Fermi energy for (n+1) and (n-1) configurations.

Table 1: Wyckoff positions and standardized atomic coordinates of $\mathrm{Yb}_{3} \mathrm{Pd}_{2} \mathrm{Sn}_{2}$ and $\mathrm{Eu}_{3} \mathrm{Pd}_{2} \mathrm{Sn}_{2}$ compounds. [3]

<table>
<thead>
  <tr>
    <th>Compound</th>
    <th>Atom</th>
    <th>Wyckoff position</th>
    <th>x/a</th>
    <th>y/b</th>
    <th>z/c</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td rowspan="10">$\boldsymbol{Yb_3Pd_2Sn_2}$</td>
    <td>Pd1</td>
    <td>8e</td>
    <td>0.019</td>
    <td>0.3517</td>
    <td>0.0903</td>
  </tr>
  <tr>
    <td>Yb1</td>
    <td>8e</td>
    <td>0.196</td>
    <td>0.6778</td>
    <td>0.0981</td>
  </tr>
  <tr>
    <td>Pd2</td>
    <td>8e</td>
    <td>0.281</td>
    <td>0.1146</td>
    <td>0.0889</td>
  </tr>
  <tr>
    <td>Yb2</td>
    <td>8e</td>
    <td>0.505</td>
    <td>0.4296</td>
    <td>0.0973</td>
  </tr>
  <tr>
    <td>Yb3</td>
    <td>4d</td>
    <td>0.004</td>
    <td>0.5108</td>
    <td>¼</td>
  </tr>
  <tr>
    <td>Yb4</td>
    <td>4d</td>
    <td>0.295</td>
    <td>0.2437</td>
    <td>¼</td>
  </tr>
  <tr>
    <td>Sn1</td>
    <td>4d</td>
    <td>0.503</td>
    <td>0.0650</td>
    <td>¼</td>
  </tr>
  <tr>
    <td>Sn2</td>
    <td>4d</td>
    <td>0.209</td>
    <td>0.8275</td>
    <td>¼</td>
  </tr>
  <tr>
    <td>Sn3</td>
    <td>4c</td>
    <td>0.308</td>
    <td>¼</td>
    <td>0</td>
  </tr>
  <tr>
    <td>Sn4</td>
    <td>4a</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <td rowspan="5">$\boldsymbol{Eu_3Pd_2Sn_2}$</td>
    <td>Eu1</td>
    <td>8e</td>
    <td>0.147</td>
    <td>0.108</td>
    <td>0.0979</td>
  </tr>
  <tr>
    <td>Eu2</td>
    <td>4d</td>
    <td>0.643</td>
    <td>0.251</td>
    <td>1/4</td>
  </tr>
  <tr>
    <td>Sn1</td>
    <td>4d</td>
    <td>0.638</td>
    <td>¼</td>
    <td>0</td>
  </tr>
  <tr>
    <td>Sn2</td>
    <td>4d</td>
    <td>0.154</td>
    <td>0.397</td>
    <td>1/4</td>
  </tr>
  <tr>
    <td>Pd1</td>
    <td>8e</td>
    <td>0.383</td>
    <td>0.4678</td>
    <td>0.0877</td>
  </tr>
</tbody>
</table>

After fixing effective U, we used calculated values in the Eu/Yb sites on to apply LSDA+U calculation on $4 f$ orbitals. For the double counting correction, we chose the methods called 'around mean field' (AMF) [21] and 'self interaction-correction' (SIC) [22-23] for $\mathrm{Yb}_{3} \mathrm{Pd}_{2} \mathrm{Sn}_{2}$ and $\mathrm{Eu}_{3} \mathrm{Pd}_{2} \mathrm{Sn}_{2}$ compounds respectively. The HF approximation was applied on Yb/Eu $4 f$ orbitals only, where LDA exchange was replaced by the exact exchange and the Hartree-Fock exchange fraction was set to be 0.25 for both compounds (see WIE2k user guide).

![](./images/812746361601523712_2.jpg)

Figure.1: (a): unit cell of $\text{Yb}_3\text{Pd}_2\text{Sn}_2$ compound, and (b); unit cell of $\text{Eu}_3\text{Pd}_2\text{Sn}_2$, compound previewed by xcrysden package [24].

## 3. Results and discussion:
### 3.1. The effective Coulomb interaction U:

According to constraint DFT described previously, the results gave 5.96 and 6.66 eV for $\text{Eu}^{2+}$ and $\text{Yb}^{2+}$ respectively. Taking into account screening effect of 6s and 5p electrons on 4f electrons, which reduce the effective U defined by Anisimov and Gunnarsson [14], as the energy cost to move one 4f-electron between two atoms, calculated values in this work are generally acceptable. For $\text{Eu}^{2+}$, we don't know previous values for effective U to compare with ours, however, for $\text{Eu}^{3+}$ we have found the following values; 9.12 [25] and 10 eV [26]. It has been found that effective U increase with the iconicity, [25] accordingly, our calculated value is in agreement. For $\text{Yb}^{2+}$, the experimental value of effective U must be in the range of 5-6 eV according to the photoemission experiment [24]. Moreover, a previous calculation was done by Antonov *et al* [27] gave 5.3 eV. In this work, effective U of $\text{Yb}^{2+}$ is overestimated by 10 to 33 %.

### 3.2. Structural properties:

Total energy determines materials properties, once the energy computed, other properties can be calculated [28]. Volume and lattice parameters are the

closest parameters related to total energy [29]; they can be derived from material equilibrium minimum energy. In order to calculate our compounds lattice parameters, three steps were done for both compounds using lattice parameters experimental results [3]. First, we determined volume at equilibrium by calculating total energy versus volume and using the results to fit Murnaghan's equation of state (EOS) (Eq.7) [30]. Bulk modulus B (Eq.8) and its first derivative B` also were calculated in this step. Second, we determined equilibrium $b/a$ ratio by calculating total energy versus $b/a$ ratio at constant volume and $c/a$ ratio. Third, we repeated the second one but for $c/a$ ratio at constant volume and $b/a$ ratio.

$$
E(V)=\frac{B V}{B^{\prime}}\left[\frac{\left(V_{0} / V\right)^{B^{\prime}}}{B^{\prime}-1}-1\right]+\frac{B_{0} V_{0}}{B_{0}{ }^{\prime}-1} \ldots \ldots \ldots(7)
$$

$$
B=V \frac{\partial^{2} E}{\partial V^{2}} \ldots \ldots \ldots(8)
$$

The volume at equilibrium is given by:

$$
V=\left(\frac{c}{a}\right) \cdot\left(\frac{b}{a}\right) \cdot a^{3} \quad \ldots \ldots \ldots \ldots(9)
$$

where $c/a$ and $b/a$ are the optimized ratios at equilibrium.

We report the results of optimization in Fig.2, Fig.3, Fig.4 and Table.2. Since it is well known that LDA approximation underestimates the cell unit volume and lattice parameters [31], our results are generally acceptable.

Table2: Calculated lattice parameters of intermetallic compounds $\mathrm{Yb}_{3} \mathrm{Pd}_{2} \mathrm{Sn}_{2}$ and $\mathrm{Eu}_{3} \mathrm{Pd}_{2} \mathrm{Sn}_{2}$, Bulk modulus $\mathrm{B}$ and its first derivative B' using LDA, LSDA and LSDA+U methods, where $\mathrm{U}=5.96$ and $\mathrm{U}=6.66 \mathrm{eV}$ for $\mathrm{Eu}$ and $\mathrm{Yb}$ respectively. * Experimental results [3].

<table>
<thead>
<tr>
<th>Compound</th>
<th>Method</th>
<th>$V(nm^{3})$</th>
<th>c/a</th>
<th>b/a</th>
<th>a (nm)</th>
<th>b (nm)</th>
<th>c (nm)</th>
<th>B (GPa)</th>
<th>B'</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="4">Yb₃Pd₂Sn₂</td>
<td>EXP</td>
<td>1.3611</td>
<td>2.381</td>
<td>2.89</td>
<td>0.58262</td>
<td>1.68393</td>
<td>1.38735</td>
<td>/</td>
<td>/</td>
</tr>
<tr>
<td>LDA</td>
<td>1.265</td>
<td>2.388</td>
<td>2.921</td>
<td>0.56603</td>
<td>1.65338</td>
<td>1.35169</td>
<td>85.27</td>
<td>5.39</td>
</tr>
<tr>
<td>LSDA</td>
<td>1.2671</td>
<td>2.392</td>
<td>2.918</td>
<td>0.56622</td>
<td>1.65224</td>
<td>1.35441</td>
<td>84.12</td>
<td>5.05</td>
</tr>
<tr>
<td>LSDA+U</td>
<td>1.2656</td>
<td>2.386</td>
<td>2.924</td>
<td>0.56609</td>
<td>1.65524</td>
<td>1.35068</td>
<td>85.27</td>
<td>5.39</td>
</tr>
<tr>
<td rowspan="3">Eu₃Pd₂Sn₂</td>
<td>EXP</td>
<td>0.74521</td>
<td>2.338</td>
<td>1.451</td>
<td>0.60335</td>
<td>0.87554</td>
<td>1.41087</td>
<td>/</td>
<td>/</td>
</tr>
<tr>
<td>LDA</td>
<td>0.63931</td>
<td>2.329</td>
<td>1.451</td>
<td>0.57406</td>
<td>0.83296</td>
<td>1.33699</td>
<td>91.28</td>
<td>5.14</td>
</tr>
<tr>
<td>LSDA+U</td>
<td>0.67266</td>
<td>2.331</td>
<td>1.47</td>
<td>0.58125</td>
<td>0.85431</td>
<td>1.35471</td>
<td>78.76</td>
<td>5.45</td>
</tr>
</tbody>
</table>

For $Yb_3Pd_2Sn_2$ compound, underestimated volume and lattice parameters depend slightly on the used method, the three methods gave almost the same result, with a relatively better precision for LSDA method (see **Table.3**); the absolute error depends weakly on the used method. While LDA+U approach overcomes some major deficiencies of LDA such as metallic solution for Mott insulators, it is still a one-electron method because it is based on static mean-filed approximation. It completely fails for strongly correlated metals where electrons reveal simultaneously localized and itinerant properties [3]. For $Eu_3Pd_2Sn_2$ compound, simple LDA and LDA+U methods didn't give result, however LSDA+U gave a better result than LSDA. For bulk modulus and its first derivative we don't found previous values to compare with ours. For the bulk modulus and its first derivative, we don't know experimental results to compare it with.

Table3: Absolute error on calculating structural properties of intermetallic compounds $Yb_3Pd_2Sn_2$ and $Eu_3Pd_2Sn_2$.

<table>
  <thead>
    <tr>
      <th rowspan="2">Compound</th>
      <th colspan="7">Absolute error (%)</th>
    </tr>
    <tr>
      <th>Method</th>
      <th>V</th>
      <th>c/a</th>
      <th>b/a</th>
      <th>A</th>
      <th>b</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3">$Yb_3Pd_2Sn_2$</td>
      <td>LDA</td>
      <td>7.061</td>
      <td>0.294</td>
      <td>1.073</td>
      <td>2.847</td>
      <td>1.814</td>
      <td>2.57</td>
    </tr>
    <tr>
      <td>LSDA</td>
      <td>6.906</td>
      <td>0.462</td>
      <td>0.969</td>
      <td>2.815</td>
      <td>1.882</td>
      <td>2.374</td>
    </tr>
    <tr>
      <td>LSDA+U</td>
      <td>7.016</td>
      <td>0.21</td>
      <td>1.176</td>
      <td>2.837</td>
      <td>1.704</td>
      <td>2.643</td>
    </tr>
    <tr>
      <td rowspan="2">$Eu_3Pd_2Sn_2$</td>
      <td>LSDA</td>
      <td>14.21</td>
      <td>0.385</td>
      <td>0</td>
      <td>4.855</td>
      <td>4.863</td>
      <td>5.236</td>
    </tr>
    <tr>
      <td>LSDA+U</td>
      <td>9.736</td>
      <td>0.299</td>
      <td>1.309</td>
      <td>3.663</td>
      <td>2.425</td>
      <td>3.981</td>
    </tr>
  </tbody>
</table>

![](./images/812746361601523712_3.jpg)

Figure.2: (a), (b) and (c); variation of total energy versus volume, $c/a$ ratio and $b/a$ ratio respectively for Yb₃Pd₂Sn₂ compound using LDA method.

![](./images/812746361601523712_4.jpg)

Figure.3: (a), (b) and (c); variation of total energy versus volume, $c/a$ ratio and $b/a$ ratio respectively for Yb₃Pd₂Sn₂ compound. (d), (e) and (f); variation of total energy versus volume, $c/a$ ratio and $b/a$ ratio respectively for Eu₃Pd₂Sn₂ compound using LSDA method.

![](./images/812746361601523712_5.jpg)

Figure.4: (a), (b) and (c); variation of total energy versus volume, $c/a$ ratio and $b/a$ ratio respectively for Yb₃Pd₂Sn₂ compound. (d), (e) and (f); variation of total energy versus volume, $c/a$ ratio and $b/a$ ratio respectively for Eu₃Pd₂Sn₂ compound using L(S)DA+U method. Where U = 6.66 and 5.96 eV for Yb and Eu respectively.

### 3.3. Density of states DOS:

Fig.5 and 6 show total and projected density of states (DOS) for both compounds. Results show that Fermi level (dotted axis) is located in a continuous DOS region (valence band VB), indicating that our compounds have a metallic character. For Yb₃Pd₂Sn₂ compound, spin up DOS and spin down DOS are equals, which correspond to non magnetic case. Moreover, we remark a Yb states cusp near Fermi level which means $c$-$f$ hybridization presence and hybridization between Yb $4f$ electrons ($[Xe] \ 4f^{14}6s^2$) and conduction electrons. Using LSDA+U method, this cusp is found to be under Fermi level (about -1.5 eV). For Eu₃Pd₂Sn₂ compound, spin up DOS and spin down DOS are not equals, the energy difference between exchange-splitting of the Eu-$4f$ states being about 4.5 eV using both LSDA and HF methods and 10.5 eV using LSDA+U method; such results exhibit a magnetic case. Similarly to Yb states, a distinct cusp of Eu ($[Xe] \ 4f^76s^2$) up states around Fermi level means presence of $c$-$f$ hybridization between Eu $4f$ electrons and conduction electrons in Eu₃Pd₂Sn₂ compound. This cusp lies under Fermi level (about -1.5 eV) using LSDA+U method. For both

compounds, at energies $E < -1\ eV$, palladium and tin contribute mainly to the VB revealing chemical bonds between Pd and Sn.

LSDA+U method fails to describe $c$-$f$ hybridization of Yb/Eu electrons. To a certain extent, our calculation gives the same result as for $\text{Yb}_3\text{Pd}_2\text{Sn}_2$ compound published by *P.Solokha et al* [3]. However, for $\text{Eu}_3\text{Pd}_2\text{Sn}_2$, we did not find previous DOS calculation to compare with. Similar contribution of Eu ions in the DOS is seen in *C.Felser et al* [33] work about $EuPdP$ compound.

![](./images/812746361601523712_6.jpg)

Figure.5: Total and projected density of states of $\text{Yb}_3\text{Pd}_2\text{Sn}_2$ compound using LDA (A), LSDA (B), LSDA+U (C) and HF (D) methods. The top right plots in every figure were made to show small DOS. LSDA+U was performed using U = 6.66 eV for Yb ions. $E_f$ presents Fermi level.

![](./images/812746361601523712_7.jpg)

Figure.6: Total and projected density of states of Eu₃Pd₂Sn₂ compound using LSDA (A), LSDA+U (B) and HF (C) methods. The top right plots in every figure were made to show small contributions in DOS. LSDA+U was performed using $U = 5.96$ eV for Eu ions. $E_f$ presents Fermi level.

### 3.4. Magnetic properties:

Total magnetic moment in unit cell and Yb/Eu ions magnetic moment of both compounds are shown in Table.4. Yb ions in Yb₃Pd₂Sn₂ compound magnetic moment and unit cell total magnetic moment are almost null. Since only $\text{Yb}^{3+}$ has magnetic behavior, Yb is in divalent states in all crystallographic sites. These results agree with magnetic measurements reported by Solokha *et al* [3]. For Eu₃Pd₂Sn₂ compound, calculated Eu ions magnetic moment has smaller value than experimental one ($7.94\ \mu_B$) [4]. We note also that these results depend on the used method; the most accurate one is HF method.

For Eu₃Pd₂Sn₂ compound magnetic ground state, we computed minimum energy by optimizing equilibrium volume for ferromagnetic (FM) and four AFM configurations using LDA+U method as shown in Fig.6. The results are summarized in Fig.7. Accordingly, a FM magnetic ground state was achieved. Both AFM1 and AFM2 configurations give the same results; their energies are greater than FM configuration energy by less than 0.1 Ry.

<table>
<caption>Table 4: magnetic moment in unit cell and atomic magnetic moment of Yb/Eu ions in Yb₃Pd₂Sn₂ and Eu₃Pd₂Sn₂ compounds. For LSDA+U method, U was set to be 6.66 and 5.96 eV for Yb and Eu sites respectively.</caption>
<thead>
<tr>
<th rowspan="2">Compound</th>
<th rowspan="2">site</th>
<th colspan="3">Magnetic moment</th>
<th colspan="3">Magnetic moment in cell</th>
<th colspan="3">Interstitial magnetic moment</th>
</tr>
<tr>
<th>LSDA</th>
<th>LSDA+U</th>
<th>HF</th>
<th>LSDA</th>
<th>LSDA+U</th>
<th>HF</th>
<th>LSDA</th>
<th>LSDA+U</th>
<th>HF</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="4">Yb₃Pd₂Sn₂</td>
<td>Yb1</td>
<td>0.001</td>
<td>0.001</td>
<td>-0.000</td>
<td rowspan="4">-0.01</td>
<td rowspan="4">0.03</td>
<td rowspan="4">-0.00</td>
<td rowspan="4">0.00</td>
<td rowspan="4">0.02</td>
<td rowspan="4">-0.00</td>
</tr>
<tr>
<td>Yb2</td>
<td>0.000</td>
<td>-0.000</td>
<td>-0.000</td>
</tr>
<tr>
<td>Yb3</td>
<td>-0.000</td>
<td>-0.000</td>
<td>-0.000</td>
</tr>
<tr>
<td>Yb4</td>
<td>-0.004</td>
<td>0.001</td>
<td>-0.000</td>
</tr>
<tr>
<td rowspan="2">Yb₃Pd₂Sn₂</td>
<td>Eu1</td>
<td>6.663</td>
<td>6.898</td>
<td>6.92</td>
<td rowspan="2">83.12</td>
<td rowspan="2">85.22</td>
<td rowspan="2">84.81</td>
<td rowspan="2">3.5</td>
<td rowspan="2">2.74</td>
<td rowspan="2">2.17</td>
</tr>
<tr>
<td>Eu2</td>
<td>6.644</td>
<td>6.887</td>
<td>6.913</td>
</tr>
</tbody>
</table>

Till now, the magnetic ground state of our compound is not determined; Curlík et al [4] proved that the title compound has a complicated magnetic ground state. Since WIEN2k can handle only with collinear magnetism, it is not possible to determine the exact magnetic ground state of our compound.

![](./images/812746361601523712_8.jpg)

Figure.6: antiferromagnetic configurations of Eu₃Pd₂Sn₂ compounds. In the ferromagnetic configuration, all Eu atoms have a spin up magnetic moment. The figures were generated using VESTA package [34].

![](./images/812746361601523712_9.jpg)

Figure.7: total energy versus volume for AFM configurations of Eu₃Pd₂Sn₂ compound using LSDA+U method, where U = 5.96 eV for Eu ions.

### 4. Conclusion:

Both compounds $Re_3Pd_2Sn_2$ ($Re = Yb, Eu$) crystallized in the orthorhombic space group $Pbcm$. The calculated lattice parameters are found to be close to the available experimental ones. Thus, for both compounds, bulk modulus and its first derivative are predicted. Estimated coulomb interaction parameter U for Eu and Yb ions in their divalent state are found equal to 5.96 and 6.66 eV respectively. The density of states proves that both compounds have a metallic behavior with existing of a $c$-$f$ hybridization between $Re$ $4f$ electrons and conduction electrons. According to spin up and spin down density of states, the $Yb_3Pd_2Sn_2$ compound has no magnetic behavior however the $Eu_3Pd_2Sn_2$ one has. The atomic magnetic moment found equal to zero for Yb ions and about $6.9\ \mu_B$ for Eu ions which is less than experimental one. At the end, we state that the ferromagnetic fundamental magnetic state found by our calculations doesn't correspond to the expected magnetic ground state, so more calculations are needed to determine the magnetic ground state of $Eu_3Pd_2Sn_2$ compound.

---

### References

[1] J. Westbrook, R. Fleischer]. Intermetallic Compounds, principles and practice. Volume3. JOHN WHLEY & SONS, LTD.

[2] P.Wachter, H.Boppart, (Eds.), in: Proceeding sof the International Conference On ValenceInstabilties,Z¨urich, Amsterdam,North-Holland,1982.

[3] P. Solokha , Curlik, M.Giovannini, N.R.Lee-Hone, M.Reiffers, D.H.Ryan, A.Saccone. Journal of Solid State Chemistry. 184(2011)2498-2505.

[4] I. Curlík, F. Gastaldo, M. Giovannini, A.M. Strydom and M. Reiffers. ACTA PHYSICA POLONICA A. Vol. 131 (2017).

[5] W. Kohn, L.J. Sham, Phys. Rev. A 140 (1965) 1133-1138.

[6] P. Blaha, K. Schwarz, G.K.H. Madsen, D. Kvasnicka, J. Luitz. University of Technology, Vienna, Austria, 2001.

[7] J.P. Perdew, Y. Wang, Phys. Rev. B 45 (1992) 13244.

[8] J. Hubbard, Proc. Roy. Soc. Lond. A 276, 238 (1963)

[9] J. Hubbard, Proc. Roy. Soc. Lond. A 296, 100 (1966)

[10] Tran F., Blaha P., Schwarz K. and Novak P.. Phys Rev B, 74:155108. 11, 48, 121(2006).

[11] K. Schwarza, P. Blahaa and S.B. Trickey. Molecular Physics. Vol. 108, 21-23, 3147-3166 (2010).

[12] Louis E. Akpabio. Applied Physics Research. Vol. 2, No. 2; November 2010.

[13] P. Blaha, K. Schwarz, G.K.H. Madsen, D. Kvasnicka, J. Luitz, An augmented plane wave plus local orbitals program for calculating crystal properties, Vienna University of Technology, Austria (2001) ISBN 3-9501031-1-2.

[14] W. Kohn and L.S. Sham, Phys. Rev. 140, A1133 (1965).

[15] J.P. Perdew, K. Burke and M. Ernzerhof, Phys. Rev. Lett. 77, 3865 (1996).

[16] Burak Himmetoglu, Andrea Floris, Stefano de Gironcoli, and Matteo Cococcioni. International Journal of Quantum Chemistry 2014, 114, 14-49. DOI: 10.1002/qua.24521.

[17] Tran, F, Blaha P, Schwarz K, and Novak P. Phys. Rev. B 74, 155108. (2006).

[18] I. de P. R. Moreira, F. Illas, and R. L. Martin, Phys. Rev. B 65, 155102 (2002).

[19] J. P. Perdew et al., J. Chem. Phys. 123, 062201 (2005).

[20] Madsen G K H and Novak P. Phys Lett 69 777-83 (2004).

[21] Czyzyk, M. T. and Sawatzky, G. A. (1994). Phys. Rev. B 49, 14211. 120.

[22] V.I. Anisimov, I.V. Solovyev, M.A. Korotin, M.T. Czyzyk, and G.A. Sawatzky, Phys. Rev. B 48, 16 929 (1993).

[23] A. I. Liechtenstein, V. I. Anisimov and J. Zaanen. Phys. Rev. B 52, 5467 (1995).

[24] A. Kokalj, J. Mol. Graphics Modelling 17, 176 (1999).

[25] Sandeep, DP. Rai, A. Shankar, MP. Ghimire, R. Khenata and R K Thapa. Phys. Scr. 90 (2015) 065803 (8pp). https://doi:10.1088/0031-8949/90/6/065803.

[26] J. F. Herbst and J. W. Wilkins, in Handbook of the Physics and Chemistry of Rare Earths, edited by K. A. Gschneidner, L. Eyring, and S. Hufner. North-Holland, Amsterdam, 1987, Vol. 10, p. 321.

[27] V. N. Antonov, A. N. Yaresko, A. Ya. Perlov, P. Thalmeier, and P. Fulde. The American Physical Society, 1998. 0163 1829/98/58(15)/9752(11).

[28] Yildirim.Aa, Koc.Ha, and Deligoz.Eb. Chin. Phys. B Vol. 21, No. 3 (2012) 037101.

[29] Karlheinz Schwarz. Journal of Solid State Chemistry 176 (2003) 319-328.

[30] F.D. Murnaghan, Proc. Natl. Acad. Sci. U. S. A. 30 (1944) 244-247.

[31] Moufdi Hadjab, Smail Berrah, Hamza Abid, Mohamed Issam Ziane, Hamza Bennacer, Battal Gazi Yalcin. Optik 127 (2016) 9280-9294.

[32] V. Anisimov, Y. Izyumov. Electronic Structure of Strongly Correlated Materials. DOI: https://doi.org/10.1007/978-3-642-04826-5.

[33] C. Felser, S. Cramm, D. Johrendt, A. Mewis, O. Jepsen, G. Hohlneicher, W. Eberhardt and O. K. Andersen. Europhys. Lett., 40 (1), pp. 85-91 (1997).

[34] K. Momma and F. Izumi. J. Appl. Crystallogr, 44, 1272-1276 (2011).
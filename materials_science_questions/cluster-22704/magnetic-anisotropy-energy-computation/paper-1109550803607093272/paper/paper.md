# Magnetoelasticity - magnetic structure interrelation – tetragonal MnPt system study

Jakub Šebesta$^{a}$, Karol Synoradzki$^{b}$, Michal Vališka$^{c}$, Tetiana Haidamak$^{c}$, Tamara J. Bednarchuk$^{d}$, Pablo Nieves$^{e}$, Dominik Legut$^{c,a}$

$^{a}$IT4Innovations, VSB – Technical University of Ostrava, 17. listopadu 2172/15, Ostrava, 708 00, Czech Republic
$^{b}$Institute of Molecular Physics, Polish Academy of Sciences, Smoluchowskiego 17, Poznań, 60-179, Poland
$^{c}$Charles University, Faculty of Mathematics and Physics, Ke Karlovu 3, Praha 2, 121 16, Czech Republic
$^{d}$Institute of Low Temperature and Structure Research, Polish Academy of Sciences, Okólna 2, Wrocław, 50-422, Poland
$^{e}$Departamento de Física, Universidad de Oviedo, C. Leopoldo Calvo Sotelo, 18, Oviedo, 33007, Spain

---

## Abstract
Magnetic materials represent an essential ingredient for the contemporary industry. Apart from common material parameters such as magnetocrystalline anisotropy, coercivity, or saturation magnetization, magnetoelastic behavior is vital for applications serving in various devices, *e.g.*, in acoustic actuators, transducers, or sensors providing a desirable fast response and high efficiency with respect to applied magnetic field. Magnetoelastic properties have been studied for ferromagnetic 3d elements, or especially in high symmetry systems containing rare-earth elements to achieve higher values. Since, unlike for rare earth Laves phases, in the transition metals or alloys, these effects are very weak. Here, in contrast, we analyze the magnetoelastic behavior of antiferromagnetic tetragonal system MnPt, explaining the experimentally measured data based on the theoretical calculations and discussing the influence of the magnetic structure. Particularly, we inspect the origin of magnetocrystalline anisotropy energy, as well as the size and source of the isotropic and anisotropic parts of magnetoelastic (magnetostriction) coefficients.

**Keywords:** magnetoelasticity, magnetostriction, antiferromagnet, ab-initio, MnPt, dilatometry

---

## 1. Introduction
The mechanical properties of the material are important for practical applications. However, for magnetic materials, high complexity emerges due to the coupling of magnetic and elastic properties, giving rise to the so-called magnetoelastic behavior [1]. There exist various kinds of magnetoelastic effects, *e.g.* volume and axial magnetostriction or Wiedemann effect, bringing many useful applications. Thereby, magnetoelastic effects can take place in force sensors, low-frequency weak-field detectors, fast pulse generators, rotational and linear motors, or magneto-acoustically driven low-energy demanding electronics [2, 3, 4, 5, 6]. Magnetoelasticity arises from the mutual relation between deformation of crystal lattice and the magnetocrystalline anisotropy. In the present work, we focus by ab-initio calculations on the interrelation between magnetic structure and magnetic properties of MnPt system. Magnetoelastic behavior, which stems from an interplay between the magnetic and elastic properties, substantially differs among the magnetic compounds. The MnPt might bear interesting properties as it belongs to the family of Pt-based tetragonal systems [7, 8], where a large magnetocrystalline anisotropy occurs [9]. It comes

Email address: jakub.sebesta@vsb.cz (Jakub Šebesta)

from the interplay of Pt strong spin-orbit coupling (SOC) with spin moments of the $3d$-elements [10, 11, 12, 13]. At room temperature, MnPt forms the L1₀ phase [14, 15, 13, 16]. It was found that such an Mn-based two-component alloy possesses surprisingly high Néel temperature ($T_N >$900 K) [17, 13, 15, 16]. The antiferromagnetic ordering of Mn-based systems arises from around half-filled Mn $d$-states [14] and the magnetic structure of MnPt is characterized by [001] Néel vector [15]. MnPt magnetic properties are useful in tunnel magnetoresistance devices [18, 19] or for spin-valve structures with giant magnetoresis- tance [20, 21, 14]. Besides, the MnPt $a$ lattice parameter is close to the Fe or MgO ones, which makes MnPt interesting for creating interfaces with those constituents [22].

In this work, we investigate the impact of different magnetic structures on the magnetoelastic behavior based on ab-initio calculations and explain the experimental behavior of a prepared MnPt sample employing ab-initio results and atomistic spin simulations. Unlike recent papers, it includes a description of antiferromagnetic systems. The calculated results reveals a substantial modifications of the magnetoelasticity with respect to the considered magnetic structures. We analyze the origin of the observed changes investigating modifications in magnetocrystalline anisotropy and charge density.

## 2. Theory

Magnetostriction describes deformations of the material dimensions in response to external magnetic field. It has two contributions, the anisotropic magnetostriction originating from the dependence of magnetocrystalline anisotropy and the isotropic volume one based on the isotropic exchange interactions.

Small deformations in solids are described by a strain tensor [23]

$$
\varepsilon_{i j}=\frac{1}{2}\left(\frac{\partial u_{i}}{\partial r_{j}}+\frac{\partial u_{j}}{\partial r_{i}}\right), \tag{1}
$$

where $\mathbf{u}(r)=\mathbf{r}^{\prime}-\mathbf{r}$ denotes a displacement vector. The magnetostriction can be expressed by the magnetization given change of the length of an originally demagnetized material [24, 25, 1]

$$
\left.\frac{l-l_{0}}{l}\right|_{\boldsymbol{\beta}} ^{\boldsymbol{\alpha}}=\sum_{i, j=x, y, z} \varepsilon_{i j}^{e q} \beta_{i} \beta_{j}, \tag{2}
$$

where $l_0$ denotes the length along the $\boldsymbol{\beta}$ direction of a demagnetized sample and $l$ is the length in the same direction when the sample is magnetized along the $\boldsymbol{\alpha}$ direction. The equilibrium strain tensor $\varepsilon_{i j}^{e q}$ comes from a minimization of the sum of the elastic energy $E_{el}$ and magnetoelastic energy $E_{me}$ with the strain [26, 1, 27]

$$
\frac{\partial\left(E_{e l}+E_{m e}\right)}{\partial \varepsilon_{i j}^{e q}}=0. \tag{3}
$$

Performing the energy minimization with respect to the strain, the magnetostriction given by magnetizing a sample, *e.g.* by an external field, can be obtained. The relative length change at the equilibrium strain in the tetragonal (I) system follows [24]

$$
\begin{aligned}
& \left.\frac{\Delta l}{l_{0}}\right|_{\boldsymbol{\beta}} ^{\boldsymbol{\alpha}}=\lambda^{\alpha 1,0}\left(\beta_{x}^{2}+\beta_{y}^{2}\right)+\lambda^{\alpha 2,0} \beta_{z}^{2} \\
& +\lambda^{\alpha 1,2}\left(\alpha_{z}^{2}-\frac{1}{3}\right)\left(\beta_{x}^{2}+\beta_{y}^{2}\right)+\lambda^{\alpha 2,2}\left(\alpha_{z}^{2}-\frac{1}{3}\right) \beta_{z}^{2} \\
& +\frac{1}{2} \lambda^{\gamma, 2}\left(\alpha_{z}^{2}-\alpha_{y}^{2}\right)\left(\beta_{x}^{2}-\beta_{y}^{2}\right)+2 \lambda^{\delta, 2} \alpha_{x} \alpha_{y} \beta_{x} \beta_{y} \\
& +2 \lambda^{\varepsilon, 2}\left(\alpha_{x} \alpha_{z} \beta_{x} \beta_{z}+\alpha_{y} \alpha_{z} \beta_{y} \beta_{z}\right),
\end{aligned}
$$

where the magnetostrictive coefficients $\lambda = \lambda(b_i, C_{ij})$ (Eqs. B.6-B.12) are functions of the elastic coefficients $C_{ij}$ (Eq. B.1) and magnetoelastic constants $b_i$ (Eq. B.3) [28]. The first two $\lambda$ coefficients describe the volume magnetostriction, whereas the rest ones are related to the magnetization direction dependent anisotropic magnetostriction.

This theoretical description was originally derived for a FM phase, however is it valid also for the assumed collinear AFM phases. The AFM structure can be split into two antiparallel FM sublattices $\mu=\{A,B\}$, whose magnetoelastic energy satisfy [29]

$$
E_{m e}^{\text {total }}=E_{m e}^{A}\left(\alpha_{A}\right)+E_{m e}^{B}\left(\alpha_{B}\right) ; \quad \alpha_{A}=-\alpha_{B}, \quad(5)
$$

$$
\begin{aligned}
& \frac{1}{V_{0}} E_{m e}^{\mu}=b_{11}^{\mu}\left(\varepsilon_{\mathrm{xx}}+\varepsilon_{\mathrm{yy}}\right)+b_{12}^{\mu} \varepsilon_{\mathrm{zz}} \\
& +b_{21}^{\mu}\left(\alpha_{z, \mu}^{2}-\frac{1}{3}\right)\left(\varepsilon_{\mathrm{xx}}+\varepsilon_{\mathrm{yy}}\right)+b_{22}^{\mu}\left(\alpha_{z, \mu}^{2}-\frac{1}{3}\right) \varepsilon_{\mathrm{zz}} \\
& +\frac{1}{2} b_{3}^{\mu}\left(\alpha_{x, \mu}^{2}-\alpha_{y, \mu}^{2}\right)\left(\varepsilon_{\mathrm{xx}}-\varepsilon_{\mathrm{yy}}\right)+2 b_{3}^{\prime \mu} \alpha_{x, \mu} \alpha_{y, \mu} \varepsilon_{\mathrm{xy}} \\
& +2 b_{4}^{\mu}\left(\alpha_{x, \mu} \alpha_{z, \mu} \varepsilon_{\mathrm{xz}}+\alpha_{y, \mu} \alpha_{z, \mu} \varepsilon_{\mathrm{yz}}\right).
\end{aligned}
\tag{6}
$$

Thanks to the opposite spin direction $(\alpha_A = -\alpha_B)$, the magnetoelastic energies of the sublattice A and B are same
$$
E_{m e}^{A}\left(\alpha_{A}\right)=E_{m e}^{A}\left(-\alpha_{A}\right)=E_{m e}^{B}\left(\alpha_{A}\right),
\tag{7}
$$
which yields for the magnetoelastic constants $b_i$
$$
b_{i}=2 b_{i}^{A}=2 b_{i}^{B}
\tag{8}
$$
assuming scaling to the total volume $V_0$.

Considering a polycrystal, a mean fractional length change between an initial state and a saturated final state can be evaluated by averaging through the magnetization directions. It yields relations as follows
$$
\left\langle\left. \frac{l-l_{0}}{l}\right|_{\boldsymbol{\beta}} ^{\boldsymbol{\alpha}}\right\rangle=\xi+\eta(\boldsymbol{\alpha} \cdot \boldsymbol{\beta})^{2},
\tag{9}
$$
where the form of $\xi$, $\eta$ parameters depends on the initial demagnetized state [30]. Assuming an initial state with domains aligned along the easy direction, the $\xi$ and $\eta$ parameters are given as follows
$$
\begin{aligned}
\xi= & \frac{4}{15} \lambda^{\alpha 1,2}+\frac{1}{15} \lambda^{\alpha 2,2}-\frac{2}{15} \lambda^{\epsilon, 2}-\frac{1}{15} \lambda^{\gamma, 2}-\frac{1}{15} \lambda^{\delta, 2} \\
& -\frac{1}{l 3}\left(2 \lambda^{\alpha 1,2}+\lambda^{\alpha 2,2}\right) \cos ^{2} \Omega,
\end{aligned}
\tag{10}
$$
$$
\eta=-\frac{2}{15} \lambda^{\alpha 1,2}+\frac{2}{15} \lambda^{\alpha 2,2}+\frac{2}{5} \lambda^{\epsilon, 2}+\frac{1}{5} \lambda^{\gamma, 2}+\frac{1}{5} \lambda^{\delta, 2}.
\tag{11}
$$
where $\Omega=0$ for easy axis and $\Omega=\frac{\pi}{2}$ for easy plane system, respectively.

### 3. Experimental

To experimentally measure the magnetostriction, a polycrystalline sample of MnPt was prepared using an arc melting process with the MAM-1 system (Edmund Bühler GmbH). Stoichiometric amounts of high-purity manganese (99.9%) and platinum (99.99%) were melted under a titanium-gettered argon atmosphere. To ensure homogeneity, the sample was flipped and remelted multiple times. The final sample weighed approximately 1 g, with a mass loss of less than 0.5%. No further heat treatment was applied. X-ray diffraction (XRD) measurements were conducted at room temperature on a sample that had been hand-ground. These measurements were performed using a PANalytical X'pert Pro diffractometer, employing CuK$\alpha$ radiation produced at 40 kV and 30 mA ($\lambda = 1.5406$ Å) in a Bragg-Brentano geometry. The resulting XRD pattern was analyzed using FullProf software [31] (Fig. E.7). High-resolution magnetostriction measurements, tracking length changes as a function of magnetic field (magnetostriction) at 2 K, were performed using a miniature capacitance dilatometer [32]. The dilatometer was connected to an AH2500A capacitance bridge, integrated into a Physical Property Measurement System (PPMS) from Quantum Design.

### 4. Calculation details

Electronic structure calculations were performed within the plane-wave based Vienna ab-initio simulation package (VASP) [33, 34] employing the projector-augmented-wave (PAW) method with PAW pseudo-potentials. Calculations consider the generalized gradient approximation (GGA) of Perdew-Burke-Ernzerhof (PBE) [35]. Primarily, the non-collinear magnetic calculations with the spin-orbit coupling were considered. The energy cut-off for the plane waves of 450 eV was used. In general, an automatic generation of a k-mesh scheme with $R_k = 70$ was considered. The relaxation was performed in the Methfessel-Paxton scheme of the order 1 (Brillouin zone (BZ) integration technique) with a smearing 0.01 eV. Due to computational demands, the same smearing was used when $R_k$ exceeded 100. Elsewhere, the tetrahedron method with Blöchl corrections was employed for the BZ integration. The energy convergence in structure relaxation calculations includes the convergence of the self-consistent

loop better than EDIFF $=10^{-7}$ eV and energy difference between relaxation steps smaller than EDIFF $=10^{-6}$ eV. Regarding calculations of the magnetoelastic properties and MAE, a tight convergence was demanded EDIFF $=10^{-9}$ eV. To obtain a good linear fit of magnetoelastic constants $b_i$, $R_k=120$ resp. $R_k=110$ was used for the calculations of elastic and magnetoelastic properties in the case of AFM1, resp. AFM2 magnetic structures (Fig. 1b,c). The elastic and magnetoelastic parameters were evaluated within AELAS [36] resp. MEALAS (with -mode 2, strain-energy method) [24, 30] packages using a finite displacement approach. The packages were used to generate distorted structures and the result analysis.

The applied strain in the magnetoelastic calculations differs between magnetic phases depending on the linearity of the obtained energy dependencies. In the case of the FM structure (Fig. 1a), the maximum applied strain $\varepsilon$ was 0.0075. The AFM1 system exhibits linear behavior in a smaller region, and the maximal strain was reduced to 0.0050. Whereas for the AFM2 structure, the maximum strain 0.0100 can be applied except for the calculation of the $b_2$ parameter, requiring a reduction to 0.0075. The R-factor of the linear fitting was better than 0.98 except for certain cases of low $b_i$ values given by related extreme demands on precision.

MAE was estimated at a fine k-mesh (FM: $R_k=70$, AFM1: $R_k=90$ and AFM2: $R_k=95$) with tight energy convergence EDIFF $=10^{-8}$ eV. High-accuracy calculations were needed to obtain smooth energy curves, particularly for antiferromagnetic structures.

The exchange interaction parameters to atomistic spin simulations were calculated within the Relativistic Spin Polarized toolkit (RSPt) package based on the Full-Potential Linear Muffin-Tin Orbital (FP-LMTO) method [37, 38]. The calculations were performed on $20 \times 20 \times 20$ $k$-mesh in the fully relativistic scheme, considering the xc-potential of PBE 96 [35] and Perdew Wang 1992 [39]. Relaxed VASP crystal structures were used in the calculations. The energy convergence was better than $10^{-10}$ Ry and the orbitals $s$, $p$, $d$ were considered in the evaluation of exchange interactions. The isotropic magnetic exchange interactions $J_{ij}$ were evaluated by the fully relativistic version of the LKAG method based on the magnetic force theorem [40]. The interaction Hamiltonian reads

$$
\hat{H}=-\sum_{i \neq j} \sum_{\{\alpha, \beta\}=\{x, y, z\}} e_{i}^{\alpha} \hat{J}_{i j}^{\alpha \beta} e_{j}^{\beta}, \tag{12}
$$

where $\hat{J}_{i j}^{\alpha \beta}$ is a $(3 \times 3)$ interaction coupling tensor and $e_{i}^{\alpha}$ denotes spin components of unitary spin vector at the site $i$. However, here, only the AFM1 phase related isotropic Heisenberg interactions $J_{ij}$ (Fig. I.8), given as follows [40]

$$
\hat{H}=-\sum_{i \neq j} J_{i j} \mathbf{e}_{i} \cdot \mathbf{e}_{j}, \tag{13}
$$

$$
J_{i j}=\frac{1}{3} \operatorname{Tr} \hat{J}_{i j}^{\alpha \beta}, \tag{14}
$$

were considered in the atomistic spin simulations together with the calculated anisotropic constants $K_1$ and $K_2$. They were employed to simulate magnetization directions of magnetic sublattices with respect to the applied external magnetic field. Atomistic spin simulations were performed within the Uppsala Atomistic Spin Dynamics (UppASD) program [41], namely, a magnetization averaged over time and particular magnetic sublattices of the AFM1 system was studied. To describe a polycrystalline system, a few distinct magnetic field orientations with respect to the crystal structure were considered, i.e., the magnetic field along the $x$, $z$, $xz$, and $xy$ Cartesian directions, where the AFM1 crystal structure $a$ axis is oriented along the Cartesian $x$ direction and the $c$ axis coincides with the $z$ direction. A 20x20x20 supercell with Mn atoms, bearing the magnetic moment as in the AFM1 phase, was considered. The simulations were performed at $T=2$ K according to the experiment, while the time and Mn atoms averaged magnetization were studied.

## 5. Results

### 5.1. Theoretical magnetoelastic behavior

Prior to the analysis of the experimental magnetostriction results, theoretical magnetoelastic properties are estimated. Despite the experimentally reported antiferromagnetic ground state of the studied

![](./images/1109550803607093272_1.jpg)

Figure 1: MnPt magnetic structures. (a) FM, (b) AFM1, (c) AFM2. Dashed lines in the AFM1 structure denote the primitive cell, similar to the FM one. (plotted in VESTA 3 [42])

MnPt system [16], in our calculations, we also considered other magnetic ordering [12, 43] to inspect the the magnetoelastic behavior and analyze the experimental behavior. Namely, we considered three collinear structures with magnetic moments pointing along the $c$-axis: ferromagnetic (FM) and two antiferromagnetic (AFM1, AFM2) structures (Fig. 1). Corresponding to the literature [16, 43, 15, 12], the AFM1 state, with AFM ordered nearest-neighbor spins in the basal $ab$-plane, was found as the ground state (Table C.2). However, it should be noted that the FM phase was observed in quenched powders and sputtered films of disordered MnPt [44]. The additional AFM 2 phase serves for comparison with another AFM phase. The obtained energy differences are in agreement with the published ones [12, 43] as well as the relaxed structural parameters [45, 43, 15, 46] (Table C.2).

Having calculated the elastic constants (Table F.4), the magnetoelastic ($b_i$) and magnetostrictive coefficients ($\lambda_i$) can be discussed, respectively. The magnetoelastic constants arise from the change of the magnetocrystalline anisotropy energy (MAE) with respect to the applied strain and the defined spin directions (Fig. 4). The type of magnetic order substantially modifies the MAE (Fig. 3). Thereby, the magnitudes of the $b_i$ parameters, including their signs, depend strongly on the magnetic structure as demonstrated by the estimated values of the magnetoelastic constants $b_i$ (Table 1). For clarity, the values of $b_i$ constants in are referred to the axis of the FM structure, similar to the case of the elastic constants.

<table>
<caption>Table 1: MnPt magnetoelastic constants $b$, magnetostrictive coefficients $\lambda$, and magnetostriction parameters for a polycrystalline sample $\xi$, $\eta$ . Axes are oriented according to the FM primitive cell, i.e., the AFM1 structure is rotated about 45 degrees along the c-axis .</caption>
<tbody>
<tr>
<td>$b$ (MPa)</td>
<td>FM</td>
<td>AFM1</td>
<td>AFM2</td>
</tr>
<tr>
<td>$b_{21}$</td>
<td>135</td>
<td>12</td>
<td>-62</td>
</tr>
<tr>
<td>$b_{22}$</td>
<td>-111</td>
<td>-19</td>
<td>23</td>
</tr>
<tr>
<td>$b_3$</td>
<td>-40</td>
<td>-37</td>
<td>118</td>
</tr>
<tr>
<td>$b_4$</td>
<td>-34</td>
<td>1</td>
<td>26</td>
</tr>
<tr>
<td>$b_3'$</td>
<td>86</td>
<td>47</td>
<td>75</td>
</tr>
<tr>
<td>$\lambda$ ($10^{-6}$)</td>
<td>FM</td>
<td>AFM1</td>
<td>AFM2</td>
</tr>
<tr>
<td>$\lambda^{\alpha 1,2}$</td>
<td>-1592</td>
<td>-88</td>
<td>757</td>
</tr>
<tr>
<td>$\lambda^{\alpha 2,2}$</td>
<td>2655</td>
<td>155</td>
<td>-1168</td>
</tr>
<tr>
<td>$\lambda^{\gamma,2}$</td>
<td>240</td>
<td>156</td>
<td>-754</td>
</tr>
<tr>
<td>$\lambda^{\varepsilon,2}$</td>
<td>170</td>
<td>-6</td>
<td>-151</td>
</tr>
<tr>
<td>$\lambda^{\delta,2}$</td>
<td>-620</td>
<td>-340</td>
<td>-775</td>
</tr>
<tr>
<td></td>
<td>FM</td>
<td>AFM1</td>
<td>AFM2</td>
</tr>
<tr>
<td>$\xi$ ($10^{-6}$)</td>
<td>-68</td>
<td>7</td>
<td>130</td>
</tr>
<tr>
<td>$\eta$ ($10^{-6}$)</td>
<td>558</td>
<td>-7</td>
<td>-623</td>
</tr>
</tbody>
</table>

The $b_i$ constants differ significantly, except for the $b_3'$ one.

More important from an experimental point of view are the magnetostrictive coefficients $\lambda^i$ (Table 1) that describe the change in length with respect to the sample magnetization (Eq. 2). Magnetic structure-dependent differences in magnetoelastic constants $b_i$ give rise to substantial differences in magnetostrictive behavior. The most striking ones are in the magnitudes of the $\lambda^{\alpha 1,2}$ and $\lambda^{\alpha 2,2}$ constants (Eqs. B.8,B.9

) coming from the $b_{21}$ and $b_{22}$ magnetoelastic coefficients. The constant $\lambda^{\alpha 1,2}$ describes an enlargement of the $ab$-basis area for magnetization applied along the $c$-axis, while $\lambda^{\alpha 1,2}$ is related to the elongation of the $c$-parameter. Concerning the FM state, a huge $ab$-basis area squeezing was revealed, being compensated by enormous $c$-axis elongation. An opposite behavior, about half-magnitude weaker, was found for the AFM2 phase. The opposite signs come from the magnetoelastic coefficients and they are also responsible for modest values related to the AFM1 phase, since the elastic constants are comparable between magnetic phases. Found magnitudes of FM and AFM2 coefficients $\lambda^{\alpha 1,2}$ and $\lambda^{\alpha 2,2}$ are outstanding compared to other compounds [7].

The $\lambda^{\gamma,2}$ coefficient (Eq. B.10 arising from $b_3$ constant denotes the change in length along the $a$ resp. $b$ axis with difference in the magnetization direction $(\alpha_x^2 - \alpha_y^2)$ resp. $(\alpha_y^2 - \alpha_x^2)$. Hence, it does not contribute when $\alpha_x^2 = \alpha_y^2$. Both the FM and AFM1 states in the basal plane prefer the elongation along the basal magnetization. The behavior of the AFM2 is opposite and way stronger. The shear in the $ab$ basis given by the in-plane components of the magnetization axis is attributed to the $\lambda^{\delta,2}$ coefficient (Eq. B.11). It is substantial irrespective of the magnetic order, bearing similar values FM and AFM2 phases as their $b_3'$ hardly vary. On the other hand, the shear perpendicular to the $ab$ basis related to $\lambda^{\varepsilon,2}$ (Eq. B.12) is much weaker. Particularly for the AFM1 phase, the MAE is almost unchanged with deformation $(b_4)$.

### 5.2. Experimental magnetostriction analysis

The obtained theoretical results are used to explain the measured behavior of a polycrystalline sample. The measured dilatometry (Fig. 2) was performed with different mutual orientations of the length change direction and the applied external magnetic field. Regarding the measured data for the parallel field orientation $(\varphi=0$ deg), the sample length shrinks up to the field of $\mu_0 H \sim 5$ T. However, further on, the sample starts to elongate, as the opposite slope of the measured dependence occurs. Applying a field perpendicular to the measured direction, a slight sample elongation was detected for weak fields. Increasing the field strength, the slope changes around a field magnitude similar to the case of the parallel field direction, and the measured sample direction starts to be reduced.

The observed behavior is related to magnetizing a sample of the AFM nature, where the behavior is more complex than in the FM system due to the AFM ordering. Performing the measurements at 2 K, one can assume that the AFM domains are randomly oriented along the easy axis directions, as the measurements are well below the Néel temperature. Applying the external field, in a textbook model, the AFM magnetic structure is modified according to the orientation of the easy axis in the magnetic domain with respect to the external magnetic field direction. For simplicity, let us consider only two limit orientations, i.e., external field parallel to the easy axis and the perpendicular orientation of the easy axis and the field. Regarding the perpendicular orientation, the external field introduces canting of the AFM moments into the direction of the magnetic field. Whereas for the parallel orientation, a spin-flop meta-magnetic transition at a certain field magnitude should appear as the system possesses weak anisotropy. In general, the applied external field smears out the AFM character of the system. On the other hand, in the FM system, the magnetic structure is kept despite the tilting of the magnetic moments.

However, to obtain an actual response of the magnetic structure to the applied external field, atomistic spin simulations of the magnetization direction were performed. They show that the canting of the magnetic moments is small (Fig. 2c,d). The induced magnetization is negligible (Fig. 2b), and the simulations correspond well to the experimental values (Fig. 2a-inset). Analysis of the sublattice magnetization direction revealed that, particularly for low fields, the sublattice magnetizations point in nearly opposite directions (Fig. 2c,d), as the magnetization directions are almost simultaneously tilted, resembling the behavior of a FM system. Moment canting is negligible, which seems to arise from a low magnetocrystalline anisotropy (Fig. 3b).

It enables one to characterize the AFM1 system at low fields in a similar way to the FM one. Therefore,

![](./images/1109550803607093272_2.jpg)

Figure 2: Experimental MnPt magnetostriction and simulated sublattice magnetization directions. (a) Magnetostriction measured (olive) parallel, (blue) perpendicular, and (red) at 45 degrees to the applied external magnetic field. The inset depicts the magnetization curve of the sample. (b-d) magnetization direction of magnetic sublattices A and B simulated in the AFM1 system depending on the external field strength. (b) Cartesian components of the total magnetization. (c,d) Magnetization directions related to the A,B sublattices in spherical coordinates. Magnetization is averaged over the atoms in the particular supercell and the time. Four different relative field orientations were applied. The $a$ axis of the AFM1 crystal cell is oriented along the Cartesian $x$ direction, and the $c$ axis along the $z$ direction. Calculations were performed at $T=2$ K same as the experiment.

we calculated the parameters $\xi$ and $\eta$ (Table 1) describing a polycrystalline system according to Eq. 9 for both AFM1 and FM MnPt magnetic phases. Regarding a weak parallel external field, where the canting is negligible (Fig. 2c,d), the negative measured magnetostriction (Fig. 2a) corresponds to the sign of the calculated AFM1 $\eta$ parameter. Actually, one can ascribe it to the difference between the parallel and perpendicular field setups in the measurements. Since saturation cannot be achieved as in the FM case, it is hard to compare the magnitude. The change of the slope and occurrence of the positive magnetostriction in the experimental measurements with increasing external field can be attributed to the canting of the magnetic moments as the AFM magnetic structure starts to be substantially modified (Fig. 2c,d) according to the simulations between 4 T and 6 T, in agreement with the measurements. Assuming a sort of FM-like contribution, the behavior will agree with the calculated positive FM $\eta$ parameter being nearly five times stronger than the AFM1 one (Table 1). Concerning the $\xi$ parameter, one can focus on the measurements with the perpendicular field orientation (Eq. 9). Following the aforemen-

tioned assumptions, the sign of the AFM1 resp. FM $\xi$ parameters (Table 1) corresponds to the observed behavior under weak and high external magnetic field (Fig. 2).

### 5.3. Magnetic structure dependent mangetoelastic behavior
The calculated magnetic structure dependence of the $b_i$ constants, which represent differences in the slopes of the MAE with respect to the applied strain [30], can be understood starting from differences in spin structure in relation to the magnetization axes' directions, or more carefully by induced charge density differences regarding the applied deformations (Fig. 4).

Begining from the $b_{21}$ constant, the area of the $ab$-base is changed (Fig. 4a). Enlarging the base area, the $c/a$ ratio gets closer to 1, and the MAE for the defined magnetization directions $\alpha_1$ and $\alpha_2$ should be smaller by simple consideration. It agrees with the positive $b_1$ sign, except AFM2 case, as the difference $E_{\alpha_1} - E_{\alpha_2}$ is less negative. Concerning AFM2 and the related $b_{21}$ minus sign, simply based on the spin orientations, one can find that both in the FM and AFM1 case, the spins along the magnetization axes $\alpha_1$ resp. $\alpha_2$ have the same direction, whereas for AFM2 it changes. It is the opposite along the $\alpha_1$ direction, but the same along the $\alpha_2$ one. A better explanation can be provided by changes in the charge density induced by the change of the magnetization axis, which were obtained by self-consistent calculations (Fig. 4a).

Regarding the AFM2 magnetic phase, significant positive charge difference $\Delta\rho = \rho(\alpha_1)-\rho(\alpha_2)$ (Fig. 4a - yellow color) appears along $a$ and $b$ directions between Mn resp. particularly in between Pt atoms. Enlarging the $a$ parameter, the extra energy contribution related to the charge difference for the $\alpha_1$ magnetization direction is reduced, which lowers the $E_{\alpha_1}$ with the respect to $E_{\alpha_2}$. The nearest Mn-Pt distance is shorter than the $a$ parameter, so the effect might be more important. However, the change of the charge density has no dominating character in this direction. On the other hand, quite the opposite character of the charge density differences for the FM magnetic phase was calculated. It agrees with the opposite sign of the $b_{21}$. Finally, the AFM1 charge difference does not offer an easily visible preference either for $\alpha_1$ resp. $\alpha_2$ magnetization direction, which might explain the small $b_{21}$ constant. Its positive sign likely comes from a negative charge density difference along the Mn-Pt direction. The parts of charge density contributing to the parameters $b_i$ are denoted in Fig. 4.

Qualitatively, the high FM $b_{21}$ value corresponds to a strong magneto-crystalline anisotropy in the FM phase compared to AFM ones (Fig. 3). The FM anisotropic constant $K_1$ is one or two orders of magnitude larger than those of AFM1 or AFM2, respectively. Further, also $K_2$ constants differ significantly across the magnetic phases, being largest for the FM magnetic phase. The $K_1$ dominates for the FM state. However, for AFM1 phase, the $K_1$ is comparable to $K_2$ and even more remarkably, the $K_2$ constant dominates the AFM2 state, making its behavior quite different. In addition, the $K_3$ constant is substantial in AFM states, while it is negligible for the FM state. The $b_{22}$ constant is related to the opposite behavior of the $b_{21}$ as it comes from elongation of the $c$-axis (Fig. 4b) followed by an increase of the MAE for the FM magnetic phase (Fig. 3). Indeed, we observed opposite behavior both in the signs and magnitudes following the difference in charge densities (Fig. 4b).

Analyzing the orbital origin of the MAE, the shape of the charge differences and its sign correspond to the orbital resolved MAE contributions (Fig. 5) obtained by summation of the orbital-resolved band energies across the Brillouin zone (Eq. 15). The orbital-resolved energy of the ion $i$ with magnetization axes $\alpha$ reads

$$
E_{lm}^{i}(\alpha)=\sum_{n,\mathbf{k}}E_{n\mathbf{k}}|\langle Y_{lm}^{i}|\phi_{n\mathbf{k}}\rangle|^{2}c_{n\mathbf{k}},\tag{15}
$$

where the $E_{n\mathbf{k}}$ is the band energy of the band $n$ at k-point $\mathbf{k}$ with occupancy $c_{n\mathbf{k}}$. Finally, $Y_{lm}^{i}$ denotes spherical harmonics centered at the ion $i$.

Regarding the FM phase, there is a strong anisotropy coming from Pt d-orbitals. Nevertheless, their contributions partly counteract. Besides, there are smaller contributions from Mn. Changing the magnetic structure, the Mn contribution dominates for the AFM1 phase corresponding to the charge density differences (Fig. 4b). The prominent $d_{xz}$ and $d_{yz}$

![](./images/1109550803607093272_3.jpg)

Figure 3: Magneto-crystalline anisotropy. (a,b) FM, (c,d) AFM1, (e,f) AFM2 magnetic phases. The insets (b,d,f) denote a change of the MAE in the ab-plane. Regarding the AFM1 magnetic structure, the axis orientation according to the FM structures is considered.

orbitals (Fig. 5c,d) are related to negative $\rho$ which would explain positive $b_{21}$. A similar explanation applies to $b_{22}$ and $d_{z^2}$ (Figs. 4b and 5c,d). Finally, Pt $d_{z^2}$ and $d_{x^2-y^2}$ contributions (Fig. 5e,f) seem to be the most important for the structure of AFM2, corresponding to $\Delta\rho$ (Fig. 4a,b). Both the orbital-resolved energy and charge density differences indicate that different orbitals are substantial depending on the magnetic structure, which seems to lead to different $b_i$ values. One has to point out that the performed projections to the spherical harmonics (Eq. 15) are not complete, and furthermore, they miss the interstitial charge. Thereby, the summations of the occupancies over all projections are not the same as the total band occupancy. Therefore, the orbital-resolved energy contributions are approximate.

Concerning the $b_3$ constant, where the shape of the $ab$-basis is changed (Fig. 4c), the FM and AFM1 states prefer the magnetization axis along the elongated $a$ axis, $E_{\alpha_1}-E_{\alpha_2}$ is negative (Table 1). In the case of FM, it comes from the charge density differences between Mn and Pt (Fig. 4c) – see dominant energy contributions of $d_{xz}$ and $d_{yz}$ orbitals (Fig. 5a). For the AFM1, the situation is more complex as opposite spin appears within the layer. Nevertheless, the mechanism is similar to that in the FM case. The orbital-resolved contributions do not help, since there are opposite contributions that almost cancel out, and the projections do not provide enough accurate information, as mentioned above. The positive sign of the AFM2 $b_3$ coefficients (Table 1) can be attributed to the denoted strong charge density difference (Fig. 4c) from $d_{xz}$ resp. $d_{yz}$ orbitals on Mn site (Fig. 5c) behaving in the opposite way to the FM state. Therefore, the magnetization alignment perpendicular to the elongation is preferred.

Further, $b_4$ coefficient is related to the modification of the $ac$-diagonal length. The FM state prefers moments aligned along the elongated diagonal, whereas the AFM states favor the antiparallel moments pointing along the shorter one (Fig. 4d). However, in the case of AFM1 phase, the preference is tiny. The FM state favors $\alpha_1$ direction which comes from $d_{xz}$ states (Fig. 5a) that bring the extra charge along the $ca$ diagonal. Particularly, the Mn contributions (Fig. 4d) show slight asymmetry in charge density differences with respect to the magnetization directions. However, they are small. Concerning AFM states, $\Delta\rho$ indicates that $\alpha_1$ brings extra density to the shrinking Mn-Pt direction, whereas for $\alpha_2$ the density appears with the elongated direction, which is preferred. Regarding the AFM1 phase, the charge density differences near Pt atoms spread more or less near the basal plane compared to the AFM2 one (Fig. 4d). Thereby, the AFM1 $b_4$ magnitude is negligible, unlike the AFM2 case where is a proximity of the Mn

![](./images/1109550803607093272_4.jpg)

Figure 4: Lattice deformations and spin directions related to calculations of magnetoelastic coefficients with related charge density differences. For each determined magnetoelastic coefficient $b_i$, lattice deformations applied to the FM, AFM1, and AFM2 magnetic structures are shown with depicted spin orientations $\alpha_1$ and $\alpha_2$. Charge density difference between the system with magnetization along $\alpha_1$ and $\alpha_2$ directions from self-consistent calculations is shown for each magnetic phase and type of deformation with the applied strain $\varepsilon=0.005$. Fine k-mesh was used (FM: $R_k=70$, AFM1: $R_k=90$ and AFM2: $R_k=95$). Yellow color denotes an excess of the charge density difference related to the $\alpha_1$ magnetization direction, whereas cyan one to the $\alpha_2$ direction. Deformations with respect to the FM axes are considered as in the Table 1. Below each charge density plot, the magnitude of the plotted $\Delta\rho$ isosurface is stated. Charge density plotted in VESTA 3 [42].

![](./images/1109550803607093272_5.jpg)

Figure 5: Atomic orbital resolved energy contributions to MAE. (a,b) FM, (c,d) AFM1, (e,f) AFM2. The energy difference $\Delta E = E_{\alpha_2} - E_{\alpha_1}$ is related to magnetization axes as shown in Fig. 4.

and Pt $\Delta\rho$ clouds.

Finally, the $b'_3$ coefficients exhibit similar values irrespective of the magnetic state (Table 1), particularly the FM and AFM2 phase. All the systems prefer spins ordered parallel along the squeezed $ab$-diagonal with similar $b'_3$ magnitude (Fig. 4e). The explanation is simple for the FM and AFM2 phases, where the $\alpha_2$ axis reduces the charge density for the shrinking Mn-Pt direction. Regarding the AFM1, the distributions of $\Delta\rho$ are quite complex, and hence it is not clear from which region the substantial interactions come. However, the orbital resolved energy contributions (Fig. 5a) suggest an effect of Mn $d_{xz}$ and $d_{yz}$ orbitals providing significant $\Delta\rho$ differences in the vicinity of the Mn atoms (Fig. 4e).

romagnetic ordering. Possibly, the strong magnetic coupling yielding high Néel temperature makes the system insensitive to the applied field. However, for the ferromagnetic state observed in quenched powders and sputtered films, the magnetoelastic response is enormous, exceeding the effect in the related FePt compound [7]. We probed the origin of the differences in the magnetoelastic behavior by analyzing charge density differences and orbital-resolved MAE contributions. It revealed a substantial difference in orbitals' contributions to the magnetoelastic behavior, explaining the distinct nature of the magnetoelastic effects in the studied magnetic phases. The ab-initio based results with atomic spin simulations were employed to describe observed experimental behavior, explaining well the measured dependencies.

## 6. Conclusions

In conclusion, we showed a significant predetermination of the magnetoelastic properties based on the type of magnetic ordering and explained the experimentally measured magnetostriction in the studied MnPt system. Due to the tetragonal symmetry, it can provide more interesting behavior than the commonly studied cubic-like materials. With regard to the antiferromagnetic ground state, the magnetoelastic effects are much smaller than those for the fer-

## Declaration of Interest Statement

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

### Author contributions

JŠ: Conceptualization, Data curation (ab-initio), Formal analysis, Investigation (ab-initio), Visualization, Writing - original draft; **KS**: Data curation(experiment), Investigation (experiment), Visualization, Writing – review & editing; **MV**: Data curation (experiment), Investigation (experiment), Visualization, Writing – review & editing; **TH**: Data curation(experiment), Investigation (experiment) ; **TJB**: Data curation(experiment), Investigation (experiment); **PN**: Conceptualization Writing – review & editing; **DL**: Conceptualization, Formal analysis, Writing & editing

---

### Acknowledgdemets

JS acknowledges GAČR project No. 24-11388I and DL GAČR project No. 25-14529L of the Grant Agency of Czech Republic and the CPU time by the Ministry of Education, Youth and Sports of the Czech Republic through the e-INFRA CZ (ID:90254) project. DL acknowledges project QM4ST (CZ.02.01.01/00/22_008/0004572) by The Ministry of Education, Youth and Sports of the Czech Republic. K.S. appreciates the support by the National Science Centre, Poland under the OPUS call in the Weave programme 2023/51/I/ST11/02562. P. N. acknowledges support by grant MU-23-BG22/00168 funded by The Ministry of Universities of Spain.

---

### Appendix A. Data availability

The datasets are available from the Zenodo repository at https://doi.org/10.5281/zenodo.15536903

---

### Appendix B. Magnetoelasticity - tetragonal system

Regarding the studied MnPt system bearing the crystal symmetry of the tetragonal (I) system, the elastic energy has the following form in the Cartesian axes [36],

$$
\begin{aligned}
\frac{1}{V_{0}}(&E_{\mathrm{el}}-E_{0})= \tag{B.1}
\\
&=\frac{1}{2}C_{11}(\varepsilon_{1}^{2}+\varepsilon_{2}^{2})+C_{12}\varepsilon_{1}\varepsilon_{2}+C_{13}(\varepsilon_{1}+\varepsilon_{2})\varepsilon_{3}
\\
&+\frac{1}{2}C_{33}\varepsilon_{3}^{2}+\frac{1}{2}C_{44}(\varepsilon_{4}^{2}+\varepsilon_{5}^{2})+\frac{1}{2}C_{66}\varepsilon_{6}^{2}
\\
&=\frac{1}{2}c_{xxxx}(\varepsilon_{\mathrm{xx}}^{2}+\varepsilon_{\mathrm{yy}}^{2})+c_{xxyy}(\varepsilon_{\mathrm{xx}}\varepsilon_{\mathrm{yy}})
\\
&+c_{xxzz}(\varepsilon_{\mathrm{xx}}+\varepsilon_{\mathrm{yy}})\varepsilon_{\mathrm{zz}}+\frac{1}{2}c_{zzzz}\varepsilon_{\mathrm{zz}}^{2}
\\
&+2c_{yzyz}(\varepsilon_{\mathrm{yz}}^{2}+\varepsilon_{\mathrm{zx}}^{2})+2c_{xyxy}\varepsilon_{\mathrm{xy}}^{2},
\end{aligned}
$$

where $E_{0}$ and $V_{0}$ stand for the equilibrium energy and volume. $C_{ij}$ resp. $c_{ijkl}$ denotes 6 independent elastic constants related to strain tensor matrix elements

$$
\begin{pmatrix}
\varepsilon_{1} \\
\varepsilon_{2} \\
\varepsilon_{3} \\
\varepsilon_{4} \\
\varepsilon_{5} \\
\varepsilon_{6}
\end{pmatrix}
=
\begin{pmatrix}
\varepsilon_{\mathrm{xx}} \\
\varepsilon_{\mathrm{yy}} \\
\varepsilon_{\mathrm{zz}} \\
2\varepsilon_{\mathrm{yz}} \\
2\varepsilon_{\mathrm{zx}} \\
2\varepsilon_{\mathrm{xy}}
\end{pmatrix}. \tag{B.2}
$$

On the other hand, the magnetoelastic energy possessing in the tetragonal (I) case 7 independent magnetoelastic constants $b_{i}$ [47, 48] reads

$$
\begin{aligned}
\frac{1}{V_{0}}E_{me} &= b_{11}(\varepsilon_{\mathrm{xx}}+\varepsilon_{\mathrm{yy}})+b_{12}\varepsilon_{\mathrm{zz}} \tag{B.3}
\\
&+b_{21}(\alpha_{z}^{2}-\frac{1}{3})(\varepsilon_{\mathrm{xx}}+\varepsilon_{\mathrm{yy}})+b_{22}(\alpha_{z}^{2}-\frac{1}{3})\varepsilon_{\mathrm{zz}}
\\
&+\frac{1}{2}b_{3}(\alpha_{x}^{2}-\alpha_{y}^{2})(\varepsilon_{\mathrm{xx}}-\varepsilon_{\mathrm{yy}})+2b_{3}^{\prime}\alpha_{x}\alpha_{y}\varepsilon_{\mathrm{xy}}
\\
&+2b_{4}(\alpha_{x}\alpha_{z}\varepsilon_{\mathrm{xz}}+\alpha_{y}\alpha_{z}\varepsilon_{\mathrm{yz}}).
\end{aligned}
$$

The first line describes the isotropic volume effect with constants $b_{11}$ and $b_{12}$. The other lines are related to the anisotropic behavior.

Evaluating the equilibrium strain given by the minimization of the sum of elastic and magnetoelastic energy

$$
\frac{\partial E_{el}+E_{me}}{\partial \varepsilon_{ij}^{eq}}=0, \tag{B.4}
$$

the relative length change in the tetragonal (I) system

follows [24]
$$
\left.\frac{\Delta l}{l_{0}}\right|_{\boldsymbol{\beta}} ^{\boldsymbol{\alpha}}=\lambda^{\alpha 1,0}\left(\beta_{x}^{2}+\beta_{y}^{2}\right)+\lambda^{\alpha 2,0} \beta_{z}^{2} \tag{B.5}
$$
$$
\begin{aligned}
&+\lambda^{\alpha 1,2}\left(\alpha_{z}^{2}-\frac{1}{3}\right)\left(\beta_{x}^{2}+\beta_{y}^{2}\right)+\lambda^{\alpha 2,2}\left(\alpha_{z}^{2}-\frac{1}{3}\right) \beta_{z}^{2} \\
&+\frac{1}{2} \lambda^{\gamma, 2}\left(\alpha_{z}^{2}-\alpha_{y}^{2}\right)\left(\beta_{x}^{2}-\beta_{y}^{2}\right)+2 \lambda^{\delta, 2} \alpha_{x} \alpha_{y} \beta_{x} \beta_{y} \\
&+2 \lambda^{\varepsilon, 2}\left(\alpha_{x} \alpha_{z} \beta_{x} \beta_{z}+\alpha_{y} \alpha_{z} \beta_{y} \beta_{z}\right),
\end{aligned}
$$

where the isotropic magnetostrictive coefficients $\lambda$ describing the volume magnetostriction are functions of the elastic muduli $C_{i j}$ and magnetoelastic constants $b_{i}$ [28]
$$
\lambda^{\alpha 1,0}=\frac{-b_{11} C_{33}+b_{12} C_{13}}{C_{33}\left(C_{11}+C_{12}\right)-2 C_{13}^{2}}, \tag{B.6}
$$
$$
\lambda^{\alpha 2,0}=\frac{2 b_{11} C_{13}-b_{12}\left(C_{11}+C_{12}\right)}{C_{33}\left(C_{11}+C_{12}\right)-2 C_{13}^{2}}. \tag{B.7}
$$

Whereas the magnetization direction dependent relative length change (Eq. B.5) is given by anisotropic coefficients [24]
$$
\lambda^{\alpha 1,2}=\frac{-b_{21} C_{33}+b_{22} C_{13}}{C_{33}\left(C_{11}+C_{12}\right)-2 C_{13}^{2}} \tag{B.8}
$$
$$
\lambda^{\alpha 2,2}=\frac{2 b_{21} C_{13}-b_{22}\left(C_{11}+C_{12}\right)}{C_{33}\left(C_{11}+C_{12}\right)-2 C_{13}^{2}} \tag{B.9}
$$
$$
\lambda^{\gamma, 2}=\frac{-b_{3}}{C_{11}-C_{12}} \tag{B.10}
$$
$$
\lambda^{\delta, 2}=\frac{-b_{3}^{\prime}}{2 C_{66}} \tag{B.11}
$$
$$
\lambda^{\varepsilon, 2}=\frac{-b_{4}}{2 C_{44}}. \tag{B.12}
$$

## Appendix C. Magnetic structures

The calculated relaxed structure parameters are in agreement with the literature [45, 43, 15, 46] (Table C.2). Similarly, the obtained energy differences between considered magnetic phases agree with the published ones [12, 43] , and the estimated magnitudes of spin magnetic moments correspond to the literature [43, 45, 15]. Alike the FePt system, the Pt sublattices bear no magnetic moments except the FM phase [43]. In considered AFM systems, only Mn atoms are magnetic, which can facilitate understanding of the magnetic behavior. Particularly, non-zero AFM oriented moments would break the tetragonal symmetry of the AFM1 structure in the $ab$-direction. Regarding the prepared polycrystalline sample, determined values of the lattice parameters are $a=2.8267(2) \AA$ and $c=3.6755(3) \AA$. They are in good agreement with the literature data [49] and calculated AFM1 ground state, where the difference is about $1 \%$.

Table C.2: Calculated MnPt magnetic phase energy differences and related structure parameters. The structure data are shown according to the FM primitive cell axes, except the $a_{n r}$ denoting the basal edge in the non-reduced cell with 4 atoms in the basis. XRD refined data of the prepared sample is added for comparison.
<table>
 <thead>
  <tr>
   <th>
   </th>
   <th>
    $\Delta$ E/f.u.
   </th>
   <th>
    a
   </th>
   <th>
    c
   </th>
   <th>
    c/a
   </th>
   <th>
    V
   </th>
   <th>
    c/$a_{nr}$
   </th>
  </tr>
  <tr>
   <th>
   </th>
   <th>
    (eV)
   </th>
   <th>
    (Å)
   </th>
   <th>
    (Å)
   </th>
   <th>
   </th>
   <th>
    (Å3)
   </th>
   <th>
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>
    NM
   </td>
   <td>
    0.00
   </td>
   <td>
    2.642
   </td>
   <td>
    3.770
   </td>
   <td>
    1.43
   </td>
   <td>
    26.3
   </td>
   <td>
    1.01
   </td>
  </tr>
  <tr>
   <td>
    FM
   </td>
   <td>
    -1.02
   </td>
   <td>
    2.931
   </td>
   <td>
    3.507
   </td>
   <td>
    1.20
   </td>
   <td>
    30.1
   </td>
   <td>
    0.85
   </td>
  </tr>
  <tr>
   <td>
    AFM1
   </td>
   <td>
    -1.32
   </td>
   <td>
    2.799
   </td>
   <td>
    3.718
   </td>
   <td>
    1.33
   </td>
   <td>
    29.1
   </td>
   <td>
    0.94
   </td>
  </tr>
  <tr>
   <td>
    AFM2
   </td>
   <td>
    -1.05
   </td>
   <td>
    2.861
   </td>
   <td>
    3.645
   </td>
   <td>
    1.27
   </td>
   <td>
    29.8
   </td>
   <td>
    0.90
   </td>
  </tr>
  <tr>
   <td>
    exp.
   </td>
   <td>
   </td>
   <td>
    2.827
   </td>
   <td>
    3.676
   </td>
   <td>
    1.30
   </td>
   <td>
    29.4
   </td>
   <td>
    0.92
   </td>
  </tr>
 </tbody>
</table>

Table C.3: MnPt spin and orbital magnetic moment components with the respect to various magnetic orderings.
<table>
 <tbody>
  <tr>
   <th>
   </th>
   <td colspan="3">
    $\mu_{\text{Mn}}^{\text{L}}$ ($\mu_{\text{B}}$)
   </td>
   <td colspan="3">
    $\mu_{\text{Pt}}^{\text{L}}$ ($\mu_{\text{B}}$)
   </td>
  </tr>
  <tr>
   <th>
   </th>
   <td>
    x
   </td>
   <td>
    y
   </td>
   <td>
    z
   </td>
   <td>
    x
   </td>
   <td>
    y
   </td>
   <td>
    z
   </td>
  </tr>
  <tr>
   <th>
    FM
   </th>
   <td>
    0.00
   </td>
   <td>
    0.00
   </td>
   <td>
    0.03
   </td>
   <td>
    0.00
   </td>
   <td>
    0.00
   </td>
   <td>
    0.07
   </td>
  </tr>
  <tr>
   <th>
    AFM1
   </th>
   <td>
    0.00
   </td>
   <td>
    0.00
   </td>
   <td>
    0.04
   </td>
   <td>
    0.00
   </td>
   <td>
    0.00
   </td>
   <td>
    0.00
   </td>
  </tr>
  <tr>
   <th>
    AFM2
   </th>
   <td>
    0.00
   </td>
   <td>
    0.00
   </td>
   <td>
    0.03
   </td>
   <td>
    0.00
   </td>
   <td>
    0.00
   </td>
   <td>
    0.00
   </td>
  </tr>
  <tr>
   <th>
   </th>
   <td colspan="3">
    $\mu_{\text{Mn}}^{\text{S}}$ ($\mu_{\text{B}}$)
   </td>
   <td colspan="3">
    $\mu_{\text{Pt}}^{\text{S}}$ ($\mu_{\text{B}}$)
   </td>
  </tr>
  <tr>
   <th>
   </th>
   <td>
    x
   </td>
   <td>
    y
   </td>
   <td>
    z
   </td>
   <td>
    x
   </td>
   <td>
    y
   </td>
   <td>
    z
   </td>
  </tr>
  <tr>
   <th>
    FM
   </th>
   <td>
    0.00
   </td>
   <td>
    0.00
   </td>
   <td>
    3.82
   </td>
   <td>
    0.00
   </td>
   <td>
    0.00
   </td>
   <td>
    0.37
   </td>
  </tr>
  <tr>
   <th>
    AFM1
   </th>
   <td>
    0.00
   </td>
   <td>
    0.00
   </td>
   <td>
    3.64
   </td>
   <td>
    0.00
   </td>
   <td>
    0.00
   </td>
   <td>
    0.00
   </td>
  </tr>
  <tr>
   <th>
    AFM2
   </th>
   <td>
    0.00
   </td>
   <td>
    0.00
   </td>
   <td>
    3.76
   </td>
   <td>
    0.00
   </td>
   <td>
    0.00
   </td>
   <td>
    0.00
   </td>
  </tr>
 </tbody>
</table>

## Appendix D. DOS

Density of the states (DOS) for the magnetic systems was compared (Fig. D.6). According to the literature, the formation of a pseudo-gap for the AFM1 ground state was observed. It is assumed that the suppressed DOS around the Fermi level, pseudogap formation, is attributed to an antiferromagnetic staggered field [14]. Alike behavior does not occur for the FM and AFM2 phases. Particularly, AFM2 possesses a high DOS at the Fermi level. It points out significant differences in the electronic structures between the AFM phases given by different orientations of the antiferromagnetic ordering. Nevertheless, for all the magnetic phases, the intensity of the Mn and Pt states is similar below the Fermi level, as the Pt conduction d-states spread across more than 6 eV while the Mn $3d$-states tend to have similar weight as $5d$ Pt states only from 3 eV below and up to the Fermi level. Above, Mn dominates the conduction states for the studied energy range.

![](./images/1109550803607093272_6.jpg)

Figure D.6: Density of states with respect to the magnetic phase. (a) FM, (b) AFM1, (c) AFM2.

## Appendix E. Experimental details - XRD measurements

The prepared polycrystalline sample was characterized by X-ray diffraction (XRD) measurements at room temperature employing $CuK\alpha$ radiation ($\lambda = 1.5406$ Å) in a Bragg-Brentano geometry, where XRD pattern was analyzed using FullProf software [31].

![](./images/1109550803607093272_7.jpg)

Figure E.7: The room temperature X-ray diffraction pattern for the MnPt sample. The open circles represent the experimental data, while the solid lines depict the Rietveld-refined pattern obtained using Fullprof software. The difference pattern is illustrated by the solid line at the bottom. Ticks indicate the positions of the Bragg reflections corresponding to the tetragonal CuAu-I type structure (space group $P4/mmm$, No. 123). The most prominent peaks are labeled with their Miller ($hkl$) indices.

## Appendix F. Elastic behavior

The determination of magnetoelastic parameters requires knowledge of elastic coefficients $C_{ij}$. Since in this work we deal not only with the ground state AFM1 magnetic structure but also with the FM and AFM2, elastic coefficients were estimated in all cases, including the NM state for comparison. To be able to compare the results (Table 1) to existing literature data for NM [45] and for AFM1 [22]), the $C_{ij}$ are defined according to the axes of the FM primitive cell. It means a rotation of the AFM1 cell and related coefficients in the $ab$-plane by 45 degrees (Fig. 1). According to the calculated values, all the structures fulfilled *Born stability criteria* for tetragonal (I) systems [50, 51]: $C_{ii} > 0$; $C_{11} > |C_{12}|$; $2C_{13}^2 < C_{33}(C_{11}+C_{12})$.

Based on the calculated values, the NM phase has the highest bulk modulus $B$ (Table F.5), making the phase the toughest. It is related to the smallest volume. The bulk modulus of the other magnetic ones is similar, corresponding to the similar volume, particularly of FM and AFM2, possessing comparable $C_{ij}$. Regarding the shear modulus $G$, the rigidness is quite dependent on the magnetic phase, while the magnetic phases are rather ductile according to the Pugh ratio $(G/B < 0.57)$ [52] unless the phase is non-magnetic, see (Table F.5).

Table F.4: The elastic constants of tetragonal MnPt for nonmagnetic (NM), ferromagnetic (FM), and two antiferromagnetic orderings (AFM1 and AFM2). The last column shows the AFM1 elastic constants with respect to the axis of the non-reduced (nr) AFM1 cell, for better comparison with the published data.

| $C_\text{ij}$(GPa) | NM  | FM  | AFM1 | AFM2 | AFM1$^\text{nr}$ |
|---------------------|-----|-----|------|------|------------------|
| $C_{11}$            | 549 | 252 | 306  | 238  | 258              |
| $C_{12}$            | 109 | 87  | 72   | 82   | 120              |
| $C_{13}$            | 171 | 152 | 141  | 155  | 141              |
| $C_{33}$            | 424 | 224 | 284  | 220  | 284              |
| $C_{44}$            | 195 | 99  | 123  | 87   | 123              |
| $C_{66}$            | 115 | 69  | 69   | 48   | 117              |

Table F.5: Bulk modulus ($B$), shear modulus ($G$) and Pugh ratio ($G/B$) in the Hill approximation

|      | $B$(GPa) | $G$(GPa) | $G/B$  |
|------|----------|----------|--------|
| NM   | 269      | 167      | 0.624  |
| FM   | 167      | 69       | 0.414  |
| AFM1 | 178      | 95       | 0.535  |
| AFM2 | 162      | 58       | 0.355  |

## Appendix G. Magnetoelasic properties

For completeness, calculated AFM1 magnetoelastic constants were estimated with respect to the axes of the non-reduced AFM1 cell (Table G.6), meaning a $\pi/4$ rotation along the $c$-axis (Fig. 1b) with respect to the results mentioned in the main text (Table 1). Rotation of the $a$ and $b$ axes in the basal plane leads to changes in the $b_i$ coefficients. The signs of $b_{21}$ and $b_{22}$ coefficients are kept. However, the change of the coordinates switches the signs of the $b_3$ and $b_3'$ coefficients related to the magnetization axes in the basal plane. One can relate it to the $K_3$ anisotropic constant and reduction of the MAE with the $\pi/4$ rotation (Fig. 3b). Eventually, $b_4$ becomes negligible. Therefore, it is important to choose the proper reference basis. In addition, the magnetoelastic coefficients were obtained not only for the tetragonal symmetry but also for the orthorhombic one (Table G.6). It proves that the tetragonal symmetry considerations are valid for the AFM1 structure.

Table G.6: Magnetoelastic constants and magnetostrictive coefficient for AFM1 related to the non-reduced cell. Tetragonal or orthorhombic symmetry is considered.

|          | tetragonal |                |          | orthorhombic |                |
|----------|------------|----------------|----------|--------------|----------------|
|          | $b$        | $\lambda$      |          | $b$          | $\lambda$      |
|          | (MPa)      | $(10^{-6})$    |          | (MPa)        | $(10^{-6})$    |
| $b_{21}$ | 9          | $\lambda^{\alpha1,2}$ | -71 | $b_1$ | 11 | $\lambda^{1}$ | -81 |
| $b_{22}$ | -15        | $\lambda^{\alpha2,2}$ | 126 | $b_2$ | -33 | $\lambda^{2}$ | 232 |
| $b_3$    | 43         | $\lambda^{\gamma,2}$ | -310 | $b_3$ | -33 | $\lambda^{3}$ | 230 |
| $b_4$    | 1          | $\lambda^{\varepsilon,2}$ | -2 | $b_4$ | 11 | $\lambda^{4}$ | -82 |
| $b_3'$   | -37        | $\lambda^{\delta,2}$ | 158 | $b_5$ | 14 | $\lambda^{5}$ | -122 |
|          |            |                |          | $b_6$ | 13 | $\lambda^{6}$ | -121 |
|          |            |                |          | $b_7$ | -37 | $\lambda^{7}$ | 154 |
|          |            |                |          | $b_8$ | 1 | $\lambda^{8}$ | -52 |
|          |            |                |          | $b_9$ | 1 | $\lambda^{9}$ | -52 |

## Appendix H. Magnetoelasticity - orthorhombic system

Regarding an orthorhombic system, the magnetoelastic energy is described by 12 independent magnetoelastic constants (3 isotropic and 9 anisotropic ones) as follows [24]

$$
\begin{aligned}
\frac{1}{V_{0}} E_{m e} &=b_{01} \varepsilon_{\mathrm{xx}}+b_{02} \varepsilon_{\mathrm{yy}}+b_{03} \varepsilon_{\mathrm{zz}} \tag{H.1} \\
&+b_{1} \alpha_{x}^{2} \varepsilon_{\mathrm{xx}}+b_{2} \alpha_{y}^{2} \varepsilon_{\mathrm{xx}}+b_{3} \alpha_{x}^{2} \varepsilon_{\mathrm{yy}} \\
&+b_{4} \alpha_{y}^{2} \varepsilon_{\mathrm{yy}}+b_{5} \alpha_{x}^{2} \varepsilon_{\mathrm{zz}}+b_{6} \alpha_{y}^{2} \varepsilon_{\mathrm{zz}} \\
&+2 b_{7} \alpha_{x} \alpha_{y} \varepsilon_{\mathrm{xy}}+2 b_{8} \alpha_{x} \alpha_{z} \varepsilon_{\mathrm{xz}}+2 b_{9} \alpha_{y} \alpha_{z} \varepsilon_{\mathrm{yz}}.
\end{aligned}
$$

The relative length change at the equilibrium strain in the orthorhombic system follows [24]

$$
\begin{aligned}
\left.\frac{\Delta l}{l_{0}}\right|_{\boldsymbol{\beta}} ^{\boldsymbol{\alpha}} &=\lambda^{\alpha 1,0} \beta_{x}^{2}+\lambda^{\alpha 2,0} \beta_{y}^{2}+\lambda^{\alpha 3,0} \beta_{z}^{2} \tag{H.2} \\
&+\lambda^{1}\left(\alpha_{x}^{2} \beta_{x}^{2}-\alpha_{x} \alpha_{y} \beta_{x} \beta_{y}-\alpha_{x} \alpha_{z} \beta_{x} \beta_{z}\right) \\
&+\lambda^{2}\left(\alpha_{y}^{2} \beta_{x}^{2}-\alpha_{x} \alpha_{y} \beta_{x} \beta_{y}\right)+\lambda^{3}\left(\alpha_{x}^{2} \beta_{y}^{2}-\alpha_{x} \alpha_{y} \beta_{x} \beta_{y}\right) \\
&+\lambda^{4}\left(\alpha_{y}^{2} \beta_{y}^{2}-\alpha_{x} \alpha_{y} \beta_{x} \beta_{y}-\alpha_{y} \alpha_{z} \beta_{y} \beta_{z}\right) \\
&+\lambda^{5}\left(\alpha_{x}^{2} \beta_{z}^{2}-\alpha_{x} \alpha_{z} \beta_{x} \beta_{z}\right)+\lambda^{6}\left(\alpha_{y}^{2} \beta_{z}^{2}-\alpha_{y} \alpha_{z} \beta_{y} \beta_{z}\right) \\
&+4 \lambda^{7} \alpha_{x} \alpha_{y} \beta_{x} \beta_{y}+4 \lambda^{8} \alpha_{x} \alpha_{z} \beta_{x} \beta_{z}+4 \lambda^{8} \alpha_{y} \alpha_{z} \beta_{y} \beta_{z}.
\end{aligned}
$$

![](./images/1109550803607093272_8.jpg)

Figure I.8: Magnetic exchange interactions of the AFM1 MnPt phase.

## Appendix I. Exchange interactions

The atomistic spin simulations (main text Figure 5) employed the following isotropic exchange interaction constants up to the $6^{th}$ nearest neighbor shell (Fig I.8). The calculated magnitudes of the exchange interactions agree with the literature [15].

## References

[1] S. Chikazumi, C. D. Graham, Jr, Physics of Ferromagnetism, 2nd Edition, International series of monographs on physics, Oxford University Press, New York, USA, 1997. doi:10.1093/oso/9780198517764.001.0001.
URL https://doi.org/10.1093/oso/9780198517764.001.0001

[2] N. Ekreem, A. Olabi, T. Prescott, A. Rafferty, M. Hashmi, An overview of magnetostriction, its use and methods to measure these properties, Journal of Materials Processing Technology 191 (1) (2007) 96–101, advances in Materials and Processing Technologies, July 30th - August 3rd 2006, Las Vegas, Nevada. doi:https://doi.org/10.1016/j.jmatprotec.2007.03.064.
URL https://www.sciencedirect.com/science/article/pii/S0924013607002889

[3] B. Spetzler, C. Bald, P. Durdaut, J. Reermann, C. Kirchhof, A. Teplyuk, D. Meyners, E. Quandt, M. Höft, G. Schmidt, F. Faupel, Exchange biased delta-E effect enables the detection of low frequency pT magnetic fields with simultaneous localization, Scientific Reports 11 (1) (2021) 5269. doi:10.1038/s41598-021-84415-2.
URL https://doi.org/10.1038/s41598-021-84415-2

[4] F. T. Calkins, A. B. Flatau, M. J. Dapino, Overview of magnetostrictive sensor technology, Journal of Intelligent Material Systems and Structures 18 (10) (2007) 1057–1066. arXiv:https://doi.org/10.1177/1045389X06072358, doi:10.1177/1045389X06072358.
URL https://doi.org/10.1177/1045389X06072358

[5] A. Bieńkowski, R. Szewczyk, The possibility of utilizing the high permeability magnetic materials in construction of magnetoelastic stress and force sensors, Sensors and Actuators A: Physical 113 (3) (2004) 270–276, new materials and Technologies in Sensor Applications, Proceedings of the European Materials Research Society 2003 - Symposium N. doi:https://doi.org/10.1016/j.sna.2004.01.010.
URL https://www.sciencedirect.com/science/article/pii/S0924424704000172

[6] P. Kuszewski, I. S. Camara, N. Biarrotte, L. Becerra, J. von Bardeleben, W. Savero Torres, A. Lemaître, C. Gourdon, J.-Y. Duquesne, L. Thevenard, Resonant magneto-acoustic switching: influence of rayleigh wave frequency and wavevector, Journal of Physics: Condensed Matter 30 (24) (2018) 244003. doi:10.1088/1361-648X/aac152.
URL https://dx.doi.org/10.1088/1361-648X/aac152

[7] D. Legut, P. Nieves, Second-order anisotropy due to magnetostriction for L1₀-FePt, Solid State Sciences 160 (2025) 107782. doi:https://doi.org/10.1016/j.solidstatesciences

.2024.107782.
URL https://www.sciencedirect.com/science/article/pii/S1293255824003479

[8] T. Das, P. Nieves, D. Legut, Large magnetocrystalline anisotropic energy and its impact on magnetostriction of L1₀-FePt, Journal of Physics D: Applied Physics 58 (3) (2024) 035004. doi:10.1088/1361-6463/ad8001.
URL https://dx.doi.org/10.1088/1361-6463/ad8001

[9] P. Ravindran, A. Kjekshus, H. Fjellvåg, P. James, L. Nordström, B. Johansson, O. Eriksson, Large magnetocrystalline anisotropy in bilayer transition metal phases from first-principles full-potential calculations, Phys. Rev. B 63 (2001) 144409. doi:10.1103/PhysRevB.63.144409.
URL https://link.aps.org/doi/10.1103/PhysRevB.63.144409

[10] M. M. Soares, M. De Santis, H. C. N. Tolentino, A. Y. Ramos, M. El Jawad, Y. Gauthier, F. Yildiz, M. Przybylski, Chemically ordered mnpt ultrathin films on Pt(001) substrate: Growth, atomic structure, and magnetic properties, Phys. Rev. B 85 (2012) 205417. doi:10.1103/PhysRevB.85.205417.
URL https://link.aps.org/doi/10.1103/PhysRevB.85.205417

[11] A. B. Shick, F. Máca, M. Ondráček, O. N. Mryasov, T. Jungwirth, Large magnetic anisotropy and tunneling anisotropic magnetoresistance in layered bimetallic nanostructures: Case study of Mn/W(001), Phys. Rev. B 78 (2008) 054413. doi:10.1103/PhysRevB.78.054413.
URL https://link.aps.org/doi/10.1103/PhysRevB.78.054413

[12] Q. ul ain, D. D. Cuong, D. Odkhuu, S. Rhim, S. Hong, Thickness effect on magnetocrystalline anisotropy of MnPt(001) film, Journal of Magnetism and Magnetic Materials 467 (2018) 69-73. doi:https://doi.org/10.1016/j.jmmm.2018.07.055.
URL https://www.sciencedirect.com/science/article/pii/S0304885318304086

[13] H. Hama, R. Motomura, T. Shinozaki, Y. Tsunoda, Spin-flip transition of L1₀-type MnPt alloy single crystal studied by neutron scattering, Journal of Physics: Condensed Matter 19 (17) (2007) 176228. doi:10.1088/0953-8984/19/17/176228.
URL https://dx.doi.org/10.1088/0953-8984/19/17/176228

[14] M. Kubota, K. Ono, R. Y. Umetsu, H. Akinaga, A. Sakuma, K. Fukamichi, Pseudogap formation in MnPt and MnPd alloys, Applied Physics Letters 90 (9) (2007) 091911. arXiv:https://pubs.aip.org/aip/apl/article-pdf/doi/10.1063/1.2561008/13159938/091911\_1\_online.pdf, doi:10.1063/1.2561008.
URL https://doi.org/10.1063/1.2561008

[15] K. Kang, D. G. Cahill, A. Schleife, Phonon, electron, and magnon excitations in antiferromagnetic L1₀-type MnPt, Phys. Rev. B 107 (2023) 064412. doi:10.1103/PhysRevB.107.064412.
URL https://link.aps.org/doi/10.1103/PhysRevB.107.064412

[16] L. Pál, E. Krén, G. Kádár, P. Szabó, T. Tarnóczi, Magnetic structures and phase transformations in Mn-based CuAu-I type alloys, Journal of Applied Physics 39 (2) (1968) 538-544. arXiv:https://pubs.aip.org/aip/jap/article-pdf/39/2/538/18345168/538\_1\_online.pdf, doi:10.1063/1.2163510.
URL https://doi.org/10.1063/1.2163510

[17] E. Krén, G. Kádár, L. Pál, J. Sólyom, P. Szabó, T. Tarnóczi, Magnetic structures and exchange interactions in the Mn-Pt system, Phys. Rev. 171 (1968) 574-585. doi:10.1103/PhysRev.171.574.
URL https://link.aps.org/doi/10.1103/PhysRev.171.574

[18] M. M. Schwickert, J. R. Childress, R. E. Fontana, A. J. Kellock, P. M. Rice, M. K. Ho, T. J. Thompson, B. A. Gurney, Magnetic tunnel

junctions with AlN and AlNxOy barriers, Jour- nal of Applied Physics 89 (11) (2001) 6871-6873.
arXiv:https://pubs.aip.org/aip/jap/article-pdf/89/11/6871/19011945/6871\_1\_online.pdf, doi:10.1063/1.1361046.
URL https://doi.org/10.1063/1.1361046

[19] J. R. Childress, M. M. Schwickert, R. E. Fontana, M. K. Ho, P. M. Rice, B. A. Gurney, Low-resistance IrMn and PtMn tunnel valves for recording head applications, Journal of Applied Physics 89 (11) (2001) 7353-7355. arXiv:https://pubs.aip.org/aip/jap/article-pdf/89/11/7353/19215608/7353\_1\_online.pdf, doi:10.1063/1.1361050.
URL https://doi.org/10.1063/1.1361050

[20] M. Saito, N. Hasegawa, F. Koike, H. Seki, T. Kuriyama, Ptmn single and dual spin valves with synthetic ferrimagnet pinned layers, Jour- nal of Applied Physics 85 (8) (1999) 4928-4930.
arXiv:https://pubs.aip.org/aip/jap/article-pdf/85/8/4928/18931430/4928\_1\_online.pdf, doi:10.1063/1.369145.
URL https://doi.org/10.1063/1.369145

[21] A. Khapikov, B. Simion, M. Lederman, Mag- netic and thermal properties of PtMn giant mag- netoresistive sensors, Journal of Applied Physics93 (10) (2003) 7313-7315. arXiv:https://pubs.aip.org/aip/jap/article-pdf/93/10/7313/18931815/7313\_1\_online.pdf, doi:10.1063/1.1557366.
URL https://doi.org/10.1063/1.1557366

[22] D. Aissat, N. Baadji, H. Mazouz, A. Boussendel, Connection between lattice parameters and magnetocrystalline anisotropy in the case of L1₀ ordered antiferromagnetic MnPt, Journal of Magnetism and Magnetic Materials 563 (2022)170013. doi:https://doi.org/10.1016/j.jmmm.2022.170013.
URL https://www.sciencedirect.com/science/article/pii/S0304885322008988

[23] L. Landau, L. Landau, E. Lifshits, A. Kose- vich, E. Lifshitz, L. Pitaevskii, Butterworth- Heinemann, Oxford, 1986. doi:https://doi. org/10.1016/B978-0-08-057069-3.50008-5,[link].
URL https://www.sciencedirect.com/science/article/pii/B9780080570693500085

[24] P. Nieves, S. Arapan, S. Zhang, A. Kadzielawa, R. Zhang, D. Legut, Maelas: Magneto-elastic properties calculation via computational hig- hthroughput approach, Computer Physics Com- munications 264 (2021) 107964. doi:https://doi.org/10.1016/j.cpc.2021.107964.
URL https://www.sciencedirect.com/science/article/pii/S0010465521000801

[25] B. Cullity, C. Graham, Introduction to Magnetic Materials, John Wiley & Sons, Ltd, New Jersey,2008. doi:https://doi.org/10.1002/9780470386323.ch8.

[26] G. Engdahl, I. D. Mayergoyz, Handbook of giant magnetostrictive materials, Vol. 107, Academic Press, San Diego, 2000. doi:https://doi.org/10.1016/B978-012238640-4.

[27] A. Clark, Chapter 7 magnetostrictive rare earth- Fe2 compounds, Vol. 1 of Handbook of Ferro- magnetic Materials, Elsevier, 1980, pp. 531-589.doi:https://doi.org/10.1016/S1574-9304(05)80122-1.
URL https://www.sciencedirect.com/science/article/pii/S1574930405801221

[28] P. Nieves, S. Arapan, S. Zhang, A. Kadzielawa, R. Zhang, D. Legut, Automated calculations of exchange magnetostriction, Computational Ma- terials Science 224 (2023) 112158. doi:https://doi.org/10.1016/j.commatsci.2023.112158.
URL https://www.sciencedirect.com/science/article/pii/S0927025623001520

[29] E. R. Callen, A. E. Clark, B. DeSavage, W. Cole- man, H. B. Callen, Magnetostriction in cu- bic Néel ferrimagnets, with application to YIG,Phys. Rev. 130 (1963) 1735-1740. doi:10.1103/PhysRev.130.1735.
URL https://link.aps.org/doi/10.1103/PhysRev.130.1735

[30] P. Nieves, S. Arapan, S. Zhang, A. Kadzielawa, R. Zhang, D. Legut, Maelas 2.0: A new ver- sion of a computer program for the calculation of magneto-elastic properties, Computer Physics Communications 271 (2022) 108197. doi:https://doi.org/10.1016/j.cpc.2021.108197.
URL https://www.sciencedirect.com/science/article/pii/S001046552100309X

[31] J. Rodríguez-Carvajal, Recent advances in mag- netic structure determination by neutron pow- der diffraction, Physica B: Condensed Matter 192 (1) (1993) 55-69. doi:https://doi.org/10.1016/0921-4526(93)90108-I.
URL https://www.sciencedirect.com/science/article/pii/092145269390108I

[32] M. Rotter, H. Müller, E. Gratz, M. Do- err, M. Loewenhaupt, A miniature capacitance dilatometer for thermal expansion and mag- netostriction, Review of Scientific Instruments 69 (7) (1998) 2742-2746. arXiv:https://pubs.aip.org/aip/rsi/article-pdf/69/7/2742/19318373/2742\_1\_online.pdf, doi:10.1063/1.1149009.
URL https://doi.org/10.1063/1.1149009

[33] G. Kresse, J. Furthmüller, Efficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set, Phys. Rev. B 54 (1996) 11169-11186. doi:10.1103/PhysRevB.54.11169.
URL https://link.aps.org/doi/10.1103/PhysRevB.54.11169

[34] G. Kresse, D. Joubert, From ultrasoft pseu- dopotentials to the projector augmented-wave method, Phys. Rev. B 59 (1999) 1758-1775. doi:10.1103/PhysRevB.59.1758.
URL https://link.aps.org/doi/10.1103/PhysRevB.59.1758

[35] J. P. Perdew, K. Burke, M. Ernzerhof, Gen- eralized gradient approximation made simple, Phys. Rev. Lett. 77 (1996) 3865-3868. doi:10.1103/PhysRevLett.77.3865.
URL https://link.aps.org/doi/10.1103/PhysRevLett.77.3865

[36] S. Zhang, R. Zhang, Aelas: Automatic elastic property derivations via high-throughput first- principles computation, Computer Physics Com- munications 220 (2017) 403-416. doi:https://doi.org/10.1016/j.cpc.2017.07.020.
URL https://www.sciencedirect.com/science/article/pii/S0010465517302400

[37] J. M. Wills, M. Alouani, P. Andersson, A. Delin, O. Eriksson, O. Grechnyev, The Full-Potential Electronic Structure Problem and RSPt, Springer Berlin Heidelberg, Berlin, Hei- delberg, 2010, pp. 47-73. doi:10.1007/978-3-642-15144-6_6.
URL https://doi.org/10.1007/978-3-642-15144-6_6

[38] Y. O. Kvashnin, O. Grånäs, I. Di Marco, M. I. Katsnelson, A. I. Lichtenstein, O. Eriksson, Ex- change parameters of strongly correlated ma- terials: Extraction from spin-polarized density functional theory plus dynamical mean-field the- ory, Phys. Rev. B 91 (2015) 125133. doi:10.1103/PhysRevB.91.125133.
URL https://link.aps.org/doi/10.1103/PhysRevB.91.125133

[39] J. P. Perdew, Y. Wang, Accurate and simple an- alytic representation of the electron-gas corre- lation energy, Phys. Rev. B 45 (1992) 13244-13249. doi:10.1103/PhysRevB.45.13244.
URL https://link.aps.org/doi/10.1103/PhysRevB.45.13244

[40] A. Szilva, Y. Kvashnin, E. A. Stepanov, L. Nord- ström, O. Eriksson, A. I. Lichtenstein, M. I. Katsnelson, Quantitative theory of magnetic in- teractions in solids, Rev. Mod. Phys. 95 (2023) 035004. doi:10.1103/RevModPhys.95.035004.
URL https://link.aps.org/doi/10.1103/RevModPhys.95.035004

[41] B. Skubic, J. Hellsvik, L. Nordström, O. Eriks- son, A method for atomistic spin dynamics simu- lations: implementation and examples, Journal of Physics: Condensed Matter 20 (31) (2008) 315203. doi:10.1088/0953-8984/20/31/315203.

URL https://dx.doi.org/10.1088/0953-8984/20/31/315203

[42] K. Momma, F. Izumi, VESTA3 for three- dimensional visualization of crystal, volumet- ric and morphology data, Journal of AppliedCrystallography 44 (6) (2011) 1272-1276. doi:10.1107/S0021889811038970.
URL https://doi.org/10.1107/S0021889811038970

[43] Z. Lu, R. V. Chepulskii, W. H. Butler, First-principles study of magnetic properties of $L1_{0^{-}}$ ordered mnpt and fept alloys, Phys. Rev. B 81(2010) 094437. doi:10.1103/PhysRevB.81.094437.
URL https://link.aps.org/doi/10.1103/PhysRevB.81.094437

[44] C. S. Severin, C. W. Chen, Ferromagnetic behav- ior of disordered MnPt films produced by rf sput-tering, Journal of Applied Physics 49 (3) (1978)1693-1695. arXiv:https://pubs.aip.org/aip/jap/article-pdf/49/3/1693/18378964/1693_1_online.pdf, doi:10.1063/1.324891.
URL https://doi.org/10.1063/1.324891

[45] J. Wang, A. Gao, W. Chen, X. Zhang, B. Zhou, Z. Jiang, The structural, elastic, phonon, ther- mal and electronic properties of MnX (X=Ni, Pd and Pt) alloys: First-principles calculations, Journal of Magnetism and Magnetic Materials333 (2013) 93-99. doi:https://doi.org/10.1016/j.jmmm.2012.12.050.
URL https://www.sciencedirect.com/science/article/pii/S0304885312010360

[46] P. Ravindran, A. Kjekshus, H. Fjellvag, P. James, L. Nordstrom, B. Johansson, O. Eriks- son, Large magnetocrystalline anisotropy in bilayer transition metal phases from first- principles full-potential calculations, Phys. Rev.B 63 (2001) 144409. doi:10.1103/PhysRevB.63.144409.
URL https://link.aps.org/doi/10.1103/PhysRevB.63.144409

[47] E. Callen, H. B. Callen, Magnetostriction, forced magnetostriction, and anomalous thermal ex-pansion in ferromagnets, Phys. Rev. 139 (1965) A455-A471. doi:10.1103/PhysRev.139.A455.
URL https://link.aps.org/doi/10.1103/PhysRev.139.A455

[48] D. Fritsch, C. Ederer, First-principles calcula- tion of magnetoelastic coefficients and magne- tostriction in the spinel ferrites $CoFe_{2} O_{4}$ andNiFe2O4, Phys. Rev. B 86 (2012) 014406. doi:10.1103/PhysRevB.86.014406.
URL https://link.aps.org/doi/10.1103/PhysRevB.86.014406

[49] R. M. A. F. Andresen, A. Kjekshus, W. B. Pear- son, Equiatomic transition metal alloys of man- ganese iv. a neutron diffraction study of mag- netic ordering in the ptmn phase, The Philo- sophical Magazine: A Journal of Theoretical Ex-perimental and Applied Physics 11 (114) (1965)1245-1256. arXiv:https://doi.org/10.1080/14786436508224933, doi:10.1080/14786436508224933.
URL https://doi.org/10.1080/14786436508224933

[50] F. Mouhat, F. m. c.-X. Coudert, Necessary and sufficient elastic stability conditions in various crystal systems, Phys. Rev. B 90 (2014) 224104. doi:10.1103/PhysRevB.90.224104.
URL https://link.aps.org/doi/10.1103/PhysRevB.90.224104

[51] D. Legut, J. Pavlů, Electronic structure and elasticity of Z-phases in the Cr-Nb-V-N system,Journal of Physics: Condensed Matter 24 (19)(2012) 195502. doi:10.1088/0953-8984/24/19/195502.
URL https://dx.doi.org/10.1088/0953-8984/24/19/195502

[52] O. N. Senkov, D. B. Miracle, Generalization of intrinsic ductile-to-brittle criteria by pugh and pettifor for materials with a cubic crystal struc-ture, Scientific Reports 11 (1) (2021) 4531. doi:10.1038/s41598-021-83953-z.

URL https://doi.org/10.1038/s41598-021-83953-z
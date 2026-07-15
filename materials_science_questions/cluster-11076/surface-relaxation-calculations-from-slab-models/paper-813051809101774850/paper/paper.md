Accepted Manuscript

![](./images/813051809101774850_1.jpg)

The surface energy and stress of metals

J.-Y. Lee, M.P.J. Punkkinen, S. Schönecker, Z. Nabi,
K. Kádas, V. Zólyomi, Y.M. Koo, Q.-M. Hu, R. Ahuja,
B. Johansson, J. Kollár, L. Vitos, S.K. Kwon

<table>
  <tr>
    <td>PII:</td>
    <td>S0039-6028(18)30085-2</td>
  </tr>
  <tr>
    <td>DOI:</td>
    <td>10.1016/j.susc.2018.03.008</td>
  </tr>
  <tr>
    <td>Reference:</td>
    <td>SUSC 21211</td>
  </tr>
  <tr>
    <td>To appear in:</td>
    <td>Surface Science</td>
  </tr>
  <tr>
    <td>Received date:</td>
    <td>25 January 2018</td>
  </tr>
  <tr>
    <td>Accepted date:</td>
    <td>11 March 2018</td>
  </tr>
</table>

Please cite this article as: J.-Y. Lee, M.P.J. Punkkinen, S. Schönecker, Z. Nabi, K. Kádas,
V. Zólyomi, Y.M. Koo, Q.-M. Hu, R. Ahuja, B. Johansson, J. Kollár, L. Vitos, S.K. Kwon, The
surface energy and stress of metals, Surface Science (2018), doi: 10.1016/j.susc.2018.03.008

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service
to our customers we are providing this early version of the manuscript. The manuscript will undergo
copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please
note that during the production process errors may be discovered which could affect the content, and
all legal disclaimers that apply to the journal pertain.

### Highlights

-   Ab initio calculation of the surface relaxation of metals
-   Surface energy and surface stress of transition metals
-   Surface energy and surface stress of simple metals and light actinides

# The surface energy and stress of metals

J.-Y. Lee¹, M. P. J. Punkkinen², S. Schönecker³, Z. Nabi⁴, K. Kádas⁵⁶, V. Zólyomi⁶⁷, Y. M. Koo¹, Q.-M. Hu⁸, R. Ahuja³⁵, B. Johansson³⁵, J. Kollár⁶†, L. Vitos³⁵⁶*, and S. K. Kwon¹*

¹Graduate Institute of Ferrous Technology, Pohang University of Science and Technology, Pohang 37673, Korea

²Department of Physics and Astronomy, University of Turku, FI-20014 Turku, Finland

³Applied Materials Physics, Department of Materials Science and Engineering, KTH - Royal Institute of Technology, Stockholm SE-100 44, Sweden

⁴Laboratory of Catalysis and Reactive Systems, Physics Department, University of Sidi Bel Abbès, 22000, Algeria

⁵Department of Physics and Astronomy, Division of Materials Theory, Uppsala University, Box 516, SE-75120 Uppsala, Sweden

⁶Institute for Solid State Physics and Optics, Wigner Research Centre for Physics, H-1525 Budapest, P.O. Box 49, Hungary

⁷National Graphene Institute, University of Manchester, Manchester, M13 9PL, United Kingdom

⁸Shenyang National Laboratory for Materials Science, Institute of Metal Research, Chinese Academy of Sciences, 72 Wenhua Road, Shenyang 110016, China

We investigated surface properties of metals by performing first-principles calculations. A systematic database was established for the surface relaxation, surface energy ($\gamma$), and surface stress ($\tau$) for metallic elements in the periodic table. The surfaces were modeled by multi-layered slab structures along the direction of low-index surfaces. The surface energy $\gamma$ of simple metals decreases as the atomic number increases in a given group, while the surface stress $\tau$ has its minimum in the middle. The transition metal series show parabolic trends for both $\gamma$ and $\tau$ with a dip in the middle. The dip occurs at half-band filling due to a long-range Friedel oscillation of the surface charge density, which induces a strong stability to the Peirels-like transition. In addition, due to magnetic effects, the dips in the $3d$ metal series are shallower and deeper for $\gamma$ and $\tau$, respectively, than those of the $4d$ and $5d$ metals. The surface stress of the transition metals is typically positive, only Cr and Mn have a negative $\tau$ for the (100) surface facet, indicating that they are under compression. The light actinides have an increasing $\gamma$ trend according to the atomic number. The present work provides a useful and consistent database for the theoretical modelling of surface phenomena.

Keywords: Surface relaxation; Surface energy; Surface stress; Density-functional theory calculations; Metals

*To whom correspondence should be addressed. E-mail: sekk@postech.ac.kr (S.K.K) and levente@kth.se (L.V)
†Deceased.

### 1. Introduction

The surface energy ($\gamma$) and the surface stress ($\tau$) are regarded as fundamental quantities to understand surface-related phenomena. In liquids, the surface energy and the surface stress are equal to each other. On the other hand, they differ in solids and we have $\tau_{ij}-\gamma\delta_{ij}=\partial\gamma/\partial\varepsilon_{ij}$ with the strain $\varepsilon_{ij}$ on the surface plane. For high symmetry surfaces, the scalar surface stress $\tau$ can be introduced for the average stress. These surface parameters strongly depend on the crystalline structure [1] and the geometry of solid surfaces have continuously been an important subject of surface science.

Metals can transform surface structures and/or modify structural parameters from those of ideally as-truncated crystals due to the layer relaxation and reconstruction. For the layer relaxation, experimental results have shown that the top layer of transition metal surfaces tends to relax inward [2], while outward relaxation can arise for some noble metals. The top layer relaxation usually induces sub-surface layer relaxations. Several theoretical models have been proposed to explain the relaxation behaviors. Punkkinen *et al.* [2] elucidated the development of models for transition metals. Here, we extend previous results [3, 4] by a systematic approach to the layer relaxation and $\gamma$ and $\tau$ of metal surfaces. It is shown that the layer relaxation is connected to $\gamma$ and $\tau$ by a quadratic relationship and a linear relationship, respectively [1, 2].

Presently, the direct measurement of the surface quantities $\gamma$ and $\tau$ is not easy. Accordingly, most of the available data have been obtained from the extrapolation of measurements on liquid phases, which is limited to isotropic crystals and not feasible for a specific surface orientation [5, 6]. Therefore, theoretical surveys of these properties have been crucial in the subject. Among several theoretical methods, two techniques are routinely used. Semi-empirical molecular dynamics methods, which are fast and computationally economical, have been helpful to understand trends of surface energetics for various materials [7-12], while leaving some doubts of reliability and accuracy. In contrast, first-principles methods are computationally expensive but provide reliable data. Thus, they have been widely spreading for a broad scope of materials research with the rapid development of computing resources. Intensive first-principles studies on the surface energies of metals have been reported by several workers [13-20], and there exist some results on various surface facets of metals determined with different methods [1-4, 21-25]. Here we should mention the database by Vitos *et al.* [4], which during the last two decades presented the most complete reference for surface energy and surface energy anisotropies of sixty metals from the period table. Vitos *et al.* [4] used the full-charge density linear muffin-tin orbitals (FCD-LMTO) method, which ensured sufficient accuracy for the surface excess energies but was not suitable to study the surface relaxation and surface stress. The purpose of

this paper is to revise and complement the previous works by compiling first-principles data for layer relaxation, surface energy, and surface stress for the low-index surfaces and thus providing an up-to-date and reliable database for metallic elements in the periodic table. We briefly describe the applied computational schemes in Section 2 and discuss results in Section 3.

## 2. Calculation methods

### 2.1. Surface energy and surface stress

The surface energy $\gamma$ is defined by the reversible work per surface area to form a surface,

$$
\gamma=\frac{E^{s}-E^{b}}{A}, \tag{1}
$$

where $E^{s}$ is the total energy of the system with surface, $E^{b}$ is the total energy of the bulk system without surface, and $A$ is the surface area. The number of atoms in the system is considered to be conserved. The surface stress $\tau$ is a tensorial quantity defined by the reversible work per surface area to stretch the surface in an elastic way and can be expressed in the form of the Shuttleworth equation [26],

$$
\tau_{i j}=\frac{1}{A} \frac{\partial(A \gamma)}{\partial \varepsilon_{i j}}=\gamma \delta_{i j}+\frac{\partial \gamma}{\partial \varepsilon_{i j}}, \tag{2}
$$

where $\tau_{i j}$ is the surface stress tensor, $\varepsilon_{i j}$ is the in-plane surface strain tensor, and $\delta_{i j}$ is the Kronecker delta ($\delta_{i j}=1$ for $i=j$ and $\delta_{i j}=0$ for otherwise). All the quantities in Eqs. (1) and (2) are evaluated for unstrained lattice, viz., $\varepsilon_{i j}=0$.

The two surface parameters $\gamma$ and $\tau$ depend on the layer relaxation in general. In order to understand the main relaxation effects, here we assume top layer relaxation only which actually gives the most significant effects compared to the subsurface layers. Accordingly, we have the inter-layer distance $\lambda$ at the surface, which is different from the bulk value $\lambda_{0}$. With the in-plane biaxial strain $\varepsilon$ [27, 28] and the ratio of the change of the inter-layer distance at the surface to the layer distance in the bulk $\delta=(\lambda-\lambda_{0}) / \lambda_{0}$, the slab energy of a multi-layered system relative to the bulk energy is formally given by

$$
E^{s}(\varepsilon, \delta)-E^{b}(\varepsilon) \cong E^{s}(0,0)-E^{b}(0)+A_{0}\left(\tau_{0} \varepsilon+\frac{1}{2} \gamma_{\varepsilon} \varepsilon^{2}+\frac{1}{2} \gamma_{\delta} \delta^{2}+\tau_{0}^{\prime} \varepsilon \delta\right), \tag{3}
$$

where $\tau_{0}, \gamma_{\varepsilon}, \gamma_{\delta}$, and $\tau_{0}^{\prime}$ are the expansion coefficients, and $A_{0}$ is the surface area of the undistorted

lattice. The slab energy $E^{s}(0,0)$ corresponds to the layer-relaxed structure in equilibrium. Note that the bulk energy $E^{b}(\varepsilon)$ does not depend upon $\delta$ and only the second and higher order terms in $\varepsilon$ appear. Therefore, the term linear in $\delta$ vanishes on the right side of the expansion.

Taking into account an infinitesimal strain $\varepsilon \to 0$, we can identify the surface energy and surface stress from the terms of Eq. (3) as

$$
\gamma(\delta) \cong \gamma(0)+\frac{1}{2} \gamma_{\delta} \delta^{2} \tag{4}
$$

and

$$
\tau(\delta) \cong \tau(0)+\tau_{0}^{\prime} \delta, \tag{5}
$$

where $\gamma(0)=\{E^{s}(0,0)-E^{b}(0)\}/A_{0}$ and $\tau(0)=\tau_{0}$ by definition, and $\tau_{0}^{\prime}$ is the derivative of $\tau(\delta)$ at $\delta=0$. Thus it is found that the surface stress is more strongly linearly dependent on the layer relaxation than the surface energy quadratically [1,2].

In order to evaluate the surface stress, a slab formed by a number of parallel atomic layers is usually considered and embedded in vacuum. The bulk structure is relaxed to the equilibrium to obtain the lattice parameters. With the equilibrium inter-layer distance $\lambda_{0}$, multi-layer relaxation calculations are performed along the perpendicular direction to the surface plane. From the relaxed slab geometry, we elongate the lattice vectors within the surface plane by $\varepsilon$ while keeping the inter-layer distances fixed. This deformation can be represented by the strain tensor,

$$
\varepsilon_{i j}=\left[\begin{array}{lll}
\varepsilon & 0 & 0 \\
0 & \varepsilon & 0 \\
0 & 0 & 0
\end{array}\right]. \tag{6}
$$

We usually carry out calculations of $E^{s}$ and $E^{b}$ with a few small deformations, for example, $\varepsilon=0, \pm 0.01$, and $\pm 0.02$ and fit them to a quadratic polynomial

$$
E^{s / b}(\varepsilon) \cong E^{s / b}(0)+c_{1}^{s / b} \varepsilon+c_{2}^{s / b} \varepsilon^{2}, \tag{7}
$$

where $c_{1}^{s / b}$ and $c_{2}^{s / b}$ are the coefficients of fitting. Then, the surface stress is determined from the linear coefficients of the slab and bulk energies as

$$
\tau=\frac{c_{1}^{s}-c_{1}^{b}}{4 A}. \tag{8}
$$

The factor 4 comes from the double-sided surfaces of the slab and the homogeneous in-plane deformation [22, 27]. Finally we mention that the difference between the surface stress and the surface energy $(\tau-\gamma)$ has previously been proposed as a measure of the driving force for surface reconstruction (see Refs. [2, 21] and references therein).

### 2.2. Numerical details
All calculations were performed within density-functional theory (DFT) [29]. To describe the electronic system with DFT, one needs to solve the one-electron Kohn-Sham problem [30] accurately and efficiently. In the present work, we employed the project augmented wave (PAW) method [31] as implemented within the Vienna Ab initio Simulation Package (VASP) [32, 33]. The exchange-correlation interaction was described by the generalized gradient approximation (GGA) [34, 35]. All calculation results including layer relaxation and surface stress were considered in comparison with previous theoretical and experimental data. Especially, the surface energy results of the PAW method were compared mainly with those obtained by the full-charge-density (FCD) approach within the linear muffin-tin orbitals (LMTO) method [36-39].

For $3d$ and $4d$ metals, the slab model of the surface consisted of 8 atomic layers for the face-centered cubic (fcc) (111) and (100) surfaces, 12 atomic layers for the body-centered cubic (bcc) (110) and the hexagonal close-packed (hcp) (0001) surfaces, and 16 atomic layers for the bcc (100) surfaces. For $5d$ metals, the slabs were 10 atomic layers thick except the bcc and fcc (100) facets, which were composed of 12 layers. A sufficiently thick vacuum region (approximately $10\ \mathring{\text{A}}$) separated the two surfaces. Spin polarization was considered for the $3d$ elements. Chromium was treated as an antiferromagnetic state with B2 structure [40] and Fe, Co, and Ni as ferromagnetically ordered. Manganese was calculated with its complex antiferromagnetic structure ($\alpha$-Mn) with 58 atoms in the unit cell. The (110) surface of $\alpha$-Mn [41] was modeled by a slab containing 130 atoms separated by vacuum layers of thickness $12.2\ \mathring{\text{A}}$. The Brillouin zone sampling was done with the Monkhorst-Pack scheme [42]. The plane wave cut-off energy was chosen as 450 ~ 500 eV for $3d$ metals, 340 ~ 460 eV for $4d$ metals, and 350 eV for $5d$ metals. All surfaces were subjected to surface layer relaxation, but surface reconstruction was not considered. Finally, for all surface facets the surface stress was determined through isotropic biaxial in-plane strains.

## 3. Results and discussion
The calculated results of the equilibrium bulk lattice constant, $c/a$ ratio, surface relaxation, surface energy, and surface stress are listed in Tables 1-5 for simple metals, $3d$, $4d$, $5d$ metals, and light

actinides, respectively. Below we discuss all sets of data separately.

### 3.1. Simple metals
For the alkali metals, we observe that the layer relaxation rapidly decays with the distance from the surface. The first layer relaxation is dominantly negative and the other layer relaxations are smaller by one order of magnitude. The top layer relaxation is significant, $d_{12} = -4.33$ % for Li, small $d_{12} = -0.98$ % for Na, and almost negligible for K, Rb, and Cs. This follows the trend of the atomic radius that increases from Li, Na, K, Rb to Cs.

The alkaline-earth metals and the other divalent sp metals including Zn and Cd show a layer relaxation in the opposite direction. The layer relaxation is positive for Be and Mg and becomes negative for Ca, Sr, and Ba in order of the atomic radius (see Table 1). The first layer relaxation also becomes smaller from 0.69% for Zn to 0.10% for Cd. These results are different from those of the alkali metals, where the relaxation pattern changes from negative values to positive ones as the atomic radius increases. It is also interesting to note that the relaxation trend of the most close-packed surface is rather independent on the bulk crystalline structure of metals. Moreover, as is evident from Table 1, the present PAW results for the layer relaxation are consistent with the previous theoretical and experimental data existing for Na, Be, Mg, Al, and Pb.

Figure 1 shows the surface energy of simple metals having sp valence electrons. The present results from the PAW method are mostly in good agreement with those of the FCD-LMTO method [4]. The surface energy of simple metals is found to be smaller than 1 J/m² except 1.77 J/m² for Be. As the atomic number increases, the surface energy decreases in each group of the periodic table. This might have a similar physical origin as the layer relaxation in Table 1. Especially for the alkali metals crystallizing in the bcc structure, it is clear that the larger the layer relaxation is, the larger the surface energy is. For comparison, Fig. 1 contains the range of previously reported data from other theoretical and experimental approaches. The present surface energy values are mostly within the range of previous data. Though for Be, Mg, Al, and Pb the ranges are rather scattered, but in general they exhibit the trends of decreasing surface energy according to the increase of atomic numbers, as the present PAW results demonstrate.

Differently from the surface energy, the surface stress of simple metals is somewhat scattered; see Fig. 2. For the alkali metals, the surface stress is well bounded and between -0.29 J/m² and 0.12 J/m², which are the values for K and Na, respectively. Beryllium has the largest surface stress $\tau = 2.99$ J/m² among the considered simple metals. The surface stress of the alkaline-earth metals decreases from Be

and Mg to Ca and increases again to Sr and Ba, forming the minimum value of $\tau = -0.85\ \text{J/m}^2$ for Ca. Although it is not as apparent as the case of the alkaline-earth metals, the surface stress of the alkaline metals also shows a shallow minimum for K. In addition, the difference between the surface stress and energy $(\tau - \gamma)$ is positive for Be, Mg, Zn, Cd, Al, In and Tl, which exhibit an outward layer relaxation.

### 3.2. Transition metals

The lattice parameters, the surface energy, and the surface stress are listed in Tables 2-4 for $3d$, $4d$, and $5d$ transition metals, respectively. It is understood that the open surface structure, the (100) surface of bcc and fcc, induces more severe layer relaxation than the close-packed surfaces, the (110) and (111) surface of bcc and fcc, respectively. The layer relaxation is most pronounced for the first layer and usually declines within 2-3 surface layers, similarly to the simple metals. However, Friedel oscillations of the interlayer distance [43-45] screening the surface perturbation can persist to larger depth in some cases. For example, both Tc and Re are half-filled in the $4d$ and $5d$ series, respectively, and their layer relaxation slowly diminishes leading to only $d_{12}/d_{34} \sim 0.45$.

Aside from magnetic influences, the top layer relaxation of the three transition metal series as a function of the $d$-occupation is similar. Chromium is antiferromagnetically ordered in the ground state and iron has a ferromagnetic ground state. The calculated top layer relaxations for the bcc (110) facets of Cr and Fe are only $-1.95\%$ and $-0.05\%$, respectively. These values are remarkably smaller in magnitude than those of adjacent non-magnetic $3d$ metals, for example, $d_{12} = -5.24\%$ for V. Molybdenum and Tungsten share the same number of valence electrons with Cr and their top layer relaxations are $d_{12} = -4.74\%$ and $-3.76\%$ for Mo and W, respectively. Also, the (0001) surfaces of Ru and Os, which have the same valence electron number as Fe, relax as much as $d_{12} = -3.96\%$ and $-3.79\%$, respectively. Hence, magnetic interactions and in particular the excess magnetic pressures near the surface are likely to prevent significant layer relaxation of the surfaces. These trends are also consistently found in the other listed theoretical and experimental data. Most of the top layer relaxation data of the (110) surface of Fe and Cr are below $1\%$ in magnitude, while those of Mo and W amount up to about $4\%$.

In addition, the behavior of Mn is quite noticeable. For the (110) facet, the $\alpha$-Mn structure has a less dense layer between the first and the third surface layer, which are relatively close-packed. The inter-layer distance between the loosely-packed second layer and the third layer is small, which eventually gives a too large value of $d_{23} = 12.30\%$. Therefore, we reconsider this structure discarding the relaxation of $d_{23}$ and obtain the first two inter-layer relaxations for $\alpha$-Mn as $d_{13}=0.99\%$ and $d_{34}=-$

1.83%, which are close in size to the results of Cr and Fe. Thus, the close-packed surfaces of the magnetic $3d$ metals exhibit unusually small layer relaxations and the positive magnetic pressure around the free surfaces would be the main cause of the phenomena of small relaxations.

One may also expect that the surface energy of a given element can be related to its cohesive energy as both of them scale with the bonding energy between constituent atoms. Especially, for transition metals, the surface energy per surface atom is roughly about 1/6 of the cohesive energy in bond-cutting models [17, 46]. Thus, the surface energy and the cohesive energy approximately follow the same trend in each of the three transition metal series.

In Fig. 3, we show the surface energies of $3d$, $4d$, and $5d$ transition metals. The surface energy of each period exhibits an approximately parabolic shape as a function of the $d$-electron occupation. When comparing the $4d$ with the $5d$ series, the surface energy of the $5d$ transition metals is larger than that of the $4d$ metals for the same valency, except at the end points. For the two elements bounding the $3d$ transition metal series, a higher surface energy is observed in comparison to that of the $4d$ and $5d$ metals. The data of both the PAW and the FCD-LMTO method are consistent in these main features and have an approximately parabolic shape. Most of the data point are found within the range of previously reported datasets. Specifically, many experimental surface energies lie in between the values of the PAW and FCD-LMTO methods or very close to them. We note that the FCD-LMTO results show higher surface energy values than the PAW partly due to the top-layer-only relaxation in the FCD-LMTO calculations.

The nearly parabolic shape of the surface energy across each transition metal series originates from the bonding nature of $d$-band electrons. Up to an approximately half-filled valance $d$-band, electrons predominantly occupy the bonding states enhancing the cohesive energy. After filling all the bonding states, anti-bonding states start to be occupied, which lowers the cohesive energy. The Friedel model reflects this fact and explains the $d$-electron contribution to the cohesion of transition metals. According to the model, the surface energy of transition metals undergoes a parabolic variation with atomic number [47]. The surface energy estimated from the measured surface tension of liquid metals also verifies the parabolic trend of transition metals [6].

Looking into the details, each curve obtained from the PAW method shows a dip in the middle. It is more pronounced in the $4d$ and $5d$ metals than in the $3d$ metals. The elements in the middle of the transition metal series, Mn, Tc, and Re, have half-filled $d$-bands. As mentioned above, these elements exhibit charge-density oscillations at the surface. These will stabilize the close-packed surface of Tc

and Re more easily leading to the lower surface energies compared to their neighboring elements. Furthermore, the correlation between the $d$-electrons is strong at the half-filled state and induces a stability to a Peierls-like bi-layer coupling. On the other hand, the effect is less pronounced in the bulk, resulting in a decreased value of the cohesive energy. We suggest that this mechanism introduces a dip in the parabolic surface energy curves.

Figure 4 shows the surface stress of transition metals. As one can see, most of the present PAW results are close to the preexisting data, and both of them show similar trends across each period. However, the ranges of the previous theoretical data for Pt and the experimental data for Pd and Cu are rather far from the present result. These disagreements may arise from the overestimation of surface stress by semi-empirical MEAM technique, and from the errors in lattice contraction measurement, for theoretical and experimental cases, respectively.

We also found that for the $4d$ and $5d$ metals, the surface stress as a function of the $d$-occupation varies similarly to the surface energy. For the early transition metals, the surface stress of the $5d$ metals is comparable to that of the $4d$ metals, whereas the other $5d$ metals have larger surface stresses than those of the $4d$ metals. The surface stress across the $4d$ and $5d$ transition metal series is approximately parabolic-shaped with a dip at approximately half $d$-band filling. Once again, the local minima are attributed to surface charge-density oscillations.

However, it is very interesting that the surface stress of the $3d$ transition metals behaves very differently from that of the $4d$ and $5d$ metals. As shown in Fig. 4, the surface stress of the $3d$ metals forms a deep sink instead of a shallow dip. Moreover, chromium and manganese have negative surface stress, $\tau = -0.32\ \mathrm{J/m^2}$ and $-0.22\ \mathrm{J/m^2}$, respectively, for the (100) surface, which is thermodynamically more stable than the (110) surface (see Table 2). These findings mean that the (100) surfaces of Cr and Mn are under compression and tend to expand the in-plane lattice constant relative to the bulk one. The surface stresses of Fe, Co, and Ni are also lower than those of the isoelectronic elements of the $4d$ and $5d$ series. In order to understand this difference, we note that magnetic order occurs only in the $3d$ metals. The magnetic moment magnitude of Cr, Mn, Fe, Co, and Ni is enhanced at the surface due to the reduced coordination number. This enhanced surface magnetism impedes significant surface layer relaxation, which would otherwise be large in the absence of spin polarization. The lesser layer relaxation would not give rise to a big change in the surface energy, because the surface energy change is of second order in the layer relaxation as shown in Eq. (4). On the contrary, the surface stress depends linearly on the layer relaxation, Eq. (5). Therefore, the impeded layer relaxation due to the magnetism can greatly affect the surface stress as observed in the

$3d$ transitional metals.

### 3.3 Light actinides
Examining the data in Table 5, for the multi-layer relaxation of some low-index surfaces of light actinides, we see that the relaxation decays rather fast with the distance from the surface. In addition, as the atomic number increases, the surface energy decreases. This was also reported in previous works [4, 48].

## 4. Conclusion
We have established a database of low-index surface properties for various metallic elements by employing a density-functional theory approach. Comparing with previous studies, the present work provides more complete and perhaps more accurate values of the surface energy and also embraces the multi-layer relaxation effects and the values of the surface stress. We expect that the database will be accessed as a useful reference in order to comprehend various kinds of surface phenomena of metallic materials.

## Acknowledgements
This work was supported by the Basic Science Research Program through the National Research Foundation of Korea (NRF-2017R1A2A1A18071775), the Swedish Research Council, the Swedish Foundation for Strategic Research, Sweden's Innovation Agency (VINNOVA Grant No. 2014-03374), the Swedish Foundation for International Cooperation in Research and Higher Education, the Carl Tryggers Foundation, the Swedish Energy Agency and the Hungarian Scientific Research Fund (OTKA 109570 and K-115608). The Swedish National Infrastructure for Computing at the National Supercomputer Centers in Linköping and Stockholm and the Finnish IT Center for Science (CSC) and the FGI project (Finland) are acknowledged.

## References
[1] S. K. Kwon, Z. Nabi, K. Kádas, L. Vitos, J. Kollár, B. Johansson, R. Ahuja, Surface energy and stress release by layer relaxation, Phys. Rev. B 72 (2005) 235423.

[2] M. P. J. Punkkinen, Q. –M. Hu, S. K. Kwon, B. Johansson, J. Kollár, L. Vitos, Surface properties of 3 d transition metals, Philos. Mag. 91 (2011) 3627-3640.

[3] H. L. Skriver, N. M. Rosengaard, Surface energy and work function of elemental metals, Phys. Rev. B 46 (1992) 7157.

[4] L. Vitos, A. V. Ruban, H. L. Skriver, J. Kollár, The surface energy of metals, Surf. Sci. 411 (1998) 186-202.

[5] W. R. Tyson, W. A. Miller, Surface free energies of solid metals: Estimation from liquid surface tension measurements, Surf. Sci. 62 (1977) 267-276.

[6] F. R. de Boer, R. Boom, W. C. M. Mattens, A. R. Miedema, A. K. Niessen, Cohesion in Metals (North-Holland, Amsterdam, 1988).

[7] M. S. Daw, M. I. Baskes, Embedded-atom method: Derivation and application to impurities, surfaces, and other defects in metals, Phys. Rev. B 29 (1984) 6443.

[8] D. Wolf, Correlation between energy, surface tension and structure of free surfaces in fcc metals, Surf. Sci. 226 (1990) 389-406.

[9] M. I. Baskes, Modified embedded-atom potentials for cubic materials and impurities, Phys. Rev. B 46 (1992) 2727.

[10] A. M. Rodriguez, G. Bozzolo, J. Ferrante, Multilayer relaxation and surface energies of fcc and bcc metals using equivalent crystal theory, Surf. Sci. 289 (1993) 100-126.

[11] J. Wan, Y. L. Fan, D. W. Gong, S. G. Shen, X. Q. Fan, Surface relaxation and stress of fcc metals: Cu, Ag, Au, Ni, Pd, Pt, Al and Pb, Model. Simul. Mater. Sci. Eng. 7 (1999) 189.

[12] J. M. Zhang, D. D. Wang, K. W. Xu, Calculation of the surface energy of bcc transition metals by using the second nearest-neighbor modified embedded atom method, Appl. Surf. Sci. 252 (2006) 8217-8222.

[13] C. L. Fu, S. Ohnishi, E. Wimmer, A. J. Freeman, Energetics of surface multilayer relaxation on W (001): evidence for short-range screening, Phys. Rev. Lett. 53 (1984) 675.

[14] T. Ning, Q. Yu, Y. Ye, Multilayer relaxation at the surface of fcc metals: Cu, Ag, Au, Ni, Pd, Pt, Al, Surf. Sci. 206 (1988) L857-L863.

[15] M. C. Payne, N. Roberts, R. J. Needs, M. Needels, J. D. Joannopoulos, Total energy and stress of metal and semiconductor surfaces, Surf. Sci. 211 (1989) 1-20.

[16] P. J. Feibelman, D. R. Hamann, LAPW calculations of Rh (001) surface relaxation, Surf. Sci. 234 (1990) 377-383.

[17] M. Methfessel, D. Hennig, M. Scheffler, Trends of the surface relaxations, surface energies, and work functions of the 4d transition metals, Phys. Rev. B 46 (1992) 4816.

[18] K. P. Bohnen, K. M. Ho, Structure and dynamics at metal surfaces, Surf. Sci. Rep. 19 (1993) 99-120.

[19] J. L. Da Silva, C. Stampfl, M. Scheffler, Converged properties of clean metal surfaces by all-electron first-principles calculations, Surf. Sci. 600 (2006) 703-715.

[20] N. E. Singh-Miller, N. Marzari, Surface energies, work functions, and surface relaxations of low-index metallic surfaces from first principles, Phys. Rev. B 80 (2009) 235407.

[21] M. P. J. Punkkinen, S. K. Kwon, J. Kollár, B. Johansson, L. Vitos, Compressive surface stress in magnetic transition metals, Phys. Rev. Lett. 106 (2011) 057202.

[22] K. Kádas, Z. Nabi, S. K. Kwon, L. Vitos, R. Ahuja, B. Johansson, J. Kollár, Surface relaxation and surface stress of 4d transition metals, Surf. Sci. 600 (2006) 395-402.

[23] V. Zólyomi, J. Kollár, L. Vitos, Anomalous surface relaxation in hcp transition metals, Phys. Rev. B 78 (2008) 195414.

[24] V. Zólyomi, J. Kollár, L. Vitos, On the surface relaxation of transition metals, Philos. Mag. 88 (2008) 2709-2714.

[25] V. Zólyomi, L. Vitos, S. K. Kwon, J. Kollár, Surface relaxation and stress for 5d transition metals, J. Phys.: Condens. Matter 21 (2009) 095007.

[26] R. Shuttleworth, The surface tension of solids, Proc. Phys. Soc. A 63 (1950) 444.

[27] J. Kollár, L. Vitos, J. M. Osorio-Guillén, R. Ahuja, Calculation of surface stress for fcc transition metals, Phys. Rev. B 68 (2003) 245417.

[28] T. -Y. Zhang, Z. -J. Wang, W. -K Chan, Eigenstress model for surface stress of solids, Phys. Rev. B 81 (2010) 195427.

[29] P. Hohenberg, W. Kohn, Inhomogeneous electron gas, Phys. Rev. 136 (1964) B864.

[30] W. Kohn, L. J. Sham, Self-consistent equations including exchange and correlation effects, Phys. Rev. 140 (1965) A1133.

[31] P. E. Blöchl, Projector augmented-wave method, Phys. Rev. B 50 (1994) 17953.

[32] G. Kresse, J. Hafner, Ab initio molecular dynamics for open-shell transition metals, Phys. Rev. B 48 (1993) 13115; G. Kresse, J. Hafner, Ab initio molecular dynamics for liquid metals, Phys. Rev. B 47 (1993) RC 558.

[33] G. Kresse, J. Furthmüller, Efficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set, Phys. Rev. B 54 (1996) 169.

[34] J. P. Perdew, J. A. Chevary, S. H. Vosko, K. A. Jackson, M. R. Pederson, D. J. Singh, C. Fiolhais, Atoms, molecules, solids, and surfaces: Applications of the generalized gradient approximation for exchange and correlation, Phys. Rev. B 46 (1992) 6671.

[35] J. P. Perdew, K. Burke, M. Ernzerhof, Generalized gradient approximation made simple, Phys. Rev. Lett. 77 (1996) 3865; J. P. Perdew, K. Burke, M. Ernzerhof, Errata: Generalized Gradient Approximation Made Simple [Phys. Rev. Lett. 77, 3865 (1996)], Phys. Rev. Lett. 78 (1997) 1396[149].

[36] L. Vitos, J. Kollár, H.L. Skriver, Full charge-density calculation of the surface energy of metals, Phys. Rev. B 49 (1994) 16694.

[37] L. Vitos, J. Kollár, H.L. Skriver, Ab initio full charge-density study of the atomic volume of $\alpha$-phase Fr, Ra, Ac, Th, Pa, U, Np, and Pu, Phys. Rev. B 55 (1997) 4947.

[38] L. Vitos, J. Kollár, H.L. Skriver, Full charge-density scheme with a kinetic-energy correction: Application to ground-state properties of the 4d metals, Phys. Rev. B 55 (1997) 13521.

[39] J. Kollár, L. Vitos, H. L. Skriver, Anomalous atomic volume of $\alpha$-Pu, Phys. Rev. B 55 (1997) 15353.

[40] R. Hafner, D. Spisák, R. Lorenz, J. Hafner, Magnetic ground state of Cr in density-functional theory, Phys. Rev. B 65 (2002) 184432.

[41] T. F. Liu, J. C. Tasy, Morphology of A12 $\alpha$-Mn structure, Scr. Metall. 21 (1987) 1213-1218.

[42] H. J. Monkhorst, J. D. Pack, Special points for Brillouin-zone integrations, Phys. Rev. B 13 (1976) 5188.

[43] J. Friedel, Philos. Mag. 43 (1952) 153; J. Friedel, Suppl. Nuovo Cim. 7 (1958), p. 287

[44] N. D. Lang, W. Kohn, Theory of metal surfaces: charge density and surface energy, Phys. Rev. B 1 (1970) 4555.

[45] J. -H. Cho, Ismail, Z. Zhang, E. W. Plummer, Oscillatory lattice relaxation at metal surfaces, Phys. Rev. B 59 (1999) 1677.

[46] M. Methfessel, D. Hennig, M. Scheffler, Calculated surface energies of the 4d transition metals: A study of bond-cutting models, Appl. Phys. A 55 (1992) 442-448.

[47] J. Friedel, The physics of clean metal surfaces, Ann. Phys. 1 (1976) 257.

[48] J. Kollár, L. Vitos, H. L. Skriver, Surface energy and work function of the light actinides, Phys. Rev. B 49 (1994) 11288.

[49] S. -H. Yoo, J. -H. Lee, Y. -K. Jung, A. Soon, Exploring stereographic surface energy maps of cubic metals via an effective pair-potential approach, Phys. Rev. B 93 (2016) 035434.

[50] K. Doll, N. M. Harrison, V. R. Saunders, A density functional study of lithium bulk and surfaces, J. Phys.: Condens. Matter 11 (1999) 5007.

[51] K. Kokko, P. T. Salo, R. Laihia, K. Mansikka, Work function and surface energy of optimized lithium slabs, Phys. Rev. B 52 (1995) 1536; K. Kokko, P. T. Salo, R. Laihia, K. Mansikka, First-principles calculations for work function and surface energy of thin lithium films, Surf. Sci. 348 (1996) 168-174.

[52] B. Fu, W. Liu, Z. Li, Surface energy calculation of alkali metals with the empirical electron surface model, Mater. Chem. Phys. 123 (2010) 658-665.

[53] T. Rodach, K. P. Bohnen, K. M. Ho, First-principles study of the Na (110) surface, Surf. Sci. 209 (1989) 481-491.

[54] M. Ropo, K. Kokko, L. Vitos, Assessing the Perdew-Burke-Ernzerhof exchange-correlation density functional revised for metallic bulk and surface systems, Phys. Rev. B, 77 (2008) 195445.

[55] E. Wachowicz, A. Kiejna, Multilayer relaxations at the (0001) surface of Be and Mg, Solid State Commun. 116 (2000) 17-20.; E. Wachowicz, A. Kiejna, Bulk and surface properties of hexagonal-close-packed Be and Mg, J. Phys.: Condens. Matter 13 (2001) 10767.

[56] P. J. Feibelman, First-principles calculation of the geometric and electronic structure of the Be (0001) surface, Phys. Rev. B 46 (1992) 2532.

[57] M. Lazzeri, S. de Gironcoli, Ab initio study of Be (0001) surface thermal expansion, Phys. Rev. Lett. 81 (1998) 2096.

[58] P. J. Feibelman, R. Stumpf, Physics of the Be (0001) surface core-level spectrum, Phys. Rev. B 50 (1994) 17480.

[59] R. Yu, P. K. Lam, First-principles total-energy study of hydrogen adsorption on Be (0001), Phys. Rev. B, 39 (1989) 5035.

[60] B. Q. Fu, W. Liu, Z. L. Li, Calculation of the surface energy of hcp-metals with the empirical electron theory, Appl. Surf. Sci. 255 (2009) 9348-9357.

[61] A. F. Wright, P. J. Feibelman, S. R. Atlas, First-principles calculation of the Mg (0001) surface relaxation, Surf. Sci. 302 (1994) 215-222.

[62] P. Staikov, T. S. Rahman, Multilayer relaxations and stresses on Mg surfaces, Phys. Rev. B 60 (1999) 15613.

[63] J. M. Zhang, D. D. Wang, K. W. Xu, Calculation of the surface energy of hcp metals by using the modified embedded atom method, Appl. Surf. Sci. 253 (2006) 2018-2024.

[64] I. Galanakis, N. Papanikolaou, P. H. Dederichs, Applicability of the broken-bond rule to the surface energy of the fcc metals, Surf. Sci. 511 (2002) 1-12.

[65] J. Schöchlin, K. P. Bohnen, K. M. Ho, Structure and dynamics at the Al (111)-surface, Surf. Sci. 324 (1995) 113-121.

[66] R. Stumpf, M. Scheffler, Ab initio calculations of energies and self-diffusion on flat and stepped surfaces of Al and their implications on crystal growth, Phys. Rev. B 53 (1996) 4958.

[67] P. J. Feibelman, Impurity calculations via a distorted-wave matrix Green's-function method, Phys. Rev. B 46 (1992) 15416.

[68] R. J. Needs, G. Rajagopal, First-principles calculations of the adsorbate-induced surface stress of KAl (111)-($\sqrt{3} \times \sqrt{3}$) R30°, Surf. Sci. 372 (1997) 179-184.

[69] R. J. Needs, Calculations of the surface stress tensor at aluminum (111) and (110) surfaces. Phys. Rev. Lett. 58 (1987) 53.

[70] R. J. Needs, M. J. Godfrey, M. Mansfield, Theory of surface stress and surface reconstruction, Surf. Sci. 242 (1991) 215-221.

[71] B. Fu, W. Liu, Z. Li, Calculation of the surface energy of fcc-metals with the empirical electron surface model, Appl. Surf. Sci. 256 (2010) 6899-6907.

[72] P. J. Feibelman, Calculation of surface stress in a linear combination of atomic orbitals

representation. Phys. Rev. B, 50 (1994) 1908.

[73] D. Yu, M. Scheffler, First-principles study of low-index surfaces of lead, Phys. Rev. B, 70 (2004) 155417.

[74] P. J. Feibelman, Ab initio step and kink formation energies on Pb (111), Phys. Rev. B 62 (2000) 17020.; P. J. Feibelman, Erratum: Ab initio step and kink formation energies on Pb(111) [Phys. Rev. B 62, 17020 (2000)], Phys. Rev. B, 65 (2002) 129902(E).

[75] M. Mansfield, R. J. Needs, Surface energy and stress of lead (111) and (110) surfaces, Phys. Rev. B 43 (1991) 8829.

[76] K. C. Mills, Y. C. Su, Review of surface tension data for metallic elements and alloys: Part 1–Pure metals, Int. Mater. Rev. 51 (2006) 329-351.; B. J. Keene, Review of data for the surface tension of pure metals, Int. Mater. Rev. 38 (1993) 157-192.

[77] S. Andersson, J. B. Pendry, P. M. Echenique, Low energy electron diffraction from Na (110) and Na2O (111) surfaces, Surf. Sci. 65 (1977) 539-551.

[78] H.L. Davis, J.B. Hannon, K.B. Ray, E.W. Plummer, Anomalous interplanar expansion at the (0001) surface of Be, Phys. Rev. Lett. 68 (1992) 2632.

[79] K. Pohl, J.H. Cho, K. Terakura, M. Scheffler, E.W. Plummer, Anomalously large thermal expansion at the (0001) surface of beryllium without observable interlayer anharmonicity, Phys. Rev. Lett. 80 (1998) 2853.

[80] P. T. Sprunger, K. Pohl, H. L. Davis, E. W. Plummer, Multilayer relaxation of the Mg (0001) surface, Surf. Sci.297 (1993) L48-L54.

[81] W. N. Unertl, H. V. Thapliyal, Surface parameters of clean Zn (0001) determined from averaged LEED data, J. Vac. Sci. Technol. 12 (1975) 263-267.

[82] J. R. Noonan, H. L. Davis, Confirmation of an exception to the "general rule"of surface relaxations, J. Vac. Sci. Technol. A 8 (1990) 2671-2676.

[83] F. Jona, D. Sondericker, P. M. Marcus, Al (111) revisited, J. Phys. C 13 (1980) L155.

[84] H. B. Nielsen, D. L. Adams, r-factor analysis of the effect of non-structural parameters in LEED, applied to Al (111), J. Phys. C 15 (1982) 615.

[85] C. Stampfl, M. Scheffler, H. Over, J. Burchhardt, M. Nielsen, D. L. Adams, W. Moritz, LEED structural analysis of Al (111)-K-($\sqrt{3} \times \sqrt{3}$) R30°: Identification of stable and metastable adsorption sites, Phys. Rev. B 49 (1994) 4959.

[86] J. Burchhardt, M. M. Nielsen, D. L. Adams, E. Lundgren, J. N. Andersen, Structure of Al (111)-($\sqrt{3} \times \sqrt{3}$) R30°-Na: A LEED study, Phys. Rev. B 50 (1994) 4718.

[87] Y. S. Li, F. Jona, P. M. Marcus, Multilayer relaxation of a Pb {111} surface, Phys. Rev. B, 43 (1991)

6337.

[88] C. Bombis, A. Emundts, M. Nowicki, and H. P. Bonzel, Absolute surface free energies of Pb, Surf. Sci. 511 (2002) 83-96.

[89] P. J. Feibelman, Relaxation of hcp (0001) surfaces: A chemical view, Phys. Rev. B 53 (1996) 13740.

[90] M. N. Huda, L. Kleinman, Density functional calculations of the influence of hydrogen adsorption on the surface relaxation of Ti (0001), Phys. Rev. B, 71 (2005) 241406.

[91] J. H. Cho, K. Terakura, Plane-wave-basis pseudopotential calculations of the surface relaxations of Ti (0001) and Zr (0001), Phys. Rev. B 56 (1997) 9282.

[92] C. L. Fu, S. Ohnishi, H. J. F. Jansen, A. J. Freeman, All-electron local-density determination of the surface energy of transition metals: W (001) and V (001), Phys. Rev. B, 31 (1985) R1168.

[93] J. C. Boettger, Nonconvergence of surface energies obtained from thin-film calculations, Phys. Rev. B 49 (1994) 16798.

[94] B. Q. Fu, W. Liu, Z. L. Li, Calculation of the surface energy of bcc-metals with the empirical electron theory. Appl. Surf. Sci. 255 (2009) 8511-8519.

[95] J. M. Zhang, D. D. Wang, K. W. Xu, Calculation of the surface energy of bcc transition metals by using the second nearest-neighbor modified embedded atom method. Appl. Surf. Sci. 252 (2006) 8217-8222.

[96] M. Aldén, H. L. Skriver, S. Mirbt, B. Johansson, Calculated surface-energy anomaly in the 3d metals, Phys. Rev. Lett. 69 (1992) 2296; M. Aldén, H. L. Skriver, S. Mirbt, B. Johansson, Surface energy and magnetism of the 3d metals, Surf. Sci. 315 (1994) 157-172.

[97] M. J. S. Spencer, A. Hung, I. K. Snook, I. Yarovsky, Density functional theory study of the relaxation and energy of iron surfaces., Surf. Sci. 513 (2002) 389-398.

[98] P. Błoński, A. Kiejna, Calculation of surface properties of bcc iron, Vacuum 74 (2004) 179-183.

[99] P. Błoński, A. Kiejna, J. Hafner, Theoretical study of oxygen adsorption at the Fe (110) and (100) surfaces, Surf. Sci. 590 (2005) 88-100.

[100] P. Błoński, A. Kiejna, Structural, electronic, and magnetic properties of bcc iron surfaces, Surf. Sci. 601 (2007) 123-133.

[101] T. Kishi, S. Itoh, Surface relaxation of Fe (001) by ab initio molecular dynamics, Surf. Sci. 358 (1996) 186-189.

[102] A. Hung, I. Yarovsky, J. Muscat, S. Russo, I. Snook, R.O. Watts, First-principles study of metallic iron interfaces, Surf. Sci. 501 (2002) 261-269.

[103] S. Schönecker, S. K. Kwon, B. Johansson, L. Vitos, Surface parameters of ferritic iron-rich Fe-Cr alloy, J. Phys.: Condens. Matter 25 (2013) 305002.

[104] S. Schönecker, X. Li, B. Johansson, S. K. Kwon, L. Vitos, Thermal surface free energy and stress


of iron, Sci. Rep. 5 (2015) 14860.

[105] A. Arya, E. A. Carter, Structure, bonding, and adhesion at the TiC (100)/Fe (110) interface from first principles, J. Chem. Phys. 118 (2003) 8982.

[106] D. E. Jiang, E. A. Carter, Adsorption and diffusion energetics of hydrogen atoms on Fe (110) from first principles, Surf. Sci. 547 (2003) 85-98.

[107] A. Stibor, G. Kresse, A. Eichler, J. Hafner, Density functional study of the adsorption of CO on Fe (110), Surf. Sci. 507 (2002) 99-102.

[108] T. Ossowski, A. Kiejna, Oxygen adsorption on Fe (110) surface revisited, Surf. Sci. 637 (2015) 35-41.

[109] M. Blanco-Rey, S. J. Jenkins, Surface stress in d-band metal surfaces, J. Phys.: Condens. Matter 22 (2010) 135007.

[110] F. Mittendorfer, A. Eichler, J. Hafner, Structural, electronic and magnetic properties of nickel surfaces, Surf. Sci. 423 (1999) 1-11.

[111] G. Kresse, J. Hafner, First-principles study of the adsorption of atomic H on Ni (111),(100) and (110), Surf. Sci. 459 (2000) 287-302.

[112] J. S. Luo, B. Legrand, Multilayer relaxation at surfaces of body-centered-cubic transition metals, Phys. Rev. B 38 (1988) 1728.; B. Legrand, M. Guillopé, J. S. Luo, G. Tréglia, Multilayer relaxation and reconstruction in bcc and fcc transition and noble metals, Vacuum 41 (1990) 311-314.

[113] G. Allan, J. Lopez, Influence of chemisorbed oxygen on nickel surface vibrations, Surf. Sci. 95 (1980) 214-226.

[114] W. B. Zhang, C. Chen, S. Y. Zhang, Equilibrium crystal shape of Ni from first principles, J. Phys. Chem. C 117 (2013) 21274-21280.

[115] M. J. Harrison, D. P. Woodruff, J. Robinson, Surface alloys, surface rumpling and surface stress, Surf. Sci. 572 (2004) 309-317.

[116] V. Ledentu, W. Dong, P. Sautet, Heterogeneous catalysis through subsurface sites, J. Am. Chem. Soc. 122 (2000) 1796-1801.

[117] T. Rodach, K. P. Bohnen, K. M. Ho, First principles calculations of lattice relaxation at low index surfaces of Cu, Surf. Sci. 286 (1993) 66-72.

[118] J. C. Cheng, H. Q. Wang, A. T. S. Wee, H. A. Huan, Relaxation of Cu (100),(110) and (111) surfaces using ab initio pseudopotentials, Surf. Rev. Lett. 8 (2001) 541-547.

[119] J. L. Da Silva, K. Schroeder, S. Blügel, First-principles investigation of the multilayer relaxation of stepped Cu surfaces, Phys. Rev. B 69 (2004) 245411.

[120] H. Bross, M. Kauzmann, Electronic structure, surface states, surface energy, and work function of the Cu (100) surface, Phys. Rev. B 51 (1995) 17135.

[121] H. M. Polatoglou, M. Methfessel, M. Scheffler, Vacancy-formation energies at the (111) surface and in bulk Al, Cu, Ag, and Rh, Phys. Rev. B 48 (1993) 1877.

[122] S. Tougaard, A. Ignatiev, Atomic structure of the scandium (0001) surface, Surf. Sci. 115 (1982) 270-278.

[123] S. D. Barrett, S. S. Dhesi, M. P. Evans, R. G. White, Determination of the surface relaxation of Sc (0001) by video LEED analysis, Meas. Sci. Technol. 4 (1993) 114.

[124] S. S. Dhesi, R. G. White, A. J. Patchett, M. P. Evans, M. H. Lee, R. I. R. Blyth, F. M. Leibsle, S. D. Barrett, Surface-structure determination of Sc (0001) using LEED and STM, Phys. Rev. B 51 (1995) 17946.

[125] G. Teeter, J. L. Erskine, Surface relaxation of Ti (0001): Influence of hydrogen contamination, Phys. Rev. B 61 (2000) 13929.

[126] H. D. Shih, F. Jona, D. W. Jepsen, P. M. Marcus, The structure of the clean Ti (0001) surface, J. Phys. C 9 (1976) 1405.

[127] V. Jensen, J. N. Andersen, H. B. Nielsen, D. L. Adams, The surface structure of V (100), Surf. Sci. 116 (1982) 66-84.

[128] D. L. Adams, H. B. Nielsen, The preparation and surface structure of clean V (110), Surf. Sci. 107 (1981) 305-320.

[129] S. Ekelund, C. Leygraf, A LEED-AES study of the oxidation of Cr (110) and Cr (100), Surf. Sci. 40 (1973) 179-199.

[130] H. Li, Y. S. Li, J. Quinn, D. Tian, J. Sokolov, F. Jona, P. M. Marcus, Quantitative low-energy electron-diffraction study of the epitaxy of Fe on Ag {001}: questions about the growth mode, Phys. Rev. B 42 (1990) 9195.

[131] K.O. Legg, F. Jona, D.W. Jepsen, P.M. Marcus, Low-energy electron diffraction analysis of clean Fe (001), J. Phys. C 10 (1977) 937.

[132] X. Tan, J. Zhou, Y. Peng, First-principles study of oxygen adsorption on Fe (110) surface, Appl. Surf. Sci. 258 (2012) 8484-8491.

[133] C. Xu, D. J. O'Connor, Surface relaxation trend study with iron surfaces, Nucl. Instrum. Methods Phys. Res. B 53 (1991) 315-325.

[134] H. D. Shih, F. Jona, U. Bardi, P. M. Marcus, The atomic structure of Fe (110), J. Phys. C 13 (1980) 3801.

[135] J. E. Prieto, C. Rath, S. Müller, R. Miranda, K. Heinz, A structural analysis of the Co (0001) surface and the early stages of the epitaxial growth of Cu on it, Surf. Sci. 401 (1998) 248-260.

[136] J. Lahtinen, J. Vaari, T. Vaara, K. Kauraala, P. Kaukasoina, M. Lindroos, LEED investigations on Co (0001): the clean surface and the (2×2)-K overlayer, Surf. Sci. 425 (1999) 90-100.


[137] J. E. Demuth, T. N. Rhodin, Elastic leed intensity-energy studies of clean (001),(110) and (111) nickel surfaces, Surf. Sci. 42 (1974) 261-298.; J. E. Demuth, D. W. Jepsen, P. M. Marcus, Analysis of low-energy-electron-diffraction intensity spectra for (001),(110), and (111) nickel, Phys. Rev. B 11 (1975) 1460.

[138] J. W. Frenken, R. G. Smeenk, J. F. Van der Veen, Static and dynamic displacements of nickel atoms in clean and oxygen covered Ni (001) surfaces, Surf. Sci. 135 (1983) 147-163.

[139] H. C. Lu, E. P. Gusev, E. Garfunkel, T. Gustafsson, A MEIS study of thermal effects on the Ni (111) surface, Surf. Sci. 352 (1996) 21-24.

[140] D. M. Lind, F. B. Dunning, G. K. Walters, H. L. Davis, Surface-structural analysis by use of spin-polarized low-energy electron diffraction: An investigation of the Cu (100) surface, Phys. Rev. B 35 (1987) 9037.

[141] H. L. Davis, J. R. Noonan, Multilayer relaxation in metallic surfaces as demonstrated by LEED analysis, Surf. Sci. 126 (1983) 245-252.

[142] R. Mayer, C. Zhang, K. G. Lynn, W. E. Frieze, F. Jona, P. M. Marcus, Low-energy electron and positron diffraction measurements and analysis on Cu (100), Phys. Rev. B 35 (1987) 3102.

[143] H. L. Davis, J. R. Noonan, Cu (100) multilayer relaxation, J. Vac. Sci. Technol. 20 (1982) 842-845.

[144] J. R. Noonan, H. L. Davis, LEED analysis of I-V spectra from Cu (100) at 100K, Bull. Am. Phys. Soc. 27 (1982) 237.

[145] S. Å. Lindgren, L. Walldén, J. Rundgren, P. Westrin, Low-energy electron diffraction from Cu (111): Subthreshold effect and energy-dependent inner potential; surface relaxation and metric distances between spectra, Phys. Rev. B 29 (1984) 576.

[146] S. P. Tear, K. Roll, M. Prutton, A comparison of reliability (R) factors in a LEED structural analysis of the copper (111) surface, J. Phys. C 14 (1981) 3297.

[147] I. Bartos, A. Barbievi, M. A. Van Hove, W. F. Chung, Q. Cai, M. S. Altman, Cu (111) surface relaxation by VLEED, Sur. Rev. Lett. 2 (1995) 477-482.

[148] H. J. Wasserman, J. S. Vermaak, On the determination of the surface stress of copper and platinum, Surf. Sci. 32 (1972) 168-174.

[149] M. Yamamoto, C.T. Chan, K.M. Ho, First-principles calculations of the surface relaxation and electronic structure of Zr(0001), Phys. Rev. B 50 (1994) 7932.

[150] M. Weinert, R. E. Watson, J. W. Davenport, G. W. Fernando, Adsorbed layer and multilayer materials: The energetics and bonding of Pd and Ag on Nb (001) and Nb (110), Phys. Rev. B, 39 (1989) 12585.

[151] J. G. Che, C. T. Chan, W. E. Jian, T. C. Leung, Surface atomic structures, surface energies, and equilibrium crystal shape of molybdenum, Phys. Rev. B 57 (1998) 1875.

[152] M. Y. Chou, J. R. Chelikowsky, Structural properties of the Ru (0001) surface, Phys. Rev. B 35 (1987) 2124.

[153] P. J. Feibelman, J. E. Houston, H. L. Davis, D. G. O'Neill, Relaxation of the clean Cu-and H-covered Ru (0001) surface, Surf. Sci. 302 (1994) 81-92.

[154] V. Fiorentini, M. Methfessel, M. Scheffler, Reconstruction mechanism of fcc transition metal (001) surfaces. Phys. Rev. Lett. 71 (1993) 1051.; H. Ibach, The role of surface stress in reconstruction, epitaxial growth and stabilization of mesoscopic structures, Surf. Sci. Rep. 29 (1997) 195-263.; H. Ibach, Erratum to:"The role of surface stress in reconstruction, epitaxial growth and stabilization of mesoscopic structures" [Surf. Sci. Rep. 29 (1997) 193], Surf. Sci. Rep. 35 (1999) 71-73.

[155] A. Filippetti, V. Fiorentini, K. Stokbro, R. Valente, S. Baroni, Formation Energy, Stress, and Relaxations of Low-Index Rhodium Surfaces, MRS Proceedings, 408. doi:10.1557/PROC-408-457.

[156] A. Eichler, J. Hafner, G. Kresse and J. Furthmüller, Relaxation and electronic surface states of rhodium surfaces, Surf. Sci. 352 (1996) 689-692.

[157] J. -M. Zhang, Y. Shu, and K. -W. Xu, Multilayer relaxation of fcc metals (001) surface: A modified embedded atom method study, Solid State Commun. 137 (2006) 441-445.

[158] I. Morrison, D. M. Bylander, L. Kleinman, Ferromagnetism of the Rh (001) surface, Phys. Rev. Lett. 71 (1993) 1083.

[159] J. -M. Zhang, F. Ma, and K. -W. Xu, Calculation of the surface energy of FCC metals with modified embedded-atom method, Appl. Surf. Sci. 229 (2004) 34-42.

[160] A. Wachter, K. P. Bohnen and K. M. Ho, Structure and dynamics at the Pd (100) surface, Surf. Sci. 346 (1996) 127-135.

[161] M. Todorova, K. Reuter and M. Scheffler, Oxygen overlayers on Pd (111) studied by density functional theory, J. Phys. Chem. B 108 (2004) 14477-14483.

[162] W. Dong, G. Kresse, J. Furthmüller and J. Hafner, Chemisorption of H on Pd (111): An ab initio approach with ultrasoft pseudopotentials. Phys. Rev. B 54 (1996) 2157.

[163] P. J. Feibelman, Anisotropy of the stress on fcc (110) surfaces. Phys. Rev. B 51 (1995) 17867.

[164] G. Boisvert, L. J. Lewis, M. J. Puska, R. M. Nieminen, Energetics of diffusion on the (100) and (111) surfaces of Ag, Au, and Ir from first principles, Phys. Rev. B 52 (1995) 9078.

[165] H. Erschbaumer, A. J. Freeman, C. L. Fu and R. Podloucky, Surface states, electronic structure and surface energy of the Ag (001) surface, Surf. Sci. 243 (1991) 317-322.

[166] W. T. Moore, P. R. Watson, D. C. Frost, K. A. R. Mitchell, An investigation of the structure of the (0001) surface of zirconium. J. Phys. C 12 (1979) L887.

[167] L. M. de la Garza, L. J. Clarke, The surface structure of Mo (110) determined by LEED, J. Phys. C 14 (1981) 5391.

[168] L. J. Clarke, LEED analysis of the surface structure of Mo (001), Surf. Sci. 91 (1980) 131-152.

[169] W. Nichtl, N. Bickel, L. Hammer, K. Heinz, K. Müller, Surface relaxation change by hydrogen adsorption on Rh (110), Surf. Sci. Lett. 188 (1987) L729-L734.

[170] W. Oed, B. Dötsch, L. Hammer, K. Heinz and K. Müller, A LEED investigation of clean and oxygen covered Rh (100), Surf. Sci. 207 (1988) 55-65.

[171] K. C. Prince, B. Ressel, C. Astaldi, M. Peloi, R. Rosei, M. Polcik, C. Crotti, M. Zacchigna, C. Comicioli, C. Ottaviani, C. Quaresima, P. Perfetti, Surface core level shift photoelectron diffraction of Rh (100), Surf. Sci. 377 (1997) 117-120.

[172] F. R. Shepherd, P. R. Watson, D. C. Frost, K. A. R. Mitchell, An investigation of the structure of the (111) surface of rhodium by LEED, J. Phys. C 11 (1978) 4591.

[173] S. Hengrasmee, K. A. R. Mitchell, P. R. Watson, S. J. White, Some observations on the use of reliability indices in LEED crystallography, Can. J. Phys. 58 (1980) 200-206.

[174] A. Wander, C. J. Barnes, L. D. Mapledoram, D. A. King, Structural transitions in ultra-thin nickel films on Rh {111}, Surf. Sci. 281 (1993) 42-50.

[175] J. Quinn, Y. S. Li, D. Tian, H. Li, F. Jona, P. M. Marcus, Anomalous multilayer relaxation of Pd {001}, Phys. Rev. B, 42 (1990) 11348.

[176] R. J. Behm, K. Christmann, G. Ertl, M. A. Van Hove, Adsorption of CO on Pd (100). J. Chem. Phys., 73 (1980) 2984-2995.

[177] H. Ohtani, M. A. Van Hove, G. A. Somorjai, Leed intensity analysis of the surface structures of Pd (111) and of CO adsorbed on Pd (111) in a $(\sqrt{3} \times \sqrt{3})$ R30° arrangement, Surf. Sci. 187 (1987) 372.

[178] M. E. Grillo, C. Stampfl, W. Berndt, Low-energy electron-diffraction analysis of the $(\sqrt{7} \times \sqrt{7})$ R19. 1-S adsorbate structure on the Pd (111) surface, Surf. Sci. 317 (1994) 84.

[179] Y. Kuk, L. C. Feldman, P. J. Silverman, Transition from the pseudomorphic state to the nonregistered state in epitaxial growth of Au on Pd (111), Phys. Rev. Lett. 50 (1983) 511.

[180] R. Lamber, S. Wetjen, N. I. Jaeger, Size dependence of the lattice parameter of small palladium particles, Phys. Rev. B, 51 (1995) 10968.

[181] H. Li, J. Quinn, Y. S. Li, D. Tian, F. Jona, P. M. Marcus, Multilayer relaxation of clean Ag {001}, Phys. Rev. B, 43 (1991) 7305.

[182] E. A. Soares, E. A., V. B. Nascimento, V. E. De Carvalho, C. M. C. De Castilho, A. V. De Carvalho, R. Toomes and D. P. Woodruff, Structure determination of Ag (111) by low-energy electron diffraction, Surf. Sci. 419 (1999) 89.

[183] P. Statiris, H. C. Lu, T. Gustafsson, Temperature dependent sign reversal of the surface contraction of Ag (111), Phys. Rev. Lett. 72 (1994) 3574.

[184] R. J. Culbertson, L. C. Feldman, P. J. Silverman, H. Boehm, Epitaxy of Au on Ag (111) studied by high-energy ion scattering, Phys. Rev. Lett. 47 (1981) 657.

[185] F. Soria, J. L. Sacedon, P. M. Echenique, D. Titterington, LEED study of the epitaxial growth of the thin film Au (111)/Ag (111) system, Surf. Sci. 68 (1977) 448-456.

[186] P. Statiris, H. C. Lu, T. Gustafsson, Temperature dependent sign reversal of the surface contraction of Ag (111), Phys. Rev. Lett. 72 (1994) 3574.

[187] H. J. Wasserman, J. S. Vermaak, On the determination of a lattice contraction in very small silver particles, Surf. Sci. 22 (1970) 164-172.

[188] A. Kiejna, Surface atomic structure and energetics of tantalum, Surf. Sci. 598 (2005) 276-284.

[189] I. G. Batirev, W. Hergert, P. Rennert, V. S. Stepanyuk, T. Oguchi, A. A. Katsnelson, J. A., Leiroe, K. H. Lee, Surface atomic forces and multilayer relaxation of W (001), W (110) and Fe/W (110), Surf. Sci. 417 (1998) 151-158.

[190] M. Arnold, G. Hupfauer, P. Bayer, L. Hammer, K. Heinz, B. Kohler, M. Scheffler, Surf. Sci. 382 (1997) 288-289.

[191] X. Qian, W. Hübner, First-principles calculation of structural and magnetic properties for Fe monolayers and bilayers on W (110), Phys. Rev. B 60 (1999) 16192.

[192] W. Xu, J. B. Adams, Structure of seven W surfaces, Surf. Sci. 319 (1994) 45-57.

[193] A. Filippetti, V. Fiorentini, Reconstructions of Ir (110) and (100): an ab initio study, Surf. Sci. 377 (1997) 112-116.

[194] Q. Ge, D. A. King, N. Marzari, M. C. Payne, First principles calculation of the energy and structure of two solid surface phases on Ir {100}, Surf. Sci. 418 (1998) 529-535.

[195] R. J. Needs, M. Mansfield, Calculations of the surface stress tensor and surface energy of the (111) surfaces of iridium, platinum and gold, J. Phys.: Condens. Matter 1 (1989) 7555.

[196] S. Baud, C. Ramseyer, G. Bihlmayer, S. Blügel, C. Barreteau, M. C. Desjonquères, D. Spanjaard, N. Bernstein, Comparative study of ab initio and tight-binding electronic structure calculations applied to platinum surfaces, Phys. Rev. B 70 (2004) 235423.

[197] S. Moré, A. P. Seitsonen, W. Berndt, A. M. Bradshaw, Ordered phases of Na adsorbed on Pt (111): Experiment and theory, Phys. Rev. B 63 (2001) 075406.

[198] A. Kokalj and M. Causà, Periodic density functional theory study of Pt (111): surface features of slabs of different thicknesses, J. Phys.: Condens. Matter 11 (1999) 7463.

[199] P. J. Feibelman, Energetics of steps on Pt (111), Phys. Rev. B 52 (1995) 16845.

[200] P. J. Feibelman, First-principles calculations of stress induced by gas adsorption on Pt (111), Phys. Rev. B 56 (1997) 2175.

[201] S. Olivier, G. Tréglia, A. Saúl, F. Willaime, Influence of surface stress in the missing row

reconstruction of fcc transition metals, Surf. Sci. 600 (2006) 5131-5135.

[202] B. D. Yu, M. Scheffler, Physical origin of exchange diffusion on fcc (100) metal surfaces, Phys. Rev. B 56 (1997) R15569.

[203] N. Takeuchi, C. T. Chan, K. M. Ho, Au (111): A theoretical study of the surface reconstruction and the surface electronic structure, Phys. Rev. B 43 (1991) 13899.

[204] A. Titov, W. Moritz, Structure of the clean Ta (100) surface, Surf. Sci. Lett. 123 (1982) L709-L716.

[205] M. A. Van Hove, S. Y. Tong, Surface structures of W (110) and W (100) faces by the dynamical LEED approach, Surf. Sci. 54 (1976) 91-100.

[206] M. K. Debe, D. A. King, F. S. Marsh, Further dynamical and experimental LEED results for a clean W{001}-(1×1) surface structure determination, Surf. Sci. 68 (1977) 437-447.

[207] B. W. Lee, A. Ignatiev, S. Y. Tong, M. Van Hove, Surface contraction of the clean W (001) face, J. Vac. Sci. Technol. 14 (1977) 291-293.

[208] L. C. Feldman, R. L. Kauffman, P. J. Silverman, R. A. Zuhr, J. H. Barrett, Surface scattering from W single crystals by MeV He⁺ ions, Phys. Rev. Lett. 39 (1977) 38.

[209] J. Kirschner, R. Feder, Surface structure determination by leed rotation diagrams; Application to the surface relaxation of W (001), Surf. Sci. 79 (1979) 176-188.

[210] L. J. Clarke, L. M. De La Garza, Surface structure of unreconstructed W (001) from alternative leed techniques, Surf. Sci. 99 (1980) 419-439.

[211] R. Feder, J. Kirschner, Spin-polarized low-energy electron diffraction: Theory, experiment and analysis of results from W (001)(1×1). Surf. Sci. 103 (1981) 75-102.

[212] G. Schmidt, H. Zagel, H. Landskron, K. Heinz, K. Müller, J. B. Pendry, The clean and H-induced reconstruction of W (100) studied by LEED at slanting primary bean incidence, Surf. Sci. 271 (1992) 416-426.

[213] J. E. Cordwell, D. Hull, The brittle fracture of [100] axis tungsten single crystals. Philos. Mag. 19 (1969) 951-966.

[214] M. G. Lagally, J. C. Buchholz, G. -C. Wang, LEED intensity-averaging experiments for surface-layer structure determination, J. Vac. Sci. Technol. 12 (1975) 213-221.

[215] R. J. Smith, C. Hennessy, M. W. Kim, C. N. Whang, M. Worthington, M. Xu, High-energy ion-scattering studies of anisotropic surface-atom vibrations on W (110), Phys. Rev. Lett. 58 (1987) 702.

[216] B. Kim, J. Chen, J. L. Erskine, W. N. Mei, C. M. Wei, Surface and bulk photoelectron diffraction from W (110) 4f core levels, Phys. Rev. B 48 (1993) 4735.

[217] M. Arnold, G. Hupfauer, P. Bayer, L. Hammer, K. Heinz, B. Kohler, M. Scheffler, Hydrogen on W (110): an adsorption structure revisited, Surf. Sci. 382 (1997) 288-289.

[218] G. Teeter, J. L. Erskine, F. Shi, M. A. Van Hove, Surface roughness and LEED crystallography:

Analysis of flat and vicinal W (110), Phys. Rev. B 60 (1999) 1975.

[219] D. Venus, S. Cool, M. Pilhal, Quantitative structural determination using spin-polarized low-energy electron diffraction rotation curves: W (110), Surf. Sci. 446 (2000) 199-210.

[220] H. L. Meyerheim, D. Sander, R. Popescu, P. Steadman, S. Ferrer, J. Kirschner, Interlayer relaxation of W (110) studied by surface x-ray diffraction, Surf. Sci. 475 (2001) 103-108.

[221] G. Besold, K. Heinz, E. Lang, K. Müller, Structure analysis of Ir (100) 1×1 by LEED (100-500 eV), J. Vac. Sci. Technol. A 1 (1983) 1473-1476.

[222] J. A. Davies, T. E. Jackman, D. P. Jackson, P. R. Norton, Surface relaxation of the platinum (100)-(1×1) surface at 175 k, Surf. Sci. 109 (1981) 20-28.

[223] D. L. Adams, H. B. Nielsen, M. A. Van Hove, Quantitative analysis of low-energy-electron diffraction: Application to Pt (111), Phys. Rev. B 20 (1979) 4789.

[224] R. Feder, H. Pleyer, P. Bauer, N. Müller, Spin polarization in low-energy electron diffraction: Surface analysis of Pt (111), Surf. Sci. 109 (1981) 419-434.

[225] J. F. Van der Veen, R. G. Smeenk, R. M. Tromp, F. W. Saris, Relaxation effects and thermal vibrations in a Pt (111) surface measured by medium energy ion scattering, Surf. Sci. 79 (1979) 219-230.

[226] B. M. Ocko, D. Gibbs, K. G. Huang, D. M. Zehner, S. G. J. Mochrie, Structure and phases of the Au (001) surface: Absolute x-ray reflectivity, Phys. Rev. B 44 (1991) 6429.

[227] C. W. Mays, J. S. Vermaak, D. Kuhlmann-Wilsdorf, On surface stress and surface tension: II. Determination of the surface stress of gold, Surf. Sci. 12 (1968) 134-140.

Table 1. Calculated surface relaxation ($d_{ij}$), surface energy ($\gamma$), and surface stress ($\tau$) of simple metals.
$d_{ij}$ is given in percentage, $\gamma$ and $\tau$ are in units of J/m². The calculated lattice constants $a$ are listed
with the structure information, in Å. Previously reported data are also tabulated, with their
annotation numbers starting as $T$ and $E$, for theoretical and experimental cases, respectively.

<table>
<thead>
<tr>
<th>Metal</th>
<th>Structure</br>$a$ ($c/a$)</th>
<th>Surface</th>
<th colspan="3">Relaxation</th>
<th>$\boldsymbol{\gamma}$</th>
<th>$\boldsymbol{\tau}$</th>
<th>$\boldsymbol{\tau-\gamma}$</th>
</tr>
<tr>
<th></th>
<th></th>
<th></th>
<th>$d_{12}$</th>
<th>$d_{23}$</th>
<th>$d_{34}$</th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Li</td>
<td>bcc</br>3.44</td>
<td>(110)</td>
<td>-4.33</td>
<td>-0.23</td>
<td>0.61</td>
<td>0.49</br>0.56<sup>T1</sup>, 0.53<sup>T2</sup></br>0.50<sup>T3</sup>, 0.54<sup>T4</sup>,</br>0.46<sup>T5</sup>, 0.46<sup>T6</sup></br>0.52<sup>E1</sup>, 0.53<sup>E2</sup></br>0.47<sup>E3</sup></td>
<td>-0.13</td>
<td>-0.62</td>
</tr>
<tr>
<td>Na</td>
<td>bcc</br>4.19</td>
<td>(110)</td>
<td>-0.98</br>-1.6±0.5<sup>T7</sup></br>-0.33±0.33<sup>E4</sup></td>
<td>0.38</br>0.0±0.5<sup>T7</sup></td>
<td>0.01</br>0.6±0.8<sup>T7</sup></td>
<td>0.21</br>0.25<sup>T1</sup>, 0.22<sup>T2</sup></br>0.31<sup>T5</sup>, 0.24<sup>T6</sup></br>0.25<sup>T7</sup>, 0.26<sup>E1</sup></br>0.26<sup>E2</sup>, 0.23<sup>E3</sup></td>
<td>0.12</td>
<td>-0.09</td>
</tr>
<tr>
<td>K</td>
<td>bcc</br>5.28</td>
<td>(110)</td>
<td>-0.01</td>
<td>0.01</td>
<td>0.00</td>
<td>0.11</br>0.14<sup>T1</sup>, 0.11<sup>T2</sup></br>0.12<sup>T5</sup>, 0.13<sup>T6</sup></br>0.15<sup>E1</sup>,0.13<sup>E2</sup></br>0.14<sup>E3</sup></td>
<td>-0.29</td>
<td>-0.40</td>
</tr>
<tr>
<td>Rb</td>
<td>bcc</br>5.67</td>
<td>(110)</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.08</br>0.10<sup>T1</sup>, 0.10<sup>T2</sup></br>0.09<sup>T5</sup>, 0.11<sup>T6</sup></br>0.09<sup>T8a</sup>, 0.12<sup>T8b</sup></br>0.12<sup>E1</sup>, 0.11<sup>E2</sup></br>0.11<sup>E3</sup></td>
<td>0.03</td>
<td>-0.05</td>
</tr>
<tr>
<td>Cs</td>
<td>bcc</br>6.15</td>
<td>(110)</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.06</br>0.08<sup>T1</sup>, 0.06<sup>T2</sup></br>0.07<sup>T5</sup>, 0.08<sup>T6</sup></br>0.10<sup>E1</sup>, 0.10<sup>E2</sup></br>0.08<sup>E3</sup></td>
<td>0.04</td>
<td>-0.02</td>
</tr>
<tr>
<td>Be</td>
<td>hcp</br>2.26 (1.58)</td>
<td>(0001)</td>
<td>2.78</br>3.17<sup>T9a</sup></br>2.74<sup>T9b</sup></br>3.9<sup>T10</sup></br>3.2<sup>T11</sup></br>2.6<sup>T12</sup></br>5.8<sup>E5</sup></br>3.1±0.7<sup>E6</sup></td>
<td>0.84</br>1.15<sup>T9a</sup></br>1.18<sup>T9b</sup></br>2.2<sup>T10</sup></br>1.0<sup>T11</sup></br>0.8<sup>T12</sup></br>-0.2<sup>E5</sup></br>1.4±0.7<sup>E6</sup></td>
<td>0.47</br>0.65<sup>T9a</sup></br>0.77<sup>T9b</sup></br>0.4<sup>T11</sup></br>0.2<sup>E5</sup></br>0.9±0.9<sup>E6</sup></td>
<td>1.77</br>1.83<sup>T1</sup>, 2.12<sup>T5</sup></br>1.67<sup>T9a</sup>, 2.01<sup>T9b</sup></br>1.92<sup>T10</sup>, 2.1<sup>T13</sup></br>1.53<sup>T14</sup>, 1.63<sup>E1</sup></br>2.70<sup>E2</sup></td>
<td>2.99</td>
<td>1.22</td>
</tr>
<tr>
<td>Mg</td>
<td>hcp</br>3.19 (1.62)</td>
<td>(0001)</td>
<td>1.45</br>2.04<sup>T9a</sup></br>1.13<sup>T9b</sup></br>1.24<sup>T15a</sup></br>1.18<sup>T15b</sup></br>1.5±0.1<sup>T16</sup></br>1.8<sup>T17</sup></td>
<td>0.26</br>1.13<sup>T9a</sup></br>0.31<sup>T9b</sup></br>0.2l<sup>T15a</sup></br>0.36<sup>T15b</sup></br>0.5±0.1<sup>T16</sup></br>0.2<sup>T17</sup></td>
<td>-0.35</br>0.72<sup>T9a</sup></br>0.21<sup>T9b</sup></br>-0.72<sup>T15a</sup></br>-0.73<sup>T15b</sup></br>0.1±0.1<sup>T16</sup></br>-0.3<sup>T17</sup></td>
<td>0.55</br>0.79<sup>T1</sup>, 0.64<sup>T5</sup>,</br>0.30<sup>T9a</sup>, 0.35<sup>T9b</sup></br>0.56<sup>T15a</sup>, 0.62<sup>T15b</sup></br>0.64<sup>T14</sup>, 0.89<sup>T18</sup></br>0.29<sup>T14</sup>, 0.79<sup>E1</sup></br>0.76<sup>E2</sup>, 0.82<sup>E3</sup></td>
<td>0.88</td>
<td>0.33</td>
</tr>
</tbody>
</table>

<table>
<tbody>
<tr>
<td>Ca</td>
<td>fcc<br>5.52</td>
<td>(111)</td>
<td>1.9±0.3E7<br>-1.82</td>
<td>0.8±0.4E7<br>0.57</td>
<td>-0.4±0.5E7<br>0.24</td>
<td>0.41<br>0.57T1, 0.51T2<br>0.35T5, 0.50T19<br>0.50E1, 0.49E2<br>0.48E3</td>
<td>-0.85</td>
<td>-1.25</td>
</tr>
<tr>
<td>Sr</td>
<td>fcc<br>6.02</td>
<td>(111)</td>
<td>-1.84</td>
<td>0.70</td>
<td>0.10</td>
<td>0.35<br>0.43T1, 0.40T2<br>0.44T8a, 0.55T8b<br>0.29T5, 0.37T19<br>0.42E1, 0.41E2<br>0.38E3</td>
<td>-0.48</td>
<td>-0.83</td>
</tr>
<tr>
<td>Ba</td>
<td>bcc<br>5.03</td>
<td>(110)</td>
<td>-2.04</td>
<td>0.92</td>
<td>0.08</td>
<td>0.31<br>0.38T1, 0.37T2<br>0.26T5, 0.38E1<br>0.37E2, 0.35E3</td>
<td>0.03</td>
<td>-0.28</td>
</tr>
<tr>
<td>Zn</td>
<td>hcp<br>2.66 (1.57)</td>
<td>(0001)</td>
<td>0.69<br>1.0±1.0E8</td>
<td>-0.65</td>
<td>-0.10</td>
<td>0.32<br>0.99T1, 0.20T14<br>0.99E1, 0.99E2<br>0.91E3</td>
<td>1.44</td>
<td>1.12</td>
</tr>
<tr>
<td>Cd</td>
<td>hcp<br>3.05 (1.87)</td>
<td>(0001)</td>
<td>0.10</td>
<td>-0.11</td>
<td>0.01</td>
<td>0.21<br>0.59T1, 0.14T14<br>0.76E1, 0.74E2<br>0.73E3</td>
<td>1.07</td>
<td>0.86</td>
</tr>
<tr>
<td>Al</td>
<td>fcc<br>4.04</td>
<td>(111)</td>
<td>0.96<br>1.35T15a<br>1.35T15b<br>1.04T20<br>1.18T21<br>1.0T22<br>1.00T23<br>2.73T24<br>1.7±0.3E9<br>2.2±1.3E10<br>0.9±0.5E11<br>1.3±0.8E12<br>1.4±0.5E13</td>
<td>-0.56<br>0.54T15a<br>0.54T15b<br>-0.54T20<br>-0.40T21<br>0.0T22<br>-0.07T23<br>0.25T24<br>0.5±0.7E9</td>
<td>0.12<br>1.06T15a<br>1.04T15b<br>0.19T20<br>0.22T21<br>0.02T24</td>
<td>0.82<br>1.20T1, 0.93T2<br>1.27T5, 0.75T15a<br>0.91T15b, 1.10T19<br>0.67T20, 0.94T21<br>1.12T22, 0.62T24<br>0.96T25, 0.71T26<br>0.96T25, 0.91T28<br>1.14E1, 1.16E2<br>1.28E3</td>
<td>1.64<br>2.78T24<br>1.60T25<br>2.32T26<br>1.25T27<br>1.44T29</td>
<td>0.82</td>
</tr>
<tr>
<td>In</td>
<td>bct<br>3.37 (1.44)</td>
<td>(100)</td>
<td>-10.9</td>
<td>5.70</td>
<td>-5.72</td>
<td>0.38<br>0.59T1</td>
<td>0.48</td>
<td>0.10</td>
</tr>
<tr>
<td></td>
<td></td>
<td>(110)</td>
<td>0.27</td>
<td>-0.72</td>
<td>0.68</td>
<td>0.36<br>0.56T1, 0.70E1<br>0.68E2, 0.60E3</td>
<td>1.96</td>
<td>1.6</td>
</tr>
<tr>
<td>Tl</td>
<td>hcp<br>3.57 (1.57)</td>
<td>(0001)</td>
<td>0.83</td>
<td>-1.61</td>
<td>0.15</td>
<td>0.29<br>0.30T1, 0.70T18<br>0.60E1, 0.58E2<br>0.49E3</td>
<td>0.57</td>
<td>0.28</td>
</tr>
<tr>
<td>Sn</td>
<td>diamond<br>6.65</td>
<td>(100)</td>
<td>2.04</td>
<td>0.54</td>
<td>0.12</td>
<td>0.88</td>
<td>0.43</td>
<td>-0.45</td>
</tr>
<tr>
<td></td>
<td></td>
<td>(111)</td>
<td>-2.96</td>
<td>0.99</td>
<td>-0.82</td>
<td>0.66<br>0.61T1,*, 0.71E1<br>0.68E2, 0.61E3</td>
<td>-0.21</td>
<td>-0.87</td>
</tr>
</tbody>
</table>

<table>
  <tr>
    <td>Pb</td>
    <td>fcc</td>
    <td>(111)</td>
    <td>-4.71</td>
    <td>1.93</td>
    <td>0.51</td>
    <td>0.27</td>
    <td>0.72</td>
    <td>0.45</td>
  </tr>
  <tr>
    <td></td>
    <td>5.03</td>
    <td></td>
    <td>-3.75ᵀ²⁴</td>
    <td>0.77ᵀ²⁴</td>
    <td>-0.15ᵀ²⁴</td>
    <td>0.32ᵀ¹, 0.60ᵀ¹⁹</td>
    <td>0.64ᵀ²⁴</td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td>-4.8ᵀ³⁰</td>
    <td>1.8ᵀ³⁰</td>
    <td>-0.3ᵀ³⁰</td>
    <td>0.36ᵀ²⁴, 0.21ᵀ²⁸</td>
    <td>0.82ᵀ³²</td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td>-6.9ᵀ³¹</td>
    <td>0.6ᵀ³¹</td>
    <td>-0.7ᵀ³¹</td>
    <td>0.28ᵀ³⁰, 0.56ᵀ³¹</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td>-3.5±1.0ᴱ¹⁴</td>
    <td>0.5±1.4ᴱ¹⁴</td>
    <td>1.6±1.8ᴱ¹⁴</td>
    <td>0.26ᵀ³², 0.59ᴱ¹</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>0.60ᴱ², 0.52ᴱ³</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>0.44±0.02ᴱ¹⁵</td>
    <td></td>
    <td></td>
  </tr>
</table>

* calculated as bct structure, for (001) plane [4]
ᵀ¹ FCD-LMTO, GGA [4]
ᵀ² PAW, GGA (Perdew-Burke-Ernzerhof revised for solids (PBEsol)) [49]
ᵀ³ linear combination of Gaussian-type orbitals, GGA [50]
ᵀ⁴ pseudopotential, GGA [51]
ᵀ⁵ tight-binding (TB) LMTO, local density approximation (LDA) [3]
ᵀ⁶ semi-empirical, empirical electron surface model (EESM) [52]
ᵀ⁷ pseudopotential, LDA [53]
ᵀ⁸ᵃ exact muffin-tin orbitals (EMTO), GGA (Perdew-Burke-Ernzerhof (PBE)) [54]
ᵀ⁸ᵇ EMTO, LDA [54]
ᵀ⁹ᵃ pseudopotential, GGA [55]
ᵀ⁹ᵇ pseudopotential, LDA [55]
ᵀ¹⁰ linearized augmented plane-wave (LAPW), LDA [56]
ᵀ¹¹ pseudopotential, LDA [57]
ᵀ¹² pseudopotential, LDA [58]
ᵀ¹³ pseudopotential, LDA [59]
ᵀ¹⁴ semi-empirical, empirical electron theory (EEM) [60]
ᵀ¹⁵ᵃ full-potential linearized augmented plane-wave (FP-LAPW), GGA [19]
ᵀ¹⁵ᵇ FP-LAPW, LDA [19]
ᵀ¹⁶ pseudopotential, LDA [61]
ᵀ¹⁷ pseudopotential, LDA [62]
ᵀ¹⁸ semi-empirical, modified embedded-atom method (MEAM) [63]
ᵀ¹⁹ full-potential Korringa-Kohn-Rostoker (FKKR), LDA [64]
ᵀ²⁰ pseudopotential, GGA [20]
ᵀ²¹ pseudopotential, LDA [65]
ᵀ²² pseudopotential, LDA [66]
ᵀ²³ pseudopotential, LDA [67]
ᵀ²⁴ semi-empirical, MEAM [11]
ᵀ²⁵ pseudopotential, LDA [68]
ᵀ²⁶ pseudopotential, LDA [69]
ᵀ²⁷ pseudopotential, LDA [70]
ᵀ²⁸ semi-empirical, EESM [71]
ᵀ²⁹ linear combination of atomic orbitals (LCAO), LDA [72]
ᵀ³⁰ pseudopotential, GGA [73]
ᵀ³¹ ultrasoft pseudopotential (USPP), GGA [74]
ᵀ³² pseudopotential, LDA [75]
ᴱ¹ extrapolation from surface tension measurement [5]
ᴱ² extrapolation from surface tension measurement [6]
ᴱ³ extrapolation from surface tension measurement [76]
ᴱ⁴ low-energy electron diffraction (LEED) [77]
ᴱ⁵ LEED [78]
ᴱ⁶ LEED [79]
ᴱ⁷ LEED [80]
ᴱ⁸ LEED [81]
ᴱ⁹ LEED [82]
ᴱ¹⁰ LEED [83]
ᴱ¹¹ LEED [84]
ᴱ¹² LEED [85]
ᴱ¹³ LEED [86]
ᴱ¹⁴ LEED [87]
ᴱ¹⁵ scanning tunneling microscopy (STM) [88]


Table 2. Calculated surface relaxation ($d_{ij}$), surface energy ($\gamma$), and surface stress ($\tau$) of $3d$ transition metals. $d_{ij}$ is given in percentage, $\gamma$ and $\tau$ are in units of J/m². The calculated lattice constants $a$ are listed with the structure information, in Å. Previously reported data are also tabulated, with their annotation numbers starting as $T$ and $E$, for theoretical and experimental cases, respectively.

<table>
  <thead>
    <tr>
      <th>Metal</th>
      <th>Structure<br>$a$ ($c/a$)</th>
      <th>Surface</th>
      <th colspan="3">Relaxation</th>
      <th>$\gamma$</th>
      <th>$\tau$</th>
      <th>$\tau-\gamma$</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th>$d_{12}$</th>
      <th>$d_{23}$</th>
      <th>$d_{34}$</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Sc</td>
      <td>hcp<br>3.32 (1.55)</td>
      <td>(0001)</td>
      <td>-2.58<br>-1.89±0.76<sup>E1</sup><br>-0.04±0.19<sup>E2</sup><br>-6.08±1.14<sup>E3</sup></td>
      <td>1.19<br>-1.14±1.14<sup>E3</sup></td>
      <td>0.29</td>
      <td>1.26<br>1.83<sup>T1</sup>, 0.82<sup>T2</sup><br>0.82<sup>T3</sup>, 1.26<sup>T4</sup><br>1.28<sup>E4</sup>, 1.16<sup>E5</sup></td>
      <td>0.73</td>
      <td>-0.53</td>
    </tr>
    <tr>
      <td>Ti</td>
      <td>hcp<br>2.94 (1.59)</td>
      <td>(0001)</td>
      <td>-7.14<br>-7.7<sup>T5</sup><br>-6.84<sup>T6a</sup><br>-6.44<sup>T6b</sup><br>-6.47<sup>T7</sup><br>-7.55<sup>T8</sup><br>-6.8<sup>T9</sup><br>-4.9<sup>E6</sup><br>-2.14±2.14<sup>E7</sup></td>
      <td>2.87<br>2.8<sup>T5</sup><br>2.82<sup>T6a</sup><br>2.64<sup>T6b</sup><br>4.01<sup>T7</sup><br>2.86<sup>T8</sup><br>1.2<sup>T9</sup><br>1.4<sup>E6</sup></td>
      <td>-0.49<br>-0.51<sup>T6a</sup><br>0.37<sup>T6b</sup><br>-0.68<sup>T7</sup><br>-0.94<sup>T8</sup><br>-1.1<sup>E6</sup></td>
      <td>1.97<br>2.63<sup>T1</sup>, 1.95<sup>T2</sup><br>1.40<sup>T3</sup>, 2.19<sup>T5</sup><br>1.99<sup>T6a</sup>, 2.27<sup>T6b</sup><br>1.96<sup>T7</sup>, 1.95<sup>T8</sup><br>2.24<sup>T9</sup>, 2.10<sup>E4</sup><br>1.98<sup>E5</sup>, 1.99<sup>E8</sup></td>
      <td>0.65</td>
      <td>-1.32</td>
    </tr>
    <tr>
      <td>V</td>
      <td>bcc<br>2.99</td>
      <td>(100)</td>
      <td>-12.41<br>-9.0<sup>T10</sup><br>-6.67<sup>E9</sup></td>
      <td>0.24<br>0.6<sup>T10</sup><br>0.99<sup>E9</sup></td>
      <td>2.87</td>
      <td>2.40<br>3.03<sup>T1</sup>, 3.4<sup>T10</sup><br>2.68<sup>T11</sup>, 3.00<sup>T12</sup><br>2.11<sup>T13</sup>, 2.83<sup>T14</sup><br>2.55<sup>E4</sup>, 2.62<sup>E8</sup></td>
      <td>2.12</td>
      <td>-0.28</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>(110)</td>
      <td>-5.24<br>-0.93±0.93<sup>E10</sup></td>
      <td>0.58</td>
      <td>0.01</td>
      <td>2.41<br>3.26<sup>T1</sup>, 2.02<sup>T2</sup><br>2.66<sup>T11</sup>, 1.62<sup>T13</sup><br>2.65<sup>T14</sup></td>
      <td>2.12</td>
      <td>-0.29</td>
    </tr>
    <tr>
      <td>Cr</td>
      <td>bcc*<br>2.87</td>
      <td>(100)</td>
      <td>-5.06<br>-0.17±0.55<sup>E11</sup></td>
      <td>3.62</td>
      <td>-1.04</td>
      <td>3.06<br>3.98<sup>T1</sup>, 4.05<sup>T11</sup><br>3.37<sup>T13</sup>, 2.42<sup>T14</sup><br>2.23<sup>T15</sup>, 2.30<sup>E4</sup><br>2.89<sup>E5</sup>, 2.35<sup>E8</sup></td>
      <td>-0.32</td>
      <td>-3.38</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>(110)</td>
      <td>-1.95<br>0.89±0.25<sup>E11</sup></td>
      <td>0.44</td>
      <td>0.20</td>
      <td>3.10<br>3.51<sup>T1</sup>, 3.59<sup>T11</sup><br>2.60<sup>T13</sup>, 2.23<sup>T14</sup><br>3.58<sup>T15</sup></td>
      <td>0.79</td>
      <td>-2.31</td>
    </tr>
    <tr>
      <td>Mn</td>
      <td>bcc**<br>2.80</td>
      <td>(100)</td>
      <td></td>
      <td></td>
      <td></td>
      <td>2.14<br>1.57<sup>T15</sup></td>
      <td>-2.24</td>
      <td>-4.38</td>
    </tr>
    <tr>
      <td></td>
      <td>$\alpha$-Mn<br>8.64</td>
      <td>(100)</td>
      <td></td>
      <td></td>
      <td></td>
      <td>2.59<br>3.10<sup>T1,***</sup>, 2.80<sup>T15,***</sup><br>2.42<sup>T16,***</sup>, 1.60<sup>E4</sup><br>1.59<sup>E5</sup>, 1.54<sup>E8</sup></td>
      <td>-0.22</td>
      <td>-2.81</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>(110)</td>
      <td>-6.95<br>($\boldsymbol{d_{13}=0.99}$)</td>
      <td>12.30</td>
      <td>-1.83<br>($\boldsymbol{d_{34}=-1.83}$)</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Fe</td>
      <td>bcc<br>2.84</td>
      <td>(100)</td>
      <td>-0.18<br>-1.89<sup>T17</sup><br>-3.09<sup>T18</sup></td>
      <td>2.88<br>2.59<sup>T17</sup><br>2.83<sup>T18</sup></td>
      <td>0.78<br>0.21<sup>T17</sup><br>1.93<sup>T18</sup></td>
      <td>2.50<br>2.22<sup>T1</sup>, 3.12<sup>T11</sup><br>2.66<sup>T13</sup>, 2.57<sup>T14</sup></td>
      <td>1.39<br>0.57<sup>T23a</sup><br>1.15<sup>T23b</sup></td>
      <td>-1.11</td>
    </tr>
  </tbody>
</table>

<table><tbody><tr><td></td><td></td><td></td><td>-3.03<sup>T19</sup>
-3.6<sup>T20</sup>
0.35<sup>T21</sup>
-0.21±2.09<sup>E12</sup>
-1.4±3<sup>E13</sup></td><td>2.14<sup>T19</sup>
2.3<sup>T20</sup>
-0.14<sup>T21</sup>
1.19±2.09<sup>E12</sup></td><td>3.11<sup>T19</sup>
0.4<sup>T20</sup></td><td>2.18<sup>T15</sup>, 2.29<sup>T17</sup>
2.25<sup>T18</sup>, 2.47<sup>T20</sup>
2.35<sup>T22</sup>, 2.62<sup>T23a</sup>
3.07<sup>T23b</sup>, 2.53<sup>T24</sup></td><td>0.23<sup>T24</sup></td><td></td></tr><tr><td></td><td></td><td>(110)</td><td>-0.05
-0.13<sup>T17</sup>
-0.11<sup>T18</sup>
-0.33<sup>T19</sup>
-0.1<sup>T20</sup>
-0.35<sup>T25</sup>
-0.36<sup>T26</sup>
-0.08<sup>T27</sup>
0.23<sup>T28</sup>
-0.52<sup>T29</sup>
1±2<sup>E14</sup>
0.5±2.0<sup>E15</sup></td><td>0.71
0.20<sup>T17</sup>
1.16<sup>T18</sup>
0.89<sup>T19</sup>
0.3<sup>T20</sup>
0.44<sup>T25</sup>
0.46<sup>T26</sup>
0.40<sup>T27</sup>
0.77<sup>T28</sup>
0.43<sup>T29</sup>
0.5±1<sup>E14</sup></td><td>-0.15
-0.06<sup>T17</sup>
1.14<sup>T18</sup>
0.76<sup>T19</sup>
-0.5<sup>T20</sup>
-0.26<sup>T26</sup>
-0.25<sup>T27</sup>
-0.20<sup>T28</sup>
-0.29<sup>T29</sup></td><td>2.45
2.43<sup>T1</sup>, 3.00<sup>T11</sup>
2.05<sup>T13</sup>, 2.37<sup>T14</sup>
2.66<sup>T15</sup>, 2.27<sup>T17</sup>
2.25<sup>T18</sup>, 2.37<sup>T20</sup>
2.25<sup>T22</sup>, 2.46<sup>T24</sup>
2.29<sup>T25</sup>, 2.43<sup>T26</sup>
2.43<sup>T28</sup>, 2.41<sup>T29</sup>
2.48<sup>E4</sup>, 2.62<sup>E5</sup>
2.42<sup>E8</sup></td><td>1.56
1.91<sup>T24</sup></td><td>-0.89</td></tr><tr><td>Co</td><td>hcp
2.49 (1.62)</td><td>(0001)</td><td>-2.89
-2.55<sup>T30</sup>
-2.93±0.98<sup>E16</sup>
-2.1<sup>E17</sup></td><td>1.85
1.34<sup>T30</sup>
0.49±1.95<sup>E16</sup>
1.3<sup>E17</sup></td><td>-0.72
-0.48<sup>T30</sup>
-1.95±2.93<sup>E16</sup></td><td>2.11
2.78<sup>T1</sup>, 2.86<sup>T3</sup>
2.99<sup>T4</sup>, 2.74<sup>T15</sup>
2.55<sup>E4</sup>, 2.52<sup>E5</sup>
2.52<sup>E8</sup></td><td>2.20</td><td>0.09</td></tr><tr><td>Ni</td><td>fcc
3.52</td><td>(100)</td><td>-3.74
-3.6<sup>T31</sup>
-3.6<sup>T32</sup>
2.53<sup>T33</sup>
-3.7<sup>T34</sup>
-2.7<sup>T35</sup>
1.14±1.14<sup>E18</sup>
-3.2±0.5<sup>E19</sup></td><td>0.55
1.4<sup>T31</sup>
1.0<sup>T32</sup>
0.08<sup>T33</sup>
0.4<sup>T34</sup></td><td>0.04
0.3<sup>T31</sup>
0.00<sup>T33</sup></td><td>2.22
2.43<sup>T1</sup>, 2.61<sup>T11</sup>
2.77<sup>T15</sup>, 2.60<sup>T16</sup>
2.19<sup>T31</sup>, 2.48<sup>T32</sup>
2.42<sup>T33</sup>, 2.25<sup>T36</sup></td><td>1.73
2.37<sup>T33</sup>
2.39<sup>T37</sup></td><td>-0.49</td></tr><tr><td></td><td></td><td>(111)</td><td>-1.31
-1.02<sup>T30</sup>
-0.9<sup>T31</sup>
-1.2<sup>T32</sup>
2.70<sup>T33</sup>
-2.1<sup>T34</sup>
-1.5<sup>T35</sup>, -0.6<sup>T38</sup>
-1.23±1.23<sup>E18</sup>
0±1<sup>E20</sup></td><td>-0.09
-0.25<sup>T30</sup>
0.0<sup>T31</sup>
0.1<sup>T32</sup>
0.05<sup>T33</sup>
0.2<sup>T34</sup></td><td>0.11
0.59<sup>T30</sup>
0.0<sup>T31</sup>
0.00<sup>T33</sup></td><td>1.92
2.01<sup>T1</sup>, 2.28<sup>T8</sup>
2.69<sup>T15</sup>, 2.27<sup>T16</sup>
1.93<sup>T31</sup>, 1.88<sup>T32</sup>
2.02<sup>T33</sup>, 1.95<sup>T36</sup>
2.03<sup>T38</sup>, 2.45<sup>E4</sup>
2.37<sup>E5</sup>, 2.38<sup>E8</sup></td><td>2.16
2.00<sup>T30</sup>
2.21<sup>T33</sup>
2.23<sup>T37</sup></td><td>0.24</td></tr><tr><td>Cu</td><td>fcc
3.64</td><td>(100)</td><td>-1.61
-0.83<sup>T33</sup>
-3.6<sup>T34</sup>
-3.02<sup>T39</sup>
-1.06<sup>T40</sup>
-2.52<sup>T41</sup>
-1.2<sup>E21</sup>
-2.4<sup>E22</sup>
-1.1±0.4<sup>E23</sup>
-2.1<sup>E24</sup>
-1.1<sup>E25</sup></td><td>1.48
0.04<sup>T33</sup>
0.3<sup>T34</sup>
0.08<sup>T39</sup>
-0.65<sup>T40</sup>
0.84<sup>T41</sup>
0.9<sup>E21</sup>
1.0<sup>E22</sup>
1.7±0.6<sup>E23</sup>
0.45<sup>E24</sup>
1.7<sup>E25</sup></td><td>1.25
-0.00<sup>T33</sup>
-0.24<sup>T39</sup>
1.28<sup>T40</sup>
0.68<sup>T41</sup></td><td>1.44
2.17<sup>T1</sup>, 2.09<sup>T2</sup>
1.81<sup>T11</sup>, 1.92<sup>T16</sup>
1.65<sup>T33</sup>, 1.71<sup>T39</sup>
1.80<sup>T42</sup>, 2.15<sup>T43</sup></td><td>2.55
2.10<sup>T33</sup>
1.87<sup>T37</sup></td><td>1.11</td></tr></tbody></table>

<table><tbody><tr><td rowspan="13">(111)</td><td>-1.0±0.4<sup>E26</sup></td><td>2.0±0.8<sup>E26</sup><br></td><td rowspan="13">0.31<br>-0.24<sup>T6a</sup><br>-0.43<sup>T6b</sup><br>0.00<sup>T33</sup><br></td><td rowspan="13">1.30<br>1.95<sup>T1</sup>, 1.96<sup>T2</sup><br>1.41<sup>T6a</sup>, 1.92<sup>T6b</sup><br>1.67<sup>T11</sup>, 1.67<sup>T16</sup><br>1.41<sup>T33</sup>, 1.59<sup>T39</sup><br>1.91<sup>T43</sup>, 1.94<sup>T44</sup><br>1.83<sup>E4</sup>, 1.70<sup>E5</sup><br>1.79<sup>E8</sup></td><td rowspan="13">1.87<br>1.93<sup>T33</sup><br>1.73<sup>T37</sup><br>0±0.45<sup>E30</sup></td><td rowspan="13">0.57</td></tr><tr><td>-0.31</td><td>0.04</td></tr><tr><td>-1.19<sup>T6a</sup></td><td>-0.65<sup>T6a</sup></td></tr><tr><td>-1.58<sup>T6b</sup></td><td>-0.73<sup>T6b</sup></td></tr><tr><td>0.14<sup>T33</sup></td><td>-0.01<sup>T33</sup></td></tr><tr><td>-2.0<sup>T34</sup></td><td>0.1<sup>T34</sup></td></tr><tr><td>-1.27<sup>T39</sup></td><td>-0.64<sup>T39</sup></td><td>-0.26<sup>T39</sup></td></tr><tr><td>0.56<sup>T40</sup></td><td>-0.07<sup>T40</sup></td><td>0.55<sup>T40</sup></td></tr><tr><td>-0.60<sup>T41</sup></td><td>-0.18<sup>T41</sup></td><td>0.12<sup>T41</sup></td></tr><tr><td>-0.7<sup>E27</sup></td><td>-0.6<sup>E27</sup></td><td>-0.8<sup>E27</sup></td></tr><tr><td>-0.3±1.0<sup>E28</sup></td><td></td><td></td></tr><tr><td>0.5 ~ 1<sup>E29</sup></td><td></td><td></td></tr></tbody></table>

*commensurable antiferromagnetic state with the B2 structure [40]
** hypothetical ferromagnetic structure (unrelaxed)
*** calculated as fcc structure, for (111) plane
<sup>T1</sup> FCD-LMTO, GGA [4]
<sup>T2</sup> TB LMTO, LDA [3]
<sup>T3</sup> semi-empirical, EEM [60]
<sup>T4</sup> semi-empirical, MEAM [63]
<sup>T5</sup> LAPW, LDA [89]
<sup>T6a</sup> FP-LAPW, GGA [19]
<sup>T6b</sup> FP-LAPW, LDA [19]
<sup>T7</sup> ultrasoft pseudopotential (USPP), GGA [20]
<sup>T8</sup> PAW, GGA (Perdew-Wang 91 (PW91)) [90]
<sup>T9</sup> pseudopotential, LDA [91]
<sup>T10</sup> FP-LAPW, LDA [92]
<sup>T11</sup> PAW, GGA (PBEsol) [49]
<sup>T12</sup> FP-LAPW, LDA [93]
<sup>T13</sup> semi-empirical, EEM [94]
<sup>T14</sup> semi-empirical, second nearest-neighbor MEAM [95]
<sup>T15</sup> TB LMTO, LDA [96]
<sup>T16</sup> semi-empirical, EESM [72]
<sup>T17</sup> USPP, GGA (PW91) [97]
<sup>T18</sup> USPP, GGA [98]
<sup>T19</sup> USPP, GGA (in PW91) [99]
<sup>T20</sup> PAW, GGA [100]
<sup>T21</sup> pseudopotential, LDA [101]
<sup>T22</sup> USPP, GGA (PW 91) [102]
<sup>T23a</sup> EMTO, GGA (PBE) [103]
<sup>T23b</sup> full-potential local-orbital (FPLO), PBE [103]
<sup>T24</sup> EMTO, GGA (PBE) [104]
<sup>T25</sup> USPP, GGA [105]
<sup>T26</sup> PAW, GGA (PW91) [106]
<sup>T27</sup> PAW, LDA [107]
<sup>T28</sup> PAW, GGA(PBE) [108]
<sup>T29</sup> PAW, GGA (PBE) [132]
<sup>T30</sup> USPP, GGA (PW91) [109]
<sup>T31</sup> USPP, GGA [110]
<sup>T32</sup> PAW, GGA (PW91) [111]
<sup>T33</sup> semi-empirical, MEAM [11]
<sup>T34</sup> TB [112]
<sup>T35</sup> TB [113]
<sup>T36</sup> PAW, GGA (PBE) [114]
<sup>T37</sup> USPP, GGA (PBE) [115]
<sup>T38</sup> USPP, GGA (PW91) [116]
<sup>T39</sup> pseudopotential, LDA [117]
<sup>T40</sup> pseudopotential, LDA [118]
<sup>T41</sup> FP-LAPW, GGA (PBE) [119]
<sup>T42</sup> modified augmented plane-wave, LDA [120]
<sup>T43</sup> FKKR, LDA [64]

$^{T44}$ FP-LMTO, LDA [121]
$^{E1}$ LEED [122]
$^{E2}$ LEED [123]
$^{E3}$ LEED [124]
$^{E4}$ extrapolation from surface tension measurement [6]
$^{E5}$ extrapolation from surface tension measurement [76]
$^{E6}$ LEED [125]
$^{E7}$ LEED [126]
$^{E8}$ extrapolation from surface tension measurement [5]
$^{E9}$ LEED[127]
$^{E10}$ LEED [128]
$^{E11}$ LEED[129]
$^{E12}$ LEED [130]
$^{E13}$ LEED [131]
$^{E14}$ medium energy ion scattering (MEIS) [133]
$^{E15}$ LEED [134]
$^{E16}$ LEED [135]
$^{E17}$ LEED [136]
$^{E18}$ LEED [137]
$^{E19}$ Rutherford backscattering spectroscopy (RBS) [138]
$^{E20}$ MEIS [139]
$^{E21}$ LEED [140]
$^{E22}$ MEIS [117]
$^{E23}$ LEED [141]
$^{E24}$ LEED [142]
$^{E25}$ LEED [143]
$^{E26}$ LEED [144]
$^{E27}$ LEED [145]
$^{E28}$ LEED [146]
$^{E29}$ LEED [147]
$^{E30}$ lattice contraction experiment [148]

Table 3. Calculated surface relaxation ($d_{ij}$), surface energy ($\gamma$), and surface stress ($\tau$) of $4d$ transition metals. $d_{ij}$ is given in percentage, $\gamma$ and $\tau$ are in units of J/m². The calculated lattice constants $a$ are listed with the structure information, in Å. Previously reported data are also tabulated, with their annotation numbers starting as $T$ and $E$, for theoretical and experimental cases, respectively.

<table>
<thead>
<tr>
<th>Metal</th>
<th>Structure<br>$a$ ($c/a$)</th>
<th>Surface</th>
<th colspan="3">Relaxation<br>$d_{12}$ $d_{23}$ $d_{34}$</th>
<th>$\gamma$</th>
<th>$\tau$</th>
<th>$\tau-\gamma$</th>
</tr>
</thead>
<tbody>
<tr>
<td>Y</td>
<td>hcp<br>3.65 (1.55)</td>
<td>(0001)</td>
<td>-2.37<br>-3.66<sup>T1</sup></td>
<td>0.94</td>
<td>0.21</td>
<td>1.00<br>1.51<sup>T2</sup>, 1.18<sup>T3a</sup><br>1.38<sup>T3b</sup>, 0.68<sup>T4</sup><br>1.15<sup>T5,*</sup>, 0.74<sup>T6</sup><br>1.13<sup>E1</sup>, 1.03<sup>E2</sup></td>
<td>1.00<br>0.60<sup>T1</sup></td>
<td>0.00</td>
</tr>
<tr>
<td>Zr</td>
<td>hcp<br>3.23 (1.61)</td>
<td>(0001)</td>
<td>-6.39<br>-2.77<sup>T1</sup><br>-4.7<sup>T7</sup><br>-6.3<sup>T8</sup>, -1±2<sup>E3</sup></td>
<td>2.04<br>1.2<sup>T7</sup></td>
<td>0.25<br>1.0<sup>T7</sup></td>
<td>1.57<br>2.26<sup>T2</sup>, 1.90<sup>T3a</sup><br>2.15<sup>T3b</sup>, 1.53<sup>T4</sup><br>1.75<sup>T5,*</sup>,1.23<sup>T6</sup><br>2.04<sup>T7</sup>, 1.73<sup>T8</sup><br>2.25<sup>T9</sup>, 2.00<sup>E1</sup><br>1.73<sup>E2</sup>, 1.91<sup>E4</sup></td>
<td>1.15<br>1.57<sup>T1</sup></td>
<td>-0.42</td>
</tr>
<tr>
<td>Nb</td>
<td>bcc<br>3.31</td>
<td>(110)</td>
<td>-4.21<br>-1.88<sup>T1</sup><br>-3.7<sup>T5</sup><br>-3.6<sup>T10</sup></td>
<td>0.60<br>-0.5<sup>T10</sup></td>
<td>-0.27</td>
<td>2.06<br>2.69<sup>T2</sup>, 2.32<sup>T3a</sup>,<br>2.66<sup>T3b</sup>, 1.64<sup>T4</sup><br>2.36<sup>T5</sup>, 2.9<sup>T11</sup><br>2.32<sup>T12</sup>, 2.39<sup>T13</sup><br>2.50<sup>T14</sup>, 2.70<sup>E1</sup><br>2.49<sup>E2</sup>, 2.67<sup>E4</sup></td>
<td>2.99<br>3.44<sup>T1</sup></td>
<td>0.93</td>
</tr>
<tr>
<td rowspan="3">Mo</td>
<td rowspan="3">bcc<br>3.17</td>
<td>(100)</td>
<td>-12.44<br>-4.69<sup>T1</sup><br>-9.3<sup>T5</sup><br>-6.3<sup>T10</sup></td>
<td>-0.50<br>-0.7<sup>T10</sup></td>
<td>3.46</td>
<td>2.32<br>2.86<sup>T2</sup>, 2.86<sup>T5</sup><br>3.1<sup>T11</sup>, 2.63<sup>T12</sup><br>3.15<sup>T13</sup>, 2.77<sup>T14</sup></td>
<td>0.89<br>1.79<sup>T1</sup></td>
<td>-1.43</td>
</tr>
<tr>
<td>(110)</td>
<td>-4.74<br>-1.56<sup>T1</sup><br>-3.9<sup>T5</sup><br>-3.3<sup>T10</sup><br>-4.3<sup>T15</sup><br>-1.6±2.0<sup>E5</sup></td>
<td>0.73<br>-0.7<sup>T10</sup><br>-0.2<sup>T15</sup></td>
<td>0.22<br>-0.4<sup>T15</sup></td>
<td>2.73<br>3.45<sup>T2</sup>, 3.23<sup>T3a</sup><br>3.69<sup>T3b</sup>, 3.18<sup>T4</sup><br>3.14<sup>T5</sup>, 3.03<sup>T12</sup><br>2.54<sup>T13</sup>, 2.92<sup>T14</sup><br>2.92<sup>T15</sup>, 3.00<sup>E1</sup><br>2.07<sup>E2</sup>, 2.91<sup>E4</sup></td>
<td>2.96<br>4.15<sup>T1</sup></td>
<td>0.23</td>
</tr>
<tr>
<td>(100)</td>
<td>-13.05<br>-4.36<sup>T1</sup><br>-9.0<sup>T5</sup><br>-6.9<sup>T10</sup><br>-11.1<sup>T15</sup><br>-9.5±3.0<sup>E6</sup></td>
<td>4.20<br>-1.1<sup>T10</sup><br>2.3<sup>T15</sup><br>1.0±2.0<sup>E6</sup></td>
<td>-2.58<br>-1.7<sup>T15</sup></td>
<td>3.15<br>3.84<sup>T2</sup>, 3.52<sup>T5</sup><br>3.49<sup>T12</sup>, 3.32<sup>T13</sup><br>3.26<sup>T14</sup>, 3.34<sup>T15</sup></td>
<td>1.98<br>3.27<sup>T1</sup></td>
<td>-1.17</td>
</tr>
<tr>
<td>Tc</td>
<td>hcp<br>2.76 (1.60)</td>
<td>(0001)</td>
<td>-6.70<br>-1.53<sup>T1</sup></td>
<td>5.23</td>
<td>-3.03</td>
<td>2.21<br>3.69<sup>T2</sup>, 3.25<sup>T3a</sup><br>3.86<sup>T3b</sup>, 2.80<sup>T4</sup><br>2.63<sup>T5,*</sup>, 2.66<sup>T6</sup><br>3.15<sup>E1</sup></td>
<td>2.59<br>3.48<sup>T1</sup></td>
<td>0.38</td>
</tr>
<tr>
<td>Ru</td>
<td>hcp</td>
<td>(0001)</td>
<td>-3.96</td>
<td>0.12</td>
<td>0.10</td>
<td>2.52</td>
<td>3.15</td>
<td>0.63</td>
</tr>
</tbody>
</table>

<table>
<tbody>
<tr>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
2.73 (1.58)
</td>
<td>
-1.04<sup>T1</sup>
<br>
-3.80<sup>T16</sup>
<br>
-3<sup>T17</sup>
<br>
-4.0<sup>T18</sup>
<br>
-2.1<sup>E7</sup>
</td>
<td>
0.20<sup>T16</sup>
<br>
-0.1<sup>E7</sup>
</td>
<td>
0.44<sup>T16</sup>
<br>
0.5<sup>E7</sup>
</td>
<td>
3.93<sup>T2</sup>, 3.47<sup>T3a</sup>
<br>
4.18<sup>T3b</sup>, 3.32<sup>T4</sup>
<br>
2.99<sup>T5,*</sup>, 3.0<sup>T17</sup>
<br>
3.05<sup>E1</sup>, 2.89<sup>E2</sup>
<br>
3.04<sup>E4</sup>
</td>
<td>
4.75<sup>T1</sup>
<br>
3.33<sup>T16</sup>
</td>
<td>
</td>
</tr>
<tr>
<td>
Rh
</td>
<td>
fcc
</td>
<td>
(100)
</td>
<td>
3.85
</td>
<td>
-4.05
<br>
-1.30<sup>T1</sup>, -3.5<sup>T5</sup>
<br>
-4.3<sup>T10</sup>
<br>
-4.5<sup>T19</sup>, -5.1<sup>T20</sup>
<br>
-3.4<sup>T21</sup>
<br>
-3.8±0.2<sup>T22</sup>
<br>
0.2<sup>T23</sup>
<br>
-6.9±1.0<sup>E8</sup>
<br>
1.0±0.9<sup>E9</sup>
<br>
0.5±2.0<sup>E10</sup>
<br>
-1.4±3.6<sup>E11</sup>
</td>
<td>
0.42
<br>
0.6<sup>T10</sup>
<br>
0.7±0.3<sup>T22</sup>
<br>
-0.04<sup>T23</sup>
<br>
1.9±1.0<sup>E8</sup>
</td>
<td>
0.34
<br>
0.6±0.3<sup>T22</sup>
<br>
-0.04<sup>T23</sup>
</td>
<td>
2.35
<br>
2.80<sup>T2</sup>, 2.90<sup>T4</sup>
<br>
2.81<sup>T5</sup>, 2.84<sup>T12</sup>
<br>
2.79<sup>T19</sup>, 2.59<sup>T20</sup>
<br>
2.65<sup>T24</sup>, 2.90<sup>T25</sup>
<br>
3.12<sup>T26</sup>
</td>
<td>
2.35
<br>
2.14<sup>T1</sup>
<br>
4.30<sup>T19</sup>
<br>
3.15<sup>T21</sup>
<br>
2.04<sup>T27</sup>
</td>
<td>
0.00
</td>
</tr>
<tr>
<td>
</td>
<td>
</td>
<td>
(111)
</td>
<td>
</td>
<td>
-1.80
<br>
-0.20<sup>T1</sup>, -2.5<sup>T5</sup>
<br>
-2.4<sup>T10</sup>
<br>
-2.02<sup>T16</sup>
<br>
-1.6<sup>T21</sup>
<br>
-1.7±0.2<sup>T22</sup>
<br>
-1.6±0.8<sup>E9</sup>
<br>
-2±2<sup>E12</sup>
<br>
-2.7±1.4<sup>E13</sup>
</td>
<td>
-0.74
<br>
0.3<sup>T10</sup>
<br>
-1.55<sup>T16</sup>
<br>
-0.3±0.1<sup>T22</sup>
</td>
<td>
0.63
<br>
-0.29<sup>T16</sup>
<br>
0.5±0.1<sup>T22</sup>
</td>
<td>
2.01
<br>
2.47<sup>T2</sup>, 2.63<sup>T3a</sup>
<br>
3.34<sup>T3b</sup>, 2.78<sup>T4</sup>
<br>
2.53<sup>T5</sup>, 2.44<sup>T12</sup>
<br>
2.59<sup>T25</sup>, 2.65<sup>T26</sup>
<br>
2.70<sup>E1</sup>, 2.61<sup>E2</sup>
<br>
2.66<sup>E4</sup>
</td>
<td>
2.73
<br>
2.11<sup>T1</sup>
<br>
2.29<sup>T16</sup>
<br>
2.97<sup>T21</sup>
</td>
<td>
0.72
</td>
</tr>
<tr>
<td>
Pd
</td>
<td>
fcc
</td>
<td>
(100)
</td>
<td>
3.96
</td>
<td>
-1.33
<br>
-0.75<sup>T1</sup>, -0.6<sup>T5</sup>
<br>
-4.2<sup>T10</sup>
<br>
-0.8<sup>T19</sup>, -1.20<sup>T29</sup>
<br>
-1.30<sup>T28</sup>
<br>
-1.97<sup>T30</sup>
<br>
0.29±1.54<sup>E14</sup>
<br>
0.3±2.6<sup>E15</sup>
</td>
<td>
-0.13
<br>
0.6<sup>T10</sup>
<br>
-0.00<sup>T28</sup>
<br>
0.17<sup>T30</sup>
<br>
-0.77±1.54<sup>E14</sup>
</td>
<td>
0.27
<br>
0.35<sup>T28</sup>
<br>
-0.01<sup>T30</sup>
</td>
<td>
1.51
<br>
2.33<sup>T2</sup>, 1.90<sup>T4</sup>
<br>
1.86<sup>T5</sup>, 1.84<sup>T12</sup>
<br>
1.79<sup>T19</sup>, 2.22<sup>T26</sup>
<br>
1.49<sup>T28</sup>, 2.13<sup>T29</sup>
<br>
1.66<sup>T30</sup>, 2.17<sup>T31</sup>
<br>
2.3<sup>E9</sup>
</td>
<td>
2.16
<br>
1.69<sup>T1</sup>
<br>
2.07<sup>T19</sup>
<br>
2.69<sup>T30</sup>
</td>
<td>
0.65
</td>
</tr>
<tr>
<td>
</td>
<td>
</td>
<td>
(111)
</td>
<td>
</td>
<td>
0.42
<br>
0.28<sup>T1</sup>, -0.1<sup>T5</sup>
<br>
-2.5<sup>T10</sup>
<br>
0.55<sup>T16</sup>
<br>
0.25<sup>T28</sup>
<br>
-0.32<sup>T30</sup>
<br>
-0.01<sup>T32a</sup>
<br>
-0.22<sup>T32b</sup>
<br>
-0.03<sup>T33</sup>
<br>
-0.10<sup>T34</sup>
<br>
1.3±1.3<sup>E16</sup>
<br>
2.4±0.9<sup>E17</sup>
<br>
0.0±4.4<sup>E18</sup>
</td>
<td>
-0.32
<br>
0.3<sup>T10</sup>
<br>
-0.06<sup>T16</sup>
<br>
-0.34<sup>T28</sup>
<br>
-0.02<sup>T30</sup>
<br>
-0.41<sup>T32a</sup>
<br>
-0.53<sup>T32b</sup>
<br>
0.08<sup>T33</sup>
<br>
-1.3±1.3<sup>E16</sup>
<br>
0.7±0.9<sup>E17</sup>
</td>
<td>
-0.07
<br>
0.25<sup>T16</sup>
<br>
0.10<sup>T28</sup>
<br>
-0.00<sup>T30</sup>
<br>
-0.22<sup>T32a</sup>
<br>
-0.33<sup>T32b</sup>
<br>
0.00<sup>T33</sup>
<br>
2.2±1.3<sup>E16</sup>
<br>
0.7±1.8<sup>E17</sup>
</td>
<td>
1.33
<br>
1.92<sup>T2</sup>, 1.65<sup>T3a</sup>
<br>
2.29<sup>T3b</sup>, 1.88<sup>T4</sup>
<br>
1.64<sup>T5</sup>, 1.59<sup>T12</sup>
<br>
2.01<sup>T26</sup>, 1.31<sup>T28</sup>
<br>
1.38<sup>T30</sup>, 1.89<sup>T31</sup>
<br>
1.33<sup>T32a</sup>, 1.87<sup>T32b</sup>
<br>
1.85<sup>T35</sup>, 2.05<sup>E1</sup>
<br>
1.99<sup>E2</sup>, 2.00<sup>E4</sup>
</td>
<td>
2.57
<br>
2.15<sup>T1</sup>
<br>
1.89<sup>T16</sup>
<br>
3.14<sup>T30</sup>
<br>
3.69<sup>T36</sup>
<br>
6.0±0.9<sup>E19</sup>
</td>
<td>
1.24
</td>
</tr>
<tr>
<td>
Ag
</td>
<td>
fcc
</td>
<td>
(100)
</td>
<td>
4.16
</td>
<td>
-1.71
<br>
-1.08<sup>T1</sup>, -1.9<sup>T5</sup>
<br>
-4.5<sup>T10</sup>
<br>
-1.04<sup>T30</sup>
</td>
<td>
0.56
<br>
0.6
<br>
0.11<sup>T30</sup>
</td>
<td>
0.25
<br>
-0.01<sup>T30</sup>
</td>
<td>
0.84
<br>
1.20<sup>T2</sup>, 1.20<sup>T4</sup>
<br>
1.21<sup>T5</sup>, 1.14<sup>T12</sup>
<br>
1.12<sup>T19</sup>, 1.40<sup>T26</sup>
</td>
<td>
1.31
<br>
0.88<sup>T1</sup>
<br>
1.68<sup>T19</sup>
<br>
1.48<sup>T30</sup>
</td>
<td>
0.47
</td>
</tr>
</tbody>
</table>


<table>
<tbody>
<tr>
<td>
</td>
<td>
$-1.9^{T37}$
</td>
<td>
</td>
<td>
</td>
<td>
$1.09^{T30}$, $1.03^{T31}$
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
</td>
<td>
$0\pm1.5^{E20}$
</td>
<td>
</td>
<td>
</td>
<td>
$1.24^{T37}$, $1.27^{T38}$
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
$1.3^{E9}$
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
(111)
</td>
<td>
-0.30
</td>
<td>
-0.46
</td>
<td>
0.07
</td>
<td>
0.76
</td>
<td>
0.79
</td>
<td>
0.03
</td>
</tr>
<tr>
<td>
</td>
<td>
$0.16^{T1}$, $-1.4^{T5}$
</td>
<td>
</td>
<td>
</td>
<td>
$1.17^{T2}$, $0.89^{T3a}$
</td>
<td>
$0.75^{T1}$
</td>
<td>
</td>
</tr>
<tr>
<td>
</td>
<td>
$-2.6^{T10}$
</td>
<td>
$0.1^{T10}$
</td>
<td>
</td>
<td>
$1.40^{T3b}$, $1.12^{T4}$
</td>
<td>
$1.75^{T30}$
</td>
<td>
</td>
</tr>
<tr>
<td>
</td>
<td>
$0.94^{T30}$
</td>
<td>
$-0.07^{T30}$
</td>
<td>
$0.00^{T30}$
</td>
<td>
$1.21^{T5}$, $1.07^{T12}$
</td>
<td>
$1.42\pm0.30^{E26}$
</td>
<td>
</td>
</tr>
<tr>
<td>
</td>
<td>
$-1.3^{T37}$
</td>
<td>
</td>
<td>
</td>
<td>
$1.25^{T26}$, $1.09^{T30}$
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
</td>
<td>
$0.00\pm0.85^{E21}$
</td>
<td>
$0.00\pm1.27^{E21}$
</td>
<td>
</td>
<td>
$0.90^{T31}$, $1.24^{T37}$
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
</td>
<td>
$-2.5^{E22}$, $-2\sim^{E23}$
</td>
<td>
</td>
<td>
</td>
<td>
$1.25^{E1}$, $1.20^{E2}$
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
</td>
<td>
$0^{E24}$, $-2.5^{E25}$
</td>
<td>
</td>
<td>
</td>
<td>
$1.25^{E4}$
</td>
<td>
</td>
<td>
</td>
</tr>
</tbody>
</table>

$^{*}$ calculated as fcc structure, for (111) layer

$^{T1}$ exact muffin-tin orbitals, GGA [22]

$^{T2}$ FCD-LMTO, GGA [4]

$^{T3a}$ exact muffin-tin orbitals (EMTO), GGA (PBE) [65]

$^{T3b}$ exact muffin-tin orbitals (EMTO), LDA [65]

$^{T4}$ TB LMTO, LDA [3]

$^{T5}$ FP-LMTO, LDA [17]

$^{T6}$ semi-empirical, EEM [60]

$^{T7}$ pseudopotential, LDA [149]

$^{T8}$ LAPW, LDA [89]

$^{T9}$ semi-empirical, MEAM [63]

$^{T10}$ TB [112]

$^{T11}$ FP-LAPW, LDA[150]

$^{T12}$ PAW, GGA (PBEsol) [49]

$^{T13}$ semi-empirical, EEM [94]

$^{T14}$ semi-empirical, second nearest-neighbor MEAM [95]

$^{T15}$ pseudopotential, LDA [151]

$^{T16}$ USPP, GGA (PW91) [109]

$^{T17}$ pseudopotentials, LDA [152]

$^{T18}$ LAPW, LDA [153]

$^{T19}$ FP-LMTO, LDA [154]

$^{T20}$ LAPW, LDA [16]

$^{T21}$ USPP, LDA [155]

$^{T22}$ USPP, LDA [156]

$^{T23}$ semi-empirical, MEAM [157]

$^{T24}$ pseudopotentials, LDA [158]

$^{T25}$ semi-empirical, MEAM [159]

$^{T26}$ FKKR, LDA [64]

$^{T27}$ USPP, GGA (PBE) [115]

$^{T28}$ FP-LAPW, GGA [19]

$^{T29}$ pseudopotentials, LDA [160]

$^{T30}$ semi-empirical, MEAM [11]

$^{T31}$ semi-empirical, EESM [71]

$^{T32a}$ USPP, GGA [20]

$^{T32b}$ USPP, LDA [20]

$^{T33}$ FP-LAPW, GGA [161]

$^{T34}$ FCD-LMTO, LDA and GGA [4, 48]

$^{T35}$ USPP, LDA [162]

$^{T36}$ LCAO [163]

$^{T37}$ FP-LMTO, LDA [164]

$^{T38}$ FP-LAPW, LDA [165]

$^{E1}$ extrapolation from surface tension measurement [6]

$^{E2}$ extrapolation from surface tension measurement [76]

$^{E3}$ LEED [166]

$^{E4}$ extrapolation from surface tension measurement [5]

$^{E5}$ LEED [167]

$^{E6}$ LEED [168]

$^{E7}$ LEED [153]

$^{E8}$ LEED [169]

$^{E9}$ LEED [170]
$^{E10}$ LEED [171]
$^{E11}$ LEED [172]
$^{E12}$ LEED [173]
$^{E13}$ LEED [174]
$^{E14}$ LEED [175]
$^{E15}$ LEED [176]
$^{E16}$ LEED [177]
$^{E17}$ LEED [178]
$^{E18}$ high energy ion scattering (HEIS) [179]
$^{E19}$ measurement from metal clusters [180]
$^{E20}$ LEED [181]
$^{E21}$ LEED [182]
$^{E22}$ MEIS [183]
$^{E23}$ HEIS [184]
$^{E24}$ LEED [185]
$^{E25}$ MEIS [186]
$^{E26}$ lattice contraction experiment [187]

<table><tbody><tr><td colspan="10">ACCEPTED MANUSCRIPT</td></tr><tr><td colspan="10">Table 4. Calculated surface relaxation ($d_{ij}$), surface energy ($\gamma$), and surface stress ($\tau$) of $5d$ transition metals. $d_{ij}$ is given in percentage, $\gamma$ and $\tau$ are in units of J/m². The calculated lattice constants $a$ are listed with the structure information, in Å. Previously reported data are also tabulated, with their annotation numbers starting as $T$ and $E$, for theoretical and experimental cases, respectively.</td></tr><tr><td>Metal</td><td>Structure</td><td>Surface</td><td colspan="3">Relaxation</td><td>$\gamma$</td><td>$\tau$</td><td>$\tau-\gamma$</td></tr><tr><td></td><td>$a$ ($c/a$)</td><td></td><td>$d_{12}$</td><td>$d_{23}$</td><td>$d_{34}$</td><td></td><td></td><td></td></tr><tr><td>La</td><td>hcp</td><td>(0001)</td><td>-4.77</td><td>4.33</td><td>-1.99</td><td>0.71</td><td>0.64</td><td>-0.07</td></tr><tr><td></td><td>3.77 (1.63)</td><td></td><td></td><td></td><td></td><td>$1.12^{T1},0.57^{T2}$</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>$1.02^{E1},0.85^{E2}$</td><td></td><td></td></tr><tr><td>Hf</td><td>hcp</td><td>(0001)</td><td>-6.86</td><td>3.49</td><td>-1.03</td><td>1.73</td><td>1.24</td><td>-0.49</td></tr><tr><td></td><td>3.19 (1.58)</td><td></td><td></td><td></td><td></td><td>$2.47^{T1},1.75^{T2}$</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>$1.79^{T3},2.15^{E1}$</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>$2.19^{E3}$</td><td></td><td></td></tr><tr><td>Ta</td><td>bcc</td><td>(100)</td><td>-13.43</td><td>0.09</td><td>2.98</td><td>2.47</td><td>1.78</td><td>-0.69</td></tr><tr><td></td><td>3.31</td><td></td><td>$-13.9^{T4}$</td><td>$0.15^{T4}$</td><td>$3.0^{T4}$</td><td>$3.10^{T1},2.74^{T6}$</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>$-6.3^{T5}$</td><td>$-1.9^{T5}$</td><td>$1.9^{T5}$</td><td>$2.27^{T4},3.59^{T7}$</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>$-11\pm2^{E4}$</td><td>$1^{E4}$</td><td></td><td>$3.09^{T8}$</td><td></td><td></td></tr><tr><td></td><td></td><td>(110)</td><td>-4.87</td><td>0.24</td><td>0.01</td><td>2.37</td><td>2.58</td><td>0.21</td></tr><tr><td></td><td></td><td></td><td>$-5.1^{T4}$</td><td>$0.06^{T4}$</td><td>$-0.1^{T4}$</td><td>$3.08^{T1},1.80^{T2}$</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>$-3.8^{T5}$</td><td>$1.0^{T5}$</td><td>$-0.5^{T5}$</td><td>$2.31^{T4},2.58^{T6}$</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>$2.73^{T7},2.79^{T8}$</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>$3.15^{E1},2.90^{E3}$</td><td></td><td></td></tr><tr><td>W</td><td>bcc</td><td>(100)</td><td>-12.16</td><td>2.97</td><td>-1.34</td><td>4.02</td><td>2.71</td><td>-1.31</td></tr><tr><td></td><td>3.17</td><td></td><td>$-3.5^{T5}$</td><td>$-0.6^{T5}$</td><td></td><td>$4.64^{T1},4.28^{T6}$</td><td>$1.28^{T9}$</td><td></td></tr><tr><td></td><td></td><td></td><td>$-4.02^{T9}$</td><td>$3.06^{T9}$</td><td></td><td>$3.86^{T7},4.05^{T8}$</td><td>$1.28^{T12}$</td><td></td></tr><tr><td></td><td></td><td></td><td>$-5.5^{T10}$</td><td>$2.4^{T10}$</td><td>$1.2^{T10}$</td><td>$7.77^{T9},4.78^{T11}$</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>$-6.33\pm6.33^{E5}$</td><td></td><td></td><td>$6.0\pm0.9^{E13}$</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>$-4.4\pm3.2^{E6}$</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>$-11\pm2^{E7}$</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>$-6\sim^{E8}$</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>$-5.5\pm1.5^{E9}$</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>$-6.7\pm2E^{10}$</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>$-7.0\pm1.5^{E11}$</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>$-6.0\pm1.5^{E12}$</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>(110)</td><td>-3.76</td><td>0.45</td><td>0.02</td><td>3.28</td><td>4.08</td><td>0.80</td></tr><tr><td></td><td></td><td></td><td>$-3.6^{T13}$</td><td>$0.2^{T13}$</td><td></td><td>$4.01^{T1},3.84^{T2}$</td><td>$2.72^{T9}$</td><td></td></tr><tr><td></td><td></td><td></td><td>$-4.1^{T14}$</td><td>$-0.4^{T14}$</td><td></td><td>$3.49^{T6},2.95^{T7}$</td><td>$3.75^{T12}$</td><td></td></tr><tr><td></td><td></td><td></td><td>$-1.4^{T5}$</td><td>$-0.4^{T5}$</td><td></td><td>$3.47^{T8},5.08^{T9}$</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>$-0.8^{T9}$</td><td>$0.3^{T9}$</td><td></td><td>$3.68^{E1},3.27^{E3}$</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>$-5.0^{T15}$</td><td>$4.6^{T15}$</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>$0.0\pm3.0^{E14}$</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>$-2.0\sim^{E15}$</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>$1.0\pm2.0^{E16}$</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>$-3.1\pm0.6^{E17}$</td><td>$0.0\pm0.9^{E17}$</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>$-3.0\pm1.3^{E18}$</td><td>$0.2\pm1.3^{E18}$</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>$-2.2\pm1.0^{E19}$</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>$-2.7\pm0.5^{E20}$</td><td>$0.0\pm0.3^{E20}$</td><td></td><td></td><td></td><td></td></tr><tr><td>Re</td><td>hcp</td><td>(0001)</td><td>-6.23</td><td>3.94</td><td>-2.72</td><td>2.61</td><td>3.37</td><td>0.76</td></tr><tr><td></td><td>2.77 (1.62)</td><td></td><td>$-6.03^{T16}$</td><td>$3.43^{T16}$</td><td>$-1.75^{T16}$</td><td>$4.21^{T1},3.27^{T2}$</td><td>$3.54^{T16}$</td><td></td></tr><tr><td colspan="10">37</td></tr></tbody></table>

<table>
<tbody><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>2.94ᴛ³, 3.77ᴛ¹⁷
3.60ᴱ¹, 2.52ᴱ²
3.63ᴱ³</td><td></td><td></td></tr>
<tr><td rowspan="2">Os</td><td rowspan="2">hcp
2.75 (1.58)</td><td>(10$\overline{1}$0)</td><td>-16.44</td><td>0.12</td><td>-1.85</td><td rowspan="2">2.96
4.57ᴛ¹, 4.04ᴛ²
3.45ᴱ¹, 3.44ᴱ³</td><td rowspan="2">5.07</td><td rowspan="2">2.11</td></tr>
<tr><td>(0001)</td><td>-3.79</td><td>0.04</td><td>0.89</td></tr>
<tr><td rowspan="3">Ir</td><td rowspan="3">fcc
3.88</td><td>(10$\overline{1}$0)</td><td>-17.20</td><td>0.63</td><td>-2.41</td><td rowspan="3">2.84
3.72ᴛ¹, 3.81ᴛ²
3.24ᴛ⁶, 3.98ᴛ¹⁸
3.49ᴛ¹⁹, 3.73ᴛ²⁰
3.74ᴛ²², 2.90ᴛ²³
3.71ᴛ²⁴</td><td rowspan="3">3.25
4.01ᴛ¹⁸
6.36ᴛ²²</td><td rowspan="3">0.41</td></tr>
<tr><td>(100)</td><td>-5.42
-2.7ᴛ⁵
-3.8ᴛ¹⁸
-6.56ᴛ¹⁹
-3.8ᴛ²⁰
0.59ᴛ²¹
-2±2ᴱ²¹</td><td>0.99
0.2ᴛ⁵
1.0ᴛ¹⁸
0.0</td><td>0.35
-0.5ᴛ¹⁸
-0.02</td></tr>
<tr><td>(111)</td><td>-2.09
-1.5ᴛ⁵
-1.91ᴛ¹⁶
-1.3ᴛ¹⁸
-3.0ᴛ²⁰</td><td>-0.51
0.1ᴛ⁵
-0.47ᴛ¹⁶
-0.2ᴛ¹⁸</td><td>0.32
0.22ᴛ¹⁶
0.0ᴛ¹⁸</td></tr>
<tr><td rowspan="3">Pt</td><td rowspan="3">fcc
3.98</td><td></td><td></td><td></td><td></td><td>2.06
2.97ᴛ¹, 3.41ᴛ²
2.56ᴛ⁶, 3.26ᴛ¹⁸
3.00ᴛ²⁰, 3.26ᴛ²²
2.82ᴛ²³, 3.02ᴛ²⁴
3.27ᴛ²⁵, 3.00ᴱ¹
3.05ᴱ², 2.93ᴱ⁵</td><td>4.37
4.45ᴛ¹⁶
4.87ᴛ¹⁸
5.30ᴛ²²
5.30ᴛ²⁵</td><td>2.31</td></tr>
<tr><td>(100)</td><td>-2.54
-4.1ᴛ⁵
-2.37ᴛ²⁶
-2.11ᴛ²⁷
0.2±2.6ᴱ²²</td><td>-0.47
0.2ᴛ⁵
-0.55ᴛ²⁶
0.17ᴛ²⁷</td><td>0.03
0.29ᴛ²⁶
-0.01ᴛ²⁷</td><td>1.85
2.73ᴛ¹, 2.48ᴛ²
2.23ᴛ⁶, 2.51ᴛ²²
2.65ᴛ²⁴, 1.81ᴛ²⁶
2.16ᴛ²⁷, 1.75ᴛ²⁸</td><td>3.32
3.61ᴛ¹²
5.59ᴛ²²
3.98ᴛ²⁷</td><td>1.47</td></tr>
<tr><td>(111)</td><td>0.99
-2.3ᴛ⁵
0.77ᴛ¹⁶ᵇ
0.85ᴛ²⁶
1.08ᴛ²⁷
1.14ᴛ²⁹ᵃ
0.88ᴛ²⁹ᵇ
1.3ᴛ³⁰
1.20ᴛ³¹
0.87ᴛ³²
1.1±0.44ᴱ²³
0.5±0.9ᴱ²⁴
1.4±0.9ᴱ²⁵</td><td>-0.49
0.2ᴛ⁵
-0.23ᴛ¹⁶ᵇ
-0.56ᴛ²⁶
-0.03ᴛ²⁷
-0.29ᴛ²⁹ᵃ
-0.22ᴛ²⁹ᵇ
0.3ᴛ³⁰
-0.50ᴛ³¹</td><td>-0.12
-0.13ᴛ¹⁶ᵇ
-0.15ᴛ²⁶
0.00ᴛ²⁷
-0.21ᴛ²⁹ᵃ
-0.17ᴛ²⁹ᵇ
0.5ᴛ³⁰</td><td>1.49
2.30ᴛ¹, 2.35ᴛ²
1.81ᴛ⁶, 2.31ᴛ²⁴
2.20ᴛ¹⁸, 1.49ᴛ²⁶
1.65ᴛ²⁷, 1.52ᴛ²⁸
1.67ᴛ²⁹ᵃ, 2.23ᴛ²⁹ᵇ
2.07ᴛ³³, 2.20ᴛ³⁴
2.48ᴱ¹, 2.49ᴱ²
2.37ᴱ⁵, 2.91ᴱ²⁵</td><td>4.25
5.24ᴛ¹²
4.45ᴛ¹⁶ᵇ
5.61ᴛ²⁵
6.67ᴛ²⁷
5.60ᴛ³⁴
6.28ᴛ³⁵
4.94ᴛ³⁶
2.57±0.40ᴱ²⁶</td><td>2.76</td></tr>
<tr><td rowspan="3">Au</td><td rowspan="3">fcc
4.17</td><td>(100)</td><td>-1.52
-6.1ᴛ⁵
-1.0ᴛ²⁰
-1.51ᴛ²⁶
-5.83ᴛ²⁷
-1.2ᴛ³⁷
-20±3ᴱ²⁷</td><td>0.10
0.5ᴛ⁵
0.33ᴛ²⁶
1.19ᴛ²⁷
0.4ᴛ³⁷
2±3ᴱ²⁷</td><td>0.32
0.24ᴛ²⁶
-0.23ᴛ²⁷</td><td>0.86
1.63ᴛ¹, 1.71ᴛ²
1.19ᴛ⁶, 1.32ᴛ²⁰
1.42ᴛ²², 1.62ᴛ²⁴
0.85ᴛ²⁶, 1.03ᴛ²⁷
1.26ᴛ²⁸, 1.39ᴛ³⁷</td><td>2.07
3.14ᴛ²²
2.06ᴛ²⁷</td><td>1.21</td></tr>
<tr><td>(111)</td><td>1.67
-3.7ᴛ⁵
-0.4ᴛ²⁰</td><td>0.04
0.8ᴛ⁵</td><td>0.22</td><td>0.71
1.28ᴛ¹, 1.61ᴛ²
1.01ᴛ⁶, 1.32ᴛ²⁰</td><td>1.77
2.77ᴛ²⁵
1.18±0.09ᴱ²⁸</td><td>1.06</td></tr>
<tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
</tbody></table>

<table>
<tbody>
<tr>
<td>
</td>
<td>
$-0.04^{T26}$
</td>
<td>
$-1.86^{T26}$
</td>
<td>
$-1.40^{T26}$
</td>
<td>
$1.39^{T24}$, $1.25^{T25}$
</td>
</tr>
<tr>
<td>
</td>
<td>
$-3.22^{T27}$
</td>
<td>
$0.58^{T27}$
</td>
<td>
$-0.10^{T27}$
</td>
<td>
$0.74^{T26}$, $0.87^{T27}$
</td>
</tr>
<tr>
<td>
</td>
<td>
$0.8^{T38}$
</td>
<td>
$-0.3^{T38}$
</td>
<td>
</td>
<td>
$1.09^{T28}$, $1.04^{T38}$
</td>
</tr>
<tr>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
$1.50^{E1}$, $1.51^{E2}$
</td>
</tr>
<tr>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
$1.51^{E5}$
</td>
</tr>
<tr>
<td colspan="5">
$^{T1}$ FCD-LMTO, GGA [4]
</td>
</tr>
<tr>
<td colspan="5">
$^{T2}$ TB LMTO, LDA [3]
</td>
</tr>
<tr>
<td colspan="5">
$^{T3}$ semi-empirical, EEM [60]
</td>
</tr>
<tr>
<td colspan="5">
$^{T4}$ PAW, GGA [188]
</td>
</tr>
<tr>
<td colspan="5">
$^{T5}$ TB [112]
</td>
</tr>
<tr>
<td colspan="5">
$^{T6}$ PAW, GGA (PBEsol) [49]
</td>
</tr>
<tr>
<td colspan="5">
$^{T7}$ semi-empirical, EEM [94]
</td>
</tr>
<tr>
<td colspan="5">
$^{T8}$ semi-empirical, second nearest-neighbor MEAM [95]
</td>
</tr>
<tr>
<td colspan="5">
$^{T9}$ modified LAPW, LDA [189]
</td>
</tr>
<tr>
<td colspan="5">
$^{T10}$ FP-LAPW, LDA [92]
</td>
</tr>
<tr>
<td colspan="5">
$^{T11}$ FP-LAPW, LDA [93]
</td>
</tr>
<tr>
<td colspan="5">
$^{T12}$ USPP, GGA (PBE) [115]
</td>
</tr>
<tr>
<td colspan="5">
$^{T13}$ FP-LAPW, LDA [190]
</td>
</tr>
<tr>
<td colspan="5">
$^{T14}$ FP-LAPW, LDA [191]
</td>
</tr>
<tr>
<td colspan="5">
$^{T15}$ TB [192]
</td>
</tr>
<tr>
<td colspan="5">
$^{T16}$ USPP, GGA (PW91) [109]
</td>
</tr>
<tr>
<td colspan="5">
$^{T16b}$ USPP, LDA [109]
</td>
</tr>
<tr>
<td colspan="5">
$^{T17}$ semi-empirical, MEAM [63]
</td>
</tr>
<tr>
<td colspan="5">
$^{T18}$ pseudopotential, LDA [193]
</td>
</tr>
<tr>
<td colspan="5">
$^{T19}$ pseudopotential, LDA [194]
</td>
</tr>
<tr>
<td colspan="5">
$^{T20}$ FP-LMTO, LDA [164]
</td>
</tr>
<tr>
<td colspan="5">
$^{T21}$ semi-empirical, MEAM [157]
</td>
</tr>
<tr>
<td colspan="5">
$^{T22}$ FP-LMTO, LDA [154]
</td>
</tr>
<tr>
<td colspan="5">
$^{T23}$ semi-empirical, MEAM [159]
</td>
</tr>
<tr>
<td colspan="5">
$^{T24}$ FKKR, LDA [64]
</td>
</tr>
<tr>
<td colspan="5">
$^{T25}$ pseudopotential, LDA [15, 195]
</td>
</tr>
<tr>
<td colspan="5">
$^{T26}$ USPP, GGA [20]
</td>
</tr>
<tr>
<td colspan="5">
$^{T27}$ semi-empirical, MEAM [11]
</td>
</tr>
<tr>
<td colspan="5">
$^{T28}$ semi-empirical, EESM [71]
</td>
</tr>
<tr>
<td colspan="5">
$^{T29a}$ FP-LAPW, GGA [19]
</td>
</tr>
<tr>
<td colspan="5">
$^{T29b}$ FP-LAPW, LDA [19]
</td>
</tr>
<tr>
<td colspan="5">
$^{T30}$ FP-LAPW, LDA [196]
</td>
</tr>
<tr>
<td colspan="5">
$^{T31}$ pseudopotential, GGA (PBE) [197]
</td>
</tr>
<tr>
<td colspan="5">
$^{T32}$ LCAO, LDA/GGA (PW91) [198]
</td>
</tr>
<tr>
<td colspan="5">
$^{T33}$ pseudopotential, LDA [199]
</td>
</tr>
<tr>
<td colspan="5">
$^{T34}$ LCAO, LDA [163]
</td>
</tr>
<tr>
<td colspan="5">
$^{T35}$ LCAO, LDA [200]
</td>
</tr>
<tr>
<td colspan="5">
$^{T36}$ pseudopotential, LDA [201]
</td>
</tr>
<tr>
<td colspan="5">
$^{T37}$ pseudopotential, LDA [202]
</td>
</tr>
<tr>
<td colspan="5">
$^{T38}$ pseudopotential, LDA [203]
</td>
</tr>
<tr>
<td colspan="5">
$^{E1}$ extrapolation from surface tension measurement [6]
</td>
</tr>
<tr>
<td colspan="5">
$^{E2}$ extrapolation from surface tension measurement [76]
</td>
</tr>
<tr>
<td colspan="5">
$^{E3}$ extrapolation from surface tension measurement [5]
</td>
</tr>
<tr>
<td colspan="5">
$^{E4}$ LEED [204]
</td>
</tr>
<tr>
<td colspan="5">
$^{E5}$ LEED [205]
</td>
</tr>
<tr>
<td colspan="5">
$^{E6}$ LEED [206]
</td>
</tr>
<tr>
<td colspan="5">
$^{E7}$ LEED [207]
</td>
</tr>
<tr>
<td colspan="5">
$^{E8}$ ion backscattering [208]
</td>
</tr>
<tr>
<td colspan="5">
$^{E9}$ LEED [209]
</td>
</tr>
<tr>
<td colspan="5">
$^{E10}$ LEED [210]
</td>
</tr>
<tr>
<td colspan="5">
$^{E11}$ spin-polarized LEED [211]
</td>
</tr>
<tr>
<td colspan="5">
$^{E12}$ LEED [212]
</td>
</tr>
<tr>
<td colspan="5">
$^{E13}$ spark discharge technique [213]
</td>
</tr>
<tr>
<td colspan="5">
$^{E14}$ LEED [214]
</td>
</tr>
<tr>
<td colspan="5">
$^{E15}$ HEIS [215]
</td>
</tr>
<tr>
<td colspan="5">
$^{E16}$ photoelectron diffraction [216]
</td>
</tr>
<tr>
<td colspan="5">
$^{E17}$ LEED [217]
</td>
</tr>
</tbody>
</table>

$^{E18}$ LEED [218]
$^{E19}$ spin-polarized LEED [219]
$^{E20}$ surface XRD [220]
$^{E21}$ LEED [221]
$^{E22}$ HEIS [222]
$^{E23}$ LEED [223]
$^{E24}$ LEED [224]
$^{E25}$ MEIS [225]
$^{E26}$ lattice contraction experiment [148]
$^{E27}$ XRD [226]
$^{E28}$ lattice contraction experiment [227]

Table 5. Calculated surface relaxation ($d_{ij}$), surface energy ($\gamma$), and surface stress ($\tau$) of light actinides.
$d_{ij}$ is given in percentage, $\gamma$ and $\tau$ are in units of J/m². The calculated lattice constants $a$ are listed
with the structure information, in Å. Previously reported data are also tabulated, with their
annotation numbers starting as $T$ and $E$, for theoretical and experimental cases, respectively.

<table>
<thead>
<tr>
<th>Metal</th>
<th>Structure<br>$a$ ($c/a$)</th>
<th>Surface</th>
<th colspan="3">Relaxation</th>
<th>$\gamma$</th>
<th>$\tau$</th>
<th>$\tau-\gamma$</th>
</tr>
<tr>
<th></th>
<th></th>
<th></th>
<th>$d_{12}$</th>
<th>$d_{23}$</th>
<th>$d_{34}$</th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Ac</td>
<td>fcc<br>5.66</td>
<td>(100)</td>
<td>-4.66</td>
<td>0.14</td>
<td>1.46</td>
<td>0.62<br>$0.73^{T1}$</td>
<td>0.52</td>
<td>-0.10</td>
</tr>
<tr>
<td></td>
<td></td>
<td>(111)</td>
<td>-4.28</td>
<td>1.94</td>
<td>0.17</td>
<td>0.60,<br>$0.87^{T1}$, $0.82^{T2}$</td>
<td>0.45</td>
<td>-0.15</td>
</tr>
<tr>
<td>Th</td>
<td>fcc<br>5.05</td>
<td>(100)</td>
<td>-2.74</td>
<td>1.72</td>
<td>-0.38</td>
<td>1.15<br>$1.47^{T1}$</td>
<td>1.61</td>
<td>0.46</td>
</tr>
<tr>
<td></td>
<td></td>
<td>(111)</td>
<td>-2.65</td>
<td>-0.71</td>
<td>-0.73</td>
<td>1.05<br>$1.48^{T1}$, $1.37^{T2}$<br>$1.50^{E1}$</td>
<td>0.90</td>
<td>-0.15</td>
</tr>
<tr>
<td>Pa</td>
<td>bct<br>3.93 (0.81)</td>
<td>(100)</td>
<td>-8.83</td>
<td>-1.70</td>
<td>2.23</td>
<td>1.70<br>$2.58^{T1}$</td>
<td>1.49</td>
<td>-0.21</td>
</tr>
<tr>
<td></td>
<td></td>
<td>(110)</td>
<td>-2.33</td>
<td>-0.01</td>
<td>0.94</td>
<td>1.39<br>$2.90^{T1}$, $2.33^{T2,*}$</td>
<td>1.91</td>
<td>0.52</td>
</tr>
</tbody>
</table>

$^*$ calculated as fcc structure, for (111) plane
$^{T1}$ FCD-LMTO, GGA [4]
$^{T2}$ FCD-LMTO, LDA [48]
$^{E1}$ extrapolation from surface tension measurement [5]

![](./images/813051809101774850_2.jpg)

Figure 1. Theoretical surface energies of thermodynamically stable facets of low temperature crystallographic structures for simple metals. For comparison, the previous FCD-LMTO calculations [4] (dashed lines) are shown together, and the range of other theoretical and experimental data are also displayed on the left and right side of each surface energy plot, respectively. All previous data and the present calculation results demonstrate that the surface energy decreases as the atomic number increases, in each group of the periodic table.

![](./images/813051809101774850_3.jpg)

Figure 2. Theoretical surface stresses of thermodynamically stable facets of low temperature crystallographic structures for simple metals. For comparison, the range of previously reported theoretical data are shown together, if available. The trend of the present calculation results are somewhat scattered, but apparently have minimum values in the middle of the alkali and the alkali-earth group in the periodic table.

![](./images/813051809101774850_4.jpg)

Figure 3. Theoretical surface energies of thermodynamically stable facets of low temperature crystallographic structures for the 3d (a), 4d (b), and 5d (c) transition metals, with surface energies from previous FCD-LMTO calculations shown for comparison. In addition, the ranges of the reported data from other theoretical and experimental approaches are marked on the left and right side of every surface energy plot, respectively. The surface energies vary approximately parabolically as a function of the d-electron occupation.

![](./images/813051809101774850_5.jpg)

Figure 4. Theoretical surface stresses of thermodynamically stable facets of low temperature crystallographic structures for the transition metals. For comparison, the range of previously reported theoretical and experimental data are shown together, on the left and right side of each stress plot, respectively. The 4d and 5d curves are approximately parabolic-shaped with a shallow dip, while the curve of the 3d metals has a pronounced minimum. Moreover, Cr and Mn have negative values of the surface stress, which means that the (100) surfaces of Cr and Mn are under slight compression.

Graphical Abstract

![](./images/813051809101774850_6.jpg)
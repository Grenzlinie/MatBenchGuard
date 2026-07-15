Journal Pre-proofs

The evolution of configuration and final state of graphene on rough iron surface

Xin He, Qingshun Bai, Rongqi Shen, Feihu Zhang, Yongbo Guo

<table>
  <tr>
    <td>PII:</td>
    <td>S0169-4332(20)31841-9</td>
  </tr>
  <tr>
    <td>DOI:</td>
    <td>https://doi.org/10.1016/j.apsusc.2020.147084</td>
  </tr>
  <tr>
    <td>Reference:</td>
    <td>APSUSC 147084</td>
  </tr>
  <tr>
    <td>To appear in:</td>
    <td>Applied Surface Science</td>
  </tr>
  <tr>
    <td>Received Date:</td>
    <td>15 March 2020</td>
  </tr>
  <tr>
    <td>Revised Date:</td>
    <td>20 June 2020</td>
  </tr>
  <tr>
    <td>Accepted Date:</td>
    <td>24 June 2020</td>
  </tr>
</table>

![](./images/812590912956792833_1.jpg)

Please cite this article as: X. He, Q. Bai, R. Shen, F. Zhang, Y. Guo, The evolution of configuration and final state of graphene on rough iron surface, Applied Surface Science (2020), doi: https://doi.org/10.1016/j.apsusc.2020.147084

This is a PDF file of an article that has undergone enhancements after acceptance, such as the addition of a cover page and metadata, and formatting for readability, but it is not yet the definitive version of record. This version will undergo additional copyediting, typesetting and review before it is published in its final form, but we are providing this version to give early visibility of the article. Please note that, during the production process, errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

© 2020 Published by Elsevier B.V.

# The evolution of configuration and final state of graphene on rough iron surface

Xin He*, Qingshun Bai, Rongqi Shen, Feihu Zhang and Yongbo Guo

School of Mechanical and Electrical Engineering, Harbin Institute of Technology, Harbin 150001

## ARTICLE INFO
**Keywords:**
graphene
iron
morphology defects evolution
strain state
random rough surface

## ABSTRACT
Molecular dynamics simulations are performed to investigate the evolution of configuration and morphology defects, the final strain and strain induced energy state of graphene on rough iron substrate. A series of randomly rough surfaces are modeled to simulate the real iron surface for the first time. The results show that the formation of morphology defects in graphene are mainly caused by the rapid normal displacement and the following shrinking along lateral di- rections that are both induced by the strong adhesion between graphene and iron. Fortunately, this strong adhesion cannot lead to global strain in whole graphene layers, i.e., the C-C strain are almost localized around the peaks of the asperities. Thus, the deformation energy (~20 meV/C atom) is mainly induced by bond angle bends and dihedral rotations rather than the expansion or compression of bond length. Through statistical analysis, we further find that the strain and deformation energy are linearly dependent on the substrate roughness. Our findings provide in- sight into tuning the morphology of graphene and the substrate designing of graphene-based devices. As the photoelectric performance of graphene is largely influenced by strain, our study also provides a guiding direction for evaluating the performance of graphene devices.

## 1. Introduction
Graphene/iron system possesses a great potential for applications in the following fields: graphene-based magnetic and spintronic devices[1, 2], surface passivation of iron[3], lubricating of iron-based metals[4] and growing graphene on iron substrate[5]. Graphene's two-dimensional (2D) nature lead to a excellent flexibility, thus the interface be- tween graphene and substrate can determine its extrinsic morphology[6, 7] which can in turn influence its electronic properties[8], lubrication performance[9], interfacial thermal resistance[10] and electrical contact resistance[11]. Un- derstanding graphene's state on solid substrate can, therefore, help to improve or even tune the properties of graphene devices[12, 13]

In order to study the rough contact of graphene, researchers have developed many types of substrates, such as one- dimensional (1D) grooves[13, 14, 15, 16, 17, 18, 19, 20, 21], two-dimensional patterned surface with sinusoidal[22], herringbone and checkerboard [23] corrugations, hemispherical surface[24], steps[25], nanopillars[26] and nano- particles[27], to model the microstructure in a real surface. Both the experimental[16, 28, 29] and theoretical results[14,23] show that the morphology of graphene on a rough surface have three states: i) fully-conformal, i.e., graphene com- pletely covers substrate surface; ii) partially-conformal, i.e., some part of graphene contacts with substrate surface intimately while other part remains suspended; iii) non-conformal, i.e., graphene remains flat and suspended on the

*Corresponding author: Dr. Xin He, E-mail: x.he@hit.edu.cn
ORCID(s): 0000-0002-8903-2046 (X. He)

top of the substrate surface. And several theoretical models have been formulated to investigate the factors that can influence the final states of graphene. Most of these models are based on the continuum mechanics and energy min- imization method that the total energy of the graphene/substrate system is minimized to obtain the final morphology of graphene[13, 14, 15, 17, 19, 20, 21, 23, 30, 31]

According to these theoretical models, it has been found that the adhesion energy between graphene and sub- strate, the thickness or bending stiffness[6, 32, 33] as well as the in-plane strain of graphene[15, 23, 25, 34, 30], the roughness[21] and mechanical properties of substrate[6, 15] can all influence graphene's final morphology. But on the whole, the final morphology results from the competition between two energy terms: the adhesion energy between graphene and substrate, and the strain energy stored in graphene and substrate[19, 24, 28]. Although the interface friction between graphene and substrate is usually not considered in most analytical models, it can, in fact, signifi- cantly reduce the conformability of graphene[19, 35]. Thus, a tilted smaller graphene sheet is more prone to conform to substrate because of the reduced interface friction[35]. Zhang *et al.*[15] predicate an interesting phenomenon of the sudden morphological transition of graphene from fully-conformal to non-conformal that is called "snap-through" tran- sition. They further suggest that this transition depends on the graphene-substrate adhesion, the number of graphene layers as well as the stiffness of substrate. This phenomenon is further demonstrated through experimental[16, 28] and theoretical[14, 23] researches. Xiong *et al.* [18, 36] further studied the elastic substrate with power-law grading modulus and found that the graded parameter $\alpha$ is the dominant factor to control the morphology and snap-through transition.

Regardless of the details of these theoretical models, an analytical solution can always be obtained, that is, graphene's final morphology can be predicated. However, through the exquisite AFM scanning of a graphene/silica system, Geringer *et al.*[12] hold that even the tiny details of the transferring process can have large impacts on the physical properties of graphene which indicates that the final state of a transferred graphene is not only depend on the certainty factors that have been considered in previous continuum models but also depend on some unpredictable factors such as the complicated deformation history of graphene, the randomness of the asperities distribution and the thermal fluctuation. Therefore, the morphology defects that have been widely observed in experiments[37, 38] cannot be ob- tained in the previous continuum models. Although molecular dynamics (MD) simulations, which is a valuable tool to provide information on the micromechanics and kinetics of the evolution of contact interface, has been employed to simulate the final configuration of graphene[13, 24, 35], analysis was seldom extended to its dynamic evolution. For the graphene/iron system, we have studied the interactions between graphene and Fe(110) plane[39], Wang *et al.*[40] studied the adhesion energy of graphene on single crystal iron with different crystal planes. Most other studies focus on electrical/magnetic/mechanical properties.

In this work, therefore, molecular dynamics simulations were performed to study the evolution of configuration and

final state of graphene on rough iron surface. Compared to previous studies, we concentrate on the dynamic adhesion process, the formation mechanism of morphology defects and the final strain state of graphene which are seldom studied. We firstly studied the adhesion and morphology evolution of graphene on the widely adopted 1D sinusoidal corrugations in Sec. 3.1, and then the substrates were extended to 2D sinusoidal surface in Sec. 3.2. Finally, A series of randomly rough iron substrates were modeled for the first time to simulate the actual contact interface, and the final strain state of graphene on these rough surfaces were quantified based on statistical methods in Sec. 3.3.

## 2. Simulation details
We performed molecular dynamics simulations of the adhesion of graphene on rough iron surface for the purpose of investigating the evolution of the configuration and final state of graphene. Three types of iron substrates were modeled as monocrystalline block of iron with different rough surface: one dimensional sinusoidal corrugations (Fig. 1a), two dimensional sinusoidal surface (Fig. 1b) and pseudo-random Gaussian rough surface (Fig. 1c and d).

1D sinusoidal corrugations was modeled as $Z_{\mathrm{s}}=A \sin (\frac{2 \pi}{\lambda} x)$, where $A$ is amplitude of the grooves and $\lambda$ is wavelength. In 1D models, $A$ was fixed at 1.5 nm and $\lambda$ was swept in the range of 3 nm to 18 nm in increments of 3 nm. The width (along $y$ direction) of the substrate was fixed at 22 nm and the length of the graphene layers (range from 46.5 nm to 140 nm ) was long enough to cover no less than 7 corresponding sinusoidal grooves. 2D sinusoidal surface was given by $Z_{\mathrm{s}}(x, y)=A \sin (\frac{2 \pi}{\lambda} x) \sin (\frac{2 \pi}{\lambda} y)$. The amplitude $A$ and wavelength $\lambda$ were fixed at 1.5 nm and 15 nm, respectively. The lateral dimensions of the 2D substrate is about 105 nm × 105 nm and the size of the graphene sheet is 95 nm × 95 nm.

For randomly rough surface, the most important parameters to influence the final topography of a real surface are the root mean square height $S_{\mathrm{q}}$ and the nominal asperities distance $d^{\text {asp }}[41,42]$. In this work, 6 rough substrates with different $S_{\mathrm{q}}$ (range from $2 \mathring{A}$ to $7 \mathring{A}$ in increment of $1 \mathring{A}$) have been built to investigate the adhesion of graphene on iron. In order to describe the micro-structure of rough surface as realistic as possible, the target rough surface was resolved into three sub-surface. To model these sub-surfaces, the simulation box was divided into $N^{x} \times N^{y}$ 2D-matrix unit cells. The cell vertices constitute the control points of the sub-surface and are assigned a random height value (z direction) such that the total distribution follows Gaussian distribution. In such a way, one can model different surface by varying the size of the unit cell (i. e., $d^{\text {asp}}$) and root mean square height $S_{\mathrm{q}}$. Therefore, the final target surface can be formulated as:

$$
\left\{
\begin{aligned}
&S(S_{\mathrm{q}}, d^{\mathrm{asp}})=\sum_{i=1}^{3} S_{i}(\sqrt{k_{i}} S_{\mathrm{q}}, d_{i}^{\mathrm{asp}}) \\
&S_{i}(\sqrt{k_{i}} S_{\mathrm{q}}, d_{i}^{\mathrm{asp}}) \sim N_{i}(0, k_{i} S_{\mathrm{q}}^{2})
\end{aligned}
\right. \tag{1}
$$

![](./images/812590912956792833_2.jpg)

Figure 1: Schematic representations of the initial state of the 1D sinusoidal corrugations (a), 2D sinusoidal surface (b), top view of a pseudo-random Gaussian rough surface with a root mean square height of 6 Å (c), and perspective of randomly rough iron substrate (d). Surface in (b), (c) and (d) are colored according to the height amplitude along z direction. As the height amplitude of the randomly rough surface is variable in different substrate, scale bar in (c) and (d) is not presented here, the specific values can be found in Fig. 8b.

where $S(S_{\mathrm{q}}, d^{\mathrm{asp}})$ is the target surface and $S_{i}(\sqrt{k_{i}}S_{\mathrm{q}}, d_{i}^{\mathrm{asp}})$ ($i$ =1, 2, 3) is the $i$-th sub-surface. The three weighting factors $k_{i}$ ($i$ =1, 2, 3) are 0.6, 0.3 and 0.1, respectively. We assigned $d_{1}^{\mathrm{asp}} = 50$ Å to model the major asperities (Fig. S1a) and assigned $d_{2}^{\mathrm{asp}} = 25$ Å, $d_{3}^{\mathrm{asp}} = 12.5$ Å to model the detailed rough structure (Fig. S1b and c). The z coordinates of each sub-surface obey the Normal distribution of $N_{i}(0, k_{i}S_{\mathrm{q}}^{2})$. In order to account for periodic boundary conditions, the resulting 2D-matrix of z values of each sub-surface was then padded at each boundary with 2, 4, 8 rows (or columns) from the opposite side for sub-surface $S_{1}$, $S_{2}$ and $S_{3}$, respectively. And then these three sub-surfaces can be merged together to generate the final randomly rough surface. This final rough surface can be further used as a template, $S_{\mathrm{tp}}$, to generate the other 5 surfaces by scaling up the z coordinates of $S_{\mathrm{tp}}$ proportionally. In this case, the lateral shape of these surface are similar to each other. The lateral dimensions of iron substrate was 50 nm × 50 nm and the size of the graphene sheet was 48.5 nm× 48.5 nm. These rough substrates are in good agreement with the actual ultra-smooth surface. More details about the generation of randomly rough surface are attached in Supplementary Material S1. In following, the root mean square height of iron surface and graphehen are denoted as $S_{\mathrm{q}}^{\mathrm{Fe}}$ and $S_{\mathrm{q}}^{\mathrm{Gr}}$, respectively.

In all the simulations, $x$-, $y$- and $z$-axis were aligned along the [00$\overline{1}$] [$\overline{1}$10], and [110] crystal direction of bcc iron, respectively. The zigzag direction of graphene was parallel to $x$-axis. Periodic boundary conditions were applied along lateral directions ($x$- and $y$-axis). Monolayer (1L) or ABA stalked multi-layer graphene was initially free suspended upon the iron substrate and then relaxed long enough until the system reached an equilibrium state. After that graphene layers were displaced to iron substrate until them interact with each other and then graphene layers can be attracted to

iron by adhesion force. A Finnis-Sinclair[43] potential was used for the Fe-Fe interactions and AIREBO[44] potential was used to simulate the interactions within graphene atoms. The interactions between graphene and iron substrate were modeled by Lenard-Jones potential with the parameters of $\epsilon=0.043\,\text{eV}$ and $\sigma=2.221\,\text{\AA}$, which has been validated in our previous study[39]. Nosé-Hoover thermostat was applied to control the temperature of the system with a time step of 1 fs. The simulations were performed with the LAMMPS[45] code. The atomic configurations are displayed using AtomEye[46] and OVITO[47].

## 3. Results and discussion

### 3.1. Adhesion of graphene on 1D sinusoidally corrugated substrates

As shown in Fig. 2(a), when the wavelength is 3 nm, part of the 1L graphene completely conforms to iron surface that indicates the adhesion strength between graphene and iron is enough to bend 1L graphene. However, it can also be found that the other part is still suspended on the top of the substrate that is called non-conformal. The two distinct states demonstrate that the bending stiffness of graphene is not the dominant factor to control 1L grapenhe's morphology. In fact, graphene membrane experienced a severe interface sliding before conforming to rough surface[35]. A great amount of energy was dissipated during this sliding to overcome the strong chemical interactions between graphene and iron. Thus the equilibrium morphology of graphene is determined by the competition among the bending stiffness of graphene, the adhesion strength and interface friction between graphene and iron. In consideration of the ultra-low bending stiffness of graphene[48], the interlayer friction can be the major factor to dominate its morphology, especially for 1L graphene. Sliding coefficient $\eta=(L_\lambda-\lambda)/\lambda$ was defined to evaluate the intensity of interface friction, where $L_\lambda$ is the arc length of one cycle of the sine curve. Meanwhile, adhesion energy, $E_{\text{ad}}$, can be applied to predicate the conformal state because it is approximately proportional to contact area. It was defined as $E_{\text{ad}}=E_{\text{total}}-E_{\text{Fe}}-E_{\text{Gr}}$, where $E_{\text{total}}$, $E_{\text{Fe}}$ and $E_{\text{Gr}}$ are total energy of the whole system, energy of iron substrate and energy of graphene layers, respectively. As shown in Fig. 3, the decrease of $\eta$ (from 1.30 at $\lambda=3\,\text{nm}$ to 0.14 at $\lambda=6\,\text{nm}$) results in an increment of $E_{\text{ad}}$ by more than 60% (from $0.40\,\text{J/m}^2$ to $0.65\,\text{J/m}^2$ ) due to the transition of contact state from partly conformal (Fig. 2a) to fully-conformal (Fig. 2b). And then followed a stable stage in which graphene is always fully-conformal, Fig. 2(b), (c) and (d). We attribute the subsequent reduction of $E_{\text{ad}}$ to the defects of fold (Fig. 2e) and wrinkles (Fig. 2f).

Fig. 2g and m show the configurations of bilayer (2L) and trilayer (3L) graphene when $\lambda=3\,\text{nm}$. Unlike 1L graphene, they are both completely non-conformal owing to the dramatic increase of the bending stiffness which is proportional to the cube of the membrane thickness[32]. In this case, bending stiffness develop into a primary factor to graphene's morphology. As interlayer shear modulus of multi-layer graphene is three orders of magnitude lower than in-plane Young's modulus, the bending stiffness should be dominated by interlayer shear[49]. In light of this

![](./images/812590912956792833_3.jpg)

Figure 2: Side views of the stable configuration of graphene on top of sinusoidal iron grooves with different wavelength. The 1st, 2nd and 3rd column are monolayer, bilayer and trilayer graphene at 300 K, respectively. The 4th column is trilayer graphene at 10 K. (e) and (j) show the morphology defect of fold. (f) and (l) show the defect of wrinkle. (r) shows the defect of sublayer wrinkles. Most of the multi-layer graphene, (h-l) and (n-r), experienced interlayer sliding. For the situation of 10 K (s-x), by contrast, graphene layers are always aligned. Only part of the representative snapshots are presented here due to space limitation, the whole snapshots can be found in Supplementary Materials S2. The bottom cyan atoms are iron atoms, the black, red and green atoms are graphene atoms.

![](./images/812590912956792833_4.jpg)

Figure 3: Adhesion energy $E_{\text{ad}}$ and sliding coefficient $\eta$ as a function of the wavelength $\lambda$. The insert shows the relationship between adhesion energy and sliding coefficient. Note that 'partly conformal' means part of the graphene sheet is fully-conformal but other part is non-conformal that is the case shown in Fig. 2(a).

argument, the morphology of multilayer graphene is mainly determined by interlayer sliding which can facilitate the bending deformation. Therefore, both the fully-conformal and partially-conformal multilayer graphene experienced a certain degree of interlayer sliding in the case of $T=300$ K, see in Fig. 2 (h-l and m-r).

In consideration of the mentioned relationship among the shear strength, bending stiffness and conformal state, we proposed a question that: can the morphology of graphene be tuned by varying the interlayer shear strength which is depend on environment temperature? Thus we performed MD simulations of the interlayer friction of a four-layer graphene system. The simulation details can be found in Supplementary Material S3. As shown in Fig. S8, the

friction force decreases about 98% when environment temperature goes from 10 K to 300 K. This dependence is in good agreement with experimental results[50]. And then we performed simulations of 3L graphene on same iron surfaces at 10 K. It can be found that the bent (Fig. 2m) and fully-conformal (Fig. 2n) 3L graphene at 300K turn into free standing (Fig. 2s) and partially-conformal (Fig. 2t) at 10 K, respectively. When $\lambda > 6$nm, graphene are fully-conformal under two temperature, while its morphology is defectless when $T$=10 K.

The morphology defects have been mentioned above repeatedly, we now turn our attention to the formation of these defects. We found four types of defects on 1D sinusoidally corrugated surface, the fold in Fig. 2(e and j), the wrinkles in Fig. 2(f and l), the sublayer wrinkles in Fig. 2(r) and the interlayer sliding that can be observed in most multilayer graphene. These defects have not been observed in previous continuum mechanics models but have been observed in experiments[37, 38]. We attribute the formation of these defects to the dynamic evolution of the morphology. Fig. 4 presents the evolution history of the configuration of 3L graphene. The free-standing graphene sheet, Fig. 4(a), has intrinsic three-dimensional structure of ripples due to the instability of two-dimensional crystal. Therefore, the graphene atoms nearest to iron substrate can be attracted firstly and subjected to a rapid normal displacement which can subsequently result in a moving waves, Fig. 4(b). These waves move forward with a high velocity of about 1000 m/s, Fig. 4(c). The fluctuation of graphene in normal direction (along z-axis) reduced its lateral dimensions, therefore it shrunk inward with a speed of about 200 m/s which can further increase the amplitude of the waves (Fig. 4c). With the evolution of the morphology, several graphene domains randomly contacted with substrate and were anchored on it subsequently. The waves were restrained between these anchor sites and gradually evolved into wrinkles, Fig. 4d. These wrinkles were initially large and not stable, and oscillated left and right due to thermal fluctuations, Fig. 4(e-g). Since the adhesion strength between graphene and iron is much stronger than that between graphene layers, the bottom graphene collapsed downward and peeled from the upper layers and then gradually slid along interface (Fig. 4d-h). Consequently, Consequently, sublayer wrinkles instead of overall wrinkles usually forms in multi-layer graphene. For few layers graphene, it may be folded due to rapid disturbances and low bending stiffness. Therefore, all the defects are related to the formation and evolution of the waves. Since the moving waves is hardly to form under low temperature owing to the increased bending stiffness, defects are completely inhibited. The formation of these morphology defects indicates that it is very difficult to obtain a completely smooth graphene on iron substrate without artificial intervention.

Interestingly, We found that the defects are more prone to form on relatively flat surfaces which is a bit different from empirical understanding. We attribute this phenomenon to three aspects. First, the waves are significantly weakened by the decrease of the adhesion energy between graphene and rough iron. Second, the nucleation rate of the anchor sites is faster in rough surface which can significantly inhibit the formation of the moving waves. Finally, the concave/convex of the rough surface can offset the normal fluctuation of graphene layers. Thus no defects can be found in the rough surface with large sliding coefficient $\eta$, shown in Fig. 2(b-d). We also note that the length of graphene can also

influence the formation of defects.

![](./images/812590912956792833_5.jpg)

Figure 4: Evolving of the configuration of 3L graphene on 1D sinusoidal iron substrates. The wavelength of substrates is 18 nm. (e)-(h) just show part of the snapshots marked by black dotted line in (d). The bottom cyan atoms are iron atoms, the black, red and green atoms are graphene atoms.

### 3.2. Adhesion of graphene on 2D sinusoidally corrugated substrates

In previous section, we studied the adhesion of graphene on 1D sinusoidal corrugations which can be considered absolutely smooth in $y$ direction. But the absolutely smooth surface does not exist in actual engineering. Even the sub-nanometer roughness cannot be ignored compared with the thickness of graphene, $3.4\ \mathrm{\mathring{A}}$. Therefore, As described in Sec. 2, the substrates were extended to 2D sinusoidal corrugations.

As shown in Fig. 5, the adhesion process of graphene on 2D iron substrate was essentially the same as that on 1D sinusoidal grooves. Both of them go through three stages: initial adhesion, wave formation and propagation, wrinkles formation and relaxation. The difference is that in 1D case, all the waves are approximately parallel to each other, even if they are restrained by multiple anchor sites, they can relaxed easily through interlayer or interface sliding. Thus only a small number of defects can be formed. But in 2D conditions, multiple nonparallel waves were intertwined together (Fig. 5b) and thereafter evolved into intertwined wrinkles (Fig. 5c). Contrast to 1D grooves, interface and interlayer sliding were mostly suppressed due to the bi-directional deformation of graphene. The wrinkles, therefore, are difficult to be relaxed and more larger defects can be preserved, Fig. 5d. The aligned 2L (Fig. S9) and 3L (Fig. S10) graphene are also the clearest illustrations of the suppression of interlayer sliding. It should also be noted that the 2L and 3L graphene in Fig. S9 and Fig. S10 are defectless compared to 1L graphene in Fig. 5. It is mainly the result of the suppression of waves which caused by increased bending stiffness rather than the interface sliding. In order to

![](./images/812590912956792833_6.jpg)

Figure 5: Evolution of the configuration of 1L graphene on 2D corrugated iron substrate with a wavelength of 15 nm. (a) $t = 40$ ps, the first wave formed due to the rapid displacement of the graphene atoms. (b) $t = 80$ ps, two sets of moving waves intertwined together. (c) $t = 120$ ps, intertwined wrinkles evolved from the intertwined waves in (b). (d) $t = 400$ ps, the final configuration. The black dash lines show the dynamic evolution of the waves and wrinkles. The white arrows highlight the local warps and the pink arrows indicate the moving directions of the waves. The red dash cycle marks the region shown in Fig.6(a).

![](./images/812590912956792833_7.jpg)

Figure 6: Local configuration of 1L (a), 2L (b) and 3L (c) graphene on 2D sinusoidal iron surface that taken from the red dash cycle marked area in Fig. 5(d), Fig. S9 and Fig. S10, respectively. Local warps are located at the side of the concave region. The top scatter and pink lines are the corresponding cross-sectional view. Atoms are colored by the height of graphene ($z$ direction). The concave region of graphene in (a) and (c) appear O shape and in (b) it shows a C-like shape.

validate this mechanism, we raised the temperature of these simulations, however, interlayer or interface sliding cannot be observed.

Fig. 6 shows the local close-up views of 1L-3L graphene. There are mainly two appearance of the concave region of graphene: O shaped in Fig. 6(a, c) and C shaped in Fig. 6b, all of which are partially-conformal. Compared with the fully-conformal state in 1D case ($\lambda = 15$ nm), we attribute this transition to the different deformation mechanism of graphene. As presented in Sec. 3.1, graphene can achieve high compliance on 1D corrugations just through bending itself. Otherwise, graphene, on 2D surface, need to be stretched or compressed to conform substrate surface which

is much more difficult than bent. Therefore graphene was warped around the side of the concave regions. With the increase of the bending stiffness, local warping becomes more difficult and resulting in low compliance. As shown in Fig. 6, The depth of the concave region in graphene (24.5 Å, 23.2 Å, 20.8 Å for 1L, 2L, 3L respectively) is much shallower than that in iron substrate, 30 Å.

Meanwhile, we also found that the shape and position of the initially attracted graphene can significantly influence the final morphology. Large moving waves are prone to be formed in sharper graphene, i.e., high aspect ratio (e.g. the corners of rectangular graphene in this work). In contrast, waves are scarcely formed if the curvature of the graphene edge is small enough (the midpoint of graphene edge or the inner area of graphene in this work). We cannot tell beforehand the evolution of the morphology, because it not only depend on the initial configuration controlled by thermal vibration but also depend on the randomly rough substrate and the complicated deformation history. In consideration of this argument, we suggest that circle graphene may can help to improve the smoothness of transferred graphene.

### 3.3. State of graphene on iron with randomly rough surface
Until now, the configuration evolution and defects formation of graphene on iron substrate with regularly patterned surface have been studied. These models are appropriate for investigating the details of the adhesion, but, as pointed out in Sec. 3.2, it cannot fully reveal the actual state of graphene due to the randomness of rough surfaces. Thus, we further turn our attention to the randomly rough iron substrate aiming for quantifying the state of graphene based on statistical methods. To minimize the influence of thermal fluctuation, if not specified, all the analysis performed in this section were on quasistatic configurations which were obtained by further relaxing the system using the conjugate gradient method. This relaxation does not alter the state of graphene qualitatively, but it makes the statistical results more reliable and stable.

Fig. 7a and b show the surface morphology of substrate and monolayer graphene in the case of $S_{\mathrm{q}}^{\mathrm{Fe}}=7$ Å. As expected, graphene cannot fully reproduce the morphology of iron surface, especially the detailed structure. It was divided into several relatively smoother regions by wrinkles that formed around the asperities of iron surface, Fig. 7b. Fig. 7c shows the histograms of the heights over graphene and iron surface both of which obey Normal distribution. As shown in Fig. 8a, the standard deviations of the height variations, which is actually the root mean square height of the surface, are 6.03 Å and 7.06 Å for graphene and iron substrate surface, respectively. That is, graphene sheet is approximately 17% smoother than iron surface. The maximum height[41] of graphene, $S_{\mathrm{z}}^{\mathrm{Gr}}$, 36.7 Å, was reduced by about 30% compared to that of the iron surface of 53.2 Å, fig. 8b. The adhesion energy of 1L graphene on Fe(110) is about 150 meV/C atom[39]. Therefore $E_{\mathrm{ad}}$, 104 meV/C atom, reduced by about 31%, fig. 8c. The difference of the roughness between graphene and substrate surface decreased gradually with the reduction of $S_{\mathrm{q}}^{\mathrm{Fe}}$. When $S_{\mathrm{q}}^{\mathrm{Fe}}$

lowered to $2$ Å, the roughness of graphene ($S_{\mathrm{q}}^{\mathrm{Gr}}$ and $S_{\mathrm{z}}^{\mathrm{Gr}}$) and iron substrate ($S_{\mathrm{z}}^{\mathrm{Fe}}$) are $2.09$ Å, $14.3$ Å and $16.0$ Å, respectively. Meanwhile, adhesion energy $E_{\mathrm{ad}}$ increased to $148$ meV/C atom. That is, the relative errors in $S_{\mathrm{q}}$, $S_{\mathrm{z}}$ and $E_{\mathrm{ad}}$ are lowered to $2.3\%$, $10.6\%$ and $1.3\%$, respectively. The experimentally measured roughness of graphene on silica is approximately $60\%$ smoother than that of the silica surface[29] ($S_{\mathrm{q}}^{\mathrm{silica}} = 3.1$ Å). In present work, when $S_{\mathrm{q}}^{\mathrm{Fe}} = 3$ Å, graphene is only $4\%$ smoother than iron surface. We attribute the improved conformability to the strong adhesion between graphene and iron that is much greater than that between graphene and graphene and silica, $16$ meV/C atom[29].

![](./images/812590912956792833_8.jpg)

Figure 7: Morphology of the graphene/Fe system when $S_{\mathrm{q}}^{\mathrm{Fe}} = 7$ Å. (a) morphology of iron substrate. (b) morphology of 1L graphene, white dash lines show the intertwined local wrinkles. (c) height distribution of the numeric surface (blue cycle) shown in Fig. S2b, iron surface (red diamond) shown in (a) and graphene surface (purple square) shown in (b). The histograms are well-described by Gaussian distributions. Atoms in (a) and (b) are colored according to the height amplitude along $z$ direction.

We further analyzed the relationship between the contact state of graphene and the roughness of iron. When $S_{\mathrm{q}}^{\mathrm{Fe}} \leqslant 6$ Å, $S_{\mathrm{q}}^{\mathrm{Gr}}$, $S_{\mathrm{z}}^{\mathrm{Gr}}$ and $E_{\mathrm{ad}}$ are linearly depend on $S_{\mathrm{q}}^{\mathrm{Fe}}$ (see Fig. 8). This dependence may be applied to estimate the adhesion strength in actual engineering. But unfortunately, this linear dependence can no longer hold true when $S_{\mathrm{q}}^{\mathrm{Fe}}$ increased to $7$ Å. The increased difference between $S_{\mathrm{z}}^{\mathrm{Gr}}$ and $S_{\mathrm{z}}^{\mathrm{Fe}}$ (Fig. 8b) indicates that more graphene atoms are not contact with iron surface when $S_{\mathrm{q}}^{\mathrm{Fe}} > 6$ Å. The smoother domain of graphene in Fig. 7b and the rapid drop of the adhesion energy in Fig. 8c can be the evidence of the reduction of contact area.

As mentioned above, the strong adhesion between graphene and iron can, on the one hand, improve the compliance of graphene that may be beneficial for interfacial thermal resistance and electrical contact resistance of graphene-based devices. But, on the other hand, it can result in a higher strain in graphene which can consequently influence the electronic transport properties. Therefore, we continue to examine graphene's strain state. We plotted the histograms of the atomic strain in Fig. 9. The results unambiguously show that the distributions of atomic strain in graphene do not obey normal distribution and the Kurtosis value (Fig. S16) of these distributions are much greater than 3 (A Gaussian distribution has a Kurtosis value of 3). It pose a question that why can't the atomistic strain in graphene, like the morphology, follow Gaussian distribution. To explain this phenomenon, we first performed analysis of the spatial distribution of the strain of graphene atoms and the results are presented in Supplementary Material S7. It is obvious that the highly strained atoms mainly located around the peaks of the substrate, especially for rougher substrate, while most of other atoms are approximately in near-equilibrium state. Thus we can hold that most of the deformation in graphene is achieved through bond angle bends and dihedral rotations rather than the expansion or compression of bond length. We further analyzed the deformation energy of graphene to help understanding this

![](./images/812590912956792833_9.jpg)

Figure 8: Contact state of graphene on rough iron substrate. Variation of root mean square height of graphene (a), maximum height of graphene (blue cycle) and iron surface (red square) (b), adhesion energy between iron substrate and graphene (c) and deformation energy of graphene (d). Deformation energy, $E_{\text{deform}}^{\text{Gr}}$, is the variation of the total energy of graphene during the adhesion process, $E_{\text{deform}}^{\text{Gr}} = E_{\text{aftdef}}^{\text{Gr}} - E_{\text{free}}^{\text{Gr}}$, where $E_{\text{aftdef}}^{\text{Gr}}$ is the energy of deformed graphene and $E_{\text{free}}^{\text{Gr}}$ is the energy of free suspended graphene.

phenomenon. As shown in the insert in Fig. 9, the average strain of all the C-C bonds, $\epsilon_{\text{ave}}$, is not more than 0.6% which is considered to be trivial here. The high Kurtosis value indicates that the standard deviation mainly stems from the high strain. Therefore we further investigated 'mean top 10% strain', $\epsilon_{\text{mean}}^{0.1}$, that was defined as the average of the top 10% of the atomic strain in graphene. When $S_{\text{q}}^{\text{Fe}}$ ranged from 2 Å to 7 Å, $\epsilon_{\text{mean}}^{0.1}$, increased from 0.95% to 1.87%. According Ref. [29], the corresponding maximum energy density stored in graphene can be estimated in the range of $0.9 \sim 3.5$ meV/Å² (2.3 ~ 8.9 meV/C atom) which is much lower than the total deformation energy shown in Fig. 8d. We suggest that it is because, as mentioned above, the total deformation energy is the combined effects of bond length expansion/compression, bond angle bends and dihedral rotations. The lateral two items contribute the most to deformation energy when graphene is low strained. Therefore, the energy density that is calculated from tensile/compressive strain may be seriously underestimated, especially on ultra-smooth surfaces in which case graphene is just slightly strained. For rougher substrate, the tensile/compressive strain induced energy can account for a large proportion of the total deformation energy.

It should be noted that the reason we choose 10% as the threshold are as follows: i) low enough to demonstrate

![](./images/812590912956792833_10.jpg)

Figure 9: Strain histograms of graphene sheet on iron substrates with different $S_{\mathrm{q}}$. Negative values are compressive strain and positive values are tensile strain. The solid lines are the results of Normal distribution fitting of the corresponding data. The insert shows the dependence of mean top 10% strain (blue circle), $\epsilon_{\text{mean}}^{0.1}$, and average strain (red square), $\epsilon_{\text{ave}}$, on root mean square height of iron substrate, $S_{\mathrm{q}}^{\mathrm{Fe}}$. The error bars correspond to a standard deviation in these measurements. Note that the absolute value of the strain are used to calculate the maximum and average strain.

the effect of high strain; ii) high enough to reflect the overall strain state of graphene and meanwhile to eliminate the effect of the randomness of atomic strain. We also choose other values (from 5% to 30%) as threshold, it just change the value of $\epsilon_{\text{mean}}^{0.1}$ but keep the varying trend unchanged.

Moreover, it is easy to find the linear dependence of $\epsilon_{\text{ave}}$ and $\epsilon_{\text{mean}}^{0.1}$ on $S_{\mathrm{q}}^{\mathrm{Fe}}$ when $S_{\mathrm{q}}^{\mathrm{Fe}}$ is in the range of $2\ \mathring{\mathrm{A}} \sim 5$ $\mathring{\mathrm{A}}$. Same as the relationship shown in Fig. 8, these linear relationship can no longer holds true if $S_{\mathrm{q}}^{\mathrm{Fe}} > 5\ \mathring{\mathrm{A}}$. There must be some delicate connections among these variables. So we now concentrate on finding out the relationship. When $S_{\mathrm{q}}^{\mathrm{Fe}}$ goes up from $5\ \mathring{\mathrm{A}}$ to $6\ \mathring{\mathrm{A}}$, $S_{\mathrm{z}}^{\mathrm{Gr}}$ increases too, but $\epsilon_{\text{ave}}$ and $\epsilon_{\text{mean}}^{0.1}$ remain approximately constant. It further demonstrates that the deformation of Gr can only be realized through bond angle bends and dihedral rotations in this case. Therefore, the total deform energy increased, 8d. And when $S_{\mathrm{q}}^{\mathrm{Fe}}$ is in the range of 6-7 $\mathring{\mathrm{A}}$, the average strain remain almost unchanged but $\epsilon_{\text{mean}}^{0.1}$ increased by 8% which can result in an increment in total deformation energy. At the same time, the energy that result from bond angle bends and dihedral rotations decreased with the rapid decrease of $S_{\mathrm{z}}^{\mathrm{Gr}}$ that is manifested as the small smoother graphene patches in Fig. 7(b). Therefore with the combined effects of these two aspects, the total deformation energy remain approximately constant. Thus it can be concluded that $6\ \mathring{\mathrm{A}}$ may be a appropriate roughness which can balance the manufacturing cost and the quality of graphene coatings in actual engineering.

Another question then arises naturally: since the sum of deformation energy and adhesion energy is less than

the adhesion strength (see in Fig. S23), why can't graphene be further strained to conform to substrate? In fact, the adhesion force between graphene and iron can achieve its maximum value at a distance of $r=(26/7)^{1/6}\sigma=2.77$ $\text{\AA}$, and it decreases with $r^{13}$, i.e., a decrease of $1$ $\text{\AA}$ in distance can yield a reduction of $80\%$ in adhesion force. The high roughness (more than $10$ $\text{\AA}$ in $S_z$ ) makes graphene to be partially- or non-conformal and then the Fe-C distance exceeds the interaction range. We examined the maximum strain in graphene and found it can increase to $7\%$ when $S_{\mathrm{q}}^{\mathrm{Fe}}=7$ $\text{\AA}$, which can subsequently yield a strain energy of $48$ meV/C atom. Combined the adhesion energy of $104$ meV/C atom, it exactly matches the total adhesion strength of $150$ meV/C atom.

## 4. Conclusion

We have performed molecular dynamics simulations of the adhesion of graphene on rough iron substrate. For the first time, randomly rough surface are applied to model the realistic substrate, and the formation mechanism of morphology defects has been revealed. We find that the moving waves in graphene as well as the intertwining of these waves,which are both induced by the strong adhesion between graphene and iron, are the root causes of these defects. And the strong adhesion can further lead to a very local strain in graphene. Therefore, the deformation energy stored in graphene are mainly composed of bond angle bends and dihedral rotations rather than expansion or compression of bond length. Because the strain and deformation energy are both linearly depend on the roughness of substrate, a appropriate root mean square height of iron surface ($6$ $\text{\AA}$ in this work) can help to balance the manufacturing cost and the quality of graphene coatings. Our finds reveal the actual contact state between graphene and solid substrate at atomistic scale which can help to deepen the understanding of the configuration evolution and the final state of graphene. It provides insight into tuning the morphology of graphene and the substrate designing of graphene-based devices.

## Acknowledgment

This research was supported by Key projects of National Natural Science Foundation of China [grant number 51535003] and National Natural Science Foundation of China [grant number 51575138, 51775146].

## References

[1] M. Cattelan, G. W. Peng, E. Cavaliere, L. Artiglia, A. Barinov, L. T. Roling, M. Favaro, I. Píš, S. Nappini, E. Magnano, F. Bondino, L. Gavioli, S. Agnoli, M. Mavrikakis, G. Granozzi, The nature of the Fe-graphene interface at the nanometer level, Nanoscale 7 (2015) 2450-2460. doi:10.1039/C4NR04956J.

[2] M. Weser, E. N. Voloshina, K. Horn, Y. S. Dedkov, Electronic structure and magnetic properties of the graphene/Fe/Ni(111) intercalation-like system, Phys. Chem. Chem. Phys. 13 (16) (2011) 7534-7539. doi:10.1039/C1CP00014D.

[3] D. Marchetto, P. Restuccia, A. Ballestrazzi, M. Righi, A. Rota, S. Valeri, Surface passivation by graphene in the lubrication of iron: A comparison with bronze, Carbon 116 (2017) 375-380. doi:10.1016/j.carbon.2017.02.011.

[4] D. Berman, A. Erdemir, A. V. Sumant, Few layer graphene to reduce wear and friction on sliding steel surfaces, Carbon 54 (2013) 454-459. doi:10.1016/j.carbon.2012.11.061.

[5] N. A. Vinogradov, A. A. Zakharov, V. Kocevski, J. Rusz, K. A. Simonov, O. Eriksson, A. Mikkelsen, E. Lundgren, A. S. Vinogradov, N. Märtensson, A. B. Preobrajenski, Formation and structure of graphene waves on Fe(110), Physical Review Letters 109. doi:10.1103/ PhysRevLett.109.026101.

[6] U. Stöberl, U. Wurstbauer, W. Wegscheider, D. Weiss, J. Eroms, Morphology and flexibility of graphene and few-layer graphene on various substrates, Applied Physics Letters 93 (2008) 051906. doi:10.1063/1.2968310.

[7] E. Stolyarova, K. T. Rim, S. Ryu, J. Maultzsch, P. Kim, L. E. Brus, T. F. Heinz, M. S. Hybertsen, G. W. Flynn, High-resolution scanning tunneling microscopy imaging of mesoscopic graphene sheets on an insulating surface, Proceedings of the National Academy of Sciences 104 (2007) 9209-9212. doi:10.1073/pnas.0703337104.

[8] J.-H. Chen, C. Jang, S. Xiao, M. Ishigami, M. S. Fuhrer, Intrinsic and extrinsic performance limits of graphene devices on SiO2, Nature Nanotechnology 3 (2008) 206-209. doi:10.1038/nnano.2008.58.

[9] W. Zhao, F. Duan, Effect of Supporting Metal Substrates on the Tribological Properties of Monolayer Graphene, Tribol Lett 68 (2020) 1-14. doi:10.1007/s11249-020-1267-3.

[10] J. Zhang, Y. Wang, X. Wang, Rough contact is not always bad for interfacial energy coupling, Nanoscale 5 (2013) 11598-11603. doi:10.1039/C3NR03913G.

[11] F. Giubileo, A. Di Bartolomeo, The role of contact resistance in graphene field-effect devices, Progress in Surface Science 92 (2017) 143-175. doi:10.1016/j.progsurf.2017.05.002.

[12] V. Geringer, M. Liebmann, T. Echtermeyer, S. Runte, M. Schmidt, R. Rückamp, M. C. Lemme, M. Morgenstern, Intrinsic and extrinsic corrugation of monolayer graphene deposited on SiO2, Phys. Rev. Lett. 102 (2009) 076102. doi:10.1103/PhysRevLett.102.076102.

[13] T. Li, Extrinsic morphology of graphene, Modelling Simul. Mater. Sci. Eng. 19 (2011) 054005. doi:10.1088/0965-0393/19/5/054005.

[14] T. Li, Z. Zhang, Substrate-regulated morphology of graphene, J. Phys. D: Appl. Phys. 43 (2010) 075303. doi:10.1088/0022-3727/43/7/075303.

[15] Z. Zhang, T. Li, Determining graphene adhesion via substrate-regulated morphology of graphene, Journal of Applied Physics 110 (2011) 083526. doi:10.1063/1.3656720.

[16] S. Scharfenberg, N. Mansukhani, C. Chialvo, R. L. Weaver, N. Mason, Observation of a snap-through instability in graphene, Applied Physics Letters 100 (2) (2012) 021910. doi:10.1063/1.3676059.

[17] L. Wang, N. Lu, Conformability of a Thin Elastic Membrane Laminated on a Soft Substrate With Slightly Wavy Surface, J. Appl. Mech 83 (2016) 041007. doi:10.1115/1.4032466.

[18] L. Xiong, Y. Gao, The morphology of graphene on an elastic graded substrate, Physica E: Low-dimensional Systems and Nanostructures 63 (2014) 293-298. doi:10.1016/j.physe.2014.06.014.

[19] K. Zhang, M. Arroyo, Adhesion and friction control localized folding in supported graphene, Journal of Applied Physics 113 (2013) 193501. doi:10.1063/1.4804265.

[20] T. J. W. Wagner, D. Vella, The sensitivity of graphene "snap-through" to substrate geometry, Appl. Phys. Lett. 100 (2012) 233111. doi:10.1063/1.4724329.

[21] W. Gao, R. Huang, Effect of surface roughness on adhesion of graphene membranes, J. Phys. D: Appl. Phys. 44 (2011) 452001. doi:

10.1088/0022-3727/44/45/452001.

[22] N. G. Boddeti, R. Long, M. L. Dunn, Adhesion mechanics of graphene on textured substrates, International Journal of Solids and Structures 97 (2016) 56-74. doi:10.1016/j.ijsolstr.2016.07.043.

[23] T. Li, Z. Zhang, Snap-through snstability of graphene on substrates, Nanoscale Research Letters 5 (2009) 169. doi:10.1007/ s11671-009-9460-1.

[24] Y. Zhou, Y. Chen, B. Liu, S. Wang, Z. Yang, M. Hu, Mechanics of nanoscale wrinkling of graphene on a non-developable surface, Carbon 84 (2015) 263-271. doi:10.1016/j.carbon.2014.11.055.

[25] Y. He, W. Yu, G. Ouyang, Effect of stepped substrates on the interfacial adhesion properties of graphene membranes, Physical Chemistry Chemical Physics 16 (2014) 11390-11397. doi:10.1039/C4CP00633J.

[26] G. Li, C. Yilmaz, X. An, S. Somu, S. Kar, Y. Joon Jung, A. Busnaina, K.-T. Wan, Adhesion of graphene sheet on nano-patterned substrates with nano-pillar array, Journal of Applied Physics 113 (2013) 244303. doi:10.1063/1.4811718.

[27] S. Zhu, T. Li, Wrinkling Instability of Graphene on Substrate-Supported Nanoparticles, Journal of Applied Mechanics 81 (6) (2014) 061008. doi:10.1115/1.4026638.

[28] S. Scharfenberg, D. Z. Rocklin, C. Chialvo, R. L. Weaver, P. M. Goldbart, N. Mason, Probing the mechanical properties of graphene using a corrugated elastic substrate, Appl. Phys. Lett. 98 (9) (2011) 091908. doi:10.1063/1.3553228.

[29] M. Ishigami, J. H. Chen, W. G. Cullen, M. S. Fuhrer, E. D. Williams, Atomic structure of graphene on SiO2, Nano Lett. 7 (2007) 1643-1648. doi:10.1021/n1070613a.

[30] S. Viola Kusminskiy, D. K. Campbell, A. H. Castro Neto, F. Guinea, Pinning of a two-dimensional membrane on top of a patterned substrate: The case of graphene, Phys. Rev. B 83 (2011) 165405. doi:10.1103/PhysRevB.83.165405.

[31] S. Qiao, J. B. Gratadour, L. Wang, N. Lu, Conformability of a Thin Elastic Membrane Laminated on a Rigid Substrate With Corrugated Surface, IEEE Transactions on Components, Packaging and Manufacturing Technology 5 (9) (2015) 1237-1243. doi:10.1109/TCPMT.2015.2453319.

[32] P. Koskinen, O. O. Kit, Approximate modeling of spherical membranes, Phys. Rev. B 82 (2010) 235420. doi:10.1103/PhysRevB.82.235420.

[33] D. Sen, K. S. Novoselov, P. M. Reis, M. J. Buehler, Tearing graphene sheets from adhesive substrates produces tapered nanoribbons, Small 6 (2010) 1108-1116. doi:10.1002/sm11.201000097.

[34] Z. H. Aitken, R. Huang, Effects of mismatch strain and substrate surface corrugation on morphology of supported monolayer graphene, Journal of Applied Physics 107 (2010) 123531. doi:10.1063/1.3437642.

[35] H. Chen, Y. Yao, S. Chen, Adhesive contact between a graphene sheet and a nano-scale corrugated surface, J. Phys. D: Appl. Phys. 46 (2013) 205303. doi:10.1088/0022-3727/46/20/205303.

[36] L. Xiong, Y. Gao, Surface roughness and size effects on the morphology of graphene on a substrate, Physica E: Low-dimensional Systems and Nanostructures 54 (2013) 78-85. doi:10.1016/j.physe.2013.06.008.

[37] W. Zhu, T. Low, V. Perebeinos, A. A. Bol, Y. Zhu, H. Yan, J. Tersoff, P. Avouris, Structure and Electronic Transport in Graphene Wrinkles, Nano Letters 12 (7) (2012) 3431-3436. doi:10.1021/n1300563h.

[38] S. Deng, V. Berry, Wrinkled, rippled and crumpled graphene: an overview of formation mechanism, electronic properties, and applications, Materials Today 19 (4) (2016) 197-212. doi:10.1016/j.mattod.2015.10.002.

[39] X. He, Q. Bai, R. Shen, Atomistic perspective of how graphene protects metal substrate from surface damage in rough contacts, Carbon 130 (2018) 672-679. doi:10.1016/j.carbon.2018.01.023.

[40] L. Wang, J. Jin, P. Yang, Y. Zong, Q. Peng, Graphene Adhesion Mechanics on Iron Substrates: Insight from Molecular Dynamic Simulations, Crystals 9 (2019) 579. doi:10.3390/cryst9110579.

[41] ISO 25178-2: 2012 Geometrical product specifications (GPS) - Surface texture: Areal - Part 2: Terms, definitions and surface texture parameters (Aug. 2012).

[42] S. Eder, D. Bianchi, U. Cihak-Bayr, A. Vernes, G. Betz, An analysis method for atomistic abrasion simulations featuring rough surfaces and multiple abrasive particles, Computer Physics Communications 185 (2014) 2456-2466. doi:10.1016/j.cpc.2014.05.018.

[43] M. I. Mendelev, S. Han, D. J. Srolovitz, G. J. Ackland, D. Y. Sun, M. Asta, Development of new interatomic potentials appropriate for crystalline and liquid iron, Philosophical Magazine 83 (2003) 3977-3994. doi:10.1080/14786430310001613264.

[44] D. W. Brenner, Olga a Shenderova, Judith a Harrison, S. J. Stuart, B. Ni, S. B. Sinnott, A second-generation reactive empirical bond or- der (REBO) potential energy expression for hydrocarbons, Journal of Physics: Condensed Matter 14 (2002) 783-802. doi:10.1088/ 0953-8984/14/4/312.

[45] S. Plimpton, Fast Parallel Algorithms for Short-Range Molecular Dynamics, Journal of Computational Physics 117 (1995) 1-19. doi: 10.1006/jcph.1995.1039.

[46] J. Li, AtomEye: An efficient atomistic configuration viewer, Modelling Simul. Mater. Sci. Eng. 11 (2) (2003) 173-177. doi:10.1088/ 0965-0393/11/2/305.

[47] A. Stukowski, Visualization and analysis of atomistic simulation data with OVITO-the Open Visualization Tool, Modelling Simul. Mater. Sci. Eng. 18 (1) (2009) 015012. doi:10.1088/0965-0393/18/1/015012.

[48] A. Fasolino, J. H. Los, M. I. Katsnelson, Intrinsic ripples in graphene, Nat Mater 6 (11) (2007) 858-861. doi:10.1038/nmat2011.

[49] Y. Shen, H. Wu, Interlayer shear effect on multilayer graphene subjected to bending, Appl. Phys. Lett. 100 (10) (2012) 101909. doi:10. 1063/1.3693390.

[50] X. Zhao, M. Hamilton, W. G. Sawyer, S. S. Perry, Thermally Activated Friction, Tribol Lett 27 (1) (2007) 113-117. doi:10.1007/ s11249-007-9220-2.
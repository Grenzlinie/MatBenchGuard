# Size-dependent elastic properties of thin films: surface anisotropy and surface bonding

ZHOU XiaoYe, REN Hang, HUANG BaoLing & ZHANG TongYi*

Department of Mechanical and Aerospace Engineering, Hong Kong University of Science and Technology,
Clear Water Bay, Kowloon, Hong Kong, China

Received January 6, 2014; accepted February 18, 2014; published online March 10, 2014

Surface eigenstress and eigendisplacement models were used to investigate the surface stress, surface relaxation and surface elasticity of thin films with different surface orientations. Molecular dynamics simulations and first-principles calculations were conducted on face-centered cubic Au films with the focus on relaxation induced nonlinear initial deformation. The simulation results verify the theoretical predictions of the size dependency of surface energy density and surface stress, and the nonlinear scaling law of the size-dependent Young's modulus of thin films. The mechanism of the size-dependent behaviors was further explored at the atomic bonding level with the charge density field. The Au atomic bonding at surfaces is enhanced compared to its interior counterpart and therefore the nominal Young's modulus of the Au thin films is larger when the film thickness is smaller.

surface elasticity, surface stress, size-dependent Young's modulus, Molecular dynamics simulations, First-principle calculations

**Citation:** Zhou X Y, Ren H, Huang B L, et al. Size-dependent elastic properties of thin films: surface anisotropy and surface bonding. Sci China Tech Sci, 2014, 57: 680-691, doi: 10.1007/s11431-014-5499-z

## 1 Introduction
Atoms at solid surfaces have less coordination number than those in the bulk. In traditional continuum mechanics, the surface effect is ignored since the ratio of surface area to volume is negligible. However, when material's dimension is lowered down to the nanometer scale, the presence of surface is no longer trivial. Experimental results showed that elastic properties of nanomaterials are size-dependent. The Young's moduli of nanomaterials are either getting higher [1–3] or lower [4] as the dimensions of materials become smaller. Besides, theoretical studies have been conducted to clarify the mechanism lying behind the size-dependent elastic properties of nanomaterials. Miller and Shenoy [5] introduced the surface elastic constants to explain the size-dependent Young's Modulus of nanomaterial. Shenoy [6] further calculated the surface elastic constant tensor of thin films of various materials with different surface orientations and studied the effects of relaxation on surface elastic constants. Huang et al. [7,8] studied the size-dependent effective properties of a heterogeneous material with interface energy effect. Dingreville et al. [9] and Dingreville and Qu [10] systematically studied the relationship among the surface energy, surface stress and surface elastic constants within the scheme of continuum mechanics, showing that surface energy and surface stress would cause the size-dependent elastic behavior of nanomaterials. Zhou and Huang [11] studied the size-dependent Young's modulus of thin film with a combination of molecular statics and first-principles calculations and concluded that a surface might be softer or stiffer than the correspond-

*Corresponding author (email: mezhangt@ust.hk)
© Science China Press and Springer-Verlag Berlin Heidelberg 2014
tech.scichina.com link.springer.com

ing bulk and the size-dependent behavior depended on the competition between electron redistribution and lower co- ordination on the surface. Liang et al. [12] studied the Young's moduli of Cu nanowires with Molecular dynamics (MD) simulations and concluded that the core nonlinearity was the dominating factor affecting the size-dependent elas- tic properties of nanomaterials.

When a film is created by being taken out from a bulk material, fresh surfaces without relaxation have high surface energy. Besides, fresh surfaces are born with surface stress, called surface eigenstress. Due to the high surface energy and surface eigenstress, newly created thin films have to relax, which causes initial deformation and surface eigen- displacement. Surface relaxation has been widely studied by both experiments and simulations. Low energy electron diffraction was used to study the interlayer spacing change at metal surfaces [13] and the results showed that the top- most layer contracted inwards. The contraction was the largest for the topmost layer, and decreases rapidly for inner layers. Furthermore, the surface relaxation behaviors of films are dependent on surface orientations [14]. The con- traction amount of surface atom layers of Au nano-particles with diameters of 3-5 nm changed with the surface orienta- tion [14]. Through atomistic simulations, Diao et al. [15] found that surface relaxation induces the length change in gold nanowires and phase transformation for the nanowire with a small cross size of 1.83 nmx1.83 nm. Punkkinen et al.[16] studied the surface stress of 4d transition metal thin films by first-principles calculations and found that while in most cases surface stress of metal films is tensile, the sur- face stress of some magnetic materials is compressive, which was attributed to the magnetic pressure. Zhang et al.[17] studied the size-dependent elastic properties of nan- owires with MD simulations. The nanowire was first re- laxed to its free-standing equilibrium state and external loading was applied to obtain the nominal Young's moduli of the nanowires. The nominal Young's moduli of nan- owires were found to depend on the core Young's modulus, surface elastic modulus and edge elastic constant. Studies of pure bending and nanobridge tests [18] of nanowires further showed that the size-dependency of nominal Young's mod- ulus was more significant in bending tests than that in ten- sile-compressive tests. The study on Au nanowires [19] investigated the effect of surface and core nonlinearity on the nominal Young's modulus with the nonlinear scale laws derived from the surface eigenstress model [20]. For metals, the nonlinearity effect is significant and is the main factor influencing the nominal Young's modulus of nanowires because the relaxation-induced initial deformation is large and nonlinear. For diamond nanowires, the surface factor is predominant due to the linear relaxation-induced initial de- formation.

To have a clear understanding of the surface relaxation and its influence on size-dependent elastic properties of nanomaterials, Zhang et al. proposed the surface eigen- stress [20] and eigendisplacement models [21], which sys- tematically described the surface relaxation process. Con- sequently, the nonlinear scaling laws have been developed for the size-dependent nominal moduli of thin films and nanowires determined from tension/compression and bend- ing tests. As mentioned above, relaxation inevitably hap- pens in nanomaterials to reduce the surface energy or to relieve the surface eigenstress. For (100) Au films, Zhang etal. [21] separated the relaxation process into three steps: dimension-conserved normal relaxation, dimension- changed normal relaxation and parallel relaxation. The sur- face eigendisplacement is independent of the film thickness, while the equilibrium initial in-plane strain is dependent on the film thickness.

In the present study, the surface eigenstress and eigendis- placement models were used to study size-dependent Young's moduli of Au (110) and (111) thin films. A com- plete description of bulk elasticity and surface elasticity was given here in Appendix for the cubic (110) and (111) films and corresponding bulks, which provide the analytic for- mulas for the determination of surface properties from at- omistic calculations including first-principles calculations and MD simulations. The first-principles calculations aim to understand the mechanism of surface induced size-depen- dent behaviors at the atomic bonding level. Eberhart did extensive studies on the relationship between the charge density topology and the material's mechanical properties, such as shear moduli [22], fracture behavior [23] and stack- ing fault [24]. Recently, Nakashima et al. [25] used both experimental and theoretical methods to show that the bonding electron has a strong correlation with the Young's moduli. Following those works [22-25] we used the defor- mation charge density topology to explain the surface in- duced stiffening of thin films.

## 2 Surface eigenstress and surface eigendisplace- ment model

Following the previous approach [17, 20, 21], a thin film is considered as a composite of a geometrically three-dimen- sional (3D) core, which has the same material properties as its bulk counterpart, and two geometrically two-dimensional(2D) surfaces. The studied film has considerably large but finite in-plane dimensions along the x and y directions and a finite thickness along the z direction. Sufficiently large in-plane dimensions allow us to ignore the effect induced by lateral edges far away from the film central region of inter- est. The previous work [20, 21] has studied the elastic be- havior of the Au (100) films with the surface eigenstress and eigendisplacement models. Here we extend the model to Au (110) and (111) films. We consider a film built up with the lattice constant of its bulk counterpart with the original dimension of $L_{x} \times L_{y} \times h_{0}$ . For (110) films, the or thogonal coordinates of the x, y and z axes were set, respec-

tively, along $[1 \overline{1} 0]$, [001], and [110] directions. For (111) films, the $x$, $y$ and $z$ axes were set along $[\overline{1} \overline{1} 2]$, $[1 \overline{1} 0]$ and [111] directions, respectively. The newly created film has an unrelaxed potential energy, $U^{unr}$. Then the film will relax to minimize the energy. The relaxation was controlled and separated into dimension conserved normal relaxation, dimension changed normal relaxation, and parallel relaxation. The dimension conserved normal relaxation changed the potential energy from $U^{unr}$ to $U^{dc \perp r}$, and dimension changed normal relaxation further reduced the energy to $U^{\perp r}$, and the film thickness to $h=h_{0}+2 w_{0}$, with $w_{0}$ being the surface eigendisplacement [19]. After dimension changed normal relaxation, the traction-free boundary condition along the surface should be satisfied during parallel relaxation and afterwards. After parallel relaxation, the potential energy reached the minimum value of $U^{r}$ and an initial in-plane deformation appeared in the film.

Zhang et al. [21] gave a full description of normal relaxation by introducing surface elastic compliance. The nominal elastic compliance of a film is given as
$$
S_{z}^{n}=S_{z}^{c}+\frac{2 S_{z}^{s}}{h}, \quad(1)
$$
where $S_{z}^{n}$, $S_{z}^{c}$ and $S_{z}^{s}$ denote the nominal, core and surface elastic compliance of the film, respectively. Eq. (1) clearly shows that the nominal elastic compliance of thin film depends on film thickness. The work required to retrieve the film from the state after dimension changed normal relaxation to the state before dimension changed normal relaxation is
$$
W=\frac{A}{2} h \sigma_{z} \varepsilon_{z}^{n}=\frac{A}{2} \frac{h\left(\varepsilon_{z}^{n 0}\right)^{2}}{S_{z}^{n}}, \quad(2)
$$
where $A$ is the surface area of the simulated film, $\varepsilon_{z}^{n 0}=2 w_{0} / h$ is the nominal strain gauging the deformation from the state after dimension changed normal relaxation to the state before dimension changed normal relaxation. The corresponding relationship of surface energy is given by
$$
\gamma^{d c \perp r}=\gamma^{\perp r}+\frac{2 w_{0}^{2}}{h S_{z}^{c}+2 S_{z}^{s}}. \quad(3)
$$

Eqs. (1)-(3) are used to analyze the results from atomistic calculations during the normal relaxation.

The initial in-plane strain induced by parallel relaxation could be nonlinear, thus we need to consider higher order elastic constants. We include the theoretical description of the nonlinear elasticity for the core and surface in the Appendix. The second-order elastic constants (SOEC) and the third-order elastic constants (TOEC) are defined as the second and third order derivatives of the strain energy function with respect to strain and their values are determined accordingly from the simulations. As mentioned before, a thin film is treated as a composite of two surfaces and one core. The surface force and the core force should be balanced at equilibrium for a film under no external load. The force balance allows us to evaluate the values of surface elastic constants once the film thickness and the core elastic constants are available. This approach is stated with formulas in the Appendix. After obtaining the surface and bulk elastic constants and the surface eigenstresses, we calculate the nominal Young's modulus of thin films straightforwardly. For simplicity, we consider pseudo uniaxial Young's modulus with an in-plane dimension fixed for (110) films and biaxial Young's modulus for (111) films to demonstrate the size effect on the elastic properties of thin films. The derivation of the nominal Young's modulus of (110) and (111) thin films is described in detail in the Appendix. Adopting the definition of core and surface Young's moduli in the Appendix, the nominal Young's Modulus, $\bar{Y}_{i}^{n}$, of (110) thin films along $i$ ($x$ or $y$) direction with another in-plane ($y$ or $x$) dimension fixed is expressed by the following nonlinear scaling law:
$$
\bar{Y}_{i}^{n}=Y_{i}^{c}+\frac{2 Y_{i}^{s}}{h}+2\left(\tilde{Y}_{i}^{c}+\frac{2 \tilde{Y}_{i}^{s}}{h}\right) \varepsilon_{i}^{i n i},(i=x \text { or } y), \quad(4 \mathrm{a})
$$

$$
\begin{gathered}
\varepsilon_{i}^{i n i}=\frac{-\left(h Y_{i}^{c}+2 Y_{i}^{s}\right)+\sqrt{\left(h Y_{i}^{c}+2 Y_{i}^{s}\right)^{2}-8 \sigma_{i}^{s 0}\left(h \tilde{Y}_{i}^{c}+2 \tilde{Y}_{i}^{s}\right)}}{2\left(h \tilde{Y}_{i}^{c}+2 \tilde{Y}_{i}^{s}\right)}, \\
(i=x \text { or } y), \quad(4 \mathrm{~b})
\end{gathered}
$$
where $\varepsilon_{i}^{i n i}$ denotes the relaxation induced initial in-plane strain along $i$ direction, $Y_{i}^{c}$ and $\tilde{Y}_{i}^{c}$ denote the core first and second Young's modulus along $i$ direction, $Y_{i}^{s}$ and $\tilde{Y}_{i}^{s}$ denote the surface first and second Young's modulus along $i$ direction, and $\sigma_{i}^{s 0}$ is the surface eigenstress along $i$ direction. Similarly, the nonlinear scaling law for biaxial Young's modulus of (111) and (100) films is given by
$$
\bar{Y}_{b i}^{n}=Y_{b i}^{c}+\frac{2 Y_{b i}^{s}}{h}+2\left(\tilde{Y}_{b i}^{c}+\frac{2 \tilde{Y}_{b i}^{s}}{h}\right) \varepsilon_{b i}^{i n i}, \quad(5 \mathrm{a})
$$

$$
\begin{gathered}
\varepsilon_{b i}^{i n i}=\frac{-\left(h Y_{b i}^{c}+2 Y_{b i}^{s}\right)+\sqrt{\left(h Y_{b i}^{c}+2 Y_{b i}^{s}\right)^{2}-8 \sigma_{b i}^{s 0}\left(h \tilde{Y}_{b i}^{c}+2 \tilde{Y}_{b i}^{s}\right)}}{2\left(h \tilde{Y}_{b i}^{c}+2 \tilde{Y}_{b i}^{s}\right)}, \\
(5 \mathrm{~b})
\end{gathered}
$$
where $\varepsilon_{b i}^{i n i}$ denotes the relaxation induced initial biaxial in-plane strain, $Y_{b i}^{c}$ and $\tilde{Y}_{b i}^{c}$ denote the core first and second-order biaxial Young's modulus, $Y_{b i}^{s}$ and $\tilde{Y}_{b i}^{s}$ denote the surface first and second-order biaxial Young's modulus,

respectively, and $\sigma_{bi}^{s0}$ is the surface biaxial eigenstress.
Eq. (4) and eq. (5) are the nonlinear scaling laws of the nominal Young's modulus of thin film determined from tensile and compressive tests, indicating how the nominal Young's modulus of a thin film changes with its thickness. This size-dependency comes from the surface and the non- linearity of the material. The core and surface Young's moduli and the surface eigenstress are intrinsic material properties, while the initial in-plane strain and the nominal Young's modulus are all dependent on film thickness.

## 3 Simulations
### 3.1 MD simulations
In the previous study [20,21], the surface eigenstress and eigendisplacement models have been verified by MD simu- lations on the Au (100) films. Here we apply the models to Au (110) and (111) films. The simulations were performed with LAMMPS software [26] in a molecular statics frame- work and implemented by using the conjugate gradient method, and the Au embedded-atom potential [27,28]. Sim- ulations on bulk Au crystal were conducted first to get thecore elastic properties. A representative domain of $8 \times 8 \times 8$  was adopted with periodic boundary condition in all three directions to represent bulk FCC Au crystal. The orthogonal coordinates of the $x, y$ and $z$ axes were set, respectively, along [100], [010], and [001] directions of the crystal coor- dinate system. The methodology to determine the elastic constants from the simulations is stated in the Appendix. Then the core elastic constants in the sample coordinate system of the (111) or (110) films are calculated by the ro- tation transformation of coordinate system (see the Appen- dix for details). For thin film simulations, the periodic boundary condition is applied only along the in-plane direc- tions, i.e., along the $x$ and $y$ directions. The unrelaxed film has the same lattice arrangement as that in the stress-free bulk counterpart. The normal relaxation of the thin films was performed the same way as a previous simulation on(100) films [20,21]. Following the methodology described in the Appendix, a series of strain modes were applied to the thin film and the force balance equations were used for fit- ting the surface elastic constants. After parallel relaxation, the film is at thermodynamic equilibrium state with initial in-plane deformation. The pseudo uniaxial tensile/compress tests were simulated on the relaxed (110) films, where me-chanical tensile/compress loads were applied along $x$ (or $y$ )direction with $y$ (or $x$ ) dimension fixed to get the nominal pseudo uniaxial Young's modulus with one fixed in-plane dimension, whereas the biaxial tensile/compress tests were simulated on the relaxed (100) and (111) films to determine the biaxial Young's modulus.

### 3.2 First-principles calculations
With the local density approximation (LDA) [29] and the projector augmented wave (PAW) method [30] and using VASP software [31], we conducted first-principles calcula- tions to study the electronic structure of Au thin films. The equilibrium lattice constant of Au bulk was determined by energy minimization to be $4.062 \AA$ . The bulk elastic con stants were determined by performing tensile/compressive tests on bulk Au crystal. The films were built using the su- perlattice method with the bulk lattice constant. A vacuum layer of $20 \AA$ was used to separate thin films. The total charge density was obtained from self-consistent calcula- tions with the electronic energy convergent tolerance less than $1 ×10^{-5} eV$ . Like in MD simulations, relaxations were separated into normal relaxation and parallel relaxation. The structures were relaxed by using the conjugate gradient method and the residual force convergent tolerance was set to be less than $0.01 eV / \AA$ . The surface eigenstress and sur face elastic constants were determined from the force bal- ance equation, the same as the method adopted in the MD simulations. The nominal Young's moduli were predicted by the nonlinear scaling laws and were compared with the simulation results.
With first-principles calculations, we are able to visualize the electronic structure of Au thin films and the change of charge density during relaxation. According to Bader's the- ory of molecules and crystals [32], atomic bonding in the FCC Au could be described by the charge density at critical points, which are defined as the maximum, minimum and saddle points of the charge density field, $\rho(r)$ . At those points, the gradient of the charge density field vanishes. Bond critical point (BCP), which is defined as the saddle points of $\rho(r)$ , is simply the middle point between two nearest neighbor atoms for FCC metal (see Figure 1(a)). The cage critical point (CCP), showed in Figure 1(a), rep- resents the minimum of $\rho(r)$ and is located at the middle point between two second nearest neighbor atoms. To clearly illustrate the bonding charge density, we calculated the deformation charge density at BCPs. Deformation charge density is defined as the charge difference between the charge density of the solid and the superposition of theatomic charge density of isolated atoms:
$$\Delta \rho(\boldsymbol{r})=\rho(\boldsymbol{r})-\sum \rho_{\text {atom }}(\boldsymbol{r}),\qquad(6)$$
where $\rho(r)$ is the charge density of the FCC structure, and∑Patom(r) is the superposition of atomic charge densities placed at atomic sites. A higher $\Delta \rho(r)$ indicates a stronger bonding. Here we use $\Delta \rho(r)$ at BCPs to demonstrate the bonding strength. Figure 1(b) shows the charge density dif- ference $\Delta \rho(r)$ on (100), (110) and (111) planes of Au bulk crystal, illustrating an obvious electron accumulation at bond critical points (BCPs) which indicates that when

![](./images/813155244434259968_1.jpg)

Figure 1 (a) Schematic drawing showing the BCPs and CCPs on the (100), (110) and (111) planes of an FCC crystal; (b) charge density difference $\Delta\rho(r)$ on the (100), (110) and (111) planes of Au bulk crystal.

forming a FCC crystal, the Au atoms interact with each other via electron cloud and those bonding electrons are mainly located at BCPs.

During relaxation, the film changes its dimensions, which will make it difficult to compare the charge density before and after relaxation. Here we select a small volume surrounding a BCP before relaxation, called the small volume. When the small volume changes during deformation, we shall integrate deformation charge density inside the deformed small volume to denote the change of bonding strength with deformation. The small volume is not selected randomly. It should only contain the BCP of interest but not any other regions. Here we use a cube with each side about $0.1$ Å, about 1/25 of the inter-atomic distance.

## 4 Results and discussion
### 4.1 MD simulations

Table 1 lists the second-order elastic constants (SOEC) and third-order elastic constants (TOEC) of Au bulk crystal in the crystal coordinate system, while Table 2 shows the elastic constants in the sample coordinates of the (110) film. For (111) films, the first and second-order biaxial Young's moduli, $Y_{bi}^c$ and $\tilde{Y}_{bi}^c$, are 197.71 and $-1375.98$ GPa, respectively.

Figure 2 shows the (110) surface energy density as a function of film thickness before relaxation, after dimension conserved normal relaxation and after dimension changed normal relaxation. It has been demonstrated for Au (100) films [20,21] that dimension conserved normal relaxation causes all atomic layers to change their layer spacing, while only a few surface layers vary their layer spacing by dimension changed normal relaxation. The total change of the layer spacing induced by normal relaxation is called the surface eigendisplacement, which is a material surface intrinsic property independent of film thickness. Table 3 lists the change in atomic layer spacing after dimension changed normal relaxation for Au (100), (110), and (111) films, showing the surface orientation-dependency. The layer spacing change of (100) and (111) films stops after 4 atomic surface layers, but the layer spacing change happens for 8 atomic layers of (110) films. This means that (110) films need to adjust the spacing of more layers to reduce energy. Besides, the (110) surface has the largest value of the surface eigendisplacement, as shown in Table 4 and Figure 3. Table 4 shows the surface energy density before and after dimension changed normal relaxation, the energy reduction during normal relaxation and the surface eigendisplacement of Au (100), (110) and (111) films. The (110) surface possesses the largest surface energy density, while the (111)

<table>
<caption>Table 1 SOEC $c_{ij}$ and TOEC $\tilde{c}_{ijk}$ of Au bulk crystal in the crystal coordinate system</caption>
<thead>
<tr>
<th colspan="3">SOEC (GPa)</th>
<th colspan="6">TOEC (GPa)</th>
</tr>
<tr>
<th>$c_{11}$</th>
<th>$c_{12}$</th>
<th>$c_{44}$</th>
<th>$\tilde{c}_{111}$</th>
<th>$\tilde{c}_{222}$</th>
<th>$\tilde{c}_{112}$</th>
<th>$\tilde{c}_{144}$</th>
<th>$\tilde{c}_{155}$</th>
<th>$\tilde{c}_{123}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>183.3</td>
<td>159.4</td>
<td>44.3</td>
<td>−998.8</td>
<td>−769.5</td>
<td>−1487.3</td>
<td>1505.1</td>
<td>−191.4</td>
<td>−5032.2</td>
</tr>
</tbody>
</table>

<table>
<caption>Table 2 SOEC $c'_{ij}$ and TOEC $\tilde{c}'_{ijk}$ of Au bulk crystal in the sample coordinate of the (110) films</caption>
<thead>
<tr>
<th colspan="6">SOEC (GPa)</th>
<th colspan="9">TOEC (GPa)</th>
</tr>
<tr>
<th>$c'_{11}$</th>
<th>$c'_{22}$</th>
<th>$c'_{33}$</th>
<th>$c'_{12}$</th>
<th>$c'_{23}$</th>
<th>$c'_{13}$</th>
<th>$\tilde{c}'_{111}$</th>
<th>$\tilde{c}'_{222}$</th>
<th>$\tilde{c}'_{333}$</th>
<th>$\tilde{c}'_{122}$</th>
<th>$\tilde{c}'_{112}$</th>
<th>$\tilde{c}'_{133}$</th>
<th>$\tilde{c}'_{113}$</th>
<th>$\tilde{c}'_{233}$</th>
<th>$\tilde{c}'_{223}$</th>
<th>$\tilde{c}'_{123}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>215.7</td>
<td>183.1</td>
<td>215.7</td>
<td>158.7</td>
<td>158.7</td>
<td>127.1</td>
<td>−1939.3</td>
<td>−998.8</td>
<td>−1939.3</td>
<td>−769.5</td>
<td>−1754.6</td>
<td>−1173.8</td>
<td>−1173.8</td>
<td>−1754.6</td>
<td>−769.5</td>
<td>−4764.8</td>
</tr>
</tbody>
</table>

![](./images/813155244434259968_2.jpg)

Figure 2 The (110) surface energy density versus film thickness. The
solid curve denotes the prediction from $\gamma^{dc,1r}=\gamma^{1r}+\frac{2w_{0}^{2}}{hS_{c}^{z}+2S_{z}^{s}}$.

<table>
 <thead>
  <tr>
   <th colspan="4">
    Table 3 Changes in atomic layer spacing ($\Delta h_{i,i + 1}$) after NR in Au (100), (110), and (111) films
   </th>
  </tr>
  <tr>
   <th>
   </th>
   <th>
    (110)
   </th>
   <th>
    (100)
   </th>
   <th>
    (111)
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <th>
    $\Delta h_{1,2}$
   </th>
   <td>
    $- 0.222$
   </td>
   <td>
    $- 0.129$
   </td>
   <td>
    $- 0.101$
   </td>
  </tr>
  <tr>
   <th>
    $\Delta h_{2,3}$
   </th>
   <td>
    $0.032$
   </td>
   <td>
    $0.012$
   </td>
   <td>
    $0.015$
   </td>
  </tr>
  <tr>
   <th>
    $\Delta h_{3,4}$
   </th>
   <td>
    $- 0.010$
   </td>
   <td>
    $0.000$
   </td>
   <td>
    $- 0.002$
   </td>
  </tr>
  <tr>
   <th>
    $\Delta h_{4,5}$
   </th>
   <td>
    $0.009$
   </td>
   <td>
    $0.000$
   </td>
   <td>
    $0.000$
   </td>
  </tr>
  <tr>
   <th>
    $\Delta h_{5,6}$
   </th>
   <td>
    $- 0.004$
   </td>
   <td>
    $0.000$
   </td>
   <td>
    $0.000$
   </td>
  </tr>
  <tr>
   <th>
    $\Delta h_{6,7}$
   </th>
   <td>
    $0.002$
   </td>
   <td>
    $0.000$
   </td>
   <td>
    $0.000$
   </td>
  </tr>
  <tr>
   <th>
    $\Delta h_{7,8}$
   </th>
   <td>
    $- 0.001$
   </td>
   <td>
    $0.000$
   </td>
   <td>
    $0.000$
   </td>
  </tr>
  <tr>
   <th>
    $\Delta h_{8,9}$
   </th>
   <td>
    $0.000$
   </td>
   <td>
    $0.000$
   </td>
   <td>
    $0.000$
   </td>
  </tr>
 </tbody>
</table>

<table>
 <thead>
  <tr>
   <th colspan="5">
    Table 4 Surface energy densities before and after normal relaxation ($\gamma^{unr}$, $\gamma^{1r}$) and their difference (${\Delta\gamma} = {\gamma^{unr} - \gamma^{1r}}$), and eigendisplacement ($w_{0}$)
   </th>
  </tr>
  <tr>
   <th>
   </th>
   <th>
    $\gamma^{unr}$ (J/m²)
   </th>
   <th>
    $\gamma^{1r}$ (J/m²)
   </th>
   <th>
    $\Delta\gamma$ (J/m²)
   </th>
   <th>
    $w_{0}$ (nm)
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <th>
    (110)
   </th>
   <td>
    $1.094$
   </td>
   <td>
    $0.976$
   </td>
   <td>
    $0.117$
   </td>
   <td>
    $- 0.0195$
   </td>
  </tr>
  <tr>
   <th>
    (100)
   </th>
   <td>
    $0.976$
   </td>
   <td>
    $0.915$
   </td>
   <td>
    $0.061$
   </td>
   <td>
    $- 0.0117$
   </td>
  </tr>
  <tr>
   <th>
    (111)
   </th>
   <td>
    $0.826$
   </td>
   <td>
    $0.785$
   </td>
   <td>
    $0.041$
   </td>
   <td>
    $- 0.0088$
   </td>
  </tr>
 </tbody>
</table>

![](./images/813155244434259968_3.jpg)

Figure 3 Relationship between the energy reduced during normal relaxation and the surface eigendisplacement.

surface has the lowest. We plotted the normal relaxation-induced reduction in the surface energy density versus the surface eigendisplacement in Figure 3, showing a liner relationship between the two properties.

Using the force balance and initial in-plane strain induced by parallel relaxation, we determine the surface eigenstress and surface second and third-order elastic constants, which are listed in Table 5 for the (110) surface and in Table 6 for the (100) and (111) surfaces.

After relaxation, we conducted tension/compression tests on the films to determine the nominal elastic constants. The nominal Young’s modulus along $x$ or $y$ direction of the (110) films, the nominal biaxial Young’s modulus of the (111) films and (100) films [20] are plotted against the film thickness in Figures 4–7. The simulation results agree well with the prediction from the nonlinear scaling laws of eqs. (4) and (5). The nominal Young’s modulus along [1 $\overline{1}$0] direction of the (110) films and the biaxial nominal Young’s modulus of the (111) films become higher as the thickness decreases, while the nominal Young’s modulus along [001]

<table>
 <thead>
  <tr>
   <th colspan="7">
    Table 5 Surface eigenstress and surface elastic constants of (111) films
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>
    Eigenstress
   </td>
   <td>
   </td>
   <td>
    $\sigma_{x}^{s0}$
   </td>
   <td>
    $\sigma_{y}^{s0}$
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    (N m-1)
   </td>
   <td>
   </td>
   <td>
    1.53
   </td>
   <td>
    0.88
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    SOEC
   </td>
   <td>
   </td>
   <td>
    $C_{11}^{s}$
   </td>
   <td>
    $C_{12}^{s}$
   </td>
   <td>
    $C_{22}^{s}$
   </td>
   <td>
    $Y_{x}^{s}$
   </td>
   <td>
    $Y_{y}^{s}$
   </td>
  </tr>
  <tr>
   <td>
    (N m-1)
   </td>
   <td>
   </td>
   <td>
    2.73
   </td>
   <td>
    15.96
   </td>
   <td>
    $- 7.22$
   </td>
   <td>
    2.73
   </td>
   <td>
    $- 7.22$
   </td>
  </tr>
  <tr>
   <td>
    TOEC
   </td>
   <td>
   </td>
   <td>
    ${\overset{\sim}{C}}_{111}^{s}$
   </td>
   <td>
    ${\overset{\sim}{C}}_{222}^{s}$
   </td>
   <td>
    ${\overset{\sim}{C}}_{122}^{s}$
   </td>
   <td>
    ${\overset{\sim}{C}}_{211}^{s}$
   </td>
   <td>
    ${\overset{\sim}{Y}}_{x}^{s}$
   </td>
   <td>
    ${\overset{\sim}{Y}}_{y}^{s}$
   </td>
  </tr>
  <tr>
   <td>
    (N m-1)
   </td>
   <td>
   </td>
   <td>
    8.21
   </td>
   <td>
    9.85
   </td>
   <td>
    343.89
   </td>
   <td>
    $- 155.92$
   </td>
   <td>
    4.11
   </td>
   <td>
    4.93
   </td>
  </tr>
 </tbody>
</table>

<table>
 <thead>
  <tr>
   <th colspan="4">
    Table 6 Surface eigenstress and surface biaxial Young’s moduli of (100) and (111) films
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>
   </td>
   <td>
    $\sigma^{s0}$(N m-1)
   </td>
   <td>
    $Y_{bi}^{s}$(N m-1)
   </td>
   <td>
    ${\overset{\sim}{Y}}_{bi}^{s}$(N m-1)
   </td>
  </tr>
  <tr>
   <td>
    (100) [20, 21]
   </td>
   <td>
    1.56
   </td>
   <td>
    $- 1.40$
   </td>
   <td>
    $- 5.44$
   </td>
  </tr>
  <tr>
   <td>
    (111)
   </td>
   <td>
    2.42
   </td>
   <td>
    $- 21.92$
   </td>
   <td>
    383.20
   </td>
  </tr>
 </tbody>
</table>

![](./images/813155244434259968_4.jpg)

Figure 4 Nominal biaxial Young’s modulus of Au (100) films, including the results from MD simulations [20], first-principles calculations and predictions from nonlinear scaling law of eq. (5).

![](./images/813155244434259968_5.jpg)

Figure 5 Nominal Young's modulus along x direction [1 $\overline{1}$0] of the Au (110) films, including the results from MD simulations, first-principles calculations and predictions from nonlinear scaling law of eq. (4).

![](./images/813155244434259968_6.jpg)

Figure 6 Nominal Young's modulus along y direction [001] of the Au (110) films, including the results from MD simulations, first-principles calculations and predictions from nonlinear scaling law of eq. (4).

![](./images/813155244434259968_7.jpg)

Figure 7 Nominal biaxial Young's modulus of Au (111) films, including the results from MD simulations, first-principles calculations and predictions from nonlinear scaling law of eq. (5).

direction of the (110) films shows the opposite trend. Although the trend of the size-dependent Young's modulus varies with the loading direction, the nonlinear scaling law of eq. (4) is universal, which predicts the nominal Young's moduli of (110) thin films perfectly. Eq. (4) indicates that the values of surface and core first and second order Young's moduli, and the value of surface eigenstress determine whether the nominal Young' modulus of a thin film gets higher or lower as the film thickness decreases. These values together describe the elastic behavior of thin films.

### 4.2 First-principles calculations

Table 7 listed the core and surface elastic properties of Au thin films obtained from first-principles calculations. The elastic properties were used to predict the nominal Young's moduli of thin films. The nominal Young's moduli of Au (100), (110), and (111) thin films calculated by the first-principles calculations are also illustrated in Figures 4-7, where the theoretical prediction based on the nonlinear scaling laws are plotted by the solid curves. Although the values of material and surface intrinsic properties determined from the first-principles calculations vary from these calculated from MD simulations, the theoretical prediction based on the nonlinear scaling laws agree with the data from the first-principles calculations, which indicates again the general validness of the nonlinear scaling laws. Furthermore, the two simulation methods gave the same trends of the size-dependent Young's moduli.

Table 8 listed the deformation charge density at BCPs of the 5 topmost atomic layers of (100) films with different thickness. It is shown that the $\Delta \rho$ at the first layer is larger than those layers inside the material, while the $\Delta \rho$ at the second layer decreases a little but not obvious. From the third layer, the $\Delta \rho$ almost remains the same, meaning that

<table><caption>Table 7 Core and surface elastic properties of Au (100), (110) and (111) thin films obtained from DFT calculations</caption>
  <thead>
    <tr>
      <th></th>
      <th>(100)</th>
      <th>[1 $\overline{1}$0] /(110)</th>
      <th>[001]/(110)</th>
      <th>(111)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$Y^c$ (GPa)</td>
      <td>83.66</td>
      <td>132.83</td>
      <td>73.33</td>
      <td>187.67</td>
    </tr>
    <tr>
      <td>$\tilde{Y}^c$ (GPa)</td>
      <td>–723.81</td>
      <td>–1333.50</td>
      <td>–963.15</td>
      <td>–2046.73</td>
    </tr>
    <tr>
      <td>$Y^s$ (N m$^{-1}$)</td>
      <td>48.75</td>
      <td>63.65</td>
      <td>–26.67</td>
      <td>95.37</td>
    </tr>
    <tr>
      <td>$\tilde{Y}^s$ (N m$^{-1}$)</td>
      <td>60.47</td>
      <td>409.23</td>
      <td>461.85</td>
      <td>655.06</td>
    </tr>
    <tr>
      <td>$\sigma^{s0}$ (N m$^{-1}$)</td>
      <td>3.20</td>
      <td>3.31</td>
      <td>1.67</td>
      <td>4.21</td>
    </tr>
  </tbody>
</table>

<table><caption>Table 8 Deformation charge density $\Delta \rho$ at BCP of each layers and the surface excess of deformation charge density $\Delta \rho_{surface}$ of (100) films with different thickness</caption>
  <thead>
    <tr>
      <th colspan="2">Thickness (nm)</th>
      <th>1.83</th>
      <th>2.23</th>
      <th>2.64</th>
      <th>3.05</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="5">$\Delta \rho$ at BCP</td>
      <td>1st</td>
      <td>0.0414</td>
      <td>0.0414</td>
      <td>0.0414</td>
      <td>0.0414</td>
    </tr>
    <tr>
      <td>2nd</td>
      <td>0.0323</td>
      <td>0.0324</td>
      <td>0.0324</td>
      <td>0.0323</td>
    </tr>
    <tr>
      <td>3rd</td>
      <td>0.0336</td>
      <td>0.0336</td>
      <td>0.0336</td>
      <td>0.0336</td>
    </tr>
    <tr>
      <td>4th</td>
      <td>0.0336</td>
      <td>0.0336</td>
      <td>0.0336</td>
      <td>0.0336</td>
    </tr>
    <tr>
      <td>5th</td>
      <td>0.0338</td>
      <td>0.0338</td>
      <td>0.0338</td>
      <td>0.0338</td>
    </tr>
    <tr>
      <td colspan="2">$\Delta \rho_{surface}$</td>
      <td>0.0058</td>
      <td>0.0058</td>
      <td>0.0058</td>
      <td>0.0058</td>
    </tr>
  </tbody>
</table>

the change happens only at the surface layers. Therefore, we can define a surface property that is independent of film thickness. Following Gibbs' definition of surface properties, we define a surface excess deformation charge density as

$$
\Delta \rho_{\text {surface }}=\sum_{i=1}^{N} \Delta \rho_{i}-N \Delta \rho_{\text {bulk }}, \quad(7)
$$

where $\sum_{i=1}^{N} \Delta \rho_{i}$ represents the sum of the deformation charge densities at BCP (or any other critical points of the charge density field) of each atomic layer of the thin film, $\Delta \rho_{b u l k}$ is the deformation charge density at BCP of the corresponding bulk. Table 8 shows that the surface excess deformation charge density is independent of the film thickness, because the charge redistribution occurs only at a few layers near the surface. Therefore, the surface excess deformation charge density must be an intrinsic property of a material surface like the surface eigenstress, surface eigendisplacement and surface elastic constants.

Table 9 lists the deformation charge density at BCPs and CCPs at the 5 topmost layers of (100), (110) and (111) Au films and the surface excess charge density. It is clear that the surface excess are positive at BCPs of all three films, but are negative at the CCP of (110) film. As shown in Figure 1(a), the CCPs of (110) film are located between atoms along the [001] direction, while the BCPs are located between atoms along $[1 \overline{1} 0]$. The surface excess at these two kinds of critical points shows that the bonding along [001] is weakened by the surface while the bonding along $[1 \overline{1} 0]$ is strengthened by the surface. For (100) Au films, the atomic bonds at BCP and CCP are both strengthened by the surface and for (111) Au films, the atomic bonds at BCP are also enhanced by the surface. The surface excess deformation charge density can explain the size-dependent Young's moduli of thin films. The atomic bonds along [001] direction are weakened by the surface, thereby leading to a decrease in the nominal Young's modulus along

<table><thead><tr><th rowspan="3">Layer number</th><th colspan="6">$\Delta \rho$ ($10^{-3}$ e/Å³)</th></tr><tr><th colspan="2">(100)</th><th colspan="2">(110)</th><th colspan="2">(111)</th></tr><tr><th>BCP</th><th>CCP</th><th>BCP</th><th>CCP</th><th>BCP</th><th>CCP</th></tr></thead><tbody><tr><td>1st</td><td>41.40</td><td>17.41</td><td>42.99</td><td>13.87</td><td>39.56</td><td rowspan="7">N.A.</td></tr><tr><td>2nd</td><td>32.85</td><td>11.99</td><td>33.79</td><td>11.61</td><td>33.72</td></tr><tr><td>3rd</td><td>34.10</td><td>15.12</td><td>34.20</td><td>14.32</td><td>34.36</td></tr><tr><td>4th</td><td>34.32</td><td>14.71</td><td>34.46</td><td>14.55</td><td>34.47</td></tr><tr><td>5th</td><td>34.37</td><td>14.72</td><td>34.58</td><td>14.79</td><td>34.48</td></tr><tr><td>bulk</td><td>34.45</td><td>14.73</td><td>34.45</td><td>14.73</td><td>34.45</td></tr><tr><td>$\Delta q_{surface}$</td><td>4.90</td><td>0.30</td><td>7.75</td><td>$-4.50$</td><td>4.35</td></tr></tbody></table>

Table 9 Deformation charge density $\Delta \rho$ at BCPs and CCPs at each atom layer of (100), (110) and (111) Au films and the corresponding bulks and the surface excess of deformation charge density $\Delta \rho_{surface}$

[001] direction when the film thickness goes down, as shown in Figure 6. For (100) and (111) Au films and the $[1 \overline{1} 0]$ direction of (110) Au films, the surface is a strengthening factor which leads to an increase of Young's moduli as the thickness decreases, as shown in Figures 4, 5 and 7.

Table 10 lists the amount of deformation charge in an original small volume surrounding BCP at each atomic layer of Au (100), (110) and (111) films and CCP of (110) films before relaxation, after normal relaxation and after parallel relaxation. The small volume scales with the whole structure when it changes its dimensions, so that the charge included in this small volume before and after relaxation can be compared. Here the surface charge excess, which definition is similar to eq. (9), is no longer refers to surface excess deformation charge density, but rather an integration of charge density in that small volume. The calculation results show that the surface charge excess is positive for the BCP of Au (100), (110) and (111) films, but negative for the CCP of (110) films. However, the values of surface charge excess all increase after parallel relaxation, which might mean that the relaxation enhances the surface effect on the bonding strength.

<table><thead><tr><th rowspan="3"></th><th colspan="3">(100) BCP</th><th colspan="3">(110) BCP</th><th colspan="3">(110) CCP</th><th colspan="3">(111) BCP</th></tr><tr><th>UR</th><th>NR</th><th>PR</th><th>UR</th><th>NR</th><th>PR</th><th>UR</th><th>NR</th><th>PR</th><th>UR</th><th>NR</th><th>PR</th></tr></thead><tbody><tr><td>1st</td><td>33.4</td><td>33.7</td><td>35.8</td><td>34.4</td><td>33.9</td><td>36.3</td><td>11.2</td><td>13.3</td><td>12.2</td><td>31.8</td><td>32.0</td><td>33.5</td></tr><tr><td>2nd</td><td>26.4</td><td>26.2</td><td>29.2</td><td>27.0</td><td>26.9</td><td>28.5</td><td>9.3</td><td>9.9</td><td>9.3</td><td>27.1</td><td>27.1</td><td>28.6</td></tr><tr><td>3rd</td><td>27.4</td><td>27.5</td><td>30.3</td><td>27.3</td><td>27.7</td><td>29.8</td><td>11.5</td><td>11.4</td><td>11.5</td><td>27.6</td><td>27.6</td><td>29.0</td></tr><tr><td>4th</td><td>27.4</td><td>27.4</td><td>30.3</td><td>27.3</td><td>27.3</td><td>29.5</td><td>12.0</td><td>11.7</td><td>11.8</td><td>27.7</td><td>27.7</td><td>29.1</td></tr><tr><td>5th</td><td>27.4</td><td>27.4</td><td>30.3</td><td>27.3</td><td>27.3</td><td>29.5</td><td>12.0</td><td>11.8</td><td>11.8</td><td>27.7</td><td>27.7</td><td>29.1</td></tr><tr><td>Bulk</td><td>27.5</td><td>27.5</td><td>27.5</td><td>27.5</td><td>27.5</td><td>27.5</td><td>11.8</td><td>11.8</td><td>11.8</td><td>27.5</td><td>27.5</td><td>27.5</td></tr><tr><td>$\Delta q_{surface}$</td><td>4.5</td><td>4.7</td><td>18.4</td><td>5.8</td><td>5.6</td><td>16.1</td><td>$-3.0$</td><td>$-0.9$</td><td>$-2.4$</td><td>4.4</td><td>4.6</td><td>11.8</td></tr></tbody></table>

Table 10 Amount of deformation charge in an original small volume, dv, around BCP at each layer of Au (100), (110) and (111) films and CCP of (110) film before relaxation (UR), after normal relaxation (NR) and after parallel relaxation (PR)

$$
\Delta q=\int \Delta \rho(\boldsymbol{r}) \mathrm{d} v \times 10^{-5}(\mathrm{e})
$$

## 5 Conclusions

In this study, the surface eigenstress and eigendisplacement models were adopted to study the elastic properties of thin films with different surface orientations. The surface and core elastic properties of (110) and (111) films were deter- mined from the MD simulations and the first-principles calculations. The surface eigenstress, surface and core elas- tic constants are intrinsic material properties and with them we are able to predict the size-dependent nominal Young's moduli of thin films with the nonlinear scaling laws. Alt- hough the values of the intrinsic properties depend on the atomic potential used in the MD simulations and the nu- merical method in first-principles calculations, the nonlinear scaling laws are generally valid. The first-principles calcu- lations further provide information about the bonding situa- tion of thin films. The calculated deformation charge densi- ties at bond critical points of thin films show that the en- hanced bond strength at surface layer is responsible for the higher Young's modulus of thin film in comparison with its bulk counterpart. While the surface is an elastically streng-thening factor for the $Au(100),(111)$ films and $[1 \overline{1} 0]$  direction of (110) films, it is an elastically weakening factor for [001] direction of $Au$ (110) films, as illustrated by the surface excess deformation charge density. The analysis of charge density topology confirms the results of nominal Young's moduli calculated from MD simulations and first-principles calculations, and shed the electronic struc- ture and atomic bonding insight into the mechanism of the size-dependent nominal elastic modulus of thin films.

This work was supported by the Hong Kong Research Grants Council(Grant No. 622312).

1 Cuenot S, Frétigny C, Demoustier-Champagne S, et al. Surface ten- sion effect on the mechanical properties of nanomaterials measuredby atomic force microscopy. Phys Rev B, 2004, 69(16): 165410
2 Ni H, Li X. Young's modulus of $ZnO$ nanobelts measured using atomic force microscopy and nanoindentation techniques. Nano-technology, 2006, 17(14): 3591
3 Chen C Q, Shi Y, Zhang Y S, et al. Size dependence of Young'smodulus in ZnO nanowires. Phys Rev Lett, 2006, 96(7): 075505
4 Nam C Y, Jaroenapibal P, Tham D, et al. Diameter-dependent elec-tromechanical properties of GaN nanowires. Nano lett, 2006, 6(2):153-158
5 Miller Ronald E, Shenoy Vijay B. Size-dependent elastic propertiesof nanosized structural elements. Nanotechnology, 2000, 11(3): 139
6 Shenoy Vijay B. Atomistic calculations of elastic properties of me-tallic fcc crystal surfaces. Phys Rev B, 2005, 71(9): 094104
7 Huang Z P, Wang J. A theory of hyperelasticity of multi-phase mediawith surface/interface energy effect. Acta Mechanica, 2006, 182(3-4):195-210
8 Huang Z P, Sun L. Size-dependent effective properties of a hetero- geneous material with interface energy effect: from finite defor- mation theory to infinitesimal strain analysis. Acta Mechanica, 2007,190(1-4): 151-163
9 Dingreville R, Qu J, Mohammed C. Surface free energy and its effect on the elastic behavior of nano-sized particles, wires and films. JMech Phys Solids, 2005, 53(8): 1827-1854
10 Dingreville R, Qu J. A semi-analytical method to compute surfaceelastic properties. Acta Mater, 2007, 55(1): 141-147
11 Zhou L G, Huang H C. Are surfaces elastically softer or stiffer? ApplPhys Lett, 2004, 84(11): 1940-1942
12 Liang H, Upmanyu M, Huang H. Size-dependent elasticity of nan-owires: Nonlinear effects. Phys Rev B, 2005, 71(24): 241403
13 Jona F. LEED crystallography. J Phys C, 1978, 11(21): 4271-4306
14 Huang W J, Sun R, Tao J, et al. Coordination-dependent surface atomic contraction in nanocrystals revealed by coherent diffraction.Nat Mater, 2008, 7(4): 308-313
15 Diao J, Gall K L, Dunn M. Atomistic simulation of the structure andelastic properties of gold nanowires. J Mech Phys Solids, 2004, 52(9):1935-1962
16 Punkkinen M P J, Kwon S K, Kollár J, et al. Compressive surfacestress in magnetic transition metals. Phys Rev Lett, 2011, 106(5):057202
17 Zhang T Y, Luo M, Chan W K. Size-dependent surface stress, sur-face stiffness, and Young's modulus of hexagonal prism [111] $\beta-SiC$ nanowires. J Appl Phys, 2008, 103(10): 104308
18 Chan W K, Zhang T Y. Mechanics analysis and atomistic simula-tions of nanobridge tests. J Appl Phys, 2010, 107(2): 023526
19 Wang Z J, Liu C, Li Z G, et al. Size-dependent elastic properties of Au nanowires under bending and tension-Surfaces versus core non-linearity. J Appl Phys, 2010, 108(8): 083506-083508
20 Zhang T Y, Wang Z J, Chan W K. Eigenstress model for surfacestress of solids. Phys Rev B, 2010, 81(19): 195427
21 Zhang T Y, Ren H, Wang Z, et al. Surface eigen-displacement and surface Poisson's ratios of solids. Acta Mater, 2011, 59(11): 4437-4447
22 Eberhart M. Charge-density-shear-moduli relationships in aluminum-lithium alloys. Phys Rev Lett, 2001, 87(20): 205503
23 Jones T E, Sauer M A, Eberhart M E. First-principles study of the mode-1 fracture of Fe-TiX interfaces (X=C,N). Phys Rev B, 2008,78(9):092104
24 Kioussis N, Herbranson M, Collins E, et al. Topology of electronic charge density and energetics of planar faults in fcc metals. Phys RevLett, 2002, 88(12): 125501
25 Nakashima P N H, Smith A E, Etheridge J, et al. The bonding elec-tron density in aluminum. Science, 2011, 331(6024): 1583-1586
26 Plimpton S. Fast parallel algorithms for short-range molecular dy-namics. J Comput Phys, 1995, 117(1): 1-19
27 Daw M S, Baskes M I. Semiempirical, quantum mechanical calcula- tion of hydrogen embrittlement in metals. Phys Rev Lett, 1983,50(17): 1285-1288
28 Daw M S, Baskes M I. Embedded-atom method: Derivation and ap- plication to impurities, surfaces, and other defects in metals. PhysRev B, 1984, 29(12): 6443-6453
29 Perdew J P, Zunger A. Self-interaction correction to density- functional approximations for many-electron systems. Phys Rev B,1981, 23(10): 5048-5079
30 Blochl P E. Projector augmented-wave method. Phys Rev B, 1994,50(24): 17953-17979
31 Kresse G, Hafner J. Ab initio molecular-dynamics simulation of the liquid-metal-amorphous-semiconductor transition in germanium.Phys Rev B, 1994, 49(20): 14251-14269
32 Bader R F W. Atoms in Molecules: a Quantum Theory. Oxford: Ox-ford University Press,1990

### Appendix
## Nonlinear elasticity of Au bulk crystal

In the present work, the mechanics analysis is carried out in a Lagrangian coordinate system, i.e., in the undeformed coordinate system. The potential energy of a solid body can be expressed in terms of strains through Taylor-series expansion

$$
U=V_{0}[u(0)+\frac{1}{2 !} c_{i j k l} \varepsilon_{i j} \varepsilon_{k l}+\frac{1}{3 !} \tilde{c}_{i j k l m n} \varepsilon_{i j} \varepsilon_{k l} \varepsilon_{m n}+\ldots], \quad \text { (A1) }
$$

where $\varepsilon_{i j}$ denotes the strain tensor with $i$ and $j(=1,2,3)$ representing the Cartesian coordinates, $c_{i j k l}$ and $\tilde{c}_{i j k l m n}$ represent, respectively, the second-order elastic constant (SOEC) tensor and third-order elastic constant (TOEC) tensor, $V_{0}$ is the volume of the undeformed body, and $u(0)$ is the potential energy density per unit volume at the stress-free state. We can simplify the notations in the tensors by the Voight notation $(11 \rightarrow 1,22 \rightarrow 2,33 \rightarrow 3,23 \rightarrow 4$, $31 \rightarrow 5$ and $12 \rightarrow 6)$. Therefore, we have $\varepsilon_{11}=\varepsilon_{1}, \varepsilon_{22}=\varepsilon_{2}$, $\varepsilon_{33}=\varepsilon_{3}, \varepsilon_{23}=\varepsilon_{4} / 2, \varepsilon_{31}=\varepsilon_{5} / 2$ and $\varepsilon_{12}=\varepsilon_{6} / 2$ for the strain tensors.

For single crystal with cubic symmetry, the SOEC have 3 independent components: $c_{11}, c_{12}$ and $c_{44}$. The TOEC have 6 independent components: $\tilde{c}_{111}, \tilde{c}_{112}, \tilde{c}_{144}, \tilde{c}_{155}$, $\tilde{c}_{123}$ and $\tilde{c}_{456}$. The energy density can be expressed as

$$
\frac{U}{V_{0}}=u(0)+\phi_{2}+\phi_{3}+\ldots, \quad \text { (A2) }
$$

where
$$
\begin{aligned}
\phi_{2}= & \frac{1}{2} c_{11}\left(\varepsilon_{1}^{2}+\varepsilon_{2}^{2}+\varepsilon_{3}^{2}\right)+c_{12}\left(\varepsilon_{1} \varepsilon_{2}+\varepsilon_{1} \varepsilon_{3}+\varepsilon_{2} \varepsilon_{31}\right) \\
& +\frac{1}{2} c_{44}\left(\varepsilon_{4}^{2}+\varepsilon_{5}^{2}+\varepsilon_{6}^{2}\right),
\end{aligned}
$$

$$
\begin{aligned}
\phi_{3}= & \frac{1}{6} \tilde{c}_{111}\left(\varepsilon_{1}^{3}+\varepsilon_{2}^{3}+\varepsilon_{3}^{3}\right) \\
& +\frac{1}{2} \tilde{c}_{112}\left(\varepsilon_{1}^{2} \varepsilon_{2}+\varepsilon_{1}^{2} \varepsilon_{3}+\varepsilon_{2}^{2} \varepsilon_{3}+\varepsilon_{2}^{2} \varepsilon_{1}+\varepsilon_{3}^{2} \varepsilon_{1}+\varepsilon_{3}^{2} \varepsilon_{2}\right) \\
& +\frac{1}{2} \tilde{c}_{144}\left(\varepsilon_{4}^{2} \varepsilon_{1}+\varepsilon_{5}^{2} \varepsilon_{2}+\varepsilon_{6}^{2} \varepsilon_{3}\right) \\
& +\frac{1}{2} \tilde{c}_{155}\left(\varepsilon_{4}^{2} \varepsilon_{2}+\varepsilon_{4}^{2} \varepsilon_{3}+\varepsilon_{5}^{2} \varepsilon_{1}+\varepsilon_{5}^{2} \varepsilon_{3}+\varepsilon_{6}^{2} \varepsilon_{1}+\varepsilon_{6}^{2} \varepsilon_{2}\right) \\
& +\tilde{c}_{456} \varepsilon_{4} \varepsilon_{5} \varepsilon_{6}+\tilde{c}_{123} \varepsilon_{1} \varepsilon_{2} \varepsilon_{3} .
\end{aligned}
$$

To experimentally determine the values of elastic constants, we apply mechanical strains along certain crystalline directions. Denoting applied strain mode by $\xi$, we rewrite the potential energy as $U / V_{0}=u(0)+P_{2} \xi^{2}+P_{3} \xi^{3}$, where the coefficients of the quadratic and the cubic terms, $P_{2}$ and $P_{3}$, are combinations of SOEC and TOEC, respectively. In the present work, six strain modes, listed in Table A1, are used in the simulations to obtain the elastic constants.

The above elastic constants are expressed in the crystal coordinate system, where $x, y$ and $z$ axes are along [100], [010] and [001] respectively. Since the elasticity of (110) and (111) films is considered here, we need to get the elastic constant in the sample coordinates of (110) and (111) films.

For (110) films, the $x, y$ and $z$ axes are set along $\left[\begin{array}{lll}1 & \overline{1} & 0\end{array}\right]$, [001] and [110] respectively. To get the elastic constant at sample coordinate, we need to rotate the crystal coordinate to the sample coordinate. The rotation matrix $\boldsymbol{T}$ is

$$
\left[\begin{array}{ccc}
-1 / \sqrt{2} & 1 / \sqrt{2} & 0 \\
0 & 0 & 1 \\
1 / \sqrt{2} & 1 / \sqrt{2} & 0
\end{array}\right] .
$$

The SOEC and TOEC at the sample coordinate system of (110) films are obtained by

$$
c_{i j k l}^{\prime}=T_{i a} T_{j b} c_{a b c d} T_{k c} T_{l d}, \quad \text { (A4a) }
$$

$$
\tilde{c}_{i j k l m n}^{\prime}=T_{i a} T_{j b} T_{k c} \tilde{c}_{a b c d e f} T_{l d} T_{m e} T_{n f}, \quad \text { (A4b) }
$$

respectively. After rotation, the SOECs at the sample coordinate are expressed as $c_{11}^{\prime}=c_{33}^{\prime}=\left(c_{11}+c_{12}+2 c_{44}\right) / 2$, $c_{22}^{\prime}=c_{11}, \quad c_{13}^{\prime}=\left(c_{11}+c_{12}-2 c_{44}\right) / 2, \quad c_{12}^{\prime}=c_{23}^{\prime}=c_{12}, \quad c_{44}^{\prime}=$ $c_{66}^{\prime}=c_{44}, c_{55}^{\prime}=\left(c_{11}-c_{22}\right) / 2$. The left 27 components of the SOEC tensor are 0 . We can see from the SOEC tensor that normal strain will not induce shear stress. Since shear strain is not under consideration, we only need $c_{i j}^{\prime}$, where $i, j=1,2,3$. The TOEC is more complicated, but we only consider $c_{i j k}^{\prime}$ where $i, j, k=1,2,3$. One can follow eq. (A4b) to derive the expression for $c_{i j k}^{\prime}$.

For (111) films, the $x, y$ and $z$ axes are set along $\left[\begin{array}{lll}\overline{1} & \overline{1} & 2\end{array}\right]$, $\left[\begin{array}{lll}1 & \overline{1} & 0\end{array}\right]$ and [111] respectively. The rotation matrix $\boldsymbol{T}$ is

<table>
<caption>Table A1 Strain modes and corresponding expression of $P_{2}, P_{3}$</caption>
<thead>
  <tr>
    <th>Strain mode</th>
    <th>$P_{2}$</th>
    <th>$P_{3}$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>$\eta _{1}=(\xi ,0,0,0,0,0)$</td>
    <td>$\frac {1}{2}c_{11}$</td>
    <td>$\frac {1}{6}\tilde {c}_{111}$</td>
  </tr>
  <tr>
    <td>$\eta _{2}=(\xi ,\xi ,0,0,0,0)$</td>
    <td>$c_{11}+c_{12}$</td>
    <td>$\frac {1}{3}\tilde {c}_{111}+\tilde {c}_{112}$</td>
  </tr>
  <tr>
    <td>$\eta _{3}=(\xi ,0,0,2\xi ,0,0)$</td>
    <td>$\frac {1}{2}c_{11}+2c_{44}$</td>
    <td>$\frac {1}{6}\tilde {c}_{111}+2\tilde {c}_{144}$</td>
  </tr>
  <tr>
    <td>$\eta _{4}=(\xi ,0,0,0,0,2\xi )$</td>
    <td>$\frac {1}{2}c_{11}+2c_{44}$</td>
    <td>$\frac {1}{6}\tilde {c}_{111}+2\tilde {c}_{155}$</td>
  </tr>
  <tr>
    <td>$\eta _{5}=(0,0,0,2\xi ,2\xi ,2\xi )$</td>
    <td>$6c_{44}$</td>
    <td>$8\tilde {c}_{456}$</td>
  </tr>
  <tr>
    <td>$\eta _{6}=(\xi ,\xi ,\xi ,0,0,0)$</td>
    <td>$\frac {3}{2}c_{11}+3c_{12}$</td>
    <td>$\frac {1}{2}\tilde {c}_{111}+3\tilde {c}_{112}+\tilde {c}_{123}$</td>
  </tr>
</tbody>
</table>

$$
\begin{bmatrix}
-1/\sqrt{6} & -1/\sqrt{6} & 2/\sqrt{6} \\
1/\sqrt{2} & -1/\sqrt{2} & 0 \\
1/\sqrt{3} & 1/\sqrt{3} & 1/\sqrt{3}
\end{bmatrix}.
$$

The SOECs at the sample coordinate of the (111) film are
$$
\begin{aligned}
& c_{11}^{\prime}=c_{22}^{\prime}=\left(c_{11}+c_{12}+2 c_{44}\right) / 2, \\
& c_{13}^{\prime}=c_{23}^{\prime}=\left(c_{11}+2 c_{22}-2 c_{44}\right) / 3, \\
& c_{33}^{\prime}=\left(c_{11}+2 c_{12}+4 c_{44}\right) / 3, \\
& c_{12}^{\prime}=\left(c_{11}+5 c_{22}-2 c_{44}\right) / 6, \\
& c_{44}^{\prime}=c_{55}^{\prime}=\left(c_{11}-c_{22}+c_{44}\right) / 3, \\
& c_{66}^{\prime}=\left(c_{11}-c_{22}+4 c_{44}\right) / 6, \\
& c_{15}^{\prime}=-\sqrt{2}\left(c_{12}-c_{11}+2 c_{44}\right) / 6, \\
& c_{25}^{\prime}=c_{46}^{\prime}=\sqrt{2}\left(c_{12}-c_{11}+2 c_{44}\right) / 6.
\end{aligned}
$$

The left 18 components are all zero. We can see that the selected sample coordinate ensures that the elastic properties along x and y directions are identical, which means that the x and y directions are elastically equivalent. Therefore we can apply biaxial loading the (111) film just like (100) film. It should be noted that $c_{15}'$ and $c_{25}'$ are not zero, which means that normal strain (or stress) might induce shear stress (or strain). However, because $c_{15}'=-c_{25}'$, when a biaxial strain $\eta_{bi}=(\xi,\xi)$ is applied to (111) film, the shear stress induced by normal strain would cancel each other and remains zero. The TOECs are too complicated to be listed. One can follow eq. (A4b) to derive the expression for $c_{ijk}'$.

The biaxial Young's modulus can be easily derived using $c_{ij}'$. Supposing that a biaxial strain $\eta_{bi}=(\xi,\xi)$ is applied to the bulk crystal and the z direction is under plane-stress condition during loading, we have $\sigma_{3}^{c}=c_{3j}'\varepsilon_{j}+\tilde{c}_{3jk}'\varepsilon_{j}\varepsilon_{k}=0$, where $\sigma_{3}^{c}$ indicates the stress along z direction; $i,j,k$=1,2,3. For simplicity, we make an approximation to ignore the nonlinear term when we derive $\varepsilon_{3}$. The two in-plane direction should have the same elastic properties so that we have $\varepsilon_{3}=-2c_{31}'/c_{33}'$. Then we can derive the biaxial stress to be
$$
\begin{aligned}
\sigma_{1}^{c}= & {\left[c_{11}^{\prime}+c_{12}^{\prime}-2\left(c_{13}^{\prime}\right)^{2} / c_{33}^{\prime}\right] \varepsilon_{1} } \\
& +\left[\tilde{c}_{111}^{\prime}+2 \tilde{c}_{112}^{\prime}+\tilde{c}_{122}^{\prime}-4 \tilde{c}_{113}^{\prime} c_{13}^{\prime} / c_{33}^{\prime}+4 \tilde{c}_{133}^{\prime}\left(c_{13}^{\prime} / c_{33}^{\prime}\right)^{2}\right] \varepsilon_{1}^{2}, \\
& \text { (A5) }
\end{aligned}
$$
where $\sigma_{1}^{c}$ is the normal stress along x direction of the bulk material. Then the first and second order biaxial Young's modulus are $Y_{bi}^{c}=c_{11}'+c_{12}'-2(c_{13}')^{2}/c_{33}'$ and $\tilde{Y}_{bi}^{c}=\tilde{c}_{111}'+2\tilde{c}_{112}'+\tilde{c}_{122}'-4\tilde{c}_{113}'c_{13}'/c_{33}'+4\tilde{c}_{133}'(c_{13}'/c_{33}')^{2}$, respectively.

### Surface elastic constants
As stated above, a thin film is treated as a composite of two surfaces and the core in between. Because the core and the surfaces are coherently attached, they subject to the same in-plane strains. From now on, the analysis is performed in the sample coordinate system. For simplicity, we use capital $C$ instead of $c'$ as the elastic constants in the sample coordinate system: $C_{ij}=c_{ij}'$, $\tilde{C}_{ijk}^{c}=\tilde{c}_{ijk}'$. As for surface elastic constants, we use the notations of $C_{ij}^{s}$ and $\tilde{C}_{ijk}^{s}$, with $i,j,k$=1,2,3. The potential energy of a thin film is the sum of the surface potential energy, $U^{c}$, and the core potential energy, $U^{s}$:
$$
U=U^{c}+U^{s}, \quad \text { (A6a) }
$$
where $U^{c}$ is given by eq. (A1) and $U^{s}$ takes the form
$$
\begin{aligned}
U^{s}=2 A\left[\gamma(0)+\sigma_{i}^{s 0} \varepsilon_{i}+\frac{1}{2!} C_{i j}^{s} \varepsilon_{i} \varepsilon_{j}+\frac{1}{3!} \tilde{C}_{i j k}^{s} \varepsilon_{i} \varepsilon_{j} \varepsilon_{k}+...\right].
\\ \text { (A6b) }
\end{aligned}
$$

In eq. (A6b), $\gamma(0)$ represents the surface energy density per unit surface area at the in-plane strain-free state and $\sigma_{i}^{s0}$ denotes the surface eigenstress along $i$ direction. At the in-plane strain-free state, no parallel relaxation has occurred yet. After parallel relaxation, the film reaches the equilibrium state with minimized potential energy, which requires
$$
\begin{aligned}
\frac{\partial U}{\partial \varepsilon_{i}} & =V_{0}\left(C_{i j}^{c} \varepsilon_{j}+\frac{1}{2} \tilde{C}_{i j k}^{c} \varepsilon_{j} \varepsilon_{k}\right)+2 A\left(\sigma_{i}^{s 0}+C_{i j}^{s} \varepsilon_{j}+\frac{1}{2} \tilde{C}_{i j k}^{s} \varepsilon_{j} \varepsilon_{k}\right) \\
& =0. \quad \text { (A7a) }
\end{aligned}
$$

Note that $V_{0}=h\cdot A$, therefore we have
$$
h\left(C_{i j}^{c} \varepsilon_{j}+\frac{1}{2} \tilde{C}_{i j k}^{c} \varepsilon_{j} \varepsilon_{k}\right)+2\left(C_{i}^{s 0}+C_{i j}^{s} \varepsilon_{j}+\frac{1}{2} \tilde{C}_{i j k}^{s} \varepsilon_{j} \varepsilon_{k}\right)=0. \text { (A7b) }
$$

Eq. (A7b) is simply the force balance equation of the core force and the surface forces,
$$
F_{i}^{c}=-2 F_{i}^{s}, \quad \text { (A7c) }
$$
with $F_{i}^{c}=h(\sigma_{ij}^{c}\varepsilon_{j}+1/2\tilde{C}_{ijk}^{c}\varepsilon_{j}\varepsilon_{k})$ and $F_{i}^{s}=\sigma_{i}^{s0}+C_{ij}^{s}\varepsilon_{j}$ $+1/2\tilde{C}_{ijk}^{s}\varepsilon_{j}\varepsilon_{k}$.

To extract the value of surface elastic constant, we apply in-plane strain in the simulations according to the following strain modes and fit the simulation data with the force balance equation. After normal relaxation, the thin film satisfies the plane-stress condition along the thickness direction. Because the core and surface are adhered to each other, they would have the same in-plane strain at any moment. The relaxation induced in-plane strain is called the initial equilibrium strain that satisfies the force balance equation. For

<table><thead><tr><td><b>Table A2 Core force under particular strain mode</b></td><td></td></tr><tr><td><b>Strain mode</b></td><td><b>Core force</b></td></tr></thead><tbody><tr><td><b>$η_{1}=(ξ,0)$</b></td><td><b>$F_{x}^{c}=-2[σ_{x}^{s0}+C_{11}^{s}ε_{1}+1/2\overline {C}_{111}^{s}ε_{1}^{2}]$</b></td></tr><tr><td><b>$η_{2}=(0,ξ)$</b></td><td><b>$F_{y}^{c}=-2[σ_{y}^{s0}+C_{22}^{s}ε_{2}+1/2\overline {C}_{222}^{s}ε_{2}^{2}]$</b></td></tr><tr><td><b>$η_{3}=(ξ,ξ)$</b></td><td><b>$F_{x}^{c}=-2[σ_{x}^{s0}+(C_{11}^{s}+C_{12}^{s})ε_{3}+1/2(\overline {C}_{111}^{s}+\overline {C}_{122}^{s}+2\overline {C}_{112}^{s})ε_{3}^{2}]$</b></td></tr><tr><td><b>$η_{4}=(ξ,ξ)$</b></td><td><b>$F_{y}^{c}=-2[σ_{y}^{s0}+(C_{22}^{s}+C_{12}^{s})ε_{4}+1/2(\overline {C}_{112}^{s}+\overline {C}_{222}^{s}+2\overline {C}_{122}^{s})ε_{4}^{2}]$</b></td></tr></tbody></table>

simplicity, we use different strain modes for the (110) and (111) films and denote the initial equilibrium strain under strain mode $\eta_{n}$ by $\varepsilon_{n}$ .

The core force, $F_{x}^{c}$ and $F_{y}^{c}$ , can be easily calculated with the initial equilibrium strain and the bulk elastic constants. The surface eignestress and surface elastic constants are then obtained by fitting the force balance equation. After this, the second and third order elastic constants of the surface can be calculated. Due to the symmetry of FCC (100) and (111) films, we use the biaxial loading mode, $\eta_{b i}=(\xi, \xi)$ and have the force balance equation
$$
\begin{array}{r}
F^{c}=-2\left[\sigma^{s 0}+\left(C_{11}^{s}+C_{12}^{s}\right) \varepsilon_{b i}+1 / 2\left(\tilde{C}_{111}^{s}+\tilde{C}_{122}^{s}+2 \tilde{C}_{112}^{s}\right) \varepsilon_{b i}^{2}\right], \\
(\mathrm{A} 8 \mathrm{a})
\end{array}
$$
where $\varepsilon_{b i}$ denotes the initial biaxial strain. The first and second order surface biaxial Young's moduli are given by $Y_{b i}^{s}=C_{11}^{s}+C_{12}^{s}$ and $\tilde{Y}_{b i}^{s}=1 / 2(\tilde{C}_{111}^{s}+\tilde{C}_{122}^{s}+2 \tilde{C}_{112}^{s})$ . The force balance equation can be rewritten as
$$F^{c}=-2\left[\sigma^{s 0}+Y_{b i}^{s} \varepsilon_{b i}+\tilde{Y}_{b i}^{s} \varepsilon_{b i}^{2}\right]. \quad \text { (A8b) }$$

### Nominal Young's moduli
The normal direction of the film, i.e., z direction is under plane-stress condition in the present study. For FCC (110) films, we choose pseudo uniaxial Young's modulus to demonstrate the size-effect of elastic properties of thin films. Unlike traditional uniaxial loading which applies loading along one direction with two other direction surfaces traction-free, here we adopt a fixed dimension pseudo uniaxial loading to simplify the mathematical derivation. For example, if we apply strain along x direction of the (110) film, then the y dimension is fixed. This loading corresponds to the strain mode $\eta_{1}=(\xi, 0)$ . For the strain mode $\eta_{1}=(\xi, 0)$ , the total force along x direction is
$$
\begin{aligned}
F_{x}= & F_{x}^{c}+2 F_{x}^{s}=\left\{\left[C_{11}^{c}-\left(C_{13}^{c}\right)^{2} / C_{33}^{c}\right] \xi\right. \\
& \left.+\frac{1}{2}\left[\tilde{C}_{111}^{c}+\tilde{C}_{133}^{c}\left(C_{13}^{c} / C_{33}^{c}\right)^{2}-\tilde{C}_{113}^{c} C_{13}^{c} / C_{33}^{c}\right] \xi^{2}\right\} h \\
& +2 C_{11}^{s} \xi+\tilde{C}_{111}^{s} \xi^{2}.
\end{aligned}
$$

We introduce the core first-order pseudo uniaxial Young's modulus
$$Y_{x}^{c}=C_{11}^{c}-\left(C_{13}^{c}\right)^{2} / C_{33}^{c}, \quad \text { (A10a) }$$
and the core second-order pseudo uniaxial Young's modu- lus as
$$\tilde{Y}_{x}^{c}=1 / 2\left[\tilde{C}_{111}^{c}+\tilde{C}_{133}^{c}\left(C_{13}^{c} / C_{33}^{c}\right)^{2}-\tilde{C}_{113}^{c} C_{13}^{c} / C_{33}^{c}\right]. \quad \text { (A10b) }$$

Regarding surface, we have the surface first-order pseu- do uniaxial Young's modulus as
$$Y_{x}^{s}=C_{11}^{s}, \quad \text { (A11a) }$$
and the surface second-order pseudo uniaxial Young's modulus as
$$\tilde{Y}_{x}^{s}=\frac{1}{2} \tilde{C}_{111}^{s}. \quad \text { (A11b) }$$

Then, we rewrite the force along x direction with y di- mension fixed,
$$F_{x}=\left(Y_{x}^{c} \xi+\tilde{Y}_{x}^{c} \xi^{2}\right) h+2\left(Y_{x}^{s} \xi+\tilde{Y}_{x}^{s} \xi^{2}\right), \quad \text { (A12a) }$$
or the nominal stress
$$\sigma_{x x}^{n}=\left(Y_{x}^{c} \xi+\tilde{Y}_{x}^{c} \xi^{2}\right)+2\left(Y_{x}^{s} \xi+\tilde{Y}_{x}^{s} \xi^{2}\right) / h. \quad \text { (A12b) }$$

From the nominal stress, we have the nominal Young's modulus at any strain $\varepsilon_{x}$ 
$$\bar{Y}_{x}^{n}=Y_{x}^{c}+2 \tilde{Y}_{x}^{c} \varepsilon_{x}+2\left(Y_{x}^{s}+2 \tilde{Y}_{x}^{s} \varepsilon_{x}\right) / h. \quad \text { (A13) }$$

If the strain $\varepsilon_{x}$ is the initial equilibrium strain under strain mode $\eta_{1}$ , its value can be determined from the force balance equation, i.e., eq. (A12a) or eq. (A12b) equals zero, which gives
$$\varepsilon_{x}^{i n i}=\frac{-\left(h Y_{x}^{c}+2 Y_{x}^{s}\right)+\sqrt{\left(h Y_{x}^{c}+2 Y_{x}^{s}\right)^{2}-8 \sigma_{x}^{s 0}\left(h \tilde{Y}_{x}^{c}+2 \tilde{Y}_{x}^{s}\right)}}{2\left(h \tilde{Y}_{x}^{c}+2 \tilde{Y}_{x}^{s}\right)}.$$

Replacing the subscript " x " with " y " eqs. (A13) and (A14) gives the nominal Young's modulus at any strain $\varepsilon_{y}$ and the initial equilibrium strain, $\varepsilon_{y}^{i n i}$ .

Similarly, the biaxial nominal Young's modulus under any strain and the initial equilibrium strain for FCC (111) and (100) films are given, respectively by
$$\bar{Y}_{b i}^{n}=Y_{b i}^{c}+2 \tilde{Y}_{b i}^{c} \varepsilon_{b i}+2\left(Y_{b i}^{s}+2 \tilde{Y}_{b i}^{s} \varepsilon_{b i}\right) / h. \quad \text { (A15a) }$$

$$
\varepsilon_{b i}^{i n i}=\frac{-\left(h Y_{b i}^{c}+2 Y_{b i}^{s}\right)+\sqrt{\left(h Y_{b i}^{c}+2 Y_{b i}^{s}\right)^{2}-8 \sigma_{b i}^{s 0}\left(h \tilde{Y}_{b i}^{c}+2 \tilde{Y}_{b i}^{s}\right)}}{2\left(h \tilde{Y}_{b i}^{c}+2 \tilde{Y}_{b i}^{s}\right)}.
$$
(A15b)
# Carbon Dioxide Adsorption-Induced Deformation of Microporous Carbons

Piotr Kowalczyk,*,† Sylwester Furmaniak,‡ Piotr A. Gauden,‡ and Artur P. Terzyk‡

Applied Physics, RMIT University, GPO Box 2476 V, Victoria 3001, Australia, and
Department of Chemistry, Physicochemistry of Carbon Materials Research Group,
N. Copernicus University, Gagarin St. 7, 87-100 Torun, Poland

Received: December 19, 2009; Revised Manuscript Received: February 10, 2010

Applying the thermodynamic model of adsorption-induced deformation of microporous carbons developed recently (Kowalczyk, P.; Ciach, A.; Neimark, A. *Langmuir* **2008**, *24*, 6603), we study the deformation of carbonaceous amorphous porous materials due to adsorption of carbon dioxide at 333 K and pressures up to 27 MPa. The internal adsorption stress induced by adsorbed/compressed carbon dioxide is very high in the smallest ultramicropores (for instance, solvation pressure in 0.23 nm ultramicropore reaches 3.2 GPa at 27 MPa). Model calculations show that any sample of carbonaceous porous solid containing a fraction of the smallest ultramicropores with pore size below 0.31 nm will expand at studied operating conditions. This is because the high internal adsorption stress in ultramicropores dominates sample deformation upon adsorption of carbon dioxide at studied operation conditions. Interestingly, the nonmonotonic deformation (i.e., initial contraction and further expansion) of the above mentioned porous materials upon adsorption of carbon dioxide at 333 K is also theoretically predicted. Our calculations reproduce quantitatively the strain isotherm of carbon dioxide on carbide-derived activated carbon at 333 K and experimental pressures up to 2.9 MPa. Moreover, we extrapolate adsorption and strain isotherms measured by the gravimetric/dilatometric method up to 27 MPa to mimic geosequestration operating conditions. And so, we predict that expansion of the studied carbon sample reaches 0.75% at 27 MPa and 333 K. Presented simulation results can be useful for the interpretation of the coal deformation upon sequestration of carbon dioxide at high pressures and temperatures.

## 1. Introduction

Understanding the adsorption-induced deformation of microporous solids (e.g., activated carbons, charcoals, and coals) is one of the long-standing problems in adsorption science and catalysis. The first studies on charcoal swelling were published by Bangham¹ and Fakhoury in 1928, followed by the precise measurements of carbon contraction and expansion performed by Haines and McIntosh.² In the recent years, Tvardovskiy and co-workers³⁻⁷ have reported a series of precise dilatometric experiments of activated carbon deformation upon adsorption of various gases, including argon, methane, nitrogen, and carbon dioxide, at different temperatures.

It is assumed that carbonaceous porous solids consist of disordered arrays of slit-shaped pores embedded in an amorphous matrix.⁸⁻¹² The solid−fluid interaction potential in the smallest carbon pores is very high, and it is responsible for high compression of guest molecules.¹³⁻²⁰ Thus, packing/compression of molecules adsorbed in lower dimensional carbon pores can be very different in comparison to the bulk phase.²¹⁻³⁰ It is welldocumented that the resulting additional force, known as a solvation or structural one,³¹ is closely connected with adsorption-induced deformation of porous solids.³²⁻⁴⁰ The oscillatory solvation force is responsible for a significant adsorption stress on the order of GPa.³²⁻⁴⁰ For a single slit-shaped carbon pore, this internal adsorption stress may be either positive or negative, depending on the interplay of adsorption and confining effects, and it causes either contraction or swelling, respectively.³²⁻⁴⁰ Real porous carbons/coals are heterogonous solids consisting of pores of different sizes, including very small ultramicropores (pore width below 0.7 nm) and micropores (pore width below 2 nm) according to IUPAC classification.⁴¹ Thus, as has been recently suggested by Kowalczyk et al.,³⁷ the observed isotropic expansion of amorphous porous materials can be treated as a superposition of adsorbed-induced deformations of individual stacks of slit-shaped pores.

Mechanical properties of porous carbonaceous solids are critically important for various technological applications.⁸,⁹ Among them, the geosequestration of carbon dioxide has been currently extensively investigated.⁴²⁻⁴⁷ The sequestration of carbon dioxide in geologic formations (e.g., depleted oil and gas fields, saline formations, and unmineable coal seams) needs further research to clarify the microscopic mechanism of adsorption-induced swelling/shrinkage.⁴²⁻⁴⁷ Injected millions of tons of carbon dioxide produce an internal adsorption stress that both deforms a carbonaceous matrix and causes large permeability change. Deep understanding of adsorption-induced deformation of carbonaceous materials upon the loading of carbon dioxide seems to be very important because sequestrated fluid leakage poses local risks to other resources, potable groundwater, vegetation, and animal life, and to human health, notwithstanding the global aspect of the return of carbon dioxide to the atmosphere, even if it is at acceptable levels. Moreover, it is well-documented that deformation of pore channels during injection of carbon dioxide affects the coal bed methane recovery and lowers the amount of sequestrated fluid.⁴²⁻⁴⁷

* To whom correspondence should be addressed. Telephone: +61 (03) 99252571. Fax: +61 (03) 99255290. E-mail: piotr.kowalczyk@rmit.edu.au.
† RMIT University.
‡ N. Copernicus University.

10.1021/jp911996h © 2010 American Chemical Society
Published on Web 02/25/2010

Deformation of Microporous Carbons

There were a few attempts to describe adsorption-induced deformation on the basis of phenomenological thermodynamics. $^{3}$ To best our knowledge, the most successful approaches to analyzing the adsorption-induced deformation of porous solids collected by dilatometric experiments were based on density functional theory, $^{32,33}$ computer simulation, $^{37-40}$ and thermodynamics of vacancy solution. $^{48}$ In particular, density functional theory $^{32,33}$ and computer simulation $^{37-40}$ have been instrumental in describing adsorption-induced deformation in ordered and disordered porous materials such as zeolites, MCM-41 silica, and activated carbons.

The aim of the present paper is to study the microscopic mechanism of adsorption-induced deformation of porous carbonaceous materials upon adsorption of carbon dioxide at 333 K and high pressures. We want to answer the following questions: (1) *Why do carbonaceous solids consisting of very small ultramicropores swell during adsorption of supercritical carbon dioxide at high pressures?* (2) *What is the magnitude of this adsorption-induced sample deformation?* To answer these questions, we use and further explore thermodynamic approach developed in ref 37. As previously, we employ Monte Carlo simulations to compute the adsorption stress in slit-shaped carbon pores of various sizes. Next, we use a microscopic model of adsorption-induced deformation to explain the expansion of an activated carbon sample upon adsorption of carbon dioxide at 333 K studied in ref 6. Finally, we predict adsorption and strain isotherms of carbon dioxide on a studied sample of carbide-derived activated carbon at pressures up to 27 MPa in accord to mimic geosequestration operating conditions.

### 2. Theory of the Elastic Stress in Microporous Carbons

As previously, we represent the carbon sample as a macroscopically isotropic disordered three-dimensional medium composed of stacks of slit-shaped pores of various sizes embedded in an amorphous matrix. $^{37}$ We assume that the carbon matrix is incompressible and it transfers the adsorption stress isotropically. This assumption arises from the observation that stacks of slit-shaped pores embedded in the amorphous carbon matrix are randomly oriented. $^{8,9}$ Following our previous study, the volumetric strain measured in dilatometric experiments is given by $^{37}$

$$
\varepsilon=\frac{\varphi}{k}\left[\bar{\sigma}_{\mathrm{s}}-p\right] \quad(1)
$$

In the above equation, the effective adsorption stress and bulk modulus are, respectively, expressed by $^{37}$

$$
\bar{\sigma}_{\mathrm{s}}=\frac{\int H \sigma_{\mathrm{s}}(H, p) S(H) \mathrm{d} H}{\int H S(H) \mathrm{d} H} \quad(2)
$$

$$
K=\frac{k}{\varphi} \quad(3)
$$

Here, $\varphi$ denotes porosity, $k$ denotes the elastic modulus, $S(H)$ is the surface area of pores of width $(H, H+\mathrm{d} H)$, and $\sigma_{\mathrm{s}}(H, p)$ is the adsorption stress in a single slit-shaped pore of width $H$.

In order to calculate the volumetric strain given by eq 1, one has, first of all, to compute the adsorption stress in individual slit-shaped carbon pores and next to average this stress with the pore size distribution function. $^{37}$

<table>
<caption>TABLE 1: Parameters Used for Modeling of Carbon-Dioxide−Carbon-Dioxide Interactions:⁵³ σff and εff/kb Denote Lennard−Jones Collision Diameter and Well Depth, Respectively, kb is the Boltzmann Constant, loo Denotes Distance between Oxygen Atoms, and q Represents Point Charges Attached to Carbon and Oxygen Atoms</caption>
<thead>
  <tr>
    <th></th>
    <th>σff (nm)</th>
    <th>εff/kb (K)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>carbon dioxide</td>
    <td>C: 0.2824<br>O: 0.3026</td>
    <td>C: 28.68<br>O: 82.0</td>
  </tr>
  <tr>
    <td>loo (nm)</td>
    <td colspan="2">O−O: 0.2324</td>
  </tr>
  <tr>
    <td>q (e)</td>
    <td colspan="2">C: 0.664<br>O: −0.332</td>
  </tr>
</tbody>
</table>

We compute the adsorption stress in individual slit-shaped pores from $^{32,37}$

$$
\sigma_{\mathrm{s}}(H, p)=-\left.\frac{\partial \Omega_{\mathrm{p}}(H)}{\partial H}\right|_{T, p} \quad(4)
$$

In the above equation, $\Omega_{\mathrm{p}}(H, p, T)$ denotes the grand thermodynamic potential per unit surface area at the studied pressure and temperature. This method requires the thermodynamics integration along the simulated isotherm to compute the grand thermodynamic potential and, subsequently, the differentiation of the grand thermodynamic potential with respect to $H.^{32,37}$

$$
\Omega_{\mathrm{p}}(\mu, T)=\Omega_{\mathrm{p}}\left(\mu_{\mathrm{r}}, T\right)-\int_{\mu_{\mathrm{r}}}^{\mu} N \mathrm{~d} \mu \quad(5)
$$

$$
\sigma_{\mathrm{s}}(H, \mu)=k_{\mathrm{b}} T \frac{\partial N\left(\mu_{\mathrm{r}}\right)}{\partial H}+\int_{\mu_{\mathrm{r}}}^{\mu} \frac{\partial N}{\partial H} \mathrm{~d} \mu \quad(6)
$$

Here, $N(H, T, \mu)$ is the number of adsorbed molecules per surface area in the pore of width $H$ at the given environmental conditions, chemical potential $\mu$, and temperature $T$. The grand potential and solvation pressure were calculated from eqs 5 and 6 by thermodynamic integration along the isotherm starting from a reference ideal gas state at a sufficiently low vapor pressure, $\Omega_{\mathrm{p}}(\mu_{\mathrm{r}}, T)=-k_{\mathrm{b}} N(\mu_{\mathrm{r}}) T$. Details connected with derivations of eqs $1-6$ are given elsewhere. $^{37}$

### 3. Simulation Methodology

#### 3.I. Fluid−Fluid Interaction Potential.
We model carbon dioxide as an atomistic rigid linear molecule. In the atomistic simulations, we express the intermolecular potential between two carbon dioxide molecules $A$ and $B$ as a sum of site−site terms, $^{49-52}$

$$
U^{A, B}(\mathbf{q})=\sum_{i=1}^{3} \sum_{j=1}^{3} u_{i j}\left(r_{i j}^{A, B}\right) \quad(7)
$$

where the sum is taken over all sites $i$ of the molecule $A$ and sites $j$ of the molecule $B$, $\mathbf{q} \equiv\left\{\mathrm{r}_{i}^{A}-\mathrm{r}_{i}^{B}\right\}_{i, j=1,2,3}$ is the set of separations between each atom in molecule $A$ and each atom in molecule $B$, $r_{i j}^{A, B}=\left\|\mathrm{r}_{i}^{A}-\mathrm{r}_{j}^{B}\right\|$ is the distance between two sites $i$ and $j$ on molecules $A$ and $B$, respectively, and $u_{i j}(r)$ denotes distance dependent site−site interaction potential.

![](./images/811802196004831232_1.jpg)

Figure 1. Reproduction of experimental equation of state for carbon dioxide⁶⁷ at 333 K (solid line) by a three-center atomistic model of carbon dioxide with two sets of parameters taken from Potoff and Siepmann⁵⁶ (black circles) and Nguyen⁵³ (open circles).

Depending on the type of site, $u_{ij}(r)$ is given by a pairwise dispersion or electrostatic interaction energy. We assume that the dispersion energy of interaction is given by the (12,6) Lennard−Jones equation⁴⁹,⁵⁰

$$
u_{i j}^{A, B}=4 \varepsilon^{A, B}\left[\left(\frac{\sigma^{A, B}}{r_{i j}^{A, B}}\right)^{12}-\left(\frac{\sigma^{A, B}}{r_{i j}^{A, B}}\right)^{6}\right] \tag{8}
$$

The parameters of the potential for all investigated molecules, that is, $\sigma^{A,B}$ and $\sigma^{A,B}$, are taken from force field developed by Nguyen⁵³ (see Table 1).

We model electrostatic force via the Coulomb law of electrostatic potential⁴⁹,⁵⁰

$$
u_{i, j}^{A, B}=\frac{1}{4 \pi \varepsilon_{0}} \frac{q_{i}^{A} q_{j}^{B}}{r_{i j}^{A, B}} \tag{9}
$$

where $\varepsilon_{0}$ is the permittivity of free space ($\varepsilon_{0}=8.85419 \times 10^{-12}$ C² N⁻¹ m⁻²), $q_{i}^{A}$ denotes the value of the point charge $i$ on molecule $A$, $q_{j}^{B}$ denotes the value of the point charge $j$ on molecule $B$, $r_{ij}^{A,B}$ is the distance between two charges $i$ and $j$ on molecules $A$ and $B$, respectively. The values of the point charges are taken from the force field developed by Nguyen⁵³ (see Table 1).

3.II. Solid−Fluid Interaction Potential. The total carbon−carbon dioxide−carbon interaction potential is a superposition of potentials exerted by opposing walls,

$$
U_{\mathrm{sf}}^{A}(\mathbf{q})=\sum_{i=1}^{3}\left[U_{\mathrm{s}}\left(z_{i}^{A}\right)+U_{\mathrm{s}}\left(H-z_{i}^{A}\right)\right] \tag{10}
$$

where the sum is taken over all sites $i$ of molecule $A$, $\mathbf{q} \equiv \{z_{i}^{A}, H - z_{i}^{A}\}_{i=1,2,3}$ is the set of separations between each atom in molecule $A$ and pore walls, and $H$ denotes the slit-shaped carbon pore width.

The potential $U_{s}(x)$ is modeled by the 10-4-3 potential,⁵⁴,⁵⁵

$$
U_{\mathrm{s}}(x)=2 \pi \rho_{\mathrm{s}} \varepsilon_{\mathrm{sf}} \sigma_{\mathrm{sf}}^{2} \Delta\left[\frac{2}{5}\left(\frac{\sigma}{x}\right)^{10}-\left(\frac{\sigma}{x}\right)^{4}-\left(\frac{\sigma_{\mathrm{sf}}^{4}}{3 \Delta(x+0.61 \Delta)^{3}}\right)\right]_{(11)}
$$

where $\rho_{\mathrm{s}}=114 \mathrm{~nm}^{-3}$ is the density of carbon atoms, $\Delta=0.335$ nm denotes the distance between sheets of carbons, and $\sigma_{\text{sf}}$ and $\varepsilon_{\text{sf}}$ denote Lennard−Jones solid−fluid collision diameter and well depth, respectively. The parameters of the solid−fluid potential were calculated from the Lorentz−Berthelot mixing rule. For carbon, we adopted the following parameters:⁵⁴ $\sigma_{\text{ss}}=$ 0.34 nm and $\varepsilon_{\text{ss}}/k_{\text{b}}=28$ K.

3.III. Simulation Details. The adsorption isotherms were computed by the grand canonical Monte Carlo method (GCMC).⁴⁹,⁵⁰ We adopted the standard setup for GCMC simulation of adsorption in slit-shaped pore geometry, that is, cubic simulation box of size $4 \mathrm{~nm} \times 4 \mathrm{~nm} \times H$ with periodic boundary conditions and minimum image convention for computing molecular interactions in $x$ and $y$ directions.⁴⁹,⁵⁰ The grand canonical ensemble simulations utilized $5 \times 10^{7}$ configurations; the first $2.5 \times 10^{7}$ configurations were discarded to guarantee equilibration. Then 60 adsorption isotherms of carbon dioxide at 333 K and pressures from 1 $\times 10^{-6}$ to 27 MPa were computed. All simulated adsorption isotherms of carbon dioxide consisted of 85 points and covered the range of pore sizes, $H_{\text{eff}} \in [0.19,4.7]$ nm, where $H_{\text{eff}}=H-0.34$ nm. The thermodynamic integration was performed according to eq 6 with an ideal gas as a reference state.³⁷

![](./images/811802196004831232_2.jpg)

Figure 2. Variation of absolute value of adsorption (upper panel) and solvation pressure (bottom panel) of carbon dioxide in a series of slit-shaped carbon pores (an effective pore width, $H_{\text{eff}}=H-0.34$ nm, is displayed on the plots) at 333 K. The solid blue line on the upper panel corresponds to bulk carbon dioxide at 333 K.⁶⁷

![](./images/811802196004831232_3.jpg)

Figure 3. Histogram describing the orientation of adsorbed carbon dioxide molecules in selected slit-shaped carbon pores, $H_{eff}$: 0.23 (bottom panel), 0.36 (middle panel), and 0.535 nm (upper panel). The values of external pressures are given in each panel. Note that parallel and perpendicular orientation of carbon dioxide molecules to the pore walls corresponds to $\alpha = 0^\circ$and $\alpha = 90^\circ$, respectively.

### 3.IV. Packing of Carbon Dioxide in Carbon Slit-Shaped
Pores. Packing of linear carbon dioxide molecules in slit-shaped carbon pores is essential for microscopic understanding of adsorption-induced deformation of both single pores as well as real samples of porous materials. $^{32-40}$

To determine the packing/compression of adsorbed phases in the studied pore geometry, we compute the absolute value of adsorption from the following formula

$$
\Gamma_{\text{abs}} = \langle N \rangle / V \tag{12}
$$

where $\langle N \rangle$ is the ensemble average of the number of carbon dioxide molecules in the simulation box of volume $V = L_xL_yH_{\text{eff}}$.

![](./images/811802196004831232_4.jpg)

Figure 4. Solvation pressures of carbon dioxide at 333 K versus slit-shaped carbon pore size computed for bulk pressures from 0.03 to 27 MPa. Maximum solvation pressures correspond to slit-shaped carbon pore width of 0.23 nm, and minimum is found in pores of pore width of 0.36 nm. Note the high solvation pressures in the smallest ultramicropores of pore width lower 0.315 nm.

![](./images/811802196004831232_5.jpg)

Figure 5. Theoretical pore volume distributions used for the investigation of adsorption-induced deformation of microporous activated carbon upon carbon dioxide adsorption at 333 K. For all considered model samples of activated carbons, we assume the total pore volume of 0.47 cm³/g.

The orientation of adsorbed carbon dioxide molecules in the studied pore geometry is described by the angle between the axis of the molecule and the wall plane as follows

$$
\alpha = \arccos\left( \frac{\sqrt{(x_{O'} - x_{O''})^2 + (y_{O'} - y_{O''})^2}}{\sqrt{(x_{O'} - x_{O''})^2 + (y_{O'} - y_{O''})^2 + (z_{O'} - z_{O''})^2}} \right) \tag{13}
$$

where $\{x_{O'},y_{O'},z_{O'}\}$ and $\{x_{O''},y_{O''},z_{O''}\}$ denotes Cartesian coordinates of oxygen atoms of adsorbed carbon dioxide molecules.

![](./images/811802196004831232_6.jpg)

Figure 6. Adsorption-induced deformation curves of carbon dioxide at 333 K computed on the basis of pore volume distributions displayed in Figure 5. The assumed bulk modulus K is 20 GPa (circles), 30 GPa (squares), 40 GPa (triangles), and 50 GPa (tilted squares).

Parallel and perpendicular orientation of carbon dioxide mol- ecules to the pore walls corresponds to $\alpha = 0^{\circ}$ and $\alpha = 90^{\circ}$, respectively.

## 4. Results and Discussion
### 4.I. Isotherms of Carbon Dioxide and Solvation Pressure in Individual Pores.
The accuracy of computer simulations strongly depends on the applied force field. Here, we study the thermodynamic properties of carbon dioxide adsorbed in slit- shaped carbon pores of molecular dimensions at 333 K and high pressures. Thus, the validation of the applied force field against known experimental data is necessary. As one can see from Figure 1, the force filed proposed by Nguyen⁵³ reproduces experimental data reasonably well. In contrast, the TraPPE force field developed by Potoff and Siepmann⁵⁶ correctly reproduces the experimental density of carbon dioxide for pressures below 10 MPa. It is not surprising if one takes into account that Nguyen adjusted force field parameters to correctly reproduce the experimental equation of state for carbon dioxide at high pressures and temperatures.⁵³ It has been shown that the TraPPE force field correctly reproduces the gas−liquid coexistence data for carbon dioxide;⁵⁶ however, as we show here, this model systematically underpredicts the experimental density of carbon dioxide at 333 K and pressures above 10 MPa. That is why in all conducted simulations we represent the carbon dioxide molecule with a three-center model with the force filed proposed by Nguyen.

The impact of the pore size on adsorption and solvation pressure is crucial for understanding the adsorption-induced deformation at an atomistic level. When the attraction between pore walls and adsorbed fluid molecules is strong enough, dense solidlike/compressed liquidlike layers of fluid are formed in the pores. As a result, the repulsive solvation force is induced. However, when the packing of fluid molecules in confined geometry is imperfect, the attractive solvation force is generated. Carbon dioxide is strongly adsorbed in slit-shaped carbon pores at studied operating conditions, as is presented in Figure 2. The simulated adsorption isotherms exhibit type I behavior according to IUPAC classification.⁴¹ Regardless the value of the external pressure, carbon dioxide molecules adsorbed in very small pores lay flat on the pore walls, as is shown in Figure 3. Clearly, parallel orientation of adsorbed molecules to the pore walls maximizes the adsorbate−adsorbent dispersion interactions. The computed solvation force is very high in the smallest ultrami- cropores because of high adsorption and compression of adsorbed carbon dioxide molecules, as is presented in Figures 2 and 4. As an example, the solvation pressure in a 0.23 nm ultramicropore reaches 3.2 GPa at 27 MPa. Further expansion of the pore size results in fast reduction of the solvation force, as is displayed in Figures 2 and 4. As pore size reaches 0.31 nm, solvation force crosses zero and is further negative. Microscopic configurations of adsorbed carbon dioxide in 0.35−0.37 nm ultramicropores show imperfect packing of adsorbed molecules (see Figure 3 and movie in the Supporting Information). As expected, adsorbed molecules tend to maximize their contact with the pore walls; however, as pore size increases, other orientations of adsorbed carbon dioxide molecules impact the magnitude of the solvation force, as is presented in Figures 2−4. Near a pore size of 0.54 nm, we observe secondary maximum of solvation force. Due to the high temperature ($T =$ 333 K), the secondary maximum as well as pore size dependence of the solvation pressure is rapidly damped, as is shown in

![](./images/811802196004831232_7.jpg)

Figure 7. Dependence of the deformation of carbide-derived activated carbon on the carbon dioxide adsorption at 333 K measured by the dilatometric method (open circles on upper panel)³·⁶ and computed from the proposed thermodynamic model (solid line on upper panel). Dashed line in the upper panel shows extrapolation of the strain isotherm up to 27 MPa. Bottom panel presents the comparison between the experimental adsorbed amount of carbon dioxide at 333 K (open circles)³·⁶ and that predicted from the thermodynamic model of adsorption-induced deformation of microporous solids.³⁷

Figure 4. Compression of the supercritical carbon dioxide in pores of above 1.3 nm at considered external conditions is negligible.

4.II. Analysis of Adsorption-Induced Deformation in Microporous Carbon: Carbon Dioxide. Adsorption-induced deformation of heterogeneous carbons can be easily predicted from assumed pore size distribution and bulk modulus. As previously, we model pore size distribution by the Gaussian functions,³⁷ (see Figure 5). The corresponding deformation curves of carbon dioxide at 333 K are shown in Figure 6. Clearly, the internal pore structure greatly impacts the deformation curves, since the solvation pressure is strongly affected by the size of the carbon pores. Interestingly, we predict both monotonic and nonmonotonic shapes of deformation curves due to adsorption of carbon dioxide at the studied operating conditions. For samples 1−3, we observe expansion in the whole range of pressures. This is because the assumed pore size distributions corresponding to counted carbon samples contain a fraction of the smallest ultramicropores with pore size below 0.31 nm. The great excess of the pore pressure computed for the smallest ultramicropores causes the porous solid to swell and the bulk modulus controls the extent of expansion, as is displayed in Figure 6. It is worth underlining that, for the investigated values of bulk modulus, the maximum theoretical expansion of the carbon sample due to adsorption of carbon dioxide at 333 K and 27 MPa is around 4.2%. The deformation curve computed for sample 4 is very interesting. It is important to note that this sample of porous carbon contains only wider pores above 0.4 nm (i.e., we cut the smallest ultramicropores characterized by high positive solvation force). The shape of the deformation curve computed for sample 4 is nonmonotonic with an initial contraction and further expansion, as is presented in Figure 6. This nonmonotonic shape of the deformation curve can be easily explained by the fact that assumed pore size distribution is composed of a mixture of wider micropores.³⁷ Micropores with positive solvation force tend to expand to reduce the internal adsorption stress. In contrast, micropores with negative solvation force tend to contract. Note, however, that the magnitude of deformation computed for sample 4 is lower in comparison to all remaining studied samples of porous carbon. A further shift of the pore size distribution to the wider range of pore sizes results in complete exclusion of adsorption- induced deformation because adsorbed carbon dioxide does not procure any adsorption stress. We may therefore conclude that a real sample of heterogeneous porous carbon/coal should expand upon adsorption of carbon dioxide at 333 K and high pressures. This is because real porous carbons/coals contain some fraction of the smallest ultramicropores⁸·⁹·⁵⁷ that dominate deformation induced by adsorbed/compressed carbon dioxide at studied operation conditions (see Figures 4−6).

![](./images/811802196004831232_8.jpg)

Figure 8. Pore volume distribution of carbide-derived activated carbon computed from experimental deformation-pressure dependence pre- sented in Figure 7.

4.III. Comparison with Experimental Data. The simulation model was employed to describe the experimental data collected on a carbide-derived activated carbon during carbon dioxide adsorption at 333 K characterized by the micropore volume $W_0 = 0.47\ \text{cm}^3/\text{g}$, and the characteristic energy of adsorption $E_0 = 30\ \text{kJ/mol}$.³·⁶ The high value of the characteristic energy of adsorption indicates the presence of ultramicropores in the studied sample of activated carbon. Here, we want to underline that high quality carbide-derived activated carbon is composed of stacks of slit-shaped pores of various sizes embedded in an amorphous matrix.³⁻⁷·⁵⁸⁻⁶² Deformation curves collected by dilatometric experiment cover the range of pressures up to 2.9 MPa.³·⁶ The proposed model reproduces the monotonic behavior of the experimental dilatometric curve reasonably well, as is displayed in Figure 7. The studied sample of activated carbon expands up to 0.2% at 2.9 MPa and 333 K. The predicted bulk modulus of the investigated carbide-derived activated carbon is 12 GPa. This value is comparable with the reported data for vitreous carbons⁶³ and polycrystalline graphite.⁶⁴·⁶⁵ Moreover, our previous estimation of bulk modulus of 7 GPa for carbide-

derived activated carbon from an argon dilatometric experiment at 243 K is close to the current prediction.³⁷ The pore size distribution was determined to provide the best fit with the experimental deformation-pressure dependence. As expected, the computed pore size distribution is complex with a mixture of small and wider pores, as is shown in Figure 8. However, as we show in the previous paragraph, the presence of the smallest ultramicropores is responsible for the experimentally measured expansion of the studied carbon at given operating conditions. One great advantage of the microscopic model of adsorption-induced deformation is its ability to extrapolate dilatometric experiment to different operating conditions. Knowing the pore size distribution and bulk modulus of the investigated porous carbon, we compute adsorption and strain isotherms up to 27 MPa. Here, we want to point out that the assumed linear stress−strain relation is justified by the fact that the strain measured for microporous materials (e.g., zeolites, activated carbons) is small, typically in fractions of a percent.³ That is why we expected that for the studied activated carbon the linear Hooke law should hold at higher pressures. As pointed by Neimark et al.,⁶⁶ it is not true for adsorption-induced deformation (e.g., breathing and gate opening) of flexible metal−organic frameworks. In Figure 7, we compare the experimental and calculated adsorption isotherms of carbon dioxide on carbidederived carbon at 333 K. The overall agreement between the measured and predicted adsorbed amount of carbon dioxide is good. Finally, we extrapolate the dilatometric experiment to higher pressures. We found that the expansion of studied carbon sample reaches 0.75% at 27 MPa, as is shown in Figure 7.

## 5. Conclusions

We study adsorption-induced deformation of carbonaceous amorphous porous materials due to adsorption of carbon dioxide at 333 K and high pressures. We show that adsorbed and compressed carbon dioxide molecules induce very high adsorption stress in the smallest ultramicropores with pore size below 0.31 nm. At 27 MPa, the solvation pressure in 0.23 nm ultramicropore reaches 3.2 GPa. As pore size increases the solvation pressure is rapidly damped in the range of micropores because thermal fluctuations smooth the packing effects at 333 K. Model calculations as well as dilatometric experiment show that any sample of carbonaceous porous solid containing a fraction of the smallest ultramicropores with pore size below 0.31 nm will expand at the studied operating conditions. This is because the adsorbed stress in ultramicropores is much higher in comparison to that in wider micropores. Nevertheless, the nonmonotonic deformation (i.e., initial contraction and further expansion) of porous carbons/coals upon adsorption of carbon dioxide at 333 K is also theoretically predicted. Our calculations reproduce quantitatively the strain isotherm of carbon dioxide on carbide-derived activated carbon at 333 K and experimental pressures up to 2.9 MPa. The predicted bulk modulus of slitshaped carbide-derived activated carbon of 12 GPa is characteristic for vitreous carbons and polycrystalline graphite. Finally, we extrapolate adsorption and strain isotherms measured by gravimetric/dilatometric method to higher pressures to mimic geosequestration operating conditions. From the thermodynamic model of adsorption-induced deformation, we predict that expansion of studied carbon sample reaches 0.75% at 27 MPa and 333 K. The presented simulation results can be useful for the interpretation of coal swelling/contraction upon sequestration of carbon dioxide at high pressures and temperatures.

**Acknowledgment.** P.K. acknowledges the use of the computer clusters VPAC (Victorian Partnership for Advanced Computing, Melbourne, Australia). P.K. acknowledges the Royal Melbourne Institute of Technology (Academic Level B, 2008-2010). P.G. and A.P.T. acknowledge the use of the computer cluster at Poznan Supercomputing and Networking Centre as well as the Information and Communication Technology Centre of the Nicolaus Copernicus University (Torun, Poland). S.F. gratefully acknowledges the financial support from the Foundation for Polish Science.

Supporting Information Available: Snapshots of carbon dioxide confined in selected slit-shaped carbon ultramicropores. This material is available free of charge via the Internet at http://pubs.acs.org.

## References and Notes

(1) Bangham, D. H.; Fakhoury, N. *Nature* **1928**, *122*, 681.
(2) Haines, R. S.; McIntosh, R. *J. Chem. Phys.* **1947**, *15*, 28.
(3) Tvardovskiy, A. V. *Sorbent deformation*; Elsevier Ltd.: Oxford, 2007.
(4) Tvardovskiy, A. V.; Fomkin, A. A.; Tarasevich, Yu. I.; Zhukova, A. I. *J. Colloid Interface Sci.* **1999**, *212*, 246.
(5) Yakovlev, V. Yu.; Fomkin, A. A.; Tvardovskiy, A. V. *J. Colloid Interface Sci.* **2003**, *268*, 33.
(6) Yakovlev, V. Yu.; Fomkin, A. A.; Tvardovskiy, A. V.; Sinitsyn, V. A. *Russ. Chem. Bull., Int. Ed.* **2005**, *54*, 1373.
(7) Yakovlev, V. Yu.; Fomkin, A. A.; Tvardovskiy, A. V.; Sinitsyn, V. A.; Pulin, A. L. *Russ. Chem. Bull., Int. Ed.* **2003**, *52*, 354.
(8) Bansal, R. Ch.; Goyal, M. *Activated Carbon Adsorption*; CRC Press: Boca Raton, FL, 2005.
(9) Marsh, H., Rodriguez-Reinoso, F. *Activated Carbon*; Elsevier Ltd.: Oxford, 2006.
(10) Gauden, P. A.; Kowalczyk, P.; Terzyk, A. P. *Langmuir* **2003**, *19*, 4253.
(11) Kowalczyk, P.; Terzyk, A. P.; Gauden, P. A.; Leboda, R.; Szmechtig-Gauden, E.; Rychlicki, G.; Ryu, Z.; Rong, H. *Carbon* **2003**, *41*, 1113.
(12) Ravikovitch, P. I.; Vishnyakov, A.; Russo, R.; Neimark, A. V. *Langmuir* **2000**, *16*, 2311.
(13) Vishnyakov, A.; Ravikovitch, P. I.; Neimark, A. V. *Langmuir* **1999**, *15*, 8736.
(14) Bhatia, S. K.; Tran, K.; Nguyen, T. X.; Nicholson, D. *Langmuir* **2004**, *20*, 9612.
(15) Kowalczyk, P.; Holyst, R.; Terrones, M.; Terrones, H. *Phys. Chem. Chem. Phys.* **2007**, *9*, 1786.
(16) Brennan, J. K.; Thomson, K. T.; Gubbins, K. E. *Langmuir* **2002**, *18*, 5438.
(17) Terzyk, A. P.; Furmaniak, S.; Harris, P. J. F.; Gauden, P. A.; Wloch, J.; Kowalczyk, P.; Rychlicki, G. *Phys. Chem. Chem. Phys.* **2007**, *9*, 5919.
(18) Nicholson, D.; Parsonage, N. G. *Computer Simulation and the Statistical Mechanics of Adsorption*; Academic Press: London, 1982.
(19) Kaneko, K.; Ishii, C.; Ruike, M.; Kuwabara, H. *Carbon* **1992**, *30*, 1075.
(20) Hoffmann, J.; Nielaba, P. *Phys. Rev. E* **2003**, *67*, 036115.
(21) Miyahara, M.; Gubbins, K. E. *J. Chem. Phys.* **1997**, *106*, 2865.
(22) Lastoskie, C.; Gubbins, K. E.; Quirke, N. *Langmuir* **1993**, *9*, 2693.
(23) Kowalczyk, P.; Tanaka, H.; Holyst, R.; Kaneko, K.; Ohmori, T.; Miyamoto, J. *J. Phys. Chem. B* **2005**, *109*, 17174.
(24) Kowalczyk, P.; Tanaka, H.; Kaneko, K.; Terzyk, A. P.; Do, D. D. *Langmuir* **2005**, *21*, 5639.
(25) Tan, Z.; Gubbins, K. E. *J. Phys. Chem. B* **1990**, *94*, 6061.
(26) Kowalczyk, P.; Holyst, R.; Terzyk, A. P.; Gauden, A. P. *Langmuir* **2006**, *22*, 1970.
(27) Evans, R.; Marconi, M. B.; Tarazona, P. *J. Chem. Phys.* **1986**, *84*, 2376.
(28) Kowalczyk, P.; Bhatia, S. K. *J. Phys. Chem. B* **2006**, *110*, 23770.
(29) Ustinov, E. A.; Do, D. D. *Langmuir* **2003**, *19*, 8349.
(30) Striolo, A.; Chialvo, A. A.; Cummings, P. T.; Gubbins, K. E. *Langmuir* **2003**, *19*, 8583.
(31) Israelachvili, J. *Intermolecular and Surface Forces*; Academic Press: New York, 1998.
(32) Ravikovitch, P. I.; Neimark, A. V. *Langmuir* **2006**, *22*, 10864.
(33) Ustinov, E. A.; Do, D. D. *Carbon* **2006**, *44*, 2652.
(34) Balbuena, P. B.; Berry, D.; Gubbins, K. E. *J. Phys. Chem.* **1993**, *97*, 937.
(35) Snook, I. K.; van Megen, W. *J. Chem. Phys.* **1980**, *72*, 2907.
(36) Evans, R.; Bettolo Marconi, U. M. *J. Chem. Phys.* **1987**, *86*, 7138.
(37) Kowalczyk, P.; Ciach, A.; Neimark, A. V. *Langmuir* **2008**, *24*, 6603.
(38) Günther, G.; Schoen, M. *Mol. Simul.* **2009**, *35*, 138.

(39) Günther, G.; Prass, J.; Paris, O.; Schoen, M. *Phys. Rev. Lett.* **2008**, 101, 086104.

(40) Günther, G.; Schoen, M. *Phys. Chem. Chem. Phys.* **2009**, 11, 9082.

(41) Sing, K. S. W.; Everett, D. H.; Haul, R. A. W.; Moscou, L.; Pierotti, R. A.; Rouquerol, J.; Siemieniewska, T. *Pure Appl. Chem.* **1985**, 57, 603.

(42) Bickle, M. J. *Nat. Geosci.* **2009**, 2, 815.

(43) Matter, J. M.; Kelemen, P. B. *Nat. Geosci.* **2009**, 2, 873.

(44) Lackner, K. S. *Science* **2003**, 300, 1677.

(45) Schrag, D. P. *Science* **2007**, 315, 812.

(46) Haszeldine, R. S. *Science* **2009**, 325, 1647.

(47) Witze, A. *Nature* **2008**, 456, 290.

(48) Jakubov, T. S.; Mainwaring, D. E. *Phys. Chem. Chem. Phys.* **2002**, 4, 5678.

(49) Allen, M. P.; Tildesley, D. J. *Computer Simulation of Liquids*; Clarendon: Oxford, 1987.

(50) Frenkel, D.; Smit, B. *Understanding Molecular Simulation From Algorithms To Applications*; Academic Press: London, 1996.

(51) Kowalczyk, P.; Gauden, P. A.; Ciach, A. *J. Phys. Chem. B* **2009**, 113, 12988.

(52) Stone, A. J. *Science* **2008**, 321, 787.

(53) Nguyen, T. X. Characterization of Nanoporous Carbons. Ph.D. Thesis, The University of Queensland, Brisbane, 2006.

(54) Steele, W. A. *Surf. Sci.* **1973**, 36, 317.

(55) Steele, W. A. *The Interaction of Gases with Solid Surfaces*; Pergamon: New York, 1974.

(56) Potoff, J.; Siepmann, J. *AIChE J.* **2001**, 47, 1676.

(57) Ekrem, P.; Badie, I. M.; Schroeder, K. *Langmuir* **2003**, 19, 9764.

(58) Chmiola, J.; Yushin, G.; Gogotsi, Y.; Portet, C.; Simon, P.; Taberna, P. L. *Science* **2006**, 313, 5794.

(59) Gogotsi, Y.; Welz, S.; Ersoy, D. A.; McNallan, M. J. *Nature* **2001**, 411, 283.

(60) Gogotsi, Y.; Dash, R. K.; Yushin, G.; Yildirim, T.; Laudisio, G.; Fischer, J. E. *J. Am. Chem. Soc.* **2005**, 127, 16006.

(61) Gogotsi, Y.; NikitinA.; Ye, H.; Zhou, W.; Fischer, J. E.; Yi, B.; Foley, H. C.; Barsoum, M. W. *Nat. Mater.* **2003**, 2, 591.

(62) Nguyen, T. X.; Bae, J.-S.; Bhatia, S. K. *Langmuir* **2009**, 25, 2121.

(63) Sekine, T. *Carbon* **1993**, 31, 227.

(64) Kelly, B. T. *Physics of Graphite*; Applied Science Publishers: London, 1981.

(65) Boey, S. Y.; Bacon, D. J. *Carbon* **1986**, 24, 557.

(66) Neimark, A. V.; Coudert, F.-X.; Boutin, A.; Fuchs, A. H. *J. Phys. Chem. Lett.* **2010**, 1, 445.

(67) Vagraftik, N. B. *The Handbook of Thermodynamic Properties of Gases and Liquids*; G.I.F.M.L.: Moscow, 1963 (in Russian).

JP911996H
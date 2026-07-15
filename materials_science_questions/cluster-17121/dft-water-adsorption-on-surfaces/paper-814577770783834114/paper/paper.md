# Adsorbed water on iron surface by molecular dynamics

F.W. Fernandes, T.M.B. Campos, L.S. Cividanes *, E.A.N. Simonetti, G.P. Thim

Instituto Tecnológico de Aeronáutica, Divisão de Ciências Fundamentais, Departamento de Física, Praça Marechal Eduardo Gomes, 50 - Vila das Acácias,
CEP 12.228-900, São José dos Campos, SP, Brazil

---

## ARTICLE INFO

**Article history:**
Received 18 May 2015
Received in revised form
11 November 2015
Accepted 15 November 2015
Available online 23 November 2015

**Keywords:**
Interfaces
Metals
Adsorption
Molecular dynamics

## ABSTRACT

The adsorption of $H_2O$ molecules on metal surfaces is important to understand the early process of water corrosion. This process can be described by computational simulation using molecular dynamics and Monte Carlo. However, this simulation demands an efficient description of the surface interactions between the water molecule and the metallic surface. In this study, an effective force field to describe the iron-water surface interactions was developed and it was used in a molecular dynamics simulation. The results showed a very good agreement between the simulated vibrational-DOS spectrum and the experimental vibrational spectrum of the iron-water interface. The water density profile revealed the presence of a water double layer in the metal interface. Furthermore, the horizontal mapping combined with the angular distribution of the molecular plane allowed the analysis of the water structure above the surface, which in turn agrees with the model of the double layer on metal surfaces.

© 2015 Published by Elsevier B.V.

---

### 1. Introduction

The metallic corrosion process, which is mostly trigged by the interaction between water and metallic surfaces, is the progressive degradation of a material. Great efforts have been made to understand the early interactions between water-metal in order to slow down the chemical reactions involved in the corrosion process. A systematic study of the adsorption of water molecules in the iron interface is fundamental to understand the initial stages of the corrosion of metallic iron.

Water adsorption on iron surface has been experimentally studied using photoluminescence techniques [4]. Kolotyrkin and co-works [1] studied the water-iron interface using electroreflection spectroscopy. Hung [2,3] analyzed the adsorption and dissociation of water on a Fe (100) surface by High Resolution Electron Energy Loss Spectroscopy spectrum (HREELS) at various temperatures. These authors showed that the interaction between water molecules and iron surfaces is performed by several steps, which is initiated by deposition of water on metallic surface, followed by a charge transference process.

The statistical, structural and dynamical properties of solid-liquid interfaces have been studied by several computational methods, showing good agreement with the experimental results [5-7,11-19]. Molecular dynamics is one of the most used computational methods for interface studies due to its molecular approaching. In addition, very large systems can be simulated since molecular dynamics (MD) is based on the movements of atoms and molecules in a system with n-bodies. The movements of molecules are based on pre-determined interatomic potentials and molecular mechanics force fields.

Few studies are found in literature about water/iron interface simulation, and as far as we know, none water/iron study was performed using classical method simulations, i.e. they were all performed using ab initio methods [5-10]. Jung [9], Govender [8] and Freitas [10] studied the water-iron interface using DFT and they observed that among the most stable energy adsorption sites (top, bridge and hollow) the top site showed the lowest energy adsorption. These different adsorption sites corrugate the first layer of adsorbed water, where the water-iron distance in the z axis (perpendicular to iron surface) is related to the energy site. The corrugation effect on the liquid adsorption was first simulated by Spohr [7]. His empirical model for describing water interaction with the surface depends on two factors: the water-metal distances and the water location over the metallic surface (i.e. its position in relation to sites top, bridge and hollow). However, the parameterization of the potential function was obtained by ab initio simulation of the water adsorption on a small cluster of a metallic surface. For some metals (e.g. iron), it is very hard to obtain such potential function due to the degeneracy of states and a lack of spin paring configuration near the Fermi level.

Here, a new force field based on a modified Spohr model was developed, which models very well the water-iron interface. The parameterization was obtained using the adsorption energy and

---

* Corresponding author.
E-mail address: flaviano@ita.br (L.S. Cividanes).

http://dx.doi.org/10.1016/j.apsusc.2015.11.143
0169-4332/© 2015 Published by Elsevier B.V.

the equilibrium distance of the water molecule in relation to the three main adsorption sites (top, bridge and hollow). This method- ology was used to study the adsorption of water molecules on the BCC surface of the Fe (1 0 0) by molecular dynamics, which in turn can be used to study water on other metallic surfaces.

## 2. Computational procedures
Molecular dynamic simulation was performed using the DL POLY 2.0 software package [20] using the force field described in 2.1 and the movement equations were integrated by Leapfrog Verlet algorithm [21]. First, the system was relaxed using NPT ensemble with the barostat-thermostat Berendsen [22] at 298 K and 1 atm. After that, the temperature was set to 133 K and a new equilibrium configuration was obtained performing at least 500 ps as time sim- ulation procedure. During that, canonical variables were obtained with the temperature and pressure controlled at each 0.1 ps using NPT ensemble with the barostat-thermostat Nosé-Hoover [51]. After relaxation, the statistical data was performed by collecting 1000 frames and 1 fs as a simulation time step. The thermodynamic equilibrium was assumed when the simulation showed a RMS of the total energy of 0.1%. In vibrational frequency, 1154 frames and 3.9 fs period time was used to get the autocorrelation function.

The molecular configuration was constituted by 1073 water molecules above an ideal block of BCC of 1729 iron atoms. The sur- face in contact with the water molecules had 100 Fe atoms and the crystalline structure was cleaved at plane (1 0 0). In order to reproduce an infinite structure, an orthorhombic periodic bound- ary condition was used. A cutoff of $10\mathring{A}$ was used in order to minimize the computational cost. The NPT ensemble with the barostat-thermostat Berendsen [22], with temperature and pres- sure control at each 0.1 ps, was used in all simulations. In this work, the box dimension and the molecular configuration setup described above were sufficient to represent, by the structural and energetic point of view, the iron-water interface.

An initial configuration of the system described previously was simulated at 298 K and 1 atm until the thermodynamic equilibrium is obtained. After that, the temperature was set at 133 K and a new equilibrium configuration was obtained. Fig. 1 shows the molecule distribution after thermodynamic equilibrium at 133 K, where oxy- gen atoms are red circles, hydrogen atoms are white and Fe atoms are brown and green. The Fe atoms in contact with water molecules are green and all others are brown. Fig. 1 also shows the definition of sites Top (T), bridge (B) and hollow (H) in relation to an iron surface.

![](./images/814577770783834114_1.jpg)

Fig. 1. Water and iron positions after thermodynamic equilibrium and the definition of sites top, bridge and hollow. The red X positions are the exact positions of top, bridge and hollow.

### 2.1. Force field.
The force field was built for modeling water-water, Fe-water and intramolecular interactions of water molecules. Several mod- els [23-33] for water molecules were tested to describe water at 133 K. However, as none of them were able to describe the water properties properly a new force field was built, see Eqs. (1)-(4),
$$V(r)=V_{b n d}+V_{f l x}+V_{v d w}+V_{e l e},\qquad(1)$$

$$V_{b n d}=\sum_{b n d} E_{0}\left(1-e^{-k\left(r_{O H}-\bar{r}_{O H}\right)}\right)^{2} e^{(r-\lambda)},\qquad(2)$$

$$V_{f l x}=\sum_{f l x} \frac{K_{H O H}}{2}\left(\theta_{H O H}-\bar{\theta}_{H O H}\right)^{2},\qquad(3)$$

$$V_{v d w}=\sum_{i<j} 4 \varepsilon_{0}\left[\left(\frac{\sigma}{r_{i j}}\right)^{12}-\left(\frac{\sigma}{r_{i j}}\right)^{6}\right].\qquad(4)$$

Eq. (2) is related to O-H bonding of water molecule and it is a modified Morse potential. Morse potential showed the best result due to its enharmonic property, giving more flexibility to the stretching and to hydrogen bonding as well. In addition, the Morse potential function was multiplied by an exponential function, avoiding total molecule breakdown during the system relaxation. In this term, $E_{0}$ is the bond energy, $k$ is the potential well depth and $r_{O H}$ is the OH bond length [34-36]. The value of these parameters has been shown in Table 1.

Eq. (3) is the scissoring potential of water molecule, which is based on a harmonic potential. In this term, $\theta$ is the HOH angle, $\bar{\theta}$ is the equilibrium angle and $K_{H O H}$ is the bond vibration force constant. The short distance intermolecular interactions of water molecules were modeled by 12-6 Lennard-Jones (Eq. (4)) and the long distance by the Ewald summation. The parameters of the Lennard-Jones potential and partial charges of oxygen $q_{0}$ and hydrogen $q_{H}$ were that of the TIP3P model [25].

The Fe-water interaction was built in order to reproduce the Born-Oppenheimer potential energy surface of the Fe (100)+1H₂O system, where the corrugation effect over the peri- odic iron surface is considered in the energy of the adsorption sites. The $Fe-H_{2}O$ interactions are described by a set of radial site-site pair potentials given by
$$V_{F e-H_{2} O}=V_{F e-O}(z, \rho)+V_{F e-H_{1}}(r)+V_{F e-H_{2}}(r),\qquad(5)$$

$$\begin{aligned}
& V_{F e-O}(z, \rho) \\
& =\frac{1}{2} \sum A\left[\left(e^{-2 \beta_{0}\left(z-z_{0}\right)}-2 e^{-\beta_{0}\left(z-z_{0}\right)}\right)-\alpha e^{-2 \beta_{1}\left(z-z_{0}\right)} e^{-\gamma \rho^{2}}\right],
\end{aligned}\qquad(6)$$

<table>
<caption>Table 1 Parameters of Eqs. (2)-(4).</caption>
<thead>
<tr>
<th>Parameter</th>
<th>Unit</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>$E_{0}$</td>
<td>kcal/mol</td>
<td>103.3</td>
</tr>
<tr>
<td>$k$</td>
<td>$\mathring{A}^{-1}$</td>
<td>3.08</td>
</tr>
<tr>
<td>$\bar{r}_{OH}$</td>
<td>$\mathring{A}$</td>
<td>0.9</td>
</tr>
<tr>
<td>$\kappa$</td>
<td>$\mathring{A}^{-1}$</td>
<td>0.45</td>
</tr>
<tr>
<td>$\lambda$</td>
<td>$\mathring{A}$</td>
<td>2.4</td>
</tr>
<tr>
<td>$K_{HOH}$</td>
<td>kcal/mol rad</td>
<td>87.733</td>
</tr>
<tr>
<td>$\bar{\theta}_{HOH}$</td>
<td>Degree</td>
<td>108.47</td>
</tr>
<tr>
<td>$\varepsilon_{0}$</td>
<td>kcal/mol</td>
<td>0.1522</td>
</tr>
<tr>
<td>$\sigma$</td>
<td>$\mathring{A}$</td>
<td>3.1506</td>
</tr>
<tr>
<td>$q_{O}$</td>
<td>E</td>
<td>$-0.834$</td>
</tr>
<tr>
<td>$q_{H}$</td>
<td>E</td>
<td>0.417</td>
</tr>
</tbody>
</table>

<table><thead><tr><th colspan="3">Table 2Parameters of Eqs. (5)–(7).</th></tr><tr><th>Parameter</th><th>Unit</th><th>Value</th></tr></thead><tbody><tr><td>A</td><td>kcal/mol</td><td>1.843</td></tr><tr><td>$\alpha$</td><td>–</td><td>192.701</td></tr><tr><td>$\beta_0$</td><td>Å⁻¹</td><td>1.6790</td></tr><tr><td>$\beta_1$</td><td>Å⁻¹</td><td>1.5901</td></tr><tr><td>$z_0$</td><td>Å</td><td>2.72</td></tr><tr><td>$\gamma$</td><td>Å⁻²</td><td>0.8297</td></tr><tr><td>B</td><td>kcal/mol</td><td>0.0237</td></tr><tr><td>$\beta_H$</td><td>Å⁻¹</td><td>2.0</td></tr><tr><td>$r_H$</td><td>Å</td><td>1.5</td></tr></tbody></table>

$$
V_{Fe-H}(r)=Be^{-\beta_{H}(r-r_{H})}, \tag{7}
$$

The vertical equilibrium distance between water oxygen and iron metal is $z_0$ and $\rho$ is the projection of the relative distance between water oxygen atoms and iron metal on the $xy$ plane. The corrugation effect is performed using the second part of Eq. (6), which depends on $z_0$ and $\rho$.

The corrugation effect is performed by a Gaussian function, $e^{-\gamma \rho^{2}}$, (width $=\sqrt{1 / 2 \gamma}$); where $\alpha$ is a constant related to the adsorption energy ($A$), which is added to the corrugation effect when $\rho \to \infty$. In this force field, one water oxygen atom is able to interact simultaneously with several iron atoms and the total $V_{Fe-O}$ potential was performed by the sum of individual contributions of all iron atoms. However, in order to avoid the interaction energy overvaluation the total $V_{Fe-O}$ energy was divided by N (number of individual contributions). The Fe–H interaction had a repulsive character and was represented by an exponential function with a negative argument.

Table 1.
The parameters of Eq. (5) were obtained through the optimization of the potential energy surface $V(\{\xi_{i}\} ; z, \rho)$ that determined the interaction between $H_{2} O$ molecules and Fe (1 0 0) surface. In this expression, $\xi_{i}$, $\{\xi_{i}, i=1,2,...9\}$, represents a parameter set formed by nine parameters, as showed in Table 2. Initially, a set was randomly determined and $V(\{\xi_{i}\} ; z, \rho)$ was determined. Then, these parameters were changed by an increment $d\xi_{i}$ and a new set was created. Finally, $V(\{\xi_{i}\} ; z, \rho)$ was calculated again. The best $\xi_{i}$ is obtained when the adsorption energy and the equilibrium distance of the $H_{2} O$ molecule satisfy the mean square value, according to Eq. (8),

$$
\left\{ \frac{1}{6} \sum_{k=1}^{3} \left[ (V-E_{k})^{2} + (z-d_{k})^{2} \right] \right\}^{1/2} = \text{min}, \tag{8}
$$

where, $E_k$ and $d_k$ represent the values of the adsorption energy and the distance of equilibrium determined by Freitas et al. [10] for water adsorption over an iron surface. The values of these parameters has been shown in Table 2.

Fig. 2 shows a top and perspective view of the potential surface $V\left(\left\{\xi_{i}\right\} ; z, \rho\right)$ of the system Fe (1 0 0)–water (Eq. (5)) for water molecules at $z=2.30$ Å. The sinusoidal behavior is due to the superposition of Fe–water interactions, performing the corrugation.

<table><thead><tr><th colspan="4">Table 3$E_{ads}$ and $d$ for water adsorption over a Fe (1 0 0) surface.</th></tr><tr><th></th><th>Reference</th><th>Top</th><th>Bridge</th><th>Hollow</th></tr></thead><tbody><tr><td>$E_{ads}$ (kcal/mol)</td><td>21</td><td>7.841</td><td>6.226</td><td>5.304</td></tr><tr><td>$E_{ads}$ (kcal/mol)</td><td>This work</td><td>7.782</td><td>6.304</td><td>5.225</td></tr><tr><td>$d$ (Å)</td><td>22</td><td>2.28</td><td>2.10</td><td>2.95</td></tr><tr><td>$d$ (Å)</td><td>This work</td><td>2.30</td><td>2.37</td><td>2.42</td></tr></tbody></table>

Table 3 shows the values of the adsorption energy ($E_{ads}$) and equilibrium distance ($d$) found in the literature and they were calculated using Eq. (1) at Top (T), Bridge (B) and Hollow (H) sites.

## 3. Results and discussion

To analyze the water model at low temperature, as showed in Eq. (1)–(4), the density of pure ice was calculated for a system containing $512~H_{2} O$ molecules at 133 K and 1 atm. In this case, the control of temperature and pressure was made using the Nose-Hoover thermostat-barostat following the same procedures described previously. Under these conditions the value found for the density of ice was $1.07~\text{g}~\text{cm}^{-3}$, which is between the densities of ice Ih and II according to Londsdale and Kam [37–42].

A small separation between the metallic surfaces shown in Fig. 1 meaningfully affects the behavior of $H_{2} O$ molecules in the region covered by the metallic walls. Therefore, the internal density of energy (energy per $H_{2} O$ molecule) and the volumetric density of ice were calculated for various with different heights of the cavity between the metallic walls. The internal density of energy was calculated at 0 K while the volumetric density of ice was 133 K. However, for each selected system, the amount of molecules was calculated in order to perform the density found for pure ice at 133 K ($1.07~\text{g}~\text{cm}^{-3}$) which was showed previously. Thus, the dimensions of the simulation box were kept constant during the simulation at each system and the temperature was controlled using the Nose-Hoover thermostat.

![](./images/814577770783834114_2.jpg)

Fig. 2. Surface potential of water molecules above the Fe (1 0 0) according to Eq. (5).

Fig. 3 shows the density of internal energy and density of ice in relation to the z-axis (normal to iron surface). It can be observed that the energy density decreases with the z-axis value. This behavior is due to the simultaneous interactions of the buck water molecules with the two metallic surfaces. In addition, the volumetric density tends to be $1~\text{g}~\text{cm}^{-3}$ when $z=24$ Å. Therefore, the energy is practically constant (14.5 kcal/mol) for values higher than 24 Å. According to the volumetric density, its value tends to be $1~\text{g}~\text{cm}^{-3}$ when $z=24$ Å and the small variation of the structure of ice in this region can be neglected. Thus, the interaction between the buck water molecules and the two metallic surfaces can be neglected for z-axis higher than 24 Å.

Fig. 4 shows the density profile of water molecules in relation to z axis (normal to iron surface, see Fig. 1 for axes definition), where the distance equals to zero is on the iron surface. Density was normalized by $\rho_0$, which is the density in the center of the simulation

![](./images/814577770783834114_3.jpg)

Fig. 3. Energy and volumetric densities in relation to z-axis.

![](./images/814577770783834114_4.jpg)

Fig. 4. Z-density profile of water.

box ($\rho_0$=0.033 molecule/$\mathring{\text{A}}^3$). This profile can be divided into three regions: I, II and III. Region I is in contact with the iron surface, has a thickness of $3.5\mathring{\text{A}}$ and the density peak ($2.25\mathring{\text{A}}$) is $12\rho_0$. Region II is between $3.5$ and $6.0\mathring{\text{A}}$, where the density peak ($4.7\mathring{\text{A}}$) is $3.5\rho_0$. The region III is higher than 6.0.

The water density in the region near the metallic surface is much higher than the water density far from the metallic surface. However, the relative density of water over metallic surfaces (region I) depends on the metallic nature. Neves and co-workers [17] found a density of $5.5\rho_0$ at a distance of $2.5\mathring{\text{A}}$ for the water adsorbed on the Au (2 1 0) surface. Spohr [7] determined a density of $6.5\rho_0$ for water at $2.5\mathring{\text{A}}$ on a Hg (1 0 0) surface. Ignazack and co-workers [42] found $7\rho_0$ at $2.2275\mathring{\text{A}}$ for adsorption on a Cu (1 0 0) surface. The elevated density obtained in our work is due to the perfect alignment of iron atoms of the first layer, since all iron movements are frozen. This perfect alignment optimizes the alignment of water molecules in the first region, increasing the density. A real iron crystalline vibrates and all iron atoms oscillate over an average position, breaking the perfect alignment. The use of a frozen system does not alter the final results, since all interactions were concerned, less the iron-iron interaction. This approximation was already used by several authors [7,16,17,42] with excellent results.

![](./images/814577770783834114_5.jpg)

Fig. 5. (A) Top view of the water distribution over iron surface. (B) Side view of the water distribution over iron surface.

Fig. 5 shows the mapping of water molecules in the region I. The atom positions mean their localization after the simulation is completed. The iron atoms were frozen during all simulation, so they are in the last frame perfectly aligned as they were at the beginning of the simulation. However, oxygen and hydrogen atoms obeyed the overall condition of simulation in terms of force and energy, assuming new positions after each new time step. The green and brown circles represent iron atoms of the first crystalline plane and iron atoms of the bulk, respectively. The red and white circles represent the oxygen and hydrogen atoms, respectively. The green lines represent the Fe-water intermolecular bonding. One can observe that oxygen atoms are located preferentially over the top position, but

![](./images/814577770783834114_6.jpg)

Fig. 6. Angular distribution of the vectors normal, H-H and dipole in relation to axis X and Z. (a) Vector dipole; (b) Vector H-H; (c) Vector normal (d) Definition of the vectors.

slightly dislocated to bridge and a few of them are dislocated to the hollow site.

The oxygen adsorption on top and bridge position is due to metal action over oxygen atoms, pulling them into the positions where the adsorption energies are minimal. However, the nucleation of ice over the iron surfaces is dependent on the iron crystalline structure and the water-water intermolecular bonding. Therefore, ice grows in clusters following the BCC iron cubic structures. The oxygen atoms showed a slight displacement from the top position due to the need to satisfy the hydrogen bonding and the potential energy described by Eq. (5). This behavior was also experimentally observed by Hung [2,3] using HEELS (High-Resolution Electron Energy Loss Spectroscopy) spectroscopy, studying water adsorption on Fe (1 0 0) at several temperatures.

The hydrogen atoms are in well-defined spots due to the necessity of satisfying the several conditions of all hydrogen bonding, i.e. a hydrogen atom located in the first layer must satisfy the hydrogen bonding with the neighboring oxygen atoms of the first and the second layers and the iron atoms as well. This effect is strongly affected by the interatomic distance of Fe-Fe atoms of the iron surface, which commands the site position of oxygen atoms of the first layer.

### 3.1. Orientation

Fig. 6 shows the angular distribution of normal, dipole, and H-H vectors of the water molecules located in region I. The vector normal is perpendicular to water molecule plane, the vector dipole is a bisector between the two O-H bindings and the vector H-H is a vector that passes in the center of the two hydrogen atoms. This discussion will be divided into two parts: first in relation to axis z and later related to axis x.

#### 3.1.1. Axis z

The angular distribution of the vector normal shows the highest probability for $\theta \to \mathrm{zero}^{\circ}$, i.e., the vector normal has a major tendency to be parallel to axis Z, i.e. water molecular plane tends to be parallel to plane iron surface (plane XY). However, the vector H-H shows two probabilities for vector H-H ($\varphi \sim 90^{\circ}$ and $\varphi \sim \pm 45^{\circ}$). The vector dipole showed a major probability for $\psi \sim 96^{\circ}$ and $\psi \sim 53^{\circ}$. Therefore, the maxima probabilities found for the three vectors suggested two possible orientations for the water molecule plane in relation to axis z. The first one is the water plane which is practically parallel to the iron surface, but the distance Fe-H is slightly lower than the Fe-O distance, making the vector dipole points to the iron surface. The second one suggests that the plane of the water molecule is $45^{\circ}$ in relation to the iron surface.

#### 3.1.2. Axis X

Now, a discussion in relation to axis X will be performed. The probabilities for vector normal, H-H and dipole are $\theta \sim \mathrm{zero}^{\circ}$, $\varphi \sim 45^{\circ}$ and $\psi \sim 135^{\circ}$, respectively. The value found for the vector normal agrees with that previously determined for axis z, where the water molecular plane is practically parallel to the iron surface. The values for the vectors H-H and dipole are determined by the formation of the hydrogen bonding among the water molecules of the first and second layers. These vectors were found at 45 and $135^{\circ}$ in relation to axis x since they had to satisfy the previous condition.

### 3.2. Vibrational analysis

The vibration states were determined using Fourier Transform of the vibrational density of states (vibrational-DOS) of oxygen and hydrogen atoms of the water molecules. The isolated water

![](./images/814577770783834114_7.jpg)

Fig. 7. Vibrational-DOS spectra of Ow and Hw of ice at 133 K.

molecule possesses 9 degrees of freedom: three of them are translational, three are rotational, and three are vibrational. The three vibration modes are called symmetric stretch, asymmetric stretch and scissors (or bend or deformation). However, water molecules in the liquid and solid phases have intermolecular bonding (H-bonding), where a hydrogen atom from one water molecule is attracted by the oxygen atom of another water molecule, forming an additional attractive potential for proton. The main components of H-bonding are electrostatic forces, charge transfer, covalent forces, dispersion forces and exchange repulsion [52].

An important consequence of the presence of H-bonding (i.e. for solid and liquid phases) on the vibrational spectroscopy is that the vibrational energy levels move closer together and the transitions associated with O-H stretch are shifted to lower frequencies. Consequently, the vibrational spectrum of ice is far more complex than that of the isolated molecules, partly because the free rotations and translations of the isolated molecule are "frustrated" by the locking of the molecule into the lattice, transforming them into new vibrational modes. Therefore, the distinction between the OH symmetric and asymmetric stretch breaks down when H-bonding is considered. The intermolecular coupling and the OH stretch results in the absorption of infrared radiation between 3000 and $3600 \mathrm{~cm}^{-1}$ in condensed phases.

The deformation mode results in a broad infrared absorption feature centered at $1650 \mathrm{~cm}^{-1}$ in condensed phases. However, this assignment is complicated by possible contributions from the overtones of the frustrated rotations. The frustrated rotations (also called librations) occur in the frequency range between 50 and $1200 \mathrm{~cm}^{-1}$, with a broad maximum at $800-840 \mathrm{~cm}^{-1}$ for ice I. Finally, a frustrated translation is associated with peaks at $220-240 \mathrm{~cm}^{-1}$. In this region, the experimental spectroscopy of ice I shows three broad and intense bands between 50 and $1200 \mathrm{~cm}^{-1}$. Since water vapor does not exhibit any peak in this range rather than fine lines of transitions between rotational states, one can conclude that these bands are associated to the intermolecular vibrations.

The oxygen spectrum of ice determined in this work at 133 K is shown in Fig. 7-A. It clearly shows the three bands of solid water: $3000-3600$, $1500-1700$ and $60-1200 \mathrm{~cm}^{-1}$. The first two bands are too weak to make possible a proper analysis. Nevertheless, one can observe a weak band centered at $3246 \mathrm{~cm}^{-1}$ and another at $1692 \mathrm{~cm}^{-1}$. There is a strong and broad band in the range of $50-1200 \mathrm{~cm}^{-1}$, where three peaks can be determined: 58,222 and $480 \mathrm{~cm}^{-1}$. The hydrogen spectrum (Fig. 7-B) determined in this work at 133 K is more sensitive in the whole range of $50-4000 \mathrm{~cm}^{-1}$ than the oxygen spectrum. In this spectrum one can clearly see the presence of the three strong and broad bands that are expected for solid water: $\sim 3300 \mathrm{~cm}^{-1}, \sim 1600 \mathrm{~cm}^{-1}$ and $50-1200 \mathrm{~cm}^{-1}$. The hydrogen and oxygen spectra showed basically the same peaks.

The band at $3500-3700 \mathrm{~cm}^{-1}$ is related to OH stretching and it is associated to the H-bonding intermolecular interactions and the locking of water molecules due to the solid iron structure. One can clearly see the presence of three peaks from the deconvolution process plot $(2950,3213$ and $3315 \mathrm{~cm}^{-1})$ and they are red shifted about $300 \mathrm{~cm}^{-1}$ from those of isolated water, as it was expected for solid water. Taylor and co-workers [45] studied the vibrational spectroscopy of water at $77^{\circ} \mathrm{C}$ using Raman spectroscopy and they found the following peaks in this region: at 3085, 3210 and $3320 \mathrm{~cm}^{-1}$ for ice Ih, at 3083, 3215 and $3320 \mathrm{~cm}^{-1}$ for Ic, at 3194 and $3314 \mathrm{~cm}^{-1}$ for ice II, at 3159 and $3281 \mathrm{~cm}^{-1}$ for ice III, at 3181 and $3312 \mathrm{~cm}^{-1}$ for ice V. Hardin and co-workers studied vitreous ice by infrared spectroscopy and they obtained the peak positions at $3191,3253$ and $3367 \mathrm{~cm}^{-1}$. Therefore, one can conclude that the theoretical spectra at about $3200 \mathrm{~cm}^{-1}$ agreed very much with the experimental ones.

The band at $1200-1800 \mathrm{~cm}^{-1}$ in the spectrum of condensed water is associated to the deformation vibration mode of water molecules coupled with intermolecular interaction and overtones of the frustrated rotations. The peaks related to frustrated rotations are in the range of $525-1040 \mathrm{~cm}^{-1}$. The deconvolution process clearly shows two peaks (1666 and $1763 \mathrm{~cm}^{-1}$ ). Devlin and co-workers [43] studied the infrared absorption spectrum of the amorphous ice at 133 K and they found bands in 1670, 1711 and $1735 \mathrm{~cm}^{-1}$. Once again, one can observe the close correlation between the experimental spectrum and the one obtained in this work.

The band $50-1200 \mathrm{~cm}^{-1}$ was originally associated with the rotational movement of the isolated molecule. Nevertheless, liquid water and solid water infrared and Raman spectra are much more complex than that of isolated water molecules due to vibrational overtones and combinations with librations (restricted rotations; that is, rocking motions). Our simulation process determined peaks at 53, 222, 487, 654 and $827 \mathrm{~cm}^{-1}$ (hydrogen spectrum). Devlin attributed a peak at $810 \mathrm{~cm}^{-1}$ to the libration mode of amorphous ice and at $840 \mathrm{~cm}^{-1}$ to crystalline ice. In our work, this peak was observed at $827 \mathrm{~cm}^{-1}$ (for hydrogen). Hardin and co-workers [44] studied the vibrational spectroscopy of the vitreous and cubic ice at 92 K and they observed a peak at $675 \mathrm{~cm}^{-1}$ for the vitreous and at 690 for the cubic ones. They assigned this peak to a vibration mode that comes from a composition of the translational and rotational movements which are hindered by both the low temperature and the crystalline lattice. In our work this peak was determined at $654 \mathrm{~cm}^{-1}$ (for hydrogen). Jung and co-workers [9] were studying water adsorption over an iron structure using DFT simulation and attributed the peak at $420 \mathrm{~cm}^{-1}$ to the wagging mode of the HOH molecule, while in our work this peak was determined at $487 \mathrm{~cm}^{-1}$ for hydrogen and 480 for oxygen. Hardin also observed a peak at $212 \mathrm{~cm}^{-1}$ for vitreous ice at 92 K and they attributed it to the translational mode (hindered by the crystalline lattice) and ours is determined at $222 \mathrm{~cm}^{-1}$. Taylor and co-workers [45] studied the ices Ih, Ic, II, III and V using Raman spectroscopy and they observed the presence of strong peaks at low frequency (about $40 \mathrm{~cm}^{-1}$, compared to ours at $53 \mathrm{~cm}^{-1}$ ) in the spectrum of all ices. These peaks appear in the spectrum of liquid and solid water, but their assignment is still debatable. In order to clarify it, several studies have been made in liquid water, where Walrafen [46]; Mizoguchi [47]; Winkler [48], Padro [49] and Tsai [50] showed different points of view about this assignment.

![](./images/814577770783834114_8.jpg)

Fig. 8. Vibrational-DOS spectra of Ow and Hw of ice at 133 K located at several distances from the iron surface. For comparison, the ice spectra are put together.

![](./images/814577770783834114_9.jpg)

Fig. 9. Vibrational-DOS spectra of ice at 133 K and solid water inside a layer of 1.80 Å from the iron surface.

In order to study and properly make assignments of the vibra- tional mode of water molecules of the iron-water interface, it was built the vibrational-DOS spectrum of oxygen and hydrogen water molecules located inside layers of several thicknesses counted from the iron surface. These spectra were compared to the same spec- tra of the pure ice shown in Fig. 8 (also see Figs. 7 and 9). The oxygen spectra of all layers show the same characteristics of the ice spectrum, that is, the spectra are very intense and sensitive at a very low wave number (50-1200 cm⁻¹). The ice peaks are centered at 58, 222 and 480 cm⁻¹ in the ice spectrum and they sys- tematically shift to the blue direction as they approach the iron surface. When the layer has a thickness of 1.80 Å the peak at 58 is shifted to 87 and the one at 480-510 cm⁻¹. A magnification at the peak centered at 222 cm⁻¹ of the ice spectrum shows that it is really a band formed of small peaks (202 and 285 cm⁻¹) and the intensity of these small peaks increase as they approach the iron surface. However, the relative intensity of these peaks depends on the distance from the iron surface. The spectrum of the layer with 1.80 Å of thickness shows that the peak at 202 cm⁻¹ blue shifts to 277 cm⁻¹ and that the one at 285 also blue shifts to 334 cm⁻¹. One remarkable observation is the presence of a strong new peak at 392 cm⁻¹ and a weak one at 152 cm⁻¹. The peak at 392 cm⁻¹ is most likely related to Fe-OH₂ stretch, which was already experi- mentally observed by Hung and co-workers at 415 cm⁻¹. However, Jung and co-workers studying this system by ab initio simulation attributed this peak (they observed it at 430 cm⁻¹) to the wagging mode of water molecules. Jung also attributed a peak at 217 cm⁻¹ to Fe-OH₂ interaction. This peak at 217, observed by Jung, is most likely our peak at 152 cm⁻¹. These two peaks, at 152 and 392 cm⁻¹, were assigned to stretch, indicating the formation of the chemical bonding Fe···OH₂. Therefore, the correlation between simulation and experimental assignment made it possible to detect the forma- tion of a chemical bonding between water molecules and the iron surface.

The low frequency range of the vibrational-DOS of water molecules' hydrogen atoms inside the layer of 1.80 Å of thickness is characterized by a lot of librational overtones. The presence of a huge number of overtones makes it difficult to establish a proper correlation between both vibrational-DOS spectra. However, the peak at 1014 cm⁻¹ in the spectrum of the 1.80 Å layer clearly does not have any correlation with any peak of the ice spectrum. This peak at 1014 cm⁻¹ should be the same observed by Hung and co- workers at 930 cm⁻¹, where they attributed it to water libration positioned over the top site of an iron crystalline structure. This agreed with the horizontal mapping, where it can be seen that the oxygen atoms occupying mainly the top site over the bridge and hollow ones. This result also agrees with Jung and co-workersí results where they determined that the top site is the more energet- ically favorable position for oxygen during water adsorption over (1 0 0) the iron structure. In addition, the vibrational-DOS spectrum showed a weak peak at 778 cm⁻¹, which Hung and co-workers attributed to the libration mode of oxygen located in the bridge site. The bridge site is the second most favorable position for the oxygen atom of the water molecule (the first is the top position).

In addition Hung and co-workers observed a strong peak at 3000 cm⁻¹ which they assigned to Fe···HOH, that is an intermolecular H-bonding between the water molecule and the

iron atom from the crystalline structure. One can observe in the vibrational-DOS of hydrogen atoms that the peak at $2932 \mathrm{~cm}^{-1}$ becomes increasingly stronger and this peak does not exist in the pure water spectrum. Therefore, it is possible to conclude that the peak at $3000 \mathrm{~cm}^{-1}$ observed by Hung, appears, in our spectrum, to have slightly shifted to a lower wavenumber $(2932 \mathrm{~cm}^{-1})$, confirming once more that our simulation was able to detect the chemical interaction between the iron from the surface and water molecules.

Finally, Hung and co-workers observed a peak at $3470 \mathrm{~cm}^{-1}$ and Jung and co-workers detected a peak at $3590 \mathrm{~cm}^{-1}$ and both of them assigned these peaks to $\mathrm{O}-\mathrm{H}$ stretching of adsorbed water molecules over the iron surface. In our vibrational-DOS hydrogen spectrum, the peak at $3464 \mathrm{~cm}^{-1}$ is not present in the ice spectrum and the intensity of this peak increases as it approaches the iron surface. Therefore, this peak should be related to that one at 3470 of Hung and $3590 \mathrm{~cm}^{-1}$ of Jung with a slight shift to a lower wavenumber.

The Metal- $\mathrm{H}_{2} \mathrm{O}$ interaction was modeled considering a clean and perfectly flat metallic surface. This behavior can only be achieved in the absence of phonon vibrations. This vibration deforms solid structure, forming atomic steps on the iron surface. Therefore, some aspects related to the water structure above the iron surface could be overestimated due to the presence of defects along the iron-water interface. However, the use of a perfectly flat surface overestimates the water density of the first layer. The perfect alignment of iron atoms of the Fe (100) first layer aligns all oxygen atoms of all $\mathrm{H}_{2} \mathrm{O}$ molecules of the first water layer, increasing the local density. By the way, the lattice vibration could couple with the enharmonic vibration of water at low temperature, changing the vibrational-DOS of oxygen and hydrogen (Figs. 8 and 9). However, despite the errors caused by a frozen Fe (100) structure, the values found for vibrational-DOS still shows a good agreement with experimental data.

## 4. Conclusion

In this study, we proposed a two-dimensional model of interaction between ice and a perfectly metallic surface Fe (100). Its efficacy was tested by analyzing the structure of the ice near the metal surface. For this, we calculated the density profile of the region where the bilayer was observed due to the high density of water in this region, which is common in liquids that are near the metal-liquid interface. The orientation of the molecular plane relative to the surface showed the arrangement of the molecules along the surface which favors hydrogen bonding. The oxygen molecules in the first layer primarily presented its location in the TOP sites, in agreement with the theoretical prediction proposed in previous works. This distribution also favored the hydrogen bonds between neighboring molecules, which in turn, compete with Metal- $\mathrm{H}_{2} \mathrm{O}$ interaction. Furthermore, the model also demonstrated its ability to describe the vibrational spectrum of water near the surface. For this, the density of atomic vibrational states was compared with experimental data from the HREELS spectrum, which showed good agreement with the main vibrational modes.

## Acknowledgments

The authors gratefully acknowledge the financial support of CAPES, CNPq and Fapesp.

## References

[1] Y.M. Kolotyrkin, R.M. Lazorenko-Manevich, L.A. Sokolova, Spectroscopic studies of water adsorption on iron group metals, J. Electroanal. Chem. Interfacial Electrochem. 228 (1987) 301.

[2] W.H. Hung, J. Schwartz, S.L. Bernasek, Sequential oxidation of Fe (100) by water adsorption: formation of an ordered hydroxylated surface, Surf. Sci. 248 (1991) 332.

[3] W.H. Hung, J. Schwartz, S.L. Bernasek, Adsorption of $\mathrm{H}_{2} \mathrm{O}$ on oxidized $\mathrm{Fe}$ and $\mathrm{O}_{2}$, Surf. Sci. 294 (1993) 21.

[4] A.N. Podobaev, Adsorption of water molecules in the process of electroionization of the iron group metals, Russ. J. Gen. Chem. 79 (2009) 1965.

[5] A.M. Kuznetsov, R.R. Nazmutdinov, M.S. Shapnik, Water adsorption-quantum chemical approach, Electrochim. Acta 34 (1989) 1821.

[6] S. Meng, E.G. Wang, S. Gao, Water adsorption on metal surfaces: a general picture from density functional theory studies, Phys. Rev. B 69 (2004) 195404.

[7] E. Spohr, G. Tóth, K. Heizinger, Structure and dynamics of water and hydrated ions near platinum and mercury surfaces as studied by MD simulations, Electrochim. Acta 41 (1996) 2131.

[8] A. Govender, D.C. Ferré, J.W. Niemantsverdriet, The surface chemistry of water on Fe (100): a density functional theory study, Chem. Phys. Chem. 13 (2012) 1583.

[9] S.C. Jung, M.H. Kang, Adsorption of a water molecule on Fe (100): density-functional calculations, Phys. Rev. B 81 (2010) 115460.

[10] R.R.Q. Freitas, R. Rivelio, F.B. Mota, C.M.C. Castilho, Dissociative adsorption and aggregation of water on the Fe (100) surface: a DFT study, J. Phys. Chem. C 116 (2012) 20306.

[11] A.C. Yang, C.I. Weng, Structural and dynamic properties of water near monolayer-protected gold clusters with various alkanethiol tail groups, J. Phys. Chem. C 114 (2010) 8697.

[12] A.C. Yang, C.I. Weng, T.C. Chen, Behavior of water molecules near monolayer-protected clusters with different terminal segments of ligand, J. Chem. Phys. 135 (2011) 034101.

[13] V. Koparde, P. Cummings, Molecular dynamics study of water adsorption on TiO₂ nanoparticles, J. Phys. Chem. C 111 (2007) 6920.

[14] S.H. Park, G. Sposito, Structure of water adsorbed on a mica surface, Phys. Rev. Lett. 89 (2002) 085501.

[15] L. Cheng, P. Fenter, K.L. Nagy, M.L. Schlegel, N.C. Sturchio, Molecular-scale density oscillations in water adjacent to a mica surface, Phys. Rev. Lett. 87 (2001) 156103.

[16] R.S. Neves, A.J. Motheo, R.P.S. Fartaria e, F.M.S.S. Fernandes, Modelling water adsorption on Au (210) surfaces. I. A force field for water-Au interactions by DFT, J. Electrochim. Chem. 609 (2007) 140.

[17] R.S. Neves, A.J. Motheo, R.P.S. Fartaria e, F.M.S.S. Fernandes, Modelling water adsorption on Au (210) surfaces: II. Monte Carlo simulations, J. Electrochim. Chem. 612 (2008) 179.

[18] K. Heizinger, E. Spohr, Computer simulations of water-metal interfaces, Electrochim. Acta 34 (1989) 1849.

[19] E. Spohr, Ion adsorption on metal surfaces. The role of water-metal interactions, J. Mol. Liq. 64 (1995) 91.

[20] W. Smith, DL POLY 2.0: A general-purpose parallel molecular dynamics simulation package, J. Mol. Graph. 14 (1996) 136.

[21] M.P. Allen, D.J. Tildesley, Computer Simulation of Liquids, Clarendon Press, Oxford, 1989.

[22] H.J.C. Berendsen, J.P.M. Postma, W. van Gunsteren, A. DiNola, J.R. Haak, Molecular dynamics with coupling to an external bath, J. Chem. Phys. 81 (1984) 3684.

[23] Y. Wu, H.L. Tepper, G.A. Voth, Flexible simple point-charge water model with improved liquid-state properties, J. Chem. Phys. 124 (2006) 024503.

[24] H.J.C. Berendsen, J.R. Grigera, T.P. Straatsma, The missing term in effective pair potentials, J. Phys. Chem. 91 (1987) 6269.

[25] M.W. Mahoney, W.L. Jorgensen, A five-site model for liquid water and the reproduction of the density anomaly by rigid, nonpolarizable potential functions, J. Chem. Phys. 112 (2000) 8910.

[26] M. Levitt, M. Hirshberg, R. Sharon, K.E. Laidig, V. Daggett, Calibration and testing of a water model for simulation of the molecular dynamics of proteins and nucleic acids in solution, J. Phys. Chem. B 101 (1997) 5051.

[27] H.W. Horn, W.C. Swope, J.W. Pitera, J.D. Madura, T.J. Dick, G.L. Hura, T. Head-Gordon, Development of an improved four-site water model for biomolecular simulations: TIP4P-Ew, J. Chem. Phys. 120 (2004) 9665.

[28] S.W. Rick, A reoptimization of the five-site water potential (TIP5P) for use with Ewald sums, J. Chem. Phys. 120 (2004) 6085.

[29] S.W. Rick, Simulations of ice and liquid water over a range of temperatures using the fluctuating charge model, J. Chem. Phys. 114 (2001) 2276.

[30] J.L.F. Abascal, E. Sanz, R.G. Fernandez, C. Vega, A potential model for the study of ices and amorphous water: TIP4P/Ice, J. Chem. Phys. 122 (2005) 224516.

[31] M.A. Gonzalez, J.L.F. Abascal, A flexible model for water based on TIP4P/2005, J. Chem. Phys. 135 (2011) 224516.

[32] G.S. Fanourgakis, S.S. Xantheas, The flexible, polarizable, thole-type interaction potential for water (TTM2-F) revisited, J. Phys. Chem. A 110 (2006) 4100.

[33] H.A. Stern, F. Rittner, B.J. Berne, R.A. Friesner, Combined fluctuating charge and polarizable dipole models: application to a five-site water potential function, J. Chem. Phys. 115 (2001) 2237.

[34] K.E. Larsson, U. Dahlborg, Some vibrational properties of solid and liquid $\mathrm{H}_{2} \mathrm{O}$ and $\mathrm{D}_{2} \mathrm{O}$ derived from differential cross-section data, J. Nucl. Energy Parts A/B 16 (1962) 81.

[35] A.J. Leadbetter, The thermodynamic and vibrational properties of $H_2O$ ice and $D_2O$ ice, Proceedings of the Royal Society of London. Series A. Mathematical and Physical Sciences 287 (1965) 403.

[36] J.E. Bertie, E. Whalley, Infrared spectra of ices Ih and Ic in the range 4000 to $350\ \mathrm{cm}^{-1}$, J. Chem. Phys. 40 (1964) 1637.

[37] K. Londsdale, The structure of ice, Proc. R. Soc. A 247 (1958) 424.

[38] B. Kamb, Ice. II. A proton-ordered form of ice, Acta Crystallogr. 17 (1964) 1437.

[39] B. Kamb, Overlap interaction of water molecules, J. Chem. Phys. 43 (1965) 3917.

[40] B. Kamb, Structure of ice VI, Science 150 (1965) 205.

[41] B. Kamb, A. Prakash, C. Knobler, Structure of ice. V, Acta Crystallogr. 22 (1967) 706.

[42] A. Ignaczak, J.A.N.F. Gomes, Simulations of liquid water in contact with a Cu (1 0 0) surface, J. Mol. Struct.: Theochem. 464 (1999) 227.

[43] J.P. Devlin, J. Sadlej, V. Buch, Infrared spectra of large $H_2O$ clusters: new understanding of the elusive bending mode of ice, J. Phys. Chem. A 105 (2001) 974.

[44] A.H. Hardin, K.B. Harvey, Temperature dependences of the ice I hydrogen bond spectral shifts, Spectrochim. Acta Part A 29 (1973) 1139.

[45] M.J. Taylor, E. Whalley, Raman spectra of ices Ih, Ic, II, III, and V, J. Chem. Phys. 40 (1964) 1660.

[46] G.E. Walrafen, Y.C. Chu, G.J. Piermarini, Low-frequency Raman scattering from water at high pressures and high temperatures, J. Phys. Chem. 100 (1996) 10363.

[47] K. Mizoguchi, Y. Hori, Y. Tominaga, Study on dynamical structure in water and heavy water by low-frequency Raman spectroscopy, J. Chem. Phys. 97 (1992) 1961.

[48] K. Winkler, J. Lindner, P. Vohringer, Low-frequency depolarized Raman-spectral density of liquid water from femtosecond optical Kerr-effect measurements: lineshape analysis of restricted translational modes, Phys. Chem. Chem. Phys. 4 (2002) 2144.

[49] J.A. Padro, J. Marti, An interpretation of the low-frequency spectrum of liquid water, J. Chem. Phys. 118 (2003) 452.

[50] K.H. Tsai, T.-M. Wu, Local structural effects on low-frequency vibrational spectrum of liquid water: the instantaneous-normal-mode analysis, Chem. Phys. Lett. 417 (2006) 389.

[51] S. Melchionna, G. Ciccotti, Hoover NPT dynamics for systems varying in shape and size, Mol. Phys. 78 (1993) 533.

[52] D. Eisenberg, W. Kauzmann, The Structure and Properties of Water, Oxford University Press, New York, 1969.
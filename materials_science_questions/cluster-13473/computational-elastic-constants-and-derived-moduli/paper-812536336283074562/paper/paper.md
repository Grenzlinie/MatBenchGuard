Journal Pre-proofs

Computational Study of Elastic, Structural Stability and Dynamics properties
of Penta-graphene Membrane

J.M. De Sousa, A.L. Aguiar, E.C. Girão, Alexandre F. Fonseca, A.G. Souza
Filho, D.S. Galvão

![](./images/812536336283074562_1.jpg)

<table>
  <tr>
    <td>PII:</td>
    <td>S0301-0104(20)31177-0</td>
  </tr>
  <tr>
    <td>DOI:</td>
    <td>https://doi.org/10.1016/j.chemphys.2020.111052</td>
  </tr>
  <tr>
    <td>Reference:</td>
    <td>CHEMPH 111052</td>
  </tr>
  <tr>
    <td>To appear in:</td>
    <td>Chemical Physics</td>
  </tr>
  <tr>
    <td>Received Date:</td>
    <td>22 May 2020</td>
  </tr>
  <tr>
    <td>Accepted Date:</td>
    <td>14 November 2020</td>
  </tr>
</table>

Please cite this article as: J.M. De Sousa, A.L. Aguiar, E.C. Girão, A.F. Fonseca, A.G. Souza Filho, D.S. Galvão,
Computational Study of Elastic, Structural Stability and Dynamics properties of Penta-graphene Membrane,
Chemical Physics (2020), doi: https://doi.org/10.1016/j.chemphys.2020.111052

This is a PDF file of an article that has undergone enhancements after acceptance, such as the addition of a cover
page and metadata, and formatting for readability, but it is not yet the definitive version of record. This version
will undergo additional copyediting, typesetting and review before it is published in its final form, but we are
providing this version to give early visibility of the article. Please note that, during the production process, errors
may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

© 2020 Published by Elsevier B.V.

# Computational Study of Elastic, Structural Stability and Dynamics properties of Penta-graphene Membrane

J. M. De Sousa$^{a,*}$, A. L. Aguiar$^{b}$, E. C. Girão$^{b}$, Alexandre F. Fonseca$^{c}$, A. G. Souza Filho$^{d}$, D. S. Galvão$^{c,e}$

$^{a}$Instituto Federal do Piauí - IFPI, São Raimundo Nonato, Piauí 64770-000, Brazil.
$^{b}$Departamento de Física, Universidade Federal do Piauí, CEP 64049-550, Teresina, Piauí, Brazil
$^{c}$Applied Physics Department, State University of Campinas, Campinas, SP, 13083-970, Brazil.
$^{d}$Departamento de Física, Universidade Federal do Ceará, CEP 60455-900, P.O. Box 6030, Fortaleza, Ceará, Brazil
$^{e}$Center for Computing in Engineering and Sciences, State University of Campinas - UNICAMP, Campinas, 13083-859, SP, Brazil.

## Abstract
Recently, a new two-dimensional carbon allotrope called Penta-graphene membrane was proposed. The Penta-graphene membrane exhibits mechanical and electronic interesting properties, including typical band gap values of semiconducting materials. Penta-graphene membrane has a Cairo-tiling-like 2D lattice of non coplanar pentagons and its mechanical properties still have not been fully investigated. In this work, we combined reactive molecular dynamics (MD) simulations and density functional theory (DFT) calculations to investigate the mechanical properties and fracture patterns of Penta-graphene membranes under tensile stress. We show that Penta-graphene membranes can hold up to 20% of strain and that fracture occurs only after substantial dynamical bond breaking and the formation of 7, 8 and 11 carbon rings, as well as carbon chains. The stress-strain behavior was observed to follow two regimes, one exhibiting linear elasticity followed by a plastic one, involving carbon atom re-hybridization with the formation of carbon rings and chains.

**Keywords:** penta-graphene, mechanical properties, DFT, reactive molecular

---
*Corresponding author*
Email address: josemoreiradesousa@ifpi.edu.br (J. M. De Sousa)

Preprint submitted to Chemical Physics
September 1, 2020

dynamics, nanotechnology, fracture

## 1. Introduction

Graphene is one of the most important topics in materials science today [1, 2, 3, 4, 5, 6, 7, 8]. Several studies have focused on physical and/or chemical modifications of the perfect honeycomb lattice, since its zero band gap limits the development of some pure graphene-based electronic devices [9]. Functionalization of graphene [10, 11], and graphene nanoribbons [12] are examples of strategies used to tune the band gap aiming the incorporation of carbon-based materials in electronics applications. On the other hand, the scientific community has a strong interest on developing other layered structures which have a band gap. Hexagonal boron-nitride [13, 14], carbon nitride nanosheets [15, 16, 17], metal dichalcogenides [18, 19], and silicene membranes [20, 21, 22] are examples of other two-dimensional structures that overcome graphene "bandgapless" limitation. Other pure carbon structures such as graphynes [23, 24, 25, 26, 27], fullerene-based sheets [28] and haeckelites (nanostructured 2D systems formed by pentagonal, hexagonal and heptagonal rings of carbon atoms) [29] are also good candidates for future devices development.

Recently, a new 2D carbon allotrope called *penta-graphene* (as illustrated in Figure 1) has been proposed by Zhang *et al.* [30]. Such membranes have a unique arrangement of carbon atoms in a network of non-coplanar pentagons, similar to a *Cairo pentagonal tiling*, as shown by DFT calculations [31]. They also showed that Penta-graphene is not only mechanically and thermodynamically stable, but also presents a large band gap of 3.25eV [30]. Besides that, it also exhibits interesting thermal and mechanical properties, such as negative Poisson's ratio (auxetic behaviour [32]) due to its metastability and intricate atomic structural configuration. Figure 1 shows the Penta-graphene membrane frontal and lateral views.

So, many theoretical studies have been already devoted to Penta-graphene and its stability has been the subject of debate [33, 34]. So, inspired by the

![](./images/812536336283074562_2.jpg)

Figure 1: Frontal (top) and lateral (bottom) views of a Penta-graphene membrane. The arrows indicate the directions of the applied tensile deformations considered in this study. The figure inset shows the Penta-graphene square unit cell, with lattice parameter $a=3,64$ Å.

new carbon allotrope composed by non-coplanar pentagons, a lot of studies, such as first-principles studies and molecular dynamics methods, suggest that Penta-graphene membrane and functionalized penta-graphene membrane are stable and have interesting electronic, mechanical and thermal properties properties [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]. Its thermal conductivity at room temperature has been estimated by different methods to be about 167 W/mK [47] (from MD simulations) and 645 W/mK [48] (from first principles calculations). In addition, atomistic simulations based on first principles show that Penta-graphene membrane have potential applications as anode material for a Li/Na-ion battery [49], as a metal-free catalyst for carbon allotrope oxidation [50], as adsorption behaviors of small molecules [51], thermal conductivity of monolayer and bilayer Penta-graphene membrane at room temperature [52],

that nitrogen doping of $sp_2$-like carbons atoms in Penta-graphene membrane can produce a bandgap modulation between semimetallic and semiconductor behav- ior [53], as a promising template for nanobiological devices and could be used for sensing of biomolecules such as a strong physisorption exists in DNA/RNA and nucleobases/base pairs-Penta-graphene membrane complexes [54], as a promis- ing controllable $CO_2$ capture and separation material in an electric field [55], penta-graphene nanoribbons as potential applications in spin electronics, opto-electronic devices and solar cells [56], an applications in spintronic devices [57] and among others.

Penta-graphene nanoribbons have also been theoretically investigated in terms of stability and electronic band structure. These quasi-1D systems have been shown to preserve the semiconducting character from their layer parent counterpart and the gap value depends on their width [58]. Similar to graphene, Penta-graphene functionalization (hydrogenation and fluorination) allows tun- ing its electronic and mechanical properties [44]. In special, an unexpected increasing in thermal conductivity was observed for the case of a hydrogenated membrane [59]. Recently, interesting mechanical and structural behaviors for the Penta-graphene membrane were reported based on reactive molecular dy- namics (MD) simulations [60]. It has been predicted that a structural transition from Penta-graphene membrane to graphene (or from Penta-graphene mem- brane to hexagraphene) can occur as a result of thermal and/or tensile strains, thus leading to the assumption that Penta-graphene and graphene 2D might be considered different structural phases of the same material [60]. On the other hand, DFT based calculations suggest that a transition from Penta-graphene to biphenylene takes place under uniaxial stress [61]. Such reports indicates that further investigation is needed in order to understand the behavior of Penta- graphene membrane under tensile stress and its further rupture. In this paper, we combine density functional theory (DFT) calculations and reactive classical MD simulations (with a properly chosen set of potential parameters) to inves- tigate the fracture patterns of Penta-graphene membrane under axial tensile strain, as schematically shown in Fig. 1. So, our results reveal the formation

of structures with 7, 8 and 11 carbon rings and carbon chains, just before the mechanical failure (fracture), which happens at about 20% of strain. Such a result show a closer agreement to the recent results from Ref. [60, 61]. Both Young's modulus and Poisson's ratio of Penta-graphene membrane were also calculated and compared with the original *ab initio* predictions [30].

## 2. Methods

We combined classical (MD), and quantum (DFT) methods to investigate the structural and dynamical aspects of Penta-graphene membrane under tensile stress, up to the limit of mechanical failure (fracture). In the following sections we provide technical details on the computational techniques used in this work.

### 2.1. MD simulations

The MD simulations were performed using the reactive force field (ReaxFF) [62, 63]. The numerical integration of the Newton's equations was performed in the large-scale atomic / molecular massively parallel simulator (LAMMPS) code [64]. ReaxFF is a reactive force field developed by van Duin, Goddard III and co-workers, which is designed to be a bridge between quantum chemical force fields and empirical bonding energy terms. ReaxFF is parameterized using available experimental data and/or using DFT calculations. In ReaxFF, the total bond energy between atoms are obtained through the computation of all interatomic distances and updated at every time step of the classical MD runs. In this way, the structural connectivity is determined uniquely by the atomic positions, thus allowing the ReaxFF to create and break (dissociate) chemical bonds in a dynamical way, through the whole simulation. This is important to describe not only the equilibrium structures, but also the fracture patterns of the investigated systems. The energy of the system is divided into partial energy contributions, which include bonded and non-bonded terms as follows [62]:

$$
E_{system} = E_{bond} + E_{over} + E_{under} + E_{val}
$$

$$
\begin{aligned}
&+E_{p e n}+E_{t o r}+E_{c o n j}+E_{v d W} \\
&+E_{c o} \quad,
\end{aligned} \quad(1)
$$

where each term, respectively, represents the energies corresponding to the bond distance, the over-coordination, the under-coordination, the valence, the penalty for handling atoms with two double bonds, the torsion, the conjugated bond energies, the van der Waals, and coulomb interactions, respectively. ReaxFF has been extensively used in the study of the dynamic aspects of nanostructures, such as fractures of graphynes 2D and 1D [65, 66, 67], carbon nitride 2D [68], re-active process of hydrogenation of highly twisted carbon nanotubes [69], ballistic penetration of graphene sheets [70], carbon and boron nitride nanoscrolls at high impact collisions [71], connected carbon nanorings [72], carbyne [73, 74], degra-dation of graphene and graphdiyne membranes in gaseous atmospheres [75, 76], among other carbon based nanostructures.

Here, for the study of structural and fracture mechanics of Penta-graphene membrane, we considered square membranes under periodic boundary conditions with dimensions of approximately $80\ \mathring{\mathrm{A}} \times 80\ \mathring{\mathrm{A}}$. In all calculations, these structures were initially thermalized at 300 K and 0 atm in a $NPT$ ensemble, in order to obtain an equilibrated structure before the beginning of the fracture dynamics study. After that, a stretching process was then considered within a $NVT$ ensemble, also at $300K$, with the temperature controlled by a Nose-Hoover thermostat [77], as implemented in the LAMMPS [64] code. Although it is expected that there are thermal effects on the elastic properties, in a previous work [60] it was showed that exists a thermal transition from penta-graphene to graphene at about 600K. In this sense, to avoid mixing the strain and thermal effects, we opted to consider the MD simulations only for room temperature (300 K).

In our calculations, the timestep of numerical integration was set to 0.05 fs, and a constant engineering strain rate of $\delta=10^{-6} fs^{-1}$ was considered. These values were chosen to be small enough that the system has time to fully relax before the next length increment.

The above conditions were maintained up to the mechanical failure. The mechanical properties of the Penta-graphene membrane were analyzed by the stress-strain relationship, where the engineering strain, $\varepsilon$, under tension is defined as

$$
\varepsilon=\frac{\zeta-\zeta_{0}}{\zeta_{0}}=\frac{\Delta \zeta}{\zeta_{0}}, \quad (2)
$$

where $\zeta_{0}$ and $\zeta$ are the length of the structure before and after the dynamics of deformation, respectively. The *per-atom* stress tensor of each carbon atom are calculated by [78]:

$$
\sigma_{\alpha \beta}=\frac{1}{\Gamma} \sum_{i}^{N}\left(m_{i} v_{\alpha i} v_{i \beta}+r_{i \alpha} f_{i \beta}\right), \quad (3)
$$

where $\Gamma$ is the atom volume, $N$ the number of atoms, $m_{i}$ the mass of carbon atoms, $v$ the velocity, $r$ the coordinates of the carbon atoms and $f_{i \beta}$ is the $\beta$ component of the force acting on the $i$-th atom. In order to perform a more detailed analysis of the distribution of stress along the structure during the fracture process, we also calculated the quantity known as *von Mises stress*, $\sigma_{v M}$, which is mathematically given by [78]:

$$
\sigma_{v M}=\left[\frac{\left(\sigma_{x x}-\sigma_{y y}\right)^{2}+\left(\sigma_{y y}-\sigma_{z z}\right)^{2}+\left(\sigma_{z z}-\sigma_{x x}\right)^{2}+6\left(\sigma_{x y}+\sigma_{y z}+\sigma_{z x}\right)^{2}}{2}\right]^{\frac{1}{2}}, \quad (4)
$$

where $\sigma_{x y}, \sigma_{y z}$ and $\sigma_{z x}$ are shear stress components. This methodology is widely used in atomistic simulations involving nanostructured systems formed by atoms of carbon [79, 80, 81, 82], as well as hybrid C and N systems [17], and silicene [83], for instance. It allows a dynamical visualization (qualitatively) of where the stress is accumulated and/or dissipated during the stretching/fracture process along the whole structure.

### 2.2. DFT calculations

For quantum mechanical calculations, we used a LCAO-based DFT ap- proach [84, 85], as implemented in the SIESTA code [86, 87]. The Kohn-Sham orbitals were expanded in a double-$\zeta$ basis set composed of numerical pseu- doatomic orbitals of finite range enhanced with polarization orbitals. A common

atomic confinement determined by an energy shift of 0.02 $Ry$ was used to define the cutoff radius for the basis functions, while the fineness of the real space grid was determined by a mesh cutoff of 400 Ry [88]. For the exchange-correlation potential, we used the generalized gradient approximation (GGA) [89], and the pseudopotentials were modeled within the norm-conserving Troullier-Martins [90] scheme in the Kleinman-Bylander [91] factorized form. Brillouin-zone integrations were performed by using a Monkhorst-Pack[92] grid of $8 \times 8 \times 1$ $k$-points. All geometries were fully optimized for each strain level given by Eq.2 until the maximum force component on any atom was less than $10\ \text{meV}/\text{\AA}$. The lattice vectors were manually deformed along selected directions (uniaxial and biaxial) and the coordinates of carbon atoms were rescaled along these directions before full convergence. Periodic boundary conditions were imposed, with a perpendicular off-plane lattice vector $\text{a}_z$ large enough $(20\ \text{\AA})$ to prevent spurious interactions between periodic images. For uniaxial stretching, we have considered two cases: with and without constrains along the perpendicular in-plane directions. The stress tensor $\sigma_{ij}$ is related to strain tensor $\varepsilon_{ij}$ $(i,j=x,y,z)$ by $\sigma_{ij}=(1/S)(\partial U/\partial \varepsilon_{ij})$, where $S=(\vec{a_x} \times \vec{a_y})$ is the area of the unit cell. For each strained structural geometry relaxation, the SCF convergence thresholds for electronic total energy were set to $10^{-4}$ eV.

## 3. Results

### 3.1. Choice of ReaxFF parameters

Before starting the MD study of the Penta-graphene membrane fracture, we performed DFT- and MD-based calculations tests to use as benchmark for the choice of the multiple avaialble ReaxFF parameters sets. Among the possible choices, we considered four different ReaxFF sets, as developed by Mueller *et al.* [63], Mattsson *et al.* [93], Chenoweth *et al.* [94], and Srinivasan *et al.* [95]. These parameters were developed for carbon in different multicomponent systems. The one from Srinivasan, for instance, was recently developed for condensed phases of carbon. The tests consist in the calculation of the thickness,

Young's modulus ($Y$), and Poisson's ratio ($\nu$) of Penta-graphene membrane using the same protocols by Zhang *et al.* [30] These quantities are computed from the elastic constants $C_{11}$ and $C_{12}$ through the use of the following equations:

$$
Y = \frac{C_{11}^2 - C_{12}^2}{C_{11}}, \tag{5}
$$

and

$$
\nu = \frac{C_{12}}{C_{11}}. \tag{6}
$$

The elastic constants $C_{11}$ and $C_{12}$ were obtained from energy minimization calculations of the structure in what can be called uniaxial and biaxial tensile stresses tests, respectively. If the elastic strain energy per area of a two-dimensional system can be written as:

$$
U(\epsilon) = 0.5C_{11}\epsilon_{xx}^2 + 0.5C_{22}\epsilon_{yy}^2 + C_{12}\epsilon_{xx}\epsilon_{yy}, \tag{7}
$$

where $C_{11}$, $C_{22}$ and $C_{12}$ are components of the elastic modulus tensor of the structure, and 1 and 2 correspond to $x$ and $y$ directions, respectively, then the uniaxial and bi-axial tensile stresses can be defined as follows. For the penta-graphene structure, $C_{11}=C_{22}$, so it will be enough to apply a uniaxial tensile stress test along either one of the $x$ or $y$ directions to obtain $C_{11}$ or $C_{22}$. If a uniaxial tensile strain along $x$ direction is applied to the penta-graphene and the structure size at $y$ direction is kept fixed, i. e., $\epsilon_{yy}=0$, the energy of the structure will be $U=0.5C_{11}(\epsilon_{xx})^2$. By fitting the energy of the structure versus $\epsilon_{xx}$ by a quadratic function for small $\epsilon_{xx}$, we obtain $C_{11}$ and, consequently, $C_{22}$. If a biaxial tensile strain is applied along $x$ and $y$ directions at the same time and keeping $\epsilon_{xx}=\epsilon_{yy}\equiv\epsilon$, then the energy of the structure will be $U=(C_{11}+C_{12})\epsilon^2$, and by fitting this energy versus $\epsilon$ again by a quadratic function, we will obtain $(C_{11}+C_{12})$ and, therefore, $C_{12}$. With $C_{11}$ and $C_{12}$, we calculate Young's modulus and Poisson's ratio using equations (5) and (6). This method has been successfully used to obtain the Young's modulus and Poisson's ratio of some families of graphyne and graphdiyne structures [96]. The energy minimizations were calculated with convergence tolerances of 0 and $10^{-8}\ Kcal/mol\text{·}\mathring{A}$ for the energy and force, respectively.

In Table (1) we present the results previously reported in Ref. [30] for $Y$ and $\nu$, as well as the DFT and ReaxFF (four different parameters sets) results obtained in our simulations.

Table 1: Comparison of structural and mechanical properties of Penta-graphene membrane structures obtained by DFT from Ref. [30], our DFT calculations, and our MD ReaxFF [63, 93, 94, 95] calculations, respectively.

<table>
  <thead>
    <tr>
      <th>Method</th>
      <th>Thickness (Å)</th>
      <th>Young's Modulus (GPa.nm)</th>
      <th>Poisson's ratio</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>DFT from Ref. [30]</td>
      <td>1.20</td>
      <td>263.8</td>
      <td>-0.068</td>
    </tr>
    <tr>
      <td>DFT from our calculations</td>
      <td>1.23</td>
      <td>257.6</td>
      <td>-0.096</td>
    </tr>
    <tr>
      <td>ReaxFF - Mattsson</td>
      <td>0.882</td>
      <td>150.5</td>
      <td>-0.154</td>
    </tr>
    <tr>
      <td>ReaxFF - Srinivasan</td>
      <td>1.34</td>
      <td>133.9</td>
      <td>0.366</td>
    </tr>
    <tr>
      <td>ReaxFF - Muller</td>
      <td>1.05</td>
      <td>322.0</td>
      <td>0.335</td>
    </tr>
    <tr>
      <td>ReaxFF - Chenoweth</td>
      <td>1.09</td>
      <td>197.0</td>
      <td>0.380</td>
    </tr>
  </tbody>
</table>

From this table we can see a good agreement between our DFT (performed with a localized orbital basis) results and those from Ref. [30] (which used a plane-wave basis set), including the prediction of the auxetic behavior. There are several set parameters for ReaxFF in the literature, which leads to the question about which is the most appropriate to study a specific structure. Our parameter choice was based on obtaining the closest agreement with Zhang et al. [30] DFT Young's modulus value. We observe that the Mattsson [93] set of parameters is the only one which correctly predicts the sign of Penta-graphene Poisson's ratio. However, it presents a much softer structure (smaller membrane thickness and smaller Young's modulus than those calculated from DFT). The Srinivasan [95] set of parameters predicts reasonable thickness but a much smaller elastic modulus than that obtained from DFT. On the other hand, the Mueller [63] and the Chenoweth [94] sets of parameters present the best matches for the thickness and Young's modulus as compared with both DFT calculations. If we take the results from Zhang et al. [30] as reference, both Mueller's and the

Chenoweth's sets give smaller thickness with similar deviations. On the other hand, those two parameter sets show distinct trends for the Young's Modulus: $Y$ is $\sim 22\%$ higher for Muller's and $\sim 25\%$ lower for Chenoweth's in comparison with Zhang's DFT result. For the physical aspects of the phenomenon we are investigating here, the thickness and Young's modulus parameters are the most important to be precisely described. In this sense the Chenoweth's [94] and Mueller's [63] set of parameters would be the best choice. As Chenoweth [94] set was already used in Ref. [60] to investigate Penta-graphene membrane under tensile strain, we decided to use Mueller's set [63] in our calculations. As these two paramater sets have opposite trends for $Y$, this allow a broad view on the mechanical properties of Penta-graphene membrane once we compare our results with the previous literature. While the plastic regime starts at about 10% of strain, for Mueller's set of ReaxFF parameters, fracture takes place at about 20%, which is very close to the 19.5% failure strain predicted from our DFT calculations (Zhang et al [30] had not calculated the failure strain under appli- cation of uniaxial tensile stress). In addition, Mueller's set has been used to test the room-temperature stability of Penta-graphene membrane. Our preliminary calculations showed that Penta-graphene membrane characteristics (thickness and crystallinity) have been stable up to 300K with no significant changes.

### 3.2. MD results

We start discussing our results based on MD. In Figure 2 we present the stress-strain curve based on the Mueller [63] set of ReaxFF parameters. We ob- serve two regimes, an elastic one (regime 1) and a second plastic regime (regime 2), plastic in the sense that the totally structural recovery is no longer possible, resulting from permanent deformations due to local structural reconstructions, as shown in Fig. 3. While the plastic regime starts at about 10% of strain, fracture takes place at about 20%, which is very close to the maximum of 19.5% failure strain predicted from our DFT calculations.

In Figure 3a we present MD snapshots of strained membranes, including one close to the fracture, where the formation of many carbon chains can be seen.

![](./images/812536336283074562_3.jpg)

Figure 2: Penta-graphene membrane stress-strain curve. The vertical full line divides the curve into elastic (regime 1) and plastic (regime 2). Over-imposed red line on the stress-strain curve indicates the average inclinations in both regimes. The arrow indicates the fracture point of the fracture of Penta-graphene membrane.

In Figures 3b-d we present representative MD snapshots of the plastic regime, where it is possible to observe the existence of 7, 8 and 11 carbon rings. These rings are formed from the reconstruction of broken $C-C$ bonds. In figure 4, we show representative MD snapshots representing the von Mises stress values of tensioned Penta-graphene membranes. In this figure one can identify regions of high (in red color) and low stress (in blue color), so that von Mises stress analysis allows an easy identification of the reconstructions which occur as a result of local stress concentration during the dynamical stretching. By looking at von Mises stress, we also can clearly identify the region of fracture. Details of the carbon chains that are formed at large tension strains, just before final rupture of the structure, are shown in Fig. 5. The distances between the carbon

atoms along the chains indicate the formation of a structure having alternating single and triple bonds, corresponding to the so called polyynic configuration. This chain configuration is the most stable linear structure, as predicted through computational calculations for incomplete fractures in graphene membranes (for which is observed the formations of long stable carbon chains [97]).

![](./images/812536336283074562_4.jpg)

Figure 3: (a) Representative MD snapshots of tensioned Penta-graphene membrane at 0% (leftmost panel), 19.7% (middle panel) and 20% (rightmost panel) strains. (b), (c) and (d) are representative MD snapshots showing the existence of 7, 8, 11 rings formed at 18%, 18.5% and 18.7% strains.

These results show a good agreement to the theoretical investigations [60, 61], which predicted that the Penta-graphene membrane evolve the structural transition, during either tensile or thermal strains, although structural defects were also present.

### 3.3. DFT results

We have carried out DFT calculations on the Penta-graphene membrane structures under uniaxial and biaxial tensile strains up to the limit of rupture. One of the goals in these calculations is to identify intermediate structures

![](./images/812536336283074562_5.jpg)

Figure 4: Representative MD snapshots showing the von Mises stress values of Penta-graphene membrane at (a) 19%, (b) 19.50% and (c) 20% strains. The scale bar represents the renormalized values of local von Mises stress to indicate low (blue) and high (red) stressed regions.

![](./images/812536336283074562_6.jpg)

Figure 5: Structural details of a carbon chain formed at the last stages of a Penta-graphene membrane. (a) Structure just before final breaking using von Misses color code to identify stress concentration. (b) Carbon atoms are labeled to identify the single and triple bonds that forms along the chain. Numerical values are in Angstroms. The scale bar represents the renormalized values of local von Mises stress to indicate low (blue) and high (red) stressed regions)

in order to get further insight into the fracture dynamics. In addition, we
want to use this DFT analysis to shed light on the comparison of the MD

results using different sets of ReaxFF parameters to describe the membrane mechanical properties. Two distinct choices for the Penta-graphene membrane unit cell were used in order to investigate differences in failure mechanisms. These units cells were labeled R0 and R45 (rotated of $45^{\circ}$ from R0) as shown in Fig. 6a. It is interesting to note that R45 have neither perpendicular nor parallel C-C bonds along uniaxial $x$ and $y$ strain directions. However, the R0 structure has both types of bonds, which will play a significant hole just before the rupture under uniaxial strain. We have calculated the energy shift due to the in-plane strain to determine the Penta-graphene mechanical stability. For a 2D membrane, using the standard Voigt notation (1-$xx$, 2-$yy$, and 6-$xy$), the elastic strain energy per unit area can be expressed as a function of $C_{11}$ , $C_{22}$ and $C_{12}$ elastic modulus tensor, corresponding to second partial derivative of strain energy with respect to strain. The elastic constants can be derived by fitting the energy curves associated with uniaxial and equi-biaxial strains. The curves are plotted in Fig. 6b. We should note here that the mechanical behavior of R0 and R45 structures are almost the same in low-strain regime (up to 5%), producing similar results for the elastic constants. Under uniaxial $\varepsilon_{xx}$ strain, i.e. $\varepsilon_{yy}=0$, the energy follows $U(\varepsilon_{xx})=1/2C_{11}\varepsilon_{xx}^{2}$. Parabolic fitting of the uniaxial strain curve yields $C_{11}=277.5$ GPa$\cdot$nm. Under equi-biaxial strain, $\varepsilon_{yy}=\varepsilon_{xx}$, we have $U(\varepsilon_{xx})=(C_{11}+C_{12})\varepsilon_{xx}^{2}$. By fitting the equi-biaxial strain curve we obtain $C_{11}+C_{12}=250.8$ GPa$\cdot$nm, hence, $C_{12}=-26.7$ GPa$\cdot$nm. The in-plane Young's modulus is calculated to be as large as 274.95 GPa$\cdot$nm, which is very similar to what was observed by other authors [30]. We also note that $C_{12}$ is negative for this membrane, leading to a negative Poisson's ratio (NPR),$\nu=-0.096$. This result confirms that Penta-graphene membrane is an auxetic material. We also studied the ideal Penta-graphene membrane strength and failure mechanism by calculating the variation of stress as a function of the equi-biaxial and uniaxial tensile strain. The results are presented in Fig. 6c, which show that the strain at the maximum stress before failure is 19.5% and 23% for uniaxial and biaxial strains, respectively.

The simulation of uniaxial stretching with the in-plane perpendicular lattice

vector fixed also allowed the computation of the residual perpendicular stress components (not shown in Fig. 6c), which exhibit negative values. Furthermore, when no constrains are imposed to uniaxial loading, the length of the perpendic- ular lattice vector increases, which is an additional evidence that Penta-graphene membrane is an auxetic material. For equi-biaxial stretching loading, we plot $(\sigma_{xx}+\sigma_{yy})$ in Fig 6c. Therefore, we observed that Penta-graphene membrane is very strong, with the ultimate tensile strength (UTS) given by ~38GPa.nm (R0 uniaxial), and ~29GPa.nm (R45 uniaxial). This discrepancy will be further discussed. For biaxial stretching, we obtained UTS of ~52GPa.nm (biaxial) independent of the R0 or R45 conformation.

In Fig. 7a-b, we present Penta-graphene membrane snapshots for R0 and R45 structures, respectively before and after failure caused by a maximum of 20% for x-axis stretching (similar results were obtained for y-axis stretching, not shown). Penta-graphene membrane fractured membranes of Fig. 7a-b were duplicated along x- and y-direction in Fig 7c-d for a better visualization of the fracture patterns (see colored non-pentagonal rings). It is interesting to note that the patterns of R0 and R45 ruptured structures after 20% of strain are similar, with the formation of thin porous membranes with $8-C$ rings for both strained directions (cf. Fig. 7c-d). However, we note significant differences in R0 and R45 structures concerning the maximum of tensile stress under uniaxial stretching just before the rupture, as we can see in Fig. 6c. We obtained ~38GPa.nm (R0), and ~29GPa.nm (R45) for this quantity. We can explain such a difference in terms of the parallel C-C bonds present in R0 structure, which play a significant role at 19% of strain, as one can see in Fig. 8a.

For symmetry reasons, the original Penta-graphene membrane structure (no stressed) has only two types of C-C bonds, which connect both tri-coordinated atoms (1.33Å) and also tri- and tetra-coordinated atoms (1.55Å), independent of the R0 and R45 unit cell construction. However, when subjected to uniax- ial loading, those bonds are stressed differently. At 19% of strain, the parallel aligned C-C bonds in R0 structure are stressed up to 1.46Å, while the perpen- dicular C-C bonds remains with the same length of zero-strain structure, as we

![](./images/812536336283074562_7.jpg)

Figure 6: (a) R0 and (b) R45 unit cells used to study Penta-graphene membrane failure mechanisms. The Penta-graphene membrane primitive cell (yellow square) was $2\times2$ ($3\times3$) replicated for R0 (R45) structure in order to model the fracture process. (c) Penta-graphene membrane strain-energy curves in low-strain regime. Parabolic fitting was used to estimate the Young's modulus value (see text). (d) Penta-graphene membrane strain-stress curves for R0 and R45 under equi-biaxial and uniaxial stretching. Equi-biaxial (black and green) curves is $(\sigma_{xx}+\sigma_{yy})$ stress versus strain $(\varepsilon_{xx})$. Uniaxial curves is $(\sigma_{xx})\sigma_{yy}$ versus $(\varepsilon_{xx})\varepsilon_{yy}$ strain.

can observe in Fig. 8a (top panels). In R45 conformation, at 19% of strain, the same C-C bonds are slightly elongated to $1.37Å$.

Therefore, as we have C-C bonds (between tri-coordinated atoms) parallel to the strain direction in the R0 structure, we observe larger stress for the R0

![](./images/812536336283074562_8.jpg)

Figure 7: Snapshots of Penta-graphene membrane under 2.5% and 20% of uniaxial strain indicated by red arrows. (a) R0 structure after uniaxial stretching converges to 8-porous structures aligned to diagonal direction. A residual $\sigma_{xy}$ stress component is obtained which indicated that those structure after the failure point is not energetically stable. (b) R45 structure after uniaxial stretching converges to 8-porous structures aligned to perpendicular direction. No residual $\sigma_{xy}$ stress component are observed which indicated that those structure after failure point is energetically stable. Extended Penta-graphene membrane porous membranes after failure strain are also shown. Uniaxial strain of 20% along the $x$-axis for R0 structure (c) and R45 structure (d). Porous of 8 (blue) carbon atoms rings are highlighted for better visualization.

case as the strain is directly transmitted to these bonds, differently from the R45 arrangement. During the biaxial loading, as we can observe from Fig. 8b, similiar C-C bond lengths are obtained for tri- and tetra-coordinated atoms, which can explain why biaxial stress-strain curves are very similar for R0 and R45 structure.

These DFT results (and those from Ref. [61]) are closer to our MD simulations (using Mueller's parameter set [63]) in comparison to those reported in

![](./images/812536336283074562_9.jpg)

Figure 8: (a) R0 (top) and R45 (down) structures under 19% of uniaxial strain. (b) R0 (top) and R45 (down) structures under 19% of biaxial strain. Carbon-Carbon bonds lengths in Å units are shown in detail. Carbon atoms from primitive unit cell are highlighted in black for better visualization.

Ref. [60]. Apart from differences related to temperature effects and sample size, the main reason for differences between the classical results lies in the softness of the material as differently predicted by the different simulation set parameters. However, as we do not observe hexagons during the fracture process (as investigated by DFT), this does not suggest a structural transition from Penta-graphene membrane to hexagraphene. This allows us to argue that the Muller's set of ReaxFF parameters seems to be more suitable to describe the fracture of Penta-graphene membrane as its predictions are closer to that from ab initio calculations.

### 4. Concluding remarks

In this work, we have investigated the mechanical properties and fracture patterns of Penta-graphene membrane. We have combined DFT and Molecular Dynamic Method with interatomic force field ReaxFF. The stress-strain behav- ior was observed to follow two regimes, one exhibiting linear elasticity followed by a plastic one (involving carbon atom re-hybridization and bond breaking). The auxetic character of Penta-graphene membrane (negative Poisson's ratio) was confirmed and a nanostructural transition. We show that Penta-graphene membrane can hold up to 20% of strain and that fracture occurs only after sub- stantial dynamical bond breaking, when we observe the formation of 7, 8 and11 carbon rings and carbon chains prior complete fracture.

### Acknowledgements

This work was supported in part by the Brazilian Agencies CAPES, CNPq and FAPESP. J.M.S and D.S.G. thank the Center for Computational Engi- neering and Sciences at Unicamp for financial support through the So Paulo Research Foundation (FAPESP)/CEPID grant #2013/08293-7. A.L.A acknowl- edges CENAPAD-SP for computer time and the Brazilian agencies CNPq (grants427175/2016-0 and 313845/2018-2) for financial support. E.C.G. acknowledges support from CNPq (Process No. 307927/2017 2) and Coordenacao de Aper- feicoamento de Pessoal de Nivel Superior (CAPES) through the Science Without Borders program (Project Number A085/2013). A.F.F. is a fellow of the Brazil- ian Agency CNPq (#311587/2018-6) and acknowledges support from FAPESP grant #2018/02992-4. AGSF thank the Fundacao Cearense de Apoio ao De- senvolvimento Cientifico e Tecnológico for financial support through Grants PRONEX PR2-0101-853 00006.01.00/15 and PNE-0112-00048.01.00/16. The authors J.M.S, A.L.A and E.C.G thank the Laboratorio de Simulacao Com- putacional Cajuína (LSCC) at Universidade Federal do Piauí for computational support.

### References

[1] K. S. Novoselov, A. K. Geim, S. Morozov, D. Jiang, M. Katsnelson, I. Grigorieva, S. Dubonos, A. Firsov, Two-dimensional gas of massless dirac fermions in graphene, nature 438 (7065) (2005) 197-200.

[2] S. Park, R. S. Ruoff, Chemical methods for the production of graphenes, Nature nanotechnology 4 (4) (2009) 217-224.

[3] W. Gao, L. B. Alemany, L. Ci, P. M. Ajayan, New insights into the structure and reduction of graphite oxide, Nature chemistry 1 (5) (2009) 403-408.

[4] S. Stankovich, D. A. Dikin, G. H. Dommett, K. M. Kohlhaas, E. J. Zimney, E. A. Stach, R. D. Piner, S. T. Nguyen, R. S. Ruoff, Graphene-based composite materials, nature 442 (7100) (2006) 282-286.

[5] A. K. Geim, Graphene: status and prospects, science 324 (5934) (2009) 1530-1534.

[6] H. Chen, M. B. Müller, K. J. Gilmore, G. G. Wallace, D. Li, Mechanically strong, electrically conductive, and biocompatible graphene paper, Advanced Materials 20 (18) (2008) 3557-3561.

[7] G. Eda, M. Chhowalla, Graphene-based composite thin films for electronics, Nano Letters 9 (2) (2009) 814-818.

[8] F. Scarpa, S. Adhikari, A. S. Phani, Effective elastic mechanical properties of single layer graphene sheets, Nanotechnology 20 (6) (2009) 065709.

[9] F. Withers, M. Dubois, A. K. Savchenko, Electron properties of fluorinated single-layer graphene transistors, Physical review B 82 (7) (2010) 073403.

[10] Y. Xu, H. Bai, G. Lu, C. Li, G. Shi, Flexible graphene films via the filtration of water-soluble noncovalent functionalized graphene sheets, Journal of the American Chemical Society 130 (18) (2008) 5856-5857.

[11] T. Ramanathan, A. Abdala, S. Stankovich, D. Dikin, M. Herrera-Alonso, R. Piner, D. Adamson, H. Schniepp, X. Chen, R. Ruoff, et al., Functional- ized graphene sheets for polymer nanocomposites, Nature nanotechnology3 (6) (2008) 327-331.

[12] Y.-W. Son, M. L. Cohen, S. G. Louie, Half-metallic graphene nanoribbons, Nature 444 (7117) (2006) 347-349.

[13] G. Giovannetti, P. A. Khomyakov, G. Brocks, P. J. Kelly, J. Van Den Brink, Substrate-induced band gap in graphene on hexagonal boron nitride: Ab initio density functional calculations, Physical Review B 76 (7) (2007)073103.

[14] K. Watanabe, T. Taniguchi, H. Kanda, Direct-bandgap properties and evi- dence for ultraviolet lasing of hexagonal boron nitride single crystal, Nature materials 3 (6) (2004) 404-409.

[15] P. Niu, L. Zhang, G. Liu, H.-M. Cheng, Graphene-like carbon nitride nanosheets for improved photocatalytic activities, Advanced Functional Materials 22 (22) (2012) 4763-4770.

[16] A. Thomas, A. Fischer, F. Goettmann, M. Antonietti, J.-O. Müller, R. Schlögl, J. M. Carlsson, Graphitic carbon nitride materials: variation of structure and morphology and their use as metal-free catalysts, Journal of Materials Chemistry 18 (41) (2008) 4893-4908.

[17] J. de Sousa, T. Botari, E. Perim, R. Bizao, D. S. Galvao, Mechanical and structural properties of graphene-like carbon nitride sheets, RSC Advances6 (80) (2016) 76915-76921.

[18] Q. H. Wang, K. Kalantar-Zadeh, A. Kis, J. N. Coleman, M. S. Strano, Elec- tronics and optoelectronics of two-dimensional transition metal dichalco- genides, Nature nanotechnology 7 (11) (2012) 699-712.

[19] M. Chhowalla, H. S. Shin, G. Eda, L.-J. Li, K. P. Loh, H. Zhang, The chemistry of two-dimensional layered transition metal dichalcogenide nanosheets, Nature chemistry 5 (4) (2013) 263-275.

[20] K. Takeda, K. Shiraishi, Theoretical possibility of stage corrugation in si and ge analogs of graphite, Physical Review B 50 (20) (1994) 14916.

[21] B. Aufray, A. Kara, S. Vizzini, H. Oughaddou, C. Léandri, B. Ealet, G. Le Lay, Graphene-like silicon nanoribbons on ag (110): A possible for- mation of silicene, Applied Physics Letters 96 (18) (2010) 183102.

[22] P. Vogt, P. De Padova, C. Quaresima, J. Avila, E. Frantzeskakis, M. C. Asensio, A. Resta, B. Ealet, G. Le Lay, Silicene: compelling experimental evidence for graphenelike two-dimensional silicon, Physical review letters 108 (15) (2012) 155501.

[23] R. Baughman, H. Eckhardt, M. Kertesz, Structure-property predictions for new planar forms of carbon: Layered phases containing sp 2 and sp atoms, The Journal of chemical physics 87 (11) (1987) 6687-6699.

[24] V. Coluci, S. Braga, S. Legoas, D. Galvao, R. Baughman, Families of carbon nanotubes: Graphyne-based nanotubes, Physical Review B 68 (3) (2003) 035430.

[25] V. Coluci, S. Braga, S. Legoas, D. Galvao, R. Baughman, New families of carbon nanotubes based on graphyne motifs, Nanotechnology 15 (4) (2004) S142.

[26] A. Ivanovskii, Graphynes and graphdyines, Progress in Solid State Chem- istry 41 (1) (2013) 1-19.

[27] Y. Li, L. Xu, H. Liu, Y. Li, Graphdiyne and graphyne: from theoreti- cal predictions to practical construction, Chemical Society Reviews 43 (8) (2014) 2572-2586.

[28] F. I. L. Passos, J. G. da Silva Filho, A. Saraiva-Souza, A. G. Souza Filho, V. Meunier, E. C. Girão, One- and two-dimensional carbon nanostructures based on unfolded buckyballs: An ab initio investigation of their electronic properties, Physical Review B 95 (2017) 195124.

[29] H. Terrones, M. Terrones, E. Hernández, N. Grobert, J. Charlier, P. Ajayan, New metallic allotropes of planar and tubular carbon, Physical Review Letters 84 (8) (2000) 1716.

[30] S. Zhang, J. Zhou, Q. Wang, X. Chen, Y. Kawazoe, P. Jena, Penta-graphene: A new carbon allotrope, Proceedings of the National Academy of Sciences 112 (8) (2015) 2372-2377.

[31] X. Shao, X. Liu, X. Zhao, J. Wang, X. Zhang, M. Zhao, Electronic properties of a $\pi$-conjugated cairo pentagonal lattice: Direct band gap, ultrahigh carrier mobility, and slanted dirac cones, Physical Review B 98 (8) (2018) 085437.

[32] R. H. Baughman, D. S. Galvão, Crystalline networks with unusual pre- dicted mechanical and thermal properties, Nature 365 (6448) (1993) 735.

[33] C. P. Ewels, X. Rocquefelte, H. W. Kroto, M. J. Rayson, P. R. Briddon, M. I. Heggie, Predicting experimentally stable allotropes: Instability of penta-graphene, Proceedings of the National Academy of Sciences 112 (51) (2015) 15609-15612.

[34] P. Avramov, V. Demin, M. Luo, C. H. Choi, P. B. Sorokin, B. Yakobson, L. Chernozatonskii, Translation symmetry breakdown in low-dimensional lattices of pentagonal rings, The journal of physical chemistry letters 6 (22) (2015) 4525-4531.

[35] F. Q. Wang, J. Yu, Q. Wang, Y. Kawazoe, P. Jena, Lattice thermal con- ductivity of penta-graphene, Carbon 105 (2016) 424-429.

[36] P. Yuan, Z. Zhang, Z. Fan, M. Qiu, Electronic structure and magnetic properties of penta-graphene nanoribbons, Physical Chemistry Chemical Physics 19 (14) (2017) 9528-9536.

[37] M. Yagmurcukardes, H. Sahin, J. Kang, E. Torun, F. Peeters, R. Senger, Pentagonal monolayer crystals of carbon, boron nitride, and silver azide, Journal of Applied Physics 118 (10) (2015) 104303.

[38] T. Stauber, J. Beltrán, J. Schliemann, Tight-binding approach to penta- graphene, Scientific reports 6 (2016).

[39] H. Sun, S. Mukherjee, C. V. Singh, Mechanical properties of monolayer penta-graphene and phagraphene: a first-principles study, Physical Chem- istry Chemical Physics 18 (38) (2016) 26736-26742.

[40] L. Hu, D. Maroudas, Thermal transport properties of graphene nanomeshes, Journal of Applied Physics 116 (18) (2014) 184304.

[41] W. Xu, G. Zhang, B. Li, Thermal conductivity of penta-graphene from molecular dynamics study, The Journal of chemical physics 143 (15) (2015) 154703.

[42] G. R. Berdiyorov, M. E.-A. Madjet, First-principles study of electronic transport and optical properties of penta-graphene, penta-sic 2 and penta- cn 2, Rsc Advances 6 (56) (2016) 50867-50873.

[43] X.-L. Pan, Y.-Q. Zhao, Z.-Y. Zeng, X.-R. Chen, Q.-F. Chen, Electronic, elastic, optical and thermal transport properties of penta-pdas2 monolayer: First-principles study, Solid State Communications 307 (2020) 113802.

[44] X. Li, S. Zhang, F. Q. Wang, Y. Guo, J. Liu, Q. Wang, Tuning the elec- tronic and mechanical properties of penta-graphene via hydrogenation and fluorination, Physical Chemistry Chemical Physics 18 (21) (2016) 14191-14197.

[45] M.-Q. Le, Mechanical properties of penta-graphene, hydrogenated penta-graphene, and penta-cn2 sheets, Computational Materials Science 136 (2017) 181-190.

[46] W. Tu, K. Wang, L. Qin, Z. Sun, J. Chen, Intrinsic mechanical proper- ties and fracture mechanism of monolayer penta-graphene investigated by nanoindentation: A molecular dynamics study, Computational Materials Science 169 (2019) 109145.

[47] W. Xu, G. Zhang, B. Li, Thermal conductivity of penta-graphene from molecular dynamics study, The Journal of chemical physics 143 (15) (2015) 154703.

[48] F. Q. Wang, J. Yu, Q. Wang, Y. Kawazoe, P. Jena, Lattice thermal con- ductivity of penta-graphene, Carbon 105 (2016) 424-429.

[49] B. Xiao, Y.-c. Li, X.-f. Yu, J.-b. Cheng, Penta-graphene: A promising an- ode material as the li/na-ion battery with both extremely high theoretical capacity and fast charge/discharge rate, ACS Applied Materials & Inter- faces (2016).

[50] R. Krishnan, W.-S. Su, H.-T. Chen, A new carbon allotrope: penta- graphene as a metal-free catalyst for co oxidation, Carbon 114 (2017) 465-472.

[51] H. Qin, C. Feng, X. Luan, D. Yang, First-principles investigation of adsorp- tion behaviors of small molecules on penta-graphene, Nanoscale research letters 13 (1) (2018) 1-7.

[52] Z. Sun, K. Yuan, X. Zhang, G. Qin, X. Gong, D. Tang, Disparate strain response of the thermal transport properties of bilayer penta-graphene as compared to that of monolayer penta-graphene, Physical Chemistry Chem- ical Physics 21 (28) (2019) 15647-15655.

[53] R. M. d. Santos, L. E. de Sousa, D. S. Galvão, L. A. R. Junior, Tuning penta-graphene electronic properties through engineered line defects, arXiv preprint arXiv:2001.06062 (2020).

[54] B. Li, Z.-G. Shao, Adsorption of dna/rna nucleobases and base pairs on penta-graphene from first principles, Applied Surface Science 512 (2020) 145635.

[55] M. Wang, Z. Zhang, Y. Gong, S. Zhou, J. Wang, Z. Wang, S. Wei, W. Guo, X. Lu, Penta-graphene as a promising controllable co2 capture and separa- tion material in an electric field, Applied Surface Science 502 (2020) 144067.

[56] T. Wu, M. Yao, J. Li, M. Li, M. Long, First-principles prediction of the electronic property, carrier mobility and optical absorption in edge-modified pristine sawtooth penta-graphene nanoribbons (sspgnrs), Results in Physics (2020) 103103.

[57] J. Correa, M. Pacheco, S. Bravo, L. Chico, Electronic and magnetic prop- erties of pentagonal nanoribbons, Carbon 162 (2020) 209–219.

[58] B. Rajbanshi, S. Sarkar, B. Mandal, P. Sarkar, Energetic and electronic structure of penta-graphene nanoribbons, Carbon 100 (2016) 118–125.

[59] X. Wu, V. Varshney, J. Lee, T. Zhang, J. L. Wohlwend, A. K. Roy, T. Luo, Hydrogenation of penta-graphene leads to unexpected large improvement in thermal conductivity, Nano letters 16 (6) (2016) 3925–3935.

[60] S. W. Cranford, When is 6 less than 5? penta-to hexa-graphene transition, Carbon 96 (2016) 421–428.

[61] O. Rahaman, B. Mortazavi, A. Dianat, G. Cuniberti, T. Rabczuk, Meta- morphosis in carbon network: From penta-graphene to biphenylene under uniaxial tension, FlatChem 1 (2017) 65 – 73.

[62] A. C. Van Duin, S. Dasgupta, F. Lorant, W. A. Goddard, Reaxff: a reactive force field for hydrocarbons, The Journal of Physical Chemistry A 105 (41) (2001) 9396–9409.


[63] J. E. Mueller, A. C. van Duin, W. A. Goddard III, Development and vali- dation of reaxff reactive force field for hydrocarbon chemistry catalyzed by nickel, The Journal of Physical Chemistry C 114 (11) (2010) 4939-4949.

[64] S. Plimpton, Fast parallel algorithms for short-range molecular dynamics, Journal of computational physics 117 (1) (1995) 1-19.

[65] S. W. Cranford, M. J. Buehler, Mechanical properties of graphyne, Carbon49 (13)(2011) 4111-4121.

[66] J. M. de Sousa, G. Brunetto, V. R. Coluci, D. S. Galvao, Torsional "super- plasticity" of graphyne nanotubes, Carbon 96 (2016) 14-19.

[67] J. De Sousa, R. Bizao, V. Sousa Filho, A. Aguiar, V. Coluci, N. Pugno, E. Girao, A. Souza Filho, D. Galvao, Elastic properties of graphyne-based nanotubes, Computational Materials Science 170 (2019) 109153.

[68] J. De Sousa, T. Botari, E. Perim, R. Bizao, D. S. Galvao, Mechanical and structural properties of graphene-like carbon nitride sheets, RSC advances6 (80) (2016) 76915-76921.

[69] J. De Sousa, P. Autreto, D. Galvao, Hydrogenation dynamics process of single-wall carbon nanotube twisted, Chemical Physics Letters 739 (2020)136960.

[70] R. A. Bizao, L. D. Machado, J. M. de Sousa, N. M. Pugno, D. S. Gal- vao, Scale effects on the ballistic penetration of graphene sheets, Scientific reports 8 (1) (2018) 1-8.

[71] C. F. Woellner, L. D. Machado, P. A. Autreto, J. M. de Sousa, D. S. Galvao, Structural transformations of carbon and boron nitride nanoscrolls at high impact collisions, Physical Chemistry Chemical Physics 20 (7) (2018) 4911-4916.

[72] N. Chen, M. T. Lusk, A. C. van Duin, W. A. Goddard III, Mechanical prop- erties of connected carbon nanorings via molecular dynamics simulation, Physical Review B 72 (8) (2005) 085416.

[73] R. Mirzaeifar, Z. Qin, M. J. Buehler, Tensile strength of carbyne chains in varied chemical environments and structural lengths, Nanotechnology25 (37) (2014) 371001.

[74] A. Nair, S. Cranford, M. Buehler, The minimal nanowire: Mechanical prop-erties of carbyne, EPL (Europhysics Letters) 95 (1) (2011) 16002.

[75] M. Z. Flores, P. A. Autreto, S. B. Legoas, D. S. Galvao, Graphene to graphane: a theoretical study, Nanotechnology 20 (46) (2009) 465704.

[76] P. Autreto, J. De Sousa, D. Galvao, Site-dependent hydrogenation on graphdiyne, Carbon 77 (2014) 829-834.

[77] D. J. Evans, B. L. Holian, The nose-hoover thermostat, The Journal of chemical physics 83 (8) (1985) 4069-4074.

[78] A. P. Garcia, M. J. Buehler, Bioinspired nanoporous silicon provides greattoughness at great deformability, Computational Materials Science 48 (2)(2010) 303-309.

[79] M. Wang, X. Qiu, X. Zhang, Mechanical properties of super honeycombstructures based on carbon nanotubes, Nanotechnology 18 (7) (2007)075711.

[80] R. Dos Santos, E. Perim, P. Autreto, G. Brunetto, D. Galvao, On theunzipping of multiwalled carbon nanotubes, Nanotechnology 23 (46) (2012)465702.

[81] V. R. Coluci, N. M. Pugno, S. O. Dantas, D. S. Galvao, A. Jorio, Atom-istic simulations of the mechanical properties of 'super'carbon nanotubes,Nanotechnology 18 (33) (2007) 335702.

[82] R. A. Bizao, T. Botari, E. Perim, N. M. Pugno, D. S. Galvao, Mechani-cal properties and fracture patterns of graphene (graphitic) nanowiggles,Carbon 119 (2017) 431-437.

[83] T. Botari, E. Perim, P. Autreto, A. Van Duin, R. Paupitz, D. Galvao, Mechanical properties and fracture dynamics of silicene membranes, Physical Chemistry Chemical Physics 16 (36) (2014) 19417-19423.

[84] P. Hohenberg, W. Kohn, Inhomogeneous electron gas, Physical review 136 (3B) (1964) B864.

[85] W. Kohn, L. J. Sham, Self-consistent equations including exchange and correlation effects, Physical review 140 (4A) (1965) A1133.

[86] P. Ordejón, E. Artacho, J. M. Soler, Self-consistent order-n density-functional calculations for very large systems, Physical Review B 53 (16) (1996) R10441.

[87] D. Sánchez-Portal, P. Ordejon, E. Artacho, J. M. Soler, Density-functional method for very large systems with lcao basis sets, International Journal of Quantum Chemistry 65 (5) (1997) 453-461.

[88] E. Anglada, J. M. Soler, J. Junquera, E. Artacho, Systematic generation of finite-range atomic basis sets for linear-scaling calculations, Physical Review B 66 (20) (2002) 205101.

[89] J. P. Perdew, K. Burke, M. Ernzerhof, Generalized gradient approximation made simple, Physical review letters 77 (18) (1996) 3865.

[90] N. Troullier, J. L. Martins, Efficient pseudopotentials for plane-wave calculations, Physical review B 43 (3) (1991) 1993.

[91] L. Kleinman, D. Bylander, Efficacious form for model pseudopotentials, Physical Review Letters 48 (20) (1982) 1425.

[92] H. J. Monkhorst, J. D. Pack, Special points for brillouin-zone integrations, Physical review B 13 (12) (1976) 5188.

[93] T. R. Mattsson, J. M. D. Lane, K. R. Cochrane, M. P. Desjarlais, A. P. Thompson, F. Pierce, G. S. Grest, First-principles and classical molecular

dynamics simulation of shocked polymers, Physical Review B 81 (5) (2010) 054103.

[94] K. Chenoweth, A. C. Van Duin, W. A. Goddard, Reaxff reactive force field for molecular dynamics simulations of hydrocarbon oxidation, The Journal of Physical Chemistry A 112 (5) (2008) 1040-1053.

[95] S. G. Srinivasan, A. C. Van Duin, P. Ganesh, Development of a reaxff potential for carbon condensed phases and its application to the thermal fragmentation of a large fullerene, The Journal of Physical Chemistry A 119 (4) (2015) 571-580.

[96] S. A. Hernandez, A. F. Fonseca, Anisotropic elastic modulus, high pois- son's ratio and negative thermal expansion of graphynes and graphdiynes, Diamond and Related Materials 77 (2017) 57-64. doi:https://doi.org/ 10.1016/j.diamond.2017.06.002.

[97] Y. I. Jhon, S.-E. Zhu, J.-H. Ahn, M. S. Jhon, The mechanical responses of tilted and non-tilted grain boundaries in graphene, Carbon 50 (10) (2012) 3708-3716.
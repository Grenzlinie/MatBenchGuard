# COMPUTER STUDY OF THE ATOMIC MECHANISM OF DEFORMATION AND FAILURE OF CHROMIUM – NIOBIUM BICRYSTALS

V. V. Ogorodnikov and K. V. Malishevskii

UDC 539.3:669.01:681.142.33

Molecular-dynamic simulation of Cr – Nb bicrystals subjected to stretching is carried out in a paired potential approach. Illustrations are provided for the atomic mechanism of deformation and failure, that depends on orientation of a bicrystal with respect to acting force $\boldsymbol{P}$. In the case of a starting configuration $(100)\perp\boldsymbol{P}$ there is a mechanism of reorientation $(100)\perp\boldsymbol{P} \to (110)\perp\boldsymbol{P}$, at first in niobium and then in chromium. With a starting configuration of $(110)\perp\boldsymbol{P}$ a niobium crystallite is only deformed with elastic deformation; at the same time deformation from the chromium direction is ductile-brittle in nature. With an initial configuration of $(111)\perp\boldsymbol{P}$ purely brittle failure is observed. In all cases fracture passes through the interphase boundary. Reasons for these atomic-structural transformations are explained. The dependence of potential energy, the number of pair interactions, and the work of deformation and stress on the deformation are analyzed.

Keywords: nanocrystal, bicrystal, chromium, niobium, composite properties, computer modelling, interatomic interaction, molecular dynamics, structural transformation, atomic mechanism, deformation, failure, strength.

Layered composites based on chromium, in particular Cr – Nb, are distinguished by high heat resistance and quite high resistance to brittle failure [1]. The aim of the present work is computer modelling of the fragments of layered composites considered as model chromium-niobium bicrystals that are subject during operation to the action of high mechanical loads. The first experience of molecular-dynamic modelling of the deformation and failure of a chromium nanocrystal and Cr – Nb bicrystals in tension along one direction <100> is the work of the authors in [2, 3]. Results of this modelling showed the promise of the procedure developed for studying atomic-structural changes in metals under the action of destructive mechanical stresses, and also the requirement of additional computer experiments with other directions of load application (<110> and <111>).

Interatomic Cr – Cr, Nb – Nb, and Cr – Nb interactions were calculated by molecular-dynamic modelling using a paired potential presented in the form of a universal Rose energy function [4]:

$$U = U_0(1 + a)\exp(-a).$$

Here we have written $a$ as

$$a = b(1 - y) + c(1 - y)^2 + d(1 - y)^3,$$

where $y = r/r_0$; $b$ is Rose parameter; $c$, $d$ are additional parameters required for calculating the Grüneisen coefficient for chromium [5]. Parameter $b$ is determined by a combination of properties: volumetric elasticity modulus, atomization (sublimation) energy, and lattice spacing [4, 5]. Action of the potential is limited by the cut-off radius $r_\text{k}$ including within the sphere of action two coordination spheres in an equilibrium state. Parameters of the potentials used are calculated from empirical data and presented in Table 1. The procedure for finding potential parameters on the example

Institute for Problems of Materials Science, National Academy of Sciences of Ukraine, Kiev. Translated from Poroshkovaya Metallurgiya, Nos. 1-2(429), pp. 82-91, January-February, 2003. Original article submitted October 1, 2001.

1068-1302/03/0102-0073$25.00 ©2003 Plenum Publishing Corporation

of chromium is given in [7]. For a ${\rm Cr}-{\rm Nb}$ pair average values of $b$, $c$, $d$, $r_0$, and $U_0$ for chromium and niobium were used that taking account of the Rose energy function made it possible to construct a self-congruent paired potential (Fig. 1).

The model for ${\rm Cr}-{\rm Nb}$ bicrystals is a cylinder 4-5 nm long and 2.0-2.5 nm in diameter with a number of atoms of ~1200. The cylindrical surface was prescribed with an accuracy to the crystallographic facet. Depending on bicrystal development the longitudinal axis of the cylinder coincided with one of the directions (<100>, <110>, or <111>) that were also tensile directions. In contrast to crystals with one sort of atoms no special boundary was determined for the ${\rm Cr}-{\rm Nb}$ interphase boundary. A unique condition of initial orientation was to obtain a single chain of atoms through the centre of the crystal passing through both grains and coinciding with a chosen crystallographic orientation in both grains. The version of orientation determined the overall number of atoms in a bicrystal, its length and diameter, and also its parameters for each of the crystallites (Cr, Nb) (Table 2). The specific surface energy, including the external surface energy and that for the interphase boundary, was about the same value (~47 nJ/m²) for the three versions of orientation presented.

Tension was accomplished by moving apart atoms of the end surfaces (two atoms each from each direction). The rest of the atoms were involved in tension as result of their interaction with the end atoms and with each other. For each iteration the crystal was lengthened by 0.0001 nm. The physical time for crystal life, corresponding to one iteration, was 5 fsec. Correspondingly the absolute tensile rate was constant and was $2{\cdot}10^{-5}$ nm/fsec (20 m/sec), where the relative rate was different due to the nonuniform specimen length in the original state (Table 2). As previous experiments have shown, this rate is much less than the rate of relaxation processes in the lattice providing coherence of atomic displacements. We note that the rate of elastic wave propagation in a solid is 2-6 km/sec. A bicrystal was heated to 300 K with a thermalization interval (maintenance of a prescribed temperature) of 50 iterations.

Structural rebuilding in bicrystals for the three cases of tension (along directions <100>, <110>, and <111>) is presented in Figs. 2-4 (on the left are shown longitudinal sections of a cylinder, and on the right there are transverse sections). The structure in sections (both longitudinal and transverse) was scanned to a depth of 0.5 nm, and therefore within a section there are atoms that are at a different depth. Structural changes in a crystal were recorded for each iteration, but only the change through each 100 iterations was accounted. The overall number of iterations up to failure reached 20000-30000.

<table>
<caption>TABLE 1. Parameters of ${\rm Cr}-{\rm Cr}$, ${\rm Nb}-{\rm Nb}$, and ${\rm Cr}-{\rm Nb}$ Paired Potentials</caption>
<thead>
<tr>
<th>Potential</th>
<th>$b$</th>
<th>$c$</th>
<th>$d$</th>
<th>$U_0$, eV</th>
<th>$r_0$, nm</th>
<th>$r_{\rm k}$, nm</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cr – Cr</td>
<td>5.58</td>
<td>2.79</td>
<td>5.58</td>
<td>–0.6345</td>
<td>0.262</td>
<td>0.350</td>
</tr>
<tr>
<td>Nb – Nb</td>
<td>5.19</td>
<td>0.64</td>
<td>3.11</td>
<td>–1.1274</td>
<td>0.297</td>
<td>0.400</td>
</tr>
<tr>
<td>Cr – Nb</td>
<td>4.80</td>
<td>–1.51</td>
<td>0.63</td>
<td>–0.8810</td>
<td>0.280</td>
<td>0.375</td>
</tr>
</tbody>
</table>

<table>
<caption>TABLE 2. Geometric Parameters of Nanocrystals</caption>
<thead>
<tr>
<th>Bicrystal
orientation</th>
<th>Tensile
direction</th>
<th>Number of atoms,
overall (Cr + Nb)</th>
<th>Length, nm,
overall (Cr + Nb)</th>
<th>Diameter, nm,
Cr; Nb</th>
<th>$S_{\rm sp}$, nm $^{-1}$</th>
<th>$\varepsilon_1$, %</th>
</tr>
</thead>
<tbody>
<tr>
<td>(100)$\perp$P</td>
<td>&lt;100&gt;</td>
<td>1168 (712 + 456)</td>
<td>4.63 (2.24 + 2.39)</td>
<td>2.080; 1.980</td>
<td>2.40</td>
<td>0.0022</td>
</tr>
<tr>
<td>(110)$\perp$P</td>
<td>&lt;110&gt;</td>
<td>1190 (702 + 488)</td>
<td>4.81 (2.36 + 2.45)</td>
<td>2.060; 2.034</td>
<td>2.37</td>
<td>0.0021</td>
</tr>
<tr>
<td>(111)$\perp$P</td>
<td>&lt;111&gt;</td>
<td>1221 (637 + 584)</td>
<td>3.93 (1.70 + 2.23)</td>
<td>2.355; 2.349</td>
<td>2.21</td>
<td>0.0025</td>
</tr>
</tbody>
</table>

**Note.** $\mathbf{P}$ is tensile force, $S_{\rm sp}$ is specific surface, $\varepsilon_1$ is relative deformation for one iteration.

![](./images/812399198279303168_1.jpg)

Fig. 1. Paired interaction potentials.

![](./images/812399198279303168_2.jpg)

Fig. 2. Structural changes in a Cr – Nb bicrystal with tension along the direction <100>. Tension 0 (a); 0.2 (b); 9.3 (c); 21.3 (d); 47.4 (e); 48% (f).

![](./images/812399198279303168_3.jpg)

Fig. 3. Structural changes in a Cr – Nb bicrystal with tension along the direction <110>. Tension 0 (a); 0.2 (b); 9.1 (c); 9.5 (d); 14.6 (e); 34.5% (f).

![](./images/812399198279303168_4.jpg)

Fig. 4. Structural changes in a Cr - Nb bicrystal with tension along the direction <111>. Tension 0 (a); 0.25 (b); 9.2 (c); 9.4 (d); 14.5% (e).

The initial orientation for tension of a bicrystal along <100> is presented in Fig. 2a. The transverse section to the right gives an idea about the level of the approach towards a cylindrical surface from chromium side (Fig. 2a), and in Fig. 2b to the right from the niobium side. Characteristic stages of tension are given in Fig. 2b-f. Tension up to 0.2% (Fig. 2b) leads to a corresponding increase in interatomic distance in the <100> direction and adjustment of atom lattices at the boundary. Then at the centre of the longitudinal section a small (9.3%) deformation neck forms (Fig. 2c) advancing in the direction of the niobium grain (Fig. 2d). Thus, in the first stage of tension almost all deformation occurs for niobium as the more ductile material. Simultaneously there is atomic-structural rebuilding in niobium: reorientation of planes with respect to the operating forces $(100)\perp\mathbf{P}\to(110)\perp\mathbf{P}$ and fragmentation of the niobium crystal, i.e. twinning. Twin boundaries are mobile: two boundaries (Fig. 2d) combined into one (Fig. 2e). Rebuilding in chromium (second stage of deformation) commences with about 22% deformation at that instant when in the niobium it has embraced all of the crystallite and deformation by this mechanism becomes impossible within it.

Deformation is transmitted rapidly from niobium to chromium, and in chromium it proceeds more simply: without twinning and fragmentation by uniform reorientation $(100)\perp\mathbf{P}\to(110)\perp\mathbf{P}$ (Fig. 2f, to the right). The transverse section decreases and acquires a somewhat distorted oval shape. The crystal lengthens as a result of extension of atoms in the horizontal direction, and spaces that form are filled with atoms approaching in the vertical direction. The reserves of this deformation mechanism are exhausted when the rebuilding wave in chromium reaches the left-hand boundary of the specimen (Fig. 2f) where the orientation $(100)\perp\mathbf{P}$ is fixed. From this instant the bicrystal is not in a state to resist the breaking force. The third and final stage of deformation is generation and development of a failure crack. It is generated at the interphase boundary and develops in a brittle fashion at a very high rate (deformation section 47.5-48%).

![](./images/812399198279303168_5.jpg)

Fig. 5. Dependence of values of potential energy for a whole crystal (a), a chromium grain (b), a niobium grain (c), number of interactions (d), work of deformation (e) and stress (f) on the amount of Cr – Nb bicrystal deformation along the directions <100>, <110>, and <111>.

Tension of a bicrystal with the initial configuration (110)⊥P is presented in Fig. 3. Deformation of 0.2% leads to atomic relaxation at the interphase surface (Fig. 3b). The boundary plane of niobium is compressed, but for chromium it stretches slightly and bends as a result of which step forms. With further deformation (9.1%) the step even out (Fig. 3c) and distance between planes at the center of the longitudinal section increases markedly reaching a critical value

(9.5%) after which there is breaking (Fig. 3d). By moving away atoms of chromium and niobium at the surface lose a bond. At the same time in the central part a bridge of chromium atoms forms to which not only boundary atoms are attracted, but also deep-seated atoms that move along <111> slip planes to the surface. Then the bridge thins (Fig. 3e) and with deformation of 34.5% there is breaking along the interphase surface (Fig. 3f), and some of the atoms are captured by the niobium grain. Over the whole time of tension the niobium crystallite experiences only elastic tension of 7.5% with overall deformation of 9.1% which is removed after subsequent relaxation. The structure for the transverse section of the interphase boundary with different degrees of deformation is shown to the right in Fig. 3c-f.

For the initial configuration (111)⊥P there is typically imperfections at the junction of chromium and niobium grains due to the different atom diameters and lattice spacing (Fig. 4a). Therefore in the initial stage of deformation there is structural rebuilding, i.e. conjugation of planes over both sides of the interphase boundary (Fig. 4b). However, further tension introduces distortions afresh into the structure of the boundary (Fig. 4c), that serve as an area of stress concentration. The level of damage increases rapidly (Fig. 4d) and leads to brittle failure by separation of the chromium and niobium planes (Fig. 4e). The fracture has a stepped structure taking on a regular crystallographic facet. The internal structure of both crystallites does not change during the whole process.

Thus, the configuration (111)⊥P appears to be the least durable (14.5% elongation). More lasting were the configurations (110)⊥P and (100)⊥P (34.5 and 48%, respectively). The high endurance of the orientation (100)⊥P is due to the atomic-structural rebuilding within the body of the chromium and niobium grains giving to deformation of a viscoplastic nature. Nonetheless, the final stage of deformation for this orientation occurs in a brittle fashion. Failure of a bicrystal with a (111)⊥P configuration is ductile-brittle in nature; some proportion of toughness is due to formation of a bridge of chromium atoms. For the (111)⊥P configuration pure brittle failure is typical, i.e. fracture. In all cases failure occurred over the interphase boundary. This conclusion agrees with data for the low strength of an interphase boundary in layered Cr – Nb composites [1].

We have studied the change in potential energy of a bicrystal $E$ as the overall energy $U_{ij}$ for all paired interactions calculated for one atom during tension: $E=(1/2\Sigma U_{ij})/N_{\text{a}}$, $N_{\text{a}}$ is the total number of atoms in a bicrystal (Fig. 5a). Similar dependences have been plotted separately for chromium (Fig. 5b) and niobium (Fig. 5c) grains. The total number of interactions in a bicrystal $N$, summed for all atoms taking account of the operating radius for the potential, has been determined (Fig. 5d). A study was made of the change in the work of deformation in proportion to specimen tension $A = \{N_{\text{a}}\Delta l/(V_{0}L_{0})\}\Sigma\Delta E_{m}$, where $\Delta l = \text{const}$ is specimen elongation for one iteration, $m$ is a summation index for the number of iterations (Fig. 5e); the change in stress $\sigma=\Delta EN_{\text{a}}K/V_{0}$ due to the amount of deformation ($\Delta E = E - E_{\text{min}}$, $E_{\text{min}}$ is minimum energy reached after the initial relaxation, $V_{0}$ is specimen volume, $K=(L_{0}+R_{0})/R_{0}$ is a coefficient taking account of the ratio of load application area to the area of the whole surface, $L_{0}$ and $R_{0}$ are cylinder original length and radius) (Fig. 5f). Stress $\sigma$ characterizes material resistance to the active tensile force $P=\sigma S_{0}$ ($S_{0}$ is the initial specimen cross sectional area).

In the initial stage of tension (up to 0.5%) there is a tendency towards a small reduction in $E$ for a bicrystal and individual crystallites independent of orientation (Fig. 5a-c). This is connected with relaxation, i.e. atomic rebuilding, at the specimen side surface and interphase boundary. A slight increase in the number of bonds $N$ (Fig. 5d) and the more marked release of stresses (Fig. 5f) are also noted.

In the deformation range 0.5-8% there is a sharp increase in energy $E$ and stress $\sigma$, which is due to an increase in interatomic distances and atomic collisions that are caused by structural rebuilding (evidence of this is the increase in the number of bonds $N$ in the preceding stage). In the case of <100> a contribution to the change in $E$ is also from breaking of some portion of interatomic bonds, whereas in the case of <110> and <111> the number of bonds is almost unchanged (Fig. 5d). It should be noted that use of a paired potential with another (large) bounding radius $r_{\text{k}}$ could affect the number of peaks causing smoothing and possibly the form of the potential energy curves in certain cases could become similar to curves for Nb with the direction <100> (Fig. 5c).

This process for a bicrystal with a tensile direction <100> ceases with emergence of $E$ into a flat area with deformation of 8-9% (Fig 5a), and for a bicrystal and individual grains with directions <110> and <111> energy $E$ emerges into a sharp peak (Fig. 5b-c). There is also intense breaking of bonds, that in the case of <110> and <111> is

<table><thead><tr><td>Tensile direction</td><td>ε, %</td><td>Y, GPa</td><td>$σ_{y}$, GPa</td><td>$ε_{t},\% $</td><td>$A_{t},GJ/m^{3}$</td><td>$σ_{t}$, GPa</td></tr></thead><tbody><tr><td><100></td><td>8.4</td><td>78</td><td>5.2</td><td>48</td><td>0.95</td><td>22.2</td></tr><tr><td><110></td><td>9.5</td><td>123</td><td>9.0</td><td>32</td><td>0.39</td><td>9.6</td></tr><tr><td><111></td><td>9.6</td><td>83</td><td>(5.7)</td><td>17</td><td>0.17</td><td>7.9</td></tr></tbody></table>

TABLE 3. Elastic and Strength Characteristics of Model Cr – Nb Bicrystals

avalanche in nature (Fig. 5d). In turn breaking of bonds promotes rapid liberation of elastic energy and the formation of new bonds as a result of atomic rebuilding in other areas, which leads to a partial restoring in the values of $N$, $E$, and $\varepsilon$ (deformation of 9-10%). Features of the change in parameters in the case of <100> are connected with the start of marked atomic-structural rebuilding $(100)\perp \mathbf{P}\to(110)\perp \mathbf{P}$ noted above.

Further tension along <110> (above 10%) is accompanied by a prolonged and significant change in the $E$ up to failure deformation of 48%, and in the niobium grain a dip in $E$ is observed in the section 21-36% (Fig. 5c). We note that in this period occurs transfer of deformation from the niobium grain to the chromium grain (Fig. 2d, e) leading to stress relaxation and a reduction in energy in the niobium grain (Fig. 5c) and an opposite change in the chromium grain (Fig. 5b). In the final deformation stage (45-48%) a new peak for energy and stress arises with a simultaneous avalanche reduction in the number of bonds. After failure there is intense atomic-structural relaxation in the fragments formed with formation of new bonds and removal of stresses ceasing towards 50% extension.

Deformation above 10% for <110> is characterized by a gradual increase in $E$ with a simultaneous reduction $N$ and $\sigma$ up to the instant of failure (34.5%). Then there is a weak tendency towards a reduction $E$ connected with stress relaxation in the chromium fragment that undergoes the greatest structural changes (Fig. 3).

An increase in $E$ in the case of <111> ceases with 13.5% of deformation, i.e. the instant of new avalanche breaking of bonds and the formation of a main crack leading to rapid purely brittle failure (with 14.5% deformation). Then the energy of fragments is unchanged since they have a regular crystallographic structure (Fig. 4e).

We have determined the elastic and strength properties for model Cr – Nb bicrystals from computer study data (Table 3). We note that the results of computer tests for breaking of nanocrystalline specimens carried out with a constant rate of tension could have a number of differences from the results of actual tests of large specimens with a constant loading rate. Since the initial stage of tension in these studies includes the stage of atomic rebuilding of the structure and corresponding stress relaxation, the elastic deformation section moves in the direction of higher values. Emergence into a rectilinear dependence occurs gradually. In the case of large specimens the Young’s modulus is 280 GPa for chromium and 106-157 GPa for niobium [6], so that $Y$ for the combined nanocrystals appears to be close to the value of $Y$ for niobium (Table 3).

For a large chromium specimen there is no yielding, but for niobium $\sigma_{y}=0.27$ GPa [6]. In a bicrystalline nanospecimen both chromium and niobium reveal significant ductility in the <100> direction connected with reorientation of planes, twinning, fragmentation, and boundary movement. Here the yield point, developing first from the niobium direction in this nanospecimen, appeared to be twenty times higher than for a niobium macrospecimen. An even higher value of $\sigma_{y}$ appeared for specimen subjected to tension along <110> (Table 3). These high values of $\sigma_{y}$ are natural for undislocated specimens. The value of $\sigma_{y}=5.7$ GPA for <111>, included in brackets (Table 3), is not the yield point, but it only signifies the first stage of brittle crack failure development “delayed” (temporarily) ahead of a barrier.

The overall work of deformation $A_{t}$ and ultimate strength $\sigma_{t}$ decrease in the series $(100)\perp \mathbf{P}-(110)\perp \mathbf{P}-(111)\perp \mathbf{P}$ (Table 3). An inverse dependence is observed for total elongation $\varepsilon_{t}$. This is explained by the effect of the atomic-structural rebuilding noted before that provides plastic flow and material strengthening with tension in the directions <100> and <110>. The ultimate strength of large polycrystalline specimens is 0.084 GPa for chromium and 0.35 GPa for niobium [6], which is two to three orders of magnitude lower than the strength of the tested nanospecimens (Table 3). As might be expected the latter corresponds to the strength of filamentary crystals, i.e. whiskers [6].

Thus, the regularities obtained in both atomic-structural rebuilding and the change of integral parameters are well described in the existing ideas about possible deformation mechanisms for metals under load and the nature of change in properties. This is valuable for modelling an actual process in a real metallic material on the basis of a paired potential that is to some approximation a solution of the quantum-mechanical equation for an interatomic bond. The results of this work confirm that paired potentials constructed empirically or obtained from special first principle calculations [7] quite adequately describe the most essential energy and mechanical parameters of interatomic interactions in BCC-metals. We have established specific atomic mechanisms for deformation and failure under specific conditions including an idea about the possible processes in nanocrystals and layered composites of the system Cr – Nb. It is possible to use the procedure developed for obtaining interatomic potentials in other metal systems and the subsequent extensive choice of materials and deformation conditions in relation to the stated problem.

The work was carried out within the framework of the INTAS-97-31994 program.

## REFERENCES

1.  A. T. Kolomiets, "Possible creation of ductile heat- and corrosion-resistant materials based on BCC refractory metals," in: *Electron Microscopy and Strength of Metals* [in Russian], Institute for Problems of Materials Science, National Academy of Sciences of Ukraine, Kiev (1997).

2.  V. V. Ogorodnikov and K. V. Malishevskii, "Computer modelling of tension for a chromium nanocrystal," in: *Theory and Modelling of the Electron Structure and Properties of Refractory Compounds, Alloys, and Metals* [in Russian], Institute for Problems of Materials Science, National Academy of Sciences of Ukraine, Kiev (1997).

3.  V. V. Ogorodnikov and K. V. Malishevskii, "Molecular-dynamic modelling of tension for a Cr – Nb bicrystal," *Modelling in Materials Science. Mathematical Models and the Computer Experiment in Materials Science*, Proc. Inst. Materials Science Problems, Ukrainian National Academy of Sciences, Kiev, Series 2, No. 5, 104-112 (2001).

4.  P. Vinet, J. H. Rose, J. Ferrante, and J. R. Smith, "Universal features of the equation of state solids," *J. Phys. Condens. Materials*, **1**, No. 11, 1941-1963 (1989).

5.  V. V. Ogorodnikov, "Analytical derivation of the Rose energy equation," *Fiz. i Tekhn. Vysokikh Davlenii*, **4**, No. 2, 15-21 (1994).

6.  V. G. Bar'yakhtar (ed.), *Solid Physics. Encyclopaedic Dictionary, in 2 vols.* [in Russian], Nauk. Dumka, Kiev (1996).

7.  V. Ogorodnikov, K. Malishevskii, A. Lisenko, and V. Bekenev, "Lattice energy, equation of state, and interatomic potential of chromium," *Phys. Strength Plasticity*, **16**, 323-341 (1996).
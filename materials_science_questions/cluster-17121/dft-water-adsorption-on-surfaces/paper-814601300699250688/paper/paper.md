# Nanoscale Hydrophilicity on Metal Surfaces at Room Temperature: Coupling Lattice Constants and Crystal Faces

Zhen Xu, $^\dagger$ Yi Gao, $^\dagger$ Chunlei Wang, $^{*, \dagger}$ and Haiping Fang $^\dagger$

$^\dagger$Division of Interfacial Water and Key Laboratory of Interfacial Physics and Technology, Shanghai Institute of Applied Physics, Chinese Academy of Sciences, P.O. Box 800-204, Shanghai 201800, China

![](./images/814601300699250688_1.jpg)

**ABSTRACT:** It is generally accepted that the metal−water interface tensions are quite high; thus, the metal surfaces are usually regarded as hydrophilic. Using the molecular dynamics simulations, we have investigated the microscopic wetting behaviors of a series of metal surfaces at room temperature, including Ni, Cu, Pd, Pt, Al, Au, Ag, and Pb with three crystal faces of (100), (110), and (111). We have found that the wetting of the metals is greatly dependent on both the lattice constants and crystal surfaces. Particularly, stable water droplets are found forming on the first ordered water layer, serving as an evidence of room temperature "ordered water monolayer that does not completely wet water" on Pd(100), Pt(100), and Al(100) surfaces, while water films without ordered water monolayer are found on (110) and (111) faces of all metal surfaces and even (100) face of other metal surfaces (Ni, Cu, Au, Ag, and Pb). The formation of water droplets is attributed to the rhombic ordered water layers on the surfaces, reducing the number of hydrogen bond formation between the monolayers and other water molecules atop the water monolayer. These results demonstrate a tight correlation among the lattice constant, the crystal faces, and the surface wetting behaviors. Our findings of the novel wetting behavior may have potential applications in the surface friction reduction at the metal surfaces, design of the anti-ice materials, and the nonfouling materials.

![](./images/814601300699250688_2.jpg)

## 1. INTRODUCTION

The wetting behaviors on materials surfaces, $^{1−9}$ termed hydrophobicity and hydrophilicity, have attracted great attention due to their fundamental role in numerous phenomena, such as the dissolution processes, $^{10,11}$ self-assembly behaviors of amphiphilies, $^{12}$ protein folding, $^{13−15}$ surface frictions, $^{16−18}$ and other issues arising in the fields of physical chemistry $^{19−29}$ and biology. $^{30,31}$ Metals or metal-based nanostructures have been used widely to manufacture sensors, electronic, and biomedical devices. Among these applications, one main concern is the wetting property of the metals or metal nanoparticles $^{22,32−40}$ when water molecules contact with them. For example, the surface wetting property may affect the solubility of metal nanoparticles, which directly affects the catalyst process of generating hydrogen gas from water. $^{41}$ In biomedical fields, the wetting property of metal surfaces affects the biocompatibility of metal particles for drug delivery. $^{42}$ Generally, the surface energies of metal surfaces are quite high; $^{43}$ thus, metal surfaces are regarded as hydrophilic surfaces. $^{44}$ However, several works including experiments and simulations show inconsistency on the wetting properties of metal surfaces. Taking the metals Pt and Pd as an example, the experimental work by Erb$^{33}$ has found that the advancing contact angles were $50^\circ$ on the Pt surface and $74^\circ$ on the Pd surface at room temperature. However, the experiments $^{43}$ by Tyson et al. and the simulations by Heinz et al. $^{35}$ found that the solid/liquid interface tensions on the Pt and Pd surface are rather high, indicating the highly hydrophilicity of the Pt and Pd surfaces at room temperature. Using quantum calculations, Meng et al. $^{45}$ have also presented that Pt(111) is highly hydrophilic based on their proposed criteria. Recently, Limmer et al. $^{40}$ have found that even the same metals with different crystal faces (100) and (111), the wetting behaviors are quite different, where water droplets were found coexisting with the water monolayers. These contradictions may be attributed to that we are still lacking a full understanding of the wetting behavior of the heavy metal surfaces. It has been known that the geometry, the atomic arrangements, and the chemically heterogeneous $^{9,46−49}$ of the solid surface are playing key roles in the surface wetting behaviors. Considering that both the lattice constants and crystal faces of metal surfaces affect the atomic arrangements, the understanding of the role of lattice constants and crystal face in the wetting behavior of the metal surfaces is urgently needed but still unknown.

In this study, using molecular dynamics (MD) simulations, we attempt to explore the effects of lattice constant and crystal surface on the surface wetting properties of eight FCC heavy metals (Ni, Cu, Pd, Pt, Al, Au, Ag, and Pb) at room temperature. It is found that stable water droplets on the first water layer, serving as an evidence of "ordered water monolayer

Received: May 3, 2015
Revised: July 31, 2015

<table>
<caption>Table 1. List of the Lattice Constants and Lennard-Jones (LJ) Parameters of Metals</caption>
<thead>
  <tr>
    <th>metal</th>
    <th>Ni</th>
    <th>Cu</th>
    <th>Pd</th>
    <th>Pt</th>
    <th>Al</th>
    <th>Au</th>
    <th>Ag</th>
    <th>Pb</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>lattice constant (nm)</td>
    <td>0.352</td>
    <td>0.362</td>
    <td>0.389</td>
    <td>0.392</td>
    <td>0.405</td>
    <td>0.408</td>
    <td>0.409</td>
    <td>0.495</td>
  </tr>
  <tr>
    <td>$\sigma$ (nm)</td>
    <td>0.227</td>
    <td>0.233</td>
    <td>0.251</td>
    <td>0.253</td>
    <td>0.261</td>
    <td>0.263</td>
    <td>0.263</td>
    <td>0.318</td>
  </tr>
  <tr>
    <td>$\varepsilon$ (kJ/mol)</td>
    <td>23.612</td>
    <td>19.738</td>
    <td>25.707</td>
    <td>32.606</td>
    <td>16.798</td>
    <td>22.114</td>
    <td>19.064</td>
    <td>12.245</td>
  </tr>
</tbody>
</table>

that does not completely wet water", at room temperature can be found on Pd(100), Pt(100), and Al(100) surfaces, based on the force field developed by Heinz et al.³⁵ The phenomena are attributed to the rhombic ordered structures of first water monolayer induced by the atom arrangements of (100) surface of Pd, Pt, and Al, different from our previous work⁴⁶ with hexagonal hydrogen bond networks of water molecules. The rhombic ordered water structures greatly enhance the number of hydrogen bonds formed inside the first water monolayer and in turn reduce the possibilities of hydrogen bonds formation between the water molecules in this monolayer and other water molecules above. In contrast, no water droplets are found on other metal surfaces (Ni, Cu, Au, Ag, and Pb) with the crystal face (100) or the crystal faces (110) and (111) for eight FCC heavy metals we investigated. Our findings highlight the matching of the water molecules and the surface atomic arrangements, where both lattice constants and the crystal faces are important for the matching between the hydrogen bond network of water molecules and the atomic arrangements. The novel wetting behavior may have potential applications in the electrochemistry, surface friction reduction at the metal surfaces, design of the anti-ice materials, and the antifouling materials.

## 2. SYSTEMS AND METHODS
Here, eight different face-centered cubic (FCC) metals with the lattice constant order of Ni < Cu < Pd < Pt < Al < Au < Ag < Pb were studied. The lattice constants are shown in Table 1. For each metal, three different crystal surfaces (100), (110), and (111) were constructed with a plane in the $x-y$ dimensions (more details of the simulation box sizes could be found in PS 1 of the Supporting Information). In the simulations, the metal atoms were modeled as uncharged Lennard-Jones (LJ) particles, and the parameters of these metals were from the force field developed by Heinz et al.³⁵ (see the detailed parameters in Table 1). This force field had been proven to reproduce the metal-water interfacial energies very well³⁵ and was widely used.⁵⁰⁻⁵³ In the PS4 of Supporting Information, the average adsorption energy per water molecule on (111) surface of some metals and some typical water structure on Cu(110) and Pt(111) surface are compared to the results from experiments and DFT calculations to check the accuracy of the force field. Initially, a water film with thickness of 1.2 nm was placed on different metal surfaces. The simulation time was 8 ns for all the metals, and the last 4 ns data were collected for analysis. The periodic boundary conditions were applied in all directions. MD simulations were performed using a time step of 1.0 fs from Gromacs 4.5.4⁵⁴ in a constant volume and constant temperature (NVT) ensemble. The temperature was maintained at 300 K using the v-rescale method. The LJ interactions were treated with a cutoff distance of 1.0 nm, and the particle mesh Ewald (PME) method⁵⁵ with a real-space cutoff of 1 nm was utilized to treat the long-range electrostatic interactions. The extended simple point charge (SPC/E) model⁵⁶ was utilized for water molecules. Herein, the hydrogen bond was determined using a geometrical criterion, where two water molecules were hydrogen bonded if the O-O distance was less than 0.35 nm and simultaneously the angle H-O···O was less than 30°.

## 3. RESULTS AND DISCUSSION
We first investigate the (100) crystal faces of the metals Ni, Cu, Pd, Pt, Al, Au, Ag, and Pb. Our simulation results show that most of these metal surfaces, including Ni, Cu, Au, Ag, and Pb, are always completely covered by the water molecules. However, to our surprise, water molecules gradually began to assemble and form a clear water droplet after 4 ns in the simulation time on three solid surfaces of Pd, Pt, and Al, as shown in Figures 1a, 1b, and 1d, respectively. At the same time, one can also observe that water monolayer completely covers on the solid metal surfaces outside the water droplets. Thus, this phenomenon serves as a direct evidence of a water droplet coexisting with the water monolayer, similar to the prediction in our previous work,⁴⁶ the experiment phenomena on self-assemble monolayer surface with terminal COOH,⁵⁷ sapphire surface,⁵⁸ and BSA (bovine serum albumin)-Na₂CO₃ membrane,⁵⁹ and simulation phenomena on talc surface,⁶⁰ hydroxylated Al₂O₃, and SiO₂ surfaces.⁶¹ We have plotted the contact angle values of the water droplets as a function of lattice constant in Figure 2. The method for calculating the contact

![](./images/814601300699250688_3.jpg)

Figure 1. Side-view snapshot of a cylindrical water droplet on a water monolayer on (a) Pd(100), (b) Pt(100), and (d) Al(100) surface and the complete covering water film on some typical surfaces, (c) Pd(110), (e) Pd(111), and (f) Ni(100) surfaces.

![](./images/814601300699250688_4.jpg)

Figure 2. Contact angles of water droplets on (100) crystal surfaces with different lattice constants.

angle of water droplet on the water monolayer follows the work by Vanzo et al.,⁶² where a cylindrical water droplet is employed. Clearly, there is a tight dependent relationship between the contact angles of water droplets and the lattice constants of different metal types. As one can observe, the contact angles for the metal Pt, Pd, and Al are 57°, 53°, and 32°, respectively. In addition, there are no obvious changes of the contact angles as time increases after 4 ns, indicating the existence of water droplet is stable. It should be noted that some of the metal surfaces are easily to be oxidized, which may affect the surface constituent and atomic arrangements. This fact may account of the lack of the direct experimental evidence of the room temperature "ordered water monolayer that does not completely wet water" on the mental surfaces. It should be pointed out that the force field we used neglects the effects of the metal's electronic polarization, which may account of the different contact angles between our simulation and work by Limmer et al.⁴⁰ As a comparison, for the (110) and (111) crystal faces, we have found that the contact angles are 0° with only the water films spreading over the surfaces (see Pd(110) of Figure 1c, Pd(111) of Figure 1e, and Ni(100) of Figure 1f as typical examples). The phenomenon of water droplets found on (100) crystal faces of Pd, Pt, and Al while water films on the other surfaces clearly shows that the wetting of metal surfaces is greatly dependent on both the crystal faces and the metal types, i.e., lattice constants.

Our previous works¹⁸,⁴⁶,⁴⁷,⁶³⁻⁶⁵ have shown that the numbers of hydrogen bonds (H bonds) formed between the first water monolayer and water molecules above it are the key in understanding the wetting behavior of water droplet on water monolayer. Here we have also calculated the average number of H bonds formed by a water molecule in the first monolayer with its neighboring water molecules in the same layer (namely, within-monolayer H bonds) as well as the average number of H bonds formed between a water molecule in the first monolayer and the water molecules above this monolayer (namely, monolayer-second-layer H bonds). The thickness of first water layer, which is defined as the distance from the solid surface to the first valley of the water density distribution profile along the z-axis, is shown in PS2 of the Supporting Information. For an easy description, we always use the term monolayer-second-layer H bonds no matter whether there is clear water droplet because the H bonds are always formed between water molecules in monolayer and the water molecules above monolayer. As shown in Figure 3, for (100) crystal surface as lattice constant increases, there is a transition region, where larger within-monolayer H bonds and smaller monolayer-second-layer H bonds can be found for the metal Pd(100), Pt(100), and Al(100). The numbers of within-monolayer H bonds under water droplet for Pd(100), Pt(100), and Al(100) are 3.272, 3.272, and 2.963, respectively. Correspondingly, the numbers of monolayer-second-layer H bonds for Pd(100), Pt(100), and Al(100) are 0.408, 0.413, and 0.549, respectively, smaller than other metals, i.e., 0.645 for Ni(100), 0.623 for Cu(100), 0.564 for Au(100), 0.568 for Ag(100), and 0.703 for Pb(100), respectively. It should be noted that the number of monolayer-second-layer H bonds for Au(100) and Ag(100) is very close to that of Al(100), indicating the three metals locate at a transition region from formation of water droplet to the disappearance of water droplet. The comparison clearly indicates that for the metal Pt(100), Pd(100), and Al(100) surfaces water molecules in the first monolayer prefer to form hydrogen bonds within the monolayer, rather than between water droplet and water monolayer. Since there are no hydrogen bond donors or acceptors on the metal surfaces, each water molecule in first water monolayer outside the water droplet can form 3.680, 3.685, and 3.512 H bonds for Pd(100), Pt(100), and Al(100), which are close to the saturated value 4 that each water can form. Clearly, there is a competition between within-monolayer H bonds and monolayer-second-layer H bonds, which are dependent on the lattice constant. An increase of the former reduces the likelihood of formation of the latter. The fewer number of the monolayer-second-layer H bonds results in weaker interactions between the first water monolayer and the water molecules above the first monolayer. This is the reason that a stable water droplet can form on the water monolayer on the Pd(100), Pt(100), and Al(100) surfaces, while no clear water droplets are observed on other metal surfaces. In addition, we find that the number of within-monolayer H bonds per water molecule in the monolayer outside the droplet is larger than that under water droplet, indicating the water molecules in water droplet will disturb the H bond networks of water monolayer. We have also investigated the within-monolayer H bonds and monolayer-second-layer H bonds of (110) crystal surfaces for different metals as illustrated in Figure 3. We have found that the number of H bonds of within monolayer is much smaller than that on (100) crystal surfaces, resulting in much larger number of monolayer-second-layer H bonds. As a result, the water droplet is not found for the (110) surfaces, and the water molecules cover the surfaces completely. The distribution of H bonds on the (111) crystal face is very similar to that of (110) crystal face, and the comparison of number of H bonds between (111) and (100) faces is shown in Figure S1 of the Supporting Information.

![](./images/814601300699250688_5.jpg)

Figure 3. Average number of H bonds formed by a water molecule in first water monolayer with other water molecules in the same monolayer (black) and by a water molecule in first monolayer with water molecules above first monolayer (red) for (100) and (110) crystal faces, respectively.

The structure of the first water layer is important in understanding the formation of water droplet on water monolayer. A typical example of water molecules near the Pd(100) surface can be found in Figure 4a, which is also quite similar to the Pt(100) surface of the previous work by Limmer et al.⁴⁰ For these structures, water molecules in the monolayer can form a rhombic H bond network, where each molecule in this monolayer forms almost four hydrogen bonds with the four neighboring water molecules. However, similar to our previous work,⁴⁶ thermal fluctuations usually break the H bond network under the water droplet, and some H bonds formed between monolayer and the second layer. This provides a structural basis

![](./images/814601300699250688_6.jpg)

![](./images/814601300699250688_7.jpg)

![](./images/814601300699250688_8.jpg)

![](./images/814601300699250688_9.jpg)

Figure 4. (a) Snapshot of the water molecules in monolayer outside the droplet showing regular two-dimensional (2D) ordered rhombic together with the H bonds (in green lines) forming between neighboring water molecules. (b) Probability distribution of the angle $\varphi$ between the $x$-$y$ plane projection of one water molecule dipole orientation and $x$-axis for (100) crystal face. (c) Probability distribution of the angle $\Psi$ between OH bonds and the $z$-axis. (d) Probability distribution of the angle $\varphi$ between the $x$-$y$ plane projection of one water molecule dipole orientation and $x$-axis for Pd(100), Pd(110), and Pd(111).

that water molecules assemble a water droplet on the water monolayer for the Pd(100), Pt(100), and Al(100) surfaces. The rhombic ordered water structures can be also confirmed by the distribution of the angle $\varphi$ demonstrating the water dipole orientations of the first water layer, where the angle $\varphi$ is calculated by the angle between the projection onto the $x$-$y$ plane of one water dipole orientation and $x$-direction. As shown in Figure 4b, for Pd(100) and Pt(100) surfaces, clear dipole orientation preferences of the water with four highest peaks are found at $\varphi = 0^\circ$, $\varphi = 90^\circ$, $\varphi = 180^\circ$, and $\varphi = 270^\circ$, respectively. However, for Al(100) and Au(100) surfaces, the preferences of water dipole orientation are not so strong as Pd(100) and Pt(100), and the preferences nearly disappeared for the Ni(100) and Pb(100). Figure 4c shows the probability distribution of the angle $\Psi$ between water OH groups of the first water layer and the $z$-axis. It is clear that there are two major peaks at $\Psi \approx 18^\circ$ and $\Psi \approx 90^\circ$ for the (100) crystal surfaces of some metals, indicating the OH bonds pointing to the water above the monolayer and OH bonds tangent to the surface, respectively. The angle of $90^\circ$ dominates the distribution of OH bonds, and it means the water prefers to form H bond networks within the monolayer while the angle of $18^\circ$ means the water in first layer prefers to form H bonds with the water above monolayer. The maximum of the $\Psi \approx 90^\circ$ peak and minimum of the $\Psi \approx 18^\circ$ peak are both found for Pd(100) and Pt(100), which further illustrating the H bond networks are more stable than other metals.

For (110) and (111) crystal surfaces of all the metals, the angles $\varphi$ between the $x$-$y$ plane projection of one water dipole orientation and $x$-axis are very different to that of (100) crystal face. Here, we take the Pd as an example to explore the behaviors of water on different crystal surfaces. As shown in Figure 4d, although four peaks are found for Pd(110) at $\varphi = 45^\circ$, $\varphi = 135^\circ$, $\varphi = 225^\circ$, and $\varphi = 315^\circ$, respectively, the peaks of the probability are much lower than that for Pd(100) surface. As for Pd(111), only one peak is found at $\varphi = 0^\circ$, and the peak is also lower than that for Pd(100). As a result, the ordered water monolayer on Pd(110) and Pd(111) is not as stable as that on Pd(100) and the H bonds of water molecules in monolayer are disturbed by the water above them. This results in the smaller number of within-monolayer H bonds and larger number of monolayer-second-layer H bonds (see Figure 3 and Figure S1 in the Supporting Information).

Another arising question is why the lattice constants and crystal faces affect the ordered structures of the water molecules on metal surfaces. For the eight metal surfaces with the same (100) faces, we have computed the adjacent oxygen-oxygen distance (O-O) of first water layer and the distance between adjacent surface metal atoms (M-M). The results are shown in Figure 5a. Clearly, for Pd(100), Pt(100), and Al(100), the difference between the O-O distance and M-M distance are smaller than that for other metals. This indicates the structures of surface atoms of Pd(100), Pt(100), and Al(100) match the O-O distance of the first water layer and favor the formation of the more stable H bond network of the first water layer very well. In contrast, for other (100) surfaces, the first water layers are much disturbed by the water molecules above them due to the nonmatching between the O-O distance and M-M distance, and the droplet cannot form on the water monolayer. The better matching between the surface atoms results in the more ordered water monolayers.

Besides the lattice constant, the matching of H bond networks and atomic arrangement of the crystal face is also very important. To form a stable rhombic 2D H bond network, one

![](./images/814601300699250688_10.jpg)

Figure 5. (a) Adjacent oxygen−oxygen distance of first water layer and distance of adjacent (100) surface atoms as a function of lattice constant. (b) First layer lattice for Pd(100), Pd(110), and Pd(111) surfaces; the red, white, and blue spheres denote oxygen, hydrogen, and metal atoms, respectively.

water molecule in the water monolayer prefers to form four H bonds with the nearest neighbors, since no hydrogen bonds can form between monolayer and solid surface. This requires four nearest water molecules around each water molecule. To optimize this matching, the arrangement of the metal surface atoms should be square, as manifest of the unit shape of the (100) surface in Figure 5b, taking the Pd as an example. In addition, the H−O−H angle of water molecule is 109.5°, close to the angle 90° of the square atomic arrangement. We have also presented the unit shapes of the surface (110) and (111) in Figure 5b, which are rectangle and rhombic, respectively. For Pd(110), though there are four nearest surface atoms around each surface atom, anisotropy distances of atom arrangement in x and y directions will disrupt the hydrogen bond network of the monolayer. While for Pd(111), though the distance between the two nearest atoms could match the O−O distance very well, there are six nearest-neighboring atoms around each atom, together with the rhombic angle 60° obviously deviating from H−O−H angle 109.5°, hindering the formation of the stable rhombic hydrogen bond network of the monolayer as well.

## 4. CONCLUSIONS

In summary, we have studied the nanoscale wetting behaviors of water molecules on some FCC metals. We have found that both the lattice constants and crystal surfaces greatly affect the wettability of FCC metals. Particularly, stable water droplets on water monolayers are found on crystal surface (100) of the metals Pd, Pt, and Al. The key to the water droplet on the water monolayer is the appropriate matching between the surface atoms arrangement and water molecules, which results in the rhombic ordered water monolayers. The ordered water structures reduce the number of hydrogen bond formed between the monolayers and other water molecules. In contrast, no water droplet can be found on other metal surfaces (Ni, Cu, Au, Ag, Pb) with (100) crystal surface and all of those metal surfaces with (110) and (111) crystal faces due to the lack of ordered water. Our work provides a better understanding of the wettability of some FCC metals and helps to expand our understanding of hydrophobicity and hydro- philicity and the "molecular-scale hydrophilicity"24 we proposed. Particularly, more attentions should be paid when the macroscopic surface contact angles on some specific solid surfaces with ordered water are measured in the experiments, where the apparent contact angles may reflect the wetting degree of adsorbed water, rather than the wetting degree of solid surfaces. We note that the metal surfaces are easily to be oxidized, which may affect the surface constituent and atomic arrangements. This may account of the fact that there is still lack of the direct experimental evidence of the room temperature "ordered water monolayer that does not completely wet water" on the mental surfaces. In applications, we have found that the ordered water monolayer that does not completely wet water can reduce the surface frictions¹⁸ at the hydrophilic surfaces. It should be noted that the work by Ho et al.¹⁶ presented direct slip length on the hydrophilic surfaces, which also shows the friction reduction at hydrophilic surfaces.

## ASSOCIATED CONTENT

### Supporting Information
The Supporting Information is available free of charge on the ACS Publications website at DOI: 10.1021/acs.jpcc.5b04237.

Detailed box sizes for all the simulation systems with metal surfaces, the thickness of the first water layer on different metal surfaces, the average number of H bonds formed by a water molecule in the first water monolayer for (100) and (111) crystal faces of the metals, the average adsorption energy per water molecule on (111) surface of some metals, and some typical water structure on Cu(110) and Pt(111) surface at low temperature to check the accuracy of the force field (PDF)

## AUTHOR INFORMATION

### Corresponding Author
*E-mail wangchunlei@sinap.ac.cn; Tel +86-21-39523458 (C.W.).

### Notes
The authors declare no competing financial interest.

## ACKNOWLEDGMENTS

We gratefully acknowledge Drs. Beien Zhu and Quanzi Yuan for the helpful discussions. This work was supported by the National Science Foundation of China (Grant Nos. 11290164 and 11204341), the Key Research Program of Chinese Academy of Sciences (Grant No. KJZD-EW-M03), the Knowledge Innovation Program of SINAP, the Knowledge Innovation Program of the Chinese Academy of Sciences, the Youth Innovation Promotion Association CAS, Hundred People Project from Chinese Academy of Sciences, and Pu- jiang Rencai Project from Science and Technology Commission of Shanghai Municipality (13PJ1410400), Shanghai Super- computer Center of China, Deepcomp 7000, and ScGrid of Supercomputing Center, Computer Network Information Center of Chinese Academy of Sciences.

## REFERENCES

(1) Li, Y.; Gao, Y. Interplay between Water and Anatase (101) Surface with Subsurface Oxygen Vacancy. *Phys. Rev. Lett.* 2014, 112, 206101.

(2) Giovambattista, N.; Debenedetti, P. G.; Rossky, P. J. Effect of Surface Polarity on Water Contact Angle and Interfacial Hydration Structure. J. Phys. Chem. B 2007, 111, 9581−9587.

(3) Pham, V.-T.; Penfold, T. J.; van der Veen, R. M.; Lima, F.; El Nahhas, A.; Johnson, S. L.; Beaud, P.; Abela, R.; Bressler, C.; Tavernelli, I.; Milne, C. J.; Chergui, M. Probing the Transition from Hydrophilic to Hydrophobic Solvation with Atomic Scale Resolution. J. Am. Chem. Soc. 2011, 133, 12740−12748.

(4) Sommer, A. P.; Zhu, D.; Mester, A. R.; Forsterling, H. D.; Gente, M.; Caron, A.; Fecht, H. J. Interfacial Water an Exceptional Biolubricant. Cryst. Growth Des. 2009, 9, 3852−3854.

(5) Huang, X.; Margulis, C. J.; Berne, B. J. Dewetting-Induced Collapse of Hydrophobic Particles. Proc. Natl. Acad. Sci. U. S. A. 2003, 100, 11953−11958.

(6) Introzzi, L.; Fuentes-Alventosa, J. M.; Cozzolino, C. A.; Trabattoni, S.; Tavazzi, S.; Bianchi, C. L.; Schiraldi, A.; Piergiovanni, L.; Farris, S. Wetting Enhancer” Pullulan Coating for Antifog Packaging Applications. ACS Appl. Mater. Interfaces 2012, 4, 3692−3700.

(7) Chen, F.; Zhang, D.; Yang, Q.; Yong, J.; Du, G.; Si, J.; Yun, F.; Hou, X. Bioinspired Wetting Surface via Laser Microfabrication. ACS Appl. Mater. Interfaces 2013, 5, 6777−6792.

(8) Wang, J.; Liu, M.; Ma, R.; Wang, Q.; Jiang, L. In Situ Wetting State Transition on Micro- and Nanostructured Surfaces at High Temperature. ACS Appl. Mater. Interfaces 2014, 6, 15198−15208.

(9) Zhu, C.; Li, H.; Huang, Y.; Zeng, X. C.; Meng, S. Microscopic Insight into Surface Wetting: Relations between Interfacial Water Structure and the Underlying Lattice Constant. Phys. Rev. Lett. 2013, 110, 126101.

(10) Chandler, D. Interfaces and the Driving Force of Hydrophobic Assembly. Nature 2005, 437, 640−647.

(11) Zangi, R.; Berne, B. J. Aggregation and Dispersion of Small Hydrophobic Particles in Aqueous Electrolyte Solutions. J. Phys. Chem. B 2006, 110, 22736−22741.

(12) Zhao, L.; Wang, C.; Liu, J.; Wen, B.; Tu, Y.; Wang, Z.; Fang, H. Reversible State Transition in Nanoconfined Aqueous Solutions. Phys. Rev. Lett. 2014, 112, 078301.

(13) Zhou, R. H.; Huang, X. H.; Margulis, C. J.; Berne, B. J. Hydrophobic Collapse in Multidomain Protein Folding. Science 2004, 305, 1605−1609.

(14) Liu, P.; Huang, X. H.; Zhou, R. H.; Berne, B. J. Observation of a Dewetting Transition in the Collapse of the Melittin Tetramer. Nature 2005, 437, 159−162.

(15) Ren, X.; Zhou, B.; Wang, C. Promoting Effect of Ethanol on Dewetting Transition in the Confined Region of Melittin Tetramer. Nucl. Sci. Technol. 2012, 23 (252), 252−256.

(16) Ho, T. A.; Papavassiliou, D. V.; Lee, L. L.; Striolo, A. Liquid Water Can Slip on a Hydrophilic Surface. Proc. Natl. Acad. Sci. U. S. A. 2011, 108, 16170.

(17) Tocci, G.; Joly, L.; Michaelides, A. Friction of Water on Graphene and Hexagonal Boron Nitride from Ab Initio Methods: Very Different Slippage Despite Very Similar Interface Structures. Nano Lett. 2014, 14, 6872−6877.

(18) Wang, C.; Wen, B.; Tu, Y.; Wan, R.; Fang, H. Friction Reduction at a Superhydrophilic Surface: Role of Ordered Water. J. Phys. Chem. C 2015, 119, 11679−11684.

(19) Ball, P. Material Witness: When Water doesn't Wet. Nat. Mater. 2013, 12, 289−289.

(20) Wang, C. L.; Zhou, B.; Tu, Y. S.; Duan, M. Y.; Xiu, P.; Li, J. Y.; Fang, H. P. Critical Dipole Length for the Wetting Transition Due to Collective Water-dipoles Interactions. Sci. Rep. 2012, 2, 358.

(21) Yuan, Q.; Zhao, Y.-P. Precursor Film in Dynamic Wetting, Electrowetting, and Electro-Elasto-Capillarity. Phys. Rev. Lett. 2010, 104, 246101.

(22) Carrasco, J.; Hodgson, A.; Michaelides, A. A molecular Perspective of Water at Metal Interfaces. Nat. Mater. 2012, 11, 667−674.

(23) Giovambattista, N.; Rossky, P. J.; Debenedetti, P. G. Computational Studies of Pressure, Temperature, and Surface Effects on the Structure and Thermodynamics of Confined Water. Annu. Rev. Phys. Chem. 2012, 63, 179−200.

(24) Shi, G.; Shen, Y.; Liu, J.; Wang, C.; Wang, Y.; Song, B.; Hu, J.; Fang, H. Molecular-scale Hydrophilicity Induced by Solute: Molecular-thick Charged Pancakes of Aqueous Salt Solution on Hydrophobic Carbon-based Surfaces. Sci. Rep. 2014, 4, 6793.

(25) Godawat, R.; Jamadagni, S. N.; Garde, S. Characterizing Hydrophobicity of Interfaces by Using Cavity Formation, Solute Binding, and Water Correlations. Proc. Natl. Acad. Sci. U. S. A. 2009, 106, 15119−15124.

(26) Ren, X.; Wang, C.; Zhou, B.; Fang, H.; Hu, J.; Zhou, R. Ethanol Promotes Dewetting Transition at Low Concentrations. Soft Matter 2013, 9, 4655.

(27) Ren, X.; Zhou, B.; Wang, C. Water-induced Ethanol Dewetting Transition. J. Chem. Phys. 2012, 137, 024703.

(28) Mei, F.; Zhou, X.; Kou, J.; Wu, F.; Wang, C.; Lu, H. A Transition between Bistable Ice When Coupling Electric Field and Nanoconfinement. J. Chem. Phys. 2015, 142, 134704.

(29) Gabayno, J. L. F.; Liu, D.-W.; Chang, M.; Lin, Y.-H. Controlled Manipulation of $Fe_3O_4$ Nanoparticles in an Oscillating Magnetic Field for Fast Ablation of Nanochannel Occlusion. Nanoscale 2015, 7, 3947−3953.

(30) Giovambattista, N.; Lopez, C. F.; Rossky, P. J.; Debenedetti, P. G. Hydrophobicity of Protein Surfaces: Separating Geometry From Chemistry. Proc. Natl. Acad. Sci. U. S. A. 2008, 105, 2274−2279.

(31) Yang, Z.; Shi, B.; Lu, H.; Xiu, P.; Zhou, R. Dewetting Transitions in the Self-Assembly of Two Amyloidogenic $\beta$-Sheets and the Importance of Matching Surfaces. J. Phys. Chem. B 2011, 115, 11137−11144.

(32) Hoffer, E. K.; Sultan, S.; Herskowitz, M. M.; Daniels, I. D.; Sclafani, S. J. A. Prospective Randomized Trial of a Metallic Intravascular Stent in Hemodialysis Graft Maintenance. J. Vasc. Interv. Radiol. 1997, 8, 965−973.

(33) Erb, R. A. Wettability of Metals under Continuous Condensing Conditions. J. Phys. Chem. 1965, 69, 1306−1309.

(34) Feibelman, P. J. Partial Dissociation of Water on Ru(0001). Science 2002, 295, 99−102.

(35) Heinz, H.; Vaia, R. A.; Farmer, B. L.; Naik, R. R. Accurate Simulation of Surfaces and Interfaces of Face-Centered Cubic Metals Using 12−6 and 9−6 Lennard-Jones Potentials. J. Phys. Chem. C 2008, 112, 17281−17290.

(36) Meng, S.; Wang, E. G.; Gao, S. Water Adsorption on Metal Surfaces: A General Picture from Density Functional Theory Studies. Phys. Rev. B: Condens. Matter Mater. Phys. 2004, 69, 195404.

(37) Meng, S.; Xu, L. F.; Wang, E. G.; Gao, S. W. Vibrational Recognition of Hydrogen-bonded Water Networks on a Metal Surface. Phys. Rev. Lett. 2002, 89, 167104.

(38) Michaelides, A.; Morgenstern, K. Ice Nanoclusters at Hydro- phobic Metal Surfaces. Nat. Mater. 2007, 6, 597−601.

(39) Ogasawara, H.; Brena, B.; Nordlund, D.; Nyberg, M.; Pelmenschikov, A.; Pettersson, L. G. M.; Nilsson, A. Structure and Bonding of Water on Pt(111). Phys. Rev. Lett. 2002, 89, 276102.

(40) Limmer, D. T.; Willard, A. P.; Madden, P.; Chandler, D. Hydration of Metal Surfaces can be Dynamically Heterogeneous and Hydrophobic. Proc. Natl. Acad. Sci. U. S. A. 2013, 110, 4200−4205.

(41) Esswein, A. J.; Nocera, D. G. Hydrogen Production by Molecular Photocatalysis. Chem. Rev. 2007, 107, 4022−4047.

(42) Li, X.; Wang, L.; Fan, Y.; Feng, Q.; Cui, F.-z. Biocompatibility and Toxicity of Nanoparticles and Nanotubes. J. Nanomater. 2012, 6.

(43) Tyson, W. R.; Miller, W. A. Surface Free Energies of Solid Metals: Estimation from Liquid Surface Tension Measurements. Surf. Sci. 1977, 62, 267−276.

(44) Osman, M. A.; Keller, B. A. Wettability of Native Silver Surfaces. Appl. Surf. Sci. 1996, 99, 261−263.

(45) Meng, S.; Wang, E. G.; Gao, S. A Molecular Picture of Hydrophilic and Hydrophobic Interactions from ab initio Density Functional Theory Calculations. J. Chem. Phys. 2003, 119, 7617−7620.

(46) Wang, C. L.; Lu, H. J.; Wang, Z. G.; Xiu, P.; Zhou, B.; Zuo, G. H.; Wan, R. Z.; Hu, J.; Fang, H. P. Stable Liquid Water Droplet on a


Water Monolayer Formed at Room Temperature on Ionic Model Substrates. *Phys. Rev. Lett.* 2009, 103, 137801.

(47) Wang, C.; Zhou, B.; Xiu, P.; Fang, H. Effect of Surface Morphology on the Ordered Water Layer at Room Temperature. *J. Phys. Chem. C* 2011, 115, 3018−3024.

(48) Giovambattista, N.; Debenedetti, P. G.; Rossky, P. J. Enhanced Surface Hydrophobicity by Coupling of Surface Polarity and Topography. *Proc. Natl. Acad. Sci. U. S. A.* 2009, 106, 15181−15185.

(49) Wang, J.; Bratko, D.; Luzar, A. Probing Surface Tension Additivity on Chemically Heterogeneous Surfaces by a Molecular Approach. *Proc. Natl. Acad. Sci. U. S. A.* 2011, 108, 6374−6379.

(50) Sha, M.; Dou, Q.; Luo, F.; Zhu, G.; Wu, G. Molecular Insights into the Electric Double Layers of Ionic Liquids on Au(100) Electrodes. *ACS Appl. Mater. Interfaces* 2014, 6, 12556−12565.

(51) Jiang, X.; Gao, J.; Huynh, T.; Huai, P.; Fan, C.; Zhou, R.; Song, B. An improved DNA Force Field for ssDNA Interactions with Gold Nanoparticles. *J. Chem. Phys.* 2014, 140, 234102.

(52) Heinz, H.; Farmer, B. L.; Pandey, R. B.; Slocik, J. M.; Patnaik, S. S.; Pachter, R.; Naik, R. R. Nature of Molecular Interactions of Peptides with Gold, Palladium, and Pd−Au Bimetal Surfaces in Aqueous Solution. *J. Am. Chem. Soc.* 2009, 131, 9704−9714.

(53) Nirmalraj, P.; Thompson, D.; Molina-Ontoria, A.; Sousa, M.; Martín, N.; Gotsmann, B.; Riel, H. Nanoelectrical Analysis of Single Molecules and Atomic-scale Materials at the Solid/liquid Interface. *Nat. Mater.* 2014, 13, 947−953.

(54) Hess, B.; Kutzner, C.; van der Spoel, D.; Lindahl, E. GROMACS 4: Algorithms for Highly Efficient, Load-Balanced, and Scalable Molecular Simulation. *J. Chem. Theory Comput.* 2008, 4, 435−447.

(55) Darden, T.; York, D.; Pedersen, L. Particle Mesh Ewald: An N-log(N) Method for Ewald Sums in Large Systems. *J. Chem. Phys.* 1993, 98, 10089−10092.

(56) Berendsen, H. J. C.; Grigera, J. R.; Straatsma, T. P. The Missing Term in Effective Pair Potentials. *J. Phys. Chem.* 1987, 91, 6269−6271.

(57) James, M.; Darwish, T. A.; Ciampi, S.; Sylvester, S. O.; Zhang, Z.; Ng, A.; Gooding, J. J.; Hanley, T. L. Nanoscale Condensation of Water on Self-assembled Monolayers. *Soft Matter* 2011, 7, 5309−5318.

(58) Lutzenkirchen, J.; Zimmermann, R.; Preocanin, T.; Filby, A.; Kupcik, T.; Kuttner, D.; Abdelmonem, A.; Schild, D.; Rabung, T.; Plaschke, M.; Brandenstein, F.; Werner, C.; Geckeis, H. An Attempt to Explain Bimodal Behaviour of the Sapphire C-plane Electrolyte Interface. *Adv. Colloid Interface Sci.* 2010, 157, 61−74.

(59) Wang, Y.; Duan, Z.; Fan, D. An Ion Diffusion Method for Visualising a Solid-like Water Nanofilm. *Sci. Rep.* 2013, 3, 3505.

(60) Rotenberg, B.; Patel, A. J.; Chandler, D. Molecular Explanation for Why Talc Surfaces Can Be Both Hydrophilic and Hydrophobic. *J. Am. Chem. Soc.* 2011, 133, 20521−20527.

(61) Phan, A.; Ho, T. A.; Cole, D. R.; Striolo, A. Molecular Structure and Dynamics in Thin Water Films at Metal Oxide Surfaces: Magnesium, Aluminum, and Silicon Oxide Surfaces. *J. Phys. Chem. C* 2012, 116, 15962−15973.

(62) Vanzo, D.; Bratko, D.; Luzar, A. Wettability of Pristine and Alkyl-functionalized Graphane. *J. Chem. Phys.* 2012, 137, 034707.

(63) Wang, C.; Li, J.; Fang, H. Ordered Water Monolayer at Room Temperature. *Rend. Fis. Acc. Lincei* 2011, 22, 5−16.

(64) Wang, C.; Zhao, L.; Zhang, D.; Chen, J.; Shi, G.; Fang, H. Upright or Flat Orientations of the Ethanol Molecules on Surface with Charge Dipoles and the Implication on the Wetting Behavior. *J. Phys. Chem. C* 2014, 118, 1873.

(65) Wang, C. L.; Yang, Y. Z.; Fang, H. P. Recent Advances on "Ordered Water Monolayer that does not Completely Wet Water" at Room Temperature. *Sci. China: Phys., Mech. Astron.* 2014, 57, 802−809.

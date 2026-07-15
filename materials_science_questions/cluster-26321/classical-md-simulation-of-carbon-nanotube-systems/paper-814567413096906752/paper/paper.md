# Manipulation of a neutral and nonpolar nanoparticle in water using a nonuniform electric field

Zhen Xu, Chunlei Wang, Nan Sheng, Guohui Hu, Zhewei Zhou', and Haiping Fang'

Citation: *J. Chem. Phys.* **144**, 014302 (2016); doi: 10.1063/1.4939151

View online: http://dx.doi.org/10.1063/1.4939151

View Table of Contents: http://aip.scitation.org/toc/jcp/144/1

Published by the American Institute of Physics

![](./images/814567413096906752_1.jpg)

# Manipulation of a neutral and nonpolar nanoparticle in water using a nonuniform electric field

Zhen Xu, $^{1,2}$ Chunlei Wang, $^{1}$ Nan Sheng, $^{1}$ Guohui Hu, $^{2}$ Zhewei Zhou, $^{2,a)}$ and Haiping Fang $^{1,a)}$

$^{1}$Division of Interfacial Water and Key Laboratory of Interfacial Physics and Technology, Shanghai Institute of Applied Physics, Chinese Academy of Sciences, Shanghai 201800, China
$^{2}$Shanghai Institute of Applied Mathematics and Mechanics, Shanghai Key Laboratory of Mechanics in Energy Engineering, Shanghai University, Shanghai 200072, China

(Received 29 September 2015; accepted 16 December 2015; published online 5 January 2016)

The manipulation of nanoparticles in water is of essential importance in chemical physics, nanotechnology, medical technology, and biotechnology applications. Generally, a particle with net charges or charge polarity can be driven by an electric field. However, many practical particles only have weak and even negligible charge and polarity, which hinders the electric field to exert a force large enough to drive these nanoparticles directly. Here, we use molecular dynamics simulations to show that a neutral and nonpolar nanoparticle in liquid water can be driven directionally by an external electric field. The directed motion benefits from a nonuniform water environment produced by a nonuniform external electric field, since lower water energies exist under a higher intensity electric field. The nanoparticle spontaneously moves toward locations with a weaker electric field intensity to minimize the energy of the whole system. Considering that the distance between adjacent regions of nonuniform field intensity can reach the micrometer scale, this finding provides a new mechanism of manipulating nanoparticles from the nanoscale to the microscale. © 2016 AIP Publishing LLC. [http://dx.doi.org/10.1063/1.4939151]

## I. INTRODUCTION

The controllable manipulations of nanoparticles and molecules $^{1–20}$ are of great importance in natural and industrial applications, such as drug $^{21}$ and biomolecule $^{22}$ delivery, traps for the targeted molecules, $^{23}$ gathering or segregating nanoparticles, $^{24}$ and control of interactions or chemical reactions of materials or molecules. $^{25}$ Many strategies have been employed to achieve these applications, including optical, $^{26}$ mechanical, $^{27}$ thermal, $^{14}$ magnetic, $^{28}$ and electrical $^{29}$ means. Among these approaches, electrical control is particularly attractive because it is relatively noninvasive and nondestructive to the nanoparticles. $^{29–31}$ However, most natural and synthetic nanoparticles have weak and even negligible charge and polarity, (i.e., fullerene, carbon-based nanoparticles, and even many biomolecules), which hinders the electric field to exert a force large enough to drive these nanoparticles directly. To overcome this obstacle, previous efforts were focused on the modification of the nanoparticle with charge or polar groups, which might change the functions of the nanoparticles. Nanoparticle manipulation can be achieved by driving the water droplet enveloping the nanoparticle, such as proposed by Xiu et al. $^{32}$ In their work, a charge-neutral peptide is dissolved in the water droplet and the peptide-water droplet can be driven by an external field. This work benefits from the polarity of water molecules and the strong interactions of water molecules with an external electric field. $^{33–46}$ A drawback to this design is that the peptide-water droplet must be confined to the interior of a non-metal nanotube.

In this work, we propose a new strategy that utilizes a nonuniform electric field to controllably manipulate a neutral and nonpolar nanoparticle in liquid water. We demonstrate this effect under a staircase electric field using molecular dynamics (MD) simulations. Although the electric field weakly or negligibly exerts a force on the nanoparticle directly, it is the nonuniform water around the nanoparticle that makes the nanoparticle spontaneously move along a certain direction. Finally, the nanoparticle arrives at the location where the effects of the existence of the nanoparticle on the changes in water energies are minimized. The nonuniform water around the nanoparticle is produced by the nonuniform staircase electric field, and locations with a higher intensity electric field have lower water energy. When the nanoparticle is initially placed in a region with a higher intensity electric field, it makes the changes in water energy of system larger, and therefore it is forced to move to a region with a lower intensity electric field. Since the interval of each step can be set to the microscale due to the free diffusion of the nanoparticle, the present method can be used to manipulate nanoparticles from the nanoscale to the microscale. Thus, this phenomenon is expected to be applied extensively, including for the manipulation and delivery of biomolecules, materials, and even drugs across large spaces and over short times.

## II. MODELS AND METHODS

A sketch of the physical model is illustrated in Fig. 1(a). There are two parallel solid plates with an area of $5\times5$ nm$^{2}$

$^{a)}$Electronic mail: fanghaiping@sinap.ac.cn and zhwzhou@shu.edu.cn

![](./images/814567413096906752_2.jpg)

FIG. 1. (a) Sketch of the physical model. A nanoparticle is initially located at $z=3.0$ nm (the blue sphere), and the space is filled with water. A staircase electric field is applied perpendicular to the $z$-axis, with 4 steps of $4E$, $3E$, $2E$, and $E$, respectively, from bottom to top. The direction is denoted by the red arrow and the intensity is represented by the sizes of arrows. The dashed lines represent the transition lines of the staircase electric field. The green arrow and purple particle denote the direction of movement and the final position of the nanoparticle. (b) Three typical trajectories. The $z$-coordinate of the center of mass of the nanoparticle is shown for $E = 0.1, 0.2,$ and $0.3$ V/nm, respectively. (c) Average velocities of the nanoparticle as a function of $z$-coordinate. (d) Peak positions of the average velocity and $\mathrm{d}U_{NP-volume}/\mathrm{d}z$.

located at $z = 0$ nm and $z = 24$ nm, respectively. The solid plates are used to prevent the water molecules from crossing the periodic boundary along the $z$-axis, and simple graphenes are chosen as the walls. In addition, to confirm the placement of the graphene plates would not affect the movement of nanoparticle, the new physical models without graphene plates are constructed and discussed in the supplementary material. $^{47}$ The entire space is divided into four equal subspaces along the $z$-direction. An external four-staircase electric field, with four field intensities of $E$, $2E$, $3E$, and $4E$, is applied to the system, where $E$ is the staircase intensity difference. Values of $E = 0.1, 0.2,$ and $0.3$ V/nm are employed, respectively. Then, a sphere nanoparticle is placed in the cubic box at the center of the first subspace nearest to the bottom solid wall. Herein, we take a fullerene $\mathrm{C}_{180}$ with a hollow interior and a radius of 0.59 nm as the sample nanoparticle, which is solvated in a cuboid box. The number of water molecules is $\mathrm{N}=19\ 386$.

MD simulations are performed with the NVT ensemble using GROMACS 4.5.4. $^{48}$ The temperature is maintained at 300 K using the v-rescale method. Periodic boundary conditions are imposed in all directions. The time step in all simulations is set to be 2 fs and the data are collected every 0.5 ps. The Lennard-Jones (LJ) interactions are treated with a cutoff distance of 1.2 nm, and the particle mesh Ewald (PME) method $^{49}$ with a real-space cutoff of 1 nm is used for the long-range electrostatic interactions. The extended simple point charge (SPC/E) model is utilized for the water molecules. $^{50}$ In these simulations, the carbon atoms in $\mathrm{C}_{180}$ are modeled as uncharged LJ particles with the parameters $\sigma_{\mathrm{CC}}=0.34$ nm and $\varepsilon_{\mathrm{CC}}=0.3612$ kJ/mol. The harmonic potentials are used for $\mathrm{C}_{180}$ to maintain a bond length of 0.14 nm and a bond angle of $120^{\circ}$, with the energy constants $393\ 960$ kJ/mol and $527$ kJ$\cdot$mol$^{-1}\cdot$rad$^{-2}$, respectively. Meanwhile, the bonds of $\mathrm{C}_{180}$ are represented by weak proper dihedral angle potentials. We consider the $\mathrm{C}_{180}$-water interaction using a carbon-oxygen LJ potential with the parameters $\sigma_{\mathrm{CO}}=0.33$ nm and $\varepsilon_{\mathrm{CO}}=0.48$ kJ/mol; these have been used widely for carbon-water systems. $^{51-53}$ For each value of $E$, first the nanoparticle is constrained by position restraints and the system is simulated for 4 ns to reach the equilibrium state. Then, the constraints are removed and the simulations are run for 200 ns. To explore the water energy for each water molecule as a function of $z$-coordinate and the water energies of system without nanoparticle, similar systems of a water box without nanoparticles are simulated for 60 ns, and the last 50 ns trajectories are used to calculate the water energies. To calculate the average velocity of the nanoparticle, the entire area along the $z$-axis is divided into 240 small areas $\Delta z$ with range of 0.1 nm. Then, the velocities of the nanoparticles taken from 10 independent cases for each value of $E$ are averaged at each $\Delta z$.

## III. RESULTS AND DISCUSSION

Fig. 1(b) shows three typical trajectories of the $z$-position of the center of mass (COM) for the nanoparticle at $E = 0.1,\ 0.2,$ and $0.3$ V/nm, respectively. All of the nanoparticles move from the region with the highest field intensity to the region with the lowest intensity. We have found that the movement processes can be divided by two processes, "rapidly crossing transition region" and "free diffusion in uniform region." When the nanoparticle moves close to a transition line between these two types of regions, it crosses that transition line rapidly. Then, the nanoparticle fluctuates with a free diffusion between two adjacent transition lines until it is close to the next transition line. To characterize the directional movement quantitatively, the average velocities of the nanoparticle along the $z$-axis are computed (Fig. 1(c)). For

![](./images/814567413096906752_3.jpg)

FIG. 2. (a) Water energy per water molecule as a function of z-coordinate at $E=0.1$ (red line), 0.2 (purple line), and 0.3 (blue line) V/nm. (b) Distributions of angle $\varphi$ between the water dipole and electric field direction. (c) Changes in water energy in the volume of the nanoparticle $\mathrm{U_{NP-volume}}$ (solid lines) along the z-coordinate and the change in energy by $\mathrm{U_{water}-U_{with-NP}}$ due to the insertion of nanoparticle at $z=3$ nm, 9 nm, 15 nm, and 21 nm (symbols) for $E=0.1$, 0.2, and 0.3 V/nm, respectively. Each energy is shown with the value at $z=21$ nm subtracted for $E=0.1$, 0.2, and 0.3 V/nm, respectively. (d) Derivative of water energy in the volume of nanoparticle $\mathrm{d}U_{\text{NP-volume}}/\mathrm{d}z$ as a function of z-coordinate.

each value of $E$, there are three peaks of the average velocities in regions adjacent to the transition lines. This shows that the nanoparticle velocity reaches a maximum at the higher intensity region adjacent to the transition line. Then, the velocity decreases to near 0 until the nanoparticle becomes close to the next transition line.

In order to exploit the physics underlying this phenomenon, we have computed the water energy as a function of the $z$-coordinate, using a pure water model under a staircase electric field. Herein, the water energy consists of water-water interaction energy and the electric energy of water imposed by the electric field, $-\mathbf{E}\cdot \boxed{\mu}$, where $\boxed{\mu}$ is the water dipole moment. In Fig. 2(a), we show the water energy for each water molecule in the region under the different intensities of electric field. We find that water energy for each molecule is lower for the stronger intensity electric field than that for the weaker intensity electric field, consistent with a previous study. $^{54}$ In addition, the separated energy changes of the water-water energy and the electric energy of water are shown in the supplementary material. $^{47}$ The results show that the changes of the total water energy are mainly contributed by the changes of electric energy of water. This is because water is more ordered in a higher field intensity, since the dipole moment of water prefers to be along the field direction. $^{55}$ In Fig. 2(b), we show the changes in the angle $\varphi$ between the water dipole and the field direction along the $z$-axis. Clearly there are sharp changes in the angles near transition lines, causing rapid variations in the water energy for each water molecule.

Now, we consider the situation when the nanoparticle is solvated in the water. The nanoparticle replaces some water molecules and affects the water energies of water molecules around the nanoparticle. First, we consider the changes in water energy due to the nanoparticle inserting under different electric field intensities, denoted here by $\mathrm{U_{NP-volume}}$, which is calculated by summing the water energies of water molecules in the nanoparticle volume. For now, we neglect the impact in water energies of water molecules around the nanoparticle. To illustrate the difference of $\mathrm{U_{NP-volume}}$ at different positions more clearly, each value of $\mathrm{U_{NP-volume}}$ subtracts the value of $\mathrm{U_{NP-volume}}$ at $z=21$ nm for $E=0.1$, 0.2, and 0.3 V/nm, respectively. From Fig. 2(c), the curves of $\mathrm{U_{NP-volume}}$ along the $z$-axis are quite similar to those of water energy for each water molecule; that is, the absolute values of $\mathrm{U_{NP-volume}}$ are larger when the nanoparticle is in a stronger field than that when it is in a weaker field. This indicates that the placement of the nanoparticle in a stronger intensity field results in larger changes in water energies. Accordingly, the nanoparticle in the present system will be forced to move to a location with a weaker intensity, and it reaches a new equilibrium that the changes in water energies are minimized. We speculate that the derivative $\mathrm{d}U_{\text{NP-volume}}/\mathrm{d}z$ should be related to the driving force of the nanoparticle produced by the rate of changes in water energy due to the nanoparticle inserting at different positions. Consequently, the positive and negative values denote the motion of the nanoparticle along the $+z$ and $-z$ directions, respectively. As shown in Fig. 2(d), in the regions adjacent to the transition lines, the values of $\mathrm{d}U_{\text{NP-volume}}/\mathrm{d}z$ are always positive, indicating that the nanoparticle will always move along $+z$ direction in these regions. This is consistent with the COM curves around the transition lines shown in Fig. 1(b). Interestingly, there are maximal values of $\mathrm{d}U_{\text{NP-volume}}/\mathrm{d}z$ near the transition lines. This is consistent with the behavior of the average velocities of the nanoparticle, where the maximal velocity always locates at the region near the transition lines, as shown in Fig. 1(d). When located in the regions far from the transition lines, small positive and negative values of the derivative indicate that the nanoparticle movements are back-and-forth and slow. Under the assumption of over-damping, $^{56}$ the nanoparticle velocity is consistent with the driving force.

In reality, when a nanoparticle is placed in the water, it will change the distribution of nearby water molecules. There are huge fluctuations in the computation when the nanoparticle is placed in water, which requires a huge computational capacity. Thus, we only compute the energy of the whole system $\mathrm{U_{with-NP}}$ when the nanoparticle is placed at four typical positions: $z=3$ nm, 9 nm, 15 nm, and 21 nm. Herein, the $\mathrm{U_{with-NP}}$ is defined as the sum of the water energy and water-nanoparticle interaction energy. Then we calculate the change in energy of the system due to the nanoparticle inserting by

![](./images/814567413096906752_4.jpg)

FIG. 3. Z-coordinate of the COM of the nanoparticle as a function of time for two cases under a V-shape staircase electric field. The initial z-coordinates of the nanoparticle COMs for the two cases are located at 2.5 nm (red) and 22.5 nm (blue), respectively.

$U_{\text{water}} - U_{\text{with-NP}}$, where the $U_{\text{water}}$ denotes the water energy of the pure water system. Also, for clear description, each value of $U_{\text{water}} - U_{\text{with-NP}}$ subtracts the value of $U_{\text{water}} - U_{\text{with-NP}}$ at $z = 21$ nm for $E = 0.1$, 0.2, and 0.3 V/nm, respectively. As shown in Fig. 2(c), the absolute values of $U_{\text{water}} - U_{\text{with-NP}}$ at different positions due to the existence of the nanoparticle decrease when the intensity becomes weaker. This change tendency is consistent with the changes in the water energy in the volume of the nanoparticle $U_{\text{NP-volume}}$. As expected, when the nanoparticle moves from the higher field intensity to the lower field intensity, the changes in energy of system $U_{\text{water}} - U_{\text{with-NP}}$ due to the existence of the nanoparticle become smaller, indicating that the directed motion of the nanoparticle is energetically favorable. We note that the absolute values of $U_{\text{water}} - U_{\text{with-NP}}$ are always larger than that of $U_{\text{NP-volume}}$, however, the difference does not qualitatively affect the tendency of the changes in water energy, as we computed above. This difference consists of the interactions between the water molecules inside the volume of nanoparticle and the water molecules around the nanoparticle, as these interactions are not considered in the calculation of the water energy in the volume of nanoparticle.

It is clear that this type of nonuniform electric field can target a nanoparticle to the desired region. As an example of potential applications, we designed a new V-shaped staircase electric field, shown in Fig. 3, in which the entire region is divided into five equal parts along the z-direction. In these five parts, the field intensity is 0.6, 0.4, 0.2, 0.4, and 0.6 V/nm, respectively. Initially, the COM of the nanoparticle is located at the position (2.5 nm, 2.5 nm, 22.5 nm) and (2.5 nm, 2.5 nm, 2.5 nm), respectively. In both the cases, we can see that the nanoparticle moves toward and finally reaches the range of [10 nm, 15 nm], which is within the weakest field intensity.

## IV. CONCLUSION

In summary, we have demonstrated the feasibility of controlling and manipulating a neutral and nonpolar (or with weak charge or polar) nanoparticle in a water environment, by subjecting it to a staircase electric field. Directed motion occurs even with no (or with a weak) electric interaction between the electric field and the nanoparticle. This remarkable manipulation ability is attributed to a nonuniform water environment induced by the staircase electric field, in which lower water energies are found in regions with the stronger electric field intensity. To minimize the changes in the water energies of the system due to the existence of the nanoparticle, the nanoparticle spontaneously and rapidly crosses the transition regions to an adjacent region with lower uniform field intensity.

We note that the present method for manipulating and targeting nanoparticles can be extended to microscale systems. The particle diffuses almost freely in the uniform field region. A simple estimate shows that, within a time of 0.01 s and 0.1 s, the probabilities that a particle moves over 1 $\mu$m in a uniform region via free diffusion are about 48% and 82%, respectively. Thus, manipulation of the nanoparticles can be achieved in the nanoscale and microscale system through several processes including "rapidly crossing transition region at nanoscale" and "free diffusion in uniform region at nano- or micro-scale." For the experiments, the staircase electric field could be achieved by connecting series of parallel plate capacitors with different field intensity. Moreover, the field intensity can be small since the experimental time interval is much larger than the achievable simulation time. Thus, we expect that the present method can be used to control the delivering, trapping, and separating of nano-materials, molecules, and even drugs across a large space.

## ACKNOWLEDGMENTS

We gratefully acknowledge Dr. Yi Gao, Dr. Beien Zhu, Dr. Jige Chen, and Dr. Xuechuan Nie for the helpful discussions. This work was supported by the NSFC (Grant Nos. 11290164 and 11372175), the Key Research Program of Chinese Academy of Sciences (Grant No. KJZD-EW-M03), the Knowledge Innovation Program of the Chinese Academy of Sciences, the Youth Innovation Promotion Association CAS, the Innovation Program of Shanghai Municipality Education Commission, China (Grant No. 14ZZ095), the Shanghai Supercomputer Center of China, the Deepcomp7000 and ScGrid of the supercomputing Center, and the Computer Network Information Center of the Chinese Academy of Sciences.

$^{1}$D. Račko and P. Cifra, J. Chem. Phys. 138, 184904 (2013).
$^{2}$H.-J. Feng, T. R. Paudel, E. Y. Tsymbal, and X. C. Zeng, J. Am. Chem. Soc. 137, 8227–8236 (2015).
$^{3}$S. Whitelam and S. A. F. Bon, J. Chem. Phys. 132, 074901 (2010).
$^{4}$X. Wang, Y. Chen, L. Xue, N. Pothayee, R. Zhang, J. S. Riffle, T. M. Reineke, and L. A. Madsen, J. Phys. Chem. Lett. 5, 3825–3830 (2014).
$^{5}$O. Andreussi, S. Caprasecca, L. Cuppellini, I. Guarnetti-Prandi, C. A. Guido, S. Jurinovich, L. Viani, and B. Mennucci, J. Phys. Chem. A 119, 5197–5206 (2015).
$^{6}$Y. Zhou, X. Zhou, D. J. Park, K. Torabi, K. A. Brown, M. R. Jones, C. Zhang, G. C. Schatz, and C. A. Mirkin, Nano Lett. 14, 2157–2161 (2014).
$^{7}$W. W. Xu, Y. Gao, and X. C. Zeng, Sci. Adv. 1, e1400211 (2015).
$^{8}$K. F. Rinne, S. Gekle, D. J. Bonthuis, and R. R. Netz, Nano Lett. 12, 1780–1783 (2012).
$^{9}$G. Zhang, S. Peng, Y. Shang, Z.-D. Yang, and X. C. Zeng, J. Mater. Chem. C 2, 10017–10030 (2014).
$^{10}$L. Soukiassian, A. J. Mayne, G. Comtet, L. Hellner, G. Dujardin, and A. Gourdon, J. Chem. Phys. 122, 134704 (2005).
$^{11}$J. L. F. Gabayno, D.-W. Liu, M. Chang, and Y.-H. Lin, Nanoscale 7, 3947–3953 (2015).
$^{12}$J. Yao, H. Yan, and C. M. Lieber, Nat. Nanotechnol. 8, 329–335 (2013).
$^{13}$X. Jiang, J. Hu, A. M. Lieber, C. S. Jackan, J. C. Biffinger, L. A. Fitzgerald, B. R. Ringeisen, and C. M. Lieber, Nano Lett. 14, 6737–6742 (2014).

$^{14}$A. Barhoumi, W. Wang, D. Zurakowski, R. S. Langer, and D. S. Kohane, Nano Lett. 14, 3697–3701 (2014).

$^{15}$W. Gu, B. Zhou, T. Geyer, M. Hutter, H. Fang, and V. Helms, Angew. Chem., Int. Ed. 50, 768–771 (2011).

$^{16}$G. Hu, M. Mao, and S. Ghosal, Nanotechnology 23, 395501 (2012).

$^{17}$Y. Tu, M. Lv, P. Xiu, T. Huynh, M. Zhang, M. Castelli, Z. Liu, Q. Huang, C. Fan, H. Fang, and R. Zhou, Nat. Nanotechnol. 8, 594–601 (2013).

$^{18}$A. Barreiro, R. Rurali, E. R. Hernandez, J. Moser, T. Pichler, L. Forro, and A. Bachtold, Science 320, 775–778 (2008).

$^{19}$C. Zhu, H. Li, and S. Meng, J. Chem. Phys. 141, 18C528 (2014).

$^{20}$J. Zhang, X. Xu, and T. Qian, Phys. Rev. E 91, 033016 (2015).

$^{21}$Q. Hu, P. S. Katti, and Z. Gu, Nanoscale 6, 12273–12286 (2014).

$^{22}$A. Khvorova, M. F. Osborn, and M. R. Hassler, Nat. Biotechnol. 32, 1197–1198 (2014).

$^{23}$Y. Pang and R. Gordon, Nano Lett. 12, 402–406 (2012).

$^{24}$K. Thorkelsson, J. H. Nelson, A. P. Alivisatos, and T. Xu, Nano Lett. 13, 4908–4913 (2013).

$^{25}$M. Nakaya, Y. Kuwahara, M. Aono, and T. Nakayama, J. Nanosci. Nanotechnol. 11, 2829–2835 (2011).

$^{26}$T. Iida, J. Phys. Chem. Lett. 3, 332–336 (2012).

$^{27}$H. Kobayashi, S. Hirata, and M. Vacha, J. Phys. Chem. Lett. 4, 2591–2596 (2013).

$^{28}$J.-J. Lee, K. J. Jeong, M. Hashimoto, A. H. Kwon, A. Rwei, S. A. Shankarappa, J. H. Tsui, and D. S. Kohane, Nano Lett. 14, 1–5 (2014).

$^{29}$L. Zheng, J. P. Brody, and P. J. Burke, Biosens. Bioelectron. 20, 606–619 (2004).

$^{30}$T. D. Edwards and M. A. Bevan, Langmuir 30, 10793–10803 (2014).

$^{31}$K. Venta, M. Wanunu, and M. Drndić, Nano Lett. 13, 423–429 (2013).

$^{32}$P. Xiu, B. Zhou, W. Qi, H. Lu, Y. Tu, and H. Fang, J. Am. Chem. Soc. 131, 2840–2845 (2009).

$^{33}$X. J. Gong, J. Y. Li, H. J. Lu, R. Z. Wan, J. C. Li, J. Hu, and H. P. Fang, Nat. Nanotechnol. 2, 709–712 (2007).

$^{34}$J. Su and H. Guo, ACS Nano 5, 351–359 (2010).

$^{35}$S. Joseph and N. R. Aluru, Phys. Rev. Lett. 101, 064502 (2008).

$^{36}$X.-P. Li, G.-P. Kong, X. Zhang, and G.-W. He, Appl. Phys. Lett. 103, 143117 (2013).

$^{37}$J. Kou, H. Lu, F. Wu, J. Fan, and J. Yao, Nano Lett. 14, 4931–4936 (2014).

$^{38}$Q. Yuan and Y.-P. Zhao, Phys. Rev. Lett. 104, 246101 (2010).

$^{39}$C. Wang, H. Lu, Z. Wang, P. Xiu, B. Zhou, G. Zuo, R. Wan, J. Hu, and H. Fang, Phys. Rev. Lett. 103, 137801 (2009).

$^{40}$B. Wang and P. Král, Phys. Rev. Lett. 101, 046103 (2008).

$^{41}$C. D. Daub, D. Bratko, T. Ali, and A. Luzar, Phys. Rev. Lett. 103, 207801 (2009).

$^{42}$G. Hu, A. Xu, Z. Xu, and Z. Zhou, Phys. Fluids 20, 102101 (2008).

$^{43}$Z. Xu, G. Hu, Z. Wang, and Z. Zhou, Appl. Math. Mech. 35, 1–12 (2014).

$^{44}$C. Wang, B. Wen, Y. Tu, R. Wan, and H. Fang, J. Phys. Chem. C 119, 11679–11684 (2015).

$^{45}$Y. He, G. Sun, K. Koga, and L. Xu, Sci. Rep. 4, 6596 (2014).

$^{46}$Z. Xu, G. Hu, Z. Wang, and Z. Zhou, Appl. Math. Mech. 35, 535–540 (2014).

$^{47}$See supplementary material at http://dx.doi.org/10.1063/1.4939151 for new physical model without graphene plates and separated energy changes of water–water energy and electric energy of water.

$^{48}$B. Hess, C. Kutzner, D. van der Spoel, and E. Lindahl, J. Chem. Theory Comput. 4, 435–447 (2008).

$^{49}$T. Darden, D. York, and L. Pedersen, J. Chem. Phys. 98, 10089–10092 (1993).

$^{50}$H. J. C. Berendsen, J. R. Grigera, and T. P. Straatsma, J. Phys. Chem. 91, 6269–6271 (1987).

$^{51}$S.-H. Chong and S. Ham, Angew. Chem., Int. Ed. 53, 3751 (2014).

$^{52}$J. Li, X. Gong, H. Lu, D. Li, H. Fang, and R. Zhou, Proc. Natl. Acad. Sci. U. S. A. 104, 3687–3692 (2007).

$^{53}$R. Wan, J. Li, H. Lu, and H. Fang, J. Am. Chem. Soc. 127, 7166–7170 (2005).

$^{54}$T. Cramer, F. Zerbetto, and R. García, Langmuir 24, 6116–6120 (2008).

$^{55}$S. J. Suresh, A. V. Satish, and A. Choudhary, J. Chem. Phys. 124, 074506 (2006).

$^{56}$G. Goldstein, J. Goldstein, and G. Menzala, Q. Appl. Math. 71, 183–199 (2013).

![](./images/814567413096906752_5.jpg)
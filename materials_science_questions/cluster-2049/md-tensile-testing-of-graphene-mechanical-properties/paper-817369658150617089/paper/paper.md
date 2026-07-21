# Molecular dynamics simulation of shear deformation of multi-layer graphene sheets with Tersoff potential

Xiaoxi Zhao

School of Water Conservancy and Environmental Engineering,
Zhengzhou University,
Zhengzhou 450001, China
Email: xxzhao168@zzu.edu.cn

and
Department of Modern Mechanics,
University of Science and Technology of China,
Hefei 230027, China
Email: zhaox09@mail.ustc.edu.cn

Yizhe Zhang

School of Life Sciences,
Zhengzhou University,
Zhengzhou 450001, China
Email: yizhezhang@126.com

Yongchi Li

Department of Modern Mechanics,
University of Science and Technology of China,
Hefei 230027, China
Email: ycli@ustc.edu.cn

Wei Liu*

School of Life Sciences,
Zhengzhou University,
No. 100, Kexue Avenue,
Zhengzhou 450001, China
Fax: 86-371-67783235
Email: weiliu@zzu.edu.cn
*Corresponding author

Abstract: The failure process of multi-layer graphene sheets with AB stacking order under shear deformation is simulated using molecular dynamics method with Tersoff potential. Shear stress-strain relationships and shear failure modes of zigzag and armchair graphene sheets are obtained, while the effect of the number of graphene layers on the shear properties of zigzag and armchair graphene sheets is investigated. The results indicate that the shear modulus of

Copyright © 2019 Inderscience Enterprises Ltd.

graphene sheets is inclined to diverge with the increase of the number of graphene layers. Moreover, the ultimate stress and shear failure strain of zigzag and armchair graphene sheets are reduced gradually with the increase of the number of graphene layers.

Keywords: multi-layer graphene; shear modulus; molecular dynamics; failure mode; Tersoff potential.

Reference to this paper should be made as follows: Zhao, X., Zhang, Y., Li, Y. and Liu, W. (2019) 'Molecular dynamics simulation of shear deformation of multi-layer graphene sheets with Tersoff potential', *Int. J. Nanomanufacturing*, Vol. 15, Nos. 1/2, pp.12-24.

Biographical notes: Xiaoxi Zhao is currently a Lecturer at the School of Water Conservancy and Environmental Engineering in Zhengzhou University, and is pursuing her on-the-job doctorate at Department of Modern Mechanics in University of Science and Technology of China. Her research interests include simulations of 2D materials and biomechanics.

Yizhe Zhang received his Doctor's degree from the Jilin University in 2006. Currently, he is a Lecturer at the School of Life Sciences in Zhengzhou University. His research interests involve biomaterials and nano materials.

Yongchi Li is currently a Professor at the Department of Modern Mechanics in University of Science and Technology of China. His research work is mainly focused on explosive dynamics and dynamics constitutive relation of materials and structure.

Wei Liu is a Professor at the School of Life Sciences in Zhengzhou University. He received his PhD degree from the Department of Chemical Physics in University of Science and Technology of China. His research activities include biomechanics, biomaterials and 2D materials.

This paper is a revised and expanded version of a paper entitled 'Molecular dynamics simulation of shear deformation of multi-layer graphene sheets with Tersoff potential' presented at International Conference on Energy Material and Nanotechnology (ICEM3-2017), Zhengzhou, China, 14-16 April 2017.

## 1 Introduction

Two-dimensional materials, which possess multiple unique features, have a periodic planar structure at the nanoscale and macroscale and consist of one or several layers of atoms in a direction perpendicular to the planar structure. It has long been considered that strict two-dimensional crystal only exists stably at the absolute zero of temperature. In 2004, a simple micromechanical cleavage method was used to obtain graphene in the atmospheric environment (Novoselov et al., 2004). Graphene is a free-standing one-atom-thick carbon sheet, in which each carbon atom can form three carbon-carbon single bonds with adjacent carbon atoms. Meanwhile, every carbon atom has a non-bonding electron, which can move freely on the surface of the planar honeycomb structure. The structural characteristics of graphene make it unusual stable and a kind of material with many unique properties such as extremely high mechanical strength (Grantab et al.,

2010), good thermal conductivity (Balandin et al., 2008) and excellent electrical conductivity (Kim et al., 2009). The multiple properties attract many attentions in the area of high performance nanoelectronic devices (Kim et al., 2009), high energy storage devices (Hu et al., 2016; Foster et al., 2017), nanocomposite materials (Ramanathan et al., 2008), catalyst (Gao et al., 2017) and environmental purification (He et al., 2016). Many researches on the mechanical properties of graphene mainly focus on the Young's modulus of single- and multi-layer graphene sheets in tension, and the values of Young's modulus obtained with numerical calculation and theoretical analysis are similar to that obtained from atomic force microscopy experiment, which is up to 1 TPa (Bu et al., 2009; Lee et al., 2008; Liu et al., 2007; Reddy et al., 2006).

In recent years, the effect of shear deformation on graphene aroused wide interest. Although the shear modulus of graphene can be extracted from a resonance frequency shift near the absolute zero of temperature, it is hard to conduct experiments for directly measuring the shear modulus of graphene (Liu et al., 2010, 2012). Computational simulations can be performed to obtain the mechanical properties of graphene under shear deformation as an alternative method. Based on the basic principle of physics and quantum chemistry, molecular dynamics is a mathematical simulation, which can obtain the physical information of atoms in a molecular system through the computation. It has gradually become an indispensable method for various nano systems (Irle et al., 2009; Karkalos and Markopoulos, 2017). Min and Aluru (2011) investigated the temperature effect on the shear mechanical properties of graphene using molecular dynamics simulations with the modified AIREBO potential to avoid non-physical phenomenon, but the shear failure modes of graphene were not given. The shear modulus calculated from their simulations ranges from 0.35 to 0.48 GPa. Yi and Chang (2012) just gave the range of the shear modulus of single-layer chiral graphene with molecular dynamics method. Moreover, Ruiz et al. (2015) established the coarse-grained molecular dynamics model to get the shear stiffness of multi-layer graphene sheets for combining with the coarse-grained models of organic macromolecules to explore the properties of hybrid nanocomposite materials. However, some interactions between individual atoms, which are lost in coarse-grained models, are critical for acquiring the accurate value of the shear modulus of graphene sheets and understanding the failure modes of graphene, while the effect of the number of graphene layers on the shear mechanical properties of graphene sheets is not presented.

In this paper, we investigated the shear mechanical properties of multi-layer graphene sheets with most common AB stacking order using molecular dynamics method with Tersoff potential. The shear mechanical responses of zigzag and armchair graphene sheets were explored, and the shear stress-strain curves and shear failure modes were obtained. Furthermore, the variations of shear modulus, the ultimate stress and shear failure strain of graphene sheets were presented with the increase of the number of the graphene layers.

## 2 Methodology

### 2.1 Models

Graphene possesses a hexagonal-cell honeycomb structure, in which one carbon atom forms three carbon-carbon bond (0.142 nm) with three nearest atoms. According to the

edge shapes of monolayer graphene, there are two basic structural pattern, namely, zigzag and armchair (Nakada et al., 1996). The zigzag models of multi-layer graphene sheets with AB stacking, which is the most common order (Charlier et al., 1992), were first constructed using VMD molecular graphics program (http://www.ks.uiuc.edu/Research/vmd/). Since the mechanical properties and electronic structure of armchair graphene are different from those of zigzag (Barone et al., 2006; Min and Aluru, 2011), the armchair models were built by a 90 degree rotation of the zigzag models. The interlayer distance is 0.335 nm (3.35 Å). Figure 1 shows the zigzag model of three-layer graphene sheet, in which carbon atom A of one layer and carbon atom B of adjacent layer have the same horizontal positions. Graphene monolayer for simulation has a dimension of 10 nm × 10 nm and contains 3,984 carbon atoms. The volume of multi-layer graphene sheets equals the size of monolayer graphene multiplied by the interlayer distance.

Figure 1 Schematic illustration of geometric models of zigzag graphene sheets, (a) the top view of single-layer model (b) the top view of double-layer model (c) the top view of three-layer model (d) the side view of three-layer model, in which the interlayer distance is 3.35 Å (see online version for colours)

![](./images/817369658150617089_1.jpg)

Note: For clarity, carbon atoms and carbon-carbon bonds in different layers are displayed in different colours and sizes.

### 2.2 Molecular dynamics method

In molecular dynamics simulations, all atoms or particles of a system are described as mass points and they interact with each other after a fixed period of time (also called time step). When the positions and velocities of the atoms are known, the force exerted on atoms at the current time step can be calculated from the interatomic potentials. At the next time step, positions and velocities of the atoms can be determined using the Newton's equation of motion, in which the force exerted on an atom is equal to its mass multiplied by its acceleration. Moreover, the physical quantities and mechanical properties of the whole system can be computed through statistical analysis of motion trajectories and velocity distribution of the atoms in the system. For a system of N atoms, the force $F$ exerted on atom $i$ can be expressed as the gradient of the total potential energy $U$ as follows:

$$
F_{i}=-\nabla_{i} U \tag{1}
$$

The interatomic potentials are described by potential functions, which is key to determining the accuracy of the system in molecular dynamics simulations. Tersoff potential can describe well the mechanical properties of carbon atoms, silicon atoms and germanium atoms in covalently bonded materials (Tersoff, 1989). The interatomic potentials can be expressed by Tersoff potential function as follows:

$$
U_{T e r s o f f}=\frac{1}{2} \sum_{i} \sum_{j \neq i} f_{C}\left(r_{i j}\right)\left[f_{A}\left(r_{i j}\right)+b_{i j} f_{R}\left(r_{i j}\right)\right] \tag{2}
$$

where $U_{Tersoff}$ is the total potential energy, functions $f_{A}$ and $f_{R}$ are the attractive and repulsive interactions, respectively, $f_{C}$ is a smooth cut-off function, $r_{i j}$ is the distance between atom $i$ and atom $j$, and $b_{i j}$ is the bond order.

However, Tersoff potential cannot represent the atomic interaction between the monolayers in multi-layer graphene sheets. Therefore, the Lennard-Jones (L-J) potential function is introduced to describe the non-bond interactions between the graphene monolayers besides Tersoff potential. The L-J potential function is as follows:

$$
U_{L J}=4 \varepsilon\left[\left(\frac{\sigma}{\gamma}\right)^{12}-\left(\frac{\sigma}{\gamma}\right)^{6}\right] \tag{3}
$$

where $UL_J$ is the potential energy, $\varepsilon$ is the depth of the potential well, $\sigma$ is the finite distance at which the interatomic potential between two atoms is zero, and $\gamma$ is the distance between two atoms. The values of $\varepsilon$ and $\sigma$ are 0.00284 eV and 3.35 nm, respectively. In the formula, the first term exhibits the short-range repulsion between two atoms, and the second term describes the long-range attraction between two atoms.

From a mathematical point of view, the molecular dynamics simulation is regarded as an initial value problem, which could be solved using numerical methods. The physical quantities at time $t+\Delta t$ can be obtained from those at time $t$ and their time derivative for discrete time system. The velocity Verlet algorithm is now widely used to solve the equations of motion in molecular dynamics simulations, which is stated as follows:

$$
\begin{cases}
\vec{x}(t+\Delta t)=\vec{x}(t)+\vec{v}(t)\Delta t+\frac{1}{2}\vec{a}(t)\Delta t^2 \\
\vec{v}(t+\Delta t)=\vec{v}(t)+\frac{\vec{a}(t)+\vec{a}(t+\Delta t)}{2}\Delta t
\end{cases}
\tag{4}
$$

where $\vec{x}(t)$ is the position vector of an atom at time $t$, $\vec{v}(t)$ is the velocity vector of the atom at time $t$, and $\vec{a}(t)$ is the acceleration vector of the atom at time $t$, $\Delta t$ is the time step size.

All molecular dynamics simulations for determining the mechanical properties of multi-layer graphene sheets were performed with LAMMPS package (Plimpton, 1995). The VMD molecular graphics program (Humphrey et al., 1996) was used to display the structure of graphene sheets. Conjugate gradient method was used to minimise graphene models. Periodic boundary condition was considered in all directions. A time step of 1.0 fs was applied for all the simulations. NPT simulations were carried out for 50 ps at a constant temperature of 300 K, which was maintained by Nose-Hoover thermostats. The shear simulations were performed using NVT ensemble after the structural relaxation of graphene. The graphene sheets were deformed at a constant shear strain rate of $1 \times 10^9$ s$^{-1}$. The molecular dynamics trajectory data was collected every picosecond. All deformation simulations were conducted until the failure of graphene sheets.

During the shear simulation of multi-layer graphene models, shear stress-strain relationship can be defined as follows:

$$
\begin{cases}
\tau = \frac{F}{A} \\
\gamma = \tan\theta
\end{cases}
\tag{5}
$$

where $\tau$ is the shear stress, $F$ is the force exerted on multi-layer graphene sheet, $A$ is the cross-sectional area of multi-layer graphene sheet, $\gamma$ is the shear strain and $\theta$ is the shear deflection angle. Moreover, the ultimate stress is the capacity of multi-layer graphene sheet to withstand shear loads tending to produce a sliding failure on graphene sheet along a graphene plane.

## 3 Results and discussion

### 3.1 Mechanical response of multi-layer graphene sheets

The mechanical responses of single-layer and multi-layer graphene sheets were evaluated by shear tests. Figures 2 and 3 show the shear stress-strain curves of zigzag and armchair graphene sheets, respectively. When the strain is less than 0.2, the mechanical responses of zigzag graphene sheets are very similar to those of armchair graphene sheets. The stress of armchair graphene sheets increases rapidly at a strain of 0.30, while the stress of zigzag graphene sheets increases gradually. Once fracture occurs, the stress of armchair graphene sheets and single-layer zigzag graphene quickly decreases toward zero, whereas there are one or several turns in stress-strain curves of other zigzag graphene sheets. The phenomenon is mainly caused by a little difference of the failure mode between different layers.

Figure 2 Shear stress-strain curves of the zigzag models of single- and multi-layer graphene sheets (see online version for colours)

![](./images/817369658150617089_2.jpg)

Figure 3 Shear stress-strain curves of the armchair models of single- and multi-layer graphene sheets (see online version for colours)

![](./images/817369658150617089_3.jpg)

### 3.2 Effect of the number of layer on the shear modulus

Shear modulus can be calculated by the ratio of the stress to the strain at the elastic deformation stage. Least-square regression is used to compute the slope of the linear portion of the shear stress-strain curve in the strain ranges from 0.020 to 0.045. It is illustrated that the volume of multi-layer graphene sheets is necessary for the calculation of the stress according to the classical theory of continuum. The effect of the number of layers on the shear modulus is represented in Figure 4. When the number of layers is not more than five, the value of the shear modulus of zigzag graphene sheet is close to that of

corresponding armchair graphene. Finally, the shear modulus of zigzag graphene sheets begin to diverge from that of the armchair graphene sheets with the increase of the number of layers. However, the values of the shear modulus shown in Figure 4 are close to those reported in the literatures, which range from 200 to 480 GPa (Liu et al., 2012; Ruiz et al., 2015).

Figure 4 Effect of the number of layers on the shear modulus of graphene sheets (see online version for colours)

![](./images/817369658150617089_4.jpg)

### 3.3 Effect of the number of layer on the fracture stress and strain

We investigated the effect of the number of layer on the fracture stress and strain at 300 K. The variation of ultimate stress is represented in Figure 5(a). The ultimate stress of zigzag and armchair graphene sheets decreases with the increase of the number of layers. The ultimate stresses of zigzag graphene sheets are less than those of corresponding armchair graphene sheets. Figure 5(b) shows that the shear failure strain of graphene sheets slightly decreases with the increase of the number of layers. The shear failure strain of zigzag graphene sheet is significantly larger than that of corresponding armchair graphene sheet. Variation tendencies of ultimate stress and shear failure strain can be described using the formula $y = mx + n$, where $y$ is the ultimate stress or the shear failure strain and $x$ is the number of layers. The fitting curves shown in Figure 5 are obtained with least-square linear regression, and fitting parameters $m$ and $n$ are listed in Table 1.

Table 1 The fitting parameters obtained from linear regression analysis

<table>
    <thead>
        <tr>
            <th rowspan="2">Fitting parameter</th>
            <th colspan="2">Ultimate stress</th>
            <th colspan="2">Shear failure strain</th>
        </tr>
        <tr>
            <th>Zigzag</th>
            <th>Armchair</th>
            <th>Zigzag</th>
            <th>Armchair</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>m</td>
            <td>–1.63929</td>
            <td>–0.88929</td>
            <td>–0.00343</td>
            <td>–0.00282</td>
        </tr>
        <tr>
            <td>n</td>
            <td>126.128</td>
            <td>124.128</td>
            <td>0.558</td>
            <td>0.433</td>
        </tr>
    </tbody>
</table>

Figure 5 Effect of the number of layers on (a) the ultimate stress and (b) the shear failure strain of graphene sheets (see online version for colours)

![](./images/817369658150617089_5.jpg)

### 3.4 The fracture mode of multi-layer graphene sheets

Figures 6–8 show the fracture process of three-layer armchair graphene sheets during shear deformation, in which the top, middle and bottom layers of the graphene sheets are displayed in red, green and blue, respectively. The graphene layers begin to decline under shear loading condition in the early stages of deformation. With the increase of the load, wrinkles are apparently observed in each layer, which can result in the softening of materials. When the shear strain reaches 0.428, the obvious damage begin to occur near the upper edge of the top-layer graphene and the lower edge of the bottom-layer graphene

along the shear direction, whereas no carbon-carbon bond breakage is observed in the middle layer. The fracture of the middle layer appears at shear strain of 0.429. The failure modes of the other multi-layer graphene sheets are similar to those of three-layer armchair graphene sheets.

Figure 6 Failure modes of the top layer of the three-layer armchair graphene sheet at a shear strain of (a) 0.428, (b) 0.429 and (c) 0.430 (see online version for colours)

![](./images/817369658150617089_6.jpg)

Figure 7 Failure modes of the middle layer of the three-layer armchair graphene sheet at a shear strain of (a) 0.428, (b) 0.429 and (c) 0.430 (see online version for colours)

![](./images/817369658150617089_7.jpg)

Figure 7 Failure modes of the middle layer of the three-layer armchair graphene sheet at a shear strain of (a) 0.428, (b) 0.429 and (c) 0.430 (continued) (see online version for colours)

![](./images/817369658150617089_8.jpg)

Figure 8 Failure modes of the bottom layer of the three-layer armchair graphene sheet at a shear strain of (a) 0.428, (b) 0.429 and (c) 0.430 (see online version for colours)

![](./images/817369658150617089_9.jpg)

### 4 Conclusions

The shear mechanical properties and the failure modes of multi-layer graphene sheets have been investigated by molecular dynamics simulations. The effect of the number of graphene layers on the shear modulus, ultimate stress and shear failure strain of zigzag and armchair graphene sheets are studied. The results show that the ultimate stress and the shear failure strain of zigzag and armchair graphene sheets decrease with the increase of the number of layers. However, the shear modulus of multi-layer graphene sheets are inclined to finally diverge with the increase of the number of layers.

### Acknowledgements

This research was supported by Special Program for Applied Research on Super Computation of the NSFC-Guangdong Joint Fund (the Second Phase) under Grant No.U1501501 and Key Research Project of the Higher Education of Henan Province, P R China (17A570011).

### References

Balandin, A.A., Ghosh, S., Bao, W., Calizo, I., Teweldebrhan, D., Miao, F. and Lau, C.N. (2008) 'Superior thermal conductivity of single-layer graphene', *Nano Letters*, Vol. 8, No. 3, pp.902-907.

Barone, V., Hod, O. and Scuseria, G.E. (2006) 'Electronic structure and stability of semiconducting graphene nanoribbons', *Nano Letters*, Vol. 6, No. 12, pp.2748-2754.

Bu, H., Chen, Y., Zou, M., Yi, H., Bi, K. and Ni, Z. (2009) 'Atomistic simulations of mechanical properties of graphene nanoribbons', *Physics Letters A*, Vol. 373, No. 37, pp.3359-3362.

Charlier, J.C., Michenaud, J.P. and Gonze, X. (1992) 'First-principles study of the electronic properties of simple hexagonal graphite', *Physical Review B*, Vol. 46, No. 8, pp.4532-4539.

Foster, C.W., Down, M.P., Zhang, Y., Ji X., Rowley-Neale, S.J., Smith, G.C., Kelly, P.J. and Banks, C.E. (2017) '3D printed graphene based energy storage devices', *Scientific Reports*, Vol. 7, No. 42233, pp.1-11.

Gao, H., Zhang, P., Zhao, J., Zhang, Y., Hu, J., Shao, G. (2017) 'enhancement on photocatalytic hydrogen production over the Z-scheme photosynthetic heterojunction system', *Applied Catalysis B: Environmental*, Vol. 210, pp.297-305.

Grantab, R., Shenoy, V.B. and Ruoff, R.S. (2010) 'Anomalous strength characteristics of tilt grain boundaries in graphene', *Science*, Vol. 330, No. 6006, pp.946-948.

He, L., Chen, L., Zhao, Y., Chen, W., Shan, C., Su, Z., Wang, E. (2016) 'TiO2 film decorated with highly dispersed polyoxometalate nanoparticles synthesized by micelle directed method for the efficiency enhancement of dye-sensitized solar cells', *Journal of Power Sources*, Vol. 328, pp.1-7.

Hu, J., Wang, P., Liu, P., Cao, G., Wang, Q., Wei, M., Mao, J., Liang, C., Shao, G. (2016) 'In situ fabrication of nano porous NiO-capped Ni3P film as anode for li-ion battery with different lithiation path and significantly enhanced electrochemical performance', *Electrochimica Acta*, Vol. 220, pp.258-266.

Humphrey, W., Dalke, A. and Schulten, K. (1996) 'VMD – visual molecular dynamics', *Journal Molecular Graphics*, Vol. 14, No. 1, pp.33–38.

Irle, S., Ohta, Y., Okamoto, Y., Page, A.J., Wang, Y. and Morokuma, K. (2009) 'Milestones in molecular dynamics simulations of single-walled carbon nanotube formation: a brief critical review', *Nano Research*, Vol. 2, No. 10, pp.755–767.

Karkalos, N.E. and Markopoulos, A.P. (2017) 'Modeling nano-metric manufacturing processes with molecular dynamics method: a review', *Current Nanoscience*, Vol. 12, No. 999, p.1.

Kim, K.S., Zhao, Y., Jang, H., Lee, S.Y., Kim, J.M., Kim, K.S., Ahn, J., Kim, P., Choi, J. and Hong B.H. (2009) 'Large-scale pattern growth of graphene films for stretchable transparent electrodes', *Nature*, Vol. 457, No. 7230, pp.706–710.

Lee, C., Wei, X., Kystar, J.W. and Hone J. (2008) 'Measurement of the elastic properties and intrinsic strength of monolayer graphene', *Science*, Vol. 321, No. 5887, pp.385–388.

Liu, F., Ming, P.M. and Li, J. (2007) 'Ab initio calculation of ideal strength and phonon instability of graphene under tension', *Physical Review B*, Vol. 76, No. 6, p.064120.

Liu, X., Metcalf, T.H., Robinson, J.T., Houston, B.H. and Scarpa F. (2012) 'Shear modulus of monolayer graphene prepared by chemical vapor deposition', *Nano Letter*, Vol. 12 No. 2, pp.1013–1017.

Liu, X., Robinson, J.T., Wei, Z., Sheehan, P.E., Houston, B.H. and Snow, E.S. (2010) 'Low temperature elastic properties of chemically reduced and CVD-grown graphene thin films', *Diamond and Related Materials*, Vol. 19, Nos. 7–9, pp.875–878.

Min, K. and Aluru, N.R. (2011) 'Mechanical properties of graphene under shear deformation', *Applied Physics Letters*, Vol. 98, No. 1, p.013113.

Nakada, K., Fujita, M., Dresselhaus, G. and Dresselhaus, M.S. (1996) 'Edge state in graphene ribbons: nanometer size effect and edge shape dependence', *Physical Review B*, Vol. 54, No. 24, p.17954.

Novoselov, K.S., Geim, A.K., Morozov, S.V., Jiang, D., Zhang, Y., Dubonos, I.V., Grigorieva, I.V. and Firsov, A.A. (2004) 'Electric field effect in atomically thin carbon films', *Science*, Vol. 306, No. 5696, pp.666–669.

Plimpton, S. (1995) 'Fast parallel algorithms for short-range molecular dynamics', *Journal of Computational Physics*, Vol. 117, No. 1, pp.1–19.

Ramanathan, T., Abdala, A. A., Stankovich, S., Dikin DA, Herrera-Alonso, M., Piner, R.D., Adamson, D.H., Schniepp, H.C., Chen, X., Ruoff, R.S., Nguyen, S.T., Aksay, I.A., Prud'Homme, R.K. and Brinson, L.C. (2008) 'Functionalized graphene sheets for polymer nanocomposites', *Nature Nanotechnology*, Vol. 3, No. 6, pp.327–331.

Reddy, C.D., Rajendran, S. and Liew, K.M. (2006) 'Equilibrium configuration and continuum elastic properties of finite sized graphene', *Nanotechnology*, Vol. 17, No. 3, pp.864–870.

Ruiz, L., Xia, W., Meng, Z. and Keten, S. (2015) 'A coarse-grained model for the mechanical behavior of multi-layer graphene', *Carbon*, Vol. 82, pp.103–115.

Tersoff, J. (1989) 'Modeling solid-state chemistry: interatomic potentials for multicomponent systems', *Physical Review B*, Vol. 39, No. 8, pp.5566–5568.

Yi, L. and Chang, T. (2012) 'Loading direction dependent mechanical behavior of graphene under shear strain', *Science China: Physica, Mechanics and Astronomy*, Vol. 55, No. 6, pp.1083–1087.
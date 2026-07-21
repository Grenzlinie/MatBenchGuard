# A kinetic Monte Carlo simulation of center shift on template-induced surface

Gang Liu, Heng Zhang, Guokui Liu, Shiling Yuan*, Qingzeng Zhu

Key Laboratory of Colloid and Interface Chemistry, Shandong University, Jinan 250100, PR China

---

### HIGHLIGHTS
- The kinetic MC simulation is employed to study the center shift of template-induced deposition.
- Two mechanisms of center shift are proposed: nucleation deviation and growth deviation.
- The dependence of the shift mechanism on the interactions has been confirmed.
- Based on details of the two shift mechanisms, a method for reducing center deviation is supplied.

---

### GRAPHICAL ABSTRACT
![](./images/811147867245772801_1.jpg)

The morphology evolution of deposited particles on patterned substrate surface : a) 500 particles, b) 2000 particles, c) 4000 particles, d) 8000 particles.

---

### ARTICLE INFO
**Article history:**
Received 11 April 2016
Received in revised form 7 September 2016
Accepted 11 September 2016
Available online 13 September 2016

**Keywords:**
Center shift
Kinetic Monte Carlo simulation
Template-induced growth

---

### ABSTRACT
In this paper, the center shift of organic particles on template-induced surface is systematically studied by a series of kinetic Monte Carlo simulations. The morphology evolution of center shift, the dependence of center deviation on interactions and the effects of geometrical sizes are obtained. Based on the morphology evolution of center shift, two different mechanisms are proposed, i.e. nucleation deviation and growth deviation. The former is mainly induced by the lateral nucleation of deposited particles, and the latter is mainly determined by the randomly diffusion motion of deposited particles. The two mechanisms present a significant difference for the evolution of center deviation. Based on the details of the two mechanisms, a possible method for reducing the center deviation is also supplied in the simulation.

© 2016 Elsevier B.V. All rights reserved.

---

## 1. Introduction
Micro/nanofabrication of organic device has received great interest due to its broad potential applications in the areas of organic optics and electronics [1-8]. However, conventional strategies to create scalable high-resolution patterns of organic molecules can't simply be applied to organic materials because they are sensitive to ultraviolet, organic solvents and water that involved in the procedure [9]. Recently, a template-directed growth technique has been successfully proposed to pattern organic functional molecule structures [10-16]. In the technique, the prepatterned surfaces, such as $SiO_2$ surface patterned with Au stripes [13,14],

* Corresponding author.
E-mail address: shilingyuan@sdu.edu.cn (S. Yuan).

http://dx.doi.org/10.1016/j.colsurfa.2016.09.029
0927-7757/© 2016 Elsevier B.V. All rights reserved.

![](./images/811147867245772801_2.jpg)

Fig. 1. The schematic diagram of the center derivation. (sketch map form Wang's experiment [20]).

are used as templates to control the organic structures at predefined areas. Based on the binding-energy differences of the organic particles at different locations on the template, the templatedirected processes can easily realize the full nucleation control of organic particles and create organic patterns with high resolution. Importantly, the technique has been successfully utilized to create well-defined geometric patterns with tunable physical properties [13-16]. Not only the lateral morphology but also the dimension in the out-of-plane-direction can be fully controlled. At the same time, the mechanism of template-directed patterning technique has been successfully examined by Monte Carlo (MC) simulations [17-23]. The area-selective nucleation control conditions [17-19], the morphology evolution of particles [21,22] and the impact of molecular interactions [20,22,23] have been revealed in these simulations. These performed MC simulations bridge the experiments with theory in a good consistence, and supply much impetus for the future patterning experiments of organic molecules.

Although exciting progresses have been witnessed in both experiments and simulations, there are still some challenges for the further application of template-directed technique in micro/nanofabrication of organic devices. For example, the growth of organic aggregate exhibits a significant center shift, as seen in Fig. 1. The position of organic aggregates can't be accurately controlled on the predefined area. The organic aggregates show a large center deviation. The similar experimental phenomenon has been observed in gold square-induced growth of Perylene3,4,9,10-tetracarboxylic dianhydride (PTCDA) and small gold dot-induced growth of N,N'-Di[(N-(3,6-di-tert-butyl-carbazyl))-ndecyl] quinacridone (DtCDQA) [20]. Even the bulge formation of DtCDQA on gold stripe are fully analogous to the center shift [13]. These shifts significant reduce the precision of organic devices.

However, the theoretical and experimental treatments focused on the center shift have rarely been reported. To gain deeper insight on the atomistic mechanisms, the kinetic Monte Carlo (KMC) algorithm based on the coarse-grained model is conducted to analyze these center shifts [21,22]. The goal of the present work is to analyze the aggregation behavior of deposited particles in the shift process, determine the relationship between center deviation and interactions, and find the effects of geometrical sizes using a series of kinetic Monte Carlo simulations.

## 2. Simulation details

In the simulation, a three-dimensional cubic lattice box is used. As shown in Fig. 2, a three dimensional lattice of size $100a \times 100a \times 2a$ ($a$ being the lattice constant), built by gray balls, is employed to represent the $SiO_2$ substrate in the experiment [13,20].

![](./images/811147867245772801_3.jpg)

Fig. 2. Setup of simulation box. The gray balls represent the substrate, the yellow balls stand for prepatterned structures, and the brown balls reflect the organic particles. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

The Au squares with a width of $14a$, a height of $4a$ and a periodicity of $50a$ are introduced to construct the gold cell on the substrate. The periodic boundary conditions are conducted in the template surface to yield a quasi-infinite surface. In the simulation, the height of the square is an important parameter for the diffusion of deposited particles. The height is too high or low, the control of final aggregated morphology will be lost. Here, the height of Au squares is set to $4a$, which have been proved to be appropriate [20,23]. The organic molecules randomly deposit in the lattice box and finally nucleate on the template surface. The amorphous silica dioxide, gold and organic molecules are represented with spherical particles in the coarse-grained model.

Based on same diffusion/binding mechanism, the MC algorithms previously used in template-directed patterning of organic particles [21-23] are modified to explore the center shift in this present work. The same diffusion barrier and diffusion procedure for selected molecules are adopted. In the simulation, the cutoff distance for interactions is $\sqrt{3}a$. The substrate ($s$) and prepatterned patterns ($g$) are fixed and only the organic particles ($p$) can jump in sites of the lattice. There are three energy types: organic particleorganic particle interaction $\varepsilon_{pp}$, organic particle-pattern interaction $\varepsilon_{pg}$ and organic particle-substrate interaction $\varepsilon_{ps}$. The interaction between two arbitrary particles $i$ and $j$ of type $t(i)$ and $t(j)$ is given by:

$$
E_{ij}=-\varepsilon_{t(i)t(j)}f\left(r_{ij}\right) \tag{1}
$$

where $r_{ij}$ denotes the distance between particles $i$ and $j$, and $f(r_{ij})$ is defined as $f(r_{ij})=1$ for $r_{ij} \leq \sqrt{2}a$, $f(r_{ij})=0.5$ for $r_{ij} \leq \sqrt{3}a$ and $f(r_{ij})=0$ for the else. $\varepsilon_{ps}$ and $\varepsilon_{pg}$ are set to 0.3 and 1.3 (unit $k_BT$), respectively. These interaction parameters have been proved to be appropriate [20-23]. Then the potential energy of particle could be calculated by summarizing the total interactions between the organic particle and its surrounding particles:

$$
E_{i}=\sum-\varepsilon_{t(i)t(j)}f\left(r_{ij}\right) \tag{2}
$$

According to the full-diffusion bond-counting barrier model proposed by Larsson [24,25], the diffusion barrier $E_{barrier}$ can be obtained:

$$
E_{barrier}=\alpha\left(E_{i_{new}}+E_{i_{old}}\right)-E_{i_{old}} \tag{3}
$$

Where $E_{i_{old}}$ and $E_{i_{new}}$ are the potential energies of particle in the old and the new site, respectively. Finally, the diffusion rate of particle from old site to new site can be obtained by an Arrhenius expression:

$$
V_{ij}=De^{\left(-E_{barrier}/k_BT\right)} \tag{4}
$$

During each MC step, only one MC move is selected according to the standard Metropolis criterion. In the simulation, one organic particle is randomly added to the system per 10,000 MC steps.

![](./images/811147867245772801_4.jpg)

Fig. 3. Temporal snapshots of morphology evolution of deposited particles on patterned substrate surface. The snapshots were taken after deposit a) 500 particles, b) 2000 particles, c) 4000 particles, d) 8000 particles. The interactions $\varepsilon_{pp}$, $\varepsilon_{ps}$ and $\varepsilon_{pg}$ are set to 2.1, 0.3 and 1.3, respectively.

## 3. Results

### 3.1. Temporal evolution

In the template-directed processes, the binding-energy difference of the organic particles at different locations plays a crucial role in the growth of organic structures. The relative stronger interaction $\varepsilon_{pg}$ between organic particle and prepatterned structure is favored to control nucleation sites of deposited particles on the prepatterned structure. The weaker interaction $\varepsilon_{ps}$ between organic particle and substrate is used for the accretion of the deposited particles on the substrate. The interaction $\varepsilon_{pp}$ between organic particle and organic particle is a dominating parameter for determining the final organic configuration. To get a rich behavior of the center shift, the details of morphology evolution are analyzed when $\varepsilon_{pp}$, $\varepsilon_{ps}$ and $\varepsilon_{pg}$ are 2.1, 0.3 and 1.3, respectively. These interaction energies have been proved appropriate by the temporal snapshots of morphology evolution (Fig. 3a-d).

As shown in Fig. 3, the phenomenon of center shift being similar with Fig. 1 has been observed. Especially in the initial deposition stage, the organic particles exhibit a larger center deviation. Not only the deposited particles aggregated on the lateral surface of squares, but also the particles on the upper surface show a large center deviation (Fig. 3a). Based on the aggregated properties of deposited particles, two types of center shift can be concluded: nucleation deviation and growth deviation. For the nucleation deviation, the loss of nucleation control, especially for the control of nucleation position, is the main cause for the center shift. Once the organic particles nucleate on the substrate where is far away from the center of squares, the final organic aggregated structure would exhibit a large center deviation. The growth deviation is observed mainly on the upper surface of squares. Due to the randomness of diffusion motion, it is difficult to completely control the nucleation position of deposited particles on the upper surface of squares. Thus, it is difficult to realize the center agreement between organic structure and prepatterned square. In Fig. 3a, the organic aggregate stayed on the upper surface of Square 1 shows the typical growth deviation. We note that the influence of growth deviation on final center shift gradually decreases with the increase of deposited particles (Fig. 3a-c). Even when the upper surface of Square 1 is completely covered by the deposited particles (Fig. 3c), the influence of growth deviation can be ignored, i.e. the center of organic aggregate agrees well with the Square 1. With the further increase of deposited particles, the center deviation appears again when the deposited particles overflow the upper surface (Fig. 3d). However, for the nucleation deviation, the amount of deposited particles can't affect the stable aggregates on the lateral surface of squares, and the center shift induced by nucleation deviation can't be completely eliminated by a larger amount of deposited particles.

### 3.2. Center deviation as a function of $\varepsilon_{pp}$

To quantitative analyze the influence of organic particle-substrate interaction $\varepsilon_{pp}$ on the evolution of morphology, we introduced the following parameter as a measurement of center deviation:

$$
r=\left(\left(x_{pattern}-x_{square}\right)^{2}+\left(y_{pattern}-y_{square}\right)^{2}\right)^{1 / 2} \tag{5}
$$

Where $x_{pattern}=\frac{1}{N} \Sigma x_{i}$, $y_{pattern}=\frac{1}{N} \Sigma y_{i}$. Actually, the parameter $r$ is the distance between the center of organic aggregate $(x_{pattern}, y_{pattern})$ and the center of square $(x_{square}, y_{square})$. In case the center of organic aggregate agrees well with the square, $r \approx 0$. In the following simulations, the interaction $\varepsilon_{pp}$ is varied from 0.9 to 2.3 with fixed $\varepsilon_{pg}$ = 1.3 and $\varepsilon_{ps}$ =0.3. The evolutions of center deviation $r$ for different $\varepsilon_{pp}$ are shown in Fig. 4a. The amount of deposited particles is adopted as the abscissa for convenience.

For the small $\varepsilon_{pp}$ of 0.9-1.9, the evolutions of $r$ show the same trend for different $\varepsilon_{pp}$. In the initial deposition stage (Fig. 4b), a rapidly decrease of $r$ with deposited particles is observed. The lowest $r$ is obtained when the amount of deposited particles is about 800. With the further increase of deposited particles, as shown in Fig. 4a, the center deviation $r$ exhibits a significant difference for different $\varepsilon_{pp}$. For the small $\varepsilon_{pp}$ of 0.9-1.3, the center deviation $r$ becomes larger again when the amount of deposited particles exceeds one appropriate number. For the relatively large $\varepsilon_{pp}$ of 1.5-1.9, the center deviation $r$ is still maintained in a relatively low value. There is not a significant increase within 10,000 deposited particles. According to the snapshots of organic particles shown in Fig. 5, the evolution of center deviation $r$ in the range of $0.9 \leq \varepsilon_{pp} \leq 1.9$ actually is the growth deviation. Due to the randomness of nucleation on the upper surface of squares, the center deviation $r$ is much larger in the initial stage. With the increase of deposited particles, more and more particles will aggregate on the upper surface. When the upper surface is full of the deposited particles, the organic pattern would well agree with the squares

![](./images/811147867245772801_5.jpg)

Fig. 4. The evolutions of center deviation $r$ within 10,000 particles a) and 2000 particles b) for different $\varepsilon_{pp}$. The $\varepsilon_{ps}$ and $\varepsilon_{pg}$ are set to 0.3 and 1.3 respectively.

![](./images/811147867245772801_6.jpg)

Fig. 5. The morphology evolution of growth deviation. The $\varepsilon_{ps}$ and $\varepsilon_{pg}$ are set to 0.3 and 1.3 respectively.

![](./images/811147867245772801_7.jpg)

Fig. 6. The morphology evolution of nucleation deviation for $\varepsilon_{pp}=2.3$. The $\varepsilon_{ps}$ and $\varepsilon_{pg}$ are set to 0.3 and 1.3 respectively.

and the lowest center deviation $r \approx 0$ can be obtained. With the further increase of deposited particles, the deposited particles would saturate the upper surface and spread to the lateral surface. Then the center deviation $r$ will become larger again. Here, the saturated amount of deposited particles on the upper surface exhibits a strong correlation with organic particle-substrate interaction $\varepsilon_{pp}$. The stronger $\varepsilon_{pp}$, the more particles can aggregated on the upper surface. As shown in Fig. 5, the overflowing of organic particles from the upper surface to lateral surface can be clearly observed at about 1000 deposited particles for $\varepsilon_{pp}=0.9$. For $\varepsilon_{pp}=1.1$, the overflowing phenomenon is noted at about 4000 deposited particles. However, for the larger $\varepsilon_{pp}$ of 1.3, the saturated amount of deposited particles on the upper surface even exceeds 6000.

For the large $\varepsilon_{pp}$ about $\varepsilon_{pp} \geq 2.1$, the influence of $\varepsilon_{pp}$ on the center shift is different with the growth deviation. The rapidly decrease of $r$ with deposited particles is not observed in the initial deposition stage (Fig. 4b). The center deviation $r$ is relatively larger during the whole deposition process as shown in Fig. 4a. According to the aggregated morphology shown in Fig. 6, we note that the center shift in the range of $\varepsilon_{pp} \geq 2.1$ actually is the nucleation deviation. The initial nucleus which is far away from the center of squares plays a crucial role for the subsequently growth of organic particles. In Fig. 6, most of organic particles aggregate on the lateral surface of squares when the amount of particles is 500 particles. In the initial deposition stage, more and more particles would aggregate on the lateral surface with the increase of organic particles. Thus, an increased trend of $r$ is observed in the initial deposition stage. However, when the amount of deposited particles exceeds 1500 (Fig. 6), much more particles prefer to adsorb on the upper surface of squares. Therefore, a slow decrease of center deviation $r$ with the increase of deposited particles can be observed.

### 3.3. Center deviation as a function of $\varepsilon_{ps}$
As described above, the center shift of organic particles is related with the interaction $\varepsilon_{pp}$. Besides $\varepsilon_{pp}$, the organic particle-substrate interaction $\varepsilon_{ps}$ is also a dominating interaction in determining the diffusion and nucleation of deposited particles. To address the influence of $\varepsilon_{ps}$ on the center shift, in the following simulations, the interaction $\varepsilon_{ps}$ was varied from 0.2 to 1.0 with fixing $\varepsilon_{pg}=1.3$ and $\varepsilon_{pp}=1.6$. Fig. 7a shows the influence of organic particle-substrate interaction $\varepsilon_{ps}$ on the evolution of center shift. Fig. 7b shows the evolution of center shift in the initial deposition stage. For the small $\varepsilon_{ps}$ in the range of 0.2-0.7, the whole evolutions of center deviation $r$ are the typical growth deviation. The initial rapid decrease of $r$ and the subsequent maintaining in the low level are clearly revealed in Fig. 7. The similar value of $r$ further indicates that the interactions $\varepsilon_{ps}$ with different values play a same role in the center shift. Here, the impact of the organic particle-substrate interaction in the range of 0.2-0.7 maybe mainly focus on the accretion of the deposited particles and provide a sufficiently high surface diffusion rate on the substrate. With the further increase of $\varepsilon_{ps}$, a larger center deviation is observed. Even the center shift mechanism is completely changed to nucleation deviation when $\varepsilon_{ps}$ is larger than 0.9.

### 3.4. Effects of geometrical sizes
So far, the temporal evolution of center shift and the influence of interactions have been investigated. Two different mechanisms for center deviation have been proposed, i.e. growth deviation and nucleation deviation. Compared with the growth deviation, the nucleation deviation exhibits a larger center shift. Then we are interested in the next question under which conditions the nucleation deviation can be restricted and a good center consistence can be obtained. Concerning the initial nucleation on the lateral surface of squares, the height of squares maybe play a crucial role in the nucleation deviation. If the height is too high, much more particles would locate on the lateral surface and the diffusion of deposited particles from the lateral surface to the upper surface would be restricted. On the contrary, when the height is low enough, i.e. the height of square is 0, the nucleation deviation maybe change to the growth deviation and a small center deviation can be obtained. In order to clarify the influence of square height, the typical nucleation deviation with $\varepsilon_{pp}=2.1$, $\varepsilon_{ps}=0.3$ and $\varepsilon_{pg}=1.3$ is further analyzed in the following.

As described in Fig. 4, for the system with $\varepsilon_{pp}=2.1$, $\varepsilon_{ps}=0.3$ and $\varepsilon_{pg}=1.3$, the evolution of center deviation $r$ is the typical nucleation deviation. During the whole deposition process, the initial rapid increase and the subsequently slow decrease of $r$ clearly exhibit the property of nucleation deviation. By decreasing the square height from $4a$ to 0, the influence of square height on the center shift is systematically revealed. As shown in Fig. 8, the higher the square is, the larger center shift would be obtained. When the height is $4a$, the evolution of center deviation $r$ is induced by nucleation deviation. However, for the lower squares, a smaller center deviation can be obtained. Even when the height of square is 0, the center shift is completely controlled by the growth deviation and the smallest center deviation $r$ is obtained. Here, the dependence of center deviation on the square height actually supplies a potential method to reduce the center deviation in the template-induced experiments.

![](./images/811147867245772801_8.jpg)

Fig. 7. Temporal evolutions of $r$ within 10,000 particles a) and 2000 particles b) for different $\varepsilon_{ps}$. The $\varepsilon_{pp}$ and $\varepsilon_{pg}$ are set to 1.6 and 1.3 respectively.

![](./images/811147867245772801_9.jpg)

Fig. 8. The relationship between the evolution of center deviation $r$ and the height of squares. The $\varepsilon_{pp}$, $\varepsilon_{ps}$ and $\varepsilon_{pg}$ are 2.3, 0.3 and 1.3, respectively.

### 4. Conclusion

In conclusion, we investigated the center shift of organic particles on template-induced surface using a series of kinetic Monte Carlo simulations. The morphology evolution of center shift, the dependence of center deviation on interactions and the effects of geometrical sizes were systematically explored. In the simulation, two different mechanisms for center shift have been proposed, i.e. nucleation deviation and growth deviation. The two mechanisms present a significant difference for the evolution of center deviation. The nucleation deviation corresponding to a larger center deviation is mainly induced by the lateral nucleation of deposited particles. The growth nucleation is mainly determined by the randomly diffusion motion of deposited particles. In the morphology evolution processes, the initial nucleation control, especially for the first nucleus, plays a crucial role in determining the shift mechanism. Once the organic particles aggregate on the lateral surface of squares, the subsequently evolution of center shift would exhibit the typical property of nucleation deviation. If the organic particles aggregate on the upper surface of squares in the initial deposition stage, the growth deviation would work.

From the simulation, the dependence of shift mechanism on the interactions and the geometrical sizes of the template have been confirmed. The relatively strong organic particle-organic particle interaction $\varepsilon_{pp}$ and the higher squares are favored for the nucleation deviation. On the contrary, the smaller $\varepsilon_{pp}$ and the lower squares can reduce the center deviation, even change the nucleation deviation to growth deviation. That supplies a potential method for template-induced experiments to reduce the center deviation.

### Acknowledgement

We acknowledge the financial support by the National Natural Science Foundation of China (No. 21573130).

### References

[1] X. Fang, Y. Bando, U.K. Gautam, C. Ye, D. Golberg, Inorganic semiconductor nanostructures and their field-emission applications, J. Mater. Chem. 18 (2008) 509-522.

[2] L. Bardotti, B. Prével, P. Jensen, M. Treilleux, P. Mélinon, A. Perez, J. Gierak, G. Faini, D. Mailly, Organizing nanoclusters on functionalized surfaces, Appl. Surf. Sci. 191 (2002) 205-210.

[3] S.Y. Chou, C. Keimel, J. Gu, Ultrafast and direct imprint of nanostructures in silicon, Nature 417 (2002) 835-837.

[4] S. Lenhert, P. Sun, Y. Wang, H. Fuchs, C.A. Mirkin, Massively parallel dip-pen nanolithography of heterogeneous supported phospholipid mutilayer patterns, Small 3 (2007) 71-75.

[5] J. Fan, J.M. Michalik, L. Casado, S. Roddaro, M.R. Ibarra, J.M. De Teresa, Investigation of the influence on graphene by using electron-beam and photo-lithography, Solid State Commun. 151 (2011) 1574-1578.

[6] S.L. Kim, G.M. Kim, Micropatterning on roll surface using photo-lithography processes, Int. J. Precis. Eng. Man. 12 (2011) 763-768.

[7] Y. Bellouard, A. Said, M. Dugan, P. Bado, Fabrication of high-aspect ratio micro-fluidic channels and tunnels using femtosecond laser pulses and chemical etching, Opt. Expr. 12 (2004) 2120-2129.

[8] S.R. Forrest, The Path to Ubiquitous and low-cost organic electronic appliances on plastic, Nature 428 (2004) 911-918.

[9] M. Cölle, M. Büchel, D.M. de Leeuw, Switching and filamentary conduction in non-volatile organic memories, Org. Electron. 7 (2006) 305-312.

[10] W. Wang, D.Y. Zhong, J. Zhu, F. Kalischewski, R.F. Dou, K. Wedeking, Y. Wang, A. Heuer, H. Fuchs, G. Erker, L. Chi, Patterned nucleation control in vacuum deposition of organic molecules, Phys. Rev. Lett. 98 (2007) [225504-4].

[11] W. Wang, C. Du, D. Zhong, M. Hirtz, Y. Wang, N. Lu, L. Wu, D. Ebeling, L. Li, H. Fuchs, L. Chi, Control over patterning of organic semiconductors: step-edge-induced area-selective growth, Adv. Mater. 21 (2009) 4721-4725.

[12] W. Wang, C. Du, H. Bi, Y. Sun, Y. Wang, C. Mauser, E.D. Como, H. Fuchs, L. Chi, Tunable multicolor ordered patterns with two dye molecules, Adv. Mater. 22 (2010) 2764-2769.

[13] W. Wang, C. Du, C. Wang, M. Hirtz, L. Li, J. Hao, Q. Wu, R. Lu, N. Lu, Y. Wang, H. Fuchs, L. Chi, High-resolution triple-color patterns based on the liquid behavior of organic molecules, Small 7 (2011) 1403-1406.

[14] W. Wang, C. Du, L. Li, H. Wang, C. Wang, Y. Wang, H. Fuchs, L. Chi, Addressable organic structure by anisotropic wetting, Adv. Mater. 25 (2013) 2018-2023.

[15] H. Wang, W. Wang, L. Li, J. Zhu, W. Wang, Z. Xie, H. Fuchs, Y. Lei, L. Chi, Surface microfluidic patterning and transporting organic small molecules, Small 10 (2014) 2549-2552.

[16] H. Wang, W. Wang, L. Li, M. Hirtz, C.G. Wang, Y. Wang, Z. Xie, H. Fuchs, L. Chi, Tunable organic hetero-patterns via molecule diffusion control, Small 10 (2014) 3045-3049.

[17] F. Kalischewski, J. Zhu, A. Heuer, Loss of control in pattern-directed nucleation: A theoretical study, Phys. Rev. B 78 (2008) [155401-13].

[18] F. Kalischewski, A. Heuer, Dynamic effects on the loss of control in template-directed nucleation, Phys. Rev. B 80 (2009) [155421-4].

[19] S.F. Hopp, A. Heuer, Kinetic Monte Carlo study of nucleation processes on patterned surfaces, J. Chem. Phys. 133 (2010) [204101-7].

[20] F. Lied, T. Mues, W. Wang, L. Chi, A. Heuer, Different growth regimes on prepatterned surfaces: consistent evidence from simulations and experiments, J. Chem. Phys. 136 (2012) [024704-8].

[21] H. Zhang, G. Liu, W. Wang, L. Chi, S.L. Yuan, Step-edge induced area selective growth: a kinetic Monte Carlo study, RSC Adv. 4 (2014) 25005-25010.

[22] G. Liu, H. Zhang, W. Wang, S.L. Yuan, A kinetic Monte Carlo simulation of surface microfluidic patterning organic molecules based on anisotropic wetting, Chem. Phys. Lett. 628 (2015) 54-59.

[23] G. Liu, H. Zhang, G.K. Liu, S.L. Yuan, A kinetic Monte Carlo simulation of organic particles hetero-patterning on template-induced surface, Colloids Surf. A: Physicochem. Eng. Aspects 494 (2016) 186-193.

[24] M.I. Larsson, Kinetic Monte Carlo simulations of adatom island decay on Cu (111), Phys. Rev. B 64 (2001) [115428-10].

[25] R.F. Sabiryanov, M.I. Larsson, K.J. Cho, W.D. Nix, B.M. Clemens, Surface diffusion and growth of patterned nanostructures on strained surfaces, Phys. Rev. B 67 (2003) [125412-8].
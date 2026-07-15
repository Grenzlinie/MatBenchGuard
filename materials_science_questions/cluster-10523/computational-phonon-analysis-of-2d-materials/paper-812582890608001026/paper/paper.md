# How interlayer twist angles affect thermal conduction of double-walled nanotubes: A non-equilibrium molecular dynamics study

Xianhua Nie $^{a,b}$, Li Zhao $^{a,*}$, Shuai Deng $^{a}$, Xi Chen $^{b}$

$^{a}$ Key Laboratory of Efficient Utilization of Low and Medium Grade Energy (Tianjin University), MOE, Tianjin University, Tianjin300350, China
$^{b}$ Earth Engineering Center, Center for Advanced Materials for Energy and Environment, Department of Earth and Environmental Engineering, Columbia University, New York, NY10027, United States

---

## ARTICLE INFO

**Article history:**
Received 8 December 2019
Revised 6 July 2020
Accepted 19 July 2020

**Keywords:**
Carbon nanotube
Boron nitride nanotube
Twist angle
Thermal conductivity
Non-equilibrium molecular dynamics

---

## ABSTRACT

Carbon nanotubes have been widely considered as a promising low dimensional material in microelectronic, chemical and biological applications. Moreover, assisted by the boron nitride nanotube, the combined nanotube has better strength and thermal stability. In these multi-walled nanotubes, the interlayer twist angle could affect the thermal conductivity. In our previous studies, effects of the interlayer twist angle on thermal conductivity of multilayer graphene have been carefully investigated. However, few studies focus on the thermal conductivity on multi-walled nanotubes with interlayer twist angles. Such knowledge gap poses challenges to their potential applications. Therefore, in this study, the thermal conductivity of 4 types of nanotubes, including double-walled carbon nanotube, double-walled boron nitride nanotube, boron nitride nanotube coaxially wrapped by carbon nanotube and carbon nanotube coaxially wrapped by boron nitride nanotube, is investigated based on the non-equilibrium molecular dynamics simulation. The size effect is firstly evaluated, and then, five different twisted structures according to the chiral angle of the inner tube were taken into consideration at five different temperatures. Moreover, the phonon vibrational density of state was estimated to analyze the underlying mechanisms during the thermal conduction. The results indicate that the interlayer twist angle affects the thermal conductivity. With a constant chiral angle of the outer tube, the thermal conductivity increases as the chiral angle of the inner tube increases, and the maximum value of the thermal conductivity can be obtained when the chiral angle of the inner tube is $30.00^{\circ}$. The observation would guide to study thermal transport in the twisted low dimensional structures.

© 2020 Elsevier Ltd. All rights reserved.

---

## 1. Introduction

Nowadays, the carbon nanotube (CNT) has been widely considered as not only one of the most efficient heat-dissipating materials but also an efficient transistor material [1] due to its admirable thermal conductivity of $\sim 3000\ \mathrm{W\cdot m^{-1}\cdot K^{-1}}$[2], thus it has a promising future in the efficient thermal management of Nano-Electromechanical System (NEMS). Besides, at present, the CNT is also found that it can be utilized as the nano-pump [3,4] and the nano-separator [5,6], which make CNT an appropriate material to design novel nanodevices applied in both chemical and biological fields. Particularly, the temperature gradient and the corresponding vibrational characteristics of CNT also plays a vital role in influencing the performance of the nano-pump and the nano-separator.

Therefore, the thermal performance, especially the thermal conductivity, of the CNT is the foundation of the above applications.

However, because the CNT will be oxidized when the temperature is higher than about 400 K [7], the oxidation temperature is too low to meet the requirement of the emerging applications as the working temperature increases. Therefore, the CNT is usually utilized together with the boron nitride nanotube (BNNT). Compared to CNT, although BNNT has a relatively lower thermal conductivity, its thermal conductivity is still satisfactory [8]. Importantly, it has a better thermal stability. Currently, a novel stable structure combining both CNT and BNNT has been proposed and studied [9,10], and the results indicated that the coaxial structure of BNNT and CNT can improve the oxidation temperature of the CNT [11].

Therefore, as discussed above, the thermal performance of the CNT, as well as the coaxial structure of BNNT and CNT should be paid increasing attention to. Plenty of studies focused on the

* Corresponding author.
E-mail address: jons@tju.edu.cn (L. Zhao).

https://doi.org/10.1016/j.ijheatmasstransfer.2020.120234
0017-9310/© 2020 Elsevier Ltd. All rights reserved.

![](./images/812582890608001026_1.jpg)
![](./images/812582890608001026_2.jpg)

<table>
<caption>Table 1 State-of-the-art of MD studies on thermal transport of nanotubes.</caption>
<thead>
<tr>
<th>Author (Year)</th>
<th>Type of nanotubes</th>
<th>The number of walls</th>
<th>Length of the sample</th>
<th>Maximum value ($\text{W•m}^{-1}•\text{K}^{-1}$)</th>
<th>Factors affecting thermal conduction</th>
</tr>
</thead>
<tbody>
<tr>
<td>Diao et al. (2017) [24]</td>
<td>CNT</td>
<td>Single wall</td>
<td>50–400 nm</td>
<td>1393.1</td>
<td>Different reactive force fields</td>
</tr>
<tr>
<td>Cui et al. (2015) [25]</td>
<td>CNT</td>
<td>Single wall</td>
<td>19.68nm</td>
<td>~1000</td>
<td>Inter-tube additional particles</td>
</tr>
<tr>
<td>Yang et al. (2014) [26]</td>
<td>CNT</td>
<td>Single wall</td>
<td>–</td>
<td>~500</td>
<td>Constructional parameters of the CNT network.</td>
</tr>
<tr>
<td>Salaway et al. (2014) [27]</td>
<td>CNT</td>
<td>Single wall</td>
<td>47–630 nm</td>
<td>~900</td>
<td>Several computational variables.</td>
</tr>
<tr>
<td>Shelly et al. (2010) [28]</td>
<td>CNT</td>
<td>Single wall</td>
<td>12.3 nm, 24.6 nm, and 36.9 nm</td>
<td>~700 (as can be seen in Fig. 4 of the reference)</td>
<td>Length effect</td>
</tr>
<tr>
<td>Xu and Buehler (2009) [29]</td>
<td>CNT</td>
<td>Single wall</td>
<td>49.26 nm</td>
<td>301</td>
<td>Mechanical effects, such as mechanical tensile, compressive and torsional strain.</td>
</tr>
<tr>
<td>Padgett and Brenner (2004) [30]</td>
<td>CNT</td>
<td>Single wall</td>
<td>10–310 nm</td>
<td>350</td>
<td>Chemisorption</td>
</tr>
<tr>
<td>Khalkhali et al. (2019) [31]</td>
<td>Silicene nanotubes</td>
<td>Single wall</td>
<td>40–150 nm</td>
<td>40</td>
<td>Grain boundary, axial strain, random vacancy defect</td>
</tr>
<tr>
<td>Li et al. (2017) [8]</td>
<td>BNNT & CNT</td>
<td>Single wall</td>
<td>20–160 nm</td>
<td>~700 for CNT and ~300 for BNNT</td>
<td>Compare the mechanical and thermal properties between BNNT and CNT</td>
</tr>
<tr>
<td>Jiang et al. (2011) [32]</td>
<td>BNNT</td>
<td>Single wall</td>
<td>–</td>
<td>–</td>
<td>–</td>
</tr>
</tbody>
</table>

thermal conductivity of the nanotubes experimentally and theoretically [12,13]. Direct and reliable understandings can be achieved from experiments. Kim et al. [14] measured the thermal conductivity of a multi-walled CNT, and high thermal conductivity of about $3000\ \text{W•m}^{-1}•\text{K}^{-1}$ was obtained at room temperature. Choi et al. [15] also measured the thermal conductivity of the multi-walled CNT with different sizes utilizing the 3-$\omega$ method, and their results showed that the thermal conductivity ranges from 650 to 830 $\text{W•m}^{-1}•\text{K}^{-1}$. Moreover, Hu et al. [16] studied the thermal transport of single-walled CNT in the temperature range from 295 K to 323 K utilizing the 3-$\omega$ method as well, and the thermal conductivity they obtained ranges from $74\ \text{W•m}^{-1}•\text{K}^{-1}$ to $83\ \text{W•m}^{-1}•\text{K}^{-1}$. Except for individual nanotubes, Qiu et al. [17,18] experimentally studied the thermal transport of the CNT array, and a remarkable enhancement was observed. However, according to the brief overview of experimental studies, it can be found that most of the studies focused on CNT, and less focused on BNNT or other types of nanotubes. In addition, although experiments can provide reliable thermal conductivity of nanotubes, there're still some shortages. Generally, the accuracy is significantly affected by the quality of the nanotube samples, and high accuracy experiments with high purity samples always lead to a high cost. Furthermore, some structural parameters of nanotubes affecting thermal transport are hard to be controlled sometimes, and the mechanism of thermal transport cannot be understood based on experiments.

In order to investigate the thermal transport and understand the underlying mechanism of the thermal conduction of nanotubes, plenty of approaches have been developed [19–23]. Therein, molecular dynamics simulation (MD) can be considered as a powerful tool, and it has been widely utilized to reveal the thermal properties of molecular materials. A brief state-of-the-art of current MD studies on thermal transport of nanotubes is summarized in Table 1. It can be seen from the table: Firstly, the thermal conductivity of the single wall CNT has been extensively studied. However, compared to CNT, fewer studies focused on other nanotubes, like BNNT, and this posed a challenge in the application of some other potential nanotubes and their combined structures.

Secondly, it can also be found that most of the existing MD studies focused on types of single-walled nanotubes. For instance, Li et al. [8] systematically studied the mechanical and thermal properties of the single-walled CNT and BNNT, and the work provided fundamental knowledge of single-walled CNT and BNNT in engineering. Diao et al. [24] studied the thermal conductivity of the single-walled CNT, and the effects of different MD potentials were investigated. This work clarifies the prediction capacity of MD and promotes the application of MD in studying the thermal properties of single-walled CNTs. However, limited studies focused on the thermal conductivity of multi-walled nanotubes. Generally, multi-walled nanotubes have advantages on high strength, large size, and surface area over single-walled nanotubes [33,34]. These advantages make multi-walled nanotubes to be more practical material in engineering. He et al. [9] carefully investigated the thermal property of the coaxial CNT@BNNT multi-walled nanotube, and the effects of temperature and strain on thermal conductivity were analyzed. Nevertheless, in multi-walled nanotubes, the existence of interlayer twist angles is also inevitable, and the effects of interlayer twist angles were not considered in their study. As one of the factors affecting the thermal transport of nanotubes, few studies have been conducted about as shown in Table 1. This is not conducive to the application of multi-walled nanotubes.

Recently, increasing studies on twisted multilayer graphene have been aroused since Cao et al. [35,36], and it becomes a hot research topic rapidly [37]. Some of the followers conducted researches on the electronic properties of types of twisted low dimensional materials [38,39]. Besides, there're some studies on thermal properties [40–42]. Particularly, in our previous studies [43], effects of interlayer twist angles on in-plane and cross-plane thermal conduction of multilayer graphene were carefully investigated. According to all of these studies on twisted graphene, plenty of unique properties like superconductivity [35], local maximum thermal conductivity [43] and so on have been discovered. Furthermore, nanotubes can be seen as being curled from 2D nanosheets. Therefore, how does the thermal conductivity change after the nano-sheet is curled into a nanotube? To the best of the authors' knowledge, few published studies focused on it.

Above all, two main knowledge gaps can be concluded: the first is that the thermal conductivity of BNNT is rarely studied experimentally and theoretically, rather than the combined structure of CNT and BNNT. The second is that the effects of the interlayer twist angle of a multi-walled nanotube on thermal conductivity were rarely reported. Therefore, in this study, effects of the in-

![](./images/812582890608001026_3.jpg)

Fig. 1. Schematic diagram of doublewallcarbonnanotube. (a) Schematic diagram of twisted bilayer graphene. (b) Misoriented base vectors caused by the twist angle. (c) Schematic diagram of the twisted double-walled nanotubes.

terlayer twist angle on the thermal conductivity of several types of nanotubes, including double-walled CNT, double-walled BNNT, BNNT coaxially wrapped by CNT (BNNT@CNT) and CNT coaxially wrapped by BNNT (CNT@BNNT) were investigated utilizing non-equilibrium molecular dynamics (NEMD). The interlayer twist angle of double-walled nanotubes is characterized by the difference of chiral angles between the inner and the outer tubes. In NEMD of this work, the chiral angle of the outer tube is 30.00°, and the chiral angles of inner tubes are 0.00°, 5.82°, 14.70°, 23.41°, and 30.00° depending on the structure of the inner tube respectively. Besides, the vibrational density of state (VDOS) is utilized to analyze the underlying mechanism of the thermal conduction. To the best of the authors' knowledge, this study is one of the few comprehensive and systematic MD studies and analyses on thermal conductivity of double-walled nanotubes with twist angles compared to existing studies.

## 2. Simulation methods

In order to study the effect of interlayer twist angle on thermal conductivity of double-walled nanotubes, the configuration was established. The establishment of the twisted double-walled nanotubes can be seen in Fig. 1. Fundamentally, the nanotubes can be considered to be the graphene curling along a chiral vector $\vec{C}_h$, and the chiral vector can be determined by a pair of base vectors $\vec{a}_1$, $\vec{a}_2$ and chiral parameters $n$, $m$ according to the relations as shown in Eq. (1). Similarly, the twisted double-walled nanotube can be established by the twisted double-layer graphene curling along the chiral vectors, as shown in Fig. 1(a). Nevertheless, because of the existence of the twist angle of graphene, the directions of base vectors of each graphene layer become different, as shown in Fig. 1(b). Consequently, with the same direction of the chiral vector, the chiral parameters $n$ and $m$ should be different. The angle $\langle \vec{a}_1, \vec{C}_h \rangle$ is defined as the chiral angle. The chiral parameters of the twisted layer can be determined as the following:

Firstly, in a stable double-walled CNT and BNNT, the distance between the inner and the outer tubes ranges from 3.40 ~ 3.57 Å, therefore, the chiral parameters should meet the following restrictions as shown in Eq. (2). Where $d$ is the diameter of the nanotube and the subscripts "inner" and "outer" represent the inner tube and the outer tube. The determination of the diameter can be seen in Eq. (3). Where $a_0$ is the lattice constant of graphene or BN nanosheet. The $a_0$ of both graphene and BN nano-sheet is set as 1.43. In this study, the chiral parameter of the outer tube is set as (15, 15), thus a series of chiral parameters of inner tubes can be obtained. Then, the chiral angle of the inner tube (ITCA) is calculated according to Eq. (4). Finally, the ITCA of 0.00°, 5.82°, 14.70°, 23.41°, and 30.00° was selected as the studied structure. Correspondingly, the inner tubes are (17,0), (16,2), (14,5), (12,8) and (10,10) nanotubes. In this study, for convenience, the ITCA is utilized to characterize different cases. Moreover, four different double-walled nanotubes, including double-walled CNT, double-walled BNNT, BNNT@CNT and CNT@BNNT were studied.

$$
C_{h}=n \cdot \vec{a}_{1}+m \cdot \vec{a}_{2} \tag{1}
$$

$$
\Delta d=\frac{1}{2}\left(d_{\text {outer }}-d_{\text {inner }}\right) \in[3.4,3.57] \tag{2}
$$

$$
d=\frac{a_{0} \sqrt{3} \sqrt{n^{2}+n m+m^{2}}}{\pi} \tag{3}
$$

$$
\cos \left\langle\vec{a}_{1}, \vec{C}_{h}\right\rangle=\frac{2 n+m}{2 \sqrt{n^{2}+n m+m^{2}}} \tag{4}
$$

Considering the computational efficiency and the accuracy [31,44,45], the non-equilibrium molecular dynamics (NEMD) simulation was utilized to study the thermal transport of the twisted double-walled nanotubes based on a popular MD package, Large-scale Atomic/Molecular Massively Parallel Simulator (LAMMPS) [46], and the visualization of the simulation was conducted by Open Visualization Tool (OVITO) [47]. In this study, the temperature ranges from 200 K to 600 K with a step of 100 K, and this range covers almost all potential temperatures in the application of nanotubes. Taking BNNT@CNT as an example, the configurations of twisted nanotubes are illustrated in Fig. 2. Wrapped by (15, 15) outer tube, the inner tubes are (17,0), (16,2), (14,5), (12,8) and (10,10) nanotubes with chiral angles of 0.00°, 5.82°, 14.70°, 23.41° and 30.00° respectively, in order to establish the interlayer twist angles.

The optimized Tersoff potential (opt-Tersoff) [48] and Tersoff potential [49] were utilized to describe the C-C and B-N $sp^2$ interactions respectively. Moreover, as for the interlayer interactions, including C-C, C-B, C-N, B-B, B-N, and N-N interactions, were described by Lennard-Jones (L-J) potentials as shown in Eq. (5). All

![](./images/812582890608001026_4.jpg)

Fig. 2. Structure of the studied nanotubes (Taking BNNT@CNT as an example). (a) (17,0)@(15,15) nanotubes. (b) (16,2)@(15,15) nanotubes. (c) (14,5)@(15,15) nanotubes. (d) (12,8)@(15,15) nanotube. (e) (10,10)@(15,15) nanotube.

<table>
<caption>Table 2. L-J parameters applied in this study.</caption>
<thead>
<tr>
<th></th>
<th>C-C</th>
<th>B-B</th>
<th>N-N</th>
</tr>
</thead>
<tbody>
<tr>
<td>$\varepsilon$ / eV</td>
<td>0.002844</td>
<td>0.004116</td>
<td>0.006281</td>
</tr>
<tr>
<td>$\sigma$ / Å</td>
<td>3.4</td>
<td>3.453</td>
<td>3.365</td>
</tr>
</tbody>
</table>

![](./images/812582890608001026_5.jpg)

Fig. 3. Schematic diagram of the NEMD model (all of the lengths are in unit Å).

of the L-J parameters are listed in Table 2. The L-J parameters of C–C interaction were obtained from Girifalco et al. [50], while the L-J parameters of B-B and N-N interactions were obtained from Baowan et al. [51]. The interactions between unlike atoms, like C-B, C-N, and B-N interactions were calculated by the Lorentz-Berthelot mixing rule as shown in Eq. (6). Moreover, the temperature was calculated according to Eq. (7).

$$
u_{IJ}=4\varepsilon\left[\left(\frac{\sigma}{r_{ij}}\right)^{12}-\left(\frac{\sigma}{r_{ij}}\right)^{6}\right] \tag{5}
$$

$$
\varepsilon_{ij}=\sqrt{\varepsilon_{ii}\cdot\varepsilon_{jj}},\quad \sigma_{ij}=\frac{1}{2}\left(\sigma_{ii}+\sigma_{jj}\right) \tag{6}
$$

$$
T_{\text{MD}}=\frac{2}{3Nk_{B}}\sum_{i}\frac{p_{i}^{2}}{2m_{i}} \tag{7}
$$

The diagram of the NEMD can be seen in Fig. 3. Taking the 10 nm nanotube as an example, there're two fixed regions whose lengths are 3 Å located at both sides of the nanotube. This region is utilized to restrict the relative motion of the inner and outer tubes. Next to the fixed region, there're heat source and heat sink located at each side of the nanotube respectively, for the purpose of the heat flux establishment. The heat source is colored in red and the heat sink is colored in blue as shown in Fig. 3, and the lengths of the heat source region and the heat sink region are 10 Å. The average temperature of the heat source and the heat sink is the set temperature of the nanotube, ranging from 200 K to 600 K as indicated above. The temperature of the heat source is the average temperature plus 100 K, while that of the heat sink is the average temperature minus 100 K. Non-periodic boundary condition (shrink-wrapped boundary condition) was performed for x, y, and z directions, and the timestep of the simulation was set as 0.001 ps. During the NEMD, the initial configuration of nanotube was firstly optimized by energy minimization. Then the structure further optimized in the micro-canonical (NVE) ensemble for 1 ns, and the time is long enough to obtain a stable configuration of the nanotube. Furthermore, in order to generate a constant temperature gradient along the nanotube, the Langevin thermostat was performed for the heat source and the heat sink for 1 ns. Followed by which, another 5 ns in the NVE ensemble was conducted in order to obtain a satisfactory linear temperature profile along the nanotube and record the desired statistical parameters for post-processing. It should be noted that each case has been simulated for 5 times in order to evaluate the uncertainty of the thermal conductivity calculation.

One of the temperature profiles of at the equilibrium state can be seen in Fig. 4(a). The nanotube was divided into 100 equal segments, and each point in the figure represents the statistical temperature of each segment. Only the linear region, which is fitted by the red line, can be utilized to calculate the temperature gradient along the nanotube. Furthermore, the thermal conductivity can be calculated by the Fourier's law as shown in Eq. (8). Where $q$ is the heat flux along the nanotube; $k$ is the thermal conductivity; $\partial T/\partial x$ is the temperature gradient along the nanotube; $A$ is the cross-sectional area. It should be noted that the double-walled nanotubes are simplified as two coaxial shells with the thickness of 3.4 Å in order to determine the cross-sectional area $A$. If the thickness of the single walled nanotube is $b$ (equals to 3.4 Å), and the diameters of the inner and the outer tube are $d_{\text{inner}}$ and $d_{\text{outer}}$

![](./images/812582890608001026_6.jpg)
![](./images/812582890608001026_7.jpg)

Fig. 4. Temperature profiles and energy during the quasi-steady heat conduction. (a) A typical temperature profile along the nanotubes. (b) Changes of energy added and subtracted to the simulated system over time.

respectively, the cross-sectional area $A$ can be calculated according to Eq. (9) [24,28,29]. Moreover, the energy added and subtracted from the heat source and the heat sink can be seen in Fig. 4(b). It can be seen that the energy added and subtracted from the nanotube has the same value and growth rate, thus the total energy of the studied system remains constant.

$$
q=-k A \frac{\partial T}{\partial x} \tag{8}
$$

$$
A=\pi b\left(d_{\text {inner }}+d_{\text {outer }}\right) \tag{9}
$$

## 3. Results analyses

### 3.1. Size effects evaluation

The size effect was firstly evaluated and 5 different twisted CNTs with lengths of 5 nm, 10 nm, 20 nm, 50 nm, and 100 nm were considered. All of the evaluations were conducted at the temperature of 200 K. The relationship between the length and the thermal conductivity is illustrated in Fig. 5(a), and the relationship between the ITCA and the thermal conductivity is illustrated in Fig. 5(b). As shown in Fig. 5(a), the horizontal axis represents the length of CNT, and the vertical axis represents the thermal conductivity. Different colors represent different ITCAs of nanotubes. It can be seen that with the same twist angle or ITCA, the thermal conductivity of CNT increases as the length of the CNT increases. Furthermore, as the length of CNT further increases, the growth rate of thermal conductivity with the length decreases. For instance, when the ITCA is 0, the thermal conductivity is 125.2 $\mathrm{W} \bullet \mathrm{m}^{-1} \bullet \mathrm{K}^{-1}$ and $885.7 \mathrm{~W} \bullet \mathrm{m}^{-1} \bullet \mathrm{K}^{-1}$ for 5 nm and 10 nm CNT respectively. The corresponding growth rate of the thermal conductivity with the length is $152.1 \mathrm{~W} \bullet \mathrm{m}^{-1} \bullet \mathrm{K}^{-1} \bullet \mathrm{nm}^{-1}$. Moreover, as the length of the CNT further increases, the thermal conductivity is $1349.8 \mathrm{~W} \bullet \mathrm{m}^{-1} \bullet \mathrm{K}^{-1}$ and $1849.9 \mathrm{~W} \bullet \mathrm{m}^{-1} \bullet \mathrm{K}^{-1}$ for 20 nm and 50 nm CNT respectively, and the corresponding growth rate decreases to $16.67 \mathrm{~W} \bullet \mathrm{m}^{-1} \bullet \mathrm{K}^{-1} \bullet \mathrm{nm}^{-1}$. This result is consistent with some previous studies qualitatively [27,30,31,52].

Moreover, Fig. 5(a) also shows the effect of the interlayer twist angle on thermal conduction, and lines in different colors are close to each other. However, it can be recognized that double-walled CNT has a larger thermal conductivity when the ITCA is larger. For a clearer expression, the relationship among the length of the CNT, the ITCA, and thermal conductivity is presented in Fig. 5(b). In this figure, the horizontal axis represents the ITCA with the unit of degree, while the vertical axis represents the thermal conductivity. Lines with different colors represent different lengths of CNT. Firstly, it can be seen that the changes in the thermal conductivity of CNT with different lengths have a similar trend. Therefore, the effect of interlayer twist angle on thermal conductivity can be studied by CNTs with one specific length qualitatively. Then, it also can be concluded that the thermal conductivity is more sensitive to the length of CNT compared to the ITCA. Intuitively, When the length of the CNT is 10 nm, the thermal conductivity is $885.7 \mathrm{~W} \bullet \mathrm{m}^{-1} \bullet \mathrm{K}^{-1}$ and $942.9 \mathrm{~W} \bullet \mathrm{m}^{-1} \bullet \mathrm{K}^{-1}$ for the ITCA of $0.00^{\circ}$ and $30.00^{\circ}$ respectively. However, when the ITCA is $0.00^{\circ}$, the thermal conductivity can increase from $885.7 \mathrm{~W} \bullet \mathrm{m}^{-1} \bullet \mathrm{K}^{-1}$ to $1349.8 \mathrm{~W} \bullet \mathrm{m}^{-1} \bullet \mathrm{K}^{-1}$ as the length of CNT increases from 10 nm and 20 nm CNT respectively.

Besides, the diameter size effects were also evaluated, and the relationship between the diameter of the twisted double-walled CNT and the thermal conductivity is illustrated in Fig. 6. All of the cross-sectional areas of nanotubes were calculated according to Eq. (9). In this figure, two types of CNT, (15,15) tube whose diameter is 2.03 nm and (30,30) tube whose diameter is 4.07 nm, were selected as outer tubes, and the length of the studied samples is 10 nm. The twisted double-walled CNT was established according to the method introduced in Section 2. It's worth mentioning that as for the (30,30) outer tube, there's no inner tube with ITCA of $0.00^{\circ}$ according to the method. (39,7), (35,13), (31,18) and (25,25) CNT with the chiral angle of $8.11^{\circ}, 15.18^{\circ}, 21.29^{\circ}$, and $30.00^{\circ}$ respectively were selected as the corresponding inner tube. As shown in Fig. 6, results of twisted double-walled CNT with larger radius are demonstrated in solid lines, while that of twisted double-walled CNT with smaller radius are demonstrated in dash lines. Different colors represent different temperatures. It can be seen that double-walled CNT with larger diameter has a significantly lower thermal conductivity. The reason for the phenomenon is that: (1) the length of nanotubes utilized in the evaluation is 10 nm, and a shorter nanotube could enhance the phonon scattering [31], which enlarges the difference of thermal conductivity between nanotubes with a larger and smaller diameter. (2) As the diameter of double-walled CNT increases, the lattice mismatch between the inner and the outer tubes is enhanced, thus the phonon scattering center increases, leading to lower thermal conductivity. Moreover, it can be seen that whether CNT with larger or smaller diameter, the change of thermal conductivity with ITCA shares a similar regulation: the thermal conductivity increases as the ITCA increases and the ther-

![](./images/812582890608001026_8.jpg)

Fig. 5. Length effect evaluation of the twisted double-walled CNTs. (a) The relation- ship between the length and the thermal conductivity. (b) The relationship between the ITCA and thermal conductivity.

![](./images/812582890608001026_9.jpg)

Fig. 6. Diameters sizeeffect evaluation of the twisted double-walled CNTs.

![](./images/812582890608001026_10.jpg)

Fig. 7. The effects of the ITCA on thermal conductivity of double-walled CNT and BNNT. (a) Double-walled CNT. (b) Double-walled BNNT.

mal conductivity decreases as the temperature increases. Further- more, as for the double-walled CNT with a smaller diameter, the thermal conductivity increases by 6.5% as the ITCA increases from 14.70° to 30.00° at 200 K. While as for the double-walled CNT with a larger diameter, the thermal conductivity increases by 2.8% as the ITCA increases from 15.18° to 30.00° at 200 K. Therefore, a smaller diameter has a more significant effect on thermal conductivity. The effects of the interlayer twist angle will be discussed in detail in the following parts.

### 3.2. Effects of the twist angle at different temperatures

The effects of interlayer twist angles on thermal conductivity of double-walled CNT, BNNT, BNNT@CNT, and CNT@BNNT are shown in Fig. 7(a) ~ (b) and Fig. 8(a) ~ (b) respectively. All of these results were obtained by 10 nm nanotubes, due to the qualitative rela- tionship between the ITCA and thermal conductivity is the same for nanotubes with different lengths. In these figures, the horizon- tal axis represents the ITCA, while the vertical axis represents the thermal conductivity. Curves with different colors represent differ- ent temperatures. Besides, the uncertainty of the calculation was

![](./images/812582890608001026_11.jpg)

Fig. 8. The effects of the ITCA on thermal conductivity of combined structures. (a) BNNT@CNT. (b) CNT@BNNT.

indicated by the error bar. As for the double-walled CNT as shown in Fig. 7(a), it can be seen that:

Firstly, the thermal conductivity decreases as the temperature increases, and the rate of decrease in thermal conductivity with the increasing temperature decreases. For instance, with the ITCA of 0.00°, the thermal conductivity decreases from 885.7 $W•m^{-1}•K^{-1}$to 696.3 $W•m^{-1}•K^{-1}$ as temperatures increases from 200 K to 300 K, decreased by 21.38%. Furthermore, when the temperature increases from 500 K to 600 K, the thermal conductivity decreases from 517.4 $W•m^{-1}•K^{-1}$ to 464.3 $W•m^{-1}•K^{-1}$, decreased by 10.26%. Nanotubes with other ITCAs also share the same regulation.

Secondly, at a specific temperature, the thermal conductivity increases as the ITCA increase monotonically, and there's a maximum value when the chiral angle is 30.00°. At this point, it should be noted that the inner tube and the outer tube have the same chirality. Besides, the increase rate of thermal conductivity with the ITCA is larger at a lower temperature. At the temperature of 200 K, the thermal conductivity increases from 885.7 $W•m^{-1}•K^{-1}$ to 942.9 $W•m^{-1}•K^{-1}$, increased by 6.46%, as the ITCA increases from 0.00° to 30.00°. While at the temperature of 600 K, the thermal conductivity increased by 3.63%.

Above all, it can be seen that the thermal conductivity of twisted double-walled CNT is more sensitive to temperature compared to the twist angle. Furthermore, as for the double-walled BNNT, as shown in Fig. 7(b), the relationship among the chiral angle, the temperature, and the thermal conductivity share a similar regulation to that of CNT: The thermal conductivity decreases as the temperature increases. The thermal conductivity increases as the ITCA increases at a similar increase rate at different temperatures, and there's a maximum value when the chiral angle becomes 30.00°. The maximum increase rate, which is obtained at 200 K, is 5.70% as the chiral angle increases from 0.00° to 30.00°. However, the difference between the thermal conductivity of twisted BNNT and the CNT is that the overall thermal conductivity of the twisted double-walled BNNT, ranging from 25.0 $W•m^{-1}•K^{-1}$ to 59.9 $W•m^{-1}•K^{-1}$, is lower than that of twisted double-walled CNT, ranging from 462.2 $W•m^{-1}•K^{-1}$ to 942.9 $W•m^{-1}•K^{-1}$. This is because that there're two types of atoms, B and N, in the BNNT, and the two types of atoms carry a different amount of energy, resulting in the different vibrational frequencies of both atoms. The mismatch of the vibrational frequency increases the scattering center of phonons, leading to larger energy dissipation during the thermal conduction. Different from the BNNT, the CNT consists of only C atoms, and the energy dissipation is smaller.

As for the combined structures, BNNT@CNT and CNT@BNNT, the effects of the ITCA on thermal conductivity are illustrated in Fig. 8(a) and (b) respectively. From the figure, it can be seen that the thermal conduction of the combined structure is smaller than that of the double-walled CNT, and is slightly higher than that of the double-walled BNNT. This indicates that although the combined structure can improve the strength and the thermo-stability of CNT, the thermal conduction performance would be deterio-rated.

Moreover, similar to the results of CNT and BNNT, it can be seen that the thermal conductivity of the combined structures increases as the chiral angle increases. At the temperature of 200 K, as for BNNT@CNT structure as shown in Fig. 8(a), the thermal conductivity increases slightly as the ITCA increases. The thermal conductivity increases from 75.1 $W•m^{-1}•K^{-1}$ to 77.2 $W•m^{-1}•K^{-1}$, increased by 2.80% as the ITCA increases from 0.00° to 30.00°. The increase rate is smaller than that of the double-walled CNT or BNNT. A similar phenomenon can be obtained at other temperatures. Besides, as for the CNT@BNNT structure as shown in Fig. 8(b), at 200 K, the thermal conductivity increases from 69.4 $W•m^{-1}•K^{-1}$ to 73.4 $W•m^{-1}•K^{-1}$, increased by 5.76%, as the ITCA increases from 0.00° to 30.00°. Therefore, compared to BNNT@CNT, the CNT@BNNT is more sensitive to the ITCA. Particularly, a unique phenomenon can be observed for the CNT@BNNT structure. As the ITCA increases from 0.00° to 30.00°, although the thermal conductivity increases correspondingly, the maximum value is achieved when the ITCA is 23.41°, rather than 30.00° as other structures do. Thereafter, the thermal conductivity nearly remains constant when the ITCA increases from 23.41° to 30.00° In this region of ITCA, the increase rates at 200 K, 300 K, 400 K, 500 K, and 600 K are 0.19%, −0.44%, −0.71%, 0.15% and 0.26% respectively. The explanation of the results above will be discussed in Section 3.3 from the phonon point of view.

### 3.3. Phonon properties

The effects of twist angles on the thermal conductivity of nanotubes have been demonstrated above. The thermal conduction of the studied structures is dominated by phonon. Therefore, the vibrational density of state (VDOS), which can be calculated by the

![](./images/812582890608001026_12.jpg)

Fig. 9. VDOS of double-walled nanotubes. (a) Double-walled CNT. (b) Double-walled BNNT.

Fourier transform of the velocity autocorrelation function (VACF) as shown in Eqs. (10) ~ (11), was utilized to study the mechanism behind the phenomenon. All of the VDOS in this study were calculated at 200 K, and nanotubes with ITCAs of 0.00° and 30.00° were compared.

$$
VDOS(\omega)=\int_{0}^{\tau} VACF(t) e^{-2 \pi i \omega t} \mathrm{dt}
\tag{10}
$$

$$
VACF(t)=\frac{\left\langle\sum_{i} v_{i}(0) v_{i}(t)\right\rangle}{\left\langle\sum_{i} v_{i}(0) v_{i}(0)\right\rangle}
\tag{11}
$$

The VDOS of twisted double-walled CNT and BNNT can be seen in Fig. 9(a) and (b) respectively. As for the double-walled CNT, it can be seen that two main peaks are located at 23.8 THz and 50.8 THz. Therein, the highest peak locating at 50.8 THz is the G-peak of the twisted double-walled CNT, characterizing the stretching of C-C $sp^{2}$ bonds. The relative height of the two main peaks has been indicated in the figure. Compared to the twisted double-walled CNT with ITCA of 0.00°, the CNT with ITCA of 30.00° has a slightly lower G-peak; however, the peak locating at 23.8 THz is much higher. As for the CNT, the thermal conductivity is dominated by the low-frequency phonon, especially in the range of 12 ~ 30 THz [53], therefore, the higher peat at 23.8 THz leading to a higher thermal conductivity for CNT with ITCA of 30.00°.

As for the twisted double-walled BNNT, it can be found that four obvious peaks are located at 16.6 THz, 32.3 THz, 40.6 THz, and 48.0 THz. Similar to the double-walled CNT, the highest peak, namely G-peak of the BNNT, located at 48.0 THz. Moreover, it's obvious that there's a gap in the range of 30 ~ 40 THz, and the gap results in the phonon scattering during the thermal conduction. That's why the thermal conductivity of BNNT is much less than that of CNT. Furthermore, compared to the BNNT with ITCA of 0.00°, although the peak located at 16.6 THz of BNNT with ITCA of 30.00° is slightly lower, the peaks locating at 40.6 THz and 48.0 THz are higher. The overall effect makes the thermal conductivity of BNNT with ITCA of 30.00° higher than that of BNNT with ITCA of 0.00° slightly.

![](./images/812582890608001026_13.jpg)

Fig. 10. VDOS of the combined structures. (a) BNNT@CNT and (b) CNT@BNNT.

The VDOS of the BNNT@CNT and CNT@BNNT can be seen in Fig. 10(a) and (b) respectively. As for the twisted BNNT@CNT, it

![](./images/812582890608001026_14.jpg)

Fig. 11. Changes of thermal conductivity with twist angles for bilayer graphene [34] and double-walled CNT.

can be seen that: Firstly, there're two main peaks at 48.3 THz and 50.7 THz, and these two peaks are G-peaks of BNNT and CNT respectively. When the ITCA is 0.00°, these two peaks have the same amplitude approximately. However, when the ITCA increases to 30.00°, the amplitude of the BNNT is slightly higher than that of CNT. This indicates that the BNNT carries more energy than CNT. Then, compared to Fig. 9(b), the gap in the range of 30 ~ 40 THz is filled, thus the thermal conductivity of the BNNT@CNT is higher than that of BNNT. Thirdly, compared to BNNT@CNT with ITCA of 0.00°, the BNNT@CNT with ITCA of 30.00° has a higher peak at 48.3 THz. Moreover, there're also some other peaks in the range of 10 ~ 40 THz, but the BNNT@CNT with ITCA of 0.00° doesn't. Therefore, the thermal conductivity of the BNNT@CNT with ITCA of 30.00° has a higher thermal conductivity.

As for the VDOS of CNT@BNNT, firstly, similar to that of BNNT@CNT, there're two main peaks, which can be considered as G-peaks of BNNT and CNT, located at 48.3 THz and 50.7 THz respectively. However, in the CNT@BNNT structure, the G-peak of BNNT is significantly higher than that of CNT, no matter the ITCA is 0.00° or 30.00°. Then, the obvious difference of VDOS between the CNT@BNNT with ITCAs of 0.00° and 30.00° can be found in the peak located at ~40 THz. The obvious higher amplitude results in a larger thermal conductivity of CNT@BNNT with ITCA of 30.00°.

## 4. Discussions

In our previous work[43], effects of the interlayer twist angle on thermal conductivity of multilayer graphene were investigated, and the comparison between the twisted bilayer graphene and the twisted double-walled CNT was conducted in this section. The comparison can be seen in Fig. 11, for convenience, all of the temperatures as shown in Fig. 11 is 200 K. Moreover, because the twist angle defined in the multilayer graphene is the chiral angle difference between the twisted layer and the base layer. Thus the twist angle of the twisted double-walled CNT is defined in the same way: it is defined as the difference between chiral angles between the inner tube and the outer tube as shown in Eq. (12). Where $\theta_{twist}$ is the twist angle of the double-walled CNT, and $\theta_{outer}$ is the chiral angle of the outer tube. From the comparison, it can be seen that: firstly, the thermal conductivity of the bilayergraphene is significantly lower than that of the double-walled CNT. Particularly, the thermal conductivity of the bilayer graphene is 36.72% lower than that of the double-walled CNT when the twist angle is 0.00°. This is because that the curling of the graphene has a better symmetry, and the number of edges is reduced, which decreases the scattering center of phonons.

$$\theta_{\text{twist}}=\theta_{\text{outer}}-\text{ITCA}=30^{\circ}-\text{ITCA} \tag{12}$$

Secondly, the thermal conductivity of the bilayer graphene decreases firstly as the twist angle increase from 0.00° to about 15.00°and then increases as the twist angle increases from about 15.00° to 30.00°. Nevertheless, as for the double-walled CNT, the thermal conductivity decreases monotonically in the range of 0.00°~ 30.00°. The explanation can be assumed that the CNT (whose point group is $D_{nh}$) has a higher symmetry than graphene (whose point group is $D_{6h}$), and the high symmetry makes the thermal conductivity less sensitive to the twist angle. Specially, we can assume that the thermal conductivity of the fullerene (whose point group is $T_d$) would not be affected by the twist angles anymore. However, at the present stage, there's only a qualitative explanation and the mechanism should be further studied in future work.

## 5. Conclusion

In this work, effects of the interlayer twist angle on thermal conductivity of double-walled CNT, BNNT, BNNT@CNT, and CNT@BNNT were studies utilizing NEMD, and the underlying mechanism was analyzed with the help of VDOS from the phonon aspect. The results were also compared with the results of twisted multilayer graphene. Some conclusions can be summarized as the following:

(1) Compared to the length of nanotubes and the temperature, the interlayer twist angle of double-walled nanotubes has a smaller impact on the thermal conductivity. The thermal conductivity increases as the length of the nanotube increases, with a decreasing increase rate. Besides, the thermal conductivity decreases as the temperature increases with a decreasing decrease rate.

(2) For all of the studied nanotubes, including CNT, BNNT, BNNT@CNT, and CNT@BNNT, the thermal conductivity increases as the ITCA increases, and the thermal conductivity can reach a maximum value when the ITCA is 30.00°. Especially, as for CNT@BNNT, the maximum value can be reached when the ITCA is 23.41°, and the increment is negligible as the ITCA further increases to 30.00°. Among all of the studied cases, as the ITCA increases from 0.00° to 30.00°, the maximum relative increment is 6.46%, which is obtained from double-walled CNT structures at 200 K.

(3) The effects of interlayer twist angle on thermal conductivity of the double-walled nanotubes are different from that of multi-layered graphene. The overall thermal conductivity of the nanotubes is significantly higher than that of graphene and there's no maximum or minimum value. This may be caused by the high symmetry of the nanotube.

## Declaration of Competing Interest

The authors declared that there is no conflict of interest.

## Acknowledgement

The work is supported by the **National Key Research and Development Plan** (Grant No. 2018YFB0905103). In addition, the financial support from the **China Scholarship Council** (CSC, Grant No. 201906250021) to the first author is gratefully acknowledged.

## References

[1] G. Hills, C. Lau, A. Wright, S. Fuller, M.D. Bishop, T. Srimani, P. Kanhaiya, R. Ho, A. Amer, Y. Stein, D. Murphy, Arvind Chandrakasan A., M.M. Shulaker, Modern microprocessor built from complementary carbon nanotube transistors, Nature 572 (7771) (2019) 595-602.

[2] J.R. Lukes, H. Zhong, Thermal Conductivity of Individual Single-Wall Carbon Nanotubes, J. Heat Transfer 129 (6) (2007) 705-716.

[3] E. Oyarzua, J.H. Walther, C.M. Megaridis, P. Koumoutsakos, H.A. Zambrano, Carbon Nanotubes as Thermally Induced Water Pumps, ACS Nano 11 (10) (2017) 9997-10002.

[4] S. De, N.R. Aluru, Energy Dissipation in Fluid Coupled Nanoresonators: the Effect of Phonon-Fluid Coupling, ACS Nano 12 (1) (2018) 368-377.

[5] X. Nie, L. Zhao, S. Deng, X. Chen, Y. Zhang, Z. Du, Separation of binary organic mixture in T-shaped carbon nanotube separator: insights from molecular dynamics simulation, J. Mol. Liq. 312 (2020) 113371.

[6] X. Nie, L. Zhao, S. Deng, X. Chen, Y. Zhang, Understanding transport and separation of organic mixed working fluids in T-junction from multi-scale insights: literature review and case study, Int. J. Heat Mass Transf. 154 (2020) 119702.

[7] S.C. Tsang, P.J.F. Harris, M.L.H. Green, Thinning and opening of carbon nanotubes by oxidation using carbon dioxide, Nature 362 (6420) (1993) 520-522.

[8] T. Li, Z. Tang, Z. Huang, J. Yu, A comparison between the mechanical and thermal properties of single-walled carbon nanotubes and boron nitride nanotubes, Physica E Low-dimensional Syst. Nanostruct. 85 (2017) 137-142.

[9] T. He, T. Li, Z. Huang, Z. Tang, X. Guan, Mechanical and thermal properties of the coaxial carbon nanotube@boron nitride nanotube composite, Physica E Low-dimensional Syst. Nanostruct. 107 (2019) 182-186.

[10] J. Yuan, K.M. Liew, Structural stability of a coaxial carbon nanotube inside a boron-nitride nanotube, Carbon 49 (2) (2011) 677-683.

[11] K.M. Liew, J. Yuan, High-temperature thermal stability and axial compressive properties of a coaxial carbon nanotube inside a boron nitride nanotube, Nanotechnology 22 (8) (2011) 085701.

[12] B. Kumanek, D. Janas, Thermal conductivity of carbon nanotube networks: a review, J. Mater. Sci. 54 (10) (2019) 7397-7427.

[13] L. Qiu, N. Zhu, H. Zou, Y. Feng, X. Zhang, D. Tang, Advances in thermal transport properties at nanoscale in China, Int. J. Heat Mass Transf. 125 (2018) 413-433.

[14] P. Kim, L. Shi, A. Majumdar, P.L. McEuen, Thermal transport measurements of individual multiwalled nanotubes, Phys. Rev. Lett. 87 (21) (2001) 215502.

[15] T.Y. Choi, D. Poulikakos, J. Tharian, U. Senhausser, Measurement of thermal conductivity of individual multiwalled carbon nanotubes by the 3-$\omega$ method, Appl. Phys. Lett. 87 (1) (2005) 013108.

[16] X.J. Hu, A.A. Padilla, J. Xu, T.S. Fisher, K.E. Goodson, 3-Omega Measurements of Vertically Oriented Carbon Nanotubes on Silicon, J. Heat Transfer 128 (11) (2006) 1109-1113.

[17] L. Qiu, K. Scheider, S.A. Radwan, L.S. Larkin, C.B. Saltonstall, Y. Feng, X. Zhang, P.M. Norris, Thermal transport barrier in carbon nanotube array nano-thermal interface materials, Carbon N Y 120 (2017) 128-136.

[18] L. Qiu, X. Wang, G. Su, D. Tang, X. Zheng, J. Zhu, Z. Wang, P.M. Norris, P.D. Bradford, Y. Zhu, Remarkably enhanced thermal transport based on a flexible horizontally-aligned carbon nanotube array film, Sci. Rep. 6 (2016) 21014.

[19] C.-H. Wang, Y.-Y. Feng, K. Yue, X.-X. Zhang, Discontinuous finite element method for combined radiation-conduction heat transfer in participating media, Int. Commun. Heat Mass Transf. (2019) 108 104287.

[20] D.L. Nika, E.P. Pokatilov, A.S. Askerov, A.A. Balandin, Phonon thermal conduction in graphene: role of Umklapp and edge roughness scattering, Phys. Rev. B 79 (15) (2009) 155413.

[21] J.H. Seol, I. Jo, A.L. Moore, L. Lindsay, Z.H. Aitken, M.T. Pettes, X. Li, Z. Yao, R. Huang, D. Broido, N. Mingo, R.S. Ruoff, L. Shi, Two-dimensional phonon transport in supported graphene, Science 328 (5975) (2010) 213-216.

[22] J.-W. Jiang, B.-S. Wang, J.-S. Wang, First principle study of the thermal conductance in graphene nanoribbon with vacancy and substitutional silicon defects, Appl. Phys. Lett. 98 (11) (2011) 113114.

[23] C.-H. Wang, Y.-Y. Feng, Y.-H. Yang, Y. Zhang, K. Yue, X.-X. Zhang, Chebyshev collocation spectral method for vector radiative transfer equation and its applications in two-layered media, J. Quant. Spectros. Radiat. Transf. 243 (2020) 106822.

[24] C. Diao, Y. Dong, J. Lin, Reactive force field simulation on thermal conductivities of carbon nanotubes and graphene, Int. J. Heat Mass Transf. 112 (2017) 903-912.

[25] L. Cui, Y. Feng, X. Zhang, Dependence of Thermal Conductivity of Carbon Nanopeapods on Filling Ratios of Fullerene Molecules, J. Phys. Chem. A 119 (45) (2015) 11226-11232.

[26] X. Yang, D. Chen, Z. Han, X. Ma, A.C. To, Effects of welding on thermal conductivity of randomly oriented carbon nanotube networks, Int. J. Heat Mass Transf. 70 (2014) 803-810.

[27] R.N. Salaway, L.V. Zhigilei, Molecular dynamics simulations of thermal conductivity of carbon nanotubes: resolving the effects of computational parameters, Int. J. Heat Mass Transf. 70 (2014) 954-964.

[28] R.A. Shelly, K. Toprak, Y. Bayazitoglu, Nose-Hoover thermostat length effect on thermal conductivity of single wall carbon nanotubes, Int. J. Heat Mass Transf. 53 (25-26) (2010) 5884-5887.

[29] Z. Xu, M.J. Buehler, Strain controlled thermomutability of single-walled carbon nanotubes, Nanotechnology 20 (18) (2009) 185701.

[30] C.W. Padgett, D.W. Brenner, Influence of chemisorption on the thermal conductivity of single-wall carbon nanotubes, Nano Lett. 4 (6) (2004) 1051-1053.

[31] M. Khalkhali, F. Khoeini, A. Rajabbour, Thermal transport in silicene nanotubes: effects of length, grain boundary and strain, Int. J. Heat Mass Transf. 134 (2019) 503-510.

[32] J.-W. Jiang, J.-S. Wang, Theoretical study of thermal conductivity in single-walled boron nitride nanotubes, Phys. Rev. B 84 (8) (2011) 085439.

[33] J.H. Lehman, M. Terrones, E. Mansfield, K.E. Hurst, V. Meunier, Evaluating the characteristics of multiwall carbon nanotubes, Carbon 49 (8) (2011) 2581-2602.

[34] S. Iijima, Helical microtubules of graphitic carbon, Nature 354 (1991) 56-58.

[35] Y. Cao, V. Fatemi, S. Fang, K. Watanabe, T. Taniguchi, E. Kaxiras, P. Jarillo-Herrero, Unconventional superconductivity in magic-angle graphene superlattices, Nature 556 (7699) (2018) 43-50.

[36] Y. Cao, V. Fatemi, A. Demir, S. Fang, S.L. Tomarken, J.Y. Luo, J.D. Sanchez-Yamagishi, K. Watanabe, T. Taniguchi, E. Kaxiras, R.C. Ashoori, P. Jarillo-Herrero, Correlated insulator behaviour at half-filling in magic-angle graphene superlattices, Nature 556 (7699) (2018) 80-84.

[37] U. Mogera, G.U. Kulkarni, A new twist in graphene research: twisted graphene, Carbon 156 (2020) 470-487.

[38] K. Tran, G. Moody, F. Wu, X. Lu, J. Choi, K. Kim, A. Rai, D.A. Sanchez, J. Quan, A. Singh, J. Embley, A. Zepeda, M. Campbell, T. Autry, T. Taniguchi, K. Watanabe, N. Lu, S.K. Banerjee, K.L. Silverman, S. Kim, E. Tutuc, L. Yang, A.H. MacDonald, X. Li, Evidence for moire excitons in van der Waals heterostructures, Nature 567 (7746) (2019) 71-75.

[39] C. Jin, E.C. Regan, A. Yan, M. Iqbal Bakti Utama, D. Wang, S. Zhao, Y. Qin, S. Yang, Z. Zheng, S. Shi, K. Watanabe, T. Taniguchi, S. Tongay, A. Zettl, F. Wang, Observation of moire excitons in WSe2/WS2 heterostructure superlattices, Nature 567 (7746) (2019) 76-80.

[40] W. Su, Y. Hwang, S. Deng, L. Zhao, D. Zhao, Thermodynamic performance comparison of Organic Rankine Cycle between zeotropic mixtures and pure fluids under open heat source, Energy Convers. Manage. 165 (2018) 720-737.

[41] A.I. Cocemasov, D.L. Nika, A.A. Balandin, Engineering of the thermodynamic properties of bilayer graphene by atomic plane rotations: the role of the out-of-plane phonons, Nanoscale 7 (30) (2015) 12851-12859.

[42] H. Li, H. Ying, X. Chen, D.L. Nika, A.I. Cocemasov, W. Cai, A.A. Balandin, S. Chen, Thermal conductivity of twisted bilayer graphene, Nanoscale 6 (22) (2014) 13402-13408.

[43] X. Nie, L. Zhao, S. Deng, Y. Zhang, Z. Du, How interlayer twist angles affect in-plane and cross-plane thermal conduction of multilayer graphene: a non-equilibrium molecular dynamics study, Int. J. Heat Mass Transf. 137 (2019) 161-173.

[44] X. Nie, Z. Du, L. Zhao, S. Deng, Y. Zhang, Molecular dynamics study on transport properties of supercritical working fluids: literature review and case study, Appl. Energy 250 (2019) 63-80.

[45] C. Si, X.-D. Wang, Z. Fan, Z.-H. Feng, B.-Y. Cao, Impacts of potential models on calculating the thermal conductivity of graphene using non-equilibrium molecular dynamics simulations, Int. J. Heat Mass Transf. 107 (2017) 450-460.

[46] S. Plimpton, Fast parallel algorithms for short-range molecular Dynamics, J. Comput. Phys. 117 (1995) 1-19.

[47] A. Stukowski, Visualization and analysis of atomistic simulation data with OVITO-the Open Visualization Tool, Model. Simul. Mater. Sci. Eng. 18 (1) (2010) 015012.

[48] L. Lindsay, D.A. Broido, Optimized Tersoff and Brenner empirical potential parameters for lattice dynamics and phonon thermal transport in carbon nanotubes and graphene, Phys. Rev. B 81 (20) (2010) 205441.

[49] A. Kinaci, J.B. Haskins, C. Sevik, T. Çağin, Thermal conductivity of BN-C nanostructures, Phys. Rev. B 86 (11) (2012) 115410.

[50] L.A. Girifalco, M. Hodak, R.S. Lee, Carbon nanotubes, ropes buckyballs, and a universal graphitic potential, Phys. Rev. B 62 (19) (2000) 13104-13110.

[51] D. Baowan, J.M. Hill, Nested boron nitride and carbon-boron nitride nanocones, Micro Nano Lett. 2 (2) (2007) 46-49.

[52] Y. Zhang, A. Fan, M. An, W. Ma, X. Zhang, Thermal transport characteristics of supported carbon nanotube: molecular dynamics simulation and theoretical analysis, Int. J. Heat Mass Transf. 159 (2020) 120111.

[53] G. Wu, B. Li, Thermal rectification in carbon nanotube intramolecular junctions: molecular dynamics calculations, Phys. Rev. B 76 (8) (2007) 085424.
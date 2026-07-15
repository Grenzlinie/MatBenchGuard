# Ab initio molecular dynamics study on local structure and dynamic properties of liquid $\boldsymbol{Ni_{62}Nb_{38}}$ alloy

Feiyun Chen $^{a,b}$, Chengcheng Cao $^{b}$, Qiu Zhong $^{b}$, Jianjun Liu $^{c}$, Liping Yang $^{b,c,*}$, Zezhong Chen $^{a,**}$

$^{a}$ School of Materials Science and Engineering, University of Shanghai for Science and Technology, Shanghai 200093, China
$^{b}$ Inorganic Materials Analysis and Testing Center, Shanghai Institute of Ceramics, Chinese Academy of Sciences, Shanghai 200050, China
$^{c}$ State Key Laboratory of High-Performance Ceramics and Superfine Microstructure, Shanghai Institute of Ceramics, Chinese Academy of Sciences, Shanghai 200050, China

---

## ARTICLE INFO

**Keywords:**
Liquid $Ni_{62}Nb_{38}$alloy
Ab initio molecular dynamics
local structure
Short-range order
Electronic structure

## ABSTRACT

In the temperature range between 1873 K and 1233 K, structural evolution and dynamic properties of liquid $Ni_{62}Nb_{38}$ alloy have been studied by ab initio molecular dynamics. The evolution of local structure was characterized by pair distribution functions, structure factors, bond angle distributions, coordination numbers and chemical short-range order parameters, and electronic structure is mainly reflected by the density of states. Self-diffusion coefficients were calculated out to represent dynamic properties. It is found that with the decrease of temperature, short-range order tends to increase and medium-range order can be discovered in the under-cooling system. Meanwhile, a series of complex local structure like tetrahedron and icosahedron gradually forms in the liquid. Moreover, the whole system is hetero-coordinating. During the whole process, both Ni and Nb diffusion coefficients show a decreasing trend, effectively prohibiting nucleation and crystal growth, and it is beneficial to the amorphous transformation of liquid $Ni_{62}Nb_{38}$ alloy. The formation of chemical bonds between Ni and Nb atoms is mainly because of the hybridization interaction between Ni and Nb d-states.

---

## 1. Introduction

Since 1990s, researchers have found that a series of liquid alloys have extraordinary glass forming ability (GFA) which can form bulk metallic glasses (BMGs), and these bulk metallic glasses have been widely studied because of their better properties compared with conventional alloys [1–4]. Previous studies point out that bulk metallic glasses with good GFA are usually multi-component, because various kinds of atoms with quite different atomic sizes can easily hinder crystallization process of super-cooled liquid, thus contributing to amorphization [5]. However, with the research further deepened, some binary bulk metallic glasses have also been proved with outstanding GFA such as Cu-Zr [6–9], Mg-Zn [10,11] and Cu-Hf [12,13], which gives easier access to study how liquid alloys turn to amorphous state.

Originating from their peculiar atomic and electronic structure, BMGs usually exhibit outstanding performance, like excellent magnetic properties in Fe-Si-B [14] system and mechanical properties in Mg-Cu-Ga [15] system, so they are believed to have broad prospects for application. For example, there have been scalpels that are made of $Cu_{64}Zr_{36}$ metal glass in the market. In order to further develop new BGMs and optimize their performance, much effort is being devoted to understand the internal mechanism of BMGs. Recently, Xiong et al. [16] studied the structure and dynamic properties of liquid Ag-Ge alloy and unveiled that the dominant short-range order in the nearest shell promotes the development of medium-range order and the formation of metallic glasses. Shi et al. [17] studied the evolution of chemical short-range order (CSRO) in U-Nb metallic glass during solidification and found that icosahedron and bcc type clusters play an important role in the amorphization and the increase of Nb content is beneficial to the amorphous transformation.

As a kind of typical binary amorphous alloys, Ni-Nb system has attracted much attention because of its excellent GFA resulting from the high negative mixing heat between Ni and Nb, up to $-30$ kJ/mol [18]. From Leonhardt et al. [19] preparing $Ni_{59.5}Nb_{40.5}$ ribbons by

---

* Corresponding author at: Inorganic Materials Analysis and Testing Center, Shanghai Institute of Ceramics, Chinese Academy of Sciences, Shanghai 200050, China.
** Corresponding author at: School of Materials Science and Engineering, University of Shanghai for Science and Technology, Shanghai 200093, China.
E-mail addresses: lpyang@mail.sic.ac.cn (L. Yang), zzhchen@usst.edu.cn (Z. Chen).

https://doi.org/10.1016/j.mtcomm.2021.102207
Received 12 August 2020; Received in revised form 16 January 2021; Accepted 23 February 2021
Available online 28 February 2021
2352-4928/© 2021 Published by Elsevier Ltd.

melt-spinning in 1999 to recently Zhu et al. [20] manufacturing its amorphous rods with a maximum diameter of 1.5 mm, its related research hotspot mainly focuses on how to realize bigger bulk amorphous preparation, but the fact that the Ni-Nb system is a good object to study the formation mechanism of metallic glasses seems to be a little neglected. Previously, Sváb et al. used high-resolution [21] and time-of-flight neutron diffraction technologies [22] to obtain structural factors and the corresponding pair distribution functions of $Ni_{62}Nb_{38}$ and $Ni_{44}Nb_{56}$ amorphous ribbons, respectively. Reddy et al. [23] studied the contribution of Nb to GFA and plasticity of Ni-Nb metallic glass by using classical molecular dynamics (MD) with embedded atom potential, which is a kind of empirical simulations to obtain important information about the amorphous microstructure in metallic glasses, like pair distribution functions.

Whether modern investigation techniques such as synchrotron radiation and neutron diffraction, or empirical simulations based on classical MD can all give insight into metallic glasses to some extent, but their obtained results are still hard to essentially explain the formation of metallic glasses. Fortunately, the emergence of ab initio molecular dynamics (AIMD) simulations has enabled researchers to study the evolution of electronic structure during amorphization and it can provide much more specific and reliable description of local structure and chemical composition. In this paper, liquid $Ni_{62}Nb_{38}$ alloy has been studied by AIMD between 1873 K and 1233 K. Pair distribution functions, structure factors, bond angle distributions, coordination numbers and CSRO parameters are discussed during the local structural evolution. Meanwhile, along with dynamic characteristics, mean square displacement (MSD), self-diffusion equation and viscosity equation are also studied. All the results open a door to deeply understand the evolution of local structure and dynamic properties of $Ni_{62}Nb_{38}$ alloy during rapid cooling.

## 2. Computational details

Molecular dynamics simulations of liquid $Ni_{62}Nb_{38}$ alloy were performed using Vienna Ab initio simulation software package (VASP) [24, 25] in a framework based on density functional theory (DFT) [26]. The interaction between electrons and ions was investigated by the method of Projector Augmented-Wave (PAW) [27]. Electronic exchange and mutuality were described by general gradient approximation (GGA) [28] in the form of Pedrew-Burke-Ernzerhof (PBE). The valence electron numbers of Ni and Nb are 10 and 13, respectively. The plane wave cut-off energy was set as 294 eV. The entire MD calculation process was performed in an NVT ensemble with a Nosé-Hoover thermostat [29]. Verlet algorithm was used to integrate Newton's motion equation, and the time step was set to 3 fs. Only the $\Gamma$ point was applied to the Brillouin zone of the supercell for sampling.

The original configuration in all the simulations is a cubic supercell composed of 100 atoms (62 Ni atoms and 38 Nb atoms) with a random distribution and periodic boundary conditions. In order to obtain the equilibrium liquid state, the $Ni_{62}Nb_{38}$ supercell was heated to 2500 K and kept melted in 5000 MD steps, much higher than its melting temperature (Tm ≈ 1457 K), which can completely eliminate the memory effect. The energy of the system as a function of time is shown in Fig. 1 (a), and it indicates that the 5000 MD step running has established a robust thermal equilibrium within the supercell. Subsequently, with the cooling rate of $6.976 × 10^{13}$ K/s, the melt was cooled to each temperature point from 2500 K. Fig. 1(b) shows the density of the system at different temperatures as a reference, which was calculated by adjusting the side length of the cube to make the external pressure of the supercell fluctuate near zero. After it was cooled to the interest temperature, the supercells run another 5000 ion steps to make the system reach complete equilibrium. Finally, another 3000 steps were run to analyze the structure and dynamic characteristics of $Ni_{62}Nb_{38}$ liquid alloy.

Electronic structural calculation adopted $1 × 1 × 1$ k-mesh, and the plane wave cut-off energy was set as 400 eV according to convergence test. Finally, Pair distribution functions, structural factors, bond angle distributions, coordination numbers and CSRO parameters were obtained to analyze the atomic configuration.

## 3. Results and discussions

### 3.1. PDFs and SFs

The short-range structure and atomic order of liquid Ni-Nb alloy can be well described by the distribution function, calculated by the following formula:

$$
g(r)=1+\frac{1}{4 \pi r \rho_{0}}\left[\frac{2}{\pi} \int_{0}^{\infty} q[S(q)-1] \sin (q r) d q\right] \tag{1}
$$

Where $\rho_{0}$ is the average atomic density.

The partial pair-distribution function $g_{ij}(r)$ between $i$ and $j$ atom types can be expressed as,

$$
g_{i j}(r)=\frac{V}{N_{i} N_{j}}<\sum_{i=1}^{N_{i}} \frac{n_{i j}(r, \Delta r)}{4 \pi r^{2} \Delta r}>\tag{2}
$$

![](./images/812495248415522817_1.jpg)

Fig. 1. (a) The energy of liquid $Ni_{62}Nb_{38}$ alloy as a function of time during the AIMD simulations. (b) the computational density of liquid $Ni_{62}Nb_{38}$ alloy as a function of temperature.

where $V$ is the supercell volume, $i$ and $j$ represent the central and coordination atoms, respectively, $N_i$ and $N_j$ are their respective number, and $\mathrm{n}_{i j}(r, \Delta r)$ is the number of $j$ atoms in the sphere shell from $r$ to $r+\Delta r$.

Fig. 2 shows $g(r)$ curves obtained from AIMD calculation of $\mathrm{Ni}_{62} \mathrm{Nb}_{38}$ alloy at 1473 K, compared with those obtained from MD simulation with the developed FS potential at T = 1447 K [30]. There is only a little difference between them that results from the slight temperature variation, and their good consistence indicates that the calculation method in this study is efficient and accurate.

Fig. 3 shows total and partial distribution functions of liquid $\mathrm{Ni}_{62} \mathrm{Nb}_{38}$ alloy at different temperatures. As shown in Fig. 3(a), there appear typical curves similar to that of liquid in all the total pair distribution functions where the first and second peaks are located at 2.52 $\pm 0.02$ Å and $4.58 \pm 0.08$ Å, respectively. It is clear that both the peak heights gradually increase with the temperature decreasing from 1873 K to 1233 K. Also, there is a split trend for the second peak at 1403 K and 1233 K in Fig. 3(a), and this phenomenon can be more easily recognized at the same temperatures for Ni-Ni partial pair distribution function in Fig. 3(b). The height increase and peak split can both manifest the continuous evolution of local structure, and the former indicates the enhancement of short-range order during cooling, while the later indicates that short-range order gradually assembles together and forms local clusters, contributing to the appearance of medium range order in liquid $\mathrm{Ni}_{62} \mathrm{Nb}_{38}$ alloy [16]. In general, the internal atoms tend to re-arrange and local structure becomes more and more ordered, usually described as the increase in the degree of local order. In addition, the first peak positions in Fig. 3(d) are larger than those in Fig. 3(b), mainly because the atomic radius of Nb is bigger than that of Ni. Under 1403 K, the interval between the first and second peaks is smaller in Fig. 3(d) than in the other figures, which points out the existence of Nb-Nb medium-range order.

In order to further understand the local atomic structure of liquid Ni-Nb alloy, total and partial structural factors were also analyzed. The total structure factor $S(q)$ can be calculated out from the three partial structure factors $S_{i j}(q)$, atomic concentration of the elements $c_i$ and $c_j$, and the scattering factors $f_i$ and $f_j$ in the alloys:

$$
S(q)-1=\frac{c_{i}^{2} f_{i}^{2}\left(S_{i j}-1\right)+2 c_{i} c_{j} f_{i} f_{j}\left(S_{i j}-1\right)+c_{j}^{2} f_{j}^{2}\left(S_{i j}-1\right)}{\left(c_{i} f_{i}+c_{j} f_{j}\right)^{2}} \tag{3}
$$

The scattering factors $f_i$ and $f_j$ are obtained from the tabulated data [31]. The Faber-Ziman partial structural factor $S_{i j}(q)$ [16] can be obtained by Fourier transform function:

$$
S_{i j}(q)=1+4 \pi \rho_{i j} \int_{0}^{\infty} r^{2} \frac{\sin q r}{q r}\left[g_{i j}(r)-1\right] d r \tag{4}
$$

Where $g_{i j}(r)$ can be calculated by Eq. (2). Total and partial structural factors of liquid $\mathrm{Ni}_{62} \mathrm{Nb}_{38}$ alloy at different temperatures are shown in Fig. 4. As the temperature drops from 1873 K to 1233 K, the intensity of the first peak at $2.95 \pm 0.02 \AA^{-1}$ increases, which indicates the occurrence of local atoms that arrange orderly. As indicated from Fig. 4(b) and (d), both the curves of Ni-Ni and Nb-Nb partial structural factors show a peak at $1.82 \pm 0.02 \AA^{-1}$, but their location corresponds to a minimum value in the curve of Ni-Nb partial structural factor. Therefore, there is only a small pre-peak at $\sim 1.80 \AA^{-1}$ in Fig. 4(a), and the pre-peak becomes more and more intensive with the decrease of temperature. It is noteworthy that at 1473 K, a small peak appears between the first and second peaks, and the second peak slightly splits in Fig. 4(a)-(c), which means that short range order has significantly increased and medium range order has already formed when the $\mathrm{Ni}_{62} \mathrm{Nb}_{38}$ melt cooled to this state [32].

From F-Z partial structure factors, Bhatia-Thornton (BT) static structure factor can be computed by the following parameters [33]: autocorrelation function of the number density $S_{N N}(q)$, component wave autocorrelation function $S_{C C}(q)$, or correlation function between number density and component fluctuation $S_{N C}(q)$, and their respective equation can be expressed as

$$
S_{N N}(q)=x_{1} S_{11}(q)+x_{2} S_{22}(q)+2\left(x_{1} x_{2}\right)^{1 / 2} S_{12}(q) \tag{5}
$$

$$
S_{C C}(q)=x_{1} x_{2}\left[x_{2} S_{11}(q)+x_{1} S_{22}(q)-2\left(x_{1} x_{2}\right)^{\frac{1}{2}} S_{12}(q)\right] \tag{6}
$$

$$
S_{N C}(q)=x_{1} x_{2}\left[S_{11}(q)-S_{22}(q)+2\left(x_{2}-x_{1}\right) S_{12}(q) \bigg/ \left(x_{1} x_{2}\right)^{\frac{1}{2}}\right] \tag{7}
$$

$S_{C C}(q)$ describes the relative arrangement of different species. $x_1$ and $x_2$ represent the percentage of $\mathrm{Ni}$ and $\mathrm{Nb}$ atoms in the total number of atoms, respectively. Generally, $S_{C C}(q \rightarrow 0)$ equals to $x_{1} x_{2}$ for an ideal alloy at large distances, and $S_{C C}(q \rightarrow 0)$ is much larger than $x_{1} x_{2}$ for homo-coordinating systems, but $S_{C C}(q \rightarrow 0)$ is smaller than $x_{1} x_{2}$ for hetero-coordinating systems.

Fig. 5 shows the B-T static structure factors at 1233 K. The $S_{N N}(q)$ curve has a sharp first peak, which means there exist a large number of short-range ordered structures in the system. There is a main peak of $S_{C C}$ (q) at 1.92 Å, indicating a strong chemical order in the system, and this peak position corresponds to that of the pre-peak in the total structure factor. In addition, $S_{C C}(q \rightarrow 0)<x_{1} x_{2}$ illustrates that the alloy inside tends to form pairs consisting of different atoms, namely hetero-coordination.

![](./images/812495248415522817_2.jpg)

Fig. 2. Partial pair distribution functions of liquid $\mathrm{Ni}_{62} \mathrm{Nb}_{38}$ alloy obtained from the AIMD simulation at $\mathrm{T}=1473 \mathrm{~K}$ and MD simulation at $\mathrm{T}=1447 \mathrm{~K}$.

### 3.2. Bond angle distribution

In order to further elucidate local structural change of liquid $\mathrm{Ni}_{62} \mathrm{Nb}_{38}$ alloy during cooling, Ni-Ni-Ni, Ni-Ni-Nb, Nb-Nb-Nb, Nb-Ni-Nb, Nb-Nb-Ni and Ni-Nb-Ni bond angle distributions at different temperatures have been characterized as shown in Fig. 6. The cutoff distance was selected with the first minimum value of the total pair distribution function in Fig. 2(a). Both Ni-Ni-Ni and Ni-Nb-Nb partial bond angle distributions in Fig. 6(a) and (b) have two main peaks at $\sim 55^{\circ}$ and $\sim 110^{\circ}$, both of which become sharper as the temperature decreases, indicating an increase in the degree of order [17]. Meanwhile, at 1233 K, the main two peaks shift to right with about $2^{\circ}$. It should be noted that the bond angle of bcc structure is likely to be $53^{\circ}$, while the bond angles of $f c c$, $h c p$ and icosahedral structure are usually more than $60^{\circ}$. Thus, the gradual shifting of the peak to around $55^{\circ}$ is attributed to the formation of $f c c$, $h c p$ and icosahedral short-range-order in the

![](./images/812495248415522817_3.jpg)

Fig. 3. Total and partial pair distribution functions of $Ni_{62}Nb_{38}$ liquid at different temperatures. (a) $g_{total}(r)$, (b) $g_{Ni-Ni}(r)$, (c) $g_{Ni-Nb}(r)$ and (d) $g_{Nb-Nb}(r)$.

![](./images/812495248415522817_4.jpg)

Fig. 4. Total and partial structural factors of liquid $Ni_{62}Nb_{38}$ alloy at different temperatures. (a) $S_{total}(q)$, (b) $S_{Ni-Ni}(q)$, (c) $S_{Ni-Nb}(q)$ and (d) $S_{Nb-Nb}(q)$.

![](./images/812495248415522817_5.jpg)

Fig. 5. B-T static structure factors at 1233 K of liquid $Ni_{62}Nb_{38}$ alloy.

cooling process, which is faster than that of bcc short-range order [16]. However, the peak at $110^{\circ}$ shifts nondirectionally, since the bond angle distribution of bcc and other structures are similar in the vicinity of $110^{\circ}$. For Nb-Ni-Nb partial bond angle distribution in Fig. 6(c), the main peaks are located at around $63^{\circ}$ and $115^{\circ}$, corresponding to the characteristic peak of standard icosahedron-symmetric structure [34]. In Fig. 6(e) and (f), there are two main peaks in Nb-Nb-Ni and Ni-Nb-Ni partial bond angle distributions that are located at $\sim50^{\circ}$ and $\sim100^{\circ}$, relatively more left than the main peaks in the other four figures, implying the existence of distorted icosahedral geometries in $Ni_{62}Nb_{38}$ system [35]. In general, there appears a flat plane at $\sim150^{\circ}$ with the temperature under 1403 K in all the partial bond angle distributions in Fig. 3, which suggests that tetrahedron and some other complex polyhedron are likely to form and further contribute to the degree of local order increasing [36,37].

### 3.3. Coordination number and chemical short-range order

Coordination numbers in liquid $Ni_{62}Nb_{38}$ alloy vs temperature are shown in Fig. 7. Its calculation is based on the pair distribution functions in Fig. 2(a) where the minimum value between the first and second peaks determines the cutoff distance. Generally, the total and partial coordination numbers almost have no change with the decrease of temperature, which indicates that the order of the first nearest-neighbor keeps stable when the overheated $Ni_{62}Nb_{38}$ melt translates to the undercool state. Also, the total nearest neighbor coordination number around Nb is always larger than that around Ni, due to the difference of atomic size and chemical properties. It is noted that the Nb-Ni coordination number is $\sim9.23$ at 1233 K, relatively larger than that of Ni-Ni whose value equals to 6.22, which indicates that Ni atoms tend to gather in the shell of Nb centered clusters, leading to the formation of medium-range-order. Meanwhile, each Ni atom has 6.2 Ni and 5.7 Nb coordinating atoms, and each Nb atom has 9.2 Ni and 4.8 Nb coordinating atoms, which means the average chemical components for Ni and Nb center clusters are $Ni_{7.2}Nb_{5.7}$ (close to $Ni_{7}Nb_{6}$) and $Nb_{5.8}Ni_{9.2}$, respectively. This is well consistent with the results of the "cluster-plus-glue-atom" model [38]. Besides, Nb-Nb coordination number is very small, mainly caused by the fact that the number of Nb atoms is much less than that of Ni atoms in the AIMD calculation. In order to explore atomic arrangement and specific clusters in the liquid, Warren-Cowley CSRO parameter $(\alpha_{ij})$ is used to estimate CSRO in the first coordination shell of Ni and Nb atoms, which is defined as [39,40]:

![](./images/812495248415522817_6.jpg)

Fig. 6. Bond angle distributions in liquid $Ni_{62}Nb_{38}$ alloy at various temperatures. (a) Ni-Ni-Ni, (b) Ni-Ni-Nb, (c) Nb-Ni-Nb, (d) Nb-Nb-Nb, (e) Nb-Nb-Ni, (f) Ni-Nb-Ni.

![](./images/812495248415522817_7.jpg)

Fig. 7. Total and partial coordination numbers in liquid $Ni_{62}Nb_{38}$ alloy at different temperatures.

$$
\alpha_{ij}=1-N_{ij}/(c_{j}N_{tot}) \tag{8}
$$

Where $N_{ij}$ is the coordination number of $j$ atoms around $i$ atoms, $c_j$ is the fraction of $j$ atoms, and $N_{tot}$ is the total coordination number. The relationship between CSRO parameter and temperature is shown in Fig. 8. For random arranged atoms, CSRO parameter is zero. When CSRO parameter is negative, it represents that there is an attractive force between $i$ and $j$ atoms, causing that the concentration of $j$ atoms in the first coordination shell of $i$ atoms exceeds the average concentration of $j$ atoms in the liquid. When CSRO parameter is positive, it indicates that there is a repulsive force between these two kinds of atoms. In this case, as shown in Fig. 8, Ni-Ni and Nb-Nb CSRO parameters are positive, indicating whether Ni or Nb atoms is repulsive to itself, but Ni-Nb and Nb-Ni CSRO parameters are negative, meaning that Ni and Nb atoms attract with each other. It can be concluded that when the liquid alloy turns to the supercooled state, Ni atoms tend to easily gather around Nb atoms and form Nb centered clusters, and with the degree of order increasing, these Nb clusters are likely to share Ni atoms in their neighbor sites, which is beneficial to the subsequent formation of medium range order [16].

![](./images/812495248415522817_8.jpg)

Fig. 8. CSRO parameters in liquid $Ni_{62}Nb_{38}$ alloy at different temperatures.

### 3.4. Dynamics properties
Dynamic characteristics are very important for exploring nucleation and glass transformation of liquid alloys, which can be described by mean square displacement (MSD) as a function of time:

$$
< R_{\alpha}^{2}(t) > = \frac{1}{N_{\alpha}} < \sum_{i=1}^{N_{\alpha}} |R_{i\alpha}(t+\tau)-R_{i\alpha}(\tau)|^{2} > \tag{9}
$$

Where $N_{\alpha}$ is the number of $\alpha$ atoms, $R_{i\alpha}$ is the coordination number of $i$ atoms around $\alpha$ atoms, and $\tau$ is the origin of any time. Self-diffusion coefficient $D$ is related to the slope of MSD curve, which can be deduced from Einstein's relation [41],

$$
D=\lim_{t \to \infty} < R_{i\alpha}^{2}(t) > /6t \tag{10}
$$

MSD curves and self-diffusion coefficients of liquid $Ni_{62}Nb_{38}$ alloy are shown in Fig. 9. The error bars in the plot were calculated by dividing the total 3000 MD steps into three 1000 MD steps. It can be seen in Fig. 9(a) that whether total or Ni and Nb partial MSD curves at different temperatures show a clear linear dependence on time, representing that configuration at each temperature point achieves equilibrium in the AIMD calculation. As indicated by Fig. 9(b), when the temperature decreases, Ni diffusion coefficient decreases from $0.237 \times 10^{-4}\ \text{cm}^2/\text{s}$ to $0.023 \times 10^{-4}\ \text{cm}^2/\text{s}$, and Nb diffusion coefficient drops from $0.195 \times 10^{-4}\ \text{cm}^2/\text{s}$ to $0.021 \times 10^{-4}\ \text{cm}^2/\text{s}$. In addition, the total diffusion coefficient also shows a decreasing trend, probably caused by the increase of icosahedral short-range order during the cooling, which has been proved to be able to slow down the liquid and facilitate the formation of glass [40,42].

### 3.5. Density of states
In order to understand the bonding between Ni and Nb atoms, electronic structure of liquid $Ni_{62}Nb_{38}$ alloy at 1873 K and 1233 K has been analyzed, and its total and local density of states (DOS) is shown in Fig. 10. It can be found that the density of the state from the overheated state to the supercooled state is almost unchanged. There are two main peaks in both the total DOS distributions below Fermi level at -1.49 eV and -2.35 eV that are very close to the two main peaks in their respective Ni d-DOS distribution and can be well fitted out by the sum of the corresponding peaks in Ni and Nb d-DOS distributions. The heights of the two main peaks in the two Ni d-DOS distributions are much higher than the corresponding ones in Nb d-DOS distributions, so the valence band at the melt state is mainly controlled by the Ni d state, and it may be related to the larger number of d valence electrons in Ni atoms. However, Nb atoms have more influence on the conduction band above Fermi level compared with Ni atoms. In Fig. 10, Fermi energy levels of the entire system at 1873 K and 1233 K lie at the edge of Ni d-band but in the middle of Nb d-band. In other words, the whole electronic properties of liquid $Ni_{62}Nb_{38}$ alloy are mainly determined by $d$ electrons of Ni and Nb atoms. At the same time, it can be found that Ni and Nb $s$-states are mainly located at the bottom of the valence band, so their contribution to the electronic properties is tiny. Therefore, the existence of Ni-Nb chemical bonds in the $Ni_{62}Nb_{38}$ melt is mainly because of the hybridization interaction between Ni and Nb $d$-states, and Ni $s$-, Ni $p$-, Nb $s$- and Nb $p$- states have little effect on the formation of chemical bonds and electronic properties.

## 4. Conclusions
AIMD calculation has been carried out to simulate the amorphization of liquid $Ni_{62}Nb_{38}$ alloy. The results including pair distribution functions, structure factors, coordination numbers, CSRO parameters and bond angle distributions give deep insight into the evolution of local structure of liquid $Ni_{62}Nb_{38}$ alloy during rapid cooling. In this process,

![](./images/812495248415522817_9.jpg)

Fig. 9. (a) Total and partial mean square displacements at various temperatures versus time, and (b) total, Ni- and Nb- self-diffusion coefficients versus temperature in liquid $Ni_{62}Nb_{38}$ alloy.

![](./images/812495248415522817_10.jpg)

Fig. 10. Total and partial density of states of $Ni_{62}Nb_{38}$ liquid alloy at 1873 K and 1233 K.

local structure of liquid $Ni_{62}Nb_{38}$ alloy tends to transform from simple to complex, forming like tetrahedron and icosahedron, even Nb centered clusters with Ni atoms in the nearest shell. Therefore, the degree of order gradually increases, and there is medium range order appearing subsequently in the liquid system. Meanwhile, Ni and Nb atoms tend to form pairs in the way of hetero-coordination.

In addition, dynamic properties including diffusion coefficients in the whole cooling process have also been calculated out by AIMD. It is found that with the gradual increase of short and medium order in the liquid, both Ni and Nb atoms diffuse more slowly, greatly hindering the appearance of local constituent and structure that crystallization needs. The density of states (DOS) analysis shows that the existence of chemical bonds between Ni and Nb atoms in liquid $Ni_{62}Nb_{38}$ alloy is mainly because of the hybridization interaction between Ni and Nb d-states.

Due to the fact that the density of liquid $Ni_{62}Nb_{38}$ alloy is hard to investigated experimentally, especially over 1473 K, the lack of accurate density may result in a little deviation in the simulation, but the good consistence of the AIMD calculation results with the previous MD simulation can basically prove the accuracy and rationality of the obtained results. Therefore, this work can provide a deeper understanding of the structure of metallic liquids at the atomic scale, and unveil the formation mechanism of metallic glasses in the rapid cooling process to some extent.

## 5. Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## 6. Data availability

The raw data required to reproduce these findings cannot be shared at this time as the data also forms part of an ongoing study.

## CRediT authorship contribution statement

Feiyun Chen: Conceptualization, Methodology, Software, Formal analysis, Investigation, Data curation, Writing - original draft, Visualization. Chengcheng Cao: Supervision, Project administration, Formal analysis, Writing - review & editing. Qiu Zhong: Project administration, Funding acquisition. Jianjun Liu: Software, Funding acquisition. Liping Yang: Conceptualization, Methodology, Software, Supervision, Project administration, Funding acquisition. Zezhong Chen: Supervision, Project administration, Funding acquisition.

## Acknowledgements

This work was supported by China's Manned Space Station Project [Mission No: TGTHYY0401], Shanghai Technical Platform for testing on inorganic materials (19DZ2290700), and the National Natural Science Foundation of China (Grant No.51606209).

## References

[1] W.L. Johnson, Bulk amorphous metal-An emerging engineering material, Jom 54 (2002) 40-43.

[2] F.Q. Guo, S.J. Poon, G.J. Shiflet, CaAl-based bulk metallic glasses with high thermal stability, Appl. Phys. Lett 84 (2004) 37-39.

[3] J. Schroers, W.L. Johnson, Ductile bulk metallic glass, Phys. Rev. Lett 93 (2004), 255506.

[4] W.L. Johnson, Bulk Glass-Forming Metallic Alloys: Science and Technology, MRS Bull 24 (1998) 42-56.

[5] A.L. Greer, Metallic Glasses, Science 267 (1995) 1947-1953.

[6] D. Wang, Y. Li, B.B. Sun, Bulk metallic glass formation in the binary Cu-Zr system, Appl. Phys. Lett 84 (2004) 4029-4031.

[7] A.L. Zhang, D. Chen, Z.H. Chen, Bulk metallic glass-forming region of Cu-Zr binary and Cu-Zr based multicomponent alloy systems, J. Alloys Compd 477 (2009) 432-435.

[8] A. Foroughi, R. Tavakoli, H. Aashuri, Molecular dynamics study of structural formation in $Cu_{50}-Zr_{50}$ bulk metallic glass, J. Non-Cryst. Solids 432 (2016) 334-341.

[9] B.F. Lu, L.T. Kong, K.J. Laws, EXAFS and molecular dynamics simulation studies of Cu-Zr metallic glass: Short-to-medium range order and glass forming ability, Mater. Charact 141 (2018) 41-48.

[10] Y. Liang, Y. Zhang, B. Yu, The deformation and transformation of icosahedron in $Mg_{70}Zn_{30}$ metallic glasses, Chem. Phys. Lett 703 (2018) 39-43.

[11] A. Foroughi, R. Tavakoli, Topological and chemical short-range order and their correlation with glass form ability of Mg-Zn metallic glasses: A molecular dynamics study, Comput. Mater. Sci 180 (2020).

[12] L. Xia, K.C. Chan, S.K. Kwok, Formation of metastable phases and their effect on the glass-forming ability of Cu-Hf binary alloys, Mater. Trans 51 (2010) 68-71.

[13] I.A. Figueroa, J.D. Plummer, G.A. Lara-Rodriguez, Metallic glass formation in the binary Cu-Hf system, J. Mater. Sci. 48 (2012) 1819-1825.

[14] C. Smith, S. Katakam, S. Nag, Improved soft magnetic properties by laser devitrification of Fe-Si-B amorphous magnetic alloys, Mater. Lett 122 (2014) 155-158.

[15] R. Gao, Y.F. Zhao, X.J. Liu, Ab initio molecular dynamics simulation of the liquid and amorphous structure of $Mg_{65}Cu_{25}Gd_{10}$ alloy, Physica B: Condens. Matter. 426 (2013) 65-70.

[16] L.H. Xiong, K. Chen, F.S. Ke, Structural and dynamical properties of liquid $Ag_{74}Ge_{26}$ alloy studied by experiments and ab initio molecular dynamics simulation, Acta Mater 92 (2015) 109-116.

[17] Y. Shi, M. Liu, Y. Chen, Evolution of local atomic structure during solidification of $U_{116}Nb_{12}$ liquid: An ab initio molecular dynamics study, J. Alloys Compd 787 (2019) 267-275.

[18] F.R. de Boer, R. Boom, W.C.M. Mattens, Cohesion in Metals: Transition Metal Alloys, 1988.

[19] M. Leonhardt, W. Löser, H.G. Lindenkreuz, Solidification kinetics and phase formation of undercooled eutectic Ni-Nb melts, Acta Mater 47 (1999) 2961-2968.

[20] Z.W. Zhu, H.F. Zhang, D.G. Pan, W.S. Sun, Z.Q. Hu, Fabrication of Binary Ni-Nb Bulk Metallic Glass with High Strength and Compressive Plasticity, Adv. Eng. Mater 8 (2006) 953-957.

[21] E. Sváb, G. Mészáros, G. Konczos, Short range order in amorphous in $Ni_{62}Nb_{38}$ studied by isotopic neutron diffraction, J. Non-Cryst. Solids 104 (1988) 0-299.

[22] E. Sváb, G. Mészáros, J. Takács, Partial correlations in NiNb amorphous alloys, J. Non-Cryst. Solids 144 (1992) 99-106.

[23] K. Vijay Reddy, S. Pal, Contribution of Nb towards enhancement of glass forming ability and plasticity of Ni-Nb binary metallic glass, J. Non-Cryst. Solids 471 (2017) 243-250.

[24] G. Kresse, J. Hafner, Ab initio molecular dynamics for open-shell transition metals, Phys. Rev. B: Condens. Matter. 48 (1993) 13115-13118.

[25] G. Kresse, J. Furthmüller, Efficiency of ab-initio total energy calculations for metals and semiconductors using a plane-wave basis set, Comput. Mater. Sci 6 (1996) 15-50.

[26] J.A. Maruhn, P.G. Reinhard, E. Suraud, Density Functional Theory, Plenum Press, 2010.

[27] P.E. Blochl, Projector augmented-wave method, Phys. Rev. B: Condens. Matter. 50 (1994) 17953-17979.

[28] J.P. Perdew, K. Burke, M. Ernzerhof, Generalized Gradient Approximation Made Simple, Phys. Rev. Lett 77 (1996) 3865-3868.

[29] W.G. Hoover, Canonical dynamics: Equilibrium phase-space distributions, Phys. Rev. A 31 (1985) 1695-1697.

[30] Y. Zhang, R. Ashcraft, M.I. Mendelev, C.Z. Wang, K.F. Kelton, Experimental and molecular dynamics simulation study of structure of liquid and amorphous $Ni_{62}Nb_{38}$ alloy, J. Chem. Phys. 145 (2016), 204505.

[31] D. Waasmaier, A. Kirfel, New Analytical Scattering-Factor Functions for Free Atoms and Ions, Acta Cryst. A51 (1995) 416-431.

[32] J. Zhao, Z. Tang, K.F. Kelton, Evolution of the atomic structure of a supercooled $Zr_{55}Cu_{35}Al_{10}$ liquid, Intermetallics 82 (2017) 53-58.

[33] J.P. Boon, S. Yip, Molecular Hydrodynamics, Phys. Today 34 (1981) 92.

[34] S. Wu, M.J. Kramer, X.W. Fang, Structural and dynamical properties of liquid $Cu_{80}Si_{20}$ alloy studied experimentally and by ab initio molecular dynamics simulations, Phys. Rev. B 84 (2011).

[35] Y.R. Guo, C. Qiao, J.J. Wang, H. Shen, S.Y. Wang, Bergman-type medium range order in amorphous Zr77Rh23 alloy studied by ab initio molecular dynamics simulations, J. Alloys Compd 790 (2019) 675-682.

[36] E.A. Porai-Koshits, The Structure of Noncrystalline Materials, Annu. Rev. Mater. Sci 6 (1976) 389-409.

[37] F.S. Ke, G.Q. Yue, B. Shen, Bergman-type medium-range order in rapidly quenched $Ag_{0.74}Ge_{0.26}$ eutectic alloy studied by ab initio molecular dynamics simulation, Acta Mater 80 (2014) 498-504.

[38] H. Tian, H. Liu, C. Zhang, J. Zhao, C. Dong, B. Wen, Ab initio molecular dynamics simulation of binary $Ni_{62.5}Nb_{37.5}$ bulk metallic glass: validation of the cluster-plus-glue-atom model, J. Mater. Sci. 7 (2012) 7628-7634.

[39] A. Alam, R.K. Chouhan, A. Mookerjee, Phonon modes and vibrational entropy of disordered alloys with short-range order: A first-principles calculation, Phys. Rev. B 83 (2011).

[40] L.H. Xiong, H.B. Lou, X.D. Wang, Evolution of local atomic structure during solidification of $Al_{2}Lu$ liquid: An ab initio study, Acta Mater 68 (2014) 1-8.

[41] W.B. Zhang, X.D. Wang, Q.P. Cao, Structure and dynamical properties of liquid $Ni_{64}Zr_{36}$ and $Ni_{65}Hf_{35}$ alloys: an ab initio molecular dynamics study, J. Phys. : Condens. Matter. 30 (2018), 365401.

[42] W.K. Luo, H.W. Sheng, F.M. Alamgir, Icosahedral short-range order in amorphous alloys, Phys. Rev. Lett 92 (2004), 145502.
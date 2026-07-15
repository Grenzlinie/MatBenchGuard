# Determining phase transition using potential energy distribution and surface energy of Pd nanoparticles

Maryam Azadeh$^{a,1}$, Movaffaq Kateb$^{b}$, Pirooz Marashi$^{a,*}$

$^{a}$ Department of Mining and Metallurgical Engineering, Amirkabir University of Technology, Tehran, Iran
$^{b}$ Science Institute, University of Iceland, Dunhaga 3, IS-107 Reykjavik, Iceland

---

## ARTICLE INFO

**Keywords:**
Nanoparticle
Melting
Allotropic transition
Potential energy distribution
Surface energy

---

## ABSTRACT

Molecular dynamics simulation is employed to understand the thermodynamic behavior of cuboctahedron (cub) and icosahedron (ico) nanoparticles with 2–20 number of shells (55–28,741 atoms). The embedded atom method was used to describe the interatomic potential. Conventional melting criteria such as potential energy and specific heat capacity ($C_p$) caloric curves as well as structure analysis by radial distribution function ($G(r)$) and common neighbor analysis (CNA) were utilized simultaneously to provide a comprehensive picture of the melting process. It is shown that the potential energy distribution and surface energy ($\gamma_p$) proposed here are holding several advantages over previous criteria. In particular, potential energy distribution can distinguish between interior and surface atoms and even corner, edge and plane atoms at the surface. While $G(r)$ and CNA are not surface sensitive methods and cannot distinguish between surface melting and an allotropic transition. It is also shown that allotropic change appears more clearly in $C_p$ and $\gamma_p$ rather than potential energy. However, determining accurate $C_p$ requires enough sampling to be averaged. Finally, a few issues in the current methods for determining $\gamma_p$ were discussed and a simple method based on available models was proposed which, independent of estimation of the surface area, predicts the correct temperature and size-dependent trend in agreement with Guggenheim-Katayama and Tolman's models, respectively.

---

## 1. Introduction

Nanoparticles are known as the most unstable structures among different nanosolids due to the higher surface to volume ratio [1]. Thus, it is crucial to develop a quantitative understanding of their thermodynamic stability for practical applications specifically when the thermal instability can be considered as a failure at the elevated temperatures. For instance, it has been shown that Pd clusters might experience a solid state transition [2] below their melting temperature ($T_{mp}$) which has been misinterpreted as surface melting previously [3]. This indicates, importance of developing proper tools or methods for determine quantitatively correct values. In this regard, the main attention has been brought to Monte Carlo (MC) [4] and molecular dynamics (MD) [5,6] simulation which have proven to be an excellent tool for understanding the stability and melting behavior of nanoparticles.

Several methods are used in MD simulations to identify the melting process based on atomic specifics. The first criterion proposed by Lindemann [7], stating the melting of crystals occurs when the average amplitude of atomic vibrations, is higher than the threshold value. The global Lindemann index ($\delta_L$) is a system average of atomic quantities which shows a linear increase with the temperature increment in solid-state regime and a step change due to the melting. However, most of vibrations of the surface atoms in the small clusters, which have more degree of freedom, assumed as melting behavior by this model [8,9]. This is a serious issue since it may lead to misinterpretation of the surface melting.

We have recently shown that a combination of various criteria such as caloric curves and structure analysis is required to study the phenomenological melting of nanoparticles [2]. In this view, the advantage of a more recent structure characterization method of common neighbor analysis (CNA) over radial distribution function ($G(r)$) has been discussed. It has been shown that CNA facilitates observation of an allotropic change which could be confused with the surface melting using $G(r)$. On the other hand, CNA treats the surface atoms as a disordered structure due to the lack of symmetry at the cluster surface. While separate $G(r)$ can be defined for each cluster shell including surface atoms allowing to some extent study surface phenomena. This difference arises from the fact that $G(r)$ was originally developed to

---

* Corresponding author.
E-mail address: **pmarashi@aut.ac.ir** (P. Marashi).
$^{1}$ Present address: School of Metallurgy and Materials Engineering, University of Tehran, Iran.

https://doi.org/10.1016/j.commatsci.2019.109187
Received 18 May 2019; Received in revised form 31 July 2019; Accepted 4 August 2019
0927-0256/ © 2019 Elsevier B.V. All rights reserved.

determine number of nearest neighbors while CNA is based on bond angles between 1st nearest neighbors.

A more conventional method for determining a transition temperature is through caloric curves such as an isotherm change in the cluster potential energy ($U_p$) [10,11] or a peak in specific heat capacity ($C_p$) [12]. Unlike structure analysis, caloric curves can not provide any information on the mechanism of melting or phase transition. For instance, it has been shown that cuboctahedron (cub) clusters are melting almost uniformly by nucleation of melt at (1 0 0) planes of surface and its propagation inward, while icosahedron (ico) nanoparticles are melting diagonally starting from a corner [2]. It has also been shown that cub to ico transformation is achieved through a **transitional disordered state** which can be carefully monitored by CNA [6,2] while it only appears as a minor peak in $C_p$ or a small step change in $U_p$ which was ignored in the previous studies [12,13,3]. However, one can easily obtain the melting enthalpy of clusters ($\Delta H_{mp}$) from caloric curves.

Another important criterion is the surface energy of clusters ($\gamma_p$) which plays an important role in their phase transformation [14]. It is usually defined as the work of cutting a cluster out of the bulk material per unit area [15]. In contrast with CNA, $\gamma_p$ is very sensitive to the arrangement of surface atoms allowing to determine the melting temperature and solid state transitions. Regardless of this potential, utilizing $\gamma_p$ for detecting a phase transition is barely studied [16]. For instance, it has been shown experimentally that (1 1 0) planes melt completely with surface melting mechanism and (1 0 0) planes show partial surface melting while there is no surface melting for (1 1 1) surfaces [17]. This trend can be explained by the difference in surface energies, i.e. $\gamma_{(110)} > \gamma_{(100)} > \gamma_{(111)}$[18], which makes (1 1 1) planes more resistant against surface melting.

In the present study we demonstrate utilizing potential energy distribution and surface energy for determining solid state transition as well as melting temperature. The result are compared to conventional criteria such as caloric curves, $G(r)$ and CNA.

## 2. MD simulation

### 2.1. Simulation procedures

MD simulations were performed by solving Newton's equation of motion [19] using large-scale atomistic/molecular massively parallel simulator (LAMMPS) [20] open source code, version 22 August 2018 (available at http://lammps.sandia.gov/). The embedded atom method (EAM) [21,22] was utilized to describe the interatomic potential between Pd atoms. Eq. (1) represents the formulation of EAM potential:

$$
E_{i}=F_{i}\left[\sum_{i \neq j} \rho_{i j}\left(r_{i j}\right)\right]+\frac{1}{2} \sum_{i \neq j} U_{i j}\left(r_{i j}\right)
\tag{1}
$$

where $E_i$ and $F_i$ are cohesive and embedding energies of atom $i$, respectively. $\rho_{ij}(r_{ij})$ is the electron density of $j$ atoms located around the $i$ atom at the distance $r_{ij}$. Clearly, $F_i$ is a many body interaction term while $U_{ij}$ takes the pair interaction into account.

The EAM potential is extensively used for describing solid characteristics such as cohesive energy and elastic constant [23] as well as metals melting temperature [23,24]. Moreover, it is reliable in determining the transitional properties especially the heat of fusion and heat capacities above the room-temperature [25]. The EAM has also been verified for quantitatively correct description of such nanoscale systems namely surface energy and geometry of low index surfaces [21,26]. We have recently showed that the structure factor of molten Pd obtained by EAM potential is in close agreement to that of tight-binding and experiment [2].

The time integration of the equation of the motion was performed using the Verlet algorithm [27,28] with a timestep of 3 fs. The temperature was controlled by Nose-Hoover thermostat with damping time of 30 fs. These conditions are designed to generate positions and velocities sampled from canonical (NVT) ensemble. The initial velocities of the atoms were defined randomly from a Gaussian distribution at the 300 K and system was relaxed for 300 ps in the NVT ensemble. The melting simulations were performed by starting at 300 K, and then the temperature was elevated at a heating rate of $1.4 \times 10^{12}$ K/s.

### 2.2. Cluster preparation

The Pd nanoparticles were considered to be in the cub and ico forms as found in experimental characterizations [29]. It is worth noting that in theoretical modeling routine, several structures and apparent shapes are considered. However those structure transform to more spherical shapes, ico and cub at elevated temperature as reported previously [30]. For different sizes of given clusters, cub and ico were made based on the so called magic number ($N_t$), total number of atoms, which is described as the function of the shell number ($n$) [31]:

$$
N_{t}=\frac{1}{3}\left[10 n^{3}+15 n^{2}+11 n+3\right]
\tag{2}
$$

where $n=0$ denotes a monoatomic system and $n>1$ defines the full shell clusters.

Here, clusters with sizes below 12 nm including clusters of $n=2-20$ ($N_t=55-28,741$ atoms) were chosen.

### 2.3. Visualization

Version 2.9.0 of the open visualization tool (OVITO) package were used to generate atomistic illustrations (available at http://ovito.org/)[32].

## 3. Results and discussion

### 3.1. Relaxation

At the beginning, each nanoparticle was relaxed at room temperature as discussed in Section 2.1 to minimize the potential energy of the entire system. Fig. 1 shows the atoms coordination, before and after relaxation for 8-cub and 8-ico cluster. The perspective view clearly shows that there is no change in the shape and symmetry of the particle, indicating current EAM potential can successfully model the stable shapes of Pd nanoparticles. The exceptions were 2-cub and 4-cub cluster that present a cub to ico transformation during the relaxation. This is in agreement with the previous result using a non-dynamic minimum energy calculation [5]. It is worth mentioning that, we still call them 2-cub and 4-cub in the following.

### 3.2. Melting criteria

#### 3.2.1. Caloric curves

Fig. 2 illustrates the variation of $U$ and $C_p$ with $T$ for the 8-cub cluster (including 2057 Pd atoms) and corresponding snapshots. $U$ was determined by averaging over potential energy of entire atoms in the cluster and $C_{p}(T)=\partial\langle U_{p}angle_{T}/\partial T+\frac{3}{2}R$ with $R$ being universal gas constant [12]. The figure also contains the results of 8-ico cluster for comparison. The caloric curves present a typical melting behavior, i.e. an isotherm transition of $U$ corresponding to the main peak in the $C_p$ due to the latent heat of fusion. $T_{mp}$ equal to 1274 and 1288 K were determined using $C_p$ for the 8-cub and 8-ico clusters, respectively. In the caloric curve of 8-cub cluster, there is a step change at $\sim$1070 K corresponding to the local minimum in $C_p$. Such a behavior has been observed before however barely discussed in most cases [3,5]. For instance, Pan et al. [3] interpreted the $C_p$ minor peak as the surface melting [3]. However, they reported the surface melting for both cub and ico clusters without such a minor peak for the ico. Thus it is highly unlikely that local minimum or minor peak in $C_p$ are associated with surface melting. Apparently Zhang et al. [33] were the first who noticed

![](./images/812744168873918466_1.jpg)

Fig. 1. Atomistic view of (a) 8-cub and (b) 8-ico clusters before (a, b)1 and after (a, b)2 relaxation at 300 K, for 300 ps. Perspective view clearly shows there is no change in the symmetry and shape of clusterss.

such a step change in the caloric curve and attributed it to a solid-state transition using CNA. Utilization of heat capacity has been also de- monstrated for a more complex transition at elevated temperature in Pt- Pd alloy [34,35]. In this case, a visible change in the nanoparticle shape and number of surface atoms has been shown to be associated with the heat capacity fluctuations. Snapshots (b)1-(b)3 of Fig. 2, indicate no surface melting but slightly rounding in the corners due to surface diffusion. However, It can be clearly seen that (1 1 1) planes enclosed by triangles in (b)3 appear at the expense of vanishing (1 1 0) plane in- dicated by a square in (b)2. Snapshots (b)4 and (b)5 were taken close to the $T_{mp}$ that indicate a diagonal melting, i.e. faceted (1 1 1) planes on the top corner and rounded corner at the bottom. This incident might be associated with the partitioned structure of ico which retards the growth of the liquid phase. Finally, (b)6 snapshot shows the complete melting of the cluster.

### 3.2.2. Radial distribution function

The first and simplest structure analysis is offered by the radial distribution function, $G(r)$. It describes how the atom number density ($\rho$) varies as a function of distance from a reference atom $(r)$.

$$G(r)=4 \pi r^{2} \rho d r \tag{3}$$

where $dr$ is the bin size or thickness of the spherical shell in which number of atoms is counted.

Fig. 3 depicts the variation of $G(r)$ with $T$ for 8-cub and 8-ico clusters using $12 \AA$ cutoff and $d r=0.01 \AA$. The figure also contains $G(r)$ of a bulk sample for comparison obtained for 32,000 atoms with peri- odic boundary condition. In all cases, the $G(r)$ shows the same pattern for solid and liquid states in agreement with previously reported pat- terns [3]. The solid-state at the bottom of each figure can be interpreted from 4 main peaks indicated by dashed line corresponding to 4 shells (not to be confused with 4th nearest neighbors). The 1st shell is con- sisting of 12 equidistance atoms and thus presents a single peak while further shells contain more peaks due to their geometrical complexity. The difference between cub and ico cluster is limited to peaks at 3rd and 4th shells $(7<r<12 \AA)$. The molten state at the top of each figure consisting of 4 broad peaks. It can be clearly seen that an increase in temperature causes broadening of peaks in the both solid and molten states. The melting can be interpreted as a step change in the position of inner shells peak (1st and 2nd dashed lines on the left). A $T_{mp}$ of about 1300 K can be detected for both figures in agreement with values ob- tained from caloric curves. In addition there is a step change at about 1100 K in 3rd and 4th dashed lines of the cub cluster (cf. Fig. 3(a)). Since the step change is more evident in 4th dashed line corresponding to the 4th shell, Pan et al. [3] reported such a phenomenon as shell by shell melting. However, it is shown earlier that this step change belongs to cub to ico transformation. In the case of ico, the melting is associated with a smooth change in the peaks positions which is more evident in the 4th dashed line.

### 3.2.3. Common neighbor analysis

Recently, CNA has shown promising thanks to providing the possi- bility of distinction between allotropic transitions and melting process [2]. The CNA identifies the crystal structure of each atom based on the concept of bond-orientational order parameter developed by Steinhardt et al. [36]. Briefly, the CNA determines local crystal structure based by decomposition of $G(r)$ into different angles [37]. Thus a twining grain boundary as the main difference of ico and cub cluster can be de- termined based on a slight angle difference between pairs of 1st nearest neighbors while it has the same number of 1st nearest neighbors as an

![](./images/812744168873918466_2.jpg)

Fig. 2. (a) Variation of $U_p$ and $C_p$ with temperature for 8-cub and 8-ico clusters and (b) snapshots of 8-cub cluster corresponding to points 1-6 indicated in the (a).

fcc atom.

Fig. 4 presents the variation in the ratio of different structures obtained by CNA with temperature for 8-cub cluster. The figure also includes corresponding snapshots of the particle cross section at points 1-6 indicated with vertical dashed lines. At 300 K, cub cluster (indicated by symbols) is made of 70% fcc atoms and 30% surface atoms characterized as disordered. While ico cluster indicated by lines consists of about 30% of each fcc, hcp and surface atoms. As temperature increases, percentage of fcc and disordered atoms show a mirror change up to 1070 K. There is also a slight change in the

![](./images/812744168873918466_3.jpg)

Fig. 3. Variation of $G(r)$ with temperature for (a) 8-cub and (b) 8-ico clusters compared to that of (c) the bulk. The colorbar illustrates normalized $G(r)$ with main peaks indicated by dashed lines.

percentage of hcp atoms as can be seen in snapshots (b)1 and (b)2. However, between 2 and 3 there is 24.6% drop in fcc percentage and 19.1% increase in disordered percentage. This is followed by 8.8% drop in disordered atoms and nucleation of 9.3% hcp and 4.3% fcc atoms. As can be seen in snapshot b(3), there is higher ratio of disordered atoms at the bottom of cluster because of incomplete cub to ico transition which explains the slight difference between structure ratios of cub and ico cluster after the transition.

### 3.2.4. Potential energy distribution
A major difference between surface and interior atoms is their nearest neighbor which is reflected in the per atom potential energy. Thus it allows the study of surface related phenomena such as the surface melting more precisely. Fig. 5 illustrates the variation of the potential energy distribution with $T$ for 8-cub and 8-ico clusters with the color bar being number of atoms that possess a specific energy in the log scale. The figure also contain the result of the bulk for comparison. Unlike $G(r)$, the features of the potential energy distribution show a clear difference between clusters and the bulk. At ambient temperature, a sharp peak is evident as indicated by 1st corresponding to the interior atoms with potential energy about $E_c$ (3.935 eV/atom). There are also three minor peaks for both cub and ico with higher (more positive) potential energy which belong to surface atoms. Unlike 1st peak, the position of 2nd-4th peaks are different in cub and ico. The dark blue region between 1st and 2nd peaks indicates the lack of atoms with intermediate potential energy and the fact that dividing a cluster into interior and surface atoms is correct assumption at low temperatures. Strictly speaking, however, the surface atoms in both clusters have to be divided into plane, edge and corner atoms corresponding to the 2nd-4th minor peaks, respectively. At elevated temperatures, the potential energy distribution and major peak become broader and there are no distinguishable minor peaks for both clusters. At this stage it is very hard to divide between inner and outer atoms and even at the particle-vacuum interface potential energy changes very smoothly.

As can be seen in both cluster, there is a step change in the major peak at about 1300 K corresponding to $T_{mp}$. It can be also seen that 3rd cub peak vanishes at 1100 K while 2nd and 4th peaks showing negligible variation. One may think this is associated with the surface melting. However, it is expected that after surface melting the cluster corners disappear. While here the 4th peak indicates the existence of corners above 1100 K. Comparing the 2nd-4th cub peaks with that of ico cluster, it appears that cub cluster present the same distribution as ico above 1100 K. This indicates that cub cluster transformed into ico below $T_{mp}$. Thus, the potential energy distribution can be utilized to determine shape of the cluster as well as melting and solid state transition temperatures. However, it is necessary to compare the potential energy distribution with the structure analysis result such as CNA to understand the exact origin of such variations in the potential energy distribution.

![](./images/812744168873918466_4.jpg)

Fig. 4. (a) Variation of fcc, hcp and disordered ratio with temperature for 8-cub and 8-ico clusters. (b) Snapshots of 8-cub cross section corresponding to the dashed lines 1–6 in the (a).

### 3.2.5. Surface energy

In MD simulation, the simplest way to determine the $\gamma_p$ is based on the slab model which is mainly defined at absolute zero where ab initio and MD are in close agreement [38,39].

$$
\gamma_{p}=\frac{U_{p}-N_{t} E_{c}}{4 \pi R_{p}^{2}} \tag{4}
$$

where the $U_p$ is the total potential energy of the cluster and $E_c$ is per atom cohesive energy of the bulk system. The denominator represents

![](./images/812744168873918466_5.jpg)

Fig. 5. Variation of potential energy distribution with $T$ for (a) 8-cub and (b) 8-ico clusters in comparison with (c) the bulk. The colorbar indicates number of atoms possessing a specific energy in log scale.

the cluster surface area for a spherical cluster of radius $R_p$. The later can be determined by Guinier formula [40]:

$$
R_{p}=R_{g} \sqrt{\frac{5}{3}}+r_{a} \tag{5}
$$

$$
R_{g}=\sqrt{\frac{1}{N} \sum_{i}\left(r_{i}-r_{c m}\right)^{2}} \tag{6}
$$

where $r_a$ is atomic radius and $R_g$ stands for cluster gyration radius with $r_i$ and $r_{cm}$ respectively being coordinates of atom $i$ and particle center of mass.

$U_p$ increases with the increase in $T$ (cf. Fig. 2) and consequently Eq. (4) predicts increased $\gamma_p$ upon $T$ increment. This is in contradiction with Guggenheim-Katayama empirical formula [41]. Another statistical definition of $\gamma_p$ is based on the coordination number concept or so called broken bond model [42].

$$
\gamma_{b}=\left(1-\frac{Z_{s}}{Z_{b}}\right) \frac{E_{c}}{a_{0}} \tag{7}
$$

where $a_0$ denotes the area of the two-dimensional unit cell of the solid. Eq. (7) states that $\gamma_b$ is directly proportional to the $E_c$. Assuming this stands correct for clusters, Jiang and Lu [42] proposed the following size-dependent surface energy for the clusters.

$$
\frac{\gamma_{p}}{\gamma_{b}}=\frac{E_{p}}{E_{c}}=\left(1-\frac{1}{D / r_{a}-1}\right) \exp \left(-\frac{2 E_{c}}{3 R T_{s b}} \frac{1}{D / r_{a}-1}\right) \tag{8}
$$

with $E_p$ being cluster cohesive energy and $T_{sb}$ being the sublimation temperature of bulk material. One can adopt Eq. (8) by substituting $E_p$ with $U$:

$$
\frac{\gamma_{p}}{\gamma_{b}}=\frac{U}{E_{c}} \tag{9}
$$

The main advantage of Eq. (9) is the fact that it does not need the estimation of the cluster surface area.

The variation of $\gamma_p$ for 8-cub and 8-ico cluster with $T$ are shown in Fig. 6. It can be seen that Eq. (9) predicts the correct slop i.e. $\partial \gamma_{p} / \partial T<0$. The isotherm change in both curves indicate melting at about 1300 K. The figure inset shows the variation of $\gamma_p$ around the transitions of 8-cub cluster. The local minimum due to cub to ico transition can be clearly seen in the figure inset. We would like to remark that the slop of the curve $(\partial \gamma_{p} / \partial T)$ remains the same before and after such a transition. However, ico structure is the most compact one and consequently presents smaller surface area and higher $\gamma_p$. Thus cub to ico transition appears as a jump in $\gamma_p$ while melting is associated with an expansion resulting in a drop in $\gamma_p$.

![](./images/812744168873918466_6.jpg)

Fig. 6. Variation of $\gamma_p$ with $T$ for 8-cub and 8-ico clusters. The inset magnifies transitions of 8-cub cluster.

### 3.3. Size-dependency

#### 3.3.1. Size-dependent melting temperature
Safaei [43] developed a model considering the effects of the 1st nearest neighbors (NN) and the 2nd NN atomic interactions. An approximation of the formula without considering 2nd NN atomic interaction is as follows:

$$
\frac{T_{m p}}{T_{m b}}=1-\frac{N_{s}}{N_{t}}\left(1-q \frac{\epsilon_{s}}{\epsilon_{i}}\right), \quad q=\frac{\bar{Z}_{s}}{Z_{i}}
\tag{10}
$$

here $N_s$ stands for the number of surface atoms, $q$ is the coordination number ratio with $Z_i$ equal to 12 for interior atoms and $\bar{Z}_s$ as the average coordination numbers of surface atoms. The $\epsilon_i$ and $\epsilon_s$ respectively are bond energies of interior and surface atoms which the latter consists of cluster faces, edges and corners.

Fig. 7 compares normalized $T_{mp}$ obtained from caloric curves in comparison with previous MD [3,40] and MC [44] simulations. The figure also contains values calculated from Eq. (10) assuming that the bond strength for the surface and interior atoms to be equal. The melting points in the present study are in good agreement with previous MD result and lower than Safaei model [43]. However, the model always predicts lower $T_{mp}$ for cub due to lower coordination number of (1 0 0) planes at the surface while ico surface is only made out of (1 1 1) planes with a higher coordination number. In this simulation, however, 2-8-cub clusters are showing a different trend than higher shell numbers since 2-4-cub are already transformed to ico during relaxation and 6-8-cub transform to ico before melting. Thus, the first deficiency of the models is assuming a static crystallite without a crossover of different structures. Another difference is a smoother variation of $T_{mp}$ in the present result. These differences can also be explained by the static assumptions in the models. For instance, the $Z_i$ equal to 12 is not satisfied for sub-surface atoms at an elevated temperature when surface diffusion occurs or the ratio of fcc atoms drops as shown in Fig. 4. The MC result for clusters with 12-14 atoms shows Pd₁₃ very well fitted with Safaei model and thus it is valid for full shell clusters. However, the model is unable to describe $T_{mp}$ of Pd₁₂ and Pd₁₄ clusters those reshaped to form a more stable cluster.

#### 3.3.2. Size-dependent melting enthalpy
Attarian and Safaei [46] proposed the following model for the size-dependent melting enthalpy of clusters.

$$
\frac{H_{m p}}{H_{m b}}=\left[1-2(1-q) \frac{D_{0}}{D+D_{0}}\right]\left\{1+\frac{3 R T_{m b}}{2 H_{m b}} \ln \left[1-2(1-q) \frac{D_{0}}{D+D_{0}}\right]\right\}
\tag{11}
$$

with $D_0$ being a specific diameter which the entire atoms are located at the surface (i.e. $N_s=N_t$) and $H_{mb}$ is the bulk melting enthalpy.

The variation of $H_{mp}$ with the particle size is shown in Fig. 8 in comparison with Attarian and Safaei [46] model and previous MD results [3,40]. However, the model shows a negligible difference for ico and cub and thus it is plotted for different $\bar{Z}_s$ of 6 and 3 corresponding to $q=0.5$ and 0.25, respectively. As can be seen, the model predicts an increase in the $H_{mp}$ with the particle size. However, the model determines $H_{mp}<0$ below 0.5754 and 1.1984 nm respectively for $\bar{Z}_s$ of 6 and 3 meaning that melting of smaller particles are exothermic and favorable. This failure is originated from crystalline basis of the model, which is not defined for a few atoms. Again, the results present a unified trend for ico clusters, while small cub clusters have a different trend than bigger ones. It can be seen that the result of Pan et al. [3] underestimates the $H_{mp}$ using SC potential.

#### 3.3.3. Size-dependent surface energy
Fig. 9 shows the normalized surface energy calculated using Eq. (4) and (9), in comparison with Jiang model Eq. (8), previous MD simulation [40] and experimental results [48,49]. The figure clearly shows the Eq. (4) (slab model) predicts a linear increase of $\gamma_p$ with the particle size. While Eq. (9) and Jiang model are showing a non-linear variation of $\gamma_p$ with the particle size in agreement with Tolman model [50], perturbation theory [51,52] and MC simulation [53]. This is very important since the latter predicts $\gamma_p=\gamma_b$ for a infinity large particle while former results in values bigger than $\gamma_b$. Based on experimental data, Eq. 4 and liquid drop model used in the calculation of spherical cluster underestimated the $\gamma_p$. It is worth noting that there is negligible difference between values calculated for cub and ico in all cases.

![](./images/812744168873918466_7.jpg)

Fig. 7. Dependence of the $T_{mp}$ on the size of particle obtained from $C_p$ in comparison with MD [3,40] and MC simulation [44] as well as Safaei model [43]. All datasets are normalized to the experimental value of $T_{mb}=1825$ K [45].

## 4. Conclusion

In conclusion, the stability and melting behavior of palladium clusters with 2-20 shells of cub and ico structures studied using molecular dynamics simulation and EAM force field. The result shows small cub clusters are unstable at room temperature in agreement with experimental results. While cub clusters of intermediate size transform to ico at elevated temperatures and both cub and ico are stable up to the melting point for larger sizes. It is shown that $G(r)$ features are similar for the clusters and bulk. Thus $G(r)$ is not a surface sensitive method and needs to be compared with CNA to provide meaningful data on solid state transitions. While potential energy distribution gives

![](./images/812744168873918466_8.jpg)

Fig. 8. Variation of melting enthalpy with the diameter of Pd clusters, in comparison with previous MD results [3,40] as well as Attarian and safaei [46] model using $D_0=0.6712$ nm and the bulk value 16.7 kJ/mol [47].

![](./images/812744168873918466_9.jpg)

Fig. 9. Variation of normalized $\gamma_p$ with the cluster size at 300 K using proposed, Eqs. (9) and (4) in comparison with Jiang [42] model and spherical cluster calculated by liquid drop model [40]. The experimental data was calculated in Ref [48] from surface stress of embedded clusters with weak particle matrix infractions [49]. All datasets were normalized to the bulk value of $2050\ \text{mJ/m}^2$[41].

different characteristics for the interior and surface atoms and even various sites at the surface i.e. plane, edge and corner. This allows the distinction between solid state transition and surface melting. Furthermore, utilizing $\gamma_p$ for detection of allotropic and melting transitions was compared to caloric curves i.e. potential energy and $C_p$. It is shown that cub to ico transition appears as a step change in potential energy which was neglected in the previous studies. While it appears as a minor peak in $C_p$ or a local minimum in $\gamma_p$ below melting point. However, the accuracy of $C_p$ depends on the number of samples averaged over. It is also shown that the well-known slab model predict the wrong trend for temperature and size dependency of clusters in contradiction with Guggenheim-Katayama and Tolman models, respectively. A simple relation was introduced based on available models that predict a correct trend for both size and temperature dependent $\gamma_p$.

## Data availability

The raw/processed data required to reproduce these findings cannot be shared at this time as the data also forms part of an ongoing study.

## Conflict of interest

The authors have no conflict of interest to declare.

## Acknowledgments

The Authors would like to thank Dr. Ebrahim Tayyebi and professor Hamid Modarress from Physical Chemistry groups respectively at University of Iceland and Amirkabir University of Technology for sharing their expertise in the surface energy calculation. This work is partially supported by University of Iceland Research Fund.

## Appendix A. Supplementary data

Supplementary data associated with this article can be found, in the online version, at https://doi.org/10.1016/j.commatsci.2019.109187.

## References

[1] M. Schmidt, R. Kusche, B. von Issendorff, H. Haberland, Irregular variations in the melting point of size-selected atomic clusters, Nature 393 (1998) 238-240.
[2] M. Kateb, M. Azadeh, P. Marashi, S. Ingvarsson, Size and shape-dependent melting mechanism of pd nanoparticles, J. Nanopart. Res. 20 (2018) 251.
[3] Y. Pan, S. Huang, Z. Liu, W. Wang, Molecular dynamics simulation of shell-symmetric Pd nanoclusters, Mol. Simul. 31 (2005) 1057-1061.
[4] J. Westergren, S. Nordholm, Melting of palladium clusters-density of states determination by Monte Carlo simulation, Chem. Phys. 290 (2003) 189-209.
[5] F. Baletto, R. Ferrando, A. Fortunelli, F. Montalenti, C. Mottet, Crossover among structural motifs in transition and noble-metal clusters, J. Chem. Phys. 116 (2002) 3856-3863.
[6] D. Schebarchov, S. Hendy, Solid-liquid phase coexistence and structural transitions in palladium clusters, Phys. Rev. B 73 (2006) 121402.
[7] F.A. Lindemann, The calculation of molecular vibration frequencies, Phys. Z. 11 (1910) 609-612.
[8] S. Alavi, D.L. Thompson, Molecular dynamics simulations of the melting of aluminum nanoparticles, J. Phys. Chem. A 110 (2006) 1518-1523.
[9] H. Zhang, J.F. Douglas, Glassy interfacial dynamics of Ni nanoparticles: part I colored noise, dynamic heterogeneity and collective atomic motion, Soft Matter 9 (2013) 1254-1265.
[10] J.-H. Shim, B.-J. Lee, Y.W. Cho, Thermal stability of unsupported gold nanoparticle: a molecular dynamics study, Surf. Sci. 512 (2002) 262-268.
[11] S. Zhao, S. Wang, D. Cheng, H. Ye, Three distinctive melting mechanisms in isolated nanoparticles, J. Phys. Chem. B 105 (2001) 12857-12860.
[12] Y. Qi, T. Çag˘ın, W.L. Johnson, W.A. Goddard III, Melting and crystallization in Ni nanoclusters: the mesoscale regime, J. Chem. Phys. 115 (2001) 385-394.
[13] L. Wang, Y. Zhang, X. Bian, Y. Chen, Melting of Cu nanoclusters by molecular dynamics simulation, Phys. Lett. A 310 (2003) 197-202.
[14] F.D. Fischer, T. Waitz, D. Vollath, N.K. Simha, On the role of surface energy and surface stress in phase-transforming nanoparticles, Prog. Mater. Sci. 53 (2008) 481-527.
[15] F.P. Buff, The spherical interface. I. Thermodynamics, J. Chem. Phys. 19 (1951) 1591-1594.
[16] V.S. Myasnichenko, M. Razavi, M. Dtukesh, N.Y. Sdobnyakov, M.D. Starostenkov, Molecular dynamic investigation of size-dependent surface energy of icosahedral copper nanoparticles at different temperature, Lett. Mater. 6 (2016) 266-270.
[17] Q. Mei, K. Lu, Melting and superheating of crystalline solids: from bulk to nanocrystals, Prog. Mater. Sci. 52 (2007) 1175-1262.
[18] S.K. Sankaranarayanan, V.R. Bhethanabotla, B. Joseph, Molecular dynamics simulation study of the melting of Pd-Pt nanoclusters, Phys. Rev. B 71 (2005) 195415.

[19] M.P. Allen, D.J. Tildesley, Computer Simulation of Liquids, Oxford University Press, 1989.

[20] S. Plimpton, Fast parallel algorithms for short-range molecular dynamics, J. Comput. Phys. 117 (1995) 1–19.

[21] S. Foiles, M. Baskes, M. Daw, Embedded-atom-method functions for the fcc metals Cu, Ag, Au, Ni, Pd, Pt, and their alloys, Phys. Rev. B 33 (1986) 7983.

[22] M.S. Daw, S.M. Foiles, M.I. Baskes, The embedded-atom method: a review of theory and applications, Mater. Sci. Rep. 9 (1993) 251–310.

[23] S. Foiles, J. Adams, Thermodynamic properties of fcc transition metals as calculated with the embedded-atom method, Phys. Rev. B 40 (1989) 5909.

[24] S. Foiles, Application of the embedded-atom method to liquid transition metals, Phys. Rev. B 32 (1985) 3409.

[25] J. Mei, J. Davenport, G. Fernando, Analytic embedded-atom potentials for fcc metals: application to liquid and solid copper, Phys. Rev. B 43 (1991) 4653.

[26] M.S. Daw, M.I. Baskes, Embedded-atom method: derivation and application to impurities, surfaces, and other defects in metals, Phys. Rev. B 29 (1984) 6443.

[27] L. Verlet, Computer experiments on classical fluids. I. Thermodynamical properties of Lennard-Jones molecules, Phys. Rev. 159 (1967) 98.

[28] M. Kateb, K. Dehghani, Comparison of fracture behavior of sharp with blunt crack tip in nanocrystalline materials by molecular dynamics simulation, Int. J. Modern Phys.: Conf. Ser. 5 (2012) 410–417.

[29] M. José-Yacamán, M. Marín-Almazo, J.A. Ascencio, High resolution TEM studies on palladium nanoparticles, J. Mol. Catal. A: Chem. 173 (2001) 61–74.

[30] Y. Wen, H. Fang, Z. Zhu, S. Sun, Molecular dynamics investigation of shape effects on thermal characteristics of platinum nanoparticles, Phys. Lett. A 373 (2009) 272–276.

[31] C.P. Poole Jr, F.J. Owens, Introduction to Nanotechnology, John Wiley & Sons, 2003.

[32] A. Stukowski, Visualization and analysis of atomistic simulation data with OVITO- the open visualization tool, Modell. Simul. Mater. Sci. Eng. 18 (2009) 015012.

[33] Y. Zhang, Y.-H. Wen, Z.-Z. Zhu, S.-G. Sun, Structure and stability of Fe nanocrystals: an atomistic study, J. Phys. Chem. C 114 (2010) 18841–18846.

[34] I. Chepkasov, Y.Y. Gafner, M. Vysotin, et al., A study of melting of various types of Pt-Pd nanoparticles, Phys. Solid State 59 (2017) 2076–2081.

[35] I.V. Chepkasov, M.A. Visotin, E.A. Kovaleva, A.M. Manakhov, V.S. Baidyshev, Z.I. Popov, Stability and electronic properties of PtPd nanoparticles via MD and DFT calculations, J. Phys. Chem. C 122 (2018) 18070–18076.

[36] P.J. Steinhardt, D.R. Nelson, M. Ronchetti, Bond-orientational order in liquids and glasses, Phys. Rev. B 28 (1983) 784.

[37] D. Faken, H. Jnsson, Systematic analysis of local atomic structure combined with 3D computer graphics, Comput. Mater. Sci. 2 (1994) 279–286.

[38] L. Vitos, A. Ruban, H.L. Skriver, J. Kollar, The surface energy of metals, Surf. Sci. 411 (1998) 186–202.

[39] B. Medasani, I. Vasiliev, Computational study of the surface properties of aluminum nanoparticles, Surf. Sci. 603 (2009) 2042–2046.

[40] L. Miao, V.R. Bhethanabotla, B. Joseph, Melting of Pd clusters and nanowires: a comparison study using molecular dynamics simulation, Phys. Rev. B 72 (2005) 134109.

[41] N.K. Adam, The Physics and Chemistry of Surfaces, third ed., Oxford University Press, 1941.

[42] Q. Jiang, H. Lu, Size dependent interface energy and its applications, Surf. Sci. Rep. 63 (2008) 427–464.

[43] A. Safaei, The effect of the averaged structural and energetic features on the co-hesive energy of nanocrystals, J. Nanopart. Res. 12 (2010) 759–776.

[44] Y.J. Lee, E.-K. Lee, S. Kim, R.M. Nieminen, Effect of potential energy distribution on the melting of clusters, Phys. Rev. Lett. 86 (2001) 999.

[45] M. Wortis, Equilibrium crystal shapes and interfacial phase transitions, Chemistry and Physics of Solid Surfaces VII, Springer, 1988, pp. 367–405.

[46] M. Attarian Shandiz, A. Safaei, Melting entropy and enthalpy of metallic nano-particles, Mater. Lett. 62 (2008) 3954–3956.

[47] T. Iida, R.I. Guthrie, The Physical Properties of Liquid Metals, Clarendon Press, Walton Street, Oxford OX 2 6 DP, UK, 1988.

[48] H. Lu, Q. Jiang, Comment on higher surface energy of free nanoparticles, Phys. Rev. Lett. 92 (2004) 179601.

[49] R. Lamber, S. Wetjen, N.I. Jaeger, Size dependence of the lattice parameter of small palladium particles, Phys. Rev. B 51 (1995) 10968.

[50] R.C. Tolman, The effect of droplet size on surface tension, J. Chem. Phys. 17 (1949) 333–337.

[51] V. Samsonov, L. Shcherbakov, A. Novoselov, A. Lebedev, Investigation of the mi-crodrop surface tension and the linear tension of the wetting perimeter on the basis of similarity concepts and the thermodynamic perturbation theory, Colloids Surf. A 160 (1999) 117–121.

[52] E. Tayyebi, S. Amjad-Iranagh, K. Golzar, H. Modarress, Surface tension curvature correction for fluid-vapour interface by thermodynamics of curved boundary layers, Phys. Chem. Liq. 52 (2014) 400–415.

[53] V. Samsonov, A. Chernyshova, N.Y. Sdobnyakov, Size dependence of the surface energy and surface tension of metal nanoparticles, Bull. Russ. Acad. Sci.: Phys. 80 (2016) 698–701.
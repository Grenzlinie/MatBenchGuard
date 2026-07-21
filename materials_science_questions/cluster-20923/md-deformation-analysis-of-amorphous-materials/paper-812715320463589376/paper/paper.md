![](./images/812715320463589376_1.jpg)
![](./images/812715320463589376_2.jpg)

Article

# Super Ductility of Nanoglass Aluminium Nitride

Yinbo Zhao $^{1}$ , Xianghe Peng $^{1, *}$, Cheng Huang $^{1}$, Bo Yang $^{1}$, Ning Hu $^{1}$ and Mingchao Wang $^{2}$

1 College of Aerospace Engineering, Chongqing University, Chongqing 400044, China;
zyb123@cqu.edu.cn (Y.Z.); huangcheng@cqu.edu.cn (C.H.); yangbo16@cqu.edu.cn (B.Y.);
ninghu@cqu.edu.cn (N.H.)
2 Department of Materials Science and Engineering, Faculty of Engineering, Monash University, Clayton,
VIC 3800, Australia; Mingchao.Wang@monash.edu

* Correspondence: xhpeng@cqu.edu.cn

Received: 25 September 2019; Accepted: 28 October 2019; Published: 29 October 2019

![](./images/812715320463589376_3.jpg)

**Abstract:** Ceramics have been widely used in many fields because of their distinctive properties, however, brittle fracture usually limits their application. To solve this problem, nanoglass ceramics were developed. In this article, we numerically investigated the mechanical properties of nanoglass aluminium nitride (ng-AlN) with different glassy grain sizes under tension using molecular dynamics simulations. It was found that ng-AlN exhibits super ductility and tends to deform uniformly without the formation of voids as the glassy grain size decreases to about 1 nm, which was attributed to a large number of uniformly distributed shear transformation zones (STZs). We further investigated the effects of temperature and strain rate on ng-AlN$_{d=1\ \text{nm}}$, which showed that temperature insignificantly influences the elastic modulus, while the dependence of the ultimate strength on temperature follows the $T^{2/3}$ scaling law. Meanwhile, the ultimate strength of ng-AlN$_{d=1\ \text{nm}}$ is positively correlated with the strain rate, following a power function relationship.

**Keywords:** nano-glass ceramic; amorphous AlN; interface; ductility; molecular dynamics simulations

## 1. Introduction

High-strength ceramics [1] have been extensively investigated owing to their high strength and hardness, and low density, etc. among which aluminium nitride (AlN), a member of nitrides with metals from the IIIA group has attracted considerable attention due to its distinctive properties, as well as its mechanical properties. For instance, AlN with a wurtzite structure can be used as an ideal radiator and electronic packaging material, due to its high thermal conductivity [2,3], low thermal expansion [4,5], and excellent insulation [6] properties. However, the tensile brittle rupture due to the strong covalent bonds makes their application strongly limited [7]. In order to overcome this deficiency, great efforts have been made to enhance its ductility and toughness. It was found by Heard et al. [8] that an intrinsic failure pattern of the AlN known as brittle fracture would be changed to plastic deformation under a high hydrostatic pressure condition. Meanwhile, it was found in an experiment that the decrease of the size of AlN pillar may induce brittle-to-ductile transition, due to the activation of dislocations [9]. Besides, at high pressure, metal oxides with an amorphous structure could undergo severe plastic deformation at moderate temperatures [10–12]. Zhao et al. [13] further investigated the deformation mechanism in amorphous AlN (a-AlN), and found that, compared with its crystalline counterpart, the enhanced ductility of a-AlN can be attributed to the self-repairing mechanism.

Nanoglass (NG) [14] is a class of novel non-crystalline materials, which was first proposed and synthesised by Jing et al. [15] in 1989. NG is made up of glassy nanoclusters connected by the glass-glass interfaces prepared via compacting glassy nanoparticles [16]. Fang et al. [17] investigated the deformation structure of Sc₇₅Fe₂₅ nanoglass and found that nanoglass could undergo remarkable plastic deformation, which was attributed to the effect of glass-glass interface. Sopu et al. [18] found

Nanomaterials 2019, 9, 1535; doi:10.3390/nano9111535
www.mdpi.com/journal/nanomaterials

that the glassy interfaces could play a precursor role in the formation of shear bands (SBs). Adibi et al. [19] investigated the effect of the glassy grain size and found that, with the decrease of the grain size, the deformation mode changes from a single SB to uniform superplastic flow. Softening towards the NG occurs during superplastic flow, so Sha et al. [20] proposed a bimodal grain size model, which could improve the strength without sacrificing super-plasticity. Besides the attractive mechanical properties, NG exhibits enhanced thermal stability compared with MG (Metallic glass) [21,22], attributed to the lower free energy state of NG compared with MG [23]. Based on the properties of nanoglass mentioned above, Gleiter [14] predicted that an age of new technologies based on non-crystalline materials would begin. Kushima et al. [24] found that the crystalline structure of ZnO nanowire electrode was transformed into NG during the first charge in the Li-ion nanobattery, which implies the necessity to investigate the mechanical properties of NG ceramics.

However, less progress in the mechanical properties of the NG ceramics could be found in the literature. In addition, it is difficult to obtain the information about the inhomogeneous structure of NGs in experiments, as X-ray or neutron-based techniques can only provide average structural information [23]. Molecular dynamics simulation (MD) can serve as an effective means to gain an insight into the microstructure in NG ceramics and their evolution during deformation. MD simulation has been widely adopted to investigate different kinds of mechanical response of various atomic structures, such as dislocations [25,26], nano-twin boundaries [27,28], and shear bands [13,29], etc. with the Large-scale Atomic/Molecular Massively Parallel Simulator (LAMMPS) algorithm [30].

In this work, we aim to confirm the effect and the influencing effects of nanoglass structure that may help to improve or achieve the super ductility of ceramics by changing its nanostructure without adding any other ingredients, for the purpose to promote the more extensive applications of ceramics in more fields. The mechanical property of nanoglass AlN (ng-AlN) is to be investigated using the MD simulations and compared with that of a-AlN, and the mechanisms of the super ductility of ng-AlN are to be uncovered. First, the short range order (SRO) and medium range order (MRO) nanostructures at the glassy interface are studied. Then, the effects of the size of the glassy particles in ng-AlN are explored. Finally, the temperature and strain rate effects during tension are investigated.

## 2. Computational Methods

Systematic simulations are performed with the Large-scale Atomic/Molecular Massively Parallel Simulator (LAMMPS) [30], which is open code and has the functions required for this research. The atomic interactions within the Al-N are modelled with the Vashishta potential [31], which has been widely used to investigate the deformation mechanism of AlN under different kinds of loading conditions [13,29,32,33]. The integration time step of 1 fs is adopted in all the simulations. First, to construct an amorphous AlN unit, a crystal unit (w-AlN) with the size of $49.76\ (x) \times 48.47\ (y) \times 49.80\ (z)\ \mathring{A}^3$ is built at first, then it is melted at 3500 K for 500 ps and cooled down to 10 K at a rate of $2 \times 10^{14}$ K/s, at zero external pressure (NPT) ensemble with periodic boundary conditions (PBCs) applied in all dimensions [13]. Second, ng-AlN is constructed with the Voronoi tessellation method [34] using the "seeds" randomly distributed in the sample with the amorphous AlN (a-AlN) unit as a source. The size of the cuboidal sample is $262\ \mathring{A}\ (x) \times 51\ \mathring{A}\ (y) \times 523\ \mathring{A}\ (z)$. In order to study the effect of grain size on the mechanical properties of nanoglass ceramic, 7, 27, and 436 seeds are distributed randomly and the corresponding average grain sizes are 8, 4, and 1 nm, respectively, as shown in Figure 1a. The grains are columnar with the generatrix along the $y$ direction. To avoid an abnormal high stress concentration, the overlapped atoms at the glassy gains are deleted. Then, the conjugate gradient algorithm is adopted to minimize the energy of the structure. They are relaxed in isothermal-isobaric (NPT) ensemble by a Nose-Hoover thermostat at 10 K for 200 ps to release the residual stress with the PBCs applied to the three directions. For comparison, the amorphous AlN (a-AlN) is also generated by replication of the a-AlN unit [13], as mentioned above, with the same size of ng-AlN as illustrated in Figure 1a. It is then relaxed in an NPT ensemble for 200 ps at 10 K as well.

![](./images/812715320463589376_4.jpg)

Figure 1. (a) Atomic configuration of ng-AlN with average grain size of 8 nm, 4 nm, and 1 nm, and
a-AlN, respectively. Grains are coloured to highlight the architecture; (b) Distributions of atomic
volume corresponding to these samples after relaxation, respectively.

Uniaxial tension is applied along the z-direction for all the samples with a constant strain rate
of $10^8$ s$^{-1}$. The PBCs are used in y- and z-directions and the free surface condition towards the
x-direction. The simulations are performed in an NVE (microcanonical) ensemble for 3000 ps at 10 K
using a Langevin thermostat [35]. The temperature of 10 K is adopted to reduce the influence of the
perturbation caused by the random vibration of the atoms. The atomic stress is calculated based on the
virial stress [36]. Mises equivalent strain [37], $\varepsilon_{equ}$, is employed to identify the plastic deformation of
the sample, and the region where $\varepsilon_{equ} \geq 0.2$ is considered as a shear transformation zone (STZ) [13].
The software Ovito [38] is used to process and visualise the simulation results.

## 3. Results and Discussion

### 3.1. Structural of ng-AlN

ng-AlN has an amorphous structure containing a certain fraction of interfaces, which is different from the conventional a-AlN. To better understand the structure of ng-AlN, the radial distribution functions (RDFs) of ng-AlN with different grain sizes and that of a-AlN are analysed and shown in Figure 2a. RDF is defined as the average density of the atoms in a thin spherical shell, with a reference atom as its center, and $r$ and $r + dr$ as its inner and outer radii, respectively. RDF can be expressed as:

$$
g(r)=\frac{N(r, r+d r)}{4 \pi r^{2} d r \rho} \tag{1}
$$

where $N(r, r + dr)$ the number of atoms in the spherical shell, and $\rho$ is the average density of the sample. Figure 2a respectively shows the RDF curves of a-AlN, ng-AlN$_{d=8\ \text{nm}}$, ng-AlN$_{d=4\ \text{nm}}$, and ng-AlN$_{d=1\ \text{nm}}$ where it can be seen that they almost coincide with each other. The locations of the first peak, which are related to the bond length of Al-N, are nearly identical; however, the height of the first peak (which is also defined as "intensity") corresponding to a-AlN is higher than those of ng-AlNs, as shown in the upper inset in Figure 2a, indicating that the average coordination number (CN) of a-AlN is larger than that of ng-AlN. The intensity decreases with the increase of the glassy interface in the ng-AlN samples, indicating that the average CN decreases with the increase of the glassy interface. The distributions of CN in a-AlN and ng-AlNs with different grain sizes are shown in Figure 2b. As we know, only three kinds of short range order (SRO) structures exist in a-AlN, i.e., threefold-coordinated, fourfold-coordinated, and fivefold-coordinated atoms [13,39]. In the ng-AlN, we do not find any other SRO structures different from that in a-AlN, as shown in Figure 2b. The fraction of five-coordinated atoms covers only about 0.5%, while three-coordinated atoms and four-coordinated atoms account for nearly 30% and 70% in the ng-AlN of different particle sizes and in a-AlN, respectively. With the increase of interface, the fraction of four-coordinated atoms decreases and three-coordinated atoms increases (Figure 2b), leading to a reduction of average CN. The second peaks in the RDF curves (Figure 2a) related to the bond lengths of both Al-Al and N-N correspond to the medium range order (MRO) structure. With the increase of interface, the position of the second peak shifts leftwards, indicating the decrease of the lengths of both Al-Al and N-N bonds. It has been shown that there are four kinds of MRO structures in a-AlN, i.e., fourfold ring, sixfold ring, eightfold ring, and tenfold ring, respectively [13]. In the RDF curves, the sequence of the heights of the second peaks is similar to that of the first peaks, indicating that the MRO structures in ng-AlN are relatively sparse compared with those in a-AlN, and become sparser with the increase of the interface. In order to further investigate the properties of the glassy interface, the Voronoi volume [40] is calculated for a-AlN and ng-AlNs with different grain sizes after relaxation, as shown in Figure 1b, where it can be found that the atomic volume at the glassy interface is larger than that in the intragranular part, which should be related to the decrease of the CN of ng-AlN.

![](./images/812715320463589376_5.jpg)

Figure 2. (a) Radial distribution functions (RDFs), (b) Coordination number of a-AlN, ng-AlN$_{d=8\ \text{nm}}$, ng-AlN$_{d=4\ \text{nm}}$, and ng-AlN$_{d=1\ \text{nm}}$, respectively.

### 3.2. Comparison between Mechanical Properties of ng-AlN and a-AlN

The stress strain ($\sigma-\varepsilon$) curves of the ng-AlNs with the grain sizes of $d=1$ nm, 4 nm, and 8 nm, respectively, are shown in Figure 3, where the $\sigma-\varepsilon$ curve of a-AlN is also provided for comparison. To better distinguish the elastic moduli of these samples, we calculate the bulk modulus, $B$ and Young's modulus, $Y$, of these samples with the elastic constants using the following relationships,

$$
B=\frac{C_{11}+2 C_{12}}{3} \tag{2}
$$

$$
Y=\frac{\left(C_{11}+2 C_{12}\right)\left(C_{11}-C_{12}\right)}{C_{11}+C_{12}}. \tag{3}
$$

![](./images/812715320463589376_6.jpg)

Figure 3. Tensile stress-strain ($\sigma - \varepsilon$) curves for a-AlN and ng-AlNs with average grain size of 8 nm, 4 nm, and 1 nm, respectively.

The calculated $B$ and $Y$ of these samples shown in Table 1, where it can be seen that $B$ and $Y$ of ng-AlNs are smaller than those of a-AlN, and they decrease with the decrease of the grain size. Such kind of reduction in elastic property could be related to higher free volume at glassy interface, as shown in Figure 1b. Meanwhile, the cohesive energy decreases with the increase of grain size, which implies that the structure with larger grain size should be more stable. It means that the glassy interface has higher energy than the amorphous matrix. The ultimate strengths of ng-AlNs are relatively smaller than that of a-AlN and decrease with the decrease of grain size, as illustrated in Figure 3, which should be the result of the softer glass-glass interface, i.e., the more the glassy interface, the softer the ng-AlN.

Table 1. Mechanical properties of a-AlN and ng-AlNs obtained with the Molecular dynamics simulation (MD) simulations. Notations: $Ec$ (eV), cohesive energy; $B$ (GPa), bulk modulus; $C_{11}$ and $C_{12}$ (GPa), elastic constant; $Y$ (GPa), Young modulus.

<table>
<thead>
  <tr>
    <th></th>
    <th>$Ec$ (eV)</th>
    <th>$B$ (GPa)</th>
    <th>$C_{11}$ (GPa)</th>
    <th>$C_{12}$ (GPa)</th>
    <th>$Y$ (GPa)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>a-AlN</td>
    <td>−5.480</td>
    <td>98.8</td>
    <td>155.6</td>
    <td>70.4</td>
    <td>111.7</td>
  </tr>
  <tr>
    <td>ng-AlN$_{d=8\mathrm{nm}}$</td>
    <td>−5.474</td>
    <td>96.6</td>
    <td>153.0</td>
    <td>68.4</td>
    <td>110.7</td>
  </tr>
  <tr>
    <td>ng-AlN$_{d=4\mathrm{nm}}$</td>
    <td>−5.469</td>
    <td>95.1</td>
    <td>151.0</td>
    <td>67.2</td>
    <td>109.6</td>
  </tr>
  <tr>
    <td>ng-AlN$_{d=1\mathrm{nm}}$</td>
    <td>−5.454</td>
    <td>90.9</td>
    <td>145.6</td>
    <td>63.6</td>
    <td>106.9</td>
  </tr>
</tbody>
</table>

With the increase of the glassy interface, the sample becomes more ductile, as shown in Figure 3. In order to investigate the deformation mechanism of the enhanced ductility with the decrease of the glassy grain size, the local shear strain is shown in Figure 4. Different from a-AlN, STZs are mainly activated in the glassy interface. $\sigma$ reaches the ultimate strength at $\varepsilon = 0.1204$, 0.1208, 0.1334, and 0.1402, for a-AlN, ng-AlN$_{d=8\mathrm{nm}}$, ng-AlN$_{d=4\mathrm{nm}}$, and ng-AlN$_{d=1\mathrm{nm}}$, respectively, as shown in Figure 4, which could be ascribed to that the free volume at the glassy interface is larger than that in the matrix. The main shear band forms in a-AlN at $\varepsilon = 0.180$, as shown in Figure 4a. While in ng-AlN$_{d=8\mathrm{nm}}$ and ng-AlN$_{d=4\mathrm{nm}}$, STZs form at the glassy interface coalesce, propagate over the entire sample, and

develop to shear bands (SBs) at $\varepsilon = 0.180$, as shown in Figure 4b,c. The SBs interact with each other in ng-AlNs due to the existence of glassy interfaces, leading to the slow drop of stress, as shown in Figure 3. The formation and propagation of SBs are driven by the elastic energy [18], and at the glassy interface the local energy is released, which may suppress the formation of mature shear band, accounting for that the width of the shear bands in ng-AlNs is smaller than that in a-AlN. Subsequently, voids initiate and grow in the SBs at $\varepsilon = 0.1900$, $0.2150$, and $0.2177$ in a-AlN, ng-AlN$_{d = 8\ \text{nm}}$, and ng-AlN$_{d = 4\ \text{nm}}$, as shown in Figure 4a–c, respectively. With the further increase of $\varepsilon$, the voids coalesce, giving rise to eventual destruction of the a-AlN, ng-AlN$_{d = 8\ \text{nm}}$ and ng-AlN$_{d = 4\ \text{nm}}$ sample at $\varepsilon = 0.3$. It is noteworthy that STZs emerge in the entire ng-AlN$_{d = 1\ \text{nm}}$ at $\varepsilon = 0.18$, as the result of high fraction of the glassy interface (Figure 4d). During the further loading, ng-AlN$_{d = 1\ \text{nm}}$ tends to deform uniformly without forming voids, exhibiting superplasticity, as can be seen in the $\sigma - \varepsilon$ curves in Figure 3.

The initiation and propagation of STZs associated with temporal and spatial distributions are closely related to the deformation mode [19,41]. In ng-AlN$_{d = 8\ \text{nm}}$ and ng-AlN$_{d = 4\ \text{nm}}$, although STZs develop mainly at the glassy interfaces at first, they expand through glassy grain boundaries, forming SBs that dominate the plastic deformation and may suppress the formation of other STZs at the glassy interfaces, as shown in Figure 4b,c. When the grain size is reduced to 1 nm, besides the STZs developing initially in the glassy interface, other new STZs appear, which may lead to homogeneous deformation in the whole sample under extremely large strain. It indicates that the glassy grain size strongly affects deformation mode of nanoglass ceramics. The fractions of atoms with $\eta_{i}^{Mises} > 0.2$ in a-AlN and ng-AlNs with different grain sizes during deformation process are shown in Figure 5. Overall, there are higher fraction of atoms at high shear strain level in ng-AlNs than that of a-AlN, due to the existence of glassy interface, and the fraction increases with the increase of glassy interface, due to the decrease of the grain size, as shown in Figure 5. It is noteworthy that the fraction of atoms at higher shear strain level in ng-AlN$_{d = 1\ \text{nm}}$ at $\varepsilon = 0.3$ is about 60%, indicating that most atoms participating in the shear deformation may lead to more uniform plastic deformation. Another interesting phenomenon is that in ng-AlN$_{d = 1\ \text{nm}}$ the fraction of atoms at high shear strain level before $\varepsilon = 0.19$ is smaller than that in the others, as shown in Figure 5. As the fraction of glassy interfaces in ng-AlN$_{d = 1\ \text{nm}}$ is much larger than that in the other ng-AlNs and glassy interface plays softeningrole, the stored elastic energy in ng-AlN$_{d = 1\ \text{nm}}$ should be less than that in the others, which could trigger relatively fewer STZs in the initial stage.

![](./images/812715320463589376_7.jpg)

Figure 4. Evolution of von-Mises strain for (a) a-AlN, (b) ng-AlN$_{d=8\,\text{nm}}$, (c) ng-AlN$_{d=4\,\text{nm}}$, (d) ng-AlN$_{d=1\,\text{nm}}$ at different strain levels.

![](./images/812715320463589376_8.jpg)

Figure 5. Fraction of atoms with relatively large atomic von Mises shear strain $\eta_{i}^{Mises} > 0.2$ for a-AlN
and ng-AlNs with different grain sizes at different strains.

### 3.3. Effect of Temperature

As has been mentioned above, when the glassy grain size of ng-AlN is reduced to 1nm, it exhibits superplasticity. In this subsection, we further investigate the effect of temperature on the mechanical property of ng-AlN$_{d=1\ \text{nm}}$ under tension, as shown in Figure 6. Before loading, the sample is relaxed at 150 K, 300 K, 450 K, and 600 K, respectively, to achieve the stable structure at the corresponding temperature. Similarly, we calculate the bulk and elastic moduli of these samples with the elastic constants at different temperatures, as shown in Table 2, where it can be seen that the temperature insignificantly influences the elastic property. In contrast, the ultimate strength is sensitive to the temperature, as can be seen in Figure 6. Figure 7 shows the effect of temperature ($T$) on the ultimate strength ($\sigma_{b}$). It is obvious that $\sigma_{b}$ decreases with the increase of $T$. Johnson et al. [42] proposed a universal criterion for the temperature dependence on yield strength:

$$
\sigma_{y}(T)=\sigma_{0}\left[1-C\left(T / T_{g}\right)^{2 / 3}\right] \tag{4}
$$

where $\sigma_{0}$ is a constant, $T_{g}$ the glass transition temperature of AlN ($T_{g}=3070$ K, predicted from MD simulations [31]) and the parameter $C \equiv\left[g(k / \beta) \ln \left(\omega_{0} / \tau \dot{\varepsilon}\right)\right]^{2 / 3}$ [43], which depends on the strain rate $\dot{\varepsilon}$. $g$ measures the $T$-dependence of elastic moduli, $k$ is the Boltzmann constant, and $\omega_{0}$ the frequency of shear waves of nm wavelength. These parameters and $\beta, \tau$ can be treated as constants [42].
The relationship between $\sigma_{b}$ and $T$ can be well described by Equation (4) with $C=1.06$, as shown in Figure 7, which can be ascribed to the fact that diffusive homogeneous flow may take place at a lower stress level with diffusive rearrangements at high temperature.

![](./images/812715320463589376_9.jpg)

Figure 6. Tensile stress-strain $(\sigma - \varepsilon)$ curves for ng-AlN$_{d=1\ \text{nm}}$ under different temperatures.

Table 2. Mechanical properties of ng-AlN$_{d=1\ \text{nm}}$ at different temperature (10 K, 150 K, 300 K, 450 K,
and 600 K) obtained with the MD simulations.

<table>
  <thead>
    <tr>
      <th></th>
      <th>B (GPa)</th>
      <th>C₁₁ (GPa)</th>
      <th>C₁₂ (GPa)</th>
      <th>Y (GPa)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>10 K</td>
      <td>90.9</td>
      <td>145.6</td>
      <td>63.6</td>
      <td>106.9</td>
    </tr>
    <tr>
      <td>150 K</td>
      <td>92.7</td>
      <td>147.7</td>
      <td>65.2</td>
      <td>107.7</td>
    </tr>
    <tr>
      <td>300 K</td>
      <td>92.6</td>
      <td>147.7</td>
      <td>65.0</td>
      <td>107.9</td>
    </tr>
    <tr>
      <td>450 K</td>
      <td>91.5</td>
      <td>146.0</td>
      <td>64.2</td>
      <td>106.8</td>
    </tr>
    <tr>
      <td>600 K</td>
      <td>89.2</td>
      <td>142.7</td>
      <td>62.4</td>
      <td>104.7</td>
    </tr>
  </tbody>
</table>

![](./images/812715320463589376_10.jpg)

Figure 7. Ultimate strength as a function of temperature (T) for ng-AlN$_{d=1\ \text{nm}}$.

Next, we take 10 K, 300 K, and 600 K as the representatives to study the effect of temperature.
It is noteworthy that, with the increase of the temperature, the number of three-coordinated atoms

decreases, while that of four-coordinated atoms and five-coordinated atoms increases, as shown in Figure 8, which suggests that the free volume in the sample decreases with the increase of the temperature. The applied strains for ng-AlN$_{d=1\ \text{nm}}$ to reach its ultimate strengths are $\varepsilon=0.1402$, 0.1230, and 0.1184 corresponding to 10 K, 300 K, and 600 K, respectively, as shown in Figure 6, where it can be found that the applied strains decrease with the increase of the temperature, along with the emergence of STZs as illustrated in Figures 4d and 9a,b. As has been mentioned above, although the free volume decreases with the increase of the temperature, which may weaken the activation of the STZs, the increase of temperature may help to overcome the activation barrier of critical shear event, and permit shear localisation to occur at low stress level [41]. It can be found that temperature does not change the homogeneous deformation behaviour of ng-AlN$_{d=1\ \text{nm}}$, while the regions of STZs increase with the increase of the temperature at the same strain level, as comparing between Figures 4d and 9a,b. For direct observation, the fractions of the atoms with $\eta_i^{\text{Mises}}>0.2$ in ng-AlN$_{d=1\ \text{nm}}$ at different temperatures are shown in Figure 10, where it can be seen that the higher the temperature, the larger the fraction of atoms at higher shear strain level. It is worth to note that in ng-AlN$_{d=1\ \text{nm}}$, the fraction of atoms with $\eta_i^{\text{Mises}}>0.2$ could even reach about 82% at $\varepsilon=0.3$ in the case of 600 K.

![](./images/812715320463589376_11.jpg)

Figure 8. Radial distribution functions (RDFs) for ng-AlN$_{d=1\ \text{nm}}$ at different temperatures—10 K, 300 K, 600 K.

![](./images/812715320463589376_12.jpg)

Figure 9. Evolution of von-Mises strain for ng-AlN$_{d=1\ \text{nm}}$ at different strain levels at (a) 300 K and (b)
600 K, respectively.

![](./images/812715320463589376_13.jpg)

Figure 10. Fraction of atoms with relatively large atomic von Mises shear strain $\eta_{i}^{Mises}>0.2$ for
ng-AlN$_{d=1\ \text{nm}}$ at different temperatures with the variation of strain.

### 3.4. Effect of Strain Rate

The effect of strain rate on the mechanical properties of ng-AlN$_{d=1\ \text{nm}}$ under tension is shown
in Figure 11. It can be found that the ultimate strength is positively correlated with strain rate.
The variation of ultimate strength ($\sigma_{b}$) against strain rate ($\dot{\varepsilon}$) is shown in Figure 12, where it is obvious

that $\sigma_b$ increases with the increase of $\dot{\varepsilon}$. Symonds et al. [44] suggested a power law relationship for the dependence of yield strength, $\sigma_y$, on $\dot{\varepsilon}$ as follows:

$$
\sigma_y = A + B\dot{\varepsilon}^C \tag{5}
$$

where $A$, $B$, and $C$ are the fitting parameters. We extend Equation 5 to the description for the dependence of $\sigma_b$ on $\dot{\varepsilon}$, the parameters of which are fitted using the calculated results (Figure 12) as $A = 5.68756$, $B = 1.727 \times 10^{-5}$, $C = 0.48901$, and the fitting curve is also shown in Figure 12, where it can be seen that Equation (5) can well describe the dependence of $\sigma_b$ on $\dot{\varepsilon}$.

![](./images/812715320463589376_14.jpg)

Figure 11. Tensile stress-strain ($\sigma - \varepsilon$) curves for ng-AlN$_{d = 1\ \text{nm}}$ at different strain rates.

![](./images/812715320463589376_15.jpg)

Figure 12. Ultimate strength as a function of strain rate ($\dot{\varepsilon}$) for ng-AlN$_{d = 1\ \text{nm}}$.

The ultimate stress (or the yield stress) is closely related to the activation of the STZs. The available free volume (the free volume which is mobile [45]) decreases with the increase of the $\dot{\varepsilon}$, ascribed to the less time for atoms to diffuse and for the free volume to be rearranged. The fewer available free volume implies that the activation of STZ needs higher stress, leading to strain rate hardening effect [46]. The fraction of atoms of $\eta_i^{Mises} > 0.2$ in ng-AlN$_{d = 1\ \text{nm}}$ at different $\dot{\varepsilon}$ is shown in Figure 13a, where it

can be seen that the fraction of STZs decreases with the increase of $\dot{\varepsilon}$ before $\varepsilon=0.243$. It is rather remarkable that at $\varepsilon_{1}=0.243$ the fraction of STZs in the sample under tension at $\dot{\varepsilon}=5 \times 10^{8} \mathrm{~s}^{-1}$ exceeds that at $\dot{\varepsilon}=10^{8} \mathrm{~s}^{-1}$, and at $\varepsilon_{2}=0.265$ the fraction of STZs in the sample under tension at $\dot{\varepsilon}=10^{9} \mathrm{~s}^{-1}$ exceeds that at $\dot{\varepsilon}=5 \times 10^{8} \mathrm{~s}^{-1}$, as illustrated in Figure 13a. It can be attributed to that the heat induced by the formation of the first wave of STZs leads to the rapid activation of the next wave of STZs. The distributions of $\eta_{i}^{Mises}$ with STZs fraction of 0.2 (marked with the dashed line in Figure 13a) at $\dot{\varepsilon}=10^{8} \mathrm{~s}^{-1}, \dot{\varepsilon}=10^{9} \mathrm{~s}^{-1}$ and $\dot{\varepsilon}=10^{10} \mathrm{~s}^{-1}$ respectively, are shown in Figure 13b, where one can find that for the fixed fraction, the distribution of STZs becomes more uniform with the increase of $\dot{\varepsilon}$, attributed to that there is not sufficient time for atoms to diffuse and the free volume to be rearranged at a higher strain rate. At a higher strain rate, STZs would develop more uniformly, while at a lower strain rate, STZs would develop locally and then extend.

![](./images/812715320463589376_16.jpg)

Figure 13. (a) Fraction of atoms with relatively large atomic von Mises shear strain $\eta_{i}^{Mises}>0.2$ for ng-AlN$_{d=1 \mathrm{~nm}}$ at different strain rates with the variation of strain; (b) Distributions of von-Mises strain for ng-AlN$_{d=1 \mathrm{~nm}}$ under strain rate of $\dot{\varepsilon}=10^{8} \mathrm{~s}^{-1}, 10^{9} \mathrm{~s}^{-1}$ and $10^{10} \mathrm{~s}^{-1}$ corresponding to strain $\varepsilon=0.203$, 0.215, and 0.240, respectively.

### 4. Conclusions

We investigated using MD simulations the mechanical properties of ng-AlNs with different sizes of glassy grains, which were subjected to uniaxial tension at different temperatures and strain rates. Some conclusions were drawn as follows:

1. The volume of the atoms at the glassy interface is larger than that in the intragranular part, due to the increase of three-coordinated atoms. The type of the SRO structures in ng-AlN is the same as that in a-AlN. The fraction of four-coordinated atoms decreases while that of three-coordinated atoms increases with the increase of interface. The MRO structure in ng-AlN is relatively sparse compared with that in a-AlN, and become sparser with the increase of interface.

2. The bulk and elastic moduli of ng-AlNs are smaller than those of a-AlN. They decrease with the decrease of the grain size, so do the ultimate strengths, which can be attributed to the weak glass-glass interface. STZs are mainly activated at the glassy interface in ng-AlN, which is different from that in a-AlN. When the size of glassy grain is reduced to 1 nm, ng-AlN would exhibit super-ductility and its deformation tends to be uniform without generating voids, which can be attributed to the uniform distribution of a great many of STZs generated.

3. Temperature insignificantly affects the elastic modulus of ng-AlN, but strongly affects the ultimate strength, which follows $T^{2/3}$ scaling law for $\text{ng-AlN}_{d=1\ \text{nm}}$. The uniform diffusive flow could take place at low stress, leading to lower strength. It was also found that the higher the temperature, the larger the fraction of STZs, which could even reach nearly 82% in $\text{ng-AlN}_{d=1\ \text{nm}}$ at 600 K as $\varepsilon=0.3$.

4. The ultimate strength of ng-AlN increases with the increase of strain rate, following a power law relationship. At a higher strain rate, there is less time for atoms to diffuse and for free volume to be rearranged, which may lead to the smaller available free volume inducing higher stress for the activation of STZ. Although at the initial deformation stage the number of STZs decreases with the increase of the strain rate, the number of STZs at a higher strain rate would exceed that at a lower strain rate.

Author Contributions: Y.Z., X.P. conceived and designed the simulations. Y.Z., C.H., and B.Y. analysed the data. Y.Z. wrote the paper. X.P., N.H., and M.W. reviewed the paper.

Funding: This research was funded by the National Natural Science Foundation of China (Grant No. 11932004).

Acknowledgments: The authors gratefully acknowledge the financial support from the National Natural Science Foundation of China (Grant No. 11932004).

Conflicts of Interest: The authors declare no conflict of interest.

### References

1. Levinshtein, M.E.; Rumyantsev, S.L.; Shur, M.S. *Properties of Advanced Semiconductor Materials: GaN, AlN, InN, BN, SiC, SiGe*; Wiley: New York, NY, USA, 2001.

2. Slack, G.A. Nonmetallic crystals with high thermal conductivity. *J. Phys. Chem. Solids* **1973**, *34*, 321–335. [CrossRef]

3. Slack, G.A.; Tanzilli, R.A.; Pohl, R.O.; Vandersande, J.W. The intrinsic thremal conductivity of AlN. *J. Phys. Chem. Solids* **1987**, *48*, 641–647. [CrossRef]

4. Slack, G.A.; Bartram, S.F. Thermal expansion of some diamondlike crystals. *J. Appl. Phys.* **1975**, *46*, 89–98. [CrossRef]

5. Yim, W.M.; Paff, R.J. Thermal expansion of AlN, sapphire, and silicon. *J. Appl. Phys.* **1974**, *45*, 1456–1457. [CrossRef]

6. Chin, V.W.L.; Tansley, T.L.; Osotchan, T. Electron mobilities in gallium, indium, and aluminum nitrides. *J. Appl. Phys.* **1994**, *75*, 7365–7372. [CrossRef]

7. Davidge, R.W. Mechanical properties of ceramic materials. *Contemp. Phys.* **1969**, *10*, 105–124. [CrossRef]

8. Heard, H.C.; Cline, F.C. Mechanical behaviour of polycrystalline BeO, $\text{Al}_2\text{O}_3$ and AlN at high pressure. *J. Mater. Sci.* **1980**, *15*, 1889–1897. [CrossRef]

9. Guo, J.J.; Reddy, K.M.; Hirata, A.; Fujita, T.; Gazonas, G.A.; McCauley, J.W.; Chen, M.W. Sample size induced brittle-to-ductile transition of single-crystal aluminum nitride. *Acta Mater.* 2015, 88, 252–259. [CrossRef]

10. Xu, X.; Wang, Y.; Guo, A.; Geng, H.; Ren, S.; Tao, X.; Liu, J. Enhanced plasticity by nanocrystallite in bulk amorphous $Al_2O_3$-$ZrO_2$-$Y_2O_3$. *Int. J. Plast.* 2016, 79, 314–327. [CrossRef]

11. Gandhi, A.S.; Jayaram, V. Plastically deforming amorphous $ZrO_2$-$Al_2O_3$. *Acta Mater.* 2003, 51, 1641–1649. [CrossRef]

12. Paul, A.; Jayaram, V. Deformation and structural densification in $Al_2O_3$-$Y_2O_3$ glass. *Acta Mater.* 2011, 59, 82–92. [CrossRef]

13. Zhao, Y.; Peng, X.; Fu, T.; Huang, C.; Xiang, H.; Hu, N.; Yan, C. Investigation of mechanical behaviour of amorphous aluminium nitride. *Materialia* 2018, 2, 148–156. [CrossRef]

14. Gleiter, H. Nanoglasses: A new kind of noncrystalline material and the way to an age of new technologies? *Small* 2016, 12, 2225–2233. [CrossRef] [PubMed]

15. Jing, J.; Kramer, A.; Birringer, R.; Gleiter, H.; Gonser, U. Modified Atomic Structure in A Pd-Fe-Si Nanoglass A Mossbauer study. *J. Non Cryst. Solids* 1989, 113, 167–170. [CrossRef]

16. Gleiter, H.; Schimmel, T.; Hahn, H. Nanostructured solids—From nanoglasses to quantum transistors. *Nano Today* 2014, 9, 17–68. [CrossRef]

17. Fang, J.X.; Vainio, U.; Puff, W.; Wurschum, R.; Wang, X.L.; Wang, D.; Ghafari, M.; Jiang, F.; Sun, J.; Hahn, H.; et al. Atomic structure and structural stability of $Sc_{75}Fe_{25}$ nanoglasses. *Nano Lett.* 2012, 12, 458–463. [CrossRef]

18. Șopu, D.; Ritter, Y.; Gleiter, H.; Albe, K. Deformation behavior of bulk and nanostructured metallic glasses studied via molecular dynamics simulations. *Phys. Rev. B* 2011, 83, 100202. [CrossRef]

19. Adibi, S.; Sha, Z.-D.; Branicio, P.S.; Joshi, S.P.; Liu, Z.-S.; Zhang, Y.-W. A transition from localized shear banding to homogeneous superplastic flow in nanoglass. *Appl. Phys. Lett.* 2013, 103, 211905. [CrossRef]

20. Sha, Z.D.; Branicio, P.S.; Pei, Q.X.; Liu, Z.S.; Lee, H.P.; Tay, T.E.; Wang, T.J. Strong and superplastic nanoglass. *Nanoscale* 2015, 7, 17404–17409. [CrossRef]

21. Chen, N.; Louzguine-Luzgin, D.V.; Xie, G.Q.; Sharma, P.; Perepezko, J.H.; Esashi, M.; Yavari, A.R.; Inoue, A. Structural investigation and mechanical properties of a representative of a new class of materials: Nanograined metallic glasses. *Nanotechnology* 2013, 24, 045610. [CrossRef]

22. Wang, J.Q.; Chen, N.; Liu, P.; Wang, Z.; Louzguine-Luzgin, D.V.; Chen, M.W.; Perepezko, J.H. The ultrastable kinetic behavior of an Au-based nanoglass. *Acta Mater.* 2014, 79, 30–36. [CrossRef]

23. Ivanisenko, Y.; Kübel, C.; Nandam, S.H.; Wang, C.; Mu, X.; Adjaoud, O.; Albe, K.; Hahn, H. Structure and Properties of Nanoglasses. *Adv. Eng. Mater.* 2018, 20, 1800404. [CrossRef]

24. Kushima, A.; Liu, X.H.; Zhu, G.; Wang, Z.L.; Huang, J.Y.; Li, J. Leapfrog cracking and nanoamorphization of ZnO nanowires during in situ electrochemical lithiation. *Nano Lett.* 2011, 11, 4535–4541. [CrossRef] [PubMed]

25. Zhao, Y.; Peng, X.; Fu, T.; Huang, C.; Feng, C.; Yin, D.; Wang, Z. Molecular dynamics simulation of nano-indentation of (111) cubic boron nitride with optimized Tersoff potential. *Appl. Surf. Sci.* 2016, 382, 309–315. [CrossRef]

26. Zhao, Y.; Peng, X.; Fu, T.; Zhu, X.; Hu, N.; Yan, C. Strengthening mechanisms of graphene coated copper under nanoindentation. *Comput. Mater. Sci.* 2018, 144, 42–49. [CrossRef]

27. Fu, T.; Peng, X.; Huang, C.; Zhao, Y.; Weng, S.; Chen, X.; Hu, N. Effects of twin boundaries in vanadium nitride films subjected to tensile/compressive deformations. *Appl. Surf. Sci.* 2017, 426, 262–270. [CrossRef]

28. Huang, C.; Peng, X.; Yang, B.; Zhao, Y.; Xiang, H.; Chen, X.; Li, Q.; Fu, T. Molecular dynamics simulations for responses of nanotwinned diamond films under nanoindentation. *Ceram. Int.* 2017, 43, 16888–16894. [CrossRef]

29. Zhao, Y.; Peng, X.; Huang, C.; Fu, T.; Yang, B.; Hu, N.; Xi, Y.; Yan, C. Notch effects on deformation of crystalline and amorphous AlN—A nanoscale study. *Ceram. Int.* 2019, 45, 907–917. [CrossRef]

30. Plimpton, S. Fast parallel algorithms for short-range molecular dynamics. *J. Comput. Phys.* 1995, 117, 1–19. [CrossRef]

31. Vashishta, P.; Kalia, R.K.; Nakano, A.; Rino, J.P. Interaction potential for aluminum nitride: A molecular dynamics study of mechanical and thermal properties of crystalline and amorphous aluminum nitride. *J. Appl. Phys.* 2011, 109, 033514. [CrossRef]

32. Xiang, H.; Li, H.; Fu, T.; Huang, C.; Peng, X. Formation of prismatic loops in AlN and GaN under nanoindentation. *Acta Mater.* **2017**, *138*, 131–139. [CrossRef]

33. Branicio, P.S.; Nakano, A.; Kalia, R.K.; Vashishta, P. Shock loading on AlN ceramics: A large scale molecular dynamics study. *Int. J. Plast.* **2013**, *51*, 122–131. [CrossRef]

34. Brostow, W.; Dussault, J.; Fox, B. Construction of voronoi polyhedral. *J. Comput. Phys.* **1978**, *29*, 81–92. [CrossRef]

35. Adelman, S.A.; Doll, J.D. Generalized Langevin equation approach for atom/solid-surface scattering: General formulation for classical scattering off harmonic solids. *J. Chem. Phys.* **1976**, *64*, 2375–2388. [CrossRef]

36. Tsai, D.H. The virial theorem and stress calculation in molecular dynamics. *J. Chem. Phys.* **1979**, *70*, 1375–1382. [CrossRef]

37. Shimizu, S.O.F.; Li, J. Theory of Shear Banding in Metallic Glasses and Molecular Dynamics Calculations. *Mater. Trans.* **2007**, *48*, 2923–2927. [CrossRef]

38. Stukowski, A. Visualization and analysis of atomistic simulation data with OVITO–the Open Visualization Tool. *Model. Simul. Mater. Sci. Eng.* **2010**, *18*, 015012. [CrossRef]

39. Durandurdu, M. Uncovering Nanoclusters in Amorphous AlN: An Ab Initio Study. *J. Am. Ceram. Soc.* **2015**, *98*, 1095–1098. [CrossRef]

40. Sheng, H.W.; Luo, W.K.; Alamgir, F.M.; Bai, J.M.; Ma, E. Atomic packing and short-to-medium-range order in metallic glasses. *Nature* **2006**, *439*, 419–425. [CrossRef]

41. Schuh, C.; Hufnagel, T.; Ramamurty, U. Mechanical behavior of amorphous alloys. *Acta Mater.* **2007**, *55*, 4067–4109. [CrossRef]

42. Johnson, W.L.; Samwer, K. A universal criterion for plastic yielding of metallic glasses with a $(T/T_g)^{2/3}$ temperature dependence. *Phys. Rev. Lett.* **2005**, *95*, 195501. [CrossRef] [PubMed]

43. Yao, L.; Jin, Z.-H. Stagnation accommodated global plasticity in nanoglass composites. *Scr. Mater.* **2015**, *106*, 46–51. [CrossRef]

44. Cowper, G.R.; Symonds, P.S. Strain hardening and strain rate effect in the impact loading of cantilever beams. *Small Bus. Econ.* **1957**, *31*, 235–263.

45. Li, M.C.; Jiang, M.Q.; Li, G.; He, L.; Sun, J.; Jiang, F. Ductile to brittle transition of fracture of a Zr-based bulk metallic glass: Strain rate effect. *Intermetallics* **2016**, *77*, 34–40. [CrossRef]

46. Li, M.C.; Jiang, M.Q.; Yang, S.; Jiang, F.; He, L.; Sun, J. Effect of strain rate on yielding strength of a Zr-based bulk metallic glass. *Mater. Sci. Eng. A* **2017**, *680*, 21–26. [CrossRef]

![](./images/812715320463589376_17.jpg)

© 2019 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (http://creativecommons.org/licenses/by/4.0/).
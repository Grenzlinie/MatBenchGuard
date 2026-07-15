# A feasibility study on the fracture strength measurement of polycrystalline graphene using nanoindentation with a cylindrical indenter
Jihoon Han $^{a}$ , Seunghwa Ryu $^{b, *}$ , Dongwoo Sohn $^{c, * *}$

$^{a}$ Research Reactor Utilization Department, Korea Atomic Energy Research Institute, 989-111 Daedeok-daero, Yuseong-gu, Daejeon 34057, Republic of Korea
$^{b}$ Department of Mechanical Engineering, Korea Advanced Institute of Science and Technology (KAIST), 291 Daehak-ro, Yuseong-gu, Daejeon 34141, Republic of Korea
$^{c}$ Division of Mechanical Engineering, College of Engineering, Korea Maritime and Ocean University, 727 Taejong-ro, Yeongdo-gu, Busan 49112, Republic of Korea

---

## ARTICLE INFO
Article history:
Received 27 February 2016
Received in revised form
1 June 2016
Accepted 2 June 2016
Available online 3 June 2016

## ABSTRACT
The strength of pristine graphene and its grain boundaries (GBs) are mainly measured by nano- indentation with a spherical tip due to the difficulty of conducting uniaxial tensile tests. However, we recently showed that the fracture forces from the spherical indenter cannot be directly mapped onto the uniaxial strength. In this paper, employing a series of molecular dynamics simulations combined with a fracture mechanics analysis, we demonstrate that the fracture force from cylindrical indenters can be directly mapped onto the strength of graphene under uniaxial tension. Under indentation with cylin- drical tips or uniaxial tension, the rupture of graphene sheets that have GBs with a low-tilt angle occurs simultaneously with the onset of crack nucleation at the GBs. On the contrary, when indented by a spherical indenter tip, the graphene sheets sustain the indentation loads until the crack size becomes comparable to the tip radius. Furthermore, the results show that estimating the strength with a cylin- drical indenter is not very sensitive to the indentation site as well as angular misalignments that can be caused by human error or the limitations of the apparatus. Our work presents the feasibility of obtaining the tensile strength from nanoindentation experiments, which may suggest a new standard to measure the tensile strength of graphene and related two-dimensional materials.

© 2016 Elsevier Ltd. All rights reserved.

---

## 1. Introduction
Due to the exceptional mechanical [1-3], thermal [4], and electronic properties [5-9], pristine graphene has attracted extensive research attention, as a building block of highly robust and efficient devices. However, it is still a challenging work to synthesize a large-area single crystal graphene sheet which would exhibit theoretically predicted superior properties. Chemical vapor deposition (CVD) [10-12] is the most popular method to produce large-area graphene, which inevitably leads to polycrystalline graphene containing grain boundaries (GBs) composed of an array of pentagon-heptagon (5-7) defects and vacancies [13-17].

Many experimental, theoretical, and computational studies have been performed to examine the effect of GBs on the strength of CVD-synthesized graphene, with uniaxial tensile testing [18-25] and nanoindentation testing [9,26-34]. Most works reported that the strength of polycrystalline graphene is lower than that of pristine graphene [19-24]. Theoretical and computational studies explained that the weakening of the CVD-synthesized graphene is caused by the dipolar pre-stress induced by 5-7 defects along GBs [21-24]. However, Lee et al. [26] reported an experimental study of nanoindentation suggesting that the strengths of polycrystalline graphene are comparable to the strength of pristine graphene regardless of the misorientation angle of GBs, which is inconsistent with theoretical predictions. In contrast, other nanoindentation studies [27,28] revealed that strengths of polycrystalline graphene depend on the mismatch angle and that higher angle GBs have higher strength; these experimental results are in good agreement with theoretical predictions.

A direct way for resolving the controversy is to perform the

---
* Corresponding author.
** Corresponding author.
E-mail addresses: ryush@kaist.ac.kr (S. Ryu), dsohn@kmou.ac.kr (D. Sohn).

http://dx.doi.org/10.1016/j.carbon.2016.06.004
0008-6223/© 2016 Elsevier Ltd. All rights reserved.

![](./images/811267415085154304_1.jpg)
![](./images/811267415085154304_2.jpg)
![](./images/811267415085154304_3.jpg)

uniaxial tension test on CVD-synthesized graphene. However, it has been prohibitively difficult to clamp ends of the atomically thin graphene sheet with a superior degree of alignment required for the uniaxial tension test. Hence, some molecular dynamics simu- lation studies have been performed to examine the validity of nanoindentation test for measuring the tensile strength, because the stress distributions of indentation and uniaxial tension are very different [30-32]. Those studies found that the fracture load criti- cally depends on the indentation site because of the highly concentrated stress distribution around the spherical indenter tip, and that the failure mechanism of polycrystalline graphene with GBs differs from that of uniaxial tensile simulations [32]. Fracture in tensile loading occurs simultaneously with the onset of crack nucleation. In contrast, graphene sheets often sustain indentation loads after cracks nucleate due to stable crack growth originating from the quickly decaying stress field, which is inversely propor- tional to the distance from the indenter tip.

Hence, a new method should be developed to reduce the large scattering of the failure load and to more reliably predict the uni- axial tensile properties for two-dimensional (2D) materials. In a recent experimental study, wedge indentation [35,36] was carried out to measure the mechanical properties of a suspended graphene ribbon device. The wedge tip led to uniform strain over the entire graphene sheet, as in uniaxial tensile testing. This approach shows the feasibility of a mechanical testing by which the tensile prop- erties of 2D materials and ultra-thin films can be measured. Much research [37,38] is performed to measure the mechanical behaviors of graphene using wedge indentation. However, the GB effect on the mechanical strength of polycrystalline graphene measured by the wedge indentation test has not yet been reported, in both experimental and theoretical studies.

Recently mechanical behaviors of carbon materials, such as graphene and carbon nanotube, under various loading conditions have been investigated by using molecular dynamics simulations [39,40]. In this study, by employing a series of molecular dynamics simulations combined with a fracture mechanics analysis, we propose nanoindentation using a cylindrical tip as an alternative to the spherical indenter tip, which inherently involves significant variation in strength estimation. A cylindrical indenter can be regarded as an approximation of the tip of wedge indenter used in experiments [35,36], unless the tip of wedge is atomically sharp. As shown in the later part, the mechanical responses barely depend on the radius of cylinder down to 1 nm. Thus, we belive that the cy- lindrical indentation in this study can be directly compared to an experimental wedge indentation with different radius of curvature at the tip. The cylindrical indenter tip generates uniform in-plane stress over the entire area of graphene, which is very similar to the case of uniaxial tension. Additionally, in both uniaxial and cy- lindrical indentation simulations, fractures occur simultaneously with the onset of crack nucleation near 5-7 defects. Indeed, we show that the failure force from nanoindentation with the cylin- drical tip can be directly mapped onto the uniaxial strength and comparable to the uniaxial strength. Furthermore, the results show that estimating the strength with a cylindrical indenter is not very sensitive to the indentation site and angular misalignments that can be caused by human error or limitations of the apparatus. Our findings imply that cylindrical indentation can be used as an alternative experimental method to measure the uniaxial tensile strength, and this method is suitable to investigate the dependency of the strength on the misorientation angle in polycrystalline graphene.

## 2. Computational methods

We first prepare square bi-crystalline graphene sheets containing symmetric tilt GBs, as depicted in Fig. 1. Zigzag-oriented graphene sheets are also created by varying the misorientation angle between $0^{\circ}$ and $28^{\circ}$ (see Fig. 1), and armchair-oriented gra phene sheets are created by varying the misorientation angle be- tween $0^{\circ}$ and $22^{\circ}$ (see Fig. S1 in Section S1 of the Supplementary Materials). The dimensions of the sheets are $50 ~nm \times 50 ~nm$, which are sufficiently wider than the range of the local pre-stress fields of GBs.

Using the prepared graphene samples, molecular dynamics simulations are performed by employing the Large-scale Atomic/ Molecular Massively Parallel Simulator (LAMMPS) package [41]. The interatomic interaction between carbon atoms in the graphene sheet is described by the adaptive intermolecular reactive empirical bond order (AIREBO) potential [42]. The cutoff radius of $r_{cc}=1.92 \AA$ is used to avoid the influence of spurious stress peaks on the fracture process [22-25]. A constant time step of $1.0 fs$ is used in all of the molecular dynamics simulations. We initially equilibrate the samples for $20 ps$ with the Nosé-Hoover barostat (NPT ensemble) at300 K, and then for 10 ps with the Nosé- Hoover thermostat (NVT ensemble) at $300 ~K$ . Subsequently, nanoindentation simulations are performed with the Nosé-Hoover thermostat at $300 ~K$ .

We use virtual indenter tips for spherical and cylindrical in- denters, which are considered rigid bodies making frictionless contact with the graphene sheets. Because graphene can serve as an ultra-thin solid-state lubricant [43,44], neglecting the frictional interaction between the indenter tip and the graphene sheet is reasonable. The friction originated from the weak van der Waals interactions is much lower than the fracture strength of graphene, and hence, its effect on the strength estimation would be negligible. Both indenters exert a force on each carbon atom given as $F(r)=-K(r-R)^{2}$ , where $K, r$ , and $R$ indicate the specific force constant, the distance from each atom to the center of the indenter, and the radius of the indenter, respectively. The non-zero value of the repulsive force can be extracted only for $r<R$ . The cylindrical indenter is extended infinitely in its longitudinal direction (i.e., the y-direction in Fig. 2(a)). In this study, a $K$ of $10 eV / \AA^{3}$ and an $R$ of50 Å are used to simulate the nanoindentation of the poly- crystalline graphene. The atoms on edges, indicated in red in Fig. 2(a) and (b), are fixed to mimic the clamped boundary condi- tions. For the cylindrical indentation tests without angular misalignment, a periodic boundary condition is applied along the y- direction in Fig. 2(a). In contrast, the periodic boundary condition is removed and the effect of stress concentration at the corner of the clamped edge is considered when we study the effect of angular misalignment. In the rupture process of graphene sheets, the atomic configurations are visualized using the Visual Molecular Dynamics package [45] and AtomEye package [46].

The indenter tips are moved down in the transverse direction(i.e., the z-direction in Fig. 2) by $0.1 \AA$ from the initial position of the indenter every 5 ps until the polycrystalline graphene fails completely, which corresponds to a loading speed of $0.02 \AA / ps$ . As the indenter gradually moves downward, the force exerted on the indenter is measured continuously, and the values are averaged over 5 ps at each deformation increment to minimize thermal fluctuations. The indentation depth is defined as the relative dis- tance between the lowest point of the tip and the initial position of the graphene sheet. Meanwhile, the stress tensor is calculated by the virial stress considering an atomic volume of $8.8 \AA^{3}[24,25]$ and a thickness of $0.34 ~nm$ .

## 3. Results and discussion

### 3.1. Nanoindentation of pristine graphene

We carry out nanoindentation on pristine graphene sheets via

![](./images/811267415085154304_4.jpg)

Fig. 1. (a)-(e) Atomic configurations of zigzag-oriented graphene in the vicinity of symmetric tilt GBs with a misorientation angle of (a) 5.7°, (b) 13.2°, (c) 17.9°, (d) 21.8°, and (e) 27.8°. The atomic configurations get from our previous study [32]. Atomic configurations of armchair-oriented graphene are presented in the Section S1 of the Supplementary Materials. The dark grey color indicates the atomic configuration of the 5-7 defects.

![](./images/811267415085154304_5.jpg)

Fig. 2. Schematic of the nanoindentation simulation using (a) a cylindrical indenter tip, and (b) a spherical indenter tip. (A color version of this figure can be viewed online.)

molecular dynamics simulations, as shown in Fig. 2. The schematic diagrams of both cylindrical and spherical nanoindentation shows the different deformation behaviors of the free suspended gra- phene sheet. We observe that the stress field obtained from cy- lindrical indenter is uniformly distributed over the entire sample (see Fig. 3(a)). The stress field distribution is similar to that of uniaxial tensile testing while the spherical indentation generates a highly concentrated stress field that decays in proportion to $1/r$, where $r$ is the distance from the center of the indenter tip, as shown in Fig. 3(b).

For both the spherical and cylindrical indenter, we obtained the stress-force curves for pristine graphene, as shown in Fig. 3(c) and (d) (see Section S2 of the Supplementary Materials for the details). Following the previous studies [32], we estimated the strengths of polycrystalline graphene by converting the fracture force to the strength using the stress-force relationship [2,26,27]. For cylindri- cal indentation, the estimated strengths of zigzag- and armchair- oriented graphene are 100 GPa and 125 GPa (see Fig. 3(c)), respectively, which are in good agreement with the previous uni- axial tensile simulations [22-24]. We find that the radius of cy- lindrical indenter barely affect the mechanical response of the graphene sheet because of uniform stress distribution (see Section S3 of the Supplementary Materials). On the contrary, the biaxial stress state of spherical indentation tests results in chirality- independent strength, and the estimated strength of pristine gra- phene is 105 GPa (see Fig. 3(d)). Therefore, to investigate the chirality-dependent strength of graphene and its uniaxial tensile properties, the nanoindentation simulation with a cylindrical tip is a better choice.

### 3.2. Nanoindentation of polycrystalline graphene

Having established the validity of both nanoindentation simu- lations for pristine graphene, we carry out nanoindentation simu- lations to examine the effect of GBs on the strength of polycrystalline graphene sheets having GBs with various tilt angles. We construct a series of symmetric tilt GBs with various tilt angles (see Fig. 1). To calculate the failure force of polycrystalline gra- phene, the GB line is placed at the center of the sample. For cy- lindrical nanoindentation, the tip position does not affect the GB strength because the cylindrical tip covers the entire GB line (See Fig. 4(a)), while the indentation site of the spherical tip along the GB line should be considered due to the uncertainty in the position of spherical indenter tip (see Fig. 4(b)).

For cylindrical indentation, force-displacement curves of zigzag- oriented graphene sheets are shown in Fig. 4(c). The results from cylindrical indentation agree well with those from uniaxial tests with molecular dynamics simulations [23], and density functional theory calculations [22] (see Fig. 4(d)) because the cylindrical indentation and uniaxial tensile simulations lead to almost iden- tical stress distributions. Hence, the cylindrical indenter can serve as an alternative to uniaxial tension for studying the effects of de- fects along the GBs such as strength enhancement and weakening [23] in detail. On the contrary, for nanoindentation with a spherical indenter, the failure forces (and estimated strength) are sensitive to the distance (D) along the GB line due to the highly concentrated stress under the tip, as described in our previous study [32]. Consequently, the estimated strength can vary up to 50%, which is significantly larger than the statistical error from thermal

![](./images/811267415085154304_6.jpg)

Fig. 3. In-plane stress distributions obtained from (a) cylindrical nanoindentation, and (b) spherical nanoindentation [32] along the central line of the graphene sheet shortly before crack nucleation. Stress versus force curves obtained from (c) cylindrical nanoindentation, and (d) spherical nanoindentation [32]. Stresses are calculated by the maximum virial stress. For cylindrical indentation, the in-plane stress corresponds to $\sigma_{xx}$, which is observed at the indentation site; for spherical indentation, the in-plane stresses are defined by the mean value of $\sigma_{xx}$ and $\sigma_{yy}$, which are also obtained at the indentation site. The stress transformation to calculate the in-plane stress is described in Section S2 of the Supplementary Materials. (A color version of this figure can be viewed online.)

fluctuations (see Fig. 4(d)), where the error bars indicate the strength minima and maxima.

To understand the observed the difference between indentation with a cylindrical tip, indentation with a spherical tip, and uniaxial tensile studies, we carefully compare the evolution of the atomic configurations of graphene sheets under each loading condition. Our previous study showed that a graphene sheet under spherical indentation often sustains a significant load beyond crack initiation (see Fig. 5(a)). The overestimation of the strength of GBs is attributed to the delay in catastrophic crack growth after crack nucleation. On the contrary, the fracture occurs right after the onset of crack nucleation in both cylindrical indentation and uniaxial tensile simulation, as depicted in Fig. 5(b) and (c), respectively. Both simulations predict catastrophic crack propagation right after crack initiation. The unstable crack growth is attributed to the homogenous stress field that provides enough driving force for catastrophic crack growth (see Section S4 of the Supplementary Materials for the details). Therefore, indentation with a cylindrical tip might serve as an alternative to uniaxial tensile testing for measuring the strength of graphene. Our findings suggest the feasibility of measuring the uniaxial tensile strength without performing a uniaxial tensile test.

### 3.3. Effects of parallel misalignment on GB strength

To examine the feasibility of the cylindrical nanoindentation test in detail, we first examine the sensitivity of the strength estimation to the offset distance between the indenter tip and GB line (see Fig. 6(a) and (b)). The failure force is estimated as a function of the distance (S) from the GB line (all force-displacement curves are presented in Fig. S6 and S7 in the Section S5 of the Supplementary Materials). Our previous study [32] found that the strength estimation increases with the distance (S) and approaches that of pristine graphene under spherical indentation when the distance becomes comparable to the indenter radius ($S > 50$ Å), as the fracture starts at the center of the spherical indenter tip (see Figs. 6(a), (c) and 7(a)). Under spherical indentation in the case of $S > 50$ Å, the GBs have no contribution on the rupture due to the sharp stress concentration around the indenter tip. For cylindrical indentation, we find that the failure forces are insensitive to the distance, regardless of the tilt angle (see Fig. 6(b) and (d) for zigzag-oriented graphene and Fig. S10(a) for armchair-oriented graphene in the Section S6 of the Supplementary Materials). Although the distance is larger than the indenter radius, the GB line is subjected to a homogenous stress field that is generated over all of the 5-7 defects along the GB line, and this stress field provides a sufficient driving force for the unstable crack growth at the GB line (see Fig. 7(b)). For cylindrical indentation, the failure always occurs at the GB line, regardless of the distance, due to the homogeneous stress field in polycrystalline graphene. Therefore, cylindrical indentation is a better estimator to predict the GB strength under uniaxial tension.

### 3.4. Effects of angular misalignment on GB strength and stress concentration at corners

Second, we study the effect of angular misalignment of the cylindrical indenter tip on the strength of GBs. Due to the inevitable

![](./images/811267415085154304_7.jpg)

Fig. 4. Schematic diagrams of (a) a cylindrical and (b) a spherical nanoindentation simulation in which the indenter tip is located on the GB line. (c) Force-displacement curves of zigzag tilt GBs with respect to the misorientation tilt angles under cylindrical indentation. (d) The strength estimation from both the nanoindentation and uniaxial tensile sim- ulations is plotted together. For spherical indentations, the strength minima and maxima are represented by error bars. The values of spherical indentation are obtained from our previous study [32]. The uniaxial tensile values are obtained from the data of molecular dynamics simulations by Wei et al. [23] and of density functional theory calculations by Grantab et al. [22]. (A color version of this figure can be viewed online.)

![](./images/811267415085154304_8.jpg)

Fig. 5. Atomic configurations of a zigzag-oriented graphene with an angle of 5.7° at various indentation depths or tensile strains. (a) Force-deflection curve from spherical nanoindentation and atomic configurations at various deflections at D = 40 Å. The spherical indentation data are obtained from our previous study [32]. (b) Force-deflection curve from cylindrical nanoindentation and atomic configurations at various deflections. (c) Stress-strain curve from uniaxial tension and atomic configurations [32] at various strains. The color contours indicate $\sigma_{xx}$. (A color version of this figure can be viewed online.)

human error or the limited accuracy of the testing apparatus, it is important to examine the cylindrical nanoindentation test's

sensitivity to the angular misalignment between the GB line and cylindrical tip. We measure the failure force as a function of both

![](./images/811267415085154304_9.jpg)

Fig. 6. Schematic diagram of nanoindentation simulations with parallel misalignment for (a) spherical indentation and (b) cylindrical indentation. Strength estimation as a function of indenter position (S) for zigzag-oriented graphene using (c) spherical indentation and (d) cylindrical indentation. The spherical indentation data are obtained from our previous study [32]. (A color version of this figure can be viewed online.)

![](./images/811267415085154304_10.jpg)

Fig. 7. Comparison of the rupture processes of spherical and cylindrical indentation. Force-deflection curve and atomic configurations of zigzag-oriented graphene with an angle of 17.9° (a) at distance (S) of 6 nm through spherical indentation, and (b) at distance (S) of 8 nm through cylindrical indentation. The color contours indicate $\sigma_{xx}$. (A color version of this figure can be viewed online.)

the in-plane angle $(\theta_{z})$ and out-of-plane angle $(\theta_{x})$ between the longitudinal axis of cylindrical indenter tip and the GB line, as depicted in Fig. 8(a) and (b). All force-displacement curves are presented in Fig. S8 and S9 in the Section S5 of the Supplementary Materials, and the results of strength estimation are shown in Fig. 8(c) and (d). For the simulation with an angular misalignment between the GB line and the axis of the cylindrical indenter, periodic boundary conditions are not applied. Hence, we consider the stress concentration effect at the corner of graphene sheets. We consider the maximum in-plane and out-of-plane angles up to 20 and 2°, respectively.

For low-tilt-angle GBs, the results shows that the strength estimation is a slowly increasing function of the in-plane misalignment angle (see Fig. 8(c)). Cracks always nucleate at the center of the indentation site and then propagate along the GB line (see Fig. 9(a) and (b)). The observed fracture behavior can be

![](./images/811267415085154304_11.jpg)

Fig. 8. (a) and (b) are schematic diagrams of the nanoindentation simulation with an in-plane angle and out-of-plane angle, respectively. Strength estimation as a function of (c) in-plane angle ($\theta_z$), and (d) out-of-plane angle ($\theta_x$) for zigzag-oriented graphene. (A color version of this figure can be viewed online.)

understood by comparing the resolved applied stress normal to the GB line and the GB strength ($\sigma_{GB}$). Cracks nucleate and grow along the GB line when the resolved applied stress ($\sigma_{app} \cos^2\theta_z$) becomes larger than the GB strength, i.e., $\sigma_{app} \geq \sigma_{GB}/\cos^2\theta_z$. Hence, the failure force and the strength estimation would increase in proportion to $1/\cos^2\theta_z$.

However, in the case of high-tilt-angle GB (tilt angle of $27.8^\circ$), the fracture initiates at the edge of graphene sheet near the clamped boundary (see Fig. 9(c)). The observed fracture behavior can be understood by comparing two fracture criterions with respect to the GB strength and the stress concentration at the clamped boundary. When the stress concentration factor is $K$ (i.e., the stress near the corner is $K\sigma_{app}$), the fracture initiates if the strength of pristine graphene ($\sigma_{pri}$) is smaller than $K\sigma_{app}$, i.e., $\sigma_{app} \geq \sigma_{pri}/K$ (see Fig. 9(d)). Hence, the fracture criterion will be given as $\sigma_{app} \geq \min[\sigma_{GB}/\cos^2\theta_z, \ \sigma_{pri}/K]$. If $\sigma_{GB}/\cos^2\theta_z < \sigma_{pri}/K$, the fracture is likely to initiate at the GB; otherwise, the graphene will start to fail at the corner. Note that $\sigma_{GB,5.7^\circ} < \sigma_{GB,13.2^\circ} < \sigma_{GB,17.9^\circ} < \sigma_{GB,21.8^\circ} < \sigma_{GB,27.8^\circ}$, as shown in Fig. 4(d). Due to the relatively low GB strength, the fracture occurs at the GB line for low-tilt-angle GBs. In contrast, the fracture of high-tilt-angle GBs (with higher strength) occurs at the corner

![](./images/811267415085154304_12.jpg)

Fig. 9. The rupture processes of zigzag-oriented graphene with different in-plane angular misalignment: symmetric tilt GBs with a tilt angle of (a) $5.7^\circ$, (b) $17.9^\circ$, (c) $27.8^\circ$, and (d) pristine graphene. The color contours indicate $\sigma_{xx}$. (A color version of this figure can be viewed online.)

![](./images/811267415085154304_13.jpg)

Fig. 10. The rupture processes of zigzag-oriented graphene with an out-of-plane angle of $2^{\circ}$: symmetric tilt GBs with (a) $5.7^{\circ}$, (b) $17.9^{\circ}$, and (c) $27.8^{\circ}$. The color contours indicate $\sigma_{xx}$.
(A color version of this figure can be viewed online.)

because the other fracture criterion is preferentially satisfied for high-tilt-angle GBs. From Fig. 9(c), we realized that the GB strength with a tilt angle of $27.8^{\circ}$ cannot be measured when we take into account the presence of corner because the crack does not initiate at the GB line even at the zero in-plane angle $(\theta_{z}=0^{\circ})$, i.e., $\sigma_{GB}>\sigma_{pri}/K$. This suggests that in laboratory experiments where such a corner effect is unavoidable, only the strength of low-tilt- angle GBs can be measured accurately.

We also investigate the effects of out-of-plane angular misalignment on strength estimation, as shown in Fig. 8(d). We limit the out-of-plane angle to within $2^{\circ}$, which is considered the maximum operator error [47]. The strength estimation shows that the strength slightly decreases with the out-of-plane angle. Similar to the in-plane misalignment angle study, failure starts from the corner for high-tilt-angle GBs (tilt angle of $27.8^{\circ}$), as depicted in Fig. 10. Thus, care must be taken in performing and interpreting the experimental results in realistic conditions.

## 4. Conclusion
In conclusion, by combining a series of molecular dynamics simulations and fracture mechanics analysis, we find that the fracture force of polycrystalline graphene measured by cylindrical indentation is more suitable than that of spherical indentation for mapping the fracture force onto the uniaxial tensile strength. Spherical indentation results in sharp stress concentration around the indenter tip and overestimates the strength of polycrystalline graphene. On the contrary, cylindrical indentation generates a uniform in-plane stress field over the entire graphene sheet, as in the uniaxial tensile test. In addition, we demonstrate that esti- mating the strength using cylindrical indentations is not very sensitive to the indentation site and the angular misalignments that can be caused by human error in testing or limitations of the apparatus. Therefore, our findings suggest the feasibility of substituting cylindrical indentation for uniaxial tensile testing to measure the strength of graphene or related 2D materials.

Unfortunately, due to the stress concentrations at the corner, we find that it is very difficult to measure the strength of high-tilt- angle GBs or pristine graphene by the cylindrical indentation tests, while the spherical indentation tests can be performed without much concern on the boundary effect because of high stress concentration near the indenter tip [32]. However, this lim- itation can be overcome by creating graphene sheets with a dog- bone-like geometry via laser cutting, as in the case of the uniaxial tension. The effects of laser cutting or oxidation on the graphene edges on the strength estimation will be the subject of our future study. In addition, a cylindrical indentation study on the strength estimation of polycrystalline graphene with three or more grains is currently in progress and will be reported in the future study.

## Acknowledgments
This research was supported by Basic Science Research Program through the National Research Foundation of Korea (NRF) funded by the Ministry of Education (2014R1A1A2058549) and by the Korean government (MSIP:Ministry of Science, ICT and Future Planning) (2012M2A2A6004262 and 2016M3D1A1900038).

## Appendix A. Supplementary data
Supplementary data related to this article can be found at http:// dx.doi.org/10.1016/j.carbon.2016.06.004.

## References
[1] J.S. Bunch, A.M. van der Zande, S.S. Verbridge, I.W. Frank, D.M. Tanenbaum, J.M. Parpia, et al., Electromechanical resonators from graphene sheets, Science315 (5811) (2007) 490-493.
[2] C. Lee, X.D. Wei, J.W. Kysar, J. Hone, Measurement of the elastic properties andintrinsic strength of monolayer graphene, Science 321 (5887) (2008)385-388.
[3] S.P. Koenig, N.G. Boddeti, M.L. Dunn, J.S. Bunch, Ultrastrong adhesion of gra- phene membranes, Nat. Nanotechnol. 6 (9) (2011) 543-546.
[4] A.A. Balandin, S. Ghosh, W. Bao, I. Calizo, D. Teweldebrhan, F. Miao, et al.,Superior thermal conductivity of single-layer graphene, Nano Lett. 8 (3)(2008) 902-907.
[5] K.S. Novoselov, A.K. Geim, S.V. Morozov, D. Jiang, Y. Zhang, S.V. Dubonos, et al., Electric field effect in atomically thin carbon films, Science 306 (5696)(2004)666-669.
[6] K.S. Novoselov, A.K. Geim, S.V. Morozov, D. Jiang, M.I. Katsnelson, I.V. Grigorieva, et al., Two-dimensional gas of massless Dirac fermions in graphene, Nature 438 (7065)(2005) 197-200.
[7] Y. Zhang, Y.-W. Tan, H.L. Stormer, P. Kim, Experimental observation of thequantum Hall effect and Berry's phase in graphene, Nature 438 (7065) (2005)201-204
[8] A.K. Geim, K.S. Novoselov, The rise of graphene, Nat. Mater. 6 (3) (2007)183-191.
[9] Y. Wang, Z. Song, Z. Xu, Characterizing phonon thermal conduction in poly- crystalline graphene, J. Mater. Res. 29 (03) (2014) 362-372.
[10] Q.K. Yu, J. Lian, S. Siriponglert, H. Li, Y.P. Chen, S.S. Pei, Graphene segregated onNi surfaces and transferred to insulators, Appl. Phys. Lett. 93 (11) (2008)113103.
[11] A. Reina, X.T. Jia, J. Ho, D. Nezich, H.B. Son, V. Bulovic, et al, Large area, few- layer graphene films on arbitrary substrates by chemical vapor deposition,Nano Lett. 9 (1) (2009) 30-35
[12] Y. Lee, S. Bae, H. Jang, S. Jang, S.E. Zhu, S.H. Sim, et al, Wafer-scale synthesis and transfer of graphene films, Nano Lett. 10 (2) (2010) 490-493.
[13] J. Avila, I. Razado, S. Lorcy, R. Fleurier, E. Pichonat, D. Vignaud, et al, Exploring electronic structure of one-atom thick polycrystalline graphene films: a nano angle resolved photoemission study, Sci. Rep. 3 (2013) 2439.
[14] J.C. Meyer, A.K. Geim, M.I. Katsnelson, K.S. Novoselov, T.J. Booth, S. Roth, The structure of suspended graphene sheets, Nature 446 (7131) (2007) 60-63.
[15] P.Y. Huang, C.S. Ruiz-Vargas, A.M. van der Zande, W.S. Whitney, M.P. Levendorf, J.W. Kevek, et al., Grains and grain boundaries in single-layer graphene atomic patchwork quilts, Nature 469 (7330) (2011) 389-392.
[16] K. Kim, Z. Lee, W. Regan, C. Kisielowski, M.F. Crommie, A. Zettl, Grainboundary mapping in polycrystalline graphene, ACS Nano 5 (3) (2011)2142-2146.
[17] K. Kim, V.I. Artyukhov, W. Regan, Y.Y. Liu, M.F. Crommie, B.I. Yakobson, et al., Ripping graphene: preferred directions, Nano Lett. 12 (1) (2012) 293-297.
[18] L.J. Yi, Z.N. Yin, Y.Y. Zhang, T.C. Chang, A theoretical evaluation of the

temperature and strain-rate dependent fracture strength of tilt grain boundaries in graphene, Carbon 51 (2013) 373-380.

[19] Y.I. Jhon, S.E. Zhu, J.H. Ahn, M.S. Jhon, The mechanical responses of tilted and non-tilted grain boundaries in graphene, Carbon 50 (10) (2012) 3708-3716.

[20] J.F. Zhang, J.J. Zhao, J.P. Lu, Intrinsic strength and failure behaviors of graphene grain boundaries, ACS Nano 6 (3) (2012) 2704-2711.

[21] L. Yi, Z. Yin, Y. Zhang, T. Chang, A theoretical evaluation of the temperature and strain-rate dependent fracture strength of tilt grain boundaries in gra- phene, Carbon 51 (0) (2013) 373-380.

[22] R. Grantab, V.B. Shenoy, R.S. Ruoff, Anomalous strength characteristics of tilt grain boundaries in graphene, Science 330 (6006) (2010) 946-948.

[23] Y.J. Wei, J.T. Wu, H.Q. Yin, X.H. Shi, R.G. Yang, M. Dresselhaus, The nature of strength enhancement and weakening by pentagon-heptagon defects in graphene, Nat. Mater. 11 (9) (2012) 759-763.

[24] T.H. Liu, C.W. Pao, C.C. Chang, Effects of dislocation densities and distributions on graphene grain boundary failure strengths from atomistic simulations, Carbon 50 (10) (2012) 3465-3472.

[25] J. Han, S. Ryu, D. Sohn, S. Im, Mechanical strength characteristics of asym- metric tilt grain boundaries in graphene, Carbon 68 (2014) 250-257.

[26] G.H. Lee, R.C. Cooper, S.J. An, S. Lee, A. van der Zande, N. Petrone, et al., High- strength chemical-vapor deposited graphene and grain boundaries, Science 340 (6136) (2013) 1073-1076.

[27] H.I. Rasool, C. Ophus, W.S. Klug, A. Zettl, J.K. Gimzewski, Measurement of the intrinsic strength of crystalline and polycrystalline graphene, Nat. Commun. 4 (2013) 2811.

[28] C.S. Ruiz-Vargas, H.L.L. Zhuang, P.Y. Huang, A.M. van der Zande, S. Garg, P.L. McEuen, et al., Softened elastic response and unzipping in chemical vapor deposition graphene membranes, Nano Lett. 11 (6) (2011) 2259-2263.

[29] L.X. Zhou, Y.G. Wang, G.X. Cao, Van der Waals effect on the nanoindentation response of free standing monolayer graphene, Carbon 57 (2013) 357-362.

[30] Z.D. Sha, Q. Wan, Q.X. Pei, S.S. Quek, Z.S. Liu, Y.W. Zhang, et al., On the failure load and mechanism of polycrystalline graphene by nanoindentation, Sci. Rep. 4 (2014) 7437.

[31] Z. Song, V.I. Artyukhov, J. Wu, B.I. Yakobson, Z. Xu, Defect-detriment to gra- phene strength is concealed by local probe: the topological and geometrical effects, ACS Nano 9 (1) (2015) 401-408.

[32] J. Han, N.M. Pugno, S. Ryu, Nanoindentation cannot accurately predict the tensile strength of graphene or other 2D materials, Nanoscale 7 (38) (2015) 15672-15679.

[33] L. Ruiz, W. Xia, Z. Meng, S. Keten, A coarse-grained model for the mechanical behavior of multi-layer graphene, Carbon 82 (2015) 103-115.

[34] X. Wei, Z. Meng, L. Ruiz, W. Xia, C. Lee, J.W. Kysar, et al., Recoverable slippage mechanism in multilayer graphene leads to repeatable energy dissipation, ACS Nano 10 (2) (2016) 1820-1828.

[35] M. Huang, T.A. Pascal, H. Kim, W.A. Goddard, J.R. Greer, Electronic-mechanical coupling in graphene from in situ nanoindentation experiments and multi- scale atomistic simulations, Nano Lett. 11 (3) (2011) 1241-1246.

[36] E.G. Herbert, W.C. Oliver, M.P. de Boer, G.M. Pharr, Measuring the elastic modulus and residual stress of freestanding thin films using nanoindentation techniques, J. Mater. Res. 24 (09) (2009) 2974-2985.

[37] Z. Lixin, W. Yugang, C. Guoxin, Estimating the elastic properties of few-layer graphene from the free-standing indentation response, J. Phys. Condens. Matter 25 (47) (2013) 475301.

[38] S.Y. Kim, S.-Y. Cho, J.W. Kang, O.K. Kwon, Molecular dynamics simulation study on mechanical responses of nanoindented monolayer-graphene-nano- ribbon, Phys. E Low Dimens. Syst. Nanostruct. 54 (2013) 118-124.

[39] F.W. Sun, H. Li, K.M. Liew, Compressive mechanical properties of carbon nanotubes encapsulating helical copper nanowires, Carbon 48 (5) (2010) 1586-1591.

[40] F.W. Sun, H. Li, Torsional strain energy evolution of carbon nanotubes and their stability with encapsulated helical copper nanowires, Carbon 49 (4) (2011) 1408-1415.

[41] S. Plimpton, Fast parallel algorithms for short-range molecular-dynamics, J. Comput. Phys. 117 (1) (1995) 1-19.

[42] S.J. Stuart, A.B. Tutein, J.A. Harrison, A reactive potential for hydrocarbons with intermolecular interactions, J. Chem. Phys. 112 (14) (2000) 6472-6486.

[43] D. Berman, A. Erdemir, A.V. Sumant, Graphene: a new emerging lubricant, Mater. Today 17 (1) (2014) 31-42.

[44] K.-S. Kim, H.-J. Lee, C. Lee, S.-K. Lee, H. Jang, J.-H. Ahn, et al., Chemical vapor deposition-grown graphene: the thinnest solid lubricant, ACS Nano 5 (6) (2011) 5107-5114.

[45] W. Humphrey, A. Dalke, K. Schulten, VMD: visual molecular dynamics, J. Mol. Graph 14 (1) (1996) 33-38.

[46] J. Li, AtomEye: an efficient atomistic configuration viewer, Model Simul. Mater Sci. Eng. 11 (2) (2003) 173-177.

[47] J.-F. Song, S. Low, D. Pitchure, A. Germak, S. DeSogus, T. Polzin, et al., Estab- lishing a worldwide unified Rockwell hardness scale using standard diamond indenters, Measurement 24 (4) (1998) 197-205.
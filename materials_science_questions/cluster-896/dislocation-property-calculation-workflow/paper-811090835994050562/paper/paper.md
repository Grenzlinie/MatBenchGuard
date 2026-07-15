Full length article

# Non-Schmid response of $Fe_3Al$: The twin-antitwin slip asymmetry and non-glide shear stress effects

S. Alkan, H. Sehitoglu*

Department of Mechanical Science and Engineering, University of Illinois at Urbana-Champaign, Urbana, IL 61801, USA

---

## ARTICLE INFO
Article history:
Received 24 September 2016
Received in revised form
30 November 2016
Accepted 11 December 2016
Available online xxx

Keywords:
Schmid law
Non-glide stresses
DIC
Atomistic modelling
$Fe_3Al$

## ABSTRACT
The non-Schmid effects in $DO_3$ ordered $Fe_3Al$ ($DO_3$-$Fe_3Al$) are investigated by utilizing experimental measurements of the onset of slip and atomistic scale simulations to study slip directionality and core effects. Uniaxial tension and compression experiments were conducted on $DO_3$-$Fe_3Al$ single crystals utilizing high resolution Digital Image Correlation (DIC) to measure local slip strain evolution. The measured critical resolved shear stress (CRSS) values exhibited close agreement with the theoretical values upon developing a modified Peierls-Nabarro (P-N) formalism relying on molecular dynamics (MD) simulation results. Both experimental and theoretical values indicate the break-down of Schmid Law due to two factors: the role of non-glide shear (NGS) stress component acting on the glide plane, called the NGS effect, and twinning-antitwinning asymmetry, termed the TA effect. To ascertain the role of NGS stress component on the dislocation core structures, molecular statics (MS) simulations were conducted upon imposing elastic-anisotropic dislocation displacement fields with Eshelby-Stroh formalism. Both experimental measurements and modified P-N calculations confirm that the applied NGS stress component is as important as TA slip asymmetry on the break-down of Schmid Law in CRSS values. The calculated core spreading suggests that the extent of the relative displacements on $\{ 110\}$ family planes, favoring either twinning or antitwinning shear, can significantly contribute to the non-Schmid behavior of $DO_3$-$Fe_3Al$ with the accompanying elastic shear coupling between NGS stress component and glide shear (GS) strain. Further extension of the modified P-N formalism towards yielding behavior at continuum scale is also discussed.

© 2016 Acta Materialia Inc. Published by Elsevier Ltd. All rights reserved.

---

### 1. Introduction
The conventional Schmid Law implies the existence of a constant CRSS magnitude. The CRSS concept, which is assumed to be independent of slip system orientation and the sense of loading, has served the community well [1]. However, it is well established that CRSS values of body centered cubic (bcc) structured pure metals do not obey the Schmid Law [2,3]. Two reasons for the deviation from Schmid Law are known to be responsible but are not well understood: they are (i) twin-antitwin slip asymmetry (TA) and (ii) non-glide shear (NGS) stress effects which we explain below step by step.

Firstly, the CRSS along the $<111>$ direction on $\{ 112\}$ glide planes depends on the twining or antitwinning direction of slip [4]. This phenomenon is called as twin-antitwin slip asymmetry, hereafter denoted as TA effect [5,6]. The magnitude of this asymmetry may vary due to the specific electron configuration or bonding type present and is reflected on the topology of Generalized Stacking Fault Energy (GSFE), or $\gamma$, surface [7,8]. The quantitative extent of this asymmetry can be established by the atomistic simulations such as Molecular Dynamics (MD) or Molecular Statics (MS).

Secondly, the applied shear stress components couple with the non-planar core structure of screw dislocations regardless of whether or not they exert Peach-Koehler force [4,9,10]. This coupling transforms the core structures from a sessile to glissile configuration for the screw dislocation to move [9,11-13]. The reaction coordinates of this transformation is a function of the applied stress tensor components, including both the GS (glide shear) and NGS (non-glide shear) stress components, i.e. $\Sigma_{GS}$ and $\Sigma_{NGS}$, which act along a parallel and perpendicular direction to the Burgers' vector on the active glide plane respectively [14,15]. The effect of $\Sigma_{NGS}$ on the critical value of $\Sigma_{GS}$ at the instant of slip

* Corresponding author.
E-mail address: huseyin@illinois.edu (H. Sehitoglu).

http://dx.doi.org/10.1016/j.actamat.2016.12.019
1359-6454/© 2016 Acta Materialia Inc. Published by Elsevier Ltd. All rights reserved.

Please cite this article in press as: S. Alkan, H. Sehitoglu, Non-Schmid response of $Fe_3Al$: The twin-antitwin slip asymmetry and non-glide shear stress effects, Acta Materialia (2016), http://dx.doi.org/10.1016/j.actamat.2016.12.019

initiation, i.e. equal to CRSS, can be revealed by studying the dislocation core displacements with MS simulations. To that end, superpartial screw dislocations are created by the relaxation of a derived anisotropic displacement field inside a designated simulation box. We will demonstrate both TA and NGS effects rigorously in this paper in an attempt to unravel the causes of non-Schmid behavior in an ordered bcc-based alloy.

The bcc-based ordered structures, e.g. DO₃, B2, L2₁, are also known to exhibit non-Schmid behavior [16-20]. In these structures, the dislocations are dissociated into their partials unlike pure bcc metals. Thus, the nature of the underlying mechanisms are more complicated because of the mutual interactions. As stated earlier, our main focus in this study be will be the non-Schmid plastic behavior of DO₃-Fe₃Al which is an intermetallic exhibiting superelastic behavior due to reversible slip [21-25]. In DO₃ structured metallic materials, plastic strain is accommodated by the glide of $<111>$ superdislocations which are dissociated into four $1/4<111>$ superpartials. These partials are separated by Nearest Neighbor Anti Phase Boundary (NNAPB) and Next Nearest Neighbor Anti Phase Boundary (NNNAPB) faults [26,27].

Recently, the present authors reported the CRSS values attained by the first principle, Density Functional Theory (DFT) calculations on DO₃-Fe₃Al. Fig. 1(a), adopted from this aforementioned study, illustrates the asymmetry in $<111>$ cross sections of $\gamma$ curves on planes exhibiting the break-down of Schmid Law [21]. This asymmetry is also reflected on the resolved shear stress vs shear strain curves in Fig. 1(b). We also note the directional nature of CRSS and the shear moduli in Fig. 1(b).

Besides the TA asymmetry, the applied $\Sigma_{NGS}$ on the active glide system also plays a significant role in the non-Schmid response of DO₃-Fe₃Al [24,25,28]. This $\Sigma_{NGS}$ effect lying under the different CRSS values measured on the active glide systems under tension and compression loading is shown in Fig. 1(c). The orientation relationship of crystals and the applied loading were interpreted using the conventional angle $\chi$, as can be seen in Fig. 1(d) [3]. Physically, $\chi$ corresponds to the angle between two planes which are significant in defining the dependence of slip geometry on the applied loading orientation and sense in bcc-based structures. First of these planes, taken as the reference plane for $\chi$, is the $\{110\}$ family plane with the highest resolved shear stress along the slip vector, i.e. either parallel to $[\overline{1}11]$ or $[111]$ for the sample orientations studied in this work ($[\overline{1}11]$ is chosen for the illustration in Fig. 1). The second plane is the maximum resolved shear stress plane (MRSSP) which can be any crystallographic plane bearing the highest shear stress along the same slip direction. It is important to note that $\chi$ angle is bounded between $\pm30^{\circ}$ owing to the bcc crystal symmetry. This symmetry enables to use the standard stereographic triangle with the corners $[001]-[011]-[\overline{1}11]$. Furthermore, the angle $\chi$ is a directional measure which takes a positive/negative value towards the closest plane sheared along the antitwinning/twinning sense. Regarding the data presented in Fig. 1, it is inferred that both TA asymmetry and $\Sigma_{NGS}$ component effects should be investigated in order to gain a fundamental knowledge of non-Schmid behavior of DO₃-Fe₃Al.

The paper represents a multifaceted approach to understanding the origin of non-Schmid phenomenon in ordered DO₃-Fe₃Al alloy. To our knowledge, this is the first time that the significance of non-Schmid effects is shown for Fe₃Al. The contribution in this work can

![](./images/811090835994050562_1.jpg)

Fig. 1. (a) The GSFE curves illustrate the lack of symmetry in $<111>$ cross-section of $\gamma$ surface on $(\overline{1}\overline{1}2)$ plane of DO₃-Fe₃Al owing to the TA asymmetry effect. (b) Resolved shear stress vs shear strain curves of DO₃-Fe₃Al exhibiting TA slip asymmetry depending on the sense of shearing. (c) The CRSS values measured on the active glide systems exhibit differences under tension and compression due to the presence of $\Sigma_{NGS}$ components. (d) The load and crystal orientation effects are analyzed using the conventional angle $\chi$ which is measured from the most highly sheared (in the direction of slip vector) $\{110\}$ family plane to the MRSSP plane. $\chi$ angle varies between $-30^{\circ}\leq\chi\leq30^{\circ}$ and it is taken as positive towards the closest $\{112\}$ family plane sheared along the antitwinning direction in the slip direction zone which is $(112)$ for the glide along $(101)[\overline{1}11]$ system under compression. The shear stress components, $\Sigma_{GS}$ and $\Sigma_{NGS}$, acting on the active glide system are also illustrated.

be summarized in capsule form as follows: (i) development of advanced DIC strain measurements to pinpoint precisely the onset of slip in DO₃-Fe₃Al using single crystal orientations chosen to accentuate TA asymmetry, and arrange Σ_NGS component that assists or resists CRSS through core spreading. Macroscopic strain measurements are imprecise in this regard. (ii) a multiscale predictive tool utilizing both continuum and atomistic terms in a modified P-N formulation that results in a modified yield criterion illustrating the non-Schmid phenomenon, (iii) demarcation between the role of TA and Σ_NGS effects utilizing Stroh-Eshelby anisotropic elasticity formulation [29-31] for NNAPB and NNNAPB fault arrangements resulting in clear demonstration of the isolated role of these two important effects.

Previous works have built a foundation for the present analysis but lacked the comparison with experiments and also delivered ideal stress levels in GPa's as opposed to MPa's. Additionally, most of the previous efforts have been focused on the single screw dislocation in a pure bcc metal and the deviation of CRSS values from Schmid Law has not been quantified for the bcc-based ordered structures in which the screw dislocation dissociates into its partials, such as in DO₃-Fe₃Al in this work. The anisotropic elasticity treatment in this study using the Stroh-Eshelby formalism overcomes the limitations of an isotropic derivation of the displacements for the DO₃-Fe₃Al especially having a high anisotropy ratio. We show that the deviations from Schmid Law in DO₃-Fe₃Al is substantial compared to other cubic alloys and our work represents a very thorough experimental program to illustrate this.

In accomplishing these goals; firstly, the orientation dependence of CRSS values in DO₃-Fe₃Al (23.7% at. Al concentration) single crystals were investigated experimentally. For this purpose; [0 0 1], [1 5 11] and [0 1 1] loading orientations were selected. The single crystals were subjected to both uniaxial tensile and compressive loading. The onset of slip in single crystals was identified precisely using high resolution, in-situ DIC strain measurements. Concurrently, MD simulations were utilized to evaluate the theoretical CRSS values by the modified P-N formalism [21]. The close agreement of both approaches on the non-Schmid response of DO₃-Fe₃Al, stimulated further interrogation on the role of the core structure. By employing the MS simulations via imposing the anisotropic external displacement fields corresponding to the applied Σ_GS and Σ_NGS components, the core displacements [32] at the leading partials were established. These results provided insight on the role of the stress components on the glide resistance of screw character partials in DO₃-Fe₃Al. The paper describes the experimental methods followed by the demonstration of non-Schmid effects studied with MD and MS calculations. The predictions of CRSS magnitudes from the modified P-N formalism were achieved without any fitting constants or adjustable parameters. For comparison purposes, CRSS values were also evaluated employing the generalized yielding criterion proposed in the literature [33-36] comparing a number of bcc alloys. The resulting CRSS values address the promising future extensions of this study for the crystal plasticity modelling efforts.

## 2. Methods
### 2.1. Experiments
Single crystals of Fe₃Al were grown by Bridgman technique in He atmosphere. The tensile dog-bone specimens (1.5 mm × 3 mm net section with 10 mm gage length) and compression specimens (4 mm × 4 mm x 10 mm) were cut by electro-discharge machining with the loading directions parallel to [0 0 1], [1 5 11], [0 1 1] crystallographic directions. Following a solution treatment at 800 °C for 1 h and successively iced water quenching, the specimens were annealed at 400 °C for 10 h in order to obtain DO₃ order and cooled in the furnace until reaching to the room temperature. To ensure the orientations of the heat treated single crystals, one virgin sample from each direction was prepared for X-Ray diffraction analysis. The pole figures and the diffraction patterns were obtained by Philips Xpert 2 diffractometer.

The compression and tension experiments were conducted using servo hydraulic load frame at ambient air with a strain rate of $5 × 10^{-5}\ s^{-1}$. Each specimen was mirror-polished and a speckle pattern was applied on its surface in order to measure the strain fields by the DIC technique. The compression experiments were conducted on a MTS servo hydraulic load frame while the MTI SEM Tester load frame was used for tensile loading. For high resolution imaging, a CCD Camera + Olympus BX51M microscope combination (with Olympus lenses) was used. The resolution provided by this set up is 0.4 μm/pix.

### 2.2. Molecular dynamics (MD) simulations
We employed MD simulations to quantify the CRSS values theoretically. For this purpose, an open source software LAMMPS (large-scale atomic/molecular massively parallel simulator) was utilized [37]. MD simulations were conducted employing a semi empirical potential developed for Fe-Al alloys within the framework of Embedded Atom Method (EAM) at 300 K [38]. The temperature is controlled with a Nose' - Hoover thermostat algorithm [39,40]. DO₃ lattice structure was inserted in a prismatic simulation box size of $900 × 300 × 50\ \mathring{A}$ with periodic boundary conditions in all three directions. To mimic the uniaxial experiments in this study, the simulation box was oriented such that in each scenario either [0 0 1], [1 5 11] or [0 1 1] was subjected to uniaxial tensile/compressive loading. Also additional orientations of [20 31 36], [$\overline{1}$9 30 48], [$\overline{1}$ 2 10] and [3 6 31] were subjected to only uniaxial compression for comparison purposes with the reported results in Ref. [25]. A stress concentrator was inserted inside the pristine crystal of DO₃-Fe₃Al as a straight dislocation source. In order to evaluate the theoretical CRSS values on the glide plane, we utilized the modified P-N formalism [21]. This formalism relates Peierls stress to the gradient of the total energy of the system with respect to the position of the dislocation line. The total energy (per unit dislocation length) of the crystallite which contains the four partials, $E^{total}$, is composed of the misfit energy, $E^{misfit}$, the line energy, $E^{line}$, the interaction energy of the partials, $E^{inter}$, and the applied work, $W$:

$$
E^{\text{total}} = E^{\text{misfit}} + E^{\text{line}} + E^{\text{inter}} - W \tag{1}
$$

Among these terms, $E^{misfit}$ is equal to the potential energies of the partials regarding their positions inside the crystallite and can be evaluated as in Eq. (2).

$$
E^{\text{misfit}} = \int_{-\infty}^{+\infty} \gamma(f(x))dx \tag{2}
$$

The term $\gamma$ represents the GSFE landscape of the system on either {1 1 0} or {1 1 2} slip planes along the slip direction and is written as a function of the atomistic disregistry function, $f(x)$, which is also a function of x coordinate on the glide plane perpendicular to the dislocation lines [21,41]. The $\gamma$ values are attained by utilizing the control box method [42,43]. In control box approach, ahead of the oncoming partial dislocations a group of atoms is designated and the variation of their total potential energy from the perfect lattice energy, $E_{CB}^{\text{perfect}}$, to $E_{CB}$ is tracked during the slip motion based on the following formulation:


$$
\gamma=\frac{E_{\mathrm{CB}}-E_{\mathrm{CB}}^{\text {perfect }}}{A_{\mathrm{CB}}}
\tag{3}
$$

where $A_{\mathrm{CB}}$ is the glide surface area of the control box. Owing to the non-planar structure of the partial dislocation cores, multilayer of atoms on both sides of the sheared glide plane are traced ensuring the convergence of $\gamma$ values.

At this point it is worth emphasizing that the non-planar cores of the partials interact with the applied stress components. As a result, $\gamma$ values in Eq. (3), traced during the glide reaction, are affected by the applied loading owing to the different core transformation paths followed. This interplay inevitably induces small differences in the $\gamma$ values attained between the control-box approach and the conventional half-block sliding approach which is conducted under pure shearing along the fault displacement [44,45]. These small differences are exemplified in Fig. 2 for $(\begin{array}{lll}1 & 0 & 1\end{array})[\begin{array}{lll}\overline{1} & 1 & 1\end{array}]$ glide system loaded under tension, shear and compression. As the [ $\begin{array}{lll}1 & 5 & 11\end{array}]$ sample is loaded under compression/ tension, the $1 / 4[\begin{array}{lll}\overline{1} & 1 & 1\end{array}]$ partials nucleated from the stress concentrator gliding on $(\begin{array}{lll}1 & 0 & 1\end{array})$ plane corresponds to higher/lower $\gamma$ values compared to pure shear loading. Even though this loading effect on GSFE curves generated is small for the [ $\begin{array}{lll}1 & 5 & 11\end{array}]$ sample, it can be significant for other orientations and is closely linked to the anisotropic behavior of CRSS values under varying $\chi$ values.

Revisiting the general formulation in Eq. (2), the disregistry function, $f(x)$, represents the inelastic displacements parallel to Burgers' vector across the glide plane. It is written as [21,46]:

$$
\begin{aligned}
f(x)= & \frac{b}{\pi}\left(\tan ^{-1}\left(\frac{x}{\xi}\right)+\tan ^{-1}\left(\frac{x-d_{1}}{\xi}\right)+\tan ^{-1}\left(\frac{x-\left(d_{1}+d_{2}\right)}{\xi}\right)\right. \\
& \left.+\tan ^{-1}\left(\frac{x-\left(d_{1}+d_{2}+d_{3}\right)}{\xi}\right)\right)+2 b
\end{aligned}
\tag{4}
$$

where $\xi$ is the half core width of the partials; $d_{1}, d_{2}, d_{3}$ are the separation distances between them, as shown in Fig. B.1., and $b$ is the magnitude of superpartial Burgers' vector, $\boldsymbol{b}$ ($b=|\boldsymbol{b}||1 / 4<111>|$). The discrete form of $E^{\text{misfit }}$ is given in Eq. (5) where $x$ variable is changed with the $m a^{\prime}-u$ expression to reflect the discreteness of the lattice in the Peierls-Nabarro formulation [47,48]. In Eq. (5), $m$ is an integer, $a^{\prime}$ is the shortest distance between two equivalent atomic rows in the direction of dislocation displacement and $u$ is the position of the leading dislocation line.

$$
E^{\text {misfit }}=\sum_{m=-\infty}^{m=+\infty} \gamma\left(f\left(m a^{\prime}-u\right)\right) a^{\prime}
\tag{5}
$$

The total energy per unit dislocation length, $E^{\text {total }}$, consists of both short range, $E^{\text {misfit }}$, and long range, $E^{\text {line }}$ and $E^{\text {inter }}$, energy terms with the applied work, $W$. The long range energy terms are dependent on the elastic constants, the magnitude of Burgers' vector of each partial, $b$, and the separation distances between them: $d_{1}, d_{2}$ and $d_{3}$. We have the following expression for $E^{\text {total }}$ [21,46]:

$$
E^{\text {total }}=\underbrace{\frac{n H C_{1212} b^{2}}{4 \pi} \ln \left(\frac{L}{2 \xi}\right)}_{E^{\text {line }}}+\underbrace{\sum_{m=-\infty}^{m=+\infty} \gamma\left(f\left(m a^{\prime}-u\right)\right) a^{\prime}}_{E^{\text {misfit }}}-\underbrace{\frac{H C_{1212} b^{2}}{4 \pi} \ln \left(\frac{L}{u-d_{1}}+\frac{L}{u-d_{1}-d_{2}}+\frac{L}{u-d_{1}-d_{2}-d_{3}}\right)}_{E^{\text {inter }}}+\underbrace{\sum_{G S} 4 b \mathrm{CRSS}}_{W}
\tag{6}
$$

![](./images/811090835994050562_2.jpg)

Fig. 2. The variation of GSFE curves along $(\begin{array}{lll}1 & 0 & 1\end{array})[\begin{array}{lll}\overline{1} & 1 & 1\end{array}]$ glide system under different applied loading conditions are plotted. The $\gamma$ curves calculated under the uniaxial tensile and compressive loading for [ $\begin{array}{lll}1 & 5 & 11\end{array}]$ sample are compared with the curve generated by the pure shear. As can be seen the resulting curves show slight variations owing to the effect of stress components acting. The energy barrier against the glide motion is calculated to be highest under the compressive loading and lowest under the tensile loading. The signs of shear stress components acting on the glide plane are surmised to be effective on the dislocation core resulting in this fault energy difference.

In Eq. (6) above, $C_{1212}$ is a component of the fourth order elastic stiffness tensor, $\boldsymbol{C}$, written in the $\mathrm{DO}_{3}$ crystallographic frame and relates the second order stress, $\boldsymbol{\sigma}$, and the strain, $\boldsymbol{\varepsilon}$, tensors respectively as in Eq. (7) where the indices $i, j, k, l$ take values 1 to 3 obeying the repeated indices summation convention (further information can be found in Appendix A).

$$
\sigma_{i j}=C_{i j k l} \varepsilon_{k l}
\tag{7}
$$

Revisiting Eq. (6), $n$ represents the number of superpartials, i.e. 4 in our case, and $L$ is the outer dimension of the crystallite and is taken to be 1000 times $b$. The parameter $H$ is dependent on the elastic constants and involves information about the elastic response of the general anisotropic medium [21,49]. $H$ can be written as in Eq. (8) [50]:

$$
H=1-12\left(1-\sqrt{\frac{C_{1111}-C_{1122}}{2 C_{1212}}}\right)
\tag{8}
$$

After determining the individual energy terms and the applied work; Peierls stress, $\tau_{\mathrm{p}}$, which is taken as equal to theoretical CRSS, is calculated as the maximum slope of $E^{\text {total }}$ with respect to $u$, and is given as follows:

$$
\tau_{\mathrm{p}}=\max \left(\frac{1}{b} \frac{\partial E^{\text {total }}}{\partial u}\right)
\tag{9}
$$

Please cite this article in press as: S. Alkan, H. Sehitoglu, Non-Schmid response of $\mathrm{Fe}_{3} \mathrm{Al}$ : The twin-antitwin slip asymmetry and non-glide shear stress effects, Acta Materialia (2016), http://dx.doi.org/10.1016/j.actamat.2016.12.019

![](./images/811090835994050562_3.jpg)

Fig. 3. The $\gamma$ curves generated by the MS simulations along the corresponding slip systems are plotted using dashed curves. The DFT calculations reported in Ref. [21] are also included, as solid curves, for comparison.

In modified P-N formalism, theoretical CRSS values are affected by the general topology of the GSFE curves generated. The peak energy value on the GSFE curves, i.e. unstable stacking fault energy, $\gamma^{\text{us}}$, represents the energy barrier against the motion of the partials on the corresponding glide system. Similarly, the first/third and second minima of the GSFE curves correspond to NNAPB, $\gamma^{\text{NNAPB}}$, and NNNAPB, $\gamma^{\text{NNNAPB}}$, fault energies of the pertinent system respectively. These fault energies are decisive in the separation distances and the restoring forces between the partials. The core structure of a partial is transformed at the onset of glide motion in a tendency to minimize the restoring forces acting on it. Thus, $\gamma^{\text{NNAPB}}$ and $\gamma^{\text{NNNAPB}}$ energies are of paramount importance to understand the core behavior of partials.

### 2.3. Molecular statics (MS) simulations

The DFT and MD simulations are well established, while the MS simulations, which can be very instructive for studying core structures and energy barriers under shearing have not been as well described. It is our aim to highlight the efficacy of the MS simulations and the results derived from MS below. In this study, MS simulations are based on the relaxation-type calculations of the $\text{DO}_3$ crystal structure employing Fe-Al potential under varying ratio of applied shear stress components, i.e. $\Sigma_{\text{GS}}$ and $\Sigma_{\text{NGS}}$. We employed MS simulations: (i) to check the accuracy of the Fe-Al potential used especially in relation to DFT based results, and (ii) to investigate the core structures of the leading superpartials under shear stress components corresponding to the uniaxial compressive loading along [1 5 11], [0 0 1] and [20 31 36] crystallographic directions. While a defect free crystal structure was utilized for the former one, a superdislocation, dissociated into four superpartials, was inserted inside the simulation box to accomplish the latter. The details are provided in Study of the core structure section.

### 2.4. Efficacy of the Fe-Al potential – the GSFE surface

In order to accomplish (i) above, the minima of the GSFE curves calculated from the MS simulations under pure shearing were compared with the first principles DFT calculations [21]. In these MS simulations, the same size of the simulation box and the boundary conditions were utilized as in the MD simulations. To that end, the upper half of a bulk, pristine crystal was displaced by a fault vector of $\boldsymbol{t}=\alpha<111>$, where $0 \leq \alpha \leq 1$, along a chosen glide plane (either $\{110\}$ or $\{112\}$) with respect to the lower one. Following each displacement increment parallel to $\boldsymbol{t}$, the simulation box is allowed to relax ensuring that the maximum force magnitude on each atom is lower than 0.015 eV/Angstroms. Calculating the total bulk potential energy of the sheared crystal, $E$, and the total bulk perfect lattice energy, $E^{\text{perfect}}$, at each $\alpha$ value visited, the GSFE curve per unit glide area, $\gamma$, is generated as formulated in Eq. (10) where $A$ is the glide surface area.

$$
\gamma=\frac{E-E^{\text{perfect}}}{A} \tag{10}
$$

The resulting GSFE curves are plotted in Fig. 3, in comparison with the reported curves generated by ab initio DFT calculations in Ref. [21]. In addition to these curves plotted, the resulting NNAPB and NNNAPB fault energy values, $\gamma^{\text{NNAPB}}$ and $\gamma^{\text{NNNAPB}}$ attained from these curves are also tabulated in Table 1. It is worth emphasizing that even though there are inevitable differences between the tabulated values of $\gamma^{\text{NNAPB}}$ and $\gamma^{\text{NNNAPB}}$ for ab-initio DFT and MS simulations owing to the sui generis physical and mathematical instruments underlying these two approaches, the resulting curves present very good agreement and the relative differences of $\gamma^{\text{NNAPB}}$ and $\gamma^{\text{NNNAPB}}$ values from both approaches do not exceed 15%. Thus, the resulting values are accepted to justify the use of the potential for our MD and MS simulations in this study promising an accurate assessment of the core effects given below.

### 2.5. Study of the core structure

After establishing the efficiency of the potential used with the earlier DFT calculations, the displacement fields in the core region of the leading superpartials for the [20 31 36], [1 5 11] and [0 0 1] compression samples were investigated by a simulation box delineated as a rectangular parallelpiped which is bounded by the planes $(\overline{1} \overline{2} 1)$, (1 0 1) and $(\overline{1} 11)$. The simulation box has a size of $900 \times 300$ Å with a thickness of only 3 atomic layers along $[\overline{1} 11]$ direction. A local right hand coordinate frame $x_1 - x_2 - x_3$ (see Appendix A for the coordinate system) is attached to the system such that $x_1$ and $x_2$ axes are parallel to $[\overline{1} \overline{2} 1]$ and $[\begin{array}{lll}1 & 0 & 1\end{array}]$ crystallographic directions in $\text{DO}_3$ lattice. A superdislocation dissociated into four $1/4$ $[\overline{1} 11]$ superpartials with screw character is inserted inside the simulation box. The initial atomic positions were imposed based on the numerical solution of the displacement field in an elastic-anisotropic medium corresponding to four straight

<table>
<caption>Table 1<br>$\gamma^{\text{NNAPB}}$ and $\gamma^{\text{NNNAPB}}$ values obtained by DFT calculations and MS simulations are tabulated. All the values are given in $\text{mJ/m}^2$.</caption>
<thead>
<tr>
<th>
</th>
<th colspan="2">$(\overline{1} \overline{2} 2)$ $[\overline{1} \overline{1} \overline{1}]$
</th>
<th colspan="2">$(\overline{1} \overline{2} 2)$ $[\begin{array}{lll}1 & 1 & 1\end{array}]$
</th>
<th colspan="2">$(101)$ $[\overline{1} 11]$
</th>
</tr>
<tr>
<th>
</th>
<th>DFT
</th>
<th>MS
</th>
<th>DFT
</th>
<th>MS
</th>
<th>DFT
</th>
<th>MS
</th>
</tr>
</thead>
<tbody>
<tr>
<td>$\gamma^{\text{NNAPB}}$
</td>
<td>273
</td>
<td>260
</td>
<td>241
</td>
<td>253
</td>
<td>249
</td>
<td>239
</td>
</tr>
<tr>
<td>$\gamma^{\text{NNNAPB}}$
</td>
<td>138
</td>
<td>151
</td>
<td>52
</td>
<td>61
</td>
<td>36
</td>
<td>41
</td>
</tr>
</tbody>
</table>

partial dislocations each with strength $1/4$ [$\overline{1}$ 1 1]. To establish the dislocation displacement fields associated with the superpartials, we used the Stroh-Eshelby formalism [29-31]. The initial separa- tion distances of these superpartials were taken as 20 nm, i.e. $d_{1}$ & $d_{3}$, for NNAPB and 30 nm, i.e. $d_{2}$, for NNNAPB faults based on an iterative try-out procedure regarding the reported values in the literature [21,51]. Given the initial positions of the atoms in $DO_{3}$ structure, the atoms on the $(\overline{1} \overline{2} 1)$ and $(\begin{array}{lll}1 & 0 & 1\end{array})$ boundary planes are fixed in their initial configuration and the rest of the atoms inside the box are relaxed ensuring maximum force on each atom is lower than 0.015 eV/Angstroms. To make the partial dislocations effec- tively infinite, the periodic boundary conditions are applied to the(11 1) planes.

In order to analyze the leading partial cores in the $[\begin{array}{llll}1 & 5 & 11\end{array}],[\begin{array}{llll}0 & 0 & 1\end{array}]$  and [20 31 36] compression samples at the instant of glide motion initiation by the designated simulation box, the uniaxial stress states in the experimented coordinate frame $X_{1}-X_{2}-X_{3}$ are to be transformed into $x_{1}-x_{2}-x_{3}$ frame. The corresponding stress tensors, i.e. $\sigma^{[\begin{array}{llll}1 & 5 & 11\end{array}]}, \sigma^{[\begin{array}{llll}20 & 31 & 36\end{array}]}$ and $\sigma^{[\begin{array}{llll}0 & 0 & 1\end{array}]}$ , are given in matrix form in $x_{1}-x_{2}-x_{3}$ frame by the following expressions in Eq. (11) to Eq.(13):

$$\left[\boldsymbol{\sigma}^{[1511]}\right]=\eta\left[\begin{array}{ccc}0 & 0 & 0 \\0 & -0.49 & -0.50 \\0 & -0.50 & -0.51\end{array}\right] \mathrm{MPa}\qquad(11)$$

$$\left[\boldsymbol{\sigma}^{[001]}\right]=\lambda\left[\begin{array}{ccc}-0.16 & -0.29 & -0.23 \\-0.29 & -0.50 & -0.41 \\-0.23 & -0.41 & -0.33\end{array}\right] \mathrm{MPa}\qquad(12)$$

$$\left[\boldsymbol{\sigma}^{[203136]}\right]=\omega\left[\begin{array}{ccc}-0.13 & 0.28 & 0.19 \\0.28 & -0.59 & -0.40 \\0.19 & -0.40 & -0.28\end{array}\right] \mathrm{MPa}\qquad(13)$$

where $\eta, \lambda$ and $\omega$ are the proportional loading coefficients which take positive values for the compressive loading. These stress states in Eq. (11) to Eq. (13) are applied on the simulation box by imposing the corresponding homogeneous strains, $\varepsilon$ , on the simulation boxwithin the context of anisotropic linear elasticity in $x_{1}-x_{2}-x_{3}$ frame as in Eq. (14):

$$\varepsilon_{i j}^{\prime}=S_{i j k l}^{\prime} \sigma_{k l}^{\prime}\qquad(14)$$

where $S_{i j k l}'$ are the components of the fourth order elastic compli ance tensor, $S$ . The details on the transformation of these tensors and the derivation of the anisotropic displacement field imposed can be found in Appendix A and Appendix B. The calculations indicate that only $\Sigma_{GS}$ components, i.e. $\sigma_{23}^{\prime}^{[\begin{array}{lll}0 & 0 & 1\end{array}]}, \sigma_{23}^{\prime}^{[\begin{array}{lll}20 & 31 & 36\end{array}]}$ , $\sigma_{23}^{\prime}^{[\begin{array}{lll}1 & 5 & 11\end{array}]}$ , and $\sum _{NCS}$ components, i.e. $\sigma_{21}^{\prime}^{[\begin{array}{lll}0 & 0 & 1\end{array}]}, \sigma_{21}^{\prime}^{[\begin{array}{lll}20 & 31 & 36\end{array}]}, \sigma_{21}^{\prime}^{[\begin{array}{lll}1 & 5 & 11\end{array}]}$ , acting on the active glide plane prevail upon the behavior of the leading partial core structures even though the other stress tensor components have a finite magnitude. Thus, the focus will be given on $\Sigma_{GS}$ and $\Sigma_{NCS}$ components acting on $(\begin{array}{lll}1 & 0 & 1\end{array})$ slip plane((1 01 $)[\overline{1} 11]$ system is observed to be activated for these three orientations under compression loading in MD simulations). The loading was built up by increasing the coefficients, i.e. $\eta, \lambda$ and $\omega$ , incrementally beginning from zero. Following each increment, the simulation box was relaxed. For each scenario studied, either the[1 5 11], [20 31 36] or [0 0 1] compression samples, the coefficients were increased until the leading partial started to move.

As can be seen in the expressions Eq. (11) to Eq. (13), the [0 0 1]and [20 31 36] compression samples have non-zero $\Sigma_{NCS}$ components acting on $(\begin{array}{lll}1 & 0 & 1\end{array})$ slip plane, i.e. $\sigma_{21}^{\prime}^{[\begin{array}{lll}0 & 0 & 1\end{array}]} \neq 0$ and $\sigma_{21}^{\prime}^{[\begin{array}{lll}20 & 31 & 36\end{array}]} \neq 0$ , unlike the [ $\begin{array}{lll}1 & 5 & 11\end{array}]$ sample in which $\sigma_{21}^{\prime}^{[\begin{array}{lll}1 & 5 & 11\end{array}]}=0$ . It is worth emphasizing that the compression samples of [0 0 1] and[20 31 36] are particularly convenient to study the interplay be- tween $\sum _{NCS}$ components and CRSS values for two reasons. Firstly, the absolute values of the ratios of $\sum _{NCS}$ to $\sum _{GS}$ components are very close for both of the [20 31 36] and [0 0 1] compression samples, i.e. $|\sigma_{21}^{\prime}^{[\begin{array}{lll}20 & 31 & 36\end{array}]} / \sigma_{23}^{\prime}^{[\begin{array}{lll}20 & 31 & 36\end{array}]}| \approx|\sigma_{21}^{\prime}^{[\begin{array}{lll}0 & 0 & 1\end{array}]} / \sigma_{23}^{\prime}^{[\begin{array}{lll}0 & 0 & 1\end{array}]}| \approx 0.70$ . This ratio of 0.70 is considered to be substantial and its effects on CRSS will provide insight. Secondly, $\Sigma_{NCS}$ components are of different signs with respect to $\Sigma_{GS}$ components in these two samples. This sign differ ence enables us to understand the response of the core structure to the sense of $\sum _{NCS}$ components. For these reasons, the core struc tures of the leading partials in these three samples were calculated by MS simulations and visualized by the differential displacement map technique (DDMT) [32] in Fig. 7 where the [11 1] components of the relative displacements of the neighboring atoms are pro- jected on the paper by the arrows drawn between the atoms with their lengths proportional to their magnitudes. The arrows are normalized such that an arrow touching the two neighboring atoms represents a relative displacement of $|1 / 12[\overline{1} 11]|$ magni tude. Note that in case of the greater relative displacements, an integer multiple of $|1 / 12[\overline{1} 11]|$ is substracted from the corre sponding displacement. This is required for the displacements be- tween the atoms across the APB faults.

Fig. 7 shows the calculated leading partial core structures under the absence and presence of $\sum _{NCS}$ and $\sum _{GS}$ components. In the absence of any applied loading, Fig. 7(a), the relative displacements are calculated to extend over the three $\left\{\begin{array}{lll}1 & 1 & 0\end{array}\right\}$ planes in the zone of the dislocation line, [11 1], similar to the bcc metals [9]. The applied $\sum _{GS}$ component, spreads the core displacements on the fourth sector among the six $\pi / 3$ sectors formed by the $\left\{\begin{array}{lll}1 & 1 & 0\end{array}\right\}$ planes (the first $\pi / 3$ sector is bounded by $(\begin{array}{lll}1 & 0 & 1\end{array})$ and $(\begin{array}{lll}1 & 1 & 0\end{array})$ planes and extends towards the right of the figure-the other sectors follow in coun- terclockwise sense), as can be seen in Fig. 7(c). The superimposition of a $\Sigma_{NCS}$ component in the opposite sense of the Peach-Koehler force exerted by the $\sum _{GS}$ component, promotes this spreading further, as seen in Fig. 7(b) and decreases the calculated CRSS magnitude. Reversing the sign of $\sum _{NCS}$ component as in Fig. 7(d), extends core spreading on the third sector in [ $\overline{1} 11]$ zone and in creases the $\sum _{GS}$ value at the instant of glide initiation in compliance with the experimental CRSS measurements. This evidence indicates that there is a correlation between the core shapes and CRSS values to be further interrogated. This point will be discussed in detail in Results - Discussion.

## 3. Results - discussion

### 3.1. Experimental results

The uniaxial stress, $\sigma$ , vs strain, $\varepsilon$ , curves obtained from tensile experiments are reported in Fig. 4. The DIC contour plots, captured at the instant of slip initiation, are reported in the insets labeled asA, B and C for the crystallographic loading axes of $[\begin{array}{lll}0 & 0 & 1\end{array}],[\begin{array}{lll}1 & 5 & 11\end{array}]$ and $[\begin{array}{lll}0 & 1 & 1\end{array}]$ respectively. The activated slip systems are included in Table 2. The results indicate that the [0 0 1] sample fails due to cleavage just after the slip activities were detected. However,[1 5 11] and [0 1 1] orientations show uniaxial strains over 4% and2% respectively. During unloading, these orientations also exhibit superelasticity.

The $\sigma-\varepsilon$ curves of compressive loading experiments are shown in Fig. 5. Under compressive loading, [0 0 1] orientation has the

---
Please cite this article in press as: S. Alkan, H. Sehitoglu, Non-Schmid response of $Fe_{3} Al$ : The twin-antitwin slip asymmetry and non-glide shear stress effects, Acta Materialia (2016), http://dx.doi.org/10.1016/j.actamat.2016.12.019

![](./images/811090835994050562_4.jpg)

Fig. 4. The uniaxial tensile stress vs strain curves of DO₃-Fe₃Al samples oriented along the three different crystallographic loading directions. The DIC images show the nucleation of slip at locations A, B and C on the curves.

<table>
<caption>Table 2<br>Active slip systems are tabulated for both tension and compression.</caption>
<thead>
<tr>
<th></th>
<th>[0 0 1]</th>
<th>[1 5 11]</th>
<th>[0 1 1]</th>
</tr>
</thead>
<tbody>
<tr>
<td>Tension</td>
<td>$(\overline{1}\ \overline{1}\ 2)\ [1\ 1\ 1]$</td>
<td>$(1\ 0\ 1)\ [\overline{1}\ 1\ 1]$</td>
<td>$(\overline{2}\ 1\ 1)\ [1\ 1\ 1]$</td>
</tr>
<tr>
<td>Compression</td>
<td>$(1\ 0\ 1)\ [\overline{1}\ 1\ 1]$</td>
<td>$(1\ 0\ 1)\ [\overline{1}\ 1\ 1]$</td>
<td>$(\overline{2}\ 1\ 1)\ [1\ 1\ 1]$</td>
</tr>
</tbody>
</table>

highest CRSS of 291±2 MPa. The [1 5 11] and [0 1 1] compression samples exhibit superelasticity upon unloading similar to the tensile loading. Unlike the other orientations, the activated glide plane does not coincide with the MRSSP for the [0 0 1]compression sample. Though $(\overline{1}\ \overline{1}\ 2)\ [1\ 1\ 1]$ system is favored in Schmid Factor analyses, the observed slip traces indicate that the activated system is $(1\ 0\ 1)\ [\overline{1}\ 1\ 1]$. This phenomenon is a slip anomaly as Schmid Law asserts the coincidence of the active glide plane and the MRSSP [3]. This slip anomaly stems from the fact that the faults in the core region of the partials split along the $\{ 1\ 1\ 0\}$ family planes and transform under the corresponding applied stress in such a way that partials prefer gliding along $\{ 1\ 1\ 0\}$ planes instead of gliding along the antitwinning direction on $\{ 1\ 1\ 2\}$. The lower energy barrier value for the leading partials, $\gamma^{us}$, on $\{ 1\ 1\ 0\}$ planes also eases this glide plane preference of the partials as reflected on the $\gamma$ curves in Fig. 3. The observed slip behavior indicates that applied stress tensor components play a very significant role on the nature of the sessile to glissile transformation of the dislocation core structure. We will address this point later as we visualize the leading partial core structures by DDMT at the instant just before the slip initiation.

As [0 1 1] and [0 0 1] tensile loading orientations favor slip along antitwinning and twinning directions in the absence of a $\Sigma_{NGS}$ component on $(\overline{2}1\ 1)$ and $(\overline{1}\ \overline{1}2)$ planes respectively, the differential of CRSS magnitudes in these two orientations gives the quantitative measure of TA slip asymmetry along $\{ 1\ 1\ 2\} <1\ 1\ 1>$ systems. This asymmetry corresponds to 46±3 MPa. For [1 5 11] orientation, CRSS values are equal in tension and compression within the experimental error margin. Thus, there is no CRSS magnitude differential between tension and compression for this orientation and Schmid Law holds in the absence of $\Sigma_{NGS}$ components on $(1\ 0\ 1)$ glide plane. As the presence of $\Sigma_{NGS}$ components are known to induce deviations from Schmid Law for pure bcc metals [52], a similar tendency is also expected for DO₃ structured alloys. In compliance with this tendency, the [0 0 1] compression sample constitutes an example of non-Schmid behavior. The CRSS differential between the [0 0 1] and [1 5 11] compression samples is measured to be 56±2 MPa even though $(1\ 0\ 1)\ [\overline{1}1\ 1]$ system is activated for both orientations. In this case, $\Sigma_{NGS}$ components are substantial to induce significant changes in the transformation path of core structure from sessile to glissile configuration. Thus, the CRSS differential between the [0 0 1] and [1 5 11] compression samples indicates that the $\Sigma_{NGS}$ components are as important as the TA slip asymmetry on the anisotropic glide resistance of DO₃-Fe₃Al. Though MS simulations were utilized to understand the underlying mechanism of this CRSS differential as will be presented later in the text, even these experimental measurements reveal that $\Sigma_{NGS}$ components affect the shearing directions between the atoms in the partial core zones. As a consequence of this $\Sigma_{NGS}$ effect, the change of the core structure in the [0 0 1] compression sample is likely to be reflected as a CRSS increase compared to the [1 5 11] sample.

### 3.2. Theoretical results
The theoretical CRSS values on the glide plane evaluated from the modified P-N analyses are shown in Fig. 6. As can be seen, the theoretical CRSS values are in close agreement with the experimental measurements. For comparison purposes, the CRSS values from the uniaxial compression experiments reported in Ref. [25] are also included in Fig. 6 with the theoretical values evaluated by the modified P-N formalism at the pertinent $\chi$ values. It is noted that the results added from the literature are more difficult to

![](./images/811090835994050562_5.jpg)

Fig. 5. The uniaxial compression stress vs strain curves of DO₃-Fe₃Al samples oriented along the three different crystallographic loading directions. The DIC images show the nucleation of slip at locations A, B and C on the curves.

establish precisely at the onset of slip because conventional displacement measurements at macroscale as opposed to at local scale was undertaken.

The question of the relationship between the core structures and the $\Sigma_{\text{NGS}}$ components naturally arises as CRSS values differ significantly even at the same observed glide system for the [1 5 11], [0 0 1] and [20 31 36] compression samples. To that end, MS simulations are conducted for these samples to further analyze the relative displacements at the leading partial core zones. In that regard, the core structure of the leading partial in the unstressed crystallite is shown in Fig. 7(a). It is seen that the largest displacement differentials are confined on (1 0 1), (1 1 0) and (0$\overline{1}$1) planes introducing three fractional dislocations on $\{ 110\}$ family planes. Following references [53,54], it is to be noted that the fractional dislocations are separated by the generalized stacking faults that have non-constant fault vectors along their width, unlike the partial dislocations which are separated by a stable stacking fault ribbon with a well-defined fault vector which is imposed by the local minima on the GSFE curve. Though the core structure has threefold rotation symmetry around [$\overline{1}$1 1] screw axis (triad symmetry), it is not invariant under $<110>$

![](./images/811090835994050562_6.jpg)

Fig. 6. CRSS values measured in the experiments and evaluated from the modified P-N formalism are shown. The CRSS values attained from the uniaxial compression experiments reported in Ref. [25] are also included for comparison.

Please cite this article in press as: S. Alkan, H. Sehitoglu, Non-Schmid response of Fe₃Al: The twin-antitwin slip asymmetry and non-glide shear stress effects, Acta Materialia (2016), http://dx.doi.org/10.1016/j.actamat.2016.12.019

![](./images/811090835994050562_7.jpg)

Fig. 7. (a) to (d): The relative displacements among the atoms on the three adjacent (1 1 1) planes in the core regions of the leading $1/4[\overline{1}11]$ superpartials are shown. Only the relative displacements parallel to $[\overline{1}11]$ are considered. The arrows are normalized so that an arrow touching both atoms is of magnitude: $|1/12[\overline{1}11]|$. The differential displacements greater than $|1/24[\overline{1}11]|$ are emphasized by red coloring. The atoms located on the same $(\overline{1}11)$ plane are colored the same. The black triangle indicates the initial position of the dislocation line which is located at the geometric center of the triangle surrounded by three $[\overline{1}11]$ atom rows. (a) shows the unstressed core configuration which is composed of three fractionals splitting on three $\{110\}$ family planes in $[\overline{1}11]$ zone. This core structure is not invariant under $<110>$ diad symmetry operation though it exhibits threefold screw rotation symmetry. The configuration in (b) shows the core structure for the [20 31 36] compression sample just before glide motion. Under the combined effects of the $\Sigma_{GS}$ and $\Sigma_{NGS}$ components, the displacements are concentrated on $(\begin{array}{lll}1 & 0 & 1\end{array})$ and $(\begin{array}{lll}1 & 1 & 0\end{array})$ planes in a zig-zag fashion. This core structure corresponds to the lowest CRSS value among the three configurations under applied shear stresses in this figure. The core structure in (c) corresponds to the $[\begin{array}{lll}1 & 5 & 11\end{array}]$ compression sample which is not subject to a $\Sigma_{NGS}$ component on $(\begin{array}{lll}1 & 0 & 1\end{array})$ glide plane. In this configuration the displacements are concentrated along $(\begin{array}{lll}1 & 0 & 1\end{array})$ and $(\begin{array}{lll}1 & 1 & 0\end{array})$ planes similar to the [20 31 36] compression sample but to a smaller extent. (d) shows the core structure in the $[\begin{array}{lll}0 & 0 & 1\end{array}]$ compression sample just before gliding under the effect of both $\Sigma_{GS}$ and $\Sigma_{NGS}$ components. The relative displacements of the neighboring atoms are concentrated on $(\begin{array}{lll}1 & 0 & 1\end{array})$ and $(\begin{array}{lll}0 & \overline{1} & 1\end{array})$ planes. This core structure corresponds to the highest CRSS magnitude. The shearing of $\left\{\begin{array}{lll}1 & 1 & 2\end{array}\right\}$ planes along the antitwinning direction and the elastic coupling between $\Sigma_{NGS}$ and GS strain are decisive on the higher glide resistance calculated in the $[\begin{array}{lll}0 & 0 & 1\end{array}]$ compression sample. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

diad symmetry operation which is composed of the consecutive reflections in the $(\overline{1}11)$ and $(\overline{1}\overline{2}1)$ planes respectively [55]. Due to the lack of the $<110>$ diad symmetry, there exist two energetically equivalent, i.e. degenerate, core configurations. These degenerate configurations are related to each other by the $<110>$ diad symmetry operation. The existence of the degenerate core configurations for the $1/4[\overline{1}11]$ leading partial core in $DO_{3}$ structure exhibits similarity with the $1/2<111>$ dislocation core structure in pure bcc metals evaluated utilizing central-force interatomic potentials [9,32,56]. At this point, it is worth emphasizing that the unstressed core structures are dependent on the nature of the interatomic forces considered as the core structure calculations in pure bcc metals based on the tight binding Bond-Order Potentials [55,57], ab-initio DFT [58,59] and many body EAM potentials [60-62] indicate that the differential displacements are evenly split on $\{110\}$ planes conserving both triad and diad symmetries.

The core structure of the leading superpartial dislocation in the [20 31 36] compression sample is shown in Fig. 7(b) just before the glide motion as $\omega$ coefficient in Eq. (13) attains a value of 920 MPa. It is worth emphasizing that the stress components extracted directly from the MS simulations are higher compared to CRSS values evaluated within the framework of the modified P-N model and the experimental measurements. This trend stems from the fact that the MS simulations do not encompass the temperature effects unlike the MD simulations employing Nose' - Hoover thermostat algorithm and the room temperature experimental measurements. As can be seen in Eq. (13), this sample is subjected to both $\Sigma_{GS}$ and $\Sigma_{NGS}$ components along $[\overline{1}11]$ and $[\overline{1}\overline{2}1]$ respectively. For this sample, unlike the unstressed configuration, the trailing fractionals on $(\begin{array}{lll}1 & 1 & 0\end{array})$ and $(\begin{array}{lll}0 & \overline{1} & 1\end{array})$ contract and the leading fractional extends over the $(\begin{array}{lll}1 & 0 & 1\end{array})$ planes in a zig-zag fashion forming a 4-layered $(\begin{array}{lll}2 & 1 & 1\end{array})$ fault. This fault shears the $\left\{\begin{array}{lll}1 & 1 & 2\end{array}\right\}$ planes along the twinning direction. Further increase of $\omega$ causes the center of the leading partial translate a distance of $1/6[12\overline{1}]$ in $(\begin{array}{lll}1 & 0 & 1\end{array})$ plane.

The $[\begin{array}{lll}1 & 5 & 11\end{array}]$ compression sample is subjected only to a $\Sigma_{GS}$ component along $[\overline{1}11]$ and the core structure just before glide motion, as $\eta$ coefficient in Eq. (11) attains a value of 1080 MPa, can be seen in Fig. 7(c). The applied $\Sigma_{GS}$ component causes the leading fractional extend in a zig zag fashion along $\{110\}$ family planes and form a 3-layered $(\begin{array}{lll}2 & 1 & 1\end{array})$ fault which shears the $\left\{\begin{array}{lll}1 & 1 & 2\end{array}\right\}$ planes along the twinning direction, similar to the [20 31 36] sample. Consequently, the relative displacements are concentrated on $(\begin{array}{lll}1 & 0 & 1\end{array})$ and $(\begin{array}{lll}1 & 1 & 0\end{array})$ planes. The absence of a $\Sigma_{NGS}$ component along $[\overline{1}\overline{2}1]$, unlike the [20 31 36] compression sample, increases the critical $\Sigma_{GS}$ magnitude required to translate the dislocation center $(|\sigma_{23}^{\prime[203136]}|=368$ MPa and $|\sigma_{23}^{\prime[1511]}|=540$ MPa). This behavior complies with the qualitative trend observed in the CRSS values predicted by the modified P-N formalism. Further increase of $\eta$ induces a translation of the dislocation center by $1/6[12\overline{1}]$.

The $[\begin{array}{lll}0 & 0 & 1\end{array}]$ compression sample is subjected to both a $\Sigma_{GS}$ component along $[\overline{1}11]$ and a $\Sigma_{NGS}$ component along $[12\overline{1}]$, in opposite sense with $\sigma_{21}^{\prime[203136]}$. The core structure of the leading partial in this sample just before glide motion, as $\lambda$ coefficient in Eq. (12) attains a value of 1430 MPa, can be seen in Fig. 7(d). The relative displacements are concentrated on $(\begin{array}{lll}1 & 0 & 1\end{array})$ and $(\begin{array}{lll}0 & \overline{1} & 1\end{array})$ planes in a zigzag fashion producing a 4-layered $(\begin{array}{lll}1 & \overline{1} & 2\end{array})$ fault. The presence of a $\Sigma_{NGS}$ component favoring the formation of faults shearing $\{112\}$ planes along the antitwinning direction is reflected on the

![](./images/811090835994050562_8.jpg)

magnitude of the critical $\Sigma_{\text{GS}}$ magnitude, i.e. $\left|\sigma_{23}^{\prime}{ }^{[0 \text { 0 1] }}\right|=710$ MPa.

The shearing of $\left\{\begin{array}{lll}1 & 1 & 2\end{array}\right\}$ planes along antitwinning/twinning directions in response to the core displacement extensions on $\left\{\begin{array}{lll}1 & 1 & 0\end{array}\right\}$ planes is the predominant mechanism prevailing on the CRSS magnitudes. In addition to non-planar core transformation mechanisms, anisotropic $\Sigma_{\text{NGS}}$ and GS strain coupling also contributes to CRSS values. Within the framework of the elastic anisotropy, the applied homogeneous GS strains, i.e. $\varepsilon_{23}^{\prime[20 \text { 31 36] }}$ and $\varepsilon_{23}^{\prime[0 \text { 0 1] }}$, for the [0 0 1] and [20 31 36] compression samples are dependent on both $\Sigma_{\text{GS}}$, i.e. $\sigma_{23}^{\prime}{ }^{[20 \text { 31 36] }}$ and $\sigma_{23}^{\prime}{ }^{[0 \text { 0 1] }}$, and $\Sigma_{\text{NGS}}$, i.e. $\sigma_{21}^{\prime}{ }^{[20 \text { 31 36] }}$ and $\sigma_{21}^{\prime}{ }^{[0 \text { 0 1] }}$, components as in expressed in Eq. (15) and Eq. (16):

$$
\varepsilon_{23}^{\prime[20 \text { 31 36] }}=2 S_{2321}^{\prime} \sigma_{21}^{\prime[20 \text { 31 36] }}+2 S_{2323}^{\prime} \sigma_{23}^{\prime[20 \text { 31 36] }}
\tag{15}
$$

$$
\varepsilon_{23}^{\prime[0 \text { 0 1] }}=2 S_{2321}^{\prime} \sigma_{21}^{\prime[0 \text { 0 1] }}+2 S_{2323}^{\prime} \sigma_{23}^{\prime[0 \text { 0 1] }}
\tag{16}
$$

where $S_{2321}^{\prime}$ and $S_{2323}^{\prime}$ are equal to $-2.02 \times 10^{-2} \mathrm{GPa}^{-1}$ and $+3.57 \times 10^{-2} \mathrm{GPa}^{-1}$ respectively. In $\mathrm{DO}_{3}-\mathrm{Fe}_{3} \mathrm{Al}$, though the component $S_{2323}^{\prime}$ is positive, the elastic anisotropic shear coupling component $S_{2321}^{\prime}$, relating the $\Sigma_{\text{NGS}}$ component and GS strain, is negative. To a first order approximation, the applied homogeneous GS strain inside the simulation box just before the glide motion can be related to the critical resultant glide shearing displacement on $\left(\begin{array}{lll}1 & 0 & 1\end{array}\right)$ glide plane, $u_{3}^{\prime}{ }^{\text {CRSS }}$, composed of $u_{3}^{\prime}{ }^{\text {GS }}$ and $u_{3}^{\prime}{ }^{\text {NGS }}$, as illustrated in Fig. 8 for the [0 0 1] and [20 31 36] compression samples. As the applied strain tensor components, $\varepsilon_{23}^{\prime[0 \text { 0 1] }}$ and $\varepsilon_{23}^{\prime[20 \text { 31 36] }}$ are constant inside the designated simulation box of prismatic shape, the displacements can be evaluated by integration with respect to $x_{2}$ coordinate complying with the derivation in Appendix B $\left(u_{3}^{\prime}{ }^{\text {CRSS }}=b=u_{3}^{\prime}{ }^{\text {total }}(0,0)+\right.$ Higher Order Terms $\approx u_{3}^{\prime}{ }^{\text {total }}(0,0)$ ). The negative value of $S_{2321}^{\prime}$ causes the shearing displacement $u_{3}^{\prime}{ }^{\text {NGS }}$ to have an opposite sense with respect to $u_{3}^{\prime}{ }^{\text {GS }}$ in the $\left[\begin{array}{lll}0 & 0 & 1\end{array}\right]$ compression sample. Thus, to create an atomistic disregistry of one Burgers' vector magnitude, $b$, in accordance with P-N model [31]; $u_{3}^{\prime}{ }^{\text {GS }}$ is to be greater than $b$ because of the opposing effect of $u_{3}^{\prime}{ }^{\text {NGS }}$ $\left(u_{3}^{\prime}{ }^{\text {GS }}+u_{3}^{\prime}{ }^{\text {NGS }}=b\right)$. The requirement for the greater magnitude of $u_{3}^{\prime}{ }^{\text {GS }}$, contributes to the higher CRSS magnitude in the $\left[\begin{array}{lll}0 & 0 & 1\end{array}\right]$ compression sample compared to the other orientations. The same mechanism can also lower the CRSS magnitude if the sense of $\Sigma_{\text{NGS}}$ component acting is reversed and $u_{3}^{\prime}{ }^{\text {NGS }}$ and $u_{3}^{\prime}{ }^{\text {GS }}$ have the same sign. This is exemplified in the lower CRSS value evaluated for the [20 31 36] compression sample. The intermediate CRSS magnitude for [1 5 11] compression sample in which $\Sigma_{\text{NGS}}$ component is absent, also complies with this conjecture. This GS strain and $\Sigma_{\text{NGS}}$ component interaction prevailing upon the CRSS magnitudes has been proposed previously for bcc and B2 ordered alloys [10,63,64] though it has been observed for the first time in a $\mathrm{DO}_{3}$ ordered alloy within the framework of the experimental measurements and atomistic scale calculations presented in this work.

### 3.3. Comparison of results with other bcc metals and ordered B2 & $\boldsymbol{DO}_{3}$ ordered alloys

The quantitative extent of the $\Sigma_{\text{NGS}}$ component effect and the TA slip asymmetry in pure bcc metals and bcc-based ordered alloys show large variations depending on the electronic configuration, temperature, order and composition characteristics of the materials [3]. To that end, the experimental CRSS values on the active glide system of some bcc and bcc-based ordered alloys are tabulated in Table 3 with the measurements on $\mathrm{DO}_{3}-\mathrm{Fe}_{3} \mathrm{Al}$ from this study included. As can be seen from the data tabulated at room temperature, the magnitude of the non-Schmid effects are material dependent. Among the pure bcc metals, the measured CRSS values for $\alpha$-Fe and Ta are observed to obey Schmid Law although significant differences are observed for W and Mo. These deviations from the Schmid Law observed in W and Mo are common for Group VIB transition materials in Periodic Table [7] and are associated with the asymmetric GSFE cross section and the tendency of the edge character-fractional formation inside the dislocation core

<table>
<caption>Table 3<br>CRSS values measured on the active glide systems of {1 1 0} <1 1 1> or {1 1 2} <1 1 1> are tabulated with $\chi=\pm 30^{\circ}$ under tension and compression based on the data available in the literature for pure bcc metals and bcc-based ordered alloys including $DO_{3}-Fe_{3}Al$ from this study.</caption>
<thead>
<tr>
<th rowspan="2"></th>
<th colspan="2">Tension</th>
<th colspan="2">Compression</th>
</tr>
<tr>
<th>$\chi=+30^{\circ}$</th>
<th>$\chi=-30^{\circ}$</th>
<th>$\chi=-30^{\circ}$</th>
<th>$\chi=+30^{\circ}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>W (293 K) [69]</td>
<td>110 MPa</td>
<td>95 MPa</td>
<td>132 MPa</td>
<td></td>
</tr>
<tr>
<td>Ta (293 K) [70]</td>
<td>70.5 MPa</td>
<td>70.5 MPa</td>
<td>47 MPa</td>
<td>47 MPa</td>
</tr>
<tr>
<td>Mo (293 K) [71]</td>
<td>54.5 MPa</td>
<td>31 MPa</td>
<td>101.5 MPa</td>
<td>37 MPa</td>
</tr>
<tr>
<td>Nb (293 K) [71]</td>
<td>24.5 MPa</td>
<td>20 MPa</td>
<td>17 MPa</td>
<td>22 MPa</td>
</tr>
<tr>
<td>$\alpha$-Fe (298 K) [72]</td>
<td>14.5 MPa</td>
<td>14.5 MPa</td>
<td></td>
<td></td>
</tr>
<tr>
<td>B2-FeAl (300 K) [66]</td>
<td></td>
<td></td>
<td>320 MPa</td>
<td>360 MPa</td>
</tr>
<tr>
<td>B2-$\beta$ CuZn [73]</td>
<td></td>
<td></td>
<td>23 MPa</td>
<td>25 MPa</td>
</tr>
<tr>
<td>B2-$\beta$ Brass (297 K) [74]</td>
<td>45 MPa</td>
<td>45 MPa</td>
<td></td>
<td></td>
</tr>
<tr>
<td>$DO_{3}-Fe_{3}Al_{0.8}Si_{0.2}$ (293 K) [28]</td>
<td>430 MPa</td>
<td>325 MPa</td>
<td></td>
</tr>
<tr>
<td>$DO_{3}-Fe_{3}Al$ (This Study, 293K)</td>
<td>251 MPa</td>
<td>203 MPa</td>
<td>210 MPa</td>
<td>292 MPa</td>
</tr>
</tbody>
</table>

interacting with $\Sigma_{NGS}$ components. The d-orbital anisotropy observed in transition metals has been proposed to be the reason behind this behavior [65].

Among the B2 and $DO_{3}$ structured alloys studied with active glide systems of either $\{110\}<111>$ or $\{112\}<111>$; B2 FeAl [66], $DO_{3}-Fe_{3}Al_{0.8}Si_{0.2}$ [28], $DO_{3}-Fe_{3}Al$ (this study) show the largest deviations from the Schmid behavior, as tabulated in Table 3. Though a solid explanation for the different discrepancies measured among these alloys is difficult as their CRSS values are reported by the different research groups and the mechanical properties of these ordered alloys are highly sensitive in ordering/ heat treatment and local chemical effects, the extensive non- Schmid behavior in these iron aluminides can be attributed to the elastic anisotropic coupling and charge transfer mechanisms accompanying p-d orbital hybridization effects between Al and Fe in B2-FeAl [63] as also seen in $DO_{3}-Fe_{3}Al$ and $DO_{3}-Fe_{3}Al_{0.8}Si_{0.2}$ [67,68]. The orbital hybridization stems from the overlap of d orbital electrons in Fe with p orbital valence electrons in Al and attributes directionality and strength on the bonds between Fe and Al. This bond structure between Fe and Al is not observed in B2-$\beta$ CuZn or B2-$\beta$ brass alloys in which metallic bonding is dominant.

It is worth commenting on the temperature depency of the non- Schmid yield behavior. The non-Schmid phenomenon is a function of the electronic configuration and the bonding character of the transition metals and intermetallics owing to the partially filled d orbitals [75-77]. As addressed in the recent works of Lim et al. [36] and Patra et al. [78], some of the intermetallics and transition elements, such as $\beta$ CuZn, $\beta$ Brass, Nb and Ta, are known to exhibit strongly anisotropic yield behavior at 77 K [3,74]. However, at room temperature it has been generally assumed that non-Schmid behavior is negligible. Among the materials shown in Table 3, the transition elements located in Group VB in the periodic table, i.e. Nb and Ta, are known to exhibit small antitwin-twin asymmetry in addition to the weak tendency of interaction with the applied non- glide stress components based on their radially symmetric $\gamma$ surface topology [7]. Similarly, the charge density maps of $\alpha$ - Fe [79], $\beta$ CuZn and $\beta$ Brass [80] exhibit weak directionality. Therefore, in these materials, the non-Schmid behavior is expected to be rather small at room temperature compared to 77 K owing to the onset of thermally activated glide mechanisms [81-84].

On the other hand, in the case of $Fe_{3} Al$, the d orbital of $Fe(3 d^{6}$  $4 s^{2})$ overlaps with the p orbital of $Al(3 s^{2} 3 p^{1})$ and this interaction results in strong and directional p-d hybridization effects [68].Therefore, $Fe_{3} Al$ class of intermetallics (including $Fe_{3} Al_{0.8} Si_{0.2}$  shown in Table 3) exhibit very strong non-Schmid behavior at 293 K. Dislocation configuration change (from uncoupled to coupled par- tial dislocation behavior) can occur above 373 K [23] for $Fe_{3} Al$ and can limit the non-Schmid effects. However, as stated earlier, the effect is very prevalent in a wide temperature range of 77 K-293 K (based on our experimental works at 293 K and additional data at77 K). Similarly, the strong covalent character bonding in Mo $(4 d^{5}$  $5 s^{1}$ ), owing to the half filled d-orbitals [57,85], is observed to have a prominent contribution to the non-Schmid behavior at 293 K. In summary, the results underscore the competing roles of the bonding directionality dominating at low temperatures and the thermally activated (kink pair and cross-glide) mechanisms oper- ating at elevated temperatures. It would be worthwhile to check other intermetallic alloys to assess their propensity for displaying non-Schmid effects at finite temperatures in future works.

The elastic anisotropy of $DO_{3}-Fe_{3} Al$ , which is also reflected on Zener's shear elastic anisotropy ratio with a value of 7.1 [21], has considerable effects on the MS calculations, especially at the stage of creating a dissociated superdislocation inside the delineated simu- lation box. The implementation of the anisotropic screw dislocation displacement fields as an initial condition is of paramount impor- tance for the accurate determination of atomic sites. The isotropic screw dislocation displacement fields [31] are observed to be insufficient as both elastic properties and APB energies of $DO_{3}-Fe_{3} Al$  are highly anisotropic. In that regard, the use of isotropic fields leads to the creation of an additional Burgers' vector of finite magnitude normal to the glide plane as also reported in the literature [19]. In contrast with the simulation results benefitting from the isotropic elastic displacements, the Transmission Electron Microscope studies conducted on $DO_{3}-Fe_{3} Al$ show that the deviation of partial slip vectors from $1 / 4<111>$ are insignificant (e.g. reported as0.0014 nm for NNNAPB faults) [86]. We observed that the aniso- tropic displacement fields help minimize the undesired, relaxation induced deviations in the slip vector with an achieved additional Burger's vector magnitude of $0.06 b(b=|1 / 4<111>|)$ only.

### 3.4. Transition to continuum scale
The physical mechanisms introducing non-Schmid plastic behavior at atomic scale have significant implications on the con- tinuum scale yielding behavior of bcc structured metallic materials as also reflected in our experimental measurements. In that regard, construction of a crystal plasticity model encompassing TA slip asymmetry and $\sum_{NGS}$ component effect necessitates the modification of the conventional yield criterions which are only $\Sigma_{GS}$  component dependent and equivalent to Tresca criterion. Following the pioneering study of Qin and Bassani [33], these non- Schmid effects are considered in the literature by a generalized yield criterion which is composed of a linear relation between the shear stress components on the $\{110\}$ planes intersecting along the $<111>$ slip vector and an effective, glide plane dependent critical stress level [34-36].

By implementing second order stress tensor transformation rules and neglecting the effect of hydrostatic stress on the slip, itcan be shown that considering any two of these three $\left\{\begin{array}{lll}1 & 1 & 0\end{array}\right\}$  planes is sufficient to generate the generalized yield criterion under

Please cite this article in press as: S. Alkan, H. Sehitoglu, Non-Schmid response of $Fe_{3} Al$ : The twin-antitwin slip asymmetry and non-glide shear stress effects, Acta Materialia (2016), http://dx.doi.org/10.1016/j.actamat.2016.12.019

<table>
<caption>Table 4
The fitting parameters of the generalized yield criterion for the {1 1 0} <111> glide systems: $a_1$, $a_2$, $a_3$ and $\tau_{cr}^\ast$ for are tabulated for DO₃-Fe₃Al (at 300 K) in comparison with Mo and Ta (at 0 K) and W (at 77 K) reported in the literature [34,36]. $\tau_{cr}^\ast$ values are normalized with respect to the corresponding $C_{1212}$ values in the pertinent crystallographic frames.</caption>
<thead>
<tr>
<th>Material</th>
<th>Glide System</th>
<th>$a_1$</th>
<th>$a_2$</th>
<th>$a_3$</th>
<th>$\tau_{cr}^\ast/C_{1212}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>DO₃-Fe₃Al (300 K)ª</td>
<td>(1 0 1) [1 1 1]</td>
<td>0.30</td>
<td>−0.25</td>
<td>0.07</td>
<td>0.002</td>
</tr>
<tr>
<td>Mo (0 K) [34]</td>
<td>(1 0 1) [1 1 1]</td>
<td>0.24</td>
<td>0</td>
<td>0.35</td>
<td>0.027</td>
</tr>
<tr>
<td>Ta (0 K) [34]</td>
<td>(1 0 1) [1 1 1]</td>
<td>0</td>
<td>0.56</td>
<td>0.75</td>
<td>0.028</td>
</tr>
<tr>
<td>W (77 K) [36]</td>
<td>{1 1 1} &lt;1 1 1&gt;</td>
<td>0.15</td>
<td>0.05</td>
<td>0.01</td>
<td>0.002</td>
</tr>
</tbody>
<tfoot>
<tr>
<td colspan="6">ª This study.</td>
</tr>
</tfoot>
</table>

a general 3-D external stress state. Adapting it to the nomenclature used in this paper, the generalized yield criterion for any active glide system can be written as:

$$
\begin{aligned}
\mathrm{CRSS} & +a_{1} \mathrm{CRSS} \frac{\cos (\chi+\pi / 3)}{\cos \chi}+a_{2} \Sigma_{\mathrm{NGS}} \\
& +a_{3} \Sigma_{\mathrm{NGS}} \frac{\cos (2 \chi+\pi / 6)}{\sin 2 \chi}=\tau_{\mathrm{cr}}^{*}
\end{aligned}
\tag{17}
$$

where $a_1$, $a_2$, $a_3$ and $\tau_{\text{cr}}^{*}$ are adjustable fitting parameters that are determined from the CRSS values predicted by the modified P-N formulation and the corresponding $\Sigma_{\text{NGS}}$ components (based on the stress state in $x_1 - x_2 - x_3$ frame) in this study. The terms $\mathrm{CRSS}/\cos\chi$ and $\Sigma_{\text{NGS}}/\sin2\chi$ represent the GS and NGS stress components acting on the neighboring $\{110\}$ glide plane making an angle of $60^\circ$ with the active glide plane in the slip vector zone. At this point it is worth emphasizing that for $\chi=0$, the term $\Sigma_{\text{NGS}}/\sin2\chi$ is equal to zero as can be shown by coordinate frame transformation.

As our main purpose is to demonstrate the multiscale effects of non-Schmid glide behavior in DO₃-Fe₃Al, obeying the generalized yield criterion given in Eq. (17) can be regarded as the first step for the construction of a prospective crystal plasticity model informed by the modified P-N formalism or the continuum scale experimental measurements within the framework of non-associated flow. For this purpose, the critical values of the components $\Sigma_{\text{GS}}$, i.e. CRSS, and $\Sigma_{\text{NGS}}$ at the instant that the glide motion initiates were employed for the compression samples of [20 31 36], [19 30 48], [1 5 11], [1 2 10], [3 6 31], [0 0 1] and the [1 5 11] tensile sample. It is noted that the common active glide system for these samples is (1 0 1) [1 1 1]. CRSS values were attained from the modified P-N formalism and the corresponding $\Sigma_{\text{NGS}}$ values were evaluated by transforming the corresponding uniaxial stress tensor in $X_1-X_2-X_3$ frame to $x_1-x_2-x_3$ as shown in Appendix A. For this derivation, the pertinent $\chi$ values of these samples were extracted from Fig. 6. The calculated parameters are tabulated in Table 4 with the reported values for $\{110\}$ $<111>$ systems for Mo, Ta, and W in the literature [34–36].

The CRSS values calculated from the modified P-N formalism in Eq. (9), generalized yield criterion of Eq. (17) and measured from the experiments are tabulated in Table 5 for the pertinent samples. The close agreement present between these enlisted values reveals that the generalized yield criterion is capable of predicting the CRSS values attained from the modified P-N formalism within excellent agreement. This agreement has the following significant implementations: (i) yield criterion for a specific glide system in DO₃-Fe₃Al can be constructed by a linear, homogeneous function of stress tensor components as proposed, including both $\Sigma_{\text{GS}}$ and $\Sigma_{\text{NGS}}$ components. (ii) CRSS and the corresponding $\Sigma_{\text{NGS}}$ values evaluated by an atomistically-informed, robust computational framework, i.e. the modified P-N formalism, can predict the continuum scale yielding behavior of DO₃-Fe₃Al. At this point it is worth emphasizing that even though we employed modified P-N predictions to conduct the fitting procedure, the predicted CRSS values from the generalized yield criterion also show very good agreement with the experimental measurements corresponding to the active(1 0 1) [1 1 1] glide system. This indicates the supremacy of the high magnification, in situ measurements in pinpointing the CRSS values compared to macro-scale measurement techniques.

Extension of this generalized yield criterion for varying 3-D stress states promoting the activation of different glide systems induces significant asymmetries in the shape of convex yield hyper surface in the principal stress space owing to the TA asymmetry and $\Sigma_{\text{NGS}}$ component effects [34,35,41]. The effects of non-planar core structure of screw dislocations are not only limited with the non-Schmid character of the yield surfaces. The proposed crystal plasticity models [34,87] demonstrated that the non-associated flow accompanying the non-Schmid yield behavior has an intensifying effect on the slip localization. However, the post yielding effects of non-planar core structures of screw dislocations are yet to be understood comprehensively and further efforts in this area would be of great interest for the scientific community. Another possible extension of the work is to evaluate shape memory alloys (which range from B2 to DO₃ structures in the austenite phase) that could potentially have the propensity for non-Schmid effects.

<table>
<caption>Table 5
The CRSS values predicted from the modified P-N, the generalized yield criterion and the experimental measurements are compared for the enlisted compression (C) and tension (T) samples.The experimental values from this study and the reported values in the literature [25], distinguished with an asterisk sign *, in the literature are also included for comparison purposes.</caption>
<thead>
<tr>
<th>DO₃-Fe₃Al sample</th>
<th>Modified P-N CRSS (MPa) Eq. (9)</th>
<th>Generalized yield criterion CRSS (MPa) Eq. (17)</th>
<th>Experimental CRSS (MPa)</th>
</tr>
</thead>
<tbody>
<tr>
<td>[20 31 36] C</td>
<td>228</td>
<td>239</td>
<td>237*</td>
</tr>
<tr>
<td>[19 30 48] C</td>
<td>236</td>
<td>234</td>
<td>249*</td>
</tr>
<tr>
<td>[1 5 11] C</td>
<td>243</td>
<td>240</td>
<td>234, 249*</td>
</tr>
<tr>
<td>[1 5 11] T</td>
<td>240</td>
<td>240</td>
<td>230</td>
</tr>
<tr>
<td>[1 2 10] C</td>
<td>268</td>
<td>270</td>
<td>262*</td>
</tr>
<tr>
<td>[3 6 31] C</td>
<td>292</td>
<td>290</td>
<td>281*</td>
</tr>
<tr>
<td>[0 0 1] C</td>
<td>297</td>
<td>293</td>
<td>292</td>
</tr>
</tbody>
</table>

## 4. Conclusions
In this work, the non-Schmid effects governing the plastic deformation of DO₃-Fe₃Al single crystals are interrogated by making a distinction between the twin-antitwin symmetry (TA effect) and the role of $\Sigma_{\text{NGS}}$ components (NGS effect). Following conclusions are drawn from this work:

(1) The glide resistance in $\{112\}$ planes in DO₃-Fe₃Al exhibits TA slip asymmetry. Slip in antitwinning sense is measured to be harder than the twinning sense.

---
Please cite this article in press as: S. Alkan, H. Sehitoglu, Non-Schmid response of Fe₃Al: The twin-antitwin slip asymmetry and non-glide shear stress effects, Acta Materialia (2016), http://dx.doi.org/10.1016/j.actamat.2016.12.019

(2) The presence of $\Sigma_{\text{NGS}}$ components is a major factor in non-Schmid behavior of DO₃-Fe₃Al.

(3) The theoretical CRSS values calculated utilizing MD simulations in modified P-N framework exhibit close agreement with the experimental measurements.

(4) MS simulations showed that the core structure of the leading superpartial dislocation, with screw character, in unstressed DO₃-Fe₃Al crystallite is composed of three fractional dislocations split asymmetrically along the $\{ 110\}$ planes. The stressed core configurations are calculated to extend over $\{ 110\}$ planes by creating multilayered shear faults. The samples with the faults shearing $\{ 112\}$ planes in the slip vector zone along twinning/antitwinning direction under the applied $\Sigma_{\text{NGS}}$ are observed to have a lower/higher calculated CRSS magnitude compared to no-$\Sigma_{\text{NGS}}$ orientation.

(5) The elastic-anisotropic $\Sigma_{\text{NGS}}$ and GS strain coupling related to the elastic compliance tensor components is calculated to have a prevailing effect on the CRSS values calculated. This calculated coupling suggests that the anisotropy of the elastic constants may ease or harden the screw partial glide. Thus, CRSS values in DO₃-Fe₃Al, are dependent on both shear stresses acting on the glide plane, $\Sigma_{\text{GS}}$ and $\Sigma_{\text{NGS}}$, and GS strain.

(6) The generalized yield criterion encompassing both $\Sigma_{\text{GS}}$ and $\Sigma_{\text{NGS}}$ components is demonstrated to predict CRSS values in very good agreement with the modified P-N formalism and continuum scale experimental measurements. This is an inspiring step towards a prospective crystal plasticity model bridging both atomistically-informed methods and macroscale deformations in a material exhibiting non-Schmid plastic behavior such as DO₃-Fe₃Al.

## Acknowledgements

The work was supported by National Science Foundation [grant number CMMI-NSF13-00284] which is gratefully acknowledged.We also acknowledge the use of the parallel computing resource, Taub cluster, and Frederick Seitz Materials Research Laboratories Central Facilities for X-ray diffraction analyses at University of Illinois. The single crystals were grown by Prof. Y. Chumlyakov, Tomsk State University, Tomsk, Russia.

## Appendix A

In the representation of the material constants, crystallographic orientations of the single crystals and the applied loading; three coordinate frames are used. These are: DO₃ crystal frame, $X_{1}-X_{2}-X_{3}$ and $x_{1}-x_{2}-x_{3}$ coordinate frames as shown in Fig. A.1. DO₃ crystal frame base vectors $\boldsymbol{e}_{\mathbf{1}}$, $\boldsymbol{e}_{\mathbf{2}}$, $\boldsymbol{e}_{\mathbf{3}}$ are equal to $\left[\begin{array}{lll}1 & 0 & 0\end{array}\right],\left[\begin{array}{lll}0 & 1 & 0\end{array}\right],\left[\begin{array}{lll}0 & 0 & 1\end{array}\right]$ DO₃ lattice vectors. The orthonormal, right hand coordinate frame $X_{1}-X_{2}-X_{3}$ is oriented such that the axis $X_{2}$ is coincident with the line of action of the uniaxial load vector, i.e. [p q r] direction in DO₃ coordinate frame, and $X_{3}$ axis is normal to the sample surface on which DIC pattern is implemented. $X_{1}-X_{2}-X_{3}$ frame is employed throughout the experiments and MD simulations. The unit basis vectors of $X_{1}-X_{2}-X_{3}$ frame are $\boldsymbol{e}_{1}^{\prime \prime}$, $\boldsymbol{e}_{2}^{\prime \prime}$ and $\boldsymbol{e}_{3}^{\prime \prime}$. Among these three basis vectors, $\boldsymbol{e}_{1}^{\prime \prime}$ and $\boldsymbol{e}_{2}^{\prime \prime}$ are tabulated in Table A.1. Finally, $x_{1}-x_{2}-x_{3}$ is an orthonormal, right hand coordinate frame attached to the simulation box frame and employed in MS simulations. The unit basis vectors of $x_{1}-x_{2}-x_{3}$ frame, $\boldsymbol{e}_{1}^{\prime}, \boldsymbol{e}_{2}^{\prime}, \boldsymbol{e}_{3}^{\prime}$; are set parallel to $\left[\begin{array}{lll}\overline{1} & \overline{2} & 1\end{array}\right],\left[\begin{array}{lll}1 & 0 & 1\end{array}\right]$ and $\left[\begin{array}{lll}\overline{1} & 1 & 1\end{array}\right]$ directions in DO₃ crystal frame.

![](./images/811090835994050562_9.jpg)

Fig. A.1. $X_{1}-X_{2}-X_{3}$ and $x_{1}-x_{2}-x_{3}$ frames are illustrated with the DO₃ crystallographic frame. $X_{1}-X_{2}-X_{3}$ frame attached on the experimented sample is oriented such that $X_{2}$ coincides with the line of action of the uniaxial loading (parallel to [p q r] direction in DO₃ crystal frame) and $X_{3}$ is parallel to the normal of the surface on which the deformation is tracked by DIC. $x_{1}-x_{2}-x_{3}$ frame is oriented such that $x_{2}$ and $x_{3}$ are set parallel to the directions $\left[\begin{array}{lll}1 & 0 & 1\end{array}\right]$ and $\left[\begin{array}{lll}\overline{1} & 1 & 1\end{array}\right]$, denoted in DO₃ crystal frame. The coordinates with respect to $x_{1}-x_{2}-x_{3}$ frame are determined by transforming the coordinates in $X_{1}-X_{2}-X_{3}$ frame by the transformation matrix:[$\mathbf{Q}$] and from the coordinates in DO₃ crystal frame by the transformation matrix [$\mathbf{R}$].

Table A.1
The unit basis vectors $\boldsymbol{e}_{1}^{\prime \prime}$ and $\boldsymbol{e}_{2}^{\prime \prime}$ corresponding to $\left[\begin{array}{lll}0 & 0 & 1\end{array}\right],\left[\begin{array}{lll}1 & 5 & 11\end{array}\right],\left[\begin{array}{lll}0 & 1 & 1\end{array}\right],\left[\begin{array}{lll}20 & 31 & 36\end{array}\right],\left[\begin{array}{lll}19 & 30 & 48\end{array}\right],\left[\begin{array}{lll}1 & 2 & 10\end{array}\right],\left[\begin{array}{lll}3 & 6 & 31\end{array}\right]$ samples are tabulated with respect to the DO₃ crystal coordinate frame. Note that the third basis vector $\boldsymbol{e}_{3}^{\prime \prime}$ is equal to the cross-product of $\boldsymbol{e}_{1}^{\prime \prime}$ and $\boldsymbol{e}_{2}^{\prime \prime}$ vectors.

<table>
<thead>
<tr>
<th>Loading direction</th>
<th>$\boldsymbol{e}_{1}^{\prime \prime}$</th>
<th>$\boldsymbol{e}_{2}^{\prime \prime}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>$\left[\begin{array}{lll}0 & 0 & 1\end{array}\right]$</td>
<td>$1/\sqrt{2}\ \left[\begin{array}{lll}\overline{1} & 1 & 0\end{array}\right]$</td>
<td>$\left[\begin{array}{lll}0 & 0 & 1\end{array}\right]$</td>
</tr>
<tr>
<td>$\left[\begin{array}{lll}1 & 5 & 11\end{array}\right]$</td>
<td>$1/\sqrt{122}\ \left[\begin{array}{lll}\overline{1}1 & 0 & 1\end{array}\right]$</td>
<td>$1/\sqrt{147}\ \left[\begin{array}{lll}1 & 5 & 11\end{array}\right]$</td>
</tr>
<tr>
<td>$\left[\begin{array}{lll}0 & 1 & 1\end{array}\right]$</td>
<td>$\left[\begin{array}{lll}\overline{1} & 0 & 0\end{array}\right]$</td>
<td>$1/\sqrt{2}\ \left[\begin{array}{lll}0 & 1 & 1\end{array}\right]$</td>
</tr>
<tr>
<td>$\left[\begin{array}{lll}20 & 31 & 36\end{array}\right]$</td>
<td>$1/\sqrt{106}\ \left[\begin{array}{lll}\overline{9} & 0 & 5\end{array}\right]$</td>
<td>$1/\sqrt{2657}\ \left[\begin{array}{lll}20 & 31 & 36\end{array}\right]$</td>
</tr>
<tr>
<td>$\left[\begin{array}{lll}19 & 30 & 48\end{array}\right]$</td>
<td>$1/\sqrt{89}\ \left[\begin{array}{lll}0 & 8 & 5\end{array}\right]$</td>
<td>$1/\sqrt{3565}\ \left[\begin{array}{lll}19 & 30 & 48\end{array}\right]$</td>
</tr>
<tr>
<td>$\left[\begin{array}{lll}\overline{1} & 2 & 10\end{array}\right]$</td>
<td>$1/\sqrt{5}\ \left[\begin{array}{lll}2 & 1 & 0\end{array}\right]$</td>
<td>$1/\sqrt{105}\ \left[\begin{array}{lll}\overline{1} & 2 & 10\end{array}\right]$</td>
</tr>
<tr>
<td>$\left[\begin{array}{lll}3 & 6 & 31\end{array}\right]$</td>
<td>$1/\sqrt{5}\ \left[\begin{array}{lll}\overline{2} & 1 & 0\end{array}\right]$</td>
<td>$1/\sqrt{1000}\ \left[\begin{array}{lll}3 & 6 & 31\end{array}\right]$</td>
</tr>
</tbody>
</table>

As a notation convention, ith component of any vector $\boldsymbol{T}$ will be denoted as $T_{i}$, $T_{i}^{I}$ and $T_{i}^{II}$ with respect to DO₃ crystal, $x_{1}-x_{2}-x_{3}$ and $X_{1}-X_{2}-X_{3}$ frames. Similar nomenclature will also be followed for the matrices and the tensors of any degree. Unless explicitly addressed, the subscripted indices will get the set of values 1,2,3 and 1,2 for the Latin and Greek letters respectively.We shall use Einstein summation convention over the repeating indices.

The external stress tensor, $\boldsymbol{\sigma}$, corresponding to the uniaxial tensile load of magnitude $\sigma$ parallel to $X_{2}$ in $X_{1}-X_{2}-X_{3}$ frame can be written in matrix notation as in Eq. (A.1).

$$
[\boldsymbol{\sigma}]=\begin{bmatrix}
0 & 0 & 0 \\
0 & \sigma & 0 \\
0 & 0 & 0
\end{bmatrix} \tag{A.1}
$$

The components of $\boldsymbol{\sigma}$ tensor, $\sigma_{kl}^{''}$ in $X_{1}-X_{2}-X_{3}$ frame, are transformed to $x_{1}-x_{2}-x_{3}$ frame by the second order tensor transformation rule of $\sigma_{ij}^{'}=[\mathbf{Q}]_{ik}\sigma_{kl}^{''}[\mathbf{Q}]_{lj}^{T}$ where [$\mathbf{Q}$] is the coordinate transformation matrix from $X_{1}-X_{2}-X_{3}$ to $x_{1}-x_{2}-x_{3}$ frame and the superscript $[]^{T}$ indicates the transpose of the given matrix

Please cite this article in press as: S. Alkan, H. Sehitoglu, Non-Schmid response of Fe₃Al: The twin-antitwin slip asymmetry and non-glide shear stress effects, Acta Materialia (2016), http://dx.doi.org/10.1016/j.actamat.2016.12.019

expression. [Q] is written as:

$$
[\mathbf{Q}]=\left[\begin{array}{lll}
\mathbf{e}_{1}^{\prime} \bullet \mathbf{e}_{1}^{\prime \prime} & \mathbf{e}_{1}^{\prime} \bullet \mathbf{e}_{2}^{\prime \prime} & \mathbf{e}_{1}^{\prime} \bullet \mathbf{e}_{3}^{\prime \prime} \\
\mathbf{e}_{2}^{\prime} \bullet \mathbf{e}_{1}^{\prime \prime} & \mathbf{e}_{2}^{\prime} \bullet \mathbf{e}_{2}^{\prime \prime} & \mathbf{e}_{2}^{\prime} \bullet \mathbf{e}_{3}^{\prime \prime} \\
\mathbf{e}_{3}^{\prime} \bullet \mathbf{e}_{1}^{\prime \prime} & \mathbf{e}_{3}^{\prime} \bullet \mathbf{e}_{3}^{\prime \prime} & \mathbf{e}_{3}^{\prime} \bullet \mathbf{e}_{3}^{\prime \prime}
\end{array}\right] \tag{A.2}
$$

where $(\bullet)$ represents the vector dot product operator.

The second order external/applied stress, $\boldsymbol{\sigma}$, and strain, $\boldsymbol{\varepsilon}$, tensors are related by the fourth order elastic stiffness, $\boldsymbol{C}$, and the compliance, $\boldsymbol{S}$, tensors with their pertinent symmetry properties [88]. In DO₃ crystal frame, the relations between $\boldsymbol{\sigma}$ and $\boldsymbol{\varepsilon}$ are written as in Eq. (A.3) and Eq. (A.4):

$$
\sigma_{i j}=C_{i j k l} \varepsilon_{k l} \tag{A.3}
$$

$$
\varepsilon_{i j}=S_{i j k l} \sigma_{k l} \tag{A.4}
$$

The components of $\boldsymbol{C}$ tensor are reported in Ref. [21] with respect to DO₃ crystal frame as: $C_{1111}=165$ GPa, $C_{1122}=125$ GPa, $C_{1212}=142$ GPa. Given the components of $\boldsymbol{C}$ tensor, the components of $\boldsymbol{S}$ are evaluated utilizing the Voigt Notation in which $\boldsymbol{C}$ tensor is represented as a $6 \times 6$ symmetric matrix, $[\mathbf{C}]$. In this notation, the following replacements are made on the indices: $11 \rightarrow 1$, $22 \rightarrow 2$, $33 \rightarrow 3$, $23 \rightarrow 4$, $13 \rightarrow 5$ and $12 \rightarrow 6$ (e.g. $C_{1222}=[\mathbf{C}]_{62}$ ). The inverse of $[\mathbf{C}]$ is equal to $[\mathbf{S}]$ as follows:

$$
[\mathbf{S}]=[\mathbf{C}]^{-1} \tag{A.5}
$$

where $[]^{-1}$ is the matrix inverse operator. The components of the symmetric matrix $[\mathbf{S}]$ are related to the components of $\boldsymbol{S}$ tensor as in Eq. (A.6) [88].

$$
\begin{array}{ll}
{[\mathbf{S}]_{m n}=S_{i j k l}} & \text { for } \mathrm{m} \text { and } \mathrm{n} \leq 3 \\
{[\mathbf{S}]_{m n}=2 S_{i j k l}} & \text { for } \mathrm{m} \text { and } \mathrm{n}>3 \\
{[\mathbf{S}]_{m n}=4 S_{i j k l}} & \text { for } \mathrm{m} \text { and } \mathrm{n}>3
\end{array} \tag{A.6}
$$

Following the transformation rules for a fourth order tensor, the components of $\boldsymbol{C}$ and $\boldsymbol{S}$ tensors with respect to $x_{1}-x_{2}-x_{3}$ frame are evaluated as follows:

$$
C_{i j k l}^{\prime}=[\mathbf{R}]_{i p}[\mathbf{R}]_{j q}[\mathbf{R}]_{k r}[\mathbf{R}]_{l s} C_{p q r s} \tag{A.7}
$$

$$
S_{i j k l}^{\prime}=[\mathbf{R}]_{i p}[\mathbf{R}]_{j q}[\mathbf{R}]_{k r}[\mathbf{R}]_{l s} S_{p q r s} \tag{A.8}
$$

where $[\mathbf{R}]$ is the transformation matrix from the DO₃ crystal frame to $x_{1}-x_{2}-x_{3}$ frame and written as:

$$
[\mathbf{R}]=\left[\begin{array}{lll}
\mathbf{e}_{1}^{\prime} \bullet \mathbf{e}_{1} & \mathbf{e}_{1}^{\prime} \bullet \mathbf{e}_{2} & \mathbf{e}_{1}^{\prime} \bullet \mathbf{e}_{3} \\
\mathbf{e}_{2}^{\prime} \bullet \mathbf{e}_{1} & \mathbf{e}_{2}^{\prime} \bullet \mathbf{e}_{2} & \mathbf{e}_{2}^{\prime} \bullet \mathbf{e}_{3} \\
\mathbf{e}_{3}^{\prime} \bullet \mathbf{e}_{1} & \mathbf{e}_{3}^{\prime} \bullet \mathbf{e}_{2} & \mathbf{e}_{3}^{\prime} \bullet \mathbf{e}_{3}
\end{array}\right] \tag{A.9}
$$

## Appendix B

The core structure of the leading superpartial in [1 5 11], [20 31 36] and [0 0 1] compression samples were calculated by employing MS simulations as explained in the previous sections. To that end, the four superpartials were inserted inside the pristine crystal by introducing the displacement fields of these straight dislocations, each with strength $\boldsymbol{b}=|\boldsymbol{b}|=|1 / 4[\overline{1} 11]|$, on all of the atoms inside the simulation box. Our main goal in this section is to summarize the solution methodology we implemented in evaluating these displacement fields based on the anisotropic elasticity methods [29-31]. Throughout this section, the formulations will be given with respect to the local coordinate frame attached to the simulation box with $x_{1}-x_{2}-x_{3}$ axes parallel to $[\overline{1} \overline{2} 1]$, [1 01$]$ and $[\overline{1} 11]$ respectively. The italic variables $x, y$ and $z$ represent the coordinates along $x_{1}, x_{2}$ and $x_{3}$ axes respectively. The partial differentiation of any expression with respect to $x_{i}$, i.e. $\partial() / \partial x_{i}$, will be shown as ()$_{, i}$.

In linear elasticity, the components of stress tensor $\boldsymbol{\sigma}$ can be related to strain tensor $\boldsymbol{\varepsilon}$ based on the expression in Eq. (B.1):

$$
\sigma_{i j}^{\prime}=C_{i j k l}^{\prime} \varepsilon_{k l}^{\prime} \tag{B.1}
$$

where the strain tensor components, $\varepsilon_{k l}^{\prime}$, are related to the partial derivatives of the displacement field components $u_{k}^{\prime}$ and $u_{l}^{\prime}$ by:

$$
\varepsilon_{k l}^{\prime}=\frac{1}{2}\left(u_{k, l}^{\prime}+u_{l, k}^{\prime}\right) \tag{B.2}
$$

On the other hand the stress components $\sigma_{i j}^{\prime}$ satisfy the equilibrium conditions as follows:

$$
\sigma_{i j, j}^{\prime}=0 \tag{B.3}
$$

Plugging the expressions in Eq. (B.1) and Eq. (B.2) into Eq. (B.3) and considering $\sigma_{i 3,3}^{\prime}=0$, indicate that the general solution for the displacement components $u_{k}^{\prime}$ can be written as:

$$
u_{k}^{\prime}=A_{k} f(x+p y) \tag{B.4}
$$

where $f$ is an analytic complex function and the components of the displacement vector $\boldsymbol{u}^{\prime}$ are independent of $x_{3}$ coordinate (e.g. $\partial \boldsymbol{u}^{\prime} / \partial x_{3}=0$ ). The components of the constant coefficient vector, $\boldsymbol{A}$, satisfy:

$$
\left(C_{i 1 k 1}^{\prime}+p C_{i 1 k 2}^{\prime}+p C_{i 2 k 1}^{\prime}+p^{2} C_{i 2 k 2}^{\prime}\right) A_{k}=0 \tag{B.5}
$$

The set of linear equations in Eq. (B.5) have a non-zero solution for the vector $\boldsymbol{A}$ if and only if the determinant of the matrix expression in parentheses is zero. This condition is given in Eq. (B.6).

$$
\operatorname{det}\left|C_{i 1 k 1}^{\prime}+p C_{i 1 k 2}^{\prime}+p C_{i 2 k 1}^{\prime}+p^{2} C_{i 2 k 2}^{\prime}\right|=0 \tag{B.6}
$$

The roots of the sextic expression in Eq. (B.6) have been shown to be imaginary by Eshelby et al. [30]. As the coefficients of the sextic expression in Eq. (B.6) are real, the six complex roots must occur in pairs of complex conjugates. Following the fact that the displacement components must be real, it is sufficient to consider only one of each complex conjugate root pairs $p_{\mathrm{n}}(\mathrm{n}=1,2,3)$ since the complex parts are necessarily cancelled. Note that the repeated index summation convention is not implemented on n. Each $\boldsymbol{A}^{\mathrm{n}}$ vector, corresponding to $p_{\mathrm{n}}$, is obtained by solving Eq. (B.5).

The general solution for $f$ takes the following form given in Eq. (B.7) when the elastic distortion field stems from the presence of a dislocation. $\pm$ indicates that the sign of $D^{\mathrm{n}}$ is taken to be same as the imaginary part of $p_{\mathrm{n}}$.

$$
f\left(x+p_{\mathrm{n}} y\right)=\frac{ \pm D^{n}}{2 \pi \sqrt{-1}} \log \left(x+p_{\mathrm{n}} y\right)+\sum_{m=-\infty}^{\infty} H_{m}\left(x+p_{\mathrm{n}} y\right)^{m} \tag{B.7}
$$

The logarithmic expression of the first term on the right hand side (R.H.S.) of Eq. (B.7) imposes a branch-cut ensuring the multi-valued nature of displacements across the glide plane in the right half-space for our Burgers' circuit convention. From a mathematical perspective, all the terms in the Laurent series, i.e. the second expression on the R.H.S. of Eq. (B.7), are continuous across the

Please cite this article in press as: S. Alkan, H. Sehitoglu, Non-Schmid response of Fe₃Al: The twin-antitwin slip asymmetry and non-glide shear stress effects, Acta Materialia (2016), http://dx.doi.org/10.1016/j.actamat.2016.12.019

branch-cut. Thus, each revolution taken around the dislocation line relates the coefficient $D^{\mathrm{n}}$ with $\Delta f$, which is the discontinuity in the values of the function $f$ across the branch-cut. Recalling the relation in Eq. (B.4) between the displacement components and the analytical function $f$, the discontinuities of the displacement components can be written in terms of the Burgers' vector components as in Eq. (B.8). Note that the Burgers' vector of each superpartial, $\boldsymbol{b}$, is equal to $\sqrt{3} / 4\left[\begin{array}{llll}0 & 0 & 1\end{array}\right]$ in $x_{1}-x_{2}-x_{3}$ coordinate frame.

$$
\operatorname{Re}\left[\sum_{\mathrm{n}=1}^{3} \pm A_{k}^{\mathrm{n}} D^{\mathrm{n}}\right]=b_{k}^{\prime}
\tag{B.8}
$$

As there is one $D^{\mathrm{n}}$ solution for each root $p_{\mathrm{n}}$ and each $D^{\mathrm{n}}$ consists of both real and imaginary parts, we need six equations to solve for all $D^{\mathrm{n}}$ values. However, there are only three linearly independent equations in the set of equations given in Eq. (B.8). Thus, the force equilibrium conditions are visited for the second set of three equations.

Considering the condition $\partial \sigma_{i 3}^{\prime} / \partial x_{3}=0$ in this derivation and the symmetry of stress tensor, Eq. (B.3) turns out to be $\sigma_{\alpha \beta, \beta}^{\prime}=0$. In the context of the elasticity theory, the total force vector, $\boldsymbol{F}^{\prime}$, exerted on a two dimensional, simply connected material cross-section (normal to $x_{3}$ and the dislocation lines of the superpartials) enclosed by a closed curve C is given by the following integral expression:

$$
F_{i}^{\prime}=\int_{C} \sigma_{i \beta}^{\prime} n_{\beta}^{\prime} d C
\tag{B.9}
$$

where $n_{\beta}^{\prime}$ are the components of the unit normal vector, $\boldsymbol{n}^{\prime}$, to C on the $x_{1} x_{2}$ plane. Recalling for the general form of $f$ function in Eq. (B.7) along with the displacement field components in Eq. (B.4) and plugging them into the expressions of Eq. (B.1) and Eq. (B.2), gives the stress components, $\sigma_{i j}^{\prime}$, as:

$$
\sigma_{i j}^{\prime}=\sum_{\mathrm{n}=1}^{3} B_{i j k}^{\mathrm{n}} A_{k}^{\mathrm{n}} \frac{1}{2}\left(\frac{\partial f\left(x+p_{\mathrm{n}} y\right)}{\partial x}-\sqrt{-1} \frac{\partial f\left(x+p_{\mathrm{n}} y\right)}{\partial y}\right)
\tag{B.10}
$$

where

$$
B_{i j k}^{\mathrm{n}}=C_{i j k 1}^{\prime}+C_{i j k 2}^{\prime} p_{\mathrm{n}}
\tag{B.11}
$$

Evaluating the contour integral in Eq. (B.9) by utilizing the parametric representation of the complex line integral [89], the resultant force components, $F_{i}^{\prime}$, are given as:

$$
F_{i}^{\prime}=\sum_{\mathrm{n}=1}^{3} B_{i 2 k}^{\mathrm{n}} \operatorname{Re}\left[\sum_{\mathrm{n}=1}^{3} \pm A_{k}^{\mathrm{n}} D^{\mathrm{n}}\right]
\tag{B.12}
$$

As stated earlier, the sets of equations given in Eq. (B.8) and Eq. (B.12) were solved together for the real and imaginary parts of $D^{\mathrm{n}}$ with the conditions of $F_{i}^{\prime}=0$ imposed (note that the force fields applied by the other partials and APB faults necessarily sum up to zero). Having $D^{\mathrm{n}}$ and $\boldsymbol{A}$ being evaluated for each partial, the related displacement components, $u_{k}^{\prime}$, due to each partial can be calculated for each lattice site initially at $\left(x_{o}, y_{o}, z_{o}\right)$ coordinates in the perfect $\mathrm{DO}_{3}$ lattice by Eq. (B.13) (Note that the solution is independent of $z_{o}$ coordinate).

$$
u_{k}^{\prime}\left(x_{o}, y_{o}\right)=\operatorname{Re}\left[-\frac{1}{2 \pi \sqrt{-1}} \sum_{\mathrm{n}=1}^{3} A_{k}^{\mathrm{n}} D^{\mathrm{n}} \log \left(x_{o}+p_{\mathrm{n}} y_{o}\right)\right]
\tag{B.13}
$$

The resultant displacement field vector in the unstressed configuration, $\boldsymbol{u}^{\prime}{ }^{\text {unstress }}$, is calculated by the superposition of the displacement fields of each individual partial dislocation. After determining $\boldsymbol{u}^{\prime}{ }^{\text {unstress }}$ field, the final coordinates of each atomic lattice site $(x, y, z)$ are evaluated by Eq. (B.14). Following the operation of this displacement field as an initial condition into the system within the framework of anisotropic elasticity, the system is relaxed by utilizing the Fe-Al EAM potential [38].

$$
(x, y, z)=\left(x_{o}, y_{o}, z_{o}\right)+\left(u_{1}^{\prime \text { unstress }}, u_{2}^{\prime \text { unstress }}, u_{3}^{\prime \text { unstress }}\right) \quad \text { (B.14) }
$$

Fig. B.1 illustrates the total displacement field along $x_{3}$ direction in the unstressed configuration, $u_{3}^{\prime}{ }^{\text {unstress }}$, around the four superpartials placed inside the simulation box. As can be seen, $u_{3}^{\prime}{ }^{\text {unstress }}$ field increases as furthering away from the partial dislocations, though the gradient increases in the close neighborhood of them. This localization trend near the dislocation centers indicates that instead of $u_{3}^{\prime}{ }^{\text {unstress }}$ field itself, the spatial gradient field of it is a better measure to visualize the core structures both in unstressed and stressed states. In that regard, even though it is not an immediate substitute for the gradient field, the use of relative displacements between the neighboring atoms near the dislocation center, as in DDMT, proves itself advantageous for analyzing the partial core structures.

![](./images/811090835994050562_10.jpg)

Fig. B.1. The superimposed $u_{3}^{\prime}$ unstress displacement fields of the four superpartial dislocations in the unstressed configuration. The displacements are normalized by the total Burger's vector, $4 b=\sqrt{3}[\begin{array}{lll}0 & 0 & 1\end{array}]$ , in $x_{1}-x_{2}-x_{3}$ frame.

The applied shear stress components, $\Sigma_{\mathrm{GS}}$ and $\Sigma_{\mathrm{NGS}}$ are simulated by imposing the corresponding homogeneous strain fields within the framework of anisotropic elasticity.

For the [p q r] compression sample where [p q r] is one of the crystallographic directions: [ $\left[\begin{array}{lll}1 & 5 & 11\end{array}\right],\left[\begin{array}{lll}0 & 0 & 1\end{array}\right]$ or $\left[\begin{array}{lll}20 & 31 & 36\end{array}\right]$; the independent non-zero shear strains can be written as:

$$
\varepsilon_{23}^{\prime}{ }^{[\mathrm{p} \text { q } \mathrm{r}]}=2 S_{2321}^{\prime} \sigma_{21}^{\prime}{ }^{[\mathrm{p} \text { q } \mathrm{r}]}+2 S_{2323}^{\prime} \sigma_{23}^{\prime}{ }^{[\mathrm{p} \text { q } \mathrm{r}]}
\tag{B.15}
$$

$$
\varepsilon_{21}^{\prime}{ }^{[\mathrm{p} \text { q } \mathrm{r}]}=2 S_{2121}^{\prime} \sigma_{21}^{\prime}{ }^{[\mathrm{p} \text { q } \mathrm{r}]}+2 S_{2123}^{\prime} \sigma_{23}^{\prime}{ }^{[\mathrm{p} \text { q } \mathrm{r}]}
\tag{B.16}
$$

where $\sigma_{23}^{\prime}{ }^{[\mathrm{p} \text { q r] }}$ and $\sigma_{21}^{\prime}{ }^{[\mathrm{p} \text { q r] }}$ are the $\Sigma_{\mathrm{GS}}$ and $\Sigma_{\mathrm{NGS}}$ components respectively in $x_{1}-x_{2}-x_{3}$ frame. In the expressions Eq. (B.15) and Eq. (B.16), the components $S_{2121}^{\prime}, S_{2321}^{\prime}$ and $S_{2323}^{\prime}$ are equal to $+2.13 \times 10^{-2} \mathrm{GPa}^{-1},-2.02 \times 10^{-2} \mathrm{GPa}^{-1},+3.57 \times 10^{-2} \mathrm{GPa}^{-1}$ respectively.

Based on the expression Eq. (B.2) relating the strain field and the displacement field components, the components of the additional
---
Please cite this article in press as: S. Alkan, H. Sehitoglu, Non-Schmid response of $\mathrm{Fe}_{3} \mathrm{Al}$ : The twin-antitwin slip asymmetry and non-glide shear stress effects, Acta Materialia (2016), http://dx.doi.org/10.1016/j.actamat.2016.12.019

elastic displacement field, $\boldsymbol{u}'^\text{elastic}$, created due to the applied loading on the simulation box are as follows:

$$
u_{1}^{\prime \text { elastic }}(x, y, z)=2 x \varepsilon_{21}^{\prime[\text { p q r }]} \tag{B.17}
$$

$$
u_{2}^{\prime \text { elastic }}(x, y, z)=0 \tag{B.18}
$$

$$
u_{3}^{\prime \text { elastic }}(x, y, z)=2 y \varepsilon_{23}^{\prime[\text { p q r }]} \tag{B.19}
$$

The total displacement field, $\boldsymbol{u}'^\text{total}$, under the applied loading with respect to the initial perfect DO₃ configuration is then given as:

$$
\boldsymbol{u}^{\prime \text { total }}=\boldsymbol{u}^{\prime \text { unstress }}+\boldsymbol{u}^{\prime \text { elastic }} \tag{B.20}
$$

Imposing the total displacement field $\boldsymbol{u}'^\text{total}$, the system is relaxed. This procedure is followed repeatedly until the center of the leading partial starts to translate.

## References

[1] E. Schmid, W. Boas, Plasticity of Crystals A, Hughes and Co., London, 1950.
[2] J.W. Christian, Some surprising features of the plastic deformation of body- centered cubic metals and alloys, Metall. Trans. A 14 (1983) 1237–1256.
[3] M.S. Duesbery, The dislocation core and plasticity, in: F.R.N. Nabarro (Ed.), Dislocations in Solids, vol. 8, Elsevier Science Publishers B.V., Netherlands, 1989, pp. 67–173.
[4] M.S. Duesbery, On non-glide stresses and their influence on the screw dislo- cation core in body-centred cubic metals. I. The Peierls stress, Proc. R. Soc. Lond. A Math. Phys. Eng. Sci. 392 (1984) 145–173.
[5] G.I. Taylor, The deformation of crystals of $\beta$-brass, Proc. R. Soc. Lond. A Math. Phys. Eng. Sci. 118 (1928) 1–24.
[6] F. Guiu, Slip asymmetry in molybdenum single crystals deformed in direct shear, Scr. Metall. 3 (1969) 449–454.
[7] M.S. Duesbery, V. Vitek, Plastic anisotropy in b.c.c. transition metals, Acta Mater. 46 (1998) 1481–1492.
[8] L. Dezerald, D. Rodney, E. Clouet, L. Ventelon, F. Willaime, Plastic anisotropy and dislocation trajectory in bcc metals, Nat. Commun. 7 (2016) 11695.
[9] V. Vitek, Theory of the core structures of dislocations in body-centred-cubic metals, Cryst. Lattice Defects 5 (1974) 1–34.
[10] M.S. Duesbery, On non-glide stresses and their influence on the screw dislocation core in body-centred cubic metals II. The core structure, Proc. R. Soc. Lond. A Math. Phys. Eng. Sci. 392 (1984) 175–197.
[11] V. Vitek, M. Yamaguchi, Core structure of nonscrew 1/2(111) dislocations on (110) planes in b.c.c. crystals. II. Peierls stress and the effect of an external shear stress on the cores, J. Phys. F Metal. Phys. 3 (1973) 537.
[12] T. Imura, Direction observation of dislocation behavior in bcc metals (Mo,Nb) and $\beta$-CuZn single crystals, in: M. Meshii (Ed.), Mechanical Properties of BCC Metals, The Metallurgical Society of AIME, New York, 1981.
[13] F. Louchet, L.P. Kubin, D. Vesely, In situ deformation of b.c.c. crystals at low temperatures in a high-voltage electron microscope Dislocation mechanisms and strain-rate equation, Philos. Mag. A 39 (1979) 433–454.
[14] R. Gröger, V. Vitek, Multiscale modeling of plastic deformation of molybde- num and tungsten. III. Effects of temperature and plastic strain rate, Acta Mater. 56 (2008) 5426–5439.
[15] R. Gröger, V. Vitek, Stress dependence of the Peierls barrier of 1/2⟨1 1 1⟩ screw dislocations in bcc metals, Acta Mater. 61 (2013) 6362–6371.
[16] M. Yamaguchi, Y. Umakoshi, The deformation behaviour of intermetallic superlattice compounds, Prog. Mater. Sci. 34 (1990) 1–148.
[17] V. Paidar, Generalized stacking faults in model lattice of ordered Fe-Si alloys, Czechoslov. J. Phys. B 26 (1976) 865–874.
[18] M. Yamaguchi, D.P. Pope, V. Vitek, Y. Umakoshi, Planar faults and dislocation dissociations in body-centred-cubic-derivative ordered structures, Philos. Mag. A 43 (1981) 1265–1275.
[19] M. Yamaguchi, Y. Umakoshi, Dislocations in b.c.c. metals and ordered alloys and compounds with b.c.c.-based ordered structures, in: V. Paidar, L. Lejcek (Eds.), The Structure and Properties of Crystal Defects, Elsevier, Liblice Cze- choslovakia, 1983.
[20] Y. Umakoshi, M. Yamaguchi, T. Yamane, Core structure effects on the motion of superlattice dislocations in the DO3 type-ordered structure, in: H. Suzuki, T. Ninomiya, K. Sumino, S. Takeuchi (Eds.), Dislocations in Solids, Proceedings of Yamada Conference IX University of Tokyo Press, Japan, 1985, pp. 81–84.
[21] A. Ojha, S. Alkan, L. Patriarca, H. Sehitoglu, Y. Chumlyakov, Shape memory behavior in Fe3Al-modeling and experiments, Philos. Mag. 95 (2015) 2553–2570.
[22] H.Y. Yasuda, T. Nakajima, K. Nakano, K. Yamaoka, M. Ueda, Y. Umakoshi, Effect of Al concentration on pseudoelasticity in Fe3Al single crystals, Acta Mater. 53 (2005) 5343–5351.
[23] H.Y. Yasuda, T. Nakajima, Y. Umakoshi, Temperature dependence of pseu- doelasticity in Fe3Al single crystals, Intermetallics 15 (2007) 819–823.
[24] H.Y. Yasuda, K. Nakano, M. Ueda, Y. Umakoshi, Orientation dependence of pseudoelasticity in Fe3Al single crystals, Mater. Sci. Forum 426–432 (2003) 1801–1806.
[25] H.Y. Yasuda, Y. Umakoshi, Pseudoelastic behaviour of Fe3Al single crystals with DO3 structure, Intermetallics 18 (2010) 1273–1278.
[26] M.J. Marcinkowski, N. Brown, Theory and direct observation of dislocations in the Fe3Al superlattices, Acta Metall. 9 (1961) 764–786.
[27] L.P. Kubin, A. Fourdeux, J.Y. Guedou, J. Rieu, Pseudoelasticity and slip revers- ibility in DO3-ordered Fe–Al single crystals by in situ experiments, Philos. Mag. A 46 (1982) 357–378.
[28] S. Hanada, S. Watanabe, T. Sato, O. Izumi, Deformation of Fe3Al0.8SiO2 with DO3 structure, Trans. Jpn. Inst. Metals 22 (1981) 873–881.
[29] A.N. Stroh, Dislocations and cracks in anisotropic elasticity, Philos. Mag. 3 (1958) 625–646.
[30] J.D. Eshelby, W.T. Read, W. Shockley, Anisotropic elasticity with applications to dislocation theory, Acta Metall. 1 (1953) 251–259.
[31] J.P. Hirth, J. Lothe, Theory of Dislocations, second ed., John Wiley & Sons, U.S.A, 1982.
[32] V. Vitek, R.C. Perrin, D.K. Bowen, The core structure of ½⟨111⟩ screw dislo- cations in b.c.c. crystals, Philos. Mag. 21 (1970) 1049–1073.
[33] Q. Qin, J.L. Bassani, Non-associated plastic flow in single crystals, J. Mech. Phys. Solids 40 (1992) 835–862.
[34] R. Gröger, V. Racherla, J.L. Bassani, V. Vitek, Multiscale modeling of plastic deformation of molybdenum and tungsten: II. Yield criterion for single crys- tals based on atomistic studies of glide of screw dislocations, Acta Mater. 56 (2008) 5412–5425.
[35] J.L. Bassani, V. Racherla, From non-planar dislocation cores to non-associated plasticity and strain bursts, Prog. Mater. Sci. 56 (2011) 852–863.
[36] H. Lim, C.R. Weinberger, C.C. Battaile, T.E. Buchheit, Application of generalized non-Schmid yield law to low-temperature plasticity in bcc transition metals, Model. Simul. Mater. Sci. Eng. 21 (2013) 045015.
[37] S. Plimpton, Fast parallel algorithms for short-range molecular dynamics, J. Comput. Phys. 117 (1995) 1–19.
[38] M.I. Mendelev, D.J. Srolovitz, G.J. Ackland, S. Han, Effect of Fe segregation on the migration of a non-symmetric $\Sigma 5$ tilt grain boundary in Al, J. Mater. Res. 20 (2005) 2018–2021.
[39] S. Nosé, A unified formulation of the constant temperature molecular dy- namics methods, J. Chem. Phys. 81 (1984) 511–519.
[40] W.G. Hoover, Canonical dynamics: equilibrium phase-space distributions, Phys. Rev. A 31 (1985) 1695–1697.
[41] A. Ojha, H. Sehitoglu, Critical Stresses for twinning, slip, and transformation in Ti-based shape memory alloys, Shape Mem. Superelasticity 2 (2016) 180–195.
[42] M.D. Sangid, T. Ezaz, H. Sehitoglu, I.M. Robertson, Energy of slip transmission and nucleation at grain boundaries, Acta Mater. 59 (2011) 283–296.
[43] P.B. Chowdhury, H. Sehitoglu, R.G. Rateick, H.J. Maier, Modeling fatigue crack growth resistance of nanocrystalline alloys, Acta Mater. 61 (2013) 2531–2547.
[44] V. Vitek, Intrinsic stacking faults in body-centred cubic crystals, Philos. Mag. 18 (1968) 773–786.
[45] V. Vitek, Core structure of screw dislocations in body-centred cubic metals: relation to symmetry and interatomic bonding, Philos. Mag. 84 (2004) 415–428.
[46] J. Wang, H. Sehitoglu, Modeling of pseudotwinning in Fe3Ga, Model. Simul. Mater. Sci. Eng. 22 (2014).
[47] P.B. Chowdhury, H. Sehitoglu, R.G. Rateick, Predicting fatigue resistance of nano-twinned materials: Part I – role of cyclic slip irreversibility and Peierls stress, Int. J. Fatigue 68 (2014) 277–291.
[48] E.B. Tadmor, R.E. Miller, R.S. Elliott, Continuum Mechanics and Thermody- namics: from Fundamental Concepts to Governing Equations, Cambridge University Press, United Kingdom, 2012.
[49] A.K. Head, The [111] dislocation in a cubic crystal, Phys. Status Solidi (b) 6 (1964) 461–465.
[50] A.K. Head, The energy of a screw dislocation in a cubic crystal, Phys. Status Solidi (b) 5 (1964) 51–54.
[51] R.C. Crawford, I.L.F. Ray, D.J.H. Cockayne, The weak-beam technique applied to superlattice dislocations in iron-aluminium alloys, Philos. Mag. 27 (1973) 1–7.
[52] V. Vitek, M. Mrovec, J.L. Bassani, Influence of non-glide stresses on plastic flow: from atomistic to continuum modeling, Mater. Sci. Eng. A 365 (2004) 31–37.
[53] M.S. Duesbery, V. Vitek, D.K. Bowen, The effect of shear stress on the screw dislocation core structure in body-centred cubic lattices, Proc. R. Soc. Lond. A Math. Phys. Eng. Sci. 332 (1973) 85–111.
[54] V. Vitek, F. Kroupa, Generalized splitting of dislocations, Philos. Mag. 19 (1969) 265–284.
[55] R. Gröger, A.G. Bailey, V. Vitek, Multiscale modeling of plastic deformation of molybdenum and tungsten: I. Atomistic studies of the core structure and glide of 1/2⟨1 1 1⟩ screw dislocations at 0 K, Acta Mater. 56 (2008) 5401–5411.
[56] W. Xu, J.A. Moriarty, Atomistic simulation of ideal shear strength, point de- fects, and screw dislocations in bcc transition metals: Mo as a prototype, Phys. Rev. B 54 (1996) 6941–6951.
[57] M. Mrovec, D. Nguyen-Manh, D.G. Pettifor, V. Vitek, Bond-order potential for

---

Please cite this article in press as: S. Alkan, H. Sehitoglu, Non-Schmid response of Fe₃Al: The twin-antitwin slip asymmetry and non-glide shear stress effects, Acta Materialia (2016), http://dx.doi.org/10.1016/j.actamat.2016.12.019

molybdenum: application to dislocation behavior, Phys. Rev. B 69 (2004) 094115.

[58] S. Ismail-Beigi, T.A. Arias, Ab initio study of screw dislocations in Mo and Ta: a new picture of plasticity in bcc transition metals, Phys. Rev. Lett. 84 (2000) 1499-1502.

[59] C. Woodward, S.I. Rao, Ab-initio simulation of isolated screw dislocations in bcc Mo and Ta, Philos. Mag. A 81 (2001) 1305-1316.

[60] M.I. Mendelev, S. Han, D.J. Srolovitz, G.J. Ackland, D.Y. Sun, M. Asta, Devel- opment of new interatomic potentials appropriate for crystalline and liquid iron, Philos. Mag. 83 (2003) 3977-3994.

[61] J. Marian, W. Cai, V.V. Bulatov, Dynamic transitions from smooth to rough to twinning in dislocation motion, Nat. Mater. 3 (2004) 158-163.

[62] J. Chaussidon, M. Fivel, D. Rodney, The glide of screw dislocations in bcc Fe: atomistic static and dynamic simulations, Acta Mater. 54 (2006) 3407-3416.

[63] C.L. Fu, M.H. Yoo, Deformation behavior of B2 type aluminides: FeAl and NiAl, Acta Metallur. Mater. 40 (1992) 703-711.

[64] Z.S. Basinski, M.S. Duesbery, The low temperature flow stress of body-centred cubic materials, in: R. Bullough, C.S. Hartley, J.P. Hirth (Eds.), Dislocation Modelling of Physical Systems, Pergamon, 1981, pp. 273-279.

[65] K. Masuda, A. Sato, Effects of d-orbital anisotropy on the core behavior of a (1/2) <111> screw dislocation in bcc transition metals, in: M. Meshii (Ed.), Mechanical Properties of BCC Metals, The Metallurgical Society of AIME, New York, 1981.

[66] T. Yamagata, H. Yoshida, Deformation behavior of FeAl single crystals, Mater. Sci. Eng. 12 (1973) 95-100.

[67] G.P. Das, B.K. Rao, P. Jena, S.C. Deevi, Electronic structure of substoichiometric Fe-Al intermetallics, Phys. Rev. B Condens. Matter Mater. Phys. 66 (2002) 1842031-18420313.

[68] B.V. Reddy, P. Jena, S.C. Deevi, Electronic structure and transport properties of Fe-Al alloys, Intermetallics 8 (2000) 1197-1207.

[69] A.S. Argon, S.R. Maloof, Fracture of tungsten single crystals at low tempera- tures, Acta Metall. 14 (1966) 1463-1468.

[70] D. Hull, J.F. Byron, F.W. Noble, Orientation dependence of yield in body- centered cubic metals, Can. J. Phys. 45 (1967) 1091-1099.

[71] P.J. Sherwood, F. Guiu, H.C. Kim, P.L. Pratt, Plastic anisotropy of tantalum, niobium, and molybdenum, Can. J. Phys. 45 (1967) 1075-1089.

[72] A.S. Keh, Y. Nakada, Plasticity of iron single crystals, Can. J. Phys. 45 (1967) 1101-1120.

[73] M. Yamaguchi, Y. Umakoshi, The operative slip systems and slip line morphology in $\beta$CuZn and $\beta$(CuNi)Zn alloys, Acta Metall. 24 (1976) 1061-1067.

[74] S. Hanada, M. Mohri, O. Izumi, Plasticity of beta-brass single crystals at low temperatures, Trans. Jpn. Inst. Metals 16 (1975) 453-461.

[75] A. Sato, K.-I. Masuda, Screw-dislocation motion in b.c.c. transition metals model calculation using a tight-binding-type electronic theory, Philos. Mag. Part B 43 (1981) 1-17.

[76] M. Mrovec, R. Gröger, A.G. Bailey, D. Nguyen-Manh, C. Elsässer, V. Vitek, Bond- order potential for simulations of extended defects in tungsten, Phys. Rev. B 75 (2007) 104119.

[77] J. Friedel, Transition metals, in: J. Ziman (Ed.), The Physics of Metals, Cam- bridge University Press, Great Britain, 1969, pp. 341-408.

[78] A. Patra, T. Zhu, D.L. Mcdowell, Constitutive equations for modeling non- Schmid effects in single crystal bcc-Fe at low and ambient temperatures, Int. J. Plastic. 59 (2014) 1-14.

[79] T.E. Jones, M.E. Eberhart, D.P. Clougherty, Topology of the spin-polarized charge density in bcc and fcc iron, Phys. Rev. Lett. 100 (2008) 017208.

[80] F.J. Arlinghaus, Energy bands in ordered beta-brass, Phys. Rev. (1967) 491-499.

[81] M. Wen, A.H.W. Ngan, Atomistic simulation of kink-pairs of screw dislocations in body-centred cubic iron, Acta Mater. 48 (2000) 4255-4265.

[82] A. Seeger, U. Holzwarth, Slip planes and kink properties of screw dislocations in high-purity niobium, Philos. Mag. 86 (2006) 3861-3892.

[83] L.H. Yang, J.A. Moriarty, Kink-pair mechanisms for a/2 (111) screw dislocation motion in bcc tantalum, Mater. Sci. Eng. A 319-321 (2001) 124-129.

[84] H. Yoshida, Y. Murakami, T. Saito, On the relation between temperature dependence of the strength and dislocation arrangements in beta-brass, J. Jpn. Inst. Metals 34 (1970) 660-666.

[85] D.G. Pettifor, Bonding and Structure of Molecules and Solids, Oxford Univer- sity Press, United States, 1995.

[86] W. Liu, H. Rosner, E. Langmaack, A. Gemperle, J. Gemperlova, J. Pesicka, E. Nembach, TEM investigations on the structure of antiphase boundaries in D03 ordered Fe3Al, Mater. Sci. Eng. A 258 (1998) 15-19.

[87] M. Dao, R.J. Asaro, Non-Schmid effects and localized plastic flow in interme- tallic alloys, Mater. Sci. Eng. A 170 (1993) 143-160.

[88] J.W. Steeds, Introduction to Anisotropic Elasticity Theory of Dislocations, Oxford University Press, Great Britain, 1973.

[89] E. Kreyszig, Advanced Engineering Mathematics, ninth ed., John Wiley & Sons, Singapore, 2006.

Please cite this article in press as: S. Alkan, H. Sehitoglu, Non-Schmid response of Fe₃Al: The twin-antitwin slip asymmetry and non-glide shear stress effects, Acta Materialia (2016), http://dx.doi.org/10.1016/j.actamat.2016.12.019
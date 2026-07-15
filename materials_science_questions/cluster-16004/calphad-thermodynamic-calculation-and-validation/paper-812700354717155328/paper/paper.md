# Effect of alloying elements on the $\gamma'$ antiphase boundary energy in Ni-base superalloys

M. Dodaran $^{a,b}$, A. Hemmasian Ettefagh $^{c}$, S.M. Guo $^{c}$, M.M. Khonsari $^{c}$, W.J. Meng $^{c}$, N. Shamsaei $^{a,b}$, S. Shao $^{a,b,*}$

$^{a}$ Department of Mechanical Engineering, Auburn University, Auburn, AL, 36849, USA
$^{b}$ National Center for Additive Manufacturing Excellence (NCAME), Auburn University, Auburn, AL, 36849, USA
$^{c}$ Department of Mechanical and Industrial Engineering, Louisiana State University, Baton Rouge, LA, 70803, USA

---

## ARTICLE INFO

**Keywords:**
Ni-base superalloys
Alloy design
Antiphase boundary energy
L1₂ structure
Cluster expansion
Density functional theory

---

## ABSTRACT

Mechanical and fatigue performance of $\gamma$-$\gamma'$ Ni-base superalloys are strongly affected by the antiphase boundary energy (APBE) of the $\gamma'$ precipitates which, in turn, is dictated by the alloy's composition. Due to the multi-component character of these alloys, establishing composition-APBE relationships are challenging, even though the qualitative effect of individual solutes on the APBE may be known. This work attempts to utilize density functional theory-based cluster expansion calculations to systematically assess the effect of composition on the APBE of the $\gamma'$ phases in Ni-base superalloys. We aim to elucidate the influence of not only one single element but also multiple coexisting alloying elements on the $\gamma'$ APBE. By explicit consideration of configurational disorder via Monte Carlo sampling, the effect of temperature on the APBE has also been analyzed. This work reveals that (1) effects of individual solute element M on the APBE energy obtained in an isolated, ternary condition (i.e. in $\text{Ni}_{3-x}\text{Al}_{1-y}\text{M}_{x+y}$) does not directly translate to a multi-solute case and that (2) the mutual synergistic interactions among different solute elements are not negligible. Based on the present results, an empirical master equation that predicts the APBE based on the composition of the $\gamma'$ phases has been obtained.

---

## 1. Introduction

Ni-base superalloys generally have excellent high-temperature strength, creep rupture resistance and corrosion resistance, and have been widely adopted in key components within the mid-high temperature regions of gas-turbine engines. These alloys typically comprise a $\gamma$ (FCC) matrix phase, strengthened by either $\gamma'$ (A₃B type of an ordered L12 structure, e.g. $\text{Ni}_3\text{Al}$) or $\gamma''$ (an ordered body-centered tetragonal) coherent precipitates. The strengthening effect of the precipitates derives from two origins. First, the ordered lattice structures of the $\gamma'$ and $\gamma''$ phases inhibit the motion of dislocations, as the passing of a perfect dislocation from the $\gamma$ phase to the $\gamma'$ and $\gamma''$ phases leads to the formation of antiphase boundaries (APB). Second, the lattice mismatch between the $\gamma$ matrix and $\gamma'$ or $\gamma''$ precipitates induces long-range coherency stresses which further inhibits the motion of incoming dislocations. The lattice mismatch between $\gamma$ and $\gamma'$ is sensitive on the exact alloying composition (such as additions of Cr, Co, Ti or Mo, etc.), but is generally very small, around $\sim\pm0.2\%$ [1–3]. The $\gamma$-$\gamma'$-$\gamma''$ alloys generally offer better mechanical strengths over the $\gamma$-$\gamma'$ alloys due to the additional strengthening effects offered by the lattice distortions surrounding the coherent $\gamma''$ phase (a mismatch of $\sim3\%$) [4]. However, the $\gamma''$ phase is unstable under temperatures above $650\ ^{\circ}\text{C}$ and decomposes to a $\delta$ (orthorhombic $\text{DO}_a$) phase, which deteriorates the overall strength of the three-phase alloys [5–7]. On the other hand, the $\gamma'$ phase displays a remarkable "stress anomaly" as a function of temperature in the intermediate temperature range ($\sim300\ \text{K}$--$900\ \text{K}$) [8], whereby the critical resolved shear stress (CRSS) increases as a function of the temperature. For these reasons, $\gamma$-$\gamma'$ alloys are still preferred in the high-temperature regions of the gas turbines. The $\gamma$-$\gamma'$ alloys are the focus of the present paper.

Under normal service conditions, modern rotating machinery's components are exposed to cyclic loading (such as vibration and rotating-bending, etc.) at low amplitudes and relatively high loading frequency. These constitute high cycle fatigue (HCF, $N_{\text{f}}>10^6$) and even very high cycle fatigue (VHCF, $N_{\text{f}}\approx10^9$) conditions. Under the HCF and VHCF conditions, macroscopic plastic deformation is vanishingly small,

---

* Corresponding author. Department of Mechanical Engineering, Auburn University, Auburn, AL, 36849, USA.
E-mail address: sshao@auburn.edu (S. Shao).

https://doi.org/10.1016/j.intermet.2019.106670
Received 7 October 2019; Received in revised form 25 November 2019; Accepted 26 November 2019
Available online 16 December 2019
0966-9795/© 2019 Elsevier Ltd. All rights reserved.

as reflected by the almost linear hysteresis response. Thus, macroscopic plastic yielding does not occur. Instead, localized plastic deformation occurs due to elastic incompatibilities among grains and local stress risers [9,10]. The cyclic plastic deformations are typically achieved by the simple to- and fro-motion of dislocations, resulting in little disloca- tion multiplication and cyclic hardening/softening [11-13]. The accu- mulation of fatigue damage is largely associated with the screw dislocations, whose motion is likely to generate irreversible cyclic deformation, due to interruptive events such as cross-slip [10,11]. The extent of cyclic slip reversibility is dependent on the superalloys' composition, to which the occurrence of these interruptive events is sensitive.

In the FCC $\gamma$ phase, perfect dislocations always dissociate into Shockley partials. Cross-slip of a perfect screw dislocation requires the temporary recombination of the partials, whose rate is positively correlated to the stacking fault energy (SFE) and, in turn, composition. In the $L1_2 \gamma'$ phase, perfect screw dislocations exist in pairs, separated by ribbons of either APB or superlattice stacking faults (SSF).

When a perfect FCC dislocation enters the $\gamma'$ precipitate, an APB is created on its wake until it is removal by a closely-spaced trailing perfect FCC dislocation. These dislocation-APB-dislocation defects are referred to as the super-dislocations in the $\gamma'$ precipitates, with each dislocation being named as superpartial dislocations. The magnitude of the strengthening by $\gamma'$ precipitates is closely related to the magnitude of APB energy (APBE), which is an important parameter in precipitation strengthening theories (PST) [14-21].

Extensive experimental evidence indicates that the (111) type slip with a screw-APB-screw configuration is predominant in the "stress anomaly" regime [22]. The screw-APB-screw defects are referred to as the superscrew dislocations, while each perfect screw dislocation is referred to as superpartial dislocations. The mutual elastic interaction between the superpartials generates an interaction force component perpendicular to their slip plane, providing a driving force for their cross-slip. Due to this reason, the slip of screw dislocations in $\gamma'$ is rarely planar and has a natural propensity to undergo the (111) to (100) type of cross-slip. The tendency of these cross-slip events is related to APBE.

A typical (111)-(100) cross-slip mechanism in the $\gamma'$ phase is illus- trated in Fig. 1. Each superpartial (SP in Fig. 1) dislocation dissociates into two Shockley partial (ShP in Fig. 1) dislocations separated by complex stacking faults (CSF) according to the reaction:

$$
a[1 \overline{1} 0] \rightarrow \frac{a}{2}[1 \overline{1} 0]+\frac{a}{2}[1 \overline{1} 0] \rightarrow \frac{a}{6}[1 \overline{2} 1]+\frac{a}{6}[2 \overline{1} \overline{1}]+\frac{a}{6}[1 \overline{2} 1]+\frac{a}{6}[2 \overline{1} \overline{1}]. \tag{1}
$$

The products of Reaction (1) correspond to the Burgers vectors of ShP $a$, ShP $b$, ShP $c$, and ShP $d$, respectively (Fig. 1(a)). Subjected to the mutual elastic interaction between SP 1 and SP 2, SP 2 dislocation feels both the tangential $(F_{\theta}^{1 \to 2})$ and the radial force $(F_{r}^{1 \to 2})$ originating from SP 1 (Fig. 1(b)). The resultant force drives the cross-slip of SP2 onto a (001) plane (Fig. 1(c)) [23,24]. The superpartial dislocations then re-dissociate into Shockley partials (Fig. 1(d)). Upon the onset of a reversed loading, the SP 2 dislocation (ShP $c$ and ShP $d$) now travels back along a different path (Fig. 1(e)). The mechanism depicted in Fig. 1 leads to irreversible slip as the trajectory of a superpartial dislocation (SP 2) altered during its to-and-fro motion. If the mechanism represents the behavior of small screw segments of a larger dislocation loop, then such motion would lead to an increase in dislocation density due to the in- crease in the edge dislocation length (edge dislocations cannot cross-slip).

The width of the APB ribbons depends on the competition between the repulsion between SP 1 and SP 2 and the surface tension in the APB. Lower APBE, therefore, leads to wider APB ribbons shown in Fig. 1(a) and (b), and vice versa. If the APBE is low, then the tangential force component generated by the interaction between SP 1 and SP 2 may lead to a significantly reduced cross-slip rate. Therefore, APBE strongly af- fects the cross-slip based motion of the super screw dislocations and plays a central role in the accumulation of fatigue damage in Ni-base superalloys. Lower APBE is thus favored to reduce the damage accu- mulation for Ni-base alloys under cyclic loading. This is echoed by experimental findings on $\gamma$-$\gamma'$ alloys [1,25,26].

In Ni-base superalloys, the APBE can be tuned by adjusting the relative fractions of the alloying elements (can be up to 10 species) [27-30]. Although understanding the precise effect of each alloying element on the overall APBE in the $\gamma'$ phase of a commercial alloy is highly desirable, obtaining such knowledge has been proved to be challenging for both experiments and numerical calculations. In exper- iments, the APBE can be obtained indirectly via the measurement of the spacing between superpartials via weak-beam transmission electron microscopy [8,22,31], which can be associated with large systematic errors. In simulations, molecular dynamic (MD) using interatomic embedded atom method (EAM) potentials has been employed to study

![](./images/812700354717155328_1.jpg)

Fig. 1. A schematic illustration of a typical cross-slip mechanism in the $\gamma'$ alloys and the resulting slip irreversibility when loading is reversed. APBs are represented by bold solid line segments, while the CSFs are represented by bold dashed line segments. The forces felt by SP 2 is represented by the thin blue arrows.

the planar faults, including APB and stacking faults, in pure Ni₃Al [32]. The stable fault energies and the energy landscape on various fault planes have been measured. The major drawback of MD is that describing the interatomic interaction among multiple atom types is challenging and requires a specifically parameterized interatomic po- tential that is tuned for a very narrow purpose [33,34]. Although at- tempts of direct density functional theory (DFT) calculations have been made for this purpose [35], addressing the long-range disordering ef- fects of the alloys is challenging due to the limitations in the size of DFT simulation cells.

In this work, we utilize the cluster expansion method combined with DFT calculation and Monte-Carlo (MC) sampling to assess the effect of composition on the (111) APBE of both an idealized Ni₃Al γ' phase and the γ' phase in a commercial alloy-Inconel 939. This article is orga- nized as follows: in Section 2, a background is given on prevailing nu- merical methods available for the calculation of APBE in ordered γ' phases; in Section 3 the computational details of this work is provided; in Section 4, effects of compositional variation and temperature changes on the relative APBE of ternary and multicomponent γ' phases are provided; finally, conclusions are drawn in Section 5.

## 2. Background

Several methods have been utilized to calculate the APBE of L1₂ structures, taking into account the atomic disordering due to alloying. These methods include
(1) direct, "brute-force" DFT calculations;
(2) ab initio calculation with the coherent potential approximation (CPA);
(3) cluster expansion (CE) based method; and
(4) one dimensional-long periodic structure (1D-LPS) method.

Methods (1)-(3) all share a common supercell approach, where the APBE is calculated based on the energy differences between two supercells (atomistic structures)—one with APB and one without. Be- tween these two structures, the energy difference is assumed to be solely due to presence of defect, and the APBE can be expressed as

$$
\gamma_{A P B}=\frac{E_{A P B}-E_{p r i s}}{A} \tag{2}
$$

where $\gamma_{APB}$ is the defect formation energy per unit area, $E_{APB}$ is the total energy of the structure with APB, $E_{pris}$ is that of the pristine one, and $A$ is the area of the defect in the computational cells. This has been the central idea for the calculation of the formation energies of generalized planar defects, including stacking fault energy [36], heterophase inter- face energy [37], and grain boundary energy [38]. This type of bi-crystal setup has been not only useful for these boundary energy calculations, but also in studies where the deformation at boundaries is focused [39, 40].

Method (1) constitutes calculating the total energies of the pristine structure and the structure with APB [41-43]. A typical representation of the computational cells is given in Fig. 2(a) [42]. To consider the effect of alloying, the supercells are typically randomly mixed—in the form of substitutional atoms-with a third atomic species [42]. The mole fraction of the alloying element corresponds to the number of the solute atoms divided by the total number of atoms in the computational cell. As typical DFT calculations can only consider a few tens of atoms (well below 100), this method cannot probe the effect of dilute solutes (mole fractions below a few %). In addition, the positions of the solute atoms relative to the APB affect the APBE. Indeed, it is energetically preferred for solute atoms to segregate at or near the APB according to experimental observations [43]. The APBE of an alloyed L1₂ structure is, in fact, a mean-field quantity, where the effects due to the randomly positioned solutes are "averaged". To address this, current direct ap- proaches typically perform large number of calculations on randomized atomistic configurations to obtain the averaged energies of the pristine and APB structures, which is computationally expensive [36,44]. In addition, the length scale of DFT is typically limited to a few tens of angstroms, which, with the application of periodic boundary conditions, imposes an unphysical spatial periodicity.

Method (2) addresses the configurational disorder introduced by the solute atoms using ab-initio calculations based on the coherent potential approximation (CPA) [28]. The essential idea is to replace the randomly positioned atoms in a lattice structure with an effective medium (Fig. 2 (b)), whose parameters can be solved self-consistently [44]. Typical approaches using this method describe potential field around atoms using exact muffin-tin orbitals (EMTO) [44] approximation and solves the Schrödinger equation using the Green's function method, as opposed to the Hamiltonian formalism commonly adopted by prevailing DFT calculations. According to the combined EMTO-CPA approach, the Green's function $(g)$ and the alloy potential $(P_{alloy})$ that characterizes the real alloy can be replaced by a site-independent coherent potential $\tilde{P}$ and a coherent Green's function $\tilde{g}$. The Green's function of individual atomic species, $g_i$, weight-averaged by their mole fraction $m_i$, is used to calcu- late the coherent Green's function that describes the system of random atomic configuration, i.e. $\tilde{g}=\sum_{i} m_{i} g_{i}$. With this method, the calculation of the APBE of an L1₂ phase at any given alloy composition would simply

![](./images/812700354717155328_2.jpg)

Fig. 2. Schematic illustrations of popular methods to study the effect of impurities on APB energy in γ'. (a) Direct DFT approach (image recreated with permission from Ref. [42]); (b) coherent potential approximation (CPA) method; (c) cluster expansion-based method; (d) one dimensional long period structure (1D-LPS) method.

require $ab$ initio calculations of the total energies of two effective atomistic structures with and without the APB. Method (2), as a mean-field technique, avoids the statistical nature of the problem, therefore cannot address the effect of temperature on APBE, which includes both configurational and vibrational contributions (phonon related).

The cluster expansion (CE) based methods (Method (3)), when combined with both DFT calculations and MC sampling, can address satisfactorily the effects of alloying elements and temperature on the APBE. The energy of a multicomponent alloy can be defined by the cluster expansion method introduced by Sanchez et al. [45]. Essentially, CE expresses the configuration-dependent energy of the atomistic configuration of an alloy by first abstracting the alloy's atomic structure into a lattice model, then expressing the energy into a polynomial form of the occupation states (spins) [46,47], see (Fig. 2(c)). The coefficients in the polynomial form are acquired by considering the energies of a large quantity of small periodic atomic clusters obtained from DFT calculations. Once the CE has been performed, energy of relatively large atomistic structures, containing at least thousands of atoms, can be efficiently calculated. Aided by MC sampling, the total energy of thousands of atomistic structures with randomized atomic positioning, with and without APBs, can be calculated [48]. This enables one to produce enough configurational variation for an accurate assessment of the average APBE. Thus, the APBE in the $\gamma'$ phase can be accurately measured with the disordered alloying elements properly accounted for [49].

Method (4) represents another class of approaches that evaluate the planar fault energies, including stacking fault energy and APBE, using a one dimensional Ising (1DI) based models [50-53]. 1DI model describes the configurational energy of local stacking sequence of an infinite stack of atomic monolayers—also referred to as polytypes—by perfect ($S_i = +1$) and faulty ($S_i = -1$) and parametrize the energy of the stack according to Ref. [54].

$$
E=J_{0}-J_{1} \sum_{i} S_{i} S_{i+1}-J_{2} \sum_{i} S_{i} S_{i+2}-J_{3} \sum_{i} S_{i} S_{i+3}-\cdots \tag{3}
$$

where $J_n$ are the interaction coefficients between the stacking of nearest neighbors ($J_1$), second nearest neighbors ($J_2$), etc. The one-dimensional long period structures (1D-LPS) method can be considered as an extension of the 1DI model to the case of APB in L1₂ structures. According to this method, the energy difference of a structure containing several APBs from the reference, APB-free structure, can be expressed as the following [53]:

$$
\begin{aligned}
E_{S}-E_{L 1_{2}} & =\frac{1}{N} \sum_{i}\left(\sigma_{i}+\frac{1}{2}\right) E_{A P B}+\frac{1}{N} \sum_{j>i} I_{j-i}\left(\sigma_{i}+\frac{1}{2}\right)\left(\sigma_{j}+\frac{1}{2}\right) \\
& +\frac{1}{N} \sum_{j>i>k} H_{i-k, j-i}\left(\sigma_{i}+\frac{1}{2}\right)\left(\sigma_{j}+\frac{1}{2}\right)\left(\sigma_{k}+\frac{1}{2}\right)
\end{aligned} \tag{4}
$$

where $E_S$ is the per-atom energy of the structure containing the APB, $E_{L1_2}$ is the per atom energy of reference structure, $N$ is periodicity in which the APB occurs (i.e. one APB per $N$ L1₂ cell), $E_{APB}$ is the per-atom energy contribution of a single APB, $\sigma_i$ is the corresponding occupation number defined based on the presence of APB i.e. $\sigma_i=1/2$ when the APB is present and $\sigma_i=-1/2$ when the APB is not present. $I_n$ and $H_{m,n}$ are the pair and three-body interaction coefficient, respectively. Therefore, energies of base L1₂ structure, as well as its derived atomistic structures by periodically adding APBs, can be calculated using DFT, which can then be used to fit with Eq. (4) to obtain necessary coefficients, including the $E_{APB}$, to obtain the APBE. For instance, the D0₂₂ and D0₂₃ are derived from the L1₂ structure, by introducing one {100} APB every one and two L1₂ cubes, respectively (Fig. 2(d)) [53]. Like Method (1), the disordering effect of the solute atoms requires performing large number of DFT calculations using atomistic configurations with randomized solute distributions. Due to this reason, Method (4) shares the drawback of Method (1) being computationally expensive.

### 3. Methodology

Based on the overview of the prevailing simulation methodologies in the foregoing section, the CE based methods are appealing as they can explicitly address the statistical nature of the solute-APB interaction and account for the effect of temperature through configurational variations. As was discussed by Sluiter et al., the vibrational contribution to APBE is small compared to the configurational contribution [55]. Using CE combined with DFT and MC, we study the effect of composition and temperature on the {111} APBE of Inconel 939. APB on the {111} plane is considered in this work due to their importance in the alloys cyclic deformation mechanisms in all temperature ranges [56]. CE is performed using ATAT toolkit [57] which relies on the $ab$ initio total-energy calculation on small and simple clusters of atoms.

Under the formalism of CE [45], the energy of an arbitrary atomistic configuration can be expressed by a polynomial of the energies of its composing atomic clusters. The energy of each atomic cluster is proportional to the product of an orthogonal cluster function $\varphi(\sigma)$ and an interaction energy coefficient $K$. Mathematically, the total energy is written as

$$
E(\sigma)=\sum_{\alpha} \sum_{s} K_{\alpha s} \varphi_{\alpha s}(\sigma), \tag{5}
$$

where $\varphi_{\alpha s}(\sigma)$ are the orthogonal cluster functions, $K_{\alpha s}$ are the interaction energy coefficients among all clusters (also referred to as effective cluster interaction, ECI), $\alpha$ is a designation of the atomic clusters, and $s$ is the order of the orthogonal polynomials with which the atomic clusters (cluster functions) are expressed. This suggests that, if the energies of a finite number of strategically chosen atomic structures can be provided, e.g. from DFT calculations, then Eq. (5) can be fitted with a given number of $K_{\alpha s}$. In a sense, CE extracts the interaction among atoms and attempts to predict the energy of unknown atomistic configurations.

The accuracy of a CE can be defined based on a cross-validation score, i.e.

$$
C V=\sqrt{\frac{1}{n} \sum_{i=1}^{n}\left(E_{i}-\widehat{E}_{i}\right)^{2}} \tag{6}
$$

where $n$ is the total number of structures used for fitting, $E_i$ and $\widehat{E}_i$ are the calculated (e.g. using DFT) energy of structure $i$ and predicted value of the energy by CE, respectively [47,48]. In this work, all cross-validation scores are below 35 meV/atom.

DFT calculations were performed to obtain the total energies of small, periodic atomistic structures and provide input to CE. Pseudopotentials from the Standard Solid State Pseudopotentials (SSSP) [58] were selected and their accuracy in predicting the lattice and elastic constants was verified. Resulting values of lattice parameter and elastic moduli have been compared with results from experiments and/or similar DFT calculations, as shown in Table 1. For these verifications, the wave function energy cutoff used is 35 Ry (476 eV), and the k points mesh grid used is $11 \times 11 \times 11$ for primitive cells with dimensions of $\sim 2.5 \times \sim 2.5 \times \sim 2.5 \mathring{A}^3$. Accordingly, in the DFT calculations for CE, k-point meshes are created for computational cells in such a way that a total of 1000 integration points are distributed uniformly within the Brillouin zone. Although APBE is sensitive to the local (~several $\mathring{A}$) mole fraction of alloying elements, the APBE of the alloy is a mean field quantity and is "averaged" over a long range (tens of nm or above). Therefore, in this study, atoms are assumed to reside at perfect L1₂ lattice points, even with the presence of multiple alloying elements. The effect of local, atomic-scale lattice distortions on the APBE is assumed to be small and is neglected. Indeed, experiments revealed that distortions in the first nearest neighbor distance induced by alloying elements in Ni are less than 3.6%, while that in the second nearest neighbor distance is

<table>
<caption>Table 1
A comparison of elastic (C<sub>ij</sub>) and lattice constants (a and c), of different atom types, between results of this study and existing literature. DFT – density functional theory; Exp. – experiment.</caption>
<tbody>
<tr>
<td rowspan="2">Al</td>
<td colspan="4">This study</td>
<td>Literature</td>
</tr>
<tr>
<td> </td>
<td>C<sub>11</sub></td>
<td>C<sub>12</sub></td>
<td>C<sub>44</sub></td>
<td>a</td>
<td>a</td>
</tr>
<tr>
<td>Exp [85].</td>
<td>116.3</td>
<td>64.8</td>
<td>30.9</td>
<td rowspan="2">4.0377 Å</td>
<td rowspan="2">4.019 Å<br>Exp [87].</td>
</tr>
<tr>
<td>Exp [86].</td>
<td>114.3</td>
<td>61.92</td>
<td>31.62</td>
</tr>
<tr>
<td>Exp [85].</td>
<td>107.3</td>
<td>60.8</td>
<td>2.83</td>
<td> </td>
<td> </td>
</tr>
<tr>
<td>DFT [88]</td>
<td>121</td>
<td>63</td>
<td>33.0</td>
<td> </td>
<td> </td>
</tr>
<tr>
<td>DFT [89]</td>
<td>105</td>
<td>54</td>
<td>26</td>
<td> </td>
<td> </td>
</tr>
<tr>
<td>DFT [90]</td>
<td>103</td>
<td>56</td>
<td>30</td>
<td> </td>
<td> </td>
</tr>
<tr>
<td>This study</td>
<td>123.31</td>
<td>54.45</td>
<td>39.83</td>
<td> </td>
<td> </td>
</tr>
<tr>
<td rowspan="2">Ti</td>
<td colspan="6">This study</td>
<td colspan="2">Literature</td>
</tr>
<tr>
<td> </td>
<td>C<sub>11</sub></td>
<td>C<sub>12</sub></td>
<td>C<sub>13</sub></td>
<td>C<sub>33</sub></td>
<td>C<sub>44</sub></td>
<td>a</td>
<td>c/a</td>
<td>a</td>
<td>c/a</td>
</tr>
<tr>
<td>Exp [91].</td>
<td>176.1</td>
<td>86.9</td>
<td>68.3</td>
<td>190.5</td>
<td>50.8</td>
<td rowspan="2">2.939 Å</td>
<td rowspan="2">1.5800</td>
<td>2.95107 Å</td>
<td>1.587 Å</td>
</tr>
<tr>
<td>Exp [92].</td>
<td>160</td>
<td>90</td>
<td>66</td>
<td>181</td>
<td>46</td>
<td>Exp [93].</td>
<td>Exp [93].</td>
</tr>
<tr>
<td>DFT [94]</td>
<td>171.6</td>
<td>85</td>
<td>78.6</td>
<td>187.5</td>
<td>39</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
</tr>
<tr>
<td>DFT [95]</td>
<td>174.5</td>
<td>87</td>
<td>78</td>
<td>188</td>
<td>42</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
</tr>
<tr>
<td>DFT [96]</td>
<td>194</td>
<td>69</td>
<td>80</td>
<td>175</td>
<td>41</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
</tr>
<tr>
<td>This study</td>
<td>189.9</td>
<td>62.8</td>
<td>69.9</td>
<td>194.6</td>
<td>42.03</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
</tr>
<tr>
<td rowspan="2">Ni</td>
<td colspan="4">This study</td>
<td>Literature</td>
</tr>
<tr>
<td> </td>
<td>C<sub>11</sub></td>
<td>C<sub>12</sub></td>
<td>C<sub>44</sub></td>
<td>a</td>
<td>a</td>
</tr>
<tr>
<td>Exp [97].</td>
<td>253</td>
<td>158</td>
<td>122</td>
<td rowspan="5">3.5178 Å</td>
<td rowspan="5">3.508 Å Exp [98].</td>
</tr>
<tr>
<td>Exp [97].</td>
<td>252</td>
<td>152</td>
<td>123</td>
</tr>
<tr>
<td>Exp [92].</td>
<td>250</td>
<td>150</td>
<td>120</td>
</tr>
<tr>
<td>MD [99]</td>
<td>240</td>
<td>140</td>
<td>140</td>
</tr>
<tr>
<td>DFT [100]</td>
<td>290</td>
<td>154</td>
<td>–</td>
</tr>
<tr>
<td>DFT [101]</td>
<td>287</td>
<td>155</td>
<td>150</td>
<td> </td>
<td> </td>
</tr>
<tr>
<td>This study</td>
<td>276.7</td>
<td>153.4</td>
<td>134.5</td>
<td> </td>
<td> </td>
</tr>
<tr>
<td rowspan="2">Cr</td>
<td colspan="4">This study</td>
<td>Literature</td>
</tr>
<tr>
<td> </td>
<td>C<sub>11</sub></td>
<td>C<sub>12</sub></td>
<td>C<sub>44</sub></td>
<td>a</td>
<td>a</td>
</tr>
<tr>
<td>Exp [102].</td>
<td>391</td>
<td>90.53</td>
<td>102</td>
<td rowspan="3">2.8473 Å</td>
<td rowspan="3">2.884 Å Exp [103].</td>
</tr>
<tr>
<td>Exp [104].</td>
<td>339.8</td>
<td>58.6</td>
<td>99.0</td>
</tr>
<tr>
<td>DFT [104]</td>
<td>340</td>
<td>59</td>
<td>100</td>
</tr>
<tr>
<td>DFT [101]</td>
<td>508</td>
<td>170</td>
<td>127</td>
<td> </td>
<td> </td>
</tr>
<tr>
<td>This study</td>
<td>505</td>
<td>134</td>
<td>106</td>
<td> </td>
<td> </td>
</tr>
<tr>
<td rowspan="2">Co</td>
<td colspan="6">This study</td>
<td colspan="2">Literature</td>
</tr>
<tr>
<td> </td>
<td>C<sub>11</sub></td>
<td>C<sub>12</sub></td>
<td>C<sub>13</sub></td>
<td>C<sub>33</sub></td>
<td>C<sub>44</sub></td>
<td>a</td>
<td>c/a</td>
<td>a</td>
<td>c/a</td>
</tr>
<tr>
<td>Exp [105].</td>
<td>307</td>
<td>165</td>
<td>103</td>
<td>358</td>
<td>75</td>
<td rowspan="3">2.4917 Å</td>
<td rowspan="3">1.6230</td>
<td>2.497 Å</td>
<td>–</td>
</tr>
<tr>
<td>Exp [106].</td>
<td>295</td>
<td>159</td>
<td>111</td>
<td>335</td>
<td>71</td>
<td>Exp [103].</td>
<td>Exp [103].</td>
</tr>
<tr>
<td>Exp [107].</td>
<td>306.3</td>
<td>165.1</td>
<td>101.9</td>
<td>357.4</td>
<td>75.3</td>
<td>2.51 Å</td>
<td>1.622</td>
</tr>
<tr>
<td>DFT [101]</td>
<td>353</td>
<td>188</td>
<td>116</td>
<td>443</td>
<td>63</td>
<td> </td>
<td> </td>
<td>Exp [108].</td>
<td>Exp [108].</td>
</tr>
<tr>
<td>DFT [109]</td>
<td>325</td>
<td>165</td>
<td>105</td>
<td>365</td>
<td>90</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
</tr>
<tr>
<td>DFT [109]</td>
<td>295</td>
<td>135</td>
<td>85</td>
<td>340</td>
<td>95</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
</tr>
<tr>
<td>This study</td>
<td>381.8</td>
<td>142.6</td>
<td>102.4</td>
<td>416</td>
<td>96.8</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
</tr>
<tr>
<td rowspan="2">Mo</td>
<td colspan="4">This study</td>
<td>Literature</td>
</tr>
<tr>
<td> </td>
<td>C<sub>11</sub></td>
<td>C<sub>12</sub></td>
<td>C<sub>44</sub></td>
<td>a</td>
<td>a</td>
</tr>
<tr>
<td>Exp [110].</td>
<td>450.02</td>
<td>172.92</td>
<td>125.03</td>
<td rowspan="6">3.1279 Å</td>
<td rowspan="6">3.147 Å [111]</td>
</tr>
<tr>
<td>Exp [112].</td>
<td>464.79</td>
<td>158</td>
<td>108.94</td>
</tr>
<tr>
<td>Exp [113].</td>
<td>463.0</td>
<td>161.1</td>
<td>103.8</td>
</tr>
<tr>
<td>DFT [114]</td>
<td>463</td>
<td>163</td>
<td>103</td>
</tr>
<tr>
<td>DFT [115]</td>
<td>459.7</td>
<td>161.1</td>
<td>103.8</td>
</tr>
<tr>
<td>DFT [116]</td>
<td>484.0</td>
<td>162.0</td>
<td>95.3</td>
</tr>
<tr>
<td>This study</td>
<td>408.9</td>
<td>173.3</td>
<td>76.2</td>
<td> </td>
<td> </td>
</tr>
</tbody>
</table>

less than 1% [59]. Only long-range lattice distortion effect, i.e. lattice dilation or contraction, is considered. Accordingly, in the present set of DFT calculations, only volumetric relaxations of the computational cells are performed, ionic relaxations are prohibited. Similar assumptions have been made in other studies in the literature and have yielded satisfactory results [42]. The soundness of our assumption will also be verified in Section 4 when the results of our calculations are compared with existing literature.

Once the CE is performed and the ECIs acquired, the energies of atomistic structures much larger than those considered in DFT calculations can be obtained. Using the Thermo-Calc software [60], a series of compositional ranges for all atomic types are determined, ensuring that throughout these ranges, no more than 5% of phases other than γ and γ' exist. Corresponding to the compositional ranges, Table 2 lists the number of atoms (given in parentheses) for each species present in the atomistic structures. To calculate APBE, atomistic structures containing 2160 atoms are created, duplicated along [111] and shifted to create {111} APBs (Fig. 3), and energy differences due to this operation measured. The dimensions of these duplicated structures along the crystallographic directions [10$\overline{1}$], [01$\overline{1}$], and [111] are 29.94 Å, 29.94 Å, and 72.89 Å, respectively (see Fig. 3). Structures of this size eliminate the interaction between the APBs from neighboring periodic cells, enable slight changes in the composition, and allow for the probing of dilute solutions. To compare, in the supercell approach which requires direct DFT calculations, the supercells only contain ~50 atoms [35].

The effect of the randomness in the distribution of solute atoms is addressed by MC sampling technique. In this work, MC sampling uses the metropolis algorithm and generates a minimum of 2500 different atomistic configurations at each composition. For compositions that converges slowly, as many as 6000 configurations are created. Whenever the spatial configuration changes, the energy of the structure can be determined using the ECIs. Starting from any given structure, the next attempted structure is randomly generated following the approach

**Table 2**
Compositions of $\gamma'$ phase considered in this study in the multicomponent cases (Section 4.3). Numbers give the at. % fraction of each element. Numbers in parentheses are the numbers of atoms included in the atomistic structures. Bold numbers correspond to the case of Inconel 939.

<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="5">Constant Ratio</th>
      <th colspan="5">Sacrificial Nickel</th>
    </tr>
    <tr>
      <th>Al</th>
      <th>2.56</th>
      <th>3.80</th>
      <th>4.19</th>
      <th>4.60</th>
      <th>5.60</th>
      <th>2.48</th>
      <th>3.60</th>
      <th>4.19</th>
      <th>4.60</th>
      <th>5.25</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Ni</td>
      <td>68.28 (1503)</td>
      <td>67.39 (1482)</td>
      <td><b>67.04 (1474)</b></td>
      <td>66.67 (1467)</td>
      <td>65.87 (1447)</td>
      <td>68.61 (1510)</td>
      <td>67.64 (1487)</td>
      <td><b>67.04 (1474)</b></td>
      <td>66.67 (1466)</td>
      <td>65.98 (1450)</td>
    </tr>
    <tr>
      <td>Al</td>
      <td>8.58 (189)</td>
      <td>10.00 (220)</td>
      <td><b>10.52 (231)</b></td>
      <td>11.05 (243)</td>
      <td>12.25 (269)</td>
      <td>8.51 (187)</td>
      <td>9.75 (214)</td>
      <td><b>10.52 (231)</b></td>
      <td>11.05 (243)</td>
      <td>11.84 (260)</td>
    </tr>
    <tr>
      <td>Ti</td>
      <td>13.88 (306)</td>
      <td>12.54 (276)</td>
      <td><b>12.03 (265)</b></td>
      <td>11.52 (253)</td>
      <td>10.36 (228)</td>
      <td>13.91 (306)</td>
      <td>12.79 (281)</td>
      <td><b>12.03 (265)</b></td>
      <td>11.52 (253)</td>
      <td>10.76 (236)</td>
    </tr>
    <tr>
      <td>Cr</td>
      <td>1.24 (27)</td>
      <td>1.54 (34)</td>
      <td><b>1.64 (36)</b></td>
      <td>1.75 (38)</td>
      <td>1.98 (43)</td>
      <td>1.21 (27)</td>
      <td>1.48 (33)</td>
      <td><b>1.64 (36)</b></td>
      <td>1.75 (38)</td>
      <td>1.91 (42)</td>
    </tr>
    <tr>
      <td>Co</td>
      <td>6.14 (135)</td>
      <td>6.74 (148)</td>
      <td><b>6.99 (154)</b></td>
      <td>7.25 (159)</td>
      <td>7.89 (173)</td>
      <td>5.88 (129)</td>
      <td>6.57 (144)</td>
      <td><b>6.99 (154)</b></td>
      <td>7.25 (159)</td>
      <td>7.83 (172)</td>
    </tr>
    <tr>
      <th>Ti</th>
      <th>2.00</th>
      <th>4.00</th>
      <th>4.38</th>
      <th>5.00</th>
      <th>5.50</th>
      <th>1.80</th>
      <th>3.60</th>
      <th>4.38</th>
      <th>4.80</th>
      <th>5.26</th>
    </tr>
    <tr>
      <td>Ni</td>
      <td>68.03 (1505)</td>
      <td>67.2 (1479)</td>
      <td><b>67.04 (1474)</b></td>
      <td>66.83 (1468)</td>
      <td>66.64 (1465)</td>
      <td>68.53 (1516)</td>
      <td>67.04 (1486)</td>
      <td><b>67.04 (1474)</b></td>
      <td>66.80 (1468)</td>
      <td>66.57 (1462)</td>
    </tr>
    <tr>
      <td>Al</td>
      <td>13.05 (289)</td>
      <td>10.87 (239)</td>
      <td><b>10.52 (231)</b></td>
      <td>10.00 (220)</td>
      <td>9.56 (212)</td>
      <td>11.20 (291)</td>
      <td>10.52 (247)</td>
      <td><b>10.52 (231)</b></td>
      <td>10.20 (231)</td>
      <td>9.88 (217)</td>
    </tr>
    <tr>
      <td>Ti</td>
      <td>8.51 (188)</td>
      <td>11.56 (254)</td>
      <td><b>12.03 (265)</b></td>
      <td>12.69 (279)</td>
      <td>13.18 (289)</td>
      <td>11.09 (183)</td>
      <td>12.03 (244)</td>
      <td><b>12.03 (265)</b></td>
      <td>12.46 (265)</td>
      <td>12.88 (283)</td>
    </tr>
    <tr>
      <td>Cr</td>
      <td>2.00 (44)</td>
      <td>1.68 (37)</td>
      <td><b>1.64 (36)</b></td>
      <td>1.59 (35)</td>
      <td>1.54 (34)</td>
      <td>1.70 (44)</td>
      <td>1.64 (37)</td>
      <td><b>1.64 (36)</b></td>
      <td>1.62 (36)</td>
      <td>1.58 (35)</td>
    </tr>
    <tr>
      <td>Co</td>
      <td>6.08 (134)</td>
      <td>6.86 (151)</td>
      <td><b>6.99 (154)</b></td>
      <td>7.20 (158)</td>
      <td>7.42 (163)</td>
      <td>6.61 (126)</td>
      <td>6.99 (146)</td>
      <td><b>6.99 (154)</b></td>
      <td>7.2 (154)</td>
      <td>7.45 (163)</td>
    </tr>
    <tr>
      <th>Cr</th>
      <th>9.00</th>
      <th>18.00</th>
      <th>24.35</th>
      <th>25.00</th>
      <th>26.47</th>
      <th>5.90</th>
      <th>9.00</th>
      <th>24.35</th>
      <th>25.00</th>
      <th>25.94</th>
    </tr>
    <tr>
      <td>Ni</td>
      <td>66.54 (1457)</td>
      <td>66.74 (1464)</td>
      <td><b>67.04 (1474)</b></td>
      <td>67.09 (1476)</td>
      <td>67.31 (1480)</td>
      <td>70.05 (1536)</td>
      <td>69.46 (1522)</td>
      <td><b>67.04 (1474)</b></td>
      <td>66.94 (1472)</td>
      <td>66.88 (1471)</td>
    </tr>
    <tr>
      <td>Al</td>
      <td>10.93 (239)</td>
      <td>10.66 (234)</td>
      <td><b>12.03 (265)</b></td>
      <td>10.51 (231)</td>
      <td>10.53 (232)</td>
      <td>10.71 (235)</td>
      <td>10.65 (234)</td>
      <td><b>12.03 (265)</b></td>
      <td>10.54 (231)</td>
      <td>10.60 (233)</td>
    </tr>
    <tr>
      <td>Ti</td>
      <td>11.26 (247)</td>
      <td>11.77 (258)</td>
      <td><b>12.03 (265)</b></td>
      <td>12.05 (265)</td>
      <td>12.00 (264)</td>
      <td>10.82 (237)</td>
      <td>11.15 (244)</td>
      <td><b>12.03 (265)</b></td>
      <td>12.02 (265)</td>
      <td>11.96 (263)</td>
    </tr>
    <tr>
      <td>Cr</td>
      <td>1.06 (23)</td>
      <td>1.47 (32)</td>
      <td><b>1.64 (36)</b></td>
      <td>1.66 (36)</td>
      <td>1.67 (37)</td>
      <td>0.75 (16)</td>
      <td>1.01 (22)</td>
      <td><b>1.64 (36)</b></td>
      <td>1.67 (36)</td>
      <td>1.68 (37)</td>
    </tr>
    <tr>
      <td>Co</td>
      <td>8.88 (194)</td>
      <td>7.81 (172)</td>
      <td><b>6.99 (154)</b></td>
      <td>6.89 (152)</td>
      <td>6.67 (147)</td>
      <td>6.21 (136)</td>
      <td>6.29 (138)</td>
      <td><b>6.99 (154)</b></td>
      <td>7.03 (154)</td>
      <td>7.08 (156)</td>
    </tr>
    <tr>
      <th>Co</th>
      <th>14.20</th>
      <th>16.50</th>
      <th>18.22</th>
      <th>30.00</th>
      <th>36.00</th>
      <th>5.00</th>
      <th>11.00</th>
      <th>18.22</th>
      <th>28.00</th>
      <th>43.00</th>
    </tr>
    <tr>
      <td>Ni</td>
      <td>68.95 (1519)</td>
      <td>67.85 (1493)</td>
      <td><b>67.04 (1474)</b></td>
      <td>61.24 (1339)</td>
      <td>58.23 (1271)</td>
      <td>72.98 (1619)</td>
      <td>70.69 (1557)</td>
      <td><b>67.04 (1474)</b></td>
      <td>59.49 (1305)</td>
      <td>42.03 (923)</td>
    </tr>
    <tr>
      <td>Al</td>
      <td>10.54 (232)</td>
      <td>10.52 (231)</td>
      <td><b>10.52 (231)</b></td>
      <td>10.76 (235)</td>
      <td>11.01 (240)</td>
      <td>9.52 (211)</td>
      <td>10.28 (227)</td>
      <td><b>10.52 (231)</b></td>
      <td>10.89 (239)</td>
      <td>11.28 (247)</td>
    </tr>
    <tr>
      <td>Ti</td>
      <td>11.82 (260)</td>
      <td>11.96 (263)</td>
      <td><b>12.03 (265)</b></td>
      <td>12.10 (265)</td>
      <td>11.93 (260)</td>
      <td>11.93 (265)</td>
      <td>11.91 (262)</td>
      <td><b>12.03 (265)</b></td>
      <td>12.10 (266)</td>
      <td>11.70 (257)</td>
    </tr>
    <tr>
      <td>Cr</td>
      <td>1.68 (37)</td>
      <td>1.66 (37)</td>
      <td><b>1.64 (36)</b></td>
      <td>1.58 (35)</td>
      <td>1.58 (34)</td>
      <td>1.51 (33)</td>
      <td>1.64 (36)</td>
      <td><b>1.64 (36)</b></td>
      <td>1.92 (42)</td>
      <td>3.18 (70)</td>
    </tr>
    <tr>
      <td>Co</td>
      <td>5.09 (112)</td>
      <td>6.16 (136)</td>
      <td><b>6.99 (154)</b></td>
      <td>13.08 (286)</td>
      <td>16.25 (355)</td>
      <td>1.45 (32)</td>
      <td>3.54 (78)</td>
      <td><b>6.99 (154)</b></td>
      <td>14.03 (308)</td>
      <td>30.18 (663)</td>
    </tr>
  </tbody>
</table>

![](./images/812700354717155328_3.jpg)

Fig. 3. A typical atomistic structure used to calculate APBE. The APB was created by shifting the top crystallite with respect to the lower crystallite by $a/2[1\overline{1}0]$.

outlined in Ref. [61]. If the new structure has less energy compared to the current one, the new structure will automatically be accepted. Otherwise, a probability $\exp(-\beta\Delta E)$, where $\Delta E$ is the energy difference between the structures, will be assigned for the acceptance of the new structure [48]. This has been done for multiple temperatures ranging from 300 K to 1300 K with 200 K intervals.

## 4. Results and discussion

In order to establish a baseline on the APBE of the ordered L1₂ precipitate, we first look into the case of a binary Ni₃Al alloy. Then, we investigate the isolated cases of single solute addition to the Ni₃Al structure resulting in ternary $\gamma'$ phases. Lastly, multicomponent cases representative of the variants of the Inconel 939 alloy, whose base composition is shown in Table 3 [62], are studied. A total of five separate CE listed in Table 4 are performed. The results of these studies—APBE—are presented as relative values (i.e. $\Delta\gamma_{\text{APB}}$) with respect to that of pure Ni₃Al for each case. Since a different CE is used for each ternary and multicomponent alloy case, a specific reference point of pure Ni₃Al APBE should be calculated using the corresponding CE. Note that although systematic errors exist in the DFT calculations as well as in CE, a significant portion of which can be canceled via the calculation of $\Delta\gamma_{\text{APB}}$. The concept of error cancelation can be rationalized by realizing the fact that the errors of the same origins in energy calculation exists in both the Ni₃Al reference point as well as target composition. Additional related discussions can be found in Refs. [29,48].

### 4.1. APBE of pure Ni₃Al $\gamma'$ phase

The APBE of pure Ni₃Al is first calculated based on a binary CE with the cross-validation score of 7.85 meV/atom—about a quarter of the typical reported values of $\sim$30 meV/atom [29,48]. ECIs are obtained by the volumetric relaxation of 95 different clusters. In a computational cell of Ni₃Al containing 4320 atoms, an APBE of 320.737 mJ/m² was obtained. The APBE of pure Ni₃Al and off-stoichiometry Ni₃Al reported in the literature is provided in Table 4. It is noted that although the APBE reported in this work significantly overestimates the experimental measurements ($\sim$195 mJ/m²), it largely agrees with other theoretical calculations, including both DFT and CE. It is also noted from Table 4 that several DFT based studies reported two APBE for pure Ni₃Al, a higher and a lower estimation, that correspond to idealized and fully-relaxed conditions. For the calculations performed in the idealized condition, all atoms in atomistic structure containing the APB still reside in a perfect FCC parent lattice. This condition is also inherent to all CE based approaches. However, the atomistic structure constructed from this pure geometrical consideration does not coincide with the true ground energy state. Indeed, a gamma-surface analysis revealed that minimum energy stacking in the APB deviates from a perfect FCC stacking [63]. Therefore, the in-plane atomic arrangement at the APB predicted by calculations performed under the "fully-relaxed" condition

**Table 3**
Base composition in wt%, of Inconel 939 [62].

| C    | Cr   | Co   | Mo    | W    | Ta   | Nb   | Al   | Ti    | Ni   |
|------|------|------|-------|------|------|------|------|-------|------|
| 0.15 | 22.4 | 19.0 | <0.01 | 2.02 | 1.45 | 1.05 | 2.00 | 3.71 | Bal. |

**Table 4**
Summary of the CE performed for the current study and a comparison of the obtained {111} APBE with literature.

| CE (This study)                          | Cross validation score (meV/atom) | Number of clusters relaxed | APBE of pure Ni₃Al (mJ/m²) |
|------------------------------------------|-----------------------------------|----------------------------|----------------------------|
| Ni-Al                                    | 0.007                             | 95                         | 320.737                    |
| Ni-Al-Ti-Co<sup>a</sup>                  | 0.028                             | 60                         | 208.749                    |
| Ni-Al-Ti-Cr                              | 0.029                             | 59                         | 221.705                    |
| Ni-Al-Ti-Mo                              | 0.032                             | 132                        | 252.858                    |
| Ni-Al-Ti-Cr-Co-Mo                        | 0.030                             | 498                        | 268.734                    |

| Literature: | Method       | Composition | APBE                  |
|-------------|--------------|-------------|-----------------------|
|             | DFT [76]     | Ni-25Al     | 223                   |
|             | DFT [73]     | Ni-25Al     | 240                   |
|             | DFT [71]     | Ni-25Al     | 270/210ᵇ              |
|             | DFT [63]     | Ni-25Al     | 220/172ᵇ              |
|             | DFT [77]     | Ni-25Al     | 306/188ᵇ              |
|             | DFT [82]     | Ni-25Al     | 152                   |
|             | DFT [42]     | Ni-25Al     | 315/181ᵇ              |
|             | DFT [46]     | Ni-25Al     | 344                   |
|             | DFT [30]     | Ni-25Al     | 310                   |
|             | CE [46,48]   | Ni-25Al     | 318                   |
|             | CE [55]      | Ni-25Al     | 300                   |
|             | Exp [117].   | Ni-24.2Al   | 194 ± 22ᶜ             |
|             | Exp [78].    | Ni-25Al     | 195 ± 13ᶜ             |
|             | Exp [79].    | Ni-25Al     | 180 ± 30ᵈ             |
|             | Exp [117].   | Ni-25.9Al   | 250 ± 29ᶜ             |
|             | PST [118,119]| Ni-25Al     | 135ᵉ                   |
|             | PST [20]     | Ni-25Al     | 161ᵉ                   |

ᵃ This cluster expansion is employed to study both the effect of individual Titanium and Cobalt solutes.
ᵇ The higher and lower values correspond to idealized and fully-relaxed conditions.
ᶜ Corrected values using either Cockayne correction or Image simulations.
ᵈ Uncorrected values.
ᵉ Values determined from the precipitation strengthening theories (PST).

tend to approach the realistic, experimental conditions. This is likely the origin of the discrepancy in APBE of pure Ni₃Al between the present work and the experiments.

However, it is also worth noting that the validity of the DFT calculations based on fully-relaxed condition may be debatable as the APBs always appear as ribbons in the $\gamma'$ phase and are always constrained by the surrounding media. Although lattice relaxations parallel to the APB may be permitted, the out-of-plane relaxation is inhibited. Indeed, in the case of CSF ribbons embedded in a $\gamma'$ phase, little changes (if any) in the {111} interplanar spacing parallel to APB can be resolved by high resolution (transmission electron microscopy) TEM imaging (see Fig. 3(d) of Ref. [64]).

Nevertheless, the goal of the present study is to assess the influence of composition and temperature on the APBE. It is expected that the systematic errors in the absolute APBE observed in this work exist in all calculations of APBE and, when the relative APBE $\Delta\gamma_{\text{APB}}$ is calculated, cancel to a large extent. Indeed, using DFT calculations, Crudden et al. [30] captured the effect of Ti addition on the $\Delta\gamma_{\text{APB}}$ which agreed with the experiments, even though they conducted their calculations under the idealized condition and reported an APBE value for pure Ni₃Al of 310 mJ/m².

### 4.2. Composition and temperature effects on APBE for ternary $\gamma'$ phase

For the ternary cases, the mixture of excessive third elements into the base Ni₃Al can result in the decomposition of the $\gamma'$ phase. To ensure that the APBE obtained from MC-based calculations are valid, the stability of the $\gamma'$ phase due to the introduction of solutes is first investigated using Thermo-Calc software with the TCNI8 database [60]. Fig. 4 shows the mole fraction of $\gamma'$ phase as a function of composition, which is given by the mole fraction of Al and the solute element. These solutes are all of the substitutional type [65]. It can be observed from Fig. 4 that the solutes prefer to form substitutes on certain atomic sites over others. As a guide to the eye, the red dashed lines correspond to the compositions in which the solute atoms only replace the Al atoms. Compositions above the diagonal lines correspond to substitutions of both Al and Ni by the solutes. The horizontal line of 25% of Al correspond to the substitution of Ni atoms. Compositions below the diagonal lines correspond to Al% + Solute% below 25% and suggest replacement of Al sites by Ni atoms. In the case of Ti (Fig. 4(a)), the coincidence (or near-coincidence) between the field of 100% $\gamma'$ and the dashed line suggests that the solute atoms prefer to replace aluminum atoms, which is in agreement with the literature [28,65]. In the cases of Cr and Mo, similar preferences can be observed (Fig. 4(b) and (d)). However, in the literature, the agreement on such preferences has not been well established [65-70]. In the case of Co, Fig. 4(c) suggests that the solute atoms simultaneously replace Al and Ni at an approximate ratio of 1:7 (green dashed line), giving strong preference to Ni sites. This is in qualitative agreement with the literature, although the latter suggests an exclusive preference of Co replacing Ni in $\gamma'$ phase [65]. According to these observations the exact compositions of the ternary $\gamma'$ alloys investigated in this work are shown in Table 5. As shown, the site preference is given to only Al for the cases of Ti, Cr, and Mo, whereas the site preference is given to only Ni for the case of Co.

The effect of the solutes, including Ti, Cr, Co, and Mo, on the APBE is shown in Fig. 5. Note that CEs performed for these cases led to slightly different APBE for pure Ni₃Al as shown in Table 4. Even though this is the case, these energies are still in agreement with the literature [42, 71-79]. The systematic errors associated with these energies are expected to be canceled to a large extent when $\Delta\gamma_{\text{APB}}$ is calculated, as will be shown later when the result of this work is compared to the literature.

**Effect of Ti:** For the case of Ti, eight different compositions ranging from 1% to 15% of Ti are considered (Fig. 5(a)). An increase in the amount of Ti results in a substantial increase in APBE. For low Ti fraction of 1%, the increase in APBE at room temperature is as low as 6 mJ/m². This value increases as Ti fraction increases and it is as high as 140 mJ/ m² at 15% of Ti. At each composition, an increase in temperature slightly reduces the value of $\Delta\gamma_{\text{APB}}$. For instance, an increase in temperature from room temperature to 1300 K leads to only a reduction of around 15 mJ/m². A comparison between the results of this work (for the case of Ti solutes at 300 K) and the literature has been provided in Fig. 6(a). Sun et al. [29] have studied the effect of both Ti and Hf impurities on the APBE of Ni₃Al. For 1% and 10% of Ti, they have reported a $\Delta\gamma_{\text{APB}}$ of 10 and 65 mJ/m², respectively, agreeing well with the present study. The agreement is also a testament of the soundness of the assumption made in this work that the effect of atomic-scale lattice distortion can be neglected. In Sun et al., similar reducing effect of temperature on $\Delta\gamma_{\text{APB}}$ has been witnessed. Wider compositional range, starting from pure Ni₃Al to a complete substitution of Al by Ti has been studied by Chandran et al. [42]. However, care should be taken when interpreting their results in the limit of complete Ti substitution of Al, as the stable phase for Ni₃Ti is D0₂₄, a hexagonal structure, instead of L1₂

![](./images/812700354717155328_4.jpg)

Fig. 4. Phase fractions of $\gamma'$ as functions of compositional adjustment in a ternary alloy Ni-Al-M. (a) M = Ti (b) M = Cr (c) M = Co (d) M = Mo. Elemental fractions are given in mole fractions.

<table>
<thead>
<tr>
<th>Ternary alloy</th>
<th>Solute Site Preference</th>
<th>Minimum solute fraction (%)</th>
<th>Maximum solute fraction (%)</th>
<th>Number of compositions</th>
</tr>
</thead>
<tbody>
<tr>
<td>Ni-Al-Ti</td>
<td>Al</td>
<td>1.00</td>
<td>15.00</td>
<td>8</td>
</tr>
<tr>
<td>Ni-Al-Cr</td>
<td>Al</td>
<td>0.1</td>
<td>9.0</td>
<td>7</td>
</tr>
<tr>
<td>Ni-Al-Co</td>
<td>Ni</td>
<td>1.0</td>
<td>23.0</td>
<td>6</td>
</tr>
<tr>
<td>Ni-Al-Mo</td>
<td>Al</td>
<td>0.1</td>
<td>7.0</td>
<td>6</td>
</tr>
</tbody>
</table>

[80]. In their study, using the reference {111} APBE of $315\,\text{mJ/m}^2$, the $\Delta\gamma_{\text{APB}}$ at 0 K is close to $300\,\text{mJ/m}^2$ for 15% Ti. The increasing effect on the APBE due to Ti addition into Ni₃Al $\gamma'$ has also been reported by Raynor et al. using precipitation strengthening theories [81]. It is also worth to note that part of results presented by Chandran et al. are based on "full-cell relaxation" which yields APBs in a stress-free state and inter planar spacing at APB distinct from the $\gamma'$ phase. As discussed at the beginning, This assumption might not be realistic as the APBs always appear as ribbons in the $\gamma'$ phase and are always constrained by surrounding media.

Further, increase in the APBE by addition of Ti to Ni₃Al has also been reported by several other works, including Vamsi et al. [82], Gorbatov et al. [28], and Crudden et al. [30] (Fig. 6(a)). The present work showed qualitative agreement with their results. Although the present work underestimates the experimental $\Delta\gamma_{\text{APB}}$ value reported by Kawabata et al. [83] at 10% Ti, it agrees well with the experimental measurement by Korner et al. [84].

Effect of Cr: A maximum of 9% Cr can be added to Ni₃Al before a new phase starts to appear. Seven different compositions ranging from 0.1 to 9% have been studied (Fig. 5(b)). At all temperatures, the presence of Cr reduces the APBE of the $\gamma'$ phase (reflected by negative values of $\Delta\gamma_{\text{APB}}$) and this reducing effect appears to be more significant at higher mole fractions. Like the case of Ti, increasing temperature seems to decrease the APBE. The temperature-induced reduction is more pronounced at temperatures above 800 K. Compared to the case of Ti (a maximum of $\Delta\gamma_{\text{APB}} = 140\,\text{mJ/m}^2$), the magnitude of reduction achieved by addition of Cr is merely $70\,\text{mJ/m}^2$. The findings of this work (at 300 K) have been compared to the literature in Fig. 6(b). In qualitative agreement with the present work, Crudden et al. [30] have also shown—using DFT calculations—that Cr reduces the overall APBE in the $\gamma'$ phase. However, the magnitude of reduction predicted by Crudden et al. ($\Delta\gamma_{\text{APB}}$ of $-15\,\text{mJ/m}^2$ at Cr fraction of 9%) is significantly less than that by the present work ($\Delta\gamma_{\text{APB}}$ of $-33\,\text{mJ/m}^2$ at Cr fraction of 9%) [30]. In contrast, Gorbatov et al., using CPA method (Method 2 introduced in Section 2), suggested that the APBE initially increases as a function of increasing Cr content, then drastically decreases beyond 5% of Cr [28].

Effect of Co: Co fractions ranging from 1% to 23%—a total of 6 compositions—have been assessed (see results presented in Fig. 5(c)). Similar to Cr, Co also tends to decrease the APBE. For Co fractions smaller than 10%, the reduction in APBE is very small and does not exceed $1.5\,\text{mJ/m}^2$. The decreasing effect appears to be stronger at Co fractions above 10%. Also similar to the previous cases, temperature rises tend to reduce the APBE. At room temperature, the maximum reduction in APBE is only $\sim20\,\text{mJ/m}^2$ (at Co fraction of 23%), while at 1300 K this reduction becomes $\sim50\,\text{mJ/m}^2$. Employing CPA method (Method 2 as introduced in Section 2), Gorbatov et al. [28] showed that the addition of Co up to 10% results in gradual, almost linear, reduction of the APBE. The comparison of results is provided in Fig. 6(c). As shown, at 10% of Co, Gorbatov et al. showed that the APBE reduced by $\sim20\,\text{mJ/m}^2$ – a rate significantly higher than the results of the present study.

![](./images/812700354717155328_5.jpg)

Fig. 5. Effect of Composition and Temperature change on the relative APB energy of ternary alloy. Single elements, including (a) Ti, (b) Cr, (c) Co, and (d) Mo are added to pure Ni₃Al phase.

**Effect of Mo:** For the case of Mo, six different compositions ranging from 0.1 to 7% have been considered. The effect of Mo addition to Ni₃Al on the APBE is shown in Fig. 5(d). An overall reducing effect similar to Cr and Co has been witnessed as a result of the Mo addition. The rate at which the Mo solutes reduce the APBE (~3 mJ/m² per percent mole fraction) is between that of Cr (~5 mJ/m² per percent mole fraction) and Co (~1.5 mJ/m² per percent mole fraction), c.f. Fig. 5(b), (c), and 5 (d). Temperature effects in the case of Mo are unique. Specifically, for compositions below 1%, $\Delta\gamma_{APB}$ stays constant up to 1000 K followed by a slight reduction at higher temperatures. For composition above 1%, an increase in temperature leads to an increase, a plateau, then a decrease in APBE. In other words, the reducing effect of temperature on APBE appears to be suppressed from room temperature (300 K) to intermediate (~800 K). Using DFT calculations, Crudden et al. have shown that the addition of Mo at 7% can reduce the APBE by ~12 mJ/m², which is in good agreement with this study, see Fig. 6(d) [30].

It is convenient to cast an understanding of the effect of individual elements on the APBE into an empirical relation that can be later used to predict the APBE of a multicomponent alloy. Following Crudden et al. [30], the relative APBE is assumed to be linearly dependent on the mole fraction of the solutes, i.e.

$$
\Delta\gamma_{APB}=\sum_{i=1}^{n}K_{i}X_{i}, \tag{7}
$$

where $K_{i}$ are the coefficients for the APBE change induced by each solute type (at mole fraction $x_{i}$ in $\gamma'$ phase). The coefficients $K_{i}\ (i=1,2,3,4)$ obtained from the linear fit of the data presented in Fig. 5 are provided in Table 6. It is apparent that Ti has the strongest (positive) influence on APBE, while Co has the weakest (negative) influence.

### 4.3. Composition and temperature effects on APBE for multicomponent $\gamma'$ phase

Having established a baseline on the effect of individual elements, the current section aims to elucidate the combined effect of multiple solutes on the APBE in the $\gamma'$ phase. We note that prior alloy design practices have heavily relied upon the knowledge of the individual solute elements, similar to that generated from Section 4.2, the mutual interactions among the solute elements have been assumed negligible [30]. Indeed, the scope of most prior research is confined to the effect of individual solute elements [28,46,48]. This work takes Inconel 939 (wt. % composition given in Table 3), a Ni-base superalloy that is primarily $\gamma'$ strengthened, as a model material system to investigate the effect of adjustment in solute mole fraction on the APBE. The composition of the $\gamma'$ phase according to Thermo-Calc is also given in Table 2. Although the Inconel 939 contains 7 major alloying elements (whose mole fraction > 1%), there are only Al, Ti, Cr, Co, and Mo with mole fraction > 1% in the $\gamma'$ phase. As elements may preferentially reside in either phases, increasing the overall fraction of an element does not necessarily lead to an increase of said element in the desired phase. In this work, only elements—other than Ni—in the $\gamma'$ phase with mole fraction above 1% will be considered for adjustment, including Al, Cr, Co, and Ti. Two adjustment strategies have been considered, i.e.

(1) Adjusting the mole fraction of one alloying element at the expense of Ni – dubbed "Sacrificial Ni",
(2) Adjusting the mole fraction of one alloying element while maintaining the ratio of all other elements – dubbed "Constant Ratio".

Strategy (1) is common among alloy design where the minor additives are introduced while the major base element appear as a balancing element. Strategy (2) becomes increasing important as additive

![](./images/812700354717155328_6.jpg)

Fig. 6. Comparison of relative APB energy in ternary alloys as a result of compositional variation obtained in this study with literature. Data points of this study correspond to the temperature of 300 K. Two black markers in (a) represents the results from experiments. The calculation of $\Delta \gamma_{\text{APB}}$ used absolute APB energy of 195 mJ/m² reported by Kruml [78] as reference.

Table 6
Fitted coefficients for Eqs. (7) and (8). The coefficients have the unit mJ/m². The root mean square errors (RMSE) evaluate the fit of Eqs. (7) and (8) (with the coefficients given in this table) for data shown in Figs. 7 and 8.

<table>
<thead>
<tr>
<th>T (K)</th>
<th>K1 (Ti)</th>
<th>K2 (Cr)</th>
<th>K3 (Co)</th>
<th>K4 (Mo)</th>
<th>F1 (Ti-Cr)</th>
<th>F2 (Ti-Co)</th>
<th>F3 (Cr-Co)</th>
<th>H (Ti-Cr-Co)</th>
<th>RMSE Eq. (7)</th>
<th>RMSE Eq. (8)</th>
</tr>
</thead>
<tbody>
<tr>
<td>500</td>
<td>8.862</td>
<td>−4.497</td>
<td>−1.229</td>
<td>−2.574</td>
<td>0.8166</td>
<td>0.0916</td>
<td>−4.337</td>
<td>0.3211</td>
<td>19.79</td>
<td>6.00</td>
</tr>
<tr>
<td>700</td>
<td>8.196</td>
<td>−4.793</td>
<td>−1.423</td>
<td>−2.495</td>
<td>0.6286</td>
<td>0.0954</td>
<td>−4.440</td>
<td>0.3724</td>
<td>24.17</td>
<td>4.90</td>
</tr>
<tr>
<td>900</td>
<td>8.011</td>
<td>−5.256</td>
<td>−1.574</td>
<td>−2.512</td>
<td>0.5223</td>
<td>0.0628</td>
<td>−5.266</td>
<td>0.4626</td>
<td>23.66</td>
<td>6.04</td>
</tr>
<tr>
<td>1100</td>
<td>7.795</td>
<td>−6.184</td>
<td>−1.838</td>
<td>−2.726</td>
<td>0.6641</td>
<td>0.0634</td>
<td>−5.681</td>
<td>0.4975</td>
<td>26.83</td>
<td>7.32</td>
</tr>
<tr>
<td>1300</td>
<td>7.560</td>
<td>−7.962</td>
<td>−2.410</td>
<td>−3.247</td>
<td>0.8702</td>
<td>0.1109</td>
<td>−5.532</td>
<td>0.4792</td>
<td>34.45</td>
<td>7.78</td>
</tr>
</tbody>
</table>

Table 7
Mole fractions of the $\gamma$ and $\gamma'$ phases as a result of overall compositional adjustments.

<table>
<tbody>
<tr>
<td colspan="12">
</td>
</tr>
<tr>
<td>Constant Ratio</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>Al</td>
<td>$\gamma$</td>
<td>$\gamma'$</td>
<td>Ti</td>
<td>$\gamma$</td>
<td>$\gamma'$</td>
<td>Cr</td>
<td>$\gamma$</td>
<td>$\gamma'$</td>
<td>Co</td>
<td>$\gamma$</td>
<td>$\gamma'$</td>
</tr>
<tr>
<td colspan="12">
</td>
</tr>
<tr>
<td>2.56</td>
<td>77.79</td>
<td>15.67</td>
<td>2</td>
<td>85.60</td>
<td>12.92</td>
<td>9</td>
<td>70.98</td>
<td>27.30</td>
<td>14.2</td>
<td>62.04</td>
<td>31.39</td>
</tr>
<tr>
<td>3.8</td>
<td>72.36</td>
<td>26.15</td>
<td>4</td>
<td>72.79</td>
<td>25.75</td>
<td>18</td>
<td>69.87</td>
<td>28.56</td>
<td>16.5</td>
<td>68.11</td>
<td>29.33</td>
</tr>
<tr>
<td>4.19</td>
<td>70.68</td>
<td>27.86</td>
<td>4.38</td>
<td>70.68</td>
<td>27.86</td>
<td>24.35</td>
<td>70.68</td>
<td>27.86</td>
<td>18.22</td>
<td>70.68</td>
<td>27.86</td>
</tr>
<tr>
<td>4.6</td>
<td>68.83</td>
<td>29.60</td>
<td>5</td>
<td>65.26</td>
<td>31.25</td>
<td>25</td>
<td>70.37</td>
<td>27.72</td>
<td>30</td>
<td>81.62</td>
<td>17.12</td>
</tr>
<tr>
<td>5.6</td>
<td>59.40</td>
<td>34.16</td>
<td>5.5</td>
<td>59.55</td>
<td>33.53</td>
<td>26.47</td>
<td>65.85</td>
<td>27.70</td>
<td>36</td>
<td>87.96</td>
<td>10.88</td>
</tr>
<tr>
<td colspan="12">
</td>
</tr>
<tr>
<td colspan="12">Sacrificial Nickel</td>
</tr>
<tr>
<td colspan="12">
</td>
</tr>
<tr>
<td>Al</td>
<td>$\gamma$</td>
<td>$\gamma'$</td>
<td>Ti</td>
<td>$\gamma$</td>
<td>$\gamma'$</td>
<td>Cr</td>
<td>$\gamma$</td>
<td>$\gamma'$</td>
<td>Co</td>
<td>$\gamma$</td>
<td>$\gamma'$</td>
</tr>
<tr>
<td colspan="12">
</td>
</tr>
<tr>
<td>2.48</td>
<td>78.83</td>
<td>14.68</td>
<td>1.8</td>
<td>87.96</td>
<td>10.61</td>
<td>5.9</td>
<td>88.51</td>
<td>10.08</td>
<td>5</td>
<td>64.69</td>
<td>31.97</td>
</tr>
<tr>
<td>3.6</td>
<td>73.43</td>
<td>24.81</td>
<td>3.6</td>
<td>75.35</td>
<td>23.20</td>
<td>9</td>
<td>83.46</td>
<td>15.12</td>
<td>11</td>
<td>69.97</td>
<td>28.60</td>
</tr>
<tr>
<td>4.19</td>
<td>70.68</td>
<td>27.86</td>
<td>4.38</td>
<td>70.68</td>
<td>27.86</td>
<td>24.35</td>
<td>70.68</td>
<td>27.86</td>
<td>18.22</td>
<td>70.68</td>
<td>27.86</td>
</tr>
<tr>
<td>4.6</td>
<td>68.03</td>
<td>29.77</td>
<td>4.8</td>
<td>66.85</td>
<td>30.29</td>
<td>25</td>
<td>69.52</td>
<td>28.14</td>
<td>28</td>
<td>72.06</td>
<td>25.45</td>
</tr>
<tr>
<td>5.25</td>
<td>60.47</td>
<td>33.01</td>
<td>5.26</td>
<td>60.49</td>
<td>32.82</td>
<td>25.94</td>
<td>64.83</td>
<td>28.68</td>
<td>43</td>
<td>78.60</td>
<td>17.19</td>
</tr>
<tr>
<td colspan="12">
</td>
</tr>
</tbody>
</table>

manufacturing (AM) based alloy design approaches maturity [10]. With powder-based AM, composition of alloys can be adjusted by mixing additives into base powders. The composition of the resulting alloy would then have increased mole fractions of the additives while the fractions of all other elements would reduce at a constant ratio. The compositions considered in this work—using Inconel 939 as a base alloy—following these two strategies have been provided in Table 2, along with the number of atoms in each species in the atomistic models. For adjustment of each element, 5 different compositions are considered. To ensure the completeness of understanding, not only addition of elements, but also reduction of them, are considered. Using Thermo-Calc, the limits within which an element can be adjusted is determined, ensuring formation of no more than 5% of any new phases (in addition to $\gamma$ and $\gamma'$) and no less than 10% of $\gamma'$ phase. The phase mole fractions of the $\gamma$ and $\gamma'$ phases corresponding to the overall compositional adjustment are given in Table 7.

A CE comprising 6 elements has been performed involving DFT calculation of the total energy of 498 periodic atomic clusters, resulting in ECIs with a cross-validation score of this CE 30 meV/atom. Based on this cluster expansion, the reference APBE of the pure Ni₃Al phase of $\gamma_{\text{APB}}=268\ \text{mJ/m}^2$ was obtained (Table 4). Results presented subsequently in this section, shown in Figs. 7 and 8, are the change in the APBE ($\Delta\gamma_{\text{APB}}$) based on this reference value. Due to the combined presence of alloying elements, the relative APBE ($\Delta\gamma_{\text{APB}}$) of the base Inconel 939 is $120\pm20\ \text{mJ/m}^2$ at the temperature range of 500 K ~ 1300 K.

**Effect of adjustments in Al:** An overall change in the fraction of Al, using both strategies, from ~2.5% to ~5.4% alters the concentration of Al inside $\gamma'$ phase from ~8% to ~12% (Table 2). As shown in Figs. 7(a) and 8(a), both temperature and adjustment in Al fraction have moderate effect on the APBE of the $\gamma'$ phase. An increase in temperature from 500 K to 1300 K reduces the $\Delta\gamma_{\text{APB}}$ by $20$–$30\ \text{mJ/m}^2$, while an increase from 8.0% to 12.0% of Al in $\gamma'$ phase leads to a drop in $\Delta\gamma_{\text{APB}}$ from $120\pm20$ to $90\pm10\ \text{mJ/m}^2$. This reducing effect of Al is expected as the increase in Al content in the $\gamma'$ phase reduces the fractions of other solutes. It is also noted from Figs. 7(a) and 8(a) that the two composition adjustment strategies resulted in very similar results.

**Effect of adjustments in Ti:** In the case of Ti, ~3% increase in the overall composition of Ti following both strategies, starting from ~2%, results in the change of Ti concentration inside $\gamma'$ phase from ~8% to ~13% (see Table 2). As shown in Figs. 7(b) and 8(b), an increase in temperature from 500 K to 1300 K slightly reduces the $\Delta\gamma_{\text{APB}}$ by $20\ \text{mJ/m}^2$. An increase in Ti composition drastically increases the APBE. In both strategies, with an increase of Ti fraction ranging from ~8.00% to ~13.00% in the $\gamma'$ phase, $\Delta\gamma_{\text{APB}}$ increased from ~$40\ \text{mJ/m}^2$ to ~$120\ \text{mJ/m}^2$. This behavior agrees with the observation made in the ternary case (Section 4.2) where the addition of Ti from 1 to 15% increased the APBE from ~6 to ~140 ($\text{mJ/m}^2$). The adjustment of Ti fraction using the two composition adjustment strategies resulted in very similar results.

**Effect of adjustments in Cr:** Using either compositional adjustment strategies, the overall fraction of Cr can vary from below 5% to above 25% without the formation of new phases. Variations of overall Cr fraction using both strategies resulted very similar, small variation in the composition in the $\gamma'$ phase (Table 2), i.e. from ~1% to 1.6%. It should be noted, however, that the phase fractions are significantly different via the two compositional adjustment strategies (Table 7). For all compositions obtained from Constant Ratio, $\gamma'$ phase fraction is almost constant and has a value of ~27%, while sacrificial Ni results in $\gamma'$ phase fraction ranging from ~10% to ~30%. The changes in composition, result in a slight increase in APBE by $20\ \text{mJ/m}^2$ at all temperature ranges (Figs. 7(c) and 8(c)). The increase in APBE is almost linear throughout the range of compositions. This trend is opposite to what has been witnessed before in the case of ternary $\gamma'$ phase. This is likely due to the fact that the actual variation of Cr in the $\gamma'$ phase is exceedingly small compared to that of Ti + Co, and that these variations (increase in Ti and decrease in Co) favors the increase in APBE. Consistent with observations made in other elemental adjustments, increase in temperature from 500 to 1300

![](./images/812700354717155328_7.jpg)

Fig. 7. Variation of relative APB energy of Inconel 939 by compositional modification, using "Constant Ratio" strategy. Figures (a), (b), (c), and (d) correspond to adjustments of Al, Ti, Cr, and Co elements. The compositions in the plots are the actual compositions in the $\gamma'$ phase.

![](./images/812700354717155328_8.jpg)

Fig. 8. Variation of relative APB energy of Inconel 939 by compositional modification, using "Sacrificial Ni" strategy. Figures (a), (b), (c), and (d) correspond to adjustment of Al, Ti, Cr, and Co elements. The compositions in the plots are the actual compositions in the $\gamma'$ phase.

K results in a moderate reduction in APBE of $20\ \text{mJ/m}^2$. Although adjustment of Cr under both strategies changes the APBE in a similar way, the "sacrificial Ni" strategy lead to a greater variation in the APBE (compare Figs. 7(c) and 8(c)).

Effect of adjustments in Co: As shown in Table 2, without the formation of a new phase, adjustment of the overall fraction of Co from ~15% to ~36% can be achieved using Constant Ratio strategy, which results in the concentration of Co inside $\gamma'$ phase changing from ~5% to 16%. On the other hand, a wider compositional range of overall and in-$\gamma'$ fractions of Co spanning from ~5% to ~43% can be achieved via Sacrificial Ni strategy, which leads to the concentration change of Co inside $\gamma'$ phase from ~1%-30%. Distinct from all other atomic species, one should note that the addition of Co using either strategy reduces the phase fraction of $\gamma'$ significantly (Table 7). As shown in Figs. 7(d) and 8 (d), similar to the cases of other elements, increase in temperature reduces the APBE by $\sim 20\ \text{mJ/m}^2$. Interestingly, APBE changes due to adjustment in Co have a nonmonotonic trend. As the change in fractions of all other elements (including Cr, Ti, and Al as shown in Table 2) favors the reduction of APBE, the initial increase in the APBE with increasing Co is likely due to the synergistic effect of the coexisting solutes. This suggests that the mutual interaction among solutes might not be negligible.

To illustrate, we first compare the relative APBE predicted by Eq. (7) with those obtained from CE at 500 K for multicomponent $\gamma'$ phases, as shown by the orange circles in Fig. 9. The $K_i$ parameters used were obtained by fitting the data presented in Section 4.2 (Table 6). The root-mean-squared error (RMSE) of the prediction is $\sim 20\ \text{mJ/m}^2$. To improve the accuracy of empirical prediction, Eq. (7) can be modified realizing that the multiple solute atoms in the $\text{Ni}_3\text{Al}$ phase may have significant mutual interaction. These interactions can be represented by "cross-terms" of two or more mole fractions of solutes, such as $x_{\text{Ti}}x_{\text{Cr}}$, $x_{\text{Ti}}x_{\text{Co}}$, $x_{\text{Co}}x_{\text{Cr}}$, and $x_{\text{Ti}}x_{\text{Cr}}x_{\text{Co}}$. Eq. (7) can, therefore, be rewritten as

![](./images/812700354717155328_9.jpg)

Fig. 9. Comparison of the predictive performance of Eq. (7) (without cross terms) and Eq. (8) (with cross terms).

$$
\Delta \gamma_{A P B}=\sum_{i=1}^{n} K_{i} x_{i}+F_{1} x_{T i} x_{C r}+F_{2} x_{T i} x_{C o}+F_{3} x_{C r} x_{C o}+H x_{T i} x_{C r} x_{C o}, \tag{8}
$$

where $K_i$ stands for the coefficients in Eq. (7) shown in Table 6, $F_i$ and $H$ are the coefficients for the binary and ternary cross-terms. At each temperature, based on the existing $K_i$, a set of $F_i$, and $H$ parameters can be obtained. With the added cross terms, the performance of the fit is substantially improved (blue diamonds in Fig. 9). The RMSE for the new fit using Eq. (8) is only $6\ \text{mJ/m}^2$. The parameters and RMSE of the fits for data at all temperatures are provided in Table 6. The same improvement in the performance of fits is evident in all temperatures.

Predictions made by Eq. (8) show good agreement with the literature. As was discussed before, this study focuses on the effect of alloying

on the relative APBE ($\Delta\gamma_{\text{APB}}$). Experimental measurement based on TEM reported APBE values of $180$-$250\ \text{mJ/m}^2$ for stoichiometric and near-stoichiometric $\text{Ni}_3\text{Al}$ (see Table 4). Using these values as reference, APBE measurement by Baither et al. [19] leads to $\Delta\gamma_{\text{APB}}=-34$-$100\ \text{mJ/m}^2$ for Nimonic-105 alloy and $\Delta\gamma_{\text{APB}}=8$-$170\ \text{mJ/m}^2$ for Nimonic-PE16 alloy. In this work, Eq. (8) predicts $-25\ \text{mJ/m}^2$ for Nimonic-105 and $124\ \text{mJ/m}^2$ for Nimonic-PE16. $^1$ We notice that Eq. (8) slightly under predicts the $\Delta\gamma_{\text{APB}}$ (within the scatter band) for Nimonic-105 and is in perfect agreement with experiments for Nimonic-PE16.

## 5. Conclusions

In this work, utilizing the ATAT toolkit, density functional theory-based cluster expansion (CE) calculations were performed combined with Monte Carlo sampling to investigate the effect of composition and temperate on the antiphase boundary energy of the $\gamma'$ phase. The effects of both individual solute elements in a ternary environment and the coexistence of multiple solute elements are systematically investigated. The following conclusions have been reached:

(1) In a ternary $\gamma'$ phase, i.e. $\text{Ni}_{3-x}\text{Al}_{1-y}\text{M}_{x+y}$, the addition of Ti significantly increases the APBE, while addition of Cr, Co and Mo all reduces the APBE. Per percent addition in mole fraction, Ti, Cr, Co, and Mo induce the change of APBE by $\sim140$, $\sim70$, $\sim50$, and $\sim25\ \text{mJ/m}^2$, respectively.

(2) The effect of temperature on the APBE depends on the composition. In most cases, temperature moderately decreases the APBE, by $20$-$40\ \text{mJ/m}^2$. Exceptions seem to be the additions of Ti or Mo into $\text{Ni}_3\text{Al}$ – where the effect of temperature change from $300\ \text{K}$ to $1300\ \text{K}$ only results in a minor fluctuation in APBE of $<5\ \text{mJ/m}^2$.

(3) The effect of individual solutes on the APBE energy obtained in an isolated, ternary condition (i.e. in $\text{Ni}_{3-x}\text{Al}_{1-y}\text{M}_{x+y}$) does not translate to a multi-solute environment. The mutual synergistic interactions among the solute are not negligible.

(4) Interaction between Cr and Co appears to be the strongest across all temperature ranges, while the interaction between Ti and Co is almost negligible. The binary Ti–Cr and ternary Ti–Cr–Co interactions are moderate.

(5) Empirical, master equations that predicts the APBE based on the composition of the $\gamma'$ phases are obtained from fitting of the present calculations.

## Declaration of competing interest

None.

## Acknowledgements

This material is based upon work supported by the U.S. Department of Energy, Office of Science, Office of Basic Energy Sciences, under Award Number DE-SC0019378. The authors also thank Prof. Axel van de Walle and Dr. Ruoshi Sun at Brown University for their kind input and helpful discussions. Portions of this research were conducted with high performance computing resources provided by Louisiana State University (http://www.hpc.lsu.edu).

## Appendix A. Supplementary data

Supplementary data to this article can be found online at https://doi.org/10.1016/j.intermet.2019.106670.

$^1$ We realize the existence of $3.2\%$ (at.) Fe in the $\gamma'$ phase of Nimonic-PE16. However, the effect of Fe on the APBE was shown to be small [41]. The dilute presence of Fe is therefore ignored in the present work.

## Disclaimer

This report was prepared as an account of work sponsored by an agency of the United States Government. Neither the United States Government nor any agency thereof, nor any of their employees, makes any warranty, express or implied, or assumes any legal liability or responsibility for the accuracy, completeness, or usefulness of any information, apparatus, product, or process disclosed, or represents that its use would not infringe privately owned rights. Reference herein to any specific commercial product, process, or service by trade name, trademark, manufacturer, or otherwise does not necessarily constitute or imply its endorsement, recommendation, or favoring by the United States Government or any agency thereof. The views and opinions of authors expressed herein do not necessarily state or reflect those of the United States Government or any agency FA R&D Special TC NOVEMBER 2017- FF Page 4 of 12 thereof.

## Credit author statement

M. Dodaran – Methodology, Validation, Formal analysis, Investigation, Visualization, Data curation, Writing - Original Draft.

A. Hemmasian Ettefagh – Methodology, Investigation, Formal analysis, Writing - Review & Editing.

S.M. Guo – Resources, Investigation, Supervision, Writing - Review & Editing.

M.M. Khonsari – Resources, Investigation, Supervision, Writing - Review & Editing.

W.J. Meng – Resources, Investigation, Supervision, Writing - Review & Editing.

N. Shamsaei –Resources, Investigation, Supervision, Writing - Review & Editing.

S. Shao – Conceptualization, Resources, Supervision, Project administration, Funding acquisition, Validation, Investigation, Visualization, Formal analysis, Writing - Original Draft, Writing - Review & Editing.

## References

[1] S.D. Antolovich, R. Bowman, The Effect of Microstructure on the Fatigue Crack Growth Resistance of Nickel Base Superalloys, TMS-AIME, Warrendale, PA, 1986.

[2] R.D. Field, T.M. Pollock, W.H. Murphy, The development of $\gamma/\gamma'$ interfacial dislocation networks during creep in Ni-base superalloys. Superalloys 1992, Seventh Int. Symp., TMS, 1992, pp. 557-566, https://doi.org/10.7449/1992/Superalloys_1992_557_566.

[3] H. Long, H. Wei, Y. Liu, S. Mao, J. Zhang, S. Xiang, Y. Chen, W. Gui, Q. Li, Z. Zhang, X. Han, Effect of lattice misfit on the evolution of the dislocation structure in Ni-based single crystal superalloys during thermal exposure, Acta Mater. 120 (2016) 95-107, https://doi.org/10.1016/j.actamat.2016.08.035.

[4] J. Oblak, D. Duvall, D. Paulonis, An estimate of the strengthening arising from coherent, tetragonally-distorted particles, Mater. Sci. Eng. 13 (1974) 51-56, https://doi.org/10.1016/0025-5416(74)90020-2.

[5] M. Sundararaman, P. Mukhopadhyay, S. Banerjee, Precipitation of the $\delta$-Ni$_3$Nb phase in two nickel base superalloys, Metall. Trans. A. 19 (1988) 453-465, https://doi.org/10.1007/BF02649259.

[6] P.M. Mignanelli, N.G. Jones, E.J. Pickering, O.M.D.M. Messé, C.M.F. Rae, M. C. Hardy, H.J. Stone, Gamma-gamma prime-gamma double prime dual-superlattice superalloys, Scr. Mater. 136 (2017) 136-140, https://doi.org/10.1016/j.scriptamat.2017.04.029.

[7] C. Slama, M. Abdellaoui, Structural characterization of the aged Inconel 718, J. Alloy. Comp. 306 (2000) 277-284, https://doi.org/10.1016/S0925-8388(00)00789-1.

[8] N. Baluc, R. Schäublin, Weak beam transmission electron microscopy imaging of superdislocations in ordered Ni $_3$ Al, Philos. Mag. A 74 (1996) 113-136, https://doi.org/10.1080/01418619608239693.

[9] C. Bathias, Fatigue Limit in Metals, John Wiley & Sons, Inc., Hoboken, NJ, 2014.

[10] S. Shao, M.M. Khonsari, S. Guo, W.J. Meng, N. Li, Overview: additive manufacturing enabled accelerated design of Ni-based alloys for improved fatigue life, Addit. Manuf. 29 (2019) 100779, https://doi.org/10.1016/j.addma.2019.100779.

[11] H. Mughrabi, Microstructural mechanisms of cyclic deformation, fatigue crack initiation and early crack growth, Philos. Trans. R. Soc. A Math. Phys. Eng. Sci. 373 (2015), https://doi.org/10.1098/rsta.2014.0132, 20140132-20140132.

M. Dodaran et al.
Intermetallics 117 (2020) 106670

[12] S. Shao, M.M. Khonsari, J. Wang, N. Shamsaei, N. Li, Frequency dependent deformation reversibility during cyclic loading, Mater. Res. Lett. 6 (2018) 390-397.

[13] M. Dodaran, M.M. Khonsari, S. Shao, Critical operating stress of persistent slip bands in Cu, Comput. Mater. Sci. 165 (2019) 114-120, https://doi.org/10.1016/ j.commatsci.2019.04.036.

[14] A.J. Ardell, Precipitation hardening, Metall. Trans. A. 16 (1985) 2131-2165, https://doi.org/10.1007/BF02670416.

[15] A.J. Ardell, M. Pozuelo, Disorder strengthening of ordered L1 2 alloys by face centered cubic (A1) precipitates, Intermetallics 88 (2017) 81-90, https://doi.org/ 10.1016/j.intermet.2017.05.010.

[16] R.W. Kozar, A. Suzuki, W.W. Milligan, J.J. Schirra, M.F. Savage, T.M. Pollock, Strengthening mechanisms in polycrystalline multimodal nickel-base superalloys, Metall. Mater. Trans. A 40 (2009) 1588-1603, https://doi.org/10.1007/s11661- 009-9858-5.

[17] A.J. Ardell, Chapter 12: Intermetallics as Precipitates and Dispersoids in High- Strength Alloys, John Wiley & Sons, Ltd., New York, 1994.

[18] B. Reppich, Some new aspects concerning particle hardening mechanisms in $\gamma'$ precipitating Ni-base alloys-I. Theoretical concept, Acta Metall. 30 (1982) 87-94, https://doi.org/10.1016/0001-6160(82)90048-7.

[19] D. Baither, C. Rentenberger, H.P. Karnthaler, E. Nembach, Three alternative experimental methods to determine the antiphase-boundary energies of the $\gamma'$ precipitates in superalloys, Philos. Mag. A 82 (2002) 1795-1805, https://doi.org/ 10.1080/01418610208235690.

[20] A. Ardell, C. Huang, Antiphase boundary energies and the transition from shearing to looping in alloys strengthened by ordered precipitates, Philos. Mag. Lett. 58 (1988) 189-197.

[21] E. Nembach, G. Neite, Precipitation hardening of superalloys by ordered $\gamma'$-particles, Prog. Mater. Sci. 29 (1985) 177-319, https://doi.org/10.1016/0079- 6425(85)90001-5.

[22] G. Molénat, D. Caillard, Dislocation mechanisms in Ni 3 Al at room temperature. In situ straining experiments in TEM, Philos. Mag. A 64 (1991) 1291-1317, https://doi.org/10.1080/01418619108225350.

[23] M.H. Yoo, On the theory of anomalous yield behavior of $Ni_3Al$ - effect of elastic anisotropy, Scr. Metall. 20 (1986) 915-920, https://doi.org/10.1016/0036-9748 (86)90466-7.

[24] M.H. Yoo, Stability of superdislocations and shear faults in L12 ordered alloys, Acta Metall. 35 (1987) 1559-1569, https://doi.org/10.1016/0001-6160(87) 90102-7.

[25] S.D. Antolovich, Microstructural aspects of fatigue in Ni-base superalloys, Philos. Trans. R. Soc. A Math. Phys. Eng. Sci. 373 (2015), https://doi.org/10.1098/ rsta.2014.0128, 20140128-20140128.

[26] B. Lawless, S.D. Antolovich, C. Bathias, B. Boursier, The effect of microstructure on the fatigue crack propagation and overload behavior of Waspaloy at room temperature, in: J.M. Wells, J.D. Landes (Eds.), Fract. Interact. Microstruct. Mech. Mech., The Metallurgical Society, Warrendale, PA, 1984, pp. 285-301.

[27] D.E. Laughlin, K. Hono (Eds.), Physical Metallurgy, fifth ed., Elsevier,, 2015 https://doi.org/10.1016/C2010-0-65716-6.

[28] O.I. Gorbatov, I.L. Lomaev, Y.N. Gornostyrev, A.V. Ruban, D. Furrer, V. Venkatesh, D.L. Novikov, S.F. Burlatsky, Effect of composition on antiphase boundary energy in $Ni_3Al$ based alloys ab initio calculations, Phys. Rev. B. 93 (2016) 224106, https://doi.org/10.1103/PhysRevB.93.224106.

[29] R. Sun, C. Woodward, A. van de Walle, First-principles study on $Ni_3Al$ (111) antiphase boundary with Ti and Hf impurities, Phys. Rev. B. 95 (2017) 214121, https://doi.org/10.1103/PhysRevB.95.214121.

[30] D.J. Crudden, A. Mottura, N. Warnken, B. Raeisinia, R.C. Reed, Modelling of the influence of alloy composition on flow stress in high-strength nickel-based superalloys, Acta Mater. 75 (2014) 356-370, https://doi.org/10.1016/j. actamat.2014.04.075.

[31] D. Caillard, N. Clément, A. Couret, P. Lours, A. Coujou, {111} Glide in Ni 3 Al at room temperature. In situ observations under weak-beam conditions, Philos. Mag. Lett. 58 (1988) 263-269, https://doi.org/10.1080/09500838808214763.

[32] Y. Mishin, Atomistic modeling of the $\gamma$ and $\gamma'$-phases of the Ni-Al system, Acta Mater. 52 (2004) 1451-1467, https://doi.org/10.1016/j.actamat.2003.11.026.

[33] B. Jelinek, S. Groh, M.F. Horstemeyer, J. Houze, S.G. Kim, G.J. Wagner, A. Moitra, M.I. Baskes, Modified embedded atom method potential for Al, Si, Mg, Cu, and Fe alloys, Phys. Rev. B. 85 (2012) 245102, https://doi.org/10.1103/ PhysRevB.85.245102.

[34] Sepideh Kavousi, B. Novak, M.I. Baskes, M. Asle Zaeem, D. Moldovan, MEAM potential for high temperature crystal-melt properties of Ti-Ni alloys and its application to phase field simulation of solidification, Model. Simul. Mater. Sci. Eng. (2019), https://doi.org/10.1088/1361-651X/ab580c.

[35] Y. Koizumi, S. Ogata, Y. Minamino, N. Tsuji, Energies of conservative and non- conservative antiphase boundaries in Ti 3 Al: a first principles study, Philos. Mag. 86 (2006) 1243-1259, https://doi.org/10.1080/14786430500380126.

[36] M. Chandran, S.K. Sondhi, First-principle calculation of stacking fault energies inNi and Ni-Co alloy, J. Appl. Phys. 109 (2011) 103525, https://doi.org/10.1063/ 1.3585786.

[37] W. Xu, A.P. Horsfield, D. Wearing, P.D. Lee, First-principles calculation of Mg/ MgO interfacial free energies, J. Alloy. Comp. 650 (2015) 228-238, https://doi. org/10.1016/j.jallcom.2015.07.289.

[38] T. Uesugi, K. Higashi, First-Principles calculation of grain boundary excess volume and free volume in nanocrystalline and ultrafine-grained aluminum, Mater. Trans. 54 (2013) 1597-1604, https://doi.org/10.2320/matertrans.L- M2013816.

[39] R. Namakian, G.Z. Voyiadjis, An atomic displacive model for {10-12}<-1011> twinning in hexagonal close packed metals with the emphasis on the role of partial stacking faults in formation of {10-12} twins, Acta Mater. 150 (2018) 381-393, https://doi.org/10.1016/j.actamat.2018.03.028.

[40] J. Wang, R.G. Hoagland, J.P. Hirth, A. Misra, Atomistic modeling of the interaction of glide dislocations with "weak" interfaces, Acta Mater. 56 (2008) 5685-5693, https://doi.org/10.1016/j.actamat.2008.07.041.

[41] K. Kumar, R. Sankarasubramanian, U.V. Waghmare, Tuning planar fault energies of $Ni_3Al$ with substitutional alloying: first-principles description for guiding rational alloy design, Scr. Mater. 142 (2018) 74-78, https://doi.org/10.1016/j. scriptamat.2017.08.021.

[42] M. Chandran, S.K. Sondhi, First-principle calculation of APB energy in Ni-based binary and ternary alloys, Model. Simul. Mater. Sci. Eng. 19 (2011), 025008, https://doi.org/10.1088/0965-0933/19/2/025008.

[43] S.K. Makineni, M. Lenz, S. Neumeier, E. Spiecker, D. Raabe, B. Gault, Elemental segregation to antiphase boundaries in a crept CoNi-based single crystal superalloy, Scr. Mater. 157 (2018) 62-66, https://doi.org/10.1016/j. scriptamat.2018.07.042.

[44] L. Vitos, Computational Quantum Mechanics for Materials Engineers, Springer London, London, 2007, https://doi.org/10.1007/978-1-84628-951-4.

[45] J.M. Sanchez, F. Ducastelle, D. Gratias, Generalized cluster description of multicomponent systems, Phys. A Stat. Mech. Its Appl. 128 (1984) 334-350, https://doi.org/10.1016/0378-4371(84)90096-7.

[46] R. Sun, C. Woodward, A. van de Walle, First-principles study on N3Al (111) antiphase boundary with Ti and Hf impurities, Phys. Rev. B. 95 (2017) 214121, https://doi.org/10.1103/PhysRevB.95.214121.

[47] Z.W. Lu, S.-H. Wei, A. Zunger, S. Frota-Pessoa, L.G. Ferreira, First-principles statistical mechanics of structural stability of intermetallic compounds, Phys. Rev. B. 44 (1991) 512-544, https://doi.org/10.1103/PhysRevB.44.512.

[48] R. Sun, A. van de Walle, Automating impurity-enhanced antiphase boundary energy calculations from ab initio Monte Carlo, Calphad 53 (2016) 20-24, https://doi.org/10.1016/j.calphad.2016.02.005.

[49] A. Van De Walle, M. Asta, First-principles investigation of perfect and diffuse antiphase boundaries in HCP-based Ti-Al alloys, Metall. Mater. Trans. A. 33 (2002) 735-741, https://doi.org/10.1007/s11661-002-1002-8.

[50] M. Rahaman, V.I. Razumovskiy, B. Johansson, A.V. Ruban, Temperature dependence of stacking-fault and anti-phase boundary energies in Al Sc from ab initio calculations, Philos. Mag. 93 (2013) 3423-3441, https://doi.org/10.1080/ 14786435.2013.810817.

[51] C. Amador, J.J. Hoyt, B.C. Chakoumakos, D. de Fontaine, Theoretical and experimental study of relaxations in $Al_3Ti$ and $Al_3Zr$ ordered phases, Phys. Rev. Lett. 74 (1995) 4955-4958, https://doi.org/10.1103/PhysRevLett.74.4955.

[52] A.T. Paxton, H.M. Polatoglou, Origin of the modulated phase in copper-gold alloys, Phys. Rev. Lett. 78 (1997) 270-273, https://doi.org/10.1103/ PhysRevLett.78.270.

[53] C. Colinet, A. Pasturel, Structural stability of one-dimensional long-period structures in the TiAl3 compound, J. Phys. Condens. Matter 14 (2002) 311, https://doi.org/10.1088/0953-8984/14/26/311.

[54] P.J.H. Denteneer, W. van Haeringen, Stacking-fault energies in semiconductors from first-principles calculations, J. Phys. C Solid State Phys. 20 (1987) L883-L887, https://doi.org/10.1088/0022-3719/20/32/001.

[55] M. Sluiter, Y. Hashi, Y. Kawazoe, The effect of segregation and partial order on the thermodynamics of (111) antiphase boundaries in $Ni_3Al$, Comput. Mater. Sci. 14 (1999) 283-290, https://doi.org/10.1016/S0927-0256(98)00120-7.

[56] R.E. Smallman, R.J. Bishop, Modern Physical Metallurgy and Materials Engineering, Elsevier, 1999, https://doi.org/10.1016/B978-0-7506-4564-5. X5000-9.

[57] A. van de Walle, M.D. Asta, A. Walle, G. Ceder, Automating first-principles phase diagram calculations, J. Phase Equilibria 23 (2002) 348-359, https://doi.org/ 10.1361/10549710277031596.

[58] G. Prandini, A. Marrazzo, I.E. Castelli, M. Nounet, N. Marzari, Precision and efficiency in solid-state pseudopotential calculations, Npj Comput. Mater. 4 (2018) 72, https://doi.org/10.1038/s41524-018-0127-2.

[59] U. Scheuer, B. Lengeler, Lattice distortion of solute atoms in metals studied by x- ray-absorption fine structure, Phys. Rev. B. 44 (1991) 9883-9894, https://doi. org/10.1103/PhysRevB.44.9883.

[60] J.-O. Andersson, T. Helander, L. Höglund, P. Shi, B. Sundman, Thermo-Calc & DICTRA, computational tools for materials science, Calphad 26 (2002) 273-312, https://doi.org/10.1016/S0364-5916(02)00037-8.

[61] A. van de Walle, M. Asta, Self-driven lattice-model Monte Carlo simulations of alloy thermodynamic properties and phase diagrams, Model. Simul. Mater. Sci. Eng. 10 (2002) 521-538, https://doi.org/10.1088/0965-0933/10/5/304.

[62] G. Sjoberg, D. Imamovic, J. Gabel, O. Caballero, J.W. Brooks, J.-P. Ferte,A. Lugan, Evaluation of the IN 939 alloy for large aircraft engine structures, in: Superalloys 2004 - Tenth Int. Symp, 2004, pp. 441-450, https://doi.org/ 10.7449/2004/Superalloys_2004_441_450. TMS.

[63] G. Schocek, S. Kohlhammer, M. Fahnle, Planar dissociations and recombination energy of [110] superdislocations in Ni 3 Al: generalized Peierls model in combination with ab initio electron theory, Philos. Mag. Lett. 79 (1999) 849-857, https://doi.org/10.1080/095008399176544.

[64] S.Y. Yuan, Z.H. Jiang, J.Z. Liu, Y. Tang, Y. Zhang, Nano-twinning in a $\gamma'$ precipitate strengthened Ni-based superalloy, Mater. Res. Lett. 6 (2018) 683-688, https://doi.org/10.1080/21663831.2018.1538021.

[65] M.H.F. Sluiter, Y. Kawazoe, Site preference of ternary additions in $Ni_3Al$, Phys. Rev. B. 51 (1995) 4062-4073, https://doi.org/10.1103/PhysRevB.51.4062.

[66] S. Ochial, Y. Oya, T. Suzuki, Alloying behaviour of $Ni_3Al$, $Ni_3Ga$, $Ni_3Si$ and $Ni_3Ge$, Acta Metall. 32 (1984) 289-298, https://doi.org/10.1016/0001-6160(84)90057-9.

[67] E.S. Machlin, J. Shao, Quaternary gamma-prime (L12) pseudobinary properties as revealed by the ionicity modified pair potential model, Scr. Metall. 11 (1977) 859-862, https://doi.org/10.1016/0036-9748(77)90338-6.

[68] C. Wolverton, D. de Fontaine, Site substitution of ternary additions to $Ni_3Al$ ($\gamma'$) from electronic-structure calculations, Phys. Rev. B. 49 (1994) 12351-12354, https://doi.org/10.1103/PhysRevB.49.12351.

[69] W.T. Loomis, J.W. Freeman, D.L. Sponseller, The influence of molybdenum on the $\gamma'$/phase in experimental nickel-base superalloys, Metall. Mater. Trans. B 3 (1972) 989-1000, https://doi.org/10.1007/BF02647677.

[70] D. Blavette, A. Bostel, Phase composition and long range order in $\gamma'$ phase of a nickel base single crystal superalloy CMSX2: an atom probe study, Acta Metall. 32 (1984) 811-816, https://doi.org/10.1016/0001-6160(84)90154-8.

[71] O.N. Mryasov, Y.N. Gornostyrev, M. van Schilfgaarde, A.J. Freeman, Superdislocation core structure in L12 $Ni_3Al$, $Ni_3Ge$ and $Fe_3Ge$: peierls-Nabarro analysis starting from ab-initio GSF energetics calculations, Acta Mater. 50 (2002) 4545-4554, https://doi.org/10.1016/S1359-6454(02)00282-3.

[72] Y. Mishin, Atomistic modeling of the $\gamma$ and $\gamma'$-phases of the Ni-Al system, Acta Mater. 52 (2004) 1451-1467, https://doi.org/10.1016/j.actamat.2003.11.026.

[73] N.M. Rosengaard, H.L. Skriver, Ab initio study of antiphase boundaries and stacking faults in L 1 2 and DO 22 compounds, Phys. Rev. B. 50 (1994) 4848-4858, https://doi.org/10.1103/PhysRevB.50.4848.

[74] V.R. Manga, J.E. Saal, Y. Wang, V.H. Crespi, Z.-K. Liu, Magnetic perturbation and associated energies of the antiphase boundaries in ordered $Ni_3Al$, J. Appl. Phys. 108 (2010) 103509, https://doi.org/10.1063/1.3513988.

[75] X.-X. Yu, C.-Y. Wang, Effect of alloying element on dislocation cross-slip in $\gamma$-Ni 3 Al: a first-principles study, Philos. Mag. 92 (2012) 4028-4039, https://doi.org/10.1080/14786435.2012.700419.

[76] J. Wang, H. Sehitoglu, Dislocation slip and twinning in Ni-based L12 type alloys, Intermetallics 52 (2014) 20-31, https://doi.org/10.1016/j. intermet.2014.03.009.

[77] A.T. Paxton, Y.Q. Sun, The role of planar fault energy in the yield anomaly in L12 intermetallics, Philos. Mag. A 78 (1998) 85-104, https://doi.org/10.1080/014186198253697.

[78] T. Kruml, From dislocation cores to strength and work-hardening: a study of binary $Ni_3Al$, Acta Mater. 50 (2002) 5091-5101, https://doi.org/10.1016/S1359-6454(02)00364-6.

[79] P. Veyssiere, J. Douin, P. Beauchamp, On the presence of super lattice intrinsic stacking faults in plastically deformed Ni 3 Al, Philos. Mag. A 51 (1985) 469-483, https://doi.org/10.1080/01418618508237567.

[80] K. Hagihara, T. Nakano, Y. Umakoshi, Plastic deformation behaviour in $Ni_3Ti$ single crystals with DO24 structure, Acta Mater. 51 (2003) 2623-2637, https:// doi.org/10.1016/S1359-6454(03)00060-0.

[81] D. Raynor, J.M. Silcock, Strengthening mechanisms in $\gamma'$ precipitating alloys, Met. Sci. J. 4 (1970) 121-130, https://doi.org/10.1179/ msc.1970.4.1.121.

[82] K.V. Vamsi, S. Karthikeyan, Effect of off-stoichiometry and ternary additions on planar fault energies in Ni 3 Al, in: Superalloys 2012, John Wiley & Sons, Inc., Hoboken, NJ, USA, 2012, pp. 521-530, https://doi.org/10.1002/9781118516430.ch57.

[83] T. Kawabata, D. Shindo, K. Hiraga, High-resolution TEM observations of superdislocations in $Ni_3(Al, Ti)$, Mater. Trans., JIM 33 (1992) 565-570, https:// doi.org/10.2320/matertrans1989.33.565.

[84] A. Korner, Weak-beam study of superlattice dislocations moving on cube planes in Ni 3 (Al, Ti) deformed at room temperature, Philos. Mag. A 58 (1988) 507-522, https://doi.org/10.1080/01418618808210427.

[85] J. Vallin, M. Mongy, K. Salama, O. Beckman, Elastic constants of aluminum, J. Appl. Phys. 35 (1964) 1825-1826, https://doi.org/10.1063/1.1713749.

[86] G.N. Kamm, G.A. Alers, Low-temperature elastic moduli of aluminum, J. Appl. Phys. 35 (1964) 327-330, https://doi.org/10.1063/1.1713309.

[87] V.N. Staroverov, G.E. Scuseria, J. Tao, J.P. Perdew, Tests of a ladder of density functionals for bulk solids and surfaces, Phys. Rev. B. 69 (2004), 075102, https:// doi.org/10.1103/PhysRevB.69.075102.

[88] J.H. Westbrook, R.L. Fleischer (Eds.), Intermetallic Compounds - Principles and Practice, John Wiley & Sons, Ltd, Chichester, UK, 2002, https://doi.org/10.1002/0470845856.

[89] Y. Le Page, P. Saxe, Symmetry-general least-squares extraction of elastic data for strained materials from ab initio calculations of stress, Phys. Rev. B. 65 (2002) 104104, https://doi.org/10.1103/PhysRevB.65.104104.

[90] G.J. Ackland, X. Huang, K.M. Rabe, First-principles thermodynamics of transition metals: W, NiAl, and PdTi, Phys. Rev. B. 68 (2003) 214104, https://doi.org/10.1103/PhysRevB.68.214104.

[91] E.S. Fisher, C.J. Renken, Single-crystal elastic moduli and the hcp -> bcc transformation in Ti, Zr, and Hf, Phys. Rev. 135 (1964) A482-A494, https://doi. org/10.1103/PhysRev.135.A482.

[92] P. Paufler, Landolt-börnstein, new series, K. H. Hellwege (ed.), group III: crystal and solid state physics, vol. 12: magnetic and other properties of oxides and related compounds, part c: hexagonal ferrites. Special lanthanide and actinide compounds, Springer-Verlag, Cryst. Res. Technol 18 (1983), https://doi.org/10.1002/crat.2170181220, 1546-1546.

[93] R.M. Wood, The lattice constants of high purity alpha titanium, Proc. Phys. Soc. 80 (1962) 783-786, https://doi.org/10.1088/0370-1328/80/3/323.

[94] C. Bercegeay, S. Bernard, First-principles equations of state and elastic properties of seven metals, Phys. Rev. B. 72 (2005) 214101, https://doi.org/10.1103/ PhysRevB.72.214101.

[95] U. Arganan, E. Eidelstein, O. Levy, G. Makov, Thermodynamic properties of titanium from ab initio calculations, Mater. Res. Express 2 (2015), 016505, https://doi.org/10.1088/2053-1591/2/1/016505.

[96] A.T. Raji, S. Scandolo, R. Mazzarello, S. Nsengiyumva, M. Härting, D.T. Britton, Ab initio pseudopotential study of vacancies and self-interstitials in hcp titanium, Philos. Mag. 89 (2009) 1629-1645, https://doi.org/10.1080/14786430903019032.

[97] J.R. Neighbours, F.W. Bratten, C.S. Smith, The elastic constants of nickel, J. Appl. Phys. 23 (1952) 389-393, https://doi.org/10.1063/1.1702218.

[98] C. Kittel, Introduction to Solid State Physics, 8th Ed., Wiley, Hoboken, NJ, 2005 https://doi.org/10.1007/978-3-540-93804-0.

[99] T. Cain, B.M. Pettitt, Elastic constants of nickel: variations with respect to temperature and pressure, Phys. Rev. B. 39 (1989) 12484-12491, https://doi. org/10.1103/PhysRevB.39.12484.

[100] K. Kociskova, P. Ballo, Atomic calculation of elastic constants for fcc metals: ab- initio and semiempirical approach, Kovoe Mater 45 (2007) 81-84.

[101] H. Wang, G. Guo, Gradient-corrected density functional calculation of structural and magnetic properties of BCC, FCC and HCP Cr, J. Magn. Magn. Mater. 209 (2000) 98-99, https://doi.org/10.1016/S0304-8853(99)00654-X.

[102] D.I. Bolef, J. de Klerk, Anomalies in the elastic constants and thermal expansion of chromium single crystals, Phys. Rev. 129 (1963) 1063-1067, https://doi.org/10.1103/PhysRev.129.1063.

[103] P. Janthon, S.(Andy) Luo, S.M. Kozlov, F. Viñes, J. Limtrakul, D.G. Truhlar, F. Illas, Bulk properties of transition metals: a challenge for the design of universal density functionals, J. Chem. Theory Comput. 10 (2014) 3832-3839, https://doi. org/10.1021/ct500532v.

[104] A. Sumer, J.F. Smith, A comparison of the elastic constants of chromium as determined from diffuse X-ray and ultrasonic techniques, J. Appl. Phys. 34 (1963) 2691-2694, https://doi.org/10.1063/1.1729792.

[105] G.R. Harp, R.F.C. Farrow, D. Weller, T.A. Rabedeau, R.F. Marks, Unusual stability of fcc Co(110)/Cu(110), Phys. Rev. B. 48 (1993) 17538-17544, https://doi.org/10.1103/PhysRevB.48.17538.

[106] R.F. Hearmon, The elastic constants of anisotropic materials-II, Adv. Phys. (1956) 323-382.

[107] A.R. Wazzan, A. Bristoti, L.B. Robinson, A. Ahmedieh, Temperature dependence of the single-crystal elastic constants of Co-rich Co-Fe alloys, J. Appl. Phys. 44 (1973) 2018-2024, https://doi.org/10.1063/1.1662508.

[108] Appendix E: Parameter Tables of Crystals, in: Crystallogr. Surf. Struct, Wiley-VCH Verlag GmbH & Co. KGaA, Weinheim, Germany, 2011, pp. 265-266, https://doi. org/10.1002/9783527633296.app5.

[109] G. Steinle-Neumann, L. Stixrude, R.E. Cohen, First-principles elastic constants for the hcp transition metals Fe, Co, and Re at high pressure, Phys. Rev. B. 60 (1999) 791-799, https://doi.org/10.1103/PhysRevB.60.791.

[110] F.H. Featherston, J.R. Neighbours, Elastic constants of tantalum, tungsten, and molybdenum, Phys. Rev. 130 (1963) 1324-1333, https://doi.org/10.1103/ PhysRev.130.1324.

[111] V. Milman, B. Winkler, J.A. White, C.J. Pickard, M.C. Payne, E.V. Akhmatskaya, R.H. Nobes, Electronic structure, properties, and phase stability of inorganic crystals: a pseudopotential plane-wave study, Int. J. Quantum Chem. 77 (2000) 895-910, https://doi.org/10.1002/(sici)1097-461x(2000)77:5<895::aid- qua10>3.0.co;2-c, doi:10.1002/(SICI)1097-461X(2000)77:5<895::AID- QUA10>3.0.CO;2-C.

[112] K.W. Katahara, M.H. Manghnani, E.S. Fisher, Pressure derivatives of the elastic moduli of BCC Ti-V-Cr, Nb-Mo and Ta-W alloys, J. Phys. F Met. Phys. 9 (1979) 773-790, https://doi.org/10.1088/0305-4608/9/5/006.

[113] S. Allard, Metals, Thermal and Mechanical Data, Pergamon, 1969.

[114] L. Koci, Y. Ma, A.R. Oganov, P. Souvatzis, R. Ahuja, Elasticity of the superconducting metals V, Nb, Ta, Mo, and W at high pressure, Phys. Rev. B. 77 (2008) 214101, https://doi.org/10.1103/PhysRevB.77.214101.

[115] H. Ikehata, N. Nagasako, T. Furuta, A. Fukumoto, K. Miwa, T. Saito, First- principles calculations for development of low elastic modulus Ti alloys, Phys. Rev. B. 70 (2004) 174113, https://doi.org/10.1103/PhysRevB.70.174113.

[116] Z. Liu, J. Shang, First principles calculations of electronic properties and mechanical properties of bcc molybdenum and niobium, Rare Met. 30 (2011) 354-358, https://doi.org/10.1007/s12598-011-0302-9.

[117] D.M. Dimiduk, A.W. Thompson, J.C. Williams, The compositional dependence of antiphase-boundary energies and the mechanism of anomalous flow in Ni 3 Al alloys, Philos. Mag. A 67 (1993) 675-698, https://doi.org/10.1080/01418619308207184.

[118] A. Ardell, Order hardening: comparison between revised theory and experiment, Met. Sci. J. 14 (1980) 221-224.

[119] M. Grohlich, P. Haasen, G. Frommeyer, Precipitation hardening of NiAl by large volume fractions of $\gamma'$, Scr. Metall. 16 (1982) 367-370.
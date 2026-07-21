![](./images/813205441000505344_1.jpg)

Theoretical prediction of universal curves for carrier transport in Si / SiO 2 ( 100 )
interfaces

Takamitsu Ishihara and Koichi Kato

Citation: Journal of Applied Physics 114, 053713 (2013); doi: 10.1063/1.4817791
View online: http://dx.doi.org/10.1063/1.4817791
View Table of Contents: http://scitation.aip.org/content/aip/journal/jap/114/5?ver=pdfcov
Published by the AIP Publishing

---

Articles you may be interested in
Nanoscale probing of dielectric breakdown at SiO 2 / 3 C-SiC interfaces
J. Appl. Phys. 109, 013707 (2011); 10.1063/1.3525806

Transport properties of a spin-split two-dimensional electron gas in an In 0.53 Ga 0.47 As In P quantum well
structure
J. Appl. Phys. 106, 073722 (2009); 10.1063/1.3244613

One-step synthesis of Ge – SiO 2 core-shell nanowires
Appl. Phys. Lett. 94, 083109 (2009); 10.1063/1.3089235

Ultraviolet and blue photoluminescence from sputter deposited Ge nanocrystals embedded in SiO 2 matrix
J. Appl. Phys. 103, 103534 (2008); 10.1063/1.2930877

Carrier compensation and scattering mechanisms in Si-doped In As y P 1 y layers grown on InP substrates
using intermediate In As y P 1 y step-graded buffers
J. Appl. Phys. 100, 063705 (2006); 10.1063/1.2349358

---

![](./images/813205441000505344_2.jpg)

[This article is copyrighted as indicated in the article. Reuse of AIP content is subject to the terms at: http://scitation.aip.org/termsconditions. Downloaded to ] IP:
155.33.16.124 On: Fri, 03 Oct 2014 12:04:39

# Theoretical prediction of universal curves for carrier transport in $Si/SiO_2(100)$ interfaces
Takamitsu Ishihara$^{a)}$ and Koichi Kato
Advanced LSI Technology Laboratory, Corporate Research & Development Center, Toshiba Corporation,
1 Komukai Toshiba-cho, Saiwai-ku, Kawasaki 212-8582, Japan

(Received 15 May 2013; accepted 23 July 2013; published online 7 August 2013)

Atomic structure dependence of carrier transport in $Si/SiO_2$ interface has been extensively studied. It is shown by first-principles calculations that a strong Si-O dipole is formed at the interface, and the polarized interface Si-O dipole becomes the origin of the dipole scattering. A physics-based dipole scattering model, which considers the inelastic scattering due to the vibrated dipole as well as the elastic scattering, is proposed. In particular, it is found that Si atom that forms the Si-O dipole vibrates parallel to the interface and becomes the origin of the inelastic dipole scattering. By performing the mobility calculation based on relaxation-time approximation, it is shown that the interface Si-O dipole has a significant influence on the carrier mobility in the inversion layer, and that the interface Si-O dipole scattering is one of the main scattering components that limit the carrier transport in the inversion layer, in addition to the conventional scattering components: the substrate impurity scattering, the bulk phonon scattering, and the surface roughness scattering. Upon incorporation of the Si-O dipole scattering, universal curves have been fully predicted. © 2013 AIP Publishing LLC. [http://dx.doi.org/10.1063/1.4817791]

## I. INTRODUCTION

Interface engineering, a key technological issue arising from the miniaturization of silicon devices, $^{1}$ has been developed based on the understanding of atomic structure of $Si/SiO_2$ interface and interface carrier transport. The oxidation process determines the atomistic structure of the $Si/SiO_2$ interface. $^{1}$ There have been known several types of the interface structures for the $Si/SiO_2$ interface, for example, $\beta$-cristobalite, $\alpha$-quartz, and tridymite structures. It has been known that $\alpha$-quartz structure is stable energetically, while several experimental studies suggest the importance of $\beta$-cristobalite structure. $^{1,3,4}$ In any case, layer-by-layer oxidation with the introduction of oxygen atoms among the Si-Si bonds at the early stage of oxidation has been found to be the key oxidation process, according to detailed studies. $^{1,2}$ Therefore, much knowledge on the atomistic properties of the $Si/SiO_2$ interface has been obtained.

Regarding carrier transport under the $Si/SiO_2$ interface, many studies have been performed theoretically $^{5,6}$ and experimentally. $^{7,8}$ According to these studies, the mechanism that limits the carrier transport under the $Si/SiO_2$ interface has been clarified. That is, substrate impurity scattering, bulk phonon scattering, and surface roughness scattering are the main scattering components that limits the carrier transport under the $Si/SiO_2$ interface. Such classification of the scattering components has been greatly succeeded for the quantitative understanding of the carrier transport properties. However, the phenomenological surface-roughness scattering model which describes the geometrical interface roughness $^{5,6}$ has been introduced for the quantitative understanding. Since the appropriate choice of the parameters related to the interface roughness enables reproduction of the experimental mobility in MOSFETs, the conventional carrier transport modeling cannot fully clarify the relation between the atomistic structure of the $Si/SiO_2$ interface and the carrier transport properties under the $Si/SiO_2$ interface.

Recently, several studies have been carried out which aim to understand the interface carrier transport in view of the atomistic structure of the interface. Reference 9 has reported a study on the understanding of the surface-roughness-limited carrier transport based on the atomistic interface roughness. Recent studies have also afforded an insight into the atomistic structure of the interface states based on first-principles calculations and shown the impact of the interface states on the interface carrier transport. $^{10,11}$ According to these studies, it has been found that interface defects, such as the interface states, form dipole by the charge transfer between the defects and the surrounding atoms, and the dipoles formed by the polarized interface states become the origin of both the elastic and inelastic scattering. These facts indicate that the interface carrier transport is closely related with the atomic structure of the $Si/SiO_2$ interface. However, little is known about such relations.

One possible clue in investigating such relations is the fact that the dipoles due to the polarized Si and oxygen atoms are formed in the $SiO_2$ gate oxides owing to the charge transfer that occurs because of the difference in electronegativity between Si atom and oxygen atom. $^{12}$ Actually, the dipoles formed by the charge transfer between Si atoms and $SiO_2$ layers have been known to lead to the flatband voltage shift in MOSFETs. $^{13,14}$ These facts suggest the importance of the polarized Si-O dipole for understanding the interface carrier transport. $^{15}$ The carrier transport properties under the influence of the dipole scattering have been extensively studied for the case of III-V nitrides. $^{16,17}$ For the case

$^{a)}$Electronic mail: takamitsu.ishihara@toshiba.co.jp

of the carrier transport in the inversion layer of MOSFETs, carrier transport properties have been understood normally in terms of bulk phonon scattering, surface roughness scattering, and Coulomb scattering, $^{7,8}$ and the influence of the interface dipole due to the polarized Si-O on the interface carrier transport has not been fully understood yet. Since the concentration of the interface Si-O dipoles is quite large $(\simeq 10^{14} cm^{-2}),^{14}$ the role of the interface Si-O dipole should be clarified for the correct understanding of the interface carrier transport, and also for establishing the guidelines of future interface engineering. In this paper, we report an extensive study on the relation between the atomic structure of the $Si / SiO_{2}$ interface and the interface carrier transport, taking the carrier transport in MOSFETs as an example.

The remainder of this paper is organized as follows. In Sec. II, formulation for the dipole scattering due to the interface Si-O dipole, including the contribution from the inelastic scattering component, is explained. The scattering models for bulk phonon scattering and surface roughness scattering are presented in Appendix. The expression of the mobility based on the relaxation-time approximation is given in Sec. III. The calculation methods of the mobility and the atomic structure of the $Si / SiO_{2}$ interface are explained in Sec. III. In Sec. IV, the calculated results for $\mu_{dipole}$ based on our formulation are presented and, the calculated results are compared with the experimental universal curve. Finally, conclusions are drawn in Sec. V.

## II. FORMULATION OF DIPOLE SCATTERING

Since the polarized Si-O bond at the interface is the origin of the interface dipole and causes the dipole scattering, the dipole scattering due to the interface Si-O dipole is formulated below. The formulation is carried out by including the contributions from both the elastic scattering and the inelastic scattering. In the formulation, the random distribution and orientation of dipoles are assumed in evaluating the dipole scattering rate. When performing the mobility calculation of the dipole scattering, the effective charge and the vibrational energy of the Si-O dipole are necessary. We have evaluated these quantities by performing first principles calculations for the two typical atomic configurations of the $Si / SiO_{2}$ interface: $\beta$-cristobalite and tridymite structures. On the details of first principles calculation, the explanations are given in Sec. III.

### A. Formulation of elastic dipole scattering

First, we formulate the elastic dipole scattering model. We denote the position of the $i$-th $Si$ atom as $R_{Si}=(R_{i}, R_{z})$, and the position of the $O$ atom as $R_{O}=(R_{i}+r_{a}, R_{Z}+z_{a})$, where $(r_{a}, z_{a})$ is the displacement vector between the Si and the O atoms, as shown in Fig. 1. We simplify the Si-O dipole configuration in Fig. 2 as the random and two-dimensional dipole distribution as is also shown in Fig. 1. Then, the discrete distribution of the Si-O dipoles is expressed as
$$
\begin{aligned}
\rho_{\text {ext,dipole }}(\mathbf{r}, z)= & \sum_{j}\left(\delta\left(\mathbf{r}-\mathbf{R}_{j}\right) \delta\left(z-R_{z}\right)\right. \\
& \left.-\delta\left(\mathbf{r}-\mathbf{R}_{j}-\mathbf{r}_{a}\right) \delta\left(z-R_{z}-z_{a}\right)\right), \quad(1)
\end{aligned}
$$

![](./images/813205441000505344_3.jpg)

FIG. 1. Schematic diagram that shows the coordinate system representing the dipole configuration.

where we have assumed the average charge distribution of the dipoles, for simplicity. We have also assumed that the effective charge of the Si atom is equal to that of the oxygen atom. The difficulty in formulating the dipole scattering model comes from the fact that the discrete distribution of the dipoles is embedded in the background of the depth-dependent electrostatic potential caused by the application of the gate voltage. Since the latter potential component is not responsible for the dipole scattering, the dipole scattering potential component needs to be extracted from the net potential distribution. $^{18}$ The extraction is carried out in Appendix A and we show here only the results, where the relaxation time of the elastic dipole scattering is expressed as
$$
\begin{aligned}
A(\mathbf{q}, z)= & e \int d z^{\prime} \rho_{\text {ext,dis }}\left(\mathbf{q}, z^{\prime}\right) G_{q}\left(z, z^{\prime}\right) \\
& +2 \epsilon_{s i} \sum_{i, k} s_{i}^{k} A_{i}^{k}(\mathbf{q}) \int d z^{\prime} G_{q}\left(z, z^{\prime}\right) g_{i}^{k}\left(z^{\prime}\right),
\end{aligned}\qquad(2)
$$
where
$$
A_{i}^{k}(\mathbf{q})=\int d z A(\mathbf{q}, z) g_{i}^{k}(z).\qquad(3)
$$

Multiplying both sides of Eq. (2) by $g_{j}^{l}(z)$ and integrating over z, we obtain
$$
\begin{aligned}
A_{j}^{l}(\mathbf{q})=e^{*} \int d z^{\prime} \rho_{\text {ext,dis }}\left(\mathbf{q}, z^{\prime}\right) G_{j}^{l}\left(q, z^{\prime}\right)+2 \epsilon_{s i} \sum_{i, k} s_{i}^{k} A_{i}^{k}(\mathbf{q}) G_{j i}^{l k}(q), \\
(4)
\end{aligned}
$$
where
$$
G_{j}^{l}\left(\mathbf{q}, z^{\prime}\right)=\int d z G_{q}\left(z, z^{\prime}\right) g_{j}^{l}\left(z^{\prime}\right),\qquad(5)
$$

![](./images/813205441000505344_4.jpg)

FIG. 2. $\beta$-cristobalite structure for (110) cross-section of $SiO_{2} / Si$ (100) interface. Vibrational mode and energy of the interface Si-O dipole are shown.

$$
G_{j i}^{l k}(q)=\int d z g_{j}^{l}\left(z^{\prime}\right) \int d z^{\prime} g_{i}^{k}\left(z^{\prime}\right) G_{q}\left(z, z^{\prime}\right),\qquad(6)
$$

$$
\rho_{\mathrm{ext}, \mathrm{dis}}(\mathbf{q}, z)=\sigma(\mathbf{q})\left(\delta\left(z-R_{z}\right)-e^{i \mathbf{q} \cdot \mathbf{r}_{a}} \delta\left(z-R_{z}-z_{a}\right)\right),\quad(7)
$$

$$
\sigma(\mathbf{q})=\sum_{i}\left(e^{i \mathbf{q} \cdot \mathbf{R}_{i}}-N_{\text {dipole }}\right).\qquad(8)
$$

$A_{j}^{l}(\mathbf{q})$ can be further expressed as
$$
A_{j}^{l}(\mathbf{q})=\left.A_{j}^{l}(\mathbf{q})\right|_{\mathrm{Si}}-\left.A_{j}^{l}(\mathbf{q})\right|_{\mathrm{O}},\qquad(9)
$$
where $\left.A_{i}^{l}(q)\right|_{\mathrm{Si}}$ and $\left.A_{i}^{l}(q)\right|_{\mathrm{O}}$ are the contributions of the Coulomb potential from the Si atom and the O atom, respectively. $\left.A_{j}^{l}(q)\right|_{\mathrm{Si}}$ is given by the following Poisson's equation:
$$
\begin{aligned}
\left.A_{j}^{l}(\mathbf{q})\right|_{\mathrm{Si}}= & e^{*} \int d z^{\prime} \rho_{\mathrm{ext}, \mathrm{Si}}\left(\mathbf{q}, z^{\prime}\right) G_{j}^{l}\left(q, z^{\prime}\right) \\
& +2 \epsilon_{s i} \sum_{i, k}\left.s_{i}^{k} A_{i}^{k}(\mathbf{q})\right|_{\mathrm{Si}} G_{j i}^{l k}(q),
\end{aligned}\qquad(10)
$$

$$
\rho_{\mathrm{ext}, \mathrm{Si}}(\mathbf{q}, z)=\sigma(\mathbf{q}) \delta\left(z-R_{z}\right).\qquad(11)
$$

Then, it is easily found that $\left.A_{i}^{k}(\mathbf{q})\right|_{\mathrm{Si}}$ is expressed as
$$
\left.A_{i}^{k}(\mathbf{q})\right|_{\mathrm{Si}}=\sigma(\mathbf{q}) A_{i}^{k}\left(q ; R_{z}\right),\qquad(12)
$$
where the dependence on the position of the Si atom is explicitly shown, and $A_{i}^{k}(\mathbf{q} ; R_{z})$ is the solution of the following Poisson equation:
$$
\begin{aligned}
A_{j}^{l}\left(\mathbf{q} ; R_{z}\right)= & e^{*} \int d z^{\prime} \delta\left(z^{\prime}-R_{z}\right) G_{j}^{l}\left(q, z^{\prime}\right) \\
& +2 \epsilon_{s i} \sum_{i, k} s_{i}^{k} A_{i}^{k}\left(\mathbf{q} ; R_{z}\right) G_{j i}^{l k}(q).
\end{aligned}\qquad(13)
$$

Similarly, $\left.A_{i}^{k}(\mathbf{q})\right|_{\mathrm{O}}$ is expressed as
$$
\left.A_{i}^{k}(\mathbf{q})\right|_{\mathrm{O}}=\sigma(\mathbf{q}) e^{i \mathbf{q} \cdot \mathbf{r}_{a}} A_{i}^{k}\left(q ; R_{z}+z_{a}\right),\qquad(14)
$$
here, $A_{i}^{k}(\mathbf{q} ; \mathrm{R}_{\mathrm{z}}+\mathrm{z}_{\mathrm{a}})$ is the solution of the following Poisson equation:
$$
\begin{aligned}
A_{j}^{l}\left(\mathbf{q} ; \mathrm{R}_{\mathrm{z}}+z_{\mathrm{a}}\right)= & e^{*} \int d z^{\prime} \delta\left(z^{\prime}-R_{z}-z_{a}\right) G_{j}^{l}\left(q, z^{\prime}\right) \\
& +2 \epsilon_{s i} \sum_{i, k} s_{i}^{k} A_{i}^{k}(\mathbf{q}) G_{j i}^{l k}(q).
\end{aligned}\qquad(15)
$$

Then, in order to calculate the momentum relaxation time, the averaging in terms of the random distribution of the dipoles, $\langle|A_{i}^{k}(q)|^{2}\rangle$ , needs to be performed, as is explained in Ref. 45. As a result of such averaging, $\langle|A_{i}^{k}(q)|^{2}\rangle$ can be expressed as
$$
\begin{aligned}
\left\langle\left|A_{i}^{k}(\mathbf{q})\right|^{2}\right\rangle= & \left|A_{i}^{k}\left(\mathbf{q} ; R_{z}\right)\right|^{2}+\left|A_{i}^{k}\left(\mathbf{q} ; R_{z}+z_{a}\right)\right|^{2} \\
& +2 \cos \left(\mathbf{q} \cdot \mathbf{r}_{a}\right) A_{i}^{k}\left(\mathbf{q} ; R_{z}\right) A_{i}^{k}\left(\mathbf{q} ; R_{z}+z_{a}\right). \quad(16)
\end{aligned}
$$

For a random distribution of dipole orientation, we average Eq. (16) in terms of the angle, $\phi$ , between $\mathbf{q}$ and $\mathbf{r}_{a} \cdot^{19}$ That is,
$$
\left\langle\left\|A_{i}^{k}(\mathbf{q})\right\|^{2}\right\rangle=\frac{\int_{0}^{2 \pi} d \phi\left\langle\left|A_{i}^{k}(\mathbf{q})\right|^{2}\right\rangle}{\int_{0}^{2 \pi} d \phi},\qquad(17)
$$

$$
\begin{aligned}
= & \left|A_{i}^{k}\left(\mathbf{q} ; R_{z}\right)\right|^{2}+\left|A_{i}^{k}\left(\mathbf{q} ; R_{z}+z_{a}\right)\right|^{2} \\
& +\frac{\int_{0}^{2 \pi} d \phi \cos \left(q\left|\mathbf{r}_{a}\right| \cos \phi\right)}{\int_{0}^{2 \pi} d \phi} \\
& \times A_{i}^{k}\left(\mathbf{q} ; R_{z}\right) A_{i}^{k}\left(\mathbf{q} ; R_{z}+z_{a}\right).
\end{aligned}\qquad(18)
$$

Then, the momentum relaxation time $\tau_{e l}^{i k}$ of the elastic dipole scattering for subband i in valley k is expressed as
$$
\frac{1}{\tau_{\mathrm{el}}^{i k}(E)}=\int_{0}^{2 \pi} \frac{1}{\tau_{\mathrm{el}}^{i k}(E, \theta)} d \theta,\qquad(19)
$$

$$
\frac{1}{\tau_{\mathrm{el}}^{i k}(E, \theta)}=\frac{m_{c}^{i k}}{2 \pi \hbar^{3}}(1-\cos (\theta))\left\langle\left\|A_{i}^{k}(\mathbf{q})\right\|^{2}\right\rangle.\qquad(20)
$$

In the above derivation, the screening effect by the free carriers in the inversion layer is treated as the second term in the r.h.s of Eq. (4). For MOSFETs with SiO₂ gate insulators, the amount of Coulomb scattering centers, such as the fixed charges and the interface states, is an order of magnitude $1 \times 10^{10} \sim 1 \times 10^{11} \mathrm{~cm}^{-2}$, and that for MOSFETs with high-k gate insulators $\sim 1 \times 10^{12} \mathrm{~cm}^{-2}$. However, the amount of the dipoles at the $\mathrm{Si} / \mathrm{SiO}_{2}$ interface is an order of the magnitude, $1 \times 10^{14} \mathrm{~cm}^{-2}$, which is much larger than the conventional cases. Apparently, a conventional linear screening model, such as the Debye or the Thomas-Fermi screening model, breaks down when the average distance between the dipoles becomes smaller than the screening length. For the case of the Si/SiO2 interface, the screened dipole potential by the free carriers in the inversion layer can become longrange over the average distance between the dipoles. This situation can easily occur for the small Ns (surface carrier concentration) region. In this situation, a consistent onecenter scattering approximation that is the basis of the conventional transport theory does not hold. In order to adopt a consistent one-center scattering approximation, screening of the dipole potential due to the other dipoles is necessary to exclude the possibility of there being a second scattering center closer to the carrier being scattered. Then, the problem is how to construct a screening model of the dipole potential by the other dipoles.

This problem was discussed by Sano $^{20,21}$ in detail when treating the Coulomb potential due to the discrete impurities in the framework of the Drift-Diffusion method to simulate the carrier transport under the discrete impurities. Sano applied the concept proposed by Conwell-Weisskopf, $^{22}$ in which the screening is mainly due to the overlap of electrostatic potentials of ionized dopants. According to Sano's discussions, such overlap of electrostatic potentials can be regarded as the screening charge, and the screening of the dipole potential due to the other dipoles is realized by introducing the cut-off parameter $r_{\text {ave }}$, which is the average

distance between the dipoles. Then, the required screening model should exhibit the following properties. When the average distance between the dipoles becomes larger than the screening length due to the free carriers, it should result in a conventional linear screening model, such as the Debye or the Thomas-Fermi screening model. When the average distance between the dipoles becomes smaller than the screening length due to the free carriers, the screening is realized by the overlap of electrostatic potentials in the range of the average distance between the dipoles. Based on these considerations, we use the following screening model proposed by Morgan:23

$$
\frac{1}{\lambda^{2}}=\frac{1}{\lambda_{s}^{2}}+\frac{1}{r_{\text {ave }}^{2}},
\tag{21}
$$

where $\lambda_{s}$ is the screening length due to the free carriers in the inversion layer. At the strong inversion condition, $\lambda_{s}$ becomes smaller than $r_{\text {ave }}$ and $\lambda \simeq \lambda_{s}$. On the other hand, at the weak inversion condition $\lambda_{s}$ becomes larger than $r_{\text {ave }}$ and $\lambda \simeq r_{\text {ave }}$. Thus, the screening model, Eq. (21), enables to adopt a consistent one-center scattering approximation for the case when the average distance between the dipoles becomes smaller than the screening length due to the free carriers.

### B. Formulation of inelastic dipole scattering

Next, we formulate the inelastic dipole scattering associated with the vibration of the dipole. We denote the positions of the atoms forming the Si-O dipole as shown in Fig. 3. The middle point of the dipole is expressed as $\mathbf{R}_{i, m}=\left(\mathbf{R}_{i}, z_{i}\right)$, and the positions of the Si and the O atoms with respect to the middle point are expressed as $\mathbf{R}_{\mathrm{Si}}=\left(\mathbf{R}, \mathrm{R}_{z}\right)$ and $\mathbf{R}_{\mathrm{O}}=\left(\mathbf{R}^{\prime}, \mathrm{R}_{z}^{\prime}\right)$, respectively. Generally, each atom forming the dipole can vibrate around its equilibrium position. We assume there are no correlations in the vibration between the Si and the oxygen atoms, and we express the displacement vectors of the Si and the oxygen atoms as $\mathbf{u}_{\mathrm{Si}}=\left(\mathbf{u}, \mathrm{u}_{z}\right)$ and $\mathbf{u}_{\mathrm{O}}=\left(\mathbf{u}, \mathrm{u}_{z}\right)$, respectively. Then, Coulomb potential at the point $\mathbf{r}_{p}=(\mathbf{r}, z)$ associated with the vibrated Si-O dipole can be expressed as

$$
\begin{aligned}
V_{\text {Coulomb }}= & V_{\mathrm{O}}\left(\mathbf{r}_{p}-\mathbf{R}_{\mathrm{O}}-\mathbf{R}_{i, m}-\mathbf{u}_{\mathrm{O}}\right) \\
& +V_{\mathrm{Si}}\left(\mathbf{r}_{p}-\mathbf{R}_{\mathrm{Si}}-\mathbf{R}_{i, m}-\mathbf{u}_{\mathrm{Si}}\right),
\end{aligned}
\tag{22}
$$

where $V_{\mathrm{O}}$ and $V_{\mathrm{Si}}$ are the Coulomb potentials associated with the oxygen and the Si atoms, respectively. The second term in the r.h.s of Eq. (22) can be expanded in terms of the small deviations $\mathbf{u}_{\mathrm{Si}}$ and $\mathbf{u}_{\mathrm{O}}$ as

$$
\begin{aligned}
V_{\text {Coulomb }} \simeq & V_{\mathrm{O}}\left(\mathbf{r}-\mathbf{R}_{\mathrm{O}}-\mathbf{R}_{i, m}\right)+V_{\mathrm{Si}}\left(\mathbf{r}-\mathbf{R}_{\mathrm{Si}}-\mathbf{R}_{i, m}\right) \\
& -\mathbf{u}_{\mathrm{Si}} \cdot \nabla_{\mathbf{r}_{p}} V_{\mathrm{Si}}\left(\mathbf{r}_{p}-\mathbf{R}_{\mathrm{Si}}-\mathbf{R}_{i, m}\right) \\
& +\mathbf{u}_{\mathrm{O}} \cdot \nabla_{\mathbf{r}_{p}} V_{\mathrm{O}}\left(\mathbf{r}_{p}-\mathbf{R}_{\mathrm{O}}-\mathbf{R}_{i, m}\right).
\end{aligned}
\tag{23}
$$

![](./images/813205441000505344_5.jpg)

FIG. 3. Schematic diagram that shows the dipole position.

The first and the second terms in Eq. (23) lead to the elastic dipole scattering, and the third and the fourth terms in the r.h.s of Eq. (23) lead to the inelastic dipole scattering.

Then, the Coulomb potentials associated with the vibration of the Si and the oxygen atoms are given as

$$
\begin{array}{r}
\delta V\left(\mathbf{r}-\mathbf{R}_{\mathrm{Si}}-\mathbf{R}_{i, m}\right) \simeq \mathbf{u}_{\mathrm{Si}}(\mathbf{R}) \cdot \nabla_{\mathbf{r}} V_{\mathrm{Si}}\left(\mathbf{r}_{p}-\mathbf{R}_{\mathrm{Si}}-\mathbf{R}_{i, m}\right), \\
(24)
\end{array}
$$

$$
\delta V\left(\mathbf{r}-\mathbf{R}_{\mathrm{O}}-\mathbf{R}_{i, m}\right) \simeq \mathbf{u}_{\mathrm{O}}(\mathbf{R}) \cdot \nabla_{\mathbf{r}} V_{\mathrm{O}}\left(\mathbf{r}_{p}-\mathbf{R}_{\mathrm{O}}-\mathbf{R}_{i, m}\right).
\tag{25}
$$

The total potential energy associated with the vibration of the Si-O dipole is evaluated as $^{22}$

$$
\begin{aligned}
\delta \tilde{V}_{\mathrm{Si}}\left(\mathbf{r}-\mathbf{R}_{\mathrm{Si}}-\mathbf{R}_{i, m}\right)= & \frac{1}{S} \cdot \int d \mathbf{R} \mathbf{u}_{\mathrm{Si}}(\mathbf{R}) \\
& \times \nabla_{\mathbf{r}_{p}} V_{\mathrm{Si}}\left(\mathbf{r}_{p}-\mathbf{R}_{\mathrm{Si}}-\mathbf{R}_{i, m}\right), \quad(26)
\end{aligned}
$$

$$
\begin{aligned}
\delta \tilde{V}_{\mathrm{O}}\left(\mathbf{r}-\mathbf{R}_{\mathrm{O}}-\mathbf{R}_{i, m}\right)= & \frac{1}{S} \cdot \int d \mathbf{R} \mathbf{u}_{\mathrm{O}}(\mathbf{R}) \\
& \times \nabla_{\mathbf{r}_{p}} V_{\mathrm{O}}\left(\mathbf{r}_{p}-\mathbf{R}_{\mathrm{O}}-\mathbf{R}_{i, m}\right), \quad(27)
\end{aligned}
$$

by averaging the positions along the vibrational directions of the Si and the oxygen atoms, where $S$ is the area of the unit cell. When we express the wave function in the subband $\mathrm{n}$ as $|\mathbf{k}, n\rangle$, where $\mathbf{k}$ is the two-dimensional wave vector, $|\mathbf{k}, n\rangle$ stands for $\exp (i \mathbf{k} \cdot \mathbf{r}) \cdot \zeta_{n}(z)$ and the scattering matrix element is expressed as

$$
\begin{aligned}
\left\langle\mathbf{k}^{\prime}, m\left|\delta \tilde{V}_{\mathrm{Si}}\right| \mathbf{k}, n\right\rangle= & \frac{1}{S} \cdot i\left(\mathbf{k}^{\prime}-\mathbf{k}\right) \int d \mathbf{R} \mathbf{u}_{\mathrm{Si}}(\mathbf{R}) e^{i\left(\mathbf{k}^{\prime}-\mathbf{k}\right) \cdot\left(\mathbf{R}+\mathbf{R}_{i}\right)} \\
& \times \int d z \zeta_{n}(z) \zeta_{m}(z) A\left(\mathbf{k}^{\prime}-\mathbf{k} ; z-\left(R_{z}+z_{i}\right)\right),
\end{aligned}
\tag{28}
$$

$$
\begin{aligned}
\left\langle\mathbf{k}^{\prime}, m\left|\delta \tilde{V}_{\mathrm{O}}\right| \mathbf{k}, n\right\rangle= & \frac{1}{S} \cdot i\left(\mathbf{k}^{\prime}-\mathbf{k}\right) \int d \mathbf{R} \mathbf{u}_{\mathrm{O}}(\mathbf{R}) e^{i\left(\mathbf{k}^{\prime}-\mathbf{k}\right) \cdot\left(\mathbf{R}+\mathbf{R}_{i}+\mathbf{r}_{a}\right)} \\
& \times \int d z \zeta_{n}(z) \zeta_{m}(z) A\left(\mathbf{k}^{\prime}-\mathbf{k} ; z-\left(R_{z}+z_{i}+z_{a}\right)\right),
\end{aligned}
\tag{29}
$$

where

$$
A\left(\mathbf{k}^{\prime}-\mathbf{k} ; z-\left(R_{z}+z_{i}\right)\right)=\int d \mathbf{r} e^{i\left(\mathbf{k}^{\prime}-\mathbf{k}\right) \cdot \mathbf{r}} V\left(\mathbf{r}, z-\left(R_{z}+z_{i}\right)\right).
\tag{30}
$$

Here, we assume that the Si and the oxygen atoms are equally polarized and we express $V=V_{\mathrm{Si}}=V_{\mathrm{O}}$. Since the interface Si-O dipole locates just at the interface, $A\left(\mathbf{k}^{\prime}-\mathbf{k} ; z-\left(R_{z}+z_{i}\right)\right)$ can be explicitly given as

$$
\begin{aligned}
& A\left(\mathbf{k}^{\prime}-\mathbf{k} ; z-\left(R_{z}+z_{i}\right)\right) \\
& \quad=\frac{e e^{*}}{2 \epsilon_{\mathrm{Si}}\left|\mathbf{k}^{\prime}-\mathbf{k}\right|}\left\{e^{-\left|\mathbf{k}^{\prime}-\mathbf{k}\right|\left|z-R_{z}-z_{i}\right|}+b_{\mathbf{k}^{\prime}-\mathbf{k}} e^{-\left|\mathbf{k}^{\prime}-\mathbf{k}\right|\left|z+R_{z}+z_{i}\right|}\right\}, \\
& \quad(31)
\end{aligned}
$$

where the expression of $b_{\mathbf{q}}$ is given in, for example, Refs. 18, 47, and 48. The displacement vectors $\mathbf{u}_{\mathrm{Si}}(\mathbf{R})$ and $\mathbf{u}_{\mathrm{O}}(\mathbf{R})$ can be expressed in terms of plane waves as

$$
\mathbf{u}_{\mathrm{Si}}(\mathbf{R})=\sum_{\mathbf{q}}\left\{a_{\mathrm{Si}, \mathbf{q}} \mathbf{e}_{\mathbf{q}} e^{i \mathbf{q} \cdot \mathbf{R}}+c . c .\right\}, \quad(32)
$$

$$
\mathbf{u}_{\mathrm{O}}(\mathbf{R})=\sum_{\mathbf{q}}\left\{a_{\mathrm{O}, \mathbf{q}} \mathbf{e}_{\mathbf{q}} e^{i \mathbf{q} \cdot \mathbf{R}}+c . c .\right\}, \quad(33)
$$

where $a_{\mathrm{Si}, \mathbf{q}}$ and $a_{\mathrm{O}, \mathbf{q}}$ are normal coordinates of the $\mathrm{Si}$ and the oxygen atoms, $\mathbf{e}_{\mathbf{q}}$ is a unit polarization vector, and $\mathbf{q}$ is the two-dimensional wavevector. Substituting Eqs. (32) and (33) in Eqs. (28) and (29), the scattering matrix element for the transition from the subband $\mathrm{n}$ to the subband $\mathrm{m}$ can be expressed as

$$
\begin{aligned}
\left\langle\mathbf{k}^{\prime}, m\left|\delta \tilde{V}_{\mathrm{Si}}\right| \mathbf{k}, n\right\rangle= & i a_{\mathrm{Si}, \mathbf{q}}\left(\mathbf{k}^{\prime}-\mathbf{k}\right) \\
& \times \mathbf{e}_{\mathbf{q}} e^{i\left(\mathbf{k}^{\prime}-\mathbf{k}\right) \cdot \mathbf{R}_{i}} A_{n m}\left(\mathbf{k}^{\prime}-\mathbf{k} ; R_{z}+z_{i}\right), \quad(34)
\end{aligned}
$$

$$
\begin{aligned}
\left\langle\mathbf{k}^{\prime}, m\left|\delta \tilde{V}_{\mathrm{O}}\right| \mathbf{k}, n\right\rangle= & i a_{\mathrm{O}, \mathbf{q}}\left(\mathbf{k}^{\prime}-\mathbf{k}\right) \\
& \times \mathbf{e}_{\mathbf{q}} e^{i\left(\mathbf{k}^{\prime}-\mathbf{k}\right) \cdot \mathbf{R}_{i}} A_{n m}\left(\mathbf{k}^{\prime}-\mathbf{k} ; R_{z}+z_{i}\right), \quad(35)
\end{aligned}
$$

where

$$
\begin{aligned}
A_{n m}\left(\mathbf{k}^{\prime}-\mathbf{k} ; R_{z}+z_{i}\right)= & \int d z \zeta_{n}(z) \zeta_{m}(z) A\left(\mathbf{k}^{\prime}-\mathbf{k} ; z\right. \\
& \left.-\left(R_{z}+z_{i}\right)\right). \quad(36)
\end{aligned}
$$

In calculating the scattering rate, the evaluation of $\left\langle\left|\sum_{i}\left\langle n_{\mathbf{k}^{\prime}-\mathbf{k}} \mp 1 ; \mathbf{k}^{\prime}, m\left|\delta \tilde{V}_{\mathrm{Si}}\right| \mathbf{k}, n ; n_{\mathbf{k}^{\prime}-\mathbf{k}}\right\rangle\right|^{2}\right\rangle$ is necessary. Here, $\langle\langle\cdots\rangle\rangle$ means the average in terms of the random distribution of the dipoles, and $\left|\mathbf{k}, n ; n_{\mathbf{k}^{\prime}-\mathbf{k}}\right\rangle=|\mathbf{k}, n\rangle \otimes\left|n_{\mathbf{k}^{\prime}-\mathbf{k}}\right\rangle$ where $n_{\mathbf{k}^{\prime}-\mathbf{k}}$ is the occupation number and $\left|n_{\mathbf{k}^{\prime}-\mathbf{k}}\right\rangle$ is the harmonic oscillator wave-function for phonons. Then,

$$
\left\langle n_{\mathbf{k}^{\prime}-\mathbf{k}}-1\left|a_{\mid \mathrm{A}, \mathbf{k}^{\prime}-\mathbf{k}}\right| n_{\mathbf{k}^{\prime}-\mathbf{k}}\right\rangle=\sqrt{\frac{\hbar}{2 M_{\mathrm{red}} \omega_{\mathrm{A}}}} n_{\mathbf{k}^{\prime}-\mathbf{k}}, \quad(37)
$$

$$
\left\langle n_{\mathbf{k}^{\prime}-\mathbf{k}}+1\left|a_{\mathrm{A}, \mathbf{k}^{\prime}-\mathbf{k}}^{\dagger}\right| n_{\mathbf{k}^{\prime}-\mathbf{k}}\right\rangle=\sqrt{\frac{\hbar}{2 M_{\mathrm{red}} \omega_{\mathrm{A}}}}\left(n_{\mathbf{k}^{\prime}-\mathbf{k}}+1\right), \quad(38)
$$

for phonon absorption and emission, respectively, and $\mathrm{A}=\mathrm{Si}$ or $\mathrm{A}=\mathrm{O}$. Here, $M_{\text {red }}$ is the reduced mass of the Si-O dipole defined by

$$
\frac{1}{M_{\mathrm{red}}}=\frac{1}{M_{\mathrm{Si}}}+\frac{1}{M_{\mathrm{O}}}, \quad(39)
$$

where $M_{\mathrm{Si}}$ and $M_{\mathrm{O}}$ are the masses, and $\hbar \omega_{\mathrm{Si}}$ and $\hbar \omega_{\mathrm{O}}$ are the vibrational energies of the $\mathrm{Si}$ and the oxygen atoms of the Si-O dipole. According to the manner of Ref. 45, the scattering matrix element, $\left\langle\left|\sum_{i}\left\langle n_{\mathbf{k}^{\prime}-\mathbf{k}} ; \mathbf{k}^{\prime}, m\left|\delta \tilde{V}_{\mathrm{Si}, \mathrm{O}}\right| \mathbf{k}, n ; n_{\mathbf{k}^{\prime}-\mathbf{k}}\right\rangle\right|^{2}\right\rangle$, can be evaluated for phonon absorption and emission as

$$
\begin{aligned}
\left\langle\left\langle\mid \sum_{i}\right.\right. & \left.\left.\left\langle\mathbf{k}^{\prime}, m\left|\delta \tilde{V}_{\mathrm{Si}}\right| \mathbf{k}, n\right\rangle\right|^{2}\right\rangle_{\mathrm{ab}} \\
= & \frac{m_{c} N_{\text {dipole }}}{8 M_{\mathrm{red}} \hbar \omega_{\mathrm{Si}}} \cdot\left(\frac{e e^{*}}{\epsilon_{\mathrm{Si}}}\right)^{2} \cdot n_{\mathbf{k}^{\prime}-\mathbf{k}} \\
& \times|| \mathbf{k}^{\prime}-\mathbf{k}\left|A_{n m}\left(\mathbf{k}^{\prime}-\mathbf{k} ; R_{z}+z_{i}\right)\right|^{2}, \quad(40)
\end{aligned}
$$

$$
\begin{aligned}
\left\langle\left\langle\mid \sum_{i}\right.\right. & \left.\left.\left\langle\mathbf{k}^{\prime}, m\left|\delta \tilde{V}_{\mathrm{Si}}\right| \mathbf{k}, n\right\rangle\right|^{2}\right\rangle_{\mathrm{emi}} \\
= & \frac{m_{c} N_{\text {dipole }}}{8 M_{\text {red }} \hbar \omega_{\mathrm{Si}}} \cdot\left(\frac{e e^{*}}{\epsilon_{\mathrm{Si}}}\right)^{2} \cdot\left(n_{\mathbf{k}^{\prime}-\mathbf{k}}+1\right) \\
& \times|| \mathbf{k}^{\prime}-\mathbf{k}\left|A_{n m}\left(\mathbf{k}^{\prime}-\mathbf{k} ; R_{z}+z_{i}\right)\right|^{2}, \quad(41)
\end{aligned}
$$

for the $\mathrm{Si}$ atom, and

$$
\begin{aligned}
\left\langle\left\langle\mid \sum_{i}\right.\right. & \left.\left.\left\langle\mathbf{k}^{\prime}, m\left|\delta \tilde{V}_{\mathrm{O}}\right| \mathbf{k}, n\right\rangle\right|^{2}\right\rangle_{\mathrm{ab}} \\
= & \frac{m_{c} N_{\text {dipole }}}{8 M_{\text {red }} \hbar \omega_{\mathrm{Si}}} \cdot\left(\frac{e e^{*}}{\epsilon_{\mathrm{Si}}}\right)^{2} \cdot n_{\mathbf{k}^{\prime}-\mathbf{k}} \\
& \times|| \mathbf{k}^{\prime}-\mathbf{k}\left|A_{n m}\left(\mathbf{k}^{\prime}-\mathbf{k} ; R_{z}+z_{i}+z_{a}\right)\right|^{2}, \quad(42)
\end{aligned}
$$

$$
\begin{aligned}
\left\langle\left\langle\mid \sum_{i}\right.\right. & \left.\left.\left\langle\mathbf{k}^{\prime}, m\left|\delta \tilde{V}_{\mathrm{O}}\right| \mathbf{k}, n\right\rangle\right|^{2}\right\rangle_{\mathrm{emi}} \\
= & \frac{m_{c} N_{\text {dipole }}}{8 M_{\text {red }} \hbar \omega_{\mathrm{Si}}} \cdot\left(\frac{e e^{*}}{\epsilon_{\mathrm{Si}}}\right)^{2} \cdot\left(n_{\mathbf{k}^{\prime}-\mathbf{k}}+1\right) \\
& \times|| \mathbf{k}^{\prime}-\mathbf{k}\left|A_{n m}\left(\mathbf{k}^{\prime}-\mathbf{k} ; R_{z}+z_{i}+z_{a}\right)\right|^{2} .
\end{aligned}
$$

Here, $e^{*}$ is the effective charge of the Si atom, where we have assumed that the $\mathrm{Si}$ and the oxygen atoms are equally polarized.

In the above formulation, we assume that the $\mathrm{Si}$ and the oxygen atoms oscillate with no correlation between them. For the case where the $\mathrm{Si}$ and the oxygen atoms oscillate in-phase or inopposite phase, the scattering matrix element can be expressed as

$$
\begin{aligned}
\left\langle\left\langle\left|\sum_{i}\left\langle\mathbf{k}^{\prime}, m\left|\delta \tilde{V}_{\text {phase }}\right| \mathbf{k}, n\right\rangle\right|^{2}\right\rangle\right\rangle_{\mathrm{ab}}= & \frac{m_{c} N_{\text {dipole }}}{8 M_{\text {red }} \hbar \omega_{\mathrm{Si}}} \cdot\left(\frac{e e^{*}}{\epsilon_{\mathrm{Si}}}\right)^{2} \cdot n_{\mathbf{k}^{\prime}-\mathbf{k}}\left|\mathbf{k}^{\prime}-\mathbf{k}\right|^{2} \\
& \times\left\langle\left\langle\left|A_{n m}\left(\mathbf{k}^{\prime}-\mathbf{k} ; R_{z}+z_{i}\right) \pm e^{i\left(\mathbf{k}^{\prime}-\mathbf{k}\right) \cdot \mathbf{r}_{a}} A_{n m}\left(\mathbf{k}^{\prime}-\mathbf{k} ; R_{z}+z_{i}+z_{a}\right)\right|^{2}\right\rangle,\right.
\end{aligned}
$$

$$
\begin{aligned}
\left\langle\left\langle\left|\sum_{i}\left\langle\mathbf{k}^{\prime}, m\left|\delta \tilde{V}_{\text {phase }}\right| \mathbf{k}, n\right\rangle\right|^{2}\right\rangle\right\rangle_{\mathrm{emi}}= & \frac{m_{c} N_{\text {dipole }}}{8 M_{\text {red }} \hbar \omega_{\mathrm{Si}}} \cdot\left(\frac{e e^{*}}{\epsilon_{\mathrm{Si}}}\right)^{2} \cdot\left(n_{\mathbf{k}^{\prime}-\mathbf{k}}+1\right)\left|\mathbf{k}^{\prime}-\mathbf{k}\right|^{2} \\
& \times\left\langle\left\langle\left|A_{n m}\left(\mathbf{k}^{\prime}-\mathbf{k} ; R_{z}+z_{i}\right) \pm e^{i\left(\mathbf{k}^{\prime}-\mathbf{k}\right) \cdot \mathbf{r}_{a}} A_{n m}\left(\mathbf{k}^{\prime}-\mathbf{k} ; R_{z}+z_{i}+z_{a}\right)\right|^{2}\right\rangle\right\rangle .
\end{aligned}
$$
(45)

Here, $\pm$ stands for in-phase and opposite-phase oscillation, respectively. The averaging in terms of the angle, $\phi$, between $\mathbf{q} = \mathbf{k}' - \mathbf{k}$ and $\mathbf{r}_a$, is carried out as Eq. (18)
$$
\begin{aligned}
& \left\langle\left|A_{n m}\left(\mathbf{q} ; R_{z}+z_{i}\right) \pm e^{i(\mathbf{q}) \cdot \mathbf{r}_{a}} A_{n m}\left(\mathbf{q} ; R_{z}+z_{i}+z_{a}\right)\right|^{2}\right\rangle \\
& \quad=\left|A_{i}^{k}\left(\mathbf{q} ; R_{z}+z_{i}\right)\right|^{2}+\left|A_{i}^{k}\left(\mathbf{q} ; R_{z}+z_{i}+z_{a}\right)\right|^{2} \\
& \quad \pm \frac{\int_{0}^{2 \pi} d \phi \cos \left(q\left|\mathbf{r}_{a}\right| \cos \phi\right)}{\int_{0}^{2 \pi} d \phi} A_{i}^{k}\left(\mathbf{q} ; R_{z}+z_{i}\right) A_{i}^{k}\left(\mathbf{q} ; R_{z}+z_{i}+z_{a}\right).
\end{aligned}
$$

Finally, the scattering rate of the inelastic dipole scattering associated with the vibration of the Si atom from the subband n to the subband m is expressed as
$$
\frac{1}{\tau_{\text {inel }}^{n m}}=\frac{1}{\tau_{\mathrm{ab}}^{n m}}+\frac{1}{\tau_{\mathrm{emi}}^{n m}},\qquad(47)
$$

$$
\begin{aligned}
\frac{1}{\tau_{\mathrm{ab}}^{n m}}= & \frac{1}{(2 \pi)^{2}} \cdot \frac{2 \pi}{\hbar} \int d \mathbf{k}^{\prime}\left\langle\left|\sum_{i}\left\langle\mathbf{k}^{\prime}, m|\delta \tilde{V}| \mathbf{k}, n\right\rangle\right|^{2}\right\rangle_{\mathrm{ab}} \\
& \times \delta\left(\epsilon_{\mathbf{k}^{\prime}}+\epsilon_{m}-\epsilon_{\mathbf{k}}-\epsilon_{n}-\hbar \omega_{\mathrm{Si}}\right),
\end{aligned}\qquad(48)
$$

$$
\begin{aligned}
\frac{1}{\tau_{\mathrm{emi}}^{n m}}= & \frac{1}{(2 \pi)^{2}} \cdot \frac{2 \pi}{\hbar} \int d \mathbf{k}^{\prime}\left\langle\left|\sum_{i}\left\langle\mathbf{k}^{\prime}, m|\delta \tilde{V}| \mathbf{k}, n\right\rangle\right|^{2}\right\rangle_{\mathrm{emi}} \\
& \times \delta\left(\epsilon_{\mathbf{k}^{\prime}}+\epsilon_{m}-\epsilon_{\mathbf{k}}-\epsilon_{n}+\hbar \omega_{\mathrm{Si}}\right),
\end{aligned}\qquad(49)
$$

where
$$
\epsilon_{\mathbf{k}}=\frac{\hbar^{2}}{2 m_{c}^{i}} k^{2},\qquad(50)
$$

is the two-dimensional kinetic energy, $\delta \tilde{V}=\delta \tilde{V}_{\mathrm{Si}}+\delta \tilde{V}_{\mathrm{O}}$ stands for the simple harmonic oscillation case, and $\delta \tilde{V}$ $=\delta \tilde{V}_{\text {phase }}$ stands for the in-phase and opposite-phase oscillation case of the Si and the oxygen atoms, respectively. As can be seen in Sec. V, our first-principles calculation has shown that only the Si atom of the dipole vibrates parallel to the interface, while the oxygen atom of the dipole is kept fixed, at the vibrational mode with the lowest vibrational energy (17 meV). Therefore, we consider only the contribution of the Si atom vibration (Eqs. (40) and (41)) to the dipole scattering rate.

It should be noted here that the strong dipole can also be formed at interface states, $^{15,24}$ and becomes the origin of the dipole scattering. However, the concentration of the interface states at the $Si / SiO_{2}$ interface is an order of the magnitude, $\sim 10^{10} \mathrm{~cm}^{-2}$, in MOSFETs with thick gate oxides $(\sim 10 \mathrm{~nm})$, and its influence on the interface carrier transport at the $\mathrm{Si} / \mathrm{SiO}_{2}$ interface can be neglected except for the case of MOSFETs with thin gate oxides $(<2 \mathrm{~nm})$.

Finally, we would like to comment on the treatment of the screening effect due to the free carriers in the inversion layer for the case of the inelastic dipole scattering. Since the inelastic scattering causes the dynamic response of the electron gas, it is necessary to treat the dynamical screening. However, the theoretical treatment of the dynamic screening is very difficult because the dynamic response of the electron gas makes the screening mechanism complicated by the plasmon excitation and its damping. In our treatment, the screening effect by the free carriers in the inversion layer is considered in the elastic dipole scattering model, but not considered in the inelastic dipole scattering model. We have neglected the screening effect on the inelastic dipole scattering because we have followed the discussion given by Fischetti $^{6}$ on the dynamic screening for the case of the acoustic phonon scattering in silicon inversion layers. Here, we briefly mention the key issues of his discussion.

The static screening becomes significant for the shortwavelength region (large wave number). This is because the long-range excitation, such as that of plasmon, decays rapidly compared with the short-range individual excitation. As a result, Coulomb interaction becomes short-range and leads to the polarization of the electron gas, which is the static screening effect. $^{6}$ This occurs at low temperature and/or high electron densities, where the electron gas becomes highly degenerate. On the other hand, the dynamic screening becomes significant for the long-wavelength region (small wave number). The long-range nature of Coulomb interaction is enhanced owing to the long-wavelength plasmon excitation and leads to the anti-screening effect $^{25,26}$ that enhances the strength of the effective Coulomb interaction. $^{6}$ This situation occurs at high temperature and/or low electron densities, where the electron gas becomes non-degenerate. For the case of the inversion layer in MOSFET at room temperature, the highly degenerate electron state only occurs at extremely large effective electric field where the electron thermal energy can be neglected. Under the effective electric field region, which is of interest from the viewpoint of device engineering, the contribution of the electron thermal energy makes it difficult to realize the highly degenerate electron states even for the high effective electric field region. Electrons are distributed in the wave number space from the small wave number region to the large wave number region, according to Fermi distribution. Therefore, both screening effects (anti-screening and static screening) coexist because the wave number region that contributes to the screening extends from the small wave number region to the large wave number region. As a result, long-wavelength anti-screening and short-wavelength screening are canceled almost completely and the situation becomes almost equivalent to what it would be without screening effects. $^{6}$ On the basis of these discussions, we have neglected the screening effect on the inelastic dipole scattering. It should be mentioned here that the static screening is considered in the case of the optical phonon scattering in the Ridley's text book. $^{22}$ However, Ridley's screening model for the optical phonon scattering is applicable only to highly degenerate electron gas and its validity is not confirmed for the case of nondegenerate electron gas. In addition, the initial state wavefunctions are orthogonal to the final state wave-functions, and the strength of the screening effect is also suppressed (Eq. (6)). Based on these considerations, our assumption where the screening effect on the inelastic dipole scattering is neglected is considered to be reasonable.

## III. MOBILITY CALCULATION SCHEME

We have constructed a general framework of mobility modeling that can properly take into account the elastic scattering and the inelastic scattering associated with the dipoles (Fig. 4). Since such dipoles vibrate with their own frequencies and become the origin of the inelastic scattering as is explained in Sec. II, vibrational mode of the dipole is evaluated accurately by the first-principles calculations. By using the vibrational mode of the dipole thus obtained, the mobility limited by the dipole scattering, $\mu_{\text{dipole}}$, is calculated based on the relaxation-time approximation. The explicit expression of $\mu_{\text{dipole}}$ is derived by summing up the contributions from each subband as follows:

$$
\mu_{\text{dipole}}=\sum_{i, k} N_{i k} \mu_{\text{dipole}}^{i k}, \quad(51)
$$

where $N_{i k}$ is the occupancy of subband i in valley k. $\mu_{\text{dipole}}^{i k}$ is the mobility contribution from subband i in valley k and is calculated from the relaxation time $\tau_{\text{dipole}}^{i k}$ that includes the contribution from both the elastic and inelastic scattering components as

$$
\mu_{\text{dipole}}^{i k}=\frac{e\left\langle\tau_{\text{dipole}}^{i k}\right\rangle}{m_{c}^{i k}}, \quad(52)
$$

where $m_{c}^{i k}$ is the conductivity mass of subband i in valley k, and the averaged relaxation time $\left\langle\tau_{\text{dipole}}^{i k}\right\rangle$ is given by

$$
\left\langle\tau_{\text{dipole}}^{i k}\right\rangle=\frac{\int_{E_{i k}}^{\infty} \tau_{\text{dipole}}^{i k}(E) \frac{\partial f_{0}}{\partial E}\left(E-E_{i k}\right) d E}{\int_{E_{i k}}^{\infty} f_{0} d E}, \quad(53)
$$

$$
\frac{1}{\tau_{\text{dipole}}^{i k}}=\frac{1}{\tau_{\mathrm{el}}^{i k}}+\frac{1}{\tau_{\text{inel}}^{i k}}, \quad(54)
$$

where $E_{i k}$ denotes the subband energy for subband i in valley k, and $f_{0}$ is the Fermi distribution function. The mobility limited by the bulk phonon scattering, $\mu_{\text{phonon}}$, and the mobility limited by the surface roughness scattering, $\mu_{\text{rough}}$, can also be obtained in the same way as described above by using the energy and the momentum relaxation times given in Appendix B. For the calculation of $\mu_{\text{phonon}}$, phonon scattering processes and their transition paths between the valleys are taken into account as shown in Figure 5. It should be noted here on the surface roughness scattering model and the acoustic phonon scattering model we used.

![](./images/813205441000505344_6.jpg)

FIG. 4. Outline of the universal mobility modeling scheme.

Regarding the acoustic phonon scattering model, we have used the isotropic model. However, anisotropic deformation potential model is more physics-based and adequate for the evaluation of the acoustic phonon scattering rate. We explain why we have used the isotropic model for the acoustic phonon scattering. From the viewpoint of the modeling, the key issues in evaluating $\mu_{\text{phonon}}$ are how to reach the bulk-Si limit for the magnitude of $\mu_{\text{phonon}}$ at low effective electric field $\left(E_{\text{eff}}\right)$ and to represent the experimental $E_{\text{eff}}$-dependence. Regarding the $E_{\text{eff}}$-dependence of $\mu_{\text{phonon}}, E_{\text{eff}}^{\frac{7}{3}}$-dependence is observed in the experiment. $^{7,8}$ However, the experimentally observed $E_{\text{eff}}^{\frac{7}{3}}$-dependence of $\mu_{\text{phonon}}$ in the inversion layer cannot be reproduced even by the anisotropic deformation potential model for the acoustic phonon scattering. $^{6,40}$ The expected $E_{\text{eff}}^{\frac{7}{3}}$-dependence of $\mu_{\text{phonon}}$ is obtained only for the high $E_{\text{eff}}$ region $\left(\mathrm{N}_{\mathrm{s}} \geq 2 \times 10^{12} \mathrm{~cm}^{-2}\right)^{6,40}$ For the low $E_{\text{eff}}$ region, the $E_{\text{eff}}$-dependence of $\mu_{\text{phonon}}$ becomes weaker than the experimental $E_{\text{eff}}^{\frac{7}{3}}$-dependence. At present, the anisotropic deformation potential model for the acoustic phonon scattering cannot fully represent the $E_{\text{eff}}^{\frac{7}{3}}$-dependence within the $E_{\text{eff}}$ region of technical interest $(0.1 \sim 1 \mathrm{MV} / \mathrm{cm})$. The differences between the theoretical calculation of the $E_{\text{eff}}$-dependence and the experimental $E_{\text{eff}}^{\frac{7}{3}}$-dependence of $\mu_{\text{phonon}}$ are clearly shown in Ref. 40. Though that paper presents only the calculated results of $\mu_{\text{phonon}}$ by the isotropic model, similar differences in the $E_{\text{eff}}$-dependence of $\mu_{\text{phonon}}$ between the anisotropic model and the experiment are observed, since the $E_{\text{eff}}$-dependence of $\mu_{\text{phonon}}$ calculated by the anisotropic model is similar to that calculated by the isotropic model. $^{6,40}$ Therefore, there are no significant differences in the $E_{\text{eff}}$-dependence of $\mu_{\text{phonon}}$ between the anisotropic and isotropic deformation potential models.

On the other hand, the anisotropic model can reach the bulk-Si limit for the magnitude of $\mu_{\text{phonon}}$ at low $E_{\text{eff}} \cdot{ }^{6}$ The well-known value $^{50}$ of the deformation potential for the isotropic acoustic phonon scattering model, 9 eV, is too small to

![](./images/813205441000505344_7.jpg)

FIG. 5. Schematic diagram of scattering processes from (a) the twofold degenerate valleys and (b) the four-fold degenerate valleys for intra-valley acoustic phonons and inter-valley phonons for electrons in an inversion layer. L and H represent the twofold and the four-fold valleys, respectively. The number in parenthesis stands for the degeneracy in each scattering process.

reproduce the experimentally obtained magnitude of $\mu_{\text{phonon}}$ when the isotropic model is used for the evaluation of the acoustic phonon scattering rate. This fact indicates that the isotropic model cannot reach the bulk-Si limit for the magnitude of $\mu_{\text{phonon}}$ at low $E_{\text{eff}}$. In order to reach the bulk-Si limit for the magnitude of $\mu_{\text{phonon}}$ at low $E_{\text{eff}}$ by the isotropic model, we have employed the idea of higher coupling with the acoustic phonons than in bulk. $^{7,8,40}$ Using the larger value of the acoustic phonon deformation potential than in bulk, the isotropic model can reach the bulk-Si limit for the magnitude of $\mu_{\text{phonon}}$ at low $E_{\text{eff}}$. According to this procedure, the isotropic model for the acoustic phonon scattering can reproduce almost the same results by the anisotropic model. Therefore, the use of the anisotropic model for the acoustic phonon scattering does not cause a change in our calculated results, and the essence of our conclusions is not altered. Since the evaluation of $\mu_{\text{dipole}}$ needs much time-consuming calculation, we have avoided the use of the anisotropic model for the acoustic phonon scattering that also needs much time-consuming calculation. Therefore, we consider that the use of the isotropic model can be justified at least at room temperature. When studying the temperature dependence, the isotropic model may cause errors, and we consider that the anisotropic model should be used.

Regarding the surface roughness scattering model, the functional form of the roughness power spectrum is a key for the evaluation of $\mu_{\text{rough}}$. However, the conventional Gaussian or exponential form of the roughness power spectrum has the limitation on predicting $\mu_{\text{rough}}$. This limitation has become clear for the case of advanced MOSFETs. As pointed out in Refs. 27 and 28, the Gaussian or exponential form of the roughness power spectrum cannot reproduce both the electron- and hole-$\mu_{\text{rough}}$ with the same $\Delta$ and $\Lambda$. There are no physical reasons that the interface geometry is different between NMOSFET and PMOSFET, since the fabrication process is identical for the two cases, and the only difference is the type of dopant impurity in the substrate. Based on this consideration, Pirovano *et al.* have proposed the form of the roughness power spectrum that enables reproduction of both the electron- and hole-$\mu_{\text{rough}}$ with the same $\Delta$ and $\Lambda$: $^{28,29}$

$$
S(q)=\pi(\Delta \Lambda)^{2} e^{-\frac{(q \Lambda)^{n}}{4}}. \tag{55}
$$

They have found that the hole-$\mu_{\text{rough}}$ is strongly affected by the form of the roughness power spectrum, namely, by the choice of n, whereas the electron-$\mu_{\text{rough}}$ is less affected. At hole Fermi energy the change in the form of $S(q)$ by changing n is significant, whereas the change in the form of $S(q)$ is small at electron Fermi energy. Focusing on this nature of S(q), they have found that n=4, Eq. (B20), is the appropriate choice. When the Gaussian or the exponential form of the roughness power spectrum is used, the different values of $\Delta$ and $\Lambda$ for NMOSFET and PMOSFET are necessary to reproduce the electron- and hole-$\mu_{\text{rough}}$. We consider that the choice of the appropriate form of the roughness power spectrum, even if it is different from the conventional Gaussian or exponential form, is physically more plausible than to change the values of $\Delta$ and $\Lambda$ for NMOSFET and PMOSFET because the fabrication process for the two is identical and the interface geometry should be the same for the two cases. This idea has also been applied for the case of MOSFETs with oxynitride gate oxide (oxide with nitrogen incorporated), and has enabled reproduction of the electron- and hole-$\mu_{\text{rough}}$ with the same $\Delta$ and $\Lambda$ by the appropriate choice of the roughness power spectrum. $^{30}$ Thus, the validity of the use of the roughness power spectrum form which is different from the conventional Gaussian or exponential form is confirmed. When the conventional Gaussian or exponential form of the roughness power spectrum is used, the change in the electron-$\mu_{\text{rough}}$ is almost negligible compared to that calculated by the roughness power spectrum, Eq. (B20). Therefore, the essence of our results does not depend on the choice of the form of the roughness power spectrum.

## IV. CALCULATION METHODS

### A. Subband structure calculation method

The 2-dimensional subband structure is obtained by solving the Poisson and Schrödinger equations self-consistently. $^{31}$ Twenty subbands are considered for each valley in the evaluation of $\mu_{\text{phonon}}$ because the contribution of higher subbands is indispensable for the quantitative evaluation of $\mu_{\text{phonon}}$. $^{49}$ For the case of $\mu_{\text{dipole}}$, 4 subbands are considered for each valley in the evaluation of $\mu_{\text{dipole}}$. The contribution of the higher subbands is necessary for the quantitative evaluation of $\mu_{\text{dipole}}$ because the multi-subband occupation significantly increases the amount of $\mu_{\text{dipole}}$ compared with $\mu_{\text{dipole}}$ evaluated under the single-subband occupation. $^{32,33,46}$ This is because the increased inversion layer width and the greater subband energies of the higher subbands reduce the dipole scattering rate. The former, in particular, has an exponential effect on $\mu_{\text{dipole}}$. The multi-subband screening due to the occupation of higher subbands also significantly weakens the strength of the dipole scattering potential. Thus, the inclusion of higher subbands is necessary for the quantitative evaluation of $\mu_{\text{dipole}}$. However, the consideration of the subbands higher than 4-subbands needs extremely time-consuming calculations for the evaluation of $\mu_{\text{dipole}}$. This is why we have considered 4-subbands in the evaluation of $\mu_{\text{dipole}}$.

### B. Calculation method for electronic structure and phonon vibrational mode

Our calculations are based on density functional theory (DFT) and the generalized gradient approximation (GGA) of PW91 in order to describe the atomic structure of the $\text{Si}/\text{SiO}_{2}$ (100) interface properly. We used the original version of the PHASE code. $^{35}$ The calculations were performed using ultrasoft pseudopotentials for silicon and oxygen atoms with 1*k* to 4*k* points for Brillouin-zone samplings. We found that the cutoff energies of 25Ry for the wave functions and 144Ry for the augmented electron densities are sufficient for conversing electronic calculations. $^{10}$ In the present study, the calculations were performed with a thick $\text{SiO}_{2}$ film region and with the $\text{Si}/\text{SiO}_{2}$(100) interface region, separately. The $\text{Si}/\text{SiO}_{2}$ (100) interface structure is prepared by inserting O atom into a Si-Si bond from the topmost surface to deeper

regions on a repeated slab modified from a $c(4 \times 2)$ surface unit cell consisting of 14 layers of Si atoms and a vacuum spacing with the same thickness. Accordingly, the oxidized layers are relaxed in order to be in equilibrium positions. Inversion symmetry with respect to the slab center located at a Si bond center is used for the interface to increase the computational efficiency.

An effective charge of valence electrons for each atom is also evaluated by summing electronic charge densities within its Wigner-Seitz cell, which can be calculated at grid points generated regularly on Cartesian coordinates. In particular, the charge density defined at each grid point belongs to the atom closest to the grid point. $^{36}$

The vibrational mode of the interface Si-O dipole is evaluated by solving the dynamical matrix of atomic force that is obtained by adding the small deviations to the atomic positions from their equilibrium positions. The vibrational mode of the Si-O dipole is evaluated by considering the vibrations of the second-nearest neighbor atoms around the focused Si-O dipole with the other atoms being kept fixed. It should be noted here that the essence of our results does not depend on how the valence charge is divided with the Wigner-Seitz cell.

## V. RESULTS

Figure 2 shows $\beta$-cristobalite structures for the (110) cross-section of the $Si/SiO_2(100)$ interface used in our first-principles calculation. The Si atom of the interface Si-O dipole has been found to vibrate parallel to the interface, whereas the oxygen atom of the Si-O dipole has been found to be almost fixed, at the vibrational mode with the lowest vibrational energy. The effective charge of the Si atom has been evaluated by the division of valence charge with the Wigner-Seitz cell, and has been found to be $-1.1e$ ($e$ is the elementary charge) for $\beta$-cristobalite and tridymite structures. This lowest vibrational energy has been evaluated to be 17 meV for $\beta$-cristobalite structure (Fig. 2) and 25 meV for tridymite structure. These are almost comparable with electron thermal energy and makes the main contribution to the inelastic dipole scattering. Since the differences in the magnitude of the lowest vibrational energy and the effective charge between $\beta$-cristobalite and tridymite structures are small, there are no significant differences in the vibrational mode between the two structures. This is because the vibrational properties of the interface Si-O dipole are determined by the strength of the interface Si-O bond. The strength of the interface Si-O bond is determined by the atomic nature of Si and oxygen atoms, and the influence of the atomic configuration is small. Therefore, the vibrational properties of the interface Si-O dipole are specific to the interface Si-O bond and do not depend on the details of the atomic configuration of the $SiO_2$ structure. For another atomic configurations of the $Si/SiO_2(100)$ interface, essentially the same results as the above would be obtained.

The difference between the above-mentioned vibrational mode and the well-known surface optical (SO) phonon mode should be noted. $^{6,37}$ The above-mentioned vibrational mode is localized at the interface, whereas the SO phonon mode extends over the entire region of the gate insulator. For the case of the SO phonon mode for $SiO_2$ gate dielectrics, the hard Si-O bonds in $SiO_2$ far from the interface yield a reduced ionic polarization. This leads to a small difference between a dielectric of static and optical permittivities, and relatively high vibrational energies (larger than 50 meV). Therefore, the influence of the SO phonons on the carrier transport under $SiO_2$ gate dielectrics is limited. On the other hand, the charge transfer to the oxygen atom located near the interface from the adjacent Si atom located at the substrate side becomes large compared with the charge transfer from the Si atom located at the gate insulator side. This is the origin of the strong Si-O dipole formation at the interface. As a result of such strong dipole formation, the vibrational energy of the dipole becomes relatively small. Thus, the Si atom vibration found in this study is indeed the localized vibrational mode that is specific to the interface, and is essentially different from the conventional SO phonon mode.

Figure 6 shows the calculated mobility limited by the interface Si-O dipole scattering, $\mu_{dipole}$. The contributions from the elastic scattering and the inelastic scattering are shown separately. The contribution from the inelastic scattering to $\mu_{dipole}$ has been evaluated by considering only the lowest vibrational energy, 17 meV, for $\beta$-cristobalite structure, because the difference of the lowest vibrational energy between $\beta$-cristobalite and tridymite structures is only 8 meV and its influence on the amount of $\mu_{dipole}$ can be negligible. In addition, since the vibrational energies of the other vibrational modes are almost all larger than 100 meV, their contribution to the dipole scattering at room temperature is also neglected. Both the elastic and the inelastic mobility components are found to decrease with the increase in the effective electric field, $E_{eff}$, in contrast to the case of the mobility limited by the charged centers, such as the substrate impurities and the fixed charges. $^{34,52}$ Such behavior can be qualitatively understood as follows. For a low $E_{eff}$ region, de Broglie wavelength of electrons becomes large, and the dipole potential distribution is averaged for such electrons with larger wavelength than the average distance among dipoles. Thus, the frequency of the dipole scattering is reduced for the low $E_{eff}$ region. For an extremely low $E_{eff}$ region, however, the elastic dipole scattering becomes strong. This is because the inter-subband scattering rate becomes large due to the

![](./images/813205441000505344_8.jpg)

FIG. 6. Elastic and inelastic component of $\mu_{dipole}$ due to polarized Si-O dipole. The dipole concentration, $N_{dipole}$, is taken to be $6.87 \times 10^{14}\ \text{cm}^{-2}$.

narrow subband energy interval. For the case of the inelastic dipole scattering, the subband energy interval becomes nar- rower than the vibrational energy of the Si atom. As a result, the transition among the subbands caused by the phonon emission can hardly occur and the scattering rate of the inelastic dipole scattering continues to decrease with the decrease in $E_{eff }$ . For a high $E_{eff }$ region, on the other hand, de Broglie wavelength of electron becomes smaller than the av- erage distance between dipoles. Since the dipole potential is intensified within the range of the average distance between dipoles, the strength of the dipole scattering is enhanced for the high $E_{eff }$ region.

Figure. 7 shows the influence of the inelastic phonon scattering on $\mu_{dipole }$ . It is found from Fig. 7 that the elastic dipole scattering component makes the main contribution. The contribution from the inelastic scattering component is relatively small, because the heavy mass of the Si and oxy- gen atom reduces the frequency of the inelastic dipole scat- tering (see Eqs. (40) and (41)). However, the influence of the inelastic dipole scattering is still obvious. This is because the vibrational energy of the Si atom (17 meV) is almost compa- rable with the electron thermal energy in the inversion layer, and the frequency of the inelastic scattering process becomes large. The influence of the inelastic dipole scattering becomes large at high temperature because the inter-subband scattering due to the phonon emission can frequently occur because of the large electron thermal energy, though its influence is relatively small at room temperature. The low vibrational energy of the polarized Si atom suggests the exis- tence of another scattering component caused by the cou- pling of the localized phonon mode with the plasmon excitation. Since the plasmon excitation occurs in the middle-range $E_{eff }$ region $^{38,39}$ (the lifetime of the plasmon ex citation is reduced in the low $E_{eff }$ region, whereas the large plasmon energy at high $E_{eff }$ region prevents the plasmon ex citation), the strong coupling between the localized phonon mode and the plasmon excitation can lead to the mobility degradation in the middle-range $E_{eff }$ region. Therefore, not only the elastic dipole scattering but also the inelastic scat- tering has to be taken into account for the quantitative evalu- ation of $\mu_{dipole }$ .

Figure. 8 shows the effective electric field dependence of the effective field mobility, $\mu_{eff }$ , calculated by adding the contributions from the bulk phonon-scattering-limited mobil- ity and $\mu_{dipole }$ based on Matthiessen's rule as

$$
\mu_{\text {eff }}^{-1}=\mu_{\text {phonon }}^{-1}+\mu_{\text {dipole }}^{-1},\qquad(56)
$$

where $\mu_{phonon }$ is the bulk phonon-scattering-limited mobility. It is found from Fig. 8 that the interface Si-O dipole scattering leads to significant mobility degradation. It should be men- tioned here that the calculated $\mu_{phonon }$ shows weaker $E_{eff }$ -de pendence than expected from the experiment $(\propto E_{eff }^{\frac{3}{2}})^{7}$ Such behavior has also been pointed out by several authors. $^{6,49}$ The inconsistency of the $E_{eff }$ -dependence of $\mu_{phonon }$ between the model calculation and the experiment has been a long- standing issue. $^{6,40,49}$ From Fig. 8, it is found that the dipole scattering in addition to the inelastic dipole scattering gives the stronger $E_{eff }$ -dependence of the effective field mobility, $\mu_{eff }$ . This fact indicates that the experimental $E_{eff }^{\frac{3}{2}}$ -dependence of the inversion layer mobility can be attributed to the dipole scattering due to the interface Si-O dipole. It should be pointed out here that the value of the deformation potential of the acoustic phonon used in our study (Table I) is smaller than the value given in the literature $^{8,40,49}$ and is close to the value of bulk Si deformation potential. This is because the addi- tional dipole scattering component is considered in addition to the conventional phonon scattering component.

![](./images/813205441000505344_9.jpg)

FIG. 7. Influence of the inelastic phonon scattering on $\mu_{dipole }$ due to polarized Si-O dipole. The dipole concentration, $N_{dipole }$ , is taken to be $6.87 \times 10^{14} ~cm^{-2}$ .

![](./images/813205441000505344_10.jpg)

FIG. 8. Calculated results of the effective field mobility, $\mu_{eff }$  $=(\mu_{phonon }^{-1}+\mu_{dipole }^{-1})^{-1}$ .

By considering the contribution from the surface rough- ness scattering, the universal curve is well reproduced(Fig. 9). Note that the amount of roughness parameters $\Delta$  becomes almost $\sim 0.6 ~nm$ when using the Matsumoto Uemura surface roughness model $^{51}$ without considering the dipole scattering. This is an unphysically large value consid- ering the interface geometry $^{41-44}$ (the Si-O bond length is~0.16 nm and the width of the roughness step is an order of the magnitude, 0.3 nm ), whereas the value of $\Delta$ obtained by our calculation, $\Delta=0.35 nm$ , is reasonable in comparisonwith the values reported in the literature. $^{6}$

<table>
<caption>TABLE I. Physical parameters used in the present calculations.</caption>
<tbody>
<tr>
<td>$\rho$</td>
<td>Crystal density</td>
<td>$2329\ \text{kg}\ \text{m}^{-3}$</td>
</tr>
<tr>
<td>$s_{l}$</td>
<td>Sound velocity</td>
<td>$9037\ \text{m}\ \text{s}^{-1}$</td>
</tr>
<tr>
<td>$D_{\text{ac}}$</td>
<td>Acoustic deformation potential</td>
<td>$10\ \text{eV}$</td>
</tr>
</tbody>
</table>

![](./images/813205441000505344_11.jpg)

FIG. 9. Comparison of the calculated results of the effective field mobility, $\mu_{\text{eff}} = (\mu_{\text{phonon}}^{-1} + \mu_{\text{dipole}}^{-1} + \mu_{\text{sr}}^{-1})^{-1}$, considering phonon scattering ($\mu_{\text{phonon}}$), surface roughness scattering ($\mu_{\text{sr}}$), and dipole scattering due to the interface Si-O dipole ($\mu_{\text{dipole}}$), with the universal curve.

It should also be noted that the dipole scattering causes the non-negligible violation of the universality (Figs. 7 and 8). This is because the dipole potential originates from the Coulomb potential of the polarized Si-O dipole, and the strength of the Coulomb potential depends strongly on the surface carrier concentration, $N_s$, rather than $E_{\text{eff}}$. For the case of the phonon scattering, the frequency of the phonon scattering depends on the inversion layer width through the form factor, Eqs. (B1)-(B13). Since the inversion layer width is identified uniquely by $E_{\text{eff}}$, the bulk phonon-scattering-limited mobility is determined by $E_{\text{eff}}$. However, as can be seen from Fig. 9, the slight discrepancies from the universality caused by the dipole scattering can be absorbed in substrate impurity scattering and surface roughness scatterings. Therefore, we conclude that the interface Si-O dipole scattering is one of the main scattering components limiting the carrier transport in the inversion layer, in addition to the substrate impurity scattering, the bulk phonon scattering, and the surface roughness scattering.

Finally, we would like to comment on the influence of the surface roughness on the Si-O dipole scattering. The distortion of the Si-O dipole-position caused by the surface roughness leads to the fluctuation of the dipole potential. Such fluctuation of the dipole potential also becomes an origin of the carrier scattering, and the Si-O dipole scattering becomes more influential on the interface carrier transport through the surface roughness. By considering the additional scattering induced by the fluctuation of the Si-O dipole potential caused by the surface roughness, the conventional surface roughness scattering becomes less influential on the interface carrier transport. The roughness rms value $\Delta$ is considered to be smaller than the value obtained in this study. When it is used with the more physics-based surface roughness scattering model that takes into account the various roughness-related scattering components inherent to the interface, for example, the Ando model, $^5$ the value of $\Delta$ is considered to be reduced further. These considerations indicate that the conventional surface roughness scattering component that considers only the fluctuation of the electrostatic potential induced by the surface roughness is the additional scattering component, but the polarized Si-O dipole scattering and its fluctuation due to the surface roughness are the main scattering components, of the universal curve.

Therefore, study of the dipole scattering under the surface roughness is worthwhile for the further understanding of the interface carrier transport. For example, the approach to include the interface geometry accurately by the band structure calculation $^{54}$ is a powerful approach for such purpose.

## VI. CONCLUSIONS

We have reported an extensive study on the atomic structure dependence of carrier transport in the $\text{Si}/\text{SiO}_2$ interface. By performing the first-principles calculations, we have found the strong dipole formation due to the polarized Si-O dipole with the effective charge of $-1.1e$ ($e$ is the elementary charge). We have also found that only the Si atom of the dipole vibrates parallel to the interface, whereas the oxygen atom of the dipole is kept almost fixed, at the lowest vibrational energy which is almost comparable to electron thermal energy, and this lowest-energy-vibrational mode makes the main contribution to the Si-O dipole scattering. Based on these findings, the dipole scattering model has been formulated, including the contribution from both the inelastic scattering and the elastic scattering. The mobility limited by the interface Si-O dipole scattering has been quantitatively evaluated based on the relaxation-time approximation to examine the influence of the dipole scattering due to the interface Si-O dipole on the carrier transport in the inversion layer.

Though the main contribution comes from the elastic dipole scattering component, we have found that the influence of the inelastic dipole scattering is still obvious. We have found that the dipole scattering gives stronger $E_{\text{eff}}$-dependence of the mobility than the bulk phonon scattering does, and that the experimental $E_{\text{eff}}^3$-dependence of the inversion layer mobility is attributable to the dipole scattering due to the interface Si-O dipole. Upon the incorporation of the Si-O dipole scattering, universal curves have been fully predicted.

This fact indicates that the interface Si-O dipole scattering is one of the main scattering components limiting the carrier transport in the inversion layer, in addition to the conventional scattering components: the substrate impurity scattering, the bulk phonon scattering, and the surface roughness scattering. Besides the case of the $\text{Si}/\text{SiO}_2$ interface, our findings are generally applicable to any interfaces between different materials, where the dipoles are formed owing to the large charge transfer. Therefore, it is essential to consider the interface dipole scattering for the quantitative understanding of the interface carrier transport.

## ACKNOWLEDGMENTS

We would like to thank Dr. Yuuichiro Mitani of Toshiba Corporation for his support throughout this study.

## APPENDIX A: DERIVATION OF ELASTIC DIPOLE SCATTERING POTENTIAL

According to the procedure given in Ref. 18, the elastic dipole scattering potential is derived as follows. Using Fourier transformation, Eq. (1) can be further expressed as follows:

$$
\begin{aligned}
\rho_{\text {ext,dipole }}(\mathbf{r}, z)= & \frac{1}{V} \sum_{i}\left[\sum_{\mathbf{q}} e^{i \mathbf{q} \cdot\left(\mathbf{r}-\mathbf{R}_{i}\right)} \delta\left(z-R_{z}\right)\right. \\
& \left.-\sum_{\mathbf{q}} e^{i \mathbf{q} \cdot\left(\mathbf{r}-\mathbf{R}_{i}-\mathbf{r}_{a}\right)} \delta\left(z-R_{z}-z_{a}\right)\right], \quad(\mathrm{A} 1) \\
= & \frac{1}{V} \sum_{i}\left[\left(\sum_{\mathbf{q} \neq 0} e^{i \mathbf{q} \cdot\left(\mathbf{r}-\mathbf{R}_{i}\right)}+1\right) \delta\left(z-R_{z}\right)\right. \\
& \left.-\left(\sum_{\mathbf{q} \neq 0} e^{i \mathbf{q} \cdot\left(\mathbf{r}-\mathbf{R}_{i}-\mathbf{r}_{a}\right)}+1\right) \delta\left(z-R_{z}-z_{a}\right)\right], \quad \text { (A2) } \\
= & N_{\text {dipole }}\left(\delta\left(z-R_{z}\right)-\delta\left(z-R_{z}-z_{a}\right)\right) \\
& +\frac{1}{V} \sum_{i}\left[\sum_{\mathbf{q} \neq 0} e^{i \mathbf{q} \cdot\left(\mathbf{r}-\mathbf{R}_{i}\right)} \delta\left(z-R_{z}\right)\right. \\
& \left.-\sum_{\mathbf{q} \neq 0} e^{i \mathbf{q} \cdot\left(\mathbf{r}-\mathbf{R}_{i}-\mathbf{r}_{a}\right)} \delta\left(z-R_{z}-z_{a}\right)\right], \quad \text { (A3) }
\end{aligned}
$$

where $N_{\text {dipole }}$ is the two-dimensional surface dipole concen- tration. The first term in Eq. (A3) is the continuous distribu- tion of the dipoles averaged with respect to $\mathbf{r}$, whereas the second term represents the discrete dipole distribution that excludes the contribution of the continuous dipole distribu- tion. $^{45}$ Such decomposition of the dipole distribution indicates that the dipole potential comes from the two parts $^{18}$

$$
\psi_{\text {dipole }}(\mathbf{r}, z)=\psi_{\text {continuous }}(z)+\psi_{\text {dis }}(\mathbf{r}, z). \quad \text { (A4) }
$$

$\psi_{\text {continuous }}(z)$ is the potential component under the average charge distribution of the dipoles

$$
\rho_{\text {ext,continuous }}(z)=N_{\text {dipole }}\left(\delta\left(z-R_{z}\right)-\delta\left(z-R_{z}-z_{a}\right)\right) . \text { (A5) }
$$

Since $\psi_{\text {continuous }}(z)$ is determined electrostatically under the application of the gate voltage and depends only on $z$, $\psi_{\text {continuous }}(z)$ satisfies the following Poisson equation:

$$
\begin{aligned}
\frac{\partial}{\partial z}\left[\epsilon(z) \frac{\partial \psi_{\text {continuous }}(z)}{\partial z}\right]=e^{*} \rho_{\text {ext,continuous }}(z) & +e \rho_{\mathrm{Si}}^{0}(z)-N_{\mathrm{A}}, \\
& (\mathrm{A} 6)
\end{aligned}
$$

where $e^{*}$ is the effective charge of the dipole, $N_{\mathrm{A}}$ is the acceptor density, and $\rho_{\mathrm{Si}}^{0}(z)$ is the electron density in the inversion layer. Since $\psi_{\text {continuous }}(z)$ is the electrostatic potential that contributes to the formation of the sub-band structure and contains no singularity, $\psi_{\text {continuous }}(z)$ is not responsible for the dipole scattering.

On the other hand, $\psi_{\text {dipole }}(\mathbf{r}, z)$ is the net potential distribution under the total dipole distribution (Eq. (1)), and is determined from the following Poisson equation:

$$
\begin{aligned}
\nabla\left[\epsilon(z) \nabla \psi_{\text {dipole }}(\mathbf{r}, z)\right]=e^{*} \rho_{\text {ext,dipole }}(\mathbf{r}, z)+e \rho_{\mathrm{Si}}(\mathbf{r}, z)-N_{\mathrm{A}}, \\
(\mathrm{A} 7)
\end{aligned}
$$

where $\rho_{\mathrm{Si}}(\mathbf{r}, z)$ is the electron density defined by

$$
\rho_{\mathrm{Si}}(\mathbf{r}, z)=\sum_{j, k} N_{j}^{k}(\mathbf{r}) g_{j}^{k}(z), \quad \text { (A8) }
$$

where $g_{i}^{k}(z)=\zeta_{i}^{k}(z) \cdot \zeta_{i}^{k *}(z)\left(\zeta_{i}^{k}(z)\right.$ is the envelope function) is the inversion layer carrier density of $i$ th subband at valley $k$ and $N_{i, k}(\mathbf{r})$ is the two-dimensional surface carrier concentration under the potential variation $\bar{\psi}_{\text {dis }}^{i k}(\mathbf{r})$ that is given as

$$
N_{i}^{k}(\mathbf{r})=\frac{n_{v}^{i k} m_{d}^{k}}{\pi \hbar^{2}} F_{0}\left(\frac{E_{F}-E_{i}^{k}-e \bar{\psi}_{\text {dis }}^{i k}(\mathbf{r})}{k_{B} T}\right), \quad \text { (A9) }
$$

where $E_{F}$ is the Fermi level, $E_{i}^{k}$ is the sub-band energy, $F_{0}(x)=\log \left(1+e^{x}\right)$, and $\bar{\psi}_{\text {dipole }}^{i k}(\mathbf{r})$ is expressed as

$$
\bar{\psi}_{\text {dis }}^{i k}(\mathbf{r})=\int d z \psi_{\text {dis }}(\mathbf{r}, z) g_{i}^{k}(z). \quad \text { (A10) }
$$

Here, $\psi_{\text {dis }}(\mathbf{r}, z)$ is given by

$$
\psi_{\text {dis }}(\mathbf{r}, z)=\psi_{\text {dipole }}(\mathbf{r}, z)-\psi_{\text {continuous }}(z), \quad \text { (A11) }
$$

according to Eq. (A4). Thus, $\psi_{\text {dis }}(\mathbf{r}, z)$ is interpreted as the discrete and singular part of the dipole potential that excludes the contribution of the electrostatic potential component, $\psi_{\text {continuous }}(z)$. Therefore, $\psi_{\text {dis }}(\mathbf{r}, z)$ is indeed the scattering potential responsible for the dipole scattering, and we express $\psi_{\text {dis }}(\mathbf{r}, z)$ as $\psi_{\text {scat }}(\mathbf{r}, z)$ in the following. It should be noted here on the validity of Eq. (A9) that is the basis of the above derivation. We assume that the electron charge in the inversion layer follows the variation of the interface dipole potential. This assumption holds when the electron wavelength is smaller than the average distance between the dipoles $\left(r_{\text {ave }}\right)$. When the electron wavelength becomes larger than $r_{\text {ave }}$, this assumption does not hold and the multi-dipole screening needs to be considered because the dipoles within the range of the electron wavelength contribute to the screening. Such situation can actually occur for low-energy electrons. As was discussed in Refs. 55 and 56, the free electrons cannot screen a given dipole in a multi-dipole system as effectively as they can screen the same dipole in a single-dipole system, and the multi-dipole screening model should be taken into account. However, such a situation can only occur for the low surface electron concentration region in the inversion layer, and the influence of the screening effect due to the free electrons is small. Therefore, the use of Eq. (A9) does not cause the significant errors and the essence of our results is not altered.

Substituting Eq. (A4) into Eq. (A7) and using Eq. (A6), we obtain the Poisson equation that determines $\psi_{\text {scat }}(\mathbf{r}, z)$

$$
\begin{aligned}
\nabla\left[\epsilon(z) \nabla \psi_{\text {scat }}(\mathbf{r}, z)\right]=e^{*}\left\{\rho_{\text {ext,dipole }}(\mathbf{r}, z)-N_{\text {dipole }}\left(\delta\left(z-R_{z}\right)\right.\right. \\
\left.\left.-\delta\left(z-R_{z}-z_{a}\right)\right)\right\}+e\left\{\rho_{\mathrm{Si}}(\mathbf{r}, z)-\rho_{\mathrm{Si}}^{0}(z)\right\} .
\end{aligned}
$$

$\rho_{\mathrm{Si}}(\mathbf{r}, z)$ is expanded in terms of $\psi_{\text {scat }}(\mathbf{r}, z)$ as was carried out by Stern and Howard, ${ }^{46}$

$$
\rho_{\mathrm{Si}}(\mathbf{r}, z) \simeq \rho_{\mathrm{Si}}^{0}(z)+\frac{2 \epsilon_{s i}}{e} \sum_{i, k} s_{i}^{k} \bar{\psi}_{\text {scat }}^{i k}(\mathbf{r}) g_{i}^{k}(z), \quad \text { (A13) }
$$

where $s_{i}^{k}$ is the screening factor defined by

$$
s_{i}^{k}=\frac{e^{2} N_{i}^{k}}{2 \epsilon_{\mathrm{Si}} E_{d}^{i k}}, \tag{A14}
$$

$$
E_{d}^{i k}=k T\left(1+e^{-x}\right) \log \left(1+e^{-x}\right), \tag{A15}
$$

$$
x=\frac{E_{i}^{k}-E_{F}}{k T}. \tag{A16}
$$

Introducing the notations

$$
\begin{aligned}
\rho_{\mathrm{ext}, \mathrm{dis}}(\mathbf{r}, z)= & \sum_{i}\left(\delta\left(\mathbf{r}-\mathbf{R}_{i}\right) \delta\left(z-R_{z}\right)\right. \\
& -\delta\left(\mathbf{r}-\mathbf{R}_{i}-\mathbf{r}_{a}\right) \delta\left(z-R_{z}-z_{a}\right) \\
& -\rho_{\mathrm{ext}, \mathrm{continuous}}(z), \quad \text { (A17) }
\end{aligned}
$$

Eq. (A12) can be rewritten as

$$
\begin{aligned}
\nabla\left[\epsilon(z) \nabla \psi_{\text {scat }}(\mathbf{r}, z)\right]= & e^{*} \rho_{\text {ext,dis }}(\mathbf{r}, z) \\
& +2 \epsilon_{\mathrm{Si}} \sum_{i, k} s_{i}^{k} \bar{\psi}_{\text {scat }}^{i k}(\mathbf{r}) g_{i}^{k}(z), \quad \text { (A18) }
\end{aligned}
$$

Multiplying both sides of Eq. (A18) by $\exp (i \mathbf{q} \cdot \mathbf{r})$ and integrating over $\mathbf{r}$, we get

$$
\begin{aligned}
& \left(\frac{\partial}{\partial z} \epsilon(z) \frac{\partial}{\partial z}-\epsilon(z) q^{2}\right) A(\mathbf{q}, z) \\
& \quad=e^{*} \rho_{\text {ext }}(\mathbf{q}, z)+2 \epsilon_{\mathrm{Si}} \sum_{i, k} s_{i}^{k} g_{i}^{k}(z) \int d z^{\prime} A\left(\mathbf{q}, z^{\prime}\right) g_{i}^{k}\left(z^{\prime}\right). \\
& \quad \text { (A19) }
\end{aligned}
$$

Here, the following Fourier transformations have been introduced:

$$
\begin{aligned}
\rho_{\text {ext }}(\mathbf{q}, z) & =\int d \mathbf{r} \exp (i \mathbf{q} \cdot \mathbf{r}) \rho_{\text {ext,dis }}(\mathbf{r}, z), \\
A(\mathbf{q}, z) & =\int d \mathbf{r} \exp (i \mathbf{q} \cdot \mathbf{r}) \psi_{\text {scat }}(\mathbf{r}, z).
\end{aligned}
$$

To solve Eq. (A19), we introduce the Green function, $G_{q}\left(z, z^{\prime}\right)$, which satisfies the following equation:

$$
\left(\frac{\partial}{\partial z} \epsilon(z) \frac{\partial}{\partial z}-\epsilon(z) q^{2}\right) G_{q}\left(z, z^{\prime}\right)=\delta\left(z-z^{\prime}\right). \quad \text { (A21) }
$$

The expressions for $G_{q}\left(z, z^{\prime}\right)$ are given in, for example, Refs. 18, 47, and 48.

## APPENDIX B: SCATTERING MODELS FOR PHONON SCATTERING AND SURFACE ROUGHNESS SCATTERING

Using the subband energy and the wave function obtained by solving the Schrödinger and Poisson equations self-consistently, the phonon-scattering-limited electron mobility and surface-roughness-scattering-limited mobility were calculated under the relaxation-time approximation. We employ the conventional scattering model for bulk phonon scattering and surface roughness scattering. First, the expression of the relaxation time and the scattering parameters for phonon scattering are described. Fig. 5 shows the schematic diagram of each phonon scattering process and its transition path between the valleys.

### 1. Intra-valley phonon scattering model

According to the selection rules for the electron-phonon interaction in bulk $\mathrm{Si}$, intra-valley phonon scattering is allowed for acoustic phonon. The momentum-relaxation rate for deformation potential scattering by intra-valley acoustic phonon from the $i$ th subband to the $j$ th subband is given by $^{49}$

$$
\frac{1}{\tau_{a c 2}^{i, j}(E)}=\frac{n_{\nu 2} m_{d 2} D_{a c}^{2} k_{B} T}{\hbar^{3} \rho s_{l}^{2}} \cdot \frac{1}{W_{i, j}}, \quad \text { (B1) }
$$

$$
\frac{1}{W_{i, j}}=\int \zeta_{i}(z)^{2} \zeta_{j}(z)^{2} d z, \quad \text { (B2) }
$$

$$
\frac{1}{\tau_{a c 4}^{i, j}(E)}=\frac{n_{\nu 4} m_{d 4} D_{a c}^{2} k_{B} T}{\hbar^{3} \rho s_{l}^{2}} \cdot \frac{1}{W_{i, j}^{\prime}}, \quad \text { (B3) }
$$

$$
\frac{1}{W_{i, j}^{\prime}}=\int \zeta_{i}^{\prime}(z)^{2} \zeta_{j}^{\prime}(z)^{2} d z, \quad \text { (B4) }
$$

where $D_{\text {ac }}$ denotes the deformation potential due to acoustic phonon, $n_{v}^{\text {ac }}$ is the degeneracy of the valley with respect to intra-valley scattering, $\rho$ is the mass density of the crystal, and $s_{l}$ is the longitudinal sound velocity. The value of $n_{v}^{\text {ac }}$ is taken to be 2 and 1 for the twofold and the fourfold valleys, respectively. $W_{i, j}$ is the form factor determined by the wave functions of the $i$ th and the $j$ th subbands, and $W_{i, i}$ is interpreted to be the effective thickness of the wave function of the $i$ th subband with respect to $z$. The total scattering probability of electrons in the $i$ th subband with energy $E, \tau_{\mathrm{ac}}^{i}(E)$, is given by summing up $\tau_{\mathrm{ac}}^{i, j}(E)$ over all subbands where the transition is allowed

$$
\frac{1}{\tau_{a c 2}^{i}}=\sum_{j} \frac{U\left(E-E_{j}\right)}{\tau_{a c 2}^{i, j}(E)}, \quad \text { (B5) }
$$

$$
\frac{1}{\tau_{a c 4}^{i}}=\sum_{j} \frac{U\left(E-E_{j}^{\prime}\right)}{\tau_{a c 4}^{i, j}(E)}, \quad \text { (B6) }
$$

where $U(x)$ is the step function defined by

$$
U(x)=1 \quad \text { for } \quad x>0, \quad \text { (B7) }
$$

$$
U(x)=0 \quad \text { for } \quad x<0. \quad \text { (B8) }
$$

The physical parameters used in the calculation of Eqs. (B1) and (B3) are listed in Table I.

### 2. Inter-valley phonon scattering model

The momentum-relaxation rate for inter-valley phonon scattering from the $i$ th subband in the twofold valleys to the $j$ th subband in the fourfold valleys is given by $^{49}$

$$
\begin{aligned}
\frac{1}{\tau_{\text {inter2 }}^{i, j}(E)}= & \sum_{k}^{\{f\}} \frac{n_{\nu 2 \rightarrow 4}^{f} m_{d 4} D_{k}^{2} k_{B} T}{\hbar \rho E_{k}} \cdot \frac{1}{V_{i, j}}\left(N_{k}+\frac{1}{2} \pm \frac{1}{2}\right) \\
& \times \frac{1-f\left(E \mp E_{k}\right)}{1-f(E)} \cdot U\left(E \mp E_{k}-E_{j}^{\prime}\right), \quad \text { (B9) } \\
\frac{1}{V_{i, j}}= & \int \zeta_{i}(z)^{2} \zeta^{\prime}{ }_{j}(z)^{2} d z, \quad \text { (B10) }
\end{aligned}
$$

where $n_{\nu 2 \rightarrow 4}^{f}=4$ is the degeneracy of the valleys into which electrons are scattered, $D_{k}$ and $E_{k}$ are the deformation potential and the energy of the $k$ th inter-valley phonon, respectively, $N_{k}$ is the occupation number of the $k$ th inter-valley phonon, the plus and the minus signs in $(N_{k}+\frac{1}{2} \pm \frac{1}{2})$ correspond to phonon emission and phonon absorption, $f(E)$ is the Fermi-Dirac distribution function, and the summation with respect to $k$ is performed over all the f-phonons. Similarly, the relaxation time for transitions $\tau_{\text {inter4 }}^{i, j}(E)$ from the $i$ th subband in the fourfold valley to the $j$ th subband in the fourfold valleys, and the relaxation time for transitions $\tau_{\text {inter4 }}^{\prime i, j}(E)$ from the $i$ th subband in the fourfold valley to the $j$ th subband in the twofold valleys, are given by Eqs. (B11) and (B12), respectively,

$$
\begin{aligned}
\frac{1}{\tau_{\text {inter4 }}^{i, j}(E)}= & \sum_{k}^{\{f\}} \frac{n_{\nu 4 \rightarrow 4}^{f} m_{d 4} D_{k}^{2} k_{B} T}{\hbar \rho E_{k}} \cdot \frac{1}{W^{\prime}{ }_{i, j}}\left(N_{k}+\frac{1}{2} \pm \frac{1}{2}\right) \\
& \times \frac{1-f\left(E \mp E_{k}\right)}{1-f(E)} \cdot U\left(E \mp E_{k}-E_{j}^{\prime}\right) \\
+ & \sum_{k}^{\{f\}} \frac{n_{\nu 4 \rightarrow 2}^{g} m_{d 4} D_{k}^{2} k_{B} T}{\hbar \rho E_{k}} \cdot \frac{1}{W^{\prime}{ }_{i, j}}\left(N_{k}+\frac{1}{2} \pm \frac{1}{2}\right) \\
& \times \frac{1-f\left(E \mp E_{k}\right)}{1-f(E)} \cdot U\left(E \mp E_{k}-E_{j}^{\prime}\right), \quad \text { (B11) }
\end{aligned}
$$

$$
\begin{aligned}
\frac{1}{\tau_{\text {inter4 }}^{\prime i, j}(E)}= & \sum_{k}^{\{f\}} \frac{n_{\nu 4 \rightarrow 2}^{f} m_{d 2} D_{k}^{2} k_{B} T}{\hbar \rho E_{k}} \cdot \frac{1}{V^{\prime}{ }_{i, j}}\left(N_{k}+\frac{1}{2} \pm \frac{1}{2}\right) \\
& \times \frac{1-f\left(E \mp E_{k}\right)}{1-f(E)} \cdot U\left(E \mp E_{k}-E_{j}\right), \quad \text { (B12) } \\
\frac{1}{V^{\prime}{ }_{i, j}}= & \int \zeta^{\prime}{ }_{i}(z)^{2} \zeta^{\prime}{ }_{j}(z)^{2} d z, \quad \text { (B13) }
\end{aligned}
$$

where $n_{\nu 4 \rightarrow 4}^{f}=2$, $n_{\nu 4 \rightarrow 4}^{g}=1$, and $n_{\nu 4 \rightarrow 2}^{f}=2$ are the degeneracies of the valleys into which electrons are scattered. The total inter-valley phonon scattering probabilities of electrons, $\tau_{\text {inter2 }}^{i}$ and $\tau_{\text {inter4 }}^{i}$, in the twofold and the fourfold valleys, respectively, are

$$
\frac{1}{\tau_{\text {inter2 }}^{i}}=\sum_{j} \frac{U\left(E-E_{j}\right)}{\tau_{\text {inter2 }}^{i, j}(E)}, \quad \text { (B14) }
$$

$$
\frac{1}{\tau_{\text {inter4 }}^{i}}=\sum_{j} \frac{U\left(E-E_{j}^{\prime}\right)}{\tau_{\text {inter4 }}^{i, j}(E)}+\sum_{j} \frac{U\left(E-E_{j}^{\prime}\right)}{\tau_{\text {inter4 }}^{\prime i, j}(E)}. \quad \text { (B15) }
$$

Parameters for inter-valley phonon scattering models are summarized in Table II. These parameters were taken from Ref. 50.

<table><caption>TABLE II. Parameters for inter-valley phonon scattering models.</caption>
<tbody>
<tr>
<th>Type of intervalley scattering</th>
<td>$E_{k}$ (meV)</td>
<td>$D_{k}$ ($\times 10^{8}$ eV/cm)</td>
</tr>
<tr>
<th>f</th>
<td>19.0</td>
<td>0.3</td>
</tr>
<tr>
<th>f</th>
<td>47.5</td>
<td>2.0</td>
</tr>
<tr>
<th>f</th>
<td>59.1</td>
<td>2.0</td>
</tr>
<tr>
<th>g</th>
<td>12.1</td>
<td>0.5</td>
</tr>
<tr>
<th>g</th>
<td>18.6</td>
<td>0.8</td>
</tr>
<tr>
<th>g</th>
<td>62.2</td>
<td>11.0</td>
</tr>
</tbody>
</table>

## 3. Surface roughness scattering model

We have used the surface roughness scattering model proposed by Matsumoto and Uemura. $^{51}$ The perturbation potential associated with the surface roughness proposed by their model is given by

$$
\Delta V_{s}(z)=\frac{\partial V_{h}(z)}{\partial z} \Delta(\mathbf{r}), \quad \text { (B16) }
$$

where $\Delta(\mathbf{r})$ is the displacement of the interface from a perfect plane layer, and $V_{h}(z)$ is the Hartree potential calculated by Poisson's equation. Then, the scattering matrix element for electrons in the $i$ th subband is given by

$$
\Delta H_{\mathrm{woscr}, \mathrm{i}}^{l}(\mathbf{q})=\int d z \zeta_{i}^{\prime l}(z) \frac{\partial V_{h}(z)}{\partial z} \zeta_{i}^{\prime l}(z) \cdot \Delta(\mathbf{q}), \quad \text { (B17) }
$$

where $l$ is the valley index, and $\mathbf{q}=|\mathbf{k}^{\prime}-\mathbf{k}|$. Here, the intersubband transitions are neglected, and the screening effect by the free carriers in the inversion layer is not considered. The screening effect by the free carriers in the inversion layer can be included in the same way as for the case of the elastic dipole scattering, and the scattering matrix element that includes the screening effect is given by $^{52,53}$

$$
\Delta H_{\mathrm{scr}, \mathrm{i}}^{l}(\mathbf{q})=\Delta H_{\mathrm{woscr}, \mathrm{i}}^{l}(\mathbf{q})+2 \epsilon_{\mathrm{Si}} \sum_{k j} s_{j}^{k} \Delta H_{\mathrm{scr}, \mathrm{j}}^{l}(\mathbf{q})^{k} G_{i j}^{l k}. \quad (\mathrm{B} 18)
$$

Then, the momentum relaxation time for the surface roughness scattering is given by

$$
\begin{aligned}
\frac{1}{\tau_{\text {rough }}^{i k}(E, \theta)}=\frac{1}{2 \pi \hbar} \int d \mathbf{k}^{\prime}(1-\cos (\theta)) \delta\left(E^{\prime}-E\right)\left\langle\left|\Delta H_{\text {scr,i }}^{l}(\mathbf{q})\right|^{2}\right\rangle. \\
(\mathrm{B} 19)
\end{aligned}
$$

In order to calculate $\tau_{\text {rough }}^{i k}$, the roughness power spectrum, $S(q)=\langle|\Delta(\mathbf{q})|^{2}\rangle$, must be determined. We have used the following form of $S(q)$ proposed by Pirovano: $^{28,29}$

$$
S(q)=\pi(\Delta \Lambda)^{2} e^{-\frac{(q \Lambda)^{4}}{4}}, \quad \text { (B20) }
$$

where $\Delta$ is the roughness rms value, and $\Lambda$ is the correlation length. This form of $S(q)$ was chosen to reproduce the universality of both electron and hole mobility under the same parameters $\Delta$ and $\Lambda$ in MOSFETs with pure $\mathrm{SiO}_{2}$ gate oxides. $^{28}$ The values of $\Delta$ and $\Lambda$ used in this study are $\Delta=0.35 \mathrm{~nm}$ and $\Lambda=1.2 \mathrm{~nm}$, respectively. Note that another functional form of the roughness power spectrum has also been proposed. $^{57,58}$ When the another form is used, the essence of our results is not altered.

$^1$T. Yamasaki, C. Kaneta, T. Uchiyama, T. Uda, and K. Terakura, *Phys. Rev. B* **63**, 115314 (2001).

$^2$K. Kato and T. Uda, *Phys. Rev. B* **62**, 15978 (2000).

$^3$K. Tatsumura, T. Shimura, E. Mishima, K. Kawamura, D. Yamasaki, H. Yamamoto, T. Watanabe, M. Umeno, and I. Ohdomari, *Phys. Rev. B* **72**, 045205 (2005).

$^4$K. Tatsumura, T. Watanabe, D. Yamasaki, T. Shimura, M. Umeno, and I. Ohdomari, *Phys. Rev. B* **69**, 085212 (2004).

$^5$T. Ando, A. B. Fowler, and F. Stern, *Rev. Mod. Phys.* **54**, 437 (1982).

$^6$M. V. Fischetti and S. E. Laux, *Phys. Rev. B* **48**, 2244 (1993).

$^7$S. Takagi, A. Toriumi, M. Iwase, and H. Tango, *IEEE Trans. Electron. Devices* **41**, 2357 (1994).

$^8$S. Takagi, A. Toriumi, M. Iwase, and H. Tango, *IEEE Trans. Electron. Devices* **41**, 2363 (1994).

$^9$M. H. Evans, X.-G. Zhang, J. D. Joannopoulos, and S. T. Pantelides, *Phys. Rev. Lett.* **95**, 106802 (2005).

$^{10}$K. Kato, T. Yamasaki, and T. Uda, *Phys. Rev. B* **73**, 073302 (2006).

$^{11}$T. Ishihara, D. Matsushita, K. Tatsumura, Y. Nakabayashi, J. Koga, and K. Kato, Tech. Dig. - Int. Electron. Devices Meet., 101 (2007).

$^{12}$W. A. Harrison, *Elementary Electronic Structure* (World Scientific, 1999).

$^{13}$P. Perfetti, C. Quaresima, C. Coluzza, C. Fortunato, and G. Margaritondo, *Phys. Rev. Lett.* **57**, 2065 (1986).

$^{14}$H. Z. Massoud, *J. Appl. Phys.* **63**, 2000 (1988).

$^{15}$T. Ishihara, D. Matsushita, and Koichi Kato, Tech. Dig. - Int. Electron. Devices Meet., 4.3.1–4.3.4 (2009).

$^{16}$D. Jena, A. C. Gossard, and U. K. Mishra, *J. Appl. Phys.* **88**, 4734 (2000).

$^{17}$W. Zhao and D. Jena, *J. Appl. Phys.* **96**, 2095 (2004).

$^{18}$T. Ishihara, J. Koga, K. Matsuzawa, and S. Takagi, *J. Appl. Phys.* **102**, 073702 (2007).

$^{19}$P. R. Rimbey and G. D. Mahan, *J. Appl. Phys.* **57**, 2812 (1985).

$^{20}$N. Sano, K. Matsuzawa, M. Mukai, and N. Nakayama, *Microelectron. Reliab.* **42**, 189 (2002).

$^{21}$N. Sano, K. Matsuzawa, M. Mukai, and N. Nakayama, Tech. Dig. - Int. Electron. Devices Meet., 275 (2000).

$^{22}$B. K. Ridley, *Quantum Processes in Semiconductors* (Clarendon, Oxford, 1999).

$^{23}$T. N. Morgan, *Phys. Rev.* **139**, A343 (1965).

$^{24}$K. Hess and C. T. Sah, *Surf. Sci.* **47**, 650 (1975).

$^{25}$A. L. Fetter and J. D. Walecka: *Quantum Theory of Many-Particle Systems* (McGraw-Hill, New York, 1971).

$^{26}$J. R. Meyer and F. J. Bartoli, *Phys. Rev. B* **28**, 915 (1983).

$^{27}$A. Pirovano, A. L. Lacaita, G. Ghidini, and G. Tallarida, *IEEE Electron Devices Lett.* **21**, 34 (2000).

$^{28}$A. Pirovano, A. L. Lacaita, G. Zandler, and R. Oberhuber, Tech. Dig. – Int. Electron. Devices Meet., 21.2.1–21.2.4 (1999).

$^{29}$A. Pirovano, A. L. Lacaita, G. Zandler, and R. Oberhuber, *IEEE Trans. Electron. Devices* **47**, 718 (2000).

$^{30}$T. Ishihara, K. Matsuzawa, M. Takayanagi, and S. Takagi, *Jpn. J. Appl. Phys. Part 1* **41**, 2353 (2002).

$^{31}$F. Stern, *Phys. Rev. B* **5**, 4891 (1972).

$^{32}$D. Esseni and A. Abramo, *IEEE Trans. Electron Devices* **50**, 1665 (2003).

$^{33}$F. Gámiz and M. V. Fischetti, *Appl. Phys. Lett.* **83**, 4848 (2003).

$^{34}$J. Koga, S. Takagi, and A. Toriumi, in *Extended Abstract International Conference on Solid State Devices and Materials (SSDN)*, 1994, p. 895.

$^{35}$See http://www.ciss.iis.u-tokyo.ac.jp/english for PHASE, Institute of Industrial Science, University of Tokyo.

$^{36}$K. Kato, D. Matsushita, K. Muraoka, and Y. Nakasaki, *Phys. Rev. B* **78**, 085321 (2008).

$^{37}$M. V. Fischetti, D. A. Neumayer, and E. A. Cartier, *J. Appl. Phys.* **90**, 4587 (2001).

$^{38}$M. V. Fischetti and S. E. Laux, *J. Appl. Phys.* **89**, 1205 (2001).

$^{39}$M. V. Fischetti, *J. Appl. Phys.* **89**, 1232 (2001).

$^{40}$S. Takagi, *VLSI Des.* **8**, 1 (1998).

$^{41}$S. M. Goodnick, D. K. Ferry, and C. W. Wilmsen, *Phys. Rev. B* **32**, 8171 (1985).

$^{42}$D. Hojo, N. Tokuda, and K. Yamabe, *Jpn. J. Appl. Phys. Part 2* **41**, L505 (2002).

$^{43}$D. Hojo, H. Oeda, N. Tokuda, and K. Yamabe, *Jpn. J. Appl. Phys. Part 1* **42**, 1903 (2003).

$^{44}$R. Hasunuma, J. Okamoto, N. Tokuda, and K. Yamabe, *Jpn. J. Appl. Phys. Part 1* **43**, 7861 (2004).

$^{45}$T. H. Ning and C. T. Sah, *Phys. Rev. B* **6**, 4605 (1972).

$^{46}$F. Stern and W. E. Howard, *Phys. Rev.* **163**, 816 (1967).

$^{47}$M. V. Fischetti, *J. Appl. Phys.* **89**, 1205 (2001).

$^{48}$S. Barraud, O. Bonno, and M. Casse, *J. Appl. Phys.* **104**, 073725 (2008).

$^{49}$S. Takagi, J. L. Hoyt, J. J. Welser, and J. F. Gibbons, *J. Appl. Phys.* **80**, 1567 (1996).

$^{50}$C. Jacoboni and L. Raggiani, *Rev. Mod. Phys.* **55**, 645 (1983).

$^{51}$Y. Matsumoto and Y. Uemura, *Jpn. J. Appl. Phys.*, Suppl. **2** Pt. 2, 367 (1974).

$^{52}$F. Gámiz and J. B. Roldán, *J. Appl. Phys.* **94**, 392 (2003).

$^{53}$F. Gámiz, J. A. Lopez-Villanueva, J. A. Jimenez-Tejada, I. Melchor, and A. Palma, *J. Appl. Phys.* **75**, 924 (1994).

$^{54}$M. V. Fischetti and S. Narayanan, *J. Appl. Phys.* **110**, 083713 (2011).

$^{55}$J. R. Meyer and F. J. Bartoli, *Phys. Rev. Lett.* **57**, 2568 (1986).

$^{56}$J. R. Meyer and F. J. Bartoli, *Phys. Rev. B* **36**, 5989 (1987).

$^{57}$D. R. Leadley, M. J. Kearney, A. I. Horrell, H. Fisher, L. Risch, E. H. C. Parker, and T. E. Whall, *Semicond. Sci. Technol.* **17**, 708 (2002).

$^{58}$R. M. Feenstra and M. A. Lutz, *J. Appl. Phys.* **78**, 6091 (1995).
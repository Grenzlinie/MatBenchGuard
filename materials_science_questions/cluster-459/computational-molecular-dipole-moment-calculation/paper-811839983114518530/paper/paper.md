# Atomistic Electrodynamics Model for Optical Properties of Silver Nanoclusters

Lin Lin Jensen and Lasse Jensen*

Department of Chemistry, The Pennsylvania State University, 104 Chemistry Building, Univeristy Park, Pennsylvania 16802-4615

Received: May 27, 2009; Revised Manuscript Received: July 13, 2009

In this work we have presented an atomistic electrodynamics model for describing the optical properies of silver clusters in the size range of 1-5 nm. The model consists of interacting atom-type capacitances and polarizabilities that combined describe the total response of the nanoclusters. A double Lorentzian oscillator is used to describe the frequency-dependent atomic polarizabilities, while a single Lorentzian oscillator is used to describe the frequency-dependent atomic capacitances. All atomic parameters have been optimized using reference data obtained from time-dependent density functional theory (TDDFT) calculations. As a comprehensive test of our model, we have studied the frequency-dependent polarizabilities of quasi-spherical silver nanoclusters having different structural motifs, i.e., icosahedra, truncated Ino and Marks decahedra, and regular truncated octahedra and cubocahedra. We have shown that clusters in all five structural motifs exhibit a strong absorption peak in the spectral region of 2.4-4.8 eV, although the size evolution of absorption peak location and peak width depends strongly on the number of atoms and the atomic arrangements of the clusters.

## Introduction
The optical properties of noble metal nanoparticles have fascinated scientists for a long time, starting with Michael Faraday's investigations of colloidal gold in the middle 1800s.¹ The main feature of these nanoparticles is that they exhibit surface plasmons (collective oscillations of the conduction electrons) that are absent in individual atoms and in the bulk. Excitation of these plasmons leads to a strong absorption band in the UV−visible region, generally referred to as surface plasmon resonance (SPR). The SPR wavelength can be tuned by adjusting the size, shape, and surrounding of the nanoparticle,² and this versatility has been exploited in a wide range of applications in catalysis, optics, chemical and biological sensing, and medical therapeutics.³⁻⁷

Accurate and efficient simulations of optical properties are necessary to rationalize experimental findings and predict/design novel nanostructured materials with specific optical properties. Classical electrodynamics methods, such as Mie theory,⁸ the discrete dipole approximation, (DDA)⁹,¹⁰ and the finite difference time domain (FDTD) method,¹¹ have been widely employed to model nanospheres, nanodisks, nanorods, nanoprisms, and other complex geometrical configurations. These methods have been proven to describe the optical properties of large nanoparticles accurately; however, they suffer two main shortcomings when describing nanoparticles smaller than ∼10 nm. First, these methods solve Maxwell's equations using the frequency-dependent dielectric functions of the bulk metal. The bulk dielectric functions can be empirically modified to account for the enhanced electron-surface scattering in small nanoparticles, and this approach has been shown to improve upon the classical results.⁴,¹² Second, in all of these methods, the nanoparticle is treated as a continuous metal without any discrete atomic structure. This lack of microscopic structural detail makes it particularly problematic to incorporate effects of adsorbed molecules and molecule-plasmon couplings.

On the other hand, time-dependent local density approximation (TDLDA) within a jellium-type model has been shown to be quite reasonable for describing the optical properties of silver and gold nanoparticles below 7 nm.⁴,¹³⁻¹⁵ The TDLDA formalism treats the electron excitation of the system quantum mechanically, while the jellium approach allows inclusion of specific effects such as effect of homogeneous embedding medium. Recently, Nordlander et. al have extended this approach to investigate gold nanoshells and nanoshell dimers.¹⁶⁻¹⁸ However, these jellium-type approaches neglect the structure of the ionic core and are thus most successful when describing spherical nanoparticles. To retain the atomic structure of the nanoparticles, ab initio calculations are ideal and can be performed for nanoparticles smaller than 1 nm. Recently we have used time-dependent density functional theory (TDDFT) to calculate the absorption spectra of Ag_N clusters with N = 2−8 and 20.¹⁹ This TDDFT approach has also been used to simulate excitation spectra of silver tetrahedral clusters with 10−120 atoms²⁰ and charged gold octahedral clusters with 6−146 atoms.²¹ However due to obvious computational constraints, ab initio calculations cannot be carried out for nanoparticles in the intermediate size range.

In this work, we present an atomistic electrodynamics model that can bridge the first-principles modeling and the classical electrodynamics descriptions. The model is an extension of our previously reported capacitance-polarizability interaction model (CPIM) for static polarizabilities of large silver and gold nanoclusters.²² In the CPIM, the nanoparticle is considered as a collection of N interacting atoms that combined describe the total response. Each atom is characterized by an atomic polarizability and an atomic capacitance, and these intrinsic atomic properties are optimized by parametrization against reference data obtained from TDDFT calculations. In our previous work, we have shown that the CPIM is computationally efficient and reported static polarizabilities for silver and gold

* To whom correspondence should be addressed. E-mail: jensen@ chem.psu.edu.

10.1021/jp904956f CCC: $40.75
© 2009 American Chemical Society
Published on Web 07/31/2009

An Atomistic Electrodymanics Model
J. Phys. Chem. C, Vol. 113, No. 34, 2009 15183

nanotubes, nanodisks, and nanospheres with diameters as large as 4.5 nm.²² Here we extend the CPIM to treat the frequency-dependent complex molecular polarizability, and show that the TDDFT results can be well reproduced by describing the response of individual atom using Lorentz oscillators. The frequency-dependent CPIM (FD-CPIM) is atomistic in nature and does not require any input obtained from the bulk metal, thus allowing straightforward coupling between atoms, molecular clusters, and intermediate nanoclusters.

We have applied the FD-CPIM to study the absorption spectra of silver nanoparticles in the size range of 1−5 nm. Experimental and theoretical studies have shown that silver clusters in this size range can present both noncrystalline structures in the form of icosahedra and truncated decahedra and face-centered cubic (fcc) crystalline structures, although the relative proportions of these structures depend on the experimental conditions.²³⁻²⁷ It is therefore essential to investigate the evolution of absorption spectrum with increasing size for silver clusters of different structural motifs. We have considered five different quasi-spherical motifs: icosahedra, truncated Ino and Marks decahedra for multiply twinned noncrystalline structures, and regular truncated octahedra and cuboctahedra for fcc crystalline structures. We will show below how the absorption behavior changes as a function of cluster size for each structural motif. The obtained trends will be compared to predictions from the TDLDA-jellium model as well as experimental results whenever available.³

### Theory

In this section we briefly summarize the theory of the capacitance-polarizability interaction model (CPIM) presented in our previous work²²˒²⁸ and extend it to compute the complex molecular polarizability of structures subject to an external electric field oscillating at a frequency $\omega$. Let $N$ be the number of atoms in the structures considered, where each atom $i$ is characterized by a frequency-dependent capacitance, $c_i(\omega)$, and a frequency-dependent polarizability, $\alpha_{i,\alpha\beta}(\omega)$. Due to the interactions between different atoms, each will have an induced atomic charge, $q_i^{\text{ind}}(\omega)$, and an induced atomic dipole, $\mu_{i,\alpha}^{\text{ind}}(\omega)$, for which the total energy $V$ can be written as

$$
\begin{aligned}
V = \frac{1}{2} \sum_{i}^{N} \frac{q_{i}^{\text{ind}}(\omega) q_{i}^{\text{ind}}(\omega)}{c_{i}(\omega)} + \frac{1}{2} \sum_{i}^{N} \sum_{j \neq i}^{N} q_{i}^{\text{ind}}(\omega) T_{i j}^{(0)} q_{j}^{\text{ind}}(\omega) - \\
\sum_{i}^{N} \sum_{j \neq i}^{N} \mu_{i, \alpha}^{\text{ind}}(\omega) T_{i j, \alpha}^{(1)} q_{j}^{\text{ind}}(\omega) + \frac{1}{2} \sum_{i}^{N} \mu_{i, \alpha}^{\text{ind}}(\omega) \alpha_{i, \alpha \beta}^{-1}(\omega) \mu_{i, \beta}^{\text{ind}}(\omega) - \\
\frac{1}{2} \sum_{i}^{N} \sum_{j \neq i}^{N} \mu_{i, \alpha}^{\text{ind}}(\omega) T_{i j, \alpha \beta}^{(2)} \mu_{j, \beta}^{\text{ind}}(\omega) + \sum_{i}^{N} q_{i}^{\text{ind}}(\omega) \varphi_{i}^{\text{ext}}(\omega) - \\
\sum_{i}^{N} E_{\alpha}^{\text{ext}}(\omega) \mu_{i, \alpha}^{\text{ind}}(\omega) - \lambda(q^{\text{cluster}} - \sum_{i}^{N} q_{i}^{\text{ind}}(\omega)) \quad (1)
\end{aligned}
$$

where the first two terms are the energies associated with the atomic charges only, the third term is the interaction between the atomic charges and atomic dipoles, and the fourth and fifth terms are the energy of the induced atomic dipoles. The sixth term is the interaction between the atomic charges and an external potential $\varphi_i^{\text{ext}}(\omega)$, and the seventh term is the interaction between the atomic dipoles and an external electric field $E_{\alpha}^{\text{ext}}(\omega)$. The last term ensures that the charge of the cluster, $q^{\text{cluster}}$, is retained, and $\lambda$ is a regular Lagrange multiplier. Here $T_{ij}^{(0)}$, $T_{ij,\alpha}^{(1)}$, and $T_{ij,\alpha\beta}^{(2)}$ are the so-called interaction tensors $T_{ij,\alpha_1,\alpha_2,...,\alpha_n}^{(n)}$ of rank $n$, describing the relative distance and orientation of the atoms. To ensure that there is no "polarizability catastrophy",²⁹ i.e., that the equations diverge as the distance tends to zero, we adopted the renormalized interaction tensors proposed by Mayer³⁰ which is an extension of an earlier model by Jensen et al.³¹ In this model the dipoles and charges are considered as having a Gaussian charge distribution rather than being point object.

To describe the interactions with an oscillating external electric field, the induced atomic dipoles and atomic charges are usually described using a simple Lorentzian frequency-dependence of both the atomic polarizability and atomic capacitance.³²˒³³ Although, a recent study related the frequency-dependence to the current flowing through the bonds.³⁴˒³⁵ This approach is reasonable if the dielectric functions of the materials can be qualitatively described by a simple Drude model or one Lorentz-oscillator model. However, it is well-known that the dielectric constants of bulk silver metal have components contributed by both free electrons and bound electrons, which are typically described using several oscillators.³⁶ The polarizability per atom can be obtained from the bulk dielectrics using the Clausius-Mossotti equation³⁷

$$
\alpha \propto \frac{\varepsilon - 1}{\varepsilon + 2} \tag{2}
$$

where $\varepsilon$ is the bulk dielectric constants of silver. In the UV−vis regions, the polarizability obtained in this way can be reproduced using two Lorentzian oscillators. This is illustrated in Figure 1, where we plot the bulk dielectric constants and the polarizabilities per atom obtained using the Clausius−Mossotti equation and the fit of two oscillators.

Thus, we base our model on two Lorentzian oscillators to describe the frequency-dependence of the atomic polarizability $\alpha_{i,\alpha\beta}(\omega)$. However, we found that a single Lorentzian oscillator worked the best to describe the frequency-dependence of the atomic capacitance $c_i(\omega)$. In this way the frequency-dependent polarizability $\alpha_{i,\alpha\beta}(\omega)$ and frequency-dependent capacitance $c_i(\omega)$ are given by

$$
\begin{aligned}
\alpha_{i, \alpha \beta}(\omega=0) &=\alpha_{i, s, \alpha \beta} ; \\
\alpha_{i, \alpha \beta}(\omega>0) &=\alpha_{i, s, \alpha \beta}\left(\frac{\omega_{i, 1}^{2}}{\omega_{i, 1}^{2}-\omega^{2}-i \gamma_{i, 1} \omega}+\right. \\
&\left.\frac{\omega_{i, 2}(N)^{2}}{\omega_{i, 2}(N)^{2}-\omega^{2}-i \gamma_{i, 1} \omega}\right)
\end{aligned} \tag{3}
$$

and

$$
c_{i}(\omega=0)=c_{i, s} ; \quad c_{i}(\omega>0)=c_{i, s}\left(\frac{\omega_{i, 1}^{2}}{\omega_{i, 1}^{2}-\omega^{2}-i \gamma_{i, 1} \omega}\right) \tag{4}
$$

where $\alpha_{i,s,\alpha\beta}$ is the static atomic polarizability and $c_{i,s}$ is the static atomic capacitance. The parameters $\omega_{i,1}$ and $\omega_{i,2}$ are the oscillator resonance frequencies and $\gamma_{i,1}$ and $\gamma_{i,2}$ the oscillator widths for the first and second oscillators, respectively. The "overall" resonance frequency for the second oscillator, $\omega_{i,2}(N)$, is assumed to be size dependent as

$$
\omega_{i,2}(N) = \omega_{i,2}(1 + A/N^{1/3})
\tag{5}
$$

with $A$ being the size correction parameter. This size correction is included to ensure that the absorption maximum red shifts as the cluster size increases for small clusters $(N < 71)$, as demonstrated by both experimental results$^{38}$ and our TDDFT results. Several other models for both $\alpha_{i,\alpha\beta}(\omega)$ and $c_i(\omega)$ were also explored, and the proposed expressions were found to provide the best agreement between FD-CPIM and TDDFT results.

According to classical response theory, the molecular polarizability can be determined by minimizing the total energy $V$ with respect to the induced atomic charges $q_i^{\text{ind}}(\omega)$, the induced atomic dipoles $\mu_{i,\alpha}^{\text{ind}}(\omega)$, as well as the Langrange multiplier $\lambda$. The resulting $4N + 1$ set of complex linear equations can be recast into matrix form as

$$
\begin{pmatrix}
E^{\text{ext}}(\omega) \\
\varphi^{\text{ext}}(\omega) \\
q^{\text{cluster}}
\end{pmatrix}
=
\begin{pmatrix}
A & -M & 0 \\
-M^T & -C & 1 \\
0 & 1 & 0
\end{pmatrix}
\begin{pmatrix}
\mu^{\text{ind}}(\omega) \\
q^{\text{ind}}(\omega) \\
\lambda
\end{pmatrix}
\tag{6}
$$

where the matrix elements are defined as

$$
A_{ii,\alpha\beta} = \alpha_{i,\alpha\beta}(\omega)^{-1}; \quad A_{ij,\alpha\beta} = -T_{ij,\alpha\beta}^{(2)} \quad (i \neq j)
\tag{7}
$$

$$
M_{ii,\alpha} = 0; \quad M_{ij,\alpha} = T_{ij,\alpha}^{(1)} \quad (i \neq j)
\tag{8}
$$

and

$$
C_{ii} = c_i(\omega)^{-1}; \quad C_{ij} = T_{ij}^{(0)} \quad (i \neq j)
\tag{9}
$$

By inverting the $(4N + 1) \times (4N + 1)$ relay matrix we can solve for the induced charges and dipole moments as

$$
\begin{aligned}
\begin{pmatrix}
\mu^{\text{ind}}(\omega) \\
q^{\text{ind}}(\omega) \\
\lambda
\end{pmatrix}
&=
\begin{pmatrix}
A & -M & 0 \\
-M^T & -C & 1 \\
0 & 1 & 0
\end{pmatrix}^{-1}
\begin{pmatrix}
E^{\text{ext}}(\omega) \\
\varphi^{\text{ext}}(\omega) \\
q^{\text{cluster}}
\end{pmatrix} \\
&=
\begin{pmatrix}
B & g & h_1 \\
g^T & D & h_2 \\
h_1^T & h_2^T & h_3
\end{pmatrix}
\begin{pmatrix}
E^{\text{ext}} \\
\varphi^{\text{ext}} \\
q^{\text{cluster}}
\end{pmatrix}
\end{aligned}
\tag{10}
$$

The complex molecular polarizability can then be written in terms of the inverted relay matrix

$$
\alpha_{\alpha\beta}^{\text{mol}}(\omega) = \sum_{i,j}^N \big(B_{ij,\alpha\beta}(\omega) - \mathbf{r}_{i,\alpha}D_{ij}(\omega)\mathbf{r}_{j,\beta}\big)
\tag{11}
$$

where the first term is contributions from the dipole-dipole interactions and the second term is the charge-transfer (CT) contributions. As we have shown previously, the static molecular polarizability, $\alpha_{\alpha\beta}^{\text{mol}}(\omega=0)$, only depends on the atomic positions $\mathbf{r}_i$ and two intrinsic atomic properties: the static atomic capacitance $c_{i,s}$ and the static atomic polarizabilities $\alpha_{i,s}$, since they determine entirely the matrices $B$ and $D$. The static molecular polarizability can be calculated efficiently by using the optimized static atomic capacitance and polarizability, and very good agreement between the CPIM and the TDDFT results can be achieved both for the isotropic and anisotropic polarizability of silver and gold clusters as a function of size.

In this work we are mainly interested in understanding how the absorption spectra of small metal nanoparticles evolve with size. The absorption cross section $\sigma(\omega)$ can be directly related to the imaginary polarizability as

$$
\sigma(\omega) = \frac{4\pi\omega}{c}Im[\bar{\alpha}(\omega)] = \frac{4\pi\omega}{c}Im\left[\frac{1}{3}\big(\alpha_{xx}^{\text{mol}} + \alpha_{yy}^{\text{mol}} + \alpha_{zz}^{\text{mol}}\big)\right]
\tag{12}
$$

where $\bar{\alpha}(\omega)$ is the isotropic polarizability of the nanocluster and $c$ the velocity of light. To describe the frequency-dependent molecular polarizability, $\alpha_{\alpha\beta}^{\text{mol}}(\omega > 0)$, five additional atomic parameters are needed: the oscillator resonance frequencies $\omega_{i,1}$ and $\omega_{i,2}$, the oscillator widths $\gamma_{i,1}$ and $\gamma_{i,2}$, and the size correction parameter $A$.

### Parameterization of the FD-CPIM

The reference data used for parametrization of the FD-CPIM consists of the frequency-dependent complex polarizabilities of $\text{Ag}_{58}$ and $\text{Ag}_{68}$ clusters. The geometries of these silver clusters were optimized using the Becke-Perdew (BP86) XC-potential and a triple-$\zeta$ polarized Slater type (TZP) basis set from the $\text{ADF}^{39}$ basis set library.$^{40,41}$ The 1s-3d core was kept frozen for Ag atoms and scalar relativistic effects were accounted for by means of the zeroth-order regular approximation (ZORA).$^{42}$ The structures of the Ag metal clusters were optimized using initial structures taken from the work of Doye and Wales,$^{43}$ and were reported in our previous work.$^{22}$ Frequency dependent polarizabilities were calculated for 20 incident wavelengths in the region between 2.5 and 4.5 eV, and the finite lifetime was included phenomenologically by a common damping parameter $\Gamma = 0.0037$ au $(\sim800$ cm$^{-1})$. All polarizability calculations were carried out using the Adiabatic Local Density Approximation (ALDA) within the AORESPONSE module$^{44}$ of the ADF program package.$^{45,46}$

The optimized parameters of our FD-CPIM were obtained by minimizing the difference between the TDDFT molecular polarizability tensor and the model molecular polarizability tensor for both $\text{Ag}_{58}$ and $\text{Ag}_{68}$ clusters. The static atomic parameters $(\alpha_s$ and $c_s)$ were fixed to the previously reported values$^{22}$ for silver clusters, i.e., $\alpha_s = 49.9843$ au and $c_s = 3.4502$ au The parameters describing the frequency-dependence of the atomic polarizability and atomic capacitance were optimized by minimizing

$$
\text{rms} = \sqrt{\frac{\sum_{j=1}^{N_{\text{mol}}}\left(\frac{\sum_{k=1}^{N_{\text{req}}}\sum_{\alpha,\beta=1}^3 Im(\alpha_{\alpha,\beta,j,k}^{\text{FD-CPIM}} - \alpha_{\alpha,\beta,j,k}^{\text{TDDFT}})^2}{N_{\text{freq}} - 1}\right)}{N_{\text{mol}} - 1}}
\tag{13}
$$

i.e., we parametrized the frequency dependence only for the difference between the imaginary parts of the molecular polarizability tensors, as our objective is to simulate the absorption spectra of the nanoclusters. The optimized values for these parameters are $\omega_{i,1} = 0.0747$ au, $\omega_{i,2} = 0.0545$ au, $\gamma_{i,1} = 0.0604$ au, $\gamma_{i,2} = 0.0261$ au, and $A = 2.7759$ au. Note

![](./images/811839983114518530_1.jpg)

(a) Dielectric Constants

![](./images/811839983114518530_2.jpg)

(b) Polarizability

Figure 1. Comparison between bulk polarizabilities of silver calculated using Clausius-Mossotti equation (curves) and fitted with two-lorentzoscillators model (▲). Black, real part of bulk polarizabilities, and red, imaginary part of bulk polarizabilities.

![](./images/811839983114518530_3.jpg)

(a) Imaginary

![](./images/811839983114518530_4.jpg)

(b) Real

Figure 2. Comparison between calculated imaginary (a) and real (b) parts of the isotropic polarizabilities, $\bar{\alpha}(\omega)$, of $Ag_{58}$ and $Ag_{68}$ clusters. (□) represent the TDDFT results for the $Ag_{58}$ cluster, (■) represent the FD-CPIM results for the $Ag_{58}$ cluster, $(\triangle)$ represent the TDDFT results for the Ag68 cluster, and (▲) represent the FD-CPIM results for the $Ag_{68}$ cluster.

that due to the size correction small clusters $(N<420)$ have higher "overall" resonance frequency for the second oscillator as compared to that for the first oscillator, whereas larger clusters $(N>1680)$ have much lower (10% or more) "overall" resonance frequency for the second oscillator as compared to that for the first oscillator.

In Figure 2 we show a comparison between TDDFT and FD- CPIM for the imaginary and real parts of the isotropic polarizabilities, $\bar{\alpha}(\omega)$, as a function of incident frequency. The FD-CPIM results were calculated using the optimized param- eters. We see that the FD-CPIM calculations reproduce the TDDFT results reasonably well for both imaginary and real parts of the isotropic polarizabilities. From Figure 2a we see that the $Ag_{58}$ cluster has a dominant absorption peak at around $3.4 eV$ , whereas the $Ag_{68}$ cluster has an absorption maximum at around3.3 eV. This absorption peak is a microscopic analog of the localized surface plasmon resonances found in bigger clusters. We expect that this peak gradually evolves into the plasmon peak as the size of the metal cluster increases. Also we observe that there is a shoulder to the blue of the plasmon peak for both clusters, i.e., around $4.2 eV$ for the $Ag_{58}$ cluster and $3.9 eV$ for the $Ag_{68}$ cluster. For these clusters we find a slight red shift(~0.1 eV) in plasmon frequency as the cluster size increases. This is in good agreement with the experimental results by Liebsh et al. where they found that plasmon frequency red-shifted going from $3.80 \pm 0.05 eV$ for $Ag_{50 \pm 3}^{+}$ clusters to 3.77 $\pm 0.03 eV$ for $Ag_{70 \pm 5}^{+}$ clusters. $^{38}$ However, the results presented here have lower plasmon energy and broader plasmon width when compared to the experimental results. This is likely due to that we are studying neutral clusters since removing charge from nanoparticles leads to a shift in plasmon frequency to higher energies. $^{47}$ However, deficiencies in the xc-functional cannot be ruled out.

## Results

To understand the size and shape evolution of the plasmon peak for silver nanoparticles smaller than $5 ~nm$ we carried out FD-CPIM calculations for a series of silver clusters withicosahedral (Ih), truncated Ino ( $i$ -Dh) and Marks ( $m$ -Dh) decahedral, truncated octahedral (TO) and cuboctahedral (c- TO) structural motifs. All structures were constructed with bond length of $R_{Ag-Ag}=2.889 \AA$ taken from bulk silver. The effective diameter of the silver clusters ranges from $\sim 1.0$ to $\sim 5.0 ~nm$ . The optimized parameters were used to calculate the complex molecular polarizabilities in the $2.4-4.8 eV$ spectral region, and the absorption spectra of the nanoclusters are described by the normalized absorption cross section, i.e., $\sigma(\omega) / N$ . Overall, clusters in all five structural motifs exhibit a strong absorption peak in the studied spectral region, although the calculated plasmon frequency and width depend strongly on the number of atoms and atomic arrangements of the clusters. In the following, we present results for the silver icosahedral clusters first as they have the most spherical structures, then results for the truncated decahedral clusters, and finally results for the truncated octahedral clusters.

Icosahedral Nanoclusters. Icosahedra are structured in concentric shells and have a quasispherical shape obtained by packing together 20 distorted tetrahedra sharing a common vertex. The magic number for an icosahedron with $k$ shells is N = 10/3k3 +5k2 + 11/3k + 1, and here we considered silver icosahedral clusters with $k$ ranging from 4 to $11.^{48}$ Figure 3 illustrates the side and top views of the smallest $(Ag_{147})$ and largest $(Ag_{3871})$ icosahedral clusters considered in this work.

In Figure 4 we plot the plasmon frequency and plasmon width(full width at half-maximum) for the series of silver icosahedralclusters. We see that the plasmon frequency red shifts from 3.97

![](./images/811839983114518530_5.jpg)
![](./images/811839983114518530_6.jpg)
![](./images/811839983114518530_7.jpg)
![](./images/811839983114518530_8.jpg)

(a) Ag₁₄₇ Ih
(b) Ag₁₄₇ Ih
(c) Ag₃₈₇₁ Ih
(d) Ag₃₈₇₁ Ih

Figure 3. Side (a and c) and top (b and d) views of silver icosahedral clusters: a 4-shell Ag₁₄₇ icosahedral cluster (a and b); a 11-shell Ag₃₈₇₁ icosahedral cluster (c and d).

![](./images/811839983114518530_9.jpg)
![](./images/811839983114518530_10.jpg)

(a) Plasmon Frequency
(b) Plasmon Width

Figure 4. Size evolutions of the plasmon frequency (a) and plasmon width (b) for a series of silver icosahedral clusters.

![](./images/811839983114518530_11.jpg)
![](./images/811839983114518530_12.jpg)

(a) With CT
(b) Without CT

Figure 5. Normalized absorption cross sections, $\sigma(\omega)/N$, as a function of the incident frequency for a series of icosahedral clusters: with CT contributions (a) and without CT contributions (b). In both subfigures from top to bottom: results for (□) Ag₁₄₇, (■) Ag₃₀₉, (○) Ag₅₆₁, (●) Ag₉₂₃, (△) Ag₁₄₁₅, (▲) Ag₂₀₅₇, (∇) Ag₂₈₆₉, and (▼) Ag₃₈₇₁ icosahedral clusters.

eV for the Ag₁₄₇ cluster and converges at 3.77 eV for the Ag₃₈₇₁ cluster. Also, we see that the plasmon width narrows first from 1.53 eV for the Ag₁₄₇ cluster to 1.26 eV for the Ag₅₆₁ cluster, broadens to 1.51 eV for the Ag₁₄₁₅ cluster, then gradually narrows to 1.44 eV for the Ag₃₈₇₁ cluster. We thus see that there is a strong size-dependence for clusters smaller than ~1500 atoms.

In Figure 5a we plot the normalized absorption cross sections, $\sigma(\omega)/N$, as a function of the incident frequency. For comparison, we present in Figure 5b the calculated $\sigma(\omega)/N$ spectra from only the dipole−dipole interactions. We observe some similar trends from both sets of spectra, although the overall spectral profiles are quite different. First, we see that there is a strong absorption peak for all clusters in the 2.4−4.8 eV spectral region, with the plasmon frequency being ~3.7 eV according to the overall $\sigma(\omega)/N$ spectra while ~4.2 eV according to the $\sigma(\omega)/N$ spectra with only dipole−dipole contributions. Second, we see that the plasmon frequency gradually red shift and converges for large clusters. Last, we see that the peak intensity per atom decreases as cluster size increases, with the sharpest decrease occurs from the Ag₁₄₇ cluster to the Ag₉₂₃ cluster. The similar trends between the two sets of spectra show that the dipole−dipole contributions remain dominant for all cluster sizes, and the observed difference in the plasmon frequency as well as peak intensities can be attributed to the changes in the CT contributions.

Silver Truncated Decahedral Nanoclusters. Similar to the icosahedra, decahedral structures belong to the class of multiply twinned particles. Regular decahedra have a single 5-fold axis, however, they are less spherical than icosahedra. Truncated decahedra have shapes closer to a sphere, and they are characterized by three indices (m,n,p), where m and n are the numbers of atoms on the sides of the (100) facets that are perpendicular and parallel to the 5-fold axis. The depth of the Marks reentrance is denoted as p, where p = 1 corresponds to no reentrance, i.e., the Ino decahedra.⁴⁹ Two decahedra belong to the same “family” if they have the same values of m - n, which measures the squareness of the (100) facets.⁵⁰ We only studied the “family two” Ino decahedra (i-Dh) with m - n = 2 and “family two” Marks decahedra (m-Dh) with m = n and p = 2. The total number of atoms in an i-Dh or a m-Dh is given by $N = 1/6[\{30p^3 - 135p^2 + 207p - 102\} + [5m^3 + (30p - 45)m^2 + (60(p^2 - 3p) + 136)m] + n[15m^2 + (60p - 75)m + 3(10p^2 - 30p) + 66]] - 1$. Figure 6 illustrates the side views of (4,2,1) Ag₈₅ (the smallest i-Dh), (11,9,1) Ag₃₃₁₉ (the largest

![](./images/811839983114518530_13.jpg)
![](./images/811839983114518530_14.jpg)
![](./images/811839983114518530_15.jpg)
![](./images/811839983114518530_16.jpg)

(a) $\text{Ag}_{85}$ $i$-Dh
(b) $\text{Ag}_{3319}$ $i$-Dh
(c) $\text{Ag}_{75}$ $m$-Dh
(d) $\text{Ag}_{3274}$ $m$-Dh

Figure 6. Side views of silver truncated decahedral clusters. From left to right: (4,2,1) $\text{Ag}_{85}$ and (11,9,1) $\text{Ag}_{3319}$ $i$-Dh clusters and (3,3,2) $\text{Ag}_{75}$ and (9,9,2) $\text{Ag}_{3274}$ $m$-Dh clusters.

![](./images/811839983114518530_17.jpg)

(a) $i$-Dh

![](./images/811839983114518530_18.jpg)

(b) $m$-Dh

![](./images/811839983114518530_19.jpg)

(c) Plasmon Frequency

![](./images/811839983114518530_20.jpg)

(d) Plasmon Width

Figure 7. Normalized absorption cross sections, $\sigma(\omega)/N$, as a function of the incident frequency for series of silver $i$-Dh (a) and $m$-Dh (b) clusters. In subfigure (a) from top to bottom: results for ($\square$) $\text{Ag}_{85}$, ($\blacksquare$) $\text{Ag}_{207}$, ($\bigcirc$) $\text{Ag}_{409}$, ($\bullet$) $\text{Ag}_{711}$, ($\bigtriangleup$) $\text{Ag}_{1133}$, ($\blacktriangle$) $\text{Ag}_{1695}$, ($\nabla$) $\text{Ag}_{2417}$, and ($\blacktriangledown$) $\text{Ag}_{3319}$ $i$-Dh clusters; In subfigure (b) from top to bottom: results for ($\square$) $\text{Ag}_{75}$, ($\blacksquare$) $\text{Ag}_{192}$, ($\bigcirc$) $\text{Ag}_{389}$, ($\bullet$) $\text{Ag}_{686}$, ($\bigtriangleup$) $\text{Ag}_{1103}$, ($\blacktriangle$) $\text{Ag}_{1660}$, ($\nabla$) $\text{Ag}_{2377}$, and ($\blacktriangledown$) $\text{Ag}_{3274}$ $m$-Dh clusters. Also shown: size evolutions of the plasmon frequency (c) and plasmon width (d) for series of silver $i$-Dh ($\square$) and $m$-Dh ($\blacksquare$) clusters. Results for Ih clusters ($\bullet$) are shown for comparison.

$i$-Dh), (3,3,2) $\text{Ag}_{75}$ (the smallest $m$-Dh), and (9,9,2) $\text{Ag}_{3274}$ (the largest $m$-Dh) clusters considered in this work.

Figure 7 plots the normalized absorption cross sections, $\sigma(\omega)/$ $N$, as a function of the incident frequency, as well as the size evolutions of the plasmon frequency and plasmon width for series of silver truncated decahedral clusters. Similar to the absorption spectra of icosahedral clusters (Figure 5a), we see that all truncated decahedral clusters exhibit a strong absorption peak in the 2.4−4.8 eV spectral region. For both the $i$-Dh ($\square$) and $m$-Dh ($\blacksquare$) clusters, we see that except in the small size range ($N < 500$), a steady red shifts in the plasmon frequency and narrowing in the plasmon width are observed for the size evolution over the entire size domain. Moreover, the $i$-Dh clusters are found to have consistently lower plasmon frequencies and broader plasmon widths as compared to those of the $m$-Dh clusters. These size-dependences for the truncated decahedral clusters are larger than what we found for the silver icosahedral clusters over similar size range, demonstrating that the atomic arrangement of the nanoclusters plays a predominant role in determining the size evolution of the plasmon resonance. It is also clear from Figure 7c,d that the plasmon frequency and width for the truncated decahedral clusters converge much slower with size.

Silver Truncated Octahedral Nanoclusters. A truncated octahedron is obtained by symmetrically removing the six corners of a complete octahedron, resulting in a more spherical like shape. It is characterized by two indices $(n_{l,}n_{cut})$, where $n_{l}$ is the length of the edge of the complete octahedron, and $n_{cut}$ the number of layers cut at each corner, and has a total number of atoms $N = 1/3(2n_{l}^{3}+n_{l})-2n_{cut}^{3}-3n_{cut}^{2}-n_{cut}$. Regular truncated octahedra (TO) can be obtained if $n_{l}=3n_{cut}+1$, and they have square and hexagonal facets. Cuboctahedra ($c$-TO) are possible if $n_{l}=2n_{cut}+1$, obtaining square and triangular facets. $^{24,50}$ Note that the cuboctahedra and icosahedra sequences contain clusters with the same numbers of atoms and these clusters can convert to each other through twinning transformation. $^{50}$ Figure 8 illustrates the side views of (7,2) $\text{Ag}_{201}$ (the smallest TO), (19,6) $\text{Ag}_{4033}$ (the largest TO), (7,3) $\text{Ag}_{147}$ (the smallest $c$-TO), and (21,10) $\text{Ag}_{3871}$ (the largest $c$-TO) clusters considered in this work.

Figure 9 plots the normalized absorption cross sections, $\sigma(\omega)/$ $N$, as a function of the incident frequency, as well as the size

![](./images/811839983114518530_21.jpg)
![](./images/811839983114518530_22.jpg)
![](./images/811839983114518530_23.jpg)
![](./images/811839983114518530_24.jpg)

(a) Ag₂₀₁ TO
(b) Ag₄₀₃₃ TO
(c) Ag₁₄₇ c-TO
(d) Ag₃₈₇₁ c-TO

Figure 8. Side views of silver truncated octahedral clusters: From left to right: (7,2) Ag₂₀₁ and (19,6) Ag₄₀₃₃ TO clusters and (7,3) Ag₁₄₇ and (21,10) Ag₃₈₇₁ c-TO clusters.

![](./images/811839983114518530_25.jpg)
![](./images/811839983114518530_26.jpg)

(a) TO
(b) c-TO

![](./images/811839983114518530_27.jpg)
![](./images/811839983114518530_28.jpg)

(c) Plasmon Frequency
(d) Plasmon Width

Figure 9. Normalized absorption cross sections, $\sigma(\omega)/N$, as a function of the incident frequency for series of silver TO (a) and $c$-TO (b) clusters. In subfigures (a) from top to bottom: results for ($\bullet$) Ag₂₀₁, ($\triangle$) Ag₅₈₆, ($\Delta$) Ag₁₂₈₉, ($\nabla$) Ag₂₄₀₆, and ($\blacktriangledown$) Ag₄₀₃₃ TO clusters. In subfigure (b) from top to bottom: results for ($\square$) Ag₁₄₇, ($\blacksquare$) Ag₃₀₉, ($\bigcirc$) Ag₅₆₁, ($\bullet$) Ag₉₂₃, ($\triangle$) Ag₁₄₁₅, ($\Delta$) Ag₂₀₅₇, ($\nabla$) Ag₂₈₆₉, and ($\blacktriangledown$) Ag₃₈₇₁ $c$-TO clusters. Also shown: size evolutions of the plasmon frequency (c) and plasmon width (d) for series of silver TO ($\blacktriangledown$) and $c$-TO ($\Delta$) clusters. Results for Ih clusters ($\bullet$) are shown for comparison.

evolutions of the plasmon frequency and plasmon width for series of silver truncated octahedral clusters. We see that similar to the absorption spectra of the icosahedral (Figure 5a) and truncated decahedral (Figure 7a,b) clusters, there is a strong absorption peak in the 2.4−4.8 eV spectral region for all truncated octahedral clusters. We note first that clusters in the cuboctahedral and icosahedral series, although having the same sequence of atoms, exhibit different size-dependences of the plasmon frequency and plasmon width. This again demonstrates the profound influence of the atomic arrangement on the plasmon behaviors of the nanoclusters. For the $c$-TO ($\Delta$) clusters, we see that the plasmon frequency starts at 4.15 eV and converges to around 3.71 eV. In contrast, regular truncated octahedral clusters ($\blacktriangledown$) start at 3.55 eV and end at 3.79 eV slightly higher in energy than the Ih clusters. For both clusters we see that the width initially narrows and then broadens ending up around 1.62 eV for the $c$-TO clusters and 1.52 eV for the TO clusters, both broader than the icosahedral clusters.

### Discussion

It has been well demonstrated that the shape and size of a silver nanoparticle play very important roles in determining the number, positions, and intensities of its surface plasmon resonances.² At small sizes, theoretical studies have shown that icosahedra, truncated decahedra, truncated octahedra are ther- modynamically favored structural motifs for silver clusters. Simulations have predicted that silver clusters follow the general trend with the icosahedral motif the most favored at small sizes ($N < 300$), truncated decahedral clusters favored in the intermediate range ($300 < N < 20\ 000$), while truncated octahedral clusters expected for large sizes.⁴⁹ Experimentally though, the observed structures of silver clusters depend on both thermodynamical and kinetic factors, although Marks decahedral clusters are found to be typically predominate under most reaction conditions.²⁶

Experimentally, both redshift and blueshift in the plasmon frequency with decreasing size have been observed for particles with diameter smaller than 10 nm. Kreibig⁵¹ et al. reported that for silver embedded in glass matrix, the plasmon frequency remains constant for particles between 5.5 and 11.0 nm, but shifts to higher energy as diameter decreases from 5.5 to 2.2 nm. Broyer¹³ et al. reported that as diameter decreases from 6.7 to 1.5 nm, the surface plasmon resonance slightly blueshifted for silver nanoparticles embedded in alumina maxtrix. They also reported TDLDA simulations within the jellium model, which confirmed the observed trend. Anantharaman et al.⁵² observed

redshift and broadening of the plasmon resonance with decreasing nanoparticle size for $Ag-SiO_2$ composite in the size range of 5−10 nm.

We find for the quasi-spherical structures studied in this work that the plasmon peak in general blue shifts as the size of the particle decreases. When the size of the nanoparticles becomes small than 500 atoms we see a significant variation in the size-dependences among the different structures. This is expected due to the onset of quantum size effects which become increasingly important as the size of the particles becomes smaller. In our model this is accounted for by a size-dependent Lorentzian oscillator and that the interactions between dipoles and charges are damped at short distances. As the particle size reached around 5 nm, the largest particles studied, we see that the plasmon peaks for the different nanoparticles show only small size effects, although the peak position does depend on the geometry. Thus, these results are in good agreement with the experimental results of Kreibig and Broyer. However, the observed trend is in contrast to DDA results for spheres with the same effective radius as the icosahedral clusters, where the plasmon frequency is found to stay more or less constant while the plasmon width broadens as cluster size increases. Classically when the real part of the bulk dielectric constants of silver equals to −2, the Mie resonance wavelength is obtained at 3.5 eV, so we see that our model produces higher plasmon frequency, 3.8 eV for the isocahedra clusters, as compared to the classical Mie frequency for large clusters. Although size corrections to the dielectric constant are important for particles of the size considered here they only affect the plasmon peak width, but not the plasmon frequency. $^{4,12}$ This discrepancy is most likely a result of fitting our parameters to TDDFT results for small clusters. However, our results highlight the importance of size and shape in the small nanoparticle regime where traditional electrodynamic simulations fail.

In order to compare further with DDA simulations, we calculated the plasmon wavelength for small silver icosahedral and cuboctahedral clusters of a 4.4 nm diameter. Gonzalez et. $al^{53}$ have recently shown that DDA simulations for these nanoparticles immersed in DMSA give plasmon peaks at 2.99 and 2.92 eV, respectively, in good agreement with experimental results of 2.95 eV for similar sized particles. Using DDA, we find that the resonance plasmon frequencies are located at 3.45 and 3.42 eV for the icosahedral and cuboctahedral clusters of 4.4 nm diameter in vacuum, respectively. The largest icosahedral and cubocahedral clusters considered here have effective diameters of $\sim$4.8 nm, and our FD-CPIM plasmon frequencies are at 3.77 and 3.71 eV, respectively. We note that both our FD-CPIM and DDA calculations suggest that for icosahedral and cuboctahedral clusters with the same number of atoms, the former has higher plasmon frequency as compared to the later. Again, we see that our results are about 0.3 eV too high in energy as compared with DDA simulations due to the way our model is parametrized.

## Conclusions
We have presented an atomistic electrodynamics model for describing the optical properies of silver clusters. This model is an extension of a capacitance-polarizability interaction model previously reported. A double Lorentzian oscillator is used to describe the frequency-dependent atomic polarizabilities, while a single Lorentzian oscillator is used to describe the frequency-dependent atomic capacitances. All atomic parameters have been optimized using TDDFT reference data. To achieve good agreement between the model and TDDFT results for the full polarizability tensor of medium sized $(N=58,68)$ silver clusters it was found necessary to include size-dependence in the Lorentzian oscillator. This accounts for the quantum size effects which are important for small clusters. As a comprehensive test of our model, we have studied the absorption spectra of quasi-spherical silver nanoclusters having different structural motifs, i.e. icosahedra, truncated Ino and Marks decahedra, and regular truncated octahedra and cubocahedra. We have shown that clusters in all five structural motifs exhibit a strong absorption peak in the spectral region of 2.4−4.8 eV, although the size evolution of the absorption peak location and peak width depends strongly on the number of atoms and the atomic arrangement of the clusters. We find in general that the plasmon frequency blue shifts as the size of the particle decreases and is more or less converged for particles around 5 nm, which is in good agreement with experimental findings. However, we find that the plasmon frequency for icosahedral particles converges to around 3.8 eV which is somewhat higher than the 3.5 eV expected from classical Mie theory. This is likely a result of parametrizing the model to a data set of small clusters.

Acknowledgment. L.J. acknowledges start-up funds from the Pennsylvania State University, and support received from Research Computing and Cyberinfrastructure, a unit of Information Technology Services at Penn State.

## References and Notes
(1) Faraday, M. *Philos. Trans. R. Soc. London* **1857**, 147, 145−181.
(2) Kelly, K. L.; Coronado, E. A.; Zhao, L. L.; Schatz, G. C. *J. Phys. Chem. B* **2003**, 107, 668−677.
(3) Halperin, W. P. *Rev. Mod. Phys.* **1986**, 58, 533.
(4) Link, S.; El-Sayed, M. A. *Annu. Rev. Phys. Chem.* **2003**, 54, 331−366.
(5) Kalsin, A.; Fialkowski, M.; Paszewski, M.; Smoukov, S. K.; Bishop, K. J. M.; Grzybowski, B. A. *Science* **2006**, 312, 420−424.
(6) Stuart, D. A.; Yuen, J. M.; Shah, N.; Lyandres, O.; Yonzon, C. R.; Glucksberg, M. R.; Walsh, J. T.; Duyne, P. V. *Anal. Chem.* **2006**, 78, 7211−7215.
(7) Huang, X.; El-Sayed, I. H.; Qian, W.; El-Sayed, M. A. *J. Am. Chem. Soc.* **2006**, 128, 2115−2120.
(8) Mie, G. *Ann. Phys. (Leipzig)* **1908**, 25, 377−445.
(9) Yang, W.-H.; Schatz, G. C.; Van Duyne, R. P. *J. Chem. Phys.* **1995**, 103, 869−875.
(10) Draine, B. T.; Flatau, P. J. *J. Opt. Soc. Am. A* **1994**, 11, 1491−1499.
(11) Bian, R. X.; Dunn, R. C.; Xie, X. S.; Leung, P. T. *Phys. Rev. Lett.* **1995**, 75, 4772−4775.
(12) Coronado, E. A.; Schatz, G. C. *J. Chem. Phys.* **2003**, 119, 3926.
(13) Cottancin, E.; Celep, G.; Lermé, J.; Pellarín, M.; Huntzinger, J. R.; Vialle, J. L.; Broyer, M. *Theor. Chim. Acta* **2006**, 116, 514−523.
(14) Brack, M. *Rev. Mod. Phys.* **1993**, 65, 677.
(15) Bonačić-Koutecký, V.; Fantucci, P.; Koutecký, J. *Chem. Rev.* **1991**, 91, 1035.
(16) Prodan, E.; Nordlander, P. *Nano Lett.* **2003**, 3, 543−547.
(17) Prodan, E.; Nordlander, P.; Halas, N. J. *Nano Lett.* **2003**, 3, 1411−1415.
(18) Zuloaga, J.; Prodan, E.; Nordlander, P. *Nano Lett.* **2009**, 9, 887−891.
(19) Jensen, L.; Zhao, L. L.; Schatz, G. C. *J. Phys. Chem. C* **2007**, 111, 4756−4764.
(20) Aikens, C. M.; Li, S.; Schatz, G. C. *J. Phys. Chem. C* **2008**, 112, 11272−11279.
(21) Stener, M.; Nardelli, A.; De Francesco, R.; Fronzoni, G. *J. Phys. Chem. C* **2007**, 111, 11862−11871.
(22) Jensen, L. L.; Jensen, L. *J. Phys. Chem. C* **2008**, 112, 15697−15703.
(23) Baletto, F.; Mottet, C.; Ferrando, R. *Phys. Rev. Lett.* **2000**, 84, 5544−5547.
(24) Baletto, F.; Ferrando, R.; Fortunelli, A.; Montalenti, F.; Mottet, C. *J. Chem. Phys.* **2002**, 116, 3856−3863.
(25) Shao, X.; Yang, X.; Cai, W. *Chem. Phys. Lett.* **2008**, 460, 315−318.
(26) Xia, Y.; Xiong, Y.; Lim, B.; Skrabalak, S. E. *Angew. Chem. Int. Ed* **2009**, 48, 60−103.
(27) Pileni, M. P. *J. Phys. Chem. C* **2007**, 111, 9019−9038.

(28) Jensen, L.; Åstrand, P.-O.; Mikkelsen, K. V. *Int. J. Quantum Chem.* 2001, 84, 513–522.

(29) Thole, B. T. *Chem. Phys.* 1981, 59, 341.

(30) Mayer, A. *Phys. Rev. B* 2007, 75, 045407.

(31) Jensen, L.; Åstrand, P.-O.; Osted, A.; Kongsted, J.; Mikkelsen, K. V. *J. Chem. Phys.* 2002, 116, 4001.

(32) Shanker, B.; Applequist, J. *J. Chem. Phys.* 1996, 104, 6109–6116.

(33) Jensen, L.; Åstrand, P.-O.; Sylvester-Hvid, K. O.; Mikkelsen, K. V. *J. Phys. Chem. A* 2000, 104, 1563.

(34) Mayer, A.; Lambin, P.; Åstrand, P.-O. *Nanotechnology* 2008, 19 (12), 025203.

(35) Mayer, A.; Gonzalez, A. L.; Aikens, C. M.; Schatz, G. C. *Nanotechnology* 2009, 20, 195204.

(36) Bohren, C. F.; Huffman, D. R. *Absorption and scattering of light by small particles*; Wiley: New York, 1998.

(37) Böttcher, C. J. F. *Theory of Electric Polarization, 2nd ed.*; Elsevier: Amsterdam, 1973; Vol. 1.

(38) Tiggesbäumker, J.; Köller, L.; Meiwes-Broer, K.-H.; Liebsch, A. *Phys. Rev. A* 1993, 48, R1749–R1752.

(39) ADF, http://www.scm.com, 2007.

(40) Becke, A. D. *Phys. Rev. A* 1988, 38, 3098.

(41) Perdew, J. P. *Phys. Rev. B* 1986, 33, 8822.

(42) van Lenthe, E.; Baerends, E. J.; Snijders, J. G. *J. Chem. Phys.* 1993, 99, 4597–4610.

(43) Doye, J. P. K.; Wales, D. J. *New J. Chem.* 1998, 22, 733–744.

(44) Jensen, L.; Autschbach, J.; Schatz, G. C. *J. Chem. Phys.* 2005, 122, 224115.

(45) van Gisbergen, S. J. A.; Snijders, J. G.; Baerends, E. J. *Chem. Phys. Lett.* 1996, 259, 599–604.

(46) van Gisbergen, S. J. A.; Snijders, J. G.; Baerends, E. J. *Comput. Phys. Commun.* 1999, 118, 119.

(47) Juluri, B. K.; Zheng, Y. B.; Ahmed, D.; Jensen, L.; Huang, T. J. *J. Phys. Chem. C* 2008, 112, 7309–7317.

(48) Mackay, A. L. *Acta Crystallogr.* 1962, 15, 916–918.

(49) Baletto, F.; Ferrando, R. *Rev. Mod. Phys.* 2005, 77, 371–423.

(50) Cleveland, C. L.; Landman, U. *J. Chem. Phys.* 1991, 94, 7376–7396.

(51) Kreibig, U.; Fragstein, C. V. *Z. Physik* 1969, 224, 307–323.

(52) Thomas, S.; Nair, S. K.; Jamal, E. M. A.; Al-Harthi, S. H.; Varma, M. R.; Anantharaman, M. R. *Nanotechnology* 2008, 19 (7), 075710.

(53) Gonzalez, A. L.; Noguez, C.; Ortiz, G. P.; Rodriguez-Gattorno, G. *J. Phys. Chem. B* 2005, 109, 17512–17517.

JP904956F
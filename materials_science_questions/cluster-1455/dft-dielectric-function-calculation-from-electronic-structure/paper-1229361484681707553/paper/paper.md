# Nonempirical Range-Separated Hybrid Functional with Spatially Dependent Screened Exchange

Jiawei Zhan,† Marco Govoni,†,‡,¶ and Giulia Galli*,†,‡,§

†Pritzker School of Molecular Engineering, University of Chicago, Chicago, Illinois 60637, United States

‡Materials Science Division and Center for Molecular Engineering, Argonne National Laboratory, Lemont, Illinois 60439, United States

¶Department of Physics, Computer Science, and Mathematics, University of Modena and Reggio Emilia, Modena, 41125, Italy

§Department of Chemistry, University of Chicago, Chicago, Illinois 60637, United States

E-mail: gagalli@uchicago.edu

## Abstract

Electronic structure calculations based on Density Functional Theory have successfully predicted numerous ground state properties of a variety of molecules and materials. However, exchange and correlation functionals currently used in the literature, including semi-local and hybrid functionals, are often inaccurate to describe the electronic properties of heterogeneous solids, especially systems composed of building blocks with large dielectric mismatch. Here, we present a dielectric-dependent range-separated hybrid functional, SE-RSH, for the investigation of heterogeneous materials. We define a spatially dependent fraction of exact exchange inspired by the static Coulomb-hole and screened-exchange (COHSEX) approximation used in many body perturbation theory, and we show that the proposed functional accurately predicts


the electronic structure of several non-metallic interfaces, three- and two-dimensional, pristine and defective solids and nanoparticles.

## 1 Introduction

Materials are heterogeneous systems, often composed of different building blocks including interfaces¹ and defects. Density Functional Theory (DFT)²⁻⁴ has been extremely successful in predicting ground state and thermodynamic properties of many materials. However, a density functional that provides an equally accurate description of the electronic structure of systems composed of portions with different dielectric properties is not yet available (for example, a low-band-gap semiconductor interfaced with an insulating oxide, or an amorphous solid interfaced with a crystalline one). In general, density functionals appropriate to study thermodynamic properties may not accurately predict other quantities, such as electronic excitations and transport coefficients.⁵,⁶ In particular, the predictions of simple properties of heterogeneous materials such as band gaps and offsets are still challenging when using DFT.⁷,⁸ Hence the development of density functionals for heterogeneous systems remains a critical need of the materials science and condensed matter physics communities. We emphasize that accurate calculations of electronic band gaps and energy level alignments in heterostructures are essential to understand the functionality and performance of semiconductor devices,⁹ as well as of solar and photo-electrochemical cells.¹⁰ Band gaps and band offsets are necessary inputs for the evaluation of the quantum efficiency of several processes, including electron-hole separation or charge recombination in semiconductors and insulators.

Importantly, even when using theories beyond mean-field (e.g. many-body perturbation theory,¹¹,¹² dynamical mean field theory¹³,¹⁴ or Quantum Monte Carlo¹⁵), DFT results are almost always required as input. Another key reason to improve the accuracy and broaden the applicability of DFT calculations is the need to obtain reliable data to apply machine learning (ML) algorithms, as the success and promise of ML rely on the accuracy of compu-

tational and experimental data constituting the training sets. $^{16}$

DFT was originally applied to compute the structural and electronic properties of con- densed matter systems using the local density approximation $^{17-20}$ (LDA) and then gradi ent corrected approximations $^{21,22}$ (GGA) to the exchange and correlation energy functional (xc). Subsequently, hybrid functionals, $^{23-25}$ utilized first for finite, molecular systems, were adopted for solids as well. In hybrid DFT, the exchange energy is defined as a linear com- bination of exact (Hartree-Fock) and local exchange $^{26}$ energies. Among hybrid functionals, PBE0 $^{27}$ and HSE $^{28-30}$ have been popular ones to describe condensed systems. Recently, dielectric-dependent hybrid $^{31-34}$ functionals have been increasingly adopted to investigate the structural and electronic properties of solids, $^{32,33}$ liquids $^{35,36}$ and also of several molecules. $^{33}$ Other emerging approaches include Koopmans-compliant functionals $^{37-40}$ and the Localized Orbital Scaling Correction, $^{41,42}$ applicable to both molecules and solids.

However, most of these functionals are often not sufficiently accurate to predict the electronic properties of heterogeneous systems, including surfaces and interfaces, if differ- ent portions of the system exhibit substantially different dielectric screening. Several ap- proaches $^{43-45}$ have been recently proposed in an attempt to address this problem. Shimazaki et al. $^{43}$ introduced a descriptor of the local environment surrounding atoms in a semiconduc tor, which they used to define a position-dependent atomic dielectric constant. Borlido et al. $^{44}$ defined a local dielectric function using an empirical, system-dependent fitting process. Zheng et al. $^{45}$ introduced instead a nonempirical Screened-Exchange Dielectric-Dependent hybrid (SE-DDH) functional, using intuitive assumptions on local dielectric screening and showing promising results for both heterogeneous semiconductors and insulators.

In this work, we introduce a non-empirical, range-separated, dielectric-dependent func- tional which provides consistent and accurate predictions of the electronic properties of both3D and 2D solids, as well as of interfaces and finite systems. The functional is based on the definition of a mixing fraction of exact and local exchange energies and potentials, inspired by the static COulomb Hole and Screened-EXchange (COHSEX) approximation $^{46}$ used in

many body perturbation theory. We present a thorough validation of our results for various condensed systems, with focus on fundamental electronic properties such as band gaps and energy level alignments.

The remainder of this paper is organized as follows: In Sec. 2, we derive the expression of the Screened-Exchange Range-Separated Hybrid (SE-RSH) functional and establish a con- nection with more advanced electronic structure methods. We then present applications to the electronic structure of a variety of complex materials in Sec. 3. We conclude with Sec. 4.

## 2 Method

### 2.1 General hybrid functionals for complex materials

The generalized Kohn-Sham (GKS) nonlocal potential $v_{\rm GKS}(\mathbf{r},\mathbf{r}')$ entering the Kohn-Sham (KS) Hamiltonian is given by:

$$
v_{\rm GKS}(\mathbf{r},\mathbf{r}') = v_{H}(\mathbf{r}) + v_{x}(\mathbf{r},\mathbf{r}') + v_{c}(\mathbf{r}) + v_{\rm ext}(\mathbf{r}),
\tag{1}
$$

where $v_{H}(\mathbf{r})$, $v_{x}$ and $v_{c}(\mathbf{r})$ are the Hartree, nonlocal exchange and correlation potential, respectively, and $v_{\rm ext}(\mathbf{r})$ is the attractive Coulomb potential between electrons and nuclei. In hybrid DFT, the term $v_{x}(\mathbf{r},\mathbf{r}')$ is given by a linear combination of exact and semilocal exchange potential, and the mixing fraction $\alpha(\mathbf{r},\mathbf{r}')$ between the two depends on the specific hybrid functional. In Range-Separated Hybrid (RSH) functionals, $^{47-53}$ $\alpha(\mathbf{r},\mathbf{r}')$ has the following form:

$$
\alpha(\mathbf{r},\mathbf{r}') = m + (n - m)\mathrm{erfc}\left(\mu|\mathbf{r}-\mathbf{r}'|\right),
\tag{2}
$$

where the values of $m$ and $n$ determine the fraction of exact exchange included in the long- range (lr) and short-range (sr) components, respectively. The screening parameter $\mu$ defines how lr and sr components are connected to each other. By using $\alpha$ defined above, $v_{x}(\mathbf{r},\mathbf{r}')$

is:

$$
\begin{aligned}
v_{x}(\mathbf{r}, \mathbf{r}')= & \alpha(\mathbf{r}, \mathbf{r}') \Sigma_{x}(\mathbf{r}, \mathbf{r}') \\
& +(1-m) v_{x}^{\mathrm{lr}}(\mathbf{r} ; \mu)+(1-n) v_{x}^{\mathrm{sr}}(\mathbf{r} ; \mu),
\end{aligned} \tag{3}
$$

where the Hartree-Fock exchange $\Sigma_{x}(\mathbf{r}, \mathbf{r}')$ is given by:

$$
\Sigma_{x}(\mathbf{r}, \mathbf{r}')=-\sum_{j}^{N} \phi_{j}^{*}\left(\mathbf{r}'\right) \phi_{j}(\mathbf{r}) v\left(\mathbf{r}, \mathbf{r}'\right), \tag{4}
$$

and $\phi_{j}$ is the $j^{\text{th}}$ KS single-particle wave function, $N$ is the number of occupied electronic states and $v(\mathbf{r}, \mathbf{r}')$ is the Coulomb potential. The lr and sr components of the semilocal exchange potential, denoted as $v_{x}^{\mathrm{lr}}(\mathbf{r} ; \mu)$ and $v_{x}^{\mathrm{sr}}(\mathbf{r} ; \mu)$ respectively, depend only on the density $\rho(\mathbf{r})$ and its gradient. Here we adopt the PBE$^{21}$ approximation for the semilocal exchange $v_{x}(\mathbf{r})$ and correlation $v_{c}(\mathbf{r})$.

The expression of many of the exchange functionals commonly used in the literature, including PBE0$^{27}$ and HSE, $^{28-30}$ may be recovered from Eq.(3). In some recently defined Range-Separated Dielectric-Dependent Hybrid functionals (RS-DDH), $^{34,54}$ the values of $m, n, \mu$ are related to system-dependent dielectric properties computed from first principle. These functionals were shown to yield accurate electronic properties of inorganic materials and molecular crystals.

However, in the case of RS-DDH functionals, the mixing fraction entering Eq.(3) is not expected to be appropriate to describe interfaces and surfaces. Recently, Zheng et al.$^{45}$ introduced a mixing fraction defined using a local, spatially-dependent dielectric function $\epsilon(\mathbf{r})$:

$$
\alpha^{\mathrm{SE}-\mathrm{DDH}}\left(\mathbf{r}, \mathbf{r}'\right)=\frac{1}{\sqrt{\epsilon(\mathbf{r}) \epsilon\left(\mathbf{r}'\right)}}. \tag{5}
$$

Building on Ref. 45, we define a Screened-Exchange Range-Separated Hybrid (SE-RSH) functional that extends the applicability of RS-DDH to complex, heterogeneous materials,


and we define $\alpha(\mathbf{r}, \mathbf{r}')$ as follows:

$$
\begin{aligned}
\alpha^{\mathrm{SE}-\mathrm{RSH}}(\mathbf{r}, \mathbf{r}')= & \left(1-\frac{1}{\sqrt{\epsilon(\mathbf{r}) \epsilon\left(\mathbf{r}^{\prime}\right)}}\right) \operatorname{erfc}\left(\mu(\mathbf{r})\left|\mathbf{r}-\mathbf{r}^{\prime}\right|\right) \\
& +\frac{1}{\sqrt{\epsilon(\mathbf{r}) \epsilon\left(\mathbf{r}^{\prime}\right)}}.
\end{aligned}
\tag{6}
$$

Here, $\epsilon(\mathbf{r})$ and $\mu(\mathbf{r})$ represent a local dielectric function and local screening function, respectively, obtained from first principles as discussed below (Section 2.2). Table 1 summarizes the mixing fraction of exact exchange used to define all energy functionals mentioned above.

**Table 1:** The fraction of exact exchange used in several exchange-correlation functionals listed in column 1; $m$, $n$ and $\mu$ denote the long-range, short-range fraction of exact exchange and the screening parameter (function), respectively (see Eq. 2). $\epsilon_{\infty}$ is the macroscopic dielectric constant. See Sec. 2.2 for the definitions of $\mu(\mathbf{r})$ and $\epsilon(\mathbf{r})$.

<table>
<thead>
  <tr>
    <th></th>
    <th>$m$</th>
    <th>$n$</th>
    <th>$\mu$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>PBE$^{21}$</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>HSE06$^{28,29}$</td>
    <td>0</td>
    <td>0.25</td>
    <td>0.11</td>
  </tr>
  <tr>
    <td>DDH$^{31}$</td>
    <td>$1/\epsilon_{\infty}$</td>
    <td>$1/\epsilon_{\infty}$</td>
    <td>0</td>
  </tr>
  <tr>
    <td>RS-DDH$^{34}$</td>
    <td>$1/\epsilon_{\infty}$</td>
    <td>0.25</td>
    <td>$\mu$</td>
  </tr>
  <tr>
    <td>DD0-RSH-CAM$^{54}$</td>
    <td>$1/\epsilon_{\infty}$</td>
    <td>1</td>
    <td>$\mu$</td>
  </tr>
  <tr>
    <td>SE-DDH$^{45}$</td>
    <td>$1/\sqrt{\epsilon(\mathbf{r})\epsilon(\mathbf{r}')}$</td>
    <td>$1/\sqrt{\epsilon(\mathbf{r})\epsilon(\mathbf{r}')}$</td>
    <td>0</td>
  </tr>
  <tr>
    <td>SE-RSH</td>
    <td>$1/\sqrt{\epsilon(\mathbf{r})\epsilon(\mathbf{r}')}$</td>
    <td>1</td>
    <td>$\mu(\mathbf{r})$</td>
  </tr>
</tbody>
</table>

Using Eq.(6), the exchange and correlation potential of SE-RSH is then expressed as:

$$
\begin{aligned}
v_{x c}^{\mathrm{SE}-\mathrm{RSH}}\left(\mathbf{r}, \mathbf{r}^{\prime}\right)= & \alpha^{\mathrm{SE}-\mathrm{RSH}}\left(\mathbf{r}, \mathbf{r}^{\prime}\right) \Sigma_{x}\left(\mathbf{r}, \mathbf{r}^{\prime}\right) \\
& +\left(1-\frac{1}{\epsilon(\mathbf{r})}\right) v_{x}^{\mathrm{lr}}(\mathbf{r} ; \mu(\mathbf{r}))+v_{c}(\mathbf{r}).
\end{aligned}
\tag{7}
$$

The lr component of the PBE semilocal exchange can be calculated by scaling the PBE exchange hole, $^{55} J^{\mathrm{PBE}}(s, y)$, by the lr screening factor:

$$
\begin{aligned}
v_{x}^{\mathrm{lr}}(\mathbf{r} ; \mu(\mathbf{r}))= & -\epsilon_{x}^{\mathrm{LDA}}(\rho(\mathbf{r})) \frac{8}{9} \\
& \times \int_{0}^{\infty} \mathrm{d} y \, y J^{\mathrm{PBE}}(s, y) \operatorname{erf}\left(\frac{\mu(\mathbf{r}) y}{k_{F}}\right),
\end{aligned}
\tag{8}
$$

where $s = |\nabla\rho|/2k_F\rho$ is the reduced gradient, $k_F=(3\pi^2\rho)^{1/3}$ and $\epsilon_x^{\mathrm{LDA}}$ is the LDA exchange energy density.

As we remark in the Supporting Information, the calculation of the exchange energy entering the SE-RSH functional scales as the number of points used to represent $\mu(\mathbf{r})$. Hence, we adopt a coarse-grained approximation to $\mu(\mathbf{r})$ for computational convenience. Further, an integrable divergence appears as a singularity when the nonlocal exchange energy is formulated in reciprocal space and is present for any strictly positive mixing fraction $\alpha(\mathbf{r},\mathbf{r}')$. This divergence is treated following the procedure proposed by Gygi and Baldereschi$^{56}$ (see the Supporting Information for details).

## 2.2 Local Dielectric and Screening Functions

We describe next a non-empirical approach to compute the two local functions entering Eq.(6), namely the local dielectric function $\epsilon(\mathbf{r})$ and the local screening function $\mu(\mathbf{r})$. The former is obtained by DFT calculations in a finite electric field by minimizing the functional: $^{45,57,58}$

$$
F(\mathbf{E},[\rho])=E_{\mathrm{KS}}[\rho]-\int \mathbf{E} \cdot \mathbf{r} \rho(\mathbf{r}) d \mathbf{r},
\tag{9}
$$

where $\int \mathbf{E} \cdot \mathbf{r} \rho(\mathbf{r}) d \mathbf{r}$ is called the electric enthalpy, $\mathbf{E}$ is an external electric field and $E_{\mathrm{KS}}$ is the Kohn-Sham energy of the system. In periodic non-metallic systems, the spatially dependent

induced polarization due to the field $\mathbf{E}$ can be defined as: $^{59}$

$$
\Delta P(\mathbf{r})=-e \sum_{i}^{N} \Delta \mathbf{r}_{c}^{i} \delta\left(\mathbf{r}-\mathbf{r}_{c}^{i}\right),
\tag{10}
$$

where $\Delta \mathbf{r}_{c}^{i}$ is the shift of the center $(\mathbf{r}_{c})$ of the $i^{\text{th}}$ Wannier function induced by the applied electric field. The spatially dependent $\epsilon$ is then determined as:

$$
\epsilon_{k l}(\mathbf{r})=\delta_{k l}+4 \pi \frac{\Delta P_{k}(\mathbf{r})}{\Delta E_{l}},
\tag{11}
$$

where $k$ and $l$ are Cartesian coordinates.

![](./images/1229361484681707553_1.jpg)

Figure 1: Top panel: The local dielectric function $\epsilon(z)$ and local screening function $\mu(z)$ for a model H-Si/H₂O interface, computed as averages of $\epsilon(\mathbf{r})$ (Eq. 11) and $\mu(\mathbf{r})$ (Eq. 12) in the (x,y) plane parallel to the interface. The z axis is perpendicular to the interface. Bottom panel: Band edges of H-Si/H₂O computed (Eq. 20) at different levels of theory, using the SE-RSH functional proposed in this work, the HSE06 functional $^{28,29}$ and $G_0W_0@$DDH calculations. $^{60}$

The local screening function, which generalizes the definition of constant screening parameter $\mu_{\text{TF}}$ introduced by Skone et al. $^{34}$ for homogeneous materials, is related to the volume occupied by the valence electrons:

$$
\mu(\mathbf{r})=\frac{1}{2} k_{\mathrm{TF}}(\mathbf{r})=\left(\frac{3 \rho_{v}(\mathbf{r})}{\pi}\right)^{1 / 2},
\tag{12}
$$

where $k_{TF}$ is the Thomas-Fermi screening length and $\rho_v$ is the valence electron density. Fig.(1) shows $\epsilon(\mathbf{r})$ and $\mu(\mathbf{r})$ computed at the PBE level of theory for a model H-Si/H$_2$O interface. We can clearly observe two distinct average values of $\epsilon(\mathbf{r})$ and $\mu(\mathbf{r})$ in the two bulk regions where $\epsilon$ and $\mu$ oscillate around constant values, equal to those one would obtain in the respective bulk systems represented by slabs of the same size.

Alternative definitions of screening parameters for homogeneous materials have been suggested in the literature. For example, Skone et al. $^{34}$ and Chen et al. $^{54}$ defined screening parameters $\mu_{\text{fit}}$ by using a model to fit the long-range decay of the diagonal elements of the dielectric function $[\epsilon^{-1}]$. However, these authors noted that RS-DDH utilizing either $\mu_{\text{TF}}$ or $\mu_{\text{fit}}$ yields comparable accuracy, with $\mu_{\text{TF}}$ being less computationally demanding to obtain.

We have tested the impact of calculating $\epsilon(\mathbf{r})$ and $\mu(\mathbf{r})$ in a self-consistent manner.

![](./images/1229361484681707553_2.jpg)

Figure 2: The local dielectric function $\epsilon(z)$ and local screening function $\mu(z)$ for a h-BN monolayer, computed as averages of $\epsilon(\mathbf{r})$ (Eq. 11) and $\mu(\mathbf{r})$ (Eq. 12) in the (x,y) plane of the monolayer. The z axis is perpendicular to the monolayer. The solid and dashed lines represent calculations conducted at the PBE level of theory and self-consistent calculations (see text), respectively.

Specifically, the local functions given by Eq.(11) and Eq.(12) are evaluated iteratively until convergence is achieved, akin to the method proposed in Ref. 31,34. A comparison of non-self-consistent (at the PBE level) and self-consistent (sc) $\epsilon(\mathbf{r})$ and $\mu(\mathbf{r})$ for a monolayer h-BN is presented in Fig.(2). We also report the fundamental band gap of the system computed with SE-RSH in Fig.(3), along with $G_0W_0$ results.

Consistent with previous studies, $^{45}$ we found that utilizing a self-consistent approach for the computation of $\mu(\mathbf{r})$ and $\epsilon(\mathbf{r})$ yields only minor changes in their values, while significantly

![](./images/1229361484681707553_3.jpg)

Figure 3: The fundamental band gap ($E_g$) of a h-BN monolayer, computed as a function of the vacuum length (d) in the supercell. Results are shown using the SE-RSH functional proposed in this work, where the local functions $\epsilon(\mathbf{r})$ and $\mu(\mathbf{r})$ (see Fig. 2) are computed either at the PBE level of theory (non-sc) or self-consistently (sc). We also show $G_0W_0$ results obtained by truncating the Coulomb potential in two-dimensions. $^{61}$

increasing the computational cost. Therefore, in the following, we report results obtained by the SE-RSH functional with $\epsilon(\mathbf{r})$ and $\mu(\mathbf{r})$ computed at the PBE level of theory, non self-consistently.

We note that we have not used the SE-RSH functional for structural relaxations, as an efficient strategy to update $\epsilon(\mathbf{r})$ and $\mu(\mathbf{r})$ when atomic positions vary is still under investigation. Therefore, in our study, all atomic structures were optimized with the PBE functional and then electronic structure calculations were carried out with the SE-RSH functional. However, we note that some studies $^{54}$ have utilized the RS-DDH functional to obtain the lattice constants of homogeneous semiconductors and insulators, including some of those reported in Table 3. For example, Ref. 54 showed that the RS-DDH functional yields lattice constants in better agreement with experiments than the semilocal PBE functional. These results are encouraging since the SE-RSH functional reduces to RS-DDH in homogeneous bulk systems.

### 2.3 Screened Fock Exchange as a simplified Self-Energy

We now turn to discuss the connection of the KS equations with the functional defined in the previous section, and the Hedin's equations $^{11}$ of many body perturbation theory. In

the Hedin's equations, instead of an exchange-correlation potential, a nonlocal and energy-dependent operator is present, known as the self-energy $\Sigma$. Here we compare the GKS potential of Eq.(1) with the self-energy expressed within the static $GW$ approximation$^{46}$ (static-COHSEX):

$$
\Sigma(\mathbf{r}, \mathbf{r}^{\prime} ; \omega=0)=\Sigma_{\mathrm{SEX}}(\mathbf{r}, \mathbf{r}^{\prime})+\Sigma_{\mathrm{COH}}(\mathbf{r}, \mathbf{r}^{\prime}),
\tag{13}
$$

where $\Sigma_{\mathrm{SEX}}$ is the statically screened-exchange (SEX) and the local $\Sigma_{\mathrm{COH}}$ represents the Coulomb-hole (COH) interaction:

$$
\begin{aligned}
\Sigma_{\mathrm{SEX}}(\mathbf{r}, \mathbf{r}^{\prime}) & =-\sum_{i=1}^{N} \phi_{i}^{*}(\mathbf{r}^{\prime}) \phi_{i}(\mathbf{r}) W(\mathbf{r}, \mathbf{r}^{\prime}) \\
\Sigma_{\mathrm{COH}}(\mathbf{r}, \mathbf{r}^{\prime}) & =-\frac{1}{2} \delta(\mathbf{r}-\mathbf{r}^{\prime})\left[v(\mathbf{r}, \mathbf{r}^{\prime})-W(\mathbf{r}, \mathbf{r}^{\prime})\right].
\end{aligned}
\tag{14}
$$

In Eq.(14), the screened Coulomb potential $W$ is:

$$
W(\mathbf{r}, \mathbf{r}^{\prime})=\int \mathrm{d} \mathbf{r}^{\prime \prime} \epsilon^{-1}(\mathbf{r}, \mathbf{r}^{\prime \prime}) v(\mathbf{r}^{\prime \prime}, \mathbf{r}^{\prime}),
\tag{15}
$$

where $\epsilon^{-1}$ is the inverse dielectric response function.

The use of the COHSEX's self-energy in the KS equations, instead of the exchange-correlation (xc) potential, has been previously explored by several authors$^{34,54}$ for homogeneous systems. Below, we compare the results of COHSEX and the SE-RSH xc potential for a representative heterogeneous system.

We define a screened Hartree-Fock exchange $\Sigma_{x}^{\alpha}$ operator:

$$
\Sigma_{x}^{\alpha}(\mathbf{r}, \mathbf{r}^{\prime})=-\sum_{j}^{N} \phi_{j}^{*}(\mathbf{r}^{\prime}) \phi_{j}(\mathbf{r}) \alpha(\mathbf{r}, \mathbf{r}^{\prime}) v(\mathbf{r}, \mathbf{r}^{\prime}).
\tag{16}
$$

which depends on the density matrix $(\rho)$ and it is thus invariant under unitary transformations of the occupied manifold. We express $\Sigma_{x}^{\alpha}$ using maximally localized orbitals $(\psi)$ obtained from a unitary transformation of the KS eigenstates. Within such a representation

, the off-diagoonal elements of the screened Hartree-Fock exchange can be neglected, and
the matrix elements of $\Sigma_x^\alpha$ become:

$$
\begin{aligned}
\langle k|\Sigma_x^\alpha| l\rangle &=-\sum_{j}^{N} \iint \mathrm{d} \mathbf{r} \mathrm{d} \mathbf{r}^{\prime} \rho_{k j}(\mathbf{r}) \alpha\left(\mathbf{r}, \mathbf{r}^{\prime}\right) v\left(\mathbf{r}, \mathbf{r}^{\prime}\right) \rho_{l j}^{*}\left(\mathbf{r}^{\prime}\right) \\
& \approx-\left\langle\rho_{k k}|\alpha \odot v| \rho_{l l}\right\rangle \delta_{k l},
\end{aligned}
\tag{17}
$$

where $\rho_{k j}(\mathbf{r})=\psi_{k}^{*}(\mathbf{r}) \psi_{j}(\mathbf{r}), \rho_{k k}(\mathbf{r})$ is the $k^{\text {th }}$ orbital density and $\odot$ is the Hadamard product.

In a similar fashion, the matrix elements of $\Sigma_{\mathrm{SEX}}$ in a localized representation become:

$$
\left\langle k\left|\Sigma_{\mathrm{SEX}}\right| l\right\rangle \approx-\left\langle\rho_{k k}\left|\epsilon^{-1} v\right| \rho_{l l}\right\rangle \delta_{k l}.
\tag{18}
$$

We then define state-dependent screened-exchange Ratios (R) using the matrix elements
of $\Sigma_{x}^{\alpha}$ and $\Sigma_{\mathrm{SEX}}$, respectively:

$$
\begin{aligned}
& \mathrm{R}_{i}^{\alpha}=\frac{\left\langle\rho_{i i}|\alpha \odot v| \rho_{i i}\right\rangle}{\left\langle\rho_{i i}|v| \rho_{i i}\right\rangle} \\
& \mathrm{R}_{i}^{\epsilon^{-1}}=\frac{\left\langle\rho_{i i}\left|\epsilon^{-1} v\right| \rho_{i i}\right\rangle}{\left\langle\rho_{i i}|v| \rho_{i i}\right\rangle}.
\end{aligned}
\tag{19}
$$

We use the Projective Dielectric Eigenpotential Method (PDEP) $^{62}$ to evaluate the static
dielectric response function in a separable form $^{63}$ and to compute $\mathrm{R}^{\epsilon^{-1}}$. Fig.(4) shows $\mathrm{R}^{\epsilon^{-1}}$
and $\mathrm{R}^{\alpha}$ evaluated for mixing fractions $\alpha\left(\mathbf{r}, \mathbf{r}^{\prime}\right)$ corresponding to different hybrid functionals
for a model $\mathrm{Si}_{3} \mathrm{~N}_{4} / \mathrm{Si}(100)$ interface.

In the case of the DDH functional where $\alpha=1 / \epsilon_{\infty}, \mathrm{R}$ is a constant. The behavior of
$\mathrm{R}$ evaluated for the SE-DDH functional is similar to that of $\mathrm{R}^{\epsilon^{-1}}$. However, the absolute
values of $\mathrm{R}$ obtained with SE-DDH differ from those of $\mathrm{R}^{\epsilon^{-1}}$. Interestingly, when using the
range-separated functional SE-RSH, we finally obtain values of $\mathrm{R}$ in excellent agreement with
those of $\epsilon^{-1}$. Hence, we conclude that the mixing fraction used in the definition of SE-RSH
is an accurate approximation of the statically screened COHSEX.


![](./images/1229361484681707553_4.jpg)

Figure 4: The state dependent screened-exchange Ratio (R) computed for a model Si₃N₄/Si(100) interfaces, where Si is crystalline and Si₃N₄ is amorphous. We show R computed at different levels of the theory, using Eq.(19) and the functionals SE-DDH,⁴⁵ DDH³¹ and SE-RSH proposed in this work. The results for $\epsilon^{-1}$ were obtained with the WEST code.⁶⁴,⁶⁵

## 2.4 Computational details

We implemented the SE-RSH hybrid functional in the Qbox⁶⁶ code and performed calculations for several systems using supercells and the $\Gamma$ point sampling of the Brillouin zone, with optimized norm-conserving Vanderbilt pseudopotentials.⁶⁷ The energy cutoff for the plane-wave basis set is set at 60 Ry. For two-dimensional systems, we used the lattice parameters presented in Table 2 and 6×6 supercells, without performing any additional relaxation of the cell volume. The atomic positions were optimized using the PBE functional until the atomic forces were below 0.05 eV/Å. To minimize the interactions between neighboring supercells, a minimum of 15 Å vacuum spacing was included in our supercells.

# 3 Electronic structure of complex materials using the SE-RSH functional

In the following, we first assess the accuracy of the SE-RSH functional for the electronic properties of three-dimensional homogeneous systems and then investigate heterogeneous systems, including interfaces, two-dimensional pristine and defective systems (2D systems)

Table 2: Lattice parameters ($a_0$) of two-dimensional systems studied in this work.

<table>
<thead>
  <tr>
    <th></th>
    <th>$a_0(\mathring{A})$</th>
    <th>Reference</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>BP</td>
    <td>3.18</td>
    <td>Ref. 68</td>
  </tr>
  <tr>
    <td>phosphorene</td>
    <td>3.31</td>
    <td>Ref. 69</td>
  </tr>
  <tr>
    <td>MoS₂</td>
    <td>3.16</td>
    <td>Ref. 70</td>
  </tr>
  <tr>
    <td>WS₂</td>
    <td>3.15</td>
    <td>Ref. 71</td>
  </tr>
  <tr>
    <td>GaAs</td>
    <td>3.97</td>
    <td>Ref. 72</td>
  </tr>
  <tr>
    <td>GaN</td>
    <td>3.20</td>
    <td>Ref. 73</td>
  </tr>
  <tr>
    <td>AlN</td>
    <td>3.09</td>
    <td>Ref. 68</td>
  </tr>
  <tr>
    <td>graphane(CH)</td>
    <td>2.51</td>
    <td>Ref. 74</td>
  </tr>
  <tr>
    <td>h-BN</td>
    <td>2.51</td>
    <td>Ref. 75</td>
  </tr>
</tbody>
</table>

and nanoparticles.

### 3.1 Homogenous 3D systems

In Table 3, we compare the band gaps obtained for 3D systems using the SE-RSH hybrid functional and other dielectric-dependent hybrid functionals, $^{31,34,54}$ specifically the RS-DDH$^{34}$ and the DD0-RSH-CAM, $^{54}$ that both utilize $1/\epsilon_\infty$ as the fraction of Fock exchange in the long range part and a constant screening parameter $\mu$. The main difference between RS-DDH and DD0-RSH-CAM lies in the description of the short-range exchange potential: the fraction of Fock exchange is 25% in the former and 100% in the latter. In our comparisons, the average values of the local dielectric function $\overline{\epsilon(\mathbf{r})}$ and of the local screening function $\overline{\mu(\mathbf{r})}$ are adopted when using RS-DDH and DD0-RSH-CAM, instead of $\epsilon_\infty$ and $\mu$.

Since in our calculations we did not consider electron-phonon coupling, we subtracted the value of the zero-phonon remormalization (ZPR)$^{54}$ from the computed values of the band gaps of semiconductors and insulators when comparing with experiments. The results obtained with the SE-RSH and DD0-RSH-CAM functionals are extremely similar, showing the relative insensitivity of the band gaps of the semiconductors studied here to the small variation of $\epsilon(\mathbf{r})$ and $\mu(\mathbf{r})$ in homogeneous 3D systems. $^{45}$ We note that when $\epsilon(\mathbf{r})$ and $\mu(\mathbf{r})$

Table 3: Fundamental energy gaps (eV) [Columns 4-8] of three dimensional materials obtained using different energy functionals, as specified in the first row. Column 2 and 3 provide the macroscopic dielectric constant and constant screening parameter used in DDH, RS-DDH and DD0-RSH-CAM calculations. Zero-phonon renormalization of the band gap ($E_{\text{corr}}$) (eV) are also reported in the last column when available from experiments. MAE and MARE are the mean absolute and mean absolute relative error of calculated band gap, respectively, compared to ($\text{Exp.} + E_{\text{corr}}$).

<table>
<thead>
<tr>
<th>
</th>
<th>
$\overline{\epsilon(\mathbf{r})}$
</th>
<th>
$\overline{\mu(\mathbf{r})}$
</th>
<th>
PBE$^{21}$
</th>
<th>
HSE06$^{28,29}$
</th>
<th>
DDH$^{31}$
</th>
<th>
RS-DDH$^{34}$
</th>
<th>
DD0-RSH-CAM$^{54}$
</th>
<th>
SE-RSH
</th>
<th>
Exp.
</th>
<th>
$E_{\text{corr}}$$^{\text{a}}$
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
Si
</td>
<td>
11.76
</td>
<td>
0.55
</td>
<td>
0.61
</td>
<td>
1.14
</td>
<td>
0.99
</td>
<td>
1.02
</td>
<td>
1.11
</td>
<td>
1.10
</td>
<td>
1.17
</td>
<td>
0.06
</td>
</tr>
<tr>
td>
SiO$_2$
</td>
<td>
2.49
</td>
<td>
0.51
</td>
<td>
5.95
</td>
<td>
7.69
</td>
<td>
9.99
</td>
<td>
9.88
</td>
<td>
10.62
</td>
<td>
10.43
</td>
<td>
9.7
</td>
<td>
</td>
</tr>
<tr>
<td>
C
</td>
<td>
5.60
</td>
<td>
0.68
</td>
<td>
4.19
</td>
<td>
5.35
</td>
<td>
5.42
</td>
<td>
5.45
</td>
<td>
5.67
</td>
<td>
5.63
</td>
<td>
5.48
</td>
<td>
0.37
</td>
</tr>
<tr>
<td>
SiC
</td>
<td>
6.53
</td>
<td>
0.61
</td>
<td>
1.37
</td>
<td>
2.24
</td>
<td>
2.35
</td>
<td>
2.36
</td>
<td>
2.45
</td>
<td>
2.44
</td>
<td>
2.42
</td>
<td>
0.11
</td>
</tr>
<tr>
<td>
BN
</td>
<td>
4.43
</td>
<td>
0.68
</td>
<td>
4.53
</td>
<td>
5.83
</td>
<td>
6.33
</td>
<td>
6.39
</td>
<td>
6.56
</td>
<td>
6.56
</td>
<td>
6.4
</td>
<td>
0.34
</td>
</tr>
<tr>
<td>
AlP
</td>
<td>
7.27
</td>
<td>
0.55
</td>
<td>
1.56
</td>
<td>
2.25
</td>
<td>
2.27
</td>
<td>
2.37
</td>
<td>
2.47
</td>
<td>
2.45
</td>
<td>
2.52
</td>
<td>
0.02
</td>
</tr>
<tr>
<td>
AlAs
</td>
<td>
8.27
</td>
<td>
0.57
</td>
<td>
1.32
</td>
<td>
1.93
</td>
<td>
1.91
</td>
<td>
1.90
</td>
<td>
2.07
</td>
<td>
2.05
</td>
<td>
2.24
</td>
<td>
0.04
</td>
</tr>
<tr>
<td>
GaAs
</td>
<td>
13.37
</td>
<td>
0.54
</td>
<td>
0.42
</td>
<td>
1.26
</td>
<td>
0.79
</td>
<td>
0.90
</td>
<td>
1.43
</td>
<td>
1.41
</td>
<td>
1.52
</td>
<td>
0.05
</td>
</tr>
<tr>
<td>
MgO
</td>
<td>
2.81
</td>
<td>
0.63
</td>
<td>
4.79
</td>
<td>
6.47
</td>
<td>
7.70
</td>
<td>
7.88
</td>
<td>
8.32
</td>
<td>
8.25
</td>
<td>
7.83
</td>
<td>
0.53
</td>
</tr>
<tr>
<td>
MAE(eV)
</td>
<td>
</td>
<td>
</td>
<td>
1.78
</td>
<td>
0.74
</td>
<td>
0.40
</td>
<td>
0.33
</td>
<td>
0.22
</td>
<td>
0.22
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
MARE(%)
</td>
<td>
</td>
<td>
</td>
<td>
43.6
</td>
<td>
14.4
</td>
<td>
14.1
</td>
<td>
12.16
</td>
<td>
5.5
</td>
<td>
5.9
</td>
<td>
</td>
<td>
</td>
</tr>
</tbody>
</table>

$^{\text{a}}$ $E_{\text{corr}}$ values are from Ref. 54.


are constant, the expressions of the SE-RSH and DD0-RSH-CAM functionals coincide. The energy gaps calculated using the RS-DDH functional are marginally lower compared to those obtained with the DD0-RSH-CAM and SE-RSH functionals, indicating that using the un-screened Fock exchange potential within the short-range component is an effective strategy.

We used the same functionals to compute the electronic structure of point defects in 3D materials, in particular the nitrogen-vacancy (NV) center in diamond. The results are presented in Fig.(5). We find that SE-RSH yields band edges and defect levels comparable to those obtained from DD0-RSH-CAM calculations, showing that using the average local dielectric function and local screening parameter of the host crystal provides an accurate description of the electronic properties of the defect. We will see in Sec. 3.4 that a different conclusion holds for defects in 2D systems.

![](./images/1229361484681707553_5.jpg)

Figure 5: Single-particle energy levels (eV) of the nitrogen vacancy in diamond, computed at different levels of theory and referenced to the valence band maximum (VBM). We show results obtained with the DDH,³¹ DD0-RSH-CAM⁵⁴ functionals and the SE-RSH functional proposed in this work. All calculations were performed in cells with 216 atoms.

## 3.2 Heterogeneous 3D systems: Interfaces

We investigated the electronic properties of several representative interfaces H-Si/H₂O, Si/Si₃N₄, Si/SiO₂) using the same models reported in Ref. 44,45.

Fig.(1) and (6) show the band edges of three interfaces obtained by computing the Local

![](./images/1229361484681707553_6.jpg)

Figure 6: Top panel: The local dielectric function $\epsilon(z)$ and local screening function $\mu(z)$ for model $\text{Si/Si}_3\text{N}_4$ and $\text{Si/SiO}_2$ interfaces, computed as averages of $\epsilon(\mathbf{r})$ (Eq. 11) and $\mu(\mathbf{r})$ (Eq. 12) in the (x,y) plane parallel to the interface. The z axis is perpendicular to the interface. Bottom panel: Band edges of $\text{Si/Si}_3\text{N}_4$ and $\text{Si/SiO}_2$ computed (Eq. 20) at different levels of theory, using the SE-RSH functional proposed in this work and the HSE06 functional. $^{28,29}$ Experimental data (Exp.) $^{76,77}$ are reported as dashed lines and green bands, whose width indicates the expected range of the conduction band minimum (See Table 4).

Density of States (LDOS) $^{78}$ defined as:

$$
D(\epsilon, z)=2 \sum_{n}\left|\left\langle z | \phi_{n}\right\rangle\right|^{2} \delta\left(\epsilon-\epsilon_{n}\right), \tag{20}
$$

where z is the direction perpendicular to the interface, $\left|\left\langle z | \phi_{n}\right\rangle\right|^{2}$ is the electron density integrated in the $xy$ plane, and $\epsilon_{n}$ are the Kohn-Sham eigenvalues.

In the case of $\text{H-Si/H}_2\text{O}$, we obtain a band gap in the silicon region (1.8 eV) which is larger than the bulk value (1.17 eV) since the slab chosen to represent Si has just few layers and hence the system is quantum confined. $^{79}$ In the water region, we obtain a value of 10 eV, which is in good agreement with the values 10.5 eV obtained at the $\text{G}_0\text{W}_0@\text{DDH}$ level. $^{60}$ Interestingly, SE-RSH provides a smaller band gap compared to DD0-RSH-CAM, which yields 10.9 eV. $^{80}$ This discrepancy can be attributed to the more localized nature of the electronic density in water, relative to that of semiconductors reported in Table 3. In water, $\epsilon(\mathbf{r})$ exhibits marked fluctuations, reaching values substantially higher than $\epsilon_{\infty}$ in re-

gions of high electronic density. Hence, using $1/\epsilon_\infty$ as the mixing fraction of exact exchange in the long-range component is not an accurate approximation. In the cases of $Si/Si_3N_4$ and $Si/SiO_2$, we also compare computed band offsets with experiments and other calculations (see Table 4) carried out using supercells of the same size.

Table 4: Conduction band (CBO) and Valence band (VBO) offsets (eV) for models of $Si/Si_3N_4$ and $Si/SiO_2$ interfaces computed at different levels of theory, compared to experimental results (Exp.). The $G_0W_0$ results have been computed starting from PBE calculations.

<table>
  <thead>
    <tr>
      <th>Interface</th>
      <th>Method</th>
      <th>CBO</th>
      <th>VBO</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="4">$Si/Si_3N_4$</td>
      <td>HSE06</td>
      <td>1.90</td>
      <td>1.23</td>
    </tr>
    <tr>
      <td>SE-RSH</td>
      <td>2.3</td>
      <td>1.63</td>
    </tr>
    <tr>
      <td>$G_0W_0$ $^{76}$</td>
      <td>1.90</td>
      <td>1.50</td>
    </tr>
    <tr>
      <td>Exp. $^{76}$</td>
      <td>1.83-2.83</td>
      <td>1.5-1.78</td>
    </tr>
    <tr>
      <td rowspan="4">$Si/SiO_2$</td>
      <td>HSE06</td>
      <td>3.02</td>
      <td>3.75</td>
    </tr>
    <tr>
      <td>SE-RSH</td>
      <td>3.68</td>
      <td>5.07</td>
    </tr>
    <tr>
      <td>$G_0W_0$ $^{44}$</td>
      <td>2.90</td>
      <td>4.10</td>
    </tr>
    <tr>
      <td>Exp.</td>
      <td>3.22-3.82$^{a}$</td>
      <td>4.71 $^{77}$</td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <td colspan="4">$^{a}$CBO estimated using VBO=4.71 eV, and the experimental band gaps of Si (1.17 eV) and $SiO_2$ (9.1–9.7 eV $^{44,81}$), respectively.</td>
    </tr>
  </tfoot>
</table>

We now turn to semiconductor superlattices that are almost lattice-matched, and represent a class of systems thoroughly studied$^{82}$ by the electronic structure community. We computed band offsets for GaAs/AlAs(100), AlP/GaP(100) and Si/GaP(100) heterojunctions, using the same supercells as in Ref. 82 and the method of Van de Walle et al.$^{83}$ Our results are reported in Table 5, together with those of other calculations performed with the PBE, PBE0 functionals and the $G_0W_0@$PBE approximation. $^{44,45}$

In agreement with $G_0W_0$ calculations, all hybrid functionals show that AlAs/GaAs and Si/GaP are type I heterojunctions, whilst AlP/GaP is type II. The SE-DDH functional, however, yields a larger value for the conduction band offset (CBO) of AlAs/GaAs due to its substantial underestimation of the experimental GaAs band gap. Indeed, hybrid functionals

Table 5: Conduction (CBO) and valence (VBO) band offsets of selected semiconductor heterojunctions computed using the method of Ref. 83.

<table>
  <thead>
    <tr>
      <th></th>
      <th>Method¹</th>
      <th>CBO</th>
      <th>VBO</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="5">AlAs/GaAs</td>
      <td>HSE06</td>
      <td>0.26</td>
      <td>0.43</td>
    </tr>
    <tr>
      <td>SE-DDH</td>
      <td>0.57</td>
      <td>0.54</td>
    </tr>
    <tr>
      <td>SE-RSH</td>
      <td>0.11</td>
      <td>0.56</td>
    </tr>
    <tr>
      <td>$G_0W_0$</td>
      <td>0.17</td>
      <td>0.60</td>
    </tr>
    <tr>
      <td>Exp.</td>
      <td>0.18</td>
      <td>0.53</td>
    </tr>
    <tr>
      <td rowspan="5">GaP/Si</td>
      <td>HSE06</td>
      <td>0.74</td>
      <td>0.40</td>
    </tr>
    <tr>
      <td>SE-DDH</td>
      <td>0.72</td>
      <td>0.47</td>
    </tr>
    <tr>
      <td>SE-RSH</td>
      <td>0.71</td>
      <td>0.55</td>
    </tr>
    <tr>
      <td>$G_0W_0$</td>
      <td>0.83</td>
      <td>0.53</td>
    </tr>
    <tr>
      <td>Exp.</td>
      <td>0.38</td>
      <td>0.80</td>
    </tr>
    <tr>
      <td rowspan="5">AlP/GaP</td>
      <td>HSE06</td>
      <td>-0.55</td>
      <td>0.48</td>
    </tr>
    <tr>
      <td>SE-DDH</td>
      <td>-0.40</td>
      <td>0.56</td>
    </tr>
    <tr>
      <td>SE-RSH</td>
      <td>-0.50</td>
      <td>0.55</td>
    </tr>
    <tr>
      <td>$G_0W_0$</td>
      <td>-0.87</td>
      <td>0.67</td>
    </tr>
    <tr>
      <td>Exp.</td>
      <td>-0.39</td>
      <td>0.55</td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <td colspan="4">¹ Experimental and $G_0W_0$ values are from Ref. 44.</td>
    </tr>
  </tfoot>
</table>

without a correct short-range mixing fraction commonly underestimate the band gap of systems with localized semicore d states. $^{54}$ Instead, the accuracy of the SE-RSH functional in predicting band offsets is comparable to that of $G_0W_0$, due to the description, on the same footing, of localized and delocalized electronic states.

### 3.3 2D systems

Predicting the electronic structure of 2D systems is more challenging, in general, than that of 3D materials, as many xc functionals are tailored for bulk solids. $^{84}$ For example, the DDH functional is not expected to be accurate for 2D systems because the macroscopic dielectric constant $\epsilon_\infty$ is ill-defined when vacuum is present in the supercell. In addition the comparison with experiments is not straightforward since measurements are usually performed on substrates whose interaction with the 2D material may not be negligible. $^{85}$

Here we assess the accuracy of the SE-RSH functional for nine 2D systems by comparing results with those of the $GW$ quasiparticle method. Table 6 shows the results obtained with several hybrid functionals, including SE-RSH, SE-DDH (Eq. 5), HSE06 and DDH ($\alpha=1/\epsilon_{\text{bulk}}$). Values of the macroscopic dielectric constant for their corresponding bulk systems ($\epsilon_{\text{bulk}}$) used in DDH calculations are from Ref. 54. $GW$ quasiparticle band gaps are used as reference values. We find that HSE06 systematically underestimates the fundamental band gaps of all the 2D systems studied here and that DDH yields more accurate band gaps compared to HSE06, albeit not in excellent agreement with experiments. The accuracy of DDH for 2D systems may be improved $^{74}$ if the mixing fraction of exact exchange is appropriately fine-tuned through the enforcement of the generalized Koopmans' condition, $^{98,99}$ e.g. by using specific defects as probes. However, such a method may require multiple calculations for charged defective systems whose specific choice is material dependent.

When using SE-DDH, we obtain an improvement over DDH results, however the computed band gaps are slightly underestimated compared to our reference results.

Among all hybrid functionals adopted here, the SE-RSH functional provides the most

Table 6: Fundamental energy gaps (eV) evaluated with hybrid functionals compared with the results of $GW$ calculations for 2D systems. For calculations with the DDH functional we used the mixing fraction corresponding to the 3D bulk long-wavelength dielectric constant. The SE-DDH and SE-RSH columns report electronic gaps evaluated with the functionals described in Sec.2. The calculations marked as Ref. ($GW$) have all been performed at the $G_0W_0$@PBE level of theory (except those of Ref. 68) with the lattice constant shown in Table 2. The MAE and MARE are computed by comparing the calculated band gap to the reference gap (column 6).

<table>
  <thead>
    <tr>
      <th></th>
      <th>HSE06²⁸,²⁹</th>
      <th>DDH³¹</th>
      <th>SE-DDH⁴⁵</th>
      <th>SE-RSH</th>
      <th>Ref. ($GW$)</th>
      <th>Other $GW$ resultsᵇ</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>BP</td>
      <td>1.36</td>
      <td>1.35</td>
      <td>1.31</td>
      <td>1.64</td>
      <td>1.81ᵃ ⁶⁸</td>
      <td></td>
    </tr>
    <tr>
      <td>phosphorene</td>
      <td>1.50</td>
      <td>1.60</td>
      <td>1.66</td>
      <td>2.1</td>
      <td>2.00⁶⁹</td>
      <td>1.94-2.1⁸⁶,⁸⁷</td>
    </tr>
    <tr>
      <td>MoS₂ᶜ</td>
      <td>2.17</td>
      <td>2.3</td>
      <td>2.13</td>
      <td>2.61</td>
      <td>2.58⁷⁰</td>
      <td>2.60-2.80⁸⁸⁻⁹⁰</td>
    </tr>
    <tr>
      <td>WS₂ᶜ</td>
      <td>2.48</td>
      <td>2.46</td>
      <td>2.50</td>
      <td>2.68</td>
      <td>2.90⁷¹</td>
      <td>3.05-3.11⁸⁹,⁹¹</td>
    </tr>
    <tr>
      <td>GaAs</td>
      <td>1.67</td>
      <td>1.63</td>
      <td>1.63</td>
      <td>2.43</td>
      <td>2.86⁷²</td>
      <td>2.95⁹²</td>
    </tr>
    <tr>
      <td>GaN</td>
      <td>3.53</td>
      <td>3.64</td>
      <td>3.97</td>
      <td>4.41</td>
      <td>4.44⁷³</td>
      <td>4.14-5.00⁶⁸,⁹³</td>
    </tr>
    <tr>
      <td>AlNᶜ</td>
      <td>3.08</td>
      <td>4.73</td>
      <td>5.33</td>
      <td>5.68</td>
      <td>5.57ᵃ ⁶⁸</td>
      <td>5.36-5.7⁹⁴,⁹⁵</td>
    </tr>
    <tr>
      <td>graphane(CH)</td>
      <td>4.41</td>
      <td></td>
      <td>5.40</td>
      <td>6.02</td>
      <td>6.40⁷⁴</td>
      <td></td>
    </tr>
    <tr>
      <td>h-BN</td>
      <td>5.7</td>
      <td>6.41</td>
      <td>7.27</td>
      <td>7.52</td>
      <td>7.40⁷⁵</td>
      <td>7.00-8.43⁶¹,⁷⁵,⁹⁶,⁹⁷</td>
    </tr>
    <tr>
      <td>MAE(eV)</td>
      <td>1.28</td>
      <td>0.79</td>
      <td>0.58</td>
      <td>0.18</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>MARE(%)</td>
      <td>29.4</td>
      <td>21.1</td>
      <td>17.9</td>
      <td>5.4</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

ᵃ $G_0W_0$@LDA;
ᵇ Results obtained with lattice parameters different from those of Table 2 or $GW$ approximation different from $G_0W_0$@PBE;
ᶜ Kinetic energy cutoff: 70 Ry

![](./images/1229361484681707553_7.jpg)

Figure 7: Upper panel: The state-dependent screening $\epsilon_i$ (Eq. 21) as a function of the state index for selected bands (V and C denote VBM and CBM respectively) for monolayer BP (left) and GaN (right). The dashed lines show the values of the long-wavelength dielectric constant of the 3D bulk ($\epsilon_{\text{bulk}}$). Bottom panel: Single-particle eigenvalues referenced to vacuum computed with the DDH$^{31}$ and SE-DDH$^{45}$ functionals, and the SE-RSH functional proposed in this work. Calculations with the DDH functional were performed with $\alpha = 1/\epsilon_{\text{bulk}}$.

accurate band gaps. It usually yields larger band gaps than SE-DDH, aligning more closely with the $GW$ results. This effect is particularly pronounced for ML-GaAs, illustrating that the underestimation of band gaps in systems with localized semicore d states by SE-DDH, previously observed in semiconductor heterojunctions, is also evident in two-dimensional systems.

Although Ref. 71,74 mainly attribute the failure of DDH to the inability to describe the weak screening of the vacuum surrounding 2D systems, we find that in some cases simply using a local dielectric function $\epsilon(\mathbf{r})$ does not improve the band gaps obtained with DDH. For example, in monolayer BP system, both SE-DDH and DDH predicts a band gap $\simeq 1.3$ eV, while the $G_0W_0@$PBE value is 1.8 eV.

To understand these results, we further consider the electronic structures of two representative monolayers: BP and GaN, and we define state-dependent screening parameters as

$$
\epsilon_{i}=\int \epsilon(\mathbf{r})\left|\phi_{i}(\mathbf{r})\right|^{2} \mathrm{d} \mathbf{r} \tag{21}
$$

to obtain an estimate of the effect of screening on each band.

Fig.(7) shows the variation of computed band edges as a function of the exchange-correlation functionals, along with the state-dependent screenings of several bands (VBM and CBM are the highest occupied and lowest unoccupied bands, respectively). For monolayer BP, the screening of both VBM and CBM is close to $\epsilon_{\text{bulk}}^{\text{BP}}$, and SE-DDH and DDH yield similar results. However, for monolayer GaN, the screening of VBM and CBM are smaller than $\epsilon_{\text{bulk}}^{\text{GaN}}$ and SE-DDH yields higher CBM and VBM than DDH and also a larger band gap. For both BP and GaAs, SE-RSH further increases the band gap and yields more accurate results.

The above examples illustrate that in certain low-dimensional systems, electronic states may be subject to bulk-like screening when the in-plane macroscopic dielectric constant of the monolayerr is similar to $\epsilon_{\infty}$ of the 3D bulk. $^{100}$ In this case, it is the inaccurate description of short-range screening that may lead to the failure of DDH.

### 3.4 Defects in 2D systems

In the literature, several first-principle calculations of the electronic structure of defects in
3D systems have been performed using a global hybrid functional, known as PBE0($\alpha$),$^{101}$
where the amount of Fock exchange admixed with semilocal exchange is controlled by a
single parameter $\alpha$; the latter is determined by fitting the experimental value of the band
gap of the host system.

However, such a scheme often fails for 2D systems.$^{71}$ Here, we investigate various point
defects in monolayer systems, including a single carbon atom substituting sulfur ($\text{C}_\text{S}$) in
monolayer $\text{WS}_2$ and substituting boron ($\text{C}_\text{B}$) in monolayer h-BN.

Fig.(8) shows the computed single-particle eigenvalues referenced to vacuum obtained

![](./images/1229361484681707553_8.jpg)

Figure 8: Upper panel: The state-dependent screening $\epsilon_i$ (Eq. 21) is plotted as a function
of state index (V, D and C denote VBM, defect state and CBM respectively). The dashed
lines represent the macroscopic dielectric constant of the corresponding bulk systems. Lower
panel: Single-particle eigenvalues with respect to the vacuum level. For each system, SE-
RSH and PBE0($\alpha$) results are compared against $G_0W_0$ reference results.

with different electronic structure methods, including $G_0W_0@\text{PBE}$. Also showed in Fig.(8)
is the state-dependent screening defined in Eq.(21).

We found that for the two defective systems studied here, PBE0($\alpha$) predicts qualitatively

inaccurate results compared to $GW$. In the case of ML h-BN, for example, $\text{PBE0}(\alpha)$ would incorrectly predict one defect state to be above the CBM. This result may stem from the differences in dielectric screening experienced by the defect states and the band edges of the material. As illustrated in the upper panel of Fig.(8), the CBM of ML h-BN is exposed to a weaker screening than the defect states and the VBM, and hence a mixing fraction determined solely from the band gap of ML h-BN is likely too large to accurately describe defect levels.

In the case of ML WS2, the discrepancy between $\text{PBE0}(\alpha)$ and SE-RSH or $GW$ results arises not only from the difference in dielectric screening experienced by different electronic states, but also from the difference in the level of orbital localization, in particular the d orbitals of W contributing to the VBM and CBM.

Unlike PBE0, SE-RSH can effectively differentiate between diverse electronic states based on their respective environments and underlying physics and hence yields more accurate results.

### 3.5 Finite Systems
Similar to the case of low dimensional systems, DDH is not expected to be accurate for finite systems such as nanoparticles. A generalization of DDH to finite systems was proposed by Brawand et al. $^{33}$ (we call this generalization SX), with:

$$
v_{x c}^{\mathrm{SX}}\left(\mathbf{r}, \mathbf{r}^{\prime}\right)=\alpha^{\mathrm{SX}} \Sigma_{x}\left(\mathbf{r}, \mathbf{r}^{\prime}\right)+\left(1-\alpha^{\mathrm{SX}}\right) v_{x}(\mathbf{r})+v_{c}(\mathbf{r}), \tag{22}
$$

where $\alpha^{\mathrm{SX}}$ is the screened-exchange constant:

$$
\alpha^{\mathrm{SX}}=\frac{\sum_{j}^{N}\left\langle j\left|\Sigma_{\mathrm{SEX}}\right| j\right\rangle}{\sum_{j}^{N}\left\langle j\left|\Sigma_{x}\right| j\right\rangle}. \tag{23}
$$

![](./images/1229361484681707553_9.jpg)

Figure 9: Upper panel: The screening (Eq. 21) and inverse participation ratio (IPR) of the highest occupied molecular orbital (HOMO) as a function of the number of Si atoms in the core of hydrogen-passivated silicon clusters. Bottom panel: The fundamental gaps of hydrogen-passivated silicon clusters as a function of the number of Si atoms in the core, predicted using SE-RSH, SE-DDH, $^{45}$ SX $^{33}$ and HSE06. $^{28,29}$ Fundamental gaps obtained from $G_0W_0$ starting from PBE wave functions ($G_0W_0$@PBE) are included for comparison.

The SX functional is, in spirit, similar to SE-RSH since the mixing fraction $\alpha^{\text{SX}}$ is also designed to replace the non-local exchange potential with the screened-exchange self-energy $\Sigma_{\text{SEX}}$. However it is less general than SE-RSH.

Fig.(9) presents the fundamental gaps of several hydrogen-passivated silicon clusters, computed using various methods and plotted against the number of Si atoms within the cluster core, using the structural models of Ref. 102. The Mean Absolute Error (MAE) of SE-RSH with respect to $G_0W_0$@PBE is found to be approximately 0.19 eV, as compared to 0.27, 0.53 and 1.14 eV for SX, SE-DDH and HSE06, respectively. The PBE functional markedly underestimates the gap of these clusters, with a MAE of 1.58 eV. Interestingly, the fundamental gaps predicted by HSE are consistently shifted by about 0.8 eV relative to the corresponding PBE values, suggesting a similar description of quantum confinement effects by the two functionals, albeit distinct from that obtained from the $GW$ approximation.

In Fig.(9) we also present the state-dependent screening values as well as the inverse participation ratio of the highest occupied orbitals, defined as $\text{IPR}_{\text{HOMO}} = \int |\phi_{\text{HOMO}}(\mathbf{r})|^4\text{d}\mathbf{r}$.

A higher IPR value indicates a more localized single particle wave function. We can see that as the size of the system is reduced, $\epsilon_{\text{HOMO}}$ decreases. Such a change leads to a size-dependent correction, relative to PBE, obtained with both SE-DDH and SE-RSH. However, SE-DDH becomes more inaccurate as the IPR increases, while SE-RSH provides a consistently accurate description of the gaps for all molecules, demonstrating the accuracy of SE-RSH in dealing with strongly localized electronic systems and the importance of enhanced short-range Fock exchange for finite systems.

## 4 Conclusions

In this work, we generalized the definition of range-separated hybrid functionals to heteroge- neous systems by defining a non-empirical functional (SE-RSH), where the mixing fraction of exact and local exchange depends on a spatially dependent local dielectric function and a local screening function. The definition of SE-RSH is inspired by the static COHSEX approximation, $^{46}$ used in many body perturbation theory. Using the SE-RSH, we obtained electronic energy gaps and band offsets in good agreement with experimental data for both homogeneous and heterogeneous three-dimensional systems, and in excellent agreement with $GW$ calculations for pristine and defective two-dimensional systems as well as silicon clusters for which measurements are currently unavailable. This good agreement stems from the abil- ity of the SE-RSH functional to account for the different screening experienced by different electronic states and by an accurate description of both localized and delocalized electronic states. Given its accuracy and its derivation without any empirical parameters, the SE-RSH functional is particularly well-suited for high-throughput calculations of heterogeneous sys- tems. Additionally, research is currently underway to explore the integration of the SE-RSH functional with time-dependent DFT (TDDFT) $^{103,104}$ calculations, thus enabling efficient investigations of excited-state properties and optical response in complex materials.

### Supporting Information Available

Details of implementation, including the procedure to obtain a coarse-grained approximation of the local screening function $\mu(\mathbf{r})$ as well as the method to handle the integrable divergence of the exchange energy.

### Acknowledgement

We thank Francois Gygi, Yu Jin and Huihuo Zheng for many useful discussions. This work was supported by DOE/BES through the computational materials science center Midwest Integrated Center for Computational Materials (MICCoM). The computational resources were provided by University of Chicago's Research Computing Center.

### References

(1) Mannhar, J.; Herrnberger, A. The interface is still the device. *Nat. Mater.* **2012**, *11*, 91.

(2) Hohenberg, P.; Kohn, W. Inhomogeneous Electron Gas. *Physical Review* **1964**, *136*, B864-B871.

(3) Kohn, W.; Sham, L. J. Self-Consistent Equations Including Exchange and Correlation Effects. *Physical Review* **1965**, *140*, A1133-A1138.

(4) Teale, A. M.; Helgaker, T.; Savin, A.; Adamo, C.; Aradi, B.; Arbuznikov, A. V.; Ayers, P. W.; Baerends, E. J.; Barone, V.; Calaminici, P., et al. DFT exchange: sharing perspectives on the workhorse of quantum chemistry and materials science. *Physical chemistry chemical physics* **2022**, *24*, 28700-28781.

(5) Cohen, A. J.; Mori-Sánchez, P.; Yang, W. Challenges for density functional theory. *Chemical reviews* **2012**, *112*, 289-320.

(6) Verma, P.; Truhlar, D. G. Status and challenges of density functional theory. *Trends in Chemistry* **2020**, *2*, 302-318.

(7) Hinuma, Y.; Grüneis, A.; Kresse, G.; Oba, F. Band alignment of semiconductors from density-functional theory and many-body perturbation theory. *Physical Review B* **2014**, *90*, 155405.

(8) Ghosh, A.; Jana, S.; Rauch, T.; Tran, F.; Marques, M. A.; Botti, S.; Constantin, L. A.; Niranjan, M. K.; Samal, P. Efficient and improved prediction of the band offsets at semiconductor heterojunctions from meta-GGA density functionals: A benchmark study. *The Journal of Chemical Physics* **2022**, *157*, 124108.

(9) Kroemer, H. Nobel Lecture: Quasielectric fields and band offsets: teaching electrons new tricks. *Reviews of modern physics* **2001**, *73*, 783.

(10) Grätzel, M. Photoelectrochemical cells. *nature* **2001**, *414*, 338-344.

(11) Hedin, L. New Method for Calculating the One-Particle Green's Function with Appli- cation to the Electron-Gas Problem. *Physical Review* **1965**, *139*, A796-A823.

(12) Martin, R. M.; Reining, L.; Ceperley, D. M. *Interacting Electrons: Theory and Computational Approaches*; Cambridge University Press, 2016.

(13) Georges, A.; Kotliar, G.; Krauth, W.; Rozenberg, M. J. Dynamical mean-field theory of strongly correlated fermion systems and the limit of infinite dimensions. *Reviews of Modern Physics* **1996**, *68*, 13.

(14) Kotliar, G.; Savrasov, S. Y.; Haule, K.; Oudovenko, V. S.; Parcollet, O.; Marianetti, C. Electronic structure calculations with dynamical mean-field theory. *Reviews of Modern Physics* **2006**, *78*, 865.

(15) Becca, F.; Sorella, S. *Quantum Monte Carlo approaches for correlated systems*; Cam- bridge University Press, 2017.

(16) Kulik, H.; Hammerschmidt, T.; Schmidt, J.; Botti, S.; Marques, M.; Boley, M.; Schef- fler, M.; Todorović, M.; Rinke, P.; Oses, C., et al. Roadmap on machine learning in electronic structure. *Electronic Structure* **2022**, 4, 023004.

(17) Kohn, W.; Sham, L. J. Self-consistent equations including exchange and correlation effects. *Physical review* **1965**, 140, A1133.

(18) Ceperley, D. M.; Alder, B. J. Ground state of the electron gas by a stochastic method. *Physical review letters* **1980**, 45, 566.

(19) Perdew, J. P.; Zunger, A. Self-interaction correction to density-functional approxima- tions for many-electron systems. *Physical Review B* **1981**, 23, 5048.

(20) Perdew, J. P.; Wang, Y. Accurate and simple analytic representation of the electron- gas correlation energy. *Physical review B* **1992**, 45, 13244.

(21) Perdew, J. P.; Burke, K.; Ernzerhof, M. Generalized Gradient Approximation Made Simple. *Physical Review Letters* **1996**, 77, 3865–3868.

(22) Perdew, J. P.; Chevary, J. A.; Vosko, S. H.; Jackson, K. A.; Pederson, M. R.; Singh, D. J.; Fiolhais, C. Atoms, molecules, solids, and surfaces: Applications of the generalized gradient approximation for exchange and correlation. *Physical Review B* **1991**, 46, 6671–6687.

(23) Maier, T. M.; Arbuznikov, A. V.; Kaupp, M. Local hybrid functionals: Theory, im- plementation, and performance of an emerging new tool in quantum chemistry and beyond. *Wiley Interdisciplinary Reviews: Computational Molecular Science* **2019**, 9.

(24) Becke, A. D. A new mixing of Hartree–Fock and local density-functional theories. *The Journal of Chemical Physics* **1993**, 98, 1372–1377.

(25) Jaramillo, J.; Scuseria, G. E.; Ernzerhof, M. Local hybrid functionals. *The Journal of Chemical Physics* **2003**, 118, 1068–1073.

(26) Ghosh, S.; Verma, P.; Cramer, C. J.; Gagliardi, L.; Truhlar, D. G. Combining Wave Function Methods with Density Functional Theory for Excited States. *Chemical Re- views* **2018**, *118*, 7249–7292.

(27) Adamo, C.; Barone, V. Toward reliable density functional methods without adjustable parameters: The PBE0 model. *The Journal of chemical physics* **1999**, *110*, 6158–6170.

(28) Heyd, J.; Scuseria, G. E.; Ernzerhof, M. Hybrid functionals based on a screened Coulomb potential. *The Journal of Chemical Physics* **2003**, *118*, 8207–8215.

(29) Heyd, J.; Scuseria, G. E.; Ernzerhof, M. Erratum: "Hybrid functionals based on a screened Coulomb potential" [J. Chem. Phys. 118, 8207 (2003)]. *The Journal of Chemical Physics* **2006**, *124*, 219906.

(30) Krukau, A. V.; Vydrov, O. A.; Izmaylov, A. F.; Scuseria, G. E. Influence of the exchange screening parameter on the performance of screened hybrid functionals. *The Journal of Chemical Physics* **2006**, *125*, 224106.

(31) Skone, J. H.; Govoni, M.; Galli, G. Self-consistent hybrid functional for condensed systems. *Phys. Rev. B* **2014**, *89*, 195112.

(32) Marques, M. A. L.; Vidal, J.; Oliveira, M. J. T.; Reining, L.; Botti, S. Density-based mixing parameter for hybrid functionals. *Physical Review B* **2011**, *83*, 035119.

(33) Brawand, N. P.; Govoni, M.; Vörös, M.; Galli, G. Performance and Self-Consistency of the Generalized Dielectric Dependent Hybrid Functional. *Journal of Chemical Theory and Computation* **2017**, *13*, 3318–3325.

(34) Skone, J. H.; Govoni, M.; Galli, G. Nonempirical range-separated hybrid functionals for solids and molecules. *Physical Review B* **2016**, *93*, 235106.

(35) Gaiduk, A. P.; Pham, T. A.; Govoni, M.; Paesani, F.; Galli, G. Electron affinity of liquid water. *Nature Communications* **2018**, *9*, 247.

(36) Pham, T. A.; Govoni, M.; Seidel, R.; Bradforth, S. E.; Schwegler, E.; Galli, G. Elec- tronic structure of aqueous solutions: Bridging the gap between theory and experi- ments. *Science Advances* **2017**, 3, e1603210.

(37) Borghi, G.; Ferretti, A.; Nguyen, N. L.; Dabo, I.; Marzari, N. Koopmans-compliant functionals and their performance against reference molecular data. *Physical Review B* **2014**, 90, 075135.

(38) Colonna, N.; Nguyen, N. L.; Ferretti, A.; Marzari, N. Koopmans-Compliant Function- als and Potentials and Their Application to the GW100 Test Set. *Journal of Chemical Theory and Computation* **2019**, 15, 1905–1914.

(39) Nguyen, N. L.; Colonna, N.; Ferretti, A.; Marzari, N. Koopmans-compliant spectral functionals for extended systems. *Physical Review X* **2018**, 8, 021051.

(40) Colonna, N.; De Gennaro, R.; Linscott, E.; Marzari, N. Koopmans Spectral Function- als in Periodic Boundary Conditions. *Journal of Chemical Theory and Computation* **2022**, 18, 5435–5448.

(41) Li, C.; Zheng, X.; Su, N. Q.; Yang, W. Localized orbital scaling correction for system- atic elimination of delocalization error in density functional approximations. *National Science Review* **2018**, 5, 203–215.

(42) Mahler, A.; Williams, J.; Su, N. Q.; Yang, W. Localized orbital scaling correction for periodic systems. *Physical Review B* **2022**, 106, 035147.

(43) Shimazaki, T.; Nakajima, T. Theoretical study of a screened Hartree–Fock exchange potential using position-dependent atomic dielectric constants. *The Journal of Chem- ical Physics* **2015**, 142, 074109.

(44) Borlido, P.; Marques, M. A. L.; Botti, S. Local Hybrid Density Functional for Inter- faces. *Journal of Chemical Theory and Computation* **2018**, 14, 939–947.

(45) Zheng, H.; Govoni, M.; Galli, G. Dielectric-dependent hybrid functionals for hetero- geneous materials. *Physical Review Materials* **2019**, *3*, 073803.

(46) Hybertsen, M. S.; Louie, S. G. First-Principles Theory of Quasiparticles: Calculation of Band Gaps in Semiconductors and Insulators. *Phys. Rev. Lett.* **1985**, *55*, 1418–1421.

(47) Leininger, T.; Stoll, H.; Werner, H.-J.; Savin, A. Combining long-range configuration interaction with short-range density functionals. *Chemical physics letters* **1997**, *275*, 151–160.

(48) Vydrov, O. A.; Scuseria, G. E. Assessment of a long-range corrected hybrid functional. *The Journal of Chemical Physics* **2006**, *125*, 234109.

(49) Vydrov, O. A.; Heyd, J.; Krukau, A. V.; Scuseria, G. E. Importance of short-range versus long-range Hartree-Fock exchange for the performance of hybrid density func- tionals. *The Journal of chemical physics* **2006**, *125*.

(50) Yanai, T.; Tew, D. P.; Handy, N. C. A new hybrid exchange–correlation functional us- ing the Coulomb-attenuating method (CAM-B3LYP). *Chemical physics letters* **2004**, *393*, 51–57.

(51) Chai, J.-D.; Head-Gordon, M. Long-range corrected hybrid density functionals with damped atom–atom dispersion corrections. *Physical Chemistry Chemical Physics* **2008**, *10*, 6615–6620.

(52) Stein, T.; Kronik, L.; Baer, R. Reliable prediction of charge transfer excitations in molecular complexes using time-dependent density functional theory. *Journal of the American Chemical Society* **2009**, *131*, 2818–2820.

(53) Baer, R.; Livshits, E.; Salzner, U. Tuned range-separated hybrids in density functional theory. *Annual review of physical chemistry* **2010**, *61*, 85–109.

(54) Chen, W.; Miceli, G.; Rignanese, G.-M.; Pasquarello, A. Nonempirical dielectric-dependent hybrid functional with range separation for semiconductors and insulators. *Physical Review Materials* **2018**, *2*, 073803.

(55) Ernzerhof, M.; Perdew, J. P. Generalized gradient approximation to the angle- and system-averaged exchange hole. *The Journal of Chemical Physics* **1998**, *109*, 3313–3320.

(56) Gygi, F.; Baldereschi, A. Self-consistent Hartree-Fock and screened-exchange calculations in solids: Application to silicon. *Physical Review B* **1986**, *34*, 4405.

(57) Stengel, M.; Spaldin, N. A. Accurate polarization within a unified Wannier function formalism. *Phys. Rev. B* **2006**, *73*, 075121.

(58) Souza, I.; Íñiguez, J.; Vanderbilt, D. First-Principles Approach to Insulators in Finite Electric Fields. *Phys. Rev. Lett.* **2002**, *89*, 117602.

(59) Stengel, M.; Spaldin, N. A. Accurate polarization within a unified Wannier function formalism. *Physical Review B* **2006**, 075121.

(60) Gaiduk, A. P.; Pham, T. A.; Govoni, M.; Paesani, F.; Galli, G. Electron affinity of liquid water. *Nature communications* **2018**, *9*, 1–6.

(61) Hüser, F.; Olsen, T.; Thygesen, K. S. Quasiparticle GW calculations for solids, molecules, and two-dimensional materials. *Physical Review B* **2013**, *87*, 235132.

(62) Wilson, H. F.; Gygi, F.; Galli, G. Efficient iterative method for calculations of dielectric matrices. *Physical Review B* **2008**, *78*, 113303.

(63) Govoni, M.; Galli, G. Large scale GW calculations. *Journal of Chemical Theory and Computation* **2015**, *11*, 2680–2696.

(64) Govoni, M.; Galli, G. Large scale GW calculations. *Journal of chemical theory and computation* **2015**, *11*, 2680–2696.

(65) Yu, V. W.-z.; Govoni, M. GPU Acceleration of Large-Scale Full-Frequency GW Calculations. *Journal of Chemical Theory and Computation* **2022**, *18*, 4690–4707.

(66) Gygi, F. Architecture of Qbox: A scalable first-principles molecular dynamics code. *IBM Journal of Research and Development* **2008**, *52*, 137–144.

(67) Hamann, D. Optimized norm-conserving Vanderbilt pseudopotentials. *Physical Review B* **2013**, *88*, 085117.

(68) Şahin, H.; Cahangirov, S.; Topsakal, M.; Bekaroglu, E.; Akturk, E.; Senger, R. T.; Ciraci, S. Monolayer honeycomb structures of group-IV elements and III-V binary compounds: First-principles calculations. *Phys. Rev. B* **2009**, *80*, 155453.

(69) Tran, V.; Sokolski, R.; Liang, Y.; Yang, L. Layer-controlled band gap and anisotropic excitons in few-layer black phosphorus. *Phys. Rev. B* **2014**, *89*, 235319.

(70) Hüser, F.; Olsen, T.; Thygesen, K. S. How dielectric screening in two-dimensional crystals affects the convergence of excited-state calculations: Monolayer MoS 2. *Physical Review B* **2013**, *88*, 245309.

(71) Chen, W.; Griffin, S. M.; Rignanese, G.-M.; Hautier, G. Nonunique fraction of Fock exchange for defects in two-dimensional materials. *Physical Review B* **2022**, *106*, L161107.

(72) Fakhrabad, D. V.; Shahtamasebi, N.; Ashhadi, M. Quasiparticle energies and optical excitations in the GaAs monolayer. *Physica E: Low-dimensional Systems and Nanostructures* **2014**, *59*, 107–109.

(73) Shu, H.; Niu, X.; Ding, X.; Wang, Y. Effects of strain and surface modification on stability, electronic and optical properties of GaN monolayer. *Applied Surface Science* **2019**, *479*, 475–481.

(74) Smart, T. J.; Wu, F.; Govoni, M.; Ping, Y. Fundamental principles for calculating charged defect ionization energies in ultrathin two-dimensional materials. *Phys. Rev. Mater.* **2018**, *2*, 124002.

(75) Berseneva, N.; Gulans, A.; Krasheninnikov, A. V.; Nieminen, R. M. Electronic structure of boron nitride sheets doped with carbon from first-principles calculations. *Phys. Rev. B* **2013**, *87*, 035404.

(76) Pham, T. A.; Li, T.; Nguyen, H.-V.; Shankar, S.; Gygi, F.; Galli, G. Band offsets and dielectric properties of the amorphous Si3N4/Si(100) interface: A first-principles study. *Applied Physics Letters* **2013**, *102*, 241603.

(77) Bersch, E.; Di, M.; Consiglio, S.; Clark, R.; Leusink, G.; Diebold, A. C. Complete band offset characterization of the HfO 2/SiO 2/Si stack using charge corrected x-ray photoelectron spectroscopy. *Journal of Applied Physics* **2010**, *107*, 043702.

(78) Yamasaki, T.; Kaneta, C.; Uchiyama, T.; Uda, T.; Terakura, K. Geometric and electronic structures of Si O 2/Si (001) interfaces. *Physical Review B* **2001**, *63*, 115314.

(79) Weston, L.; Tailor, H.; Krishnaswamy, K.; Bjaalie, L.; Van de Walle, C. Accurate and efficient band-offset calculations from density functional theory. *Computational Materials Science* **2018**, *151*, 174–180.

(80) Bischoff, T.; Reshetnyak, I.; Pasquarello, A. Band gaps of liquid water and hexagonal ice through advanced electronic-structure calculations. *Physical Review Research* **2021**, *3*, 023182.

(81) Keister, J.; Rowe, J.; Kolodziej, J.; Niimi, H.; Madey, T.; Lucovsky, G. Band offsets for ultrathin SiO 2 and Si 3 N 4 films on Si (111) and Si (100) from photoemission spectroscopy. *Journal of Vacuum Science & Technology B: Microelectronics and Nanometer Structures Processing, Measurement, and Phenomena* **1999**, *17*, 1831–1835.

(82) Steiner, K.; Chen, W.; Pasquarello, A. Band offsets of lattice-matched semiconductor heterojunctions through hybrid functionals and G 0 W 0. *Physical Review B* **2014**, *89*, 205309.

(83) Van de Walle, C. G.; Martin, R. M. Theoretical study of band offsets at semiconductor interfaces. *Physical Review B* **1987**, *35*, 8154.

(84) Tran, F.; Blaha, P. Accurate Band Gaps of Semiconductors and Insulators with a Semilocal Exchange-Correlation Potential. *Phys. Rev. Lett.* **2009**, *102*, 226401.

(85) Ryou, J.; Kim, Y.-S.; Kc, S.; Cho, K. Monolayer MoS2 Bandgap Modulation by Dielectric Environments and Tunable Bandgap Transistors. *Scientific reports* **2016**, *6*, 29184.

(86) Liang, L.; Wang, J.; Lin, W.; Sumpter, B. G.; Meunier, V.; Pan, M. Electronic bandgap and edge reconstruction in phosphorene materials. *Nano letters* **2014**, *14*, 6400-6406.

(87) Chen, Y.; Quek, S. Y. Tunable bright interlayer excitons in few-layer black phosphorus based van der Waals heterostructures. *2D Materials* **2018**, *5*, 045031.

(88) Cheiwchanchamnangij, T.; Lambrecht, W. R. Quasiparticle band structure calculation of monolayer, bilayer, and bulk MoS 2. *Physical Review B* **2012**, *85*, 205302.

(89) Shi, H.; Pan, H.; Zhang, Y.-W.; Yakobson, B. I. Quasiparticle band structures and optical properties of strained monolayer MoS 2 and WS 2. *Physical Review B* **2013**, *87*, 155304.

(90) Jin, C.; Rasmussen, F. A.; Thygesen, K. S. Tuning the Schottky barrier at the graphene/MoS2 interface by electron doping: density functional theory and many-body calculations. *The Journal of Physical Chemistry C* **2015**, *119*, 19928-19933.

(91) Wang, L.; Kutana, A.; Yakobson, B. I. Many-body and spin-orbit effects on direct-indirect band gap transition of strained monolayer MoS2 and WS2. *Annalen der Physik* 2014, 526, L7-L12.

(92) Mishra, H.; Bhattacharya, S. Exciton-driven giant nonlinear overtone signals from buckled hexagonal monolayer GaAs. *Physical Review B* 2020, 101, 155132.

(93) Chen, Q.; Hu, H.; Chen, X.; Wang, J. Tailoring band gap in GaN sheet by chemical modification and electric field: Ab initio calculations. *Applied Physics Letters* 2011, 98, 053102.

(94) Vahedi, D.; Shahtahmassebi, N.; Ashhadi, M. Optical excitations and quasiparticle energies in the AlN monolayer honeycomb structure. *Superlattices and Microstructures - Micro and Nanostructures* 2015, 79, 38-44.

(95) Karami, I.; Ketabi, S. Tuning of the electronic and optical properties of AlN monolayer by fluorination: Study of many-body effects. *Computational Condensed Matter* 2021, 28, e00564.

(96) Attaccalite, C.; Bockstedte, M.; Marini, A.; Rubio, A.; Wirtz, L. Coupling of excitons and defect states in boron-nitride nanostructures. *Physical Review B* 2011, 83, 144115.

(97) Román, R. J. P.; Costa, F. J. C.; Zobelli, A.; Elias, C.; Valvin, P.; Cassabois, G.; Gil, B.; Summerfield, A.; Cheng, T. S.; Mellor, C. J., et al. Band gap measurements of monolayer h-BN and insights into carbon-related point defects. *2D Materials* 2021, 8, 044001.

(98) Perdew, J. P.; Parr, R. G.; Levy, M.; Balduz, J. L. Density-Functional Theory for Fractional Particle Number: Derivative Discontinuities of the Energy. *Physical Review Letters* 1982, 49, 1691-1694.

(99) Perdew, J. P.; Yang, W.; Burke, K.; Yang, Z.; Gross, E. K.; Scheffler, M.; Scuse- ria, G. E.; Henderson, T. M.; Zhang, I. Y.; Ruzsinszky, A., et al. Understanding band gaps of solids in generalized Kohn-Sham theory. *Proceedings of the national academy of sciences* **2017**, *114*, 2801–2806.

(100) Laturia, A.; Van de Put, M. L.; Vandenberghe, W. G. Dielectric properties of hexag- onal boron nitride and transition metal dichalcogenides: from monolayer to bulk. *npj 2D Materials and Applications* **2018**, *2*, 6.

(101) Miceli, G.; Chen, W.; Reshetnyak, I.; Pasquarello, A. Nonempirical hybrid functionals for band gaps and polaronic distortions in solids. *Physical Review B* **2018**, *97*, 121112.

(102) Brawand, N.; Vörös, M.; Govoni, M.; Galli, G. Generalization of Dielectric-Dependent Hybrid Functionals to Finite Systems. *Physical Review X* **2016**, *6*.

(103) Runge, E.; Gross, E. K. Density-functional theory for time-dependent systems. *Phys- ical review letters* **1984**, *52*, 997.

(104) Jin, Y.; Govoni, M.; Galli, G. Vibrationally resolved optical excitations of the nitrogen- vacancy center in diamond. *npj Computational Materials* **2022**, *8*, 238.

# Supporting Information: Nonempirical
Range-Separated Hybrid Functional with
Spatially Dependent Screened Exchange

Jiawei Zhan, $^\dagger$ Marco Govoni, $^{\dagger,\ddagger,\P}$ and Giulia Galli$^{*,\dagger,\ddagger,\S}$

$^\dagger$Pritzker School of Molecular Engineering, University of Chicago, Chicago, Illinois 60637,
United States

$^\ddagger$Materials Science Division and Center for Molecular Engineering, Argonne National
Laboratory, Lemont, Illinois 60439, United States

$^\P$Department of Physics, Computer Science, and Mathematics, University of Modena and
Reggio Emilia, Modena, 41125, Italy

$^\S$Department of Chemistry, University of Chicago, Chicago, Illinois 60637, United States

E-mail: gagalli@uchicago.edu

## Coarse-Grained Approximation of $\mu(\mathbf{r})$

In SE-RSH, the exchange energy $E_{x,i}$ associated to the state $\phi_i$ is:

$$
E_{x,i} = \sum_j \iint \frac{\alpha(\mathbf{r},\mathbf{r}')\rho_{ij}^*(\mathbf{r}')\rho_{ij}(\mathbf{r})}{|\mathbf{r}-\mathbf{r}'|} \mathrm{d}\mathbf{r}\mathrm{d}\mathbf{r}', \tag{1}
$$

where $\alpha(\mathbf{r},\mathbf{r}')$ is the mixing fraction introduced in Eq.(6) of the main text and $\rho_{ij}(\mathbf{r}) = \phi_i^*(\mathbf{r})\phi_j(\mathbf{r})$. The short range exchange energy $E_{x,i}^\text{SR}$ is:

$$
E_{x,i}^\text{SR} = \sum_{j} \iint \frac{\operatorname{erfc}\left(\mu(\mathbf{r})|\mathbf{r}-\mathbf{r}'|\right) \rho_{ij}^*(\mathbf{r}') \rho_{ij}(\mathbf{r})}{|\mathbf{r}-\mathbf{r}'|} \mathrm{d}\mathbf{r}\mathrm{d}\mathbf{r}'. \tag{2}
$$

Eq.(2) is computationally intractable for an arbitrary function $\mu(\mathbf{r})$. We represent $\mu(\mathbf{r})$ as:

$$
\mu(\mathbf{r}) = \sum_{\mathbf{r}_0} \mu(\mathbf{r}_0)\delta(\mathbf{r}-\mathbf{r}_0), \tag{3}
$$

where $\mathbf{r}_0$ is a grid point in real space; Eq.(2) becomes:

$$
E_{x,i}^\text{SR} = \sum_{\mathbf{r}_0;j,\mathbf{G}} \frac{\rho_{ij;\mathbf{r}_0}^*(\mathbf{G}) \rho_{ij}(\mathbf{G})}{|\mathbf{G}|^2} \left(1 - e^{-\frac{|\mathbf{G}|^2}{4\mu(\mathbf{r}_0)^2}}\right), \tag{4}
$$

where $\rho_{ij}(\mathbf{G})$ and $\rho_{ij,\mathbf{r}_0}(\mathbf{G})$ are the Fourier components of $\rho_{ij}(\mathbf{r})$ and $\rho_{ij}(\mathbf{r})\delta(\mathbf{r}-\mathbf{r}_0)$, respectively. The computational cost of Eq.(4) is then proportional to the number of grid points $(\mathbf{r}_0)$, used to represent $\mu(\mathbf{r})$.

We adopt a coarse-grained approximation to the function $\mu(\mathbf{r})$:

$$
\mu(\mathbf{r}) \approx \sum_{t} \mu_t f_t(\mathbf{r}), \tag{5}
$$

where:

$$
f_t(\mathbf{r}) = \begin{cases}
1 \text{ if } \mathbf{r} \in \Omega_t \\
0 \text{ else where}
\end{cases} \tag{6}
$$

$$
\mu_t = 1/\Omega_t \int \mu(\mathbf{r}) f_t(\mathbf{r})\mathrm{d}\mathbf{r},
$$

and $\{f_t(\mathbf{r})\}$ are projectors defined in the volume $\{\Omega_t\}$, and $\{\mu_t\}$ are the average of the function $\mu(\mathbf{r})$ in $\{\Omega_t\}$.

The algorithm used here to obtain $\{f_t(\mathbf{r})\}$ and $\{\mu_t\}$, called Adaptive Binning (AB), is the following:

1. Evaluate $\mu(\mathbf{r})$ on the real space grid used to represent the charge density.

2. If the standard deviation $(\sigma)$ of $\mu(\mathbf{r})$ is less than $0.1 \times \overline{\mu(\mathbf{r})}$ (see below), where $\overline{\mu(\mathbf{r})}$ is the mean value of $\mu(\mathbf{r})$, approximate $\mu(\mathbf{r})$ with $\overline{\mu(\mathbf{r})}$.

3. If $\sigma$ exceeds $0.1 \times \overline{\mu(\mathbf{r})}$:

(a) Partition $\mu(\mathbf{r})$ into N=2 bins.

(b) Compute the mean $\{\mu_t\}$ and standard deviation $\{\sigma_t\}$ of $\mu(\mathbf{r})$ in each bin.

(c) Increment the bin number (N) until the following inequality is satisfied: $|\mu_i - \mu_j| > \sigma_i + \sigma_j$, for any (i, j) bin pairs, where $1 \leq i < j \leq N$.

4. For all $\mathbf{r}$, the projector $f_t(\mathbf{r})$ associated to the $t^{th}$ bin is defined as 1 if $\mu(\mathbf{r})$ belongs to the $t^{th}$ bin, zero otherwise.The projectors satisfy the following properties: $f_i(\mathbf{r})f_j(\mathbf{r}) = f_i(\mathbf{r})\delta_{ij}$, and $\sum_i f_i(\mathbf{r}) = 1 \forall \mathbf{r}$.

Table (1) presents the variation of $\mu(\mathbf{r})$ observed in selected homogeneous 3D bulk systems and heterogeneous systems studied in this work. Based on these results, we have chosen $0.1 \times \overline{\mu(\mathbf{r})}$ as a reasonable threshold that appears to be sufficiently small to accurately describe variations in heterogeneous systems and not overly sensitive to fluctuations in homogeneous systems.

Fig.(1) compares the probability density function and the binned density of $\mu(\mathbf{r})$ for several heterogeneous systems, where bins are determined via the AB algorithm. The choice of how to subdivide the entire supercell into smaller volumes $\Omega_t$ and hence how to determine $\mu_t$ depends on the system. For example, we found that for the $\text{Si/Si}_3\text{N}_4$ interface a single constant parameter $\mu$ is sufficient and hence $\Omega_t$ is equal to the whole supercell. For 2D systems and nanoparticles we found instead that two or more $\mu_t$ paramters are required to obtain an accurate description of the short range component of the exchange and correlation. The use of Eq.(5) was inspired by previous results$^{1,2}$ showing that the results of electronic structure calculations with range separated hybrid functionals were relatively insensitive to

Table 1: The ratio between the standard deviation ($\sigma$) and the mean value $\overline{\mu(\mathbf{r})}$ of the function $\mu(\mathbf{r})$ in selected homogeneous and heterogeneous systems.

<table>
<thead>
  <tr>
    <th></th>
    <th>$\sigma/\overline{\mu(\mathbf{r})}$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Si</td>
    <td>0.06(3)</td>
  </tr>
  <tr>
    <td>SiO₂</td>
    <td>0.07(1)</td>
  </tr>
  <tr>
    <td>C</td>
    <td>0.01(9)</td>
  </tr>
  <tr>
    <td>SiC</td>
    <td>0.03(6)</td>
  </tr>
  <tr>
    <td>h-BN</td>
    <td>0.94(9)</td>
  </tr>
  <tr>
    <td>Si₃₅H₃₆</td>
    <td>0.94(6)</td>
  </tr>
  <tr>
    <td>Si/Si₃N₄</td>
    <td>0.08(7)</td>
  </tr>
  <tr>
    <td>H-Si/H₂O</td>
    <td>0.16(7)</td>
  </tr>
</tbody>
</table>

![](./images/1229361484681707553_10.jpg)

Figure 1: The dashed line and histogram show the probability density function and the binned density of $\mu(\mathbf{r})$, respectively, for a Si₃₅H₃₆ silicon cluster, monolayer h-BN, and model H-Si/H₂O and Si/Si₃N₄ interfaces. The bins are determined using the Adaptive Binning (AB) algorithm described in the text.

the choice of $\mu$.

We note that although the complexity of the calculations of the exchange integral of SE-RSH is the same as that of global hybrid functionals', the prefactor is $T$ times larger, where $T$ is the number of $\{\mu_t\}$ used to approximate the function $\mu(\mathbf{r})$. Hence it is desirable to keep $T$ as small as possible, avoiding unnecessary computational complexity.

The application of the short-range exchange operator to state $\phi_i$:

$$
\begin{aligned}
\left(\Sigma_{x}^{\mathrm{SR}} \phi_{i}\right)(\mathbf{r})= & \sum_{j} \phi_{j}(\mathbf{r}) \\
& \times \int \frac{\operatorname{erfc}(\mu(\mathbf{r})|\mathbf{r}-\mathbf{r}'|) \rho_{i j}^{*}(\mathbf{r}')}{|\mathbf{r}-\mathbf{r}'|} \mathrm{d} \mathbf{r}'
\end{aligned}
\tag{7}
$$

is also evaluated using a coarse-grained approximation of $\mu(\mathbf{r})$.

# Divergence in the Evaluation of Exchange Integrals

We define the function $F_{i j}(\mathbf{G})$:

$$
F_{i j}(\mathbf{G})=\iint \alpha\left(\mathbf{r}, \mathbf{r}^{\prime}\right) \rho_{i j}^{*}\left(\mathbf{r}^{\prime}\right) \rho_{i j}(\mathbf{r}) e^{i \mathbf{G} \cdot\left(\mathbf{r}-\mathbf{r}^{\prime}\right)} \mathrm{d} \mathbf{r} \mathrm{d} \mathbf{r}^{\prime},
\tag{8}
$$

and write the exchange energy $E_{x, i}$ as:

$$
E_{x, i}=\sum_{\mathbf{G}, j} \frac{F_{i j}(\mathbf{G})}{|\mathbf{G}|^{2}},
\tag{9}
$$

The divergence for $\mathbf{G} \rightarrow 0$ is integrated by generalizing the procedure proposed by Gygi et al. $^{3}$ An auxiliary function $A_{i}$ is constructed for each state $\phi_{i}$ as:

$$
\begin{aligned}
A_{i} & =\sum_{G} m_{i} \frac{e^{-\alpha|G|^{2}}}{|\mathbf{G}|^{2}} \\
& =m_{i} \frac{\Omega}{(2 \pi)^{3}} 2 \pi \sqrt{\frac{\pi}{\alpha}}
\end{aligned}
\tag{10}
$$


where $m_i = \sum_j F_{ij}(\mathbf{G}=0)$ and $\Omega$ is the volume of the supercell. Eq.(9) can then be rewritten as:

$$
\sum_{\mathbf{G}} \left[ \frac{\sum_j F_{ij}(\mathbf{G})}{|\mathbf{G}|^2} - m_i \frac{e^{-\alpha|G|^2}}{|\mathbf{G}|^2} \right] + m_i \frac{\Omega}{(2\pi)^3} 2\pi \sqrt{\frac{\pi}{\alpha}},
\tag{11}
$$

where

$$
\left[ \frac{\sum_j F_{ij}(\mathbf{G})}{|\mathbf{G}|^2} - m_i \frac{e^{-\alpha|G|^2}}{|\mathbf{G}|^2} \right]_{\mathbf{G}=0}
\tag{12}
$$

is a smooth differentiable function. Note that in the original formulation of Gygi et al.'s, $\alpha(\mathbf{r},\mathbf{r}')=1$ and hence, $m_i=1$.

## References

(1) Skone, J. H.; Govoni, M.; Galli, G. Nonempirical range-separated hybrid functionals for solids and molecules. *Physical Review B* **2016**, *93*, 235106.

(2) Chen, W.; Miceli, G.; Rignanese, G.-M.; Pasquarello, A. Nonempirical dielectric-dependent hybrid functional with range separation for semiconductors and insulators. *Physical Review Materials* **2018**, *2*, 073803.

(3) Gygi, F.; Baldereschi, A. Self-consistent Hartree-Fock and screened-exchange calculations in solids: Application to silicon. *Physical Review B* **1986**, *34*, 4405.
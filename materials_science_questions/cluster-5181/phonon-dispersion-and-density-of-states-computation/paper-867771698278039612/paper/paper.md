
# Phonon Hall effect with first-principles calculations

Kangtai Sun, \( ^{1,*} \)  Zhibin Gao, \( ^{1,2,\dagger} \)  and Jian-Sheng Wang \( ^{1} \) 

 \( ^{1} \) Department of Physics, National University of Singapore, Singapore 117551, Republic of Singapore

 \( ^{2} \) State Key Laboratory for Mechanical Behavior of Materials,

Xi'an Jiaotong University, Xi'an 710049, China

(Revised 17 May 2021)

Phonon Hall effect (PHE) has attracted a lot of attention in recent years with many theoretical and experimental explorations published. While experiments work on complicated materials, theoretical studies are still hovering around the phenomenon-based models. Moreover, previous microscopic theory was found unable to explain large thermal Hall conductivity obtained by experiments in strontium titanate (STO). Therefore, as a first attempt to bridge this gap, we implement first-principles calculations to explore the PHE in real materials. Our work provides a new benchmark of the PHE in sodium chloride (NaCl) under a large external magnetic field. Moreover, we demonstrate our results in barium titanate (BTO), and discuss the results in STO in detail about their deviation from experiments. As possible future directions, we further propose that the inner electronic Berry curvature or cubic potential plays important roles in the PHE in STO.

## I. INTRODUCTION

PHE, as a phonon analogue to the quantum Hall effect of electrons, has been a rather intriguing area since its first observation in 2005  \( [1] \) . In the past decade, several theoretical explanations and mechanisms have been proposed  \( [2–9] \) . Currently, the most successful microscopic theory was developed by Qin et al. in which the PHE is related to the topological properties of the phononic structure  \( [6] \) . However, with more experiments published, it is evident that we have not reached the end of the story yet. In 2020, an experimental group found a large PHE in STO, and they thought it can be explained by Qin's theory  \( [10] \) . However, subsequently, a theoretical group pointed out that Qin's theory cannot explain the large value in experiments and they used Boltzmann transport theory to successfully predict the ratio between the longitudinal thermal conductivity and the phonon Hall conductivity  \( [11] \) . Furthermore, another experimental work found that if the  \( {}^{16}O \)  in STO is replaced with its isotope  \( {}^{18}O \) , the phonon Hall conductivity will become two orders of magnitude smaller  \( [12] \) . This is a very bizarre behavior challenging all current theories. The authors concluded that the PHE in STO with  \( {}^{16}O \)  is more like an enhancement compared with  \( SrTi^{18}O_{3} \) , and therefore they attributed the reason most likely to the behavior of the transverse optical phonon modes in STO at low temperature. All these recent experiments are performed on complex materials, therefore, it is difficult to understand them with simplified models, and more accurate and persuasive first-principles calculations are needed.

Usually, harmonic assumption is made in first-principles calculations for phonon properties like phonon dispersion. However, in some highly anharmonic materials, harmonic terms alone will produce imaginary phonon frequencies, and they cannot explain those phenomena such as the thermal expansion, temperature-dependent phonon dispersion, and some phase transitions. Therefore, beyond harmonicity is a natural requirement to explore the PHE in complex materials like STO, and it was argued in a similar perovskite, BTO, that the anharmonic soft phonon modes will result in a large dielectric constant  \( [13] \)  which could act as a magnifier of the PHE  \( [11] \) . Based on this understanding, anharmonicity should play an important role in the PHE in real materials. In recent years, many packages based on first-principles calculations have been developed to calculate anharmonic properties in solids such as SCAILD, ALAMODE, and TDEP  \( [14–16] \) . With the help of these packages, it is feasible for us to study the PHE in real materials, which could deepen our understandings in this area.

The paper is organized as follows. In section II, we describe the self-consistent phonon calculation, which is the first step to calculate the PHE. In section III, we introduce the general PHE theory and discuss how to apply it to real materials utilizing the results obtained by the self-consistent phonon calculation. In section IV, we present our results for NaCl and BTO, and discuss the situation in STO. In section V, we draw conclusions of our work and propose that there is still a lot of future work required to fully understand the PHE. We also provide an appendix with some key details.

## II. ANHARMONIC SELF-CONSISTENT PHONON CALCULATION FOR SOFT PHONON MODES

There are currently three approaches to handle the anharmonicity: density functional perturbation theory  \( [17, 18] \) , ab initio molecular dynamics (AIMD)  \( [16, 19] \) , and self-consistent phonon (SCPH) theory  \( [14, 15, 20, 21] \) . Perturbation theory is only valid for weak anharmonicity, while AIMD is a nonperturbative approach. However, since AIMD is based on the time-dependent Schrödinger
 

equation for all particles approximately [22], it cannot include zero-point vibration which is significant at low temperature. SCPH provides another choice to address anharmonicity nonperturbatively considering the quantum effect. Therefore, in this study, we focus on the SCPH approach, and borrow the ALAMODE package developed by Tadano and Shinji [15]. In this section, we briefly introduce the SCPH theory.

A general Hamiltonian with the third- and the fourth-order Taylor expansion of the potential can be described as follows:

 \[ \begin{aligned}\hat{H}&=\frac{1}{2}\sum_{i}p_{i}^{2}+\frac{1}{2}u^{T}Ku\\&+\frac{1}{3}\sum_{ijk}\Gamma_{ijkl}u_{i}u_{j}u_{k}+\frac{1}{4}\sum_{ijkl}T_{ijkl}u_{i}u_{j}u_{k}u_{l},\end{aligned} \quad (1) \] 

where  \( u_{i} \equiv \sqrt{M_{i}}x_{i} \) ,  \( M_{i} \)  and  \( x_{i} \)  are mass and displacement of the i-th degree of freedom, respectively. Although the third-order term has important contribution for most anharmonic behaviors like thermal expansion and phonon lifetime, the fourth-order term is also important, especially for the soft phonon modes. Moreover, the fourth-order is simpler than the third if we apply a mean-field approximation by replacing  \( u^{4} \)  with  \( \langle u^{2}\rangle u^{2} \) . With this approximation, the problem goes back to a quadratic one with the effective force constants being determined self-consistently. Therefore, in this paper, we only focus on the fourth-order correction. By an equation of motion method [23], the non-equilibrium Green's function (NEGF) satisfies:

 \[ \begin{aligned}G(1,2)&=G_{0}(1,2)\\&+\int d1^{\prime}d2^{\prime}d3d4G_{0}(1,1^{\prime})T(1^{\prime},2^{\prime},3,4)G(2^{\prime},3,\\ \end{aligned} \quad (2) \] 

where  \(  G(1,2) = -\frac{i}{\hbar}\langle\hat{T}u(1)u(2)\rangle  \) ,  \(  G(1,2,3,4) = -\frac{i}{\hbar}\langle\hat{T}u(1)u(2)u(3)u(4)\rangle  \) ,  \( \hat{T} \)  is the contour order operator,  \(  G_{0}(1,2)  \)  is the non-interacting version of  \(  G(1,2)  \) , and numbers represent the combination of  \( (jt) \) . To close this equation, we need to apply a mean-field approximation:

 \[ \begin{aligned}G(1,2,3,4)\approx i\hbar\Big[&G(1,2)G(3,4)+G(1,3)G(2,4)\\&+G(1,4)G(2,3)\Big].\end{aligned} \quad (3) \] 

Then we can work out the effective force constant matrix:

 \[ K^{e}=K+\Sigma, \quad (4) \] 

where we define

 \[ \Sigma_{ij}=3\sum_{kl}T_{ijkl}\langle u_{k}u_{l}\rangle. \quad (5) \] 

The ingredient we need in the PHE is the dynamic matrix, and therefore we need to transform the equation into mode space, which is:

 \[ \begin{aligned}&D_{nn^{\prime}}(\boldsymbol{q})=\omega_{n}(\boldsymbol{q})^{2}\delta_{nn^{\prime}}\\&\quad+3\sum_{mm^{\prime}\boldsymbol{q}^{\prime}}T_{nn^{\prime}mm^{\prime}}(\boldsymbol{q},\boldsymbol{q}^{\prime})\langle Q_{m}(\boldsymbol{q}^{\prime})Q_{m^{\prime}}(\boldsymbol{q}^{\prime})^{*}\rangle,\\ \end{aligned} \quad (6) \] 

where Q represents normal modes, n and m are indices for normal modes, q and  \( q^{\prime} \)  are lattice momentum, and  \( \omega_{n} \)  is the eigenfrequency. This equation should be solved self-consistently. In 2015, Tadano and Shinji have already discussed details within their ALAMODE package [15]. Therefore, we utilize their package to calculate the dynamic matrix for real materials.

## III. PHONON HALL EFFECT THEORY

Currently, the widely accepted general theory for the PHE was proposed by Qin et al. in 2012 [6]. This theory introduces an effective vector potential to explain the PHE. We describe a harmonic phonon system in the reciprocal space with a Hamiltonian  \( \hat{H}=\frac{1}{2}\sum_{q}y_{q}^{\dagger}H(\boldsymbol{q})y_{q} \) , where  \( H_{q}=\operatorname{diag}\{D_{q},I\} \)  with  \( D_{q} \)  being the dynamic matrix,  \( y_{q}=(\boldsymbol{u}_{q},\boldsymbol{v}_{q})^{T} \) ,  \( u_{q} \)  is the displacement vector multiplied by the associated mass, and  \( v_{q}=\dot{u}_{q} \)  is the corresponding velocity vector. The  \( y_{q} \)  satisfies the commutation relation:

 \[ \begin{aligned}&[y_{\boldsymbol{q}},y_{\boldsymbol{q}^{\prime}}^{\dagger}]=i\hbar J(\boldsymbol{q})\delta_{\boldsymbol{q}\boldsymbol{q}^{\prime}},\\&J(\boldsymbol{q})=\begin{pmatrix}0&I\\ -I&-2A_{\boldsymbol{q}}\end{pmatrix},\\ \end{aligned} \quad (7) \] 

where  \( A_{q} \)  is an anti-Hermitian matrix. Assuming  \( y_{q} = \psi_{q} e^{-i\omega_{q} t} \) , we obtain the following eigen equation [9]:

 \[ \omega_{\boldsymbol{q}i}\psi_{\boldsymbol{q}i}=\begin{pmatrix}0&iI\\ -iD_{\boldsymbol{q}}&-i2A_{\boldsymbol{q}}\end{pmatrix}\psi_{\boldsymbol{q}i}\equiv\hat{H}_{\boldsymbol{q}}\psi_{\boldsymbol{q} i}, \quad (8) \] 

Comparing to the standard Kubo's theory [5], the key ingredient of Qin's theory is an energy magnetization term:

 \[ \kappa_{x y}=\kappa_{x y}^{\mathrm{K u b o}}+\frac{2M_{E}^{2}}{T V}. \quad (9) \] 

Here we take the phonon Hall conductivity in x-y plane as an example. V is the volume in real space, and T is the temperature.  \( M_{E}^{2} \)  is the circulation of the phonon energy current named as the energy magnetization [24]. This correction term completely cancels the Kubo term to successfully avoid the divergence of the phonon Hall conductivity at zero temperature in the theory with Kubo term alone. By solving the eigensystem, the Berry curvatures and phonon Hall conductivity are given by Qin et al.:

 \[ \mathbf{\Omega}_{q i}=-\mathrm{I m}\Big[\frac{\partial\bar{\psi}_{\boldsymbol{q}i}}{\partial\boldsymbol{q}}\times\frac{\partial\psi_{\boldsymbol{q}i}}{\bar{\partial}\boldsymbol{q}}\Big], \quad (10) \] 

and

 \[ \kappa_{x y}=-\frac{1}{2T}\int_{-\infty}^{\infty}d\epsilon\epsilon^{2}\sigma_{x y}(\epsilon)\frac{d n(\epsilon)}{d\epsilon}, \quad (11) \]
 

where

 \[ \begin{align*}\bar{\psi}&=\psi^{\dagger}\begin{pmatrix}D_{\boldsymbol{q}}&0\\0&I\end{pmatrix},\\\sigma_{xy}(\epsilon)&=-\frac{1}{V\hbar}\sum_{\substack{h\omega_{\boldsymbol{q}i}\leq\epsilon}}\Omega_{\boldsymbol{q}i}^{z},\end{align*} \quad (12) \] 

 \( n(\epsilon)=1/(e^{\epsilon/(k_{B}T)}-1) \)  is the Bose function at temperature T,  \( \epsilon \)  represents the energy, and  \( k_{B} \)  is the Boltzmann constant. The summation includes both positive and negative frequencies. The most common source of the  \( A_{q} \)  is the external magnetic field which has been applied in many experiments measuring the PHE. To describe this process, spin-phonon interaction was introduced.

## A. Spin-phonon interaction

After the first observation of the PHE in 2005, several researchers have tried to explain the experiments theoretically  \( [3-5] \) , and all of them focused on the Raman-type spin-phonon interaction (SPI). Under an external magnetic field, the SPI in an ionic crystal lattice has the form of  \( [5] \) 

 \[ H_{I}=\sum_{i}\boldsymbol{h}_{\alpha}\cdot(\boldsymbol{u}_{\alpha}\times\boldsymbol{p}_{\alpha}) \quad (13) \] 

where  \( h_{\alpha} = -\frac{q_{\alpha}}{2M_{\alpha}}B \)  if it is purely due to Lorentz force,  \( m_{\alpha} \)  and  \( q_{\alpha} \)  are the ionic mass and charge at site  \( \alpha \) ,  \( u_{\alpha} \)  and  \( p_{\alpha} \)  are the vectors of displacement and momentum of the  \( \alpha \) -th lattice site, respectively. If one assumes the magnetic field is along z-axis, the SPI can be written as

 \[ H_{I}=u^{T}A p, \quad (14) \] 

where A is an antisymmetric block diagonal matrix in real space with the diagonal block being  \( \begin{pmatrix} 0 & h_{\alpha} \\ -h_{\alpha} & 0 \end{pmatrix} \) . However, using  \( q_{\alpha} \)  as the charge of the ion is not very accurate in real materials, and in fact, ionic materials do not have free charges. Instead, charge property should be described by a tensor, i.e., the Born effective charge tensor [25]. With this correction, the A matrix is:

 \[ \boldsymbol{A}=\frac{e}{4M_{\alpha}}(\boldsymbol{Z}_{\alpha}^{T}\times\boldsymbol{B}+\boldsymbol{B}\times\boldsymbol{Z}_{\alpha}), \quad (15) \] 

where  \( Z_{\alpha} \)  is the Born effective charge dyadic of the ion at site  \( \alpha \) . The derivation and the meaning of the cross product are discussed in the appendix.

## B. An optimization: \(\Theta(x)\)

Although equation (11) is enough to calculate the phonon Hall conductivity, it is usually difficult to implement the integral over the energy accurately if the Berry curvatures at some q points have large values. However, it is accessible to avoid this difficulty if we initially integrate over the energy by hand. In such a way, the formula of the phonon Hall conductivity becomes

 \[ \kappa_{x y}=\frac{k_{B}^{2}T}{2V\hbar}\sum_{\boldsymbol{q},i}\Omega_{q i}^{z}\Theta(\beta\hbar\omega_{\boldsymbol{q}i}), \quad (16) \] 

where  \( \beta = 1/k_{B}T \) , and

 \[ \Theta(x)=\begin{cases}\displaystyle\frac{x^{2}}{e^{x}-1}-2x\ln(|e^{x}-1|),&x\neq0,\\ \displaystyle+2\mathrm{Re}[\mathrm{Li}_{2}(e^{-x})]&x=0.\end{cases} \quad (17) \] 

 \( Li_{2} \)  is the so-called dilogarithm function. Although the dilogarithm function is still an integral, there are developed reliable packages to calculate it accurately in many languages such as Fortran, C++ and Mathematica. With this formula, the accuracy can be greatly boosted, therefore we call it an optimization. The details of the integration can be found in the appendix.

## IV. NUMERICAL DETAILS, RESULTS AND DISCUSSION

Dynamic matrix, vector potential, and Berry curvatures are the ingredients to calculate the phonon Hall conductivity. We determine the structures of the materials based on first-principles calculations using Quantum-Espresso (QE) [26], then calculate their interatomic force constants (IFC) up to the fourth-order with the help of the AIMD package in QE, and finally using the ALAMODE to extract the corresponding dynamic matrix including both analytic and non-analytic (with LO-TO splitting) part. We assume the vector potential is just from the SPI introduced in the last section with the block diagonal A matrix. The Born effective charge dyadic is calculated by ph.x module in QE. As for the Berry curvatures, equation (10) is too abstract to be used in a real calculation, but fortunately, converting it to a more explicit form using the eigen equation is already a common skill in topological physics. Taking the z-component of the Berry curvature as an example:

 \[ \Omega_{j,q_{x}q_{y}}^{z}=-\mathrm{I m}\Big[\sum_{j\neq j^{\prime}}\frac{\bar{\psi}_{j}\frac{\partial\bar{H}}{\partial q_{x}}\psi_{j^{\prime}}\bar{\psi}_{j^{\prime}}\frac{\partial\bar{H}}{\partial q_{y}}\psi_{j}}{(\omega_{j}-\omega_{j^{\prime}}+i\eta)^{2}}-(q_{x}\leftrightarrow q_{y})\Big], \quad (18) \] 

where  \( \omega_{j} \)  is the eigenfrequency in equation (8),  \( \eta \)  is related to the inverse of the phonon lifetime to avoid infinity when there are degenerate points. Since both the analytic and non-analytic part of the dynamic matrix have explicit formulas, and the SPI is independent of q, the Berry curvatures can be explicitly worked out. Thereafter, the phonon Hall conductivity can be obtained by the summation of the weighted Berry curvatures in the first Brillouin zone.
 

## A. Numerical results for NaCl

In 2011, Agarwalla et al. have calculated the PHE in NaCl using “General Utility Lattice Program” (GULP) with a Coulomb potential and a non-Coulomb Buckingham potential [27]. However, at that time, they used a not quite correct theory and their approach was still model-based. Therefore, we recalculate the PHE in NaCl in first-principles as a new benchmark. In our first-principles calculations, we apply structure optimization with the PAW-PBE pseudo-potential for Na and Cl to determine the lattice constant which turns out to be 5.65 Å with the energy cutoff being 500 eV, and we use a  \( 2 \times 2 \times 3 \)  supercell to calculate the IFCs. A  \( 50 \times 50 \times 500 \)  grid and a  \( 8 \times 8 \times 6 \)  grid are employed in calculating the dynamic matrix according to equation (6) for q and  \( q' \)  respectively. The small  \( \eta \)  is chosen to be  \( 0.1 \, cm^{-1} \) .

![](./images/867771698278039612_1.jpg)

FIG. 1. (a) Phonon dispersion of NaCl at \(T = 300\) K without magnetic field. (b) Phonon dispersion of NaCl at \(T = 300\) K with an external magnetic field being \(3 \times 10^{5}\) T.

Figure 1(a) shows the phonon dispersion of NaCl at T = 300 K without an external magnetic field. LO-TO splitting is considered using the mixed-space approach [28]. It can be seen that in Fig. 1(a) there are many degenerate points. If we apply a magnetic field (along z-direction throughout the paper) of  \( 3 \times 10^{5} \)  T, those degenerate points will be lifted especially for the two TO modes as Figure 1(b) illustrates. Therefore, the role of magnetic field plays is to open gaps in the phonon dispersion. Since NaCl has a simple structure, the branches in phonon dispersion can be well separated from each other by the applied magnetic field. As a result, we can draw the corresponding Berry curvatures of each branch, which are shown in Fig. 2. Certain symmetries are observed in the Fig. 2. The first and second acoustic branches are almost opposite to each other, so are the first and second optical branches, while the third acoustic branch and the third optical branch have their own patterns. This behaviour is consistent with the phonon dispersion of NaCl.

Figure 3 illustrates the dependence of the phonon Hall conductivity on magnetic field and temperature. It can be seen that as the temperature goes to 0, conductivity also decreases to 0. This is a favorable correction compared with the blowup of the conductivity near 0 K in Agarwalla et al.'s plots. For a small magnetic field, the

![](./images/867771698278039612_2.jpg)

FIG. 2. The Berry curvatures of six positive branches in  \( b_{1}-b_{2} \)  reciprocal plane of NaCl under the magnetic field  \( B=3\times10^{5} \)  T at temperature T=300 K, where  \( \mathbf{b}_{1}=\frac{2\pi}{a}(-\hat{q}_{x}+\hat{q}_{y}+\hat{q}_{z}) \) ,  \( \mathbf{b}_{2}=\frac{2\pi}{a}(\hat{q}_{x}-\hat{q}_{y}+\hat{q}_{z}) \)  are the two of three basis vectors with a being the lattice constant. The horizontal and vertical axes represent the fraction of  \( b_{1} \)  and  \( b_{2} \)  in the range of  \( (-0.5,0.5) \) . The unit of the Berry curvatures is  \( a_{0}^{2} \) , where  \( a_{0} \)  is the Bohr radius. From (a) to (f), the associated eigenvalues are in ascending order.

![](./images/867771698278039612_3.jpg)

FIG. 3. (a) Phonon Hall conductivity versus the applied magnetic field at T = 50 K and T = 100 K respectively. (b) Phonon Hall conductivity versus temperature at  \( B = 3 \times 10^{5} \)  T and  \( B = 5 \times 10^{5} \)  T respectively.

magnitude of the conductivity is roughly linearly growing up, and when the magnetic field increases further, the magnitude starts to decrease, the same behavior as that in Agarwalla et al.'s results. However, the conductivity does not change sign in the same range of the magnetic field. Moreover, the magnitudes of our results are about one order larger than Agarwalla et al.'s, which is another progress of the ab initio approach.

Although we obtain observable values of the phonon Hall conductivity, it requires a rather large magnetic field, about  \( 10^{5} \)  T at least. In experiments, a magnetic field with an order of magnitude 1 is enough to induce observable and even large phonon Hall conductivity in complex materials [1, 10]. Therefore, it deserves to implement our approach in some much more complicated materials such as materials in the family of perovskites.
 

## B. Numerical results for BTO

BTO has a large dielectric constant, and it was argued that it is due to its soft optical phonons  \( [13] \)  at  \( \Gamma \)  point. Previous study implies that a large dielectric constant could result in large phonon Hall conductivity  \( [11] \) , therefore, we calculate the PHE in BTO to verify this point. At different temperature ranges, BTO has different structures, while currently this structural diversity cannot be precisely caught by first-principles calculations  \( [29] \) . Therefore, we still choose the simple cubic BTO to implement the calculation. PAW-PBE pseudo-potentials for Ba, Ti, and O are employed with a  \( 2 \times 2 \times 3 \)  supercell to calculate the dynamic matrix. The lattice constant is optimized to be 4.024 Å, and the energy cutoff is set to be 800 eV. q and  \( q' \)  grids are  \( 50 \times 50 \times 5 \)  and  \( 8 \times 8 \times 3 \)  respectively. The small  \( \eta \)  is still chosen to be  \( 0.1 \, cm^{-1} \) .

![](./images/867771698278039612_4.jpg)

FIG. 4. Phonon dispersion of BTO at \(T = 60\) K without magnetic field.

The phonon dispersion of BTO at T = 60 K is illustrated in Fig. 4 where the two soft TO modes can be clearly seen near  \( \Gamma \)  point whose frequencies are close to 0. Applying magnetic field results in a similar behavior as in NaCl which is trying to open gaps in dispersion. Since our goal for NaCl is to provide a benchmark while for BTO is to compare with experimental values, we use a reasonably large magnetic field with an order of magnitude 1 in this case. Within this range, the phonon dispersion almost remains the same under the magnetic field, therefore, it is not necessary to demonstrate it here.

Similar to Fig. 3, Figure 5 shows the behaviours of the phonon Hall conductivity against the magnetic field and temperature. Figure 5(a) is drawn at 60 K for this is roughly the lowest temperature range that first-principles calculations can correctly address the soft optical phonons in BTO [13]. Again, for a small magnetic field, the Hall conductivity demonstrates a linear relationship with the magnetic field. For large fields, the phonon Hall conductivity also becomes large and even has a sign change. Figure 5(b) is under a magnetic field of 16 T, the absolute value of Hall conductivity increases at first and reaches a peak near 150 K, then starts to decrease. However, the order of magnitude is two orders smaller than the order of the experimental values in STO. Although STO and BTO are different materials, they have very similar crystal structures and both have soft optical modes at low temperatures [30]. Therefore, we think the comparison is reasonable.

![](./images/867771698278039612_5.jpg)

![](./images/867771698278039612_6.jpg)

FIG. 5. (a) Phonon Hall conductivity versus the applied magnetic field at \(T = 60\) K. (b) Phonon Hall conductivity versus temperature at \(B = 16\) T.

We note that when we enlarge the magnetic field, the phonon Hall conductivity in the BTO encounters a sign change. Since the conductivity is just the sum of the weighted Berry curvatures in the first Brillouin zone, we should observe clues for the sign change from the Berry curvatures and phonon dispersion of the BTO. Usually, the great change of Berry curvatures comes from band-openings or band-crossings. However, monitoring the evolution of each branch in the BTO is not a good idea. In the phonon dispersion of the BTO, many branches are deeply entangled so that we cannot always distinguish each branch correctly traveling around the whole Brillouin zone, neither the Berry curvatures of each branch. Moreover, the phonon Hall conductivity is an overall effect summing over all the weighted Berry curvatures so we cannot only analyze the individual Berry curvatures along the high symmetry path. Therefore, we decide to simply split the branches into two groups, three acoustic branches and twelve optical branches, and draw a plot of contributions to the phonon Hall conductivity of the two groups, which is the Fig. 6. Comparing with the Fig. 5(a), we can conclude that the acoustic contributions are larger than optical for small magnetic fields so that the total conductivity is negative initially, and when the magnetic field surpasses some value, the situation gets reversed. Once a small magnetic field is applied to the system, the degenerate branches will be slightly lifted (points near the  \( \Gamma \)  point are dominant) so that the Berry curvatures rapidly increase as shown in the Fig. 6. Initial tiny gaps nearly produce symmetric Berry curvatures (dominated by the same  \( \eta \)  in equation (18)) among all the branches. However, due to the  \( \Theta \)  function, the
 

acoustic branches with much smaller eigenvalues will contribute more resulting in a negative conductivity (with a transformation, it is valid to just consider the positive branches [6]). When the magnitude of the magnetic field keeps increasing, by zooming in the phonon dispersion, we find that the gaps in the acoustic branches grow faster than those in the optical branches against the magnetic field. As a result, the magnitude of the Berry curvatures of the acoustic branches decreases faster than those in the optical branches. The slopes of the two groups in the Fig. 6 verify this statement. Finally, at some value of the magnetic field, the optical branches contribute more to the phonon Hall conductivity so that a sign change shows up.

![](./images/867771698278039612_7.jpg)

FIG. 6. Mode-dependent contributions to the phonon Hall effect for varying magnetic field at  \( T = 60 \, K \) . The red squares stand for the acoustic contributions and the blue dots for the optical contributions.

Why are the results so small? Our intuition is that the spin-phonon interaction, in this case, is too weak for it cannot even remove the degeneracy of the soft optical phonons. With this degeneracy, although we have soft optical phonons, their effects just get canceled. This canceling can be easily checked by looking at the mode contribution to the phonon Hall conductivity. However, currently we have no idea what are the suitable ingredients to open a gap between soft optical phonons from first-principles calculations, and we would like to leave it as an open question that deserves our further exploration. Therefore, we perform a numerical test to open a gap by hand.

There are two ways to manually open a small gap at and near the  \( \Gamma \)  point, one is to lift the higher soft optical phonon branch and the other is to lift the lower soft optical phonon branch. The latter one will induce band-crossing points near the  \( \Gamma \)  point. Figure 7 shows the Hall conductivity after these two operations. It can be seen that their magnitudes are indeed enlarged to be close to the experimental values. These two operations result in opposite signs, and usually the phonon Hall conductivity experiments measured has a negative sign.

![](./images/867771698278039612_8.jpg)

![](./images/867771698278039612_9.jpg)

FIG. 7. (a) Open a small gap by manually lifting 1% of the value of the higher soft optical phonon branch at and near  \( \Gamma \)  point (the chosen range is where the frequencies are lower than  \( 100\ cm^{-1} \) ). (b) Open a small gap with the same value and range as (a), but by manually lifting 1% of the value of the lower soft optical phonon branch which will introduce band-crossing points near  \( \Gamma \)  point. These two operations can be imagined considering a partially degenerate two-level system.

## C. Discussion for STO

Last year, an experimental group found a large phonon Hall conductivity in STO under the magnetic field around 15 T. Therefore, we also explored the PHE in STO by first-principles calculations. Since BTO and STO have a similar structure, the numerical details are almost the same as BTO except for the pseudo-potential files. Our optimized lattice constant for STO is 3.852 Å based on the PBEsol exchange-correlation functional for Sr, Ti, and O [31], which performs better than other functionals and is consistent with the previous experimental values [32] and theoretical calculations [15]. However, we cannot obtain large phonon Hall conductivity even after manually open a gap, and the order of magnitude is still two orders smaller than the experiments in STO. The failure could result from many reasons. Firstly, we choose a cubic structure while at low temperature, STO has different phases of structure. Secondly, we expect there should be soft phonon modes with frequencies being close to 0 near  \( \Gamma \)  point so that the dielectric constant of the STO will be as large as  \( 10^{4} \)  at low temperature, while our current approach utilizing ALAMODE cannot produce that soft optical modes, and the dielectric constant we obtained is about three orders smaller than expected. Thirdly, perhaps we cannot produce large PHE with the SPI.

Right after the experiment, a theoretical paper by Chen et al. discussed this experiment in detail [11]. The authors pointed out that with Qin’s theory, the phonon Hall conductivity can only be about four orders smaller than the experimental value. Although our results are two orders smaller, it is not large enough. Moreover, ac-
 

According to our observation, the SPI we used is too weak to open a gap between two soft phonon modes at  \( \Gamma \)  point. Therefore the degeneration may cause canceling during the calculation. We obtain large values as those in the experiment if we open a gap by hand in BTO (not in STO for we cannot produce soft phonon modes in STO). In Chen et al.'s paper, they also provide another direction to explain the experiment, which is using the Boltzmann transport theory. With their approach, they made a successful prediction of the ratio between the longitudinal conductivity and the phonon Hall conductivity. However, there is another new experiment in STO challenging their theory. Just by replacing the  \( {}^{16}O \)  in STO with the isotope  \( {}^{18}O \) , researchers found that the phonon Hall conductivity will be reduced by two orders [12]. It is difficult to explain this behavior using Boltzmann transport theory for the replacement only changes the mass. Moreover, it is unnatural that we can only explain the PHE with macroscopic methods.

When there is an external magnetic field, the ion will experience two effective vector potentials: one is from the real magnetic field (the SPI in our case), and the other is from the "Berry phase" due to the phase of electron ground state, which was first pointed out by Mead and Truhlar [33]. The latter one has already been considered in Qin's theory, and Saito et al. have discussed in detail how to include it in a square lattice model [7]. However, it seems that nobody knows how to calculate this electron-related vector potential in first-principles calculations. Another electron-related physical process is the spin-orbit coupling (SOC) of electrons. In our consideration, the SOC may affect the PHE in two ways. First, the SOC may relate to the electronic "Berry phase", but we cannot deal with it yet. Second, the SOC may modify the phonon dispersion directly. As a quick exploration, we calculate the phonon dispersion of the STO turning on the SOC at zero temperature, which is illustrated in the appendix. However, the effect of the SOC is rather weak that the phonon dispersion almost remains the same. Although previous research reported the SOC in the STO-based heterostructures [34] and gating system [35], there are no studies on the SOC in bulk STO or BTO before. Therefore, the high temperature effect of the SOC in the STO or BTO deserves future exploration. Besides, in our calculations, we do not take care of the cubic potential term which is related to the phonon lifetime. Qin's theory starts from the harmonic assumption, therefore we cannot deal with cubic term with this theory. Currently, we simply add a small constant value  \( \eta \)  in equation (18) to represent the inverse of the phonon lifetime. Although we can tune the  \( \eta \)  to modify the phonon Hall conductivity, a systematical theory for PHE considering the cubic term should be developed in future work. Therefore, we think the experiments still lack a microscopic explanation, and our intuition is that it may be relevant to the inner electronic topological structure of the STO or the cubic potential term in the STO, which is a future project to explore.

## V. CONCLUSION

In summary, we introduce an approach to calculate the phonon Hall conductivity in real materials using first-principles calculations, and implemented it for NaCl, BTO, and STO. Although the approach is very direct, it highly relies on whether first-principles calculations can predict materials properly and how to introduce the effective vector potential in materials. We have provided a benchmark of the PHE in NaCl to be examined in the future, and based on our calculation, there is still a gap to address soft phonons in STO using first-principles calculations. We conclude that SPI is not a good candidate to explain the PHE in real materials, and propose that the inner electronic structure or cubic potential term in STO may be possible directions to explore in future work. Finally, we think the relationship between the soft mode and  \( \kappa_{xy} \)  is far from clear quantitatively and needs further exploration. This study provides an effective route to capture the PHE from the accurate first-principles calculations in any real materials and has implications in promoting related experimental investigations.

## ACKNOWLEDGMENTS

J.-S. W. is supported by a FRC grant R-144-000-402-114 and an MOE tier 2 grant R-144-000-411-112. Z. GAO acknowledges the financial support from FRC tier 1 funding of Singapore (grant no. R-144-000-402-114). We also acknowledge the support by HPC Platform, Xi'an Jiaotong University.

## Appendix A: Spin-phonon interaction with Born effective charge

If we take a careful look at the form of SPI, it can be found that it has the similar form as the Hamiltonian containing a Lorentz force, therefore, to generalize it to couple with the Born effective charge, we should start from the magnetic energy. The energy of a magnetic moment is

 \[ V_{m}=-m\cdot\boldsymbol{B}, \quad (A1) \] 

where usually  \( m = \frac{e}{2} r \times v \) , e is the charge of the particle. Since the Born effective charge is a tensor, we should insert it into the equation carefully. A reasonable argument is from the way Born effective charge acting on the electric field, which is  \( Z^{T} E \) . Here we take the transpose of Z because the first index of it is associated with the electric field [25]. If we change the reference system so that the charge appears to move with a velocity v, it will also feel a magnetic field  \( E \rightarrow E + v \times B \) . Therefore,  \( Z^{T} \)  should act on  \( v \times B \) , not on B directly. Moreover, in electronic systems, the rate of change of the polarization is  \( \frac{dP}{dt} = e Z v \) . Analogous to this, we propose that in
 

magnetic case, Z acts on v. However, this replacement breaks the antisymmetry over r and v. To restore it, we add a term with Z act also on r so that the energy becomes

 \[ \begin{align*}V_{m}&=-\frac{e}{4}[r\times(Z\boldsymbol{v})+(Z\boldsymbol{r})\times\boldsymbol{v}]\cdot\boldsymbol{B}\\&=-\frac{e}{4}[((\boldsymbol{v}Z^{T})\times\boldsymbol{B})\cdot\boldsymbol{r}+(\boldsymbol{v}\times\boldsymbol{B})\cdot(Z\boldsymbol{r})]\\&=-\frac{e}{4}[v_{i}Z_{ki}B_{l}\epsilon^{klj}r_{j}+\epsilon^{ikl}v_{i}B_{k}Z_{lj}r_{j}]\\&\equiv-\frac{e}{4}[\boldsymbol{v}\cdot(\boldsymbol{Z}^{T}\times\boldsymbol{B}+\boldsymbol{B}\times\boldsymbol{Z})\cdot\boldsymbol{r}]\end{align*} \quad (A2) \] 

Then compare it with the form of the SPI,  \( H_{I} = u^{T} A p = -p^{T} A u \) , we can conclude that

 \[ A=\frac{e}{4M_{\alpha}}(Z_{\alpha}^{T}\times\boldsymbol{B}+\boldsymbol{B}\times\boldsymbol{Z}_{\alpha}) \quad (A3) \] 

## Appendix B: The  \( \Theta \)  function

Given equation (11), we can firstly integrate with respect to energy.

 \[ \begin{align*}\kappa_{xy}&=\frac{1}{2TV\hbar}\sum_{\boldsymbol{q},i}\Omega_{q i}^{z}\int_{-\infty}^{\infty}d\epsilon\epsilon^{2}\theta(\epsilon-\hbar\omega_{\boldsymbol{q}i})\frac{dn(\epsilon)}{d\epsilon}\\&\equiv\frac{k_{B}^{2}T}{2V\hbar}\sum_{\boldsymbol{q},i}\Omega_{q i}^{z}\Theta(\beta\hbar\omega_{\boldsymbol{q}i}),\end{align*} \quad (B1) \] 

where  \( \theta \)  is the step function,  \( n(\epsilon) = 1/(e^{\beta\epsilon} - 1) \)  is the Bose function,  \( \beta = 1/k_{B}T \) , and

 \[ \Theta(x)=\int_{x}^{\infty}y^{2}d n(y), \quad (B2) \] 

with the substitution  \( \beta\epsilon\rightarrow y \) . By integration by parts, we obtain

 \[ \Theta(x)=\frac{x^{2}}{e^{x}-1}+\int_{x}^{\infty}\frac{2y d y}{e^{y}-1}. \quad (B3) \] 

When x = 0, the first term is an indeterminate value, but the original integral in this case has a definite value  \( \pi^{2}/3 \) . When  \( x \neq 0 \) , we make another substitution  \( y \to -\ln(u) \) :

 \[ \Theta(x)=\frac{x^{2}}{e^{x}-1}-2\int_{0^{+}}^{e^{-x}}\frac{\ln(u)}{1-u}d u. \quad (B4) \] 

Again we use integration by parts,

 \[ \begin{align*}\Theta(x)&=\frac{x^{2}}{e^{x}-1}+2\ln(u)\left.\ln(|1-u|)\right|_{0^{+}}^{e^{-x}}\\&\quad-2\int_{0^{+}}^{e^{-X}}\frac{\ln|1-u|}{u}du\\&=\frac{x^{2}}{e^{x}-1}-2x\ln(|1-e^{-x}|)-2\int_{0^{+}}^{e^{-X}}\frac{\ln|1-u|}{u}du.\end{align*} \quad (B5) \] 

The last term is related to the Spence's function or the dilogarithm function:

 \[ -\int_{0^{+}}^{x}\frac{\ln\left|1-u\right|}{u}d u=\begin{cases}\mathrm{Li}_{2}(x),&x\leq1,\\ \pi^{2}/3-\ln^{2}(x)/2&x>1.\end{cases} \quad (B6) \] 

Since  \( \mathrm{Li}_{2}(x)+\mathrm{Li}_{2}\big(1/x\big)=\pi^{2}/6-\ln^{2}(-x)/2 \) , we can combine two cases so that finally we obtain

 \[ \Theta(x)=\begin{cases}\displaystyle\frac{x^{2}}{e^{x}-1}-2x\ln(|e^{x}-1|),&x\neq0,\\ \displaystyle+2\mathrm{Re}[\mathrm{Li}_{2}(e^{-x})]&x=0.\end{cases} \quad (B7) \] 

Here we always take the real part of the  \( \mathrm{Li}_{2}(e^{-x}) \)  for when  \( e^{-x} > 1 \) , it is a complex value while  \( \Theta(x) \)  is real.

## Appendix C: Spin-orbit coupling in STO

![](./images/867771698278039612_10.jpg)

FIG. 8. The phonon dispersion of the STO with and without the SOC at 0 K. The black solid line stands for the case without the SOC, and the red dotted line for the case with the SOC.

We calculate the phonon dispersion of the STO with the SOC considered at zero temperature. The numerical details are the same as we introduced in the main text except the SOC turned on during the first-principles calculations. The comparison is given in the Fig. 8. It can be seen that the effect of the SOC at zero temperature is too weak to modify the phonon dispersion obviously. The effect of the SOC at higher temperature has not been reported yet, and currently, precise first-principles calculations for STO at non-zero temperatures are still challenging.
 

[1] C. Strohm, G. Rikken, and P. Wyder, Phenomenological evidence for the phonon hall effect, Physical review letters 95, 155901 (2005).

[2] J.-S. Wang and L. Zhang, Phonon hall thermal conductivity from the green-kubo formula, Phys. Rev. B 80, 012301 (2009).

[3] L. Sheng, D. Sheng, and C. Ting, Theory of the phonon hall effect in paramagnetic dielectrics, Physical review letters 96, 155901 (2006).

[4] Y. Kagan and L. Maksimov, Anomalous hall effect for the phonon heat conductivity in paramagnetic dielectrics, Physical review letters 100, 145902 (2008).

[5] L. Zhang, J. Ren, J.-S. Wang, and B. Li, Topological nature of the phonon hall effect, Phys. Rev. Lett. 105, 225901 (2010).

[6] T. Qin, J. Zhou, and J. Shi, Berry curvature and the phonon hall effect, Phys. Rev. B 86, 104305 (2012).

[7] T. Saito, K. Misaki, H. Ishizuka, and N. Nagaosa, Berry phase of phonons and thermal hall effect in nonmagnetic insulators, Physical Review Letters 123, 255901 (2019).

[8] X. Zhang, Y. Zhang, S. Okamoto, and D. Xiao, Thermal hall effect induced by magnon-phonon interactions, Phys. Rev. Lett. 123, 167202 (2019).

[9] K. Sun, Z. Gao, and J.-S. Wang, Current-induced phonon hall effect, Phys. Rev. B 102, 134311 (2020).

[10] X. Li, B. Fauqué, Z. Zhu, and K. Behnia, Phonon thermal hall effect in strontium titanate, Physical Review Letters 124, 105901 (2020).

[11] J.-Y. Chen, S. A. Kivelson, and X.-Q. Sun, Enhanced thermal hall effect in nearly ferroelectric insulators, Physical Review Letters 124, 167601 (2020).

[12] S. Sim, H. Yang, H.-L. Kim, M. J. Coak, M. Itoh, Y. Noda, and J.-G. Park, Sizable suppression of thermal hall effect upon isotopic substitution in srtio 3, Physical Review Letters 126, 015901.

[13] J.-S. Wang, Phonon soft modes and para-to ferro-electric phase transitions, Physica A: Statistical Mechanics and its Applications, 125641 (2020).

[14] P. Souvatzis, O. Eriksson, M. Katsnelson, and S. Rudin, Entropy driven stabilization of energetically unstable crystal structures explained from first principles theory, Physical review letters 100, 095901 (2008).

[15] T. Tadano and S. Tsuneyuki, Self-consistent phonon calculations of lattice dynamical properties in cubic srtio 3 with first-principles anharmonic force constants, Physical Review B 92, 054301 (2015).

[16] O. Hellman, P. Steneteg, I. A. Abrikosov, and S. I. Simak, Temperature dependent effective potential method for accurate free energy calculations of solids, Physical Review B 87, 104111 (2013).

[17] S. Baroni, S. De Gironcoli, A. Dal Corso, and P. Giannozzi, Phonons and related crystal properties from density-functional perturbation theory, Reviews of Modern Physics 73, 515 (2001).

[18] K. Esfarjani and H. T. Stokes, Method to extract anharmonic force constants from first principles calculations, Physical Review B 77, 144112 (2008).

[19] T. Sun, D.-B. Zhang, and R. M. Wentzcovitch, Dynamic stabilization of cubic ca si o 3 perovskite at high temperatures and pressures from ab initio molecular dynamics, Physical Review B 89, 094109 (2014).

[20] N. Werthamer, Self-consistent phonon formulation of anharmonic lattice dynamics, Physical Review B 1, 572 (1970).

[21] I. Errea, M. Calandra, and F. Mauri, Anharmonic free energies and phonon dispersions from the stochastic self-consistent harmonic approximation: Application to platinum and palladium hydrides, Physical Review B 89, 064302 (2014).

[22] R. Car and M. Parrinello, Unified approach for molecular dynamics and density-functional theory, Phys. Rev. Lett. 55, 2471 (1985).

[23] Y. Xu, J.-S. Wang, W. Duan, B.-L. Gu, and B. Li, Nonequilibrium green's function method for phonon-phonon interactions and ballistic-diffusive thermal transport, Physical Review B 78, 224303 (2008).

[24] T. Qin, Q. Niu, and J. Shi, Energy magnetization and the thermal hall effect, Physical review letters 107, 236601 (2011).

[25] X. Gonze and C. Lee, Dynamical matrices, born effective charges, dielectric permittivity tensors, and interatomic force constants from density-functional perturbation theory, Physical Review B 55, 10355 (1997).

[26] P. Giannozzi, S. Baroni, N. Bonini, M. Calandra, R. Car, C. Cavazzoni, D. Ceresoli, G. L. Chiarotti, M. Cococcioni, I. Dabo, A. Dal Corso, S. de Gironcoli, S. Fabris, G. Fratesi, R. Gebauer, U. Gerstmann, C. Gougoussis, A. Kokalj, M. Lazzeri, L. Martin-Samos, N. Marzari, F. Mauri, R. Mazzarello, S. Paolini, A. Pasquarello, L. Paulatto, C. Sbraccia, S. Scandolo, G. Sclauzero, A. P. Seitsonen, A. Smogunov, P. Umari, and R. M. Wentzcovitch, Quantum espresso: a modular and open-source software project for quantum simulations of materials, Journal of Physics: Condensed Matter 21, 395502 (19pp) (2009).

[27] B. K. Agarwalla, L. Zhang, J.-S. Wang, and B. Li, Phonon hall effect in ionic crystals in the presence of static magnetic field, The European Physical Journal B 81, 197 (2011).

[28] Y. Wang, J. Wang, W. Wang, Z. Mei, S. Shang, L. Chen, and Z. Liu, A mixed-space approach to first-principles calculations of phonon frequencies for polar materials, Journal of Physics: Condensed Matter 22, 202201 (2010).

[29] R. A. Evarestov and A. V. Bandura, First-principles calculations on the four phases of bátio \( _{3} \) , Journal of computational chemistry 33, 1123 (2012).

[30] X. He, D. Bansal, B. Winn, S. Chi, L. Boatner, and O. Delaire, Anharmonic eigenvectors and acoustic phonon disappearance in quantum paraelectric srtio 3, Physical review letters 124, 145901 (2020).

[31] J. P. Perdew, A. Ruzsinszky, G. I. Csonka, O. A. Vydrov, G. E. Scuseria, L. A. Constantin, X. Zhou, and K. Burke, Restoring the density-gradient expansion for exchange in solids and surfaces, Phys. Rev. Lett. 100, 136406 (2008).

[32] A. Okazaki and M. Kawanimami, Lattice constant of strontium titanate at low temperatures, Materials Research Bulletin 8, 545 (1973).

[33] C. A. Mead and D. G. Truhlar, On the determination of born-oppenheimer nuclear motion wave functions including complications due to conical intersections and identical nuclei, The Journal of Chemical Physics 70, 2284 (1979).
 

[34] Y. Kim, R. M. Lutchyn, and C. Nayak, Origin and transport signatures of spin-orbit interactions in one-and two-dimensional srtio 3-based heterostructures, Physical Review B 87, 245121 (2013).

[35] H. Nakamura, T. Koga, and T. Kimura, Experimental evidence of cubic rashba effect in an inversion-symmetric oxide, Physical Review Letters 108, 206601 (2012).
 

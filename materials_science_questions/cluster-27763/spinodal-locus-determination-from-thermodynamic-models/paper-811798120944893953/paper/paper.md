# Effective Soft-Core Potentials and Mesoscopic Simulations of Binary Polymer Mixtures

J. McCarty, I. Y. Lyubimov, and M. G. Guenza*

Department of Chemistry and Institute of Theoretical Science, University of Oregon, Eugene, Oregon 97403

Received January 8, 2010; Revised Manuscript Received March 2, 2010

ABSTRACT: Mesoscopic molecular dynamics simulations are used to determine the large-scale structure of several binary polymer mixtures of various chemical architecture, concentration, and thermodynamic conditions. By implementing an analytical formalism, which is based on the solution to the Ornstein-Zernike equation, each polymer chain is mapped onto the level of a single soft colloid. From the appropriate closure relation, the effective, soft-core potential between coarse-grained units is obtained and used as input to our mesoscale simulations. The potential derived in this manner is analytical and explicitly parameter dependent, making it general and transferable to numerous systems of interest. From computer simulations performed under various thermodynamic conditions the structure of the polymer mixture, through pair correlation functions, is determined over the entire miscible region of the phase diagram. In the athermal regime mesoscale simulations exhibit quantitative agreement with united atom simulations. Furthermore, they also provide information at larger scales than can be attained by united atom simulations and in the thermal regime approaching the phase transition.

## 1. Introduction

The mixing of two or more types of polymers is of great scientific and technological interest, as it opens up the possibility of creating new materials emerging with specific physical and chemical properties. $^{1}$ However, although polymer blends have been very much a part of everyday life, these continue to be a source of extensive scientific inquiry. The rich physics in polymer mixtures stems in part from the fact that their structure and dynamics change as thermodynamic conditions that cause phase separation (i.e., spinodal decomposition) are approached. Mix- ture stability is driven not only by temperature and composition but also by differences in chain length and monomer architecture that may contribute substantial entropic effects. From physical and engineering standpoints, a goal is to understand and predict changes that a polymer will undergo when mixed with another polymer system. $^{2,3}$ Theoretical efforts have focused on this area, resulting in the development of several approaches connecting monomeric structure to static and dynamic properties as a function of thermodynamic parameters. $^{4-9}$

Molecular dynamics (MD) studies have aided our under- standing of the correlation between local (intra- and inter- molecular) structure and global fluid properties that govern polymer mixtures. $^{10-16}$ However, these computational appro aches have been limited to relatively small length and time scales because present-day computing power limits the attainment of extended scales. $^{17}$ For polymer blends, this is particularly proble matic because as the spinodal decomposition is approached, a divergent length scale in concentration fluctuations develops, thereby readily exceeding box sizes commonly used to model polymeric ensembles. In this manner, the determination of large- scale properties for polymer mixtures with atomic reso- lution requires increasingly larger simulation boxes and becomes rapidly unfeasible.

One way to circumvent this difficulty is to introduce a coarse- grained description of the polymer mixture, where small-scale atomistic details are statistically averaged out. The resulting structure allows for computer simulations of large systems, including a high number of polymers, chains with large molecular weights, and for a long time scale. Recent mesoscopic descrip- tions based on various coarse-grained approaches have been presented in the literature and effectively utilized to investigate the demixing of polymer solutions, $^{18}$ immiscible polymer blends, $^{19}$ and star-linear polymer mixtures. $^{20}$ By combining information obtained from simulations of the coarse-grained system with information obtained at smaller length scales and shorter times, in the context of a multiscale procedure, it is possible to obtain a complete and exhaustive description of the polymer mixture at all length scales of interest. $^{21}$ We have previously shown that a procedure, which combines information at the two length scales of the effective segment length and the radius of gyration, accurately determines the structural properties of homopolymer melts. $^{22}$ This multiscale modeling procedure hasbeen recently extended to treat polymer mixtures. $^{23}$

In this publication, we focus on performing simulations of polymer mixtures where the ensemble of polymers is mapped onto a system of interacting soft, colloidal particles. At this level of coarse-graining each polymer is represented as one soft colloidal particle centered at the polymer center-of-mass. The concept of modeling flexible polymer chains as soft spheres was originally proposed by Flory and Krigbaum $^{24}$ for dilute polymer solutions; however, the resulting effective potential exhibited an incorrect trend in repulsive interactions with increasing chain length or polymer density. For dilute to semidilute solutions, Louis and co-workers were able to obtain correct scaling beha- vior for polymer chains mapped onto soft spheres using liquid state theory in conjunction with Monte Carlo simulations. $^{25}$ This approach was later extended to poor solvent conditions where coils contract to avoid contact with the solvent. $^{26}$ Importantly, this work shows that for a given set of state conditions a simple

*To whom correspondence should be addressed. E-mail: mguenza@ uoregon.edu.

effective pair potential, $v(r)$, is capable of reproducing the radial distribution function, $g(r)$, which depends on many body interactions. Because of this reduction in interactions that need to be calculated at each computational step, mesoscale simulations of polymers represented as soft colloids are useful in determining many structural as well as dynamical properties of polymer blends, including how morphologies develop depending on the thermodynamic parameters of the system. $^{27}$ The advantage of this extreme coarse-graining of the polymer is that it is possible to simulate very large ensembles of particles, i.e., adopt large simulation boxes, with a modest increase in the computational time. Such an extreme level of coarse-graining becomes important for simulations of systems where the relevant range of length scales is particularly large, for example in micellar aggregates of ionic surfactants. $^{28}$

The implementation of mesoscale simulations requires attaining the effective "bare" potential, $v^{\text{cc}}(r)$, that characterizes pairwise decomposable interactions between molecular center-of-mass (com) sites. Since $v^{\text{cc}}(r)$ corresponds to a free energy obtained from the monomer frame of reference, it depends on the thermodynamic state of the system, as specified by the density, temperature, polymer molecular weight, and composition of the mixture.

The determination of a reliable, fully transferable, coarse-grained potential is a highly desirable goal. $^{29}$ While phenomenological as well as rigorously numerical approaches have been described in the literature $^{25,30-32}$ to determine effective coarse-grained pair potentials for polymer systems, their reliance on acquired microscopic simulation data partially defeats the gain in computational time that is possible with a coarse-graining procedure. Typically, mesoscopic potentials are optimized to full atomistic simulations under a given set of thermodynamic conditions, limiting their transferability. Moreover, the optimization procedure generally starts from the mean-force potential, which is the effective potential between two particles in the field of the surrounding particles and is conceptually different from the bare potential, $v^{\text{cc}}(r)$. We have developed an analytical formalism to calculate the effective potential, $v^{\text{cc}}(r)$, starting from liquid state theory and solving the Ornstein-Zernike equation. $^{33,34}$ The potential obtained in such a manner is explicitly related to the structural parameters of the polymer, making it specific to any system we desire to simulate but also fully transferable to systems with different molecular structure and thermodynamic conditions.

More specifically, our nonphenomenological expressions for the com-com total pair intermolecular correlation functions, $h_{\alpha \beta}^{\text{cc}}(r)$, between self ($\alpha \alpha$) and cross ($\alpha \beta$) interactions, are obtained from a generalized Ornstein-Zernike integral equation for binary polymer mixtures where atomistic sites are accounted for as real sites, while coarse-grained sites are treated as auxiliary sites. The equation formally bridges information from the microscopic (monomer) domain to mesoscopic (molecular) scales. The derived equations for $h_{\alpha \beta}^{\text{cc}}(r)$ reproduce well and with no fitting parameters united atom (UA) molecular dynamics (MD) simulation data in both real and reciprocal spaces. Our renormalized description $^{33,34}$ correctly recovers the known analytical expressions for density and concentration fluctuations of mixtures of colloidal liquids, by Kirkwood and Buff $^{35}$ and by Bhatia and Thornton, $^{36}$ slightly modified as our expressions account for soft potentials instead of hard-core ones. Together, these tests provide a benchmark which supports the foundation of our renormalization procedure.

In the current publication we extend our previous work to demonstrate that the derived coarse-grained effective potential, when input to mesoscale MD simulations of binary polymer blends, is capable of reproducing the large-scale structure of the polymer,which depends on many body interactions at the monomer level. We demonstrate that our approach is useful to produce mesoscale simulations of binary homopolymer mixtures at various temperatures and concentrations approaching the spinodal. In this way, we are able to test the derived potential in terms of how well it reproduces the mesoscopic structure of the mixture over different regions of the phase diagram, where atomistic level simulations are computationally exhaustive. We make use of the hypernetted-chain (HNC) closure to calculate the effective potential, $v_{\alpha \beta}^{\text{cc}}(r)$, as a function of the total correlation function, $h_{\alpha \beta}^{\text{cc}}(r)$. In turn, the pair potentials, $v_{\alpha \beta}^{\text{cc}}(r)$, are used as an input to a coarse-grained simulation, where polymers interact as soft colloidal particles.

Systems investigated are blends of polyethylene, polyisobutylene, and polypropylenes in their head-to-head, istotactic, and syndiotactic forms. We show that our method is robust and allows for the equilibrium structural properties of the fluid mixture to be readily calculated under any thermodynamic parameters of interest. While the focus here is on static properties, the derived potential is widely applicable to nonequilibrium systems and may be useful in other methods commonly employed, such as dissipative particle dynamics, $^{37}$ which currently rely on numerical potentials.

To demonstrate the reliability of our mesoscale simulations, we first consider systems that are far from the spinodal temperature, for which the liquid is well-mixed, and show that in this regime our $v_{\alpha \beta}^{\text{cc}}(r)$ reproduces quantitatively the liquid structure at the level of com obtained from UA MD simulations, $^{13,14}$ establishing consistency between the different levels of description. We then extend our analysis to different thermodynamic conditions for which no UA data are available, focusing on mixtures of head-to-head polypropylene and polyethylene (hhPP/PE) in the miscible region of the phase diagram. The temperature dependence is expressed in terms of a single interaction parameter that enters our simulation through the analytical form of the potential and depends on the local interactions between monomers. From the simulation trajectories, we calculate pair distribution functions which depend on the parameters of the system and manifest the trends for demixing of the coarse-grained mixture. From this treatment, and from the fact that our expressions recover known expressions for colloidal liquids, we calculate the concentration fluctuation contribution to the scattering function, $S(k)$, which is related to the scattered light intensity measured in experimental studies of critical binary polymer mixtures. In this way, we are able to test the derived potential in terms of how well it reproduces the mesoscopic structure of the mixture over different regions of the phase diagram. Results show that the effective potential between center-of-masses of polymers in a mixture can be used to produce mesoscopic simulations under a variety of thermodynamic conditions, making the procedure useful to a number of applications in polymer physics. To test the versatility of our approach, we show how the proposed theory may be applied to blends that present a lower critical solution temperature (LCST). We study the hhPP/PIB mixture using the temperature dependence of the $\chi$ parameter from the literature and run mesoscale simulations at various temperatures. The concentration fluctuation structure factor shows that fluctuations in concentration become smaller as the temperatures decreases, as it is expected.

The current publication is organized as follows. In section 2, a review of our derivation for $h_{\alpha \beta}^{\text{cc}}(r)$ is provided. These results are then used in section 3 for the calculation of $v_{\alpha \beta}^{\text{cc}}(r)$, obtained from the HNC closure. In section 4, our representations for $v_{\alpha \beta}^{\text{cc}}(r)$ are implemented in mesoscopic simulations of binary polymer blends, where the mixture is modeled as an assembly of soft, interacting colloidal particles. Section 5 compares predicted total correlation functions, analytical and from mesoscale simulations, with data from united atom molecular dynamic simulations.

In section 6 data obtained from mesoscopic simulations are used to calculated liquid partial structure factors which are used to determine the phase diagram of the mixture. Section 7 investigates how corrections to the Debye form factor affect the precision of the predicted total correlation functions. Finally, in section 8 we show how our approach is effective in predicting high-temperature demixing for the LCST blend hhPP/PIB.

## 2. Mesoscopic Pair Correlation Functions for Asymmetric Binary Polymer Blends

Pair correlation functions (pcfs) comprise a standard approach in liquid-state theory to describe the structure of liquids. Since it is generally sufficient to account for two-body correlations, pcfs can be employed to determine all structural and thermodynamic properties of a system. $^{38}$ Moreover, these are input to the equation of motion describing cooperative dynamics, where the effect of the surrounding medium on single-chain dynamics is taken into account. $^{39,40}$ In the context of our coarse-graining procedure, pcfs provide a convenient manner of calculating, with the aid of an appropriate closure, the bare pair potential needed to perform mesoscopic simulations. In this section, a brief review is given of the theoretical formalism we previously developed to describe coarse-grained binary mixtures of asymmetric polymer blends. $^{33,34}$

Our model for a binary blend consists of A and B homopolymers, having $N_{\mathrm{A}}$ and $N_{\mathrm{B}}$ monomer sites with segment lengths $\sigma_{\mathrm{A}}$ and $\sigma_{\mathrm{B}}$, respectively. For simplicity, these monomer sites are taken to span equivalent volumes so that the polymer volume fraction is given by $\phi=n_{\mathrm{A}} N_{\mathrm{A}} /\left(n_{\mathrm{A}} N_{\mathrm{A}}+n_{\mathrm{B}} N_{\mathrm{B}}\right)$, where $n_{\alpha}$ is the number of molecules of type $\alpha$ in the mixture with $\alpha \in\{\mathrm{A}, \mathrm{B}\}$. While $\rho=\left(n_{\mathrm{A}} N_{\mathrm{A}}+n_{\mathrm{B}} N_{\mathrm{B}}\right) / V$ quantifies the total number of monomer sites contained in a region of space spanned by $V$, the site and chain number densities for molecules of type A are given by $\rho_{\mathrm{A}}=n_{\mathrm{A}} N_{\mathrm{A}} / V=\phi \rho$ and $\rho_{\mathrm{c}, \mathrm{A}}=n_{\mathrm{A}} / V$, respectively.

The derivation of our analytical expressions for total intermolecular com pcfs in a polymer mixture extends from a procedure outlined by Krakoviack et al. $^{41}$ for homopolymer solutions. The key step in this approach is to include molecular coms as *auxiliary* sites along with monomer sites serving as *real* sites. The generalized Ornstein-Zernike integral equation is solved in reciprocal space and is given by
$$
\mathbf{H}(k)=\boldsymbol{\Omega}(k) \mathbf{C}(k)[\boldsymbol{\Omega}(k)+\mathbf{H}(k)]
\quad(1)
$$
where $\mathbf{H}(k)$ is the matrix of total intermolecular pcfs, $\mathbf{C}(k)$ is the matrix of direct intermolecular pcfs, and $\boldsymbol{\Omega}(k)$ represents the matrix of intramolecular pcfs. Specializing to the case of a binary polymer mixture, each matrix in eq 1 is of rank four, composed of four $2 \times 2$ blocks that account for monomer-monomer (mm), com-com (cc), and the corresponding cross (cm and mc) interactions. For instance
$$
\mathbf{H}(k)=\left[\begin{array}{ll}
\mathbf{H}^{\mathrm{mm}}(k) & \mathbf{H}^{\mathrm{mc}}(k) \\
\mathbf{H}^{\mathrm{cm}}(k) & \mathbf{H}^{\mathrm{cc}}(k)
\end{array}\right]
\quad(2)
$$

The remaining matrices in eq 1 follow an arrangement analogous to that of eq 2. Each block in eq 2 contains self $(\alpha \alpha)$ interactions along its diagonal, whereas cross $(\alpha \beta)$ interactions occupy off-diagonal positions.

As a next step, the individual block elements that define the matrices in eq 1 are defined. The intermolecular total pcf matrix $\mathbf{H}(k)$ is composed of the chain-averaged monomer-monomer pcfs $H_{\alpha \beta}^{\mathrm{mm}}(k)=\rho_{\alpha} \rho_{\beta} h_{\alpha \beta}^{\mathrm{mm}}(k)$, the com-monomer pcfs $H_{\alpha \beta}^{\mathrm{cm}}(k)=$ $\rho_{\mathrm{c}, \alpha} \rho_{\beta} h_{\alpha \beta}^{\mathrm{cm}}(k)=H_{\beta \alpha}^{\mathrm{mc}}(k)$, and com-com pcf $H_{\alpha \beta}^{\mathrm{cc}}(k)=\rho_{\mathrm{c}, \alpha} \rho_{\mathrm{c}, \beta} h_{\alpha \beta}^{\mathrm{cc}}(k)$.
Note that, in general, $h_{\alpha \beta}^{\mathrm{cm}}(k)=h_{\beta \alpha}^{\mathrm{mc}}(k)$ while $h_{\alpha \beta}^{\mathrm{cm}}(k) \neq h_{\alpha \beta}^{\mathrm{mc}}(k)$ when $\alpha \neq \beta$. The intramolecular pcf matrix $\boldsymbol{\Omega}(k)$ is similarly composed of $\Omega_{\alpha \beta}^{\mathrm{mm}}(k)=\rho_{\alpha} \rho_{\beta} \omega_{\alpha \beta}^{\mathrm{mm}}(k) \delta_{\alpha \beta} z_{\alpha \beta}, \Omega_{\alpha \beta}^{\mathrm{cm}}(k)=$ $\rho_{\mathrm{c}, \alpha} \rho_{\beta} \omega_{\alpha \beta}^{\mathrm{cm}}(k) \delta_{\alpha \beta} z_{\alpha \beta}=\Omega_{\beta \alpha}^{\mathrm{mc}}(k)$, and $\Omega_{\alpha \beta}^{\mathrm{cc}}(k)=\rho_{\mathrm{c}, \alpha} N_{\beta} \rho_{\mathrm{c}, \beta} \delta_{\alpha \beta} z_{\alpha \beta}$, where $z_{\alpha \beta}=\left[\phi_{\beta} \rho\left(2-\delta_{\alpha \beta}\right)\right]^{-1}$. Finally, the intermolecular direct total pcf matrix $\mathbf{C}(k)$ acquires a much simpler structure when including the approximation that any interaction involving auxiliary sites is negligible. $^{42}$ Under these conditions, the only nonzero block in $\mathbf{C}(k)$ involves monomer-monomer pcfs, defined as $C_{\alpha \beta}^{\mathrm{mm}}(k)=c_{\alpha \beta}^{\mathrm{mm}}(k)$.

Using the matrix definitions described above, eq 1 is solved to obtain the intermolecular mesoscopic total pcfs, which are given by the relation
$$
h_{\alpha \beta}^{\mathrm{cc}}(k)=\left[\frac{\omega_{\alpha \alpha}^{\mathrm{cm}}(k) \omega_{\beta \beta}^{\mathrm{cm}}(k)}{\omega_{\alpha \alpha}^{\mathrm{cm}}(k) \omega_{\beta \beta}^{\mathrm{mm}}(k)}\right] h_{\alpha \beta}^{\mathrm{mm}}(k)
\quad(3)
$$

Upon inspection, it is readily seen that eq 3 formally connects com distribution functions to monomer-monomer intra- and intermolecular distribution functions. In this manner, one calculates mesoscale properties from information on the local polymer scale. As mentioned before, this feature is relevant because properties on the mesoscale ultimately depend on small-scale interactions.

To obtain analytical solutions for $h_{\alpha \beta}^{\mathrm{cc}}(k)$, a brief description is given for each of the correlation functions entering into eq 3. The com-monomer intramolecular pcf can be approximated in reciprocal space with a Gaussian distribution as
$$
\omega_{\alpha \alpha}^{\mathrm{cm}}(k)=N_{\alpha} \mathrm{e}^{-k^{2} R_{\mathrm{g} \alpha}{ }^{2} / 6}
\quad(4)
$$
with the molecular radius of gyration defined as $R_{\mathrm{g} \alpha}=(N / 6)^{1 / 2} \sigma_{\alpha}$. On the other hand, the monomer-monomer intramolecular pcf is given by the Debye formula
$$
\omega_{\alpha \alpha}^{\mathrm{mm}}(k)=\frac{2 N_{\alpha}\left[\mathrm{e}^{-k^{2} R_{\mathrm{g} \alpha}{ }^{2}}-1+k^{2} R_{\mathrm{g} \alpha}{ }^{2}\right]}{k^{4} R_{\mathrm{g} \alpha}{ }^{4}}
\quad(5)
$$

For analytical convenience, however, it is customary to approximate eq 5 with its Padé approximant given by $^{43}$
$$
\omega_{\alpha \alpha}^{\mathrm{mm}}(k) \approx \frac{N_{\alpha}}{1+k^{2} R_{\mathrm{g} \alpha}{ }^{2} / 2}
\quad(6)
$$

Although approximated, inclusion of eq 6 allows for a convenient analytic expression for $h^{\mathrm{cc}}(r)$ given by eq 9, which has been shown to give good agreement with simulations for the total pair correlation function in both real and reciprocal spaces. $^{33}$ We discuss the implication for this approximation in detail below. In the current publication, we use both eq 5 and eq 6 for $\omega^{\mathrm{mm}}(k)$ and compare the resulting mesoscopic $h^{\mathrm{cc}}(k)$ from eq 3.

The respective monomer-monomer intermolecular total pcfs used are taken from the thread limit of the polymer reference interaction site model $^{4,5}$ (PRISM). The initial analytical treatment in the context of PRISM for polymer mixtures $^{44}$ has been extended by Yatsenko et al. $^{34}$ to account for chain asymmetry effects in the system. In this approach, a new parameter enters the formalism, $\gamma=\sigma_{\mathrm{B}} / \sigma_{\mathrm{A}}$, which defines the monomer asymmetry.

While the thread model for polymer chains coarsely describes the liquid structure on local scales, it accurately captures the onset of the "correlation hole" effect at a length scale of $R_{\mathrm{g}}$. Given that the spatial dimension of interest in our description is $R_{\mathrm{g}}$, the thread limit of PRISM is an adequate representation for the intended purpose of the present work. The solutions

are given by $^{33,34}$

$$
h_{\mathrm{AA}}^{\mathrm{mm}}(r)=\frac{3}{\pi \rho r \sigma_{\mathrm{AB}}{ }^{2}}\left[\frac{1-\phi}{\phi} \mathrm{e}^{-r / \xi_{\phi}}+\gamma^{2} \mathrm{e}^{-r / \xi_{p_{\mathrm{AA}}}}-\frac{1}{\phi} \frac{\sigma_{\mathrm{AB}}{ }^{2}}{\sigma_{\mathrm{A}}{ }^{2}} \mathrm{e}^{-r / \xi_{c \mathrm{~A}}}\right]
$$

$$
\begin{aligned}
h_{\mathrm{BB}}^{\mathrm{mm}}(r)= & \frac{3}{\pi \rho r \sigma_{\mathrm{AB}}{ }^{2}}\left[\frac{\phi}{1-\phi} \mathrm{e}^{-r / \xi_{\phi}}+\gamma^{-2} \mathrm{e}^{-r / \xi_{p_{\mathrm{BB}}}}\right. \\
& \left.-\frac{1}{1-\phi} \frac{\sigma_{\mathrm{AB}}{ }^{2}}{\sigma_{\mathrm{B}}{ }^{2}} \mathrm{e}^{-r / \xi_{\mathrm{cB}}}\right] \\
h_{\mathrm{AB}}^{\mathrm{mm}}(r)= & \frac{3}{\pi \rho r \sigma_{\mathrm{AB}}{ }^{2}}\left[-\mathrm{e}^{-r / \xi_{\phi}}+\mathrm{e}^{-r / \xi_{p_{\mathrm{AB}}}}\right]
\end{aligned}
\tag{7}
$$

where

$$
\xi_{\phi}=\frac{\sigma_{\mathrm{AB}}}{\sqrt{24 \phi(1-\phi) \chi_{\mathrm{s}}\left(1-\chi / \chi_{\mathrm{s}}\right)}}
\tag{8}
$$

is the length scale governing concentration fluctuations, which diverges at the spinodal temperature. Here, $\chi$ is a single interaction parameter that depends on the specific nearest neighbor pair energies between two AA, AB, or BB monomers and is given by $\chi=\varepsilon_{\mathrm{AB}}-\left(\varepsilon_{\mathrm{AA}}+\varepsilon_{\mathrm{BB}}\right) / 2$. In a mesoscopic treatment which averages out the specific monomer interactions, $\chi$ is an input parameter corresponding to the temperature dependence of a specific polymer architecture. From our definitions it clear that the quantity $\chi / \rho$ is the analogue of the Flory-Huggins interaction parameter, and at the spinodal temperature $\chi \rightarrow \chi_{\mathrm{s}}$, where $\chi_{\mathrm{s}}=$ $\left[2 N_{\mathrm{A}} \phi\right]^{-1}+\left[2 N_{\mathrm{B}}(1-\phi)\right]^{-1}$. The quantity $\left(1-\chi / \chi_{\mathrm{s}}\right)$ can be seen as a reduced temperature that indicates how far the system is from its spinodal temperature. Also in eq $7, \xi_{\mathrm{c} \alpha}=R_{\mathrm{g} \alpha} / 2^{1 / 2}$ is the length scale of the correlation hole while $\xi_{\rho \alpha \beta}{ }^{-1}=\pi \rho \sigma_{\alpha \beta}{ }^{2} / 3+$ $\xi_{\mathrm{c} \alpha \beta}{ }^{-1}$ is the density correlation length scale with $\sigma_{\alpha \beta}{ }^{2}=\phi_{\beta} \sigma_{\alpha}{ }^{2}+$ $\phi_{\alpha} \sigma_{\beta}{ }^{2}$. This latter definition reintroduces finite-size effects, local semiflexibility, and branching that pertain to each component through a meltlike description. The effective segment length scales are determined from the radius of gyration of each component polymer, through the relation $\sigma_{\alpha}=$ $\left(6 / N_{\alpha}\right)^{1 / 2} R_{\mathrm{g}}$.

Inserting the definitions from eqs 4,6 , and 7 into eq 3 , the intermolecular total pcfs at the com level read

$$
\begin{aligned}
h_{\mathrm{AA}}^{\mathrm{cc}}(r) & =\frac{1-\phi}{\phi} I_{\mathrm{AA}}^{\phi}(r)+\gamma^{2} I_{\mathrm{AA}}^{\rho}(r) \\
h_{\mathrm{BB}}^{\mathrm{cc}}(r) & =\frac{\phi}{1-\phi} I_{\mathrm{BB}}^{\phi}(r)+\gamma^{-2} I_{\mathrm{BB}}^{\rho}(r) \\
h_{\mathrm{AB}}^{\mathrm{cc}}(r) & =-I_{A B}^{\phi}(r)+I_{\mathrm{AB}}^{\rho}(r)
\end{aligned}
\tag{9}
$$

where $I_{\alpha \beta}^{\phi}(r)$ and $I_{\alpha \beta}^{\rho}(r)$ identify the concentration and density fluctuation contributions, respectively. We introduce here a compact notation with the function $I_{\alpha \beta}^{\lambda}(r)$ defined as

$$
\begin{gathered}
I_{\alpha \beta}^{\lambda}(r)=\frac{3}{4} \sqrt{\frac{3}{\pi}} \frac{\xi_{\rho}^{\prime}}{R_{\mathrm{g} \alpha \beta}} \vartheta_{\alpha \beta 1}\left(1-\frac{\xi_{\mathrm{c} \alpha \beta}{ }^{2}}{\xi_{\lambda}{ }^{2}}\right) \mathrm{e}^{-3 r^{2} /\left(4 R_{\mathrm{g} \alpha \beta}{ }^{2}\right)} \\
-\frac{1}{2} \frac{\xi_{\rho}^{\prime}}{r} \vartheta_{\alpha \beta 2}\left(1-\frac{\xi_{\mathrm{c} \alpha \beta}{ }^{2}}{\xi_{\lambda}{ }^{2}}\right)^{2} \mathrm{e}^{R_{\mathrm{g} \alpha \beta}{ }^{2} /\left(3 \xi_{\lambda}{ }^{2}\right)}\left[\mathrm{e}^{r / \xi_{\lambda}} \operatorname{erfc}\left(\frac{R_{\mathrm{g} \alpha \beta}}{\xi_{\lambda} \sqrt{3}}+\frac{r \sqrt{3}}{2 R_{\mathrm{g} \alpha \beta}}\right)\right. \\
\left.-\mathrm{e}^{-r / \xi_{\lambda}} \operatorname{erfc}\left(\frac{R_{\mathrm{g} \alpha \beta}}{\xi_{\lambda} \sqrt{3}}-\frac{r \sqrt{3}}{2 R_{\mathrm{g} \alpha \beta}}\right)\right]
\end{gathered}
\tag{10}
$$

and

$$
\vartheta_{\alpha \beta 1}=\frac{\left(1-\frac{\xi_{\mathrm{c} \alpha \alpha}{ }^{2} \xi_{\mathrm{c} \beta \beta}{ }^{2}}{\xi_{\mathrm{c} \alpha \beta}{ }^{2} \xi_{\lambda}{ }^{2}}\right)}{\left(1-\frac{\xi_{\mathrm{c} \alpha \beta}{ }^{2}}{\xi_{\lambda}{ }^{2}}\right)}
\tag{11}
$$

$$
\vartheta_{\alpha \beta 2}=\frac{\left(1-\frac{\xi_{\mathrm{c} \alpha \alpha}{ }^{2}}{\xi_{\lambda}{ }^{2}}\right)\left(1-\frac{\xi_{\mathrm{c} \beta \beta}{ }^{2}}{\xi_{\lambda}{ }^{2}}\right)}{\left(1-\frac{\xi_{\mathrm{c} \alpha \beta}{ }^{2}}{\xi_{\lambda}{ }^{2}}\right)^{2}}
\tag{12}
$$

where $\xi_{\lambda} \in\left\{\xi_{\phi}, \xi_{\rho}\right\}$ and $\xi_{\rho}^{\prime}=3 /\left(\pi \rho \sigma_{\mathrm{AB}}{ }^{2}\right)$. Radii of gyration in the blend are defined such that $2 R_{\mathrm{g} \alpha \beta}{ }^{2}=R_{\mathrm{g} \alpha}{ }^{2}+R_{\mathrm{g} \beta}{ }^{2}=4 \xi_{\mathrm{c} \alpha \beta}{ }^{2}$, with $\xi_{\mathrm{c} \alpha \alpha} \equiv \xi_{\mathrm{c} \alpha}$.

The development presented here is the required input to the derivation of the effective pair interaction potentials, a topic that will be addressed in the following section.

### 3. The Effective Soft-Core Potential

Our theoretical approach is based on an integral equation description of intermolecular pair correlation functions. A closure approximation is needed to connect these liquid structure functions to the effective pair interaction potentials which are required to perform, in our case, mesoscopic simulations of polymer mixtures mapped onto ensembles of soft colloidal particles. Since the fundamental units in our description interact through a soft-core potential, use is made of the hypernetted-chain (HNC) closure, which is known to be accurate for such systems. $^{45}$ The relationship connecting the effective pair interaction potential $v_{\alpha \beta}^{\mathrm{cc}}(r)$ with pcfs is given by the HNC closure as

$$
\left(k_{\mathrm{B}} T\right)^{-1} v_{\alpha \beta}^{\mathrm{cc}}(r)=h_{\alpha \beta}^{\mathrm{cc}}(r)-\ln \left[1+h_{\alpha \beta}^{\mathrm{cc}}(r)\right]-c_{\alpha \beta}^{\mathrm{cc}}(r)
\tag{13}
$$

where $c_{\alpha \beta}^{\mathrm{cc}}(r)$ is the direct pcf. Following the matrix definitions presented in section 2, and taking our system to be a simple liquid comprised by soft colloidal particles, the direct pair correlation functions are defined by

$$
\begin{gathered}
c_{\alpha \alpha}^{\mathrm{cc}}(k)=\frac{1}{\rho_{\mathrm{c}, \alpha}}-\frac{S_{\beta \beta}^{\mathrm{cc}}(k)}{\left(\rho_{\mathrm{c}, \alpha}+\rho_{\mathrm{c}, \beta}\right)\left|\mathbf{S}_{\mathrm{cc}}(k)\right|} \\
c_{\alpha \beta}^{\mathrm{cc}}(k)=\frac{S_{\alpha \beta}^{\mathrm{cc}}(k)}{\left(\rho_{\mathrm{c}, \alpha}+\rho_{\mathrm{c}, \beta}\right)\left|\mathbf{S}_{\mathrm{cc}}(k)\right|}
\end{gathered}
\tag{14}
$$

where $S_{\beta \beta}^{\mathrm{cc}}$ and $S_{\alpha \beta}^{\mathrm{cc}}$ are the static structure factors for a binary mixture, and $\left|\mathbf{S}_{\mathrm{cc}}(k)\right|=S_{\mathrm{AA}}^{\mathrm{cc}}(k) S_{\mathrm{BB}}^{\mathrm{cc}}(k)-\left[S_{\mathrm{AB}}^{\mathrm{cc}}(k)\right]^{2}$ is the determinant of the mesoscopic static structure factor matrix. For a binary mixture these static structure factors are given by

$$
\begin{gathered}
S_{\mathrm{AA}}(k)=\phi+\phi^{2} \rho_{\mathrm{ch}} h_{\mathrm{AA}}^{\mathrm{cc}}(k) \\
S_{\mathrm{BB}}(k)=1-\phi+(1-\phi)^{2} \rho_{\mathrm{ch}} h_{\mathrm{BB}}^{\mathrm{cc}}(k) \\
S_{\mathrm{AB}}(k)=\phi(1-\phi) \rho_{\mathrm{ch}} h_{\mathrm{AB}}^{\mathrm{cc}}(k)
\end{gathered}
\tag{15}
$$

where the total chain density $\rho_{\mathrm{ch}}=\rho / N$. By inserting eqs 9 and 14 into eq 13 , the $v_{\alpha \beta}^{\mathrm{cc}}(r)$ are obtained.

Since the potential is obtained from an inversion procedure utilizing the HNC closure, the adequacy of this method is limited to systems for which the HNC is valid, which includes the weakly interacting soft particles modeled here. However, for systems of

![](./images/811798120944893953_1.jpg)

Figure 1. Comparison of the effective pair interaction potential $v_{\alpha \beta}(r)$ derived from the HNC closure for the hhPP/PE blend, $\phi=0.5$, with $\chi / \chi_{s} \in\{0.0,0.1$, $0.3,0.5,0.7,0.9\}$. The upper panels show $v^{\mathrm{cc}}(r)$ obtained via the Padé approximation, and the lower panels show $v^{\mathrm{cc}}(r)$ from the Debye form. The inset highlights the change in the repulsive part of the potential as the reduced temperature is changed. The solid line represents the athermal regime $(\chi / \chi_{s}=0.0)$. In both the AA and BB curves, the repulsive component decreases as the system approaches the spinodal $(\chi / \chi_{s}=1)$, whereas the AB curve increases.

hard spheres or for low density ionic fluid models, such as the restricted primitive model (RPM), the HNC has been shown to be inaccurate, $^{46}$ and more sophisticated closures are required. $^{32,47}$

The analytical solution of our mesoscopic approach represents an advantage to previous work, where effective pair potentials are derived from simulations performed on a microscopic level. Such a requirement partially defeats the computational time gains behind a coarse-graining procedure. Overall, our approach by- passes the need to perform atomistic simulations for each thermodynamic state point of interest, which is necessary in numerical implementations since the effective pair interaction potentials depend on the state of the system. This can be readily appreciated from the pcfs that enter into the HNC closure, which are themselves state-dependent.

We investigated the effect that the use of the Debye formalism, eq 5, or of its Padé approximant, eq 6, for the monomer form factor in the denominator of eq 3 has on the calculation of the potential. The Padé approximant is less precise than the Debye equation, but it allows for the analytical solution of the total correlation functions, eq 9. We observe that when eq 6 is used, singular points arise in the low $k$ regime in the solution of eq 14 for $c^{\mathrm{cc}}(k)$ as the determinant of the mesoscopic static structure factor, $|\mathrm{S}_{\mathrm{cc}}(k)|=S_{\mathrm{AA}}^{\mathrm{cc}}(k) S_{\mathrm{BB}}^{\mathrm{cc}}(k)-[S_{\mathrm{AB}}^{\mathrm{cc}}(k)]^{2}$, passes through zero. This corresponds to an unphysical region of negative compressibility. When eq 5 is used instead, such singular points do not arise.

For homopolymer melts, it has previously been determined that the singularities in $c^{\mathrm{cc}}(k)$ occur as a result of the intrinsic error introduced in eq 6 by the Padé approximation. $^{42}$ In order to obtain a usable form of the effective potential from eq 13, we tested two schemes: in scheme 1, we enforced the condition that $c^{\mathrm{cc}}(k=0) \leq c^{\mathrm{cc}}(k) \leq 0$ for low $k$, which effectively eliminates any singularities from the direct correlation function; in scheme 2, we enforced the isothermal compressibility limit, such that for regions where $|\mathrm{S}_{\mathrm{cc}}(k)| \leq |\mathrm{S}_{\mathrm{cc}}(0)|$, we truncated $h^{\mathrm{cc}}(k)$ so that $h_{\alpha \beta}^{\mathrm{cc}}(k)=h_{\alpha \beta}^{\mathrm{cc}}(k=0)$. The two schemes are equivalent and give identical results within the precision of our calculation. This is so because polymer liquids are almost incompressible.

<table>
 <thead>
  <tr>
   <th colspan="7">Table 1. Polyolefin Blends ($T = 453$ K, $N_{\text{A}} = N_{\text{B}} = 96$)</th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>blend [A/B]</td>
   <td>$\phi$</td>
   <td>$\rho$ [sites/Å³]</td>
   <td>$R_{\text{gA}}$ [Å]</td>
   <td>$\gamma$</td>
   <td>$\chi$</td>
  </tr>
  <tr>
   <td>hhPP/PE</td>
   <td>0.50</td>
   <td>0.0332</td>
   <td>12.32</td>
   <td>1.34</td>
   <td>$-0.0294 + 17.58/T^{a,b}$</td>
  </tr>
  <tr>
   <td>PIB/PE</td>
   <td>0.50</td>
   <td>0.0343</td>
   <td>9.76</td>
   <td>1.68</td>
   <td>$0.00257 + 4.99/T^{b}$</td>
  </tr>
  <tr>
   <td>PIB/sPP</td>
   <td>0.50</td>
   <td>0.0343</td>
   <td>9.76</td>
   <td>1.41</td>
   <td>$\cdots$</td>
  </tr>
  <tr>
   <td>sPP/PE</td>
   <td>0.50</td>
   <td>0.0328</td>
   <td>13.89</td>
   <td>1.19</td>
   <td>$\cdots$</td>
  </tr>
  <tr>
   <td>iPP/PE</td>
   <td>0.25</td>
   <td>0.0328</td>
   <td>11.35</td>
   <td>1.47</td>
   <td>$0.005^{c}$</td>
  </tr>
  <tr>
   <td>iPP/PE</td>
   <td>0.75</td>
   <td>0.0328</td>
   <td>11.33</td>
   <td>1.48</td>
   <td>$0.01^{c}$</td>
  </tr>
  <tr>
   <td>hhPP/PIB</td>
   <td>0.50</td>
   <td>0.0343</td>
   <td>12.4</td>
   <td>1.28</td>
   <td>$0.027 - 11.4/T^{b,d,e}$</td>
  </tr>
  <tr>
   <td colspan="6">$^{a}$Reference 48. $^{b}$Reference 49. $^{c}$Reference 13. $^{d}$Reference 14. $^{e}$Reference 50.</td>
  </tr>
 </tbody>
</table>

In this work, we study polymer blends of polyethylene (PE), polyisobutylene (PIB), and polypropylenes in their head-to-head (hhPP), isotactic (iPP), and syndiotactic (sPP) forms. The effec- tive pair potential, $v^{cc}(r)$, for interactions of type AA, BB, and AB is calculated for the different binary polymer mixtures and for hhPP:PE under different values of $\phi$ and $\chi$ using both the Debye form and Padé form of the intramolecular distribution function(eqs 5 and 6). As a model calculation of the potential, we present the results for the prototypical hhPP/PE polymer blend in Figure 1, which shows how the potential depends on the reduced temperature $(1 - \chi / \chi_{s})$. Input parameters to our theoretical calculations are reported in Table 1 as data for the UA simula- tions against which we test our approach. $^{13,14}$ Although there is a noticeable difference in the potential obtained using either eq 5 or6, they are qualitatively similar in many respects. For example, under athermal conditions, the mixture is random and the number of $AB$ contacts is in between those of the self-terms, $AA$ and $BB$. Correspondingly, pair interactions accounting for AB contacts must be intermediately repulsive. This effect is reflected in the plot of $v_{\alpha \beta}^{cc}(r)$. The A-type (flexible hhPP) particles display the highest repulsive response as a consequence of their stronger correlation hole effect. The inset of Figure 1 highlights

<table>
<caption>Table 2. Mesoscale Simulation Parameters for Blends of hhPP/PE</caption>
<thead>
<tr>
<th>form factor</th>
<th>interaction parameter</th>
<th>particles</th>
<th>$\boldsymbol{\phi}$</th>
<th>$\boldsymbol{L/2\ [R_{\rm g}^{-1}]}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>Padé</td>
<td>$\chi/\chi_{\rm s} = \{0.1, 0.3, 0.5, 0.7\}$</td>
<td>5324</td>
<td>0.5</td>
<td>8.549</td>
</tr>
<tr>
<td>Debye</td>
<td>$\chi/\chi_{\rm s} = \{0.1, 0.3, 0.5\}$</td>
<td>5324</td>
<td>0.5</td>
<td>8.549</td>
</tr>
<tr>
<td>Debye</td>
<td>$\chi/\chi_{\rm s} = 0.7$</td>
<td>10648</td>
<td>0.5</td>
<td>10.771</td>
</tr>
<tr>
<td>Debye</td>
<td>$\chi = \{0.008, 0.012, 0.016, 0.019\}$</td>
<td>10648</td>
<td>{0.5, 0.7, 0.9}</td>
<td>10.771</td>
</tr>
</tbody>
</table>

the change in the repulsive component in the potential, as the ratio, $\chi/\chi_{\rm s}$, is varied.

While the full Debye form (eq 5) for the monomer form factor prevents an explicit analytic expression for $h^{\rm cc}(r)$ in the form of eq 9, which was the motivation for adopting the Padé approximation, a numerically obtained $h^{\rm cc}(r)$ still can be readily obtained for any given system and so does not represent a limitation to our approach and avoids any singularities in the low $k$ region for $c^{\rm cc}(r)$. For this reason, in our following calculations the Debye approximation will be preferentially used.

The potentials $v_{\alpha\beta}^{\rm cc}(r)$, calculated following the procedures discussed here, are required to carry out the simulations of the polymer liquid on a mesoscopic level. In the next section, we discuss the implementation of the $v_{\alpha\beta}^{\rm cc}(r)$ to our mesoscopic simulations, and in the following sections we compare mesoscale simulation results with UA MD simulations and theoretical predictions.

### 4. Mesoscopic Simulations of Binary Mixtures

In this section, we implement molecular dynamics simulations for the systems presented in Table 1, and we describe our methodology for carrying out mesoscopic simulations.

In our mesoscopic modeling approach, we implement classical MD simulations, where the ensemble is evolved in the microcanonical ($N$, $V$, $E$) ensemble. In the initialization step, all particles are placed on a cubic lattice with periodic boundary conditions. We use reduced units such that all length units are scaled by $R_{\rm g}$ ($r^* = r/R_{\rm g}$) and energies scaled by $k_{\rm B}T$. The type of particle that occupies a particular site is determined at random. Even though the molecular center-of-mass coordinates from a UA MD simulation can be used as an initial point, our calculations were started afresh as a more stringent test of our procedure and to allow us to increase the number of particles in the system (or, equivalently, the spatial dimension) at will, capturing relevant features of the effective pair interaction potential and to improve the statistical sampling of the ensemble. The potential and its corresponding derivative are entered as tabulated inputs to the program, and linear interpolation was used to determine values not found in the supplied numerical data as the algorithm proceeds. Each site is given an initial velocity pooled from a Mersenne Twister random number generator. $^{51}$ Subsequently, the system is evolved using a velocity Verlet integrator. Equilibrium is induced in the ensemble by rescaling the velocity at regular intervals and is manifested in the system when observing a Maxwell−Boltzmann distribution of velocities, a steady temperature, a stabilized Boltzmann $H$-theorem function, and a decayed translational order parameter.

Once the equilibration step is completed, velocity rescaling is discontinued and trajectories are collected over a traversal of $\sim 8R_{\rm g}$. The fastest benchmark in our studies is for a duration of $\sim 4$ h for a system consisting of $\sim 6000$ particles, performed on a single-CPU workstation. This compares extraordinarily well with a UA implementation that requires $\sim 24$ h for a system with 1600 particles performed in parallel on a 64-node cluster $^{14}$ for an equivalent trajectory. We stress that our benchmarks for mesoscopic simulations represent an underestimate in the computational time since these have not been subjected to a parallelized algorithm.

<table>
<caption>Table 3. Mesoscale Simulation Parameters for Athermal Blends</caption>
<thead>
<tr>
<th>system</th>
<th>particles</th>
<th>$\boldsymbol{\phi}$</th>
<th>$\boldsymbol{L/2\ [R_{\rm g}^{-1}]}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>hhPP/PE</td>
<td>5324</td>
<td>0.5</td>
<td>8.549</td>
</tr>
<tr>
<td>PIB/PE</td>
<td>4096</td>
<td>0.5</td>
<td>8.365</td>
</tr>
<tr>
<td>PIB/sPP</td>
<td>5488</td>
<td>0.5</td>
<td>10.416</td>
</tr>
<tr>
<td>sPP/PE</td>
<td>1728</td>
<td>0.5</td>
<td>5.635</td>
</tr>
<tr>
<td>iPP/PE</td>
<td>4913</td>
<td>0.25</td>
<td>8.482</td>
</tr>
<tr>
<td>iPP/PE</td>
<td>1728</td>
<td>0.75</td>
<td>6.016</td>
</tr>
</tbody>
</table>

Extensive mesoscale simulations were performed on a typical system, the hhPP/PE mixture, to investigate the consistency of our approach. Simulations were performed for compositionally symmetric mixtures, but also while approaching the spinodal, $\chi = \{0.008, 0.012, 0.016, 0.019\}$, while changing the fraction of A and B species in the melt such that $\phi = \{0.5, 0.7, 0.9\}$. Mesoscale simulation parameters for all of the hhPP/PE systems are presented in Table 2. For systems with $\chi$ approaching $\chi_{\rm s}$, larger simulation boxes, with 10648 particles, were used to properly account for the increase in the length scale of concentration fluctuations. Those systems also required longer equilibration. These simulations were run using the LONI TeraGrid system $^{52}$ to facilitate performing numerous simulations at a time.

### 5. Total Pair Correlation Functions of the Polymer Mixture from Mesoscale Simulations

From the trajectories of our mesoscopic simulations, the intermolecular total pcfs are computed. Initially, we set $\chi = 0$ to determine the liquid structure far from the spinodal temperature, i.e. under athermal conditions, $(1 - \chi/\chi_{\rm s}) = 1$. Mesoscale simulation parameters for these blends are presented in Table 3. For these simulations we compare the resulting pcfs to UA MD simulations. To obtain center-of-mass distribution functions from UA simulations, the center-of-mass coordinates for each chain are evaluated at each time step as the averaged sum of the position coordinates of each united atom. The radial distribution of center-of-mass coordinates is evaluated in the usual method employed for liquids. $^{53}$ The resulting pcfs are shown in Figure 2 for the systems listed in Table 1. Mesoscopic simulations are found to yield a coarse-grained liquid structure in agreement with our theoretical predictions from the analytical expression of eq 9, serving as a self-consistent check of our determination of the effective pair potential through the HNC closure. The results presented in Figure 2 were obtained using the Padé approximation (eq 6) which works sufficiently well under athermal conditions where the low $k$ behavior is less important since critical fluctuations are assumed to be small.

The liquid structure from mesoscopic simulations are in general consistent with data obtained from UA MD simulations, with the exception of blends containing iPP and PIB for which theoretical predictions and mesoscopic MD predict a less pronounced correlation hole than UA MD simulations. These observations are not surprising since these systems tend to possess very efficient intramolecular packing, leading to smaller isothermal compressibilities and thermal expansion coefficients when compared to other polyolefin blends. $^{14,50}$ The effective intramolecular packing arises from the attractive interactions between

![](./images/811798120944893953_2.jpg)

Figure 2. Comparison of mesoscopic simulations [open symbols] with UA MD simulations [filled symbols] for the $h_{\alpha\beta}(r)$ of polymer mixtures under athermal conditions. Also shown are theoretical predictions [solid curves] based on our analytic expression, eq 9. Presented are data from AA [circles], AB [triangles], and BB [squares] contributions for compositionally symmetric and asymmetric systems. For comparison, numerical predictions obtained from eq 3 using the Debye form are shown [dashed curves]. For clarity, the inset highlights the peak region for each separate contribution.

methyl moieties induced by their geometrical arrangement. However, the theory and mesoscopic simulations do exhibit good agreement for $r \approx R_{\text{g}}$.

Moving to the thermal regime, where large-scale fluctuations in the local concentration develop as the system approaches a second-order phase transition, we present results for the typical 50:50 mixture of hhPP/PE, although the theory and methods employed are ubiquitous and generally applicable to a wide range of systems. For these simulations the value of the $\chi$ parameter was varied such that $\chi/\chi_{\text{s}} = \{0.1, 0.3, 0.5, 0.7\}$ in order to see the changes in the pcfs as the system approaches the spinodal. Figure 3 shows the dependence of the partial correlation functions on the interaction parameter, $\chi$. The left side of Figure 3 shows the resulting correlation function from mesoscale simulations with the potential obtained via the Padé approximation, after using our truncation scheme for $c^{\text{cc}}(r)$ in the HNC (see upper panels Figure 1). Use of the Padé approximation has the advantage of allowing a fully analytic solution for $h^{\text{cc}}(r)$, as shown in eq 9, which shows quantitative agreement with UA simulations in the athermal limit (as shown in Figure 2).

The right panels of Figure 3 shows the correlation function obtained using the potential derived from the Debye form (see lower panels of Figure 1). Here, comparison is again made to numerical predictions based on eq 3, since an analytic solution, such as that of eq 9, is not possible when the Debye form is used. In both the right and left panels of Figure 3 mesoscopic simulations show quantitative agreement with our theoretical predictions, indicating the self-consistency of our approach. Furthermore, despite the differences in the potential used in the simulation, Figure 3 shows that the resulting pcfs from either the Padé or Debye form are qualitatively similar. Lastly, we note that despite the approximations made in obtaining the analytical

![](./images/811798120944893953_3.jpg)

Figure 3. Comparison of mesoscopic simulations [symbols] with numerical predictions [curves] for the $h_{\alpha\beta}(r)$ of a 50:50 mixture of hhPP/PE for different values of the ratio, $\chi/\chi_{s}$. The left panel shows results obtained using the Padé approximation with our truncation scheme. The right panel depicts the results when the Debye form is used. Mesoscale simulations are shown to capture the structural changes that occur as the system approaches the spinodal. The inset highlights the peak region of $h(r)$.

form of eq 9, our analytical expressions recover the correct $k=0$ limit. $^{33,34}$ In fact, all of the forms for $h^{cc}(k)$ exhibit the same $k=0$ behavior.

The standard approach to describe the mixing behavior of polymers is the Flory-Huggins model. Under Flory-Huggins treatment, the phenomenon of demixing is understood in terms of contributions to the free energy of mixing. Generally, at low enough temperatures the translational entropy, which is asso- ciated with the center-of-mass motion of the molecules and always favors mixing, is outweighed by local monomer- monomer interactions. In most cases, van der Waals interactions are stronger between like pairs than those between unlike pairs, resulting in a positive free energy of mixing. As a result, lower temperature favors spontaneous demixing due to changes in the local free energy of the system. $^{1}$ In an empirical manner, the Flory-Huggins parameter, $\chi$, is used to describe these changes in local free energy. At the limit of the spinodal temperature, $\chi \to \chi_{s}$ , and since $\chi \propto 1 / T$ , positive values of $\chi$ always lead to incompatibility of the mixture. $^{1}$

In real systems, the simple Flory-Huggins model does not hold, and the $\chi$ parameter may be a complicated function of $N, \phi$ , and $T$ , leading to the variety of phase behaviors observed in polymer blends. For example, some blends phase separate upon cooling, while others show an opposite trend in demixing and phase separate upon heating. It is customary to fit the experi- mental temperature dependence of a mixture to the form $\chi=a+$  $b / T$ , where $a$ and $b$ may be either positive or negative depending on the system. Table 1 shows the experimentally determined $a$ and $b$ parameters for a few of the systems investigated in this paper. It should be noted that when applying an equation for the

![](./images/811798120944893953_4.jpg)

Figure 4. Comparison of mesoscopic simulations [symbols] with numerical predictions [curves] for the $h_{\alpha \beta}^{cc}(r)$ of hhPP/PE for different values of $\phi$. Left panels show data when $\chi=0.008$. Right panels show data for $\chi=0.012$. Shown are the separate contributions for AA [circles], AB [triangles], and BB [squares] interactions. As $\phi$ increases, the fraction of species B in the simulation box decreases, and thus, the statistics become poorer for BB interactions.

$\chi$ parameter from the literature, the $\chi$ value must be normalized by the average number of UA sites per monomer $^{14}$ to be consistent with the site-basis description adopted here.

In our present treatment, the interaction parameter $\chi$ is treated as an adjustable parameter, which describes the interactions that drive phase separation. It is analogous to the Flory-Huggins parameter; however, since in our model it represents a system specific parameter, it may be given any value positive or negative depending on the behavior of the system of interest. The advantage of a mesoscale approach is that once the system specific parameters are defined, the trends in phase behavior can be readily calculated without requiring restrictively large MD simulations.

As a further implementation of our theory, we perform mesoscale simulations at several fixed values of $\chi$ for which the fraction of A and B species in the melt is varied. For these simulations, we again use hhPP/PE as a typical system and vary the volume fraction such that $\phi=\{0.5,0.7,0.9\}$. In order to better capture the large-scale structural changes, simulations were performed in a large box with 10 648 particles. Figure 4 shows the resulting pair correlation functions for mesoscale simulations run with $\chi=0.008$ and $\chi=0.012$, and Figure 5 shows the case where $\chi=0.016$ and $\chi=0.019$. In all cases, mesoscale simulations correctly capture the structural changes that depend on the concentrations of the species in the mixture when comparison is made with our theoretical predictions. For these simulations we

![](./images/811798120944893953_5.jpg)

Figure 5. Same as Figure 4, except that left panels show data when $\chi = 0.016$ and right panels show data for $\chi = 0.019$.

limit our consideration to using only the Debye form in eq 3 to avoid any effects due to the truncation scheme in the low $k$ region. Once more, theory and mesoscale simulations appear to be fully consistent in predicting the structural information on the mixture in the length scales larger or equal to the polymer radius of gyration.

### 6. Scattering Functions and Concentration Fluctuations

The mesoscale pair correlation functions effectively describe the polymer fluid as a liquid of soft colloidal particles. Once these pcfs are obtained from simulation, any property of the liquid can be calculated, including the equation of state, internal energy, compressibility, and others. $^{45}$ In this section, we examine the extent to which our classical MD simulations of soft colloidal particles reproduce the structural changes which occur as the system approaches the spinodal. Because of the increasing length scale of fluctuations as the system approaches the critical temperature for demixing, UA simulations can only reach a very limited region of the phase diagram. An advantage of using a procedure that captures the structure at the mesoscopic scale is that the relevant length scale of the simulation can increase considerably with respect to UA MD, and simulations can describe the increasing length scale of the fluctuations. Thus, a mesoscopic picture greatly facilitates the ability to capture this phenomenon, since we are able to simulate many thousands of chains represented as soft spheres. Models using Monte Carlo methods with phenomenological potentials have been previously performed at the level of soft colloids, demonstrating the valuable information that may be gained about phase transitions. $^{31,54}$ The advantage of the procedure presented here is that the potentials used to simulate the system are explicitly parameter dependent, being related to the system-specific molecular parameters, such as $R_{\mathrm{g}}$. The potentials obtained in this manner allow for mesoscale simulations to be performed on any number of different,

![](./images/811798120944893953_6.jpg)

Figure 6. Top left: partial structure factor, $S^{\phi \phi}(k)$, obtained from mesoscopic simulations [symbols] of the coarse-grained mixture of 50:50 hhPP/PE with $\chi/\chi_{\mathrm{s}} \in \{0.0, 0.1, 0.3, 0.5, 0.7\}$. The curves represent theoretical values obtained using the Debye function. Partial structure factor $S^{\rho \rho}(k)$ (top right) and $S^{\rho \phi}(k)$ (bottom left) are also shown for different values of $\chi/\chi_{\mathrm{s}}$. $S^{\rho \rho}(k)$ does not change noticeably with $\chi/\chi_{\mathrm{s}}$, but $S^{\rho \phi}(k)$ has a slight $\chi/\chi_{\mathrm{s}}$ dependence at low $k$. Bottom right: extrapolated $1/S^{\phi \phi}(0)$ values vs $\chi$ [symbols]. The line represents a linear fit to the data and is extrapolated to the spinodal, $\chi_{\mathrm{s}}$ (dashed line).

but specific, systems under different thermodynamic conditions, mapping them as soft colloids.

The static structure factors for each component are calculated from our simulations by Fourier transform of the total correlation function

$$
S_{\mathrm{AA}}(k)=\phi+4 \pi \phi^{2} \rho_{\mathrm{ch}} \int_{0}^{\infty} r^{2} \frac{\sin k r}{k r} h_{\mathrm{AA}}(r) \mathrm{d} r
$$

$$
S_{\mathrm{BB}}(k)=1-\phi+4 \pi(1-\phi)^{2} \rho_{\mathrm{ch}} \int_{0}^{\infty} r^{2} \frac{\sin k r}{k r} h_{\mathrm{BB}}(r) \mathrm{d} r \quad(16)
$$

$$
S_{\mathrm{AB}}(k)=4 \pi \phi(1-\phi) \rho_{\mathrm{ch}} \int_{0}^{\infty} r^{2} \frac{\sin k r}{k r} h_{\mathrm{AB}}(r) \mathrm{d} r
$$

Density and concentration fluctuation contributions can be written as linear combinations of the static structure factors according to the formalism of Bhatia and Thornton. $^{36}$ Here, the density fluctuation, $S^{\rho \rho}(k)$ is given by

$$
S^{\rho \rho}(k)=S_{\mathrm{AA}}(k)+S_{\mathrm{BB}}(k)+2 S_{\mathrm{AB}}(k) \quad(17)
$$

The concentration fluctuation contribution, $S^{\phi \phi}(k)$, may be expressed as

$$
S^{\phi \phi}(k)=(1-\phi)^{2} S_{\mathrm{AA}}(k)+\phi^{2} S_{\mathrm{BB}}(k)-2 \phi(1-\phi) S_{\mathrm{AB}}(k) \quad(18)
$$

and is particularly important since it provides information about the stability of the binary mixture against demixing. The coupling term, $S^{\rho \phi}(k)$, is given by

$$
S^{\rho \phi}(k)=(1-\phi) S_{\mathrm{AA}}(k)-\phi S_{\mathrm{BB}}(k)+(1-2 \phi) S_{\mathrm{AB}}(k) \quad(19)
$$

Figure 6 shows the colloidal partial structure factors, $S^{\rho \rho}(k), S^{\phi \phi}(k)$, and $S^{\rho \phi}(k)$, calculated from pcfs obtained from mesoscopic simulations shown in the right panel of Figure 3 using eqs 17−19. The data from the simulation is compared to predictions based on our numerical values for $h^{\mathrm{cc}}(k)$, obtained from eq 3 using the Debye function. Since it is particularly pertinent to capture the low $k$ behavior where concentration fluctuations will diverge as the spinodal is approached, we use the results for the Debye form since the Padé approximation introduces unphysical effects in this regime, typically for $k R_{\mathrm{g}}<2$. As seen in Figure 6, the curves of the density fluctuation contribution, $S^{\rho \rho}(k)$, which behaves similarly to the static structure factor for a single-component liquid, $^{34}$ are indistinguishable over the range of $\chi$ investigated. The function $S^{\phi \phi}(k)$ exhibits a slight dependence on the ratio $\chi/\chi_{\mathrm{s}}$ in which the minimum at low $k$ becomes slightly more pronounced. The minimum in $S^{\phi \phi}(k)$ represents the length scale for asymmetry in the mixture arising from the difference in particle size. $^{34}$ The partial structure factor, $S^{\phi \phi}(k)$, exhibits a characteristic diverging behavior as the spinodal is approached, indicating an increase in the length scale of concentration fluctuations.

![](./images/811798120944893953_7.jpg)

Figure 7. Concentration fluctuation partial structure factor, $S^{\phi \phi}(k)$, calculated from mesoscale simulations [filled symbols] at different values of $\phi$ for the mixture hhPP/PE. The curves represent theoretical predictions.

As illustrated in the upper left of Figure 6, $S^{\phi \phi}(0)$ increases as the ratio $\chi/\chi_{\mathrm{s}} \to 1$. As the system nears the phase transition, the divergence of $S^{\phi \phi}(k)$ is indicative of the concentration fluctuations becoming increasingly macroscopic. Since concentration fluctuations occur on an increasingly large scale, the relevant region of the $S^{\phi \phi}(k)$ curve occurs in the low $k$ region; however, because of periodic boundary conditions, simulation data are only reliable at a distance less than half the length of the simulation box. This makes extrapolation of the $k=0$ limit from mesoscopic simulations still difficult, as seen in Figure 6, even though thousands of particles were represented. In this respect, our numerical predictions may serve as a guide for extending $S(k)$ to the $k=0$ limit. Furthermore, we have previously shown that eq 9 also gives an estimate for $S^{\phi \phi}(0)$ given by $^{34}$

$$
S^{\phi \phi}(0)=\frac{\phi(1-\phi)}{1-\chi / \chi_{\mathrm{s}}}+\frac{\phi^{2}(1-\phi)^{2}\left(\gamma^{2}-1\right)^{2}}{\left(\phi \gamma^{2}+1-\phi\right) \gamma^{2}} \frac{\xi_{\rho}{ }^{2}}{\xi_{\mathrm{cA}}{ }^{2}} \quad(20)
$$

Even though it is based on the Padé approximation, eq 20 may be used to estimate $S^{\phi \phi}(0)$ since $h^{\mathrm{cc}}(k)$ calculated from the Padé approximation has the same $k=0$ limit as $h^{\mathrm{cc}}(k)$ from the Debye form. The lower right of Figure 6 shows a linear plot of $1/S^{\phi \phi}(0)$ vs $\chi$ for which the $k=0$ limit was determined by our theoretical predictions.

Following eqs 16−19, the concentration fluctuation partial structure factor, $S^{\phi \phi}(k)$, was calculated from the mesoscale simulations presented in Figures 4 and 5, where the volume fraction, $\phi$, was changed. The resulting $S^{\phi \phi}(k)$ is presented in Figure 7 along with theoretically predicted values using the Debye formula. Once again, mesoscale simulations show an increase in concentration fluctuations as the thermodynamic conditions are changed, and $\chi \to \chi_{\mathrm{s}}$ or $\phi \to 0.5$. In general, mesoscale simulations are consistent with our theoretical predictions based on eq 3 up to the limit set by the finite box size. As seen in Figure 7, when $\chi$ is low or the polymer volume fraction of one species is large, the system is well mixed and the extrapolation to low $k$ is straightforward. However, for the case when $\phi=0.5$ and $\chi=0.019$, as depicted in the lower right panel of Figure 7, it becomes more difficult to reach the $k=0$ limit from mesoscale simulation, even if the precision is higher than for atomistic simulations for the reasons previously discussed. Since our simulations are consistent with our theoretical predictions as shown in Figures 2−5, we estimate the extrapolated $S(k=0)$ limit based on these predictions.

Once this method is employed, it is possible to discern the phase behavior of the mixture from the extrapolated $k=0$ limit. In order to include more data points, we calculate $S^{\phi \phi}(0)$ for a range of $\chi$ and $\phi$ values, based on our solution to eq 3. These are presented in Figure 8, which shows the structure factor as a function of the volume fraction for several fixed values of the $\chi$ parameter. The interpolation between the points is given by eq 20, which demonstrates that our analytical expression is useful in determining the phase behavior.

Finally, in Figure 9 a plot of the inverse structure factor, $S^{\phi \phi}(0)$, vs $\chi$ at each value of $\phi$ shows the linear behavior from which the spinodal, $\chi_{\mathrm{s}}$, may be extrapolated and used to sketch

![](./images/811798120944893953_8.jpg)

Figure 8. Extrapolated $k = 0$ limit of $S^{\phi\phi}(k)$ based on our numerical predictions [data points] and from our analytical expression, eq 20 [curves], as a function of $\phi$ for different fixed values of $\chi$, for the mixture hhPP/PE.

![](./images/811798120944893953_9.jpg)

![](./images/811798120944893953_10.jpg)

Figure 9. Top: inverse concentration fluctuation structure factor, $S^{\phi\phi}(0)$, plotted against the interaction parameter, $\chi$, for different values of $\phi$, for the mixture hhPP/PE. The solid line depicts a linear fit to the data, and the dashed line shows the extrapolation to the spinodal. Bottom: phase diagram for the coarse-grained mixture obtained from the above extrapolation to the spinodal, $\chi_s$. The solid curve depicts the Flory−Huggins analytical expression.

the phase diagram of the system. In the bottom panel of Figure 9 the spinodal curve is compared to the predicted Flory−Huggins model, $\chi_s=[2N_{\text{A}}\phi]^{-1}+[2N_{\text{B}}(1-\phi)]^{-1}$, which was used in eq 8.

The spinodal curve from our simulation exhibits a characteristic parabolic shape consistent with mean-field theory, where $\xi_{\phi}\sim(1 - \chi/\chi_s)^{-\nu}$, $\nu = 1/2$. In the immediate region of the critical temperature, mean-field theory breaks down, and Ising-type critical behavior is expected. For this narrow temperature region, the linear extrapolation in Figure 9 would be invalid and the spinodal will exhibit a flatter peak. $^{54}$ For long polymer chains, the temperature region for which mean field theory becomes invalid is very small, since the Ginzburg number, which scales inversely with $N$, is small. $^{11}$ As seen in the upper panel of Figure 9, most of the simulations performed are well within the temperature region described by mean-field theory. Although the linear extrapolation becomes less quantitative near the horizontal axis, the mean-field approximation is consistent withour data.

### 7. Corrections to the Debye Intramolecular Form Factor

Upon examination of Figure 2, it appears that there is slightly better agreement between UA MD simulations when compared to our analytical results using the Padé approximation than with the full Debye form (as indicated by the dashed lines). Since the Padé form is an approximation, this improvement is likely due to a cancellation of errors. The Debye formula is exact for ideal Gaussian chains; however, Wittmer et al. have recently shown that dense polymer melts exhibit deviations from ideal Gaussian behavior because of long-range correlations arising from the repulsive interaction of chain segments. $^{55}$ These deviations become more significant for polymers confined between walls in ultrathin films. $^{56}$ In this section we investigate the implementation of higher order corrections to the Gaussian approximation on the effective pair potential by evaluating eq 3 numerically with a corrected from of the intramolecular form factor.

In the infinite chain limit $(N\rightarrow\infty)$ it has been proposed that corrections to the Debye formula in the intermediate wave vector range depends only on the monomer density, such that $^{55,57}$

$$
\frac{1}{\omega^{\text{mm}}(k)}=\frac{1}{\omega_{\text{Debye}}^{\text{mm}}(k)}+\frac{1}{32}\frac{k^3}{\rho} \tag{21}
$$

Although approximate for finite chain lengths, eq 21 was input into eq 3 to obtain a corrected form of the pair potential which is shown in Figure 10 (top left) for a 50:50 mixture of hhPP/PE. The resulting correlation functions, displayed in Figure 10, show that the corrected Debye formula agrees very well with UA MD simulations for this sample, indicating that the disagreement between mesoscale simulations using the Debye formula and UA simulations on intermediate length scales is due to non-Gaussian behavior of real chains as the Flory ideality hypothesis breaks down. On the local scale, however, the corrected Debye and the UA-MD simulations tend to disagree. This is not relevant for systems with long chains, such as the hhPP:PE mixture, but it becomes important for short chains, e.g. mixtures of PIB chains, where the behavior at short distance becomes unphysical. In conclusion, while in the current publication we limit our investigation to just this correction term for the hhPP:PE mixture, further study is necessary to investigate if the observed improvement is a common feature of long-chain mixtures, independent of their monomeric structures. The pcf$s$ obtained using the Padé approximation (Figure 2) are also shown in Figure 10 and compare well with the corrected Debye results.

### 8. Applications to Miscible LCST Blends

While most polymer blends are immiscible and tend to demix at experimentally relevant temperatures, some systems are known to be miscible having a lower critical solution temperature

![](./images/811798120944893953_11.jpg)

![](./images/811798120944893953_12.jpg)

![](./images/811798120944893953_13.jpg)

![](./images/811798120944893953_14.jpg)

Figure 10. Top left: effective pair potential between A type chains for an athermal mixture of hhPP/PE with $\phi = 0.5$ when corrections to the Debye formula are included (solid line). The dashed line indicates the potential obtained using the uncorrected Debye formula. Top right: the AA component of the correlation function calculated from mesoscale simulations using the corrected Debye formula at $\chi = 0.0$ (open circles) and $\chi = 0.7$ (open triangles). The solid line represents theoretical predictions, and the dashed line indicates predictions using the Debye formula. Filled circles represent UA MD simulations. BB component (bottom left) and AB component (bottom right) of the correlation function for the same mixture. The pcfs obtained using the Padé approximation are shown to nearly superimpose with the corrected Debye form (partially shaded circles).

(LCST). In this section we demonstrate the extension of our approach to model LCST blends where the effective $\chi$ parameter may be negative over most of the temperature range of interest. It is worth noticing that while the hhPP/PIB blend is miscible, the iPP/PIB blend is immiscible, indicating that subtle changes in the specific polyolefin architecture may give rise to a completely different phase diagram. The temperature dependence of the $\chi$ parameter for the miscible hhPP/PIB blend is reported in Table 1. The $\chi$ parameter in the literature is defined on a monomer basis and must be divided by the number of united atom sites per monomer (4.8 for hhPP/PIB) to be consistent with the UA site description used here. We performed mesoscale simulations for various temperatures of a mixture of 50:50 hhPP/PIB ($\chi_{\text{s}} = 0.021$).

The resulting correlation functions determined for two temperatures, 2000 K and 200 K, from mesoscale simulations are shown in Figure 11. When compared with Figure 3, it is evident that the pcfs for the hhPP/PIB blend exhibit an opposite trend with temperature. These differences are clearly evident in the concentration fluctuation structure factor, which was calculated from these pcfs at various temperatures and is shown in the bottom right of Figure 11. As depicted in the low wave vector behavior of $S^{\phi\phi}(k)$, fluctuations in the concentration become smaller as the temperature is decreased, and the system becomes more stable. These results indicate that our procedure of mapping polymer blends as soft colloids and performing mesoscopic simulations using an effective pair potential can be applied to miscible LCST blends given that the temperature dependence of the $\chi$ parameter is known.

### 9. Summary

In this paper, we present the implementation of our analytical coarse-grained description for polymer mixtures in mesoscopic modeling through computer simulation. Using the analytical representations for the intermolecular total pair correlation functions at the center-of-mass level and the hypernetted-chain closure, we derive the effective pair interaction potentials which are the required input to the coarse-grained simulations. The simulations are then carried out, and the coarse-grained liquid structure, as given by the intermolecular pair correlation function, is extracted from the trajectories. In the athermal regime, results are compared with our theoretical predictions and data obtained from united atom molecular dynamics simulations. In the thermal regime, mesoscopic simulations capture the relevant trends for demixing of polymers in the miscible regime approaching the spinodal. These results are used to calculate static structure factors which are related to the increasing concentration fluctuations of the mixture. By extrapolation to the low wave vector limit, we are able to determine the phase diagram of the coarse-grained mixture which is consistent with mean-field theory predictions. The consistency of all representations supports the theoretical foundation of our development.

While other methods exist to obtain equilibrium properties of blends, an analytical potential is desirable for many of these approaches. For example, the Gaussian equivalent representation (GER) has been implemented using a purely repulsive Gaussian potential for a system of interacting particles to obtain a field-theoretic representation of the partition function and used to compute structural and thermodynamic quantities of

![](./images/811798120944893953_15.jpg)

Figure 11. Top left: AA component of the correlation function for the miscible blend, hhPP/PIB ($\phi = 0.5$) at $T = 2000$ K (circles) and $T = 200$ K (triangles). Theoretical predictions are indicated as solid lines. BB component (top right) and AB component (bottom left) of the same mixture. Bottom right: concentration fluctuation structure factor for hhPP/PIB obtained from mesoscale simulation (symbols) and from theory (solid line) at various temperatures.

interest. $^{58,59}$ Possible future applications of the analytical potential derived in this publication could include using it in low-cost approximation methods, such as the zeroth-order GER model formalism.

Although the current publication is focused on determining the equilibrium structure of blends under various conditions, the proposed procedure of obtaining the effective potential and performing mesoscale simulations should be useful in determining the nonequilibrium and dynamic behavior of these systems as well, where time must be treated explicitly. Future work in this direction should include examining the phase transition that occurs when the thermodynamic conditions of the system are suddenly changed. In the context of a multiscale modeling procedure, mesoscale simulations, such as those performed here, may be coupled to a more detailed description in order to combine local and global information over multiple length and time scales.

Acknowledgment. This research was supported by the National Science Foundation through grant DMR-0804145. Computational resources were provided by LONI through the TeraGrid project supported by NSF.

### References and Notes

(1) Strobl, G. *The Physics of Polymers*; Springer: New York, 2006.
(2) Balsara, N. In *Physical Properties of Polymers Handbook*; Mark, J. E., Ed.; AIP Press: Woodbury, NY, 1996.
(3) Olabisi, O.; Robeson, L. M.; Shaw, M. T. *Polymer-Polymer Miscibility*; Academic Press: New York, 1979.
(4) Schweizer, K. S.; Curro, J. G. *Adv. Polym. Sci.* **1994**, 116, 321.
(5) Schweizer, K. S.; Curro, J. G. *Adv. Chem. Phys.* **1997**, 98, 1.
(6) Dudowicz, J.; Freed, K. F.; Douglas, J. F. *Phys. Rev. Lett.* **2002**, 88, 095503.
(7) Lodge, T. P.; McLeish, T. C. B. *Macromolecules* **2000**, 33, 5278.
(8) Zeroni, I.; Ozair, S.; Lodge, T. P. *Macromolecules* **2008**, 41, 5033.
(9) Lipson, J. E. G. *Macromol. Theory Simul.* **1998**, 7, 263.
(10) Müller, M. *Macromol. Theory Simul.* **1999**, 8, 343 and citations therein.
(11) Binder, K. *Comput. Phys. Commun.* **2002**, 147, 22.
(12) Clancy, T. C.; Putz, M.; Weinhold, J. D.; Curro, J. G.; Mattice, W. L. *Macromolecules* **2000**, 33, 9452.
(13) Heine, D.; Wu, D. T.; Curro, J. G.; Grest, G. S. *J. Chem. Phys.* **2003**, 118, 914.
(14) Jaramillo, E.; Wu, D. T.; Grest, G. S.; Curro, J. G. *J. Chem. Phys.* **2004**, 120, 8883.
(15) Sewell, T. D.; Rasmussen, K. Ø.; Bedrov, D.; Smith, G. D.; Thompson, R. B. *J. Chem.* **2007**, 127, 144901.
(16) Bedrov, D.; Liu, W.; Colby, R. H. *Philos. Mag.* **2008**, 88, 3979.
(17) Frenkel, D.; Smit, B. *Understanding Molecular Simulation: From Algorithms to Applications*; Academic Press: New York, 1996.
(18) Yelash, L.; Virnau, P.; Paul, W.; Binder, K. *Phys. Rev. E* **2008**, 78, 031801.
(19) Sun, Q.; Faller, R. *J. Chem. Phys.* **2007**, 126, 144908.
(20) Camargo, M.; Likos, C. N. *J. Chem. Phys.* **2009**, 130, 204904.
(21) Baeurle, S. A. *J. Math. Chem.* **2009**, 46, 363.
(22) McCarty, J.; Lyubimov, I. Y.; Guenza, M. G. *J. Phys. Chem. B* **2009**, 113, 11876.
(23) McCarty, J.; Lyubimov, I. Y.; Guenza, M. G., in preparation.
(24) Flory, P. J.; Krigbaum, W. R. *J. Chem. Phys.* **1950**, 18, 1086.
(25) Louis, A. A.; Bolhuis, P. G.; Hansen, J.-P.; Meijer, E. J. *Phys. Rev. Lett.* **2000**, 85, 2522.
(26) Krakoviack, V.; Hansen, J.-P.; Louis, A. A. *Phys. Rev. E* **2003**, 67, 041801.
(27) Malescio, G. *J. Phys.: Condens. Matter* **2007**, 19, 073101.
(28) Baeurle, S. A.; Kroener, J. *J. Math. Chem.* **2004**, 36, 409.
(29) Mullinax, J. W.; Noid, W. G. *J. Chem. Phys.* **2009**, 131, 104110.
(30) Dautenhahn, J.; Hall, C. *Macromolecules* **1994**, 27, 5399.

(31) Murat, M.; Kremer, K. *J. Chem. Phys.* **1998**, *108*, 4340.

(32) Bolhuis, P. G.; Louis, A. A.; Hansen, J.-P.; Meijer, E. J. *J. Chem. Phys.* **2001**, *114*, 4296.

(33) Yatsenko, G.; Sambriski, E. J.; Nemirovskaya, M. A.; Guenza, M. *Phys. Rev. Lett.* **2004**, *93*, 257803.

(34) Yatsenko, G.; Sambriski, E. J.; Guenza, M. G. *J. Chem. Phys.* **2005**, *122*, 054907.

(35) Kirkwood, J. G.; Buff, F. P. *J. Chem. Phys.* **1951**, *19*, 774.

(36) Bhatia, A. B.; Thornton, D. E. *Phys. Rev. B* **1970**, *2*, 3004.

(37) Groot, R. D. *Lect. Notes Phys.* **2004**, *640*, 5.

(38) Hansen, J.-P.; McDonald, I. R. *Theory of Simple Liquids*; Academic Press: London, 1991.

(39) Guenza, M. *Macromolecules* **2002**, *35*, 2714.

(40) Guenza, M. *Phys. Rev. Lett.* **2002**, *88*, 025901.

(41) Krakoviack, V.; Hansen, J.-P.; Louis, A. A. *Europhys. Lett.* **2002**, *58*, 53.

(42) Sambriski, E. J.; Yatsenko, G.; Nemirovskaya, M. A.; Guenza, M. G. *J. Chem. Phys.* **2006**, *125*, 234902.

(43) Doi, M.; Edwards, S. F. *The Theory of Polymer Dynamics*; Oxford University Press: Oxford, 1968.

(44) Tang, H.; Schweizer, K. S. *J. Chem. Phys.* **1996**, *105*, 779.

(45) McQuarrie, D. A. *Statistical Mechanics*; University Science Books: Sausalito, CA, 2000.

(46) Hoye, J. S.; Lomba, E.; Stell, G. *Mol. Phys.* **1993**, *79*, 523.

(47) Zerah, G.; Hansen, J.-P. *J. Chem. Phys.* **1986**, *84*, 2336.

(48) Jeon, H. S.; Lee, J. H.; Balsara, N. P. *Macromolecules* **1998**, *31*, 3328.

(49) Lee, J. H.; Balsara, N. P.; Chakraborty, A. K.; Krishnamoorti, R.; Hammouda, B. *Macromolecules* **2002**, *35*, 7748.

(50) Krishnamoorti, R.; Graessley, W. W.; Fetters, L. J.; Garner, R. T.; Lohse, D. J. *Macromolecules* **1995**, *28*, 1252.

(51) Matsumoto, M.; Nishimura, T. *ACM Trans. Model. Comput. Simul.* **1990**, *8*, 3.

(52) Catlett, C.; et al.et al. TeraGrid: Analysis of Organization, System Architecture, and Middleware Enabling New Types of Applications. In *HPC and Grids in Action*; Advances in Parallel Computing Series; Grandinetti, L., Ed.; IOS Press: Amsterdam, 2007.

(53) Allen, M. P.; Tildesley, D. J. *Computer Simulation of Liquids*; Oxford Science Publications: Oxford, UK, 1992.

(54) Sariban, A.; Binder, K. *J. Chem. Phys.* **1987**, *86*, 5859. Sariban, A.; Binder, K. *Macromolecules* **1988**, *21*, 711. Sariban, A.; Binder, K. *Colloid Polym. Sci.* **1989**, *267*, 469.

(55) Wittmer, J. P.; Beckrich, P.; Johner, A.; Semenov, A. N.; Obukhov, S. P.; Meyer, H.; Baschnagel, J. *Europhys. Lett.* **2007**, *77*, 56003.

(56) Cavallo, A.; Müller, M.; Wittmer, J. P.; Johner, A.; Binder, K. *J. Phys.: Condens. Matter* **2005**, *17*, S1697.

(57) Beckrich, P.; Johner, A.; Semenov, A. N.; Obukhov, S. P.; Benoit, H.; Wittmer, J. P. *Macromolecules* **2007**, *40*, 3805.

(58) Baeurle, S. A.; Efimov, G. V.; Nogovitsin, E. A. *Europhys. Lett.* **2006**, *75*, 378.

(59) Baeurle, S. A.; Efimov, G. V.; Nogovitsim, E. A. *J. Chem. Phys.* **2006**, *124*, 224110.
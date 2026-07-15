PHYSICAL REVIEW MATERIALS 4, 113802 (2020)

# Short-range order in face-centered cubic VCoNi alloys

Tatiana Kostiuchenko, $^{1}$ Andrei V. Ruban, $^{2,3}$ Jörg Neugebauer, $^{4}$ Alexander Shapeev, $^{1}$ and Fritz Körmann $^{4,5, *}$

$^{1}$ Skolkovo Institute of Science and Technology, Skolkovo Innovation Center, Nobel St. 3, Moscow 143026, Russia
$^{2}$ Department of Materials Science and Engineering, KTH Royal Institute of Technology, SE-100 44 Stockholm, Sweden
$^{3}$ Materials Center Leoben, 8700 Leoben, Austria
$^{4}$ Computational Materials Design, Max-Planck-Institut für Eisenforschung GmbH, D-40237 Düsseldorf, Germany
$^{5}$ Materials Science and Engineering, Delft University of Technology, 2628 CD, Delft, The Netherlands

![](./images/812547258233913344_1.jpg)
(Received 18 August 2020; accepted 6 October 2020; published 4 November 2020)

Concentrated solid solutions including the class of high entropy alloys (HEAs) have attracted enormous attention recently. Among these alloys a recently developed face-centered cubic (fcc) equiatomic VCoNi alloy revealed extraordinary high yield strength, exceeding previous high-strength fcc CrCoNi and FeCoNiCrMn alloys. Significant lattice distortions had been reported in the VCoNi solid solution. There is, however, a lack of knowledge about potential short-range order (SRO) and its implications for most of these alloys. We performed first-principles calculations and Monte Carlo simulations to compute the degree of SRO for fcc VCoNi, namely, by utilizing the coherent-potential approximation in combination with the generalized perturbation method as well as the supercell method in combination with recently developed machine-learned potentials. We analyze the chemical SRO parameters as well as the impact on other properties such as relaxation energies and lattice distortions.

DOI: 10.1103/PhysRevMaterials.4.113802

## I. INTRODUCTION

Multicomponent alloys, also known as high entropy alloys (HEAs) or chemically complex alloys (CCAs), have attracted enormous attention in the last decade, from theory and experiment, due to their remarkable materials properties and overwhelming compositional phase space for alloy design [1-3]. A recent example is an equiatomic face-centered cubic (fcc) single-phase VCoNi alloy revealing remarkable strength [4].

One of the key components in the design and exploration of multicomponent alloys is the knowledge about its phase stability. In fact, many such alloys have been demonstrated to decompose at elevated temperatures, e.g., the equiatomic fcc FeCoNiCrMn (also known as Cantor alloy) [5]. An important issue to address is therefore whether the solid solutions involve local chemical ordering or short-range order (SRO), which could affect, e.g., defect properties and hence their mechanical properties. This has, for example, been demonstrated in recent simulations of computed stacking-fault energies in fcc CrCoNi [6,7]. There are also some experimental results suggesting the presence of SRO in selected fcc HEAs such as, e.g., fcc CrCoNi [7,8], fcc FeCoNiCr [9,10], in Ni-Co-Fe-Cr alloys [11], and fcc CrFeCoNiPd [12]. In Ref. [7], a correlation between the mechanical behavior and SRO has been established for fcc CrCoNi.

For VCoNi, which is in the focus of the present work, a single-phase solid solution has been experimentally confirmed at $900\,^\circ\text{C}$ [4]. For lower temperatures, recent experiments revealed formation of a $({\text{Co,Ni)3V}}$ $\kappa$ phase at around $850\,^\circ\text{C}$ [13] as well as a secondary, V-rich $\sigma$ phase at temperatures below $800\,^\circ\text{C}$. The $\kappa$ phase features a close-packed ordered nine-layered hexagonal structure with an abcbcacab packing sequence [13-16] with characteristic layered-wise enrichment and depletion of V. This suggests that V could play a key role for the SRO in the solid solution. As mentioned above, the SRO could impact different properties such as, e.g., the degree of lattice distortions, which was one of the key computational descriptors to develop this high-strength alloy and for which V played a dominant role [4]. It is therefore crucial to accurately determine the degree of SRO and its implication for these properties.

As mentioned above, for most of the alloys only limited experimental information is available for quantifying the degree of SRO. In addition to experiments, in particular, *ab initio*-based density-functional theory (DFT) calculations have therefore been utilized to explore multicomponent alloys [2]. A number of such techniques are available to address phase stability and, in particular, SRO; among them the coherent-potential approximation (CPA) [17,18] based methods such as the generalized perturbation method (GPM) [19-21] in combination with Monte Carlo (MC) simulations or the concentration wave method [22,23]. These methods have been extensively employed in the past few years for multicomponent alloys [10,23-27] also due to their

---

*f.h.w.kormann@tudelft.nl

Published by the American Physical Society under the terms of the Creative Commons Attribution 4.0 International license. Further distribution of this work must maintain attribution to the author(s) and the published article's title, journal citation, and DOI. Open access publication funded by the Max Planck Society.

2475-9953/2020/4(11)/113802(10)
113802-1
Published by the American Physical Society

computational efficiency. A limitation of such mean-field approaches is, however, the great challenge to include local relaxation effects, which can be important for phase stability considerations [28,29]. One alternative is explicit DFT-based Monte Carlo simulations employing supercells [6,30–32]. These calculations are, however, restricted to rather small simulation boxes (typically a few hundred) and also computationally extremely demanding. Therefore, DFT-derived energies are often mapped onto effective models such as the cluster-expansion technique [33], which is, however, computationally inefficient when treating multicomponent alloys [34]. An alternative to these approaches is provided by recently developed machine-learned potentials, which allow one to extremely efficiently parametrize the energy landscape, in particular for multicomponent alloys [29,34].

In the present work we employ two state-of-the art approaches. One is the recently developed low-rank potential (LRP), a machine-learned potential based on supercell calculations allowing us to fully account for lattice-relaxation effects. In addition, to estimate the importance of magnetic excitations, we perform Green's function multiple-scattering theory calculations to extract chemical effective interactions and study their dependence on the high-temperature magnetic state, which accounts for longitudinal spin fluctuations (LSF). The order-disorder transition is computed as well as the SRO parameters above the critical temperature. Potential implications, e.g., on lattice distortions and solid-solution strengthening contributions, are discussed.

## II. COMPUTATIONAL DETAILS

### A. Density-functional theory calculations for supercell approach

As outlined in the introduction above, the first model we employ is the low-rank interatomic potential (LRP) [34] (see also below), which is used as an interaction model in canonical Monte Carlo (MC) simulations in order to investigate short-range order and order-disorder phase transitions in the equiatomic VCoNi system. The LRP model is based on spin-polarized DFT calculations. To compute the reference energies of atomic configurations for the LRP training, VASP 5.4.1. [35–38] was used in combination with the projector augmented wave (PAW) method [39] and utilizing the Perdew-Burke-Ernzerhof generalized gradient approximation (PBE-GGA) [40]. Since we are interested in quantifying the degree of SRO at high temperatures, we performed the corresponding calculations at a lattice constant corresponding to high temperatures. The lattice constant has been derived from a Debye-Grüneisen model [41] at 1175 K, which is around the experimentally observed phase transition [13]. For the Debye-Grüneisen model, we computed the total energy of the alloy, $E(V)$, bulk modulus, and its derivative utilizing a $3 \times 3 \times 3$ (108 atom) special quasirandom (SQS) [42] structure. The predicted room-temperature lattice constant of $3.599$ Å is very close to the experimental value of $3.601$ Å [4]. The obtained value at 1175 K, $3.643$ Å, has been employed to compute the structures entering the training set, see below.

For the training set of the potential, different supercell sizes are chosen, ranging from $2 \times 2 \times 2$ (32 atoms) to $3 \times 3 \times 3$ (108 atoms). The value of the plane-wave cutoff energy is chosen to be 320 eV, which is 1.2 times larger than the recommended cutoff energy of the PAW pseudopotentials utilized. A $k$-point mesh is generated by the Monkhorst-Pack [43] scheme and is $6 \times 6 \times 6$ for the system with 32 atoms, $4 \times 6 \times 6$ for the system with 48 atoms, and $4 \times 4 \times 4$ for systems with 108 atoms. Ionic relaxations of atomic positions are included in the calculations to account for the impact of lattice relaxations, which is presumably large in this alloy [4]. The energy convergence criteria for the ionic relaxations are set to achieve an error of $10^{-4}$ eV. Electronic excitations are included by utilizing the Fermi distribution in the DFT calculations with a smearing parameter of 0.1 eV, which corresponds to a temperature close to the experimentally observed transition temperature.

### B. The low-rank potential method

The atomistic structure for the LRP [34] model is represented as site occupancies in the ideal crystalline lattice. Each site is occupied by one of the atomic species (V, Co, Ni in this case). The sequence of atomic species among the closest neighbors of each site represents the environment of this site. The environment of each site has a contribution to the energy of the atomic configuration given by the formula
$$V(\xi)=V\left(\sigma_{1}, \ldots, \sigma_{n}\right)=V\left(\sigma\left(\xi+r_{1}\right), \ldots, \sigma\left(\xi+r_{n}\right)\right), \quad(1)$$
where $V$ is the LRP model in the tensor form, as described below, $\xi$ is the position of a central atom, $\sigma(\xi+r_{i})$ is the species of the $i$th site and $r_{i}$ is the vector connecting the central site with the $i$th neighbor, and $n$ is the number of closest neighbors in the environment, including the central atom ($n=13$ in the fcc case). The local lattice distortions are allowed as long as the topology of the supercell stays the same. The full energy of an atomic configuration can be described as a sum of individual contributions of the environments:
$$E(\sigma)=\sum_{\xi \in \Omega} V(\xi),\qquad(2)$$
where $\Omega$ is the lattice sites periodically repeated in space. The tensor $V$ contains energy contributions of all possible atomic environments, namely, $m^{n}$ environments, where $m$ is the number of species in the system. Thus, for a fcc system with $m=3$ species ({V, Co, Ni} in this case) the tensor $V$ consists of about 1.6 million coefficients which is completely unfeasible to obtain from quantum-mechanical data. To remedy this, the LRP potential postulates a certain low-rank structure of $V$, or, to be precise, that there are some good approximants of $V$ among the low-rank 13-dimensional tensors in the sense of the tensor-train decomposition [44]. This decomposition scheme will be explained in the following. Let us consider for the moment that $V$ is a large $N \times N$ matrix (i.e., a two-dimensional tensor). We identify the matrix $V$ with a discrete function $V(\sigma_{1}, \sigma_{2})$. Assuming that the matrix $V$ has a low rank $r$ means that the column vectors of $V$ can be expressed as a linear combination of $r$ vectors $w_{1},..., w_{r}$:
$$V\left(\sigma_{1}, \sigma_{2}\right)=\sum_{i=1}^{r} u_{i}\left(\sigma_{1}\right) w_{i}\left(\sigma_{2}\right).\qquad(3)$$

Here we used the notation $u_{i}(\sigma_{1})$ for the coefficients of the linear expansion to make the notation symmetric. The

expansion (3) is reminiscent of the method of separation of variables and could be motivated as follows: Often when the matrix $V$ describes some regular (smooth) function, only a few singular values $s_i$ are far from zero,

$$
V(\sigma_1, \sigma_2) \approx \sum_{i=1}^r s_i u_i(\sigma_1) w_i(\sigma_2),
$$

where the right-hand side is precisely a singular value decomposition. For symmetric positive-definite matrices $V$, $s_i$ would be the nonzero eigenvalues with $u_i = w_i$ being the corresponding eigenvectors. Adsorbing $s_i$ into $u_i$ and $w_i$ yields (3). One could generalize (3) to more than two dimensions by postulating $V(\sigma_1, \dots, \sigma_n) = \sum_{i=1}^r a_1(\sigma_1) \cdots a_n(\sigma_n)$. This formalism leads, however, to computational issues when used in optimization algorithms [45]. Instead, we utilize the density-matrix renormalization-group analogy, and hence cast (3) in the vector product form:

$$
V(\sigma_1, \sigma_2) = \boldsymbol{a}_1(\sigma_1) \cdot \boldsymbol{a}_2(\sigma_2),
$$

with $\boldsymbol{a}_1$ and $\boldsymbol{a}_2$ being some $r$-dimensional vectors. We then generalize:

$$
V(\sigma_1, \dots, \sigma_n) = \prod_i A_i(\sigma_i), \tag{4}
$$

where $A_i$ are matrices with rank $r$ or less ($A_1, A_n$ are of size $1 \times r$ and $r \times 1$, correspondingly, $A_2, \dots, A_{n-1}$ are of size $r \times r$), $r$ is this rank of the decomposition. The elements of the matrices $A_i$ are the parameters of the LRP. Thus, the tensortrain decomposition reduces the number of these parameters from $m^n$ to $nmr^2$. In the context of our three-component alloy, $\sigma_i$ can take either of the three values (V, Co, or Ni). We found that $r = 5$ is an optimal rank and thus about 900 parameters were fit instead of 1.6 million.

The parameters are found as a result of solving the minimization problem with the following functional:

$$
\frac{1}{K} \sum_{k=1}^K \left| E(\sigma^{(k)}) - E^{\text{qm}}(\sigma^{(k)}) \right|^2, \tag{5}
$$

where $\sigma^{(k)}$ are the atomic configurations, the total number of which in the training set is $K$, and $E(\sigma^{(k)})$ and $E^{\text{qm}}(\sigma^{(k)})$ are the energies of $\sigma^{(k)}$ predicted by LRP and calculated by DFT, correspondingly. The minimization was done with an alternating least squares method that reduces to simply optimizing one matrix $A_i$ at a time (this is a linear problem), and simulated annealing which consists of adding random Gaussian noise to every element of $A_i$ with a magnitude that gradually reduces from one iteration to the next.

The dependence of $V$ on its parameters is not linear. Thus, different local energy minima exist in the parameter space. Therefore, depending on the initial parameters, the minimization algorithm finds different local minima. The latter means that each LRP gives independent energy predictions, and with a trained ensemble of several LRPs, the uncertainty level of the LRP model can be estimated. In this work, an ensemble of 10 LRPs was used. The 10 LRPs differ by the random initialization of the matrices $A_i$ in Eq. (4). The coefficients of each matrix were drawn from a normal distribution with zero mean. The value of the variance does not affect the results because, at each step of the optimization, the matrices $A_i$ are rescaled to the data [34]. We find that, in practice, all 10 LRPs have comparable fitting errors.

![](./images/812547258233913344_2.jpg)

FIG. 1. Workflow for the LRP training and the new structure sampling. The sketch is similar to the one implemented in Ref. [29].

The initial training set consisted of random disordered configurations with sizes $3 \times 3 \times 3$ (108 atoms), $3 \times 2 \times 2$ (48 atoms), $2 \times 2 \times 2$ (32 atoms) confined to equimolar (for 108- and 48-atom cells) or as close to equimolar as possible (for the 32-atom cell). The number of configurations with 108, 48, and 32 atoms was 86, 70, and 70, correspondingly, in the training set, and 10, 10, and 9 configurations in the validation set. We note that fcc point symmetries were applied, so that each configuration enters the training set together with the other 47 equivalent configurations, thus effectively generating about 10 000 data points to determine the 900 parameters of the LRP.

To improve the accuracy of the LRP, the workflow from Ref. [29] (see Fig. 1) for selecting new configurations is used. MC calculations are conducted for systems with 108 atoms. The values of the enthalpy and heat capacity for the LRP ensemble are compared for different temperatures, and configurations that correspond to the temperature range with the highest deviations are sampled.

The sampled configurations are added to the training and validation set and the new ensemble of LRP is trained. Each training starts with a new random distribution of initial matrices $A_i$. This procedure continues until the training error stops changing significantly. In this work, 40 new configurations were sampled and added to the data sets.

The rank is an adjustable parameter and, to choose it, we considered values from three to six. Starting from $r = 5$, the accuracy of prediction achieves 2 meV/atom.

LRP is a representative of the machine-learned class of interatomic potentials and can be compared with the cluster expansion method (CE). In contrast with the CE [46], LRP has a form of many-body interaction without separating it into two-body, three-body, etc. Similarly to CE, if atomic displacements do not change the topology of the lattice structure, then the local lattice distortions can be taken into account.

### C. Monte Carlo method

The LRPs are used in a canonical Mote Carlo method [47]. We mainly focus on the temperature range of 1100–1500 K,

as the experimentally observed order-disorder phase transition is at approximately 1175 K [4].

The simulations are carried out for systems with 6912 atoms ($12 \times 12 \times 12$ in lattice units, based on a four-atom primitive fcc cell). The number of MC steps is adaptive for different temperature ranges: for temperatures higher than $2000$ K—$2 \times 10^8$ steps, for the interval of 1250–2000 K—$2 \times 10^9$ steps, for temperatures lower than 1250 K, the number of steps is $2 \times 10^{10}$. For the smaller structures with 32 atoms ($2 \times 2 \times 2$ in lattice units), the number of steps is two orders of magnitude smaller. To achieve an unbiased averaging, the so-called *burn-in* approach [48] was implemented, i.e., we neglected the first half of MC steps for each temperature value. This technique is necessary at the range of temperatures that include phase transitions but was used permanently in our calculations to improve the robustness of the algorithm.

### D. Multiple-scattering theory calculations
As a second approach, in order to obtain a qualitative picture of the impact of low- and high-temperature magnetism as well as the effective interactions in V-Co-Ni alloys, the Green's function multiple-scattering theory was used as implemented in the exact muffin-tin orbital method (EMTO) [49–51]. The electronic structure of the random alloys was obtained within the coherent-potential approximation (CPA) as well as by using the locally self-consistent Green's function (LSGF) technique [52,53] within the EMTO method, ELSGF [54].

All the EMTO-CPA calculations were done by utilizing the Lyngby version of the Green's function EMTO code, which allows us to calculate effective interactions [55] employing the screened generalized perturbation method (SGPM) [19,56,57], to include the impact of longitudinal spin fluctuations (LSFs). Moreover, the screened Coulomb interactions are treated properly in the single-site DFT-CPA approximation [20,21].

The self-consistent electronic structure calculations were performed in the local density approximation (LDA) using the Perdew and Wang functional [58] while the total energies were calculated by the full charge-density technique [51] employing PBE-GGA [40]. The Brillouin-zone integration was done by using a $30 \times 30 \times 30$ Monkhorst-Pack grid [43] or finer. All calculations have been done with $l_{\text{max}} = 3$ for partial waves, and the electronic core states were recalculated at every iteration during the self-consistent calculations for the valence electrons.

The ELSGF method was used to calculate the screened Coulomb interactions used in the DFT-CPA part of the EMTO-CPA calculations. In this case, the one-electron potential of the alloy components and the total energy have additional contributions, $V_{\text{scr}}^i$, and $E_{\text{scr}}$, respectively, due to the screening charge around atomic spheres, which is not accounted for in the single-site approximation [20,21]:

$$
V_{\text{scr}}^i = -e^2 \alpha_i^0 \frac{\bar{q}_i}{S_{\text{WS}}},
$$

$$
E_{\text{scr}} = \sum_i c_i E_{\text{scr}}^i, \tag{6}
$$

$$
E_{\text{scr}}^i = -e^2 \frac{1}{2} \alpha_i^0 \beta_{\text{scr}} \frac{\bar{q}_i^2}{S_{\text{WS}}}.
$$

Here, $\bar{q}_i$ and $\alpha_i^0$ are the net charge of the atomic sphere of the $i$th component in the single-site CPA calculations and its on-site screening constant, respectively; $S_{\text{WS}}$ is the Wigner-Seitz radius; $E_{\text{scr}}^i$ is the contribution of the screened Coulomb interactions to the electrostatic energy of the $i$th alloy component; $\beta_{\text{scr}}$ is the average on-site screening constant, which accounts for the electrostatic multipole moment energy contribution due to the inhomogeneous local environment of different sites in a random alloy.

The screening constants for the Co-Ni-V alloys were determined from ELSGF 864-atom $6 \times 6 \times 6$ supercell calculations. The on-site screening constants $\alpha_i^0$ were determined from the conditional average of the net charges $q_i$ and the Madelung potentials $V_i^{\text{Mad}}$ of the $i$th component in the supercell, $\langle q_i \rangle$ and $\langle V_i^{\text{Mad}} \rangle$, respectively as

$$
\alpha_i^0 = \frac{S_{\text{WS}} \langle V_i^{\text{Mad}} \rangle}{e^2 \langle q_i \rangle}. \tag{7}
$$

The intersite screening constants $\alpha_p^{ij}$ are needed in the calculations of the electrostatic contribution $V_p^{ij-\text{scr}}$ to the SGPM potential at the $p$th coordination shell for the $i$-$j$ pair of alloy components,

$$
V_p^{ij-\text{scr}} = e^2 \alpha_p^{ij} \frac{\bar{q}_{ij}^2}{S_{\text{WS}}}. \tag{8}
$$

Here, $\bar{q}_{ij} = \bar{q}_i - \bar{q}_j$ were obtained in the supercell ELSGF calculations for random alloys from the screening charge by exchanging the corresponding alloy components ($i$ and $j$ in some specific sites have random local environment on average) as described in Refs. [20,21].

## III. RESULTS AND DISCUSSION
### A. Phase stability and short-range order
A goal of the present work is to investigate the degree of short-range order in VCoNi alloy as well as the interplay with lattice distortions and relaxation effects, which is closely related to the exceptional strengthening of the VCoNi alloy [4].

As sketched in Fig. 1, we first included 226 configurations to the training set. We trained an ensemble of 10 LRPs, which were used in the MC simulations for systems with 108 atoms. We analyzed the dependencies of enthalpy and heat capacity on temperature obtained with these 10 LRPs. Based on this initial set of potentials, we sampled a number of new configurations at a range of temperatures close to the precomputed order-disorder phase transition, i.e., near temperatures where significant fluctuations among the initial potentials was observed. As a result, 40 new configurations were selected and included in the fitting procedure, namely, 10 configurations for each of the following temperatures: 760, 860, 1100, and 1140 K. These configurations were recalculated with VASP (see above) and added to the training and validation sets, thus improving the prediction error of the finally utilized LRPs down to 2 meV/atom.

We also evaluated the impact of including a number of DFT-computed $4 \times 4 \times 4$ supercell results to the training set. The accuracy of the energy prediction is still about 2 meV/atom, resulting in qualitatively similar predictions of, e.g., specific-heat capacities, as will be shown below. We

![](./images/812547258233913344_3.jpg)

FIG. 2. Specific-heat capacity $C_V(T)$ for fcc VCoNi from MC simulations for a $12 \times 12 \times 12$ simulation box. The dashed and solid black lines represent the average heat capacity calculated with an ensemble of 10 LRPs including up to $3 \times 3 \times 3$ supercells in the training set and including up to $4 \times 4 \times 4$ supercells in the training set, respectively. The light and dark gray areas show the uncertainty level of the LRPs ensembles.

thus concluded that the inclusion of explicit DFT supercell calculations beyond the mainly used $3 \times 3 \times 3$ cells into the LRP training set would not qualitatively alter our main results and conclusions.

To investigate the temperature-dependent evolution of SRO and phase stability of the alloy, LRP-based MC simulations were carried out for larger $12 \times 12 \times 12$ supercells (6912 atoms). In Fig. 2 the dependence of specific-heat capacity on temperature, $C_V(T)$, is presented. We first observe a phase transition with a characteristic peak in $C_V(T)$ around 1400–1500 K. There is a slight dependence of the transition temperature depending on the largest DFT-computed supercells in the training set, which is manifested in deviations mainly around the peak whereas the lower and higher temperatures appear less size-dependent. The overall transition temperature is also somewhat higher than the experimental one, which is between 1123 and 1173 K [4,13]. The discrepancy may be related to missing thermal fluctuations such as, e.g., vibrations which could in principle alter the predictions [59]. We also note that the present approach cannot account for the experimentally observed hexagonal $\kappa$ phase. On the fcc lattice we observe a phase transition to a partially ordered structure, where V atoms almost fully occupy one of the four primitive cubic sublattices of the fcc structure, as shown in the inset of Fig. 2. The computed atomic concentration of V for each of the four sublattices are shown in Fig. 3. This clearly shows that the observed phase transition is caused by a strong site preference of V on one of the four sublattices, while the remaining V is equally distributed on the other sublattices, which corresponds to the M3V-L1$_2$ ordering.

The L1$_2$ structure is formed in Co$_3$V alloys as a metastable phase if the alloys are quenched and constrained to the fcc lattice (see, e.g., Ref. [60] and references therein). Recently, a similar L1$_2$ ordering has been also reported for a four-component fcc FeCoNiV alloy [61]. It may therefore be that the L1$_2$ ordering observed in the present work for VCoNi can exist as a metastable phase. The experimentally observed $\sigma$ phase [4,13,62] at temperatures below 800 K cannot be covered by our simulations because we are operating on the fcc lattice. We therefore focus in the following on the SRO effects at high temperatures.

![](./images/812547258233913344_4.jpg)

FIG. 3. The dependence of site occupancy on temperature in the equimolar $12 \times 12 \times 12$ cell for vanadium. The four different lines correspond to the four primitive cubic sublattices of the fcc structure.

To quantify the degree of SRO, the Warren-Cowley SRO parameters [63] were calculated:
$$
\alpha_{m}^{i j}=1-\frac{p_{m}^{i j}}{c_{i} c_{j}},\qquad(9)
$$
where $\alpha_{m}^{i j}$ is the Warren-Cowley SRO parameter for the atomic types $i$ and $j$ at the $m$th coordination shell; $p_{m}^{i j}$ is the probability of finding atom type $j$ at the $m$th coordination shell $i$ of atom $m$, and $c_i$, $c_j$ are the concentrations of elements $i$ and $j$ in the alloy. According to this definition, positive (negative) values of the SRO parameter at the $m$th coordination shell mean that atoms $i$ and $j$ avoid (attract) each other at the corresponding coordination shell.

The computed SRO parameters for the first and second coordination shells are shown in Figs. 4(a) and 4(b). Obviously, there is strong ordering between pairs Co-V and Ni-V at the first coordination shell, while these pairs exhibit strong repulsion at the second coordination shell, which corresponds to the L1$_2$ type of ordering (in the completely ordered A$_3$ B-L1$_2$ phase, the Warren-Cowley SRO parameters at the first two coordination shells are $-1/3$ and 1). Thus, the formation of atomic SRO in VCoNi alloys is mainly driven by the strong interaction of V with Co and Ni.

### B. Interplay and impact of short-range order and lattice distortions

Since the fcc VCoNi solid solution is prone to significant local lattice distortions [4], it is important to evaluate how relevant the inclusion of the corresponding relaxation energies are for an accurate modeling. An advantage of the LRP approach employed here is that local distortions can effectively be “switched off,” allowing us to explore their impact and relevance, e.g., for the prediction of SRO parameters as well as phase stability.

Similarly to our previous work [29], we evaluate the impact of local distortions and the corresponding relaxation energies

![](./images/812547258233913344_5.jpg)

FIG. 4. Temperature-dependent Warren-Cowley short-range order parameters derived from an ensemble of 10 LRPs.

by training a new ensemble of LRP potentials on a set of static DFT calculations followed by subsequent MC runs, as discussed above. Thus-obtained specific-heat capacity is shown in Fig. 5 and shows that the M3V-type of ordering sets in only above temperatures of 2000 K. This is about 30% larger compared with the case when relaxation effects are included and highlights the importance of taking relaxations into account for modeling such alloys.

To further elucidate the impact of relaxation energies, we performed an additional MC simulation from the previous LRPs, including relaxations for a smaller $4 \times 4 \times 4$ supercell (containing 256 atoms) and selected ten snapshots at three representative temperatures: at 1000 K for a M3V type of ordered structure, at 1540 K for a strongly SRO-containing solid solution, and at 4000 K to represent a random solid solution. In total, 30 new structures were recalculated with DFT to extract the relaxation energies, which are depicted in Fig. 6 (light blue bars). The error bars indicate the standard deviation for the mean value as obtained from averaging over the ten individual calculations for each case. There is a clear trend of increasing relaxation energies with increasing disorder. The largest relaxation energies of roughly 30 meV/atom are found for the solid solution and are almost twice as large as found for the M3V type of ordered structures. This is consistent with our findings that the computed transition temperature decreases drastically if relaxation effects are included in the simulations.

![](./images/812547258233913344_6.jpg)

FIG. 5. Temperature dependence of specific-heat capacity based on MC simulations for equimolar fcc VCoNi $3 \times 3 \times 3$, $4 \times 4 \times 4$, and $6 \times 6 \times 6$ supercells. The LRPs utilized are trained on static DFT calculations without taking local distortions into account. The observed phase transition is observed around 2000 K, which is roughly 30% larger than if relaxation energies were properly taken into account.

Based on the examples considered, we also evaluated the impact of the electronic free-energy contributions to the phase stability. As mentioned above, all our calculations include electronic free energies based on a Fermi smearing parameter of 0.1 eV, which corresponds to a temperature of 1160 K, close to the experimentally observed phase transition. In Fig. 6, the electronic free-energy contributions are shown in light green for the different scenarios. Although the electronic free energies are overall of similar magnitude as compared with

![](./images/812547258233913344_7.jpg)

FIG. 6. Electronic free-energy contributions at 1160 K (corresponding to a Fermi smearing of 0.1 eV) in light green, relaxation energies (light blue), and mean-squared atomic displacements (light red) obtained from DFT calculations of 256-atom ($4 \times 4 \times 4$) supercells selected from MC runs for three different scenarios: MC simulations at 1000 K (M3V type of ordering), at 1540 K (SRO-containing solid solution), and at 4000 K (random solid solution). Relaxation energies and lattice distortions increase with increasing disorder. The standard deviation obtained by averaging over 10 different supercells for each case is depicted as error bars.

the relaxation energies, the relative changes are much smaller, implying that SRO does not significantly alter the electronic density of states, and vice versa, the computed phase transition is not largely affected by electronic excitations. There is overall a slight increase in the electronic free energy with increasing disorder, indicating that the electronic excitations contribute to the stabilization of the solid solution.

We next considered the reverse impact of relaxations and SRO, i.e., how largely SRO can impact the amount of local lattice distortions. For this purpose we resort to the mean square atomic displacement (MSAD), defined as

$$
\mathrm{MSAD}=\frac{1}{N} \sum_{i}\left(\mathbf{R}_{i}-\mathbf{R}_{i}^{\text {ideal }}\right)^{2}, \quad(10)
$$

where $i$ runs over all atomic positions $\mathbf{R}_{i}$, $\mathbf{R}_{i}^{\text {ideal }}$ denotes the ideal fcc lattice positions, and $N$ is the number of atoms $i$.

In previous works [4,64], the square root of MSAD had been utilized as an effective parameter to quantify the degree of lattice distortions as well as a promising descriptor correlating with the mechanical strength of the alloy. It is therefore important to evaluate how the distortions are affected by the degree of SRO found in the alloy. We therefore resort to the 30 DFT calculations at the three representative temperatures discussed above and evaluated the MSAD parameter for all of them. The results are also shown in Fig. 6 (light red colored bars).

Similar to the relaxation energies, we again find an increase in lattice distortions with increasing disorder. The relative change is, however, less than with the relaxation energies. For example, for the M3V type of ordered structures, the square root of MSAD drops by about 25%. For the strongest SRO-containing solid solution case chosen at 1540 K, just above the transition temperature (see Fig. 2), the decrease in the lattice distortion parameter is only 6%. Assuming that the MSAD value correlates with the alloys' solid-solution strengthening ability [4,64], it would suggest that SRO has only very little impact on this mechanism. Note that other defect energetics, such as stacking-fault energies, might be more sensitive to SRO as, e.g., recently discussed for CrCoNi [6,7].

### C. Finite temperature magnetism and effective interactions in VCoNi alloys

The low temperature magnetism of VCoNi alloys depends on the alloy content and the state of order. Although fcc Co has the highest Curie temperature among all the transition metals, it is a relatively weak itinerant magnet, i.e., the local magnetic moment of Co atoms is quite sensitive to the magnetic state, the local structure, and the chemical environment of Co atoms. At 0 K, e.g., fcc random Co-V alloys are nonmagnetic if the concentration of V is larger than 50 at.%.

The ferromagnetic state of pure Ni is much weaker than that of Co, and Ni loses its magnetic moment in fcc random Ni-V alloys when the concentration of V exceeds 12 at.%. One would therefore expect the ordered $\mathrm{Ni}_{3} \mathrm{~V}$ to be nonmagnetic. This is indeed true for the ground-state $\mathrm{DO}_{22}$ structure. However, the $\mathrm{L1}_{2}-\mathrm{Ni}_{3} \mathrm{~V}$ is ferromagnetic with the main contribution to the total magnetic moment of the alloy coming from the $\mathrm{V}$ atoms, which is on the order of $1 \mu_{\mathrm{B}}$, while the magnetic moment of $\mathrm{Ni}$ is only $0.05 \mu_{\mathrm{B}}$ and is parallel to that of $\mathrm{V}$.

Exchanging some $\mathrm{Ni}$ by $\mathrm{Co}$ (randomly) in $\mathrm{L1}_{2}-\mathrm{Ni}_{3} \mathrm{~V}$ changes the ground-state magnetic structure: in the $\mathrm{L1}_{2}-\left(\mathrm{Co}_{50} \mathrm{Ni}_{50}\right)_{3} \mathrm{~V}$ alloy, the magnetic moment of $\mathrm{Ni}$ remains small, of the order of $0.05 \mu_{\mathrm{B}}$, and is parallel to that of $\mathrm{Co}$, which is about $0.5 \mu_{\mathrm{B}}$, while the magnetic moment of $\mathrm{V}$ is about $0.4 \mu_{\mathrm{B}}$ and it is antiparallel to those of $\mathrm{Co}$ and $\mathrm{Ni}$. If one now increases the concentration of $\mathrm{V}$ towards the equimolar VCoNi composition in the $\mathrm{L1}_{2}$ structure by placing randomly $\mathrm{V}$ atoms on the $\mathrm{Ni}$ and $\mathrm{Co}$ sublattices, the alloy becomes nonmagnetic. At the same time, the equimolar fcc VCoNi random alloy is ferromagnetic, with the following magnetic moments of $\mathrm{Co}, \mathrm{Ni}$, and $\mathrm{V}$: $0.6 \mu_{\mathrm{B}}, 0.07 \mu_{\mathrm{B}}$, and $-0.1 \mu_{\mathrm{B}}$, respectively. However, its magnetic energy, i.e., the difference of the total energy of this alloy in the ferromagnetic and nonmagnetic states, is only about 8 K/at.

This is a short description of what happens with the local and total magnetic moments and magnetic state in V-Co-Ni alloys at 0 K, which have been obtained in the EMTO-CPA calculations in this work. It is clear that, independently of the ordered state, VCoNi alloys can be considered as nonmagnetic at very low temperatures. However, this cannot *a priori* be assumed at high temperatures, where entropy induces large longitudinal spin fluctuations in all three alloy components. In particular, the disordered local moment (DLM) calculations [65] with the LSF entropy $3 \ln (\langle m\rangle)$ [66] show that, at 1000 K, the magnetic moments of $\mathrm{Co}, \mathrm{Ni}$, and $\mathrm{V}$ are $1.33 \mu_{\mathrm{B}}, 0.65 \mu_{\mathrm{B}}$, and $0.87 \mu_{\mathrm{B}}$, respectively. These are quite sizable magnetic moments stabilized by the LSFs and one can therefore expect that they may also affect the effective interactions in this alloy, which we discuss below.

Following Ref. [55], we consider here for clarity a quasibinary form of the pair interaction contribution to the configurational Hamiltonian:

$$
H^{(2)}=-\frac{1}{2} \sum_{p} \sum_{\alpha \neq \beta} V_{p}^{(2)-\alpha \beta} \sum_{i j \in p} \delta c_{i}^{\alpha} \delta c_{j}^{\beta}, \quad(11)
$$

where $V_{p}^{(2)-\alpha \beta}$ are the effective pair interactions of the $\alpha$ and $\beta$ alloy components at the $p$ th coordination shell; $\delta c_{i}^{\alpha}=c_{i}^{\alpha}-c^{\alpha}$ is the concentration fluctuation of the $\alpha$ component from its average concentration $c_{i}^{\alpha}$ in the alloy at site $i$.

In Fig. 7, we show the effective pair interactions for all the three pairs of alloy components in equimolar VCoNi alloy obtained from the SGPM nonmagnetic and paramagnetic DLM-LSF calculations. The DLM-LSF calculations were performed at 1000 K. These calculations are done for the ideal fcc lattice positions, without consideration of local lattice relaxations, which are quite significant in this system due to relatively large size mismatch of Co-V and Ni-V alloy pairs, as has been demonstrated above.

To get the total effective interactions, the strain-induced interactions of Co-V and Ni-V pairs has therefore been estimated in the dilute limit of pure Co and Ni considering V as an impurity. The strain-induced interactions of the Co-Ni pairs were neglected since the size difference of these alloy components is insignificant, at least compared with those of Co-V and Ni-V alloys [67]. These calculations were also done with VASP using 256-atom $(4 \times 4 \times 4)$ supercells in the ferromagnetic state to mimic the increased size of alloy components at high temperatures due to the quite substantial local

![](./images/812547258233913344_8.jpg)

FIG. 7. Effective pair interactions obtained from the SGPM calculations in nonmagnetic and at $T=1000$ K paramagnetic DLM-LSF states. Squares show the total pair interactions, i.e., SGPM interactions and strain-induced interactions obtained from separate VASP supercell calculations (see text for details). The Co-V and Ni-V pair interactions obtained in the VCoNi and respective binary M3V alloys are compared in the insets.

magnetic moments. Note that the strain-induced interactions are mainly due to the size effect, while SGPM catches the "chemical" part of interactions, related to the renormalization of the electronic states.

Obviously, the main effect due to strain-induced interactions and LSF is related to a renormalization of the effective interactions at the first coordination shell. The LSF effect is more pronounced in the case of Co-V interactions due to relatively large local magnetic moments of Co and V, while the local lattice relaxation effects are stronger in the case of Ni-V pairs, as Ni atoms are somewhat smaller than Co ones. The important point here, however, is that all these renormalizations only change the interactions quantitatively, not qualitatively. Both, Co-V and Ni-V interactions still promote the so-called (100)-type ordering specific for the L1₂ structure on the fcc lattice.

There is, however, an interesting observation if one compares the pair interactions obtained in the VCoNi alloy with those obtained for the binaries (shown in the insets in Fig. 7). In fact, the Co-V and Ni-V interactions in binary Co₃V and Ni₃V alloys are very similar (see red and black diamonds in insets in Fig. 7). The ground state of Ni₃V is, however, DO₂₂ and not L1₂. This suggests that the DO₂₂ structure is stabilized by multisite interactions, which is indeed the case. The multisite interactions are also quite strong in the equimolar VCoNi alloy, especially the three-site interactions. However, their effect on ordering in VCoNi is very small due to the equimolar, i.e., also more "symmetric," alloy composition because the three-site interactions contribute to the ordering only for asymmetric alloy compositions.

Thus, the pair effective interactions play the most important role for atomic ordering in the equimolar VCoNi alloy, and the Monte Carlo results presented in Fig. 4 can be readily understood from the pair effective interactions in Fig. 7: strong ordering of Co-V and Ni-V atoms at the first coordination shell and at the same time a quite strong repulsion at the second coordination shell. The Co-V and Ni-V SRO parameters are extremely similar in the Monte Carlo simulations presented above, which is due to the fact that the effective interactions for these pairs of alloy components are very close to each other. And, finally, the atomic SRO parameters of NiCo are also consistent with the trend in the corresponding Ni-Co effective interactions in Fig. 7.

### IV. CONCLUSIONS

The phase stability and short-range order (SRO) in the medium entropy fcc VCoNi alloy have been investigated by utilizing a recently developed machine-learned potential in combination with DFT supercell calculations as well as employing a complementary DFT-based multiple-scattering theory. On the fcc lattice, a phase transition to an M3V-type of ordering is found at about 1500 K. Above the phase transition, the SRO is mainly caused by a strong ordering of Co-V and Ni-V pairs at the first coordination shell accompanied by their relatively strong repulsion at the second coordination shell. By using two complementary DFT approaches, we showed that the impact of longitudinal spin fluctuations on the effective pair interactions is small compared with the chemical contribution and does not change the qualitative trends.

The inclusion of atomic relaxations and relaxation energies was found to be important for a quantitative description, and neglecting it results in an increase of the predicted transition temperatures by more than 30%. This is caused by the large relaxation energies of the VCoNi solid solution. On the other hand, the relative lattice distortions remain rather strong, also in the SRO-containing alloys. A small decrease in the mean square atomic displacement value suggests that SRO would affect the overall lattice distortions only very little, and hence likely the friction stress and solid solution ability. Finite-temperature electronic free-energy contributions also contribute to the stabilization of the random alloy, although their relative impact is weaker as compared with the effect of lattice relaxations.

### ACKNOWLEDGMENTS

We kindly appreciate fruitful discussions with Seok Su Sohn, Christian Liebscher, and Yuji Ikeda. F.K. and A.S. acknowledge support from the collaborative DFG-RFBR Grant (Grants No. DFG KO 5080/3-1 and No. RFBR 20-53-12012). A.V.R. acknowledges a European Research Council grant, the VINNEX center Hero-m, financed by the Swedish Governmental Agency for Innovation Systems (VINNOVA), Swedish industry, and the Royal Institute of Technology (KTH). Calculations were done using NSC

113802-8

(Linköping) and PDC (Stockholm) resources provided by the Swedish National Infrastructure for Computing (SNIC). A.V.R. also gratefully acknowledges the financial support under the scope of the COMET program within the K2 Center "Integrated Computational Material, Process and Product Engineering (IC-MPPE)" (Project No COMET 859480). This program is supported by the Austrian Federal Ministries for Climate Action, Environment, Energy, Mobility, Innovation and Technology (BMK) and for Digital and Economic Affairs (BMDW), represented by the Austrian research funding association (FFG), and the federal states of Styria, Upper Austria, and Tyrol.

[1] E. P. George, D. Raabe, and R. O. Ritchie, High-entropy alloys, Nat. Rev. Mater. 4, 515 (2019).

[2] Y. Ikeda, B. Grabowski, and F. Körmann, Ab initio phase stabilities and mechanical properties of multicomponent alloys: A comprehensive review for high entropy alloys and compositionally complex alloys, Mater. Charact. 147, 464 (2019).

[3] E. P. George, W. A. Curtin, and C. C. Tasan, High entropy alloys: A focused review of mechanical properties and deformation mechanisms, Acta Mater. 188, 435 (2020).

[4] S. S. Sohn, A. Kwiatkowski da Silva, Y. Ikeda, F. Körmann, W. Lu, W. S. Choi, B. Gault, D. Ponge, J. Neugebauer, and D. Raabe, Ultrastrong medium-entropy single-phase alloys designed via severe lattice distortion, Adv. Mater. 31, 1807142 (2019).

[5] F. Otto, A. Dlouhý, K. G. Pradeep, M. Kuběnová, D. Raabe, G. Eggeler, and E. P. George, Decomposition of the single-phase high-entropy alloy CrMnFeCoNi after prolonged anneals at intermediate temperatures, Acta Mater. 112, 40 (2016).

[6] J. Ding, Q. Yu, M. Asta, and R. O. Ritchie, Tunable stacking fault energies by tailoring local chemical order in CrCoNi medium-entropy alloys, Proc. Natl. Acad. Sci. USA 115, 8919 (2018).

[7] R. Zhang, S. Zhao, J. Ding, Y. Chong, T. Jia, C. Ophus, M. Asta, R. O. Ritchie, and A. M. Minor, Short-range order and its impact on the crconi medium-entropy alloy, Nature (London) 581, 283 (2020).

[8] F. X. Zhang, S. Zhao, K. Jin, H. Xue, G. Velisa, H. Bei, R. Huang, J. Y. P. Ko, D. Pagan, J. C. Neuefeind et al., Local Structure and Short-Range Order in a NiCoCr Solid Solution Alloy, Phys. Rev. Lett. 118, 205501 (2017).

[9] C. Niu, A. Zaddach, A. Oni, X. Sang, J. Hurt III, J. LeBeau, C. Koch, and D. Irving, Spin-driven ordering of Cr in the equiatomic high entropy alloy NiFeCrCo, Appl. Phys. Lett. 106, 161906 (2015).

[10] B. Schönfeld, C. R. Sax, J. Zemp, M. Engelke, P. Boesecke, T. Kresse, T. Boll, T. Al-Kassab, O. E. Peil, and A. V. Ruban, Local order in Cr-Fe-Co-Ni: Experiment and electronic structure calculations, Phys. Rev. B 99, 014206 (2019).

[11] Y. Ma, Q. Wang, C. Li, L. J. Santodonato, M. Feygenson, C. Dong, and P. K. Liaw, Chemical short-range orders and the induced structural transition in high-entropy alloys, Scr. Mater. 144, 64 (2018).

[12] Q. Ding, Y. Zhang, X. Chen, X. Fu, D. Chen, S. Chen, L. Gu, F. Wei, H. Bei, Y. Gao et al., Tuning element distribution, structure and properties by composition in high-entropy alloys, Nature (London) 574, 223 (2019).

[13] S. S. Sohn, A. Kwiatkowski da Silva, W. Lu, W. S. Choi, B. Gault, and D. Ponge, Acta Mat. (to be published).

[14] C. Liu, Atomic ordering and structural transformation in the V-Co-Ni ternary alloys, Metall. Trans. A 4, 1743 (1973).

[15] C. Liu and H. Inouye, Control of ordered structure and ductility of (Fe, Co, Ni) 3 V alloys, Metall. Trans. A 10, 1515 (1979).

[16] T. Onozuka, S. Yamaguchi, and M. Hirabayashi, Long-period ordered structures in the quasi-binary Co₃V-Ni₃V alloy, J. Appl. Crystallogr. 6, 273 (1973).

[17] P. Soven, Coherent-potential model of substitutional disordered alloys, Phys. Rev. 156, 809 (1967).

[18] B. Gyorffy, Coherent-potential approximation for a nonoverlapping-muffin-tin-potential model of random substitutional alloys, Phys. Rev. B 5, 2382 (1972).

[19] F. Ducastelle and F. Gautier, Generalized perturbation theory in disordered transitional alloys: Applications to the calculation of ordering energies, J. Phys. F: Met. Phys. 6, 2039 (1976).

[20] A. V. Ruban and H. L. Skriver, Screened Coulomb interactions in metallic alloys. I. Universal screening in the atomic-sphere approximation, Phys. Rev. B 66, 024201 (2002).

[21] A. V. Ruban, S. I. Simak, P. A. Korzhavyi, and H. L. Skriver, Screened Coulomb interactions in metallic alloys. II. Screening beyond the single-site and atomic-sphere approximations, Phys. Rev. B 66, 024202 (2002).

[22] B. L. Gyorffy and G. M. Stocks, Concentration Waves and Fermi Surfaces in Random Metallic Alloys, Phys. Rev. Lett. 50, 374 (1983).

[23] P. Singh, A. V. Smirnov, and D. D. Johnson, Atomic short-range order and incipient long-range order in high-entropy alloys, Phys. Rev. B 91, 224204 (2015).

[24] F. Körmann, A. V. Ruban, and M. H. Sluiter, Long-ranged interactions in bcc NbMoTaW high-entropy alloys, Mater. Res. Lett. 5, 35 (2017).

[25] P. Singh, A. Smirnov, A. Alam, and D. D. Johnson, First-principles prediction of incipient order in arbitrary high-entropy alloys: exemplified in Ti₀.₂₅CrFeNiAlₓ, Acta Mater. 189, 248 (2020).

[26] P. Singh, A. V. Smirnov, and D. D. Johnson, Ta-Nb-Mo-W refractory high-entropy alloys: Anomalous ordering behavior and its intriguing electronic origin, Phys. Rev. Mater. 2, 055004 (2018).

[27] P. Singh, A. Marshal, A. V. Smirnov, A. Sharma, G. Balasubramanian, K. G. Pradeep, and D. D. Johnson, Tuning phase stability and short-range order through Al doping in (CoCrFeMn)₁₀₀₋ₓ Alₓ high-entropy alloys, Phys. Rev. Mater. 3, 075002 (2019).

[28] F. Körmann and M. H. Sluiter, Interplay between lattice distortions, vibrations and phase stability in NbMoTaW high entropy alloys, Entropy 18, 403 (2016).

[29] T. Kostiuchenko, F. Körmann, J. Neugebauer, and A. Shapeev, Impact of lattice relaxations on phase transitions in a high-entropy alloy studied by machine-learning potentials, npj Comput. Mater. 5, 55 (2019)

113802-9

[30] M. Widom, W. P. Huhn, S. Maiti, and W. Steurer, Hybrid Monte Carlo/molecular dynamics simulation of a refractory metal high entropy alloy, *Metall. Mater. Trans. A* **45**, 196 (2014).

[31] C. Niu, W. Windl, and M. Ghasisaeidi, Multi-cell Monte Carlo relaxation method for predicting phase stability of alloys, *Scr. Mater.* **132**, 9 (2017).

[32] S. Yin, J. Ding, M. Asta, and R. O. Ritchie, *Ab initio* modeling of the energy landscape for screw dislocations in body- centered cubic high-entropy alloys, *npj Comput. Mater.* **6**, 110 (2020).

[33] J. M. Sanchez, Cluster expansion and the configurational theory of alloys, *Phys. Rev. B* **81**, 224202 (2010).

[34] A. Shapeev, Accurate representation of formation energies of crystalline alloys with many components, *Comput. Mater. Sci.* **139**, 26 (2017).

[35] G. Kresse and J. Hafner, *Ab initio* molecular dynamics for liquid metals, *Phys. Rev. B* **47**, 558 (1993).

[36] G. Kresse and J. Hafner, *Ab initio* molecular-dynamics simula- tion of the liquid-metal-amorphous-semiconductor transition in germanium, *Phys. Rev. B* **49**, 14251 (1994).

[37] G. Kresse and J. Furthmüller, Efficiency of *ab initio* total energy calculations for metals and semiconductors using a plane-wave basis set, *Comput. Mater. Sci.* **6**, 15 (1996).

[38] G. Kresse and J. Furthmüller, Efficient iterative schemes for *ab initio* total-energy calculations using a plane-wave basis set, *Phys. Rev. B* **54**, 11169 (1996).

[39] P. E. Blöchl, Projector augmented-wave method, *Phys. Rev. B* **50**, 17953 (1994).

[40] J. P. Perdew, K. Burke, and M. Ernzerhof, Generalized Gra- dient Approximation Made Simple, *Phys. Rev. Lett.* **77**, 3865 (1996).

[41] V. L. Moruzzi, J. F. Janak, and K. Schwarz, Calculated thermal properties of metals, *Phys. Rev. B* **37**, 790 (1988).

[42] A. Zunger, S.-H. Wei, L. G. Ferreira, and J. E. Bernard, Special Quasirandom Structures, *Phys. Rev. Lett.* **65**, 353 (1990).

[43] H. J. Monkhorst and J. D. Pack, Special points for Brillouin- zone integrations, *Phys. Rev. B* **13**, 5188 (1976).

[44] I. V. Oseledets, Tensor-train decomposition, *SIAM J. Sci. Comput.* **33**, 2295 (2011).

[45] L. Grasedyck, Hierarchical singular value decomposition of tensors, *SIAM J. Matrix Anal. Appl.* **31**, 2029 (2010).

[46] Q. Wu, B. He, T. Song, J. Gao, and S. Shi, Cluster expansion method and its application in computational materials science, *Comput. Mater. Sci.* **125**, 243 (2016).

[47] K. Binder, D. Heermann, L. Roelofs, A. J. Mallinckrodt, and S. McKay, Monte Carlo simulation in statistical physics, *Comput. Phys.* **7**, 156 (1993).

[48] M. K. Cowles and B. P. Carlin, Markov chain Monte Carlo convergence diagnostics: A comparative review, *J. Am. Stat. Assoc.* **91**, 883 (1996).

[49] O. Andersen, O. Jepsen, and G. Krier, Exact muffin-tin orbital theory, *Lectures on Methods of Electronic Structure Calcula- tions* (World Scientific Publishing, Singapore, 1994), p. 63.

[50] L. Vitos, I. A. Abrikosov, and B. Johansson, Anisotropic Lattice Distortions in Random Alloys from First-Principles Theory, *Phys. Rev. Lett.* **87**, 156401 (2001).

[51] L. Vitos, *Computational Quantum Mechanics for Materials En- gineers: The EMTO Method and Applications* (Springer-Verlag, London, 2007).

[52] I. Abrikosov, A. M. N. Niklasson, S. I. Simak, B. Johansson, A. V. Ruban, and H. L. Skriver, Order-$N$ Green's Function Technique for Local Environment Effects in Alloys, *Phys. Rev. Lett.* **76**, 4203 (1996).

[53] I. A. Abrikosov, S. I. Simak, B. Johansson, A. V. Ruban, and H. L. Skriver, Locally self-consistent Green's function approach to the electronic structure problem, *Phys. Rev. B* **56**, 9319 (1997).

[54] O. E. Peil, A. V. Ruban, and B. Johansson, Self-consistent supercell approach to alloys with local environment effects, *Phys. Rev. B* **85**, 165140 (2012).

[55] A. V. Ruban and M. Dehghani, Atomic configuration and properties of austenitic steels at finite temperature: Effect of longitudinal spin fluctuations, *Phys. Rev. B* **94**, 104111 (2016).

[56] F. Ducastelle, *Order and Phase Stability in Alloys* (Elsevier Science Publishers, Amsterdam, 1991) .

[57] A. V. Ruban, S. Shallcross, S. I. Simak, and H. L. Skriver, Atomic and magnetic configurational energetics by the gener- alized perturbation method, *Phys. Rev. B* **70**, 125115 (2004).

[58] J. P. Perdew and Y. Wang, Accurate and simple analytic repre- sentation of the electron-gas correlation energy, *Phys. Rev. B* **45**, 13244 (1992).

[59] A. van de Walle and G. Ceder, The effect of lattice vibrations on substitutional alloy thermodynamics, *Rev. Mod. Phys.* **74**, 11 (2002).

[60] L. Nagel, B. Fultz, and J. Robertson, Phase equilibria of Co₃V, *J. Phase Equilib.* **18**, 21 (1997).

[61] S. Wang, S. Chen, Y. Jia, Z. Hu, H. Huang, Z. Yang, A. Dong, G. Zhu, D. Wang, D. Shu *et al.*, FCC-$L1_2$ ordering transformation in equimolar FeCoNiV multi-principal element alloy, *Mater. Des.* **168**, 107648 (2019).

[62] E. Hall and S. Algie, The sigma phase, *Int. Mater. Rev.* **11**, 61 (1966).

[63] J. M. Cowley, Short- and long-range order parameters in disor- dered solid solutions, *Phys. Rev.* **120**, 1648 (1960).

[64] N. L. Okamoto, K. Yuge, K. Tanaka, H. Inui, and E. P. George, Atomic displacement in the CrMnFeCoNi high-entropy alloy— A scaling factor to predict solid solution strengthening, *AIP Adv.* **6**, 125008 (2016).

[65] B. Gyorffy, A. Pindor, J. Staunton, G. Stocks, and H. Winter, A first-principles theory of ferromagnetic phase transitions in metals, *J. Phys. F: Met. Phys.* **15**, 1337 (1985).

[66] A. V. Ruban, A. B. Belonoshko, and N. V. Skorodumova, Impact of magnetism on Fe under Earth's core conditions, *Phys. Rev. B* **87**, 014405 (2013).

[67] S. He, P. Peng, O. I. Gorbatov, and A. V. Ruban, Effec- tive interactions and atomic ordering in Ni-rich Ni-Re alloys, *Phys. Rev. B* **94**, 024111 (2016).
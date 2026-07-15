# A deep neural network interatomic potential for studying thermal conductivity of $\beta$-Ga₂O₃

Cite as: Appl. Phys. Lett. 117, 152102 (2020); https://doi.org/10.1063/5.0025051
Submitted: 12 August 2020 . Accepted: 25 September 2020 . Published Online: 14 October 2020

Ruiyang Li, Zeyu Liu, Andrew Rohskopf, Kiarash Gordiz, Asegun Henry, Eungkyu Lee, and Tengfei Luo

## COLLECTIONS
Paper published as part of the special topic on Ultrawide Bandgap Semiconductors

![](./images/812555252250181632_1.jpg)
![](./images/812555252250181632_2.jpg)
![](./images/812555252250181632_3.jpg)

## ARTICLES YOU MAY BE INTERESTED IN
### Structural transition and recovery of Ge implanted $\beta$-Ga₂O₃
Applied Physics Letters 117, 152101 (2020); https://doi.org/10.1063/5.0022170

### Electro-thermal co-design of $\beta$-(AlₓGa₁₋ₓ)₂O₃/Ga₂O₃ modulation doped field effect transistors
Applied Physics Letters 117, 153501 (2020); https://doi.org/10.1063/5.0021275

### Raman scattering in heavily donor doped $\beta$-Ga₂O₃
Applied Physics Letters 117, 152107 (2020); https://doi.org/10.1063/5.0024494

![](./images/812555252250181632_4.jpg)

Appl. Phys. Lett. 117, 152102 (2020); https://doi.org/10.1063/5.0025051
© 2020 Author(s).

117, 152102

# A deep neural network interatomic potential
for studying thermal conductivity of $\beta$-Ga$_2$O$_3$

Cite as: Appl. Phys. Lett. 117, 152102 (2020); doi: 10.1063/5.0025051
Submitted: 12 August 2020 · Accepted: 25 September 2020 ·
Published Online: 14 October 2020

![](./images/812555252250181632_5.jpg)

Ruiyang Li, $^{1}$ Zeyu Liu, $^{1}$ Andrew Rohskopf, $^{2}$ Kiarash Cordiz, $^{2}$ Asegun Henry, $^{2}$ Eungkyu Lee, $^{1,3,a)}$
and Tengfei Luo $^{1,4,5,a)}$

## AFFILIATIONS
$^{1}$Department of Aerospace and Mechanical Engineering, University of Notre Dame, Notre Dame, Indiana 46556, USA
$^{2}$Department of Mechanical Engineering, Massachusetts Institute of Technology, Cambridge, Massachusetts 02139, USA
$^{3}$Department of Mechanical System Engineering, Kumoh National Institute of Technology, 61 Daehak-ro, Gumi-si, Gyeongbuk 39177, South Korea
$^{4}$Department of Chemical and Biomolecular Engineering, University of Notre Dame, Notre Dame, Indiana 46556, USA
$^{5}$Center for Sustainable Energy of Notre Dame (ND Energy), University of Notre Dame, Notre Dame, Indiana 46556, USA

Note: This paper is part of the Special Topic on Ultrawide Bandgap Semiconductors.
$^{a)}$Authors to whom correspondence should be addressed: elee@kumoh.ac.kr and tluo@nd.edu

## ABSTRACT
$\beta$-Ga$_2$O$_3$ is a wide-bandgap semiconductor of significant technological importance for electronics, but its low thermal conductivity is an impeding factor for its applications. In this work, an interatomic potential is developed for $\beta$-Ga$_2$O$_3$ based on a deep neural network model to predict the thermal conductivity and phonon transport properties. Our potential is trained by the $ab$ $initio$ energy surface and atomic forces, which reproduces phonon dispersion in good agreement with first-principles calculations. We are able to use molecular dynamics (MD) simulations to predict the anisotropic thermal conductivity of $\beta$-Ga$_2$O$_3$ with this potential, and the calculated thermal conductivity values agree well with experimental results from 200 to 500 K. Green-Kubo modal analysis is performed to quantify the contributions of different phonon modes to the thermal transport, showing that optical phonon modes play a critical role in the thermal transport. This work provides a high-fidelity machine learning-based potential for MD simulation of $\beta$-Ga$_2$O$_3$ and serves as a good example of exploring thermal transport physics of complex semiconductor materials.

Published under license by AIP Publishing. https://doi.org/10.1063/5.0025051

As a wide-bandgap transparent oxide semiconductor, $\beta$-Ga$_2$O$_3$ has attracted much scientific and technological attention. $^{1}$ Due to its large critical electric field and relatively inexpensive growth method, $^{2}$ $\beta$-Ga$_2$O$_3$ is a promising candidate for applications in power electronic devices, $^{3}$ solar-blind UV photodetectors, $^{4}$ and gas sensors. $^{5}$ In particular, for high-power and high-voltage switching devices (e.g., transistors), the performance and reliability can be significantly affected by the high temperature induced by localized Joule heating in the channel of oxide semiconductors. $^{6,7}$ An understanding of the thermal properties of $\beta$-Ga$_2$O$_3$ is, therefore, critical for better thermal management and device packaging design.

A few experimental studies have reported the thermal conductivity values of $\beta$-Ga$_2$O$_3$. $^{8-11}$ It is shown that the measured thermal conductivity ($\kappa$) of $\beta$-Ga$_2$O$_3$ is anisotropic due to the monoclinic lattice structure. $^{12}$ Recent computational studies using the first-principles Boltzmann transport equation (BTE) method, $^{13,14}$ however, failed to predict $\kappa$ values in good agreement with the experimental values, which is likely due to factors like the difficulties in obtaining converged $\kappa$ with respect to the grid size and the broadening coefficient for screening the scattering phase space. In addition, given the large conventional cell of $\beta$-Ga$_2$O$_3$ containing 20 atoms, the first-principles calculations are highly time-consuming especially when extensive convergence tasks need to be performed. $Ab$ $initio$ molecular dynamics (AIMD) can also accurately predict thermal conductivity, $^{15}$ but simulations of $\beta$-Ga$_2$O$_3$ will be severely limited by the system size (a few hundred atoms) and timescales (tens of picoseconds). Molecular dynamics (MD) simulation using empirical potentials enables us to efficiently predict properties of both bulk materials and nanostructures, over a wider range of system sizes (up to hundreds of nanometers) $^{16}$ and timescales (up to tens of nanoseconds), $^{17}$ even though the prediction accuracy highly depends on the fidelity of the potentials. However, such accurate potentials do not exist for $\beta$-Ga$_2$O$_3$, and

developing them is usually a challenging task, which commonly involves fitting pre-selected functional forms with the *ab initio* energy surface.¹⁸ Depending on the specific problem of interest, the fixed functional form of empirical potentials can limit the applicability of the fitted potential, especially when higher order terms (e.g., force and anharmonicity) are important. Studying thermal transport is one such problem.

Thanks to the recent advances in machine learning (ML)-based techniques,¹⁹ one can reconstruct the *ab initio* potential energy surface using certain ML models, such as artificial neural networks²⁰ and Gaussian process regression²¹ with very high accuracy. Such ML models can be used as reliable fitting tools to develop interatomic potentials that precisely map the atomic configurations to the corresponding *ab initio* energies and forces. Several different ML potentials have been proposed to predict thermal properties of crystalline solids such as Si,²² Zr,²³ graphene,²⁴ and MoS₂.²⁵ Recent studies proved that even materials with more complex structures can be well simulated using ML potentials,²⁶²⁷ and a unified potential has been developed to model different phases of Si and, at the same time, predict thermal conductivity values accurately.²⁸ It has also been proved that long-range interactions are important for the correct description of thermal vibrations in covalent materials, but two-body empirical potentials using radial descriptors cannot properly capture the forces and interatomic force constants due to the lack of flexibility.²⁹ Since ML potentials can provide such flexibility and no accurate potential exists for $\beta$-Ga₂O₃, a ML potential for $\beta$-Ga₂O₃ will be highly impactful to the community.

In this work, we develop a neural network potential (NNP) to predict the thermal conductivity of $\beta$-Ga₂O₃ with MD simulations. The potential is obtained by training a deep neural network (DNN) model with the *ab initio* data of a $\beta$-Ga₂O₃ supercell. Accurate $\kappa$ values can be achieved using the NNP, which agree well with the experimental results at different temperatures. Normal mode analysis has been performed to quantify the contributions to thermal transport from different phonon modes.

In order to build the NNP for $\beta$-Ga₂O₃, we first need to generate a reference dataset for the training process. AIMD simulations³⁰ are conducted to collect the needed data (potential energy, atomic forces, atomic coordinates, and supercell lattice vectors) of $\beta$-Ga₂O₃. We perform AIMD simulations at different finite temperatures, along with static self-consistent density functional theory (DFT) calculations of randomly displaced structures at 0 K to diversify the sampled phase space. As for the AIMD simulations at finite temperatures, snapshots are collected from different molecular trajectories in the isobaric-isothermal ensemble with temperature ranging from 50 to 600 K at zero pressure. The system is first equilibrated for 1.0 ps with a time step of 1.0 fs, and then the snapshots are collected every four steps during production runs for 5.0 ps at different temperatures. The *ab initio* calculations are carried out using the QUICKSTEP algorithm implemented in the CP2K package, which is based on the Gaussian and plane wave (GPW) approaches.³¹³² We use the triple-$\zeta$ valence plus polarization (TZVP) basis sets and the Goedecker-Teter-Hutter (GTH) pseudopotentials³³ to describe core-valence interactions. The plane wave cutoff is set to be 800 Ry, and the Brillouin zone is sampled at the $\Gamma$ point. All the calculations are performed for a relaxed monoclinic $2 \times 4 \times 2$ $\beta$-Ga₂O₃ supercell, with the lattice parameters $a=12.376\,\mathring{\text{A}}$, $b=3.084\,\mathring{\text{A}}$, $c=5.893\,\mathring{\text{A}}$, and $\beta=103.83^\circ$ [Fig. 1(a)], in good agreement with the experimental results.³⁴ A total of 9200 *ab initio* snapshots are generated for the training process.

An end-to-end DNN-based potential scheme is used to obtain the NNP for $\beta$-Ga₂O₃. This MD potential scheme, namely, the Smooth Edition of Deep Potential (DeePot-SE) developed by Zhang *et al.*,³⁵ represents the lattice potential energy as a sum of atomic energies, which can be determined by the local environment of each atom. Within DeePot-SE, all the natural symmetries are preserved by mapping the local environments to an embedded feature space. More details about this scheme and related models can be found in the literature.³⁶³⁷ In this study, our DNN model is composed of an embedding network and a fitting network, and the only inputs are the chemical species and atomic coordinates. We have used a two-layer embedding network to map the original inputs to symmetry-preserving components. The fitting network is a three-layer feedforward neural network containing 160 nodes in each layer, which maps

![](./images/812555252250181632_6.jpg)
![](./images/812555252250181632_7.jpg)

FIG. 1. (a) A conventional unit cell of the $\beta$-Ga₂O₃ crystal and three crystallographic directions. The green and red spheres represent gallium atoms and oxygen atoms, respectively. (b) Standardized potential energies and atomic forces from MD simulations using NNP and *ab initio* calculations. Energies and forces are standardized by subtracting the average ($\mu$) from them and then divided by the standard deviation ($\sigma$). Both quantities are plotted within $\pm7\sigma$.

the embedded features to the atomic energies. The DNN model is trained with the ab initio dataset to minimize the loss function, which is a weighted sum of mean square errors in energy and force. The opti- mization is solved by TensorFlow's implementation of the Adam sto- chastic gradient descent method. $^{38}$ The DNN structures and training hyper-parameters are also optimized to minimize the prediction errors. All training data and potential files are included in Ref. 39. Then, we use the LAMMPS package $^{40}$ with this established NNP to perform MD simulations of $\beta-Ga_{2} O_{3}$.

The fitting accuracy can be verified by the agreement between NNP predictions and the benchmark AIMD results. We compare the NNP-predicted energies and forces for a separate testing dataset con- taining 600 AIMD snapshots that are randomly selected and not included in the training dataset. It is found that our NNP can provide very similar results compared to the testing data at different tempera- tures, with the root mean square errors of $0.0005 eV$ per atom for the potential energy and $0.078 eV / \AA$ for the atomic forces. The mean per cent errors in energy and force are $0.0003 \%$ and $9.1 \%$, respectively. For comparison, it has been reported that popular empirical potentials such as Tersoff $^{41}$ and Stillinger-Weber $^{42}$ potential for crystalline Si result in $35 \%$ and $210 \%$ error in forces, respectively. $^{43}$ Figure 1(b) shows the comparison of AIMD energies and forces and NNP- predicted quantities, indicating that the NNP accurately reproduces the ab initio energies and forces.

To evaluate the accuracy of harmonic force constants, we calcu- late the phonon dispersion relation along selected high symmetry paths. The harmonic force constants are computed by fitting displace- ment-force data using the Alamode program, $^{44}$ where symmetry irreducible displacements of $0.01 \AA$ are imposed and atomic forces are calculated with this NNP. As shown in Fig. 2(a), the phonon disper- sion using NNP agrees well with that from the first-principles calcula- tion by Santia et al., $^{13}$ while existing empirical potentials fail to capture that. $^{45,46}$ Considering the low symmetry and high anisotropy of -Ga2O3, it is reasonable to see that the phonon dispersion profile is much more complex than that of many other wide-bandgap materials, such as GaN and $ZnO^{47}$ At the same time, it is understandable why it has been very difficult to achieve an excellent agreement in phonon dispersion using a fitted empirical potential composed of simple func- tions. However, because of the versatility arising from high complexity of the DNN, harmonic force constants can be reproduced accurately with NNP, which are important for the prediction of thermal conductivity.

Equilibrium MD (EMD) simulations are preformed to evalu-ate the thermal conductivity using the Green-Kubo approach. $^{48-50}$  The Green-Kubo formula relates the instantaneous fluctuations of heat current, in terms of autocorrelation function, to thermal con- ductivity as

$$
\kappa_{\alpha}=\frac{1}{k_{B} T^{2} V} \int_{0}^{\tau_{0}}\left\langle J_{\alpha}(0) J_{\alpha}(t)\right\rangle d t. \tag{1}
$$

Here, $\kappa_{\alpha}$ denotes the thermal conductivity in the $\alpha$ direction, $k_{B}$ is the Boltzmann constant, $V$ is the volume of the simulation cell, $T$ is the temperature, $\tau_{0}$ is the integral upper limit, which should be infinite theoretically, $t$ represents the correlation time, $\langle\rangle$ denotes the ensem ble average, and $J_{\alpha}$ is the component of heat current $J$ in the $\alpha$ direction, which is expressed as $^{51}$

![](./images/812555252250181632_8.jpg)

FIG. 2. (a) Phonon dispersion relation of $\beta-Ga_{2} O_{3}$ along selected high symmetry paths using NNP. The dispersion relation agrees well with the phonon dispersionfrom DFT calculations. $^{13}$ Only the dispersion along the $\Gamma \to X_{1}$ path in Fig. S2(Ref. 13) is shown for comparison. (b) Phonon dispersion along three crystallo- graphic directions, denoted by $\Gamma \to A_{1}([100]), \Gamma \to A_{2}([010])$ , and $\Gamma \to A_{3}$ ([001]).

$$
J=\sum_{i} \boldsymbol{v}_{i} E_{i}+\sum_{i} \sum_{j \neq i} \boldsymbol{r}_{i j}\left(\frac{\partial U_{j}}{\partial \boldsymbol{r}_{i j}} \cdot \boldsymbol{v}_{i}\right), \tag{2}
$$

where $E_{i}, v_{i}, U_{j}$ , and $r_{i j}$ are the site energy, atomic velocity, potential energy, and distance between atoms $i$ and $j$ , respectively. Conventionally, one defines $\sum_{i} v_{i} E_{i}$ as the kinetic part, which is found to barely contribute to the thermal conductivity for solids and can be simply neglected. $^{52}$ We, thus, only focus on the potential part $\sum_{i} \sum_{j \neq i} r_{i j}(\frac{\partial U_{j}}{\partial r_{i j}} \cdot v_{i})$ for the heat current in this work.

We perform EMD simulations on a bulk $\beta-Ga_{2} O_{3}$ system con sisting of $4 \times 13 \times 7$ conventional unit cells consisting of 7280 atoms(at least $4 ~nm$ long in each crystallographic direction), which is usually not feasible to simulate using first-principles methods. Periodic boundary conditions are applied in all three directions, and the isobaric-isothermal ensemble is first used to equilibrate the system at zero pressure for $200 ps$ with a time step of $1.0 fs$ . Then, the

simulations are switched to the microcanonical ensemble and run for another 2 ns to collect the heat current data. To suppress the statistical uncertainty, 15 independent MD runs with different initial velocity distributions are performed to obtain the average $\kappa$ values at 200, 300, 400, and 500 K. As mentioned in Ref. 28, MD simulations using NNP are usually slower than those using empirical potentials. With the potential in this work, it takes around 6 days to simulate a 7280-atom system for 2 ns using a single Intel Xeon Silver 4110 CPU core and a NVIDIA TITAN Xp GPU, which suggests that our calculations of thermal conductivity are in a reasonable computing time range.

Figure 3(a) shows the average integral of heat current autocorrelation functions along three crystallographic directions at 300 K. The inset shows the thermal conductivity values for various simulation cell sizes, with the 7280-atom system giving results within the error bar of the case for a 5040-atom system, which are considered converged with respect to the domain size. We have observed the anisotropy in thermal conductivity, with the calculated values at 300 K to be $\kappa_{[100]}=10.68$, $\kappa_{[010]}=20.78$, and $\kappa_{[001]}=12.61$ W m$^{-1}$ K$^{-1}$. The temperature dependence of $\kappa$ is plotted in Fig. 3(b) along with the results from time-domain thermoreflectance (TDTR) measurements. $^{8,11}$ Predictions from first-principles BTE calculations are also included for comparison. $^{13,14}$ The calculated $\kappa$ values using NNP show good agreement with experimentally observed trends, with the highest $\kappa$ along the [010] direction. However, for the [100] and [001] directions, both NNP predicted results and experimental results are lower than the first-principles results. One of the reasons could be that MD simulations with NNP naturally include higher order anharmonicities, whereas the BTE method truncates the anharmonic force constants to the third order. $^{53}$ Moreover, another observation is that the BTE-calculated $\kappa$ values in the [010] and [001] directions are essentially the same, which contradicts with both experimental measurements $^{8,11}$ and our MD calculations. We, thus, cast our doubts on the BTE results, $^{13}$ which are challenging to obtain accurately given the complexity of the $\beta$-Ga$_2$O$_3$ unit cell and uncertainties in convergence with respect to different parameters in such calculations as previously mentioned. At high temperatures (>400 K), our calculated $\kappa$ values in all directions agree quantitatively with experimental measurements. At lower temperatures (e.g., 200 K), the MD results are lower than experiments, which is likely due to the size effect of the simulation domain and the overestimation of the scattering rates that cutoff the contributions from long wavelength phonons, which are more important at lower temperatures due to their increased mean free path. Here, we have not accounted for any quantum effect in our calculations, and there can be two competing quantum effects: classical statistics gives larger modal heat capacities at high frequencies but smaller phonon scattering times at low frequencies compared to quantum statistics. $^{54}$ Since the quantum correction is still controversial in accounting for quantum effects, we do not include quantum correction in this work. However, for practical applications, $\beta$-Ga$_2$O$_3$ thermal conductivity above room temperature is more important, where our NNP-EMD is able to yield good results.

![](./images/812555252250181632_9.jpg)

FIG. 3. (a) Thermal conductivity of $\beta$-Ga$_2$O$_3$ as a function of correlation time using the Green-Kubo method with NNP. These curves show the thermal conductivity along different crystal orientations at 300 K, each of which is the average of 15 independent simulations with different initial velocity distributions. The inset shows the simulation domain size-dependent thermal conductivity at 300 K. (b) Temperature-dependent thermal conductivity calculated from NNP-EMD for different crystal directions (solid symbols), compared with the reported experimental values, $^{8,11}$ (cross symbols) and first-principles predictions based on DFT force constants. $^{13,14}$ (solid lines and dashed lines).

To further study the phonon transport physics, we calculate the contribution of different phonon modes to the anisotropic thermal conductivity using Green-Kubo modal analysis (GKMA). $^{55,56}$ The GKMA method combines the lattice dynamics with the Green-Kubo formula such that the thermal conductivity becomes a direct summation of modal contributions. For a system with $N$ atoms vibrating around their equilibrium positions, one can obtain $3N$ collective modes of vibration by lattice dynamics calculations on the entire supercell. Then, the MD trajectory can be projected onto the modes by relating the velocity of each atom $j$ to the normal mode velocity $\dot{X}_n$ for mode $n$,

$$
\boldsymbol{v}_j=\dot{\boldsymbol{x}}_j=\sum_{n} \dot{\boldsymbol{x}}_{j, n}=\frac{1}{\sqrt{m_j}} \sum_{n} \boldsymbol{e}_{j, n} \dot{X}_n, \tag{3}
$$

where $m_j$ is the mass of atom $j$ and $\boldsymbol{e}_{j,n}$ is the eigenvector that gives the magnitude and direction of motion for atom $j$ in mode $n$. The normal mode velocity can be obtained by reverse transformation,

$$
\dot{X}_n=\sum_{j} \sqrt{m_j} \boldsymbol{e}_{j, n}^{*} \cdot \dot{\boldsymbol{x}}_j, \tag{4}
$$

where * represents the complex conjugate. Neglecting the kinetic part, we can write the heat current in Eq. (2) as a sum of individual modal contributions,

$$
J=\sum_{n}^{3 N} J_{n}=\sum_{n}^{3 N} \sum_{i} \sum_{j \neq i} \boldsymbol{r}_{i j}\left(\frac{\partial U_{j}}{\partial \boldsymbol{r}_{i j}} \cdot \frac{1}{\sqrt{m_{i}}} \boldsymbol{e}_{i, n} \dot{X}_{n}\right). \tag{5}
$$

By substituting Eq. (5) into Eq. (1), we have the contribution of mode $n$ in thermal conductivity

$$
\kappa_{\alpha, n}=\frac{1}{k_{B} T^{2} V} \int_{0}^{\tau_{0}}\left\langle J_{\alpha, n}(0) J_{\alpha}(t)\right\rangle d t. \tag{6}
$$

Using the modes obtained from the finite difference method, we perform a modal analysis based on the GKMA method for $\beta$-Ga₂O₃ at 300 K. The accumulation of thermal conductivity with respect to mode frequency is shown in Fig. 4. Our GKMA results using NNP show that around 80% of $\kappa$ in three crystal directions are contributed by the phonon modes below 10 THz. It is also evident that the optical phonons with frequency above 5 THz play a critical role in the thermal transport, especially in the [010] direction. At 300 K, optical phonons with frequency above 5 THz contribute over 45% of the total $\kappa_{[010]}$. The high optical phonon contribution may result from the hybridiza- tion of low energy optical modes with the longitudinal acoustic mode. $^{13,14}$ Furthermore, compared to [100] and [001] directions with relatively flat optical phonon branches [Fig. 2(b)], the [010] direction shows larger phonon group velocities, which can lead to a higher $\kappa$ contributed by optical phonons.

In summary, we have developed an interatomic potential for $\beta$-Ga₂O₃ using a deep neural network model. This NNP is trained with $ab$ initio energies and forces such that it can reproduce the pho- non dispersion in very good agreement with the first-principles results. Using MD simulations with this NNP, we predict the lattice thermal conductivity in three crystallographic directions over a range of tem- peratures from 200 to 500 K. The thermal conductivity of $\beta$-Ga₂O₃ is found to exhibit large anisotropy, and our predictions agree well with experimental results in the literature especially above room temperature. Furthermore, the modal analysis using the GKMA method reveals that optical phonon modes contribute significantly to the overall thermal conductivity at 300 K, especially in the [010] direc- tion. These results demonstrate the accuracy of our NNP in predicting thermal properties of $\beta$-Ga₂O₃. Since the accurate prediction of ther- mal conductivity implies the accuracy of our NNP in both second and third order force constants, this potential can be a foundation for MD simulations of other $\beta$-Ga₂O₃ properties, such as mechanical and thermo-mechanical properties. In addition to $\beta$-Ga₂O₃, more NNPs can be developed in the same vein to study thermal transport in other complex semiconductor materials.

![](./images/812555252250181632_10.jpg)

FIG. 4. Accumulated thermal conductivity along three crystallographic directions with respect to mode frequency at 300 K.

The authors would like to thank ONR MURI (No. N00014-18-1-2429) for the financial support. The simulations are supported by the Notre Dame Center for Research Computing and NSF through the eXtreme Science and Engineering Discovery Environment (XSEDE) computing resources provided by Texas Advanced Computing Center (TACC) Stampede II under Grant No. TG-CTS100078.

DATA AVAILABILITY

The data that support the findings of this study are openly avail- able at Ref. 39.

REFERENCES

¹F. Shan, G. Liu, W. Lee, G. Lee, I. Kim, and B. Shin, J. Appl. Phys. 98, 023504 (2005).

²S. Pearton, J. Yang, P. H. Cary IV, F. Ren, J. Kim, M. J. Tadjer, and M. A. Mastro, Appl. Phys. Rev. 5, 011301 (2018).

³M. Higashiwaki, A. Kuramata, H. Murakami, and Y. Kumagai, J. Phys. D 50, 333002 (2017).

⁴A. Singh Pratiyush, S. Krishnamoorthy, S. Vishnu Solanke, Z. Xia, R. Muralidharan, S. Rajan, and D. N. Nath, Appl. Phys. Lett. 110, 221107 (2017).

⁵M. Fleischer and H. Meixner, Sens. Actuators, B 6, 257 (1992).

⁶H. Zhou, K. Maize, G. Qiu, A. Shakouri, and P. D. Ye, Appl. Phys. Lett. 111, 092102 (2017).

⁷Z. Cheng, V. D. Wheeler, T. Bai, J. Shi, M. J. Tadjer, T. Feygelson, K. D. Hobart, M. S. Goorsky, and S. Graham, Appl. Phys. Lett. 116, 062105 (2020).

⁸Z. Guo, A. Verma, X. Wu, F. Sun, A. Hickman, T. Masui, A. Kuramata, M. Higashiwaki, D. Jena, and T. Luo, Appl. Phys. Lett. 106, 111909 (2015).

⁹Z. Galazka, K. Irmscher, R. Uecker, R. Bertram, M. Pietsch, A. Kwasniewski, M. Naumann, T. Schulz, R. Schewski, and D. Klimm, J. Cryst. Growth 404, 184 (2014).

¹⁰M. Handwerg, R. Mitdank, Z. Galazka, and S. Fischer, Semicond. Sci. Technol. 30, 024006 (2015).

¹¹P. Jiang, X. Qian, X. Li, and R. Yang, Appl. Phys. Lett. 113, 232105 (2018).

¹²Z. Liu and T. Luo, in Gallium Oxide: Materials Properties, Crystal Growth, and Devices, edited by M. Higashiwaki and S. Fujita (Springer International Publishing, Cham, 2020), p. 535.

¹³M. D. Santia, N. Tandon, and J. Albrecht, Appl. Phys. Lett. 107, 041907 (2015).

¹⁴Z. Yan and S. Kumar, Phys. Chem. Chem. Phys. 20, 29236 (2018).

¹⁵C. Carbogno, R. Ramprasad, and M. Scheffler, Phys. Rev. Lett. 118, 175901 (2017).

¹⁶K. Kadau, T. C. Germann, and P. S. Lomdahl, Int. J. Mod. Phys. C 17, 1755 (2006).

¹⁷R. A. Böckmann and H. Grubmüller, Nat. Struct. Biol. 9, 198 (2002).

¹⁸J. R. Lloyd and T. Luo, Handbook of Molecular Dynamics Potential Functions (Begell House, Inc., Redding, CT, 2011).

¹⁹X. Wan, W. Feng, Y. Wang, H. Wang, X. Zhang, C. Deng, and N. Yang, Nano Lett. 19, 3387 (2019).

²⁰J. Behler and M. Parrinello, Phys. Rev. Lett. 98, 146401 (2007).

²¹A. P. Bartók, M. C. Payne, R. Kondor, and G. Csányi, Phys. Rev. Lett. 104, 136403 (2010).

$^{22}$A. P. Bartók, J. Kermode, N. Bernstein, and G. Csányi, *Phys. Rev. X* **8**, 041048 (2018).

$^{23}$X. Qian and R. Yang, *Phys. Rev. B* **98**, 224108 (2018).

$^{24}$P. Rowe, G. Csányi, D. Alfè, and A. Michaelides, *Phys. Rev. B* **97**, 054303 (2018).

$^{25}$X. Gu and C. Zhao, *Comput. Mater. Sci.* **165**, 74 (2019).

$^{26}$G. C. Sosso, V. L. Deringer, S. R. Elliott, and G. Csányi, *Mol. Simul.* **44**, 866 (2018).

$^{27}$R. Galvelis, S. Doerr, J. M. Damas, M. J. Harvey, and G. De Fabritiis, *J. Chem. Inf. Model.* **59**, 3485 (2019).

$^{28}$R. Li, E. Lee, and T. Luo, *Mater. Today Phys.* **12**, 100181 (2020).

$^{29}$A. Rohskopf, S. Wyant, K. Gordiz, H. R. Seyf, M. G. Muraleedharan, and A. Henry, *Comput. Mater. Sci.* **184**, 109884 (2020).

$^{30}$R. Car and M. Parrinello, *Phys. Rev. Lett.* **55**, 2471 (1985).

$^{31}$J. VandeVondele, M. Krack, F. Mohamed, M. Parrinello, T. Chassaing, and J. Hutter, *Comput. Phys. Commun.* **167**, 103 (2005).

$^{32}$T. D. Kühne, M. Krack, F. R. Mohamed, and M. Parrinello, *Phys. Rev. Lett.* **98**, 066401 (2007).

$^{33}$S. Goedecker, M. Teter, and J. Hutter, *Phys. Rev. B* **54**, 1703 (1996).

$^{34}$J. Åhman, G. Svensson, and J. Albertsson, *Acta Crystallogr., Sect. C* **52**, 1336 (1996).

$^{35}$L. Zhang, J. Han, H. Wang, W. Saidi, R. Car, and E. Weinan, in *Advances in Neural Information Processing Systems* (NIPS, 2018), p. 4436–4446.

$^{36}$L. Zhang, J. Han, H. Wang, R. Car, and E. Weinan, *Phys. Rev. Lett.* **120**, 143001 (2018).

$^{37}$H. Wang, L. Zhang, J. Han, and E. Weinan, *Comput. Phys. Commun.* **228**, 178 (2018).

$^{38}$D. P. Kingma and J. Ba, arXiv:1412.6980 (2014).

$^{39}$See https://github.com/RuiyangLi6/NNP_Ga2O3 for data and code.

$^{40}$S. Plimpton, *J. Comput. Phys.* **117**(1), 1 (1995).

$^{41}$J. Tersoff, *Phys. Rev. B* **39**, 5566 (1989).

$^{42}$F. H. Stillinger and T. A. Weber, *Phys. Rev. B* **31**, 5262 (1985).

$^{43}$A. Rohskopf, H. R. Seyf, K. Gordiz, T. Tadano, and A. Henry, *npj Comput. Mater.* **3**(1), 27 (2017).

$^{44}$T. Tadano, Y. Gohda, and S. Tsuneyuki, *J. Phys.* **26**, 225402 (2014).

$^{45}$M. A. Blanco, M. B. Sahariah, H. Jiang, A. Costales, and R. Pandey, *Phys. Rev. B* **72**, 184103 (2005).

$^{46}$B. Zhang, and L. Zhang, *J. Phys. D* **53**, 434001 (2020).

$^{47}$X. Wu, J. Lee, V. Varshney, J. L. Wohlwend, A. K. Roy, and T. Luo, *Sci. Rep.* **6**, 22504 (2016).

$^{48}$R. Kubo, M. Toda, and N. Hashitsume, *Statistical Physics II: Nonequilibrium Statistical Mechanics* (Springer Science & Business Media, 2012), Vol. 31.

$^{49}$H. Meng, X. Yu, H. Feng, Z. Xue, and N. Yang, *Int. J. Heat Mass Transfer* **137**, 1241 (2019).

$^{50}$X. Yu, R. Li, T. Shiga, L. Feng, M. An, L. Zhang, J. Shiomi, and N. Yang, *J. Phys. Chem. C* **123**, 26735 (2019).

$^{51}$Z. Fan, L. F. C. Pereira, H.-Q. Wang, J.-C. Zheng, D. Donadio, and A. Harju, *Phys. Rev. B* **92**, 094301 (2015).

$^{52}$A. Kinaci, J. B. Haskins, and T. Çağin, *J. Chem. Phys.* **137**, 014106 (2012).

$^{53}$T. Feng, L. Lindsay, and X. Ruan, *Phys. Rev. B* **96**, 161201 (2017).

$^{54}$J. Turney, A. McGaughey, and C. Amon, *Phys. Rev. B* **79**, 224305 (2009).

$^{55}$W. Lv and A. Henry, *New J. Phys.* **18**, 013028 (2016).

$^{56}$H. R. Seyf, K. Gordiz, F. DeAngelis, and A. Henry, *J. Appl. Phys.* **125**, 081101 (2019).
<br>
Appl. Phys. Lett. **117**, 152102 (2020); doi: 10.1063/5.0025051
Published under license by AIP Publishing
117, 152102-6
Journal Pre-proof

![](./images/812729834575757312_1.jpg)

Thermal Conductivity Modeling using Machine Learning Potentials: Application to
Crystalline and Amorphous Silicon

Xin Qian, Shenyou Peng, Xiaobo Li, Yujie Wei, Ronggui Yang

<table>
  <tr>
    <td>PII:</td>
    <td>S2542-5293(19)30120-8</td>
  </tr>
  <tr>
    <td>DOI:</td>
    <td>https://doi.org/10.1016/j.mtphys.2019.100140</td>
  </tr>
  <tr>
    <td>Reference:</td>
    <td>MTPHYS 100140</td>
  </tr>
  <tr>
    <td>To appear in:</td>
    <td>Materials Today Physics</td>
  </tr>
  <tr>
    <td>Received Date:</td>
    <td>4 August 2019</td>
  </tr>
  <tr>
    <td>Revised Date:</td>
    <td>9 September 2019</td>
  </tr>
  <tr>
    <td>Accepted Date:</td>
    <td>18 September 2019</td>
  </tr>
</table>

Please cite this article as: X. Qian, S. Peng, X. Li, Y. Wei, R. Yang, Thermal Conductivity Modeling using Machine Learning Potentials: Application to Crystalline and Amorphous Silicon Materials Today Physics, https://doi.org/10.1016/j.mtphys.2019.100140.

This is a PDF file of an article that has undergone enhancements after acceptance, such as the addition of a cover page and metadata, and formatting for readability, but it is not yet the definitive version of record. This version will undergo additional copyediting, typesetting and review before it is published in its final form, but we are providing this version to give early visibility of the article. Please note that, during the production process, errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

© 2019 Published by Elsevier Ltd.

![](./images/812729834575757312_2.jpg)

![](./images/812729834575757312_3.jpg)

# Thermal Conductivity Modeling using Machine Learning Potentials: Application to Crystalline and Amorphous Silicon

Xin Qian¹, Shenyou Peng², Xiaobo Li,³ Yujie Wei² and Ronggui Yang¹*

¹Department of Mechanical Engineering
University of Colorado, Boulder, CO 80309, USA

²The State Key Laboratory of Nonlinear Mechanics (LNM),
Institute of Mechanics, Chinese Academy of Sciences,
Beijing, 100190, PRC

³State Key Laboratory of Coal Combustion,
School of Energy and Power Engineering,
Huazhong University of Science and Technology,
Wuhan 430074, Hubei, China

Email: [Ronggui.Yang@Colorado.Edu](mailto:Ronggui.Yang@Colorado.Edu)

ORCID: 0000-0002-3198-2014 (Xin Qian)
0000-0002-3602-6945 (Ronggui Yang)

## Abstract
First-principles based modeling on phonon dynamics and transport using density functional theory and Boltzmann transport equation has proven powerful in predicting thermal conductivity of crystalline materials, but it remains unfeasible for modeling complex crystals and disordered solids due to the prohibitive computational cost to capture the disordered structure, especially when the quasiparticle "phonon" model breaks down. Recently, machine-learning regression algorithms show great promises for building high-accuracy potential fields for atomistic modeling with length and time scales far beyond those achievable by first-principles calculations. In this work, using both crystalline and amorphous silicon as examples, we develop machine learning based potential fields for predicting thermal conductivity. The machine learning based

interatomic potential is derived from density functional theory calculations by stochastically sampling the potential energy surface in the configurational space. The thermal conductivities of both amorphous and crystalline silicon are then calculated using equilibrium molecular dynamics, which agree well with experimental measurements. This work documents the procedure for training the machine-learning based potentials for modeling thermal conductivity, and demonstrates that machine-learning based potential can be a promising tool for modeling thermal conductivity of both crystalline and amorphous materials with strong disorder.

Keywords: Thermal Conductivity, Machine Learning, Molecular Dynamics

In the past decade, first-principles based calculations have become a powerful tool for predicting thermal conductivity of a wide range of bulk $^{1-6}$ and low-dimensional crystals. $^{7-18}$ Despite the successful application in modeling the phonon properties and thermal conductivity of simple crystals, first-principles calculation for complex crystals and disordered materials remains challenging, since the computational cost increases dramatically with the lowering of crystalline symmetry and the increasing size of unit cells. $^{19,20}$ It also becomes questionable to apply the quasiparticle "phonon" picture assumed by the Boltzmann transport theory to complex crystals and disordered materials, since considerable amount of vibrational modes in these low-symmetry systems become diffusive or localized. $^{21,22}$ For modeling disordered systems, molecular dynamics (MD) simulations become a great choice since MD can easily incorporate detailed atomic structures including defects and local strains. However, MD has limited fidelity and accuracy, due to the lack of accurate interatomic potentials. Improving the accuracy of empirical interatomic potential is difficult, because the *ab-initio* potential energy surface (PES) can hardly be fitted by simple functional forms that are artificially assigned based on the pre-knowledge of the interatomic bonding. $^{19,20,23,24}$ Using "rigid" or "definite" functional forms also severely limits the transferability among different atomic structures and material phases, since it usually requires re-formulating the fitting functionals.

Recently, machine learning potential (MLP) emerges as a promising tool for bridging the gap between the first-principles calculations and MD simulations for modeling thermal transport. Since MLP does not artificially assign functional forms, it does not suffer from the limited accuracy as empirical potential does while intrinsically incorporates anharmonic effects. $^{25}$ In the past five years, MLP has been successfully developed and used to model the structural, thermodynamic and mechanical properties of some simple crystals such as Si, Ge and GaN$^{26-28}$

and amorphous materials. $^{29,30}$ However, implementations of MLP for studying thermal transport has been rare, and limited to simple crystals with relative weak disorder such as vacancies and alloys. $^{31,32}$ In this work, we develop MLP for modeling thermal conductivity of both crystalline and amorphous materials, using silicon as an example. Although there exist quite a few methods of constructing MLP such as artificial neural network, $^{26}$ supporting vector regression, $^{33}$ and spectral neighbor analysis potential (SNAP), $^{34}$ the Gaussian approximation potential (GAP) $^{27,35}$ is chosen in this work since its accuracy of predicting interatomic forces is one of the highest among other MLP methods. $^{36}$ Furthermore, the training of GAP models based on Gaussian process regression $^{37}$ only involves linear algebra without nonlinear optimizations.

First, we briefly describe here the training of the GAP models for c-Si and a-Si. To construct the training database, we use a stochastic method to generate random uncorrelated snapshots to sample the ab-initio PES. After GAP models are developed, thermal conductivity of both crystalline silicon (c-Si) and amorphous silicon (a-Si) are calculated using the equilibrium molecular dynamics (EMD) simulations. Figure 1a shows the training strategy for building the GAP model for c-Si. Since our goal is to model thermal conductivity, the GAP model should be able to fit and interpolate the PES around the equilibrium configuration accessible by thermal vibrations. Compared with ab-initio molecular dynamics which sample a trajectory in the configurational space, a more efficient method is to stochastically generate uncorrelated snapshots with random displacements: $^{38}$

$$
\boldsymbol{u}_{i}=\sum_{s} \boldsymbol{e}_{i s}\left\langle A_{i s}\right\rangle \sqrt{-2 \ln \zeta_{1}} \sin \left(2 \pi \zeta_{2}\right) \tag{1}
$$

where $\boldsymbol{u}_{i}$ is the displacement of atom $i$ from equilibrium position, $\boldsymbol{e}_{i s}$ and $\left\langle A_{i s}\right\rangle$ are the eigenvector and average amplitude of atom $i$ participating in the vibration of normal mode $s$, $\zeta_{1}$

and $\zeta_{2}$ are two random numbers uniformly distributed in the interval of (0,1). The amplitude $\langle A_{i s}(T)\rangle$ of normal mode $s$ can be written as: $^{38}$

$$
\left\langle A_{i s}\right\rangle=\sqrt{\frac{\hbar\left(n_{s}+\frac{1}{2}\right)}{m_{i} \omega_{s}}} \tag{2}
$$

where $m_{i}$ is the mass of atom $i$, $n_{s}$ is the Bose-Einstein distribution $n_{s}=\left[\exp \left(\frac{\hbar \omega_{s}}{k_{B} T}\right)-1\right]^{-1}$ at temperature $T$ and frequency $\omega_{s}$.

Clearly, generating displacement snapshots using Eqs. (1-2) requires the knowledge of force constants to obtain both normal mode frequency $\omega_{s}$ and eigenvectors $\boldsymbol{e}_{i s}$. For c-Si, $\omega_{s}$ and $\langle A_{i s}\rangle$ can be easily obtained from harmonic lattice dynamics calculations. Phonopy $^{39}$ package is used to generate supercells of c-Si containing $5 \times 5 \times 5$ primitive cells with finite displacements, then density functional theory (DFT) calculations are performed to obtain the interatomic forces using the projected augumented wave (PAW) method implemented in the VASP package. $^{40,41}$ Exchange-correlation energy is treated with the Perdew-Burke-Ernzerhof (PBE) functionals, $^{42}$ and the plane-wave cutoff energy is set to 350 eV, more than $40 \%$ larger than the maximum plane-wave energy recommended by the pseudopotential for Si. $^{43,44}$ After the vibrational frequencies and eigenvectors are obtained by solving the dynamical equation. The displacement amplitudes are calculated at 300 K and 600 K, with 100 snapshots at each temperature. In total, 50000 local chemical environments (i.e. each atom with its neighbors in each snapshot) are sampled in the database. Self-consistent field (SCF) calculations are then performed using the VASP package for each snapshot to obtain the energies and forces, which are then used as target observables to be fitted in the training dataset. We note that thermal expansion is not included in this work since silicon has negligible thermal expansion below $600 \mathrm{~K} .{ }^{45}$ For strongly anharmonic

materials, one could easily perform lattice dynamics with increased lattice constant to generate a new set of snapshots into the database, $^{38}$ or directly perform AIMD simulations to construct the database. $^{25}$ In the training process, the energies and forces are expressed as a linear combination of a set of kernel functions specified in the SOAP descriptor, $^{46}$ and the associated linear coefficients are obtained through the sparsified Gaussian process regression formalism $^{47}$ where the regression details can be found in ref. $^{48}$. Hyper-parameters used for training are listed in Table 1, while the meaning of each parameter can be found in our previous work $^{25}$ and references $^{29,31}$. Increasing cutoff radius of neighboring atoms $r_{cut}$ has negligible improvement on accuracy of phonon dispersion once it is beyond the second nearest neighbor (4.5 Å), which is also observed in fitting ab-initio potential energy surface of silicon using either empirical functionals $^{49}$ or machine learning methods. $^{28}$

Table 1. Hyper-parameters for GAP with SOAP kernels.

<table>
<thead>
  <tr>
    <th>$r_{cut}$</th>
    <td>4.5 Å</td>
  </tr>
</thead>
<tbody>
  <tr>
    <th>$d$</th>
    <td>0.5 Å</td>
  </tr>
  <tr>
    <th>$\sigma_v$ for energy</th>
    <td>0.0001 eV/atom</td>
  </tr>
  <tr>
    <th>$\sigma_v$ for forces</th>
    <td>0.001 eV/Å</td>
  </tr>
  <tr>
    <th>$\sigma_w$</th>
    <td>1.0 eV</td>
  </tr>
  <tr>
    <th>$\sigma_a$</th>
    <td>0.5 Å</td>
  </tr>
  <tr>
    <th>$\zeta$</th>
    <td>4</td>
  </tr>
  <tr>
    <th>$n_{max}$</th>
    <td>12</td>
  </tr>
  <tr>
    <th>$l_{max}$</th>
    <td>12</td>
  </tr>
</tbody>
</table>

![](./images/812729834575757312_4.jpg)

Figure 1. (a) Training strategy for c-Si: lattice dynamics using are performed with finite-displacement method using DFT. to obtain eigenvectors which is then used to generate snapshots with random displacements. DFT calculations are performed to obtain energies and forces corresponding to these snapshots. The energies and forces are then used as the training database to obtain GAP model for c-Si. (b) Training strategy for a-Si. In the first iteration of training, eigenvectors necessary to generate random snapshots are obtained from the empirical SW potential. DFT calculations are performed to obtain energies and forces corresponding to these snapshots. The energies and forces are then used as the training database to the first generation of GAP. A new set of eigenvectors are derived from the GAP model, which are used to train the next generation of GAP model. Such process is repeated until the energy change is smaller than $2{\times}10^{-3}$ eV/atom.

However, constructing the training database for a-Si is not as simple. First, it is nontrivial to obtain a relaxed amorphous network with atoms in equilibrium positions from DFT. Since a reasonable initial structure is important for the convergence of energy and forces when relaxing the atomic structures using DFT calculations, the classical MD simulation was performed first using Stillinger-Weber (SW) potential$^{50}$ to generate the initial structure of a-Si using a melt-

quench method. $^{30}$ A c-Si simulation cell containing 216 atoms (3×3×3 conventional cells) is first thermalized to 3000 K for 500 ps using Nose-Hoover reservoir (NPT ensemble) for the melting process. The temperature of Nose-Hoover reservoir is then decreased to 1 K with a rate of 10 K/ps, and is kept at the final temperature to quench the system for another 2 ns. The final structure obtained from classical MD is then used as an initial guess for the amorphous Si network for performing geometry relaxation in DFT calculations. Although larger a-Si simulation cells can be obtained using this melt-quench method, the number of atoms is limited to 64 to 216 atoms accessible by DFT calculations due to the computational cost. $^{51}$ The simulation cell obtained using SW potential is then relaxed using the conjugated gradient (CG) algorithm implemented in VASP package, $^{41}$ until the atomic forces becomes smaller than $10^{-6}$ eV/Å. The other challenge is the high computational cost to perform first-principles lattice dynamics on an amorphous network containing hundreds of atoms. To mitigate this challenge, we use the training strategy for a-Si as shown Figure 1b. Instead of generating random snapshots directly from DFT calculations, a set of trial eigenvectors is derived using the empirical SW potential. Since the optimized structure obtained from DFT calculations is not the same as the equilibrium structure obtained with the SW potential, there are soft vibrational modes with imaginary frequencies when performing lattice dynamics using SW potential. These soft modes are excluded when using Eq. (1) to sum the displacement over all modes for the first generation of random snapshots. After obtaining the trial snapshots, SCF calculations of the energy and forces were performed for each snapshot. The obtained forces and energies of the snapshots are recorded in the database for training the first generation of GAP model. Note that the first generation of the generated random displacements do not correspond to the equilibrium population of the phonon modes. To minimize the possible error induced by the unphysical

displacements, we adopted an iterative training process similar to the method used by Hellman et al. for developing temperature dependent effective potential (TDEP) method. $^{38}$ The first generation of GAP model is used to perform lattice dynamics again to generate a new set of snapshots for training the next generation of GAP model. Such process is repeated until the change of the total energy is smaller than $2 \times 10^{-3}$ eV/atom, and the soft modes disappear to ensure that the trained structure is dynamically stable using the GAP model. In this work, 50 snapshots are generated for training each generation of GAP model, and convergence of atomic energy is achieved in the third iteration of training. The computational cost for training the potential itself is small, and one can perform the training within several CPU hours without any parallelization of the code. The major computational cost of generating GAP models instead comes from constructing the database. In this work, constructing the database of a-Si only involves 150 snapshots, which is comparable to the computational cost of computing force constants of simple crystals using the displacement method. $^{38}$

After the GAP models are trained, it is necessary to evaluate not only the accuracy of GAP models for reproducing the ab-initio energies and forces in the training database, but also the accuracy in predicting energies and forces for snapshots that are not in the training database. The root-mean-squared error (RMSE) of the energies and forces of GAP models are calculated by comparing with the data in the training databases. As shown in Figure 2a-b, the RMSE of GAP reproducing the energy and interatomic forces in c-Si are 0.00057 eV/atom and 0.0215 eV/Å, respectively. Compared with the RSME of interatomic forces (0.29 eV/ Å) using empirical SW potential, the RMSE of forces using GAP model is one order of magnitude smaller. Clearly shown in Figure 2b, the SW potential has a steeper correlation to DFT forces compared with GAP models, which means that SW systematically overestimated the interatomic forces.

Compared with our previous work using ab-initio molecular dynamics (AIMD) simulations for sampling the PES for crystalline $Zr,^{25}$ similar level of regression accuracy is achieved while the required number of snapshots is one order of magnitude smaller. AIMD snapshots sample a trajectory on the ab-initio PES, which are inter-correlated. The stochastically generated snapshots are independent of each other which results in a more effective sampling in the configurational space. To evaluate the accuracy in predicting forces of snapshots outside the training database, another set of snapshots was generated as the testing dataset and the corresponding forces and energies are calculated, as shown in Figure 2a-b. The RMSE of energy and interatomic forces evaluated based on testing dataset are 0.00058 eV/atom and 0.0217 eV/Å, respectively, which are very close to the accuracy evaluated based on the training dataset. To evaluate the accuracy of harmonic force constants, we calculated dispersion along high-symmetry paths as well as phonon frequencies at symmetry irreducible points in the first Brillouin zone. The harmonic force constants of GAP models are calculated using the finite displacement method, $^{52}$ where symmetry-irreducible displacements of 0.03 Å are imposed and the corresponding interatomic forces here are calculated using the trained GAP model. As shown in Figure 2c, phonon dispersion for c-Si using GAP is in excellent agreement with DFT calculation based on Purdue-Burke-Ernzerhof (PBE) functional. In Figure 2d the phonon frequencies of symmetry irreducible q-points are also calculated and compared using a q-mesh of $13×13×13$. The maximum deviation of phonon frequencies by GAP is 0.28 THz compared with those obtained by PBE, indicating the GAP model accurately reproduces harmonic force constants. To evaluate how the uncertainty for predicting energy accumulates over time, we performed both MD simulation with GAP and AIMD simulation using the same initial velocity distribution under microcanonical (NVE) ensemble, and the trajectory of potential energy

fluctuation is recorded over time as shown in Figure 2e. In the first 250 fs, the energy fluctuation curve of MD using GAP follows closely with AIMD simulation. The two trajectories deviates significantly after 250 fs due to the accumulation of errors in predicting energy and forces. Although any small amount of error in predicting forces and energy would eventually lead to such deviation of the trajectories due to the chaotic nature of a many-body system,⁵³ evaluating the maximum time before the energy fluctuation curve of MLP bifurcate from the trajectory of AIMD still serve as a validation of the fitting accuracy of MLP.

![](./images/812729834575757312_5.jpg)

Figure 2. Comparisons of (a) energy and (b) forces computed from DFT and GAP, (c) phonon dispersion along high-symmetry paths and (d) phonon frequencies of at irreducible q-points in the first Brillouin zone of c-Si. (e) Trajectory of energy by AIMD and MD using GAP with the same initial velocity distribution. A simulation cell of 5 ×5 ×5 primitive cells is used to perform AIMD and MD simulation.

Figure 3a-b shows regression and prediction accuracy of energy and forces of a-Si. In the training database, the RMSE for reproducing energy and forces (0.034 eV/atom and 0.34 eV/Å, respectively) is one order of magnitude larger compared with the c-Si, due to the much more complicated atomic structure and local atomic environments. $^{29}$ The accuracy in predicting energy and forces becomes lower when using the training dataset. The RMSE of energy and forces are 0.066 eV/atom and 0.54 eV/Å evaluated using the testing database, respectively. Similar to the case of c-Si, the accuracy of calculating interatomic forces using GAP models still outperform the empirical SW potential by an order of magnitude, whose RMSE for the forces is as big as 1.5 eV/ Å, similar to the case in c-Si. To further assess whether GAP could accurately capture the structural features of a-Si network, the radial distribution function (RDF) $g(r)$ of the equilibrium a-Si structures obtained from GAP and PBE are calculated and compared, as shown in Figure 3c. It is observed that GAP can reasonably reproduce the radial distribution function compared with PBE functionals, while SW potential falsely predicts a peak of RDF near 3 Å.

![](./images/812729834575757312_6.jpg)

Figure. 3. (a) energy and (b) forces computed from DFT using PBE functional and GAP for a-Si. (c) Radial distribution function of equilibrium a-Si structure predicted by DFT using PBE functional, GAP and the empirical SW potential.

After the training process, GAP models are developed to predict interatomic forces need for thermal conductivity calculations. Equilibrium molecular dynamics (EMD) are performed to obtain thermal conductivity using the LAMMPS package.⁵⁴ First, the isothermal-isobaric ensemble (NPT) are used to thermalize the simulation cells for 400 ps with a time step of 0.5 fs for both c-Si and a-Si. The simulations are then switched to microcanonical (NVE) ensemble for thermal conductivity calculation. In GAP models, heat flux $\boldsymbol{J}$ is expressed as:

$$
\boldsymbol{J}=\frac{1}{V} \sum_{i}\left(E_{i} \boldsymbol{v}_{i}-\boldsymbol{S}_{i} \cdot \boldsymbol{v}_{i}\right) \tag{3}
$$

where $V$ is the volume of the simulation cell, $E_{i}$ and $\boldsymbol{v}_{i}$ are the energy and velocity of atom $i$, and the atomic virial stress tensor $\boldsymbol{S}_{i}$ is written as the outer product of relative position $\boldsymbol{r}_{j}-\boldsymbol{r}_{i}$ and local potential derivative with respect to the neighboring atom $\frac{\partial E_{i}}{\partial \boldsymbol{r}_{j}}$:

$$
\boldsymbol{S}_{i}=\sum_{j}\left(\boldsymbol{r}_{j}-\boldsymbol{r}_{i}\right) \otimes \frac{\partial E_{i}}{\partial \boldsymbol{r}_{j}} \tag{4}
$$

Thermal conductivity is then calculated using the Green-Kubo formula:

$$
k=\frac{V}{3 k_{B} T^{2}} \int\langle\boldsymbol{J}(0) \cdot \boldsymbol{J}(t)\rangle d t \tag{5}
$$

To perform the Green-Kubo integration, heat autocorrelation function $\langle\boldsymbol{J}(0) \cdot \boldsymbol{J}(t)\rangle$ is sampled every 5 fs, and integrated up to 200 ps for c-Si and 40 ps for a-Si until the thermal conductivity values stopped increasing with the increase of the correlation time, as shown in Figure 4a-b. To suppress the uncertainty, ten individual simulations with different initial velocity distributions are performed to average the heat autocorrelation function. At room temperature, the thermal conductivity values of c-Si and a-Si are found to be 121 W/mK and 1.4 W/mK, respectively. In Figure 4c, the thermal conductivity of c-Si obtained from EMD is compared with

the values calculated by iteratively solving Boltzmann transport equation, using the harmonic and third-order force constants obtained from PBE functionals (145 W/mK) and the trained GAP model (137 W/mK). Third-order anharmonic force constants of both GAP model and PBE are calculated using finite displacement method, $^{52}$ using a supercell of $5×5×5$ primitive cells and a cutoff to the fourth nearest neighbor. ShengBTE package $^{43}$ is used to iteratively solve the BTE with a $13×13×13$ $q$-mesh to sample the reciprocal $\boldsymbol{q}$ space. The slightly lower thermal conductivity obtained by solving BTE from GAP could be attributed to the error in predicting the interatomic forces. Even with the same GAP model, the thermal conductivity predicted by EMD simulation is 12% lower than that by solving BTE. At a high temperature of 500 K, the difference between thermal conductivity predicted by EMD (61 W/mK) and BTE (77 W/mK) increased to ~20%. There could be two reasons leading to the lower thermal conductivity from EMD simulations: 1). the classical statistics in MD could lead to overestimated scattering rates, $^{55}$ and 2) MD simulations with GAP naturally includes higher order anharmonicities, while BTE approach truncates the anharmonic force constants to the third order. One possible reason that GAP overestimate anharmonicity could be the built-in variance nature of Gaussian process regression. It is known that the variance of predicting forces and energies increase as the input configuration moving close to the boundary of the sampled region, and the accuracy would decrease dramatically if one tires to extrapolate the PES to the unsampled region. In this work, the PES is sampled with amplitude of thermal vibrations up to 600 K. At higher temperatures close to 600 K, the trained GAP would more frequently interpolate the PES in the region with larger variances in forces and energies, which could lead to overestimated anharmonicity. Such underestimated thermal conductivity by EMD using machine learning based interatomic potential is also observed in transition metal dichalcogenide alloys. $^{31}$ Compared with the

empirical SW potential, $^{56}$ GAP model still shows much higher accuracy in predicting thermal conductivity of c-Si. Figure 4d shows thermal conductivity of a-Si obtained from EMD using the GAP for a-Si. The predicted thermal conductivity is ~1.4 W/mK at room temperature, within the range of measurement values of a-Si (1 ~ 2 W/mK). $^{57-59}$ Considering the fact that experimentally prepared a-Si usually contains different concentrations of hydrogen which reduces the phonon localization and leads to higher thermal conductivity, $^{60}$ the thermal conductivity obtained in this work could serve as an estimation for non-hydrogenated a-Si. On the other hand, the GAP model predicts a lower thermal conductivity for a-Si than that using the empirical potentials, $^{61-63}$ probably due to the fact that the empirical potentials predicts higher bonding stiffness compared with DFT calculation using PBE functionals, consistent with the trend we observed in c-Si.

Finally, we briefly compare the computational cost of AIMD and MD using GAP. For a simulation cell containing 250 atoms, Each ionic step in AIMD takes 110 seconds of CPU time, using 48 processors with the Brillouin zone sampled at Gamma point. MD simulations using GAP models trained this work takes around 0.1 s per time step with the same number of atoms and processors, which is about three orders of magnitude faster than AIMD. However, MD calculations using GAP is much slower than that uses the empirical potential with simple functionals such as SW potential, which takes only 0.3 ms per time step under the same condition. Therefore, it still remains challenging to implement machine learning potential to model thermal conductivity of materials with multiple elements, since the computational cost would further increase with the increasing number of elements. $^{35}$

In summary, we have developed GAP models with regression accuracy of 0.02 eV/Å and 0.3 eV/Å for interatomic forces in crystalline and amorphous silicon, respectively, showing one-

order-of-magnitude improvement in both energy and forces compared with the empirical SW potential. Thermal conductivity of c-Si and a-Si at room temperature is calculated to be 121 W/mK and 1.4 W/mK respectively using EMD, agreeing reasonably well with experiments and first-principles calculations. This work shows that GAP can be a promising tool for modeling thermal conductivity of both crystalline and amorphous materials with strong disorder.

![](./images/812729834575757312_7.jpg)

Figure 4. (a-b) Thermal conductivity calculated using Green-Kubo method of (a) c-Si and (b) a-Si as a function of correlation time. The shaded area shows the standard deviation among 10 independent simulations with different initial velocity distributions (c) Thermal conductivity of crystalline silicon derived from GAP model using EMD and BTE, compared with experiments by Glassbrenner et al,⁶⁴ EMD simulation using SW potential by Volz et al.⁵⁶ BTE simulation using SW potential by Babaei et al.,³² (d)Thermal conductivity of amorphous silicon calculated using EMD with the GAP model developed in this work, compared with EMD results by Larkin et al.,⁶¹ Isaeva et al.⁶² and Lv et al., ⁶³ and experimental measurements by Zink et. al ⁵⁷., Regner et al.,⁵⁸ and Cahill et. al. ⁵⁹

**Acknowledgement:** This work is supported by NSF (Grant No. 1512776). Density functional theory calculations and training of the GAP models are performed using the Summit supercomputer, which is supported by NSF (awards ACI-1532235 and ACI-1532236), University of Colorado Boulder and Colorado State University. Molecular dynamics simulations are performed using the Yuan supercomputer supported by Supercomputing Center of Chinese Academy of Sciences.

### References

1.  W. Li, N. Mingo, L. Lindsay, D. A. Broido, D. A. Stewart and N. A. Katcho, Phys. Rev. B **85** (19) (2012).
2.  A. Ward, D. A. Broido, D. A. Stewart and G. Deinzer, Phys. Rev. B **80** (12) (2009).
3.  K. Esfarjani, G. Chen and H. T. Stokes, Phys. Rev. B **84** (8) (2011).
4.  D. A. Broido, M. Malorny, G. Birner, N. Mingo and D. A. Stewart, Appl. Phys. Lett. **91** (23), 231922 (2007).
5.  A. Ward and D. A. Broido, Phys. Rev. B **81** (8) (2010).
6.  L. Lindsay, D. A. Broido and T. L. Reinecke, Phys. Rev. Lett. **109** (9), 095901 (2012).
7.  G. Fugallo, A. Cepellotti, L. Paulatto, M. Lazzeri, N. Marzari and F. Mauri, Nano Lett **14** (11), 6109-6114 (2014).
8.  L. Lindsay, D. A. Broido and N. Mingo, Phys. Rev. B **82** (11) (2010).
9.  L. Lindsay, D. A. Broido and N. Mingo, Phys. Rev. B **83** (23) (2011).
10. X. Gu and R. Yang, J. Appl. Phys. **117** (2), 025102 (2015).
11. H. Xie, M. Hu and H. Bao, Appl. Phys. Lett. **104** (13), 131906 (2014).
12. A. Jain and A. J. McGaughey, Scientific reports **5**, 8501 (2015).
13. G. Qin, Q. B. Yan, Z. Qin, S. Y. Yue, M. Hu and G. Su, Phys. Chem. Chem. Phys. **17** (7), 4854-4858 (2015).
14. B. Sun, X. Gu, Q. Zeng, X. Huang, Y. Yan, Z. Liu, R. Yang and Y. K. Koh, Adv. Mater. **29** (3), 1603297 (2017).
15. J. Zhu, H. Park, J.-Y. Chen, X. Gu, H. Zhang, S. Karthikeyan, N. Wendel, S. A. Campbell, M. Dawber, X. Du, M. Li, J.-P. Wang, R. Yang and X. Wang, Advanced Electronic Materials **2** (5), 1600040 (2016).
16. X. Gu, B. Li and R. Yang, J. Appl. Phys. **119** (8), 085106 (2016).
17. X. Gu and R. Yang, Appl. Phys. Lett. **105** (13), 131903 (2014).
18. X. Gu and R. Yang, Phys. Rev. B **94** (7) (2016).
19. X. Qian, X. Gu and R. Yang, J. Phys. Chem. C (2015).
20. X. Qian, X. Gu and R. Yang, Nano Energy **41**, 394-407 (2017).
21. J. Yang, X. Qian, W. Pan, R. Yang, Z. Li, Y. Han, M. Zhao, M. Huang and C. Wan, Adv. Mater. **31** (24), 1808222 (2019).
22. H. R. Seyf, L. Yates, T. L. Bougher, S. Graham, B. A. Cola, T. Detchprohm, M.-H. Ji, J. Kim, R. Dupuis, W. Lv and A. Henry, npj Computational Materials **3**, 49 (2017).

23. A. Rohskopf, H. R. Seyf, K. Gordiz, T. Tadano and A. Henry, npj Computational Materials **3** (1) (2017).

24. P. C. Howell, The Journal of chemical physics **137** (22), 224111 (2012).

25. X. Qian and R. Yang, Phys. Rev. B **98** (22), 224108 (2018).

26. J. Behler and M. Parrinello, Phys. Rev. Lett. **98** (14), 146401 (2007).

27. A. P. Bartok, M. C. Payne, R. Kondor and G. Csanyi, Phys. Rev. Lett. **104** (13), 136403 (2010).

28. A. P. Bartok, J. Kermode, N. Bernstein and G. Csanyi, Physical Review X **8** (4) (2018).

29. V. L. Deringer and G. Csányi, Phys. Rev. B **95** (9), 094203 (2017).

30. V. L. Deringer, N. Bernstein, A. P. Bartok, M. J. Cliffe, R. N. Kerber, L. E. Marbella, C. P. Grey, S. R. Elliott and G. Csanyi, J Phys Chem Lett **9** (11), 2879-2885 (2018).

31. X. Gu and C. Y. Zhao, Computational Materials Science **165**, 74-81 (2019).

32. H. Babaei, R. Guo, A. Hashemi and S. Lee, arxiv: 1905.09497 (2019).

33. R. M. Balabin and E. I. Lomakina, Phys. Chem. Chem. Phys. **13** (24), 11710-11718 (2011).

34. A. P. Thompson, L. P. Swiler, C. R. Trott, S. M. Foiles and G. J. Tucker, Journal of Computational Physics **285**, 316-330 (2015).

35. A. P. Bartók and G. Csányi, Int. J. Quantum Chem **115** (16), 1051-1057 (2015).

36. Y. Zuo, C. Chen, X. Li, Z. Deng, Y. Chen, J. Behler, G. Csányi, A. V. Shapeev, A. P. Thompson, k. Mitchell, A. Wood and S. P. Ong, arXiv:1906.08888 (2019).

37. C. E. Rasmussen and C. K. I. Williams, *Gaussian Processes for Machine Learning*. (MIT Press, 2006).

38. N. Shulumba, O. Hellman and A. J. Minnich, Phys. Rev. B **95** (1) (2017).

39. A. Togo and I. Tanaka, Scripta Mater. **108**, 1-5 (2015).

40. G. Kresse and J. Furthmuller, Comput. Mater. Sci. **6**, 15-50 (1996).

41. G. Kresse and D. Joubert, Phys. Rev. B **59** (3), 1758 (1991).

42. J. P. Perdew, K. Burke and M. Ernzerhof, Phys. Rev. Lett. **77**, 3865 (1996).

43. W. Li, J. Carrete, N. A. Katcho and N. Mingo, Comput. Phys. Commun. **185** (6), 1747-1758 (2014).

44. D. Sholl and J. A. Steckel, *Density functional theory: a practical introduction*. (John Wiley & Sons, 2011).

45. Y. Okada and Y. Tokumaru, J. Appl. Phys. **56**, 314 (1984).

46. A. P. Bartók, R. Kondor and G. Csányi, Phys. Rev. B **87** (18), 184115 (2013).

47. J. Schreiter, D. Nguyen-Tuong and M. Toussaint, Neurocomputing **192**, 29-37 (2016).

48. W. J. Szlachta, A. P. Bartók and G. Csányi, Phys. Rev. B **90** (10), 104108 (2014).

49. T. J. Lenosky, B. Sadigh, E. Alonso, V. V. Bulatov, T. D. d. I. Rubia, J. Kim, A. F. Voter and J. D. Kress, Modelling Simul. Mater. Sci. Eng. **8**, 825-841 (2000).

50. J. Zi, K. Zhang and X. Xie, Phys. Rev. B **41** (18), 12915-12918 (1990).

51. A. Pedersen, L. Pizzagalli and H. Jónsson, New Journal of Physics **19** (6), 063018 (2017).

52. G. Kresse, J. Furthmuller and J. Hafner, Europhys. Lett. **32** (9), 729-734 (1995).

53. R. D. Skeel, SIAM J Sci Comput **31** (2), 1363-1378 (2009).

54. S. Plimpton, Journal of Computational Physics **117**, 1-19 (1995).

55. M. Puligheddu, Y. Xia, M. K. Y. Chan and G. Galli, arXiv:1902.08260 (2019).

56. S. G. Volz and G. Chen, Phys. Rev. B **61** (4), 2651 (2000).

57. B. L. Zink, R. Pietri and F. Hellman, Phys. Rev. Lett. **96** (5), 055902 (2006).

58. K. T. Regner, D. P. Sellan, Z. Su, C. H. Amon, A. J. McGaughey and J. A. Malen, Nature communications **4**, 1640 (2013).

59. D. G. Cahill, M. Katiyar and J. R. Abelson, Phys Rev B Condens Matter **50** (9), 6077-6081 (1994).

60. M. C. Wingert, J. Zheng, S. Kwon and R. Chen, Semicond. Sci. Technol. **31** (11), 113003 (2016).

61. J. M. Larkin and A. J. H. McGaughey, Phys. Rev. B **89**, 144303 (2014).

62. L. Isaeva, G. Barbalinardo, D. Donadio and S. Baroni, arxiv: 1904.02255 (2019).

63. W. Lv and A. Henry, New Journal of Physics **18** (1), 013028 (2016).

64. C. J. Glassbrenner and G. A. Slack, Phys. Rev. **134** (4A), A1058-A1069 (1964).

- High-fidelity machine learning potential are developed for crystalline and amorphous Si

- Efficient training is achieved through stochastic sampling of the *ab-initio* potential energy surface

- Details are documented for training the machine-learning potentials for modeling thermal conductivity
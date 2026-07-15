# Large-scale atomistic simulation of dislocation core structure in face-centered cubic metal with Deep Potential method

Fenglin Deng$^{a,b,1}$, Hongyu Wu$^{a,b,1}$, Ri He$^{a,b}$, Peijun Yang$^{c}$ and Zhicheng Zhong$^{a,b,d,*}$

$^{a}$CAS Key Laboratory of Magnetic Materials and Devices, Ningbo Institute of Materials Technology and Engineering, Chinese Academy of Sciences, Ningbo, 315201, China
$^{b}$Zhejiang Province Key Laboratory of Magnetic Materials and Application Technology, Ningbo Institute of Materials Technology and Engineering, Chinese Academy of Sciences, Ningbo, 315201, China
$^{d}$China Center of Materials Science and Optoelectronics Engineering, University of Chinese Academy of Sciences, Beijing, 100049, China
$^{c}$Northeastern University, School of Materials Science and Engineering, Shenyang, 110819, China

## ARTICLE INFO

**Keywords:**
Deep Potential
dislocation core structure
splitting width

## ABSTRACT

The core structure of dislocations is critical to their mobility, cross slip, and other plastic behaviors. Atomistic simulation of the core structure is limited by the size of first-principles density functional theory (DFT) calculation and the accuracy of classical molecular dynamics with empirical interatomic potentials. Here, we utilize a Deep Potential (DP) method learned from DFT calculations to investigate the dislocations of face-centered cubic copper on a large scale and obtain their core structures and energies. The validity of the DP description of the core structure and elastic strain from dislocation is confirmed by a fully discrete Peierls model. Moreover, the DP method can be further extended easily to dislocations with defects such as surface or vacancy, and our study will pave a way in the large-scale atomistic simulation of dislocation on the DFT level.

## 1. Introduction

Dislocation is one of the most important defects which determines plastic properties in metals [1]. Dislocation usually has a detailed core structure related to crystal properties such as elasticity and atomic bonding [2–4]. From Peierls' dislocation theory [5], the formation of core structure originates from a balance in which the elastic interaction between dislocation density tends to make the core wider, while the misfit energy is the complete opposite tendency. For example, compared with covalent crystals, breaking metallic bonds will induce small misfit energy which means a wider dislocation core [1]. In face-centered cubic (FCC) metal, determination of dislocation width is a key issue because it has a large impact on the cross slip process [6–8]. Investigating the dislocation core at atomic level will serve to indicate the experimental signatures of core effects.

For investigating the dislocation core structure, Peierls-Nabarro (P-N) model together with the $\gamma$-surface is a successful analytical model [2, 5, 9–11]. But this model cannot predict the atomic positions around the dislocation core precisely and cannot handle anisotropic material [12] or complex systems such as high entropy alloy in a satisfactory way. For atomic simulation, first-principles density functional theory (DFT) calculations can predict the atomic structures with quantum accuracy. Nevertheless, DFT calculation is limited by small length and time scale. The splitting width of the dissociated dislocation in FCC copper is up to $2\sim4$ nm from experimental observations [13, 14], which is beyond the reaches of conventional DFT methods [15]. Interatomic potentials are a very effective method for understanding the core structure but predicted dislocation core usually depends on the quality of potential [16, 17]. In addition, developing an interatomic potential for the alloy system with acceptable accuracy is not a trivial task. Accurate atomic simulations of dislocation core structure demand a generalizable potential with high accuracy.

In recent years, machine learning methods have been used as a powerful tool to develop the interatomic potential of crystalline materials [18–22]. Among them, the recently proposed Deep Potential (DP) method based on a deep neural network (DNN) can provide a DFT-level accurate interatomic potential [23, 24]. Many high accurate DP potentials have been developed for systems of vastly different materials [25–27] including metals and alloys [28, 29]. Zhang *et al.* developed a DP potential of Cu, and the accuracy of this potential has been validated. This potential outperforms the modified embedded atom method (MEAM) potentials in almost all examined properties including elasticity and stacking fault energy [28]. We try to use it in studying the dislocation core structure in copper.

In the DP method, the neural network is trained from a large dataset that contains a wide range of atomic configurations with a small number of atoms (Figure 1(a)). Each lattice configuration is labeled by atomic coordinates and the corresponding DFT energy and atomic forces. The energy calculation of variable size supercells from DNN is implemented by setting up a local environment for every atom and its neighbors inside a cutoff radius. The DP method will not output the total energy of configuration directly but return atomic energies determined by an atom's local environment. By summing atomic energies, the well-trained DP potential can be used to predict the energy and force of a large defected supercell at DFT level (Figure 1(b)).

*Corresponding author: zhong@nimte.ac.cn
$^{1}$These authors contribute equally to this work.

Large-scale atomistic simulation of dislocation core structure in face-centered cubic metal with Deep Potential method

![](./images/867752528257745543_1.jpg)

Figure 1: (a) A large dataset of DFT energies and forces of a wide range of atomic configurations. (b) The deep neural network trained by Deep Potential (c) and (d) The neural network potential can be used to predict the energy and force of large supercell that contains the vacancy, surface, and dislocation at DFT level.

In this paper, we use DP method to investigate the $1/2\langle 110\rangle\{111\}$ dislocations in FCC copper. The core structure and energy of dislocation are calculated by the DP method. Since it is almost impossible to validate the accuracy of dislocation properties obtained from the DP method by comparing DFT results, we implement the calculation of extended dislocation core structure and energy by the fully discrete Peierls model (see section 3.3) developed by Wang *et al.* [30–32]. The core structure predicted by the DP method agrees well with which obtained from the discrete model. This result demonstrates the generalizability of the DP potential of Cu. Furthermore, by analyzing the energies of dislocation arrays with different sizes, the DP method is proven to reproduce the elastic interaction between dislocations on a large scale. We also investigate the properties of a screw dislocation in Cu film and vacancy-dislocation interaction in the bulk. DP method provides significant promise for studying dislocations at the atomic level and also offers critical physical quantities for other simulation methods on a larger scale, such as discrete dislocation dynamics and phase-field simulation [33–35].

## 2. Method

### 2.1. Construction of supercell

We investigate the $1/2\langle 110\rangle\{111\}$ dislocation which possesses $\{111\}$ glide plane and $1/2\langle 110\rangle$ Burgers vector. By choosing different dislocation line directions, the $0^\circ$ (screw), $60^\circ$ (mixed), $90^\circ$ (edge), and $30^\circ$ (mixed) straight dislocation is constructed. The periodic boundary conditions (PBCs) are used in atomic simulations. Figure 2 shows two different simulation cells in this work. Symbols $\odot$ and $\otimes$ represent straight dislocations with opposite Burgers vectors. The dashed line shows a supercell that contains a dislocation quadrupole with two glide planes, while the dash-dotted one contains a dislocation dipole with only one glide plane. They both form a dislocation quadrupole array in the plane perpendicular to the dislocation line. The initial dislocations are created by the displacement fields proposed in [36], which is the exact solution of dislocation and anti-dislocation array in the P-N model.

![](./images/867752528257745543_2.jpg)

Figure 2: Schematic diagram of the screw dislocation quadrupole array. The dashed line shows a quadrupole supercell and the dash-dotted one shows a dipole supercell.

To describe the simulated supercells explicitly, the following auxiliary lattice vectors $\mathbf{a}_i$ are used,
$$
\mathbf{a}_{1}=\frac{1}{2}[011], \quad \mathbf{a}_{2}=\frac{1}{2}[2 \overline{1} 1], \quad \mathbf{a}_{3}=[11 \overline{1}].
$$

The vectors $\mathbf{a}_1$ and $\mathbf{a}_2$ represent two unequivalent choices of dislocation line direction (see Figure 5(a)). The vector $\mathbf{a}_3$ is the normal direction of glide plane. The basis vectors of quadrupole supercells can be defined by vectors $\boldsymbol{\alpha}_i=l_i \mathbf{a}_i$. In the case of dipole supercell, the basis vector $\boldsymbol{\alpha}_1$ and $\boldsymbol{\alpha}_2$ are the same with quadrupole case, while $\boldsymbol{\alpha}_3$ depends on the direction of dislocation line. If $\langle 110\rangle$ is chosen as the dislocation line direction, we set $\boldsymbol{\alpha}_3=l_3 \mathbf{a}_3+(l_2 \mathbf{a}_2+\mathbf{b})/2$, where $\mathbf{b}$ is the Burgers vector. For the $\langle 112\rangle$ case, we set $\boldsymbol{\alpha}_3=l_3 \mathbf{a}_3+(l_1 \mathbf{a}_1+\mathbf{b})/2$. Now we can use the parameters array $(l_1,l_2,l_3)$ to represent the supercell in calculation.

For testing the generalizability of the Cu DP potential, the quadrupole supercells with $(l_1,l_2,l_3)=(1,8,4)$ for $0^\circ$ and $60^\circ$ dislocation, and $(8,1,4)$ for $90^\circ$ and $30^\circ$ dislocation are constructed. Each supercell has 192 atoms. In addition, the supercell $(l_1,l_2,l_3)=(2,1,2)$ with two free surfaces or a single vacancy is also taken into account.

To investigate the dislocation core structure, we construct the dislocation dipole supercells with $(l_1,l_2,l_3)=(1,480,70)$ for screw and $60^\circ$ dislocation, and $(480,1,70)$ for edge dislocation. These cells which contain about $10^5$ atoms are large enough to obtain stable dislocation cores.

### 2.2. Computation details

To obtain the lattice configurations in testing dataset, we performed molecular dynamics calculations by Vienna *ab initio* Simulation Package (VASP) code[37, 38]. The Perdew-Burke-Ernzerhof functional [39] was adopted for structure relaxation. The kinetic energy cutoff was set to 650 eV, the K-point was set using the Monkhorst–Pack mesh [40] with the spacing $0.1\ \mathrm{\AA}^{-1}$, and the temperature was set to 300

Large-scale atomistic simulation of dislocation core structure in face-centered cubic metal with Deep Potential method

K. We also performed static calculations by VASP to obtain the generalized stacking fault energy.

We performed the molecular statics (MS) calculation by LAMMPS code [41] to obtain the stable structure of dislocation cores. The DP potential of Cu comes from the recent work by Zhang *et al.*[28], and EAM potential is proposed by Mishin *et al.* [42]. We have attempted to update the original Cu DP potential by adding generalized stacking fault configurations to the training dataset for obtaining a specified potential in studying dislocations. This modification is not evident, so the original Cu DP potential is used in this work (see section 3.2 for details).

## 3. Results
### 3.1. Accuracy of DP method

![](./images/867752528257745543_3.jpg)

Figure 3: (a), (b), (c) ((d), (e), (f)) show the atomic force obtained from DP (EAM potential) compared with DFT in systems contain the dislocations, free surfaces, the Cu vacancy respectively. The subplots show the relative frequency $p$ of $|f_i^{\text{DP/EAM}} - f_i^{\text{DFT}}|$ for each case.

The investigation of atomic simulation of dislocation demands the atomic potential possessing high accuracy in calculating atomic force and generalized stacking fault energy. In [28], only elastic properties of Cu bulk and formation energies of vacancy, surface, and intrinsic stacking fault (ISF) obtained from the DP method are compared with those obtained from other methods. For demonstrating the accuracy of DP potential, we compare the atomic forces calculated by DP and EAM potential with DFT results. The atomic forces in different configurations are shown in Figure 3. Considering the limitations of DFT method, the configurations containing dislocations are all small and unstable. The atomic forces predicted by DP agree well with DFT results, which are much better than the EAM

Table 1
The root-mean-squared errors (RMSEs) of atomic force from DP and EAM with respect to DFT references in dislocation, free surface, and vacancy systems.

| RMSEs (eV/Å) | dislocation   | free surface  | vacancy       |
|--------------|---------------|---------------|---------------|
| DP           | $8.81 \times 10^{-3}$ | $9.75 \times 10^{-3}$ | $1.28 \times 10^{-2}$ |
| EAM          | $3.23 \times 10^{-2}$ | $7.19 \times 10^{-2}$ | $6.2 \times 10^{-2}$ |

results. The root-mean-squared errors (RMSEs) of atomic force in free surface systems obtained from the DP method with respect to DFT references are one order of magnitude smaller than EAM results (see Table 1). For the systems containing dislocations or Cu vacancy, the RMSEs of DP results are about four times smaller than EAM results. The comparison of total energies shows a similar trend as well. Especially for the vacancy case, the RMSEs of energies from the DP method are about forty times smaller than EAM results.

### 3.2. Generalized stacking fault energy
The generalized stacking fault energy (GSFE) or $\gamma$-surface is extremely useful in qualitatively analyzing the spreading of a dislocation core, which is defined by the surplus energy per unit area when a relative gliding exists between two half infinite bulks[2, 10]. The negative gradient of GSFE describes the restoring stress between the mismatched lattice planes, which is necessary for the P-N model.

For interatomic potentials, the ability to calculate an accurate GSFE is rather essential because the predicted dislocation core is associated with the character of obtained GSFE [43]. Therefore, we test the accuracy of the original Cu DP potential for predicting GSFE in this section. We have attempted to update the original DP potential by including generalized stacking faults in the training dataset. The GSFE calculated by original and updated DP potential and EAM potential is compared with that obtained from DFT.

For the $\{111\}$ glide plane in FCC copper, the GSFE along two directions, [011] and $[2\overline{1}\overline{1}]$, is taken into consideration. The normal direction of the glide plane, $[11\overline{1}]$, is neglected. The structure relaxation is allowed along the direction perpendicular to the glide plane before energy calculation. We use the slip displacement field $\mathbf{s}$ to represent the rigid glide vector of generalized stacking fault which is defined by the relative displacement field of the two mismatched lattice planes, $\mathbf{s} = \mathbf{u}^\text{a} - \mathbf{u}^\text{b}$. The $\mathbf{u}^\text{a}$ ($\mathbf{u}^\text{b}$) denotes the displacement field of the atom which belongs to the lattice plane above (below) the glide plane. The component of $\mathbf{s}$ along [011] is denoted by $s_x$ and $[2\overline{1}1]$ by $s_y$. Due to the high cost of DFT calculation, only several positions along these two glide directions are calculated.

Figure 4 shows the GSFE calculated by DFT, original and updated DP, and EAM potential. There is no evident difference between original and updated DP potential in predicting GSFE. Although the training dataset contains

Large-scale atomistic simulation of dislocation core structure in face-centered cubic metal with Deep Potential method

![](./images/867752528257745543_4.jpg)

Figure 4: The generalized stacking fault energy (GSFE) along (a) [011] and (b) [2$\overline{1}$1] direction is calculated by DFT, original and updated DP, and EAM potential.

no generalized stacking fault, the GSFE predicted by the original DP potential is almost the same as that by DFT. When the rigid gliding happens around the initial or the ISF state ($\boldsymbol{s} = 0$ or $s_y = b/\sqrt{3}$, where $b = |\mathbf{b}| = 2.57\mathring{\text{A}}$), both DP and EAM potential predict the same GSFE as DFT does. When the two half bulk glide around the most unstable positions, like $s_x = b/2$ or $s_y = 2b/\sqrt{3}$ shown in Fig 4, the GSFE predicted by DP seems more accurate than that from EAM potential. Due to the original DP potential performing so well on the calculation of GSFE, we believe it can be applied to simulate the extended dislocations in FCC copper directly.

### 3.3. Core structure of dissociated dislocations
Figure 5(a) shows the well-known dissociation mechanism of a full screw dislocation with Burgers vector $\mathbf{b}$. The mismatching exists between the $\{111\}$ lattice planes with atom positions labeled as A (black circle) and B (blue dashed circle) respectively. A full screw dislocation can be constructed by gliding the atoms on B-plane from B to $B'$ relatively when region changes from I to III. Due to the relatively small unstable stacking fault (USF) energy in $\gamma$-surface of copper, the atoms at B prefer gliding to position C (red dashed circle) firstly and then from C to $B'$. Which means the $1/2\langle 110 \rangle$ dislocation in copper would dissociate to two Shockley $1/6\langle 112 \rangle$ partial dislocations which are separated by an ISF ribbon (labeled as region II in Figure 5(a)). The distance between two Shockley partial dislocations is called the splitting width (denoted by $d$).

![](./images/867752528257745543_5.jpg)

Figure 5: (a) Schematic diagram of the dissociation mechanism of the screw dislocation in FCC lattice. The dashed lines represent the dislocation line of two Shockley partial dislocations. (b) A $(l_1,l_2,l_3)=(2,40,15)$ supercell contains 7200 Cu atoms and two dissociated screw dislocations.

In this section, we investigate the core structure of $1/2\langle 110 \rangle\{111\}$ dislocations by DP, EAM potential, and the fully discrete Peierls model. The $0^\circ$, $60^\circ$, and $90^\circ$ dislocation are investigated and the $30^\circ$ dislocations are not considered because they tend to annihilate under PBCs. To obtain the stable dislocation core by DP or EAM potential, a large distance between dislocations in the quadrupole array is set and MS calculations are performed. As shown in Figure 5(b), the $0^\circ$ screw dislocations in supercell have split into Shockley partials automatically. The atoms around dislocation lines are plotted in white and stacking fault ribbons are plotted in red.

Main information of dislocation core is contained in the slip displacement $\mathbf{s}(l)$, where integer $l$ labels the atoms on the mismatched lattice plane. Due to the planar character of these extended dislocations, only the components belong to glide plane are taken into account. We define the discrete dislocation density $\rho_i(l)$ by slip displacement field, $\rho_i(l) = s_i(l+1)-s_i(l)$. The splitting width $d$ is defined by the distance between two peaks of dislocation density ($\rho_x$ in screw and edge case and $\rho_y$ in mixed case). The slip displacement $s_i(l)$ ($i=x,y$) extracted from the DP and EAM results is shown in Figure 6.

![](./images/867752528257745543_6.jpg)

Figure 6: The slip displacement and discrete density of $0^\circ$, $60^\circ$, and $90^\circ$ dislocation are obtained from EAM potential, DP method, and fully discrete Peierls model which are plotted in solid and empty circles respectively.

For evaluating core structures obtained from MS, we use the fully discrete Peierls model to study the slip displacements. DFT methods are not considered because of the large splitting width of dislocation cores in Cu. When dislocation line is along $\langle 110 \rangle$ direction, the energy functional in this discrete model is

$$
\begin{aligned}
F= & \frac{1}{4 \lambda_{x}^{2}} \sum_{l=-\infty}^{\infty}\left[\beta_{s} \rho_{x}^{2}(l)+\beta_{e} \rho_{y}^{2}(l)\right] \\
& -\frac{1}{4 \pi \lambda_{x}} \sum_{l, l^{\prime}=-\infty}^{\infty}\left[K_{s} \rho_{x}(l) \rho_{x}\left(l^{\prime}\right)+K_{e} \rho_{y}(l) \rho_{y}\left(l^{\prime}\right)\right] \times \\
& \psi^{(0)}\left(\left|l-l^{\prime}\right|+\frac{1}{2}\right)+\sum_{l=-\infty}^{\infty} \gamma\left(s_{x}, s_{y}\right),
\end{aligned}
\tag{1}
$$

where $\lambda_{x}$ is the step length defined by the distance between the lattice lines paralleled to $\langle 110 \rangle$, $K_{s}$ and $K_{e}$ are the energy pre-factors of screw and edge dislocations, $\beta_{s}$ and $\beta_{e}$ are the contact-interaction constants, $\psi^{(0)}(x)$ is the first derivative of the logarithm of the gamma function, and $\gamma(s_{x}, x_{y})$ is the $\gamma$-surface. When $\langle 112 \rangle$ is chosen as the dislocation line direction, the energy functional can be obtained by exchanging the dislocation density $\rho_{x}$ and $\rho_{y}$ and changing the $\lambda_{x}$ to $\lambda_{y}$ in (1), where $\lambda_{y}$ denotes the step length between the lattice lines paralleled to $\langle 112 \rangle$. For the $\{111\}$ glide plane in FCC lattice, the step length $\lambda_{x}=\sqrt{3} b / 2$ and $\lambda_{y}=b / 2$. The energy pre-factors $K_{s}=\mu$ and $K_{e}=\mu /(1-v)$ [1], where $\mu$ is the shear modulus and $v$ is the Poisson ratio. The contact-interaction constants are determined by the following formulae [44],

$$
\beta_{s}=\frac{3}{4}\left(1-\tan ^{2} \theta \sin ^{2} \phi\right) \mu h,
$$

$$
\beta_{e}=\frac{3}{4}\left(\frac{2-2 v}{1-2 v}-\tan ^{2} \theta \cos ^{2} \phi\right) \mu h,
$$

where $\tan \theta=1 / \sqrt{2}, \phi=\pi / 6$, and $h=\sqrt{2 / 3} b$ is the distance of the two nearest lattice planes paralleled to glide plane.

To compute the shear modulus $\mu$ and Poisson ratio $v$ under the isotropic approximation, the elastic constant calculated by DFT in [28] is used. The fitting formula for $\gamma(s_{x}, s_{y})$ in [45] is applied because an analytical formula for $\gamma$-surface in the dislocation equations is necessary. By applying the numerical method mentioned in [46], slip displacements determined by energy functional (1) are obtained and shown in Figure 6.

**Table 2**
Comparison of splitting width $d$ (in units of $b$) obtained from different methods for dislocations in Cu.

<table>
  <thead>
    <tr>
      <th></th>
      <th>EAM</th>
      <th>DP</th>
      <th>discrete model</th>
      <th>experiment values</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0°</td>
      <td>5.2</td>
      <td>6.1</td>
      <td>7.8</td>
      <td>7.0 [13]</td>
    </tr>
    <tr>
      <td>60°</td>
      <td>13.0</td>
      <td>14.7</td>
      <td>14.7</td>
      <td>13.3 [14]</td>
    </tr>
    <tr>
      <td>90°</td>
      <td>14.5</td>
      <td>15.0</td>
      <td>17.5</td>
      <td>14.9 [13]</td>
    </tr>
  </tbody>
</table>

We find these different methods predict similar core structures for respective dislocations (see Figure 6). In Table 2, the splitting widths obtained from these methods are compared with experimental values. The EAM potential tends to predict a narrower splitting width in the 0° case and the discrete model tends to predict a wider core in the 90° case. The splitting width $d$ (in unit of $b$) of 0°, 60°, and 90° dislocation calculated by DP method is 6.1, 14.7, and 15 respectively, which is close to the experiment values [13, 14] or results in recent works [47, 48]. In general, these results show that the DP method can predict the dissociated dislocation core structure with high accuracy.

### 3.4. Core energy of screw dislocation
We study the core energy and elastic energy of a screw dislocation in FCC copper by DP method and fully discrete Peierls model in this section. From continuum theory, elastic energy caused by dislocations originates from the logarithmic form interaction. This elastic energy of the dislocation quadrupole array is divergent when increasing dislocation distances and system size simultaneously. The core energy can be obtained by subtracting the elastic part from the total energy of a screw dislocation.

In DP method, we can obtain the total dislocation energy of the $(l_1, l_2, l_3)$ supercell by subtracting energy $N_a E_a$ from that of defected supercell, where $N_a = 6l_1l_2l_3$ is the number of Cu atoms in the defected system, $E_a = -3.728$ eV is the atomic energy in FCC copper from DP potential. As shown in Figure 7(a), we increase the cell parameter $l_3$ from 5 to 90 with fixed $l_2 = 40, 80, 120$, or 160. For a specified distance of dislocation dipole $L_d$, a large enough $L_h$ of supercell is necessary for ensuring the convergence of dipole energy. To investigate the distance $L_d$ dependence of dislocation elastic energy, it's enough to set $l_3 = 60$ when changing $l_2$ from 30 to 120.

For analyzing the results obtained from DP method, we use fully discrete Peierls model to calculate the energy of a dipole array that is equivalent to a quadrupole array with infinite large $L_h$. Specifically, we consider the energy caused by one screw dislocation in the $(l_1, l_2, l_3 \to \infty)$ array where all dislocations share a common glide plane. The elastic energy per unit length of one screw dislocation in it is
$$
E_{elastic} = -\frac{1}{4\pi} \sum_{l,l'=1}^{l_2} \left[ K_s \rho_x(l)\rho_x(l') + K_e \rho_y(l)\rho_y(l') \right] \times
$$
$$
\sum_{i=-\infty}^{\infty} (-1)^i \psi^{(0)} \left( \left| l - l' + il_2 \right| + \frac{1}{2} \right).
$$
where the infinity summation is truncated by a proper large number which ensures the convergence of results. Due to the locality of contact-interaction and misfit interaction, it's reasonable to define the core energy $E_{core}$ (unit length) as follows,
$$
E_{core} = \frac{1}{4\lambda_x} \sum_{l=1}^{l_2} \left[ \beta_s \rho_x^2(l) + \beta_e \rho_y^2(l) \right] + \lambda_x \sum_{l=1}^{l_2} \gamma(s_x, s_y).
$$

Then the total energy of a dislocation dipole array $(l_1, l_2, \infty)$ is
$$
E_d = 2l_1 b(E_{elastic} + E_{core}). \tag{2}
$$

It's hard to solve slip displacement $s(l)$ in dipole array self-consistently. Therefore we use the isolated dislocation result obtained in the previous section as an approximate solution.

![](./images/867752528257745543_7.jpg)

**Figure 7:** The energy of dislocation array varies with increasing distance in direction (a) [111] or (b) [211]. DP method can describe the logarithmic elastic interaction between dislocations. The dislocation energy obtained from the fully discrete Peierls model is plotted by the solid line (or dashed line with a constant shift).

The dislocation energy obtained from (2) is also shown in Fig 7(b). Compared with the discrete model result, the DP result shows a similar divergent tendency which demonstrates the long-range dislocation interaction holds in the DP

Large-scale atomistic simulation of dislocation core structure in face-centered cubic metal with Deep Potential method

method. The energy predicted by the discrete model is a little bit larger than that from the DP method. This energy deviation might come from the inaccurate core structure described by the discrete model. If this model result is moved down by about $\Delta = 0.29$ eV (about $0.028$ eV/Å for each screw dislocation), it will agree well with the energy from the DP method. With the assistance of the discrete model, we estimate the unit length core energy $E_{core}$ of a screw dislocation in copper is about $0.22$ eV/Å. These results indicate that DP can describe the long-range elastic interaction caused by dislocations and can provide valuable physical quantities such as core energy for other simulation methods.

### 3.5. Surface effect and vacancy-dislocation interaction

The above sections only concern ideal isolated dislocations or periodic dislocation array. For interpreting actual plastic properties, how other defects affect dislocation properties is very important. In this section, we study the interactions between dislocation and some intrinsic defects such as free surface and Cu vacancy.

The free surface plays a vital role in nanoscale materials and it has been studied by atomic simulations or in the Peierls' framework [49-51]. The core size and mobility of dislocation usually vary with film thickness. The vacancy-dislocation interaction is another key issue in dislocation dynamics because it governs vacancy diffusion in the vicinity of dislocation and controls the dislocation climb. This interaction has been modeled by elastic theory and atomic simulations [52, 53]. Yet investigating the surface effect or vacancy interaction of dislocations in copper by DFT is difficult because the defected system is too large. The analytical theory or classical interatomic potentials can not describe these defects precisely. Therefore DP is a proper method for studying the free surface and Cu vacancy and this method is used in this section.

Firstly, we investigate the surface effect of a screw dislocation in Cu films. The free surfaces of a Cu film are two paralleled $\{111\}$ lattice planes. The middle plane of a film is chosen as the dislocation glide plane. Four cases with different film thickness $H = 1.05, 1.47, 2.31$, and $12.38$ nm are considered. Slip displacement fields $s_x$ are extracted from the stable configurations and shown in Figure 8(a). The splitting widths $d$ and Peierls stresses $\tau_p$ are listed in Table 3. The core structure of a screw dislocation in a free-standing Cu film becomes narrower than that in an FCC copper bulk when the film thickness is smaller than 2 nm (about 10 $\{111\}$ lattice planes). For the film with thickness $H = 12.38$ nm, Peierls stress is about 7.5 MPa which is close to the bulk case (2.9 MPa obtained by molecular dynamics in [48]). If the film thickness is smaller than 3 nm, the Peierls stress of screw dislocation will be up to several hundred MPa which is much larger than that in bulk. In general, the surface will significantly affect the core and mobility of screw dislocation when the thickness of Cu film is about several nanometers.

![](./images/867752528257745543_8.jpg)

Figure 8: (a) The screw dislocation core structure in Cu films with different thicknesses. The thinner film is, the smaller splitting width is. (b) The interaction energy between the vacancy and the screw dislocation in FCC copper.

<table>
<caption>Table 3 Surface effect on the splitting width and Peierls stress of screw dislocations in different Cu films.</caption>
<thead>
  <tr>
    <th colspan="2">Film thickness $H$ (nm)</th>
    <th>1.05</th>
    <th>1.47</th>
    <th>2.31</th>
    <th>12.38</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>$d$ ($b$)</td>
    <td>(DP)</td>
    <td>4.0</td>
    <td>4.9</td>
    <td>5.9</td>
    <td>6.1</td>
  </tr>
  <tr>
    <td>$\tau_p$ (MPa)</td>
    <td>(DP)</td>
    <td>892.5</td>
    <td>501.3</td>
    <td>244.9</td>
    <td>7.5</td>
  </tr>
  <tr>
    <td>$d$ ($b$)</td>
    <td>(EAM)</td>
    <td>4.0</td>
    <td>4.5</td>
    <td>5.2</td>
    <td>5.3</td>
  </tr>
  <tr>
    <td>$\tau_p$ (MPa)</td>
    <td>(EAM)</td>
    <td>916.6</td>
    <td>589.7</td>
    <td>210.2</td>
    <td>5.2</td>
  </tr>
</tbody>
</table>

The interaction between a single vacancy and a screw dislocation $E_{int}^{V-D}$ in copper is studied by the DP method as well. We calculate the energy of a dipole supercell $(l_1,l_2,l_3)=(4,160,70)$ containing a single vacancy in the lattice plane above or below the glide plane. The zero point of $E_{int}^{V-D}$ is set by the energy of the case that Cu vacancy is far from the dislocation. As shown in Figure 8(b), the maximum attractive energy is -0.185 eV in the compressive region of the partial dislocation. In contrast to this strong attractive energy, the vacancy-dislocation interaction observed in the tensile region is much smaller.

## 4. Conclusions

In summary, we use the DP method to investigate $1/2\langle110\rangle\{111\}$ dislocation in FCC copper. The DP method

Large-scale atomistic simulation of dislocation core structure in face-centered cubic metal with Deep Potential method

can predict the energies and atomic forces for large dislocation systems on the DFT level, which is more accurate than EAM results. The DP predictions of splitting width of 0°, 60°, and 90° dislocation is close to experiment values. With the assistance of the fully discrete Peierls model, we analyze the results of the screw dislocation array obtained by the DP method. The long-range elastic behavior of dislocation can be described by the DP method well. By subtracting the elastic part from total energy, we estimate the core energy of screw dislocation in copper is 0.22 eV/Å.

In addition, the DP method demonstrates its advantages in describing the effects of intrinsic defects on dislocation. We observed significant surface effects on screw dislocation when Cu film thickness is about several nanometers. When the film thickness is smaller than 3 nm, the Peierls stress of screw dislocation will be up to several hundred MPa. For the vacancy-dislocation interaction in copper, the maximum attractive energy between vacancy and compressive side of Shockley partial dislocation is -0.185 eV. We believe the DP method will open a new avenue in studying the kink, jog, or pinning in dislocation dynamics. Moreover, compared to empirical interatomic potentials, the deep learning based DP method is easier to extend and more accessible in complex systems including high entropy alloy.

### 5. Acknowledgement
We acknowledge financial support from the National Key R&D Program of China (Grant No. 2021YFA0718900, and No. 2017YFA0303602), the Key Research Program of Frontier Sciences of CAS (Grant No. ZDBS-LY-SLH008), the National Nature Science Foundation of China (Grants No. 11974365), the Science Center of the National Science Foundation of China (52088101), and K.C. Wong Education Foundation (GJTD-2020-11). Calculations were performed at the Supercomputing Center of Ningbo Institute of Materials Technology and Engineering.

### 6. Data availability
The Cu DP potential used in this work is available in the online open data repository http://dplibrary.deepmd.net/.

### References
[1] J. P. Hirth, J. Lothe, Theory of dislocations, New York: McGraw-Hill, 1982.
[2] V. Vitek, Theory of the core structures of dislocations in body-centred-cubic metals, Crystal Lattice Defects 5 (1974) 1–34.
[3] M. S. Duesbery, G. Y. Richardson, The dislocation core in crystalline materials, Critical Reviews in Solid State and Materials Sciences 17 (1991) 1–46.
[4] V. Vitek, Core structure of screw dislocations in body-centred cubic metals: relation to symmetry and interatomic bonding, Philosophical Magazine 84 (2004) 415–428.
[5] R. Peierls, The size of a dislocation, Proceedings of the Physical Society 52 (1940) 34–37.
[6] B. Escaig, Cross-slipping process in the f.c.c. structure, in: A. B. J. A.R. Rosenfield, G.T. Hahn, R. Jaffee (Eds.), Proceedings of the Battelle Colloquium in Dislocation Dynamics, New York: McGraw-Hill, 1968, pp. 655–677.
[7] J. Bonneville, B. Escaig, J. Martin, A study of cross-slip activation parameters in pure copper, Acta Metallurgica 36 (1988) 1989–2002.
[8] T. Rasmussen, K. W. Jacobsen, T. Leffers, O. B. Pedersen, Simulations of the atomic structure, energetics, and cross slip of screw dislocations in copper, Phys. Rev. B 56 (1997) 2977–2990.
[9] F. R. N. Nabarro, Dislocations in a simple cubic lattice, Proceedings of the Physical Society 59 (1947) 256–272.
[10] V. Vitek, Intrinsic stacking faults in body-centred cubic crystals, The Philosophical Magazine: A Journal of Theoretical Experimental and Applied Physics 18 (1968) 773–786.
[11] V. V. Bulatov, E. Kaxiras, Semidiscrete variational peierls framework for dislocation core properties, Phys. Rev. Lett. 78 (1997) 4221–4224.
[12] G. Schoeck, The peierls model: Progress and limitations, Materials Science and Engineering: A 400-401 (2005) 7–17.
[13] W. M. Stobbs, C. H. Sworn, The weak beam technique as applied to the determination of the stacking-fault energy of copper, The Philosophical Magazine: A Journal of Theoretical Experimental and Applied Physics 24 (1971) 1365–1381.
[14] B. Weiler, W. Sigle, A. Seeger, High-resolution electron-microscopy study of 60°-dislocations in cu, Physica Status Solidi (A) 150 (1995) 221–225.
[15] D. Rodney, L. Ventelon, E. Clouet, L. Pizzagalli, F. Willaime, Ab initio modeling of dislocation core properties in metals and semiconductors, Acta Materialia 124 (2017) 633–659.
[16] R. Gröger, V. Vitek, Directional versus central-force bonding in studies of the structure and glide of 1/2<111> screw dislocations in bcc transition metals, Philosophical Magazine 89 (2009) 3163–3178.
[17] S. Chiesa, M. Gilbert, S. Dudarev, P. Derlet, H. V. Swygenhoven, The non-degenerate core structure of a ½<111> screw dislocation in bcc transition metals modelled using finnis–sinclair potentials: The necessary and sufficient conditions, Philosophical Magazine 89 (2009) 3235–3243.
[18] J. Behler, M. Parrinello, Generalized neural-network representation of high-dimensional potential-energy surfaces, Phys. Rev. Lett. 98 (2007) 146401.
[19] A. P. Bartók, M. C. Payne, R. Kondor, G. Csányi, Gaussian approximation potentials: The accuracy of quantum mechanics, without the electrons, Phys. Rev. Lett. 104 (2010) 136403.
[20] Y. Zhao, J. Fan, L. Su, T. Song, S. Wang, C. Qiao, Snap: A communication efficient distributed machine learning framework for edge computing, in: 2020 IEEE 40th International Conference on Distributed Computing Systems (ICDCS), 2020, pp. 584–594. doi:10.1109/ICDCS47774.2020.00072.
[21] K. T. Schütt, H. E. Sauceda, P.-J. Kindermans, A. Tkatchenko, K.-R. Müller, Schnet–a deep learning architecture for molecules and materials, The Journal of Chemical Physics 148 (2018) 241722.
[22] H. Wang, L. Zhang, J. Han, W. E, DeePMD-kit: A deep learning package for many-body potential energy representation and molecular dynamics, Comput. Phys. Commun. 228 (2018) 178–184.
[23] L. Zhang, J. Han, H. Wang, R. Car, W. E, Deep potential molecular dynamics: A scalable model with the accuracy of quantum mechanics, Phys. Rev. Lett. 120 (2018) 143001.
[24] L. Zhang, H. Wang, R. Car, W. E, Phase diagram of a deep potential water model, Phys. Rev. Lett. 126 (2021) 236001.
[25] L. Zhang, J. Han, H. Wang, W. A. Saidi, R. Car, W. E, End-to-end symmetry preserving inter-atomic potential energy model for finite and extended systems, in: Proceedings of the 32nd International Conference on Neural Information Processing Systems, 2018, pp. 4441–4451. doi:10.5555/3327345.3327356.
[26] B. Fu, Y. Sun, L. Zhang, H. Wang, B. Xu, Deep learning inter-atomic potential for thermal and phonon behaviour of silicon carbide with quantum accuracy, 2021. arXiv:2110.10843.
[27] R. He, H. Wu, L. Zhang, X. Wang, F. Fu, S. Liu, Z. Zhong, Structural phase transitions in SrTiO₃ from deep potential molecular dynamics, Phys. Rev. B 105 (2022) 064104.
[28] Y. Zhang, H. Wang, W. Chen, J. Zeng, L. Zhang, H. Wang, W. E, Dp-gen: A concurrent learning platform for the generation of reliable deep learning based potential energy models, Computer Physics
---
Deng: Preprint submitted to Elsevier  Page 8 of 9

Large-scale atomistic simulation of dislocation core structure in face-centered cubic metal with Deep Potential method

Communications 253 (2020) 107206.

[29] W. Jiang, Y. Zhang, L. Zhang, H. Wang, Accurate deep potential model for the al-cu-mg alloy in the full concentration space, Chinese Physics B 30 (2021) 050706.

[30] S. Wang, S. Zhang, J. Bai, Y. Yao, Shape change and peierls barrier of dislocation, Journal of Applied Physics 118 (2015) 244903.

[31] S. Wang, L. Huang, R. Wang, The $90^{\circ}$ partial dislocation in semiconductor silicon: An investigation from the lattice p-n theory and the first principle calculation, Acta Materialia 109 (2016) 187-201.

[32] H. Xiang, R. Wang, S. Wang, Core structure and thermal transformation of the 1/2{110}{111} screw dislocation in aluminum, Journal of Applied Physics 127 (2020) 125106.

[33] R. LeSar, Simulations of dislocation structure and response, Annual Review of Condensed Matter Physics 5 (2014) 375-407.

[34] I. Beyerlein, A. Hunter, Understanding dislocation mechanics at the mesoscale using phase field dislocation dynamics, Philosophical Transactions of the Royal Society A: Mathematical, Physical and Engineering Sciences 374 (2016) 20150166.

[35] N. Bertin, R. B. Sills, W. Cai, Frontiers in the simulation of dislocations, Annual Review of Materials Research 50 (2020) 437-464.

[36] F. Deng, X. Hu, S. Wang, Dislocation neutralizing in a self-organized array of dislocation and anti-dislocation, Chinese Physics B 28 (2019) 116103.

[37] G. Kresse, J. Furthmüller, Efficiency of ab-initio total energy calculations for metals and semiconductors using a plane-wave basis set, Computational Materials Science 6 (1996) 15 - 50.

[38] G. Kresse, J. Furthmüller, Efficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set, Phys. Rev. B 54 (1996) 11169-11186.

[39] G. I. Csonka, J. P. Perdew, A. Ruzsinszky, P. H. T. Philipsen, S. Lebègue, J. Paier, O. A. Vydrov, J. G. Ángyán, Assessing the performance of recent density functionals for bulk solids, Phys. Rev. B 79 (2009) 155107.

[40] H. J. Monkhorst, J. D. Pack, Special points for brillouin-zone integrations, Phys. Rev. B 13 (1976) 5188-5192.

[41] S. Plimpton, Fast parallel algorithms for short-range molecular dynamics, Journal of Computational Physics 117 (1995) 1-19.

[42] Y. Mishin, M. J. Mehl, D. A. Papaconstantopoulos, A. F. Voter, J. D. Kress, Structural stability and lattice defects in copper: Ab initio, tight-binding, and embedded-atom calculations, Phys. Rev. B 63 (2001) 224106.

[43] M. Duesbery, V. Vitek, Plastic anisotropy in b.c.c. transition metals, Acta Materialia 46 (1998) 1481-1492.

[44] S. F. Wang, A unified dislocation equation from lattice statics, Journal of Physics A: Mathematical and Theoretical 42 (2008) 025208.

[45] V. Vorontsov, R. Voskoboinikov, C. Rae, Shearing of $\gamma'$ precipitates in ni-base superalloys: a phase field study incorporating the effective $\gamma$-surface, Philosophical Magazine 92 (2012) 608-634.

[46] V. Karlin, V. Maz'ya, A. Movchan, J. Willis, R. Bullough, Numerical solution of nonlinear hypersingular integral equations of the peierls type in dislocation theory, SIAM Journal on Applied Mathematics 60 (2000) 664-678.

[47] G. Liu, X. Cheng, J. Wang, K. Chen, Y. Shen, Quasi-periodic variation of peierls stress of dislocations in face-centered-cubic metals, International Journal of Plasticity 90 (2017) 156-166.

[48] G. Liu, X. Cheng, J. Wang, K. Chen, Y. Shen, Improvement of nonlocal peierls-nabarro models, Computational Materials Science 131 (2017) 69-77.

[49] A. Dutta, M. Bhattacharya, P. Barat, P. Mukherjee, N. Gayathri, G. C. Das, Lattice resistance to dislocation motion at the nanoscale, Phys. Rev. Lett. 101 (2008) 115506.

[50] X. Cheng, Y. Shen, L. Zhang, X. Liu, Surface effect on the screw dislocation mobility over the peierls barrier, Philosophical Magazine Letters 92 (2012) 270-277.

[51] J. Bai, S. Wang, Screw dislocation equations in a thin film and surface effects, International Journal of Plasticity 87 (2016) 181-203.

[52] R. Bullough, R. C. Newman, The kinetics of migration of point defects to dislocations, Reports on Progress in Physics 33 (1970) 101-148.

[53] E. Clouet, The vacancy-edge dislocation interaction in fcc metals: A comparison between atomic simulations and elasticity theory, Acta Materialia 54 (2006) 3543-3552. Selected Papers from the Meeting "Micromechanics and Microstructure Evolution: Modeling, Simulation and Experiments" held in Madrid/Spain, 11-16 September 2005.

---
Deng: Preprint submitted to Elsevier
Page 9 of 9
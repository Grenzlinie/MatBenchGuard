Full length article

# Effect of stress on vacancy formation and diffusion in fcc systems: Comparison between DFT calculations and elasticity theory

Damien Connétable $^{a, *}$, Philippe Maugis $^{b}$

$^{a}$ CIRIMAT UMR 5085, CNRS-INP-UPS, ENSIACET, 4 allée Émile Monso, BP 44362, Toulouse Cedex 4 F-31030, France
$^{b}$ Aix Marseille Univ, CNRS, IM2NP, Marseille, France

---

## ARTICLE INFO

**Article history:**
Received 16 July 2020
Revised 14 September 2020
Accepted 15 September 2020
Available online 21 September 2020

**Keywords:**
Fcc systems
Vacancy
Stress effects
DFT
Elasticity theory

---

## ABSTRACT

This paper discusses the effect of stress on the solubility and diffusivity of vacancies using the elasticity theory of point defects. To support the discussion, results are compared with DFT calculations to verify model accuracy. The particular case of vacancies in aluminum is discussed in detail (DFT-elasticity), while three other metallic fcc systems - Ni, Cu and Pd - are discussed through the elasticity approach only. Different types of loading were considered: hydrostatic, multi-axial and shear stresses. In the case of a uni-axial loading, two different directions were investigated: the first along a main crystallographic direction, i.e. [001], and the second perpendicular to the dense plane (111). In order to quantify the effect of stress on diffusivity, the diffusion coefficient of each configuration was expressed for further calculations. By analyzing the symmetry break during the loading process, non-equivalent atomic jumps were identified and diffusion equations obtained. A multi-physic approach was carried out by combining first-principles calculations, to study atomic-scale processes, and a multi-state formalism, to obtain exact diffusion equations. Results show that elasticity accurately captures the effects of stress on vacancy diffusion and solubility and an application method is presented.

© 2020 Acta Materialia Inc. Published by Elsevier Ltd. All rights reserved.

---

## 1. Introduction

The solubility and diffusion mechanisms of point defects are key parameters in many fields, such as phase transformation [1], corrosion [2], plasticity [3], oxidation [4], creep, etc. Vacancies are particularly interesting because they are involved in many mechanisms and determine physical properties. For instance, vacancies participate in dislocation motions [5], radiation damage healing and in the diffusion of most atoms in solid solution in materials [6]. Numerical simulations, and specifically DFT calculations, are approaches that can be used to study them in detail.

In most cases found in the literature, simulations are carried out at ambient pressure, i.e. the lattice and atomic positions are both relaxed to obtain the atomistic parameters at zero pressure. Formation and migration energies are thus computed stress free. Still, other authors have carried out their simulations at a fixed strain (with the same lattice parameters). This type of approach necessarily leads to the use of simulations in which the stresses on the system are inevitably different. The parameters thus obtained are then used in equations to compute vacancy solubility or diffusivity, solute diffusion, etc. If thermal expansion is disregarded, these data should be representative enough to describe atomistic processes.

However, in real materials, internal or external stresses (or strains) are not always equal to zero. During thermomechanical processing or product use, internal or external stresses appear in the grains and may reach a magnitude of a few GPa. Structural defects (such as solute atoms, dislocations, precipitates, grain boundaries) also induce stresses inside the material. These stresses or strains could therefore strongly impact all physical processes in which the amount and mobility of vacancies are involved. It is therefore necessary to have a clear description of the effects of stress and strain in order to accurately describe the behavior of materials at the atomic scale. This will also help developing new materials and the ever-finer interpretation of the phenomenological behavior of matter.

This issue has been present in the literature for many years, but it is only recently that approaches have been developed to rationalize the effect of stress on vacancies. These effects have been studied for a long time only in the case of semiconductor systems for which experimental data are available. The effect of stress has been studied in the case of self-diffusion, vacancy diffusion, etc. For example, Aziz [7,8] focuses on the effect of pressure on the diffusivity of solutes and vacancies in semiconductors. He formal-

---

* Corresponding author.
E-mail addresses: damien.connetable@ensiacet.fr (D. Connétable), philippe.maugis@im2np.fr (P. Maugis).

https://doi.org/10.1016/j.actamat.2020.09.053
1359-6454/© 2020 Acta Materialia Inc. Published by Elsevier Ltd. All rights reserved.

![](./images/812564355441754112_1.jpg)
![](./images/812564355441754112_2.jpg)
![](./images/812564355441754112_3.jpg)

ized the effects of hydrostatic pressure and bi-axial stress on dif- fusion using a thermodynamic approach including atomic param- eters. A more formal approach is to study vacancy or solutes us- ing the elasticity theory. Clouet and Varvenne [9-11] rationalized the elasticity theory by proposing a reliable approach to evaluate accurately and easily the elastic tensor $\mathcal{P}$ which are key parame ters with elastic constants of the system. $\mathcal{P}$ quantifies rather pre cisely the elastic effects induced by the insertion of an atom or a defect in a crystal. Moreover, such an approach can also be used to predict the effects of composition, temperature and mechanical loading on solubility and diffusivity. It has been carried out in the specific case of carbon insertion in iron [12,13]. This is interest- ing because, in a bcc-Fe system, carbon insertion induces strongly anisotropic elastic tensor with high values.

To include the effect of stress in matter transport, Trinkle de- veloped [14] a method to take stress into account using the elastic- ity theory. Tchitchekova et al. [12] also developed a method to de- termine the energy barriers for interstitial diffusion under a stress field.

The methodology presented hereinafter succeeds in taking into account the effect of stress state within fcc-metals on vacancy sol- ubility and diffusivity. The implicit effects of temperature on lat- tice parameters are ignored for simplification purposes. To illus- trate our approach, the case of aluminum is studied in detail by comparing elasticity theory and DFT simulations. After validation, other fcc metals will be discussed, i.e. Ni, Cu and Pd structures, for which only the elasticity approach will be given.

In this study, the different loads that were considered should be sufficiently representative of the main states of stress. The simplest case, which is hydrostatic stress, but also multi-axial stresses were examined. Two cases of uni-axial loading were considered, the case of a loading along one of the main axes of the fcc phase, [001] for example, and in the direction of the dense plane, i.e. [111]. The case of bi-axial loading was also considered. In each of these cases, DFT calculations are compared to the elasticity model in terms of va- cancy formation energy and vacancy migration energy. Then, con- centration and diffusion coefficients are calculated to quantify the effect of stress. This is also an opportunity to discuss vacancy coef- ficients in systems undergoing a deformation by studying explicitly the effect of deformation by characterizing the symmetry break. This work shows that the elasticity theory is able to capture qual- itatively and quantitatively the physics of the load.

The DFT procedure is described in Section 2 and the elastic- ity model in Section 3. Preliminary results are thereafter presented and discussed in Section 4. To conclude, Section 5 examines the comparison between DFT calculations and elasticity model results for different loadings.

## 2. DFT Approach

### 2.1. Theoretical calculation method

Atomistic calculations were performed using density functional theory (DFT) with VASP (Vienna ab initio simulation package) [15]. Self-consistent Kohn-Sham equations [16] were solved using projector augmented wave (PAW) pseudo-potentials [17], in the framework of the Perdew-Burke-Ernzerhof exchange and correla- tion functional (PBE [18]). For Al, Cu and Pd, calculations were performed without spin effects, contrary to nickel which exhibits a magnetism equal to about $0.72 \mu_{B}$ per atom. The plane-wave energy cut-off was set to 600 eV. Equivalent $12 \times 12 \times 12$ Monkhorst-Pack meshes [19] were used to sample the first Bril- louin zone of super-cells $(2 \times 2 \times 2)$. Additional simulations were performed with denser k-mesh grids (up to $24 \times 24 \times 24$ ) for the Al system. The value of the vacancy formation energy is then slightly modified; the difference, about 10 meV for the $2 \times 2 \times 2$ super-cell, remains negligible in view of the numerical cost. Re- garding the values of the elastic tensor parameters, the difference is even smaller, less than $0.1 \%$.

To perform a calculation for a given loading (uni-axial, bi-axial, shear or hydrostatic stress), the components of the stress tensor σ_ij were fixed based on the loading during relaxation (super-cell shape, volume and atomic positions). For instance, in the case of uni-axial loading along the z direction, a series of calculations were conducted with different fixed values of $\sigma_{z z}$ stresses while the other stress components were set to zero. The internal energies (and vibrational energies for the hydrostatic loading) for a given stress were then obtained through simulations, for the system with defect as well as for the reference state. For each configuration (with and without point defect), lattice parameters and energies were fitted as a function of stress with a sixth-order polynomial.

Considering the transformations that occur under constant tem- perature T and uniform stress tensor $\sigma$ , the thermodynamic equi librium is reached when the Gibbs energy of the system $G[\sigma, T]$ is at its minimum. In the presence of vacancies, function G includes the Gibbs energy of formation of a mono-vacancy, $G^{f}[\sigma, T]$ . Forma tion of a vacancy in a crystal implies the relaxation of the crystal lattice around the vacancy, the creation of an ad-atom at the sur- face of the crystal and a change in the phonon spectrum. In the present approach, the Gibbs energy of formation therefore consists of three terms:
$$
G^{\mathrm{f}}[\boldsymbol{\sigma}, T]=H^{\mathrm{rel}}[\boldsymbol{\sigma}]+p V_{a t}+G_{\mathrm{vib}}^{\mathrm{f}}[\boldsymbol{\sigma}, T].\qquad(1)
$$

The first term $H^{rel}[\sigma]$ is the enthalpy of relaxation:
$$
H^{\mathrm{rel}}[\boldsymbol{\sigma}]=U^{\mathrm{f}}[\boldsymbol{\sigma}]-V \sigma_{i j} \epsilon_{i j}^{\mathrm{rel}}\qquad(2)
$$
where $U^{f}[\sigma]$ is the change in internal energy due to the atom re laxation around the vacancy, $\epsilon_{i j}^{rel }$ is the uniform strain resulting from the relaxation and V is the volume of the system. The second term $p V_{a t}$ in Eq. 1 is the work of the system against the external pressure p when the ad-atom is created. $p=-\frac{1}{3} \sigma_{i i}$ is the pressure, and $V_{a t}$ is the atomic volume of the lattice. The last term $G_{vib }^{f}[\sigma, T]$ is the change in vibrational Gibbs energy due to the vacancy. In the linear elasticity approach, the vibration effects will be neglected, so that the enthalpy part of the Gibbs energy of formation will be expressed as:
$$
H^{\mathrm{f}}[\boldsymbol{\sigma}]=U^{\mathrm{f}}[\boldsymbol{\sigma}]-V \sigma_{i j} \epsilon_{i j}^{\mathrm{rel}}+p V_{a t}.\qquad(3)
$$

### 2.2. Formation energies

From DFT calculations, the relaxation part of the internal energy of vacancy formation in a crystal submitted to a uniform stress $\sigma$ can be determined by:
$$
U^{\mathrm{f}}[\boldsymbol{\sigma}]=E_{o}^{\text {bulk+vac }}[\boldsymbol{\sigma}]-\frac{N-1}{N} E_{o}^{\text {bulk }}[\boldsymbol{\sigma}].\qquad(4)
$$
$E_{o}^{bulk+vac }[\sigma]$ and $E_{o}^{bulk }[\sigma]$ are the DFT energies of a super-cell com posed of N atomic sites, with and without vacancy, respectively, computed for a given stress tensor $\sigma$ . $G_{vib }^{f}[\sigma, T]$ corresponds to the phonon contribution to the Gibbs energy of formation calculated at temperature T. For simplification purposes, it was only taken into account for the hydrostatic loading. It is given by the standard re- lationship
$$
G_{\mathrm{vib}}^{\mathrm{f}}[\boldsymbol{\sigma}, T]=G_{\mathrm{vib}}^{\text {bulk+vac }}[\boldsymbol{\sigma}, T]-\frac{N-1}{N} G_{\mathrm{vib}}^{\text {bulk }}[\boldsymbol{\sigma}, T]\qquad(5)
$$
where the vibrational Gibbs energy is expressed by:
$$
G_{\mathrm{vib}}[\boldsymbol{\sigma}, T]=k_{\mathrm{B}} T \sum_{n, q} \ln \left[2 \sinh \left(\frac{\hbar \omega_{n, q}[\boldsymbol{\sigma}, T]}{2 k_{\mathrm{B}} T}\right)\right].\qquad(6)
$$
$k_{B}$ is the Boltzman's constant, $\omega_{n, q}$ are the frequencies of all atoms in the wave vector $\boldsymbol{q}$ and the mode n. Interatomic force constants

(IFC) were computed using the finite displacements method on 2 × 2 × 2 super-cells, to limit numerical costs induced by simulations. $G_{\text{vib}}[\boldsymbol{\sigma}, T]$ was then computed using 20 × 20 × 20 $\mathbf{q}$-meshes.

In all loadings subsequently considered, there is only one non-equivalent vacancy. In the dilute approximation, the site fraction of vacancies at equilibrium, $C_{\mathrm{v}}$, is therefore related to the Gibbs energy of formation through the well-known equation:

$$
C_{\mathrm{v}}[\boldsymbol{\sigma}, T]=\exp \left[-\frac{G^{\mathrm{f}}[\boldsymbol{\sigma}, T]}{k_{\mathrm{B}} T}\right]. \tag{7}
$$

Quasiharmonic and anharmonic effects are neglected here for simplification purposes. However, it must be kept in mind that to have an accurate description of what happens at high temperature, these effects must imperatively be taken into account in the calculation of the formation free energy as shown by the recent theoretical works [20,21]. Stress effects must therefore be added to these effects. But this is out of the scope of this paper.

### 2.3. Atomic jumps
To study migration processes, CLIMB-NEB simulations [22] were conducted on 2 × 2 × 2 super-cells, containing 32 atoms. The energy of the transition state was calculated using 600 eV and 12 × 12 × 12 $\mathbf{k}$-meshes to sample the first-Brillouin zone. The migration enthalpy was taken as the enthalpy difference between the transition-state and the initial configuration. The phonon contributions to the Gibbs energy were computed for the initial states (is) and the transition states (ts) to compute jump rates. The phonopy package was then used [23] to compute inter-atomic forces.

The elementary mechanism of an atomic jump occurs at a frequency $\Gamma$ expressed by [24,25]:

$$
\Gamma[\boldsymbol{\sigma}, T]=\frac{k_{\mathrm{B}} T}{h} \frac{\mathcal{Z}_{\mathrm{ts}}}{\mathcal{Z}_{\mathrm{is}}} \exp \left[-\frac{H^{\mathrm{m}}[\boldsymbol{\sigma}]}{k_{\mathrm{B}} T}\right]. \tag{8}
$$

In this equation, $H^{\mathrm{m}}[\boldsymbol{\sigma}]$ is the migration enthalpy of the jump, i.e. the enthalpy difference between the transition state and the initial state. It is expressed as:

$$
H^{\mathrm{m}}[\boldsymbol{\sigma}]=U^{\mathrm{m}}[\boldsymbol{\sigma}]-V \sigma_{i j} \epsilon_{i j}^{\mathrm{m}} \tag{9}
$$

where $U^{\mathrm{m}}=U^{f}(\mathrm{ts})-U^{f}(\mathrm{is})$ is the migration energy and $\boldsymbol{\epsilon}^{\mathrm{m}}=\boldsymbol{\epsilon}(\mathrm{ts})-\boldsymbol{\epsilon}(\mathrm{is})$ is the strain of migration. $\mathcal{Z}$ is the partition function linked to the Gibbs free energy of vibration through:

$$
G_{\mathrm{vib}}=-k_{\mathrm{B}} T \ln \mathcal{Z}. \tag{10}
$$

The rest of the study considers that the ratio $\mathcal{Z}_{\mathrm{TS}} / \mathcal{Z}_{\mathrm{IS}}$ depends little on the loading.

## 3. Linear elasticity approach
Equations presented below are inspired from the work of Maugis et al. [13] and derive from the linear elasticity theory of point defects [26,27]. The effect of an applied strain or stress can be achieved using two quantities: the elastic dipole tensor of the point defect (vacancy or transition state), $\mathcal{P}$, and the rank-4 stiffness tensor of the lattice, $\mathbf{C}$. They were both computed using DFT calculations, as detailed in Section 4.

When a stress $\boldsymbol{\sigma}$ is applied to a crystal of volume $V$ containing a point defect, the resulting uniform strain of the relaxed crystal is, with reference to the stress-free defect-free crystal:

$$
\epsilon_{i j}=S_{i j k l}\left(\sigma_{k l}+\frac{\mathcal{P}_{k l}}{V}\right) \tag{11}
$$

where $\mathbf{S}=\mathbf{C}^{-1}$ is the compliance tensor. In this equation, $S_{i j k l} \sigma_{k l}$ is the elastic response of the defect-free crystal and $S_{i j k l} \frac{\mathcal{P}_{k l}}{V}$ is the relaxation strain $\epsilon_{i j}^{\text {rel }}$ of the defect. Under an uniform strain $\epsilon_{i j}$, the following quantity needs to be added to the internal energy:

$$
U^{\mathrm{el}}=\frac{1}{2} V \epsilon_{i j} C_{i j k l} \epsilon_{k l}-\mathcal{P}_{k l} \epsilon_{k l}. \tag{12}
$$

The second term in this equation accounts for the defect-strain interaction. By combining Eqs 11 and 12, it can be found that the elastic contribution to the formation energy of the defect equals $-\frac{1}{2 V} \mathcal{P}_{i j} S_{i j k l} \mathcal{P}_{k l}$. This quantity can be viewed as a correction of the formation energy when performing DFT calculations on a supercell of finite volume $V$. Its value does not depend on the applied stress, therefore according to the elasticity theory the following relationship can be established

$$
U^{\mathrm{f}}[\boldsymbol{\sigma}]=U^{\mathrm{f}}[\mathbf{0}]. \tag{13}
$$

This will be verified later in this study.

Consider now the volume of relaxation tensor of the defect $\mathcal{V}_{k l}=\mathcal{P}_{i j} S_{i j k l}$ and the scalar volume of relaxation $V^{\text {rel }}=\operatorname{tr}\left(\mathcal{V}_{k l}\right)$. Using tensor $\mathcal{V}$, the effect of stress on the enthalpy function can be computed, provided the vibrational effects are neglected. For instance, from Eq. 2 the stress-dependent relaxation enthalpy of a vacancy is:

$$
H^{\mathrm{rel}}[\boldsymbol{\sigma}]=U^{\mathrm{f}}-\mathcal{V}_{k l} \sigma_{k l}. \tag{14}
$$

It can be noticed that the stress-free enthalpy $H^{\text {rel }}[\mathbf{0}]$ corresponds to the formation energy $U^{\mathrm{f}}$. Eq. 14 defines the change in relaxation enthalpy resulting from the applied stress:

$$
\Delta H^{\mathrm{rel}}=-\mathcal{V}_{k l} \sigma_{k l}. \tag{15}
$$

Similarly the change in formation enthalpy of a vacancy is

$$
\Delta H^{\mathrm{f}}=-\mathcal{V}_{k l} \sigma_{k l}+p V_{a t}. \tag{16}
$$

Using Eq. 7 the effect of stress on the equilibrium site fraction of vacancies is given by:

$$
C_{\mathrm{V}}[\boldsymbol{\sigma}, T]=C_{\mathrm{V}}[\mathbf{0}, T] \exp \left[-\frac{\Delta H^{\mathrm{f}}[\boldsymbol{\sigma}]}{k_{\mathrm{B}} T}\right]. \tag{17}
$$

Regarding atomic jumps, similarly to the above mentioned reasoning, the migration energy is stress-independent:

$$
U^{\mathrm{m}}[\boldsymbol{\sigma}]=U^{\mathrm{m}}[\mathbf{0}], \tag{18}
$$

and the migration enthalpy is affected by the applied stress according to:

$$
\Delta H^{\mathrm{m}}=-\Delta \mathcal{V}_{k l} \sigma_{k l} \tag{19}
$$

where $\Delta \mathcal{V}_{k l}=\Delta \mathcal{P}_{i j} S_{i j k l}$ is the migration volume tensor. We introduced the difference in elastic dipole between the transition state, $\mathcal{P}^{\text {ts }}$, and the stable state, $\mathcal{P}^{\text {vac }}: \Delta \mathcal{P}_{i j}=\mathcal{P}_{i j}^{\text {ts }}-\mathcal{P}_{i j}^{\text {vac }}$. If the transition state had an isotropic symmetry, the migration volume tensor $\Delta \mathcal{V}_{k l}$ would be reduced to the scalar tensor $\frac{1}{3} V^{\mathrm{m}} \mathcal{I}$, where $V^{\mathrm{m}}=\operatorname{tr}\left(\Delta \mathcal{V}_{k l}\right)$ is the volume of migration. This is not the case here, as will be shown in what follows. The effect of stress on jump frequency is given by

$$
\Gamma[\boldsymbol{\sigma}, T]=\Gamma[\mathbf{0}, T] \exp \left[-\frac{\Delta H^{\mathrm{m}}[\boldsymbol{\sigma}]}{k_{\mathrm{B}} T}\right]. \tag{20}
$$

## 4. Preliminary results
### 4.1. Ground state properties of fcc systems
As seen above, different parameters are required to use the elasticity theory, in particular the elastic constants and lattice parameters of the perfect crystal. They were computed from the primitive cells (for elastic constants the linear response was employed using VASP). Results are summarized in Table 1 and compared to the literature.

<table><caption>Table 1 Comparison between theoretical/experimental data of lattice parameters $a_0$, in Å, and elastic constants $C_{ij}$, in GPa, for Al, Cu, Ni and Pd systems. The bulk modulus, $B=(C_{11}+2C_{12})/3$, and shear modulus, $C'=(C_{11}-C_{12})/2$, are also given.</caption>
<thead>
  <tr>
    <th></th>
    <th>$a_0$</th>
    <th>$C_{11}$</th>
    <th>$C_{44}$</th>
    <th>$C_{12}$</th>
    <th>$C'$</th>
    <th>$B$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Al</td>
    <td>4.04/4.05 [28]</td>
    <td>105/116 [28]</td>
    <td>33/31 [28]</td>
    <td>65/65 [28]</td>
    <td>22/26</td>
    <td>78/82 [28]</td>
  </tr>
  <tr>
    <td>Cu</td>
    <td>3.62/3.61 [28]</td>
    <td>193/168-173 [29,30]</td>
    <td>85/61-76 [29,30]</td>
    <td>134/118-129 [29,30]</td>
    <td>29/24 [29,30]</td>
    <td>154/138 [28]</td>
  </tr>
  <tr>
    <td>Ni</td>
    <td>3.52/3.52 [28]</td>
    <td>272/253 [31]</td>
    <td>125/122 [31]</td>
    <td>158/158 [31]</td>
    <td>57/47 [31]</td>
    <td>196/189 [31]</td>
  </tr>
  <tr>
    <td>Pd</td>
    <td>3.94/3.87 [32]</td>
    <td>202/234 [32]</td>
    <td>60/71 [32]</td>
    <td>153/176 [32]</td>
    <td>25/29 [32]</td>
    <td>169/181 [28]</td>
  </tr>
</tbody>
</table>

<table><caption>Table 2 Stress-free crystal: vacancy formation energy ($U^{\text{f}}$), migration energy in first- and second-nearest neighboring position (labeled $U_{1mn}^{\text{m}}$ and $U_{2mn}^{\text{m}}$), in eV; formation and migration vibration enthalpies ($H_{vib}^{\text{f}}$ and $H_{vib}^{\text{m}}$), in meV. For the 54-atoms case, the rhombohedric representation was used.</caption>
<thead>
  <tr>
    <th>nb</th>
    <th>super-cell</th>
    <th>$\mathbf{k}$-mesh</th>
    <th>$U^{\text{f}}$</th>
    <th>$U_{1mn}^{\text{m}}$</th>
    <th>$U_{2mn}^{\text{m}}$</th>
    <th>$H_{vib}^{\text{f}}$</th>
    <th>$H_{vib}^{\text{m}}$</th>
  </tr>
  <tr>
    <th>atoms</th>
    <th>size</th>
    <th></th>
    <th></th>
    <th></th>
    <th></th>
    <th></th>
    <th></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>32</td>
    <td>2 $\times$ 2 $\times$ 2</td>
    <td>12 $\times$ 12 $\times$ 12</td>
    <td>0.628</td>
    <td>0.570</td>
    <td>2.325</td>
    <td>-8</td>
    <td>-26</td>
  </tr>
  <tr>
    <td>54</td>
    <td>3 $\times$ 3 $\times$ 2</td>
    <td>10 $\times$ 10 $\times$ 15</td>
    <td>0.660</td>
    <td>0.549</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
  </tr>
  <tr>
    <td>108</td>
    <td>3 $\times$ 3 $\times$ 3</td>
    <td>10 $\times$ 10 $\times$ 10</td>
    <td>0.639</td>
    <td>0.595</td>
    <td>2.389</td>
    <td>-2</td>
    <td>-</td>
  </tr>
  <tr>
    <td>216</td>
    <td>6 $\times$ 6 $\times$ 6</td>
    <td>8 $\times$ 8 $\times$ 8</td>
    <td>0.636</td>
    <td>0.607</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
  </tr>
</tbody>
</table>

DFT results (lattice parameters, elastic constants) of all four fcc systems studied are found in excellent agreement with experimental and theoretical literature [28–30,32]. In the case of palladium, Amin-Ahmadi et al. [33] already showed that the ground state of fcc-Pd is magnetic, in contradiction with experimental findings. For that reason, it was decided to consider Pd as non-magnetic for further calculations. Further discussions will be based on the DFT values found in this study.

### 4.2. Vacancy characteristics
The Al system is considered representative enough to be focused on. The following section summarizes the additional parameters used in the elastic model, i.e. vacancy formation energy, migration energy, etc. As the Al system will be stressed, it is important to be sure that the common description of diffusion parameters will be precise enough to describe the ground state properties of the vacancy.

The size effect of the super-cell was first considered. Tests were therefore conducted. DFT results, formation and migration energies, for three sizes of super-cells are given in Table 2. It can be noted that, at this stage of approximation, the effect of the supercell size on the relaxation energy is small, within a range of 10 meV. The use of small super-cells was considered to be accurate enough. The vacancy formation energy is equal to about 0.64 eV, in agreement with earlier works [20,34,35]. This value corresponds to the low temperature value of the vacancy formation energy, as already explained, an-harmonic effects are always neglected here, see Glensk et al. [20].

To describe diffusion at the atomic scale, it was considered that the vacancy jumps to its first-nearest neighboring Al atom: with a jump rate $\Gamma_{12}$, as depicted in Fig. 1.

The macroscopic diffusion coefficient $D$ of the vacancy is therefore given in terms of elementary parameters: lattice parameter, $a$, and frequency, $\Gamma_{12}$. Both depend on stress (for instance $p$) and temperature ($T$). As a function of $p$ and $T$ (in this case, the stress does not change the symmetry of the system), $D$ is thus given by:

$$
D[p, T]=a^{2}[p, T] \Gamma_{12}[p, T]. \qquad (21)
$$

In addition to the usual jump, $\Gamma_{12}$, the jumps towards the second-nearest Al neighbor, labeled $\Gamma_{2nn}$, were also considered. Equation of diffusion 21 should thus be modified into (for simplification purposes, $p$ and $T$ were omitted):

$$
D=a^{2}\left(\Gamma_{12}+\Gamma_{2 n n}\right). \qquad (22)
$$

The effect of super-cell size on migration energies (to $1nn$ and $2nn$ sites) was studied. At ambient pressure (i.e. $p=0$ GPa), NEB calculations were done for both trajectories. Results are summarized in Table 2. In both jumps, the trajectory is direct and the transition state is located in the middle of the path (as in all fcc systems). Results also show that the migration energy towards the $2nn$ positions, about 2.3 eV, is significantly higher than for the direct jump, 0.6 eV. From a probability standpoint, $\Gamma_{2nn}$ is much smaller than $\Gamma_{12}$ and can be neglected in first approximation, even under stress. In what follows, only first-nearest neighboring jumps were therefore considered.

Results for the $1nn$ jump are found in excellent agreement with experimental and theoretical findings. Mantina et al. [34] (and references therein) for instance obtained a value of 0.6 eV. In Appendix A, the vacancy concentration and diffusivity were plotted using DFT values.

Data (formation and migration energies) for Ni [36,37], Cu [20] and Pd [38,39], Table 3, are found in excellent agreement with theoretical literature. In the case of Ni and Cu [40], the agreement with the experimental data is rather good, but not for Pd. For palladium, the experimental values of vacancy formation energy measured at high temperature is at least 0.5 eV higher than ours (calculated at 0K) [41,42]. This difference can be explained as in the case of aluminum. The anharmonic effects at high temperature should have a strong impact and thus modify the values of the high temperature formation energies. Consequently, the rest of the study considers that vacancy characteristics resulting from DFT results will be considered accurate enough to capture the effect of stress.

### 4.3. Elastic dipoles
In order to complete the basic properties, elastic dipole tensors, $\mathcal{P}$, were computed. To do so, first the perfect system (without defect) was optimized and then one vacancy was introduced. Atomic forces were thus minimized without relaxing the shape and volume of the cell. The residual stress tensor, $\sigma^{res}$, was used to compute $\mathcal{P}$, as described by Varvenne [10]. Large super-cells were used, i.e. up to 216 atoms, see Table 3. As explained above, two tensors are needed: one for the stable state of the vacancy, and another for the transition state. The dipole tensor of the Al vacancy in the conventional cubic frame, is written as (in eV):

$$
\mathcal{P}^{\mathrm{vac}}=\left[\begin{array}{ccc}
-2.62 & 0 & 0 \\
0 & -2.62 & 0 \\
0 & 0 & -2.62
\end{array}\right]=-2.62 \mathcal{I}, \qquad (23)
$$

![](./images/812564355441754112_4.jpg)

Fig. 1. From left to right: detail of atomic jumps for hydrostatic ($p$), [001] ($\sigma_{zz}$) and [111] ($\sigma_{111}$) uni-axial stresses, and for shear stress in plane [010] ($\sigma_{xy}$). Letters on figures correspond to length of boxes.

Table 3
DFT values according to the super-cell size: elastic dipole tensor $\mathcal{P}$ (in eV), image interaction energy $E_{\text{d}}$ (meV), volume of relaxation $V^{\text{rel}}$ (in $\mathring{\text{A}}^{3}$), migration energy, $U^{\text{m}}$ in eV, formation energy $U^{\text{f}}$ (in eV) and vibration energy $U_{\text{vib}}^{\text{f}}$ (in meV). Values from the elasticity theory: volume tensor of relaxation $\mathcal{V}$ and volume of relaxation $V^{\text{rel}}$ (in $\mathring{\text{A}}^{3}$). In the case of the Al system, a $6 \times 6 \times 6$ super-cell generated from the primitive cell, labeled $^{p}$, was also used. $\mathcal{I}$ is the identity matrix.

<table>
<thead>
<tr>
<th></th>
<th></th>
<th>super-cell size</th>
<th>$\mathcal{P}$ (DFT)</th>
<th>$\mathcal{V}$ (elast.)</th>
<th>$E_{\text{d}}$</th>
<th>$V^{\text{rel}}$ (DFT/elast.)</th>
<th>$U^{\text{f}}$</th>
<th>$U_{\text{vib}}^{\text{f}}$</th>
<th>$U^{\text{m}}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>Al</td>
<td>vac</td>
<td>$2 \times 2 \times 2$</td>
<td>$-2.31 \ \mathcal{I}$</td>
<td>$-1.57 \ \mathcal{I}$</td>
<td>6</td>
<td>-5.01/-4.71</td>
<td>0.642</td>
<td>-8</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>$3 \times 3 \times 3$</td>
<td>$-2.52 \ \mathcal{I}$</td>
<td>$-1.72 \ \mathcal{I}$</td>
<td>2</td>
<td>-5.17/-5.15</td>
<td>0.639</td>
<td>-2</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>$6 \times 6 \times 6^{p}$</td>
<td>$-2.62 \ \mathcal{I}$</td>
<td>$-1.79 \ \mathcal{I}$</td>
<td>1</td>
<td>-5.82/-5.36</td>
<td>0.636</td>
<td>-</td>
<td></td>
</tr>
<tr>
<td></td>
<td>ts</td>
<td>$2 \times 2 \times 2$</td>
<td>$\begin{pmatrix} -1.72 & -0.38 & 0.00 \\ -0.38 & -1.72 & 0.00 \\ 0.00 & 0.00 & 1.42 \end{pmatrix}$</td>
<td>$\begin{pmatrix} -4.66 & -0.92 & 0.00 \\ -0.92 & -4.66 & 0.00 \\ 0.00 & 0.00 & 7.94 \end{pmatrix}$</td>
<td>19</td>
<td>-1.78/-1.38</td>
<td>1.212</td>
<td>-26</td>
<td>0.570</td>
</tr>
<tr>
<td></td>
<td></td>
<td>$3 \times 3 \times 3$</td>
<td>$\begin{pmatrix} -2.12 & -0.19 & 0.00 \\ -0.19 & -2.12 & 0.00 \\ 0.00 & 0.00 & 1.89 \end{pmatrix}$</td>
<td>$\begin{pmatrix} -5.89 & -0.47 & 0.00 \\ -0.47 & -5.89 & 0.00 \\ 0.00 & 0.00 & 10.18 \end{pmatrix}$</td>
<td>9</td>
<td>-1.56/-1.60</td>
<td>1.234</td>
<td>-</td>
<td>0.595</td>
</tr>
<tr>
<td></td>
<td></td>
<td>$6 \times 6 \times 6^{p}$</td>
<td>$\begin{pmatrix} -2.29 & -0.21 & 0.00 \\ -0.21 & -2.29 & 0.00 \\ 0.00 & 0.00 & 1.62 \end{pmatrix}$</td>
<td>$\begin{pmatrix} -5.89 & -0.50 & 0.00 \\ -0.50 & -5.89 & 0.00 \\ 0.00 & 0.00 & 9.77 \end{pmatrix}$</td>
<td>2</td>
<td>-2.62/-2.02</td>
<td>1.243</td>
<td>-</td>
<td>0.607</td>
</tr>
<tr>
<td>Cu</td>
<td>vac</td>
<td>$2 \times 2 \times 2$</td>
<td>$-3.59 \ \mathcal{I}$</td>
<td>$-1.25 \ \mathcal{I}$</td>
<td>12</td>
<td>-3.87/-3.74</td>
<td>1.065</td>
<td>-8</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>$3 \times 3 \times 3$</td>
<td>$-3.68 \ \mathcal{I}$</td>
<td>$-1.28 \ \mathcal{I}$</td>
<td>4</td>
<td>-3.53/-3.84</td>
<td>1.039</td>
<td>-</td>
<td></td>
</tr>
<tr>
<td></td>
<td>ts</td>
<td>$2 \times 2 \times 2$</td>
<td>$\begin{pmatrix} -3.69 & -0.80 & 0.00 \\ -0.80 & -3.69 & 0.00 \\ 0.00 & 0.00 & 1.45 \end{pmatrix}$</td>
<td>$\begin{pmatrix} -5.34 & -0.76 & 0.00 \\ -0.76 & -5.34 & 0.00 \\ 0.00 & 0.00 & 8.62 \end{pmatrix}$</td>
<td>12</td>
<td>-2.62/-2.07</td>
<td>1.753</td>
<td>-19</td>
<td>0.688</td>
</tr>
<tr>
<td></td>
<td></td>
<td>$3 \times 3 \times 3$</td>
<td>$\begin{pmatrix} -4.09 & -0.44 & 0.00 \\ -0.44 & -4.09 & 0.00 \\ 0.00 & 0.00 & 1.49 \end{pmatrix}$</td>
<td>$\begin{pmatrix} -5.83 & -0.41 & 0.00 \\ -0.41 & -5.83 & 0.00 \\ 0.00 & 0.00 & 9.33 \end{pmatrix}$</td>
<td>4</td>
<td>-2.54/-2.32</td>
<td>1.779</td>
<td>-</td>
<td>0.740</td>
</tr>
<tr>
<td>Ni</td>
<td>vac</td>
<td>$2 \times 2 \times 2$</td>
<td>$-4.41 \ \mathcal{I}$</td>
<td>$-1.20 \ \mathcal{I}$</td>
<td>12</td>
<td>-3.81/-3.60</td>
<td>1.445</td>
<td>-8</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>$3 \times 3 \times 3$</td>
<td>$-4.67 \ \mathcal{I}$</td>
<td>$-1.27 \ \mathcal{I}$</td>
<td>4</td>
<td>-3.80/-3.88</td>
<td>1.430</td>
<td>-</td>
<td></td>
</tr>
<tr>
<td></td>
<td>ts</td>
<td>$2 \times 2 \times 2$</td>
<td>$\begin{pmatrix} -4.52 & -0.37 & 0.00 \\ -0.37 & -4.52 & 0.00 \\ 0.00 & 0.00 & 1.73 \end{pmatrix}$</td>
<td>$\begin{pmatrix} -3.59 & -0.24 & 0.00 \\ -0.24 & -3.59 & 0.00 \\ 0.00 & 0.00 & 5.19 \end{pmatrix}$</td>
<td>27</td>
<td>-2.35/-1.99</td>
<td>2.478</td>
<td>-19</td>
<td>1.033</td>
</tr>
<tr>
<td></td>
<td></td>
<td>$3 \times 3 \times 3$</td>
<td>$\begin{pmatrix} -5.09 & -0.13 & 0.00 \\ -0.13 & -5.09 & 0.00 \\ 0.00 & 0.00 & 2.59 \end{pmatrix}$</td>
<td>$\begin{pmatrix} -4.29 & -0.85 & 0.00 \\ -0.85 & -4.29 & 0.00 \\ 0.00 & 0.00 & 6.52 \end{pmatrix}$</td>
<td>11</td>
<td>-2.39/2.06</td>
<td>2.487</td>
<td>-</td>
<td>1.057</td>
</tr>
<tr>
<td>Pd</td>
<td>vac</td>
<td>$2 \times 2 \times 2$</td>
<td>$-5.79 \ \mathcal{I}$</td>
<td>$-1.83 \ \mathcal{I}$</td>
<td>23</td>
<td>-5.82/-5.48</td>
<td>1.176</td>
<td>-3</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>$3 \times 3 \times 3$</td>
<td>$-5.98 \ \mathcal{I}$</td>
<td>$-1.88 \ \mathcal{I}$</td>
<td>7</td>
<td>-6.35/-5.66</td>
<td>1.155</td>
<td>-</td>
<td></td>
</tr>
<tr>
<td></td>
<td>ts</td>
<td>$2 \times 2 \times 2$</td>
<td>$\begin{pmatrix} -5.14 & -0.32 & 0.00 \\ -0.32 & -5.14 & 0.00 \\ 0.00 & 0.00 & 1.02 \end{pmatrix}$</td>
<td>$\begin{pmatrix} -7.70 & -1.37 & 0.00 \\ -2.37 & -7.70 & 0.00 \\ 0.00 & 0.00 & 12.48 \end{pmatrix}$</td>
<td>10</td>
<td>-3.88/-2.91</td>
<td>2.031</td>
<td>-27</td>
<td>0.855</td>
</tr>
<tr>
<td></td>
<td></td>
<td>$3 \times 3 \times 3$</td>
<td>$\begin{pmatrix} -5.56 & -0.46 & 0.00 \\ -0.46 & -5.56 & 0.00 \\ 0.00 & 0.00 & 0.55 \end{pmatrix}$</td>
<td>$\begin{pmatrix} -7.77 & -0.62 & 0.00 \\ -0.62 & -7.77 & 0.00 \\ 0.00 & 0.00 & 12.21 \end{pmatrix}$</td>
<td>8</td>
<td>-3.92/-3.33</td>
<td>2.027</td>
<td>-</td>
<td>0.872</td>
</tr>
</tbody>
</table>

where $\mathcal{I}$ is the identity matrix. For the transition state, calculated for a jump in the [110] direction, results give:

$$
\mathcal{P}^{\text{ts}} = \begin{bmatrix} -2.29 & -0.21 & 0 \\ -0.21 & -2.29 & 0 \\ 0 & 0 & 1.62 \end{bmatrix}. \tag{24}
$$

As expected from the crystal symmetry, the dipole tensor of the vacancy, Eq. 23, has an isotropic symmetry. Conversely, the dipole tensor of the transition state along direction [110], Eq. 24, exhibits anisotropy: the [001] axis is compressed during the jump, while [010] and [100] axes are under tension. Furthermore, a slight shear stress of $-0.21$ eV occurs in the (001) plane. As a consequence, diffusion under applied stress is expected to be anisotropic.

The dipole tensor of migration along direction [110] is obtained from Eqs. 23 and 24:

$$
\Delta \mathcal{P} = \begin{bmatrix} 0.33 & -0.21 & 0 \\ -0.21 & 0.33 & 0 \\ 0 & 0 & 4.24 \end{bmatrix}, \tag{25}
$$

<table><thead><tr><th colspan="5">Table 4 Parameters for the vacancy diffusivity.</th></tr><tr><th></th><th>Al</th><th>Cu</th><th>Ni</th><th>Pd</th></tr></thead><tbody><tr><td>$U^f$ [eV]</td><td>0.636</td><td>1.039</td><td>1.430</td><td>1.155</td></tr><tr><td>$U^m$ [eV]</td><td>0.607</td><td>0.740</td><td>1.057</td><td>0.872</td></tr><tr><td>$S^f$ [J/K/mol]</td><td>9.77</td><td>11.44</td><td>8.00</td><td>4.84</td></tr><tr><td>$D_0$ ($10^{-6}$) [m²/s]</td><td>4.12</td><td>1.40</td><td>2.68</td><td>3.97</td></tr></tbody></table>

from which the volume tensor of migration can be derived (in eV/GPa):

$$
\Delta \mathcal{V} = \begin{bmatrix}
-0.026 & -0.003 & 0 \\
-0.003 & -0.026 & 0 \\
0 & 0 & 0.072
\end{bmatrix},
\tag{26}
$$

or, as a function of the atomic volume $V_{at}$:

$$
\Delta \mathcal{V} = \begin{bmatrix}
-0.25 & -0.03 & 0 \\
-0.03 & -0.25 & 0 \\
0 & 0 & 0.70
\end{bmatrix} V_{at},
\tag{27}
$$

with $V_{at} = 16.5$ $\mathring{A}^3$.

From the symmetry of tensor $\Delta \mathcal{V}$, it can be seen that the migration energies are sensitive not only to the applied pressure and normal stresses, but also to the shear components in the reference frame of the crystal.

As was done for Al, elastic tensors were calculated for Cu, Ni and Pd metals, see Table 3.

This Table also reports the volume of relaxation ($V^{\text{rel}}$) when a vacancy is inserted in the system: the first quantity corresponds to the DFT value, while the second was computed from the relaxation volume tensor. Results show that both quantities are close: the elasticity theory captures with a good accuracy the relaxation volume of the vacancy in the systems studied here. The interaction energy with vacancy periodic images (calculations done at constant volume, $E_d$) is always low, about 10 meV, in agreement with the fact that volume and pressure constant calculations provide equivalent results from 108 atoms.

The formation and migration energies computed from the largest super-cells are gathered in Table 4 (first and second lines). DFT results obtained here are in agreement with the literature [40,43,44]. Results also show that $\mathcal{P}$ converge since $3 \times 3 \times 3$ super-cells. The rest of the study therefore considers these values to be accurate enough.

From Al to Pd, the elastic tensor of the vacancy and its transition state increase. The Ni system, which has the highest elastic constants, exhibits the lowest anisotropy among transition states. Therefore, the effect of anisotropy on diffusion was expected to be small, especially for a non-hydrostatic loading.

From the additional data summarized in Table B.5, it can be concluded that the four fcc metals of the study exhibit a lattice contraction of about 1/3 of the atomic volume when an atom is removed ($V^{\text{rel}} \simeq -\frac{1}{3}V_{at}$). Hence, the gap formation volume is always almost equal to $V^f \simeq \frac{2}{3}V_{at}$.

The effect of different stresses on the formation and migration energies can now be investigated in detail.

### 5. Hydrostatic stress

The effect of hydrostatic stress on the solubility and diffusion of vacancies is the first point investigated. From an experimental standpoint, the range of hydrostatic stress has no limit. The maximal pressure is only limited by phase transitions. Under compression (resp. tension) a decrease (resp. increase) in diffusivity is expected. For this purpose, the different quantities introduced in Section 3, i.e. internal energies, enthalpies of vibration and migration, and jump rates, were calculated using DFT on a set of stresses for aluminum only. For the system with and without vacancy, the volume and energy were calculated as a function of stress. DFT

![](./images/812564355441754112_5.jpg)

Fig. 2. Formation and migration energies (top) and enthalpies (middle) in aluminum as a function of pressure, under hydrostatic loading. Bottom: lattice parameter of bulk aluminum as function of pressure. Continuous lines: DFT; dashed lines: elasticity theory.

results were computed to generate a polynomial curve fit. From these fits, the evolution of lattice parameter, energy and enthalpy were deduced as a function of pressure using Eq. 7 (neglecting the effect of temperature on internal energy). $G^f[p]$ was then computed using these polynomials. Results are depicted in Fig. 2.

The formation and migration energies computed by DFT are found almost pressure-independent, except at higher pressures, as can be seen in Fig. 2 top. Yet even at high pressure, $> 4$ GPa, the elasticity theory deviates only a little from DFT results. One way to correct this would be to evaluate the effect of stress on elastic tensors, but this is beyond the scope of this study. This

stress-independence was expected from the linear elasticity theory Eqs. 13 and (18). The slightly positive curvature of the lattice parameter is explained by the deviation from linearity, Fig. 2 bottom. In this graph, $a_{mod}$ refers to the lattice parameter computed from the elasticity theory (Eq. 11):

$$
a[p]=a_{o}\left[1-\frac{p}{3 B}\right] \tag{28}
$$

where $B$ is the bulk modulus. To evaluate the effect of vacancy concentration on lattice parameters, $+a_{o} C_{v} P_{11}^{\text{vac}} / 3 B V_{at}$ must be added (this correction is always the same in the uni-axial and bi-axial cases)

When the applied stress is hydrostatic, the equations of elasticity can be simplified as follows, to account for the effect of pressure on the enthalpies. The formation of a vacancy is accompanied by a volume increase of the crystal, $+V_{at}$, and a volume decrease due to the atomic relaxation around the vacancy, $+V^{\text{rel}}$. Hence, the total volume change during the formation of a vacancy is $V^{\mathrm{f}}=V_{a t}+V^{\text {rel }}$. From the elasticity theory $V^{\text {rel }}=\operatorname{tr}(\mathcal{V})$. Calculations give $V^{\text {rel }}=-0.35 V_{a t}$, resulting in a volume of formation $V^{\mathrm{f}}=0.65 V_{a t}$. Then, according to Eq. 16, the variation $\Delta H^{\mathrm{f}}$ in formation enthalpy due to the applied pressure is a linear function of pressure $p$ ( $p$ in GPa):

$$
\Delta H^{\mathrm{f}}[p]=p V^{\mathrm{f}}=0.067 p. \tag{29}
$$

Similarly, applying Eq. 19 to the case of hydrostatic pressure, with $V^{\mathrm{m}}=0.20 V_{a t}$, yields the change in migration enthalpy due to the applied pressure:

$$
\Delta H^{\mathrm{m}}[p]=p V^{\mathrm{m}}=0.020 p. \tag{30}
$$

As can be seen, the elasticity theory predicts that both enthalpies should increase as the applied pressure increases.

Concerning DFT results found, the formation enthalpy evolution is in agreement with the results of Iyer et al. [45]. The evolution of $H^{\mathrm{f}}$ is similar. However, quantitatively, since they used the Perdew-Zunger functional (PZ81-LDA [46]), their energies are higher than those of this study. The formation energy decreases rapidly to reach a value of 0eV for a pressure of 7.5GPa. To deepen to the work of Iyer, the effect of loading on migration enthalpy was investigated. Results show the same trend as for the formation enthalpy, as can be seen in Fig. 2. The height of the barrier decreases with pressure, but the slope is smaller than from the formation energy.

When comparing DFT calculations and elasticity theory, it is clear that the elasticity theory accurately reproduces DFT calculations of both migration and formation enthalpies. This is due to the fact that the main effect on enthalpy is included in the pressure term, Eqs. 29 and 30, as illustrated in Fig. 2 top that shows the plot of the DFT internal energy $U^{\mathrm{f}}$ only.

From this, a conclusion can be drawn concerning the effect of hydrostatic pressure on vacancies. All contributions yield the same effect: when the pressure applied to the system increases, the solubility decreases ( $H^{\mathrm{f}}$ increases) and the vacancy diffusivity decreases ( $H^{\mathrm{m}}$ increases). This behavior is consistent with experimental results on most metals [47]. In addition, the good agreement between the elasticity model and DFT calculations, even at high pressures, is noteworthy. The result obtained is consistent with the idea that as the system expands ( $p<0$ ), vacancies form and diffuse easier. The increase of lattice parameter induces an increase of atomic distances which facilitates the formation of vacancies and reduces energy barriers.

The last effect studied is that of pressure on vibrational enthalpy. Until now, all vibrational aspects were neglected for simplification purposes, nevertheless, the present DFT calculations are able to capture their effect, which is not yet the case of the elasticity theory. As was done for the internal energy, $G_{v i b}$ of the vacancy and of the transition state were computed for different temperatures. Results on the formation and migration vibrational enthalpies are depicted in Fig. 3.

![](./images/812564355441754112_6.jpg)

Fig. 3. Vibrational formation and migration enthalpies in aluminum as a function of hydrostatic pressure for different temperature.

Results show that the effect of an hydrostatic loading is still negligible on the vacancy formation enthalpy and low on the transition state (a few meV). The main effect remains the $p V$ contribution. Since the pressure range of hydrostatic stress is the largest, the effect of loading on the vibrational enthalpy will be neglected in the rest of the study.

Equilibrium concentrations and diffusion coefficients of the vacancy can now be plotted for all fcc systems considered, see Figs. 4 and 5, respectively. Results are plotted using the parameters summarized in Table B.6 in Appendix B.

Regardless of the metal under tension (resp. compression), the concentration and diffusivity of vacancies increase (resp. decrease). The effect is more pronounced in Al than in other metals. This is a consequence of Aluminum's relatively low elastic stiffness. For all metals, the highest main effect of pressure is observed at low and intermediate temperatures. The increase (in concentration and diffusivity) can reach several orders of magnitude at room temperature, but only when the pressure is high. For a stress equal to $\pm 1 \mathrm{GPa}$, the change in vacancy concentration is about one order of magnitude only. The enhancement on diffusivity is only of one order of magnitude, in the range where the model is numerically accurate. The main notable effect of pressure is the increase in vacancy concentration, in the case of metals with low elastic stiffness.

To conclude, the elasticity theory can capture the physics, but the behavior of the different materials presented here is little influenced by the hydrostatic loading.

## 6. Uni-axial/bi-axial stress

### 6.1. Formalism

The case of uni-axial and bi-axial stresses along the main crystallographic directions can be treated using the same framework. In the case of a uni-axial (along, for example, the [001] direction) or a bi-axial stress (applying an equivalent loading along, for example the [100] and the [010] directions), the cubic structure evolves into a tetragonal structure, where two directions are equivalent. The initial space group No225 ( $F d \overline{3} m$ ) changes into space group No139 (I4/mmm) for the perfect stressed structure. The atoms in the lattice are still equivalent, thus there is one type of vacancy. Eq. 7, which gives the vacancy concentration $C_{v}$, is still applicable in the present case. In such a configuration however, the degeneracy of the jump rates is lifted. Two distinct jump rates, $\Gamma_{12}$ and $\Gamma_{13}$,

![](./images/812564355441754112_7.jpg)

Fig. 4. Vacancy concentration as function of T in Al, Cu, Ni and Pd systems under different hydrostatic loadings in the range of -8 to +8GPa.

describe the whole migration process: the first one is in the square plane (labeled 12) and the second one is along the third direction (13 along z for the uni-axial stress), as displayed in Fig. 1, b). There is a symmetry break in the vacancy diffusion coefficient along the crystallographic direction. The diffusion coefficients in the plane, $D_{x,y}$, and along the z direction, $D_{z}$, are thus given by [48]:

$$
\left\{
\begin{aligned}
D_{x,y}[\sigma_{zz}, T] &= \frac{a^2}{2} \left( \Gamma_{12} + \Gamma_{13} \right) \\
D_{z}[\sigma_{zz}, T] &= c^2 \Gamma_{13}
\end{aligned}
\right.
\tag{31}
$$

In the case of a uni-axial stress, $a = b$ and $c$ are, the perpendicular lattice parameters and the lattice parameter in the direction of the uni-axial loading ($\sigma_{zz}$), respectively. All quantities, i.e. $a$, $c$, $C_V$, $\Gamma_{12}$ and $\Gamma_{13}$, depend on $\sigma_{zz}$ and $T$.

Diffusion coefficients can be approximated, by a Taylor expansion of eq. 31, using the following equations:

$$
\left\{
\begin{aligned}
D_{x,y}[\sigma_{zz}, T] &= \frac{a^2}{2} \Gamma_{12}[0] \left( \exp\left[ \frac{-\Delta H_{12}}{k_B T} \right] + \exp\left[ \frac{-\Delta H_{13}}{k_B T} \right] \right) \\
D_{z}[\sigma_{zz}, T] &= c^2 \Gamma_{12}[0] \exp\left[ \frac{-\Delta H_{12}}{k_B T} \right]
\end{aligned}
\right.
\tag{32}
$$

where $\Gamma_{12}[0]$ is the stress-free atomic jump.

Equivalent equations were obtained for a bi-axial stress.

## 6.2. Results
### 6.2.1. Uni-axial stress
In the case of stress along [001], DFT and elasticity theory results are drawn in Fig. 6. As was done for hydrostatic stress, the evolution of the formation energy, migration energies (perpendicular to and along the stress) and lattice parameters ($a = b$ and $c$) are represented. Contrary to hydrostatic stress, the pressures applied in uni-axial and bi-axial loadings are limited; in this study, it was chosen to limit the stress value to $\pm$ 1GPa. The first discussion focuses on the effect of a uni-axial stress.

When the metal is pulled (contracted), the system undergoes a contraction (expansion) in the direction transverse to the stress direction, see Fig. 6. This is well explained by the elasticity theory and rationalized by Poisson's ratio, $\nu$. From the present results, the ratio $\delta c / \delta a \simeq 0.37$ is found in excellent agreement with the theoretical prediction of Poisson's ratio for aluminum, which is approximately equal to 0.34 in DFT (computed from elastic constants) and experimentally. The evolution of lattice parameters can be also rationalized with the following relations:

$$
\left[
\begin{aligned}
a, b &= a_0 \left( 1 - \frac{C_{12}}{6BC'} \sigma_{zz} \right) \\
c &= a_0 \left( 1 + \frac{C_{11}+C_{12}}{6BC'} \sigma_{zz} \right)
\end{aligned}
\right.
\tag{33}
$$

as can be seen in Fig. 6 ($a_0$ is the stress-free lattice parameter and $C'$ the shear modulus).

Concerning the solubility energy, if the internal energy part, $U$, is directly computed by using DFT results, the correction related to the elastic energy leads to:

$$
\begin{aligned}
H &= U - V \epsilon_{zz} \sigma_{zz} \\
&= U[\sigma_{zz}] - V \left[ \frac{c[\sigma_{zz}]-a_0}{a_0} \right] \sigma_{zz}
\end{aligned}
\tag{34}
$$

where $V$ is the volume of the system and $\epsilon_{zz}$ the elongation (contraction) under $\sigma_{zz}$. Eqs. 3 and 4 are then used to compute $H^f$.

The behavior observed is the same as for hydrostatic stress, i.e. a decrease in formation enthalpy when the material is pulled. As

![](./images/812564355441754112_8.jpg)

Fig. 5. Vacancy diffusion coefficients as function of T in Al, Cu, Ni and Pd systems under different hydrostatic loading.

expected, a lifting of degeneracy of the migration energies can be noticed during a tensile or compressive test. An increase in migration energy along (001) and an opposite mechanism (decrease) in the plane [110] is observed.

The energy barriers decrease in the direction perpendicular to the stress, while they increase in all other directions.

From the elasticity theory (Eq. 29) the applied stress modifies the vacancy formation energy via the pressure $p=-\sigma_{zz}/3$, i.e.
$$
\Delta H^{\mathrm{f}}=-0.022 \sigma_{zz}. \tag{35}
$$

According to Eq. 30, the two migration enthalpies are modified as follows:
$$
\left\{
\begin{aligned}
\Delta H_{12}^{\mathrm{m}}&= -0.074\sigma_{zz} \\
\Delta H_{13}^{\mathrm{m}}&= +0.026\sigma_{zz}.
\end{aligned}
\right. \tag{36}
$$

There is an excellent agreement between DFT simulations and the elastic model. Contrary to what was found for hydrostatic loading, the evolution of vacancy concentration under a uni-axial stress is relatively small; the formation energy difference at 1 GPa is below < 0.1eV. The effect of $\sigma_{zz}$ on vacancy concentration is thus low, as can be seen in Fig. 7 top. However, the symmetry break in the diffusion coefficient is, on the contrary, more pronounced.

To clarify, the $D_x/D_z$ ratio for different loadings is plotted in Fig. 7 bottom. For high positive loadings, a small symmetry break and an increase in vacancy diffusivity can be observed. This is why it would be difficult to identify experimentally.

The results obtained on the four metals can now be compared. The slopes of migration and formation enthalpies are gathered in Tables B.5 and B.6. Results show that the effect of stress depends little on the metal species, all slopes are equivalent. Based on aluminum results, it can be deduced that the effect of uni-axial loading is thus small. Vacancy concentration changes little as a function of stress.

### 6.2.2. Bi-axial stress

In the case of a [100]+[010] stress, simulations results are depicted in Fig. 8. Results are very similar to those of a uni-axial loading.

Qualitatively and quantitatively, uni-axial and bi-axial loadings lead overall to the same result. On the other hand, the elasticity theory adequately captures the physics, reproducing DFT results accurately. The evolution of the lattice parameters can be described using the following equations:
$$
\left\{
\begin{aligned}
a,b &= a_{o}\left(1+\frac{C_{11}}{6BC}\sigma_{xx}\right) \\
c &= a_{o}\left(1-\frac{C_{12}}{3BC}\sigma_{xx}\right)
\end{aligned}
\right. \tag{37}
$$

Results using the elasticity theory, with $\sigma_{xx}=\sigma_{yy}$, give:
$$
\Delta H^{\mathrm{f}}=-0.045 \sigma_{xx}. \tag{38}
$$
and
$$
\left\{
\begin{aligned}
\Delta H_{12}^{\mathrm{m}}&= +0.0051\sigma_{xx} \\
\Delta H_{13}^{\mathrm{m}}&= -0.046\sigma_{xx},
\end{aligned}
\right. \tag{39}
$$

With these parameters, DFT results can once more be reproduced with a high degree of accuracy. As in previous cases, it can be deduced from these results that the vacancy (concentration and diffusivity) in fcc metals is little affected by a bi-axial stress. It can also be noted that the values of $\Delta H$ depends little on the metal.

![](./images/812564355441754112_9.jpg)

Fig. 6. Evolution of formation and migration energies as a function of the stress, under a uni-axial stress along [001], $\sigma_{zz}$ (in GPa).

## 7. Along the [111] direction

For the second uni-axial loading, another direction was considered: along [111], perpendicular to the dense plane. The $Fd\overline{3}m$ symmetry thus changes into a rhombohedric structure: space group $R\overline{3}m$, No166. In this representation, all lattice parameters are equal and all angles are also equal but not orthogonal. Two jump rates ($\Gamma_{12}$ and $\Gamma_{13}$) are necessary to describe the atomistic process of diffusion. In the cubic representation of the cell, the two parameters $\Gamma_{12}$ and $\Gamma_{13}$ are displayed in Fig. 1 c). In the rhombohedral cell, see Fig. 1 d), the expression of the diffusion coefficient is thus transformed into:

$$
D[\sigma_{111}, T] = \frac{a_{111}^2}{2} \left( \Gamma_{12} + \Gamma_{13} \right) \tag{40}
$$

$a_{111}$ corresponds to the lattice parameters of the primitive unit-cell, the loading is along the [111] direction. However, for simplification purposes, a [111] loading can also be represented using the hexagonal representation of the unit cell, as displayed Fig. 1 e). The stress is thus along the new z axis and diffusion coefficients can be written as:

$$
\left\{
\begin{aligned}
D_{basal}[\sigma_{zz}, T] &= \frac{2 a_{basal}^2}{3} \left( 3 \Gamma_{13} + \Gamma_{12} \right) \\
D_{z}[\sigma_{zz}, T] &= \frac{c_{h}^2}{3} \Gamma_{12}
\end{aligned}
\right. \tag{41}
$$

where $\Gamma_{13}$ is the jump rate in the new $xy$ (basal) plane, and $\Gamma_{12}$ the one along the axial direction. $a_{basal}$ and $c_{h}$ are the new lattice parameters of the box. This second representation was chosen to perform calculations ($3 \times 3 \times 2$ super-cell, i.e. 54 atoms).

![](./images/812564355441754112_10.jpg)

Fig. 7. Vacancy concentration (top) and ratio of vacancy diffusion coefficients $D_{x}/D_{z}$ (bottom) as a function of $T$ for Al for different values of $\sigma_{zz}$.

As for previous cases, there is only one nonequivalent vacancy, but there are two distinct jumps. Results are depicted in Fig. 9. Here again, the formation energy increases when the metal is pulled.

However, the effect on diffusivity, on anisotropy and the explicit stress dependence, is almost non-existent. DFT results are confirmed by the elasticity theory. The formation enthalpy dependence is:

$$
\Delta H^{\mathrm{f}} = -0.022 \sigma_{111}. \tag{42}
$$

while migration enthalpies can be expressed as:

$$
\left\{
\begin{aligned}
\Delta H_{12}^{\mathrm{m}} &= -0.0048 \sigma_{111}, \\
\Delta H_{13}^{\mathrm{m}} &= -0.0088 \sigma_{111}.
\end{aligned}
\right. \tag{43}
$$

![](./images/812564355441754112_11.jpg)

Fig. 8. Evolution of the formation (top) and migration (middle energies as a func- tion of stress, under a bi-axial stress along [100]+[010]. The evolution of lattice pa- rameters is also plotted (bottom).

![](./images/812564355441754112_12.jpg)

Fig. 9. Evolution of the formation (top) and migration (middle) enthalpies as a function of pressure, under a uni-axial stress along [111], $\sigma_{111}$ (in GPa). The effect on lattice parameters is also represented, bottom.

As can be seen, the effect of a uni-axial loading in the dense plane is negligible, even at 1.5 GPa. All fcc systems considered here show the same trend, see Tables B.6 and B.5.

### 8. Shear stress

Lastly, the effect of pure shear stress $\sigma_{xy}$ in plane (001) is dis- cussed The cubic symmetry is transformed into a monoclinic struc- ture C/2m, No12. There is still only one type of vacancy, but three jump rates are needed to describe the migration process, as shown in Fig. 1. In the xz and yz directions, the lattice remains square, and in the xy it is diamond-shape. The length of the lattice is neverthe- less unchanged, diffusion coefficients are thus expressed as:

$$
\left\{
\begin{aligned}
D_{x,y}[\sigma_{xy}, T] &= \frac{a^2}{4} \left(\Gamma_{13a} + \Gamma_{13b} + 2\Gamma_{12}\right) \\
D_{z}[\sigma_{xy}, T] &= c^2 \Gamma_{12}
\end{aligned}
\right. \tag{44}
$$

From the elasticity theory, a shear stress has no effect on the formation enthalpy of vacancies, since the hydrostatic pressure is null:

$$
\Delta H^{\mathrm{f}} = 0. \tag{45}
$$

However, a small effect on energy barriers is found:

$$
\begin{cases}
\Delta H_{12}^{\mathrm{m}} = 0.0, \\
\Delta H_{13a}^{\mathrm{m}} = +0.0061\sigma_{xy}, \\
\Delta H_{13b}^{\mathrm{m}} = -0.0061\sigma_{xy}.
\end{cases} \tag{46}
$$

Shear stress $\sigma_{xy}$ has no effect on the migration along [011], and opposite effects along [110] and $[1\overline{1}0]$.

## 9. Conclusion

This article presents a full method to study the effect of stress on vacancy formation and diffusivity energies in fcc systems. Elasticity theory was rationalized by using DFT parameters and compared to first-principles calculations. Results show that both approaches lead to equivalent results quantitatively until a few GPa, and qualitatively beyond. The benefit of the elastic approach is that it allows reproducing loading effects using a few parameters for a reduced numerical cost as compared to full DFT calculations. Results also show that the vibrational enthalpy changes little with the loading. Additionally, a vacancy diffusion equation is proposed in the case of fcc distorted systems.

In terms of results, the effect of stress (as well as strain) can strongly modify vacancy concentration and diffusivity, but mainly in the case of hydrostatic loading. For high loads, other physical processes such as dislocations or interfaces, can also change the amount of vacancies and their diffusivity. It was shown that all four metals have a very similar stress behavior. The anisotropy induced by the disruption of symmetry is considered low. To further prove this point, experiments on soft materials should be carried out. The present results can probably be extended to other materials and in particular to bcc and hcp systems.

These results can significantly improve the understanding of physical processes within materials undergoing local or global deformations.

## Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Acknowledgments

This work was performed using HPC resources from CALMIP (Grant 2018 and 2019-p0749) and GENCI-CINES (Grant A0040910368). DC would like to thank CALMIP staff members for their help in using HPC resources.

## Appendix A. Parameters at 0 GPa

Results on the vacancy and tracer diffusivity and the vacancy concentration at ambient pressure are plotted in Fig. A.10.

![](./images/812564355441754112_13.jpg)

Fig. A.10. Vacancy and tracer diffusion coefficients, and vacancy concentration as function of $T$ for Al, Cu, Ni and Pd systems.

tion and migration energies are given in Table 3, vibrational en- thalpy and entropy are included in the calculations.

Based on these results and the vibrational partition functions of the transition and stable states, the vacancy diffusion coeffi- cient $D(T)$ was computed and fit using an Arrhenius function of the following form $D_{0}\exp(-Q/k_{B}T)$. The tracer diffusion coefficients, $f^{*}C_{1v}*D_{1v}$, were also drawn.

The vacancy formation entropy (at high $T$), $S^{f}$, was also calculated. $S^{f}$ is expressed as:

$$
S^{f}=S_{\mathrm{vib}}[(N-1).Al]-\frac{N-1}{N}S_{\mathrm{vib}}[N.Al] \tag{A.1}
$$

where the phonon entropy, $S_{\mathrm{vib}}$, corresponds to the high temperature value (at $0K$, $S_{\mathrm{vib}}=0$).

In fine, diffusion coefficients $(D_{0}$=$3.6\ 10^{-6}\ m^{2}/s$ and $Q$=$1.24$ eV) are in excellent agreement with experimental values, see Mantina [34] for instance for Al. $S^{f}\simeq1.17\ k_{B}$ or $9.8$ J/K/mol, to be compared to the experimental value ranging from $0.7$-$1.1\ k_{B}$ unit [34].

## Appendix B. Results

Results of the elastic model computed using DFT values from Table 3 are summarized in Tables B.5 and B.6. Data are computed DFT calculations with $3\ \times\ 3\ \times\ 3$ super-cell sizes.

<table>
<caption>Table B.5 Atomic volume ($V_{at}$), relaxation volume ($V^{\mathrm{rel}}$) and formation volume ($V^{\mathrm{f}}$) of a vacancy, in $\mathring{A}^{3}$. Changes in formation enthalpy ($\Delta H^{\mathrm{f}}$, in eV) due to an applied stress ($p$ or $\sigma$, in GPa). From DFT calculations with $3\ \times\ 3\ \times\ 3$ super-cell size and elasticity theory of point defects.</caption>
<thead>
<tr>
<th>stress state</th>
<th></th>
<th>Al</th>
<th>Cu</th>
<th>Ni</th>
<th>Pd</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="8">hydrostatic<br>uni-axial [001]<br>bi-axial [100]+[010]<br>uni-axial [111]<br>shear (001)</td>
<td>$V_{at}$</td>
<td>16.5</td>
<td>11.9</td>
<td>10.9</td>
<td>15.3</td>
</tr>
<tr>
<td>$V^{\mathrm{rel}}$</td>
<td>-5.36</td>
<td>-3.84</td>
<td>-3.88</td>
<td>-5.66</td>
</tr>
<tr>
<td>$V^{\mathrm{f}}$</td>
<td>11.1</td>
<td>8.06</td>
<td>7.02</td>
<td>9.64</td>
</tr>
<tr>
<td>$V^{\mathrm{f}}/V_{at}$</td>
<td>0.67</td>
<td>0.68</td>
<td>0.64</td>
<td>0.63</td>
</tr>
<tr>
<td>$\Delta H^{\mathrm{f}}$</td>
<td>$0.067p$</td>
<td>$0.049p$</td>
<td>$0.042p$</td>
<td>$0.058p$</td>
</tr>
<tr>
<td>$\Delta H^{\mathrm{f}}$</td>
<td>$-0.022\sigma_{zz}$</td>
<td>$-0.016\sigma_{zz}$</td>
<td>$-0.014\sigma_{zz}$</td>
<td>$-0.019\sigma_{zz}$</td>
</tr>
<tr>
<td>$\Delta H^{\mathrm{f}}$</td>
<td>$-0.045\sigma_{xx}$</td>
<td>$-0.032\sigma_{xx}$</td>
<td>$-0.028\sigma_{xx}$</td>
<td>$-0.039\sigma_{xx}$</td>
</tr>
<tr>
<td>$\Delta H^{\mathrm{f}}$</td>
<td>$-0.022\sigma_{111}$</td>
<td>$-0.016\sigma_{111}$</td>
<td>$-0.014\sigma_{111}$</td>
<td>$-0.019\sigma_{111}$</td>
</tr>
<tr>
<td></td>
<td>$\Delta H^{\mathrm{f}}$</td>
<td>0.</td>
<td>0.</td>
<td>0.</td>
<td>0.</td>
</tr>
</tbody>
</table>

<table>
<caption>Table B.6 Migration dipole tensor ($\mathcal{\Delta P}$, in eV) and migration volume tensor ($\Delta \mathcal{V}$, in $\mathring{A}^{3}$) for an atom jump in direction [110]. Changes in migration enthalpy ($\Delta H^{m}$, in eV) due to stress ($p$ or $\sigma$, in GPa) for various jumps. From DFT calculations ($3\ \times\ 3\ \times\ 3$ super-cell) and elasticity theory of point defects.</caption>
<thead>
<tr>
<th>stress state</th>
<th></th>
<th>Al</th>
<th>Cu</th>
<th>Ni</th>
<th>Pd</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="16">hydrostatic<br>uni-axial [001]<br>bi-axial [100] + [010]<br>uni-axial [111]<br>shear (001)</td>
<td>$\Delta \mathcal{P}$</td>
<td>$\begin{pmatrix}0.33 &amp; -0.21 &amp; 0.00 \\-0.21 &amp; 0.33 &amp; 0.00 \\0.00 &amp; 0.00 &amp; 4.247\end{pmatrix}$</td>
<td>$\begin{pmatrix}-0.41 &amp; -0.44 &amp; 0.00 \\-0.44 &amp; -0.41 &amp; 0.00 \\0.00 &amp; 0.00 &amp; 5.17\end{pmatrix}$</td>
<td>$\begin{pmatrix}-0.42 &amp; -0.13 &amp; 0.00 \\-0.13 &amp; -0.42 &amp; 0.00 \\0.00 &amp; 0.00 &amp; 7.26\end{pmatrix}$</td>
<td>$\begin{pmatrix}0.42 &amp; -0.46 &amp; 0.00 \\-0.46 &amp; 0.42 &amp; 0.00 \\0.00 &amp; 0.00 &amp; 6.53\end{pmatrix}$</td>
</tr>
<tr>
<td>$\Delta \mathcal{V}$</td>
<td>$\begin{pmatrix}-4.12 &amp; -0.49 &amp; 0.00 \\-0.49 &amp; -4.12 &amp; 0.00 \\0.00 &amp; 0.00 &amp; 11.5\end{pmatrix}$</td>
<td>$\begin{pmatrix}-4.55 &amp; -0.41 &amp; 0.00 \\-0.41 &amp; -4.55 &amp; 0.00 \\0.00 &amp; 0.00 &amp; 10.6\end{pmatrix}$</td>
<td>$\begin{pmatrix}-3.01 &amp; -0.083 &amp; 0.00 \\-0.083 &amp; -3.01 &amp; 0.00 \\0.00 &amp; 0.00 &amp; 7.78\end{pmatrix}$</td>
<td>$\begin{pmatrix}-5.88 &amp; -0.61 &amp; 0.00 \\-0.61 &amp; -5.88 &amp; 0.00 \\0.00 &amp; 0.00 &amp; 14.1\end{pmatrix}$</td>
</tr>
<tr>
<td>$\Delta H_{12}$</td>
<td>$0.020p$</td>
<td>$0.0094p$</td>
<td>$0.0101p$</td>
<td>$0.0145p$</td>
</tr>
<tr>
<td>$\Delta H_{12}$</td>
<td>$-0.074\sigma_{zz}$</td>
<td>$-0.0662\sigma_{zz}$</td>
<td>$-0.0486\sigma_{zz}$</td>
<td>$-0.0880\sigma_{zz}$</td>
</tr>
<tr>
<td>$\Delta H_{13}$</td>
<td>$+0.026\sigma_{zz}$</td>
<td>$+0.0284\sigma_{zz}$</td>
<td>$+0.0188\sigma_{zz}$</td>
<td>$+0.0367\sigma_{zz}$</td>
</tr>
<tr>
<td>$\Delta H_{12}$</td>
<td>$+0.0051\sigma_{xx}$</td>
<td>$+0.0568\sigma_{xx}$</td>
<td>$+0.0376\sigma_{xx}$</td>
<td>$+0.0735\sigma_{xx}$</td>
</tr>
<tr>
<td>$\Delta H_{13}$</td>
<td>$-0.046\sigma_{xx}$</td>
<td>$-0.0378\sigma_{xx}$</td>
<td>$-0.0297\sigma_{xx}$</td>
<td>$-0.0512\sigma_{xx}$</td>
</tr>
<tr>
<td>$\Delta H_{13}$</td>
<td>$-0.0088\sigma_{111}$</td>
<td>$-0.0014\sigma_{111}$</td>
<td>$-0.0033\sigma_{111}$</td>
<td>$-0.0023\sigma_{111}$</td>
</tr>
<tr>
<td>$\Delta H_{12}$</td>
<td>$-0.0048\sigma_{111}$</td>
<td>$-0.0049\sigma_{111}$</td>
<td>$-0.0040\sigma_{111}$</td>
<td>$-0.0074\sigma_{111}$</td>
</tr>
<tr>
<td>$\Delta H_{12}$</td>
<td>0.</td>
<td>0.</td>
<td>0.</td>
<td></td>
</tr>
<tr>
<td>$\Delta H_{13a}$</td>
<td>$+0.0061\sigma_{xy}$</td>
<td>$+0.0052\sigma_{xy}$</td>
<td>$+0.0010\sigma_{xy}$</td>
<td>$+0.0077\sigma_{xy}$</td>
</tr>
<tr>
<td>$\Delta H_{13b}$</td>
<td>$-0.0061\sigma_{xy}$</td>
<td>$-0.0052\sigma_{xy}$</td>
<td>$-0.0010\sigma_{xy}$</td>
<td>$-0.0077\sigma_{xy}$</td>
</tr>
</tbody>
</table>

## Appendix C. Tri-axial case

In the case of a tri-axial stress, the fcc system evolves into a Fmmm (No69) orthorhombic structure. Three non-equivalent jumps are used to describe vacancy diffusion: $\Gamma_{12}$, $\Gamma_{13}$ and $\Gamma_{14}$. The convention is the same as the one used in Fig. 1. The diffusion coefficients become:

$$
D_{x}=\frac{a^{2}}{2}\left(\Gamma_{12}+\Gamma_{13}\right) \tag{C.1}
$$

$$
D_{y}=\frac{b^{2}}{2}\left(\Gamma_{12}+\Gamma_{14}\right) \tag{C.2}
$$

$$
D_{z}=\frac{c^{2}}{2}\left(\Gamma_{13}+\Gamma_{14}\right) \tag{C.3}
$$

where $a$, $b$ and $c$ are the deformed axes.

## References

[1] P. Fratzl, O. Penrose, Competing mechanisms for precipitate coarsening in phase separation with vacancy dynamics, Phys. Rev. B 55 (1997) R6101-R6104, doi:10.1103/PhysRevB.55.R6101.

[2] M. Urquidi, Solute-vacancy interaction model and the e ect of minor alloying elements on the initiation of pitting corrosion, Journal of The Electrochemical Society 132 (3) (1985) 555. 10.1149%2F1.113886

[3] S.-J. Lee, J. Kim, S.N. Kane, B.C.D. Cooman, On the origin of dynamic strain aging in twinning-induced plasticity steels, Acta Mater. 59 (17) (2011) 6809-6819, doi:10.1016/j.actamat.2011.07.040.

[4] S.T. Dunham, J.D. Plummer, Point-defect generation during oxidation of silicon in dry oxygen. i. theory, J. Appl. Phys. 59 (7) (1986) 2541-2550, doi:10.1063/1.337003.

[5] G. Lu, E. Kaxiras, Can vacancies lubricate dislocation motion in aluminum? Phys. Rev. Lett. 89 (2002) 105501, doi:10.1103/PhysRevLett.89.105501.

[6] A. Lidiard, Philos. Mag. 46 (1955) 1218.

[7] M.J. Aziz, Thermodynamics of diffusion under pressure and stress: relation to point defect mechanisms, Appl. Phys. Lett. 70 (21) (1997) 2810-2812, doi:10.1063/1.119066.

[8] M.J. Aziz, Y. Zhao, H.-J. Gossmann, S. Mitha, S.P. Smith, D. Schiferl, Pressure and stress effects on the diffusion of b and sb in si and si-ge alloys, Phys. Rev. B 73 (2006) 054101, doi:10.1103/PhysRevB.73.054101.

[9] E. Clouet, S. Garruchet, H. Nguyen, M. Perez, C.S. Becquart, Dislocation interaction with c in alpha-fe: acomparison between atomic simulations and elasticity theory, Acta Mater. 56 (14) (2008) 3450-3460, doi:10.1016/j.actamat.2008.03.024.

[10] C. Varvenne, E. Clouet, Elastic dipoles of point defects from atomistic simulations, Phys. Rev. B 96 (2017) 224103, doi:10.1103/PhysRevB.96.224103.

[11] T.J.E. Clouet, C. Varvenne, Elastic modeling of point-defects and their interaction, Comput. Mater. Sci. 147 (2018) 49-63, doi:10.1016/j.commatsci.2018.01.053.

[12] D.S. Tchitchekova, J. Morthomas, F. Ribeiro, R. Ducher, M. Perez, A novel method for calculating the energy barriers for carbon diffusion in ferrite under heterogeneous stress, J. Chem. Phys. 141 (3) (2014) 034118, doi:10.1063/1.4889854.

[13] P. Maugis, S. Centouf, D. Connétable, Stress-controlled carbon diffusion channeling in bct-iron: a mean-field theory, J. Alloys. Compd. 769 (2018) 1121-1131, doi:10.1016/j.jallcom.2018.08.060.

[14] D.R. Trinkl, Diffusivity and derivatives for interstitial solutes: activation energy, volume, and elastodiffusion tensors, Philos. Mag. 96 (26) (2016) 2714-2735, doi:10.1080/14786435.2016.1212175.

[15] G. Kresse, J. Hafner, Ab initio molecular dynamics for liquid metals, Phys. Rev. B 47 (1993) 558-561, doi:10.1103/PhysRevB.47.558.

[16] W. Kohn, L. Sham, Self-consistent equations including exchange and correlation effect, Physical Review 140 (1965) A1133.

[17] G. Kresse, D. Joubert, From ultrasoft pseudopotentials to the projector augmented-wave method, Phys. Rev. B 59 (1999) 1758-1775, doi:10.1103/PhysRevB.59.1758.

[18] J.P. Perdew, K. Burke, M. Ernzerhof, Generalized gradient approximation made simple, Phys. Rev. Lett. 77 (1996) 3865-3868, doi:10.1103/PhysRevLett.77.3865.

[19] H.J. Monkhorst, J.D. Pack, Special points for brillouin-zone integrations, Phys. Rev. B 13 (1976) 5188-5192, doi:10.1103/PhysRevB.13.5188.

[20] A. Glensk, B. Grabowski, T. Hickel, J. Neugebauer, Breakdown of the arrhenius law in describing vacancy formation energies: the importance of local anharmonicity revealed by ab initio thermodynamics, Phys. Rev. X 4 (2014) 011018, doi:10.1103/PhysRevX.4.011018.

[21] Y. Gong, B. Grabowski, A. Glensk, F. Körmann, J. Neugebauer, R.C. Reed, Temperature dependence of the gibbs energy of vacancy formation of fcc ni, Phys. Rev. B 97 (21) (2018) 214106, doi:10.1103/PhysRevB.97.214106.

[22] G. Henkelman, B.P. Uberuaga, H. Jónsson, A climbing image nudged elastic band method for finding saddle points and minimum energy paths, J. Chem. Phys. 113 (22) (2000) 9901-9904, doi:10.1063/1.1329672.

[23] A. Togo, F. Oba, I. Tanaka, First-principles calculations of the ferroelastic transition between rutile-type and $cacl_2$-type sio₂ at high pressures, Phys. Rev. B 78 (2008) 134106, doi:10.1103/PhysRevB.78.134106.

[24] H. Eyring, The activated complex in chemical reactions, J. Chem. Phys. 3 (2) (1935) 107-115, doi:10.1063/1.1749604.

[25] G.H. Vineyard, Frequency factors and isotope effects in solid state rate processes, J. Phys. Chem. Solids 3 (1) (1957) 121-127, doi:10.1016/0022-3697(57)90059-8.

[26] R.S.D. Bacon, D. Barnett, Anisotropic continuum theory of lattice defects, Prog. Mater. Sci. 23 (1980) 51, doi:10.1016/0079- 6425(80)90007-9.

[27] R. Balluffi, Introduction to elasticity theory for crystal defects, World Scientific Publishing Company, 2016.

[28] C. Kittel, Introduction to solid state physics, Wiley, New York, 1996.

[29] H. Ledbetter, E. Naimon, Elastic properties of metals and alloys. ii, copper, J. Phys.Chem. Ref. Data 3 (1974) 897.

[30] J. Neighbours, C.S. Smith, The elastic constants of copper alloys, Acta Metall. 2 (4) (1954) 591-596, doi:10.1016/0001-6160(54)90193-5.

[31] J.R. Neighbours, F.W. Bratten, C.S. Smith, The elastic constants of nickel, J. Appl. Phys. 23 (4) (1952) 389-393, doi:10.1063/1.1702218.

[32] J.A. Rayne, Elastic constants of palladium from 4.2-300k, Phys. Rev. 118 (1960) 1545-1549, doi:10.1103/PhysRev.118.1545.

[33] B. Amin-Ahmadi, D. Connétable, M. Fivel, D. Tanguy, R. Delmelle, S. Turner, L. Malet, S. Godet, T. Pardoen, J. Proost, D. Schryvers, H. Idrissi, Dislocation/hydrogen interaction mechanisms in hydrided nanocrystalline palladium films, Acta Mater. 111 (2016) 253-261, doi:10.1016/j.actamat.2016.03.054.

[34] M. Mantina, Y. Wang, R. Arroyave, L.Q. Chen, Z.K. Liu, First-principles calculation of self-diffusion coefficients, Phys. Rev. Lett. 100 (2008) 215901, doi:10.1103/PhysRevLett.100.215901.

[35] D. Connétable, M. David, Study of vacancy-(h,b,c,n,o) clusters in al using dft and statistical approaches: consequences on solubility of solutes, J. Alloys Compd. 748 (2018) 12-25, doi:10.1016/j.jallcom.2018.03.081.

[36] L. Delczeg, E. Delczeg-Czirjak, B. Johansson, L. Vitos, Assessing common density functional approximations for the ab initio description of monovacancies in metals, Phys. Rev. B 80 (2009) 205121.

[37] E. Megchiche, S. Pérusin, J. Barthelat, C. Mijoule, Phys. Rev. B 74 (2006).

[38] T.R. Mattsson, A.E. Mattsson, Calculating the vacancy formation energy in metals: pt, pd, and mo, Phys. Rev. B 66 (2002) 214110, doi:10.1103/PhysRevB.66.214110.

[39] E.K. Delczeg-Czirjak, L. Delczeg, L. Vitos, O. Eriksson, Monovacancy formation energies and fermi surface topological transitions in pd-ag alloys, Phys. Rev. B 92 (2015) 224107, doi:10.1103/PhysRevB.92.224107.

[40] J.E. Kluin, Feature article formation of vacancies in noble metals and alloys, Philos. Mag. A 65 (6) (1992) 1263-1286, doi:10.1080/01418619208205604.

[41] H.E. Schaefer, Investigation of thermal equilibrium vacancies in metals by positron annihilation, Physica Status Solidi. A, Applied Research 102 (1) (1987) 47-65.

[42] Y. Kraftmakher, Equilibrium vacancies and thermophysical properties of metals, 1998.

[43] D.A. Andersson, S.I. Simak, Monovacancy and divacancy formation and migration in copper: a first-principles theory, Phys. Rev. B 70 (2004) 115108, doi:10.1103/PhysRevB.70.115108.

[44] R. Nazarov, T. Hickel, J. Neugebauer, Vacancy formation energies in fcc metals: influence of exchange-correlation functionals and correction schemes, Phys. Rev. B 85 (2012) 144118.

[45] M. Iyer, V. Gavini, T.M. Pollock, Energetics and nucleation of point defects in aluminum under extreme tensile hydrostatic stresses, Physical Review B 84 (2014) 014108.

[46] J. Perdew, A. Zunger, Self interaction correction to density functional approximations for many electron systems, Phys. Rev. B 23 (1981) 5048.

[47] H. Mehrer, Diffusion in solids under pressure, in: Grain Boundary Diffusion, Stresses and Segregation, Vol. 309 of Defect and Diffusion Forum, Trans Tech Publications, 2011. 91-112

[48] U. Landman, M.F. Shlesinger, Stochastic theory of multistate diffusion in perfect and defective systems. i. mathematical formalism, Phys. Rev. B 19 (1979) 6207-6219, doi:10.1103/PhysRevB.19.6207.
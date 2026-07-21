# Investigation of the Interaction of Polar Molecules on Graphite Surface: Prediction of Isosteric Heat of Adsorption at Zero Surface Coverage

Wu Fan and Anutosh Chakraborty*

School of Mechanical and Aerospace Engineering, Nanyang Technological University, 50 Nanyang Avenue, Singapore 639798, Republic of Singapore

Supporting Information

**ABSTRACT:** The interactions of polar molecules with various orientations on graphite surface are calculated employing molecular simulation under static conditions in which the multiple-sites Lennard-Jones (LJ), electrostatic, and dipole induction potentials are considered. The Henry's constant and the potential energy as a function of polar molecule−graphite separation distance ($z$) are used to calculate the isosteric heat of adsorption at zero surface coverage ($q_{\text{st}}^{\text{o}}$), and the results are compared to experimentally measure $q_{\text{st}}^{\text{o}}$ data of various polar molecules such as water, ammonia, methanol, and ethanol + graphite systems. The maximum $q_{\text{st}}^{\text{o}}$ values are observed for the $z$ values ranging from 2.5 to 4 Å with respect to various polar molecule orientations. The LJ potential contributes more than 90% and the induction potential adds less than 10% of total potentials at the maximum potential well depth, whereas the electrostatic contributions are found to be less than 1% of total potential energy. It is also found that the induction potential increases exponentially for the separation distance decreasing from 3 to 0 Å for all polar molecules presented in this Article.

![](./images/811139451177664512_1.jpg)

## 1. INTRODUCTION

The adsorption of polar molecules on carbon adsorbents at very low pressure ($P \to 0$) provides necessary information about their hydrophilic and hydrophobic behaviors on adsorbent surfaces, and these behaviors are characterized by the isosteric heat of adsorption ($q_{\text{st}}^{\text{o}}$) as a function of pore with $H$. This information is essential to design and modify carbon materials for adsorption cooling and refrigeration applications.$^{1-3}$ Adsorption of gases and liquids on graphite surfaces was extensively studied$^{4-7}$ as the system comprising graphite and polar or nonpolar adsorbate provides a benchmark to evaluate molecular models such as grand canonical Monte Carlo (GCMC) and molecular dynamics (MD). However, these methods are complex and require very high computational speed to calculate the amount of adsorbate uptake, kinetics, and isosteric heat of adsorption. Therefore, for simplicity, a static molecular simulation technique could be applied to calculate the interaction potential and the isosteric heat of adsorption ($q_{\text{st}}^{\text{o}}$) of the adsorbent−adsorbate system. It is well-known that the potential energy and $q_{\text{st}}^{\text{o}}$ provide important information about the adsorption mechanism ranging from Henry's region to the saturated pressure. Employing the knowledge of $q_{\text{st}}^{\text{o}}$, the amount of adsorbate uptake can be predicted,$^{8}$ and the pore size of adsorbent materials can be designed for various applications.$^{9-13}$

The interactions of adsorbate molecules on graphite surface are analyzed by intermolecular potential models to determine the binding energies.$^{4}$ Among the basic intermolecular potential models, the Lennard-Jones (LJ) potential model of molecules with weak long-range attraction and strong short-range repulsion$^{14}$ has been applied to predict the maximum binding energies. Pair-wise additive LJ potential model between oxygen and carbon has been widely employed to the simulation of molecular dynamics of water and graphite systems.$^{4}$ Besides the interactive force between adsorbate and adsorbent molecules, the lateral attraction force between adsorbed molecules is reported to be positively strong at higher pressure on the most homogeneous, graphitized carbon surface whether the adsorbate molecule is polar or nonpolar.$^{15}$ For adsorbates that are capable of hydrogen bonding such as water, ammonia, and methanol, the hydrogen bonding may occur between adjacent adsorbed molecules or between the adsorbate molecule and surface with oxygen complexes. Simple molecular models that neglect the direct electrostatic, the induction interaction, and high order interactions can bring about a loss of 5−15% of total interaction potential.$^{16,17}$ Therefore, interaction potential models considering electrostatic and induction effects with LJ potential are needed to be developed. For example, following the basic approach of simple effective two-body potentials for hydrogen-bonded molecules, the intermolecular potential of ammonia is represented as the sum of electrostatic interactions between charge sites on each molecule and a single LJ potential between nitrogen molecules.$^{18}$ In another study, the rigid polyatomic models combining LJ and Coulombic interactions are also applied to simulate the adsorption of polar molecules such as

Received: June 19, 2016
Revised: September 14, 2016

methanol and ethanol on graphitized carbon,¹⁹ where the potential of polar molecules on graphitized carbon is presented as the summation of all interactive potentials between LJ sites and partial charges on each molecule. A grand canonical Monte Carlo (GCMC) simulation was applied to calculate the amount of methanol on activated carbon fiber (ACF), and parallel slit pore models are used to calculate the $q_{\text{st}}^{\text{o}}$, and the results are compared to experimentally measured (calorimetric technique) $q_{\text{st}}^{\text{o}}$ data.²⁰ Hence, large differences in the amount of alcohol adsorbed and the differential heat were observed for different carbonyl configurations. Liu and Levan²¹,²² simulated the isosteric heat of adsorption at zero surface coverage as a function of pore width for the nonpolar gases + carbon systems employing (a) cylindrical pore and spherical cavity model²¹ and (b) multiwall carbon surfaces with different geometries.²²

In this Article, we present a thermodynamic approach to calculate the binding energies of polar molecules on graphite basal plane employing static molecular model, where LJ, electrostatic, and induction potentials are considered. The potential energy surfaces are presented with respect to various orientations of polar adsorbate molecules. Employing the derived potential model, the isosteric heat of adsorption is calculated as a function of pore width $H$ for the adsorption of water, ethanol, methanol, and ammonia on graphite surface. We show here the trends of $q_{\text{st}}^{\text{o}}$ for different orientations of adsorbate molecules on graphite planes. The theoretical adsorption potential and $q_{\text{st}}^{\text{o}}$ values are compared to experimental data.

Here, the adsorption potential model integrates LJ, electrostatic, and induction potentials, which takes into account dipole−dipole, dipole−quadrupole, and dipole−induced dipole interactions. Therefore, the predicted interaction potential is more accurate than those only considering LJ and charge−charge interactions according to the energy expansion equation. Prior to this research work, the multilayer LJ potential equation was applied as the interaction potential equation to predict the $q_{\text{st}}^{\text{o}}$ of adsorption for nonpolar molecules in parallel slit pore model.⁶,²² Instead of widely adopted approximation of multilayer LJ potential,²³ the present work applies the integrated and deterministic interaction potential. For simplicity, the parallel slit model is used for predicting $q_{\text{st}}^{\text{o}}$ as a function of pore width for some specific orientations. The interaction between adsorbate molecules is as important as that between adsorbate and adsorbent molecules to calculate the isosteric heats. However, this research work focuses more on $q_{\text{st}}^{\text{o}}$ at zero coverage surfaces. Therefore, the Henry’s law constant is employed in the pressure−temperature−uptake coordinate system (Clausius−Clapeyron equation) for the calculation of $q_{\text{st}}^{\text{o}}$. At zero surface coverage, the density of the adsorbed adsorbate molecules in the simulation box is relatively low, which allows the negligible adsorbate−adsorbate interactions. In this Article, various orientations of polar molecules are studied in the prediction of interaction potential between adsorbate (polar molecule) and the graphite structure. The number of possible orientations of adsorbate molecule is infinite, so a certain types of them can be studied to illustrate the effect of orientations on the interaction potential given the in-plane anisotropy of graphite and the symmetry of adsorbate molecule. It is true that the interaction potential of all orientations contributes to the average interaction potential equally. However, currently it is unable to calculate an average potential over the whole and also infinite orientation space mathematically. Therefore, we choose five different orientations of water molecules. It should be noted here that the orientation set of adsorbate molecules in the simulation box is a limited subset of the whole infinite orientation space for the initial stage of a Monte Carlo simulation.

### 2. THEORETICAL ANALYSES

In physisorption, the interactions between adsorbed species and the adsorbent surface occurred due to weak van der Waals and electrostatic-multipole forces. The total interaction potential is fairly low ($\leq 0.5$ eV). We consider a single component adsorbate molecule physisorbed on a graphite plane. Figure 1 shows the geometrical characteristics of a $\text{H}_2\text{O}$ molecule adsorbed on the hexagonal graphite surface, which contains three particular orientation sites, the hexagon center, C−C bond, and carbon atoms. The selected simulation box comprises 10 layers of carbon atoms, and each layer includes $41 \times 41$ carbon atoms (Figure 1). The sampling adsorbate molecule can move freely. For a given set of carbon atoms $r_j$, the Lennard-Jones, electrostatic, and induction potentials are only functions of adsorbent molecule position vector $\mathbf{r}$ or $(X,Y,Z)$ in graphite coordinate system. The carbon atom layers are in the $X-Y$ plane with fixed $Z$, the direction of adsorbate molecule to the honeycomb lattice of graphite. The total interaction potential $(U)$ depends on the relative position of adsorbate molecule to the hexagonal unit cell of graphite. With fixed $X$ and $Y$, the total interaction potential depends on the $Z$ direction.

![](./images/811139451177664512_2.jpg)

Figure 1. Simulation model of graphite and water molecule (here $\text{H}_2\text{O}$ is considered as an example of a polar molecule). The edge length of the hexagon of carbon atoms is $d = 1.421$ Å, and the distance between two layers is $I = 3.354$ Å. The position vector points from the $i$th carbon to the $j$th atom of the adsorbate molecule. Position vector in adsorbate molecule coordinate system $X'Y'Z'$ can be converted to graphite coordinate system $XYZ$ with a specific rotational matrix and translational vector.

It is well-known that the adsorbent−adsorbate interactions calculated by LJ potential model are generally employed to predict the enthalpy of adsorption at zero surface coverage⁴ with the negligible effects of electrostatic and induction potentials. Therefore, by combining LJ, electrostatic, and induction potentials, the total interaction potential ($U_{\text{mM}}$) term is used to obtain a more complete description of interaction potential for polar molecules, that is, $U_{\text{mM}} = U_{\text{LJ}} + U_{\text{E}} + U_{\text{I}}$. In this Article, we employ the modified LJ potential model as given by⁵

$$
\begin{aligned}
U_{\mathrm{LJ}}(\mathbf{r}_{i}-\mathbf{r}_{j}) &=4 \varepsilon_{i j}\left\{\left(\frac{\sigma_{i j}}{\left|\mathbf{r}_{i}-\mathbf{r}_{j}\right|}\right)^{12}\left[1+\gamma_{\mathrm{R}}\left(1-\frac{6}{5} \cos ^{2} \theta\right)\right]\right. \\
&\left.-\left(\frac{\sigma_{i j}}{\left|\mathbf{r}_{i}-\mathbf{r}_{j}\right|}\right)^{6}\left[1+\gamma_{\mathrm{A}}\left(1-\frac{3}{2} \cos ^{2} \theta\right)\right]\right\}
\end{aligned}
\tag{1}
$$

where $\mathbf{r}_{i}$ indicates the position vector of the $i$th adsorbate molecule atom, $\mathbf{r}_{j}$ is the position vector of the $j$th carbon atom, $\varepsilon_{i j}$ and $\sigma_{i j}$ are pair well depth potential and collision diameter, $\gamma_{\mathrm{R}}$ and $\gamma_{\mathrm{A}}$ are coefficients for repulsion and dispersion component of LJ potential, and $\theta$ is the angle between position vector $(\mathbf{r}_{i}-\mathbf{r}_{j})$ and the outer normal vector of carbon atom plane. According to the Lorentz-Berthelot combining rules, $\varepsilon_{i j}=\sqrt{\varepsilon_{i} \varepsilon_{j}}$ and $\sigma_{i j}=\frac{\sigma_{i}+\sigma_{j}}{2}$.

Equation 1 also captures the anisotropic behaviors of graphite. The carbon atom possesses quadrupole polarizability, $^{24}$ while the dipole moment effects cannot be neglected for polar molecules such as water. The interaction potential of polar molecules with graphite adsorbent consists of charge-charge as well as high-order interactions according to the energy expansion equation (Supporting Information ref 1). Therefore, the necessity for high-order effects such as dipole-dipole, dipole-quadrupole, and induction in polar molecule adsorption is palpable. In the two-body interaction, the polarization arises from the electric field formed by the opposite source. The strength of the polarization is characterized by the dipole and quadrupole moment polarizability tensor. Similarly, the transient induced dipole moment is excited by the opposing electric field to a permanent dipole moment. The electrostatic potential between the water molecule and carbon atom as shown in Figure 2 is derived from the interaction between polar molecule, for example, water dipolar moment $\mu$ and quadrupole moment $\Theta$ in the electric field $\mathbf{E}(\mathbf{r}-\mathbf{r}_{i})$ exerted by the carbon atom.

![](./images/811139451177664512_3.jpg)

Figure 2. Electrostatic model of water and graphite. Here, the dipole moment vector $(\mu)$ for water and quadrupole moment matrix $(\Theta)$ for water and carbon are shown. $r_{i j}$ is the position vector from the $i$th carbon atom to the $j$th atom of the water molecule, and $r_{i j}=-r_{i j}$. The positive charge for hydrogen atom is $q_{\mathrm{H}}$, and the negative charge for oxygen atom is $-2 q_{\mathrm{H}}$. The electric field generated by the quadrupole moment of carbon atom at position $r_{i j}$ is $E \theta_{\mathrm{C}}(r_{i j})$, and the electric field generated by the dipole and quadrupole moment of water is $E \mu_{\mathrm{H}_{2} \mathrm{O}} \theta_{\mathrm{H}_{2} \mathrm{O}}(r_{i j})$. $\theta_{\mathrm{C}}$ and $\theta_{\mathrm{H}_{2} \mathrm{O}}$ are the quadrupole moments of carbon and water. $\mu_{\mathrm{H}_{2} \mathrm{O}}$ and $\mu_{\mathrm{H}_{2} \mathrm{O}}^{\mathrm{I}}$ are the permanent and transient induced dipole moments of water.

$$
U_{\mathrm{E}}(\mathbf{r}-\mathbf{r}_{j})=\boldsymbol{\mu} \cdot \mathbf{E}(\mathbf{r}-\mathbf{r}_{j})+\frac{1}{3} \boldsymbol{\Theta}: \nabla \mathbf{E}(\mathbf{r}-\mathbf{r}_{j})
\tag{2}
$$

where $\mathbf{r}$ is the position vector for the mass center of water molecule, and $\mathbf{r}_{j}$ is the position vector of the $j$th carbon atom. The first term of the right-hand side indicates the dipolar component of electrostatic potential, which is the inner product of dipolar moment vector $\mu$ and the exerted electric field $\mathbf{E}(\mathbf{r}-\mathbf{r}_{j})$. The second term of the right-hand side is quadrupolar, and this is the double-dot product of quadrupolar moment tensor $\Theta$ and the electric field gradient (EFG) tensor $\nabla \mathbf{E}(\mathbf{r}-\mathbf{r}_{j})$. A screening factor, which is 1 for the first layer of carbon atoms and $2/(2.8+1)$ for the rest of the layers, is applied to the electrical potential of dipole and quadrupole moment. $^{25}$ The interaction between transient dipole and permanent charge contributes to the interaction potential, and is represented by

$$
U_{\mathrm{I}}(\mathbf{r}-\mathbf{r}_{j})=-\frac{1}{2} \boldsymbol{\mu}_{\mathrm{p}}^{\mathrm{I}} \cdot \mathbf{E}_{\mathrm{p}}(\mathbf{r}-\mathbf{r}_{j})-\frac{1}{2} \boldsymbol{\mu}_{\mathrm{C}}^{\mathrm{I}} \cdot \mathbf{E}_{\mathrm{C}}(\mathbf{r}-\mathbf{r}_{j})
\tag{3}
$$

where $\mathbf{r}$ is the position vector for the mass center of water molecule, $\mathbf{r}_{j}$ is the position vector of the $j$th carbon atom, $\boldsymbol{\mu}_{\mathrm{p}}^{\mathrm{I}}$ and $\boldsymbol{\mu}_{\mathrm{C}}^{\mathrm{I}}$ are the induced dipole moments of polar molecule and carbon that can be calculated according to their polarizability, and $\mathbf{E}_{\mathrm{p}}(\mathbf{r}-\mathbf{r}_{j})$ and $\mathbf{E}_{\mathrm{C}}(\mathbf{r}-\mathbf{r}_{j})$ are the total electric fields of polar molecule and carbon atom due to both permanent and transient induced dipole. The $q_{\text {st }}^{\mathrm{o}}$ is calculated using a parallel slit pore model, and therefore the interaction of adsorbate molecule with adsorbent pore is considered as the sum of the interaction of one adsorbate molecule with two opposing surfaces that consist of multilayers of adsorbent atoms. From the geometrical and potential model, the interaction potential $U(z)$ of one adsorbate molecule with the distance $z$ above the surface of adsorbent can be determined. The parallel slit model is shown in Figure 3. By definition, the

![](./images/811139451177664512_4.jpg)

Figure 3. Parallel slit shape pore model for graphite. The distances from the center of the adsorbate molecule to the surface of multilayer graphite atoms and the opposing wall are $z$ and $H-z$, respectively, for the pore width of $H$. The external wall potential of the adsorbate molecule in the pore is the sum of the interaction potential with both walls.

external well potential as a function of $z$ can be expressed with respect to the total interaction potential, which is given by

$$
V_{\text {ext }}(z)=U_{\mathrm{mM}}(z)+U_{\mathrm{mM}}(H-z)
\tag{4}
$$

where $H-z$ is the distance of adsorbate molecule to the surface of opposite wall, $H=(H_{\mathrm{c}}-\sigma_{\mathrm{ss}})$ is the required distance for adsorbent-adsorbate interactions along $z$ direction, $H_{\mathrm{C}}$ is the maximum possible distance between the centers of graphite on opposing wall, and $\sigma_{\mathrm{SS}}$ is the size of the carbon atom. Employing


the development of Steel, $^{23}$ the isosteric heat of adsorption at zero surface coverage is $q_{\mathrm{st}}^{\mathrm{o}}=-\left.k T^{2} \frac{\partial \ln K_{\mathrm{H}}}{\partial T}\right|_{x}$, where $x$ is the amount of adsorbate uptake, $K_{\mathrm{H}}$ is the Henry's law constant, and $k$ indicates the Boltzmann constant. The Henry's coefficient is given by $K_{\mathrm{H}}=\frac{1}{A}\left(\frac{Z_{1}}{k T}\right)$, where $A$ is the adsorbent surface area and $Z_{1}=\int_{V} \exp \left[-V_{\text {ext }}(z) / k T\right] \mathrm{d} z$. Substituting the values of $K_{\mathrm{H}}$ and $Z_{1}$ into the $q_{\text {st }}^{\mathrm{o}}$ equation, we have

$$
q_{\mathrm{st}}^{\mathrm{o}}=k T-\frac{\int_{0}^{H} V_{\mathrm{ext}}(z) \exp \left\{-V_{\mathrm{ext}}(z) / k T\right\} \mathrm{d} z}{\int_{0}^{H} \exp \left\{-V_{\mathrm{ext}}(z) / k T\right\} \mathrm{d} z}
$$

as a function of pore width, $H$. The $q_{\text {st }}^{\mathrm{o}}$ is the separate contributions from (i) thermal energy and (ii) adsorbate−graphite basal plane interactions. Hence, the adsorbate−adsorbate interactions are not considered due to low densities of adsorbate molecules in the Henry's region. It should be noted here that with the fixed distance, $z$, varying from adsorbate molecule to honeycomb carbon lattice, the total interaction potential depends on the relative position, $X$ and $Y$, of adsorbate molecule to the hexagonal unit cell of graphite. For hydrogen and oxygen atoms, the partial charges are 0.4238 and −0.8476 elementary charge. On the other hand, the hydrogen−oxygen−hydrogen angle is $104.5^{\circ}$, and the hydrogen−oxygen bond length is $0.95728 \mathring{A}$ for water molecule in TIP3P water model, $^{26}$ which yields both nonzero dipolar and quadrupolar moments. The electrostatic interaction between the water molecule and carbon atom model is found in Figure 2. For polar molecules and carbon atoms, the potential, collision diameter, and anisotropy parameters for calculating LJ potential are listed in Table $1,^{5,24-28}$ and the dipole moment, polarizability of dipole, and quadrupole moment for calculating electrostatic potential are listed in Table $2.^{29-31}$ The detailed simulation procedures are described in the Supporting Information.

<table>
<thead>
<tr>
<th colspan="5">Table 1. Simulation Parameters for Calculating Lennard-Jones Potential</th>
</tr>
<tr>
<th>atom pair</th>
<th>$\varepsilon$ (meV)</th>
<th>$\sigma$ ($\mathring{A}$)</th>
<th>$\gamma_{A}$</th>
<th>$\gamma_{R}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>C−H</td>
<td>2.265</td>
<td>2.965</td>
<td>0.4</td>
<td>−0.54</td>
</tr>
<tr>
<td>C−C</td>
<td>2.981</td>
<td>3.305</td>
<td>0.4</td>
<td>−1.05</td>
</tr>
<tr>
<td>C−N</td>
<td>2.811</td>
<td>3.390</td>
<td>0.4</td>
<td>−1.05</td>
</tr>
<tr>
<td>C−O</td>
<td>3.450</td>
<td>3.141</td>
<td>0.4</td>
<td>−1.05</td>
</tr>
</tbody>
</table>

## 3. RESULTS AND DISCUSSION

In this Article, the interactions between the graphite and water are presented with respect to five different orientations of water molecules, and these are shown in Figure 4. Note that the O···C distances are not important here as Figure 4 aims to describe five orientations rather than the distance between graphite and the water molecule. In fact, the molecule−graphite distance ($z$) of the five orientations can be varied from 2 to $10 \mathring{A}$ for the calculation of interaction potential. For water molecule at orientation 1, the oxygen atom is at the origin and one hydrogen atom is at $X$ axis, while the H−O−H is found in the $XY$ plane. The oxygen−graphite distance is $3 \mathring{A}$. For water molecule at orientation 2, the oxygen atom is observed at the origin. Here, one of the hydrogen atoms is at $X$ axis and the other follows toward the graphite surface, while the H−O−H plane is found at the $XZ$ plane. The oxygen−graphite distance is calculated as $3.5 \mathring{A}$. The oxygen atom is at the origin for orientation 3, where one hydrogen atom is at $X$ axis, the other hydrogen atom is away from the graphite, and the H−O−H orientation is at the $XZ$ plane. The oxygen−graphite distance is found to be $3 \mathring{A}$. The orientation 4 of water molecule is also shown in Figure 4, where the oxygen atom is at the origin, both of the hydrogen atoms are pointed away from the graphite, and the angle between H−O bond and $X$ axis is $\frac{180^{\circ}-104.52^{\circ}}{2}=37.74^{\circ}$. The H−O−H orientation is observed with respect to the $XZ$ plane. The oxygen−graphite distance is $3 \mathring{A}$. For the water molecule at fifth orientation, the oxygen atom is at the origin. Both of the hydrogens atoms are pointed toward the graphite surface, and the angle between H−O bond and $X$ axis is $\frac{180^{\circ}-104.52^{\circ}}{2}=37.74^{\circ}$. The H−O−H plane is parallel to the $XZ$ plane. The oxygen−graphite distance is $3 \mathring{A}$.

![](./images/811139451177664512_5.jpg)

Figure 4. Five different orientations of a water molecule on the graphite surface at the distance of $z$ in $Z$ direction.

The interaction energy of a water molecule with a single carbon atom as a function of O···C separations ($z$) for five selected water orientations is shown in Figure 5. It is clearly observed that the minimum H···C potential is overlapped with the repulsive portion of the O···C potential, and this overlap makes the linear C···H−O configuration most favorable. Any deviation from linearity increases the overlap and makes the C···H−O configuration more repulsive. It is found that the interaction potentials of orientations 1, 3, 4, and 5 are larger than those of orientation 2. From orientations 2 and 5, it is found that one or two hydrogen atoms of water molecule are pointed toward the basal plane of graphite; that is, H atoms are closer to carbon atoms at the same O···C distance. For also orientations 2 and 5, the smaller interaction potential can be explained by the dramatically increased positive repulsion in Lennard-Jones

<table>
<thead>
<tr>
<th colspan="7">Table 2. Simulation Parameters for Calculating Electrostatic Potential$^{a}$</th>
</tr>
<tr>
<th>molecule</th>
<th>$\boldsymbol{\mu}$ (D)</th>
<th>$\boldsymbol{\alpha}_{xx}$</th>
<th>$\boldsymbol{\alpha}_{yy}$</th>
<th>$\boldsymbol{\alpha}_{zz}$</th>
<th>$\boldsymbol{\Theta}_{xx}$ (D$\mathring{A}$)</th>
<th>$\boldsymbol{\Theta}_{yy}$ (D$\mathring{A}$)</th>
<th>$\boldsymbol{\Theta}_{zz}$ (D$\mathring{A}$)</th>
</tr>
</thead>
<tbody>
<tr>
<td>carbon</td>
<td></td>
<td>$1.44 \mathring{A}^{3}$</td>
<td>$1.44 \mathring{A}^{3}$</td>
<td>$0.41 \mathring{A}^{3}$</td>
<td>−0.5</td>
<td>−0.5</td>
<td>1</td>
</tr>
<tr>
<td>water</td>
<td>1.855</td>
<td>$1.53 \mathring{A}^{3}$</td>
<td>$1.42 \mathring{A}^{3}$</td>
<td>$1.47 \mathring{A}^{3}$</td>
<td>2.63</td>
<td>−2.50</td>
<td>−0.13</td>
</tr>
<tr>
<td>ammonia</td>
<td>1.42</td>
<td>$13.8 \mathrm{bohr}^{3}$</td>
<td>$13.8 \mathrm{bohr}^{3}$</td>
<td>$13.93 \mathrm{bohr}^{3}$</td>
<td>1.16</td>
<td>1.16</td>
<td>−2.32</td>
</tr>
<tr>
<td>methanol</td>
<td>1.69</td>
<td>$3.69 \mathring{A}^{3}$</td>
<td>$3.25 \mathring{A}^{3}$</td>
<td>$3.06 \mathring{A}^{3}$</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>ethanol</td>
<td>1.69</td>
<td>$30.37 \mathrm{bohr}^{3}$</td>
<td>$33.61 \mathrm{bohr}^{3}$</td>
<td>$38.87 \mathrm{bohr}^{3}$</td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

$^{a}$For polarizability, $1 \mathring{A}^{3}=1.11265 \times 10^{-40} \mathrm{C} \cdot \mathrm{m}^{2} / \mathrm{V}$, $1 \mathrm{bohr}^{3}=1.648773 \times 10^{-41} \mathrm{C} \cdot \mathrm{m}^{2} / \mathrm{V}$.

![](./images/811139451177664512_6.jpg)

Figure 5. Interaction energy of a water molecule with a single carbon atom as a function of C···O separation ($z$) for five different orientations.

potential added to the total negative potential as the distance ($z$) between the pair is decreased. The potential energy with respect to maximum well depth ranges from $-116$ to $-160$ meV depending on various orientations of water molecule, which agrees well with the available experimental value of $-156$ meV$^{32}$ as well as the calculated value of $-149$ meV reported by Markovic et al.$^{33}$ and $-126$ meV reported by Lin et al.$^{34}$ for water adsorption on graphene at zero surface coverage. It is also found that the electrostatic as well as induction potential increases faster when the separation distance ($z$) is smaller than $3$ Å (for water). The calculated potential energy surfaces for the water molecule with various orientations are explained in the Supporting Information.

Employing the formulation, a plot of $q_{\text{st}}^{\text{o}}$ for different water molecule orientations is shown in Figure 6. It is found that the

![](./images/811139451177664512_7.jpg)

Figure 6. Isosteric heat of adsorption of a single water molecule on a graphite atom at zero surface coverage as a function of $z$ for the selected five $\text{H}_{2}\text{O}$ orientations.

maximum $q_{\text{st}}^{\text{o}}$ of one molecule varies from $0.25$ to $0.35$ eV. For maximum isosteric heat of adsorption, the pore width varies from $2$ to $4.5$ Å with respect to the water molecule orientations. The interaction energy between a water molecule and a single layer of graphite is estimated to be $5.8 \pm 0.4$ kcal/mol ($\sim$0.25 eV).$^{35}$ In other reports,$^{36,37}$ the $q_{\text{st}}^{\text{o}}$ values at zero surface coverage vary from $1.65$ to $4.3$ kcal/mol ($0.071 - 0.185$ eV). Employing the polarizable potential model, Karapetian and Jordan$^{38}$ predicted the heat of adsorption of water molecule and graphite to be $2.50$ kcal/mol ($\sim$0.107 eV). In another study,$^{39}$ it was found that the water molecule was located at least $3.5$ Å above the graphite surface for the maximum $q_{\text{st}}^{\text{o}}$. Not only this, but also the adsorption energies on graphite surface are varied from $2.90$ to $13.72$ kcal/mol ($\sim$0.125$-$$0.59$ eV) for the distance of oxygen$-$ graphite surface ranging from $3.01$ to $3.043$ Å.$^{34}$ These data are also added in Figure 6. The $q_{\text{st}}^{\text{o}}$ is found below its liquefaction ($0.42$ eV) heat due to the hydrophobic behavior of graphite surface. It should be noted here that the maximum $q_{\text{st}}^{\text{o}}$ is found for the pore width ranging from $2.5$ to $4$ Å, which can be compared to the mean diameter of the water molecule ($2.9$ Å) or the hydrogen-bond length of $3$ Å.

Figure 7a shows three different orientations of ammonia molecule on graphite surface. It is well-known that the ammonia

![](./images/811139451177664512_8.jpg)

Figure 7. (a) Orientations of ammonia molecules above graphite ranging from $-90^{\circ}$ to $90^{\circ}$ along the $X$-axis, (b) interaction energy between graphite and ammonia $\nu(\text{C}\cdots\text{NH}_{3})$ for various $z$, and (c) $q_{\text{st}}^{\text{o}}$ as a function of $z$ for three different orientations of a $\text{NH}_{3}$ molecule.

molecule is close to a tetrahedron with one nitrogen atom at the top and three hydrogen atoms at the bottom with a $\text{H}-\text{N}-\text{H}$ angle of $107^{\circ}$ and a $\text{N}-\text{H}$ bond length of $1.017$ Å. In orientation 1, two hydrogen atoms and one nitrogen atom are parallel to the $X$-$Y$ plane. The $\text{NH}_{3}$ molecule is rotated from $90^{\circ}$ to $-90^{\circ}$ along the $X$ axis for the orientations 2 and 3, respectively. For three different $\text{NH}_{3}$ molecules orientations, the interaction potential as a function of $z$ is shown in Figure 7b. The interaction potential calculated by the LJ component is added here for comparison purposes. The orientation 2 provides the maximum well depth potential of $-125$ meV at $z = 3.6$ Å, which implies a stronger binding interaction between the carbon$-$ammonia pair. For orientations 1 and 3, the maximum interaction potentials are found to be $-108$ and $-107$ meV at $3.6$ and $3.5$ Å, respectively.

This occurs due to the linear configuration of potential well depth or $\nu_{\text{ext}}(\text{NH}_3\cdots\text{C})$, that is, the overlapping of $\text{H}\cdots\text{C}$ potential with the repulsive $\text{N}\cdots\text{C}$ potential. As a result, the most favorable $\text{C}\cdots\text{H}-\text{N}$ linear configuration occurred. Any deviation from the linear $\text{C}\cdots\text{H}-\text{N}$ configuration makes the ammonia–graphite interaction more repulsive, and the potential well depth $\nu_{\text{ext}}(\text{NH}_3\cdots\text{C})$ decreases. It should be noted here that both the electrostatic and the induction potentials increase faster when the separation distance $(z)$ is smaller than $3$ Å for the ammonia molecule. More information can be found in the Supporting Information. Employing the potential data along $z$ direction, a plot of $q_{\text{st}}^\text{o}$ for one $\text{NH}_3$ molecule adsorption is shown in Figure 7c. With respect to $\text{NH}_3$ orientation, the maximum $q_{\text{st}}^\text{o}$ varies from $0.23$ to $0.27$ eV for the $z$ values ranging from $3$ to $4$ Å, which can be compared to the mean diameter of $\text{NH}_3$ molecule ($3.6$ Å). These results are also compared to experimentally measured $q_{\text{st}}^\text{o}$ data at zero surface coverage, which are $10.5$ kcal/mol ($0.45$ eV) and $7$ kcal/mol ($0.3$ eV) for ammonia adsorption on carbon type Spheron 1000 and Spheron 2700, respectively. $^{40}$ The simulation results are quite close to the experimentally measured $q_{\text{st}}^\text{o}$ (6 kcal/ mol $\approx 0.258$ eV) data for the adsorption of ammonia on graphite. $^{41}$ The experimentally measured $q_{\text{st}}^\text{o}$ data are added in Figure 7c for comparison purposes.

Figure 8a shows three different orientations of one methanol molecule on graphite surface at the beginning of adsorption. Here, the carbon and oxygen bond is almost parallel to the carbon–carbon bond of graphite or the basal panel ($XY$ plane) as observed in orientation 1. The $\text{CH}_3-\text{OH}$ molecule is rotated $90^\circ$ with respect to the $X$-axis (orientation 2). On the other hand, the methanol molecule is rotated $-90^\circ$ above the graphite surface (orientation 3). A plot of binding interactions between one methanol molecule and graphite surface is shown in Figure 8b for three different $\text{CH}_3-\text{OH}$ orientations. The maximum potential well depth, $U_{\text{mM}}$, of $(\text{CH}_3-\text{OH}\cdots\text{C})$ varies from $-210$ to $-180$ meV when the methanol molecule is rotated from 0 to $90^\circ$ along the $X$-axis. On the other hand, the $U_{\text{mM}}$ of $(\text{CH}_3-\text{OH}\cdots\text{C})$ ranges from $-210$ to $-170$ meV for the rotational angle of methanol varying from 0 to $-90^\circ$ along its $X$-axis. The induction potential increases exponentially for the separation distance decreasing from $3$ to $0$ Å. However, the electrostatic potential is very small (Supporting Information). The plots of $q_{\text{st}}^\text{o}$ for various orientations of $\text{CH}_3-\text{OH}$ molecule on graphite surface are shown in Figure 8c. The higher $q_{\text{st}}^\text{o}$ at zero $\text{CH}_3-\text{OH}$ loading varies from $0.35$ to $0.44$ eV due to the combination of methanol– methanol and methanol–graphite interactions with the spillover of methanol molecules onto the graphite surface. At the beginning of methanol adsorption on carbon pores, the $q_{\text{st}}^\text{o}$ is measured as $58$ kJ/mol ($\sim0.58$ eV) at $303$ K. $^{42}$ For higher pore width, the $q_{\text{st}}^\text{o}$ decreases due to weak interactions between $\text{CH}_3-$ OH and graphite surface. As compared to the methanol molecule diameter of $4.2$ Å, the maximum $q_{\text{st}}^\text{o}$ is found for the values of $z$ ranging from $3.4$ to $4$ Å with respect to various methanol molecule orientations. It is also found that at the distance of $3.7$ Å, the attractive forces of the more distant groups of alcohol molecules are not compensated by the repulsive forces, and the $q_{\text{st}}^\text{o}$ is measured to be $10$ kcal/mol ($\sim0.43$ eV). $^{32}$ The adsorption of methanol in graphite pores shows slightly different behavior as compared to that of water due to stronger dispersion interactions of the $\text{CH}_3$ group with the carbon surface. Horikawa et al. $^{15}$ measured the $q_{\text{st}}^\text{o}$ as $32$ kJ/mol ($\sim0.32$ eV) for methanol adsorption on graphitized carbon black.

![](./images/811139451177664512_9.jpg)

Figure 8. (a) Three different orientations of methanol molecule on graphite surface for understanding $\text{C}\cdots\text{CH}_3-\text{OH}$ interactions, (b) $\nu(\text{C}\cdots\text{CH}_3-\text{OH})$ or intermolecular potential between graphite and methanol as a function of $z$, and (c) $q_{\text{st}}^\text{o}$ of the methanol molecule + graphite system for various $z$ values.

Figure 9a also shows three different orientations of ethanol molecule on a graphite surface. In orientation 1 of the ethanol molecule, both carbon–carbon and carbon–oxygen bonds are almost parallel to the carbon–carbon bond of graphite above the $XY$ plane. From simulation results, it is found that the maximum potential well depth $\nu_{\text{ext}}(\text{C}\cdots\text{CH}_3-\text{CH}_2-\text{OH})$ varies from $-300$ to $-270$ meV for the rotational angle of ethanol varying from $-90^\circ$ to $90^\circ$ with respect to its $X$-axis. The interaction potential as a function of $z$ is shown in Figure 9b. It should be noted here that the induction potential increases exponentially for the separation distance $(z)$ decreasing from $3$ to $0$ Å. However, the electrostatic potential remains constant with very small values (close to zero, Supporting Information). A plot of $q_{\text{st}}^\text{o}$ for one $\text{CH}_3\text{CH}_2-\text{OH}$ molecule is found in Figure 9c. The $q_{\text{st}}^\text{o}$ at zero surface coverage varies from $0.56$ to $0.62$ eV for the orientations of ethanol molecule rotating from $90^\circ$ to $-90^\circ$. The maximum $q_{\text{st}}^\text{o}$ values are obtained between $3.5$ and $4$ Å similar to the ethanol molecule diameter of $4.4$ Å. At the temperature of $300$ K, the simulation results of $q_{\text{st}}^\text{o}$ at zero surface coverage are found in good agreement with the estimated experimental values that range from $13 \pm 0.4$ kcal/mol ($\sim0.54$ eV) to $16 \pm 0.4$ kcal/mol ($\sim0.688$ eV) given by ref 43. From the simulation study, the optimum pore width is found to be $3.5$ Å. This is due to the fact that at the distance of $3.5$ Å, the attractive forces of isometric alcohol molecules are not compensated for by the repulsive forces.

![](./images/811139451177664512_10.jpg)

Figure 9. (a) Ethanol molecule orientations along the $X$ axis of rotation above the graphite, (b) $v(\mathrm{C\cdots CH_3-CH_2-OH})$ as a function of $z$ for three orientations of an ethanol molecule, and (c) $q_{\text{st}}^o$ for graphite and ethanol system for different $z$ values ranging from 1 to $10\ \mathring{A}$.

Figure 10 shows the various parts of total interaction energy for five different orientations of one water molecule on graphite surface as illustrated in Figure 4. The interactions between the graphite structure and the $\mathrm{H_2O}$ molecule are mainly dominated by the LJ interaction for $\mathrm{H_2O}$ orientations. The electrostatic potential that occurs due to partial charges of water as indicated by red lines in Figure 10 is found positive for orientations 1, 2, and 4 and provides repulsive interactions as hydrogen atoms of water molecule are pointed away from the graphite plane. However, negative electrostatic values are found in orientations 3 and 5 due to attractive interactions of hydrogen atoms that are pointed toward the graphite surface, as well as $\mathrm{H-O-H}$ is at the $X-Z$ plane. The induction effects are relatively significant between water and graphite due to the strong polarizability of the water molecule (Table 2). It should be noted that the LJ interaction is found higher at orientation 1 due to a higher attractive interaction at the optimal $\mathrm{C\cdots O}$ separation distance $(z_o)$ of $3.1\ \mathring{A}$. The interaction potential is found lower at $3.65\ \mathring{A}$ (orientation 2) due to repulsive interactions between $\mathrm{C}$ and $\mathrm{O}$. The induction interaction is the highest at orientation 5 $(z_o=2.8\ \mathring{A})$ due to the smallest distance of the water dipole to the basal plane of graphite. Similarly, the induction potential of orientation 2 is the smallest among all five orientations (Figure 10) as the distance between $\mathrm{C}$ and $\mathrm{O}$ is the highest. Figure 11 shows the maximum interactions for (a) orientation 1 of water molecule (total of $-167.75$ meV $=-153.15$ meV LJ $-14.61$ meV induction $+0.16$ meV electrostatic at $2.9\ \mathring{A}$), (b) orientation 2 of ammonia molecule (total of $-153.79$ meV $=-148.69$ meV LJ $-4.02$ meV induction $-1.071$ meV electrostatic at $3.5\ \mathring{A}$), (c) orientation 2 of methanol molecule (total of $-249.36$ meV $=-243.15$ meV LJ $-6.17$ meV induction $-0.032$ meV electrostatic), and (d) orientation 3 of ethanol (total of $-356.43$ meV $=-348.78$ meV LJ $-7.09$ meV induction $-0.557$ meV electrostatic). On the other hand, the electrostatic potential is very small as compared to the LJ potential and provides attractive or repulsive interactions depending on molecule orientations. More information is provided in the Supporting Information. In addition, the induction effects are relatively significant between polar and graphite because of the strong polarizability of the polar molecule.

![](./images/811139451177664512_11.jpg)

Figure 10. A detailed analysis of $v(\mathrm{C\cdots O})$ for five optimum orientations $(z_o)$ of a water molecule on a graphite, where maximum $q_{\text{st}}^o$ is obtained.

![](./images/811139451177664512_12.jpg)

Figure 11. A detailed analysis on interaction potentials $v(z_o)$ for four polar molecules, where the orientations of $H_2O, NH_3, CH_3-OH$, and $CH_3-CH_2-OH$ are chosen at their maximum $q_{st}^o$ and $z_o$.

## 4. CONCLUSIONS

We have carried out molecular simulations of polar molecules such as water, ammonia, methanol, and ethanol in graphite structure at the temperature of 300 K under static conditions for calculating potential well depth and the isosteric heat of adsorption at zero surface coverage. The interaction potential curves as a function of adsorbate−adsorbent separation distance $z$ and heat curves as a function of pore width $H$ illustrate how these molecules interact with a graphite surface. Some important features are as follows:

(i) The maximum potential well for graphite−water system constitutes 91.28% Lennard-Jones potential $v_{LJ}(C\cdots H_2O)$, 8.7% induction potential $v_I(C\cdots H_2O)$, and 0.012% electrostatic $v_E(C\cdots H_2O)$. The maximum potential well depth depends on various orientations of $H_2O$ molecule on graphite structure. The maximum $q_{st}^o$ at zero surface coverage is found to be 0.35 eV at orientation 1, where the oxygen atom is at the origin, one H atom is at the $X$-axis, and $H-O-H$ is obtained in the $X-Y$ plane, and the simulation result is very close to the experimental data of 0.32 eV. For water molecules, the electrostatic contribution for $v(z)$ is very close to zero and provides attractive or repulsive interactions between adsorbate and graphite molecules. On the other hand, the LJ, induction, and electrostatic contributions for ammonia adsorption on graphite are 96.68%, 2.61%, and 0.71%, respectively, for orientation 2. For water and ammonia molecules, both the induction and the electrostatic potentials increase exponentially for the separation distance decreasing from 3 to $0\ \mathring{A}$.

(ii) For ethanol and methanol, the electrostatic contribution is close to zero and provides both attractive and repulsive interactions. The $v_{LJ}(C\cdots CH_3-OH)$ and $v_{LJ}(C\cdots CH_3-CH_2-OH)$ contributions are more than 90%. The induction interactions are less than 10%. For both methanol and ethanol molecules, the induction potential increases exponentially for the separation distance decreasing from 3 to $0\ \mathring{A}$. However, the electrostatic potential remains constant, and the value is very close to zero.

(iii) Employing simulation results, the maximum potential well depths for polar molecules and graphite are obtained between 2.9 and $4\ \mathring{A}$ for various polar molecule orientations, which can be compared to the hydrogen-bond length range of about $3\ \mathring{A}$ as well as the polar molecule diameter.

(iv) From the present analysis, it is concluded that the maximum $q_{st}^o$ of the graphite−water system is smaller than the enthalpy of liquefaction of water. However, for ammonia, methanol, and ethanol + graphite systems, the maximum $q_{st}^o$ is found higher than the enthalpy of liquefaction.

## ASSOCIATED CONTENT

### Supporting Information
The Supporting Information is available free of charge on the ACS Publications website at DOI: 10.1021/acs.jpcc.6b06119.

Multipole expansion of energy; reduced multipole expansion of energy; computational strategy for electric field, interaction potential, and isosteric heat; dipole−quadropole interaction potential; interaction potential of water on graphite; interaction potential of ammonia on graphite; interaction potential of methanol on graphite; interaction potential of ethanol on graphite; coordinate transformation; molecule coordinate; nomenclature; and additional references (PDF)

## AUTHOR INFORMATION

### Corresponding Author
*Tel.: +65-6790-4222. E-mail: achakraborty@ntu.edu.sg.

### Notes
The authors declare no competing financial interest.

## ACKNOWLEDGMENTS
We acknowledge the financial support from the Ministry of Education, Singapore (grant no. MOE2014-T2-2-061).

## NOMENCLATURE
E = electric field vector (V/m)

$\mathbf{E}_{\text{dipole}}$ = electric field vector of a dipole (V/m)
$\mathbf{E}_{\text{quadrupole}}$ = electric field vector of a quadrupole (V/m)
$\mathbf{F}$ = electric field vector (V/m)
$\mathbf{I}$ = 3×3 unit diagonal matrix
$\text{m}$ = adsorbate (water, ammonia, etc.)
$\text{M}$ = adsorbent (graphite)
$q_{\text{st}}^o$ = isosteric heat of adsorption (eV)
$\mathbf{r}$ = position vector between two multipoles (m)
$\mathbf{r}^{\text{T}}$ = transposed position vector (m)
$\mathbf{r}_i$ = position vector of the $i$th atom of the adsorbate molecule (m)
$\mathbf{r}_j$ = position vector of the $j$th carbon atom (m)
$\mathbf{r}_{ij}$ = position vector from the $i$th carbon to the $j$th atom of the adsorbate molecule (m)
$R$ = ideal gas constant (J/(mol·K))
$T$ = absolute temperature (K)
$U$ = potential (J)
$U_{\text{LJ}}$ = Lennard-Jones potential (J)
$U_{\text{E}}$ = electrostatic potential (J)
$U_{\text{I}}$ = induction potential (J)
$U_{\text{mM}}$ = total interaction potential (J)
$v_{\text{ext}}$ = total external potential (meV)
$v_{\text{LJ}}$ = Lennard-Jones potential (meV)
$v_{\text{E}}$ = electrostatic potential (meV)
$v_{\text{I}}$ = induction potential (meV)
$z$ = the distance between adsorbent−adsorbate (Å)
$z_o$ = the distance for maximum $q_{\text{st}}^o$ (Å)
$\boxed{\alpha}$ = polarizability matrix ($\text{Å}^3$)
$\varepsilon_0$ = vacuum permittivity (C/(V·m))
$\varepsilon$ = potential (J)
$\varepsilon_{ij}$ = pair well depth potential (J)
$\boxed{\Theta}$ = quadrupole moment matrix (DÅ)
boxed{$\mu$} = dipole moment vector (D)
$\boxed{\mu}^{\text{I}}$ = induced dipole moment vector (D)
$\boxed{\mu}_{\text{H}_2\text{O}}^{\text{I}}$ = induced dipole moment vector of water molecule (D)
$\boxed{\mu}_{\text{C}}^{\text{I}}$ = induced dipole moment vector of carbon atom (D)
$\sigma$ = collision diameter (m)
$\sigma_{ij}$ = pair collision diameter (m)
$\gamma_{\text{A}}$ = coefficient of Lennard-Jones potential
$\gamma_{\text{R}}$ = coefficient of LJ potential
$\phi_{\text{dipole}}$ = electrical potential of a dipole (V)
$\phi_{\text{quadrupole}}$ = electrical potential of a quadrupole (V)

### Abbreviations
LJ = Lennard-Jones
$\text{Q}_{\text{st}}$ = adsorption isosteric heat
EFG = electric field gradient

---

### REFERENCES

(1) Xu, S. Z.; Wang, L. W.; Wang, R. Z. Thermodynamic Analysis of Single-Stage and Multi-Stage Adsorption Refrigeration Cycles with Activated Carbon-Ammonia Working Pair. *Energy Convers. Manage.* **2016**, *117*, 31−42.

(2) Wang, L. W.; Metcalf, S. J.; Critoph, R. E.; Thorpe, R.; Tamainot-Telto, Z. Development of Thermal Conductive Consolidated Activated Carbon for Adsorption Refrigeration. *Carbon* **2012**, *50*, 977−986.

(3) Ghazy, M.; Askalany, A. A.; Harby, K.; Ahmed, M. S. Adsorption Isotherms and Kinetics of HFC-404A onto Bituminous Based Granular Activated Carbon for Storage and Cooling Applications. *Appl. Therm. Eng.* **2016**, *105*, 639−645.

(4) Werder, T.; Walther, J. H.; Jaffe, R. L.; Halicioglu, T.; Koumoutsakos, P. On the Water-Carbon Interaction for Use in Molecular Dynamics Simulations of Graphite and Carbon Nanotubes. *J. Phys. Chem. B* **2003**, *107*, 1345−1352.

(5) Carlos, W. E.; Cole, M. W. Interaction between a He Atom and a Graphite Surface. *Surf. Sci.* **1980**, *91*, 339−357.

(6) Schindler, B. J.; Levan, M. D. The Theoretical Maximum Isosteric Heat of Adsorption in the Henry’s Law Region for Slit-Shaped Carbon Nanopores. *Carbon* **2008**, *46*, 644−648.

(7) Wang, M. X.; Huang, Z. H.; Lv, W.; Yang, Q. H.; Kang, F. Y.; Liang, K. M. Water Vapor Adsorption on Low-Temperature Exfoliated Graphene Nanosheets. *J. Phys. Chem. Solids* **2012**, *73*, 1440−1443.

(8) Chakraborty, A.; Leong, K. C.; Thu, K.; Saha, B. B.; Ng, K. C. Theoretical Insight of Adsorption Cooling. *Appl. Phys. Lett.* **2011**, *98*, 221910.

(9) Wang, Q. M.; Shen, D. M.; Bulow, M.; Lau, M. L.; Deng, S. G.; Fitch, F. R.; Lemcoff, N. O.; Semanscin, J. Metallo-Organic Molecular Sieve for Gas Separation and Purification. *Microporous Mesoporous Mater.* **2002**, *55*, 217−230.

(10) Duren, T.; Sarkisov, L.; Yaghi, O. M.; Snurr, R. Q. Design of New Materials for Methane Storage. *Langmuir* **2004**, *20*, 2683−2689.

(11) Gadipelli, S.; Guo, Z. X. Graphene-Based Materials: Synthesis and Gas Sorption, Storage and Separation. *Prog. Mater. Sci.* **2015**, *69*, 1−60.

(12) Lawler, K. V.; Sharma, A.; Alagappan, B.; Forster, P. M. Assessing Zeolite Frameworks for Noble Gas Separations through a Joint Experimental and Computational Approach. *Microporous Mesoporous Mater.* **2016**, *222*, 104−112.

(13) Fan, W.; Chakraborty, A.; Kayal, S. Adsorption Cooling Cycles: Insights into Carbon Dioxide Adsorption on Activated Carbons. *Energy* **2016**, *102*, 491−501.

(14) Bojan, M. J.; Steele, W. A. Chapter Four - Monte Carlo and Molecular Dynamics. *Adsorption by Carbons*; Elsevier: Amsterdam, 2008; pp 77−101.

(15) Horikawa, T.; Zeng, Y.; Do, D. D.; Sotowa, K.; Alcantara Avila, J. R. On the Isosteric Heat of Adsorption of Non-Polar and Polar Fluids on Highly Graphitized Carbon Black. *J. Colloid Interface Sci.* **2015**, *439*, 1−6.

(16) Brennan, J. K.; Bandosz, T. J.; Thomson, K. T.; Gubbins, K. E. Water in Porous Carbons. *Colloids Surf, A* **2001**, *187*, 539−568.

(17) Brennan, J. K.; Thomson, K. T.; Gubbins, K. E. Adsorption of Water in Activated Carbons: Effects of Pore Blocking and Connectivity. *Langmuir* **2002**, *18*, 5438−5447.

(18) Impey, R. W.; Klein, M. L. A Simple Intermolecular Potential for Liquid-Ammonia. *Chem. Phys. Lett.* **1984**, *104*, 579−582.

(19) Birkett, G. R.; Do, D. D. Simulation Study of Methanol and Ethanol Adsorption on Graphitized Carbon Black. *Mol. Simul.* **2006**, *32*, 887−899.

(20) Nobusawa, S.; Kaku, H.; Amada, T.; Asano, H.; Satoh, K.; Ruike, M. Calorimetric Study and Simulation of the Adsorption of Methanol and Propanol onto Activated Carbon Fibers. *Colloids Surf, A* **2013**, *419*, 100−112.

(21) Liu, J.; Levan, M. D. Isosteric Heats of Adsorption in the Henry’s Law Region for Carbon Single Wall Cylindrical Nanopores and Spherical Nanocavities. *Carbon* **2009**, *47*, 3415−3423.

(22) Liu, J.; LeVan, M. D. Henry’s Law Constants and Isosteric Heats of Adsorption at Zero Loading for Multi-Wall Carbon Surfaces with Different Geometries. *Carbon* **2010**, *48*, 3454−3462.

(23) Steele, W. A. *The Interaction of Gases with Solid Surfaces*; Pergamon Press: Oxford; New York, 1974.

(24) Ionov, S. I.; LaVilla, M. E. Probing the Molecule−Surface Interaction Via Inversion Symmetry Changes in the Scattering of State-selected ND₃ on Graphite (0001). *J. Chem. Phys.* **1992**, *97*, 9379−9388.

(25) Lakhlifi, A.; Killingbeck, J. P. Investigation of the Interaction of Some Astrobiological Molecules with the Surface of a Graphite (0001) Substrate. Application to the CO, HCN, H₂O and H₂CO Molecules. *Surf. Sci.* **2010**, *604*, 38−46.

(26) Abascal, J. L. F.; Vega, C. The Water Forcefield: Importance of Dipolar and Quadrupolar Interactions. *J. Phys. Chem. C* **2007**, *111*, 15811−15822.

(27) Hansen, F. Y.; Bruch, L. W.; Roosevelt, S. E. Electrostatic Forces and the Frequency-Spectrum of a Monolayer Solid of Linear-Molecules on Graphite. *Phys. Rev. B: Condens. Matter Mater. Phys.* **1992**, *45*, 11238−11248.

(28) Vidali, G.; Cole, M. W. Lateral Variation of the Physisorption Potential for Noble-Gases on Graphite. *Phys. Rev. B: Condens. Matter Mater. Phys.* **1984**, *29*, 6736−6738.

(29) Spassova, M.; Monev, V.; Kanev, I.; Champagne, B.; Mosley, D. H.; JM, A. *Ab Initio Summation over States/Sci. for Static and Dynamic Hyperpolarizabilities of Small Molecules*; Kluwer Academic Publishers: Great Britain, 2000; Basic Problems and Model Systems.

(30) Chelli, R.; Pagliai, M.; Procacci, P.; Cardini, G.; Schettino, V. Polarization Response of Water and Methanol Investigated by a Polarizable Force Field and Density Functional Theory Calculations: Implications for Charge Transfer. *J. Chem. Phys.* **2005**, *122*, 074504.

(31) DiStasio, R. A.; Gobre, V. V.; Tkatchenko, A. Van Der Waals Interactions in Molecules and Condensed Matter. *J. Phys.: Condens. Matter* **2014**, *26*, 213202.

(32) Avgul, N. N.; Kieslev, A. V. *Chemistry and Physics of Carbon*; Marcel Dekker: New York, 1970.

(33) Markovic, N.; Andersson, P. U.; Nagard, M. B.; Pettersson, J. B. C. Scattering of Water from Graphite: Simulations and Experiments. *Chem. Phys.* **1999**, *247*, 413−430.

(34) Lin, C. S.; Zhang, R. Q.; Lee, S. T.; Elstner, M.; Frauenheim, T.; Wan, L. J. Simulation of Water Cluster Assembly on a Graphite Surface. *J. Phys. Chem. B* **2005**, *109*, 14183−14188.

(35) Feller, D.; Jordan, K. D. Estimating the Strength of the Water/Single-Layer Graphite Interaction. *J. Phys. Chem. A* **2000**, *104*, 9971−9975.

(36) Pertsin, A.; Grunze, M. Water-Graphite Interaction and Behavior of Water near the Graphite Surface. *J. Phys. Chem. B* **2004**, *108*, 1357−1364.

(37) Liu, J. C.; Monson, P. A. Monte Carlo Simulation Study of Water Adsorption in Activated Carbon. *Ind. Eng. Chem. Res.* **2006**, *45*, 5649−5656.

(38) Karapetian, K.; Jordan, K. D. *Water in Confined Environments*; Springer: New York, 2003.

(39) Sanfelix, P. C.; Holloway, S.; Kolasinski, K. W.; Darling, G. R. The Structure of Water on the (0001) Surface of Graphite. *Surf. Sci.* **2003**, *532*, 166−172.

(40) Dell, R. M.; Beebe, R. A. Heats of Adsorption of Polar Molecules on Carbon Surfaces. Ii. Ammonia and Methyl-Amine. *J. Phys. Chem.* **1955**, *59*, 754−762.

(41) Avgul, N. N.; Kiselev, A. V.; Lygina, I. A. The Adsorption Energies of Water, Alcohols, Ammonia and Methylamine on Graphite. *Bull. Acad. Sci. USSR, Div. Chem. Sci.* **1961**, *10*, 1308−1313.

(42) Klomkliang, N.; Kaewmanee, R.; Saimoey, S.; Intarayothya, S.; Do, D. D.; Nicholson, D. Adsorption of Water and Methanol on Highly Graphitized Thermal Carbon Black: The Effects of Functional Group and Temperature on the Isosteric Heat at Low Loadings. *Carbon* **2016**, *99*, 361−369.

(43) Karlicky, F.; Otyepkova, E.; Banas, P.; Lazar, P.; Kocman, M.; Otyepka, M. Interplay between Ethanol Adsorption to High-Energy Sites and Clustering on Graphene and Graphite Alters the Measured Isosteric Adsorption Enthalpies. *J. Phys. Chem. C* **2015**, *119*, 20535−20543.
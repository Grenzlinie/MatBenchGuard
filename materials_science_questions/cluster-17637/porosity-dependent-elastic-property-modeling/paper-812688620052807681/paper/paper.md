# Effect of porosity on energy harvesting performance of $0.5Ba(Ca_{0.8}Zr_{0.2})O_3 - 0.5(Ba_{0.7}Ca_{0.3})TiO_3$ ceramics: A numerical study

Saptarshi Karmakar, Raj Kiran, Vishal Singh Chauhan, Rahul Vaish*

Saptarshi Karmakar, Raj Kiran, Dr. Vishal Singh Chauhan, Dr. Rahul Vaish
School of Engineering, Indian Institute of Technology Mandi, Himachal Pradesh, 175005, India
E-mail: *Corresponding author email: rahul@iitmandi.ac.in

Keywords: Piezoelectricity, Porous, Energy Harvesting, Figure of merit

## Abstract
Finite element analysis was conducted on barium calcium zirconate titanate $0.5Ba(Ca_{0.8}Zr_{0.2})O_8 - 0.5(Ba_{0.7}Ca_{0.3})TiO_3$ (BCZT) material to investigate its energy harvesting performance at different porosities. Porosities were gradually increased to 25% in steps of 5. BCZT piezoceramics attached to a host cantilever beam in unimorph configuration and subjected to base vibration is considered for the present study. Both $d_{31}$ and $d_{33}$ modes were considered. Power was harvested using a load resistance optimized with the structure's natural frequency of vibration. Up to a certain porosity level, an increase in voltage and power was observed in the system. An increment in voltage by $\sim95\%$ in $d_{31}$ mode and $\sim119\%$ in $d_{33}$ mode was observed at 10% porosity. Power increased by 50% in $d_{31}$ mode and by 53% in $d_{33}$ mode at 5% porosity compared to the non-porous material.

## 1 Introduction
Piezoelectric materials are primarily used as sensors, actuators, and energy harvesters and can be used both in $d_{33}$ and $d_{31}$ mode. Recent advancement in electronics has led to the development of electronic devices which require extremely low-power for their operations$^{[1,2]}$. The energy harvesting devices may meet this low power requirement and therefore may be used as an auxiliary

This article has been accepted for publication and undergone full peer review but has not been through the copyediting, typesetting, pagination and proofreading process, which may lead to differences between this version and the Version of Record. Please cite this article as doi: 10.1002/ente.201901302.

This article is protected by copyright. All rights reserved

power source to these kinds of devices. Reasons like this are making energy harvesting devices a popular choice for low power devices. Various approaches to energy harvesting could be piezoelectric, electromagnetic, thermoelectric, etc. $^{[3]}$. Piezoelectric energy harvesters (PEH) convert mechanical energy to electrical energy by producing surface charges in response to the applied mechanical load $^{[4]}$ and can harvest small scale power from low-frequency ambient vibrations (between 0 to $100 ~Hz)^{[5]}$. Different piezoelectric materials used for energy harvesting applications like high energy density single crystals, polycrystalline ceramics, and polymeric piezoelectric materials, etc. are already reported in the literature $^{[5]}$. Priya et al. $^{[5]}$ reviewed different piezoelectric materials like lead zirconate titanate $Pb(Zr, Ti) O_{3}(PZT)$, Yttria stabilized zirconia (YSZ), $MgO$, $SrTiO_{3}, BaTiO_{3}$ for energy harvesting applications. Although lead-based piezoelectric ceramics is a very popular choice, lead's toxic nature has a very detrimental effect on human beings and the environment. Due to this reason, piezoelectric materials which are free from lead are encouraged $^{[6-8]}$. Examples of some popular lead-free piezoelectric materials are bismuth sodium titanate (BNT), bismuth potassium titanate (BKT), potassium sodium neonate (KNN), barium zirconate titanate- barium calcium titanate (BZT-BCT) also known as BCZT $^{[9]}$. Of all the lead-free piezoelectric materials mentioned above the piezoelectric coefficient of BCZT material is quite high $(d_{33} \sim 620$  pC/N) which makes BCZT a suitable choice for energy harvesting purposes $^{[10]}$. In recent studies, the introduction of porosity in the piezoelectric materials was found to enhance the piezoelectric energy harvesting capabilities of $PZT^{[11]}, KNLNTS^{[12]}$ piezoceramics. Carefully engineered porosity induced in piezoelectric materials has been found to decrease relative permittivity and increase the piezoelectric energy harvesting figure of merits (FOM's) $^{[11]}$. Zhang et al. $^{[13]}$ induced aligned porosity in PZT material which raised the energy density by about $374 \%$ at about $60 \%$ porosity by volume fraction. BCZT, a lead-free piezoelectric material, can be a promising material for energy harvesting applications due to its high value of the piezoelectric coefficient. The use of porous lead-free BCZT material is very limited in literature, therefore, exploring the possibilities of

This article is protected by copyright. All rights reserved

using them for energy harvesting applications can lead to interesting conclusions. Since no such study has been conducted so far, in the present study, a lead-free porous BCZT was studied using the finite element method for energy harvesting applications. Analytical methods can also be used to calculate the material properties, however, they are not effective when the inclusions are complex in shape, asymmetric and are randomly distributed. The finite element method, which is a numerical method, can easily deal with such a situation and is therefore used in the present study⁽¹⁴⁾.

To harvest ambient vibrational energy, a vibrating device is required. Different types of vibration devices like cantilever, cymbal, stack, shell, etc. are reported in the literature⁽¹⁵⁾. Roundy et al.⁽¹⁶⁾ suggested different ways of improving the power output of vibrating energy harvesting devices using PZT piezoceramics e.g. using resonance tuning of actuators, designing a structure with wide bandwidth design by designing a multi-degree of freedom system, etc. The present study focuses on using porous BCZT material with a cantilever type vibrating structure for energy harvesting. A finite element model (FE model) of a cantilever beam with a piezoelectric material attached to it in a unimorph configuration was developed and a finite element study was conducted. The effective piezoelectric properties of the porous BCZT material were taken from the literature ⁽¹⁷⁾ while the effective elastic properties were evaluated from the properties of the dense BCZT material using the homogenization technique. These properties were further used to calculate the energy harvested when the unimorph piezoelectric cantilever beam is subjected to base vibrations.

Zhang et. al.⁽¹³⁾ reported an increment in energy density with porosity in porous PZT ceramics prepared using freeze casting and the present study has been conducted using piezoelectric coefficient data of bulk BCZT from Zhang et. al.⁽¹⁷⁾. The present study, however, focuses on the numerical study of the effects of porosity on energy harvesting performance of porous BCZT material and has, therefore, did not consider the difference in the manufacturing method of the porous PZT ceramic⁽¹³⁾ and BCZT ceramic ⁽¹⁷⁾.

## 2 Materials and Methods

This article is protected by copyright. All rights reserved

Lead is a toxic material and is harmful to both humans and the environment. Although toxic, it is favored as a piezoelectric material due to its high piezoelectric coefficient $^{[18]}$. To address this issue it is important to search for lead-free piezoelectric material. Barium calcium zirconate titanate, having the chemical formula $0.5Ba(Ca_{0.8}Zr_{0.2})O_8 - 0.5(Ba_{0.7}Ca_{0.3})TiO_3$(BCZT) have a fairly high value of piezoelectric coefficient $^{[10,19]}$ and is therefore explored in the present study.

Zhang et al, $^{[17]}$, conducted experimental studies on porous BCZT ceramic material and correlated piezoelectric properties to their corresponding porosities. In the present study, the relative permittivity at $1\ kHz$ and piezoelectric coefficient data are taken from Zhang et al, $^{[17]}$ and Tuan et al, $^{[20]}$. However, errors in measuring the piezoelectric coefficient data mentioned in Zhang et. al. $^{[17]}$ have not been considered in the present study to reduce computational time. There may be some variations in the simulation results if these errors are taken into account. The piezoelectric properties of the material are shown in Figure 4 and are also mentioned in Table 1.

Densities at different porosities are calculated by applying mixture rule as given in the equation (1).

$$
\rho = \rho_m v_m + \rho_v v_v \tag{1}
$$

In the above equation $\rho$, $\rho_m$ and $\rho_v$ are the densities of the porous material, solid material, and the voids respectively. $v_m$ and $v_v$ are the volume fractions of the material and the voids respectively. Usually, the voids are likely to have trapped air whose density is very less compared to the density of the solid material and therefore can be neglected. Correspondingly the approximate density of the porous material is given by equation (2).

$$
\rho \approx \rho_m v_m \tag{2}
$$

Properties at porosities 5%, 10%, 15%, 20% and 25% are considered. However, it is to also to be noted here that porosity can affect various physical properties like reducing mechanical and electrical breakdown strength which may lead to fatigue and a low life cycle. These effects have not

This article is protected by copyright. All rights reserved

been considered in the present study and may be explored in future works. A finite element model of the host cantilever beam along with the piezoelectric material attached to the host cantilever beam in unimorph configuration was developed. The formulation requires the knowledge of stiffness and compliance coefficients of porous BCZT material at different porosities. Although properties of dense BCZT material are known, their properties at different porosities were not found in any literature. The effective properties of the porous BCZT material were calculated by doing finite element analysis of the representative volume element (RVE) of the porous BCZT material$^{[12]}$. During energy harvesting, the porous BCZT material is treated as homogeneous material whose properties are the effective properties of the porous BCZT material calculated from its representative volume element.

### 2.1 Calculation of effective stiffness coefficients

Effective properties of a porous BCZT material can be calculated numerically or analytically by treating the porous BCZT as a composite material having porous bubbles as inclusions. Various numerical and analytical studies were conducted to calculate the piezocomposite's effective properties $^{[21-24]}$. Analytical methods are not very useful when the inclusions in the matrix are of complex shapes. Finite element methods (which is a numerical method) can, however, be used to calculate the homogenized properties $^{[21,24,25]}$ using a unit cell (also referred to as a representative volume element or RVE) model. RVE is a material volume that is statistically representative of the infinitesimal neighborhood at that material point as was stated by Nemat-Nasser and Hori $^{[26]}$. RVE represents a homogeneous medium that can represent the original composite material. Material property calculated from the representative volume element reflects the material property of the entire material. This technique is also referred to as homogenization and is achieved by the micromechanical analysis of composite materials using the representative volume element$^{[27]}$. Berger et al,$^{[28]}$ used a micromechanical method to find the effective properties of piezoelectric fiber composites in terms of its constituents using an RVE or unit cell model analysis.

This article is protected by copyright. All rights reserved

The phenomenon in which a potential gradient is developed in the material in response to applied mechanical stress is referred to as direct piezoelectric effect. On the other hand, when an electric potential gradient causes a strain then it is called the converse piezoelectric effect. In either case, a linear relationship among the parameters is assumed. Problems of this kind are referred to as the coupled piezoelectric problem$^{[28]}$. Correspondingly the constitutive equation for this kind of problem is given by equation (3).

$$
\left\{\begin{array}{l}
T \\
D
\end{array}\right\}=\left[\begin{array}{cc}
C & -e^{t} \\
e & \varepsilon
\end{array}\right]\left\{\begin{array}{l}
S \\
E
\end{array}\right] \tag{3}
$$

The equation (3) relates stress vector $T$ and electrical displacements $D$ to strain $S$ and electric field $E$ . In the present work, the piezoelectric properties were referred to by Zhang et al,$^{[17]}$. Therefore, here it is not necessary to calculate the piezoelectric properties using RVE analysis. Only the stiffness coefficients are required to be determined. Therefore, in the present case equation (3) will reduce to

$$
\{T\}=[C]\{S\} \tag{4}
$$

The expanded form of the equation (4) is given in equation (5)

$$
\left\{\begin{array}{l}
\overline{T_{11}} \\
\overline{T_{22}} \\
\overline{T_{33}} \\
\overline{T_{23}} \\
\overline{T_{31}} \\
\overline{T_{12}}
\end{array}\right\}=\left[\begin{array}{llllll}
C_{11}^{e f f} & C_{12}^{e f f} & C_{13}^{e f f} & C_{14}^{e f f} & C_{15}^{e f f} & C_{16}^{e f f} \\
C_{21}^{e f f} & C_{22}^{e f f} & C_{23}^{e f f} & C_{24}^{e f f} & C_{25}^{e f f} & C_{26}^{e f f} \\
C_{31}^{e f f} & C_{32}^{e f f} & C_{33}^{e f f} & C_{34}^{e f f} & C_{35}^{e f f} & C_{36}^{e f f} \\
C_{41}^{e f f} & C_{42}^{e f f} & C_{43}^{e f f} & C_{44}^{e f f} & C_{45}^{e f f} & C_{46}^{e f f} \\
C_{51}^{e f f} & C_{52}^{e f f} & C_{53}^{e f f} & C_{54}^{e f f} & C_{55}^{e f f} & C_{56}^{e f f} \\
C_{61}^{e f f} & C_{62}^{e f f} & C_{63}^{e f f} & C_{64}^{e f f} & C_{65}^{e f f} & C_{66}^{e f f}
\end{array}\right]\left\{\begin{array}{l}
\overline{S_{11}} \\
\overline{S_{22}} \\
\overline{S_{33}} \\
\overline{S_{23}} \\
\overline{S_{31}} \\
\overline{S_{12}}
\end{array}\right\} \tag{5}
$$

The piezoelectric material is transversely isotropic due to which the number of independent elastic constants in the stiffness matrix of the equation (5) reduces to 11. The constitutive equation with the reduced stiffness matrix is given by

This article is protected by copyright. All rights reserved

$$
\left\{\begin{array}{l}
\overline{T}_{11} \\
\overline{T}_{22} \\
\overline{T}_{33} \\
\overline{T}_{23} \\
\overline{T}_{31} \\
\overline{T}_{12}
\end{array}\right\}=\left[\begin{array}{llllll}
C_{11}^{e f f} & C_{12}^{e f f} & C_{13}^{e f f} & 0 & 0 & 0 \\
C_{12}^{e f f} & C_{22}^{e f f} & C_{23}^{e f f} & 0 & 0 & 0 \\
C_{13}^{e f f} & C_{23}^{e f f} & C_{33}^{e f f} & 0 & 0 & 0 \\
0 & 0 & 0 & C_{44}^{e f f} & 0 & 0 \\
0 & 0 & 0 & 0 & C_{44}^{e f f} & 0 \\
0 & 0 & 0 & 0 & 0 & C_{66}^{e f f}
\end{array}\right]\left\{\begin{array}{l}
\overline{S}_{11} \\
\overline{S}_{22} \\
\overline{S}_{33} \\
\overline{S}_{23} \\
\overline{S}_{31} \\
\overline{S}_{12}
\end{array}\right\}
\tag{6}
$$

In the above equation (6) $\overline{T}_{i j}$ and $\overline{S}_{i j}$ are the average values of engineering stress and engineering strain. Equation (6) can be applied to composite as well as porous material. In the present case, the porous material is treated as composite material having voids as inclusions. Here it is assumed that all the voids are spherical. A schematic diagram of the representative volume element with several spherical voids is shown in Figure 1. The properties of the porous material are calculated from the properties of the bulk material by subjecting the RVE to suitable boundary conditions and finding the homogenized properties by calculating the volume average of the relevant stress and strain values over the entire volume of the RVE. Boundary conditions to be applied to calculate different coefficients are given in
Table 2. The homogenized properties are calculated from the average values of stress and strain averaged over the entire volume of the RVE. The volume average of stress and strain values are calculated using equation (7) and (8).

$$
\overline{T}_{i j}=\frac{1}{V} \int_{V} T_{i j} d V
\tag{7}
$$

$$
\overline{S}_{i j}=\frac{1}{V} \int_{V} S_{i j} d V
\tag{8}
$$

In equation (7) and (8) $v$ is the RVE's total volume, $T_{i j}$ and $S_{i j}$ are the stress and strain of each element and $\overline{T}_{i j} \overline{S}_{i j}$ are the volume average of the stress and strain averaged over the entire volume of the RVE.

### 2.1.1 Boundary Conditions

Composite materials are modeled as arrays of RVE arranged periodically, therefore it is necessary to impose periodic boundary conditions. Periodic boundary conditions ensure that the mode of deformation of all the RVEs remains the same. Application of periodic boundary conditions also ensures that two neighboring unit cells do not separate or overlap during deformation. In terms of Cartesian coordinates, this periodic boundary condition can be written as given in equation (9)

This article is protected by copyright. All rights reserved

$$
u_{i}=\overline{S}_{ij}x_{i}+v_{i} \tag{9}
$$

In equation (9) $\overline{S}_{ij}$ represents average strain, $v_{i}$ represents the periodic part of the displacement components on the boundary surface also referred to as local fluctuations and $x_{j}$ refers to the normal to a boundary surface. On the opposite boundary surfaces, displacements are given by equation (10) and (11).

$$
u_{i}^{K^{+}}=\overline{S}_{ij}x_{j}^{K^{+}}+v_{i}^{K^{+}} \tag{10}
$$

$$
u_{i}^{K^{-}}=\overline{S}_{ij}x_{j}^{K^{-}}+v_{i}^{K^{-}} \tag{11}
$$

In the above equation (10) and (11) the superscripts $K^{+}$ and $K^{-}$ indicate normal to the boundary surfaces in the positive and negative $x_{j}$ directions respectively. Due to periodic boundary conditions, the local fluctuations $v_{i}^{K^{+}}$ and $v_{i}^{K^{-}}$ are identical on two opposing faces. Therefore, subtracting equation (11) from the equation (10) we get

$$
u_{i}^{K^{+}}-u_{i}^{K^{-}}=\overline{S}_{ij}\left(x_{j}^{K^{+}}-x_{j}^{K^{-}}\right) \tag{12}
$$

The boundary condition in the equation (12) is applied to the opposite faces of the RVE to calculate the homogenized effective properties of the bulk material. Effective properties are calculated by applying boundary conditions in such a way that only a single strain field parameter in the equation (5) is nonzero while all other strain parameters are zero. The homogenized property depends upon the volume fraction of the inclusions. Therefore, it turns out that the size of the RVE does not matter much so the RVE is considered to be a unit cube with one of its corners at the origin.

### 2.1.2 Calculation of effective elastic constants $C_{11}^{eff}$ and $C_{22}^{eff}$

To find the effective elastic constants $C_{11}^{eff}$ and $C_{22}^{eff}$ the boundary conditions are applied in such a way that nonzero mechanical strain exists in the first direction, only along $x_{1}$, and mechanical strain

This article is protected by copyright. All rights reserved

in all other directions is zero. That is $\overline{S}_{11} \neq 0$ while all other quantities in the strain vector are zero.

The elastic constants $C_{11}^{eff}$ and $C_{22}^{eff}$ can then be calculated from the first two rows of the constitutive equation (5)

$$
C_{11}^{e f f}=\frac{\overline{T}_{11}}{\overline{S}_{11}} \tag{13}
$$

$$
C_{12}^{e f f}=\frac{\overline{T}_{22}}{\overline{S}_{22}} \tag{14}
$$

### 2.1.3 Calculation of elastic constants $C_{13}^{eff}$ and $C_{33}^{eff}$

In this case, the boundary conditions are applied in such a way that a nonzero mechanical strain is induced in the third direction $x_3$ while in all other directions they are zero. The elastic constants $C_{13}^{eff}$ and $C_{33}^{eff}$ can then be calculated from the first and third row of the constitutive equation (5). The calculated coefficients are given below.

$$
C_{13}^{e f f}=\frac{\overline{T}_{11}}{\overline{S}_{33}} \tag{15}
$$

$$
C_{33}^{e f f}=\frac{\overline{T}_{33}}{\overline{S}_{33}} \tag{16}
$$

### 2.1.4 Calculation of elastic constants $C_{44}^{eff}$ and $C_{66}^{eff}$

It can be observed from the equation (5) that the coefficients $C_{44}^{eff}$ and $C_{66}^{eff}$ relate the shear strains to their corresponding shear stresses in the planes $x_2 - x_3$, $x_3 - x_1$ and $x_1 - x_2$ respectively. Therefore, the boundary conditions are applied in a manner to create a pure shear condition in the corresponding plane. Therefore, to calculate the coefficients $C_{44}^{eff}$ and $C_{66}^{eff}$ the boundary conditions are applied in such a way that a state of the pure shear is achieved in planes $x_1 - x_3$ and $x_1 - x_2$. To avoid any kind of rigid body motion, the intersection between the planes upon which shear stresses are applied are generally kept fixed. The equations calculating the coefficients are given below.

This article is protected by copyright. All rights reserved

$$
C_{44}^{e f f}=\frac{\overline{T}_{31}}{\overline{S}_{31}} \tag{17}
$$

$$
C_{66}^{e f f}=\frac{\overline{T}_{12}}{\overline{S}_{12}} \tag{18}
$$

## 2.2 Piezoelectric Energy Harvester (PEH)

In the present study, a cantilever beam type host structure vibrates the piezoelectric material from which energy is harvested. A unimorph cantilever beam model is considered and is subjected to base excitation of $1 \times g$ acceleration, where $g$ is the acceleration due to gravity in earth's gravitational field. Electrodes can be arranged for three different modes operations viz. $d_{33}, d_{31}$ and $d_{15}$ mode $^{[29]}$. In $d_{31}$ mode, top and bottom electrodes (TBEs) are used while in $d_{33}$ mode interdigital electrodes (IDE) are used $^{[30]}$. In $d_{15}$ mode, poling and charge collection require different electrodes and often involve complex fabrication methods and are therefore not considered in the present study $^{[29]}$.

To do a comparative study between $d_{31}$ and $d_{33}$ mode the material volume in $d_{31}$ and $d_{33}$ mode are considered to be the same. Energy is harvested by subjecting the base of the cantilever to the vibration of magnitude $1 \times g$. Strains induced in the piezoelectric material due to vibration of the cantilever beam lead to the accumulation of charges on the piezoelectric material's surfaces from which electrical energy can be harvested.

## 2.3 Finite element model of the energy harvester

The response of the piezoelectric material attached to the host structure and subjected to base vibrations are modeled using the finite element method. The finite element method is an approximate but useful technique to calculate the response to the piezoelectric structure. Many researchers have already used this method to study the response of piezoelectric materials $^{[31-35]}$. Dynamic equation of motion, derived from shear deformation theory and piezoelectric constitutive laws are used to calculate the dynamic response of the unimorph cantilever beam. Shell elements,

This article is protected by copyright. All rights reserved

which are generalized and can easily take into account the curved features of the structure, were used to discretize the domain. The finite element equation of motion for an element can be written as $^{[12,36,37]}$

$$
\left[\begin{array}{cc}
M_{u u} & 0 \\
0 & 0
\end{array}\right]_{e}\left\{\begin{array}{l}
\ddot{u} \\
\ddot{\varphi}
\end{array}\right\}_{e}+\left[\begin{array}{cc}
C_{u u} & 0 \\
0 & 0
\end{array}\right]_{e}\left\{\begin{array}{l}
\dot{u} \\
\dot{\varphi}
\end{array}\right\}_{e}+\left[\begin{array}{cc}
K_{u u} & K_{u \varphi} \\
K_{\varphi u} & K_{\varphi \varphi}
\end{array}\right]_{e}\left\{\begin{array}{l}
u \\
\varphi
\end{array}\right\}_{e}=\left\{\begin{array}{c}
f^{e x t} \\
Q
\end{array}\right\}_{e} \tag{19}
$$

In equation (19) $M_{u u}$ is the mass matrix, $C_{u u}$ refers to the damping coefficient, $K_{u u}$ is the mechanical stiffness matrix, $K_{u \varphi}$ is the direct piezoelectric coupling matrix and $K_{\varphi \varphi}$ is the dielectric stiffness matrix. Also, note that the field variables $u_{e}$ and $\varphi_{e}$ represent the elemental displacement and electrical potential vector respectively at the nodes. Also $f_{e}^{e x t}$ is the external force vector and $q_{e}^{e x t}$ is the external electric charge for an element of the piezoelectric material. The elemental equations can be assembled to find the governing global equation given by

$$
\left[M_{u u}\right]\{\ddot{u}\}+\left[C_{u u}\right]\{\dot{u}\}+\left[K_{u u}\right]\{u\}+\left[K_{u \varphi}\right]\{\varphi\}=\{F\} \tag{20}
$$

$$
\left[K_{\varphi u}\right]\{u\}+\left[K_{\varphi \varphi}\right]\{\varphi\}=\{Q\} \tag{21}
$$

Assuming that no charges get accumulated on the surface of the electrodes, the voltage developed is calculated as

$$
\{\varphi\}=-\left[K_{\varphi \varphi}\right]^{-1}\left[K_{\varphi u}\right]\{u\} \tag{22}
$$

The current flowing through the circuit is given by

$$
i=-\frac{d Q}{d t} \tag{23}
$$

To harvest power, an external resistance is connected to the electrodes. The external resistance and the capacitance between the electrodes form a resistive capacitive or RC circuit. Correspondingly, the impedance is given by $z=\sqrt{X_{R}^{2}+X_{C}^{2}}$, where $X_{R}=R$ is the resistance of the external resistor and $X_{C}$ is the impedance provided by the capacitance between the electrodes. In terms of voltage and impedance, the current in the circuit is given by

This article is protected by copyright. All rights reserved

$$i = \frac{V}{z} \tag{24}$$

Differentiating equation (21) with respect to time we get

$$\frac{d}{dt}\left(\left[K_{\varphi u}\right]\{u\}+\left[K_{\varphi \varphi}\right]\{\varphi\}\right)=\frac{d}{dt}\{Q\} \tag{25}$$

Therefore, current flowing through the external resistance is given by

$$i=-\frac{d Q}{d t}=-\frac{d}{d t}\left(\left[K_{\varphi u}\right]\{u\}+\left[K_{\varphi \varphi}\right]\{\varphi\}\right) \tag{26}$$

Using equation (23) and (24), equation (25) can be modified as

$$\left[K_{\varphi u}\right]\{\dot{u}\}+\left[K_{\varphi \varphi}\right]\{\dot{\varphi}\}+\frac{V}{z}=0 \tag{27}$$

Equation (24) and (27) can be used to calculate the current and voltage produced from which power generated by the piezoelectric material can be calculated. Piezoelectric patches with different porosities varying from 0% to 25% by volume were considered. A unimorph cantilever beam host structure with a piezoelectric patch material attached to it was modeled using the above finite element formulation. Dirichlet boundary condition is applied to the beam by assigning zero values to the displacement field variable $u$ at the fixed end and zero values to the electrical potential field variable $\varphi$ across the entire beam length. Body load was applied as a boundary condition throughout the beam's length.

## 3 Results and Discussion

To harvest energy from the structure, the BCZT piezoelectric material is attached to a steel cantilever beam structure in an unimorph configuration as shown in Figure 2. The dimensions of the cantilever beam and the piezoelectric patch material attached to it in unimorph configuration are given in

Table 3.

Power is harvested by attaching an external load resistance of optimum value to the electrodes attached to the piezoelectric material. An optimum value of the resistance depends upon

This article is protected by copyright. All rights reserved

unimorph cantilever beam structure's natural frequency as well as on the capacitance between the electrodes. The optimum resistance is calculated using equation (28) where $C$ is the piezo capacitance and $R_{opt}$ is the optimum load resistance.

$$
R_{\mathrm{opt}}=\frac{1}{C \omega} \tag{28}
$$

The natural frequency depends upon the stiffness and density of the structure. Finite element analysis is used to calculate the homogenized properties of the RVE at different porosities and the corresponding effective stiffness coefficients are shown in **Figure 3**. The density of the porous material at various porosity levels can be calculated by mixture rule. In the $d_{31}$ mode, top and bottom electrodes (TBE) are used, while in $d_{33}$ mode interdigitated electrode (IDE) configuration is used$^{[29]}$ as shown in **Figure 2**. Power harvested in $d_{33}$ mode depends upon the relative arrangement of electrodes, electrode width and the gap maintained between them$^{[29]}$. In the $d_{33}$ mode having interdigital electrode configuration, number of electrodes, their width, and the gap between two adjacent electrodes are decided by performing a parametric study for the piezoelectric material at 0% porosity by varying the width and gap parameters. Parameters at which maximum power at 0% porosity was obtained was chosen for the study. Four electrodes were used having a width of 22.5 $mm$ and a gap of $\delta=20\ mm$ between them. Capacitance in $d_{31}$ mode can be calculated by the usual formula of capacitance

$$
C=\varepsilon_{0} \varepsilon_{r} \times(A / t) \tag{29}
$$

where $\varepsilon_{0}$ is the absolute permittivity of vacuum $\left(\varepsilon_{0}=8.85 \times 10^{-12} \mathrm{~F} / \mathrm{m}\right)$, $\varepsilon_{r}$ is the relative permittivity of the piezo-material, $A$ is the cross-sectional area of the electrodes plates and $t$ the separation between the electrodes. In the case of interdigitated electrode configuration in $d_{33}$ mode however, the capacitance can be expressed by a similar expression but after converting it to the top-bottom configuration from the interdigital configuration using conformal mapping$^{[38,39]}$. Due to different arrangements of electrodes in $d_{31}$ and $d_{33}$ mode, the capacitance differs. In the case of

This article is protected by copyright. All rights reserved

interdigital electrodes, the capacitance varies as the arrangement of electrodes varies relative to each other. In general capacitance in $d_{33}$ mode is always less than the capacitance in $d_{31}$ mode$^{[29]}$.

The effective piezoelectric and dielectric properties of the porous BCZT material at different porosities are taken from the literature$^{[17]}$ and are redrawn in **Figure 4**. It can be observed that all the effective properties decrease with an increase in porosity, which is quite obvious and can be explained by the rule of mixture. The dimensions of the cantilever beam are given in

**Table 3.**

Energy is harvested by subjecting the structure to base vibration. The energy harvesting is to be done from ambient vibration, therefore, a small proof mass of 15 $mg$ is attached to the free end of the cantilever beam to reduce the natural frequency of vibration of the structure. A finite element model of the system is developed and is subjected to base vibration. Vibration induced strain generates a voltage in the piezoelectric material. The generated voltage also referred to as open-circuit voltage, is calculated using equation (22) . Its variation in the frequency domain, both in $d_{31}$ and $d_{33}$ mode, is shown in **Figure 5**. **Figure 6** shows the variation of the maximum value of the open-circuit voltage with porosity. The voltage was found to increase up to 10% porosity and decreasing thereafter. The maximum value was attained at 10% porosity both in $d_{31}$ and $d_{33}$ mode. The higher voltage attained in $d_{33}$ mode can be attributed to the lower value of capacitance in $d_{33}$ mode compared to that in $d_{31}$ mode$^{[29]}$. Voltage increased by 95% from 181 V to 354 V at 10% porosity in case of $d_{31}$ mode of operation. In case of $d_{33}$ mode, the corresponding increase in voltage at 10% porosity is 119% from 607 V to 1330 V. This increment in open-circuit voltage with porosity can be explained by expressing the open-circuit voltage in terms of those homogenized properties of the piezoelectric material which changes with a change in the porosity of the piezoelectric material. Using the equation of electrical displacement $D = Q/A = d_{ij}\sigma_{j}$ , the charge accumulated on the electrodes is given by

This article is protected by copyright. All rights reserved

$$Q=A d_{i j} \sigma_{j} \tag{30}$$

where $D$ is the electrical displacement, $Q$ is the electrical charge accumulated, $A$ is the cross-sectional area of the electrodes, $d_{i j}$ is the piezoelectric coefficient and $\sigma_{j}$ is the stress developed in the piezoelectric material. In equation (30) index, $i$ denote the direction along which electrical properties are measured and index $j$ indicates the directions along which mechanical properties are measured. If $C$ be the capacitance between the electrodes, then the voltage developed between the electrodes is

$$V=Q / C \tag{31}$$

where $C$ is the capacitance. Substituting $Q$ from equation (30) into the equation (31) and using capacitance given by equation (29) the open-circuit voltage can be expressed as

$$V_{o c}=\frac{d_{i j} \sigma_{j} t}{\varepsilon_{0} \times \varepsilon_{r}} \tag{32}$$

where $d_{i j}$ is the piezoelectric coefficient, $\sigma_{j}$ is the bending stress developed in the cantilever beam $^{[40]}$.

Interdigital electrode configuration can be converted to top-bottom electrode configuration using conformal mapping $^{[38,39]}$ and a similar expression can be applied to calculate the open-circuit voltage. Applying Hooke's law $\sigma=E \varepsilon$ and substituting this in the equation (32), the open-circuit voltage can be expressed as

$$V_{o c}=\frac{d_{i j} E_{j} t}{\varepsilon_{0} \times \varepsilon_{r}} \times e_{s} \tag{33}$$

where $e_{s}$ is the strain developed in the material. In equation (33), as porosity changes, only piezoelectric coefficient $d_{i j}$, elastic modulus $E_{j}$ and relative permittivity $\varepsilon_{r}$ of the material changes with porosity. Therefore, open circuit voltage is proportional to the above quantities as given by equation (34)

$$V_{o c} \propto \frac{d \times E}{\varepsilon_{r}} \tag{34}$$

This article is protected by copyright. All rights reserved

Equation (34) physically means that open-circuit voltage varies depending upon relative variation of material properties $d$, $E$ and $\varepsilon_{r}$ . As porosity increases, piezoelectric coefficient $d$, Young's modulus $E$ and relative permittivity $\varepsilon_{r}$ all decrease, but if the rate of decrease in relative permittivity is higher than the rate of decrease that of the product of piezoelectric coefficient and Young's modulus, then open-circuit voltage increases with porosity otherwise it decreases. **Figure 7** shows the variation of the quantity $(d \times E / \varepsilon_{r})$ with porosity. According to equation (34) the open-circuit voltage developed should vary similarly as the quantity $(d \times E / \varepsilon_{r})$ varies with porosity. Comparing **Figure 6** and **Figure 7** it can be seen that they follow a similar pattern which confirms the validity of equation (34). This explains why open-circuit voltage increases with porosity up to 10% porosity and then decreases thereafter.

Next, the performance of porous BCZT in harvesting energy is explored. **Figure 8** shows the harvested power in the frequency domain and **Figure 9** shows the variation of maximum harvested power with porosity. To harvest power, the optimized load resistance is attached to the electrodes. Optimum resistance value depends upon the structure's natural frequency of vibration and capacitance between the electrodes and is given by equation (28). From **Figure 8** and **Figure 9** it can be seen that maximum power is attained at 5% porosity. In $d_{31}$ mode, power increased from 0.03 $W$ at 0% porosity to about 0.045 $W$ at 5% porosity which is about 50% increment in harvested power output. Similarly in $d_{33}$ mode, the harvested power increases from 0.017 $W$ at 0% porosity to about 0.026 $W$ at 5% porosity which is about 53% increment. The power in $d_{33}$ mode is less than that in $d_{31}$ mode because of the lower capacitance in $d_{33}$ mode compared to that in $d_{31}$ mode$^{[29]}$.

The increment in power at 5% porosity can be explained by expressing harvested power in terms of material properties which varies with porosity. Power can be expressed in terms of voltage and impedance as $P = V^{2}/Z$ . Using $X_{R}=R$ and $X_{C}=1/C\omega$ ($\omega=2\pi f$ is the structures natural frequency of vibration measured in $rad/s$) the impedance $Z$ can be calculated as $Z=\sqrt{X_{R}^{2}+X_{C}^{2}}$.

This article is protected by copyright. All rights reserved

Using optimum resistance from equation (28) and the expression of open-circuit voltage given by equation (34), power can be expressed as

$$
P_{\text {max }} \propto \frac{d^{2} \times E}{\varepsilon_{r}} \tag{35}
$$

Equation (35) physically means that variation of maximum power depends upon the variation of the square of piezoelectric coefficient $d$, Young's modulus of elasticity $E$ and relative permittivity $\varepsilon_{r}$.
All these physical quantities decrease with an increase in porosity, but if the rate of decrease of relative permittivity is greater than that of the product of the square of the piezoelectric coefficient and Young's modulus of elasticity, then maximum power will increase with porosity. The quantity $\left(d^{2} \times E\right) / \varepsilon_{r}$ is referred to as electromechanical coupling factor $(k^{2})$ also referred to as figure of merit and is given by equation (36)$^{[41]}$.

$$
F O M 1=k^{2}=\frac{d^{2} E}{\varepsilon_{r}} \tag{36}
$$

Figure 10 shows the variation of electromechanical coupling $k^{2}$ as a function of porosity volume fraction. Comparing Figure 9 and Figure 10 it can be observed that they follow a similar pattern which explains why power increases with porosity and attains a maximum value at a porosity level of 5%. From the above study, it can be seen that although the magnitude of voltage developed and the power output depends upon the physical dimensions of the beam and the boundary conditions applied, their trend of variation with porosity is independent of these quantities.

### 3.2 Assumptions and limitations of the numerical model

The finite element method is an approximate method of analysis and is applied to a lot of practical engineering problems. However, there are certain assumptions and limitations which have to be kept in mind. The present FEM model has been used to predict the effective properties, voltage and power output of porous piezo ceramic with varying degrees of porosity. The effective properties of the porous piezo composites are calculated using a unit cell model where it is assumed that the

This article is protected by copyright. All rights reserved

average properties of the unit cell represent the properties of the entire material as a whole.
Therefore, the use of the present method should be restricted to those cases where porosity is uniformly and homogeneously distributed throughout the material volume.

The ambient vibrations are assumed to be small and due to this, the loading level is also assumed to be very low so that the material can be safely assumed to be in linear piezoelectricity regime and Hooke's law has been applied⁽⁴⁾. The piezoelectric strip material attached to the beam is thin due to which plane stress condition has been assumed in the present study. Additionally, as the porosity is increased in the material, the mechanical and electrical breakdown strength will reduce leading to low life-cycle and high fatigue. The present model is limited to predict the effective properties, voltage, and power without considering the above factors.

Therefore, it is to be noted that the use of the present numerical model is limited to predicting the effective properties, voltage and power output of porous piezo-ceramic used as an energy harvester. However, it cannot address issues like mechanical and electrical breakdown strength, life cycle and fatigue life which are also important parameters.

## 4 Conclusion
Finite element analysis was carried out on porous BCZT material and its effective elastic properties are determined. RVE of the porous BCZT material was considered at different porosities and the effective properties were calculated by applying suitable boundary conditions. The effective piezoelectric properties at different porosities are taken from literature. The effective properties are then used to calculate and predict the voltage and the power that can be harvested from this material. Voltage was found to increase by 95% in $d_{31}$ mode and 119% in $d_{33}$ mode at 10% porosity compared to the non-porous material. The harvested power showed an increment of 50% and 53% in $d_{31}$ and $d_{33}$ modes respectively at 5% porosity. Therefore, it can be concluded that BCZT material having an optimum porosity level can be a good alternative to non-porous BCZT material as it is possible to harvest more power from a porous lightweight material.

This article is protected by copyright. All rights reserved

Received: ((will be filled in by the editorial staff))
Revised: ((will be filled in by the editorial staff))
Published online: ((will be filled in by the editorial staff))

## References

[1] C. R. Bowen, H. A. Kim, P. M. Weaver, S. Dunn, *Energy and Environmental Science* **2014**, 7, 25-44;

[2] R. Pandey, G. Vats, J. Yun, C. R. Bowen, A. W. Y. Ho-Baillie, J. Seidel, K. T. Butler, S. I. Seok, *Advanced Materials* **2019**, 31, 1-26.

[3] S. Priya, D. J. Inman, *Energy harvesting technologies*, Springer US, Boston, MA, **2009**.

[4] P. Paufler, *Vol. 199*, **2010**, pp. 158-158.

[5] S. Priya, H.-C. Song, Y. Zhou, R. Varghese, A. Chopra, S.-G. Kim, I. Kanno, L. Wu, D. S. Ha, J. Ryu, R. G. Polcawich, *Energy Harvesting and Systems* **2017**, 4, 3-39.

[6] R. Vaish, *International Journal of Applied Ceramic Technology* **2013**, 10, 682-689;

[7] G. Vats, R. Vaish, *Journal of Advanced Ceramics* **2013**, 2, 141-148;

[8] G. Vats, R. Vaish, *International Journal of Applied Ceramic Technology* **2014**, 11, 883-893.

[9] P. K. Panda, B. Sahoo, *Ferroelectrics* **2015**, 474, 128-143.

[10] W. Liu, X. Ren, *Physical Review Letters* **2009**, 103, 257602-257602.

[11] J. Roscow, Y. Zhang, J. Taylor, C. R. Bowen, *The European Physical Journal Special Topics* **2015**, 224, 2949-2966.

[12] R. Kiran, A. Kumar, V. S. Chauhan, Kumar, Rajeev, R. Vaish, *Journal of Electronic Materials* **2017**, 47, 233-241.

[13] Y. Zhang, M. Xie, J. Roscow, Y. Bao, K. Zhou, D. Zhang, C. R. Bowen, *Journal of Materials Chemistry A* **2017**, 5, 6569-6580.

[14] R. Kiran, A. Kumar, V. S. Chauhan, R. Kumar, R. Vaish, *Journal of Electronic Materials* **2018**, 47, 233-241.

[15] H. S. Kim, J. H. Kim, J. Kim, *International Journal of Precision Engineering and Manufacturing* **2011**, 12, 1129-1141.

[16] S. Roundy, E. S. Leland, J. Baker, E. Carleton, E. Reilly, E. Lai, B. Otis, J. M. Rabaey, V. Sundararajan, P. K. Wright, *IEEE Pervasive Computing* **2005**, 4, 28-36.

[17] Y. Zhang, M. Xie, J. Roscow, C. Bowen, *Materials Research Bulletin* **2019**, 112, 426-431.

[18] F. Li, D. Lin, Z. Chen, Z. Cheng, J. Wang, C. Li, Z. Xu, Q. Huang, X. Liao, L. Q. Chen, T. R. Shrout, S. Zhang, *Nature Materials* **2018**, 17, 349-354.

[19] Y. Nahas, A. Akbarzadeh, S. Prokhorenko, S. Prosandeev, R. Walter, I. Kornev, J. Íñiguez, L. Bellaiche, *Nature Communications* **2017**, 8.

[20] D. A. Tuan, N. T. Tinh, V. T. Tung, T. Van Chuong, *Materials Transactions* **2015**, 56, 1370-1373.

[21] P. Gaudenzi, *Computers & structures* **1997**, 65, 157-168;

This article is protected by copyright. All rights reserved

[22] M. Melnykowycz, X. Kornmann, C. Huber, M. Barbezat, A. J. Brunner, *Smart materials and structures* **2006**, *15*, 204-204;

[23] V. Tita, M. E. Moreno, V. Tita, F. D. Marques, 2005 ed;

[24] C. Poizat, M. Sester, *Computational Materials Science* **1999**, *16*, 89-97.

[25] J. L. Teply, G. J. Dvorak, *Journal of the Mechanics and Physics of Solids* **1988**, *36*, 29-58.

[26] S. Nemat-Nasser, M. Lori, S. K. Datta, *Journal of Applied Mechanics* **1996**, *63*, 561-561.

[27] P. M. Suquet, *Lecture notes in physics* **1985**, *272*, 193-193.

[28] H. Berger, S. Kari, U. Gabbert, R. Rodriguez-Ramos, J. Bravo-Castillero, R. Guinovart-Diaz, F. J. Sabina, G. A. Maugin, *Smart Materials and Structures* **2006**, *15*, 451-458.

[29] S. B. Kim, H. Park, S. H. Kim, H. C. Wikle, J. H. Park, D. J. Kim, *Journal of Microelectromechanical Systems* **2013**, *22*, 26-33.

[30] N. W. Hagood, R. Kindel, K. Ghandi, P. Gaudenzi, *Vol. 1917* (Eds.: N. W. Hagood, G. J. Knowles), International Society for Optics and Photonics, pp. 341-352.

[31] J. Kim, V. V. Varadan, V. K. Varadan, *International Journal for Numerical Methods in Engineering* **1997**, *40*, 817-832;

[32] S. Narayanan, V. Balamurugan, *Journal of Sound and Vibration* **2003**, *262*, 529-562;

[33] I. F. Pinto Correia, C. M. Mota Soares, C. A. Mota Soares, J. Herskovits, *Computers & Structures* **2002**, *80*, 2265-2275;

[34] X. G. Tan, L. Vu-Quoc, *International Journal for Numerical Methods in Engineering* **2005**, *64*, 1981-2013;

[35] C. Y. Wang, R. Vaicaitis, *Journal of Sound and Vibration* **1998**, *216*, 865-888.

[36] R. Kumar, B. K. Mishra, S. C. Jain, *Finite Elements in Analysis and Design* **2008**, *45*, 13-24;

[37] Z. Lašová, R. Zemčík, *Procedia Engineering* **2012**, *48*, 375-380.

[38] R. Igreja, C. J. Dias, *Sensors and Actuators, A: Physical* **2004**, *112*, 291-301;

[39] J. S. Wei, *IEEE Journal of Quantum Electronics* **1977**, *13*, 152-158.

[40] J. C. Park, J. Y. Park, Y. P. Lee, *Journal of Microelectromechanical Systems* **2010**, *19*, 1215-1222.

[41] R. Xu, S.-G. Kim, *PowerMEMS* **2012**, 464-467.

Figures

This article is protected by copyright. All rights reserved

![](./images/812688620052807681_1.jpg)

Figure 1: A typical RVE having voids as inclusion.

![](./images/812688620052807681_2.jpg)

Figure 2: Schematic of the operation modes of piezoelectric energy harvester (a) $d_{31}$ mode and (b) $d_{33}$ mode.

This article is protected by copyright. All rights reserved

![](./images/812688620052807681_3.jpg)

Figure 3: Variation of stiffness coefficients of porous BCZT material with porosity.

![](./images/812688620052807681_4.jpg)

Figure 4: Variation of (a) Piezoelectric coefficient and (b) Relative permittivity ($\varepsilon_r$) of porous BCZT material with volume fraction.

This article is protected by copyright. All rights reserved

![](./images/812688620052807681_5.jpg)

Figure 5: Open circuit voltage of porous BCZT material in frequency domain (a) $d_{31}$ mode and (b)
$d_{33}$ mode.

![](./images/812688620052807681_6.jpg)

Figure 6: Variation of maximum open-circuit voltage of porous BCZT material as a function of
volume fraction.

This article is protected by copyright. All rights reserved

![](./images/812688620052807681_7.jpg)

Figure 7: Variation of $(d \times E)/\varepsilon_{r}$ of porous BCZT material as a function of volume fraction.

![](./images/812688620052807681_8.jpg)

Figure 8: Power harvested from porous BCZT material at different porosities in frequency domain in (a) $d_{31}$ mode (b) $d_{33}$ mode.

This article is protected by copyright. All rights reserved

![](./images/812688620052807681_9.jpg)

Figure 9: Variation of maximum power harvested from porous BCZT material with porosity.

![](./images/812688620052807681_10.jpg)

Figure 10: Variation of electromechanical coupling $k^{2}$ for porous BCZT material as a function of volume fraction.

This article is protected by copyright. All rights reserved

Tables

Table 1: Variation of material properties with porosity

<table>
  <thead>
    <tr>
      <th>% age porosity</th>
      <th>$d_{31}$ ($pC/N$)</th>
      <th>$d_{33}$ ($pC/N$)</th>
      <th>$\varepsilon_{r}$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>298</td>
      <td>576</td>
      <td>5549</td>
    </tr>
    <tr>
      <td>5</td>
      <td>243</td>
      <td>508</td>
      <td>2591</td>
    </tr>
    <tr>
      <td>10</td>
      <td>195</td>
      <td>432</td>
      <td>1859</td>
    </tr>
    <tr>
      <td>15</td>
      <td>159</td>
      <td>388</td>
      <td>1661</td>
    </tr>
    <tr>
      <td>20</td>
      <td>116</td>
      <td>328</td>
      <td>1241</td>
    </tr>
    <tr>
      <td>25</td>
      <td>35</td>
      <td>283</td>
      <td>1034</td>
    </tr>
  </tbody>
</table>

Table 2: Boundary conditions and equations to express the effective elastic coefficients

<table>
  <thead>
    <tr>
      <th>Eff. Coeff.</th>
      <th>$A^{-}$<br>$(u_{i})$</th>
      <th>$A^{+}$<br>$(u_{i})$</th>
      <th>$B^{-}$<br>$(u_{i})$</th>
      <th>$B^{+}$<br>$(u_{i})$</th>
      <th>$C^{-}$<br>$(u_{i})$</th>
      <th>$C^{+}$<br>$(u_{i})$</th>
      <th>Formula</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$C_{11}^{eff}$</td>
      <td>0</td>
      <td>$u_{1}$</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>$\overline{T}_{11}/\overline{S}_{11}$</td>
    </tr>
    <tr>
      <td>$C_{12}^{eff}$</td>
      <td>0</td>
      <td>$u_{1}$</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>$\overline{T}_{22}/\overline{S}_{11}$</td>
    </tr>
    <tr>
      <td>$C_{13}^{eff}$</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>$u_{3}$</td>
      <td>$\overline{T}_{11}/\overline{S}_{33}$</td>
    </tr>
    <tr>
      <td>$C_{33}^{eff}$</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>$u_{3}$</td>
      <td>$\overline{T}_{33}/\overline{S}_{33}$</td>
    </tr>
    <tr>
      <td>$C_{44}^{eff}$</td>
      <td>$u_{3}$</td>
      <td>$u_{3}$</td>
      <td>0</td>
      <td>0</td>
      <td>$u_{1}$</td>
      <td>$u_{1}$</td>
      <td>$\overline{T}_{13}/\overline{S}_{13}$</td>
    </tr>
    <tr>
      <td>$C_{66}^{eff}$</td>
      <td>$u_{2}$</td>
      <td>$u_{2}$</td>
      <td>$u_{1}$</td>
      <td>$u_{1}$</td>
      <td>0</td>
      <td>0</td>
      <td>$\overline{T}_{12}/\overline{S}_{12}$</td>
    </tr>
  </tbody>
</table>

This article is protected by copyright. All rights reserved

Table 3: Dimensions of the cantilever host and piezoelectric patch material.

<table>
    <thead>
        <tr>
            <th colspan="3">Host Structure Dimensions (mm)</th>
            <th colspan="3">Piezoelectric Patch Dimensions (mm)</th>
        </tr>
        <tr>
            <th>Length</th>
            <th>Width</th>
            <th>Thickness</th>
            <th>Length</th>
            <th>Width</th>
            <th>Thickness</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>300</td>
            <td>10</td>
            <td>5</td>
            <td>150</td>
            <td>10</td>
            <td>5</td>
        </tr>
    </tbody>
</table>

TOC text

This study aims to study interactions between AgNPs and BSA using QCM-D coupled with electrochemistry. It comes out that the mass loss and the increase in dissipation in parallel with the electrochemical oxidation/reduction of AgNPs shows that albumin adsorption on AgNPs highly diminish electrochemical Ag/AgCl conversion. The formation of a less rigid Ag layer than the original MHP-AgNPs film is indicated.

![](./images/812688620052807681_11.jpg)

This article is protected by copyright. All rights reserved
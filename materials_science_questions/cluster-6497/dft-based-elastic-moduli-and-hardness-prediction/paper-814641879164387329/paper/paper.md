![](./images/814641879164387329_1.jpg)

Available online at www.sciencedirect.com

![](./images/814641879164387329_2.jpg)

Trans. Nonferrous Met. Soc. China 25(2015) 907-914

![](./images/814641879164387329_3.jpg)

# Modified embedded-atom interatomic potential for Co-W and Al-W systems

![](./images/814641879164387329_4.jpg)

Wei-ping DONG¹, Zheng CHEN², Byeong-Joo LEE³

1. College of Engineering, Zhejiang Normal University, Jinhua 321004, China;
2. State Key Laboratory of Solidification Processing, School of Materials Science and Engineering, Northwestern Polytechnical University, Xi'an 710072, China;
3. Department of Materials Science and Engineering, Division of Advanced Nuclear Engineering, Pohang University of Science and Technology (POSTECH), Pohang 790-784, Korea

Received 28 April 2014; accepted 13 July 2014

**Abstract:** A semi-empirical interatomic potential formalism, the second-nearest-neighbor modified embedded-atom method (2NN MEAM), has been applied to obtaining interatomic potentials for the Co-W and Al-W binary system using previously developed MEAM potentials of Co, Al and W. The potential parameters were determined by fitting the experimental data on the enthalpy of formation, lattice parameter, melting point and elastic constants. The present potentials generally reproduce the fundamental physical properties of the Co-W and Al-W systems accurately. The lattice parameters, the enthalpy of formation, the thermal stability and the elastic constants match well with experiment and the first-principles results. The enthalpy of mixing and the enthalpy of formation and mixing of liquid are in good agreement with CALPHAD calculations. The potentials can be easily combined with already-developed MEAM potentials for binary cobalt systems and can be used to describe Co-Al-W-based multicomponent alloys, especially for interfacial properties.

**Key words:** modified embedded-atom method; Co-W system; Al-W system; atomistic simulation

## 1 Introduction

The development of superalloys has been driven by the demand to increase the operating temperature of gas turbines serving in power plants and aircraft engines. Nowadays, various classes of superalloys are widely used including Fe-based, Co-based and Ni-based superalloys, among which the Ni-based superalloys strengthened with the L1₂ compound ($\gamma'$ phase) have been regarded as those with the highest heat resistance. Recently, however, SOTO et al [1] found a Co-based superalloy with outstanding high-temperature strength. Similar to Ni-based superalloys, the regularly aligned coherent cuboidal $\gamma'-Co_3(Al,W)$ (L1₂ structure) phase precipitates with $\gamma$-Co (disordered FCC structure) solid-solution phase. After that, many researchers have investigated the microstructures [2,3], mechanical properties [4-7], phase equilibria [8], structural stability and elastic properties [9,10], and the effect of a replacement of W by other elements, for example, Mo (or Ta), resulting in the precipitation of $\gamma'-Co_3(Al,Mo)$ (or $Co_3(Al,Ta)$) [11,12].

It should be emphasized here that the microstructure evolution is strongly affected by the interfacial properties during recrystallization and grain growth. Therefore, information on the $\gamma/\gamma'$ interfaces in Co-based superalloys, particularly their structure, energy, solute segregation and dynamics behavior, is highly required to gain a better understanding of the strengthening effect. However, all those interfacial properties are quantitatively hard to measure experimentally. And due to the size (or number of atoms) limit, it is often not possible to investigate precipitation behavior using only first-principles calculations. Another approach is to use (semi-) empirical interatomic potentials, which can deal with more than a million atoms and can calculate the interfacial energy and solute segregation rather easily.

Foundation item: Project (51274167) supported by the National Natural Science Foundation of China; Project (LQ14E010002) supported by the Zhejiang Provincial Natural Science Foundation of China; Project (2E24692) supported by the KIST Institutional Programs, Korea
**Corresponding author:** Wei-ping DONG; Tel: +86-18757606151; E-mail: penny1688@gmail.com
DOI: 10.1016/S1003-6326(15)63679-2

With the great need for large-scale atomistic simulations on Co-Al-W systems, one needs an interatomic potential model that can describe all the constituent elements and their alloy systems simultaneously using a common mathematical formalism. However, most of interatomic potential models are mainly for a single type or similar types of elements. From this point of view, the modified embedded-atom method (MEAM) [13] interatomic potential generalizing by LEE and BASKES [14,15] is highly applicable, because it can describe a wide range of elements (body-centered cubic (BCC), face-centered cubic (FCC), hexagonal close-packed (HCP), diamond and their alloy systems [16]. For Co-Al-W-based superalloys, the 2NN MEAM has already been applied to developing interatomic potentials for pure Co [17], Al [18], W [15] and Mo [15] as well as some other HCP elements, Ti and Zr [19], and Co-Al binary system [17] also reproduced very well and has also been successfully used for exploring many aspects of solid interfacial properties, especially the interfacial energy [17,20,21]. Therefore, one can say that the 2NN MEAM can be a suitable potential formalism to investigate the Co-based superalloys. Since all binary parameters are necessary to describe a Co-based multicomponent system, the development of Co-W and the Al-W binary potentials is required in order to realize atomistic simulations on the $\gamma$-Co/$\gamma'$-L1$_2$ interfacial properties. Such an effort is made in the present work.

## 2 Interatomic potential

### 2.1 Potential formalism

In the MEAM, the total energy of a system is given by

$$
E = \sum_{i} F_{i}(\bar{\rho}_{i})+\frac{1}{2} \sum_{j(\neq i)} S_{i j} \phi_{i j}\left(R_{i j}\right) \tag{1}
$$

where $F_i$ is the embedding function for an atom $i$ embedded in a background electron density $\bar{\rho}_i$, $S_{ij}$ and $\phi_{ij}(R_{ij})$ are the screening function and the pair interaction between atoms $i$ and $j$ separated by a distance $R_{ij}$. For energy calculations, the functional forms for $F_i$ and $\phi_{ij}$ should be given. The background electron density at each atomic site is computed considering the directionality of bonding, i.e., by combining several partial electron density terms for different angular contributions with weight factors $t^{(h)}(h=1-3)$. Each partial electron density is a function of atomic configuration and atomic electron density. The atomic electron densities $\rho^{a(h)}(h=0-4)$ are given as

$$
\rho^{a(h)}(R)=\rho_{0} \exp \left[-\beta^{(h)}\left(R / r_{\mathrm{e}}-1\right)\right] \tag{2}
$$

where $\rho_0$ is the atomic electron density scaling factor and $\beta^{(h)}$ are the decay lengths which are adjustable parameters, and $r_\mathrm{e}$ is the nearest-neighbor distance in the equilibrium reference structure. A specific form is given to the embedding function $F_i$, but not to the pair interaction $\phi_{ij}$. Instead, a reference structure where individual atoms are on the exact lattice points is defined and the total energy per atom of the reference structure is estimated from the zero-temperature universal equation of state of LEE et al [18]. Then, the value of the pair interaction is evaluated from the known values of the total energy per atom and the embedding energy, as a function of the nearest-neighbor distance. In the original MEAM [13], only first nearest-neighbor interactions are considered. Neglecting the second and more distant nearest-neighbor interactions is performed by the use of a strong, many-body screening function [19]. The consideration of the second nearest-neighbor interactions in the modified formalism is affected by adjusting the screening parameters, $C_\mathrm{min}$, so that the many-body screening becomes less severe. In addition, a radial cutoff function is applied to reducing the calculation time. Details of the (2NN) MEAM formalism have been published in the literatures [13-15,19] and will not be repeated here.

To describe binary alloy systems, the pair interaction between different elements should be determined. For this, a similar technique that is used to determine the pair interaction for pure elements is applied to binary alloy systems. For the Co-W and Al-W systems, the L1$_2$ Co$_3$W and B1 AIW ordered structures were chosen as the reference structures, respectively. In the L1$_2$ Co$_3$W structure, the total energy per atom (for 3/4Co atom+1/4W atom) is given as follows [22]:

$$
\begin{aligned}
E_{\mathrm{Co}_{3} \mathrm{W}}^{u}(R)= & \frac{3}{4} F_{\mathrm{Co}}\left(\bar{\rho}_{\mathrm{Co}}\right)+\frac{1}{4} F_{\mathrm{W}}\left(\bar{\rho}_{\mathrm{W}}\right)+ \\
& \frac{Z_{1}}{2}\left[\frac{1}{2} \phi_{\mathrm{CoCo}}(R)+\frac{1}{2} \phi_{\mathrm{CoW}}(R)\right]+ \\
& \frac{Z_{2}}{2}\left[\frac{3}{4} S_{\mathrm{Co}} \phi_{\mathrm{CoCo}}(a R)+\frac{1}{4} S_{\mathrm{W}} \phi_{\mathrm{WW}}(a R)\right]
\end{aligned} \tag{3}
$$

In the B1 AIW structure, the total energy per atom (for 1/2 Al atom + 1/2 W atom) is given as follows:

$$
\begin{aligned}
E_{\mathrm{AlW}}^{u}(R)= & \frac{1}{2}\left\{F_{\mathrm{Al}}\left(\bar{\rho}_{\mathrm{Al}}\right)+F_{\mathrm{W}}\left(\bar{\rho}_{\mathrm{W}}\right)+Z_{1} \phi_{\mathrm{AlW}}(R)+\right. \\
& \left.\frac{Z_{2}}{2}\left[S_{\mathrm{Al}} \phi_{\mathrm{AlAl}}(a R)+S_{\mathrm{W}} \phi_{\mathrm{WW}}(a R)\right]\right\}
\end{aligned} \tag{4}
$$

where $Z_1$ and $Z_2$ are the numbers of first and second nearest-neighbors. $S_\mathrm{Co}$, $S_\mathrm{Al}$ and $S_\mathrm{W}$ are the screening functions for the second nearest-neighbor interactions between Co atoms, between Al atoms and between W atoms, respectively, and $a$ is the ratio between the second

and first nearest-neighbor distances in the reference structure. The pair interaction between Co and W can now be obtained in the following form ($Z_1$ and $Z_2$ are 12 and 6 in the L1₂ Co₃W structure, respectively):

$$
\begin{aligned}
\phi_{\mathrm{CoW}}(R)= & \frac{1}{3} E_{\mathrm{Co}_{3} \mathrm{~W}}^{u}(R)-\frac{1}{4} F_{\mathrm{Co}}\left(\bar{\rho}_{\mathrm{Co}}\right)-\frac{1}{12} F_{\mathrm{W}}\left(\bar{\rho}_{\mathrm{W}}\right)- \\
& \phi_{\mathrm{CoCo}}(R)-\frac{3}{4} S_{\mathrm{Co}} \phi_{\mathrm{CoCo}}(a R)-\frac{1}{4} S_{\mathrm{W}} \phi_{\mathrm{WW}}(a R)
\end{aligned} \quad(5)
$$

The pair interaction between Al and W can now be obtained in the following form ($Z_1$ and $Z_2$ are 6 and 12 in the B1 AlW structure, respectively):

$$
\begin{aligned}
\phi_{\mathrm{AlW}}(R)= & \frac{1}{3} E_{\mathrm{AlW}}^{u}(R)-\frac{1}{6} F_{\mathrm{Al}}\left(\bar{\rho}_{\mathrm{Al}}\right)-\frac{1}{6} F_{\mathrm{W}}\left(\bar{\rho}_{\mathrm{W}}\right)- \\
& {\left[S_{\mathrm{Al}} \phi_{\mathrm{AlAl}}(a R)+S_{\mathrm{W}} \phi_{\mathrm{WW}}(a R)\right] }
\end{aligned} \quad(6)
$$

The embedding functions $F_{\mathrm{Co}}$, $F_{\mathrm{Al}}$ and $F_{\mathrm{W}}$ can be readily computed. The pair interactions $\phi_{\mathrm{CoCo}}$, $\phi_{\mathrm{AlAl}}$ and $\phi_{\mathrm{WW}}$ between the same types of atoms can also be computed from the descriptions of individual elements. To obtain $E_{\mathrm{Co}_{3} \mathrm{~W}}^{u}(R)$ and $E_{\mathrm{AlW}}^{u}(R)$, the universal equation of state [18] should be considered again as follows:

$$
E^{u}(R)=-E_{\mathrm{c}}\left(1+a^{*}+d a^{*^{3}}\right) \mathrm{e}^{-a^{*}} \quad(7)
$$

where $d$ is an adjustable parameter,

$$
a^{*}=\alpha\left(R / r_{\mathrm{e}}-1\right) \quad(8)
$$

and

$$
\alpha=\left(\frac{9 B \Omega}{E_{\mathrm{c}}}\right)^{1 / 2} \quad(9)
$$

where $E_{\mathrm{c}}$ is the cohesive energy. $B$ is the bulk modulus. $\Omega$ is the equilibrium atomic volume of the reference structure. The parameters $E_{\mathrm{c}}$, $r_{\mathrm{e}}$ (or $\Omega$), $B$ and $d$ of the L1₂ Co₃W or B1 AlW in the universal equation of state are determined from experimental data or high-level calculations. Then, the pair interaction between Co and W or Al and W is determined as a function of the interatomic distance $R$.

### 2.2 Determination of potential parameters for Co-W and Al-W binary systems
The MEAM for an alloy system is based on the MEAM potentials of the constituent elements. In the present work, the MEAM parameters are employed for Co [17], Al [18] and W [15] without any modification. The MEAM potential parameters for pure Co, Al and W are listed in Table 1.

As described in the previous section, the extension of the MEAM to an alloy system involves the determination of the pair interaction between different types of atoms. The main task is to estimate the potential parameters of the universal equation of state for the reference structure. Equations (7)-(9) show that the potential parameters are $E_{\mathrm{c}}$, $r_{\mathrm{e}}$ (or $\Omega$), $B$ and $d$. The first three are material properties if the reference structure is a real phase structure that exists on the phase diagram of the relevant system. Experimental data for that phase can be used directly. Otherwise, the parameter values should be optimized so that experimental information for other phases or high-level calculation results can be reproduced, if available, or assumptions should be made. The fourth parameter, $d$, is a model parameter. The value can be determined by fitting to the $(\partial B / \partial P)$ value of the reference structure. When the reference structure is not a real phase, it is difficult to estimate a reasonable value. For such alloy systems, $d$ is given as an average value of those for the pure constituent elements.

In addition to the parameters for the universal equation of state, two more model parameters, $C_{\min }$ and $C_{\max }$, must be determined to describe alloy systems. As can be seen in Table 1, each element has its own value of $C_{\min }$ and $C_{\max }$. $C_{\min }$ and $C_{\max }$ determine the extent of screening of an atom $(k)$ from the interaction between two neighboring atoms $(i$ and $j)$. For pure elements, the three atoms are all of the same type $(i-j-k=\mathrm{A}-\mathrm{A}-\mathrm{A}$ or $\mathrm{B}-\mathrm{B}-\mathrm{B})$. However, in the case of alloys, one of the interacting atoms and/or the screening atoms can be different types (there are four cases: $i-k-j=\mathrm{A}-\mathrm{B}-\mathrm{A}$, $\mathrm{B}-\mathrm{A}-\mathrm{B}$, $\mathrm{A}-\mathrm{A}-\mathrm{B}$ and $\mathrm{A}-\mathrm{B}-\mathrm{B}$). Different $C_{\min }$ and $C_{\max }$ values may have to be given in each case. Another model parameter is the atomic electron density scaling factor $\rho_{0}$. For an equilibrium reference structure $(R=r_{\mathrm{e}})$, the values of all atomic electron densities become $\rho_{0}$. This is an arbitrary value and does not have any effect on calculations for pure elements. This parameter is often omitted when describing the potential model for pure elements. However, for alloy systems, especially for systems where the composing elements have different

<table><caption>Table 1 2NN MEAM potential parameters for pure Co, Al and W (Reference structures are HCP Co, FCC Al and BCC W)</caption>
<thead>
<tr>
<th>Element</th>
<th>$E_{\mathrm{c}}/\mathrm{eV}$</th>
<th>$r_{\mathrm{e}}/\mathring{\mathrm{A}}$</th>
<th>$B/\mathrm{GPa}$</th>
<th>$A$</th>
<th>$\beta^{(0)}$</th>
<th>$\beta^{(1)}$</th>
<th>$\beta^{(2)}$</th>
<th>$\beta^{(3)}$</th>
<th>$t^{(1)}$</th>
<th>$t^{(2)}$</th>
<th>$t^{(3)}$</th>
<th>$C_{\mathrm{min}}$</th>
<th>$C_{\mathrm{max}}$</th>
<th>$d$</th>
</tr>
</thead>
<tbody>
<tr>
<td>Co$^{\mathrm{a}}$</td>
<td>4.41</td>
<td>2.50</td>
<td>194.8</td>
<td>0.9</td>
<td>3.50</td>
<td>0.0</td>
<td>0.0</td>
<td>4.0</td>
<td>3.00</td>
<td>5.00</td>
<td>−1.0</td>
<td>0.49</td>
<td>2.00</td>
<td>0.00</td>
</tr>
<tr>
<td>Al$^{\mathrm{b}}$</td>
<td>3.36</td>
<td>2.86</td>
<td>79.4</td>
<td>1.16</td>
<td>3.20</td>
<td>2.60</td>
<td>6.00</td>
<td>2.60</td>
<td>3.05</td>
<td>0.51</td>
<td>7.75</td>
<td>0.49</td>
<td>2.80</td>
<td>0.05</td>
</tr>
<tr>
<td>W$^{\mathrm{c}}$</td>
<td>8.66</td>
<td>2.740</td>
<td>314</td>
<td>0.40</td>
<td>6.54</td>
<td>1.00</td>
<td>1.00</td>
<td>1.00</td>
<td>−0.6</td>
<td>0.3</td>
<td>−8.7</td>
<td>0.49</td>
<td>2.80</td>
<td>0.00</td>
</tr>
</tbody>
<tfoot>
<tr>
<td colspan="15">$\mathrm{a}$Ref. [17], $\mathrm{b}$Ref. [18], $\mathrm{c}$Ref. [15]</td>
</tr>
</tfoot>
</table>

coordination numbers, the scaling factor (relative difference) has a great effect on calculations.

The 13 model parameters discussed above, $E_{\mathrm{c}}$, $r_{\mathrm{e}}$, $B$, $d$, $C_{\mathrm{min}}$, $C_{\mathrm{max}}$ and $\rho_{0}$ (there are four binary $C_{\mathrm{min}}$ and $C_{\mathrm{max}}$ parameters), must be determined to describe an alloy system. The optimization of the model parameters is performed by fitting known physical properties of the alloy system. The optimization of the model parameters is performed by fitting known physical properties of the alloy system. The parameter values are determined by a systematic trial and error method after the relations between individual parameters and target property values (mostly 0 K values) are found. Several sets of parameters that equally reproduce the target property values are obtained. Those parameter sets are used to calculate thermal properties or properties at finite temperatures such as stability of equilibrium phases, thermal expansion coefficients, order-disorder transition, and the best set is finally selected.

In the case of the Co-W system, the $\mathrm{L1}_{2}$ ordered $\mathrm{Co}_{3} \mathrm{~W}$ compound was arbitrarily chosen as the reference structure similarly in Ref. [23]. Since no experimental data were available for this compound, the potential parameters $E_{\mathrm{c}}$, $r_{\mathrm{e}}$ and $B$ that correspond to the cohesive energy, equilibrium nearestneighbor distance and bulk modulus of the $\mathrm{L1}_{2} \mathrm{Co}_{3} \mathrm{~W}$ phase, respectively, could not be determined directly. The $E_{\mathrm{c}}$ value was optimized that the experimental physical properties (the lattice parameter [24,25], the enthalpy of formation [26,27] and the melting point [25]) of $\mathrm{DO}_{19}$ $\mathrm{Co}_{3} \mathrm{~W}$ structure are best reproduced simultaneously. The value of $r_{\mathrm{e}}$ was optimized from volume equation $\Omega_{\mathrm{Co}_{3} \mathrm{~W}}=$ $0.75 \Omega_{\mathrm{Co}}+0.25 \Omega_{\mathrm{W}}$. The $B$ and $d$ values were approximated by taking a weighted average of the values for pure elements [17,23,28-31]. Therefore, in the present work, the values of $B$ and $d$ of the reference structure $\left(\mathrm{Co}_{3} \mathrm{~W}\right)$ were a weighted average (3:1) of those for pure Co and W. The atomic electron density scaling factor $\rho_{0}$ values for Co and W were temporarily assumed to be the same, i.e., the ratio is 1:1. The eight $C_{\mathrm{min}}$ and $C_{\mathrm{max}}$ parameters were adjusted to better reproduce the experimental physical properties of $\mathrm{DO}_{19} \mathrm{Co}_{3} \mathrm{~W}$ structure. Table 2 shows the finally determined MEAM potential parameter sets for the Co-W binary system.

In the case of the Al-W system, the B1 AIW compound is the reference structure because the existent I26- $\mathrm{Al}_{22} \mathrm{~W}$, hP12- $\mathrm{Al}_{5} \mathrm{~W}$ and $\mathrm{mC} 30-\mathrm{Al}_{4} \mathrm{~W}$ structures are too complex. So the potential parameters $E_{\mathrm{c}}$, $r_{\mathrm{e}}$ and $B$ could not be determined directly. The experimental physical properties of the I26- $\mathrm{Al}_{22} \mathrm{~W}$, hP12- $\mathrm{Al}_{5} \mathrm{~W}$ and $\mathrm{mC} 30-\mathrm{Al}_{4} \mathrm{~W}$ structures, which are available in literature and can thus be used to determine potential parameter values, were structure [32], lattice parameter [24,33], the enthalpy of formation [33,34] and melting point [24]. The $E_{\mathrm{c}}$ was given as a default value. The $B$, $r_{\mathrm{e}}$ and $d$ values were also approximated by taking a weighted average of the values for pure elements and $\rho_{0}$ was 1 . The four $C_{\max }$ parameters were given default values, but four $C_{\text {min }}$ were adjusted to better reproduce the lattice parameter, the enthalpy of formation and elastic constants of $\mathrm{cl} 26-\mathrm{Al}_{22} \mathrm{~W}$ structure. Table 2 shows the finally determined MEAM potential parameter sets for the Al-W binary system.

<table>
<caption>Table 2 2NN MEAM potential parameters for Co-W and Al-W systems</caption>
<thead>
<tr>
<th>Parameter</th>
<th>Co-W</th>
<th>Al-W</th>
</tr>
<tr>
<th>Reference state</th>
<th>L1₂-Co₃W</th>
<th>B1-AIW</th>
</tr>
</thead>
<tbody>
<tr>
<td>$E_{\mathrm{c}}/\mathrm{eV}$</td>
<td>$0.75E_{\mathrm{c}}^{\mathrm{Co}}+0.25E_{\mathrm{c}}^{\mathrm{W}}-0.05$</td>
<td>$0.5E_{\mathrm{c}}^{\mathrm{Al}}+0.5E_{\mathrm{c}}^{\mathrm{W}}+0.45$</td>
</tr>
<tr>
<td>$r_{\mathrm{e}}/\mathring{\mathrm{A}}$</td>
<td>2.5872</td>
<td>2.4916</td>
</tr>
<tr>
<td>$B/\mathrm{GPa}$</td>
<td>$0.75B^{\mathrm{Co}}+0.25B^{\mathrm{W}}$</td>
<td>$0.50B^{\mathrm{Al}}+0.50B^{\mathrm{W}}$</td>
</tr>
<tr>
<td>$d$</td>
<td>$0.75d^{\mathrm{Co}}+0.25d^{\mathrm{W}}$</td>
<td>$0.5d^{\mathrm{Al}}+0.5d^{\mathrm{W}}$</td>
</tr>
<tr>
<td>$\rho_{0}^{\mathrm{A}}:\rho_{0}^{\mathrm{B}}$</td>
<td>1:1</td>
<td>1:1</td>
</tr>
<tr>
<td>$C_{\mathrm{min}}(\mathrm{A-B-A})$</td>
<td>$0.49(=C_{\mathrm{min}}^{\mathrm{Co}})$</td>
<td>0.81</td>
</tr>
<tr>
<td>$C_{\mathrm{min}}(\mathrm{B-A-B})$</td>
<td>$0.49(=C_{\mathrm{min}}^{\mathrm{W}})$</td>
<td>0.36</td>
</tr>
<tr>
<td>$C_{\mathrm{min}}(\mathrm{A-A-B})$</td>
<td>1.21</td>
<td>2.0</td>
</tr>
<tr>
<td>$C_{\mathrm{min}}(\mathrm{A-B-B})$</td>
<td>1.21</td>
<td>2.0</td>
</tr>
<tr>
<td>$C_{\mathrm{max}}(\mathrm{A-B-A})$</td>
<td>1.44</td>
<td>$2.80(=C_{\mathrm{max}}^{\mathrm{Al}})$</td>
</tr>
<tr>
<td>$C_{\mathrm{max}}(\mathrm{B-A-B})$</td>
<td>1.44</td>
<td>$2.80(=C_{\mathrm{max}}^{\mathrm{W}})$</td>
</tr>
<tr>
<td>$C_{\mathrm{max}}(\mathrm{A-A-B})$</td>
<td>2.8</td>
<td>$[0.5(C_{\mathrm{max}}^{\mathrm{Al}})^{1/2}+0.5(C_{\mathrm{max}}^{\mathrm{W}})^{1/2}]^{2}$</td>
</tr>
<tr>
<td>$C_{\mathrm{max}}(\mathrm{A-B-B})$</td>
<td>2.8</td>
<td>$[0.5(C_{\mathrm{max}}^{\mathrm{Al}})^{1/2}+0.5(C_{\mathrm{max}}^{\mathrm{W}})^{1/2}]^{2}$</td>
</tr>
</tbody>
<tfoot>
<tr>
<td colspan="3">Reference structures are L1₂-Co₃W and B1-AIW</td>
</tr>
</tfoot>
</table>

## 3 Calculation of physical properties and discussion

In this section, in order to evaluate the reliability of the potentials determined by the above procedure, the fundamental physical properties of the Co-W and Al-W alloy systems calculated using the MEAM potentials, and compared with experimental information and first-principles calculations. The 2NN MEAM formalism includes up to second nearest-neighbor interactions. Therefore, the radial cutoff distance during atomistic simulations should be larger than the second nearest-neighbor distance in the structures under consideration. All calculations presented here are those performed with a radial cutoff distance of 4.5 Å whose size is between the second and third nearest-neighbor distances of Co or Al. The number of atoms in samples was at least 2000, and relaxation of the sample dimensions was allowed into all directions. In the case of calculations at non-zero temperatures, the given temperature was maintained by a velocity rescaling method.

The fundamental physical properties of the Co-W and Al-W alloys calculated using the present 2NN MEAM potential listed in Tables 3-5 are presented in this section and compared with experimental data and other calculations [24-27,33-35]. But as the crystallographic structures of the Co-W and Al-W alloys are very complicated, the literature data which can be compared with are very little. An ideal interatomic potential for an alloy system would be the one that can correctly reproduce physical properties (thermodynamic, structural and elastic properties, etc.) of all solution and intermediate phases relevant to the system. Therefore, attention was paid to whether the present potential can describe the above-mentioned alloy properties correctly.

<table>
<caption>Table 3 Lattice parameters of Co₃W, Al₁₂W, Al₅W and Al₄W calculated using present (2NN) MEAM potentials, in comparison with experimental data and first-principles calculations (unit: Å)</caption>
<thead>
  <tr>
    <th>Phase</th>
    <th>Lattice parameter</th>
    <th>Expt.</th>
    <th>2NN MEAM</th>
    <th>FP calc.</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td rowspan="2">Co₃W(<i>P63/mmc</i>)</td>
    <td>a</td>
    <td>5.12¹), 5.13²)</td>
    <td>5.19</td>
    <td>5.116³)</td>
  </tr>
  <tr>
    <td>c</td>
    <td>4.12¹), 4.13²)</td>
    <td>4.18</td>
    <td>4.098³)</td>
  </tr>
  <tr>
    <td>Co₃W(<i>Pm3̄m</i>)</td>
    <td>a</td>
    <td></td>
    <td>3.659</td>
    <td>3.598³)</td>
  </tr>
  <tr>
    <td>Al₁₂W(cI26)</td>
    <td>a</td>
    <td>7.580¹)</td>
    <td>7.736</td>
    <td>7.582⁴), 7.480⁴)</td>
  </tr>
  <tr>
    <td rowspan="2">Al₅W(hP12)</td>
    <td>a</td>
    <td>4.902¹)</td>
    <td>4.765</td>
    <td></td>
  </tr>
  <tr>
    <td>c</td>
    <td>8.857¹)</td>
    <td>8.729</td>
    <td></td>
  </tr>
  <tr>
    <td rowspan="3">Al₄W(mC30)</td>
    <td>a</td>
    <td>5.272¹)</td>
    <td>5.153</td>
    <td></td>
  </tr>
  <tr>
    <td>b</td>
    <td>17.771¹)</td>
    <td>17.465</td>
    <td></td>
  </tr>
  <tr>
    <td>c</td>
    <td>5.218¹)</td>
    <td>5.227</td>
    <td></td>
  </tr>
</tbody>
</table>
¹) Ref. [24], ²) Ref. [25], ³) Ref. [35], ⁴) Ref. [33]

<table>
<caption>Table 4 Enthalpy of formation of Co₃W, Al₁₂W, Al₅W and Al₄W calculated using present 2NN MEAM potentials in comparison with literature data (unit: kJ/(g·atom))</caption>
<thead>
  <tr>
    <th>Phase</th>
    <th>Expt.</th>
    <th>2NN MEAM</th>
    <th>FP calc.</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td rowspan="2">Co₃W(<i>P63/mmc</i>)</td>
    <td>−3.8¹), −2.0¹),</td>
    <td rowspan="2">−7.78</td>
    <td>−1¹), −7.72²),</td>
  </tr>
  <tr>
    <td>−4.8²)</td>
    <td>−10.303⁴)</td>
  </tr>
  <tr>
    <td>Co₃W(<i>Pm3̄m</i>)</td>
    <td></td>
    <td>−4.8</td>
    <td>−4.8²), −6.637⁴)</td>
  </tr>
  <tr>
    <td>Al₁₂W(cI26)</td>
    <td></td>
    <td>−5.10</td>
    <td>−7.31⁵), −8.46⁵)</td>
  </tr>
  <tr>
    <td>Al₅W(hP12)</td>
    <td></td>
    <td>−21.15</td>
    <td></td>
  </tr>
  <tr>
    <td>Al₄W(mC30)</td>
    <td>−14.33³)</td>
    <td>−11.83</td>
    <td></td>
  </tr>
</tbody>
</table>
¹) Ref. [26], ²) Ref. [27], ³) Ref. [34], ⁴) Ref. [35], ⁵) Ref. [33]

Two compounds DO₁₉-Co₃W(<i>Pm3̄m</i>) and L1₂-Co₃W(<i>P63/mmc</i>) of Co-W alloys and three intermediate compounds Al₁₂W(cI26), Al₅W(hP12) and Al₄W(mC30) of Al-W system appearing on the phase diagram were investigated using the present 2NN MEAM potential. The calculated lattice parameters of Co₃W, Al₁₂W, Al₅W and Al₄W were compared with experimental data and first-principles calculations in Table 3. It is shown that the lattice parameters match well with the experiment [24,25] and the first-principles [33,35] results. Concerning the enthalpy of formation of those structures, the results are compared with available other data [26,27,33-35] in Table 4. Figures 1 and 2 show that the enthalpy of mixing of BCC Co-W (at 0 K), the enthalpy of formation and mixing of liquid Co-W, the enthalpy of mixing of BCC Al-W (at 300 K) and the enthalpy of formation and mixing of liquid Al-W are in good agreement with CALPHAD calculations even though there are small deviations.

<table>
<caption>Table 5 Elastic constants of Al₁₂W calculated using present 2NN MEAM potentials, in comparison with literature data (unit: GPa)</caption>
<thead>
  <tr>
    <th>Phase</th>
    <th>Method</th>
    <th>C₁₁</th>
    <th>C₁₂</th>
    <th>C₄₄</th>
    <th>B</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td rowspan="3">Al₁₂W</td>
    <td>Present work</td>
    <td>131</td>
    <td>72</td>
    <td>47</td>
    <td>92</td>
  </tr>
  <tr>
    <td>FP calc. ¹)</td>
    <td>150</td>
    <td>47</td>
    <td>56</td>
    <td>82</td>
  </tr>
  <tr>
    <td>FP calc. ¹)</td>
    <td>168</td>
    <td>56</td>
    <td>61</td>
    <td>93</td>
  </tr>
</tbody>
</table>
¹) Ref. [33]

As a further means to examine the reliability of the present potentials, the elastic constants of Al₁₂W were calculated and compared with available literature data [33] (see Table 5). Calculated elastic constants of Al₁₂W are also in good agreement with relevant first-principles calculation data. In order to confirm the robustness of the potentials developed, the structural stability of stable compound phases needs to be confirmed at finite temperatures up to melting points. Therefore, those

![](./images/814641879164387329_5.jpg)

Fig. 1 Calculated physical properties of Co-W system using present 2NN MEAM potential in comparison with CALPHAD results:
(a) Enthalpy of mixing of BCC Co-W (at 0 K); (b) Enthalpy of formation and mixing of liquid Co-W

![](./images/814641879164387329_6.jpg)

Fig. 2 Calculated physical properties of Al-W system using present 2NN MEAM potential in comparison with CALPHAD results:
(a) Enthalpy of mixing of BCC Al-W (at 300 K); (b) Enthalpy of formation and mixing of liquid Al-W

parameter sets were also used to calculate thermal stability of $DO_{19}$-$Co_3W$ and $Al_{12}W$. For $DO_{19}$-$Co_3W$, our calculation result of transition temperature 2200 K (including superheating) is higher than that 1391-1987 K in Ref. [25]. For $Al_{12}W$, our result of transition temperature 1300 K (including superheating) is also higher than that (900 K) in Ref. [25]. That means that the thermal stability as well as other properties of $DO_{19}$-$Co_3W$ and $Al_{12}W$ are in good agreement with literature data.

It has been shown that the present 2NN MEAM potentials for the Co-W and Al-W binary systems can reproduce most of the fundamental physical properties of the alloy systems considered reasonably well. That means the potentials can be used to examine the interfacial properties, alloying elements and interface segregation for practical $Co/Co_3(Al$, W, Ta or Mo) multicomponent alloys. Describing interatomic potentials of a wide range of elements using a common potential formalism and being able to deal with various alloy systems easily is the strongest point of the present (2NN) MEAM potential formalism. It should be noted here that the interatomic potentials are already available for Co-Al [17] binary system and all the additional alloying elements Ta [15] and Mo [15] based on the same formalism. It should be possible to extend the present interatomic potential into Co-based superalloys, e.g., Co-Al-W, to investigate the interfacial propertites, the misfit strain energy between $Co_3(Al,W)$ and Co matrix, the size distributions or the shape of the $\gamma'$ precipitates, and the interactions between the precipitates and dislocations, grain boundaries or other defects.

## 4 Conclusions
1) Considering that the Co-Al-W-based alloys are still in their early stages of development and have high potential for improvement, this research will provide the fundamental knowledge for developing the new generation Co-based superalloys.

2) It has been shown that the presently developed 2NN MEAM potentials for the Co-W and Al-W binary

systems can reproduce various fundamental physical properties of Co-W and Al-W systems reasonably well. Structural properties (enthalpy of formation and lattice parameter) of the Co-W and Al-W systems are in good agreement with experiment and the first-principles results. Elastic properties (bulk modulus and elastic constants) of $Al_{12}W$ are also in good agreement with relevant first-principles calculation data. Thermal properties (melting points) are comparable with literature data. The enthalpy of mixing and the enthalpy of formation and mixing of liquid of the Co-W and Al-W systems match well with CALPHAD calculations.

3) The potentials can be easily combined with already-developed MEAM potentials for the multicomponent Co-Al-W-based systems, and can be used for atomistic studies on the behavior of the interfacial properties, alloying elements and interface segregation for $\gamma/\gamma'$ interface.

## References

[1] SATO J, OMORI T, OIKAWA K, OHNUMA I, KAINUMA R, ISHIDA K. Cobalt-base high-temperature alloys [J]. Science, 2006, 312: 90-91.

[2] PING D H, CUI C Y, GU Y F, HARADA H. Microstructure of a newly developed $\gamma'$ strengthened Co-base superalloy [J]. Ultramicroscopy, 2007, 107: 791-795.

[3] OOHASHI T, OKAMOTO N L, KISHIDA K, TANAKA K, INUI H. Microstructures and mechanical properties of $Co_3(Al,W)$ with the L1₂ structure [J]. Materials Research Society, 2009, 1128: 1-6.

[4] SUZUKI A, POLLOCK T M. High-temperature strength and deformation of $\gamma/\gamma'$ two-phase Co-Al-W-base alloys [J]. Acta Materialia, 2008, 56: 1288-1297.

[5] POLLOCK T M, DIBBERN J, TSUNEKANE M, ZHU J, SUZUKI A. New Co-based $\gamma-\gamma'$ high-temperature alloys [J]. JOM, 2010, 62: 58-63.

[6] CHEN M, WANG C Y. First-principles study of the partitioning and site preference of Re or Ru in Co-based superalloys with $\gamma/\gamma'$ interface [J]. Physics Letters A, 2010, 374: 3238-3242.

[7] XU Yang-tao, XIA Tian-dong, ZHAO Wen-jun, WANG Xiao-jun. Microstructure and wear resistance of TIG cladding novel Co-9Al-7.5W superalloy [J]. The Chinese Journal of Nonferrous Metals, 2013, 23: 1019-1026.

[8] KOBAYASHI S, TSUKAMOTO Y, TAKASUGI T, CHINEN H, OMORI T, KIYOHITO I, ZAEFFERER S. Determination of phase equilibria in the Co-rich Co-Al-W ternary system with a diffusion- couple technique [J]. Intermetallics, 2009, 17: 1085-1089.

[9] YAO Q, XING H, SUN J. Structural stability and elastic property of the L1₂ ordered $Co_3(Al,W)$ precipitate [J]. Applied Physics Letters, 2006, 89: 161906.

[10] TANAKA K, OHASHI T, KISHIDA K, INUI H. Single-crystal elastic constants of $Co_3(Al,W)$ with the L1₂ structure [J]. Applied Physics Letters, 2007, 91: 181907.

[11] LI H, SHA J B, LI S S. Microstructures and mechanical properties of alloys Co-9Al-(9-x)W-xMo-2Ta-0.02B at room and high temperature [J]. Acta Aeronautica et Astronautica Sinica, 2011, 32(6): 1139-1146.

[12] SAMIMI P, LIU Y, Ghamarian I, SONG J, COLLINS P C. New observations of a nanoscaled pseudomorphic bcc Co phase in bulk Co-Al-(W,Ta) superalloys [J]. Acta Materialia, 2014, 69: 92-104.

[13] BASKES M I. Modified embedded-atom method potentials for cubic materials and impurities [J]. Physical Review B, 1992, 46: 2727-2742.

[14] LEE B J, BASKES M I. Second nearest-neighbor modified embedded-atom method potential [J]. Physical Review B, 2000, 62: 8564-8567.

[15] LEE B J, BASKES M I, KIM H, CHO Y K. Second nearest-neighbor modified embedded atom method potentials for BCC transition metals [J]. Physical Review B, 2001, 64: 184102.

[16] LEE B J, KO W S, KIM H K, KIM E H. The modified embedded-atom method interatomic potentials and recent progress in atomistic simulations [J]. CALPHAD, 2010, 34: 510-522.

[17] DONG W P, KIM H K, KO W S, LEE B M, LEE B J. Atomistic modeling of pure Co and Co-Al system [J]. CALPHAD, 2012, 38: 7-16.

[18] LEE B J, SHIM J H, BASKES M I. Semi-empirical atomic potentials for the FCC metals Cu, Ag, Au, Ni, Pd, Pt, Al and Pb based on first and second nearest neighbor modified embedded atom method [J]. Physical Review B, 2003, 68: 144112.

[19] KIM Y M, LEE B J, BASKES M I. Modified embedded-atom method interatomic potentials for Ti and Zr [J]. Physical Review B, 2006, 74: 014101.

[20] SILVA A C, ÅGREN J, CLAVAGUERA-MORA M T, DJUROVIC D, GOMEZ-ACEBO T, LEE B J, LIU Z K, MIODOWNIK P, SEIFERT H J. Applications of computational thermodynamics—The extension from phase equilibrium to phase transformations and other properties [J]. CALPHAD, 2007, 31: 53-74.

[21] KIM H K, JUNG W S, LEE B J. Modified embedded-atom method interatomic potentials for the Fe-Ti-C and Fe-Ti-N ternary systems [J]. Acta Materialia, 2009, 57: 3140-3147.

[22] LEE B J, SHIM J H. A modified embedded atom method interatomic potential for the Cu-Ni system [J]. CALPHAD, 2004, 28: 125-132.

[23] SA I Y, LEE B J. Modified embedded-atom method interatomic potentials for the Fe-Nb and Fe-Ti binary systems [J]. Scripta Materialia, 2008, 59: 595-598.

[24] VILLARS P, CALVERT L D. Pearson's handbook of crystallographic data for intermetallic phases (Vol.2) [M]. Materials Park, OH: ASM, 1991: 7-68.

[25] GUPTA K P. The Co-Nb-W (cobalt-niobium-tungsten) system [J]. Journal of Phase Equilibria, 2003, 24: 82-85.

[26] NIESSEN A K, MIEDEMA A R. Enthalpies of formation of liquid and solid binary alloys based on 3d metals: IV. Alloys of cobalt [J]. Physica B+C, 1988, 151: 401-432.

[27] JIANG C. First-principles study of $Co_3(Al,W)$ alloys using special quasi-random structures [J]. Scripta Materialia, 2008, 59: 1075-1078.

[28] KIM J S, KOO Y M, LEE B J. Modified embedded-atom method interatomic potential for the Fe-Pt alloy system [J]. Journal of Materials Research, 2006, 21: 199-208.

[29] KIM Y M, LEE B J. A modified embedded-atom method interatomic potential for the Cu-Zr system [J]. Journal of Materials Research, 2008, 23: 1095-1104.

[30] BRODERICK S R, AOURAG H, RAJAN K. Data mining density of states spectra for crystal structure classification: An inverse problem approach [J]. Statistical Analysis and Data Mining, 2009, 1: 353-360.

[31] OHTANI H, YAMANO M, HASEBE M. Thermodynamic analysis of the Co-Al-C and Ni-Al-C systems by incorporating ab initio energetic calculations into the CALPHAD approach [J]. CALPHAD, 2004, 28: 177-190.

[32] GRUSHKO B, VELIKANOVA T Y. Stuctual studies of materials: Formation of quasicrystals and related structures in systems of aluminum with transition metals. I. Binary systems formed by aluminum with 3d metals [J]. Powder Metallurgy and Metal

Ceramics, 2004, 43: 72-86.

[33] TAO X M, LIU Y Z, WANG R C, OUYANG Y F, DU Y, HE Y H. First-principles investigations of elastic, electronic and thermodynamic properties of $Al_{12}$X (X=Mo, W and Re) [J]. Intermetallics, 2012, 24: 15-21.

[34] MESCHEL S V, KLEPPA O J. Standard enthalpies of formation of 5d aluminides by hightemperature direct synthesis calorimetry [J]. Journal of Alloys and Compounds, 1993, 197: 75-81.

[35] XU W W, HAN J J, WANG Z W, WANG C P, WEN Y H, LIU X J, ZHU Z Z. Thermodynamic, structural and elastic properties of $Co_3$X (X=Ti, Ta, W, V, Al) compounds from first-principles calculations [J]. Intermetallics, 2013, 32: 303-311.

# Co-W 和 Al-W 合金系统的修正嵌入原子势能的计算

董卫平 $^{1}$ , 陈 铮 $^{2}$ , Byeong-Joo LEE $^{3}$

1. 浙江师范大学 工学院, 金华 321004;
2. 西北工业大学 材料学院, 凝固国家重点实验室, 西安 710072;
3. Department of Materials Science and Engineering, Division of Advanced Nuclear Engineering, Pohang University of Science and Technology (POSTECH), Pohang 790-784, Korea

摘 要: 采用半经验的第二近邻修正型嵌入原子理论的原子间作用势模型, 基于已开发的 Co, Al 和 W 纯元素原子间作用势参数, 拟合 Co-W 和 Al-W 二元合金系参数, 得到 Co-W 和 Al-W 二元合金的原子间作用势及势能函数。Co-W 和 Al-W 二元合金的势能参数主要是由晶格参数、形成焓、熔点以及弹性常数等物理性能的实验结果来确定的。结果表明, 该势能参数能准确地计算出 Co-W 和 Al-W 二元合金的基本物理性能。其中, 晶格常数、形成焓、热稳定性能和弹性常数与实验结果及第一性能计算结果非常吻合, 混合焓以及液态混合焓与相图计算结果很相符。同时, 拟合的 Co-W 和 Al-W 二元合金势能参数很容易与已有的其他 Co 基二元势能参数结合, 并广泛用于 Co-Al-W 系多元合金各种性能的计算, 特别是对界面性能的研究很适用。

关键词: 修正嵌入原子方法; Co-W 系统; Al-W 系统; 原子级模拟

(Edited by Yun-bin HE)
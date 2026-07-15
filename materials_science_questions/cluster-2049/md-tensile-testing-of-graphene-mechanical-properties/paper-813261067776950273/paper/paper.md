AIAA-2004-1609
# DISCRETE ATOMISTIC AND CONTINUUM FRACTURE PARAMETER MODELING OF A GRAPHENE SHEET

Y. Jin* and F. G. Yuan†

Professor, Department of Mechanical and Aerospace Engineering
North Carolina State University
Raleigh, NC 27695-7910

## Abstract

Macroscopic fracture parameters are investigated using molecular mechanics simulations for a graphene sheet containing atomic-scale cracks. In the discrete atomistic modeling the interatomic forces are described based on Tersoff-Brenner potential. Elastic energy release rates of the graphene sheet under symmetric (Mode I) and antisymmetric (Mode II) small deformation are directly calculated from global energy approach and local force approach using the principle of virtual work respectively. The energy release rates are also calculated through homogenized material properties based on linear elastic fracture mechanics. The results show good agreement between discrete atomistic and continuum mechanics modeling for fracture parameters and deformed crack surface profile. This establishes connections of fracture parameters between microscopic and macroscopic description of fracture in covalently bonded solids.

## Introduction

Fracture mechanics has become an engineering discipline that has been studied by both atomistic and continuum approaches. In 1921, Griffith approached the fracture theory of brittle materials from the fundamental energy balance, by introducing a specific surface energy along the crack surface. All the atomic or internal structural factors are hidden in the surface energy. An important precursor to the Griffith theory was the elastic fields of an elliptical cavity based on continuum theory. Although Griffith formulated a fracture criterion in terms of macroscopic thermodynamic quantities, a complete description required an evaluation of events at the molecular level. The maximum stress at the tip of an equilibrium crack must correspond to the theoretical cohesive strength of the material; that is, the largest possible stress level that the molecular structure can sustain by virtue of its intrinsic bond strength. The global energy approach could not be extended easily to many different geometries and loading conditions encountered in a variety of experiments and practical structures.

In 1957, Irwin used a local force approach showed, for the first time, the local stresses around the crack tip in linear elastic materials. Irwin suggested that the singular stresses could be characterized in terms of a singular parameter, stress intensity factor. This factor combines the effect of geometry and load. As a consequence, the fracture characterization problem was reduced to the calculation of single quantity of universal significance. Furthermore, Irwin provided a quantitative relation between that strain energy release rate, a global parameter, and the stress intensity factor, a local crack-tip parameter. Since the stress intensity factor characterizes the failure at the crack tip as long as process and inelastic zones are small compared with the macroscopic dimensions of the solids, so called small scale yielding, the Irwin theory can apply to non-brittle materials. Since then, the continuum based fracture mechanics has been of great interest in applying to ductile materials using other parameters such as $J$ and other advanced materials including composite materials. Various fracture criteria have been established from a macroscopic point of view. A damage tolerance philosophy based on fracture mechanics has been developed to provide structural integrity assessments in aerospace industry.

In principle, all the properties of a material are determined by constitutive atoms and the basic laws of physics, in particular fracture associated with successive failure at atomic level. Hence, atomistic simulation may open new avenues in studies of microscopic origins of material failure behavior. To provide a basic understanding of the origins of facture due to the rupture of the interatomic bonds, Elliott (1947) first attempted an analysis in explicitly considering interatomic forces which resist crack extension. Using the linear elastic solution of a cracked body under tension, the normal stress versus the displacement along the crack plane is deduced. By equating the area under the stress-displacement curve to the surface energy and the maximum stress to the critical rupture stress for the material, Elliott formulated

* Graduate Student.
† Professor, AIAA Associate Fellow.
*Copyright © 2004 by F. G. Yuan. Published by the American Institute of Aeronautics and Astronautics, Inc., with permission.*

---

1
American Institute of Aeronautics and Astronautics

a model with two semi-infinite solids that attract each other by the atomistic force-separation curve. A very close relation with Griffith theory has been found. Goodier and Kanninen (1966) examined a cracked solid by taking the interatomic forces bridging the crack surface, while all other interatomic interactions are considered to be linearly elastic. Cribb and Tomkins (1967) proposed a distribution of interatomic forces across a crack-tip and derived the corresponding interatomic force-distance curve by the continuum theory of linear elasticity. In 1970s, numerous articles have focused on the failure of the solids using atomistic models. (e.g., Chang, 1970; Kanninen and Gehlen, 1971; Sinclair and Lawn, 1972, and Gehlen *et al.*, 1972.)

Ever-increasing computational power, advancement in the description of atomic interactions in materials, and a strong desire in developing lightweight nanostructured materials have revealed the emergence of interest in predicting the properties of materials in the atomic level before they are synthesized. The prediction using atomistic simulations can gain insights on the material behavior at the most fundamental level. A material studied in the prediction can be always perfectly characterized in terms of internal structure, composition, defects, etc., making the results often less ambiguous than in experiments. Continuum mechanics approach, on the other hand, is often based on phenomenological constitutive models which can be an idealization of observed deformation properties, that may not be representative of actual physical mechanism.

In this paper, macroscopic fracture parameters are examined from both atomic-scale and macroscopic continuum model. A sample made of graphite is used to calculate the elastic energy release rates under Mode I and II small deformation. In the direct atomistic simulation, Tersoff-Brenner interatomic potential is used to describe the atomic force interactions among carbons. Two methods, global energy approach and local force approach are both adopted to compute the energy release rates. The energy release rates and deformed crack surfaces are also calculated from linear elastic fracture mechanics through homogenized material properties for comparison.

### Interatomic Potential Energy Function

Developing the interatomic potential function is the key issue of molecular simulation. Many researchers have been working over the past two decades to derive functional forms and parameters for potential function of general applicability to organic molecules. A natural starting is to describe the total interatomic potential energy in terms of three different mechanical interactions among atoms, which are bond stretching, bond bending and bond torsion. This potential function is a general function that can be applied to most atomic structures and are much less relatively computationally demanding. However it has several limitations to reflect the real chemical bond reactions. For example, analysis of the vibration spectrum shows that real diatomic molecules do not vibrate as if they were simple particles at the ends of classical springs. Another limitation is due to the fixed set of atom types. In the actual chemical structure the atom properties always depend on a particular bond environment, i.e., the carbon atom in ethyne is obviously chemically different from a carbon atom in a diamond molecule. However, when using this potential to describe the two different chemical systems listed above, the bond properties simulated by this potential would be exactly the same with each other, which is unphysical. To avoid such limitations, a Tersoff-Brenner potential energy function that can reproduce the realistic chemical bonds properties of hydrocarbon molecules more accurately is adopted to investigate the fracture parameters at the atomic level. A detailed description of the Tersoff-Brenner potential energy function will be provided in the following.

Tersoff-Brenner potential is an empirical many-body potential energy function, which is capable of modeling intramolecular chemical bonding of diamond and graphite as well as a number of essential hydrocarbons molecules (Brenner, 1990). The potential is based on Tersoff's covalent-bonding formalism with corrections for functions of neighboring atoms on local environment (Tersoff, 1988a, b, and c). For carbon atoms, the so-called Tersoff-Brenner potential energy function is given by:

$$
U=\sum_{i} \sum_{j(i>i)}\left[V_{R}\left(r_{i j}\right)-\bar{B}_{i j} V_{A}\left(r_{i j}\right)\right] \tag{1}
$$

Here $U$ is the total interatomic potential energy of the system. $i$ refers to the atom of interest, $j$ refers to neighboring atoms, and $r_{i j}$ is the distance between atoms $i$ and $j$. Fig. 1 is a schematic diagram of the atomic structure of graphite which illustrates the atom distance and neighboring atoms in the Tersoff-Brenner potential function more clearly. From the figure an arbitrary atom $i$ has three neighboring atoms $j, k_{1}, k_{2}$.

The functions $V_{R}(r_{i j})$ and $V_{A}(r_{i j})$ are the short-range pair potential describing repulsive and attractive interactions between atoms $i$ and $j$ respectively given by

$$
V_{R}\left(r_{i j}\right)=f\left(r_{i j}\right) \frac{D_{e}}{S-1} e^{-\sqrt{2 S} \beta\left(r_{i j}-r_{e}\right)} \tag{2}
$$

---
2
American Institute of Aeronautics and Astronautics

$$
V_{A}\left(r_{i j}\right)=f\left(r_{i j}\right) \frac{D_{e} S}{S-1} e^{-\sqrt{2 / S} \beta\left(r_{i j}-r_{e}\right)} \quad(3)
$$

where $r_{e}$ is the equilibrium distance of two free carbon atoms. $D_{e}, S$ and $\beta$ are constants.

![](./images/813261067776950273_1.jpg)

Figure 1 Schematic diagram of atomic structure of graphite

The cut-off function $f\left(r_{i j}\right)$, which restricts the pair potential to nearest neighbors, is simply taken as:

$$
f\left(r_{i j}\right)=\left\{\begin{array}{cc}
1 & r_{i j}<r_{1} \\
\frac{1}{2}\left[1+\cos \left(\frac{\pi\left(r_{i j}-r_{1}\right)}{r_{2}-r_{1}}\right)\right] & r_{1} \leq r_{i j} \leq r_{2} \\
0 & r_{i j}>r_{2}
\end{array} \quad(4)\right.
$$

which has a continuous value from 1 to 0 in the range of $r_{1}$ and $r_{2} . r_{2}$ is the cut-off distance.

The function $\overline{B_{i j}}$ is the critical feature of the potential. It represents a measure of the number of bonds between atoms in a material and bond angle, and is assumed to be a monotonically decreasing function of the coordination of atoms $i$ and $j$ because the more neighbors an atom has, the weaker the bond to each neighbor is. Since $\overline{B_{i j}}$ can reflect the change of local atomic environment, the Tersoff-Brenner potential then has the capability to accurately describe different hydrocarbon systems within the same set of parameters.
The form of $\overline{B_{i j}}$ is given by:

$$
\overline{B_{i j}}=\frac{1}{2}\left(B_{i j}+B_{j i}\right) \quad(5)
$$

where

$$
B_{i j}=\left[1+\sum_{k(\neq i, j)} G\left(\theta_{i j k}\right) f\left(r_{i k}\right)\right]^{-\delta} \quad(6)
$$

$\delta$ is the constant. $G\left(\theta_{i j k}\right)$, which is the function of the angle $\theta_{i j k}$ between bonds $i-j$ and $i-k$, is given by

$$
G(\theta)=a_{0}\left[1+\frac{c_{0}^{2}}{d_{0}^{2}}-\frac{c_{0}^{2}}{d_{0}^{2}+(1+\cos \theta)^{2}}\right] \quad(7)
$$

where $a_{0}, c_{0}, d_{0}$ are constants. All the constants in the Tersoff-Brenner potential are listed as follows:
$r_{e}=0.139 \mathrm{~nm}, \quad D=6.0 \mathrm{ev}, \quad S=1.22, \quad \beta=21 \mathrm{~nm}^{-1}$,
$r_{1}=0.17 \mathrm{~nm}, \quad r_{2}=0.20 \mathrm{~nm}, \quad \delta=0.5$,
$a_{0}=0.00020813, \quad c_{0}^{2}=330^{2}$, and $d_{0}^{2}=3.5^{2}$.

Note that $r_{e}$ in the potential function (Eq. 2 and 3) is not the real equilibrium bond length in any arbitrary system. Only when $\overline{B_{i j}}=1.0$ is $r_{e}$ the equilibrium bond length. The equilibrium bond length is determined by minimizing the interatomic potential with regard to $r_{i j}$, that is $\partial U / \partial r_{i j}=0$. Apparently, the equilibrium bond length is a function of $\overline{B_{i j}}$ which represents the influence of nearby neighboring atoms exerting on the bond $i-j$. Therefore for different bond conditions, such as $s p^{2}$ hybridization and $s p^{3}$ bond, this potential can automatically determine the equilibrium bond length in different systems within the same set of parameters in the potential function. This new feature also provides a way to describe the phenomenon of bond breaking and forming. This lead to the equilibrium interatomic distance for the graphene sheet equal to $r_{0}=0.145 \mathrm{~nm}$.

To give a brief picture of Tersoff-Brenner potential function, Fig. 2 describes the interatomic force and potential energy versus bond length for a single bond between atom $i$ and $j$ in a graphene sheet. In both figures the bond $i-j$ reaches equilibrium at point $A$; at point $B$ the bond length equals to $r_{1}$ and at point $C$ equals to $r_{2}$, which is the cut-off distance. In Fig. 2a the interatomic force increases dramatically when the bond length reaches $0.17 \mathrm{~nm}$. This awkward phenomenon results from the cut-off function $f\left(r_{i j}\right)$ in the Tersoff-Brenner potential. Thus, a proper adjustment in the potential function is necessary to avoid this problem when studying the mechanical properties of a bond in the range of the cut- off distance. In this paper the bond properties under

![](./images/813261067776950273_2.jpg)

(a) Interatomic force versus bond length

![](./images/813261067776950273_3.jpg)

(b) Potential energy versus bond length

Figure 2 The interatomic force and potential energy versus bond length obtained by Tersoff-Brenner potential

investigations are under a small strain field where the bond length in the system is always much smaller than $r_1$.

## Numerical Results

A sample of a graphene sheet in a zigzag form with dimensions 15.068 nm ×17.255 nm containing a system of 9840 carbon atoms is studied in this paper. Figure 3 is a schematic of the sample. In direct atomistic simulation, each and every atomistic degree of freedom is explicitly accounted for, and the minimum energy configuration is determined on the basis of interatomic interactions. The fracture of a material occurs due to the development of certain displacement discontinuity surfaces within the material. A crack is located in the middle of the graphene sheet and is perpendicular to some of the covalent bonds. The crack is modeled by removing the interatomic chemical bond to eliminate the interaction between atom pairs across the crack surface. Due to the discrete nature of atomistic modeling, the crack length is evaluated as the length measured from number of broken bonds. In the linear elastic fracture mechanics (LEFM), the Young's modulus ($E = 0.68$ TPa) is calculated from an energy approach (Jin and Yuan, 2003). A sharp crack is formed by assigning the boundary atoms in accord with the continuous crack with the "crack-tip" taken at the center of the first unbroken bond.

![](./images/813261067776950273_4.jpg)

Figure 3 Schematic diagram of a center-cracked graphene sheet;
Symbol –o– represents carbon atom.

Elastic strain energy release rates are first calculated from direct atomistic simulations by realistic crack extension models. It is assumed that the crack extension would not cause the bond reconfiguration. Two methods are proposed to calculate the macroscopic fracture parameters. The first method is based on the change of total potential energy of two self-similar graphene sheets with same dimensions but two slightly different central crack lengths, $2a$ and $2a+2\Delta a$, as given by

$$
G = -\frac{U_{2a+2\Delta a} - U_{2a}}{2\Delta a t} \tag{8}
$$

where $U_{2a}$ and $U_{2a+2\Delta a}$ are the total potential energy of the two graphene sheets under a given deformation mode obtained from Tersoff-Brenner potential. $\Delta a$ is the equilibrium interatomic distance in the $x$ direction which is equal to 0.251 nm ($0.145 \times \sqrt{3}$ nm). $t$ is the thickness of the graphene sheet. In this study an interlayer separation distance of graphite, which is 0.34 nm, is defined as the effective thickness.

Another means of evaluating the energy release rates is the local force method by determining the virtual work that is required to close the crack extension. In

this method, it is not required to calculate the total potential energy. Therefore it leads to less computational time, especially for those multi-million atomic systems, since only those neighboring atoms near the crack tip need to be evaluated; while the change of total potential energy requires all the atoms in the system have to be investigated.

Based on the principle of virtual work (PVW), the virtual work is illustrated in Figures 4 and 5 to close the crack extension in a graphene sheet for mode I and II small deformation respectively. The energy release rates for mode I and II, denoted by $G_I$ and $G_{II}$ , are expressed by:

$$
G_{I}=\frac{1}{2 \Delta a t} F_{y}\left(v^{+}-v^{-}\right) \tag{9}
$$

$$
G_{I I}=\frac{1}{2 \Delta a t}\left[F_{x}\left(u^{+}-u^{-}\right)+F_{y}\left(v^{+}-v^{-}\right)\right] \tag{10}
$$

where $F_x$ and $F_y$ are the interatomic forces exerted on atom $i$ in the $x$ and $y$ directions respectively by atom $j$ and its neighboring atoms at the crack length $2a$. $u^+$,

![](./images/813261067776950273_5.jpg)

Figure 4 A general illustration of virtual work under mode I.

![](./images/813261067776950273_6.jpg)

Figure 5 A general illustration of virtual work under mode II

$u^-$, $v^+$, $v^-$ are the crack opening displacements of atom $i$ and $j$ in the $x$ and $y$ directions at crack length $2a+2\Delta a$. Therefore two configurations have been used to obtain the value of virtual work. Note that in the discrete atomistic simulation the crack extension implies the bond broken in the immediate vicinity of the crack tip with length $\Delta a$.

In the molecular mechanics (MM) simulation, a centered crack of length $2a$ varying from 1.006 to 6.530 nm of the graphene sheet is examined. The initial state without applied deformation reaches equilibrium for approximately 100 ps with a time step of 1.5 fs. After equilibrium is reached, a small deformation, $\varepsilon_0=0.005$, is applied to the sample by scaling atomic positions and boundary conditions along the appropriate coordinate. For mode I the fixed-grip displacement $u_y=\varepsilon_0 y$ is applied on the top and bottom surfaces of the sample; for mode II $u_x=\varepsilon_0 y$ and $u_y=0$ is prescribed on these surfaces. Then roughly another 100 ps period is required to reach a minimum potential energy of the system. All molecular mechanics simulations are carried out at temperature 0 K.

Figures 6 and 7 are the close-up views of the deformation configuration near the crack tip in Mode I and II. The crack tip is located at the center between atom $i$ and $j$. The solid line and broken line refer to the deformed and undeformed configurations respectively. For Mode I the deformation of the surface of a crack

obtained by LEFM is displayed as bold-dotted line in Fig. 6. Note that in comparison with the deformed shape of the crack surfaces from atomistic simulation the deformed crack surfaces obtained from LEFM are formed by adding the equilibrium atomic separation to the resulting crack opening displacements.

Figures 8 and 9 show the normalized strain energy release rates $G/\sigma_0^2$ and $G/\tau_0^2$ versus crack length by three approaches under Mode I and Mode II deformation respectively. $\sigma_0 \text{(or } \tau_0\text{)} = F_0 / A$, where $F_0$ is the external force applied on the system resulting from the fixed-grip prescribed displacements and $A$ is the area of the cross-section of graphene sheet. From the figures, a good agreement is reached between the results from atomistic simulation and those from LEFM. This implies that the fracture parameters calculated from LEFM can be also predicted from atomic simulation. The detailed fracture parameters are also tabulated in Table 1 and 2. In Fig. 10, the deformed crack surface profile from atomistic simulation and LEFM is shown for the initial crack length $2\mathrm{a}_0 = 6.53$ nm. It is expected that they also match well.

![](./images/813261067776950273_7.jpg)

Figure 6 Close-up view of undeformed and deformed configurations near the crack tip under mode I. (Bold-dotted line is the deformed crack surface from LEFM)

![](./images/813261067776950273_8.jpg)

Figure 7 Close-up view of undeformed and deformed configurations near the crack tip under mode II

![](./images/813261067776950273_9.jpg)

Figure 8 $G/\sigma_0^2$ versus crack length under mode I

![](./images/813261067776950273_10.jpg)

Figure 9 $G/\tau_0^2$ versus crack length under mode II


**Table 1. The numerical results of $G/\sigma_0^2$ under model I**

<table>
  <thead>
    <tr>
      <th rowspan="2">$G/\sigma_0^2$<br>Crack Length (nm) ($^*$)</th>
      <th colspan="2">Atomistic Simulation</th>
      <th rowspan="2">LEFM</th>
    </tr>
    <tr>
      <th>Global Energy Method</th>
      <th>Local Force Method</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1.005</td>
      <td>0.259</td>
      <td>0.252</td>
      <td>0.283</td>
    </tr>
    <tr>
      <td>1.507</td>
      <td>0.377</td>
      <td>0.366</td>
      <td>0.397</td>
    </tr>
    <tr>
      <td>2.009</td>
      <td>0.498</td>
      <td>0.482</td>
      <td>0.510</td>
    </tr>
    <tr>
      <td>2.511</td>
      <td>0.623</td>
      <td>0.600</td>
      <td>0.642</td>
    </tr>
    <tr>
      <td>3.014</td>
      <td>0.753</td>
      <td>0.726</td>
      <td>0.769</td>
    </tr>
    <tr>
      <td>3.516</td>
      <td>0.887</td>
      <td>0.856</td>
      <td>0.906</td>
    </tr>
    <tr>
      <td>4.018</td>
      <td>1.029</td>
      <td>0.992</td>
      <td>1.037</td>
    </tr>
    <tr>
      <td>4.521</td>
      <td>1.180</td>
      <td>1.141</td>
      <td>1.180</td>
    </tr>
    <tr>
      <td>5.023</td>
      <td>1.342</td>
      <td>1.294</td>
      <td>1.354</td>
    </tr>
    <tr>
      <td>5.525</td>
      <td>1.517</td>
      <td>1.463</td>
      <td>1.527</td>
    </tr>
    <tr>
      <td>6.027</td>
      <td>1.708</td>
      <td>1.647</td>
      <td>1.688</td>
    </tr>
    <tr>
      <td>6.530</td>
      <td>1.918</td>
      <td>1.849</td>
      <td>1.883</td>
    </tr>
  </tbody>
</table>

**Table 2. The numerical results of $G/\tau_0^2$ under model II**

<table>
  <thead>
    <tr>
      <th rowspan="2">$G/\tau_0^2$<br>Crack Length (nm) ($^*$)</th>
      <th colspan="2">Atomistic Simulation</th>
      <th rowspan="2">LEFM</th>
    </tr>
    <tr>
      <th>Global Energy Method</th>
      <th>Local Force Method</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1.005</td>
      <td>0.638</td>
      <td>0.608</td>
      <td>0.635</td>
    </tr>
    <tr>
      <td>1.507</td>
      <td>0.890</td>
      <td>0.865</td>
      <td>0.888</td>
    </tr>
    <tr>
      <td>2.009</td>
      <td>1.139</td>
      <td>1.120</td>
      <td>1.142</td>
    </tr>
    <tr>
      <td>2.511</td>
      <td>1.392</td>
      <td>1.380</td>
      <td>1.403</td>
    </tr>
    <tr>
      <td>3.014</td>
      <td>1.649</td>
      <td>1.643</td>
      <td>1.663</td>
    </tr>
    <tr>
      <td>3.516</td>
      <td>1.910</td>
      <td>1.909</td>
      <td>1.930</td>
    </tr>
    <tr>
      <td>4.018</td>
      <td>2.156</td>
      <td>2.164</td>
      <td>2.201</td>
    </tr>
    <tr>
      <td>4.521</td>
      <td>2.424</td>
      <td>2.443</td>
      <td>2.484</td>
    </tr>
    <tr>
      <td>5.023</td>
      <td>2.701</td>
      <td>2.738</td>
      <td>2.753</td>
    </tr>
    <tr>
      <td>5.525</td>
      <td>3.023</td>
      <td>3.084</td>
      <td>3.072</td>
    </tr>
    <tr>
      <td>6.027</td>
      <td>3.327</td>
      <td>3.405</td>
      <td>3.406</td>
    </tr>
    <tr>
      <td>6.530</td>
      <td>3.649</td>
      <td>3.747</td>
      <td>3.695</td>
    </tr>
  </tbody>
</table>

* The unit of $G/\sigma_0^2$ or $G/\tau_0^2$ is $10^{-20}\ \text{J/Pa}^2$

## Summary

Macroscopic fracture parameters have been examined from both atomistic simulation and continuum models. There is a very good agreement between atomistic simulation and continuum mechanics for the macroscopic fracture parameters and deformed crack surfaces under small deformation. Especially the fracture parameter can be accurately evaluated from the local force field immediate vicinity of the crack in the atomistic simulation. In macroscopic fracture mechanics under small deformation, linear elastic fracture mechanics is sufficient for the description of cracking behavior for this covalently bonded material. The results merge the discrete (atomistic) and continuum (macroscopic) description of facture.

This atomistic approach can provide further insights into the mechanisms responsible for the failure process.

![](./images/813261067776950273_11.jpg)

**Figure 10** Crack surface profile under Mode I from atomistic simulation and LEFM. (The crack length is 6.530 nm.)

This link between atomistic and continuum mechanics can give physical insights of examining a variety of failure phenomena. Since the atomistic simulation often provides much more information about the microscopic structures and phenomena than that based on continuum theory, it may lead to the development of new concepts and new materials, and predictions of new types of material behavior.

## References
1.  A. A. Griffith, "The Phenomena of Rupture and Flow in Solids", *Philosophical Transactions of the Royal Society of London*, A221, pp.163-198, 1921.
2.  G. R. Irwin, "Analysis of Stresses and Strains Near the End of a Crack Traversing a Plate", *Journal of Applied Mechanics*, Vol. 24, pp. 361-364, 1957.
3.  H. A. Elliott, "An Analysis of the Conditions for Rupture Due to Griffith Cracks", *Proceedings of the Physical Society*, Vol. 59, pp. 208-223, 1947.
4.  J. N. Goodier and M. F. Kanninen, "Crack Propagation in a Continuum Model with Nonlinear Atomic Separation Law", *Technical Report 165*, Division of Engineering Mechanics, Stanford University, 1966.
5.  J. L. Cribb and B. Tomkins, "On the Nature of the Stress at the Tip of a Perfectly Brittle Crack", *Journal of the Mechanics and Physics of Solids*, Vol. 15, pp. 135-140, 1967.
6.  R. Chang, "An Atomistic Study of Fracture", *International Journal of Fracture*, Vol. 6, No. 2, pp. 111-125, 1970.

7
American Institute of Aeronautics and Astronautics

7. M. F. Kanninen and P. C. Gehlen, "Atomic Simulation of Crack Extension in BCC Iron", *International Journal of Fracture*, Vol. 7, pp. 471-474, 1971.

8. J. E. Sinclair and B. R. Lawn, "An Atomistic Model for an Equilibrium Crack in Diamond", *International Journal of Fracture*, Vol. 8, pp. 125-127, 1972.

9. P. C. Gehlen, G. T. Hahn, and M. F. Kanninen, "Crack Extension by Bond Rupture in a Model of BCC Iron", *Scripta Metallurgica*, Vol. 6, pp.1087-1090, 1972.

10. D. W. Brenner, "Empirical Potential for Hydrocarbons for Use in Simulating the Chemical Vapor Deposition of Diamond Films", *Physical Review B*, Vol. 42, pp. 9458-9471, 1990.

11. J. Tersoff, "New Empirical Approach for the Structure and Energy of Covalent Systems", *Physical Review B*, Vol. 37, pp. 6991-7000, 1988.

12. J. Tersoff, "Empirical Interatomic Potential for Carbon, with Applications to Amorphous Carbon", *Physical Review Letters*, Vol. 61, pp. 2879-2882, 1988.

13. J. Tersoff, "New Empirical Model for the Structure Properties of Silicon", *Physical Review Letters*, Vol. 56, pp. 632-635, 1988.

14. Y. Jin and F. G. Yuan, "Simulation of Elastic Properties of Single-walled Carbon Nanotubes", *Composites Science and Technology*, Vol. 63, pp. 1507-1515, 2003.

---

8
American Institute of Aeronautics and Astronautics
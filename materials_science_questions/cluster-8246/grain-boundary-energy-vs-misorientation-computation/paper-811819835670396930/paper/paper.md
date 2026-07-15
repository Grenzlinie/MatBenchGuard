# Evolution of Annealing Twins in Sputtered Cu Films

C.K. YOON¹ and D.P. FIELD¹,²

1.—Washington State University, Pullman, WA, USA. 2.—e-mail: dfield@wsu.edu

The Monte Carlo Potts model with $n$-fold method was used to simulate grain structure evolution in thin Cu films according to energetic competition principles. Surface/interface, grain boundary, and strain energy factors were applied to determine grain growth and crystallographic texture evolution as a function of film thickness. Furthermore, annealing twins were simulated through specific criteria that arbitrarily insert twin grains into the structure through grain boundary energy considerations. Four different types of microstructures were observed experimentally and simulated by the Monte Carlo technique.

**Key words:** Monte Carlo Potts model, annealing twins, microstructure evolution, copper thin films

## INTRODUCTION

The characteristic microstructure of a thin film affects its function in electronic applications. Modern Cu films and line structures, which have replaced aluminum due to its high electrical and thermal conductivity, often contain a large fraction of annealing twins. Annealing twins in face-centered cubic (FCC) metals with low stacking fault energy are typically related to the parent by $60^\circ$ rotation about the $\langle 111 \rangle$ crystal direction. These twins, which are associated with grain growth at relatively high temperature, can change the crystallographic texture and grain boundary character distribution in films and line structures. Because these annealing twins have properties that affect microstructure evolution, it is important to include them in considerations of structural evolution. Grain growth in thin films generally plays an important role in defining the microstructural characteristics of the films.¹

During annealing, normal and abnormal grain growth occur in a manner that lowers the total energy accumulated in the film. The total energy is the sum of surface energy, interface energy, strain energy, and grain boundary energy.² These combined energy variables have a tendency to be minimized during grain growth, and this generally results in texture transformation from the original state. It is well known that texture evolution during grain growth of thin films depends upon a competition between principles of surface/interface energy minimization and strain energy minimization.¹,³,⁴ {111} out-of-plane fiber textures result in thinner films where surface energy minimization controls grain growth, and {100} out-of-plane fiber textures are observed in thicker films at higher temperatures as a consequence of strain energy minimization.¹ In FCC Cu films, the {111} close-packed surface is associated with the lowest surface free energy, so strong {111} out-of-plane texture is present with little dependence on deposition and annealing conditions.⁵

The conventional Monte Carlo Potts model has been shown to be capable of making significant and precise predictions of grain growth by various researchers since the 1990s.⁶⁻¹⁰ A two-dimensional model has been applied under the assumption that thin films are two dimensional in character. Of course, three-dimensional simulations yield more realistic predictions but at the cost of greater computational effort. In this work it is shown that the thickness dependence of structure evolution can be captured by a two-dimensional model. The focus is on the texture and grain structure evolution and how these can be modeled using the Monte Carlo Potts model according to the overall energy minimization concept. Experimentally, many researchers have attempted to understand grain structure (grain growth and grain boundary properties) and

(Received May 1, 2009; accepted November 2, 2009;
published online November 26, 2009)

crystallographic texture according to various factors such as stress state, $^{11–13}$ stacking fault energy, $^{14,15}$ grain size, $^{16,17}$ and film thickness. $^{2,5,18,19}$ Our approach is to demonstrate the capabilities and difficulties associated with including these important factors of microstructure evolution in Cu thin films.

# SIMULATION TECHNIQUES

A Monte Carlo Potts model, modified from that developed by Hassold and Holm, $^{8}$ has been used to simulate two-dimensional microstructure evolution. This simulation method divides materials into a small area or particle which is assumed to be a nucleus or grain. This nucleus or grain has its own crystallographic orientation $(g)$ expressed by Bunge Euler angles indicated by spin variables ranging from 1 to $Q$. The $Q$-states are assigned total orientations $(g)$, which was set to be 3722 in our model. Each of these 3722 orientations, which are randomly selected from an input file, is unique and can be changed to that of an adjacent grain according to the effect of this change on the overall energy state. The concept of interaction between sites is based on an energy minimization model. In order to decrease the total interacting boundary area of a system, boundaries move toward their centers of curvature. High-energy-state grains have a tendency to reduce their boundary curvature, and this curvature-driven diffusive coarsening of grains dominates the grain growth. $^{8}$ Randomly selected sites or grains with adjacent neighboring grains have their unique orientations identified by Euler angles, and these are used to help determine the proposed energy change of the position $(\Delta E)$ assuming that the orientation is changed to that of one of its neighbors. In our simulation, the system provided a driving force to reach a minimum-energy state through reorientation of each site with probability $p(\Delta E)$ given by

$$
p(\Delta E)=\left\{\begin{array}{rll}
1 & \text { if } & \Delta E \leq 0 \\
\exp \left(-\Delta E / k_{\mathrm{B}} T\right) & \text { if } & \Delta E>0
\end{array}\right. \quad(1)
$$

$\Delta E$ is the energy change, $T$ is annealing temperature, and $k_{\mathrm{B}}$ is the Boltzmann constant. If the energy change is less than or equal to 0, the site will reorient to another orientation with transition probability 1. If the energy change is larger than zero, the reorientation changes with probability $\exp(-\Delta E/k_{\mathrm{B}}T)$. According to the energy minimization competition, some nuclei are consumed while others coarsen and grow, resulting in a preferred orientation. This two-dimensional (2D) microstructural evolution of grain structure has been tracked by a change of each initially established orientation according to energy considerations suggested by Park and Field. $^{2}$ The surface/interface, grain boundary, and strain energies lead to the preferred final textures of thin films. These energetic factors are described by the following Hamiltonian:

$$
E=\sum_{i=1}^{N}\left(\gamma_{\mathrm{sur}}(g)+\gamma_{\mathrm{int}}(g)+\gamma_{\mathrm{str}}(g)+\frac{1}{2} \sum_{j=1}^{m} \gamma_{\mathrm{gb}}(\Delta g)\right), \quad(2)
$$

where $E$ is the total energy of the system, $N$ is the total number of lattice sites, $\gamma_{\text{sur}}(g)$ is the surface energy of a unit lattice as a function of orientation $(g)$ according to normal direction (ND) (001) out of plane, $\gamma_{\text{int}}(g)$ is the interface energy as a function of orientation $(g)$, $\gamma_{\text{str}}(g)$ is the biaxial strain energy as a function of orientation $(g)$, $\gamma_{\text{gb}}(\Delta g)$ is the grain boundary energy as a function of misorientation $(\Delta g)$ between two grains of different index, and $m$ is 6, considering the number of nearest neighbors in a triangular (1,2) lattice (hexagonal array). For the purpose of comparing surface energy $\gamma_{\text{sur}}(g)$ in this model, the broken-bond energy concept given by Sundquist $^{20}$ was used. The number of unsatisfied broken bonds will vary from plane to plane, so the different atomic packing systems have the various crystallographic planes and the surface energy is dependent on crystallographic orientation $(g)$. The misorientation of an arbitrary grain with respect to neighboring grain orientations allows one to determine the angular difference of the surface normal from the reference. This angle is used for comparing surface energy by following a simple relationship:

$$
\frac{\gamma_{\{h k l\}}}{\gamma_{0\{h k l\}}}=\cos \theta, \quad(3)
$$

where $\gamma_{0\{hkl\}}$ is the surface energy at 0 K of the $\{hkl\}$ plane and $\theta$ is the angle between the $\{hkl\}$ plane and the reference plane. We set the surface normal unit vector $(hkl)$ of each grain with (001) ND to an initial value of $2.610 \mathrm{~J} / \mathrm{m}^{2}$ for (100) surface at $200^{\circ} \mathrm{C}$, with temperature dependence given by $\frac{\mathrm{d} \gamma_{h k l}}{\mathrm{~d} T}=-5.0 \times 10^{-4} \mathrm{~J} /\left(\mathrm{m}^{2}{ }^{\circ} \mathrm{C}\right) .^{20,21}$

The interface energy is assumed to be identical to the surface energy and can be expressed by

$$
\gamma_{\mathrm{sur}}(g)=\gamma_{\mathrm{int}}(g)=\int_{A_{h k l}} \gamma_{h k l} \mathrm{~d} A_{h k l}. \quad(4)
$$

The strain energy is given by the following equation:

$$
\begin{gathered}
\gamma_{\text {strain }}(g)=h e^{2} \int_{A_{h k l}} M_{h k l} \mathrm{~d} A_{h k l} \\
\begin{array}{c}
M_{h k l}=C_{11}+C_{12}+K-\frac{2\left(C_{12}-K\right)^{2}}{C_{11}+2 K} \\
K=\left(2 C_{44}-C_{11}+C_{12}\right)\left(h^{2} k^{2}+k^{2} l^{2}+l^{2} h^{2}\right)
\end{array} \quad(5) \\
e=\int_{T_{\text {dep }}}^{T_{\text {gg }}}\left(\alpha_{\mathrm{s}}-\alpha_{\mathrm{f}}\right) \mathrm{d} T \cong \Delta \alpha \cdot \Delta T .
\end{gathered}
$$

In the above equations, $h$ is the thickness of the films; $e$ is the elastic strain, which is a function of

the temperature difference; $M_{hkl}$ is the biaxial modulus for the $\{hkl\}$-oriented grain; $\Delta\alpha$ is the mismatch in coefficients of thermal expansion; and $C_{11}=170.2$ GPa, $C_{12}=123.2$ GPa, and $C_{44}=$ 75.4 GPa at 25°C, with temperature gradient effects included as²²

$$
\frac{\mathrm{d} C_{11}}{\mathrm{~d} T}=-0.0353 \mathrm{GPa} /{ }^{\circ} \mathrm{C},
$$

$$
\frac{\mathrm{d} C_{12}}{\mathrm{~d} T}=-0.0153 \mathrm{GPa} /{ }^{\circ} \mathrm{C},
$$

$$
\frac{\mathrm{d} C_{44}}{\mathrm{~d} T}=-0.0277 \mathrm{GPa} /{ }^{\circ} \mathrm{C}.
$$

The grain boundary energy can be described by

$$
\begin{array}{r}
\gamma_{\mathrm{gb}}(\Delta g)=h\left[L_{\mathrm{LAGB}} \gamma_{\mathrm{LAGB}}+L_{\mathrm{ICTB}} \gamma_{\mathrm{ICTB}}+L_{\mathrm{CTB}} \gamma_{\mathrm{CTB}}\right]. \\
(6)
\end{array}
$$

$L_{\mathrm{LAGB}}$, $L_{\mathrm{ICTB}}$, and $L_{\mathrm{CTB}}$ are the lengths of the large-angle grain boundary, incoherent twin boundary, and coherent twin boundary, and $\gamma_{\mathrm{LAGB}}$, $\gamma_{\mathrm{ICTB}}$, and $\gamma_{\mathrm{CTB}}$ are the energies of large-angle grain boundaries, incoherent twin boundaries, and coherent twin boundaries. The large-angle grain boundary energy is assumed to be $0.625 \mathrm{~J} / \mathrm{m}^{2}$ at $925^{\circ} \mathrm{C}$, the incoherent twin boundary energy is $0.498 \mathrm{~J} / \mathrm{m}^{2}$ at $950^{\circ} \mathrm{C}$, and the coherent twin boundary energy is $0.024 \mathrm{~J} / \mathrm{m}^{2}$ at $800^{\circ} \mathrm{C}$, with temperature effects of²³

$$
\frac{\mathrm{d} \gamma_{\mathrm{LABG}}}{\mathrm{d} T}=-1.0 \times 10^{-4} \mathrm{~J} / \mathrm{m}^{2}{ }^{\circ} \mathrm{C},
$$

$$
\frac{\mathrm{d} \gamma_{\mathrm{ICTB}}}{\mathrm{d} T}=-1.0 \times 10^{-4} \mathrm{~J} / \mathrm{m}^{2}{ }^{\circ} \mathrm{C},
$$

$$
\frac{\mathrm{d} \gamma_{\mathrm{CTB}}}{\mathrm{d} T}=-2.0 \times 10^{-5} \mathrm{~J} / \mathrm{m}^{2}{ }^{\circ} \mathrm{C}.
$$

Grain boundaries can be characterized by the misorientation $(\Delta g)$ between two neighboring sites.²⁴ The grain boundary energy increases with increasing angle of misorientation to 15°. With the exception of twin boundaries, grain boundaries with larger than 15° misorientation have similar grain boundary energies, considered to be high-angle grain boundaries (HAGB). By analyzing the misorientation $(\Delta g)$ between neighboring sites, twins and twin boundaries can be identified. Geometrically, annealing twins can form and relate to the parent through a specific misorientation $(\Delta g)$ of 60° with $\langle 111\rangle$ axis. For coherent twins, the twinning plane has to be aligned with a grain boundary plane position²⁵ and the local relationships between surface energy and grain boundary energy can be considered in the following way²⁶,²⁷:

$$
\theta_{1}=\cos ^{-1}\left(\frac{\gamma_{1}}{\gamma_{\mathrm{gb}}}\right), \quad \theta_{2}=\cos ^{-1}\left(\frac{\gamma_{2}}{\gamma_{\mathrm{gb}}}\right). \quad (7)
$$

In our simulation, the grain boundary grooving phenomenon shown in Fig. 1 was considered. The thermal grooving forms in order to achieve a

![](./images/811819835670396930_1.jpg)

Fig. 1. Schematic illustration of grain boundary energy interacting with free surface energies.

capillary force balance.²⁷ Because grain boundary grooves can develop during annealing, the Young equation 7 was applied to our model for a 300°C annealing condition and grain boundary area increased through the grooves as grain growth took place.

In addition, for the purpose of speeding up the simulation time, we applied an algorithm for determining spin flips using the $n$-fold approach.⁸ When the grain growth was nearly complete, most sites in the lattice were surrounded by sites of similar orientation. Therefore, the probability of changing orientation is low and computational time is saved by using the $n$-fold approach, as opposed to the conventional Monte Carlo method. The unit of simulation time is called the Monte Carlo step (MCS) and represents an integer time increment.⁸ One iteration represents $1/N$ time increments, and $N$ iterations are required for each site in the lattice to have a chance to change its state. Therefore, 1 unit of system simulation time elapses after $N$ iterations.

All simulations performed in this work were done using periodic boundary conditions both vertically and horizontally. The expected grain size is generally small (in units of Monte Carlo lattice sites) compared with the overall dimension of the simulation region, so we do not expect the results to be significantly influenced by the imposed boundary conditions.

## SIMULATION RESULTS

For the Monte Carlo code used in this study, the orientations marked as Bunge Euler angles of grains were compared and changed for grain growth as a function of the energetics introduced in

<table><caption>Table I. Experimental results of texture according to different film thickness in Cu films²</caption>
<thead>
  <tr>
    <th>Case</th>
    <th>Thickness</th>
    <th>Texture</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>1</td>
    <td>100-nm-thick sputtered films</td>
    <td>{111} fiber</td>
  </tr>
  <tr>
    <td>2</td>
    <td>200-nm-thick sputtered films</td>
    <td>{111} fiber + twins of {111}</td>
  </tr>
  <tr>
    <td>3</td>
    <td>500-nm-thick sputtered films</td>
    <td>{001} fiber, very large grain size</td>
  </tr>
  <tr>
    <td>4</td>
    <td>800-nm-thick sputtered films</td>
    <td>{001} + twin variants of {001}</td>
  </tr>
</tbody>
</table>

previous research, $^{2,20,21}$ as summarized in Eqs. 4–6.
Three different film thicknesses were set for the simulations at 100 nm, 500 nm, and 800 nm. The deposition temperature was $25^\circ$C and the annealing temperature was $300^\circ$C. In our simulation, as Monte Carlo steps (MCS) went up, the texture started to evolve as growth conditions favored a lowering of system energy.

Previous experimental results, given in Table I, indicate that the 100-nm-thick sputtered film has a

![](./images/811819835670396930_2.jpg)

Fig. 2. Orientation maps showing a storyboard presentation of simulated grain growth for 100 nm and $300^\circ$C; (a–e) are in order of increasing MCS; (f) shows the orientation color key.

![](./images/811819835670396930_3.jpg)

Fig. 3. Predicted texture components as a function of Monte Carlo time steps for 100 nm and 300°C.

{111} out-of-plane fiber texture. This result was compared with our simulation result, shown in Fig. 2. Figure 2 shows the simulation of micro- structure evolution at 100 nm film thickness and 300°C annealing temperature conditions. Figure 2f contains the orientation color key that is used throughout the paper for all orientation images shown. The final stage of this simulation (Fig. 2e) indicates that the texture evolves to a dominant {111} orientation.

Figure 3 shows {111}, {101}, and {001} texture component development, respectively, as a function of Monte Carlo steps (MCS). The final stage shows that the texture is almost entirely composed of {111} orientations in a thin film of 100 nm thickness. This agrees with well-known experimental observation. This phenomenon has been studied by many researchers. For thin films, the {111} orientation is favored because of the effect of surface energy minimization on the film. $^{3,4}$ In general, thin Cu films have preferred {111} texture as a result of the close-packed surface that has the lowest surface free energy. $^{5,19}$

The next simulation result, shown in Fig. 4, was based on the conditions of 500-nm-thick films with 300°C annealing temperature. Figure 4 indicates that, when the {111} grains grow, {511} twins of {111} grains start to appear, as they assist in reducing the total system energy. These twins are about $16^{\circ}$ away from {001} grains. These twins appear automatically in the evolving structure through grain boundary energy considerations. Even though surface and/or strain energy are not minimized by a {511} orientation, the total energy considerations tend to favor the twin component because of the favorable boundary energy between the {111} and {511} components. This result compares well with observations of structure evolution for 200 nm films (Table I).

Simulation results for 800-nm-thick films show a dominant {001} orientation at the final step of the MC simulation (Fig. 5). The initial textures and grain assignments for the 100 nm and 800 nm simulations were similar but the final textures are distinct. The only difference in the simulated con- ditions was film thickness. The simulation case with the 800 nm film thickness indicates that the pre- ferred texture orientation is {001}. Figure 6 indi- cates how the fractions of {111}, {101}, and {001} evolved with MC time steps. Figure 6 shows that the texture rapidly changed to {001}. {111} and {101} fractions quickly went to zero at the expense of the {001} grains. No twins of {100} grains were observed in the simulations, as there is apparently no condi- tion in which the energy would be minimized by creation of such a structure. These results, i.e., that the preferred texture formation for the thinner film (100 nm) was {111} and for the thicker film (800 nm) was {001}, can be explained by the lower energy of the system during processing. Thompson and co- workers established the concept of energy competi- tion between surface/interface and strain energy (as a function of film thickness and temperature) al- most two decades ago. $^{3,4}$ The determination of which grains will grow is a result of the competition between strain energy minimization and surface/ interface energy minimization. When the change of the surface/interface energy is larger than the change of strain energy during grain growth, {111} out-of-plane texture dominates. Otherwise, {100} texture minimizes the strain energy density and dominates growth.

## DISCUSSION

This Monte Carlo simulation method with ener- getic considerations based on surface/interface, grain boundary, and strain energies showed a structure evolution in sputtered thin films accord- ing to different thickness. Figure 7 shows a sum- mary of the final simulation results, including the resulting fractions of {111}, {511}, and {001} textures for films of 100 nm, 500 nm, and 800 nm thickness. In 100 nm films, the experimental and simulation results show that the preferred texture is {111}, with surface/interface energy minimization domi- nating structure evolution. $^{3,4}$ The 500 nm film thickness case of Fig. 6 shows that {111} grains with twins of {511} tend to form a lower total system energy when all effects (surface energy, strain energy, and grain boundary energy) are considered. In thicker films, such as the result shown for 800 nm, {001} grains grow rapidly during annealing because of strain energy minimization being the dominant factor in structure evolution. $^{3,4}$ There are no results that show a low-energy configuration for the thicker films where the twins of {001} grains are present in the simulations. It is hypothesized that, during the process of growth of {111} grains, the {511} grains which are the twin grains of {111} start to appear for the purpose of reducing the total sys- tem energy. If a grain forms that is about $15^{\circ}$ away from {111} and a twin develops in this structure, it

![](./images/811819835670396930_4.jpg)

Fig. 4. Orientation maps showing a storyboard presentation of simulated grain growth for 500 nm and 300°C; (a–e) are in the order of increasing MCS.

would provide a nucleus for growth of {100} grains.
This happens infrequently so the observed grains
are very large (nuclei spaced far apart). In addition,
experimental results show that {211} and other
texture components that are twin-related to either
{111} or {001} textures exist in the thicker films
(800 nm). Our results show no such structures. In a
previous paper,²⁸ twin formation occurred by the
brute-force method. Twins grains were arbitrarily
inserted into the structure at preselected conditions
to achieve the desired structure evolution. While
properly simulating evolved structures, this ap-
proach lacks any predictive capability.

A realistic model that is capable of accurately
predicting structure evolution requires a mecha-
nistic description of twin formation. Many
researchers indicate formation of twins in terms of
three factors, such as grain boundary energy, grain

![](./images/811819835670396930_5.jpg)

Fig. 5. Orientation maps showing a storyboard presentation of grain growth for films of 800 nm thickness at 300°C; (a–e) are in increasing MCS order.

boundary mobility, and the role of dislocation arrangement. Specifically, according to growth accidents and nucleation of twins by stacking faults or fault packets, many researchers suggest a twin formation mechanism. Gleiter²⁹ in 1969 proposed a model of annealing twin formation as a result of

![](./images/811819835670396930_6.jpg)

Fig. 6. Predicted texture components as a function of Monte Carlo time steps for 800 nm and 300°C.

growth accidents leading to stacking faults, and Pande et al. $^{30}$ carried out a systematic study of annealing twin formation in nickel with the assumption that twin formation is caused by grain boundary migration and that their density depends on the driving force for migration. Mahajan et al. $^{31}$ suggested that Shockley partial dislocation loops nucleate on consecutive {111} planes by growth accidents related to grain boundary migration. Besides, previous research $^{13-18,32}$ has shown experimental evidence of various twinning fractions caused by different kinds of conditions such as film thickness, stress state, annealing conditions, and fabrication processes. These factors would have to be included in the models to predict the formation and evolution of twins in thin films.

The experimental results presented above are for high-purity sputtered Cu films. It is well known that electroplating deposition of Cu films results in a wide variety of structures subsequent to post-deposition annealing. These can range from randomly oriented, twin-rich structures to highly oriented {111} fiber textures even for films on the order of $1\ \mu$m thickness. The effects of bath chemistry on the energetics of the system and the boundary mobility would have to be included in any models of structure evolution for plated films. This will increase the complexity of the models dramat- ically. As mentioned previously, there are several factors that lead to various mechanisms of structure evolution in thin films, whether sputtered or plated. Different factors such as the film thickness, sub- strate materials (and stacking sequence), stress state, film deposition parameters, plating bath chemistry, annealing temperature and time, and geometrical constraints would all have to be con- sidered to predict structure evolution accurately.

## CONCLUSIONS

Structure evolution in thin Cu films, including twin formation and texture evolution, were simu- lated by a Monte Carlo Potts model based on sur- face/interface, grain boundary, and strain energy factors. Three different film thicknesses were simulated and result in either {111} or {001} out- of-plane texture depending on the energy minimi- zation competition between surface/interface and strain energy. For the 100 nm films, the process of grain growth proceeds as observed experimentally, with {111} grains growing first and gradually con- suming other types of orientations. For 500 nm films, a {511} twin component was observed that tended to minimize the total system energy when grain boundaries were considered as lower-energy coherent twins. For thicker films at 800 nm, the {001} grains grow rapidly during annealing due to the strain energy minimization criterion. Monte Carlo Potts modeling including energy minimiza- tion concepts and considers twin grain evolution can reasonably predict the evolution of grain structures and crystallographic textures in thin films, but the present model fails to capture effects of twin grain nucleation and growth accurately. Specific criteria for introducing twin grains into the structure must be developed in order to obtain better results for thicker films, where surface energy no longer dom- inates structure evolution.

![](./images/811819835670396930_7.jpg)

Fig. 7. Orientation maps showing the final simulated structures for 100 nm, 500 nm, and 800 nm films at 300°C.

## REFERENCES

1.  C.V. Thompson and R. Carel, *J. Mech. Phys. Solids* 44, 657 (1996).
2.  N.J. Park and D.P. Field, *Scripta Mater.* 54, 999 (2006).
3.  C.V. Thompson, *Annu. Rev. Mater. Sci.* 20, 245 (1990).
4.  C.V. Thompson and R. Carel, *Mater. Sci. Eng* B32, 211 (1995).
5.  M.T. Perez-Prado and J.J. Vlassak, *Scripta Mater.* 47, 817 (2002).
6.  A.D. Rollett and P. Manohar, *Chapter 4 of The Monte Carlo Method* (New York: Wiley-VCH, 2004).
7.  A.D. Rollet, *Prog. Mater. Sci.* 42, 79 (1997).
8.  G.N. Hassold and E.A. Holm, *Comput. Phys.* 7, 97 (1993).
9.  E.A. Holm and C.C. Battaile, *JOM* 53, 9 (2001).
10. Y. Saito and M. Enomoto, *ISIJ int.* 32, 267 (1992).
11. M. Winning, *Scripta Mater.* 54, 987 (2006).
12. M. Winning, *Phys. Status Solidi (a)* 201, 2867 (2004).
13. D.P. Field, R.C. Eames, and T.M. Lillo, *Scripta Mater.* 54, 983–986 (2006).
14. E.E. Danaf, S.R. Kalidindi, and R.D. Doherty, *Metall. Mater. Trans.* 30A, 1223 (1999).
15. A. Rohatgi, K.S. Vecchio, and G.T. Gray, III, *Metall. Mater. Trans.* 32A, 135 (2001).
16. K. Vanstreels, S.H. Brongersma, Zs. Tokei, L. Carbonell, W. De Ceuninck, J. D'Haen, and M. D'Olieslaeger, *J. Mater. Res.* 23, 642 (2008).
17. B.B. Rath, M.A. Imam, and C.S. Pande, *Mater. Phys. Mech.* 1, 61 (2000).

18. N.J. Park, D.P. Field, M.M. Nowell, and P.R. Besser, *J. Electron. Mater.* 34, 1500 (2005).
19. D. Walther, M.E. Gross, K. Evans-Lutterodt, W.L. Brown, M. Oh, S. Merchant, and P. Naresh, *Mater. Res. Soc. Symp. Proc.*, vol. 612 (2000), p. D10.1.
20. B.E. Sundquist, *Acta Metall.* 12, 67 (1964).
21. M. Mclean, *Acta Metall.* 19, 387 (1971).
22. W.C. Overton and J. Gaffney, *Phys. Rev.* 98, 969 (1955).
23. L.E. Murr, *Interfacial Phenomena in Metals and Alloys* (London: Addison-Wesley, 1975).
24. T. Read and W. Shockley, *Phys. Rev.* 78, 275 (1950).
25. S.I. Wright and R.J. Larsen, *J. Microsc.* 205, 245 (2002).
26. F.J. Humphreys and M. Hatherly, *Recrystallization an Re-lated Annealing Phenomena*, 2nd ed. (NY: Pergamon, 2004), pp. 376–377.
27. R.W. Balluffi, S.M. Allen, and W.C. Carter, *Kinetics of Materials* (New York: Wiley-Interscience, 2005), p. 342.
28. C.J. Chung, D.P. Field, N.J. Park, and R.G. Johnson, *Thin Solid Films* 517, 1977 (2009).
29. H. Gleiter, *Acta Metall.* 17, 1421 (1969).
30. C.S. Pande, M.A. Imam, and B.B. Rath, *Met. Trans. A* 21A, 2891 (1990).
31. S. Mahajan, C.D. Pande, M.A. Imam, and B.B. Rath, *Acta Mater.* 45, 2663 (1997).
32. D.P. Field, L.T. Bradford, M.M. Nowell, and T.M. Lillo, *Acta Mater.* 55, 4233 (2007).
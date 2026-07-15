# AN ATOMICALLY DISCRETE MODEL FOR INTERSTITIAL SOLID SOLUTIONS WITH F.C.C. METALS: THERMODYNAMIC PROPERTIES*

R. H. SILLER† and R. B. McLELLAN†

The thermodynamic functions of interstitial solid solutions have been calculated from a discrete-atom model. The model entails a computer simulation technique in which all the atoms of the solid act as in- dividual particles. The solvent-solvent interaction is represented by a two-body Morse potential and a "soft sphere" potential is proposed for the solvent-solute interaction. The parameters for the solvent- solute potential are chosen to be compatible with the experimentally measured lattice dilation as a function of composition and the activation energy for interstitial diffusion. The model is used to cal- culate the partial energy and excess (vibrational) entropy of carbon in nickel and the results are com- pared with experimental therodynamic data.

## MODELE ATOMIQUEMENT DISCONTINU POUR LES SOLUTIONS SOLIDES INTERSTITIELLES DES METAUX CUBIQUES A FACES CENTREES: PROPRIETES THERMODYNAMIQUES

Les fonctions thermodynamiques des solutions solides interstitielles ont été calculées à partir d'un modèle atomique discontinu. Le modèle nécessite une technique de simulation par computer dans laquelle tous les atomes du solide agissent comme des particules individuelles. L'interaction solvant-solvant est représentée par un potentiel de Morse à deux corps, et un potentiel de "sphère molle" est proposé pour l'interaction solvant-soluté. Les paramètres pour le potentiel solvant-soluté sont choisis de façonà être compatibles avec la dilatation du réseau mesurée expérimentalement en fonction de la composition et avec l'énergie d'activation pour la diffusion de l'interstitiel. Le modèle est utilisé pour calculer l'énergie partielle et l'entropie de vibration du carbone dans le nickel, et les résultats sont comparés avec les valeurs thermodynamiques expérimentales.

## EIN ATOMISTISCH DISKRETES MODELL FÜR INTERSTITIELLE LEGIERUNGEN KUBISCH-FLÄCHENZENTRIERTER METALLE: THERMODYNAMISCHE EIGENSCHAFTEN

Die thermodynamischen Funktionen von interstitiellen Legierungen wurden an einem atomistischen Modell berechnet. Das Modell führt zu einem Computer-Simulationsverfahren, bei dem die Atome des Festkörpers als einzelne Teilchen berücksichtigt werden. Die Solvent-Solvent-Wechselwirkung wird durch ein Morse-Zweikörperpotential beschrieben und für die Solvent-Fremdstoff-Wechselwirkung wird ein "weiche-Kugel"-Potential vorgeschlagen. Die Parameter für das Solvent-Fremdstoff-Potential wurden so gewählt, daß sie mit der experimentell bestimmten Abhängigkeit der Gitterdilatation von der Zusam- mensetzung und mit der Aktivierungsenergie der Diffusion von Zwischengitteratomen kompatibel waren. Mit dem Modell wurden die partielle Energie und Überschuß-(Vibrations-) Entropie von Kohlen- stoff in Nickel berechnet und mit experimentellen thermodynamischen Daten verglichen.

---

## INTRODUCTION

Recently the thermodynamic functions of many solid binary solutions containing an interstitial solute have been measured. More specifically the partial enthalpy $\bar{H}_{u}$ and partial excess entropy $\bar{S}_{u}^{v}$ at infinite dilution have been measured for the carbon solute atoms in many f.c.c. solid solutions.

It is of interest to compare theoretical estimates of these thermodynamic functions with the experi- mental data. In this study a computer technique is used to simulate the insertion of a solute atom into an octahedral site in an f.c.c. crystal. The partial enthalpy and partial excess entropy are calculated by compar- ing the energies and vibrational entropies of the perfect crystal and the crystal containing a solute atom. The assumption is made that the partial excess entropy is due only to the perturbation of the vibrational spectrum of the crystal accompanying the insertion of a solute atom into its interstitial site. The computer simulation calculation is based on assumed forms for both the interaction potential be- tween the solvent metal atoms and that between the solute atom and the metal atoms. Since the properties of the binary system (solute diffusion energy and the elastic constants of the solvent), used to obtain the solvent-solvent and solvent-solute interaction poten- tials are well-known for the Ni-C system, Ni-C was chosen as the base system for this calculation. Further- more, the thermodynamic functions of C in solid Ni have recently been measured. $^{(1)}$ The extension of the cal culation to other f.c.c. interstitial solid solutions is straightforward.

Generally, attempts at calculating point defect formation enthalpies and entropies have fallen into three categories: (a) those that assume that the defect is imbedded in an elastic continuum; (b) those that treat a defect crystal in two parts, an atomically discrete region immediately surrounding the defect and an elastic continuum in which the discrete region is imbedded; and (c) those that treat the entire defect crystal as being atomically discrete.

---

* Received August 5, 1970; revised August 27, 1970.
† William Marsh Rice University, Department of Mechani- cal and Aerospace Engineering and Materials Science, Houston, Texas 77001.

ACTA METALLURGICA, VOL. 19, MARCH 1971

McLellan⁽²⁾ obtained good agreement with experimental results in his treatment of monovacancies in metals by assuming an elastic continuum throughout the crystal. However, the situation is complicated when the defect is a solute atom since different atomic species are involved. In the completely elastic model, (a), the disparity between the size of the impurity defect and the size of the site it is to occupy in the crystal is the important factor influencing the predictions of the theoretical models. However, it is impossible to assert whether the atomic size as such is important, or some other property of the atom which, along with size, varies with atomic number. Oriani⁽³⁾ showed that the elastic model, when applied to the problem of the energetics of a solution, yields results of undeterminable agreement with experiment. In spite of these problems the completely elastic calculation of vibrational entropies has been shown to give fair agreement with experimental observations in substitutional solid solutions.⁽⁴⁾

Johnson et al.⁽⁵⁾ treated the systems C-$lpha$Fe, N-$lpha$Fe, C-V and N-V using a discrete-elastic model, (b). In this model the solute-solvent interactions were assumed to be two-body in nature, the characteristics of the interactions being calculated from observed properties of the solid solutions. Surrounding the defect a group of 531 atoms was considered as individual particles, again with two-body coupling forces, and the remainder of the crystal was considered to be an elastic continuum.

In the discrete-elastic model a problem arises in attempting to correlate the non-radial displacements, calculated for the metal atoms at the boundary between the discrete and elastic regions with the simple elastic theory which assumes radial displacements. In treating monovacancies in metals, Wynblatt⁽⁶⁾ avoided this problem by performing the calculation of vacancy formation entropy for a discrete, finite, spherical array, (c). He showed that this approach is qualitatively consistent with all the features of the elastic approach without explicit knowledge of the quantities which lead to complications in the formalism of linear continuum elasticity theory.

## THE MODEL

The partial energy, $\bar{E}_{u}$, (which is assumed equivalent to the experimentally measured partial enthalpy, $\bar{H}_{u}$) and the partial vibrational entropy, $\bar{S}_{u}{}^{v}$, are calculated by comparing the following two systems atom by atom: (1) a perfect metal crystal and an isolated impurity atom; and (2) the metal crystal with the impurity atom occupying an octahedral interstitial site. When the impurity atom is introduced into the metal crystal the metal atoms must alter their positions in order to attain a new equilibrium configuration. The thermodynamic functions are then calculated by making a comparison of the energy and the normal mode vibrational frequencies of each atom before and after the impurity has been introduced.

Let $W_{i}{}^{0}$ be the energy of atom $i$ in system (1) and $W_{i}{}'$ be the energy of atom $i$ in system (2). The partial energy is then
$$
\bar{E}_{u}=\sum_{i}\left\{W_{i}{ }^{\prime}-W_{i}{ }^{0}\right\} \tag{1}
$$

Similarly, the partial vibrational entropy may be written:
$$
\bar{S}_{u}{ }^{v}=\sum_{i}\left\{S_{i}{ }^{\prime}-S_{i}{ }^{0}\right\} \tag{2}
$$

Since the impurity atom in system (1) is completely isolated, its energy and entropy are zero. The energy zero is that of an atom at rest in a vacuum. Therefore, only the metal atoms in the perfect crystal contribute to the energy and entropy of system (1).

For a given atom in the perfect crystal
$$
W_{i}{ }^{0}=\Phi_{i}{ }^{0} \tag{3}
$$
where $\Phi_{i}{ }^{0}$ is the cohesive energy per atom of the pure metal. In this study a pairwise potential, $\psi$, is assumed to act between the atoms. The potential of a given atom is then
$$
\Phi_{i}=\sum_{j \neq i} \psi\left(r_{i j}\right) \tag{4}
$$
where $r_{i j}$ is the distance between atoms $i$ and $j$ and is of the form
$$
\begin{aligned}
r_{i j} & =\left|\mathbf{r}_{j}-\mathbf{r}_{i}\right| \\
& =\left\{\left(x_{j}-x_{i}\right)^{2}+\left(y_{j}-y_{i}\right)^{2}+\left(z_{j}-z_{i}\right)^{2}\right\}^{1 / 2}
\end{aligned}
$$

The cohesive energy per atom is given by
$$
\Phi_{i}{ }^{0}=\left[\Phi_{i}\right]_{r_{i j}=r_{i j}{ }^{0}}
$$
where all the atoms in the perfect crystal are in their equilibrium position, $r_{i j}{ }^{0}$.

The vibrational entropy of an atom is calculated on the assumption that the atoms are independent oscillators vibrating at the same frequency, $\nu_{i}{ }^{0}$, (Einstein approximation). Huntington et al.⁽⁷⁾ in a classic paper showed that neglecting the coupling of the vibration introduced only a small error in the entropy of the crystal. The energy levels, in one dimension, of an individual oscillator of frequency $\nu_{i}$ are,
$$
E_{n}=\left(n+\frac{1}{2}\right) h \nu_{i} \quad n=0,1,2,3 \ldots \tag{5}
$$

Therefore, the single particle canonical state sum in one dimension is
$$
\begin{aligned}
q & =\sum_{n=0}^{\infty} \exp \left(-E_{n} / k T\right) \\
& =\exp \left(-h \nu_{i} / 2 k T\right) \sum_{n=0}^{\infty}\left[\exp \left(-h \nu_{i} / k T\right)\right]^{n} \\
& =\frac{\exp \left(h \nu_{i} / 2 k T\right)}{\exp \left(h \nu_{i} / k T\right)-1}
\end{aligned}
\tag{6}
$$

In three dimensions the canonical state sum is $q^{3}$ and the free energy is given by
$$
F=-3 k T \ln q
\tag{7}
$$

The entropy of one atom is therefore
$$
\begin{aligned}
S_{i} & =-\left(\frac{\partial F}{\partial T}\right)_{V} \\
& =3 k\left\{\ln q+T\left(\frac{\partial \ln q}{\partial T}\right)_{V}\right. \\
& =3 k\left\{1+\ln \frac{k T}{h \nu_{i}}\right\}
\end{aligned}
\tag{8}
$$

In order to find the normal mode frequencies, $\nu_{i}$, of a given atom, its potential, $\Phi_{i}$, following the procedure of Wynblatt, $^{(6)}$ is expanded in a Taylor's series about its equilibrium position
$$
\begin{aligned}
\Phi_{i}= & {\left[\Phi_{i}\right]_{\left(x_{i}{ }^{0}, y_{i}{ }^{0}, z_{i}{ }^{0}\right)}+\left[\frac{\partial}{\partial \alpha} \Phi_{i}\right]_{\left(x_{i}{ }^{0}, y_{i}{ }^{0}, z_{i}{ }^{0}\right)} U_{\alpha} } \\
& +\frac{1}{2}\left[\frac{\partial^{2}}{\partial \alpha \partial \beta} \Phi_{i}\right]_{\left(x_{i}{ }^{0}, y_{i}{ }^{0}, z_{i}{ }^{0}\right)} U_{\alpha} U_{\beta},
\end{aligned}
$$
where $\alpha, \beta=x, y, z$.

This gives atomic force constants which are defined by
$$
F_{\alpha \beta}=\left[\frac{\partial^{2}}{\partial \alpha \partial \beta} \Phi_{i}\right]_{\left(x_{i}{ }^{0}, y_{i}{ }^{0}, z_{i}{ }^{0}\right)}
\tag{9}
$$
where $(x_{i}^{0}, y_{i}^{0}, z_{i}^{0})$ is the equilibrium position of atom $i$, and $U_{x}, U_{y}, U_{z}$ are the displacements of the moving atom from its equilibrium position. The equations of motion of atom $i$ moving in potential, $\Phi_{i}$ are then
$$
m \ddot{U}_{\alpha}=-\sum_{\beta=x, y, z} F_{\alpha \beta} U_{\beta}
\tag{10}
$$
where $m$ is the atomic mass and $\ddot{U}_{\alpha}$ is the second time derivative of the displacements. Assuming solutions to equations (10) of the form:
$$
U_{\alpha}=A_{\alpha} \sin \left(2 \pi \nu_{i} t+\eta\right)
$$
where $A_{\alpha}$ and $\eta$ are constants and $t$ is time,
$$
\ddot{U}_{\alpha}=-\left(4 \pi^{2} \nu_{i}^{2}\right) U_{\alpha}=-\lambda U_{\alpha}
\tag{11}
$$

Substituting (11) into (10)
$$
\lambda m U_{\alpha}=\sum_{\beta=x, y, z} F_{\alpha \beta} U_{\beta}
\tag{12}
$$

Solutions to equations (12) exist only if,
$$
\operatorname{det}\left(\begin{array}{ccc}
\left(F_{x x} / m\right)-\lambda & F_{x y} / m & F_{x z} / m \\
F_{x y} / m & \left(F_{y y} / m\right)-\lambda & F_{y z} / m \\
F_{x z} / m & F_{y z} / m & \left(F_{z z} / m\right)-\lambda
\end{array}\right)=0
$$

The three roots of this equation, $\lambda_{x}, \lambda_{y}, \lambda_{z}$, yield, from equation (11) the three appropriate normal frequencies for the particle of interest.

A truncated Morse potential, as modified byGirifalco and Weizer $^{(8)}$ and Cotterill and Doyama, $^{(9)}$ was chosen for the functional form of $\psi(r_{i j})$. In this potential
$$
\begin{aligned}
\psi\left(r_{i j}\right)=D[ & \exp \left\{-2 \alpha\left(r_{i j}-r_{0}\right)\right\} \\
& \left.-2 \exp \left\{-\alpha\left(r_{i j}-r_{0}\right)\right\}\right] \quad(13)
\end{aligned}
$$
is the energy of a pair of metal atoms, $i$ and $j$, separated by a distance, $r_{i j}$. The equilibrium distance of approach is $r_{0}, \alpha$ is a constant and $D$ is the dissociation energy since $\psi(r_{0})=-D$. The values of the constants, $\alpha, r_{0}$ and $D$ used in this calculation are given in Table 1. They are determined from the experimental values of the cohesive energy, lattice parameter, and compressibility as described by Girifalco and Weizer. $^{(8)}$ The truncation comes in the expression for the energy of a given atom, $i$,
$$
\begin{aligned}
\Phi_{i}=\frac{D}{2} \sum_{\substack{j=1 \\
j \neq i}}^{J}[ & \exp \left\{-2 \alpha\left(r_{i j}-r_{0}\right)\right\} \\
& \left.-2 \exp \left\{-\alpha\left(r_{i j}-r_{0}\right)\right\}\right] \quad(14)
\end{aligned}
$$
where $J$ is the total number of atoms which fall within the sphere of influence of atom $i$. Cotterill and Doyama $^{(9)}$ found that taking $J=176$ gave satisfactory results for their defect calculations.

Although there has been considerable effort to treat at least the cohesive forces in metals from first principles-such as representing metallic cohesion

<table>
<caption>Table 1. Morse function constants</caption>
<thead>
<tr>
<th>Metal</th>
<th>$\alpha$ ($\text{Å}^{-1}$)</th>
<th>$D$ (kcal/mol)</th>
<th>$r_{0}^{0}$ ($\text{Å}$)</th>
<th>Source</th>
</tr>
</thead>
<tbody>
<tr>
<td>Ni</td>
<td>1.3843</td>
<td>9.8935</td>
<td>2.799</td>
<td>This work*</td>
</tr>
<tr>
<td>Pd</td>
<td>1.6115</td>
<td>11.0870</td>
<td>2.900</td>
<td>This work*</td>
</tr>
<tr>
<td>Cu</td>
<td>1.2866</td>
<td>7.5035</td>
<td>2.913</td>
<td>Ref. 9*</td>
</tr>
<tr>
<td>Ag</td>
<td>1.3690</td>
<td>7.6595</td>
<td>3.115</td>
<td>Ref. 8†</td>
</tr>
<tr>
<td>Au</td>
<td>1.5384</td>
<td>11.0479</td>
<td>3.035</td>
<td>Ref. 11†</td>
</tr>
<tr>
<td>Pt</td>
<td>1.5687</td>
<td>16.2088</td>
<td>2.936</td>
<td>Ref. 11†</td>
</tr>
</tbody>
<tfoot>
<tr>
<td colspan="5">* Truncated</td>
</tr>
<tr>
<td colspan="5">† Not truncated</td>
</tr>
</tfoot>
</table>

<table><caption>TABLE 2. Comparison of Einstein frequencies</caption>
<thead>
  <tr>
    <th rowspan="2">Metal</th>
    <th>Calculated</th>
    <th colspan="2">Experimental(12)</th>
  </tr>
  <tr>
    <th>$\nu_{E}$<br>$(10^{13}\ \text{sec}^{-1})$</th>
    <th>$\nu_{E}$<br>$(10^{13}\ \text{sec}^{-1})$</th>
    <th>$\theta_{D}$<br>$(^{\circ}\text{K})$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Ni</td>
    <td>0.58</td>
    <td>0.72</td>
    <td>375</td>
  </tr>
  <tr>
    <td>Pd</td>
    <td>0.44</td>
    <td>0.44</td>
    <td>275</td>
  </tr>
  <tr>
    <td>Cu</td>
    <td>0.49</td>
    <td>0.51</td>
    <td>315</td>
  </tr>
  <tr>
    <td>Ag</td>
    <td>0.33</td>
    <td>0.34</td>
    <td>215</td>
  </tr>
  <tr>
    <td>Au</td>
    <td>0.30</td>
    <td>0.27</td>
    <td>170</td>
  </tr>
  <tr>
    <td>Pt</td>
    <td>0.39</td>
    <td>0.36</td>
    <td>225</td>
  </tr>
</tbody>
</table>

with a potential dependent on volume only—the semi-empirical, two-body Morse potential has been used successfully to calculate certain properties of perfect crystals and defect crystals. The pairwises interaction leads to the Cauchy relations, which are not satisfied in metals. However, satisfactory agree- ment has been achieved between the experimental and theoretical elastic constants and, also, the equa- tions of state have been adequately reproduced.(⁸) Defect calculations using the Morse potential have dealt mainly with vacancies in metals.(⁶·⁹⁻¹¹)

An important consideration in this study is how well the calculated normal frequencies, $v_{i}^{0}$, of an atom in the perfect crystal agree with the experimental Debye temperature $\theta_{D}$. These are not directly comparable since the $v_{i}^{0}$ that results from substituting equations (14) and (9) into equations (12) is the calculated Ein- stein frequency of the pure metal. However, using $\theta_{E}=0.75 \theta_{D}^{(12)}$ enables the comparison in Table 2 to be made for six f.c.c. metals.

Having calculated $\Phi_{i}^{0}$ and $v_{i}^{0}$ for a solvent atom in the perfect crystal, the impurity solute atom may now be introduced into an octahedral site. The interaction between the solute and solvent atoms will cause the solvents to find new equilibrium positions thereby changing the energy and vibrational spectrum of the defect crystal. This solute-solvent potential $\psi_{u v}$ is also assumed to be pairwise and its functional form will be discussed later. The potential of a solvent atom, $i$, in the defect crystal can then be written

$$
\Phi_{i}{ }^{\prime}=\psi_{u v}\left(r_{i u}\right)+\sum_{\substack{j=1 \\ j \neq i}}^{176} \psi\left(r_{i j}\right) \quad(15)
$$

where $\psi(r_{i j})$ is the Morse potential and $r_{i u}$ is the dis tance from the solvent atom to the solute atom. The equilibrium coordinates of atom $i$, $(x_{i}^{0},y_{i}^{0},z_{i}^{0})$, are defined by the conditions

$$
\begin{aligned}
{\left[\frac{\partial}{\partial x_{i}} \Phi_{i}{ }^{\prime}\right]_{\left(x_{i}{ }^{0}, y_{i}{ }^{0}, z_{i}{ }^{0}\right)} } & =\left[\frac{\partial}{\partial y_{i}} \Phi_{i}{ }^{\prime}\right]_{\left(x_{i}{ }^{0}, y_{i}{ }^{0}, z_{i}{ }^{0}\right)} \\
& =\left[\frac{\partial}{\partial z_{i}} \Phi_{i}{ }^{\prime}\right]_{\left(x_{i}{ }^{0}, y_{i}{ }^{0}, z_{i}{ }^{0}\right)}=0 \quad(16)
\end{aligned}
$$

These equations must be solved approximately by expanding them in a first order Taylor's series aboutthe equilibrium position, following Wynblatt(¹¹)

$$
\begin{aligned}
& \Phi_{i x}{ }^{\prime}= \\
& \quad\left[\left(\Phi_{i x}{ }^{\prime}+\Phi_{i x x}^{\prime} \Delta x+\Phi_{i x y}^{\prime} \Delta y+\Phi_{i x z}^{\prime} \Delta z\right)\right]_{\left(x_{1}{ }^{\prime}, y_{1}{ }^{\prime}, z_{1}{ }^{\prime}\right)}=0 \\
& \Phi_{i y}{ }^{\prime}= \\
& \quad\left[\left(\Phi_{i y}{ }^{\prime}+\Phi_{i y x}^{\prime} \Delta x+\Phi_{i y y}^{\prime} \Delta y+\Phi_{i y z}^{\prime} \Delta z\right)\right]_{\left(x_{1}{ }^{\prime}, y_{1}{ }^{\prime}, z_{1}{ }^{\prime}\right)}=0 \\
& \Phi_{i z}{ }^{\prime}= \\
& \quad\left[\left(\Phi_{i z}{ }^{\prime}+\Phi_{i z x}^{\prime} \Delta x+\Phi_{i z y}^{\prime} \Delta y+\Phi_{i z z}^{\prime} \Delta z\right)\right]_{\left(x_{1}{ }^{\prime}, y_{1}{ }^{\prime}, z_{1}{ }^{\prime}\right)}=0 \\
& \quad(17)
\end{aligned}
$$

where $\Phi_{i x}{ }^{\prime}=(\partial / \partial x) \Phi_{i}{ }^{\prime}, \Phi_{i x x}^{\prime}=\left(\partial^{2} / \partial x^{2}\right) \Phi_{i}{ }^{\prime}, \Phi_{i x y}^{\prime}=$ $(\partial^{2} / \partial x \partial y) \Phi_{i}^{\prime}$, etc., $(x_{i}^{\prime}, y_{i}^{\prime}, z_{i}^{\prime})$ is the first approxima tion for the equilibrium coordinates of atom $i$ and $\Delta x=(x_{i}^{\prime \prime}-x_{i}^{\prime}), \Delta y=(y_{i}^{\prime \prime}-y_{i}^{\prime})$ and $\Delta z=$ $(z_{i}^{\prime \prime}-z_{i}^{\prime})$ where $(x_{i}^{\prime \prime}, y_{i}^{\prime \prime}, z_{i}^{\prime \prime})$ is the second approxima tion for the equilibrium coordinates of atom $i$.

In order to facilitate the calculation, equations (17) may be applied to one atom in a symmetry shell surrounding the solute atom, with new coordinates, $(x_{i}^{\prime \prime}, y_{i}^{\prime \prime}, z_{i}^{\prime \prime})$, of the other atoms in this shell deduced by symmetry rather than applying the equations to each individual atom. If the octahedral site occupied by the solute has the coordinates $(0,0,\frac{1}{2})$, in units of the lattice constant, $a$, the six atoms that make up the first nearest-neighbor symmetry shell will have coordinates $(0,0,0),(0,0,1),(\frac{1}{2},0,\frac{1}{2}),(-\frac{1}{2},0,\frac{1}{2})$, $(0,\frac{1}{2},\frac{1}{2})$ and $(0,-\frac{1}{2},\frac{1}{2})$, as in Fig. 1. Their symmetry with respect to the defect site can be seen by trans- lating the origin to $(0,0,\frac{1}{2})$ and writing their coordi nates with respect to this origin as in Table 3. If one

![](./images/812399082822696964_1.jpg)

FIG. 1. The coordinates of the six first nearest-neighbor metal atoms to a solute atom occupying the interstitial site at $(0,0,\frac{1}{2})$. Coordinates are in units of one lattice parameter.

<table>
<caption>Table 3. List of first nearest-neighbor atoms of (0, 0, ½) octahedral site. Coordinates are in units of one lattice parameter</caption>
<thead>
<tr>
<th>Reference at (0, 0, 0)</th>
<th>Reference at (0, 0, ½)</th>
<th>Displacement</th>
</tr>
</thead>
<tbody>
<tr>
<td>(0, 0, 0)</td>
<td>(0, 0, −½)</td>
<td>(0, 0, −δ)</td>
</tr>
<tr>
<td>(0, 0, 1)</td>
<td>(0, 0, ½)</td>
<td>(0, 0, δ)</td>
</tr>
<tr>
<td>(½, 0, ½)</td>
<td>(½, 0, 0)</td>
<td>(δ, 0, 0)</td>
</tr>
<tr>
<td>(−½, 0, ½)</td>
<td>(−½, 0, 0)</td>
<td>(−δ, 0, 0)</td>
</tr>
<tr>
<td>(0, ½, ½)</td>
<td>(0, ½, 0)</td>
<td>(0, δ, 0)</td>
</tr>
<tr>
<td>(0, −½, ½)</td>
<td>(0, −½, 0)</td>
<td>(0, −δ, 0)</td>
</tr>
</tbody>
</table>

of the atoms is displaced a distance, $\delta$, from the defect, the other atoms must, by symmetry, have similar displacements as shown in Fig. 1. After finding the second approximation coordinates for the first symmetry shell, equations (17) are then applied to a atom in the second shell. The coordinates of the first shell are now $(x'', y'', z'')$ while for the rest of the atoms they are $(x', y', z')$, the first approximation, which are the original coordinates before the introduction of the defect. The coordinates $(x_{i}'', y_{i}'', z_{i}'')$ are found for this atom in the second shell enabling the $(x'', y'', z'')$ to be deduced for the rest of the atoms in that shell. This procedure is repeated for successive shells until, for a given shell, there is an arbitrarily small difference, say 0.0001 lattice parameters, between $(x'', y'', z'')$ and $(x', y', z')$. Those atoms outside this last shell are assumed to have their positions unaffected by the introduction of the defect. This process is iterated until there is an arbitrarily small difference in the coordinates of any given atom from one interation to the next. These coordinates $(x^{0}, y^{0}, z^{0})$ are assumed to be the final, equilibrium configuration of the defect crystal.

$\bar{E}_{u}$ and $\bar{S}_{u}^{v}$ can now be calculated knowing the equilibrium configurations for both the perfect and defect crystals. From equations (1), (3) and (15)

$$
\bar{E}_{u}=\Phi_{u v}+\sum_{i=1}^{N}\left\{\Phi_{i}{ }^{\prime}-\Phi_{i}{ }^{0}\right\} \tag{18}
$$

where $\Phi_{u v}=\frac{1}{2} \sum_{j} \psi_{u v}(r_{j u})$ is the potential of the solute atom in the defect crystal and $N$ is the total number of atoms affected by the defect. The new normal mode frequencies, $\nu_{i}^{f}$, for each solvent atom are calculated from equations (12), while the three normal frequencies of the solute atom, which are all the same and equal to $\nu_{u}$, are also calculated from equations (12) with

$$
F_{\alpha \beta}=0 \quad \alpha \neq \beta
$$

$$
F_{\alpha \beta}=\left[\frac{\partial^{2}}{\partial_{\alpha}{ }^{2}} \Phi_{u v}\right]_{(0,0,1 / 2)} \quad \alpha=\beta
$$

The partial vibrational entropy of solution can then be written

$$
\begin{aligned}
\bar{S}_{u}{ }^{v}= & 3 k\left(1+\ln \frac{k T}{h \nu_{u}}\right)+k \sum_{i=1}^{3 N}\left\{\left[1+\ln \frac{k T}{h \nu_{i}{ }^{f}}\right]\right. \\
& \left.-\left[1+\ln \frac{k T}{h \nu_{i}{ }^{0}}\right]\right\} \\
= & 3 k\left(1+\ln \frac{k T}{h \nu_{u}}\right)+k \ln \left(\prod_{i=1}^{3 N} \frac{\nu_{i}{ }^{0}}{\nu_{i}{ }^{f}}\right) \tag{19}
\end{aligned}
$$

where $T$ is taken to be $1000^\circ$K.

## RESULTS AND DISCUSSION

In this study the interstitial solid solution C-Ni is treated, using the above approach, as a system of atomically discrete particles. A carbon atom is introduced into the octahedral site located at (0, 0, ½) and equations (17) are solved for 24 symmetry shells, comprising 586 nickel atoms, extending 3.20 lattice parameters from the defect. The total number of nickel atoms, $N$, having their energies and vibrational frequencies affected by the introduction of the defect is taken to be 1048, extending 3.91 lattice parameters from the defect. The most crucial part of this treatment is the development of the carbon-nickel potential, $\psi_{u v}(r_{i u})$. The two experimental conditions which are matched to uniquely determine the potential are the dependence of the nickel lattice parameter on carbon concentration and the carbon motion energy.

The first consideration is the approximate size of the carbon atom and its effect on the subsequent dilation of the nickel lattice. Zwell et al.${ }^{(13)}$ have measured this dilation of the nickel lattice by dissolved carbon and their results are shown in Fig. 2. In order to simulate these experiments two assumptions about $\psi_{u v}$ are made: (1) $\psi_{u v}$ is short range, extending only to the six, first nearest-neighbor atoms of the octahedral site, and (2) the displacements of these six atoms arising from the introduction of the defect are radially outward and equal to $\delta$ as in Fig. 1. These assumptions allow equations (17) to be solved for shells 2-24 without knowing the explicit functional form of $\psi_{u v}$. The first nearest-neighbor atoms are constrained to have displacements, $\delta$. In order to calculate the dilation of the lattice as a function of carbon concentration all pairwise distances, $r_{i j}$, are compared before and after the introduction of the defect. The concentration is dependent on how many nickel atoms are taken into consideration. For example, first, the carbon atom and first nearest-neighbors are considered giving an atom ratio, $\theta=\frac{1}{6}$; next, the carbon atom and first and second nearest-neighbors are considered giving $\theta=\frac{1}{14}$; then, $\theta=\frac{1}{38}$

![](./images/812399082822696964_2.jpg)

FIG. 2. Plot showing the effect of varying $\delta$ on the calculated dilation of the nickel lattice. The lines are best fits on scattered points as those shown for $\delta=0.028$. The points become nonlinear for larger dilations.

is first, second and third nearest-neighbors plus carbon atom, and so on. This procedure is explained in detail in an Appendix.

Initially a hard-sphere carbon-nickel interaction based on the Pauling radius was considered. The Pauling radius for a carbon atom with six nearest neighbors is $0.89 \AA .^{(14)}$ This would give rise to a value of $\delta=0.115$ lattice parameters in order to have the octahedral site expand enough to accommodate the carbon atom. The calculated lattice dilation for this $\delta$ was unsatisfactory and is shown in Fig. 2. Other $\delta$ 's also tried are shown in Fig. 2. It can be seen that a $\delta$ of about 0.028 lattice parameters gives satisfactory agreement with experimental data. A hard-sphere carbon-nickel interaction was, for this reason, con- sidered unsatisfactory. The potential chosen must be constrained to give the energy minimum of the first nearest-neighbor nickel atoms at $\delta=0.028$.

The activation energy, $Q$, for interstitial diffusion in the carbon-nickel system is, experimentally, about35 kcal/mol.(15) A "soft sphere" carbon-nickel potential of the form
$$\psi_{u v}\left(r_{j u}\right)=A \exp \left(-\rho r_{j u}\right) \quad(20)$$
 is used in such a form as to be compatible with this carbon motion energy while constraining the first nearest-neighbor nickel atoms at $\delta=0.028$ . This procedure determines the constants $A$ and $\rho$ . A potential based on the carbon-iron interaction devel- oped by Johnson et al., $^{(5)}$ was also tried but with unsatisfactory results. This potential, which is strongly repulsive at close separations and has a minimum, gave an activation energy for diffusion that was too small.

The activation energy for diffusion is given by
$$Q=\sum_{i}\left\{W_{i}^{*}-W_{i}^{\prime}\right\}\qquad(21)$$
 where $W_{i}^{*}$ is the energy of atom $i$ when the defect is at the saddle point for diffusion. This saddle point is taken to be the tetrahedral site at $(\frac{1}{4}, \frac{1}{4}, \frac{1}{4})$ , giving a diffusion path as shown in Fig. 3. A direct octahedral- octahedral jump was eliminated since it was assumed to take much more energy than an octahedral-tetrahedral-octahedral jump for this model. The $W_{i}^{*}$  are calculated by solving equations (17) for 28 sym- metry shells about the point $(\frac{1}{4}, \frac{1}{4}, \frac{1}{4})$ . This comprises420 nickel atoms. $A$ and $\rho$ are adjusted until both the lattice dilation and carbon motion energy conditionsare satisfied. For nickel this gives $A=17,730 kcal /$  mol and $\rho=3.9686 \AA^{-1}$ .

Once $A$ and $\rho$ have been found, further approxima tions for the equilibrium positions for octahedral and tetrahedral occupancy can be found by iterating

![](./images/812399082822696964_3.jpg)

FIG. 3. The solid line represents an octahedral-tetra- hedral-octahedral diffusion jump with the saddle point at the tetrahedral site. The dotted line represents a direct octahedral-octahedral jump.

equations (17) under these conditions. These itera- tions are repeated until the difference from one itera- tion to the next for a given coordinate is no more than 0.0001 lattice parameters. Four iterations were necessary for octahedral occupancy and six for tetrahedral occupancy. The initial and final positions for an atom in each of the symmetry shells for both cases are given in Tables 4 and 5.

<table>
<caption>TABLE 4. Lattice positions of atoms in the octahedral config- uration for carbon in nickel*</caption>
<thead>
<tr>
<th>Perfect lattice position</th>
<th colspan="3">Displaced position</th>
<th>Number</th>
</tr>
</thead>
<tbody>
<tr>
<td>(0, 0, $\frac{1}{2}$)</td>
<td>0.0000</td>
<td>0.0000</td>
<td>0.5283</td>
<td>6</td>
</tr>
<tr>
<td>($\frac{1}{2}$, $\frac{1}{2}$, $\frac{1}{2}$)</td>
<td>0.4994</td>
<td>0.4994</td>
<td>0.4994</td>
<td>8</td>
</tr>
<tr>
<td>($\frac{1}{2}$, 0, 1)</td>
<td>0.5052</td>
<td>0.0000</td>
<td>1.0056</td>
<td>24</td>
</tr>
<tr>
<td>(1, $\frac{1}{2}$, 1)</td>
<td>1.0010</td>
<td>0.5014</td>
<td>1.0010</td>
<td>24</td>
</tr>
<tr>
<td>(0, 0, $\frac{3}{2}$)</td>
<td>0.0000</td>
<td>0.0000</td>
<td>1.4995</td>
<td>6</td>
</tr>
<tr>
<td>($\frac{1}{2}$, $\frac{1}{2}$, $\frac{3}{2}$)</td>
<td>0.5011</td>
<td>0.5011</td>
<td>1.5018</td>
<td>24</td>
</tr>
<tr>
<td>(0, 1, $\frac{3}{2}$)</td>
<td>0.0000</td>
<td>1.0021</td>
<td>1.5019</td>
<td>24</td>
</tr>
<tr>
<td>(1, 1, $\frac{3}{2}$)</td>
<td>1.0008</td>
<td>1.0008</td>
<td>1.5009</td>
<td>24</td>
</tr>
<tr>
<td>($\frac{1}{2}$, 0, 2)</td>
<td>0.5001</td>
<td>0.0000</td>
<td>1.9998</td>
<td>24</td>
</tr>
<tr>
<td>($\frac{1}{2}$, $\frac{3}{2}$, $\frac{3}{2}$)</td>
<td>0.5006</td>
<td>1.5007</td>
<td>1.5007</td>
<td>24</td>
</tr>
<tr>
<td>(1, $\frac{1}{2}$, 2)</td>
<td>1.0001</td>
<td>0.5003</td>
<td>2.0007</td>
<td>48</td>
</tr>
<tr>
<td>($\frac{3}{2}$, 0, 2)</td>
<td>1.5008</td>
<td>0.0000</td>
<td>2.0007</td>
<td>24</td>
</tr>
<tr>
<td>(0, 0, $\frac{5}{2}$)</td>
<td>0.0000</td>
<td>0.0000</td>
<td>2.4998</td>
<td>6</td>
</tr>
<tr>
<td>($\frac{3}{2}$, $\frac{3}{2}$, $\frac{3}{2}$)</td>
<td>1.5005</td>
<td>1.5005</td>
<td>1.5005</td>
<td>8</td>
</tr>
<tr>
<td>($\frac{1}{2}$, $\frac{1}{2}$, $\frac{5}{2}$)</td>
<td>0.5000</td>
<td>0.5000</td>
<td>2.4999</td>
<td>24</td>
</tr>
<tr>
<td>(1, 0, $\frac{5}{2}$)</td>
<td>1.0000</td>
<td>0.0000</td>
<td>2.5000</td>
<td>24</td>
</tr>
<tr>
<td>(1, $\frac{3}{2}$, 2)</td>
<td>1.0003</td>
<td>1.5004</td>
<td>2.0004</td>
<td>48</td>
</tr>
<tr>
<td>(1, 1, $\frac{5}{2}$)</td>
<td>1.0001</td>
<td>1.0001</td>
<td>2.5003</td>
<td>24</td>
</tr>
<tr>
<td>($\frac{1}{2}$, 2, 2)</td>
<td>0.5001</td>
<td>2.0003</td>
<td>2.0003</td>
<td>24</td>
</tr>
<tr>
<td>($\frac{1}{2}$, $\frac{3}{2}$, $\frac{5}{2}$)</td>
<td>0.5000</td>
<td>1.5002</td>
<td>2.5003</td>
<td>48</td>
</tr>
<tr>
<td>($\frac{1}{2}$, 0, 3)</td>
<td>0.5000</td>
<td>0.0000</td>
<td>2.9999</td>
<td>24</td>
</tr>
<tr>
<td>(0, 2, $\frac{5}{2}$)</td>
<td>0.0000</td>
<td>2.0002</td>
<td>2.5002</td>
<td>24</td>
</tr>
<tr>
<td>($\frac{3}{2}$, 2, 2)</td>
<td>1.5002</td>
<td>2.0002</td>
<td>2.0002</td>
<td>24</td>
</tr>
<tr>
<td>(1, $\frac{1}{2}$, 3)</td>
<td>1.0000</td>
<td>0.5000</td>
<td>3.0000</td>
<td>48</td>
</tr>
</tbody>
</table>

* The position vectors are in units of lattice parameters with their origins at the octahedral site. Also given is the number of symmetrically equivalent atoms within a symmetry shell.

<table>
<caption>TABLE 5. Lattice positions of atoms in the octahedral config- uration for carbon in nickel*</caption>
<thead>
<tr>
<th>Perfect lattice position</th>
<th colspan="3">Displaced position</th>
<th>Number</th>
</tr>
</thead>
<tbody>
<tr>
<td>($\frac{1}{4}$, $-\frac{1}{4}$, $\frac{1}{4}$)</td>
<td>0.2845</td>
<td>$-0.2845$</td>
<td>0.2845</td>
<td>4</td>
</tr>
<tr>
<td>($\frac{3}{4}$, $\frac{1}{4}$, $\frac{1}{4}$)</td>
<td>0.7485</td>
<td>0.2502</td>
<td>0.2502</td>
<td>12</td>
</tr>
<tr>
<td>($\frac{3}{4}$, $-\frac{3}{4}$, $\frac{1}{4}$)</td>
<td>0.7640</td>
<td>$-0.7640$</td>
<td>0.2533</td>
<td>12</td>
</tr>
<tr>
<td>($\frac{5}{4}$, $-\frac{1}{4}$, $\frac{1}{4}$)</td>
<td>1.2485</td>
<td>$-0.2506$</td>
<td>0.2506</td>
<td>12</td>
</tr>
<tr>
<td>($\frac{3}{4}$, $\frac{3}{4}$, $\frac{3}{4}$)</td>
<td>0.7508</td>
<td>0.7808</td>
<td>0.7508</td>
<td>4</td>
</tr>
<tr>
<td>($\frac{5}{4}$, $\frac{3}{4}$, $\frac{1}{4}$)</td>
<td>1.2515</td>
<td>0.7508</td>
<td>0.2514</td>
<td>24</td>
</tr>
<tr>
<td>($\frac{5}{4}$, $-\frac{3}{4}$, $\frac{3}{4}$)</td>
<td>1.2549</td>
<td>$-0.7538$</td>
<td>0.7538</td>
<td>12</td>
</tr>
<tr>
<td>($\frac{5}{4}$, $-\frac{5}{4}$, $\frac{1}{4}$)</td>
<td>1.2554</td>
<td>$-1.2554$</td>
<td>0.2499</td>
<td>12</td>
</tr>
<tr>
<td>($\frac{7}{4}$, $\frac{1}{4}$, $\frac{1}{4}$)</td>
<td>1.7495</td>
<td>0.2497</td>
<td>0.2497</td>
<td>12</td>
</tr>
<tr>
<td>($\frac{5}{4}$, $\frac{5}{4}$, $\frac{3}{4}$)</td>
<td>1.2507</td>
<td>1.2507</td>
<td>0.7507</td>
<td>12</td>
</tr>
<tr>
<td>($\frac{7}{4}$, $-\frac{3}{4}$, $\frac{1}{4}$)</td>
<td>1.7495</td>
<td>$-0.7503$</td>
<td>0.2500</td>
<td>24</td>
</tr>
<tr>
<td>($\frac{7}{4}$, $\frac{3}{4}$, $\frac{3}{4}$)</td>
<td>1.7510</td>
<td>0.7505</td>
<td>0.7505</td>
<td>12</td>
</tr>
<tr>
<td>($\frac{5}{4}$, $-\frac{5}{4}$, $\frac{5}{4}$)</td>
<td>1.2525</td>
<td>$-1.2525$</td>
<td>1.2525</td>
<td>4</td>
</tr>
<tr>
<td>($\frac{7}{4}$, $\frac{5}{4}$, $\frac{1}{4}$)</td>
<td>1.7511</td>
<td>1.2506</td>
<td>0.2509</td>
<td>24</td>
</tr>
<tr>
<td>($\frac{9}{4}$, $-\frac{1}{4}$, $\frac{1}{4}$)</td>
<td>2.2497</td>
<td>$-0.2501$</td>
<td>0.2501</td>
<td>12</td>
</tr>
<tr>
<td>($\frac{7}{4}$, $-\frac{5}{4}$, $\frac{3}{4}$)</td>
<td>1.7519</td>
<td>1.2517</td>
<td>0.7509</td>
<td>24</td>
</tr>
<tr>
<td>($\frac{9}{4}$, $\frac{3}{4}$, $\frac{1}{4}$)</td>
<td>2.2499</td>
<td>0.7498</td>
<td>0.2499</td>
<td>24</td>
</tr>
<tr>
<td>($\frac{7}{4}$, $\frac{5}{4}$, $\frac{5}{4}$)</td>
<td>1.7504</td>
<td>1.2503</td>
<td>1.2503</td>
<td>12</td>
</tr>
<tr>
<td>($\frac{9}{4}$, $-\frac{3}{4}$, $\frac{3}{4}$)</td>
<td>2.2497</td>
<td>$-0.7500$</td>
<td>0.7500</td>
<td>12</td>
</tr>
<tr>
<td>($\frac{7}{4}$, $-\frac{7}{4}$, $\frac{1}{4}$)</td>
<td>1.7518</td>
<td>$-1.7518$</td>
<td>0.2495</td>
<td>12</td>
</tr>
<tr>
<td>($\frac{9}{4}$, $-\frac{5}{4}$, $\frac{1}{4}$)</td>
<td>2.2499</td>
<td>$-1.2500$</td>
<td>0.2498</td>
<td>24</td>
</tr>
<tr>
<td>($\frac{7}{4}$, $\frac{7}{4}$, $\frac{3}{4}$)</td>
<td>1.7504</td>
<td>1.7504</td>
<td>0.7503</td>
<td>12</td>
</tr>
<tr>
<td>($\frac{9}{4}$, $\frac{5}{4}$, $\frac{3}{4}$)</td>
<td>2.2505</td>
<td>1.2502</td>
<td>0.7502</td>
<td>24</td>
</tr>
<tr>
<td>($\frac{7}{4}$, $-\frac{7}{4}$, $\frac{5}{4}$)</td>
<td>1.7509</td>
<td>$-1.7509$</td>
<td>1.2507</td>
<td>12</td>
</tr>
<tr>
<td>($\frac{11}{4}$, $\frac{1}{4}$, $\frac{1}{4}$)</td>
<td>2.7499</td>
<td>0.2500</td>
<td>0.2500</td>
<td>12</td>
</tr>
<tr>
<td>($\frac{9}{4}$, $-\frac{5}{4}$, $\frac{5}{4}$)</td>
<td>2.2507</td>
<td>$-1.2504$</td>
<td>1.2504</td>
<td>12</td>
</tr>
<tr>
<td>($\frac{9}{4}$, $\frac{7}{4}$, $\frac{1}{4}$)</td>
<td>2.2505</td>
<td>1.7502</td>
<td>0.2503</td>
<td>24</td>
</tr>
<tr>
<td>($\frac{11}{4}$, $-\frac{3}{4}$, $\frac{1}{4}$)</td>
<td>2.7499</td>
<td>$-0.7500$</td>
<td>0.2500</td>
<td>24</td>
</tr>
</tbody>
</table>

* The position vectors have their origins at the tetrahedral site.

Having found the equilibrium configuration for octahedral occupancy and the form of $\psi_{u v}$, $\bar{E}_{u}$ and $\bar{S}_{u}^{v}$ may now be calculated. Table 6 gives the calcu- lated and experimental values of these quantities. Figure 4 shows the shell by shell contribution to $\bar{E}_{u}$ and $\bar{S}_{u}^{v}$. As can be seen, the entropy agrees very well with experiment while the energy is low by about a factor of 2. One reason for this could be the fact that, from Fig. 4, the contributions to $E_{u}$ are localized around the defect whereas shells further away from

<table>
<caption>TABLE 6. Comparison of thermodynamic functions for carbon-nickel system</caption>
<thead>
<tr>
<th></th>
<th>$\bar{E}_{u}$ (kcal/mol)</th>
<th>$\bar{S}_{u}^{v}/k$</th>
</tr>
</thead>
<tbody>
<tr>
<td>Calculated</td>
<td>$-82$</td>
<td>3.90</td>
</tr>
<tr>
<td>Experimental(¹)</td>
<td>$-157$</td>
<td>3.95</td>
</tr>
</tbody>
</table>

![](./images/812399082822696964_4.jpg)

FIG. 4. Energy and entropy as a function of distance from the defect and symmetry shell.

the defect contribute significantly to $\bar{S}_{u}^{v}$. With the introduction of the defect the assumption that the Morse constants remain unchanged for the nickel- nickel interaction may not hold for nickel atoms immediately surrounding the carbon atom. Since it is these atoms that make the major contribution to $\bar{E}_{u}$, taking the metal-metal interaction as invariant around the defect would more likely introduce error into the calculation of $\bar{E}_{u}$ than $\bar{S}_{u}^{v}$.

The vibrational frequency, $\nu_{u}$, calculated for the carbon atom located at $(0,0,\frac{1}{2})$ is $\nu_{u}=1.06\times10^{13}$ $\sec^{-1}$. This is a reasonable value which reflects well on the choice of $\psi_{uv}$. It is about double the calculated Einstein frequency for nickel, $\nu_{i}^{0}=0.58\times10^{13}\sec^{-1}$ but it is still in the range where the classical approxi- mation is valid.

The general method outlined in the present calcu- lation can, of course, be applied to other interstitial systems provided the necessary input data are avail- able. For many f.c.c. systems of interest, such as carbon dissolved in iron or cobalt, there is a phase change and another structure becomes stable at low temperatures. Thus, although accurate thermo- dynamic and diffusivity data for the high-temperature f.c.c. phase are available, the elastic data necessary for the evaluation of the Morse potential constants are lacking. Furthermore the lattice dilation data used to evaluate the form of the soft-sphere solvent- solute potential are also generally unavailable.

Recently measurements have been made of the thermodynamic properties of carbon dissolved in the f.c.c. noble metals $^{(16,17)}$ and the elastic data are of course known. Thus, in these cases, the form of the Morse potential could be found. However, the lack of diffusivity and lattice parameter data precludes the evaluation of the soft-sphere interaction. Thus an extension of the present general calculation to other systems is made difficult due to the lack of input data. By using an arbitrary form for the solvent-solute interaction, calculations could be made for the systems for which elastic data are available, but the results would be of a more tentative nature.

## ACKNOWLEDGEMENT
The authors are grateful for the support provided by NASA Grant NsG-6-59.

## REFERENCES
1. W. W. DUNN, R. B. MCLELLAN and W. A. OATES, Trans. metall. Soc. A.I.M.E. 242, 2129 (1968).
2. R. B. MCLELLAN, Trans. metall. Soc. A.I.M.E. 245, 379(1969).
3. R. A. ORIANI, J. phys. Chem. Solids 2, 327 (1957).
4. R. B. MCLELLAN and R. SHUTTLEWORTH, J. phys. Chem. Solids 24, 453 (1963).
5. R. A. JOHNSON, G. J. DIENES and A. C. DAMASK, Acta Met. 12, 1215 (1964).
6. P. WYNBLATT, J. phys. Chem. Solids 30, 2201 (1969).
7. H. B. HUNTINGTON, G. A. SHIRN and E. S. WAJDA, Phys. Rev. 99, 1085 (1955).
8. L. A. GIRIFALCO and V. G. WEIZER, Phys. Rev. 114, 687(1959).
9. R. M. J. COTTERILL and M. DOYAMA, NBS Miscellaneous Publication No. 287, pp. 47-51 (1966).
10. L. A. GIRIFALCO and V. G. WEIZER, J. phys. Chem. Solids 12, 260 (1960).
11. P. WYNBLATT, J. phys Chem. Solids 29, 215 (1968).
12. N. F. Morr and H. JoNEs, The Theory of the Properties of Metals and Alloys, pp. 8-14. Dover (1958).
13. L. AWELL, E. J. FASISKA, Y. NAKADA and A. S. KEH, Trans. metall. Soc. A.I.M.E. 242, 765 (1968).
14. L. PAULING, The Nature of the Chemical Bond, p. 400. Cornell University Press (1960).
15. R. P. SMITH, Trans. metall. Soc. A.I.M.E. 236, 1224(1966).
16. R. B. MCLELLAN, Scripta Met. 3, 389 (1969).
17. R. H. SILLER, W. A. OATES and R. B. MCLELLAN, J. less-common Metals 16, 71 (1968).

## APPENDIX
### Simulation of lattice dilations by solute atoms
When an interstitial solute atom is introduced into a pure metal the measured "lattice parameter" of the ensuing solution is generally greater than the lattice

parameter of the pure metal. This "lattice param- eter" is taken to be the weighted average inter- planar spacing of all sets of parallel planes in the crystal. At any composition the lattice parameter can be written

$$
a=a_{0}+\Delta a \tag{A.1}
$$

where $a_{0}$ is the lattice parameter of the pure metal and $\Delta a$ is the change in the average interplanar spac- ing for that composition.

In treating the atoms in the defect crystal as discrete particles, it is convenient to define $\Delta a$ in terms of interatomic distances rather than interplanar spac- ings. The average change of all interplanar spacings is approximately equivalent to the average change of all interatomic distances. The change in one pairwise distance can be written

$$
\begin{aligned}
\Delta a_{i j} &=\frac{r_{i j}{ }^{\prime}-r_{i j}{ }^{0}}{r_{i j}{ }^{0}} a_{0} \\
&=\left[\frac{r_{i j}{ }^{\prime}}{r_{i j}{ }^{0}}-1\right] a_{0} \tag{A.2}
\end{aligned}
$$

where $r_{i j}{ }^{0}$ and $r_{i j}{ }^{\prime}$ are the interatomic spacings for atoms $i$ and $j$ before and after the introduction of the defect. The average change in lattice parameter is then

$$
\Delta a=\frac{1}{P} \sum_{i=1}^{n-1}\left\{\sum_{j=i+1}^{n} \Delta a_{i j}\right\} \tag{A.3}
$$

where $n$ is the number of metal atoms considered and $P$ is the number of pairs of atoms,

$$
\begin{aligned}
P &=\sum_{k=1}^{n}(n-k) \\
&=\frac{n(n-1)}{2} \tag{A.4}
\end{aligned}
$$

Since there is always one solute atom in this group of $n$ metal atoms, the atom ratio is

$$
\theta=\frac{1}{n} \tag{A.5}
$$

For convenience, only one atom per symmetry shell need be considered. The lattice parameter for a given $\theta=1 / n$ can then be expressed

$$
a=a_{0}+\frac{a_{0}}{n(n-1)} \sum_{i=1}^{M} S_{i}\left\{\sum_{\substack{j=1 \\ j \neq i}}^{n} \frac{r_{i j}{ }^{\prime}}{r_{i j}{ }^{0}}-1\right\} \tag{A.6}
$$

where $M$ is the number of symmetry shells chosen and $S_{i}$ is the number of atoms in the $i$ th shell. That is

$$
n=\sum_{i=1}^{M} S_{1}
$$

It is to be noted that the double summation in equation (A.6) counts each pair twice. This is taken account of by dividing by $n(n-1)$, twice the number of pairs.
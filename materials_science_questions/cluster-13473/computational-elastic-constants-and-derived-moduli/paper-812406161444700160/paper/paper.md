# Molecular reinforcement: a force field evaluation

Jürgen Wendling, Joachim H. Wendorff*

Fachbereich Physikalische Chemie
und Wissenschaftliches Zentrum für Materialwissenschaften,
Philipps-Universität, D-35032 Marburg, Germany

(Received: October 27, 1995; revised manuscript of November 28, 1995)

## SUMMARY:
Computer simulations on the basis of a force field approach are used to test the concept of molecular reinforcement and to get an insight into the parameters controlling the reinforcement effect. The finding is that molecular reinforcement may be as effective as fiber reinforcement. The molecular interactions between the matrix and the rigid molecules replace the adhesion between fiber and matrix and the axial ratio of the molecules plays the same role as the axial ratio of the fiber in the case of fiber reinforcement.

## Introduction
High-stiffness high-strength polymer materials are in demand for a broad range of applications. Routes towards such high performance polymers are based, for instance, on the reinforcement of thermoplastic or thermoset matrices by fibers $^{1,2)}$. Problems connected with this approach are, among others, the adhesion between fiber and matrix and in particular the control of the fiber orientation. It should be adjusted, in the ideal case, to the shape of the part to be reinforced and to the directions along which the major forces will act. A specially interesting case is the one where a planar or even isotropic reinforcement is required.

In the past, it has been proposed to replace the macroscopic fibers by stiff linear molecules to achieve this goal $^{3-6)}$. The underlying assumption is that a rigid molecule dispersed in a matrix will lead to an increase of the modulus along its direction of orientation in a way similar to the case of a macroscopic fiber. The specific laws governing the reinforcement effects on the molecular level may, of course, be different from those representing fiber reinforcement $^{7-9)}$.

The experimental verification of the concept of molecular reinforcement has turned out to be a major problem. The principal obstacle which has to be circumvented in this approach is the inherently strong immiscibility of rigid and flexible chain molecules originating from entropy effects. This has clearly been demonstrated by Flory based on lattice calculations $^{10,11)}$. These predict that compatibility exists in general only for very high concentrations of the solvent, no miscibility is predicted for the binary mixture of the two polymer species.

Yet, there are of course ways around this problem. These involve, among others, the introduction of side chains, of specific interactions $^{12,13,28)}$ etc. We were able to show some time ago that nonlinear molecules composed of rigid linear segments, i.e. rigid multipodes such as cross-like or star-like molecules, can be expected to display an enhanced solubility both in solvents and polymer matrices and should thus be favorable

© 1996, Hüthig & Wepf Verlag, Zug
CCC 1022-1344/96/$05.00

systems for investigations on molecular reinforcement effects $^{14-16)}$. We are actually able to observe a distinct reinforcement effect. The question which has, however, not been answered so far in a general way is in which way the reinforcement effect depends on the concentration and stiffness of the rigid molecules used, on their shape as well as on the molecular interactions.

This contribution addresses this problem. It describes the results of force field calculations on the mechanical properties of a matrix composed of a flexible polymer with and without the presence of the rigid molecules of various length and interactions and it compares these results with those expected for macroscopic fiber reinforcement.

## Procedure used to simulate the molecular reinforcement

The calculation of static and dynamic properties of the condensed state cannot be achieved presently employing ab initio or semiempirical quantum mechanical calculations. It still requires the use of an appropriate force field which contains terms representing the changes induced in the potential energy as bond lengths and bond angles are deformed as well as terms representing intermolecular interactions (Lennard Jones potential and Coulomb potential $^{17-19)}$. The corresponding force constants for the chemical structure considered are obtained either from experiments (such as vibrational properties) or from ab initio calculations. We used the force field Dreiding II $^{20)}$ to perform molecular dynamic simulations for the condensed state. The procedure consisted in filling chain molecules into an amorphous cell up to a density corresponding to the macroscopic one. The equilibration of these structures was performed using standard methods. The amorphous cell was subsequently subjected to dynamic simulations. The information which can be obtained from these simulations includes, among others, the chain conformation, the cohesion energy and the solubility parameter as well as the elastic stiffness tensor. It is in particular the elastic stiffness tensor we wanted to evaluate.

There are, in principle, two different routes which can be taken to obtain information on the stiffness of he condensed state. The first one involves the calculation of the minimized energy both for the undeformed and the deformed state. The deformation energy $F$ can be expressed (Hook's law) as

$$
F = \frac{V}{2} c_{ij}^T \varepsilon_i \varepsilon_j
$$

where the $\varepsilon_{i}$ represent the deformation, $c_{ij}^T$ the isothermal elastic siffness constants and $V$ is the volume under consideration $^{25)}$. The stiffness constants are thus obtained from the deformation energy as follows:

$$
c_{ij}^T = \frac{1}{V} \left( \frac{\partial^2 F}{\partial \varepsilon_i \partial \varepsilon_j} \right)
$$

This approach has successfully been employed by Suter et al. to model mechanical properties of polymers $^{21,22)}$. It has the disadvantage that errors in the energy characte- ristic of smaller systems show up strongly in the stiffness constants.

A second approach is based on fluctuation theory $^{23,24)}$. Fluctuation theory predicts that the ensemble averaged value of the cell parameter fluctuations $\langle\varepsilon_{i}\varepsilon_{j}\rangle$ are related to the elastic stiffness constants as follows $^{24)}$

$$
\langle\varepsilon_{i}\varepsilon_{j}\rangle = \frac{k_{\text{B}}T}{V} \left(c_{ij}^{T}\right)^{-1}
$$

so that we are able to derive the elastic stiffness constants from an analysis of the cell parameter fluctuations as follows:

$$
c_{ij}^{T} = \frac{k_{\text{B}}T}{V} \langle\varepsilon_{i}\varepsilon_{j}\rangle^{-1}
$$

$\langle\varepsilon_{i}\varepsilon_{j}\rangle^{-1}$ represents the elements of the tensor inverse to $\langle\varepsilon_{i}\varepsilon_{j}\rangle$. These fluctuations of the cell dimensions are acessible from $NPT$ dynamic simulations on amorphous cell.

## Results of the simulation
In all our simulations we used the polyarylate **1** (Scheme 1) as the flexible matrix polymer. In order to test whether the force field is appropriate for the polyarylate we first of all determined the chain conformation and the cohesive energy characteristic of the amorphous cell in a detailed thermal equilibrium. These values agreed closely with experimental ones as shown in Tab. 1.

Scheme 1:

![](./images/812406161444700160_1.jpg)

Tab. 1. Comparison of simulated values, obtained for three amorphous cells (different runs),
a, b, c, with values from literature ($E_{\text{coh}}$: cohesive energy; $\delta$: solubility parameters)

<table>
  <thead>
    <tr>
      <th></th>
      <th>Cell a</th>
      <th>Cell b</th>
      <th>Cell c</th>
      <th>Average</th>
      <th>Deviation</th>
      <th>Literature</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Density in $\text{g/cm}^3$</td>
      <td>1.178</td>
      <td>1.169</td>
      <td>1.169</td>
      <td>1.178</td>
      <td>0.0045</td>
      <td>$1.21^{26)}$</td>
    </tr>
    <tr>
      <td>$E_{\text{coh}}/(\text{cal/mol})$</td>
      <td>24.52</td>
      <td>27.1</td>
      <td>26.41</td>
      <td>26.01</td>
      <td>1.336</td>
      <td></td>
    </tr>
    <tr>
      <td>$\delta/(\text{cal/cm}^3)^{1/2}$</td>
      <td>8.96</td>
      <td>9.44</td>
      <td>9.28</td>
      <td>9.23</td>
      <td>0.244</td>
      <td>$10.05^{27)}$</td>
    </tr>
  </tbody>
</table>

Fig. 1. shows the cell axes fluctuations of the polyarylate 1 chosen as the matrix
material at room temperature. It is obvious that the fluctuations are very similar along
all axes, as expected for an isotropic system. For the cell angles, we observed the same
result: the fluctuations of the angles are of similar amplitudes. The evaluation of these
fluctuations on the basis of the equation given above leads to the elastic stiffness tensor
shown in Tab. 2a. We used this tensor to derive values for the tensile modulus $E$ and
the shear modulus $G$. These are given in Tab. 3 together with experimental values. It
is apparent that the predictions agree closely with the experimental results.

![](./images/812406161444700160_2.jpg)

Fig. 1. Cell axes fluctua-
tions of an amorphous cell
composed of polyarylate 1
chains (see Scheme 1) at a
temperature of 300 K

We subsequently incorporated poly($p$-phenylene) molecular rods 2 (Scheme 1) of
infinite length into the amorphous cell. Fig. 2 represents the cell containing one rigid
rod molecule and the polyarylate 1 matrix. The introduction of the poly($p$-phenylene)
leads to a strong reduction of the cell axis fluctuation along the direction defined by
the orientation of the rigid rod as apparent from Fig. 3. The corresponding stiffness
tensor is given in Tab. 2b. The derived tensile moduli are 12 GPa in the direction of fiber
orientation ($E_{33}$) and 2.08 GPa for the transverse modulus $E_{11}$. It is apparent that the
tensile modulus $E_{33}$ is strongly increased. The magnitude of the increase will depend,
of course, on the concentration of rigid rods. The values obtained for various concen-
trations are plotted in Fig. 4. It seems that the calculated moduli are located close to
a straight line connecting the value of the matrix and of the rigid rods. We will consider
this point further below in some detail.

The next step consisted in the incorporation of finite poly($p$-phenylene) molecular
rods 2 of different length oriented along a given direction. The expectation is that the

Tab. 2. Elastic stiffness matrix for different systems

$$
c = \begin{bmatrix}
\mathbf{6.91} & \mathbf{4.17} & \mathbf{4.66} & 0.1 & 0.25 & 0.16 \\
\mathbf{4.17} & \mathbf{5.97} & \mathbf{4.14} & -0.04 & -0.1 & 0.34 \\
\mathbf{4.66} & \mathbf{4.14} & \mathbf{7} & 0.09 & 0.03 & 0.17 \\
0.1 & -0.04 & 0.09 & \mathbf{0.91} & 0.13 & 0 \\
0.25 & -0.1 & 0.03 & 0.13 & \mathbf{0.9} & 0.05 \\
0.16 & 0.34 & 0.17 & 0 & 0.05 & \mathbf{0.95}
\end{bmatrix} \quad [\text{GPa}]
$$

a) amorphous polyarylate

$$
c = \begin{bmatrix}
\mathbf{5.36} & \mathbf{4.95} & \mathbf{1.98} & 0.18 & 0.02 & 0.55 \\
\mathbf{4.95} & \mathbf{7.46} & \mathbf{1.53} & -0.23 & -0.07 & 1.18 \\
\mathbf{1.98} & \mathbf{1.53} & \mathbf{20} & 0.29 & 2 & 0.68 \\
0.18 & 0.23 & 0.29 & \mathbf{1} & 0.13 & -0.28 \\
0.02 & 0.07 & 2 & 0.13 & \mathbf{0.65} & -0.11 \\
0.55 & 1.18 & 0.68 & -0.28 & -0.11 & \mathbf{1.15}
\end{bmatrix} \quad [\text{GPa}]
$$

b) amorphous polyarylate containing one chain of
poly($p$-phenylene) with infinite length

$$
c = \begin{bmatrix}
\mathbf{5.38} & \mathbf{4.06} & \mathbf{4.24} & -0.02 & 0 & -0.02 \\
\mathbf{4.06} & \mathbf{7.01} & \mathbf{4.03} & 0.05 & -0.3 & -0.07 \\
\mathbf{4.24} & \mathbf{4.03} & \mathbf{9.18} & -0.05 & 0.02 & -0.04 \\
-0.02 & 0.05 & -0.05 & \mathbf{0.88} & 0.12 & -0.08 \\
0 & -0.3 & 0.02 & 0.12 & \mathbf{0.97} & 0.05 \\
-0.02 & -0.07 & -0.04 & -0.08 & 0.05 & \mathbf{0.47}
\end{bmatrix} \quad [\text{GPa}]
$$

c) amorphous polyarylate containing one chain of
poly($p$-phenylene) with finite length of $100\ \mathring{\text{A}}$

$$
c = \begin{bmatrix}
\mathbf{12.7} & \mathbf{11.4} & \mathbf{7.7} & -0.08 & -1.47 & 0.19 \\
\mathbf{11.4} & \mathbf{15.6} & \mathbf{12.2} & -1.35 & -0.99 & 0.26 \\
\mathbf{7.7} & \mathbf{12.2} & \mathbf{20} & -0.85 & -1.04 & 0.28 \\
-0.08 & -1.35 & -0.85 & \mathbf{3.54} & 0.37 & 0.38 \\
-1.47 & -0.99 & -1.04 & 0.37 & \mathbf{3.69} & 0.01 \\
0.19 & 0.26 & 0.28 & 0.38 & 0.01 & \mathbf{0.52}
\end{bmatrix} \quad [\text{GPa}]
$$

d) amorphous polyarylate containing one chain of
poly($p$-benzamide) with finite length of $100\ \mathring{\text{A}}$

$$
c = \begin{bmatrix}
\mathbf{8.21} & \mathbf{2.44} & \mathbf{1} & -0.61 & 1.62 & 0.85 \\
\mathbf{2.44} & \mathbf{17.8} & \mathbf{4.37} & 3.16 & 1.98 & -0.3 \\
\mathbf{1} & \mathbf{4.37} & \mathbf{13.7} & -1.12 & 2.02 & 2.16 \\
-0.61 & 3.16 & -1.12 & \mathbf{5.7} & 0.58 & -1.12 \\
1.62 & 1.98 & 2.02 & 0.58 & \mathbf{2.47} & -0.11 \\
0.85 & -0.3 & 2.16 & -1.12 & -0.11 & \mathbf{3.45}
\end{bmatrix} \quad [\text{GPa}]
$$

e) amorphous polyarylate containing one cross-molecule of
poly($p$-benzamide) with finite arm length of $100\ \mathring{\text{A}}$ each

Tab. 3. Comparison of simulated and experimental data on Lamé constants $\lambda$ and $\mu$, tensile modulus $E$, shear modulus $G$, bulk modulus $B$ and Poisson ratio $v$

<table>
  <thead>
    <tr>
      <th></th>
      <th>Calculated</th>
      <th>Literature</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$\lambda$/GPa</td>
      <td>4.32</td>
      <td>$\approx 4^{\text{a)}}$</td>
    </tr>
    <tr>
      <td>$\mu$, $G$/GPa</td>
      <td>0.92</td>
      <td>$0.8 - 0.9^{26)}$</td>
    </tr>
    <tr>
      <td>$E$/GPa</td>
      <td>2.6</td>
      <td>$2.3 - 2.5^{26)}$</td>
    </tr>
    <tr>
      <td>$B$/GPa</td>
      <td>4.933</td>
      <td>$\approx 4.57^{\text{a)}}$</td>
    </tr>
    <tr>
      <td>$v$</td>
      <td>0.412</td>
      <td>$\approx 0.42^{\text{a)}}$</td>
    </tr>
  </tbody>
</table>

a) Calculated from the experimental values of $E$ and $G$.

![](./images/812406161444700160_3.jpg)

Fig. 2. Amorphous cell composed of poly($p$-phenylene) chain 2 (Scheme 1) and a polyarylate matrix 1

poly($p$-phenylene) displays no specific interactions with the polyarylate 1 such as for instance hydrogen bonds. The evaluation along the lines discussed above leads to the stiffness tensor given in Tab. 2c in one case and the elastic moduli displayed in Tab. 4. The predictions in this particular case are that the tensile modulus $E_{33}$ is increased by about a factor of 2 and 4, respectively. The length of the molecules plays thus a role similar to the case of macroscopic reinforcement. The tensile moduli $E_{11}$ perpendicular to this direction are hardly influenced and this also holds for the shear modulus

Fig. 3. Cell axes fluctua-
tions of an amorphous cell
composed of polyarylate 1
chains as matrix and poly-
(p-phenylene) chain 2 as
reinforcement agent at a
temperature of 300 K

![](./images/812406161444700160_4.jpg)

Fig. 4. Dependence of the
tensile moduli on the con-
centration of the stiff mo-
lecules

![](./images/812406161444700160_5.jpg)

Tab. 4. Comparison between simulted values and values predicted on the basis of the
Halpin-Tsai equation (symbols see section 'Laws governing fiber reinforcement')

<table>
<thead>
<tr>
<th>Rigid molecule</th>
<th>$\phi$</th>
<th>Length
in $\mathring{A}$</th>
<th>$\zeta$</th>
<th>$E_{33}$/GPa
(Halpin-Tsai)</th>
<th>$E_{33}$/GPa
(simulation)</th>
</tr>
</thead>
<tbody>
<tr>
<td>poly($p$-phenylene)</td>
<td>0.094</td>
<td>100</td>
<td>40</td>
<td>10.9</td>
<td>5.62</td>
</tr>
<tr>
<td>poly($p$-phenylene)</td>
<td>0.175</td>
<td>170</td>
<td>68</td>
<td>26.4</td>
<td>11.2</td>
</tr>
<tr>
<td>poly($p$-benzamide)</td>
<td>0.094</td>
<td>100</td>
<td>40</td>
<td>10.2</td>
<td>9.33</td>
</tr>
<tr>
<td>poly($p$-benzamide)</td>
<td>0.175</td>
<td>170</td>
<td>68</td>
<td>23.7</td>
<td>18.1</td>
</tr>
<tr>
<td>poly($p$-benzamide) (cross)</td>
<td>0.233</td>
<td>$2\times100$</td>
<td>40</td>
<td>12, 12</td>
<td>9.4, 13.3</td>
</tr>
</tbody>
</table>

$G_{44}$. Again we will compare the results obtained so far with the corresponding results
for fiber reinforcement below.

Finally we will consider the effect of specific molecular interactions on the
reinforcement effect. We placed for this purpose aromatic rigid poly($p$-benzamide) 3
(Scheme 1) of different length in the polyarylate matrix 1. The computer analysis of
the interactions showed the presence of hydrogen bonding, i. e., the presence of specific

interactions between the rigid molecules and the matrix in agreement with our speculations. The additional interaction energies obtained by replacing the poly(p-phenylene) 2 with poly(p-benzamide) 3 are 321 kJ/mol and 467 kJ/mol for the two different structures under investigation. The analysis of the cell parameter fluctuations leads to the result that the reinforcement effect of the polyamide is substantially larger at equal length of the molecular fiber compared to the one due to the poly(p-phenylene) (Tabs. 2d and 4). It thus seems the molecular interactions play a similar role in molecular reinforcement as the interfacial adhesion in the case of fiber reinforcement.

Tab. 4 also contains the results of computer simulations on the molecular reinforcement effect of rigid cross-like poly(p-benzamide) molecules 4 (Scheme 1). The amorphous cell containing such a cross-like molecule is shown in Fig. 5. The analysis of the cell parameter fluctuations leads to the stiffness matrix displayed in Tab. 2e. It is obvious that the tensile moduli are increased along the two directions defined by the orientation of the cross-molecule. The shear moduli are, on the other hand, not affected. The cross-molecules leads thus to a planar reinforcement, the magnitude being controlled by the axial ratio of the arms.

The logical question to be answered next is whether molecular reinforcement is as effective as the macroscopic fiber reinforcement.

![](./images/812406161444700160_6.jpg)

Fig. 5. Amorphous cell composed of a cross-like multipode and a polyarylate 1 matrix

### Laws governing fiber reinforcement

We used the Halpin-Tsai equation to calculate the reinforcement effects of fibers of limited length and to get criteria on which we could judge the effectivity of molecular reinforcement. Within this continuum approach the tensile modulus $E_{33}$ along the fiber orientation direction is given for a unidirectional orientation of the fibers by $^7)$

$$
\frac{E_{33}}{E_{\mathrm{m}}}=\frac{1+\zeta \eta \phi}{1-\eta \phi} \quad \text { with } \quad \eta=\frac{E_{\mathrm{f}} / E_{\mathrm{m}}-1}{E_{\mathrm{f}} / E_{\mathrm{m}}+\zeta}
$$

where $\zeta=2(l / d)$ corresponds to twice the axial ratio, i.e. ratio of the length $l$ to the width $d$. $\phi$ represents the volume fraction of the reinforcing species having the modulus $E_{\mathrm{f}}$, and $E_{\mathrm{m}}$ is the modulus of the matrix material. Assuming fibers of infinite length we obtain a simple mixing law

$$
E_{33}=E_{\mathrm{f}} \phi+E_{\mathrm{m}} \cdot(1-\phi)
$$

which yields a linear variation of the tensile modulus with the concentration.

Fig. 6 shows the reinforcement effect along the fiber direction predicted for various lengths (aspect ratios) of the fiber including an infinite length. The result is first of all that the simulations for infinite chains agree with the simple mixing law given above,

![](./images/812406161444700160_7.jpg)

which is not very surprising. The predictions of the moduli with rigid chains of finite length are displayed in Fig. 7. A diagonal line should be obtained for the case of perfect adhesion between the rigid chain molecules and the matrix polymer. We see that the values obtained by simulations are far below the ones predicted by the Halpin-Tsai equation if the interactions are weak. One approaches the values characteristic of fiber reinforcement with perfect adhesion if specific interactions are present.

### Comparison with the results of experiments

Fig. 8 shows, as an example, the effect of the addition of $\lambda$-shaped molecules $\mathbf{5}$ (Scheme 1) on the absolute value of the tensile modulus $^{16)}$. It is apparent that this value increases as the $\lambda$-shaped molecules are added, independent of the temperature.

The upper value obtained corresponds to an increase in magnitude by a factor of about 2.6.

It has to be pointed out that this strong effect takes place along all axes, it is not restricted to a preferred direction as in the case of fiber reinforcement. In the following we will try to analyze this result using the composite theory to evaluate its predictions.

![](./images/812406161444700160_8.jpg)

Fig. 7. Comparison of the predictions from the Halpin-Tsai equation for fiber reinforcement, for fibers with different aspect ratios and simulations with different interactions between rigid chain molecules 2 (□) and 3 (●) and the polyarylate 1 matrix. A diagonal line would represent the case of ideal adhesion between the rigid chain molecules and the matrix polymer

![](./images/812406161444700160_9.jpg)

Fig. 8. Reinforcement effect due to the incorporation of 10 wt.-% of a λ-molecule 5 (cf. Scheme 1), experimental results $^{16)}$

Using the experimentally obtained modulus for the matrix of 2.5 GPa and of 150 GPa for the rigid molecule and an axial ratio of 10 (based on the MNDO-results for the λ-molecules) we obtain the predictions shown in Tab. 5 for the case of a uniaxial reinforcement. It is obvious that the experimental values are larger than the predicted ones which is not surprising in view of the fact that we have considered a random orientation of rod-like molecules rather than of planar molecules.

So the conclusion is: the concept of molecular reinforcement works, the length of the molecules and the interactions with the matrix control the magnitude of the reinforcement effect.

<table>
<caption>Tab. 5. Comparison of theoretical values (see references) with experimental ones</caption>
<thead>
<tr>
<th>Molecule</th>
<th>$E_{33}/E_{\text{m}}$ (model) $^{7)}$</th>
<th>$E_{\text{iso}}/E_{\text{m}}$ (model) $^{9)}$</th>
<th>$E/E_{\text{m}}$ (experiment)</th>
</tr>
</thead>
<tbody>
<tr>
<td>$\lambda$ ($n = 1$)</td>
<td>2.07</td>
<td>1.4</td>
<td>1</td>
</tr>
<tr>
<td>$\lambda$ ($n = 2$)</td>
<td>2.46</td>
<td>1.55</td>
<td>1.77</td>
</tr>
<tr>
<td>$\lambda$ ($n = 3$)</td>
<td>2.82</td>
<td>1.68</td>
<td>2.62</td>
</tr>
</tbody>
</table>

We gratefully acknowledge financial support by the *Deutsche Forschungsgemeinschaft* (DFG).

$^{1)}$ A. R. Brunsell, Ed., *"Fibre Reinforcements for Composite Materials"*, Elsevier, Amsterdam 1988

$^{2)}$ T. W. Chou, volume editor, *"Structure and Properties of Composites"*, in *"Materials Science and Technology"* R. W. Cahn, P. Haasen, E. J. Kramer, Eds., 13, VCH, Weinheim 1993

$^{3)}$ G. Husman, T. Helminiak, W. Adams, D. Wiff, C. Benner, *J. Am. Chem. Soc.* **40**, 797 (1974)

$^{4)}$ M. Takayanagi, T. Ogata, M. Morikawa, T. Kai, *J. Macromol. Sci.-Phys.* **B17**, 591 (1980)

$^{5)}$ W. Brostow, *Kunststoffe* **78**, 411 (1988)

$^{6)}$ E. H. Kerner, *Proc. Phys. Soc., London* **69B**, 808 (1956)

$^{7)}$ J. C. Halpin, J. L. Kardos, *Polym. Eng. Sci.* **16**, 344 (1976)

$^{8)}$ R. Hill, *J. Mech. Phys. Solids* **11**, 357 (1963)

$^{9)}$ D. R. Wiff, G. M. Lenke, P. D. Fleming III, *J. Polym. Sci., Part B: Polym. Phys.* **32**, 2555 (1994)

$^{10)}$ P. J. Flory, *Adv. Polym. Sci.* **59**, 2 (1984)

$^{11)}$ P. J. Flory, *Macromolecules* **11**, 1138 (1978)

$^{12)}$ M. Ballauff, *Chem. Unserer Zeit* **22**, 63 (1988)

$^{13)}$ M. Ballauff, *Angew. Chem.* **101**, 261 (1989)

$^{14)}$ U. Gallenkamp, *PhD-Thesis*, Darmstadt 1989

$^{15)}$ S. Claßen, U. Gallenkamp, M. Wolf, J. H. Wendorff, in *"Integration of Fundamental Polymer Science and Technology"* IV, P. Lemstra, Ed., p. 232, Elsevier, London 1989

$^{16)}$ D. Braun, C. Hartig, M. Reubold, M. Soliman, J. H. Wendorff, *Makromol. Chem., Rapid Commun.* **14**, 663 (1993)

$^{17)}$ J. J. P. Stewart, *J. Comput.-Aided Mol. Des.* **4**, 1 (1990)

$^{18)}$ T. A. Clark, *"A Handbook of Computational Chemistry"*, J. Wiley, New York 1985

$^{19)}$ R. J. Roe, Ed., *"Computer Simulations of Polymers"*, Prentice Hall, Englewood Cliffs, NJ 1991

$^{20)}$ S. L. Mayo, W. A. Goddard III, *J. Chem. Phys.* **94**, 8891 (1990)

$^{21)}$ D. Theodorou, U. W. Suter, *Macromolecules* **19**, 139 (1985)

$^{22)}$ G. C. Rutledge, U. W. Suter, *Polymer* **32**, 2179 (1991)

$^{23)}$ M. Parrinello, A. Rahman, *J. Chem. Phys.* **76**, 2662 (1982)

$^{24)}$ A. A. Gusev, M. M. Zehnder, U. W. Suter, *J. Chem. Phys.*, submitted

$^{25)}$ L. D. Landau, E. M. Lifschitz, *"Lehrbuch der theoretischen Physik"*, Vol. 5, Akademie Verlag, Berlin 1979

$^{26)}$ L. M. Robeson, J. M. Tibbitt, *"History of Polyarylates"*, in *"High Performance Polymers"*, R. B. Seymour, G. S. Kirshbaum, Eds., Elsevier, New York 1986

$^{27)}$ D. W. Van Krevelen, P. J. Hoftyzer, *"Properties of Polymers"*, Elsevier, Amsterdam 1972

$^{28)}$ C. D. Eisenbach, J. Hofmann, K. Fischer, *Macromol. Rapid Commun.* **15**, 117 (1994)
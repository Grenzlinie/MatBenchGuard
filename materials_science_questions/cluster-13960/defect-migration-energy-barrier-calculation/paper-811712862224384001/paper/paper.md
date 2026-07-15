PHYSICAL REVIEW B 82, 144115 (2010)

# Angular-dependent interatomic potential for the aluminum-hydrogen system

F. Apostol* and Y. Mishin $^{\dagger}$
Department of Physics and Astronomy, MSN 3F3, George Mason University, Fairfax, Virginia 22030, USA
(Received 6 August 2010; published 22 October 2010)

We report on the development of an angular-dependent interatomic potential for hydrogen and the aluminum-hydrogen system. The potential reproduces properties of diatomic hydrogen gas, accurate solution energies of hydrogen atoms in crystalline Al, the energetic preference of the tetrahedral interstitial site occupation over octahedral, the hydrogen diffusion barrier in Al, and a number of other properties. Some of the results predicted by the potential have been tested by molecular dynamics simulations. It is suggested that the new potential can be used in atomistic simulations of the effect of dissolved hydrogen on deformation and fracture of Al, a problem which is relevant to hydrogen-induced degradation of Al alloys.

DOI: 10.1103/PhysRevB.82.144115
PACS number(s): 61.50.Ah, 61.66.Fn, 61.72.S−, 64.70.Hz

## I. INTRODUCTION

Hydrogen-induced degradation of materials, including hydrogen embrittlement, continues to receive much attention due to its technological significance. $^{1-3}$ Hydrogen absorption is one of the mechanisms of the environmental effect on Al-based alloys for aerospace applications. Under normal conditions, an aluminum oxide layer protects the underlying Al alloy from the environment. But in the presence of mechanical stresses, the oxide layer can develop microscopic cracks exposing the alloy surface. Water molecules present in humid air can adsorb on the surface and dissociate producing atomic hydrogen (hydrogen uptake). $^{4}$ The atomic hydrogen can penetrate deeply inside the material, reducing grain boundary cohesion and causing crack formation and growth. $^{5,6}$

Atomistic simulations can provide insights into physical mechanisms of the hydrogen effect. However, such simulations rely on the availability of accurate interatomic potentials for the system in question. Analysis of literature suggests that existing potentials for the Al-H system are not suitable for comprehensive studies of the hydrogen effect on mechanical properties of Al. The embedded-atom method (EAM) potential of Ruda et al. $^{7}$ predicts energetic preference of octahedral occupation by hydrogen, which is in disagreement with recent first-principles calculations showing that tetrahedral occupation is preferred. $^{8-11}$ Pedersen and Jónsson $^{12}$ developed an effective medium theory potential, which they used to study H diffusion in Al grain boundaries. This potential accurately reproduces first-principles solubility energies on the octahedral and tetrahedral positions and the hydrogen migration barrier. However, it was not tested for any other properties and the authors caution that it should be used with care as the fit was based on a small set of target values. Al-H potentials were also part of the ternary potential sets for the Al-Ni-H (Ref. 13) and Al-Mg-H (Ref. 14) systems. In both cases, the fit included 2-3 target numbers without testing other properties. We should also mention the recently developed ReaxFF potential (force field) for Al-H which is accurately fit to first-principles data. $^{15}$ This force field is focused on the $AlH_{3}$ hydride and the hydrogen desorption from it, with less attention to crystalline Al properties or their modification by dissolved hydrogen.

The goal of this paper is to propose a different interatomic potential for the Al-H system developed using an expanded fitting database and a large set of parameters. We employ the angular-dependent potential (ADP) format, $^{16-18}$ which is an extension of the traditional EAM method $^{19,20}$ to include angular-dependent interactions. The potential development methodology is described in Sec. II, followed by testing of properties of pure H and Al-H structures in Sec. III. Our conclusions are summarized in Sec. IV.

## II. CONSTRUCTION OF POTENTIALS

We used the well-established EAM potential for pure $Al,^{21}$ which was employed in a number of previous studies of mechanical behavior of this metal. An ADP potential for hydrogen was developed in this work and was crossed with Al to obtain a binary ADP Al-H potential. All Al properties were reported in detail $^{21}$ and will not be repeated here. The choice of the ADP format for pure hydrogen permits its easy crossing with other EAM or ADP metallic potentials in the future.

### A. ADP method

In the ADP method, $^{16-18}$ the total energy $E_{tot}$ of a collection of atoms is given by

$$
\begin{aligned}
E_{\mathrm{tot}}= & \frac{1}{2} \sum_{i, j(j \neq i)} \Phi_{s_{i} s_{j}}\left(r_{i j}\right)+\sum_{i} F_{s_{i}}\left(\bar{\rho}_{i}\right)+\frac{1}{2} \sum_{i, \alpha}\left(\mu_{i}^{\alpha}\right)^{2} \\
& +\frac{1}{2} \sum_{i, \alpha, \beta}\left(\lambda_{i}^{\alpha \beta}\right)^{2}-\frac{1}{6} \sum_{i} \nu_{i}^{2},
\end{aligned}\tag{1}
$$

where indices $i$ and $j$ enumerate atoms and the superscripts $\alpha, \beta=1,2,3$ refer to Cartesian components of vectors and tensors. The first term in Eq. (1) is the sum of pair interactions $\Phi_{s_{i} s_{j}}(r_{i j})$ between an atom $i$ of chemical sort $s_{i}$ located at position $\mathbf{r}_{i}$ and an atom $j$ of chemical sort $s_{j}$ at position $\mathbf{r}_{j}=\mathbf{r}_{i}+\mathbf{r}_{i j}$. The second term is the sum of embedding energies $F_{s_{i}}$ of atom $i$ in the host electron density $\bar{\rho}_{i}$ induced at site $i$ by all other atoms of the system. The host electron density is given by

1098-0121/2010/82(14)/144115(10)
144115-1
©2010 The American Physical Society

$$
\bar{\rho}_{i}=\sum_{j \neq i} \rho_{s_{j}}\left(r_{i j}\right),
\tag{2}
$$

where $\rho_{s_{j}}(r_{ij})$ is the electron density function assigned to an atom $j$. The first two terms in Eq. (1) constitute the regular EAM format$^{19,20}$ and have a central-force character. The last three terms in Eq. (1) introduce noncentral interactions through the dipole vectors

$$
\mu_{i}^{\alpha}=\sum_{j \neq i} u_{s_{i} s_{j}}\left(r_{i j}\right) r_{i j}^{\alpha}
\tag{3}
$$

and quadrupole tensors

$$
\lambda_{i}^{\alpha \beta}=\sum_{j \neq i} w_{s_{i} s_{j}}\left(r_{i j}\right) r_{i j}^{\alpha} r_{i j}^{\beta},
\tag{4}
$$

where $\nu_{i}$ is the trace

$$
\nu_{i}=\sum_{\alpha} \lambda_{i}^{\alpha \alpha}.
\tag{5}
$$

Equations (3) and (4) introduce two additional functions $u_{s_{i} s_{j}}(r)$ and $w_{s_{i} s_{j}}(r)$ representing angular-dependent forces. As in similar potential formats such as the modified EAM (Ref. 22) and embedded-defect method,$^{23}$ the role of the angular terms is to penalize the total energy for deviations of atomic environments from cubic symmetry. These terms vanish in a perfect cubic structure but can be important in noncen- trosymmetric crystal structures and near crystalline defects. They can affect elastic constants, defect formation energies, the melting point and many other properties.

An ADP description of an element requires five functions: for example, $\Phi_{HH}(r)$, $\rho_{H}(r)$, $F_{H}(\bar{\rho})$, $u_{HH}(r)$, and $w_{HH}(r)$ for pure hydrogen (compare with three functions in EAM). For the binary system Al-H, 13 potential functions are needed: $\Phi_{AlAl}(r)$, $\Phi_{AlH}(r)$, $\Phi_{HH}(r)$, $\rho_{Al}(r)$, $\rho_{H}(r)$, $F_{Al}(\bar{\rho})$, $F_{H}(\bar{\rho})$, $u_{AlAl}(r)$, $u_{AlH}(r)$, $u_{HH}(r)$, $w_{AlAl}(r)$, $w_{AlH}(r)$, and $w_{HH}(r)$ (compare with seven functions in EAM). The Al-H potential was constructed using the following steps: (1) convert the exist- ing EAM Al potential$^{21}$ into the ADP format using the exist- ing $\Phi_{AlAl}(r)$, $\rho_{Al}(r)$, and $F_{Al}(\bar{\rho})$ functions and formally adding fictitious functions $u_{AlAl}(r)$ and $w_{AlAl}(r)$ set to identical zero, (2) develop a new ADP potential for pure H by fitting to first-principles data, and (3) construct the cross-interaction functions $\Phi_{AlH}(r)$, $u_{AlH}(r)$, and $w_{AlH}(r)$ by fitting to experi- mental and first-principles data.

### B. ADP potential for H

For elemental hydrogen, the electron-density function was chosen in the form

![](./images/811712862224384001_1.jpg)

FIG. 1. ADP potential functions for hydrogen: (a) pair interaction function $\Phi_{HH}(r)$, (b) electron density function $\rho_{H}(r)$, (c) embedding energy function $F_{H}(r)$, and (d) dipole $d_{HH}(r)$ ($\sqrt{\text{eV}}/\mathring{\text{A}}$) and quadrupole $w_{HH}(r)$ ($\sqrt{\text{eV}}/\mathring{\text{A}}^{2}$) functions.

<table>
<caption>TABLE I. Optimized values of fitting parameters of the ADP hydrogen potential.</caption>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Value</th>
      <th>Parameter</th>
      <th>Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$r_{c}$ (Å)</td>
      <td>2.10399</td>
      <td>$\alpha_{2}$ (1/Å)</td>
      <td>2.15587</td>
    </tr>
    <tr>
      <td>$h$ (Å)</td>
      <td>$7.05516 × 10^{-1}$</td>
      <td>$C_{0}$</td>
      <td>$1.46318 × 10^{-2}$</td>
    </tr>
    <tr>
      <td>$V_{0}$ (eV)</td>
      <td>$4.23413 × 10^{-1}$</td>
      <td>$s_{1}$</td>
      <td>8.08612</td>
    </tr>
    <tr>
      <td>$\alpha$</td>
      <td>4.80494</td>
      <td>$s_{2}$</td>
      <td>$1.46294 × 10^{-2}$</td>
    </tr>
    <tr>
      <td>$\beta$ (1/Å)</td>
      <td>3.51586</td>
      <td>$s_{3}$</td>
      <td>$-6.86143 × 10^{-3}$</td>
    </tr>
    <tr>
      <td>$R_{0}$ (Å)</td>
      <td>7.25356</td>
      <td>$s_{4}$</td>
      <td>3.19616</td>
    </tr>
    <tr>
      <td>$A_{1}$ (eV)</td>
      <td>$2.18646 × 10^{-2}$</td>
      <td>$s_{5}$</td>
      <td>$1.17247 × 10^{-1}$</td>
    </tr>
    <tr>
      <td>$A_{2}$ (eV/Å)</td>
      <td>$2.06845 × 10^{-2}$</td>
      <td>$s_{6}$</td>
      <td>50</td>
    </tr>
    <tr>
      <td>$A_{3}$ (eV)</td>
      <td>$4.94849 × 10^{-2}$</td>
      <td>$s_{7}$</td>
      <td>1500000</td>
    </tr>
    <tr>
      <td>$\gamma$ (eV/Å²)</td>
      <td>3.03090</td>
      <td>$d_{1}$ (√eV/Å)</td>
      <td>$7.40338 × 10^{-1}$</td>
    </tr>
    <tr>
      <td>$R_{1}$ (Å)</td>
      <td>1.52662</td>
      <td>$d_{2}$ (1/Å)</td>
      <td>1.67135</td>
    </tr>
    <tr>
      <td>$A_{0}$ (1/Å^{z1})</td>
      <td>$3.18287 × 10^{-1}$</td>
      <td>$d_{3}$ (√eV/Å)</td>
      <td>$1.02980 × 10^{-3}$</td>
    </tr>
    <tr>
      <td>$z_{1}$</td>
      <td>$1.41565 × 10^{-1}$</td>
      <td>$q_{1}$ (√eV/Å²)</td>
      <td>1.57109</td>
    </tr>
    <tr>
      <td>$\alpha_{1}$ (1/Å)</td>
      <td>1.35765</td>
      <td>$q_{2}$ (1/Å)</td>
      <td>1.80580</td>
    </tr>
    <tr>
      <td>$B_{0}$ (1/Å^{z2})</td>
      <td>$1.07196 × 10^{-2}$</td>
      <td>$q_{3}$ (√eV/Å²)</td>
      <td>$-6.08109 × 10^{-3}$</td>
    </tr>
    <tr>
      <td>$z_{2}$</td>
      <td>$2.40281 × 10^{-2}$</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

$$
\rho(r)=\left(A_{0} r^{z_{1}} e^{-\alpha_{1} r}+B_{0} r^{z_{2}} e^{-\alpha_{2} r}+C_{0}\right) \psi\left(\frac{r-r_{c}}{h}\right). \qquad (6)
$$

Here $A_{0}$, $B_{0}$, $C_{0}$, $z_{1}$, $z_{2}$, $\alpha_{1}$, $\alpha_{2}$, $r_{c}$, and $h$ are fitting parameters and $\psi(x)$ is a cutoff function defined by

$$
\psi(x)=
\begin{cases}
x^{4}/(1+x^{4}) & \quad x < 0 \\
0 & \quad x \geq 0
\end{cases} \qquad (7)
$$

$r_{c}$ being the cut-off radius. The pair-interaction function was represented by

$$
\begin{aligned}
\Phi(r)= & \left\{V_{0}\left[e^{-\alpha \beta\left(r-R_{0}\right)}-\alpha e^{-\beta\left(r-R_{0}\right)}\right]+A_{1}+A_{2}\left(r-R_{0}\right)\right. \\
& \left.+A_{3} e^{-\gamma\left(r-R_{1}\right)^{2}}\right\} \psi\left(\frac{r-r_{c}}{h}\right),
\end{aligned} \qquad (8)
$$

where $V_{0}$, $\alpha$, $\beta$, $\gamma$, $R_{0}$, $R_{1}$, $A_{1}$, $A_{2}$, and $A_{3}$ are fitting parameters. The embedding energy function was expressed by

$$
F(\bar{\rho})=\left(s_{1} \bar{\rho}+s_{2} \bar{\rho}^{2}+s_{3} \bar{\rho}^{3}-s_{4} \bar{\rho}^{s 5}\right) \omega(\bar{\rho}), \qquad (9)
$$

where

$$
\omega(\bar{\rho})=1-\frac{1-s_{6} \bar{\rho}^{2}}{1+s_{7} \bar{\rho}^{4}} \qquad (10)
$$

with $s_{i}$ ($i$=1–7) as fitting parameters. Function $\omega(\bar{\rho})$ serves to slightly modify the shape of the embedding energy function at small electron densities. Finally, the dipole and quadrupole functions were parameterized in the form

<table>
<caption>TABLE II. Optimized values of fitting parameters of the ADP Al-H potential. $s_{\text{H}}$, $g_{\text{Al}}$, and $g_{\text{H}}$ are invariant transformation parameters of the elements (Ref. <span class="citation" data-cites="27">27</span>).</caption>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Value</th>
      <th>Parameter</th>
      <th>Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$r_{c}$ (Å)</td>
      <td>3.37008</td>
      <td>$d_{2}$ (1/Å)</td>
      <td>$1.23325 × 10^{-1}$</td>
    </tr>
    <tr>
      <td>$h$ (Å)</td>
      <td>$6.30476 × 10^{-1}$</td>
      <td>$d_{3}$ (√eV/Å)</td>
      <td>$-1.09582 × 10^{-2}$</td>
    </tr>
    <tr>
      <td>$W_{0}$ (eV)</td>
      <td>$-1.08601 × 10^{-1}$</td>
      <td>$q_{1}$ (√eV/Å²)</td>
      <td>$-4.60988 × 10^{-2}$</td>
    </tr>
    <tr>
      <td>$r_{1}$ (Å)</td>
      <td>1.67001</td>
      <td>$q_{2}$ (1/Å)</td>
      <td>$1.08789 × 10^{-1}$</td>
    </tr>
    <tr>
      <td>$b_{1}$</td>
      <td>8.16186</td>
      <td>$q_{3}$ (√eV/Å²)</td>
      <td>$4.54746 × 10^{-2}$</td>
    </tr>
    <tr>
      <td>$b_{2}$</td>
      <td>8.34403</td>
      <td>$s_{\text{H}}$</td>
      <td>$4.00846 × 10^{-1}$</td>
    </tr>
    <tr>
      <td>$\delta$ (eV)</td>
      <td>$5.51726 × 10^{-2}$</td>
      <td>$g_{\text{Al}}$ (eV)</td>
      <td>$-6.42956 × 10^{-2}$</td>
    </tr>
    <tr>
      <td>$d_{1}$ (√eV/Å)</td>
      <td>$1.01564 × 10^{-1}$</td>
      <td>$g_{\text{H}}$ (eV)</td>
      <td>$-7.97198 × 10^{-1}$</td>
    </tr>
  </tbody>
</table>

$$
u(r)=\left(d_{1} e^{-d_{2}}+d_{3}\right) \psi\left(\frac{r-r_{c}}{h}\right), \qquad (11)
$$

$$
w(r)=\left(q_{1} e^{-q_{2}}+q_{3}\right) \psi\left(\frac{r-r_{c}}{h}\right) \qquad (12)
$$

with fitting parameters $d_{i}$ and $q_{i}$ ($i$=1,2,3). The parameterization of the potential functions includes the total of 31 fitting parameters.

The fitting database included the well-known values of the bond length and bond energy of the $\text{H}_{2}$ molecule (dimer),${}^{24}$ and equilibrium cohesive energies of hypothetical crystal structures of atomic hydrogen: simple cubic (SC), bcc, fcc, and hcp. The energies of these crystal structures were calculated from first-principles by Min <i>et al.</i>${}^{25}$ and later improved by Nobel <i>et al.</i>${}^{26}$ In addition, our fitting procedure imposed the constraint that $\text{H}_{2}$ be more stable than the trimer $\text{H}_{3}$ and all larger hydrogen molecules and clusters.

The fitting parameters were optimized by minimizing the weighted mean-squared deviation, $W$, of properties from their target values using a simple genetic algorithm. Starting from an initial guess, 400 potentials (species) were generated by adding random numbers to the parameters. Using $1/W$ as the fitness criterion, half of the population with the lowest fitness was eliminated whereas the remaining half was allowed to multiply. Parents were selected at random and their children were defined by averaging each parameter between the parents. The averaging was performed with weights proportional to the fitness values of the parents so that the fitter parent had a greater influence on the child. Each child was then subject to a mutation by adding some noise to its parameters. After producing a new generation of 400 children, the parents were allowed to die and the children were again subject to selection (top 50%) and reproduction. After 50–100 generations, the algorithm produced a set of nearly identical and well-optimized potentials. The process was repeated multiple times by adjusting weights assigned to individual properties until a satisfactory potential was obtained. Table I presents optimized values of the fitting parameters and Fig. 1 shows the optimized functions of the final version of the potential.


### C. Binary ADP potential for Al-H

The cross-interaction function $\Phi_{\mathrm{AlH}}(r)$ was postulated in the form of a truncated generalized Lennard-Jones function
$$
\Phi_{\mathrm{AlH}}(r)=\left[\frac{W_{0}}{b_{2}-b_{1}}\left(\frac{b_{2}}{z^{b_{1}}}-\frac{b_{1}}{z^{b_{2}}}\right)+\delta\right] \psi\left(\frac{r-r_{c}}{h}\right), \quad(13)
$$
where $z=r / r_{1}$. This function has 7 fitting parameters: $W_{0}, r_{1}$, $b_{1}$, $b_{2}$, $\delta$, $r_{c}$, and $h$. The cross-dipole $u_{\mathrm{AlH}}(r)$ and crossquadrupole $w_{\mathrm{AlH}}(r)$ functions were parameterized by Eqs. (11) and (12). In addition, a set of invariant transformations was applied to the potential functions. $^{27}$ Such transformations do not affect the total energy or any physical properties of pure Al or H but modify the shapes of the potential functions, providing three additional parameters for fitting. Thus, the parameterization of the crossfunctions involved the total of 16 parameters.

The fitting database included the experimental values of the equilibrium lattice parameters $a$ and $c$ of the $\mathrm{AlH}_{3}$ hydride (alane) reported by Turley and Rinn $^{28}$ and equilibrium formation energies of the hypothetical hydrides $\mathrm{AlH}_{2}$ (fluorite), $\mathrm{AlH}$ (zinc blende), and $\mathrm{AlH}$ (rock salt) computed from first-principles by Wolverton $e t$ al. $^{8}$ The database also included the $a b$ initio values of the dilute heats of solution of $\mathrm{H}$ at tetrahedral $\left(T_{d}\right)$, octahedral $\left(O_{h}\right)$ and substitutional sites in $\mathrm{Al}$ and the formation energies of H-vacancy pairs with the hydrogen atom at the nearest $T_{d}$ or $O_{h}$ site to the vacancy (Tables V and VI). $^{8}$

The cross-functions were optimized by minimizing the weighted mean-squared deviation of selected properties of the Al-H system from their target values using the simulated annealing method. $^{29}$ The largest weight was assigned to the dilute heats of solution of $\mathrm{H}$ in $\mathrm{Al}$, followed by the formation energies of H-vacancy pairs and the aluminum hydrides. The lattice parameters of alane were included with the lowest weight. The cross-angular terms, which turned out to be quite small, were used for fine tuning the energetics of $\mathrm{H}$ as an impurity in $\mathrm{Al}$; they leave the formation energies of the hydrides almost unchanged. The optimized values of fitting parameters are summarized in Table II and the optimized potential functions are plotted in Fig. 2. The tabulated forms of the potential functions for pure hydrogen and for the binary Al-H system can be downloaded from the NIST Interatomic Potentials Repository at http://www.ctcms.nist.gov/potentials.

<table>
<caption>TABLE III. First-neighbor distances, $R_{0}$, and cohesive energies, $E_{0}$, of selected structures of hydrogen calculated with the ADP potential in comparison with first-principles data.</caption>
<thead>
  <tr>
    <th rowspan="2">Structure</th>
    <th colspan="2">$R_{0}$ (Å)</th>
    <th colspan="2">$E_{0}$ (eV/atom)</th>
  </tr>
  <tr>
    <th>Ab initio</th>
    <th>ADP</th>
    <th>Ab initio</th>
    <th>ADP</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Dimer ($\mathrm{H}_{2}$)</td>
    <td>0.741ª</td>
    <td>0.742</td>
    <td>−2.373ª</td>
    <td>−2.373</td>
  </tr>
  <tr>
    <td>Trimer ($\mathrm{H}_{3}$)</td>
    <td></td>
    <td>0.749</td>
    <td></td>
    <td>−2.332</td>
  </tr>
  <tr>
    <td>$\mathrm{H}_{4}$</td>
    <td></td>
    <td>0.747</td>
    <td></td>
    <td>−2.013</td>
  </tr>
  <tr>
    <td>SC</td>
    <td>1.456ᵇ</td>
    <td>1.600</td>
    <td>−1.194ᵇ</td>
    <td>−1.876</td>
  </tr>
  <tr>
    <td>bcc</td>
    <td>1.561ᵇ</td>
    <td>1.643</td>
    <td>−1.064ᵇ</td>
    <td>−1.867</td>
  </tr>
  <tr>
    <td>fcc</td>
    <td>1.611ᵇ</td>
    <td>1.686</td>
    <td>−1.073ᵇ</td>
    <td>−1.861</td>
  </tr>
  <tr>
    <td>hcp</td>
    <td>1.609ᵇ</td>
    <td>1.686</td>
    <td>−1.079ᵇ</td>
    <td>−1.861</td>
  </tr>
  <tr>
    <td>Diamond</td>
    <td></td>
    <td>1.535</td>
    <td></td>
    <td>−1.889</td>
  </tr>
</tbody>
<tfoot>
  <tr>
    <td colspan="5">ªReference 24.</td>
  </tr>
  <tr>
    <td colspan="5">ᵇReferences 25 and 26.</td>
  </tr>
</tfoot>
</table>

### III. TESTING OF NEW POTENTIALS

#### A. ADP results for hydrogen

Table III shows that the new potential accurately reproduces the first-principles cohesive energy $E_{0}$ and interatomic spacing $R_{0}$ of the $\mathrm{H}_{2}$ molecule. $^{24}$ The cohesive energy is energy per atom and thus half of the binding energy between the atoms in the $\mathrm{H}_{2}$ molecule at 0 K temperature. This energy does not include the energy of zero-point vibrations, which constitutes almost $6 \%$ of the binding energy. $^{24}$

Our goal was not only to reproduce the properties of $\mathrm{H}_{2}$ but also secure its higher stability over other $\mathrm{H}_{n}$ molecules that are not found in nature. Our potential correctly predicts that all imaginary molecules $\mathrm{H}_{3}, \mathrm{H}_{4}, \ldots$ have a higher energy per atom that $\mathrm{H}_{2}$. As a more direct test of stability of $\mathrm{H}_{2}$ molecules, molecular dynamics (MD) simulations were performed in which a hydrogen gas was initially composed of

![](./images/811712862224384001_2.jpg)

FIG. 2. ADP potential functions for the Al-H system: (a) pair interaction functions $\Phi_{\mathrm{AlAl}}(r)$, $\Phi_{\mathrm{AlH}}(r)$, and $\Phi_{\mathrm{HH}}(r)$, (b) cross-dipole $u_{\mathrm{AlH}} r$ ($\sqrt{\mathrm{eV}} / \mathring{\mathrm{A}}$) and cross-quadrupole $w_{\mathrm{AlH}}(r)$ ($\sqrt{\mathrm{eV}} / \mathring{\mathrm{A}}^{2}$) functions.

<table>
<caption>TABLE IV. Formation energies, $\Delta E$, of selected aluminum hydrides calculated with the ADP potential in comparison with first-principles data when available. The energies marked by an asterisk were included in the potential fit.</caption>
<thead>
  <tr>
    <th rowspan="2">Formula</th>
    <th rowspan="2">Prototype</th>
    <th rowspan="2">Structure</th>
    <th colspan="2">$\Delta E$ (eV/atom)</th>
  </tr>
  <tr>
    <th>Ab initioa</th>
    <th>ADP</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>AlH₃</td>
    <td>AlH₃($\alpha$)</td>
    <td>$R\overline{3}c$</td>
    <td>−0.039ᵃ; −0.051ᵇ</td>
    <td>0.375</td>
  </tr>
  <tr>
    <td>AlH₃</td>
    <td>ReO₃</td>
    <td>D0₉</td>
    <td></td>
    <td>0.331</td>
  </tr>
  <tr>
    <td>AlH₂</td>
    <td>TiO₂ (rutile)</td>
    <td>C4</td>
    <td>0.28ᵃ</td>
    <td>0.382</td>
  </tr>
  <tr>
    <td>AlH₂</td>
    <td>CaF₂ (fluorite)</td>
    <td>C1</td>
    <td>0.31ᵃ</td>
    <td>0.393*</td>
  </tr>
  <tr>
    <td>AlH</td>
    <td>ZnS (zinc blende)</td>
    <td>B3</td>
    <td>0.38ᵃ</td>
    <td>0.310*</td>
  </tr>
  <tr>
    <td>AlH</td>
    <td>NaCl (rock salt)</td>
    <td>B1</td>
    <td>0.40ᵃ</td>
    <td>0.392*</td>
  </tr>
  <tr>
    <td>AlH</td>
    <td>CsCl</td>
    <td>B2</td>
    <td></td>
    <td>0.694</td>
  </tr>
  <tr>
    <td>AlH</td>
    <td>CuAu</td>
    <td>L1₀</td>
    <td></td>
    <td>0.838</td>
  </tr>
  <tr>
    <td>Al₂H</td>
    <td>Ag₂O (cuprite)</td>
    <td>C₃</td>
    <td></td>
    <td>0.215</td>
  </tr>
  <tr>
    <td>Al₃H</td>
    <td>Cu₃Au</td>
    <td>L1₂</td>
    <td></td>
    <td>0.545</td>
  </tr>
</tbody>
<tfoot>
  <tr>
    <td colspan="5">ᵃReference 8.</td>
  </tr>
  <tr>
    <td colspan="5">ᵇReference 15.</td>
  </tr>
</tfoot>
</table>

either single atoms or Hₙ molecules with $n>2$. Such tests were conducted at several different temperatures using the NVT or NPT ensembles. They have shown that the gas always undergoes atomic rearrangements resulting in H₂ molecules.

MD calculations of the pressure-density relation for hydrogen at room temperature revealed a continuous liquid-gas transition, indicating that the critical point of separation is below room temperature. The experimental critical point of H₂ is 32 K. Calculations of the phase diagram of hydrogen with this potential are in progress and will be reported in a separate publication.

The potential overestimates the cohesive energies of imaginary crystalline structures of atomic H in comparison with first-principles calculations,²⁵,²⁶ predicting values ranging from −1.89 to −1.86 eV/atom (Table III). A better agreement is obtained for the first-neighbor distances $R_0$ in these structures. For the fcc structure, the EAM potential of Ruda et al.⁷ gives $E_0$=−1.803 eV/atom, which is close to our value, but their $R_0$=1.874 Å is less accurate. Authors of other potentials available in the literature did not test crystalline structures of hydrogen. Experimentally, hydrogen is known to form an H₂ molecular crystal with a hexagonal structure. Crystals of atomic hydrogen are found only at high pressures.

### B. ADP results for Al-H system

Table IV summarizes the formation energies, $\Delta E$, of several hypothetical aluminum hydrides calculated with the ADP potential and from first principles.⁸ $\Delta E$ of a compound AlₙHₘ is defined relative to pure fcc Al and an isolated H₂ molecule as follows:

$$
\Delta E(\mathrm{Al}_{n} \mathrm{H}_{m})=\frac{1}{n+m}\left[E(\mathrm{Al}_{n} \mathrm{H}_{m})-n E_{\mathrm{fcc}}(\mathrm{Al})-\frac{m}{2} E(\mathrm{H}_{2})\right].
\tag{14}
$$

The AlH₂ (fluorite), AlH (zinc blende), and Al₂H (cuprite) structures can be viewed as fcc Al lattice with tetrahedral interstitial sites fully or partially occupied by H atoms. By contrast, AlH (rocksalt) has the fcc Al structure with all octahedral sites occupied by H atoms.

As evident from Table IV, all hydrides but one are unstable with respect to decomposition into pure Al and hydrogen ($\Delta E>0$). This is in agreement with the experimental fact that aluminum has no stable hydrides at low pressures.³⁰ The formation energies of the unstable hydrides calculated with our potential are in reasonable agreement with first-principles data.⁸ But the Al-H system has metastable hydrides ($\Delta E<0$), the best known and most stable of them being $\alpha$-AlH₃ (alane) with trigonal symmetry.²⁸ Our potential fails to predict the negative formation energy of this hydride. Sinke et al.³¹ measured the formation enthalpy of AlH₃ at room temperature by calorimetry and found a small but negative value of −0.030 eV/atom. Wolverton et al.⁸ also found a small and negative formation energy of −0.039 eV/atom by first-principles calculations at 0 K. At room temperature, however, AlH₃ has a positive formation free energy according to both experimental data (+0.129 eV/atom) (Ref. 31) and first-principles calculations (+0.120 eV/atom).⁸

The trigonal structure of $\alpha$-AlH₃ (space group $R\overline{3}c$) contains six molecules in a hexagonal unit cell with the lattice parameters $a$=4.449 Å and $c$=11.804 Å and the cell-internal position for H atoms $x_c$=0.628.²⁸ During the tests of this structure with the ADP potential, we found $a$=4.246 Å, $c$=11.368 Å, and a positive formation energy $\Delta E$=0.375 eV/atom when only the cell shape and volume were optimized keeping $x_c$ constant at the experimental value. However, when also atomic positions were allowed to vary, the trigonal structure transformed into a ReO₃-type cubic structure (primitive cubic unit cell with Al atoms in the corners and H atoms at centers of the cube edges) with $a$=3.189 Å and $\Delta E$=0.331 eV/atom. Thus, the potential predicts the trigonal structure of AlH₃ to be mechanically unstable.

MD simulations were performed to test thermal stability of the hydrides. All of them were observed to decompose into Al and H₂ at elevated temperatures. In particular, ReO₃-AlH₃ decomposes above 300 K. To our knowledge, other EAM-type Al-H potentials reported in literature did not examine the stability of Al-H compounds at zero or elevated temperatures.

Table V reports fully relaxed solution energies of isolated hydrogen atoms at different positions in Al. The solution energy $\Delta E_s$ is defined by

$$
\Delta E_{s}=E(\mathrm{Al}_{n} \mathrm{H}_{1})-\left[n E_{\mathrm{fcc}}(\mathrm{Al})+\frac{1}{2} E(\mathrm{H}_{2})\right],
\tag{15}
$$

where $n$ is the number of Al atoms in the cell. The calculations were performed for a set of $n$ values followed by ex-

<table>
<caption>TABLE V. Energies (in eV) of isolated H atoms in Al predicted by the ADP potential in comparison with experimental and first-principles data. $\Delta E_s$ is the dilute heat of solution at interstitial sites defined by Eq. (15), $\Delta E_s(T_d$-$O_h)$ is the energy difference between $\Delta E_s$ values for the tetrahedral and octahedral sites, $\Delta E_s$ (sub) is the dilute heat of solution of H on substitutional sites, and $E_m$ is the migration energy of an H atom from a tetrahedral to a nearest-neighbor octahedral site. The energies marked by an asterisk were included in the potential fit.</caption>
<tbody>
<tr>
<td>
</td>
<td>
$\Delta E_s(T_d)$
</td>
<td>
$\Delta E_s(O_h)$
</td>
<td>
$\Delta E_s(T_d$-$O_h)$
</td>
<td>
$\Delta E_s$ (sub)
</td>
<td>
$E_m$
</td>
</tr>
<tr>
<td>
Experiment
</td>
<td>
0.67a; 0.71b; 0.65c; 0.66d
</td>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
$0.17\pm0.02$e
</td>
</tr>
<tr>
<td>
Ab initio
</td>
<td>
0.69f; 0.74g
</td>
<td>
0.82f
</td>
<td>
$-0.13$f
</td>
<td>
1.76f
</td>
<td>
0.18f
</td>
</tr>
<tr>
<td>
ADP
</td>
<td>
0.693*
</td>
<td>
0.824*
</td>
<td>
$-0.131$
</td>
<td>
2.00*
</td>
<td>
0.189
</td>
</tr>
<tr>
<td colspan="6">
aReference 32.
</td>
</tr>
<tr>
<td colspan="6">
bReference 33.
</td>
</tr>
<tr>
<td colspan="6">
cReference 34.
</td>
</tr>
<tr>
<td colspan="6">
dReference 35.
</td>
</tr>
<tr>
<td colspan="6">
eReference 36.
</td>
</tr>
<tr>
<td colspan="6">
fReference 8.
</td>
</tr>
<tr>
<td colspan="6">
gReference 11.
</td>
</tr>
</tbody>
</table>

trapolation to $1/n\rightarrow0.^{37}$ For comparison, Table V contains first-principles energies computed for $n$=32 without zero-point vibrations.⁸ The agreement between the two calculation methods is excellent. In particular, the potential correctly predicts that H prefers the tetrahedral site over octahedral. It should be noted that these energies were included in the potential fit.

To evaluate the interaction between H atoms embedded in Al, we computed the formation energy, $\Delta E^{\text{H}}$, of different $\text{Al}_n\text{H}_m$ compounds per H atom

$$
\begin{aligned}
\Delta E^{\mathrm{H}}(\mathrm{Al}_{n} \mathrm{H}_{m})=\frac{1}{m}\bigg[E(\mathrm{Al}_{n} \mathrm{H}_{m})-n E_{\mathrm{fcc}}(\mathrm{Al})-\frac{m}{2}E(\mathrm{H}_{2})\bigg].
\\[-20pt]
\tag{16}
\end{aligned}
$$

If two H atoms occupy third-nearest-neighbor tetrahedral positions in each cubic unit cell of Al, the structure obtained is the stoichiometric compound $\text{Al}_2\text{H}$ (cuprite). For this compound, the ADP potential gives the energy per hydrogen atom $\Delta E^{\text{H}}$=0.645 eV, which is close to $\Delta E_s(T_d)$=0.693 eV (Table V). Thus, the potential predicts only week attractive interactions of H atoms located at third-nearest-neighbor tetrahedral sites. The calculated $\Delta E^{\text{H}}$ values of 0.620 eV and 0.589 eV for AlH (zinc blende), and $\text{AlH}_2$ (fluorite), respectively, indicate that interactions between H atoms do not increase significantly even if four or all eight $T_h$ sites are filled with hydrogen. $\Delta E^{\text{H}}$ of AlH (rocksalt), in which all $O_h$ sites are filled with hydrogen atoms, is 0.784 eV, which is comparable to $\Delta E_s(O_h)$=0.824 eV (Table V). Thus, hydrogen atoms display week attractive interactions also when they are located at $O_h$ sites. That H atoms interact weekly inside Al was first noted by Wolverton <i>et al.</i>⁸ based on first-principles calculations.

Table VI summarizes the hydrogen-vacancy interaction energies predicted by the ADP potential in comparison with experimental and first-principles data. The formation energy of a hydrogen-vacancy pair, $\Delta E_f$, is defined by the equation

$$
\begin{aligned}
\Delta E_{f}=E(\mathrm{Al}_{n-1} \mathrm{H}_{1}+V)-\bigg[(n-1)E_{\mathrm{fcc}}(\mathrm{Al})+\frac{1}{2}E(\mathrm{H}_{2})\bigg].
\\[-20pt]
\tag{17}
\end{aligned}
$$

This energy was computed for several $n$ values and extrapolated linearly to $1/n\rightarrow0$. The results were compared with first-principles calculations for $n$=32 without zero-point vibrations.⁸ The potential overestimates $\Delta E_f$ for both tetrahedral and octahedral sites but reflects the correct ordering with $\Delta E_f(T_d)<\Delta E_f(O_h)$ (Table VI).

<table>
<caption>TABLE VI. Energetics of H-vacancy interactions in Al predicted by the ADP potential in comparison with experimental and first-principles data. All energies are in eV. $\Delta E_f$ and $\Delta E_b$ are the formation and binding energies of H-vacancy pairs. The energies marked by an asterisk were included in the fitting database.</caption>
<tbody>
<tr>
<td>
</td>
<td>
$\Delta E_f(T_d$-$V)$
</td>
<td>
$\Delta E_f(O_h$-$V)$
</td>
<td>
$\Delta E_b(T_d$-$V)$
</td>
<td>
$\Delta E_b(O_h$-$V)$
</td>
</tr>
<tr>
<td>
Experiment
</td>
<td colspan="2">
</td>
<td colspan="2">
$0.53\pm0.03$a; $0.43\pm0.07$b; $0.52\pm0.10$c
</td>
</tr>
<tr>
<td>
Ab initio
</td>
<td>
0.90d; 1.00e
</td>
<td>
1.14d
</td>
<td>
0.33d; 0.34e
</td>
<td>
</td>
</tr>
<tr>
<td>
ADP
</td>
<td>
1.320*
</td>
<td>
1.363*
</td>
<td>
0.048
</td>
<td>
0.136
</td>
</tr>
<tr>
<td colspan="5">
aReference 38.
</td>
</tr>
<tr>
<td colspan="5">
bReference 39.
</td>
</tr>
<tr>
<td colspan="5">
cReference 40.
</td>
</tr>
<tr>
<td colspan="5">
dReference 8.
</td>
</tr>
<tr>
<td colspan="5">
eReference 11.
</td>
</tr>
</tbody>
</table>

![](./images/811712862224384001_3.jpg)

FIG. 3. Minimum-energy path for a jump of a hydrogen atom from a tetrahedral to a nearest octahedral position in Al. The result was obtained by the nudged elastic band method. The energy along a relaxed elastic band is plotted versus the sum of Euclidean lengths of the elastic band segments. The saddle point (maximum of energy) gives the migration energy of H in Al.

The binding energy, $\Delta E_b$, between a hydrogen atom and a vacancy is defined by

$$
\Delta E_b = -\Delta E_f + \Delta E_s + \Delta E_v, \tag{18}
$$

where $\Delta E_v$=0.675 eV is the vacancy formation energy in pure Al.²¹ A positive binding energy indicates attractive interaction, consistent with the convention in the literature. Because the potential overestimates $\Delta E_f$, the binding energies obtained are too small in comparison with both first-principles calculations and experiment (Table VI).

Tanguy and Magnin's EAM potential¹⁴ for the Al-Mg-H system was specifically designed to reproduce the hydrogen trapping by vacancies suggested by experiment³⁶ and first-principles calculations.⁸⁻¹⁰,⁴¹ Accordingly, it gives an accurate H-V binding energy of 0.55 eV. However, their potential predicts a significant relaxation of the hydrogen atom to an intermediate position between a $T_d$ site and a neighboring vacant site. The authors¹⁴ note that this strong relaxation is consistent with previous effective medium theory calculations.⁴²,⁴³ Our potential predicts only a small displacement of the hydrogen atom of about 0.17 Å, which is in good agreement with the first-principles value of 0.15 Å.⁸ In addition, Tanguy and Magnin's potential¹⁴ overestimates the migration energy of H in Al to 0.40 eV (see discussion below). The difference between the hydrogen solution energies on the tetrahedral and octahedral sites was not reported in Ref. 14.

The hydrogen migration barrier $E_m$ from a tetrahedral site to a neighboring octahedral site was computed by the nudged elastic band method.⁴⁴ The minimum energy path (the energy along the relaxed elastic band) with 15 movable images of the simulation block is plotted in Fig. 3. The ADP potential gives $E_m$=0.189 eV in excellent agreement with the first-principles prediction of 0.18 eV.⁸ The position of the hydrogen atom in the saddle point configuration is halfway between tetrahedral and octahedral sites, which is also in agreement with first-principles calculations.⁸

<table>
<caption>TABLE VII. Adsorption energies, $\Delta E_{ads}$, of isolated hydrogen atoms on high symmetry sites of Al(111) surface computed with the ADP potential in comparison with first-principles and REAXFF calculations.</caption>
<thead>
  <tr>
    <th rowspan="2">Site</th>
    <th colspan="3">$\Delta E_{ads}$ (eV/atom)</th>
  </tr>
  <tr>
    <th>Ab initioᵃ</th>
    <th>REAXFFᵃ</th>
    <th>ADP</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>hcp</td>
    <td>−1.943</td>
    <td>−2.073</td>
    <td>−2.039</td>
  </tr>
  <tr>
    <td>fcc</td>
    <td>−2.065</td>
    <td>−2.135</td>
    <td>−2.035</td>
  </tr>
  <tr>
    <td>Top</td>
    <td>−1.989</td>
    <td>−2.044</td>
    <td>−2.086</td>
  </tr>
  <tr>
    <td>Bridge</td>
    <td>−2.054</td>
    <td>−2.122</td>
    <td>Unstable</td>
  </tr>
</tbody>
<tfoot>
  <tr>
    <td colspan="4">ᵃReference 15.</td>
  </tr>
</tfoot>
</table>

It should be mentioned that early experimental measurements²,³⁹,⁴⁵,⁴⁶ indicated a range of migration energies between 0.4 and 0.6 eV. Accordingly, previous potentials used large target values such as 0.47 (Ref. 13) or 0.42 eV,¹⁴ leading to similarly high $E_m$ values calculated with the potentials. In a more recent experimental study, Young and Scully³⁶ obtained $E_m$=0.17 eV and suggested that vacancy trapping of hydrogen atoms was at least partially responsible for the previously overestimated migration energies. This experimental result has been confirmed by recent first-principles calculations.⁸

The energy of solution of hydrogen on substitutional sites (Table V) is high both with the ADP potential and by first-principles calculations.⁸ Thus, a hydrogen atom prefers to occupy an interstitial site next to a vacancy and is very unlikely to fill the vacancy.

Table VII reports fully relaxed adsorption energies, $\Delta E_{ads}$, of isolated H atoms on high symmetry sites on Al(111) surface. $\Delta E_{ads}$ is defined by

$$
\Delta E_{ads}=E(\text{Slab}+H)-E(\text{Slab})-E(H), \tag{19}
$$

where $E(\text{Slab}+H)$ is the energy of an Al slab with one H atom adsorbed on its surface, $E(\text{Slab})$ is the energy of the slab without hydrogen, and $E(H)$ is the energy of an isolated hydrogen atom (zero in the EAM and ADP methods). The adsorption energies calculated with the ADP potential are in reasonable agreement with first-principles results and REAXFF calculations.¹⁵ The only significant discrepancy is the mechanical instability of the bridge site: a hydrogen atom placed on this site moves to a nearest HCP site during the relaxation.

Finally, it should be mentioned that the potential gives highly inaccurate results for the diatomic molecule AlH and the alane molecule $\text{AlH}_3$. It should not be used for simulations involving these or similar molecules, which can be accurately modeled by other methods such as REAXFF.¹⁵

### C. Testing the hydrogen solubility in Al

Hydrogen solubility in solid Al is very small, approximately $10^{-4}$ at. % near the melting temperature.³⁰,⁴⁷ We applied MD simulations to directly verify that our ADP potential reproduces this low solubility. The simulation block with

![](./images/811712862224384001_4.jpg)

FIG. 4. (Color online) MD simulation of hydrogen desorption from Al at the temperature of 700 K. The bright (yellow in online version) and dark (blue in online version) spheres represent Al and H atoms, respectively. (a) Initial state: atomic hydrogen is randomly distributed inside Al. (b) Intermediate state: over 30% of the atomic hydrogen has evaporated and formed $H_2$ molecules. (c) Final state: all hydrogen has evaporated and formed $H_2$ gas.

dimensions $82 \times 65 \times 65$ $\text{\AA}^3$ contained about 20 500 Al atoms and initially had periodic boundary conditions in all three $\langle 100 \rangle$ directions. About 3 at. % of hydrogen atoms were introduced into random tetrahedral positions and the system was equilibrated by an NPT (zero pressure) MD run at the temperature of 700 K. The hydrogen atoms were found to diffuse through the crystal but continued to occupy $T_d$ sites. (The predominant occupation of $T_d$ sites was also confirmed in similar simulations with up to 20 at. % H.)

Two free surfaces were then created by increasing the block dimension in one of the $\langle 100 \rangle$ directions to produce a 100 $\text{\AA}$ wide gap of vacuum (Fig. 4). This effectively created in a 65-$\text{\AA}$-thick free-standing Al film containing atomic hydrogen. A new MD run was performed at 700 K for 2 ns using the NVT ensemble (fixed volume). Figure 4 illustrates the initial, intermediate and final stages of the simulation. The hydrogen atoms diffuse toward the surfaces through the Al film and evaporate, creating an expanding hydrogendepleted zone under the surfaces. After less than 1 ns, all H atoms escape from the Al film and form a diatomic gas. This test estimates the upper bound of the H solubility in solid Al as approximately $5 \times 10^{-3}$ at. %, which is consistent with experiment. Importantly, as the hydrogen atoms leave the Al film, they recombine to form $H_2$ molecules. This provides an additional confirmation that the ADP potential correctly reproduces the stability of diatomic molecules in the gaseous state. Some amount of atomic hydrogen remains in an adsorbed layer on the Al surface.

A similar test was performed on a liquid Al film at 1200 K, again showing hydrogen evaporation with the formation of $H_2$ molecules. For the same number of Al atoms, several hydrogen atoms remained inside the film in the equilibrium state. Although this test does not provide enough statistics for a quantitative estimate of the solubility, it probably suggests a larger solubility of hydrogen in liquid Al than in solid Al, which is consistent with the phase diagram. $^{30}$ We are not aware of any previous MD simulations of hydrogen solubility in Al.

In yet another MD simulation, a large periodic block of liquid Al was supersaturated with atomic hydrogen. In the course of a subsequent NPT MD run at 1200 K, the liquid formed several bubbles filled with $H_2$ molecules that grew by diffusion of hydrogen atoms toward them. Eventually, almost all hydrogen was collected into the bubbles, which continued to coarsen by a diffusion-controlled process similar to Ostwald ripening. In the end of the simulation, the block contained only one bubble filled with $H_2$, which continued to expand driven by hydrogen pressure from inside. These observations point to a possible suitability of our potential for simulations of hydrogen bubble formation in liquid Al, a process which is relevant to the problem of void formation during the casting of commercial Al alloys.

## IV. DISCUSSION AND CONCLUSIONS

We will now summarize some distinct features of the Al-H potential developed in this work in comparison with other existing potentials and force fields. As any potential, it has an intended area of applications. Specifically, it is designed for simulations of deformation and fracture of Al in the presence of dissolved hydrogen atoms. Accordingly, it is based on an existing EAM Al potential $^{21}$ which was successfully applied in a number of previous atomistic studies of dislocations, fracture cracks, and other defects involved in mechanical behavior of Al. This potential predicts a number of properties of Al in good agreement with experiment and first-principles data, including elastic constants, phonon frequencies, generalized stacking faults, surface energies, diffusion coefficients, etc.

ANGULAR-DEPENDENT INTERATOMIC POTENTIAL FOR...
PHYSICAL REVIEW B 82, 144115 (2010)

In parametrizing Al-H interactions, the emphasis was placed on reproducing the accurate solution energies of hydrogen atoms in Al, the energetic preference of the tetrahedral site occupation over octahedral, and the migration barrier for hydrogen diffusion in Al. These properties are reproduced by our potential in excellent agreement with experiment and first-principles calculations. The potential also gives reasonable results for the hydrogen solubility in the solid and liquid phases of Al and for the formation energies of several unstable hydrides. The instability of such hydrides has been directly verified by MD simulations. However, the potential underestimates hydrogen-vacancy interactions and fails to reproduce the negative formation energy of the metastable crystalline hydride $AlH_3$. This failure apparently reflects the general inability of EAM-like models, such as ADP, to capture the covalent and ionic components of the bonding in $AlH_3$. To our knowledge, other EAM-type potentials were not successful in reproducing the metastability of this hydride either. Thus, simulations of the formation of $AlH_3$ or hydrogen desorption from it are beyond the applicability range of this potential. The REAXFF force field $^{15}$ would be more suitable for modeling these processes.

One of the anticipated applications of this potential is the effect of dissolved hydrogen on crack propagation in the lattice or at grain boundaries in Al. In this process, the hydrogen atoms can diffuse to the crack surfaces and eventually evaporate into the open space. With this in mind, we put special efforts to ensure that the potential predicts the formation of $H_2$ molecules with correct binding energy. While the fitting to properties of the $H_2$ molecule did not present a particular difficulty, preventing the formation of other hydrogen molecules did.

Indeed, because EAM potentials are designed to capture the metallic bonding, they normally predict evaporation to an atomic gas. If supersaturated, the gas can form clusters whose shape and size vary, depending on temperature and pressure. There is nothing in the EAM formalism that would stabilize diatomic molecules over larger molecules or clusters. To overcome this feature, we had to add a significant angular dependence of the interatomic forces to our potential. We also imposed strong constraints during the fitting that “discouraged” the formation of $H_n$ molecules with $n>2$. The result is a potential that does indeed reproduce the formation of $H_2$ gas out of an atomic gas or out of any other initial molecular structure. The stability of $H_2$ has been directly confirmed by MD simulations at several temperatures.

Overall, this work shows the ability of the ADP method to capture at least some basic features of systems with mixed chemical bonding. This experience suggests that the method could also be applicable to strongly covalent materials such as carbon or silicon in the future.

ACKNOWLEDGMENTS

We are grateful to G. P. Purja Pun for help with some of the MD simulations. This work was supported by the National Aeronautics and Space Administration through the Langley Research Center under Grant No. NRA NNX08AC07A.

*fapostol@gmu.edu
†ymishin@gmu.edu
$^{1}$Hydrogen Effects in Materials, edited by A. W. Thompson and N. R. Moody (TMS Warrendale, PA, 1994).
$^{2}$Hydrogen in Metals III, edited by H. Wipf (Springer, New York, 1997).
$^{3}$A. Barnoush and H. Vehoff, Acta Mater. 58, 5274 (2010).
$^{4}$H. Kamoutsi, G. N. Haidemenopoulos, V. Bontozoglou, and S. Pantelakis, Corros. Sci. 48, 1209 (2006).
$^{5}$G. M. Scamans, R. Alani, and P. R. Swann, Corros. Sci. 16, 443 (1976).
$^{6}$G. A. Young and J. R. Scully, Metall. Mater. Trans. A 33, 101 (2002).
$^{7}$M. Ruda, D. Farkas, and J. Abriata, Phys. Rev. B 54, 9765 (1996).
$^{8}$C. Wolverton, V. Ozolins, and M. Asta, Phys. Rev. B 69, 144109 (2004).
$^{9}$G. Lu and E. Kaxiras, Phys. Rev. Lett. 94, 155501 (2005).
$^{10}$L. Ismer, M. S. Park, A. Janotti, and C. G. Van de Walle, Phys. Rev. B 80, 184110 (2009).
$^{11}$M. Ji, C. Z. Wang, K. M. Ho, S. Adhikari, and K. R. Hebert, Phys. Rev. B 81, 024105 (2010).
$^{12}$A. Pedersen and H. Jónsson, Acta Mater. 57, 4036 (2009).
$^{13}$J. E. Angelo and M. I. Baskes, Interface Sci. 4, 47 (1996).
$^{14}$D. Tanguy and T. Magnin, Philos. Mag. 83, 3995 (2003).
$^{15}$J. G. O. Ojwang, R. A. van Santen, G. J. Kramer, A. C. T. van Duin, and W. A. Goddard, J. Chem. Phys. 131, 044501 (2009).
$^{16}$Y. Mishin, M. J. Mehl, and D. A. Papaconstantopoulos, Acta Mater. 53, 4029 (2005).
$^{17}$Y. Mishin and A. Y. Lozovoi, Acta Mater. 54, 5013 (2006).
$^{18}$A. Hashibon, A. Y. Lozovoi, Y. Mishin, C. Elsässer, and P. Gumbsch, Phys. Rev. B 77, 094131 (2008).
$^{19}$M. S. Daw and M. I. Baskes, Phys. Rev. Lett. 50, 1285 (1983).
$^{20}$M. S. Daw and M. I. Baskes, Phys. Rev. B 29, 6443 (1984).
$^{21}$Y. Mishin, D. Farkas, M. J. Mehl, and D. A. Papaconstantopoulos, Phys. Rev. B 59, 3393 (1999).
$^{22}$M. I. Baskes, Phys. Rev. Lett. 59, 2666 (1987).
$^{23}$R. Pasianot, D. Farkas, and E. J. Savino, Phys. Rev. B 43, 6952 (1991).
$^{24}$W. E. Dasent, Inorganic Energetics: An Introduction (Cambridge University Press, Cambridge, 1982).
$^{25}$B. I. Min, H. J. F. Jansen, and A. J. Freeman, Phys. Rev. B 30, 5076 (1984).
$^{26}$J. A. Nobel, G. A. Wilson, and S. B. Trickey, Int. J. Quantum Chem. 42, 1037 (1992).
$^{27}$Y. Mishin, in Handbook of Materials Modeling, edited by S. Yip (Springer, Dordrecht, The Netherlands, 2005), Chap. 2.2, pp. 459–478.
$^{28}$J. W. Turley and H. W. Rinn, Inorg. Chem. 8, 18 (1969).
$^{29}$S. Kirkpatrick, C. D. Gelatt, and M. P. Vecchi, Science 220, 671

144115-9

(1983).

30A. San-Martin and F. D. Manchester, J. Phase Equilibria 13, 17 (1992).

31G. C. Sinke, L. C. Walker, F. L. Oetting, and D. R. Stull, J. Chem. Phys. 47, 2759 (1967).

32R. A. H. Edwards and W. Eichenauer, Scr. Metall. 14, 971 (1980).

33W. Eichenauer, Z. Metallkd. 59, 613 (1968).

34H. Sugimoto and Y. Fukai, Acta Metall. Mater. 40, 2327 (1992).

35M. Ichimura, H. Katsuta, Y. Sasajima, and M. Imabayashi, J. Phys. Chem. Solids 49, 1259 (1988).

36G. A. Young and J. R. Scully, Acta Mater. 46, 6337 (1998).

37Y. Mishin, M. R. Sørensen, and A. F. Voter, Philos. Mag. A 81, 2591 (2001).

38S. Linderoth, H. Rajainmaki, and R. M. Nieminen, Phys. Rev. B 35, 5524 (1987).

39S. Linderoth, Philos. Mag. Lett. 57, 229 (1988).

40S. M. Myers, F. Besenbacher, and J. K. Nørskov, J. Appl. Phys. 58, 1841 (1985).

41H. Gunaydin, S. V. Barabash, K. N. Houk, and V. Ozolins, Phys. Rev. Lett. 101, 075901 (2008).

42J. K. Nørskov and F. Besenbacher, J. Less-Common Met. 130, 475 (1987).

43P. Nordlander, J. K. Nørskov, F. Besenbacher, and S. M. Myers, Phys. Rev. B 40, 1990 (1989).

44G. Mills, H. Jonsson, and G. K. Schenter, Surf. Sci. 324, 305 (1995).

45W. Eichenauer, K. Hattenbach, and A. Pebler, Z. Metallkd. 52, 682 (1961).

46T. Ishikawa and R. B. McLellan, Acta Metall. 34, 1091 (1986).

47C. Qiu, G. B. Olson, S. M. Opalka, and D. L. Anton, J. Phase Equilib. Diffus. 25, 520 (2004).
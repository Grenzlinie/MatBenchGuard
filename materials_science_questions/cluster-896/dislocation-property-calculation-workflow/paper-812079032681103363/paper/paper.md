Research Article

# First-Principles Study on the Elastic Constants and Structural and Mechanical Properties of $30^\circ$ Partial Dislocation in GaAs

Huili Zhang, $^{1}$ Qiannan Gao, $^{1}$ Defang Lu, $^{2}$ Yunchang Fu, $^{3}$ and Lumei Tong $^{3}$

$^{1}$ Department of Mathematics and Physics, Hebei Petroleum University of Technology, Chengde 067500, China
$^{2}$ Department of Automobile Engineering, Hebei Petroleum University of Technology, Chengde 067500, China
$^{3}$ College of Science, Kunming University of Science and Technology, Kunming 650500, China

Correspondence should be addressed to Defang Lu; q2384@163.com

Received 10 March 2021; Accepted 7 June 2021; Published 2 July 2021

Academic Editor: Alfonso Muñoz

Copyright © 2021 Huili Zhang et al. This is an open access article distributed under the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original work is properly cited.

The second-order elastic constants, third-order elastic constants, and the generalized-stacking-fault energy for semiconductor GaAs are investigated using the first-principles calculations. The predictions of elastic constants are obtained from the coefficients of the fitted polynomials of the energy-strain functions. It is found that the nonlinear elastic effects must be considered when the applied deformations are larger than approximately 1.5%. With the Lagrangian strains up to 6.4%, the terms included up to third order in energy expansion functions are sufficient. The elastic constants given in this work agree well with the previous results and experimental data except for $C_{144}$. $C_{144}$ given by the present paper is a positive value, and the estimated 3 GPa agrees well with the experimental result of 2 GPa. The research results can provide a reference for understanding the elasticity of GaAs. The generalized-stacking-fault energy has been calculated without and with structural relaxation, respectively. The unstable stacking fault energy with structural relaxation is about two-thirds of that without relaxation. The dislocation width and Peierls stress for $30^\circ$ partial in GaAs have been investigated based on the improved P-N theory. The dislocation width is very narrow (only about one-fifth of Burgers vector $b$), which is reasonable for covalent materials. The Peierls stress is about 4 GPa, in good agreement with the experimental result of 2~3 GPa.

## 1. Introduction
III-V semiconductors receive the widespread attention due to the latent application prospect, such as photo-detectors, lasers, and light-emitting diodes [1-5]. Among the III-V direct bandgap semiconductors, GaAs is one of the most promising candidates due to its high electron mobility [6, 7]. It has been widely used in many fields, such as solar cell fabrication [8], substrate materials [9, 10], and efficient photovoltaic devices [11, 12]. Recently, lots of experimental and theoretical research studies have been carried out to study the properties of GaAs. Elasticity and plasticity are two important mechanical properties of materials, and the study of these two properties plays an important role on understanding and utilization of materials. Consequently, the elastic and plastic properties of GaAs are also of particular interest. The elastic properties of solids can be well reflected by elastic constants. For single crystals, second-order elastic constants (SOECs) and third-order elastic constants (TOECs) are both important parameters for modeling the mechanical response. In the process of plastic deformation of materials, dislocations play a key role. Therefore, the study of the elastic constants (SOECs and TOECs) and the dislocation properties of GaAs is necessary. Many experimental and theoretical research studies have been performed on the elastic constants of semiconductor GaAs. Several methods such as ultrasonic wave propagation and optical interference are used to measure the SOECs and TOECs of GaAs [13-15]. Singh et al. have calculated the TOECs of GaAs using Keating theory [16]. First-principles calculations based on density functional theory are also widely used to investigate the elastic constants of GaAs [17-19]. These results are very vital for understanding the elasticity of GaAs. However, there still

exist argument for the magnitude and sign of the TOEC $C_{144}$.

The most fundamental quantity related to the plasticity of the crystal is the Peierls stress of dislocation. However, the research on the Peierls stress of dislocation in GaAs is very limited, no matter from experimental or theoretical method. Suzuki et al. and Kamimura et al. have estimated the Peierls stress of dislocations in GaAs by extrapolating the critical shear stress to the absolute zero temperature; the estimated Peierls stress is about 2~3 GPa [20, 21]. The Peierls stress of the $30^\circ$ partial in GaAs estimated by Kamimura et al. based on the classical $P$-$N$ model using $ab$-initio $\gamma$-surface is about 23 GPa [22], which is one magnitude larger than the experimental result approximately [21]. Actually, the crystal has been treated as an elastic continuum body in the classical $P$-$N$ model, while the discrete effect of lattice which is extremely important for the narrow dislocations in semiconductors is neglected [23-25]. The improved $P$-$N$ theory which has fully considered the discrete effect of the crystal has been proposed by Wang [26-28]. The research results show that the agreement between theoretical prediction given by improved $P$-$N$ theory and the numerical and experimental results can be significantly improved [29-31]. It has been established that the glide of dissociated dislocations on closed packed planes is responsible for the high temperature plasticity in zinc-blende crystals [21, 32]. And, the $30^\circ$ partial generally possesses higher Peierls stress compared with the $90^\circ$ partial and controls the deformation [33]. And, as such, the improved $P$-$N$ theory is applied for the $30^\circ$ partial in GaAs. The restoring force in the dislocation equation is generally given by the gradient of the generalized-stacking-fault energy (GSFE) as suggested by Christian and Vitek [34]. In this paper, the SOECs, TOECs, and GSFE along $(1/2)\langle112\rangle$ on glide set of GaAs have been calculated by the first-principles calculations. Based on the calculated SOECs and GSFE, the core width and Peierls stress of $30^\circ$ partial in GaAs have been investigated by the improved $P$-$N$ theory.

## 2. Determination of SOECs and TOECs

### 2.1. Computational Method.
The finite-strain continuum elasticity theory [35-40] is widely used to obtain the TOECs; the relation between the strain energy density $\Phi$ and the elastic constants can be expressed as follows [35, 36]:

$$
\Phi(\eta)=\frac{1}{2!} \sum_{ijkl} C_{ijkl} \eta_{ij} \eta_{kl}+\frac{1}{3!} \sum_{ijklmn} C_{ijklmn} \eta_{ij} \eta_{kl} \eta_{mn}+\cdots,
\tag{1}
$$

where $\eta$ is the Lagrangian strain tensor, and it can be defined as [37]

$$
\eta_{ij}=\frac{1}{2} \sum_{k}\left(J_{k i} J_{k j}-\delta_{ij}\right),
\tag{2}
$$

where $\delta_{ij}$ is an unit matrix; the deformation tensor $J_{ij}=(\partial x_{i}'/\partial x_{j})$ constructs the connection of initial configuration $x_{j}$ and strained configuration $x_{i}'$ at the equilibrium state.

The $\alpha$th - order($\alpha\geq2$) elastic constants were defined by Brugger as [38]

$$
C_{ijklmn...}=C_{IJK...}=\left.\frac{\partial^{\alpha} \Phi}{\partial \eta_{ij} \partial \eta_{kl} \partial \eta_{mn} \cdots}\right|_{\eta=0},
\tag{3}
$$

where $I$, $J$, and $K$ are Voigt subscripts, and the Lagranian strain tensor $\eta$ links this notation by

$$
\eta=(\eta_{1}, \eta_{2}, \eta_{3}, \eta_{4}, \eta_{5}, \eta_{6}).
\tag{4}
$$

Because of the cubic symmetry, there are three independent SOECs ($C_{11}$, $C_{12}$, and $C_{44}$) and six TOECs ($C_{111}$, $C_{112}$, $C_{123}$, $C_{144}$, $C_{155}$, and $C_{456}$). Introducing six Lagrangian strain tensors in terms of a single parameter $\zeta$ to calculate the SOECs and TOECs, the strain energy per unit mass can be written as a polynomial of the strain parameter $\zeta$ [41],

$$
\Phi(\eta)=A_{2} \zeta^{2}+A_{3} \zeta^{3}+O\left(\zeta^{4}\right),
\tag{5}
$$

where the coefficients $A_{2}$ and $A_{3}$ are comprised by the SOECs and TOECs of the crystal. The applied strains $\eta_{\alpha}$ with $\alpha=A$ to $F$ and the corresponding coefficients $A_{2}$ and $A_{3}$ are listed in Table 1 [42].

To obtain accurate TOECs, $\zeta$ is changed from $-0.064$ to $0.064$ with the step of $0.008$. For covalent bonding materials, the maximal amplitude $0.064$ of the deformations is enough to obtain the accurate TOECs. The elastic constants can be obtained from the least-square polynomial fitted from the strain-energy relation given by the first-principles total-energy calculations.

We perform first-principles total-energy calculations based on the density functional theory (DFT), using the $ab$-initio simulation package (VASP 4.6) [43-45]. In order to compare the performance of two different density functionals in the first-principles prediction of the lattice constant and SOECs, the local density approximation (LDA) and the Perdew-Burke-Ernzerhof (PBE) exchange-correlation functional for generalized gradient approximation (GGA) are, respectively, used. A plane-wave basis set is employed within the framework of the projector augmented wave (PAW) method [46, 47]. In the calculation, the wave functions are expanded as a plane wave basis with the cut-off energy of 550 eV. For the first Brillouin zone integrals, reciprocal space is represented by the Monkhorst-Pack special $k$-point scheme [48] with $21\times21\times21$ grid meshes. The convergence of energy and force are set to $1.0\times10^{-6}$ eV and $1.0\times10^{-4}$ (eV/Å), respectively. The equilibrium theoretical crystal structures are determined by minimizing the Hellmann-Feynman force on the atoms and stress on the unit cell.

The lattice constant and SOECs obtained with the LDA and GGA are presented in Table 2. The results show that the GGA overestimates, while the LDA underestimates the lattice constants, which is in agreement with [19] and [49]. And, it is obvious that the predictions of LDA are in better agreement with the experiment results, regardless of the lattice constant or the SOECs. Consequently, the calculation of the TOECs and the GSFE in the present paper is based on the LDA functional.

**Table 1:** The applied strains $\eta_{\alpha}$ and the corresponding coefficients $A_2$ and $A_3$ in equation (5) as combinations of SOECs and TOECs for crystals with cubic symmetry.

| Strain type               | $A_2$                          | $A_3$                              |
|---------------------------|--------------------------------|------------------------------------|
| $\eta_A = (\zeta, 0, 0, 0, 0)$ | $(1/2)C_{11}$                  | $(1/6)C_{111}$                     |
| $\eta_B = (\zeta, \zeta, 0, 0, 0)$ | $C_{11} + C_{12}$            | $(1/3)C_{111} + C_{112}$           |
| $\eta_C = (\zeta, \zeta, \zeta, 0, 0)$ | $(3/2)C_{11} + 3C_{12}$    | $(1/2)C_{111} + 3C_{112} + C_{123}$ |
| $\eta_D = (\zeta, 0, 0, \zeta, 0)$ | $(1/2)C_{11} + (1/2)C_{44}$ | $(1/6)C_{111} + (1/2)C_{144}$      |
| $\eta_E = (\zeta, 0, 0, 0, \zeta)$ | $(1/2)C_{11} + (1/2)C_{44}$ | $(1/6)C_{111} + (1/2)C_{155}$      |
| $\eta_F = (0, 0, 0, \zeta, \zeta)$ | $(3/2)C_{44}$                | $C_{456}$                          |

**Table 2:** Comparison of the calculated equilibrium lattice constants, SOECs, and TOECs with the experimental data and previous calculations. All data are in unit of GPa except of the lattice constant in Å.

|             | This work               | Previous study                                  | Experiment                          |
|-------------|-------------------------|------------------------------------------------|-------------------------------------|
| $a_0$       | $5.763^{\text{a}}$, $5.626^{\text{b}}$ | $5.671 \ (\text{GGA})^{\text{h}}$, $5.604 \ (\text{LDA})^{\text{h}}$, $5.75 \ (\text{GGA})^{\text{i}}$ | $5.653^{\text{j}}$, $5.65325^{\text{l}}$ |
| $C_{11}$    | $100^{\text{a}}$, $117^{\text{b}}$ | $126^{\text{g}}$, $118^{\text{h}}$, $100^{\text{i}}$, $133^{\text{k}}$ | $119.0^{\text{c}}$, $118.8^{\text{d}}$ |
| $C_{12}$    | $47^{\text{a}}$, $57^{\text{b}}$ | $55^{\text{g}}$, $54^{\text{h}}$, $49^{\text{j}}$, $57^{\text{k}}$ | $53.8^{\text{c}}$, $53.7^{\text{d}}$ |
| $C_{44}$    | $50^{\text{a}}$, $58^{\text{b}}$ | $61^{\text{g}}$, $61^{\text{h}}$, $52^{\text{i}}$, $62^{\text{k}}$ | $59.5^{\text{c}}$, $59.4^{\text{d}}$ |
| $C_{111}$   | $-691$                  | $-615^{\text{f}}$, $-600^{\text{g}}$, $-561^{\text{i}}$ | $-675^{\text{c}}$, $-622^{\text{d}}$, $-620^{\text{e}}$ |
| $C_{112}$   | $-407$                  | $-386^{\text{f}}$, $-401^{\text{g}}$, $-337^{\text{i}}$ | $-402^{\text{c}}$, $-387^{\text{d}}$, $-392^{\text{e}}$ |
| $C_{123}$   | $-67$                   | $-81^{\text{f}}$, $-94^{\text{g}}$, $-83^{\text{i}}$ | $-4^{\text{c}}$, $-57^{\text{d}}$, $-62^{\text{e}}$ |
| $C_{144}$   | $3$                     | $11^{\text{f}}$, $10^{\text{g}}$, $-14^{\text{i}}$ | $-70^{\text{c}}$, $2^{\text{d}}$, $8^{\text{e}}$ |
| $C_{155}$   | $-280$                  | $-282^{\text{f}}$, $-305^{\text{g}}$, $-244^{\text{i}}$ | $-320^{\text{c}}$, $-269^{\text{d}}$, $-274^{\text{e}}$ |
| $C_{456}$   | $-24$                   | $-46^{\text{f}}$, $-43^{\text{g}}$, $-22^{\text{i}}$ | $-69^{\text{c}}$, $-39^{\text{d}}$, $-43^{\text{e}}$ |

$^{\text{a}}$This work of GGA. $^{\text{b}}$This work of LDA. $^{\text{c}}$Ref [13] ($T = 298$ K). $^{\text{d}}$Ref [14] ($T = 298$ K). $^{\text{e}}$Ref [15] ($T = 298$ K). $^{\text{f}}$Ref [16]. $^{\text{g}}$Ref [17]. $^{\text{h}}$Ref [18]. $^{\text{i}}$Ref [19]. $^{\text{j}}$Ref [49]. $^{\text{k}}$Ref [50]. $^{\text{l}}$Ref [51].

### 2.2. Results and Discussion.
The strain energies from first-principles calculations and the fitted polynomials are shown in Figure 1. It is found that, for GaAs with the Lagrangian strain up to 6.4%, considering the terms up to third order in energy expansion is sufficient to obtain good consistency with the first-principles results. In addition, the strain energies with positive strains are always smaller than ones with negative strains; therefore, the values of TOECs are typically negative. In order to examine in which range of strains the third-order effects affect the properties of GaAs, the curves of the nonlinear elasticity comparison with the linear elasticity and the DFT results of a particular deformation $\eta_C$ are shown in Figure 2. One can see that when the applied deformations are larger than approximately 1.5%, the linear elasticity is not sufficient and the third-order effects must be considered. The calculated results for lattice constant and elastic constants are presented in Table 2. The results are all agreeing well with the previous results and experimental data except for $C_{144}$. The TOEC $C_{144}$ given by the present paper is a positive value, and the estimated value of 3 GPa agrees well with the experimental result of 2 GPa given in [14]. The results given by the present paper can provide a reference for understanding the elasticity of GaAs.

## 3. GSFE and Mechanical Properties of 30° Partial Dislocations

### 3.1. First-Principles Calculations of GSFE.
The first-principles total-energy calculations were used to calculate the GSFE, and the process of optimization is the same as the calculation of elastic constants. While for the Brillouin zone, the calculations of GSFE employ $21 \times 21 \times 1$ grid meshes. Because of the zinc-blende structure, there are two different slip planes (see Figure 3). The widely and closely spaced $\{111\}$ planes, respectively, correspond to the shuffle set and glide set. For discussing the properties of $30^\circ$ partial in GaAs, the GSFE along $(1/2)\langle 112\rangle$ on glide set has been calculated with a slab calculation. In order to simulate the process of stacking fault, we employ a slab consisting of 12 atomic layers in the $\langle 111\rangle$ direction. The vacuum space of $15\ \text{Å}$ normal to $\{111\}$ plane between the periodically repeated slab is chosen to avoid the interactions between two slabs. To obtain the reasonable results, we performed that the fluctuations of calculated results' vacuum gap of $15\ \text{Å}$ and $18\ \text{Å}$ are less than 0.1%. The GSFE was generated by a set of rigid shifts of the upper slab along $(1/2)\langle 112\rangle$ with respect to the lower slab. For the relaxed GSFE, all atoms of the system are allowed to move only in the $\langle 111\rangle$ by minimization of the Hellmann–Feynman forces on each atom. The calculated GSFE is shown in Figure 4. The unstable stacking fault energy with relaxation is about two-thirds of that without relaxation.

### 3.2. Mechanical Properties of 30° Partial Dislocation.
The mechanical properties of $30^\circ$ partial in GaAs have been studied theoretically based on the improved $P$-$N$ model [28]. As done generally, the restoring force is given by the gradient of the GSFE as suggested by Christian and Vitek [34]; the dislocation equation given by the improved $P$-$N$ model is

$$
-\frac{\beta}{2 \sigma} \frac{\mathrm{d}^{2} u}{\mathrm{~d} x^{2}}-\frac{K}{2 \pi} \int_{-\infty}^{+\infty} \frac{\mathrm{d} x^{\prime}}{x^{\prime}-x}\left(\frac{\mathrm{d} u}{\mathrm{~d} x}\right)\bigg|_{x=x^{\prime}}=-\nabla \gamma(u). \tag{6}
$$

![](./images/812079032681103363_1.jpg)

FIGURE 1: The strain-energy relations for GaAs. The discrete points denote the values of DFT calculations; solid curves represent the results obtained from third-order polynomial fitting.

![](./images/812079032681103363_2.jpg)

FIGURE 2: Energy as a function of Lagrangian strain parameter $\xi$ for particular deformation $\eta_C$. Empty points denote the results of DFT calculations; dashed and solid curves indicate the results obtained from linear and nonlinear elasticity theory, respectively.

![](./images/812079032681103363_3.jpg)

FIGURE 3: The two slip planes (glide set and shuffle set) for GaAs.

![](./images/812079032681103363_4.jpg)

FIGURE 4: GSFE curves along (1/2)<112> of the glide set for GaAs. The lines denote the fitted curves from Fourier series (equation (9)), and the discrete points denote the results given by first-principles calculations.

The second-order derivative term proportional to $\beta$ represents the correction from the discrete effect caused by the interaction among the atoms on the misfit plane. $\sigma$ is the area of the primitive cell in the misfit plane, and $u$ is the displacement field. The energy factor $K$ is [53]

$$
K=\mu\left(\frac{\sin ^{2} \theta}{1-\nu}+\cos ^{2} \theta\right), \tag{7}
$$

where $\theta$ is the dislocation angle and $\mu$ and $\nu$ are the effective shear modulus and Poisson's ratio in $\{111\}$ surface [53]. The discrete parameter $\beta$ for zinc-blende structure crystals has been investigated based on a simple dynamics model [54]. For glide partials, the parameter $\beta$ is

$$
\beta=\frac{\left(c_{11}-c_{12}\right) a_{0}^{3}}{16} \sin ^{2} \theta. \tag{8}
$$

$\gamma(u)$ can be obtained by fitting the calculated GSFE data with

$$
\gamma(u)=\gamma \cos ^{2} \frac{\pi u}{b}\left(1+\Delta_{1} \cos ^{2} \frac{\pi u}{b}+\Delta_{2} \cos ^{4} \frac{\pi u}{b}\right), \tag{9}
$$

where $b$ is the Burgers vector; the fitting curves are shown in Figure 4, and the fitting parameters $\gamma$, $\Delta_{1}$, and $\Delta_{2}$ are listed in Table 3.

<table>
<caption>Table 3: The fitting parameters of GSFE, half width $\xi$, and Peierls stress $\sigma_{P}$ of $30^{\circ}$ partial in GaAs. $\xi_{0}$ and $\sigma_{P}^{0}$ are the results without considering the discrete effect ($\beta=0$). The half width and Peierls stress are, respectively, in units of Burgers vector $b$ and GPa.</caption>
<thead>
<tr>
<th></th>
<th>$\gamma$</th>
<th>$\Delta_{1}$</th>
<th>$\Delta_{2}$</th>
<th>$\xi_{0}$</th>
<th>$\xi$</th>
<th>$\sigma_{P}^{0}$</th>
<th>$\sigma_{P}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>Relaxed</td>
<td>0.14</td>
<td>−0.71</td>
<td>0.27</td>
<td>0.16</td>
<td>0.22</td>
<td>8.11</td>
<td>4.29</td>
</tr>
<tr>
<td>Nonrelaxed</td>
<td>0.14</td>
<td>−0.34</td>
<td>0.15</td>
<td>—</td>
<td>0.17</td>
<td>—</td>
<td>9.79</td>
</tr>
</tbody>
</table>

The core structure can be determined by solving dislocation equation (6) with the truncating method proposed by Wang, and the Peierls stress can be obtained from the maximum slope of the dislocation energy [54, 55]. The calculated half width $\xi$ and Peierls stress $\sigma_{P}$ of $30^{\circ}$ partial in GaAs are listed in Table 3.

It is found that the core structure calculated from the relaxed GSFE is wider, and the Peierls stress is smaller. Because of bond flip appearing for large distortion, the results obtained from the relaxed GSFE is more reliable. The narrow core is reasonable for dislocations in covalent materials. Furthermore, it can be seen that the dislocations will be widened by the discrete effect, and consequently, the Peierls stress will be decreased. The discrete effect is especially important for the narrow dislocations in covalent crystals since it is related to the interaction among the atoms on the misfit plane. The estimated 4 GPa is in good agreement with the experimental results of 2~3 GPa [20, 21]. Furthermore, the Peierls stress of $30^{\circ}$ partial in GaAs given by the classical $P$-$N$ model is 23 GPa [22], about larger by one order of magnitude than that given by improved $P$-$N$ theory. In addition to negligence of the discrete effect, another possible reason for the difference is that the law of sinusoidal force is applied in [22], while the dimensionless parameters $\Delta_{1}$ and $\Delta_{2}$ have been introduced for modifying the sinusoidal force in the present paper.

## 4. Summary and Discussion

In this paper, the SOECs, TOECs, and GSFEs for semiconductor GaAs are investigated using the first-principles total-energy calculations. The predictions of SOECs and TOECs are obtained from the coefficients of the fitted polynomials of the energy-strain functions. It is found that the nonlinear elastic effects must be considered when the applied deformations are larger than approximately 1.5%. And, with the Lagrangian strains up to 6.4%, the terms included up to the third order in energy expansion functions are sufficient to obtain good agreement with our calculated results. The elastic constants given in this work agree well with the previous results and experimental data except $C_{144}$. Regarding the disagreement in the magnitude and sign of the TOEC $C_{144}$, the result given by the present paper is a positive value, and the magnitude of 3 GPa agrees well with the experiment result of 2 GPa given in [14]. Our result can provide a reference for understanding the elasticity of GaAs.

The GSFE has been calculated, respectively, without and with structural relaxation. The unstable stacking fault energy

with relaxation is about two-thirds of that without relaxa- tion. Based on the improved $P$-$N$ theory, the dislocation width and Peierls stress of $30^\circ$ partial in GaAs have been calculated. The dislocation is very narrow, and it is rea- sonable for covalent materials. Because of bond flip appearing for large distortion, the results obtained from the relaxed GSFE are more reliable. The estimated Peierls stress in this work is about 4 GPa; it is in good agreement with the experimental results of 2~3 GPa [20, 21]. Furthermore, according to the Peierls stresses given by the classical $P$-$N$ model and improved $P$-$N$ model, it is found that the discrete effect is very important and must be considered when in- vestigating the narrow dislocations in covalent crystals.

Data Availability

The data used to support the findings of the study are available from the corresponding author upon request.

Conflicts of Interest

The authors declare that they have no conflicts of interest.

Acknowledgments

The work was supported by the National Natural Science Foundation of China (Grant no. 11104120).

References

[1] X. Y. Zhao, J. H. Huang, Z. Y. Zhuo et al., "Optical properties of atomic defects in hexagonal boron nitride flakes under high pressure," *Chinese Physical Letters*, vol. 37, Article ID 044204, 2020.
[2] H. Masataka, S. Kohei, M. Hisashi et al., "Recent progress in $\text{Ga}_2\text{O}_3$ power devices," *Semiconductor Science and Technology*, vol. 31, Article ID 034001, 2016.
[3] L. Gao, Q. L. Liu, J. W. Yang et al., "High-pressure synthesis and thermal transport properties of polycrystalline $\text{BAs}_x$," *Chinese Physical Letters*, vol. 37, Article ID 066202, 2020.
[4] K. Rahul, P. Mukhopadhyay, A. Bag et al., "Comparison of different pathways in metamorphic graded buffers on GaAs substrate: Indium incorporation with surface roughness," *Applied Surface Science*, vol. 324, pp. 304-309, 2015.
[5] J. Millán, P. Godignon, X. Perpiñà, A. Pérez-Tomás, and J. Rebollo, "A survey of wide bandgap power semiconductor devices," *IEEE Transactions on Power Electronics*, vol. 29, p. 2155, 2014.
[6] B. W. Zhang, Z. G. Nie, B. Wang et al., "Ultrafast carrier relaxation dynamics of photoexcited GaAs and GaAs/AlGaAs nanowire array," *Physical Chemistry Chemical Physics*, vol. 22, p. 25819, 2020.
[7] J. J. Zhou and M. Bernardi, "Ab initio electron mobility and polar phonon scattering in GaAs," *Physical Review B*, vol. 94, Article ID 201201, 2016.
[8] D. Frank, G. Matthias, B. Paul et al., "Wafer bonded four- junction GaInP/GaAs//GaInAsP/GaInAs concentrator solar cells with 44.7% efficiency," *Progress in Photovoltaics*, vol. 22, p. 277, 2014.
[9] S. H. Zhang, W. Xu, S. M. Badalyan, and F. M. Peeters, "Piezoelectric surface acoustical phonon limited mobility of electrons in graphene on a GaAs substrate," *Physical Review B*, vol. 87, Article ID 075443, 2013.
[10] S. Takayuki, M. Ryuichi, and O. Tohru, "Two-dimensional superconducting state of monolayer Pb films on GAaS(110) in a strong parallel magnetic field," *Physical Review Letters*, vol. 111, Article ID 057005, 2013.
[11] Y. Jongseung, J. Sungjin, I. S. Chun et al., "GaAs photovoltaics and optoelectronics using releasable multilayer epitaxial as- semblies," *Nature*, vol. 465, pp. 329-333, 2010.
[12] J. A. Czaban, D. A. Thompson, and R. R. LaPierre, "GaAs core-shell nanowires for photovoltaic applications," *Nano Letters*, vol. 9, p. 148, 2009.
[13] J. R. Drabble and A. J. Brammer, "Third order elastic constants of gallium arsenide," *Solid State Communications*, vol. 4, p. 467, 1966.
[14] H. J. McSkimin and P. Andreatch, "Third-order elastic moduli of gallium arsenide," *Journal of Applied Physics*, vol. 38, p. 2610, 1967.
[15] Y. Abe and K. Imai, "Anharmonic properties of ultrasounds in diamond-type crystals and Quartz plate under an intense excitation," *Japanese Journal of Applied Physics*, vol. 25, p. 67, 1986.
[16] R. P. Singh and G. S. Verma, "Interaction of Ga and $\text{As}_2$ molecular beams with GaAs surfaces," *Journal of Applied Physics*, vol. 39, p. 4032, 1968.
[17] J. Söorgel and U. Scherz, "Ab initio calculation of elastic constants and electronic properties of ZnSe and ZnTe under uniaxial strain," *The European Physical Journal B*, vol. 5, p. 45, 1998.
[18] S. Saib and N. Bouarissa, "High-pressure band parameters for GaAs: first principles calculations," *Solid-State Electronics*, vol. 50, p. 763, 2006.
[19] M. Lopuszynski and J. A. Majewski, "Ab initio calculations of third-order elastic constants and related properties for se- lected semiconductors," *Physical Review B*, vol. 76, Article ID 045202, 2007.
[20] T. Suzuki, T. Yasutomi, and T. Tokuoka, "Plastic deformation of GaAs at low temperatures," *Philosophical Magazine A*, vol. 79, p. 2637, 1999.
[21] Y. Kamimura, K. Edagawa, and S. Takeuchi, "Experimental evaluation of the Peierls stresses in a variety of crystals and their relation to the crystal structure," *Acta Materialia*, vol. 61, p. 294, 2013.
[22] Y. Kamimura, K. Edagawa, A. M. Iskandarov, M. Osawa, et al., "Peierls stresses estimated via the Peierls-Nabarro model using ab-initio Y-surface and their comparison with experi- ments," *Acta Materialia*, vol. 148, pp. 355-362, 2018.
[23] B. Joos, Q. Ren, and M. S. Duesbery, "Peierls-Nabarro model of dislocations in silicon with generalized stacking-fault re- storing forces," *Physical Review B*, vol. 50, Article ID 5890, 1994.
[24] B. Joos and M. S. Duesbery, "The Peierls stress of dislocations: an analytic formula," *Physical Review Letters*, vol. 78, p. 266, 1997.
[25] V. V. Bulatov and E. Kaxiras, "Semidiscrete variational peierls framework for dislocation core properties," *Physical Review Letters*, vol. 78, Article ID 4221, 1997.
[26] S. F. Wang, "Lattice theory for structure of dislocations in a two-dimensional triangular crystal," *Physical Review B*, vol. 65, Article ID 094111, 2002.
[27] S. F. Wang, "An improvement of the Peierls equation by taking into account the lattice effects," *Chinese Physics*, vol. 14, p. 2575, 2005.

[28] S. F. Wang, "A unified dislocation equation from lattice statics," *Journal of Physics A: Mathematical and Theoretical*, vol. 42, Article ID 025208, 2009.

[29] S. F. Wang, H. L. Zhang, X. Z. Wu, and R. P. Liu, "Theoretical calculation of the dislocation width and Peierls barrier and stress for semiconductor silicon," *Journal of Physics: Con- densed Matter*, vol. 22, Article ID 055801, 2010.

[30] S. F. Wang, R. P. Liu, and X. Z. Wu, "The discrete correction of the core structure for the $\langle 100 \rangle$ $\{100\}$ edge dislocation in bcc Fe," *Journal of Physics: Condensed Matter*, vol. 20, Article ID 485207, 2008.

[31] X. Z. Wu and S. F. Wang, "On the properties of $\langle 111 \rangle$ $\{110\}$ dissociated superdislocation in B2 structure YAg and YCu: Core structure and Peierls stress," *Frontiers of Materials Science in China*, vol. 3, p. 205, 2009.

[32] H. O. K. Kirchner and T. Suzuki, "Plastic homology of tet- rabonded crystals," *Acta Materialia*, vol. 46, p. 305, 1998.

[33] H. Alexander, *Dislocation in Solids*, Vol. 7, Elsevier, Amsterdam, Netherlands, 1986.

[34] J. W. Christian and V. Vitek, "Dislocations and stacking faults," *Reports on Progress in Physics*, vol. 33, p. 307, 1970.

[35] F. Birch, "Finite elastic strain of cubic crystals," *Physical Review*, vol. 71, p. 809, 1947.

[36] T. D. Murnaghan, *Finite Deformation of an Elastic Solid*, John Wiley and Sons, Inc., New York, NY, USA, 1951.

[37] R. N. Thurston and K. Brugger, "Third-order elastic constants and the velocity of small amplitude elastic waves in homo- geneously stressed media," *Physical Review*, vol. 133, Article ID A1604, 1964.

[38] K. Brugger, "Thermodynamic definition of higher order elastic coefficients," *Physical Review*, vol. 133, Article ID A1611, 1964.

[39] A. G. Every and A. K. McCurdy, "Landolt-Börnstein nu- merical data and functional relationships in science and technology, new series, group III: crystal and solid state physics," *Low Frequency Properties of Dielectric Crystals, Subvolume A: Second and Higher Order Elastic Constants*, Vol. 29, Springer-Verlag, Berlin, Germany, 1992.

[40] M. Born and K. Huang, *Dynamical Theory of Crystal Lattices*, Clarendon Press, Oxford, UK, 1954.

[41] J. J. Zhao, J. M. Winey, and Y. M. Gupta, "First-principles calculations of second- and third-order elastic constants for single crystals of arbitrary symmetry," *Physical Review B*, vol. 75, Article ID 094105, 2007.

[42] R. Wang, S. F. Wang, X. Z. Wu, and Y. Yao, "The third-order elastic moduli and pressure derivatives for AlRE (RE = Y, Pr, Nd, Tb, Dy, Ce) intermetallics with B2-structure: a first- principles study," *Solid State Communications*, vol. 151, p. 996, 2011.

[43] G. Kresse and J. Hafner, "Ab initio molecular dynamics for open-shell transition metals," *Physical Review B*, vol. 48, Article ID 13115, 1993.

[44] G. Kresse and J. Furthmüller, "Efficiency of Ab-initio total energy calculations for metals and semiconductors using a plane-wave basis set," *Computational Materials Science*, vol. 6, p. 15, 1996.

[45] G. Kresse and J. Furthmüller, "Efficient iterative schemes for Ab initio total-energy calculations using a plane-wave basis set," *Physical Review B*, vol. 54, Article ID 11169, 1996.

[46] P. E. Blöchl, "Projector augmented-wave method," *Physical Review B*, vol. 50, Article ID 17953, 1994.

[47] G. Kresse and D. Joubert, "From ultrasoft pseudopotentials to the projector augmented-wave method," *Physical Review B*, vol. 59, Article ID 1758, 1999.

[48] H. J. Monkhorst and J. D. Pack, "Special points for Brillouin- zone integrations," *Physical Review B*, vol. 13, p. 5188, 1976.

[49] M. Arrigoni and G. K. H. Madsen, "Comparing the perfor- mance of LDA and GGA functionals in predicting the lattice thermal conductivity of III-V semiconductor materials in the zincblende structure: the cases of AlAs and BAs," *Compu- tational Materials Science*, vol. 156, p. 354, 2019.

[50] R. W. G. Wycko, *Crystal Structures*, Vol. 1, Interscience, New York, NY, USA, 1963.

[51] N. Bouarissa and R. Bachiri, "Elastic constants and related properties of $\text{Al}_x\text{Ga}_{1-x}\text{As}_y\text{Sb}_{1-y}$/InAs," *Physica B*, vol. 322, p. 193, 2002.

[52] J. S. Blakemore, "Semiconducting and other major properties of gallium arsenide," *Journal of Applied Physics*, vol. 53, p. R123, 1982.

[53] J. P. Hirth and J. Lothe, *Theory of Dislocations*, Wiley, New York, NY, USA, 2nd edition, 1982.

[54] S. F. Wang, "Dislocation energy and Peierls stress: a rigorous calculation from the lattice theory," *Chinese Physics*, vol. 15, Article ID 1301, 2006.

[55] S. F. Wang, "Dislocation solution in slowly varying approx- imation," *Physics Letters A*, vol. 313, p. 408, 2003.
# Analysis of band-anticrossing model in GaNAs near localised states

Masoud Seifikar*\(^{1,2}\), Eoin P. O'Reilly\(^{1,2}\), and Stephen Fahy\(^{1,2}\)

\(^1\)Tyndall National Institute, Lee Maltings, Prospect Row, Cork, Ireland
\(^2\)Department of Physics, University College Cork, Cork, Ireland

Received 29 July 2010, revised 18 February 2011, accepted 1 March 2011
Published online 8 April 2011

Keywords dilute nitrides, electronic structure, semiconductor alloys

* Corresponding author: e-mail masoud.seifikar@tyndall.ie, Phone: +353 21 4904260, Fax: +353 21 4904058

Replacing As by N in GaNAs leads to a strong perturbation of the conduction band structure, generally described using the band-anticrossing (BAC) model. We have solved the single particle Hamiltonian for a very large supercell containing randomly placed nitrogen and have calculated the fractional \(\Gamma\) character, localisation factor and the density of states in the supercell. Comparison of these results with those calculated by the 2-level BAC model confirms the validity of the BAC model at energies away from N state energies but highlights the role of disorder at energies close to the N state energy.

© 2011 WILEY-VCH Verlag GmbH & Co. KGaA, Weinheim

## 1 Introduction
Dilute nitrite semiconductor alloys have been of great research interest, because of their unusual electronic properties and potential device applications [1]. The substitution of nitrogen atoms for a small fraction \(x\) of the group V elements in conventional III–V semiconductors such as GaAs or GaInAs strongly affects their electronic structure, with potential benefit for a range of optoelectronic devices. The rapid reduction in energy gap in \({\rm GaN_xAs_{1-x}}\) with increasing \(x\) is well explained in terms of a band-anticrossing (BAC) interaction between the GaAs host matrix conduction band (CB) edge and a set of N resonant defect levels above the CB edge [2]. The BAC model predicts an energy gap in the CB dispersion of GaNAs, above the N resonant state energy, which makes it difficult to investigate carrier transport in dilute nitride alloys such as GaNAs. However, the density of states (DOS), measured [3] and calculated using a Green's function method [4, 5], indicates a filling of this gap.

We investigate here the accuracy of the BAC model in describing the band structure of GaNAs, including the electronic structure both away from and close to the N resonant state energy. We directly solve a simplified random impurity model Hamiltonian for a very large supercell of GaNAs. We calculate the exact eigenstates of this Hamiltonian, and compare their behaviour with that predicted by the BAC model. Our results confirm the validity of the BAC model to describe states whose energy is well separated from the N resonant state energy. Our results also show that states with energy close to the N level energy are likely to be localised, implying a breakdown in the \(k\) selection assumed in the BAC model for such states. We discuss briefly the consequences of this state localisation for electron transport at high electric fields in dilute nitride alloys.

## 2 Band anti-crossing model
The band anticrossing model was introduced by Shan et al. [2] to explain the properties of III–V dilute nitrides and other mismatched alloys. The BAC model describes the electronic structure of dilute nitride material by considering the interaction between the de-localised states of the host semiconductor and localised impurity states. It is well known that an isolated N atom introduces a localised state with energy level \(E_{\rm N}\) in conventional III–V materials [6]. According to the BAC model, the Hamiltonian of \({\rm GaAs_{1-x}N_x}\) is given by:

$$
H = \begin{pmatrix}
E_{\rm M} & V_{\rm NM} \\
V_{\rm NM} & E'_{\rm N} + i\Gamma_{\rm N}
\end{pmatrix}, \tag{1}
$$

where \(E_{\rm M} = E_{\rm c} + \hbar^2k^2/(2m^*)\) is the CB energy, \(E'_{\rm N}\) the nitrogen state energy, \(\Gamma_{\rm N}\) the broadening of the nitrogen states, \(\hbar\) and \(k\) are the reduced Planck constant and wavevector, respectively, \(m^*=0.067m_0\) the GaAs effective mass, and \(m_0\) is the free electron mass. In this paper, all

© 2011 WILEY-VCH Verlag GmbH & Co. KGaA, Weinheim

energies are referenced to the GaAs CB edge energy $E_{\mathrm{c}}$. The coupling matrix element $V_{\mathrm{NM}}$ between the nitrogen and CB states depends on nitrogen concentration $x$, as $V_{\mathrm{NM}}=\beta x^{1 / 2}$ [7,8], where we choose here $\beta=2.0 \mathrm{eV}$ as the interaction parameter. The energies of the BAC upper and lower conduction subbands, denoted by $E_{+}$and $E_{-}$, are then given by:

$$
E_{ \pm}=\frac{E_{\mathrm{N}}^{\prime}+i \Gamma_{\mathrm{N}}+E_{\mathrm{M}}}{2} \pm \frac{\sqrt{\left(E_{\mathrm{N}}^{\prime}+i \Gamma_{\mathrm{N}}-E_{\mathrm{M}}\right)^{2}+4 V_{\mathrm{Nc}}^{2}}}{2}.
\tag{2}
$$

The magnitude of the imaginary part of the N energy, $\Gamma_{\mathrm{N}}$ has been estimated using the Green's function method as $\Gamma_{\mathrm{N}}=\pi \beta^{2} D\left(E_{\mathrm{N}}^{\prime}\right) / N_{\mathrm{a}}$ [9], where $N_{\mathrm{a}}$ is the number of group $\mathrm{V}$ atoms in the system, and $D\left(E_{\mathrm{N}}^{\prime}\right)$ is the GaAs CB DOS at $E_{\mathrm{N}}^{\prime}$.

### 3 Supercell model
In order to test the BAC model, we consider a large supercell of side length $L$, with $M$ randomly placed nitrogen states in the supercell. Using the manyimpurity Anderson model [4,5,10], the Hamiltonian of this system can be written as $H=H_{0}+V$, where $H_{0}$ is a sum of two terms describing the energies of extended and localised states, labelled by wave vector $|\boldsymbol{k}\rangle$ and position vector $|j\rangle$, respectively, as follows:

$$
H_{0}=\sum_{\boldsymbol{k}} E_{\boldsymbol{k}}|\boldsymbol{k}\rangle\langle\boldsymbol{k}|+\sum_{j=1}^{M} E_{\mathrm{N}}|j\rangle\langle j|.
\tag{3}
$$

The first term in $H_{0}$ describes the host matrix CB states satisfying periodic boundary conditions in the supercell, given by: $\psi_{n_{x}, n_{y}, n_{z}}=1 / L^{3 / 2} \exp \left[i\left(k_{x} x+k_{y} y+k_{z} z\right)\right]$, with energies equal to $E_{n_{x}, n_{y}, n_{z}}=\left(k_{x}^{2}+k_{y}^{2}+k_{z}^{2}\right) \hbar^{2} / 2 m^{*}+E_{\mathrm{c}}$, where $k_{i}=2 \pi n_{i} / L$, and $n_{i}$ is an integer. We include in our calculations all host states with energy $E_{n_{x}, n_{y}, n_{z}} \leq E_{\max }$, where $E_{\max }=4 \pi^{2} \hbar^{2} l^{2} /\left(m^{*} L^{2}\right)$, and $l$ is a positive integer. The second term describes the $M$ nitrogen states in the supercell, where $M=x N_{\mathrm{a}}$.

The second term in the Hamiltonian represents an interaction between extended and localised states as:

$$
V=\sum_{\boldsymbol{k}, j} V_{\mathrm{Nc}}\left[\mathrm{e}^{i \boldsymbol{k} \cdot \boldsymbol{R}_{j}}|\boldsymbol{k}\rangle\langle j|+\mathrm{e}^{-i \boldsymbol{k} \cdot \boldsymbol{R}_{j}}|j\rangle\langle\boldsymbol{k}|\right],
\tag{4}
$$

where $\boldsymbol{R}_{j}$ is the position of $j$-th $\mathrm{N}, \boldsymbol{k}=\left(k_{x}, k_{y}, k_{z}\right)$ the wavevector, and $V_{\mathrm{Nc}}=\beta / N_{\mathrm{a}}^{1 / 2}$ is the interaction parameter. In each cubic unit cell volume $a_{0}^{3}$, we have four group-V atoms. So for a supercell with side length $L=L_{0} a_{0}$, we have $N_{\mathrm{a}}=4 L_{0}^{3}$. Thus, for $\mathrm{GaAs}_{1-x} \mathrm{~N}_{x}$, $x=M / N_{\mathrm{a}}=M / 4 L_{0}^{3}$, and $V_{\mathrm{Nc}}=\beta /\left(4 L_{0}^{3}\right)^{1 / 2}$. For most calculations, we took a 4 million atom supercell $\left(L_{0}=100\right)$, adding $M=8000 \mathrm{~N}$, and choosing $l=11$, so that $E_{\max }=0.857 \mathrm{eV}$. The $\mathrm{N}$ energy, $E_{\mathrm{N}}$ in Eq. (3) differs by $\Delta E_{\mathrm{N}}$ from the value $E_{\mathrm{N}}^{\prime}$ in Eq. (1). This is because the interaction with the CB states shifts the mean $\mathrm{N}$ energy.

This energy shift can be calculated from second order perturbation theory as $[9,11]$:

$$
\Delta E_{\mathrm{N}}=\int_{0}^{E_{\max }} \frac{|\langle\boldsymbol{k}|V| j\rangle|^{2}}{E-E_{\mathrm{N}}} D(E) \mathrm{d} E,
\tag{5}
$$

with $\Delta E_{\mathrm{N}}=-13.3 \mathrm{meV}$ when we choose $E_{\mathrm{N}}=0.23 \mathrm{eV}$ and $E_{\max }=0.857 \mathrm{eV}$.

Using the Hamiltonian $H$ we can then calculate different parameters for the chosen supercell. In the rest of this paper, we calculate for supercell states their fractional $\Gamma$ factor, the DOS and wave function localisation factors, and compare the results with the BAC model.

### 4 Fractional $\boldsymbol{\Gamma}$ character
The supercell CB states $\left|c_{i}\right\rangle$, are a linear combination of the original GaAs CB states $|\boldsymbol{k}\rangle$ and localised states $|j\rangle$. We can calculate the fractional $\Gamma$ character $f_{\Gamma}$ of a supercell eigenstate by summing the CB state weights, $\left|\left\langle\boldsymbol{k} \mid c_{i}\right\rangle\right|^{2}$ over all $\boldsymbol{k} . f_{\Gamma}$ provides a measure of the host matrix character of a given state. $f_{\Gamma}$ is equal to the ratio of the GaAs to the alloy effective mass. The blue dots in Fig. 1 shows the $\Gamma$ character calculated for the large supercell of size $L_{0}=100$, with $M=8000$.

We also calculate $f_{\Gamma}$ for the eigenstates of the BAC model of Eq. (1). The dotted line in Fig. 1, shows the variation of $f_{\Gamma}=\left|\alpha_{\boldsymbol{k}}^{ \pm}\right|^{2}$ calculated using the 2-band BAC model of Eq. (1) with $\Delta E_{\mathrm{N}}=0\left(E_{\mathrm{N}}=0.23 \mathrm{eV}\right)$, where $\alpha_{\boldsymbol{k}}^{ \pm}$ is the amplitude for $E_{ \pm}$of the BAC eigenstate on the host $\boldsymbol{k}$ state. The solid (red) line in Fig. 1 shows the 2-band $f_{\Gamma}$ when we include this shift $\left(E_{\mathrm{N}}^{\prime}=0.2167 \mathrm{eV}\right)$. Very good agreement is obtained over a wide energy range between the supercell calculation and the BAC model with shifted $\mathrm{N}$ energy in Fig. 1. It can be seen, however, that for energies just below $E_{\mathrm{N}}$ the numerical results move towards the BAC model result with the original unshifted $\mathrm{N}$ energy.

![](./images/811669235301351427_1.jpg)

Figure 1 (online colour at: www.pss-b.com) Fractional $\Gamma$ character of the energy eigenstates in a $x=0.2 \%$ calculation for cell size $L=100 a_{0}$ (blue dots), compared with results from the BAC model of Eq. (1) (dashed green) and a BAC model with a shifted $E_{\mathrm{N}}$ (solid red line).

## 5 Density of states
The DOS projected onto a single CB momentum eigenstate $(n_x, n_y, n_z)$ is given by:

$$
D_{n_x,n_y,n_z}(E) = \sum_i \delta(E-E_i)\left|a_{n_x,n_y,n_z}^i\right|^2,
\tag{6}
$$

where $a_{n_x,n_y,n_z}^i$ is the amplitude of the $i^{\text{th}}$ wave function on the given CB state. We use a Gaussian function with broadening parameter $\varepsilon=3$ meV to represent the $\delta$-function. The solid blue lines in Fig. 2 show how the DOS projected onto the individual $\boldsymbol{k}$ states varies with increasing energy $E_{\text{M}}$ of the $\boldsymbol{k}$ states. The dashed red lines in Fig. 2 display the results calculated by the BAC model. In this model the DOS projected onto a single $\boldsymbol{k}$ state, is given by: $D_{\text{p}}=d_{-}+d_{+}$ where:

$$
d_{\pm} = \frac{\left|\alpha_{\pm}\right|^2}{\pi} \frac{\Delta_{\pm}}{\left(E-E_{\text{p}_{\pm}}\right)^2+\Delta_{\pm}^2},
\tag{7}
$$

where $E_{p\pm}$ and $\Delta_{\pm}$ are the real and imaginary parts of $E_{\pm}$ calculated from Eq. (2) and $\alpha_{\pm}$ is the first coefficient of the corresponding normalised eigenvector. We see very good agreement between the BAC model (with energy broadening and shifted N energy) and our supercell model eigenstates. Small differences are observed near the CB edge, $E_{\text{M}}=0$. However, for $E_{\text{M}}$ near the N state energy, the results of the BAC model are very similar to the supercell calculations. A strong splitting of bands is seen especially near the N state energy.

We consider now the 3D DOS for a supercell of size $L^3$, which can be calculated for energy $E$ in the BAC model as $D(E)=L^3k^2/[\pi^2(\text{d}E/\text{d}k)]$.

![](./images/811669235301351427_2.jpg)

**Figure 2** (online colour at: www.pss-b.com) The DOS projected onto selected GaAs $|\boldsymbol{k}\rangle$ states, calculated using the BAC model (dashed red lines) and using the numerical model for a box with $L_0=100, l=11, M=8000$ and $\varepsilon=3$ meV (solid blue lines), and the BAC model (dashed red lines). Arrows show the energy $E_{\text{M}}$ of the original $\boldsymbol{k}$ state, and dotted line displays the N energy, $E_{\text{N}}$.

The DOS projected onto the $\Gamma$ valley (host CB) states, $D_{\text{cb}}(E)$, obtained by multiplying $D(E)$ by $f_{\Gamma}$ for each $\boldsymbol{k}$ value, is given by the real part of:

$$
D_{\text{cb}}(E) = \frac{(2m^{*})^{3/2}L^3}{4\pi^2\hbar^3} \left[ E-E_{\text{c}}-\frac{V_{\text{NM}}^2}{E-(E_{\text{N}}'+i\Gamma_{\text{N}})} \right]^{1/2}.
\tag{8}
$$

For $V_{\text{NM}}=0$, we recover the usual GaAs DOS. The inset in Fig. 3b shows the DOS of GaAs in the absence of N, determined by the numerical calculation for the supercell with $L=100a_0$, $l=11$ ($E_{\text{max}}=0.857$ eV), and a Gaussian broadening $\varepsilon=20$ meV (solid line), compared to the DOS calculated analytically, $D_{\text{GaAs}}$ ($E$) (dashed line). The DOS projected onto the GaAs CB states, in the supercell calculation, is:

$$
D_{\text{cb}}(E) = \sum_{i,\boldsymbol{k}} \delta(E-E_i)\left|a_{\boldsymbol{k}}^i\right|^2.
\tag{9}
$$

The solid line in Fig. 3a shows the DOS projected onto the host CB states for a $\text{GaAs}_{1-x}\text{N}_x$ supercell with $x=0.2\%$ and $E_{\text{max}}=0.857$ eV. This is compared with the projected DOS from the BAC model of Eq. (1) with $E_{\text{max}}=\infty$, and with and without broadening. The unbroadened DOS in the BAC model has an (integrable) divergence as $E$ approaches

![](./images/811669235301351427_3.jpg)

**Figure 3** (online colour at: www.pss-b.com) (a) The DOS projected onto the GaAs CB states for $\text{GaAs}_{1-x}\text{N}_x$ with $x=0.2\%$; obtained from: (i) the BAC model with and without N broadening, and assuming $E_{\text{max}}=\infty$ (dashed red and dashed-dotted grey lines, respectively), (ii) a supercell calculation including 8000 N (solid blue line) and (iii) a Green's function method with $E_{\text{max}}=0.857$ eV (green dots). (b) Comparison between the total DOS (blue solid line), and the DOS projected onto the host CB states (red dashed line). The inset shows the GaAs DOS calculated for a supercell (solid line) and analytically (dashed line).

![](./images/811669235301351427_4.jpg)

Figure 4 (online colour at: www.pss-b.com) Localisation factor calculated from Eq. (10) for the supercell of size $L_0=50$, with $M=1000$ and $l=12$. Vertical lines display band edges predicted by the BAC model with $E_{\text{max}}=4.08$ eV.

the N state energy, due to the infinite set of $k$ values allowed for in Eq. (1). The green dots show the DOS calculated using the Green's function method [4], with a cut-off energy equal to that for the supercell calculation. The excellent agreement between the two calculations confirms the validity of using the Green's function and BAC method to describe the CB-projected DOS for the given Hamiltonian. Adding the DOS projected on the N states in the supercell calculation gives the total DOS (blue solid line) in Fig. 3b. The DOS projected onto the N states is clearly much larger than the DOS projected onto the host CB states (red dashed line).

6 Localisation factor We investigate the degree of localistaion of each state by calculating the localisation factor $L$ for the CB part of each wave function, given by [12]:

$$
L\left(E_{i}\right)=\frac{V \int_{V} \mathrm{~d}^{3} \boldsymbol{r}\left|\psi_{i}^{\mathrm{cb}}(\boldsymbol{r})\right|^{4}}{\left(\int_{V} \mathrm{~d}^{3} \boldsymbol{r}\left|\psi_{i}^{\mathrm{cb}}(\boldsymbol{r})\right|^{2}\right)^{2}},
\tag{10}
$$

where $\psi_{i}^{\mathrm{cb}}(\boldsymbol{r})=\sum_{k} a_{k}^{i} \exp (i \boldsymbol{k} \cdot \boldsymbol{r})$, and $V=L_{0}^{3} a_{0}^{3}$ is the supercell volume. Figure 4 shows the calculated localisation factor for all states in a supercell with length $L_0=50$, containing $M=1000$ N, $(x=0.2\%)$ and with $l=12$. To compare with the BAC model, the maximum of the lower band $E_{\mathrm{N}}^{\prime}$, and minimum of the upper band $E_{+0}$, are indicated on Fig. 4. The larger values of $L(E)$ in the BAC gap indicate that the states in this energy range (which have predominantly N character) are localised, in agreement with the experimental analysis of Patanè et al. [13, 14]. We conclude, given the large density of N-related states near the N energy in Fig. 3b and the localised nature of these states from Fig. 4 that we may need to use a hopping transport model to describe conduction through such states when investigating high field transport in dilute nitride alloys.

7 Discussion and conclusion We have shown by direct comparison with a supercell model Hamiltonian that the BAC model provides a good description of the electronic structure of dilute nitride alloys at energies which are well separated from the N state energy. For simplicity, we have neglected the effect of nitrogen pairs or larger clusters, that would provide further perturbation and localisation in the CB of the host semiconductor [15, 16]. Our calculations show that the electronic structure deviates from that predicted using the BAC model close to the N resonant state energy, due to the finite density of N-related states, and carrier localisation effects (breakdown of $k$ selection). We conclude that it may be necessary when modelling transport to consider hopping through the N states, at energies close to the N resonant state and BAC energy gap range.

Acknowledgements This work was supported by Science Foundation Ireland. We thank M. Vaughan for useful discussions.

### References

[1] A. Erol, Dilute III-V Nitride Semiconductors and Material Systems: Physics and Technology (Springer-Verlag, Berlin, Heidelberg, 2008).
[2] W. Shan, W. Walukiewicz, J. W. Ager, E. E. Haller, J. F. Geisz, D. J. Friedman, J. M. Olson, and S. R. Kurtz, Phys. Rev. Lett. 82(6), 1221-1224 (1999).
[3] L. Ivanova, H. Eisele, M. P. Vaughan, P. Ebert, A. Lenz, R. Timm, O. Schumann, L. Geelhaar, M. Dähne, S. Fahy, H. Riechert, and E. P. O'Reilly, Phys. Rev. B 82(16), 161201 (2010).
[4] M. P. Vaughan and B. K. Ridley, Phys. Rev. B 75(19), 195205 (2007).
[5] N. Vogiatzis and J. Rorison, J. Phys.: Condens. Matter 21, 255801 (2009).
[6] D. J. Wolford, J. A. Bradley, K. Fry, and J. Thompson, in Proceedings of 17th Intenational Conference on the Physics of Semiconductors (Springer, New York, 1984), p. 627.
[7] A. Lindsay and E. P. O'Reilly, Solid State Commun. 112(8), 443-447 (1999).
[8] E. P. O'Reilly, A. Lindsay, P. J. Klar, A. Polimeni, and M. Capizzi, Semicond. Sci. Technol. 24(3), 033001 (2009).
[9] S. Fahy, A. Lindsay, H. Ouerdane, and E. P. O'Reilly, Phys. Rev. B 74(3), 035203 (2006).
[10] P. W. Anderson, Phys. Rev. 124(1), 41-53 (1961).
[11] U. Fano, Phys. Rev. 124(6), 1866-1878 (1961).
[12] R. J. Bell and P. Dean, Discuss. Faraday Soc. 50, 55-61 (1970).
[13] A. Patanè, A. Ignatov, D. Fowler, O. Makarovsky, L. Eaves, L. Geelhaar, and H. Riechert, Phys. Rev. B 72(3), 033312 (2005).
[14] A. Patanè, J. Endicott, J. Ibáñez, P. N. Brunkov, L. Eaves, S. B. Healy, A. Lindsay, E. P. O'Reilly, and M. Hopkinson, Phys. Rev. B 71(19), 195307 (2005).
[15] A. Lindsay and E. P. O'Reilly, Phys. Rev. Lett. 93(19), 196402 (2004).
[16] X. Liu, M. Pistol, L. Samuelson, S. Schwetlick, and W. Seifert, Appl. Phys. Lett. 56(15), 1451 (1990).
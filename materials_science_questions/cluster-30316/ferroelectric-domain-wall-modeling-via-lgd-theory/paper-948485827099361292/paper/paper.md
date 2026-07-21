# Two-dimensional Discommensurations: an extension to McMillan's Ginzburg-Landau Theory

Lotte Mertens, $^{1,2}$ Jeroen van den Brink, $^{2,3}$ and Jasper van Wezel$^{1}$

$^{1}$Institute for Theoretical Physics, University of Amsterdam,
Science Park 904, 1098 XH Amsterdam, The Netherlands
$^{2}$Institute for Theoretical Solid State Physics, IFW Dresden and Würzburg-Dresden
Cluster of Excellence ct.qmat, Helmholtzstr. 20, 01069 Dresden, Germany
$^{3}$Institute for Theoretical Physics, TU Dresden, 01069 Dresden, Germany
(Dated: February 14, 2024)

Charge density waves (CDW) profoundly affect the electronic properties of materials and have an intricate interplay with other collective states, like superconductivity and magnetism. The well-known macroscopic Ginzburg-Landau theory stands out as a theoretical method for describing CDW phenomenology without requiring a microscopic description. In particular, it has been instrumental in understanding the emergence of domain structures in several CDW compounds, as well as the influence of critical fluctuations and the evolution towards or across lock-in transitions. In this context, McMillan's foundational work introduced discommensurations as the objects mediating the transition from commensurate to incommensurate CDW, through an intermediate nearly commensurate phase characterised by an ordered array of phase slips. Here, we extend the simplified, effectively one-dimensional, setting of the original model to a fully two-dimensional analysis. We find exact and numerical solutions for several types of discommensuration patterns and provide a framework for consistently describing multi-component CDW embedded in quasi-two-dimensional atomic lattices.

## I. INTRODUCTION

Various materials display phases with charge density waves: periodic modulation of electronics charge density among a crystalline atomic lattice in (static) wavelike patterns. The presence of CDWs impacts, among other things, the electronic and transport properties of materials. Furthermore, CDWs can influence the emergence of other collective states, such as superconductivity or magnetism$^{1-10}$. Theoretical models capturing the qualitative physics of the CDW phase are well-known both starting from a microscopic description, such as in the Peierls model$^{11,12}$, and in terms of macroscopic order parameter theories based on the Ginzburg-Landau paradigm$^{13-16}$. Moreover, recent advances in experimental techniques and material synthesis have enabled the detailed exploration of CDWs in various material classes, leading to tunable properties and potential applications in areas like nanoscale electromechanics and energy storage$^{17-20}$.

Often, multiple charge ordered phases are present in the phase diagram of a single material. Generically, these go from the high-temperature metallic phase to an incommensurate CDW at lower temperature, which can turn into an ordered array of commensurate patches as it is cooled further, and finally locks into the lattice to become a fully commensurate CDW at the lowest temperatures. Whether some or any of these states appear in the phase diagram of any particular materials depends on their detailed material properties.

The incommensurate charge density wave (IC-CDW) exhibit a periodic charge density modulation that does not precisely match the underlying crystal lattice, in the sense that the wave vectors describing its atomic displacements are not linear combinations of the pristine lattice vectors. The incommensurate wave vectors appearing in specific CDW materials typically arise from the interplay between nesting in the electronic band structure and the momentum-dependence of electron-phonon coupling$^{21-28}$.

Upon cooling sufficiently, an IC-CDW may undergo a second transition into a commensurate charge density wave (C-CDW) phase. In this state, the CDW wave vector is a linear combination of lattice vectors. The 'lock-in' of the CDW to the atomic lattice is favoured by the Coulomb interaction between positively charged atomic cores and negatively charged electrons. Some materials also have a phase interpolating between the high-temperature IC-CDW and the low-temperatures C-CDW, characterised by an ordered arrangement of commensurate patches separated by domain walls and topological defects. Between commensurate patches, either the phase or the amplitude of the CDW can vary, or both. The patches can have a variety of shapes and sizes, which generically depend on temperature and pressure.

The initial theoretical exploration of this intermediate phase was undertaken by McMillan in the context of $2H$-TaSe$_2$, laying the groundwork for understanding its phenomenology$^{14,29,30}$. In this work, McMillan introduced a model for an effectively one-dimensional crystal structure with a single charge density wave. His investigation showed that within a specific temperature range, the formation of domain walls between commensurate patches (discommensurations) becomes favourable as a result of the balance between the contributions of the atomic lock-in energy and electron-phonon coupling. The original paper is widely cited and has been extended and applied to several materials, including higher har-

monics or a position-dependent amplitudes to model 2D discommensuration patterns³¹⁻³³. Among others, this has been used to show that the introduction of a triple charge density wave in two dimensions reduces the IC- C phase transition in $2H$-TaSe₂ from a second to first order transition³². Complementary to the extension of the CDW Ansatz in the earlier works, we here focus on the effect of the curl term in the free energy, which we consider using an exact minimization of the free energy. This adapts McMillan's original Ansatz to general materials, and in particular allows us to explore the theory in more realistic, higher-dimensional settings.

The material investigated in the original study, $2H$- TaSe₂, can be argued to be approximated by a combination of quasi-one-dimensional CDWs, because all CDW components align with high-symmetry directions in the atomic lattice. In contrast, materials like $1T$-TaSe₂ or $1T$-TaS₂ exhibit a CDW vector that is rotated with respect to the atomic lattice³⁴,³⁵, necessitating a broader two-dimensional framework. Here, we will give a detailed derivation of McMillan's original results within a consistently two-dimensional theory. We will show that this leads to novel predictions for the orientation of discommensuration lines in generic CDW materials that are not captured in the simplified one-dimensional analysis.

## II. SINGLE-Q FREE ENERGY

A Ginzburg-Landau theory for charge order can be formulated of charge density modulations $\alpha = \sum_i Re(\psi_i)$. The CDW is then described by a sum of wave-like components of the form $\psi_i = \psi_0 e^{i(\phi_i+\vec{q}_i\cdot\vec{r})}$, where the amplitude $\psi_0$ serves as the order parameter for the multi-component CDW, while $\vec{q}_i$ and $\phi_i$ describe the wave vector and phase of the $i^{\text{th}}$ component. Spatial variations of $\psi_0$ and $\phi_i$ may be used to describe the formation of various types of domain walls.

The total free energy for a single-component (single-$Q$) charge density wave in two dimensions can then be written as²⁹
$$
\begin{aligned}
F = \int d^2r \bigg[\bar{a}\alpha^2 - b\alpha^3 + \bar{c}\alpha^4 + e|\vec{Q}\cdot(\vec{\nabla}-i\vec{Q})\psi|^2 \\
+ f|\vec{Q}\times\vec{\nabla}\psi|^2\bigg].
\end{aligned}
$$
where $\vec{Q}$ is the preferred wave vector for the IC-CDW phase which is determined by the electronic nesting or, more generally, by the momentum at which the full electronic susceptibility has a maximum²²,²⁶⁻²⁸. The coupling constants $\bar{a}$, $b$, $\bar{c}$, $e$, and $f$ can be (and typically are) dependent on parameters like temperature or pressure. The terms proportional to $e$ and $f$ measure the energy cost of changing the CDW wave vector $q$ away from $\vec{Q}$. Here, $F_e$ (the term proportional to $e$) encodes the cost in energy of altering the wavelength if $q$ is aligned with $\vec{Q}$, while for fixed wavelength $F_f$ is affected by rotations of the CDW wave vector.

The coupling constants can have spatial dependence as well, as long as they respect the lattice symmetries. This can be ensured by expanding them in terms of reciprocal lattice vectors $\vec{K}_i$ as $\bar{a}(\vec{r}) = \bar{a}_0 + \bar{a}_1 \sum_i e^{i\vec{K}_i^{(1)}\cdot\vec{r}} + ...^{29}$, where $\vec{K}_i^{(1)}$ denote the shortest possible reciprocal lattice vectors, $\vec{K}_i^{(2)}$ the second shortest, and so on. A similar expansion can be done for all coupling constants.

To reproduce the results of McMillan in describing the single-$Q$ IC-CDW and C-CDW phases in the quasi-two dimensional material $2H$-TaSe₂, it suffices to include only the constant part of $\bar{a},\bar{c},e,f$, the terms up to $b_1$ in the expansion of $b$, and a constant CDW phase $\phi(r)=\phi$. All other terms either lead to higher order effects or drop out of the analysis when performing the integral in the free energy expression. Keeping only these contributions, the free energy becomes:
$$
\begin{aligned}
F = \int d^2r \bigg[\bar{a}_0\psi_0^2\cos^2(\phi+\vec{q}\cdot\vec{r}) + \bar{c}_0\psi_0^4\cos^4(\phi+\vec{q}\cdot\vec{r}) \\
+ \bigg(b_0 + 2b_1\cos\big(\vec{K}^{(1)}\cdot\vec{r}\big)\bigg)\psi_0^3\cos^3(\phi+\vec{q}\vec{r}) \\
+ e_0\psi_0^2|\vec{Q}\cdot(\vec{q}-\vec{Q})|^2 + f_0\psi_0^2|\vec{Q}\times\vec{q}|^2\bigg].
\end{aligned}
$$

The spatial integrals over odd powers of periodic functions vanish, because of their cancelling positive and negative contributions. This can be used to also evaluate the integrals over even powers of periodic function by using trigonometric addition formulae. As an explicit example, consider the $F_a$ term with the wave vector for its periodic function written as $\vec{q} = \frac{2\pi}{\lambda}(c_x,c_y,0)$. Here, we take $c_x^2+c_y^2=1$ such that $\lambda=2\pi/|q|$ is the CDW wavelength. We can then define a periodically repeated unit cell for the function $\cos^2(\phi+\vec{q}\cdot\vec{r})$ with edge lengths in the $x$ and $y$ directions equal to $\lambda/c_x$ and $\lambda/c_y$. The free energy density $\mathcal{F}_a$ for this term then becomes:
$$
\begin{aligned}
\mathcal{F}_a &= \frac{c_x c_y}{\lambda^2} \int_0^{\lambda/c_x} \int_0^{\lambda/c_y} \bar{a}_0\psi_0^2\cos^2(\phi+\vec{q}\cdot\vec{r})dxdy \\
&= \frac{c_x c_y}{\lambda^2} \int_0^{\lambda/c_x} \int_0^{\lambda/c_y} \bar{a}_0\psi_0^2\cos^2(\vec{q}\cdot\vec{r})dxdy \\
&= \frac{c_x c_y}{\lambda^2} \int_0^{\lambda/c_x} \int_0^{\lambda/c_y} \bar{a}_0\frac{\psi_0^2}{2}(1+\cos(2\vec{q}\cdot\vec{r}))dxdy \\
&= \frac{\psi_0^2\bar{a}_0}{2}.
\end{aligned}
$$

The shift introduced in the periodic function in the second line is made possible by the fact that we integrate over an entire unit cell of the periodically repeating pattern. The cosine in the third term contributes zero when integrated over due to its periodicity, and only the constant term in the third line is left.

The analysis can be repeatedly used to evaluate any of the integrals appearing in the Ginzburg-Landau theory. For the term $\mathcal{F}_c$ we use $\cos^4(z)=3/8+1/2\cos(2z)+1/8\cos(4z)$, and the only term surviving the integral is $3/8$, yielding $\mathcal{F}_c=3\bar{c}_0\psi_0^4/8$. For the elastic energy $\mathcal{F}_e$ we

have
$$
\mathcal{F}_{e}=\frac{1}{A} \int e_{0} \psi_{0}^{2}|\vec{Q} \cdot(\vec{q}-\vec{Q})|^{2} d^{2} r.
$$

Since the integrand is constant, this simply yields $\mathcal{F}_{e}=$ $e_{0} \psi_{0}^{2}[Q_{x}(q_{x}-Q_{x})+Q_{y}(q_{y}-Q_{y})]^{2}$. Similarly, the term proportional to $f$ becomes $\mathcal{F}_{f}=f_{0} \psi_{0}^{2}|\vec{Q} \times \vec{q}|^{2}$. As the $b_{0}$ term is odd, it vanishes. The $b_{1}$ term, however, can give a non-zero contribution due to the lattice vectors $K_{i}$:
$$
\begin{aligned}
\mathcal{F}_{b 1} & =-\int 2 b_{1} \psi_{0}^{3} \cos \left(\vec{K}^{(1)} \cdot \vec{r}\right) \cos ^{3}(\phi+\vec{q} \cdot \vec{r}) d^{2} r \\
& =-\frac{b_{1} \psi_{0}^{3}}{4}\left(3 \cos (\phi) \delta_{\vec{K}^{(1)}, \pm \vec{q}}+\cos (3 \phi) \delta_{\vec{K}^{(1)}, \pm 3 \vec{q}}\right).
\end{aligned}
$$

Again, the integral over all odd powers of the cosine van- ish, *except* when the argument itself is zero. This hap- pens when either $\vec{K}_{i}= \pm \vec{q}_{i}$ or $\vec{K}_{i}= \pm 3 \vec{q}_{i}$ as the cosine can be expanded using $\cos^{3}(z)=\frac{1}{4}(3\cos(z)+\cos(3z))$. This $b_{1}$ term represents the lock-in energy coming from the Coulomb interaction between the atomic lattice and the electrons in the CDW.

Combining all terms gives the free energy density:
$$
\begin{aligned}
\mathcal{F} & =\frac{\bar{a}_{0} \psi_{0}^{2}}{2}+\frac{3 \bar{c}_{0} \psi_{0}^{4}}{8} \\
& -\frac{b_{1} \psi_{0}^{3}}{4}\left(3 \cos (\phi) \delta_{\vec{K}^{(1)}, \pm \vec{q}}+\cos (3 \phi) \delta_{\vec{K}^{(1)}, \pm 3 \vec{q}}\right) \\
& +e_{0} \psi_{0}^{2}|\vec{Q} \cdot(\vec{q}-\vec{Q})|^{2}+f_{0} \psi_{0}^{2}|\vec{Q} \times \vec{q}|^{2}.
\end{aligned}
$$

The equilibrium CDW configuration will minimize the free energy with respect to the parameters $\psi_{0}$, $\vec{q}$ and $\phi$. In the $\mathcal{F}_{e}$ and $\mathcal{F}_{f}$ terms, the energy is minimized when the CDW vector $\vec{q}$ equals the preferred IC-CDW ('nesting') vector $\vec{Q}$. The $\mathcal{F}_{b}$ term however is minimized when the CDW is commensurate with the atomic lattice, so that either $\vec{q}= \pm \vec{K}^{(1)}$ or $\vec{q}= \pm \vec{K}^{(1)}/3$. There are thus two competing processes, the lock-in with the lattice coming from the $b_{1}$ term, and the nesting preference coming from the $e_{0}$ and $f_{0}$ terms. The interplay between these effects at different temperatures will determine the CDW phase diagram.

The $b_{1}$ term also determines the CDW phase $\phi$, since its contribution to the energy is minimized for $\phi=2\pi m$ when $\vec{q}=\vec{K}^{(1)}$ and for $\phi=2\pi m/3$ when $\vec{q}=\vec{K}^{(1)}/3$. In both cases, the preferred values of the phase are such that the electronic charge maxima in the CDW coincide with a lattice position. For incommensurate values of $\vec{q}$, the CDW phase does not influence the energy at all, as any shift of the CDW pattern leaves the combined CDW-lattice configuration invariant up to a redefinition of the origin.

## III. INCOMMENSURATE CHARGE DENSITY WAVE

For incommensurate charge order within a two-dimensional atomic lattice, the CDW wave vector $\vec{q}$ equals the preferred 'nesting' vector $\vec{Q}$. All of the terms $F_{e}$, $F_{b}$, and $F_{f}$ then vanish and the free energy density needs to be minimized only with respect to the order parameter amplitude:
$$
\partial_{\psi_{0}} \mathcal{F}=\psi_{0}\left(\bar{a}_{0}+\frac{3 \bar{c}_{0}}{2} \psi_{0}^{2}\right)=0.
$$

![](./images/948485827099361292_1.jpg)

FIG. 1. Incommensurate charge density wave with the wave vector of Eq. (1). The colour scale indicates the electronic charge density modulation, ranging from $-\psi_{0}$ in blue to $+\psi_{0}$ in red. As the IC-CDW does not repeat over an integer num- ber of lattice points, the peaks of the CDW do not coincide with lattice points (black dots) except for a single line (lower left corner).

Assuming that to lowest order in $T-T_{c}$ all temperature dependence is contained in the quadratic term, we can write $\bar{a}_{0}=\bar{a}^{\prime}(T-T_{c})^{13}$. This yields two regimes. The first is for $T>T_{c}$, where $\psi_{0}=0$ and there is no charge order (disordered, metallic phase). The second regime with $T<T_{c}$ has $\psi_{0}=\sqrt{\frac{-2\bar{a}_{0}}{3\bar{c}_{0}}}$ and contains the incommensurate CDW $\psi=\psi_{0}e^{i(\phi-\vec{Q}\cdot\vec{r})}$.

For the sake of concreteness, we will consider this IC- CDW phase within a two-dimensional implementation of the model for $2H$-TaSe$_{2}$ studied by McMillan$^{14}$. We thus introduce a hexagonal two-dimensional atomic lattice de- scribed by the lattice vectors:
$$
\vec{a}_{1}=a_{0}\left(\frac{\sqrt{3}}{2}, \frac{1}{2}, 0\right), \quad \vec{a}_{2}=a_{0}\left(-\frac{\sqrt{3}}{2}, \frac{1}{2}, 0\right).
$$

This gives the reciprocal lattice vectors
$$
K_{1}=\frac{2\pi}{a_{0}}(1/\sqrt{3},1,0), \quad K_{2}=\frac{2\pi}{a_{0}}(-1/\sqrt{3},1,0).
$$

The three-component IC-CDW in McMillan's model for this material is assumed to align with the three high- symmetry directions of the atomic lattice, but the length of its wave vectors, $|Q|$, is observed to be $2\%$ shorter than $|K^{(1)}/3|^{29}$. The IC-CDW wave vectors then becomes:
$$
\vec{Q}_{1}=\frac{\pi}{2.55 a_{0}}(1, \sqrt{3}, 0), \tag{1}
$$
with $\vec{Q}_{1}$, $\vec{Q}_{2}$, and $\vec{Q}_{3}$ related by three-fold rotations.

The charge modulation for the single IC-CDW com- ponent with wave vector $\vec{Q}_{1}$ is shown in Fig. 1. As the

![](./images/948485827099361292_2.jpg)

FIG. 2. C-CDW with wave vector $\vec{C} = \vec{K}^{(1)}/3$. As the C-CDW repeats over a linear combination of lattice vectors, the ridges of CDW peak intensity $+\psi_0$ (red) always coincide with rows of lattice points (black dots).

IC-CDW does not repeat over any integer number of lattice points, the peaks in electron density indicated by black diagonal lines do not coincide with lattice points (black), except for a single line in the lower left corner.

## IV. COMMENSURATE CHARGE DENSITY WAVE

As temperature decreases, the amplitude of the order parameter $\psi_0$ increases, causing an increase in the contribution to $\mathcal{F}$ of the $b_1$ term relative to that of the $e_0$ term. Since the $b_1$ and $e_0$ terms favour different values of the wave vector $\vec{q}$, there may thus be a transition of the CDW wave vector away from the 'nesting' vector $\vec{Q}$ at low temperatures. The energy cost due to the $e_0$ and $f_0$ terms encountered in a commensurate CDW is the lowest for the commensurate wave vector closest to $\vec{Q}$.

For $2H$-TaSe$_2$ the vector $\vec{C} = \vec{K}^{(1)}/3$ is the closest commensurate vector the 'nesting' vector $\vec{Q}$, with only a $2\%$ difference in wave length between the two. The charge density modulations for one of the components of this C-CDW is displayed in Fig. $2^{29}$.

Substituting the C-CDW Ansatz in the free energy, the equilibrium value of its amplitude $\psi_0$ and phase $\phi$ can again be determined by minimizing the free energy. The minimization with respect to the phase always yields the locked-in value $\phi=0$. The amplitude on the other hand is temperature dependent, and found to be zero above the critical temperature $T_{c2}=T_c-\frac{2e_0}{\bar{a}'}(\vec{Q}\cdot(\vec{q}-\vec{Q}))^2+\frac{b_1^2}{12c_0\bar{a}'}$. At the threshold there is a first order phase transition and the amplitude jumps to:
$$
\begin{aligned}
\psi_0 &= \frac{b_1}{4c_0} \\
&+ \sqrt{\left(\frac{b_1}{4c_0}\right)^2 - \frac{2}{3c_0}\left(\bar{a}'(T-T_c)+2e_0(\vec{Q}\cdot(\vec{q}-\vec{Q}))^2\right)}.
\end{aligned} \tag{2}
$$

To determine whether the IC-CDW, C-CDW, or disordered phase will be energetically favourable at any given temperature, we can compare the free energy densities of their corresponding Ansatzes. In Fig. 3, this is shown as a function of temperature for three different values of the parameter $b_1$, and (arbitrary) fixed values of the other parameters. At each temperature, the IC-CDW and C-CDW energies are shown for the value of $\psi_0$ that minimize the energy for the corresponding Ansatz. In the grey area at high temperature, it is not favourable for any CDW to form, and the phase is metallic ($T>T_c$). Going down in temperature, the second, blue area indicates the IC-CDW being the lowest energy solution. Finally, the purple region shows the C-CDW with wave vector $\vec{K}^{(1)}/3$ being favoured. Depending on the value of $b_1=0.07$ the phase transitions separating these regions shift in temperature. Notice that in this particular case, $\vec{K}^{(1)}/3$ and $\vec{Q}$ lie in the same direction such that $\mathcal{F}_f$ is zero regardless of the value of the $f_0$ parameter.

![](./images/948485827099361292_3.jpg)

FIG. 3. The energies of the IC-CDW, C-CDW, and disordered phases as a function of temperature. The blue line indicates the energy of the IC-CDW Ansatz with wave vector $\vec{Q}$. The purple line gives the energy of the C-CDW with wave vector $\vec{K}^{(1)}/3$.The grey area is the region where none of the CDW Ansatzes has an energy lower than zero, and the disordered, metallic phase is favoured. The blue area indicates the IC-CDW Ansatz having the lowest energy, and the purple area shows C-CDW being favoured. Here we used the parameter values $e_0=0.04$, $c_0=0.008$, $\bar{a}'=0.01$, and $f_0=0$.

## V. DISCOMMENSURATIONS

So far, we have reproduced and given a pedagogical account of McMillan's description of the commensurate and incommensurate CDW phases in $2H$-TaSe$_2^{29}$. As shown by McMillan however, there may also be an intervening phase between the IC-CDW and C-CDW phases, in which regions of commensurate CDW order are separated by lines of phase slips or discommensurations$^{29}$. Within the Ginzburg-Landau theory, these defect lines can be included in the CDW order parameter $\psi$ by allowing the phase $\phi$ to be position-dependent. We thus

consider the Ansatz:
$$
\psi=\psi_{0} e^{i(\phi(\vec{r})-\vec{C} \cdot \vec{r})}, \tag{3}
$$
such that for $\phi$ zero the C-CDW with wave vector $\vec{C}$ is recovered, while for $\phi=(\vec{C}+\vec{Q}) \cdot \vec{r}$ the IC-CDW is recovered. Notice that for the specific case of McMillan's model for $H$-TaSe$_2$, the preferred commensurate wave vector is again given by $\vec{C}=\vec{K}^{(1)} / 3$. Moreover, adding integer multiples of $2\pi/3$ to $\phi$ shifts the CDW pattern by an integer number of lattice distances, which does not influence the energy.

The free energy in the presence of a position dependent phase can again be considered term by term. For general $\phi(\vec{r})$, the contribution proportional to $\bar{a}_0$ becomes:
$$
F_{a}=\int \frac{\psi_{0}^{2} \bar{a}_{0}}{4}(2+\cos (2(\phi(\vec{r})+\vec{q} \cdot \vec{r}))) d^{2} r.
$$

This integral cannot be evaluated exactly without specifying $\phi(\vec{r})$. For sufficiently smoothly varying functions $\phi(\vec{r})$, however, the second term in the integrand is approximately a plane wave everywhere. The integral over it therefore approximately vanishes, and the contribution from the first, constant term dominates: $\mathcal{F}_{a} \approx \psi_{0}^{2} a_{0} / 2$. Similarly, we find for the quartic term that $\mathcal{F}_{c} \approx 3 \psi_{0}^{2} c_{0} / 8$.

For the $b$ term, we have:
$$
\begin{aligned}
F_{b}=\frac{b_{1} \psi_{0}^{3}}{4} \int &\left(\cos \left(3 \phi(r)+3 \vec{q} \cdot \vec{r}+\vec{K}^{(1)} \cdot \vec{r}\right)\right. \\
&+3 \cos \left(\phi(r)+\vec{q} \cdot \vec{r}+\vec{K}^{(1)} \cdot \vec{r}\right) ) d^{2} r.
\end{aligned}
$$

The elastic energy term $F_e$ becomes:
$$
F_{e}=\int e_{0} \psi_{0}^{2}\left(\vec{Q} \cdot\left(\vec{K}^{(1)} / 3-\vec{Q}\right)+\vec{Q} \cdot \vec{\nabla} \phi(r)\right)^{2} d^{2} r.
$$

Finally, the $F_f$ term can be written as:
$$
F_{f}=\int f_{0} \psi_{0}^{2}\left(\vec{Q} \times \vec{K}^{(1)} / 3+\vec{Q} \times \vec{\nabla} \phi(r)\right)^{2} d^{2} r.
$$

To find the function $\phi(r)$ that minimizes $F$, we need to take the two-dimensional functional derivative of the free energy equate it to zero. This can be done by first writing the free energy as:
$$
\begin{aligned}
F &=\mathrm{cst}+\int\left(-\frac{b_{1} \psi_{0}^{3}}{4} \cos (3 \phi)\right. \\
&+e_{0} \psi_{0}^{2}\left(E_{0}+\vec{Q} \cdot \vec{\nabla} \phi\right)^{2}+f_{0} \psi_{0}^{2}\left(G_{0}+\vec{Q} \times \vec{\nabla} \phi\right)^{2} ) d^{2} r.
\end{aligned}
$$

Here 'cst' is independent of $\phi$ and will therefore not contribute to the functional derivative. We also defined $E_{0}=\vec{Q} \cdot\left(\vec{K}^{(1)} / 3-\vec{Q}\right)$ and $G_{0}=\vec{Q} \times \vec{K}^{(1)} / 3$. Setting the functional derivative of $F$ with respect to $\phi$ equal to zero then yields:
$$
\begin{aligned}
& \frac{3 \psi_{0} b_{1}}{4} \sin (3 \phi) \\
&=2 e_{0}\left(Q_{x} \partial_{x}+Q_{y} \partial_{y}\right)\left(E_{0}+Q_{x} \partial_{x} \phi+Q_{y} \partial_{y} \phi\right) \\
&+2 f_{0}\left(-Q_{y} \partial_{x}+Q_{x} \partial_{y}\right)\left(G_{0}+Q_{x} \partial_{y} \phi-Q_{y} \partial_{x} \phi\right)
\end{aligned}
$$

![](./images/948485827099361292_4.jpg)

FIG. 4. A slice of the Jacobi amplitude $\phi(x,y=0)=$ $2/3\mathrm{am}(ux,m)+\pi/2$ with $u=1$ and $m=0.9999$ as a function of position $x$. The function has steps whenever $x$ equals an integer multiple of $2K=11.98$. The red dashed lines indicate integer multiples of $2\pi/3$ along the $y$-axis.

Simplifying this expression yields the differential equation:
$$
\begin{aligned}
& \frac{3 \psi_{0} b_{1}}{8} \sin (3 \phi) \\
&=e_{0}\left(Q_{x} \partial_{x}+Q_{y} \partial_{y}\right)^{2} \phi+f_{0}\left(Q_{x} \partial_{y}-Q_{y} \partial_{x}\right)^{2} \phi. \tag{4}
\end{aligned}
$$

This expression can be recognized to be the differential equation describing the motion of a simple pendulum, which is solved by the Jacobi Amplitude function:
$$
\phi(x, y)=\frac{2}{3} \operatorname{am}\left(c_{1}(x+S y)+c_{2}, m\right)+\frac{\pi}{3},
$$
$$
\text{with } m=\frac{9 \psi_{0} b_{1}}{8 c_{1}^{2}\left(e_{0}\left(Q_{x}+Q_{y} S\right)^{2}+f_{0}\left(Q_{x} S-Q_{y}\right)^{2}\right)}.
$$

The full two-dimensional function is specified by the parameters $\psi_0$, $c_1$, $c_2$, and $S$. Among these, the integration constants $c_1$ and $c_2$ can be constrained by specifying boundary conditions on $\phi(x=0,y=0)$, as well as on $\partial_x\phi(x,y)|_{x=0,y=0}$ and $\partial_y\phi(y)|_{x=0,y=0}$. As a reminder, some of the properties and special values of the Jacobi Amplitude function are:
$$
\begin{aligned}
\operatorname{am}(x, 0) &=x \\
\operatorname{am}(x+c, 1) &=\pi / 2 & \Longleftrightarrow c \gg 1 \\
\operatorname{am}(x+2 K, m) &=\operatorname{am}(x, m)+\pi
\end{aligned}
$$

Here $K=\int_{0}^{\pi / 2} d \theta / \sqrt{1-m \sin ^{2}(\theta)}$ is the quarter period.

For McMillan's model of $H$-TaSe$_2$, the C-CDW phase is represented by $\phi=2\pi n/3$ with $n\in\mathcal{Z}$. This solution can be written as a Jacobi Amplitude function in terms of the limit:
$$
c_{2} \gg 1 \quad c_{1}^{2}=\frac{9 \psi_{0} b_{1}}{8\left(e_{0} S_{1}^{2}+f_{0} S_{2}^{2}\right)}.
$$

![](./images/948485827099361292_5.jpg)

FIG. 5. Free energies as a function of temperature for the IC-CDW Ansatz (blue line), the C-CDW Ansatz (purple line) and the discommensuration Ansatz based on the Jacobi Amplitude function (red line). Here we used $S=\sqrt{3}$, $\bar{a}'=0.01$, $b_1=0.048$, $c_0=0.04$, $e_0=0.008$, and $T_c=4.5$. For each temperature, numerical optimization using the Nelder-Mead algorithm is performed to find the parameter values that minimize the energy of the Ansatz based on the Jacobi Amplitude function on a lattice of $300\times300$ sites. The inset zooms in on the lines in the red area where the discommensuration Ansatz has significantly lower energy than the IC-CDW and C-CDW.

Here $S_1=Q^x+SQ^y$ and $S_2=Q^xS-Q^y$, so that the function $\phi(x,y)$ does not depend on $S$ for the C-CDW. The IC-CDW phase can similarly be written as a Jacobi Amplitude function by choosing:

$$
S=\sqrt{3} \qquad \psi_0b_1=0,
$$

$$
c_2=-\frac{\pi}{2} \qquad c_1=\frac{1}{2}\big(3Q_x-K_x^{(1)}\big).
$$

The Jacobi Amplitude function can also be used to interpolate between the IC-CDW and C-CDW Ansatzes. For general parameter values, it has approximately constant sections smoothly connected with steps of height $2\pi/3$ occurring every $2K$ (shown in Fig. 4). This corresponds to a CDW Ansatz with commensurate patches separated by lines of phase shifts across which the CDW is moved by precisely one lattice distance in its propagation direction. These are the discommensurations that McMillan proposed for his model of $2H$-TaSe$_2^{29}$. The direction or slope of the discommensuration lines in the two-dimensional $x,y$ plane is determined by the value of the parameter $S$.

### A. The equilibrium configuration

With any specific set of values for the coupling constants in the free energy, the values for $\psi_0$ and the parameters in the Jacobi Amplitude function yielding the lowest possible free energy can be found using a numerical optimization routine. The energy of the equilibrium configuration for $S=\sqrt{3}$, $\bar{a}'=0.01$, $b_1=0.048$, $c_0=0.04$, $e_0=0.008$, and $T_c=4.5$ is shown as a function of temperature in Fig. 5 (red line). The value of $f_0$ is irrelevant as $S_2=0$ for $S=\sqrt{3}$. For each temperature, numerical optimization using the Nelder-Mead algorithm is performed to find the parameter values that minimize the energy of the Ansatz based on the Jacobi Amplitude function on a lattice of $300\times300$ sites. The energies of the IC-CDW (blue line) and C-CDW (purple line) Ansatzes are shown for comparison.

![](./images/948485827099361292_6.jpg)

FIG. 6. Slices of the phase $\phi(x,y=0)$ as a function of position for different temperatures $T$, in three different CDW phases. All $\phi$ have been vertically offset to separate the curves. The IC-CDW phase (left panel) has approximately no domain walls, and becomes a straight line aligning with the exact IC-CDW Ansatz (dashed black line) at high temperatures. Lowering the temperature, the lowest-energy Ansatz crosses over into a regime with clear finte-sized discommensurations separating domains of finite width (middle panel). The phase slip across each of the discommensurations is $2\pi/3$. At even lower temperatures, the commensurate state obtains the lowest energy and $\phi$ becomes constant (right panel). The value of $\phi=2\pi/3$ shown here is determined by the boundary conditions. The optimization is performed on a lattice of $300\times300$ sites using $S=\sqrt{3}$, $\bar{a}'=0.01$, $b_1=0.048$, $c_0=0.04$, $e_0=0.008$, and $T_c=4.5$.

Between the phases where either the IC-CDW or the C-CDW has the lowest energy, we find a region where the discommensuration Ansatz using the Jacobi Amplitude function with finite-sized domains has the overall lowest energy. The optimized functions of $\phi$ for different temperatures are displayed in Fig. 5.

The Ansatz with lowest energy is incommensurate for high temperatures and $\phi$ is approximately a straight line as visible in the left of Fig. 6. The dashed black line shows the exact IC-CDW Ansatz. The regime in the

![](./images/948485827099361292_7.jpg)

FIG. 7. Electronic charge density modulations in the discommensuration phase. Here, we used $S = \sqrt{(3)}$ for the top panel and $S = \sqrt{(3)} - 1$ for the bottom. In both panels we used $c_1 = 8$, $c_2 = 0$ and $m = 0.9999$. The colour denotes the amplitude of the charge modulations, ranging from $-\psi_0$ in blue to $\psi_0$ in red.

middle panel shows the discommensuration phase with a domains of around the same width as those found by McMillan$^{29}$. In the right panel, the lowest energy Ansatz is shown to be the C-CDW phase, in which $\phi$ is constant. Because the equilibrium configurations were determined using a numerical optimization routine, the results can vary slightly depending on the initial conditions and the search algorithm used. The qualitative behaviour shown in Fig. 6 has been verified in multiple runs and with multiple choices for the initial conditions.

The parameter $c_1$ determines the width of the domain walls and domain interiors, while the constant $c_2$ only shifts the Jacobi Amplitude function as a whole. In this Ansatz, the width of the domain wall and the domain's interior are thus co-dependent. The $c_1$ that minimizes the free energy in the discommensuration phase is determined by the coupling constants coefficients $e_0$ and $b_1$, as well as $\psi_0$. The slices visible in Fig. 6 are one-dimensional cuts through a two-dimensional structure. The fill two-dimensional pattern contain stripe-like domains, with the domain walls perpendicular to the CDW propagation vector due to the choice of $S = \sqrt{3}$, as shown for one particular choice of parameters in Fig. 7. Any parallel one-dimensional cuts taken through the two-dimensional (infinitely large) structure are equivalent, rendering the problem effectively one-dimensional.

![](./images/948485827099361292_8.jpg)

FIG. 8. Left panel: Slices of the phase $\phi(x,y=0)$ as a function of position for different temperatures $T$, in three different CDW phases. All $\phi$ have been vertically offset to separate the curves. At low temperatures, the C-CDW with constant phase is found to have the lowest energy. At high temperatures, the phase becomes a straight line matching the IC-CDW Ansatz shown as a dashed black line. At intermediate temperatures, an Ansatz with clear discommensurations is most favourable. Right panel: The orientation $S$ of the domain walls in the Ansatz with lowest energy, as a function of temperature. The horizontal dashed black line is the value $S = \sqrt{3}$ for which domain walls appear perpendicular to the CDW wave vector. Here, we used $\bar{a}' = 0.01$, $c_0 = 0.04$, $e_0 = 0.0008$, $f_0 = 0.002$, and $T_c = 4.5$.

### B. Rotation in two dimensions

To observe the full effect of the CDW being embedded in two dimensions, we can release the constraint on $S$ and minimizing the free energy for $S$ as well as the other parameters in the discommensuration Ansatz. This allows the orientation of the domain walls to vary away from being perpendicular to the CDW propagation vector. An example of a resulting discommensuration pattern is visualised in the bottom panel of Fig. 7 for $S = \sqrt{(3)} - 1$. This construction allows for generalization of McMillan's Ansatz to truly two-dimensional discommensuration configurations.

The energy of the two-dimensional discommensuration Ansatz can be minimized with respect to $S$, $c_1$, $c_2$, and $\psi_0$ on a lattice of $200 \times 200$ sites. This gives the patterns shown for different temperatures in Fig. 8 as the equilibrium configurations. The left panel displays the one-dimensional slice $\phi(x,y=0)$ for different temperatures. The right panel indicates the orientation $S$ of the domain walls as a function of temperature.

At high temperatures the lowest energy Ansatz approaches the IC-CDW solution, and the slope of the domain walls is found to be $S = \sqrt{3}$, indicating the domain walls are perpendicular to the CDW wave vector. For the low-temperature C-CDW phase, in which $\phi$ is con-

![](./images/948485827099361292_9.jpg)

FIG. 9. Electronic charge density modulations in the dis- commensuration phase. Here, we used the parameter values obtained from the energy minization at $T=0.45$, which were found to be: $S=1.65$, $c_1=8$, $c_2=-\pi/2$, and $m=0.9999$. The colour denotes the amplitude of the charge modulations, ranging from $-\psi_0$ in blue to $\psi_0$ in red.

stant and there is only a single domain, $S$ loses meaning and the temperatures in which the C-CDW Ansatz has the lowest energy are omitted from the right panel of Fig. 8. In the discommensuration phase favoured at in- termediate temperatures, the optimal value for the slope $S$ is found to vary between 1.65 and 1.8, surrounding the value $S=\sqrt{3}$. The variation of $S$ has been confirmed not to originate in numerical artefacts by establishing its stability under changing initial conditions. The two- dimensional electronic density modulations for the cofig- uration obtained when $S$ has its lowest equilibrium value of 1.65 is displayed in Fig. 9. The small absolute value of the difference between 1.65 and $\sqrt{3}\approx1.73$ imply that the difference between Figs 7 and 9 is hard to see with the naked eye within the limited field of view. Following the thinnest blue region in Fig. 9 from the top to the bottom of the figure, however, a small oscillation around the lattice sites can be distinguished.

The energy cost associated with the variation of the CDW phase across domain walls originates from the $F_e$ and $F_f$ terms in the free energy, while the energy gain of having local C-CDW structure within the domains is pro- vided by the $b_1$ term. Considering a regime in which the $b_1$ term is sufficiently dominant to favour the formation of discommensurations, a domain wall could reduce the cost of the $F_f$ term to zero by orienting itself perpendicular to the CDW wave vector. The $F_e$ term does cost energy in that case, because of the rapid variation of the phase across the domain wall, making the local wave length ap- pear shorter than its preferred value. Starting from this situation, we can keep the width of the domain wall con- stant, but rotate it slightly so as not to be perpendicular to the CDW wave vector anymore. This will cost energy from the $F_f$ term, but since it stretches the effective local wave length observed within the domain wall, it reducesthe $F_e$ cost. The reduction in the cost associated with $F_e$  generically scales linearly with the rotation angle, while the increase in $F_f$ will generically be quadratic (since it starts from an absolute minimum). We thus expect it to typically be favourable for $S$ to deviate slightly from the orientation perpendicular to the CDW wave vector, in agreement with the numerical results shown in Fig. 8.

## VI. CONCLUSION

McMillan introduced discommensurations into the the- ory of charge density waves in his seminal work on the Ginzburg-Landau model for $2H$-TaSe$_2^{29}$. This model showed that it can be favourable for a charge den- sity wave to create commensurate domains separated by discommensurations rather than switching directly from a fully incommensurate to a fully commensurate phase. The original treatment was of an effectively one- dimensional model for a two-dimensional material. Here, we gave a detailed derivation of these original results in a consistently two-dimensional setting, and went beyond them by also allowing for intrinsically two-dimensional discommensuration patterns and specifically the effect of the curl in the free energy. The orientation of domain walls in the two-dimensional configuration is governed by the competition between the lock-in effect, the preferred orientation of local charge density modulations, and their preferred local wave length. We have shown that as a result of this competition, discommensuration lines in two-dimensional CDW materials will rotate away from being perpendicular to the CDW vector. Even though the expected rotation angle will typically be small, the effect is predicted to occur generically. When the direc- tion of the incommensurate wave vector diverts further from the commensurate one, such as occurs for example in $1T$-TaSe$_2$ or $1T$-TaS$_2$, the rotation angle of domain walls may be expected to increase accordingly. The cur- rent results thus lay a basis for the consistent modelling of discommensurations in quasi-two dimensional materi- als in general, including in particular within the family of transition metal dichalcogenides.

$^{1}$ A. Silva, J. Henke, and J. van Wezel, "Elemental chalco- gens as a minimal model for combined charge and orbital order," *Physical Review B*, vol. 97, no. 4, p. 045151, 2018.

$^{2}$ Y. Kakehashi and Y. Kakehashi, "Antiferromagnetism and spin density waves," *Modern Theory of Magnetism in Met- als and Alloys*, pp. 149-180, 2013.

$^{3}$ J. Chang, E. Blackburn, A. Holmes, N. B. Christensen, J. Larsen, J. Mesot, R. Liang, D. Bonn, W. Hardy, A. Wa- tenphul, *et al.*, "Direct observation of competition be- tween superconductivity and charge density wave order in yba2cu3o6. 67," *Nature Physics*, vol. 8, no. 12, pp. 871-876, 2012.

$^{4}$ G. Ghiringhelli, M. Le Tacon, M. Minola, S. Blanco- Canosa, C. Mazzoli, N. Brookes, G. De Luca, A. Frano, D. Hawthorn, F. He, *et al.*, "Long-range incommensu- rate charge fluctuations in (y, nd) ba2cu3o6+ x," *Science*,

vol. 337, no. 6096, pp. 821–825, 2012.

5 A. Achkar, F. He, R. Sutarto, C. McMahon, M. Zwiebler, M. Hücker, G. Gu, R. Liang, D. Bonn, W. Hardy, *et al.*, "Orbital symmetry of charge-density-wave order in la1. 875ba0. 125cuo4 and yba2cu3o6. 67," *Nature Materials*, vol. 15, no. 6, pp. 616–620, 2016.

6 E. P. Rosenthal, E. F. Andrade, C. J. Arguello, R. M. Fernandes, L. Y. Xing, X. Wang, C. Jin, A. J. Millis, and A. N. Pasupathy, "Visualization of electron nematicity and unidirectional antiferroic fluctuations at high temperatures in nafeas," *Nature physics*, vol. 10, no. 3, pp. 225–232, 2014.

7 T. Shimojima, W. Malaeb, A. Nakamura, T. Kondo, K. Ki- hou, C.-H. Lee, A. Iyo, H. Eisaki, S. Ishida, M. Nakajima, *et al.*, "Antiferroic electronic structure in the nonmagnetic superconducting state of the iron-based superconductors," *Science Advances*, vol. 3, no. 8, p. e1700466, 2017.

8 M. Hervieu, A. Barnabé, C. Martin, A. Maignan, F. Damay, and B. Raveau, "Evolution of charge ordering in manganites," *The European Physical Journal B-Condensed Matter and Complex Systems*, vol. 8, no. 1, pp. 31–41, 1999.

9 I. El Baggari, B. H. Savitzky, A. S. Admasu, J. Kim, S.- W. Cheong, R. Hovden, and L. F. Kourkoutis, "Nature and evolution of incommensurate charge order in mangan- ites visualized with cryogenic scanning transmission elec- tron microscopy," *Proceedings of the National Academy of Sciences*, vol. 115, no. 7, pp. 1445–1450, 2018.

10 Y. Cao, Z. Wang, S. Y. Park, Y. Yuan, X. Liu, S. M. Nikitin, H. Akamatsu, M. Kareev, S. Middey, D. Meyers, *et al.*, "Artificial two-dimensional polar metal at room tem- perature," *Nature communications*, vol. 9, no. 1, p. 1547, 2018.

11 R. E. Peierls, *Quantum theory of solids*. Oxford University Press, 1955.

12 R. Peierls, *More surprises in theoretical physics*. Princeton University Press, 1991.

13 L. Landau, "On the theory of phase transitions ii, phys. z. soviet 545 (1937). the english translations of landau's papers can be found in "collected papers of ld landau", by d. ter haar," 1965.

14 W. McMillan, "Landau theory of charge-density waves in transition-metal dichalcogenides," *Physical Review B*, vol. 12, no. 4, p. 1187, 1975.

15 V. Ginzburg and L. Landau, "J. exptl, and theoret," *Physics (USSR)*, vol. 20, p. 1064, 1950.

16 P. C. Hohenberg and A. P. Krekhov, "An introduction to the ginzburg-landau theory of phase transitions and nonequilibrium patterns," *Physics Reports*, vol. 572, pp. 1–42, 2015.

17 Á. Pásztor, A. Scarfato, C. Barreteau, E. Giannini, and C. Renner, "Dimensional crossover of the charge density wave transition in thin exfoliated vse2," *2D Materials*, vol. 4, no. 4, p. 041005, 2017.

18 S. Manzeli, D. Ovchinnikov, D. Pasquier, O. V. Yazyev, and A. Kis, "2d transition metal dichalcogenides," *Nature Reviews Materials*, vol. 2, no. 8, pp. 1–15, 2017.

19 G. Campi, A. Bianconi, and A. Ricci, "Nanoscale phase separation of incommensurate and quasi-commensurate spin stripes in low temperature spin glass of la2- xsrxnio4," *Condensed Matter*, vol. 6, no. 4, p. 45, 2021.

20 P. Leininger, D. Chernyshov, A. Bosak, H. Berger, and D. Inosov, "Competing charge density waves and temperature-dependent nesting in 2 h-tase 2," *Physical Re- view B*, vol. 83, no. 23, p. 233101, 2011.

21 M. Johannes, I. Mazin, and C. Howells, "Fermi-surface nesting and the origin of the charge-density wave in nb se 2," *Physical Review B*, vol. 73, no. 20, p. 205102, 2006.

22 M. Johannes and I. Mazin, "Fermi surface nesting and the origin of charge density waves in metals," *Physical Review B*, vol. 77, no. 16, p. 165135, 2008.

23 X. Zhu, Y. Cao, J. Zhang, E. Plummer, and J. Guo, "Clas- sification of charge density waves based on their nature," *Proceedings of the National Academy of Sciences*, vol. 112, no. 8, pp. 2367–2371, 2015.

24 A. Bosak, S.-M. Souliou, C. Faugeras, R. Heid, M. R. Molas, R.-Y. Chen, N.-L. Wang, M. Potemski, and M. Le Tacon, "Evidence for nesting-driven charge den- sity wave instabilities in the quasi-two-dimensional ma- terial laagsb 2," *Physical Review Research*, vol. 3, no. 3, p. 033020, 2021.

25 K. Rossnagel, E. Rotenberg, H. Koh, N. Smith, and L. Kipp, "Fermi surface, charge-density-wave gap, and kinks in 2 h- tase 2," *Physical Review B*, vol. 72, no. 12, p. 121103, 2005.

26 F. Flicker and J. van Wezel, "Charge order from orbital- dependent coupling evidenced by nbse2," *Nature Com- mun.*, vol. 6, p. 7034, 2015.

27 F. Flicker and J. van Wezel, "Charge order in $\text{nbse}_2$," *Phys. Rev. B*, vol. 94, p. 235135, 2016.

28 J. Henke, F. Flicker, J. Laverock, and J. van Wezel, "Charge order from structured coupling in vse2," *SciPost Phys.*, vol. 9, p. 056, 2020.

29 W. L. McMillan, "Theory of discommensurations and the commensurate-incommensurate charge-density-wave phase transition," *Physical Review B*, vol. 14, no. 4, p. 1496, 1976.

30 W. McMillan, "Microscopic model of charge-density waves in 2 h- ta se 2," *Physical Review B*, vol. 16, no. 2, p. 643, 1977.

31 K. Nakanishi and H. Shiba, "Domain-like incommen- surate charge-density-wave states and the first-order incommensurate-commensurate transitions in layered tan- talum dichalcogenides. i. 1t-polytype," *Journal of the Physical Society of Japan*, vol. 43, no. 6, pp. 1839–1847, 1977.

32 K. Nakanishi and H. Shiba, "Domain-like incommen- surate charge-density-wave states and the first-order incommensurate-commensurate transitions in layered tan- talum dichalcogenides. ii. 2h-polytype," *Journal of the Physical Society of Japan*, vol. 44, no. 5, pp. 1465–1473, 1978.

33 P. Bak, "Commensurate phases, incommensurate phases and the devil's staircase," *Reports on Progress in Physics*, vol. 45, no. 6, p. 587, 1982.

34 X. L. Wu and C. M. Lieber, "Hexagonal domain-like charge density wave phase of tas2 determined by scanning tun- neling microscopy," *Science*, vol. 243, no. 4899, pp. 1703–1705, 1989.

35 C. Scruby, P. Williams, and G. Parry, "The role of charge density waves in structural transformations of 1t tas2," *Philosophical Magazine*, vol. 31, no. 2, pp. 255–274, 1975.
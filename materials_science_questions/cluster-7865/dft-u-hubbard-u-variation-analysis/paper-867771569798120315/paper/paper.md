# First-principles Study of Spiral Spin Density Waves in Monolayer $MnCl_{2}$ Using Generalized Bloch Theorem

Teguh Budi Prayitno $^{1,*}$, Fumiyuki Ishii $^{2}$

$^{1}$Department of Physics, Faculty of Mathematics and Natural Science, Universitas Negeri Jakarta, Kampus A Jl. Rawamangun Muka, Jakarta Timur 13220, Indonesia
$^{2}$Nanomaterials Research Institute, Kanazawa University, Kanazawa 920-1192, Japan

We investigated the spiral spin density waves in the monolayer 1T-$MnCl_{2}$ for a set of spiral vectors based on first-principles calculations. The magnetic ground states were evaluated by means of the generalized Bloch theorem within the linear combination of pseudo-atomic orbitals. To reach our purpose, a flat spiral configuration was constructed for the Mn magnetic atom by fixing the direction of its magnetic moment. We confirmed that the ground state was a spiral ground state. We also clarified that a phase transition from a spiral ground state to the other ground states, such as the ferromagnetic state or the antiferromagnetic state, appears when introducing the hole-electron doping. Therefore, we justify that introducing the hole-electron doping tunes the phase transition in the monolayer 1T-$MnCl_{2}$.

## 1. Introduction

The investigation on the magnetic properties of the transition metal dihalides $XY_{2}$, where $X$ and $Y$ denote the metal cation and the halogen anion, is of interest due to various magnetic states, a good review can be found in Ref. 1. Regarding these materials, both various ground states and multiferroic behaviors are verified by the experimental results. $^{2-4)}$ One of the great attention is addressed to the multiferroic behavior since it can be applied to the memory devices $^{5,6)}$ by incorporating the ferroelectricity and the magnetism. This property suggests that the transition metal dihalides can be considered as one of the prominent candidates for the spintronics applications.

Our concern is to consider one of the transition metal dihalides, i.e., $MnCl_{2}$, which can be crystallized in the $CdCl_{2}$ type structure with the appropriate space group $R\overline{3}m$. The important reason why we choose this material is due to the rare exploration of the magnetic order by using the density functional theory (DFT). The ground states of its bulk structure are reported to be two antiferromagnetic (AFM) transitions with the different low Néel temperatures. Those two AFM states can be analyzed by the neutron scattering, however, the verification of these states needs a large cell within the DFT. $^{7)}$ As a consequence, it is very difficult to construct the Heisenberg Hamiltonian to study the interaction of spins of atoms. On the other hand, the helimagnetic (HM) state has also been observed in the bulk structure. Based on the spin configurations, the HM order can be closely related to the spin spiral configuration. $^{8)}$ Interestingly, some authors reported that the spiral configuration in the bulk system of $MnI_{2}$ can generate the ferroelectric polarization. $^{9)}$

Beside the bulk structure, the magnetic order of the monolayer $MnCl_{2}$ is also a great interest. In contrast to the bulk structure, the monolayer $MnCl_{2}$ is reported experimentally from the bulk structure to have either the stripe order or the HM order. $^{1)}$ It seems that the magnetic order of the monolayer $MnCl_{2}$ was deduced by analyzing the magnetic orders of the bulk structure. It is interesting because the Mermin-Wagner theorem previously prohibited the magnetic order in the two-dimensional system. $^{10)}$ Later, it was confirmed that the magnetic order in the two-dimensional system can also be induced by the magnetic anisotropy. Even though the monolayer $MnCl_{2}$ only considers the single layer, the calculation based on the DFT also requires a large cell to confirm these magnetic orders. We expect the new interesting phenomena can be observed due to the magnetic order in the monolayer $MnCl_{2}$.

The main intention of this paper is to investigate the spiral (SP) ground state in the monolayer $MnCl_{2}$. Later, we also examine if the phase transition occurs when the doping is introduced. Previously, some authors reported that the phase transition can occur when increasing the hole doping. $^{11,12)}$ Since in the monolayer $MnCl_{2}$ there is only one $Mn^{2+}$ cation, for the similar case, introducing the doping can be done experimentally, such as by a sol-gel method $^{13)}$ or a hydrothermal method. $^{14)}$ The main problem to investigate the SP state is to use a large cell, similar to the HM and the stripe orders. To reduce the computational cost, we applied the generalized Bloch theorem (GBT) using the primitive unit cell containing one Mn magnetic atom and two Cl nonmagnetic atoms. Due to its limitation regarding the orientation of the magnetic moment governed by the spiral vectors, we only considered the three stable states, i.e., the ferromagnetic (FM), SP, and AFM states. We observed that the SP ground state does exist for the nondoped case, while the other stable states can be tuned by introducing the doping. Therefore, we claimed that our calculation succeeds to prove the experimental result of the HM state in the monolayer $MnCl_{2}$.

We organize the rest of the paper as follows. The computational method and the crystal structure of the monolayer $MnCl_{2}$ will be discussed in Sec. 2. We also provide a detailed explanation of how to produce the FM, SP, and AFM states by setting the spiral vectors. The stability of the SP ground state will be qualitatively discussed by comparing with the previous study. In Sec. 3, the phase transition, which includes the three stable states, will be given in terms of the doping interval for the four different lattice constants. Then, the mechanism of the phase transition will be given by using the Heisenberg model in Sec. 4. We close our discussion by summarizing our

$^{*}$teguh-budi@unj.ac.id

results in Sec. 5.

## 2. Method
We used the OPENMX code,¹⁵ a package for exploring material properties based on the DFT with the linear combination of pseudo-atomic orbitals (LCPAO)¹⁶,¹⁷ as basis sets and the norm-conserving pseudopotentials,¹⁸ to investigate the spiral spin density waves (SSDW) in the monolayer MnCl₂. In an LCPAO, the SSDW in the materials can be expressed by the rotation of the magnetic moment of the magnetic atoms as
$$
\boldsymbol{M}_{i}(\boldsymbol{r}+\boldsymbol{R}_{i})=M_{i}(\boldsymbol{r})\left(\begin{array}{c}
\cos \left(\varphi_{0}+\boldsymbol{q} \cdot \boldsymbol{R}_{i}\right) \sin \theta_{i} \\
\sin \left(\varphi_{0}+\boldsymbol{q} \cdot \boldsymbol{R}_{i}\right) \sin \theta_{i} \\
\cos \theta_{i}
\end{array}\right),\qquad(1)
$$
where $\boldsymbol{q}$ and $\boldsymbol{R}_{i}$ are the spiral vector and the lattice vector at site $i$. Here, $\theta$ is the cone angle, which must be specified from the very beginning, between the spin rotation axis and the magnetic moment. By using the expression above, the Bloch wavefunction can be written in terms of a linear combination of pseudo-atomic orbitals (PAOs) $\phi_{i\alpha}$ at site $\tau_{i}$ as¹⁹
$$
\begin{aligned}
\psi_{v \boldsymbol{k}}(\boldsymbol{r})= & \frac{1}{\sqrt{N}} \sum_{n}^{N} \sum_{i \alpha}\left[e^{i\left(\boldsymbol{k}-\frac{\boldsymbol{q}}{2}\right) \cdot \boldsymbol{R}_{n}} C_{v \boldsymbol{k}, i \alpha}^{\uparrow}\left(\begin{array}{l}
1 \\
0
\end{array}\right)\right. \\
& \left.+e^{i\left(\boldsymbol{k}+\frac{\boldsymbol{q}}{2}\right) \cdot \boldsymbol{R}_{n}} C_{v \boldsymbol{k}, i \alpha}^{\downarrow}\left(\begin{array}{l}
0 \\
1
\end{array}\right)\right] \\
& \times \phi_{i \alpha}\left(\boldsymbol{r}-\tau_{\mathrm{i}}-\boldsymbol{R}_{\mathrm{n}}\right).
\end{aligned}\qquad(2)
$$

The complete explanation of implementing the GBT in the OPENMX code can be found in Ref. 20.

The monolayer MnCl₂ crystal with the space group $R\overline{3}m$ contains one Mn atom and two Cl atoms, as shown in Fig. 1. To start the discussion, we set the experimental lattice constant of 3.686 Å from the bulk structure and the length of vacuum (z direction) of 17.47 Å,²¹ see also Ref. 22 for the comparison. Following Fig. 1, we defined the primitive lattice

![](./images/867771569798120315_1.jpg)

Fig. 1. (Color online) Crystal structure of monolayer MnCl₂ from the top view. The black parallelogram denotes the unit cell, while the purple and green balls represent Mn and Cl atoms, respectively.

vectors as
$$
\boldsymbol{a}=a \hat{e}_{x}, \quad \boldsymbol{b}=\frac{a}{2} \hat{e}_{x}+\frac{a}{2} \sqrt{3} \hat{e}_{y},\qquad(3)
$$
where $a$ is the lattice constant. Then, the appropriate primitive reciprocal lattice vectors are found to be
$$
\boldsymbol{A}=\frac{2 \pi}{a} \hat{e}_{x}-\frac{2 \pi}{a \sqrt{3}} \hat{e}_{y}, \quad \boldsymbol{B}=\frac{4 \pi}{a \sqrt{3}} \hat{e}_{y}.\qquad(4)
$$

All the self-consistent calculations were performed using a $20 \times 20 \times 1$ $k$ point mesh in a primitive unit cell with the cutoff energy of 200 Ryd and the electronic temperature of 300 K. The functional of exchange-correlation was set to the generalized gradient approximation (GGA).²³ The basis set of Mn atom is specified by Mn4.0-s3p3d3f2, which means that three valence orbitals ($s$, $p$, and $d$ orbitals) and two polarization orbitals ($f$ orbital) were used, while the cutoff radius was set to 4.0 Bohr. Meanwhile, the basis set of Cl atoms was denoted by Cl7.0-s2p2d1, meaning that two valence orbitals ($s$ and $p$ orbitals) and one polarization orbital ($d$ orbital) were used, while the cutoff radius was set to 7.0 Bohr.

To observe the SP ground state, a flat spiral configuration ($\theta=90^{\circ}$) for the Mn atom is arranged with the defined spiral vector $\boldsymbol{q}=\phi(\boldsymbol{A}+0.5\boldsymbol{B})$, where $\phi$ runs from 0 (FM state) to 1 (AFM state), as illustrated in Fig. 2. From Fig. 2, the SSDW

![](./images/867771569798120315_2.jpg)

Fig. 2. (Color online) Spin configurations of FM state with $\phi=0$ (a) and AFM state with $\phi=1$ (b).

at various $q$ will then be determined in the interval between $\phi=0$ and $\phi=1$.

## 3. Results
### 3.1 Nondoped Case
We plot the total energy difference and the appropriate magnetic moment as the function of $\phi$, as shown in Fig. 3. As immediately observed in Fig. 3, the SP ground state occurs at $\phi=0.6$ with the magnetic moment of about $4.67\ \mu_{\text{B}}$. If the reciprocal lattice vectors are transformed to the Cartesian coordinates, the position of the SP ground state is quite same compared with that of the $\gamma$-Fe (fcc phase of iron), which also has an SP ground state.²⁴⁻³¹ Therefore, we use the $\gamma$-Fe as a reference to investigate the stability of the SP ground state in the monolayer MnCl₂. For this purpose, we introduce two kinds of the FM states, i.e., the low-spin (LS-FM) and high-spin (HS-FM) ferromagnetic states. Now, we confirm that the

state with the magnetic moment larger than $4\,\mu_{\mathrm{B}}$ is an HS-FM state.

![](./images/867771569798120315_3.jpg)

Fig. 3. (Color online) Total energy difference with respect to the FM state ($\phi=0$), $\Delta E=E(\phi)-E(\phi=0)$, and its corresponding magnetic moment of the SSDW using the lattice constant of 3.686 Å. Empty squares and filled circles refer to the total energy difference and the magnetic moment.

The existence of the SSDW in the $\gamma$-Fe is considered due to a crossing point between the HS-FM state and the AFM state. This crossing point can be regarded as a consequence of the stabilization of the $\gamma$-Fe at the low temperature. Another consequence is addressed to the sensitivity of the ground state of the $\gamma$-Fe to the lattice constant. Following this fact, our first attempt to investigate the stability of the SSDW in the monolayer $\mathrm{MnCl}_{2}$ is to find a crossing point between the AFM state and, either the LS-FM state or the HS-FM state. To realize it, we graph the dependence of the total energy difference and the appropriate magnetic moment on the lattice constant for the FM and AFM states, as shown in Fig. 4. In Fig. 4, the atomic positions for all the lattice constants were optimized until the force acting on the atom is less than $0.05\,\mathrm{meV}/\mathring{\mathrm{A}}$.

From Fig. 4, we find a crossing point between the HS-FM and AFM states without observing the LS-FM state. This means that the SP ground state is sensitive to the lattice constant, similar to the $\gamma$-Fe. Furthermore, it can be seen that the AFM state becomes more stable than the HS-FM state when the lattice constant is less than $3.797\,\mathring{\mathrm{A}}$. To convince our claim, we check and find that the FM ground state appears for the lattice constant larger than $4.2\,\mathring{\mathrm{A}}$. Note that the sensitivity of the ground state to the lattice constant may possibly bring the sensitivity to the strain. Moreover, we also deduce that the optimized lattice constant is found to be 3.804 Å by fitting the data of the dependence of the total energy on the lattice constant by using the collinear FM state. The LS-FM state can only appear, in our calculation, by applying the effective Coulomb energy $U$ in the implementation of the LDA+$U$ method in the OPENMX code. $^{32)}$ Figure 5 shows the existence of the LS-FM state when applying $U>2\,\mathrm{eV}$. However, we cannot obtain, in this case, a crossing point between the FM state and the AFM state.

Here, we would like to comment on the reliable $U$ value, which was used in the previous study, i.e., $\mathrm{Mn}^{2+}$ system. By using the OPENMX code, Han et al. $^{32)}$ showed that the reliable value of $U$ lies between 4 eV and 6 eV to obtain the experimental gap of MnO system. Comparing to their result, we claim that the LS-FM state in this interval can be accepted, as shown in Fig. 5. Furthermore, since the AFM state is more stable than the FM state for the lattice constant of $3.686\,\mathring{\mathrm{A}}$, the magnetic moment of the FM state reduces faster than that of the AFM state, where their transitions have the different critical $U$ value, see Fig. 5(b).

![](./images/867771569798120315_4.jpg)

Fig. 4. (Color online) Lattice constant dependence of the total energy difference (a) and the magnetic moment (b) of the FM (diamonds) and AFM (filled circles) states. In this case, the total energy difference, $\Delta E_{FM(AFM)}=E_{FM(AFM)}(a)-E_{FM(AFM)}(a=3.797)$, is evaluated with respect to the minimum energy at the lattice constant of $3.797\,\mathring{\mathrm{A}}$.

Note that if one wants to discuss the exchange interaction in the monolayer $\mathrm{MnCl}_{2}$, it seems to follow the so-called Goodenough-Kanamori-Anderson (GKA) rules. $^{33-35)}$ The original GKA rules explore the two different kinds of the superexchange interactions, i.e., the FM and AFM superexchange interactions, based on the angle of magnetic ion-ligand-magnetic ion. These two magnetic ions are referred to the partially filled $d$ orbitals, such as Mn ion. An FM superexchange interaction works if the angle is $90^{\circ}$ while an AFM superexchange interaction takes place if the angle is $180^{\circ}$. However, it was reported that a kind of materials, such as $\mathrm{CuGeO}_{3}$, $^{36-38)}$ sometimes violates the original rules, see ref. 39. For the case of monolayer $\mathrm{MnCl}_{2}$, a kind of superexchange interactions can be analyzed by considering the angle of Mn-Cl-Mn, which is about $101^{\circ}$.

### 3.2 Doped Case

For the next discussion, we investigate the phase transition in the monolayer $\mathrm{MnCl}_{2}$ by applying the hole-electron dop-

![](./images/867771569798120315_5.jpg)

Fig. 5. (Color online) $U$-dependent total energy difference (a), $\Delta E = E(U) - E(U=0)$, and magnetic moment for several states (b) using the lattice constant of $3.686$ Å.

ing. Figure 6 shows the doping-dependent ground state for the monolayer ${\text{MnCl}}_{2}$. For simplicity, we express the concentration of the doping per cell as $d$ ($e$/cell). As shown in Fig. 6(a), the total energy difference increases for all cases (nondoped and doped cases) as the lattice constant increases. To start the discussion on the phase transition, as shown in Fig. 6(b), let's consider first the lattice constant of $3.686$ Å, as represented by the diamonds in Fig. 6. $0 \leq d \leq 0.1$ $e$/cell is the interval, at which the ground state of the system is an SP state. As the hole doping increases from 0 to $0.5$ $e$/cell, the AFM state appears in the range of $0.15$ $e$/cell $\leq d \leq 0.2$ $e$/cell while the FM state becomes the ground state in the range of $d \geq 0.25$ $e$/cell. As the electron doping increases, the AFM state appears in the range of $-0.3$ $e$/cell $\leq d \leq -0.05$ $e$/cell while the FM state becomes the ground state in the range of $d \leq -0.35$ $e$/cell.

Based on the explanation above, we expose the phase transition for the other lattice constants. We select the lattice constants of $3.501$ Å, $3.686$ Å, $3.747$ Å, and $3.825$ Å to investigate the tendency of the phase transition as well as the competition between the superexchange interaction and the double exchange interaction in the next discussion. First of all, the SP state occurs for the region close to the nondoped case for all the lattice constants. It is also shown that the FM state becomes almost stable for all the lattice constants for the electron doping less than $-0.3$ $e$/cell. The significant change occurs for the AFM state, which is very sensitive to the doping. As the lattice constant decreases at $3.501$ Å, as represented by the empty circles in Fig. 6(b), the AFM state becomes dominant for the hole doping at $d \geq 0.2$ $e$/cell and appears in the interval of $-0.35$ $e$/cell $\leq d \leq -0.1$ $e$/cell for the electron doping. Furthermore, the FM state acquires the small portion for only the electron doping in the interval of $d \leq -0.4$ $e$/cell. On the contrary, as the lattice constant increases at $3.747$ Å, represented by the filled circles in Fig. 6(b), the AFM state acquires only the small portion for the hole doping at $d = 0.15$ $e$/cell and appears in the interval of $-0.25$ $e$/cell $\leq d \leq -0.1$ $e$/cell for the electron doping. In addition, the FM state acquires the large portion for the hole doping in the interval of $d \geq 0.2$ $e$/cell and the electron doping in the interval of $d \leq -0.3$ $e$/cell. The same tendency also occurs at $3.825$ Å, represented by the triangles in Fig. 6(b), which is close to the optimized lattice constant. We observe that the AFM state appears in the interval of $-0.2$ $e$/cell $\leq d \leq -0.05$ $e$/cell for the electron doping, but no AFM state appears for the hole doping. In addition, the FM state also gains the large portion in the interval of $d \geq 0.15$ $e$/cell for the hole doping and $d \leq -0.25$ $e$/cell for the electron doping.

Based on the above results, we clarify that the transformation of the ground state of FM-AFM-SP-AFM-FM occurs when varying $d$ from $-0.5$ $e$/cell to $0.5$ $e$/cell. The existence of the phase transition in the monolayer ${\text{MnCl}}_{2}$ on the doping can be simply understood by the Heisenberg model

$$
E = E_{0} - \frac{1}{2N} \sum_{i \neq j} J_{ij} \boldsymbol{M}_{i} \cdot \boldsymbol{M}_{j} \tag{5}
$$

where $N$ corresponds to the number of unit cells. According to Ref. 40, in which the authors discussed the 1T monolayer ${\text{FeCl}}_{2}$, the exchange parameter is given by $J_{ij} = (1/12)\Delta E_{xc}/M^{2}$. Here, the multiplier $1/12$ is intended to overcome the double counting in the summation because one Mn atom is surrounded by six nearest neighbour Mn atoms. Moreover, we choose $M$ as the magnetic moment of the AFM state and $\Delta E_{xc}$ as the total energy difference between the AFM and FM states since the AFM state is more stable than the FM state for the nondoped case. The trends of the exchange parameter $J_{ij}$ as well as the magnetic moment can be seen in Figs. 6(c) and 6(d). The positive $J_{ij}$ represents the FM state while the negative one denotes either the AFM state or the SP state, as shown in Fig. 6(c). Meanwhile, Fig. 6(d) shows that increasing the doping will reduce the magnetic moment.

### 4. Discussions

By following Ref. 11, we would like to give a qualitative explanation about two different interactions, which change the ground state. As previously mentioned in Sec. 3, a superexchange interaction controls the magnetic properties of ${\text{MnCl}}_{2}$ for the nondoped case. This interaction can be considered as an indirect interaction because the interaction is mediated by ${\text{Cl}}^{-}$ ion as a nonmagnetic ion, which is located between two ${\text{Mn}}^{2+}$ ions. In this case, each ${\text{Mn}}^{2+}$ ion contains three electrons in the $t_{2g}$ state and two electrons in the $e_{g}$ state, where all the electron spins should have the same direction to obey the Hund's rule. At the same time, the on-site Coulomb repulsion will prevent two electrons having the same direction in the $e_{g}$ state for the nearest neighbour Mn atoms. So, the magnetic moments for the nearest neighbour Mn atoms should be antiferromagnetically coupled. This delocalizes the electrons over Mn-Cl-Mn, thus allowing the electron hopping from an Mn atom to the nearest neighbour Mn atom. As a consequence, the kinetic energy reduces, a loss of the kinetic energy.

For the doped case, the FM state will be created by the

![](./images/867771569798120315_6.jpg)

Fig. 6. (Color online) Phase transition in the monolayer $MnCl_{2}$ in the doping interval $d$ (e/cell) for the four lattice constants, as shown in (a) and (b). For each doping, the total energy difference (a), $\Delta E=E(a,d,\phi=$0) $-E(a,d,\phi=\phi_{lowest})$, is evaluated by subtracting the energy of the lowest state $E(\phi=\phi_{lowest})$ from the energy of FM state $E(\phi=0)$ for each $a$ and $d$. Meanwhile, $\phi$ represents the lowest state for each doping (b). Tendencies of the exchange parameter and the magnetic moment, as shown in (c) and (d). The exchange parameter (c), $J_{ij}=(1/12)[E(a,d,\phi=1)-E(a,d,\phi=0)]/M^{2}$, and the magnetic moment at $\phi=1$ in the monolayer $MnCl_{2}$ (d), in the doping range $d$ (e/cell) for the four lattice constants. The same tendencies for the other $\phi$ are also confirmed.

so-called double exchange interaction, in which the magnetic moments in the neighboring Mn atoms are ferromagnetically coupled. Consequently, this interaction will prohibit the electron hopping between the nearest neighbour Mn atoms, thus the kinetic energy remains unchanged, a gain of the kinetic energy. On the contrary, the AFM and SP states will be induced by the superexchange interaction. This means that a gain of the kinetic energy favors an FM order while a loss of the kinetic energy leads to either an AFM order or an SP order. The ground state will be then determined by the domination between the superexchange and double exchange interactions. If the superexchange interaction is more dominant than the double exchange interaction, it leads to either an AFM state or an SP state; otherwise it favors an FM state.

By using the explanations above, the superexchange interaction is more dominant than the double exchange interaction in the interval of $d\geq-0.35$ e/cell for the lattice constant of $3.501$ Å, $-0.3$ e/cell $\leq d\leq0.2$ e/cell for the lattice constant of $3.686$ Å, $-0.25$ e/cell $\leq d\leq0.15$ e/cell for the lattice constant of $3.747$ Å, and $-0.2$ e/cell $\leq d\leq0.1$ e/cell for the lattice constant of $3.825$ Å. Meanwhile, the double exchange interaction is more dominant than the superexchange interaction in the interval of $d\leq-0.4$ e/cell for the lattice constant of $3.501$ Å, $d\leq-0.35$ e/cell and $d\geq0.25$ e/cell for the lattice constant of $3.686$ Å, $d\leq-0.3$ e/cell and $d\geq0.2$ e/cell for the lattice constant of $3.747$ Å, and $d\leq-0.25$ e/cell and $d\geq0.15$ e/cell for the lattice constant of $3.825$ Å. We deduce that the domination of the double exchange interaction increases as the lattice constant increases. Therefore, it is consistent with the appearance of the FM ground state at the lattice constant larger than $4.2$ Å.

When the distance of Mn-Mn increases as the lattice constant increases, the electron will be difficult to hop between the nearest neighbour Mn atoms, thus the kinetic energy almost remains unchanged. This difficulty is influenced by the hopping integral $t$, which determines how much energy is required for an electron to hop from one site to the other site. In this case, the strength of the superexchange interaction is proportional to $t^{2}$, whereas the strength of the double exchange interaction is only proportional to $t$. Consequently, as the lattice constant increases, the strength of the superexchange interaction reduces more rapidly than that of the double exchange interaction. Therefore, this is the reason why the double exchange interaction is more dominant than the superexchange interaction at the large lattice constant.

The competition between the superexchange and the double exchange interactions also translates the critical doping. As shown in Fig. 6(c), the critical doping decreases as the lattice constant increases. At the same time, introducing the doping tends to decrease the superexchange interaction to enter the double exchange region. Therefore, the decrease of the superexchange interaction leads to the decrease of the critical doping as the lattice constant increases. Note that the trend of $J_{ij}$ does not change for the hole doping case at the lattice constant of $3.501$ Å. This lattice constant is too small compared with the optimized lattice constant, thus the superexchange interaction is much more dominant than the double exchange interaction. Furthermore, we cannot also observe a hole-electron symmetry, as shown in Fig. 6(c). This may be caused by the different orbital occupation of the hole and electron doping. When the hole doping is taken into account, it occupies the $e_{g}$ state. Contrarily, the $t_{2g}$ state will be occupied by the electron when the electron doping is introduced. Therefore, the trend of $J_{ij}$ will be different for the hole and electron doping.

## 5. Conclusions

We verify the SSDW in the monolayer $MnCl_{2}$, as predicted in the experimental result using the bulk structure, by using the GBT. For the nondoped case, the SP ground state is sensitive to the lattice constant due to a crossing point between the HS-FM state and the AFM state. We also show that the LS-FM state can only be attained by increasing the effective Coulomb energy $U$, however, no crossing point can be ob-

served. In this case, we justify that the stability of the SP state depends on the lattice constant.

By introducing the doping, the phase transition appears from the SP-AFM-FM states in general although we cannot see the FM state at the lattice constant of 3.501 Å for the hole doping. These states can be tuned in the range of doping, as shown in Figs. 6(a) and 6(b). We also justify that the appear- ance of the phase transition in the monolayer $MnCl_{2}$ is due to the competition between the superexchange and double ex- change interactions.

Acknowledgment
The computational calculations were partly carried out us- ing ISSP supercomputers at the University of Tokyo while the remaining calculations were conducted using the server com- puter at the Universitas Negeri Jakarta. This work was sup- ported by Japan Society for the Promotion of Science (JSPS) Grants-in-Aid for Scientific Research on Innovative Area, 'Nano Spin Conversion Science' (Grant Nos. 15H01015 and 17H05180). It was also supported by a JSPS Grant-in-Aid for Scientific Research on Innovative Area, 'Discrete Geometric Analysis for Material Design' (Grant No. 18H04481). It was partially supported by a JSPS Grant-in-Aid on Scientific Re- search (Grant No. 16K04875)

1) M. A. McGuire, Crystals 7, 121 (2017).
2) T. Kurumaji, S. Seki, S. Ishiwata, H. Murakawa, Y. Tokunaga, Y. Kaneko, and Y. Tokura, Phys. Rev. Lett. 106, 167206 (2011).
3) Y. Tokunaga, D. Okuyama, T. Kurumaji, T. Arima, H. Nakao, Y. Mu- rakami, Y. Taguchi, and Y. Tokura, Phys. Rev. B 84, 060406(R) (2011).
4) T. Kurumaji, S. Seki, S. Ishiwata, H. Murakawa, Y. Kaneko, and Y. Tokura, Phys. Rev. B 87, 014429 (2013).
5) N. A. Spaldin and M. Fiebig, Science 309, 391 (2005).
6) J. F. Scott, Nature Mater. 6, 256 (2007).
7) D. G. Wiesler, M. Suzuki, I. S. Suzuki, and N. Rosov, Phys. Rev. B 55,6382 (1997).
8) Ph. Kurz, F. Förster, L. Nordström, G. Bihlmayer, and S. Blügel, Phys. Rev. B 69, 024415 (2004).
9) X. Wu, Y. Cai, Q. Xie, H. Weng, H. Fan, and J. Hu, Phys. Rev. B 86,134413 (2012).

10) N. D. Mermin and H. Wagner, Phys. Rev. Lett. 17, 1133 (1966).
11) J. Inoue and S. Maekawa, Phys. Rev. Lett. 74, 3407 (1995).
12) K. Sawada and F. Ishii, J. Phys.: Condens. Matter 21, 064246 (2009).
13) J. Du, H. Chen, H. Yang, R. Sang, Y. Qian, Y. Li, G. Zhu, Y. Mao, W. He, and D. J. Kang, Microporous Mesoporous Mater. 182, 87 (2013).
14) X. Zhang, Z. Bao, X. Tao, H. Sun, W. Chen, and X. Zhou, RSC Adv. 4,64001 (2014).
15) T. Ozaki, H. Kino, J. Yu, M. J. Han, N. Kobayashi, M. Ohfuti, F. Ishii, T. Ohwaki, H. Weng, and K. Terakura, Open source package for Material eXplorer (http://www.openmx-square.org).
16) T. Ozaki and H. Kino, Phys. Rev. B 69, 195113 (2004).
17) T. Ozaki, Phys. Rev. B 67, 155108 (2003).
18) N. Troullier and J. L. Martins, Phys. Rev. B 43, 1993 (1991).
19) T. B. Prayitno and F. Ishii, J. Phys.: Condens. Matter 31, 365801 (2019).
20) T. B. Prayitno and F. Ishii, J. Phys. Soc. Jpn. 87, 114709 (2018).
21) R. W. G. Wyckoff, Crystal Structures (Interscience Publishers, New York, U.S., 1963).
22) J. D. Tornero and J. Fayos, Z. Kristallogr. 192, 147 (1990).
23) J. P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. Lett. 77, 3865(1996).
24) M. Uhl, L. M. Sandratskii, and J. Kübler, J. Magn. Magn. Mater. 103,314 (1992).
25) O. N. Mryasov, V. A. Gubanov, and A. I. Liechtenstein, Phys. Rev. B 45,12330 (1992).
26) M. Körling and J. Ergon, Phys. Rev. B 54, R8293 (1996).
27) D. M. Bylander and L. Kleinman, Phys. Rev. B 58, 9207 (1998).

28) L. M. Sandratskii, Adv. Phys. 47, 91 (1998).
29) D. M. Bylander and L. Kleinman, Phys. Rev. B 59, 6278 (1999).
30) E. Sjöstedt and L. Nordström, Phys. Rev. B 66, 014447 (2002).
31) V. M. García-Suárez, C. M. Newman, C. J. Lambert, J. M. Pruneda, and J. Ferrer, Eur. Phys. J. B 40, 371 (2004).
32) M. J. Han, T. Ozaki, and J. Yu, Phys. Rev. B 73, 045110 (2006).
33) J. B. Goodenough, J. Phys. Chem. Solids 6, 287 (1958).
34) J. Kanamori, J. Phys. Chem. Solids 10, 87 (1959).
35) P. W. Anderson, Phys. Rev. 115, 2 (1959).
36) M. Hase, I. Terasaki, Y. Sasago, and K. Uchinokura, Phys. Rev. Lett. 71,4059 (1993).
37) H. Hori, M. Furusawa, T. Takeuchi, S. Sugai, K. Kindo, and A. Yamag- ishi, J. Phys. Soc. Jpn. 63, 18 (1994).
38) G. Castilla, S. Chakravarty, and V. J. Emery, Phys. Rev. Lett. 75, 1823(1995).
39) W. Geertsma and D. Khomskii, Phys. Rev. B 54, 3011 (1996).
40) E. Torun, H. Sahin, S. K. Singh, and F. M. Peeters, Appl. Phys. Lett. 106,192404 (2015).

6
# General microscopic model of magnetoelastic coupling from first principles

X. Z. Lu, $^{1}$ Xifan Wu, $^{2}$ and H. J. Xiang $^{1,3,*}$

$^{1}$ Key Laboratory of Computational Physical Sciences (Ministry of Education), State Key Laboratory of Surface Physics, and Department of Physics, Fudan University, Shanghai 200433, People's Republic of China

$^{2}$ Department of Physics, Temple Materials Institute, and Institute for Computational Molecular Science, Temple University, Philadelphia, Pennsylvania 19122, USA

$^{3}$ Collaborative Innovation Center of Advanced Microstructures, Fudan University, Shanghai 200433, People's Republic of China

(Received 13 October 2014; revised manuscript received 10 March 2015; published 30 March 2015)

Magnetoelastic coupling, i.e., the change of crystal lattice induced by a spin order, is not only scientifically interesting, but also technically important. In this work, we propose a general microscopic model from first-principles calculations to describe the magnetoelastic coupling and provide a way to construct the microscopic model from density functional theory calculations. Based on this model, we reveal that there exists a previously unexpected contribution to the electric polarization induced by the spin order in multiferroics due to the combined effects of magnetoelastic coupling and piezoelectric effect. Interestingly and surprisingly, we find that this lattice-deformation contribution to the polarization is even larger than that from the pure electronic and ion-displacement contributions in ${\rm BiFeO_3}$. This model of magnetoelastic coupling can be generally applied to investigate the other magnetoelastic phenomena.

DOI: 10.1103/PhysRevB.91.100405
PACS number(s): 75.80.+q, 71.15.-m, 75.85.+t, 77.65.-j

Magnetoelasticity refers to the phenomenon where a change of magnetic state can induce a change in crystal volume/shape, and vice versa. The study of this phenomenon can be traced back to the 1960s [1,2]. Magnetoelastic materials play an increasingly important role in applications such as actuation, sensing, and energy harvesting [3]. The large scientific interest in magnetoelastic coupling is connected to its fundamental importance in many research areas. For example, in some negative thermal expansion (NTE) magnetic materials [4–8], the system shows an abrupt increase in crystal volume on cooling in the vicinity of the magnetic transition from the paramagnetic (PM) state to the ordered magnetic state. In some frustrated spin systems, such as spinel $A{\rm Cr_2O_4}$ ($A = {\rm Mg, Zn}$) [9–12], magnetoelastic coupling causes a change of the crystal lattice from cubic to tetragonal when they undergo an antiferromagnetic (AFM) phase transition. Furthermore, in the phenomenon of magnetostriction [3], the strain dependence of the magnetic anisotropy and/or exchange interactions can lead to a lattice change in a certain direction when a magnetic field is applied. First-principles density function theory (DFT) calculations [13–15] have been performed to understand magnetoelasticity (in particular, magnetostriction). While direct DFT calculations agree well with the macroscopic lattice response associated with various magnetic configurations, a theoretical model that elucidates the microscopic origin is desired.

For dielectric materials, the response properties can be systematically treated by electric-magnetic enthalpy as functions of ionic displacement, strain, and applied electric and magnetic fields [16,17]. In this Rapid Communication, we further develop a first-principles-based model describing magnetoelastic coupling. In this model, the relationship between the change of crystal lattice and spin order is simplified to two linear equations from which the atomic displacements and strains induced by the spin order can be obtained simultaneously, thus quantitatively describing the lattice changes. This model is general so that it can be adopted to understand the other magnetoelastic-related phenomena [including symmetric exchange, antisymmetric Dzyaloshinskii-Moriya (DM) interaction, and single-ion anisotropy (SIA)-related cases]. According to our model, we reveal that there is a contribution (i.e., lattice deformation) to the spin-order-induced electric polarization in multiferroics: The spin order induces a lattice strain, which subsequently gives rise to an additional electric polarization through the piezoelectric effect [16,18]. By combining our model with DFT calculations, we demonstrate that the lattice-deformation contribution is larger than the pure electronic and ionic contributions in ${\rm BiFeO_3}$.

In general, the total energy of a localized magnetic system can be written as $E(u_m,\eta_j,{\bf S}_i) = E_{\rm PM}(u_m,\eta_j) + E_{\rm spin}(u_m,\eta_j,{\bf S}_i)$, where $u_m$ is the atomic displacement from a reference structure, $\eta_j$ ($j = 1,\dots,6$) is the homogeneous strain in Voigt notation, and ${\bf S}_i$ refers to the spin vector. Here, $E_{\rm PM}$ is the energy of the paramagnetic (PM) state which can be expanded as [16,17]

$$
\begin{aligned}
E_{\rm PM} &= E_0 + A_m u_m + A_j \eta_j + \frac{1}{2}B_{\rm mn}u_m u_n + \frac{1}{2}B_{\rm jk}\eta_j \eta_k \\
&\quad + B_{\rm mj}u_m \eta_j + \text{terms of third and higher orders. (1)}
\end{aligned}
$$

The first-order coefficients $A_m$ and $A_j$ and the second-order coefficients $B_{mn}$, $B_{\rm jk}$, and $B_{\rm mj}$ represent force, stress, force constant, frozen-ion elastic constant, and internal-displacement tensor, respectively. By choosing a reference structure that is in equilibrium in the PM state, we will have $A_m = A_j = 0$. It should be noted that an implied-sum notation is adopted in this work. The spin-interaction energy $E_{\rm spin}$ usually contains three parts [12] ($E_{\rm spin} = E_{\rm H} + E_{\rm DM} + E_{\rm SIA}$): the Heisenberg symmetric exchange interaction $E_{\rm H}$, antisymmetric Dzyaloshinskii-Moriya (DM) interaction $E_{\rm DM}$, and single-ion anisotropy (SIA) $E_{\rm SIA}$. The Heisenberg exchange

*hxiang@fudan.edu.cn

X. Z. LU, XIFAN WU, AND H. J. XIANG

interaction $E_{\mathrm{H}}$ can be expanded as
$$
\begin{aligned}
E_{\mathrm{H}}= & E_{\mathrm{H}}^{0}+\sum_{i, i^{\prime}} \frac{\partial J_{i i^{\prime}}}{\partial u_{m}} \mathbf{S}_{i} \cdot \mathbf{S}_{i^{\prime}} u_{m}+\sum_{i, i^{\prime}} \frac{\partial J_{i i^{\prime}}}{\partial \eta_{j}} \mathbf{S}_{i} \cdot \mathbf{S}_{i^{\prime}} \eta_{j} \\
& +\sum_{i, i^{\prime}} \frac{\partial^{2} J_{i i^{\prime}}}{\partial u_{m} \partial u_{n}} \mathbf{S}_{i} \cdot \mathbf{S}_{i^{\prime}} u_{m} u_{n}+\sum_{i, i^{\prime}} \frac{\partial^{2} J_{i i^{\prime}}}{\partial \eta_{j} \partial \eta_{k}} \mathbf{S}_{i} \cdot \mathbf{S}_{i^{\prime}} \eta_{j} \eta_{k} \\
& +\sum_{i, i^{\prime}} \frac{\partial^{2} J_{i i^{\prime}}}{\partial u_{m} \partial \eta_{j}} \mathbf{S}_{i} \cdot \mathbf{S}_{i^{\prime}} u_{m} \eta_{j} \\
& + \text { terms of third and higher orders. }
\end{aligned}
$$

Here, $E_{\mathrm{H}}^{0}$ is the zero-order term with $u_{m}=0$ and $\eta_{j}=0$ [12], $J_{i i^{\prime}}$ is the symmetric exchange interaction parameter between spins $\mathbf{S}_{i}$ and $\mathbf{S}_{i^{\prime}}$, and $\frac{\partial J_{i i^{\prime}}}{\partial u_{m}}, \frac{\partial J_{i i^{\prime}}}{\partial \eta_{j}}, \frac{\partial^{2} J_{i i^{\prime}}}{\partial u_{m} \partial u_{n}}, \frac{\partial^{2} J_{i i^{\prime}}}{\partial \eta_{j} \partial \eta_{k}}$, and $\frac{\partial^{2} J_{i i^{\prime}}}{\partial u_{m} \partial \eta_{j}}$ are the derivatives of the exchange parameters. Similarly, we can derive the expressions for $E_{\mathrm{DM}}$ and $E_{\mathrm{SIA}}$.

To obtain the structural distortion and cell deformation caused by the spin order, we can minimize the total energy $E(u_{m}, \eta_{j}, \mathbf{S}_{i})$ with respect to $u_{m}$ and $\eta_{j}$. Since $\frac{\partial^{2} J_{i i^{\prime}}}{\partial u_{m} \partial u_{n}} \ll B_{\mathrm{mn}}$, $\frac{\partial^{2} J_{i i^{\prime}}}{\partial \eta_{j} \partial \eta_{k}} \ll B_{\mathrm{jk}}$, and $\frac{\partial^{2} J_{i i^{\prime}}}{\partial u_{m} \partial \eta_{j}} \ll B_{\mathrm{mj}}$, we finally obtain that
$$
\begin{aligned}
& B_{\mathrm{mn}} u_{n}+B_{\mathrm{mj}} \eta_{j}=-\sum_{i, i^{\prime}} \frac{\partial J_{i i^{\prime}}}{\partial u_{m}} \mathbf{S}_{i} \cdot \mathbf{S}_{i^{\prime}}, \\
& B_{\mathrm{mj}} u_{m}+B_{\mathrm{jk}} \eta_{k}=-\sum_{i, i^{\prime}} \frac{\partial J_{i i^{\prime}}}{\partial \eta_{j}} \mathbf{S}_{i} \cdot \mathbf{S}_{i^{\prime}}.
\end{aligned}
$$

By solving the above linear equations, we get the displacements $u_{m}$ and strains $\eta_{j}$. The spin-order-induced strain can be used to obtain the new cell vectors $\mathbf{a}^{\text {new }}$ : $[\mathbf{a}_{1}^{\text {new }}, \mathbf{a}_{2}^{\text {new }}, \mathbf{a}_{3}^{\text {new }}]=(I+\varepsilon)[\mathbf{a}_{1}^{\mathrm{PM}}, \mathbf{a}_{2}^{\mathrm{PM}}, \mathbf{a}_{3}^{\mathrm{PM}}]$, where $\mathbf{a}^{\mathrm{PM}}$ are the cell vectors of the PM state, $I$ is a $3 \times 3$ unit matrix, and $\varepsilon$ is the strain matrix defined by $\eta_{j}$.

The magnetoelastic phenomena are associated with the dependence of the crystal cell vectors on the spin configurations. Using our above model, one can quantitatively compute the lattice change, as well as reveal the microscopic origin of the interesting phenomena in great detail. In particular, one can tell which spin site, spin pair, and type of the spin interaction are responsible for the magnetoelastic coupling. This is different from previous studies [13,14] in which the final macroscopic lattice response was obtained by changing the overall magnetic configuration of the system in the DFT calculations. In principle, we can use Eq. (3) to understand the magnetoelastic phenomena such as spin-order-related NTE, magnetic phase transition-induced lattice deformation, and magnetostriction. In the following, we will show instead that the magnetoelastic coupling will give rise to a contribution to the electric polarization induced by the spin order, in which case the dimension of Eq. (3) may be greatly reduced.

Previously, it was shown [19-25] that spin-order-induced electric polarization contains a pure electronic contribution and an ion-displacement-related contribution (see Fig. 1). As we discussed above, spin order may induce not only ion displacement, but also lattice deformation. If the system in the PM state is piezoelectric (e.g., polar), we find that the lattice deformation induced by spin order may give rise to an additional electric polarization. Therefore, there is a lattice-deformation contribution (see Fig. 1) to the electric polarization due to the combined effect of spin-order-induced stress and piezoelectricity [16,18] in a magnetic material which belongs to one of the piezoelectric crystal classes in the PM state. In terms of $u_{m}$ and $\eta_{j}$, the polarization [26] can be computed as $P_{\alpha}=Z_{\alpha m} u_{m}+e_{\alpha j} \eta_{j}$, where $Z_{\alpha m}$ and $e_{\alpha j}$ are the Born effective charge and frozen-ion piezoelectric tensor, respectively. Here, both the ion-displacement and lattice-deformation contributions are included in $P_{\alpha}$. Setting $-\sum_{i, i^{\prime}} \frac{\partial J_{i i^{\prime}}}{\partial u_{m}} \mathbf{S}_{i} \cdot \mathbf{S}_{i^{\prime}}=0$ in Eq. (3), one can obtain the polarization contribution due to the stress induced by spin order. One can also evaluate this polarization contribution through the piezoelectric constant $(d_{\alpha j})$ by using $P_{\alpha}=\sum_{j} \sigma_{j} d_{\alpha j}$, where $\sigma_{j}=-\sum_{i, i^{\prime}} \frac{\partial J_{i i^{\prime}}}{\partial \eta_{j}} \mathbf{S}_{i} \cdot \mathbf{S}_{i^{\prime}}$ is the total stress due to the spin order. And $d_{\alpha j}$ can be written as $d_{\alpha j}=S_{\mathrm{jk}} e_{\alpha k}$, in which $e_{\alpha k}$ is the relaxed-ion piezoelectric tensor and $S_{\mathrm{jk}}$ is the relaxed-ion elastic compliance tensor. Previously, Wojdel and Íñiguez [17] investigated the linear magnetoelectric (ME) coupling by including the piezoelectricity and piezomagnetism in $\mathrm{BiFeO}_{3}$ and related materials. Their model can describe the overall linear ME coupling for the spin ground state. In this work, our model is generalized to include the spin-interaction energy changes under different magnetic orderings and to describe higher-order (e.g., quadratic) ME coupling. Moreover, the current model can also identify the exchange paths resulting in the particular magnetoelsatic coupling.

![](./images/814641519582511104_1.jpg)

FIG. 1. (Color online) Schematic illustration of three contributions to the electric polarization induced by a spin order in multiferroics. The pure electronic contribution [19,21,22] arises from the electron density redistribution induced by the spin order. For the ion-displacement part, it results from the ion displacements caused by the induced forces associated with a spin order [20,24]. In this work, we reveal the lattice-deformation contribution, which results from the spin-order-induced stress (i.e., the magnetoelastic coupling).

We will now discuss how to obtain the parameters in Eq. (3) within the first-principles framework. Density functional perturbation theory can be used to compute the force constant $(B_{\mathrm{mn}})$ and the internal-displacement tensor $(B_{\mathrm{mj}})$. The frozen-ion elastic constant $(B_{\mathrm{jk}})$ can be easily obtained by calculating the strain-stress relation within DFT. To compute the first-order derivatives of the symmetric spin-exchange parameter $J_{i i^{\prime}}$ with respect to $\eta_{j}$, we propose a four-states mapping approach: $\frac{\partial J_{i i^{\prime}}}{\partial \eta_{j}}=\frac{1}{4}(\frac{\partial E_{\mathrm{I}}}{\partial \eta_{j}}+\frac{\partial E_{\mathrm{IV}}}{\partial \eta_{j}}-\frac{\partial E_{\mathrm{II}}}{\partial \eta_{j}}-\frac{\partial E_{\mathrm{III}}}{\partial \eta_{j}})=$ $-\frac{1}{4}(\sigma_{j}^{I}+\sigma_{j}^{I V}-\sigma_{j}^{I I}-\sigma_{j}^{I I I})$ (see Fig. 2). Here, I-IV refer to the four spin states with different spin orientations for sites i and i' (see Fig. 2 for an example), and $E$ and $\sigma$ denote the total energy and stress, respectively. We note that the stress can be computed without doing extra DFT calculations due

![](./images/814641519582511104_2.jpg)

FIG. 2. (Color online) Schematic illustration of the four spin states in the four-states approach to calculate the derivative of exchange parameter with respect to strain $\frac{\partial J_{ii'}}{\partial \eta_{j}}$. In the four spin states, only the spins at sites i and i' change the orientation.

to the celebrated Hellmann-Feynman theorem. The first-order derivatives of the symmetric spin-exchange parameter $J_{ii'}$ with respect to $u_{m}$, can also be efficiently evaluated by using a four-states mapping approach [12].

In the following, we will apply our general model of magnetoelastic coupling to the classic room-temperature multiferroic $BiFeO_{3}$. $BiFeO_{3}$ [27-29] crystallizes in a $R3c$ structure with a large polarization ($\sim 100\ \mu C/cm^{2}$) [30] when the temperature is lower than the FE Curie temperature $T_{C}=1000$ K. On cooling below $T_{N}=650$ K, a G-type AFM order with a long period incommensurate modulation takes place. Interestingly, some experiments [31-33] discovered the ME coupling in $BiFeO_{3}$. However, how magnetoelectric coupling actually occurs on a microscopic level in multiferroic $BiFeO_{3}$ is not clear. We will investigate the microscopic origin of the ME coupling in $BiFeO_{3}$ from our model. Our total-energy calculations are based on the DFT plus the on-site repulsion ($U$) method [34] within the generalized gradient approximation [35] (DFT $+U$) on the basis of the projector augmented wave method [36] encoded in the Vienna ab initio simulation package (VASP) [37]. The plane-wave cutoff energy is set to 500 eV in the DFT calculations, unless noted otherwise. The on-site repulsion $U$ and exchange parameter $J$ are set to 5 and 1 eV for Fe. For the calculation of electric polarization, the Berry phase method [38] is used.

Our four-states approach for computing $\frac{\partial J_{ii'}}{\partial \eta_{j}}$ is compared with the a conventional finite-difference method in which the exchange interactions at different strains are computed explicitly. To compute all $\frac{\partial J_{ii'}}{\partial \eta_{j}}$ ($j=1-6$) for a given exchange interaction $J_{ii'}$, the finite-difference method requires 48 DFT total-energy calculations, while only 4 total-energy calculations are needed in the four-states approach. Thus, the four-states approach is computationally more efficient and convenient. To check the accuracy of the four-states approach, we take $BiFeO_{3}$ as an example. A $2\times 2\times 2$ supercell of a rhombohedra $R3c$ structure is adopted to compute $\frac{\partial J_{NN}}{\partial \eta_{j}}$,

<table>
<caption>TABLE I. First-order derivative of the nearest-neighbor (NN) spin-exchange parameter with respect to the strain $\eta_{j}$ ($\frac{\partial J_{NN}}{\partial \eta_{j}}$) computed by using the four-states approach. The total stress ($\sigma_{j}$) induced by the G-type AFM order in $BiFeO_{3}$ from the model and DFT calculations is presented as well.</caption>
<tbody>
<tr>
<td>$J$</td>
<td>1</td>
<td>2</td>
<td>3</td>
<td>4</td>
<td>5</td>
<td>6</td>
</tr>
<tr>
<td>$\frac{\partial J_{NN}}{\partial \eta_{j}}$ (eV)</td>
<td>$-0.086$</td>
<td>$-0.041$</td>
<td>$-0.084$</td>
<td>$0.022$</td>
<td>$0.075$</td>
<td>$-0.029$</td>
</tr>
<tr>
<td>$\sigma_{j}$ (kbar) Model</td>
<td>$-4.769$</td>
<td>$-4.769$</td>
<td>$-6.322$</td>
<td>$0$</td>
<td>$0$</td>
<td>$0$</td>
</tr>
<tr>
<td>$\sigma_{j}$ (kbar) DFT</td>
<td>$-4.420$</td>
<td>$-4.420$</td>
<td>$-5.475$</td>
<td>$0$</td>
<td>$0$</td>
<td>$0$</td>
</tr>
</tbody>
</table>

where $J_{NN}$ is the nearest-neighbor (NN) Fe-Fe spin-exchange interaction in $BiFeO_{3}$. The plane-wave cutoff energy is increased to 700 eV in order to obtain converged results for the stress. The results are presented in Table I. Our subsequent analysis shows that $\frac{\partial J_{NN}}{\partial \eta_{3}}$ plays the most important role on the magnetoelastic coupling in $BiFeO_{3}$. Therefore, we also use the finite-difference method to evaluate $\frac{\partial J_{NN}}{\partial \eta_{3}}$ in which $J_{NN}$ is calculated as a function of the strain ($\eta_{3}$) ranging from 0 to 0.006. As shown in Fig. 3(a), the plot of $J_{NN}$ versus $\eta_{3}$ is a straight line in the studied region, thus we can obtain $\frac{\partial J_{NN}}{\partial \eta_{3}}=-0.088$ eV, which is very close to that ($-0.084$ eV) obtained from our four-states approach.

Our above calculations show that $\frac{\partial J_{NN}}{\partial \eta_{3}}$ is negative, i.e., a positive strain along the $z$ axis makes $J_{NN}$ smaller. We will understand the dependence of $J_{NN}$ on $\eta_{3}$ on the basis of the superexchange theory. As shown in Fig. 3(b), when $\eta_{3}$ is positive, the Fe1-O-Fe2 angle ($\theta$) will become closer to $180^{\circ}$ and the Fe1-O and Fe2-O bond lengths will be elongated. According to the Goodenough-Kanamori rule, the superexchange interaction $J$ is proportional to $\frac{t^{2}}{U}$ [39,40].

![](./images/814641519582511104_3.jpg)

FIG. 3. (Color online) (a) The NN symmetric spin-exchange interaction $J_{NN}$ as a function of $\eta_{3}$. The obtained $\frac{\partial J_{NN}}{\partial \eta_{3}}$ from the finite-difference method is in good agreement with that ($\frac{\partial J_{NN}}{\partial \eta_{3}}=-0.084$ eV) from the four-states approach. (b) Illustrations of the changes of bond lengths ($|{\bf l}_{1}|,|{\bf l}_{2}|$) and angle ($\theta$) with strain ($\eta_{3}$) in a Fe1-O-Fe2 system related to $J_{NN}$. Green arrows indicate the directions of ${\bf l}_{1}$ and ${\bf l}_{2}$.

where $t$ and $U$ are the effective orbital hopping and Hubbard repulsion, respectively. A larger angle makes the hopping stronger, while the longer bond length weakens the hopping. Therefore, this qualitative analysis is not able to determine how $J_{\text{NN}}$ will change. Quantitatively speaking, the effective hopping between the $3d$ orbitals of Fe1 and Fe2 can be approximately expressed as $t = t_1^{\text{pdo}\sigma} t_2^{\text{pdo}\sigma} \cos\theta$, where $t_i^{\text{pdo}\sigma}$ is the hopping integral between the $e_g$ orbital of the $i$th Fe ion and the $2p$ orbital of the intermediate O ion. Because $t_i^{\text{pdo}\sigma}$ is proportional to $\frac{1}{|\mathbf{l}_i|^4}$ [the distance vector $\mathbf{l}_i$ is defined in Fig. 3(b)] [41], we find $t \sim \frac{\cos\theta}{|\mathbf{l}_1|^4|\mathbf{l}_2|^4}$. Expanding $|\mathbf{l}_i|$ and $\cos\theta$ as a function of $\eta_3$, we obtain $t \sim \frac{\mathbf{l}_{10} \cdot \mathbf{l}_{20} + \alpha \eta_3}{|\mathbf{l}_{10}|^5|\mathbf{l}_{20}|^5}$, where $\mathbf{l}_{i0}$ is the original distance vector with $\eta_3=0$, and $\alpha = 2|\mathbf{l}_{10}^z||\mathbf{l}_{20}^z| - 5\mathbf{l}_{10} \cdot \mathbf{l}_{20}[\frac{|\mathbf{l}_{10}^z|^2}{|\mathbf{l}_{10}|^2} + \frac{|\mathbf{l}_{20}^z|^2}{|\mathbf{l}_{20}|^2}]$. One can easily see [42] that $\alpha < 0$, thus $t$ becomes smaller for a positive $\eta_3$ and $\frac{\partial J_{\text{NN}}}{\partial \eta_3} < 0$, consistent with the DFT result. Similarly, we can demonstrate that $\frac{\partial J_{\text{NN}}}{\partial \eta_1} < 0$ and $\frac{\partial J_{\text{NN}}}{\partial \eta_2} < 0$.

From our model, we can compute the total stress resulting from the ordering of the G-type AFM order by using $\sigma_{\text{AFM}} = -\sum_{<i,i'>_{\text{NN}}} \frac{\partial J_{i'}}{\partial \eta_j} \mathbf{S}_i \cdot \mathbf{S}_{i'}$, where only the NN Fe-Fe pairs are considered. This stress can be compared to the direct DFT value from a DFT calculation on BiFeO$_3$ in the G-AFM spin state with the equilibrium structure of the PM state (simulated by two orthogonal spins in the 10-atom rhombohedra cell). Table I indicates a good agreement between the model and the direct DFT calculation. This also suggests that $\frac{\partial J_{\text{NN}}}{\partial \eta_j}$ is sufficient for describing the magnetoelastic coupling in BiFeO$_3$.

We now turn to examine how the magnetoelastic coupling influences the electric polarization in BiFeO$_3$. By solving Eq. (3), we find that the strain is $\eta = (-8.26, -8.26, -35.58, 0, 0, 0)$ in the order of $10^{-4}$ as a result of the G-AFM ordering. Mediated by the coupling between polarization and strain, the lattice change will induce a polarization. As can be seen in Table II, our model predicts a lattice-deformation contribution to the polarization of $P = 1.32\ \mu\text{C}/\text{cm}^2$, which is even larger than the sum of the pure electronic and ion-displacement contributions. This is an unprecedented result in that a previously unknown contribution to electric polarization induced by spin order is found to be even larger than the widely known contributions. Table II shows that the result obtained from our model is also in agreement with the direct DFT calculations. Summing up all three spin-order-induced contributions with the same sign, the total polarization calculated for the G-type AFM order in BFO reaches $\sim 2\ \mu\text{C}/\text{cm}^2$. The spin-induced polarization in BFO is also comparable with that of HoMnO$_3$ [24,43]. We find that the direction of the polarization caused by the spin order is opposite to the inherent electric polarization due to the $R3c$ structure distortion. This is consistent with a recent experimental observation [31]. In that experiment [31], the ion-displacement contribution deduced from the displacement of the Fe ions was determined to be $0.4\ \mu\text{C}/\text{cm}^2$, which is also close to the value $(0.56\ \mu\text{C}/\text{cm}^2)$ obtained from our model.

Some experiments [32,33] suggested that an external magnetic field may change the electric polarization of BiFeO$_3$. Qualitatively, we can understand the ME coupling in BiFeO$_3$ from our model. Considering only the NN spin-exchange interaction and Zeeman term, the total energy can be written as $E = \sum_{<i,i'>_{\text{NN}}} J_{\text{NN}} \mathbf{S}_i \cdot \mathbf{S}_{i'} - \mu_B g \sum_i \mathbf{S}_i \cdot \mathbf{H}$, where $\mu_B$, $g$, and $\mathbf{H}$ are Bohr magneton, Landé factor, and magnetic field, respectively. By minimizing the total energy, the angle $\theta$ between the two spins $\mathbf{S}_1$ and $\mathbf{S}_2$ in the 10-atom cell in a magnetic field is $\theta = 2\mathrm{arc}\cos(\frac{5\mu_B H}{12 J_{\text{NN}}})$ (the effective $J_{\text{NN}} = 35.76$ meV in our study). As can be seen from Eq. (3), the spin-order-induced polarization $P \propto \langle \mathbf{S}_i \cdot \mathbf{S}_{i'} \rangle \propto \cos\theta$. It can be easily shown that $\Delta P = P(H) - P(0) \propto H^2$. Therefore, we obtain a quadratic dependence of this spin-order-induced polarization on the magnetic field, i.e., the quadratic ME coupling (see Fig. 4). At a magnetic field of 20 T, we find that $\Delta P = 9 \times 10^{-4}\ \mu\text{C}/\text{cm}^2$, which is in agreement with the result from one experiment [32], but there is a large discrepancy between our result and another experimental result [33]. Note that our above analysis is based on a simplified spin Hamiltonian without DM interactions and single-ion anisotropy. Further experimental and theoretical studies are called for to resolve this discrepancy.

In summary, we propose a microscopic model that describes magnetoelastic coupling. All of the parameters in this model can be computed from first principles. In particular, we propose an efficient four-states approach for computing the derivate of the spin-interaction parameter with respect to the strain. On the basis of this model, we reveal that there exists a previously unexpected contribution to the electric polarization induced by the spin order in multiferroics due to the combined effect of magnetoelastic coupling and piezoelectric effect. Interestingly, we find that this lattice-deformation contribution to the polarization is even larger than that from the pure

TABLE II. The different contributions to the electric polarization (in units of $\mu\text{C}/\text{cm}^2$) induced by the G-AFM order in BiFeO$_3$ from the model and DFT calculations. $P_{\text{lattice}}$, $P_e$, and $P_{\text{ion}}$ refer to the lattice deformation, pure electronic and ion-displacement contributions, respectively.

<table>
  <thead>
    <tr>
      <th>Polarization</th>
      <th>$P_{\text{lattice}}$</th>
      <th>$P_e$</th>
      <th>$P_{\text{ion}}$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Model</td>
      <td>1.32</td>
      <td>0.53</td>
      <td>0.56</td>
    </tr>
    <tr>
      <td>DFT</td>
      <td>1.22</td>
      <td>0.40</td>
      <td>0.54</td>
    </tr>
  </tbody>
</table>

![](./images/814641519582511104_4.jpg)

FIG. 4. (Color online) Polarization ($P$) vs magnetic field ($H$) calculated from our simple theoretical model. $\Delta P$ is defined as $\Delta P = P(H) - P(0)$. Experimental results (Expt. 1 [32] and Expt. 2 [33]) are also shown for comparison.

electronic and ionic contributions in $BiFeO_3$. The spin-order-induced polarization is opposite to the proper polarization due to the $R3c$ distortion, in agreement with the negative ME effect observed experimentally [31]. Furthermore, how an external magnetic field modulates the electronic polarization in $BiFeO_3$ is discussed qualitatively by using the general model. Our microscopic model of magnetoelastic coupling will be useful to investigate the linear and higher-order ME effects and the origin of magnetoelastic phenomena.

X.W. was supported as part of the Center for the Computational Design of Functional Layered Materials, an Energy Frontier Research Center funded by the US Department of Energy, Office of Science, Basic Energy Sciences under Award No. DE-SC0012575. Work at Fudan was supported by NSFC, the Special Funds for Major State Basic Research, Grant No. NCET-10-0351, Research Program of Shanghai Municipality and MOE, Program for Professor of Special Appointment (Eastern Scholar), and Fok Yung Tung Education Foundation.

[1] L. D. Landau and E. M. Lifshitz, *Electrodynamics of Continuous Media* (Pergamon, Oxford, 1984).

[2] W. F. Brown Jr., J. Appl. Phys. 36, 994 (1965).

[3] J. Atulasimha and A. B Flatau, Smart Mater. Struct. 20, 043001 (2011).

[4] K. Takenaka and H. Takagi, Appl. Phys. Lett. 87, 261902 (2005).

[5] K. Takenaka, K. Asano, M. Misawa, and H. Takagi, Appl. Phys. Lett. 92, 011927 (2008).

[6] S. Iikubo, K. Kodama, K. Takenaka, H. Takagi, and S. Shamoto, Phys. Rev. B 77, 020409(R) (2008).

[7] J. Matsuno, K. Takenaka, H. Takagi, D. Matsumura, Y. Nishihata, and J. Mizuki, Appl. Phys. Lett. 94, 181904 (2009).

[8] K. Takenaka, Sci. Technol. Adv. Mater. 13, 013001 (2012).

[9] S.-H. Lee, C. Broholm, T. H. Kim, W. Ratcliff, and S.-W. Cheong, Phys. Rev. Lett. 84, 3718 (2000).

[10] S.-H. Lee, G. Gasparovic, C. Broholm, M. Matsuda, J.-H. Chung, Y. J. Kim, H. Ueda, G. Xu, P. Zschack, K. Kakurai, H. Takagi, W. Ratcliff, T. H. Kim, and S.-W. Cheong, J. Phys.: Condens. Matter 19, 145259 (2007).

[11] L. Ortega-San-Martın, A. J. Williams, C. D. Gordon, S. Klemme, and J. P. Attfield, J. Phys.: Condens. Matter 20, 104238 (2008).

[12] H. J. Xiang, E. J. Kan, S.-H. Wei, M.-H. Whangbo, and X. G. Gong, Phys. Rev. B 84, 224429 (2011); H. Xiang, C. Lee, H.-J. Koo, X. Gong, and M.-H. Whangbo, Dalton Trans. 42, 823 (2013).

[13] R. Wu, L. Chen, and A. J. Freeman, J. Magn. Magn. Mater. 170, 103 (1997).

[14] D. Fritsch and C. Ederer, Phys. Rev. B 86, 014406 (2012).

[15] I. Turek, J. Rusz, and M. Diviš, J. Alloys Compd. 431, 37 (2007).

[16] X. Wu, D. Vanderbilt, and D. R. Hamann, Phys. Rev. B 72, 035105 (2005).

[17] J. C. Wojdel and J. Íñiguez, Phys. Rev. Lett. 103, 267205 (2009).

[18] C. W. Swartz and X. Wu, Phys. Rev. B 85, 054102 (2012).

[19] H. Katsura, N. Nagaosa, and A. V. Balatsky, Phys. Rev. Lett. 95, 057205 (2005).

[20] I. A. Sergienko and E. Dagotto, Phys. Rev. B 73, 094434 (2006).

[21] H. J. Xiang, E. J. Kan, Y. Zhang, M.-H. Whangbo, and X. G. Gong, Phys. Rev. Lett. 107, 157202 (2011).

[22] X. Z. Lu, M.-H. Whangbo, Shuai Dong, X. G. Gong, and H. J. Xiang, Phys. Rev. Lett. 108, 187204 (2012).

[23] Z.-L. Li, M.-H. Whangbo, X. G. Gong, and H. J. Xiang, Phys. Rev. B 86, 174401 (2012).

[24] H. J. Xiang, P. S. Wang, M.-H. Whangbo, and X. G. Gong, Phys. Rev. B 88, 054404 (2013).

[25] H. Wang, I. V. Solovyev, W. Wang, X. Wang, P. J. Ryan, D. J. Keavney, J.-W. Kim, T. Z. Ward, L. Zhu, J. Shen, X. M. Cheng, L. He, X. Xu, and X. Wu, Phys. Rev. B 90, 014436 (2014).

[26] Note that for the purpose of calculating the polarization, it is not necessary to know all the ion displacements since only the (in fact, optical) phonon modes at $\Gamma$ (i.e., the average ion displacements within the primitive chemical unit cell) contribute to nonzero polarization. This procedure is advantageous because it involves only linear equations with much smaller dimensions and we need only the force constants $(B_{mn})$ of the chemical unit cell that can be readily calculated.

[27] J. R. Teague, R. Gerson, and W. James, Solid State Commun. 8, 1073 (1970).

[28] I. Sosnowska, T. P. Neumaier, and E. Steichele, J. Phys. C 15, 4835 (1982).

[29] R. D. Johnson, P. Barone, A. Bombardi, R. J. Bean, S. Picozzi, P. G. Radaelli, Y. S. Oh, S.-W. Cheong, and L. C. Chapon, Phys. Rev. Lett. 110, 217206 (2013).

[30] J. Wang, J. B. Neaton, H. Zheng, V. Nagarajan, S. B. Ogale, B. Liu, D. Viehland, V. Vaithyanathan, D. G. Schlom, U. V. Waghmare, N. A. Spaldin, K. M. Rabe, M. Wuttig, and R. Ramesh, Science 299, 1719 (2003).

[31] S. Lee, M. T. Fernandez-Diaz, H. Kimura, Y. Noda, D. T. Adroja, Seongsu Lee, Junghwan Park, V. Kiryukhin, S.-W. Cheong, M. Mostovoy, and Je-Geun Park, Phys. Rev. B 88, 060103(R) (2013).

[32] A. M. Kadomtseva, A. K. Zvezdin, Yu. F. Popov, A. P. Pyatakov, and G. P. Vorob'ev, JETP Lett. 79, 571 (2004).

[33] J. Park, S.-H. Lee, S. Lee, F. Gozzo, H. Kimura, Y. Noda, Y. J. Choi, V. Kiryukhin, S.-W. Cheong, Y. Jo, E. S. Choi, L. Balicas, G. S. Jeon, and J.-G. Park, J. Phys. Soc. Jpn. 80, 114714 (2011).

[34] A. I. Liechtenstein, V. I. Anisimov, and J. Zaanen, Phys. Rev. B 52, R5467(R) (1995).

[35] J. P. Perdew, K. Burke, and M. Ernzerhot, Phys. Rev. Lett. 77, 3865 (1996).

[36] P. E. Blöchl, Phys. Rev. B 50, 17953 (1994); G. Kresse and D. Joubert, ibid. 59, 1758 (1999).

[37] G. Kresse and J. Furthmüller, Comput. Mater. Sci. 6, 15 (1996); Phys. Rev. B 54, 11169 (1996).

[38] R. D. King-Smith and D. Vanderbilt, Phys. Rev. B 47, 1651 (1993); R. Resta, Rev. Mod. Phys. 66, 899 (1994).

[39] J. Kanamori, J. Phys. Chem. Solids 10, 87 (1959).

[40] J. B. Goodenough, *Magnetism and the Chemical Bond* (Interscience, New York, 1963).

[41] W. A. Harrison, *Elementary Electronic Structure* (World Scientific, Singapore, 2004).

[42] Considering $|\mathbf{l}_1| \approx |\mathbf{l}_2|$, $\alpha$ can be simplified to the form of $2|l_{10}^{\epsilon}||l_{20}^{\epsilon}| + 5(|l_{10}^{\epsilon}|^2 + |l_{20}^{\epsilon}|^2) \cos \theta$ where $\theta = 153^\circ$. Because $2|l_{10}^{\epsilon}||l_{20}^{\epsilon}| \leqslant |l_{10}^{\epsilon}|^2 + |l_{20}^{\epsilon}|^2$, $\alpha$ should be a negative value.

[43] S. Picozzi, K. Yamauchi, B. Sanyal, I. A. Sergienko, and E. Dagotto, Phys. Rev. Lett. 99, 227201 (2007).
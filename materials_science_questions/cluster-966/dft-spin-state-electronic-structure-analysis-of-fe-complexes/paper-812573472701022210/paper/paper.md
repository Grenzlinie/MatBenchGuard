# Spin-inversion mechanisms in $O_2$ binding to a model heme compound: A perspective from nonadiabatic wave packet calculations

Kohei Saito¹ | Yuya Watabe¹ | Takaaki Miyazaki¹ | Toshiyuki Takayanagi¹ | Jun-ya Hasegawa²

¹Department of Chemistry, Saitama University, Saitama City, Saitama, Japan
²Institute for Catalysis, Hokkaido University, Sapporo, Hokkaido, Japan

Correspondence
Toshiyuki Takayanagi, Department of Chemistry, Saitama University, 255 Shimo-Okubo, Sakura-ku, Saitama City, Saitama 338-8570, Japan.
Email: tako@mail.saitama-u.ac.jp

Funding information
Grant-in-Aid for Scientific Research from the Ministry of Education, Culture, Sports, Science and Technology of Japan, Grant/Award Number: 17KT0093

## Abstract
Spin-inversion dynamics in $O_2$ binding to a model heme complex, which consisted of Fe(II)-porphyrin and imidazole, were studied using nonadiabatic wave packet dynamics calculations. We considered three active nuclear degrees of freedom in the dynamics, including the motions along the Fe-O distance, Fe-O-O angle, and Fe out-of-plane distance. Spin-free potential energy surfaces for the singlet, triplet, quintet, and septet states were developed using density functional theory calculations, and spin-orbit coupling elements were obtained from CASSCF-level electronic structure calculations. The spin-inversion mainly occurred between the singlet state and one of the triplet states due to large spin-orbit couplings and the contributions of other states were extremely small. The present quantum dynamics calculations suggested that the narrow crossing region model plays a dominant role in the $O_2$ binding dynamics. In addition, the one-dimensional Landau-Zener model underestimated the nonadiabatic transition probability.

## 1 | INTRODUCTION
Binding of molecular oxygen to the Fe(II)-porphyrin center in heme protein is a biologically important reaction. $^{[1-3]}$ One interesting aspect of this reaction is the change in spin during the oxygen binding process. $O_2$ has a triplet state with two unpaired electrons ($S = 1$, where $S$ is the spin quantum number), whereas the ground state of deoxyheme is a quintet state with four unpaired spins ($S = 2$). This produces multiple states, namely, triplet, quintet, and septet ($S = 3$), when $O_2$ interacts with deoxyheme. $^{[2]}$ In contrast, previous electron paramagnetic resonance and Mössbauer experiments have shown that the oxyheme product has a singlet ground state. $^{[4,5]}$ Thus, the $O_2$ binding reaction to heme is formally spin-forbidden. A total of four spin-multiplicity states can contribute to the binding process and at least triplet to singlet state transitions should occur to form the stable singlet oxyheme product from $^3O_2 + ^5$deoxyhem. The spin-multiplicity change has also been called spin-inversion, spin flip, spin crossover, or intersystem crossing in chemistry. $^{[6-8]}$ In addition, the chemical reaction phenomenon accompanying spin-multiplicity change is called "two-state reactivity" or "multi-state reactivity." $^{[9-11]}$ These spin transitions are induced by relativistic spin-orbit coupling (SOC) between different spin-multiplicity states, which is generally large for heavy elements. Thus, the SOC of Fe(II) is expected to play an essential role in $O_2$ binding to heme. Hereafter, we use the term "spin-inversion" to describe the spin transition.

To understand the detailed spin-inversion mechanisms in $O_2$ binding to heme, it is crucial to characterize the features of the potential energy surfaces for all the relevant spin-multiplicity states. Extensive electronic structure studies using ab initio molecular orbital wavefunction theory and density functional theory (DFT) have been performed so far in simplified heme models. $^{[12-36]}$ A typical example is a Fe(II)-porphyrin complex with a proximal imidazole or a related ligand. These theoretical studies mainly focused on the energetics of equilibrium structures, $O_2$ binding energies, and potential energy surface features as a function of the $Fe-O_2$ approach distance. From the calculated interaction potentials between the Fe(II)-porphyrin complex

and $O_2$, broad and narrow crossing region mechanisms have been proposed as spin-inversion mechanisms. $^{[3,27]}$ In the broad crossing region mechanism, spin-inversion is assumed to occur mainly at longer $Fe-O_2$ distances, for which the corresponding potential energy surfaces with different spin multiplicities of the $O_2$-heme system are nearly degenerate. The narrow crossing region mechanism, on the other hand, assumes that specific crossing points, which should mainly occur at shorter $Fe-O_2$ distances, play an essential role in the overall spin-inversion processes. Although previous theoretical studies have provided important insights into the possible spin-inversion mechanism in $O_2$ binding to heme, $^{[12-36]}$ no systematic calculation to find crossing point structures between the different spin-multiplicity states has been performed.

Recently, the mixed-spin Hamiltonian method, $^{[37,38]}$ where two potential energy surfaces with different spin multiplicities are mixed through a coupling parameter, has been employed to locate approximate spin-inversion structures between the two potential energy surfaces of the model $O_2$-heme complex. $^{[39]}$ In this method, the approximate minimum energy crossing point structure, which is important for discussing the efficiency of the spin-inversion process, can be easily optimized as a transition state on the low-lying spin-coupled potential energy surface. A total of nine spin-inversion structures were successfully optimized for the singlet-triplet, singlet-quintet, triplet-quintet, and quintet-septet spin-inversion processes. The singlet-triplet spin-inversion points occur around a short $Fe-O_2$ distance region, whereas the other singlet-quintet, triplet-quintet, and quintet-septet spin-inversion points are located at longer $Fe-O_2$ distances. $^{[39]}$ This suggests that both narrow and broad crossing mechanisms may play important roles depending on the initial spin-multiplicity state. The mixed-spin Hamiltonian method enables the calculation of the intrinsic reaction coordinate (IRC) for the spin-inversion pathway, as in the case of a single electronically adiabatic reaction. The IRC calculation showed that nuclear motions along the $Fe-O-O$ angle and Fe out-of-plane distance (deviation of Fe from the porphyrin plane) are important along the spin-inversion IRC pathways. $^{[39]}$

In this work, we perform nonadiabatic quantum wave packet dynamics calculations to understand the spin-inversion mechanisms in $O_2$ binding to a model heme compound further from a dynamical perspective. Extensive theoretical studies have been performed; however, most of the studies obtained static information about the features of the potential energy surfaces and their crossings. $^{[12-36,39]}$ Spin, nonadiabatic, and vibrational dynamics cannot be described independently due to strong SOCs in many molecular systems containing heavy elements. $^{[40-47]}$ The magnitudes of the SOCs of Fe(II) ($100$-$300\ \mathrm{cm}^{-1}$) are roughly comparable to those of many low-frequency vibrational modes of the oxyheme complex. Here, we use a reduced-dimensionality model, in which only a few nuclear degrees of freedom of the target chemical system are considered in the quantum nonadiabatic wave packet calculations. For multiple potential energy surfaces, we consider 16 low-lying spin states correlating with the singlet, triplet, quintet, and septet states.

## 2 | COMPUTATIONAL METHOD

Our simplified heme model consists of a Fe(II)-porphyrin complex ($\mathrm{FeC_{20}N_{4}H_{12}}$) with a proximal imidazole ($\mathrm{C_{3}N_{2}H_{4}}$), which we refer to as FePorIm below. We use the active coordinates $R$, $\theta$, and $d$ to describe the $O_2$ binding dynamics to this heme model. The definition of these coordinates is shown in Figure 1. The center of mass of the porphyrin moiety is defined as the coordinate origin in this study and $R$ is the distance between the $O_a$ atom of $O_2$ and the coordinate origin. $\theta$ is the $\mathrm{Fe-O_a-O_b}$ bending angle and $d$ is the deviation distance of Fe atom from the porphyrin plane. The Fe atom, the center of mass of the PorIm moiety, and the $O_a$ atom are always arranged in collinear configurations in the present calculations. The coordinates $R$, $\theta$, and $d$ are taken from our previous study on the IRC calculations for the spin-inversion pathways. $^{[39]}$ In particular, we found that the nuclear motion along $\theta$ was important for the singlet-triplet spin-inversion because the optimized $\mathrm{Fe-O_a-O_b}$ angles for the singlet and triplet minimum structures were somewhat different ($121^\circ$ and $133^\circ$, respectively). Similarly, we found that the motion along $d$ was an important role in the quintet-septet and quintet-singlet spin-inversion processes. $^{[39]}$ The Hamiltonian of the three degrees of freedom model employed in this work is written (in atomic units) as

$$
\mathcal{H}(R,\theta,d)=-\frac{1}{2\mu_R}\frac{\partial^2}{\partial R^2}-\frac{1}{m_O r^2}\frac{\partial^2}{\partial \theta^2}-\frac{1}{2\mu_d}\frac{\partial^2}{\partial d^2}+\boldsymbol{V}(R,\theta,d),\quad(1)
$$

where $\boldsymbol{V}$ is the potential energy matrix described by the spin-diabatic representation. $\mu_R$ and $\mu_d$ are the reduced masses of the motions along the $R$ and $d$ coordinates, respectively. $r$ is the $\mathrm{O_a-O_b}$ distance, which is taken to be a constant value ($r=1.24\ \mathring{A}$) throughout this study. The potential energy matrix can be formally written as

$$
\boldsymbol{V}(Q)=\begin{pmatrix}
V_0(Q) & V_{01}(Q) & 0 & 0 \\
V_{01}^\dagger(Q) & V_1(Q) & V_{12}(Q) & 0 \\
0 & V_{12}^\dagger(Q) & V_2(Q) & V_{23}(Q) \\
0 & 0 & V_{23}^\dagger(Q) & V_3(Q)
\end{pmatrix},\quad(2)
$$

where $Q$ collectively denotes the three active coordinates. Each diagonal term, $V_i(Q)$ ($i=S$, spin quantum number), is a $(2i+1)\times(2i+1)$ matrix whose diagonal elements are the spin-free potential energy surface for each spin-multiplicity state, whereas its nondiagonal elements are taken to be zero. $^{[8]}$ By omitting the $Q$ dependence, the SOC matrices, $V_{ij}$, can be written as

$$
V_{01}=\left(z_1\ ib_1\ z_1^*\right),\quad(3)
$$

$$
V_{12}=\begin{pmatrix}
z_2 & ib_2 & z_3^* & 0 & 0 \\
0 & z_4 & ib_3 & z_4^* & 0 \\
0 & 0 & z_3 & ib_2 & z_2^*
\end{pmatrix},\quad(4)
$$

$$
V_{23}=\begin{pmatrix}
z_5 & ib_4 & z_6^* & 0 & 0 & 0 & 0 \\
0 & z_7 & ib_5 & z_8^* & 0 & 0 & 0 \\
0 & 0 & z_9 & ib_6 & z_9^* & 0 & 0 \\
0 & 0 & 0 & z_8 & ib_5 & z_7^* & 0 \\
0 & 0 & 0 & 0 & z_6 & ib_4 & z_5^*
\end{pmatrix},\quad(5)
$$

![](./images/812573472701022210_1.jpg)
![](./images/812573472701022210_2.jpg)

**FIGURE 1** (a) Structure of porphyrin moiety including imidazole and $O_2$. (b) Definition of the three active coordinates $(R, \theta, d)$ used in wave packet dynamics [Color figure can be viewed at wileyonlinelibrary.com]

where the matrix elements are arranged in the order of the magnetic quantum number $(M_S)$ of the spin quantum number $(S).^{[8]} z_i, z_i^*$, and $b_i$ denote a complex value, its conjugate, and a real value, respectively. Here, we can safely ignore the SOCs with $|\Delta S| > 1$ or $|\Delta M_S| > 1$. Thus, the total potential energy matrix in Equation (2) becomes a $(16 \times 16)$ Hermitian matrix.

The spin-free potential energy surfaces for the four different spin quantum numbers are obtained from the unrestricted DFT calculations using the B97D functional. We use the standard $6$-$311+G^*$ basis sets for Fe and O atoms, and the $6$-$31G^{**}$ basis sets for C, N, and H atoms, as in our previous work. $^{[39]}$ The B97D calculations are done at the grid points described by the three coordinates $R, \theta$, and $d$, where the structure of the PorIm part is taken from the optimized structure of the isolated FePorIm in the lowest quintet state. Twenty-seven points are used for $R$ in the range of $1.5$-$6$ Å. Eleven points are chosen for $\theta$ in the range of $80$-$150^\circ$, whereas 13 points in the range of $-0.4$-$0.4$ Å are used for $d$. A total of 3,861 points are generated and all the calculations are performed using the Gaussian09 package program. $^{[48]}$ We perform the B97D calculations so that the $R$ coordinate of the $O_2$-FePorIm system becomes the Z-axis of the Cartesian coordinates. The standard cubic spline interpolation technique is used to obtain desired potential energy values at a given set of three coordinates. For the $\theta$ and $d$ coordinates, potential energy values outside the grid points are extrapolated using quadratic potentials whose polynomial parameters are determined from the grid data in the edge region. These quadratic potentials are used so that the wave packet dynamics occur mainly within the above potential energy surface region.

Figure 2a displays the one-dimensional potential energy curves for all four different spin quantum numbers as a function of $R$, which corresponds to the distance between the Fe position and the coordinate origin. The other two coordinates, namely, $\theta$ and $d$, are fully optimized with respect to energy at a fixed value of $R$. These potential energy curves correspond to the diagonal terms of the potential

![](./images/812573472701022210_3.jpg)

**FIGURE 2** (a) One-dimensional potential energy curves of FePorIm-$O_2$ in the singlet, triplet, quintet, and septet states as a function of $R$. (b) One-dimensional adiabatic potential energy curves for 16 spin states including spin-orbit couplings. The inset shows the enlarged plot in the asymptotic region. In both cases, the other two structural parameters, $\theta$ and $d$, are fully optimized with respect to energy [Color figure can be viewed at wileyonlinelibrary.com]

energy surface matrix of Equation (2). For the triplet, quintet, and sep- tet states, the potential energies are slightly shifted so that these three potential energy curves asymptotically become exactly degener- ate. The nondegenerate behavior of the original DFT calculations comes from energetic errors of the unrestricted DFT formalism. The shifted energy values are smaller than 0.13 eV. Similarly, the potential energy surface for the singlet state is also shifted so that the asymp- totic energy difference between the singlet and other states is 5.5 kcal/mol (= 0.24 eV). This value is determined from the previous best estimate (4.6-6.5 kcal/mol), which was obtained from the high- level CASPT2 calculations. $^{[49]}$ The triplet potential energy curve shows a double well feature. These two potential wells correspond to two different spin structures, as discussed in previous articles. $^{[29,39]}$ For the potential well at a longer region, $O_{2}$ has an original triplet character, even in the $O_{2}$ -FePorIm complex, and thus the $O_{2}$ moiety and the FePorIm moiety have opposite spin characters (i.e., $\alpha$ - and $\beta$-spin, respectively). In contrast, the same spin is distributed over both the $O_{2}$ and FePorIm moieties around the potential well in a shorter region due to partial electron transfer from $O_{2}$ to FePorIm. The potential energy curve for the singlet state has a potential well of~0.24 eV, which is smaller than in our previous calculations $^{[39]}$ because the FePorIm structures are always fixed in this study.

In order to further understand the quality of the present B97D-level potential energy surfaces, we have performed the strongly-contracted NEVPT2 (N-Electron Valence State Second Order Perturbation Theory) $^{[50]}$ calculations using the ORCA program. $^{[51]}$ The NEVPT2 method is an efficient computational method that can be applied to large systems and was shown to give comparable or better accuracy as the popular CASPT2. $^{[51]}$ The comparison of the potential energy curves between the B97D and NEVPT2 results is presented in Figure S1. In these calculations, the structure of the PorIm moiety is taken from the structure optimized at the B97D level. We found that both the B97D and NEVPT2 potential energy curves have a similar attractive feature suggesting that the B97D potential energy surfaces can be used to understand the nuclear dynamics at a qualitative level. However, the NEVPT2 calculations give too large asymptotic energy differences between the singlet and other spin states. This is in high contrast with the B97D results as mentioned previously. Therefore, we have compared the potential energy curves obtained from the B97D and NEVPT2 results, which are shifted in energy so as that the asymptotic energies become identical. The comparison is presented in Figure S2. It is seen that the both potential energy curves yield spin state crossings in a similar region indicating that the B97D-level potential energy surfaces are a reasonable choice for dynamics calculations.

Another important point obtained from the NEVPT2 calculations is that there exist low-lying excited states for the singlet and triplet states (see Figure S1). This indicates that such excited states should be taken into account in the nonadiabatic nuclear dynamics. However, those excited states are asymptotically correlated with the excited states of the isolated heme compound and the corresponding excita- tion energies are much larger than thermal energy. Hence, the contri- bution of those excited states is expected to be small although those states may not be ignored in the strong interaction region. The pre- sent dynamics model thus assumes "fast internal conversion" between the same spin multiplicity states with different electronic structures and focuses only on the slower intersystem crossing dynamics.

In Figure 3, two-dimensional contour plots of the potential energy surface for each spin quantum number are shown as a function of $R$ and $\theta$, where three representative values are chosen for $d(-0.2$,0, and $0.2 \AA$ ). Bold red lines in the contour plots indicate the crossing seam between the singlet and triplet potential energy surfaces. Green and blue contours correspond to the triplet-quintet and quintet-septet crossing seams, respectively. These crossing seams generally occur at shorter $R$ regions, and thus could play an important role in the narrow crossing region mechanism.

The SOC values are calculated at some selected points because it is expected that the magnitude of SOC does not depend substantially on the structure. $^{[52]}$ In this work, the SOCs are determined within the Breit-Pauli approximation (with the SOMF approximation) $^{[53]}$ usingthe state-interacting method at the state-averaged CASSCF/ def2-TZVP level of theory. These electronic structure calculations are performed using the ORCA program. $^{[51]}$ Four states (singlet, triplet, quintet, and septet) are equally averaged, where eight active electrons are distributed among seven active orbitals in the CASSCF wavefunction. The active space chosen here is minimal, including five Fe $3 d$ and two $O_{2} \pi^{*}$ orbitals. The active orbitals used in the CASSCF calculations are shown in Figure S3. We have also performed the CASSCF calculations at a selected heme- $O_{2}$ structure to understand the effect of higher electronic states on the calculated SOC values, where we have included a total of two singlet states and three triplet states. The obtained results are summarized in Table S1. It is found that the magnitude of the SOC value between the lowest triplet and quintet states is not very different from the single spin state result. This trend can also be seen for the SOC between the quintet and sep- tet states.

In Figure 4, the SOCs obtained from the state-averaged CASSCF $(8_{e}, 7_{o}) /$ def2-TZVP calculations are plotted as a function of $R$ with $d$ set to zero. In this case, $R$ is exactly the same as the $Fe-O_{a}$ distance(see Figure 1). Figure 4a shows the SOC elements between the singlet and triplet states. The value of $b_{1}(M_{s}=0$ , see Equation (3)) is much larger $(\sim 400 ~cm^{-1})$ than the values of $z_{1}(M_{s}= \pm 1)$ . This result is quantitatively consistent with the highly accurate multi-state CASPT2 calculations, $^{[29]}$ where a larger active space with larger basis sets was employed. In contrast with the singlet-triplet coupling result, the cal- culated SOCs between triplet and quintet and between quintet and septet states are much smaller (Figures 4b,c). The coupling values are essentially zero for $R \geq 3 \AA$ , although the corresponding values increase at shorter distances. The results presented in Figure 4 sug- gest that the narrow crossing region mechanism is more important than the broad crossing region mechanism in the overall spin-inversion dynamics. The $\theta$ dependence of the SOC is also examined; however, the calculated coupling values do not strongly depend on $\theta$ . Similarly, we examine the $d$ dependence of the SOCs. The structural dependence is shown in Figure S4. The change in $d$ affects the $Fe-O_{a}$ distance $(=R+d)$ . Therefore, the magnitude of the SOC can be

![](./images/812573472701022210_4.jpg)

FIGURE 3 Two-dimensional contour plots of the singlet, triplet, quintet, and septet potential energy surfaces for the FePorIm-O₂ model as a function of $(R,\theta)$ with three values of $d$. The contour increment is 0.05 eV. Zero contours are shown by bold black lines. Dotted and solid thin contours indicate negative and positive contours, respectively. Bold red, green, and blue lines correspond to singlet-triplet, triplet-quintet, and quintet-septet crossing seams, respectively [Color figure can be viewed at wileyonlinelibrary.com]

roughly described as a function of the Fe-Oₐ distance only. Accordingly, the $\theta$ dependence of the SOC is ignored and the overall SOC is assumed to depend on only the Fe-Oₐ distance in the subsequent wave packet calculations. The calculated SOC values are interpolated with the cubic spline technique to obtain a value at a desired coordinate.

Once the spin-free potential energy surfaces and nondiagonal SOC functions are obtained, we construct the total $(16\times16)$ potential energy surface matrix. Figure 2b shows the 16 adiabatic potential energy curves obtained from the diagonalization of the $(16\times16)$ matrix as a function $R$. Similar to Figure 2a, the other two coordinates, $\theta$ and $d$, are fully optimized with respect to energy at a fixed value of $R$.

The plot in the inset in Figure 2b shows enlarged potential energy curves in the asymptotic region. The triplet, quintet, and septet states, which are asymptotically degenerate without SOCs, split into the states with different energies. Due to the largest coupling $(b_1\sim400\ \text{cm}^{-1})$ between the singlet and triplet $(M_S=0)$ states, the contribution of the triplet $(M_S=0)$ state is the most dominant for the lowest adiabatic state in the asymptotic region. In addition, the energy splitting between the lowest adiabatic state and the next adiabatic state is obtained as about $80\ \text{cm}^{-1}$.

The nuclear wave packet vector $\psi(R,\theta,d;t)$ is described by solving the time-dependent Schrödinger equations as

![](./images/812573472701022210_5.jpg)

FIGURE 4 Spin-orbit couplings plotted as a function of Fe-O (=
$R + d$) distance. The coupling values are calculated at the state-
averaged CASSCF(8e, 7o)/def2-TZVP level [Color figure can be
viewed at wileyonlinelibrary.com]

$$
i \frac{\partial}{\partial t} \boldsymbol{\psi}(R, \theta, d ; t)=\mathcal{H}(R, \theta, d) \boldsymbol{\psi}(R, \theta, d ; t), \tag{6}
$$

where the nuclear Hamiltonian operator is given by Equation (1).
The initial wave packet at $t = 0$ is constructed with the product of the
standard Gaussian wave packet and Gaussian functions as

$$
\boldsymbol{\psi}(R, \theta, d ; t=0) \begin{pmatrix}
c_{1}(0) \\
c_{2}(0) \\
\vdots \\
c_{16(0)}
\end{pmatrix} e^{-a_{R}\left(R-R_{0}\right)^{2}-i k R} e^{-a_{\theta}\left(\theta-\theta_{0}\right)^{2}} e^{-a_{d}\left(d-d_{0}\right)^{2}}, \tag{7}
$$

where $c_{i}\ (t = 0)$ is the initial population amplitude for the $i$-th diabatic
state ($i = 1$ for singlet, $i = 2$-$4$ for triplet, $i = 5$-$9$ for quintet, and
$i = 10$-$16$ for septet). $k$ is the initial translational wave vector for the
motion along $R$ and is given by $k = (2\mu_{R}E)^{1/2}$, where $E$ is collision
energy. This energy corresponds to an average collision energy in the
time-dependent representation due to the Gaussian width. $R_{0},\ \theta_{0},$ and
$d_{0}$ are central positions of the initial wave packet and $a_{R},\ a_{\theta},$ and $a_{d}$ are
their width parameters, respectively. We use this simple functional
form for the initial wave packet because the purpose of this study is
to understand the nonadiabatic spin-inversion mechanism qualita-
tively. The time-dependent nuclear wave packet is represented using
grid-based discrete-variable representations (DVRs), $^{[54]}$ where the
standard particle-in-a-box basis is employed for all three coordinates.
Once the initial wave packet is prepared, it is propagated in time using
the extended split-operator method, which corresponds to the exten-
sion of the standard adiabatic split-operator method to the multiple
potential energy surface problems. $^{[55-58]}$ To avoid the artificial reflec-
tion of the wave packet at the longer edge of the grid in the
$R$ coordinate, we use a negative imaginary potential with a quadratic
form. The DVR grid parameters are 256, 128, and 64 points for $R,\ \theta,$
and $d$ coordinates, respectively. The total step for time propagation is
20,000-100,000 with $\Delta t = 10.0$ atu depending on the average colli-
sion energy.

## 3 | RESULTS AND DISCUSSION

Figures 5 and 6 show representative wave packet evolutions obtained
from the calculations with an average collision energy of $E = 0.136$ eV
$(= 0.005$ au). The initial wave packet is placed on the triplet, quintet,
and septet states with an equal diabatic population ($c_{1} = 0$ and
$c_{i} = 1/15$ for $i = 2$-$16$). In these plots, the wave packet densities are
summed over all the $M_{s}$ states. The wave packets arrive at the poten-
tial well region at $t \sim 0.5$ ps. After this, the singlet state is formed. A
small singlet component is visible at an earlier time of $t = 0.242$ ps
(Figures 5a and 6a); however, this component comes from the initial
singlet-triplet mixing due to the large $b_{1}$ SOC value. A large part of
the wave packets on the triplet, quintet, and septet states moves to a
large-$R$ region at $t = 1.208$ ps, whereas part of the wave packet on the
singlet state stays around the potential well even at $t = 1.208$ ps. This
indicates that quantum resonance states with a longer lifetime are
produced once the wave packet is trapped in the potential well. How-
ever, because the present dynamics are essentially an inelastic scatter-
ing process, the wave packet density should finally become zero due
to the absorption at the edge. The results confirm that more than
99% of the wave packet density is absorbed by the negative imaginary
potential within 24 ps.

The nonadiabatic spin-inversion mechanism can also be under-
stood from the time-dependent population on each spin-multiplicity
state, which corresponds to $|c_{i}(t)|^{2}$ ($i = 1$-$16$). Figure 7 shows the
16 population values plotted as a function of time for the wave packet
dynamics presented in Figures 5 and 6. The $i = 1$ population curve
(singlet, $S = M_{s} = 0$), which is initially zero, shows a maximum ($\sim$0.03)
at $t = 0.5$ ps. The population curve ($i = 3$, triplet with $M_{S} = 0$) shows a
dip at $t = 0.5$ ps. This mirror image indicates that spin-inversion from
one of the triplet states to the singlet state occurs around this time.
The detailed wave packet analyses show that this behavior

![](./images/812573472701022210_6.jpg)

**FIGURE 5** Snapshots of the wave packet probability densities plotted as a function of $(R, \theta)$ at an average collision energy of $E = 0.123$ eV (0.005 au) eV. For the triplet, quintet, and septet states, the corresponding probability density is summed over all $M_S$ contributions. The initial wave packet parameters are $(R_0, \theta_0, d_0, a_R, a_\theta, a_d) = (6.35$ Å, $120^\circ$, $0.16$ Å, $0.2$ au, $6.0$ au, $30.0$ au; see Equation (7))
[Color figure can be viewed at wileyonlinelibrary.com]

![](./images/812573472701022210_7.jpg)

**FIGURE 6** Snapshots of the wave packet probability densities plotted as a function of $(R, d)$ at an average collision energy of $E = 0.123$ eV (0.005 au) eV. For the triplet, quintet, and septet states, the corresponding probability density is summed over all $M_S$ contributions. The initial wave packet parameters are $(R_0, \theta_0, d_0, a_R, a_\theta, a_d) = (6.35$ Å, $120^\circ$, $0.16$ Å, $0.2$ au, $6.0$ au, $30.0$ au; see Equation (7))
[Color figure can be viewed at wileyonlinelibrary.com]

corresponds to the first passage dynamics around the singlet-triplet crossing region. Thus, the spin-inversion in $O_2$ binding to heme is an ultrafast spin-inversion process. The populations for other states are almost constant up to $t = 1$ ps, although small nonadiabatic transitions are visible for the triplet states with $M_S = \pm 1$. The change in nonadiabatic transitions for the quintet and septet states are even smaller. These results are consistent with the magnitude of SOCs shown in Figure 4. After $t = 1$ ps, all the populations gradually decay due to the absorption of the wave packet density through the negative imaginary potential in the edge region.

Based on the results presented in Figure 7, the quintet and septet states are essentially spectator states and can be safely ignored in wave packet dynamics. Therefore, we can reduce the 16-spin state dynamics to the 4-spin state dynamics, which includes only the singlet and three triplet states. This simplification substantially reduces computational time and we perform the 4-spin state dynamics calculations using many different initial conditions. The nonadiabatic dynamics do not depend strongly on the choice of the Gaussian width parameters and the initial wave packet position parameters. Instead, the initial average collision energy affects the results. Representative results are shown in Figure 8, where we plot the diabatic population evolutions calculated at four average collision energies ($E = 0.0544, 0.136, 0.218$, and $0.272$ eV). In all cases, the initial wave packet is placed on the triplet states with an equal diabatic population ($c_1 = 0$ and $c_2 = c_3 = c_4 = 1/3$). The result presented in Figure 8(b) is similar to that in Figure 7 (except for the absolute values), indicating that including the quintet and septet states does not affect the nonadiabatic dynamics. With increase in average collision energy, the earlier the time at which the nonadiabatic transition occurs. The population decay due to the negative imaginary absorption also occurs at an earlier time as the collision energy increases. These results are quite reasonable. More importantly, the nonadiabatic transition probability slightly increases as the average collision energy increases. This behavior can be understood from the increase in the peak value of the population

for $S = M_s = 0$. However, we emphasize that the present wave packet dynamics calculation cannot yield an accurate transition probability at a specific collision energy because the flux analyses cannot be applied.

![](./images/812573472701022210_8.jpg)

FIGURE 7 Time evolution of the wave packet population on the spin diabatic state obtained from the 16-spin state nonadiabatic calculations. The initial diabatic populations are set to $c_1 = 0$ and $c_i = 1/15$ ($i = 2$–16). The inset shows the enlarged plot [Color figure can be viewed at wileyonlinelibrary.com]

Such an analysis is possible if the interaction between the adiabatic states is completely ignored such as asymptotic states. In fact, the dynamics is a totally inelastic process and the incoming wave packets, which are initially located on the triplet states, finally dissociate into FePorIm + $O_2$ in the triplet states again because the asymptotic singlet production is energetically forbidden at low energy (see Figure 2).

In the multidimensional inelastic scattering case, we cannot obtain accurate probabilities for the singlet state production from the wave packet calculations. Nevertheless, it may be important to compare the results of the wave packet calculations with the well-known two-state Landau-Zener model. To estimate these probabilities roughly, we first perform the 4-spin state wave packet dynamics with a different initial wave packet population so that the initial wave packet population is only in the lowest adiabatic state in the asymptotic region (Figure 2b). This adiabatic population can be easily transformed into the spin diabatic populations using the eigenvectors of the $(4 \times 4)$ Hamiltonian matrix. In this case, the contribution of the triplet states with $M_s = \pm 1$ is essentially zero and only the nonadiabatic transition between the singlet and $M_s = 0$ triplet states is visible. The wave packet calculations are performed at four average collision energy values. The time-dependent populations in the two adiabatic states are plotted in Figure 9a as a function of time. The

![](./images/812573472701022210_9.jpg)

FIGURE 8 Time evolution of the wave packet population on the spin diabatic state obtained from the four-spin state nonadiabatic calculations. The initial diabatic populations were set to $c_1 = 0$ and $c_i = 1/3$ ($i = 2$–4) [Color figure can be viewed at wileyonlinelibrary.com]

![](./images/812573472701022210_10.jpg)

FIGURE 9 (a) Time evolution of the wave packet populations on the two spin adiabatic states obtained from the four-spin state nonadiabatic calculations, where the initial population on the lowest adiabatic state was set to unity. The calculations are done at four collision energies. (b) Time evolution of populations on the singlet ($S = M_s = 0$) and triplet ($S = 1$ and $M_s = 0$) diabatic states.
(c) Comparison of singlet production probabilities as a function of collision energy. Open and closes circles are from the adiabatic and diabatic analyses of the 3D wave packet calculations, respectively. Solid line is corresponding to the one-dimensional result (see text)
[Color figure can be viewed at wileyonlinelibrary.com]

sum of these two adiabatic populations becomes almost unity (before the population decay starts), indicating that the dynamics can be indeed described by the two-state model (evolution of the adiabatic wave packets are also shown in Figures S5 and S6). Interestingly, we can see the plateau region of the adiabatic populations just after the first passage of the crossing region. For example, in the case of $E = 0.136$ eV, the two adiabatic population curves are found to be almost flat in the range of $t = 0.55$–0.75 ps. This behavior strongly suggests that these adiabatic populations are corresponding to the single-passage transition probabilities between the two states. We can also see a slight increase in the populations on the lowest adiabatic states for $E = 0.0544$ and 0.136 eV. After this, the populations are seen to decay due to the wave packet absorption. This phenomenon suggests that the transition from the singlet to triplet states occurs before the dissociation into FePorIm + $O_2$. From these considerations, we can roughly estimate the singlet-triplet transition probabilities after the first passage of the crossing region from the observed plateau regions.

We can also roughly estimate the singlet production probabilities from the diabatic populations on the $S = M_s = 0$ state, which are plotted in Figure 9b as a function of time. The results in Figure 9b are similar to the results presented in Figure 8 except for the absolute value (by a factor of ~3). The population peak approximately corresponds to the first wave packet passage around the crossing region. We estimate the transition probability by averaging the diabatic population values in the flat region seen in the adiabatic population curve mentioned above. In this case, we have subtracted the small average initial population due to the coupling. The results of these two (adiabatic and diabatic) analyses are presented in Figure 9c. It is interesting note that the two analyses yield similar probabilities except for the lowest average energy. Also shown in Figure 9c is the transition probability calculated using the time-independent $R$-matrix propagation method,$^{[57]}$ where the one-dimensional singlet and triplet potential energy curves along with the SOCs are used (Figures 2 and 4). In this case, the transition probability can be calculated by terminating at $R = 1.8$ Å, which converts an inelastic scattering problem into a reactive scattering problem (single passage scattering case since the asymptotic analysis is applied at $R = 1.8$ Å). The one-dimensional result shows an expected feature of the standard Landau-Zener model.$^{[6-8]}$ One important conclusion is that the one-dimensional result is smaller than the wave packet result by a factor of 2–4, although our probability estimation procedures are approximate. Nevertheless, similar findings have been reported in recent theoretical studies using ab initio multiple spawning calculations of the spin-inversion dynamics of the $GeH_2$ and $SiH_2$ systems.$^{[59-61]}$ Our group has more recently found a similar trend in the study of the $^3$Fe (CO)$_4$ + $H_2$ $\rightarrow$ $^1$FeH$_2$(CO)$_4$ spin-inversion reaction.$^{[52]}$ These theoretical studies along with the present study indicate that coupling between the nonadiabatic spin-inversion motion and other nuclear motions plays an essential role leading to multidimensional nonlocal transitions. Thus, we qualitatively conclude that the multidimensional and nuclear quantum effects play an important role in spin-inversion processes for polyatomic systems although more systematic dynamics studies should be performed to understand the effect of missing nuclear degrees of freedom.

## 4 | CONCLUSIONS AND FUTURE DIRECTIONS

Understanding detailed spin-inversion mechanisms in $O_2$ binding to heme is a long-standing issue in biochemistry. In this work, we performed reduced-dimensionality nonadiabatic quantum wave packet calculations using a model heme compound, which consisted of Fe(II)-

porphyrin and imidazole. Although we considered only three nuclear degrees of freedom and only the lowest spin-multiplicity states, we obtained a reasonable picture of the spin-inversion mechanism. The spin-inversion between the singlet state ($S = 0$) and one of the triplet spin states ($S =1$ and $Ms = 0$) was important due to large SOCs and the other spin states with $Ms = \pm1$ did not contribute substantially to the nonadiabatic spin-inversion dynamics. Because the spin inversion occurred mainly in a shorter Fe-O distance region of the potential energy surfaces, we concluded that the narrow crossing region model played a more important role than the broad crossing region model within the present reduced-dimensional model. However, we empha- size that this conclusion was derived from the reduced-dimensionality model. It is possible that the SOCs between higher spin-multiplicity states such quintet and septet states may be large in different poten- tial energy surface regions, which we did not consider in this study. In addition to this, the inclusion of more nuclear degrees of freedom in the dynamics may change the nonadiabatic mechanism due to the efficiency change of vibrational energy redistribution. More impor- tantly, it should be emphasized that spin-orbit couplings are not always dominant interactions in intersystem crossing phenomena. Recently, even if spin-orbit couplings are small, spin-vibronic interac- tions, which are corresponding to the second-order terms simulta- neously containing spin-orbit and vibronic couplings, $^{[40,47]}$ can play a very important role in the nonadiabatic intersystem crossing dynam- ics. In fact, it is found that the spin-vibronic effect is significant in the intersystem crossing in thermally activated delayed fluorescence pro- cesses for $Cu$ complexes. $^{[62]}$ All these points should be addressed inthe future to fully understand the nonadiabatic dynamics in $O_{2}$  binding to heme.

## ACKNOWLEDGMENTS
This work was supported by a Grant-in-Aid for Scientific Research from the Ministry of Education, Culture, Sports, Science and Technol- ogy of Japan (Grant No. 17KT0093).

## ORCID
Toshiyuki Takayanagi $\circledcirc$ https://orcid.org/0000-0003-0563-9236
Jun-ya Hasegawa $\circledcirc$ https://orcid.org/0000-0002-9700-3309

## REFERENCES
[1] S. Shaik, H. Chen, J. Bio. Inorg. Chem. 2011, 16, 841.
[2] B. F. Minaev, V. O. Minaeva, H. Ågren, Spin-orbit coupling in enzy- matic reactions and the role of spin in biochemistry. in Handbook of Computational Chemistry (Ed: J. Leszczynski), Springer, Dordrecht1067, p. 2012.
[3] K. P. Kepp, Coord. Chem. Rev. 2017, 344, 363.
[4] J. Friedman, B. Campbell, Structural dynamics and reactivity in hemo- globin. In: Protein Structure. Proceedings in Life Sciences. (Editors: R. Austin et al.), 1987, Springer, New York, NY, 211.
[5] B. H. Huynh, G. C. Papaefthymiou, C. S. Yen, J. L. Groves, C. S. Wu, J. Chem. Phys. 1974, 61, 3750.
[6] C. M. Marian, Comp. Mol. Sci. 2012, 2, 187.
[7] J. N. Harvey, Comp. Mol. Sci. 2014, 4(1), 1.
[8] A. O. Lykhin, D. S. Kaliakin, G. E. dePolo, A. A. Kuzubov, S. A. Varganov, Int. J. Quantum Chem. 2016, 116, 750.
[9] D. Schröder, S. Shaik, H. Schwarz, Acc. Chem. Res. 2000, 33, 139.
[10] H. Hirao, D. Kumar, L. Que, S. Shaik, J. Am. Chem. Soc. 2006, 128,8590.
[11] S. Shaik, H. Hirao, D. Kumar, Acc. Chem. Res. 2007, 40, 532.
[12] D. A. Scherlis, D. A. Estrin, Int. J. Quantum Chem. 2002, 87, 158.
[13] S. Franzen, Proc. Nat. Acad. Sci. 2002, 99, 16754.
[14] K. P. Jensen, U. Ryde, J. Bio. Chem. 2004, 279, 14561.
[15] H. Nakashima, J. Hasegawa, H. Nakatsuji, J. Comput. Chem. 2006,27,426.
[16] J. Ribas-Ariño, J. J. Novoa, Chem. Comm. 2007, 3160.
[17] N. Strickland, J. N. Harvey, J. Phys. Chem. B 2007, 111, 841.
[18] D. A. Scherlis, M. Cococcioni, P. Sit, N. Marzari, J. Phys. Chem. B2007, 111, 7384.
[19] M. Radoń, K. Pierloot, J. Phys. Chem. A 2008, 112, 11824.
[20] H. Chen, M. lkeda-Saito, S. Shaik, J. Am. Chem. Soc. 2008, 130,14778.
[21] P. E. M. Siegbahn, M. R. A. Blomberg, S.-L. Chen, J. Chem. Theo. Comp.2010, 6, 2040.
[22] D. E. Bikiel, F. Forti, L. Boechi, M. Nardini, F. J. Luque, M. A. Marti, D. A. Estrin, J. Phys. Chem. B 2010, 114, 8536.
[23] S. R. Badu, R. H. Pink, R. H. Scheicher, A. Dubey, N. Sahoo, K. Nagamine, T. P. Das, Hyperfine Interact. 2010, 197, 331.
[24] T. Saito, Y. Kataoka, Y. Nakanishi, T. Matsui, Y. Kitagawa, T. Kawakami, M. Okumura, K. Yamaguchi, J. Mol. Struct.: THEOCHEM2010, 954, 98.
[25] M.-S. Liao, M.-J. Huang, J. D. Watts, Mol. Phys. 2011, 109, 2035.
[26] M. E. Ali, B. Sanyal, P. M. Oppeneer, J. Phys. Chem. B 2012, 116,5849.
[27] K. P. Kepp, ChemPhysChem 2013, 14, 3551.
[28] V. E. J. Berryman, R. J. Boyd, E. R. Johnson, J. Chem. Theo. Comp.2015, 11, 3022.
[29] Y. Kitagawa, Y. Chen, N. Nakatani, A. Nakayama, J. Hasegawa, Phys. Chem. Chem. Phys. 2016, 18, 18137.
[30] N. Kitagawa, M. Obata, T. Oda, Chem. Phys. Lett. 2016, 643, 119.
[31] T. Yang, M. G. Quesne, H. M. Neu, F. G. C. Reinhard, D. P. Goldberg, S. P. de Visser, J. Am. Chem. Soc. 2016, 138, 12375.
[32] O. S. Siig, K. P. Kepp, J. Phys. Chem. A 2018, 122, 4208.
[33] A. Lábas, D. K. Menyhárd, J. N. Harvey, J. Oláh, Chem. - Eur. J. 2018,24,5350.
[34] D. Kurokawa, J. S. Gueriba, W. A. Diño, ACS Omega 2018, 3, 9241.
[35] Q. M. Phung, K. Pierloot, Phys. Chem. Chem. Phys. 2018, 20, 17009.
[36] L. Du, F. Liu, Y. Li, Z. Yang, Q. Zhang, C. Zhu, J. Gao, J. Phys. Chem. C2018, 122, 2821.
[37] B. Yang, L. Gagliardi, D. G. Truhlar, Phys. Chem. Chem. Phys. 2018, 20,4129.
[38] T. Takayanagi, T. Nakatomi, J. Comput. Chem. 2018, 39, 1319.
[39] K. Saito, Y. Watabe, T. Fujihara, T. Takayanagi, J. Hasegawa, J. Comput. Chem. 2020, 41, 1130.
[40] T. J. Penfold, E. Gindensperger, C. Daniel, C. M. Marian, Chem. Rev.2018, 118, 6975.
[41] H. Ando, S. luchi, H. Sato, Chem. Phys. Lett. 2012, 535, 177.
[42] C. Lévêque, R. Taïeb, H. Köppel, J. Chem. Phys. 2014, 140, 091101.
[43] J. Eng, C. Gourlaouen, E. Gindensperger, C. Daniel, Acc. Chem. Res.2015, 48, 809.
[44] M. Pápai, T. J. Penfold, K. B. Møller, J. Phys. Chem. C 2016, 120,17234.
[45] M. Pápai, G. Vankó, T. Rozgonyi, T. J. Penfold, J. Phys. Chem. Lett.2016,7,2009.
[46] Y. Harabuchi, J. Eng, E. Gindensperger, T. Taketsugu, S. Maeda, C. Daniel, J. Chem. Theo. Comp. 2016, 12, 2335.
[47] M. Fumanal, E. Gindensperger, C. Daniel, J. Chem. Theo. Comp. 2017,13,1293.
[48] M. J. Frisch, G. W. Trucks, H. B. Schlegel, G. E. Scuseria, M. A. Robb, J. R. Cheeseman, G. Scalmani, V. Barone, B. Mennucci, G. A. Petersson, H. Nakatsuji, M. Caricato, X. Li, H. P. Hratchian, A. F.

Izmaylov, J. Bloino, G. Zheng, J. L. Sonnenberg, M. Hada, M. Ehara, K. Toyota, R. Fukuda, J. Hasegawa, M. Ishida, T. Nakajima, Y. Honda, O. Kitao, H. Nakai, T. Vreven, J. A. Montgomery, J. E. Peralta, F. Ogliaro, M. Bearpark, J. J. Heyd, E. Brothers, K. N. Kudin, V. N. Staroverov, R. Kobayashi, J. Normand, K. Raghavachari, A. Rendell, J. C. Burant, S. S. Iyengar, J. Tomasi, M. Cossi, N. Rega, J. M. Millam, M. Klene, J. E. Knox, J. B. Cross, V. Bakken, C. Adamo, J. Jaramillo, R. Gomperts, R. E. Stratmann, O. Yazyev, A. J. Austin, R. Cammi, C. Pomelli, J. W. Ochterski, R. L. Martin, K. Morokuma, V. G. Zakrzewski, G. A. Voth, P. Salvador, J. J. Dannenberg, S. Dapprich, A. D. Daniels, Ö. Farkas, J. B. Foresman, J. V. Ortiz, J. Cioslowski, D. J. Fox, Gaussian 09, Revision D.01, Gaussian, Inc, Wallingford, CT 2009.

[49] S. Vancoillie, H. Zhao, M. Radoń, K. Pierloot, J. Chem. Theo. Comp. 2010, 6, 576.

[50] C. Angeli, R. Cimiraglia, S. Evangelisti, T. Leininger, J. P. Malrieu, J. Chem. Phys. 2001, 114, 10252.

[51] F. Neese, Comp. Mol. Sci. 2018, e1327, 8.

[52] T. Takayanagi, Y. Watabe, T. Miyazaki, Molecules 2020, 25, 882.

[53] F. Neese, J. Chem. Phys. 2005, 122, 034107.

[54] J. C. Light, I. P. Hamilton, J. V. Lill, J. Chem. Phys. 1985, 82, 1400.

[55] T.-X. Xie, Y. Zhang, M.-Y. Zhao, K.-L. Han, Phys. Chem. Chem. Phys. 2003, 5, 2034.

[56] T.-S. Chu, K.-L. Han, J. Phys. Chem. A 2005, 109, 2050.

[57] N. Balakrishnan, C. Kalyanaraman, N. Sathyamurthy, Phys. Rep. 1997, 280, 79.

[58] G. Nyman, H.-G. Yu, Rep. Prog. Phys. 2000, 63, 1001.

[59] D. A. Fedorov, S. R. Pruitt, K. Keipert, M. S. Gordon, S. A. Varganov, J. Phys. Chem. A 2016, 120, 2911.

[60] D. A. Fedorov, A. O. Lykhin, S. A. Varganov, J. Phys. Chem. A 2018, 122, 3480.

[61] R. R. Zaari, S. A. Varganov, J. Phys. Chem. A 2015, 119, 1332.

[62] T. J. Penfold, F. B. Dias, A. P. Monkman, Chem. Comm. 2018, 54, 3926.

# SUPPORTING INFORMATION
Additional supporting information may be found online in the Supporting Information section at the end of this article.

How to cite this article: Saito K, Watabe Y, Miyazaki T, Takayanagi T, Hasegawa J. Spin-inversion mechanisms in $O_2$ binding to a model heme compound: A perspective from nonadiabatic wave packet calculations. J Comput Chem. 2020; 1-11. https://doi.org/10.1002/jcc.26409
https://doi.org/10.1038/s42005-024-01720-8

# Chirality, anisotropic viscosity and elastic anisotropy in three-dimensional active nematic turbulence

![](./images/1017408582175424536_1.jpg)

Nika Kralj¹, Miha Ravnik © ¹² & Žiga Kos © ¹²³ ✉

Various active materials exhibit strong spatio-temporal variability of their orientational order known as active turbulence, characterised by irregular and chaotic motion of topological defects, including colloidal suspensions, biofilaments, and bacterial colonies.In particular in three dimensions, it has not yet been explored how active turbulence responds to changes in material parameters and chirality.Here, we present a numerical study of three-dimensional (3D) active nematic turbulence, examining the influence of main material constants: (i) the flow-alignment viscosity, (ii) the magnitude and anisotropy of elastic deformation modes (elastic constants), and (iii) the chirality. Specifically, this main parameter space covers contractile or extensile, flow-aligning or flow tumbling, chiral or achiral elastically anisotropic active nematic fluids. The results are presented using time- and space-averaged fields of defect density and mean square velocity. The results also discuss defect density and mean square velocity as possible effective order parameters in chiral active nematics, distinguishing two chiral nematic states—active nematic blue phase and chiral active turbulence. This research contributes to the understanding of active turbulence, providing a numerical main phase space parameter sweep to help guide future experimental design and use of active materials.

Active fluids are diverse synthetic and biological materials¹⁻¹⁰. Active nematics are characterized by orientational order along the director vector $\mathbf{n}$ and propelled by anisotropic active stress¹¹,¹². A notable and rather ubiquitous dynamic state exhibited by active nematics is active turbulence¹³, characterized by continuous spatio-temporal defect proliferation and annihilation. This phenomenon is governed by the intricate interplay between defects within the director field and the structures of the velocity field¹⁴. In three dimensions, the structure of active turbulence comprises a dynamic rewiring network of defect lines and loops¹⁵⁻¹⁸, where the diverse range of possible defect shapes and their interplay with the velocity field pose significant challenges for its understanding, control and possible applicability.

Approaches for studying three-dimensional (3D) active turbulence include theoretical models of individual defect loops¹⁹⁻²¹, spectral analysis¹⁶,¹⁷, and defect tracking and extracting the statistics of linked loops²², defect curvature and length¹⁹,²³. Another possible approach is to extract the mean-field observables such as average defect density and squared velocity. The scaling of such observables with the activity was determined for single elastic constant and constant viscosity parameters²³,²⁴. However, a systematic study of 3D active nematic turbulence for different elasticity, viscosity, and chirality material parameters also at different values of activities has not been performed yet. The role of chirality in active turbulence is also relevant as the active matter materials are often weakly chiral²⁵,²⁶. As shown also for 2D active nematics²⁷⁻²⁹, a systematic numerical study can lead to better experimental control of active mater with different material properties and serve as a benchmark for theoretical models of activity-dependent dynamic regimes, instabilities, and coupled structures in the flow and orientation field.

In this paper, we show three-dimensional active nematic turbulence at different values of the main material parameters – i.e. (i) the flow-alignment viscosity parameter, (ii) the elastic constants of splay, twist, and bend deformation modes, and (iii) the intrinsic chirality. Specifically, chirality is introduced via chiral elastic energy contribution. From numerical simulations of active dynamics, defect density and mean square velocity are extracted. The simulations are performed for contractile and extensile active materials and show distinct scalings with alignment parameter and average elastic constant, while elastic anisotropy has little effect on the mean-field averaged observables of active turbulence. For chiral active nematic

¹Faculty of Mathematics and Physics, University of Ljubljana, Ljubljana, Slovenia. ²Department of Condensed Matter Physics, Jožef Stefan Institute, Ljubljana, Slovenia. ³International Institute for Sustainability with Knotted Chiral Meta Matter (WPI-SKCM2), Hiroshima University, Higashi-Hiroshima, Japan.
✉ e-mail: ziga.kos@fmf.uni-lj.si

Communications Physics| (2024)7:222

turbulence, we show that increasing inverse chiral pitch $q_0$ increases the defect density and decreases the mean square velocity. At high values of $q_0$, a transition between the active nematic blue phase and chirality-affected active turbulence is observed. Distinctly, in the active nematic blue phase, we observe effective jamming of the defect lattice and a strong drop in the magnitude of the flow field.

## Results and discussion
We performed numerical simulations of 3D active nematic turbulence using the Beris-Edwards model of nematodynamics and the active stress tensor (Methods). We numerically solve the Q-tensor and the velocity field dynamics on a periodic grid using finite difference and lattice-Boltzmann numerical approaches, respectively$^{17,24,29-32}$. The main mechanisms of active turbulence that we focus on are visualised in Fig. 1.

Q-tensor field is shown in Fig. 1a, where black rods show the director field as the main eigenvector of the Q-tensor and the gray isosurfaces show the degree of order representing the main eigenvalue. The degree of order is reduced near the core of disclination lines, which are string-like disordered structures spanning the simulation box. Figure 1b shows the velocity field and its magnitude for a selected snapshot of active turbulence. The nematic alignment has three main deformation modes, splay $(\nabla \cdot \mathbf{n})^2$, twist $\left[\mathbf{n} \cdot(\nabla \times \mathbf{n})-\frac{2\pi}{p_0}\right]^2$, and bend $[\mathbf{n} \times(\nabla \times \mathbf{n})]^2$, each with its own elastic constant $K_1$, $K_2$, and $K_3$, respectively. Twist mode can be spontaneously favoured in chiral nematic fluids by incorporating a finite intrinsic chiral pitch length $p_0$ (Fig. 1d). Active force is computed as $-\zeta \nabla \cdot Q$ and is generated by the splay and bend deformations of the active constituents alignment$^{26}$. The force direction in Fig. 1c is shown for extensile active materials ($\zeta>0$), opposite direction is expected for contractile materials ($\zeta<0$). Anisotropic viscosity of nematic fluids is in the Beris-Edwards model related to the flow-aligning parameter $\chi$, which is typically dependent on the shape of nematic building blocks and describes if they are aligning in flow gradient at a fixed angle, or constantly tumbling (Fig. 1e). Note that in principle, a general (passive or active) nematic fluid has 6 viscosity coefficients, 5 of which are independent$^{33}$. While the concepts of elastic anistropy, chirality, and flow alignment are well understood in equilibrium and driven nematic fluids, their effects on the irregular state of active turbulence is less understood, particularly in three dimensions. Here, we show how the properties of active turbulence depend on the material coupling constants determining the strength or anisotropy of elasticity, viscosity, and chirality.

## Extensile, contractile, aligning, and tumbling nematics
The defect density and the average flow magnitude in active turbulence are affected by the viscosity parameters of the nematic fluid. Here, we vary the flow-aligning parameter $\chi$, effectively modelling the flow-tumbling ($\chi<\chi_t$) and flow-aligning ($\chi>\chi_t$) nematic fluids$^{33}$, where the transition between flow-aligning and flow-tumbling regime in our simulations corresponds to $\chi_t=\frac{9S_{eq}}{4+3S_{eq}}=0.86$. At the highest value of the alignment parameter in the simulation ($\chi=1.5$), the cross-sections of the director field and the velocity magnitude field show deformation at a larger scale compared to the lowest value of the aligning parameter at $\chi=0.2$ (Fig. 2a). During the simulation, both the defect density (Fig. 2b) and the mean square velocity (Fig. 2c) fluctuate in time due to finite size effect of the simulation box. We consider the effect of the alignment parameter both for the extensile ($\zeta>0$) and the contractile ($\zeta<0$) active nematics. Independently from the sign of the active stress, the mean defect density is decreasing with an increase of the alignment parameter $\chi$ (Fig. 2d). Differently, we observe that the mean velocity decreases with the alignment parameter for contractile active nematics and increases for extensile active nematics (Fig. 2e). Different values of the flow-aligning parameter result in different Ericksen-Leslie coefficients of the anisotropic viscosity tensor (see Methods). Similarly to 2D active nematics with substrate friction$^{34}$, some change of active behaviour is observed directly at the transition between flow-aligning and flow-tumbling regime at $\chi_t=0.86$. Mean velocity dependence on the alignment parameter $\chi$ in Fig. 2(e) gradually changes its slope around $\chi_t$.

## Role of elastic constants in active turbulence
Simulations at different values of the nematic elastic constants show two main results: (i) the defect density scales approximately linearly with the average elastic constant, and (ii) changing the elastic anisotropy—different elastic penalties of the splay, twist, and bend director deformation modes—has a minor effect on the active nematic defect density and average velocity magnitude.

![](./images/1017408582175424536_2.jpg)

Fig. 1 | Active nematic turbulence in a three-dimensional system. a, b A snapshot of an active turbulence showing (a) a disclination network (gray isosurfaces) with a director field cross-section (black rods) and (b) a cross-section of the velocity field. c–e A schematic representation of mechanisms of (chiral) active turbulence: (c) different elastic modes of director deformations – splay, twist and bend – with the direction of the active force generated by the splay and bend distortions, (d) chiral structure of the director field with pitch length $P$, and (e) flow alignment and flow tumbling regime of the director field in shear flow.

![](./images/1017408582175424536_3.jpg)

Fig. 2 | Dynamics of three-dimensional active nematic turbulence for extensile and contractile materials at different aligning parameters. a Cross-section of the velocity field magnitude (color map) and the director field (black rods) at two different activities ($\zeta = 0.2\ L/(\Delta x)^2$ and $\zeta = -0.2\ L/(\Delta x)^2$) and two different alignment parameters ($\chi = 0.2$ and $\chi = 1.5$). b, c Defect density and volume-averaged root mean square velocity over time in a dynamic steady state for activity $\zeta = 0.1\ L/(\Delta x)^2$ and different alignment parameters, with the lowest plotted value of $\chi = 0.0$ in dark blue colour and the highest value of $\chi = 2.0$ in the dark red colour. d, e The dependence of the mean defect density and the mean velocity on the alignment parameter $\chi$. For $\zeta = 0.1(\Delta x)^2$, the mean defect density and the mean velocity are directly computed from panels (b) and (c), respectively. The mean defect density decreases with the alignment parameter for extensile and contractile materials. The mean velocity shows an increasing trend with the alignment parameter for extensile materials ($\zeta > 0$) and a decreasing trend for contractile materials ($\zeta < 0$). Error bars in (d, e) represent the standard deviation originated by the time-averaged defect density and root mean square velocity, respectively.

Figure 3 shows the defect density and mean square velocity when varying the magnitude of the average elastic constant. We observe that in 3D active turbulence, the mean inverse defect density increases with increasing average Frank elastic constant $\overline{K}$ (Fig. 3a), in agreement with the scaling of $\rho \sim \frac{|\zeta|\gamma_1}{\eta\overline{K}}$, predicted by considering the role of defect density on the line tension, drag force, and defect self-propulsion $^{24}$, where $\gamma_1$ is the rotational viscosity and $\eta$ the effective isotropic viscosity. Likewise, the mean square velocity (Fig. 3b) also shows a slowly increasing trend with the average elastic constant, in line with the scaling $\langle v^2 \rangle \propto |\zeta|\overline{K}$, obtained by considering the self-propulsion velocity $^{19,35}$ in the tubular neighborhood of a disclination with a radial size of $\sim 1/\sqrt{\rho}$. The observed behaviour is in agreement with results from two-dimensional active turbulence, where the inverse defect density and the mean square velocity are also reported to be proportional to the magnitude of the elastic constant $^{29,36}$.

Figure 4 shows the role of elastic anisotropy between the splay ($K_1$), twist ($K_2$) and bend ($K_3$) modes. We change the three elastic constants under the assumption of a fixed average elastic constant $\overline{K} = (K_1 + K_2 + K_3)/3$ (see also Methods). Different values of the elastic constants provide relatively comparable results as seen on colormaps for the mean defect density in Fig. 4a and mean velocity in Fig. 4b. The results in Fig. 4c show that the elastic anisotropy in the considered range has little effect on the dynamics of the active turbulence since both mean defect density and mean velocity stay roughly equal under the condition of same $\overline{K}$. With the condition of equal splay and twist modes ($K_1 = K_2$, in Fig. 4c, a slight increasing trend of the defect density is observed with increasing $K_1$ and $K_2$ and decreasing $K_3$. Figure 4d shows the role of anisotropy between splay and bend elastic constants for extensile and contractile systems. For extensile systems, a weakly increasing trend of mean defect density with increasing splay elastic constant can be observed. Contrary, for contractile active nematics, defect density gradually decreases with increasing $K_1$ at constant average Frank elastic constant. The main difference between extensile and contractile nematics is that the mean velocity is approximately 2-times larger in extensile systems for the same absolute value of activity. Similar behaviour was observed also in 2D active nematics $^{29}$.

### Chiral active turbulence and transition to active blue phase
Material chirality in nematic systems can emerge as a result of chiral nematic building blocks, chiral dopants, or-in active systems-as a results of chiral dynamics of the active agents $^{25,26}$. In bulk 3D chiral active nematic, the intrinsic chirality increases the defect density and reduces the mean square velocity of active turbulence, notably already in the low chirality (i.e. large pitch) regime, as shown in Fig. 5. For example, for the chiral pitch equal to $p_0 = 200\ \Delta x$ (i.e. 89-times the active length $l_{\mathrm{a}} = \sqrt{L/\zeta}$) at activity $\zeta = 0.2\ L/(\Delta x)^2$, the defect density is increased by 48% and the root mean square velocity decreased by 42% compared to the dynamic steady state value for achiral active turbulence (Fig. 2(d, e)). The effect of intrinsic chirality on defect density and mean square velocity is larger than the variation of $\sim 30$ % that was observed for elastic anisotropy in Fig. 4. One possible explanation is that for elastic anisotropy in Fig. 4, the elastic deformation modes are energetically unfavorable; however, for intrinsic chirality in Fig. 5 nematic twist distortions are energetically preferred, which can have a greater effect on the emerged structure.

Upon further increasing chirality (i.e. reducing pitch) the passive chiral nematic is known to transition into 3D chiral orientational structures known as chiral blue phases I, II and III, and we observe a similar transition in active chiral nematics. Increasing chirality at fixed activity causes a steady increase of the defect density (Fig. 5d, f, g), up to a structure where defect lines of the active turbulence jam into a defect network, that one could identify as an effective active blue phase III (Fig. 5a, first panel). Similarly as for the passive blue phase III $^{37}$, structural factor shows that the disclination network in active blue phase has no crystal-like order (Fig. 5c). Specifically, in active blue phase at pitch $p_0 = 25\ \Delta x$ and $\zeta = 0.2\ L/(\Delta x)^2$, the defect density is 5-times larger than in achiral nematic turbulence case (Fig. 2d). An even stronger indication of an effective structural transition is the root mean square velocity (Fig. 5e, h, i) that drops to 2% compared to the achiral case at $\zeta = 0.2\ L/(\Delta x)^2$. For the numerical material parameters of our simulation, the transition to a passive blue phase is observed at a critical pitch length $P_c \approx 40\ \Delta x$. Activity reduces this critical pitch length to $P_c = 34\ \Delta x$ at $\zeta = 0.15\ L/(\Delta x)^2$ and even further to $P_c = 32\ \Delta x$ at $\zeta = 0.2\ L/(\Delta x)^2$. How $P_c$ is obtained from the data is explained in Methods.

![](./images/1017408582175424536_4.jpg)

Fig. 3 | Defect density and mean square velocity as dependent on the average elastic constant. a Steady state mean inverse defect density and (b) steady state mean inverse velocity squared, both for three different activities. The average elastic constant is expressed in units of $K_0$ and is computed for different twist vs splay and bend elastic constants (see Methods). Error bars represent the standard deviation originated by the time-averaged quantities.

The mean square velocity drop-off and effective jamming of the disclination network can be explained by the difference of the structural features of the disclination network between active blue phase and active turbulence, as shown in Fig. 5b. The local director cross-section profile of the disclination lines in the active blue phase are close to the $-1/2$ winding number, for which the active self-propulsion is well known to be zero¹⁹. Selected double-twist cylinders are also shown in Fig. 5b, which also do not generate a self-propulsion flow³⁸. Nodal points, where 4 disclination segments meet (Fig. 5b), are further characteristic features of the blue phase III³⁷. Dynamically, we observe that in the active blue phase at $P_0=25\Delta x$, the nodal points are stable for up to $\sim150(\Delta x)^2/\Gamma L$. Contrary, in the active chiral turbulence, nodal points appear during reconfiguration events between disclination lines and are much shorter lived - at $P_0=150\Delta x$ each nodal point disappears on average after approximately $\sim13(\Delta x)^2/\Gamma L$.

We observe the distinct scaling of the disclination density and the mean square velocity near the transition between the active blue phase and the active turbulence. In Fig. 5d, e, we plot the inverse defect density and root mean square velocity dependence on the pitch length in proximity of the critical defect density $\rho_c$, critical mean velocity $v_c$ and critical chiral pitch $P_c$ of the blue phase-active turbulence transition. The slope of the graph shows that inverse defect density scales roughly as $(P_0-P_c)^{0.6}$ and mean velocity as $(P_0-P_c)^{0.3}$. Similar scaling is obtained for two different activities with a notable difference that at higher activity the blue phase-active turbulence transition occurs at smaller pitch lengths.

## Conclusions
We explore dynamic reconfiguring network of disclination lines known as active turbulence using numerical simulations for selected main material parameters: chirality, flow alignement (anistropic viscosity), and elastic anistropy (different nematic elastic constants). The difference between extensile and contractile systems is observed in increasing or decreasing dependence of mean square velocity with the alignment parameter, showing the importance of the shape of active nematic building blocks³⁹. We confirm that defect density and mean square velocity are approximately inversely proportional to the magnitude of the average elastic constant, whereas the elastic anisotropy has only a small effect on the defect density and the mean square velocity of active turbulence. Though, we speculate that elastic anisotropy could affect the local structure of the defect lines $(+1/2,-1/2$ and twisted¹⁹) in the defect network. As the elastic instability is known to drive structural reconfigurations in passive liquid crystals⁴⁰, we expect that for active nematics elastic instability might have a greater effect in confined systems at the onset of active turbulence. While current experiments on 3D active turbulence explore bulk behaviour¹⁵, the role of elastic anisotropy and alignment parameter is relevant also for possible future results in confined systems.

We performed simulations of an active chiral nematic and show the effective structural transition between chiral active turbulence and the active blue phase. The structures are distinct from each other and are separated by a continuous structural phase transition that we characterize by measuring the average inverse defect density and mean square velocity. Beyond the results reported here, the observed active blue phase dynamics would be (i) interesting to compare with blue phase dynamics due to thermal fluctuations⁴¹ and (ii) explored in the context of driving with external field, such as electric or magnetic fields⁴² or activity gradients⁴³. An interesting aspect is also the difference between the transition to active turbulence in blue phases and in modulated cholesteric phase, for which a linear hydrodynamic instability was predicted for extensile materials²⁶. While experimentally engineering 3D active blue phase materials can lead to very novel materials and phenomena, the effects of weak chirality that we show in the paper might be important also for present active nematic materials, since building blocks and processes in active matter are often chiral²⁵,²⁶, which could be even further amplified by introduction of chiral dopants. Additionally, chiral symmetry breaking allows for additional active stresses⁴⁴⁻⁴⁷. An open problem for future research is also the possibility of an active blue phase with symmetries of blue phase I or blue phase II⁴⁸.

More generally, this work is a contribution towards understanding the material-dependence of active nematic turbulence, to aid the experimental design and theoretical advances of active nematic phase⁴⁹⁻⁵¹.

## Methods
### Model equations of active nematodynamics
We simulate mesoscopic continuum description of active nematics using the adapted Beris-Edwards approach for active nematodynamics³⁰,³²,⁵². The nematic order is described by a traceless tensor order parameter $Q_{ij}$, with the director $\mathbf{n}$ as the main eigenvector, and evolves as

$$
\left(\partial_t + v_k\partial_k\right)Q_{ij}-S_{ij}=\Gamma H_{ij}, \tag{1}
$$

where $\mathbf{v}$ is the fluid velocity and $\Gamma$ is the rotational viscosity coefficient. The generalized advection term $S_{ij}$ couples the nematic order and fluid velocity

$$
\begin{aligned}
S_{ij} &= \left(\chi D_{ik}-\Omega_{ik}\right)\left(Q_{kj}+\frac{\delta_{kj}}{3}\right) \\
& \quad + \left(Q_{ik}+\frac{\delta_{ik}}{3}\right)\left(\chi D_{kj}+\Omega_{kj}\right) \\
& \quad - 2\chi\left(Q_{ij}+\frac{\delta_{ij}}{3}\right)Q_{kl}W_{lk},
\end{aligned}
$$

![](./images/1017408582175424536_5.jpg)

where $D_{ij}$ and $\Omega_{ij}$ are symmetric and antisymmetric part of the velocity gradient tensor $W_{ij}=\partial_{i}v_{j}$, and $\chi$ is the alignment parameter. The molecular field $H_{ij}$ drives system towards equilibrium of $Q_{ij}$

$$
H_{ij}=-\frac{\delta F}{\delta Q_{ij}}+\frac{\delta_{ij}}{3}\operatorname{Tr}\frac{\delta F}{\delta Q_{ij}},
$$

where $F$ is the Landau-de Gennes free energy

$$
\begin{aligned}
F= & \int\left(\frac{A}{2} Q_{ij} Q_{ji}+\frac{B}{3} Q_{ij} Q_{jk} Q_{ki}+\frac{C}{4}\left(Q_{ij} Q_{ji}\right)^{2}\right. \\
& +\frac{1}{2} L_{1}\left(\partial_{k} Q_{ij}\right)\left(\partial_{k} Q_{ji}\right)+\frac{1}{2} L_{2}\left(\partial_{i} Q_{jk}\right)\left(\partial_{j} Q_{ik}\right) \\
& \left.+\frac{1}{2} L_{3} Q_{ij}\left(\partial_{i} Q_{kl}\right)\left(\partial_{j} Q_{kl}\right)+2 L_{1} q_{0} \epsilon_{ikl} Q_{ij}\left(\partial_{k} Q_{lj}\right)\right) \mathrm{d} V.
\end{aligned}
$$

Here, $A, B$ and $C$ are material parameters and $L_{1}, L_{2}$, and $L_{3}$ are elastic constants in the tensorial formulation of the elastic free energy, and $q_{0}=2 \pi / P_{0}$ is the inverse chiral pitch. $L_{1}, L_{2}$, and $L_{3}$ can be computed from the elastic constants of the splay $K_{1}$, twist $K_{2}$, and bend $K_{3}$ deformation modes that are formulated within the director-based Frank free energy.

Often, single elastic constant approximation $(L_{1}=L, L_{2}=L_{3}=0)$ is used, where splay, twist and bend elastic modes have equal contributions $(K_{1}=K_{2}=K_{3}=K)$. In Figs. 3 and 4, we explore the role of elastic anistropy, i.e. how individual elastic modes influence the active nematic dynamics and we use non-zero $L_{1}, L_{2}$ and $L_{3}$ elastic constants, following the relations

$$
\begin{aligned}
& L_{1}=\frac{2}{27 S^{2}}\left(-K_{1}+3 K_{2}+K_{3}\right), \\
& L_{2}=\frac{4}{9 S^{2}}\left(K_{1}-K_{2}\right), \\
& L_{3}=\frac{4}{27 S^{3}}\left(-K_{1}+K_{3}\right).
\end{aligned} \tag{2}
$$

In the formulation of the elastic constants in Eq. (2), $K_{24}$ is equal to $\frac{K_{1}}{2}$ but is not relevant due to periodic boundary conditions. The flow field obeys the incompressibility condition and the Navier-Stokes equation,

$$
\partial_{i} v_{i}=0, \tag{3}
$$

$$
\rho\left(\partial_{t}+v_{j} \partial_{j}\right) v_{i}=\partial_{j} \Pi_{i j}, \tag{4}
$$

![](./images/1017408582175424536_6.jpg)

Fig. 5 | Chiral active turbulence and active blue phase. a Defect network at three different values of chiral pitch $P_0$. b Zoom of defect network at two different values of chiral pitch $P_0$, with cross-section of director field in red. c Structure factor $|S(\mathbf{k})|^2$ at two different values of chiral pitch $P_0$, on cuts along $k_y=0$. The structure factor was calculated from the Fourier transformation of the highest eigenvalue of the Q-tensor.
d Mean inverse defect density dependence on the chiral pitch $P_0$ for three different activities. Dashed line shows the value of the transition in a passive nematic at $P_c\approx40\Delta x$. e Root mean square velocity dependence on the chiral pitch $P_0$. f, h A zoomed-in area of mean inverse defect density and root mean square velocity from $P_0=25\Delta x$ to $P_0=60\Delta x$. (g, i) Log-log plot of mean inverse defect density and root mean square velocity, respectively. The data in the log-log plots is plotted relative to the critical pitch length $P_c$ and the critical defect density. The values of $P_c=32\Delta x$ and $1/\rho_c=160\Delta x$ were chosen for the activity $\zeta=0.2\ L/(\Delta x)^2$, and the values of $P_c=34\Delta x$ and $1/\rho_c=170\Delta x$ for the activity $\zeta=0.15\ L/(\Delta x)^2$. The dashed line in g has a slope of $x^{0.6}$ and the dashed line in (i) a slope of $x^{0.3}$. Error bars in (d-i) represent the standard deviation originated by the time-averaged quantities.

where $\rho$ is the fluid density and $\Pi_{ij}$ is the stress tensor, which consists a passive and an active term $\Pi_{ij}=\Pi_{ij}^{\text{passive}}+\Pi_{ij}^{\text{active}}$, where

$$
\Pi_{ij}^{\text{passive}}=-p \delta_{ij}+2 \eta D_{ij}+2 \chi\left(Q_{ij}+\frac{\delta_{ij}}{3}\right) Q_{kl} H_{kl} \tag{5}
$$

$$
-\chi H_{ik}\left(Q_{kj}+\frac{\delta_{kj}}{3}\right)-\chi\left(Q_{ik}+\frac{\delta_{ik}}{3}\right) H_{kj} \tag{6}
$$

$$
+Q_{ik} H_{kj}-H_{ik} Q_{kj}-\partial_{i} Q_{k l} \frac{\delta F}{\partial \jmath Q_{k l}}, \tag{7}
$$

$$
\Pi_{ij}^{\text{active}}=-\zeta Q_{ij}. \tag{8}
$$

Here, $p$ is the fluid pressure, $\eta$ is the isotropic viscosity, $\chi$ is the flow alignment parameter and $\zeta$ is the activity, which is positive in extensile materials and negative in contractile materials.

The coupled equations for the nematic order $Q_{ij}$ and fluid velocity $v_{i}$ are numerically solved using the hybrid lattice-Boltzmann approach $^{17,24,29-32}$, based on the finite difference method for solving the Q-tensor evolution (Eq. (1)), and the D3Q19 lattice Boltzmann method for the incompressibility and the Navier-Stokes equation (Eqs. (3), (4)).

### Material parameters

In the paper, we consider a single elastic constant approximation for the material constants $(L_{1} \neq 0, L_{2}=0$, and $L_{3}=0)$, except in Figs. 3 and 4 . Changing the values of the elastic constants affects the nematic correlation length and in turn the resolution of the numerical mesh resolution. Accordingly, we compute the average Frank elastic constant

$$
\bar{K}=\frac{1}{3}\left(K_{1}+K_{2}+K_{3}\right)=\frac{9 S^{2}}{2}\left(L_{1}+\frac{L_{2}}{3}\right)
$$

from the mapping in Eq. (2). To account for simulation results at different values of $\bar{K}$ in Fig. 3, we set $L_{1}=L$, vary the elastic constant $L_{2}$, and express the simulation results with a constant term $K_{0}=\frac{9 S_{\text {eq }}^{2}}{2} L$. Here, $L$ represents the fixed value of the elastic constant as used in Figs. 2 and 5. In Fig. 4, where we explore the role of the elastic anisotropy, we use the condition of a constant average Frank elastic constant $\bar{K}$ and choose the Frank elastic constants accordingly and express the simulation results in terms of $K_{0}$. From a given set of the Frank elastic constants, the tensorial elastic constants $L_{1}, L_{2}$, and $L_{3}$ are determined from a mapping given by Eq. (2) evaluated at $S=S_{\text {eq. }}$.

Using the alignment parameter $\chi$, rotational viscosity parameter $\Gamma$ and isotropic viscosity $\eta$ from the Beris-Edwards model of nematodynamics (Eqs. (1), (7)), we can express the Ericksen-Leslie viscosity parameters $^{33,53}$ that are typically formulated within the director-based approach to nematodynamics:

$$
\alpha_{1}=\frac{\chi^{2}}{\Gamma} \frac{9 S^{2}}{2}\left(3 S^{2}-2 S-1\right),
$$

$$
\alpha_{2}=-\frac{\chi}{\Gamma} \frac{S}{4}(3 S+4)-\frac{1}{\Gamma} \frac{9 S^{2}}{4},
$$

$$
\alpha_{3}=-\frac{\chi}{\Gamma} \frac{S}{4}(3 S+4)+\frac{1}{\Gamma} \frac{9 S^{2}}{4},
$$

$$
\alpha_{4}=\frac{\chi^{2}}{\Gamma}\left(S-\frac{2}{3}\right)^{2}+2 \eta,
$$

$$
\alpha_{5}=-\frac{\chi^{2}}{\Gamma} \frac{S}{4}(3 S-8)+\frac{\chi}{\Gamma} \frac{S}{4}(3 S+4),
$$

$$
\alpha_{6}=-\frac{\chi^{2}}{\Gamma} \frac{S}{4}(3 S-8)-\frac{\chi}{\Gamma} \frac{S}{4}(3 S+4).
$$

The flow-alignment parameter $\lambda$ in the director-based formulation then reads as $\lambda=\frac{\alpha_{2}+\alpha_{3}}{\alpha_{2}-\alpha_{3}}=\frac{3 S+4}{9 S} \chi$ and the flow-aligning to flow-tumbling transition occurs at $\lambda=1^{33}$.

The overall results of the simulations are expressed in the units of the elastic constant $L$, rotational viscosity parameter $\Gamma$ and mesh resolution $\Delta x$. Mesh resolution is defined as $\Delta x=1.5 \chi_{\mathrm{n}}$, where $\chi_{\mathrm{n}}$ is nematic correlation length defined as $\chi_{\mathrm{n}}=\sqrt{L /\left(A+B S_{\mathrm{eq}}+\frac{9}{2} C S_{\mathrm{eq}}^{2}\right)}$, where $S_{\mathrm{eq}}=0.533$ is equilibrium degree of nematic order, $A=-0.43 L /(\Delta x)^{2}, B=-5.3 L /(\Delta x)^{2}, C=4.325 L /(\Delta x)^{2}$ and $\eta=1.38 / \Gamma$. The size of the simulation box is $201 \times 201 \times 201$ mesh points and periodic boundary conditions are used in all three spatial directions. $200 \times 200 \times 200$ simulation box is used in Fig. 2. The time step in simulations is set to $\Delta t=0.025(\Delta x)^{2} /(L \Gamma)$. To recover the simulation results in the SI units, one can use typical parameter values for active systems $L=3 \mathrm{pN}, \Delta x=2 \mu \mathrm{m}$, and $\Gamma=10(\mathrm{~Pa} \mathrm{~s})^{-1}$, roughly estimated from active turbulence in bacterial and microtubule systems $^{2,54}$ and viscoelastic properties of lyotropic nematics $^{55}$.

### Data analysis

We define the defect density as the length of defect lines over a unit volume and compute it from the defect volume fraction of the regions where scalar order parameter is $S<0.4^{24}$. In the next analysis step, we average either the defect density (Figs. 2 and 4) or the inverse defect density (Figs. 3 and 5) in time and calculate its standard deviation that is presented with error bars. For the velocity field, we compute the average of the velocity squared $\left\langle v^{2}\right\rangle_{V}$ over the complete simulation volume $V$ at given time. In Figs. 2, 4, and 5, we obtain the root mean square velocity as $\langle v\rangle=\sqrt{\left\langle v^{2}\right\rangle_{V}}$ and the variability (presented by error bars) from its standard deviation. In Fig. 3, the mean inverse velocity squared $\left\langle 1 / v^{2}\right\rangle$ and its standard deviation are obtained from the time-dependence of the $1 /\left\langle v^{2}\right\rangle_{V}$. To estimate the value of the critical pitch for the transition from the active chiral turbulence to the active blue phase, we performed nonlinear regression on simulation data for mean velocity and mean inverse defect density in Fig. 5. The value of $P_{\mathrm{c}}$ with the precision of $1 \Delta x$ was determined so that the mean velocity in the log-log plot (Fig. 5i) shows a power-law scaling for the longest range of the pitch values. Once $P_{\mathrm{c}}$ was set, we employed a similar procedure to determine $1 / \rho_{\mathrm{c}}$ based on the log-log plot of the mean inverse defect density (Fig. $5 \mathrm{~g}$ ).

### Data availability

The data sets generated in this study are available from the corresponding author upon reasonable request.

### Code availability

The code used in this study is available from the corresponding author upon reasonable request.

Received: 5 January 2024; Accepted: 26 June 2024;
Published online: 07 July 2024

### References

1. Shankar, S., Souslov, A., Bowick, M. J., Marchetti, M. C. & Vitelli, V. Topological active matter. *Nat. Rev. Phys.* **4**, 380 (2022).
2. Sanchez, T., Chen, D. T. N., DeCamp, S. J., Heymann, M. & Dogic, Z. Spontaneous motion in hierarchically assembled active matter. *Nature* **491**, 431 (2012).
3. Wensink, H. H. et al. Meso-scale turbulence in living fluids. *Proc. Natl Acad. Sci.* **109**, 14308 (2012).
4. Hardoüin, J., Laurent, J., Lopez-Leon, T., Ignés-Mullol, J. & Sagués, F. Active microfluidic transport in two-dimensional handlebodies. *Soft Matter* **16**, 9230 (2020).
5. Wittmann, R., Nguyen, G. P., Löwen, H., Schwarzendahl, F. J. & Sengupta, A. Collective mechano-response dynamically tunes cell-size distributions in growing bacterial colonies. *Commun. Phys.* **6**, 331 (2023).

https://doi.org/10.1038/s42005-024-01720-0

6.  Peng, C., Turiv, T., Guo, Y., Wei, Q.-H. & Lavrentovich, O. D. Command of active matter by topological defects and patterns. *Science* **354**, 882 (2016).

7.  Sokolov, A., Aranson, I. S., Kessler, J. O. & Goldstein, R. E. Concentration dependence of the collective dynamics of swimming bacteria. *Phys. Rev. Lett.* **98**, 158102 (2007).

8.  Dombrowski, C., Cisneros, L., Chatkaew, S., Goldstein, R. E. & Kessler, J. O. Self-concentration and large-scale coherence in bacterial dynamics. *Phys. Rev. Lett.* **93**, 098103 (2004).

9.  Kokot, G. et al. Active turbulence in a gas of self-assembled spinners. *Proc. Natl Acad. Sci.* **114**, 12870 (2017).

10. Karani, H., Pradillo, G. E. & Vlahovska, P. M. Tuning the random walk of active colloids: From individual run-and-tumble to dynamic clustering. *Phys. Rev. Lett.* **123**, 208002 (2019).

11. Hatwalne, Y., Ramaswamy, S., Rao, M. & Simha, R. Rheology of Active-Particle Suspensions. *Phys. Rev. Lett.* **92**, 118101 (2004).

12. Voituriez, R., Joanny, J. F. & Prost, J. Spontaneous flow transition in active polar gels. *Europhys. Lett.* **70**, 404 (2005).

13. Alert, R., Casademunt, J. & Joanny, J.-F. Active Turbulence. *Annu. Rev. Condens. Matter Phys.*13 (2022).

14. Head, L. C. et al. Spontaneous self-constraint in active nematic flows. *Nat. Phys.* **20**, 492 (2024)

15. Duclos, G. et al. Topological structure and dynamics of three- dimensional active nematics. *Science* **367**, 1120 (2020).

16. Urzay, J., Doostmohammadi, A. & Yeomans, J. M. Multi-scale statistics of turbulence motorized by active matter. *J. Fluid Mech.* **822**, 762 (2017).

17. Krajnik, Ž., Kos, Ž. & Ravnik, M. Spectral energy analysis of bulk three- dimensional active nematic turbulence. *Soft Matter* **16**, 9059 (2020).

18. Singh, A., Suhrcke, P. H., Incardona, P. & Sbalzarini, I. F. A numerical solver for active hydrodynamics in three dimensions and its application to active turbulence. *Phys. Fluids* **35**, 105155 (2023).

19. Binysh, J., Kos, Ž., Čopar, S., Ravnik, M. & Alexander, G. P. Three- dimensional Active Defect Loops. *Phys. Rev. Lett.* **124**, 257 (2020).

20. Long, C., Tang, X., Selinger, R. L. B. & Selinger, J. V. Geometry and mechanics of disclination lines in 3d nematic liquid crystals. *Soft Matter* **17**, 2265 (2021).

21. Houston, A. J. & Alexander, G. P. Defect loops in three-dimensional active nematics as active multipoles. *Phys. Rev. E* **105**, L062601 (2022).

22. Romeo, N., Słomka, J., Dunkel, J. & Burns, K. J. Vortex line entanglement in active beltrami flows. *J. Fluid Mech.* **982**, A12 (2024).

23. Digregorio, P., Rorai, C., Pagonabarraga, I. & Toschi, F. Coexistence of Defect Morphologies in Three-Dimensional Active Nematics. *Phys. Rev. Lett.* **132**, 258301 (2024).

24. Kralj, N., Ravnik, M. & Kos, Ž. Defect line coarsening and refinement in active nematics. *Phys. Rev. Lett.* **130**, 128101 (2023).

25. Fürthauer, S., Strempel, M., Grill, S. W. & Jülicher, F. Active chiral fluids. *Eur. Phys. J. E* **35**, 1 (2012).

26. Whitfield, C. A. et al. Hydrodynamic instabilities in active cholesteric liquid crystals. *Eur. Phys. J. E* **40**, 1 (2017).

27. Giomi, L. Geometry and topology of turbulence in active nematics. *Phys. Rev. X* **5**, 031003 (2015).

28. Alert, R., Joanny, J.-F. & Casademunt, J. Universal scaling of active nematic turbulence. *Nat. Phys.* **16**, 682 (2020).

29. Thampi, S. P., Golestanian, R. & Yeomans, J. M. Vorticity, defects and correlations in active turbulence. *Philos. Trans. R. Soc. A: Math., Phys. Eng. Sci.* **372**, 20130366 (2014).

30. Carenza, L. N., Gonnella, G., Marenduzzo, D. & Negro, G. Rotation and propulsion in 3d active chiral droplets. *Proc. Natl Acad. Sci.* **116**, 22065 (2019).

31. Zhang, R., Zhou, Y., Rahimi, M. & de Pablo, J. J. Dynamic structure of active nematic shells. *Nat. Commun.* **7**, 13483 (2016).

32. Čopar, S., Aplinc, J., Kos, Ž., Žumer, S. & Ravnik, M. Topology of Three-Dimensional Active Nematic Turbulence Confined to Droplets. *Phys. Rev. X* **9**, 031051 (2019).

33. de Gennes P. G. & Prost, J. *Physics of Liquid Crystals* [PDF] (Clarendon Press, Clarendon Press, 1993).

34. Thijssen, K., Metselaar, L., Yeomans, J. M. & Doostmohammadi, A. Active nematics with anisotropic friction: The decisive role of the flow aligning parameter. *Soft Matter* **16**, 2065 (2020).

35. Giomi, L., Bowick, M. J., Mishra, P., Sknepnek, R. & Marchetti, M. C. Defect dynamics in active nematics. *Philos. Trans. R. Soc. A* **372**, 20130365 (2014).

36. Hemingway, E. J., Mishra, P., Marchetti, M. C. & Fielding, S. M. Correlation lengths in hydrodynamic models of active nematics. *Soft Matter* **12**, 7943 (2016).

37. Henrich, O., Stratford, K., Cates, M. & Marenduzzo, D. Structure of blue phase iii of cholesteric liquid crystals. *Phys. Rev. Lett.* **106**, 107801 (2011).

38. Metselaar, L., Doostmohammadi, A. & Yeomans, J. M. Topological states in chiral active matter: Dynamic blue phases and active half- skyrmions. *J. Chem. Phys.* **150** (2019).

39. Brand, H. & Pleiner, H. Theory of flow alignment in biaxial nematics and nematic discotics. *J. de. Phys.* **43**, 853 (1982).

40. Lavrentovich, O. D. Splay-bend elastic inequalities shape tactoids, toroids, umbilics, and conic section walls in paraelectric, twist-bend, and ferroelectric nematics. *Liq. Cryst. Rev.* **12**, 1 (2024).

41. Pišljar, J. et al. Blue phase iii: topological fluid of skyrmions. *Phys. Rev. X* **12**, 011003 (2022).

42. Kikuchi, H., Hisakado, Y., Uchida, K., Nagamura, T. & Kajiyama, T. Fast electro-optical effect in polymer-stabilized blue phases, in *Liquid Crystals VIII*, Vol. 5518 (SPIE, 2004) pp. 182–189.

43. Shankar, S., Scharrer, L. V. D., Bowick, M. J., & Marchetti, M. C. Design rules for controlling active topological defects. *Proc. Natl Acad. Sci.* **121**, e2400933121 (2024).

44. Kole, S., Alexander, G. P., Ramaswamy, S. & Maitra, A. Layered chiral active matter: beyond odd elasticity. *Phys. Rev. Lett.* **126**, 248001 (2021).

45. Maitra, A., Lenz, M. & Voituriez, R. Chiral active hexatics: Giant number fluctuations, waves, and destruction of order. *Phys. Rev. Lett.* **125**, 238005 (2020).

46. Hoffmann, L. A., Schakenraad, K., Merks, R. M. & Giomi, L. Chiral stresses in nematic cell monolayers. *Soft matter* **16**, 764 (2020).

47. Markovich, T., Tjhung, E. & Cates, M. E. Chiral active matter: microscopic 'torque dipoles' have more than one hydrodynamic description. *N. J. Phys.* **21**, 112001 (2019).

48. Yamashita, A. & Fukuda, J.-i. et al. Structure of twin boundaries of cholesteric blue phase i. *Phys. Rev. E* **105**, 044702 (2022).

49. Skogvoll, V., Rønning, J., Salvalaglio, M. & Angeluta, L. A unified field theory of topological defects and non-linear local excitations. *npj Comput. Mater.* **9**, 122 (2023).

50. Pratley, V. J., Caf, E., Ravnik, M. & Alexander, G. P. Three-dimensional spontaneous flow transition in a homeotropic active nematic. *Commun. Phys.* **7**, 127 (2024).

51. Vélez-Cerón, I., Guillamat, P., Sagués, F. & Ignés-Mullol, J. Probing active nematics with in-situ microfabricated elastic inclusions. *Proc. Natl Acad. Sci.* **121**, e2312494121 (2024).

52. Doostmohammadi, A., Ignés-Mullol, J., Yeomans, J. M. & Sagués, F. Active nematics. *Nat. Commun.* **9**, 045006 (2018).

53. Denniston, C., Orlandini, E. & Yeomans, J. Lattice boltzmann simulations of liquid crystal hydrodynamics. *Phys. Rev. E* **63**, 056702 (2001).

54. Wolgemuth, C. W. Collective Swimming and the Dynamics of Bacterial Turbulence. *Biophys. J.* **95**, 1564 (2008).

55. Zhang, R., Kumar, N., Ross, J. L., Gardel, M. L. & De Pablo, J. J. Interplay of structure, elasticity, and dynamics in actin-based nematic materials. *Proc. Natl Acad. Sci.* **115**, E124 (2018).

Communications Physics | (2024)7:222

https://doi.org/10.1038/s42005-024-01720-8

# Acknowledgements
The authors acknowledge funding from Slovenian Research and Innovation Agency (ARIS) under contracts P1-0099, J1-50006, J1-2462, N1-0195. This result is also part of a project that has received funding from the European Research Council (ERC) under the European Union's Horizon 2020 Research and Innovation Program (Grant Agreement No. 884928-LOGOS).

# Author contributions
N.K. performed the numerical simulations and the analysis. M.R. and Ž.K. designed and supervised the research. All authors contributed to the writing of the manuscript.

# Competing interests
The authors declare no competing interests.

# Additional information
Correspondence and requests for materials should be addressed to Žiga Kos.

Peer review information *Communications Physics* thanks Livio Nicola Carenza and the other, anonymous, reviewer(s) for their contribution to the peer review of this work.

Reprints and permissions information is available at http://www.nature.com/reprints

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.

© The Author(s) 2024

---
*Communications Physics*| (2024)7:222
9
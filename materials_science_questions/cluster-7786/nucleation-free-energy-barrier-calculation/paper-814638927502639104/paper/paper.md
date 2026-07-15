![](./images/814638927502639104_1.jpg)
![](./images/814638927502639104_2.jpg)

Available online at www.sciencedirect.com

# ScienceDirect
Acta Materialia 91 (2015) 365-376

![](./images/814638927502639104_3.jpg)
www.elsevier.com/locate/actamat

# Modelling the role of compositional fluctuations in nucleation kinetics

J. Ženíšek, $^{a}$ E. Kozeschnik, $^{a,b}$ J. Svoboda $^{c}$ and F.D. Fischer $^{d,*}$

$^{a}$ Materials Center Leoben Forschung GmbH, Roseggerstrasse 12, 8700 Leoben, Austria
$^{b}$ Institute of Materials Science and Technology, Vienna University of Technology, Favoritenstrasse 9-11/E308, 1040 Vienna, Austria
$^{c}$ Institute of Physics of Materials, Academy of Science of the Czech Republic, Žižkova 22, 616 62 Brno, Czech Republic
$^{d}$ Institute of Mechanics, Montanuniversität Leoben, Franz-Josef-Strasse 18, 8700 Leoben, Austria

Received 31 July 2014; revised 10 December 2014; accepted 17 December 2014
Available online 23 March 2015

Abstract-The classical nucleation theory of precipitate nucleation in interstitial/substitutional alloys is applied to account for the influence of spatial A-B composition fluctuations in an A-B-C matrix on the kinetics of nucleation of $(A,B)_3C$ precipitates. A and B are substitutional elements in the matrix and C is an interstitial component, assumed to preferentially bind to B atoms. All lattice sites are considered as potential nucleation sites. The fluctuations of chemical composition result in a local variation of the nucleation probability. The nucleation sites are eliminated from the system if they are located in a C-depleted diffusion zone belonging to an already nucleated and growing precipitate. The chemistry is that of an Fe-Cr-C sys- tem, and the specific interface energy is treated as a free parameter. Random, regular and homogeneous A-B distributions in the matrix are simulated and compared for various values of the interface energy. An increasing enhancement of the role of compositional fluctuations on nucleation kinetics with increasing interface energy and decreasing chemical driving force is observed.
© 2014 Acta Materialia Inc. Published by Elsevier Ltd. All rights reserved.

Keywords: Kinetics; Nucleation and growth; Precipitates; Interface energy; Fluctuations of chemical composition

## 1. Introduction

Precipitation is understood as the formation of particles of a new phase from a supersaturated solid solution. The first stage of precipitation is nucleation, usually described by classical nucleation theory (CNT) developed by Becker and Döring [1], which follows also from the solution of the Fokker-Planck equation derived by means of the clus- ter dynamics (CD) method; for details see, for example, Refs. [2-4]. Nucleation consists of the following periods:

(i) the incubation period, providing the necessary time for formation of the critical nucleus by diffusion of components to the nucleation centre;
(ii) the steady state nucleation period, during which the nucleation conditions and the nucleation rate change insignificantly;
(iii) the period during which the nucleation rate is decreasing due to exhaustion of potential nucleation sites and/or a decrease of the supersaturation of the matrix, causing a decrease of the driving force for nucleation.

The second stage of precipitation is the growth stage, followed by the third stage, which is coarsening [5,6].

It is also possible to model nucleation directly by the CD method, which allows treating the evolution of a single cluster or an ensemble of clusters in size space [7,8]. CD models assume that the size of a cluster fluctuates due to absorption and desorption of atoms from the surrounding matrix. Some CD studies of nucleation and growth of pre- cipitates can be found, for example, in Refs. [9-11]. A study of critical nuclei, where also the composition dependence of the interface energy is accounted for, can be found, for example, in Ref. [12].

Atomistic Monte Carlo (MC) methods represent an alternative approach for studying precipitation [13-16]. Since the atomistic MC methods naturally include fluctua- tions of composition at the atomic level, they can give more detailed information about the initial stages of precipitation compared to CNT or CD methods. There exist, however, also some shortcomings in application of the MC technique to the modelling of precipitation. First, the system is usu- ally described by a set of inter-atomic interaction coeffi- cients, which do not allow a free choice of the interface energy between cluster and matrix. Second, there is obviously no clear definition of a cluster representing a pre- cipitate in the nucleation or early growth stage [17]. If not stated explicitly, a cluster is usually considered as a confine- ment of atoms or molecules with at least one nearest neigh- bour connection. In the treatment based on CD, the cluster approximated by a sphere is well defined and the interface

* Corresponding author; e-mail: mechanik@unileoben.ac.at

http://dx.doi.org/10.1016/j.actamat.2014.12.031
1359-6462/© 2014 Acta Materialia Inc. Published by Elsevier Ltd. All rights reserved.

energy between cluster and matrix can be treated as a free parameter.

Of course, modelling makes it necessary to select a specific material system. The (Cr,Fe)₃C carbide has been chosen as a prototype. This carbide represents also other Cr-rich carbides that nucleate in this alloy system as (Cr,Fe)₇C₃ or (Cr,Fe)₂₃C₆ [18]. These precipitates typically show a more or less pronounced enrichment in Cr, substituting the lattice-forming element Fe of the matrix. The more Cr the matrix contains in the initial state, the more Cr is usually found in the precipitates. Nevertheless, all of these carbides are often thermodynamically stable over the entire composition range from Cr-rich to Fe-rich carbides with a clear kinetic advantage for the Fe-rich precipitates with a composition according to para-equilibrium. In this case the slow Cr diffusion is not required and fast interstitial C diffusion is fully sufficient for nucleation. Then the fluctuations of the chemical composition in Cr can play a key role in nucleation kinetics, and this is the main motivation for the present study. The Fe–Cr–C system, however, serves only as an example of general substitutional-interstitial systems. That is why we generalize the further treatment in an A–B–C formulation. Furthermore, we assume that the nucleation process of the complex carbides mentioned above occurs due to clustering of interstitial C atoms in the crystal structure of the body centred cubic (bcc) matrix. The transformation of the bcc pre-cluster to the final orthorhombic structure of the (A,B)₃C phase is assumed to occur subsequently without a significant delay. This scenario is supported by experimental evidence [19].

In the present paper, we apply CNT locally to each individual substitutional lattice site to study nucleation kinetics of the (A,B)₃C phase in a random, regular or homogeneous A–B–C matrix with A, B being substitutional and C interstitial atoms. The substitutional A atoms are assumed to be the majority species, and the interstitial C atoms are assumed to energetically prefer B atoms. Simulations are performed on a system represented by a box of a bcc lattice with periodic boundary conditions. The arrangement of substitutional A and B atoms in the lattice is either random or regular. Both arrangements are compared with the case of a homogeneous matrix as in classical CNT, supposing that to each lattice site the same chemical composition corresponding to the average composition of the matrix is attributed. Interstitial C atoms are treated on a continuum basis, in order to avoid too high computational effort. To each lattice site, local conditions for nucleation are associated. Para-conditions for nucleation are assumed, which imply that substitutional atoms are immobile; see, for example, Ref. [20]. To account for the influence of the already nucleated and grown precipitates, all lattice sites are excluded as potential nucleation sites, if they are located in the diffusion zones of growing precipitates.

The aim of this paper is to show, within the framework of CNT, how the random spatial fluctuations of A, B atoms affect the nucleation of the (A,B)₃C phase in dependence on interface energy and chemical composition of the alloy. The results of the treatment are compared with those calculated for a regular and homogeneous matrix. This original study provides clear evidence for the role of compositional fluctuations in substitutional elements on the nucleation kinetics. The effect of fluctuation itself on the nucleation kinetics drastically increases with increasing interface energy.

## 2. Classical nucleation theory

According to CNT (see, for example, Refs. [2,3]), the nucleation rate $J$ can be expressed as
$$
\frac{dN}{dt}=J=J^{SS}\exp\left(-\frac{\tau}{t}\right)\frac{N_0-N}{N_0}, \tag{1}
$$
where $N$ is the number of nucleated precipitates, $J^{SS}$ is the steady-state nucleation rate, $t$ is the time, $\tau$ is the incubation time and $N_0$ is the number of potential nucleation sites for precipitates. The steady-state nucleation rate can be written as
$$
J^{SS}=\beta^*N_0\exp\left(-\frac{G^*}{kT}\right), \tag{2}
$$
where $G^*$ is the Gibbs energy barrier to form a critical nucleus (later nucleation barrier), $k$ is the Boltzmann constant and $T$ is the absolute temperature. For spherical precipitates, the nucleation barrier $G^*$ in Eq. (2) is formulated as
$$
G^*=\frac{16\pi}{3}\frac{\gamma^3}{\Delta F^2}, \tag{3}
$$
where $\gamma$ is the specific interface energy and $\Delta F$ is the total chemical and mechanical driving force. The radius $\rho^*$ of the critical nucleus can then be written as
$$
\rho^*=\frac{2\gamma}{\Delta F}. \tag{4}
$$

The Zeldovich factor $Z$ in Eq. (2) is tacitly assumed to be $Z=1$. Here we refer to a text passage in the discussion, estimating the actual values of $Z$ and discussing its role. The attachment rate $\beta^*$ in Eq. (2) is expressed for a multi-component system according to Ref. [21] as
$$
\beta^*=\frac{4\pi\rho^{*2}}{a^4}\left[\sum_{i=1}^m\frac{(Y_i^P-Y_i^M)^2}{Y_i^M D_i^M}\right]^{-1}, \tag{5}
$$
where $a$ is the interatomic distance, $m$ is the number of components in the system (in our case 3), $Y_i^P$ ($Y_i^M$) is the site fraction of element $i$ in the nucleus of a precipitate (matrix) and $D_i^M$ is the diffusivity of element $i$ in the matrix.

## 3. Evaluation of the local nucleation conditions

### 3.1. Determination of the local nucleation barrier

Let the system be represented by a cubic simulation box of a bcc crystal lattice, fully occupied by A and B atoms, with periodic boundary conditions. The A and B atoms are assumed to be distributed randomly or regularly at the lattice sites in the box. The random distribution mimics the actual spatial fluctuations of the chemical composition. The fluctuations cause different precipitate nucleation conditions at different lattice site positions in the box. Each precipitate can be considered as a cluster of A, B, C atoms of chemical composition (A,B)₃C with its centre at a certain lattice site $p$. We define a nucleus as a subcritical precipitate with the radius $\rho<\rho^*$. The ratio of the number of substitutional atoms to the number of interstitial atoms in the cluster is fixed at 3:1. The size of a cluster is defined by the number $n_C$ of interstitial atoms in the cluster. A set of virtual clusters of size $n_C=1,2,3,\dots$, can be addressed to each lattice site $p$.

Two homogeneous matrices of compositions A-1.85 at.%B-0.03 at.%C and A-6.25 at.%B-0.03 at.%C for $\text{A} \rightarrow$ iron, $\text{B} \rightarrow$ chromium and $\text{C} \rightarrow$ carbon are considered. These matrix compositions are later denoted as 1.85B and 6.25B, respectively.

The diffusivity relevant to our modelling is only that of the interstitial element C, as the site fractions of A and B are supposed to be the same in the precipitate and in the matrix, which expresses the para-conditions for nucleation [20]. The carbon diffusivity in Fe-Cr-C alloy is supposed to be constant, i.e. ignoring possible effects of trapping as investigated recently by Fischer et al. [23].

### 3.2. Sorting of lattice sites in the simulation box with respect to the nucleation barriers

After the nucleation barriers $G_p^*$ are determined for all lattice sites $p$ in the simulation box, one can determine the values $G_{\text{min}}^*$ and $G_{\text{max}}^*$ of the minimum and maximum nucleation barrier. Moreover, the distribution function of nucleation barriers representing number densities $N_S$ of nucleation barriers in the interval $\langle G^*, G^* + \Delta G^*\rangle$ can be calculated. For a sufficiently large simulation box, one can expect that the distribution function is the same for all randomly generated systems of fixed mean chemical composition.

The distribution functions are shown for three different simulation boxes containing $12^3$, $96^3$, and $300^3$ bcc unit cells (involving two lattice sites) in Fig. 3. It is evident that even $96^3$ bcc unit cells are not sufficient for a good statistics (at least for the low B content) and thus a simulation box with $300^3$ bcc unit cells is used for a proper description.

A widening of the range of nucleation barriers $\langle G_{\text{min}}^*, G_{\text{max}}^*\rangle$ is observed for increasing B content in the matrix. The outmost right columns of the distribution functions correspond to the nucleation barrier of pure A-C clusters, which occurs more frequently for 1.85B matrix composition (Fig. 3a) than for 6.25B (Fig. 3b). Note that the nucleation barrier for pure A-C clusters increases with

![](./images/814638927502639104_4.jpg)

Fig. 3. Distribution function of nucleation barriers $G^*$ for random arrangement and $\Delta G^* = 1\text{x}10^{-20}\text{J}$. The number densities of sites $N_S$ are calculated for different simulation boxes containing $12^3$, $96^3$ and $300^3$ bcc unit cells and they are marked with light grey, dark grey and black, respectively. Matrix compositions are (a) 1.85B and (b) 6.25B. Only those parts of the distribution functions for $96^3$ and $300^3$ bcc unit cells are visible, which are not overlapped by distribution functions corresponding to smaller simulation boxes. The conditions used for the Fe-Cr-C system are $T=773$ K, $\gamma = 0.24\ \text{Jm}^{-2}$.

![](./images/814638927502639104_5.jpg)

Fig. 4. A 2-D scheme of central simulation box surrounded by eight copies due to application of periodic boundary conditions; 26 copies must be used in the 3-D case. Three sites $p_1$, $p_2$ and $p_3$ with the lowest nucleation times $t_{p_1}^{nuc} < t_{p_2}^{nuc} < t_{p_3}^{nuc}$ are depicted. So far unprocessed sites are marked with open circles; nucleated sites are marked with full circles with concentric dashed circles indicating their actual C-depleted zones. The configurations at times $t_2 = t_{p_2}^{nuc}$ and $t_3 = t_{p_3}^{nuc}$ are shown in (a) and (b), respectively. In (a), only site $p_1$ is occupied by a growing precipitate and its C-depleted zone does not include site $p_2$, where the precipitate nucleates at time $t_2$. In (b), the precipitate at site $p_3$ is not nucleated at time $t_3$, since it is located inside a depleted zone of $p_1$ from the left neighbouring simulation box.

increasing B content in the matrix, which is consistent with Fig. 2. Very low values of $G^{*}$ occur due to an increased probability of a high B content in the critical cluster for a 6.25B matrix compared to a 1.85B matrix (Fig. 3b).

## 4. Treatment of nucleation kinetics

### 4.1. Determination of the nucleation time at lattice site $p$

The nucleation kinetics at nucleation sites with the same nucleation barriers $G^{*}$ can be described by the number of nucleated precipitates $N(t)$ at time $t$. A time-dependent probability $\eta(t)$ of a single nucleation event is given by

$$
\eta(t)=\frac{N(t)}{N_{0}}. \tag{8}
$$

Integration of Eq. (1) with respect to time under the assumption $\tau=0$ (this assumption is reasonable for longer nucleation times) provides

$$
\eta(t)=1-\exp \left(-\frac{J^{S S} t}{N_{0}}\right). \tag{9}
$$

![](./images/814638927502639104_6.jpg)

Fig. 5. Distribution functions of nucleation barriers $G^{*}$ at lattice sites for $\Delta G^{*}=1 \mathrm{x} 10^{-20} \mathrm{J}$. The number densities of sites $N_{S}$ for random (regular) arrangement of A, B atoms are marked in light grey (black). The number densities of sites corresponding to the set of nucleated precipitates $N_{P}$, see Section 4.3., in random (regular) alloy are marked in dark grey (white). Nucleation barriers for homogeneous arrangement are marked by arrows. The plots (a, c, e) correspond to matrix composition 1.85B and (b, d, f) to matrix composition 6.25B. Distribution functions in (a, b) are calculated with $\gamma=0.10 \mathrm{Jm}^{-2}$, in (c, d) with $\gamma=0.15 \mathrm{Jm}^{-2}$, in (e, f) with $\gamma=0.20 \mathrm{Jm}^{-2}$ and $T=773 \mathrm{K}$ in all calculations.

The steady state nucleation rate $J^{SS}$ is given by Eqs. (2) and (5) and involves finally only quantities, such as $G^{*}$ and $\rho^{*}$, which are known for each lattice site $p$ as $G_{p}^{*}, \rho_{p}^{*}(n_{p}^{*})$, see Eq. (6). The nucleation time, $t_{p}^{nuc}$, at lattice site $p$ is then given by solution of $\eta(t_{p}^{nuc})=s$, where $s$ is a random number from the interval $\langle 0,1\rangle$. The stochastic nature of nucleation as well as the role of composition fluctuations are reflected by this treatment.

### 4.2. Diffusion-controlled growth of precipitates

The precipitate nucleated and growing at lattice site $p$ accumulates the interstitial component C from the surrounding matrix. Consequently, a spherical C-depleted zone with radius $Z_{p}$ around lattice site $p$ is formed and allows no further nucleation there. The evolution of the precipitate radius $\rho_{p}(t)$ and, consequently, $Z_{p}(t)$ is derived from the thermodynamic extremal principle [21,24] stating that
$$
\frac{1}{2} \frac{\partial Q}{\partial \dot{\rho}_{p}}=-\frac{\partial G}{\partial \rho_{p}},
\tag{10}
$$
where $Q$ is the dissipation function linked to the growth of the precipitate and $G$ is the Gibbs energy given by Eq. (7). We assume that $Q$ is determined only by the radial diffusive

![](./images/814638927502639104_7.jpg)

Fig. 6. The evolution of the number density of precipitates $N_{P}$ for the same conditions as presented in Fig. 5. Circles (triangles) mark random (regular) arrangement of A, B atoms in the lattice; homogeneous arrangements are marked with squares; (a, b) are calculated for $\gamma=0.10 \mathrm{Jm}^{-2}$; (c, d) for $\gamma=0.15 \mathrm{Jm}^{-2}$ and (e, f) for $\gamma=0.20 \mathrm{Jm}^{-2}$ and $T=773 \mathrm{K}$ in all calculations.

flux $J_p$ of component C in the matrix around the precipitate at lattice site $p$ as

$$
Q=\int_{\rho_{p}}^{Z_{p}} \frac{R T \Omega}{Y_{C}^{M} D_{C}^{M}} 4 \pi r^{2} J_{p}^{2} d r,
\tag{11}
$$

where $Y_{C}^{M}$ is the site fraction of C in the matrix, $D_{C}^{M}$ is the tracer diffusion coefficient of C in the matrix and $r$ is the radial distance from the lattice site $p$. Let us assume that the site fraction $Y_{C}^{M}$ of C in the depleted zone is constant and obtains the equilibrium value $Y_{C}^{Meq}$ from the phase diagram (Gibbs-Thomson effect is ignored). Then, the flux $J_p$ is related to $\dot{\rho}_p$ as

$$
J_{p}=\dot{\rho}_{p} \frac{\left(Y_{C}^{M e q}-Y_{C}^{P}\right) \rho_{p}^{2}}{\Omega} \frac{1}{r^{2}}, \quad \rho_{p} \leqslant r \leqslant Z_{p},
\tag{12}
$$

where $Y_{C}^{P}=1 / 3$ is the site fraction of carbon in the precipitate. From mass conservation, it follows that $Z_p$ and $\rho_p$ are related as

$$
Z_{p}=\rho_{p} \alpha, \quad \alpha=\sqrt[3]{\frac{Y_{C}^{P}-Y_{C}^{M e q}}{Y_{C}^{M 0}-Y_{C}^{M e q}}},
\tag{13}
$$

where $Y_{C}^{M 0}$ is the initial site fraction of C in the matrix. Performing the integration in Eq. (11) by using relations (12) and (13) yields

$$
Q=\frac{4 \pi k T \rho_{p}^{3}\left(Y_{C}^{M e q}-Y_{C}^{P}\right)^{2}(\alpha-1) \dot{\rho}_{p}^{2}}{Y_{C}^{M e q} D_{C}^{M} \Omega \alpha}.
\tag{14}
$$

For a sufficiently large growing precipitate, one can neglect the interface energy term, and the Gibbs energy $G$ in Eq. (10) is given by the volumetric term only as

$$
G=-\frac{4 \pi}{3} \rho_{p}^{3} \Delta F
\tag{15}
$$

with $\Delta F$ given in Fig. 2, corresponding to $Y_B$ in the precipitate being the same as in the matrix. The relations between the site fraction $Y_B$ and the mole fraction $X_B$ can be found, for example, in Ref. [25], Section 2.2. Using Eqs. (14) and (15) in Eq. (10) yields

$$
\dot{\rho}_{p}=\frac{\Delta F \cdot Y_{C}^{M e q} D_{C}^{M} \Omega \alpha}{k T\left(Y_{C}^{M e q}-Y_{C}^{P}\right)^{2}(1-\alpha) \rho_{p}}
\tag{16}
$$

with the solution

$$
\rho_{p}(t)=\left(\frac{2 \Delta F Y_{C}^{M e q} D_{C}^{M} \Omega \alpha\left(t-t_{p}^{n u c}\right)}{k T\left(Y_{C}^{M e q}-Y_{C}^{P}\right)^{2}(1-\alpha)}+\rho_{p}^{* 2}\right)^{\frac{1}{2}}.
\tag{17}
$$

Finally, the radius of the C-depleted zone $Z_p$ is given by Eq. (13).

### 4.3. Elimination of nucleation sites in diffusion zones

The model for the diffusion-controlled growth of precipitates and formation of C-depleted zones is used to identify and eliminate those sites where nucleation of new precipitates cannot occur due to depletion of the C component. Before the simulation of the nucleation kinetics, to each substitutional lattice site $p$ (potential nucleation site), its nucleation time $t_{p}^{nuc}$ and $\rho_{p}^{*}$ are assigned as described in Section 4.1 and stored in the set of nucleation candidates. The elimination procedure during simulation of nucleation kinetics consists of the following steps:

1. In the first step, the lattice site $p$ with the lowest nucleation time $t_{p}^{nuc}$, denoted as $t_1$, is selected from the set of nucleation candidates and eliminated from the set; its parameters (values of $p$, $t_{p}^{nuc}$ and $\rho_{p}^{*}$) are stored in the set of nucleated precipitates.
2. In the $i$-th step, the lattice site $p$ with the lowest nucleation time $t_{p}^{nuc}$, denoted as $t_i$, is selected from the set of remaining nucleation candidates and eliminated from the set. The lattice site $p$ is tested with respect to the set of nucleated precipitates, if the lattice site $p$ is situated within at least one of the depleted zones of nucleated precipitates calculated for time $t = t_i$ by Eqs. (17) and (13). If it is not the case, the parameters (values of

![](./images/814638927502639104_8.jpg)

Fig. 7. Profiles of the total cluster energy $G_{p}(n_{C})$ for a site $p$ with the lowest nucleation barrier for regular arrangement (solid line) and the homogeneous arrangement (dashed line). The chemical compositions of matrices (a) 1.85B and (b) 6.25B, for $\gamma=0.20 \mathrm{Jm}^{-2}$ and $T=773 \mathrm{K}$ in all calculations.

$p$, $t_p^{nuc}$ and $\rho_p^*$) are added to the set of nucleated precipitates.

3. The procedure runs until the total volume of all depleted zones reaches the volume of the simulation box.

From the set of nucleated precipitates, the total number, their positions in the simulation box and sizes can be reconstructed for any time $t$. The simulation procedure including the elimination of potential nucleation sites in C-depleted zones is schematically depicted in Fig. 4.

## 5. Results of simulations and their discussion

The simulations of nucleation are performed for two matrices with compositions 1.85B and 6.25B and for three values of specific interface energies $\gamma = 0.10, 0.15$ and $0.20\ \text{Jm}^{-2}$. Moreover, we assume random, regular (periodic arrangement of B atoms) and homogeneous (each site occupies fixed fractions of A and B atoms according to the matrix composition) arrangements of substitutional atoms in the lattice. The homogeneous

![](./images/814638927502639104_9.jpg)

Fig. 8. Radius distribution functions of precipitates in 1.85B matrix for two times $t$; (a, c and e) correspond to random (RND) arrangement and (b, d and f) correspond to regular (REG) arrangement of substitutional atoms in the lattice. (a, b) are calculated for $\gamma = 0.10\ \text{Jm}^{-2}$; (c, d) for $\gamma = 0.15\ \text{Jm}^{-2}$ and (e, f) for $\gamma = 0.20\ \text{Jm}^{-2}$ and $T = 773\ \text{K}$ in all calculations.

arrangement corresponds to the classical Becker-Döring model [1] representing the base of CNT.

To judge the effect of chemical fluctuations at the atomic level on nucleation kinetics, the distribution function of nucleation barriers at lattice sites are calculated for random and regular atomic arrangements. Moreover, to show the effect of the elimination procedure, the distribution func- tions of the nucleation barriers $G^{*}$ are compared with those from the set of nucleated precipitates, see Section 4.3. Thus, four distribution functions are grouped together in each plot as shown in Fig. 5 for different chemical compositions of the matrix and different values of $\gamma$ . The distribution functions of nucleation barriers $G^{*}$ at lattice sites indicate that an increasing amount of B atoms shifts the most fre- quent nucleation barrier $G^{*}$ towards lower values and also causes widening of the distribution function. With increas- ing interface energy $\gamma$ , the distribution function of the nucleation barriers $G^{*}$ widens. The most frequent nucle ation barrier corresponds to clusters, whose chemical com- position of A, B components equals the mean composition in the matrix and tends towards higher values with increas- ing interface energy $\gamma$ .

The evolution of the number density of precipitates is shown in Fig. 6 for random, regular and homogeneous arrangements of substitutional atoms in the lattice. The amount of precipitates in the matrix with a regular and homogeneous arrangement is in general significantly lower than for a random arrangement. As in Fig. 5, the plots are presented for different chemical composition of the matrix and different values of $\gamma$ . Lattices with a random arrange ment of substitutional atoms show a much earlier start of nucleation, a higher nucleation rate as well as a higher number density of the nucleated precipitates compared to lattices with a regular and homogeneous arrangement of the same chemical composition. The influence of arrange- ment on nucleation rate drastically increases with the value of $\gamma$ and is rather small for low values of $\gamma$ . The results for a homogeneous lattice are generally rather close to those for a regular arrangement.

It is interesting to note that, in the homogeneous arrangement, nucleation is easier than in the regular arrangement. In the case of a regular arrangement, all determined nucleation barriers are higher than those calculated for homogeneous arrangements (see arrows in Fig. 5). The reason for it can be found in Fig. 7, where the dependences of the total cluster Gibbs energy $G(\vec{n}_{p}(n_{C}))$ for the regular arrangement at the lattice site p with the lowest nucleation barrier is compared with the homogeneous arrangement. One can observe significant oscillations causing an increase of the nucleation barrier, $G_{p}^{*}$ , represented by the global maximum of $G(\vec{n}_{p}(n_{C}))$ for the case of the regular arrangement.

In the context of Fig. 7, we use the results there to dis- cuss the value and the role of the Zeldovich factor Z, which was set as Z = 1 in Eq. (2). The value of Z can be estimated from Fig. 7a calculated for $\gamma=0.20 Jm^{-2}$ and T=773 K and follows as $Z^{2} ≈2 ×10^{-4}$ for the alloy 1.85 B and Z² ≈ 10⁻⁴ for the alloy 6.25B. This fact confirms the asser- tion that the Zeldovich factor is not significantly influenced by the nucleation conditions and can be considered as a constant of the order of $10^{-2}$ . The incubation time $\tau$ may shift the time scale by an amount of $\tau$ to larger values of time t. If one accounts for the value of $Z=10^{-2}$ instead of Z=1 in the nucleation kinetics, then the nucleation kinetics slows down by a factor of $10^{2}$ , and the incubation time $\tau$ is increased by a factor of $10^{4}$ . This means that tak ing Z=1 effectively increases $\tau$ by a factor of $10^{2}$ . The incubation time relevant to our study is thus $\tau=10^{-7} s$ , which only slightly influences the nucleation kinetics with y = 0.10 Jm-2 for low times, but hardly influences the results for $\gamma=0.20 Jm^{-2}$ . Furthermore, it should be kept in mind that the Zeldovich factor is calculated under the assumption that $\Delta G(n)$ can be expanded at its maximum in a power series up to quadratic terms in $n-n^{*}$ (for details see Ref. [4], Section 6.2.6). As the function $\Delta G(n)$ is discon tinuous in the cases accounting for fluctuations, its second derivative can hardly be calculated directly and the Zeldovich factor has to be calculated from a parabola fitted to the dependence $\Delta G$ on n around $n^{*}$ . However, the numerical solution of the leading Fokker-Planck equation for nucleation indicates that the Zeldovich factor signifi- cantly underestimates the value of the steady state solution obtained numerically in Ref. [8]. As there is no limitation on the dependence $\Delta G$ on n in numerical solution, it can also be used for discontinuos $\Delta G(n)$ , if details of nucleation kinetics are of concern.

![](./images/814638927502639104_10.jpg)

Fig. 9. Radius distribution functions of precipitates growing in 6.25B matrix for two times t; (a) corresponds to random (RND) arrangements, (b) to regular (REG) arrangement, for $\gamma=0.20 Jm^{-2}$ and T=773 K in all calculations.

In Fig. 8, the radius distribution functions of precipitates in 1.85B matrix are presented for two times before the nucleation procedure stops (see Section 4.3 for details). If the interface energy $\gamma$ is low enough, nucleation is not restricted to the sites with the lowest nucleation barriers.

Both nucleation and growth occur within a short time period, during which the size distribution cannot sufficiently develop. This holds for both random and regular arrangements, as shown in Fig. 8a and b for $\gamma=0.10\,\text{Jm}^{-2}$. In this case, the radius distribution function for a random matrix

![](./images/814638927502639104_11.jpg)

Fig. 10. The evolution of the average precipitate radius $\bar{\rho}_p$ for the same conditions as presented in Fig. 5. Circles (triangles) mark random (regular) arrangement of A, B atoms in the lattice; homogeneous arrangements are marked with squares; (a, b) are calculated for $\gamma=0.10\,\text{Jm}^{-2}$; (c, d) for $\gamma=0.15\,\text{Jm}^{-2}$, and (e, f) for $\gamma=0.20\,\text{Jm}^{-2}$ and $T=773\,\text{K}$ in all calculations.

is broader than in the regular case, which is due to the wider spectrum of nucleation barriers associated with critical sizes in the random matrix. Increasing the interface energy to $\gamma=0.15\ \text{Jm}^{-2}$ reduces the nucleation rate. Consequently, the earlier nucleated precipitates have more time to grow and the radius distribution functions are wider compared to those for $\gamma=0.10\ \text{Jm}^{-2}$, see Fig. 8c and d. The random arrangement leads to a narrower radius distribution function and a lower mean radius compared to the regular arrangement at the end of the nucleation period. The effects described for $\gamma=0.15\ \text{Jm}^{-2}$ get much more intensive for $\gamma=0.20\ \text{Jm}^{-2}$, see Fig. 8e and f.

![](./images/814638927502639104_12.jpg)

Fig. 11. The evolution of the total volume $V_P$ of the precipitates in $1\ \text{m}^3$ of the matrix, presented for the same conditions as in Fig. 5. Circles (triangles) mark random (regular) arrangement of A, B atoms in the lattice; homogeneous arrangements are marked with squares; (a, b) are calculated for $\gamma=0.10\ \text{Jm}^{-2}$; (c, d) for $\gamma=0.15\ \text{Jm}^{-2}$, and (e, f) for $\gamma=0.20\ \text{Jm}^{-2}$ and $T=773\ \text{K}$ in all calculations.

Radius distribution functions in 6.25B matrix for
$\gamma = 0.20 \, \text{Jm}^{-2}$ are shown in Fig. 9. Generally, the dis-
tribution functions evolve in a way similar to the 1.85B
matrix. A higher amount of B component supports faster
nucleation, which results in a higher number density of pre-
cipitates and a smaller mean radius, compared to 1.85B
matrix under the same conditions. This is obvious by com-
paring Fig. 9a with Fig. 8e and Fig. 9b with Fig. 8f.

Figs. 10 and 11 provide, at a first glance, an overview on
the precipitation kinetics depending on the arrangement of
atoms, the chemical composition and the interface energy.
Here an increasing enhancement of the role of com-
positional fluctuations on nucleation kinetics with increas-
ing interface energy and decreasing chemical driving force
can be observed. This is valid for both alloys and can be
seen clearly in Fig. 11a, c and e or Fig. 11b, d and f. If
one compares $V_p$ (whose value is identical to that of the
volume fraction of precipitates) for a random arrangement
(circles) with a regular or homogeneous arrangement (tri-
angles or squares), one finds for the case of $\gamma = 0.20 \, \text{Jm}^{-2}$
that the same fraction of precipitates has developed in a
time interval, which is shorter by a factor of $10^5$–$10^6$ times
for the random arrangement (chemical fluctuations of B
component) compared to the regular or homogeneous
arrangement, see for example Fig. 11e. For $\gamma = 0.15 \, \text{Jm}^{-2}$
still a remarkable factor, but lower than $10^5$–$10^6$, can be
observed, whereas for $\gamma = 0.10 \, \text{Jm}^{-2}$ nearly no difference
between the three types of arrangement exists.

Nucleation of precipitates usually occurs with much fas-
ter kinetics than predicted by the classical theory of
homogeneous nucleation. That is why the difference is usu-
ally explained by heterogeneous nucleation which allows
introducing a shape factor $f < 1$ into Eq. (3). In this way,
the nucleation barrier is decreased and the nucleation kinet-
ics enhanced. The considereation of chemical fluctuations
presented in this paper offers a new view how to explain
the experimentally observed "too fast" nucleation kinetics.

The authors are of the opinion that the experimental veri-
fication of the present model will be extremely complicated as
one needs two systems, which differ only in the ordering of
the B components. Of course, there exist some systems in
which the substitutional atoms get spontaneously ordered
by lowering the temperature. However, also the chemistry
of the system changes and ordering needs some time during
which nucleation cannot be excluded. Then also, nucleation
may occur only at different temperatures as the ordered and
disordered phases are stable at different temperatures. Thus,
one may rely more on the verification of the model by means
of comparison with a computer experiment based, for exam-
ple, on the Monte Carlo methods than on some laboratory
experiments.

## 6. Conclusions
This paper presents an extension of the previously devel-
oped models for nucleation in interstitial/substitutional
alloys. The conditions for nucleation are evaluated locally
at each potential nucleation site and used as input data
for the proposed kinetic treatment of nucleation. The sites
where nucleation occurs are identified by a selection mecha-
nism based on diffusion-controlled growth of precipitates.
The whole model is applied to examine the role of internal
atomic arrangement (random vs. regular) on nucleation in
combination with various specific interface energies and
chemical composition of the alloys. It is shown that the
chemical fluctuations at the atomic level can considerably
facilitate nucleation, especially in the case of high specific
interface energies.

## Acknowledgements
Financial support by the Austrian Federal Government (in
particular from the Bundesministerium für Verkehr, Innovation
und Technologie and the Bundesministerium für Wirtschaft und
Arbeit) and the Styrian Provincial Government, represented by
Österreichische Forschungsförderungsgesellschaft mbH and by
Steirische Wirtschaftsförderungsgesellschaft mbH, within the
research activities of the K2 Competence Centre on "Integrated
Research in Materials, Processing and Product Engineering",
operated by the Materials Center Leoben Forschung GmbH in
the framework of the Austrian COMET Competence Centre
Programme, Project A1.17, is gratefully acknowledged.

J.S. gratefully acknowledges the financial support by the Czech
Science Foundation in the frame of the Project 14-24252S.

## References
[1] R. Becker, W. Döring, Ann. Phys. 24 (1935) 719.
[2] K.C. Russell, Adv. Colloid Interface Sci. 13 (1980) 205.
[3] E. Kozeschnik, Modeling Solid-State Precipitation,
Momentum Press, New York, 2013.
[4] H. Riedel, Fracture at High Temperatures, Springer, Berlin,
1987.
[5] I.M. Lifshitz, V.V. Slyozov, Zh. Eksp. Teor. Fiz. 35 (1958)
479 (in Russian).
[6] C. Wagner, Z. Elektrochem. 65 (1961) 581 (in German).
[7] J. Svoboda, I. Turek, V. Sklenicka, Acta Metall. Mater. 38
(1990) 573.
[8] J. Svoboda, Acta Metall. Mater. 39 (1991) 963.
[9] S.I. Golubov, Y.N. Osetsky, A. Serra, A.V. Barashev, J. Nucl.
Mater. 226 (1995) 252.
[10] M.H. Mathon, A. Barbu, F. Dunstetter, F. Maury, N.
Lorenzelli, C.H. de Novion, J. Nucl. Mater. 245 (1997) 224.
[11] A.V. Barashev, S.I. Golubov, D.J. Bacon, P.E.J. Flewitt, T.A.
Lewis, Acta Mater. 52 (2004) 877.
[12] E. Kozeschnik, Scripta Mater. 59 (2008) 1018.
[13] E. Clouet, A. Barbu, L. Lae, G. Martin, Acta Mater. 53
(2005) 2313.
[14] R. Weinkammer, P. Fratzl, H.S. Gupta, O. Penrose, J.
Lebowitz, Phase Trans. 77 (2004) 433.
[15] P. Warczok, J. Zenisek, E. Kozeschnik, Comput. Mater. Sci.
60 (2012) 59.
[16] P. Warczok, D. Reith, M. Schober, H. Leitner, R. Podloucky,
E. Kozeschnik, Int. J. Mater. Res. 102 (2011) 709.
[17] P. Warczok, Y. Shan, M. Schober, H. Leitner, E. Kozeschnik,
Solid State Phenomena 172–174 (2011) 309.
[18] R.G. Baker, J. Nutting, J. Iron Steel Inst. 192 (1959) 257.
[19] A. Inoue, T. Masumoto, Met. Trans. A 11A (1980) 739.
[20] E.C. Bain, Alloying Elements in Steel, American Society of
Materials, Cleveland, OH, 1939.
[21] J. Svoboda, F.D. Fischer, P. Fratzl, E. Kozeschnik, Mater.
Sci. Eng. A 385 (2004) 166.
[22] E. Kozeschnik, B. Buchmayr, MatCalc – a simulation tool for
multicomponent thermodynamics, diffusion and phase trans-
formations, in: H. Cerjak, H.K.D.H. Bhadeshia (Eds.),
Mathematical Modelling of Weld Phenomena, 5th ed.,
Woodhead, London, 2001, p. 349.
[23] F.D. Fischer, J. Svoboda, E. Kozeschnik, Model. Simul.
Mater. Sci. Eng. 21 (2013) 025008.
[24] F.D. Fischer, J. Svoboda, H. Petryk, Acta Mater. 67 (2014) 1.
[25] J. Svoboda, Y. Shan, E. Kozeschnik, F.D. Fischer, Model.
Simul. Mater. Sci. Eng. 22 (2014) 065015.
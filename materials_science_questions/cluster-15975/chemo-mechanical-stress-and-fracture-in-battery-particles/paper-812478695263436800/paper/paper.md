# An assessment of a mechanism for void growth in Li anodes

U. Roy, N.A. Fleck, V.S. Deshpande*

Department of Engineering, University of Cambridge, Cambridge CB2 1PZ, UK

---

## ARTICLE INFO

**Article history:**
Received 13 January 2021
Received in revised form 21 March 2021
Accepted 29 March 2021
Available online 5 April 2021

**Keywords:**
Solid-state battery
Butler-Volmer kinetics
Void growth
Creep

## ABSTRACT

The formation of dendrites within the solid-state electrolyte of a Lithium (Li) ion battery is exacerbated by the presence of voids at the interface between the electrolyte and the Li anode. It is assumed that voids initiate and grow by the focussing of Li flux at the periphery of pre-existing small imperfections along the interface between the solid electrolyte and Li anode. Void growth in the Li anode, driven by stripping of the $Li^+$ ions from the anode, is accompanied by creep within the anode. Consequently, the initiation and growth of these voids involve electrochemical stripping of $Li^+$ from the anode, creep deformation of the anode and flux of $Li^+$ through the adjacent solid electrolyte. Here we present a numerical analysis of this problem. We consider a single-ion conductor electrolyte, with Butler-Volmer kinetics governing the interfacial flux and the Li anode modelled as a power-law creeping solid. The study reveals that void growth can only initiate from relatively large pre-existing interfacial imperfections of size $>1200\ \mu$m along the interface of the solid electrolyte (LLZO) and the Li anode. In contrast, experimental observations suggest that voids as small as $1\ \mu$m can initiate along the LLZO/Li interface and thus the simple picture described above involving power-law creep of the Li anode coupled with Butler-Volmer kinetics, even with interfacial diffusion accounted for, is insufficient to explain these observations. Our calculations reveal that the degree of flux focussing on the periphery of small imperfections must exceed that predicted by Butler-Volmer kinetics in order for interfacial voids to initiate and grow.

---

## 1. Introduction

Li metal is a promising anode material for Li-ion batteries due to its high energy density compared to the current technology of graphite anodes [1,2]. Despite this, Li metal anodes are not currently used in Li-ion batteries due to the tendency of the Li electrode/liquid electrolyte interface to become unstable via the formation of dendrites and other such defect structures. It had been hoped that solid electrolytes (SEs), including ceramic electrolytes with a high elastic modulus, might increase the stability of electrode/electrolyte interfaces such that dendrite formation is not a problem [3,4]. However, Li filaments or dendrites do grow from Li anodes into a range of solid electrolytes including LLZO (Li stuffed garnet $Li_7La_3Zr_2O_{12}$) [5,6] and Argyrodite ($Li_6PS_5Cl$) electrolytes. Typically, these filaments grow when the Li-ion battery is charged above a critical current density and their penetration into the electrolyte results in a short-circuit failure.

Li filaments grow into the electrolyte at sites along the electrode/electrolyte interface that are near voids in the Li anode [7,8]. Recent calculations [9] have shown that such voids enhance the electric potential in the electrolyte in their vicinity which in turn promotes filament growth. Thus, an understanding of the mechanisms by which these voids form and grow is an essential step in helping design batteries which inhibit void formation and are thereby more resistant to filament formation and short-circuiting. Bruce and co-workers [7] revealed that there are two distinct critical current densities: the critical current on stripping (CCS), and the critical current on plating (CCP). Li filaments are observed to initiate and grow when Li metal is being plated on the Li electrode during charge and the CCP is defined as the current density above which the growth of Li filaments initiates [7]. Conversely, stripping Li metal from the electrode during discharge can lead to the formation of voids in the anode, resulting in a concentration of current (flux focussing) at the remaining areas of contact [7,8,10,11]. Typically, the value of CCS is less than the value of CCP, and numerous experimental studies have now revealed that the application of a stack pressure enhances the value of CCS. For example, for the Li/LLZO system, void growth or rather the formation of instabilities at the interface was observed at a CCS as low as $0.1\ \text{mAcm}^{-2}$ when no stack pressure was applied [12]; application of a stack pressure of 2 MPa increased the CCS to $0.4\ \text{mAcm}^{-2}$ [12].

The mechanics governing the formation and growth of voids in the Li electrode is a complex combination of plastic/creep deformation and vacancy diffusion within the metal electrode coupled

---

* Corresponding author.
E-mail address: vsd@eng.cam.ac.uk (V.S. Deshpande).

© 2021 Elsevier Ltd. All rights reserved.
https://doi.org/10.1016/j.eml.2021.101307
2352-4316/© 2021 Elsevier Ltd. All rights reserved.

![](./images/812478695263436800_1.jpg)
![](./images/812478695263436800_2.jpg)
![](./images/812478695263436800_3.jpg)

![](./images/812478695263436800_4.jpg)
![](./images/812478695263436800_5.jpg)
![](./images/812478695263436800_6.jpg)
![](./images/812478695263436800_7.jpg)

Fig. 1. (a) SEM cross-sections of the Li metal/Li₆PS₅Cl interface after the 6th stripping cycle [7]. The cell was loaded via a current of 1 mAcm⁻² and a stack pressure of 3 MPa and the void formed as a result of the loading is marked. (b) Sketch of the symmetric Li/LLZO/Li cell analysed with a central debonded patch of diameter 2a. The problem is analysed by considering a small region shown by the dashed lines. This zone is of radius R, heights H and L of electrolyte and Li anode, respectively. The electrolyte and the electrode are coupled together via the Butler-Volmer flux j. The detailed boundary conditions are indicated in (c) and (d) for the electrolyte and electrode, respectively.

to the electrochemical kinetics of the electrode/electrolyte interface. Krauskopf et al. [5] proposed a diffusion-based model for void growth where they argued that every Li atom that is stripped from the Li anode leaves behind a vacancy that annihilates at dislocations or grain boundaries, or diffuses from the Li/LLZO interface into the bulk Li anode. They then argued that so long as diffusion can sufficiently rapidly annihilate these vacancies, contact is maintained, and void growth does not occur. Using this idea along with a defect relaxation model [13] a critical current for void formation can then be estimated. The model however ignores the role of power-law creep deformation within the Li anode. Dislocation creep or power-law creep occurs by a combination of dislocation glide and climb aided by vacancy diffusion and is expected to aid the annihilation of vacancies created by the stripping process. This study aims to clarify the role of dislocation creep on void growth within Li anodes.

### 1.1. The model problem

The idealised electro-mechanical problem is sketched in Fig. 1b. We consider an axisymmetric Li/LLZO/Li cell with an interfacial crack-like defect of radius a that may, or may not, expand into a void depending upon the spatial distribution of stripping current into the LLZO electrolyte from the Li anode. This defect comprises a debonded patch along the interface such that the Li anode is not in contact with the electrolyte over this circular region of radius a and thus there is no Li⁺ flux over this portion of the interface. This portion of the interface is also traction-free. Over the remainder of the Li electrode/electrolyte interface it is assumed that the flux is set by Butler-Volmer kinetics. The resulting spatially inhomogeneous interfacial flux will result in creep deformation of the Li electrode and our aim is to investigate whether void growth ensues over the debonded patch from this creep deformation. Voids will initiate if the debonded patch has a tendency to separate from the electrolyte surface while if the debonded patch has a tendency to push against the electrolyte surface (and thereby generate compressive traction) a void will not initiate from this defect. The aim of this study is to calculate the instantaneous velocity field of the Li over the debonded patch with respect to the electrolyte surface and hence infer the conditions under which void growth might occur.

The outline of the paper is as follows. We first calculate the interfacial flux in the presence of the debonded patch. The low strength of the Li anode implies that the interfacial Butler-Volmer kinetics is decoupled from the deformation of the electrode allowing for independent solutions of Li⁺ flux within the electrolyte and the consequent deformation of the electrode. The interfacial flux is then used to solve the mechanical problem of creep of the electrode and thereby infer the conditions required for void growth. Finally, we also examine the role of interfacial diffusion along the electrode/electrolyte interface that is neglected in creep analysis of the electrode.

### 2. Interfacial flux in the presence of a debonded patch

We analyse the portion of the Li/LLZO/Li symmetric cell shown by the dashed lines in Fig. 1b. The LLZO electrolyte, is sandwiched between two Li electrodes, each of height L. Thus, the axisymmetric region analysed comprises portions of the electrode and electrolyte that encompass the debonded zone on the stripping electrode. We exclude the plating electrode from the region analysed by an appropriate choice of boundary conditions on the electrolyte (discussed subsequently). Our focus in this section is on estimating the interfacial flux and we discuss the governing equations for the electrolyte along with the associated boundary conditions.

We model the electrolyte as a single ion conductor, linear dielectric. Gauss' law for a linear dielectric of permittivity $\mathcal{E}$ requires that the electric field $E_{i}$ satisfies $\mathcal{E}E_{i,i}=\rho_{\text{f}}$ where $\rho_{\text{f}}$ is the density of free-charge, and a comma denotes differentiation in the usual manner. The Maxwell-Faraday equation (Faraday's law of induction) is automatically satisfied by defining $E_{i}\equiv-\phi_{,i}$, where $\phi$ is the electric potential; consequently, Gauss' law reduces to $\mathcal{E}\phi_{,ii}=-\rho_{\text{f}}$. We restrict our analysis to the case of an electroneutral electrolyte where the fractional occupancy of $\text{Li}^{+}$ remains fixed at $\theta_{0}^{\text{e}}$ and thus $\rho_{\text{f}}\equiv0$. Gauss' law for the electrolyte then reduces to

$$
\phi_{,ii}=0. \tag{2.1}
$$

The spatial gradient of the chemical potential of $\text{Li}^{+}$ within the electrolyte provide the driving force for the flux of $\text{Li}^{+}$. This driving force is $f_{i}\equiv-\partial\mu_{\text{Li}^{+}}^{\text{e}}/\partial x_{i}$ where, for the electroneutral electrolyte, the chemical potential $\mu_{\text{Li}^{+}}^{\text{e}}$ is given in terms of the reference chemical potential $\mu_{0}^{\text{e}}$, the Faraday constant $F$ and $\phi$ by $\mu_{\text{Li}^{+}}^{\text{e}}=\mu_{0}^{\text{e}}+F\phi$.

The flux of $\text{Li}^{+}$ in the electroneutral electrolyte is $h_{i}\equiv mN_{\text{L}}^{\text{e}}\theta_{0}^{\text{e}}f_{i}$, where $m$ is the mobility of $\text{Li}^{+}$ in the electrolyte and $N_{\text{L}}^{\text{e}}$ is the molar density of $\text{Li}^{+}$ sites in the electrolyte. Typically, the electrical flux in electrolytes is measured in terms of the current $j_{i}=Fh_{i}$ of the $\text{Li}^{+}$ ions, with the mobility written in terms of an ionic conductivity $\kappa\equiv j_{z}/E_{z}$ for an electrical field $E_{z}$ applied in the $z-$ direction. Thus, upon setting $\kappa=mN_{\text{L}}^{\text{e}}\theta_{0}^{\text{e}}F^{2}$ the current is related to the gradient of the electric potential as $j_{i}=-\kappa\phi_{,i}$ which is essentially a statement of Ohm's law. The conservation of $\text{Li}^{+}$ ions requires

$$
FN_{\text{L}}^{\text{e}}\dot{\theta}_{\text{e}}=-j_{i,i}, \tag{2.2}
$$

where $\dot{\theta}_{\text{e}}$ is the rate of change of occupancy of $\text{Li}^{+}$ sites in the electrolyte. However, since we are constraining the electrolyte to remain electroneutral this implies that $\dot{\theta}_{\text{e}}=0$ and the flux balance law reduces to $\phi_{,ii}=0$, i.e., identical to Eq. (2.1). Thus, for the electroneutral electrolyte, the electrical and $\text{Li}^{+}$ flux balance laws reduce to a single governing equation given by the Laplace equation $\phi_{,ii}=0$ which needs to be solved with appropriate boundary conditions. We emphasise that this reduction in the number of the independent governing equations implies that no solutions exist for certain problems (e.g., a rigid electrode with a spatially non-uniform resistance across the electrode/electrolyte interface). However, the Li electrode analysed here is far from this rigid limit and the electroneutrality simplification suffices for this study.

The solution of the governing equation $\phi_{,ii}=0$ requires specification of appropriate boundary conditions. The origin of the axisymmetric co-ordinate system is located at the centre of the debonded region with the region analysed of radius $R$ and the electrolyte spanning a region $z=0$ to $z=H$ as shown in Fig. 1c. The electrode is maintained at a fixed potential $\phi=\phi_{\text{p}}$ and the boundary conditions along the electrode/electrolyte interface ($z=0$) are

$$
\begin{aligned}
& \phi_{,i}n_{i}=0 \quad \text{over } 0\leq r<a \\
& \phi_{,i}n_{i}=-j/\kappa \quad \text{over } r\geq a \text{ on } z=0.
\end{aligned} \tag{2.3}
$$

where $n_{i}$ is the outward normal to the electrolyte on $z=0$ and $j$ is the interfacial flux (positive for flux from the electrode to electrolyte) given by the Butler-Volmer relation. In terms of the traction $T_{i}$ on the electrolyte surface and the molar volume $\Omega_{\text{Li}}$ of Li the interfacial flux is then given by [9]

$$
j=\frac{\eta-T_{i}n_{i}\Omega_{\text{Li}}/F}{Z}. \tag{2.4}
$$

In (2.4) $Z$ is the interfacial resistance while $\eta\equiv(\phi_{\text{p}}-\phi)-\mathcal{U}$ is the interface overpotential with $\mathcal{U}$ the equilibrium potential between the Li and the electrolyte. This linearised form of the Butler-Volmer relation holds in the limit $F\eta/(2\mathcal{R}T)\ll1$, where $\mathcal{R}$ and $T$ are the universal gas constant and temperature, respectively. Recalling that $\eta\approx j_{\infty}Z$ and using a value of $Z=5\ \Omega\text{cm}^{2}$, which is representative of a well-conditioned Li/LLZO interface [14], we observe that $\eta=5$ mV for an imposed areal current $j_{\infty}=1$ mAcm$^{-2}$. Thus, $F\eta/(2\mathcal{R}T)\approx0.1$ and the error in employing this linearised form compared to the non-linear Butler-Volmer relation is no more than 0.5%. The boundary condition on the surface $r=R$ follows from the recognition that the region analysed is sufficiently large that the debonded patch has no influence on the remote boundaries of the region analysed. With $n_{i}$ denoting the outward normal to the electrolyte on the surface $r=R$, the current across the surface $r=R$ vanishes so that we can then specify $\phi_{,i}n_{i}=0$ on $r=R$. It remains to specify the boundary conditions on $z=H$. In order to specify this condition we again recognise that the debonded region has no influence on the remote surface $z=H$ and thus the electric potential is spatially uniform on that boundary. Without loss of generality, we can set $\phi=-\mathcal{U}$ on $z=H$ so that the areal current density $j_{\infty}$ (current per unit area of the electrode/electrolyte interface) in the absence of the debonded region is

$$
j_{\infty}=\frac{\phi_{\text{p}}}{(H/\kappa+Z)}. \tag{2.5}
$$

Thus, it is convenient to describe the loading in terms of $j_{\infty}$ rather than the electrode potential $\phi_{\text{p}}$ and recast the governing equation $\phi_{,ii}=0$ and associated boundary conditions in terms of $\tilde{\phi}\equiv\phi+\mathcal{U}$ so that the open circuit potential $\mathcal{U}$ no longer needs to be explicitly specified.

The solution of these equations requires the coupled solution of flux in the electrolyte and the deformation of the electrode due to the term involving $T_{i}$ in (2.4). However, in nearly all practical cases the term involving $T_{i}$ can be neglected. To understand this recall that $T_{i}n_{i}$ cannot exceed approximately $3\sigma_{0}$ where $\sigma_{0}\approx$ 1 MPa [15] is the representative flow strength of Li. With $\Omega_{\text{Li}}\approx13\times10^{-6}\ \text{m}^{3}\text{mol}^{-1}$ [9] it follows that $T_{i}n_{i}\Omega_{\text{Li}}/F\approx0.4$ mV. With $\eta=5$ mV as discussed above, it is clear that under realistic imposed loadings (currents) $\eta\gg T_{i}n_{i}\Omega_{\text{Li}}/F$ and we shall proceed by neglecting the $T_{i}n_{i}\Omega_{\text{Li}}/F$ term in (2.4). Consequently, the flux distribution within the electrolyte is now decoupled from the deformation of the electrode allowing us to first solve for the flux in the electrolyte and thereby use the interfacial flux in Section 3 to evaluate the deformation of the electrode. Decoupling of the electrode deformation from the electrolyte flux significantly simplifies the problem. Dimensional analysis for this linear problem (linear Butler-Volmer kinetics, decoupled electrode deformation and a linear flux law within electrolyte) then requires that the interfacial flux distribution is given by

$$
\frac{j}{j_{\infty}}=f\left[\bar{r}\equiv\frac{r}{a},\bar{a}\equiv\frac{a}{\kappa Z}\right], \tag{2.6}
$$

where, $r$ is the radial position along the interface. Thus, in the following section we shall present the results in terms of the non-dimensional debonded zone size $\bar{a}$. The governing Laplace equation for flux within the electrolyte was solved via the finite element (FE) method using the commercial FE software ABAQUS. The FE mesh comprises 8-node quadratic axisymmetric elements of size $\approx10^{-3}a$ in the vicinity of the debonded region.

### 2.1. Numerical results

Predictions of the spatial distribution of normalised interfacial flux $j/j_{\infty}$ are plotted in Fig. 2a as a function of the normalised radial position $\bar{r}\equiv r/a$ for four choices of the normalised debonded zone size $\bar{a}$. A flux concentration develops at the edge

![](./images/812478695263436800_8.jpg)
![](./images/812478695263436800_9.jpg)

Fig. 2. (a) Distribution of the normalised flux $j/j_\infty$ along the electrolyte/electrode interface for normalised debonded patch radii $\bar{a} \equiv a/\kappa Z = 0.1, 3, 10, 100$. (b) The corresponding flux concentration factor $k_J$ as a function of the size of the debonded patch. The lower $x$-axis shows the normalised radius $\bar{a}$ while the upper $x$-axis shows the patch radius $a$ in $\mu$m for an assumed value of $\kappa Z = 20$ $\mu$m which is representative of a well-conditioned Li/LLZO interface.

of the debonded zone (i.e., around $\bar{r} \approx 1$) with the flux attaining its far-field value of $j_\infty$ for $\bar{r} > 2$ in all cases. Importantly, the flux concentration factor $k_J \equiv (j/j_\infty)_{\bar{r}=1}$ increases with increasing $\bar{a}$, see Fig. 2b. $^1$ It is instructive to relate these results to a physical size of the debonded zone for which we need to choose values of the electrolyte conductivity $\kappa$ and the interfacial resistance $Z$. The conductivity of LLZO is $\kappa = 0.4$ mScm$^{-1}$ [14] and the interfacial resistance $Z = 5$ $\Omega$cm$^2$ is representative of a well-conditioned Li/LLZO interface [14] as mentioned above. Thus, $\kappa Z = 20$ $\mu$m; the size $a$ of the debonded zone is shown on the upper $x$-axis of Fig. 2b assuming this value of $\kappa Z$. Typically, in the early stages of void formation voids of size $\sim 1$ $\mu$m [7] have been observed at Li/LLZO interfaces. It is clear from Fig. 2a that the flux concentration is negligible for voids of micron size, with flux concentrations $k_J > 2$ only for large debonded patches of size $2a > 60$ $\mu$m. For the sake of completeness, we include in Fig. 3 predictions of the spatial distribution of the normalised flux $j_z/j_\infty$ within the electrolyte adjacent to the debonded zone for three values of $\bar{a}$. Consistent with the $j/j_\infty$ distributions, the debonded patch perturbs the magnitude of $j_z$ only within a zone of extent $\sim 2a$ with $j_z \approx j_\infty$ more remotely from the debonded patch.

## 3. Creep deformation of the Li anode

We proceed to analyse the deformation of the Li electrode due to the spatially non-uniform interface flux distribution (Fig. 2a). At issue is whether there is a tendency for the Li electrode to separate from the electrolyte along the debonded patch and thereby initiate the growth of a void.

In line with an extensive literature [15,16] on the mechanical properties of Li at room temperature, we model Li as an incompressible, power-law creeping solid. Specifically, we assume that the strain rate $\dot{\varepsilon}_{ij}$ scales with the deviatoric stress $S_{ij}$ according to the relation

$$
\dot{\varepsilon}_{ij} = \frac{3}{2} \dot{\varepsilon}_0 \left( \frac{\sigma_e}{\sigma_0} \right)^{m-1} \frac{S_{ij}}{\sigma_0}. \tag{3.1}
$$

where $\sigma_0$ and $\dot{\varepsilon}_0$ are the reference stress and strain-rate, respectively, while $m$ is the power-law exponent. The deviatoric stress is related to the Cauchy stress $\sigma_{ij}$ via $S_{ij} \equiv \sigma_{ij} - \delta_{ij}\sigma_{kk}/3$, where $\delta_{ij}$ is the Kronecker delta and $\sigma_e \equiv \sqrt{(3/2)S_{ij}S_{ij}}$ is the von-Mises effective stress. Now idealise the electrode by a circular cylinder of radius $R$ and height $L$ in the $z-$direction as shown in Fig. 1d. Other than the surface of the electrode in contact with the electrolyte, all other surfaces are assumed to be traction-free: we consider here a cell with zero stack pressure. On the electrolyte/electrode interface ($z = 0$) we impose the following boundary conditions to simulate the flux of Li$^+$ across the interface

$$
\begin{aligned}
T_i &= 0 \quad &\text{over} \quad 0 \leq r < a, \\
v_i n_i &= j(\bar{r}, \bar{a})\Omega_{\text{Li}}/F \quad &\text{over} \quad r \geq a,
\end{aligned} \tag{3.2}
$$

where $v_i$ is the point-wise velocity of material on the Li electrode surface of outward normal $n_i$. Here $j(\bar{r}, \bar{a})$ is the interfacial flux distribution as calculated in Section 2 (Fig. 2a); recall that it is a function of the normalised debonded patch size $\bar{a}$. In addition to (3.2), we need to specify a tangential boundary condition over $r \geq a$. We shall present results for simulations with either (i) frictionless sliding of the electrode over the electrolyte surface such that $T_i s_i = 0$ where $s_i$ is a unit tangential vector along the electrode/electrolyte interface; or (ii) sticking friction such that $v_i s_i = 0$.

All results are presented using the measured creep properties of Li at room temperature, viz. $\sigma_0 = 1$ MPa and $\dot{\varepsilon}_0 = 0.01$ s$^{-1}$ and $m \approx 5$ [15,16]. In addition, we present numerical results for creep exponents over the range $1 \leq m \leq 20$ in order to investigate the sensitivity of our findings to the mechanism of creep deformation (i.e., viscous creep via the Coble or Nabarro-Herring mechanisms correspond to $m = 1$ while dislocation creep typically results in $m \approx 5$ [17]; significantly higher power-law exponents have been measured for some metals). All results (viz. the instantaneous velocity and strain-rate fields) are restricted to time $t = 0$ where the electrode geometry has remained unchanged.

### 3.1. Velocity field over the debonded patch

First consider the case of frictionless contact between the electrode and electrolyte so that the electrode can freely slide over the electrolyte surface. Predictions of the distribution of the normalised velocity $v_z/v_\infty$ on the electrode surface over the debonded patch are included in Fig. 4a and b for $\bar{a} = 0.1$ and 10, respectively for selected values of $m$. Here, $v_z$ is the velocity in the $z-$direction and $v_\infty \equiv j_\infty \Omega_{\text{Li}}/F > 0$ is the velocity of

$^1$ Some spot 3D calculations with elliptical debonded zones were performed to determine the effect of the debonded zone shape on the flux concentration factor. For ellipses of aspect ratio $<5$ the results in Fig. 2b hold to within 15% with the radius $a$ replaced by the length of the semi-major axis of the ellipse.

![](./images/812478695263436800_10.jpg)

Fig. 3. Spatial distribution of the normalised flux $j_{z}/j_{\infty}$ in the electrolyte around the debonded patch for normalised debonded patch radii (a) $\bar{a}=0.1$, (b) $\bar{a}=1$ and (c) $\bar{a}=10$. The electrolyte region is shown using the non-dimensional co-ordinates $(\bar{z}\equiv z/a,\bar{r}\equiv r/a)$.

![](./images/812478695263436800_11.jpg)

Fig. 4. Distribution of the normalised velocity $v_{z}/v_{\infty}$ in the Li electrode over the surface of the debonded patch for normalised patch radii (a) $\bar{a}=0.1$ and (b) $\bar{a}=10$. Results are shown as a function of the normalised radial co-ordinate $\bar{r}\equiv r/a$ for selected choices of the power-law exponent $m$ and frictionless contact between the electrode and the electrolyte.

Li metal along the electrode/electrolyte interface remote from the debonded patch. These results plotted in this normalised form are independent of the stripping current $j_{\infty}$. This feature is a consequence of the linearity of the flux relations within the electrolyte discussed in Section 2; viz. the form of the spatial distribution of the velocity as given in (3.2) is independent of the current $j_{\infty}$ (see Fig. 2a) and hence $v_{z}/v_{\infty}$ is also independent of $j_{\infty}$.

To interpret these results, recall that the electrolyte is stationary. Therefore, $v_{z}/v_{\infty}<0$ implies separation of the electrode from the electrolyte and growth of a void, while $v_{z}/v_{\infty}>0$ implies the electrode has a tendency to develop a contact pressure over the electrolyte surface along the debonded patch in order to prevent penetration of the electrode into the electrolyte. We emphasise that we do not model these contact tractions and interpret $v_{z}/v_{\infty}>0$ as implying that a contact pressure developed with no tendency to form a void. The results show that for nearly all cases considered in Fig. 4, $v_{z}/v_{\infty}>0$ with the exception being $m=20$ and $\bar{a}=10$ where we see there is a small negative value of $v_{z}/v_{\infty}$ for $\bar{r}<0.7$. Recall that Li has a power-law creep exponent $m\approx5$ and thus the calculations suggest that void growth is not expected to occur in Li electrodes. In fact, they suggest that void growth would only occur with $m=20$ for large debonded zones with $\bar{a}=10$. Recall that $\kappa Z=20\ \mu\text{m}$ for practical Li/LLZO interfaces and thus $\bar{a}=10$ corresponds to a debonded patch of size $2a=400\ \mu\text{m}$: voids on the order of $1\ \mu\text{m}$ have been observed to form [7] and thus these calculations suggest that creep deformation of the Li electrode coupled to Butler-Volmer kinetics is insufficient to explain the observed formation of voids. In particular our calculations show that dislocation creep (power-law creep) in Li has a tendency to collapse voids that might tend to form due to small levels of flux focussing around imperfections.

The spatial velocity distribution over the debonded patch surface is reasonably uniform except at the edge of the patch where the velocity is set by the flux across the electrode/electrolyte interface. Thus, the velocity $v_{0}\equiv v_{z}(r=0)$ can be used to summarise the sensitivity of the flux concentration to $\bar{a}$ and $n$. Predictions of $v_{0}/v_{\infty}$ as function of $\bar{a}$ are plotted in Fig. 5a and b, respectively, for the cases of frictionless and sticking contact between the electrode and electrolyte surfaces. The upper $x$-axis in these figures shows the debonded patch size $a$ in $\mu\text{m}$ assuming $\kappa Z=20\ \mu\text{m}$. Qualitatively, the conclusions remain unchanged between the frictionless and sticking friction cases except that the tendency for void growth is slightly enhanced with sticking contact. We emphasise that for the case of an Li electrode with a power-law exponent $m=5$ void growth will only occur for debonded patch sizes $2a\geq1200\ \mu\text{m}$, which is unrealistically large. Void growth is predicted at these large debonded patch sizes because the flux concentration factor is higher for larger values of $\bar{a}$ (Fig. 2b). To get void growth from smaller debonded patch sizes we require higher flux concentration factors than those in Fig. 2b and we thus conclude that the flux focussing predicted by Butler-Volmer kinetics is insufficient to explain the observed formation of voids in Li anodes. In particular our calculations show that dislocation creep (power-law creep) in Li has a tendency to collapse voids that might tend to form due to small levels of flux focussing around imperfections. We note in passing that the inclusion of stack pressure will only enhance the tendency for void collapse while our current calculations cannot even predict the growth of voids in the absence of stack pressure — thus calculations with stack pressure are omitted in this study.

![](./images/812478695263436800_12.jpg)
![](./images/812478695263436800_13.jpg)

Fig. 5. The normalised velocity $v_0/v_\infty$ in the electrode at the centre of the debonded patch ($v_0 \equiv v_z(\bar{r}=0)$) as a function of the debonded patch size for (a) frictionless contact and (b) sticking contact between the electrode and electrolyte. The lower $x$-axis shows the normalised patch radius $\bar{a}$ while the upper $x$-axis shows the patch radius in $\mu$m for an assumed value of $\kappa Z=20\ \mu$m which is representative of a well-conditioned Li/LLZO interface.

Our calculations clearly show that additional physics is needed in order to give a larger flux concentration at the periphery of the defect than that predicted by standard Butler-Volmer kinetics. A recent study [18] has suggested that dislocations within the Li electrode result in a break-down of standard Butler-Volmer kinetics and higher levels of flux focussing around imperfections.

### 3.2. Deformation mechanisms

The results presented in Figs. 4 and 5 suggest that the tendency for the debonded patch to separate from the electrolyte surface increases with increasing $\bar{a}$ and $m$ (i.e., $v_0$ reduces with increasing $\bar{a}$ and $m$). In order to understand the changes in the deformation fields within the electrode which give rise to this effect we include in Fig. 6 contours of strain-rate in a region of the electrode around the debonded patch. Specifically, the normalised von-Mises strain rate $\dot{\varepsilon}_e/\dot{\varepsilon}_r$ is plotted, where $\dot{\varepsilon}_e \equiv \sqrt{(2/3)\dot{\varepsilon}_{ij}\dot{\varepsilon}_{ij}}$ and $\dot{\varepsilon}_r \equiv v_\infty/(\kappa Z)$ is a representative strain-rate associated with the loading. Streamlines are included in Fig. 6 (with the length of the arrow proportional to the magnitude of the velocity) showing the flow patterns within the electrode. Results are included for two debonded patch sizes $\bar{a}=0.1$ (Fig. 6a - c) and $\bar{a}=10$ (Fig. 6d - f) with $m=1,5$ and 20 in each case. Clearly, the effective strain-rate $\dot{\varepsilon}_e$ around the debonded patch increases with increasing $\bar{a}$ and $m$. Moreover, the size of the region where high strain-rates develop also increases with increasing $\bar{a}$ and $m$. The relatively low strain-rates for the $\bar{a}=0.1$ cases (Fig. 6a - c) implies that the velocity fields are nearly uniform and there is a strong tendency for the Li to flow towards the electrolyte over the debonded patch and thereby develop compressive contact tractions between the electrode and electrolyte. In contrast, for the $\bar{a}=10$ cases (Fig. 6d - f) the high strain-rates near the edge of the patch result in non-uniform velocity fields in the $\bar{r}<1$ region. This non-uniformity is most evident in the $(\bar{a},m)=(10,20)$ case (Fig. 6f) where we observe the velocity $v_z \approx 0$ for $\bar{r}<0.7$ over $\bar{z}=0$.

### 4. The role of interfacial diffusion

The above analysis, based on creep deformation of the Li electrode, inherently accounts for vacancy diffusion within the bulk. However, it cannot explain the observed void growth in the electrode when combined with usual Butler-Volmer kinetics. It therefore remains to investigate the role of Li diffusion along the electrode/electrolyte interface. Consider the electrode with the debonded patch as shown in Fig. 1d. The spatial gradient of tractions along the electrode/electrolyte interface creates a diffusive flux of Li from the edge of the debonded zone along the interface. The interfacial radial flux of Li at the tip $r=a$ of the debonded zone is given by

$$
J_b = \left. \frac{D_b \delta_b}{\mathfrak{R}T} \frac{\partial T_n}{\partial r} \right|_{r=a}, \tag{4.1}
$$

where $D_b$ and $\delta_b$ are the interfacial diffusion co-efficient of Li and interface thickness, respectively while $T_n \equiv T_i n_i$ is the normal interfacial traction. Then the rate $\dot{h}$ of debonding of the electrode from the electrolyte follows from mass conservation as

$$
\dot{h} = \frac{2J_b \delta_b \Omega_{\text{Li}}}{a} = \left. \frac{2\delta_b^2 D_b \Omega_{\text{Li}}}{a\mathfrak{R}T} \frac{\partial T_n}{\partial r} \right|_{r=a}. \tag{4.2}
$$

This debonding rate is counteracted by the tendency of the debonded electrode patch to push against the electrolyte due to the overall stripping flux, i.e., a tendency to close a void. This closing velocity is $j_\infty \Omega_{\text{Li}}/F$ and thus it is instructive to examine the ratio

$$
\Pi \equiv \frac{\dot{h}F}{j_\infty \Omega_{\text{Li}}} = \left. \frac{2\delta_b^2 D_b F}{a\mathfrak{R}T j_\infty} \frac{\partial T_n}{\partial r} \right|_{r=a}. \tag{4.3}
$$

The physical significance of this ratio is that if $\Pi \ll 1$, the interfacial diffusive flux cannot counteract the closing of the void due to $j_\infty$ and voids will tend to collapse. It is clear from (4.3) that with increasing stripping flux $j_\infty$ and debonded zone size $a$, $\Pi$ reduces, i.e., the tendency to form voids reduces with increasing $j_\infty$ and $a$ in contrast to observations. This immediately suggests that interface diffusion plays a negligible role in void growth at the Li electrode/electrolyte interface. Nevertheless, it is worth quantifying the ratio $\Pi$.

Adhesion between Li and electrolytes such as LLZO is strong [6] and thus it is reasonable to take $D_b \delta_b$ to be the self-diffusion co-efficient of Li. At $T=300$ K, $D_b \delta_b=8 \times 10^{-15}\ \text{m}^2\text{s}^{-1}$ [19] while a reasonable estimate of the interface thickness is $\delta_b=1$ nm. Moreover, plasticity theory (confirmed by our FE calculations of Section 3) specifies that

$$
\left. \frac{\partial T_n}{\partial r} \right|_{r=a} \approx \frac{\sigma_0}{a}. \tag{4.4}
$$

Taking $a=1\ \mu$m (i.e., debonded zones of size observed in [5]) and $j_\infty=1$ mAcm$^{-2}$, we observe that $\Pi \approx 0.006\%$, i.e., the closing rate of the void due to the stripping flux exceeds the

![](./images/812478695263436800_14.jpg)

Fig. 6. Spatial distributions of normalised creep strain-rate $\dot{\varepsilon}_{e}/\dot{\varepsilon}_{r}$ within the electrode for debonded patch radii (a)-(c) $\bar{a}=0.1$ and (d)-(f) $\bar{a}=10$ with frictionless contact between the electrode and electrolyte. The electrode region is shown using the non-dimensional co-ordinates $(\bar{z}\equiv z/a, \bar{r}\equiv r/a)$. Distributions are shown for power-law exponents $m=1$(a, d), 5 (b, e) and 20 (c, f) in each case. The arrows are streamlines showing both the normalised material velocity magnitudes and directions with the scale bar for the normalised velocity magnitude shown at the bottom of the figure. The arrows on the top surface show the velocity distribution on the electrode surface at the electrode/electrolyte interface.

debonding rate due to interfacial diffusion by a factor of 16000.
This confirms that interfacial diffusion plays a negligible role in
driving the growth of voids in Li anodes.

## 5. Concluding discussion

We have analysed the coupled power-law creep deformation
of an Li electrode due to the stripping flux of Li from the elec-
trode into a single-ion conductor solid electrolyte. Creep of the Li
electrode is initiated by the presence of a debonded patch along
the electrode/electrolyte interface. The debonded patch blocks
the local stripping of $Li^{+}$ and provides a traction free surface.
The hypothesis we have tested is whether the presence of such
an imperfection/debonded patch can initiate void growth in the
electrode during stripping as observed in experiments.

Our numerical results show that, with Butler-Volmer kinet-
ics governing the interfacial flux, void growth can only initiate
from unrealistically large debonded patch sizes (patch diameters
$> 1200\ \mu\mathrm{m}$) in a Li electrode that follows power-law creep
with $m\approx5$. Moreover, we show that interfacial diffusion of Li
along the electrode/electrolyte interface also is unable to strip Li
sufficiently rapidly from the void to overcome the tendency to
close voids due to the overall flow of Li from the electrode into the
electrolyte during stripping, i.e., interfacial diffusion cannot give
rise to void growth. We thus conclude that flux focussing much
larger than that predicted by Butler-Volmer kinetics is required
in order to grow voids from micron-sized imperfections. Such an
understanding remains a topic for future work although a recent
study [18] has suggested that dislocations within the Li electrode
result in a break-down of standard Butler-Volmer kinetics and
higher levels of flux focussing around imperfections.

### Declaration of competing interest

The authors declare that they have no known competing finan-
cial interests or personal relationships that could have appeared
to influence the work reported in this paper.

### Acknowledgement

The authors acknowledge support by the Faraday Institution
through SOLBAT, grant number FIRG007.

### References

[1] K.B. Hatzell, et al., Challenges in lithium metal anodes for solid-state batteries, ACS Energy Lett. 5 (3) (2020) 922-934.

[2] K.N. Wood, M. Noked, N.P. Dasgupta, Lithium metal anodes: toward an improved understanding of coupled morphological, electrochemical, and mechanical behavior, ACS Energy Lett. 2 (3) (2017) 664.

[3] C. Monroe, J. Newman, The impact of elastic deformation on deposition kinetics at lithium/polymer interfaces, J. Electrochem. Soc. 152 (2) (2005) A396.

[4] C. Monroe, J. Newman, The effect of interfacial deformation on electrodeposition kinetics, J. Electrochem. Soc. 151 (6) (2004) A880.

[5] T. Krauskopf, et al., Toward a fundamental understanding of the lithium metal anode in solid-state batteries-An electrochemo-mechanical study on the garnet-type solid electrolyte Li6.25Al0.25La3Zr2O12, ACS Appl. Mater. Interfaces 11 (15) (2019) 14463-14477.

[6] A. Sharafi, et al., Surface chemistry mechanism of ultra-low interfacial resistance in the solid-state electrolyte Li7La3Zr2O12, Chem. Mater. 29 (2017) 7961-7968.

[7] J. Kasemchainan, et al., Critical stripping current leads to dendrite formation on plating in lithium anode solid electrolyte cells, Nat. Mater. 18 (10) (2019) 1105-1111.

[8] E. Kazyak, et al., Li penetration in ceramic solid electrolytes: operando microscopy analysis of morphology, propagation, and reversibility, Matter (2020).

[9] S. Shishvan, et al., Dendrites as climbing dislocations in ceramic electrolytes: Initiation of growth, J. Power Sources 456 (2020) 227989.

[10] M.J. Wang, R. Choudhury, J. Sakamoto, Characterizing the Li-solid-electrolyte interface dynamics as a function of stack pressure and current density, Joule 3 (9) (2019) 2165-2178.

[11] M.B. Dixit, et al., Synchrotron imaging of pore formation in Li metal solid state batteries aided by machine learning, ACS Appl. Energy Mater. (2020).

[12] M.J. Wang, R. Choudhury, J. Sakamoto, Characterizing the Li-solid-electrolyte interface dynamics as a function of stack pressure and current density, Joule 3 (9) (2019) 2165.

[13] H. Schmalzried, J. Janek, Chemical kinetics of phase boundaries in solids, Ber. Bunsenges. Phys. Chem. 102 (2) (1998) 127-143.

[14] A. Sharafi, et al., Controlling and correlating the effect of grain size with the mechanical and electrochemical properties of Li7La3Zr2O12 solid-state electrolyte, J. Mater. Chem. A 5 (40) (2017) 21491-21504.

[15] W.S. LePage, et al., Lithium mechanics: Roles of strain rate and temperature and implications for lithium metal batteries, J. Electrochem. Soc. 166 (2) (2019) A89.

[16] A. Masias, et al., Elastic, plastic, and creep mechanical properties of lithium metal, J. Mater. Sci. 54 (3) (2019) 2585.

[17] P. Sargent, M.F. Ashby, Deformation mechanism maps for alkali metals, Scr. Metall. 18 (2) (1984) 145-150.

[18] S. Shishvan, N.A. Fleck, V.S. Deshpande, The initiation of void growth during stripping of Li electrodes in solid electrolyte cells, J. Power Sources 488 (2021) 229437.

[19] R. Messer, F. Noack, Nuclear magnetic relaxation by self-diffusion in solid lithium:T₁-frequency dependence, Appl. Phys. 6 (1975) 79-88.

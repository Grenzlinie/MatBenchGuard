![](./images/812724542584651776_1.jpg)

Solvation forces and liquid-solid phase equilibria for water confined between hydrophobic surfaces

Kenichiro Koga

Citation: J. Chem. Phys. 116, 10882 (2002); doi: 10.1063/1.1480855
View online: http://dx.doi.org/10.1063/1.1480855
View Table of Contents: http://jcp.aip.org/resource/1/JCPSA6/v116/i24
Published by the AIP Publishing LLC.

---

Additional information on J. Chem. Phys.
Journal Homepage: http://jcp.aip.org/
Journal Information: http://jcp.aip.org/about/about_the_journal
Top downloads: http://jcp.aip.org/features/most_downloaded
Information for Authors: http://jcp.aip.org/authors

ADVERTISEMENT

![](./images/812724542584651776_2.jpg)

# Solvation forces and liquid-solid phase equilibria for water confined between hydrophobic surfaces

Kenichiro Koga${}^{\mathrm{a}}$

Department of Chemistry, Baker Laboratory, Cornell University, Ithaca, New York 14853-1301

(Received 20 November 2001; accepted 1 April 2002)

Solvation force and phase behavior of water confined between hydrophobic surfaces at nanoscale distances have been studied by molecular dynamics simulation of the TIP4P model water. Freezing and melting of confined water are observed at certain intersurface separations in bringing one surface to the other at a fixed temperature and a fixed lateral or bulk pressure. Solvation force curves are found to be discontinuous upon freezing and melting of confined water and exhibit strong hystereses, implying a peculiar manifestation of the hydrophobic effect. The thermodynamics for a confined system at fixed surface separation, temperature, and lateral or bulk pressure is applied for examining the liquid-solid equilibria of confined water. © 2002 American Institute of Physics.
[DOI: 10.1063/1.1480855]

## I. INTRODUCTION

When a fluid is confined in a narrow pore, its phase behavior becomes much richer than that of a bulk fluid. Many theoretical and computer experimental studies of relatively simple model fluids have illuminated various kinds of phase transition under confinement, such as confinement-induced freezing transitions, wetting and drying transitions, and prewetting and predrying transitions. ${}^{1-3}$ Less understood are the phase equilibria of confined complex fluids whose intermolecular interaction is highly directional such as a hydrogen bond interaction. Confined water is an example of this kind and a subject of this paper. Phase equilibria of confined water is of general interest since they might be playing some important roles in biological and geological processes. Also interesting is the effect of confinement on the low-temperature anomalies of water. $^{4}$

Recent computer simulation studies of confined water have revealed bilayer liquid-to-bilayer solid phase transitions ${}^{5,6}$ which are manifestation of a perfect hydrogen bond network under quasi-two-dimensional confinement. In these simulations, the phase transitions have been observed by changing temperature, $T$, in steps under constant normal pressure, $P_{zz}{}^{5}$ (the intersurface separation distance, $H$, being not fixed) and under constant lateral pressure, $P_{xx}{}^{6}$ ($H$ being fixed). Lowering temperature of the former system leads to a bilayer ice crystal $^{5}$ whereas that of the latter system gives rise to a bilayer amorphous phase. $^{6}$ The liquid-to-bilayer amorphous solid transition is an important example of the polyamorphic transition $^{7}$ because of its strong first-order character and because of the clear difference between two phases (both in structure and dynamics). $^{6}$

The present work demonstrates that liquid-solid first-order phase transitions are observed by changing the distance $H$ under fixed $(T,P_{xx})$ and fixed $(T,P)$ [or $(T,\mu)$] conditions, where $P$ is the pressure of a bulk phase in equilibrium with the confined phase and $\mu$ the chemical potential being uniform throughout the bulk and confined phases. The solvation force curves exhibit discontinuous changes and large hysteresis due to the freezing and melting transitions of confined water. Thermodynamic description of this system enables us to examine the phase boundaries in the $P_{xx}HT$ and $\mu HT$ spaces.

## II. SIMULATION MODEL, METHOD, ENSEMBLE

### A. Lateral-pressure controlled system

Figure 1 shows a model system comprising two parallel walls and $N$ molecules confined between them. The total potential energy of the system is written as
$$
U=\sum_{i=1}^{N-1} \sum_{j=i+1}^{N} \phi(r_{ij})+\sum_{i=1}^{N} V(r_{i}), \tag{1}
$$
where the pair potential $\phi$ is the TIP4P water potential $^{8}$ and its argument $r_{ij}$ presents both the distance between molecules $i$ and $j$ and their orientations. The long-range water-water intermolecular potential is smoothly truncated at $r_{c}=8.75$ Å. The external potential $V$ is a field due to the two parallel walls vertical to $z$ axis and fixed at $z_{\mathrm{wall}}=\pm H/2$. The potential energy depends on the distance of the TIP4P interaction site for an oxygen atom from the origins of the walls. That is, $V$ is a function of $z$ coordinate of the oxygen site only:
$$
V(z)=\sum_{\mathrm{wall}} v(|z-z_{\mathrm{wall}}|), \tag{2}
$$
where $v(z)=A/z^{9}-B/z^{3}$ is the 9-3 Lennard-Jones (LJ) potential $^{9}$ with parameters $A$ and $B$ chosen for the interaction between water and a "hydrophobic" solid surface. $^{10}$

The simulation cell is a rectangular prism (lamella) with lateral dimensions $L_{x}$ and $L_{y}$. Periodic boundary conditions are imposed in the $x$ and $y$ directions. This system is basically a quasi-two-dimensional system since the height $(H)$ is

${}^{\mathrm{a}}$Permanent address: Department of Chemistry, Fukuoka University of Education, Munakata, Fukuoka 811-4192, Japan; electronic mail: kk275@cornell.edu

![](./images/812724542584651776_3.jpg)

FIG. 1. Schematic diagrams for the $NP_{xx}T$ constant system (a) and the $NPT$ constant system (b).

finite (typically a few molecular diameters) while the area of walls is assumed to be infinite (by the periodic boundary conditions). As described in the following, the lateral pressure is controlled by allowing changes in lateral dimensions ($L_x$ and $L_y$) in the simulation; this model system is referred to as the lateral-pressure controlled system.

Volume of the system is defined as $V=Ah$, which is the area $A=L_xL_y$ multiplied by the effective height $h=H-2z_0$, where $z_0=2.47$ Å is the distance at which $v(z)=0$. Note that the volume of an inhomogeneous system is not uniquely defined and that the effect of how it is defined is not small if the inhomogeneity is of the order of nanometers, e.g., if $H=2z_0$ (nanometer confinement), then the volume defined here is zero whereas the volume defined as $AH$ is finite. Thus quantities per volume are not uniquely defined either.

Since this system comprises only the confined portion of the fluid (or solid), the number of molecules required in the simulation ($\rho L_xL_yh$) is much smaller than the bulk counterpart ($\rho L_x^3$). This computational advantage permits us to examine the phase behavior of confined fluid in a wide range of thermodynamic phase space, compared to the bulk-pressure controlled system described in the following.

## B. Bulk-pressure controlled system

We devised another system which comprises a confined region and a bulk environment. A schematic diagram of this system is shown in Fig. 1(b). Two parallel walls whose dimension is finite in the $x$ direction ($l_x=30$ Å) and infinite in the $y$ direction are fixed at $z_{\rm wall}=\pm H/2$ and immersed in a bulk fluid. The simulation cell is a rectangular prism with dimensions $L_x$, $L_y$, and $L_z$ containing $N$ molecules and the two walls; periodic boundary conditions are applied to the three directions. The total potential energy of the system has the same form as Eq. (1) but with a different potential field $V$:
$$
V(\mathbf{r})=
\begin{cases}
\sum_{\rm wall}v\left(|z-z_{\rm wall}|\right) & \text{if } |x|\leqslant l_x/2 \\
\sum_{\rm wall}v(r_{\rm wall}) & \text{otherwise}
\end{cases}, \tag{3}
$$
where $r_{\rm wall}=\left\{(x-x_{\rm wall})^2+(z-z_{\rm wall})^2\right\}^{1/2}$ with $x_{\rm wall}=\pm l_x/2$. The long-range interaction for each $v(r)$ is smoothly truncated at $r_c=8.75$ Å (the same distance as $r_c$ for the fluid-fluid interaction). The conditions $r_c<l_x$ and $2r_c<L_x-l_x$ necessary for both the potential and force fields to be continuous everywhere are satisfied with the above-given values for $r_c$ and $l_x$, and with those for other parameters given in the following.

In this system the bulk pressure is controlled by allowing fluctuations in one dimension $L_x$ of the simulation cell. This system enables us to directly relate the solvation force and the phase behavior of a confined system with the thermodynamic condition of the environment, although it requires much more molecules than the $NP_{xx}T$-constant system does.

## C. $NP_{xx}T$ and $NPT$ constant simulations

The method used for the constant-$NP_{xx}T$ molecular dynamics (MD) simulation is similar to the one for the standard $NPT$ MD simulation. $^{11}$ It differs from the standard method in that the lateral dimensions $L_x$ and $L_y$ are allowed to independently change their values while $H$ is fixed. This is more appropriate than the method of changing the lateral dimensions at a fixed ratio if the phase transition to a solid phase is involved as in the present study. The phase behavior was examined mainly by varying the wall-wall separation distance $H$ in steps of 0.1 Å (or larger for large $H$) at two fixed temperatures, 270 and 280 K, and at fixed lateral pressure of 0.1 MPa. The number of molecules was taken to be 240. The average lateral dimensions of the simulation box were then sufficiently large, e.g., $\langle L_x\rangle\sim 35$ Å at 270 K and $H=7.6$ Å. The Gear predictor-corrector method was employed for solving the equation of motion with a time step of 0.5 fs. The simulation time for each thermodynamic state point $(H,P_{xx},T)$ was between 5 and 20 ns, depending on the time required for equilibration. From the simulation, one can directly obtain the pressure $P_{zz}$ exerted on the walls by the confined fluid.

The standard method$^{11}$ is used for the $NPT$-constant MD simulations. In two series of MD simulations, one at 270 K and the other at 250 K, both at $P=0.1$ MPa, the interwall separations $H$ were decreased or increased in steps as in the $NP_{xx}T$ constant system. The number of molecules was taken to be 3350. Two dimensions of the simulation cell were fixed: $L_y=30$ Å and $L_z=60$ Å; the time average of another dimension, $\langle L_x\rangle$, was then nearly the same as $L_z$. The simulation time at each separation is 0.4 ns in most cases and is longer than 2.0 ns in cases when the confined water undergoes a phase transition. In this simulation, the solvation force $f$--the net force acting on the walls per area--is obtained directly.

No direct interaction between two parallel walls is assumed in both $NP_{xx}T$- and $NPT$-constant systems. (Note that the direct interaction would not alter the result of our simulation as the two walls are fixed in space.) Then the total force between the walls obtained from the simulation is purely the solvation force.

Confined fluids in the real world, such as fluids in pores and fluid between two surfaces, are usually in contact with a bulk phase. It is then natural in laboratory experiments that one controls thermodynamic variables of the bulk phase such as $P$ and $T$; in MD simulations, on the other hand, variables of a confined fluid such as pressure-tensor components $P_{ij}$ are controlled [Fig. 1(a)] or the bulk reservoir is treated explicitly at the cost of much heavier computation [Fig. 1(b)]. It should be noted that the former system does not correspond to the pressure-constant experiment because any component of the pressure tensor of a confined phase is not in general the same as the pressure of bulk phase in equilibrium with the confined phase. Direct correspondence with experiments may be achieved by the grand canonical Monte Carlo (GCMC), the Gibbs ensemble method, $^{12}$ or any other method by which the uniformity of the chemical potential is assured between confined and bulk phases. Indeed, the freezing transition in a confined LJ fluid has been studied successfully by GCMC simulations. $^{13}$ The particle (molecule) insertion, however, would be much more difficult if a solid phase of complex fluids is involved as in the present system. We are also interested in dynamical properties of the confined liquid and solid. Thus we have employed the $NP_{xx}T$ and $NPT$ ensemble MD simulations.

### III. THERMODYNAMIC RELATIONSHIPS AND PHASE EQUILIBRIA

Evans and Marini Bettolo Marconi have generalized the thermodynamics of fluids confined between two solid substrates with emphasis on the solvation force and the phase equilibria of an open ($\mu VT$-controlled) system. $^{1}$ Here we describe the thermodynamics of a one-component confined fluid in the $NP_{xx}T$ ensemble and compare thermodynamic relationships with those for the open system.

The infinitesimal change in the internal energy $U$ of the confined system [Fig. 1(a)] is written as
$$
dU=TdS-AP_{zz}dh-P_{xx}hdA+\mu dN. \tag{4}
$$

The natural choice of the thermodynamic potential appropriate to a closed system sketched in Fig. 1(a) is
$$
\Phi=U-AhP_{xx}-TS. \tag{5}
$$

Then its differential is given by
$$
d\Phi=-SdT-A\Delta Pdh+AhdP_{xx}+\mu dN, \tag{6}
$$
where $\Delta P=P_{zz}-P_{xx}$. As $U$ is a homogeneous first-order function of the variable $S$, $A$ and $N$, one has $U=TS -P_{xx}hA+\mu N$ and so from Eq. (5) one has
$$
\Phi=\mu N. \tag{7}
$$

On substituting (7) on the left-hand side of Eq. (6), one obtains the Gibbs–Duhem equation for the confined phase:
$$
d\mu=-sdT-a\Delta PdH+vdP_{xx}, \tag{8}
$$
where $s=S/N$, $a=A/N$, and $v=Ah/N=V/N$; also $dh$ $=dH$ is used. From Eq. (8) one has Maxwell relations: for a fixed lateral pressure $P_{xx}$,
$$
\left(\frac{\partial s}{\partial H}\right)_{P_{xx},T}=\left(\frac{\partial a\Delta P}{\partial T}\right)_{P_{xx},H}, \tag{9}
$$
for a fixed wall-wall distance $H$,
$$
\left(\frac{\partial s}{\partial P_{xx}}\right)_{H,T}=-\left(\frac{\partial v}{\partial T}\right)_{H,P_{xx}}, \tag{10}
$$
and for a fixed temperature $T$,
$$
\left(\frac{\partial v}{\partial H}\right)_{T,P_{xx}}=-\left(\frac{\partial a\Delta P}{\partial P_{xx}}\right)_{T,H}. \tag{11}
$$

Conditions for the phase equilibria between two distinct phases $\alpha$ and $\beta$ in the confined geometry are $T^{\alpha}=T^{\beta}$, $\mu^{\alpha}$ $=\mu^{\beta}$, and $P_{xx}^{\alpha}=P_{xx}^{\beta}$; however the pressures exerted on the walls by phase $\alpha$ and by phase $\beta$ are in general unequal, i.e., $P_{zz}^{\alpha}\neq P_{zz}^{\beta}$. The phase boundary is a surface in the $P_{xx}HT$ space, and the slopes of the surface at fixed $H$, $T$, and $P_{xx}$ are given, respectively, by
$$
\frac{dT}{dP_{xx}}=\frac{v^{\alpha}-v^{\beta}}{s^{\alpha}-s^{\beta}}, \tag{12}
$$
$$
\frac{dP_{xx}}{dH}=\frac{(a\Delta P)^{\alpha}-(a\Delta P)^{\beta}}{v^{\alpha}-v^{\beta}}, \tag{13}
$$
and
$$
\frac{dH}{dT}=-\frac{s^{\alpha}-s^{\beta}}{(a\Delta P)^{\alpha}-(a\Delta P)^{\beta}}. \tag{14}
$$

We utilize these Clapeyron equations in examining phase boundaries between two distinct condensed phases in confined water.

Now we consider thermodynamic relationships for fluids constrained between two plane-parallel walls and open to a bulk environment. $^{1}$ The system consists of fluid molecules in a large container of volume $V_{c}$ and everything else including the two parallel walls immersed in the fluid is the surroundings of that system [Fig. 1(b)]. The volume $V$ of the system is defined as $V_{c}-V_{w}$, where $V_{w}$ is the volume of the two walls defined by dividing surfaces. The dividing surfaces may be chosen arbitrarily from those lying within the fluid–wall interface regions; but a natural choice of the dividing surfaces would be one of the equipotential surfaces for the wall–fluid molecule interactions. Once the dividing surfaces are chosen, it is supposed that the infinitesimal change in $U$ is
$$
dU=-PdV+TdS+\mu dN+2\sigma dA-FdH, \tag{15}
$$
where $F$ is the total force exerted on each wall immersed in the fluid and
$$
\sigma=\frac{1}{2}\left(\frac{\partial U}{\partial A}\right)_{V,S,N,H} \tag{16}
$$

is the fluid-wall surface tension. It is noted that $V$ being fixed in the definition of $\sigma$ does not mean $V_{c}(=V+V_{w})$ being fixed, unless $V_{w}=0$ is assumed. This illustrates that the process of changing $A$ at fixed $V$ depends on how to choose the dividing surfaces defining $V_{w}$. Thus, strictly speaking, the fluid-wall surface tension $\sigma$ defined here depends on the choice of the dividing surfaces. The thermodynamic potential for the open system is the grand potential $\Omega=U-TS-\mu N$, and the equilibrium condition is $(\delta\Omega)_{\mu,T,V,H}=0$. To focus on the properties arising from inhomogeneity, excess quantities are defined following Gibbs' prescription as $S^{\text{ex}}=S-S^{b}$, $N^{\text{ex}}=N-N^{b}$, and $\Omega^{\text{ex}}=\Omega-\Omega^{b}$, where superscript $b$ denotes quantities of a homogeneous bulk system of volume $V$ at the same $\mu$ and $T$ as those for the inhomogeneous system. Then the infinitesimal change in $\Omega^{\text{ex}}$ is written as

$$
d\Omega^{\text{ex}}=-S^{\text{ex}}dT-N^{\text{ex}}d\mu+2\sigma dA-FdH. \tag{17}
$$

Since $\Omega^{\text{ex}}$ is homogeneous of the first degree in $A$, it follows that $\Omega^{\text{ex}}=2\sigma A$, and substituting this for $\Omega^{\text{ex}}$ in Eq. (17), one obtains

$$
2d\sigma=-\eta dT-\Gamma d\mu-fdH, \tag{18}
$$

where $\eta=S^{\text{ex}}/A$, $\Gamma=N^{\text{ex}}/A$, and $f=F/A$. From Eq. (18), one obtains surface Maxwell relations¹ analogous to Eqs. (9)-(11).

For given $(\mu,T,H)$, two distinct phases $\alpha$ and $\beta$ can coexist in the confined region if $(\Omega^{\text{ex}})^{\alpha}=(\Omega^{\text{ex}})^{\beta}$, or $\sigma^{\alpha}=\sigma^{\beta}$. From the latter condition with Eq. (18), the following condition holds at any phase boundary:

$$
(\eta^{\alpha}-\eta^{\beta})dT+(\Gamma^{\alpha}-\Gamma^{\beta})d\mu+(f^{\alpha}-f^{\beta})dH=0. \tag{19}
$$

Thus one finds that the slope of the phase boundary surface at fixed $H$, $T$, and $\mu$, is given, respectively, by¹

$$
\frac{dT}{d\mu}=-\frac{\Gamma^{\alpha}-\Gamma^{\beta}}{\eta^{\alpha}-\eta^{\beta}}, \tag{20}
$$

$$
\frac{d\mu}{dH}=-\frac{f^{\alpha}-f^{\beta}}{\Gamma^{\alpha}-\Gamma^{\beta}}, \tag{21}
$$

and

$$
\frac{dH}{dT}=-\frac{\eta^{\alpha}-\eta^{\beta}}{f^{\alpha}-f^{\beta}}. \tag{22}
$$

It is found that these and Eqs. (12)-(14) are closely analogous.

## IV. FORCE CURVES IN THE $NP_{xx}T$ ENSEMBLE

Figure 2 shows $P_{zz}(H)$ curves obtained from the lateral pressure-controlled simulation. At 280 K, with reducing $H$ from 13.5 to 6.5 Å, $P_{zz}$ oscillates reflecting the structure of the confined liquid [Fig. 2(a)]. The highest peak at around 8 Å corresponds to the force required for squeezing a bilayer to a monolayer. The potential energy also changes continuously at this temperature. Thus no phase transition is observed by changing $H$ at $T=280$ K and $P_{xx}=0.1$ MPa. On changing $H$ at 270 K, however, the force curve exhibits discontinuities accompanied by two hystereses. The first discontinuous change in $P_{zz}$ with reducing $H$ is observed as an abrupt drop at around $H=9$ Å, and then $P_{zz}$ increases rapidly until $H$=7.5 Å, where again a sudden drop is observed. Structural analysis confirms that the confined water undergoes the liquid-to-bilayer amorphous solid phase transition at around 9 Å, and that the amorphous phase is compressed until it melts at 7.5 Å. When $H$ is then increased, $P_{zz}$ changes continuously showing a peak at around 8 Å a peak similar to the one at 280 K and then suddenly jumps to a higher value at 8.2 Å. This jump corresponds to the liquid-to-bilayer amorphous transition. After the transition, $P_{zz}$ decreases with increasing $H$ and eventually takes negative values; but it suddenly jumps at 9.4 Å. The last jump corresponds to the bilayer amorphous-to-liquid phase transition. In this way, the confined water undergoes the liquid-to-amorphous and amorphous-to-liquid transitions with decreasing $H$, and exhibit the transitions in reverse order showing a large hyster-

![](./images/812724542584651776_4.jpg)

FIG. 2. Force $P_{zz}$ acting on the walls against the wall-wall separation distance $H$ at constant lateral pressure $P_{xx}=0.1$ MPa and at constant temperature: a 280 K and b 270 K. Left and right arrows indicate the direction that $H$ is changed.

![](./images/812724542584651776_5.jpg)

FIG. 3. Potential energy $U$ against the wall-wall separation distance $H$ at constant lateral pressure $P_{xx}$=0.1 MPa: (a) 280 K and (b) 270 K. Arrows indicate the same as in Fig. 2

![](./images/812724542584651776_6.jpg)

FIG. 4. Solvation-force curves for confined water: (a) 270 K and (b) 250 K. Arrows indicate the same as in Fig. 2.

esis. The discontinuous force curve and the hystereses reflect the first-order phase transitions of confined water.

The potential energy curve $U$ also reflects phase behavior of confined water, as plotted in Fig. 3. At 280 K, $U$ changes continuously. The pronounced increase in $U$ with decreasing $H$ from around 8.5 $\mathring{A}$ corresponds to structural change from bilayer to monolayer structure, the former being energetically more stable than the latter. A 270 K, upon decreasing $H$, $U$ drops abruptly by 4.5 kJ/mol at $H=8.8$ $\mathring{A}$ and then jumps by 7.6 kJ/mol at $H=7.5$ $\mathring{A}$. These discontinuous changes in $U$ correspond to the liquid-to-solid and solid-to-liquid phase transitions of confined water. Upon increasing $H$ reversely, distinct hystereses are observed.

### V. SOLVATION FORCE CURVES IN THE NPT ENSEMBLE

The solvation force curves between the semifinite "hydrophobic" walls immersed in the TIP4P water are plotted in Fig. 4. At 270 K, the force $f$ oscillates with decreasing $H$ from 15 to 9 $\mathring{A}$. There is a local minimum in $f$ at around 11 $\mathring{A}$ where two walls attract each other by about $-30$ MPa, and as $H$ decreases further $f$ turns to be repulsive—the two walls repel each other by about 70 MPa at $H=9$ $\mathring{A}$. As $H$ is further decreased, the thin film of water between two walls becomes unstable and drainage of molecules to the bulk environment takes place. Due to this drying transition, $f$ drops abruptly and the two walls attract each other at 8.6 $\mathring{A}$. No liquid-to-amorphous phase transition of confined water is observed at this temperature.

The solvation force curve at 250 K, which is around the melting point $(238\pm7$ K) of the TIP4P hexagonal ice, $^{14}$ is qualitatively different from that at 270 K. As shown in Fig. 4(b), when decreasing $H$ from 10 $\mathring{A}$ the solvation force exhibits a sudden drop at 9 $\mathring{A}$, followed by a rapid increase. The rapid increase in $f$ continues until the two walls repel each other by about 1100 MPa, and then the force drops suddenly at 7.8 $\mathring{A}$. When increasing $H$ from 9 $\mathring{A}$, $f$ decreases until the two walls attract each other by $-85$ MPa at 9.5 $\mathring{A}$, and then jumps abruptly to a higher value at 9.6 $\mathring{A}$. Structural analysis shows that the structure of confined water changes from liquid-like random network structure to solid-like nearly perfect network structure at 9 $\mathring{A}$ upon decreasing $H$ (Fig. 5). Figures 5(a) and 5(c) show the structure of the TIP4P water around the pair of semi-finite walls at $H=9.1$ $\mathring{A}$ and $H=9.0$ $\mathring{A}$, respectively. It is found that there exist two molecular layers between the parallel walls in both cases. Significant difference in structure is that at $H$

![](./images/812724542584651776_7.jpg)
![](./images/812724542584651776_8.jpg)

![](./images/812724542584651776_9.jpg)
![](./images/812724542584651776_10.jpg)

FIG. 5. Structures of the TIP4P water around and between the two parallel semi-finite walls at $T=250$ K and $P=0.1$ MPa: (a) side and (b) top view at $H$ $=9.1$ Å and (c) side and (d) top view at $H=9.0$ Å. With decreasing $H$ from 9.1 to $9.0$ Å, the liquid-to-solid (bilayer amorphous) transition of confined water is observed.

$=9.0$ Å, unlike at $H=9.1$ Å, most hydrogen bonds between the two layers are oriented vertically to the walls and few dangling OH bonds exist in the confined region. The difference is more evident in the top views of the confined region [Figs. 5(b) and 5(d)]; disordered network at $H=9.1$ Å turns into the bilayer amorphous network, each layer consisting of 5, 6, 7, and 8 membered rings, at $H=9.0$ Å. This structural change is essentially the same as the one observed in the $NP_{xx}T$ constant system. That is, the discontinuity in $f$ and the distinct hysteresis reflect the liquid-bilayer amorphous phase transition of water confined by the semi-finite hydrophobic walls. As shown in Fig. 4(b), the solid-like phase is stable, or at least metastable, when $7.9$ Å$<H<9.5$ Å at 250 K. Since the temperature is around the melting point of the TIP4P model water, and bulk pressure is set to 0.1 MPa, it is possible that real water under an ambient condition undergoes the confinement-induced phase transition between hydrophobic surfaces. Hydrophilic surfaces with which water molecules form hydrogen bonds would inhibit the liquid-to-solid transition because then energy difference between the confined liquid and solid phases cannot be sufficiently large to balance the entropy difference. $^{6}$ In this regard, the discontinuous solvation force may be taken as a special hydrophobic interaction due to the liquid-solid transition of water. Recent studies based on molecular theory suggest that the drying transition gives rise to an attractive solvation force between the two walls at large length scales. $^{15}$ More recently the grand canonical MC simulation showed that the SPC model water confined between hydrophobic walls at ambient pressure is metastable and evaporates below $H\sim 12.7$ Å. $^{16}$ Thus the liquid film in the present system could also be metastable. In the time scale of our simulation, however, the drying transition has been observed only at a smaller $H$. Our simulation results indicate that the liquid-to-bilayer amorphous solid free-energy barrier is lower than the liquid-to-vapor free-energy barrier under the condition examined. Whether the liquid-amorphous transition or the drying transition takes place at small length scales would depend on $P$ and $T$ of the bulk environment; the former should be observed more likely in a low $T$ and high $P$ region whereas the latter would occur in a high $T$ and low $P$ region.

## VI. PHASE EQUILIBRIA OF CONFINED WATER

In the $NP_{xx}T$-constant system, we have shown that the TIP4P water exhibits the liquid-solid phase transitions upon changing the hydrophobic wall distance $H$ at 270 K and 0.1 MPa. Now we shall examine the phase boundary. Equations (12)-(14) claim that slope of the phase boundary is determined by the ratio of differences in $s$, $v$, and $a\Delta P$ between two coexisting phases. Now let $\alpha$, $\beta$, and $\gamma$ stand for the liquid phase at large $H$, bilayer amorphous solid phase, and the liquid phase at small $H$, respectively. Then, upon decreasing $H$ at 270 K and 0.1 MPa, the three phases $\alpha$, $\beta$, and $\gamma$

<table>
<caption>TABLE I. Differences in $s$, $v$, and $a\Delta P$ between the liquid ($\alpha$) and the bilayer amorphous solid ($\beta$), and between $\beta$ and the liquid ($\gamma$), and slopes of the phase boundaries. All the quantities ($H$, $\Delta s$, etc.) are evaluated at $T=270$ K and $P_{xx}=0.1$ MPa by averaging those at liquid-to-solid and solid-to-liquid transitions. $H$ is in units of Å, $s$ in units of $\text{J mol}^{-1}\text{K}^{-1}$, $v$ in units of Å$^3$, and $a\Delta P$ in units of Å$^2$MPa.</caption>
<tr>
<td>Equilibrium</td>
<td>$H$</td>
<td></td>
<td>Difference in</td>
<td>$dT/dP_{xx}$</td>
<td>$dP_{xx}/dH$</td>
<td>$dH/dT$</td>
</tr>
<tr>
<td>$\alpha$-$\beta$</td>
<td>9.1</td>
<td>$s$</td>
<td>$-17.8$</td>
<td rowspan="3">$-1.5×10^{-2}$</td>
<td rowspan="3">$-1.6×10^3$</td>
<td rowspan="3">$-4.2×10^{-2}$</td>
</tr>
<tr>
<td></td>
<td></td>
<td>$v$</td>
<td>$0.432$</td>
</tr>
<tr>
<td></td>
<td></td>
<td>$a\Delta P$</td>
<td>$-704$</td>
</tr>
<tr>
<td>$\beta$-$\gamma$</td>
<td>7.9</td>
<td>$s$</td>
<td>$22.6$</td>
<td rowspan="3">$6.5×10^{-2}$</td>
<td rowspan="3">$-1.8×10^3$</td>
<td rowspan="3">$8.5×10^{-3}$</td>
</tr>
<tr>
<td></td>
<td></td>
<td>$v$</td>
<td>$2.44$</td>
</tr>
<tr>
<td></td>
<td></td>
<td>$a\Delta P$</td>
<td>$-4423$</td>
</tr>
</table>

appear in that order. Given in Table I is the difference in $x^l$ $-x^m$ (where $x=s$, $v$ or $a\Delta P$ and $l, m=\alpha$, $\beta$, or $\gamma$), which is evaluated approximately from the average of $\Delta x_{m\rightarrow l}$ at the $m$-to-$l$ transition and $-\Delta x_{l\rightarrow m}$ at the reverse $l$-to-$m$ transition. Since $\Delta s=(\Delta u-P_{xx}\Delta v)/T$ [from Eq. (5) and the equilibrium condition $\Phi^l=\Phi^m$] and the second term $P_{xx}\Delta v/T$ is negligible when $P_{xx}=0.1$ MPa, the difference in entropy $\Delta s$ $(=s^\beta-s^\alpha$ or $s^\gamma-s^\beta)$ is given accurately by the first term $\Delta u/T$ alone. It is found that the entropy difference between liquid and bilayer amorphous phases is as much as the difference between bulk water and ice.

Evaluated slopes of the liquid-solid phase boundary are given in Table I. In the $P_{xx}-T$ plane, the $\alpha$-$\beta$ boundary has a negative slope, which is analogous to that of bulk water and ice Ih, whereas the $\beta$-$\gamma$ boundary has a positive slope. In either case, the effect of pressure on the freezing temperature is very small as usual for any liquid-solid phase boundary. In the $H-P_{xx}$ plane, the slopes of $\alpha$-$\beta$ and $\beta$-$\gamma$ are both negative [Fig. 6(a)]. The effect of pressure $P_{xx}$ on the separation distance $H$ is very small at around 0.1 MPa and 270 K. However, at a higher pressure the transition to bilayer amorphous solid phase $(\beta)$ is not observed.⁶ This implies that the two phase boundaries ($\alpha$-$\beta$ and $\beta$-$\gamma$) meet at some higher pressure. In the $T-H$ plane, the slope of $\alpha$-$\beta$ boundary is negative whereas that of $\beta$-$\gamma$ is positive; see Fig. 6(b). At a higher temperature, e.g., 280 K, the bilayer solid phase does not exist for any separation distance $H$. Thus, the two phase boundaries seem to approach and meet each other between 270 and 280 K.

Finally, based on Eqs. (20)–(22) and the $NPT$ simulation results, we shall examine qualitatively the liquid-solid phase boundary of confined water in the $\mu VT$ space. Again let $\alpha$ and $\beta$ denote the liquid film and the bilayer solid film of confined water, respectively. At the $\alpha$-$\beta$ phase boundary at $P=0.1$ MPa, $T=250$ K, and $H=9.3$ Å, we find that $\Gamma^\alpha$ $-\Gamma^\beta>0$, $\eta^\alpha-\eta^\beta>0$, and $f^\alpha-f^\beta>0$. (Here the value of $H$ is estimated as the average of 9.0 and 9.6 Å at which the $\alpha$-to-$\beta$ and the reverse transitions are observed.) Thus, the slopes of the liquid–solid phase boundary in the $\mu-T$, $H-\mu$, and $H-T$ plane are negative. The slopes $(\partial T/\partial\mu)_H$ and $(\partial\mu/\partial H)_T$ of the $\alpha$-$\beta$ phase boundary have the same sign as $(\partial T/\partial P_{xx})_H$ and $(\partial P_{xx}/\partial H)_T$ of that boundary in the $P_{xx}HT$ space. This is consistent with the fact that $P_{xx}$ increases with increasing $\mu$.

## VII. CONCLUDING REMARKS

The MD simulations of two different systems have demonstrated that by changing the distance between hydrophobic surfaces under a constant temperature and a constant pressure ($P_{xx}$ or $P$) the liquid-solid phase transition of the TIP4P water is observed. The solid phase has a bilayer amorphous structure having a fully connected hydrogen-bond network. Due to the phase transition, the solvation force exhibits discontinuous changes and distinct hysteresis. Only when the surface is hydrophobic and the distance is within a certain range (about a nanometer), do water molecules between the surfaces form a fully connected hydrogen-bond network, which is an entropically unfavorable but energetically favorable structure. This hydrophobic effect is profound in that it is accompanied by the first-order phase transition. While recent theoretical studies have shown that the drying transition gives rise to hydrophobic attraction between large molecules or surfaces,¹⁵,¹⁶ our results indicate that the liquid-to-bilayer amorphous solid phase transition also leads to a hydrophobic attraction. So far experimental results confirming the freezing of confined water into bilayer amorphous (or crystalline) solid or demonstrating the discontinuous force presented here have not been reported; but they might be detected by the surface-force apparatus or the atomic force microscopy measurements.¹⁷ The fact that the freezing transition is observed in the $NPT$-constant system suggests that the free energy barrier for the liquid-to-bilayer amorphous solid phase transition is lower than, or at least comparable to, the barrier for the cavitation even under the ambient pressure. Moreover the results of the $NPT$-constant system indicate that the confinement-induced freezing transition could be ob-

![](./images/812724542584651776_11.jpg)

FIG. 6. Schematic phase boundaries between thick liquid film ($\alpha$), bilayer amorphous solid ($\beta$) and thin liquid film ($\gamma$): (a) the $H-P_{xx}$ plane at $T$ $=270$ K and (b) the $T-H$ plane at $P_{xx}=0.1$ MPa.

served not only between infinitely large flat surfaces but also between finite (e.g., $30 \times 30$ Å) flat plates with edges.

## ACKNOWLEDGMENTS
The author thanks Professor H. Tanaka and Professor X. C. Zeng for stimulating discussions on confined water. Professor B. Widom is acknowledged for his warm hospitality and valuable comments on the manuscript. Masniah Morshidi is also acknowledged for her critical reading of the manuscript. This work has been supported by Japan Society for the Promotion of Science (JSPS). The author is visiting Cornell University under JSPS Postdoctoral Fellowship for Research Abroad 2001.

$^{1}$R. Evans and U. Marini Bettolo Marconi, J. Chem. Phys. **86**, 7138 (1987).
$^{2}$R. Evans, J. Phys.: Condens. Matter **2**, 8989 (1990).

$^{3}$L. D. Gelb, K. E. Gubbins, R. Radhakrishnan, and M. Sliwinska-Bartkowiak, Rep. Prog. Phys. **62**, 1573 (1999).
$^{4}$T. M. Truskett and P. G. Debenedetti, J. Chem. Phys. **114**, 2401 (2001).
$^{5}$K. Koga, X. C. Zeng, and H. Tanaka, Phys. Rev. Lett. **79**, 5262 (1997).
$^{6}$K. Koga, H. Tanaka, and X. C. Zeng, Nature (London) **408**, 564 (2000).
$^{7}$O. Mishima and H. Stanley, Nature (London) **396**, 329 (1998).
$^{8}$W. Jorgensen, J. Chandrasekhar, J. Madura, R. Impey, and M. Klein, J. Chem. Phys. **79**, 926 (1983).
$^{9}$W. A. Steele, Surf. Sci. **36**, 317 (1973).
$^{10}$S. H. Lee and P. J. Rossky, J. Chem. Phys. **100**, 3334 (1994).
$^{11}$S. Nosé, J. Chem. Phys. **81**, 511 (1984).
$^{12}$A. Z. Panagiotopoulos, Mol. Phys. **61**, 813 (1987).
$^{13}$M. Miyahara and K. E. Gubbins, J. Chem. Phys. **106**, 2865 (1997).
$^{14}$G. T. Gao, X. C. Zeng, and H. Tanaka, J. Chem. Phys. **112**, 8534 (2000).
$^{15}$K. Lum, D. Chandler, and J. D. Weeks, J. Phys. Chem. B **103**, 4570 (1999).
$^{16}$D. Bratko, R. A. Curtis, H. W. Blanch, and J. M. Prausnitz, J. Chem. Phys. **115**, 3873 (2001).
$^{17}$H. K. Christenson, J. Phys.: Condens. Matter **13**, R95 (2001).
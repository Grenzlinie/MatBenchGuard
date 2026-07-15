# OBSERVATION OF LOCAL MELTING IN AN ALUMINUM BICRYSTAL
## BY MOLECULAR DYNAMICS SIMULATION

Paul S. Ho and Thomas Kwok
IBM Thomas J. Watson Research Center
Yorktown Heights, New York 10598

Tue Nguyen, Cynthia Nitta and Sidney Yip
Department of Nuclear Engineering
Massachusetts Institute of Technology
Cambridge, Massachusetts 02139

(Received May 22, 1985)

## I. Introduction
It has been recognized for some time that grain boundaries can exist in different struc- tures and that a boundary may undergo phase transitions similar to transformation in the bulk [1]. There exist indications from theoretical analysis using a lattice gas model [2] and from electron microscope data [3] that grain boundary melting can occur at a temperature distinctly below bulk melting. There are molecular dynamics simulation studies which show either a melt- ing phenomenon [4,5] or a premelting structural transition [6,7]. Also, boundary phase trans- formation has been inferred from the observed temperature variation of kinetic properties such as boundary mobility, atomic diffusivity, and intergranular cohesive strength [8].

In this Letter we report a molecular dynamics simulation study of the structural behavior at elevated temperatures of a bicrystal model of aluminum [9]. We focus on the stability of the grain boundary structure against thermal excitations by monitoring principally an order parameter (defined below) but considering also other properties such as the internal energy, the mean square displacement, and snapshots of atomic configurations. We find the bicrystal to un- dergo a gradual structural transition at the onset of which the grain boundary core shows sig- nificant disorder and becomes nonstationary. At higher temperatures the disorder becomes more pronounced and the affected region is enlarged. At even higher temperatures which are still below the bulk melting point, loss of crystalline order occurs in such a decisive manner as to suggest a process of local melting. With reference to the melting point $T_{m}$ of a corresponding model of a single crystal, the continuous transition begins at about $0.5T_{m}$ with melting setting in at about $0.7T_{m}$.

## II. Bicrystal Model
Our grain boundary model is a bicrystal composed of 900 atoms arranged in the $\Sigma=5$ symmetrical tilt structure. As shown in Fig. 1 the system is composed of a stack of 10 (001) atomic planes, each containing 18 CSL units with each unit having 5 atoms. The tilt axis is along the y-direction, [001], and the x-y plane contains the boundary. The system has periodic borders along the x- and the y-directions. Along the z-direction, [130], fixed border conditions are imposed to avoid having a second boundary in the simulation cell. A fixed border can give rise to artificial constraints on the layers of atoms adjacent to the border, and allowance must be made for this effect in interpreting the simulation results.

We have adopted two interatomic potential functions of different origin, an empirical Morse potential with parameters chosen to fit the vacancy formation energy [10], and a pseudopotential with nonlocal screening that is derived essentially from first principles [11]. We will present the results obtained using the Morse potential, but will also comment on the less extensive pseudopotential results.


### III. Structure at T = 0

The molecular dynamics simulation technique used in the present study is quite standard. We first determined the relaxed bicrystal structure at zero temperature. This initial relaxa- tion was necessary since in every other (001) plane a pair of atoms in each two CSL units across the boundary were too close to each other (cf. Fig. 1(b)). Different procedures had been used previously for relieving the strong repulsion between the close pair. We adopted the procedure of removing one of the two atoms and allowing the upper and lower crystals to have independent rigid translations, $(\Delta x, \Delta y, \Delta z)$. To find the minimum energy configuration, the relaxed struc- ture at T = 0, we sampled a large set of values of $(\Delta x, \Delta y, \Delta z)$. At a given set of $(\Delta x, \Delta y, \Delta z)$ the simulation cell was heated up to a temperature of $\sim T_{m} / 3$ and gradually cooled down to $T \sim 0$ ; the potential energy at the end of the cooling period was then regarded as the relaxed energy for this particular set of $(\Delta x, \Delta y, \Delta z)$. In this way an energy contour was generated in the space of $(\Delta x, \Delta y, \Delta z)$. We found two low-energy structures. One structure, which will be de- noted as M1, corresponds to $\Delta x=-0.158, \Delta y=0, \Delta z=0$ , in units of a, the lattice constant( $a=4.027 ~A$ at $T=0$ ); it is shown in Fig. 2. This configuration is the same as the Type 1 structure found by Hashimoto et al. using the same potential function but a different relaxa- tion procedure [12]. The other structure, denoted as M2, corresponds to $\Delta x=0.474, \Delta y=0$ , Az = 0.032. This configuration is not the same as the Type 2 structure of Hashimoto et al.[12], although the latter also involves nonzero $\Delta x$ and $\Delta z$ . It should be noted that Type 2 is higher in energy than Type 1, while M1 and M2 are quite close in energy.

### IV. Melting of Single Crystal

To study the bicrystal structure at elevated temperatures we first determined the melting point $T_{m}$ of the corresponding single crystal. We consider the internal energy $U=(1 / 2) \sum^{\prime} V_{i j}$ , where $V_{i j}^{m}$ is the pair interaction potential between atoms $i$ and $j$ , and the prime on the summa tion denotes $i \neq j$ . The variation of $U$ with temperature is shown in Fig. 3 using data obtained from simulation runs of 3000 time steps (one time step corresponds to $1.07 \times 10^{-15} ~s$ ) after an equilibration period of about 1000 time steps. The data suggest a transition taking place around $940 ~K$ , and from the total energy one obtains a latent heat of $\sim 7.4 ~kJ / mol$ . The observed melting point of aluminum is $933.2 ~K$ with latent heat of fusion of $10.79 ~kJ / mol$ .

A more direct measure of structural response to thermal disorder is provided by the orderparameter [6]

$$
\rho_{j}(\underline{K})=\frac{1}{N_{j}} \sum_{\ell=1}^{N_{j}}<\operatorname{Re}\left\{e^{i \underline{K} \cdot \underline{r}_{\ell}}\right\}>
$$

where $\underline{r}_{i}$ is the position of atom $j, \underline{K}$ is a given wave vector, the angular bracket \langle\rangle denotes an average over the trajectories generated during the simulation period, and $N_{1}$ refers to the atoms in a particular region of the simulation cell. As shown in Fig. 2 the bicrystal was divided into 12 equal regions with the boundary core lying in regions 6 and 7. The order parameter re- sults for the different regions and with $\underline{K}$ chosen to be $\underline{K}=(0,2 \pi / a, 0)$ are shown in Fig. 4.[Notice that with this choice of $\underline{K}$ we are probing along a direction where an atom sees the same environment in the bicrystal and the reference single crystal.] Since the single crystal sys- tem is symmetric about the interface between regions 6 and 7, the data for regions 1 and 12 can be combined, etc. These data were obtained from trajectories generated over 3000 time steps at each temperature. It can be seen that the interior regions (4-6) behave in a reasonable manner with an inflection point in $\rho_{i}(\underline{K})$ occurring at about the same temperature as that given by Fig.3. On the other hand, the data for region 1 show clearly the constraining effects of the fixed border. It is expected that if the simulations were carried out to sufficiently long times, there would be no change in the behavior of regions $4-6$ , while $\rho_{1}$ and $\rho_{2}$ would converge to those of the interior regions.

### V. Bicrystal Structure at Elevated Temperatures

Two separate series of simulation runs were carried out using the present bicrystal model. A series of relatively short runs, with each simulation extending over 3000 time steps after equilibration, was made to obtain the order parameter $\rho_{i}$ shown in Fig. 4. Another series of considerably longer runs, extending over intervals between 160 and $200 \times 10^{3}$ time steps with the time step now 3 times longer than that for the short runs, was made at the temperatures T/T= 0.43, 0.54, 0.65, 0.76. The primary purpose of these exceptionally long runs was to gather data on vacancy jumps for the study of grain boundary diffusion [13]. As we will see below, the long trajectories also provide valuable information on structure behavior.

In Fig. 4 one can see a continuous decrease of $\rho_{i}$ with temperature in the boundary core region, region 6 of the bicrystal. Even though we have not shown the data for regions 7-12, they correspond closely with the data for regions 6-1 respectively. This correspondence was destroyed after boundary started to migrate, and this occurred later. In view of the quite dif- ferent behavior of region 6 in the single crystal, this indicates that the effects of increasing thermal motions have a significant influence on structural order in the boundary core. The be- havior of the other regions in Fig. 4 is consistent with the picture that disorder propagates outward from the core region, and since $\rho_{i}$ for region 1 of the bicrystal is about the same as that in the single crystal, one can conclude that over the period of the simulation the un- physical constraining effects of the fixed border are dominant in this region. In interpreting the bicrystal results of Fig. 4 one must keep in mind that in contrast to the single crystal, at a given temperature below $T_{m}$ the $\rho_{j}$ values for different regions in the bicrystal need not be the same no matter how long is the simulation. This assumes that the simulation cell is large enough to allow a bulk crystal region to be stabilized against a grain boundary core region.

The results of the long simulations at $T/T_{m}=0.43,0.54,0.65$ are summarized in Fig. 5. From the time evolution of $\rho_{j}$ one can see how disorder propagated in space and time. When a region is not shown, it means that $\rho_{j}$ for that region $j$ shows no appreciable change over the entire period of simulation. At $T/T_{m}=0.43$ we observe that a slight disorder has appeared in region 7, whereas region 6 is essentially unaffected. The bicrystal structure is stable at this temperature. At $T/T_{m}=0.54$, region 7 becomes strongly disordered first and this struc- tural behavior spreads quickly to region 8. After a considerable period of time (on the scale of typical simulation periods in present-day molecular dynamics studies), region 9 becomes strongly disordered. The qualitative changes in structural behavior at this temperature from that at $T/T_{m}=0.43$ suggest the onset of structural metastability. We feel that a distinction can be made between regions 7 and 8 in that region 7 is highly disordered whereas region 8 is liquid-like in structure. Detailed examination of the instantaneous atomic positions shows that this interpretation is justified. We therefore conclude that a gradual structural transi- tion, confined mainly to a region comparable to the grain boundary core in extent, can occur at $\sim 0.5T_{m}$.

The behavior at $T/T_{m}=0.65$ shows the disorder has become more widespread. One sees a suc- cessive loss of order starting in region 6 and propagating through almost half of the simulation cell. It is in fact debatable whether the configurations in regions 2-6 can still be regarded as crystalline. We believe the system has gone into a metastable state and large fluctuations occurred in internal structure as well as in atomic mobility. It is noteworthy that region 7 has become disordered, but region 8 remained unaffected. Thus at this temperature the system is able to maintain an interface between bulk crystal and a highly disordered zone over a rather long period of simulation.

We have made similar analysis of the data at $T/T_{m}=0.76$ (not shown in Fig. 5). The order parameters for all regions decreased to zero within $80\times10^{4}$ time steps of simulation. The bi- crystal model, in its present size, is clearly mechanically unstable at this temperature. Snap- shots of the configurations after instability has set in show a structure essentially devoid of crystalline order. It seems reasonable to interpret the observed structural change as local melting. Although we have yet to examine in detail the thermodynamic variables of the resulting system, we can tell from the mean square displacement results (Fig. 6) that at $T/T_{m}=0.76$ there is a marked enhancement of atomic mobility.

### V. Discussion

We have investigated the influence of thermal motions on the structural integrity of a bi- crystal model of aluminum. Using an order parameter which probes the regularity of atomic posi- tions parallel to the boundary plane, we find the grain boundary core to remain well ordered up to about $T/T_{m}\sim0.5$ Above this temperature significant disorder appears; initially the dis- order is localized to the grain boundary core region, but with increasing temperature the ex- tent of the disordered zone grows. Random migration of the boundary core is observed which suggests the system is in a metastable state. At $T/T_{m}\sim0.76$ loss of crystalline order is so extensive that within the time period of simulation local melting appears to have occurred. The results on atomic mobility and the snapshots of instantaneous system configuration are both con- sistent with this interpretation.

We have made similar though less extensive study of the $\Sigma=5$ bicrystal model (M1 struc- ture) using a pseudopotential [11]. The melting point $T_{m}$ determined from the reference single crystal is found to be appreciably lower, $T_{m}\sim630K$. However, in terms of the reduced

temperature $T/T_m$, similar bicrystal behavior is observed as that described above. We are therefore reasonably confident that the qualitative features of our results do not depend on the details of the potential function.

The present results point to the same general conclusions as previous molecular dynamics studies of the temperature variations of enthalpy in two-dimensional bicrystals with Lennard-Jones potential [4,5]. In the case of a three-dimensional $\Sigma$ = 5 bicrystal with Lennard-Jones interaction and periodic border conditions, Ciccotti, Guillope and Pontikis found a continuous structural transition occurring at $T/T_m$ < 0.5 [6]. These workers were the first to use the order parameter $\rho(\underline{K})$ to monitor structural changes in a bicrystal, and they have obtained results (their Fig. 6) showing the same behavior as our Fig. 4. On the other hand, their simulation periods were 8000 time steps or less; on the basis of our Fig. 5, this would not be long enough to reveal any of the disordering that we have observed at $T/T_m$ $\gtrsim$ 0.54. For this reason we feel that their conclusion that the grain boundary remains crystalline up to essentially $T_m$ should be checked by longer runs than the ones reported [6,7]. Another factor which could affect their results is that their initial simulations were carried out at constant volume. With increasing temperature the system pressure and therefore the melting point would rise.

It would be desirable to make further investigations using a system that is larger at least in the z dimension and preferably also in the x dimension. It is quite essential to obtain a stable (or metastable) boundary-bulk interface when local melting occurs. In view of the fixed border condition in our simulation, considerations of system size effects, particularly along the z direction would be important.

The observation of a structural transition by molecular dynamics simulations correlates well with a two-dimensional cluster-variation calculation [2]. Atomistic simulation techniques are also well suited for estimating interfacial free energies [14]. Gibbs free energies of two and three-dimensional bicrystals ($\Sigma$ = 7) with Lennard-Jones interactions have been recently obtained by means of molecular dynamics with the results indicating a grain boundary melting transition at a temperature below $0.8T_m$ [15]. On the other hand, secondary grain boundary dislocations have now been observed in a ${\Sigma}_m$ = 5 tilt aluminum bicrystal at temperatures up to about $0.9T_m$ [16]. The implications of these data in the present context have yet to be investigated.

### Acknowledgments

We (TN, CN and SY) would like to express our appreciation of summer support and hospitality at the IBM Watson Research Center where all the simulations and data analysis were carried out. Also CN would like to acknowledge the award of an IBM Predoctoral Fellowship.

### References

[1] J. W. Gibbs, Scientific Papers, Vol. I (Dover, New York, 1961); E. W. Hart, in The Nature and Behavior of Grain Boundaries, H. Hu, ed. (Plenum Press, New York, 1972), p. 155.
[2] R. Kikuchi and J. W. Cahn, Phys. Rev. B21, 1893 (1980).
[3] M. E. Glicksman and C. L. Vold, Surf. Sci. 31, 50 (1972).
[4] F. Carrion, G. Kalonji and S. Yip, Scripta Metall. 17, 915 (1983).
[5] G. Kalonji, P. Deymier, R. Najafabadi and S. Yip, Surf. Sci. 144, 77 (1984).
[6] G. Ciccotti, M. Guillope and V. Pontikis, Phys. Rev. B27, 5576 (1983).
[7] M. Guillope, G. Ciccotti and V. Pontikis, Surf. Sci. 144, 67 (1984).
[8] K. T. Aust, in Progress in Materials Science, Chalmers Anniversary Volume, J. W. Christian, P. Haasen and T. B. Massalski, eds. (Pergamon Press, Oxford, 1981), p. 27.
[9] Preliminary results were reported by T. Kwok, P. S. Ho, S. Yip, Surf. Sci. 144, 44 (1984).
[10] R. J. M. Cotterill and M. Doyama, in Lattice Defects and their Interfaces, R. Hasiguti, ed. (Gordon and Breach, New York, 1967), p. 1.
[11] L. Dagens, M. Rasolt and R. Taylor, Phys. Rev. B11, 2726 (1976).
[12] M. Hashimoto, Y. Ishida, R. Yamamoto and M. Doyama, J. Phys. F10, 1109 (1980).
[13] C. Nitta, P. S. Ho, T. Kwok, T. Nguyen, S. Yip, to be published.
[14] A. J. C. Ladd, W. G. Hoover, V. Rosato, G. Kalonji, S. Yip and R. J. Harrison, Phys. Letters 100A, 195, (1984).
[15] P. Deymier and G. Kalonji, Acta Metall., to be published, J. Chem. Phys., to be published.
[16] S.-W. Chan, J. S. Liu, R. W. Balluffi, Scripta Metall., to be submitted.

![](./images/812401908261060609_1.jpg)

Fig. 1. Simulation cell showing orientation of the boundary plane and an x-z plane projection showing two adjacent layers of atoms (circles and points) in 2 CSL units. The cell is composed of 10 layers with each layer containing 3 CSL units along the x-direction and 6 units along the z-direction.

![](./images/812401908261060609_2.jpg)

![](./images/812401908261060609_3.jpg)

Fig. 2. Relaxed structure Ml in a simulation cell divided into 12 regions numbered as indica- ted. Two adjacent layers of atoms in regions 5-8 are shown.

Fig. 3. Variation of internal energy with temperature for the single crystal model and the bi- crystal model. Bicrystal results were obtained from runs of $16 \times 10^{4}$ time steps or longer; data at 600K and 700K refer to energies before local melting set in.

![](./images/812401908261060609_4.jpg)

Fig. 4. Variation of order parameter for different regions j with temperature. All runs are at essentially constant pressure and extend over an interval of 3000 time steps.

![](./images/812401908261060609_5.jpg)

Fig. 5. Time evolution traces of order parameter for the bicrystal model at a given temperature for different regions j (as denoted by the indicated numbers). Vertical bars indicate the magnitude of fluctuations in each trace. All runs are at essentially constant pressure.

![](./images/812401908261060609_6.jpg)

Fig. 6. Time variation of atomic mean square displacement $<\Delta^{2}r>$ (in units of $a^{2}$) at various temperatures $T/T_{m}$. The atoms considered are those in regions 8, 5, and 6 for $T/T_{m}=0.54$, 0.65, and 0.76 respectively. The values for $T/T_{m}-0.43$ are too small to be shown on the same scale. Vertical bar indicates the magnitude of fluctuations of the trace.
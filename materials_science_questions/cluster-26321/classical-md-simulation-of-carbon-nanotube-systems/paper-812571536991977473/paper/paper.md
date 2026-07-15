![](./images/812571536991977473_1.jpg)

Subscriber access provided by UNIV PRINCE EDWARD ISLAND

B: Liquids, Chemical and Dynamical Processes in Solution, Spectroscopy in Solution

# Formation of Stable Water Bridge between Two Disjoint Nanotubes with Single-File Chains of Water

Fatemeh Ebrahimi, Gholamreza R. Maktabdaran, and Muhammad Sahimi

*J. Phys. Chem. B*, Just Accepted Manuscript • DOI: 10.1021/acs.jpcb.0c05331 • Publication Date (Web): 07 Sep 2020

Downloaded from pubs.acs.org on September 8, 2020

## Just Accepted

"Just Accepted" manuscripts have been peer-reviewed and accepted for publication. They are posted online prior to technical editing, formatting for publication and author proofing. The American Chemical Society provides "Just Accepted" as a service to the research community to expedite the dissemination of scientific material as soon as possible after acceptance. "Just Accepted" manuscripts appear in full in PDF format accompanied by an HTML abstract. "Just Accepted" manuscripts have been fully peer reviewed, but should not be considered the official version of record. They are citable by the Digital Object Identifier (DOI®). "Just Accepted" is an optional service offered to authors. Therefore, the "Just Accepted" Web site may not include all articles that will be published in the journal. After a manuscript is technically edited and formatted, it will be removed from the "Just Accepted" Web site and published as an ASAP article. Note that technical editing may introduce minor changes to the manuscript text and/or graphics which could affect content, and all legal disclaimers and ethical guidelines that apply to the journal pertain. ACS cannot be held responsible for errors or consequences arising from the use of information contained in these "Just Accepted" manuscripts.

is published by the American Chemical Society. 1155 Sixteenth Street N.W., Washington, DC 20036
Published by American Chemical Society. Copyright © American Chemical Society.
However, no copyright claim is made to original U.S. Government works, or works produced by employees of any Commonwealth realm Crown government in the course of their duties.

# Formation of Stable Bridge Between Two Disjoint Nanotubes with Single-File Chains of Water

Fatemeh Ebrahimi, $^{1,\dagger}$ G.R. Maktabdaran, $^{1}$ and Muhammad Sahimi$^{2}$

$^{1}$Department of Physics, University of Birjand, Birjand 97175-615, Iran

$^{2}$Mork Family Department of Chemical Engineering and Materials Science, University of Southern California, Los Angeles, California 90089-1211, USA

**ABSTRACT:** It was recently demonstrated that stable water bridges can form between two relatively large disjoint nanochannels, such as carbon nanotubes (CNTs), under an applied pressure drop. Such bridges are relevant to fabrication of nanostructured materials, drug delivery, water desalination devices, hydrogen fuel cells, dip-pen nanolithography, and several other applications. If the nanotubes are small enough, however, then one has only single-file hydrogen-bonded chains of water molecules. The distribution of water in such nanotubes manifests unusual physical properties that are attributed to the low number of hydrogen bonds (HBs) formed in the channel since, on average, each water molecule in a single-file chain forms only 1.7 HBs, almost half of the value for bulk water. Using extensive molecular dynamics simulations, we demonstrate that stable bridges can form even between two small disjoint CNTs that contain single-file chains of water. The structure, stability, and properties of such bridges and their dependence on the applied pressure drop and the length of the gap between the two CNTs are studied in detail, as is the distribution of the HBs. We demonstrate, in particular, that the efficiency of flow through the bridge is maximum at a specific pressure difference.

# INTRODUCTION

Flow of water through nanostructured materials, and in particular in carbon nanotubes (CNTs) and similar materials, has been investigated extensively over the past two decades. The interest is due to the importance of water channels to new purification systems as the world has been increasingly facing the prospect of shortage of drinking water, as well as to osmotic power harvesting in salinity gradients, hydroelectric voltage conversion, signal transmission, drug delivery, and numerous other applications. Almost all of such studies focused on flow in single pristine nanotubes, and indicated dramatic differences with what the classical hydrodynamics predicts for much larger channels due to a variety of reasons, ranging from slip on the nanotubes' walls to interfacial effects. $^{1-4}$

To increase the effectiveness of water channels for purification, their structure must be more complex than a single tube. At the same time, for the results of studies of water in such nanostructured systems to be relevant to natural biological channel systems, as well as to practical applications, one must consider more complex geometries, such as networks of interconnected nanotubes, nanostructured channels that are connected together by junctions with sizes that are different from those of the channels, etc. In addition, technological advances have made it possible to design and construct more complex structures than a single pristine nanotube. Such important considerations have motivated recent research $^{5-13}$ for exploring fluid flow and transport phenomena in complex configurations made of nanotubes.

An important and technologically relevant variants of water channels is *water bridge* between two disjoint channels that are not physically connected. It is well understood that at ambient pressure and below water saturation, two surfaces that are in the vicinity of each other can give rise to spontaneous capillary condensation, leading to the formation of a water bridge. This is not merely a macroscopic phenomenon, because it can occur even at nanoscale. For example, a bridge can form between a surface and the tip of atomic force microscope. $^{13,14}$ Thermodynamic considerations $^{15,16}$ and the Kelvin equation $^{15}$ provide the theoretical basis for understanding such bridges. If one is able to manipulate such bridges - a difficult problem - then the outcome can be rewarding, as it is relevant to fabrication of nanostructured materials, drug delivery, dip-pen nanolithography in which the water meniscus serves as a channel for molecules to flow from the tip to the substrate, and other important problems. One way of manipulating such

bridges is through an applied electric field.¹⁷ Alternatively, the bridge may be manipulated by applying a pressure gradient - the hydrodynamic analog of an electric field - and varying the size of the two nanostructures that are connected by the water bridge. The focus of the present paper is on the latter case.

Using molecular dynamics (MD) simulation, a recent paper¹² demonstrated that a stable water bridge can form between two disjoint CNTs, and studied the efficiency of water flow through the bridge. The CNTs used in that study were wide enough to host a bulk-like distribution of water molecules. When the size of a nanotube is small enough that its cross section can accomodate only one water molecule, then, one has the well-known phenomenon of single-file water transport,¹⁸,¹⁹ whose existence has been demonstated by careful experiments.¹⁹ Flow in nanostructured systems with single-file configurations of liquids manifest unusual physical properties that are exploited in biological apolar pores, and hold promise for a wide range of technological applications, ranging from water desalination devices to hydrogen fuel cells. The unusual properties are attributed to the difference in the formation of hydrogen bonds (HBs) since, on average, each water molecule in a single-file chain forms 1.7 HBs, almost half the value for bulk water.

In this paper we report on the results of a systematic and extensive study of formation of water bridges, using MD simulations, in CNTs that are small enough to allow only single-file water transport. As we demonstrate below, both single-file and "massive" (thicker than single file) bridges can form for a range of pressure drop and the length of the gap between the two CNTs. We also demonstrate that the efficiency of flow through the bridge is maximum at a specific pressure difference. Our study sheds light on the dual role played by the HBs and the affinity of water molecules for each other. While previous studies²⁰,²¹ indicated that formation and association of HBs is a main source of hydrodynamic resistance, we show that the same factors contribute to water flow in the bridge, not only by making the formation of the bridge possible, but also by facilitating water ejection from the high-pressure reservoir toward the CNT connected to the low-pressure one.

# RESULTS

The structure of the system is shown in Figure 1 (see also the Methods section below). The mean "flow rate" $Q_H$, defined as the net number of water molecules $\Delta N_H$ over a time period

$\Delta t$ leaving the CNT connected to the high-pressure reservoir, $Q_H = \Delta N_H/\Delta t$, was computed, as was the absolute value of $Q_L = \Delta N_L/\Delta t$, the mean flow rate received by the CNT connected to the low-pressure reservoir. Four pressure drops, $\Delta P = 2600$, 3200, 3700, and 4200 atm, and three lengths $l_g$ of the gap between the two CNTs, $l_g = 8$, 13, and 18 Å were considered, as was the limit $l_g = 0$, representing a single long CNT.

Structure of the Bridge. The bridge between two disjoint nanotubes with single-le chains of water is not necessarily a single-file chain itself. In general, at lower pressures and smaller lengths of the gap between the two CNTs, the size of the water bridge is small, whereas at high pressures and large gaps it may contains many water molecules. Our MD simulations indicate that the temporal behavior and spatial conguration of the bridge can be very complex and depend on the pressure difference and the gaps width

Figure 1 presents four snapshots of the system before the formation of a bridge, after formation a single-file bridge, and what we referred to as a massive bridge with a complex structure, as well as the case in which water clusters are formed and are adsorbed on the graphene sheets that represent the boundaries of the two reservoirs connected to the two CNTs. The CNTs are separated by a gap of length $l_g = 8$ Å, and a pressure difference of $\Delta P = 4200$ atm was applied between the two reservoirs.

The first issue that we address is the distribution $f_W(N_{HB})$ of the number of water molecules in the bridge per unit length (taken to be 1 nm) that have on average $N_{HB}$ HBs. Figure 2 presents the result in which all the data represent averages over 10 ns, and are for two disjoint CNTS separated by a distance $l_g = 8$ Å and 13 Å, both for a pressure drop of $\Delta P = 3700$ atm between the two reservoirs. For comparison, we also include the same distribution for a single CNT, which was evaluated by applying the same pressure difference between two reservoirs at its two ends. Figure 2 indicates that for a single CNT $F_W$ is nonzero only when $N_{HB} < 3$, which is expected, but is also different from the distribution for the water bridge. There are some water molecules in the bridge with $N_{HB} = 3$, and fewer molecules with $N_{HB} = 4$. The maximum of the distribution is still at $N_{HB} = 2$, although its height is smaller for larger gaps.

If we increase the pressure difference to larger values, both the peak's height and the width of the distributioon grow, hence indicating formation of a massive water bridge with a more complex shape. This is demonstrated by the results in Fig. 2 for $l_g = 8$ Å and $\Delta P = 4200$ atm. We show below that these features affect remarkably the performance of system in terms

of mass flow rate.

As mentioned earlier, the results shownn in Fig. 2 represent time-averaged quantities. Both the mass and the shape of the water bridge fluctuate over time. Even in the system with a single CNT the number of HBs is not constant over time. For example, for a pressure difference of $\Delta P = 3700$ atm, $5 \times 10^3$ HBs break every 1 ns, which means the mean lifetime for a typical HB is $2 \times 10^{-4}$ ns. In addition, the average number of broken HBs in the water bridge between the two CNTs with a gap of length $l_g = 8$ $\mathring{A}$ is a little larger than that in the single CNT, $7 \times 10^3$/ns, which is a result of the instability occurring within the gap region. Increasing the pressure difference to $\Delta P = 4200$ atm amplifies the instability by increasing the number of broken HBs to $1.4 \times 10^4$/ns. Interestingly, in all the cases that we studied, the strength of hydrogen bond measured by the average distance between the donor and acceptor is the same, $^{22}$ $0.20 \pm 2$ in valence units.

When a massive bridge is formed, even though one has only single-file transport through the CNTs, its structure is complex and interesting. Thus, we analyzed the structure by examining its dependence on the number of HBs formed and another quantitative measure for a bridge of $N_B$ water molecules, namely, the eigenvalues of its gyration tensor defined by,

$$
\mathbf{G} = \frac{1}{N_B} \sum_{i=1}^{N_B} (\mathbf{X}_i^2 \mathbf{I} - \mathbf{X}_i \mathbf{X}_i) , \tag{1}
$$

with $\mathbf{X}_i$ being the distance of the $i$th water molecule from the bridge's center of mass, and $\mathbf{I}$ the unit tensor. We used an efficient method$^{23,24}$ to determine the eigenvalues of $\mathbf{G}$, namely, $\lambda_x^2$, $\lambda_y^2$, and $\lambda_z^2$, the acylindricity $A$ of the bridge given by, $A = |\langle\lambda_x^2\rangle - \langle\lambda_y^2\rangle|$, and the mean transverse radius of gyration, $R_g^2 = \frac{1}{2}(\langle\lambda_x^2\rangle + \langle\lambda_y^2\rangle)$.

Figure 3(a) presents the dynamic evolution of $N_B$, the mean number of water molecules in the bridge, which we refer to it as the bridge's mass. $N_B$ increases with the time roughly linearly. Its occasional dip is due to some of the molecules returning to the CNT from which they had exited earlier.

Figure 3(b) exhibits the correlation between the bridge's radius of gyration $R_g$ and $N_B$. Given that $N_B$ varies essentially linearly with time, Figure 3(b) essentially shows the time-dependence of $R_g$. The inset in Figure 3(b) shows the acylindricity. The results are for a time interval $\Delta t = 1.8$ ns in the same system as in Figure 1, for which the simulation indicated simultaneous formation of a massive water bridge and a growing number of water molecules

entering the CNT connected to the low-pressure reservoir through the bridge. Both quantities exhibit large fluctuations, even for a fixed $N_B$, as indicated by the error bars. Figures 3(b) indicates, therefore, that (i) the overall shape of the bridge is neither necessarily cylindrical, nor constant over time, and (ii) the cross section of the bridge can be remarkably thicker than the diameter of the CNTs and that of the single-file of the water molecules, hence indicating expansion and contraction of the streamlines in the high- and low-pressurized sides, respectively.

Another characteristic of the bridge is the dependence of its mean number of HBs per water molecule, $N_{HB}$, on the bridge mass $N_B$. The correlation between the two is shown in Figure 3(c), indicating large fluctuations in $N_{HB}$, even for a fixed bridge mass $N_B$. Initially, $N_{HB} \approx 1.5 - 1.7$, which corresponds to the number of HBs in a single-file configuration, but over time as $N_B$ increases, $N_{HB}$ approaches 2.5. Most force fields for water predict $N_{HB} \approx 4$ for bulk water at room temperature, although a recent new and highly accurate force field predicted$^{25}$ it to be $\approx 2.15$.

Temporal fluctuations may induce shrinking of the bridge, with some of the water molecules entering the CNT conneted to the low-pressure reservoir. This is shown in Figure 4, where we present the dynamic evolution of the total number of water molecules outside the two nanotubes for the gap length $l_g = 8$ Å and $\Delta P = 3700$ atm. There are some burst-like events, shown by the arrows, which indicate separation of water molecules from the bridge. While the definitive mechanisms for the burst-like discharge is not known yet, we believe that if the bridge is not too massive, thermal fluctuation can, at least in some instances, provide the proper system configuration to have burst-like discharge. We should emphasize that the discharge events take time, and that all the bridges' mass does not discharge at the same time. In addition, larger clusters of water always detach from the main stream and are adsorbed onto one of the graphene sheets, reducing the efficiency of water flow between the two CNTs. Moreover, detachment of a water cluster can break the bridge and interrupt water flow between the two CNTs for a while, until a new bridge forms again. The time for forming a new bridge is a stochastic variable, but our simulations suggest that its mean value increases with $l_g$, but deceases with larger $\Delta P$, both of which are expected.

Dependence of Water Flow Rate on the Gap's Length and the Pressure Drop. Given the force field that we employed in the simulations, water can invade the CNTs from the reservoirs without needing any external pressure gradient.$^{26}$ A thin film of water, at equilibrium with its

vapor, penetrates the CNT instantaneously with a rate of $180 \pm 20$ molecules per nanosecond. This should be compared with a rate of up to $450 \pm 50$ molecules per ns in the early times, when water begins filling the CNT under both capillary action and an applied pressure difference of $\Delta P = 3200$ atm. When the system reaches steady state, the rate is about $90 \pm 5$ molecules per ns. Two important factors cause the steady-state flow rate to be much smaller than the transient one. One is the removal of the capillary force, which happens after formation of single-file chain of water molecules, while the second one is the hydraulic resistance of the exit that adds to the entrance friction. In addition, since the slip on the walls of the CNTs provides "greasy" channels for water flow, $^{1-3,27-29}$ the entrance/exit effects are the main source of energy dissipation. $^{3,4,28,30}$

In Figure 5 we present the dependence on the gap length $l_g$ of the absolute value of the mean flow rate, $Q_L = \Delta N/\Delta t$, entering the nanotube connected to the low-pressured reservoir, as a function of pressure difference $\Delta P$. The data were computed by evaluating the change in the number of water molecules in each reservoir during a time interval of 10 ns. Within the range of the pressure differences that we considered, the flow rate in a single pristine CNT grows linearly with $\Delta P$, with its minimum value being $78 \pm 4$ and a maximum value of $106 \pm 5$ molecules per ns. As one may expect, for a configuration of disjoint CNTs $Q_L$ decreases. $^{12}$ Contrary to the $(12,12)$ CNTs, $^{12}$ however, $Q_L$ decreases with the gap width, $l_g$, with the main reason being the frequent rupture of the bridge that is intensified with increasing $l_g$. In addition, $Q_L$ reaches a maximum and then decreases. For both $l_g = 13$ and $8$ Å, the maximum is reached in the range $3200 < \Delta P < 4200$ atm, with the peak value being smaller for the larger gap.

Although from a computational view point, identifying the precise value of the pressure difference $\Delta P_m$ that maximizes water flow rate is a difficult task, we can explain its existence. By increasing the pressure, the velocity of water molecules ejecting from the CNT connected to the high-pressure reservoir increases. The absence of the CNT wall that provides smooth flow paths for water molecules increases the chance of flow instability that arises as a result of the collision of water molecule between the two CNTs in the free space between the two. At the same time, the affinity of water molecules for each other prevents their escape after collision, and usually leads to the formation and growth of a water cluster attached to the main stream in the gap between two CNTs. The increase in the number of the HBs in the emerging clusters, shown in Figure 3, supports this. As mentioned earlier, formation of such water clusters decreases the

efficiency of water flow, not only because it slows down the transport rate, but also because the large clusters generated at higher pressure difference eventually detach themselves from the bridge, and are adsorbed onto one of graphitic walls of the two reservoirs; see Figure 1(d).

Note that water flow between the two CNTs happens only when $\Delta N/\Delta t > 0$ in the CNT connected to the low-pressure reservoir. As such, we conclude that no bridge would form if $l_g \geq 18$ Å, even for very high pressure drops, which is smaller than the corresponding value for the (12,12) CNTs, $\approx 40$ Å. The limitation is caused by the same features that break the bridge, namely, single-file configuration of water molecules emerging from the CNTs with an average number of the HBs of about 1.7 is not strong enough to form stable bridge for larger $l_g$. The spreading of the water column outside the CNT is not energetically favorable, because it involves breaking of approximately 2 HBs at the entrance of the CNT connected to the low-pressure reservoir. We shall return to this point shortly.

Bridging and Dissipation. As discussed earlier, the efficiency of flow through a bridge between two small disjoint CNTs is decreased by instabilities in the fluid flow caused by the formation of water clusters and their detachment from the bridge that lead to its collapse. This is shown in Figure 6, where we present the ratio of $Q_H = \Delta N_H/\Delta t$, the rate of the number of water molecules $\Delta N_H$ leaving the CNT connected to the high-pressure reservoir, and $Q_S$, the flow rate for a single long CNT that corresponds to $l_g = \infty$. As $l_g$ increases for a fixed $\Delta P$, $Q_H$ decreases with $l_g$, and for $l_g \geq 18$ Å reaches its minimum value, $Q_J$. Under such circumstances, the existence of the low-pressure reservoir and the CNT attached to it have very little impact on the dynamics of formation of water bridge. Thus, the high-pressure CNT acts as a water jet from a CNT nozzle.³¹

We compare in the inset of Figure 6 the evolution of $\Delta N_H$ as a function of the gap's length $l_g$ for $\Delta P = 3700$ atm. It is clear that the main difference between flow via a single pristine CNT (red graph with circles) and a water jet (green curve with triangles) is that, while the former is a quasi-steady-state process, the latter is of the stick-slip type. During the stick events, water molecules are strongly attached to each other in the CNT and the reservoir and cannot leave the former, hence making ejection dynamics very slow when compared with a pristine CNT. This phenomenon is linked with the rearrangement and breaking of the HBs of the water molecules that leave the high-pressure reservoir and enter the CNT on the left (see Figure 1). It has been suggested that a major portion of entrance/exit energy dissipation is due to the energy penalty

for breaking/creating the HBs at the entrance/exit part of nanochannels.

To check this proposal, we carried out MD simulations of flow of water between the two disjoined CNTs with hypothetical water molecules in which their oxygen and hydrogen ions electric charges were reduced to 1/4 of their actual values. This turned off formation of the HBs. The simulation indicated that water flow rate increased by 220 percent over what is obtained with the standard water model that can form HBs. No water bridge is formed, however, when a gap of length $8\ \mathring{A}$ or larger is maintained between the two CNTs. At the same time, the hypothetical water molecules evaporate from both CNTs at the same rate of 500 molecules per ns, more than twice as much as the rate for a single CNT. We conclude, therefore, that formation of HBs plays a fundamental role in the formation of water bridges.

As mentioned earlier, we used the TIP3P model to represent the water molecules. The question that one may raise is the extent to which the results depend on the molecular model of water that one uses. Several authors have studied the dependence of flow of water in nanotubes on the particular molecular model that is used. Quantitatively, the TIP3P and TIP4P models produce more accurate results than the simpler SPC/E model, but they are also more expensive computationally. The qualitative aspects of the results are, however, similar. For example, Liu and Patey$^{32}$ compared the flow rates of water in CNTs, computed by the TIP3P, TIP4P/2005 and SPC/E models, and reported them to be qualitatively similar, although the details of the distributions of water in the nanotubes depended on the water model. Losey *et al.*$^{33}$ studied flow of water in CNTs using several water molecular models. While the magnitude of the flow rate depended on the water model, they were similar qualitatively. Thus, we expect all the qualitative aspects of our results to remain the same, if we use another molecular model of water. We are currently studying this issue; the results will be reported in a future paper.

Summarizing, using extensive MD simulations, we demonstrated that stable bridges can form between two small disjoint CNTs that contain single-file chains of water. Such bridges are relevant to fabrication of nanostructured materials, drug delivery, dip-pen nanolithography, water desalination devices, and hydrogen fuel cells. The properties of such water bridges and their dependence on the applied pressure drop and the length of the gap between the two disjoint CNTs were studied in detail. In particular, the crucial influence of formation of hydrogen bonds was studied. We also demonstrated that the efficiency of flow through the bridge is maximum at a specific pressure difference.

## METHODS

The simulation box contained two water reservoirs separated by a distance 98 Å along the nanotubes’ axial direction $z$. Each reservoir consisted of two parallel graphene sheets of size $44.3 \times 42.6$ Å², normal to the $z$ axis and separated initially by a distance of 40 Å. At the beginning of the simulations, each reservoir contained 2002 water molecules. A larger reservoir with four times as many water molecules was also simulated, but the rate of water flow did not change significantly. Two identical and coaxial (6,6) CNTs (with diameter of 0.806 nm), initially capped and separated by a gap of length $l_g$ were connected to the reservoirs in the middle of the graphene sheets. The outermost graphene sheet in each reservoir acted as a piston exerting constant pressure; the pressure at low-pressure reservoir was set at 1 atm, while the pressure in the high-pressure side was set such that the desired pressure difference $\Delta P$ was obtained.

The LAMMPS package³⁴ with a time step of 2 fs was employed in the simulations. Water molecules were represented by the TIP3P model. The interactions of the water molecules with the carbon atoms in the graphene sheets and on the CNTs’ walls were represented by the Lennard-Jones (LJ) potential with the standard energy and size parameters $\epsilon$ and $\sigma$, on the basis of the interactions between the oxygen and carbon atoms. The cutoff distance for the LJ interactions was set at 1.4 nm. We used $\epsilon_{O-C} = 478.4$ J/mol and $\sigma_{O-C} = 3.28$ Å from the AMBER96 force field.¹ This corresponds to a contact angle of about³ 57°. The particle-particle-particle-mesh method was used to compute the long-range Columbic interactions.

Temperature of the system was set at 300 K, using the Nosé-Hoover thermostat during the entire simulation. To prevent the possibility of thermal contribution to the velocity of the water molecules, however, those inside the CNTs, as well as in each reservoir that were at a distance less than 5 Å from the CNTs were excluded from the thermostat.³⁵,³⁶ Periodic boundary conditions were imposed in all directions. The total simulation time was up to 15 ns, depending on the setup. The water in the reservoirs reached equilibrium after typically 0.2 ns, after which the caps on the CNTs were removed to allow water to penetrate them. In the case of a single pristine CNT, water flow reached steady state after a small transient time of less than 0.2 ns. Therefore, in the numerical analysis we discarded the data produced in the first 0.5 ns of the simulation.

# AUTHORS INFORMATION

## Corresponding Author
*E-mail: f_ebrahimi@birjand.ac.ir
†E-mail: moe@usc.edu

## ORCID
: Fatemeh Ebrahimi: 0000-0001-5235-4124
Muhammad Sahimi: 0000-0002-8009-542X

## Notes
The authors declare no competing financial interest.

# ACKNOWLEDGMENTS

All the simulations were carried out using the Saffron computer cluster at the university of Birjand, Iran.

# REFERENCES

(1) Hummer, G.; Rasaiah, J.C.; Noworyta, J.P. Water Conduction Through the Hydrophobic Channel of a Carbon Nanotube. *Nature* **2001**, *414*, 188-190.

(2) Thomas, J.A.; McGaughey, A.J.H. Water Flow in Carbon Nanotubes: Transition to Sub-continuum Transport. *Phys. Rev. Lett.* **2009**, *102*, 184502.

(3) Joly, L. Capillary Filling with Giant Liquid/Solid Slip: Dynamics of Water Uptake by Carbon Nanotubes. *J. Chem. Phys.* **2011**, *135*, 214705.

(4) Walther, J.H.; Ritos, K.; Cruz-Chu, E.R.; Megaridis, C.M.; Koumoutsakos, P. Barriers to Superfast Water Transport in Carbon Nanotube Membranes. *Nano Lett.* **2013**, *13*, 1910-1914.

(5) Choe, H.; Hong, M.H.; Seo, Y.; Lee, K.; Kim, G.; Cho, Y.; Ihm, J.; Jhe, W. Formation, Manipulation, and Elasticity Measurement of a Nanometric Column of Water Molecules. *Phys. Rev. Lett.* **2005**, *95*, 187801.

(6) Xu, B.; Li, Y.; Park, T.; Chen, X. Effect of Wall Roughness on Fluid Transport Resistance in Nanopores. *J. Chem. Phys.* **2011**, *135*, 144703.

(7) Gravelle, S.; Joly, L.; Ybert, C.; Bocquet, L. Large Permeabilities of Hourglass Nanopores: From Hydrodynamics to Single File Transport. *J. Chem. Phys.* **2014**, *141*, 18C526.

(8) Ramazani, F.; Ebrahimi, F. Uncertainties in the Capillary Filling of Heterogeneous Water Nanochannels. *J. Phys. Chem. C* **2016**, *120*, 12871-12878.

(9) Ramazani, F.; Ebrahimi, F. Water Imbibition into Nonpolar Nanotubes with Extended Topological Defects. *Chem. Phys.* **2016**, *476*, 23-28.

(10) Razmkhaha, M.; Ahmadpour, A.; Taghi, M.; Mosaviana, H.; Moosavi, F. What is the Effect of Carbon Nanotube Shape on Desalination Process? A Simulation Approach. *Desalination* **2017**, *407*, 103-115.

(11) Ebrahimi, F.; Ramazani, F.; Sahimi, M. Nanojunction Effects on Water Flow in Carbon Nanotubes. *Sci. Rep.* **2018**, *8*, 7752.

(12) Sahimi, M.; Ebrahimi, F. Efficient Transport Between Disjoint Nanochannels by a Water Bridge. *Phys. Rev. Lett.* **2019** *122*, 214506.

(13) Meng, X.W.; Shen, L. Transport Between One Dimensional Disjoint Nanochannels. *Chem. Phys. Lett.* **2020**, *739*, 137029.

(14) Stifter, T.; Marti, O.; Bhushan, B. Theoretical Investigation of the Distance Dependence of Capillary and van der Waals Forces in Scanning Force Microscopy. *Phys. Rev. B* **2000**, *62*, 13667-13673.

(15) Sirghi, L.; Szoszkiewicz, R.; Riedo, E. Volume of a Nanoscale Water Bridge. *Langmuir* **2006**, *22*, 1093-1098.

(16) Jang, J.; Schatz, G.C.; Ratner, M.A. How Narrow Can a Meniscus Be? *Phys. Rev. Lett.* **2004**, *92*, 085504.

(17) Cramer, T.; Zerbetto, F.; García, R. Molecular Mechanism of Water Bridge Buildup: Field-Induced Formation of Nanoscale Menisci. *Langmuir* **2008**, *24*, 6116-6120.

(18) Köfingera, J.; Hummera, G.; Dellago, C. Single-File Water in Nanopores. *Phys. Chem. Chem. Phys.* **2011**, *13*, 15403-15417.

(19) Cambrí, S.; Schoeters, R.; Luyckx, S.; Goovaerts, E.; Wenseleers, W. Experimental Observation of Single-File Water Filling of Thin Single-Wall Carbon Nanotubes Down to Chiral Index (5,3). *Phys. Rev. Lett.* **2010**, *104*, 207401.

(20) Kalra, A.; Garde, S.; Hummer, G. Osmotic Water Transport Through Carbon Nanotube Membranes. *Proc. Natl. Acad. Sci. U.S.A.* **2003**, *100*, 10175-10180.

(21) Zhang, X.; Zhou, W.; Xu, F.; Wei, M.; Wang, Y. Resistance of Water Transport in Carbon Nanotube Membranes. *Nanoscale* **2018**, *10*, 13242-13249.

(22) Machesky, M.L., et.al. Surface Protonation at the Rutile (110) Interface: Explicit Incorporation of Solvation Structure within the Rened MUSIC Model Framework. *Langmuir* **2008**, *24*, 12331-12339.

(23) Kopp, J. Efficient Numerical Diagonalization of Hermitian $3 \times 3$ Matrices. *Int. J. Mod. Phys. C* **2008**, *19*, 523-548.

(24) Ebrahimi, F. Invasion Percolation: A Computational Algorithm for Complex Phenomena. *Comput. Sci. Eng.* **2010**, *12*(2), 84-93.

(25) Naserifar, S.; Goddard, W.A. Liquid Water is a Dynamic Polydisperse Branched Polymer. *Proc. Natl. Acad. Sci. U.S.A.* **2019**, *116*, 1998-2003.

(26) Ebrahimi, F.; Pishevar, A. Dependence of the Dynamics of Spontaneous Imbibition into Carbon Nanotubes on the Strength of Molecular Interactions. *J. Phys. Chem. C* **2015**, *119*, 28389-28395.

(27) Joseph, S.; Aluru, N.R.: Why are Carbon Nanotubes Fast Transporters of Water? *Nano Lett.* **2008**, *8*, 452-458.

(28) Falk, K.; Sedlmeier, F.; Joly, L.; Netz, R.R.; Bocquet, L. Molecular Origin of Fast Water Transport in Carbon Nanotube Membranes: Superlubricity versus Curvature Dependent Friction. *Nano Lett.* **2010**, *10*, 4067-4073.

(29) Khademi, M.; Sahimi, M. Molecular Dynamics Simulation of Pressure-Driven Water Flow in Silicon-Carbide Nanotubes. *J. Chem. Phys.* **2011**, *135*, 204509.

(30) Sisan, T.B.; Lichter, S. The End of Nanochannels. *Microfluid. Nanofluid.* **2011**, *11*, 787-791.

(31) Hanasaki, I.; Yonebayashi, T.; Kawano, S. Molecular Dynamics of a Water Jet from a Carbon Nanotube. *Phys. Rev. E* **2009**, *79*, 046307.

(32) Liu, L.; Patey, G.N. (2014). Simulations of water transport through carbon nanotubes: how different water models influence the conduction rate. *J. Chem. Phys.* **2014**, *141*, 18C518.

(33) Losey, J.; Kannam, S.K.; Todd, B.D.; Sadus, R.J. Flow of water through carbon nanotubes predicted by different atomistic water models. *J. Chem. Phys.* **2019**, *150*, 194501.

(34) https://lammps.sandia.gov/doc/Packages_user.html; accessed 10 January 2020.

(35) Thomas, M.; Corry, B. Thermostat Choice Significantly Influences Water Flow Rates in Molecular Dynamics Studies of Carbon Nanotubes. *Microfluid. Nanofluid.* **2015**, *18*, 41-47.

(36) Gravelle, S.; Yoshida, H.; Joly, L.; Ybert, C.; Bocquet, L. Carbon Membranes for Efficient Water-Ethanol Separation. *J. Chem. Phys.* **2016**, *145*, 124708.

![](./images/812571536991977473_2.jpg)

Figure 1: Four snapshots of distribution of water molecules between two disjoint CNTs separated by a gap of width $l_g = 8$ Å under an applied pressure difference of 4200 atm. (a) Before the formation of a bridge. (b) A small water bridge that is usually formed under lower pressure drops and in small gaps. (c) A medium-size bridge. (d) A massive water cluster detaches from the bridge and moves toward the hydrophobic surface of the graphitic sheet. Oother water clusters have already adsorbed on the left sheet.

![](./images/812571536991977473_3.jpg)

Figure 2: Distribution of the number of water molecules in the bridge per unit length versus the number of their hydrogen bonds $N_{HB}$ for a pressure drop of $\Delta P = 3700$ atm, when the distance between the two CNTs was $l_g = 8$ Å (diamonds) and 13 Å (squares). The graph shown by the hats shows the case with $l_g = 8$ Å and $\Delta P = 4200$ atm. For comparison, the distribution of the water molecules inside a single CNT (circles) is also shown.

![](./images/812571536991977473_4.jpg)

Figure 3: Dynamics of geometrical structure of a massive bridge. (a) Time evolution of $N_B$, the bridge mass from the formation until detachment. (b) The correlations between $R_g^2$, the mean squared transverse gyration radius, and the bridge mass. Inset: The correlation between acylindricity $A$ and the bridge mass. (c) The correlation between the mean number of hydrogen bonds $N_{HB}$ for water molecules in the bridge and its mass.

![](./images/812571536991977473_5.jpg)

Figure 4: Dynamic evolution of $N_O$, the total number of water molecules between the graphene sheets, from which the mean number of water molecules insides a straight CNT has been subtracted, for the gap's length $l_g = 8$ $\mathring{A}$ and pressure drop $\Delta P = 3700$ atm. Some of burst-like discharge events are marked by the arrows.

![](./images/812571536991977473_6.jpg)

Figure 5: The mean flow rate $Q_L$ on the low-pressured side as a function of the pressure difference $\Delta P$, for the gap's width $l_g = 0.0$ (circles), $8$ Å (squares), $13$ Å (diamonds), and $18$ Å (triangles).

![](./images/812571536991977473_7.jpg)

Figure 6: Comparison between $Q_H$, the flow of water molecules leaving the CNT connected to the high-pressured reservoir, with $Q_J$, the time-average of flow rate of water molecules emerging from a nozzle ($l_g \to \infty$ ), as a function of the gap width $l_g$, for pressure differences $\Delta P = 3200$ (triangles), 3700 (circles), and 4200 atm (squares). Inset: Dynamic evolution of $\Delta N_H$ (the reduction of the number of water molecules in the high-pressure reservoir) for gap widths $l_g = 0.0$ (red), $8$ Å (black), $13$ Å (blue), and $18$ Å (green) for $\Delta P = 3700$ atm.

![](./images/812571536991977473_8.jpg)

![](./images/812571536991977473_9.jpg)
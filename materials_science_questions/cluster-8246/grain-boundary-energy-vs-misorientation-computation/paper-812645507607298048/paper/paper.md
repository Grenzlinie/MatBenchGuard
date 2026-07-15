# Effect of symmetrical tilt grain boundary on the compatibility between copper and liquid lithium: Atomistic simulations

Chao Xu $^{a}$, Jun Wei $^{a}$, Bowen Huang $^{a,**}$, Xiancai Meng $^{b,c}$, Shifang Xiao $^{b}$, Huiqiu Deng $^{b}$, Wangyu Hu $^{a,b,*}$

$^{a}$ College of Materials Science and Engineering, Hunan University, Changsha, 410082, China
$^{b}$ Department of Applied Physics, School of Physics and Electronics, Hunan University, Changsha, 410082, China
$^{c}$ Institute of Plasma Physics, Chinese Academy of Sciences, Hefei, 230031, China

---

## ARTICLE INFO

**Article history:**
Received 31 December 2019
Received in revised form
23 March 2020
Accepted 14 April 2020
Available online 21 April 2020

**Keywords:**
Grain boundary
Cu-Li solid-Liquid interface
Compatibility
Penetration
Simulation

---

## ABSTRACT

The compatibility between Cu and liquid Li directly affects the safety of fusion devices. In this work, we investigated the compatibility between Cu Σ3 (111), Σ3 (112) and Σ5 (310) symmetrical tilt grain boundaries (STGB) and liquid Li using molecular dynamics (MD) simulation. The Li atoms rapidly penetrate the intergranular area along Σ3 (112) and Σ5 (310) grain boundaries (GBs), resulting in the formation of liquid grooves at the junctions of GBs and solid-liquid interfaces. However, the Σ3 (111) GB shows its resistance to Li penetration. In addition, the interfacial alloying and dissolution of Cu atoms are accelerated by Σ5 (310) GB via promoting the escape of Cu atoms. Then we calculated the potential energy distribution of Cu atoms which indicates the liquid metal embrittlement (LME) effect exists between Cu bicrystal and liquid Li. And we demonstrate this embrittlement has a strong correlation with the vacancy formation energy and the segregation energy of Li atoms. Comparing with the experimental results, our simulation results explain the corrosion morphology of polycrystalline Cu in liquid Li, and point out that the LME is the root cause of Cu specimen fragmentation.

© 2020 Elsevier B.V. All rights reserved.

---

## 1. Introduction

Liquid lithium (Li) is regarded as the candidates of coolant, tritium breeder and plasma-facing materials (PFMs) in fusion devices [1-5], because of its excellent performances on thermal conductivity, tritium releasing and suppressing impurities. While solid copper (Cu) is widely used in heat sink, sealing ring, and divertor. Normally, there is a layer of stainless steel existing on the surface of limiter which prevents the direct contact between Cu heat sink and liquid Li [2-5]. However, the recent study in Experimental Advanced Superconducting Tokamak (EAST) indicates that the high-energy particles severely damaged the flowing liquid Li limiter (FLiLi) [5], causing that the Cu heat sink was corroded by liquid Li. Our recent experiments [6] reported extremely poor compatibility between solid Cu and liquid Li. In the liquid Li corrosion process, a large number of Cu fragments fell off the specimens and even the Cu bulk was completely disintegrated. Then, the GBs are exposed on the residual sample's surface, and the grain edge morphology changes from angular shape to smooth pebble shape. Therefore, a detailed understanding of the interaction between solid Cu and liquid Li is the critical to their further utilization, more importantly, is for the security of the fusion reactor.

To understand this interaction, the first step is to point out the thermodynamics, kinetics and structural properties of solid-liquid interfaces, which play key roles in material performances [7-9]. Although with the help of X-rays scattering and high-resolution transmission electron microscopy (HRTEM) we are able to observe the morphology of the solid-liquid interface [10-14], the experimental devices still limit the direct observation of the microstructure and characteristics. Attributing to the advances of computer hardware and the developments of algorithm, molecular dynamics (MD) simulation has exhibited its power in the study of the solid-liquid interface. Meanwhile, the development of interatomic potential for alloy has promoted the study of heterogeneous solid-liquid interface, and a series of simulation works have been

---

* Corresponding author. College of Materials Science and Engineering, Hunan University, Changsha, 410082, China.
** Corresponding author.
E-mail addresses: bowen_huang@hnu.edu.cn (B. Huang), wyuhu@hnu.edu.cn (W. Hu).

https://doi.org/10.1016/j.jallcom.2020.155212
0925-8388/© 2020 Elsevier B.V. All rights reserved.

![](./images/812645507607298048_1.jpg)

Fig. 1. Relaxed atomic structures of Cu GBs. (a)-(c) represents the Cu Σ3 (111), Σ3 (112) and Σ5 (310) GBs, respectively. The red and blue spheres in (a) and (b) correspond to the atom positions in alternating {110} planes and in (c) correspond to the atom positions in alternating {001} planes. (For interpretation of the references to colour in this figure legend, the reader is referred to the Web version of this article.)

<table><caption>Table 1
The configuration parameters of Cu GBs: misorientation angles $\theta(^{\circ})$ and GB energies $\gamma$ ($\mathrm{J/m^2}$).</caption>
<thead>
<tr>
<th>GBs</th>
<th>$\theta(^{\circ})$</th>
<th>$\gamma$ ($\mathrm{J/m^2}$)</th>
</tr>
</thead>
<tbody>
<tr>
<td>$\Sigma=3\ (111)[1\overline{1}0]$</td>
<td>109.47</td>
<td>0.008</td>
</tr>
<tr>
<td>$\Sigma=3\ (112)[1\overline{1}0]$</td>
<td>70.53</td>
<td>0.616</td>
</tr>
<tr>
<td>$\Sigma=5\ (310)[001]$</td>
<td>36.87</td>
<td>0.964</td>
</tr>
</tbody>
</table>

<table><caption>Table 2
The configuration parameters of solid-liquid interfaces.</caption>
<thead>
<tr>
<th></th>
<th>x length (Å)</th>
<th>y length (Å)</th>
<th>z length (Å)</th>
<th>Atom number</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cu Σ3 (111)-Liquid Li</td>
<td>142.63</td>
<td>176.49</td>
<td>219.62</td>
<td>337,770</td>
</tr>
<tr>
<td>Cu Σ3 (112)-Liquid Li</td>
<td>151.30</td>
<td>203.83</td>
<td>221.30</td>
<td>415,710</td>
</tr>
<tr>
<td>Cu Σ5 (310)-Liquid Li</td>
<td>138.07</td>
<td>172.22</td>
<td>227.12</td>
<td>331,890</td>
</tr>
</tbody>
</table>

reported [15-21]. Qi et al. [15] and Yang et al. [18] adopted the atomistic fine-scale density profile, two-dimensional density map, and the Fourier structure factor to examine the atomistic microstructures and the transport properties of Cu-Ni and Al-Pb solid-liquid interfaces, respectively. In their reports, the density profile peaks in the liquid side near the interface confirmed the layered structures observed in the experiment, and the two-dimensional density maps suggest that these layered structures are ordered. Palafox-Hernandez et al. [16] found the existence of interfacial alloying by the overlapping density peaks in the (100) orientation of Cu-Pb solid-liquid interface at 625 K. However, in the (111) direction, only a pre-freezing Pb layer was observed but no alloying layer, and the pre-freezing layer disappeared at 750 K. In contrast, Yang et al. [19] indicated that the interfacial alloying in the (111) interface of the Ta-Cu solid-liquid system is rather significant.

Another important concept between liquid metal and metallic polycrystal is the liquid metal embrittlement (LME). As a form of LME, the formation of liquid grooves along the intersecting lines between grain boundary and the solid-liquid interface will greatly affect the strength of the solid metal. It has been found experimentally that a series of solid-liquid metal combinations have LME effects, such as Al-Ga [22,23], Cu-Bi [24,25], Ni-Bi [26], etc. In the early stage, the widely accepted LME mechanism is that the liquid metal atoms permeate the intergranular region and reduce the stability of GB structures. Recent experiments showed that the formation of intermetallic compounds at the GBs [26] is one of the factors leading to LME. Moreover, plenty of the MD simulations [27-33] and density functional theory (DFT) calculations [34-37] have been done to understand the LME mechanism from the atomistic level. Namilae et al.'s MD simulation results [31] illustrated that LME is significantly dependent on GB structures and external loading conditions. Rajagopalan et al. [33] employed both MD and DFT calculations to explore the mechanism of liquid Ga embrittlement of Al GBs from atomistic-scale energetics. They concluded that the dependence of LME on GB structures is strongly correlated with the binding energies of vacancies and the segregation energies of Ga. Besides the explanation in terms of energy, the atomistic size effect is also the cause of GB embrittlement. Schweinfest [34] et al. reported that the mechanism of Bi embrittlement of Cu GBs is the oversized Bi atoms weaken the interatomic bonding at GBs via pushing apart the Cu atoms.

In this paper, the influence of STGBs on the compatibility between Cu and liquid Li was investigated in terms of the microstructure evolution of solid-liquid interface, the penetration of Li atoms, and the dissolution of Cu atoms. In section 2, we will introduce our modeling and simulation process. Then, the results and discussion are presented in section 3. Finally, we will summarize our results in section 4.

## 2. Methodology

Molecular dynamics simulation was performed using LAMMPS [38] code with a time step of 2.0 fs, and a three-dimensional periodic boundary condition was employed in all of the simulations. The Nose-Hoover thermostat [39,40] and Parrinello-Rahman [41] barostat were adopted to control the temperature and pressure, respectively. We employed the modified analytic embedded-atom method (MAEAM) potentials developed by our group to describe the interactions between atoms [42]. This potential has been used to simulate the wetting of Li droplet on the surface of Cu [43] and the compatibility between Cu single crystal and liquid Li [44].

To simulate the compatibility between Cu GBs and liquid Li, we constructed Σ3 (111), Σ3 (112) and Σ5 (310) GB structures with GB energies from low to high. Then the GBs were relaxed with energy minimization procedures to get the stable configurations. The relaxed GB structures and corresponding model parameters were shown in Fig. 1 and Table 1, respectively. The prepared Cu GB models were fully equilibrated at specified temperatures with NPT ensemble to determine the dimensions of the interfaces. According to the size of the GB structure in the xy plane, the solid Li bulk was constructed and then melted at the same temperature using NPzAT ensemble, which is a NPT ensemble that only allowed the relaxation of box in z direction. After that, the Cu GBs and liquid Li bulks were assembled along z direction to construct the initial configurations of solid-liquid systems, and the configuration parameters were listed in Table 2. In the assembling process, the {110} crystal planes of Cu Σ3 (111) and Σ3 (112) GB structures were oriented to the liquid Li, and this crystal plane for Cu Σ5 (310) GB was {001} plane. A gap of 0.3 nm between the Cu GBs and liquid Li was reserved to mitigate the interaction between these two heterogeneous phases. Finally, the solid-liquid interface models were

relaxed 3.0 ns using NPzAT simulations to investigate the structural and compositional changes of the interface, and then simulated with NVT ensemble for 100 ps to calculate the density profiles, the penetration depth of Li atoms and the concentration of dissolved Cu atoms, as well as the potential energy distribution of Cu atoms.

## 3. Results and discussions

Fig. 2 shows the relaxed configurations of solid-liquid interfaces after 3.0 ns (we will use Σ3 (111), Σ3 (112) and Σ5 (310) to represent the three interfaces in the following discussion) at 600 K, 800 K, and 1000 K respectively. Similar to the interfaces between Cu single crystals and liquid Li [44], the interfacial alloying is still observed in all cases. A small amount of Li atoms permeate into the intergranular region along the Σ3 (112) GB, while the infiltration is more significant in the Σ5 (310) GB at the same temperature. As a result, the liquid Li corrodes the grain edges and forms grooves at the penetration regions. With the increase of temperature, the Li atoms penetrate the deeper region, causing the extending of the liquid groove. However, for the Σ3 (111) GB that has the lowest GB energy among all these 3 models, there is no obvious Li infiltration within our temperature range, and no modification of the interface's morphology, which can link to the interface formed by Cu (110) crystal planes contacting with liquid Li.

The curves of penetration depths over time (see Fig. 3(a)-3(c)) display that Li atoms penetrate rapidly into Cu bulks at the initial stage, and then the penetration rates decrease after Li atoms penetrate several crystal planes. The penetration rate in the Σ3 (111) interface is the lowest among the three models and the penetration almost stopped in a short period, in contrast, the Σ5 (310) interface has the highest penetration rate. Below and above 900 K, Σ3 (112) interface shows two different behaviors. Below 900 K, the penetration rate decreases rapidly to a very slow rate even tends to stop, while above this temperature, the Li atoms continue to penetrate along Σ3 (112) GB. Fig. 3(d) shows that the penetration depths increase with the temperature. And the rates of growth at Σ3 (112) and Σ5 (310) interfaces are faster than that in Σ3 (111) interface, which suggests that the penetration of Li atoms along Σ3 (112) and Σ5 (310) GBs is more susceptible to temperature. At the same temperature, the penetration depths at the three interfaces are different. The Σ5 (310) interface has the deepest penetration, followed by Σ3 (112) interface, and the penetration depth in the Σ3 (111) interface is the shallowest. The penetration depth in Σ5 (310) interface reached about 50 Å at 1000 K soon, which is approximately half the length of the Cu bicrystal. Since we use three-dimensional periodic boundary conditions, the Cu bulks

![](./images/812645507607298048_2.jpg)

Fig. 2. Snapshots of Cu Σ3 (111)-Li, Cu Σ3 (112)-Li and Cu Σ5 (310)-Li solid-liquid interfaces at 600 K, 800 K and 1000 K. The red and blue spheres represent the Cu and Li atoms, respectively. (For interpretation of the references to colour in this figure legend, the reader is referred to the Web version of this article.)

![](./images/812645507607298048_3.jpg)

Fig. 3. The time and temperature dependent penetration depth of the Li atoms in the three interfaces, Figs. (a)-(c) correspond to Σ3 (111), Σ3 (112) and Σ5 (310) interfaces, respectively.

are eroded from the upper and lower directions. Therefore, the penetration depth of 50 Å suggests that the Li atoms almost penetrate the entire Σ5 (310) GB. It can be inferred that if the relaxation time is sufficient, continuous Li penetration allows the entire Σ5 (310) GB to be penetrated at low temperatures. Once the GB is fully penetrated, the intergranular fracture will occur.

The fine-scale density profiles and two-dimensional density maps are employed to display the microstructure of the interface. As shown in Fig. 4, each peak of the fine-scale density profiles represents an atomic plane, and the overlapping density peaks denote the intersection of atomic planes. Unlike the interfaces between Cu single crystals and liquid Li [44], the overlapping density peaks in the present case are caused by both interfacial alloying and the GB penetration of Li atoms. To distinguish them, we select 6 atomic layers in the interfaces (the 6 atomic layers are marked with green numerals in Fig. 4) and use the two-dimensional density maps to analyze their in-plane structures. Fig. 5 displays the two-dimensional density of Li atoms in the first to third labeled atomic layers at 800 K. At this temperature, significant alloying reactions have taken place at the interfaces and all the three GBs have not been completely penetrated. As shown in Fig. 5(a)-5(c), the distribution of Li atoms in all three layers at Σ3 (111) interface are scattered, indicating the overlapping density peaks of Cu and Li in the density profiles (see Fig. 4(a)) are only caused by interfacial alloying. The absence of Li atoms aggregation near the grain boundary demonstrates that the Σ3 (111) GB is not the penetration channel of Li atoms. Instead, in Fig. 5(d)-5(i), due to the significant penetration of Li atoms along the Σ3 (112) and Σ5 (310) GBs, the distributions of Li atoms are concentrated near the GBs. Furthermore, the Li atoms participating in the interface alloying are still scattered in the regions far away from the GBs in the second and third labeled alternating crystal planes. In the first labeled layers of Σ3 (112) and Σ5 (310) interfaces, all the Li atoms aggregate near the GBs, which suggests the Li atoms enter the first labeled layers of these two interfaces only via the penetration along GBs. Now we can confirm that the first labeled atomic layers in the density profiles of Σ3 (112) and Σ5 (310) interfaces are the demarcation lines of interfacial alloying and the GB penetration of Li atoms. In other words, the overlapping density peaks of Fig. 4(b) and (c) on the right side of the first labeled layers are the results of interfacial alloying and penetration of Li atoms along GBs, while the left overlapping density peaks are produced by the penetration of Li atoms along GBs.

After confirming the demarcation lines of interfacial alloying and GB penetration, we marked the positions of the Cu surfaces with black dotted lines to investigate the interfacial alloying of the three models. Since the surfaces of Σ3 (111) and Σ3 (112) GB structures contacting with liquid Li are the alternating Cu {110} planes and the surface for Σ5 (310) GB is alternating Cu {001} plane, the numbers of overlapping density peaks produced by interfacial alloying in the current three cases are compared with its numbers in the (110) and (001) interfaces [44] to examine the influence of

![](./images/812645507607298048_4.jpg)

Fig. 4. The fine-scale density profiles of the three solid-liquid interface at 600 K and 800 K, the Figs. (a)-(c) correspond to Σ3 (111), Σ3 (112) and Σ5 (310) interfaces, respectively.

these GBs on interfacial alloying. In the cases of 600 K and 800 K, there are two overlapping density peaks on the right side of the black dotted lines in Σ3 (111) and Σ3 (112) interfaces (see Fig. 4(a) and (b)), which means that the interfacial alloying forms two additional alloy layers. This is consistent with the case in the {110} interface. An interesting phenomenon is that there is an additional overlapping density peak at Σ5 (310) interface at the case of 600 K (see Fig. 4(c)), but this does not exist in the (001) interface, indicating the higher alloying degree at Σ5 (310) interface. However, the number of additional alloying layers at Σ5 (310) interface at 800 K is almost identical to that at (001) interface. Apparently, the Σ5 (310) GB promotes interfacial alloying at low temperatures, and the promoting effect will be weakened or even disappear with the increase of temperature.

As the formation of an additional interfacial alloy layer requires Cu atoms to escape from the substrate and participate in the interfacial alloying, the trajectories and sources of the escaped Cu atoms are examined to find out the reason why these GBs have different effects on the interfacial alloying. The criterion for determining the escape of Cu atoms is that the location of the Cu atom is outside the surface of the initial configuration. The source distribution pattern of escaped Cu atoms can also be exhibited by two-dimensional density maps. Fig. 6 displays the in-plane distribution and the distribution perpendicular to GBs of the source of escaped Cu atoms at 600 K. The distribution perpendicular to GBs is obtained via calculating the average value of the two-dimensional density parallel to GB. As Fig. 6(a) shows that the source of escaped Cu atoms at the Σ3 (111) interfaces are scattered in the alternating {110} crystal planes and its distribution along the direction perpendicular to Σ3 (111) GB has no obvious fluctuation, which illustrates there is no difference in the numbers of Cu atoms escaping from the vicinity of Σ3 (111) GB and the inside of {110} crystal planes. In the Σ3 (112) interface (see Fig. 6(b)), the indistinct peaks at the positions of Σ3 (112) GB suggest that there are slightly more Cu atoms escaping from the vicinity of Σ3 (112) GB than from the interior of {110} crystal planes. The Cu atoms are escaped mainly from the {110} crystal planes, thus the Σ3 (111) and Σ3 (112) GBs do not affect the interface alloying. For the Σ5 (310) interface, Fig. 6(c) displays that the escaped Cu atoms mainly come from the vicinity of the Σ5 (310) GB. Thus, the Σ5 (310) GB promotes the escape of Cu atoms, which provides more Cu atoms for the interface alloying than (001) interface. By examining the configuration snapshots in Fig. 2, we find that the Cu atoms escape from Σ5 (310) GB and are adsorbed to the surface, then Li atoms mix with the adsorbed Cu atoms to form the additional alloy layers by the pre-freezing effect of the solid-liquid interface. With the increase of temperature, the freezing effect of the interface on the escaping atoms is weakened, so the promoting effect of the escaping atoms on the interface alloying is also weakened. When we examine the configuration snapshots, we also find that some escaped Cu atoms at Σ5 (310) interface dissolve into liquid Li.

In addition to the GB penetration and interfacial alloying, the dissolution of Cu atoms is another focus of the study on the compatibility between solid Cu and liquid Li. When a Cu atom diffuses to the region outside the zero point of fine-scale density profile, it is recognized as a dissolved Cu atom. The time and temperature-dependent concentrations of dissolved Cu atoms are shown in Fig. 7. The curves of concentrations over time (see Fig. 7(a)-7(c)) show that the growth rates of Cu concentration gradually decreased with the dissolution of Cu atoms, and the curve of the concentrations over temperature (see Fig. 7(d)) displays that the concentrations in the three systems are basically the same after 3.0 ns relaxation. Interestingly, as shown in Fig. 7 (c), the concentration measured from the Σ5 (310) interface (the concentration measured from the interface in this section refers to the Cu concentration in liquid Li) shows a decreasing tendency at the later relaxation stage of 1000 K. This suggests that the strong adsorption and desorption of Cu atoms in the solid-liquid interface at high temperature lead to the concentration fluctuation. And the concentration fluctuation causes slight differences between the values measured from the three systems at 900 K and 1000 K. Due to the Cu atoms are mainly escape from the {110} crystal planes at Σ3 (111) and Σ3 (112) interfaces, the concentration of dissolved Cu atoms measured from these two interfaces are same as the result measured from (110) interface. Although the Cu atoms dissolve into liquid Li from the {001} crystal planes in Σ5 (310) and (001) interfaces, the concentration measured from the Σ5 (310) interface is higher than that measured from the (001) interface, suggesting that Σ5 (310) GB accelerates the dissolution of Cu atoms. Also, our previous simulation results showed that when the temperature is

![](./images/812645507607298048_5.jpg)

Fig. 5. The two-dimensional density maps of Li atoms at 800 K, Figs. (a)-(c) correspond to the 1-3 layers in Σ3 (111) interface, respectively; Figs. (d)-(e) correspond to the 1-3 layers in Σ3 (112) interface, respectively; Figs. (g)-(i) correspond to the 1-3 layers in Σ5 (310) interface, respectively.

![](./images/812645507607298048_6.jpg)

Fig. 6. The source of escaped Cu atoms and their distributions along the direction perpendicular to GBs for the three interfaces at 600 K, Figs. (a)-(c) correspond to Σ3 (111), Σ3 (112) and Σ5 (310) interfaces, respectively.

below 1000 K the concentration measured from the (001) interface after 3.0 ns relaxation is lower than that measured from the (110) interface because Cu atoms are more difficult to dissolve from the relatively close-packed {001} crystal planes [44]. In the current three interfaces, the difference in dissolution rate of Cu atoms from {001} and {110} crystal planes has been eliminated by the accel- erated effect of Σ5 (310) GB on the dissolution of Cu atoms.

As Li atoms permeate into intergranular regions along the Σ3 (112) and Σ5 (310) GBs, the stability of Cu bicrystals is inevitably affected. It is well known that the stability of an atom depends on its potential energy. And the higher the potential energy of an atom, the more unstable it is, on the contrary, the more stable the atom is. To study the stability of Cu atoms around GBs after the penetration of Li atoms, we calculate the potential energy distribution of Cu atoms along the direction perpendicular to GBs and depict it in Fig. 8. As with the fine-scale density profile, the calculation process of the potential energy distribution of Cu atoms begins by slicing the statistical region into many bins and then counting the average potential energy of Cu atoms in each bin as the potential energy of the location of that bin. The statistical region extends from the boundary of GB penetration and interfacial alloying to the deepest penetration of Li atoms. The results illustrate that the potential energy of Cu atoms near the GB is higher than that inside the crystal plane, and the potential energy of Cu atoms near the Σ5 (310) GB is higher than that near the Σ3 (112) GB, which indicates Cu atoms are more unstable near the Σ5 (310) GB. This may be the reason why Cu

![](./images/812645507607298048_7.jpg)

Fig. 7. The time and temperature dependent dissolved Cu atomic concentrations in the three interfaces, Figs. (a)-(c) correspond to Σ3 (111), Σ3 (112) and Σ5 (310) interfaces, respectively.

![](./images/812645507607298048_8.jpg)

Fig. 8. The potential energy distribution of Cu atoms along the direction perpendicular to GBs in the case of 800 K, (a) and (b) correspond to the cases of Cu Σ3 (112) and Σ5 (310) GBs, respectively.

atoms are more likely to escape from the vicinity of Σ5 (310) GB. After the penetration of Li atoms, the increase of potential energy of these Cu atoms suggests the decrease of the GB stability. The Li atoms penetrating the Cu intergranular region produce the LME effect, and it will lead to the brittle fracture of Cu polycrystal. It can be inferred that the stability difference of Cu atoms near different GBs may be the reason for the different degrees of compatibility between Cu bicrystals and liquid Li. Generally speaking, the higher the GB energy, the higher the potential energy and the less stable the Cu atom near it will be. This means that Cu GBs with high GB energies have poor compatibility with liquid Li. If the LME is taken as the evaluation criterion, the compatibility between the liquid Li and the Σ5 (310) GB with the highest GB energy is the worst, while the Σ3 (111) GB with the lowest GB energy has the best

![](./images/812645507607298048_9.jpg)

Fig. 9. (a)-(c) The Cu vacancy binding energies as functions of distances from the Σ3 (111), Σ3 (112) and Σ5 (310) GBs, respectively. (d)-(f) The Li segregation energies of Li as functions of distances from the Σ3 (111), Σ3 (112) and Σ5 (310) GBs, respectively.

compatibility with liquid Li.

In terms of atomistic-scale energetics, the vacancy binding energy and segregation energy play significant roles in LME [33]. Vacancy binding energy of Cu determines the stability of the substrate, the substitution of Li atoms as well as their transport along GBs. Generally, the larger the negative value of binding energy indicates that the bond between vacancy and Cu GB is stronger. And the vacancies are favorable for the diffusion of Li atoms in the Cu substrate. For another, the segregation energy of Li determines the interfacial phases at GBs. And if the segregation energy is negative, the segregation of Li atoms is advantageous in energy. Fig. 9 shows the two energies as functions of distance from the GB planes. Before the calculation of the vacancy binding energy, the vacancy formation energy at a site $\alpha$ is calculated by
$$
E_{f}^{\alpha}=E_{GB}^{\alpha}-E_{GB}+E_{coh},
$$
where $E_{GB}^{\alpha}$ and $E_{GB}$ are the total energy of the GB configuration with and without a vacancy, respectively. $E_{coh}$ is the cohesive energy of per atom in a perfect crystal. The binding energy is defined as
$$
E_{b}^{\alpha}=E_{f}^{\alpha}-E_{f}^{0},
$$
where the $E_{f}^{0}$ is the vacancy formation energy in the bulk. The segregation energy of Li is determined by
$$
E_{\text{seg}}^{\alpha}=\left(E_{GB,Li}^{\alpha}-E_{GB}\right)-\left(E_{B,Li}^{0}-E_{B}^{0}\right),
$$
where the $E_{GB,Li}^{\alpha}$ and $E_{GB}$ are the total energies of Cu GB with and without a Li atom substituted for a Cu atom at site $\alpha$, respectively. $(E_{B,Li}^{0}-E_{B}^{0})$ represents the difference in energy between a replacement Li atom in the Cu bulk and a perfect Cu bulk. As Fig. 9 shows, most sites near the Σ3 (112) and Σ5 (310) GBs have negative vacancy binding energies and segregation energies, while the energies for the sites away from GBs are close to zero. This illustrates that the vacancies are strongly bound to these two GBs, and the Li atoms tend to segregate near these regions. For the vacancy binding energy of Cu, the value on the first atomic plane away from the Σ5 (310) GB is significantly lower than the values near the Σ3 (112) GB. Thus the Cu atoms near the Σ5 (310) GB are more unstable and have a larger probability to leave the lattice to form vacancies. On the other hand, the Σ5 (310) GB has more opportunities to provide vacancies to assist Li atoms to diffuse along the GB. For the segregation energy of Li, one of the sites on the Σ5 (310) GB plane has significantly lower segregation energy, which illustrates Li atoms also have an energy advantage in the segregation at Σ5 (310) GB. We note the vacancy binding energy and segregation energy at Σ3 (111) GB are almost zero. This reflects a fact that the Σ3 (111) GB has no influence on the formation of vacancy and the segregation of Li atoms, and the atomic configuration at Σ3 (111) GB is almost identical to a perfect crystal. Therefore, liquid Li causes LME at the Σ3 (112) and Σ5 (310) GBs, but Σ3 (111) GB shows a resistance to the LME.

Our simulation is consistent with the experimental results [3] and explained the cause of corrosion characteristics from the atomistic scale. Specifically, Li atoms permeate along GBs to form liquid grooves at the intergranular region, which results in the exposure of GBs and grain edges. The dissolution of Cu atoms at the edges removes the corners and gives the grains a pebble-like appearance. With the entire GB is penetrated by liquid Li, the polycrystalline specimen occurs intergranular fracture and the grains are detached from the main body of the specimen. The direct cause is that the LME reduces the cohesive strength of the GB. However, not all of the GBs can cause intergranular fracture because of the significant difference in compatibility between Cu GBs and liquid Li. One thing is clear that the extremely poor compatibility between polycrystalline Cu and liquid Li is caused by the LME.

## 4. Conclusions

The compatibility between Cu STGBs (Σ3 (111), Σ3 (112) and Σ5 (310)) and liquid Li was investigated at different temperatures using MD simulations. Our calculation indicates the compatibility tends to decrease with the climbing of GB energy. The Li atoms can penetrate the intergranular regions to form liquid grooves along Σ3 (112) and Σ5 (310) GBs, on the contrary Σ3 (111) GB shows great resistance to the penetration of Li atoms. Especially, we observed a severe penetration along the Σ5 (310) GB, which contributed to the promotion of interfacial alloying and dissolution of Cu atoms. Moreover, the potential energy of Cu atoms near the GB increased after the penetration of liquid Li, indicating that the LME effect occurred between the Cu GBs and liquid Li, which is the direct factor of the fragmentation of polycrystalline Cu in liquid Li. Finally, we illustrated that the difference of LME effects between the Cu GBs and liquid Li are strongly related to the vacancy binding energy and the Li segregation energy.

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

We deeply appreciate your consideration of our manuscript, and we look forward to receiving comments from the reviewers.

## CRediT authorship contribution statement

Chao Xu: Conceptualization, Investigation, Methodology, Formal analysis, Validation, Writing - original draft, Writing - review & editing. Jun Wei: Formal analysis, Methodology, Validation. Bowen Huang: Conceptualization, Supervision, Formal analysis, Methodology, Writing - review & editing. Xiancai Meng: Conceptualization, Methodology. Shifang Xiao: Conceptualization, Supervision, Methodology. Huiqiu Deng: Conceptualization, Resources, Formal analysis, Methodology. Wangyu Hu: Funding acquisition, Conceptualization, Formal analysis, Resources, Writing - review & editing.

## Acknowledgements

This work is supported by National Natural Science Foundation of China with Grant No. of NSFC-NSAF U1830138. We would also like to acknowledge the support of the computation platform of National Super-Computer Center in Changsha (NSCC).

## References

[1] R. Majeski, S. Jardin, R. Kaita, T. Gray, P. Marfuta, J. Spaleta, J. Timberlake, L. Zakharov, G. Antar, R. Doerner, S. Luckhardt, R. Seraydarian, V. Soukhanovskii, R. Maingi, M. Finkenthal, D. Stutman, D. Rodgers, S. Angelini, Nucl. Fusion 45 (2005) 519.

[2] J. Ren, G.Z. Zuo, J.S. Hu, Z. Sun, Q.X. Yang, J.G. Li, L.E. Zakharov, H. Xie, Z.X. Chen, Rev. Sci. Instrum. Revista. 86 (2015), 023504.

[3] X.L. Yuan, Y. Chen, J.S. Hu, J.G. Li, G.Z. Zuo, J. Ren, Y. Zhou, C.Z. Li, Z. Sun, W. Xu, X.C. Meng, M. Huang, X.W. Zheng, X.J. Yao, EAST team, Fusion Eng. Des. 112 (2016) 332-337.

[4] J.S. Hu, G.Z. Zuo, J. Ren, Q.X. Yang, Z.X. Chen, H. Xu, LE Zakharov, R. Maingi, C. Gentile, X.C. Meng, Z. Sun, W. Xu, Y. Chen, D. Fan, N. Yan, Y.M. Duan, Z.D. Yang, H.L. Zhao, Y.T. Song, X.D. Zhang, B.N. Wan, J.G. Li, EAST Team, Nucl. Fusion 56 (2016), 046011.

[5] G.Z. Zuo, J.S. Hu, R. Maingi, J. Ren, Z. Sun, Q.X. Yang, Z.X. Chen, H. Xu, K. Tritz, LE Zakharov, C. Gentile, X.C. Meng, M. Huang, W. Xu, Y. Chen, L. Wang, N. Yan, S.T. Mao, Z.D. Yang, J.G. Li, East Teama, Nucl. Fusion 57 (2017), 046017.

[6] X.C. Meng, C. Xu, G.Z. Zuo, M. Huang, K. Tritz, D. Andruczyk, Z. Sun, W. Xu, Y.Z. Qian, J.J. Huang, X. Gao, B. Yu, J.G. Li, J.S. Hu, J. Deng, Nucl. Mater. 513 (2019) 282-292.

[7] W.D. Kaplan, Y. Kauffmann, Annu. Rev. Mater. Res. 36 (1) (2006) 1-48.

[8] W.J. Boettinger, S.R. Coriell, A.L. Greer, A. Karma, W. Kurz, M. Rappaz, R. Trivedi, Acta Mater. 48 (2000) 43-70.

[9] J.J. Hoyt, M. Asta, A. Karma, Mater. Sci. Eng. R 41 (2003) 121-163.

[10] C.J. Yu, A.G. Richter, A. Datta, M.K. Durbin, P. Dutta, Phys. Rev. Lett. 82 (1999) 2326-2329.

[11] S.H. Oh, Y. Kauffmann, C. Scheu, W.D. Kaplan, M. Ruhle, Science 310 (2005) 661-663.

[12] S.E. Donnelly, R.C. Birtcher, C.W. Allen, I. Morrison, K. Furuya, M. Song, K. Mitsuishi, U. Dahmen, Science 296 (2002) 507-510.

[13] J.M. Howe, H. Saka, MRS Bull. 29 (2004) 951-957.

[14] Y. Kauffmann, S.H. Oh, C.T. Koch, A. Hashibon, C. Scheu, M. Ruhle, W.D. Kaplan, Acta Mater. 59 (2011) 4378-4386.

[15] C. Qi, J.F. Li, B. Xu, L.T. Kong, S. Zhao, Comput. Mater. Sci. 125 (2016) 72-81.

[16] J.P. Palafox-Hernandez, B.B. Laird, Mark Asta, Acta Mater. 59 (2011) 3137-3144.

[17] J.P. Palafox-Hernandez, B.B. Laird, J. Chem. Phys. 145 (2016), 211914.

[18] Y. Yang, D.L. Olmsted, Mark Asta, B.B. Laird, Acta Mater. 60 (2012) 4960-4971.

[19] G.Q. Yang, J.F. Li, Q.W. Shi, L.T. Kong, Comput. Mater. Sci. 86 (2014) 64-72.

[20] G. Yang, X. Gao, J. Li, L. Kong, J. Appl. Phys. 117 (2015) 15303.

[21] X.L. Gan, S.F. Xiao, H.Q. Deng, X.F. Li, W.Y. Hu, J. Alloys Compd. 687 (2016) 875-884.

[22] W. Ludwig, E. Pereiro-Lopez, D. Bellet, Acta Mater. 53 (2005) 151-162.

[23] E. Senel, S.C. Walmsley, S. Diplas, K. Nisancioglu, Corrosion Sci. 85 (2014) 167-173.

[24] G. Duscher, M.F. Chisholm, U. Alber, M. Rühle, Nat. Mater. 3 (2004) 621-626.

[25] A. Kundu, Km Asl, J. Luo, M.P. Harmer, Scripta Metall. 68 (2013) 146-149.

[26] J. Luo, H. Cheng, Km Asl, C.J. Kiely, M.P. Harmer, Science 333 (2011) 1730.

[27] E. Pereiro-Lopez, W. Ludwig, D. Bellet, P. Cloetens, C. Lemaignan, Phys. Rev. Lett. 95 (2005), 215501.

[28] W. Ludwig, E. Pereiro-Lopez, D. Bellet, Acta Mater. 53 (2005) 151-162.

[29] H.S. Nam, David J. Srolovitz, Phys. Rev. Lett. 99 (2007), 025501.

[30] H.S. Nam, David J. Srolovitz, Phys. Rev. B 76 (2007), 184114.

[31] S. Namilae, B. Radhakrishnan, J.R. Morris, Model. Simulat. Mater. Sci. Eng. 16 (2008), 075001.

[32] J. Kang, G.C. Glatzmaier, S. Wei, Phys. Rev. Lett. 111 (2013), 055502.

[33] M. Rajagopalan, M.A. Bhatia, Ma Tschopp, D.J. Srolovitz, K.N. Solanki, Acta Mater. 73 (2014) 312-325.

[34] R. Schweinfest, A.T. Paxton, M.W. Finnis, Nature 432 (2004) 1008.

[35] Y. Zhang, G.H. Lu, T.M. Wang, S.H. Deng, X.L. Shu, M. Kohyama, R. Yamamoto, J. Phys. Condens. Matter 18 (2006) 5121-5128.

[36] S. Zhang, O.Y. Kontsevoi, A.J. Freeman, G.B. Olson, Acta Mater. 59 (2011) 6155-6167.

[37] K.D. Bauer, M. Todorova, K. Hinger, J. Neugebauer, Acta Mater. 90 (2015) 69-76.

[38] S. Plimpton, J. Comput. Phys. 117 (1995) 1-19.

[39] S. Nose, J. Chem. Phys. 81 (1984) 511-519.

[40] W.G. Hoover, Phys. Rev. 31 (3) (1985) 1695-1697.

[41] M. Parrinello, A. Rahman, Phys. Rev. Lett. 45 (14) (1980) 1196-1199.

[42] J. Tang, J. Yang, J. Nanoparticle Res. 17 (2015) 299.

[43] X. Chen, X.G. Sun, H.Q. Deng, S.F. Xiao, X.L. Gan, X.F. Li, W.Y. Hu, Comput. Mater. Sci. 119 (2016) 114-119.

[44] C. Xu, X.C. Meng, X.G. Sun, X.L. Gan, P. Li, S.F. Xiao, H.Q. Deng, X.F. Li, W.Y. Hu, J. Alloys Compd. 763 (2018) 1-10.
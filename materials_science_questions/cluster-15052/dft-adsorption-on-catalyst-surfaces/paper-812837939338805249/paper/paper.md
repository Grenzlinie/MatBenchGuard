# Modulation of Ag modification on $NO_2$ adsorption and sensing response characteristics of Si nanowire: A DFT study

Yuxiang Qin$^{a,b,c,*}$, Liming Zhao$^{a}$, Yunqing Jiang$^{a}$

$^{a}$ School of Microelectronics, Tianjin University, Tianjin 300072, China
$^{b}$ Tianjin Key Laboratory of Imaging and Sensing Microelectronic Technology, Tianjin University, Tianjin 300072, China
$^{c}$ Key Laboratory for Advanced Ceramics and Machining Technology, Ministry of Education, School of Materials Science and Engineering, Tianjin University, Tianjin 300072, China

---

## ARTICLE INFO

**Keywords:**
Gas sensor
Etching mechanism
$NO_2$-sensing mechanism
Density functional calculations

## ABSTRACT

Surface modification by noble metal nanoparticles has been proved highly effective on response enhancement of a semiconductor gas sensor. In this work, the adsorption of $NO_2$ on Ag-modified silicon nanowire (Ag@SiNW) was investigated by means of density functional theory (DFT) calculations with aim to explore the nature and theoretical mechanism of Ag modification for sensing response enhancement. Ag surface modification tunes the electronic structure of SiNW considerably, which is further moderated by the spontaneous adsorptions of $NO_2$ on surface Si site and on the modified Ag atom. The modified Ag as a donor creates an n-doping state, activating the surface Si atom and promoting the adsorption of Si surface to $NO_2$ gas. Nevertheless, Mulliken charge transfer calculations clarify that the enhanced response observed experimentally for an Ag@SiNW sensor is mainly attributed from the gas adsorption right on Ag atom. The adsorbed $NO_2$ on modified Ag atom captures 1.27 e from the nanowire surface, which is more than twice as much as that with Si site adsorption. The calculations on geometry and charge density difference reveal the catalyst nature of the modified Ag for $NO_2$ adsorption and further clarify theoretically the possible reaction of $NO_2$, i.e., dissociation and spillover, occurring on the Ag atom. Besides, a defect-induced preferential etching mechanism of metal (Ag)-assisted chemical etching (MACE) for SiNW was proposed from a new perspective based on the lattice distortion analysis induced by Ag modification.

---

### 1. Introduction

SiNWs have attached considerable attention in recent years due to their unique physical and chemical properties and potential applications in a variety of nano/optoelectronics [1–6]. Especially, the high chemical activity and large specific surface area of the featured one-dimensional nanostructure make them an attractive candidate for gas sensor applications to detect various toxic and hazardous gases such as $H_2$, $NO_2$, $NH_3$ and $CH_4$ [7–9], which have been demonstrated by a large body of experimental results. A recent DFT study by A. Miranda, et al. further theoretically address the capability and potential of SiNW as molecule sensors for sensing other harmful gases including NO, $SO_2$, CO and HCN [10].

Among various toxic gases, $NO_2$ gas resulted from combustion and automotive emissions is highly harmful to the environment and human health; it is a main source of acid rain and photochemical smog [11]. Ultrasensitive and reliable detection of toxic $NO_2$ gas with much low concentration is thus of great requirement. In experiment, SiNW has been clarified capable of sensing $NO_2$ with ppb level [12]. Nevertheless, the sensitivity harvested from a pure SiNWs sensor is generally weak. Further improvement in response properties is therefore highly required. To this end, surface modification with noble metals, such as Pt or Pd, has been performed and experimentally proved to be much effective to enhance the sensing abilities of SiNWs sensors [13,14]. Very recently, our group fabricated a kind of Ag nanoparticles-modified SiNWs (Ag@SiNWs) by developing a special Ag modification process, and harvest unique response properties to ultrararefied $NO_2$ (10 ppb) [15]. The experimental result indicates a remarkable modulation effect of Ag surface modification on response characteristic of SiNW.

To give insight to the relevant experimental development of noble metal (such as Ag) modified SiNWs gas sensors with high sensitivity, theoretical exploitation for the response enhancement mechanism of surface modification will be crucial and highly desirable. As known, the sensing responses of SiNW and other semiconductor sensors are

---

* Corresponding author at: School of Microelectronics, Tianjin University, 92 Weijin Road, Nankai District, Tianjin 300072, China.
E-mail address: qinyuxiang@tju.edu.cn (Y. Qin.)

https://doi.org/10.1016/j.apsusc.2018.10.147
Received 8 June 2018; Received in revised form 9 October 2018; Accepted 16 October 2018
Available online 17 October 2018
0169-4332/ © 2018 Elsevier B.V. All rights reserved.

generally based on the conductivity variation due to surface adsorption of gas molecules. In the case of Ag modified SiNW, a systematic investigation about the adsorption and reaction behaviors of $NO_2$ molecule on the surface of Ag-modified SiNW especially on the modified Ag site will bring us an atomic-level understanding for the gas-sensing mechanism of Ag@SiNW especially response modulation characteristic of the modified Ag. It will be able to further provide a theoretical guideline for developing high sensitive gas-sensing materials. In this aspect, ab initio calculation has been demonstrated to be a suitable method for the investigation of molecule-surface interaction in a gas-adsorbed system by revealing its energetic and electronic properties. For instance, the first-principle electronic structure calculation for the adsorption of $NH_3$ and $NO_2$ on Si nanowire well explained the relevant experimental observations in different doping efficiency of $NH_3$ and $NO_2$ as well as the fundamentally atomic scale mechanisms for their different doping characters [16]. Similar calculation about electronic structure of $SO_2$ adsorption demonstrated the interaction of $SiNW-SO_2$ and clarified the different sensing characteristic of $SO_2$ from $NO_2$ [17]. These works ever reported all focus on the gas adsorption on bare SiNW. As for the noble metal-modified SiNW, however, relevant theoretical studies are scare thus far. Exploration and clarification for the issues including gas adsorption characteristic on the modified surface, the nature and mechanism for enhanced response and the actual role serving for the modified metal during gas-sensing are highly required for the design and further optimization of sensors based on modified nanowires.

In continuation of our previous experimental work concerning Ag-modified SiNW [15], here, we carry out DFT calculations studies for $NO_2$ adsorption on Ag@SiNW with purpose of exploring the nature and theoretical mechanism of Ag modification-induced response enhancement observed experimentally. The [1 0 0]-oriented SiNW is chosen to model, considering a good match to the actual SiNW experimentally fabricated from (1 0 0) Si wafer via metal-assisted chemical etching (MACE). The theoretical investigations in present work have a guiding significance to in-depth understand the modulation characteristic of noble metal modification to gas-sensing response and then to further optimize the noble metal-modified nanowire sensors. In addition, based on the analysis of lattice distortion in Ag@SiNW, we propose a defect-induced preferential etching mechanism from a new perspective, explaining the proceeding of MACE for formation of SiNW.

## 2. Calculation and modeling

### 2.1. Modeling system

The initial model of SiNW was constructed by cutting the $5\times5\times2$ supercell of diamond-structured bulk silicon with a virtual quadrangular, as illustrated in Fig. 1(a). All Si atoms outside the quadrangular were removed and the dangling bonds of surface Si, excluding the exact surface site for Ag modification or $NO_2$ adsorption, were passivated by hydrogen atoms. The direction of the quadrangular was chosen to produce wire with [1 0 0] orientation. The constructed SiNW, $M_0$, as shown in Fig. 1(a), has a diameter of 1.3 nm, which is the exact value of the thinnest sample ever reported experimentally [18]. To eliminate the interaction between neighboring nanowires, a vacuum space in the thickness of $20\mathring{A}$ was added along the transverse direction of [1 0 0] nanowire.

As for the [1 0 0]-oriented SiNW constructed in this work, the only specific facet, i.e., (0 0 1) facet, is available for gas adsorption [19]. In this work, we consider the $NO_2$ adsorption on [1 0 0]-oriented SiNW with surface modification by one Ag atom for reduced complexity. The atom site and bridge site of Si atoms at surface $(Si_1)$ and subsurface $(Si_2)$ were all considered as potential positions for Ag modification, thus forming five Ag@SiNW models (marked as $M_1$-$M_5$ as shown in Fig. 1(b-f)). Note that for the models concerning $Si_1$ atoms (i.e. $M_1$, $M_3$ and $M_4$), the Ag modification occurs at the dangling bond of the unpassivated surface $Si_1$, similar with the case of Refs. [16,20]. In this figure, the denotation of $Ag$-$Si_1$ means the direct bonding of Ag on clean site of $Si_1$ atom after pre-removing the passivated H atom on it; while the $Ag$-$Si_{11}$ displays the Ag bonding on the bridge site between $Si_1$ and $Si_1$ with both H atoms removal.

![](./images/812837939338805249_1.jpg)

Fig. 1. (a) $5\times5\times2$ Si supercell used for constructing [1 0 0]-oriented SiNW model (left) and the top view of the as-constructed SiNW model of $M_0$ (right). (b-e) Top views of the equilibrium configurations of Ag@SiNW: $M_1$ ($Ag$-$Si_1$), $M_2$ ($Ag$-$Si_2$), $M_3$ ($Ag$-$Si_{11}$), $M_4$ ($Ag$-$Si_{12}$) and $M_5$ ($Ag$-$Si_{22}$), respectively.

### 2.2. Computational details

First-principles calculations on energy and electronic structure of nanowire and corresponding gas adsorption system were performed based on density functional theory (DFT). All calculations were carried out with Cambridge Serial Total Energy Package (CASTEP) code in Materials Studio of Accelrys Inc.. Ultrasoft pseudopotential and the generalized gradient approximation (GGA) parametrized with the Perdew-Burke-Ernzerhof (PBE) exchange-correlation functional were adopted, which yielded the correct ground-state structure of the combined systems. The cutoff energy for the plane-wave expansion was set to be 340 eV. A higher cutoff energy was found to have little effect on the calculation results. The convergence criteria for structure optimization and energy calculation were set to be of fine quality with the maximum root-mean-square convergent tolerance less than $1\times10^{-5}$ eV/atom, that is, the force imposed on each atom was not greater than 0.03 eV/$\mathring{A}$ and 0.05 GPa for stress. All the geometric structures of nanowire were fully relaxed to minimize the total energy of the system until a precision of $10^{-5}$ eV is reached. The Monkhorst-pack sets of $k$ points used for the Brillouin zone sampling usually depend on the supercell dimensions. To ensure the convergence of the whole system in the calculation, in this work, we set the $k$-point to $3\times3\times3$ for all models. All calculations were performed in the reciprocal space.

In general, a larger supercell adopted can generally provide more satisfactory convergence [21]. Additional calculations for several models with much larger $5\times5\times4$ supercell and the corresponding data comparison to those with $5\times5\times2$ supercell (see Table S1 in the Supporting Materials) display small and acceptable data deviation, indicating the satisfactory convergence of configurations with small $5\times5\times2$ supercell adopted in this work.


## 3. Results and discussion

### 3.1. Ag@SiNW system and deduced MACE mechanism

The model of Ag@SiNW in Fig. 1(b)-(f) was constructed by attaching one Ag atom directly on $Si_2$ atom or the dangling bond of $Si_1$, or on their bridge site. To evaluate the stability of every modified structure, the modification energy $E_{\text{mod}}$ of a Ag atom onto the SiNW, defined as the total energy difference between the isolated individual constituents (SiNW and Ag atom) and the equilibrium configuration of the complex, is given by

$$
E_{\text{mod}} = E(\text{SiNW}) + E(\text{Ag})-E(\text{Ag@SiNW}) \tag{1}
$$

where $E(\text{Ag@SiNW})$ denotes the total energy of a modified SiNW nanowire with a single Ag atom attachment (i.e., Ag@SiNW); $E(\text{SiNW})$ and $E(\text{Ag})$ represent the total energies of the hydrogen-passivated SiNW and a free Ag atom, respectively. It should be noted that, for the configurations of $M_1$, $M_3$ and $M_4$ with surface $Si_1$ atom as modification site of Ag, the values of $E(\text{SiNW})$ are respectively calculated from the SiNW with pre-removal of the H passivation atoms on the $Si_1$ sites. According to this equation, a positive value of $E_{\text{mod}}$ indicates an energetically favorable modification process.

Table 1 shows the equilibrium bond lengths, $E_{\text{mod}}$ and charge transfers of Ag for the five optimized structures of $M_1$-$M_5$. In terms of $E_{\text{mod}}$, Ag atom bonding on the $Si_1$ or $Si_2$ atom sites or their bridge sites are all favorable energetically and thus are possibly formed on the surface of SiNW. Nevertheless, the Ag modification on the bridge site of adjacent $Si_2$ atoms (i.e., $M_5$) presents the highest $E_{\text{mod}}$ value (+4.4349 eV) and therefore is thought to be the most preferential modification structure. The largest charge transfer ($-0.76$ e) occurring during the Ag modification further hints a relative large impact of bridge-site-bonding of Ag on subsurface $Si_2$ atoms. In the next section, we will specifically discuss the adsorption properties of $NO_2$ molecule on Ag@SiNW surface based the system of $M_5$ model.

In experiments, SiNWs can be prepared via chemical/physical growth or MACE of silicon wafer [22,23]. The latter MACE method is particular appealing and widely investigated, due to its high compatibility with current silicon-based semiconductor technology and flexibility in producing vertical SiNWs on wafer scale. The MACE mechanism has been demonstrated experimentally by suggesting the possible redox reactions of Si occurring during the process, with assistance of metal catalyst (usually Ag or Au). During the process catalyzed by metal Ag, the mutual transformation of Ag species is deduced to be related to the fundamental mechanism of MACE [24]. In this work, a deep analysis for the lattice structure of SiNW due to Ag modification may give insight into the possible process proceeding during MACE from another perspective. In Table 1, the modification model of $M_5$ is calculated to have the most charge transfer, while $M_1$ shows the least charge transfer ($-0.33$ e). That is, Ag atom exhibits the low and high oxidation states in $M_1$ and $M_5$, respectively, which can be expressed intuitively by states of $Ag^0$ and $Ag^+$.

<table>
<caption>Table 1 Modification energies ($E_{\text{mod}}$), equilibrium bond length of the formation bonds and charge transfer occurring on Ag atom for different configurations.</caption>
<thead>
<tr>
<th>Modification model</th>
<th>Bond type</th>
<th>Bond length (Å)</th>
<th>$E_{\text{mod}}$ (eV)</th>
<th>Transferred charge (e)</th>
</tr>
</thead>
<tbody>
<tr>
<td>$M_1$</td>
<td>Ag-$Si_1$</td>
<td>2.364</td>
<td>+2.1365</td>
<td>−0.33</td>
</tr>
<tr>
<td>$M_2$</td>
<td>Ag-$Si_2$</td>
<td>3.109</td>
<td>+4.2930</td>
<td>−0.45</td>
</tr>
<tr>
<td>$M_3$</td>
<td>Ag-$Si_1$</td>
<td>2.494</td>
<td>+2.9642</td>
<td>−0.40</td>
</tr>
<tr>
<td rowspan="2">$M_4$</td>
<td>Ag-$Si_1$</td>
<td>2.552</td>
<td rowspan="2">+2.5711</td>
<td rowspan="2">−0.66</td>
</tr>
<tr>
<td>Ag-$Si_1$</td>
<td>2.397</td>
</tr>
<tr>
<td rowspan="3">$M_5$</td>
<td>Ag-$Si_2$</td>
<td>3.744</td>
<td rowspan="3">+4.4349</td>
<td rowspan="3">−0.76</td>
</tr>
<tr>
<td>Ag-$Si_2$</td>
<td>2.830</td>
</tr>
<tr>
<td>Ag-$Si_2$</td>
<td>2.760</td>
</tr>
</tbody>
</table>

![](./images/812837939338805249_2.jpg)

Fig. 2. Geometry structure comparison of $M_0$ (SiNW before Ag modification), $M_1$ (Ag modification on surface $Si_1$ atom) and $M_5$ (Ag modification on bridge site of subsurface $Si_2$ atom).

Fig. 2 shows that geometry structures of $M_0$ (SiNW before Ag modification), $M_1$ (with low oxidation of Ag) and $M_5$ (with high oxidation of Ag). Observe that the distance of adjacent Si atoms along [0 0 1] direction is shortened from $3.738$\AA\ in $M_0$ to $3.552$\AA\ in $M_1$, while that of [0 1 1] only shows a slight change from $2.331$\AA\ to $2.321$\AA, indicating the surface modification of Ag with low oxidation state ($Ag^0$ state) on the surface $Si_1$ atom causes an obvious lattice distortion beneath the Ag atom in the [0 0 1] direction. Under the modification by Ag with high oxidation state ($Ag^+$ state) in $M_5$, similar lattice distortion is also induced in the same direction of [0 0 1] due to the interaction between Ag and subsurface Si. As seen, the obvious change in the distance along [0 0 1] varies from $3.770$\AA\ in $M_1$ to $3.860$\AA\ in $M_5$ with the modified Ag changing from $Ag^0$ state to $Ag^+$ state. Above geometry analysis demonstrates a fact that the Ag modification on SiNW induces a significant lattice distortion along [0 0 1] direction, which further proceeds in the same direction with $Ag^0$ state transforming to high oxidation state of $Ag^+$. The distorted lattices produce defective sites proceeding in the [0 0 1] direction, where the energy barrier for redox reaction is lower. As a diamond-like crystal, the silicon will show the same lattice change in the anisotropic directions of [1 0 0] and [0 0 1]. Thus as for the MACE generally performing from (1 0 0) Si wafer in experiment, the lattice distortion, i.e., defective site beneath the attached Ag will be developed deeply along [1 0 0] direction; it acts as the preferential site triggering and guiding silicon etching to form [1 0 0] SiNW. In other words, the Ag modification likely guides silicon etching along [1 0 0] direction through constantly inducing lattice distortion in the same direction.

### 3.2. $NO_2$ adsorption on Ag@SiNW

The adsorption analysis first requires considering the possible surface adsorption sites on the Ag@SiNW. Previous calculation on $E_{\text{mod}}$ in Table 1 reveals that the modification configuration of $M_5$ with Ag atom modified on the bridge site of both subsurface $Si_2$ atoms is the most energetically favorable. Thus the $M_5$ is specially considered as the basic model of Ag@SiNW to further perform $NO_2$ adsorption. Referring to the related work ever reported [16], $NO_2$ adsorption with N-end coordinated the atom sites of Ag, $Si_1$, $Si_2$, as well as the bridge sites between both of them was modeled and the corresponding adsorption energies were calculated. Besides, the adsorption configuration with O atom of $NO_2$ bonded to the modified Ag site was further constructed and calculated to investigate the adsorption possibility on surface Ag atom integrally. The $NO_2$-adsorbed clean SiNW, denoted as $M_{01}$, was also calculated for comparison. Fig. 3 shows all of the optimized adsorption models and their corresponding adsorption sites (formation bonds).

To evaluate the energy change involved in the gas adsorption and describe the site preference and stability, the adsorption energy of one $NO_2$ molecule onto the SiNW, $E_{\text{ads}}$, was calculated according to the

![](./images/812837939338805249_3.jpg)

Fig. 3. Top views of the optimized adsorption configurations: $M_{01}$ denotes $NO_{2}$ adsorption onto unmodified SiNW; $M_{51}-M_{59}$ are the $NO_{2}$ adsorption on Ag@SiNW of $M_{5}$.

following expression:

$$E_{\text{ads}} = E(\text{Ag@SiNW}) + E(\text{NO}_{2})-E(\text{Ag@SiNW-NO}_{2}) \tag{2}$$

where $E(\text{Ag@SiNW-NO}_{2})$ denotes the total energy of the Ag@SiNW with a single $NO_{2}$ molecule adsorption. $E(\text{Ag@SiNW})$ and $E(\text{NO}_{2})$ represent the energies of the clear SiNW with a Ag atom modification (i.e. model of $M_{5}$) and a free $NO_{2}$ molecule respectively. Similar with calculation on $E_{\text{mod}}$, in the case of $NO_{2}$ adsorption on surface $Si_{1}$ sites (i.e., the models of $M_{51}$, $M_{53}$, $M_{55}$ and $M_{56}$), the values of $E(\text{Ag@SiNW})$ are calculated respectively based on the configurations with pre-removal of the H passivation atoms on the adsorption sites of $Si_{1}$. According to Eq. (2), a positive $E_{\text{ads}}$ value indicates the adsorption reaction is exothermic and thus the adsorption is energetically favorable, whereas a negative value indicates an unstable system.

The calculated $E_{\text{ads}}$, adsorption bond length and charge transfer for each of adsorption models in Fig. 3 are listed in Table 2. It reveals that the $NO_{2}$ molecular prefers to self-adsorb on the Ag@SiNW with N-end orienting to the surface $Si_{1}$ atom or O-end orienting to the modified Ag atom. The multiple sites capable of spontaneous $NO_{2}$ adsorption hint the capability of the Ag modified (1 0 0) SiNW to sense $NO_{2}$ gas with wide concentration range. The formed N-Si$_{1}$ or O-Ag adsorption bond length in $M_{51}$, $M_{53}$, $M_{58}$ and $M_{59}$ are all less than van der Waals radius (3.0-5.0 Å), demonstrating the interactions of the self-adsorbed $NO_{2}$ with Ag@SiNW are remarkably stronger than a typically van der Waals dispersive interaction [25]. The N-Si$_{1}$ configuration, i.e., model $M_{51}$ with N bonding the dangling bond of surface $Si_{1}$ atom, exhibits the highest $E_{\text{ads}}$ (+4.2726 eV), and therefore, should be the most stable adsorption structure for the Ag@SiNW considered in this work. The magnitude of the $E_{\text{ads}}$ value and the relative small N-Si$_{1}$ bond length of 1.916 Å indicate a much stronger interaction between $NO_{2}$ and Ag@ SiNW [26]. In $M_{52}$, $M_{54}$, $M_{55}$, $M_{56}$ and $M_{57}$, the large adsorption bond lengths beyond 3 Å reflect weak physical adsorption occurring in these configurations. In terms of $E_{\text{ads}}$, the adsorption configurations of $M_{52}$, $M_{54}$ and $M_{58}$ are energetically unfavorable.

A special attention should pay to the comparison of N-Si$_{1}$ configurations formed on clean SiNW and on Ag@SiNW, i.e., $M_{01}$ and $M_{51}$. As shown in Table 2, both models, with similar N-Si$_{1}$ bond geometry, show very different $E_{\text{ads}}$ values. The $E_{\text{ads}}$ value of $M_{51}$ is nearly two-fold of that of $M_{01}$, indicating that Ag modification promotes the strong adsorption of $NO_{2}$ on $Si_{1}$ atom sites of SiNW surface. Meanwhile, the introduced Ag atom inspires a spontaneous adsorption of $NO_{2}$ molecule with O-end orienting to it, according to the calculation on $M_{59}$. These theoretical results demonstrate the greater potential of Ag@SiNW in comparison to the unmodified nanowire for $NO_{2}$-sensing application. $NO_{2}$ adsorption on the Ag@SiNW is expected to produce more obvious surface effect, which strongly affects the electronic properties of the nanowire as illustrated in the following. On the other hand, they further clarify the role of Ag modification during gas adsorption and sensing clearly, which will be very helpful for revealing the fundamental theoretical mechanism of Ag-modified SiNWs in $NO_{2}$-sening response enhancement observed experimentally.

### 3.3. DOS analysis

Fig. 4(a) and (b) respectively show the total density of states (DOS) of SiNW (model $M_{0}$) and Ag@SiNW (model $M_{5}$) before and after $NO_{2}$ adsorption, the band structures of both adsorption configuration and the partial DOS (PDOS) of $NO_{2}$ and Ag in corresponding adsorption systems. As displayed in Fig. 4(a), the $NO_{2}$ adsorption on SiNW surface injects a clear deep state at about 0 eV in the band gap. In this case, the molecule-surface interaction can hardly change the intrinsic character of the unmodified SiNW to an obvious degree due to the inactive mid-gap electronic state, that is, the unmodified SiNW is not an ideal material for ultrasensitive detection of $NO_{2}$ gas. As for the $NO_{2}$-Ag@SiNW complex in Fig. 4(b), i.e., $M_{51}$ with N-Si$_{1}$ configuration, we observe that the adsorption of $NO_{2}$ introduce a new electronic state (a shallow state) at valence band edge. This is very different from the case of $NO_{2}$-SiNW adsorption system; it could be sleeked in the special effect of the modified Ag on $NO_{2}$ adsorption and the electronic characteristic of Ag@SiNW. Also as illustrated in Fig. 4(b), the total DOS of clean Ag@ SiNW and the corresponding PDOS of the modified Ag clearly reveal a

<table>
<caption>Table 2<br>Adsorption energies ($E_{\text{ads}}$) and the equilibrium bond length of the formation bonds for different adsorption configurations.</caption>
<thead>
<tr>
<th>Adsorption model</th>
<th>Bond type</th>
<th>Bond length (Å)</th>
<th>$E_{\text{ads}}$ (eV)</th>
</tr>
</thead>
<tbody>
<tr>
<td>$M_{01}$</td>
<td>N-Si$_{1}$</td>
<td>1.861</td>
<td>+2.3606</td>
</tr>
<tr>
<td>$M_{51}$</td>
<td>N-Si$_{1}$</td>
<td>1.916</td>
<td>+4.2726</td>
</tr>
<tr>
<td>$M_{52}$</td>
<td>N-Si$_{2}$</td>
<td>3.058</td>
<td>−1.5228</td>
</tr>
<tr>
<td>$M_{53}$</td>
<td>N-Si$_{1}$</td>
<td>1.944</td>
<td>+4.1182</td>
</tr>
<tr>
<td rowspan="3">$M_{54}$</td>
<td>N-Ag</td>
<td>2.966</td>
<td rowspan="3">−5.3511</td>
</tr>
<tr>
<td>N-Si$_{2}$</td>
<td>3.785</td>
</tr>
<tr>
<td>N-Ag</td>
<td>2.866</td>
</tr>
<tr>
<td rowspan="2">$M_{55}$</td>
<td>N-Si$_{1}$</td>
<td>3.346</td>
<td rowspan="2">+3.5598</td>
</tr>
<tr>
<td>N-Si$_{1}$</td>
<td>3.352</td>
</tr>
<tr>
<td rowspan="2">$M_{56}$</td>
<td>N-Si$_{1}$</td>
<td>2.657</td>
<td rowspan="2">+4.1728</td>
</tr>
<tr>
<td>N-Si$_{2}$</td>
<td>3.694</td>
</tr>
<tr>
<td rowspan="2">$M_{57}$</td>
<td>N-Si$_{2}$</td>
<td>4.634</td>
<td rowspan="2">+2.3025</td>
</tr>
<tr>
<td>N-Si$_{2}$</td>
<td>4.496</td>
</tr>
<tr>
<td>$M_{58}$</td>
<td>N-Ag</td>
<td>2.231</td>
<td>−2.3109</td>
</tr>
<tr>
<td>$M_{59}$</td>
<td>O-Ag</td>
<td>2.254</td>
<td>+1.1409</td>
</tr>
</tbody>
</table>

![](./images/812837939338805249_4.jpg)
![](./images/812837939338805249_5.jpg)

Fig. 4. (a) DOS of $M_0$ and $M_{01}$, PDOS of the adsorbed $NO_2$ in $M_{01}$, and band structure of $M_{01}$; (b) DOS of $M_5$ and $M_{51}$, PDOS of modified Ag in $M_5$ and the adsorbed $NO_2$ in $M_{51}$, and band structure of $M_{51}$.

fact that the Ag introduced on the surface contributes an n-doping effect, consistent with the charge transfer calculation about Ag@SiNW system in Table 1. The Ag modification-resulted DOS modification (i.e. n-doping character) promotes the adsorption of electronegative $NO_2$ on the nanowire surface via taking the electron through the dangling bond of $Si_1$ atom [27]. In other words, the $NO_2$ adsorption on surface $Si_1$ site is activated by the n-doping impurity state of Ag, which introduces an obvious shallow state near valence band as revealed in Fig. 4(b). The formed shallow state, on the one hand, induces a stronger interaction between $NO_2$ and nanowire surface which corresponds to the extremely high $E_{ads}$ value (+4.2726 eV) discussed before, and on the other hand compensates the Ag modification-resulted n-type doping effect and then causes the conductivity variation of the modified SiNW upon $NO_2$ adsorption.

The total DOS for the $NO_2$-Ag@SiNW adsorption system with O-Ag configuration, i.e., model $M_{59}$, is further calculated, as displayed in Fig. 5(a). The clean modified nanowire of $M_5$ is also shown for comparison. Clearly, $NO_2$ adsorption on Ag atom site also changes the total DOS considerably. As observed, three new electronic states appear in the valence band at about $-24$ eV, $-18$ eV and $-12.5$ eV, respectively, inducing a global shift of the electronic states towards high energies. A comparison of the PDOS of the adsorbate $NO_2$ (Fig. 5(b)) with the total DOS reveals that the introduced new electronic states primarily derive from the contributions of the adsorbate $NO_2$. Fig. 5(c)-(e) shows the orbital resolved PDOS of N, $O_a$ and $O_b$ (as marked in $M_{59}$ of Fig. 3) for $M_{59}$; it clearly indicates that the N2p and $O_a$2p of the adsorbed $NO_2$ create p- and n-doping simultaneously in the O-Ag adsorption configuration, via introducing new impurity states at the edges of valance band and conduction band. The significantly modified DOS for $M_{59}$ indicates the strong interaction between $NO_2$ molecule and Ag atom and then the capability of the attached Ag acting as active site for $NO_2$ adsorption, consistent with before mentioned results from adsorption energy calculation.

![](./images/812837939338805249_6.jpg)

Fig. 5. (a) Total DOS of the optimized O-Ag adsorption configuration ($M_{59}$) compared with that with clean surface ($M_5$), (b) PDOS of Ag before and after gas adsorption and adsorbate $NO_2$. (c-f) Orbital resolved PDOS of N, $O_a$ and $O_b$ of the adsorbate $NO_2$. The Fermi level is set to 0 eV.

### 3.4. Charge population analysis

The sensing response of a semiconductor gas sensor is usually characterized by the variation of conductance before and after gas adsorption, while the conductance variation is deemed to result from the charge distribution occurring between semiconductor and the adsorbed gas molecule. Therefore in the theoretical study of a gas sensor, charge population calculation will be highly desired since it can quantify the charge transfer between gas molecule and sensing surface and then provide us an effective understanding and prediction for the trend of conductivity change, i.e., response level, of the focused sensing semiconductor.

Herein we calculate the Mulliken population and corresponding atomic charge change of $NO_2$ molecule and concerning adsorption sites (adatoms of Ag and $Si_1$) in pure SiNW adsorption configuration of N-$Si_1$ ($M_{01}$) and both of energetically favorable Ag@SiNW adsorption systems of N-$Si_1$ ($M_{51}$) and O-Ag ($M_{59}$), and the detailed results for charge transfer are listed in Table 3. It can be seen that for every adsorption configuration, the adsorbed $NO_2$ serves as a charge acceptor to withdraw electrons from the nanowire surface. The whole $NO_2$ molecule

**Table 3**
Charge change ($\Delta$q) of NO₂ molecule and concerning adsorption sites of Ag and surface Si₁ atom in pure SiNW adsorption configuration (M₀₁) and both of Ag modified adsorption systems of N-Si₁ (M₅₁) and O-Ag (M₅₉) based on Mulliken population calculation. The negative value represents the loss of electrons while the positive value means the electrons received. Values are given with unit (e).

| Model | Formation bond | Adsorption site |          |          |          |          | $\Delta$q_NO₂ |
|-------|----------------|-----------------|----------|----------|----------|----------|---------------|
|       |                | Ag              | Si₁      | N        | Oₐ       | Oᵦ       |               |
| M₀₁   | N-Si₁          | --              | $-$0.33  | +0.30    | +0.15    | +0.15    | +0.60         |
| M₅₁   | N-Si₁          | $-$0.17         | $-$0.17  | +0.29    | +0.10    | +0.18    | +0.57         |
| M₅₉   | O-Ag           | $-$0.07         | $-$0.55  | +0.52    | +0.01    | +0.73    | +1.26         |

captures 0.57–1.26 e after adsorption on nanowire surface depending on different adsorption configurations, thus causing change of carrier concentration in nanowire. In the case of p-type SiNW, the NO₂ adsorption will cause a increased conductivity due to the decreased concentration of electron (i.e., increased hole concentration). The charge transfer behavior calculated here correlates well with the experimentally observed decrease in resistance of p-SiNWs and Ag modified p-SiNWs sensors upon exposure to NO₂ gas [28,29]. NO₂ adsorption on the modified Ag atom of Ag@SiNW induces the most significant electron transfer. As shown in Table 3, there are 1.26 e captured by the adsorbed NO₂ molecule in M₅₉, which is more than two times as much as that occurring in M₀₁ (+0.60 e). The relative larger magnitude of electron transfer in M₅₉ compared to that in M₀₁ confirms the considerable promotion of Ag modification to NO₂ adsorption and sensing of SiNW. In particular, the high magnitude of electron transfer achieved in the O-Ag configuration reveals the potential of Ag@SiNW for highly sensitive detection of rarefied NO₂ detection, which have confirmed by previous experimental investigation [15].

When NO₂ molecule is adsorbed on the surface Si₁ atom of Ag@SiNW in M₅₁, the electron number captured by gas (+0.57 e) is close to that in the unmodified configuration of M₀₁. From view point of electron transfer, it is inferred theoretically that the enhanced response for Ag@SiNWs sensor achieved in experiments is mainly attributed to the adsorption of NO₂ gas on the modified Ag particles and following interaction with the surface. Nevertheless, in the case of M₅₁, the charge population calculation clarifies an important issue that the modified Ag on the Ag@SiNW promotes the adsorption of NO₂ on Si₁ atom. As displayed in Table 3, the modified Ag atom contributes 0.17 e during NO₂ adsorption on surface Si₁ atom. It means that the Ag atom acts as an electron donor facilitating the flow of electron from surface to the adsorbed NO₂ molecular, as illustrated in Fig. 6. That is, Ag modification activates the surface Si atom and promotes the adsorption of Si surface to NO₂ gas, as evidence by the highest $E_{\text{ads}}$ value of M₅₁ in previous Table 2.

Above results from the charge population analysis are consistent to that from DOS calculations. To sum up, the modified Ag atom serves as highly active site motivating strong adsorption of NO₂ on it, which for the most part contributes the response enhancement of the sensitive Ag@SiNW; meanwhile the Ag modification further promotes the adsorption of NO₂ on surface Si atom by denoting electrons into surface. These theoretical results demonstrate the potential and effectiveness of Ag modification on NO₂ response enhancement of SiNW-based gas sensor, as well as the underlying modification/enhancement mechanism.

To achieve much deeper insight into the sensing mechanism of Ag@SiNW upon NO₂ exposure at atomic level, the possible reaction occurring on NO₂ molecular during surface adsorption is further explored based on the calculations of geometry configuration and charge density difference for the adsorbate. As the charge population calculation demonstrated, NO₂ adsorption with O-Ag configuration (M₅₉) is deduced to exhibit the main contribution to the response enhancement of Ag@SiNW due to much larger electron transfer occurring. So it will be meaningful to investigate the state of NO₂ after adsorption on the modified Ag atom. Fig. 7(a) and (b-c) respectively presents the side view for local adsorption configuration of M₅₉ and the corresponding charge density difference plots. As shown in Fig. 7(a), after adsorption, the symmetric configuration of NO₂ molecule is distorted obviously. The bond length of 1.229 Å for the N-Oₐ is similar to the N-O bond length of 1.196 Å in the isolated NO molecule as we calculated, while the N-Oᵦ bond is stretched from 1.231 Å (in free NO₂ molecule) to 2.567 Å, hinting that the N-Oᵦ bond is broken. These calculated geometrical data indicate that the adsorbed NO₂ molecule on Ag atom site is dissociated to form NO. Further considering the calculated charge change in Table 3, the Oᵦ in the adsorbed NO₂ captures 0.73 e, indicating a reduction state (i.e. in the form of O⁻). The charge density difference for the adsorbed NO₂ in Fig. 7(b) clearly shows the covalent bond feature of N-Oₐ, as well as the high charge accumulation around Oᵦ, further confirming the formation of NO and O⁻. Thus, the possible reaction occurring for NO₂ after adsorption on the modified Ag atom site can be described as:

$$\text{NO}_2(\text{ads}) + \text{e}^- \rightarrow \text{NO} + \text{O}^-(\text{ads}) \tag{3}$$

![](./images/812837939338805249_7.jpg)

Fig. 6. Charge transfer occurring between the surface and adsorbed NO₂: (upper) M₀₁, (bottom) M₅₁.

The adsorption reaction extracts electrons from the surface of Ag@SiNW, causing a change of carrier concentration and a tuned electronic structure thus to produce sensing response. Fig. 7(c) illustrates the charge density difference of Oᵦ, Ag and Si₁ atoms of M₅₉. Obvious charge accumulation and the short distance of 1.691 Å between Oᵦ and the surface Si₁ atom demonstrate a strong interaction existing between the two atoms. Therefore, the dissociated O⁻ in Eq. (3) is analyzed to be further chemisorbed on the surface Si₁ atom site of SiNW. In such a situation, the re-calculated DOS figure (see Fig. S1 in the Supplementary Material) for the M₅₉ configuration of Ag@SiNW with single Oᵦ attachment exhibits a similar feature that the NO₂ adsorption compensates the pre-existing n-type doping from Ag impurity. During sensing for a real gas sensor, this kind of attached O⁻ ions is capable of chemisorption and reaction of other NO₂ molecules on SiNW surface with formation of NO₃⁻ anions [30], inducing much larger variation in carrier concentration and then a more obvious enhancement in sensing response for Ag@SiNW.

The charge density difference plot of Fig. 7(c) is also helpful for us to understand the role of the modified Ag atom during NO₂ adsorption and dissociation. From the figure, the Oᵦ in the adsorbed NO₂ molecule interacts quite weakly to the modified Ag atom. As observed, there is no charge accumulation between the far separated atoms of Oᵦ and Ag

![](./images/812837939338805249_8.jpg)

Fig. 7. (a) Side-view for local adsorption configuration of $M_{59}$ (with some H atoms on the surface removed for clear observation); (b) and (c) corresponding charge density difference plots.

$(2.254\mathring{A})$. It indicates that the state of the Ag atom in O-Ag adsorption system is almost invariable, in line with the calculated Mulliken population result which reveals a very small charge transfer occurring on Ag atom $(-0.07$ e) after $NO_{2}$ adsorption. These results clarify the role of the modified Ag serving as a catalyst to motivate $NO_{2}$ adsorption on the site and then promote the following dissociation of the adsorbed $NO_{2}$ molecule to form $NO$ and $O^{-}$. The produced $O^{-}$ ion is further chemisorbed on the surface of SiNW with $O_{b}-Si_{1}$ formation as revealed by Fig. 7(c). Thus, the adsorption and reaction process of $NO_{2}$ on the Ag@SiNW clarified here indeed theoretically demonstrates the nature of so-called "spillover effect", which has been suggested to explain the enhanced sensing response of noble metal nanoparticles-modified gas sensor in experiment [31], based on the DFT calculations at atomic level.

## 4. Conclusions
DFT calculations were employed on Ag@SiNW and its $NO_{2}$ adsorption configurations to explore the sensing mechanism of Ag-modified SiNW to $NO_{2}$ gas, especially the theoretical mechanism of Ag modification for sensing response enhancement. Based on the geometry calculation for Ag modified SiNW, a new theoretical mechanism for MACE, i.e., defect-induced preferential etching, was first demonstrated. That is, the Ag modification guides a preferential etching of silicon along [1 0 0] direction through constantly inducing lattice distortion in the same direction. Spontaneous adsorptions of $NO_{2}$ on surface Si site and on the modified Ag atom tune the electronic structure of Ag@SiNW considerably. The adsorption on Ag atom is found to make the main contribution to response enhancement of the modified nanowire due to the most charge transfer (1.27 e) occurring in comparison to the case on Si site adsorption. On the other hand, the modified Ag as a donor creates an n-doping state, facilitating the $NO_{2}$ adsorption on the Si site. In terms of $NO_{2}$ adsorption on Ag site, the Ag atom serves as a role of catalyst to motivate the dissociation of the adsorbed $NO_{2}$ forming $NO$ and $O^{-}$ according to the charge density difference calculation. This reaction induces carrier transfer to produce sensing response. The calculations further clarify a spillover effect of $O^{-}$ occurs subsequently after $NO_{2}$ dissociation.

## Acknowledgements
This work was financially supported by the National Natural Science Foundation of China (Nos. 61574100, 61274074).

## Appendix A. Supplementary material
Supplementary data to this article can be found online at https://doi.org/10.1016/j.apsusc.2018.10.147.

## References
[1] Z. Yang, Z. Liu, J. Sheng, W. Guo, Y. Zeng, P. Gao, J. Ye, Opto-electric investigation for Si/organic heterojunction single-nanowire solar cells, Sci. Rep. 7 (2017) 14575.
[2] W. Li, Z. Guan, Y. Gao, J. Ji, Simple fabrication of Si/ZnO core/shell nanowire arrays for photoelectrochemical, Chem. Phys. Lett. 688 (2017) 79-83.
[3] A.I. Nusir, S.J. Bauman, M.S. Marie, J.B. Herzog, M.O. Manasreh, Silicon nanowires to enhance the performance of self-powered near-infrared photodetectors with asymmetrical Schottky contacts, Appl. Phys. Lett. 111 (2017) 171103.
[4] R. Liu, J. Wang, T. Sun, M. Wang, C. Wu, H. Zou, T. Song, X. Zhang, S.T. Lee, Z.L. Wang, B. Sun, Silicon nanowire/polymer hybrid solar cell-supercapacitor: a self-charging power unit with a total efficiency of 10.5%, Nano Lett. 17 (2017) 4240-4247.
[5] F. Shen, J. Wang, Z. Xu, Y. Wu, Q. Chen, X. Li, X. Jie, L. Li, M. Yao, X. Guo, T. Zhu, Rapid flu diagnosis using silicon nanowire sensor, Nano Lett. 12 (2012) 3722-3730.
[6] A. Gao, X. Yang, J. Tong, L. Zhou, Y. Wang, J. Zhao, H. Mao, T. Li, Multiplexed detection of lung cancer biomarkers in patients serum with CMOS-compatible silicon nanowire arrays, Biosensors Bioelectron. 91 (2017) 482-488.
[7] X. Chen, C.K.Y. Wong, C.A. Yuan, G. Zhang, Nanowire-Based Gas Sensors. Sens. Actuators B 177 (2013) 178-195.
[8] B.R. Huang, Y.K. Yang, H.L. Cheng, Rice-straw-like structure of silicon nanowire arrays for a hydrogen gas sensor, Nanotechnology 24 (2013) 475502.
[9] D. Liu, L. Lin, Q. Chen, H. Zhou, J. Wu, Low power consumption gas sensor created from silicon nanowires/TiO₂ core - shell heterojunctions, ACS Sens. 2 (2017) 1491-1497.
[10] A. Miranda, F. de Santiago, L.A. Perez, M. Cruz-Irisson, Silicon nanowires as potential gas sensors: a density functional study, Sens. Actuators B 242 (2017) 1246-1250.
[11] D. Zhang, Z. Liu, C. Liu, T. Tang, X. Liu, S. Han, B. Lei, C. Zhou, Detection of NO₂ down to ppb levels using individual and multiple In₂O₃ nanowire devices, Nano Lett. 4 (2012) 1919-1924.
[12] H.J. In, C.R. Field, P.E. Pehrsson, Periodically porous top electrodes on vertical nanowire arrays for highly sensitive gas detection, Nanotechnology 22 (2011) 355501 1-5.
[13] J.S. Noh, H. Kim, B.S. Kim, E. Lee, H.H. Cho, W. Lee, High-performance vertical hydrogen sensors using Pd-coated rough Si nanowires, J. Mater. Chem. 21 (2011) 15935-15939.
[14] L.B. Ahmed, S. Naama, A. Keffous, A. Hassein-Bey, T. Hadjersi, H₂ sensing properties of modified silicon nanowires, Prog. Nat. Sci. 25 (2015) 101-110.
[15] Y. Qin, D. Liu, Z. Wang, Y. Jiang, Ag nanoparticles-functionalized rough silicon nanowires array and its unique response characteristics to ultrararefied NO₂, Sens. Actuators B 258 (2018) 730-738.
[16] A. Miranda-Duran, X. Cartoxixa, M.C. Irisson, R. Rurali, Molecular doping and subsurface dopant reactivation in si nanowires, Nano Lett. 10 (2010) 3590.
[17] A. Antidormi, M. Graziano, G. Piccinini, L. Boarino, R. Rurali, First-principles calculations of SO₂ sensing with Si nanowires, Eur. Phys. J. B 89 (2016) 275.
[18] D.D.D. Ma, C.S. Lee, F.C.K. Au, S.Y. Tong, S.T. Lee, Small-diameter silicon nanowire surfaces, Science 299 (2003) 1874-1877.
[19] J.X. Cao, X.G. Gong, J.X. Zhong, R.Q. Wu, Sharp corners in the cross section of ultrathin Si nanowires, Phys. Rev. Lett. 97 (13) (2006) 136105.
[20] A. Miranda, X. Cartoixa, E. Canadell, R. Rurali, NH₃ molecular doping of silicon nanowires grown along the [112], [110], [001], and [111] orientations, Nanoscale Res. Lett. 7 (2012) 308.

[21] R. Rurali, M. Palummo, X. Cartoixà, Convergence study of neutral and charged defect formation energies in Si nanowires, Phys. Rev. B 81 (2010) 235304.

[22] Z. Huang, N. Geyer, P. Werner, J. de Boor, U. Gosele, Metal-assisted chemical etching of silicon: a review, Adv. Mater. 23 (2011) 285-308.

[23] A.G. Nassiopoulou, V. Gianneta, C. Katsogridakis, Si nanowires by a single-step metal-assisted chemical etching process on lithographically defined areas: forma- tion kinetics, Nanoscale Res. Lett. 6 (2011) 597.

[24] M.O. Williams, D. Hiller, T. Bergfeldt, M. Zacharias, How the oxidation stability of metal catalysts defines the metal assisted chemical etching of silicon, J. Phys. Chem. C 121 (2017) 9296-9299.

[25] O.F. Sankey, D.J. Niklewski, Ab initio multicenter tight-binding model for mole- cular-dynamics simulations and other applications in covalent systems, Phys. Rev. B: Condens. Matter 40 (1989) 3979.

[26] M.J.S. Spencer, I. Yarovsky, ZnO nanostructures for gas sensing: interaction of $NO_{2}$, NO, O, and N with the ZnO (1 0 1 0) surface, J. Phys. Chem., C 114 (2010) 10881-10893.

[27] E. Garrone, F. Geobaldo, P. Rivolo, G.P. Salvador, L. Pallavidino, L. Boarino, G. Amato, E. Giamello, M. Chiesa, R. Gobetto, P. Ugliengo, Boron passivation and its reactivation in mesoporous silicon: a "chemical" model, Phys. Status Solidi A 202 (2005) 1567-1570.

[28] Y. Qin, Y. Liu, Y. Wang, Aligned array of porous nanowires for gas-sensing appli- cation, ECS J. Solid State Sci. Technol. 5 (7) (2016) P380-P383.

[29] Y. Qin, Y. Wang, Y. Liu, Vertically aligned silicon nanowires with rough surface and its $NO_{2}$ sensing properties, J. Mater. Sci.: Mater. Electron. 27 (2016) 11319-11324.

[30] B. Ruhland, T. Becker, G. Müller, Gas-kinetic interactions of nitrous oxides with $SnO_{2}$ surface, Sens. Actuators B 50 (1998) 85-94.

[31] S. Choi, J. Kim, Y.T. Byun, Highly sensitive and selective $NO_{2}$ detection by Pt na- noparticles-decorated single-walled carbon nanotubes and the underlying sensing mechanism, Sens. Actuators B 238 (2017) 1032-1042.
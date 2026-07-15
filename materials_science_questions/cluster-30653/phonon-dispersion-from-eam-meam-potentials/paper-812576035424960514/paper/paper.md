Eur. Phys. J. Appl. Phys. 91, 31302 (2020)
© EDP Sciences, 2020
https://doi.org/10.1051/epjap/2020200185

**THE EUROPEAN PHYSICAL JOURNAL APPLIED PHYSICS**

Regular Article

# Structure, stability, and surface diffusion of clusters: Pt₄/Cu (110) AND Au₄/Ag (110) surface by molecular dynamics∗

Fouad Eddiai¹,∗, Moloudi Dardouri¹,², Abdessamad Hassani¹, Michael Badawi³, Khalid Sbiaai¹, and Abdellatif Hassnaoui¹

¹ Laboratory LS3M, Sultan Moulay Slimane University of Beni Mellal, Polydisciplinary Faculty, 25000 Khouribga, Morocco
² Laboratory LPMC, Chouaib Doukkali University, El Jadida, Morocco
³ Laboratoire de Physique et Chimie Théoriques, UMR 7019, Université de Lorraine - CNRS, Nancy, France

Received: 15 June 2020 / Received in final form: 14 August 2020 / Accepted: 19 August 2020

**Abstract.** In this work, molecular dynamics simulations have been used to simulate the behavior of tetramer clusters behavior in Pt₄/Cu (110) and Au₄/Ag (110) systems, in the temperature range 300-600 K. All activation barriers and formation energies related to different tetramer shapes (4S, 4L, 4T, 4N and 4l) have been calculated by embedded atom method (EAM) at static regime (0 K). From an energetical point of view, the adatoms tend to diffuse via simple jumps and exchange mechanisms leading to a transition between all forms during tetramer diffusion. Statistical analysis after molecular dynamics simulations confirms that the linear 4l shape is more stable and needs high energy to be disintegrated in both systems. The lifetime study of each shape for different temperatures (from 300 K to 600 K) proves that the 4 l form is more stiff, which is in a good agreement with the formation energy predictions.

## 1 Introduction

The diffusion of adatoms and small aggregates (monomer, dimer, trimer, etc.) on materials surface plays an important role in thin film growth. This phenomenon has a major impact on the design and development of several devices in technological applications such as catalytic converters, integrated circuits,... [1-6]. A better understanding of the surface diffusion of adatoms and small clusters could enhance the material performances by minimizing the presence of defect in such materials. Indeed, to control the growth of thin films, we have to handle all parameters affecting diffusion phenomena such as activation energy, binding energy, adsorption energy and others. For this purpose, it is mandatory to investigate all the phenomena that can occur at atomic level during epitaxial growth. In this context, several investigations have been devoted to follow trajectories of adatoms and small clusters (monomers, dimer, trimer and tetramer) to extract all diffusion mechanisms that could occur under thermal effect [7-11]. Experimentally, several field ion microscopy (FIM) experiments carried on Ir/Ir (111), Pt/Pt (100) and Ir/Ir (100) at low temperatures show a competition between linear geometry and triangular structure. In fact, when temperature increases the triangle trimers are predominant on the Ir (111) surface, however, the linear ones are predominant in the case of both Ir and Pt (100) surfaces [12]. From a theoretical point of view, Acharya et al. demonstrated that in the case of Cuₙ (3 ≤ n ≤ 8) islands on Ni (111) substrate the triangular geometry occupying the available fcc sites on (111) surface is the most stable for temperature ranging from 100 K to 600 K [13]. As we know, molecular dynamics (MD) simulations are well-adapted to study diffusion mechanisms. The MD simulation allows solving time/size scale problems encountered in other methods such as the DFT method. The use of this method is widely spread for different nominal and stepped surfaces (111), (110) and (100) [14-27]. For an isolated adatom diffusion, it has been found that the exchange process is dominant in Pt/ Pt (110) and Ir/ Ir (111) [28]. The coexistence between the two previous mechanisms is observed for example in Ag₂/Cu (110) [29]. In the case of dimers, the diffusion process takes place via the contribution of both adatoms via correlated jumps [30]. In fact, we observe the dissociation/association process where the dimer loses temporary its geometry and forms again. On the other hand, the adatoms forming the dimer could jump simultaneously in the same direction, leading thus to the so-called concerted jump which occurs when the binding energy is strong enough [30]. Such mechanisms are observed in Ag₂/Ag (110) (1 × 1) [30], Pt₂/Pt (110) [31,32], Cu₂/Ag (110) and Ag₂/Au (110) [7]. For non-perfect surfaces as well as for reconstructed surfaces, the dimer diffusion could occur via a spectacular mechanism called leap frog process (LF). This later is observed for Au₂/Au (110) (2 × 1) [7,33,34], Cu₂/Ag (110) (2 × 1), and Ag₂/Ag (110) (2 × 1) [29]. On metallic surfaces, there are not only simple elements (adatoms or

∗ Contribution to the Topical Issue “Advanced Materials for Energy Harvesting, Storage, Sensing and Environmental Engineering (ICOME 2019)”, edited by Mohammed El Ganaoui, Mohamed El Jouad, Rachid Bennacer, Jean-Michel Nunzi.

∗ e-mail: f.eddiai.fpk@gmail.com

31302-p1

dimers) but also more complex clusters in terms of either the number of atoms or their forms. Imran et al. [8] indicated that at 300 K the diffusion of small clusters can happen by jumping, sliding or shearing movements; whereas for large clusters (hexamer and more), diffusion is neglected. Several theoretical and experimental studies concerning the diffusion of clusters have been made showing that, for (Cu,Zr)/Ag (111) systems, small adatom groups have a higher probability to perform the exchange process due to their low connection to larger groups of adatoms [8]. Therefore, the dimer carries out an exchange process at 500 K as well as at 700 K. At high temperatures, one can observe a concerted exchange where the two adatoms of the same dimer perform exchange processes, simultaneously [13,35]. On the other hand, the tetramer and larger aggregates show exchange processes only at 700 K. Castellani and Légaré, argued that when trimers or tetramers are adsorbed, linear and planar configurations become competitive [36]. Tetrahe- dral tetramers also compete with other aggregates [8,12,37–43]. This leads us to consider in this study a cluster formed by four adatoms called tetramer with different forms or adatoms arrangement in order to broaden our understanding of the diffusion behavior on metallic surfaces. In this way, we will begin the study of the dynamic evolution of the tetramer islands in different forms as a function of the temperature, as well as the determination of the activation energy and the formation of the static state [40–44].

In this manuscript, we study the evolution of island tetramer geometry by MD simulations. The considered systems are Pt₄/Cu (110) and Au₄/Ag (110). Using the Embedded Atom Method (EAM), we calculated all energies needed to understand tetramers diffusion on anisotropic (110) surface. This allowed us determining the most stable tetramer form for both Pt₄ and Au₄ islands.

This paper is structured as follows. In Section 2, we present a brief description of the EAM potential. The simulation results of tetramer behavior are presented in Section 3. Sections 4 and 5 contain discussion and conclusion, respectively.

## 2 Simulation method

In general, The EAM potential is suitable for metal systems with cubic symmetry to study the effects of impurities, surface-related phenomena and defect properties [43,45,46]. The key hypothesis of the EAM method is that all atoms are considered to be embedded in the environment of the other atoms. In the EAM approach, the potential energy of an atom $i$ is the sum of two terms [47–50]:

$$
\mathbf{E}_{tot}=\sum_{i} F_{i}\left(\rho_{h i}\right)+\frac{1}{2} \sum_{i} \sum_{j(\neq i)} \boldsymbol{\varphi}_{i j}\left(r_{i j}\right).
$$

The term $F_{i}$ represents the energy necessary to immerse an atom in the electronic cloud, the term $\rho_{h i}$ is the electron density due to the other atoms of the metal, and the term $\boldsymbol{\varphi}_{i j}(r_{i j})$ designates the pair potential ensuring the repulsion between core electrons, r is the distance between the atom $(i)$ and $(j)$.

![](./images/812576035424960514_1.jpg)

Fig. 1. Substrate formed by 3 zones: free region; isothermal region; fixed region.

![](./images/812576035424960514_2.jpg)

Fig. 2. A schematic picture showing the diffusion processes for an isolated adatom in-channel (1), and cross-channel (2) on a (110) surface.

Molecular dynamics simulation that mimics the temporal evolution of systems [50,51] by computing atomic trajectories, is used to characterize the diffusion processes of a tetramer island for the two systems Au on Ag (110) and Pt on Cu (110).

The substrate (110) surface is prepared by generating 6 layers containing 5400 atoms, in fcc arrangement, at 0 K temperature and then is relaxed for 40 ps under the microcanonical conditions, as shown in Figure 1. The bottom region is fixed to avoid the sample from drifting due to any downward kinetic energy. The isothermal region allows to absorb the kinetic energy of adatoms while the top region is left free to allow clusters to relax.

## 3 Results

### 3.1 Static regime
#### 3.1.1 Activation energy

As a first step, we will check the reliability of our method by calculating the activation energy of diffusion via jump process in the two directions of several isolated adatoms on different metal surfaces (Fig. 2), then we compare our results with those existing in the literature. All potential barriers are calculated by the drag method as described in reference [32]. To perform a simple jump process, the adatom has to overcome a potential barrier.

All results of the activation energy of simple jumps in the case of Cu/Cu (110), Ag/Ag (110), Pt/Pt (110) and Au/Au (110) are summarized in Table 1. We note that our values are in a good agreement with those exiting in the literature and calculated by other methods.

From the obtained results (Tab. 1) [51] it is noted that the activation energy of Ag/Ag system is larger than those

<table>
<caption>Table 1. Summary table of activation energies according to 1 and 2 diffusion direction in the case of homogenous systems.</caption>
<thead>
<tr>
<th>Systems</th>
<th colspan="2">Activation energies $E_a$(eV)<br>In-channel (1)</th>
<th colspan="2">Activation energies $E_a$(eV)<br>Cross-channel (2)</th>
</tr>
<tr>
<th></th>
<th>This work (EAM)</th>
<th>literature</th>
<th>This work (EAM)</th>
<th>literature</th>
</tr>
</thead>
<tbody>
<tr>
<td>Ag/Ag</td>
<td>0.31</td>
<td>0.32$^{\mathrm{a}}$<br>0.28$^{\mathrm{b}}$</td>
<td>0.44</td>
<td>0, 42$^{\mathrm{a}}$<br>0, 81$^{\mathrm{b}}$</td>
</tr>
<tr>
<td>Au/Au</td>
<td>0.25</td>
<td>0.25$^{\mathrm{a}}$<br>0.31$^{\mathrm{b}}$</td>
<td>0.41</td>
<td>0, 40$^{\mathrm{a}}$<br>0, 69$^{\mathrm{b}}$</td>
</tr>
<tr>
<td>Pt/Pt</td>
<td>0.24</td>
<td>0.25$^{\mathrm{a}}$<br>0.25$^{\mathrm{b}}$</td>
<td>0.32</td>
<td>0, 30$^{\mathrm{a}}$</td>
</tr>
<tr>
<td>Cu/Cu</td>
<td>0.23</td>
<td>0.23$^{\mathrm{a}}$<br>0.26$^{\mathrm{b}}$</td>
<td>0.42</td>
<td>0, 43$^{\mathrm{a}}$</td>
</tr>
</tbody>
<tfoot>
<tr>
<td colspan="5">$^{\mathrm{a}}$ From reference [51].<br>$^{\mathrm{b}}$ From reference [52].</td>
</tr>
</tfoot>
</table>

<table>
<caption>Table 2. Activation energy of jump process along direction 1 (along diffusion channel) on (110) surface in the case of heterogenous systems.</caption>
<thead>
<tr>
<th>Systems</th>
<th></th>
<th>Ag/Au</th>
<th>Au/Ag</th>
<th>Pt/Ag</th>
<th>Cu/Pt</th>
<th>Au/Cu</th>
<th>Ag/Cu</th>
<th>Au/Pt</th>
<th>Ag/Pt</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="2">Activation energies $E_a$(eV)</td>
<td>This work (EAM)</td>
<td>0.27</td>
<td>0.25</td>
<td>0.33</td>
<td>0.29</td>
<td>0.20</td>
<td>0.24</td>
<td>0.26</td>
<td>0.23</td>
</tr>
<tr>
<td>Literature</td>
<td>0.27$^{\mathrm{a}}$</td>
<td>0.25$^{\mathrm{a}}$</td>
<td>–</td>
<td>–</td>
<td>0.20$^{\mathrm{a}}$</td>
<td>0.24$^{\mathrm{a}}$</td>
<td>–</td>
<td>–</td>
</tr>
<tr>
<td colspan="10">$^{\mathrm{a}}$ From reference [7].</td>
</tr>
</tbody>
</table>

corresponding to Au/Au, Pt/Pt, Cu/Cu on the (110) surface. This difference is associated with the strong Ag–Ag pair interaction than those of Au–Au, Pt–Pt and Cu–Cu pairs.

The diffusion phenomenon depends on the adatom-substrate environment, such as geometry and substrate nature. We recall that we obtain heterogeneous systems when adatoms and substrates have two different natures. This mixture can influence the behavior of the atoms and consequently modify the activation energy. In Table 2, we report the potential barriers for the simple jump on a (110) surface for several heterogenous systems such as Ag/Au, Au/Ag, Pt/Ag, Cu/Pt, Au/Cu, Ag/Cu, Au/Pt and Ag/Pt.

The first remark is that our values of the jump process for some systems are in a good agreement with those reported in literature. We found also that the activation energy of the Au/Cu system is small compared to the other systems Cu/Pt, Ag/Au and Au/Ag on the (110) surface.

We know that the concerted jump of islands is very costly in energy, and in general, when the adatom number increases, the island motion is neglected. Besides that, the disintegration of islands can be observed. This phenomenon can lead to the island diffusion or coalescence by adatoms reassociation as reported in kMC simulations [53].

In the case of tetramer islands, four main shapes are distinguished depending on their forms: linear geometry (l), shapes S, L and T (Fig. 3). In the same figure we illustrate some possible mechanisms during the diffusion by detachment of an adatom (1) and a dimer (2) of different tetramer geometries on the surface (110). Consequently, a transition between all forms can be observed. In Figure 3, we present several processes of diffusion of an adatom and a dimer from a tetramer island of different shapes namely (4L, 4N, 4T, 4l, 4S) on (110) fcc surfaces. The processes (a), (d), (e), (f) and (h) represent the detachment followed by simple in-channel jump. The process (b) indicates the mechanism of exchange. The processes (c) and (g) represent the cross-channel diffusion. The processes (i), (j), (k) and (l) represent the cascade jump of a dimer along the channel.

Table 3 summarizes the energies of all collected events of adatom (1) and dimer (2) diffusion for both systems Pt/Cu (110) and Au/Ag (110). According to the results obtained by the static simulation, we note that the mechanisms having an activation energy of low values (almost identical) are more probable during the time evolution for the two systems.

On the other hand, these results show that the energy barriers of the Au/Ag system are higher than that of Pt/Cu which is in a good agreement with previous findings in literature (see Tabs. 1 and 3) [7,50].

### 3.1.2 Formation energy

In this part, we are interested in calculating formation energies for the different possible forms of the tetramer cluster [36,37,54], such as 4s, 4N, 4T, 4L and 4l (Fig. 5) for both systems Pt₄/Cu (110) and Au₄/Ag (110) in the static regime (0 K).

From the results obtained for the two systems Pt₄/Cu (110) and Au₄/Ag (110) (Tab. 4), we note that the linear form 4l has the highest formation energies for both systems

![](./images/812576035424960514_3.jpg)

Fig. 3. Different processes involved in diffusion for adatom and dimer from tetramers with different forms on the (110) surface. (a), (b), (c), (d), (e), (f), (g) and (h) present some possible ways of adatom diffusion processes while (i), (j), (k) and (l) show dimer jumps. (1) and (2) stand for the diffusion of an adatom and dimer respectively.

<table>
<caption>Table 3. Static activation energies of jump and exchange mechanisms for Au and Pt adatom, dimer on a flat Ag (110) and Cu (110) surfaces respectively.</caption>
<thead>
<tr>
<th>Processes</th>
<th colspan="4">Activation energies $E_{a}$(eV)</th>
</tr>
<tr>
<th></th>
<th colspan="2">Pt/Cu (110)</th>
<th colspan="2">Au/Ag (110)</th>
</tr>
<tr>
<th></th>
<th>This work (EAM)</th>
<th>literature</th>
<th>This work (EAM)</th>
<th>literature</th>
</tr>
</thead>
<tbody>
<tr>
<td>$1(a)$</td>
<td>0.25</td>
<td>–</td>
<td>0.28</td>
<td>0.27ª</td>
</tr>
<tr>
<td>$1(b)$</td>
<td>0.16</td>
<td>–</td>
<td>0.18</td>
<td>–</td>
</tr>
<tr>
<td>$1(c)$</td>
<td>0.31</td>
<td>–</td>
<td>0.34</td>
<td>–</td>
</tr>
<tr>
<td>$1(d)$</td>
<td>0.23</td>
<td>–</td>
<td>0.31</td>
<td>–</td>
</tr>
<tr>
<td>$1(e)$</td>
<td>0.22</td>
<td>–</td>
<td>0.27</td>
<td>–</td>
</tr>
<tr>
<td>$1(f)$</td>
<td>0.25</td>
<td>–</td>
<td>0.30</td>
<td>–</td>
</tr>
<tr>
<td>$1(g)$</td>
<td>0.56</td>
<td>–</td>
<td>0.61</td>
<td>–</td>
</tr>
<tr>
<td>$1(h)$</td>
<td>0.52</td>
<td>–</td>
<td>0.54</td>
<td>0.55ª</td>
</tr>
<tr>
<td>$2(i)$</td>
<td>0.28</td>
<td>–</td>
<td>0.32</td>
<td>0.31ª</td>
</tr>
<tr>
<td>$2(j)$</td>
<td>0.28</td>
<td>–</td>
<td>0.34</td>
<td>–</td>
</tr>
<tr>
<td>$2(k)$</td>
<td>0.53</td>
<td>–</td>
<td>0.60</td>
<td>–</td>
</tr>
<tr>
<td>$2(l)$</td>
<td>0.48</td>
<td>–</td>
<td>0.51</td>
<td>–</td>
</tr>
</tbody>
<tfoot>
<tr>
<td colspan="5">ª From reference [45].</td>
</tr>
</tfoot>
</table>

<table>
<caption>Table 4. Summary table of island formation energies (tetramer) for both systems $\text{Pt}_{4}/\text{Cu}$ (110) and $\text{Au}_{4}/\text{Ag}$ (110) in (eV).</caption>
<thead>
<tr>
<th>Formation energy (eV)</th>
<th>$S$</th>
<th>$N$</th>
<th>$T$</th>
<th>$L$</th>
<th>$l$</th>
</tr>
</thead>
<tbody>
<tr>
<td>$\text{Pt}_{4}/\text{Cu}$ (110)</td>
<td>1.09</td>
<td>0.90</td>
<td>0.95</td>
<td>0.94</td>
<td>1.28</td>
</tr>
<tr>
<td>$\text{Au}_{4}/\text{Ag}$ (110)</td>
<td>0.63</td>
<td>0.62</td>
<td>0.64</td>
<td>0.59</td>
<td>0.86</td>
</tr>
</tbody>
</table>

$(1.28/0.86\,\text{eV})$, then the $4S$ form with $(1.09/0.63\,\text{eV})$, then $4N$, $4T$ and $4L$ forms with lower values.

### 3.2 Molecular dynamics simulation results

In this part we will focus on the most stable island forms (tetramers), and investigate their diffusion at different temperatures (300, 400, 500 and 600 K) for both systems ($\text{Au}_4/\text{Ag}$ (110) and $\text{Pt}_4/\text{Cu}$ (110)) using molecular dynamics simulation. After meticulous checking of all results of our simulation we have selected the remarkable cases which are quoted in the following.

Figure 4 presents the dynamic evolution of the geometry of the T-shape tetramer $\text{Pt}_{4\text{T}}/\text{Cu}$ (110) at 400 K. This figure shows that the island 4T (Fig. 5a) transforms to the linear form 4l (Fig. 5c) through the formation of an intermediate state 4T (Fig. 5b) via a single jump in the frequent channel.

![](./images/812576035424960514_4.jpg)

Fig. 4. Schema of different tetramer forms on the (110) surface: (a) a compact structure in square shape: $\boldsymbol{4S}$ (b) two dimer in parallel: $\boldsymbol{4N}$, (c) an additional atom attached to the central atom of the three-atom chain: $\boldsymbol{4T}$, (d) an additional atom attached to the final atom of the three-atom chain: $\boldsymbol{4L}$, (e) a linear chain oriented in the [110] direction: $\boldsymbol{4l}$.

![](./images/812576035424960514_5.jpg)

Fig. 5. Diffusion of T-shape tetramer $\text{Pt}_{4\text{T}}/\text{Cu}(110)$ at 400 K.

Figure 6 presents the dynamic evolution of the N-shape geometry of the tetramer $\text{Pt}_{4\text{N}}/\text{Cu}$ (110) at 500 K, the island 4N (a) undergoes several jumps of its adatoms leading to its dissociation (Fig. 6b). After an exchange process of the island adatoms with those of the substrate, we observe a 4T island formed by Cu atoms of the substrate while Pt atoms became part of the surface (Fig. 6c). Finally, by a double mechanism of a simple in-channel jump followed by a cross-channel exchange the linear geometry 4l is formed by Cu adatoms (Fig. 6d).

![](./images/812576035424960514_6.jpg)

Fig. 6. The mechanism of diffusion of the N-shape tetramer $\text{Pt}_{4\text{T}}/\text{Cu}(110)$ at 500 K.

Figure 7 presents the dynamic evolution of the geometry of the tetramer $\text{Pt}_{4\text{l}}/\text{Cu}$ (110) at 500 K, where we see how the geometry 4l (Fig. 7a) undergoes several exchange processes in a cascade way (Fig. 7b) and (Fig. 7c) with a final linear $4l$ shape formed by Cu substrate atoms as shown in Figure 7d.

![](./images/812576035424960514_7.jpg)

Fig. 7. Diffusion mechanism of a linear tetramer $\text{Pt}_{4\text{T}}/\text{Cu}(110)$ at 500 K.

Figure 8 shows the dynamic evolution of the geometry of the tetramer $\text{Pt}_{4\text{S}}/\text{Cu}$ (110) at 600 K. The 4S island (Fig. 8a) undergoes a dissociation accompanied by exchange mechanisms to form a heterogeneous 4T island (Fig. 8b) then an island 4L (Fig. 8c) by a single jump along the channel, ultimately an exchange mechanism to form the heterogeneous linear geometry 4l (Fig. 8d).

Figure 9 presents the dynamic evolution of the tetramer geometry $\text{Au}_{4\text{L}}/\text{Ag}$ (110) at 600 K, the structure of the 4S

![](./images/812576035424960514_8.jpg)

Fig. 8. Mechanism of diffusion of a square tetramer $\text{Pt}_{4\text{S}}/\text{Cu}\,(110)$ at 600 K.

![](./images/812576035424960514_9.jpg)

Fig. 9. Mechanism of diffusion of L-shaped tetramer $\text{Au}_{4\text{L}}/\text{Ag}\,(110)$ at 600 K.

island undergoes a simple jump of an adatom (Fig. 9a) according to the channel then makes an exchange mechanism (Fig. 9b) to finally form a heterogeneous linear geometry (Fig. 9c).

## 4 Discussion

In the low-temperature regime (at 300 K) it is found that for the different forms of tetramers ($\boldsymbol{S}$, $\boldsymbol{L}$, $\boldsymbol{N}$, $\boldsymbol{T}$, $\boldsymbol{l}$) of systems $\text{Pt}_{4}/\text{Cu}\,(110)$ and $\text{Au}_{4}/\text{Ag}\,(110)$ remain unchanged in time due to low thermal activation. As the temperature is increased to 400 K, we notice that the forms $\text{Pt}_{4\text{L}}/\text{Cu}\,(110)$, $\text{Pt}_{4\text{N}}/\text{Cu}\,(110)$ and $\text{Pt}_{4\text{T}}/\text{Cu}\,(110)$ undergo a partial dissociation of islands and then arrive at a more stable linear form either homogeneous or heterogeneous (see Fig. 5) by a break-stick mechanism [27]. But the forms (4S,4l) remain unchanged in both systems, this event means on the one hand that the thermal energy received by the system is insufficient to produce a displacement of the adatoms and on the other hand the energy of formation of the tetramers (S, l) is higher than those of tetramers (L, N, T). For a temperature of 500 K the form N undergoes a diffusion by the exchange mechanism to arrive at the linear form consisting of adatoms from the substrate after a duration of 70 ps, this transformation passes through intermediate forms L and T (see Fig. 6). The adsorbent $\boldsymbol{l}$-form at a temperature of 500 K is converted to a substrate linear form $\boldsymbol{l}$ through a cascade exchange mechanism within a time range of [170 ps–185 ps] (see Fig. 7), this process leads to a linear form consisting of substrate atoms while adsorbate adatoms become a part of the substrate. On the other hand, $\text{Pt}_{4\text{S}}/\text{Cu}\,(110)$, $\text{Pt}_{4\text{N}}/\text{Cu}\,(110)$ and $\text{Pt}_{4\text{T}}/\text{Cu}\,(110)$ form a linear shape of a trimer or a tetramer passing through heterogeneous intermediate forms which are more frequent. The latter is argued by the values of the formation energies which are much more important for the tetramers (S, l) with the other metastable tetramer structures (L, N, T).

![](./images/812576035424960514_10.jpg)

Fig. 10. Lifetime of each shape as function of temperature for $\text{Au}_{4}/\text{Ag}\,(110)$.

The energy differences evaluated respectively for the system $\text{Pt}_{4}/\text{Cu}\,(110)$ $\boldsymbol{0.90}$, $\boldsymbol{0.95}$, $\boldsymbol{0.94}$, $\boldsymbol{1.09}$, $\boldsymbol{1.28}$ (eV), and for the system $\text{Au}_{4}/\text{Ag}\,(110)$ $\boldsymbol{0.62}$, $\boldsymbol{0.64}$, $\boldsymbol{0.59}$, $\boldsymbol{0.63}$, $\boldsymbol{0.86}$ (eV) correspond to the following tetramer shapes 4S, 4N, 4T, 4L and 4l. At 600 K for both systems the islands of forms l, N and T are dissociated as dimers, but the L and S forms are transformed into the heterogeneous linear form (see Figs. 8 and 9). These results are in good agreement with experimental and simulations results existing in literature [40,54,55].

To show the tendency of dissociation of each cluster we plotted in Figures 10 and 11 their lifetime as a function of temperature obtained by MD simulations. The results show that, the stable shapes (S and $l$) performed the longest lifetime for all temperatures ranging from 300 K to 600 K. However, the instable geometries (N, T and L) showed very short lifetimes compared to the S and $l$ shapes. We note that the coincidence of the three lifetime profiles (4L, 4N

25. Y. Han, C.R. Stoldt, P.A. Thiel, J.W. Evans, J. Phys. Chem. C 120, 21617 (2016)

26. A. Hassani, A. Makan, K. Sbiaai, A. Tabyaoui, A. Hasnaoui, Appl. Surf. Sci. 349, 785 (2015)

27. E.F. Kherbouche, R. Annou, Comput. Mater. Sci. 110, 353 (2015)

28. S.C. Wang, G. Ehrlich, Surf. Sci. 239, 301 (1990)

29. K. Sbiaai, A. Eddiai, Y. Boughaleb, A. Hajjaji, M. Mazroui, A. Kara, Opt. Mater. (Amst). 36, 42 (2014)

30. K. Sbiaai et al., Int. Conf. Transp. Opt. Netw. 110, 1 (2012)

31. I. Matrane, E. Elkoraychy, K. Sbiaai, M. Mazroui, Y. Boughaleb, Phys. Status Solidi Basic Res. 253, 875 (2016)

32. F. Montalenti, R. Ferrando, Phys. Rev. B 59, 5881 (1999)

33. D. Teng, D.S. Sholl, Surf. Sci. 626, 6 (2014)

34. L.F. Fortunato, C.E. Zubieta, S.A. Fuente, P.G. Belelli, R. M. Ferullo, Appl. Surf. Sci. 387, 894 (2016)

35. H. Yang, Q. Sun, Z. Zhang, Y. Jia, Phys. Rev. B 76, 1 (2007)

36. F. Eddiai, M. Dardouri, A. Hassani, H. El Azrak, K. Sbiaai, A. Hassnaoui, Sensor Lett. 16, 386 (2018)

37. G.L. Kellogg, Appl. Surf. Sci. 67, 134 (1993)

38. H. Oughaddou et al., Surf. Sci. 602, 506 (2008)

39. F. Shi, Y. Shim, J.G. Amar, Phys. Rev. E 76, 1 (2007)

40. F. Graner, J.A. Glazier, Phys. Rev. Lett. 69, 2013 (1992)

41. A. Voter, Model. Opt. Thin Films 821, 214 (1987)

42. H. Hill, Phi Delta Kappan 90, 470 (2009)

43. L. Liu et al., Appl. Surf. Sci. 290, 405 (2014)

44. M. Mašín, I. Vattulainen, T. Ala-Nissila, Z. Chvoj, Surf. Sci. 566-568, 143 (2004)

45. J. Ledieu, É. Gaudry, V. FournÉe, Sci. Technol. Adv. Mater. 15 (2014)

46. H. Häkkinen, M. Manninen, Phys. Rev. B 46, 1725 (1992)

47. F. Montalenti, R. Ferrando, Phys. Rev. B 59, 5881 (1999)

48. R.A. Johnson, Phys. Rev. B 39, 12554 (1989)

49. S.M. Foiles, M.I. Baskes, M.S. Daw, Phys. Rev. B 33, 7983 (1986)

50. C.L. Liu, J.M. Cohen, J.B. Adams, A.F. Voter, Surf. Sci. 253, 334 (1991)

51. C.L. Liu, J.M. Cohen, J.B. Adams, A.F. Voter, Surf. Sci. 253, 334 (1991)

52. U.T. Ndongmouo, F. Hontinfinde, Surf. Sci. 571, 89 (2004)

53. M. Dardouri, A. Hassani, A. Hasnoui, Y. Boughaleb, Phys. Status Solidi B 1800404, 1 (2018)

54. T.Y. Fu, T.T. Tsong, Surf. Sci. 482-485, 1249 (2001)

55. T.Y. Fu, Y.J. Hwang, T.T. Tsong, Appl. Surf. Sci. 219, 143 (2003)

<table>
  <tr>
    <td>Cite this article as: Fouad Eddiai, Moloudi Dardouri, Abdessamad Hassani, Michael Badawi, Khalid Sbiaai, Abdellatif Hassnaoui, Structure, stability, and surface diffusion of clusters: Pt₄/Cu (110) AND Au₄/Ag (110) surface by molecular dynamics, Eur. Phys. J. Appl. Phys. 91, 31302 (2020)</td>
  </tr>
</table>
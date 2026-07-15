23 May 2022

# An approach for the pore-centred description of adsorption in hierarchical porous materials

Jack Evans¹

1. University of Adelaide

## Abstract
Analysis of pore size distributions based on crystalline representations of metal-organic frameworks (MOFs) featuring hierarchical pore systems, DUT-32, DUT-75, UMCM-1 and NU-1000, is presented here and leveraged to understand gas adsorption in these unique pore structures. Statistical analysis was used to effectively partition the pore space into distinct regions labelled by the pore size. This pore description was used to discover how adsorbates are located, with respect to the different pores, during simulations of argon adsorption at 87K. To further examine adsorption behaviour, a method of clustering the pore environments to locate the centre of the pore was developed. These pore centres were employed to observe the distribution of gas within the pore, describing adsorbate positions during filling events from the unique perspective of the pore centre. The methods presented here provide unsurpassed information about pore structure and adsorption properties that cannot be obtained with currently available methods and are now ready to apply to new materials to uncover new adsorption processes.

## Keywords
adsorption, metal-organic framework, pore size distribution

---
Posted on 23 May 2022 — CC-BY 4.0 — This is a preprint and has not been peer reviewed. Data may be preliminary. — https://doi.org/10.26434/chemrxiv-2022-ls3rp

# An approach for the pore-centred description of adsorption in hierarchical porous materials

Jack D. Evans

* E-Mail: j.evans@adelaide.edu.au

Analysis of pore size distributions based on crystalline representations of metal-organic frameworks (MOFs) featuring hierarchical pore systems, DUT-32, DUT-75, UMCM-1 and NU-1000, is presented here and leveraged to understand gas adsorption in these unique pore structures. Statistical analysis was used to effectively partition the pore space into distinct regions labelled by the pore size. This pore description was used to discover how adsorbates are located, with respect to the different pores, during simulations of argon adsorption at 87 K. To further examine adsorption behaviour, a method of clustering the pore environments to locate the centre of the pore was developed. These pore centres were employed to observe the distribution of gas within the pore, describing adsorbate positions during filling events from the unique perspective of the pore centre. The methods presented here provide unsurpassed information about pore structure and adsorption properties that cannot be obtained with currently available methods and are now ready to apply to new materials to uncover new adsorption processes.

## 1. Introduction
The ordered arrangement of pores made possible by crystalline framework materials has lead to exciting applications in gas storage, separation and catalysis. $^{1–3}$ In particular, the crystalline engineering of porous materials constantly produces unique pore structures with pore sizes ranging from 2 to $40\ \mathring{A}.^{4}$ The ability to engineer a porous material with a specific pore size is key to meaningful performance in promising applications. $^{5–7}$ However, a single pore environment is limited in application to a narrow regime of size and shape selectivity for guest molecules, often restricting mass transfer. Materials featuring hierarchical porosity can overcome this limitation providing an optimisation pathway for both increased diffusion and confinement, by combining different porosity scales. $^{8}$ For example, fluid catalytic cracking catalysts used in industry commonly employ a hierarchical structure such as a USY zeolite that has mesoporosity mixed with a macroporous matrix. $^{9}$ The advantages of combining several porosity regimes in a single material have been demonstrated in several applications relevant to the fields of catalysis and phase separation, however, aspects of guest behaviour in these porous systems remains uncertain. $^{10}$ Discovering the mechanisms ruling adsorption in hierarchical solids is crucial for the future design of porous materials with optimal properties toward applications. $^{11}$

Metal-organic frameworks (MOFs) are widely recognised as an important class of porous materials, featuring high porosity from well-defined and tailored structures at the atomic level. $^{12}$ Many MOFs demonstrate hierarchical porosity and the sheer structural diversity of this materials class can enable unparalleled performance in adsorption applications. The clearly defined structure of MOFs has lead to unparalleled understanding of pore filling $^{13}$ and other complex adsorption phenomena, such as breathing and negative gas adsorption. $^{14,15}$

Gas adsorption is an essential characterisation tool for porous materials and can be coupled with X-ray diffraction to experimentally probe gas adsorption behaviour on a porous host. $^{16}$ This in situ characterisation is widely employed to monitor the structure transition of flexible MOF crystals during adsorption. $^{17}$ Moreover, by careful analysis, the average location of adsorbates within the pore structure can also be observed.

Cho et al., studied several mesoporous MOFs by employing adsorption measurements paralleled with X-ray crystallography to obtain a detailed picture of adsorbate location during different stages of adsorption for several MOFs. $^{18}$ A similar approach was employed separately by Krause et al. to discover the pore filling mechanism within hierarchical MOFs to discover the adsorbate behaviour before negative gas adsorption. $^{19}$ This work demonstrated that both molecular simulation and X-ray diffraction agreed in the description of pore filling. Recently, Dantas et al. suggested an approach to compartmentalise adsorption isotherms as the sum of isotherms for individual pore compartments. $^{20}$ Molecular simulation can readily predict gas adsorption based on the crystal structure of MOFs. $^{21}$ Neimark and coworkers and also shown how to generate theoretical isotherms corresponding to the individual pore compartments of the MOFs PCN-224 and ZIF-412 using Monte Carlo simulations. $^{22}$ The above studies used visual markers from the crystal structure to identify the pore limits, which may be straightforward for some systems, but this may prove nebulous in porous materials with a complex pore system.

![](./images/1250160250103791623_1.jpg)

Fig. 1: Atomistic structures of DUT-32, DUT-75, UMCM-1, NU-1000, examined in this study. $ZnO_4$-tetrahedra blue; $Cu_2O_8$-paddlewheel dark red; $Zr_6OH_4$ dark green; C gray; O red; N light blue, H white.

$^{a}$Centre for Advanced Nanomaterials and Department of Chemistry, The University of Adelaide, North Terrace, Adelaide, South Australia 5000, Australia

Electronic Supplementary Information (ESI) available: Supplementary figures of the kernel density estimations of pore size distributions and pore-centred description of Ar adsorption on NU-1000.

Preprint | May 22, 2022 | 1-7

Pore size distributions can be computed for a void space within a porous material by geometric and stochastic ray tracing techniques. $^{23-25}$ In particular, an approach employed by the widely used software package Zeo++ describes a pore structure with lower and upper bounds of pore diameters and a pore size distribution histogram. $^{25,26}$ These approaches enable an assessment of pore structure from different perspectives and have been used in both an automated and high-throughput manner. $^{27}$ Researchers used this description to better measure pore spaces, better than one-dimensional numerical descriptors, such as smallest pore diameter.

In this work, statistical analysis is used to extract pore environments from pore size distributions of crystalline representations of MOFs that feature a hierarchical pore system, namely DUT-32$^{28}$, DUT-75$^{29}$, UMCM-1$^{30}$ and NU-1000$^{31}$ (Fig. 1). This analysis effectively partitions the entire pore volume into volume groups labelled with respect to the pore size. The pore descriptions are subsequently used to understand how the different parts of a porous framework are filled during Ar adsorption at 87 K. This is powerful analysis for understanding difficult to measure adsorption events, such as adsorbate-induced deformation, $^{32,33}$ and to ascertain the distinct adsorption steps observed in interesting isotherms. To better understand the behaviour of adsorption, a method to cluster the pore environments with respect to their size and identify the centre of the pore was developed. Finally, the pore centres were used to demonstrate the distribution of gas within the pore to describe adsorbate positions during filling events from the perspective of the centre of the pore.

## 2. Methods and approach

![](./images/1250160250103791623_2.jpg)

Fig. 2: An example of the methodology described in this work as applied to a hypothetical porous material featuring three pore sizes. Probe molecules and pore centres are depicted by spheres and stars, respectively.

The reported crystal structures of the MOFs were used without modification and supercell structures generated such that the minimum cell length was greater than 12 Å. Geometric features for the MOFs were calculated using the Zeo++ code. $^{25,26}$ Pore volumes were computed using probe size 3.4 Å, equivalent to the kinetic diameter of Ar. $^{34}$ Pore size distributions were produced using the pore size distribution method with the "--vpsd" flag in Zeo++. This produces thousands of sampled points throughout the unit cell that define the pore size at that point. The distribution of pore sizes for the sampled points was estimated using kernel density estimation (KDE) employed by statsmodels, $^{35}$ which approximates density with a series of positive functions, $K$ to produce the continuous function $\rho(y)$:

$$
\rho(y)=\sum_{i=1}^{N} K\left(y-x_{i} ; h\right) \tag{1}
$$

In this case, Gaussian kernels where used where each point contributes a Gaussian curve to the total estimate:

$$
K(x ; h) \propto \exp \left(-\frac{x^{2}}{2 h^{2}}\right) \tag{2}
$$

Applying the kernel density approximation required careful choice of $h$, which defines the bandwidth size. The bandwidth acts as a smoothing parameter, controlling the trade-off between bias and variance in the result. The value of $h$ (Table 1) was chosen based on visual analysis and the ability to recreate the shape of the pore distributions (Supplementary Figure 1-4). Materials with a combination of nanopores and mesopores required a large bandwidth to avoid spurious maxima whereas most materials with a tighter range of pore sizes a bandwidth of 1.0 Å is sufficient.

<table>
<caption>Table 1: Values of bandwidth ($h$) used for kernel density approximation.</caption>
<thead>
<tr>
<th>framework</th>
<th>$h$ / Å</th>
</tr>
</thead>
<tbody>
<tr>
<td>DUT-32</td>
<td>2.0</td>
</tr>
<tr>
<td>DUT-75</td>
<td>1.0</td>
</tr>
<tr>
<td>UMCM-1</td>
<td>1.0</td>
</tr>
<tr>
<td>NU-1000</td>
<td>10.0</td>
</tr>
</tbody>
</table>

From the KDE function the local minima and maxima were computed to give the limits and the comparable size for each pore (Fig. 2).

This pore sampling and KDE analysis provides the portioning of space to different pores, however, does not provide local information for each pore, such as the pore centre. To achieve this the sampled points, labelled by size based on KDE, was clustered using the density-based spatial clustering of applications with noise (DBSCAN) approach. $^{36,37}$ DBSCAN was applied using the sci-kit learn implementation. $^{38}$ Clustering samples core points of high density and effectively expands clusters from them and is used for data that contain clusters of similar density. The clustering of sample points provided the number of pores within this size regime in the unit cell. Simply by computing the centre for cluster the coordinates of the pore centres were computed.

Adsorption of Ar on each of the materials was simulated using grand canonical Monte Carlo (GCMC) simulations as employed by the YAFF package (version 1.6.0.post21). $^{39}$ To produce representative isotherms simulations were performed for 75 values of gas pressure and the chemical potential at each temperature and gas pressure was calculated with the Peng–Robinson equation of state. $^{40}$ Monte Carlo steps of insertion, deletion and translation were used in equal probability and $1 \times 10^{7}$ steps were simulated and the final $5 \times 10^{6}$ steps used to compute the average properties. Interactions were treated by the Lenard-Jones potential:

$$
E=4 \epsilon\left(\left(\frac{\sigma}{r}\right)^{12}-\left(\frac{\sigma}{r}\right)^{6}\right) \tag{3}
$$

A long-range cutoff of 12 Å was used and the Lennard-Jones parameters for argon and the framework atoms are detailed in Table 2. They were combined for the atom pairs using arithmetic mixing rules for $\sigma$ and geometric mixing rules for $\epsilon$.

The GCMC simulations produced snapshots every 1000 cycles which were then combined with the geometric descriptions of the pore environment, KDE labelled sampled points and pore centres. The individual pore isotherms were then computed using a closest distance criteria between each Ar atom and the KDE labelled sampled points. Pore-centred radial distributions were calculated based on the distance between the adsorbates and the pore centres.

The python code responsible for the above analyses and the data from the GCMC simulations were deposited on Zenodo. $^{44}$

Preprint | May 22, 2022 | 2

<table>
<caption>Table 2: Values of the Lennard-Jones potential employed in grand canonical Monte Carlo simulations.</caption>
<thead>
<tr>
<th>element</th>
<th>$\sigma$ / $\text{\AA}$</th>
<th>$\epsilon$ $\text{kJ mol}^{-1}$</th>
<th>Ref.</th>
</tr>
</thead>
<tbody>
<tr>
<td>Ar</td>
<td>3.380</td>
<td>1.02978</td>
<td>41</td>
</tr>
<tr>
<td>H</td>
<td>2.846</td>
<td>0.06349</td>
<td>42</td>
</tr>
<tr>
<td>C</td>
<td>3.473</td>
<td>0.3972</td>
<td>42</td>
</tr>
<tr>
<td>N</td>
<td>3.263</td>
<td>0.3233</td>
<td>42</td>
</tr>
<tr>
<td>O</td>
<td>3.033</td>
<td>0.3997</td>
<td>42</td>
</tr>
<tr>
<td>Zr</td>
<td>2.783</td>
<td>0.28820</td>
<td>43</td>
</tr>
<tr>
<td>Cu</td>
<td>3.114</td>
<td>0.02088</td>
<td>43</td>
</tr>
<tr>
<td>Zn</td>
<td>2.462</td>
<td>0.5179</td>
<td>43</td>
</tr>
</tbody>
</table>

## 3. Results and discussion
The MOFs studied in this work have similar geometric features, such as low density and high pore volume (Table 3). To put these values in context, at the time of writing, the MOFs can feature densities as low as $0.124\ \text{g cm}^{-3}$⁴⁵ and pore volumes up to $5.02\ \text{cm}^3\ \text{g}^{-1}$.⁴⁶ For conventional porous materials, such as zeolites, densities of $\approx 1.0\ \text{g cm}^{-3}$ are common.⁴⁷ These MOFs are impressive structures with unique pore volumes and have all been experimentally measured.

<table>
<caption>Table 3: Computed density and textural properties for the materials.</caption>
<thead>
<tr>
<th>framework</th>
<th>density / $\text{g cm}^{-3}$</th>
<th>Ar pore volume / $\text{cm}^3\ \text{g}^{-1}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>DUT-32</td>
<td>0.332</td>
<td>2.19</td>
</tr>
<tr>
<td>DUT-75</td>
<td>0.431</td>
<td>1.40</td>
</tr>
<tr>
<td>UMCM-1</td>
<td>0.390</td>
<td>1.65</td>
</tr>
<tr>
<td>NU-1000</td>
<td>0.472</td>
<td>1.27</td>
</tr>
</tbody>
</table>

The KDE recreates the important features of the pore size distribution as demonstrated in the Supplementary Figure 1-4, which display the pore size distribution histogram and the resulting KDE. Pore variations are reproduced well however for extremely narrow pore distributions this may not be acceptable and a narrower bandwidth value should be chosen. In general, a bandwidth value of around $1.0\ \text{\AA}$ produced a reasonable estimate, however, for NU-1000 this was increased to avoid too much noise. The pore size distributions based on KDEs are displayed in Fig. 3. These distributions clearly describe the key features of the void space found within these MOFs. The broad nature of the pores in DUT-32 can be observed stemming from the cage like structure of this material where as the one-dimensional pores of NU-1000 and UMCM-1 produce narrow peaks.

<table>
<caption>Table 4: An example of a caption to accompany a table</caption>
<thead>
<tr>
<th>framework</th>
<th>p1 / $\text{\AA}$</th>
<th>p2 / $\text{\AA}$</th>
<th>p3 / $\text{\AA}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>DUT-32</td>
<td>14.0</td>
<td>19.4</td>
<td>28.2</td>
</tr>
<tr>
<td>DUT-75</td>
<td>11.4</td>
<td>22.3</td>
<td></td>
</tr>
<tr>
<td>UMCM-1</td>
<td>11.7</td>
<td>14.1</td>
<td>24.0</td>
</tr>
<tr>
<td>NU-1000</td>
<td>7.34</td>
<td>9.22</td>
<td>29.7</td>
</tr>
</tbody>
</table>

Continuous features of the KDE function were analysed to capture the maxima of the peaks and the minima to provide limits to the pore environments. The summary of peak maxima are displayed in Table 4. The pore size distributions highlight the shear size of the pores in these materials and the breadth of pore sizes contained within NU-1000.

The analysis demonstrates the hierarchical nature of pore space for these crystalline materials with three unique pore sizes found within DUT-32, UMCM-1 and NU-1000. It was planned to also include DUT-75 for all aspects of this study, however, based on the pore size distribution only two peaks of pore sizes are observed. DUT-75 features three distinct pore environments²⁹ and there are two pores, which although are different shapes and chemistry, almost identical in size. This prohibits an approach to dissect the pore environments based on size alone. No combination of limits could discern between these pores environments. The case of DUT-75 highlights the challenges that unique pore structures pose and necessitates an entirely different approach to extract the pores in this, and related, materials.

![](./images/1250160250103791623_3.jpg)

Fig. 3: Continuous pore size distributions obtained from kernel density estimate (KDE) with minimum points (black points) separating the different pores in the structures.

The adsorption of Ar on DUT-32, UMCM-1 and NU-1000 was subsequently simulated using the established method of GCMC. The isotherms for each of the materials (Fig. 4) demonstrate steps at different partial pressures corresponding to pore-filling events, common for mesoporous materials.⁴⁸ NU-1000 features a gradual increase in amount adsorbed from 10E-5 to 10E-1 bar before rapidly increasing to saturation. This is very different to UMCM-1 and DUT-32 that both features sharp increases in amount adsorbed in two distinct steps. Generally, it is believed that the steps in isotherms of rigid materials are related to pore filling of different pore sizes.

The statistical analysis applied to the estimations of pore size distributions allows for pore environments to be separated based on the minimum values of this function. Subsequently, the adsorbate location can be identified based on the label of the pore size probe closest to the adsorbate. To be clear, the pore size probes deposited by the Zeo++ throughout the pore space have a size label that describes the pore size at that point. This approach uses that size label and the minimum values identified to attribute each probe to one of the three pores present. Applying this to the total adsorption isotherms produces adsorption isotherms for each of the three pores present in the material (Fig. 5), dubbed here as "pore isotherms".

Pore isotherms can be used, for example, to elucidate the reason for the steps observed in the total adsorption isotherms (Fig. 4). The pore isotherms for DUT-32 show that all pores have a drastic increase in uptake at $\approx 4 \times 10^{-2}$ bar followed by another filling step for the largest pore ($p3$) at $\approx 1 \times 10^{-1}$ bar. This filling process is different to UMCM-1 where the initial step is associated with the smallest pores. It appears the smallest pores $p1$ and $p2$ fill together but the large pore only be-

![](./images/1250160250103791623_4.jpg)

Fig. 4: Simulated Ar adsorption isotherms at 87 K displayed as fractional coverage ($\theta$).

gins filling after adsorption is near saturation in the smallest pores. The two-step filling processes in the largest pore ($p3$) of UMCM-1 does not appear to happen alongside but instead following adsorption in the smallest pores. The cooperative nature of all or some of the pores in DUT-32 and UMCM-1 is not present in NU-1000, where each of the pores fill seem- ingly independently, adsorption begins in the smallest pore, then medium pore and finally the largest pore. The above pore isotherms outline three different adsorption behaviours re- sponsible for the steps observed in the total isotherms (Fig. 4). For each material the largest pore is greater than $24$ Å, which would be classified as a mesopore (pore diameter $>20$ Å, demonstrating the expected type-IV behaviour for a pore of this size. $^{48}$ However, as observed for DUT-32 the surrounding pores can cooperatively fill at the same pressure leading to a de- parture from simple type-IV behaviour. These pore isotherms demonstrate the size of the pore does not necessarily dictate at which pressure adsorption occurs. Gas adsorption occurs at the medium sized pores in DUT-32 and UMCM-1 before the smallest pore highlighting the influence of pore structure on adsorption.

To understand the location of adsorbates in greater detail, beyond the global view offered by pore isotherm analysis, it was necessary to obtain the pore centres. This was achieved by applying a clustering algorithm to the pore structure probes to delineate each pore, obtaining the pore centre for each pore in the crystal structure. Applying this algorithm is not entirely straightforward and requires careful choice of maximum dis- tance between samples (EPS or epsilon) and minimum number of samples to effectively separate the probes into each respec- tive pore. Subsequently, the radial distribution of adsorbates from these pore centres can be computed to provide adsorbate locations to discover, for example, whether adsorption is oc- curring at the pore walls or extending in a multi-layer fashion toward the centre of the pore.

The approach applied to DUT-32 provides the pore-centred atomistic environment of $p1$, $p2$ and $p3$, as illustrated in Fig. 6. The pores $p1$ and $p2$ are observed to be very different in struc- ture, which leads to different adsorption sites. The radial distribution demonstrates $p2$ has a defined adsorption site at $\approx 12$ Å, associated with the face of the planar tritopic ligand. No obvious site is observed for $p1$, which leads to preferential adsorption in $p2$ observed in the pore isotherms (Fig. 5). The first step in the isotherm is observed in all pores of this ma- terial. We can see this in the radial plots of the fourth point, where a drastic increase in number of molecules is observed for each pore. The adsorbed phases after this step extends from the surface of $p1$ and $p2$ to the centre of the pore but only extends $\approx 5$ Å from the pore wall in $p3$ The localisation suggests the first step is associated with pore saturation of both $p1$ and $p2$ that triggers an adsorbed layer to form in $p3$. After this initial step only a small amount of extra adsorption is observed in $p1$ and $p2$ while the increase in pressure leads to the adsorbed layer in $p3$ to grow up to saturation. Clearly this pore-centred view of adsorption provides a unique view of the process of adsorption in hierarchical materials leading to better understanding of pore filling mechanisms.

![](./images/1250160250103791623_5.jpg)

Fig. 5: Pore isotherms for the three pores identified in the materials as ex- tracted from simulated Ar adsorption isotherms at 87 K. $p1$, $p2$ and $p3$ label each pore from smallest to largest

Applying this same approach to UMCM-1 we obtain the pore environments found in this material (Fig. 7). For this material, $p1$ and $p2$ are smaller than DUT-32 but similarly $p2$ has the face of the ligands arranged toward the centre of pore volume and available for adsorption. Ligand faces evidently are excellent adsorption sites as this is also observed to provide a preferential adsorption site leading to more adsorption, at low pressure, occurring in $p2$ than $p1$. The initial pore filling step (point three) in UMCM-1 is again related to a drastic increase in all of the pores and evidently filling the smallest pores ($p1$ and $p2$). The second pore filling step here follows a different

Preprint | May 22, 2022 | 4

![](./images/1250160250103791623_6.jpg)

Fig. 6: Pore-centred view of adsorption in DUT-32. Ar adsorption isotherm at 87 K with the points extracted for radial distribution analysis labelled as points (a). Pore environments of the pores present in DUT-32 where the centre of the pore is depicted by a green, orange and purple sphere (b). Radial distributions of Ar and framework atoms (grey background) from the centre of each pore for the pressure points labelled in the isotherm (c).

process to DUT-32, adsorbates are found to increase in popu- lation at the pore wall as the pressure increases. The adsorbed phase does not grow significantly toward the centre of the pore until after the step in the isotherm when this pore becomes filled drastically. This difference in adsorbed phase is likely related to the different nature of the mesopores in DUT-32 and UMCM-1. In DUT-32 the mesopore is a connected cage and in UMCM-1 the mesopore is a one-dimensional channel. The different behaviour suggests that a channel structure will have a greater delay in pore filling demonstrating the expected delayed onset of adsorption observed for commonly reported mesoporous materials.

This typical behaviour of one-dimensional mesopores is also evident in the same analysis applied to NU-1000 (Supplemen- tary Figure 5). Once again the adsorption in the small pores happens together at low pressure with distributions within the pores appearing filled at $\approx 1 \times 10^{-3}$ bar. At this point is it clear how little adsorption is present in the largest pore with small populations observed at the pore wall. After this point the amount adsorbed slowly grows at the wall and also into the pore with distinct peaks in structure observed when satu- rated suggesting a well defined radial pattern of the saturated phase. Upon complete pore filling at 1 bar there are subtle variations in the distributions of adsorbates in the $p 2$ pore but no drastic changes, related to adsorbate migration, observed for NU-1000 or any of the materials examined in this work. The above analysis of these three materials demonstrates that the pore-centred radial adsorption distribution is a useful tool for comparing between these hierarchical materials, identifying pore filling mechanisms that occur cooperatively and trigger further adsorption in the material.

### 4. Conclusions
Adsorption in hierarchical porous structures can produce fas- cinating phenomena that may lead to exciting technological development. However, charting this behaviour in crystalline materials is not entirely straightforward necessitating careful analysis.

This work has demonstrated that statistical analysis of probe sites can extract pore environments from commonly employed pore size distribution methods, as applied to crys- talline representations. The approach was tested for a series of MOFs that feature hierarchical pore systems, DUT-32, DUT-75, UMCM-1 and NU-1000. It is found that separating the pore system with respect to pore size can differentiate the different pores in DUT-32, UMCM-1 and NU-1000, however cannot discern the different pores in DUT-75. The challenging case of DUT-75 highlights that for materials featuring differ- ent pore environments of roughly the same size alternative approaches are required. The different sections of pore space filled during Ar adsorption at 87 K was then examined us- ing these pore descriptions to illustrate the cooperative be- haviour present in all pores of DUT-32, the two smallest pores of UMCM-1 and an absence of pore cooperativity observed for NU-1000. To extract the pore environment, which permits a local description of adsorption, clustering was applied to the probes to obtain positions of pore centres. Computing radial distributions from the pore centres led to a comparison of adsorption mechanisms in each of these pores identifying pref- erential adsorption sites and a significant difference in cage mesopores and one-dimensional mesopores.

Porosity analysis beyond global descriptions of pore volume and surface area are needed to differentiate the unique pore systems present in the growing databases of porous materials. The presented approach to extract pore isotherms and a pore-

Preprint | May 22, 2022 | 5

![](./images/1250160250103791623_7.jpg)

Fig. 7: Pore-centred view of adsorption in UMCM-1. Ar adsorption isotherm at 87 K with the points extracted for radial distribution analysis labelled as points (a). Pore environments of the pores found in UMCM-1 where the centre of the pore is depicted by a green, orange and purple sphere (b). Radial distributions of Ar and framework atoms (grey background) from the centre of each pore for the pressure points labelled in the isotherm (c).

centred adsorption environments can be readily extended to more porous materials by choosing a robust set of parameters, such as bandwidth and cluster size and distance. Moreover, this approach is not limited to in silico investigations, for example using in situ X-ray diffraction, adsorbate positions relative to these pore locations can provide experimental pore isotherms, demonstrated previously.¹⁹ The approach detailed here opens new opportunities for the automated development of pore isotherms to produce kernels to enable the characterisation of pore size distributions based on isotherms alone.²² Furthermore, by opening these tools to the research community the diverse collection of porous structures being developed can be examined in greater detail perhaps uncovering new counterintuitive and temporal adsorption processes.⁴⁹

## Author Contributions

As sole author JDE was responsible for all the above, in its entirety.

## Conflicts of interest

There are no conflicts to declare.

## Acknowledgements

JDE thanks helpful discussion with the Professor Christopher Sumby (The University of Adelaide), Professor Stefan Kaskel (Technische Universität Dresden) and the Sumby-Doonan research group at the University of Adelaide. JDE is supported by a Ramsay Fellowship from the University of Adelaide. ZIH Dresden and Phoenix HPC service at the University of Adelaide are thanked for providing high-performance computing resources. This project was undertaken with the assistance of resources and services from the National Computational Infrastructure (NCI), which is supported by the Australian Government.

## References

1. Li, H.; Li, L.; Lin, R.B.; Zhou, W.; Zhang, Z.; Xiang, S.; and Chen, B. "Porous metal-organic frameworks for gas storage and separation: Status and challenges." EnergyChem, 2019. 1(1):100006. doi:10.1016/j.enchem.2019.100006
2. Davis, M.E. "Ordered porous materials for emerging applications." Nature, 2002. 417(6891):813-821. doi:10.1038/nature00785
3. Corma, A.; García, H.; and i Xamena, F.X.L. "Engineering Metal Organic Frameworks for Heterogeneous Catalysis." Chemical Reviews, 2010. 110(8):4606-4655. doi:10.1021/cr9003924
4. Furukawa, H.; Cordova, K.E.; O'Keeffe, M.; and Yaghi, O.M. "The Chemistry and Applications of Metal-Organic Frameworks." Science, 2013. 341(6149):491-496. doi:10.1126/science.1230444
5. Stein, A.; Wang, Z.; and Fierke, M.A. "Functionalization of Porous Carbon Materials with Designed Pore Architecture." Advanced Materials, 2009. 21(3):265-293. doi:10.1002/adma.200801492
6. Eddaoudi, M.; Kim, J.; Rosi, N.; Vodak, D.; Wachter, J.; O'Keeffe, M.; and Yaghi, O.M. "Systematic Design of Pore Size and Functionality in Isoreticular MOFs and Their Application in Methane Storage." Science, 2002. 295(5554):469-472. doi:10.1126/science.1067208
7. Alezi, D.; Belmabkhout, Y.; Suyetin, M.; Bhatt, P.M.; Weseliński, Ł.J.; Solovyeva, V.; Adil, K.; Spanopoulos, I.; Trikalitis, P.N.; Emwas, A.H.; and Eddaoudi, M. "MOF Crystal Chemistry Paving the Way to Gas Storage Needs: Aluminum-Based soc-MOF for CH4, O2, and CO2 Storage." Journal of the American Chemical Society, 2015. 137(41):13308-13318. doi:10.1021/jacs.5b07053
8. Coasne, B.; Galarneau, A.; Gerardin, C.; Fajula, F.; and Villemot, F. "Molecular Simulation of Adsorption and Transport in Hierarchical Porous Materials." Langmuir, 2013. 29(25):7864-7875. doi:10.1021/la401228k
9. Yang, X.Y.; Léonard, A.; Lemaire, A.; Tian, G.; and Su, B.L. "Self-formation phenomenon to hierarchically structured porous materials: design, synthesis, formation mechanism and applications." Chemical Communications, 2011. 47(10):2763. doi:10.1039/c0cc03734f
10. Coasne, B. "Multiscale adsorption and transport in hierarchical porous materials." New Journal of Chemistry, 2016. 40(5):4078-4094. doi:10.1039/c5nj03194j
11. de A. A. Soler-Illia, G.J.; Sanchez, C.; Lebeau, B.; and Patarin, J. "Chemical Strategies To Design Textured Materials: from Microporous and Mesoporous Oxides to

Preprint | May 22, 2022 | 6

Nanonetworks and Hierarchical Structures." *Chemical Reviews*, 2002. **102**(11):4093–4138. doi:10.1021/cr0200062

12. Zhou, H.C.; Long, J.R.; and Yaghi, O.M. "Introduction to Metal-Organic Frame- works." *Chemical Reviews*, 2012. **112**(2):673–674. doi:10.1021/cr300014x

13. Struckhoff, K.C.; Thommes, M.; and Sarkisov, L. "On the Universality of Cap- illary Condensation and Adsorption Hysteresis Phenomena in Ordered and Crys- talline Mesoporous Materials." *Advanced Materials Interfaces*, 2020. **7**(12):2000184. doi:10.1002/admi.202000184

14. Férey, G. and Serre, C. "Large breathing effects in three-dimensional porous hybrid matter: facts, analyses, rules and consequences." *Chemical Society Reviews*, 2009. **38**(5):1380. doi:10.1039/b804302g

15. Krause, S.; Bon, V.; Senkovska, I.; Stoeck, U.; Wallacher, D.; Többens, D.M.; Zander, S.; Pillai, R.S.; Maurin, G.; Coudert, F.X.; and Kaskel, S. "A pressure- amplifying framework material with negative gas adsorption transitions." *Nature*, 2016. **532**(7599):348–352. doi:10.1038/nature17430

16. Bon, V.; Brunner, E.; Pöppl, A.; and Kaskel, S. "Unraveling Structure and Dynamics in Porous Frameworks via Advanced In Situ Characterization Techniques." *Advanced Functional Materials*, 2020. **30**(41):1907847. doi:10.1002/adfm.201907847

17. Schneemann, A.; Bon, V.; Schwedler, I.; Senkovska, I.; Kaskel, S.; and Fischer, R.A. "Flexible metal-organic frameworks." *Chem Soc Rev*, 2014. **43**(16):6062–6096. doi:10.1039/c4cs00101j

18. Cho, H.S.; Yang, J.; Gong, X.; Zhang, Y.B.; Momma, K.; Weckhuysen, B.M.; Deng, H.; Kang, J.K.; Yaghi, O.M.; and Terasaki, O. "Isotherms of individual pores by gas adsorption crystallography." *Nature Chemistry*, 2019. **11**(6):562–570. doi:10.1038/s41557-019-0257-2

19. Krause, S.; Evans, J.D.; Bon, V.; Senkovska, I.; Iacomi, P.; Kolbe, F.; Ehrling, S.; Troschke, E.; Getschmann, J.; Többens, D.M.; Franz, A.; Wallacher, D.; Yot, P.G.; Maurin, G.; Brunner, E.; Llewellyn, P.L.; Coudert, F.X.; and Kaskel, S. "Towards general network architecture design criteria for negative gas adsorption transitions in ultraporous frameworks." *Nature Communications*, 2019. **10**(1):3632. doi:10.1038/s41467-019-11565-3

20. Dantas, S.; Sarkisov, L.; and Neimark, A.V. "Deciphering the Relations between Pore Structure and Adsorption Behavior in Metal-Organic Frame- works: Unexpected Lessons from Argon Adsorption on Copper-Benzene-1, 3, 5- tricarboxylate." *Journal of the American Chemical Society*, 2019. **141**(21):8397–8401. doi:10.1021/jacs.9b09006

21. Evans, J.D.; Fraux, G.; Gaillac, R.; Kohen, D.; Trousset, F.; Vanson, J.M.; and Coudert, F.X. "Computational Chemistry Methods for Nanoporous Materials." *Chem- istry of Materials*, 2016. **29**(1):199–212. doi:10.1021/acs.chemmater.6b02994

22. Parashar, S.; Zhu, Q.; Dantas, S.; and Neimark, A.V. "Monte Carlo Simulations of Nanopore Compartmentalization Yield Fingerprint Adsorption Isotherms as a Ratio- nale for Advanced Structure Characterization of Metal-Organic Frameworks." *ACS Applied Nano Materials*, 2021. **4**(5):5531–5540. doi:10.1021/acsanm.1c00937

23. Gelb, L.D. and Gubbins, K.E. "Pore Size Distributions in Porous Glasses: A Com- puter Simulation Study." *Langmuir*, 1998. **15**(2):305–308. doi:10.1021/la9808418

24. Haldoupis, E.; Nair, S.; and Sholl, D.S. "Efficient Calculation of Diffusion Limitations in Metal Organic Framework Materials: A Tool for Identifying Materials for Kinetic Separations." *Journal of the American Chemical Society*, 2010. **132**(21):7528–7539. doi:10.1021/ja1023699

25. Pinheiro, M.; Martin, R.L.; Rycroft, C.H.; Jones, A.; Iglesia, E.; and Haranczyk, M. "Characterization and comparison of pore landscapes in crystalline porous materials." *Journal of Molecular Graphics and Modelling*, 2013. **44**:208–219. doi:10.1016/j.jmgm.2013.05.007

26. Willems, T.F.; Rycroft, C.H.; Kazi, M.; Meza, J.C.; and Haranczyk, M. "Al- gorithms and tools for high-throughput geometry-based analysis of crystalline porous materials." *Microporous and Mesoporous Materials*, 2012. **149**(1):134–141. doi:10.1016/j.micromeso.2011.08.020

27. Jones, A.J.; Ostrouchov, C.; Haranczyk, M.; and Iglesia, E. "From rays to struc- tures: Representation and selection of void structures in zeolites using stochas- tic methods." *Microporous and Mesoporous Materials*, 2013. **181**:208–216. doi:10.1016/j.micromeso.2013.07.033

28. Grünkler, R.; Bon, V.; Müller, P.; Stoeck, U.; Krause, S.; Mueller, U.; Senkovska, I.; and Kaskel, S. "A new metal-organic framework with ultra-high surface area." *Chemical Communications*, 2014. **50**(26):3450. doi:10.1039/c4cc00113c

29. Stoeck, U.; Senkovska, I.; Bon, V.; Krause, S.; and Kaskel, S. "Assembly of metal- organic polyhedra into highly porous frameworks for ethene delivery." *Chemical Communications*, 2015. **51**(6):1046–1049. doi:10.1039/c4cc07920e

30. Koh, K.; Wong-Foy, A.; and Matzger, A. "A Crystalline Mesoporous Coordination Copolymer with High Microporosity." *Angewandte Chemie International Edition*, 2008. **47**(4):677–680. doi:10.1002/anie.200705020

31. Mondloch, J.E.; Bury, W.; Fairen-Jimenez, D.; Kwon, S.; DeMarco, E.J.; Weston, M.H.; Sarjeant, A.A.; Nguyen, S.T.; Stair, P.C.; Snurr, R.Q.; Farha, O.K.; and Hupp, J.T. "Vapor-Phase Metalation by Atomic Layer Deposition in a Metal-Organic Framework." *Journal of the American Chemical Society*, 2013. **135**(28):10294–10297. doi:10.1021/ja4050828

32. Cho, H.S.; Deng, H.; Miyasaka, K.; Dong, Z.; Cho, M.; Neimark, A.V.; Kang, J.K.; Yaghi, O.M.; and Terasaki, O. "Extra adsorption and adsorbate superlat- tice formation in metal-organic frameworks." *Nature*, 2015. **527**(7579):503–507. doi:10.1038/nature15734

33. Javahery, S.; Simon, C.M.; Braun, E.; Witman, M.; Tiana, D.; Vlaisavljevich, B.; and Smit, B. "Adsorbate-induced lattice deformation in IRMOF-74 series." *Nature Communications*, 2017. **8**(1):13945. doi:10.1038/ncomms13945

34. Breck, D. and Breck, D. *Zeolite Molecular Sieves: Structure, Chemistry, and Use.* A Wiley-Interscience publication. Wiley, 1973. ISBN 9780471099857

35. Seabold, S. and Perktold, J. "statsmodels: Econometric and statistical modeling with python." In "9th Python in Science Conference," 2010

36. Ester, M.; Kriegel, H.P.; Sander, J.; and Xu, X. "A Density-Based Algorithm for Discovering Clusters in Large Spatial Databases with Noise." In "Proceedings of the Second International Conference on Knowledge Discovery and Data Mining," KDD'96. AAAI Press, 1996 p. 226–231

37. Schubert, E.; Sander, J.; Ester, M.; Kriegel, H.P.; and Xu, X. "DBSCAN Re- visited, Revisited." *ACM Transactions on Database Systems*, 2017. **42**(3):1–21. doi:10.1145/3068335

38. Pedregosa, F.; Varoquaux, G.; Gramfort, A.; Michel, V.; Thirion, B.; Grisel, O.; Blondel, M.; Prettenhofer, P.; Weiss, R.; Dubourg, V.; Vanderplas, J.; Passos, A.; Cournapeau, D.; Brucher, M.; Perrot, M.; and Édouard Duchesnay. "Scikit- learn: Machine Learning in Python." *Journal of Machine Learning Research*, 2011. **12**(85):2825–2830

39. Verstraelen, T.; Vanduyffhuys, L.; Vandenbrande, S.; and Rogge, S. "Yaff, yet another force field." http://molmod.ugent.be/software/, 2022

40. Peng, D.Y. and Robinson, D.B. "A New Two-Constant Equation of State." *Industrial & Engineering Chemistry Fundamentals*, 1976. **15**(1):59–64. doi:10.1021/i160057a011

41. Martín-Calvo, A.; García-Pérez, E.; García-Sánchez, A.; Bueno-Pérez, R.; Hamad, S.; and Calero, S. "Effect of air humidity on the removal of carbon tetrachloride from air using Cu-BTC metal-organic framework." *Physical Chemistry Chemical Physics*, 2011. **13**(23):11165. doi:10.1039/c1cp20168a

42. Mayo, S.L.; Olafson, B.D.; and Goddard, W.A. "DREIDING: a generic force field for molecular simulations." *The Journal of Physical Chemistry*, 1990. **94**(26):8897–8909. doi:10.1021/j100389a010

43. Rappe, A.K.; Casewit, C.J.; Colwell, K.S.; Goddard, W.A.; and Skiff, W.M. "UFF, a full periodic table force field for molecular mechanics and molecular dynamics simulations." *Journal of the American Chemical Society*, 1992. **114**(25):10024–10035. doi:10.1021/ja00051a040

44. ???? Zenodo repository corresponding to this work 10.5281/zenodo.6568212 will made open access after manuscript acceptance.

45. Li, P.; Vermeulen, N.A.; Malliakas, C.D.; Gómez-Gualdrón, D.A.; Howarth, A.J.; Mehdi, B.L.; Dohnalkova, A.; Browning, N.D.; O'Keeffe, M.; and Farha, O.K. "Bottom-up construction of a superstructure in a porous uranium-organic crystal." *Science*, 2017. **356**(6338):624–627. doi:10.1126/science.aam7851

46. Hönicke, I.M.; Senkovska, I.; Bon, V.; Baburin, I.A.; Bönisch, N.; Raschke, S.; Evans, J.D.; and Kaskel, S. "Balancing Mechanical Stability and Ultrahigh Porosity in Crystalline Framework Materials." *Angewandte Chemie International Edition*, 2018. **57**(42):13780–13783. doi:10.1002/anie.201808240

47. Sircar, S. and Myers, A.L. *Gas separation by zeolites*, vol. 1063. Marcel Dekker Inc.: New York, 2003

48. Thommes, M.; Kaneko, K.; Neimark, A.V.; Olivier, J.P.; Rodriguez-Reinoso, F.; Rouquerol, J.; and Sing, K.S. "Physisorption of gases, with special reference to the evaluation of surface area and pore size distribution (IUPAC Technical Report)." *Pure and Applied Chemistry*, 2015. **87**(9-10):1051–1069. doi:10.1515/pac-2014-1117

49. Evans, J.D.; Bon, V.; Senkovska, I.; Lee, H.C.; and Kaskel, S. "Four- dimensional metal-organic frameworks." *Nature Communications*, 2020. **11**(1):2690. doi:10.1038/s41467-020-16527-8

---

Preprint | May 22, 2022 | 7
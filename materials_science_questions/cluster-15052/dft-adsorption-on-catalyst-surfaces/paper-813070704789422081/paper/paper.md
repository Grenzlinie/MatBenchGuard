# Structural and Electronic Descriptors of Catalytic Activity of Graphene-Based Materials: First-Principles Theoretical Analysis
S. Sinthika, Umesh V. Waghmare,* and Ranjit Thapa*

Characteristic features of the d-band in electronic structure of transition metals are quite effective as descriptors of their catalytic activity toward oxygen reduction reaction (ORR). With the promise of graphene-based materials to replace precious metal catalysts, descriptors of their chemical activity are much needed. Here, a site-specific electronic descriptor is proposed based on the $p_z$ ($\pi$) orbital occupancy and its contribution to electronic states at the Fermi level. Simple structural descriptors are identified, and a linear predictive model is developed to precisely estimate adsorption free energies of OH ($\Delta G_\text{OH}$) at various sites of doped graphene, and it is demonstrated through prediction of the most optimal site for catalysis of ORR. These structural descriptors, essentially the number of ortho, meta, and para sites of N/B-doped graphene sheet, can be extended to other doped $\text{sp}^2$ hybridized systems, and greatly reduce the computational effort in estimating $\Delta G_\text{OH}$ and site-specific catalytic activity.

## 1. Introduction
Efficient conversion of chemical energy to electrical energy in a fuel cell greatly depends on the catalytic activity of the material used as its cathode.$^{[1]}$ For cathode catalysts in low-temperature fuel cells, $\text{sp}^2$-based carbon materials are attractive candidates because they are inexpensive, stable, highly abundant, and CO tolerant. However, $\text{O}_2$ does not bind well with pristine $\text{sp}^2$-based carbon materials making them poor candidates for cathodes.$^{[2]}$ Alloying through heteroatom substitution (employing mainly boron and nitrogen as dopants)$^{[3-6]}$ and defects modify the electronic properties of $\text{sp}^2$-based carbon materials, and have the potential to transform them into efficient oxygen reduction reaction (ORR) catalysts. With rising interest in $\text{sp}^2$-based carbon materials for catalysis of ORR, it is desirable to understand their chemical activity and its dependence on various configurations of substitutional doping, and develop simple models to facilitate their design and experimental synthesis.

Identification of a small set of readily accessible properties of a material as descriptors of its performance in an application facilitates construction of a simple predictive model that can be used in selecting promising materials from a large set.$^{[7,8]}$ Such descriptor-based approach has been employed by many researchers to obtain general reactivity trends of many vital reactions like hydrogen evolution reaction, ORR, CO oxidation, and $\text{CO}_2$ hydrogenation over transition metals.$^{[9]}$ For instance, electronic d-band center and the binding energy of atomic oxygen have been recognized as general descriptors for catalytic activity of transition metals and transition metal sulfides.$^{[10-12]}$ A theoretical estimate of $\text{e}_\text{g}$ or $\text{t}_{2\text{g}}$ orbital occupancy of a metal site of copper delafossite oxides correlates well with the oxygen evolution activity making it a suitable descriptor.$^{[13]}$ The electronic structure based descriptors have been extended to the delocalized oxygen 2p-band to predict the activity of perovskite oxide catalysts.$^{[14]}$

Descriptors based on the valence orbital levels of the active centers of graphene and electronegativity of dopants have also been identified.$^{[15,16]}$ However, in order to ascertain the local reactivity of different active sites of the host graphene lattice, suitable electronic descriptors are essential. A number of works hint the important role played by the $\pi$ orbitals in the activity of graphene-based catalysts.$^{[17-19]}$ Experimental and theoretical results on doped carbon nanostructures have revealed that effective utilization of carbon $\pi$ electrons that become localized upon doping is essential for $\text{O}_2$ reduction, in addition to the breaking of local charge neutrality by a dopant.$^{[20,21]}$ The significant role played by the $p_z$ orbital in anchoring the ORR intermediates was also identified in our earlier work.$^{[22]}$ It has been identified via a combined experimental and theoretical study that the $p_z$ electrons of the active sites of doped graphene are responsible for triggering ferromagnetism in graphene.$^{[23]}$

Here, we provide a comprehensive understanding of graphene-based electrocatalysts based on fundamental descriptors derived solely from $p_z$ ($\pi$) electronic structure. We show that $p_z$ orbital occupancy can be used as a simple yet powerful

Dr. S. Sinthika, $^{[+]}$ Prof. R. Thapa
SRM Research Institute and Department of Physics and Nanotechnology
SRM University
Kattankulathur 603203, Tamil Nadu, India
E-mail: ranjit.t@res.srmuniv.ac.in

Prof. U. V. Waghmare
Theoretical Sciences Unit
Jawaharlal Nehru Centre for Advanced Scientific Research
Bangalore 560064, Karnataka, India
E-mail: waghmare@jncasr.ac.in

![](./images/813070704789422081_1.jpg)
The ORCID identification number(s) for the author(s) of this article can be found under https://doi.org/10.1002/smll.201703609.

$^{[+]}$Present address: PG and Research Department of Physics, Lady Doak College, Madurai 625002, Tamil Nadu, India

DOI: 10.1002/smll.201703609

descriptor in determining the local surface reactivity of each active site of graphene-based catalysts. We then identify atomic structural descriptors and develop a predictive model of free energies of OH adsorption ($\Delta G_{\mathrm{OH}}$) at any site of nitrogen/boron-doped graphene. Our model along with these structural and electronic descriptors will help in design of the best possible sp²-based catalyst.

## 2. Results and Discussions
### 2.1. Large Data from the Dopant Configurations

A large pool of descriptors (listed in Table 1) has been identified in the literature for screening various classes of catalysts targeting specific applications. In N/B-doped graphene, the mechanism of charge transfer interaction between the dopants and the host carbon atoms is twofold: the electronegativity difference between the dopant and the neighboring carbon atoms results in the polarization of the in-plane sigma bonds (donation interaction) and a back-donation interaction from/to the dopant involving the out of plane $\pi$ bonds.[17,22]

To identify and test effective descriptors of sp² hybridized carbon catalysts, we considered a number of cases of nitrogen and boron substitution (since these dopants do not distort the host lattice) on the graphene lattice at varying concentration. Figure 1a shows various configurations (N, 2N, 3N, B, 2B, 3B) of boron and nitrogen substitution, and corresponding (inequivalent) active sites that are available for the ORR intermediates (OOH, O, and OH) to bind. The dopants are labeled with S (red) and the active sites are denoted as C (see Figure 1b). Another model suggested by Okamoto was also considered in this study, named as 2N-N.[34] In the case of boron doping (see Figure 1b), in addition to the inequivalent carbon sites listed in the table, boron substitutional sites were also considered as active sites. We also considered co-doping with boron and nitrogen (B2N) and the corresponding inequivalent carbon sites being C*, C3, and C4.

### 2.2. Descriptors: $\pi$ Electronic Structure

We first examine the following descriptors based entirely on the $\pi$ electronic structure (i) $D_{\mathrm{p}_{z}}(E_{\mathrm{F}})$, which is the density of states at the Fermi level $E_{\mathrm{F}}$ projected on $\mathrm{p}_{z}$ orbitals of the active sites, and (ii) relative $\mathrm{p}_{z}$ orbital occupancy ($O_{\mathrm{p}_{z}}$), here the occupancy is obtained as an integration of the density of occupied (from $E=-\infty$ to $E_{\mathrm{F}}$) states projected onto $\mathrm{p}_{z}$ orbital of the active site, and it is relative to the $\mathrm{p}_{z}$ occupancy of a carbon atom in the undoped graphene

$$
O_{\mathrm{p}_{z}}=\left[\int_{-\infty}^{0} \rho_{\mathrm{p}_{z}} d E\right]_{\text {active site }}-\left[\int_{-\infty}^{0} \rho_{\mathrm{p}_{z}} d E\right]_{\text {carbon atom in pristine graphene }}
\tag{1}
$$

From the $\mathrm{p}_{z}$ projected density of states of inequivalent sites of nitrogen-doped graphene (see Figure 1c), it is clear that substituted nitrogen atom donates its $\mathrm{p}_{z}$ electrons to the lattice, populating antibonding orbitals and shifting the Fermi level to the right. On the other hand, substitution of boron atom depopulates the bonding orbitals of graphene lattice, and shifts the Fermi level to the left (see Figure 1d). Even though n- and p-type doping shift the Fermi level in opposite directions, both these doping are known to be efficient in activating molecules. The values of $\mathrm{p}_{z}$ projected density of state at the Fermi level ($D_{\mathrm{p}_{z}}(E_{\mathrm{F}})$) of each active site in 1N and 1B configurations of doped graphene sheet are shown in Figure 1c,d. The parameter $D_{\mathrm{p}_{z}}(E_{\mathrm{F}})$ of an active site essentially gives a qualitative estimate on the amount by which the Fermi level is shifted (irrespective of the type of dopant), and hence the extent to which the $\mathrm{p}_{z}$ electrons are available for charge transfer and bonding. In fact, the density of states at Fermi level[35] is known to be valuable in determining the catalytic activity of transition metals as well.

The area of the projected density of occupied states (shown shaded in Figure 1c,d) gives an estimate of the number of $\mathrm{p}_{z}$ electrons available for bonding with the ORR intermediates. Each carbon atom in pristine graphene has one electron in the out of plane $\mathrm{p}_{z}$ orbital, and hence a $\mathrm{p}_{z}$ orbital occupancy of one. However, due to incompleteness of atomic orbital basis, calculated $\mathrm{p}_{z}$ occupancy is 0.986. The number of $\mathrm{p}_{z}$ electrons gained or lost by an active site upon doping (relative $\mathrm{p}_{z}$ occupancy) is obtained by subtracting this value (0.986) from the calculated $\mathrm{p}_{z}$ occupancy of each active site.

### 2.3. Correlation of the Catalytic Activity with $\Delta G_{\mathrm{OH}}$

The free energy of adsorption of OH, $\Delta G_{\mathrm{OH}}$, is given by equation

$$
\Delta G_{\mathrm{OH}}=\left(G_{\mathrm{OH}(\text { grap })}\right)-\left(G_{(\text {grap) }}+G_{\mathrm{OH}^{-}}\right)
\tag{2}
$$

The steps to estimate reaction free energies and adsorption free energies of intermediates are given in the Supporting Information.[12,36-38] The $\Delta G_{\mathrm{OH}}$ is an efficient quantifying parameter of catalytic activity, as a plot of $\Delta G_{\mathrm{OH}}$ versus overpotential yields a volcano-type relationship, from which the optimal binding strength of OH can be identified.[39] A plot of $\Delta G_{\mathrm{OH}}$ versus the negative of the overpotential ($-\eta$) of the various active sites of nitrogen-doped graphene (all configurations) shows a volcano-type plot (see Figure 2). The active sites that bind OH very strongly lie in the left leg of the volcano while the sites which bind OH weakly are at its right leg. The C3 site of 3N-doped graphene and the C3 site of 2N-doped graphene lie at the tip of the volcano, both exhibiting the lowest overpotential of 0.66 V.

### 2.4. Correlation of the Catalytic Activity with $D_{\mathrm{p}_{z}}(E_{\mathrm{F}})$

We find that $D_{\mathrm{p}_{z}}(E_{\mathrm{F}})$ exhibits quite a linear correlation with $\Delta G_{\mathrm{OH}}$ for all the active sites of boron- and nitrogen-doped graphene (see Figure 3a,b). In the case of single nitrogen doping, the *ortho* carbon atoms have the highest $D_{\mathrm{p}_{z}}(E_{\mathrm{F}})$, followed by the carbon atoms in the meta positions, and then by the para carbon atoms. The parameter $D_{\mathrm{p}_{z}}(E_{\mathrm{F}})$ is sensitive to the localized states that are created on the host carbon atoms in the vicinity of the dopants.[40] Figure 3a,b shows plots of $D_{\mathrm{p}_{z}}(E_{\mathrm{F}})$ versus $\Delta G_{\mathrm{OH}}$ of the active sites of nitrogen-, boron-, and

<table>
<thead>
<tr>
<th>Descriptor</th>
<th>Class of catalyst</th>
<th>Calculation</th>
<th>Reaction</th>
<th>Optimal catalyst(s) identified</th>
</tr>
</thead>
<tbody>
<tr>
<td>d-band center[24]</td>
<td>Transition metals, transition metal alloys</td>
<td>$\displaystyle\frac{\int_{-\infty}^{0}\rho_{d}E\mathrm{d}E}{\int_{-\infty}^{0}\rho_{d}\mathrm{d}E}$</td>
<td>ORR</td>
<td>(a) Pt and Pd[25]</td>
</tr>
<tr>
<td>$e_{g}$ occupancy[27]</td>
<td>Transition metal oxides</td>
<td>$\displaystyle\int_{-\infty}^{0}\rho_{e_{g}}\mathrm{d}E$</td>
<td>ORR</td>
<td>(b) Pt₃Ni[26]<br>LaCoO₃ ($t_{2g}^{6}e_{g}^{1}$) and LaNiO₃($t_{2g}^{6}e_{g}^{1}$)</td>
</tr>
<tr>
<td>$t_{2g}$ occupancy[13]</td>
<td>Transition metal oxides</td>
<td>$\displaystyle\int_{-\infty}^{0}\rho_{t_{2g}}\mathrm{d}E$</td>
<td>Oxygen evolution reaction (OER)</td>
<td>CuCoO₂, PtCoO₂</td>
</tr>
<tr>
<td>O p-band center[14]</td>
<td>Transition metal oxides</td>
<td>$\displaystyle\frac{\int_{-\infty}^{0}\rho_{p}E\mathrm{d}E}{\int_{-\infty}^{0}\rho_{p}\mathrm{d}E}$</td>
<td>OER</td>
<td>(Pr₀.₅Ba₀.₅)CoO₃</td>
</tr>
<tr>
<td>$E_{vac}$, vacancy formation energy[28]</td>
<td>Core shell transition metal nanoparticles</td>
<td>$E_{vac}=E_{total}^{N,clean}-(E_{total}^{N-1}+E_{total}^{Atom})$<br><br>N: number of total atoms in a slab model</td>
<td>ORR</td>
<td>Pd₃Cu₁@Pt (core@shell)</td>
</tr>
<tr>
<td>$E_{surf}$, surface energy[29]</td>
<td>Pure metals</td>
<td>$\displaystyle E_{surf}=\frac{1}{2A_{0}}(E_{slab}-N_{M}\mu_{M}-N_{C}\mu_{C})$<br><br>A₀: cross sectional area of surface slab unit cell</td>
<td>Hydrogen evolution reaction</td>
<td>Pt</td>
</tr>
<tr>
<td>$E_{surf}$, surface energy[29]</td>
<td>Transition metal carbides</td>
<td>$\displaystyle E_{surf}=\frac{1}{2A_{0}}(E_{slab}-N_{M}\mu_{M}-N_{C}\mu_{C})$<br><br>$N_{M},N_{C}$: number of metal and carbon atoms in a slab<br>$\mu_{M},\mu_{C}$: chemical potential of metal and carbon atoms</td>
<td>Hydrogen evolution reaction</td>
<td>Pt/Mo₂C</td>
</tr>
<tr>
<td>Work function[30]</td>
<td>Perovskite oxides</td>
<td>Work function calculation by density functional theory (DFT)</td>
<td>Thermionic emission</td>
<td>SrVO₃</td>
</tr>
<tr>
<td>Generalized coordination number[31]</td>
<td>Transition metals</td>
<td>$\displaystyle\overline{\mathrm{CN}}(i)=\sum_{j=1}^{n_{i}}\frac{\mathrm{cn}(j)}{\mathrm{cn}_{\max}}$<br><br>cn: coordination number<br>cn<sub>max</sub>: maximum number of first nearest neighbors in the bulk</td>
<td>ORR</td>
<td>Sites with same number of first nearest neighbors as Pt(111) but with increased second neighbors.</td>
</tr>
<tr>
<td>$E_{diff}^{[28]}$</td>
<td>Doped graphene</td>
<td>$E_{val(min)}$ (active center) $-E_{val(max)}$ (graphene)</td>
<td>ORR</td>
<td>Nitrogen-doped graphene</td>
</tr>
<tr>
<td>Free energy of OH adsorption[32]</td>
<td>Doped graphene</td>
<td>$\Delta G_{OH^{*}}=(G_{OH@G})-(G_{C}+G_{OH^{-}})$</td>
<td>ORR and OER</td>
<td>Graphene edges and N,P co-doping</td>
</tr>
<tr>
<td>Product of relative electron affinity (A) and electronegativity (E)[16]</td>
<td>Doped graphene</td>
<td>$\Phi=(E_{x}/E_{c})\times(A_{x}/A_{c})$</td>
<td>ORR</td>
<td>Nitrogen-doped graphene.</td>
</tr>
<tr>
<td>$E_{p}^{[33]}$</td>
<td>Doped graphene</td>
<td>Position of the highest peak of the active site's DOS</td>
<td>ORR</td>
<td>Incorporation of S and P dopants into the nitrogen-doped graphene.</td>
</tr>
<tr>
<td>Weighted DOS center of graphene (i) up to Fermi level and (ii) entire DOS range[33]</td>
<td>Doped graphene</td>
<td>$\displaystyle E_{center}=\frac{1}{\sum_{i}\varepsilon_{i}}\sum_{i}\varepsilon_{i}\rho_{i}$</td>
<td>Hydrogen evolution reaction</td>
<td>Does not show a proper correlation with the free energies of adsorption of hydrogen</td>
</tr>
</tbody>
</table>

co-doped graphene. The value of $R^{2}$ (goodness of fit) is 0.71 for nitrogen-doped graphene and 0.75 for boron-doped graphene. The main outliers of this correlation are the adsorbing sites located in the immediate vicinity of (adjacent to) two or more nitrogen/boron dopants. An adsorbate anchored on a carbon atom adjacent to two or more nitrogen atoms acquires electrons not only from the atom on which it is directly bonded to but also from the $p_{z}$ orbital of the neighboring dopant. That is,

![](./images/813070704789422081_2.jpg)

Figure 1. a) The various substitutional sites (denoted in red, filled circles) and active sites in the graphene lattice considered for N-, B-, and B-N co-doped graphene. b) Configurations of varied concentrations along with their active sites for catalysis. Projected density of states on $p_z$ orbitals at various active sites of c) 1N- and d) 1B-doped graphene. The turquoise, red, dark blue, and purple plots indicate the PDOS of ortho, para, meta, and B sites, respectively. The shaded area describes the $p_z$ orbital occupancy. The insets show the magnified view of the states near the Fermi level, with colored dots denoting the values of $p_z$ PDOS at the Fermi level, $D_{p_z}(E_F)$ for each active site.

the $p_z$ electron of nitrogen atoms also contributes to the adsorption of OH on such carbon atoms. Our previous work also shows that the $p_z$ projected density of states of nitrogen shift slightly toward the left relative to the Fermi level upon adsorption of an adsorbate on a C atom adjacent to it, implying that nitrogen has lost electrons, in addition to the carbon atom that directly bonds the adsorbate. $^{[22]}$ Works by Sen et al. also provide evidence to the fact that at such strongly adsorbing sites, there is transfer of $p_z$ electrons from the neighboring atoms to the adsorbate during the process of adsorption. $^{[41]}$ Similarly, in the case of boron doping, an adsorbate bonded to a carbon atom that is adjacent to two or more boron atoms acquires its electrons from the C atom on which in it is bonded to, simultaneously reducing the C atom's tendency to donate electrons to the neighboring boron atom. Hence, there is a slight deviation in the trend of $p_z$-descriptor versus $\Delta G_{OH}$ for only such sites. When these strongly adsorbing sites are not included in the linear fit, $R^2$ improves considerably to 0.90 for nitrogen and to 0.91 for boron doping. As these sites are unfavorable to ORR as they adsorb the intermediates strongly and lie in the extreme right leg of the volcano, they are not relevant to design of optimal sites.

![](./images/813070704789422081_3.jpg)

Figure 2. $\Delta G_{OH}$ versus the negative of overpotential $(-\eta)$ for the different sites of the various N- and B-doped graphene.

### 2.5. Correlation of the Catalytic Activity with $p_z$ Occupancy
Calculated relative $p_z$ occupancy exhibits a linear relationship with $\Delta G_{OH}$ (see Figure 4a). The main deviations from the straight line are associated with adsorption energies at boron sites. Though boron dopants act as strong binding sites, the $p_z$ occupancy of a boron dopant is only about $0.576e$. Unlike nitrogen dopants, boron dopant's empty $p_z$ orbital makes it a good Lewis acid, $^{[42]}$ allowing it to gain $0.57$ $p_z$ electrons from

![](./images/813070704789422081_4.jpg)

Figure 3. Correlation of $D_{\mathrm{p}_{z}}(E_{\mathrm{F}})$ at various active sites of a) N- and b) B-doped graphene with $\Delta G_{\mathrm{OH}}$.

the surrounding carbon atoms. Substituted boron does not readily donate its acquired $\mathrm{p}_{z}$ electrons to the incoming molecules/ORR intermediates, and the electronic charge transferred to the ORR intermediate is mainly from the neighboring carbon atoms. In fact, calculation of the Lowdin charges on the boron site after OH adsorption shows that its $\mathrm{p}_{z}$ occupancy increases to $0.61 e$ after adsorption, implying that a boron atom binds covalently with the OH intermediate by sharing its electrons. It is also clear that the density of states projected on $\mathrm{p}_{z}$ orbitals of B atom does not shift upon OH adsorption (shown in Figure S1 of the Supporting Information), indicating a covalent bond between the boron dopant and the adsorbate with a small charge transferred. The $\mathrm{p}_{z}$ projected density of states of ortho carbon atom of nitrogen-doped graphene is also shown for comparison (see Figure S2 of the Supporting Information). It is evident that the $\mathrm{p}_{z}$ states of the ortho carbon shift to lower energies at -10 to $-5.5 \mathrm{eV}$ upon adsorption, indicating that one of the $\mathrm{p}_{z}$ orbitals is no longer available to take active part in the $\pi$ band. $^{[43]}$ The nature of the boron active site is discussed based on its electronic structure in the Supporting Information. In an earlier work, Yang et al. have ascertained that the electrons donated to the adsorbates on boron-doped carbon nanotubes are from carbon atoms, with boron acting as a bridge. $^{[20]}$ It is thus clear that the $\mathrm{p}_{z}$ occupancy of the boron sites do not directly determine the adsorption strength of the intermediates. In this regard, we have replaced the $\mathrm{p}_{z}$ occupancy of boron sites with the average of $\mathrm{p}_{z}$ occupancies of the carbon atoms adjacent to it. As a result, linear correlation is seen (see Figure 4a) for N and B doping, and it is evident that the relative $\mathrm{p}_{z}$ occupancy of active sites of nitrogen-doped graphene should lie in the range $0.09 e-0.10 e$ to yield optimal values of $\Delta G_{\mathrm{OH}}$. This means that the sites with neighboring carbon atoms gaining $0.09 e-0.1 e$ upon doping are ideal for ORR to occur with a minimum overpotential. A contour plot (Figure 4b) demonstrates the dependence of relative $\mathrm{p}_{z}$ occupancy of active sites of N- and co-doped graphene on $\Delta G_{\mathrm{OH}}$ and hence on the negative of overpotential. The sites in the red region of this plot exhibit the lowest overpotential for ORR, i.e., these sites bind the intermediates moderately. The sites that lie in the blue region are unfavorable to ORR as they either have too strong or too weak binding with OH. The calculated values of relative $\mathrm{p}_{z}$ occupancies, $D_{\mathrm{p}_{z}}(E_{\mathrm{F}}), \Delta G_{\mathrm{OH}}$, and negative of the overpotential of various active sites and graphene-based catalysts are tabulated in Table S2 (Supporting Information).

It is also worth noting that the edge sites also function as active sites during ORR. In order to test the suitability of the descriptors on such systems, we performed calculations on two N-doped edge structure models chosen by Kim et al., $^{[44]}$ choosing a few representative inequivalent sites (see Figure S3 in the Supporting Information). We found that our chosen descriptor ($\mathrm{p}_{z}$ occupancy) exhibits a good linear correlation with the free energy of OH adsorption $(R^{2}=0.89)$, suggesting that they can be extended to predict the ORR activity of edge sites too.

### 2.6. A Minimal Set of Electronic Descriptors, a Predictive Model and Chemical Intuition

#### 2.6.1. Nitrogen-Doped Graphene

Investigation of Table S2 of the Supporting Information suggests simultaneous dependence of $\Delta G_{\mathrm{OH}}$ on $D_{\mathrm{p}_{z}}(E_{\mathrm{F}})$ and the relative $\mathrm{p}_{z}$ occupancy $(O_{\mathrm{p}_{z}})$, i.e., when either one of these two parameters is high (low), $\Delta G_{\mathrm{OH}}$ is low (high). In this section we attempt to estimate a function $f(\mathrm{p}_{z})$ that depends on both $D_{\mathrm{p}_{z}}(E_{\mathrm{F}})$ and $O_{\mathrm{p}_{z}}$ and varies linearly with $\Delta G_{\mathrm{OH}}$.

A linear fit to $\Delta G_{\mathrm{OH}}$ versus $O_{\mathrm{p}_{z}}$ at various active sites of nitrogen- and B2N-doped graphene gives a relation

$$\Delta G_{\mathrm{OH}-\text{nitrogen}}=-9.32O_{\mathrm{p}_{z}}+0.98 \tag{3}$$

Second, a linear fit to $\Delta G_{\mathrm{OH}}$ versus $D_{\mathrm{p}_{z}}(E_{\mathrm{F}})$ of N-doped graphene is

$$\Delta G_{\mathrm{OH}-\text{nitrogen}}=-3.3D_{\mathrm{p}_{z}}(E_{\mathrm{F}})+0.98 \tag{4}$$

From Equations (3) and (4) it is evident that $\Delta G_{\mathrm{OH}}$ is more sensitive to changes in $O_{\mathrm{p}_{z}}$ than to the changes in $D_{\mathrm{p}_{z}}(E_{\mathrm{F}})$.

![](./images/813070704789422081_5.jpg)

Figure 4. a) Relative $p_z$ occupancy versus $\Delta G_{OH}$ on the various active sites of N-, B-, and co-doped graphene, and b) contour plot showing the dependence of $p_z$ occupancy of the active sites of nitrogen-doped and B2N graphene on $\Delta G_{OH}$ and ORR activity (negative of overpotential).

Since the intercepts of lines (3) and (4) are equal, we can define a function that has dependence on both $O_{p_z}$ and $D_{p_z}(E_F)$, varying linearly with $\Delta G_{OH-nitrogen}$ as

$$f\left(p_{z-\mathrm{N}}\right)=2.82\left(O_{p_{z}}\right)+D_{p_{z}}\left(E_{\mathrm{F}}\right) \tag{5}$$

The slope 2.82 has a unit of $(1\ \mathrm{eV}^{-1})$ and its inverse determines the extent of shift in the Fermi level upon nitrogen doping.

The function $f(p_{z-\mathrm{N}})$ versus $\Delta G_{OH-nitrogen}$ (shown in Figure 5a ($R^2=0.75$)) can be used to develop a simple model

$$\Delta G_{\text{OH-nitrogen}}=-1.83\ f\left(p_{z-\mathrm{N}}\right)+1.01 \tag{6}$$

### 2.6.2. Boron-Doped Graphene
We repeat the above procedure to identify a correlation between $\Delta G_{OH-boron}$ and define a function $f(p_{z-\mathrm{B}})$. Interestingly, we find that the intercept of the lines $\Delta G_{OH-boron}$ versus $O_{p_z}$ and $\Delta G_{OH-boron}$ versus $D_{p_z}(E_F)$ are approximately equal

$$\Delta G_{\text{OH-boron}}=-18.21 O_{p_{z}}+1.807 \tag{7}$$

and

$$\Delta G_{\text{OH-boron}}=-6.16 D_{p_{z}}\left(E_{\mathrm{F}}\right)+1.807 \tag{8}$$

![](./images/813070704789422081_6.jpg)

Figure 5. a) Dependence of $\Delta G_{OH-nitrogen}$ on the newly defined function $f(p_{z-\mathrm{N}})$. b) Dependence of $\Delta G_{OH-boron}$ on the $f(p_{z-\mathrm{B}})$.

Equations (7) and (8) again testify a greater sensitivity of $\Delta G_{OH}$ to $O_{p_z}$ than to $D_{p_z}(E_F)$.

With another function to capture the dependence on these two descriptors

$$f\left(p_{z-\mathrm{B}}\right)=2.95\left(O_{p_{z}}\right)+D_{p_{z}}\left(E_{\mathrm{F}}\right), \tag{9}$$

and the linear $f(p_{z-\mathrm{B}})$ versus $\Delta G_{OH-boron}$ correlation (shown in Figure 5b, $R^2=0.91$), $\Delta G_{OH}$ is

$$\Delta G_{\text{OH-boron}}=-3.51 f\left(p_{z-\mathrm{B}}\right)+1.96 \tag{10}$$

Equations (6) and (10) constitute the predictive model equations of catalytic activity to ORR with functions $f$'s as minimal descriptors. Another chemical insight can be drawn from these predictive models: $\Delta G_{OH}$ on the sites of both nitrogen and boron doped is proportional to $(f(p_{z-\mathrm{B}})+2\ f(p_{z-\mathrm{N}}))$. Based on this we plotted $\Delta G_{OH}$ as a function of $f(p_z)$, as shown in Figure 6. It has to be noted that even though nitrogen and boron doping result in shifts in the Fermi level (to the right and left, respectively) in almost identical fashions, the value of $O_{p_z}$ and $D_{p_z}(E_F)$ of boron-doped graphene should be twice as much to bring about the same $\Delta G_{OH}$ as that of nitrogen-doped graphene. Overall, we successfully define an electronic descriptor

![](./images/813070704789422081_7.jpg)

Figure 6. Dependency of $\Delta G_{\mathrm{OH}}$ as a function of general electronic descriptor function $f(\mathrm{p}_{z})$.

and model equation to define the catalytic activity of graphene-based catalyst. The proposed descriptor can be tested for other application related to $\mathrm{sp}^{2}$ hybridized carbon materials.

### 2.7. Structural Descriptors and Predictive Model
We now identify a simple structural descriptor that can be readily used to screen and identify optimal sites on multi-nitrogen/boron-doped graphene for ORR, based on the linear interpolation of $\Delta G_{\mathrm{OH}}$ of inequivalent carbon atoms on 1N and 1B configurations of doped graphene. A simple predictive model based on the structural descriptors can be used to estimate site-specific $\Delta G_{\mathrm{OH}}$ of the doped graphene.

It has been confirmed by experiment and theory that the effect of nitrogen/boron substitution is localized in triangular domains to within 1 nm in the vicinity of the dopant. $^{[45]}$ The nearest-neighbor carbon atoms (ortho sites) have the highest electron densities, which have been observed as bright spots in scanning tunneling microscopic (STM) images, followed by the para sites. $^{[46]}$ These bright spots have been attributed to electronic orbitals of the dopants and host atoms that are perpendicular to the sheet. $^{[47]}$ Since these out-of-plane $\mathrm{p}_{z}$ states affect the adsorption of ORR intermediates, it is reasonable to believe that the positions of a particular active site relative to the nitrogen dopant can be used to construct a structural descriptor for N/B-doped graphene. To this end, we first define the 1,2,3-Ortho site, 1,2,3-Meta site, and 1,2,3-Para site considering N dopant as the reference site, and use them to evaluate the structural descriptor (for details, see the Supporting Information). Let us consider a carbon atom adjacent to a single nitrogen atom as 1-Ortho (see Figure S4a, Supporting Information). Assuming that this atom does not lie in the triangular area of any other dopant, the $\Delta G_{\mathrm{OH}}$ on this site is 0.42 eV. When a carbon atom is in an ortho position to two nitrogen dopants (2-Ortho; see Figure S4b, Supporting Information), the $\Delta G_{\mathrm{OH}}$ on the same site is -0.28 eV. Interestingly, when a carbon atom is in an ortho position to three nitrogen atoms (3-Ortho; see Figure S4c, Supporting Information), the $\Delta G_{\mathrm{OH}}$ on the same site is -0.94 eV which is lower than the $\Delta G_{\mathrm{OH}}$ on 1-Ortho by $\approx 2 \times-0.68$ eV. Similarly, we consider a carbon atom at a para position to nitrogen dopant/s, as illustrated in Figure S5 (Supporting Information). As the number of nitrogen atom to which a particular carbon site is in para position (see Figure S5a-c, Supporting Information) is increased from one (named as 1-Para) to two (named as 2-Para) to three (named as 3-Para) there is a linear decrease in the $\Delta G_{\mathrm{OH}}$, with each para site by about 0.33 eV. This is also the case for adsorption at the meta site (see Figure S6a,b,c, Supporting Information, that illustrates 1-Meta, 2-Meta, and 3-Meta sites, respectively) with increase in the number of nitrogen atoms, the $\Delta G_{\mathrm{OH}}$ decreases by 0.13 eV. We note that the naming convention employed here is different from the one used earlier. Here, the labels, $n$-Ortho, $n$-Para, and $n$-Meta $(n=1,2,3)$ denote a particular active site that lies in ortho, meta, or para positions with respect to $n$ dopants.

The number of nitrogen atoms that lie in the ortho, para, and meta positions to a particular active site varies linearly with $\Delta G_{\mathrm{OH}}$ having slopes of -0.68,-0.33, and 1.09, respectively, and intercepts of 1.09 (see Figure 7c). The $R^{2}$ value in all cases is greater than 0.99. This linearity suggests that the $\Delta G_{\mathrm{OH}}$ can be predicted from just the number of ortho/meta/para sites of single-N-doped graphene (which is termed as structural descriptor). See illustration of this idea for active sites in 2N-doped graphene in Figure 7a. We now present a predictive model to estimate $\Delta G_{\mathrm{OH}}$ of the active sites in terms of structural descriptors

$$\Delta G_{\text {OH-generated(N) }}=1.09-0.13 * n_{\mathrm{M}}-0.33 * n_{\mathrm{P}}-0.68 * n_{\mathrm{O}}\tag{11}$$

Where $n_{\mathrm{M}}, n_{\mathrm{P}}$, and $n_{\mathrm{O}}$ denote the number of dopants (here nitrogen) atoms that are in meta, para, and ortho positions to a particular active site. For example, for the sites that lie in ortho position to one dopant and para position to another (indicated using the red arrows in Figure 7a), $n_{\mathrm{M}}=0, n_{\mathrm{P}}=1$, and $n_{\mathrm{O}}=1$. Hence, according to predictive model, Equation (11), this site is predicted to have a $\Delta G_{\text {OH-generated }}=0.085$ eV. This site is the earlier identified $2 \mathrm{~N}-\mathrm{C}_{3}$ site having $\mathrm{p}_{z}$ occupancy of 1.08e, which was predicted to have the optimal overpotential. Using Equation (11), we searched for an optimal active site, with $\Delta G_{\mathrm{OH}}$ of -0.15 to 0.25 eV. The site which is in para positions to three nitrogen atoms (3-Para) is indicated using a green arrow in Figure 4d whose $n_{\mathrm{M}}=0, n_{\mathrm{P}}=3$, and $n_{\mathrm{O}}=0$, and its $\Delta G_{\text {OH-generated }}$ is predicted to be 0.095 eV. Performing density functional theory (DFT) calculations on this site revealed that it had overpotential of 0.48 V, which indeed has the lowest overpotential among the sites studied. This proves that our predictive model (Equation (11)) is effective in designing optimal sites and catalysts based on graphene.

We estimated $\Delta G_{\text {OH-generated }}$ for a number of different configurations of nitrogen doping, fixing the dopant concentration to three per supercell, and compared the same with the $\Delta G_{\mathrm{OH}}$ calculated using Equation (2), terming it as $\Delta G_{\text {OH-DFT. }} \Delta G_{\text {OH-generated }}$ versus $\Delta G_{\text {OH-DFT }}$ (Figure 7d) shows a linear relation among the two parameters, with an $R^{2}$ of 0.93.

Similarly, $\Delta G_{\mathrm{OH}}$ onto the carbon atoms in the vicinity of boron dopants can be estimated from the predictive model

$$\Delta G_{\text {OH-generated(B) }}=1.611-0.13 * n_{\mathrm{M}}-0.41 * n_{\mathrm{P}}-0.72 * n_{\mathrm{O}}\tag{12}$$

$\Delta G_{\text {OH-DFT }}$ versus $\Delta G_{\text {OH-generated(B) }}\left(R^{2}=0.96\right)$ is shown in Figure S7 of the Supporting Information.

![](./images/813070704789422081_8.jpg)

$\Delta G_{\text{OH-generated}}$ versus negative of the overpotential for the various sites of nitrogen- and boron-doped graphene (see Figure 8) shows that the 3-Para site (see Figure 7b) lies at the top of the volcano having the least overpotential. The free energy profile of ORR on this site is shown in Figure 8b. At the equilibrium potential, the formation of OOH is identified to be the potential-limiting step which is uphill by 0.48 eV. The reduction of OOH to O is downhill in energy by 1.08 eV. The protonation of O to OH and the conversion of OH to $\text{H}_2\text{O}$, are each uphill by only 0.3 eV. The onset potential is hence $-0.079$ V, suggesting that this site is one of the best sites for ORR to occur with a minimum overpotential. Hence, our predictive model has the potential to identify the optimal sites for ORR, ruling out the need to perform extensive DFT calculations of free energies and overpotential for each active site, thereby greatly reducing computational effort.

### 3. Conclusions
Within density functional theory, we have identified $\text{p}_z$ electron-based descriptors for predicting catalytic activity of nitrogen-, boron-, and co-doped graphene. Specifically, we demonstrated that these descriptors have a linear correlation with the $\Delta G_{\text{OH}}$, and hence can be used as screening tools while designing electrocatalysts for ORR. From the linear correlation with $\Delta G_{\text{OH}}$ (from DFT), we identified the number of ortho/meta/para positions of an active site as the structural descriptors, and presented a simple predictive model to estimate the $\Delta G_{\text{OH}}$. Based on this predictive model, we predicted that a carbon atom located in para positions to three nitrogen atoms has the lowest overpotential of 0.48 V for ORR, and verified it with DFT calculations. These proposed descriptors can be extended to other systems with $\text{sp}^2$ hybridization, and the concept of local structural descriptor can impact a number of problems of chemical activity in heterogeneous systems like alloys, polymers, and even biomolecular systems.

### 4. Computational Techniques
We used PWscf package of the Quantum ESPRESSO distribution$^{[48]}$ in our calculations here based on the plane-wave basis and ultrasoft pseudopotentials$^{[49]}$ to model ionic cores. The Perdew–Becke–Ernzerhof$^{[50]}$ gradient-corrected functional was used to approximate the exchange and correlation energy of electrons. We find that a kinetic energy cutoff of 30 Ry for truncating the plane wave basis for wavefunctions (and of 240 Ry for the charge density) is sufficient to obtain well-converged results. A $5 \times 5 \times 1$ periodic supercell of graphene consisting of 50 carbon atoms was used in modeling B and N substitution. We sampled integrations over its Brillouin zone on a $5 \times 5 \times 1$ uniform mesh of $k$-points, smearing the discontinuity in occupation numbers of electronic states with Marzari–Vanderbilt smearing method.$^{[51]}$ A 56 atom graphene nanoribbon was chosen to study the effect of edges, employing a $K$ point mesh of $1 \times 7 \times 1$. Since the parameters derived from the projected density of states are sensitive to the specific orbitals used in

![](./images/813070704789422081_9.jpg)

Figure 8. a) Volcano plot of $\Delta G_{\mathrm{OH}}$-generated versus negative of the overpotential of each active site (including the 3-Para site as found from the predictive model equation) of the different nitrogen- and boron-doping configurations of graphene. This plot helps to describe the role of predictive model equation to find new catalytic active site in a very simple way. b) Free energy profile of ORR on the 3-Para site that is identified to be the optimal site for ORR.

projection scheme and the structure, we used a spilling parameter ($S$) as an estimate of how well the pseudo-atomic orbital basis represents the eigenstates of the crystalline lattice$^{[52]}$

$$
S=\frac{1}{N_{k}} \frac{1}{N_{\alpha}} \sum_{k}^{N_{k}} \sum_{\alpha=1}^{N_{\alpha}}\left\langle\psi_{\alpha}(\boldsymbol{k})\left|(1-P(\boldsymbol{k}))\right| \psi_{\alpha}(\boldsymbol{k})\right\rangle
\tag{13}
$$

where $|\psi_{\alpha}(k)\rangle$ are the Bloch eigenstates, $N_{k}$ and $N_{\alpha}$ denote the number of $k$ points in the Brillouin zone and the number of bands considered, respectively. $P(k)$ is the projector operator onto the atomic orbital basis. Thus, $S$ is a measure of the difference between the $|\psi_{\alpha}(k)\rangle$'s in plane-wave basis and their projection into the basis of atomic orbitals, $P(k)|\psi_{\alpha}(k)\rangle$. Thus, $S$ can take a minimum value of 0 indicating that the atomic wave functions reproduce the eigenfunctions exactly, and a maximum value of 1 (the basis is orthogonal to the Hamiltonian eigenstates).

From this projection onto atomic orbitals at various sites, we found that the spilling parameters were always less than 0.015, implying that more than 98.5% of the energy eigenstates are included in the subspace spanned by the atomic basis. This validates the accuracy of this projection scheme used in identification of electronic descriptors.

## Supporting Information
Supporting Information is available from the Wiley Online Library or from the author.

## Acknowledgements
R.T. and S.S. thank Science and Engineering Research Board (SERB), India, for the financial support (Grant Nos. SB/FTP/PS028/2013 and EMR/2016/004689). R.T. thanks Ministry of New and Renewable Energy (MNRE), India, for the financial support (Grant No. 31/03/2014-15/PVSE-R&D). R.T. and S.S. also thank SRM Research Institute, SRM University, for providing supercomputing facilities. R.T. thanks Prof. Shobhana Narasimhan of Jawaharlal Nehru Centre for Advanced Scientific Research, Bangalore, India, for her initial suggestion in defining the descriptor. U.V.W. acknowledges support from the India-Korea Science and Technology Center and an AOARD project no. FA 2386-15-1-0002.

## Conflict of Interest
The authors declare no conflict of interest.

## Keywords
adsorption, descriptor, DFT, electrocatalysts, ORR

Received: October 15, 2017
Revised: November 11, 2017
Published online:

[1] A. Holewinski, J.-C. Idrobo, S. Linic, *Nat. Chem.* **2014**, 6, 828.
[2] D. Geng, N. Ding, T. S. Andy Hor, Z. Liu, X. Sun, Y. Zong, *J. Mater. Chem. A* **2015**, 3, 1795.
[3] L. K. Putri, B.-J. Ng, W.-J. Ong, H. W. Lee, W. S. Chang, S.-P. Chai, *ACS Appl. Mater. Interfaces* **2017**, 9, 4558.
[4] L. K. Putri, W.-J. Ong, W. S. Chang, S.-P. Chai, *Appl. Surf. Sci.* **2015**, 358, 2.
[5] Z. Zhang, T. Cao, S. Liu, X. Duan, L.-M. Liu, S. Wang, Y. Liu, *Part. Part. Syst. Charact.* **2017**, 34, 1600207.
[6] H. Cui, Z. Zhou, D. Jia, *Mater. Horiz.* **2017**, 4, 7.
[7] J. Ko, H. Kwon, H. Kang, B.-K. Kim, J. W. Han, *Phys. Chem. Chem. Phys.* **2015**, 17, 3123.
[8] N. İnoğlu, J. R. Kitchin, *Phys. Rev. B* **2010**, 82, 45414.
[9] Z. W. Seh, J. Kibsgaard, C. F. Dickens, I. Chorkendorff, J. K. Nørskov, T. F. Jaramillo, *Science* **2017**, 355, eaad4998.
[10] F. H. B. Lima, J. Zhang, M. H. Shao, K. Sasaki, M. B. Vukmirovic, E. A. Ticianelli, R. R. Adzic, *J. Phys. Chem. C* **2007**, 111, 404.
[11] C. Tsai, K. Chan, J. K. Nørskov, F. Abild-Pedersen, *J. Phys. Chem. Lett.* **2014**, 5, 3884.
[12] I. C. Man, H.-Y. Su, F. Calle-Vallejo, H. A. Hansen, J. I. Martínez, N. G. Inoglu, J. Kitchin, T. F. Jaramillo, J. K. Nørskov, J. Rossmeisl, *ChemCatChem* **2011**, 3, 1159.
[13] K. Toyoda, R. Hinogami, N. Miyata, M. Aizawa, *J. Phys. Chem. C* **2015**, 119, 6495.

[14] A. Grimaud, K. J. May, C. E. Carlton, Y.-L. Lee, M. Risch, W. T. Hong, J. Zhou, Y. Shao-Horn, *Nat. Commun.* 2013, 4, 2439.

[15] Y. Jiao, Y. Zheng, M. Jaroniec, S. Z. Qiao, *J. Am. Chem. Soc.* 2014, 136, 4394.

[16] Z. Zhao, M. Li, L. Zhang, L. Dai, Z. Xia, *Adv. Mater.* 2015, 27, 6834.

[17] S. Nandhini, A. Rajkamal, B. Saha, R. Thapa, *Mol. Catal.* 2017, 432, 242.

[18] P. Wang, Z. Wang, L. Jia, Z. Xiao, *Phys. Chem. Chem. Phys.* 2009, 11, 2730.

[19] S. Ni, Z. Li, J. Yang, *Nanoscale* 2012, 4, 1184.

[20] L. Yang, S. Jiang, Z. Zhao, L. Zhu, S. Chen, X. Wang, Q. Wu, J. Ma, Y. Ma, Z. Hu, *Angew. Chem., Int. Ed.* 2011, 50, 7132.

[21] J. Bhattacharjee, *J. Phys. Chem. Lett.* 2015, 6, 1653.

[22] S. Sinthika, R. Thapa, *RSC Adv.* 2015, 5, 93215.

[23] P. Błoński, J. Tuček, Z. Sofer, V. Mazánek, M. Petr, M. Pumera, M. Otyepka, R. Zbořil, *J. Am. Chem. Soc.* 2017, 139, 3171.

[24] B. Hammer, J. K. Norskov, *Adv. Catal.* 2000, 45, 71.

[25] J. K. Nørskov, J. Rossmeisl, A. Logadottir, L. Lindqvist, J. R. Kitchin, T. Bligaard, H. Jónsson, *J. Phys. Chem. B* 2004, 108, 17886.

[26] V. Stamenkovic, B. S. Mun, K. J. J. Mayrhofer, P. N. Ross, N. M. Markovic, J. Rossmeisl, J. Greeley, J. K. Nørskov, *Angew. Chem., Int. Ed.* 2006, 45, 2897.

[27] J. Suntivich, H. A. Gasteiger, N. Yabuuchi, H. Nakanishi, J. B. Goodenough, Y. Shao-Horn, *Nat. Chem.* 2011, 3, 546.

[28] S. J. Hwang, S. J. Yoo, J. Shin, Y.-H. Cho, J. H. Jang, E. Cho, Y.-E. Sung, S. W. Nam, T.-H. Lim, S.-C. Lee, S.-K. Kim, *Sci. Rep.* 2013, 3, 1309.

[29] H. Zhuang, A. J. Tkalych, E. A. Carter, *J. Phys. Chem. C* 2016, 120, 23698.

[30] R. Jacobs, J. Booske, D. Morgan, *Adv. Funct. Mater.* 2016, 26, 5471.

[31] F. Calle-Vallejo, J. Tymoczko, V. Colic, Q. H. Vu, M. D. Pohl, K. Morgenstern, D. Loffreda, P. Sautet, W. Schuhmann, A. S. Bandarenka, *Science* 2015, 350, 185.

[32] J. Zhang, Z. Zhao, Z. Xia, L. Dai, *Nat. Nanotechnol.* 2015, 10, 444.

[33] Y. Jiao, Y. Zheng, K. Davey, S.-Z. Qiao, *Nat. Energy* 2016, 1, 16130.

[34] Y. Okamoto, *Appl. Surf. Sci.* 2009, 256, 335.

[35] N. Zhang, F. Y. Chen, X. Q. Wu, *Sci. Rep.* 2015, 5, 11984.

[36] D. Shin, S. Sinthika, M. Choi, R. Thapa, N. Park, *ACS Catal.* 2014, 4, 4074.

[37] S. Trasatti, *Electrochim. Acta* 1984, 29, 1503.

[38] P. Atkins, J. Paula, *Atkins' Physical Chemistry*, W. H. Freeman And Company, New York 2006.

[39] J. Zhang, Z. Zhao, Z. Xia, L. Dai, *Nat. Nanotechnol.* 2015, 10, 444.

[40] J. R. Kitchin, J. K. Nørskov, M. A. Barteau, J. G. Chen, *J. Chem. Phys.* 2004, 120, 10240.

[41] D. Sen, R. Thapa, K. K. Chattopadhyay, *ChemPhysChem* 2014, 15, 2542.

[42] A. K. Manna, S. K. Pati, *J. Phys. Chem. C* 2011, 115, 10842.

[43] H. Lin, G. Fratesi, G. P. Brivio, *Phys. Chem. Chem. Phys.* 2015, 17, 2210.

[44] H. Kim, K. Lee, S. I. Woo, Y. Jung, *Phys. Chem. Chem. Phys.* 2011, 13, 17505.

[45] R. Lv, Q. Li, A. R. Botello-Méndez, T. Hayashi, B. Wang, A. Berkm demir, Q. Hao, A. L. El as, R. Cruz-Silva, H. R. Gutiérrez, Y. A. Kim, H. Muramatsu, J. Zhu, M. Endo, H. Terrones, J.-C. Charlier, M. Pan, M. Terrones, *Sci. Rep.* 2012, 2, 586.

[46] L. Zhao, R. He, K. T. Rim, T. Schiros, K. S. Kim, H. Zhou, C. Gutierrez, S. P. Chockalingam, C. J. Arguello, L. Palova, D. Nordlund, M. S. Hybertsen, D. R. Reichman, T. F. Heinz, P. Kim, A. Pinczuk, G. W. Flynn, A. N. Pasupathy, *Science.* 2011, 333, 999.

[47] S.-O. Guillaume, B. Zheng, J.-C. Charlier, L. Henrard, *Phys. Rev. B* 2012, 85, 35444.

[48] P. Giannozzi, S. Baroni, N. Bonini, M. Calandra, R. Car, C. Cavazzoni, D. Ceresoli, G. L. Chiarotti, M. Cococcioni, I. Dabo, A. Dal Corso, S. de Gironcoli, S. Fabris, G. Fratesi, R. Gebauer, U. Gerstmann, C. Gougoussis, A. Kokalj, M. Lazzeri, L. Martin-Samos, N. Marzari, F. Mauri, R. Mazzarello, S. Paolini, A. Pasquarello, L. Paulatto, C. Sbraccia, S. Scandolo, G. Sclauzero, A. P. Seitsonen, A. Smogunov, P. Umari, R. M. Wentzcovitch, *J. Phys.: Condens. Matter* 2009, 21, 395502.

[49] D. Vanderbilt, *Phys. Rev. B* 1990, 41, 7892.

[50] J. P. Perdew, K. Burke, M. Ernzerhof, *Phys. Rev. Lett.* 1996, 77, 3865.

[51] N. Marzari, D. Vanderbilt, A. De Vita, M. C. Payne, *Phys. Rev. Lett.* 1999, 82, 3296.

[52] D. Sanchez-Portal, E. Artacho, J. M. Soler, *Solid State Commun.* 1995, 95, 685.

*Small* 2017, 1703609

1703609 (10 of 10)

© 2017 WILEY-VCH Verlag GmbH & Co. KGaA, Weinheim
View Article Online
View Journal

PCCP

Accepted Manuscript

This article can be cited before page numbers have been issued, to do this please use: Z. Xia, X. Chen, W. Zhang, J. Li, B. Xiao and H. Du, *Phys. Chem. Chem. Phys.*, 2018, DOI: 10.1039/C8CP03803A.

![](./images/813000637632479232_1.jpg)

This is an Accepted Manuscript, which has been through the Royal Society of Chemistry peer review process and has been accepted for publication.

Accepted Manuscripts are published online shortly after acceptance, before technical editing, formatting and proof reading. Using this free service, authors can make their results available to the community, in citable form, before we publish the edited article. We will replace this Accepted Manuscript with the edited and formatted Advance Article as soon as it is available.

You can find more information about Accepted Manuscripts in the author guidelines.

Please note that technical editing may introduce minor changes to the text and/or graphics, which may alter content. The journal's standard Terms & Conditions and the ethical guidelines, outlined in our author and reviewer resource centre, still apply. In no event shall the Royal Society of Chemistry be held responsible for any errors or omissions in this Accepted Manuscript or any consequences arising from the use of any information it contains.

![](./images/813000637632479232_2.jpg)

rsc.li/pccp

# Boosted Lithium-ion hopping on halogen-doped $\chi_3$ borophene

Zihan Xia$^{a}$, Xianfei Chen$^{a,b*}$, Wentao Zhang$^{a}$, Junfeng Li$^{a}$, Beibei Xiao$^{c}$, Haiying Du$^{a*}$

$^{a}$ College of Materials and Chemistry & Chemical Engineering, Chengdu University of Technology, Chengdu 610059, China

$^{b}$ Postdoctoral Innovation Practice Base, Sichuan Konkasnow New Material Co., Ltd., Yaan 625400, China

$^{c}$ School of Energy and Power Engineering, Jiangsu University of Science and Technology, Zhenjiang 212003, China

## Abstract

Borophenes, two-dimensional boron counterparts with the three synthetic polymorphs T, $\beta_{12}$ and $\chi_3$ borophene, have been predicted to be potential anode materials for Li-ion batteries with extremely high capacities. However, Li hopping on $\beta_{12}$ and $\chi_3$ borophenes is quite slow with high energy barriers (around 0.6 eV), preventing the application of these borophenes in the fast charging realm. Here, we propose to use halogen functionalization to boost the sluggish Li-ion diffusion dynamics in borophenes by employing $\chi_3$ borophene as a prototype system. Halogens bind strongly to $\chi_3$ borophene with substantial electron transfer from the latter to the former, leading to local electron deficiency in $\chi_3$ borophene. Synergism of electron extraction from $\chi_3$ borophene and electrostatic attraction between halogens and Li results in enhanced affinity between $\chi_3$ borophene and Li and a reduced Li-ion hopping barrier. Iodine is the preferred dopant where most diffusion paths exhibit energy barriers typically smaller than 0.2 eV. Our results suggest that halogen incorporation could facilitate intercalation and deintercalation of Li-ions in borophene-based anode materials.

Keywords: borophene; density functional theory; halogen functionalization; lithium-ion batteries; Li-ion hopping barrier

* Corresponding author. Email: [chenxianfei2014@cdut.edu.cn](mailto:chenxianfei2014@cdut.edu.cn); [diane201109@126.com](mailto:diane201109@126.com)

### I. Introduction

Development of new energy technologies is expected to open promising ways to alleviate energy and environmental concerns. $^{1}$ However, the intermittent feature and randomness of the state-of-the art renewable energies including solar energy, wind energy, tidal energy and water energy, $^{2}$ prevent their direct integration into power grids and lead to waste due to insufficient energy consumption. This drawback could be overcome by energy storage technologies, *i.e.* lithium-ion batteries (LIBs), which also meet the demands of the ever-increasing numbers of electric vehicles and portable electrics. $^{3,4}$ LIBs are thus expected to provide high specific capacities, favorable reversibility and especially fast charging rates to meet the rapid development and high energy yield of the new energy industry $^{5,6}$.

The general setup of ion batteries comprises a separator, an electrolyte and two electrodes, of which the latter determine the capacity and rate performance of batteries $^{7}$. Compared with the rapid advance of cathode host materials, $^{8}$ the development of anode material lags behind and only graphite has been commercialized to date. $^{9}$ In this respect, much attention has been devoted to search for new anode materials with favorable electrochemical performances. $^{10}$ Benefiting from the unique structure of two-dimensional (2D) materials, advantageous features like large specific surface area, quantum confinement, substantial number of adsorption sites, high flexibility and relatively small volume changes could be achieved, which are essential for developing batteries with high capacity and reversibility $^{11,12}$. To this end, 2D-based anode materials including graphene $^{13,14}$, silicene $^{15,16}$, MXenes $^{17,18}$, transition metal sulfide $^{19,20}$, phosphorene polymorphs $^{21-23}$ and other hybrid materials $^{24,25}$ have been extensively explored. These achievements provided important insights into our understanding of the electrochemical mechanism of metal-ion intercalation and deintercalation, and enriched our knowledge about the configuration-performance relationship of electrode materials $^{26}$.

Recently, borophene has emerged as a new kind of elemental 2D material with different theoretically predicted isomers and three of them, *i.e.*, T, $\beta_{12}$ and $\chi_{3}$

borophenes, have been synthetized via vapor deposition $^{27,28}$. By virtue of the low relative atomic mass of boron in addition to the desired mechanical strength $^{29}$ and conductance, borophene holds great potential as anode material in LIBs to reach high theoretical capacities $^{30,31}$. Jiang et al. $^{32}$ reported a theoretical capacity of 1860 mA h $\mathrm{g}^{-1}$ referring to $\mathrm{Li}_{0.75} \mathrm{B}$ for T borophene with anisotropic hopping barriers along the ravine direction (0.0026 eV) and the ridge direction (0.33 eV). The high capacity and shallow migration barrier of Li along the ravine direction beneficial for its application in the fast charging realm and help in part to overcome the problem of mismatching energy yield and consumption. The electrochemical properties of $\beta_{12}$ and $\chi_{3}$ borophenes have also been investigated Zhang et al. $^{33}$, who reported a capacity of 1984 mA h $\mathrm{g}^{-1}$ for $\beta_{12}$ borophene and 1240 mA h $\mathrm{g}^{-1}$ for $\chi_{3}$ borophene. Unfortunately, the hopping dynamics of Li-ion on $\beta_{12}$ and $\chi_{3}$ borophenes are quite poor with extremely high energy barriers of $0.66 \sim 0.81$ eV in $\beta_{12}$ borophene $^{33,34}$ and $0.60 \sim 0.85$ eV on $\chi_{3}$ borophene $^{33}$. In light of the ever-increasing demand for fast-charging technology and given the fundamental challenges to experimentally isolate T borophene from $\beta_{12}$ and $\chi_{3}$ borophenes, identifying new approaches to reduce the hopping barrier for Li hopping on $\chi_{3}$ borophenes is necessary.

In our previous work, we demonstrated that the sluggish hopping dynamic of Li hopping on borophene stem from the weak substrate bonding of Li in the transition state, which could be improved by hole/electron doping. $^{35}$ Motivated by the strong tendency of halogen atoms $^{36}$ to attract electrons from borophene, employing $\chi_{3}$ borophene as a prototype system, we propose halogen decoration as an experimentally feasible method to facilitate Li-ion migration in $\chi_{3}$ borophene. Possible adsorption sites and bonding interactions between the halogen and $\chi_{3}$ borophene were investigated to determine the ground state configurations. Insights into the electronic structure modulation of $\chi_{3}$ borophene have been gained by using projected density of states and charge difference analysis. Subsequent Li-ion adsorption and hopping on X-$\chi_{3}$ borophene (X = F, Cl, Br or I) have been studied and compared with pristine $\chi_{3}$ borophene. We determined that not only the electron deficiency environment in $\chi_{3}$ borophene but also the strong electrostatic interactions between Li-ion and the

halogen atom contribute to the hopping dynamic of Li-ion. The mechanisms revealed may facilitate the development of new anode materials with improved rate performances.

## II. Methods
All calculations were carried out using density functional theory as implemented in the Dmol³ module, in which numerical functions on an atom-centered grid are employed as the atomic basis. Spin-restricted calculations were performed because the considered systems have nonmagnetic ground states according to our test results. The generalized gradient approximation (GGA) and the Perdew-Burke-Ernzerhof (PBE) formula were selected to describe the electron exchange correlation interaction.³⁷ Van der waals interactions are taken into account by using the DFT-D2 method.³⁸ A smearing of 0.002Ha is adopted for convergence. All-electron core treatment and double-numeric plus polarization (DNP) were applied. A supercell (2 × 3) containing 49 atoms was used to investigate pristine and halogen-doped borophene. A vacuum separation of adjacent layers of >15 Å was used to attenuate the interactions between layers by employing periodic boundary conditions. The energy, force, and displacement convergence criteria for geometry optimization were set to 1.0×10⁻⁵ Ha, 0.002 Ha Å⁻¹, and 0.005 Å, respectively. Integrated density of states analysis has been implemented to quantify the charge exchange between the halogen atoms and ${\chi}_{3}$ borophene. The minimum energy paths (MEPs) for Li-ion hopping were determined using the LST/QST tools in the Dmol³ code. This method has been well validated to determine the transition state (TS) structure.³⁹,⁴⁰ The root-mean-square (RMS) convergence for TS search was set to 0.002 Ha Å⁻¹. The Brillouin zone (BZ) was sampled by a 7 × 7 k-point mesh.

The adsorption and binding energies of the halogen atoms on ${\chi}_{3}$ borophene were obtained by using the following formulas:
$$
E_{\text{ad}} = E_{\text{X-}\chi 3} - \mu_{\text{X}} - E_{\chi 3} \tag{1}
$$
$$
E_{\text{b}} = E_{\text{X-}\chi 3} - E_{\text{X}} - E_{\chi 3} \tag{2}
$$
where $E_{\chi 3}$, $E_{\text{X}}$ and $E_{\text{X-}\chi 3}$ are the total energy of pristine ${\chi}_{3}$ borophene, isolated halogen

atoms and halogenated $\chi_3$ borophene, respectively. $\mu_X$ refers to the chemical potential of the halogen atoms derived from the corresponding diatomic molecules.

### III. Results and discussion

#### A. Halogen atom adsorption on $\chi_3$ borophene

$\chi_3$ borophene is a perfectly planar boron sheet without any buckling, which can be characterized by narrow zigzag boron rows separated by continuous hole chains. The holes in $\chi_3$ borophene consist of six boron atoms arranged in the shape of a hexagon, in analogy to graphene. The calculated lattice parameters of $\chi_3$ borophene are a = 8.41 Å and b = 2.93 Å, in agreement with previous theoretical and experimental results$^{41}$. To determine the ground state configuration of halogen atoms on $\chi_3$ borophene, several suitable adsorption sites have been considered as illustrated in Figure 1. Considering the structural symmetry of $\chi_3$ borophene, these sites could be classified as bridge, hollow and atop sites, labeled as B, H and T, respectively. To reduce the coupling between X atoms (X = F, Cl, Br or I) in adjacent images, we adopted a 2 × 3 supercell with the lattice parameters a = 16.82 Å and b = 8.78 Å, corresponding to a halogen concentration of 2.04 %. The energetically most favorable adsorption sites for all considered halogen atoms were T2 sites due to their highest $E_\text{ad}$ values. Calculated $E_\text{ad}$ values and geometric parameters are listed in Table 1. $E_\text{ad}$ values decrease from F to I along with the elongated bond length of B-X ($l_\text{B-X}$). This trend is also reflected by the decrease in the $\Delta h$ value from 0.75 to 0.42 Å. $\Delta h$ is defined as the lifting height of B atom from the $\chi_3$ borophene plane, and the value of $\Delta h$ is determined by the attractive forces of halogens X to the underlying B atoms. In addition, $E_\text{ad}$ values for all halogen atoms adsorbed onto $\chi_3$ borophene are negative suggesting that halogenation of $\chi_3$ borophene is an exothermic process. It is important to note that these calculated $E_\text{ad}$ values are smaller than the analog values reported for T borophene$^{42}$, which is in line with the higher stability of $\chi_3$ borophene. However, these values are much larger than those reported for halogen atoms adsorbed onto graphene, indicating the great potential of halogenated $\chi_3$ borophene, which is further supported by the successful experimental fabrication of halogenated graphene$^{43}$.

![](./images/813000637632479232_3.jpg)

Figure 1. (a) Adsorption sites considered for X (X = F, Cl, Br or I) on $\chi_3$ borophene. T, B, and H indicate that X adsorbed on the top of the B atoms, between the B-B bridge site and above the center of the triangle or hexagon, respectively. (b) Side view of the $2\times3$ $\chi_3$ borophene with X residing on the energetically most favorable T2 site.

Table 1. Calculated adsorption energy ($E_{\text{ad}}$), binding energy ($E_{\text{b}}$), bonding length of B and X atoms ($l_{\text{B-X}}$), charges transferred to X atoms ($\Delta q$) and lifting height of B from $\chi_3$ plane ($\Delta h$) for X adsorbed at the T2 site.

<table>
  <thead>
    <tr>
      <th>Atom</th>
      <th>$E_{\text{ad}}$(eV)</th>
      <th>$E_{\text{b}}$(eV)</th>
      <th>$l_{\text{B-X}}$ (Å)</th>
      <th>$\Delta q$(e)</th>
      <th>$\Delta h$(Å)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>F</td>
      <td>−3.47</td>
      <td>−4.71</td>
      <td>1.40</td>
      <td>−0.37</td>
      <td>0.75</td>
    </tr>
    <tr>
      <td>Cl</td>
      <td>−1.59</td>
      <td>−2.91</td>
      <td>1.86</td>
      <td>−0.24</td>
      <td>0.67</td>
    </tr>
    <tr>
      <td>Br</td>
      <td>−1.32</td>
      <td>−2.37</td>
      <td>2.07</td>
      <td>−0.23</td>
      <td>0.53</td>
    </tr>
    <tr>
      <td>I</td>
      <td>−1.04</td>
      <td>−1.93</td>
      <td>2.34</td>
      <td>−0.12</td>
      <td>0.42</td>
    </tr>
  </tbody>
</table>

### B. Electronic interactions between halogen atoms and $\boldsymbol{\chi_3}$ borophene

In $\chi_3$ borophene, each B atom lies in the vertex of a triangle or hexagon although boron possesses only three valence electrons. Due to the electron deficiency of B compared with C, B forms multi-center bonds and its in-plane $sp^2$ anti-bonding states, *i.e.*, frontier molecular orbitals, are partially occupied $^{44,45}$. Consequently, electrons could easily transfer into or out of $\chi_3$ borophene to modify its affinity to Li-ion, as demonstrated in our previous work$^{35}$. As shown in Table 1, about 0.37 e, 0.24 e, 0.23 e and 0.12 e are extracted from $\chi_3$ borophene by F, Cl, Br and I atoms, respectively, and this tendency is in good agreement with the halogens' electronegativity trend. Similar observations have also been reported for halogenated T borophene$^{42}$ while $\Delta q$ values of halogenated $\chi_3$ borophene are much smaller than those of halogenated T borophene, partially due to the enhanced stability of $\chi_3$ borophene. Plots of the electron density

difference (Figure 2a), defined as $\Delta \rho = \rho_{\text{X-borophene}} - \rho_{\text{X}} - \rho_{\text{borophene}}$ ($\rho_{\text{X-borophene}}$, $\rho_{\text{X}}$ and $\rho_{\text{borophene}}$ represent electron density of X-borophene, X atom and $\chi_3$ borophene, respectively), imply that the transferred electrons mainly increase the electron density on F atom, suggesting that strong electrostatic interactions dominate the bonding of X to $\chi_3$ borophene. However, the amount of electrons sliding to the middle of B-X increases down the group of halogens. Consequently, I atom functionalized $\chi_3$ borophene exhibits a higher covalent bonding ratio as shown in Figure 2a-d.

![](./images/813000637632479232_4.jpg)

Figure 2. Electron density difference profiles of $2 \times 3$ $\chi_3$ borophene doped with (a) F, (b) Cl, (c) Br, and (d) I. Blue and yellow areas represent electron accumulation and depletion, respectively.

To determine the effects of halogenation on the electronic conductivity of $\chi_3$ borophene and shed light on the bonding mechanism between halogen atoms and $\chi_3$ borophene, partial density of states (PDOS) have been calculated and are illustrated in Figure 3. PDOS analysis revealed that the orbital contributions of the halogen atoms at the Fermi level increase gradually from F atom to I atom. As shown in Figure 3a, weak orbital hybridization between F-$2p$ and B-$2p$ could be observed at the Fermi level in addition to some weak hybridization peaks found at low-lying energy levels. This indicates that the bonding of F atom to $\chi_3$ borophene occurs mainly through electrostatic attraction, which is consistent with the electron density difference analysis. In contrast, orbital hybridization at the Fermi level increases down the group of halogens along with an enhanced contribution of covalent bonding, as shown in Figure 3b-d. In the meantime, the energetically low hybridization peaks of the $p$-orbitals shift toward higher energies, which means that the system becomes energetically less favorable in line with the reduced $E_{\text{b}}$ value. In addition, the metallic feature of $\chi_3$ borophene is preserved upon halogenation with a considerable number of

electronic states pinned at the Fermi level, guaranteeing the desired conductance for an application, as electrode material.

![](./images/813000637632479232_5.jpg)

Figure 3. Calculated partial density of states of $\chi_3$ borophene decorated with (a) F, (b) Cl, (c) Br and (d) I at the T2 site.

### C. Lithium adsorption on halogenated $\chi_3$ borophene
Incorporation of halogen atoms breaks the symmetry of $\chi_3$ borophene, thus increasing the number of unequal Li adsorption sites with respect to pristine $\chi_3$ borophene. Nevertheless, Li atom still prefer to occupy the hollow sites of $\chi_3$ borophene as shown in Figure 4. However, many metastable adsorption sites emerge (still above the hollow sites), which can be identified by their different distances to the X atom. Generally, hollow sites close to X atom are energetically more favorable than those located at a larger distance as shown in Figure 4b. The most stable hollow site lies in the H1 site except for I atom functionalized $\chi_3$ borophene where the energetically most favorable site is H5. The corresponding $E_{\text{ad}}$ values (Table 2) are $-1.71$, $-1.74$, $-1.76$ and $-1.69$ eV for $\chi_3$ borophene decorated with F, Cl, Br and I atoms, respectively, which are all larger than those of pristine $\chi_3$ borophene $(-1.43$ eV$)^{33}$. A decline trend of $E_{\text{ad}}$ for an increasing distance of Li-ion to X atom, which converges to that of pristine $\chi_3$ borophene, has been determined. As shown in Figure 4, a rapid decrease of $E_{\text{ad}}$ is observed with $d < 4.5$ Å for all halogenated $\chi_3$ borophenes. However, for those with $d > 4.5$ Å, the $E_{\text{ad}}$ values are no longer sensitive to the increase of $d$ although they are still a little larger than $-1.43$ eV. Consequently, the

effects of halogen atoms on Li adsorption are expected to be local, as an enhanced affinity to Li could only be determined at sites close to halogen atoms. This enhanced affinity can be attributed to two factors: localized electron deficiency of $\chi_3$ borophene due to electron extraction from substrate to halogens, as demonstrated in our previous work$^{35}$ and electrostatic attraction between Li-ion and X atoms. The calculated net charges of Li-ion, B atoms and X atoms for Li-ion adsorbed on pristine and halogenated $\chi_3$ borophene (Table 3) reveal that the accumulated charges on B atom decrease due to the strong electron attraction of X atom, resulting in local electron deficiency in $\chi_3$ borophene. Then, more electrons are transferred from Li-ion to $\chi_3$ borophene and the X atoms. To this end, enhanced ionic interactions between Li-ion and halogenated $\chi_3$ borophene could be determined with $E_{\text{ad}}$ values obviously larger than that of pristine $\chi_3$ borophene. The inverse correlation between electrostatic interaction and distance $d$ also rationalizes our observation that $E_{\text{ad}}$ is sensitive to $d$ ($d$ < 4.5), as shown in Figure 4b. In addition, increased energy release for Li intercalation in halogenated $\chi_3$ borophene helps to avoid the formation of metallic dendrites during battery operation and to achieve high capacities.

![](./images/813000637632479232_6.jpg)

Figure 4. (a) Li adsorption sites on halogenated $\chi_3$ borophene; (b) relationship between the distance of Li and halogens and $E_{\text{ad}}$ of Li on halogenated $\chi_3$ borophene.

Table 2. Adsorption energy ($E_{\text{ad}}$), bond length between Li and nearest B ($l_{\text{B-Li}}$) and bond length between B atom and X atoms ($l_{\text{B-X}}$) are given for Li adsorbed in the halogenated $\chi_3$ borophene.

<table>
  <thead>
    <tr>
      <th>Doped atoms</th>
      <th>$E_{\text{ad}}$(eV)</th>
      <th>$l_{\text{B-Li}}$ (Å)</th>
      <th>$l_{\text{B-X}}$ (Å)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>F</td>
      <td>−1.71</td>
      <td>2.32</td>
      <td>1.51</td>
    </tr>
    <tr>
      <td>Cl</td>
      <td>−1.74</td>
      <td>2.34</td>
      <td>2.00</td>
    </tr>
    <tr>
      <td>Br</td>
      <td>−1.76</td>
      <td>2.42</td>
      <td>2.22</td>
    </tr>
    <tr>
      <td>I</td>
      <td>−1.69</td>
      <td>2.44</td>
      <td>2.51</td>
    </tr>
  </tbody>
</table>

Table 3. Transferred charges ($\Delta q$) in Li, B and X (X =F, Cl, Br or I) atoms for Li absorbed on pristine $\chi_3$ and X-$\chi_3$(X-doped $\chi_3$ borophene).

<table>
  <thead>
    <tr>
      <th>$\Delta q$ (e)</th>
      <th>$\chi_3$</th>
      <th>F-$\chi_3$</th>
      <th>Cl-$\chi_3$</th>
      <th>Br-$\chi_3$</th>
      <th>I-$\chi_3$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Li</td>
      <td>0.688</td>
      <td>0.752</td>
      <td>0.731</td>
      <td>0.717</td>
      <td>0.706</td>
    </tr>
    <tr>
      <td>B</td>
      <td>−0.297</td>
      <td>−0.23</td>
      <td>−0.282</td>
      <td>−0.283</td>
      <td>−0.29</td>
    </tr>
    <tr>
      <td>X</td>
      <td>—</td>
      <td>−0.49</td>
      <td>−0.34</td>
      <td>−0.31</td>
      <td>−0.23</td>
    </tr>
  </tbody>
</table>

### D. Li-ion migration on doped borophene

Li-ion hopping barriers on the surfaces of electrode materials are involved in the charging and discharging rates of ion batteries, which are highly desired in energy storage-related applications.⁴⁶ To determine the effects of halogen decoration on the mobility of Li-ion on $\chi_3$ borophene, diffusion barriers of Li-ion ($E_{\text{bar}}$) along the elementary migration pathways have been calculated. Three types of typical migration pathways for Li-ion were considered according to the structural symmetry of halogenated $\chi_3$ borophene (Figure 5a-c): (i) Li-ion hopping from hexagonal centers at larger distances to the halogen to a center nearby; (ii) Li-ion migration between the closest hexagonal centers; (iii) Li-ion hopping from the closest hexagonal centers to those at larger distances (inverse migration compared with i). For comparison, the barriers for Li-ion hopping on pristine $\chi_3$ borophene were also considered as indicated in Figure 5d. Very similar energy barriers of 0.57 and 0.61 eV have been calculated for hopping along the vertical (Path I) and horizontal directions (Path II), respectively. Our obtained $E_{\text{bar}}$ values are in accordance with other reported values³³. Noteworthily, the incorporation of van der waals correction is important to determine the hopping barrier, or $E_{\text{bar}}$ of only 0.47 and 0.48 eV could be determined.³⁵ In Figure 6, $E_{\text{bar}}$ values calculated for halogen atoms functionalized $\chi_3$ borophene are summarized. Along path i, Li-ion hopping on all halogen decorated $\chi_3$ borophene are more dexterous with lower barriers in contrast to those on the pristine one (0.57 and 0.61 eV) as shown in Figure 6a. Taking F-doped $\chi_3$ borophene as an example, the barriers of Li-ion migration from the sites H2, H3, H4, H5 and H7 to H1 decreased by 25.8 ~ 77.0 % compared with Li-ion migration on undoped $\chi_3$ borophene. The decline of $E_{\text{bar}}$ is more

evident in I-decorated $\chi_3$ borophene, where most of the energy barriers are even shallower than 0.2 eV and thus lower than those on graphene $(0.31\ \mathrm{eV})^{47}$ and silicene $(0.23\ \mathrm{eV})^{48}$, while comparable to those on $\mathrm{MoS}_2\ (0.21\ \mathrm{eV})^{39}$. The origins of the boosted hopping dynamics of Li-ion on halogen decorated $\chi_3$ borophene are rather complex as two different factors are involved. The first one can be attributed to the electrostatic attraction between Li-ion and the halogen atoms, which drives the Li-ion to reside above the centers of the boron hexagons close to the halogens. Consequently, the halogen atoms incorporated into borophene can act as Li-ion "captors" by providing an attractive force to surrounding Li-ions and pulling Li-ions at larger distances toward the hexagonal centers in close proximity with low energy barriers. The second factor may be due to the charge transfer from $\chi_3$ borophene to the halogen atoms, causing electron deficiency in borophene. As demonstrated in our previous work, electron deficiency in $\chi_3$ borophene would not only increase its affinity to Li but also lead to high Li mobility with low $E_{\text{bar}}$ values. Thus, we expect that the synergies gained from these two factors could increase the charging rate in halogen decorated $\chi_3$ borophene, enabling storage of a large amount of Li-ions in a fast way.

The discharge rate is related to the current output of the battery and highly dependent on the $E_{\text{bar}}$ value of Li-ion migration from electrode to electrolyte. As a consequence, in a desired anode material, not only should the Li-ions be stored rapidly but they should also be released easily. Indeed, due to the attractive interactions between Li-ion and the halogen atoms, migration of Li-ions at sites close to halogen atoms is slightly more difficult. This is supported by the $E_{\text{bar}}$ values determined for Li-ion hopping to sites close to halogen atoms (Figure 6c), which were significantly larger than those measured for Li-ion hopping away from halogen atoms (Figure 6a). The increase of $E_{\text{bar}}$ follows broadly the order of $\mathrm{F} > \mathrm{Cl} > \mathrm{Br}$, in accordance with the increasing electronegativity. $^{49}$ Nevertheless, incorporation of $\mathrm{Cl}$, $\mathrm{Br}$ and $\mathrm{I}$ atoms into $\chi_3$ borophene could be also beneficial for Li-ion diffusion in anodes with shallower energy barriers. With regard to $\mathrm{F}$ atom decorated $\chi_3$ borophene as shown in Figure 6c, most $E_{\text{bar}}$ values for Li-ion hopping are larger than or close to 0.57 eV. In I-doped $\chi_3$ borophene, however, considerably shallower $E_{\text{bar}}$ values were

observed except for Li-ion hopping along the sites H1-H3, exhibiting $E_{\text{bar}}$ values in the range of 0.15 ~ 0.23 eV, which were only half of those of undoped $\chi_3$ borophene. Such barriers are preceded by the commercial graphite anode $(0.37\ \text{eV})^{49,50}$, phosphorene $(0.76\ \text{eV})^{51}$, $\text{MoS}_2(0.25\ \text{eV})^{52}$ and silicene $(0.23\ \text{eV})^{48}$. To rule out the effects of different calculation methods *i.e.* codes, functional, basis set on the results, we recalculated the $E_{\text{bar}}$ of Li-ion hopping on graphene, silicene and $\text{MoS}_2$. The calculated results are in good agreement with the those reported in references as shown in Figure S1, which also prove the reliability of results. To this end, I atom decorated $\chi_3$ borophene presents the most promising potential candidate for fast charging anode materials among the here studied halogen decorated $\chi_3$ borophenes.

AIMD simulations are performed to check the dynamic stability of I-doped borophene at room temperature. The snapshots of I-doped borophene at 2000fs are shown in Figure S2. The structures remain intact without any deconstruction with atoms vibrating at their equilibrium position and also the fluctuation of free energy is smaller than 0.06 eV. Thus, the I-doped borophene is expected to be dynamic stable at room temperature.

![](./images/813000637632479232_7.jpg)

Figure 5. Migration pathways of Li-ion on halogenated $\chi_3$ borophene (a) from the hollow sites at a larger distance (H2, H3, H4, H5 and H7) to the one nearby (H1); (b) between the closest hollow sites (H6-H1); and (c) from the nearest hollow site (H1) to those at a larger distance (H2, H3, H4, H5 and H7). (d) Migration pathways of Li on pristine $\chi_3$ borophene; Path $\square$ and II indicate Li-ion hopping along the vertical and horizontal direction, respectively.

![](./images/813000637632479232_8.jpg)

Figure 6. Energy barrier ($E_{\text{bar}}$) of Li-ion hopping: (a) from H2, H3, H4, H4 and H7 to H1; (b) from H6 to H1; and (c) from H1 to H2, H3, H4, H5 and H7. Dashed lines indicate the $E_{\text{bar}}$ on pristine $\chi_3$ borophene.

To reveal the role of the halogens in boosting the Li-ion migration dynamics on I doped $\chi_3$ borophene, taking the diffusion paths from H1 to H7 and H2 as examples, we compared the $E_{\text{ad}}$ values of Li-ions in initial state (IS) and transition state (TS) with the corresponding values on pristine $\chi_3$ borophene. The calculated results are presented in Table 4. According to the reaction kinetics theory, $E_{\text{bar}}$ is determined by the $E_{\text{ad}}$ difference between TS and IS. The illustrations in Figure 7 present the calculated configurations of the TS for Li-ion diffusion on doped and undoped $\chi_3$ borophenes. We found that the incorporation of I atom did not change the diffusion path much, where Li-ion just moved a little away from those of pristine structure. Then, we give a direct comparison of $E_{\text{ad}}$ in IS and TS to reveal the main reason of reduced $E_{\text{bar}}$. Although a larger $E_{\text{ad}}$ value in IS could be determined for I-doped $\chi_3$ borophene, the increase of $E_{\text{ad}}$ in the TS is more evident, which counteracts the contribution of the former and dominates the decrease of $E_{\text{bar}}$. To this end, the key issue determining the hopping dynamics of Li-ion is the bonding strength of Li-ion in the TS, where Li-ion resides between the bridge sites of two boron atoms. The enhanced bonding in the TS on halogenated $\chi_3$ borophene could be revealed by analyzing the PDOS of the TS for Li-ion hopping on I-doped $\chi_3$ and pristine $\chi_3$ borophenes, as illustrated in Figure 7. Indeed, a larger ratio of electronic hybridization in the TS on halogenated $\chi_3$ borophene could be determined, where new hybridization peaks appear at $-4.41$ and $-2.68$ eV for I-doped $\chi_3$ borophene (Figure 7c) in contrast to pristine $\chi_3$ borophene (Figure 7a). Moreover, the peaks at $-5.01$ eV in the former shift downward, indicating enhanced stability. A similar phenomenon can also be observed in Figure 7b and d.

Table 4. $E_{\text{ad}}$ calculated of Li-ion in initial state (IS) and transition state (TS) for Li-ion hopping on $\chi_3$ and I-$\chi_3$ borophene

<table>
  <thead>
    <tr>
      <th>$E_{\text{ad}}$(eV)</th>
      <th>Migration pathway</th>
      <th>IS</th>
      <th>TS</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2">$\chi_3$</td>
      <td>Path □</td>
      <td>−1.43</td>
      <td>−0.84</td>
    </tr>
    <tr>
      <td>Path □</td>
      <td>−1.43</td>
      <td>−0.80</td>
    </tr>
    <tr>
      <td rowspan="2">I-$\chi_3$</td>
      <td>H1→H7</td>
      <td>−1.69</td>
      <td>−1.47</td>
    </tr>
    <tr>
      <td>H1→H2</td>
      <td>−1.69</td>
      <td>−1.52</td>
    </tr>
  </tbody>
</table>

![](./images/813000637632479232_9.jpg)

Figure 7. Partial density of states (PDOS) of Li-ions and B atoms in close proximity in TS for Li-ion hopping on (a), (b) pristine $\chi_3$ borophene and (c), (d) I atom decorated $\chi_3$ borophene.

### Conclusions

We investigated the incorporation of halogen atoms (F, Cl, Br and I) into $\chi_3$ borophene and the resulting effects on Li-ion adsorption and hopping based on density functional theory. Halogenation of $\chi_3$ borophene is an exothermic process with halogens residing on top of the boron atoms at the corners of boron hexagons. The adsorption energies decrease from F atom to I atom in line with their electronegativity and substantial electron transfer from $\chi_3$ borophene to the halogen atoms, producing local electron deficiency in $\chi_3$ borophene. Cooperative effects of electron deficiency of $\chi_3$ borophene and electrostatic interaction between halogen and Li result in enhanced affinity of $\chi_3$ borophene to Li and a reduced Li-ion hopping barrier. Iodine has been determined as the preferred dopant where most diffusion paths exhibit $E_{\text{bar}}$ values typically smaller than 0.2 eV. The boosted hopping dynamics of Li-ion on halogenated $\chi_3$ borophene are attributed to the significantly enhanced bonding of

Li-ion to the anode in TS over IS in contrast to that on pristine $\chi_3$ borophene. Our results provide an alternative way to boost the rate performance of borophene as anode material and the mechanisms revealed may contribute to the development of new electrode materials with high ion hopping rates.

### Corresponding Author

*Xianfei Chen, E-mail: <chenxianfei2014@cdut.edu.cn>

*Haiying Du, E-mail: <diane201109@126.com>

ORCID: Xianfei Chen: 0000-0002-5078-3950

### Conflicts of interest

There are no conflicts to declare.

### Acknowledgments

We acknowledge the supports from china postdoctoral science foundation (2017M623306XB) and special funding for postdoctoral research projects in Sichuan.

### References

1.  A. M. Omer, *Renewable & Sustainable Energy Reviews*, 2008, **12**, 1789-1821.

2.  S. Chu and A. Majumdar, *Nature*, 2012, **488**, 294-303.

3.  G. Zhou, F. Li and H.-M. Cheng, *Energy & Environmental Science*, 2014, **7**, 1307-1338.

4.  B. Dunn, H. Kamath and J.-M. Tarascon, *Science*, 2011, **334**, 928-935.

5.  E. Lee and K. A. Persson, *Nano Letters*, 2012, **12**, 4624-4628.

6.  V. Etacheri, R. Marom, R. Elazari, G. Salitra and D. Aurbach, *Energy & Environmental Science*, 2011, **4**, 3243-3262.

7.  H. Lee, M. Yanilmaz, O. Toprakci, K. Fu and X. Zhang, *Energy & Environmental Science*, 2014, **7**, 3857-3886.

8.  M. S. Islam and C. A. J. Fisher, *Chemical Society Reviews*, 2014, **43**, 185-204.

9.  C. Liu, F. Li, L. Ma and H. Cheng, *Advanced Materials*, 2010, **22**, E28-E62.

10. L. Ji, Z. Lin, M. Alcoutlabi and X. Zhang, *Energy & Environmental Science*, 2011, **4**, 2682-2699.

11. J. Liu and X.-W. Liu, *Advanced Materials*, 2012, **24**, 4097-4111.

12. S. J. Kim, K. Choi, B. Lee, Y. Kim and B. H. Hong, *Annual Review of Materials Research*, 2015, **45**, 63-84.

13. M. Pumera, *Energy & Environmental Science*, 2011, **4**, 668-674.

14. G. Guo, D. Wang, X. Wei, Q. Zhang, H. Liu, W. Lau and L. Liu, *Journal of Physical Chemistry Letters*, 2015, **6**, 5002-5008.

15. J. Zhuang, X. Xu, G. Peleckis, W. Hao, S. X. Dou and Y. Du, *Advanced Materials*, 2017, **29**.

16. S. M. Seyed-Talebi, I. Kazeminezhad and J. Beheshtian, *Physical Chemistry Chemical Physics*, 2015, **17**, 29689-29696.

17. D. Er, J. Li, M. Naguib, Y. Gogotsi and V. B. Shenoy, *Acs Applied Materials & Interfaces*, 2014, **6**, 11173-11179.

18. M. Naguib, J. Come, B. Dyatkin, V. Presser, P.-L. Taberna, P. Simon, M. W. Barsoum and Y. Gogotsi, *Electrochemistry Communications*, 2012, **16**, 61-64.

19. P. Xiang, X. Chen, J. Liu, B. Xiao and L. Yang, *Journal of Physical Chemistry C*, 2018, **122**, 9302-9311.

20. F. Li, Y. Qu and M. Zhao, *Journal of Materials Chemistry A*, 2016, **4**, 8905-8912.

21. Q. Yao, C. Huang, Y. Yuan, Y. Liu, S. Liu, K. Deng and E. Kan, *Journal of Physical Chemistry C*, 2015, **119**, 6923-6928.

22. W. Li, Y. Yang, G. Zhang and Y.-W. Zhang, *Nano Letters*, 2015, **15**, 1691-1697.

23. S. Mukherjee, L. Kavalsky and C. V. Singh, *ACS Applied Materials & Interfaces*, 2018, **10**, 8630-8639.

24. N. K. Jena, R. B. Araujo, V. Shukla and R. Ahuja, *Acs Applied Materials & Interfaces*, 2017, **9**, 16148-16158.

25. X. Xie, Z. Ao, D. Su, J. Zhang and G. Wang, *Advanced Functional Materials*, 2015, **25**, 1393-1403.

26. M. Makaremi, B. Mortazavi and C. V. Singh, *Materials Today Energy*, 2018, **8**, 22-28.

27. A. J. Mannix, X. Zhou, B. Kiraly, J. D. Wood, D. Alducin, B. D. Myers, X. Liu, B. L. Fisher, U. Santiago, J. R. Guest, M. J. Yacaman, A. Ponce, A. R. Oganov, M. C. Hersam and N. P. Guisinger, *Science*, 2015, 1513.

28. B. Feng, J. Zhang, Q. Zhong, W. Li, S. Li, H. Li, P. Cheng, S. Meng, L. Chen and K. Wu, *Nature Chemistry*, 2016, **8**, 564-569.

29. Y. Zhang, Z. Wu, P. Gao, S. Zhang and Y. Wen, *Acs Applied Materials & Interfaces*, 2016, **8**, 22175-22181.

30. D. Rao, L. Zhang, Z. Meng, X. Zhang, Y. Wang, G. Qiao, X. Shen, H. Xia, J. Liu and R. Lu, *Journal of Materials Chemistry A*, 2017, **5**, 2328-2338.

31. B. Mortazavi, A. Dianat, O. Rahaman, G. Cuniberti and T. Rabczuk, *Journal of Power Sources*, 2016, **329**, 456-461.

32. H. R. Jiang, Z. Lu, M. C. Wu, F. Ciucci and T. S. Zhao, *Nano Energy*, 2016, **23**, 97-104.

33. X. Zhang, J. Hu, Y. Cheng, H. Y. Yang, Y. Yao and S. A. Yang, *Nanoscale*, 2016, **8**, 15340-15347.

34. B. Mortazavi, O. Rahaman, S. Ahzi and T. Rabczuk, *Applied Materials Today*, 2017, **8**, 60-67.

35. J. Liu, X. Chen, X. Deng, W. Zhang, J. Li, B. Xiao and M. Pu, *Applied Surface Science*, 2018, **441**, 356-363.

36. N. Gao, W. T. Zheng and Q. Jiang, *Physical Chemistry Chemical Physics*, 2012, **14**, 257-261.

37. J. P. Perdew, K. Burke and M. Ernzerhof, *Physical Review Letters*, 1996, **77**, 3865-3868.

38. S. Grimme, *Journal of Computational Chemistry*, 2006, **27**, 1787-1799.

39. Y. Li, D. Wu, Z. Zhou, C. R. Cabrera and Z. Chen, *Journal of Physical Chemistry Letters*, 2012, **3**, 2221-2227.

40. P. Xiang, X. Chen, W. Zhang, J. Li, B. Xiao, L. Li and K. Deng, *Physical Chemistry Chemical Physics*, 2017, **19**, 24945-24954.

41. J. Liu, L. Zhang and L. Xu, *Ionics*, 2017, **24**, 1603-1615.

42. J. Khanifaev, R. Pekoz, M. Konuk and E. Durgun, *Physical Chemistry Chemical Physics*, 2017, **19**, 28963-28969.

43. F. Karlicky, K. K. R. Datta, M. Otyepka and R. Zboril, *Acs Nano*, 2013, **7**, 6434-6464.

44. T. R. Galeev, Q. Chen, J. Guo, H. Bai, C. Miao, H. Lu, A. P. Sergeeva, S. Li and A. I. Boldyrev, *Physical Chemistry Chemical Physics*, 2011, **13**, 11575-11578.

45. X. Li, S. Xie, H. Zheng, W. Q. Tian and H. Sun, *Nanoscale*, 2015, **7**, 18863-18871.

46. Y. Tang, Y. Zhang, W. Li, B. Ma and X. Chen, *Chemical Society Reviews*, 2015, **44**, 5926-5940.

47. X. Fan, W. T. Zheng and J. Kuo, *Acs Applied Materials & Interfaces*, 2012, **4**, 2432-2438.

48. G. A. Tritsaris, E. Kaxiras, S. Meng and E. Wang, *Nano Letters*, 2013, **13**, 2258-2263.

49. E. G. Leggesse, C. Chen and J. Jiang, *Carbon*, 2016, **103**, 209-216.

50. E. Pollak, B. Geng, K. Jeon, I. T. Lucas, T. J. Richardson, F. Wang and R. Kostecki, *Nano Letters*, 2010, **10**, 3386-3388.

51. S. Zhao, W. Kang and J. Xue, *Journal of Materials Chemistry A*, 2014, **2**, 19046-19052.

52. Y. Jing, Z. Zhou, C. R. Cabrera and Z. Chen, *Journal of Physical Chemistry C*, 2013, **117**, 25409-25413.

![](./images/813000637632479232_10.jpg)

252x126mm (96 x 96 DPI)
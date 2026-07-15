# Carrier doping of $\text{Bi}_2\text{Se}_3$ surface by chemical adsorption – a DFT study

Cheng Fan$^a$, Kazuyuki Sakamoto$^{b,c,d}$ and Peter Krüger$^{a,e,*}$

$^a$Graduate School of Science and Engineering, Chiba University, Chiba, 263-8522, Japan
$^b$Department of Applied Physics, Osaka University, Osaka, 565-0871, Japan
$^c$Spintronics Research Network Division, OTRI,Osaka University, Osaka, 565-0871, Japan
$^d$Center for Spintronics Research Network, Osaka University, Osaka, 565-0871, Japan
$^e$Molecular Chirality Research Center, Chiba University, Chiba, 263-8522, Japan

---

## ARTICLE INFO

**Keywords:**
topological insulator
chemical adsorption
carrier doping
density functional theory

## ABSTRACT

$\text{Bi}_2\text{Se}_3$ is one of the most promising topological insulators, but it suffers from intrinsic n-doping due to Se-vacancies, which shifts the Fermi level into the bulk conduction band, leading to topologically trivial carriers. Recently it was shown that this Fermi-level shift can be compensated by a locally controlled surface p-doping process, through water adsorption and XUV irradiation. Here, the microscopic mechanism of this surface doping is studied by means of density functional theory (DFT) focusing on the adsorption of $\text{H}_2\text{O}$, OH, O, C and CH on $\text{Bi}_2\text{Se}_3$. We find that water adsorption has a negligible doping effect while hydroxyl groups lead to n-doping. Carbon adsorption on Se vacancies gives rise to p-doping but it also strongly modifies the electronic band structure around the Dirac point. Only if the Se vacancies are filled with atomic oxygen, the experimentally observed p-doping without change of the topological surface bands is reproduced. Based on the DFT results, we propose a reaction path where photon absorption gives rise to water splitting and the produced O atoms fill the Se vacancies. Adsorbed OH groups appear as intermediate states and carbon impurities may have a catalytic effect in agreement with experimental observations.

---

### 1. Introduction

In a topological insulator, the surface becomes metallic through the appearance of edge-states, whose band dispersion forms a Dirac cone near the Fermi level. By virtue of time-inversion symmetry, the edge states are spin-momentum locked and topologically protected from back-scattering by non-magnetic impurities [1, 2, 3, 4]. These properties make topological insulators a very promising class of materials for low-consumption electronic devices. $\text{Bi}_2\text{Se}_3$ is one of earliest and best studied three-dimensional topological insulators [5, 6, 7, 8, 9, 10]. The $\text{Bi}_2\text{Se}_3$ crystal has trigonal symmetry but is more easily viewed as a hexagonal system, where the unit cell contains 15 atomic layers, or three quintuple layers (QL), a sequence of five covalently bonded atomic layers (Se-Bi-Se-Bi-Se). The QLs are held together by weak van-der-Waals interactions. This makes $\text{Bi}_2\text{Se}_3$ a layered material with a stable, Se-terminated (0001) surface. However, other surface terminations and reconstructions may be stabilized under special conditions and lattice defects exist [11, 12, 13].

Bulk $\text{Bi}_2\text{Se}_3$ is a semiconductor with a direct band gap of 0.22 eV [14]. At the (0001) surface, topological edge states with a Dirac cone dispersion appear, such that spin-momentum locked carriers cross the Fermi-level and the surface becomes conducting. These topological surface states were recently observed even in amorphous [15] and mesoporous $\text{Bi}_2\text{Se}_3$ [16] samples, which calls for a thorough investigation of the role of lattice imperfections. Many physical properties of $\text{Bi}_2\text{Se}_3$ have been studied using DFT, including dielectric [17, 18] and thermoelectric response [19] as well as the interface properties in ferromagnetic $\text{In}_2\text{Se}_3$/$\text{Bi}_2\text{Se}_3$ heterostructures [20]. $\text{Bi}_2\text{Se}_3$ is also considered a potential catalyst for the hydrogen evolution reaction [21]. In order to tune the electronic properties of $\text{Bi}_2\text{Se}_3$, doping with various elements (Te, Sb, Dy, Au, Ca, transition metals etc) has been studied both experimentally and theoretically [22, 23, 24, 25, 26, 27].

In general, the $\text{Bi}_2\text{Se}_3$(0001) surface is very stable and chemically inert, which makes it an attractive material for device applications. Exposure to water and oxygen at room temperature does not give rise to irreversible surface reactions [5]. However, $\text{Bi}_2\text{Se}_3$ is naturally $n$-doped, due the presence of Se vacancies, which are the dominant intrinsic defects. As a consequence, the Fermi level is raised into the conduction band, which leads to trivial metallic transport in the bulk and scattering of the topological surface band states with bulk carriers, i.e. a loss of the topological protected nature of the edge states. Therefore the intrinsic n-doping by Se vacancies must be compensated by p-doping if $\text{Bi}_2\text{Se}_3$ is to be used as a topological material in technological applications. To this end, bulk and surface doping with various species have been investigated. Substitution of Ca for Bi [26], as well as adsorption of Ru, $\text{NO}_2$ [6, 28, 29], $\text{O}_2$ [9, 30, 31] or O was found to lead to p-doping and thus may repair the defect-induced n-doping of $\text{Bi}_2\text{Se}_3$. However, in these methods the doping level was not shown to be stable against aging and atmospheric conditions, which is a crucial requirement for device applications. Recently, Sakamoto *et al.* [32] have developed a new method of surface p-doping by water adsorption and UV or X-ray irradiation. This method is stable under atmospheric conditions. Importantly, through radiation, the doped surface area can be controlled spatially

---

*Corresponding author. E-mail: pkruger@chiba-u.jp
ORCID(s): 0000-0001-9507-6435 (K. Sakamoto); 0000-0002-1247-9886 (P. Krüger)

C. Fan, K. Sakamoto, P. Krüger: Preprint submitted to Elsevier
Page 1 of 7

![](./images/923643931596423637_1.jpg)

**Figure 1:** Ball and stick model of the $Bi_2Se_3$ surface. A four-quintuple-layer repeated slab model is shown with 2×2 surface cell, as used in the adsorption studies.

at the nanometer scale, opening new opportunities for device applications.

Here we present a density functional theory (DFT) study on the adsorption of $H_2O$, OH, O, C and CH on $Bi_2Se_3$ surface and examine the doping effect in the light of the experimental results of Ref. [32]. We find that $H_2O$ physisorbs on the surface with negligible doping effect, whereas all other species lead to chemisorption which strongly affects the surface band structure. We compare adsorption on the pristine and defective surface and find that adsorption at the Se vacancy is energetically favored for O and OH but not for C. The experimentally observed p-doping with a well preserved Dirac cone can only be reproduced by O atom adsorption at a Se vacancy. This strongly suggests that the photo-induced p-doping process of Ref. [32] involves water splitting. Based on the DFT results we propose a mechanism for this surface reaction, where carbon impurities may act as a catalyst.

## 2. Computational details

We performed DFT calculations with the PBE exchange correlation potential and the projector augmented wave method VASP [33, 34, 35]. Van-der-Waals interactions were taken into account in the Grimme D-2 scheme. The plane-wave cut-off energy was set at 500 eV. The optimized lattice constants are $a$=4.12Å and $c$=28.89Å in very good agreement with experiment [36, 37, 38]. ($a$=4.137Å and $c$=28.679Å). The $Bi_2Se_3$ surface was modeled with slabs of four QLs and repeated slabs are separated by 15 Å vacuum (Fig. 1). The results were converged with slab thickness as was checked with a few six QL calculations (see Fig. 2 and Fig. S2 in the S.I.). The Brillouin zone of the 1×1 surface is sampled with a $\Gamma$-centered 8×8×1 k-point mesh. Adsorption studies were performed with a 2×2 surface supercell and a 4×4×1 k-point mesh. The atomic positions of the adsorbate, surface (Se) and subsurface layer (Bi) were fully optimized until atomic forces were below 0.01 eV/Å. Atoms in deeper layers were fixed to their bulk positions. Spin-orbit coupling was neglected during structural optimization. Finally, the total energy, band structure and Fermi energy were recalculated self-consistently including spin-orbit coupling, with four times as many k-points, i.e. on a 8×8×1 mesh for the 2×2 surface cell.

![](./images/923643931596423637_2.jpg)

**Figure 2:** Calculated band structure of $Bi_2Se_3$ along M-$\Gamma$-K for (a) bulk and (b-e) slabs of 1, 3, 4 and 6 quintuple layers (QL). The Fermi energy is indicated by the blue, solid line and $E = 0$ is defined as the Fermi energy of the clean 6 QL slab (e). The red colored bands indicate the Dirac cone.

## 3. Results and Discussion

### 3.1. Clean surface and band alignment

In Fig. 2 a-d the computed band structure along the high-symmetry line M-$\Gamma$-K of the surface Brillouin zone is shown for bulk $Bi_2Se_3$ and for slabs of different thicknesses. It can be seen that the topological bands in the bulk band

Carrier doping of $Bi_2Se_3$ surface by chemical adsorption - a DFT study

gap $(-0.2\ \text{eV} < E < 0.1\ \text{eV})$ develop progressively with increasing slab thickness, and for a thickness of four or more QL the Dirac cone appears at the Fermi level in agreement with the literature [39].

We now turn to adsorption of chemical species that were present in the experiments of Ref. [32], namely water, hydroxyl groups, oxygen and carbon. We examine whether these different adsorbates can give rise to surface doping with n- or p-type carriers and a corresponding up- or down-shift of the Fermi level w.r.t. the clean surface band structure. We set the Fermi level of the clean surface (6 QL slab) to zero. In all other systems, the energy scale is fixed by aligning the lowest valence band of the adsorbed system with that of the clean, 6-QL slab, see Fig. S1 in the S.I. for details. In this way, by fixing the energy zero to the Fermi-level of the clean surface, the surface doping can be seen directly as a shift of the Fermi level, which is indicated as a red line in the band structure plots in Figs 4,6.

### 3.2. Adsorption of $\boldsymbol{H_2O}$, $\boldsymbol{OH}$, $\boldsymbol{O}$, $\boldsymbol{C}$ and $\boldsymbol{CH}$ on the pristine surface
We consider a coverage of one adsorbed molecule (or atom) per $2{\times}2$ surface cell which has an area of $59\ \mathring{A}^2$. We first study the adsorption of $H_2O$, $OH$, $O$, $C$ and $CH$ on the defect-free $Bi_2Se_3$ surface. The adsorption energy is defined as
$$
E_{\text{ads}} = E(X/S) - E(S) - E(X) \tag{1}
$$
where $E(X)$, $E(S)$ and $E(X/S)$ denote, respectively, the energy of specie X in the gas phase, the energy of the clean surface (S) and the energy of X adsorbed on the surface. For each adsorbate, several stable structures were found in the calculation. Fig. 3 shows the most stable ones and their adsorption energies. The $H_2O$ molecule (Fig. 3 a) physisorbs on the $Bi_2Se_3$ surface with an adsorption energy of $-0.18\ \text{eV}$, in qualitative agreement with Ref. [5]. The water molecule is located above the center of three Se surface atoms (SeI) at a Se-O distance of $3.35\ \mathring{A}$ and an orientation that hints to some weak Se-H interaction. The hydroxyl (OH) molecule (Fig. 3 b) has a much larger adsorption energy of $-1.41\ \text{eV}$. The O atom makes a covalent bond (bond length $1.89\ \mathring{A}$) with one Se surface atom. The Se-O-H angle is strongly bent, with the H atom pointing to another surface Se atom at a distance $2.59\ \mathring{A}$, indicating weak hydrogen bonding. When a single O atom is adsorbed (Fig. 3 c) the O atom locates at a similar position as in the OH case, but the Se-O bond is shorter ($1.69\ \mathring{A}$) and the adsorption energy is twice as large ($-2.88\ \text{eV}$), as may be expected for a Se-O double bond. A single C atom (Fig. 3 d) makes a strong reaction with the surface, such that the Se atom is effectively replaced by the C atom which bonds to Bi, while the Se atom is lifted and only bonds to C with a bond length of $1.81\ \mathring{A}$. Note that the C atom has a tetrahedral coordination with four covalent bonds, which explains the high stability of the structure. In the stable conformation of the CH adsorption (Fig. 3 e) the C atom makes bonds to H, the lifted SeI and two Bi atoms.

![](./images/923643931596423637_3.jpg)

**Figure 3:** Ball-and-stick models of most stable structures and adsorption energies $E_{\text{ads}}$ of $H_2O$, $OH$, $O$ and $C$ adsorbed on a defect-free $Bi_2Se_3$ surface (denoted S) with a coverage of one molecule per $2{\times}2$ cell. Top (left) and side (right) views are shown.

The electronic bands of these adsorbate structures are shown in Fig. 4. The Brillouin zone of the $2{\times}2$ cell is smaller than that of the $1{\times}1$ cell, and the bands are downfolded. M' and K' denote the M and K points of the $2{\times}2$ cell and they correspond to the mid-points of $\Gamma$-$M$ and $\Gamma$-$K$ lines, respectively, in the $1{\times}1$ Brillouin zone. When comparing Fig. 4 a and Fig. 2 d, it is seen that water adsorption hardly changes the band structure around the Fermi level, which is slightly shifted upwards by $0.06\ \text{eV}$, but still coincides with the Dirac point. In other words, water adsorption has virtually no doping effect on clean $Bi_2Se_3$, as expected from the fact that water is physisorbed. Adsorption of an OH group (Fig. 4 b) however, leads to a large n-doping with the Fermi-level moving up by $+0.44\ \text{eV}$. Also adsorption of atomic oxygen (Fig. 4 c) or atomic carbon (Fig. 4 d) leads to a substantial n-doping with a Fermi level shifts of $+0.26\ \text{eV}$

C. Fan, K. Sakamoto, P. Krüger: *Preprint submitted to Elsevier*
Page 3 of 7

Carrier doping of $Bi_2Se_3$ surface by chemical adsorption - a DFT study

<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="2">X/S</th>
      <th colspan="2">X/V</th>
    </tr>
    <tr>
      <th>X</th>
      <th>$E_{ads}$</th>
      <th>$E_F$</th>
      <th>$E_{ads}$</th>
      <th>$E_F$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$H_2O$</td>
      <td>-0.18</td>
      <td>0.06</td>
      <td>-0.18</td>
      <td>0.29</td>
    </tr>
    <tr>
      <td>OH</td>
      <td>-1.41</td>
      <td>0.44</td>
      <td>-3.61</td>
      <td>0.55</td>
    </tr>
    <tr>
      <td>O</td>
      <td>-2.88</td>
      <td>0.26</td>
      <td>-5.42</td>
      <td>0.00</td>
    </tr>
    <tr>
      <td>C</td>
      <td>-3.93</td>
      <td>0.36</td>
      <td>-3.58</td>
      <td>0.07</td>
    </tr>
    <tr>
      <td>CH</td>
      <td>-3.23</td>
      <td>0.44</td>
      <td>-4.49</td>
      <td>0.20</td>
    </tr>
  </tbody>
</table>

Table 1
Adsorption energy $E_{ads}$ and Fermi energy $E_F$ (both in eV) of various species X adsorbed on the pristine $Bi_2Se_3$ surface (X/S) or on the Se defective surface (X/V). The Fermi level of the clean defective surface (V) is 0.32 eV

and +0.36 eV respectively. The adsorption energies and Fermi energies are summarized in Table 1. In conclusion, all considered species except $H_2O$, if adsorbed on the pristine surface would lead to n-doping.

### 3.3. Adsorption on the Se defective surface

Now we consider a defective $Bi_2Se_3$ surface with one Se vacancy in the surface layer (SeI site) of the $2 \times 2$ surface cell. If the Se vacancy is located in the sub-surface layer (SeII site), it is less stable by 0.52 eV. The optimized structure of the surface with one Se vacancy ("V(Se)") is shown in Fig. 5 a. This SE defective surface is denoted "V" in the following and its band structure is shown in Fig. 6 a. When comparing with the clean surface (Fig. 2 d), it is seen that the band structure is very similar, except for the appearance of a new band in $0 < E < 0.3$ eV (which appears as two bands in the $2 \times 2$ down-folded Brillouin zone). The Dirac cone is still clearly visible at $\Gamma$ and $E \approx 0$. However, the Fermi level is shifted upward by +0.33 eV and thus reaches the bottom of the conduction band, which implies that the carrier states are no longer topological edge states. These findings agree with the literature [6, 28, 32]. Next, we have studied the adsorption of $H_2O$, OH, O, C and CH on the Se-defective surface. For each adsorbate X, the most stable structure, denoted X/V, is shown in Figs 5 b-d and the adsorption energies are indicated. They are calculated using Eq. (1) upon replacing S by V.

The water molecule is adsorbed at the same position and orientation as in the defect-free case (Fig. 3 a), i.e. above the center of three SeI surface atoms, and the adsorption energy is nearly the same ($-0.18$ eV). The band structure of the defective surface (Fig. 6 a) is almost unchanged upon water adsorption and the Fermi level is at the same position as before adsorption. When a hydroxyl group is adsorbed on the defective surface the OH molecule fills the Se vacancy site (Fig. 5 c). The O atom substitutes the missing Se atom and makes bonds with the three neighboring Bi atoms (bond length $2.55 \mathring{A}$). The OH adsorption energy ($-3.65$ eV) is over 2 eV larger than on the pristine surface. The band structure is shown in Fig. 6 c. As compared to the clean surface, the Dirac cone is slightly shifted (by +0.15 eV) but still clearly visible. The Fermi level is at $E_F = +0.55$ eV, which is the highest value found for all systems studied here. As compared to the clean, defective surface (Fig. 6 a,
$E_F = 0.32$ eV), the Fermi level is further up-shifted by OH-adsorption. So the OH-species always leads to n-doping, whether it is adsorbed on the pristine surface (Fig. 3 b) or on a Se-vacancy site. Among the species considered here, this universal n-doping behaviour is only found for the OH-group. In the experiments [32] it was found that water adsorption followed by XUV irradiation can, under certain conditions, lead to n-doping with a Fermi-level shift of about 0.1 eV. At the same time, the O-1s XPS data showed a peak with a binding energy between that of $H_2O$ and most oxides ($O^{2-}$) which may be due to a hydroxyl group. Therefore, the present findings strongly suggest that the experimentally observed n-doping is due to OH-species, produced by radiative dissociation of water molecules.

<table>
  <thead>
    <tr>
      <th>X</th>
      <th>H</th>
      <th>O</th>
      <th>C</th>
      <th>OH</th>
      <th>CH</th>
      <th>$H_2O$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>E(X/S)</td>
      <td>0.938</td>
      <td>-2.574</td>
      <td>-3.973</td>
      <td>-3.704</td>
      <td>-4.630</td>
      <td>-5.728</td>
    </tr>
    <tr>
      <td>E(X/V)</td>
      <td>0.502</td>
      <td>-5.120</td>
      <td>-3.576</td>
      <td>-5.902</td>
      <td>-5.892</td>
      <td>-5.722</td>
    </tr>
  </tbody>
</table>

Table 2
Calculated formation energy $E$ (in eV) of various chemical species X adsorbed on the pristine (S) and Se-defective (V) $Bi_2Se_3$ surface.

When a single O atom is adsorbed on the defective surface (Figs. 5 d) the O atom occupies the Se vacancy site and makes covalent bonds with the three neighboring Bi atoms, as in the case of OH adsorption. The adsorption energy of O/V is $-5.42$ eV, i.e. about twice larger than that of O on the pristine surface (O/S). Interestingly, the band structure of O/V system is very similar to that of the pristine, defect-free surface (Fig. 2 d). The Fermi-level is exactly at the Dirac point ($E_F$=0) and so the surface is neither n- nor p-doped. This is because oxygen is isoelectronic to selenium, and one O atom can passivate almost perfectly the dangling bonds created by one Se vacancy. We thus find that oxygen adsorption on the defective surface gives rise to p-doping which can completely undo the n-doping effect of the Se vacancies, in agreement with Koleini et al. [28]. When carbon is adsorbed on the defective surface, the C atom also fills the Se vacancy and the Fermi level is down-shifted as compared to the clean defective surface by about 0.2 eV. The p-doping effect is, however smaller than for the O atom, and the band structure at $E \approx 0$ around the $\Gamma$-point is different from the pristine surface, with several new bands appearing near the Dirac cone. The same is true for CH adsorption on the Se vacancy.

For the discussion of possible surface reactions, we have listed the formation energies of the various adsorbate systems in Table 1, calculated with the following standard states: atomic C, molecular $H_2$ and $O_2$ as well as the clean $Bi_2Se_3$ surface either pristine or with one Se vacancy. From Table 1, various reactions energies can be easily computed, e.g. for the reaction $H/S + CH/S \rightarrow C/S + H_2$, we have $\Delta_r E = E(C/S)-E(CH/S)-E(H/S)= -0.28$ eV.

Carrier doping of $Bi_2Se_3$ surface by chemical adsorption -- a DFT study

### 3.4. Analysis of experimental data in the literature
A major aim of this study is to shed light on the experimental results of Ref. [32], which can be summarized as follows.
(i) The clean $Bi_2Se_3$ surface is $n$-doped due to intrinsic defects, mainly Se vacancies. The Fermi-level is about 0.4 eV above the Dirac point.
(ii) Water adsorption together with UV- or soft X-ray irradiation leads to $p$-doping, i.e. a down shift of the Fermi-level of up to 0.3 eV. As a result, the Dirac point is only about 0.1 eV below the Fermi level and the topological nature of the surface electronic structure is restored. Apart from the shift of the Dirac point, no changes of the band structure were detected.
(iii) $p$-doping was only observed when the surface is contaminated with a small amount of carbon, which comes from the scotch tape used for cleaving. For a carbon-free surface, water adsorption and light irradiation was found to slightly increase the $n$-doping.
(iv) The O-1s core-level spectra of $H_2O$ covered surface is at a binding energy $E_B = 533$ eV. Upon light radiation, two new peaks appear at lower binding energy, namely $E_B = 531$ eV and $E_B = 529.5$ eV. The $E_B = 529.5$ eV peak systematically appeared when the surface became $p$-doped. The peak at $E_B = 531$ eV, however, was not always observed, suggesting that the peak may be the signature of an intermediate state in the $p$-doping process.

In section 3 we have examined the band structure changes induced by adsorption of $H_2O$, OH, O, C and CH on the pristine and Se defective surfaces. In experiment the $p$-doping manifested itself as a shift of the Dirac point, without other changes of the band structure. $H_2O$ molecules physisorb on the surface and have almost no doping effect. OH species can fill the Se vacancies, but this leads to further $n$-doping, rather than $p$-doping. Adsorption of C at the Se vacancy leads to $p$-doping, as seen in Fig. 6 e, but the band structure around the Dirac point is strongly modified with the appearance of new, topologically trivial bands. For a high C impurity concentration as in the present model calculation, these bands would destroy the topological nature of the surface states. In the experiments of Ref. [32] no such band structure changes were observed. When an oxygen atom is adsorbed at the Se vacancy, we find strong $p$-doping which leaves the Dirac cone unchanged and totally removes the Se-vacancy induced $n$-doping, in agreement with experiment. Therefore, among the species considered, only oxygen adsorption at the Se vacancies can account for the experimental findings of Ref. [32]. As there was no free oxygen present in the experiment [32] the adsorbed O atoms must have been provided by water splitting according to the following total reaction

$$
\mathrm{H}_{2} \mathrm{O} / \mathrm{V} \rightarrow \mathrm{O} / \mathrm{V}+\mathrm{H}_{2} \quad \Delta_{r} E=0.60 \mathrm{eV} \tag{2}
$$

where $\Delta_r E$ is the calculated reaction energy. The reaction is endothermic and needs an external supply of energy. This is in agreement with the experiment. Indeed, $Bi_2Se_3$ is chemically very stable [5]. The water covered $Bi_2Se_3$ shows a chemical reaction only upon intense UV or X-ray irradiation [32], where the adsorption of photons and the following hole-decay processes can provide the energy needed to trigger an endothermic surface reaction. It is clear that once molecular hydrogen is formed, it will immediately desorb from the surface for entropy reasons. Therefore reaction (2) is in practice irreversible, which agrees with irreversibility of the $p$-doping process in experiment [32]. The foregoing analysis shows that filling of Se vacancies by oxygen from water molecules is possible on thermodynamic grounds and that it provides the only explanation for the observed $p$-doping which fits the experimental data [32].

### 3.5. A model for the chemical reaction mechanism
The atomistic details of the reaction are, however, far from obvious. Water splitting at a solid surface generally involves several intermediate states [40]. It is highly unlikely that reaction (2) occurs directly in a single step, because this would require the simultaneous breaking of two O-H bonds. Based on the theoretically calculated energies in Table I, we propose a more likely reaction mechanism, which is schematized in Fig. 7 and explained in the following. We start from a water molecule physisorbed at the Se vacancy. By photon adsorption, enough energy is provided to break one O-H and release a H atom according to the reaction

$$
\mathrm{H}_{2} \mathrm{O} / \mathrm{V} \rightarrow \mathrm{OH} / \mathrm{V}+\mathrm{H} / \mathrm{S} \quad \Delta_{r} E=0.76 \mathrm{eV} \tag{3}
$$

While the reaction energy is slightly higher than that of (2) it is much more likely since it involves only one O-H bond breaking. Once the H atom is released, it will diffuse on the $Bi_2Se_3$ surface. It may go back to the vacancy site in which case the reverse reaction of (3) occurs and the $H_2O$ molecule is restored. This is most likely, but there is a non-zero chance for two competing reactions. First, it is possible that two diffusing H atoms meet and form molecular hydrogen:

$$
\mathrm{H} / \mathrm{S}+\mathrm{H} / \mathrm{S} \rightarrow \mathrm{H}_{2} \quad \Delta_{r} E=-1.88 \mathrm{eV} \tag{4}
$$

Second, when carbon impurities are present, the diffusing H atoms may be trapped at the C sites according to the reaction

$$
\mathrm{H} / \mathrm{S}+\mathrm{C} / \mathrm{S} \rightarrow \mathrm{CH} / \mathrm{S} \quad \Delta_{r} E=-1.60 \mathrm{eV} \tag{5}
$$

The reaction energy was calculated with the most stable conformations for C/V and CH/V, see Figs 3 d,e. Given the large exothermic reaction energy, the trapped H atom is very stable. When a second diffusion H atom reaches the C site, molecular hydrogen can be formed as

$$
\mathrm{H} / \mathrm{S}+\mathrm{CH} / \mathrm{S} \rightarrow \mathrm{C} / \mathrm{S}+\mathrm{H}_{2} \quad \Delta_{r} E=-0.28 \mathrm{eV} \tag{6}
$$

which is also exothermic. Reactions (5) and (6) together yield the same product (molecular hydrogen) as reaction (4), i.e. the carbon impurities acts as a catalyst. Whether the hydrogen formation occurs directly (4) or with the C catalyst, depends on the relative concentrations of adsorbed atomic hydrogen and of C impurities. In the experiments [32] the

C. Fan, K. Sakamoto, P. Krüger: Preprint submitted to Elsevier
Page 5 of 7

Carrier doping of $Bi_2Se_3$ surface by chemical adsorption – a DFT study

C concentration was in the 0.1–1% range. The concentration of adsorbed H atoms produced by the photo-assisted reaction (3) is very difficult to estimate. However, given the large endothermic reaction energy, it might be well below 0.1%. In this case, the hydrogen formation reaction would be driven by the C catalyst. Once a Se vacancy is filled by a hydroxyl group, the following reaction may occur

$$\mathrm{OH/V} \rightarrow \mathrm{O/V} + \mathrm{H/S} \quad \Delta_r E = 1.72\ \mathrm{eV} \tag{7}$$

This reaction is clearly endothermic which means that OH/V is a stable intermediate state of the water splitting reaction. Under XUV irradiation, photon absorption may provide the energy $\Delta_r E$ for reaction (7). Moreover, hydrogen dissociation may be facilitated by the fact that the photoemission process leads to a positive charging of the surface [32]. Indeed, if the photohole is located on the OH group, a $\mathrm{H^+}$ ion may detach and form $\mathrm{H_3O^+}$ with a nearby water molecule. Since reaction (7) is by 1 eV more endothermic than hydrogen dissociation from water (reaction 3), its reaction rate should be much smaller, which implies that the concentration of H atoms at the surface $(c_\mathrm{H})$ is very low. Then, direct $\mathrm{H_2}$ formation by two diffusing H atoms (reaction 4) seems very unlikely, since the reaction rate is proportional to $c_\mathrm{H}^2$. The rate of reaction (6), on the other hand, is proportional to $c_\mathrm{H}c_\mathrm{C}$, where $c_\mathrm{C}$ is the concentration of C surface impurities. When C impurities can be detected by XPS (as in Ref. 15) we can safely assume $c_\mathrm{C} \gg c_\mathrm{H}$, and so reaction (6) is far more likely than (4), i.e. $\mathrm{H_2}$ formation is much facilitated by the presence of C impurities. The C impurities form a reservoir for surface hydrogen (reaction 5) and thus can act as a catalyst for $\mathrm{H_2}$ formation at the $\mathrm{Bi_2Se_3}$ surface (reaction 6). This may explain the experimental finding (iii) above, i.e. the fact that the XUV induced p-doping process was only observed at surfaces with some carbon contamination [32].

In order to better understand the chemical shifts observed at the O-1s core-level (point (iv) above) we have computed the binding energies $(E_B)$ with DFT-VASP (see the S.I. for details). The calculated binding energies decrease in the sequence $E_B(\mathrm{H_2O/S}) > E_B(\mathrm{OH/V}) > E_B(\mathrm{O/V})$. By comparing the theoretical and experimental chemical shifts [32], we can attribute the peak of highest binding energy (533 eV), which is the only peak before irradiation, to adsorbed $\mathrm{H_2O}$. The low energy peak (529.5 eV) which appears concomitantly with p-doping is attributed to O/V and the intermediate-energy peak (531 eV) to OH/V. These assignments fully support the proposed reaction mechanism, where OH/V is a quite stable intermediate state and O/V is the final state of the water splitting reaction.

## 4. Conclusions
In summary, we have presented a first-principles study on the adsorption of $\mathrm{H_2O}$, OH, O, C and $\mathrm{CH}$ on a $\mathrm{Bi_2Se_3}$ surface, either pristine or with Se vacancies. The effect of the adsorbed species on the topological insulator band structure was investigated. We find that $\mathrm{H_2O}$ physisorbs on $\mathrm{Bi_2Se_3}$ and has a negligible doping effect. All other species interact with the surface by chemisorption. On the pristine surface, adsorption of OH, C or O adsorption leads to $n$-doping. The Se-defective surface is intrinsically $n$-doped. If an OH group adsorbs at the Se-vacancy, the $n$-doping increases even more but if a C or a O atom fills the vacancy, $p$-doping occurs. In the case of C, the band structure around the Dirac point is strongly changed, but in the case of O, the topological surface band structure of pristine $\mathrm{Bi_2Se_3}$ is perfectly restored. We have discussed a recently reported method for controlled surface $p$-doping which uses water adsorption and XUV irradiation [32]. Based on the computed adsorption energies, we propose the following reaction mechanism which may explain the experimental findings of Ref. [32]. Water decomposes into an O atom which fills the Se vacancy and a hydrogen molecule which desorbs from the surface. The reaction is weakly endothermic but the required energy (0.6 eV) can be easily provided by photon absorption. Since the simultaneous breaking of two OH bonds is highly unlikely, we suggest that in a first step an OH group is formed which fills the vacancy while the released H atom binds to Se. In a second step the remaining H atom of the adsorbed OH group is released under photo-absorption. This reaction is substantially more endothermic (by about 1 eV) than the first step and should thus be the rate limiting process. As a consequence, the adsorbed OH group forms a relatively stable intermediate state during XUV irradiation. The presence of an intermediate state was indeed evidenced as a peak in the experimental O-1s XPS [32] whose chemical shift qualitatively agrees with the theoretical value of the adsorbed OH group. Adsorbed C atoms can trap hydrogen atoms that are diffusing on the surface and thus may act as a hydrogen atom reservoir for $\mathrm{H_2}$ molecule formation. In this way, adsorbed C atoms may play a catalytic role in the light-induced water splitting reaction, in agreement with experiment [32].

## Acknowledgments
C.F. is grateful for financial support by JST SPRING, grant No. JPMJSP2109. K.S. acknowledges support by JSPS KAKENHI grant No. JP22H01957 and JP20H05621 and the Spintronics Research Network of Japan.

## References
[1] S. Murakami, Phase transition between the quantum spin hall and insulator phases in 3d: emergence of a topological gapless phase, New Journal of Physics 9 (9) (2007) 356.
[2] J. E. Moore, The birth of topological insulators, Nature 464 (7286) (2010) 194–198.
[3] L. A. Wray, S.-Y. Xu, Y. Xia, D. Hsieh, A. V. Fedorov, Y. S. Hor, R. J. Cava, A. Bansil, H. Lin, M. Z. Hasan, A topological insulator surface under strong coulomb, magnetic and disorder perturbations, Nature Physics 7 (1) (2011) 32–37.
[4] Y. Ando, Topological insulator materials, Journal of the Physical Society of Japan 82 (10) (2013) 102001.
[5] L. V. Yashina, J. Sánchez-Barriga, M. R. Scholz, A. A. Volykhov, A. P. Sirotina, S. Neudachina, Vera, M. E. Tamm, A. Varykhalov, D. Marchenko, G. Springholz, et al., Negligible surface reactivity of topological insulators $\mathrm{Bi_2Se_3}$ and $\mathrm{Bi_2Te_3}$ towards oxygen and water, Acs Nano 7 (6) (2013) 5181–5191.

C. Fan, K. Sakamoto, P. Krüger: Preprint submitted to Elsevier
Page 6 of 7

Carrier doping of $Bi_2Se_3$ surface by chemical adsorption - a DFT study

[6] D. Hsieh, Y. Xia, D. Qian, L. Wray, J. Dil, F. Meier, J. Osterwalder, L. Patthey, J. Checkelsky, N. P. Ong, et al., A tunable topological insulator in the spin helical dirac transport regime, Nature 460 (7259) (2009) 1101-1105.

[7] J. Checkelsky, Y. Hor, R. Cava, N. Ong, Bulk band gap and surface state conduction observed in voltage-tuned crystals of the topological insulator $Bi_2Se_3$, Physical review letters 106 (19) (2011) 196801.

[8] J. Moon, N. Koirala, M. Salehi, W. Zhang, W. Wu, S. Oh, Solution to the hole-doping problem and tunable quantum hall effect in $Bi_2Se_3$ thin films, Nano letters 18 (2) (2018) 820-826.

[9] Y. Chen, J.-H. Chu, J. Analytis, Z. Liu, K. Igarashi, H.-H. Kuo, X. Qi, S.-K. Mo, R. Moore, D. Lu, et al., Massive dirac fermion on the surface of a magnetically doped topological insulator, Science 329 (5992) (2010) 659-662.

[10] K. Kuroda, M. Arita, K. Miyamoto, M. Ye, J. Jiang, A. Kimura, E. Krasovskii, E. Chulkov, H. Iwasawa, T. Okuda, et al., Hexagonally deformed fermi surface of the 3d topological insulator bi 2 se 3, Physical review letters 105 (7) (2010) 076802.

[11] M. Hermanowicz, W. Koczorowski, M. Bazarnik, M. Kopciuszyński, R. Zdyb, A. Materna, A. Hruban, R. Czajka, M. Radny, Stable bis- muth sub-monolayer termination of $Bi_2Se_3$, Applied Surface Science 476 (2019) 701-705.

[12] M. Hermanowicz, M. Radny, Topological electronic states of bismuth selenide thin films upon structural surface defects, Computational Materials Science 117 (2016) 76-82.

[13] M. Jurczyszyn, M. Sikora, M. Chrobak, L. Jurczyszyn, Studies of surface states in $Bi_2Se_3$ induced by the bise substitution in the crystal subsurface structure, Applied Surface Science 528 (2020) 1426978.

[14] G. Martinez, B. Piot, M. Hakl, M. Potemski, Y. Hor, A. Materna, S. Strzelecka, A. Hruban, O. Caha, J. Novak, A. Dubroka, C. Drasar, M. Orlita, Determination of the energy band gap of bi2se3, Scientific Reports 7 (2017) 6891.

[15] P. Corbae, S. Ciocys, D. Varjas, E. Kennedy, S. Zeltmann, M. Molina- Ruiz, S. M. Griffin, C. Jozwiak, Z. Chen, L.-W. Wang, et al., Observa- tion of spin-momentum locked surface states in amorphous $Bi_2Se_3$, Nature Materials 22 (2) (2023) 200-206.

[16] T. Nagaura, A. Ashok, A. Alowashecir, A. Vasanth, M. Han, Y. Ya- mauchi, Mesoporous semiconductive $Bi_2Se_3$ films, Nano Letters 23 (12) (2023) 5424-5429.

[17] M. Fang, Z. Wang, H. Gu, M. Tong, B. Song, X. Xie, T. Zhou, X. Chen, H. Jiang, T. Jiang, et al., Layer-dependent dielectric per- mittivity of topological insulator $Bi_2Se_3$ thin films, Applied Surface Science 509 (2020) 144822.

[18] A. Lawal, A. Shaari, R. Ahmed, N. Jarkoni, First-principles many- body comparative study of $Bi_2Se_3$ crystal: A promising candidate for broadband photodetector, Physics Letters A 381 (35) (2017) 2993-2999.

[19] D. Guo, C. Hu, Ultrahigh thermoelectricity of atomically thick $Bi_2Se_3$ single layers: A computational study, Applied surface science 321 (2014) 525-530.

[20] T. Ayadi, L. Debbichi, M. Badawi, M. Said, D. Rocca, S. Lebègue, An ab initio study of the electronic properties of the ferroelectric heterostructure $In_2Se_3/Bi_2Se_3$, Applied Surface Science 538 (2021) 148066.

[21] L.-B. Zhan, C.-L. Yang, M.-S. Wang, X.-G. Ma, Newfound two- dimensional $Bi_2Se_3$ monolayers for driving hydrogen evolution re- action with the visible-light, Applied Surface Science 564 (2021) 150389.

[22] C.-C. Wang, Y.-S. Chang, P.-T. Lin, F.-S. Shieu, H.-C. Shih, Fabrica- tion, characterization and optical properties of au-decorated $Bi_2Se_3$ nanoplatelets, Scientific Reports 12 (1) (2022) 17761.

[23] N. Patil, A. Sargar, S. Mane, P. Bhosale, Growth mechanism and characterisation of chemically grown sb doped $Bi_2Se_3$ thin films, Applied Surface Science 254 (16) (2008) 5261-5265.

[24] K. Holtgrewe, C. Hogan, S. Sanna, Evolution of topological surface states following sb layer adsorption on bi2se3, Materials 14 (7) (2021) 1763.

[25] M. Mohyedin, N. Malik, M. Taib, M. Mustaffa, O. Hassan, A. Ali, B. Haq, M. Yahya, First principles study of structural, electronic and optical properties of orthorhombic phase ni-doped $Bi_2Se_3$ using den- sity functional theory, Computational Condensed Matter 25 (2020) e00510.

[26] J.-M. Zhang, W. Ming, Z. Huang, G.-B. Liu, X. Kou, Y. Fan, K. L. Wang, Y. Yao, Stability, electronic, and magnetic properties of the magnetically doped topological insulators bi2se3, bi2te3, and sb2te3, Physical Review B 88 (23) (2013) 235131.

[27] Y. S. Hor, A. Richardella, P. Roushan, Y. Xia, J. G. Checkelsky, A. Yazdani, M. Z. Hasan, N. P. Ong, R. J. Cava, p-type bi₂se₃ for topo- logical insulator and low-temperature thermoelectric applications, Phys. Rev. B 79 (2009) 195208.

[28] M. Koleini, T. Frauenheim, B. Yan, Gas doping on the topological insulator $Bi_2Se_3$ surface, Physical Review Letters 110 (1) (2013) 016403.

[29] Y. Xia, D. Qian, D. Hsieh, R. Shankar, H. Lin, A. Bansil, A. Fedorov, D. Grauer, Y. Hor, R. Cava, et al., Topological control: Systematic control of topological insulator dirac fermion density on the surface of bi2te3, arXiv preprint arXiv:0907.3089 (2009).

[30] D. Hsieh, M. Mclver, D. H. Torchinsky, D. R. Gardner, Y. S. Lee, N. Gedik, Nonlinear optical probe of tunable surface electrons on a topological insulator, Physical review letters 106 (5) (2011) 057401.

[31] B. Zhou, Z. Liu, J. Analytis, K. Igarashi, S. Mo, D. Lu, R. Moore, I. Fisher, T. Sasagawa, Z. Shen, et al., Controlling the carriers of topological insulators by bulk and surface doping, Semiconductor Science and Technology 27 (12) (2012) 124002.

[32] K. Sakamoto, H. Ishikawa, T. Wake, C. Ishimoto, J. Fujii, H. Bent- mann, M. Ohtaka, K. Kuroda, N. Inoue, T. Hattori, et al., Spatial control of charge doping in n-type topological insulators, Nano Letters 21 (10) (2021) 4415-4422.

[33] R. G. Parr, S. R. Gadre, L. J. Bartolotti, Local density functional theory of atoms and molecules, Proceedings of the National Academy of Sciences 76 (6) (1979) 2522-2526.

[34] G. Kresse, J. Furthmüller, Efficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set, Physical review B 54 (16) (1996) 11169.

[35] J. P. Perdew, K. Burke, M. Ernzerhof, Generalized gradient approxi- mation made simple, Physical review letters 77 (18) (1996) 3865.

[36] H. Cao, S. Xu, I. Miotkowski, J. Tian, D. Pandey, M. Z. Hasan, Y. P. Chen, Structural and electronic properties of highly doped topological insulator $Bi_2Se_3$ crystals, physica status solidi (RRL)-Rapid Research Letters 7 (1-2) (2013) 133-135.

[37] W. Wyckoff Ralph, Crystal structures, vol. 2 (1964).

[38] X. Chen, H. Zhou, A. Kiswandhi, I. Miotkowski, Y. Chen, P. Sharma, A. Lima Sharma, M. Hekmaty, D. Smirnov, Z. Jiang, Thermal expan- sion coefficients of $Bi_2Se_3$ and $Sb_2Te_3$ crystals from 10 k to 270 k, Applied Physics Letters 99 (26) (2011).

[39] L. He, F. Xiu, X. Yu, M. Teague, W. Jiang, Y. Fan, X. Kou, M. Lang, Y. Wang, G. Huang, et al., Surface-dominated conduction in a 6 nm thick $Bi_2Se_3$ thin film, Nano letters 12 (3) (2012) 1486-1490.

[40] U. Aschauer, Y. He, H. Cheng, S.-C. Li, U. Diebold, A. Selloni, Influence of subsurface defects on the surface reactivity of tio2: water on anatase (101), The Journal of Physical Chemistry C 114 (2) (2010) 1278-1284.

---
C. Fan, K. Sakamoto, P. Krüger: Preprint submitted to Elsevier
Page 7 of 7

![](./images/923643931596423637_4.jpg)

Figure 4: Band dispersion of the adsorption structures on the defect-free surface (S) shown in Fig. 3. High-symmetry points of the 2×2 surface Brillouin zone are denoted by K' and M' and correspond to $k$-vectors at the midpoint of the $\Gamma$-K and $\Gamma$-M line, respectively, in the primitive Brillouin zone of Fig. 2. The red solid line shows the Fermi level and the blue dotted lines are a guide for the eye ($k$=0,$E$=0).

![](./images/923643931596423637_5.jpg)

Figure 5: (a) Computed structure of the $Bi_2Se_3$ surface with one SeI vacancy, whose position is indicated as a pale yellow ball (V(Se)). (b-e) Most stable structures and adsorption energies $E_{\text{ads}}$ of $H_2O$, OH, O and C adsorbed on the Se defective surface (which is denoted "V").

Carrier doping of $Bi_2Se_3$ surface by chemical adsorption – a DFT study

![](./images/923643931596423637_6.jpg)

Figure 6: Band dispersion of the adsorption structures of Fig. 5 on the Se-defective surface (V)

![](./images/923643931596423637_7.jpg)

Figure 7: Scheme of the suggested reaction mechanism for the XUV-induced $p$-doping of a Se-defective $Bi_2Se_3$ surface without (upper panel) and with (lower panel) C impurities.

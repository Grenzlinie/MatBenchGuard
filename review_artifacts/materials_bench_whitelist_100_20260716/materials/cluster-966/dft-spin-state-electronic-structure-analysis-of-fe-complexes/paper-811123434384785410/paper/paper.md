ORIGINAL PAPER

# DFT analysis of the electronic structure of Fe(IV) species active in nitrene transfer catalysis: influence of the coordination sphere

Ranjan Patra $^{1,2,3,4}$ · Pascale Maldivi $^{5,6}$

Received: 30 June 2016 / Accepted: 9 October 2016
© Springer-Verlag Berlin Heidelberg 2016

## Abstract
Nitrene transfer reactions to various hydrocarbon molecules can be efficiently catalyzed by Fe complexes through a mechanism reminiscent of the oxygen transfer function of oxygenase enzymes. Such enzymes exhibit a high-valent iron oxo Fe(IV)=O as the active species, and it has also been proposed that an analogous species, i.e., Fe(IV)=NR (NR being the nitrene group) is responsible for the nitrene transfer activity. We describe here the influence of the Fe(IV) coordination sphere on some key parameters for nitrene transfer efficacy, such as the spin state of the Fe(IV) cation, the electronic affinity, and the bond dissociation energy of the NHR moiety. We explore here the electronic properties of Fe(IV)=NTs (NTs = tolylsulfonylimido group) mononuclear complexes with ligands involving phenolate and nitrogen donor groups, as catalytic properties with such ligands have been found to be quite promising. Six tetradentate ligands were studied, which derive from three different scaffolds: 2-methylenepyridine-N,N-bis(2-methylene-4,6-dichlorophenol) and 2-methylenepyridine-N,N-bis(2-methylene-4,6-dimethylphenol), N,N-dimethyl-N',N'-bis(2-methylene-4,6-dichlorophenol) ethylenediamine, and N,N-dimethyl-N',N'- bis(2-methylene-4,6-dimethylphenol) ethylenediamine, N,N'-bis(2-methylene-4,6-dichlorophenol)-N,N'-dimethyl-1,2-diaminoethane and N,N'-bis(2-methylene-4,6-dimethylphenol)-N,N'-dimethyl-1,2-diaminoethane. Thanks to thorough DFT computations, we present some rationalization of the electronic properties of the resulting Fe(IV)=NTs complexes in relation to their coordination sphere and compare them to other Fe(IV) nitrene active species. We show in particular the important role of the anionic character and strong $\pi$-donation of the phenolate groups.

## Keywords
Nitrene transfer $\cdot$ Fe(IV) imido $\cdot$ DFT $\cdot$ Bond dissociation energy $\cdot$ Electronic affinity

This paper belongs to Topical Collection Festschrift in Honor of Henry Chermette

Electronic supplementary material The online version of this article (doi:10.1007/s00894-016-3142-6) contains supplementary material, which is available to authorized users.

凶 Pascale Maldivi
pascale.maldivi@cea.fr

1 Laboratoire Chimie et Biologie des Métaux /Physicochimie des Métaux en Biologie (LCBM/PMB), Univ. Grenoble Alpes, 38000 Grenoble, France
2 Laboratoire Chimie et Biologie des Métaux /Physicochimie des Métaux en Biologie (LCBM/PMB), CNRS, UMR 5249, 38000 Grenoble, France
3 Biotechnology Institute of Grenoble-Chemistry and Biology of Metals (BIG-CBM), CEA, PMB, 38000, Grenoble, France
4 Department of Chemistry, Panjab University, Chandigarh 160014, India
5 INAC-SyMMES, Univ. Grenoble Alpes, 38000 Grenoble, France
6 INAC-SyMMES, CEA, 38000 Grenoble, France

## Introduction
Nitrene transfer reactions using metal complex catalysts are very promising processes to easily insert amine groups into various aliphatic or aromatic hydrocarbons, especially in the context of pharmacology or agrochemicals [1–5], as illustrated in Scheme 1.

Although rhodium [2, 6] or ruthenium [7] complexes have been studied extensively, there is a need to turn to cheaper and less toxic metals. Among 3d metal catalysts, Fe complexes have proven very efficient in nitrene transfer [5, 8–11] and it has been proposed, on both experimental and theoretical grounds, that an active intermediate involving a high valent

$$\text{a) } \ce{S ->[M - NR] S=NR}$$

$$\text{b) } \ce{C=C ->[M - NR] <NR>}$$

$$\text{c) } \ce{(sp_3/sp_2)C-H ->[M - NR] (sp_3/sp_2)C-N(H)R}$$

Scheme 1a-c Applications of nitrene transfer in synthetic organic chemistry. a Sulfimidation, b aziridination, c amine insertion. [M-NR] represents the metal complex active in NR (nitrene group) transfer

Fe complex of the type $\text{Fe(IV)} = \text{NR}$ (NR = nitrene group) was responsible for nitrene transfer [9, 11-13]. Such intermediates present close analogies with the ferryl $\text{Fe(IV)} = \text{O}$ species in oxygenase active sites responsible for oxygen transfer to a variety of hydrocarbons in numerous biological processes [14-18]. Most investigations on Fe catalysts for nitrene transfer rely on trigonal or tetragonal $\text{Fe(IV)} = \text{NR}$ complexes made up of nitrogen donor ligands, in order to stabilize the high valent state [8, 13, 19-23]. This strategy of stabilizing the active species is interesting to get experimental data on the $\text{Fe(IV)} = \text{NR}$ active species, but on the other hand yields poorly-to-medium active catalysts. One example that has been thoroughly studied experimentally as well as theoretically is the $\text{N4PyFe(IV)} = \text{NTs}$ complex first published by Que et al. (Fig. 1a) [9, 19]. This complex bears a pentacoordinate neutral ligand with N-donor atoms only. More recently, we have described the electronic properties of binuclear iron complexes with a different N3O3 coordination sphere, that are able to give rise to very active intermediates in nitrene transfer reactions such as aziridination of styrene or amination of aliphatic C-H bonds [24-26]. The NR considered was the N-Tosyl group, which will be noted NTs. Detailed mass spectrometry, reactivity and computational studies revealed a two-level reactivity, involving two high valent active species responsible for NT transfer with increasing redox state, with $\text{Fe}_2(\text{III, IV})$ and $\text{Fe}_2(\text{III, V})$ valences [24, 26] as represented in Fig. 1.

Previous theoretical investigations [24, 26] have shown that the $\text{Fe}_\text{A}$ binuclear complexes represented in Fig. 1b, c are always $\text{Fe(III)}$, while $\text{Fe}_\text{B}$ in the complex shown in Fig. 1b is $\text{Fe(IV)}$ bonded to a NTs group, and $\text{Fe}_\text{B}$ in the complex in Fig. 1c is $\text{Fe(V)}$ bonded to both NHTs (protonated N-tosyl group) and NTs groups. In the latter case, we were able to show by thorough DFT calculations that the high-valent $\text{Fe(V)}$ atom is best described as an $\text{Fe(IV)}$ bonded to a radical ligand localized either on the NTs or on the phenolate [26]. These binuclear complexes are very active in nitrene transfer, and thus deserving of more complete reactivity studies. But both their synthesis and their computational studies are hampered by their complexity. We have thus begun an experimental and theoretical investigation of mononuclear complexes with polydentate ligands able to reproduce the coordination sphere of the binuclear complexes, i.e., involving phenolates as oxygen donors and pyridine and/or amine nitrogen donors. Three different scaffolds were considered, each being substituted either by Cl or methyl groups, yielding six different ligands: 2-methylenepyridine-N,N-bis(2-methylene-4,6-dichlorophenol) and 2-methylenepyridine-N, N-bis(2-methylene-4, 6-dimethylphenol), abbreviated as dpmp-Cl and dpmp-Me, respectively, N, N-dimethyl-N',N'-bis(2-methylene-4,6-dichlorophenol) ethylenediamine and N,N-dimethyl-N',N'-bis(2-methylene-4,6-dimethylphenol) ethylenediamine, abbreviated as dpdm-Cl and dpdm-Me, respectively, and N,N'-bis(2-methylene-4,6-dichlorophenol)-N, N'-dimethyl-1, 2-diaminoethane and N,N'-bis(2-methylene-4,6-dimethylphenol)-N, N'-dimethyl-1, 2-diaminoethane, abbreviated as salan-Cl and salan-Me, respectively. Scheme 2 shows the structures of these ligands.

These three ligands offer the opportunity, within a common set of donor groups, to modulate the possible positions of these groups in the coordination sphere, and by using Cl or $\text{CH}_3$ substituents on the phenolates, to modulate their donor character. The phenol groups of these ligands may be deprotonated to yield Fe complexes that have been studied widely in the last 15 years for various purposes. Firstly, they provide interesting biomimetic models of non-heme oxygenase Fe sites [27, 28]. Secondly, iron(II) or (III) complexes of such amine-bisphenolates also attract catalysts for the hydroamination of olefins, the C-C coupling reactions involving Grignard reagents, or radical polymerization [29-32].

For our purposes, these ligands provide a means to vary the nature and position of N-donor groups. On the one hand, salan

Fig. 1 a Fe(IV)NTs (NT = N-Tosyl group) complex from Que [19]. b First binuclear active species $\text{Fe}_2(\text{III, IV})\text{NTs}$ [24]. c Second binuclear active species $\text{Fe}_2(\text{III, V})\text{-NHTs}$, $\text{NTS}$ [26]
![](./images/811123434384785410_1.jpg)

Scheme 2 Chemical structures and short names of the ligands under investigation

![](./images/811123434384785410_2.jpg)

and dpdm may be compared as they both provide two amine N and two phenolate O donor atoms, in different positions. On the other hand, dpdm and dpmp provide similar coordination geometries, differing in only one N donor atom, which is an amine for dpdm (strong $\sigma$ donor) and a pyridine (weak $\sigma/\pi$ donor, possibly $\pi$-acceptor).

Preliminary experimental studies for NT transfer have shown that the Cl- and tBu substituted dpmp and dpdm Fe complexes exhibit a similarly high catalytic activity as the binuclear complexes described previously. In the presence of a NTs donor, such complexes are able to transfer NTs to various styrene derivatives, yielding aziridine functions, and to insert NTs into aliphatic C-H bonds with similar catalytic efficiency as the binuclear systems in terms of time scales and yields [33]. Having already been shown experimentally in binuclear complexes [24, 26], the existence of an active Fe(IV)NTs species may be postulated for the mononuclear species, and its molecular properties warrant examination.

We thus describe here a comparative study of the electronic structure, spin state ordering and electrophilicity parameters of possible Fe(IV)-NTs active species that may be derived from such ligands. All experimental and computational studies made on Fe-based catalysts for NTs transfer point to the high electrophilicity of the active species and the high bond dissociation energy (BDE) of the NH-Ts group [8, 9, 13, 14, 34-37]. These parameters will be estimated here by the electronic affinity (EA) of the Fe(IV)NTs complex and the BDE of the Fe(III)-NHTs complex.

## Computational details

All calculations were performed with ADF 2010 [38, 39] using an unrestricted Kohn-Sham approach. Fe(IV) complexes exhibit mostly two spin states due to their $d^4$ configuration : $S=2$ and $S=1$. We have thus systematically compared geometries and energies of both triplet and quintet states for the complexes.

For geometry optimizations, we chose the OPBE GGA functional, i.e., the PBE correlation functional [40] with the OPTX exchange [41, 42]. Double zeta Slater functions plus polarization (DZP set) for light atoms and triple zeta Slater functions plus polarization (TZP set) for Fe were used with small frozen cores for all atoms except H. The exchange part OPTX was chosen because of its well established reliability in open shell metal complexes to describe spin state ordering [43-47]. In order to model the solvent phase, we have carried out some optimizations and single points (SP) using the conductor-like screening model COSMO, with a medium dielectric constant $\varepsilon_{\mathrm{r}}=37.5$, corresponding to acetonitrile, which is the experimental reference solvent. Geometry optimizations tested in solvent gave very similar results (structural parameters, stabilization energies) as in the gas phase.

We also performed SP calculations with hybrid functionals, at the B3LYP level (20 % exact exchange) [48] with all electron triple zeta (TZP) basis set, for Fe and double zeta + one polarization (DZP) for all other atoms, in order to compare total bonding energies at the B3LYP level, as well as spin densities. Some tests with a larger basis set, i.e., TZ2P all electron basis sets for all atoms, were realized, and the results (spin densities, trends in bonding energies) were found to give similar results as with DZP/TZP basis sets. Other functionals were also used in SP to compare the spin state orderings of Fe(IV) : B3LYP* (15 % exact exchange) [49], PBE0 (25 % exact exchange) [50] and a metahybrid TPSSH (10 % exact exchange) [51, 52].

Calculation of EA and BDE of the N-H bond in the NTs group was carried out using the following equations:

$$[\mathrm{Fe(IV)NTs}]+\mathrm{e} \rightarrow[\mathrm{Fe(III)NTs}]^{-}+\mathrm{EA}$$

$$[\mathrm{Fe(IV)NTs}]+\mathrm{H}^{\cdot} \rightarrow[\mathrm{Fe(III)NHTs}]+\mathrm{BDE}$$

B3LYP SPs in solvent were calculated from the optimized geometries determined at the OPBE level, from which frequency calculations were performed in order to calculate the free energies at 0 K for EA and BDE. The Fe(IV) and Fe(III) ions were considered in the high spin state only, because, for Fe(IV), the latter is the most stable (vide infra) and, being in the same weak-field ligand environment, the reduced form Fe(III) was also assumed to be in the high spin state.

## Results

The ligands shown in Scheme 2 are potentially tetradentate, and, with the additional NTs ligand, yield a pentacoordinated complex. The OH functions are deprotonated when coordinated to the metal ion, thus the Fe(IV)NTs complexes are neutral. Structures with a sixth ligand coming from the solvent (acetonitrile as the reference solvent in experimental studies) were

![](./images/811123434384785410_3.jpg)

also examined and their energies compared to the pentacoordinated structures with one free acetonitrile. The salan complexes were investigated only in a square-planar coordination type, as obtained experimentally in Fe(III) com- plexes [32], whereas two modes may be obtained from the dpmp and dpdm ligands, either a trigonal pyramid or asquare-based pyramid. As can be seen from Scheme 3 representing structures with both coordination numbers(CN), the trigonal symmetry yields a position where NTs is axial (along the C3 axis) while the square pyramid mode yields an equatorial position for NTs. These two positions will be noted respectively as $NTs_{ax}$ and $NTs_{eq}$ . As illustrated in Scheme 3, NTs is axial in trigonal symmetry, whereas it is equatorial in tetragonal symmetry.

The structures of dpdm complexes, not represented on Scheme 3, are similar to the dpmp ones, with the pyridine replaced by a methylene N,N-dimethyl amine group (see Scheme 2). All geometry optimizations were performed inpenta and hexa coordination modes, in either S=1 or S=2 states. As will be seen later on, bonding of the sixth ligand acetonitrile could not be obtained in some cases. In such cases, optimizations yielded either a pentacoordinated complex with an acetonitrile molecule far from the complex, or it was impos- sibility to find any minimum in the potential energy surface.

We will first examine the total electronic energies obtainedwith B3LYP in gas phase or solvent, for both S=1 and S=2 states, from the optimized geometries of complexes with salan, dpmp and dpdm in penta- or hexa-coordination modes(Table 1). In order to compare the penta- and hexa- coordination geometries, the energy of the pentacoordinated complexes were incremented with the energy with one free acetonitrile calculated at the same theoretical level as the complexes.

As a first observation, salan complexes do not bind aceto- nitrile, most probably because the only available bonding site is trans to the NTs group, which is a highly donating ligand. For dpdm and dpmp ligands, the Me or CI substitution influences the most stable coordination number only slightly. For Me-substituted ligands, no hexacoordinated geometries with S=2 could be obtained. This may be due to the electron donor character of Me-substituted ligands, which transfer more electron density to the metal than CI-substituted ligands, thus a sixth weak ligand such as acetonitrile is not necessary to stabilize the positive charge of Fe(IV). With the CI-substitutedligands, the energy differences between CN=5 and CN=6 geometries are weak, although a general trend is that solvent calculations favor CN=5 while gas phase favor CN=6. The two possible CN=5 geometries for dpmp and dpdm, either trigonal bipyramid or square-based pyramid, are close in en- ergy, thus both pentacoordination modes deserve to be considered.

The ligands used here--both the tetradentate and the NTs ligands-are all $\pi$ -donating ligands. Combined with the ob servation that, most of the time, pentacoordination is favored, we may anticipate that the Fe(IV) experiences a weak fieldligand in such an environment, thus the high spin state (S=2) should be the ground state. Indeed our calculations are con- sistent with this expectation although spin states energetics within a DFT framework deserve special care. We compared the results given by several hybrid and metahybrid functionals(Tables S6, S7). In the pentacoordinated systems, all func-tionals yield the high spin state as ground state, while S=1 excited state is within the energy range 0.3 eV-0.6 eV. For CN=6, the energy difference between S=1 and S=2 de- pends on the functional, and more precisely on the percentage of exact exchange. B3LYP and PBE0 give S=2 as the ground state, whereas other hybrids give S=1 as the ground state. These results are consistent with usual trends, i.e., increasing the contribution of exact exchange stabilizes the highest spin state. We may conclude from all these comparisons that the most stable species overall are pentacoordinate complexes in a high spin ground state, although, in some cases with CI- substituted ligands, CN=6 structures may be very close in energy.

![](./images/811123434384785410_4.jpg)

<table>
<caption>Table 1 Comparison of electronic energies (eV) obtained with B3LYP in gas (B3LYP) or solvent phase (B3LYPS) of both coordination numbers for all complexes (Cl and Me substitutions), with S = 2 and S = 1. The absence of data is due to no bonding of acetonitrile in the optimized geometry</caption>
<thead>
<tr>
<th colspan="2"></th>
<th colspan="2">Cl</th>
<th colspan="2"></th>
<th colspan="2">CH₃</th>
<th colspan="2"></th>
</tr>
<tr>
<th colspan="2"></th>
<th colspan="2">S = 2</th>
<th colspan="2">S = 1</th>
<th colspan="2">S = 2</th>
<th colspan="2">S = 1</th>
</tr>
<tr>
<th colspan="2"></th>
<th>CN = 5</th>
<th>CN = 6</th>
<th>CN = 5</th>
<th>CN = 6</th>
<th>CN = 5</th>
<th>CN = 6</th>
<th>CN = 5</th>
<th>CN = 6</th>
</tr>
</thead>
<tbody>
<tr>
<th colspan="2">dpmp</th>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<th rowspan="2">NTs<sub>ax</sub></th>
<th>B3LYP</th>
<td>−483.27ᵃ</td>
<td></td>
<td>−482.90</td>
<td>−482.95</td>
<td>−563.14ᵃ</td>
<td></td>
<td>−562.84</td>
<td>−562.76</td>
</tr>
<tr>
<th>B3LYPS</th>
<td>−484.97ᵃ</td>
<td></td>
<td>−484.61</td>
<td>−484.61</td>
<td>−564.72ᵃ</td>
<td></td>
<td>−564.42</td>
<td>−564.23</td>
</tr>
<tr>
<th rowspan="2">NTs<sub>eq</sub></th>
<th>B3LYP</th>
<td>−483.48</td>
<td>−483.68ᵃ</td>
<td>−483.03</td>
<td>−483.60ᵃ</td>
<td>−563.17ᵃ</td>
<td></td>
<td>−562.80</td>
<td>−563.22</td>
</tr>
<tr>
<th>B3LYPS</th>
<td>−484.97ᵃ</td>
<td>−484.92</td>
<td>−484.73</td>
<td>−484.98ᵃ</td>
<td>−564.71ᵃ</td>
<td></td>
<td>−564.40</td>
<td>−564.51</td>
</tr>
<tr>
<th colspan="2">dpdm</th>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<th rowspan="2">NTs<sub>ax</sub></th>
<th>B3LYP</th>
<td>−480.53</td>
<td>−480.87ᵃ</td>
<td>−480.16</td>
<td>−480.47</td>
<td>−560.42ᵃ</td>
<td></td>
<td>−559.90</td>
<td>−560.19</td>
</tr>
<tr>
<th>B3LYPS</th>
<td>−482.08ᵃ</td>
<td>−481.97</td>
<td>−481.62</td>
<td>−481.57</td>
<td>−561.80ᵃ</td>
<td></td>
<td>−561.06</td>
<td>−561.20</td>
</tr>
<tr>
<th rowspan="2">NTs<sub>eq</sub></th>
<th>B3LYP</th>
<td>−480.56</td>
<td>−480.90ᵃ</td>
<td>−480.07</td>
<td>−480.62</td>
<td>−560.39ᵃ</td>
<td></td>
<td>−560.14</td>
<td>−560.26</td>
</tr>
<tr>
<th>B3LYPS</th>
<td>−481.45ᵃ</td>
<td>−481.38</td>
<td>−481.06</td>
<td>−481.79ᵃ</td>
<td>−561.45ᵃ</td>
<td></td>
<td>−560.96</td>
<td>−561.35</td>
</tr>
<tr>
<th rowspan="2">salan</th>
<th>B3LYP</th>
<td>−480.79ᵃ</td>
<td></td>
<td>−480.13</td>
<td></td>
<td>−560.63ᵃ</td>
<td></td>
<td>−560.02</td>
<td></td>
</tr>
<tr>
<th>B3LYPS</th>
<td>−482.24ᵃ</td>
<td></td>
<td>−481.81</td>
<td></td>
<td>−561.95ᵃ</td>
<td></td>
<td>−561.51</td>
<td></td>
</tr>
</tbody>
<tfoot>
<tr>
<th colspan="10">ᵃ Lowest energies</th>
</tr>
</tfoot>
</table>

In the following, we will examine the structural and electronic properties of the pentacoordinated high spin complexes. The results of geometry optimizations are given in Table 2, for the most important distances (Fe-NTs), in the high spin state. Exhaustive data with all distances for both spin states are shown in the Supplementary Information. Figure 2 presents examples of optimized geometries for CN = 5 dpmp-Cl complexes with either NTs in axial (Fig. 2a) or equatorial (Fig. 2b) positions, and for the salan-Cl complex (Fig. 2c).

The mean < d > values are all in a narrow range from 1.99 to 2.06 Å, which is consistent with Fe(IV) distances. The Fe-N(Ts) distance is in a narrow range : 1.75–1.78 whatever the ligand and coordination number, indicating that this bond is stronger that the rest of the coordination sphere. The values are consistent with some previously published structures of Fe-nitrene complexes [8, 13, 19, 34].

<table>
<caption>Table 2 Average Fe-ligand (&lt;d&gt;) + Fe-N(Ts) distances (Å) for salan, dpmp and dpdm (Cl and Me substitutions) from geometry optimizations using OPBE/DZP/TZP (see ESI) in for CN = 5 (without acetonitrile). All are given for S = 2</caption>
<thead>
<tr>
<th></th>
<th></th>
<th>Cl</th>
<th>Me</th>
</tr>
</thead>
<tbody>
<tr>
<th colspan="2">dpmp</th>
<td></td>
<td></td>
</tr>
<tr>
<th></th>
<th>NTs<sub>ax</sub> < d ></th>
<td>1.99</td>
<td>1.99</td>
</tr>
<tr>
<th></th>
<th>Fe-NTs</th>
<td>1.75</td>
<td>1.76</td>
</tr>
<tr>
<th></th>
<th>NTs<sub>eq</sub> < d ></th>
<td>1.99</td>
<td>1.98</td>
</tr>
<tr>
<th></th>
<th>Fe-NTs</th>
<td>1.76</td>
<td>1.77</td>
</tr>
<tr>
<th colspan="2">dpdm</th>
<td></td>
<td></td>
</tr>
<tr>
<th></th>
<th>NTs<sub>ax</sub> < d ></th>
<td>2.02</td>
<td>2.00</td>
</tr>
<tr>
<th></th>
<th>Fe-NTs</th>
<td>1.76</td>
<td>1.75</td>
</tr>
<tr>
<th></th>
<th>NTs<sub>eq</sub> < d ></th>
<td>2.04</td>
<td>2.03</td>
</tr>
<tr>
<th></th>
<th>Fe-NTs</th>
<td>1.75</td>
<td>1.75</td>
</tr>
<tr>
<th colspan="2">salan</th>
<td></td>
<td></td>
</tr>
<tr>
<th></th>
<th>NTs < d ></th>
<td>2.06</td>
<td>2.06</td>
</tr>
<tr>
<th></th>
<th>Fe-NTs</th>
<td>1.78</td>
<td>1.78</td>
</tr>
</tbody>
</table>

Table 3 lists the spin densities of the most stable geometries for the three ligands, for Fe, NTs and both OPh ligands. More complete results are given in Table S8 for CN =6 complexes and S = 1 spin state. The spin density on Fe always lies between 3 and 3.9, while NTs values are between ca. 0.3 to 0.6 either positive or negative. This points to strong donation, yet without full radical character on NTs. In some previously published work on high spin Fe(IV) nitrene species, it had been possible to identify electronic configurations consistent with a Fe(III) high spin or intermediate spin coupled to a radical NTs [8, 24]. Here, even by imposing initial spin localizations on Fe and N atoms, it was not possible to converge to such Fe(III)-˙NTs configurations from the S = 2 state. In contrast, the excited triplet state shows in most cases a low spin Fe(III) –˙NTs (see Table S8). This latter configuration had also been obtained on the S = 1 ground state complex N4pyFe(IV)NTs studied by Que and de Visser [19, 53].

When comparing the influence of the ligand structure, it may be noted that changing Cl to Me has only a weak effect on spin densities of both NTs and Fe, and no effect for salan. One particular trend observed for both dpmp and dpdm ligands is that changing the coordination symmetry (NTs<sub>eq</sub> to NTs<sub>ax</sub>) changes the sign of spin polarization of the NTs group. First, it must be remembered how donation affects spin polarization of ligands in a high spin d⁴ complex (see Scheme 4).

When β donation occurs, a net positive spin polarization arises on the ligand due to loss of β electron density. This is generally the most favorable and encountered case of charge

![](./images/811123434384785410_5.jpg)

![](./images/811123434384785410_6.jpg)

Fig. 2a–c Optimized geometries using OPBE/DZP/TZP (see electronic supplementary information) for CN = 5 complexes of Fe(IV)NTs. Ball models displayed for Fe(IV), N and O donor atoms. Hydrogen atoms are not represented for clarity. a dpmp-Cl, NTsₐₓ, b dpmp-Cl, NTsₑq, c salan-Cl

transfer as it occurs to a low energy d orbital. When $\alpha$ donation occurs, a net negative spin polarization arises on the ligand due to loss of $\alpha$ electron density. This latter case is energetically less favourable than the former because the only available d orbital for donation is then the one highest in energy. This may therefore occur with a highly donating ligand. In the complexes studied here, competition for donation between nitrene and phenolate ligands may occur depending on the relative positions of the groups in the coordination sphere, bearing in mind that $NTs^{2-}$ has a higher donating power than $OPh^-$.

This competition is seen clearly in dpdm and dpmp complexes. When NTs is in an equatorial position, the competing charge transfers result in $\beta$ donation from the OPh ligands and $\alpha$ donation from NTs. With NTs in axial position, the symmetry is trigonal, thus the oxygen atoms from OPh are not well positioned to give efficient overlaps with either dxz or dyz orbitals of the metal: this geometry does not favor strong charge transfer from OPh to dxz or dyz orbitals. Indeed, this weaker donation results in lower spin densities on OPh than when the symmetry is tetragonal. In the latter geometry, which occurs for dpdm and dpmp with NTsₑq or with salan, OPh groups yield strong $\beta$ donation (and high positive spin densities), NTs thus gives preferentially $\alpha$ donation yielding negative spin densities. Interestingly, adding acetonitrile from the trigonal geometry (CN = 6 for dpdm-Cl with S = 2) then gives a tetragonal symmetry, with the two O from phenolates now on the x and y axes. These positions are more favorable for higher donation, thus again the spin density on NTs turns out to be negative (Table S8), as in the case of pentacoordinate tetragonal symmetry. This simple picture explains all cases arising from different positions of OPh and NTs ligands.

To complete the description of the electronic structures, we have represented in Fig. 3 the Kohn-Sham orbital diagram of dpmp-Cl, dpdm-Cl and salan-Cl complexes of Fe(IV) with S = 2 and CN = 5 symmetry. Only $\alpha$ orbitals describing the antibonding d orbitals of Fe(IV) are represented in order to display the ligand field evolution with the ligand and coordination symmetry. Although these orbitals are antibonding combinations of d Fe and $\sigma$ or $\pi$ orbitals of ligands, for the sake of simplicity, we identify them only by the d contribution. Being a $d^4$ high spin configuration, the highest antibonding d orbital is empty, and, in all cases, it is the LUMO of the complex. The orbital energies are given in Table S9.

The ligand field observed for complexes with axial NTs was consistent with a trigonal bipyramid symmetry, with a

<table><thead><tr><th colspan="2" rowspan="2"></th><th>Cl</th><th>Me</th></tr><tr><th></th><th></th></tr></thead><tbody><tr><td rowspan="4">dpdm NTsₑq</td><td>Fe</td><td>3.80</td><td>3.72</td></tr><tr><td>NTs</td><td>−0.38</td><td>−0.29</td></tr><tr><td>OPh1</td><td>0.16</td><td>0.14</td></tr><tr><td>OPh2</td><td>0.21</td><td>0.24</td></tr><tr><td rowspan="4">NTsₐₓ</td><td>Fe</td><td>3.42</td><td>3.04</td></tr><tr><td>NTs</td><td>0.24</td><td>0.64</td></tr><tr><td>OPh1</td><td>0.07</td><td>0.09</td></tr><tr><td>OPh2</td><td>0.19</td><td>0.18</td></tr><tr><td rowspan="4">dpmp NTsₑq</td><td>Fe1</td><td>3.65</td><td>3.60</td></tr><tr><td>NTs</td><td>−0.25</td><td>−0.23</td></tr><tr><td>OPh1</td><td>0.17</td><td>0.18</td></tr><tr><td>OPh2</td><td>0.24</td><td>0.17</td></tr><tr><td rowspan="4">NTsₐₓ</td><td>Fe</td><td>3.25</td><td>3.34</td></tr><tr><td>NTs</td><td>0.47</td><td>0.36</td></tr><tr><td>OPh1</td><td>0.15</td><td>0.15</td></tr><tr><td>OPh2</td><td>0.07</td><td>0.08</td></tr><tr><td rowspan="4">salan</td><td>Fe</td><td>3.87</td><td>3.84</td></tr><tr><td>NTs</td><td>−0.51</td><td>−0.51</td></tr><tr><td>OPh1</td><td>0.21</td><td>0.22</td></tr><tr><td>OPh2</td><td>0.25</td><td>0.27</td></tr></tbody></table>

Table 3 Group spin densities for Fe, NTs and both phenolates from B3LYP SP in gas phase, all complexes being in high spin state. Coordination number is 5 for all complexes. When NTs is equatorial, OPh1 denotes the phenolate in trans to NTs

![](./images/811123434384785410_7.jpg)

Scheme 4 $\beta$ donation (left) or $\alpha$ donation (right) of a $\pi$ lone pair from OPh or NTs ligand to an Fe(IV) high spin ion

![](./images/811123434384785410_8.jpg)

Fig. 3 Left Orbital diagram of dpmp-Cl and dpdm-Cl complexes with NTs in axial position (trigonal symmetry); right orbital diagram of dpmp- Cl, dpdm-Cl with NTs in equatorial position and salan-Cl complexes (tetragonal symmetry). Vertical energy axis in eV. The Kohn-Sham orbital energies were obtained from B3LYP SP calculations. Only $\alpha$ MOs with d antibonding character are presented. The (x, y) plane is defined by Fe, with the two oxygen atoms from OPh groups, z axis being perpendicular to this plane

set of $2 \times d\pi$ (xz, yz), $2 \times d\delta$ (xy, $x^2-y^2$) and $d\sigma$ ($z^2$). A slight destabilization was observed for $d\pi$ and $d\delta$ levels from dpmp to dpdm, in accordance with the greater $\sigma$ donor character of the tertiary amine group in dpdm.

For complexes with dpmp-Cl and dpdm-Cl and equatorial NTs, the symmetry was tetragonal as in salan-Cl. The $d_{x2-y2}$ orbital was the highest unoccupied orbital for dpmp and dpdm ligands as expected for a square-based pyramid.

More generally, the change of dpmp to dpdm did not in- duce noticeable changes in the d orbital scheme.

In the case of salan, the LUMO is an antibonding $d\pi +$ $N_{Ts}\pi$ instead of $d_{x2-y2}$, due to the very strong $\pi$ bond between NTs and Fe, enhanced by the absence of any ligand in trans to NTs. This strong interaction lowers the corresponding bond- ing molecular orbital and raises the antibonding correspond- ing orbital, which thus becomes the LUMO.

It has already been shown by experimental and theoretical studies that nitrene transfers in high-valent Fe occur from an electrophilic active species. The determining step in the mecha- nism of transfer is mostly either an H abstraction from the organic substrate or an electron withdrawal from a C = C bond [9, 34, 35, 37]. Indeed, it has been shown experimentally that the kinetics of transfers may be linearly related to the ionization potential of the substrate, pointing to the important role of electron transfer from the substrate to the active Fe(IV) species in the rate-determining step. The EA of Fe(IV)NTs and BDE of Fe(III)NHTs are thus two key parameters for the reactivity of Fe(IV)NTs active species.

The BDE of the N-H bond is the opposite of the Gibbs energy of the reaction:
$$[FeIV]\text{-NTs}^{n+} + \text{H$\cdot$}\to[FeIII]\text{-NHTs}^{n+}$$

It measures the affinity of the nitrene species for an H atom from any substrate.

The EA measures the affinity for an electron through the Gibbs energy of the following reaction:
$$[FeIV]\text{-NTs}^{n+} + \text{e$\to$}[FeIII]\text{-NTs}^{(n-1)+}$$

We calculated both parameters for the complexes studied here, and compared with other Fe(IV)NTs species from the literature (Table 4).

At this point it should be noted that energy differences lower than ca. 0.2 eV or 5 kcal mol $^{-1}$ at this level of theory cannot be considered significant. Examining firstly the EAs, the Cl-substituted complexes of dpmp and dpdm exhibit values similar to that of Que's complex N4PyFe(IV)NTs. The Me-substituted ligand yields a lower EA for dpmp with $NTs_{ax}$ (104.4 kcal mol $^{-1}$) than the Cl-substituted analogue (122.9 kcal mol $^{-1}$), probably due to the inductive donor effect of $CH_3$ substituents that enriches the complex in electron den- sity, thus lowering its electrophilicity. Compared to the abovementioned highly active binuclear species, the mononu- clear species seem to be less electrophilic; nevertheless, the differences in EA are weak.

There is no clear difference between the BDEs, all being in a range from 95 kcal mol $^{-1}$ to 99 kcal mol $^{-1}$, except for the dpdm ligand where the values are higher than 100 kcal mol $^{-1}$. Overall, these values are rather high when compared to the BDE of the CH bond of possible aliphatic substrates, which indicates that these complexes are prone to give insertion re- actions through the abstraction of H/rebound process well- known for alkane hydroxylation. Indeed, such amination re- actions have been observed with difficult substrates such as THF (BDE = 92 kcal mol $^{-1}$ [54]) or cyclohexane (BDE = 96-100 kcal mol $^{-1}$ [55]) with the binuclear species [24, 26] or with the dpmp-Cl complex [R. Patra et al., unpublished data]. In contrast to the EAs, the substitution of Cl by Me does not

![](./images/811123434384785410_9.jpg)

<table><thead><tr><th>Table 4</th><th colspan="7">Electron affinity-bond dissociation energy (EA-BDE; kcal mol⁻¹) of dpmp (Cl and Me), dpdm-Cl and salan-Cl Fe(IV) complexes with NTs axial or equatorial, calculated from B3LYP solvent single points (SP) including zero point energy (ZPE) from OPBE geometry optimizations (see Computational details). Both binuclear complexes [24, 26] and the N4Py complex from Que [9] are mentioned</th></tr><tr><th></th><th colspan="2">dpmp-Cl</th><th>dpmp-Me</th><th colspan="2">dpdm-Cl</th><th>salan-Cl</th><th>Fe₂(III,IV)</th><th>Fe₂(III,V)</th><th>N4pyFe(IV)</th></tr><tr><th></th><th>NTsₐₓ</th><th>NTs_eq</th><th>NTsₐₓ</th><th>NTsₐₓ</th><th>NTs_eq</th><th>NTsₐₓ</th><th>[24]</th><th>[26]</th><th>[9]</th></tr></thead><tbody><tr><td>BDE</td><td>95.8</td><td>97.7</td><td>99.0</td><td>101.7</td><td>105.9</td><td>95.3</td><td>97.7</td><td>97.8</td><td>94.4</td></tr><tr><td>EA</td><td>122.9</td><td>118.3</td><td>104.4</td><td>121.4</td><td>119.9</td><td>115.6</td><td>130.1</td><td>150.9</td><td>120.5</td></tr></tbody></table>

change the BDE for dpmp much. The main evolution when changing the ligand structure is the higher BDE obtained for dpdm-Cl complexes, although energy differences with dpmp homologues are weak, being between 6 kcal mol⁻¹ and 8 kcal mol⁻¹. This increase in BDE from the pyridine donor (in dpmp) to the dimethyl amine donor (in dpdm) may be explained by examining the elementary steps that constitute the H-bond dissociation process in a general complex [Fe(IV)NTs], as represented below:

![](./images/811123434384785410_10.jpg)

Thus $\text{BDE} = \text{EA} + \Delta G_{\text{ac}} - \text{IE}_{\text{H}}$, where $\text{IE}_{\text{H}}$ is the ionization potential of H atom, and $\Delta G_{\text{ac}}$ (>0) is the acidity free energy of the reduced conjugated acid [Fe(III)NHTs]. This equation shows that the BDE results from a competition between the EA and the basicity of the reduced [Fe(III)NTs]⁻ species. From an intuitive chemical sense, increasing the electron density on the complex decreases the EA but it may increase the basicity of the reduced species. Therefore, the $\Delta G_{\text{ac}}$ positive term will increase, thus the BDE may increase. In the case of dpdm, the change of pyridine to the NMe₂, which is more basic, may reinforce the basicity of the reduced species, thus increasing the BDE.

## Discussion

In the rationalization of oxygen transfers and, more recently, nitrene transfers through Fe complexes, an important parameter has been shown to be the ground spin state of the high-valent Fe(IV) active species, as shown in previous studies [8, 37, 56]. This is generally explained by the fact that the intermediate species formed in the first step of reaction with the substrate is an Fe(III) containing complex due to either an electron or H• transfer from the substrate. If the initial spin state of Fe(IV) is S = 2, it is thus possible to generate an intermediate Fe(III) S = 5/2 complex by electron transfer on the last unoccupied d orbital of the initial Fe(IV). This intermediate gets strongly stabilized by high exchange energy, giving thus a low-energy barrier pathway [56]. As mentioned above, it so happens that many—but not all—the Fe(IV)-NTs synthetic complexes published have a S = 1 spin state and yield a low-to-moderate activity towards nitrene transfers. The complexes described here are high-spin ground state thanks firstly to the low coordination number (CN = 5) of the complexes, which weakens the ligand field. Indeed this unsaturated low coordination of the high-valent Fe ion is stabilized thanks to the presence of strong anionic donating ligands, i.e., phenolates. The second explanation for stabilization of the S = 2 spin state is that it is well known from ligand field theory that π-donating groups such as phenolate favor a low ligand field, thus a high spin state. Indeed, preliminary nitrene transfer reactions such as aziridinations or aminations of C–H aliphatic substrates on the dpmp-Cl complex are indeed much more efficient than previously described complexes in the literature [33]. This efficiency is seen through the very fast aziridination reactions, and the ability to insert the NTs group into known difficult aliphatic C–H substrates such as cyclohexane.

Two other important quantities known to control the efficiency of such active complexes for nitrene transfers are the EA of Fe(IV)NTS and BDE of the Fe(III)NHTs species. Compared to the literature, where such values are rare for Fe(IV)NR species, EA and BDEs for our complexes are among the highest seen. Another major objective of this study was to examine the variations of these parameters with the structure of the ligand (dpdm vs dpmp vs salan). Although some changes occur in the ligand field descriptions of the orbitals depending on the relative positions of the π-donor NTs and OPh groups, and of the σ-donor amine groups, the resulting electrophilicity is not modified much, and neither is the overall electronic structure. A slight increase in the BDE was observed for the dpdm ligand, probably due to the increased basicity of the ligand. This means that the dpdm ligand should yield particularly efficient Fe(IV) catalysts for reactions based on an H atom abstraction such as nitrene insertion into C–H aliphatic substrates. Another important result is that electro-attractive substituents on the phenolate ligands do increase the electrophilic nature of the complex, as observed here when changing Me to Cl. Our calculations help quantify this effect, which is quite high, with an increase in

![](./images/811123434384785410_11.jpg)

EA of $20\ \text{kcal mol}^{-1}$ from Me to Cl. More electroattracting substituents are thus expected to increase this EA, and provide still more active complexes.

## Conclusions
The electronic properties of Fe(IV)NTs complexes with systematic variation of tetradentate ligand structures have been examined in light of their capacity to be active in nitrene transfer reactions. This activity is known from experimental and theoretical data in the literature to be related to a high electrophilicity of the Fe(IV) active species and to a $S=2$ ground state. The tetradentate ligands explored here provide a good compromise in this objective. They stabilize the $S=2$ state thanks firstly to a pentacoordination mode, although a solvent may coordinate without much energetic cost, and secondly by $\pi$-donating groups (phenolates and NTs). Although these ligands are anionic, this is not detrimental for the electrophilicity of the complexes, which is close to a neutral ligand analogue (N4py). These ligands also provide a good opportunity to have a high BDE, especially dpdm-Cl because the latter favors a high basicity of the reduced species, which is also a key point for nitrene transfers into C–H aliphatic bonds.

Finally, investigations into various positions of donor groups in the coordination sphere of the Fe(IV)NTs active species show that the important point is not their relative positioning but the nature and number of donor groups. Indeed our calculations here have revealed that the tetradentate mode, combined with highly anionic $\pi$-donor groups, was responsible for the high stability of the high spin active species and high EA and BDEs. The present study thus paves the way for further improved design of ligands for still more active catalysts in nitrene transfers, while some theoretical mechanistic studies are underway.

## Acknowledgments
We thank Labex ARCANE (ANR-11-LABX-0003-01) for financial support. P.M. thanks GENCI-CINES for providing CPU resources through Grant 2015–089173. J.-M. Latour is acknowledged for fruitful discussions and suggestions.

## References
1.  Hili R, Yudin AK (2006) Making carbon-nitrogen bonds in biological and chemical synthesis. Nat Chem Biol 2:284–287. doi:10.1038/nchembio0606-284
2.  Roizen JL, Harvey ME, Bois JD (2012) Metal-catalyzed nitrogen-atom transfer methods for the oxidation of aliphatic C–H bonds. Acc Chem Res 45:911–922. doi:10.1021/ar200318q
3.  Dequirez G, Pons V, Dauban P (2012) Nitrene chemistry in organic synthesis: still in its infancy? Angew Chem Int Ed 51:7384–7395
4.  Roughley SD, Jordan AM (2011) The medicinal chemist’s toolbox: an analysis of reactions used in the pursuit of drug candidates. J Med Chem 54:3451–3479. doi:10.1021/jm200187y
5.  Chang JWW, Ton TMU, Chan PWH (2011) Transition-metal-catalyzed aminations and aziridinations of CH and CC bonds with iminoiodinanes. Chem Rec 11:331–357
6.  Fiori KW, DuBois J (2007) Catalytic intermolecular amination of C – H bonds: method development and mechanistic insights. J Am Chem Soc 129:562–568. doi:10.1021/ja0650450
7.  Au SM, Huang JS, Yu WY et al (1999) Aziridination of alkenes and amidation of alkanes by Bis(tosylimido)ruthenium(VI) porphyrins. A mechanistic study. J Am Chem Soc 121:9120–9132
8.  King ER, Hennessy TA, Betley TA (2011) Catalytic C – H bond amination from high-spin iron imido complexes. J Am Chem Soc 133:4917–4923. doi:10.1021/ja110066j
9.  Vardhaman AK, Barman P, Kumar S et al (2013) Comparison of the reactivity of nonheme iron(IV)–oxo versus iron(IV)–imido complexes: which is the better oxidant? Angew Chem Int Ed 52:12288–12292. doi:10.1002/anie.201305370
10. Liu Y, Guan X, Wong EL-M et al (2013) Nonheme iron-mediated amination of C(sp3)–H bonds. Quinquepyridine-supported iron-imide/nitrene intermediates by experimental studies and DFT calculations. J Am Chem Soc 135:7194–7204. doi:10.1021/ja3122526
11. Chandrachud PP, Jenkins DM (2015) High valent FeIV chemistry in sustainable oxidation catalysis. Tetrahedron Lett 56:2369–2376
12. Mahy J-P, Bedi G, Battioni P, Mansuy D (1988) Aziridination of alkenes catalysed by porphyrinirons: selection of catalysts for optimal efficiency and stereospecificity. J Chem Soc Perkin Trans 2:1517–1524. doi:10.1039/P29880001517
13. Leeladee P, Jameson GNL, Siegler MA et al (2013) Generation of a high-valent iron imido corrolazine complex and NR group transfer reactivity. Inorg Chem 52:4668–4682. doi:10.1021/ic400280x
14. Moreau Y, Chen H, Derat E et al (2007) NR transfer reactivity of azo-compound I of P450. How does the nitrogen substituent tune the reactivity of the species toward CH and CC activation? J Phys Chem B 111:10288–10299. doi:10.1021/jp0743065
15. Rittle J, Green MT (2010) Cytochrome P450 compound I: capture, characterization, and C-H bond activation kinetics. Science 330:933–937. doi:10.1126/science.1193478
16. Hohenberger J, Ray K, Meyer K (2012) The biology and chemistry of high-valent iron-oxo and iron-nitrido complexes. Nat Commun 3:720. doi:10.1038/ncomms1718
17. McDonald AR, Jr LQ (2013) High-valent nonheme iron-oxo complexes: synthesis, structure, and spectroscopy. Coord Chem Rev 257:414–428. doi:10.1016/j.ccr.2012.08.002
18. Farwell CC, Zhang RK, McIntosh JA et al (2015) Enantioselective enzyme-catalyzed aziridination enabled by active-site evolution of a cytochrome P450. ACS Cent Sci 1:89–93
19. Klinker EJ, Jackson TA, Jensen MP et al (2006) A tosylimido analogue of a nonheme oxoiron(IV) complex. Angew Chem Int Ed 45:7394–7397. doi:10.1002/anie.200602799
20. Cowley RE, Eckert NA, Vaddadi S et al (2011) Selectivity and mechanism of hydrogen atom transfer by an isolable imidoiron(III) complex. J Am Chem Soc 133:9796–9811
21. Mehn MP, Peters JC (2006) Mid- to high-valent imido and nitrido complexes of iron. J Inorg Biochem 100:634–643. doi:10.1016/j.jinorgbio.2006.01.023
22. Thomas CM, Mankad NP, Peters JC (2006) Characterization of the terminal iron(IV) imides [PhBPtBu2(pz’)]FeIV : NAd+. J Am Chem Soc 128:4956–4957. doi:10.1021/ja0604358
23. Nieto I, Ding F, Bontchev RP et al (2008) Thermodynamics of hydrogen atom transfer to a high-valent iron imido complex. J Am Chem Soc 130:2716–2717. doi:10.1021/ja0776834
24. Gouré E, Avenier F, Dubourdeaux P et al (2014) A diiron(III, IV) imido species very active in nitrene-transfer reactions. Angew Chem Int Ed 53:1580–1584. doi:10.1002/anie.201307429
25. 25. Avenier F, Latour J-M (2004) Catalytic aziridination of olefins and amidation of thioanisole by a non-heme iron complex. Chem Commun 1544–1545.

![](./images/811123434384785410_12.jpg)

26. Gouré E, Senthilnathan D, Coin G et al (2016) Tautomeric equilib- rium within an imido amido diiron species and catalytic two-stage nitrene transfers. Submitted

27. Velusamy M, Palaniandavar M, Gopalan RS, Kulkami GU (2003) Novel iron(III) complexes of tripodal and linear tetradentate bis(phenolate) ligands: close relevance to intradiol-cleaving catechol dioxygenases. Inorg Chem 42:8283-8293. doi:10.1021/ic020569w

28. Kurahashi T, Oda K, Sugimoto M et al (2006) Trigonal-bipyramidal geometry induced by an external water ligand in a sterically hin- dered iron salen complex, related to the active site of protocatechuate 3,4-dioxygenase. Inorg Chem 45:7709-7721. doi:10.1021/ic060650p

29. Zhu K, Shaver MP, Thomas SP (2016) Amine-bis(phenolate) iron(III)-catalyzed formal hydroamination of olefins. Chem AsianJ 11:977-980. doi:10.1002/asia.201501098

30. Reckling AM, Martin D, Dawe LN et al (2011) Structure and C-C cross-coupling reactivity of iron(III) complexes of halogenated amine-bis(phenolate) ligands. J Organomet Chem 696:787-794.doi:10.1016/j.jorganchem.2010.09.076

31. Poli R, Shaver MP (2014) Atom transfer radical polymerization (ATRP) and organometallic mediated radical polymerization (OMRP) of styrene mediated by diaminobis(phenolato)iron(II) complexes: a DFT study.Inorg Chem 53:7580-7590. doi:10.1021/ic5009347

32. Hasan K, Fowler C, Kwong P et al (2008) Synthesis and structure ofiron(III) diamine-bis(phenolate) complexes. Dalton Trans 2991-2998

33. R. Patra et al (2016) To be published

34. Kumar S, Faponle AS, Barman P et al (2014) Long-range electron transfer triggers mechanistic differences between iron(IV)-oxo and iron(IV)-imido oxidants. J Am Chem Soc 136:17102-17115. doi:10.1021/ja508403w

35. Hennessy ET, Liu RY, Iovan DA et al (2014) Iron-mediated inter- molecular N-group transfer chemistry with olefinic substrates. Chem Sci 5:1526-1532. doi:10.1039/C3SC52533C

36. Wang L, Hu L, Zhang H et al (2015) Three-coordinate iron(IV) bisimido complexes with aminocarbene ligation: synthesis, struc- ture, and reactivity. J Am Chem Soc 137:14196-14207.doi:10.1021/jacs.5b09579

37. Vardhaman AK, Lee Y-M, Jung J et al (2016) Enhanced electron transfer reactivity of a nonheme iron(IV)-imido complex as com- pared to the iron(IV)-oxo analogue. Angew Chem Int Ed 55:3709-3713. doi:10.1002/anie.201600287

38. te Velde G, Bickelhaupt FM, Baerends EJ et al (2001) Chemistrywith ADF. J Comput Chem 22:931-967. doi:10.1002/jcc.1056

39. SCM, Vrije Universiteit ADF 2010. SCM, Amsterdam, The Netherlands

40. Perdew JP, Ernzerhof M, Burke K (1996) Rationale for mixing exact exchange with density functional approximations. J ChemPhys 105:9982-9985. doi:10.1063/1.472933

41. Handy NC, Cohen AJ (2001) Left-right correlation energy. MolPhys 99:403-412. doi:10.1080/00268970010018431

42. Hoe W-M, Cohen AJ, Handy NC (2001) Assessment of a new local exchange functional {OPTX}. Chem Phys Lett 341:319-328.doi:10.1016/S0009-2614(01)00581-4

43. Swart M, Ehlers AW, Lammertsma K (2004) Performance of the OPBE exchange-correlation functional. Mol Phys 102:2467-2474.doi:10.1080/0026897042000275017

44. Swart M (2008) Accurate spin-state energies for iron complexes. J Chem Theory Comput 4:2057-2066. doi:10.1021/ct800277a

45. Conradie J, Ghosh A (2007) Electronic structure of trigonal-planar transition-metal - imido complexes: spin-state energetics, spin- density profiles, and the remarkable performance of the OLYP func-tional. J Chem Theory Comput 3:689-702

46. Swart M (2007) Metal-ligand bonding in metallocenes: differenti- ation between spin state, electrostatic and covalent bonding. InorgChim Acta 360:179-189. doi:10.1016/j.ica.2006.07.073

47. Noodleman L, Han W-G (2006) Structure, redox, pKa, spin. A golden tetrad for understanding metalloenzyme energetics and reaction path- ways. JBIC J Biol Inorg Chem 11:674-694. doi:10.1007/s00775-006-0136-3

48. Stephens PJ, Devlin FJ, Chabalowski CF, Frisch MJ (1994) Ab Initio calculation of vibrational absorption and circular dichroismspectra using density functional force fields. J Phys Chem 98:11623-11627. doi:10.1021/j100096a001

49. Reiher M, Salomon O, Artur Hess B (2001) Reparameterization of hybrid functionals based on energy differences of states of different multiplicity. Theor Chem Accounts 107:48-55. doi:10.1007/s00214-001-0300-3

50. Adamo C, Barone V (1999) Toward reliable density functional methods without adjustable parameters: the PBE0 model. J ChemPhys 110:6158-6170

51. Tao J, Perdew JP, Staroverov VN, Scuseria GE (2003) Climbing the density functional ladder: nonempirical meta\char21generalized gradient approximation designed for molecules and solids. PhysRev Lett 91:146401. doi:10.1103/PhysRevLett.91.146401

52. Staroverov VN, Scuseria GE, Tao J, Perdew JP (2003) Comparative assessment of a new nonempirical density functional: molecules and hydrogen-bonded complexes. J Chem Phys 119:12129-12137. doi:10.1063/1.1626543

53. Jaccob M, Rajaraman G (2012) A computational examination on the structure, spin-state energetics and spectroscopic parameters of high-valent FeIV[double bond, length as m-dash]NTs species. Dalton Trans 41:10430-10439. doi:10.1039/C2DT31071F

54. Laarhoven LJJ, Mulder P, Wayner DDM (1999) Determination of bond dissociation enthalpies in solution by photoacoustic calorim-etry. Acc Chem Res 32:342-349. doi:10.1021/ar9703443

55. Tian Z, Fattahi A, Lis L, Kass SR (2006) Cycloalkane and cycloalkene C-H bond dissociation energies. J Am Chem Soc128:17087-17092. doi:10.1021/ja065348u

56. Shaik S, Hirao H, Kumar D (2007) Reactivity of high-valent iron- oxo species in enzymes and synthetic reagents: a tale of many states. Acc Chem Res 40:532-542. doi:10.1021/ar600042c

![](./images/811123434384785410_13.jpg)
**COMMUNICATION**
View Article Online
View Journal | View Issue

![](./images/852937837253754880_1.jpg)
Cite this: *Chem. Commun.*, 2023,
59,5055

Received 27th February 2023,
Accepted 31st March 2023

DOI: 10.1039/d3cc00960b

rsc.li/chemcomm

# First-principles study of interfacial features and charge dynamics between spiro-MeOTAD and photoactive lead halide perovskites†

Adriana Pecoraro, $^{a}$ Francesca Fasulo, $^{b}$ Michele Pavone $^{bc}$ and Ana B. Muñoz-García $^{*ac}$

The main stability and performance issues of perovskite solar cells arise from the interfaces between the perovskite and the hole transport material. Here we address these interface issues by means of state-of-the-art first-principles calculations, providing new insights into charge transfer times and mechanisms and how they depend on the perovskite chemical composition and local interfacial environment.

Solar cells with hybrid organic-inorganic lead halide perovskites (LHPs) as photoactive moieties revolutionized the photovoltaic scenario, thanks to their intrinsic properties such as low exciton binding energies, high absorption coefficients, and long charge carrier lifetimes. $^{1}$ The efficiencies of perovskite solar cells (PSCs) rapidly increased when moving from the original methylammonium lead triiodide (MAPbI₃, MAPI) to LHPs with mixed cationic and/or anionic compositions. $^{2}$ In particular, the triple cation/dual anion $Cs_{0.05}(FA_{0.83}MA_{0.17})_{0.95}Pb(I_{0.83}Br_{0.17})_{3}$ stoichiometry with $MA=CH_{3}NH_{3}^{+}$, $FA=HC(NH_{2})^{+}$ (called triLHP in this work) has become a standard in PSCs due to its high efficiency, improved stability and device reproducibility. $^{3}$ This improvement has been ascribed to an entropy-induced major structural stability of the LHP, diminished defect content and better electronic properties. $^{4}$ Here, we aim at assessing if and to what extent compositional changes from MAPI to triLHP also affect charge transfer (CT) properties at the LHP/spiro-MeOTAD interface, being spiro-MeOTAD the archetypal hole transport material (HTM) used in start-of-the-art PSCs. $^{5,6}$ In particular, we use hybrid density functional theory (DFT)-based calculations to study interfacial structural and electronic features, and, for the first time, we outline the charge dynamics features of such interfaces and estimate hole injection rates with the projection-operator diabatization (POD) approach, $^{7}$ as recently applied for the MAPI/TiO₂ interface. $^{8}$

The computational details and structural models of the bulk LHP (Fig. S1, ESI†) and interfaces studied in this work are collected in the ESI.† A comprehensive discussion on the thermodynamic stability of PSC interfaces is provided in a recent review. $^{9}$ To build LHP/spiro-MeOTAD interfaces, we considered the thermodynamically favored (010) surface¹⁰ with both AX terminations (A = MA in MAPI or Cs, FA, MA in triLHP) and PbX₂ terminations (X = I in MAPI or I, Br in triLHP) since surface terminations have been found to influence the energy of spiro-MeOTAD frontier orbitals¹¹ and because we are interested in relating the CT features to changes in chemical interactions. For these reasons, we also considered different local compositions of both terminations in triLHP (Fig. S2, ESI†): AX terminations exposing or not the Cs atom (CSFAMAX and FAMAX in the text, respectively), plus an additional CSFAMAX layer with a maximized interaction of Cs with the most active methoxy groups of spiro-MeOTAD, $^{12,13}$ CSFAMAX(O-Cs). Similarly, we considered two PbX₂-terminated surfaces, lacking or containing a Cs atom at the subsurface layer, PbX₂ and PbX₂(Cs), respectively. The minimum-energy structures of all these interfaces are shown in Fig. 1a. The most stable interfaces have been determined in terms of binding energies $(E_{b})$ between the LHP and spiro-MeOTAD moieties computed as $E_{b}=E_{LHP/Spiro}-E_{LHP}-E_{Spiro}$, where $E_{LHP/Spiro}$, $E_{LHP}$ and $E_{Spiro}$ are the electronic energies of the fully relaxed interfaces, isolated LHP surfaces, and isolated spiro-MeOTAD molecule, respectively. Total $E_{b}$ values have been further decomposed into three main contributions:

$$
\begin{aligned}
E_{\mathrm{b}}=E_{\mathrm{a}}+E_{\mathrm{d}}^{\mathrm{Spiro}}+E_{\mathrm{d}}^{\mathrm{LHP}}&=\left(E_{\mathrm{LHP/Spiro}}-E_{\mathrm{LHP}*}-E_{\mathrm{Spiro}*}\right)\\
&+\left(E_{\mathrm{Spiro}*}-E_{\mathrm{Spiro}}\right)+\left(E_{\mathrm{LHP}*}-E_{\mathrm{LHP}}\right) \tag{1}
\end{aligned}
$$

The first contribution is the adhesion energy $(E_{a})$ and stems from the electronic interaction between the moieties and it is calculated from the LHP and spiro-MeOTAD energies at the interface geometries ($E_{\mathrm{LHP}*}$ and $E_{\mathrm{Spiro}*}$). These energetic terms

---
$^{a}$ Department of Physics "E. Pancini", University of Naples Federico II, Napoli, Italy.
E-mail: anabelen.munozgarcia@unina.it
$^{b}$ Department of Chemical Sciences, University of Naples Federico II, Napoli, Italy
$^{c}$ National Reference Center for Electrochemical Energy Storage (GISEL)-INSTM, Florence, Italy
† Electronic supplementary information (ESI) available: Computational details and supporting results. See DOI: https://doi.org/10.1039/d3cc00960b

# Communication

![](./images/852937837253754880_2.jpg)

Fig. 1 (a) Lateral views of the relaxed LHP/spiro-MeOTAD (LHP = MAPI or triLHP) interfaces with AX- and $PbX_2$-type terminations showing electron density difference isosurfaces upon interface formation. Only the two outermost layers of each LHP are shown for the ease of viewing. Yellow and blue regions denote charge accumulation and depletion zones, respectively. Isosurface value = $0.001\ \text{e}^-\ \text{bohr}^{-3}$. (b) Decompositions of the binding energies of spiro-MeOTAD on different LHP terminations and chemical environments according to eqn (1).

allow us to also evaluate the distortion energies of spiro-MeOTAD ($E_\text{d}^\text{Spiro}$) and LHP ($E_\text{d}^\text{LHP}$), accounting for energetic penalties due to conformational changes upon interface formation. Defined in this way, $E_\text{a}$ is an attractive (negative) term, while distortion energies are positive quantities that partially compensate $E_\text{a}$ to deliver the final $E_\text{b}$. This analysis is displayed in Fig. 1b, while the corresponding numerical values are listed in Table S1 (ESI†).

Our results reveal an opposite affinity of the spiro-MeOTAD molecule for either termination depending on LHP composition: while adsorption on the MAI surface is preferred for MAPI, $PbX_2$ is preferred for triLHP. Moreover, Cs appears to have a stabilizing effect in the MA terminated triLHP when linked to the methoxy group of spiro-MeOTAD: FAMAX and CsFAMAX(O-Cs) deliver similar $E_\text{b}$, with binding in CsFAMAX being less convenient.

Regarding $PbX_2$ termination in LHP, the presence of Cs in the subsurface layer reinforces the $PbX_2$(Cs)/spiro-MeOTAD binding with respect to $PbX_2$/spiro-MeOTAD by $\sim$1 eV, making the $PbX_2$(Cs)/spiro-MeOTAD the most stable interface among all explored interfaces ($\sim -4.5$ eV). The binding energy trends reflect both the structural and electronic features of the interface. On one hand, more negative binding energies correspond to the closest molecule/surface distances, as discussed in the ESI† (Fig. S3 and Table S1). On the other hand, the dominant term in $E_\text{b}$ is the adhesion energy, which suggests a mostly electronic interaction, with low distortion energies for both components, especially for the surface, with a low conformational freedom involving only cations of the topmost layer (Fig. S4, ESI†). A more in-depth structural analysis of structural rearrangements on spiro-MeOTAD is reported in Fig. S5 (ESI†). At all LHP interfaces, the angles of the main fluorene moiety and the -methoxyphenyl residues vary by $2^\circ$ and $4^\circ$, respectively, compared to the free spiro-MeOTAD molecule. These structural variations occur with an elongation of the methoxy $\text{CH}_3$-O bond of $\sim 0.02/0.03\ \mathring{\text{A}}$ at the most stable triLHP($PbX_2$(Cs))/spiro-MeOTAD interface. The electronic nature of the LHP/spiro-MeOTAD interaction is depicted by the charge density difference plots (Fig. 1a). Most of the charge rearrangement at the interface involves the fluorene ring and the methoxy groups of spiro-MeOTAD, which interact predominantly with the A cation and with the Pb atoms of AX and $PbX_2$ termina-tions, in agreement with previous investigations.$^{12,13}$ This analysis points out also a direct role of the Cs atom in stabilizing the interaction with spiro-MeOTAD. In the CsFAMAX(O-Cs) system, the increased charge density along the methoxy O-Cs bond and the O-Cs distance ($\sim 3.25\ \mathring{\text{A}}$) suggests the formation of direct bonding.$^{14}$ Also the strongest binding in the $PbX_2$(Cs) system is accompanied by a pronounced charge rearrangement involving the whole interface.

On these interfaces, we computed the atom-projected density of states (pDOS; see Fig. S6, ESI†) to obtain a first qualitative indication of frontier orbital energetics and the thermodynamic feasibility of CT. In all the cases, the spiro-MeOTAD highest occupied molecular orbital (HOMO) lies at higher energy than the LHP valence band maximum (VBM), providing a convenient driving force for hole injection. The energy difference between the donor and the acceptor band edges is the largest for the $PbX_2$ terminations of both LHPs, suggesting a more effective transfer process than that in AX ones, as also pointed out by Wang *et al.*.$^{15}$ Nevertheless, a driving force of $\sim 0.2$ eV or higher is sufficient for efficient CT, so all the considered interfaces are in principle suitable.$^{16}$ The pDOS plots also indicate the presence of several $\text{HOMO}-X$ ($X = 1, 2, 3...$) states, lying at higher energies than the LHP VBM, which can behave as additional CT channels. Motivated by this finding, we calculated the donor-acceptor coupling matrix elements for transitions occurring between both the HOMO and HOMO$-$1 molecular orbitals (MOs) of spiro-MeOTAD and the LHP VBM. Since the hole transfer process from the LHP VBM to the spiro-MeOTAD HOMO is conceptually equivalent to an electron transfer in the opposite direction, we consider spiro-MeOTAD as the electron donor, while the LHP acts as the acceptor. We calculated the spectral function $\Gamma_\text{d}(E)$ from electronic couplings:

$$
\Gamma_{\mathrm{d}}(E)=2 \pi \sum_{\mathrm{a}}\left|V_{\mathrm{ad}}\right|^{2} \delta\left(E-\varepsilon_{\mathrm{a}}\right) \tag{2}
$$

where $V_\text{ad}$ is the electronic coupling matrix element between the diabatic donor d state and the acceptor a state of the perovskite valence band, with energy $\varepsilon_\text{a}$. This function can be regarded as an estimate of the donor state decay width and provides information on the CT process timescale. In particular, the time for hole

![](./images/852937837253754880_3.jpg)

Fig. 2 Left panels: coupling matrix elements $|V_{ad}|$ between the spiro-MeOTAD HOMO and HOMO-1 donor states and LHP VB acceptor states and spectral function $\Gamma(E)$ calculated according to eqn (2) for (a) AX-type and (b) PbX$_2$-type interfaces. The spiro-MeOTAD donor state is represented by red vertical lines in $|V_{ad}|$ and $\Gamma(E)$ plots. Right panels: Atom-projected density of states (pDOS) computed at the HSE06 level of theory.

injection can be calculated in terms of the spectral function as $\tau = \hbar/\Gamma$. Coupling elements $|V_{ad}|$ and spectral functions $\Gamma$ for both the spiro-MeOTAD HOMO and HOMO-1 and LHP AX- and PbX$_2$-type surfaces are depicted in Fig. 2 (left panels). For the AX interfaces of both MAPI and triLHP, couplings are higher and the spectral function presents a more structured character in the low energy region (between $-9$ and $-6$ eV). The involvement of such deep states is consistent with recent experimental findings by Droseros *et al.* on different HTM/MAPI interfaces.$^{17}$ They observed an ultrafast charge injection at the tris(4-carbazoyl-9-ylphenyl)amine/MAPI interface in spite of a negative HOMO offset. This suggests that the hole injection takes place from perovskite states that lie deep in the VB, thus fulfilling the thermodynamic requirement. Concerning spiro-MeOTAD MOs, the highest coupling occurs when HOMO-1 is involved for most AX surfaces (MAPI-MAI, triLHP-FAMAX and triLHP-CsFAMAX-(O-Cs), being triLHP-CsFAMAX an exception, with the highest couplings with the spiro-MeOTAD HOMO within the same energy range. Regarding the PbX$_2$-type terminations, MAPI-PbI$_2$ and triLHP-PbX$_2$(Cs) present the best couplings with spiro-MeOTAD HOMO-1 MO, while only triLHP-PbX$_2$ couples more efficiently with the spiro-MeOTAD HOMO. For this termination, hole injection is more likely to occur in the $-2$ to $-4$ eV energy region rather than through deep VB states ($-9$ eV $< E_{\text{a}} - E_{\text{F}} < -6$ eV).

The actual LHP states involved in the CT process can be extracted from the atom-projected pDOS, as shown in Fig. 2 (right panels). The low energy region with the highest couplings at AX-interfaces is composed of spiro-MeOTAD oxygen p states and MA/FA cations. While in CsFAMAX Cs states are not present in the $-6$ to $-9$ eV region, such states appear in CsFAMAX-OCs, where couplings are much higher. All pDOS for PbX$_2$ derived interfaces feature mixed Pb and halide states interacting with spiro-MeOTAD oxygen p states in the $-2$ to $-4$ eV region. Also in this case, Cs states correlated to higher couplings appear for triLHP-PbX$_2$(Cs). To gain insight on the nature of donor states and clarify the differences between HOMO and HOMO-1 in terms of couplings, we show interfacial spiro-MeOTAD MOs and the corresponding energies in Fig. 3. For comparison, the same orbitals for isolated spiro-MeOTAD are plotted in Fig. S7 (ESI$\dagger$).

As suggested in other works,$^{18}$ our calculations predict a surface-induced light-to-moderate degeneracy loss between HOMO and HOMO-1 (separated by only 0.04 eV in the isolated molecule) for interfacial spiro-MeOTAD with energy differences from 0.08 to 0.37 eV. As shown in Fig. 3, either the HOMO-1 or HOMO orbital points to the surface, while the other MO points to the vacuum region. For all surfaces explored, the highest couplings occur through such MO oriented towards the surface, *i.e.* HOMO-1 for MAPI-MAI and PbI$_2$, triLHP-FAMAX and PbX$_2$(Cs) and HOMO for triLHP-PbX$_2$. An exception, and apparent contradiction, occurs for triLHP-CsFAMAX and CsFAMAX(O-Cs) cases, where more advantageous couplings occur through HOMO and HOMO-1 MOs, respectively, which are not spatially located towards the perovskite surface. Still, a closer look at these MOs (Fig. S8, ESI$\dagger$) can explain this finding: they comprise the methoxy group directly linked to the Cs-rich surface at 2.43 Å and 3.25 Å for

![](./images/852937837253754880_4.jpg)

Fig. 3 Spiro-MeOTAD HOMO and HOMO-1 MOs and difference in energy between HOMO and HOMO-1 ($\Delta E = E_{\text{HOMO}} - E_{\text{HOMO-1}}$) for all LHP/spiro-MeOTAD interfaces.

**Communication**

Table 1 Computed hole injection times ($\tau$) between donor spiro-MeOTAD HOMO or HOMO$-$1 and LHP valence band (VB) acceptor states

<table>
<thead>
<tr>
<th></th>
<th>MAPI</th>
<th colspan="3">triLHP</th>
</tr>
<tr>
<th></th>
<th>MAI</th>
<th>FAMAX</th>
<th>CsFAMAX</th>
<th>CSFAMAX(O$-$Cs)</th>
</tr>
<tr>
<th colspan="5">$\tau$ (ps): AX-type</th>
</tr>
</thead>
<tbody>
<tr>
<td>HOMO $\rightarrow$ VB</td>
<td>11.7</td>
<td>38.7</td>
<td>5.70</td>
<td>16.7</td>
</tr>
<tr>
<td>HOMO$-$1 $\rightarrow$ VB</td>
<td>1.80</td>
<td>1.65</td>
<td>12.9</td>
<td>2.50</td>
</tr>
<tr>
<th colspan="5">$\tau$ (ps): PbX$_2$-type</th>
</tr>
<tr>
<td></td>
<td>PbI$_2$</td>
<td>PbX$_2$</td>
<td colspan="2">PbX$_2$(Cs)</td>
</tr>
<tr>
<td>HOMO $\rightarrow$ VB</td>
<td>31.6</td>
<td>5.24</td>
<td colspan="2">14.3</td>
</tr>
<tr>
<td>HOMO$-$1 $\rightarrow$ VB</td>
<td>4.93</td>
<td>13.1</td>
<td colspan="2">2.68</td>
</tr>
</tbody>
</table>

CsFAMAX and CsFAMAX(O$-$Cs), respectively. Particularly for the CsFAMAX(O$-$Cs)/HOMO$-$1 case, strong couplings in the $-6$ to $-9$ eV region that also involve Cs states suggest that Cs acts as a direct hole transfer booster.

The computed hole injection times, corresponding to the coupling between the LHP and spiro-MeOTAD states described above and extracted from $\Gamma(E)$, are reported in Table 1. All the obtained values are of the order of picoseconds (ps), in agreement with other experimental works, $^{19-22}$ with triLHP presenting the fastest injections, in particular for the FAMAX/spiro-MeOTAD (HOMO$-$1) (1.65 ps), CsFAMAX(O$-$Cs)/spiro-MeOTAD (HOMO$-$1) (2.50 ps) and PbX$_2$(Cs)/spiro-MeOTAD (HOMO$-$1) (2.68 ps) interfaces. These results show that (i) triLHP is always more efficient for CT than MAPI; (ii) MAPI is only efficient at the MAI termination (1.80 ps versus 4.93 ps at the PbI$_2$ one); and (iii) Cs acts as an additional CT booster not only when directly linked to spiro-MeOTAD, but also when it is present as subsurface species.

In conclusion, our DFT study addresses the interfaces of the spiro-MeOTAD HTM with the well-studied MAPI and with the much less explored triple cation LHP formulation, providing new insights on the chemical features leading to favorable binding and enhanced CT. In agreement with the recent literature, electronic interactions are crucial for interface stability, with FA and Cs atoms strengthening the binding to spiro-MeOTAD methoxy groups. Regarding CT, we find a thermodynamically favourable scenario for all interfaces, PbX$_2$ terminations presenting the highest driving force. Being close in energy and well above the LHP VBM, we include both the HOMO and HOMO$-$1 orbitals of spiro-MeOTAD in computing couplings and injection times. Cross-analysis of coupling matrix elements and pDOS shows the specific LHP states acting as CT channels, while analysis of MOs highlights the correlation between the best couplings and orbital localization towards the LHP surface. Our estimates of injection times predict that the CT occurs on the ps timescale, in agreement with experimental works. The donor state is the spiro-MeOTAD HOMO$-$1 orbital in most cases, which injects the electron to states in the deep LHP VB region or at higher energy for MAX and PbX$_2$ terminations, respectively. Interestingly, our results also highlight a new role for the Cs cation at the triLHP surface: besides its beneficial effects on the structural stability of LHP, Cs offers a convenient anchoring point to the HTM molecule and provides effective CT channels for hole transport. Overall, our analysis offers a novel atomic-scale perspective for a comprehensive rationalization of CT mechanisms and times for some among the most representative systems of current state-of-the-art PSCs, paving the route to further investigation on the effects of dopants, defects or buffer interlayers on key processes as interfacial CT.

This work was supported by the Italian MISE-ENEA Research Agreement on the Electric System, ENEA-CRESCO for computing facilities, and PON R&I 2014-2020-Asse IV “Istruzione e ricerca per il recupero-REACT-EU”.

## Conflicts of interest
There are no conflicts to declare.

## Notes and references

1 J. Y. Kim, J.-W. Lee, H. S. Jung, H. Shin and N.-G. Park, *Chem. Rev.*, 2020, **120**, 7867-7918.
2 H.-S. Kim, A. Hagfeldt and N.-G. Park, *Chem. Commun.*, 2019, **55**, 1192-1200.
3 M. Saliba, T. Matsui, J.-Y. Seo, K. Domanski, J.-P. Correa-Baena, M. K. Nazeeruddin, S. M. Zakeeruddin, W. Tress, A. Abate, A. Hagfeldt and M. Grätzel, *Energy Environ. Sci.*, 2016, **9**, 1989-1997.
4 C. Yi, J. Luo, S. Meloni, A. Boziki, N. Ashari-Astani, C. Grätzel, S. M. Zakeeruddin, U. Röthlisberger and M. Grätzel, *Energy Environ. Sci.*, 2016, **9**, 656-662.
5 Z. Hawash, L. K. Ono and Y. Qi, *Adv. Mater. Interfaces*, 2018, **5**, 1700623.
6 Y. Saygili, H.-S. Kim, B. Yang, J. Suo, A. B. Muñoz-Garcia, M. Pavone and A. Hagfeldt, *ACS Energy Lett.*, 2020, **5**, 1271-1277.
7 I. Kondov, M. Čížek, C. Benesch, H. Wang and M. Thoss, *J. Phys. Chem. C*, 2007, **111**, 11970-11981.
8 J. Haruyama, K. Sodeyama, I. Hamada, L. Han and Y. Tateyama, *J. Phys. Chem. Lett.*, 2017, **8**, 5840-5847.
9 P. Schulz, D. Cahen and A. Kahn, *Chem. Rev.*, 2019, **119**, 3349.
10 C. Ma, M. Grätzel and N.-G. Park, *ACS Energy Lett.*, 2022, **7**, 3120-3128.
11 C. Quarti, F. De Angelis and D. Beljonne, *Chem. Mater.*, 2017, **29**, 958-968.
12 A. Torres and L. G. C. Rego, *J. Phys. Chem. C*, 2014, **118**, 26947-26954.
13 C. Coppola, A. Pecoraro, A. B. Muñoz-García, R. Infantino, A. Dessì, G. Reginato, R. Basosi, A. Sinicropi and M. Pavone, *Phys. Chem. Chem. Phys.*, 2022, **24**, 14993-15002.
14 A. Leclaire, *J. Solid State Chem.*, 2008, **181**, 2338-2345.
15 Q. Wang, E. Mosconi, C. Wolff, J. Li, D. Neher, F. De Angelis, G. P. Suranna, R. Grisorio and A. Abate, *Adv. Energy Mater.*, 2019, **9**, 1900990.
16 A. Pecoraro, A. Di Maria, P. Delli Veneri, M. Pavone and A. B. Muñoz-García, *Phys. Chem. Chem. Phys.*, 2020, **22**, 28401-28413.
17 N. Droseros, B. Dänekamp, D. Tsokkou, P. P. Boix and N. Banerji, *APL Mater.*, 2019, **7**, 041115.
18 D. Shi, X. Qin, Y. Li, Y. He, C. Zhong, J. Pan, H. Dong, W. Xu, T. Li, W. Hu, J.-L. Brédas and O. M. Bakr, *Sci. Adv.*, 2016, **2**, e1501491.
19 P. Piatkowski, B. Cohen, F. J. Ramos, M. D. Nunzio, M. K. Nazeeruddin, M. Grätzel, S. Ahmad and A. Douhal, *Phys. Chem. Chem. Phys.*, 2015, **17**, 14674-14684.
20 C. S. Ponseca Jr., E. M. Hutter, P. Piatkowski, B. Cohen, T. Pascher, A. Douhal, A. Yartsev, V. Sundström and T. J. Savenije, *J. Am. Chem. Soc.*, 2015, **137**, 16043-16048.
21 J. Leng, J. Liu, J. Zhang and S. Jin, *J. Phys. Chem. Lett.*, 2016, **7**, 5056-5061.
22 K. Pydzińska-Białek, V. Drushliak, E. Coy, K. Załłski, J. Flach, J. Idigoras, L. Contreras-Bernal, A. Hagfeldt, J. A. Anta and M. Ziółek, *ACS Appl. Mater. Interfaces*, 2020, **12**, 30399-30410.

---

5058 | *Chem. Commun.*, 2023, **59**, 5055-5058
This journal is © The Royal Society of Chemistry 2023
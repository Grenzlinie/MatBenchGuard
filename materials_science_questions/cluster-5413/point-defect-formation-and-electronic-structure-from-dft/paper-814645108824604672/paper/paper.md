PHYSICAL REVIEW B 91, 155401 (2015)

# Surface energetics of alkaline-earth metal oxides:
Trends in stability and adsorption of small molecules

Michal Bajdich, Jens K. Nørskov, and Aleksandra Vojvodic

SUNCAT Center for Interface Science and Catalysis, SLAC National Accelerator Laboratory and Department of Chemical Engineering,
Stanford University, 443 via Ortega, Stanford, California 94305, USA

Received 21 December 2014; published 1 April 2015

We present a systematic theoretical investigation of the surface properties, stability, and reactivity of rocksalt type alkaline-earth metal oxides including MgO, CaO, SrO, and BaO. The accuracy of commonly used exchange-correlation density functionals (LDA, PBE, RPBE, PBEsol, BEEF-vdW, and hybrid HSE) and random-phase approximation (RPA) is evaluated and compared to existing experimental values. Calculated surface energies of the four most stable surface facets under vacuum conditions, the (100) surface, the metal and oxygen terminated octopolar (111), and the (110) surfaces, exhibit a monotonic increase in stability from MgO to BaO. On the MgO(100) surface, adsorption of CO, NO, and CH₄ is characterized by physisorption while H₂O chemisorbs, which is in agreement with experimental findings. We further use the on-top metal adsorption of CO and NO molecules to map out the surface energetics of each alkaline-earth metal oxide surface. The considered functionals all qualitatively predict similar adsorption energy trends. The ordering between the adsorption energies on different surface facets can be attributed to differences in the local geometrical surface structure and the electronic structure of the metal constituent of the alkaline-earth metal oxide. The striking observation that CO adsorption strength is weaker than NO adsorption on the (100) terraces as the period of the alkaline-earth metal in the oxide increases is analyzed in detail in terms of charge redistribution within the $\sigma$ and $\pi$ channels of adsorbates. Finally, we also present oxygen adsorption and oxygen vacancy formation energies in these oxide systems.

DOI: 10.1103/PhysRevB.91.155401
PACS number(s): 73.20.Hb, 71.15.Nc

## I. INTRODUCTION

Alkaline-earth metal oxides (AEMOs) of rocksalt structure are simple ionic solids as opposed to more complicated transition metal oxides and their well-ordered surfaces are of great interest to theoretical and experimental surface science [1–5]. Due to their high stability and irreducibility, application of AEMOs in catalysis is limited to high temperature processes such as oxidative coupling of methane [6], but their activity can be enhanced via metal doping [4], or they can be utilized as support materials for other catalysts [7]. Furthermore, this computational catalyst study is intended to fully explore and accurately map the surface properties such as stability, vacancy formation energetics, and adsorption of small molecules and benchmark theory to available experimental data [5].

Previous calculations of AEMO surfaces addressed the electronic structure, surface stability, relaxation, and rumpling effects of nonpolar (100), (110), and (211) facets [8–11]. It was found that for a given facet, the surface energy decreases along the series going from MgO to BaO—an observation attributed mostly to a loss of Madelung energy, which is largest for MgO [8–10,12]. In addition, more open surfaces with greater number of cleaved bonds were found to be significantly less stable than the (100) surface due to a direct loss of energy associated with cleaved bonds. The origin of the positive rumpling for MgO and increasing negative rumpling for CaO, SrO, and BaO was explained on the grounds of a well-known narrowing of the O(2p) valence band [10,11]. A stability study of the MgO(111) surface by Ciston *et al.* [13] revealed the presence of stable octopolar terminations when no water was present and stable hydroxylated surface terminations in the presence of water. The MgO(100) surface is without a doubt the most studied surface of the considered AEMO series. In particular, adsorption of small molecules CO, NO, CH₄, and H₂O has received much attention by both experiments [5,14–18] and theory [1,19–21]. Important to mention are also recent accurate coupled-cluster benchmark studies of adsorption of CO [22] and CH₄ [23]. Previous theoretical studies of adsorption of water on the (100) surfaces of the AEMO series revealed the preference towards dissociation of the water molecules for CaO to BaO [24]. Perhaps the least studied surface properties are related to oxygen adsorption and oxygen vacancy formation. To our knowledge only a handful of studies exist for oxygen vacancy formation on the MgO(100) surface [25–27].

In this paper, we present a systematic computational study of surface properties of four AEMOs, MgO, CaO, SrO, and BaO, by mapping their surface energies, CO, NO, and oxygen adsorption energies, and oxygen vacancy formation energies of the most stable surfaces of these oxides. While the surface energy is a determining factor for equilibrium morphology, CO and NO adsorption energies serve as probe molecules of surface reactivity [28]. Another important surface chemistry property of an oxide surface is its oxygen chemistry, i.e., a measure of the interaction between the surface and atomic oxygen on one hand and oxygen vacancies on the other hand, since these play a key role as active centers in most oxidative and dehydrogenation reactions processes [4]. From a practical point of view, it is highly desirable that a computational catalyst study achieves an accurate mapping of possible surface energetics. In order to benchmark our theoretical approaches, we evaluated the accuracy of four levels of density functional theory (DFT) theory: the local density approximation (LDA), the generalized-gradient approximation (GGA), van der Waals corrected GGA (GGA+vdW), screened hybrid-GGA as well as post-DFT random-phase approximation (RPA), and assessed our findings against existing experimental data.

1098-0121/2015/91(15)/155401(10)
155401-1
©2015 American Physical Society

The remainder of this paper is organized as follows. First we give a brief introduction of our computational methodology, followed by a presentation of the results for bulk properties and surface stabilities of the four considered AEMOs. Next, we discuss the performance of common DFT functionals and the RPA method for adsorption of CO, NO, CH₄, and H₂O molecules on the MgO(100) surface. Then a mapping of the CO and NO adsorption energies on the different surfaces of the AEMOs is discussed. Additionally, we also provide a detailed analysis of the bond character for representative systems, including a comparison between CO@MgO(100) and CO@BaO(100), and between NO@MgO(100) and NO@BaO(100). In the last part of the Results section, we discuss the oxygen chemistry of the investigated surfaces. Finally, we conclude with a summary of our most relevant findings and their implications.

## II. METHODS
We employed the periodic plane-wave basis set implementation of DFT within the PWscf program of QUANTUM ESPRESSO [29]. We performed calculations with several DFT functionals frequently used in solid-state and surface science studies: LDA [30], GGA: PBE [31], RPBE [32], and PBEsol [33], GGA with van der Waals (vdW) density functional: BEEF-vdW,[34] and screened GGA-hybrid: HSE [35,36]. The BEEF-vdW approach combines semilocal Bayesian error estimation functional with an additional vdW nonlocal correlation term. The vdW term is computed via DFT/vdW-WF2 method [37–39], which been shown to lead to improved description of surface processes [40–42]. For elements from H to Mg we used the PBE generated norm-conserving pseudopotentials of Trouiller and Martins [43,44], while for Ca, Sr, and Ba we used the pseudopotentials of Goedecker, Hartwigse, Hutter, and Teter [45], which explicitly include semicore states. The use of norm-conserving pseudopotentials was dictated by the implemenation of GGA-hybrid part of PWscf. A kinetic-energy cutoff of 80 Ry and four times that value for the charge density cutoff was used in the calculations except for the RPA calculations as described below.

The random-phase approximation [46–48] calculations were performed using the PAW method [49] within the plane-wave VASP code [50–52]. The RPA energy at PBE optimized geometries were evaluated either (i) in conventional RPA@PBE scheme, where the exchange and correlation are calculated non-self-consistently from PBE orbitals as $E_{RPA@PBE}=E_{@PBE}^{ex}+E_{@PBE}^{corr}$, or (ii) in hybrid RPAₕ@PBE scheme [53], where the effect of self-consistent exchange energy is added as $E_{RPA_h@PBE}=E_{@HF}^{ex}+E_{@PBE}^{corr}$. The convergence of energy differences within few meV was achieved with plane-wave cutoff of 350 eV for GW variants of VASP PAW potentials. Additional computational details are provided in connection to the rest of the results.

## III. RESULTS
### A. Bulk properties
The calculated bulk properties, lattice constants $a$, bulk moduli $M$, and atomization energies $\Delta E^{AE}$, of the AEMO series are presented in Fig. 1. For each of the observables, our calculated values follow the experimentally observed trend [54–56] and are also in agreement with previous theoretical findings [10,11]. We find an increase in the lattice constant and a decrease of the bulk modulus going from MgO to BaO within the AEMO series, which is consistent with the increase of the ionic radii of the metal ions and shows a transition from ionic to more covalent bonding [12]. The atomization energy exhibits a maximum for CaO but the variations between the different AEMOs is fairly constant within a 1 eV range for a given DFT functional.

![](./images/814645108824604672_1.jpg)

FIG. 1. (Color online) Calculated lattice constants $a$, bulk moduli $M$, and atomization energies $\Delta E^{AE}$ for six different DFT functionals together with experimental values adapted from Refs. [54–56]. Note that, in our simplified comparison to experimental data, we have neglected anharmonic ZPE corrections, which can be as large as $\Delta a=-0.02$ Å for bulk MgO [57].

There are also characteristic trends in the above calculated quantities for a given DFT functional and between different functionals. The well-known overestimation of the stability within LDA is clearly visible for AEMOs. The lattice constants are too short and bulk moduli and atomization energies are too large. On the other hand, the RPBE predictions are on the opposite side of the spectrum, with too long lattice constants and underestimation of atomization energies and bulk moduli. All other functionals included in this study lie within the LDA-RPBE bounds. A comparison of our PBE, PBEsol,

and HSE data with experimental data for bulk MgO show the following lattice constant dependence $a_{\text{PBE}} > a_{\text{PBESol}} \gtrsim a_{\text{HSE}} \gtrsim a_{\text{expt}}$ (and similarly for bulk moduli $M$) while the atomization energy follows $\Delta E_{\text{PBE}}^{\text{AE}} \approx \Delta E_{\text{HSE}}^{\text{AE}} < \Delta E_{\text{expt}}^{\text{AE}} < \Delta E_{\text{PBESol}}^{\text{AE}}$. These findings are in qualitative agreement with the ones of Shimka *et al.* [57]. We find that the bulk properties obtained with the BEEF-vdW functional are not significantly improved over values obtained by the PBE functional. When it comes to the band gaps, the calculated values within the HSE functional (MgO: 6.7 eV, CaO: 5.3 eV; SrO eV: 4.7 eV; BaO: 3.2 eV) are, as expected, the closest to experimental estimates (7.8 eV, 7.1 eV, 5.9 eV, and 4.3 eV from Ref. [58]). For all functionals, the calculated density of states (DOS) of the bulk AEMOs (not shown) exhibit a narrowing of the valence $\text{O}(2p)$ band and a shift of the metal $\text{M}(p)$ semicore states towards higher energies within the series from MgO to BaO in agreement with previous studies [10,11].

### B. Energetics of stoichiometric surfaces
The most stable surface termination of rocksalt type compounds is the nonpolar (100) surface, which has been argued to be due to its close packed bulklike structure [59]. In terms of stability, the (110) surface followed by the (211) surface are other low-index stoichiometric nonpolar surface terminations characterized by increasing number of uncoordinated bonds at the surface [9]. The polar (111) surface is known to reconstruct to form two different octopolar terminations [60,61] (metal and oxygen terminated: M-oct and O-oct) with a $2 \times 2$ periodicity. Additionally, in the presence of water, the (111) facet can be greatly stabilized by hydroxilation of the surface [13].

For this study, we have selected four low-index stoichiometric surface terminations under vacuum conditions, namely the (100), (110), and the M-oct and O-oct (111) surfaces. Their calculated surface energies normalized to $1 \times 1$ unit surface area are summarized in Fig. 2. The surface energy is obtained via the linearized method of Fiorentini and Methfessel [62]. Slabs from 2 to 8 metal-oxide layers have been studied with a surface energy convergence within 0.01 eV, which was achieved for 4–6 layers. The periodic symmetric surface slabs were separated by $16\ \mathring{\text{A}}$ of vacuum, cleaved at bulk geometries and fully relaxed within fixed unit cells bellow maximum threshold force of $0.05\ \text{eV}/\mathring{\text{A}}$. To be noted is that the HSE investigation of the (111) surfaces was omitted due to prohibitively large computational cost within plane-wave PWscf for the larger slabs.

For all surfaces, we find that the calculated surface energy decreases monotonically along the series from MgO to BaO, as has been attributed previously to a loss of Madelung energy, which is largest for MgO [8–10,12]. Furthermore, the energy differences between the facets also decrease along the series. This observation has strong implications for the surface morphology of AEMOs, with BaO having much larger probability of having different facets exposed than MgO, as first pointed out by Broqvist *et al.* [10] We also find, that the surface energies of the two octopolar (111) terminations fall in-between the (100) and (110) surfaces. For MgO, the O-oct (111) surface has a lower surface energy relative to the M-Oct (111) surface, as observed by Ciston *et al.* [13]. Interestingly, the stability between the O-oct and M-Oct (111) surfaces is reversed for the rest of the AEMO series (see lower panels of Fig. 2). For a given metal oxide, the ordering of stabilities between the individual surfaces approximately corresponds to coordination loss per surface metal site, which is 1/6 for (100), 1.5/6 on average for (111) M-Oct (same for O-site in O-oct termination), and 2/6 for (110).

![](./images/814645108824604672_2.jpg)

FIG. 2. (Color online) Calculated surface energies of stoichiometric low-index terminated alkaline-earth metal-oxide surfaces in eV normalized to $1 \times 1$ surface area. The results for the (100), (110), and two octopolar (111) terminated (M-Oct, O-oct) surfaces obtained using six different DFT functionals are shown. The corresponding primitive cell of the surfaces used in the calculations are also shown as insets, where larger spheres represent the metal atoms. For clarity, only the top layer was rendered in color.

Qualitatively, each of the investigated DFT functionals predicts similar trends for surface stability of the AEMO series. We find that the surface energies lie within the bounds of LDA (too high) and the RPBE (too low), as we found for bulk properties. For MgO(100), the calculated surface energies are shown in Table I, with PBESol, BEEF-vdW, and RPA methods having the best agreement with the experimental finding. As experimental reference, we have chosen the value of 0.575 eV [63], which is based on thermodynamic measurements of polycrystalline samples as opposed to experiments based on cleavage energy of single crystals [64], which are likely to overestimate this quantity [65]. The good performance of PBESol functional is expected, given its design to match the jellium surface energies [66,67]. Contrary to bulk properties, the improved performance of the BEEF-vdW functional over the PBE functional for surface energies is somewhat surprising and suggests the importance of long-range interactions for surface properties.

<table>
<caption>TABLE I. MgO(100) surface energies $\sigma$ in eV per $1 \times 1$ area compared to experiment.</caption>
<thead>
<tr>
<th>Method</th>
<th>Expt. [63]</th>
<th>LDA</th>
<th>PBE</th>
<th>RPBE</th>
<th>PBESol</th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>$\sigma [\text{eV}/1 \times 1]$</td>
<td>0.575</td>
<td>0.634</td>
<td>0.503</td>
<td>0.429</td>
<td>0.568</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>BEEF-vdW</td>
<td>HSE</td>
<td>RPA@PBE</td>
<td>$\text{RPA}_h@\text{PBE}$</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>$\sigma [\text{eV}/1 \times 1]$</td>
<td></td>
<td>0.573</td>
<td>0.550</td>
<td>0.577</td>
<td>0.582</td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

![](./images/814645108824604672_3.jpg)

FIG. 3. (Color online) Upper panel: adsorption energies of CO, NO, CH₄, and H₂O molecules on the MgO(100) surface. The 2 × 2 unit cells are shown as insets with geometries discussed in the text. Except for the case of CH₄ with one monolayer coverage, all other adsorbates are in the limit of low coverage (up to coverage of $\Theta = 1/8$) as discussed in text. The experimental and calculated values are summarized in Table II. Lower panel: associated atomization errors of each molecular species for the different methods relative to the ZPE corrected experimental atomization energies as adapted from NIST CCCBD [68].

## C. Adsorption on the MgO(100) surface
The MgO(100) surface is the most studied surface of the AEMO series and its interaction with different adsor- bates has been experimentally well characterized (see, e.g., review of Campbell and Sellers [5]). For direct comparison with experiments [14–17] and known theoretical benchmarks [1,19,21–24], we have chosen to study adsorption of CO, NO, and H₂O at low adsorbate coverage as well as CH₄ at what is often referred to as one monolayer coverage (50% occupancy of metal sites).

Figure 3 summarizes the calculated adsorption energies, which have been obtained from slab models consisting of four MgO layers, where the bottom 2 layers are fixed to bulk positions and the remaining top 2 layers are fully relaxed. The slabs were separated with a 16 Å of vacuum. The adsorption energies have been extrapolated from $\sqrt{2} \times \sqrt{2}$ to $\sqrt{8} \times \sqrt{8}$ cells, with values converged within 0.01 eV at intermediate $2 \times 2$ cells. Due to higher computational cost, the reported values for HSE and RPA calculations are only for intermediate cell sizes.

The geometries of physisorbed CO and NO molecules on the MgO(100) surface at low coverage are relatively well known from previous theoretical studies [1,19,21,22]. At this coverage, the CO molecule adsorbs on top of the Mg metal site with a C-Mg bond length of approximately 2.4 Å and a small tilting angle of $5^{\circ}$. In contrast to CO, the extra unpaired electron of the NO leads to a strongly tilted adsorption geometry of the NO molecule $(50 \pm 10^{\circ})$ with approximately the same N-Mg bond length of 2.4 Å as for the C-Mg bond of an adsorbed CO molecule. Experimentally measured adsorption energies of both CO and NO find a weak binding to the surface (see Fig. 3), likely with a long range dispersive character of the bond mediated by dipole interactions. Importantly, NO adsorbs marginally stronger than CO by approximately $1 \pm 0.5$ kcal mol⁻¹. We also note, that both experimental estimates have been extrapolated to zero coverage and include zero point vibrational energy of $-4$ kJ mol⁻¹ as adapted from Ref. [22].

In Fig. 3 we compare the adsorption energies predicted from six DFT functionals to experimental results for CO [14,15] and NO [14], as well as to available accurate quantum chemical CCSD(T) adsorption benchmarks [22]. We find that all calculated and experimental adsorption energies lie within the bounds of LDA (too strong adsorbate-surface interaction) and RPBE (too weak adsorbate-surface interaction), as was observed for the bulk and surface properties. However, LDA and PBEsol and to a lesser degree also the PBE functional predict that CO adsorbs stronger than NO (see Fig. 3). One possible origin of this discrepancy could lie in the larger overbinding error found for the gas-phase NO as compared to CO molecule that have been found for these functionals (see atomization errors of lower panel of Fig. 3). The experimentally observed adsorption trend is accurately captured within RPBE, HSE, and BEEF-vdW. We find that the BEEF-vdW extrapolated adsorption energies for CO and NO are in best agreement with experimental values, while HSE predicts slightly too weak adsorption suggesting the

TABLE II. Adsorption energies on the MgO(100) surface in eV.

| Method       | CO                  | NO                | CH₄               | H₂O                |
|--------------|---------------------|-------------------|-------------------|--------------------|
| Expt.        | $-0.18(2)$[14]<br>$-0.23(2)$[15] | $-0.26(2)$[14] | $-0.16(1)$[16]<br>$-0.17(1)$[17] | $-0.52(10)$[18] |
| CCSD(T)      | $-0.218$[22]        |                   | $-0.138$[23]      |                    |
| LDA          | $-0.393$            | $-0.299$          | $-0.259$          | $-0.847$           |
| PBE          | $-0.158$            | $-0.157$          | $-0.033$          | $-0.455$           |
| RPBE         | $-0.046$            | $-0.076$          | $-0.016$          | $-0.276$           |
| PBEsol       | $-0.237$            | $-0.180$          | $-0.072$          | $-0.592$           |
| BEEF-vdW     | $-0.215$            | $-0.266$          | $-0.184$          | $-0.438$           |
| HSE          | $-0.127$            | $-0.072$          | $-0.030$          | $-0.450$           |
| RPA@PBE      | $-0.072$            | $0.029$           | $-0.087$          | $-0.492$           |
| RPAₕ@PBE     | $-0.310$            | $-0.360$          | $-0.140$          | $-0.608$           |

importance of the long-range interactions for these systems.
Despite that RPBE predicts the correct order between CO and
NO adsorption energies, the adsorbate-surface bond strength
is too weak—which cannot be improved by inclusion of vdW
interactions (not shown).

When it comes to adsorption of $CH_4$, the most favorable
coverage is one monolayer, i.e., one methane molecule on
top of every other metal atom in what is known as the
“dipod” configuration (two hydrogen bonds pointing upwards
and two hydrogen bonds pointing downwards towards the
nearest surface oxygen atoms) [16,17]. Two dipods rotated
$90^\circ$ relative to each other form the most stable $2 \times 2$ periodic
superstructure [23], which was also employed in this study.
The interaction between the $CH_4$ molecule and the MgO(100)
surface has a predominantly vdW nature with small or no
contribution from dipole interactions [23], and this is the least
bound adsorbate of all studied systems. We find that from all
DFT functionals, only the BEEF-vdW predicted adsorption
energy lies in the vicinity of the experiment and CCSD(T)
benchmark. The obtained BEEF-vdW average equilibrium
bond distance between the $CH_4$ molecules and the surface
is $3.32\ \mathring{A}$, which agrees with the experimental value of $3.30\ \mathring{A}$
[69].

Adsorption of $H_2O$ on MgO(100) (Fig. 3) is an example
of a weakly chemisorbed system with significant hydrogen
to surface bonding [18]. The lowest energy structure is best
described as water lying flat on the surface with one hydrogen
pointing towards the surface oxygen [24]. The PBE, PBEsol,
BEEF-vdW, and HSE calculated adsorption energies of water
on the MgO(100) surface all lie within the relatively broad
experimental estimate.

Finally, we would like to comment on the performance of
the RPA method. In Fig. 3 we compare the performance of the
conventional RPA scheme as well as the hybrid RPA scheme.
Clearly, the hybrid RPA outperforms the conventional RPA
scheme for CO, NO, and $CH_4$ adsorption and predicts exper-
imental ordering of energies, albeit at slightly overestimated
values for CO and NO when compared to experiments. On
the other hand, the RPA@PBE scheme predicts too weak
adsorption bonds and has difficulty with describing the NO
adsorption, which is the only spin-polarized system of the
ones investigated here. For $H_2O$ adsorption, both methods
deliver comparable results. Lastly, $RPA_h@PBE$ also reduces
the well-known atomization errors of conventional RPA (lower
panel of Fig. 3).

### D. CO and NO adsorption in the AEMO series

In this section, we focus on the adsorption energy trends
of CO and NO on the most stable surface terminations of the
different AEMOs. The adsorption energies of CO and NO
molecules in the on-top surface metal site as a function of the
surface energy, which was shown to be a monotonic function of
the AEMO series (see Fig. 2), are presented in Fig. 4. As for the
MgO(100) surface, we employed 4 layer slab models with the
bottom 2 atomic layers fixed in bulk positions and remaining
top 2 layers fully relaxed for all surfaces. All the energetics
is calculated using $2 \times 2$ simulation cells, corresponding to
a coverage of $\Theta=0.25$ for the (100), (110), and with only
single on-top site for (111)-M-oct surface. The on-top metal
site of the (111)-O-oct surface is occupied by oxygen and does
not allow for additional adsorption; therefore, it is omitted in
the rest of our analysis.

![](./images/814645108824604672_4.jpg)

FIG. 4. (Color online) Adsorption energies of CO (top panel) and
NO (bottom panel) in the on-top surface metal site on the (100), (111)-
M-oct, and (110) surfaces of the AEMO series plotted as function of
surface energy. For clarity, only the BEEF-vdW results are shown for
NO on (111)-M-oct.

The most general trend (see Fig. 4) is that, for a given sur-
face termination, both the $E_{\text{ads}}^{\text{CO}}$ and the $E_{\text{ads}}^{\text{NO}}$ get progressively
weaker as we move from MgO to BaO within the AEMO
series. The only exception is the case of NO adsorbed on the
(100) terraces, where we observe a strengthening of the NO
to surface bond. In addition, we find that for both CO and
NO on a given metal oxide, a less stable surface on average
adsorbs a molecule stronger than a more stable surface. This
behavior is expected, as less stable surfaces are also more open,
i.e., are characterized by a larger number of uncoordinated
bonds [9,59], which in turn can interact with the adsorbate.
When it comes to the surfaces studied here, we observe that
the (100) surface has fivefold coordinated metal sites, the
(110) surface has fourfold coordinated metal sites, and the
(111)-M-Oct surface has single threefold and triple fivefold
coordinated metal sites. As we have discussed in Sec. III B, the
above average number of uncoordinated bonds is a relatively
good predictor of the surface energy. However, for the case
of CO and NO adsorption (see Fig. 4), we find that there
is no significant difference between the adsorption energies
on the (110) and (111)-M-Oct surface, while there is a clear
difference between the (100) surface and the other two surface
terminations. Hence we conclude that bond counting or the use

![](./images/814645108824604672_5.jpg)

FIG. 5. (Color online) Charge density difference plots for CO@MgO(100) (left) and CO@BaO(100) (right) projected along the (110) direction obtained with the BEEF-vdW functional. The positive (negative) values of this quantity indicate regions with gain (loss) of electronic charge. The numeric labels indicate the change in the Bader charge upon adsorption relative to the free gas-phase molecule. Small red and black spheres indicate positions of oxygen and carbon atoms, respectively.

of surface energy to predict the adsorption energetics is limited and provides only a rough estimate of the reactivity of different surfaces. In other words, they can not be used as descriptors since they are unable to give any quantitative comparison nor provide an ordering between the different oxide surfaces.

We also find that NO always binds stronger to the surface than CO. This is the same dependence as for the experimental results on the MgO(100) surface as we discussed in the previous section. We also note that the same ordering of CO vs NO adsorption energies is found on the NiO(100) surface [70]. In the next section, we analyze in greater detail the origin of this effect.

### E. Electronic structure analysis of CO and NO bond formation

Here we discuss the above mentioned observation that CO adsorbes marginally $(\sim 0.05$ eV) weaker on BaO(100) than on MgO(100), while NO adsorbs substantially stronger ($\sim 0.1$ eV) on BaO(100) than on MgO(100). The analysis is based on representative results obtained with the BEEF-vdW functional. We have chosen the BEEF-vdW functional due to its predictability of the CO and NO adsorption on the MgO(100) surface. In order to understand the reasons behind differences in chemical bonding, it is instructive to plot the charge density difference (CDD) upon adsorption. This quantity is obtained as $\rho_{\mathrm{CDD}}=\rho_{\{\mathrm{Ads+surf}\}}-\rho_{\mathrm{Ads}}-\rho_{\text{surf}}$, where $\rho_{\mathrm{Ads}}$, $\rho_{\text{surf}}$, and $\rho_{\{\mathrm{Ads+surf}\}}$ are self-consistent densities of the adsorbate, surface, and of the combined system, respectively. We note that $\rho_{\mathrm{Ads}}$ and $\rho_{\text{surf}}$ have been calculated based on the fixed geometry of the combined system to allow for identification of true electronic effects and avoid geometric effects.

Figures 5 and 6 show the CDDs for CO and NO on the (100) surface of MgO and BaO. For the adsorbed CO molecule, $\rho_{\mathrm{CDD}}$ depicts polarization in the $\sigma$ channel, which is about twice as large for MgO than for BaO. This is also quantitatively supported from the calculated Bader charges as indicated in Figs. 5 and 6. For the adsorbed NO molecule, on the other hand, the overall change in the density due to adsorption is much larger than the one for CO. Both CDD plots for adsorbed NO are dominated by polarization in the $\pi$ channel. In contrast to the CO cases, the polarization is stronger for BaO than for MgO. Hence we conclude that the change in polarization is a good measure of the adsorption strength for the AEMOs.

We find that the intramolecular CO bond length essentially remains unchanged upon adsorption on both MgO and BaO relative to its gas phase value of $R_{\mathrm{CO}}=1.121$ Å for BEEF-vdW, while it is marginally shorter for geometries obtained with the HSE functional. This also indicates a small repulsive interaction in the $\sigma$ channel, which often has been observed upon CO adsorption on pure metals [71]. On the other hand, the elongation of the internal NO bond is clearly visible for BaO: $R_{\mathrm{NO}}=1.166$ Å (MgO: $R_{\mathrm{NO}}=1.146$ Å) when compared to the bond of gas phase NO molecule $R_{\mathrm{NO}}=1.145$ Å (BEEF-vdW functional). This observation is consistent with the picture of $\pi$-back donation to the NO molecule, which is similar to the case of NO@Ru(001) and NO@NiO(100) [72,73].

The projected density of states (PDOS) for CO and NO on the (100) surface of MgO and BaO are shown in Fig. 7. For the adsorbed CO, the $4 \tilde{\sigma}$, $5 \tilde{\sigma}$, and $1 \tilde{\pi}$ adsorbate states are very similar to the ones of the gas-phase CO molecule. Only a small hybridization with the states of the surface $\mathrm{Ba}(5 p)$ atoms is observed. The change in intensity of the carbon $5 \tilde{\sigma}$ state for CO@MgO(100) is also detected, although its value is likely underestimated due to the small radii employed in the atomic orbital projectors. Overall, the shifts in the position of the peaks are larger for CO@MgO(100) than for CO@BaO(100), in agreement with the larger polarization found in the charge density differences (see Fig. 5).

For adsorbed NO, the $4 \tilde{\sigma}$, $5 \tilde{\sigma}$, and $1 \tilde{\pi}$ adsorbate states are significantly more hybridized than for adsorbed CO. We find that the larger tilting angle $(47^{\circ})$ of the NO towards the MgO(100) surface leads to a lift of the degeneracy between the $\pi_{x}$ and $\pi_{y}$ states. A small hybridization of the $2 \tilde{\pi}$ state with the surfaces and a reordering of the $1 \tilde{\pi}$ state relative to the $5 \tilde{\sigma}$ state in the minority spin channel is also observed. For NO@BaO(100), the significantly smaller tilting angle

![](./images/814645108824604672_6.jpg)

FIG. 6. (Color online) Charge density difference contour plots for NO@MgO(100) (left) and NO@BaO(100) (right) projected along the ⟨100⟩ direction calculated at the BEEF-vdW level. Small blue sphere indicate positions of the nitrogen atom while the rest of the labels are identical to Fig. 5. Insets: full three-dimensional shapes of charge density difference contours at values of ±0.001.

$(17^\circ)$ of the NO molecule is not sufficient to lift the $\pi_{x,y}$ degeneracy. However, the $4\tilde{\sigma}$ and $2\tilde{\pi}$ states are significantly more hybridized with the states of the $Ba(5p)$ and $O(2p)$ surface atoms. The relative ordering of the $1\tilde{\pi}$ to $5\tilde{\sigma}$ is reversed within both spin channels. Again, we find overall larger hybridization and shifts in the states for NO@BaO(100) than for NO@MgO(100), which is consistent with the picture of a larger polarization observed in the density difference (see Fig. 5). In other words, the differences in adsorption of CO and NO on the MgO(100) and BaO(100) surfaces can be rationalized from the electronic structure.

### F. Adsorption of atomic oxygen and oxygen vacancy formation

Another very important property of an oxide surface is its reactivity towards oxygen. We have investigated oxygen adsorption energy dependence on different surface sites of the AEMO surfaces as well as the formation of oxygen vacancies. For the (100) and (110) surfaces, in addition to direct on-top adsorption, we have identified two more stable configurations: the metal-metal bridge sites as well as in metal-oxygen-metal (MOM) sites, in which an $O_2$-like structure is formed (shown as inset of Fig. 8). The energetic map of adsorption for studied surfaces of the AEMO series is

![](./images/814645108824604672_7.jpg)

FIG. 7. (Color online) Projected density of states of CO (left panel) and NO (right panel) adsorbed on the MgO(100) and BaO(100) surfaces compared to their gas-phase spectra as calculated within the BEEF-vdW functional. All spectra are aligned relative to the Fermi level $E_F$, except for the gas-phase spectrum of CO, which was aligned to match the position of the $5\sigma$ peak to an experimental spectrum (adapted from Fig. 43 of Ref. [71]). For NO, the spin-minority channel is indicated as negative values. The atomic projections to $\sigma$ and $\pi$ contributions of molecules have been enhanced by a factor of 2 for CO and 4 for NO for clarity.

![](./images/814645108824604672_8.jpg)

FIG. 8. (Color online) Upper panel: adsorption energy of atomic oxygen $E_{\text{ads}}^{\text{O}}$, for adsorbate coverage $\Theta=0.25$, on the surfaces of the AEMO series shown as function of surface energy. As in Fig. 4, the reported results are for six DFT functionals and two RPA methods. For on-top and bridge sites, only the PBE results are shown. The inset depicts the geometry of the MOM site. Lower panel: same as above but for oxygen vacancy formation energy $E_{\text{f}}^{\text{O}}$.

shown in the upper panel of Fig. 8. In the lower panel of Fig. 8, we report the calculated oxygen vacancy formation energies, more specifically the formation energies for the neutral surface F centers. It is customary to define the oxygen adsorption energy $E_{\text{ads}}^{\text{O}}=E_{\{ \text{surf+Oads} \} }-E_{\text{surf}}-\mu_{\text{O}}$ and oxygen vacancy formation energy $E_{\text{f}}^{\text{O}}=E_{\text{surf}}-E_{\{ \text{surf-O} \} }-\mu_{\text{O}}$ relative to gas phase $\text{O}_{2}$ as $\mu_{\text{O}}=E_{\text{DFT}}(\text{O}_{2})/2$. Note that a straightforward conversion to atomic oxygen as reference can be obtained by subtracting half of its experimental atomization energy (5.21 eV). An alternative definition is possible by using water and hydrogen as Ref. [74] as follows: $\mu_{\text{O}}=E_{\text{DFT}}(\text{H}_{2}\text{O})-E_{\text{DFT}}(\text{H}_{2})+2.506$ eV, which leads to only a small constant shift ($\sim$0.1 eV) in observed values. As in the CO and NO calculations, we employed identical 4 layer slab models and $2\times2$ simulation cells. For the (111) surfaces, the oxygen adsorption energy is calculated at the on-top metal site for the M-oct termination, while the oxygen vacancy formation is calculated by oxygen removal from the O-oct terminated surface.

We find that the adsorption at the on-top metal site on any surface is very weak, with adsorbed oxygen maintaining its triplet spin state (see Fig. 8). A stronger adsorption is found for the oxygen on the bridge sites of the (100) and (110) surfaces by about 0.6 eV and for these systems some residual spin polarization remains on the adsorbed oxygen. The most stable adsorption site on the (100) and (110) surfaces is the MOM site, which is about 1 eV more stable than the on-top site. Adsorbed oxygen at the MOM site forms a stretched $\text{O}_{2}$-like structure, which is further stabilized by the surrounding metal atoms (shown as inset of Fig. 8). In this case, the magnetic moment of the oxygen is fully quenched by the surface. The calculated oxygen vacancy formation energies are shown in the lower panel of Fig. 8. For all the studied oxide surfaces, we find that the final electronic configuration of the oxygen vacancy is the same as for the singlet-type neutral F-center.

The geometric structure of the local adsorption environment plays a crucial role in the interaction between oxygen and surface. The two surfaces with higher surface energies have also a higher number of uncoordinated bonds when compared to the (100) surface and the oxygen generally adsorbs stronger on them, as we discussed above. We find a similar inverse effect for the oxygen vacancy formation energy; that is, the formation energy decreases for less stable surfaces relative to the (100) surface. However, it is clear that the surface energy is only a weak indicator of the oxygen reactivity in these systems.

The electronic structure differences between the oxides of the AEMO series are also clearly visible. For a given adsorption site, the adsorption is strengthened along the AEMO series, similar to what we found for NO adsorption on the (100) surface. For the MOM site, this gain is as large as 1.5 eV, i.e., the adsorption energy difference between O@MgO(100) and O@BaO(100). A comparison between the density of states of O adsorbed on MgO(100) and BaO(100) (not shown) indicates a much larger hybridization between O($2p$) and BaO states. For vacancy formation, we observe destabilization of the vacancy as the covalency of the oxide increases. This is reasonable, since the extra electron pair in the vacancy gives rise to strong Madelung stabilization [26], which is largest for MgO and decreases along the series [12].

The adsorption calculations of O on the MOM sites for the different DFT functionals reveal the familiar ordering and energy range and bounds as observed for the NO and CO adsorption, that is, RPBE yielding a too weak and LDA a too strong binding. The variation in the adsorption energies is as large as 0.8 eV. Within these bounds, $E_{\text{ads}}^{\text{O}}$ is ordered as $E_{\text{HSE}}<E_{\text{PBE}}<E_{\text{PBEsol}}\approx E_{\text{BEEF-vdW}}$. The $E_{\text{f}}^{\text{O}}$ has a similar ordering as $E_{\text{ads}}^{\text{O}}$. While we were unable to find any experimental or calculated oxygen adsorption energies, our vacancy formation energy of 6.28 eV for MgO(100) within HSE functional agrees very well with the recently published HSE value of 6.34 eV [27]. Interestingly, the RPA results predict too strong oxygen binding oxygen adsorption and too large vacancy formation energies, which are very close to LDA results. This finding is independent of oxygen reference or hardness of oxygen pseudopotential indicating the inability of RPA to capture missing correlation under change of electron pairs (from triplet to singlet) [75,76].

Finally, we discuss the relations and correlations of the oxygen chemistry between different AEMOs that we have identified. In Fig. 9 we show that an approximate linear relation exists between the vacancy formation energies of the different AEMOs surfaces and the vacancy formation energies of the (100) surfaces. This is of utter importance, since the vacancy

![](./images/814645108824604672_9.jpg)

FIG. 9. (Color online) Linear dependence of $E_{\mathrm{f}}^{\mathrm{O}}$ in (110) and O- oct (111) surfaces relative to $E_{\mathrm{f}}^{\mathrm{O}}$ of (100) surfaces. Inset: similar linear dependence between on-top $E_{\mathrm{ads}}^{\mathrm{O}}$ and $E_{\mathrm{f}}^{\mathrm{O}}$ using only the PBE data of Fig. 8.

formation energy of a less stable surface can be predicted based on the vacancy formation of the most stable surface. Additionally, we also find a linear relation between on-top oxygen adsorption energies and surface formation energies, shown as inset of Fig. 9. Hence a good estimate of the oxygen adsorption energetics can be established with the knowledge of only the oxygen vacancy formation of the (100) surfaces.

## IV. CONCLUSIONS
In conclusion, we have performed a thorough compu- tational study of the surface chemistry of alkaline-earth transition-metal oxides (MgO, CaO, SrO, and BaO) using different DFT functionals (LDA, PBE, RPBE, PBEsol, BEEF- vdW) and RPA methods, and benchmarked our results with existing experimental values. The most important factors determining the surface properties of AEMOs have either an electronic or structural origin. We find that the electronic effects are responsible for ordering of adsorption energies within the AEMO series and structural effects are responsible for ordering between different facets for a given AEMO.

For surface energies, the RPA methods and the PBEsol functional provide the most accurate predictions compared to experiments. The best performing DFT functionals for the surface adsorption energetics on MgO(100) are found to be the BEEF-vdW functional and hybrid RPA method mostly due to direct incorporation of long-range interactions. A complete mapping of adsorption energetics on the AEMO surfaces using the CO and NO as probing molecules reveals a stronger adsorption of NO relative to CO, which is attributed to much larger polarization in the $\pi$ channel of the bond between the NO and the surface.

Finally, we establish an internal hierarchy in the oxygen chemistry of different AEMO surfaces, which include the (100), the (110), and the oxygen and metal terminated (111) surfaces. The oxygen vacancy formation energetics of all surfaces are found to be linearly correlated to the energies of the most stable (100) surfaces. In addition, we find that there is a linear relation between oxygen adsorption energies and the oxygen vacancy formation energies of the (100) surfaces. This leaves us with a scheme, at least to a first order, to approximate the reactivity of different AEMO surfaces based only on the calculated oxygen vacancy formation energies of the (100) surfaces.

## ACKNOWLEDGMENTS
The authors would like to thank Lars G. M. Pettersson and Anders Nilsson for useful discussions and comments. M.B. would also like to acknowledge Matúš Dubecký and Philipp Plessow for their help with RPA calculations. We also acknowledge the support from the project titled "Predictive Theory of Transition Metal Oxide Catalysis: DOE Materials Genome Project (No. DE-AC02-76SF00515)". This research partially employed NERSC computational resources under DOE Contract No. DE-AC02-05CH11231.

[1] M. A. Nygren and L. G. M. Pettersson, J. Chem. Phys. 105, 9339 (1996).
[2] H.-J. Freund and G. Pacchioni, Chem. Soc. Rev. 37, 2224 (2008).
[3] H.-J. Freund and D. W. Goodman, in Handbook of Hetero- geneous Catalysis (Wiley-VCH Verlag GmbH & Co. KGaA, Weinheim, Germany, 2008).
[4] E. W. McFarland and H. Metiu, Chem. Rev. 113, 4391 (2013).
[5] C. T. Campbell and J. R. V. Sellers, Chem. Rev. 113, 4106 (2013).
[6] J. H. Lunsford, Angew. Chem. 107, 1059 (1995).
[7] P. Frondelius, A. Hellman, K. Honkala, H. Häkkinen, and H. Grönbeck, Phys. Rev. B 78, 085426 (2008).
[8] J. Goniakowski and C. Noguera, Surf. Sci. 319, 68 (1994).
[9] J. Goniakowski and C. Noguera, Surf. Sci. 323, 129 (1995).
[10] P. Broqvist, H. Grönbeck, and I. Panas, Surf. Sci. 554, 262 (2004).
[11] N. V. Skorodumova, K. Hermansson, and B. Johansson, Phys. Rev. B 72, 125414 (2005).
[12] G. Pacchioni, C. Sousa, F. Illas, F. Parmigiani, and P. S. Bagus, Phys. Rev. B 48, 11573 (1993).
[13] J. Ciston, A. Subramanian, and L. D. Marks, Phys. Rev. B 79, 085421 (2009).
[14] R. Wichtendahl, M. Rodriguez-Rodrigo, U. Härtel, H. Kuhlen- beck, and H.-J. Freund, Phys. Status Solidi A 173, 93 (1999).
[15] Z. Dohnálek, G. A. Kimmel, S. A. Joyce, P. Ayotte, R. S. Smith, and B. D. Kay, J. Phys. Chem. B 105, 3747 (2001).
[16] D. R. Jung, J. Cui, and D. R. Frankl, Phys. Rev. B 43, 10042 (1991).
[17] S. L. Tait, Z. Dohnálek, C. T. Campbell, and B. D. Kay, J. Chem. Phys. 122, 164708 (2005).
[18] D. Ferry, S. Picaud, P. N. M. Hoang, C. Girardet, L. Giordano, B. Demirdjian, and J. Suzanne, Surf. Sci. 409, 101 (1998).
[19] G. Pacchioni, G. Cogliandro, and P. S. Bagus, Int. J. Quantum Chem. 42, 1115 (1992).
[20] M. A. Nygren, L. G. M. Pettersson, Z. Barandiarán, and L. Seijo, J. Chem. Phys. 100, 2010 (1994).

[21] R. Valero, J. R. B. Gomes, D. G. Truhlar, and F. Illas, J. Chem. Phys. 129, 124710 (2008).

[22] A. D. Boese and J. Sauer, Phys. Chem. Chem. Phys. 15, 16481 (2013).

[23] S. Tosoni and J. Sauer, Phys. Chem. Chem. Phys. 12, 14330 (2010).

[24] J. Carrasco, F. Illas, and N. Lopez, Phys. Rev. Lett. 100, 016101 (2008).

[25] L. A. Kappers, R. L. Kroes, and E. B. Hensley, Phys. Rev. B 1, 4151 (1970).

[26] A. M. Ferrari and G. Pacchioni, J. Phys. Chem. 99, 17010 (1995).

[27] N. A. Richter, S. Sicolo, S. V. Levchenko, J. Sauer, and M. Scheffler, Phys. Rev. Lett. 111, 045502 (2013).

[28] C. Lamberti, A. Zecchina, E. Groppo, and S. Bordiga, Chem. Soc. Rev. 39, 4951 (2010).

[29] P. Giannozzi, S. Baroni, N. Bonini, M. Calandra, R. Car, C. Cavazzoni, D. Ceresoli, G. L. Chiarotti, M. Cococcioni, I. Dabo, A. Dal Corso, S. de Gironcoli, S. Fabris, G. Fratesi, R. Gebauer, U. Gerstmann, C. Gougoussis, A. Kokalj, M. Lazzeri, L. Martin-Samos, N. Marzari, F. Mauri, R. Mazzarello, S. Paolini, A. Pasquarello, L. Paulatto, C. Sbraccia, S. Scandolo, G. Sclauzero, A. P. Seitsonen, A. Smogunov, P. Umari, and R. M. Wentzcovitch, J. Phys.: Condens. Matter 21, 395502 (2009).

[30] J. P. Perdew and Y. Wang, Phys. Rev. B 45, 13244 (1992).

[31] J. P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. Lett. 77, 3865 (1996).

[32] B. Hammer, L. B. Hansen, and J. K. Nørskov, Phys. Rev. B 59, 7413 (1999).

[33] J. P. Perdew, A. Ruzsinszky, G. I. Csonka, O. A. Vydrov, G. E. Scuseria, L. A. Constantin, X. Zhou, and K. Burke, Phys. Rev. Lett. 100, 136406 (2008).

[34] J. Wellendorff, K. T. Lundgaard, A. Møgelhøj, V. Petzold, D. D. Landis, J. K. Nørskov, T. Bligaard, and K. W. Jacobsen, Phys. Rev. B 85, 235149 (2012).

[35] J. Heyd, G. E. Scuseria, and M. Ernzerhof, J. Chem. Phys. 118, 8207 (2003).

[36] J. Heyd, G. E. Scuseria, and M. Ernzerhof, J. Chem. Phys. 124, 219906 (2006).

[37] E. Hult, Y. Andersson, B. I. Lundqvist, and D. C. Langreth, Phys. Rev. Lett. 77, 2029 (1996).

[38] P. L. Silvestrelli, K. Benyahia, S. Grubisić, F. Ancilotto, and F. Toigo, J. Chem. Phys. 130, 074702 (2009).

[39] K. Lee, É. D. Murray, L. Kong, B. I. Lundqvist, and D. C. Langreth, Phys. Rev. B 82, 081101(R) (2010).

[40] K. Tonigold and A. Groß, J. Chem. Phys. 132, 224701 (2010).

[41] P. L. Silvestrelli, A. Ambrosetti, S. Grubisić, and F. Ancilotto, Phys. Rev. B 85, 165405 (2012).

[42] P. L. Silvestrelli and A. Ambrosetti, Phys. Rev. B 87, 075401 (2013).

[43] M. Fuchs and M. Scheffler, Comput. Phys. Commun. 119, 67 (1999).

[44] N. Troullier and J. L. Martins, Phys. Rev. B 43, 1993 (1991).

[45] C. Hartwigsen, S. Goedecker, and J. Hutter, Phys. Rev. B 58, 3641 (1998).

[46] D. Bohm and D. Pines, Phys. Rev. 82, 625 (1951).

[47] D. Pines and D. Bohm, Phys. Rev. 85, 338 (1952).

[48] D. Bohm and D. Pines, Phys. Rev. 92, 609 (1953).

[49] P. Blöchl, Phys. Rev. B 50, 17953 (1994).

[50] G. Kresse and J. Hafner, Phys. Rev. B 47, 558 (1993).

[51] G. Kresse and J. Furthmüller, Comput. Mater. Sci. 6, 15 (1996).

[52] G. Kresse and D. Joubert, Phys. Rev. B 59, 1758 (1999).

[53] X. Ren, A. Tkatchenko, P. Rinke, and M. Scheffler, Phys. Rev. Lett. 106, 153003 (2011).

[54] Z. P. Chang and G. R. Barsch, J. Geophys. Res. 74, 3291 (1969).

[55] Z. P. Chang and E. K. Graham, J. Phys. Chem. Solids 38, 1355 (1977).

[56] M. Königstein and C. R. A. Catlow, J. Solid State Chem. 140, 103 (1998).

[57] L. Schimka, J. Harl, and G. Kresse, J. Chem. Phys. 134, 024116 (2011).

[58] A. S. Rao and R. J. Kearney, Phys. Status Solidi B 95, 243 (1979).

[59] P. W. Tasker, J. Phys. C 12, 4977 (1979), wOS:A1979JA36200036.

[60] D. Wolf, Phys. Rev. Lett. 68, 3315 (1992).

[61] D. Wolf, Solid State Ion. 75, 3 (1995).

[62] V. Fiorentini and M. Methfessel, J. Phys.: Condens. Matter 8, 6525 (1996).

[63] G. Jura and C. W. Garland, J. Am. Chem. Soc. 74, 6033 (1952).

[64] A. R. C. Westwood and D. L. Goldheim, J. Appl. Phys. 34, 3335 (1963).

[65] J. Ciston, A. Subramanian, D. Kienzle, and L. Marks, Surf. Sci. 604, 155 (2010).

[66] R. Armiento and A. E. Mattsson, Phys. Rev. B 72, 085108 (2005).

[67] G. I. Csonka, J. P. Perdew, A. Ruzsinszky, P. H. T. Philipsen, S. Lebègue, J. Paier, O. A. Vydrov, and J. G. Ángyán, Phys. Rev. B 79, 155107 (2009).

[68] NIST Computational Chemistry Comparison and Benchmark Database, edited by R. D. Johnson III (NIST, Gaithersburg, MD, 2013).

[69] R. M. Hazen, American Mineralogist 61, 266 (1976).

[70] R. Valero, J. R. B. Gomes, D. G. Truhlar, and F. Illas, J. Chem. Phys. 132, 104701 (2010).

[71] A. Nilsson and L. G. M. Pettersson, Surf. Sci. Rep. 55, 49 (2004).

[72] M. Staufer, U. Birkenheuer, T. Belling, F. Nörtemann, N. Rösch, M. Stichler, C. Keller, W. Wurth, D. Menzel, L. G. M. Pettersson, A. Föhlisch, and A. Nilsson, J. Chem. Phys. 111, 4704 (1999).

[73] A. Rohrbach and J. Hafner, Phys. Rev. B 71, 045405 (2005).

[74] C. Ebensperger and B. Meyer, Phys. Status Solidi B 248, 2229 (2011).

[75] H. Eshuis, J. E. Bates, and F. Furche, Theor. Chem. Acc. 131, 1 (2012).

[76] X. Ren, P. Rinke, C. Joas, and M. Scheffler, J. Mater. Sci. 47, 7447 (2012).
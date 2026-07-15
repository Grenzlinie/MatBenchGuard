PHYSICAL REVIEW B 82, 155125 (2010)

# First-principles study of electronic and vibrational properties of BaHfN₂

Amandeep Kaur,¹ Erik R. Ylvisaker,¹ Yan Li,² Giulia Galli,¹,² and Warren E. Pickett¹
¹Department of Physics, University of California, Davis, California 95616, USA
²Department of Chemistry, University of California, Davis, California 95616, USA

(Received 29 July 2010; revised manuscript received 16 September 2010; published 18 October 2010)

The transition-metal nitride BaHfN₂, which consists of weakly bonded neutral slabs of closed shell ions, has structural and chemical similarities to other layered nitrides which have impressive superconducting $T_c$ when electron-doped: $A_x$HfNCl, $A_x$ZrNCl, $A_x$TiNCl, with $T_c$=25.5, 15.2 K and 16.5 K, respectively, for appropriate donor (A) concentrations x. These similarities suggest the possibility of BaHfN₂ being another relatively high $T_c$ nitride upon doping, with effects of structure and the role of specific transition-metal ions yet to be understood. We report first-principles electronic-structure calculations for stoichiometric BaHfN₂ using density-functional theory with plane-wave basis sets and separable dual-space Gaussian pseudopotentials. An indirect band gap of 0.8 eV was obtained and the lowest conduction band is primarily of Hf $5d_{xy}$ character, similar to $\beta$-ZrNCl and $\alpha$-TiNCl. The two N sites, one in the Hf layer and another one in the Ba layer, were found to have very anisotropic Born effective charges (BEC): deviations from the formal charge (-3) are opposite for the two sites, and opposite for the two orientations (in plane, out of plane). LO-TO splittings and comparison of BECs and dielectric constant tensors to those of related compounds are discussed, and the effect of electron doping on the zone-center phonons is reported.

DOI: 10.1103/PhysRevB.82.155125
PACS number(s): 71.20.–b, 63.20.–e, 74.25.Jb, 74.25.Kc

## I. INTRODUCTION

High-temperature superconductivity has been a puzzle since the quasi-two-dimensional (2D), doped insulating copper oxides were reported to become superconducting with very high $T_c$s. Since then several other layered transition-metal oxides have been found to be good superconductors although at relatively low temperature, for example, $Li_x$NbO₂ (Ref. 1) and $Na_x$CoO₂ (Ref. 2) at about 5 K. The undoped parent compounds of the cuprate high-temperature superconductors are magnetic insulators and their transition from a magnetic insulator to a metal upon doping completely modifies their electronic structure.³ These transition-metal oxides still attract a great deal of interest because the superconductivity is not yet well understood.

Recently, interest has been growing for another class of layered superconductors, the transition-metal nitrides⁴,⁵ such as $MNX$ ($M$=Ti, Zr, Hf; $X$=Cl, Br, I) and ternary transition-metal dinitrides $AMN_2$ ($A$=alkaline earth metal, $M$=Ti, Zr, Hf), some of which have been reported to become superconducting with high $T_c$ values. Superconductivity up to 12 K was first measured in $\beta$-ZrNCl by Yamanaka *et al.* in 1996,⁴ and since then the highest $T_c$’s that have been measured for these transition-metal nitrides are as follows: 25.5 K for $Li_{0.48}(THF)_y$HfNCl,⁴ 15.2 K for intercalated $\beta$-ZrNCl (Ref. 6) and 16.5 K recently reported⁷ for $\alpha$-TiNCl upon doping with Li. These electron-doped transition-metal nitrides form a new and seemingly unconventional class of high $T_c$ superconductors because, unlike the transition-metal oxides, the parent compounds are not Mott insulators. The parent compounds for these layered quasi-2D nitrides are nonmagnetic ionic band insulators with a gap in the range of 2–4 eV.⁸⁻¹⁰

In these transition-metal nitrides, the superconducting mechanism presents a real conundrum. Experimental measurements of the isotope effect¹¹ in $Li_x$ZrNCl show a very weak dependence on the N mass, suggesting that electron-phonon mediated pairing cannot adequately account for the superconductivity in the $MNX$ family. Specific heat measurements on $Li_x$ZrNCl (Ref. 12) estimate the upper limit for the electron-phonon coupling constant $\lambda \approx 0.2$ for $Li_{0.12}$ZrNCl. A theoretical study on $Li_x$ZrNCl (Ref. 13) predicted the coupling constant on the average around 0.5. The computed and the estimated coupling constant is far too small to account for the $T_c$ of 12–15 K. The magnetic susceptibility measurements¹⁴ also give a mass enhancement factor that appears too small for electron-phonon coupling.

There is no clear evidence of strong electronic correlations in the transition-metal nitrides. These compounds do not show the antiferromagnetism that is characteristic of strong correlations nor even the Curie-Weiss susceptibility that signals local moments, and there is no frustration on either the honeycomb lattice or rectangular lattice. In fact, the bandwidths of the $d$ states (where doped electrons reside) are rather large¹⁵ and undoped systems are in $d^0$ configurations, so these systems should be well described (except for the value of the gap) by first-principles calculations employing the local-density approximation (LDA). There is no observation of magnetism in the parent compounds at all, so the possibility of spin fluctuations as a pairing mechanism, similar to what is thought by some to cause superconductivity in cuprates, seems unlikely. While a possible pairing mechanism mediated by magnetic fluctuations has been suggested,¹⁶ this mechanism seems at odds with observed behavior so far. Some groups have also proposed charge fluctuations¹⁷,¹⁸ as a pairing mechanism or plasmon enhancement of weak BCS superconductivity.

In this paper we focus on the ternary nitride BaHfN₂, whose electronic structure and vibrational properties have not yet been studied theoretically. This compound has many chemical and structural similarities with the layered transition-metal nitrides $MN$Cl’s ($M$=Ti,Hf,Zr) that are impressive superconductors when they are electron doped. We

1098-0121/2010/82(15)/155125(9)
155125-1
©2010 The American Physical Society

TABLE I. Structurally optimized lattice constants ($a$ and $c$) and reduced internal coordinates ($z$) for atoms in the unit cell, obtained from different sets of pseudopotentials (PSPs) including Hartwigsen-Goedecker-Hutter (HGH) (Refs. 19 and 20) and Troullier-Martin (TM) (Ref. 21) type PSPs. The inclusion of semicore $5s$ and $5p$ states for Ba and Hf PSPs are indicated by Ba$^{sc}$ and Hf$^{sc}$, respectively. The computed band gap for the experimental geometry, $E_{g}^{exp}$, is compared with FPLO (FLAPW) results.

<table>
  <thead>
    <tr>
      <th></th>
      <th>PSP</th>
      <th>$a/a_{exp}$</th>
      <th>$c/c_{exp}$</th>
      <th>$z$ (Ba)</th>
      <th>$z$ (Hf)</th>
      <th>$z$ (N2)</th>
      <th>$E_{g}^{exp}$ (eV)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>LDA</td>
      <td>FPLO</td>
      <td>0.992</td>
      <td>0.986</td>
      <td>0.846</td>
      <td>0.415</td>
      <td>0.177</td>
      <td>0.68</td>
    </tr>
    <tr>
      <td></td>
      <td>FLAPW</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>0.8</td>
    </tr>
    <tr>
      <td></td>
      <td>HGH, Ba$^{sc}$, Hf$^{sc}$</td>
      <td>0.986</td>
      <td>0.982</td>
      <td>0.848</td>
      <td>0.415</td>
      <td>0.176</td>
      <td>0.82</td>
    </tr>
    <tr>
      <td></td>
      <td>TM</td>
      <td>1.005</td>
      <td>1.017</td>
      <td>0.846</td>
      <td>0.415</td>
      <td>0.177</td>
      <td>0.78</td>
    </tr>
    <tr>
      <td></td>
      <td>TM, Ba$^{sc}$</td>
      <td>0.997</td>
      <td>0.987</td>
      <td>0.849</td>
      <td>0.413</td>
      <td>0.170</td>
      <td>0.87</td>
    </tr>
    <tr>
      <td></td>
      <td>TM, Ba$^{sc}$, Hf$^{sc}$</td>
      <td>0.984</td>
      <td>0.972</td>
      <td>0.847</td>
      <td>0.415</td>
      <td>0.177</td>
      <td>1.11</td>
    </tr>
    <tr>
      <td>PBE</td>
      <td>HGH, Ba$^{sc}$, Hf$^{sc}$</td>
      <td>1.000</td>
      <td>1.007</td>
      <td>0.848</td>
      <td>0.415</td>
      <td>0.180</td>
      <td>0.95</td>
    </tr>
    <tr>
      <td></td>
      <td>TM</td>
      <td>1.022</td>
      <td>1.036</td>
      <td>0.845</td>
      <td>0.416</td>
      <td>0.186</td>
      <td>1.00</td>
    </tr>
    <tr>
      <td></td>
      <td>TM, Ba$^{sc}$</td>
      <td>1.011</td>
      <td>1.008</td>
      <td>0.850</td>
      <td>0.413</td>
      <td>0.175</td>
      <td>1.13</td>
    </tr>
    <tr>
      <td></td>
      <td>TM, Ba$^{sc}$, Hf$^{sc}$</td>
      <td>1.004</td>
      <td>0.999</td>
      <td>0.849</td>
      <td>0.414</td>
      <td>0.179</td>
      <td>1.25</td>
    </tr>
    <tr>
      <td>Exp.$^{\mathrm{a}}$</td>
      <td></td>
      <td></td>
      <td></td>
      <td>0.8479</td>
      <td>0.4142</td>
      <td>0.168</td>
      <td></td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <td colspan="8">${}^{\mathrm{a}}$Reference 5.</td>
    </tr>
  </tfoot>
</table>

suggest that this compound has the potential to provide another high $T_{c}$ transition-metal nitride superconductor when electron doped. In this paper we present calculations of the electronic structure, lattice vibrations, and dielectric constant tensors of BaHfN$_2$, and compare them with those of other nitrides. This comparison with other layered nitrides may help in predicting the origin of the superconductivity in these layered nitrides.

The rest of the paper is organized as follows. We first describe the crystal structure of BaHfN$_2$ (Sec. II) and the computational methods (Sec. III). Then we present our results for structural and electronic properties of BaHfN$_2$ (Sec. IV), followed by analysis of the vibrational properties (Sec. V). Finally, we discuss the case when BaHfN$_2$ is electron doped by replacing one of the two Ba atoms in the unit cell by a La atom (Sec. VI). A summary of our findings in Sec. VII concludes the paper.

## II. STRUCTURE

We use structural coordinates for BaHfN$_2$ from powder x-ray diffraction measurements reported by Gregory $et$ $al.^{5}$ The nitrodohafnate BaHfN$_2$ crystallizes in the tetragonal space group $P4/nmm$, for which KCoO$_2$ is the customary example. The measured lattice constants are $a$=4.128 Å and $c$=8.382 Å. There are two inequivalent N sites which we denote N1 (lying nearly in the Hf plane) and N2 (nearly in the Ba plane), i.e., BaN2-HfN1. Ba, Hf, and N2 occupy Wyckoff position 2c $(\frac{1}{4},\frac{1}{4},z)$ and N1 occupies position 2b $(\frac{3}{4},\frac{1}{4},\frac{1}{2})$ (see Table I).

The structure of BaHfN$_2$ shown in Fig. 1 is sometimes described as composed of $[{\mathrm{HfN}}_{2}]^{2-}$ anions and Ba$^{2+}$ cations.$^{5}$ These anions are composed of Hf atoms inside a square pyramid of five nitrogen atoms (four N1's and one N2), forming layers of edge sharing pyramids stacked along the $c$ axis; the apices of adjoining pyramids are aligned alternatively up and down along the $c$ axis. The Ba$^{2+}$ cations are situated between these Hf-N sheets levelled with the pyramid apices.

Another description for the structure of BaHfN$_2$ comprises of (nearly) coplanar (BaN2)$^{-}$ layer and a corrugated (HfN1)$^{+}$ layer, with Hf ions lying alternately above and below the N2 layer. Each neutral BaN2-HfN1-N1Hf-N2Ba structural unit [outlined in Fig. 1(a)] is weakly bonded to neighboring units in the $c$ direction; upon intercalation, dopant ions will lie between the Ba-N2 layers. Similarly, in $\alpha$-TiNCl [Fig. 1(b)] there is a layer of transition-metal (Ti) atoms and N atoms, with Cl$^{-}$ ions playing a role analogous to the (BaN2)$^{-}$ unit in BaHfN$_2$. Neutral TiNCl slabs are weakly bound to each other. A more detailed study of that compound will be presented separately.

As we show below, the site energies and bonding of the N1 and N2 sites are quite different, and the simple viewpoint of formal closed shell ions, e.g., Ba$^{2+}$, Hf$^{4+}$, and N$^{3-}$ may not be sufficient to address the structural relationships.

![](./images/811712687145746433_1.jpg)

FIG. 1. (Color online) (a) Layered geometry of BaHfN$_2$: N$^{3-}$ anions form a square base pyramid around Hf$^{4+}$, forming a $[{\mathrm{HfN}}_{2}]^{2-}$ anion. Ba$^{2+}$ cations sit in between the tips of the pyramids. (b) Layered $\alpha$-TiNCl structure.

### III. DESCRIPTION OF CALCULATIONS

We carried out density-functional theory (DFT) calculations with the ABINIT package,22 within both LDA and gradient corrected [generalized gradient approximation (GGA)/Perdew-Burke-Ernzerhof (PBE) (Ref. 23)] exchange and correlation functionals. Norm-conserving pseudopotentials (PSPs) in the relativistic separable dual-space Gaussian Hartwigsen-Goedecker-Hutter (HGH) form19,20 were used to treat the electronic configuration of Ba (5s, 5p, 6s), Hf (5s, 5p, 5d, 6s), and N (2s, 2p), including 5s and 5p semicore states for Ba and Hf. Plane wave basis sets with a kinetic energy cutoff of 120 Ry were used. A 8×8×4 Monkhorst-Pack24 k-point grids were used to sample the Brillouin zone for ground state calculations. We have checked that further increasing the cutoff energy to 140 Ry or the k-point grid to 12×12×6 and 18×18×6 has a negligible influence on the relaxed geometry and phonon frequencies. The computed LDA band structure of BaHfN₂ at experimental geometry was found to agree well with results obtained from the full-potential, all-electron code FPLO;25 the latter also provides a convenient way to compute contributions to the electronic bands and density of states (DOS) from individual atomic orbitals. We have confirmed that spin-orbit coupling has no significant influence to the band structure. Phonon calculations are done within density functional perturbation theory26 and are carried out at the Γ point, and the obtained frequencies and displacement eigenmodes were used to compute Born effective charges (BEC) and the static dielectric tensor ϵ₀.

To examine the influence of PSPs on the calculated structural, electronic and vibrational properties of BaHfN₂, especially the inclusion of 5s, 5p semicore states for Ba and Hf, we also carried DFT calculations using Troullier-Martin (TM) (Ref. 21) PSPs generated using the FHI98PP program27 with LDA/Perdew-Zunger (PZ) (Ref. 28) and GGA/PBE exchange-correlation functionals, respectively. A 8×8×4 k-grid and a kinetic-energy cut off of 90 Ry were used.

To simulate the doped BaHfN₂, we replaced one of the two Ba atoms in the unit cell with La, which provides an extra electron per formula unit and provides metallic screening with its impact on the zone-center phonons. HGH PSPs with semicore states 5s and 5p for Ba, Hf, and La were used to do calculations for the doped system with kinetic-energy cut-off of 120 Ry and a k-point mesh of 12×12×6.

### IV. ELECTRONIC-STRUCTURE CALCULATIONS

#### A. Structural relaxation and electronic structure

It is instructive for future studies to quantify the effects of different types of pseudopotentials on the relaxed structure and the energy gap. We have performed structural relaxation for the BaHfN₂ crystal using both LDA and GGA/PBE, and results are compared with experimental geometry⁵ in Table I. In addition to the HGH PSPs, we also employed different sets of norm-conserving TM PSPs. The inclusion of 5s and 5p semicore states, if present, is denoted by Ba^sc and Hf^sc, respectively. The optimized cell parameters and internal coordinates were compared with all-electron, full potential reference results from FPLO.25 The band gap was computed for the experimental geometry, E_g^exp using FPLO (Ref. 25) and full-potential linear-augmented plane waves code (FP-LAPW) implemented in the ELK code.29 The results are listed in Table I.

![](./images/811712687145746433_2.jpg)

FIG. 2. (Color online) Projected density of States (PDOS) showing strong hybridization of Ba 5p semicore states with N2 2s states and a weak mixing with N2 2p states.

One observation from Table I is that as one includes semicore states of Ba and Hf, the equilibrium lattice constants becomes smaller while the energy gap E_g^exp increases substantially. Such trend holds for both LDA and PBE PSPs of TM type. The inclusion of semicore states is important since there is significant amount of hybridization of Ba semicore 5p states with N2 2s state, as can be seen from Fig. 2. We observed a trend of decrease in equilibrium lattice constants upon inclusion of semicore states. This is mainly due to the decrease in Ba-N2 and Ba-Hf bond length.

On the other hand, TM-type PSPs generated using the FHI98PP code are so-called single projector pseudopotentials, e.g., there is only one pseudopotential for each angular momentum type, not for each valence orbital. The corresponding PSPs with Ba^sc and/or Hf^sc failed to describe the energy position of 6s states properly, even for the isolated atoms. Such PSPs tend to predict energy gaps of BaHfN₂ larger than those without the semicore states in the valence configuration. The discrepancy in E_g^exp compared with all-electron calculations can be as much as 0.4 eV. The HGH pseudopotentials, on the other hand, were constructed with multiple projectors per angular momentum type and therefore can describe orbitals of same angular momentum but different shells reasonably well. Indeed, from Table I, we find that overall HGH pseudopotentials give structural properties and energy gap similar to those calculated from all-electron calculation and in the following, we present results obtained with LDA type HGH pseudopotentials.

Figure 3 shows the band structure of BaHfN₂, using the so-called fatbands emphasis of band character for Hf 5d_xy states. The fatbands are obtained by using the expansion of the wave functions in terms of the basis atomic orbitals at each k point

$$
|\mathbf{k} n\rangle=\sum_{\mathbf{R s} L} c_{L s}^{\mathbf{k} n} e^{i \mathbf{k} \cdot(\mathbf{R}+\mathbf{s})}|\mathbf{R s} L\rangle,
\tag{1}
$$

where n is the band index and L≡lm is the orbital index. R+s denotes a regular lattice site, with R a Bravais lattice

![](./images/811712687145746433_3.jpg)

FIG. 3. (Color online) (a) Band structure showing Hf $5d$ bands. The amount of Hf $5d_{xy}$ character is shown in the band structure by the width of the lines, revealing that the lowest conduction band has strong Hf $5d_{xy}$ character. (b) The density of states, units for horizontal axis are per electron volt. The shaded area indicates the amount of Hf $5d$ character. The Fermi level lies at the bottom of the lowest conduction band.

vector and $\mathbf{s}$ a basis vector of the unit cell. The width of the fatband is proportional to $|c_{Ls}^{kn}|^{2}$.

BaHfN$_2$ is a band insulator with a calculated band gap 0.68–0.80 eV using full-potential, all-electron methods (FPLO, LAPW). Given the usual LDA underestimate of band gaps the true gap of BaHfN$_2$ may be as large as 1.5 eV. This layered ionic semiconductor character is very similar to that of the MNCl compounds ($M$=Ti,Hf,Zr) which have been found to superconduct with impressively high $T_c$ values when electron-doped. The lowest conduction band in BaHfN$_2$ has primarily Hf $5d_{xy}$ character with a width of 3 eV. Since these states are empty, Hf is formally 4+, and the rest of the electronic structure is indicative of a closed shell, ionic insulator with some mixing of N $2p$ states and Hf $5d$ states. This characterization is similar to ZrNCl, which is also an ionic semiconductor with lowest conduction band having Zr in-plane $4d$ character, $^{15}$ and TiNCl which has Ti $3d_{xy}$ character.$^{7,30}$ The Hf $5d$ character extends through a range of 8 eV beyond the Fermi level [see Fig. 2(b)] partially due to crystal-field splitting of the $5d$ orbitals.

Figure 4 shows the projected DOS (PDOS) in the valence-conduction band region. Integrating the density of states, we find that only above a doping level of 0.17 electrons (shifting the Fermi level upward by 0.9 eV) do bands other than the two-dimensional Hf $5d_{xy}$ band start filling up with electrons. The conduction bands which appear at 0.9 eV above the Fermi level are Ba $5d$ states at $M$ that have some dispersion along $k_z$ (compare the points $M$ and $A$). There is also some nitrogen hybridization in the conduction bands that contribute to their in-plane dispersion.

As mentioned earlier, there are two N sites, corresponding to the corrugated layers Hf$^{4+}$N1$^{3-}$ and the nearly flat Ba$^{2+}$N2$^{3-}$ layers. The projected DOS shows that the N1 and N2 ions are quite distinct in electronic character. The N2 ion in the BaN2 layer has the more weakly bound (and therefore more polarizable) N $2p$ states, lying just below the gap. The energy states of N1 ion in the HfN1 layer (closer to the highly charged Hf$^{4+}$ ion) is centered about 2 eV lower in energy. From purely energetic (binding) consideration, N1 should have a correspondingly lower polarizability.

![](./images/811712687145746433_4.jpg)

FIG. 4. (Color online) Total density of states (DOS) for BaHfN$_2$, with projected density of states for (a) Ba, Hf with (b) blowup of conduction bands, and (c) N1, N2 with (d) blowup of conduction bands. The lowest conduction bands, are composed of Hf $5d_{xy}$ states. (b) and (d) show almost 2D like behavior around the bottom of the conduction band up to $\sim$0.9 eV, where Ba conduction states start to appear.

### B. Fermi surface for electron doping

According to our band structure calculations in Fig. 3, when BaHfN$_2$ is electron-doped (as are ZrNCl, HfNCl, and TiNCl when they become superconducting), the Fermi surface will be a single $\Gamma$-centered (nearly) circular surface up to $x$=0.17 for doping concentration $x$ when doped with alkali metals; for doping concentration $x$$>$0.17 carriers also go into the bottom of the Ba $5d$ bands at $M$ and then additional Hf $5d$ bands at $\Gamma$. In this respect, BaHfN$_2$ is similar to TiNCl (Ref. 30) but different from the hexagonal compounds [(Zr,Hf)NCl] which have the band minimum at the zone corner $K$ points, of which there are two.

This difference in Fermi surfaces has some importance for electronic response. In the doped (Zr,Hf)NCl compounds, nesting of the two Fermi surfaces has recently been put forward$^{31}$ as a potential source of spin fluctuations, which was suggested as a possible candidate for pairing mechanism. However, with a single simple Fermi surface such as displayed by doped TiNCl (known to be an excellent superconductor) and doped BaHfN$_2$ (which we suggest by analogy may be a good superconductor), this mechanism is not available. Since the superconducting $T_c$ is large (and almost similar in magnitude) in TiNCl and ZrNCl, and their characters are otherwise so similar but Fermi surfaces are different, the mechanism of spin fluctuations seems to be degraded in likelihood. Electron-phonon coupling is weak in $A_x$ZrNCl, and the materials are pauli-paramagnetic. Thus for possible pairing in these materials, long sought electronic mechanisms of pairing need consideration. A single electron gas with a given value of $k_F$ is different from a pair of identical, degenerate electron gases with a value of $k_F$ that is $1/\sqrt{2}$ as large. One main difference, as mentioned above, is that there is no nesting that might enhance charge fluctuations (as is the case

<table>
<caption>TABLE II. Born effective charges (BECs) of BaHfN₂ and metallochloronitrides MNCl (M=Hf,Zr,Ti). All BECs have been calculated at experimental lattice constants and relaxed atomic positions. α-TiNCl is orthorhombic, so \(Z_{xx}^* \neq Z_{yy}^*\) and both are listed. For comparison, BECs of NaCoO₂ (Ref. 32) are also listed.</caption>
<tbody><tr><td></td><td colspan="4">BaHfN₂</td><td colspan="3">β-HfNCl</td><td colspan="3">β-ZrNCl</td><td colspan="3">α-TiNCl</td><td colspan="3">NaCoO₂</td></tr>
<tr><td></td><td>Hf</td><td>N1</td><td>N2</td><td>Ba</td><td>Hf</td><td>N</td><td>Cl</td><td>Zr</td><td>N</td><td>Cl</td><td>Ti</td><td>N</td><td>Cl</td><td>Na</td><td>Co</td><td>O</td></tr>
<tr><td>\(Z_{xx}^*/Z_{yy}^*\)</td><td>4.52</td><td>−4.66</td><td>−2.59</td><td>2.73</td><td>4.7</td><td>−3.4</td><td>−1.2</td><td>5.1</td><td>−3.8</td><td>−1.3</td><td>5.9/6.4</td><td>−5.5/−4.4</td><td>−0.4/−1.9</td><td>0.87</td><td>2.49</td><td>−1.68</td></tr>
<tr><td>\(Z_{zz}^*\)</td><td>3.09</td><td>−1.65</td><td>−4.58</td><td>3.14</td><td>2.5</td><td>−1.6</td><td>−0.9</td><td>2.6</td><td>−1.6</td><td>−1.0</td><td>1.7</td><td>−0.9</td><td>−0.8</td><td>1.37</td><td>0.87</td><td>−1.12</td></tr>
<tr><td>\(Z^{\text{Formal}}\)</td><td>+4</td><td>−3</td><td>−3</td><td>+2</td><td>+4</td><td>−3</td><td>−1</td><td>+4</td><td>−3</td><td>−1</td><td>+4</td><td>−3</td><td>−1</td><td>+1</td><td>+3</td><td>−2</td></tr>
</tbody></table>

also for spin fluctuations) or affect pairing symmetry. An- other clear difference is that the characteristic momentum scale \(k_F\) is different.

## V. VIBRATIONAL SPECTRUM
### A. Born-effective charges

The MNCl compounds become superconducting upon electron doping from an ionic insulator to the metallic phase. The relatively low-density electron gas that is formed upon light doping might not adequately screen the ionic nature of the MN layers, so the electronic response may still have short-range ionic character. For this reason we calculate and analyze the Born effective charges in some detail.

The BEC tensor \(Z^*\) is a fundamental quantity for the study of lattice dynamics, describing the long range Cou- lomb part of the force constants. The Born effective charge \(Z_{\kappa,\gamma\alpha}^*\) of atom \(\kappa\) can be viewed either as the change in polarization \(P_\gamma\) induced by the periodic displacement \(\tau_{\kappa,\alpha}\) under the condition of zero macroscopic electric field, or as the force \(F_{\kappa,\alpha}\) induced on atom \(\kappa\) by an electric field \(\mathcal{E}_\gamma\) under the condition of no atomic displacement. It can also be ex- pressed as the second partial derivative of the total energy with respect to the displacement and the electric field

$$
Z_{\kappa, \gamma \alpha}^{*}=V \frac{\partial P_{\gamma}}{\partial \tau_{\kappa, \alpha}}=\frac{\partial F_{\kappa, \alpha}}{\partial \mathcal{E}_{\gamma}}=-\frac{\partial^{2} E}{\partial \mathcal{E}_{\gamma} \partial \tau_{\kappa, \alpha}},\qquad(2)
$$

where \(V\) is the volume of the unit cell. One might naively expect the BECs to be close to the formal charges of the compound but this is often not the case. The BEC can be decomposed into the charge of the (pseudo-) ion \(\kappa\), \(Z_{\kappa}\), and the electronic screening term, \(\Delta Z_{\kappa,\gamma\alpha}\).

$$
Z_{\kappa, \gamma \alpha}^{*}=Z_{\kappa, \gamma \alpha}+\Delta Z_{\kappa, \gamma \alpha}.\qquad(3)
$$

The computed BECs for BaHfN₂ are provided in Table II. In tetragonal symmetry the BEC tensor is diagonal and re- duces to two values \(Z_{xx}^*=Z_{yy}^*\) and \(Z_{zz}^*\). The BECs for Hf and Ba in the plane are reasonably close to their formal charges (Hf is 0.52 larger and Ba is 0.73 larger) while their perpen- dicular charges differ substantially from the formal charges (being smaller than the formal charge for Hf) indicating a more complex electronic response.

The two nitrogen sites have very different and unusual BECs. For comparison, previously calculated³² BECs of NaCoO₂ are also listed in Table II. The BECs for O in NaCoO₂ are rather uninteresting, both being smaller than their respective formal charges. By contrast, in BaHfN₂, N1 has a BEC of −4.66 in the plane and −1.65 perpendicular to the plane, respectively, with magnitude much larger and much smaller than the formal charge. N2, on the other hand, has a BEC of −2.6 in the plane and about −4.6 perpendicular to the plane, again very different from the formal charge but in the opposite sense with respect to N1. The BEC of N1 is consistent with covalent bonding between N1 and Hf, given its anomalously large magnitude in the plane. N2 behaves in the opposite way, and its BEC is consistent with little cova- lent bonding with Ba (as expected) but with significant co- valent interaction with Hf in the inner layer. BECs with mag- nitudes greater than the formal charges reflect large electronic response to atomic motion. For example, in the case of perovskite BaHfO₃ (Ref. 33) the large Born-effective charges of Hf (\(Z^*=5.75\)) and O (\(Z_{||}^*=-4.42,Z_{\perp}^*=-2.03\)) indicate a mixed ionic-covalent nature of Hf-O bond, similar to the case found here for the Hf-N1 bond. Also, Ba in BaHfO₃, which has a cubic site symmetry, was found to have a similar average BEC [\(Z^*=2.72\) as that computed for Ba in BaHfN₂ here (\(Z^*=2.87\))].

The Hf-N1 layer, taken as a unit, behaves as if having a charge of −0.14 (nearly neutral) in the plane and +1.44 (slightly cationic, rather consistent with the formal charges) for vibrations perpendicular to the plane. The Ba-N2 layer behaves in an opposite manner.

In Table II, we draw a comparison between the BECs of metallochloronitrides MNCl (M=Ti,Hf,Zr) (Refs. 30 and 34) and those of BaHfN₂. BECs of N in MNCl's show simi- lar trends as those of N1 in the case of BaHfN₂. There is considerable anisotropy in the effective charges for both the M and N ions. The effective charge for Cl in MNCl is close to its formal charge (reflecting its high electronegativity), however, the Cl analog in BaHfN₂, Ba-N2, is somewhat dif- ferent, with large anisotropy.

### B. Zone-center phonons

BaHfN₂ has eight atoms in the unit cell resulting in 24 phonon modes, three of which are acoustic modes and the remaining 21 are optical modes. The phonon frequencies are listed in Table III with their polarization and symmetry. There are \(8E_g+6E_u\) modes with polarization perpendicular to the c axis (within the x-y plane) and \(3A_{1g}+3A_{2u}+1B_{1g}\) modes with polarization along the z axis. The modes \(A_{1g}\), \(B_{1g}\), and \(E_g\) are Raman active, and the modes \(A_{2u}\), \(E_u\) are

TABLE III. Calculated zone-center phonon frequencies for BaHfN₂ and Ba₀.₅La₀.₅HfN₂. The phonons were computed using the optimized geometry. All phonons with x-y polarization are doubly degenerate. The symmetry column refers to the symmetry of the phonons in higher symmetry insulating system (point group $D_{4h}$ vs $C_{4v}$ for the metallic system). There is a split in degeneracy in the long wavelength limit between the LO and TO modes, and the magnitude of LO-TO splitting, $\sqrt{\omega_{\text{LO}}^{2}-\omega_{\text{TO}}^{2}}$, is listed in the last column. All frequencies reported in inverse centimeters.

<table>
  <thead>
    <tr>
      <th rowspan="2">Mode</th>
      <th rowspan="2">Symmetry</th>
      <th rowspan="2">Polarization</th>
      <th colspan="3">BaHfN₂ frequency</th>
      <th rowspan="2">Ba₀.₅La₀.₅HfN₂ frequency</th>
    </tr>
    <tr>
      <th>$\omega_{\text{TO}}$</th>
      <th>$\omega_{\text{LO}}$</th>
      <th>$\sqrt{\omega_{\text{LO}}^{2}-\omega_{\text{TO}}^{2}}$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1–2ᵃ</td>
      <td>$E_{u}$</td>
      <td>x-y</td>
      <td>72</td>
      <td>93</td>
      <td>59</td>
      <td>76</td>
    </tr>
    <tr>
      <td>3–4ᵇ</td>
      <td>$E_{g}$</td>
      <td>x-y</td>
      <td>82</td>
      <td></td>
      <td></td>
      <td>94</td>
    </tr>
    <tr>
      <td>5ᵃ</td>
      <td>$A_{2u}$</td>
      <td>z</td>
      <td>105</td>
      <td>144</td>
      <td>98</td>
      <td>144</td>
    </tr>
    <tr>
      <td>6ᵇ</td>
      <td>$A_{1g}$</td>
      <td>z</td>
      <td>120</td>
      <td></td>
      <td></td>
      <td>136</td>
    </tr>
    <tr>
      <td>7–8ᵇ</td>
      <td>$E_{g}$</td>
      <td>x-y</td>
      <td>152</td>
      <td></td>
      <td></td>
      <td>148</td>
    </tr>
    <tr>
      <td>9ᵇ</td>
      <td>$A_{1g}$</td>
      <td>z</td>
      <td>172</td>
      <td></td>
      <td></td>
      <td>175</td>
    </tr>
    <tr>
      <td>10–11ᵃ</td>
      <td>$E_{u}$</td>
      <td>x-y</td>
      <td>210</td>
      <td>240</td>
      <td>116</td>
      <td>210</td>
    </tr>
    <tr>
      <td>12–13ᵇ</td>
      <td>$E_{g}$</td>
      <td>x-y</td>
      <td>232</td>
      <td></td>
      <td></td>
      <td>283</td>
    </tr>
    <tr>
      <td>14ᵇ</td>
      <td>$B_{1g}$</td>
      <td>z</td>
      <td>341</td>
      <td></td>
      <td></td>
      <td>328</td>
    </tr>
    <tr>
      <td>15–16ᵃ</td>
      <td>$E_{u}$</td>
      <td>x-y</td>
      <td>424</td>
      <td>614</td>
      <td>444</td>
      <td>475</td>
    </tr>
    <tr>
      <td>17ᵃ</td>
      <td>$A_{2u}$</td>
      <td>z</td>
      <td>468</td>
      <td>492</td>
      <td>152</td>
      <td>457</td>
    </tr>
    <tr>
      <td>18–19ᵇ</td>
      <td>$E_{g}$</td>
      <td>x-y</td>
      <td>623</td>
      <td></td>
      <td></td>
      <td>651</td>
    </tr>
    <tr>
      <td>20ᵃ</td>
      <td>$A_{2u}$</td>
      <td>z</td>
      <td>641</td>
      <td>751</td>
      <td>391</td>
      <td>596</td>
    </tr>
    <tr>
      <td>21ᵇ</td>
      <td>$A_{1g}$</td>
      <td>z</td>
      <td>717</td>
      <td></td>
      <td></td>
      <td>646</td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <td colspan="7">ᵃIR active mode.</td>
    </tr>
    <tr>
      <td colspan="7">ᵇRaman active mode.</td>
    </tr>
  </tfoot>
</table>

infrared active. We found some phonon frequencies were quite sensitive to the inclusion of semicore states in Ba and Hf pseudopotentials with several phonons differing by 15–30 % in the absence of semicore states.

The LO-TO splittings of the IR active modes can be related to the Born-effective charges as

$$
\sum_{m}\left[\omega_{\mathrm{LO}, m}^{2}-\omega_{\mathrm{TO}, m}^{2}\right]=\frac{4 \pi}{\epsilon_{\alpha \alpha}^{\infty} V} \sum_{\kappa} \frac{\left(e Z_{\kappa, \alpha \alpha}^{*}\right)^{2}}{M_{\kappa}}. \tag{4}
$$

In this relation, $m$ goes over the IR active modes of a given polarization direction $\alpha$, $M_{\kappa}$ is the ionic mass of the atom $\kappa$, and $\epsilon_{\alpha \alpha}^{\infty}$ is the $\alpha$th diagonal element of the high-frequency dielectric constant. When the LO phonons are excited, a macroscopic electric field is created due to the long range nature of the Coulomb interaction. The squares of the BECs, divided by the mass, give the contribution of that ion to the electric field. One interesting example (see Table III): the large splitting $(\Delta \omega)$ of mode 15 is due largely to the fact that the light N1 ions are vibrating in the x-y plane and the BEC for N1 is rather large (-4.66), accounting for most of the shift of 45% in LO frequency. The second largest splitting $(\Delta \omega)$ is for the mode 20, with a shift of about 17% in frequency. In this mode we have primarily N2 vibrating along the $z$ direction and the BEC for N2 along $z$ is $Z_{z z}^{*}(\mathrm{~N} 2)=$ -4.58 which again accounts for the large splitting. Mode 5 has a large relative shift of 37%; it has primarily N1 and Ba vibrations opposite to each other (for description of the modes please see the Appendix).

### C. Dielectric response

We now discuss the electronic and ionic lattice contributions to the macroscopic dielectric constants, computed for BaHfN₂ by doing the phonon calculation using both experimental lattice constants with relaxed geometry and completely relaxed geometry. $\epsilon^{\infty}$ denotes the high-frequency electronic response where there is no contribution from the ionic lattice polarizability $(P^{ion})$ and $\epsilon^{0}$ is the sum of the electronic and ionic response. Their relationship is given by

$$
\epsilon_{\alpha \beta}^{0}=\epsilon^{e l}+4 \pi P^{i o n}=\epsilon_{\alpha \beta}^{\infty}+4 \pi \sum_{m} P_{m, \alpha \beta}, \tag{5}
$$

$$
P_{m, \alpha \beta}=\frac{1}{\Omega} \frac{S_{m, \alpha \beta}}{\omega_{m}^{2}}, \tag{6}
$$

where the sum is over all the modes and $S_{m, \alpha \beta}$ is the mode-oscillator strength tensor which is defined as

$$
S_{m, \alpha \beta}=\sum_{\kappa, \alpha^{\prime}} Z_{\kappa, \alpha \alpha^{\prime}}^{*} U_{m}\left(\kappa, \alpha^{\prime}\right) \times \sum_{\kappa^{\prime}, \beta^{\prime}} Z_{\kappa^{\prime}, \beta \beta^{\prime}}^{*} U_{m}\left(\kappa^{\prime}, \beta^{\prime}\right), \tag{7}
$$

where $U_{m}(\kappa, \alpha)$ is the component of the phonon eigenvector for the $m$th mode corresponding to the displacement of the atom $\kappa$ in direction $\alpha$.

The values of the static dielectric constants for BaHfN₂ and comparison to the group IVB metallochloronitrides³⁴ are given in Table IV. $\epsilon^{\infty}$ for BaHfN₂ is larger than for the metallochloronitrides (the electronic polarizability $\epsilon^{\infty}-1$ is


<table><caption>TABLE IV. Calculated macroscopic dielectric constants for BaHfN₂ and group IVB nitrochlorides using (a) fully relaxed geometry and (b) the experimental structure with relaxed atomic positions.</caption>
<tbody><tr><th></th><th></th><td>$\epsilon_{xx/yy}^{\infty}$</td><td>$\epsilon_{zz}^{\infty}$</td><td>$\epsilon_{xx/yy}^{0}$</td><td>$\epsilon_{zz}^{0}$</td></tr>
<tr><td>(a)</td><td>BaHfN₂</td><td>7.47</td><td>7.55</td><td>33.8</td><td>21.4</td></tr>
<tr><td>(b)</td><td>BaHfN₂</td><td>7.35</td><td>7.31</td><td>44.7</td><td>24.0</td></tr>
<tr><td>(b)</td><td>$\alpha$-TiNCl</td><td>6.9/7.4</td><td>3.2</td><td>22.3/38.3</td><td>3.7</td></tr>
<tr><td>(b)</td><td>$\beta$-ZrNCl</td><td>6.2</td><td>4.4</td><td>13.8</td><td>5.9</td></tr>
<tr><td>(b)</td><td>$\beta$-HfNCl</td><td>5.4</td><td>4.0</td><td>11.1</td><td>5.1</td></tr>
</tbody></table>

50–60 % larger than the Hf counterpart), consistent with the smaller band gap (0.8 eV versus around 1.8 eV for ZrNCl and HfNCl).

With the exception of the in-plane values for TiNCl, the lattice polarizability $\epsilon^{0}-\epsilon^{\infty}$ of other MNCI’s is smaller by a factor of 5–15 relative to that of BaHfN₂. This is due to the fact that the phonons in BaHfN₂ are softer than the phonons in MNCI’s and the oscillator strengths for modes which contribute to $P^{ion}$ in BaHfN₂ are much larger than the modes contributing to $P^{ion}$ for the other chloronitrides. The modes that contribute to lattice polarizability $P^{ion}$ in BaHfN₂ are shown in Table V together with their contributions. The main contribution arises from the lowest IR active mode for each direction ($x$ and $z$). We found that the frequency of the lowest IR mode in the plane is highly sensitive to the inclusion of the semicore states in Ba pseudopotential, and as a result when these states absent $\varepsilon_{xx}^{0}$ is reduced from 44.7 to 17.3.

For some comparison we note the dielectric constants for a few transition-metal nitrides. The high-frequency dielectric constants for group IVB nitrides have been reported³⁵ as follows: Ti₃N₄, Zr₃N₄, and Hf₃N₄ with $\epsilon^{\infty}$=18.31, 9.36, and 10.10, respectively. Ti₃N₄ has a higher dielectric constant due to a small band gap.

## VI. DOPING WITH ELECTRONS

We consider La substitutional doping by replacing one Ba in the unit cell with La. The vibrational frequencies for the doped system are included in Table III. Since there is no experimental data on Ba₀.₅La₀.₅HfN₂ we use relaxed lattice constants, which are smaller by almost 3% than the experimental lattice constants of BaHfN₂. The band structure of (BaLa)₀.₅HfN₂ is shown in Fig. 5 with fat bands for Hf and La. The nearly dispersionless La 4f states are located 1 eV above $E_{F}$ but have no clear impact on what we discuss in the following. There are two nearly cylindrical Fermi surfaces around $\Gamma$, one of which has Hf $5d_{xy}$ character and another has La $5d_{x^{2}-y^{2}}$ character; mixing may occur at or near crossing of the Fermi surfaces. The lowest conduction bands near $M$, primarily La $5d_{yz}$, $5d_{xz}$ in character (not shown as fat bands) are significantly lowered from the corresponding undoped Ba bands, creating two Fermi surfaces that are larger than anticipated from a rigid band picture using the BaHfN₂ bands. These surfaces have significant three dimensional character, but even at this (large) doping level they do not reach the top of the zone (the $A$ point). The lowering of the bands around $M$ is also seen within the virtual crystal approximation (where both Ba and La are replaced by an “average ion”) so we expect this to be a robust feature for doping by La. A small Fermi surface near $M$, of mainly La $5d_{z^{2}}$ character, arises near this level of doping.

The phonon frequencies for the metallic system are shown in Table III. Although the replacement of one Ba with La changes the symmetry, corresponding modes between the two systems can be identified by examining the scalar products of their eigenvectors. Several of the softer modes have slightly higher frequencies in (BaLa)₀.₅HfN₂ likely due to the decreased lattice constant of the metallic system. More interestingly, several of the high-frequency modes are renormal-

<table><caption>TABLE V. Lattice contribution (defined in Eq. (6)) to the macroscopic dielectric constants for selected phonons computed using fully relaxed geometry. Only three phonon modes contribute to the lattice polarizability in each direction.</caption>
<tbody><tr><th>Mode</th><th>$\omega_{TO}$ (cm⁻¹)</th><th>$4\pi P_{m,xx}$</th><th>$4\pi P_{m,zz}$</th></tr>
<tr><td>1–2</td><td>72</td><td>14.0</td><td></td></tr>
<tr><td>5</td><td>105</td><td></td><td>10.1</td></tr>
<tr><td>10–11</td><td>210</td><td>5.1</td><td></td></tr>
<tr><td>15–16</td><td>424</td><td>7.3</td><td></td></tr>
<tr><td>17</td><td>468</td><td></td><td>1.3</td></tr>
<tr><td>20</td><td>641</td><td></td><td>2.4</td></tr>
</tbody></table>

![](./images/811712687145746433_5.jpg)

FIG. 5. (Color online) Doped band structure showing La and Hf $5d$ bands. The amount of Hf $5d_{xy}$ and La $5d_{x^{2}-y^{2}}$ character is shown in the band structure by the weight of the points in the lines. The lowering of the $5d$ character due to replacement of Ba by La is substantial. The Fermi level lies at an energy of 0 eV.

ized in the metallic system. These high-frequency modes are dominated by motion of the N1 and N2 atoms.

## VII. SUMMARY
We have examined the electronic and vibrational structure of the ternary nitride $BaHfN_{2}$ within density-functional theory. We find that $BaHfN_{2}$ indeed has chemical and electronic similarities with high $T_{c}$ metallochloronitrides $MNCl$'s ($M$=Ti,Hf,Zr), so its candidacy as another high $T_{c}$ superconducting nitride is plausible. The basic electronic and vibrational properties of the undoped insulating phase provide a basis for an understanding of the behavior of $BaHfN_{2}$ upon doping.

The highly anisotropic Born effective charges for the N ions are not so unusual but the anisotropies that have an opposite sign for the two N sites are noteworthy. These distinctions suggest unusually anisotropic ionic bonding and electronic screening in $BaHfN_{2}$, so that in the absence of strong correlations and magnetism, electron-electron interactions might play a significant role in pairing in these layered nitrides when electron doped. The large BECs result in correspondingly large LO-TO splittings for some zone center phonons, as well as large dielectric constants that also imply unusual characteristics of electronic screening. We have provided an initial analysis of how the system is affected by doping and found that (at rather heavy doping) bands near $M$ are significantly lowered so that conduction would occur both in the Hf states near $\Gamma$ and in states near $M$ located in the BaN layer.

The MNCl compounds, which are impressive superconductors when doped, provide an interesting analogy to $BaHfN_{2}$, with its similar structural, electronic, and vibrational similarities but larger electronic screening. The mechanism of pairing in doped MnCl is the interesting question: according to standard and reliable linear response calculations, conventional coupling to phonons is substantially too weak. There is little magnetic behavior of interest, only some enhancement of the Pauli susceptibility as the critical doping level is approached from the metallic side. With these two "common" mechanisms apparently ruled out, the focus falls on some peculiar electronic behavior.

It is worth noting that, in the ionic semiconductor ZrNCl, it requires $x_{cr}$=0.06 carriers per transition-metal ion for conductivity to appear. This can be contrasted with the electron doping of the ionic semiconductor $SrTiO_{3}$, which becomes conducting for $x\sim10^{-4}$ carriers per transition-metal ion, and becomes superconducting at slightly higher doping but only at 0.4 K. The bands into which the electron carriers are doped seem similar, except for their difference in dimensionality (2D vs three dimensional). The other obvious difference is the dielectric constant, which in $SrTiO_{3}$ increases to greater than $10^{4}$ (though we know of no report for the MNCl compounds). The lack of conductivity in ZrNCl for $x<x_{cr}$ implies there are 'solvated' electrons in the ionic lattice, presumably inhibited from conduction by some polaronic character. The local charge carrier-charged ion interactions may extend into the superconducting regime because the screening length is larger than in more dense metals. Such interactions are not included in the conventional electron-phonon coupling theory.

One potentially important difference between $BaHfN_{2}$ and the MNCl compound is worth noting. From the point of view of vapor phase growth of the materials, MNCl contains two reactive, highly electronegative anions. There is relatively little experience in vapor growth (molecular beam epitaxy, pulsed laser deposition) of such materials. Since the appearance of the high $T_{c}$ cuprates, there has been a huge amount of experience accumulated, and expertise gained, in deposition of oxides with one electronegative anion but several cations. From this viewpoint, $BaHfN_{2}$—with one anion and two cations—is attractive for vapor phase growth, and hence for study and potential application of ultrathin superconducting layers.

## ACKNOWLEDGMENTS
We acknowledge helpful conversations with Quan Yin, particularly on unpublished work on TiNCl. We also acknowledge J. N. Eckstein for his useful comments in the early stages of this work. This work was supported by DOE/SciDAC under Grant DE-FC02-06ER25794 and by DOE/SciDAC-e Grant DE-FC02-06ER25777.

## APPENDIX: DESCRIPTION OF THE VIBRATIONAL MODES
Here we provide a brief characterization of the eigenvectors of all optical modes at $q$=0, which can be useful in interpreting optical data and in comparing with similar ionic semiconductors. The units are per centimeter.

$\omega$=72: Ba oscillating against other atoms in the $x$-$y$ plane. These two degenerate soft mode is largely responsible for the large static dielectric constant $\epsilon_{xx/yy}^{0}$.

$\omega$=82: this mode is primarily out-of-phase Ba vibrations in the $x$-$y$ plane.

$\omega$=105: Ba and N1 moving against each other with strong amplitude along the $z$ axis. Hf and N2 are in phase with each other oscillating weakly as compared to Ba and N1.

$\omega$=120: this mode is primarily out-of-phase Ba vibrations along the $z$ axis.

$\omega$=152: this mode has primarily N2 and Hf vibrations in the $x$-$y$ plane with N2 vibrating with a large amplitude as compared to Hf with Ba and N1 participating very weakly.

$\omega$=172: Hf and N2 vibrating along $z$, with Ba vibrating very weakly opposite to Hf.

$\omega$=210: these two mode are primarily in-phase N2 vibrations in the $x$-$y$ plane.

$\omega$=232: these two modes are primarily out-of-phase N2 vibrations in the $x$-$y$ plane.

$\omega$=341: this mode exhibits pure N1 vibrations along the $z$ axis, with nearest neighbor N1 atoms out of phase.

$\omega$=424: these two modes have primarily in-phase N1 vibrations in the $x$-$y$ plane with Hf moving weakly against N1 and Ba and N2 in the Ba-N2 moving weakly in phase with N1.

$\omega$=468: N1 vibrating with large amplitude in phase with Ba, N2 and out of phase with Hf along the $z$ axis and each of the other atoms participate very weakly.

$\omega$=623: these two modes are primarily out-of-phase N1 vibrations in the $x$-$y$ plane.

$\omega$=641: this mode is primarily in-phase N2 vibrations against other atoms along the $z$ axis. This mode dominates the ionic response in the $z$ direction, especially due to the large magnitude of BEC for N2: $Z_{zz}^{*}$(N2)=-4.58.

$\omega$=717: this mode is primarily out-of-phase N2 vibrations along the $z$ axis with very weak participation from Ba and Hf.

---

$^{1}$M. J. Geselbracht, T. J. Richardson, and A. M. Stacy, *Nature (London)* **345**, 324 (1990).

$^{2}$K. Takada, H. Sakurai, E. Takayama-Muromachi, F. Izumi, R. A. Dilanian, and T. Sasaki, *Nature (London)* **422**, 53 (2003).

$^{3}$M. A. Kastner, R. J. Birgeneau, G. Shirane, and Y. Endoh, *Rev. Mod. Phys.* **70**, 897 (1998).

$^{4}$S. Yamanaka, H. Kawaji, K.-i. Hotehama, and M. Ohashi, *Adv. Mater.* **8**, 771 (1996).

$^{5}$D. H. Gregory, M. G. Barker, P. P. Edwards, M. Slaski, and D. J. Siddons, *J. Solid State Chem.* **137**, 62 (1998).

$^{6}$Y. Taguchi, A. Kitora, and Y. Iwasa, *Phys. Rev. Lett.* **97**, 107001 (2006).

$^{7}$S. Yamanaka, T. Yasunaga, K. Yamaguchi, and M. Tagawa, *J. Mater. Chem.* **19**, 2573 (2009).

$^{8}$M. Ohashi, S. Yamanaka, and M. Hattori, *J. Ceram. Soc. Jpn. Int. Ed.* **97**, 1175 (1989).

$^{9}$C. Felser and R. Seshadri, *J. Mater. Chem.* **9**, 459 (1999).

$^{10}$I. Hase and Y. Nishihara, *Phys. Rev. B* **60**, 1573 (1999).

$^{11}$Y. Taguchi, T. Kawabata, T. Takano, A. Kitora, K. Kato, M. Takata, and Y. Iwasa, *Phys. Rev. B* **76**, 064508 (2007).

$^{12}$Y. Taguchi, M. Hisakabe, and Y. Iwasa, *Phys. Rev. Lett.* **94**, 217002 (2005).

$^{13}$R. Heid and K.-P. Bohnen, *Phys. Rev. B* **72**, 134527 (2005).

$^{14}$H. Tou, Y. Maniwa, T. Koiwasaki, and S. Yamanaka, *Phys. Rev. Lett.* **86**, 5775 (2001).

$^{15}$R. Weht, A. Filippetti, and W. E. Pickett, *Europhys. Lett.* **48**, 320 (1999).

$^{16}$Y. Kasahara, T. Kishiume, T. Takano, K. Kobayashi, E. Matsuoka, H. Onodera, K. Kuroki, Y. Taguchi, and Y. Iwasa, *Phys. Rev. Lett.* **103**, 077004 (2009).

$^{17}$A. Bill, H. Morawitz, and V. Z. Kresin, *Phys. Rev. B* **66**, 100501 (2002).

$^{18}$A. Bill, H. Morawitz, and V. Z. Kresin, *Phys. Rev. B* **68**, 144519 (2003).

$^{19}$C. Hartwigsen, S. Goedecker, and J. Hutter, *Phys. Rev. B* **58**, 3641 (1998).

$^{20}$M. Krack, *Theor. Chim. Acta* **114**, 145 (2005).

$^{21}$N. Troullier and J. L. Martins, *Phys. Rev. B* **43**, 1993 (1991).

$^{22}$X. Gonze *et al.*, *Comput. Mater. Sci.* **25**, 478 (2002).

$^{23}$J. P. Perdew, K. Burke, and M. Ernzerhof, *Phys. Rev. Lett.* **77**, 3865 (1996).

$^{24}$H. J. Monkhorst and J. D. Pack, *Phys. Rev. B* **13**, 5188 (1976).

$^{25}$K. Koepernik and H. Eschrig, *Phys. Rev. B* **59**, 1743 (1999).

$^{26}$X. Gonze and C. Lee, *Phys. Rev. B* **55**, 10355 (1997).

$^{27}$M. Fuchs and M. Scheffler, *Comput. Phys. Commun.* **119**, 67 (1999).

$^{28}$J. P. Perdew and A. Zunger, *Phys. Rev. B* **23**, 5048 (1981).

$^{29}$The ELK FP-LAPW Code, http://elk.sourceforge.net/

$^{30}$Q. Yin, E. R. Ylvisaker, and W. E. Pickett (unpublished).

$^{31}$K. Kuroki, *Phys. Rev. B* **81**, 104502 (2010).

$^{32}$Z. Li, J. Yang, J. G. Hou, and Q. Zhu, *Phys. Rev. B* **70**, 144518 (2004).

$^{33}$R. Vali, *Solid State Commun.* **147**, 1 (2008).

$^{34}$E. R. Ylvisaker, Q. Yin, and W. E. Pickett (unpublished).

$^{35}$M. Xu, S. Wang, G. Yin, J. Li, Y. Zheng, L. Chen, and Y. Jia, *Appl. Phys. Lett.* **89**, 151908 (2006).

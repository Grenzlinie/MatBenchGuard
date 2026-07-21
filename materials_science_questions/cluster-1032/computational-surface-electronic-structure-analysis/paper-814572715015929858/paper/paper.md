# Atomic structure and electronic properties of the two-dimensional (Au,Al)/Si(111)2 × 2 compound

D. V. Gruznev, $^{1,2}$ L. V. Bondarenko, $^{1,2}$ A. V. Matetskiy, $^{1,2}$ A. Y. Tupchaya, $^{1,2}$ E. N. Chukurov, $^{1}$ C. R. Hsing, $^{3}$ C. M. Wei, $^{3}$ S. V. Eremeev, $^{4,5}$ A. V. Zotov, $^{1,2,6}$ and A. A. Saranin $^{1,2,*}$

$^{1}$Institute of Automation and Control Processes FEB RAS, 5 Radio Street, 690041 Vladivostok, Russia
$^{2}$School of Natural Sciences, Far Eastern Federal University, 690950 Vladivostok, Russia
$^{3}$Institute of Atomic and Molecular Sciences, Academia Sinica, P.O. Box 23-166 Taipei, Taiwan
$^{4}$Institute of Strength Physics and Materials Science, 634021 Tomsk, Russia
$^{5}$Tomsk State University, 634050 Tomsk, Russia
$^{6}$Department of Electronics, Vladivostok State University of Economics and Service, 690600 Vladivostok, Russia

(Received 1 September 2015; revised manuscript received 14 October 2015; published 7 December 2015)

A combination of scanning tunneling microscopy, angle-resolved photoelectron spectroscopy, *ab initio* random structure searching, and density functional theory electronic structure calculations was applied to elucidate the atomic arrangement and electron band structure of the (Au,Al)/Si(111)2 × 2 two-dimensional compound formed upon Al deposition onto the mixed $5×2/\sqrt{3}×\sqrt{3}$ Au/Si(111) surface. It was found that the most stable 2 × 2-(Au, Al) compound incorporates four Au atoms, three Al atoms, and two Si atoms per 2 × 2 unit cell. Its atomic arrangement can be visualized as an array of meandering Au atomic chains with two-thirds of the Al atoms incorporated into the chains and one-third of the Al atoms interconnecting the chains. The compound is metallic and its electronic properties can be controlled by appropriate Al dosing since energetic location of the bands varies by $\sim$0.5 eV during increasing of Al contents. The 2 × 2-(Au, Al) structure appears to be lacking the $C_{3v}$ symmetry typical for the hexagonal lattices. The consequence of the peculiar atomic structure of the two-dimensional alloy is spin splitting of the metallic states, which should lead to anisotropy of the current-induced in-plane spin polarization.

DOI: 10.1103/PhysRevB.92.245407

PACS number(s): 68.43.Hn, 68.37.Ef, 68.43.Bc

## I. INTRODUCTION

The adsorption of metals in monolayer and submonolayer amounts on semiconductor (e.g., silicon) substrates forming ordered two-dimensional (2D) structures has attracted con- siderable attention from researchers due to the abundance of resulting surface reconstructions exhibiting a variety of interesting structural and electronic properties. Such adsorp- tion structures are interesting in respect to the creation of metallic surface states on semiconductors because they are the electronic equivalent of a two-dimensional electron gas. Of special interest is the Rashba spin-split two-dimensional electron gas [1,2] which arises owing to the spin-orbit interac- tion (SOI) and spin-orbit-induced in-plane modification of the wave functions [3]. Spin splitting of a spin-degenerate electron gas has an advantage to efficiently manipulate the spin freedom of electrons without the requirement of externally applied magnetic field [4]. This is considered to be a key ingredient for promising spin-orbitronics applications [5] since the spin splitting of the 2D states underlies many phenomena, including spin Hall effect [6–8], low dissipation spin current [9–11], and charge-to-spin conversion (Rashba-Edelstein effect) [12–15].

Since SOI is proportional to the square of the charge of a nu- cleus, the biggest Rashba splitting was observed at surfaces of heavy-element metals such as Au(111) [16] and Bi(111) [17], as well as in high-$Z$ adsorbed structures on semiconductor surfaces. The large Rashba-type spin splitting of surface states has been found at the Bi/Si(111) [18,19], Tl/Si(111) [20,21], Pt/Si(110) [22], Pb/Ge(111) [23], and Au/Ge(111) [24] sur- faces. It should be noted that the spin splitting observed in these systems can be called Rashba splitting only simplistically be- cause the spin textures, caused by the interplay of SOI and sur- face symmetry, often differ from those predicted by the Rashba model and demonstrate the behavior similar to that of the Dres- selhaus type [19,20,24,25]. Moreover, a combined effect of Rashba and Dresselhaus SOI with different or equal coupling constants may lead to a rich variety of phenomena (see, e.g., Refs. [26–29]).

One of the promising directions within this research field is associated with going beyond the case of a single atomic species, i.e., studying phenomena trigged by the coadsorption of two or more species. Taking into account the large number of possible combinations of atomic species, the number of potentially advanced multiadsorbate systems could be quite large. Active investigations of coadsorption of metals on silicon leading to the formation of the ordered compound reconstructions have been investigated starting approximately in the early 1990s and continuing today [25,30–51]. In the early works, techniques such as low-energy electron diffraction (LEED), reflection high-energy electron diffrac- tion, Auger-electron spectroscopy (AES), and photoelectron spectroscopy were commonly used and the main goals of the investigations were the characterization of the phase formation processes, finding new reconstructions, and establishing their periodicity and plausible composition. Currently, applying advanced techniques, such as scanning tunneling microscopy (STM) with atomic resolution and angle-resolved photoelec- tron spectroscopy (ARPES) accompanied by comprehensive density functional theory (DFT) calculations, has made it possible to accurately determine the exact atomic arrangement and electronic band structure of the 2D compounds. Very recent studies of two-dimensional Sn-Ag [48], Bi-Na [25],

*saranin@iacp.dvo.ru

1098-0121/2015/92(24)/245407(7)

245407-1

©2015 American Physical Society

Tl-Pb [25], and Tl-Sn [50] compounds on Si(111) provide vivid examples. These studies, in particular, have demonstrated that such systems can possess remarkable properties. For example, Sn-Ag and Tl-Sn are characterized by extremely high electron velocity at the Fermi level of $\sim8\times10^5$ m/s, which is comparable to the value reported for graphene. The Bi-Na, Tl-Pb, and Tl-Sn compounds demonstrate a giant Rashba-type spin splitting of metallic surface-state bands with momentum splitting $\Delta k_{\parallel}\sim0.04-0.05\mathring{\mathrm{A}}^{-1}$ and energy splitting $\Delta E_{\mathrm{F}}\sim150-250$ meV. In addition, (Tl, Pb)/Si(111) has been recently found to exhibit superconducting properties below 2.25 K [52], thus extending the list of the known one-atomic-layer superconductors, which is actually very short and includes, so far, only the In and Pb atomic layers on Si(111) [53,54].

Following the trend for exploring 2D compounds on silicon, we revisited the (Au, Al)/Si(111)$2\times2$ reconstruction which was first detected in the LEED-AES study of Au and Al coadsorption on Si(111) [33]. In the present study, we used a combination of STM and ARPES techniques, as well as DFT calculations [in particular, for *ab initio* random structure search (AIRSS)], to characterize in detail the structural and electronic properties of the (Au, Al)/Si(111)$2\times2$ reconstruction.

## II. EXPERIMENTAL AND CALCULATION DETAILS

Our experiments were performed with an Omicron Multi-probe system equipped with STM and ARPES and operating in an ultrahigh vacuum $(\sim2.0\times10^{-10}$ Torr). Atomically clean Si(111)$7\times7$ surfaces were prepared *in situ* by flashing to $1280^{\circ}\mathrm{C}$ after the samples were first outgassed at $600^{\circ}\mathrm{C}$ for several hours. Gold and aluminum were deposited from tungsten filament and basket, respectively. STM images were acquired in a constant-current mode with mechanically cut PtIr tips used as STM probes after annealing in vacuum. ARPES measurements were conducted using a VG Scienta R3000 electron analyzer and high-flux He discharge lamp $(h\nu=21.2$ eV) with a toroidal-grating monochromator as a light source.

Density functional theory calculations were performed using the projector augmented-wave (PAW) method [55,56], as implemented in the Vienna *Ab initio* Simulation Package (VASP) [57,58]. Relativistic effects, including spin-orbit interaction, were taken into account. In order to find the most stable structures of each (Au, Al)/Si(111) configuration with different Au, Al, and Si coverages, we used the *ab initio* random structure searching (AIRSS) method [59], which has already proven to be an efficient and effective method for exploring equilibrium structures of solids [60], point defects [61], surfaces [50,62,63], and clusters [64]. The (Au, Al)/Si(111)$2\times2$ supercell geometry was simulated by a repeating slab of five Si bilayers and a vacuum region of $\sim15\mathring{\mathrm{A}}$. Si atoms in the bottom two bilayers were fixed at their bulk positions, the top three bilayers were allowed to fully relax, and the dangling bonds on the bottom surface were saturated by hydrogen atoms. The kinetic cutoff energy was 400 eV, and a Monkhorst-Pack $6\times6\times1$ $k$-point mesh was used to sample the surface Brillouin zone within AIRSS. The geometry optimization was performed until the residual force was smaller than $10\ \mathrm{meV/\mathring{A}}$. For the band structure calculation on the stable (Au, Al)/Si(111) structures, the $k$-mesh and substrate thickness were increased up to $9\times9\times1$ and six Si bilayers, respectively.

![](./images/814572715015929858_1.jpg)

FIG. 1. (Color online) Formation of the $2\times2$-Au, Al layer when the $\sqrt{3}\times\sqrt{3}$-Au phase prevails at the initial Au/Si(111) surface. (a) $1000\times750\mathring{\mathrm{A}}^{2}$ and (b) $500\times370\mathring{\mathrm{A}}^{2}$ STM images of the $2\times2$-Au, Al reconstruction at the stage when the $2\times2$-Au, Al domains merge together. (c) $500\times370\mathring{\mathrm{A}}^{2}$ STM image of the $2\times2$-Au, Al surface at the final growth stage. (d) LEED pattern ($E_{p}=46$ eV) from the $2\times2$-Au, Al surface.

## III. RESULTS AND DISCUSSION

The (Au, Al)/Si(111)$2\times2$ surface reconstruction was prepared by depositing Al onto the surface which represented a mixture of $\sqrt{3}\times\sqrt{3}$-Au and $5\times2$-Au reconstructions held at $\sim600^{\circ}\mathrm{C}$. The $\sqrt{3}\times\sqrt{3}$-Au and $5\times2$-Au reconstructions were preliminarily prepared at the same temperature of $\sim600^{\circ}\mathrm{C}$. Remember that an ideal Si(111)$\sqrt{3}\times\sqrt{3}$-Au phase incorporates 1.0 ML of Au [65] [1 ML (monolayer) $=7.8\times10^{14}\mathrm{cm}^{-2}$], while the real Si(111)$\sqrt{3}\times\sqrt{3}$-Au surface is characterized by a somewhat higher Au coverage due to the presence of heavy domain walls [66]. According to very recent results, the Si(111)$5\times2$-Au reconstruction contains 0.7 ML of Au [67–70].

The patches of the $2\times2$-Au, Al reconstructions appear randomly at the surface and grow in size with Al deposition. At the stage when the $2\times2$-Au, Al domains merge together to cover the whole surface, the specific feature of the $2\times2$-Au, Al layer is the presence of the numerous dark troughs. When the $\sqrt{3}\times\sqrt{3}$-Au phase prevails at the initial Au/Si(111) surface, most of the long troughs are oriented along the $\langle1\overline{2}1\rangle$, while among the short troughs, those oriented along the $\langle10\overline{1}\rangle$ directions also present in addition to the $\langle1\overline{2}1\rangle$-oriented troughs [Figs. 1(a) and 1(b)]. Remember that the $\langle10\overline{1}\rangle$ and $\langle1\overline{2}1\rangle$ directions correspond to the main crystallographic Si(111) directions and $\sqrt{3}$-period directions, respectively. It is worth noting that the troughs are not domain walls since the $2\times2$ lattices from both sides of a given trough are in phase. This is especially apparent in the regions where the troughs are broken into separate bars. The density of troughs decreases with Al

![](./images/814572715015929858_2.jpg)

FIG. 2. (Color online) (a) $7400 × 5600\,\mathrm{\mathring{A}}^2$ and (b) $340 × 250\,\mathrm{\mathring{A}}^2$ STM images of the $2 × 2$-(Au, Al) layer formed when the $5 × 2$-Au phase prevails at the initial Au/Si(111) surface. The $2 × 2$ unit cell is outlined in (b).

deposition and eventually the $2 × 2$ surface that is almost free of troughs is formed [Fig. 1(c)]. Thus, one can conclude that the development of troughs is associated with an Al deficit.

When the $5 × 2$-Au phase prevails at the initial Au/Si(111) surface, the ribbonlike structure develops with troughs oriented exclusively along the $\langle 10\overline{1}\rangle$ directions (Fig. 2). They remain at prolonged Al deposition. Meanwhile, the patches of the Au-free $\text{Si(111)}\sqrt{3} × \sqrt{3}$-Al phase appear, indicating that preservation of the troughs in this case is associated with the Au deficit.

Figure 3 shows dual-polarity ($\pm 0.8\,\text{V}$) high-resolution STM images of the $\text{Si(111)}2 × 2$-(Au, Al) surface reconstruction. One can see that at both polarities, the structure shows up basically as a hexagonal array with a single round protrusion per $2 × 2$ unit cell. This is especially true for the empty-state STM images where all protrusions have the same round shape, albeit possibly differing in brightness. The filled-state STM images reveal a more apparent variation in the appearance of the protrusions. Namely, in addition to varying brightness, in many cases the bridgelike features can be noticed in between neighboring protrusions.

ARPES observations revealed that the characteristic band structure of the $2 × 2$-(Au, Al) layer already develops at the stage when the Au-Al compound surface contains numerous troughs [Fig. 4(a)]. The most prominent features in the ARPES spectrum lie at $\approx-1.65\,\text{eV}$ and at $\approx-0.65\,\text{eV}$ (denoted by red and blue arrows at the $\bar{\Gamma}_0$ and $\bar{\Gamma}_1$ points, respectively, in Fig. 4). However, all spectral features become more distinct only with further Al dosing [Fig. 4(b)]. Simultaneously, all of the bands go up to the lower electron binding energies [Fig. 4(c)]. The lower sharp feature (shown by red) shifts up by $0.35\,\text{eV}$, and the upper spectral feature (shown by blue) shifts up by $0.53\,\text{eV}$ becoming more intense. Note that as revealed by the calculations (to be shown below), the latter band has a surface origin, but overlaps with the projected bulk bands, and hence it is a resonant band.

In order to establish an atomic structure of the $\text{Si(111)}2 ×$ 2-(Au, Al) compound reconstruction, we applied an AIRSS technique for a set of reasonable compositions. As a starting point, we considered the surface structure which incorporates four Au atoms, four Si atoms, and one Al atom per $2 × 2$ unit cell [i.e., 1.0 ML of Au and 1.0 ML of Si inherited from the initial Au/Si(111) surface, plus 0.25 ML of adsorbed Al] placed above a nonreconstructed Si(111) bilayered surface. The lowest-energy configuration found for such a composition is shown in Fig. 5(a). The basic element of the reconstruction is a rectangle built of four Au atoms with an Al atom in its center. It is hatched in yellow in Fig. 5(a). This rectangular unit is surrounded by Si adatoms from the short sides and by Si dimers from the long sides. In the simulated STM images, the rectangular unit shows up as a single, almost round protrusion seen at both bias polarities [Fig. 5(d), left panel]. One can notice that this unit (and, consequently, the basis of the crystal structure as well) is lacking the $C_{3v}$ symmetry typical for hexagonal structures. Note that the surface structure can be thought of also as consisting of meandering Au atomic chains running along the $[1\overline{1}0]$ direction and interconnected through Al atoms.

Taking into account that the $2 × 2$-(Au, Al) compound grows from a mixture of $\sqrt{3} × \sqrt{3}$-Au and $5 × 2$-Au (of which the latter contains 0.7 ML Au), one can expect that the compound might contain less than 1.0 ML Au. To check this possibility, we performed AIRSS calculations for the structures containing three Au atoms per $2 × 2$ unit cell. However, the corresponding lowest-energy configuration

![](./images/814572715015929858_3.jpg)

FIG. 3. (Color online) Dual-polarity (a) $\pm 0.6\,\text{V}$, (b) $\pm 0.8\,\text{V}$, and (c) $\pm 1.0\,\text{V}$ $110 × 110\,\mathrm{\mathring{A}}^2$ STM images of the $2 × 2$-(Au, Al) layer ribbons. Images show almost the same surface area where the characteristic defect is indicated by a star to guide the eye. The $2 × 2$ unit cell is outlined in (c).

![](./images/814572715015929858_4.jpg)

FIG. 4. (Color online) ARPES data illustrating evolution of the electron band structure in the course of $2 × 2$-(Au, Al) layer formation. ARPES spectra at the (a) intermediate and (b) final stages of the $2 × 2$-(Au, Al) layer formation, i.e., after dosing the Au/Si(111) surface with 0.5 and 0.9 ML of Al, respectively. (c) Energy shifting of the bands as a function of Al dose. Open blue and red circles and lines in (c) correspond to the top of the bands, indicated by blue and red arrows, respectively, in (a) and (b).

![](./images/814572715015929858_5.jpg)

FIG. 5. (Color online) The lowest-energy atomic configurations determined with AIRSS for the $2\times2$-(Au, Al) compounds containing (a) one, (b) two, and (c) three Al atoms per $2\times2$ unit cell. Au atoms are shown by yellow circles, Al atoms are shown by red circles, and Si atoms are shown by gray and white circles. Basic rectangular units are hatched in yellow and meandering Au atomic chains are highlighted by red broken lines in (a). (d) Simulated dual-polarity ($\pm0.8$ V) STM images corresponding to each of the above structures. The $2\times2$ unit cells are outlined and their location in the simulated STM images coincides with that in the model structures.

appears to be 0.73 eV less energetically favorable than that with four Au atoms, indicating that the $2\times2$-(Au, In) compound does plausibly contain 1.0 ML of Au.

Adding Al to the basic (Au, Al)/Si(111)$2\times2$ configuration shown in Fig. 5(a) was found to decrease formation energy only in the cases when added Al atoms substitute Si atoms in the dimers. Substitution of a single Si atom nearest to the rectangular unit (i.e., incorporation of two Al atoms per $2\times2$ unit cell) [Fig. 5(b)] lowers the formation energy by 0.68 eV. When the nearest Si atoms from both sides of the rectangular unit are substituted by Al atoms (i.e., three Al atoms per $2\times2$ unit cell are incorporated) [Fig. 5(c)], the formation energy becomes still lower by 0.49 eV. One can notice that additional Al atoms are incorporated within the meandering Au atomic chains. Simulation of STM images [Fig. 5(d)] for the above “Al-rich” configurations demonstrates that the round shape of the protrusions in the empty-state images are preserved, while in the filled-state images, bridgelike features appear whose counterparts can be seen in the experimental filled-state STM images (Fig. 3).

The evolution of the calculated electron band structure of the $2\times2$-(Au, Al) compound in the course of increasing Al contents is illustrated in Fig. 6. By comparing the calculated spectra with the ARPES-derived ones shown in Fig. 4, one can conclude that the $\bar{\Gamma}$ parabolic spectral feature at higher binding energy should be associated with the edge of the region of high density of the bulk states (dense net of the bulk projected states; see red arrow in Fig. 6), while the feature at smaller binding energy corresponds to the calculated $\bar{\Gamma}$ resonant state in the bulk-projected area (blue arrow in Fig. 6). One can also see that the most apparent trend is the shifting of all of the bands up to the lower electron binding energies, in agreement with the ARPES observations (Fig. 4). However, changing the Al contents from one to two atoms per $2\times2$ unit cell results in very small energy shifts, i.e., $\sim$0.15 eV for the resonant band and almost nothing for the bulk bands [Figs. 6(a) and 6(b)], and the most essential change here is the appearance of the metallic band, hence changing the semiconducting properties of the surface to the metallic ones. When the third Al atom is added [Fig. 6(c)], the considerable energy shifts of about 0.4–0.5 eV are observed. One can see that the effect of changing Si atoms for Al is twofold, namely, the surface bands are modified and all of the bands go up to the lower electron binding energies. The latter effect is associated with the fact that replacing one Si atom for Al means decreasing the number of electrons by one per $2\times2$ unit cell, which naturally lowers the Fermi level. This can also be visualized as a shifting up of the bands with respect to the Fermi level. In conclusion, by comparing calculation results (Fig. 6) with the experimental ARPES data (Fig. 4), one can see a good resemblance both in the Al dose at which energy shifting takes place and the order of shift values.

![](./images/814572715015929858_6.jpg)

FIG. 6. (Color online) Calculated band structures for the $2\times2$-(Au, Al) compounds incorporating (a) one, (b) two, and (c) three Al atoms per $2\times2$ unit cell. The characteristic Si bulk band is outlined and marked by a red arrow; the surface resonant band is marked by a blue arrow.

As mentioned above, the $2\times2$-(Au, Al) 2D compound is lacking the $C_{3v}$ symmetry of the Si(111) substrate and possesses $C_{2v}$ symmetry. Thus, the [1$\bar{1}$0] vector of the hexagonal $2\times2$ cell is directed along the meandering Au atomic chain, while the [$\bar{1}$01] and [01$\bar{1}$] vectors make an angle of $\pm120^\circ$ with this chain. This directional variance is naturally reflected in the difference of the band dispersions along different directions, as illustrated by the calculated band structures shown in Figs. 7(a) and 7(b) and Figs. 7(c) and 7(d). Due to occurrence of three rotational domains of the $2\times2$-(Au, Al) structure on the real surface, the experimental ARPES spectrum has to combine together the band dispersions for different (inequivalent) directions. Figure 7(e) presents the sum of the calculated band dispersions shown in Figs. 7(a) and 7(b) superposed with the experimental ARPES spectrum. For a better visualization, Fig. 7(f) shows the experimental momentum distribution curve (MDC) at the Fermi level, with green tics indicating the positions where the calculated metallic bands cross the Fermi level. One can see clear counterparts of the principal spectral features in the calculated band structures, and vice versa. However, one should bare in mind that merged

![](./images/814572715015929858_7.jpg)

FIG. 7. (Color online) Calculations of the electron band structure of the $2\times2$-($\text{Au}$, $\text{Al}$) compound which take into account the lack of $C_{3v}$ symmetry of the reconstruction. Sketches of reciprocal space geometry with boundaries of the $2\times2$ surface Brillouin zones (SBZs) is shown in the insets. The band structure is calculated for the case when the (a) $\bar{\Gamma}-\bar{\text{M}}$ direction is along the $[11\bar{2}]$ and (b) $\bar{\Gamma}-\bar{\text{K}}$ direction is along the $[1\bar{1}0]$, i.e., perpendicular and parallel to the gold atoms chain, respectively. The band structure is also calculated for the two almost equivalent cases when the (c) $\bar{\Gamma}-\bar{\text{M}}$ direction is along the $[2\bar{1}\bar{1}]$ or $[\bar{1}2\bar{1}]$ and (d) $\bar{\Gamma}-\bar{\text{K}}$ direction is along the $[10\bar{1}]$ or $[01\bar{1}]$. To adopt a proper correspondence to the experimental spectrum, the Fermi level in the calculated band structures is shifted up by 200 meV. In the calculated band structures, the size of the circles corresponds to the strength of the surface character summed over all orbitals at a particular $k_{\parallel}$. The red and blue colors of the circles mark opposite in-plane spin directions. (e) Sum of the calculated band structures of the $2\times2$-($\text{Au}$, $\text{Al}$) layer superposed on the experimental ARPES spectrum. The piece of the spectrum in the $\bar{\Gamma}-\bar{\text{K}}$ direction (outlined by the yellow dashed frame) is extracted from the data set acquired spectra from different domains which are limited in size and are not perfectly homogeneous [as evidenced by STM (see Fig. 3)] lead to smeared spectral features in the ARPES spectrum that, in turn, hamper experimental evaluation of more fine features, e.g., spin splitting. As for calculations, they yield maximal spin splitting of the metallic band near the Fermi level along the $\bar{\Gamma}-\bar{\text{M}}$ direction, which only slightly depends on the crystallographic orientation: it is characterized by momentum splitting $\Delta k_{\parallel}=0.037$ $\text{\AA}^{-1}$ in all directions and energy splitting $\Delta E_{\text{F}}=197$ meV in the $[11\bar{2}]$ direction and $\Delta E_{\text{F}}=177$ meV in the $[2\bar{1}\bar{1}]$ and $[\bar{1}2\bar{1}]$ directions. The Fermi-level position adopted here is the same as that in the experiment. It should be pointed out that it lies just below the $\bar{\Gamma}-\bar{\text{K}}$ ($[1\bar{1}0]$) crossing of the Rashba branches, where inner and outer branches change the sign of the in-plane spin helicity [Fig. 7(b)].

Such a surface band structure results in a remarkable 2D Fermi surface and spin texture [Fig. 8(a)] with almost antiparallel orientation of the spin along the $[1\bar{1}0]$ direction that resembles those predicted [26] and found in zinc-blende semiconductor quantum wells [27,28] and recently on the $\text{ZnO}(10\bar{1}0)$ surface [71]. In such systems with $C_{2v}$ symmetry, owing to the equal Rashba and Dresselhaus coupling constants, the SOI is linearly dependent on the electron momentum in specific directions, providing the one-dimensional orientation of the spin texture and causing suppression of the spin relaxation or existence of so-called persistent spin helix.

The spin alignment is almost in plane (the $S_{z}$ component is rather small) with the exception of points lying in the ($-\bar{\text{K}}$)-$\bar{\Gamma}-\bar{\text{K}}$ ($[1\bar{1}0]$) direction, where the spin has an out-of-plane orientation, which is positive and negative for different branches. The contours degenerate in the $\bar{\Gamma}-\bar{\text{K}}$ direction at the calculated Fermi-level position at $\approx0.35$ eV and split away from this energy, while the spin texture keeps the preferred alignment along the $[1\bar{1}0]$ direction. Such an alignment of the spin texture should cause significant anisotropy in the Rashba-Edelstein effect. In the spin-split 2D electron gas, the electric field applied along an in-plane direction induces the spin polarization in the perpendicular in-plane direction and this effect is isotropic for systems with isotropic Rashba splitting. In the $2\times2$-($\text{Au}$, $\text{Al}$) 2D alloy where spins are aligned preferably along the meandering gold chains, the electric field applied along the $[11\bar{2}]$ direction (i.e., perpendicular to the chains) should result in the largest induced spin polarization, while the effect should be almost absent in the $[1\bar{1}0]$ direction, i.e., along the chain.

Figure 8(d) shows experimental Fermi map acquired in the second SBZ. For comparison, Fig. 8(e) shows three calculated $120^{\circ}$ rotated Fermi contours. One can see that they are in good agreement. Though the experimental Fermi map is smeared in the second SBZ [see Fig. 8(d)] where the surface spectral features show up more pronounced. (f) Experimental MDC taken at the Fermi level with green tics indicating the location of the calculated bands. Broad maxima at the $\bar{\Gamma}$ and $\bar{\text{K}}$ points are repercussions of the lower intense spectral features.

![](./images/814572715015929858_8.jpg)

FIG. 8. (Color online) Calculated constant-energy maps (left column) and spin components $S_x$, $S_y$, and $S_z$ vs the azimuthal angle (right column) at (a) experimental Fermi level, (b) 150 meV above Fermi level, and (c) 300 meV above Fermi level [see corresponding lines in Fig. 7(b)]. (d) ARPES Fermi map acquired in the second SBZ. (e) Three calculated $120^\circ$ rotated Fermi contours with the one having the greatest intensity as in (d) due to prevailing domains of the corresponding orientation.

owing to the presence of different rotational domains of the $2\times2$-(Au, Al) structure, spin-split zones can be resolved in some directions. The Fermi map shows the noticeable $k_x/k_y$ asymmetry, which indicates that one domain orientation prevails over the other two, and thus the anisotropy in the Rashba-Edelstein effect can be observed.

## IV. CONCLUSION

In conclusion, we elucidated the atomic structure and electronic properties of the ordered two-dimensional Au-Al compound grown on Si(111). The most stable compound was found to incorporate four Au atoms, three Al atoms, and two Si atoms per $2\times2$ unit cell. Its basic element is a rectangular unit built of four Au atoms with an Al atom in its center and two Al atoms adjacent to the short sides of the rectangular unit. The structure can also be thought of as consisting of meandering Au atomic chains aligned along the $[1\overline{1}0]$ directions, where two Al atoms per $2\times2$ unit cell occupy sites inside the chains and one Al atom resides in between the chains. This structure is lacking $C_{3v}$ symmetry typical for hexagonal lattices. From the electronic viewpoint, the compound exhibits metallic properties. Drastic changes in the location of the electron bands during increasing Al contents in the compound provide a principal possibility to control electronic properties of the compound by depositing an appropriate amount of Al. Calculations reveal that its surface-state bands are spin split and the spin texture demonstrates unusual spin alignment, where spins are directed along the gold chain direction that should result in significant anisotropy in the Rashba-Edelstein effect.

## ACKNOWLEDGMENTS

The works utilizing ARPES measurements were supported by the Russian Science Foundation (Grant No. 14-12-00479). STM experiments were supported by Russia President Grant No. MK-6592.2015.2 for young researchers. Calculations were supported in part by the National Science Council of Taiwan through Grant No. NSC 103-2923-M-001-005-MY3 and by the RAS “Far East” Program, Project No. 0262-2015-0056. We thank E. E. Krasovskii for fruitful discussions.

[1] Y. Bychkov and E. Rashba, JETP Lett. 39, 78 (1984).
[2] Y. A. Bychkov and E. I. Rashba, J. Phys. C 17, 6039 (1984).
[3] E. E. Krasovskii, Phys. Rev. B 90, 115434 (2014).
[4] D. D. Awschalom and M. E. Flatte, Nat. Phys. 3, 153 (2007).
[5] A. Manchon, H. C. Koo, J. Nitta, S. M. Frolov, and R. A. Duine, Nat. Mater. 14, 871 (2015).
[6] J. E. Hirsch, Phys. Rev. Lett. 83, 1834 (1999).
[7] S. Zhang, Phys. Rev. Lett. 85, 393 (2000).
[8] J. Wunderlich, B. Kaestner, J. Sinova, and T. Jungwirth, Phys. Rev. Lett. 94, 047204 (2005).
[9] S. Murakami, N. Nagaosa, and S.-C. Zhang, Science 301, 1348 (2003).
[10] S. O. Valenzuela and M. Tinkham, Nature (London) 442, 176 (2006).

[11] X.-D. Cui, S.-Q. Shen, J. Li, Y. Ji, W. Ge, and F.-C. Zhang, Appl. Phys. Lett. 90, 242115 (2007).
[12] A. Aronov, Y. B. Lyanda-Geller, and G. Pikus, JETP 73, 537 (1991).
[13] V. M. Edelstein, Phys. Rev. Lett. 75, 2004 (1995).
[14] Y. K. Kato, R. C. Myers, A. C. Gossard, and D. D. Awschalom, Science 306, 1910 (2004).
[15] V. Sih, R. C. Myers, Y. K. Kato, W. H. Lau, A. C. Gossard, and D. D. Awschalom, Nat. Phys. 1, 31 (2005).
[16] S. LaShell, B. A. McDougall, and E. Jensen, Phys. Rev. Lett. 77, 3419 (1996).
[17] Y. M. Koroteev, G. Bihlmayer, J. E. Gayone, E. V. Chulkov, S. Blügel, P. M. Echenique, and P. Hofmann, Phys. Rev. Lett. 93, 046403 (2004).

[18] I. Gierz, T. Suzuki, E. Frantzeskakis, S. Pons, S. Ostanin, A. Ernst, J. Henk, M. Grioni, K. Kern, and C. R. Ast, *Phys. Rev. Lett.* **103**, 046803 (2009).

[19] K. Sakamoto, H. Kakuta, K. Sugawara, K. Miyamoto, A. Kimura, T. Kuzumaki, N. Ueno, E. Annese, J. Fujii, A. Kodama *et al.*, *Phys. Rev. Lett.* **103**, 156801 (2009).

[20] K. Sakamoto, T. Oda, A. Kimura, K. Miyamoto, M. Tsujikawa, A. Imai, N. Ueno, H. Namatame, M. Taniguchi, P. E. J. Eriksson *et al.*, *Phys. Rev. Lett.* **102**, 096805 (2009).

[21] S. D. Stolwijk, A. B. Schmidt, M. Donath, K. Sakamoto, and P. Krüger, *Phys. Rev. Lett.* **111**, 176402 (2013).

[22] J. Park, S. W. Jung, M. C. Jung, H. Yamane, N. Kosugi, and H. W. Yeom, *Phys. Rev. Lett.* **110**, 036801 (2013).

[23] K. Yaji, Y. Ohtsubo, S. Hatta, H. Okuyama, K. Miyamoto, T. Okuda, A. Kimura, H. Namatame, M. Taniguchi, and T. Aruga, *Nat. Commun.* **1**, 17 (2010).

[24] P. Höpfner, J. Schäfer, A. Fleszar, J. H. Dil, B. Slomski, F. Meier, C. Loho, C. Blumenstein, L. Patthey, W. Hanke *et al.*, *Phys. Rev. Lett.* **108**, 186801 (2012).

[25] D. V. Gruznev, L. V. Bondarenko, A. V. Matetskiy, A. A. Yakovlev, A. Y. Tupchaya, S. V. Eremeev, E. V. Chulkov, J.-P. Chou, C.-M. Wei, M.-Y. Lai *et al.*, *Sci. Rep.* **4**, 4742 (2014).

[26] B. A. Bernevig, J. Orenstein, and S.-C. Zhang, *Phys. Rev. Lett.* **97**, 236601 (2006).

[27] J. D. Koralek, C. P. Weber, J. Orenstein, B. A. Bernevig, S.-C. Zhang, S. Mack, and D. D. Awschalom, *Nature (London)* **458**, 610 (2009).

[28] M. P. Walser, C. Reichl, W. Wegscheider, and G. Salis, *Nat. Phys.* **8**, 757 (2012).

[29] I. A. Nechaev, P. M. Echenique, and E. V. Chulkov, *Phys. Rev. B* **81**, 195112 (2010).

[30] H. Daimon, C. Chung, S. Ino, and Y. Watanabe, *Surf. Sci.* **235**, 142 (1990).

[31] M. Sasaki, J. Yuhara, M. Inoue, and K. Morita, *Surf. Sci.* **283**, 327 (1993).

[32] J. Yuhara, M. Inoue, and K. Morita, *J. Vac. Sci. Technol. A* **11**, 2714 (1993).

[33] E. A. Khramtsova, A. A. Saranin, A. B. Chub, and V. G. Lifshits, *Surf. Sci.* **331**, 594 (1995).

[34] D. Ishikawa, J. Yuhara, R. Ishigami, K. Soda, and K. Morita, *Surf. Sci.* **357**, 432 (1996).

[35] J. Yuhara, D. Ishikawa, and K. Morita, *Appl. Surf. Sci.* **117-118**, 94 (1997).

[36] J. Yuhara and K. Morita, *Appl. Surf. Sci.* **123-124**, 56 (1998).

[37] D. Nakamura, J. Yuhara, and K. Morita, *Appl. Surf. Sci.* **130-132**, 72 (1998).

[38] J. Yuhara, K. Matsuda, Y. Hattori, and K. Morita, *Appl. Surf. Sci.* **162-163**, 368 (2000).

[39] J. Yuhara, D. Nakamura, K. Soda, and K. Morita, *Surf. Sci.* **482-485**, 1374 (2001).

[40] T. Yamanaka and S. Ino, *Surf. Sci.* **527**, L191 (2003).

[41] P. Shukrinov, P. Mutombo, V. Cháb, and K. C. Prince, *Surf. Sci.* **532-535**, 650 (2003).

[42] D. Gruznev, B. V. Rao, Y. Furukawa, M. Mori, T. Tambo, V. G. Lifshits, and C. Tatsuyama, *Appl. Surf. Sci.* **212-213**, 135 (2003).

[43] T. C. Di, B. Ressel, K. C. Prince, V. Cháb, S. Santucci, S. Faccani, G. Profeta, and L. Ottaviano, *J. Phys.: Condens. Matter* **16**, 3507 (2004).

[44] M. Morita, S. N. Takeda, M. Yoshikawa, A. Kuwako, Y. Kato, and H. Daimon, *Appl. Surf. Sci.* **254**, 7872 (2008).

[45] L. Tang, Z. L. Guan, D. Hao, J. F. Jia, X. C. Ma, and Q. K. Xue, *Appl. Phys. Lett.* **95**, 193102 (2009).

[46] C. Li, F. Wang, Q. Sun, and Y. Jia, *J. Phys.: Condens. Matter* **23**, 265001 (2011).

[47] N. V. Denisov, A. A. Yakovlev, O. A. Utas, S. G. Azatyan, A. V. Zotov, A. A. Saranin, L. N. Romashev, N. I. Solin, and V. V. Ustinov, *Surf. Sci.* **606**, 104 (2012).

[48] J. R. Osiecki, H. M. Sohail, P. E. J. Eriksson, and R. I. G. Uhrberg, *Phys. Rev. Lett.* **109**, 057601 (2012).

[49] D. V. Gruznev, A. V. Zotov, and A. A. Saranin, *J. Electron Spectrosc. Relat. Phenom.* **201**, 81 (2015).

[50] D. V. Gruznev, L. V. Bondarenko, A. V. Matetskiy, A. Y. Tupchaya, A. A. Alekseev, C. R. Hsing, C. M. Wei, S. V. Eremeev, A. V. Zotov, and A. A. Saranin, *Phys. Rev. B* **91**, 035421 (2015).

[51] P. Matvija, P. Sobotík, I. Ošťádal, and P. Kocán, *Appl. Surf. Sci.* **331**, 339 (2015).

[52] A. V. Matetskiy, S. Ichinokura, L. V. Bondarenko, A. Y. Tupchaya, D. V. Gruznev, A. V. Zotov, A. A. Saranin, R. Hobara, A. Takayama, and S. Hasegawa, *Phys. Rev. Lett.* **115**, 147003 (2015).

[53] T. Zhang, P. Cheng, W. J. Li, Y. J. Sun, G. Wang, X. G. Zhu, K. He, L. Wang, X. Ma, X. Chen *et al.*, *Nat. Phys.* **6**, 104 (2010).

[54] M. Yamada, T. Hirahara, and S. Hasegawa, *Phys. Rev. Lett.* **110**, 237001 (2013).

[55] P. E. Blöchl, *Phys. Rev. B* **50**, 17953 (1994).

[56] G. Kresse and D. Joubert, *Phys. Rev. B* **59**, 1758 (1999).

[57] G. Kresse and J. Hafner, *Phys. Rev. B* **49**, 14251 (1994).

[58] G. Kresse and J. Furthmüller, *Comput. Mater. Sci.* **6**, 15 (1996).

[59] C. J. Pickard and R. J. Needs, *J. Phys.: Condens. Matter* **23**, 053201 (2011).

[60] C. J. Pickard and R. J. Needs, *Phys. Rev. Lett.* **97**, 045504 (2006).

[61] A. J. Morris, C. J. Pickard, and R. J. Needs, *Phys. Rev. B* **78**, 184102 (2008).

[62] D. Gruznev, A. Matetskiy, L. Bondarenko, O. Utas, A. Zotov, A. Saranin, J. Chou, C. Wei, M. Lai, and Y. Wang, *Nat. Commun.* **4**, 1679 (2013).

[63] J. P. Chou, C. M. Wei, Y. L. Wang, D. V. Gruznev, L. V. Bondarenko, A. V. Matetskiy, A. Y. Tupchaya, A. V. Zotov, and A. A. Saranin, *Phys. Rev. B* **89**, 155310 (2014).

[64] J. P. Chou, C. R. Hsing, C. M. Wei, C. Cheng, and C. M. Chang, *J. Phys.: Condens. Matter* **25**, 125305 (2013).

[65] Y. G. Ding, C. T. Chan, and K. M. Ho, *Surf. Sci.* **275**, L691 (1992).

[66] T. Nagao, S. Hasegawa, K. Tsuchie, S. Ino, C. Voges, G. Klos, H. Pfnür, and M. Henzler, *Phys. Rev. B* **57**, 10100 (1998).

[67] J. Kautz, M. W. Copel, M. S. Gordon, R. M. Tromp, and S. J. van der Molen, *Phys. Rev. B* **89**, 035416 (2014).

[68] T. Shirasawa, W. Voegeli, T. Nojima, Y. Iwasawa, Y. Yamaguchi, and T. Takahashi, *Phys. Rev. Lett.* **113**, 165501 (2014).

[69] S. G. Kwon and M. H. Kang, *Phys. Rev. Lett.* **113**, 086101 (2014).

[70] K. Seino and F. Bechstedt, *Phys. Rev. B* **90**, 165407 (2014).

[71] M. A. U. Absor, F. Ishii, H. Kotaka, and M. Saito, *Appl. Phys. Express* **8**, 073006 (2015).
![](./images/813268097333985283_1.jpg)

CARBON 53 (2013) 346-356

Available at www.sciencedirect.com

SciVerse ScienceDirect

journal homepage: www.elsevier.com/locate/carbon

![](./images/813268097333985283_2.jpg)

# A theoretical quantification of the possible improvement in the mechanical properties of carbon nanotube bundles by carbon ion irradiation

N.P. O'Brien $^{a}$, M.A. McCarthy $^{a,*}$, W.A. Curtin $^{b}$

$^{a}$ Department of Mechanical, Aeronautical and Biomedical Engineering, Irish Centre for Composites Research, Materials and Surface Science Institute, University of Limerick, Limerick, Ireland
$^{b}$ Institute of Mechanical Engineering, STI-IGM-GE, Station 9, École Polytechnique Fédérale de Lausanne, 1015 Lausanne, Switzerland

---

## ARTICLE INFO

Article history:
Received 17 August 2012
Accepted 10 November 2012
Available online 17 November 2012

---

## ABSTRACT

Improvement of single wall carbon nanotube (CNT) bundle mechanical properties through carbon ion irradiation is investigated using molecular dynamics. Increased inter-tube shear and toughness properties through formation of inter-tube cross-links is balanced against decreased tensile strength from induced defects. Bundles irradiated with carbon ions with energy 50-300 eV/ion, and fluence between $4×10^{13}\ \text{cm}^{-2}$ and $2×10^{14}\ \text{cm}^{-2}$, are mechanically tested. We find that with careful control of irradiation parameters, shear and toughness parameters increase by an order of magnitude, while tensile properties reduce by only 30-40%; in real CNT fibres with discontinuous CNT filaments the reduction would be much less. The nano-scale interface response resembles that of micro-scale composites, in which interstitial C atoms play a key role. This makes C ion deposition an attractive option over irradiation by electrons or other types of ions, since the extra C atoms can provide the required interstitial atoms. Within a certain cross-link density range, the interface shear modulus, shear stress at bonding onset, and frictional sliding stress after debonding are all linearly related to cross-link density making controlled design of fibre shear properties feasible. A possible post-treatment with very low energy irradiation is proposed for healing holes and partially restoring tensile strength.

© 2012 Elsevier Ltd. All rights reserved.

---

### 1. Introduction

The exceptional mechanical properties of carbon nanotubes (CNTs) make them highly attractive as potential reinforcing constituents in next generation composites [1,2]. Due to van der Waals interactions, CNTs tend to form into hexagonally arranged bundles, which can form the basis for macroscopic CNT fibres or ropes [3,4]. However, the weakness of these van der Waals interactions during shear between neighbouring tubes has major negative ramifications for the mechanical properties of CNT fibre-based composites [5-8]. Tensile strength is compromised since transfer of loads from the matrix to the inner tubes in the bundle requires very long fibre lengths, so that over long portions of a CNT fibre, most of the CNTs carry very little load; flexural stiffness is severely limited due to the ease with which tubes can slide over each other; and composite toughness, particularly in ceramic matrices, is determined by the work required to fracture and pull out fibres bridging matrix cracks, and so is greatly reduced if the inner tubes can easily slide out from the bundle.

A number of researchers have investigated the use of irradiation or deposition, either with electrons or ions, to promote covalent bonds or cross-links between neighbouring walls in MWCNTs [8-14] or tubes [15-19] in CNT bundles. It

---

* Corresponding author. Fax: +353 61 202 944.
E-mail address: michael.mccarthy@ul.ie (M.A. McCarthy).
0008-6223/$ - see front matter © 2012 Elsevier Ltd. All rights reserved.
http://dx.doi.org/10.1016/j.carbon.2012.11.021

has been shown computationally that only a small amount of cross-links can dramatically increase inter-wall or inter-tube stiffness [16,20]. On the other hand, irradiation produces the unwanted side effect of other kinds of defects, such as vacan- cies, adatoms, and Stone-Wales defects, which have a detri- mental effect on mechanical properties, particularly tensile properties [12,16,21]. Thus a delicate balance has to be struck. The formation of defects (including cross-links) and their ef- fects on mechanical properties is a formidably complex prob- lem, influenced by many factors including CNT size, the number of walls, the number of tubes in the bundle, incident particle mass, energy, dosage and whether or not the particle forms chemical bonds with the C atoms in the CNT lattice [22]. Nevertheless, experimental evidence has recently been presented of a threefold increase in tensile strength in MWCNTs [8] and an order of magnitude increase in tensile strength and modulus in CNT bundles [7], achieved through promotion of cross-links via irradiation. These studies pro- vide strong motivation for further investigation of this topic, with the aim of elucidating the relationship between the chemical functionalization induced by the irradiation process and the changes in resulting mechanical properties.

To date, molecular dynamics studies have been performed on CNT irradiation with ions of noble gases [12,23-25], CH₃[15,26], CF₃[12], potassium [27], boron and nitrogen [28], as well as electron irradiation via a primary knock-on atom method [12]. Deposition of carbon ions or "self-deposition" has been considered for irradiation of single tubes in [22], CNT bundles in [17,19], and graphene in [29], although none of these studies have addressed the effects on mechanical properties. Carbon ion deposition is an interesting option since it introduces no impurities into the system, provides additional carbon interstitial atoms to mediate cross-links, and enables efficient momentum transfer due to the match between the mass of the deposition and target atoms.

In [19] we presented a molecular dynamics study of the carbon-ion irradiation of SWCNT bundles, with carbon ions. We demonstrated that carbon-ion irradiation induces CNT cross-links but also causes defects. The ability to control the level of cross-linking through adjusting the energy/ion or the fluence was demonstrated in principle for small bundles. The cross-links formed were found to be of several different types, from simple direct bonds between CNTs, to complex links involving one or more interstitial atoms. In the present paper, we study the relationship between the cross-links and defects induced by carbon ion irradiation of SWCNT bun- dles, and the resulting mechanical properties. We quantify the improved inter-tube shear and toughness properties through pull-out tests of individual CNTs from the bundle. This also gives us the opportunity to examine the applicabil- ity of standard "friction laws" to nano-scale sliding interfaces, building on the work in [11] on sliding between CNTs and dia- mond matrices. We also measure the reduction in tensile properties due to induced defects. Our study uses a re- cently-developed reactive bond-order potential with environ- ment-dependent first nearest-neighbour definition [30] which accurately simulates bond-forming and bond-breaking pro- cesses in carbon-based systems. Our simulations reveal that with careful control of irradiation parameters, shear and toughness parameters are greatly increased, with only modest reductions in tensile properties. Interstitial C atoms are found to play a key role in sliding behaviour. Within a cer- tain range of cross-link density, the interface shear modulus, shear stress at onset of debonding, and frictional sliding stress after debonding are all linearly related to cross-link density making controlled design of fibre shear properties feasible.

## 2. Simulation method
### 2.1. Interatomic interactions
To study the pull-out of CNTs from a bundle and tensile strength of bundles, an accurate interatomic potential capa- ble of representing bond breaking and bond forming is essen- tial. As described in [19] molecular mechanics calculations in the literature performed using the well-established REBO po- tential [31] show inappropriate fracture mechanisms and grossly overestimate the stress for C-C bond breaking, as compared to values predicted by quantum mechanics calcu- lations [32-35]. The inaccuracy stems from the functional form for the cutoff function used in the original REBO poten- tial that greatly increases the bond force for distances be- tween 0.17 nm and 0.20 nm [36]. For studies only concerned with bond breaking, some authors have avoided the nonphys- ical fracture mechanisms by removing the cutoff function [10,34,37] which then leads to underestimation of the stresses for bond breaking [10,14,32-34,37] and, moreover, precludes consideration of bond formation. To rectify these problems, we use a modified REBO potential recently presented in [30], where a local environment-dependent cut-off function based on screening concepts [38] allows a bond between two atoms to persist over long distances provided that no third atom moves into the bonding region. This leads to smooth changes in forces and a much better description of bond breaking and reforming compared with first principles calculations.

### 2.2. Geometry and irradiation simulations
Full details of the irradiation simulations are given in [19] so only brief details are presented here. The geometry simulated comprised a bundle of seven hexagonally arranged (26, 0) SWCNTs, each with radius 10.18 Å and length 59.6 Å (see Fig. 1). Our simulations mimicked the pulsed laser deposition process in [39,40] which produces both C⁺ ions and neutral carbon atoms (as well as slower C₂ and C₃ molecules). Periodic boundary conditions (PBCs) were applied in the z direction to simulate an 'infinitely' long bundle. Five "rings", of deposition carbon atoms were initially placed around the CNT bundle, as shown in Fig. 1(a). Deposition atom coordinates and trajecto- ries (within the angle ± 28°, illustrated in Fig. 1(b)) were gener- ated randomly. The wide angle was chosen so as to produce inter-tube links which connect the CNTs not just radially, but also circumferentially. The deposition strategy simulated is somewhat idealised, but should be achievable through modification of the pulsed laser deposition procedure used in [40]. The rings of deposition atoms were fired in one at a time without a thermostat so the energy of the impinging atoms was added to the CNT bundle, with relaxation and cooling phases following each ring. Incident energies of

![](./images/813268097333985283_3.jpg)

Fig. 1 – (a) Hexagonally arranged 7-tube (26, 0) SWCNT bundle model with five rings of deposition atoms, (b) random deposition atom trajectory parameters and portion of outer tubes, s, within bond interaction distance of centre tube and thus contributing to the "shear area", $A_{SH}$, when the centre tube is pulled out; L = tube length, (c) inter-tube cross-links and adatoms formed and (d) example of vacancy defects formed.

50 eV/ion, 100 eV/ion, 150 eV/ion, 200 eV/ion and 300 eV/ion were examined. The fluence (particles per unit area) varied from $4.0 \times 10^{13}\ \text{cm}^{-2}$ for one deposition "ring", up to $2.0 \times 10^{14}\ \text{cm}^{-2}$ for five deposition rings. We define "dosage" here as the total incident energy – which is the energy/ion multiplied by the number of incident ions – divided by the mass of the CNT bundle. Our dosages ranged from 2 MGy (or MJ/kg) for one ring of 50 eV ions to 60 MGy for five rings of 300 eV ions. For all incident energies, five runs with varying initial random trajectories of the incident C atoms were performed in order to assess statistical variation.

### 2.3. Mechanical test simulations

The mechanical properties of the pristine and irradiated SWCNT bundles were evaluated through MD simulations of tensile tests and "pull-out" tests involving drawing out of the centre CNT. The bundles tested were those for which one, three, and five rings of atoms had been deposited, giving15 tensile tests and 15 pull-out tests at each deposition energy. As in the deposition simulations, periodic boundary conditions were applied for both tests in order to simulate an 'infinitely' long bundle and to avoid end effects. The MD time step was set to 0.25 fs and a velocity re-scaling thermostat was used to maintain the temperature of the CNT rope models at 0.5 K throughout each test. During the initial relaxation phase which lasted 12.5 ps for the tensile test and 18.75 ps for the pull-out test, both ends of the CNT bundle were fixed in z and free to move in x and y for both tests. After relaxation, the tensile and pull-out tests were performed. An NVE microcanonical ensemble was used for the pull-out tests, whereas an NPT ensemble was used for the tension tests to allow the volume of the simulation box to vary as it is deformed in the z direction.

For the tensile test, the top face of the periodic box was displaced $0.025\ \text{\AA}$ in the z direction every 0.25 ps, while the bottom face was kept fixed in z, until the bundle failed. The applied stress was measured on the top face. For the pull-out test, the bottom two rings of atoms for the outer CNTs were fixed in the z direction, and the centre CNT was drawn out by displacing its upper two rings of atoms $0.025\ \text{\AA}$ every 0.25 ps, across the periodic box boundaries. The pull-out force was obtained as the force on these two rings of atoms. Relaxation was performed between displacements. For both test series, the displacement rate was 10 m/s and all CNTs were free to move in the x and y directions throughout.

## 3. Results and discussion

### 3.1. Irradiation effects on inter-tube shearing

The irradiation simulations resulted in inter-tube cross-links (Fig. 1(c)). More than ten different types of cross-link were observed, including direct $\text{sp}^3$ bonded links with no interstitial C atom, and links mediated by one or more interstitial C atoms. For full details see [19]. The cross-links relevant to the pull-out tests are those between the outer tubes and the centre tube, hereafter referred to as "centre links". We define a reference area for shear resistance as $A_{SH}$, see Fig. 1(b). This area includes all atoms in the outer CNTs which are within the interaction distance of the centre CNT atoms for the potential [30] used here (prior to irradiation) and includes all centre links post-irradiation. We divide the number of centre links by $A_{SH}$ to get an areal inter-tube link density (ITLD or $\rho$). Fig. 2 shows $\rho$ as a function of dosage for energy/ion of 50–300 eV. We see that in the range 100–200 eV/ion, $\rho$ is proportional to dosage, and thus can be controlled by varying either the fluence or the energy/ion. Lower energy irradiation (50 eV/ion) was relatively ineffective in forming centre links. Higher energy irradiation (300 eV/ion) was highly effective in forming centre links, but production of defects was excessive [19].

![](./images/813268097333985283_4.jpg)

Fig. 2 – Areal inter-tube link density (ITLD or $\rho$), as a function of dosage, with incident beam energies of 50–300 eV (only links to centre CNT included).

![](./images/813268097333985283_5.jpg)

Fig. 3 - Pull-out stress versus pull-out distance for irradiated CNT bundles with incident energies of (a) 50 eV, (b) 100 eV, (c) 150 eV, and (d) 200 eV.

The average interfacial shear stress is calculated as the pull-out force divided by $A_{SH}$. Fig. 3 shows the pull-out stress versus pull-out distance for the irradiated SWCNT bundles; only the result which is most representative of the five random trajectory instances is shown for clarity. For comparison, the result for the pristine case is shown in Fig. 3(a). We see that the nano-scale interface response resembles that of traditional micro-scale composites: pull-out is characterised by an elastic stretching region at small displacements ($x < 1$-$2$ Å), followed by the onset of debonding, in which inter-tube bonds are broken, up to a displacement of 2-3.5 Å and then a drop to a lower oscillating sliding stress ("pull-out sliding" regime). The only exception to this behaviour is the highest dosage case (39.3 MGy) where the shear stress reaches a peak of 10.1 GPa and then drops to zero. In this case, the centre CNT did not pull out and instead failed in tension. Both the elastic and sliding response vary with dosage, which as mentioned above is directly related to $\rho$. Notably, the effective frictional stresses at the interface after debonding are quite high (several GPa) for higher cross-link densities.

The nano-scale pull-out behaviour shown in Fig. 3, resembles micro-scale composite response, and can be understood by analysing the atomic deformation mechanisms at the interface. As noted above, more than ten different types of inter-tube cross-link were found post-irradiation. Fig. 4 shows snapshots in time of the pull-out behaviour of three of them: a direct link, a link involving one interstitial carbon atom, and a link involving two interstitial carbon atoms. The key finding from this figure is that when cross-links involving an interstitial atom (Fig. 4(b) and (c)) break (at the end of the elastic region of pull-out), new links are formed and broken several times subsequently. On the other hand, direct links in which no interstitial is present (Fig. 4(a)), once broken, do not re-form, and so do not contribute to the pull-out force in the sliding regime. The bond breaking and reforming processes for interstitial-mediated cross-links are responsible for the overall 'stick and slip' behaviour observed. The directly bonded cross-links contribute to the initial elastic behaviour but not to the sliding stress. We can conclude that to produce tough CNT-fibres, in which significant energy is absorbed during CNT pull-out from the fibre, it is desirable to have C interstitials at CNT interfaces, since inter-tube links will spontaneously form and break during sliding. This makes C ion deposition an attractive option over irradiation by electrons or other types of ions, since extra C atoms are added to the system, so not all interstitials have to come from knocking out atoms from the CNT lattice (thereby reducing tensile strength).

The pull-out force was divided by the number of centre links to give the pull-out force per centre link, which is plotted against pull-out distance in Fig. 5, for energies ranging from 50 eV to 200 eV; only representative instances among the five random trajectories for each case are shown for clarity. The ITLD ($\rho$) is also shown in the legend. In [11] the pull-out force per cross-link involving a single interstitial carbon atom between a CNT and a diamond matrix was found to collapse

![](./images/813268097333985283_6.jpg)

Fig. 4 - Bond breaking and re-forming during pull out of centre CNT. Snapshots in time, time increasing from left to right, numbers are to guide eye in following individual atoms over time, (a) direct $sp^3$-$sp^3$ bond, (b) cross-link with one interstitial and two $sp^3$-$sp$ bonds, and (c) cross-link with two interstitials and seven $sp^3$-$sp^3$ bonds.

all the data for different interstitial densities onto nearly a single universal curve for interstitial C atom densities of 0.73–2.18 nm⁻². The system studied here differs from that in [11] in that the cross-links are between two CNTs rather than between a CNT and diamond matrix, and there are several different types of cross-link, some of which are direct links and some of which involve one or multiple interstitials. We see from Fig. 5 that for low cross-link densities, $\rho < 0.7$ nm⁻², the force per cross-link is high and oscillates erratically. This is due to the small number of inter-tube links at this density, given the short length of the tubes studied. With just a few links distributed randomly axially and circumferentially very unsymmetrical loads on the centre CNT occur, with large relative force oscillations as individual cross-links break and re-form. However, as $\rho$ increases into the range considered in [11], i.e. $\rho > 0.7$ nm⁻² (which corresponds to >18 centre links in total in the system) the curves collapse quite well onto a single curve, as in [11]. We can thus say that the varying strength of the different cross-link types averages out if enough of them are present, and we can directly relate the shear mechanical properties to the number of cross-links present or $\rho$. Unlike [11] however, we find an upper limit to this, since above $\rho = 1.7$ nm⁻², we see from Fig. 6(d) that failure of the centre CNT during pull-out can occur since the interfacial shear stress is too large. It needs to be borne in mind that, unlike in [11], the centre CNT, like all the CNTs in the bundle, contains defects such as vacancies and Stone-Wales defects due to the irradiation process, so the value of $\rho$ needed to cause pull-out CNT failure would vary somewhat depending on the damage level in the pull-out CNT.

In Fig. 6, we plot some key parameters against $\rho$, for $\rho > 0.7$ nm⁻². Fig. 6(a) shows the "interface shear modulus" $\mu$ prior to debonding. Here we have defined the interface shear strain $\gamma_{xy}$ as the applied displacement divided by the inter-tube gap. From the graph we see that $\mu$ scales linearly with $\rho$, in the range $\rho = 0.7$–1.7 nm⁻²,

$$
\mu \cong 10\rho \ \text{GPa nm}^2 \tag{1}
$$

This is more than double the value $\mu \cong 4.6\rho$ GPa nm², found in [11] for CNT sliding in a diamond matrix with interstitial carbon atoms. On the other hand, in [20] an effective shear modulus for the interface between walls of a DWNT directly bonded with $sp^3$-bonds was found that scales with the bond fraction $f$. Converting their bond fraction $f$ to an areal density of bonds $\rho$, their result is

$$
\mu \cong 12\rho \ \text{GPa nm}^2 \tag{2}
$$

Since in our system, both direct bonds and bonds mediated by interstitial C atoms are present, it is reasonable that our result should be between the values found in [11,20]. Furthermore, the bonds in [11] involved one interstitial C atom initially bonded to just one CNT atom and one diamond matrix atom. As described in [19] many of the interstitial atoms in our system were initially bonded to more than one atom

![](./images/813268097333985283_7.jpg)

Fig. 5 - Pull-out force per inter-tube cross-link with the centre CNT versus pull-out distance for irradiated CNT bundles with incident energies of (a) 50 eV, (b) 100 eV, (c) 150 eV, and (d) 200 eV (ITLD = inter-tube link density or $\rho$ in $1/nm^{2}$).

in each CNT - an example can be seen in Fig. 4(c) - which is a stiffer arrangement, so the interstitial-mediated bonds here are on average stiffer than in [11]. We see that with an areal density of cross-links, $\rho=1.7\ nm^{-2}$, we get an interface shear modulus 17 GPa. This is more than three times the value of 5 GPa found from our simulations of CNT bundles without cross-linking.

In Fig. 6(b) and (c) we see that in the range $\rho=0.7-1.7\ nm^{-2}$, the interface shear stress at the onset of debonding or yield stress, $\tau_{y}$ (note this is not the maximum shear stress during pull-out, it is the stress at the end of the linear region of the load-displacement curve), and the frictional sliding stress after debonding, $\tau$ (calculated for pull-out distance $x>8\mathring{A}$) are both linearly dependent on $\rho$, scaling as

$$
\tau_{y} \cong 3.7\rho\ \text{GPa nm}^2 \tag{3}
$$

$$
\tau \cong 2.6\rho\ \text{GPa nm}^2 \tag{4}
$$

Concerning the interface shear strength $\tau_{y}$, we see that with $\rho=1.7\ nm^{-2}$, we get an interface shear strength of 6.3 GPa. This is seven times larger than the value of 0.9 GPa we found for CNT bundles without cross-linking. The equation for $\tau$ is slightly below the value found in [11] ($\tau \cong 3\rho$ GPa nm$^{2}$), which contrasts with the finding on modulus above. The reason for this becomes clear from examining Fig. 4(c) and other similar cases, from which we see that while original cross-links may be quite complex and initially stiffer than those in [11], re-bonds after failure tend to be chain-like, resembling the cross-links involving a single interstitial in [11]. In addition, unlike [11] there are some direct bonds between CNTs in our system, which as noted above do not reform once broken and thus do not contribute to the sliding stress. Our results provide further evidence to that in [11] that a friction-like sliding stress emerges at the atomistic scale, thus conforming to the standard constant sliding stress used in the majority of models to predict composite performance.

An important issue in composite behaviour is toughness, which is dominated by the energy dissipated by frictional sliding during fibre pull-out. The energy dissipated due to "friction" generated by breaking and re-forming of interstitial-mediated inter-tube bonds can be computed as the work done during pull-out, corresponding to the area under the applied force vs. displacement curve. Typically the pull-out work is converted into a fracture toughness by division by the composite cross-sectional area; here we take the "composite" cross-sectional area to be the area of the circle enclosing the 7-tube bundle. For a density of $\rho=1.46\ nm^{-2}$, we obtain a toughness of $\sim 2.8\ J\ m^{-2}$ for just 1 nm of pull out. Such a value far exceeds the work done by weak van der Waals bonding between perfect nanotubes ($0.2\ J\ m^{-2}$ for 1 nm of pull out in our simulations).

### 3.2. Tensile test simulations

The trade-off for the above greatly enhanced shear properties is reduced tensile strength due to irradiation-produced

![](./images/813268097333985283_8.jpg)

Fig. 6 - Elastic and sliding parameters for pull-out versus ITLD (or $\rho$) for irradiated CNT bundles (a) interface shear modulus, (b) interface shear strength, and (c) interface sliding stress. Lines show linear relationships in the range $\rho$ = 0.7-1.7 nm$^{-2}$.

defects. For our tensile tests, the tensile stress was defined as the tensile force divided by the cross-sectional area of the CNT bundle (~15 nm$^2$), which was computed as seven times the area of a single CNT, as given in Eq. (11),

$$
A = 7\pi\left[\left(r+\frac{t}{2}\right)^2 - \left(r-\frac{t}{2}\right)^2\right] \tag{5}
$$

where $r$ is the CNT radius and $t$ = 0.335 nm is the graphitic layer thickness. The strain was calculated by dividing the change in length by the original length of the CNT bundle. Fig. 7(a) shows the tensile stress versus strain for the bundles irradiated with energies of 100 eV/ion (for all random trajectories) - the curves from other irradiation energies are similar in form. For comparison, our result for the pristine (unirradiated) bundle is also shown. For the pristine case, the Young's modulus, tensile strength and maximum strain are 860 GPa, 91 GPa and 17.2% respectively, which is at the low end of theoretical values in the literature for individual CNTs [8,41,42]. MD simulations tend to underestimate tensile strength compared to more accurate quantum mechanics calculations [32-35]. However our interest is in changes due to irradiation, not exact theoretical values, so the fact that these values are in the correct range is sufficient for our purposes.

We see from Fig. 7(a) that carbon atom irradiation causes a significant decrease in stiffness, strength and maximum strain relative to the pristine case. However, while pristine CNTs are the ultimate baseline, their existence in practical macro-scale composites can be considered rare. Thus, we performed a tensile test simulation on a bundle with just one single-atom vacancy in one CNT and from Fig. 7(a) we find a tensile strength of 81 GPa and a tensile strain of 11.9%, representing drops of 11% and 31%, respectively from the pristine case. This level of reduction is in line with previous studies on single CNTs with single vacancies [36]. We see that the reduction in tensile properties due to irradiation is much milder when considered against this less stringent baseline.

Clean planar fracture was exhibited for the pristine bundle, with the stress dropping to zero after failure. The irradiated bundles exhibited a less clean fracture, with crack propagation between CNTs at sites where inter-tube bonds had formed, and the stress does not reduce to zero as bonds still remain between CNTs after failure occurs. Another feature evident in Fig. 7(a) is that the irradiated bundles were already under slight tensile load before they were tensile tested, particularly at higher energies. This is because damage and inter-tube linking caused the equilibrium length of the CNT bundle to reduce during irradiation.

Fig. 7(b) and (c) provides a statistical analysis of the results from all tensile test simulations for strength and maximum strain respectively. We see that for the maximum dosage considered here (40 MGy), the tensile strength reduces to ~50 GPa and the maximum strain reduces to ~8%, representing 38% and 33% drops respectively from the single 1-atom vacancy case. It is also noticeable that at similar dosages, lower energy irradiation produces less of a reduction. In the previous section, we found that within the inter-tube link density range

![](./images/813268097333985283_9.jpg)

Fig. 7 - Tensile test result on 7-tube bundles, (a) stress versus strain for incident energy of 100 eV, (b) tensile strength, (c) maximum strain, and (d) strength vs. maximum hole size.

$\rho=0.7-1.7\ \text{nm}^{-2}$, the shear properties are predictable and improve by an order of magnitude over non-irradiated bundles. Thus we see a very large benefit, for a relatively small cost. In fact the reduction in tensile strength considered here is greater than would occur in practical CNT-fibre reinforced composites. In macro-scale CNT fibres, individual CNTs would be unlikely to run along the full length of the fibre, and when embedded in a matrix, load would generally be transferred from the matrix to the outer CNTs and then inwards through shear load transfer between CNTs. Highly imperfect bonding to the matrix would exist at the fibre ends, in contrast with the end conditions here. Inter-tube cross-links would facilitate the transfer of load to all CNTs in the fibre, and so would have major beneficial effects on the tensile strength of macro-scale fibres in composites, which would offset the reductions described above.

As noted above we found many different types of defects [19] post-irradiation, at random locations within the bundle. Under tensile load, the load transfer within the cross-linked, defective CNT bundles is highly complex. However, Fig. 7(d) shows that there is still a strong correlation between the reduction in tensile strength and the largest hole size in the bundle after irradiation (measured as the largest distance across the hole, as illustrated in the figure), as one would expect for a single CNT. We find that $\sigma_{\mathrm{Ult}} \propto c^{-m}$, with $m \cong 0.35$, where $c$ is the largest hole size. This is close to the value $m \cong 0.4$ that we found in [10] for pristine MWCNTs. There is scatter in Fig. 7(d) because tensile strength is also affected by other defects found such as Stone-Wales defects and adatoms. For example, we performed a tensile test simulation with just one adatom on one CNT and found the bundle strength decreases to 85.9 GPa and the maximum strain diminishes to 13.5%, which are reductions from the pristine case of 5.6% and 22% respectively. This is because the bonding at the attachment point changes from $\mathrm{sp}^{2}$ to $\mathrm{sp}^{3}$, with consequent increase of bond length from $1.42 \AA$ to $1.54 \AA$, which weakens the CNT structure.

In considering an optimal strategy for irradiation then, one should consider the effect on maximum hole size. In [19] we found that for the same dosage, irradiation with 100 eV irradiation led to smaller holes than 200 eV irradiation, and this ties in with the tensile strength values seen in Fig. 7(b) and (d). An advantage of C ion deposition is that it provides extra C atoms to the system, which on subsequent annealing have the potential to migrate to vacancy locations, causing healing of the CNT lattice. A further observation related to this issue is that irradiation at very low energy ($\sim 1$ eV/ion) can actually result in filling in or healing of pre-existing holes as deposition atoms latch onto dangling bonds on the hole perimeter. This process is illustrated in Fig. 8(a) and (b). This results in an increase in tensile strength of the bundle with negligible change in pull-out stress - see Fig. 9 for the beneficial effect of 1250 additional "healing" C atoms deposited at 1 eV/ion energy. Thus a potential strategy would be to apply low energy deposition, after irradiation at the energies needed to produce cross-links. The limitation on this is that as well as filling in

![](./images/813268097333985283_10.jpg)

Fig. 8 - Largest hole size for 150 eV, 17.88 MGy, (a) pre-healing, (b) after depositing 3 additional rings of 250 atoms at 1 eV (red dashed ring highlights area where hole healing has taken place), and (c) line up of adatoms providing weak point in structure; green bonds are ~1.54 Å in length, blue bonds are ~1.42 Å in length. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)

![](./images/813268097333985283_11.jpg)

Fig. 9 - Effect of "healing" 1 eV C ion irradiation on (a) tensile strength and (b) pull-out stress.

holes, the low energy atoms also adsorb as adatoms. As noted above, adatoms reduce tensile strength, though the effect is masked by vacancy defects which have a greater impact on tensile strength. However, if enough adatoms are deposited during low energy irradiation they will eventually line up somewhere in the bundle, perpendicular to the CNT axial direction, forming a crack-like weakening of the structure. The highlighted area in Fig. 8(c) shows one such example after 2000 "healing" atoms were applied, and the CNT bundle failed at this location when tensile loading was applied resulting in a reduction in tensile strength (see Fig. 9(a)).

### 4. Concluding remarks

In summary, we have investigated the improvement of the mechanical properties of single wall carbon nanotube bun- dles through carbon ion irradiation using classical molecular dynamics simulations. These studies were made possible through the use of a recently developed modified REBO poten- tial that introduces an environmental screening coefficient to accurately capture bond breaking and reforming processes. With careful control of irradiation parameters, we find that shear and toughness properties are increased by an order of magnitude, while tensile properties are reduced by only ~30-40% relative to a bundle with a single defect. In fact in real CNT fibres containing discontinuous CNT filaments the increased load transfer between CNTs would result in an in- crease in tensile strength that would significantly offset or even negate such a reduction. We find that the nano-scale interface response resembles that of traditional micro-scale composites: pull-out is characterised by an elastic stretching region at small displacements followed by the onset of deb- onding, in which inter-tube bonds are broken, and then a drop to a lower sliding stress, in which inter-tube links involv- ing interstitial C atoms are continuously re-formed and bro- ken. In contrast direct bonds between CNTs, once broken do not reform and thus do not contribute to the sliding stress. For energy absorption during pull-out it is thus desirable to have C interstitials at CNT interfaces, which makes C ion deposition an attractive option over irradiation by electrons or other types of ions, since extra C atoms are added to the system. Another advantage of adding C atoms to the system is that they may migrate on annealing to partially heal vacan- cies caused by irradiation. Within a certain range of cross-link density, the interface shear modulus, shear stress at onset of debonding, and frictional sliding stress after debonding are all linearly related to cross-link density making controlled design of fibre shear properties feasible. Despite the variety of de- fects formed the tensile strength of irradiated bundles de- pends strongly on one parameter, viz.: largest hole size in

the bundle. A possible post-irradiation treatment with very low energy irradiation is proposed for healing such holes and therefore partially restoring tensile strength. The relationships found here between cross-link/defect density and mechanical properties should hold for larger bundles than considered here, although as noted in [19] the irradiation strategies for achieving such cross-link densities will be more complex.

## Acknowledgements
This work has been supported by the INSPIRE project under the Programme for Research in Third Level Institutions, Higher Education Authority of Ireland. Computations were performed on the Irish Centre for High End Computing facilities (ICHEC).

## REFERENCES
[1] Yu MF, Files BS, Arepalli S, Ruoff RS. Tensile loading of ropes of single wall carbon nanotubes and their mechanical properties. Phys Rev Lett 2000;84(24):5552-5.

[2] Yakobson BI, Avouris P. Mechanical properties of carbon nanotubes. Carbon Nanotubes 2001;80:287-327.

[3] Cheng TW, Hsu WK. Winding of single-walled carbon nanotube ropes: an effective load transfer. Appl Phys Lett 2007;90(12):123102-1-3.

[4] Zhang XF, Li QW, Tu Y, Li YA, Coulter JY, Zheng LX, et al. Strong carbon-nanotube fibers spun from long carbon-nanotube arrays. Small 2007;3(2):244-8.

[5] Xia Z, Curtin WA. Pullout forces and friction in multiwall carbon nanotubes. Phys Rev B 2004;69(23):233408-1-4.

[6] Salvetat JP, Briggs GAD, Bonard JM, Bacsa RR, Kulik AJ, Stockli T, et al. Elastic and shear moduli of single-walled carbon nanotube ropes. Phys Rev Lett 1999;82(5):944-7.

[7] Filleter T, Bernal R, Li S, Espinosa HD. Ultrahigh strength and stiffness in cross-linked hierarchical carbon nanotube bundles. Adv Mater 2011;23(25):2855-60.

[8] Peng B, Locascio M, Zapol P, Li SY, Mielke SL, Schatz GC, et al. Measurements of near-ultimate strength for multiwalled carbon nanotubes and irradiation-induced crosslinking improvements. Nat Nanotechnol 2008;3(10):626-31.

[9] Byrne EM, Letertre A, McCarthy MA, Curtin WA, Xia Z. Optimizing load transfer in multiwall nanotubes through interwall coupling: theory and simulation. Acta Mater 2010;58(19):6324-33.

[10] Byrne EM, McCarthy MA, Xia Z, Curtin WA. Multiwall nanotubes can be stronger than single wall nanotubes and implications for nanocomposite design. Phys Rev Lett 2009;103(4):045502-1-4.

[11] Pavia F, Curtin WA. Interfacial sliding in carbon nanotube/diamond matrix composites. Acta Mater 2011;59(17):6700-9.

[12] Pregler SK, Sinnott SB. Molecular dynamics simulations of electron and ion beam irradiation of multiwalled carbon nanotubes: the effects on failure by inner tube sliding. Phys Rev B 2006;73(22):224106-1-9.

[13] Fonseca AF, Borders T, Baughman RH, Cho KJ. Load transfer between cross-linked walls of a carbon nanotube. Phys Rev B 2010;81(4):045429-1-7.

[14] Li L, Xia ZH, Curtin WA, Yang YQ. Molecular dynamics simulations of interfacial sliding in carbon-nanotube/diamond nanocomposites. J Am Ceram Soc 2009;92(10):2331-6.

[15] Ni B, Andrews R, Jacques D, Qian D, Wijesundara MBJ, Choi YS, et al. A combined computational and experimental study of ion-beam modification of carbon nanotube bundles. J Phys Chem B 2001;105(51):12719-25.

[16] Kis A, Csanyi G, Salvetat JP, Lee TN, Couteau E, Kulik AJ, et al. Reinforcement of single-walled carbon nanotube bundles by intertube bridging. Nat Mater 2004;3(3):153-7.

[17] Federizzi RL, Moura CS, Amaral L. Polymerization of carbon nanotubes through self-irradiation. J Phys Chem B 2006;110(46):23215-20.

[18] Cornwell CF, Welch CR. Very-high-strength (60-GPa) carbon nanotube fiber design based on molecular dynamics simulations. J Chem Phys 2011;134(20):204708-1-8.

[19] O'Brien NP, McCarthy MA, Curtin WA. Improved inter-tube coupling in CNT bundles through carbon ion irradiation. Carbon 2013;51:173-84.

[20] Xia ZH, Guduru PR, Curtin WA. Enhancing mechanical properties of multiwall carbon nanotubes via sp(3) interwall bridging. Phys Rev Lett 2007;98(24):245501-1-4.

[21] Sammalkorpi M, Krasheninnikov AV, Kuronen A, Nordlund K, Kaski K. Irradiation-induced stiffening of carbon nanotube bundles. Nucl Instrum Methods Phys Res Sect B 2005;228:142-5.

[22] Xu ZJ, Zhang W, Zhu ZY, Huai P. Molecular dynamics study of damage production in single-walled carbon nanotubes irradiated by various ion species. Nanotechnology 2009;20(12):125706-1-11.

[23] Pomoell JAV, Krasheninnikov AV, Nordlund K, Keinonen J. Ion ranges and irradiation-induced defects in multiwalled carbon nanotubes. J Appl Phys 2004;96(5):2864-71.

[24] Pregler SK, Jeong B-W, Sinnott SB. Ar beam modification of nanotube based composites using molecular dynamics simulations. Compos Sci Technol 2008;68(9):2049-55.

[25] Salonen E, Krasheninnikov AV, Nordlund K. Ion-irradiation-induced defects in bundles of carbon nanotubes. Nucl Instrum Methods Phys Res Sect B 2002;193:603-8.

[26] Ni B, Sinnott SB. Chemical functionalization of carbon nanotubes through energetic radical collisions. Phys Rev B 2000;61(24):16343-6.

[27] Kotakoski J, Krasheninnikov A, Nordlund K. A molecular dynamics study of the clustering of implanted potassium in multiwalled carbon nanotubes. Nucl Instrum Methods Phys Res Sect B 2005;240(4):810-8.

[28] Kotakoski J, Krasheninnikov AV, Ma YC, Foster AS, Nordlund K, Nieminen RM. B and N ion implantation into carbon nanotubes: insight from atomistic simulations. Phys Rev B 2005;71(20):205408-1-6.

[29] Compagnini G, Giannazzo F, Sonde S, Raineri V, Rimini E. Ion irradiation and defect formation in single layer graphene. Carbon 2009;47(14):3201-7.

[30] Pastewka L, Pou P, Perez R, Gumbsch P, Moseler M. Describing bond-breaking processes by reactive potentials: importance of an environment-dependent interaction range. Phys Rev B 2008;78(16):161402-1-4.

[31] Brenner DW, Shenderova OA, Harrison JA, Stuart SJ, Ni B, Sinnott SB. A second-generation reactive empirical bond order (REBO) potential energy expression for hydrocarbons. J Phys-Condens Matter 2002;14(4):783-802.

[32] Yakobson BI, Campbell MP, Brabec CJ, Bernholc J. High strain rate fracture and C-chain unraveling in carbon nanotubes. Comput Mater Sci 1997;8(4):341-8.

[33] Hirai Y, Nishimaki S, Mori H, Kimoto Y, Akita S, Nakayama Y, et al. Molecular dynamics studies on mechanical properties of carbon nano tubes with pinhole defects. Jpn J Appl Phys 2003;42:4120. Copyright (C) 2003 The Japan Society of Applied Physics.

[34] Shenderova OA, Brenner DW, Omeltchenko A, Su X, Yang LH. Atomistic modeling of the fracture of polycrystalline diamond. Phys Rev B 2000;61(6):3877-88.

[35] Pastewka L, Moser S, Moseler M. Atomistic insights into the running-in, lubrication, and failure of hydrogenated diamond-like carbon coatings. Tribol Lett 2010;39(1):49-61.

[36] Belytschko T, Xiao SP, Schatz GC, Ruoff RS. Atomistic simulations of nanotube fracture. Phys Rev B 2002;65(23):235430-1-8.

[37] Zhang SL, Mielke SL, Khare R, Troya D, Ruoff RS, Schatz GC, et al. Mechanics of defects in carbon nanotubes: atomistic and multiscale simulations. Phys Rev B 2005;71(11):115403-1-12.

[38] Baskes MI, Angelo JE, Bisson CL. Atomistic calculations of composite interfaces. Modell Simul Mater Sci Eng 1994;2(3A):505-18.

[39] Schittenhelm H, Geohegan DB, Jellison GE, Puretzky AA, Lance MJ, Britt PF. Synthesis and characterization of single-wall carbon nanotube-amorphous diamond thin-film composites. Appl Phys Lett 2002;81(11):2097-9.

[40] Sorescu M, Grabias A, Tarabasanu-Mihaila D, Diamandescu L. Bulk versus surface effects in magnetic thin films obtained by pulsed laser deposition. Appl Surf Sci 2003;217(1-4):233-8.

[41] Mielke SL, Troya D, Zhang S, Li JL, Xiao SP, Car R, et al. The role of vacancy defects and holes in the fracture of carbon nanotubes. Chem Phys Lett 2004;390(4-6):413-20.

[42] Ogata S, Shibutani Y. Ideal tensile strength and band gap of single-walled carbon nanotubes. Phys Rev B 2003;68(16):165409-1-4.
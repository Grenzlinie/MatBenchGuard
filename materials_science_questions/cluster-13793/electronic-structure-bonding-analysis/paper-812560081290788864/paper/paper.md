# Ab initio calculations and a scratch test study of RF-magnetron sputter deposited hydroxyapatite and silicon-containing hydroxyapatite coatings

R.A. Surmenev$^{a,*}$, I.Yu. Grubova$^{a}$, E. Neyts$^{b}$, A.D. Teresov$^{c}$, N.N. Koval$^{c}$, M. Epple$^{d}$, A.I. Tyurin$^{e}$, V.F. Pichugin$^{a}$, M.V. Chaikina$^{f}$, M.A. Surmeneva$^{a}$

$^{a}$ Physical Materials Science and Composite Materials Centre, National Research Tomsk Polytechnic University, Tomsk
$^{b}$ Department of Chemistry, PLASMANT Research Group, NANOLab Center of Excellence, University of Antwerp, Universiteitsplein 1, B-2610, Wilrijk-Antwerp, Belgium
$^{c}$ Institute of High Current Electronics SB RAS, 2/3 Akademichesky Avenue, 634055, Tomsk, Russia
$^{d}$ Inorganic Chemistry and Center for Nanointegration Duisburg-Essen (CeNIDE), University of Duisburg-Essen, Universitaetsstr, 4-7, Essen, 45141, Germany
$^{e}$ NanoCenter "Nanotechnology and Nanomaterials", G.R. Derzhavin Tambov State University, 392000, Tambov, Russia
$^{f}$ Institute of Solid State Chemistry and Mechanochemistry, Siberian Branch of the Russian Academy of Sciences, Ul. Kutateladze 18, Novosibirsk, 630128 (Russia)

---

## ARTICLE INFO

**Keywords:**
adhesion strength
ab initio calculations
VASP
RF magnetron sputtering
hydroxyapatite coating
silicon-containing

---

## ABSTRACT

A crucial property for implants is their biocompatibility. To ensure biocompatibility, thin coatings of hydroxyapatite (HA) are deposited on the actual implant. In this study, we investigate the effects of the addition of silicate anions to the structure of hydroxyapatite coatings on their adhesion strength via a scratch test and ab initio calculations. We find that both the grain size and adhesion strength decrease with the increase in the silicon content in the HA coating (SiHA). The increase in the silicon content to 1.2 % in the HA coating leads to a decrease in the average crystalline size from 28 to 21 nm, and in the case of 4.6 %, it leads to the formation of an amorphous or nanocrystalline film. The decreases in the grain and crystalline sizes lead to peeling and destruction of the coating from the titanium substrate at lower loads. Further, our ab initio simulations demonstrate an increased number of molecular bonds at the amorphous SiHA-TiO$_2$ interface. However, the experimental results revealed that the structure and grain size have more pronounced effects on the adhesion strength of the coatings. In conclusion, based on the results of the ab initio simulations and the experimental results, we suggest that the presence of Si in the form of silicate ions in the HA coating has a significant impact on the structure, grain size, and number of molecular bonds at the interface and on the adhesion strength of the SiHA coating to the titanium substrate.

---

## 1. Introduction

Different approaches are used to improve the biocompatible properties of metallic implants to increase their lifetime and to decrease the patient's recovery time. The most frequently used approaches are plasma spraying [1], micro-arc oxidation [2], RF magnetron sputtering [3,4], sol-gel, and biomimetics [5].

Biocompatible coatings are mostly based on either pure hydroxyapatite (HA) or HA containing different bioactive elements, such as Si, Mg, and Sr, deposited by plasma-assisted techniques. These coatings are known to possess mechanical properties that are suitable for biomedical applications [5,6]. It was previously reported that doping of pure HA with Si results in the enhancement of its bioactive performance [7-9]. It was also reported that Si-containing coatings have significant effects on cell behaviour [5].

It is known that modifying the implant surface with HA-based coatings promotes better implant osseointegration in comparison to uncoated implants [5]. In spite of controversial studies, which describe results contrary to the beneficial effects of the coatings [10], exploring the different routes for implant surface modification with calcium-phosphate-based (CaP) coatings is still a current research trend.

The adhesion strength is one of the most important properties of the coatings, as it defines the overall success of the implant [11]. However, no structure-adhesion strength relationship has been revealed for thin RF magnetron sputter deposited CaP-based coatings of pure HA and silicon-containing HA (SiHA). In addition, to the best of our knowledge, there are no studies reporting the effect of Si on the adhesion strength of SiHA bioactive coatings.

Although biocompatible ceramic HA coatings have been widely investigated experimentally, theoretical studies are scarce. To the best

---

* Corresponding author:
E-mail address: rsurmenev@mail.ru (R.A. Surmenev).

https://doi.org/10.1016/j.surfin.2020.100727
Received 27 August 2020; Accepted 25 September 2020
Available online 02 October 2020
2468-0230/ © 2020 Elsevier B.V. All rights reserved.

of our knowledge, there are no studies reporting the results of *ab initio* calculations of the adhesion strength of RF magnetron sputter deposited coating, in particular in comparison with the experimental results obtained via adhesion test. However, such studies, which are performed using computer modelling based on the first principles quantum mechanical methods, can predict the sub-nanometre physics and chemistry at the metal-ceramic-coating interface. Moreover, currently, the design of materials based on first principles has become an important, cost-effective tool for predicting the structural, electronic, mechanical, and physicochemical characteristics of materials [12-15].

The objective of this study is, therefore, to investigate the physicomechanical properties of the deposited coatings of pure HA and SiHA and to investigate the influence of the atomic factors on the electronic and physical-mechanical properties of the reconstructed interfaces, as follows: work of adhesion, chemical bond formation mechanisms, integral charge transfer, and charge density distribution.

## 2. Materials and methods

To produce an RF magnetron sputter-deposited coating, first, the precursor powders were synthesized with a tailored chemical and phase composition by mechanochemical synthesis [16]. Powders of Si-substituted HA ($\text{Ca}_{10}(\text{PO}_4)_{6-x}(\text{SiO}_4)_x(\text{OH})_{2-xo}$ $x=0$; 0.5 and 1.72 Mol) were prepared and analysed. The content of silicon in the powders was previously optimized and reported elsewhere [17,18]. The HA and SiHA powder were obtained from the Institute of Solid State Chemistry and Mechanochemistry of the Siberian Branch of the Russian Academy of Sciences (ISSC SB RAS) and are reported by the manufacturer to have an average particle size of ~70 nm. Then, the sputtering targets were prepared by a conventional ceramic technology, which involves the pressing of a powder into pellets followed by annealing. An aqueous solution of polyvinyl alcohol (PVA) was used as the binder. The mixture was compacted at a pressure of 70 MPa and then sintered in air at $1100^\circ\text{C}$ for 1 h. The investigations of the precursor-powders and sintered targets for sputtering were previously described elsewhere [18,19]. It is very important to note that in the case of SiHA powder containing 1.2 and 4.9 at% of Si (corresponds to 0.5 and 1.72 Mol), the preparation of the target resulted in the formation of the calcium phosphate (CaP) phase HA and tricalcium phosphate (TCP), as determined by XRD.

The films were deposited using an RF (13.56 MHz) plasma setup (RF powered electrode is 20 cm in diameter). The RF power of 500 W, the Ar gas pressure (working pressure of 0.4 Pa with a base pressure of $10^{-4}$ Pa) and the distance between the target and substrates were kept at 40 mm for all experiments. The HA and SiHA coatings were deposited for up to 8 h. Si wafers, KBr crystals (as a model compound) and pure titanium were used as substrates. The titanium was treated with an impulse electron beam (SOLO setup, IHSE SB RAS, Tomsk). The treatment conditions are as follows: impulse duration of 50 µs, impulse number – 3, and an energy density of $15\ \text{J•cm}^{-2}$. Optical ellipsometry (Ellipse 1891-S AG, ISP SB RAS, Russia) was used to determine the thickness of the deposited coatings [20], which was calculated as the mean of 10 measurements from each studied sample group. The morphology and chemical composition were studied using a MERLIN field emission scanning electron microscope equipped with energy-dispersive X-ray spectroscopy (EDS) (Carl Zeiss). The structure of the HA coatings was examined using X-ray diffraction (XRD) (Shimadzu XRD-7000) and CuKα radiation at 40 kV with a current of 40 mA and at an incidence angle of $2^\circ$ (2θ range from $5^\circ$ to $90^\circ$ with a step size of $0.01^\circ$). The average crystallite size was calculated using Scherrer's equation from the broadening of the diffraction peaks, taking into account the instrument broadening and using the PowderCell 2.4 program. An instrumental broadening of $0.1^\circ$ 2θ was determined by the full width at a half maximum (FWHM) of a highly crystalline silicon powder as standard. As references for the HA and titanium patterns, the standard cards from the ICDD database #9-0432 and #44-1294 were used, respectively. The molecular compositions of the deposited coatings were investigated using Fourier transform infrared spectroscopy (FTIR, Bruker Vertex 70; 400-4000 cm⁻¹; resolution 4 cm⁻¹; averaging of 20 scans). All the spectra were collected over a range from 400 to 4000 cm⁻¹ at a resolution of 4 cm⁻¹. A scratch test was performed using a CSEM Micro Scratch Tester. The parameters used in the experiments were as follows: a linearly increasing load on the indenter (200 µm in radius) from 0.01 to 15 N; a scratch length of 10 mm; and a normal pressure rate of $15\ \text{N min}^{-1}$. The critical load, at which the delamination of the coating from the substrate began, was characterized using the friction coefficient (FC).

The first-principles calculations were performed with the Vienna *ab initio* simulation package (VASP) [21-25] using the Perdew-Burke-Ernzerhof (PBE) generalized gradient approximation (GGA) [26,27] and a plane wave energy cut-off of 500 eV. For the elements, the valence electron configurations were $1\text{s}^1$ for hydrogen, $[\text{Ne}]\ 3\text{s}^23\text{p}^3$ for phosphorus, $[\text{Ar}]\ 4\text{s}^2$ for calcium, $[\text{He}]\ 2\text{s}^22\text{p}^4$ for oxygen, $[\text{Ne}]\ 3\text{s}^23\text{p}^2$ for silicon, and $[\text{Ar}]\ 3\text{d}^34\text{s}^1$ for titanium. The total energy in the calculations is converged to within 0.01 eV, and a $6\ \times\ 6\ \times\ 1\ \Gamma$-centred k-point grid is used for k-point sampling. The crystal structures are visualized by the VESTA 3 program [28].

## 3. Results and discussion

Typical SEM images of the SiHA coatings (1.2 and 4.6 at% Si) are shown in Fig. 1, which allows the surface grain structure to be revealed. The decrease in the grain size according to the obtained SEM images correlates well with the decrease in the crystallite size according to the X-ray diffraction results (Fig. 2a) [29].

It is seen in the Fig. 2a that pure HA coating reveals <001> texture, which is typical for RF-magnetron sputter deposited coating [30]. In addition, the increase of the content of Si in the coating results in the decrease of the (002) plane (2θ at $25.9^\circ$) intensity of the HA coating. In further, there is no peak at $25.9^\circ$ in case of the coating with the content of 4.6 at% Si. The absence of an "amorphous hump" in the XRD pattern for the (4.6 at.% Si) SiHA coating is similar to that seen in XRD-patterns for commercial plasma-sprayed HA coatings [1]. These observations allow revealing that Si significantly affects the coating structure and the increase of its content results in the decrease of the coating degree of crystallinity, which is also found elsewhere [31]. A possible mechanism is that Si atoms can accumulate on the surface of HA crystallites, as well as Si can be integrated into the structure of HA in the form of orthosilicate anions $\text{SiO}_4^{4-}$, replacing phosphate anions $\text{PO}_4^{3-}$. Thus, the segregation of Si atoms on the surface of HA crystallites leads to the decrease in their growth rate (Table 1), which results in the decrease in the average grain size from $(150\pm15)$ to $(70\pm5)$ nm (Fig. 1a-c) with the increase of the Si content in the coating from 0 to 4.6 at%. Moreover, the increase in the Si content to 4.6 at% results in the formation of a nanocrystalline or X-ray amorphous coating (Fig. 2a).

The results of the X-ray diffraction correlate well with the IR-spectroscopy results (Fig. 2b). All the $\text{PO}_4^{3-}$ bonds, which are typical for HA, are observed [32,33]. However, the increase in the Si content in the HA coatings results in the distortion of the phosphate groups' absorption bonds and, thus, increases their structural disorder. In the case of pure HA coating, all the bonds assigned to phosphate groups are well-resolved. However, in the case of 4.6 at% of Si, it is not observed, which is in good agreement with the fact that the addition of Si results in the decrease of the HA grain size and the formation of an X-ray amorphous or nanocrystalline coating (Fig. 2a). The typical EDS-spectrum of the SiHA coating (1.2 at% Si) is presented in Fig. 2c.

It is known that the mechanical properties of a biocompatible coating on the implant surface play a decisive role in its success. Therefore, the effect of the silicon content in the HA coating on its adhesion strength was studied via a standard scratch test complemented by first-principles calculations.

Our scratch test experiments demonstrate a relationship between

![](./images/812560081290788864_1.jpg)

a) SiHA coating (4.6 at% Si)

![](./images/812560081290788864_2.jpg)

b) SiHA coating (1.2 at% Si)

![](./images/812560081290788864_3.jpg)

c) HA coating

Fig. 1. SEM-images of HA coatings with different contents of silicate groups deposited on the surfaces of Ti treated with an impulse electron beam.

the applied load and the friction coefficient (FC) under loading of the diamond indenter. We find significant fluctuations in the FC that are associated with the microstructure of the deposited coating [34] (Fig. 3). A careful analysis of the results reveals deformation behaviour during the destruction of the coatings. In the case of the HA coating, the FC value increases at relatively low normal loads and reaches a constant value of ~ 0.75 for a load exceeding 6 mN. The value of the critical load ($L_c$) at the time when the deposited coating begins to peel off from the substrate for HA coatings is ~ 5.85 N, and in the case of SiHA (1.2 at% Si), it is ~ 5.5 N.

The experimental results allow us to establish that the destruction of the HA coating occurs via the cohesive mechanism, which is subsequently accompanied by peeling of the coating from the substrate along the scratching direction. In the case of SiHA coatings containing 1.2 at% Si, a local destruction of the SiHA (1.2 at% Si) coating is found along the edges of the scratches at high loads. In addition, the destruction of crystalline SiHA (1.2 at% Si) coatings occurs via the plastic deformation mechanism, which is in accordance with the results reported elsewhere [17].

Peeling of the SiHA coating (4.6 at% Si) is observed at lower loads, which is consistent with the decrease in the grain size, which indicates that an increase in the Si content in the coating reduces the adhesion strength as a result of an increase in the internal microstress. Thus, a higher Si content in the HA coating leads to an increase in the indenter penetration depth into the coating and a greater loss of the coating during scratching due to wear, which is in good agreement with the X-ray diffraction analysis results. The differences in the microstructures of the deposited coatings determine the various behaviours of the studied materials, which are connected with the microstress caused by the application of the normal load of the indenter on the coating surface [29]. As shown in Fig. 3, in addition to the formation of the pile ups, peeling and destruction of the HA coating during scratching is observed, whereas in the case of SiHA coatings, the material is removed from under the indenter in the direction of its movement; thus, fewer cracks along the scratching direction occur compared to pure HA films.

The decrease in the adhesion strength with the increase in the Si content can most probably be associated with the increase in the microstress in the coating, the increase in the number of structural defects and incoherent interfaces, which is confirmed by the coating microstructure results obtained by XRD diffraction [35]. It is seen from the XRD results that the higher the content of Si, the less crystalline coatings are deposited. In addition, IR-spectra reveal that the increase of the content of Si makes the resolution of P-O bands in the wave number range 900-1100 $cm^{-1}$ impossible and signifies the increase of the internal defects in the coating.

The adhesion strength and deformation mechanisms of the coating at the interface are influenced not only by the coating microstructure but also by the interatomic interaction between the bioceramic coating and the metallic substrate. Therefore, to obtain further insight in the adhesion mechanism between titanium and the HA or SiHA coatings, we systematically study the interatomic interaction at the substrate-coating interface by using density functional theory (DFT) calculations.

In this work, we used the interface formed between the most stable HA (001) and rutile ($rTiO_2$) (110) surfaces [36-38] in an amorphous state. The initial configurations of 44-atom HA (001) and 72-atom $rTiO_2$ (110) - (1 × 3 × 4) surfaces were cut out from converged and fully optimized hexagonal HA and tetragonal $rTiO_2$ unit cells by the ADF (Amsterdam Density Functional) software package [39]. The selection of the stacking configurations with the minimum total energy for the entire system and the amorphization of HA were performed using the serial version of ReaxFF [40,41] in accordance with the previously reported procedures [42]. In our previous study [42], we confirmed the reliability of the amorphicity of the obtained amorphous calcium phosphate (a-HA) and amorphous titanium dioxide ($a-TiO_2$) systems by comparing the calculated structural features with existing theoretical results and experimental data [43-46].

Based on the relaxation results presented earlier [42], we selected a representative $a-HA/a-TiO_2$ configuration that gave us the best interatomic interaction for the generation of the Si substituted interfaces. Then, using the selected configuration of $a-HA/a-TiO_2$, we created 12 Si doped-$a-HA/a-TiO_2$ interfaces (114-atom supercell) through the substitution of one P atom by one Si atom in each of the six $PO_4$ groups in a-HA (a-SiHA) with the creation of OH-vacancies as charge compensation [47].

For each interface, after optimization using DFT, we calculated the work of adhesion ($W_{ad}$) as the total energy difference between the optimized structure of the interface system and the isolated component slabs (substrate and coating) with the same geometry as that of the optimized interface system divided by the interface surface area [48]. The calculated the $W_{ad}$ of the a-SiHA / $a-TiO_2$ and $a-HA/a-TiO_2$ interfaces; those which showed the best interatomic interaction are listed in

![](./images/812560081290788864_4.jpg)
![](./images/812560081290788864_5.jpg)

![](./images/812560081290788864_6.jpg)

Fig. 2. a) X-ray diffraction patterns; b) IR spectra, HA and SiHA coatings with various Si content; c) EDS-spectrum of the SiHA coating (1.2 at% Si).

<table>
<caption>Table 1<br>Lattice parameters and crystallite sizes calculated for various types of coatings.</caption>
<thead>
<tr>
<th>Type of the coating</th>
<th>Lattice parameters, Å</th>
<th>Crystallite size, nm</th>
</tr>
</thead>
<tbody>
<tr>
<td>HA</td>
<td>a = 9.4351(1)<br>c = 6.9013(2)</td>
<td>28 ± 3</td>
</tr>
<tr>
<td>SiHA (x=0.5) (1.2 at% Si)</td>
<td>a=9.4719(3)<br>c=6.9224(1)</td>
<td>21 ± 5</td>
</tr>
<tr>
<td>SiHA (x=1.72) (4.6 at % Si)</td>
<td>-</td>
<td>Nanocrystalline or X-ray amorphous coating</td>
</tr>
</tbody>
</table>

### Table 2.
As seen, the interactions (absolute value of the obtained $W_{ad}$) for the a-SiHA / a-TiO₂ interfaces are higher than those found for the a-HA/a-TiO₂ interfaces (a 13 % increase on average), thus showing the large influence of the Si dopants on the coating-substrate adhesive bond strength.

To clarify the effects of the Si doping in the a-HA structure on the chemical bonding mechanism at the constructed interfaces, we compare the charge redistribution that arises due to the electronic hybridization between the orbitals of the coating and the substrate using a charge density difference (CDD) visualization, as follows [49]:

$$
\Delta \rho(r)=\rho_{\mathrm{a}-\mathrm{HA} / \mathrm{a}-\mathrm{TiO}_{2}}(r)-\rho_{\mathrm{a}-\mathrm{HA}}(r)-\rho_{\mathrm{a}-\mathrm{TiO}_{2}}(r),
$$

where $\rho_{\mathrm{a}-\mathrm{HA} / \mathrm{a}-\mathrm{TiO}_{2}}(r)$ is the charge density of the total a-HA / a-TiO₂ interface system, and $\rho_{\mathrm{a}-\mathrm{HA}}(r)$ and $\rho_{\mathrm{a}-\mathrm{TiO}_{2}}(r)$ are the charge densities for the isolated a-HA and a-TiO₂ slabs, respectively.

The CDDs with isosurface values of $\pm 0.008 \mathrm{e} / \AA^{3}$ for the a-HA / a-TiO₂ and a-SiHA / a-TiO₂ systems are shown in Fig. 4. For both interfaces, we observe a charge depletion near the O atoms from the a-TiO₂ slabs and a charge accumulation near the Ca atoms, which means that covalent (polar) Ca-O bonds are formed. The same character of the charge transfer is observed between the O atoms from the $\mathrm{PO}_{4}$ groups and the Ti atoms along the Ti-O direction at the interface. Further, it can be seen that the Ti and Ca atoms act as electron acceptors (Lewis acid), whereas the O atoms from the coating and the a-TiO₂ slab act as electron donors (Lewis base) [50].

Based on the visualization of CDD, the doping-induced effects on the bond lengths are analysed as well. For a-HA / a-TiO₂, one strong $\mathrm{Ti}-\mathrm{O}$ bond $(1.83 \AA)$ and three relatively weak covalent $\mathrm{Ca}-\mathrm{O}$ bonds in the range of $2.43 \pm 0.07 \AA$ are detected.

The a-SiHA / a-TiO₂ interface, on the other hand, gives two dominant $\mathrm{Ti}-\mathrm{O}$ bonds $(1.90 \AA$ and $2.22 \AA)$ and three $\mathrm{Ca}-\mathrm{O}$ bonds $(2.34 \AA$, $2.44 \AA$ and $2.46 \AA$), showing the quite strong chemical bonding at the interface.

Moreover, we obtain a high $W_{a d}$ value of $-2.785 \mathrm{~J} / \mathrm{m}^{2}$ for the a-SiHA / a-TiO₂ interface, which agrees with the observation that the number of Ti-O bonds between the surfaces increased due to the substitution, providing that the covalent bonding interactions are stronger than those for the a-HA / a-TiO₂ $\left(-2.429 \mathrm{~J} / \mathrm{m}^{2}\right)$.

The integral charge transfers (ICT) as calculated using the Bader code [51] are found to be -0.467 and -0.346 electrons for the a-HA / a-TiO₂ and a-SiHA / a-TiO₂ interfaces, respectively (Table 2). A negative value for the ICT means that a-TiO₂ receives an electron charge from a-HA. Note that the total charge transfer is insignificant due to the character of bonding at the interface.

Thus, it was found that replacing the phosphate groups with Si anions in the a-HA crystal greatly influences the coating-substrate interaction. Doping leads to an increase in adhesion by $\sim 13 \%$ due to a rise in the amount of interfacial polar covalent Ti-O bonds across the

![](./images/812560081290788864_7.jpg)

Fig. 3. Change in the FC values as a function of the applied load obtained using the scratch test for the HA and SiHA coatings with a Si content of 1.2 and 4.6 at%.

<table>
<caption>Table 2 Work of adhesion calculated with PBE functional.</caption>
<thead>
<tr>
<th>system</th>
<th>a-HA / a-TiO₂</th>
<th>a-SiHA / a-TiO₂</th>
</tr>
</thead>
<tbody>
<tr>
<td>Wₐd (J/m²)</td>
<td>−2.429</td>
<td>−2.785</td>
</tr>
<tr>
<td>ICT (electron)</td>
<td>−0.467</td>
<td>−0.346</td>
</tr>
</tbody>
</table>

![](./images/812560081290788864_8.jpg)

Fig. 4. a) Charge density difference (CDD) for the a-HA/a-TiO₂ interface and b) the a-SiHA/a-TiO₂ interface. The isosurface value is set to ± 0.008 e/Å³. The yellow regions show electron depletion, and the cyan regions represent electron accumulation. The white, red, purple, dark blue, light blue and orange spheres represent the H, O, P, Si, Ca, and Ti atoms, respectively.

interface.

It is important to note that according to the obtained experimental data, compressive microstresses and the microstructures of the HA coatings have key effects on the adhesion strength. However, explicit determination of the effect of the Si doping on the adhesion properties of HA coating based on a Ti substrate is needed, and it is necessary to exclude the influence of the parameters associated with its processing and preparation methods. For this, the use of computer simulations based on the first principles of quantum mechanical methods is highly

suitable.

## 4. Conclusions
We investigated the influence of Si doping on the adhesion strength of hydroxyapatite coatings on titanium substrates. The segregation of Si atoms on the surface of HA crystallites results in a decrease in their growth rate. The decrease in the average grain size in the coatings, according to SEM results, from $(150 \pm 15)$ to $(70 \pm 5)$ nm with the increase in the Si content is in accordance with the decrease in the crystallite size determined by XRD diffraction. The decrease in the adhesion of the HA coatings with the increase in the Si content is connected with the changes of the structures of the films and dete- rioration of their structures. Different deformation and failure me- chanisms of the coatings were observed. In the case of the crystalline HA coatings, failure occurs due to the low cohesion of the coating, whereas the SiHA coating with 1.2 at% Si is deformed in a plastic manner, without any detachment from the titanium substrate. Both elastic and plastic failure mechanisms were observed in the case of the SiHA coatings with a Si content of 4.6 at%; moreover, plastic de- formation was dominant. This work also presents the results of DFT calculations, which were employed for the investigation of the effect of substitutional Si doping in an amorphous CaP (a-HA) structure on the interfacial bonding mechanism between the a-HA coating and an amorphous titanium dioxide (a-TiO₂) substrate. The calculations re- vealed that Si doping leads to an increase in the adhesion by ~ 13 % due to a rise in the number of interfacial polar covalent Ti–O bonds across the interface. Thus, the quantum-mechanical calculation methods made it possible to determine the mechanisms of the forma- tion of interfacial regions in composite materials based on CaPs and titanium.

## Declaration of Competing Interest
The authors declare no competing interests.

## Acknowledgements
The research was conducted at the Tomsk Polytechnic University within the framework of a Tomsk Polytechnic University Competitiveness Enhancement Program grant. The authors also ac- knowledge the support from the Ministry of Science and Higher Education of the Russian Federation (State Project “Science” NoWSWW-2020-0011), and the Russian President’s grant MK-330.2020.8. The work was carried out in part using the Turing HPC infrastructure of the CalcUA core facility of the Universiteit Antwerpen (UAntwerp), a di- vision of the Flemish Supercomputer Centre (VSC), funded by the Hercules Foundation, the Flemish Government (department EWI) and the UAntwerp, Belgium. The authors acknowledge the support of Dr. O. Prymak for the discussion of the results obtained.

## References
[1] R.B. Heimann, Plasma-Sprayed Hydroxylapatite Coatings as Biocompatible Intermediaries Between Inorganic Implant Surfaces and Living Tissue, J Therm Spray Tech 27 (2018) 1212–1237.
[2] E.V. Legostaeva, K.S. Kulyashova, E.G. Komarova, M. Epple, Y.P. Sharkeev, I.A. Khlusov, Physical, chemical and biological properties of micro-arc deposited calcium phosphate coatings on titanium and zirconium-niobium alloy, Materialwissenschaft und Werkstofftechnik 44 (2013) 188–197.
[3] R. Bosco, Eva, R.U. Edreira, J.G.C. Wolke, S.C.G. Leeuwenburgh, J.J.J.P. van den Beucken, J.A. Jansen, Instructive coatings for biological guidance of bone implants, Surf. Coat. Technol. 233 (2013) 91–98.
[4] M.A. Surmeneva, R.A. Surmenev, V.F. Pichugin, N.N. Koval, A.D. Teresov, A.A. Ivanova, I.Yu Grubova, V.P. Ignatov, O. Primak, M. Epple, Adhesion Properties of a Silicon-Containing Calcium Phosphate Coating Deposited by RF Magnetron Sputtering on a Heated Substrate, Journal of Materials Investigation. X-ray, Synchrotron and Neutron Techniques 7 (2013) 944–951.
[5] R.A. Surmenev, M.A. Surmeneva, A.A. Ivanova, Significance of calcium phosphate coatings for the enhancement of new bone osteogenesis – a review, Acta Biomater 10 (2014) 557–579.
[6] R.A. Surmenev, A review of plasma-assisted methods for calcium phosphate-based coatings fabrication, Surf. Coat. Technol. 206 (2012) 2035–2056.
[7] J.R. Henstock, L.T. Canham, S.I. Anderson, Silicon: The evolution of its use in biomaterials, Acta Biomater 11 (2015) 17–26.
[8] E.M. Carlisle, Silicon: A possible factor in bone calcification, Science 167 (1970) 279–280.
[9] E.M. Carlisle, In vivo requirement for silicon in articular cartilage and connective tissue formation in the chick, J. Nutr. 106 (1976) 478–484.
[10] R.A. Surmenev, M.A. Surmeneva, A critical review of decades of research on cal- cium phosphate-based coatings: How far are we from their widespread clinical application? Current Opinion in Biomedical Engineering 10 (2019) 35–44.
[11] L. Sun, C.C. Berndt, K.A. Gross, A. Kucuk, Material Fundamentals and Clinical Performance of Plasma-Sprayed Hydroxyapatite coatings, J. Biomed. Mater. Res. 58 (2001) 570–592.
[12] J. Hafner, Materials simulations using VASP-a quantum perspective to materials science, Comput. Phys. Commun. 177 (2007) 6–13.
[13] E.M. Ann, A.S. Peter, P.D. Michael, R.M. Thomas, L. Kevin, Designing meaningful density functional theory calculations in materials science-a primer Model. and Simul, Mater. Sci. Eng. 13 (2005) 71.
[14] M.K. Niranjan, First principles study of structural, electronic and elastic properties of cubic and orthorhombic, RhSi Intermetallics 26 (2012) 150–156.
[15] R.O. Jones, Density functional theory: its origins, rise to prominence, and future Rev, Mod. Phys. 87 (2015) 689–746.
[16] M.V. Chaikina, N.V. Bulina, A.V. Ishchenko, I.Yu. Prosanov, Mechanochemical synthesis of SiO₄⁴⁻ substituted hydroxyapatite, Part I - Kinetics of interaction be- tween the components, European Journal of Inorganic Chemistry 2014 (2014) 4803–4809.
[17] M.A. Surmeneva, R.A. Surmenev, M.V. Chaikina, A.A. Kachaev, V.F. Pichugin, M. Epple, Phase and elemental composition of silicon-containing hydroxyapatite- based coatings fabricated by RF-magnetron sputtering for medical implants, Inorganic Materials: Applied Research 4 (2013) 227–235.
[18] M.A. Surmeneva, R.A. Surmenev, M.V. Chaikina, A.A. Kachaev, V.F. Pichugin, M. Epple, Phase and elemental composition of silicon-containing hydroxyapatite- based coatings fabricated by RF-magnetron sputtering for medical implants, Inorganic Materials: Applied Research 4 (2013) 227–235.
[19] M.A. Surmeneva, M.V. Chaikina, V.I. Zaikovskiy, V.F. Pichugin, O. Prymak, M. Epple, R.A. Surmenev, The structure of an RF-magnetron sputter-deposited si- licate-containing hydroxyapatite-based coating investigated by high-resolution techniques, Surf. Coat. Technol. 218 (2013) 39–46.
[20] G.H. Bu-Abbud, N.M. Bashara, J.A. Woollam, Thin Solid Films 138 (1986) 27–41.
[21] G. Kresse, D. Joubert, From ultrasoft pseudopotentials to the projector augmen- tedwave method, Physical Review B 59 (1999) 1758–1775.
[22] G. Kresse, J. Hafner, Norm-conserving and ultrasoft pseudopotentials for first-row and transition elements, Journal of Physics: Condensed Matter 6 (1994) 8245–8257.
[23] G. Kresse, J. Furthmüller, Efficient iterative schemes for ab initio total-energy cal- culations using a plane-wave basis set, Physical Review B 54 (1996) 11169–11186.
[24] G. Kresse, J. Furthmüller, Efficiency of ab-initio total energy calculations for metals and semiconductors using a plane-wave basis set, Computational Materials Science 6 (1996) 15–50.
[25] G. Kresse, J. Hafner, Ab initio molecular dynamics for liquid metals, Physical Review B 47 (1993) 558–561.
[26] J.P. Perdew, K. Burke, M. Ernzerhof, Generalized gradient approximation made simple, Physical Review Letters 77 (1996) 3865–3868.
[27] J.P. Perdew, K. Burke, M. Ernzerhof, Generalized gradient approximation made simple, [Errata]. Phys. Rev. Lett. 78 (1997) 1396.
[28] K. Momma, F. Izumi, VESTA 3 for three-dimensional visualization of crystal, vo- lumetric and morphology data, Journal of Applied Crystallography 44 (2011) 1272–1276.
[29] M.A. Surmeneva, T.M. Mukhametkaliyev, A.I. Tyurin, A.D. Teresov, N.N. Koval, T.S. Pirozhkova, I.A. Shuvarin, A.V. Shuklinov, A.O. Zhigachev, C. Oehr, R.A. Surmenev, Effect of silicate doping on the structure and mechanical properties of thin nanostructured RF magnetron sputter-deposited hydroxyapatite films, Surface and Coatings Technology 275 (2015) 176–184.
[30] V.F. Pichugin, R.A. Surmenev, E.V. Shesterikov, M.A. Ryabtseva, E.V. Eshenko, S.I. Tverdokhlebov, O. Prymak, M. Epple, The preparation of calcium phosphate coatings on titanium and nickel-titanium by rf-magnetron sputtered deposition: composition, structure and micromechanical properties, Surface and Coatings Technology 202 (2008) 3913–3920.
[31] E.S. Thian, J. Huang, M.E. Vickers, S.M. Best, Z.H. Barber, W. Bonfield, Silicon- substituted hydroxyapatite (SiHA): A novel calcium phosphate coating for biome- dical applications, Journal of Materials Science 41 (2006) 709–717.
[32] A.A. Ivanova, M.A. Surmeneva, R.A. Surmenev, D. Depla, Influence of deposition conditions on the composition, texture and microstructure of RF-magnetron sputter- deposited hydroxyapatite thin films, Thin Solid Films 591 (2015) 368–374.
[33] A.A. Ivanova, M.A. Surmeneva, I.Y. Grubova, A.A. Sharonova, V.F. Pichugin, M.V. Chaikina, O. Prymak, M. Epple, R.A. Surmenev, Influence of the substrate bias on the stoichiometry and structure of RF-magnetron sputter-deposited silver-con- taining calcium phosphate coatings, Mat.-wiss. u.Werkstofftech. 44 (2013) 218–225.
[34] H. Pelletier, A. Carradò, J. Faerber, I.N. Mihailescu, Microstructure and mechanical characteristics of hydroxyapatite coatings on Ti/TiN/Si substrates synthesized by pulsed laser deposition, Appl. Phys. A 102 (2011) 629–640.
[35] A.A. Ivanova, M.A. Surmeneva, A.I. Tyurin, R.A. Surmenev, Correlation between

structural and mechanical properties of RF magnetron sputter deposited hydro- xyapatite coating, Materials Characterization 142 (2018) 261-269.

[36] H.Z. Zhang, J.F. Banfield, Thermodynamic analysis of phase stability of nanocrys- talline titania, Journal of Materials Chemistry 8 (1998) 2073-2076.

[37] N.H. de Leeuw, A Computer Modelling Study of the Uptake and Segregation of Fluoride Ions at the Hydrated Hydroxyapatite (0001) Surface: Introducing a $Ca_{10}(PO_{4})_{6}(OH)_{2}$ potential model, Phys. Chem. Chem. Phys. 6 (2004) 1860-1866.

[38] N. Almora-Barrios, K.F. Austen, N.H. de Leeuw, A Density Functional Theory Studyof the Binding of Glycine, Proline and Hydroxyproline to the Hydroxyapatite (0001) and (0110) Surfaces, Langmuir 25 (2009) 5018-5025.

[39] G. te Velde, F.M. Bickelhaupt, E.J. Baerends, C. Fonseca Guerra, S.J.A. van Gisbergen, J.G. Snijders, T. Ziegler, Chemistry with ADF, Journal of Computational Chemistry 22 (2001) 931-967.

[40] K. Chenoweth, A.C.T. van Duin, W.A. Goddard, ReaxFF reactive force field formolecular dynamics simulations of hydrocarbon oxidation, Ibid 112 (2008)1040-1053.

[41] A.C.T. van Duin, S. Dasgupta, F. Lorant, W.A. Goddard, ReaxFF, a reactive forcefield for hydrocarbons, The Journal of Physical Chemistry A 105 (2001)9396-9409.

[42] I.Y. Grubova, M.A. Surmeneva, S. Huygh, R.A. Surmenev, E. Neyts, Density func- tional theory study of interface interactions in hydroxyapatite/rutile composites forbiomedical applications, The Journal of Physical Chemistry C 121 (2017)15687-15695.

[43] H. Wu, D. Xu, M. Yang, X. Zhang, Surface structure of hydroxyapatite from simu- lated annealing molecular dynamics simulations, Langmuir 32 (2016) 4643-4652.

[44] S.V. Dorozhkin, Amorphous calcium orthophosphates: nature, chemistry and bio-medical applications, International Journal of Materials and Chemistry 2 (2012)19-46.

[45] K. Kaur, C.V. Singh, Amorphous $TiO_{2}$ as a photocatalyst for hydrogen production: aDFT study of structural and electronic properties, Energy Procedia 29 (2012)291-299.

[46] I. Manzini, G. Antonioli, D. Bersani, P.P. Lottici, G. Gnappi, A. Montenero, X-ray absorption spectroscopy study of crystallization processes in sol-gel-derived $TiO_{2}$, Journal of Non-Crystalline Solids 192-193 (1995) 519-523.

[47] I.Y. Grubova, M.A. Surmeneva, S. Huygh, R.A. Surmenev, E.C. Neyts, Effects of silicon doping on strengthening adhesion at the interface of the hydro- xyapatite-titanium biocomposite: A first-principles study, Computational Materials Science 159 (2019) 228-234.

[48] M.W. Finnis, The theory of metal-ceramic interfaces, Journal of Physics: Condensed Matter 8 (1996) 5811-5836.

[49] J.P. Sun, J. Dai, Y. Song, Y. Wang, R. Yang, Affinity of the interface between hy- droxyapatite (0001) and titanium (0001) surfaces: a first-principles investigation, ACS Applied Materials & Interfaces 6 (2014) 20738-20751.

[50] F. Labat, P. Baranek, C. Domain, C. Minot, C. Adamo, Density functional theory analysis of the structural and electronic properties of $TiO_{2}$ rutile and anatase polytypes: Performances of different exchange-correlation functionals, The Journal of Chemical Physics 126 (2007) Art. N 154703 [12 p.].

[51] E. Sanville, S.D. Kenny, R. Smith, G. Henkelman, An Improved Grid-BasedAlgorithm for Bader Charge Allocation, Journal of Computational Chemistry 28(2007) 899-908.
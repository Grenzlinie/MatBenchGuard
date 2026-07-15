# Density functional study of structural defects in h-BNC₂ sheets

This content has been downloaded from IOPscience. Please scroll down to see the full text.

2013 J. Phys.: Condens. Matter 25 025304

(http://iopscience.iop.org/0953-8984/25/2/025304)

View the table of contents for this issue, or go to the journal homepage for more

Download details:

IP Address: 128.248.155.225
This content was downloaded on 31/01/2014 at 19:16

Please note that terms and conditions apply.

# Density functional study of structural defects in h-BNC₂ sheets

Pooja Srivastava and Prasenjit Sen

Harish-Chandra Research Institute, Chhatnag Road, Jhunsi, Allahabad 211019, India

E-mail: prasen@hri.res.in

Received 12 September 2012, in final form 13 November 2012
Published 6 December 2012
Online at stacks.iop.org/JPhysCM/25/025304

## Abstract
Structure, energetics, electronic and magnetic properties of single and double vacancies and Stone–Wales defects in h-BNC₂ sheets have been calculated using the planewave pseudopotential method within density functional theory. The formation energy of a defect strongly depends on its location within the sheet. In some cases, though not all, the energy ordering of various defects can be rationalized in terms of the strengths of various bonds that are broken or created during the defect formation. Single vacancy defects have rather low migration barriers, and the energy cost of double vacancies is smaller than that of two isolated single vacancies. Barriers of formation for Stone–Wales defects at the interfaces are large, but those for healing these defects are quite small. Therefore, they can heal easily even at moderate temperatures. Thus, double vacancies are the most likely defect structures in these sheets.
Many of the defects possess finite magnetic moments. Unlike BN sheets and graphene, some of the double vacancies and Stone–Wales defects are also found to possess finite moment.

S Online supplementary data available from stacks.iop.org/JPhysCM/25/025304/mmedia

(Some figures may appear in colour only in the online journal)

## 1. Introduction
Isolation of two dimensional (2D) graphene sheets [1] generated a lot of excitement, as its unusual properties make it an attractive candidate for various applications [2, 3]. However, the absence of a band gap in graphene is a disadvantage, since this leads to a poor on–off ratio in graphene-based field effect transistors [2]. Many different approaches have been suggested, both experimentally and through theoretical calculations, to open a gap in the electronic bands of graphene. These include preparing graphene nanoribbons [4, 5], growing graphene on substrates such as hexagonal BN (h-BN) [6] or SiC [7–9], sandwiching a graphene layer between two h-BN layers [10] etc. A number of workers studied mechanical and electronic properties of hybrid h-BNC systems [11–15]. Recently, Ci *et al* [16] have successfully synthesized bi- and tri-layers of such hybrid h-BNC sheets in which each layer contains all three types of atom. Electrical conductivity of these sheets could be tuned over a wide range by varying the ratio of C and BN in these materials.

This has renewed interest in 2D h-BNC sheets [17–21]. All theoretical studies at various levels of theory [18–20, 22] have indicated that energetically it is favourable for the C and BN regions to completely phase separate in these sheets. However, Ci *et al* [16] found evidence of domains of graphene and BN. These are probably meta-stable structures produced in their chemical vapour deposition experiments due to the kinetics of the growth process. Whatever the ideal structure, h-BNC sheets, like any other real material, are likely to contain structural defects. Indeed, such defects have been observed in graphene and h-BN sheets, and they are found to have significant effects on their properties. Single vacancy (SV), double vacancy (DV) and Stone–Wales (SW) defects have been observed in graphene in transmission electron microscope (TEM) and scanning tunnelling microscope (STM) images [23–26]. Some properties of these defects have also been studied theoretically: their formation energies (FEs), magnetic moments and barrier for migration (for SV and DV) or formation (for SW) have been calculated [26]. The migration barrier for SV defects is found to be rather small (1.3 eV), while the FE of a DV defect is much smaller

than that of two isolated SV defects. This suggests that, even at moderate temperatures, DV defects are more likely to be found than SV defects. Theoretical studies have found non-zero magnetic moment on SV defects in graphene. The moment was found to depend on defect concentration [27, 28]. A recent calculation found a moment of $1.7\ \mu_{\mathrm{B}}$ for an SV in a 72-atom cell [29]. However, no long-range order of these moments could be detected down to liquid helium temperatures [32]. The FE energy of an SW defect is $\sim 5$ eV [31]. Formation of SW defects has to overcome a large barrier of $\sim 10$ eV, while the barrier for the reverse process, i.e. to heal the defect, is also quite large, and has been calculated to be in the range of $\sim$3.74–5 eV [26, 33, 34]. Therefore, once such defects are formed, they are likely to survive at room temperature.

SV and multiple vacancy defects have also been observed in h-BN sheets [35–37]. Their properties have been studied theoretically [38–44]. In h-BN also, DV defects are less expensive than SV defects. However, the migration barriers for both B and N vacancies are higher than that for SV in graphene. Both N and B vacancies give finite magnetic moments in h-BN. No SW defects were observed in TEM images of h-BN [37]. It was conjectured that SW defects have large FE in h-BN. While this is perfectly plausible, there can be other explanations as well. Even with a not-so-low FE, if the barrier to heal the defect is small, one is unlikely to find such defects. This is the case with h-BNC sheets, as we will discuss later.

The central point is that an understanding of formation, electronic, magnetic and diffusion properties of defects in h-BNC systems is crucial for their applications. Some efforts have been made in this direction. Barbosa *et al* [45] studied vacancies and anti-site defects in h-BNC₂ using density functional theory (DFT) methods. However, the structure they took for h-BNC₂ is not of the type observed in the experiments of Ci *et al* [16], nor is it the lowest energy structure in which C and BN domains are completely separated. In fact, in view of the recent calculations on the energetics of various structural arrangements of C and BN domains in h-BNC sheets [18–20], theirs is likely a very high-energy structure. Therefore, the relevance of these calculations to real materials is limited. Pruneda has more recently studied anti-site and vacancy defects near the C–N and C–B interfaces in h-BNC sheets [21]. The anti-site defects cost less energy compared to vacancies, and some of these defects are found to have finite magnetic moment. However, neither the migration barrier of these defects, nor the properties of DV or SW defects in h-BNC systems, have been calculated so far. The lesson from graphene is that it is important to have a thorough knowledge of these defects because SV defects may diffuse easily to form DV defects.

In this paper we present the first detailed study of SV, DV and SW defects on an h-BNC₂ sheet. FEs, magnetic moments, diffusion and formation barriers for these defects have been calculated. Properties of h-BNC sheets fundamentally depend on both the composition and arrangement of C and BN regions [16, 18, 20]. We have restricted the composition to equal percentages of C and BN. We have also taken a structure for h-BNC₂ in which C and BN domains are completely separated and have zigzag C–B and C–N interfaces. Earlier works showed that this has the lowest energy [16, 18–20, 22]. In this work we have worked with 64- and 80-atom supercells. In the former there are four zigzag chains of C and BN domains each, and in the latter there are five zigzag chains (figure 1). The energetics of various defects in these two systems follow the same relative ordering, although the energy values are different. Therefore, we present results for the 80-atom cell in detail and mention some numbers for the 64-atom cell. In some cases we have also done calculations on 128- and 192-atom supercells, which will be mentioned later. We should emphasize at this point that, since properties of the pure sheets change with the widths of the C and BN regions, comparing properties of the same defect in two BNC₂ sheets of different widths (e.g. the 64-atom and 80-atom cells we studied) is comparing two fundamentally different systems, and is not the same as what is generally understood as analysing finite size effects in numerical calculations. The rest of the paper is organized as follows. In section 2 we discuss the methods used in our calculations. In different subsections of section 3, we present in detail the results obtained for defects in the h-BNC₂ sheet, discuss their electronic and magnetic properties and present the diffusion and formation barriers for SV and SW defects respectively. Finally, we draw our conclusions in section 4.

## 2. Method

All the calculations were performed within the framework of density functional theory (DFT). The VASP code [46–49] was used for these. The wave functions are expressed in a plane wave basis set with an energy cutoff of 550 eV, and Brillouin zone integrations are performed using a $(9\times 3\times 1)$ $k$-point mesh within the Monkhorst–Pack scheme for an 80-atom supercell. For 64-, 128- and 192-atom supercells we used $(9\times 5\times 1)$, $(9\times 1\times 1)$ and $(5\times 1\times 1)$ $k$-point meshes respectively. Ionic potentials are represented by the projector augmented wave (PAW) potential [50]. The exchange-correlation energy is represented by the gradient corrected (GGA) functional proposed by Perdew, Burke and Ernzerhof (PBE) [51]. An h-BNC₂ sheet is represented by a repeated layer geometry. Layers were separated by a vacuum space equal to $12\ \mathring{\mathrm{A}}$ to avoid any interaction between successive layers. We used a lattice constant of $2.5\ \mathring{\mathrm{A}}$ as found in our earlier calculations [20]. Atomic structures of h-BNC₂ sheets with defects were optimized until the forces on all the atoms were less than $0.01\ \mathrm{eV}\ \mathring{\mathrm{A}}^{-1}$. During the optimization, all internal coordinates of the B, N and C atoms were allowed to relax while the lattice constants were kept fixed.

## 3. Results and discussion

Figure 1(a) shows the labels for various vacancies in the 80-atom cell we have studied: single letters represent single vacancies and double letters represent double vacancies. C1, C2, N1, B2, CC1, CC2, BN1, BN2 and CN are at the C–N

![](./images/813263937133871105_1.jpg)

Figure 1. (a) Single and double vacancy defects studied in the work are marked. (b) The Stone-Wales defects studied here are indicated. Details of their names are given in the text. Black, small grey (pink) and large grey (green) circles represent C, N and B atoms respectively. See text for details.

<table>
<caption>Table 1. Formation energies ($E_f$ in eV), total magnetic moment (in $\mu_B$), and distance between atoms around vacancy ($x$, $y$ and $z$ in $\mathring{A}$) for various SV defects.</caption>
<thead>
<tr>
<th>Defect</th>
<th>Formation energy</th>
<th>Magnetic moment</th>
<th>$x = y$</th>
<th>$z$</th>
</tr>
</thead>
<tbody>
<tr>
<td>C1</td>
<td>6.34</td>
<td>1.40</td>
<td>2.53</td>
<td>2.58</td>
</tr>
<tr>
<td>C2</td>
<td>7.81</td>
<td>2.13</td>
<td>2.51</td>
<td>2.67</td>
</tr>
<tr>
<td>C3</td>
<td>5.84</td>
<td>2.00</td>
<td>2.47</td>
<td>2.68</td>
</tr>
<tr>
<td>C4</td>
<td>7.62</td>
<td>0.00</td>
<td>2.46</td>
<td>2.62</td>
</tr>
<tr>
<td>C5</td>
<td>7.54</td>
<td>2.01</td>
<td>2.47</td>
<td>2.68</td>
</tr>
<tr>
<td>B1</td>
<td>8.63</td>
<td>2.62</td>
<td>2.71</td>
<td>2.60</td>
</tr>
<tr>
<td>B2</td>
<td>7.30</td>
<td>1.90</td>
<td>2.66</td>
<td>2.57</td>
</tr>
<tr>
<td>B3</td>
<td>8.81</td>
<td>3.00</td>
<td>2.65</td>
<td>2.58</td>
</tr>
<tr>
<td>N1</td>
<td>7.37</td>
<td>0.33</td>
<td>2.15</td>
<td>2.37</td>
</tr>
<tr>
<td>N2</td>
<td>7.23</td>
<td>1.00</td>
<td>2.43</td>
<td>2.47</td>
</tr>
<tr>
<td>N3</td>
<td>8.26</td>
<td>1.00</td>
<td>2.41</td>
<td>2.44</td>
</tr>
</tbody>
</table>

interface and C3, C4, N2, B1, CC3, CC4, BN3, BN4 and CB are at the C–B interface. C5 and CC5 are inside the graphene region, and B3, N3 and BN5 are inside the h-BN region. We consider six SW defects each at the C–N and C–B interfaces that are labelled as SW1-N, …, SW6-N, and SW1-B, …, SW6-B respectively. SW1-N, SW2-N, SW5-N and SW6-N represent rotations of CN, CC1, CC2 and BN2 bonds respectively. SW3-N and SW4-N represent clockwise and anti-clockwise rotation respectively of the BN1 bond. Similarly at the C–B interface, SW1-B, SW2-B, SW5-B and SW6-B represent rotations of CB, CC3, CC4 and BN4 bonds respectively. SW3-B and SW4-B represent clockwise and anti-clockwise rotations of the BN3 bond. The bonds in the pristine sheet whose rotations create these defects are shown in figure 1(b).

FEs and induced magnetic moments for single and double vacancies and SW defects are shown in tables 1–3 respectively. The FE for a vacancy defect created by removing $n$ atoms is defined as

$$
E_f = E_{\text{BNC}_2+\text{vac}} + \sum n_X \mu_X - E_{\text{BNC}_2} \tag{1}
$$

where $E_{\text{BNC}_2+\text{vac}}$ and $E_{\text{BNC}_2}$ are the total energies of the h-BNC$_2$ sheet with and without vacancies of $X$ ($X = \text{B}$, $\text{N}$, $\text{C}$) atom(s). $n_X$ is the number and $\mu_X$ is the chemical potential of atom $X$ in its reference state. The sum goes over all the missing atoms. For carbon, boron and nitrogen we have chosen graphene, $\alpha$-boron and $\alpha$-N$_2$ as reference states. For

**Table 2.** Formation energies ($E_f$ in eV) and total magnetic moment (in $\mu_\text{B}$) of various double vacancy defects.

| Defect | Formation energy | Magnetic moment |
|--------|------------------|-----------------|
| CC1    | 6.04             | 0.24            |
| CC2    | 9.58             | 1.33            |
| CC3    | 5.68             | 0               |
| CC4    | 9.82             | 0.4             |
| CC5    | 6.75             | 0               |
| BN1    | 9.70             | 1.56            |
| BN2    | 9.97             | 0.68            |
| BN3    | 10.60            | 0               |
| BN4    | 12.32            | 2.00            |
| BN5    | 11.66            | 1.61            |
| CB     | 8.86             | 1.00            |
| CN     | 9.11             | 0.33            |

**Table 3.** Formation energies ($E_f$ in eV) and total magnetic moment (in $\mu_\text{B}$) for various SW defects.

| Defect | Formation energy | Magnetic moment |
|--------|------------------|-----------------|
| SW1-N  | 5.38             | 0.43            |
| SW2-N  | 4.20             | 0.0             |
| SW3-N  | 5.33             | 0.9             |
| SW4-N  | 6.76             | 0.0             |
| SW5-N  | 5.23             | 1.1             |
| SW6-N  | 8.61             | 0.0             |
| SW1-B  | 6.63             | 0               |
| SW2-B  | 4.26             | 0.31            |
| SW3-B  | 5.21             | 0.14            |
| SW4-B  | 6.90             | 0.46            |
| SW5-B  | 4.51             | 0               |
| SW6-B  | 8.16             | 0               |

the SW defect the FE is
$$
E_f = E_{\text{BNC}_2+\text{SW}} - E_{\text{BNC}_2} \tag{2}
$$
where $E_{\text{BNC}_2+\text{SW}}$ and $E_{\text{BNC}_2}$ are the total energies of the sheet with and without the SW defect. We mainly focus on defects at or close to the C–N and C–B interfaces. Defects deep inside graphene and h-BN regions are expected to have the same properties as the corresponding defects in graphene and h-BN sheets, which have been studied [26] in detail. We have studied some of these for comparison with the existing results and for comparison with the defects at the interfaces.

Creating a vacancy breaks certain bonds in the pristine sheet. However, the atoms around the vacancy may relax and form new bonds. The formation energy of a particular defect depends on the details of the bonds broken and formed. In pure graphene or h-BN all the bonds are equivalent, and therefore there is only one inequivalent C, B or N SV one can create. In h-BNC$_2$, however, there are many inequivalent C, B and N atoms, and the formation energy will depend on the location of the defect in the sheet. We found it difficult to formulate a general rule that explains the ordering of formation energies of all the defects in the h-BNC$_2$ sheet. However, as we discuss in detail below, in some cases, the order of the FEs for various defects can be rationalized in terms of the relative strengths of various pair-wise bonds in the sheet. For this we use the fact that formation of BB and NN bonds are unfavourable [18–20, 22], and that the strengths of the CN, BN, CC and CB bonds decrease in this order [13].

### 3.1. Single vacancies
SV defects in graphene have a rather large FE of 7 eV [26]. A dynamic Jahn–Teller effect saturates two of the three dangling bonds and leaves the system with a magnetic moment of $1.7\ \mu_\text{B}$ [29]. Rearrangement of atoms lead to the formation of a five-membered ring and a nine-membered ring. N SVs cost less energy in h-BN than B SVs. Liu and Cheng [42] find that the magnetic moments due to B and N SVs in h-BN depend on the distance between two nearest neighbour defects. At small separations, B SV gives a moment of $1.5\ \mu_\text{B}$. At large separations, both give $1\ \mu_\text{B}$. Si *et al* [43], however, find different results. In their calculations, N and B SVs in h-BN give 1 and $3\ \mu_\text{B}$ respectively, independent of the defect concentration. The relaxations of atoms around the two defects are also different. Three B atoms around an N SV move closer to each other, while the N atoms around a B vacancy move away from each other.

According to the ordering of the bond strengths mentioned earlier, it should be easier to create C vacancies at the C–B interface than at the C–N interface since a CB bond is weaker than a CN bond. Indeed, $E_f(\text{C}1) > E_f(\text{C}3)$. We also find $E_f(\text{C}2) > E_f(\text{C}4)$. A possible reason for this is the following. As Tang *et al* [52] have argued, in a BNC sheet, there is charge transfer of 0.2 e from the bonding $\pi$ states of the C network in the graphene domain to the B p$_z$ states at the C–B interface. Conversely, there is a charge transfer of 0.1 e from the N p$_z$ states to the anti-bonding $\pi^*$ states of the C network at the C–N interface. In either case, the CC bond next to the interface is weakened compared to its strength in a pure graphene network, but it is weakened somewhat more at the C–B interface than at the C–N interface since charge transfer is larger at the former. Therefore, the C3–C4 bond is weaker than the C1–C2 bond, explaining the energy ordering $E_f(\text{C}2) > E_f(\text{C}4)$. Similar to a recent study [21], we have also found that SV defects at the interfaces cost less energy than similar defects away from them. Thus $E_f(\text{C}1) < E_f(\text{C}2)$ and $E_f(\text{C}3) < E_f(\text{C}4)$. For C5, deep inside the C domain, FE is 7.54 eV, close to the cost of an SV in pure graphene [30]. In h-BNC$_2$ also, rearrangement of atoms takes place around SV defects. However, the details of such rearrangements depend on the specific defect site. In **figure 2** we have shown the relaxed geometries around SV defects at the interfaces. $x$, $y$ and $z$ are the distances between various pairs of atoms. At the C–N interface, atoms around C vacancies (C1 and C2) move slightly apart. In pristine h-BNC$_2$, the distances $x$, $y$ and $z$ around C1 are 2.44, 2.44 and 2.5 Å respectively. After creation of the C1 vacancy these become 2.53, 2.53 and 2.58 Å respectively (**figure 2(a)**). At the C–B interface, atoms immediately next to the vacancy come closer to each other. In pristine h-BNC$_2$, distances $x$ and $y$ around C3 are both 2.56 Å, and after creation of the C3 vacancy they become 2.47 Å (**figure 2(b)**). Distance $z$ in this case increases from 2.5 Å in the pristine sheet to 2.68 Å in the presence of the C3

![](./images/813263937133871105_2.jpg)

Figure 2. Fully relaxed structures for (a) C1, (b) C3, (c) N1 and (d) B1 SV defects. $x$, $y$ and $z$ are distances between various atom pairs that are given in table 1. Black, small grey (pink) and large grey (green) circles represent C, N and B atoms respectively.

vacancy defect. Such distances around all the SV defects are given in table 1.

The situation is slightly different around B and N vacancies. It is easier to create these SVs next to the interface rather than right at the interface: $E_f(\text{B2}) < E_f(\text{B1}) < E_f(\text{N2}) < E_f(\text{N1})$. Similar to the case in h-BN [39, 40], N vacancies cost less energy than B SVs in h-BNC$_2$. $E_f(\text{N1}) < E_f(\text{B1})$, $E_f(\text{N2}) < E_f(\text{B2})$ and $E_f(\text{N3}) < E_f(\text{B3})$. As in h-BN, atoms around N and B SVs relax significantly, affecting considerably the final electronic and magnetic properties of the system. At the C–N interface, $x$, $y$, and $z$ in pristine h-BNC$_2$ are 2.48, 2.48 and 2.50 Å respectively (figure 2(c)). After creating the N1 SV we find $x = y = 2.15$ and $z = 2.37$ Å. At the C–B interface in pristine h-BNC$_2$, $x$, $y$ and $z$ are 2.60, 2.60 and 2.5 Å respectively. After creating the B1 SV these become 2.71, 2.71 and 2.60 Å respectively (figure 2(d)). Thus atoms around the N1 SV move closer while those around the B1 SV move apart. Other N and B vacancies behave in a similar fashion. As the atoms around N vacancies come closer to each other, there may be weak bonds between them, reducing somewhat the energy cost of the dangling bonds. Atoms around the B vacancies move further apart, precluding such a possibility. This explains why N SV defects have lower FEs than the corresponding B SV defects.

The same systematics for the FEs also hold for the 64-atom supercell. The exact FE numbers, however, are slightly different. For example, the FE of C1 is 6.55 eV, while that for C3 is 5.98 eV. Those for C2 and C4 are 7.73 and 7.57 eV respectively. FEs for the C3 defect have been calculated for 128- and 192-atom supercells also, and the values are 5.68 eV and 5.65 eV respectively. The FE of C3, therefore, decreases with increasing widths of the C and BN regions in the size range of systems we have studied. All our results for the 64-atom supercell are given as supplementary information (available at stacks.iop.org/JPhysCM/25/025304/ mmedia).

The final point we want to discuss in this section is how the FEs would change if the graphene–BN phase boundary were to be slightly different from the zigzag interface we have considered. A full treatment of such realistic systems is computationally quite expensive and will be the subject of a future project. Here we give some indicative results. We consider slightly altered atomic structures near the phase boundary within the constraint of a BNC$_2$ stoichiometry in the two following ways: (i) one pair of C1 and N1 atoms is interchanged; (ii) one pair of C3 and B1 atoms is interchanged. In the first case, if the C1 atom is removed the FE is 5.58 eV, and if the N1 atom is removed the FE is 7.37 eV. In the latter case, if the C3 atom is removed the FE is 6.76 eV, and if the B1 atom is removed the FE is 9.23 eV.

### 3.2. Double vacancies

In graphene, atoms around DVs rearrange without leaving behind any dangling bonds, and, instead of four hexagons, two pentagons and one octagon are formed (5–8–5 defect). A rotation of one of the bonds in the octagon can give rise to three five-membered rings, and three seven-membered rings (555–777 defect). A further transformation of this 555–777 defect due to rotation of a bond can lead to a 5555–6–7777 defect. The FE of a 5–8–5 defect in graphene is 8 eV. The 555–777 defect has the lowest FE, about 7 eV [26]. Strong electrostatic binding between B and N SVs has been found in h-BN [44]. Thus formation of DVs is more likely than that of separated SVs. This is consistent with electron paramagnetic resonance (EPR) measurements in h-BN and BN nanotubes, in which very few SVs are found [53]. DVs in h-BN also lead to 5–8–5 defects [44]. In h-BNC$_2$, as shown in figure 3, not all DVs reduce to 5–8–5 defects. Some DV defects leave behind unsaturated bonds in the structure. For example, CC1 and CC3 vacancies result in 5–8–5 defects, whereas CB, CN and BN DVs do not reduce to 5–8–5 defects. Double vacancies are non-magnetic in graphene, but, due to dangling bonds, in h-BNC$_2$ some double vacancies give rise to magnetism. We discuss this in detail later. We have not studied 555–777 or 5555–6–7777 defects in h-BNC$_2$ for two major reasons. First, for DV near the interfaces, there are many inequivalent bonds that can be rotated. Thus there are

![](./images/813263937133871105_3.jpg)

Figure 3. Fully relaxed structure for (a) CC1, (b) CC3, (c) BN1 and (d) BN3 DV defects. Black, small grey (pink) and large grey (green) circles represent C, N and B atoms respectively.

![](./images/813263937133871105_4.jpg)

Figure 4. Fully relaxed structure for (a) SW1, (b) SW2, (c) SW3, (d) SW4, (e) SW5 and (f) SW6 Stone-Wales defects. Black, small grey (pink) and large grey (green) circles represent C, N and B atoms respectively.

a number of possible new structures that one has to calculate, increasing the computational cost manifold. Second, 555-777 or 5555-6-7777 defects spread over a larger area on the sheet. Therefore, calculating their properties on an 80-atom cell is not possible.

DV defects can obviously be viewed as two neighbouring SV defects. A comparison of tables 1 and 2 shows that in many cases the FE of a DV is very close to the FEs of the individual SVs that make it up, and in all cases it is lower than the sum of the individual SV defects. For example, CC1 is a combination of C1 and C2, which have FEs of 6.34 eV and 7.81 eV respectively. CC1 has an FE of only 6.04 eV, smaller than that of either of the individual SV defects. N1 has an FE of 7.37 eV, but CN, which is a combination of C1 and N1, has an FE of 9.11 eV, much lower than the combined FE of isolated C1 and N1 defects. Similar to SV defects, DV defects right at the interface have smaller FEs compared to similar DV defects away from the interface. For example, FEs of CC1, CC3, BN1 and BN3 are lower than the FEs of CC2, CC4, BN2 and BN4 respectively. Moreover, in some cases, FEs of DV defects follow the same order as the sums of FEs of the two individual SV defects that make them. To illustrate the point let us take the CC DV defects. CC1 is a combination of neighbouring C1 and C2 SV defects. Similarly, CC3 and CC5 are combinations of C3 and C4 and of C5 and C5 defects respectively. The sum of the FEs of C1 and C2 is 14.15 eV. Similarly, the sums of FEs of C3 and C4 and of C5 and C5 are 13.46 and 15.08 eV respectively. Thus $E_f(\text{C3}) + E_f(\text{C4}) < E_f(\text{C1}) + E_f(\text{C2}) < E_f(\text{C5}) + E_f(\text{C5})$. Table 3 shows that $E_f(\text{CC3}) < E_f(\text{CC1}) < E_f(\text{CC5})$. However, this trend is not

valid in every case. For example, $E_f(\text{BN4}) > E_f(\text{BN5})$ and $E_f(\text{CN}) > E_f(\text{CB})$, whereas the sums of individual SV defects suggest the opposite. We would like to reiterate here that, because of the heterogeneity of the system and its finite size, there are many symmetry inequivalent atoms. Atoms around different defects relax very differently, as we have already discussed. Consequently, we find it difficult to form general rules that explain the trend of the observed FEs in every case.

### 3.3. Stone–Wales defects

SW defects involve rotation of bonds by $90^\circ$ about the midpoint of that bond. Rotation of a bond does not give rise to dangling bonds but involves rearrangement of atoms in which existing bonds are broken and new ones are formed. The FE of an SW defect depends upon which bonds are broken and which new bonds are created. Our calculations show that the rotation of a CC bond costs less energy as compared to the rotation of BN bonds, because rotation of BN bonds results in the formation of BB or NN bonds, which are unfavourable [22, 19]. Table 3 shows the formation energies of various SW defects at C–N and C–B interfaces. Final relaxed structures for all the six SW defects considered in this work are shown in figure 4.

At both C–B and C–N interfaces, the ordering of the FEs for various SW defects (SW1–SW6) is the same, so in the following discussion we do not always explicitly write B or N to denote the interface. Similar to SV and DV defects, creation of SW defects at the interface costs less energy than SW defects inside graphene or h-BN domains. Using the fact that BB and NN bonds are unfavourable (wrong bonds), and considering the bonds broken and formed in creating the defects, the FEs for various SW defects can be classified into three groups. The first group contains SW1, SW2 and SW5 because these defects do not create any BB or NN bonds. The second group contains SW3 since this creates one wrong bond, an NN bond in the case of SW3-N and a BB bond in the case of SW3-B. The third group contains SW4 and SW6 since both of these create one NN and one BB wrong bond each. The defects in the first group are expected to have lower FEs compared those in the second group, while the defects in the third group are expected to have the largest FEs. This is, however, without considering the effects of atomic relaxations. FEs of most of the SW defects follow this trend, except for SW1 and SW3, as can be seen in table 3. SW2 has the lowest FE at both the interfaces, and FEs of SW1, SW2 and SW5 are less than those of SW4 and SW6. However, the FE of SW1-B is almost 1.5 eV higher than that of SW3-B. FEs of SW1-N, SW3-N and SW5-N are also comparable. The reason for this is not obvious, but may be related to the relaxation of the atoms and consequent release of strain in the sheet. Both SW4 and SW6 have similar rearrangements of bonds: two BN bonds are broken, and one NN and one BB bond are formed. Still, the FE of SW4 is substantially smaller than that of SW6, probably because the bonds that are being disturbed in SW4 are at the interface, while in SW6 they are slightly away from the interface. As we have remarked before, finding general rules valid in every case turned out to be difficult. As yet another example of this, we take the cases of SW1 defects. Both SW1-N and SW1-B break two CC and two BN bonds and form BN, CC, CN and CB bonds. Yet, SW1-B has a substantially larger FE than SW1-N. This simple minded consideration of relative strengths of different bonds is also not sufficient to rationalize the ordering of FEs of the defects within the first group.

### 3.4. Defect induced magnetism

As mentioned before, an SV in graphene gives a moment of $1.7\ \mu_\text{B}$. In h-BN, a B vacancy gives a moment of $3\ \mu_\text{B}$ while an N vacancy gives a moment of $1\ \mu_\text{B}$. These moments are mostly localized on the atoms surrounding the vacancy. Not surprisingly, SV defects deep inside the graphene and h-BN regions on an h-BN sheet give rise to nearly the same moments. In our calculations, the C5 vacancy gives a moment of $\sim 2\ \mu_\text{B}$, while B3 and N3 vacancies give $3\ \mu_\text{B}$ and $1\ \mu_\text{B}$ respectively. B, C and N vacancies near the interfaces have very different magnetic properties. In particular, at the C–N interface, C1, C2, N1 and B2 vacancies induce magnetic moments of 1.4, 2.1, 0.3 and $1.9\ \mu_\text{B}$ respectively. At the C–B interface, C3, N2 and B1 vacancies produce moments of 2.0, 1 and $2.6\ \mu_\text{B}$ respectively, while the C4 vacancy is non-magnetic. In a previous study on defects in h-BNC sheets, Pruneda [21] found very similar results for magnetic moments on C and N SVs. C1, C3, N1 and N2 defects were found to give moments of 1.8, 2, 0 and $1\ \mu_\text{B}$ respectively. However, B1 and B2 in his study gave 3 and $1\ \mu_\text{B}$, different from what we found. It has to be recalled that the system he studied had five C and seven BN zigzag chains running parallel to the interfaces, different from ours. As we have argued, the properties of these sheets fundamentally depend on the width of the graphene and BN regions. Therefore, this difference should not surprise us.

In most cases, the moment appears on atoms surrounding the defect site. However, for some defects at the C–B interface, a considerable part of the moment appears on C atoms at the C–N interface. For example, for a C3 vacancy, a moment of $0.2\ \mu_\text{B}$ appears on each of the C1 atoms bonded to the N atoms at the other end of the graphene region. In order to check if this apparent long-range effect of the C3 vacancy is an artefact of small cell sizes, we performed the same calculation on larger cells by increasing the widths of the graphene and BN domains, keeping the stoichiometry at $\text{BNC}_2$. On 128- and 192-atom supercells also, we found the same total moment of $2\ \mu_\text{B}$ on a C3 SV, and each C1 atom next to the N atoms has the same moment as in the smaller cell. In these larger supercells, the extents of the cell parallel to the interfaces were kept unchanged, while the widths of the C and BN regions were increased. A 128-atom supercell contains eight C and eight BN chains, while a 192-atom supercell contains 12 C and 12 BN chains. To illustrate the point, we show the distribution of spin density in the h-BNC$_2$ sheet for C1 and C3 defects in figure 5. Clearly, the spin moment is largely confined to the vicinity of the defect in the case of C1 SV (figure 5(a)). In the case of C3 SV (figure 5(b)) there is a much

![](./images/813263937133871105_5.jpg)

Figure 5. Spin density (difference in up and down spin densities) iso-surface plots for (a) C1 and (b) C3 SV defects at an isovalue of $0.014e\ \mathring{A}^{-3}$. Grey (yellow) and dark (blue) surfaces represent positive and negative values of spin density respectively. Black, small grey (pink) and large grey (green) circles represent C, N and B atoms respectively.

larger spin density on the C1 and C2 atoms as compared to the spin on the C3 and C4 atoms in the case of the C1 vacancy. This convinces us that the effect of C3 vacancies is really long ranged, and is a consequence of the electronic properties of the h-BNC₂ sheet. Indeed, such a long-range effect of C vacancies at the C–B interface has been reported by Pruneda [21] for a slightly different system that he studied. This shows that such effects may be generic to hybrid h-BNC sheets, and go beyond the particular composition we have chosen here. What exactly causes this, and whether this is an effect of the variation of the effective potential for the electrons across the sheet, as reported by Pruneda [21], requires further investigation.

In graphene, double vacancies are non-magnetic, but in h-BNC₂ some DVs are magnetic. CC2 induces a magnetic moment of $1.3\ \mu_{\text{B}}$; CC1 and CC4 show very weak magnetization. Other C double vacancies considered in this study are non-magnetic. At the C–N interface the BN1 vacancy induces a magnetic moment of $1.56\ \mu_{\text{B}}$, while at the C–B interface BN3 is non-magnetic. The BN4 vacancy, which is next to BN3, induces a magnetic moment of $2\ \mu_{\text{B}}$, while BN2 induces a moment of only $0.68\ \mu_{\text{B}}$. CN and CB double vacancies at the interfaces have moments of $\sim0.3$ and $1\ \mu_{\text{B}}$ respectively. The details of the magnetic moment in each case depend on the bonds broken and formed, and also the atomic relaxations. The general trend we found for DV defects is as follows. Twofold coordinated C atoms bonded to one C and one N atom develop magnetic moment (CC2), while twofold coordinated C atoms bonded to two C atoms (CC2, CC4, CB, BN1, BN3) or to one C and one B atom do not have magnetic moment. The small moment that develops in the case of CC4 is on the C atoms bonded to N atoms at the C–N interface. Twofold coordinated N atoms that are bonded to one C and one B or to two B atoms also develop magnetic moment. BN1 and BN2 are examples of the former, while CB, BN4 and BN5 are examples of the latter. BN3 is an exception to this rule in which a twofold coordinated N atom does not have any moment. Twofold coordinated B atoms do not develop moment except in BN4, in which two such B atoms have finite moments on them. In the case of CN DV, a tiny moment appears on the C atoms bonded to the B atoms at the far-away C–B interface. Thus, similar to C3 SV, CN and CC4 have a long-range magnetic effect.

Stone–Wales defects are non-magnetic in graphene as all C atoms are threefold coordinated, and there are no dangling bonds, but in h-BNC₂ some Stone–Wales defects induce magnetic moment. SW3 and SW5 at the C–N interface show the largest magnetic moments of 0.9 and $1.1\ \mu_{\text{B}}$ respectively. In the case of SW3-N, the moment is located largely on the C and N atoms in the pentagons and heptagons created by the defect. Only one of the B atoms in the defect region has substantial moment. In SW5-N, the moment is entirely located on the C and N atoms in the mixed heptagon (the other heptagon has C atoms at all corners).

### 3.5. Diffusion of defects

We have already mentioned that the diffusion barrier for an SV on graphene is rather small, while a DV has a much larger diffusion barrier. Creation of SW defects on graphene has a huge energy barrier, but the reverse process also has a substantial barrier of 5 eV, suggesting that once formed these defects will remain stable below $1000\,^{\circ}\text{C}$ [26]. Diffusion of the SV and DV in h-BN has also been calculated [44]. The B SV is found to have a smaller barrier (2.6 eV) compared to an N SV (5.8 eV). A BN DV has a diffusion barrier between 4.5 and 6 eV for different diffusion paths. We calculated the diffusion barrier of SV defects, and the barrier for formation of SW defects at the interfaces on a h-BNC₂ sheet. For estimation of these activation barriers we use the nudged elastic band method (NEB) [54, 55] as implemented in the VASP package. Because there are many possible defects of each type and many different paths a defect can diffuse along, and because NEB calculations are expensive, we studied diffusion barriers of the SV across the interface only. Further, to keep the calculations manageable, we took a straight line path between the initial and final structures in the case of SV migration. For calculation of the formation barrier of SW defects, rotation of bonds in the plane of the sheet was considered. Even if these are not the minimum-energy barriers, our calculations produce an upper bound on them.

A C1 vacancy migrating to the N1 site is labelled as C1–N1, while an N1 vacancy migrating to the C1 site is labelled as N1–C1. Similar labelling is used for C3–B1 and B1–C3 processes. Our calculated diffusion barriers for C1–N1, N1–C1, C3–B1 and B1–C3 process are 1.78, 0.02, 1.12 and 2.3 eV respectively. Thus, as in graphene, diffusion barriers for SV defects are small in h-BNC₂ also, and they are likely to migrate and form DVs or larger vacancies in the sheet even at moderate temperatures.

The formation barrier for SW1-N is 6.55 eV. The barrier for the reverse process is 1.26 eV. For SW1-B these quantities are 8.2 eV and 1.6 eV respectively. Thus in both cases a large barrier has to be crossed in order to form the SW1 defects, but after they are formed the barrier to revert back

to the un-defected structure is rather small. Therefore, these defects can heal easily, and it is unlikely that h-BNC₂ sheets will contain any significant concentration of SW defects at the interfaces at room temperatures or higher. This situation is different from graphene, but is very similar to that in BN nanotubes [56]. The formation barrier and healing barrier for SW defects in BN nanotubes were found to be 5.6 eV and 1.4 eV respectively. This suggests that the energy difference between the un-defected structure and the saddle point is rather large, while that between the saddle point and the defected structure is relatively small. These depend on the details of bonds broken and formed and the strain in the sheet, the latter being particularly important at the saddle point.

## 4. Conclusions
Structural, electronic and magnetic aspects of SV, DV and SW defects in h-BNC₂ sheets have been studied in detail using DFT methods. We have attempted to rationalize the energy orderings of different defects of each type based on the simple idea of relative strengths of various inter-atomic bonds in the sheet. While we have been partially successful, the system is quite complex for an easy generalization which is valid in every case. A few definite conclusions that can be drawn are the following: SV defects migrate easily; DV defects are energetically less costly. The formation barrier for SW defects near the interface is large, but that for healing is small. Thus they are likely to get annealed even at moderate temperatures. It is already known from previous studies that h-BN sheets do not have SW defects. These suggest that the defects most likely to be seen in these hybrid sheets are DV defects over the entire system, and SW defects inside the graphene region. Unlike pure graphene and h-BN, some DV and SW defects give rise to finite magnetic moment in h-BNC₂ sheets. We hope this information will be useful in any future application of these hybrid materials. An experimental attempt at creating an ordered set of defects, and exploration of a possible ordering of the moments on the defects, could open avenues for novel applications.

## Acknowledgments
Calculations were performed at the cluster computing facility and HRI, Allahabad (http://cluster.hri.res.in), and the HPC facility at the IUAC, New Delhi (www.iuac.res.in/hpc).

## References
[1] Novoselov K S, Geim A K, Morozov S V, Jiang D, Zhang Y, Dubonos S V, Grigorieva I V and Firsov A A 2004 *Science* **306** 666

[2] Abergel D S L, Apalkov V, Berashevich J, Ziegler K and Chakraborty T 2010 *Adv. Phys.* **59** 261

[3] Rao C N, Sood A K, Voggu R and Subrahmanyam K S 2010 *Phys. Chem. Lett.* **1** 572

[4] Nakada K, Fujita M, Dresselhaus G and Dresselhaus M S 1996 *Phys. Rev. B* **54** 17954
Miyamoto Y, Nakada K and Fujita M 1999 *Phys. Rev. B* **59** 9858

Ezawa M 1999 *Phys. Rev. B* **73** 045432

Peres N M R, Castro Neto A H and Guinea F 2006 *Phys. Rev. B* **73** 195411

Brey L and Fertig H A 2006 *Phys. Rev. B* **73** 235411

Ouyang Y, Yoon Y, Fodor J K and Guo J 2006 *Appl. Phys. Lett.* **89** 203107

Son Y W, Cohen M L and Louie S G 2006 *Nature* **444** 347

Son Y W, Cohen M L and Louie S G 2006 *Phys. Rev. Lett.* **97** 216803

Barone V, Hod O and Scuseria G E 2006 *Nano Lett.* **6** 2748

Areshkin D A, Gunlycke D and White C T 2007 *Nano Lett.* **7** 204

Han M Y, Özyilmaz B, Zhang Y B and Kim P 2007 *Phys. Rev. Lett.* **98** 206805

[5] Jiao L, Wang X, Diankov G, Wang H and Dai H 2010 *Nature Nanotechnol.* **5** 321

Wu Z-S, Ren W, Gao L, Liu B, Zhao J and Cheng H-M 2010 *Nano Res.* **3** 16

Cai J *et al* 2010 *Nature* **466** 470

Bai J, Duan X and Huang Y 2009 *Nano Lett.* **9** 2083

Datta S S, Strachan D R, Khamis S M and Johnson A T 2008 *Nano Lett.* **8** 1912

Ci L, Xu Z, Wang L, Gao W, Ding F, Kelly K F, Yakobson B I and Ajayan P M 2008 *Nano Res.* **1** 116

Li X, Wang X, Zhang L, Lee S and Dai H 2008 *Science* **319** 1229

Chen Z, Lin Y-M, Rooks M J and Avouris P 2007 *Physica E* **40** 228

Jiao L, Zhang L, Wang X, Diankov G and Dai H 2009 *Nature* **458** 877

Kosynkin D V, Higginbotham A L, Sinitskii A, Lomeda J R, Dimiev A, Price B K and Tour J M 2009 *Nature* **458** 872

[6] Giovannetti G, Khomyakov P A, Brocks G, Kelly P J and van den Brink J 2007 *Phys. Rev. B* **76** 073103

[7] Rollings E, Gweon G H, Zhou S Y, Mun B S, McChesney J L, Hussain B S, Fedorov A, First P N, de Heer W A and Lanzara A 2006 *J. Phys. Chem. Solids* **67** 2172

[8] Zhou S Y, Gweon G H, Fedorov A V, First P N, De Heer W A, Lee D H, Guinea F, Castro Neto A H and Lanzara 2007 *Nature Mater.* **6** 770

[9] Ohta T, Bostwick A, Seyller T, Horn K and Rotenberg E 2006 *Science* **313** 951

[10] Slawińska J, Zasada I, Kosiński P and Klusek Z 2010 *Phys. Rev. B* **82** 085431

[11] Liu A Y, Wentzcovitch R M and Cohen M L 1989 *Phys. Rev. B* **39** 1760

[12] Blase X, Charlier J-C, Vita A D and Car R 1999 *Appl. Phys. A* **68** 293
Blase X 2000 *Comput. Mater. Sci.* **17** 107

[13] Mazzoni M S C, Nunes R W, Azevedo S and Chacham H 2006 *Phys. Rev. B* **73** 073108

[14] Miyamoto Y, Cohen M L and Louie S G 1995 *Phys. Rev. B* **52** 14971

[15] Nozaki H and Itoh S 1996 *Phys. Rev. B* **53** 14161

[16] Ci L *et al* 2010 *Nature Mater.* **9** 430

[17] Pruneda J M 2010 *Phys. Rev. B* **81** 161409

[18] Zhu J, Bhandary S, Sanyal B and Ottosson H 2011 *J. Phys. Chem. C* **115** 10264

[19] da Rocha Martins J and Chacham H 2011 *ACS Nano* **5** 385

[20] Srivastava P, Deshpande M and Sen P 2011 *Phys. Chem. Chem. Phys.* **13** 21593

[21] Pruneda J M 2012 *Phys. Rev. B* **85** 045422

[22] Yuge K 2009 *Phys. Rev. B* **79** 144109

[23] Gass M H, Bangert U, Bleloch A L, Wang P, Nair R R and Geim A K 2008 *Nature Nanotechnol.* **3** 676

[24] Meyer J C, Kisielowski C, Erni R, Rossell M D, Crommie M F and Zettl A 2008 *Nano Lett.* **8** 3582

[25] Ugeda M M, Brihuega I, Guinea F and Gomez-Rodriguez J M 2010 *Phys. Rev. Lett.* **104** 096804

[26] Banhart F, Kotakoski J and Krasheninnikov A V 2011 ACS Nano 5 26

[27] Singh R and Kroll P 2009 J. Phys.: Condens. Matter 21 196002

[28] Yazyev O V 2010 Rep. Prog. Phys. 73 056501

[29] Nanda B R K, Sherafati M, Popović Z and Satpathy S 2012 New J. Phys. 14 083004

[30] Krasheninnikov A V, Lehtinen P O, Foster A S and Nieminen R M 2006 Chem. Phys. Lett. 418 132
El-Barbary A A, Telling R H, Ewels C P, Heggie M I and Briddon P R 2003 Phys. Rev. B 68 144107

[31] Ma J, Alfè D, Michaelides A and Wang E 2009 Phys. Rev. B 80 033407

[32] Nair R R, Sepioni M, Tsai I-L, Lehtinen O, Keinonen J, Krasheninnikov A V, Thomson T, Geim A K and Grigorieva I V 2012 Nature Phys. 8 199

[33] Zobelli A, Ivanovskaya V, Wagner P, Suarez-Martinez I, Yaya A and Ewels C P 2012 Phys. Status Solidi b 249 276

[34] Özçelik V O, Cahangirov S and Ciraci S 2012 Phys. Rev. B 85 235456

[35] Jin C, Lin F, Suenaga K and Iijima S 2009 Phys. Rev. Lett. 102 195505

[36] Suenaga K, Kobayashi H and Koshino M 2012 Phys. Rev. Lett. 108 075501

[37] Alem N, Erni R, Kisielowski C, Rossell M D, Gannett W and Zettl A 2009 Phys. Rev. B 80 155425

[38] Zunger A and Katzir A 1975 Phys. Rev. B 11 2378

[39] Guedes J P, Azevedo S and Machado M 2011 Eur. Phys. J. B 80 127

[40] Yang J H, Kim D, Hong J and Qian X 2010 Surf. Sci. 604 1603

[41] Wanga V, Mab N, Mizusekia H and Kawazoe Y 2012 Solid State Commun. 152 816

[42] Liu R-F and Cheng C 2007 Phys. Rev. B 76 014405

[43] Si M S and Xue D S 2007 Phys. Rev. B 75 193409

[44] Zobelli A, Ewels C P, Gloter A and Seifert G 2007 Phys. Rev. B 75 094104

[45] Barbosa R C, Guimaraes P S and Baierle R J 2010 Thin Solid Films 518 4356

[46] Kresse G and Hafner J 1994 Phys. Rev. B 47 558
Kresse G and Hafner J 1994 Phys. Rev. B 49 14251

[47] Kresse G 1993 Thesis Technische Universität at Wien

[48] Kresse G and Furthmüller J 1996 Comput. Mater. Sci. 6 15

[49] Kresse G and Furthmüller J 1996 Phys. Rev. B 54 11169

[50] Blöchl P E 1994 Phys. Rev. B 50 17953

[51] Perdew J P, Burke K and Ernzerhof M 1996 Phys. Rev. Lett. 77 3865

[52] Tang C, Lingzhi K and Changfeng C 2012 Chem. Phys. Lett. 523 98

[53] Fanciulli M 1997 Phil. Mag. B 76 363

[54] Mills G, Jonsson H and Schenter G K 1995 Surf. Sci. 324 305

[55] Jonsson H, Mills G and Jacobsen K W 1998 Nudged elastic band method for finding minimum energy paths of transitions Classical and Quantum Dynamics in Condensed Phase Simulations ed B J Berne, G Ciccotti and D F Coker (Singapore: World Scientific)

[56] Kim G, Park J and Hong S 2012 Chem. Phys. Lett. 522 79
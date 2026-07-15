![](./images/812739967804506114_1.jpg)
![](./images/812739967804506114_2.jpg)

Subscriber access provided by University of Glasgow Library

Article

# Graphene Nanoscrolls via Electric Field-Induced Transformation of Water-Submerged Graphene Nanoribbons for Energy Storage, Nanofluidic, and Nanoelectronic Applications

Mahnaz Islam, Md. Mushfiqur Rahman, Mokter Mahmud Chowdhury, and Md. Kawsar Alam

*ACS Appl. Nano Mater.*, Just Accepted Manuscript • Publication Date (Web): 03 Sep 2019
Downloaded from pubs.acs.org on September 3, 2019

## Just Accepted

"Just Accepted" manuscripts have been peer-reviewed and accepted for publication. They are posted online prior to technical editing, formatting for publication and author proofing. The American Chemical Society provides "Just Accepted" as a service to the research community to expedite the dissemination of scientific material as soon as possible after acceptance. "Just Accepted" manuscripts appear in full in PDF format accompanied by an HTML abstract. "Just Accepted" manuscripts have been fully peer reviewed, but should not be considered the official version of record. They are citable by the Digital Object Identifier (DOI®). "Just Accepted" is an optional service offered to authors. Therefore, the "Just Accepted" Web site may not include all articles that will be published in the journal. After a manuscript is technically edited and formatted, it will be removed from the "Just Accepted" Web site and published as an ASAP article. Note that technical editing may introduce minor changes to the manuscript text and/or graphics which could affect content, and all legal disclaimers and ethical guidelines that apply to the journal pertain. ACS cannot be held responsible for errors or consequences arising from the use of information contained in these "Just Accepted" manuscripts.

is published by the American Chemical Society. 1155 Sixteenth Street N.W., Washington, DC 20036
Published by American Chemical Society. Copyright © American Chemical Society.
However, no copyright claim is made to original U.S. Government works, or works produced by employees of any Commonwealth realm Crown government in the course of their duties.

# Graphene Nanoscrolls via Electric Field-Induced Transformation of Water-Submerged Graphene Nanoribbons for Energy Storage, Nanofluidic, and Nanoelectronic Applications

Mahnaz Islam,† Md. Mushfiqur Rahman,∥ Mokter Mahmud Chowdhury,‡ and Md. Kawsar Alam*†

† Department of Electrical and Electronic Engineering, Bangladesh University of Engineering and Technology, Dhaka 1205, Bangladesh

∥ School of Electrical and Computer Engineering, Purdue University, West Lafayette, IN 47907, USA

‡ Department of Electrical and Computer Engineering, The University of British Columbia Vancouver, British Columbia V6T 1Z4, Canada

*Corresponding Author: kawsaralam@eee.buet.ac.bd, kawsar.alam@alumni.ubc.ca

ABSTRACT: Nanoscroll is a rolled-up sheet of nanoribbon resembling a spiral papyrus-like multilayer structure, having a broad range of applications from gas and energy storage to nanofluidic and nanoelectronic devices. However, the existing methods of fabrication suffer from complex processing, high energy consumption, abundant impurities, and/or hybrid nanostructures rendering them insufficient to fabricate scalable and high-quality nanoscrolls. Here, we predict that a graphene nanoribbon self-assembles into a nanoscroll under the influence of an external rotating electric field. Using molecular dynamics simulation, we show that electric field-induced alignment of water dipoles originates rotation in a water-submerged graphene nanoribbon. Based on this principle, we propose a setup for nanoscroll formation from water-submerged graphene nanoribbon where one end of the nanoribbon is kept fixed, while the other end orients itself with the rotating electric field and, eventually, self-assembles into a nanoscroll. The nanoscroll is found to be energetically more stable than the initial configuration and retains its stability on removal of the external field as well as the aqueous environment. Findings from concentration profiles of the nanoscroll further confirm the stability as well

as uniformity of its morphology. The formation mechanism is found to be minimally dependent on the applied field's strength and frequency. The proposed method can be used to induce self-assembly of any nanoribbon structure independent of its dimensions and chirality, multilayer nanoribbons as well as to form nanotemplate encapsulated core/shell composites. The proposed method would enable large scale realization of high-quality nanoscrolls from nanoribbons, facilitating fundamental and applied research on nanomaterials.

KEYWORDS: nanoscroll, graphene nanoribbon, self-assembly, molecular dynamics, water dipole moment.

INTRODUCTION

The realization of extraordinary carbon nanomaterials, such as carbon nanotubes (CNT) and graphene, has paved ways for far-reaching novel applications in electronics, energy storage, and bio-inspired systems, to name a few.[¹] Nanoshells, formed by the collapse of stacked materials, are another class of nanomaterials hinted for applications in molecular storage, drug delivery and electronic devices.[²] Analogous to a multi-walled

CNT is a graphene sheet spirally wrapped into a one-dimensional hollow tubular structure called graphene nanoscroll (GNS).⁽³⁾ GNS inherits the excellent thermal and mechanical properties of CNT and graphene as well as exceptional structural,⁽⁴⁾ electronic,⁽⁵⁾ and optical properties.⁽⁶⁾ For example, their unique open-ended structure facilitates a tunable core⁽⁷⁾ such that their interlayer galleries are susceptible to intercalation via donors/acceptors and expand to accommodate the volume of the intercalant,⁽⁸⁾ offering a more efficient utilization of the surface area of graphene sheets. GNSs carry current throughout a continuous scrolled graphene layer in contrast to multi-walled CNTs where conduction occurs only through the outermost layer and thus can support a higher current density (up to $5 \times 10^7$ A/cm).⁽⁹⁾ As a result, GNSs have been explored for revolutionary applications in hydrogen and energy storage,⁽⁸⁾ supercapacitors,⁽¹⁰,¹¹⁾ batteries,⁽¹²⁾ electroactuators,⁽¹³⁾ controllable water/ion channels and nanofluidic devices,⁽¹⁴⁾ electronic devices,⁽⁹⁾ lubrication,⁽¹⁵⁾ etc. Despite such potential and increasing research interests, fabrication of GNS still remains a challenge.⁽¹⁶⁾ Different fabrication techniques such as arc discharge,⁽³⁾ ball milling,⁽¹⁷⁾ chemical routes via ultra-active metal intercalation⁽¹⁸,¹⁹⁾ or

acceptor type compound intercalation⁽²⁰⁾ have been employed in literature. The non-selectivity of the methods, abundant chemical impurities and/or difficulty in controlling scrolling initiation/direction result in low yield and poor quality of the GNSs.⁽¹¹⁾ Moreover, use of harsh reaction conditions such as high-temperature processing and inert atmosphere render the methods energy expensive and unsuitable for large-scale production.⁽¹¹⁾ The existing mechanical routes that utilize interfacial forces such as differential surface strain,⁽⁹⁾ external stress from adsorption of gas atoms,⁽²¹⁾ microexplosion,⁽²²⁾ Langmuir-Blodgett (LB),⁽²³⁾ cold quenching in liquid nitrogen⁽²⁴⁾ give rise to high-quality GNSs but still suffer from low throughput and complex process conditions. Thus, there exists a trade-off between high quality and large quantity in the fabrication methods of GNSs that have been reported so far. More recently, theoretical⁽¹⁶, ²⁵⁻²⁸⁾ as well as experimental⁽¹², ²⁹⁾ works have proposed a purely physical route activated by nanotemplates such as water nanodroplets,⁽²⁵⁾ single or multi-walled CNTs,⁽²⁶⁾ diamond-like carbon nanoparticle,⁽¹⁵⁾ fullerene,⁽²⁸⁾ Si Nanowire⁽²⁷⁾ and metal nanoparticles⁽¹⁶⁾ to induce the self-assembly of graphene into hybrid core/shell composite

structures. The common reason cited to explain the self-assembly is the van der Waals (vdW) interaction between nanotemplate and graphene that induces the encapsulation of the graphene nanoribbon (GNR) onto the template, resulting in the formation of a more stable hybrid structure than the individual ones. However, the formation is critical upon the dimension and position of the nanotemplate used, *e.g.* a CNT radius larger than ~10 Å⁽²⁶⁾ or a Si nanowire radius larger than ~5 Å,⁽²⁷⁾ thus offering less control over the process and final structure achievable. Moreover, there have been no assuring reports on how to remove the template once a scroll structure is obtained. Thus, the cost and difficulty in removing the templates are the main hindrances to large scale production and applications of such processes.⁽¹¹⁾ As a result, a simple, purely physical, room-temperature, high yield method towards the fabrication of a pure GNS without the added complexity of a nanotemplate is missing from the literature.

Using molecular dynamics (MD) simulation, we have proposed such a method that utilizes the electric (E-) field induced orientation of a suspended GNR structure submerged in water to facilitate its self-assembly into a GNS with a hollow core and

homogeneous morphology. We have varied the length, width, and chirality of the initial GNR as well as the strength and angular frequency of the E-field to prove the versatility of the proposed method. We have also shown that the same setup is equally capable to generate core/shell composite structures without the limitation of a critical dimension of the nanotemplate and stable scroll structures from multilayer GNRs.

# RESULTS AND DISCUSSION

Principle of formation. When a static E-field is applied to a dipolar liquid such as water, the polarization of the water molecules causes reorientation of dipoles along the applied E-field direction to attain a more energetically stable state. Daub *et al.*$^{[30]}$ showed that a non-polar nanoparticle immersed in such a dipolar liquid in the presence of an applied static field will also orient itself along the field direction. This alignment process was later rigorously studied for a non-polar CNT by Guo *et al.*$^{[31]}$ Using MD simulation, Guo *et al.*$^{[31]}$ showed that while water molecules orient toward the applied E-field direction due to the alignment of dipoles, they also try to orient parallel to the CNT surface in order to maximize hydrogen bonds. In an effort to satisfy these two conditions, the CNT is forced to orient toward the applied E-field.$^{[31]}$ However, no such study has been conducted for a non-polar GNR submerged in water.


![](./images/812739967804506114_3.jpg)

Figure 1. A freestanding GNR submerged in DI water under an external rotating E-field.

(a) GNR (at time $t_1$) is aligned with XZ plane when an anti-clockwise rotating E-field of

strength 1 V/nm and 10 Gr.p.m angular frequency is applied in the YZ plane. GNR (at

time $t_2$) has been rotating to align with the YZ plane. GNR (at time $t_3$) is almost aligned

Thus, at first, we used MD simulations to study the effect of a rotating E-field on a

freestanding GNR immersed in deionized (DI) water. In particular, a $100.3\ \mathring{A} \times 51.9\ \mathring{A}$

GNR aligned with XZ plane was placed in an $8\ \text{nm} \times 12\ \text{nm} \times 12\ \text{nm}$ box containing

37,091 water molecules and an anti-clockwise rotating E-field of 1.0 V/nm magnitude and

10 Gr.p.m. angular speed was applied in the YZ plane for a simulation time of 30 ns. The

choice of E-field parameters (strength and frequency) have been discussed in a later

section. The results show that the GNR continuously orients itself toward the rotating E-

field performing a spinning motion. This is in agreement with the previous reports on E-

field induced self-assembly of hydrated nanoparticles¹³⁰·³¹¹ and thus validates the choice of our simulation environment. The sequential snapshots showing the angular displacement of the GNR are given in Figure 1 (t₁→t₂→…→t₁₂). The full simulation video of 30 ns may be found in **Supporting Movie 1** (water molecules are not shown for clarity).

It is interesting to note that in an effort to acquire the minimum energy state, the GNR first aligns with the plane of the applied E-field (YZ plane), as shown in Figure 1a, where GNR at time t₁ is the initial state which upon application of an E-field rotates in two planes (GNR at time t₂) until it aligns to the YZ plane (GNR at time t₃). After that, the GNR follows the applied E-field and rotates in an anti-clockwise direction in the YZ plane, as shown in Figures 1b, c, and d. On the other hand, if the E-field is applied in the same plane as the GNR, it simply rotates in its existing plane and performs the spinning motion as soon as the field is applied, as expected. The corresponding simulation video of a freestanding water-submerged GNR aligned to the YZ plane under the influence of a clockwise E-field in the same plane is shown in **Supporting Movie 2**. Of course, an anticlockwise E-field would induce an anticlockwise rotation in the GNR (**Supporting Movie 1**) while a clockwise

field would cause a clockwise spinning GNR (Supporting Movie 2); in the rest of this work, we have employed anticlockwise rotating E-fields, unless mentioned otherwise.

Proposed setup to form nanoscrolls. To utilize the rotating E-field in achieving the formation of a GNS, the setup shown in Figure 2a is proposed. Two fixed substrates can be used to support a GNR with prolonged edges on either side and cantilever beams may be used to suspend the structure while the whole setup is immersed in a dipolar liquid which is not shown in the schematic for clarity. This means that the prolonged edges are restricted in their motion due to surface adhesion with the substrate while the suspended portion is free to move. In our study, the prolonged edges of the GNR have been kept fixed to incorporate the effect of the substrate and the whole setup surrounded by DI water. An atomistic representation of the proposed setup is shown in Figure 2b including the water molecules. For all the studies performed in this work, the GNR structure was placed aligned to the XZ plane with its prolonged edges kept fixed while a rotating E-field was applied in the YZ plane. The length, $L$ of the GNR is measured along the Z direction and the width, $W$ along the X direction on the side without the prolonged edges.

GNRs have been fabricated through patterning by nanolithography,[32] unzipping CNTs by plasma[33] or chemical etching,[34] chemical exfoliation of graphene,[35] nanocutting graphene and nanotubes via catalytic nanoparticles,[36] epitaxial growth of graphene on templated SiC,[37] as well as through direct synthesis by self-assembly of polycyclic aromatic hydrocarbons.[38] The electronic and magnetic properties of GNR are significantly determined by its width, crystallographic symmetry and edge termination[39-43] leading to the development of fabrication tools capable of precisely controlling width and edge geometry of GNRs at the atomic scale.[38] Cai *et al*.[38] reported bottom-up chemical synthesis of atomically precise GNRs with widths less than 10 nm. Bennett *et al*.[44] reported a reliable full layer transfer of bottom-up synthesized GNRs. Moreover, various cutting techniques have been developed to create GNRs with specific shapes.[36]

Numerous works have been reported on the electronic transport through T, L, Y, Z, and cross-

![](./images/812739967804506114_4.jpg)

Figure 2. Proposed setup to induce the self-assembly of a GNR with prolonged edges using an applied E-field. (a) Device schematics: a cantilever beam-based system may be used to suspend a GNR with prolonged edges in a dipolar liquid such as water, with fixed substrates to support the prolonged edges. (b) Corresponding atom based

configuration of the system. To simulate the effect of placing the prolonged edges of
the GNR on a substrate, the prolonged edges are kept fixed in simulation.

shaped GNRs as well as on the resulting nanodevices.[45-49] These methods can be
employed to create the GNR with prolonged edges shown in Figure 2. Alternatively,
GNRs of suitable dimensions and edges can be fused together to create the junctions.[50]

After the required GNR structure is prepared, it can be transferred to a suitable substrate
and the whole setup suspended in water.[44] Obviously, the substrates have to be
separated by more than the width of the GNR and must have a height greater than the
length of the GNR to allow its free suspension. It should be noted that the interfacial
interaction between the substrate and the prolonged edges of the GNR should be
sufficiently strong to hold the edges in place as the GNR transforms into a nanoscroll.

Strong interfacial interactions, attributed to the formation of chemical bonds, between
graphene and common substrates such as metals (e.g. Au/Ni, Si, SiOx) may be
experimentally achieved by using various mechanisms like nanoscale welding[51, 52] and
different annealing protocols of rapid thermal annealing and vacuum annealing.[53]

Chemical bond formation has also been reported for other substrates such as Cu, Ni and SiC.[⁵⁴⁻⁵⁶] In addition, non-bonded vdW interaction between graphene and its target substrate may also be enhanced by techniques such as inserting a PMMA interlayer on top of SiO₂[⁵⁷] and replacing SiO₂ substrate with atomically flat GaAs substrate,[⁵⁸] which may as well be explored in our proposed setup in order to fix the position of the prolonged edges. The rotating E-field can be realized using quadruple electrodes. The four electrodes can be separated from each other by an appropriate gap between opposing electrodes. Self-assembly of the GNR in water requires the presence of an E-field while conduction of an electric current itself is not necessary, thus the quadruple electrodes can be placed outside the proposed setup shown in Figure 2, so that the structure is subjected to the applied E-field but is physically separated from the electrodes. Also, it can be noted that DI water has been used in the setup which is not conductive in its pure form. Once a stable GNS is formed, the prolonged portion can be used as electrical contacts for device applications.[⁵⁹,⁶⁰] It is noteworthy to mention that experimental setups of graphene sheets suspended via electrical contacts on suitable substrates[⁶⁰] as well as immersed in polar

and nonpolar liquids⁵⁹ have been reported , and thus further justify the validity of our proposed setup .

Formation of nanoscroll. A $100.3\ \mathrm{\mathring{A}} \times 94.5\ \mathrm{\mathring{A}}$ zigzag GNR structure was placed in a 12 nm × 12 nm × 12 nm cubic box containing 55169 water molecules as shown in Figure 2b, and an anti-clockwise rotating E-field of 90 Gr.p.m. angular frequency and 1 V/nm strength was applied for a simulation time of 10 ns. Figure 3 shows the evolution in the vdW interaction energy profile of the GNR as a function of simulation time. The inset shows the same energy profile magnified for the first 4200 ps time of this simulation.

Figure 4a shows the snapshots of the resulting self-assembly of the GNR into a scroll structure at different time frames. The simulation video of 10 ns may be found in Supporting Movie 3. It is observed that, in effect, the GNR tries to align itself with the direction of the rotating E-field. The effect of the fixed prolonged edges is that the GNR is fixed

![](./images/812739967804506114_5.jpg)

Figure 3. Time evolution of the vdW interaction energy profile of the GNR when it is

immersed in water and subjected to a rotating E-field (t= 0 to 10 ns), on removal of the E-

field (t= 10 ns to t= 15 ns), further removal of the aqueous environment (t= 15 ns to t= 20

along the X axis in one of its width edges and the other edge is free to rotate. Thus, in

following the rotating E-field, the GNR with fixed prolonged edges (Figure 2) rotates about
<br>

its fixed edge and forms a folded structure in contrast to a freestanding GNR (Figure 1)

which performs a spinning motion. At t= 660 ps (C2, Figure 4a(ii)), the GNR completes

one rotation about its fixed edge with no significant change in its vdW interaction energy

![](./images/812739967804506114_6.jpg)

Figure 4. (a) Snapshots of different configurations formed during the self-assembly of a

$100.3\ \mathrm{\mathring{A}} \times 94.5\ \mathrm{\mathring{A}}$ zigzag GNR with fixed prolonged edges on application of a rotating E-

field of strength 1 V/nm and 10 Gr.p.m. angular frequency at (i) t= 0 ps, (ii) t= 660 ps,

(iii) t= 1100 ps, (iv) t= 2020 ps, (v) t= 2600 ps, (vi) t= 3720 ps, (vii) t= 3910 ps, and (viii)

t= 4109 ps; (b) Final structure (C9) formed on removal of the rotating E-field at t= 4109 ps.

(Figure 3). However, further rotation causes the formation of a single folded, double layered graphene structure (C3, Figure 4a(iii)) accompanied by a sharp fall in the vdW energy profile (Figure 3). Continued rotation of this configuration is also followed by added folds (C4, Figure 4a(iv) and C5, Figure 4a(v)) and corresponding drops in the vdW interaction energy (Figure 3). The process is thus driven by a combination of both the applied E-field and the interwall interaction energy causing self-assembly of the GNR. At t= 3720 ps, the folded GNR forms a round scroll-shaped structure (C6, Figure 4a(vi)). After that, a periodic exchange between two configurations (C7, Figure 4a(vii) and C8, Figure 4a(viii)) is seen while the rotating E-field "squeezes" the round scroll structure resulting in spike-like changes in the vdW interaction energy (Figure 3).

In order to verify which configuration is the final result of this self-assembly process, the applied E-field is removed at t= 10 ns and the trajectory calculated for a further 5 ns. The resulting GNS with a hollow inner core and round well-defined scroll structure is shown in Figure 4b (C9). The constant vdW interaction energy of the final structure as shown in Figure 3 after t= 10 ns reflects its stability. Further, the aqueous environment is removed

at t= 15 ns and the simulation conducted for another 5 ns. The structure retains the scroll topology shown in Figure 4b and a constant vdW interaction energy (Figure 3). Thus, the proposed mechanism results in the formation of a stable GNS that does not unwind into a planar structure on removal of actuating force and the aqueous environment. The full simulation video for 20 ns can be found in the **Supporting Movie 4**. For all the different studies conducted in this work, the final scroll structures shown have been produced after the subsequent removal of the applied E-field and the aqueous environment requiring extended simulations without an E-field and water for a finite amount of time, which we carried out for 5 ns each to ensure the stability of the nanoscroll. As mentioned previously, this corresponds to the flat portions of the energy profile shown in Figure 3, after 10 and 15 ns, respectively. For the remaining studies in this work, the time variation of the energy profiles are shown for the GNR structure under an applied E-field only, for the sake of clarity, and only the average value of the vdW interaction energy of the final structures is mentioned since it remains constant over time (Supporting Information: Figures S2, S4, S6, S8, S10, S11, and S13). Further, it is notable that the proposed mechanism of

nanoscroll formation is not limited by common defects such as point, line and/or planar defects in the precursor GNR. To that end, we considered single vacancy, dual vacancy, and line defects in the initial GNR and confirmed the formation of stable nanoscroll configuration under rotating E-fields by performing several sample calculations. For the rest of this work, we have used GNRs with no defects as the precursor to obtain nanoscroll structure.

To understand the energy origins of the structural evolution onset by the rotating E-field that is depicted in Figure 4a, we calculated the contribution of the bonded and non-bonded interaction energies of the different configurations (C1 to C9) along with their total potential energy. The results shown in Figure 5 are the energy changes relative to the undistorted GNR with fixed prolonged edges (C1, Figure 4a(i)). Bonded interaction energy is the sum of bond stretching potential, angle bending potential, dihedral torsion, and inversion. Non-bonded interaction energy is the sum of vdW and Coulombic interaction energies, while the sum of bonded and non-bonded terms is the total potential energy of the configuration. As studied by Braga et al.,⁴ scroll formation is dominated by two

significant energy contributions- an increase in elastic strain energy caused by the bending of the graphite sheet and the decrease in free energy generated by the vdW interaction of the overlapping graphene layers. The interlayer interaction that is responsible for stabilizing multiwall structures corresponds to an interlayer separation of ~0.34 nm, common to

![](./images/812739967804506114_7.jpg)

Figure 5. Changes in bonded interaction, non-bonded interaction and potential energy terms relative to an undistorted GNR with fixed prolonged edges during its self-assembly induced by a rotating E-field. Configuration number refers to the configurations shown in Figure 4.

all sp² bonded carbon-based structures.[¹] Thus, a scroll structure will be stable if the energy gain from interwall interactions outweighs the strain energy in bending of a

graphene sheet. Any bending of the graphene sheet before a possible overlapping occurs must, therefore, be energy assisted. In our proposed method, the applied E-field provides the required energy in the initial bending of the GNR. As seen in Figure 5, there is an increase in the bonded interaction energy with the bending of GNR indicating decreasing stability. However, when there is significant overlapping of the rotating GNR, there is a sharp fall in the non-bonded interaction energy upon a successful folding of the GNR, so that the overall process yields a more stable configuration than the initial GNR. Thus, on removal of the E-field after the formation of C8 (Figure 4a(viii)), the scroll structure is retained (C9, Figure 4b).

To characterize the scroll structure formed using our proposed method (C9), we calculated the atomic concentration profiles (no. of atoms per unit volume) of the GNS formed along Y and Z directions (Figure 6a). The concentration profiles along a specific direction are calculated by

![](./images/812739967804506114_8.jpg)

Figure 6. Atomic concentration profiles of different molecules involved. (a) Concentration profile of the GNS shown in Figure 4b along the Y and Z directions, plotted against the relative distance from the center of the GNS. The distances $d_1$, $d_2$, and $d_3$ measured along the Y direction are shown in the figure. Distances along Z direction are not shown for clarity. (b) Concentration profile of the initial GNR and final GNS along the Z direction. (c) splitting the cubic box into evenly spaced slices parallel to the corresponding plane and determining the number of target atoms (whose concentration profile is to be calculated) in each slice. The blue solid line represents the concentration profile of the GNS along Y

and the red dashed line along the Z direction. The concentration profiles along the two directions confirm the uniform morphology of the GNS formed by our proposed method.

This is in contrast to previously reported experimental methods of GNS fabrication where the GNSs formed were of poor morphology and ill-defined layers.[9, 19, 20] It is observed that there are five peaks along each curve in Figure 6a. If we follow the front view of the GNS shown in Figure 4b(ii) along, for example, the Z direction from the positive axis to the negative axis, we encounter five graphene layers. Thus, each peak in the concentration profile along a specific axis represents a layer of the GNS and the distance between the adjacent peaks represents the interlayer distance. Here, we define the distances $d_1$, $d_2$, and $d_3$ as the distance between adjacent peaks along each of Y and Z directions, moving from their negative to positive axes (Figure 4b). The distances $d_1$, $d_2$, and $d_3$ measured along the Y direction are shown in Figure 6a. The values of the distances are given in Table 1. All the measured distances in both Y and Z directions are greater than 3.4 Å, which is the shortest interlayer distance of the graphitic allotrope,[1] and thus have entered the strong-adhesive-binding region of the chemical bond. In

addition, the inner ($d_i$) and outer diameter ($d_o$) of the GNS, taken as the distance between the innermost and outermost peaks, respectively, are also shown. The small peak in the concentration profile along Y is attributed to the irregular scroll edge formed where the nanoribbon terminates and hence does not truly represent a complete layer of the scroll.[26] Thus, the corresponding distance measured $d_1$ is ignored in the results shown in Table 1. **Table 1**. Interlayer distances ($d_1$, $d_2$, $d_3$), inner ($d_i$) and outer ($d_o$) diameters along with their corresponding averages ($\bar{d}$ , $\bar{d}_i$, and $\bar{d}_o$) of the GNS formed using our proposed method.

<table>
  <thead>
    <tr>
      <th rowspan="2">Axes</th>
      <th colspan="5">Distance (nm)</th>
      <th colspan="3">Average (nm)</th>
    </tr>
    <tr>
      <th>$d_1$</th>
      <th>$d_2$</th>
      <th>$d_3$</th>
      <th>$d_i$</th>
      <th>$d_o$</th>
      <th>$\bar{d}$</th>
      <th>$\bar{d}_i$</th>
      <th>$\bar{d}_o$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2">Y</td>
      <td rowspan="2">-</td>
      <td>0.359</td>
      <td>0.347</td>
      <td>0.921</td>
      <td>1.903</td>
      <td rowspan="4">0.344<br>8</td>
      <td rowspan="4">0.808<br>2</td>
      <td rowspan="4">1.808<br>0</td>
    </tr>
    <tr>
      <td>2</td>
      <td>3</td>
      <td>9</td>
      <td>8</td>
    </tr>
    <tr>
      <td rowspan="2">Z</td>
      <td>0.347</td>
      <td>0.335</td>
      <td>0.335</td>
      <td>0.694</td>
      <td>1.712</td>
    </tr>
    <tr>
      <td>2</td>
      <td>3</td>
      <td>2</td>
      <td>5</td>
      <td>2</td>
    </tr>
  </tbody>
</table>

Therefore, the concentration profiles further validate the stability of the scroll formed.

Figure 6b shows the concentration profiles along Z direction of the initial GNR (blue solid

line) along with that of the final GNS (red dashed line) representing the reorientation of the atoms along its length. Figure 6c shows the concentration profile of the water molecules along the Y and Z directions in the simulation box after the formation of the GNS. The dip in the water concentration profile at the center represents the hydrophobicity of the formed GNS. The same is also seen in Figure 6d which shows the decrease in the solvent accessible surface area (SASA) of the GNR during its self-assembly into a scroll. Initially, the nanoribbon structure offers a planar, wider area available to the water molecule which decreases as it scrolls into a more closed structure.

Thus, formation of the GNS involves water molecules being pushed out from its inner core. Nonetheless, few water molecules that may remain adhered to the nanoscroll core or interface despite the weak vdW interaction energy between water-GNS may be removed using commonly used drying methods for carbon-based nanostructures, such as vacuum drying in a freezer-dryer followed by vacuum drying in a drying oven.

Varying strength and angular frequency of applied E-field. To predict the effect of E-field parameters on the formation mechanism of a GNS, we analyzed the orientation of

the water dipoles under rotating E-fields of varying strength and angular frequency similar to Rahman et al.[⁶¹] Figure S1a shows the variation of the average dipole strength per water molecule in the X, Y and Z directions under a rotating E-field of strength 1 V/nm and 30 Gr.p.m. When a rotating field is applied in the YZ plane, E-field in the Y and Z directions is varied sinusoidally with a 90° phase difference between them. Since the water dipoles align parallel to the direction of the applied E-field, a similar sinusoidal variation in their orientation along the axes is seen. The norm of the dipole moment vector per water molecule (|p|) is also shown (cyan line), which is a measure of the degree of alignment of the water molecules. In Figure S1b, the variation of |p| for varying strengths of E-field at an angular frequency of 30 Gr.p.m. shows that |p| decreases for weaker E-fields, i.e. the water molecules are less aligned with the direction of the applied E-field.

Thus, it can be predicted that a minimum E-field strength would be required to induce the alignment of the GNR structure. On the other hand, Figure S1c shows that |p| remains constant for a very wide range of frequencies up to an ultra-fast speed of ~1000 Gr.p.m and only decreases after that point. The water dipoles need a finite amount of time to

orient toward the direction of the applied E-field, thus $|p|$ decreases for ultra-fast speeds.

Therefore, relatively lower frequencies (such as in kHz, MHz range) are equally applicable to our proposed setup. Nonetheless, the frequencies used in our study were in the Gr.p.m. range to realize feasible simulation costs since a time step of 1 fs was used in our simulation. Because the dipoles can follow the rotating field at our chosen frequencies, which corresponds to the relatively flat section of Figure S1c (magnified in its inset), the accuracy of the simulation and the feasibility of setup are justified. Moreover, it can be extrapolated from Figure S1c that after a certain arbitrarily high frequency of the applied E-field, the water dipoles would be completely unable to respond to its extremely fast changing direction, and thus the GNR would remain stationary. We have refrained from determining the exact value of this frequency since such high frequencies are difficult to obtain in an experimental setup and thus would be impractical.

To determine the effect of varying E-field strength, we applied E-fields of constant angular frequency equal to 30 Gr.p.m. but varying in strengths from 0.1 V/nm to 1 V/nm at 0.1 V/nm steps to a $100.3\ \mathrm{\mathring{A}} \times 51.9\ \mathrm{\mathring{A}}$ GNR for a simulation time of 10 ns. Our results

confirm that there is, indeed, a minimum strength of the applied E-field required to cause
the GNR to continuously align with it and thus form a nanoscroll. For the structure under
study, the minimum E-field strength required for the formation of a nanoscroll structure is
found to be 0.2 V/nm at an angular frequency of 30 Gr.p.m. **Supporting Movie 5** shows
the trajectories of this GNR under 0.1 V/nm (red) and 0.2 V/nm (cyan) strengths of E-field.

At a lower E-field strength than 0.2 V/nm, the field is not strong enough to cause sufficient
alignment of the water dipoles (Figure S1b) that would induce a complete rotational
motion in the planar GNR. As a result, the free end of the GNR does not come close
enough to its fixed edge to induce any non-bonded vdW interaction within the GNR and
thus, no self-assembly is observed.

From the previous discussion, it can be deduced that the alignment process of a GNR
submerged in water would perform well up to a range of high frequencies since the
average water dipole moment remains constant up to an ultra-high angular frequency. In
order to determine the range of frequencies over which the formation of a GNS can be
obtained, we varied the frequency of the applied E-field from 10 Gr.p.m. to 100 Gr.p.m.

in 10 Gr.p.m. steps and also higher speeds of 150 Gr.p.m. to 350 Gr.p.m. at 50 Gr.p.m steps to a $100.3\ \text{Å} \times 34.9\ \text{Å}$ GNR structure immersed in water. Arbitrarily high angular frequencies such as 1000 Gr.p.m. are not feasible for practical applications and thus have not been used in our study. Our results show that while the trajectory of the GNR during its self-assembly might follow three different regimes depending on the angular frequency of the rotating E-field, the final structure formed is fairly independent of the angular frequency and resembles a scroll structure under all conditions. During the scrolling motion, the GNR can follow the rotating E-field up to a certain angular frequency after which it starts to lag behind. A similar phenomenon was reported for a CNT immersed in water under a rotating E-field.[61] The maximum frequency up to which the GNR is "locked" with the applied E-field is called the locked frequency and for the GNR under simulation, it is about 30 Gr.p.m. Figure 7a shows the snapshots at quarterly time intervals for one time period of each simulation trajectories under 10 Gr.p.m.

![](./images/812739967804506114_9.jpg)

Figure 7. (a) Snapshots showing a $100.3\ \mathrm{\mathring{A}} \times 34.9\ \mathrm{\mathring{A}}$ GNR under rotating E-fields of three different angular frequencies at (i) t= T/4, (ii) t= T/2, (iii) t= 3T/4, and (iv) t= T. GNRs represent the trajectories under $\omega_1$= 10 Gr.p.m. (T= 6 ns), $\omega_2$= 60 Gr.p.m. (T= 1 ns), and $\omega_3$= 300 Gr.p.m. (T= 0.2 ns), respectively. At 10 Gr.p.m. ($\omega_1$), the GNR also represents the predicted position of the E-field since it is below the "locked" frequency; at 60 Gr.p.m. ($\omega_2$), GNR lags the E-field and at 300 Gr.p.m. ($\omega_3$), GNR follows a jerky trajectory. (b) The (cyan), 60 Gr.p.m. (red) and 300 Gr.p.m. (green). The three different trajectories identified during the self-assembly of the GNR are classified according to whether the angular frequency is below the locked frequency (Regime A), slightly above the locked frequency (Regime B) or much higher than the locked frequency (Regime C). The frequencies

selected for representing the three regimes in Figure 7a have been chosen accordingly.

Since 10 Gr.p.m. is below the locked frequency of the GNR under study, it is successfully "locked" with the direction of the applied E-field and thus can also be used to represent the direction of the E-field in each frame. It is observed that the GNRs marked red (60 Gr.p.m.) and green (300 G r.p.m.) lag behind the GNR marked cyan (10 Gr.p.m.) in each snapshot. The GNR marked cyan successfully completes one complete rotation in one time period of the corresponding angular frequency and is also seen to form a double folded structure in the final frame (Regime A). The GNR marked red also follows a rotational motion about its fixed edge, however, is always a certain angle behind the E-field it is trying to follow (Regime B). On the other hand, the trajectory of the GNR marked green shows sudden "jerks" in its motion, such that it does not leave the first quadrant in one time period (Regime C). The superimposed trajectories of the GNR under these three frequencies (10 Gr.p.m. (cyan), 60 Gr.p.m.(red) and 300 Gr.p.m. (green)) can be found in **Supporting Movie 6**. The initial frames clearly distinguish between the complete rotational motion of the cyan and red marked GNRs from the irregular, jerking motion of

the GNR marked green. The simulation video also serves to show that the final structures formed as a result of the trajectories in the three different regimes all resemble a scroll- like formation. While trajectories in regime A and B follow the sequential structural evolution depicted in Figure 4a, the GNR under a very high frequency such as the one marked green suddenly assembles into a scroll structure.

For the frequencies studied in this work, we were able to identify two types of scroll as the final structures, classified according to whether the fixed edge of the initial GNR forms the outer (scroll type A) or inner (scroll type B) edge along the length of the final GNS. For slower frequencies below the locked frequency of the GNR structure under study, we found scroll type A to be predominant (10 and 20 G r.p.m.) while for frequencies in regime B, scroll type B (30, 40, 50 and 60 Gr.p.m.) structures were found more likely. However, the final structure formed under frequencies in regime C were found to be both scroll types A and B. This may be related to their ultrafast, sudden formation after a haphazard, jerky rotation of the initial GNR. Figure 7b shows the final structures formed under two representative frequencies 10 (scroll type A, Figure 7b(i)) and 40 Gr.p.m (scroll type B,

Figure 7b(ii)). The corresponding trajectories are shown in **Supporting Movies 7 and 8**, respectively. The time evolution of vdW interaction energy profile for the GNR under 10 and 40 Gr.p.m. is shown in Figure S2 (Supporting Information). The sharp fall in the vdW profile reflects the stability of the self-assembly process. Further, the average vdW interaction energies of the scroll types A and B under 10 and 40 Gr.p.m. are -6493.59 kJ/mol and -6552.79 kJ/mol, in that order, confirming that both type of scroll formation are of comparable stability. We also calculated their concentration profiles along the Y and Z directions (Figure S3) and measured the interlayer distances (Table S4). From Figure 7b, it is apparent that the two types of scrolls formed appear to be mirror images of each other, and the concentration profiles in Figure S3 confirm that observation. Thus, the concentration profile for scroll type A along Z-axis (Figure S3a-red dashed line) resembles that for scroll type B along Y-axis (Figure S3b-blue solid line). Nevertheless, all the structures formed are stable configurations, further verified by the average interlayer distances ($d$) of the structures under each frequency shown in Table S4, which is more than 3.4 Å.

Varying width for a fixed length of GNR. To investigate the versatility of our proposed setup, we varied the dimensions of the initial GNR as well as its chirality and characterized the resulting scroll formed in each case. Specifically, at first, the length of a zigzag GNR ($L$) was kept fixed at 100.3 Å while its width ($W$) was varied over 17.8 Å to 94.5 Å. A rotating E-field of 20 Gr.p.m. angular frequency and 1 V/nm strength was applied for a simulation time of 15 ns. The resulting final structures formed after the subsequent removal of the E-field are shown in Figure 8a. The full simulation video of the individual simulation trajectories superimposed on each other ($W_1$

![](./images/812739967804506114_10.jpg)

Figure 8. Effects of varying width, length and chirality of the initial GNRs on the final scroll structure. (a) Scrolls formed from initial GNRs with the same length ($L=100.3$ Å) but varying width ($W$). (Left to right) $W_1=17.8$ Å, $W_2=26.2$ Å, $W_3=34.9$ Å, $W_4=43.4$ Å, $W_5=60.4$ Å, and $W_6=94.5$ Å. Both the lateral and front view of the final structures are shown. (b) Scrolls formed from initial GNRs with the same width ($W=44.4$ Å) but varying lengths. (Left to right) $L_1=59.7$ Å, $L_2=86.8$ Å, $L_3=105.2$ Å, $L_4=126.2$ Å, and $L_5=207.4$ Å. Only the front view of the final structures are shown. (c) Scrolls formed from initial

GNRs with approximately the same dimensions but of different chiral angle: (Left to Right) $0^\circ$, $5^\circ$, $10^\circ$, $15^\circ$, $20^\circ$, $25^\circ$, and $30^\circ$. The top row shows a portion of the initial GNR structure while the bottom row shows an oblique view of the corresponding scroll structure.

(blue), $W_2$ (red), $W_3$ (yellow), $W_4$ (green), $W_5$ (purple), and $W_6$ (brown)) may be found in Supporting Movie 9. Since the GNR rolls along the direction of its length, the resulting nanoscrolls each have the same number of scroll-turns but are of different lengths which is equal to the width of the initial GNR. The final structures formed for widths $W_1$ and $W_2$ are of scroll type B while the rest of the widths form scroll type A structures. The scroll type is consistent with the frequency-dependent trajectory regime for each structure at 20 G r.p.m. (explained later). The change in the vdW interaction energy profile of the GNRs under an applied E-field is shown in Figure S4a. Since the vdW interaction energy invariably increases with the increase in the number of atoms in the structure, the profiles shown have been calculated for the vdW interaction energy per carbon atom in the structure. A sharp fall in the energy profile is seen in each case which shows the resulting

scroll structures are more stable than the initial planar ribbon. As explained previously, a sharp fall indicates the formation of a folded structure while nanoscroll formation occurs at the onset of spike-like changes in the energy profile. The profiles for the wider GNRs depict a more visible stepwise change compared to that for the narrower GNRs. This is because a wider GNR forms more slowly than a narrower GNR, and each folded structure (formed in the course of the self-assembly) follows the E-field for a comparatively longer period of time, resulting in a stepwise fall in the vdW interaction energy profile. Figure S4b shows the average vdW interaction energy per carbon atom of the final structure formed after the subsequent removal of the E-field against the corresponding width of the initial GNR. It is observed that the scroll morphology formed for a wider GNR is more stable than that for a narrower GNR, while they have the same number of scroll-turns. The average interlayer distance ($d$) of each structure, measured from their concentration profiles (Figure S5), is ~3.4 Å (Table S5) thus proving the existence of a strong force between the layers.

The variable E-field angular frequency and strength study was repeated for GNR structures of different dimensions. It was found that the minimum E-field strength required to induce self-assembly of a GNR increases with decreasing width of the GNR. For example, for a GNR measuring $100.3\ \mathrm{\mathring{A}} \times 17.8\ \mathrm{\mathring{A}}$ the required minimum E-field strength at an angular frequency of 30 G r.p.m. is 0.4 V/nm. For weaker E-fields at this frequency, the trajectory of the GNR shows that it is unable to follow the rotating E-field due to an irregular, "jerky" path (Supporting Movie 10). This observation is traced back to the increasing disorientation of the water molecules at weaker strengths of E-field (Figure S1b). Since a narrower GNR offers a smaller solvent accessible surface area to the surrounding water molecules it is immersed in, there is less area of contact between the GNR and the water molecules and thus, a higher degree of orientation per water molecule is required to bring about a complete rotation of the GNR. A complete rotation, in turn, is required for the free end of the GNR to come close enough to its fixed end to induce its self-assembly. Although we have used an E-field strength of 1 V/nm elsewhere in this work, much lower strengths of E-field may be sufficient in practical applications depending

on the dimensions of the GNR structure. On the other hand, the locked frequencies for GNRs measuring $100.3\ \text{\AA} \times 17.8\ \text{\AA}$ and $100.3\ \text{\AA} \times94.5\ \text{\AA}$ are found to be 15 Gr.p.m. and 92 Gr.p.m., respectively, accurate to the nearest Gr.p.m. Thus, a wider GNR is able to follow a faster rotating E-field. The range of frequencies over which the different trajectory regimes are identified for different size of the initial GNR is noted in Table S6. The values noted are accurate to the nearest 10 (for frequencies less than 100 Gr.p.m.) or 50 Gr.p.m. (for frequencies greater than 100 Gr.p.m.) angular frequency, since we have carried out simulations in these frequency steps. Since the locked frequencies of GNRs of different dimensions are all in the Gr.p.m. range, any rotational E-field of frequency lower than these may be used to obtain a locked, rotational alignment of the GNR (Regime A) to result in its self-assembly into a stable scroll structure (scroll type A). Thus, in practical applications, suitable low-frequency E-fields may be used to achieve the self-assembly of a GNR into a nanoscroll using our proposed method to avoid the complexity of applying a high-frequency E-field. As a matter of fact, at extremely high frequencies of the E-field, GNSs cannot be obtained due to the previously mentioned non-responsiveness of the

GNR at such ultra-fast rotating fields. Thus, Regime C in Table S6 is valid up to a finite albeit arbitrarily high E-field frequency, after which the GNR remains stationary even in the presence of an applied field. Since such high frequencies are impractical for experimental realization and do not serve a significant purpose in obtaining the formation a GNS, we have not identified their exact values in Table S6.

Varying length for a fixed width of GNR. Next, we varied the length of the initial GNR over 59.7 Å to 207.4 Å while its width was kept fixed at 44.4 Å and subjected each to a rotating E-field of 30 Gr.p.m. angular frequency and 1 V/nm strength for 10 ns. The resulting final structures formed after the subsequent removal of the E-field are shown in Figure 8b. It is observed that structures for $L_1$ and $L_5$ resemble scroll type B while the middle lengths form scroll type A structures. The sharp fall in the vdW energy profile shown in Figure S6a for each GNR represents the stability of the final structures for each length. The stepwise change for the longer GNRs relates to their longer time of formation, as explained previously. Thus, both single-layered and multi- layered GNS can be formed using our proposed method. The average vdW interaction energy per carbon atom of the

scrolls formed for GNRs with varying lengths is shown in Figure S6b, which reflects the increasing stability of the scroll morphology as the number of scroll-turns increases. An increasing length, of course, causes a higher number of scroll-turns in the final structure as seen in Figure 8b as well as in the number of peaks in the concentration profiles shown in Figure S7. For example, there are only three peaks in the concentration profile along the Z direction for the GNS formed from a GNR with length $L_1$, thus there is only one measured distance, $d_1$ shown in Table S7. On the other hand, there are seven peaks in the corresponding profile for the case with initial length $L_5$, thus resulting in five measured distances, $d_1$ to $d_5$. All the structures yield a stable configuration as seen by their average interlayer distance ($d$) shown in Table S7. The inner diameter varies over 8.34 Å to 10.50 Å showing no obvious trend with the changing length, however, the outer diameter of the scrolls increases with the increasing length and varies from 13.68 Å to 27.20 Å for the lengths used in this study. In contrast to our findings, Shi *et al.*$^{[7]}$ have reported an analytical relation that predicts a non-linear increase in the nanoscroll core size for increasing length of the GNR assuming constant values for parameters such as surface

energy and bending stiffness. Our understanding suggests that these parameters may be affected by the changing length of GNR as well as the particular fluid media in which the nanoscroll is being formed.[62]

Varying chirality of initial GNR. Lastly, we used GNRs of approximately the same dimensions but of different chirality and applied a rotating E-field of 30 Gr.p.m. angular frequency and 1 V/nm strength. The chirality of the GNS can be controlled by varying the chirality of the initial GNR.[26] In Figure 8c, the top row shows part of a zigzag type GNR (chiral angle $0^\circ$), an armchair type GNR (chiral angle $30\mathring{A}$) along with some chiral GNRs (chiral angles $5^\circ$, $10^\circ$, $15^\circ$, $20^\circ$, and $25^\circ$). The bottom row shows the GNSs formed from the corresponding GNR which retains the chirality of the initial planar structure. All the structures formed resemble a scroll type B, except for the armchair GNR which forms a scroll type A structure. The characteristic sharp drop in the vdW interaction energy profile over time for each chirality of the initial GNR shown in Figure S8a confirms the stability of each final structure. Comparison of the average vdW interaction energy per carbon atom of the final structures (Figure S8b) reveals that the morphologies of the structures are of

comparable stability. The concentration profiles for each structure along the Y and Z directions are shown in Figure S9, while Table S8 lists the measured characteristic distances. All types of chiral GNSs formed using our proposed method are stable 1-D configurations since the average interlayer distance ($d$) in each case enters the strong-adhesive-binding regime. The inner diameter varies over 8.91 Å to 10.31 Å with the changing chirality although no significant trend could be established between them.

Formation of hybrid-GNS structure. GNS formation induced by different nanotemplates such as CNT, nanowires, metal nanoparticles and others triggered the study of different hybrid-GNS core/shell structure.[15, 16, 26, 29] Inspired by these studies, we investigated whether our proposed setup can also be utilized to form a core/shell GNS structure.

Similar to Xia *et al.*,[26] an (8,8) single-walled CNT (SWCNT) of diameter equal to approximately 10 Å and length 99 Å is placed along the fixed edge of a 100.3 Å × 94.5 Å GNR structure. The combined structure is placed in a 12 nm × 12 nm × 14 nm box containing 64296 water molecules and subjected to a clockwise rotating E-field of 90 Gr.p.m. angular frequency and 1 V/nm strength. In addition to the prolonged edges of the

GNR structure, the carbon atoms at the edge of the SWCNT on either end are also kept fixed in this simulation (in practice, the two ends of the SWCNT would also be in contact with the fixed substrate to fix its position ). The resulting assembly of the GNR around the CNT forms the hybrid core/shell composite shown in Figure 9a(i). It has been shown previously that only CNTs larger than $10\ \mathrm{\mathring{A}}$ in diameter are able to induce the self-assembly of a GNR around it.$^{[26]}$ When a rotating E-field is applied to such a structure submerged in water, the effect of the E-field prevails the vdW interaction energy between the CNT and the GNR. As a result, the GNR follows the applied E-field and gradually encapsulates the CNT in contrast to an ultra-fast assembly that is seen in the absence of the E-field (Supporting Movie 11). In fact, because our

![](./images/812739967804506114_11.jpg)

Figure 9. (a) Hybrid core/shell composite structures formed using our proposed setup.

The GNR used is of zigzag type measuring 100.3 Å x 94.5 Å. The applied clockwise rotating E-field has an angular frequency of 90 Gr.p.m. and 1 V/nm strength. Structure formed using (i) (8,8) SWCNT of diameter approximately 10 Å and (ii) (4,4) SWCNT of diameter approximately 5.4 Å. The figure shows both lateral and front view of the final proposed setup utilizes self-assembly induced by an applied E-field, we are able to overcome the restriction of a minimum diameter of the CNT that was required in earlier proposed methods. Figure 9a(ii) shows the resulting core/shell composite when a (4,4) SWCNT of diameter approximately equal to 5.4 Å and length 99 Å is used instead. The full simulation video of 10 ns is available in Supporting Movie 12. Thus, using an applied E-field to induce the self-assembly of a GNR over a SWCNT, we were able to form a

core/shell composite hybrid structure and at the same time, remove the dependence of
the formation on the dimension of the nanotemplate. The inner diameter of the composite
is determined by the diameter of the SWCNT and thus our proposed method offers more
control over the size of the composite structure than the methods available in literature.

[26, 27]The temporal evolution in the vdW interaction energy of the structure as the GNR
encompasses the (8,8) and (4,4) SWCNTs are shown in Figure S10a and b, respectively.

The red lines with triangular markers show the energy interaction profiles for the SWCNTs
which of course remains constant throughout the simulation as the SWCNT itself does
not undergo any structural changes. The orange line with cross markers shows the vdW
interaction energy profile for the GNR which shows a sharp fall indicating the self-
assembly of the GNR. The blue line with round markers shows the vdW interaction energy
profile for the core/shell composite structure and depicts the same sharp fall as in the
profile for GNR. On the other hand, we have also calculated the vdW interaction energy
between the SWCNT and the GNR over the course of the self-assembly (violet line with
square markers). As the planar GNR encircles the fixed SWCNT, the area of contact

increases so that the magnitude of the vdW interaction energy between them increases as well. Comparison of the vdW interaction energy per carbon atom of the hybrid composite structures formed from (8,8) and (4,4) SWCNTs reveals that the core/shell composite formed using (4,4) CNT is morphologically more enduring than that for (8,8) SWCNT (Figure S11). All values of interlayer distances ($d$) (Table S9), calculated from the concentration profiles (Figure S12), lie well within that for a strong-adhesive-binding region, so that it is virtually impossible to remove the SWCNT from the hybrid structure.

Formation of scrolls from multilayer GNRs. Double and triple layered zigzag GNR structures with prolonged edges each measuring $100.3\ \mathrm{\mathring{A}} \times 94.5\ \mathrm{\mathring{A}}$ were placed in 12 nm $\times$ 12 nm $\times$ 12 nm cubic boxes containing 54058 water molecules each and subjected to rotating E-fields of 90 Gr.p.m. angular frequency and 1 V/nm strength for 10 ns. After 10 ns, the E-field was turned off and the resulting structures formed are shown in Figure 9b.

As seen in the figure, the bilayer and trilayer GNRs form inter-twined structures with well-defined scroll morphology. As an example, the full simulation video for the trilayer GNR structure under an E-field can be found in **Supporting Movie 13**. In a related work,

Chivilikhin et al.[⁶²] studied the formation of nanorolls from compounds with a layered structure in fluid media. The formation process was simulated as a multistage process, revealing that intercalation via water molecules onsets detachment of a double nanolayer which first twists into an unstressed coil and subsequently into a multiwalled nanoroll, as a result of competing internal and external stresses. In contrast, the external energy is provided by an applied E-field in our work and the formation of nanoscrolls from multilayer GNRs is onset by the alignment of water dipoles with the applied field direction, as described previously. However, in the absence of an E-field, the intercalation of water molecules itself cannot induce the scrolling of multilayer GNRs, as confirmed via our simulations.

As the multilayer GNRs inter-twin into a scroll morphology, there is a sharp fall in the vdW interaction energy of the structure (Figure S13). The average interlayer distances of the scroll structures are 3.571 and 3.418 Å respectively in the case of bilayer and trilayer GNR (Table S10) calculated from their concentration profiles (Figure S14). The sharp fall

in the vdW interaction energy profiles paired with the distances measured from the concentration validates the stability of the final scroll structures.

## CONCLUSION

We have used MD simulation to study the E-field induced orientation of a suspended GNR structure submerged in water to facilitate its self-assembly into a GNS with a hollow core and homogeneous morphology. The stability and uniformity of the final scrolls formed have been illustrated with the aid of vdW interaction energy profiles and concentration profiles along the scrolling directions. The versatility of the method has been established by depicting scroll formation from GNR structures varying in length, width, and chirality, thus relinquishing a higher degree of control over the final structure obtained. We have shown the effect of changing E-field properties such as its angular frequency and strength on the trajectory of the GNR and the corresponding GNSs formed, thus establishing the relative independence of the proposed technique on the process conditions. Moreover, it has been shown that the proposed setup overcomes the limitation of a critical dimension of the nanotemplate when utilized to form a core/shell composite

structure. This work thus offers a simple electrical energy activated, purely physical,
energy-inexpensive method towards the fabrication of a pure GNS from a nanoribbon at
room temperature. Such a method would pave the way for the realization of high-quality
GNS from nanoribbons facilitating exciting new avenues of research on nanoscrolls for
applications in hydrogen and energy storage, nanofluidic, and nanoelectronic devices.

## METHODS

To study the self-assembly of the GNR structure immersed in water under an applied
rotating E-field into a nanoscroll, we adopted the MD simulation approach. The MD
approach is a popular technique for studying GNR-based systems.[4, 7, 14, 16, 25-28] We used
the GPU-accelerated-GROMACS 5.1.5 package[63] as the computational platform,
wherein the carbon atoms were modeled as uncharged Lennard-Jones (LJ) particles[61]
and the optimized potentials for liquid simulations- all atom (OPLS-AA) force field[64] was
implemented. Bonded interaction between carbon-carbon atoms was accounted for by a
Morse bond potential for bond stretching, a harmonic cosine potential for bending and a
twofold cosine potential for torsion. The non-bonded vdW interactions are described by

12-6 LJ potential. For the water molecules, the TIP3P water model has been used.[⁶⁵] The values of the interaction potential parameters for carbon atoms and water are given in Table S1 and Table S2, respectively. As for GNR-water cross-interactions, a carbon-oxygen LJ potential was employed.[⁶¹]

For all the MD simulations conducted in this work, dangling bonds at the edges were appended by covalently bonded hydrogen atoms and the structure was energy minimized (EM) using steepest descent method with a tolerance in force of 1 kJ/mol/nm. Periodic boundary conditions were applied in all directions to keep the total number of atoms constant. The GNR structure was then equilibrated in water in an NVT followed by an NPT ensemble, each for 5 ns, to bring the temperature and pressure to 300 K and 1 bar, respectively. Once the solvent was fully relaxed in terms of potential and kinetic energies and exhibited the desired temperature and pressure, a rotating E-field was applied in the YZ plane. The rotating E-field was accomplished by applying two sinusoidal E-fields in the Y and Z directions with a $90^\circ$ phase difference between them. The temperature and pressure were maintained at 300 K and 1 bar using the Nose-Hoover thermostat[⁶⁶, ⁶⁷] at

0.1 ps coupling time and the Berendsen barostat⁽⁶⁸⁾ at 1.0 ps coupling time, respectively.

The particle-mesh Ewald method⁽⁶⁹⁾ was used to model the long-range electrostatic interaction between water molecules and a cut-off radius of 1.2 nm was used for LJ interactions. The Leap-frog integration scheme⁽⁷⁰⁾ with a time step of 1 fs was used to solve the equations of motions, with data saved every 1 ps. All trajectories presented in this work have been calculated for a simulation time equal to five time periods of the corresponding E-field (30 ns for 10 Gr.p.m., 15 ns for 20 Gr.p.m.) unless it is less than 10 ns, in which case the simulation time is 10 ns (all other angular frequencies).The prolonged edges of the GNR structure were kept fixed in all directions to simulate the effect of a substrate. Lastly, the molecular graphics program VMD 1.9.2 was used for rendering molecular trajectories. Further details on the simulation parameters and methodology are presented in the Supporting Information.

## ASSOCIATED CONTENT

Supporting Information. This material is available free of charge on the ACS publication website at https://pubs.acs.org/.

Description of simulation model and parameters, summary of all simulated cases, temporal evolution of van der Waals energy during formation, average van der Waals energy after formation, concentration profiles along scrolling direction and tables of measured characteristic interwall distances and inner/outer diameters for all final structures.(pdf) Movie files containing simulation videos. (mpg)

## AUTHOR INFORMATION

### Corresponding Author

Md. Kawsar Alam*

*Email Address: kawsaralam@eee.buet.ac.bd, kawsar.alam@alumni.ubc.ca

ORCID: 0000-0003-0467-3248

Author contributions. M.I. performed all the MD simulations, and wrote the manuscript and supporting information. M.M.R., M.M.C., and M.K.A. conceived the idea. M.I, M.M.R., and M.M.C. designed the modeling approach, and M.M.R designed the simulation setup and confirmed the proof of concept. M.I. and M.K.A. analyzed the data. M.K.A. edited the

manuscript and supervised the entire work. All authors discussed the results and commented on the final manuscript.

Competing interests statement. The authors declare no competing financial interest.

## ACKNOWLEDGMENT
We are grateful to the Department of EEE, Bangladesh University of Engineering and Technology (BUET) for allowing us to use the simulation facility of Nanoelectronic Devices and Materials Research Lab exclusively.

## REFERENCES
(1) Gogotsi, Y., Presser, V., Eds, *Carbon Nanomaterials*, CRC press: Boca Raton, 2013.

(2) Silva, F. W. N.; Cruz-Silva, E.; Terrones, M.; Terrones, H.; Barros, E. B. Bnc Nanoshells: A Novel Structure for Atomic Storage. *Nanotechnology* **2017**, 28, 465201.

(3) Bacon, R. Growth, Structure, and Properties of Graphite Whiskers. *J. Appl. Phys.* **1960**, 31, 283-290.

(4) Braga, S. F.; Coluci, V. R.; Legoas, S. B.; Giro, R.; Galvão, D. S.; Baughman, R. H. Structure and Dynamics of Carbon Nanoscrolls. *Nano Lett.* **2004**, 4, 881-884.

(5) Chen, Y.; Lu, J.; Gao, Z. Structural and Electronic Study of Nanoscrolls Rolled up by a Single Graphene Sheet. *J. Phys. Chem. C* **2007**, 111, 1625-1630.

(6) Pan, H.; Feng, Y.; Lin, J. Ab Initio Study of Electronic and Optical Properties of Multiwall Carbon Nanotube Structures Made up of a Single Rolled-up Graphite Sheet. *Phys. Rev. B* **2005**, 72, 085415.

(7) Shi, X.; Pugno, N. M.; Gao, H. Tunable Core Size of Carbon Nanoscrolls. *J. Comput. Theor. Nanosci.* **2010**, 7, 517-521.

(8) Mpourmpakis, G.; Tylianakis, E.; Froudakis, G. E. Carbon Nanoscrolls: A Promising Material for Hydrogen Storage. *Nano Lett.* **2007**, 7, 1893-1897.

(9) Xie, X.; Ju, L.; Feng, X.; Sun, Y.; Zhou, R.; Liu, K.; Fan, S.; Li, Q.; Jiang, K. Controlled Fabrication of High-Quality Carbon Nanoscrolls from Monolayer Graphene. *Nano Lett.* **2009**, 9, 2565-2570.

(10) Zeng, F.; Kuang, Y.; Liu, G.; Liu, R.; Huang, Z.; Fu, C.; Zhou, H. Supercapacitors Based on High-Quality Graphene Scrolls. *Nanoscale* **2012**, 4, 3997-4001.

(11) Zheng, B.; Xu, Z.; Gao, C. Mass Production of Graphene Nanoscrolls and Their Application in High Rate Performance Supercapacitors. *Nanoscale* **2016**, 8, 1413-1420.

(12) Zhao, J.; Yang, B.; Zheng, Z.; Yang, J.; Yang, Z.; Zhang, P.; Ren, W.; Yan, X. Facile Preparation of One-Dimensional Wrapping Structure: Graphene Nanoscroll-Wrapped of Fe3o4 Nanoparticles and Its Application for Lithium-Ion Battery. *ACS Appl. Mater. Interfaces* **2014**, 6, 9890-9896.

(13) Tarábková, H.; Zelinger, Z.; Janda, P. Electrochemically Controlled Winding and Unwinding of Substrate-Supported Carbon Nanoscrolls. *Phys. Chem. Chem. Phys.* 2018, 20, 5900-5908.

(14) Shi, X.; Cheng, Y.; Pugno, N. M.; Gao, H. Tunable Water Channels with Carbon Nanoscrolls. *Small* 2010, 6, 739-744.

(15) Berman, D.; Deshmukh, S. A.; Sankaranarayanan, S. K. R. S.; Erdemir, A.; Sumant, A. V. Macroscale Superlubricity Enabled by Graphene Nanoscroll Formation. *Science* 2015, 348, 1118-1122.

(16) Bejagam, K. K.; Singh, S.; Deshmukh, S. A. Nanoparticle Activated and Directed Assembly of Graphene into a Nanoscroll. *Carbon* 2018, 134, 43-52.

(17) Li, J. L.; Peng, Q. S.; Bai, G. Z.; Jiang, W. Carbon Scrolls Produced by High Energy Ball Milling of Graphite. *Carbon* 2005, 43, 2830-2833.

(18) Shioyama, H.; Akita, T. A New Route to Carbon Nanotubes. *Carbon* 2003, 41, 179-181.

(19) Viculis, L. M.; Mack, J. J.; Kaner, R. B. A Chemical Route to Carbon Nanoscrolls. *Science* 2003, 299, 1361-1361.

(20) Savoskin, M. V.; Mochalin, V. N.; Yaroshenko, A. P.; Lazareva, N. I.; Konstantinova, T. E.; Barsukov, I. V.; Prokofiev, I. G. Carbon Nanoscrolls Produced from Acceptor-Type Graphite Intercalation Compounds. *Carbon* 2007, 45, 2797-2800.

(21) Yu, D.; Liu, F. Synthesis of Carbon Nanotubes by Rolling up Patterned Graphene Nanoribbons Using Selective Atomic Adsorption. *Nano Lett.* 2007, 7, 3046-3050.

(22) Zeng, F.; Kuang, Y.; Wang, Y.; Huang, Z.; Fu, C.; Zhou, H. Facile Preparation of High-Quality Graphene Scrolls from Graphite Oxide by a Microexplosion Method. *Adv. Mater.* 2011, 23, 4929-4932.

(23) Gao, Y.; Chen, X.; Xu, H.; Zou, Y.; Gu, R.; Xu, M.; Jen, A. K. Y.; Chen, H. Highly-Efficient Fabrication of Nanoscrolls from Functionalized Graphene Oxide by Langmuir–Blodgett Method. *Carbon* 2010, 48, 4475-4482.

(24) Zhao, J.; Yang, B.; Yang, Z.; Zhang, P.; Zheng, Z.; Ren, W.; Yan, X. Facile Preparation of Large-Scale Graphene Nanoscrolls from Graphene Oxide Sheets by Cold Quenching in Liquid Nitrogen. *Carbon* **2014**, 79, 470-477.

(25) Patra, N.; Wang, B.; Král, P. Nanodroplet Activated and Guided Folding of Graphene Nanostructures. *Nano Lett.* **2009**, 9, 3766-3771.

(26) Xia, D.; Xue, Q.; Xie, J.; Chen, H.; Lv, C.; Besenbacher, F.; Dong, M. Fabrication of Carbon Nanoscrolls from Monolayer Graphene. *Small* **2010**, 6, 2010-2019.

(27) Chu, L.; Xue, Q.; Zhang, T.; Ling, C. Fabrication of Carbon Nanoscrolls from Monolayer Graphene Controlled by P-Doped Silicon Nanowires: A Md Simulation Study. *J. Phys. Chem. C* **2011**, 115, 15217-15224.

(28) Xu, S.; Fu, H.; Li, Y.; Zhang, C.; Gu, Z.; Zhang, D. Novel Scroll Peapod Produced by Spontaneous Scrolling of Graphene onto Fullerene String. *Phys. Chem. Chem. Phys.* **2016**, 18, 10138-10143.

(29) Sharifi, T.; Gracia-Espino, E.; Reza Barzegar, H.; Jia, X.; Nitze, F.; Hu, G.; Nordblad, P.; Tai, C.-W.; Wågberg, T. Formation of Nitrogen-Doped Graphene

Nanoscrolls by Adsorption of Magnetic Γ-Fe2o3 Nanoparticles. *Nat. Commun.* 2013, 4, 2319.

(30) Daub, C. D.; Bratko, D.; Ali, T.; Luzar, A. Microscopic Dynamics of the Orientation of a Hydrated Nanoparticle in an Electric Field. *Phys. Rev. Lett.* 2009, 103, 207801.

(31) Guo, X.; Su, J.; Guo, H. Electric Field Induced Orientation and Self-Assembly of Carbon Nanotubes in Water. *Soft Matter* 2012, 8, 1010-1016.

(32) Han, M. Y.; Özyilmaz, B.; Zhang, Y.; Kim, P. Energy Band-Gap Engineering of Graphene Nanoribbons. *Phys. Rev. Lett.* 2007, 98, 206805.

(33) Jiao, L.; Zhang, L.; Wang, X.; Diankov, G.; Dai, H. Narrow Graphene Nanoribbons from Carbon Nanotubes. *Nature* 2009, 458, 877-880.

(34) Kosynkin, D. V.; Higginbotham, A. L.; Sinitskii, A.; Lomeda, J. R.; Dimiev, A.; Price, B. K.; Tour, J. M. Longitudinal Unzipping of Carbon Nanotubes to Form Graphene Nanoribbons. *Nature* 2009, 458, 872-876.

(35) Li, X.; Wang, X.; Zhang, L.; Lee, S.; Dai, H. Chemically Derived, Ultrasmooth Graphene Nanoribbon Semiconductors. *Science* 2008, 319, 1229-1232.

(36) Ci, L.; Song, L.; Jariwala, D.; Elías, A. L.; Gao, W.; Terrones, M.; Ajayan, P. M. Graphene Shape Control by Multistage Cutting and Transfer. *Adv. Mater.* 2009, 21, 4487-4491.

(37) Sprinkle, M.; Ruan, M.; Hu, Y.; Hankinson, J.; Rubio-Roy, M.; Zhang, B.; Wu, X.; Berger, C.; de Heer, W. A. Scalable Templated Growth of Graphene Nanoribbons on Sic. *Nat. Nanotechnol.* 2010, 5, 727-731.

(38) Cai, J.; Ruffieux, P.; Jaafar, R.; Bieri, M.; Braun, T.; Blankenburg, S.; Muoth, M.; Seitsonen, A. P.; Saleh, M.; Feng, X.; Müllen, K.; Fasel, R. Atomically Precise Bottom-up Fabrication of Graphene Nanoribbons. *Nature* 2010, 466, 470-473.

(39) Chung, H.-C.; Chang, C.-P.; Lin, C.-Y.; Lin, M.-F. Electronic and Optical Properties of Graphene Nanoribbons in External Fields. *Phys. Chem. Chem. Phys.* 2016, 18, 7573-7616.

(40) Chung, H.-C.; Lin, Y.-T.; Lin, S.-Y.; Ho, C.-H.; Chang, C.-P.; Lin, M.-F. Magnetoelectronic and Optical Properties of Nonuniform Graphene Nanoribbons. *Carbon* 2016, 109, 883-895.

(41) Chung, H. C.; Lee, M. H.; Chang, C. P.; Lin, M. F. Exploration of Edge-Dependent Optical Selection Rules for Graphene Nanoribbons. *Opt. Express* 2011, 19, 23350.

(42) Prezzi, D.; Varsano, D.; Ruini, A.; Marini, A.; Molinari, E. Optical Properties of Graphene Nanoribbons: The Role of Many-Body Effects. *Phys. Rev. B* 2008, 77, 041404(R).

(43) Dutta, S.; Pati, S. K. Novel Properties of Graphene Nanoribbons: A Review. *J. Mater. Chem.* 2010, 20, 8207-8223.

(44) Bennett, P. B.; Pedramrazi, Z.; Madani, A.; Chen, Y.-C.; de Oteyza, D. G.; Chen, C.; Fischer, F. R.; Crommie, M. F.; Bokor, J. Bottom-up Graphene Nanoribbon Field-Effect Transistors. *Appl. Phys. Lett.* 2013, 103, 253114.

(45) Chen, Y. P.; Xie, Y. E.; Yan, X. H. Electron Transport of L-Shaped Graphene Nanoribbons. *J. Appl. Phys.* 2008, 103, 063711.

(46) Chen, Y. P.; Xie, Y. E.; Sun, L. Z.; Zhong, J. Asymmetric Transport in Asymmetric T-Shaped Graphene Nanoribbons. *Appl. Phys. Lett.* 2008, 93, 092104.

(47) Wang, Z. F.; Li, Q.; Shi, Q. W.; Wang, X.; Hou, J. G.; Zheng, H.; Chen, J. Ballistic Rectification in a Z-Shaped Graphene Nanoribbon Junction. *Appl. Phys. Lett.* 2008, 92, 133119.

(48) OuYang, F.; Xiao, J.; Guo, R.; Zhang, H.; Xu, H. Transport Properties of T-Shaped and Crossed Junctions Based on Graphene Nanoribbons. *Nanotechnology* 2009, 20, 055202.

(49) Papon, R.; Sharma, S.; Shinde, S. M.; Thangaraja, A.; Kalita, G.; Tanemura, M. Formation of Graphene Nanoribbons and Y-Junctions by Hydrogen Induced Anisotropic Etching. *RSC Advances* 2015, 5, 35297-35301.

(50) Chen, Y.-C.; Cao, T.; Chen, C.; Pedramrazi, Z.; Haberer, D.; de Oteyza, D. G.; Fischer, F. R.; Louie, S. G.; Crommie, M. F. Molecular Bandgap Engineering of Bottom-up Synthesized Graphene Nanoribbon Heterojunctions. *Nat. Nanotechnol.* 2015, 10, 156-160.

(51) Keramatnejad, K.; Zhou, Y. S.; Li, D. W.; Golgir, H. R.; Huang, X.; Zhou, Q. M.; Song, J. F.; Ducharme, S.; Lu, Y. F. Laser-Assisted Nanowelding of Graphene to

Metals: An Optical Approach toward Ultralow Contact Resistance. *Adv. Mater. Interfaces* **2017**, 4, 1700294.

(52) Yuan, Y.; Chen, J. Nano-Welding of Multi-Walled Carbon Nanotubes on Silicon and Silica Surface by Laser Irradiation. *Nanomaterials* **2016**, 6, 36.

(53) Das, S.; Lahiri, D.; Agarwal, A.; Choi, W. Interfacial Bonding Characteristics between Graphene and Dielectric Substrates. *Nanotechnology* **2014**, 25, 045707.

(54) Das, S.; Lahiri, D.; Lee, D.-Y.; Agarwal, A.; Choi, W. Measurements of the Adhesion Energy of Graphene to Metallic Substrates. *Carbon* **2013**, 59, 121-129.

(55) Gao, Y.; Cao, T.; Cellini, F.; Berger, C.; de Heer, W. A.; Tosatti, E.; Riedo, E.; Bongiorno, A. Ultrahard Carbon Film from Epitaxial Two-Layer Graphene. *Nat. Nanotechnol.* **2017**, 13, 133-138.

(56) Takamoto, S.; Yamasaki, T.; Nara, J.; Ohno, T.; Kaneta, C.; Hatano, A.; Izumi, S. Atomistic Mechanism of Graphene Growth on a Sic Substrate: Large-Scale Molecular Dynamics Simulations Based on a New Charge-Transfer Bond-Order Type Potential. *Phys. Rev. B* **2018**, 97, 125411.

(57) Giesbers, A. J. M.; Zeitler, U.; Neubeck, S.; Freitag, F.; Novoselov, K. S.; Maan, J. C. Nanolithography and Manipulation of Graphene Using an Atomic Force Microscope. *Solid State Commun.* **2008**, 147, 366-369.

(58) He, Y.; Dong, H.; Li, T.; Wang, C.; Shao, W.; Zhang, Y.; Jiang, L.; Hu, W. Graphene and Graphene Oxide Nanogap Electrodes Fabricated by Atomic Force Microscopy Nanolithography. *Appl. Phys. Lett.* **2010**, 97, 133301.

(59) Newaz, A. K. M.; Puzyrev, Y. S.; Wang, B.; Pantelides, S. T.; Bolotin, K. I. Probing Charge Scattering Mechanisms in Suspended Graphene by Varying Its Dielectric Environment. *Nat. Commun.* **2012**, 3, 734.

(60) Schmidt, M. E.; Hammam, A. M. M.; Iwasaki, T.; Kanzaki, T.; Muruganathan, M.; Ogawa, S.; Mizuta, H. Controlled Fabrication of Electrically Contacted Carbon Nanoscrolls. *Nanotechnology* **2018**, 29, 235605.

(61) Rahman, M. M.; Chowdhury, M. M.; Alam, M. K. Rotating-Electric-Field-Induced Carbon-Nanotube-Based Nanomotor in Water: A Molecular Dynamics Study. *Small* **2017**, 13, 1603978.

(62) Chivilikhin, S. A.; Popov, I. Y.; Blinova, I. V.; Kirillova, S. A.; Konovalov, A. S.; Oblogin, S. I.; Tishkin, V. O.; Chernov, I. A.; Gusarov, V. V. Simulation of the Formation of Nanorolls. *Glass Phys. Chem.* 2007, 33, 315-319.

(63) Abraham, M. J.; Murtola, T.; Schulz, R.; Páll, S.; Smith, J. C.; Hess, B.; Lindahl, E. Gromacs: High Performance Molecular Simulations through Multi-Level Parallelism from Laptops to Supercomputers. *SoftwareX* 2015, 1-2, 19-25.

(64) Jorgensen, W. L.; Tirado-Rives, J. The Opls [Optimized Potentials for Liquid Simulations] Potential Functions for Proteins, Energy Minimizations for Crystals of Cyclic Peptides and Crambin. *J. Am. Chem. Soc.* 1988, 110, 1657-1666.

(65) Jorgensen, W. L.; Chandrasekhar, J.; Madura, J. D. Comparison of Simple Potential Functions for Simulating Liquid Water. *J. Chem. Phys.* 1983, 79, 926.

(66) Nose´, S. A Molecular Dynamics Method for Simulations in the Canonical Ensemble. *Mol. Phys.* 1984, 52, 255-268.

(67) Hoover, W. G. Canonical Dynamics: Equilibrium Phase-Space Distributions. *Phys. Rev. A* 1985, 31, 1695-1697.

(68) Berendsen, H. J. C.; Postma, J. P. M.; van Gunsteren, W. F.; DiNola, A.; Haak, J. R. Molecular Dynamics with Coupling to an External Bath. *J. Chem. Phys.* **1984**, 81, 3684-3690.

(69) Darden, T.; York, D.; Pedersen, L. Particle Mesh Ewald: An N·Log(N) Method for Ewald Sums in Large Systems. *J. Chem. Phys.* **1993**, 98, 10089-10092.

(70) Hockney, R. W.; Goel, S. P.; Eastwood, J. W. Quiet High-Resolution Computer Models of a Plasma. *J. Comp. Phys.* **1974**, 14, 148-158.

For Table of Contents Only

![](./images/812739967804506114_12.jpg)

![](./images/812739967804506114_13.jpg)

(a) $t_1$= 0 ns$\rightarrow$ $t_2$= 1.5 ns$\rightarrow$ $t_3$= 3.9 ns

(b) $t_4$= 3.9 ns$\rightarrow$ $t_5$= 4.65 ns $\rightarrow$ $t_6$= 5.4ns

(c) $t_7$= 6.15 ns$\rightarrow$ $t_8$= 6.9 ns$\rightarrow$ $t_9$= 7.65 ns

(d) $t_{10}$= 8.4 ns$\rightarrow$ $t_{11}$= 9.15 ns $\rightarrow$ $t_{12}$= 9.9 ns

![](./images/812739967804506114_14.jpg)

![](./images/812739967804506114_15.jpg)

![](./images/812739967804506114_16.jpg)

![](./images/812739967804506114_17.jpg)

![](./images/812739967804506114_18.jpg)

![](./images/812739967804506114_19.jpg)

![](./images/812739967804506114_20.jpg)

![](./images/812739967804506114_21.jpg)
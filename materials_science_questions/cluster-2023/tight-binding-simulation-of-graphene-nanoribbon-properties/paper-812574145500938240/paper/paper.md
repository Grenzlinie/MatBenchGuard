# First Principle Analysis of Os-passivated Armchair Graphene Nanoribbons for Nanoscale Interconnects

Vipul Kumar Nishad, *Student Member, IEEE*, Atul Kumar Nishad, *Member, IEEE*, Sourajeet Roy, *Member, IEEE*, Brajesh Kumar Kaushik, *Senior Member, IEEE* and Rohit Sharma, *Senior Member, IEEE*

**Abstract**— In this paper, transport properties of Osmium (Os)-passivated armchair graphene nanoribbons (AGNRs) have been explored for applications in nanoscale interconnects. Os has been used for passivation in place of Hydrogen (H). In general, H-passivation is used to reduce the edge scattering in AGNRs. However, this increases the bandgap of the structure. In our study, it is found that Os-passivation reduces the edge scattering with improvement in metallicity of AGNRs, which makes it suitable for future nanoscale interconnects. We have extracted key parameters, such as transmission spectrum, I-V characteristics, number of conduction channels, Fermi velocity, kinetic inductance and quantum capacitance. We have compared our results with Fe-passivated AGNRs. In case of Os-passivated AGNRs, up to eight conduction channels are seen that result in higher currents of up to 4x as compared to Fe-passivated AGNRs.

## I. INTRODUCTION

Graphene is seen as a promising interconnect material as we approach technology nodes at the end of the roadmap [1-5]. Metallic nature is a primary concern for any material for possible interconnect applications [6-8]. Graphene is a semimetal that exhibits extraordinary current carrying capability and mean free path (mfp) [1, 9-12]. Graphene Nanoribbons (GNRs) exhibit bandgap at these nanoscale dimensions that makes it challenging for them to be used as interconnects. In addition, Hydrogen passivation is performed that is essential to eliminate dangling bonds present at GNR's edge. Hydrogen passivation reduces edge scattering but it further increases the bandgap. Therefore, all fabricated Hydrogen passivated GNRs show semiconducting behaviour [13, 14]. Theoretically, only armchair GNRs (AGNRs) show semiconducting behaviour, therefore, AGNRs have been considered in our first principle study. Also, one needs to look at the alternative solution towards increase in metallicity of AGNRs so that extraordinary properties of graphene can be utilized for interconnect applications. One of the alternatives can be passivation of AGNRs using other atoms in place of Hydrogen.

There are several elements available in the periodic table. In [15], authors have inspected the electronic properties of Ag, Au, Co, Cu, Fe and Ni-passivated ZGNRs. In that, authors have observed the metallic nature of Fe, Co and Ni-passivated ZGNRs, while semiconducting nature for Cu, Ag and Au-passivated ZGNRs. In [16], Sarikavak-Lisesivdin *et.al.* have explored the electronic properties of Ru-passivated AGNRs that show metallic behaviour. In [17], Jippo *et.al.* have performed first-principle study on H, F and Cl-passivated AGNRs. In that, lesser bandgap of F- and Cl-passivated AGNRs achieved as compared to H-passivated AGNRs. Still an enormous research work is required in the field of edge passivation of AGNRs. There are several elements are still untouched that can be explored and determine the possibility of metallicity. This can open huge opportunities for nanoscale interconnect applications.

In this paper, first principle calculations have been performed to evaluate the effect of Osmium (Os) passivation on AGNRs. In that, structural stability, electronic and transport properties of one-edge and both-edge Os-passivated AGNRs configurations are analysed using density functional theory (DFT) and non-equilibrium Green's function (NEGF) formalism. Further, significant parameters for AGNRs interconnect i.e. number of conduction channel ($N_{ch}$), Fermi velocity, kinetic inductance and quantum capacitance are also calculated. Based on our analysis, we observe that one edge Os-passivated AGNRs show six while both edge Os-passivated AGNRs show eight conduction channels across the Fermi level. Both edge Os-passivated AGNRs produce up to 4x higher current as compared to Fe-passivated AGNRs [18] thereby promising superior interconnect performance.

The remainder of the paper is organised as follows: Section II describes the computational details that have been used for first-principle study. Section III focuses on the results and discussion. Finally, section IV summarizes this paper.

## II. COMPUTATIONAL DETAILS

In this paper, density functional theory calculation has been done using Atomistix Tool Kit (ATK) [19]. AGNRs have been investigated with edge passivation by H-atom on both sides and Os-atom on one edge as well as both sides, as shown in Fig. 1. The structural geometry of AGNRs are optimized using a maximum atomic force of 0.05 eV/Å and stress error tolerance of 0.1 GPa within the DFT framework.

Vipul Kumar Nishad and Rohit Sharma are with the Department of Electrical Engineering, Indian Institute of Technology Ropar, Rupnagar, India. Email: vipul.nishad@iitrpr.ac.in, rohit@iitrpr.ac.in

Atul Kumar Nishad is with the Department of Electronics & Communication Engineering, National Institute of Technology, Warangal, India. Email: atul@nitw.ac.in

Sourajeet Roy and Brajesh Kumar Kaushik are with the Department of Electronics and Communication Engineering, Indian Institute of Technology Roorkee, Roorkee, India. Email: sourajeet.roy@ece.iitr.ac.in, bkk23fec@iitr.ac.in

---

978-1-7281-8264-3/20/$31.00 ©2020 IEEE

![](./images/812574145500938240_1.jpg)

Fig.1 The schematic representation of supercells used in simulation. (a) H-passivated AGNRs, (b) one-edge Os-passivated AGNRs and (c) both-edge Os-passivated AGNRs.

LBFGS optimizer method is used in this framework. Generalized Gradient Approximation (GGA) [20] type of exchange correlation along with Perdew-Burke-Ernzerhof (PBE) as predefined functionals have been used in our analysis. DoubleZetaPolarized basis set with 150 Ryd value of Density mesh cut-off is selected. $1 \times 1 \times 100$ $k$-point sampling for the integration of Brillouin zone is taken. The supercell is periodic in Z-direction and to suppress the interaction between structures and its periodic images, $10\mathring{A}$ of vaccum space is used in X- and Y-direction.

<table>
<caption>TABLE I<br>BINDING ENERGY AND BANDGAP ($E_G$) FOR AGNRS</caption>
<thead>
<tr>
<th colspan="2">AGNR configurations</th>
<th>Binding Energy/passivating atom (eV)</th>
<th>Bandgap (eV)</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2">H-passivated</td>
<td>-5.59</td>
<td>1.52 (direct)</td>
</tr>
<tr>
<td>One-edge passivated</td>
<td>Os-</td>
<td>-6.34</td>
<td>Metallic</td>
</tr>
<tr>
<td>Both-edge passivated</td>
<td>Os-</td>
<td>-7.09</td>
<td>Metallic</td>
</tr>
</tbody>
</table>

### III. RESULTS AND DISCUSSION

In this section, the structural stability, electronic and transport properties of H-passivated, one-edge Os-passivated and both-edge Os-passivated AGNRs are presented. Fig. 1 shows the supercells of H-passivated, one-edge Os-passivated and both-edge Os-passivated AGNRs configurations. In order to determine the structural stability, binding energy calculation is required. Interconnect configuration having more negative binding energy value indicates a more stable structure. Binding energy for various configurations is shown in Table I. It is seen that our proposed both one-edge and both-edge Os-passivated AGNRs are more stable as compared to H-passivated AGNRs. The Density of States (DOS) and band structure calculation are also performed and shown in Fig. 2. From Fig. 2 and Table 1, nonzero-bandgap ($\sim1.52eV$) of H-passivated AGNRs can be clearly observed. With Os-passivation, AGNR structure converts from semiconducting to metallic in nature. This can be further justified from the DOS and band structure plot shown in Fig. 2. Supercell shown in Fig. 1 has been extended and used in standard two-probe model for calculations of various transport properties. This standard two-probe model is shown in Fig. 3. Fig. 4

![](./images/812574145500938240_2.jpg)

Fig. 2. DOS profiles and band structures for AGNRs (with $N=7$). (a) and (d) H-passivated AGNRs. (b) and (e) One-edge Os-passivated AGNRs. (c) and (f) Both-edge Os-passivated AGNRs. Fermi level has shown by dotted line at 0 eV.

156
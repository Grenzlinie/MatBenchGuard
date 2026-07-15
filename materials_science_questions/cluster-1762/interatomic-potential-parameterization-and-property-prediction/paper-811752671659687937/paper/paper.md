# Chemical Sputtering of GaN Crystal with a Chlorine-Adsorbed Layer

This content has been downloaded from IOPscience. Please scroll down to see the full text.

2010 Jpn. J. Appl. Phys. 49 08JE03

(http://iopscience.iop.org/1347-4065/49/8S1/08JE03)

View [the table of contents for this issue], or go to the [journal homepage] for more

Download details:

IP Address: 134.129.120.3
This content was downloaded on 06/03/2015 at 16:31

Please note that [terms and conditions apply].

# Chemical Sputtering of GaN Crystal with a Chlorine-Adsorbed Layer
Kenji Harafuji* and Katsuyuki Kawamura¹

Department of Electrical and Electronic Engineering, Ritsumeikan University, 1-1-1 Noji-Higashi, Kusatsu, Shiga 525-8577, Japan
¹Department of Earth and Planetary Science, Tokyo Institute of Technology, 2-12-1 Ookayama, Meguro, Tokyo 152-8551, Japan
Received online September 16, 2009; accepted December 14, 2009; published online August 20, 2010

A molecular dynamics simulation has been carried out to investigate the chemical sputtering of wurtzite-type GaN(0001) surfaces with and without a Cl-adsorbed layer. Sputtering of crystalline atoms is examined with Ar impacts at energies less than 250 eV. Ga sputtering does not take place at all on the clean surface without Cl-adsorption. On the other hand, Ga sputtering yield has a large finite value for Ar impact on the Cl-adsorbed surface. Generally, Ga is sputtered in the form of Ga–Cl₂, and sometimes in the form of Ga–Cl, Ga–N–Cl, Ga–N, and Ga–N–Ga–Cl₂. Ga atoms are not singly sputtered. Atoms escape from the surface in the time range of 200–3000 fs after the impact of the incident Ar atom. The shorter and longer escape times correspond to physical and chemical sputtering, respectively.
© 2010 The Japan Society of Applied Physics

DOI: 10.1143/JJAP.49.08JE03

## 1. Introduction
GaN is an excellent material for short-wavelength optoelec- tronic devices such as ultraviolet light-emitting diodes and laser diodes.¹,²) GaN is, however, chemically inert in acids and bases at room temperature.³) Reactive ion etching is thus conventionally used to form mesa structures to reach the n- type material, and to form ridge structures to attain lateral optical confinement.⁴) A gas mixture of Cl-based chemicals is usually used for etching discharges. Adesida et al. reported the reactive ion etching characteristics in silicon tetrachloride plasmas, and showed that etch rates increased monotonically with increasing plasma self-bias voltage exceeding 50 nm/min at 400 V.⁵) Pearton et al. reported that highly anisotropic etching was achieved at low dc self-bias in electron cyclotron resonance $Cl_{2}/H_{2}$ or $CH_{4}/H_{2}/Ar$ discharges.⁶) Chemically assisted ion beam etching characteristics were also investigated using a 500 eV Ar ion beam directed onto a sample in a $Cl_{2}$ ambient.⁷) Although many articles have been presented on GaN etching, the physical and chemical mechanisms of the surface reaction are not yet clear.

Molecular dynamics (MD) simulation is a powerful tool for investigating details of physical and chemical mecha- nisms that would otherwise be difficult or impossible to obtain.⁸) Several studies on silicon etching by MD simulation have been reported.⁹⁻¹¹)

Nord et al. carried out an MD study of damage accumu- lation during ion beam irradiation of GaN in the incident ion energy range between 200 eV and 10 keV.¹²) They used a bond-order potential where long-range interactions were not explicitly included. Although the potential has a flexibility that can treat pure Ga and N phases, the neglect of the Coulomb interaction is not necessarily adequate from the physical point of view.

In this study, MD simulation is carried out to investigate the Ar ion sputtering process of GaN(0001) surfaces. Two cases are simulated, one with a Cl-adsorbed surface and the other with a clean surface. Sputtering yield is evaluated as a function of Ar impact energy. Preliminary results have been presented elsewhere by the present authors.¹³⁻¹⁷) To the best of our knowledge, basic experimental data relating to sputtering yields have not yet been reported.

The organization of this paper is as follows. In §2, the interatomic potential and the accuracy of the potential are briefly described. In §3, simulation models are explained. In §4, calculation results are presented. Statistical data of sputtering yield is obtained as a function of incident Ar energy. Finally, concluding remarks are made in §5.

## 2. Interatomic Potential
### 2.1 Functional form
In this study, the functional form of a two-body interatomic potential is modeled as follows:

$$
\begin{aligned}
u_{i j} & =\frac{Z_{i} Z_{j} e^{2}}{4 \pi \varepsilon_{0} r_{i j}}+f_{0}\left(b_{i}+b_{j}\right) \exp \left(\frac{a_{i}+a_{j}-r_{i j}}{b_{i}+b_{j}}\right) \\
& +D_{1 i j} \exp \left(-\beta_{1 i j} r_{i j}\right)+D_{2 i j} \exp \left(-\beta_{2 i j} r_{i j}\right)-\frac{c_{i} c_{j}}{r_{i j}^{6}}, \quad (1)
\end{aligned}
$$

where the first term is the Coulomb interaction, the second term is the Gilbert-type short-range repulsion, the third and fourth terms represent the covalent bonding and covalent repulsion of the modified Morse type, respectively, and the last term is the van der Waals potential. The variable $r_{i j}$ is the interatomic distance between the $i$ th and $j$ th atoms, $\varepsilon_{0}$ is the dielectric constant of vacuum, $Z_{i}$ is the effective charge for each atom, $f_{0}$ is the constant for unit conversion [41.86 kJ/(nm·mol)], $a_{i}$ is the repulsion radius, $b_{i}$ is the softness parameter, $D_{1}$, $D_{2}$, $\beta_{1}$, and $\beta_{2}$ are covalent coefficients, and $c_{i}$ is the van der Waals coefficient.

These potential parameters for Ga and N are determined on the basis of the periodic restricted Hartree-Fock ab initio method (CRYSTAL 98).¹⁸,¹⁹) The obtained potential param- eters are listed in Table I. The method is also used to determine lattice constants $a$, $b$, and $c$, the internal parameter $u$, and the volume $V$ for a unit cell of a wurtzite-type GaN crystal with $P6_{3}mc$ symmetry. The lattice constants give the minimal total energy $E$. The obtained values are as follows: $a = b = 0.320031$ nm, $c = 0.51574$ nm, and $u = 0.369894$. These parameters are used in the following MD simulation.

As the unit cell for constructing an MD basic cell, a rectangular parallelepiped is selected, as shown by the broken lines in Fig. 1. The lattice constants $a$, $b'$, and $c$ in Cartesian coordinates are shown there. In the figure, the definitions of the crystal directions $A$, $B$, and $C$ are also depicted. The definition of the MD basic cell is explained in §3.

### 2.2 Reliability of the potential
The accuracy of the interatomic potential for Ga and N atoms is checked with respect to three different consider-

*E-mail address: harafuji@se.ritsumei.ac.jp

08JE03-1
© 2010 The Japan Society of Applied Physics

<table>
 <thead>
  <tr>
   <th>
    Atom
   </th>
   <th>
    $Z$
    <br/>
    (e)
   </th>
   <th>
    $a$
    <br/>
    (nm)
   </th>
   <th>
    $b$
    <br/>
    (nm)
   </th>
   <th>
    $c$
    <br/>
    $(\text{kJ/mol})^{1/2}{(\text{nm})}^{3}$
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>
    N
   </td>
   <td>
    $- 1.150$
   </td>
   <td>
    $0.1970$
   </td>
   <td>
    $0.0123$
   </td>
   <td>
    $0.0364$
   </td>
  </tr>
  <tr>
   <td>
    Ga
   </td>
   <td>
    $1.150$
   </td>
   <td>
    $0.0834$
   </td>
   <td>
    $0.00911$
   </td>
   <td>
    $0.0$
   </td>
  </tr>
  <tr>
   <td>
    Ar
   </td>
   <td>
    $0$
   </td>
   <td>
    $0.1878$
   </td>
   <td>
    $0.0117$
   </td>
   <td>
    $0.0788$
   </td>
  </tr>
  <tr>
   <td>
    Cl
   </td>
   <td>
    $- 0.48$
   </td>
   <td>
    $0.2061$
   </td>
   <td>
    $0.0190$
   </td>
   <td>
    $0.0573$
   </td>
  </tr>
  <tr>
   <td>
    Na
   </td>
   <td>
    $0.48$
   </td>
   <td>
    $0.1493$
   </td>
   <td>
    $0.0120$
   </td>
   <td>
    $0.0184$
   </td>
  </tr>
  <tr>
   <td>
    Atom-atom
   </td>
   <td>
    $D_{1}$
    <br/>
    (kJ/mol)
   </td>
   <td>
    $\beta_{1}$
    <br/>
    $(\text{nm}^{- 1})$
   </td>
   <td>
    $D_{2}$
    <br/>
    (kJ/mol)
   </td>
   <td>
    $\beta_{2}$
    <br/>
    $(\text{nm}^{- 1})$
   </td>
  </tr>
  <tr>
   <td>
    N–Ga
   </td>
   <td>
    $- 5250.5$
   </td>
   <td>
    $20.0$
   </td>
   <td>
    $6581.7$
   </td>
   <td>
    $40.0$
   </td>
  </tr>
 </tbody>
</table>

Table I. Potential parameters of wurtzite-type GaN crystal in eq. (1) for Coulomb interaction, Gilbert-type short-range repulsion, van der Waals potential, and covalent terms.

![](./images/811752671659687937_1.jpg)

Fig. 1. Definition of lattice constants $a$, $b$, and $c$ and internal parameter $u$ in a unit cell (denoted by solid lines) of wurtzite-type GaN crystals. Another type of unit cell (denoted by broken lines) for constructing an MD basic cell and the lattice constants $a$, $b'$, and $c$ in Cartesian coordinates are also shown. The definitions of the crystal directions, $A$, $B$, and $C$, are depicted.

ations. The details are given elsewhere, $^{18,20–22)}$ and the essence of the method is described in this paper.

First, elastic constants are examined. A bulk modulus of 224 GPa is obtained through fitting the $V$–$E$ curve from the ab initiocalculation to the integrated form of the third-order Birch–Murnaghan’s equation of state. On the other hand, the bulk modulus of 201 GPa and elastic stiffness are separately calculated by an MD simulation using the interatomic potential of eq. (1). The calculated elastic constants are in agreement with reported theoretical and experimental values. $^{23–27)}$

Second, the phonon spectrum is examined. The velocity autocorrelation function is evaluated by MD calculation. Then, this function is Fourier-transformed with respect to time. Most of the typical peaks are consistent with the experimental data obtained from Raman scattering spectroscopy, $^{28)}$ for example, $840\text{cm}^{- 1}$ for the $E_{1}$(LO) mode obtained by the present calculation and $741\text{cm}^{- 1}$ obtained by experiment.

Third, a test MD simulation is performed at pressures lower than 400 GPa to determine the global minimum configuration among the three possible crystal structures (wurtzite, zincblende, and NaCl-type rock-salt structures) under the present two-body interatomic potential. The calculation indicates that the wurtzite-type structure has the lowest energy configuration at lower pressures. The phase transition from the initial rock-salt structure under high pressure to zincblende- or wurtzite-type structures with a four-coordination number takes place at the lower pressures of 9–20 GPa.

### 3. Simulation Model

The MXDORTO code developed by Kawamura $^{29)}$ is used for the present MD simulation. The molecular motion is solved by the Verlet method. The Coulomb interaction is calculated by the Ewald sum method. The argon ions are neutralized before impact, and therefore the potential shown in Table I is for neutral Ar.

Details of the approach we took in the simulation are similar to those in previously reported studies. $^{9,10)}$ All atomic pairs among gallium, nitrogen, chlorine, sodium, and argon are taken into account using the potential of eq. (1). Figure 2 shows the model configuration, where Figs. 2(a)–2(c) are the top view and the side view of the crystal part, and the side view of the entire MD cell, respectively. The small black and intermediate white circles denote Ga and N atoms, respectively. The intermediate gray circles are the Cl and Na atoms. The larger gray circle is the Ar atom.

An MD basic cell consists of $10a \times 6b' \times 8c$ unit cells containing a total of 1920 Ga atoms and 1920 N atoms. The top surface has half-monolayer Cl coverage (60 Cl atoms with $- 0.48e$ charge). Counter 60 Na atoms with $+ 0.48e$ charge are set on the bottom surface to satisfy the charge neutrality condition for the Ewald sum method. In Fig. 2(a), Na atoms on the bottom surface are omitted to clearly show the distribution of Cl atoms. Potential parameters of Cl and Na are determined on the basis of the rock-salt crystal of NaCl. The charge of Cl atoms is estimated by the ab initio method (Gaussian 03) with MP2/3-21G for GaCl₂ and GaCl₃ molecules. $^{30)}$

The bottom one-pair layer of Ga and N atoms of the MD basic cell, 240 atoms, and 60 Na atoms are set to the thermostat of 300 K. The surface area of the MD basic cell is $3.21 \times 3.33\text{nm}^{2}$. The height is 4.31 nm. A vacuum region with a height of 12.28 nm is set along the $C$ direction of the cell. Periodic boundary conditions are employed three dimensionally on the boundary of the cell. MD simulations are performed under the NVE ensemble except for the bottom thermostat layers, where $N$ (number of atoms), $V$ (volume), and $E$ (energy) are kept constant.

First, relaxation calculation of 15 ps without Cl and Na atoms and that of 14 ps with Cl and Na atoms are carried out to attain an equilibrium state. Second, Ar atoms are brought to the surface at normal incidence. Three different energies, 100, 150, and 250 eV, are considered. The incident position is given by random number. A time step of 0.7–1.0 fs is used depending on the Ar energy. In the present study, at each Ar incidence, the motion of all atoms is followed for at least 7 ps. It takes about 3 h CPU time for a single Ar impact event to complete the simulation by using a 2.4 GHz personal computer.

### 4. Calculation Results

Figure 3 shows snapshots at four typical times in the near-surface region. A single Ar atom is initially located at a distance of 1.16 nm from the (0001) surface. The Ar atom is directed normal to the surface at the energy of 150 eV. Figure 3(a) shows both the top view and the side view along

![](./images/811752671659687937_2.jpg)

Fig. 2. Model configuration of the simulation. (a) Top view of the crystal part of an MD cell. (b) Side view of the crystal part. (c) Side view of an entire MD cell.

![](./images/811752671659687937_3.jpg)

Fig. 3. Snapshots of the side and top views of a layer in the near-surface region at four typical times after the ion incidence: (a) 50, (b) 475, (c) 2230, and (d) 3030 fs. A single Ar ion is impinged normal to the (0001) surface at an energy of 150 eV.

the $A$-direction. The Ar ion reaches the top surface at 50 fs at the lower left position.

Figures 3(b)-3(d) show the side views along both the $A$- and $B$-directions. In Fig. 3(b) at 475 fs, collision-cascade takes place circularly with its center at the Ar incident point. As a result, a hot spot is generated and develops in both horizontal and vertical directions. The original hexagonal crystal structure is very disordered at the incident point. Ar is reflected upward. Adsorbed Cl atoms are also physically sputtered out.

At 2230 fs in Fig. 3(c), the hot spot shrinks, and then disappears. The original hexagonal crystal structure is almost recovered. That is, recrystallization takes place. It is noted that a volatile product of a $GaCl_2$ molecule is generated, and that this molecule begins to leave the surface.

At 3030 fs in Fig. 3(d), the $GaCl_2$ molecule is moving upward. Another Ga-Cl product, which is located at the left side of the $GaCl_2$ molecule in the lower figure, also managed to leave the surface, but this has insufficient energy to overcome the surface barrier, and is captured on the surface.

Several types of molecules or clusters are sputtered. Generally, Ga is sputtered in the form of $Ga-Cl_2$, and sometimes in the form of Ga-Cl, Ga-N-Cl, Ga-N, and Ga-$N-Ga-Cl_2$. Bond reconstruction among these molecules/

clusters occurs, especially near the surface region. Ga atoms are not singly sputtered.

The typical time scale of events for incident energies of 100–250 eV is as follows. Atoms escape in the time range of 200–3000 fs after the impact of the incident Ar atom. The shorter time corresponds to physical sputtering. That is, atoms in the crystalline structure are sputtered out owing to the linear collision-cascade mechanism. The longer time corresponds to chemical sputtering. Bond reconstruction among atoms takes place in the hot spot. When an instantaneous volatile product satisfies the following two conditions, it is chemically sputtered. The first condition is that the product has almost charge neutrality. The second condition is that the product has sufficient energy to overcome the surface barrier.

Since the interatomic potential in eq. (1) is a fixed charge model, there always exists Coulomb interaction between sputtered atoms and crystal atoms in the MD cell. In the present calculation, it is judged that atoms are sputtered when they travel upward to a distance of 6.1 nm from the surface. Some of the ejected atoms return to the surface before reaching this distance when the two conditions are not satisfied.

After 200–700 fs, the kinetic energy is distributed among many atoms in the crystalline structure creating a hot spot at the impact region of the Ar atom. After this time, no individual atom has sufficient kinetic energy to overcome the high surface barrier. That is, atoms are not physically sputtered out. The peak of the hot spot generation is at approximately 500 fs. The randomized atoms at the hot spot are recrystallized after about 1500 fs, and the initial wurtzite- type crystal structure is almost recovered. The kinetic energy introduced by the incident Ar atom is finally absorbed by the 300 K thermostat.

The sputtering phenomenon on the surface without a Cl- adsorbed layer, that is, with a clean surface, is different from the case with a Cl-adsorbed layer in several points. The case with the clean surface has already been reported else- where.¹⁴ The essence is as follows. Nitrogen atoms are mostly sputtered. Ga atoms are not sputtered singly, and are always sputtered with N atom in pairs. Atoms in the crystalline structure are sputtered out within about 100 fs after the impact of the incident Ar atom due to the linear collision-cascade mechanism. That is, physical sputtering takes place. After the hot-spot generation, no individual atom has sufficient kinetic energy to overcome the high surface barrier. That is, atoms are not sputtered out.

Figure 4 shows the impact energy dependence of sputter- ing yield for the range of 0 to 250 eV. Two cases, with and without the Cl-adsorbed layer, are compared. The data is averaged with 30 Ar impacts. In the case without the Cl- adsorbed layer, that is, with the clean surface, N atoms are mostly sputtered. In this energy range, Ga sputtering does not take place at all. In the case with the Cl-adsorbed layer, on the other hand, Ga sputtering yield has large finite value for Ar impact. N sputtering yield is similar to the case with the clean surface.

As is expected from the data for the case with the clean surface, if the energetic Ar ion incidence is repeatedly made without refreshing the crystal, the near-surface region in the crystal becomes Ga-rich. Cl-based chemicals such as a Cl₂/ BCl₃/Ar gas mixture are thus necessary for the stoichio- metric etching of GaN crystal. In the present calculation, the threshold energy is approximately 100 eV, except for the case of Ga sputtering with the clean surface.

![](./images/811752671659687937_4.jpg)

Fig. 4. Impact energy dependence of the sputtering yield for N and Ga atoms averaged over 30 Ar impacts. Two cases, with and without a Cl- adsorbed layer, are compared.

The main issue to be solved in the present model is the treatment of the atomic charge. The charge should be dynamically changed depending on the bond condition. The dynamic charge model is, however, very time-consuming at present, when charges are determined on the basis of the chemical potential at each time step. A qualitative picture of the present calculation of chemical sputtering is fundamen- tally plausible, but quantitative evaluation should be further examined.

## 5. Conclusions

A molecular dynamics simulation has been carried out to investigate the chemical sputtering of Cl-adsorbed wurtzite- type GaN(0001) surfaces. Sputtering yield is examined with 30 Ar impacts at three energies, 100, 150, and 250 eV. Ga sputtering does not take place at all on the clean surface, whereas Ga sputtering yield has large finite value for Ar impact on the Cl-adsorbed surface. Generally, Ga is sputtered in the form of Ga–Cl₂, and sometimes in the form of Ga–Cl, Ga–N–Cl, Ga–N, and Ga–N–Ga–Cl₂. Ga atoms are not singly sputtered. Atoms escape from the surface in the time range of 200–3000 fs after the impact of the incident Ar atoms. The shorter and longer escape times correspond to physical and chemical sputtering, respectively.

## Acknowledgement

We acknowledge the financial support of a Grant-in-Aid for Scientific Research (No. 19540527) from the Japan Society for the Promotion of Science.

1) J. S. Cabalu, A. Bhattacharyya, C. Thomidis, I. Friel, and T. D. Moustakas: J. Appl. Phys. 100 (2006) 104506.
2) S. Nakamura, M. Senoh, S. Nagahama, N. Iwasa, T. Yamada, T. Matsushita, H. Kiyoku, Y. Sugimoto, T. Kozaki, H. Umemoto, M. Sano, and K. Chocho: Jpn. J. Appl. Phys. 37 (1998) L309.
3) L. Zhang, J. Ramer, J. Brown, K. Zheng, L. F. Lester, and S. D. Hersee: Appl. Phys. Lett. 68 (1996) 367.
4) Y. Lacroix, T. Nakanishi, and S. Sakai: Proc. Int. Workshop Nitride Semiconductors, Nagoya, 2000 (IPAP, Tokyo, 2000) IPAP Conf. Ser. 1.

08JE03-4
© 2010 The Japan Society of Applied Physics

p. 782.

5) I. Adesida, A. Mahajan, E. Andideh, M. A. Khan, D. T. Olsen, and J. N. Kuznia: Appl. Phys. Lett. 63 (1993) 2777.

6) S. J. Pearton, C. R. Abernathy, and F. Ren: Appl. Phys. Lett. 64 (1994) 2294.

7) I. Adesida, A. T. Ping, C. Youtsey, T. Dow, M. A. Khan, D. T. Olson, and J. N. Kuznia: Appl. Phys. Lett. 65 (1994) 889.

8) M. E. Barone, T. O. Robinson, and D. B. Graves: IEEE Trans. Plasma Sci. 24 (1996) 77.

9) D. E. Hanson, A. F. Voter, and J. D. Kress: J. Appl. Phys. 82 (1997) 3552.

10) M. E. Barone and D. B. Graves: J. Appl. Phys. 78 (1995) 6604.

11) H. Feil, J. Dieleman, and B. J. Garrison: J. Appl. Phys. 74 (1993) 1303.

12) J. Nord, K. Nordlund, and J. Keinonen: Phys. Rev. B 68 (2003) 184104.

13) K. Harafuji and K. Kawamura: Abstr. 18th Int. Symp. Plasma Chemistry, 2007, p. 43.

14) K. Harafuji and K. Kawamura: Jpn. J. Appl. Phys. 47 (2008) 1536.

15) K. Harafuji and K. Kawamura: Proc. Plasma Science Symp. 2009 and 26th Symp. Plasma Processing, 2009, p. 98.

16) K. Harafuji and K. Kawamura: Proc. 31th Int. Symp. Dry Process, 2009, p. 13.

17) K. Harafuji and K. Kawamura: Jpn. J. Appl. Phys. 49 (2010) 011001.

18) K. Harafuji, T. Tsuchiya, and K. Kawamura: Jpn. J. Appl. Phys. 43 (2004) 522.

19) V. R. Sanders, R. Dovesi, C. Roetti, M. Causa, N. M. Harrison, R. Orlando, and C. M. Zicovich Wilson: CRYSTAL 98, User's manual, University of Torino (Italy) and CLRC Daresburg Laboratory (UK) (1999).

20) K. Harafuji, T. Tsuchiya, and K. Kawamura: J. Appl. Phys. 96 (2004) 2501.

21) K. Harafuji, T. Tsuchiya, and K. Kawamura: J. Appl. Phys. 96 (2004) 2513.

22) K. Harafuji and K. Kawamura: Jpn. J. Appl. Phys. 44 (2005) 6495.

23) K. Shimada, T. Sota, and K. Suzuki: J. Appl. Phys. 84 (1998) 4951.

24) A. F. Wright: J. Appl. Phys. 82 (1997) 2833.

25) M. Yamaguchi, T. Yagi, T. Azuhata, T. Sota, K. Suzuki, S. Chichubu, and S. Nakamura: J. Phys.: Condens. Matter 9 (1997) 241.

26) R. B. Schwarz, K. Khachaturyan, and E. R. Weber: Appl. Phys. Lett. 70 (1997) 1122.

27) T. Tsuchiya, K. Kawamura, O. Ohtaka, H. Fukui, and T. Kikegawa: Solid State Commun. 121 (2002) 555.

28) H. Harima: J. Phys.: Condens. Matter 14 (2002) R967.

29) K. Kawamura: Japan Chemistry Program Exchange, 1996, P029.

30) Gaussian 03, Revision E.01, User's Reference (Gaussian, Inc., Wallingford, CT, 2004).
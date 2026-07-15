
# Bonding in MgSi and AlMgSi Compounds Relevant to AlMgSi Alloys

Anders G. Frøseth \( ^{*} \)  and Ragnvald Høier

Norwegian University of Science and Technology (NTNU), N-7034 Trondheim, Norway

Peter M. Derlet

Paul Scherrer Institute, CH-5232 Villigen PSI, Switzerland

Sigmund J. Andersen and Calin D. Marioara

SINTEF Materials Technology, Applied Physics, N-7050 Trondheim, Norway
(Dated: September 14, 2018)

The bonding and stability of MgSi and AlMgSi compounds relevant to AlMgSi alloys is investigated with the use of  \( (\mathrm{L})\mathrm{APW}+(\mathrm{lo}) \)  DFT calculations. We show that the  \( \beta \)  and  \( \beta^{\prime\prime} \)  phases found in the precipitation sequence are characterised by the presence of covalent bonds between Si-Si nearest neighbour pairs and covalent/ionic bonds between Mg-Si nearest neighbour pairs. We then investigate the stability of two recently discovered precipitate phases, U1 and U2, both containing Al in addition to Mg and Si. We show that both phases are characterised by tightly bound Al-Si networks, made possible by a transfer of charge from the Mg atoms.

## I. INTRODUCTION

Precipitation or age hardened alloys are today one of the most important alloy types in industry. In the AlMgSi alloy system, Mg-Si and Al-Mg-Si precipitates formed during specific heat treatments give rise to a very significant increase in strength. The precipitation sequence is generally accepted to be:

 \[ S S S S\rightarrow\mathrm{M g}/\mathrm{S i~C l u s t e r s}\rightarrow G P Z\rightarrow\beta^{\prime\prime}\rightarrow\beta^{\prime}\rightarrow\beta, \quad (1) \] 

where GPZ refers to a Guinier Preston Zone and SSSS refers to a Super Saturated Solid Solution. Very little is known about the early stages of the precipitation process. However, it is believed that when the SSSS is heat treated Mg and Si atoms quickly diffuse substitutionally to form small clusters due to the large amount of quenched-in vacancies \( ^{1} \)  (a large part of the vacancies move to interfaces like surfaces and grain boundaries in the later stages of the heat treatment). Although the details are hard to investigate experimentally, several studies of such clustering have been carried out using atom probe microscopy \( ^{2,3} \) . The first phase which can be resolved using high resolution electron microscopy (HREM) is the GPZ. From this, a model of its crystal structure has recently been proposed \( ^{4} \) . The structure of the proceeding phase,  \( \beta^{\prime\prime} \) , was also solved using electron microscopy techniques \( ^{5} \) , a result which has later been supported by ab initio calculations \( ^{6} \) .

Earlier it was believed that the GPZ,  \( \beta^{\prime\prime} \)  and  \( \beta \)  phases all had the stoichiometry of the  \( \beta \) -phase,  \( Mg_{2}Si \) , and that alloys should be optimized accordingly. Thus, the terminal  \( \beta \) -phase was of primary importance. Later however, it had been confirmed that the  \( \beta^{\prime\prime} \)  gives a greater contribution to the hardness due to its semi-coherent interface with the aluminium matrix and needle-like shape, which is more effective for dislocation pinning \( ^{7} \) . The  \( \beta^{\prime\prime} \)  stoichiometry has been shown to be  \( Mg_{5}Si_{6} \)  \( ^{5} \) .
Recently, several additional phases have been identified experimentally \( ^{8,9,10} \) , giving the extended precipitation sequence:

 \[ \begin{aligned}S S S S\rightarrow M g/S i C l u s t e r s\rightarrow G P Z\rightarrow\beta^{\prime\prime}\\ \rightarrow(\beta^{\prime}+U2+U1+B^{\prime})\rightarrow\beta.\end{aligned} \quad (2) \] 

In ref. 8 the phases U1, U2 and  \( B' \)  are referred to as type A, B and C respectively. These three phases, in addition to  \( \beta' \) , are often grouped together since little is known about their interdependence. However it is believed that the peak of concentration with respect to time for each of these structures follows the ordering given by the above precipitation sequence \( ^{8} \) . They all form relatively late in the precipitation sequence usually at temperatures in the range 200-300 °C, and in Si-rich alloy compositions.

It has been considered a general rule of thumb that successful aluminium precipitation hardening alloys contain secondary and ternary alloying elements which are larger and smaller than aluminium \( ^{11} \) . Now, the concept of atom size in this context must be based on the type of bonding involved. One can have either ionic, metallic or covalent radii for the constituent elements giving dramatically different values for atomic size \( ^{12} \) . It is clear that when studying the electronic density of compound structures this type of concept may lead to an oversimplification. It is therefore interesting to carry out a theoretical study of the electronic structure and bonding characteristics of the relevant phases with respect to their relative stability. This is the purpose of the present work, where we employ full potential ab initio methods based on Density Functional Theory (DFT) to investigate the bonding within the above mentioned structures. In section II we describe the Linear Augmented Plane Wave + local orbitals approach, (L)APW+(lo), used for all calculations. Section III describes the results obtained for the three models of precipitate phases containing only Mg and Si ( \( \beta'' \) ,  \( \beta' \) , and  \( \beta \) ), and section IV deals with the phases containing Al, Mg and Si (U1 and U2).
 

## II. METHOD

The ab initio calculations were performed using WIEN2k, a program package implementing the full potential (L)APW+(lo) DFT method \( ^{13} \) . The Augmented Plane Wave approach (APW)+(lo) method \( ^{14} \)  differs from the LAPW method in the linearization of the APW's. In slater's original APW method \( ^{15} \)  the unit cell is partitioned into non-overlapping atomic spheres and an interstitial region. The basis functions are plane waves for the interstitial region and radial wave functions within the atomic spheres. In the LAPW method the basis functions inside the spheres are linearized with respect to the energy  \( E_{l} \) :

 \[ \psi_{\mathbf{k}_{n}}(\boldsymbol{r})=\sum_{l m}(A_{l m,\mathbf{k}_{n}}u_{l}(r,E_{l})+B_{l m,\mathbf{k}_{n}}\dot{u}_{l}(r,E_{l}))Y_{l m}(\hat{\boldsymbol{r}}) \quad (3) \] 

where  \( u_{l}(r,E_{l}) \)  are radial functions and  \( Y_{lm}(\boldsymbol{r}) \)  are spherical harmonics.  \( \dot{u}_{l}(r,E_{l}) \)  is the energy derivative of  \( u_{l}(r,E_{l}) \) .  \( A_{lm,\mathbf{k}_{n}} \)  and  \( B_{lm,\mathbf{k_{n}}} \)  are determined by matching the above basis to the value and derivative of the plane waves for each k-vector at the sphere boundary. An alternative way for doing the linearization is the APW+lo method. One starts with the original APW's and adds local orbitals to obtain the variational flexibility in the basis functions.

 \[ \psi_{\mathbf{k}_{n}}(\boldsymbol{r})=\sum_{l m}(A_{l m,\mathbf{k}_{n}}u_{l}(r,E_{l})+\phi_{l o})Y_{l m}(\hat{\boldsymbol{r}}) \quad (4) \] 

 \[ \phi_{l o}=B_{l m}u_{l}(r,E_{l})+C_{l m}\dot{u}_{l}(r,E_{i}) \quad (5) \] 

At first sight this looks very similar to the LAPW basis. However, the  \( B_{lm} \)  and  \( C_{lm} \)  are no longer dependent on the wave-vector and are determined by the requirement that the local orbital is zero at the sphere boundary and normalized. The great advantage of this scheme is that the calculations converge to results almost identical with those of the LAPW method but for dimensioning parameters which effectively leads to a smaller basis set \( ^{16} \) . The WIEN2k code uses a mixed APW+lo/LAPW basis set, exploiting the advantages of both methods.

To make the results for the different structures comparable, we used the same set of APW+(lo) parameters for all calculations:  \( R_{mt} = 2.1 \)  Bohr,  \( R_{mt}k_{max} = 7 \)  and  \( G_{max} = 14 \)  Ry \( ^{1/2} \) . Here,  \( R_{mt} \)  is the muffin tin radius,  \( K_{max} \)  is the plane wave cut-off and  \( G_{max} \)  the maximum Fourier component of the electron density. For all calculations we used the modified tetrahedron method \( ^{17} \)  for Brillouin zone integrations. All k-point meshes were checked for convergence. Thus in general, the highly symmetric structures (like bulk Al, Si and Mg) with few symmetrically inequivalent atoms in the unit cell, require a denser k-point mesh than the precipitate phases with larger unit cells and a lower symmetry. For the exchange-correlation potential we used the Generalized Gradient Approximation (GGA) of Perdew et. al \( ^{18} \) 

![](./images/867771569798119566_1.jpg)

FIG. 1: Conventional unit cell for fluorite  \( Mg_{2}Si \) , equivalent to the  \( \beta \)  phase in the AlMgSi precipitation sequence. The large spheres are Mg atoms and the smaller ones are Si.

## III. MgSi PHASES

## A.  \( \beta \) 

The  \( \beta \)  phase (fluorite  \( Mg_{2}Si \) ) is the terminal equilibrium structure of the precipitation sequence. It has a fcc primitive unit cell (space group  \( Fm\bar{3}m \)  (225)), with an experimental lattice parameter  \( a=6.39\ \AA^{4} \) . It forms precipitates of a plate-like or cubic shape up to  \( 20\ \mum \)  in diameter. Its interface with the Al matrix is fully incoherent \( ^{4} \) . The conventional unit cell, containing 8 Mg atoms and 4 Si atoms, is shown in fig. 1. As can be seen, each of the Si atoms in the structure has 8 Mg nearest neighbours, giving each Mg atom 4 Si nearest neighbours at the same distance. The Si atoms are arranged as an fcc lattice interpenetrated by a sc Mg lattice.

Several ab initio studies of the bonding in Fluorite  \( Mg_{2}Si \)  have been carried out in the past \( ^{19,20,21} \) . However, to our knowledge, none of these involved the LAPW or  \( (\mathrm{L})\mathrm{APW}+(\mathrm{lo}) \)  DFT method. For our calculations we use the experimentally observed lattice constant for this phase in the Al matrix: 6.39 Å. Performing a volume relaxation, this value differed by only 0.25 % from the calculated optimized value 6.37 Å, and by 0.6 % from the experimental value for bulk  \( Mg_{2}Si \) , 6.338 Å \( ^{22} \) . The calculated bulk modulus, derived from a second order Birch fit, was 54.3 GPa, compared to 59 GPa from experiment \( ^{22} \) . Using the 6.39 Å lattice constant the nearest neighbour (nm) Mg-Si distance is 2.77 Å, the Si-Si nm distance is 4.51 Å and the Mg-Mg nm distance is 3.29 Å.

Past linear-combination-of-atomic-orbitals Hartree Fock and DFT pseudopotential calculations \( ^{19,21} \)  indicate considerable charge transfer from the electropositive Mg atoms to the electronegative Si atoms resulting in a partly ionic Si-Mg bond for the  \( \beta \)  phase. This result is also supported by the present work. Fig. 2 displays the bonding charge density for the (101) plane of fig. 1. We define the bonding charge density as the difference between the converged valence charge density from DFT.
 
![](./images/867771569798119566_2.jpg)

FIG. 2: Bonding charge density for (101) plane. The two central peaks are Mg atoms. The four corner peaks are Si atoms. Thick lines represent positive contour lines and thin lines represent negative contour lines.

and the charge density derived from the isolated neutral atoms. Thus the bonding charge density indicates the charge transfer resulting from the converged electronic structure. In fig. 2, the thick lines represent positive contours corresponding to charge transfer to the region, while the thinner lines represent negative contours corresponding to charge transfer away from the region. The concentration of thick lines around the Si atoms thus displays a net build up of charge around the Si atoms counterbalanced by a net reduction of charge around the central Mg atoms, indicating that some ionicity is indeed at play.

Fig. 3 displays the corresponding total and partial electronic density of states (DOS) for the  \( \beta \)  phase. Here the partial DOS represents the "Muffin tin decomposed" DOS for both the Mg and Si atoms, in which the occupied states are projected onto the muffin tin eigenvectors (see section II) of the particular atom. In this way, some information can be gained on the local DOS at each atom, however such a procedure is not complete since the interstitial region cannot be locally resolved. On the other hand, the total DOS represents the DOS derived from all the "Muffin tin decomposed" DOS and the interstitial DOS of the entire computational cell. Note that the calculation is based on the primitive unit cell, containing 1 symmetrically inequivalent Si atom and 2 symmetrically inequivalent Mg atoms, thus the partial Mg DOS contains the contribution for 2 Mg atoms, and the Si DOS the contribution from 1 Si atom.

A general feature of the total and partial DOS in fig. 3 is the two broad bands below the Fermi energy (indicated by the horizontal line at 0.26 Ry) separated by an energy of approximately 0.4 Rydbergs. That the occupancy is dominated by Si states, where the partial Mg DOS represents the two inequivalent Mg atoms, is a further indication of the presence of ionicity whereby the Mg has simply donated electrons to the Si. In addition, this phase has a band-gap. The magnitude of the gap

![](./images/867771569798119566_3.jpg)

FIG. 3: Muffin tin decomposed DOS for the  \( \beta \)  phase. Note that the atomic Mg DOS is half the magnitude of the total Mg DOS. The vertical line represents the fermi level.

at the  \( \Gamma \) -point is 0.13 Ry (1.77 eV), which is somewhat smaller than the experimental value of 2.27 eV for a lattice constant of 6.338 Å \( ^{23} \) .

Figs. 4a and b now display the s, p and d decomposed partial DOSs for both Si and the two inequivalent Mg atoms. In this case, the total DOS represents the total muffin tin decomposed DOS for the particular atom, that is, the sum of the s, p and d partial DOSs. Inspection of fig. 4a reveals that the lower band consists of s states where as the upper band consists of predominantly p states with a little s state character. For the case of the Mg, fig. 4b, the DOS below the Fermi level largely mimics that of Si apart from both occupied bands being of mixed s and p character.

Insight into the general features of the DOSs shown in fig. 4 can be understood from the perspective of beginning with pure fcc Si with a lattice constant of 6.39Å, giving a rather large nn Si-Si separation of 4.52Å. For such a system there can be no strong hybridization between the atomic valence s and p states, maintaining a gap of approximately 0.3 Ry in the corresponding DOS (not shown). The s and p band centers differ by about 0.4 Ry, which is not so dissimilar from the 0.49 Ry difference between the isolated atom 3s and 3p valence states. With the addition of the interpenetrating cubic array of Mg atoms, both bands broaden reducing the gap to about 0.2 Ry. Thus in fig. 4a, the dominant s character of the filled lower band and the dominant p character of the upper filled band arises from the strong onsite Si orthogonality requirement, whereas in fig. 4 the mixed s and p character of the corresponding Mg bands arises from the Mg-Si s and p matrix interaction elements. We note that the corresponding heights of the Mg total DOS are significantly less than the Si DOS, following approximately the square-root dependence of a metallic DOS. Thus, through charge transfer to the Si, the Mg plays the role of “strengthening” the Si backbone lattice, provid-
 

a)

![](./images/867771569798119566_4.jpg)

b)

![](./images/867771569798119566_5.jpg)

FIG. 4: a) Si and b) Mg muffin tin decomposed DOS for the  \( \beta \)  phase. Note that for the Si DOS, the s-curve is practically superimposed on the total-curve for the lower band in the range -0.4 to -0.25 Ry. Scaled square-root curve shown for comparison.

ing an explanation of the origin of the  \( \beta \)  phase band gap through the pulling down of the excited s, p and d states of atomic Si.

## B.  \( \beta^{\prime\prime} \) 

The  \( \beta^{\prime\prime} \) -phase has a base-centred-monoclinic conventional unit cell (space group  \( C2_{m} \) ) with experimental lattice parameters  \( a = 15.16 \, \AA \) ,  \( b = 6.74 \, \AA \) , c = 4.05 Å, and  \( \gamma_{ab} = 105.3^\circ \)  \( ^{5} \) . Fig. 5 displays the conventional cell for two viewing orientations. This phase forms precipitates of a needle-like shape, typically with a thickness of 30-50 Å and a length of 300-400 Å. The needle length, which is along the <001> direction of the  \( \beta^{\prime\prime} \) -phase unit cell, runs parallel to the <001> direction of the Aluminium matrix. For the present work we use the experimentally derived lattice parameters and the relaxed atomic positions of the inequivalent Si and Mg atoms by minimizing the forces by a Newton-Coates procedure with respect to the C2/m space group. The resulting inequivalent atomic coordinates are listed in table I. The given space group of this phase was first solved by high resolution

![](./images/867771569798119566_6.jpg)

a)

![](./images/867771569798119566_7.jpg)

b)

FIG. 5: Conventional unit cell for  \( \beta^{\prime\prime} \)  seen from a) < 001 > direction, and b) slightly away from the < 010 > cartesian direction. The large circles represent Mg and the small circles Si.

TABLE I: Relaxed fractional coordinates for the inequivalent atomic positions of the  \( \beta^{\prime\prime} \)  phase.

<table><tr><td>Atom</td><td>a</td><td>b</td><td>c</td></tr><tr><td>Mg1</td><td>0.0</td><td>0.0</td><td>00</td></tr><tr><td>Mg2</td><td>0.346(1)</td><td>0.071(9)</td><td>00</td></tr><tr><td>Mg3</td><td>0.421(6)</td><td>0.063(6)</td><td>00</td></tr><tr><td>Si1</td><td>0.055(7)</td><td>0.662(7)</td><td>00</td></tr><tr><td>Si2</td><td>0.194(4)</td><td>0.250(5)</td><td>00</td></tr><tr><td>Si3</td><td>0.209(1)</td><td>0.627(5)</td><td>00</td></tr></table>

electron microscopy techniques \( ^{5} \)  and later supported by FLAPW DFT calculations \( ^{6} \) . Fig. 6 displays the bonding charge density contour plot for the (002) plane. A dominant feature is the concentration of charge between the Si nearest neighbours, and to a lesser extent between the Si and Mg nearest neighbours, indicating that covalency is at play in this system \( ^{6} \) . Such charge transfer to the bonding regions originates from the core regions of both the Si and Mg atoms, in addition to the homogeneous interstitial region between the Mg atoms. The depletion of charge from the Mg is comparable to that seen in the  \( \beta \) -phase, indicating that for this system both ionicity and covalency is present in the bonding. The nearest neighbour distance range in this structure is 2.39-2.53 Å for Si-Si and 2.61-2.84 Å for Si-Mg. This is not dissimilar to the nearest neighbour distance of 2.33 Å in covalently bonded diamond cubic Si and 2.76 Å in the covalent/ionic equilibrium  \( \beta \)  phase. Moreover, one of the inequivalent Si atoms is  \( sp^{3} \)  (tetrahedrally) coordinated and another is  \( sp^{2} \)  coordinated \( ^{6} \) . Fig. 7 displays the Total DOS (including the muffin tin and interstitial regions) for the  \( \beta \)  phase. Unlike the  \( \beta' \)  phase, there is no band gap.
 
![](./images/867771569798119566_8.jpg)

FIG. 6: Bonding charge density for (002) plane section of the  \( \beta^{\prime\prime} \)  Structure. Thick contour lines represent a positive charge transfer, while thin lines represent a negative charge transfer.

![](./images/867771569798119566_9.jpg)

FIG. 7: Total DOS for the  \( \beta^{\prime\prime} \)  phase. The vertical line represents the fermi level.

However, depressions can be identified at -0.1 and 0.4 Rydbergs reminiscent of the gaps seen in fig. 3. By inspection of the partial DOS for each inequivalent atom we find that for the Si atoms there is a dominant s character for the lower energy states (< -0.2 Ry), whereas, at about 0.2 Ry, the p character dominates. In between these regimes, a mixture of p and s character exists, indicating strong hybridization. Indeed fig. 8a displays the partial DOS for Si2, which from past work is locally  \( sp^{3} \)  coordinated \( ^{6} \) , showing approximate correspondence with the diamond cubic Si DOS \( ^{24} \) . In particular the dominant s character of the  \( L_{2'} \) , the s and p character of the  \( \mathrm{L}_{1} \)  and the dominant p character of  \( X_{4} \)  the high symmetry points. Alternatively, fig. 8b shows the partial DOS for Mg3, which from charge density profile analysis \( ^{6} \)  is in a homogeneous metallic environment, displaying an approximate shifted metallic square-root behaviour.

a)

![](./images/867771569798119566_10.jpg)

b)

![](./images/867771569798119566_11.jpg)

FIG. 8: Partial DOS for the a) Si2 and b) Mg3 (see table. I) atom in the  \( \beta^{\prime\prime} \)  phase.

TABLE II: Fractional coordinates for the inequivalent atomic positions of the U1 phase \( ^{9} \) .

<table><tr><td>Atom</td><td>a</td><td>b</td><td>c</td></tr><tr><td>Mg</td><td>0.0</td><td>0.0</td><td></td></tr><tr><td>Al</td><td>1/3</td><td>2/3</td><td>0.632(8)</td></tr><tr><td>Si</td><td>1/3</td><td>2/3</td><td>0.243(8)</td></tr></table>

## IV. AlMgSi PHASES

## A. U1

The U1 conventional/primitive unit cell is trigonal (space group  \( P_{3m1} \) ) with experimentally derived lattice parameters  \( a = b = 4.05 \, \AA \) , and  \( c = 6.74 \, \AA \) . It contains 1 Mg, 2 Al, and 2 Si atoms giving the formula  \( MgAl_{2}Si_{2} \) . The unit cell and atomic positions are shown in table II and fig. 9. Experiments show that the  \( <001> \)  direction of the U1 unit cell runs parallel to the  \( <310> \)  direction of the fcc Al matrix \( ^{9} \) . The U1 phase usually forms rod-like precipitates with a length of 50-500 nm and a width of approximately 50 nm. Performing a volume relaxation, we found the calculated unit cell equilibrium volume to differ by only 1% from the experimentally derived unit cell volume. From a second order Birch fit we
 
![](./images/867771569798119566_12.jpg)

FIG. 9: U1 conventional unit cell in a) perspective and b) < 001 > direction. The small, black spheres are Si atoms, the large dark spheres Al atoms, and the large white spheres Mg atoms.

obtained a bulk modulus of 71 GPa.

The U1 phase can be categorized as belonging to a class of structures given the name  \( CaAl_{2}Si_{2} \) -type Zintl compounds \( ^{25} \) . In Zintl compounds, the electropositive elements are thought of as merely electron donors to the electronegative elements which thereby are able to fulfill the octet rule. For  \( MgAl_{2}Si_{2} \)  this implies that each Mg atom donates two electrons to  \( Al_{2}Si_{2} \)  for each unit cell. This gives  \( Al_{2}Si_{2}^{2-} \) , or two units of  \( AlSi^{-} \) which is isoelectronic to AlN, fulfilling the octet rule. The resulting layered structure is sketched in fig. 10.  \( AlSi^{-} \) constitutes a double layer of tightly bound “chair-like” six-membered rings separated by layers of hexagonal  \( Mg^{2+} \) . In the Al-Si network, each Si atom bonds to 4 Al atoms forming an umbrella-like structure, while each Al atom forms the more common tetrahedral structure with 4 nearest neighbour Si atoms. The Al-Si bond length within each AlSi layer is 2.48 Å, while the length of the Al-Si bonds connecting the two  \( AlSi^{-} \) layers is 2.62 Å. The length of the Mg-Si bond is 2.86 Å (see below and fig. 11), somewhat larger than the length of the partly ionic bond in the  \( \beta \)  equilibrium structure, but similar to Mg-Si bonds found in the  \( Mg_{5}Si_{6} \)   \( \beta^{\prime\prime} \)  phase \( ^{6} \) .

The calculated bonding charge density for the (110) plane is shown in fig 11. There is a clear concentration of charge between the Al and Si atoms indicating strong

![](./images/867771569798119566_13.jpg)

FIG. 10: U1 bonding network

Bonding Charge Density for 110 Plane Section

![](./images/867771569798119566_14.jpg)

FIG. 11: U1 bonding charge density for the (110) plane. Thick lines represent contour levels with a positive value, thin lines a negative value.

Al-Si bonding. There is also a small build-up of charge between the Si and corner Mg atoms which constitutes a coupling between  \( Mg^{2+} \)  and AlSi \( ^{-} \)  layers.

Evidence of the layered structure can also be found in the DOS. Figs. 12 and 13 show the muffin tin decomposed total and partial DOS. The total DOS below the fermi level is characterized by two broad bands, separated by a 0.1 Ry band gap (fig. 12a). It is also evident that the major contribution to the total DOS stems from the Al and Si states. This is an indication that the Mg donates charge to the Al-Si network and is not strongly involved in the electronic bonding. Furthermore, the Si states give a relatively larger contribution to the total DOS than the Al states. From the angular decomposed Si DOS (fig. 12b) one can see that the contribution to the lower band comes mainly from Si s states, while the higher band consists mainly of p states with a modest mixing in of s-states. This can be seen as an indication of a partial hybridization of the Si states resulting in the Si bonding environment being partly covalent. This hybridization can also be identified in the Al DOS (fig. 13a). Compared to a metallic DOS \( ^{12} \) , there is a peak concentration of s states with mixed in p states slightly below 0 Ry resembling the  \( L_{1} \)  lobe of a covalent DOS. However for both Al and Mg (fig. 13b), the overall shape of the to-
 

a)

![](./images/867771569798119566_15.jpg)

b)

![](./images/867771569798119566_16.jpg)

FIG. 12: a) total and b) Si muffin tin decomposed DOS for the U1 phase. Note that the Al and Si DOS consists of the contribution from 2 symmetrically equivalent atoms, while the Mg DOS stems from only one atom. One therefore has to divide by a factor two to get the atomic DOS for Al and Si.

tal atomic DOS seems roughly to follow the square-root relationship characteristic of a metallic DOS.

The origin of the band gap at the centre of the occupied states can be understood from the same line of reasoning as for the  \( \beta \)  phase. In the U1 phase, the Si atoms are arranged as an hcp lattice with lattice parameters  \( a = 4.05 \, \AA \)  and  \( c = 6.74 \, \AA \) . If we once again consider only the Si system (with a nearest neighbour distance of  \( 4.05 \, \AA \) ), then little hybridization of the atomic Si s and p valence states can be expected and a similar DOS to the  \( \beta \)  is seen. That is, the occupied valence states will be separated into two relatively narrow bands. By introducing the Al and Mg, the Al forms a tightly bound bonding network with the silicon via the donation of charge from the Mg atoms. This coupling results in a broadening (with respect to the artificial Si sub-structure) of the two occupied bands and in the removal of the band gap seen in  \( \beta \) . This has its origins in the stronger mixed s and p character of the second occupied band (centred at  \( \approx -0.2 \, Ry \) ) of Si (fig. 12b), when compared to the strong p character of the corresponding band for  \( \beta \)  (fig. 4) — indicating strong hybridization between the Si p states and the Al s and p states.

a)

![](./images/867771569798119566_17.jpg)

b)

![](./images/867771569798119566_18.jpg)

FIG. 13: a) Al and b) Mg muffin tin decomposed DOS for the U1 phase.

## B. U2

The U2 primitive/conventional unit cell is orthorhombic (space group  \( P_{nma} \) ) with experimentally derived lattice parameters  \( a = 6.75\AA \) ,  \( b = 4.05\AA \) , and  \( c = 7.94\AA \) . It contains 4 Mg, 4 Al, and 4 Si atoms giving the formula  \( Mg_{4}Al_{4}Si_{4} \)  (fig. 14). The coordinates of the symmetrically inequivalent atoms of the unit cell are shown in table III. The morphology and size of the precipitate formed by the U2 phase is usually the same as for the U1 phase. The  \( <100> \)  direction of the unit cell is oriented parallel to the  \( <310> \)  direction of the fcc Al matrix \( ^{10} \) . By performing a volume relaxation of the unit cell, we get an equilibrium volume differing by less than 1% from the experimentally derived unit cell volume. A second order Birch fit gives a bulk modulus of 69.1 GPa, very close to the value obtained for the U1 phase.

The U2 phase is similar to the TiNiSi structure type \( ^{26,27} \) . As for the U1 phase, the bonding in the U2 phase is characterized by the electropositive Mg atoms donating charge to the electronegative Al and Si atoms forming a tightly bound bonding network (fig. 15). However, unlike for the U1 phase, the electropositive Mg atoms retain a large amount of charge and (using a simple chemical picture) there is not enough transfer for the electronegative elements to fulfill the octet rule \( ^{27} \) . The Al-Si
 
![](./images/867771569798119566_19.jpg)

a)

![](./images/867771569798119566_20.jpg)

b)

FIG. 14: U2 conventional unit cell in a) perspective and b) < 010 > direction

![](./images/867771569798119566_21.jpg)

FIG. 15: U2 bonding network

bond lengths are all 2.59 to 2.61Å, while the bond lengths of the Mg-Si neighbour coupling is 2.78 and 2.86Å.

Fig. 16 displays the bonding charge density maps for the  \( (040) \) ,  \( (020) \)  and  \( (040) \(  planes of the U2 unit cell. As for the U1 phase, there is a concentration of charge between Al and Si nearest neighbours making up the AlSi bonding network. This charge concentration appears to have more of a covalent, directional character, than the U1 Al-Si bond. Furthermore, one can identify a more pronounced charge concentration in between Mg-Si neighbours than for the U1 phase. This fits well with

TABLE III: Fractional coordinates for the inequivalent atomic positions of the U2 phase unit cell \( ^{10} \) .

<table><tr><td>Atom</td><td>a</td><td>b</td><td>c</td></tr><tr><td>Mg</td><td>0.034(9)</td><td>3/4</td><td>0.327(4)</td></tr><tr><td>Al</td><td>0.361(4)</td><td>1/4</td><td>0.432(5)</td></tr><tr><td>Si</td><td>0.239(3)</td><td>1/4</td><td>0.120(9)</td></tr></table>

![](./images/867771569798119566_22.jpg)

Bonding Charge Density for 020 Plane Section

![](./images/867771569798119566_23.jpg)

Bonding Charge Density for 0–40 Plane Section

![](./images/867771569798119566_24.jpg)

FIG. 16: Bonding charge density for a) (040) plane b) (020) plane and c) (040) plane of the U2 unit cell. Thick lines represent contour levels with a positive value, thin lines a negative value.

the general assumption for this structure class — that a large amount of Mg charge is retained. As for the U1 phase there is no indication of charge build-up between Al and Mg neigbour, indicating that the AlSi network is mainly coupled to the Mg atoms via the Si atoms.

This picture is further justified by the total and partial DOS shown in figs. 17 and 18. Comparing the DOS of the U2 phase with the DOS of the U1 phase one can identify several common features, supporting the proposition that the electronic bonding picture is very similar for the two phases. Note that the total DOS is the sum of 1 Mg, 1 Al, and 1 Si atom, as opposed to 1 Mg, 2 Al, and 2 Si atom for the U1 phase (fig. 12a). From the atom decomposed DOS of the U2 phase (fig. 17a) one can see that the Al and Si states are dominating with respect
 

a)

![](./images/867771569798119566_25.jpg)

b)

![](./images/867771569798119566_26.jpg)

FIG. 17: a) total and b) Si muffin tin decomposed DOS for the  \( U^{2} \)  phase.

to the Mg states, and that the Si states give a slightly larger contribution than the Al states. This is consistent with the donation of charge from Mg to Al+Si atoms, as in the case of U1. However, the Mg DOS gives a larger contribution to the total DOS than for the U1 phase. This is an indication that there is less Mg to Al and Si charge transfer, than for the U1 Zintl-type phase. We remind the reader that it is difficult to quantify the charge transfer because the (L)APW+(lo) method does not use an atomic/localised basis set. Furthermore, the magnitude of the band gap separating the two occupied bands is slightly smaller for the U2 phase than for the U1 phase (0.075 Ry vs. 0.1 Ry for the U1 phase). Consequently, the region of hybridization around 0 Ry is increased for the Al and Si DOS (fig. 18 a and b) consistent with the pronounced covalent character of the Al-Si bonds found in the bonding charge density.

As for the U1 and  \( \beta \)  phase, the origin of the band gap in the occupied states can be explained by the separation of the Si atoms with respect to each other, which for this structure forms a slightly distorted h.c.p structure (not shown here) with lattice parameters comparable to those of the U1 Si hcp sub-lattice.

a)

![](./images/867771569798119566_27.jpg)

b)

![](./images/867771569798119566_28.jpg)

FIG. 18: a) Al and b) Mg muffin tin decomposed DOS for the U2 phase.

## V. DISCUSSION AND CONCLUDING REMARKS

We have made a comparative study of the electronic structure of the  \( \beta \) ,  \( \beta^{\prime\prime} \) , U1, and U2 phases in the AlMgSi alloy precipitation sequence. The bonding in the  \( \beta \)  phase is characterized by the covalent bonding between Si-Si nearest neighbour pairs and ionic/covalent bonding between Si-Mg nearest neighbour pairs. For the  \( \beta \)  phase the bonding is dominated by the partly ionic Mg-Si bond. By calculating the heat of formation for the various precipitate phases further insight can be gained in the observed precipitation sequence. Presently we employ the formula:

 \[ \Delta H=E_{\mathrm{AlMgSi}}-x_{\mathrm{Mg}}E_{\mathrm{Mg}}-x_{\mathrm{Si}}E_{\mathrm{Si}}-x_{\mathrm{Al}}E_{\mathrm{Al}}, \quad (6) \] 

where  \( \Delta H \)  is the formation energy/enthalpy per atom,  \( E_{AlMgSi} \)  is the energy of the given AlMgSi compound, and  \( E_{Mg} \) ,  \( E_{Si} \) , and  \( E_{Al} \)  are the equilibrium ground state (zero temperature) energies per atom at of hcp Mg, dc Si, and fcc Al respectively.  \( x_{i} \)  is the relative content of element i in the compound. Results for the various phases in the precipitation sequence are shown in table IV and figure 19. For the  \( \beta \)  and  \( \beta^{\prime\prime} \)  phases we used the experimentally observed lattice parameters. For the  \( \beta^{\prime\prime} \)  we used the relaxed coordinates found from force minimization (table I). We have also included the corresponding
 
![](./images/867771569798119566_29.jpg)

FIG. 19: Calculated energies of formation for the various precipitate phases. The error bars indicate the estimated level of accuracy of  \( \pm2.0 \)  mRy. The line connecting  \( \beta^{\prime\prime} \)  and  \( \beta \)  is a guide to the eye.

energy from a past model for the  \( \beta^{\prime} \)  phase proposed by Matsuda et al. \( ^{8} \) .

It is difficult to draw any quantitative conclusions based on the relative formation energy of these phases in Aluminium, at finite temperatures, without taking into account the effects of the interface and entropy. The calculated energies are nonetheless very reasonable. As can be seen, only 3 phases  \( (\beta, U1 \)  and  \( U2) \) , give a negative formation energy. The  \( U1 \)  and  \( U2 \)  are lower in energy than  \( \beta^{\prime\prime} \) , but higher than the  \( \beta \)  phase.  \( \beta \) s shows the most negative energy, which is line with expectations, since it is the terminal equilibrium structure of the precipitation sequence. The energy of  \( \beta^{\prime\prime} \)  is slightly positive, but not markedly different from  \( \beta \) ,  \( U1 \)  and  \( U2 \) .  \( \beta^{\prime\prime} \) , which can be derived from an fcc super-cell, forms early in the precipitation sequence at temperatures above  \( 150\;^{\circ}C \) , but gradually disappears after further heat treatment \( ^{4} \) .

We note the unusually high heat of formation for Matsuda's  \( \beta^{\prime} \)  model which has a hexagonal unit cell with space group  \( P\bar{6}2m \)  with experimentally derived lattice parameters  \( a = b = 4.05\mathring{A} \) ,  \( c = 6.74\mathring{A} </math> and the stoichiometry Mg \( _{2} \) Si. For the calculated formation energy, we used the experimentally derived lattice parameters and published coordinates. Upon volume relaxation, we however found that the structure reduced in volume by 26% corresponding to a heat of formation of 25 mRy. Furthermore, from a second order Birch fit, we find that for the experimental lattice constant, the Matsuda's  \( \beta^{\prime} \)  phase is under a negative pressure of approximately 6.9 GPa. Since the experimentally derived unit cell parameters are regarded as being extremely accurate it becomes difficult to see how such as phase might exist within the Al matrix.
To this date U1 and U2 are the only phases in the precipitation sequence of the AlMgSi alloy system containing Aluminium in addition to Magnesium and Silicon. The crystallographic structure type of both phases belong to structure families containing an abundance of documented compounds. A characteristic for both phases is the formation of a tightly bound network of Al and Si atoms made possible by at charge transfer from the electropositive Mg atoms. Considering the wide range of structures belonging to this family it is possible that these these type of structures containing other hardening elements than Mg and Si would form stable precipitates in Aluminium alloys. For example, it is quite remarkable that the U1 phase with Magnesium replaced by the rare earth element Europium produces a CaAl \( _{2} \) Si \( _{2} \) -type structure with lattice parameters and coordinates differing from the U1-phase by only few percent \( ^{28} \) . Suggested further work include the calculations on these two phases with iso-valent species substituted for the Si and Mg sites. In the future these calculations could also be used together with interfacial energies and entropy calculations to estimate the solid solubility of these phases in Aluminium.

Furthermore, the rule of thumb that successful aluminium precipitation hardened alloys have secondary and ternary elements that are larger and smaller than aluminium is not sufficiently accurate when applied to the stability of bulk phases in the precipitation sequence. The atomic radii of Al, Si, and Mg vary with the bonding environment. For example, in the equilibrium  \( \beta \)  phase the atomic size of Si is increased and that of Mg correspondingly decreased in forming a dominating ionic/covalent Mg-Si bond. Also, using the appropriate values for ionic radii \( ^{12} \) , the Mg-Si bond length in the  \( \beta \)  and  \( \beta^{\prime\prime} \)  phases are predicted to be considerably smaller than what the present calculations show. A more precise formulation would involve the ability of the secondary(A) and ternary(B) elements to form stable bonds (A-B, A-A, and B-B) with bond lengths which are comparable that of the Al-Al bond.

## Acknowledgments

This study has been performed as part of the research programs “KMB Heat Treatment Fundamentals” and “SUP Micro- and Nanostructure Based Materials Development”, supported by the Norwegian Research Council and collaborators from the industry. Parts of this work has been supported by the Norwegian Research Council through CPU time on the NOTUR Origin 3800.
 

TABLE IV: Calculated formation energies and bulk moduli. Space groups are given with space group number in parentheses.

<table><tr><td>Structure</td><td>Space</td><td>Al:Mg:Si</td><td>Lattice</td><td>Bulk Modulus</td><td>Energy/Atom</td></tr><tr><td>Type</td><td>Group</td><td>in Unit Cell</td><td>Parameters ( \( \AA \) )</td><td>(GPa)</td><td>(mRy)</td></tr><tr><td>\( \beta^{\prime\prime a} \)</td><td>C2/m (12)</td><td>0:5:6</td><td>a=15.16 b=6.74 c=4.05</td><td>65</td><td>3.53</td></tr><tr><td>\( \beta \)</td><td>Fm3m (225)</td><td>0:4:2</td><td>a=b=c=6.39</td><td>54</td><td>-10.93</td></tr><tr><td>\( \beta&#x27; \)  Matsuda \( ^{b} \)</td><td>P62m (189)</td><td>0:4:2</td><td>a=b=7.1 c=4.05</td><td>NA</td><td>38.174</td></tr><tr><td>U2</td><td>P3m1 (164)</td><td>4:4:4</td><td>a=b=4.05 c=6.74</td><td>69</td><td>-3.04</td></tr><tr><td>U1</td><td>P \( _{nma} \)  (62)</td><td>2:1:2</td><td>a=6.75 b=4.05 c=7.94</td><td>71</td><td>-0.45</td></tr></table>

 \( ^{a} \) Ref. 5

 \( ^{b} \) Ref. 8

 \( ^{3} \)  G. A. Edwards et al., Acta Mater. 46, 3893 (1998).

 \( ^{4} \)  C. D. Marioara et al., Acta Mater. 49, 321 (2001).

 \( ^{5} \)  H. W. Zandbergen, S. J. Andersen, and J. Jansen, Science 277, 1221 (1997).

 \( ^{6} \)  P. M. Derlet, S. J. Andersen, C. D. Marioara, and A. Froseth, J. Phys.: Condens. Matter 14, 4011 (2002).

 \( ^{7} \)  M. Takeda et al., Journal of Materials Science 33, 2385 (1998).

 \( ^{8} \)  K. Matsuda et al., Journal of Materials Science 35, 179 (2000).

 \( ^{9} \)  S. J. Andersen, C. D. Marioara, A. Froseth, R. Vissers, and H. Zandbergen, To be published (2002).

 \( ^{10} \)  S. J. Andersen, C. D. Marioara, A. Froseth, R. Vissers, and H. Zandbergen, To be published (2002).

 \( ^{11} \)  N. Ryum, Aluminium Alloys, Their Physical and Mechanical Properties, vol. III (EMAS, West Midlands, England, 1986).

 \( ^{12} \)  C. Kittel, Introduction to Solid State Physics (John Wiley and Sons Inc., New York, 1996), 7th ed.

 \( ^{13} \)  P. Blaha, K. Schwarz, G. Madsen, D. Kvasnicka, and J. Luitz, WIEN2k, An Augmented Plane Wave + Local Orbitals Program for Calculating Crystal Properties (Karlheinz Scwarz, Techn. Universitat Wien, Austria, 1999), ISBN 3-9501031-1-2.

 \( ^{14} \)  E. Sjostedt, L. Nordstrom, and D. J. Singh, Solid State Commun. 114, 15 (2000).

 \( ^{15} \)  J. C. Slater, Advances in Quantum Chemistry 1, 35 (1964).

 \( ^{16} \)  G. K. H. Madsen, P. Blaha, K. Schwarz, E. Sjostedt, and L. Nordstrom, Phys. Rev. B 64, 195134 (2001).

 \( ^{17} \)  P. E. Blochl, O. Jepsen, and O. K. Andersen, Phys. Rev. B 49, 16223 (1994).

 \( ^{18} \)  J. P. Perdew, S. Burke, and M. Ernzerhof, Phys. Rev. Lett. 77, 3865 (1996).

 \( ^{19} \)  P. Baranek, J. Schamps, and I. Noiret, J. Phys. Chem. B 101, 9147 (1997).

 \( ^{20} \)  P. Baranek, J. Schamps, and I. Noiret, J. Phys. Chem. B 103, 2601 (1999).

 \( ^{21} \)  D. M. Wood and A. Zunger, Phys. Rev. B 34, 4105 (1986).

 \( ^{22} \)  E. Anastassakis and J. P. Hawranek, Phys. Rev. B 5, 4003 (1972).

 \( ^{23} \)  O. Madelung, Landolt-Bornstein Numerical Data and Functional Relationships in Science and Technology, New Series, Group III, vol. 17e (1983).

 \( ^{24} \)  A. Y. Liu, K. J. Chang, and M. L. Cohen, Phys. Rev. B 37, 6344 (1988).

 \( ^{25} \)  C. Cheng, R. Hoffman, R. Nesper, and H. von Schnering, J. Am. Chem. Soc. 108, 1876 (1986).

 \( ^{26} \)  G. Nuspl, J. Evers, G. A. Landrum, and R. Hoffman, Inorg. Chem. 35, 6922 (1996).

 \( ^{27} \)  G. A. Landrum, R. Hoffman, J. Evers, and H. Boysen, Inorg. Chem. 37, 5754 (1998).

 \( ^{28} \)  P. Schobinger-Papamantellos and F. Hulliger, Jour. of Less-Comm. Met. 146, 327 (1989).
 


# Orbital order and electron itinerancy in CoV₂O₄ and Mn₀.₅Co₀.₅V₂O₄ from first principles

Jyoti Krishna \( ^{1} \)  and T. Maitra \( ^{2,*} \) 

 \( ^{1} \) Department of Physics, Arizona State University, Tempe, AZ - 85287, USA

 \( ^{2} \) Department of Physics, Indian Institute of Technology Roorkee, Roorkee 247667, Uttarakhand, India

In view of the recent experimental predictions of a weak structural transition in  \( CoV_{2}O_{4} \)  we explore the possible orbital order states in its low temperature tetragonal phases from first principles density functional theory calculations. We observe that the tetragonal phase with  \( I4_{1}/amd \)  symmetry is associated with an orbital order involving complex orbitals with a reasonably large orbital moment at Vanadium sites while in the phase with  \( I4_{1}/a \)  symmetry, the real orbitals with quenched orbital moment constitute the orbital order. Further, to study the competition between orbital order and electron itinerancy we considered  \( Mn_{0.5}Co_{0.5}V_{2}O_{4} \)  as one of the parent compounds,  \( CoV_{2}O_{4} \) , lies near itinerant limit while the other,  \( MnV_{2}O_{4} \) , lies deep inside the orbitally ordered insulating regime. Orbital order and electron transport have been investigated using first principles density functional theory and Boltzmann transport theory in  \( CoV_{2}O_{4} \) ,  \( MnV_{2}O{}_{4} \)  and  \( Mn_{0.5}Co_{0.5}V_{2}O_{4} \) . Our results show that as we go from  \( MnV_{2}O_{4} \)  to  \( CoV_{2}O{}_{4} \)  there is enhancement in the electron's itinerancy while the nature of orbital order remains unchanged.

## I. INTRODUCTION

The family of spinel vanadates  \( AV_{2}O_{4} \)  (AVO) presents a perfect platform for understanding the interplay among all possible degrees of freedom in a solid such as spin, orbital, lattice and charge \( ^{1,2} \) . In addition, the Mott physics is also at play here, as by mere controlling of the V-V distance (by varying the size of  \( A^{2+} \)  ion), the system can be driven to its itinerant state from an orbitally and magnetically ordered insulating state \( ^{3,4} \) . One can thus observe a fascinating competition between orbital order and electron itinerancy by tuning V-V distance in these materials. An additional geometrical frustration due to pyrochlore lattice of  \( V^{3+} \)  ions, makes spinel vanadates a fertile ground to study competing magnetic interactions ( \( J_{V-V} \)  and  \( J_{A-V} \) ) on a geometrically frustrated lattice. Whilst, the partially filled  \( t_{2g} \)  orbitals of  \( V^{3+} \)  ions, makes it always orbitally active, thereby triggering a structural transition, a magnetic transition normally follows at low temperatures due to the partial lifting of geometrical frustration. The multiple transitions (structural and magnetic) in AVO is thus a consequence of the nature of  \( A^{2+} \)  ion being magnetic, orbitally active or both (e.g.  \( MnV_{2}O_{4} \) ,  \( CoV_{2}O{}_{4} \) ,  $ FeV_{2}O_{4} et

Among the spinel vanadates with magnetic A-site ion,  \( CoV_{2}O_{4} \)  is unique in two ways: one, it sits very close to itinerancy limit 2.94 Å in terms of V-V distance ( \( R_{V-V} \) ) \( ^{8-10} \)  such that on the application of moderate pressure (about  \( \sim 8 \)  GPa) it shows metallic behavior \( ^{11} \)  and two, the existence of any structural transition in this compound is highly debated with most of the earlier experimental reports finding no evidence of cubic to tetragonal structural transition in this system \( ^{8,11,12} \)  whereas recent reports claim to observe a weak structural transition \( ^{10,13} \) . Interestingly though, it has got the highest magnetic transition temperatures: a collinear ferrimagnetic transition temperature  \( T_{C} = 150 \)  K and a non-collinear ferrimagnetic  \( T_{NC} = 90 \)  K \( ^{13} \)  among the AVOs. Recent strain measurements have reportedly identified a weak first order structural transition ( \( \Delta a/a \sim 10^{-4} \) ) at 90 K concurrent with  \( T_{NC} \)  \( ^{10,13} \) . Further, from the dielectric measurements, the authors proposed an orbital glassy state to be present at low temperatures. From another recent high resolution neutron powder diffraction measurement a very small tetragonal distortion (1 - c/a < 0.06%) has been captured in  \( CoV_{2}O_{4} \)  at 95 K and on further lowering of temperature, a change in the tetragonal symmetry from  \( I4_{1}/amd \)  to  \( I4_{l}/a \)  was observed at 59K via single crystal synchrotron radiation measurement \( ^{14} \) . Further analysis has led the authors to propose an anti-ferro orbitally ordered state below 59K.

MnV_{2}O_{4}, on the other hand, is insulating in character and R_{V-V} is away from the itinerancy limit and orbitally ordered \( ^{5,15-20} \) . Here, competing superexchange interactions J_{Mn-V} and J_{V-V} lead to two magnetic transitions: a collinear ferrimagnetic transition (T_{C}) at 56 K (V spins aligned opposite to that of Mn spins along c-direction) and a non-collinear ferrimagnetic (T_{NC}) transition (V spins cant away from c-axis while Mn spins remain parallel to c-axis) at 53 K. Also, the structural transition (cubic to tetragonal with space group I4_{1}/a) is well established in this system which occurs at 53 K coincident with T_{NC}. In the tetragonal phase, VO_{6} octahedra are compressed along c-axis because of Jahn-Teller (JT) effect. The tetragonal compression along c-axis lowers the d_{xy} orbital which then gets occupied by one electron. The second electron has therefore the choice of going to either d_{xz}, d_{yz} or both paving the way for a possible orbital ordering in the system. The cooperative JT effect forces the orbitals to order in certain fashion relieving the frustration of the lattice.

Many theoretical models are proposed for orbital order (OO) in spinel vanadates that depends on the relative strength of SO coupling, superexchange and
 

JT interaction \( ^{21-23} \) . The possible scenarios for OO in these systems are (1) A-type anti-ferro (real) OO, in which the second electron of V ion, alternately occupies  \( d_{xz}/d_{yz} \)  orbital in successive ab-planes along c direction resulting in the quenching of orbital angular momentum L, (2) Ferro (complex) OO, results in the ordering of complex orbitals ( \( d_{yz}\pm id_{xz} \) ) due to enhanced SO coupling leading to unquenched L. X-ray Magnetic Circular Dichroism (XMCD) technique has been very useful for detecting the local orbital moment \( ^{24,25} \)  which provides the information about real or complex orbital ordering. In case of  \( MnV_{2}O_{4} \) , previous DFT calculations indicate real orbital ordering \( ^{26,27} \)  which was corroborated by XMCD measurements \( ^{24} \) .

In a recent measurement, Ma et al. \( ^{[28]} \)  have looked into the effect of Co doping in  \( MnV_{2}O_{4} \)  and observed a crossover from orbitally ordered low Co-doping regime to increased electron itinerancy in high Co-doped regime. Therefore, it would be interesting to explore using first principles DFT and transport calculations the following two phenomena. Firstly, the nature of orbital ordering in low temperature phases of  \( CoV_{2}O_{4} \)  in view of the structural transitions observed recently in experiments \( ^{[14]} \)  and secondly, the competition between orbital order and electron itinerancy as a function of Co doping as we go from  \( MnV_{2}O_{4} \)  to  \( CoV_{2}O _{4} \) . We have addressed above two issues in our work presented in this paper.

## II. METHODOLOGY

The first principles density functional theory and Boltzmann transport theory have been used for the calculations presented in this paper. The structural parameters for  \( MnV_{2}O_{4} \)  and  \( CoV_{2}O_4 \)  (in its different structural phases) were obtained from experiments \( ^{[14,15]} \) . For  \( Mn_{0.5}Co_{0.5}V_{2}O_{4} \) , 50% of Mn ions were substituted by Co in the experimental structure of the  \( MnV_{2}O_{4} \) . We have then optimized both parent ( \( MnV_{2}O_{4} \)  and  \( CoV_{2}O_4 \) ) and doped structures using 2Doptimize package available in WIEN2k \( ^{[29]} \) . This package effectively performs 2D optimization in volume, c/a and atomic positions. The optimization (volume, c/a and oxygen positions) were carried out within Perdew-Burke-Ernzerhof Generalized Gradient Approximation (PBE-GGA) \( ^{[30]} \)  exchange-correlation functional within the full potential linearized augmented plane wave (FP-LAPW) method as implemented in WIEN2k. In this, we have considered nine different structures having their volumes varied by 0.5%, 1.0%, 1.5% and 2.0% with respect to experimental structure, and for each volume, nine different c/a structures were taken. We obtained the minimum energy structure from a total 81 different structures where oxygen positions were allowed to relax. Using this optimized structure, we performed further self-consistent field calculations considering 78  \( \vec{k} \)  points in the irreducible Brillouin zone and plane wave cut off ( \( R_{mt}K_{max} \) ) to be

TABLE I. The V-O bond lengths in the ab-plane and along c, A-O bond length for x=0.0 (MnV₂O₄), x=0.5 (MnₓCo₁₋ₓV₂O₄) and x=1.0 (CoV₂O₄), after structural optimization.

<table><tr><td>x</td><td>V-O (c)</td><td>V-O (ab)</td><td>A-O</td></tr><tr><td>0.0</td><td>2.0293</td><td>(2.0434,2.0137)</td><td>2.0346</td></tr><tr><td>0.5</td><td>2.0191</td><td>(2.0331,2.0036)</td><td>2.0244</td></tr><tr><td>1.0</td><td></td><td></td><td></td></tr><tr><td>Fd3m (PHASE 1)</td><td>2.0169</td><td>(2.0169,2.0169)</td><td></td></tr><tr><td>I41/amd (PHASE 2)</td><td>2.0148</td><td>(2.0176,2.0176)</td><td></td></tr><tr><td>I41/a (PHASE 3)</td><td>2.0150</td><td>(2.0059,2.0295)</td><td>1.9696</td></tr></table>

8.0. The muffin tin radii were taken as 2.0, 1.95 and 1.65 a.u. for Mn/Co, V and O respectively. Due to the presence of 3d electrons, Coulomb correlation (U) becomes indispensable, which was included in our calculations within GGA+U \( ^{31} \) . This takes into account the on-site Coulomb interaction and removes the self Coulomb and self exchange-correlation energy. The spin-orbit coupling (SO) is included by the second variational method with scalar relativistic wavefunctions \( ^{32} \) . To analyse the orbital order and electron transport we used maximally-localized Wannier functions (MLWF) to fit the DFT bands calculated by WIEN2k. WANNIER90 \( ^{33} \)  and WIEN2WANNIER \( ^{34} \)  codes were used for this purpose. We calculated the transport properties using BoltzWann code that utilizes semi-classical Boltzmann transport theory \( ^{35} \) .

## III. RESULTS AND DISCUSSIONS

In view of recent experimental report \( ^{14} \)  on the observation of weak structural transitions in  \( CoV_{2}O_{4} \)  from cubic (Fd \( \bar{3} \) m) to tetragonal (I \( \bar{4}_{1} \) /amd and I \( \bar{4} \) 1/a) phases, we investigated the electronic structure and nature of orbital ordering in the experimentally observed tetragonal phases in this system from first principles calculations. Further, we also looked into the effect of Co doping on the competition between orbital ordering and electron itinerancy as we go from  \( MnV_{2}O_{4} \)  to  \( CoV_{2}O_4 \) . The results presented in this section have therefore been divided into two parts. In part A, we present our calculations and results on the electronic structure and orbital order analysis of the cubic (Fd \( \bar{3} \) m) and tetragonal (I \( \bar{4} \) 1/amd and I \( \bar{4}_{1} \) /a) phases of  \( CoV_{2}O_{4} \) . In part B, we present our results on the effect of Co doping (x) on  \( MnV_{2}O_{4} \)  where we have discussed electronic structure, orbital ordering and electron transport calculations for the parent and doped compounds. Electronic structure calculations are performed within GGA+U and GGA+U+SO approximations with  \( U_{eff} = U-J = 4 \)  eV for Mn/Co and 3 eV for V ions where U is the Coulomb correlation and J is Hund's coupling.
 
![](./images/867747555490922976_1.jpg)

![](./images/867747555490922976_2.jpg)

![](./images/867747555490922976_3.jpg)

FIG. 1. The total density of states (DOS) for Co, V, and O within GGA+U for (a) cubic Fd \( \bar{3} \) m, (b) tetragonal I4 \( _{1} \) /amd and (c) I4 \( _{1/} \) a phases in majority and minority spin channel.

## A. CoV₂O₄ and its different phases

The GGA+U calculations were carried out on the optimized structures (see Table I) for all the three structural phases (cubic (phase 1), tetragonal I4 \( _{1} \) /amd (phase 2) and tetragonal I4 \( _{1} \) /a (phase 3)) by considering a collinear ferrimagnetic spin configuration where the spins of V are antiparallel with respect to Co spins along c-axis. The total energy calculations reveal that the tetragonal phase with I4 \( _{1} \) /a symmetry has the lowest energy which is consistent with the experiment. In Figure 1 we present the total density of states (DOS) of all the three phases of CoV \( _{2} \) O \( _{4} \)  for both the spin channels calculated within GGA+U approximation. While the cubic and tetragonal (I4 \( _{1} \) /amd) phase display the metallic character even with large U (in contrary to the experiments), an insulating behavior is observed for tetragonal phase 3 (I4 \( _{1} \) /a) (consistent with experiments). From DOS one can clearly observe that the tetrahedral crystal field splits the d-states of Co \( ^{2+} \)  ions into the lower energy e \( _{g} \)  and higher energy t \( _{2g} \)  states. Four out of the seven valence electrons of Co \( ^{2+} \)  thus completely fill the e \( _{g} \)  states (both majority and minority) and the rest three electrons make t \( _{2g} \)  states half-filled (only majority states are filled, minority states remain empty). Because of this, the filled Co d-states lie much below the Fermi level (FL). On the other hand, V \( ^{3+} \)  ions are octahedrally coordinated by O ions thus the d-states here split into higher energy e \( _{g} \)  and lower t \( _{2g} \)  states. The two d-electrons of V \( ^{3+} \)  ions thus partially fill the t \( _{2g} \)  states that lie near Fermi level (FL). Tetragonal distortions present in phase 2 does not split the t \( _{2g} \)  states completely to open a gap while in phase 3 a finite gap is seen in DOS due to the splitting of t \( _{2g} \)  states (see Figure 2 below). Note that in addition to octahedral crystal field, the trigonal distortion is also present in case of V ions (as O-V-O angles deviate from 90°). Because of varying strengths of tetragonal and trigonal distortions present in three phases the nature and magnitude of splitting of t \( _{2g} \)  states are different.

We present in Figure 2, the partial V DOS of three different phases calculated within GGA+U (left panel) and GGA+U+SO (right panel). One can see from Figure 2 (left) that in phase 1 (the cubic phase) where only trigonal distortion is present, the  \( t_{2g} \)  states split into a lower singlet  \( a_{1g} \)  and the higher doublet  \( e_{g}^{\prime} \)  states which are linear combinations of  \( d_{xy} \) ,  \( d_{xz} \)  and  \( d_{yz} \)  orbitals. In phase 2, the presence of both tetragonal and the trigonal distortion create much complicated splitting of  \( t_{2g} \)  states. In phase 3, the extent of trigonal distortion is much lower than the tetragonal compression thus  \( t_{2g} \)  split into pure  \( d_{xy} \) ,  \( d_{xz} \)  and  \( d_{yz} \)  states. In phase 1 and 2, the highest occupied  \( t_{2g} \)  level remains doubly degenerate and filled by one electron and hence the system shows metallic behavior. In phase 3, however, we see a further splitting of the  \( t_{2g} \)  levels giving rise to a band gap in the DOS as seen in Figure 2(c)(left). This splitting is because of the Jahn-Teller (JT) distortion associated with I4 \( _{1} \) /a symmetry where the V-O bonds are different in all three directions. This is also associated with a long range orbital ordering (OO) as discussed below. Comparing the DOS of GGA+U and GGA+U+SO we observe that for phase 1 and 2 they are drastically different whereas for phase 3 they are very similar. In phase 1 and 2 we obtain an insulating electronic structure within GGA+U+SO, un-
 

(a)

![](./images/867747555490922976_4.jpg)

(a)

![](./images/867747555490922976_5.jpg)

(b)

![](./images/867747555490922976_6.jpg)

(b)

![](./images/867747555490922976_7.jpg)

(c)

![](./images/867747555490922976_8.jpg)

(c)

![](./images/867747555490922976_9.jpg)

FIG. 2. The Vanadium partial density of states (DOS) for d-electrons within GGA+U (left) and for GGA+U+SO (right) for (a) cubic  \( Fd\bar{3}m \) , (b) tetragonal  \( I41/amd \)  and (c)  \( I41/a \)  phases for majority and minority spin channels. Note that the set  \( [d_{x^{2}-y^{2}}, d_{xz} \)  and  \( d_{yz}] \)  form  \( t_{2g} \)  rather than conventionally used  \( [d_{xy}, d_{xz} \)  and  \( d_{yz}] \)  as the crystallographic a and b-axes are rotated by  \( 45^{\circ} \)  with respect to planar V-O bonds of  \( VO_{6} \)  octahedra.

like the metallic solution of GGA+U, which is consistent with experiment. The SO effect on DOS is seen to be quite significant in phase 1 and 2, whereas in phase 3 it is negligible. This is also reflected in calculated orbital moment values at V site which are -0.66  \( \mu_{B} \)  and -0.06  \( \mu_{R} \)  for phase 2 and 3 respectively.
In order to understand the nature of OO, which is difficult to ascertain from the DOS, we have calculated 3D electron and hole densities in real space at V sites and have also done an analysis using tight-binding (Wannier orbitals) basis for phase 2 and 3. In Figure 3 we show the calculated 3D hole densities for phase 2 and phase 3
 

(a)

![](./images/867747555490922976_10.jpg)

(b)

![](./images/867747555490922976_11.jpg)

FIG. 3. 3D hole density in real space depicting the nature of unoccupied orbitals of  \( V^{3+} \)  ion for (a) phase 2 and (b) phase 3. The rotation of the orbitals (in ab plane and c-direction) in the V chain is because of the trigonal distortion.

![](./images/867747555490922976_12.jpg)

![](./images/867747555490922976_13.jpg)

FIG. 4. Left: The spin-polarized total DOS for 50% (x=0.5) Co doping at  \( MnV_{2}O_{4} \)  site calculated within GGA+U approximation. Right The vanadium partial DOS for d states.

at V sites within GGA+U+SO approximation. Comparing these two one can clearly see that that unoccupied V orbital structure and hence the occupied ones are very different in phase 2 and 3. As also evident from the large orbital moment (-0.66 \( \mu_{B} \) ) value in case of phase 2, we propose the presence of a complex orbital order of the type  \( d_{xz} \pm id_{yz} \)  in this case as seen in  \( ZnV_{2}O_{4} \)  \( ^{23} \) . While in phase 3, a further analysis using Wannier orbitals basis along with a small value of calculated orbital moment (-0.06 \( \mu_{B} \) ) support A-type orbital order where real orbitals  \( d_{yz} \)  and  \( d_{xz} \)  are occupied at V sites in successive ab planes along c-direction. Therefore, we conclude that the transition seen in experiment \( ^{14} \)  at 59K where the crystalline symmetry changes from  \( I4_{1}/amd \)  to  \( I4_{11}/a \)  is also associated with complex to real orbital order transition. Future XMCD measurements are expected to shed further light on this.

## B. 50% Co doped MnV_{2}O_{4}

As discussed in the introduction,  \( MnV_{2}O_{4} \)  is known to be orbitally ordered while  \( CoV_{2}O_{4} \)  is close to the itinerant regime. In view of the recent experimental measurements by Ma et al. \( ^{[28]} \)  and to study the competition between electron itinerancy and orbital order in Co doped  \( MnV_{2}O_{4} \)  from theoretical perspective, we considered 50% of Mn by Co in  \( MnV_{2}O_{4} \)  (i.e.  \( Mn_{1-x}Co_{x}V_{2}O_{4} \)  with x=0.5). In a previous study we have reported the effect of Co doping on the structural parameters such as lattice constants, inter-vanadium distance ( \( R_{V-V} \) ) etc. \( ^{[36]} \) . With increase in Co doping at Mn sites the lattice constants a and c are seen to decrease. This is because of the smaller size of Co ion compared to that of Mn. This induced chemical pressure due to Co doping also affects  \( R_{V-V} \) . We also observe that with Co doping, the Mn-O bond lengths along c-axis decrease due to the hydrostatic
 
![](./images/867747555490922976_14.jpg)

FIG. 5. The temperature dependence of electrical conductivity ( \( \sigma \) ) for different doping concentrations (x) in  \( Mn_{1-x}Co_{x}V_{2}O_{4} \) .

pressure acting at Mn site which shrinks Mn-O tetrahedron (see Table I). This contraction enhances local trigonal distortion in  \( VO_{6} \)  octahedron.

In Figure 4 we present the total and V partial DOS of  \( Mn_{0.5}Co_{0.5}V_{2}O_{4} \)  within GGA+U approximation. Comparing the DOS for this doped compound with the same for parent compounds  \( CoV_{2}O_{4} \)  (phase 3, see Figure 2) and  \( MnV_{2}O_{4} \)  (not shown here), we observe that the bandgap decreases. To clearly establish that the electron itinerancy indeed increases with Co doping we have calculated the electrical conductivity as a function of temperature using Boltzmann transport theory. For this we have used Wannier fits to DFT bands of  \( V\ t_{2g} \)  states around FL obtained from Wien2k within GGA+U. The variation of electrical conductivity ( \( \sigma \) ) with temperature for  \( MnV_{2}O_{4} \)  (x=0.0),  \( CoV_{2}O_{4} \)  (x=1.0) and 50% Co doped (x=0.5)  \( MnV_{2}O_{4} \)  are shown in Figure 5. We can clearly see that  \( \sigma \)  rises as Co concentration increasing indicating an enhancement of electron itinerancy in the system. Also, we see that with increasing temperature  \( \sigma \)  rises in all three cases showing the insulating character of the systems.

To ascertain how much orbital order is affected by Co doping, we have performed Wannier analysis of the  \( V t_{2g} \)  bands around the FL of  \( CoV_{2}O_{4} \) ,  \( MnV_{2}O^{4} \)  and x = 0.5 Co doped case. The comparison is presented in Figure 6. The projections of individual Wannier d orbitals on to V d-bands of the respective compounds are shown. The color code depicts the strength of the orbital character with red representing the highest. One can clearly see that in all three cases  \( d_{xy} \)  orbital is predominantly occupied at a V site whereas there is a difference between occupancies of  \( d_{xz} \)  and  \( d_{yz} \)  orbitals. Further analysis by plotting these Wannier orbitals in real space reveals that A-type OO similar to phase 3 of  \( CoV_{2}O_{4} \)  prevails in all three compounds (i.e. one electron of  \( V^{3+} \)  always occupies at  \( d_{xy} \)  orbital with another electron alternating between  \( d_{xz} \)  and  \( d_{yz} \) ). If we consider the difference between the orbital occupancies of  \( d_{xz} \)  and  \( d_{yz} \)  orbitals as the strength of the orbital order, then one can clearly see from Figure 6 that in  \( MnV_{2}O_{4} \)  and x = 0.5 Co doped casethis difference is somewhat larger that the same in  \( CoV_{2}O_{4} \) . Thus one can conclude from the above discussion that as we go from  \( MnV_{2}O_{4} \)  to  \( CoV_{2}O^{4} \) , the electron itinerancy increases, the nature of orbital order remains same while the strength of orbital order weakens. Finally we would like to mention that we have also performed calculations including SO interaction for the doped compound to see whether complex orbitals are present in this case. The orbital moment for V ion is found to be -0.068  \( \mu_{B} \)  which is very small. Thus here also only real orbitals are involved in OO.

## IV. CONCLUSIONS

We have performed the first principles calculation in the three different structural phases of  \( CoV_{2}O_{4} \) : cubic, tetragonal with  \( I4_{1}/amd \)  symmetry and tetragonal with  \( I4_{1}/a \)  symmetry. Total energy calculations reveal that tetragonal with  \( I4_{1}/a \)  symmetry is indeed lower in energy with respect to the cubic phase. Our GGA+U calculations show that while cubic and tetragonal phase with  \( I4_{1}/amd \)  symmetry remain metallic in character, the tetragonal phase with  \( I4_{1}/a \)  symmetry becomes insulating. We observe further from our GGA+U+SO calculations that tetragonal phase with  \( I4_{1}/amd \)  symmetry has orbital order involving complex orbitals with large orbital moment whereas tetragonal phase with  \( I4_{1}/a \)  symmetry has A-type orbital order comprising of real orbitals with negligible orbital moment. Therefore, we conclude that the structural transition seen in experiment at 59K where the symmetry of tetragonal phase changes from  \( I4_{1}/amd \)  to  \( I4_{2}/a \) , is associated with complex to real orbital order transition. We also performed calculations for 50% Co doped  \( MnV_{2}O_{4} \)  compound (i.e.  \( Mn_{0.5}Co_{0.5}V_{2}O_{4} \) ) to study the competition between electron itinerancy and orbital order as a function of doping. We observed that doping Co at Mn sites indeed reduces the strength of orbital order even though the orbital order remains the same. At the same time, it enhances the electron itinerancy which we could clearly see from calculated electrical conductivity which increases with the Co content.

## V. ACKNOWLEDGEMENT

This work is supported by DST-DAAD project (grant no INT/FRG/DAAD/P-16/2018). JK acknowledges MHRD(INDIA) for research fellowship.
 

(a)

![](./images/867747555490922976_15.jpg)

(b)

![](./images/867747555490922976_16.jpg)

(c)

![](./images/867747555490922976_17.jpg)

dxz

![](./images/867747555490922976_18.jpg)

dyz

![](./images/867747555490922976_19.jpg)

dyz

![](./images/867747555490922976_20.jpg)

dyz

![](./images/867747555490922976_21.jpg)

![](./images/867747555490922976_22.jpg)

![](./images/867747555490922976_23.jpg)

FIG. 6. Projection of V  \( t_{2g} \)  bands on to  \( d_{xy} \) ,  \( d_{xz} \)  and  \( d_{yz} \)  Wannier orbitals for (a)  \( CoV_{2}O_{4} \)  in phase 3 (b)  \( MnV_{2}O_{4} \)  and (c) x=0.5. The color bar on right side depicts the orbital character with the red (blue) color showing highest (lowest) character of a particular orbital.

* tulimfph@iitr.ac.in

 \( ^{1} \)  Paolo G Radaelli, New Journal of Physics 7, 53 (2005).

 \( ^{2} \)  S.-H. Lee, H. Takagi, D. Louca, M. Matsuda, S. Ji, H. Ueda, Y. Ueda, T. Katsufuji, J.-H. Chung, S. Park, S.-W. Cheong, and C. Broholm, Journal of the Physical Society of Japan 79, 011004 (2010).

 \( ^{3} \)  A. Kiswandhi, J. Ma, J. S. Brooks, and H. D. Zhou, Physical Review B 90, 155132 (2014).

 \( ^{4} \)  A. Kiswandhi, J. S. Brooks, J. Lu, J. Whalen, T. Siegrist, and H. D. Zhou, Phys. Rev. B 84, 205138 (2011).

 \( ^{5} \)  V. O. Garlea, R. Jin, D. Mandrus, B. Roessli, Q. Huang, M. Miller, A. J. Schultz, and S. E. Nagler, Physical Review Letters 100, 066404 (2008).

 \( ^{6} \)  S. Kawaguchi, H. Ishibashi, S. Nishihara, M. Miyagawa, K. Inoue, S. Mori, and Y. Kubota, Journal of Physics: Condensed Matter 25, 416005 (2013).

 \( ^{7} \)  S. Kawaguchi, H. Ishibashi, S. Nishihara, S. Mori, J. Campo, F. Porcher, O. Fabelo, K. Sugimoto, J. Kim, K. Kato, M. Takata, H. Nakao, and Y. Kubota, Physical Review B 93, 024108 (2016).

 \( ^{8} \)  Y. Huang, Z. Yang, and Y. Zhang, Journal of Physics: Condensed Matter 93, 056003 (2012).

 \( ^{9} \)  R. Kaur, T. Maitra, and T. Nautiyal, Journal of Physics: Condensed Matter 26, 045505 (2014).

 \( ^{10} \)  Reig-i-Plessis, D. Casavant, V. O. Garlea, A. A. Aczel, M. Feygenson, J. Neuefeind, H. D. Zhou, S. E. Nagler, and G. J. MacDougall, Physical Review B 93, 014437 (2016)

 \( ^{11} \)  A. Kismarahardja, J. S. Brooks, A. Kiswandhi, K. Matsubayashi, R. Yamanaka, Y. Uwatoko, J. Whalen, T. Siegrist and H. D. Zhou, Physical Review Letters 106, 056602(4) (2011).

 \( ^{12} \)  J. H. Lee, J. Ma, S. E. Hahn, H. B. Cao, M. Lee, T. Hong, H.-J. Lee, M. S. Yeom, S. Okamoto, H. D. Zhou, M. Matsuda and R. S. Fishman, Scientific Reports 7, 17129 (2017).

 \( ^{13} \)  R. Koborinai, S. E. Dissanayake, M. Reehuis, M. Matsuda, T. Kajita, H. Kuwahara, S. -H. Lee, and T. Katsufuji, Physical Review Letters 116, 037201 (2016).

 \( ^{14} \)  H. Ishibashi, S. Shimono, K. Tomiyasu, S. Lee, S. Kawaguchi, H. Iwane, H. Nakao, S. Torii, T. Kamiyama, and Y. Kubota, Physical Review B 96, 144424 (2017).

 \( ^{15} \)  Y. Nii, H. Sagayama, T. Arima, S. Aoyagi, R. Sakai, S. Maki, E. Nishibori, H. Sawa, K. Sugimoto, H. Ohsumi, and M. Takata, Physical Review B 86, 125142 (2012).

 \( ^{16} \)  S.-H. Baek, N. J. Curro, K.-Y. Choi, A.P. Reyes, P.L. Kuhns, H. D. Zhou, and C. R. Wiebe, Physical Review B 80, 140406(R) (2009).

 \( ^{17} \)  J.-H. Chung, J.-H. Kim, S.-h. Lee, T. J. Sato, T. Suzuki, M. Katsumura, and T. Katsufuji, Physical Review B 77,
 

054412 (2008).

 \( ^{18} \)  H. D. Zhou, J. Lu, and C. R. Weibe, Physical Review B 76, 174403 (2007).

 \( ^{19} \)  K. Adachi, T. Suzuki, K. Kato, K. Osaka, M. Takata, and T. Katsufuji, Physical Review Letters 95, 197202 (2005).

 \( ^{20} \)  T. Suzuki, M. Katsumura, K. Taniguchi, T. Arima, and T. Katsufuji, Physical Review Letters 98, 127203 (2007).

 \( ^{21} \)  H. Tsunetsugu, Y. Motome, Physical Review B 68, 060405(R)(2003).

 \( ^{22} \)  O. Tchernyshyov, Physical Review Letters 93, 15 (2004).

 \( ^{23} \)  T. Maitra, and R. Valenti, Physical Review Letters 99, 126401 (2007).

 \( ^{24} \)  K. Matsuura, H. Sagayama, Y. Nii, N. D. Khanh, N. Abe, and T. Arima, Physical Review B 92, 035133 (2015).

 \( ^{25} \)  J. Okabayashi, S. Miyasaka, K. Hemmi, K. Tanaka, S. Tajima, H. Wadati, A. Tanaka, Y. Takagi, and T. Yokoyama, Journal of the Physical Society of Japan 84, 104703 (2015).

 \( ^{26} \)  S. Sarkar, T. Maitra, R. Valenti, and T. Saha-Dasgupta, Physical Review Letters 102, 216405 (2009).

 \( ^{27} \)  D. Dey, T. Maitra and A. Taraphder, Physical Review B 93, 195133 (2016).

 \( ^{28} \)  J. Ma, J. H. Lee, S. H. Hahn, T. Hong, H. B. Cao, A. A. Aczel, Z. L. Dun, M. B. Stone, W. Tian, Y. Qiu, J. R.

D. Copley, H. D. Zhou, R. S. Fishman, and M. Matsuda, Physical Review B 91, 020407(R) (2015).

 \( ^{29} \)  P. Blaha, K. Schwarz, G. K. H. Madsen, D. Kvasnicka, and J. Luitz, WIEN2k An Augmented Plane Wave + Local Orbitals Program for Calculating Crystal Properties (Karlheinz Schwarz, Techn. Universität Wien, Austria, 2001).

 \( ^{30} \)  J. P. Perdew, A. Ruzsinszky, G. I. Csonka, O. A. Vydrov, G. E. Scuseria, L. A. Constantin, X. Zhou, and K. Burke, Physical Review Letters 100, 136406 (2008).

 \( ^{31} \)  V. I. Anisimov, I. V. Solovyev, and M. A. Korotin, Physical Review B 48, 23 (1993).

 \( ^{32} \)  D. D. Koelling, and B. N. Harmon, Journal of Physics C: Solid State Physics 10, 3107 (1977).

 \( ^{33} \)  A. A. Mostofi, J. R. Yates, Y.-S. Lee, I. Souza, D.Vanderbilt, and N. Marzari, Computer Physics Communications 178, 685 (2008).

 \( ^{34} \)  J. Kunes, R. Arita, P. Wissgott, A. Toschi, H. Ikeda, K. Held, Computer Physics Communications 181, 1888 (2010).

 \( ^{35} \)  G. Pizzi, D. Volja, B. Kozinsky, M. Fornari, and N. Marzari, Computer Physics Communications 185, 422 (2014).

 \( ^{36} \)  Jyoti Krishna and Tulika Maitra, AIP Conference Proceedings 1832, 090022 (2017).
 

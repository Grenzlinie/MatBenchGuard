# Simulation of Carbon Nanotube Pull-out When Bonded to a Polymer Matrix

S. J. V. Frankland¹ and V. M. Harik²

¹ICASE, M/S 132C, NASA Langley Research Center, Hampton, VA 23681-2199
²Swales Aerospace, M/S 186A, NASA Langley Research Center, Hampton, VA 23681-2199

## ABSTRACT

A carbon nanotube pulling through a polyethylene matrix was simulated using molecular dynamics. The interfacial sliding was characterized in terms of a nanoscale friction model, which is parametrized from the molecular dynamics simulation, and involves determining the critical pull-out force on the nanotube and the effective viscosity at the nanotube/polymer interface. Comparison was made of the pull-out behavior of non-bonded and functionalized nanotube composites. Chemical bonds between the polymer and the nanotube increased the critical pull-out force, the resistance to interfacial sliding, and the interfacial viscosity.

## INTRODUCTION

In polymer-nanotube composites, the strength of the interface between the polymer and the nanotube (NT) may be enhanced by chemically bonding the NTs to the polymer. Chemical functionalization of NTs remains a challenge [1, 2], but in some polymer-NT composites, where significant load transfer between the polymer and the nanotube has been observed, chemical bonding with the NT may occur [3].

In traditional fiber-reinforced composites, the fiber-matrix interfacial shear strength is often characterized by fiber pull-out experiments [4]. Analogous nanoscale pull-out experiments have been carried out with atomic force microscopy for the sliding of NTs in multi-walled NTs [5] and in bundles of single-walled NTs [6]. A simulated pull-through test has also been devised for polymer-NT composites via molecular dynamics (MD) to determine the interfacial shear strength while a force is applied to the NT. These simulations have indicated an increase in the interfacial shear strength with the addition of chemical bonds between the polymer and a NT [7]. Furthermore, the simulations have been extended to study the interfacial sliding of the NT during pull-out in non-bonded composites, and to characterize the effective interfacial viscosity due to the van der Waals interactions of the polymer and the NT [8, 9].

In this work, the interfacial sliding during pull-out of a NT chemically bonded to a crystalline polymer matrix was modeled with MD simulations. The objective was to show some of the mechanisms which may serve to enhance its ability to transfer mechanical load within the composite. First, a description of the composite structure will be given with details of the MD simulations. Then stages encountered by the NT during interfacial sliding will be analyzed. Finally, the sliding velocity will be interpreted by using the interfacial viscosity model [8, 9].

## MOLECULAR DYNAMICS SIMULATION

The simulated polymer-NT composite consisted of a (10,10) carbon nanotube embedded in a crystalline polyethylene (PE) matrix (Figure 1a). The NT was chemically bonded at three

locations to one of the nearby polymer chains (Figure 1b). Each attachment included a direct bond to the NT, two $\text{CH}_2$ groups and a direct bond to the chain (Figure 1d). In the MD simulations, all the chemical bonding, including the chemical bonds between the NT and the PE, was represented with the same hydrocarbon potential [10]. The non-bonded interactions were represented with the Lennard-Jones potential [11]. The system was replicated across periodic boundaries in each of the 3-dimensions, making the NT and the PE chains infinitely long. This composite was similar to the crystalline polyethylene used in previous work [7], and the detailed chemical description is kept for consistency.

To simulate the interfacial sliding of the NT, force was added to each atom of the NT in the axial direction. As the system was periodic, the NT moved through the polymer into the next periodic image when it began to slide. The applied force was incremented over time. The simulation is run for about 210,000 MD steps of 0.05 fs each. The size of the force increment was increased by a factor of 2.5 at 105,000 steps. The displacements and velocities of the NT, the attached chains, and the nearby chains were monitored under increasing force. The attached chain exhibited a breakage before the initial force loading due to reactivity included in the hydrocarbon potential, and retained that configuration throughout the rest of the simulation (Figure 1c). The initial configuration also included attachments to a second chain on the opposite side of the NT, but this attached chain did not survive past 40,000 steps. Only a third of this chain survived the initial NT pull-out force intact. This incident had marginal effect of the investigated interfacial sliding after the onset of pull-out; that sliding was dominated by the friction along the entire surface area and the chemical bonding of the first chain.

![](./images/811669650172542977_1.jpg)

Figure 1. The structure of the functionalized polymer-nanotube composite (a) cross-sectional view, (b) side view of the starting structure with links 1 and 2 and (c) the actual structure of NT and the attached chain with one breakage (d) close-up of an attachment.

# RESULTS AND DISCUSSION

## Interfacial Sliding

The velocity profile of the NT under load is plotted in Figure 2. Several stages were observed in the interfacial sliding of the NT through this composite. However, the interfacial sliding of the NT in this composite is significantly different from that observed previously for the non-bonded PE/NT composite [8, 9]. Initially, the NT experienced thermal vibrations and

interacts with the adjacent polymer chains in equilibrium at 300 K. At 0.17 nN enough force was exerted on the NT for interfacial sliding to begin. This initial pull-out force was higher than that observed for the onset of NT sliding in a non-bonded composite. The next difference between the composites occurred when the NT velocity peaked just past 20,000 steps and then decreased again almost to zero. At this point, the NT was under the constraint of the chemical bonds attaching it to the chain. Increasing the force on the NT beyond this point caused it to drift about 0.5 A as shown by the NT displacement in Figure 3. At about 57,000 steps, the NT began to accelerate on average until about 141,000 steps. Although the size of the force increment was increased in this range, the relation of force to velocity maintained the same slope (Figure 4).

![](./images/811669650172542977_2.jpg)

FIGURE 2. Velocity of the center of mass of a carbon NT during the simulated pull-out.

![](./images/811669650172542977_3.jpg)

FIGURE 3. Displacement of individual carbon atoms of the NT during the simulated pull-out.

![](./images/811669650172542977_4.jpg)

FIGURE 4. The force-velocity relation for the simulated NT pull-out.

In this range, one of the links (Link 1 in Figure (1b)) of the chain engaged part of the chain nearby to move with the NT. The chain was loose enough that the part near Link 1 moved with the NT while the rest of chain progressively slowed down in the vicinity of Link 2. Link 2 was moving with the NT, but it was loose enough that it did not engage its part of the chain into motion. The linkages and the chains had significantly more degrees of freedom and could move differently relative to one another and the NT. A transition took place at about 141,000 steps, where Link 2 broke releasing its part of the chain. This transition was followed by two peaks in NT velocity (Figure 2) indicating continued acceleration of the NT and the attached chain.

In Figure 3, the displacement of individual carbon atoms associated with the sliding NT, the bonded chain and a non-bonded chain are shown as the applied force increased up to 3 nN. The bonded polymer chain moved along with the NT pulled by force, while a non-bonded chain vibrated around its initial position without significant motion in the direction of NT axis.

### Interfacial viscosity

The NT pull-out process, in general, and interfacial sliding, in particular, can be described by an interfacial friction model [9], which is analogous to a Bingham-type model for viscoplastic failure of the interface including the concept of interfacial viscosity [12,13]. The model describes the dependence of the average applied force, $<f>_{pull}$, on the average NT velocity, $<V_{z}>$, in the z-direction of the NT axis:

$$(1) \quad <f>_{pull}=f_{0}+\chi_{eff}<V_{z}>,$$

where $f_0$ is the critical pull-out force and $\chi_{eff}$ is the effective viscosity coefficient, which can be obtained from the MD simulation. The effective viscosity, $\chi_{eff}$, of the NT/polymer interface is defined as a proportionality constant in the force-velocity relation that characterizes the interfacial momentum transfer. NT velocity variations shown in Figure 2 are plotted in Figure 4 for every incremental force loading. Once the critical pull-out force, $f_0$, at 0.17 nN was reached, the force-velocity dependence could be approximated by a linear relation (the solid line). The inverse of the slope of the resulting line is the coefficient $\chi_{eff}$, which is 2.3±0.2 (nN ps)/A. This slope can be estimated from dashed lines like those shown in Figure 4, which bound the NT velocity variations during NT sliding.

The average applied force, $<f>_{pull}$, in equation (1) is related to the average shear stress, $<\tau>$, for sliding interactions by the force balance: $<\tau> \approx <f>_{pull}/A_i$, where $A_i$ is the interfacial area between the NT and polymer. During the NT pull-out, the applied force is balanced by the interfacial friction characterized by the effective viscosity, $\mu_{eff}$, and the induced shear stress, $<\tau>$. The effective viscosity coefficient, $\chi_{eff}$, is related to the effective viscosity $\mu_{eff}$ via

$$(2) \quad \mu_{eff}=\frac{\chi_{eff} \bar{h}_{vdW}}{A_{i}},$$

where $\bar{h}_{vdW}$ is the van der Waals separation between the stationary polymer and the sliding NT. Therefore, the effective viscosity, $\mu_{eff}$, is 0.27 cP, which is 50% higher than that of the non-bonded NT composite, 0.18 cP [8, 9].

## CONCLUDING REMARKS

The interfacial sliding of a carbon nanotube (NT) chemically bonded to a local chain in a polymer matrix is simulated with molecular dynamics (MD) and the results fit an interfacial friction model for NT pull-out. The interfacial sliding in this composite differs from a non-bonded composite in at least two major ways. First, the NT is observed to be constrained by the chemical linkages. Second, as the linkages are flexible, they engage separately in motion with the NT at different times and force loadings. These differences result in higher interfacial shear strengths and higher interfacial viscosities than in the non-bonded composite, yielding qualitative information for the design of NT-reinforced polymer composites.

## ACKNOWLEDGMENT

This research was supported by National Aeronautics and Space Administration under NASA Contract No. NAS1-97046 while S. J. V. Frankland was at ICASE, NASA Langley Research Center, Hampton, VA. V. M. Harik was partially supported by the NASA URETI for Bio-inspired Nanostructured Multifunctional Materials (award No. NCC-1-02037). The molecular dynamics simulations were carried out with DL-POLY which is a package of molecular simulations subroutines written by W. Smith and T. R. Forester, copyright The Council for the Central Laboratory of the Research Councils, Daresbury Laboratory at Daresbury, Nr. Warrington, England, UK, 1996.

## REFERENCES

1. P. J. Boul, J. Liu, E. T. Mickelson, C. B. Huffman, L. M. Ericson, I. W. Chiang, K. A. Smith, D. T. Colbert, R. H. Hauge, J. L. Margrave, and R.E. Smalley, *Chem. Phys. Lett.* **310**, 367 (1999).
2. Y. Chen, R. C. Haddon, S. Fang, A.M. Rao, P. C. Eklund, W. H. Lee, E. C. Dickey, E. A. Grulke, J. C. Pendergrass, A. Chavan, B. E. Haley, and R. E. Smalley, *J. Mat. Res.* **13**, 2423 (1998).
3. H. D. Wagner, O. Lourie, Y. Feldman, and R. Tenne, *Appl. Phys. Lett.* **72**, 188 (1998).
4. V. T. Bechtel and N. R. Sottos, *Comp. Sci & Techn.* **58**, 1727 (1998).
5. M. F. Yu, B. I. Yakobson, and R. S. Ruoff, *J. Phys. Chem. B* **104**, 8764 (2000).
6. M. F. Yu, B. S. Files, S. Arepalli and R. S. Ruoff, *Phys. Rev. Lett.* **84**, 5552 (2000).
7. S. J. V. Frankland, A. Caglar, D. W. Brenner, M. Griebel, *J. Phys. Chem. B* **106**, 3046 (2002).
8. S. J. V. Frankland, V. M. Harik, *Mat. Res. Soc. Symp. Proc.* **733 E**, T6.2.1 (2002).
9. S. J. V. Frankland, V. M. Harik, *Surf. Sci. Lett.* (2003), in press.
10. D. W. Brenner, O. A. Shenderova, J. A. Harrison, S. J. Stuart, B. Ni, and S. B. Sinnott, *J. Phys C: Condensed Matter* **14**, 783 (2002).
11. M. P. Allen and D. J. Tildesley, *Computer Simulation of Liquids*, (Clarendon Press, Oxford, 1987).
12. V. M. Harik, *Experimental and Theoretical Studies of Interfacial Effects in Multiphase Media*, Ph.D. Thesis, University of Delaware, Newark, DE, 1997.
13. V. M. Harik and R. A. Cairncross, *Mech. Mater.* **32**, 807 (2000).
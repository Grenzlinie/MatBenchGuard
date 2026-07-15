Markus J. Buehler
Yong Kong
Huajian Gao
e-mail: hjgao@mf.mpg.de

Max Planck Institute for Metals Research,
Heisenbergstr. 3, 70569 Stuttgart,
Germany

# Deformation Mechanisms of Very Long Single-Wall Carbon Nanotubes Subject to Compressive Loading

We report atomistic studies of single-wall carbon nanotubes with very large aspect ratios subject to compressive loading. These long tubes display significantly different mechanical behavior than tubes with smaller aspect ratios. We distinguish three different classes of mechanical response to compressive loading. While the deformation mechanism is characterized by buckling of thin shells in nanotubes with small aspect ratios, it is replaced by a rod-like buckling mode above a critical aspect ratio, analogous to the Euler theory in continuum mechanics. For very large aspect ratios, a nanotube is found to behave like a flexible macromolecule which tends to fold due to vdW interactions between different parts of the carbon nanotube. This suggests a shell-rod-wire transition of the mechanical behavior of carbon nanotubes with increasing aspect ratios. While continuum mechanics concepts can be used to describe the first two types of deformation, statistical methods will be necessary to describe the dynamics of wire-like long tubes.

[DOI: 10.1115/1.1751181]

Keywords: Carbon Nanotubes, Mechanical Properties, Buckling Folding, Shell, Rod, Macromolecule

## 1 Introduction

Since their discovery in 1991 by Iijama [1], carbon nanotubes (CNTs) have received tremendous attention from various branches of science. Extensive research studies have been carried out via varieties of experimental, theoretical and computer simulation approaches. One of the striking features of CNTs is the enormous potential to use them in nanoscale devices. Due to their very interesting mechanical, optical and electrical properties, CNTs could become one of the best nanomaterials to be established as one of the cornerstones for tomorrow's technology.

CNTs are found in various configurations and geometries [2]. Essentially, they consist of a graphite sheet rolled along a certain orientation into a tube. If the tube consists of a single graphite layer, it is referred to as a single wall nanotube (SWNT). If there are more than one layers in one tube, the tube is referred to as a multi-wall nanotube (MWNT). SWNTs are usually found in bundles of nearly parallel tubules but individual SWNTs are sometimes found as well. SWNTs are known be extremely flexible. They can be easily bent into arcs with very small curvatures on the order of several nanometers or below. CNTs are considered the strongest and most flexible molecular material because of the C-C covalent bonding and seamless hexagonal network architecture. Van der Waals (vdW) forces dominate the interlayer and intertubular interactions between carbon nanotubes.

SWNTs have already found applications in technological devices. They are for instance used as sensors to detect protein binding [3]. Other research has revealed that DNA can be spontaneously encapsulated into a SWNT if the tube radius exceeds a critical value [4]. All these mechanisms could potentially be integrated in nanodevices, as for example in lab-on-a-chip technology. A proper understanding of the mechanics of SWNT is crucial to engineer novel nanoscale devices. A joint treatment using classical mechanics method (e.g., continuum finite element method) in conjunction with studies on the atomic scale will be important for such type of novel engineering in the 21st century.

In nanoscale devices, large stresses can occur due to thermal or lattice mismatch between different materials. Therefore, the reliability of many devices depends critically on the understanding of the response of CNT to mechanical loading. In consequence, mechanical properties of SWNT have received considerable interest in the past. Some of the major questions of mechanical properties of CNTs are how much strain can a CNT sustain elastically, and what are the deformation mechanisms.

Yacobsen et al. (1996) [5] investigated the behavior of single, free-standing SWNTs under compressive loading using classical, molecular-dynamics (MD) with empirical potentials. The longest tube considered was 6 nm with a diameter of 1 nm. The authors developed a continuum shell model to describe the buckling modes of the CNTs. Ozaki and co-workers (2000) [6] investigated SWNTs under axial compression using tight binding (TB) MD methods and system sizes up to a few thousand atoms. In their studies, the length of the nanotubes was limited to about 14 nm with a diameter of 0.67 nm. A ripple shell buckling was observed once the SWNT was put in compressive loading. The details of the ripple buckling (e.g., the ripple wavelength) were found to be strongly dependent on the temperature, and the stress under large strain and zero temperature depends on the helicity. SWNTs under tensile and compressive loading were studied by Dereli and Ozdogan (2003) [7] using a TB-MD scheme in an attempt to obtain the stress-strain curve, theoretical strength and Poisson's ratio for SWNTs. The authors modeled CNTs with about 400 atoms, featuring a total length of 20 layers, corresponding to a few nanometers. Ru (2003) [8] recently considered buckling of a double walled carbon nanotube embedded in an elastic medium under compressive loading using a double-shell continuum mechanics model. The main finding was that critical buckling strain for MWNTs may be reduced compared to SWNTs, indicating that MWNT could even be more susceptible to axial buckling than SWNTs. Other research focused on the mechanical properties of CNTs filled with small molecules. The authors in [9] investigated compression of CNTs filled with nanoparticles and molecules

---

Contributed by the Materials Division for publication in the JOURNAL OF ENGINEERING MATERIALS AND TECHNOLOGY. Manuscript received by the Materials Division June 30, 2003; revision received March 1, 2004. Associate Editor: Y. Huang.

Journal of Engineering Materials and Technology
JULY 2004, Vol. 126 / 245
Copyright © 2004 by ASME

(e.g., $C_{60}$, $NH_4$). The longest tube considered had a length around 20 nm. Research has also been carried out to investigate the elastic properties of CNTs. As recently shown by Hod and Rabani (2003) [10], SWNTs can be bent into closed-ring structures ("nano-rings"). The authors in [10] used the Tersoff-Brenner potential in a classical MD scheme to study the elastic properties of the CNT ring structure. There are also studies focused on the interaction between different CNTs. It was shown that when SWNTs are formed into bundles due to vdW interaction [11], their cross-section shape can change significantly. The change in shape can modify the flexural rigidity and promote bending or other forms of elastic deformation [11]. The shape change can also affect the electrical conductivity of CNTs. Failure mechanisms such as fracture nucleation in SWNTs under tension have been discussed using a combined continuum-atomistic approach [12].

Significant research has been carried out to understand the behaviors of SWNT under mechanical loading. However, most studies in the literature are directed at short tubes with length below 20 nm and diameter in the range of 1-2 nm. The reason of studying nanotubes with rather small aspect ratios can at least partly be attributed to limited computational resource in the past. Experiments, on the other hand, have shown that SWNTs can grow to lengths above 700 nm with a diameter of 0.9 nm, resulting in an aspect ratio as large as about 800 [2]. Such long SWNTs could potentially be utilized as nanowires or means to transport biological or other molecules. On the other hand, today's supercomputer technology and parallel computing algorithms have allowed MD simulations to be performed on system sizes up to one billion atoms and time scales up to nanoseconds [13]. The aim of the present work is to investigate mechanical properties of very long SWNTs under compressive loading using MD simulation techniques.

The paper proceeds as follows. First, we give a brief introduction into the numerical method and the interatomic potential. MD simulations of a SWNT with a fixed diameter but variable length under compressive loading by constant displacement rate will then be discussed in some detail. We report different failure mechanisms ranging from shell buckling for very short tubes to Euler buckling for long tubes to flexible macromolecule like behavior for very long tubes. We discuss different failure modes and their implications.

## 2 Computer Simulation Tool and Setup

### 2.1 Simulation Tool.
Our simulation tool is classical molecular dynamics (MD) [14]. MD predicts the motion of a large number of atoms by numerically integrating the equations of motion governed by interatomic interaction. Normally, we have to rely on classical MD to simulate system sizes above 50,000 atoms and time-scales on the order of nanoseconds, as such system sizes and time scales are still beyond the capabilities of quantum mechanics based methods.

Interatomic potentials are the core of classical MD methods. During the last decades, numerous potentials describing atomic interaction in various materials with different levels of accuracy have been proposed, each having unique problems and strengths. Approaches range from quantum-mechanics based treatments (e.g., tight-binding potentials) to multi-body potentials. For covalently-bonded materials like carbon or silicon, bond-order multi-body potentials have been developed (e.g., Tersoff potential or Stillinger-Weber [15,16]). These multi-body potentials capture not only pair wise interactions, but also additional contributions from the local geometric configuration of the neighboring atoms.

In the present work, we use the Tersoff potential [15] to describe the interatomic bonding of C-C atoms. The Tersoff potential has proven to be a reliable empirical potential to describe the bonding inside carbon nanotubes (bond length of C-C bonds is 1.4218 $\mathring{A}$). For the van der Waals interaction between nonbonding atoms, we use Lennard-Jones potential [14] with parameters $\sigma$=3.89 $\mathring{A}$, and $\varepsilon$=0.005 eV. The time step is chosen to be $\Delta t$$\approx$$1\cdot10^{-15}$ sec.

![](./images/812345319537770496_1.jpg)

Fig. 1 Simulation setup of a single wall carbon nanotube under compressive loading. The loading is controlled by constant displacement rate at both ends. The geometry of the SWNT is specified by the tube length L and diameter d.

### 2.2 Simulation Setup.
We consider a single wall (N,N) armchair nanotube of length L and a diameter d which is dependent on the choice of N. We study SWNTs ranging from (4,4) to (20,20) corresponding to a diameter range from about 0.6 nm to about 3 nm. For our studies, it is useful to define the nanotube aspect ratio as $\mu$=$L/d$. We consider SWNTs with aspect ratios ranging from around five up to values as large as several hundred. Figure 1 shows the simulation setup. The outermost layers of atoms near the axial ends of the SWNT are fixed in all directions, and are moved stepwise according to a prescribed loading history. This displacement controlled loading induces a compressive strain onto the SWNT.

The displacement rate is chosen to be around 5 m/s. This is two orders of magnitudes below the sound velocities which is on the order of several km/s.

## 3 Simulation Results

### 3.1 Shell Buckling: SWNT as a Shell.
We begin with compression of nanotubes at small aspect ratios. In this geometry, CNTs are hollow molecules reminiscent of macroscopic objects in continuum mechanics referred to as "shells". Deformation in such cases can be effectively described by the elastic shell theory (see, e.g., [5,6]).

Prior to compressive loading, we initialize the system at a temperature close to zero. A compression of constant displacement rate is then imposed at the tube ends. The result of this simulation is depicted in Fig. 2 for a (20,20) SWNT with an aspect ratio of $\mu$$\approx$5. The initially "perfect" circular shell structure is elastically deformed and buckles under compression. We find that the buckle begins to appear at a critical applied strain, and may change its shape as the load increases. The mode of deformation is shown in more detail in the inlay in Fig. 2. The buckling is completely elastic (reversible upon unloading) in the beginning. If the compressive strain becomes too large, plastic deformation may occur due to generation of atomic defects in the nanotube.

The continuum theory of shells [17-19] explains that the buckling appears due to instabilities governed by elastic energy. The energy of a shell can be expressed as a surface integral of the quadratic form of deformation [17-19] and instability occurs because buckling tends to decrease energy above a critical strain. Elastic deformation can be regarded as small perturbations from the original shape and decomposed into Fourier harmonics, corresponding to I azimuthal lobes and J half waves (referred to as "(I,J) pattern") along the tube. The Fourier decomposition of elastic deformation then involve modal functions like sin(2Iy/d),

![](./images/812345319537770496_2.jpg)

Fig. 2 Time sequence of the shell-buckling mode of SWNTs at small aspect ratios. The deformation is similar to that reported in [5] for similar aspect ratios but smaller tubes. Atoms are colored according their potential energy. The red color highlights high-potential energy regions such as those associated with stress concentration.

$\cos(2Iy/d)$, $\sin(\pi Jx/L)$, and $\cos(\pi Jx/L)$. Upon a critical strain, the perfect shape of the cylinder becomes unstable and the structure lowers its energy by assuming a $(I,J)$ pattern.

An important observation of SWNTs with small aspect ratio is that they do not bend with respect to the tube axis, even if the strain is significantly increased. The short tubes maintain their symmetry axis even under very large compressive strains.

As discussed in [5], the critical strain for shell buckling depends on the diameter $d$ as
$$
\varepsilon_{S} \propto \frac{1}{d} \tag{1}
$$

The tube length $L$ has little effect on shell buckling.

### 3.2 Euler Buckling: SWNT as a Rod.
When we increase the aspect ratios $\mu>20$, much different behaviors emerge. As in the previous case, we initialize the system at a temperature close to zero. Figure 3(a) suggests that upon application of compressive strain, a local shell buckling similar, but not identical, to that observed in the previous case is generated near the ends of the nanotube. However, unlike in the previous case where the buckle spans over the complete CNT, the buckle in the present case is restricted to localized regions along the tube length, with much of the tube remaining in the cylindrical shape. We find three of such localized buckling regions allowing for out-of-plane bending of the CNT. The overall deformed shape is very reminiscent of Euler buckling of a rod subject to clamped boundary conditions at both ends. In contrast to shell buckling, the CNT bends with respect to the tube axis after buckling occurs. These results indicate that compressive loading causes Euler-buckling of long CNTs via localized regions of severe shell distortion along the tube length. Similar deformation mode has previously been observed in CNTs under bending, but our study seems to be the first to associate it with Euler buckling under compression Fig. 3(b) shows some details of the deformation. It seems that the proper continuum description of buckling of long nanotubes is no longer a cylindrical shell as in the previous case, but rather Euler buckling of a rod.

Study of how an elastic rod behaves under increasing compressive loading dates back to Euler in the 18th century. Euler was the first to investigate mechanical properties of very thin and long structures. He found that a rod with large aspect ratios under compressive loading undergoes an instability called buckling above a critical value of the applied load. For a clamped rod with length $L$ and flexural rigidity $D=EI$, the critical buckling load is [17-21]
$$
F_{E}=\pi^{2} \frac{4 D}{L^{2}} \tag{2}
$$

This critical load is inversely proportional to the square of the length and proportional to the flexural rigidity. The deformation can be described by the first buckling mode of a clamped rod as
$$
1-\cos\left(\frac{2 \pi x}{L}\right) \tag{3}
$$
which describes, in an approximate way, quite well the overall shape of buckled nanotubes in our simulations (see, e.g., Fig. 3(b)). The flexural rigidity is linearly proportional to the Young's modulus of the material, $D \propto E$, and is related to the radius of the rod according to $D \propto d^{3}$ (geometrical moment of inertia). In terms of the aspect ratio $\mu$, the critical load is, therefore,
$$
F_{E} \propto \frac{d^{3}}{L^{2}}=\frac{d}{\mu^{2}} \tag{4}
$$

The critical strain for Euler Buckling then scales as
$$
\varepsilon_{E} \propto \frac{d^{2}}{L^{2}}=\frac{1}{\mu^{2}} \tag{5}
$$

We find in the simulations that the longer the CNT, the smaller the critical strain for buckling, in agreement with the Euler theory.

![](./images/812345319537770496_3.jpg)

Fig. 3 Time sequence of rod-like long range buckling of a nanotube with large aspect ratio: (a) buckles are generated near the tube ends and flow toward the center of the tube; and (b) the overall deformation of the nanotube is reminiscent of Euler buckling of an elastic rod. Atoms are colored according their potential energy. The red color highlights high-potential energy regions. The larger the aspect ratio, the smaller the critical strain for buckling.

The transition from shell-buckling to rod-buckling is then well predicted by continuum mechanics. For a CNT with a constant diameter $d$, the critical strain for shell buckling at small tube lengths would remain constant [5], as suggested by Eq. (1). In contrast, Eq. (5) predicts that the critical strain for rod buckling decreases inversely with the square of the length. This implies that beyond a critical aspect ratio, the critical strain for Euler buckling would be lower than that required for shell buckling. Therefore, a transition from shell buckling at small aspect ratios to rod buckling at large aspect ratios is expected even for a continuum tube.

In Fig. 4 we plot the critical strain for buckling initiation as a function of the aspect ratio of the (20,20) SWNT. The continuum

![](./images/812345319537770496_4.jpg)

Fig. 4 Critical strain for shell buckling or rod buckling as a function of the aspect ratio for a (20,20) SWNT (the length changes while the diameter is kept constant). The plot shows continuum theory predictions of critical buckling strain for short tubes (straight, dotted line) and long tubes (continuous line). The intersection point defines the critical aspect ratio at which the deformation mode switches from shell buckling to rod buckling. This is found to be around $\mu_T$$\approx$12.5.

predictions of Eq. (1) and Eq. (5) are also plotted for comparison. Note that the critical strain for Euler buckling increases monotonically as the aspect ratio is reduced. The MD simulations show a decrease of the critical strain with decreasing length below the critical aspect ratio. This is at odds with the continuum prediction of shall buckling and may be caused by the effects of boundary conditions or nanotube size. For large aspect ratios, the critical strains are relatively close to the prediction by the Euler theory.

The numerical results indicate that, in contrast to continuum predictions of a constant buckling load at a constant diameter, the buckling strength actually decreases with the nanotube aspect ratio in the regime of shell buckling. The simulations thus suggest that there exists an "optimal" aspect ratio for which CNTs can sustain the highest external loading without buckling. This optimal aspect ratio corresponds to the transition from shell buckling to Euler buckling, which is found at an aspect ratio of $\mu_T$$\approx$12.5 for the (20,20) tube under consideration.

3.3 Wire Like Behavior: CNT as a Macromolecule. In the previous sections we have reported a transition from shell buckling to rod buckling in SWNTs under compression as the length-to-diameter aspect ratio increases. This transition could be explained by continuum theory of thin tube. If the aspect ratio becomes even larger, we observe yet another transition characterized by a transition from rod-buckling to folding of a flexible macromolecule. The deformation mode is briefly described below.

The temperature of the system is chosen to be around 300 K before the loading is applied. The lengths of the CNT range from 150 nm to 350 nm, which refers to aspect ratios up to 580. We study (4,4) and (8,8) SWNTs.

Some time snapshots are depicted in Fig. 5 for a (4,4) SWNT with a diameter of about 0.6 nm. Upon compression, this very long CNT starts to "fold" like a flexible macromolecule. The simulation results indicate that very long SWNTs tend to form helical structures.

The mechanics of deformation could be described in the following way. Like polymeric molecules, CNTs have an associated persistent length associated with bending deformation. If the tube length is smaller than the persistent length, the mechanical behavior of CNTs would be like an elastic rod or cylindrical shell. If the tube length exceeds the persistent length, bending of one part of CNT becomes decoupled from another and the CNT behaves like a flexible wire. This is a common feature among many biomolecules such as DNA, RNA and peptides. Long flexible molecules are known to subject to form self-folded structures.

![](./images/812345319537770496_5.jpg)

Fig. 5 Time sequence of macromolecule like deformation of SWNTs at very large aspect ratios. Upon application of compressive loading, the nanotube immediately starts to fold into a helical structure. The inlay shows a detailed view of the SWNT, illustrating high flexibility. The CNT shown here is a (4,4) SWNT.

Therefore, very long CNTs are also expected to fold to minimize thermodynamic free energy and may undergo phase transitions at different temperatures. CNTs also exhibit a "self-folding" mechanism where different parts of the same nanotube align to form bundles via van der Waals interactions. This is certainly possible due to the great flexibility of long CNTs. The self-folded SWNT bundles are indeed observed, as shown in Fig. 6, as the VdW forces fold CNT into a self-adhered folding structure.

Simulations of the very thin (4,4) nanotube illustrate the macromolecular behavior of CNTs. In fact, existence of even thinner tubes down to (3,3) has been verified by quantum mechanical calculations [21] and experiments [22]. We have also repeated the simulation for a (8,8) tube and obtained the same qualitative results, suggesting that the macromolecular behavior not only appears in very thin CNTs, but also in tubes with larger diameters provided the aspect ratio is sufficiently large.

## 4 Discussion, Conclusions, and Outlook

We have shown that SWNTs under compressive loading may undergo different deformation mechanisms as the aspect ratios increase. Our results suggest three different classes of mechanical response for nanotubes in compression.

For nanotubes with very small aspect ratios, the deformation mechanism is characterized by buckling of the cylindrical shell structure. Our results are similar to the deformation patterns observed by Yacobsen et al. (1996) [5], although we used CNTs with three times larger diameter and length at the same length-to-diameter aspect ratio. This serves as an indication that the CNT buckling depends primarily on the aspect ratio.

Beyond a critical aspect ratio, the shell-buckling behavior of CNTs changes to rod-buckling described by the Euler theory of

![](./images/812345319537770496_6.jpg)

Fig. 6 Self-folding of CNT. The macromolecule like CNT can fold upon itself. Different parts of the CNT can be brought into adhesive contact by the vdW interaction. The "self-zipping" can form a rather stable agglomerate at certain temperatures.

![](./images/812345319537770496_7.jpg)

Fig. 7 Overview of deformation mechanisms of SWNTs in compression: Shell-rod-wire transition as a function of the length-to-diameter aspect ratio of the CNT. The plot shows different modes of deformation: (a) buckling of the cylindrical shell structure; (b) rod-like behavior with localized buckling along the length of the tube; and (c) a flexible macromolecule.

continuum mechanics. Similar Euler buckling in $SiO_{2}$ nanobeams of high aspect ratios in compression was recently reported by Carr et al. (2003) [23] nanobeams.

From our simulations, we estimate a critical aspect ratio of $\mu_{T} \approx 12.5$ for the transition from shell buckling to rod buckling.

For extremely large aspect ratios, the CNT is found to behave like a flexible macromolecule and tends to deform into helical structures. For even larger aspect ratios, the tube is extremely flexible and behaves as a bio-molecule. This suggests a shell-rod-wire transition of the mechanical behavior of carbon nanotubes with increasing aspect ratios.

The three different deformation mechanisms of SWNTs are summarized in Fig. 7. The first two classes of deformation (shell and rod) could be effectively described by continuum mechanics concepts. However, statistical mechanics and entropic forces appear to play an important role in the third class, the wire-like behavior of nanotubes with very large aspect ratios. Statistical theories of macromolecules may be used to analyze the dynamics of such nanostructures. Thermodynamical properties of very long and thin CNTs will be an interesting subject for further study. The observation of a "self-folding" mechanism where different parts of the same CNT are brought into adhesive contact indicates that CNTs become very flexible at very large aspect ratios (see self-folded state shown in Fig. 6). In this case, different parts of the CNTs attract each other due to the vdW interaction. It will be interesting to further study such self-folding under entropical forces. A broader investigation is left to the future work [26].

Other possible future research could focus on the mechanical response of MWNTs under compressive loading. Continuum analyses suggest that they may be more sensitive to buckling than SWNTs [8]. Also, MWNTs may behave as macro-molecules at very large aspect ratios. The interlayer vdW interactions of MWNTs may affect the overall thermodynamic properties and it may require new developments in statistical mechanics to fully describe the thermodynamics of flexible MWNTs.

Designing nano-scale devices remains a challenging task. Design engineers usually rely on a set of design rules to create new structures and devices. Such methods exist for instance for an estimate of the critical diameter of a truss member. In the classical "macroscopic" engineering fields (e.g., mechanical or civil engineering), such concepts are well established. However, there are few design concepts available for nano-scale devices. Developing such design concepts could become a challenging and important task for future research. The study reported in this paper may serve as an example how atomistic simulations combined with continuum mechanics concept can help improve our understanding of the behaviors of nanostructures.

Acknowledgment

The simulations were carried out in the Garching Supercomputer Center of the Max Planck Society. The MD calculations are preformed using the ITAP IMD code [24,25] which was kindly provided to us by the group of Prof. Hans Trebin at the Institute for Theoretical and Applied Physics (ITAP) of University of Stuttgart along with helpful discussions on MD simulations of covalently bonded systems.

References

[1] Iijima, S., 1991, "Helical Microtubules of Graphitic Carbon," Nature (London), 354, p. 56.

[2] Dresselhaus, M. S., Dresselhaus, G., and Eklund, P. C., 1996, Science of Fullerenes and Carbon Nanotubes, Academic Press, San Diego.

[3] Star, A., Gabriel, J.-C. P., Bradley, K., and Grüner, G., 2003, "Electronic Detection of Specific Protein Binding Using Nanotube FET Devices," Nano Lett., 3(4), pp. 459-463.

[4] Gao, H., Kong, Y., Cui, D., and Ozkan, C., 2003, "Spontaneous Insertion of DNA Oligonucleotides Into Carbon Nanotubes," Nano Lett., 3, pp. 471-473.

[5] Yacobsen, B. I., Brabec, C. J., and Bernholc, J., 1996, "Nanomechanics of Carbon Tubes: Instabilities Beyond Linear Response," Phys. Rev. Lett., 76(14), p. 2511.

[6] Ozaki, T., Iwasa, Y., and Mitani, T., 2000, "Stiffness of Single-Walled Carbon Nanotubes Under Large Strain," Phys. Lett., 84(8), p. 1712.

[7] Dereli, G., and Ozdogan, C., 2003, "Structural Stability and Energetics of Single-Walled Carbon Nanotubes Under Uniaxial Strain," Phys. Rev. B, 67(3), 035416.

[8] Ru, C. Q., 2001, "Axially Compressed Buckling of a Doublewalled Carbon Nanotube Embedded in an Elastic Medium," J. Mech. Phys. Solids, 49(6), pp. 1265-1279.

[9] Ni, B., Sinnott, S. B., Mikulski, P. T., and Harrison, J. A., 2002, "Compression of Carbon Nanotubes Filled With C-60, CH4, or Ne: Predictions From Molecular Dynamics Simulations," Phys. Rev. Lett., 88(20), 205505.

[10] Hod, O., and Rabani, E., 2003, "Carbon Nanotube Closed-Ring Structures," Phys. Rev. B, 67, p. 195408.

[11] Hertel, T., Walkup, R. E., and Avouris, P., 1998, "Deformation of Carbon Nanotubes by Surface van der Waals Forces," Phys. Rev. B, 58, p. 13870.

[12] Zhang, P., Huang, Y., Gao, H., and Hwang, K. C., 2002, "Fracture Nucleation in Single-Wall Carbon Nanotubes Under Tension: A Continuum Analysis Incorporating Interatomic Potentials," J. Appl. Mech., 69(4), pp. 454-458.

[13] Abraham, F. F., Walkup, R., Gao, H., Duchaineau, M., de La Rubia, T., and Seager, M., 2002, "Simulating Materials Failure by Using Up to One Billion Atoms and the World's Fastest Computer: Work-Hardening," Proceedings of the National Academy of Sciences of the United States of Americ (PNAS), 99, pp. 5783-5787.

[14] Allen, M., and Tildesley, D., 1989, Computer Simulation of Liquids, Oxford University Press.

[15] Tersoff, J., 1988, "New Empirical Approach for the Structure and Energy of Covalent Systems," Phys. Rev. B, 37, p. 6991.

[16] Brenner, D. W., 1990, "Empirical Potential for Hydrocarbons for Use in Simulating the Chemical Vapor Deposition of Diamond Films," Phys. Rev. B, 42, p. 9458.

[17] Landau, L. D., and Lifshitz, E. M., 1986, Elasticity Theory, Pergamon, Oxford.

[18] Allen, H., and Bulson, P., 1980, Background to Buckling, London, McGraw Hill.

[19] Timoshenko, S., and Gere, J., 1988, Theory of Elastic Stability, New York, McGraw-Hill.

[20] Feynman, R., Leyton, R., and Sands, M., 1964, The Feynman Lectures in Physics, 2, Addison-Wesley, Reading.

[21] Liu, H. J., and Chan, C. T., 2002, "Properties of $4 \mathring{A}$ Carbon Nanotubes From, First-Principle Calculations," Phys. Rev. B, 66, pp. 115416.

[22] Marin, C., Serrano, M. D., Yao, N., and Ostrogorsky, A. G., 2003, "Evidence for a Bundle of $4 \mathring{A}$ Single-Walled Carbon Nanotubes," Nanotechnology, 14(3), pp. L4-5.

[23] Carr, S. M., and Wybourne, M. N., 2003, "Elastic Instability of Nanomechanical Beams," Appl. Phys. Lett., 82(5), p. 709.

[24] Roth, J., Gähler, F., and Trebin, H.-R., 2000, "A Molecular Dynamics Run With 5.180.116.000 Particles," Int. J. Mod. Phys. C, 11, pp. 317-322.

[25] Stadler, J., Mikulla, R., and Trebin, H.-R., 1997, "IMD: A Software Package for Molecular Dynamics Studies on Parallel Computers," Int. J. Mod. Phys. C, 8, pp. 1131-1140.

[26] Buehler, M. J., Kong, Y., Gao, H., and Huang, Y., 2004, "Self-Folding and Unfolding of Carbon-Nanotubes," Proceedings of ASME-IMECE 2004, November 13-19, 2004, Anaheim, CA, USA.

---
Journal of Engineering Materials and Technology
JULY 2004, Vol. 126 / 249
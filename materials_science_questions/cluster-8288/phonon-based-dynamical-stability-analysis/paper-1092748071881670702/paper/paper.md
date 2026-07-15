
# A Panoramic View of MXenes via a New Design Strategy

Noah Oyeniran \( ^{a} \) , Oyshee Chowdhury \( ^{a} \) ; Chongze Hu \( ^{a*} \) , Traian Dumitrica \( ^{b} \) , Panchapakesan Ganesh \( ^{c} \) , Jacek Jakowski \( ^{d} \) , Zhongfang Chen \( ^{e} \) , Raymond R. Unocic \( ^{f} \) , Michael Naguib \( ^{g} \) , Vincent Meunier \( ^{h} \) , Yury Gogotsi \( ^{i} \) , Paul R. C. Kent \( ^{d} \) , Bobby G. Sumpter \( ^{c} \) , Jingsong Huang \( ^{c*} \) 

 \( ^{a} \)  Department of Aerospace Engineering and Mechanics, The University of Alabama, Tuscaloosa, Alabama 35487, USA

 \( ^{b} \)  Department of Mechanical Engineering, University of Minnesota Twin Cities, Minneapolis, Minnesota 55455, USA

 \( ^{c} \)  Center of Nanophase Materials Sciences, Oak Ridge National Laboratory, Oak Ridge, Tennessee 37831, USA

 \( ^{d} \)  Computational Sciences and Engineering Division, Oak Ridge National Laboratory, Oak Ridge, Tennessee 37831, USA

 \( ^{e} \)  Department of Chemistry, University of Puerto Rico, Rio Piedras, San Juan, Puerto Rico 00931, USA

 \( ^{f} \)  Department of Materials Science and Engineering, North Carolina State University, Raleigh, North Carolina 27695, USA

 \( ^{g} \)  Department of Physics and Engineering Physics, Tulane University, New Orleans, Louisiana 70118, USA

 \( ^{h} \)  Department of Engineering Science and Mechanics, The Pennsylvania State University, University Park, Pennsylvania 16801, USA

 \( ^{i} \)  Department of Materials Science and Engineering, and A.J. Drexel Nanomaterials Institute, Drexel University, Philadelphia, Pennsylvania 19104, USA

 \( ^{*} \) Corresponding authors

Email address: hucz@ua.edu (Chongze Hu) and huangj3@ornl.gov (Jingsong Huang)

Notice: This manuscript has been authored by UT-Battelle, LLC, under Contract No. DE-AC0500OR22725 with the U.S. Department of Energy. The United States Government retains and the publisher, by accepting the article for publication, acknowledges that the United States Government retains a non-exclusive, paid-up, irrevocable, worldwide license to publish or reproduce the published form of this manuscript or allow others to do so, for the United States Government purposes. The Department of Energy will provide public access to these results of federally sponsored research in accordance with the DOE Public Access Plan (http://energy.gov/downloads/doe-public-access-plan).
 

## Abstract

Two-dimensional (2D) transition metal carbides and nitrides, known as MXenes, possess unique physical and chemical properties, enabling diverse applications in fields ranging from energy storage to communication, catalysis, sensing, healthcare, and beyond. The transition metal and nonmetallic atoms in MXenes can exhibit distinct coordination environments, potentially leading to a wide variety of 2D phases. Despite extensive research and significant advancements, a fundamental understanding of MXenes' phase diversity and its relationship with their hierarchical precursors, including intermediate MAX phases and parent bulk phases, remains limited. Using high-throughput modeling based on first-principles density functional theory, we unveil a wide range of MXenes and comprehensively evaluate their relative stabilities across a large chemical space. The key lies in considering both octahedral and trigonal prismatic coordination environments characteristic of various bulk phases. Through this comprehensive structural library of MXenes, we uncover a close alignment between the phase stability of MXenes and that of their hierarchical 3D counterparts. Building on this, we demonstrate a new design strategy where the atomic coordination environments in parent bulk phases can serve as reliable predictors for the design of MXenes, reducing reliance on intermediate MAX phases. Our study significantly expands the landscape of MXenes, at least doubling the number of possible structures.

## Introduction

Layered transition metal carbides (TMC) or nitrides (TMN), also known as MXenes, have emerged as a class of promising two-dimensional (2D) materials since the discovery of monolayer  \( Ti_{3}C_{2} \)  in 2011 \( ^{1-7} \) . To date, more than 50 MXenes have been synthesized (MX structures, not counting solid solutions and distinct surface terminations), and over 100 distinct MXenes have been theoretically predicted based on combinations of M and X elements \( ^{8} \) . The chemical formula of MXenes is typically written as  \( M_{n+1}X_{n}T_{x} \) , where M represents an early transition metal (lanthanides have been added recently \( ^{9,10} \) ), X represents carbon (C) or nitrogen (N), and  \( T_{x} \)  represents surface functional groups such as oxygen (O), fluoride (F), chloride (Cl), hydrogen (H), hydroxyl (-OH), chalcogens, among others; n is the layer number (n = 1-4); and x is the number of surface terminations per unit formula (typically x = 2). Due to the large variety of transition metals (M) and surface functional groups ( \( T_{x} \) ), MXenes exhibit a huge (virtually infinite) compositional space and unique and highly tunable material properties, which provide them with a significant potential for various practical applications, such as catalysis \( ^{11,12} \) , superconductivity \( ^{6} \) , energy storage \( ^{13} \) , environmental remediation \( ^{14} \) , electromagnetic devices \( ^{15} \) , and many others \( ^{13,16} \) .

Experimentally, 2D layered MXenes are typically synthesized by selectively etching the “A” layers in their precursor MAX phases \( ^{17-19} \) ,  \( M_{n+1}AX_{n} \) , followed by a delamination process using intercalation and mechanical agitation/sonication \( ^{20} \)  or other techniques such as liquid exfoliation \( ^{21,22} \) . It is widely recognized that MXenes can inherit similar crystal structures as those of layered MAX phases \( ^{23} \) . For instance, aberration-corrected scanning transition electron microscopy (AC-STEM) combined with refined X-ray (XRD) measurements \( ^{6} \)  have revealed the structural relationships between the three-dimensional (3D)  \( Ti_{3}AlC_{2} \)  MAX phases and their associated  \( Ti_{3}C_{2}T_{x} \)  MXene, where the MXene inherits the hexagonal closed packed (HCP) arrangement of the MAX phases. One notable feature of this crystal structure is that the carbon atoms located between Ti layers are octahedrally bonded with six nearest-neighbor Ti elements, reminiscent of a face-centered cubic (FCC)-like local crystal structure \( ^{9,24} \) . However, some
 

experimental and computational studies have demonstrated that the X elements (C and/or N), located between M layers, can form a trigonal prismatic coordination environment with six surrounding M elements \( ^{25-36} \) . Notably, some MXene phases are more energetically and structurally stable in this form than the octahedral one \( ^{25-36} \) . These findings suggest that the stability of MXenes is influenced not only by their 3D precursor (e.g., MAX phases) but also by the local coordination arrangements of both X and M elements within the layered MXenes.

The study of phase stability in MXenes, specifically between octahedral and trigonal prismatic coordination, parallels prior research on transition metal dichalcogenides (TMDs) \( ^{37} \) . Using nomenclature similar to TMDs, a monolayer MXene with octahedral coordination can be termed as the 1T phase, while a structure with trigonal prismatic coordination can be referred to as the 1H phase (or 2H phase, considering termination elements in some studies \( ^{25} \) ). Extensive studies have examined the stability of the 1T and 1H phases across a series of MXenes. For example, carbide-based MXenes with groups III and IV transition metals and nitride-based MXenes with group IV transition metals are typically stable in the 1T phases \( ^{26, 28, 32, 35} \) , while both carbide- and nitride-based MXenes with group VI elements are more likely to form the 1H phases \( ^{26, 33, 35, 36, 38} \) . Similar phase stability trends have also been studied in layered transition metal borides, sulfides, and phosphides, with both 1T and 1H phases theoretically predicted in these materials \( ^{27, 39, 40} \) . Given the markedly different material properties exhibited by these phases, understanding their stability is a critical step toward developing novel MXenes with improved properties.

In this work, we systematically investigated the phase stability of MXenes with various local crystal structures, tracing the origins to their hierarchichal precursors, including the intermediate MAX phases and the parent bulk phases. We found that all MXenes, from monolayer to multiple layers  \( (n = 1-3) \) , can be derived from four types of bulk phases, each characterized by unique atomic coordination environments \( ^{41, 42} \) . Using Ti- and Mo-based TMCs and TMNs as model systems, we carried out extensive density functional theory (DFT) calculations and demonstrated that these bulk phases have consistent energetic stability relative to their derived MXene counterparts and the intermediate MAX phases. Furthermore, high-throughput modeling suggests that this structural relationship extends across all transition metals in the periodic table, enabling the direct use of bulk phase information to predict MXene crystal structures without reliance on intermediate MAX phases (Fig. 1a). This study significantly expands the landscape of MXenes, at least doubling the number of possible structures.

## Results

## Nomenclature for MXene structures

Two types of coordinations are commonly observed in 3D bulk TMCs and TMNs, and they are respectively octahedral (denoted as O) and trigonal prismatic (denoted as P), where the former has six atoms that form bond angles of  \( 90^{\circ} \)  around the center atom, while the latter has six atoms arranged in a form of triangular prism. Since both the M and X elements can exhibit these two types of coordination, the combination of them gives four types of bulk structures with various coordination environments (Fig. 1b) with a 1:1 stoichiometric ratio of M to X elements. The first bulk phase has an FCC, rock-salt crystal structure with a coordination sequence O-O respectively for M and X elements. This classical structure, with a space group of  \( Fm\overline{3}m \) , is the most widely observed local crystal structure for the central layers inside
 

MXenes. For convenience, we denote this type of crystal structure as the B1 phase in this study. Additionally, two nickel arsenide (NiAs)-type hexagonal crystal structures \( ^{43} \)  with both O and P coordination are illustrated in Fig. 1b. The first NiAs-type hexagonal structure, denoted as HX1a, has a coordination sequence of P-O, respectively, for M and X elements. The second NiAs-type hexagonal structure has an exchanged coordination sequence O-P for M and X elements, and we denote it as HX1b. These two hexagonal structures have a space group of  \( P6_{3}/mmc \) , which is commonly observed in the MAX phases  \( (\mathrm{M}_{\mathrm{n}+1}\mathrm{AX}_{\mathrm{n}}) \)  or terminated MXenes  \( (\mathrm{M}_{\mathrm{n}+1}\mathrm{X}_{\mathrm{n}}\mathrm{T}_{\mathrm{x}}) \) , as the main group elements A or termination groups T can form such coordination arrangement with surrounding M elements. Finally, a tungsten carbide (WC)-type hexagonal crystal structure, with a space group of  \( P\bar{6}m2^{44} \) , exhibits a P-P coordination sequence for M and X elements. We denoted this type of bulk phase as HX2; see Fig. 1b.

Each bulk phase can yield two variants of MXenes with distinct coordination sequences characterized by different atomic positions of the surface termination elements. Figs. 1c-e illustrate these bulk-derived MXenes, ranging from the thinnest  \( M_{2}XT_{2} \)  to  \( M_{4}X_{3}T_{2} \) . For  \( M_{2}XT_{2} \)  (Fig. 1c), the B1-derived MXenes have two types of coordination sequence for M-X-M: O'-O'-O' and P'-O-P', based on the termination element positions, where the prime symbol (') denotes the coordination of the outermost layer of M elements. These structures are referred to as T-1 and T-2, respectively (Fig. 1c). Owing to the octahedral coordination of the middle layer of X element, the HX1a-derived MXenes share the same coordination sequence as the B1-derived MXenes, i.e., T-2 and T-1 MXenes (Fig. 1c). In contrast, HX1b- and HX2-derived MXenes, with prismatic coordination for the middle layer of X elements, resulting in two new MXenes with coordination sequences O'-P-O' and P'-P-P', referred to as H-1 and H-2 MXenes, respectively (Fig. 1c). Overall, four types of  \( M_{2}XT_{2} \) -based MXenes with different coordination sequences have been derived from the four bulk phases.

Thicker MXenes,  \( M_{3}X_{2}T_{2} \) , have a more complicated coordination environment than thinner variants. Specifically, the two B1-derived MXenes, T-1 and T-2, have two distinct coordination sequences for the M-X-M-X-M arrangement: O'-O-O-O-O' and P'-O-O-O-P' (Fig. 1d). Different from the thinnest cases, these two MXenes are not the same as HX1a-derived ones, as the central M layer in the latter configuration has prismatic coordination, leading to P'-O-P-O-P' and O'-O-P-O-O' coordination sequences (named as H1a-1 and H1a-2). Similarly, HX1b-derived MXenes exhibit O'-P-O-P-O' and P'-P-O-P-P' coordination sequences, named H1b-1 and H1b-2, respectively (Fig. 1d). In HX2-derived  \( M_{3}X_{2}T_{2} \)  MXenes, both M and X elements adopt prismatic coordination, resulting in P'-P-P-P-P' and O'-P-P-P-O' coordination sequences, which are named as H2-1 and H2-2. Eight different  \( M_{3}X_{2}T_{2} \) -based MXenes with various coordination sequences can be derived from the four bulk phases.

Similar to  \( M_{3}X_{2}T_{2} \) ,  \( M_{4}X_{3}T_{2} \)  MXenes also have eight bulk-derived structures with different coordination sequences (Fig. 1e). Using the same nomenclature, the B1-derived MXenes are designated as T-1 and T-2; HX1a-derived MXenes as H1a-1 and H1a-2; HX1b-derived MXenes as H1b-1 and H1b-2; and HX2-derived MXenes as H2-1 and H2-2 (Fig. 1e).

In total, 20 MXenes  \( (4+8+8) \)  can be derived from the four bulk phases across all three groups of MXenes with different thicknesses. Since most experimentally reported MXenes exhibit B1-derived crystal structures (T-1 and T-2), we estimate that this study effectively doubles the number of currently known MXenes.

## Phase stability of MXenes

With a clear understanding of the crystal structures of MXenes and their associated coordination sequence, we performed DFT calculations to analyze the energetic relationships between the bulk phases, MAX phases, and their derived MXenes. Due to existing experiments, we primarily selected Ti- and Mo-based TMCs and TMNs in this work and chose aluminum (Al) as the “A” layer in the MAX phases \( ^{4} \) . Table 1 summarizes the DFT-calculated phase
 

stability of TiC-based bulk phases, MAX phases, and corresponding MXenes. These results indicate that the B1 phase with an O-O coordination is the most stable, suggesting that octahedral coordination is the most favorable for Ti and C elements. This finding agrees with many prior experimental and computational studies \( ^{4,32} \) .

Interestingly, both TiC-based MAXs and MXenes have similar trends of phase stability as bulk phases. For instance, B1-derived  \( Ti_{2}AlC \)  (MAX) and  \( Ti_{2}C_{F2} \)  (MXene) both exhibit the same order of phase stability as their corresponding bulk phases, reinforcing that octahedral coordination is beneficial to both Ti and C elements in MAX and MXenes. Even in the thicker MAX and MXenes, Table 1 also shows that B1-derived phases, T-1 or T-2, have the most stable structure among all MXenes. This prediction is in line with the trend of bulk phases and thus suggests that all TiC-based  \( Ti_{n+1}C_{n}F_{2} \)  (n = 1-3) MXenes synthesized from the MAX route by HF etching should end up with the B1-derived MXenes.

Similar phase stability trends were found between bulk phases and their associated MAX and MXenes phases for Mo-based carbides. According to DFT calculations, the most stable bulk phase of MoC is HX2 with P-P coordination, suggesting that both Mo and C preferably adopt trigonal prismatic coordination. This observation is consistent with prior studies \( ^{25,28,33} \) . By examining the energetic stability of MoC bulk-derived MAX phases and MXenes, we found that HX2-derived structures are generally the most stable, especially when  \( n \geq 2 \) . This finding indicates that MoC-based MXenes synthesized by the MAX route through HF etching should end up with HX2-derived structures, where P coordination dominates (Table 2). One exception was found for the thinnest case,  \( Mo_{2}CF_{2} \) , where the most stable configuration in the  \( Mo_{2}AlC \)  MAX phase is B1-derived T-1. This exception is probably because Al layers are more favorable in forming octahedral coordinates with the outermost Mo layers. Still, after etching the Al layers, the monolayer  \( Mo_{2}CF_{2} \)  becomes more energetically favorable in a hexagonal structure.

Furthermore, we systematically performed DFT calculations to evaluate the structural stability of nitrides-based MAX phases and MXenes for all bulk-derived configurations. Our results consistently show that TiN- and MoN-based MAX and MXenes always exhibit a very similar order of phase stability compared to their bulk counterparts (Suppl. Tables S1-2). These findings further indicate that bulk phases can serve as an effective indicator to predict the stable structures of MXenes in terms of their coordination environment; we carried out DFT calculations for 240 MXenes structures for Ti- and Mo-based carbide and nitride MXenes with three different termination groups (oxygen termination, fluoride termination, and non-termination). All DFT-calculated energies and lattice parameters of these MXenes are documented in Suppl. Tables S3-16.

## Lattice-dynamical stability of MXenes

Building on the prior analysis, we conclude that MXenes can be rationally designed based on the stability of their bulk counterparts. However, confirming their lattice dynamical stability is crucial to ensure they represent local minima on the potential energy surface and are viable for experimental synthesis. Thus, we performed density functional perturbation theory (DFPT)-based phonon calculations to evaluate the lattice-dynamical stability of all MXenes studied in this work. Based on the calculated phonon spectra (Suppl. Figs. S1-30), we identified the stable MXenes of all Mo- and Ti-based MXenes with three termination groups: non-termination, F-termination, and O-termination.

An analysis of the stable MXenes for non-termination cases (Figs. 2a-c) reveals that 76 out of 80 ( \( \sim95\% \) ) MXenes across all three thicknesses considered (n = 1-3) are lattice dynamically stable without any imaginary frequency, except a few cases in the  \( Mo_{3}N_{2} \)  and  \( Ti_{4}N_{3} \)  families. These results suggest that the novel MXenes studied in this work, especially those derived from hexagonal bulk phases such as HX1a-, HX1b-, and HX2-derived MXenes, are lattice dynamically stable and feasible to be synthesized under vacuum and observed in experiments.
 

Phonon calculations were also conducted for F- and O-terminated MXenes. Using TiC-based MXenes as one example, some representative phonon spectra of hexagonal-derived MXenes are plotted in Fig. 2d-f. The phonon spectra reveal that most F-terminated TiC MXenes do not exhibit any imaginary frequency, suggesting lattice dynamical stability. Yet, O-terminated TiC MXenes consistently exhibit large imaginary frequencies (Fig. 2d-f), indicating that oxygen atoms are less efficient in stabilizing MXene structures. As summarized in Fig. 2a-c, F-terminated MXenes have more stable configurations than O-terminated cases. For instance, 58 out of 80 (72.5%) F-terminated MXenes are dynamically stable compared to only 45 out of 80 (56.3%) O-terminated MXenes. This finding suggests that F atoms are more effective than O atoms in stabilizing layered structures of MXene, implying that future experiments should adopt hydrogen fluoride to etch the MAX phases to achieve these stable MXenes.

## A comprehensive search for MXene phases

Although DFT calculations have demonstrated that bulk phase stability can effectively predict the stability of MXenes for Ti- and Mo-based systems, the bulk phase stability for other transition metals remains largely unexplored. Therefore, we carried out high-throughput DFT calculations across the periodic tables for transitional metals to calculate the phase stability of their bulk phases based on their ground-state energies. By comparing the relative stabilities of four bulk phases, we identified 13 different ranking orders, which are illustrated by distinct colors across the periodic table in Fig. 3a-b.

Fig. 3a shows the phase stability order of all TMCs. It is evident that group III, IV, and V elements predominantly appear in dark purple, indicating that the most stable MXenes based on these metals should be B1-derived phases. Such a prediction agrees with some prior studies, which have found that Sc-, Ti-, Zr-, Nb-, and Hf-based monolayer carbide MXenes are most stable in an octahedral coordination environment \( ^{26} \) . On the contrary, the yellow regions corresponding to group VI to VIII metals suggest that their favorable bulk phases are HX2, implying that layered MXenes based on these elements are likely to form HX2-based structures.

To verify this trend, we performed DFT calculations to assess the stability of MXenes for two representative transitional metals, i.e., Hf and Re elements, which favor B1- and HX2-bulk phases. As shown in Fig. 3c, the most stable HfC-based MXenes across three thicknesses (n=1-3) are consistently B1-derived T-1 or T-2, but the most stable ReC-based MXenes are always HX2-derived or H1b-derived. These results further confirmed our prior findings that bulk phase stability can be exploited to reliably predict the structural stability of MXenes. It is also worth noting that the most stable bulk phase of group IX to XII metals are either HX1a or HX1b phases, meaning that their associated MXenes will likely adopt these two structures.

Fig. 3b presents the order of phase stability for all TMNs. Interestingly, the color map of this phase stability has one group leftward shift compared to TMCs, which can be ascribed to nitrogen having one extra electron than carbon atoms. The most stable B1 phases of TMNs are observed for groups III, IV, XII, and some group XI metals (dark purple colors). Meanwhile, the HX2 stable bulk phase is mainly from group V metals as well as Cr and Tc. However, there is no clear boundary distinguishing the stability of HX2 and HX1 phases between group VI and X elements (Fig. 3b).

To validate these trends, we again used Hf and Re as representatives to evaluate the phase stability of their MXenes across three layers  \( (n=1-3) \) . As shown in Fig. 3d, HfN-based MXenes consistently exhibit B1-derived (T-2) structures, while ReN-based MXenes tend to have H1b- or HX2-derived structures. Notably, the most favorable B1 phase of HfN suggests that their derived MXenes are highly favorable in octahedral environments, which agrees well with prior observations \( ^{28} \) . Therefore, our calculations once again confirm that bulk phase stability can be
 

used as an indicator to predict the phase stability of layered MXenes.

## Discussion

MXenes are currently synthesized through a top-down approach, starting with their bulk precursor MAX phases, which are then exfoliated into layered 2D phases. While the resulting layered MXenes are typically considered to maintain the same crystal structure as their parent MAX phases, this is not always the case. Reviewing the coordination environment shows that all these 2D phases can be derived from four distinct bulk phases. Subsequent DFT calculations indicate that the structural stability of MXene is always consistent with the phase stability of their bulk counterparts. These findings suggest a design strategy for 2D materials, where the bulk phase can be used as an important indicator to predict the structures and stability of derived MXenes.

Fig. 3e summarizes all reported MXene structures from experiments and modeling efforts since the first discovery of MXene in 2011. The data reveal that the reported MXenes primarily exhibit B1-derived or HX1a-derived structures dominated by the O- or P-type coordination environments, respectively. By extending the analysis to four bulk phases in this study, we show that the internal bulk crystal structure of MXenes, particularly in multiple-layer cases  \( (n \geq 2) \) , can have alternating O- and P-coordination sequences. Recent studies have further demonstrated that MXenes can behave as metastable bulk phases at elevated temperatures, as evidenced by the phase transition of the  \( \sim \) 1 nm-thick  \( Ti_{3}C_{2}T_{x} \)  from hexagonal crystal to the B1 crystal structure \( ^{45-47} \) . Thus, it is reasonable to anticipate that these thick  \( Ti_{3}C_{2}T_{x} \)  can alternate between O and P coordination during the phase transition. Meanwhile, in the presence of external stimuli, MXene may undergo phase-like transformation among the various 2D phases by alternating the coordination sequence, a phenomenon that has been observed in TMD and MAX phases \( ^{48, 49} \) . Therefore, revisiting the crystal structures and their coordination environment of all MXenes is particularly important to understand phase transition behaviors in MXenes.

Finally, this study establishes a structural library of MXenes that extends beyond layered TMC and TMNs to encompass other transition metal-based 2D materials. For instance, layered transition metal borides (MBenes) \( ^{40, 50} \) , sulfides (MSenes) \( ^{39, 51} \) , and phosphides (MPenes) \( ^{52, 53} \)  have been investigated experimentally and computationally. However, most prior studies primarily focused on the 1T and 2H monolayer phases derived from TMD research. Future studies of these 2D materials can expand to include other bulk-derived 2D phases, which remain largely unexplored. The panoramic view of 2D phases lays a solid foundation for understanding phase stability and their structural relationships across a broad range of 2D materials.

## Methods

## Density functional theory (DFT) calculations

All density functional theory (DFT) calculations were conducted using the Vienna ab initio Simulation Package (VASP, version 5.4.4) \( ^{54-56} \)  and the projector-augmented wave (PAW) method \( ^{57, 58} \) . The PBE-D2 functional \( ^{59} \)  with vdW correction was adopted for the structural optimizations of all MXene phases, where all atoms were relaxed until the Hellmann-Feynman forces were smaller than  \( 10^{-2} \)  eV/ \( \mathring{A} \) . Following the structural optimizations, we performed static
 

calculations to calculate the charge density and electronic band structures using the semi-local Perdew-Burke-Ernzerhof (PBE) exchange-correlation functional \( ^{60} \) . The lattice parameters along all directions were fully optimized for the bulk and MAX phases, and only Al-containing MAX phases are considered in this study. However, in the case of 2D materials, the lattice parameters were only allowed to relax along the x- and y-directions (parallel to the 2D materials). Meanwhile, the lattice parameter along the z direction (perpendicular to the 2D materials) was fixed at 20 Å to avoid interactions from adjacent periodic boundaries for all kinds of calculations. According to the convergence test, the Brillouin-zone integrations were performed using a  \( \Gamma \) -centered 14×14×1 k-point grid for all MXene and MAX phases and a 10×10×10 grid for all cubic unit cells. The kinetic energy cutoff for plane waves was set to 700 eV, the convergence criterion for electronic self-consistency was set to  \( 10^{-6} \)  eV, and VASP's “accurate” precision setting was adopted to avoid wrap-around errors. Spin polarization was considered for all DFT calculations due to the magnetization observed in some MXenes. All crystal structures were visualized by VESTA software \( ^{61} \) .

## Phonon calculations

Based on the DFT-optimized structures, we calculated the phonon spectra and vibrational density of states (DOS) for all MXenes using the Phonopy code \( ^{62,63} \) . The density functional theory perturbation theory (DFPT) method was adopted to calculate the force constants. Here, the energy cutoff, energy convergence, and force convergence were the same as those of structural relaxations. We tested the  \( 1\times1\times1 \) ,  \( 2\times2\times1 \) , and  \( 3\times3\times1 \)  supercells of MXene phases to eliminate the imaginary phonon frequencies. We found that  \( 3\times3\times1 \)  supercell is the sufficient to achieve clean phonon spectra; we, therefore, adopted this configuration for all phonon calculations. The phonon spectra were sampled in the reciprocal space using primitive-based high symmetry k-points  \( \Gamma(0,0,0) \) , K(1/3, 1/3, 0), and M(0.5, 0, 0).

## Author contributions

C.H. and J.H. initiated this study and supervised all aspects of this work. C.H. and J.H. performed initial DFT calculations, and N.O. and O.C. performed additional DFT calculations. T.D., B.S., P.K., and P.G. provided detailed feedback on the simulation method. All authors wrote the manuscript together and contributed to the revision of this manuscript.

## Acknowledgments

N.O., O.C., and C.H. acknowledge the support of DOE Award DE-SC0025431. This research used resources of the National Energy Research Scientific Computing Center (NERSC), a DOE Office of Science User Facility supported by the Office of Science of the U.S. Department of Energy under Contract No. DE-AC02-05CH11231 using NERSC award BES-ERCAP0031213. A portion of the calculations used the resources of the Compute and Data Environment for Science (CADES) at ORNL and of the NERSC, which are supported by the Office of Science of the U.S. DOE under contract nos. DE-AC05-00OR22750 and DE-AC02-05CH11231, respectively. Some work was performed at the Center for Nanophase Materials Sciences, a U.S. DOE Office of Science User Facility operated at Oak Ridge National Laboratory.
 

## Competing interests

The authors declare no competing interests.

## Additional information

Supplementary information: The authors prepared 16 Suppl. Tables and 30 Suppl. Figs. in the Supplementary Information.

## Reference

1. Gogotsi, Y.; Anasori, B., The Rise of MXenes. ACS Nano 2019, 13 (8), 8491-8494.

2. Anasori, B.; Lukatskaya, M. R.; Gogotsi, Y., 2D metal carbides and nitrides (MXenes) for energy storage. Nature Reviews Materials 2017, 2 (2), 16098.

3. Naguib, M.; Mashtalir, O.; Carle, J.; Presser, V.; Lu, J.; Hultman, L.; Gogotsi, Y.; Barsoum, M. W., Two-Dimensional Transition Metal Carbides. ACS Nano 2012, 6 (2), 1322-1331.

4. Naguib, M.; Kurtoglu, M.; Presser, V.; Lu, J.; Niu, J.; Heon, M.; Hultman, L.; Gogotsi, Y.; Barsoum, M. W., Two-Dimensional Nanocrystals Produced by Exfoliation of  \( Ti_{3}AlC_{2} \) . Advanced Materials 2011, 23 (37), 4248-4253.

5. Nemani, S. K.; Torkamanzadeh, M.; Wyatt, B. C.; Presser, V.; Anasori, B., Functional two-dimensional high-entropy materials. Communications Materials 2023, 4 (1), 16.

6. Kamysbayev, V.; Filatov, A. S.; Hu, H.; Rui, X.; Lagunas, F.; Wang, D.; Klie, R. F.; Talapin, D. V., Covalent surface modifications and superconductivity of two-dimensional metal carbide MXenes. Science 2020, 369 (6506), 979-983.

7. Champagne, A.; Charlier, J.-C., Physical properties of 2D MXenes: from a theoretical perspective. Journal of Physics: Materials 2021, 3 (3), 032006.

8. Khan, K.; Tareen, A. K.; Iqbal, M.; Hussain, I.; Mahmood, A.; Khan, U.; Khan, M. F.; Zhang, H.; Xie, Z., Recent advances in MXenes: a future of nanotechnologies. Journal of Materials Chemistry A 2023, 11 (37), 19764-19811.

9. Rems, E.; Hu, Y.-J.; Gogotsi, Y.; Dominko, R., Pivotal Role of Surface Terminations in MXene Thermodynamic Stability. Chemistry of Materials 2024, 36 (20), 10295-10306.

10. Qian Fang, L. W., Kai Chang, Hongxin Yang, Pu Yan, Kecheng Cao, Mian Li, Zhifang Chai, Qing Huang, Semiconducting and Ferromagnetic Lanthanide MXenes Derived from Carbon Intercalated Two-dimensional Halides. arXiv:2410.18337 2024.

11. Kumar Katiyar, N.; Biswas, K.; Yeh, J.-W.; Sharma, S.; Sekhar Tiwary, C., A perspective on the catalysis using the high entropy alloys. Nano Energy 2021, 88, 106261.

12. Gu, J.; Zhao, Z.; Huang, J.; Sumpter, B. G.; Chen, Z., MX Anti-MXenes from Non-van der Waals Bulks for Electrochemical Applications: The Merit of Metallicity and Active Basal Plane. ACS Nano 2021, 15 (4), 6233-6242.

13. Pang, J.; Mendes, R. G.; Bachmatiuk, A.; Zhao, L.; Ta, H. Q.; Gemming, T.; Liu, H.; Liu, Z.; Rummeli, M. H., Applications of 2D MXenes in energy conversion and storage systems. Chemical Society Reviews 2019, 48 (1), 72-133.

14. Gao, Q.; Sun, W.; Ilani-Kashkoul, P.; Tselev, A.; Kent, P. R. C.; Kabengi, N.; Naguib, M.; Alhabeb, M.; Tsai, W.-Y.; Baddorf, A. P.; Huang, J.; Jesse, S.; Gogotsi, Y.; Balke, N., Tracking ion intercalation into layered Ti3C2 MXene films across length scales. Energy & Environmental Science 2020, 13 (8), 2549-2558.

15. Han, M.; Shuck, C. E.; Singh, A.; Yang, Y.; Foucher, A. C.; Goad, A.; McBride, B.; May, S. J.;
 

Shenoy, V. B.; Stach, E. A.; Gogotsi, Y., Efficient microwave absorption with  \( V_{n+1}C_{n}T_{x} \)  MXenes. Cell Reports Physical Science 2022, 3 (10), 101073.

16. Wei, Y.; Zhang, P.; Soomro, R. A.; Zhu, Q.; Xu, B., Advances in the Synthesis of 2D MXenes. Advanced Materials 2021, 33 (39), 2103148.

17. Meshkian, R.; Näslund, L.-Å.; Halim, J.; Lu, J.; Barsoum, M. W.; Rosen, J., Synthesis of two-dimensional molybdenum carbide,  \( Mo_{2}C \) , from the gallium based atomic laminate  \( Mo_{2}Ga_{2}C \) . Scripta Materialia 2015, 108, 147-150.

18. Zhou, H.; Chen, Z.; Kountoupi, E.; Tsoukalou, A.; Abdala, P. M.; Florian, P.; Fedorov, A.; Müller, C. R., Two-dimensional molybdenum carbide 2D-Mo2C as a superior catalyst for  \( CO_{2} \)  hydrogenation. Nature Communications 2021, 12 (1), 5510.

19. Naguib, M.; Halim, J.; Lu, J.; Cook, K. M.; Hultman, L.; Gogotsi, Y.; Barsoum, M. W., New Two-Dimensional Niobium and Vanadium Carbides as Promising Materials for Li-Ion Batteries. Journal of the American Chemical Society 2013, 135 (43), 15966-15969.

20. Naguib, M.; Unocic, R. R.; Armstrong, B. L.; Nanda, J., Large-scale delamination of multi-layers transition metal carbides and carbonitrides “MXenes”. Dalton Transactions 2015, 44 (20), 9353-9358.

21. Montazeri, K.; Badr, H.; Ngo, K.; Sudhakar, K.; Elmelegy, T.; Uzarski, J.; Natu, V.; Barsoum, M. W., Delamination of MXene Flakes Using Simple Inorganic Bases. The Journal of Physical Chemistry C 2023, 127 (21), 10391-10397.

22. VahidMohammadi, A.; Kayali, E.; Orang, J.; Beidaghi, M., Techniques for MXene Delamination into Single-Layer Flakes. In 2D Metal Carbides and Nitrides (MXenes): Structure, Properties and Applications, Anasori, B.; Gogotsi, Y., Eds. Springer International Publishing: Cham, 2019; pp 177-195.

23. Li, X.; Xie, X.; Gonzalez-Julian, J.; Malzbender, J.; Yang, R., Mechanical and oxidation behavior of textured Ti2AlC and Ti3AlC2 MAX phase materials. Journal of the European Ceramic Society 2020, 40 (15), 5258-5271.

24. Li, Z.; Yu, L.; Milligan, C.; Ma, T.; Zhou, L.; Cui, Y.; Qi, Z.; Libretto, N.; Xu, B.; Luo, J.; Shi, E.; Wu, Z.; Xin, H.; Delgass, W. N.; Miller, J. T.; Wu, Y., Two-dimensional transition metal carbides as supports for tuning the chemistry of catalytic nanoparticles. Nature Communications 2018, 9 (1), 5258.

25. Lei, J.; Kutana, A.; Yakobson, B. I., Predicting stable phase monolayer  \( Mo_{2}C \)  (MXene), a superconductor with chemically-tunable critical temperature. Journal of Materials Chemistry C 2017, 5 (14), 3438-3444.

26. Chen, C.; Ji, X.; Xu, K.; Zhang, B.; Miao, L.; Jiang, J., Prediction of T- and H-Phase Two-Dimensional Transition-Metal Carbides/Nitrides and Their Semiconducting–Metallic Phase Transition. ChemPhysChem 2017, 18 (14), 1897-1902.

27. Yin, J.; Wu, B.; Wang, Y.; Li, Z.; Yao, Y.; Jiang, Y.; Ding, Y.; Xu, F.; Zhang, P., Novel elastic, lattice dynamics and thermodynamic properties of metallic single-layer transition metal phosphides: 2H-M2P ( \( Mo_{2}P \) ,  \( W_{2}P \) , Nb \( _{2}P \)  and Ta \( _{2}P \) ). Journal of Physics: Condensed Matter 2018, 30 (13), 135701.

28. Jin, W.; Wu, S.; Wang, Z., Structural, electronic and mechanical properties of two-dimensional Janus transition metal carbides and nitrides. Physica E: Low-dimensional Systems and Nanostructures 2018, 103, 307-313.

29. Hu, T.; Hu, M.; Gao, B.; Li, W.; Wang, X., Screening Surface Structure of MXenes by High-Throughput Computation and Vibrational Spectroscopic Confirmation. The Journal of Physical Chemistry C 2018, 122 (32), 18501-18509.

30. Akgenc, B., New predicted two-dimensional MXenes and their structural, electronic and lattice dynamical properties. Solid State Communications 2019, 303-304, 113739.

31. AKGENC, B., Two-dimensional Ti2C monolayer (MXene): surface functionalization, induced metal,
 

semiconductor transition. Turkish Journal of Physics 2019, 43 (5).

32. Akgenc, B.; Mogulkoc, A.; Durgun, E., Phase-dependent electronic and magnetic properties of  \( Ti_{2}C \)  monolayers. Journal of Applied Physics 2020, 127 (8), 084302.

33. Lim, K. R. G.; Handoko, A. D.; Johnson, L. R.; Meng, X.; Lin, M.; Subramanian, G. S.; Anasori, B.; Gogotsi, Y.; Vojvodic, A.; Seh, Z. W., 2H- \( MoS_{2} \)  on  \( Mo_{2}CT_{x} \)  MXene Nanohybrid for Efficient and Durable Electrocatalytic Hydrogen Evolution. ACS Nano 2020, 14 (11), 16140-16155.

34. Schultz, T.; Frey, N. C.; Hantanasirisakul, K.; Park, S.; May, S. J.; Shenoy, V. B.; Gogotsi, Y.; Koch, N., Surface Termination Dependent Work Function and Electronic Properties of  \( Ti_{3}C_{2}T_{x} \)  MXene. Chemistry of Materials 2019, 31 (17), 6590-6597.

35. Bera, S.; Kumar, H., Phase Stability of MXenes: Understanding the Role of Coordination Symmetries, Transition Metals, and Surface Terminations. The Journal of Physical Chemistry C 2023, 127 (42), 20734-20741.

36. Kotmool, K.; Kaewmaraya, T.; Hussain, T.; Ahuja, R.; Luo, W.; Bovornratanaraks, T., Biaxial stress and functional groups (T = O, F, and Cl) tuning the structural, mechanical, and electronic properties of monolayer molybdenum carbide. Physical Chemistry Chemical Physics 2022, 24 (29), 17862-17869.

37. Han, G. H.; Duong, D. L.; Keum, D. H.; Yun, S. J.; Lee, Y. H., van der Waals Metallic Transition Metal Dichalcogenides. Chemical Reviews 2018, 118 (13), 6297-6336.

38. Wang, J.; Bai, L.; Yao, C.; Niu, L., A DFT computational prediction of 2H phase  \( W_{2}C \)  monolayer and the effect of O functional groups. Physics Letters A 2022, 424, 127842.

39. Shu-Xiang Qiao, Y.-L. H., Na Jiao, Meng-Meng Zheng, Hong-Yan Lu, Ping Zhang, MSene: A new large family of two-dimensional transition metal sulfide with MXene structure. arXiv:2405.03928 2024.

40. Shukla, A.; Sharma, G.; Krishnamurty, S., Functionalized  \( Mo_{2}Bx_{2} \)  (X = H, OH, O) MBenes as a promising sensor, capturer and storage material for environmentally toxic gases: A case study of 1T and 2H phase. Applied Surface Science 2023, 615, 156299.

41. Hu, C.; Huang, J.; Sumpter, B. G.; Meletis, E.; Dumitrică, T., Ab Initio Predictions of Hexagonal  \( \mathrm{Zr(B,C,N)} \)  Polymorphs for Coherent Interface Design. The Journal of Physical Chemistry C 2017, 121 (46), 26007-26018.

42. Hu, C.; Huang, J.; Sumpter, B. G.; Meletis, E.; Dumitrică, T., Ab Initio Predictions of Strong Interfaces in Transition-Metal Carbides and Nitrides for Superhard Nanocomposite Coating Applications. ACS Applied Nano Materials 2018, 1 (5), 2029-2035.

43. Onodera, A.; Mimasaka, M.; Sakamoto, I.; Okumura, J.; Sakamoto, K.; Uehara, S.; Takemura, K.; Shimomura, O.; Ohtani, T.; Fujii, Y., Structural and electrical properties of NiAs-type compounds under pressure. Journal of Physics and Chemistry of Solids 1999, 60 (2), 167-179.

44. Kurlov, A. S.; Gusev, A. I., Tungsten carbides and W-C phase diagram. Inorganic Materials 2006, 42 (2), 121-127.

45. Wyatt, B. C.; Nemani, S. K.; Desai, K.; Kaur, H.; Zhang, B.; Anasori, B., High-temperature stability and phase transformations of titanium carbide  \( \left(\mathrm{Ti}_{3}\mathrm{C}_{2}\mathrm{T}_{x}\right) \)  MXene. Journal of Physics: Condensed Matter 2021, 33(22), 224002.

46. Sang, X.; Xie, Y.; Yilmaz, D. E.; Lotfi, R.; Alhabeb, M.; Ostadhossein, A.; Anasori, B.; Sun, W.; Li, X.; Xiao, K.; Kent, P. R. C.; van Duin, A. C. T.; Gogotsi, Y.; Unocic, R. R., In situ atomistic insight into the growth mechanisms of single layer 2D transition metal carbides. Nature Communications 2018, 9(1), 2266.

47. Seredych, M.; Shuck, C. E.; Pinto, D.; Alhabeb, M.; Precetti, E.; Deysher, G.; Anasori, B.; Kurra, N.; Gogotsi, Y., High-Temperature Behavior and Surface Chemistry of Carbide MXenes Studied by Thermal Analysis. Chemistry of Materials 2019, 31 (9), 3324-3332.
 

48. Duerloo, K.-A. N.; Li, Y.; Reed, E. J., Structural phase transitions in two-dimensional Mo- and W-dichalcogenide monolayers. Nature Communications 2014, 5 (1), 4214.

49. Nikolaevsky, M.; Friedman, R.; Dahlqvist, M.; Hornik, M.; Sterer, E.; Barsoum, M. W.; Rosen, J.; Melchior, A.; Caspi, E. a. N., Possible monoclinic distortion of  \( Mo_{2}GaC \)  under high pressure. Journal of Applied Physics 2020, 127 (14), 145103.

50. Xu, T.; Wang, Y.; Xiong, Z.; Wang, Y.; Zhou, Y.; Li, X., A Rising 2D Star: Novel MBenes with Excellent Performance in Energy Conversion and Storage. Nano-Micro Letters 2022, 15 (1), 6.

51. Wang, M.; Zhang, L.; He, Y.; Zhu, H., Recent advances in transition-metal-sulfide-based bifunctional electrocatalysts for overall water splitting. Journal of Materials Chemistry A 2021, 9 (9), 5320-5363.

52. Du, H.; Kong, R.-M.; Guo, X.; Qu, F.; Li, J., Recent progress in transition metal phosphides with enhanced electrocatalysis for hydrogen evolution. Nanoscale 2018, 10 (46), 21617-21624.

53. Shi, Y.; Zhang, B., Recent advances in transition metal phosphide nanomaterials: synthesis and applications in hydrogen evolution reaction. Chemical Society Reviews 2016, 45 (6), 1529-1541.

54. Kresse, G.; Hafner, J., Ab initio molecular dynamics for liquid metals. Physical Review B 1993, 47 (1), 558-561.

55. Kresse, G.; Furthmüller, J., Efficiency of ab-initio total energy calculations for metals and semiconductors using a plane-wave basis set. Computational Materials Science 1996, 6 (1), 15-50.

56. Kresse, G.; Furthmüller, J., Efficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set. Physical Review B 1996, 54 (16), 11169-11186.

57. Blöchl, P. E., Projector augmented-wave method. Physical Review B 1994, 50 (24), 17953-17979.

58. Kresse, G.; Joubert, D., From ultrasoft pseudopotentials to the projector augmented-wave method. Physical Review B 1999, 59 (3), 1758-1775.

59. Grimme, S., Semiempirical GGA-type density functional constructed with a long-range dispersion correction. Journal of Computational Chemistry 2006, 27 (15), 1787-1799.

60. Perdew, J. P.; Burke, K.; Ernzerhof, M., Generalized Gradient Approximation Made Simple. Physical Review Letters 1996, 77 (18), 3865-3868.

61. Izumi, K. M. a. F., VESTA 3 for three-dimensional visualization of crystal, volumetric and morphology data. J. Appl. Cryst. 2011, 44 (1272-1276).

62. Togo, A.; Chaput, L.; Tadano, T.; Tanaka, I., Implementation strategies in phonopy and phono3py. Journal of Physics: Condensed Matter 2023, 35 (35), 353001.

63. Togo, A., First-principles Phonon Calculations with Phonopy and Phono3py. Journal of the Physical Society of Japan 2022, 92 (1), 012001.
 
![](./images/1092748071881670702_1.jpg)

Fig. 1. A panoramic view of 2D MXene structures in transition metals carbides (TMCs) or nitrides (TMNs). a Schematic diagram of synthesizing the MXene structures from their hierarchical precursors, including the intermediate MAX phases and their parent bulk phases. Each TMC or TMN can have four types of bulk phases, and their crystal structures and associated top views are illustrated in panel b. These structures include one face-center-cubic (FCC) crystal structure (denoted as B1), two NiAs-type hexagonal structures (denoted as HX1a and HX1b), and one WC-type hexagonal crystal structure (denoted as HX2). The coordination number sequence of M-X (M = transition metals, X = C or N) was labeled for each structure. The octahedral and prismatic coordination were labeled as O and P, and the yellow and pink polyhedral, respectively, represent the coordination of M and X elements. c Crystal structures and associated coordination sequence (M-X-M) of four M₂X-type MXenes derived from each bulk phase. d Crystal structures and associated coordination sequence (M-X-M-M) of eight different M₃X₂-based MXenes derived from each bulk phase. e Crystal structures and associated coordination sequence (M-X-M-X-M-M) of eight different M₄X₃-based MXenes derived from each bulk phase. The B1-derived MXenes are commonly reported MXene phases observed in experiments. Based on the additional hexagonal bulk phases, we can derive and expand the candidates of the 2D MXenes family to 20 different structures. The symbol ’ denotes the coordination of the outermost layer of M or X.
 

Table 1. DFT-calculated phase stability and coordination environment for TiC-based bulk materials, MAX phases, and MXene phases. The thinnest MAX phase  \( \left(\mathrm{Ti}_{2}\mathrm{CAl}\right) \)  is derived from four bulk structures, while thicker MAX phases  \( \left(\mathrm{Ti}_{3}\mathrm{C}_{2}\mathrm{Al}\right) \)  exhibit eight derived phases, separated into two major groups (1 and 2). The 2D MXenes are tabulated similarly to MAX phases, and only F-terminated MXenes are summarized in this table. The order of phase stability is based on the ranking of DFT-calculated ground-state energies. The most stable coordination is listed for each group.

<table><tr><td>Phase</td><td>Materials system</td><td>Coordination</td><td>Order of phase stability</td><td>Most stable coordination</td></tr><tr><td>Bulk</td><td>TiC</td><td>Ti-C</td><td>B1 &lt; HX1a &lt; HXl1b &lt; HX2</td><td>O-O</td></tr><tr><td></td><td>Ti2CAl</td><td>Ti-C-Ti</td><td>T-1 &lt; T-2 &lt; H-1 &lt; H-2</td><td>O’-O-O’</td></tr><tr><td></td><td>Ti3C2Al-1</td><td>Ti-C-Ti-C-Ti</td><td>T-1 &lt; H1a-1 &lt; HClb-1 &lt; HD-1</td><td>O’-O-O-O-O’</td></tr><tr><td>MAX</td><td>Ti3C2Al-2</td><td>Ti-C-Ti-C-Ti</td><td>H1a-2 &lt; T-2 &lt; HClb-2 &lt; HD-2</td><td>O’-O-P-O-O’</td></tr><tr><td></td><td>Ti4C3Al-1</td><td>Ti-C-Ti-C-Ti-C-TTi</td><td>T-1 &lt; H1a-1 &lt; HClb-1 &lt; HD-1</td><td>O’-O-O-O-O-O-O’</td></tr><tr><td></td><td>Ti4C3Al-2</td><td>Ti-C-Ti-C-Ti-C-TTi</td><td>T-2 &lt; H1a-2 &lt; HClb-2 &lt; HD-2</td><td>P’-O-O-O-O-O-P’</td></tr><tr><td></td><td>Ti2CF2</td><td>Ti-C-Ti</td><td>T-1 &lt; T-2 &lt; H-1 &lt; H-2</td><td>O’-O-O’</td></tr><tr><td></td><td>Ti3CF2-1</td><td>Ti-C-Ti-C-Ti</td><td>T-1 &lt; H1a-1 &lt; HClb-1 &lt; HD-1</td><td>O’-O-O-O-O’</td></tr><tr><td>MXene</td><td>Ti3CF2-2</td><td>Ti-C-Ti-C-Ti</td><td>H1a-2 &lt; T-1 &lt; HClb-2 &lt; HD-2</td><td>O’-O-P-O-O’</td></tr><tr><td></td><td>Ti4CF2-1</td><td>Ti-C-Ti-C-Ti-C-TTi</td><td>T-1 &lt; T-2 &lt; H-1 &lt; H-2</td><td>O’-O-O-O-O-O-O’</td></tr><tr><td></td><td>Ti4CF2-2</td><td>Ti-C-Ti-C-Ti-C-TTi</td><td>H1a-2 &lt; T-1 &lt; HClb-2 &lt; HD-2</td><td>O’-O-P-O-P-O-O’</td></tr></table>
 

Table 2. DFT-calculated phase stability and coordination environment for MoC-based bulk materials, MAX phases, and MXene phases. The thinnest MAX phase  \( \left(\mathrm{Mo}_{2}\mathrm{CAl}\right) \)  is derived from four bulk structures, while thicker MAX phases  \( \left(\mathrm{Mo}_{3}\mathrm{C}_{2}\mathrm{Al}\right) \)  and  \( \mathrm{Mo}_{4}\mathrm{C}_{3}\mathrm{Al} \)  exhibit eight derived phases, separated into two major groups (1 and 2). The 2D MXenes are tabulated similarly to MAX phases, and only F-terminated MXenes are summarized in this table. The order of phase stability is based on the ranking of DFT-calculated ground-state energies. The most stable coordination is listed for each group.

<table><tr><td>Phase</td><td>Materials system</td><td>Coordination</td><td>Order of phase stability</td><td>Most stable coordination</td></tr><tr><td rowspan="3">Bulk</td><td>MoC</td><td>Mo-C</td><td>HX2&lt;HX1a&lt;HX1b&lt;B1</td><td>P-P</td></tr><tr><td>Mo2CAI</td><td>Mo-C-Mo</td><td>T-1&lt;T-2&lt;H-1&lt;H-2</td><td>O’-O-O’</td></tr><tr><td>Mo3C2Al-1</td><td>Mo-C-Mo-C-Mo</td><td>H2-1&lt;H1b-1&lt;Hla-1&lt;T-1</td><td>P’-P-P-P-P’</td></tr><tr><td rowspan="3">MAX</td><td>Mo3C2Al-2</td><td>Mo-C-Mo-C-Mo</td><td>H2-2&lt;Hla-2&lt;H1b-2&lt;T-2</td><td>O’-P-P-P-O’</td></tr><tr><td>Mo4C3Al-1</td><td>Mo-C-Mo-C-Mo-C-Mc</td><td>H2-1&lt;Hla-1&lt;H1b-1&lt;T-1</td><td>P’-P-P-P-P-P-P’</td></tr><tr><td>Mo4C3Al-2</td><td>Mo-C-Mo-C-Mo-C-Mc</td><td>H2-2&lt;Hla-2&lt;H1b-2&lt;T-2</td><td>O’-P-P-P-P-P-O’</td></tr><tr><td rowspan="5">MXene</td><td>Mo2CF2</td><td>Mo-C-Mo</td><td>H-1&lt;H-2&lt;T-2&lt;T1</td><td>O’-P-O’</td></tr><tr><td>Mo3C2F2-1</td><td>Mo-C-Mo-C-Mo</td><td>H1b-1&lt;H2-1&lt;T-1&lt;Hla-1</td><td>O’-P-O-P-O’</td></tr><tr><td>Mo3C2F2-2</td><td>Mo-C-Mo-C-Mo</td><td>H2-2&lt;H1b-2&lt;T-2&lt;Hla-2</td><td>O’-P-P-P-O’</td></tr><tr><td>Mo4C3F2-1</td><td>Mo-C-Mo-C-Mo-C-Mc</td><td>H2-1&lt;H1b-1&lt;T-1&lt;Hla-1</td><td>P’-P-P-P-P-P-P’</td></tr><tr><td>Mo4C3F2-2</td><td>Mo-C-Mo-C-Mo-C-Mc</td><td>H2-2&lt;H1b-2&lt;T-2&lt;Hla-2</td><td>O’-P-P-P-P-P-O’</td></tr></table>
 
![](./images/1092748071881670702_2.jpg)

![](./images/1092748071881670702_3.jpg)

![](./images/1092748071881670702_4.jpg)

![](./images/1092748071881670702_5.jpg)

![](./images/1092748071881670702_6.jpg)

![](./images/1092748071881670702_7.jpg)

![](./images/1092748071881670702_8.jpg)

![](./images/1092748071881670702_9.jpg)

![](./images/1092748071881670702_10.jpg)

Fig. 2. Lattice-dynamical stability of 2D MXenes. a-c Percentage of lattice-dynamically stable 2D MXenes among all Mo- and Ti-based 2D MXenes with and without termination atoms for  \( M_{2}XT_{x} \) ,  \( M_{3}X_{2}T_{x} \) , and  \( M_{3}X_{2}T_{x} \) . Configurations with no imaginary frequencies or only minor ones are considered stable. d DFT-calculated phonon spectra and vibrational density of states (vDOS) of 2D hexagonal-derived  \( Ti_{2}C \)  MXenes without termination, and with F and O terminations. e-f Phonon spectra and vDOS of 2D H1a-derived  \( Ti_{3}C_{2} \)  and  \( Ti_{4}C_{3} \)  MXenes under the same termination conditions.
 
![](./images/1092748071881670702_11.jpg)

Fig. 3. Comprehensive search for MXene phases based on bulk phase stability. a Phase stability ordering of four bulk phases for all transitional metal carbides (TMC), ranked by DFT-calculated ground-state energies. Lower order suggests a more energetically stable phase. b Phase stability ordering of four bulk phases for all transitional metal nitrides (TMN). c-d Verification of phase stability of two representative 2D MXenes systems, Hf- and Re-based TMC and TMNs. e Chronological review of the existing MXene crystal structures reported by prior experiments and simulations. This study expands the family of 2D MXenes to 20 crystal structures based on the coordination environment, approximately doubling the number of MXenes reported so far.
 

## Supporting Information

## A Panoramic View of MXenes via a New Design Strategy

Noah Oyeniran \( ^{a} \) , Oyshee Chowdhury \( ^{a} \)  , Chongze Hu \( ^{a*} \) , Traian Dumitrica \( ^{b} \) , Panchapakesan Ganesh \( ^{c} \) , Jacek Jakowski \( ^{d} \) , Zhongfang Chen \( ^{e} \) , Raymond R. Unocic \( ^{f} \) , Michael Naguib \( ^{g} \) , Vincent Meunier \( ^{h} \) , Yury Gogotsi \( ^{i} \) , Paul R. C. Kent \( ^{d} \) , Bobby G. Sumpter \( ^{c} \) , Jingsong Huang \( ^{c*} \) 

 \( ^{a} \)  Department of Aerospace Engineering and Mechanics, The University of Alabama, Tuscaloosa, Alabama 35487, USA

 \( ^{b} \)  Department of Mechanical Engineering, University of Minnesota Twin Cities, Minneapolis, Minnesota 55455, USA

 \( ^{c} \)  Center of Nanophase Materials Sciences, Oak Ridge National Laboratory, Oak Ridge, Tennessee 37831, USA

 \( ^{d} \)  Computational Sciences and Engineering Division, Oak Ridge National Laboratory, Oak Ridge, Tennessee 37831, USA

 \( ^{e} \)  Department of Chemistry, University of Puerto Rico, Rio Piedras, San Juan, Puerto Rico 00931, USA

 \( ^{f} \)  Department of Materials Science and Engineering, North Carolina State University, Raleigh, North Carolina 27695, USA

 \( ^{8} \)  Department of Physics and Engineering Physics, Tulane University, New Orleans, Louisiana 70118, USA

 \( ^{h} \)  Department of Engineering Science and Mechanics, The Pennsylvania State University, University Park, Pennsylvania 16801, USA

 \( ^{i} \)  Department of Materials Science and Engineering, and A.J. Drexel Nanomaterials Institute, Drexel University, Philadelphia, Pennsylvania 19104, USA

 \( ^{*} \) Corresponding authors

Email address: hucz@ua.edu (Chongze Hu) and huangj3@ornl.gov (Jingsong Huang)
 

## Table of Contents

## Supplementary Tables:

Table S1. Correlation of DFT-calculated energetic stability between TiN-based bulk materials and associated MAX and MXene phases.

Table S2. Correlation of DFT-calculated energetic stability between MoN-based bulk materials and associated MAX and MXene phases.

Table S3. DFT-calculated energy difference and lattice constants among all non-terminated TiC-based 2D MXenes using PBE and PBE-D2 functionals.

Table S4. DFT-calculated energy difference and lattice constants among all oxygen-terminated TiC-based 2D MXenes using PBE and PBE-D2 functionals.

Table S5. DFT-calculated energy difference and lattice constants among all fluoride-terminated TiC-based 2D MXenes using PBE and PBE-D2 functionals.

Table S6. DFT-calculated energy difference and lattice constants among all non-terminated MoC-based 2D MXenes using PBE and PBE-D2 functionals.

Table S7. DFT-calculated energy difference and lattice constants among all oxygen-terminated MoC-based 2D MXenes using PBE and PBE-D2 functionals.

Table S8. DFT-calculated energy difference and lattice constants among all fluoride-terminated MoC-based 2D MXenes using PBE and PBE-D2 functionals.

Table S9. DFT-calculated energy difference and lattice constants among all non-terminated TiN-based 2D MXenes using PBE and PBE-D2 functionals.

Table S10. DFT-calculated energy difference and lattice constants among all oxygen-terminated TiN-based 2D MXenes using PBE and PBE-D2 functionals.

Table S11. DFT-calculated energy difference and lattice constants among all fluoride-terminated TiN-based 2D MXenes using PBE and PBE-D2 functionals.

Table S12. DFT-calculated energy difference and lattice constants among all non-terminated MoN-based 2D MXenes using PBE and PBE-D2 functionals.

Table S13. DFT-calculated energy difference and lattice constants among all oxygen-terminated MoN-based 2D MXenes using PBE and PBE-D2 functionals.

Table S14. DFT-calculated energy difference and lattice constants among all fluoride-terminated MoN-based 2D MXenes using PBE and PBE-D2 functionals.

Table S15. DFT-calculated energy difference and lattice constants among all fluoride-terminated HfC- and HfN-based 2D MXenes using PBE-D2 functional.

Table S16. DFT-calculated energy difference and lattice constants among all fluoride-terminated ReC- and ReN-based 2D MXenes using PBE-D2 functional.

## Supplementary Figures:

Figs. S1–5. Phonon spectra and vibrational DOSs of Mo-based MXenes without termination atoms.

Figs. S6-10. Phonon spectra and vibrational DOSs of Ti-based MXenes without termination atoms.

Figs. S11-15. Phonon spectra and vibrational DOSs of Mo-based MXenes terminated by fluorine (F) atoms.

Figs. S16-20. Phonon spectra and vibrational DOSs of Mo-based MXenes terminated by oxygen (O) atoms.

Figs. S21-25. Phonon spectra and vibrational DOSs of Ti-based MXenes terminated by fluorine (F) atoms.

Figs. S26-30. Phonon spectra and vibrational DOSs of Ti-based MXenes terminated by oxygen (O) atoms.
 

Table S1. DFT-calculated phase stability and coordination environment for TiN-based bulk materials, MAX phases, and MXene phases. The thinnest MAX phase  \( \left(\mathrm{Ti}_{2}\mathrm{NAI}\right) \)  is derived from four bulk structures, while thicker MAX phases  \( \left(\mathrm{Ti}_{3}\mathrm{N}_{2}\mathrm{Al}\right) \)  and  \( \left(\mathrm{Ti}_{4}\mathrm{N}_{3}\mathrm{Al}\right) \)  exhibit eight derived phases, separated into two major groups (1 and 2). The 2D MXenes are tabulated similarly to MAX phases, and only F-terminated MXenes are summarized in this table. The order of phase stability is based on the ranking of DFT-calculated ground-state energies. The most stable coordination is listed for each group.

<table><tr><td>Phase</td><td>Materials system</td><td>Coordination</td><td>Order of phase stability</td><td>Most stable coordination</td></tr><tr><td rowspan="3">Bulk</td><td>TiN</td><td>Ti-N</td><td>B1&lt;HX1a&lt;HX1b&lt;HX2</td><td>O-O</td></tr><tr><td>Ti2NAI</td><td>Ti-N-Ti</td><td>T-1&lt;T-2&lt;H-1&lt;H-2</td><td>O&#x27;-O-O&#x27;</td></tr><tr><td>Ti3N2Al-1</td><td>Ti-N-Ti-N-Ti</td><td>T-1&lt;H1a-1&lt;H-1b-1&lt;H2-1</td><td>O&#x27;-O-O-O-O&#x27;</td></tr><tr><td rowspan="3">MAX</td><td>Ti3N2Al-2</td><td>Ti-N-Ti-N-Ti</td><td>T-2&lt;H1a-2&lt;H-1b-2&lt;H2-2</td><td>P&#x27;-O-O-O-P&#x27;</td></tr><tr><td>Ti4N3Al-1</td><td>Ti-N-Ti-N-Ti-N-T-i</td><td>T-1&lt;H1a-1&lt;H-1b-1&lt;H2-1</td><td>O&#x27;-O-O-O-O-O-O&#x27;</td></tr><tr><td>Ti4N3Al-2</td><td>Ti-N-Ti-N-Ti-N-T-i</td><td>T-2&lt;H1a-2&lt;H-1b-2&lt;H2-2</td><td>P&#x27;-O-O-O-O-O-P&#x27;</td></tr><tr><td rowspan="3"></td><td>Ti2NF2</td><td>Ti-N-Ti</td><td>T-1&lt;T-2&lt;H-2&lt;H1</td><td>O&#x27;-O-O&#x27;</td></tr><tr><td>Ti3NF2-1</td><td>Ti-N-Ti-N-Ti</td><td>T-1&lt;H1a-1&lt;H2-1&lt;H-1b-1</td><td>O&#x27;-O-O-O-O&#x27;</td></tr><tr><td>Ti3NF2-2</td><td>Ti-N-Ti-N-Ti</td><td>T-2&lt;H1a-2&lt;H2-2&lt;H-1b-2</td><td>P&#x27;-O-O-O-P&#x27;</td></tr><tr><td rowspan="2">MXene</td><td>Ti4N3F2-1</td><td>Ti-N-Ti-N-Ti-N-T-i</td><td>T-1&lt;H1a-1&lt;H-1b-1&lt;H2-1</td><td>O&#x27;-O-O-O-O-O-O&#x27;</td></tr><tr><td>Ti4N3F2-2</td><td>Ti-N-Ti-N-Ti-N-T-i</td><td>T-2&lt;H1a-2&lt;H-1b-2&lt;H2-2</td><td>P&#x27;-O-O-O-O-O-P&#x27;</td></tr></table>
 

Table S2. DFT-calculated phase stability and coordination environment for MoN-based bulk materials, MAX phases, and MXene phases. The thinnest MAX phase  \( \left(\mathrm{Mo}_{2}\mathrm{NAI}\right) \)  is derived from four bulk structures, while thicker MAX phases  \( \left(\mathrm{Mo}_{3}\mathrm{N}_{2}\mathrm{Al}\right) \)  and  \( \mathrm{Mo}_{4}\mathrm{N}_{3}\mathrm{Al} \)  exhibit eight derived phases, separated into two major groups (1 and 2). The 2D MXenes are tabulated similarly to MAX phases, and only F-terminated MXenes are summarized in this table. The order of phase stability is based on the ranking of DFT-calculated ground-state energies. The most stable coordination is listed for each group.

<table><tr><td>Phase</td><td>Materials system</td><td>Coordination</td><td>Order of phase stability</td><td>Most stable coordination</td></tr><tr><td rowspan="3">Bulk</td><td>MoN</td><td>Mo-N</td><td>HX1b &lt; HX2 &lt; HX1a &lt; B1</td><td>O-P</td></tr><tr><td>Mo2NAI</td><td>Mo-N-Mo</td><td>H-1 &lt; H-2 &lt; T-2 &lt;T-1</td><td>O&#x27;-P-O&#x27;</td></tr><tr><td>Mo3N2Al-1</td><td>Mo-N-Mo-N-Mo</td><td>H1b-1 &lt; H2-1 &lt;H1a-1 &lt; T-1</td><td>O&#x27;-P-O-P-O&#x27;</td></tr><tr><td rowspan="3">MAX</td><td>Mo3N2Al-2</td><td>Mo-N-Mo-N-Mo</td><td>H1b-2 &lt; H2-2 &lt;H1a-2 &lt; T-2</td><td>P&#x27;-P-O-P-P&#x27;</td></tr><tr><td>Mo4N3Al-1</td><td>Mo-N-Mo-N-Mo-N-MO</td><td>H1b-1 &lt; H2-1 &lt;H1a-1 &lt; T-1</td><td>O&#x27;-P-O-P-O-P-O&#x27;</td></tr><tr><td>Mo4N3Al-2</td><td>Mo-N-Mo-N-Mo-N-MO</td><td>H1b-2 &lt; H2-2 &lt;H1a-2 &lt; T-2</td><td>P&#x27;-P-O-P-O-P-P&#x27;</td></tr><tr><td rowspan="3"></td><td>Mo2NF2</td><td>Mo-N-Mo</td><td>H-1 &lt; T-1 &lt; H-2 &lt; T-2</td><td>O&#x27;-P-O&#x27;</td></tr><tr><td>Mo3N2F2-1</td><td>Mo-N-Mo-N-Mo</td><td>H1b-1 &lt; H2-1 &lt; T-1 &lt;H1a-1</td><td>O&#x27;-P-O-P-O&#x27;</td></tr><tr><td>Mo3N2F2-2</td><td>Mo-N-Mo-N-Mo</td><td>H2-2 &lt; H1b-2 &lt;H1a-2 &lt; T-2</td><td>O&#x27;-P-P-P-O&#x27;</td></tr><tr><td rowspan="2">MXene</td><td>Mo4N3F2-1</td><td>Mo-N-Mo-N-Mo-N-MO</td><td>H1b-1 &lt; T-1 &lt; H2-1 &lt;H1a-1</td><td>O&#x27;-P-O-P-O-P-O&#x27;</td></tr><tr><td>Mo4N3F2-2</td><td>Mo-N-Mo-N-Mo-N-MO</td><td>H2-2 &lt; H1b-2 &lt;H1a-2 &lt; T-2</td><td>O&#x27;-P-P-P-P-P-O&#x27;</td></tr></table>
 

Table S3. DFT-calculated energy difference ( \( \Delta E \) ) and DFT-optimized lattice constants (a) of all non-terminated TiC-based 2D MXenes ( \( Ti_{n+1}C_{n} \) , where n = 1-3) using PBE functional and PBE-D2 with vdW corrections. The energy difference is determined by:  \( \Delta E = E_{MX} - \min(E_{MX}) \) , where  \( E_{MX} \)  is the ground state energy of each MXene structure and  \( \min(E_{MX}) \)  is the energy of the most stable MXene within the same group.

<table><tr><td colspan="5">Ti2C (no termination)</td></tr><tr><td></td><td>PBE-D2  \( \Delta E \)  (eV/atom)</td><td>PBE  \( \Delta E \)  (eV/atom)</td><td>PBE-D2  \( a \)  ( \( \textup{\AA} \) )</td><td>PBE  \( a \)  ( \( \textup{\AA} \) )</td></tr><tr><td>T-1</td><td>0.000</td><td>0.000</td><td>3.04</td><td>3.04</td></tr><tr><td>T-2</td><td>0.000</td><td>0.000</td><td>3.04</td><td>3.04</td></tr><tr><td>H-1</td><td>0.426</td><td>0.424</td><td>3.02</td><td>3.01</td></tr><tr><td>H-2</td><td>0.426</td><td>0.424</td><td>3.02</td><td>3.01</td></tr><tr><td colspan="5">Ti3C2 (no termination)</td></tr><tr><td></td><td>PBE-D2  \( \Delta E \)  (eV/atom)</td><td>PBE  \( \Delta E \)  (eV/atom)</td><td>PBE-D2  \( a \)  ( \( \textup{\AA} \) )</td><td>PBE  \( a \)  ( \( \textup{\AA} \) )</td></tr><tr><td>T-1</td><td>0.000</td><td>0.000</td><td>3.10</td><td>3.10</td></tr><tr><td>T-2</td><td>0.000</td><td>0.000</td><td>3.10</td><td>3.10</td></tr><tr><td>H1a-1</td><td>0.034</td><td>0.030</td><td>3.09</td><td>3.09</td></tr><tr><td>H1a-2</td><td>0.034</td><td>0.030</td><td>3.09</td><td>3.09</td></tr><tr><td>H1b-1</td><td>0.477</td><td>0.464</td><td>3.06</td><td>3.06</td></tr><tr><td>H1b-2</td><td>0.477</td><td>0.464</td><td>3.06</td><td>3.07</td></tr><tr><td>H2-1</td><td>0.521</td><td>0.505</td><td>3.06</td><td>3.07</td></tr><tr><td>H2-2</td><td>0.521</td><td>0.505</td><td>3.07</td><td>3.07</td></tr><tr><td colspan="5">Ti4C3 (no termination)</td></tr><tr><td></td><td>PBE-D2  \( \Delta E \)  (eV/atom)</td><td>PBE  \( \Delta E \)  (eV/atom)</td><td>PBE-D2  \( a \)  ( \( \textup{\AA} \) )</td><td>PBE  \( a \)  ( \( \textup{\AA} \) )</td></tr><tr><td>T-1</td><td>0.000</td><td>0.000</td><td>3.09</td><td>3.09</td></tr><tr><td>T-2</td><td>0.000</td><td>0.000</td><td>3.09</td><td>3.09</td></tr><tr><td>H1a-1</td><td>0.036</td><td>0.028</td><td>3.10</td><td>3.11</td></tr><tr><td>H1a-2</td><td>0.036</td><td>0.028</td><td>3.10</td><td>3.11</td></tr><tr><td>H1b-1</td><td>0.488</td><td>0.466</td><td>3.06</td><td>3.06</td></tr><tr><td>H1b-2</td><td>0.488</td><td>0.466</td><td>3.06</td><td>3.06</td></tr><tr><td>H2-1</td><td>0.555</td><td>0.529</td><td>3.07</td><td>3.08</td></tr><tr><td>H2-2</td><td>0.555</td><td>0.529</td><td>3.07</td><td>3.08</td></tr></table>
 

Table S4. DFT-calculated energy difference ( \( \Delta E \) ) and DFT-optimized lattice constants (a) of all oxygen-terminated TiC-based 2D MXenes ( \( Ti_{n+1}C_{n}O_{2} \) , where n = 1-3) using PBE functional and PBE-D2 with vdW corrections. The energy difference is determined by:  \( \Delta E = E_{MX} - \min(E_{MX}) \) , where  \( E_{MX} \)  is the ground state energy of each MXene structure and  \( \min(E_{MX}) \)  is the energy of the most stable MXene within the same group.

<table><tr><td colspan="5">Ti2CO2(oxygen termination)</td></tr><tr><td></td><td>PBE-D2 ΔE(eV/atom)</td><td>PBE ΔE(eV/ atom)</td><td>PBE-D2 a(Å)</td><td>PBE a(Å)</td></tr><tr><td>T-1</td><td>0.000</td><td>0.000</td><td>3.03</td><td>3.03</td></tr><tr><td>T-2</td><td>0.374</td><td>0.366</td><td>2.96</td><td>2.96</td></tr><tr><td>H-1</td><td>0.087</td><td>0.072</td><td>3.04</td><td>3.05</td></tr><tr><td>H-2</td><td>0.443</td><td>0.420</td><td>2.96</td><td>2.97</td></tr><tr><td colspan="5">Ti3C2O2(oxygen termination)</td></tr><tr><td></td><td>PBE-D2 ΔE(eV/atom)</td><td>PBE ΔE(eV/ atom)</td><td>PBE-D2 a(Å)</td><td>PBE a(Å)</td></tr><tr><td>T-1</td><td>0.000</td><td>0.000</td><td>3.04</td><td>3.04</td></tr><tr><td>T-2</td><td>0.219</td><td>0.213</td><td>3.01</td><td>3.02</td></tr><tr><td>H1a-1</td><td>0.298</td><td>0.290</td><td>3.15</td><td>3.15</td></tr><tr><td>H1a-2</td><td>0.091</td><td>0.087</td><td>3.03</td><td>3.04</td></tr><tr><td>H1b-1</td><td>0.186</td><td>0.165</td><td>3.04</td><td>3.05</td></tr><tr><td>H1b-2</td><td>0.411</td><td>0.384</td><td>3.02</td><td>3.02</td></tr><tr><td>H2-1</td><td>0.521</td><td>0.490</td><td>2.99</td><td>2.99</td></tr><tr><td>H2-2</td><td>0.288</td><td>0.263</td><td>3.04</td><td>3.04</td></tr><tr><td colspan="5">Ti4C3O2(oxygen termination)</td></tr><tr><td></td><td>PBE-D2 ΔE(eV/atom)</td><td>PBE ΔE(eV/ atom)</td><td>PBE-D2 a(Å)</td><td>PBE a(Å)</td></tr><tr><td>T-1</td><td>0</td><td>0.000</td><td>3.04</td><td>3.04</td></tr><tr><td>T-2</td><td>0.174</td><td>0.170</td><td>3.02</td><td>3.03</td></tr><tr><td>H1a-1</td><td>0.288</td><td>0.278</td><td>3.10</td><td>3.11</td></tr><tr><td>H1a-2</td><td>0.123</td><td>0.118</td><td>3.05</td><td>3.05</td></tr><tr><td>H1b-1</td><td>0.251</td><td>0.225</td><td>3.04</td><td>3.05</td></tr><tr><td>H1b-2</td><td>0.425</td><td>0.396</td><td>3.02</td><td>3.03</td></tr><tr><td>H2-1</td><td>0.571</td><td>0.536</td><td>3.00</td><td>3.00</td></tr><tr><td>H2-2</td><td>0.387</td><td>0.356</td><td>3.04</td><td>3.04</td></tr></table>
 

Table S5. DFT-calculated energy difference ( \( \Delta E \) ) and DFT-optimized lattice constants (a) of all fluoride-terminated TiC-based 2D MXenes ( \( Ti_{n+1}C_{n}F_{2} \) , where n = 1-3) using PBE functional and PBE-D2 with vdW corrections. The energy difference is determined by:  \( \Delta E = E_{MX} - \min(E_{MX}) \) , where  \( E_{MX} \)  is the ground state energy of each MXene structure and  \( \min(E_{MX}) \)  is the energy of the most stable MXene within the same group.

<table><tr><td colspan="5">Ti2CF2(fluoride termination)</td></tr><tr><td></td><td>PBE-D2 ΔE(eV/atom)</td><td>PBE ΔE(eV/ atom)</td><td>PBE-D2 a(Å)</td><td>PBE a(Å)</td></tr><tr><td>T-1</td><td>0.000</td><td>0.000</td><td>3.05</td><td>3.06</td></tr><tr><td>T-2</td><td>0.117</td><td>0.112</td><td>2.97</td><td>2.98</td></tr><tr><td>H-1</td><td>0.213</td><td>0.211</td><td>3.07</td><td>3.08</td></tr><tr><td>H-2</td><td>0.337</td><td>0.326</td><td>2.95</td><td>2.95</td></tr><tr><td colspan="5">Ti3C2F2(fluoride termination)</td></tr><tr><td></td><td>PBE-D2 ΔE(eV/atom)</td><td>PBE ΔE(eV/ atom)</td><td>PBE-D2 a(Å)</td><td>PBE a(Å)</td></tr><tr><td>T-1</td><td>0.000</td><td>0.000</td><td>3.07</td><td>3.08</td></tr><tr><td>T-2</td><td>0.110</td><td>0.106</td><td>3.02</td><td>3.02</td></tr><tr><td>H1a-1</td><td>0.145</td><td>0.138</td><td>3.01</td><td>3.02</td></tr><tr><td>H1a-2</td><td>0.021</td><td>0.018</td><td>3.07</td><td>3.07</td></tr><tr><td>H1b-1</td><td>0.293</td><td>0.280</td><td>3.06</td><td>3.06</td></tr><tr><td>H1b-2</td><td>0.386</td><td>0.368</td><td>3.00</td><td>3.00</td></tr><tr><td>H2-1</td><td>0.451</td><td>0.431</td><td>2.98</td><td>2.99</td></tr><tr><td>H2-2</td><td>0.332</td><td>0.317</td><td>3.06</td><td>3.07</td></tr><tr><td colspan="5">Ti4C3F2(fluoride termination)</td></tr><tr><td></td><td>PBE-D2 ΔE(eV/atom)</td><td>PBE ΔE(eV/ atom)</td><td>PBE-D2 a(Å)</td><td>PBE a(Å)</td></tr><tr><td>T-1</td><td>0.000</td><td>0.000</td><td>3.08</td><td>3.08</td></tr><tr><td>T-2</td><td>0.085</td><td>0.082</td><td>3.03</td><td>3.03</td></tr><tr><td>H1a-1</td><td>0.148</td><td>0.140</td><td>3.03</td><td>3.04</td></tr><tr><td>H1a-2</td><td>0.039</td><td>0.034</td><td>3.08</td><td>3.08</td></tr><tr><td>H1b-1</td><td>0.328</td><td>0.309</td><td>3.05</td><td>3.06</td></tr><tr><td>H1b-2</td><td>0.407</td><td>0.384</td><td>3.01</td><td>3.01</td></tr><tr><td>H2-1</td><td>0.502</td><td>0.476</td><td>3.00</td><td>3.00</td></tr><tr><td>H2-2</td><td>0.402</td><td>0.380</td><td>3.05</td><td>3.06</td></tr></table>
 

Table S6. DFT-calculated energy difference ( \( \Delta E \) ) and DFT-optimized lattice constants (a) of all non-terminated MoC-based 2D MXenes ( \( Mo_{n+1}C_{n} \) , where n = 1-3) using PBE functional and PBE-D2 with vdW corrections. The energy difference is determined by:  \( \Delta E = E_{\mathrm{MX}} - \min(E_{\mathrm{MX}}) \) , where  \( E_{MX} \)  is the ground state energy of each MXene structure and  \( \min(E_{\mathrm{MX}}) \)  is the energy of the most stable MXene within the same group.

<table><tr><td colspan="5">Mo2C (no termination)</td></tr><tr><td></td><td>PBE-D2  \( \Delta E \)  (eV/atom)</td><td>PBE  \( \Delta E \)  (eV/atom)</td><td>PBE-D2  \( a \)  ( \( \textup{\AA} \) )</td><td>PBE  \( a \)  ( \( \textup{\AA} \) )</td></tr><tr><td>T-1</td><td>0.088</td><td>0.065</td><td>2.90</td><td>3.00</td></tr><tr><td>T-2</td><td>0.088</td><td>0.065</td><td>2.90</td><td>3.00</td></tr><tr><td>H-1</td><td>0.000</td><td>0.000</td><td>2.84</td><td>2.85</td></tr><tr><td>H-2</td><td>0.000</td><td>0.000</td><td>2.84</td><td>2.85</td></tr><tr><td colspan="5">Mo3C2 (no termination)</td></tr><tr><td></td><td>PBE-D2  \( \Delta E \)  (eV/atom)</td><td>PBE  \( \Delta E \)  (eV/atom)</td><td>PBE-D2  \( a \)  ( \( \textup{\AA} \) )</td><td>PBE  \( a \)  ( \( \textup{\AA} \) )</td></tr><tr><td>T-1</td><td>0.076</td><td>0.069</td><td>3.01</td><td>3.02</td></tr><tr><td>T-2</td><td>0.076</td><td>0.069</td><td>3.01</td><td>3.02</td></tr><tr><td>H1a-1</td><td>0.070</td><td>0.071</td><td>2.90</td><td>2.92</td></tr><tr><td>H1a-2</td><td>0.070</td><td>0.072</td><td>2.90</td><td>2.92</td></tr><tr><td>H1b-1</td><td>0.044</td><td>0.043</td><td>2.85</td><td>2.87</td></tr><tr><td>H1b-2</td><td>0.044</td><td>0.043</td><td>2.85</td><td>2.87</td></tr><tr><td>H2-1</td><td>0.000</td><td>0.000</td><td>2.85</td><td>2.87</td></tr><tr><td>H2-2</td><td>0.000</td><td>0.000</td><td>2.85</td><td>2.87</td></tr><tr><td colspan="5">Mo4C3 (no termination)</td></tr><tr><td></td><td>PBE-D2  \( \Delta E \)  (eV/atom)</td><td>PBE  \( \Delta E \)  (eV/atom)</td><td>PBE-D2  \( a \)  ( \( \textup{\AA} \) )</td><td>PBE  \( a \)  ( \( \textup{\AA} \) )</td></tr><tr><td>T-1</td><td>0.126</td><td>0.125</td><td>3.07</td><td>3.08</td></tr><tr><td>T-2</td><td>0.126</td><td>0.125</td><td>3.08</td><td>3.08</td></tr><tr><td>H1a-1</td><td>0.481</td><td>0.083</td><td>2.91</td><td>2.92</td></tr><tr><td>H1a-2</td><td>0.074</td><td>0.083</td><td>2.91</td><td>2.92</td></tr><tr><td>H1b-1</td><td>0.076</td><td>0.074</td><td>2.87</td><td>2.88</td></tr><tr><td>H1b-2</td><td>0.076</td><td>0.074</td><td>2.87</td><td>2.88</td></tr><tr><td>H2-1</td><td>0.000</td><td>0.000</td><td>2.86</td><td>2.88</td></tr><tr><td>H2-2</td><td>0.000</td><td>0.000</td><td>2.86</td><td>2.88</td></tr></table>
 

Table S7. DFT-calculated energy difference ( \( \Delta E \) ) and DFT-optimized lattice constants (a) of all oxygen-terminated MoC-based 2D MXenes ( \( Mo_{n+1}C_{n}O_{2} \) , where n = 1-3) using PBE functional and PBE-D2 with vdW corrections. The energy difference is determined by:  \( \Delta E = E_{MX} - \min(E_{MX}) \) , where  \( E_{MX} \)  is the ground state energy of each MXene structure and  \( \min(E_{MX}) \)  is the energy of the most stable MXene within the same group.

<table><tr><td colspan="5">Mo2CO2(oxygen termination)</td></tr><tr><td></td><td>PBE-D2 ΔE(eV/atom)</td><td>PBE ΔE(eV/ atom)</td><td>PBE-D2 a(Å)</td><td>PBE a(Å)</td></tr><tr><td>T-1</td><td>0.331</td><td>0.279</td><td>2.95</td><td>3.09</td></tr><tr><td>T-2</td><td>0.068</td><td>0.075</td><td>2.87</td><td>2.88</td></tr><tr><td>H-1</td><td>0.194</td><td>0.194</td><td>2.88</td><td>2.90</td></tr><tr><td>H-2</td><td>0.000</td><td>0.000</td><td>2.86</td><td>2.87</td></tr><tr><td colspan="5">Mo3C2O2(oxygen termination)</td></tr><tr><td></td><td>PBE-D2 ΔE(eV/atom)</td><td>PBE ΔE(eV/ atom)</td><td>PBE-D2 a(Å)</td><td>PBE a(Å)</td></tr><tr><td>T-1</td><td>0.317</td><td>0.321</td><td>3.06</td><td>3.07</td></tr><tr><td>T-2</td><td>0.165</td><td>0.166</td><td>2.90</td><td>2.92</td></tr><tr><td>H1a-1</td><td>0.072</td><td>0.084</td><td>2.88</td><td>2.90</td></tr><tr><td>H1a-2</td><td>0.269</td><td>0.278</td><td>2.95</td><td>2.96</td></tr><tr><td>H1b-1</td><td>0.189</td><td>0.188</td><td>2.89</td><td>2.90</td></tr><tr><td>H1b-2</td><td>0.066</td><td>0.065</td><td>2.87</td><td>2.89</td></tr><tr><td>H2-1</td><td>0.000</td><td>0.000</td><td>2.87</td><td>2.89</td></tr><tr><td>H2-2</td><td>0.165</td><td>0.163</td><td>2.86</td><td>2.91</td></tr><tr><td colspan="5">Mo4C3O2(oxygen termination)</td></tr><tr><td></td><td>PBE-D2 ΔE(eV/atom)</td><td>PBE ΔE(eV/ atom)</td><td>PBE-D2 a(Å)</td><td>PBE a(Å)</td></tr><tr><td>T-1</td><td>0.304</td><td>0.314</td><td>3.04</td><td>3.05</td></tr><tr><td>T-2</td><td>0.192</td><td>0.076</td><td>2.97</td><td>2.98</td></tr><tr><td>H1a-1</td><td>0.075</td><td>0.090</td><td>2.90</td><td>2.91</td></tr><tr><td>H1a-2</td><td>0.228</td><td>0.240</td><td>2.95</td><td>2.96</td></tr><tr><td>H1b-1</td><td>0.177</td><td>0.176</td><td>2.89</td><td>2.91</td></tr><tr><td>H1b-2</td><td>0.079</td><td>0.078</td><td>2.88</td><td>2.89</td></tr><tr><td>H2-1</td><td>0.000</td><td>0.000</td><td>2.88</td><td>2.89</td></tr><tr><td>H2-2</td><td>0.129</td><td>0.127</td><td>2.90</td><td>2.91</td></tr></table>
 

Table S8. DFT-calculated energy difference ( \( \Delta E \) ) and DFT-optimized lattice constants (a) of all fluoride-terminated MoC-based 2D MXenes ( \( Mo_{n+1}C_{n}F_{2} \) , where n = 1-3) using PBE functional and PBE-D2 with vdW corrections. The energy difference is determined by:  \( \Delta E = E_{MX} - \min(E_{MX}) \) , where  \( E_{MX} \)  is the ground state energy of each MXene structure and  \( \min(E_{MX}) \)  is the energy of the most stable MXene within the same group.

<table><tr><td colspan="5">Mo2CF2(fluoride termination)</td></tr><tr><td></td><td>PBE-D2  \( \Delta E \)  (eV/atom)</td><td>PBE  \( \Delta E \)  (eV/atom)</td><td>PBE-D2  \( a \)  ( \( \textup{\AA} \) )</td><td>PBE  \( a \)  ( \( \textup{\AA} \) )</td></tr><tr><td>T-1</td><td>0.174</td><td>0.174</td><td>2.85</td><td>2.88</td></tr><tr><td>T-2</td><td>0.097</td><td>0.081</td><td>2.96</td><td>2.98</td></tr><tr><td>H-1</td><td>0.000</td><td>0.000</td><td>2.89</td><td>2.91</td></tr><tr><td>H-2</td><td>0.056</td><td>0.054</td><td>2.92</td><td>2.93</td></tr><tr><td colspan="5">Mo3C2F2(fluoride termination)</td></tr><tr><td></td><td>PBE-D2  \( \Delta E \)  (eV/atom)</td><td>PBE  \( \Delta E \)  (eV/atom)</td><td>PBE-D2  \( a \)  ( \( \textup{\AA} \) )</td><td>PBE  \( a \)  ( \( \textup{\AA} \) )</td></tr><tr><td>T-1</td><td>0.116</td><td>0.111</td><td>3.05</td><td>3.05</td></tr><tr><td>T-2</td><td>0.113</td><td>0.106</td><td>3.00</td><td>3.01</td></tr><tr><td>H1a-1</td><td>0.114</td><td>0.114</td><td>2.93</td><td>2.95</td></tr><tr><td>H1a-2</td><td>0.129</td><td>0.137</td><td>2.87</td><td>2.89</td></tr><tr><td>H1b-1</td><td>0.029</td><td>0.028</td><td>2.87</td><td>2.89</td></tr><tr><td>H1b-2</td><td>0.027</td><td>0.024</td><td>2.90</td><td>2.91</td></tr><tr><td>H2-1</td><td>0.043</td><td>0.040</td><td>2.88</td><td>2.90</td></tr><tr><td>H2-2</td><td>0.000</td><td>0.000</td><td>2.86</td><td>2.88</td></tr><tr><td colspan="5">Mo4C3F2(fluoride termination)</td></tr><tr><td></td><td>PBE-D2  \( \Delta E \)  (eV/atom)</td><td>PBE  \( \Delta E \)  (eV/atom)</td><td>PBE-D2  \( a \)  ( \( \textup{\AA} \) )</td><td>PBE  \( a \)  ( \( \textup{\AA} \) )</td></tr><tr><td>T-1</td><td>0.097</td><td>0.100</td><td>3.14</td><td>3.14</td></tr><tr><td>T-2</td><td>0.129</td><td>0.127</td><td>3.04</td><td>3.05</td></tr><tr><td>H1a-1</td><td>0.107</td><td>0.112</td><td>2.93</td><td>2.95</td></tr><tr><td>H1a-2</td><td>0.120</td><td>0.131</td><td>2.89</td><td>2.91</td></tr><tr><td>H1b-1</td><td>0.056</td><td>0.055</td><td>2.88</td><td>2.90</td></tr><tr><td>H1b-2</td><td>0.055</td><td>0.052</td><td>2.89</td><td>2.91</td></tr><tr><td>H2-1</td><td>0.027</td><td>0.024</td><td>2.89</td><td>2.91</td></tr><tr><td>H2-2</td><td>0.000</td><td>0.000</td><td>2.87</td><td>2.89</td></tr></table>
 

Table S9. DFT-calculated energy difference ( \( \Delta E \) ) and DFT-optimized lattice constants (a) of all non-terminated TiN-based 2D MXenes ( \( Ti_{n+1}N_{n} \) , where n=1-3) using PBE functional and PBE-D2 with vdW corrections. The energy difference is determined by:  \( \Delta E = E_{MX} - \min(E_{MX}) \) , where  \( E_{MX} \)  is the ground state energy of each MXene structure and  \( \min(E_{MX}) \)  is the energy of the most stable MXene within the same group.

<table><tr><td colspan="5">Ti2N (no termination)</td></tr><tr><td></td><td>PBE-D2  \( \Delta E \)  (eV/atom)</td><td>PBE  \( \Delta E \)  (eV/atom)</td><td>PBE-D2  \( a \)  ( \( \textup{\AA} \) )</td><td>PBE  \( a \)  ( \( \textup{\AA} \) )</td></tr><tr><td>T-1</td><td>0.000</td><td>0.000</td><td>2.99</td><td>2.98</td></tr><tr><td>T-2</td><td>0.000</td><td>0.000</td><td>2.99</td><td>2.98</td></tr><tr><td>H-1</td><td>0.318</td><td>0.316</td><td>2.89</td><td>2.89</td></tr><tr><td>H-2</td><td>0.318</td><td>0.316</td><td>2.89</td><td>2.88</td></tr><tr><td colspan="5">Ti3N2 (no termination)</td></tr><tr><td></td><td>PBE-D2  \( \Delta E \)  (eV/atom)</td><td>PBE  \( \Delta E \)  (eV/atom)</td><td>PBE-D2  \( a \)  ( \( \textup{\AA} \) )</td><td>PBE  \( a \)  ( \( \textup{\AA} \) )</td></tr><tr><td>T-1</td><td>0.000</td><td>0.000</td><td>3.04</td><td>3.04</td></tr><tr><td>T-2</td><td>0.000</td><td>0.000</td><td>3.04</td><td>3.04</td></tr><tr><td>H1a-1</td><td>0.045</td><td>0.042</td><td>3.02</td><td>3.02</td></tr><tr><td>H1a-2</td><td>0.045</td><td>0.042</td><td>3.02</td><td>3.02</td></tr><tr><td>H1b-1</td><td>0.312</td><td>0.303</td><td>2.91</td><td>2.91</td></tr><tr><td>H1b-2</td><td>0.312</td><td>0.303</td><td>2.91</td><td>2.91</td></tr><tr><td>H2-1</td><td>0.358</td><td>0.345</td><td>2.88</td><td>2.89</td></tr><tr><td>H2-2</td><td>0.358</td><td>0.345</td><td>2.88</td><td>2.89</td></tr><tr><td colspan="5">Ti4N3 (no termination)</td></tr><tr><td></td><td>PBE-D2  \( \Delta E \)  (eV/atom)</td><td>PBE  \( \Delta E \)  (eV/atom)</td><td>PBE-D2  \( a \)  ( \( \textup{\AA} \) )</td><td>PBE  \( a \)  ( \( \textup{\AA} \) )</td></tr><tr><td>T-1</td><td>0.000</td><td>0.000</td><td>2.99</td><td>2.99</td></tr><tr><td>T-2</td><td>0.000</td><td>0.000</td><td>2.99</td><td>2.99</td></tr><tr><td>H1a-1</td><td>0.097</td><td>0.092</td><td>2.97</td><td>2.97</td></tr><tr><td>H1a-2</td><td>0.097</td><td>0.092</td><td>2.97</td><td>2.97</td></tr><tr><td>H1b-1</td><td>0.323</td><td>0.309</td><td>2.93</td><td>2.94</td></tr><tr><td>H1b-2</td><td>0.323</td><td>0.309</td><td>2.93</td><td>2.94</td></tr><tr><td>H2-1</td><td>0.390</td><td>0.370</td><td>2.89</td><td>2.90</td></tr><tr><td>H2-2</td><td>0.390</td><td>0.370</td><td>2.89</td><td>2.90</td></tr></table>
 

Table S10. DFT-calculated energy difference ( \( \Delta E \) ) and DFT-optimized lattice constants (a) of all oxygen-terminated TiN-based 2D MXenes ( \( Ti_{n+1}N_{n}O_{2} \) , where n = 1-3) using PBE functional and PBE-D2 with vdW corrections. The energy difference is determined by:  \( \Delta E = E_{MX} - \min(E_{MX}) \) , where  \( E_{MX} \)  is the ground state energy of each MXene structure and  \( \min(E_{MX}) \)  is the energy of the most stable MXene within the same group.

<table><tr><td colspan="5">Ti2NO2(oxygen termination)</td></tr><tr><td></td><td>PBE-D2 ΔE(eV/atom)</td><td>PBE ΔE(eV/ atom)</td><td>PBE-D2 a(Å)</td><td>PBE a(Å)</td></tr><tr><td>T-1</td><td>0.000</td><td>0.000</td><td>3.00</td><td>3.00</td></tr><tr><td>T-2</td><td>0.254</td><td>0.248</td><td>2.91</td><td>2.92</td></tr><tr><td>H-1</td><td>0.079</td><td>0.069</td><td>3.01</td><td>3.01</td></tr><tr><td>H-2</td><td>0.335</td><td>0.315</td><td>2.92</td><td>2.92</td></tr><tr><td colspan="5">Ti3N2O2(oxygen termination)</td></tr><tr><td></td><td>PBE-D2 ΔE(eV/atom)</td><td>PBE ΔE(eV/ atom)</td><td>PBE-D2 a(Å)</td><td>PBE a(Å)</td></tr><tr><td>T-1</td><td>0.000</td><td>0.000</td><td>3.01</td><td>3.01</td></tr><tr><td>T-2</td><td>0.184</td><td>0.181</td><td>2.95</td><td>2.95</td></tr><tr><td>H1a-1</td><td>0.212</td><td>0.207</td><td>2.92</td><td>2.93</td></tr><tr><td>H1a-2</td><td>0.015</td><td>0.012</td><td>2.98</td><td>2.98</td></tr><tr><td>H1b-1</td><td>0.106</td><td>0.094</td><td>3.02</td><td>3.02</td></tr><tr><td>H1b-2</td><td>0.323</td><td>0.303</td><td>2.94</td><td>2.94</td></tr><tr><td>H2-1</td><td>0.359</td><td>0.336</td><td>2.91</td><td>2.92</td></tr><tr><td>H2-2</td><td>0.130</td><td>0.113</td><td>2.98</td><td>2.99</td></tr><tr><td colspan="5">Ti4N3O2(oxygen termination)</td></tr><tr><td></td><td>PBE-D2 ΔE(eV/atom)</td><td>PBE ΔE(eV/ atom)</td><td>PBE-D2 a(Å)</td><td>PBE a(Å)</td></tr><tr><td>T-1</td><td>0.000</td><td>0.000</td><td>3.00</td><td>3.00</td></tr><tr><td>T-2</td><td>0.131</td><td>0.129</td><td>2.96</td><td>2.97</td></tr><tr><td>H1a-1</td><td>0.185</td><td>0.179</td><td>2.93</td><td>2.93</td></tr><tr><td>H1a-2</td><td>0.045</td><td>0.041</td><td>2.96</td><td>2.97</td></tr><tr><td>H1b-1</td><td>0.141</td><td>0.125</td><td>2.99</td><td>3.00</td></tr><tr><td>H1b-2</td><td>0.306</td><td>0.286</td><td>2.95</td><td>2.95</td></tr><tr><td>H2-1</td><td>0.361</td><td>0.336</td><td>2.91</td><td>2.92</td></tr><tr><td>H2-2</td><td>0.186</td><td>0.165</td><td>2.95</td><td>2.96</td></tr></table>
 

Table S11. DFT-calculated energy difference ( \( \Delta E \) ) and DFT-optimized lattice constants (a) of all fluoride-terminated TiN-based 2D MXenes ( \( Ti_{n+1}N_{n}F_{2} \) , where n=1-3) using PBE functional and PBE-D2 with vdW corrections. The energy difference is determined by:  \( \Delta E = E_{MX} - \min(E_{MX}) \) , where  \( E_{MX} \)  is the ground state energy of each MXene structure and  \( \min(E_{MX}) \)  is the energy of the most stable MXene within the same group.

<table><tr><td colspan="5">Ti2NF2(fluoride termination)</td></tr><tr><td></td><td>PBE-D2  \( \Delta E \)  (eV/atom)</td><td>PBE  \( \Delta E \)  (eV/atom)</td><td>PBE-D2  \( a \)  ( \( \textup{\AA} \) )</td><td>PBE  \( a \)  ( \( \textup{\AA} \) )</td></tr><tr><td>T-1</td><td>0.000</td><td>0.000</td><td>3.06</td><td>3.06</td></tr><tr><td>T-2</td><td>0.084</td><td>0.085</td><td>2.90</td><td>2.91</td></tr><tr><td>H-1</td><td>0.207</td><td>0.204</td><td>2.90</td><td>2.91</td></tr><tr><td>H-2</td><td>0.164</td><td>0.159</td><td>2.88</td><td>2.89</td></tr><tr><td colspan="5">Ti3N2F2(fluoride termination)</td></tr><tr><td></td><td>PBE-D2  \( \Delta E \)  (eV/atom)</td><td>PBE  \( \Delta E \)  (eV/atom)</td><td>PBE-D2  \( a \)  ( \( \textup{\AA} \) )</td><td>PBE  \( a \)  ( \( \textup{\AA} \) )</td></tr><tr><td>T-1</td><td>0.011</td><td>0.012</td><td>3.02</td><td>3.03</td></tr><tr><td>T-2</td><td>0.000</td><td>0.000</td><td>2.94</td><td>2.94</td></tr><tr><td>H1a-1</td><td>0.040</td><td>0.038</td><td>2.92</td><td>2.93</td></tr><tr><td>H1a-2</td><td>0.064</td><td>0.064</td><td>2.98</td><td>2.99</td></tr><tr><td>H1b-1</td><td>0.188</td><td>0.180</td><td>2.93</td><td>2.94</td></tr><tr><td>H1b-2</td><td>0.161</td><td>0.151</td><td>2.91</td><td>2.92</td></tr><tr><td>H2-1</td><td>0.186</td><td>0.173</td><td>2.89</td><td>2.90</td></tr><tr><td>H2-2</td><td>0.214</td><td>0.203</td><td>2.91</td><td>2.92</td></tr><tr><td colspan="5">Ti4N3F2(fluoride termination)</td></tr><tr><td></td><td>PBE-D2  \( \Delta E \)  (eV/atom)</td><td>PBE  \( \Delta E \)  (eV/atom)</td><td>PBE-D2  \( a \)  ( \( \textup{\AA} \) )</td><td>PBE  \( a \)  ( \( \textup{\AA} \) )</td></tr><tr><td>T-1</td><td>0.000</td><td>0.000</td><td>3.02</td><td>3.02</td></tr><tr><td>T-2</td><td>0.020</td><td>0.019</td><td>2.95</td><td>2.96</td></tr><tr><td>H1a-1</td><td>0.073</td><td>0.069</td><td>2.92</td><td>2.93</td></tr><tr><td>H1a-2</td><td>0.072</td><td>0.068</td><td>2.99</td><td>3.00</td></tr><tr><td>H1b-1</td><td>0.211</td><td>0.200</td><td>2.95</td><td>2.95</td></tr><tr><td>H1b-2</td><td>0.194</td><td>0.181</td><td>2.92</td><td>2.93</td></tr><tr><td>H2-1</td><td>0.241</td><td>0.223</td><td>2.89</td><td>2.90</td></tr><tr><td>H2-2</td><td>0.261</td><td>0.245</td><td>2.91</td><td>2.92</td></tr></table>
 

Table S12. DFT-calculated energy difference ( \( \Delta E \) ) and DFT-optimized lattice constants (a) of all non-terminated MoN-based 2D MXenes ( \( Mo_{n+1}N_{n} \) , where n = 1-3) using PBE functional and PBE-D2 with vdW corrections. The energy difference is determined by:  \( \Delta E = E_{MX} - \min(E_{MX}) \) , where  \( E_{MX} \)  is the ground state energy of each MXene structure and  \( \min(E_{MX}) \)  is the energy of the most stable MXene within the same group.

<table><tr><td colspan="5">Mo2N (no termination)</td></tr><tr><td></td><td>PBE-D2  \( \Delta E \)  (eV/atom)</td><td>PBE  \( \Delta E \)  (eV/atom)</td><td>PBE-D2  \( a \)  ( \( \textup{\AA} \) )</td><td>PBE  \( a \)  ( \( \textup{\AA} \) )</td></tr><tr><td>T-1</td><td>0.088</td><td>0.095</td><td>2.90</td><td>2.82</td></tr><tr><td>T-2</td><td>0.088</td><td>0.095</td><td>2.90</td><td>2.82</td></tr><tr><td>H-1</td><td>0.000</td><td>0.000</td><td>2.84</td><td>2.83</td></tr><tr><td>H-2</td><td>0.000</td><td>0.000</td><td>2.84</td><td>2.83</td></tr><tr><td colspan="5">Mo3N2 (no termination)</td></tr><tr><td></td><td>PBE-D2  \( \Delta E \)  (eV/atom)</td><td>PBE  \( \Delta E \)  (eV/atom)</td><td>PBE-D2  \( a \)  ( \( \textup{\AA} \) )</td><td>PBE  \( a \)  ( \( \textup{\AA} \) )</td></tr><tr><td>T-1</td><td>0.375</td><td>0.358</td><td>3.08</td><td>3.08</td></tr><tr><td>T-2</td><td>0.190</td><td>0.206</td><td>2.78</td><td>2.79</td></tr><tr><td>H1a-1</td><td>0.178</td><td>0.189</td><td>2.82</td><td>2.84</td></tr><tr><td>H1a-2</td><td>0.178</td><td>0.189</td><td>2.82</td><td>2.84</td></tr><tr><td>H1b-1</td><td>0.000</td><td>0.000</td><td>2.81</td><td>2.83</td></tr><tr><td>H1b-2</td><td>0.000</td><td>0.000</td><td>2.82</td><td>2.83</td></tr><tr><td>H2-1</td><td>0.056</td><td>0.054</td><td>2.82</td><td>2.83</td></tr><tr><td>H2-2</td><td>0.056</td><td>0.054</td><td>2.82</td><td>2.83</td></tr><tr><td colspan="5">Mo4N3 (no termination)</td></tr><tr><td></td><td>PBE-D2  \( \Delta E \)  (eV/atom)</td><td>PBE  \( \Delta E \)  (eV/atom)</td><td>PBE-D2  \( a \)  ( \( \textup{\AA} \) )</td><td>PBE  \( a \)  ( \( \textup{\AA} \) )</td></tr><tr><td>T-1</td><td>0.272</td><td>0.000</td><td>3.23</td><td>2.99</td></tr><tr><td>T-2</td><td>0.203</td><td>0.307</td><td>2.78</td><td>2.80</td></tr><tr><td>H1a-1</td><td>0.203</td><td>0.296</td><td>2.85</td><td>2.87</td></tr><tr><td>H1a-2</td><td>0.203</td><td>0.296</td><td>2.85</td><td>2.87</td></tr><tr><td>H1b-1</td><td>0.000</td><td>0.084</td><td>2.82</td><td>2.83</td></tr><tr><td>H1b-2</td><td>0.000</td><td>0.084</td><td>2.82</td><td>2.83</td></tr><tr><td>H2-1</td><td>0.064</td><td>0.146</td><td>2.83</td><td>2.84</td></tr><tr><td>H2-2</td><td>0.064</td><td>0.146</td><td>2.83</td><td>2.84</td></tr></table>
 

Table S13. DFT-calculated energy difference ( \( \Delta E \) ) and DFT-optimized lattice constants (a) of all oxygen-terminated MoN-based 2D MXenes ( \( Mo_{n+1}N_{n}O_{2} \) , where n = 1-3) using PBE functional and PBE-D2 with vdW corrections. The energy difference is determined by:  \( \Delta E = E_{MX} - \min(E_{MX}) \) , where  \( E_{MX} \)  is the ground state energy of each MXene structure and  \( \min(E_{MX}) \)  is the energy of the most stable MXene within the same group.

<table><tr><td colspan="5">Mo2NO2(oxygen termination)</td></tr><tr><td></td><td>PBE-D2 ΔE(eV/atom)</td><td>PBE ΔE(eV/ atom)</td><td>PBE-D2 a(Å)</td><td>PBE a(Å)</td></tr><tr><td>T-1</td><td>0.259</td><td>0.272</td><td>2.85</td><td>2.86</td></tr><tr><td>T-2</td><td>0.259</td><td>0.061</td><td>2.85</td><td>2.87</td></tr><tr><td>H-1</td><td>0.096</td><td>0.099</td><td>2.87</td><td>2.88</td></tr><tr><td>H-2</td><td>0.000</td><td>0.000</td><td>2.87</td><td>2.88</td></tr><tr><td colspan="5">Mo3N2O2(oxygen termination)</td></tr><tr><td></td><td>PBE-D2 ΔE(eV/atom)</td><td>PBE ΔE(eV/ atom)</td><td>PBE-D2 a(Å)</td><td>PBE a(Å)</td></tr><tr><td>T-1</td><td>0.328</td><td>0.329</td><td>3.14</td><td>3.14</td></tr><tr><td>T-2</td><td>0.104</td><td>0.119</td><td>2.83</td><td>2.84</td></tr><tr><td>H1a-1</td><td>0.142</td><td>0.153</td><td>2.87</td><td>2.88</td></tr><tr><td>H1a-2</td><td>0.241</td><td>0.258</td><td>2.82</td><td>2.84</td></tr><tr><td>H1b-1</td><td>0.102</td><td>0.104</td><td>2.85</td><td>2.87</td></tr><tr><td>H1b-2</td><td>0.000</td><td>0.000</td><td>2.83</td><td>2.85</td></tr><tr><td>H2-1</td><td>0.072</td><td>0.071</td><td>2.87</td><td>2.88</td></tr><tr><td>H2-2</td><td>0.101</td><td>0.101</td><td>2.84</td><td>2.86</td></tr><tr><td colspan="5">Mo4N3O2(oxygen termination)</td></tr><tr><td></td><td>PBE-D2 ΔE(eV/atom)</td><td>PBE ΔE(eV/ atom)</td><td>PBE-D2 a(Å)</td><td>PBE a(Å)</td></tr><tr><td>T-1</td><td>0.263</td><td>0.270</td><td>3.19</td><td>3.19</td></tr><tr><td>T-2</td><td>0.133</td><td>0.150</td><td>2.82</td><td>2.83</td></tr><tr><td>H1a-1</td><td>0.170</td><td>0.182</td><td>2.87</td><td>2.89</td></tr><tr><td>H1a-2</td><td>0.238</td><td>0.254</td><td>2.84</td><td>2.85</td></tr><tr><td>H1b-1</td><td>0.079</td><td>0.082</td><td>2.85</td><td>2.87</td></tr><tr><td>H1b-2</td><td>0.000</td><td>0.000</td><td>2.83</td><td>2.85</td></tr><tr><td>H2-1</td><td>0.078</td><td>0.076</td><td>2.85</td><td>2.87</td></tr><tr><td>H2-2</td><td>0.086</td><td>0.085</td><td>2.85</td><td>2.87</td></tr></table>
 

Table S14. DFT-calculated energy difference ( \( \Delta E \) ) and DFT-optimized lattice constants (a) of all fluoride-terminated MoN-based 2D MXenes ( \( Mo_{n+1}N_{n}F_{2} \) , where n = 1-3) using PBE functional and PBE-D2 with vdW corrections. The energy difference is determined by:  \( \Delta E = E_{MX} - \min(E_{MX}) \) , where  \( E_{MX} \)  is the ground state energy of each MXene structure and  \( \min(E_{MX}) \)  is the energy of the most stable MXene within the same group.

<table><tr><td colspan="5">Mo2NF2(fluoride termination)</td></tr><tr><td></td><td>PBE-D2  \( \Delta E \)  (eV/atom)</td><td>PBE  \( \Delta E \)  (eV/atom)</td><td>PBE-D2  \( a \)  ( \( \textup{\AA} \) )</td><td>PBE  \( a \)  ( \( \textup{\AA} \) )</td></tr><tr><td>T-1</td><td>0.174</td><td>0.114</td><td>2.85</td><td>2.78</td></tr><tr><td>T-2</td><td>0.097</td><td>0.228</td><td>2.96</td><td>3.00</td></tr><tr><td>H-1</td><td>0.000</td><td>0.000</td><td>2.89</td><td>2.80</td></tr><tr><td>H-2</td><td>0.056</td><td>0.151</td><td>2.92</td><td>2.98</td></tr><tr><td colspan="5">Mo3N2F2(fluoride termination)</td></tr><tr><td></td><td>PBE-D2  \( \Delta E \)  (eV/atom)</td><td>PBE  \( \Delta E \)  (eV/atom)</td><td>PBE-D2  \( a \)  ( \( \textup{\AA} \) )</td><td>PBE  \( a \)  ( \( \textup{\AA} \) )</td></tr><tr><td>T-1</td><td>0.245</td><td>0.237</td><td>3.21</td><td>3.20</td></tr><tr><td>T-2</td><td>0.334</td><td>0.316</td><td>2.99</td><td>3.02</td></tr><tr><td>H1a-1</td><td>0.310</td><td>0.305</td><td>2.88</td><td>2.91</td></tr><tr><td>H1a-2</td><td>0.166</td><td>0.173</td><td>2.82</td><td>2.84</td></tr><tr><td>H1b-1</td><td>0.000</td><td>0.000</td><td>2.82</td><td>2.84</td></tr><tr><td>H1b-2</td><td>0.128</td><td>0.125</td><td>2.83</td><td>2.85</td></tr><tr><td>H2-1</td><td>0.165</td><td>0.160</td><td>2.83</td><td>2.84</td></tr><tr><td>H2-2</td><td>0.021</td><td>0.019</td><td>2.82</td><td>2.84</td></tr><tr><td colspan="5">Mo4N3F2(fluoride termination)</td></tr><tr><td></td><td>PBE-D2  \( \Delta E \)  (eV/atom)</td><td>PBE  \( \Delta E \)  (eV/atom)</td><td>PBE-D2  \( a \)  ( \( \textup{\AA} \) )</td><td>PBE  \( a \)  ( \( \textup{\AA} \) )</td></tr><tr><td>T-1</td><td>0.132</td><td>0.124</td><td>3.22</td><td>3.23</td></tr><tr><td>T-2</td><td>0.271</td><td>0.284</td><td>2.79</td><td>2.81</td></tr><tr><td>H1a-1</td><td>0.290</td><td>0.285</td><td>2.90</td><td>2.93</td></tr><tr><td>H1a-2</td><td>0.194</td><td>0.201</td><td>2.84</td><td>2.87</td></tr><tr><td>H1b-1</td><td>0.000</td><td>0.000</td><td>2.82</td><td>2.84</td></tr><tr><td>H1b-2</td><td>0.089</td><td>0.087</td><td>2.83</td><td>2.85</td></tr><tr><td>H2-1</td><td>0.150</td><td>0.145</td><td>2.84</td><td>2.86</td></tr><tr><td>H2-2</td><td>0.046</td><td>0.043</td><td>2.83</td><td>2.83</td></tr></table>
 

Table S15. DFT-calculated energy difference ( \( \Delta E \) ) and DFT-optimized lattice constants (a) of all fluoride-terminated HfC- and HfN-based 2D MXenes using PBE-D2 functional with vdW corrections. The energy difference is determined by:  \( \Delta E = E_{\mathrm{MX}} - \min(E_{\mathrm{MX}}) \) , where  \( E_{MX} \)  is the ground state energy of each MXene structure and  \( \min(E_{\mathrm{MX}}) \)  is the energy of the most stable MXene within the same group.

<table><tr><td colspan="3">Hf2CF2</td><td colspan="2">Hf2NF2</td></tr><tr><td></td><td>ΔE(eV/atom)</td><td>a(Å)</td><td>ΔE(eVs/atom)</td><td>α(Å)</td></tr><tr><td>T-1</td><td>0.000</td><td>3.26</td><td>0.028</td><td>3.25</td></tr><tr><td>T-2</td><td>0.064</td><td>3.15</td><td>0.000</td><td>3.06</td></tr><tr><td>H-1</td><td>0.259</td><td>3.24</td><td>0.160</td><td>2.98</td></tr><tr><td>H-2</td><td>0.305</td><td>3.11</td><td>0.051</td><td>3.02</td></tr><tr><td colspan="3">Hf3C2F2</td><td colspan="2">Hf3N2F2</td></tr><tr><td></td><td>ΔE(eVs/atom)</td><td>a(Å)</td><td>ΔE(evs/atom)</td><td>α(Å)</td></tr><tr><td>T-1</td><td>0.000</td><td>3.29</td><td>0.099</td><td>3.20</td></tr><tr><td>T-2</td><td>0.088</td><td>3.21</td><td>0.000</td><td>3.10</td></tr><tr><td>H1a-1</td><td>0.114</td><td>3.20</td><td>0.026</td><td>3.08</td></tr><tr><td>H1a-2</td><td>0.003</td><td>3.29</td><td>0.131</td><td>3.09</td></tr><tr><td>H1b-1</td><td>0.310</td><td>3.25</td><td>0.247</td><td>3.01</td></tr><tr><td>H1b-2</td><td>0.366</td><td>3.16</td><td>0.164</td><td>3.04</td></tr><tr><td>H2-1</td><td>0.419</td><td>3.14</td><td>0.162</td><td>3.02</td></tr><tr><td>H2-2</td><td>0.337</td><td>3.24</td><td>0.258</td><td>3.01</td></tr><tr><td colspan="3">Hf4C3F2</td><td colspan="2">Hf4N3F2</td></tr><tr><td></td><td>ΔE(eVs/atom)</td><td>a(Å)</td><td>ΔE(evs/atom)</td><td>α(Å)</td></tr><tr><td>T-1</td><td>0.000</td><td>3.30</td><td>0.041</td><td>3.21</td></tr><tr><td>T-2</td><td>0.070</td><td>3.23</td><td>0.000</td><td>3.11</td></tr><tr><td>H1a-1</td><td>0.121</td><td>3.22</td><td>0.019</td><td>3.08</td></tr><tr><td>H1a-2</td><td>0.025</td><td>3.28</td><td>0.088</td><td>3.12</td></tr><tr><td>H1b-1</td><td>0.337</td><td>3.24</td><td>0.222</td><td>3.03</td></tr><tr><td>H1b-2</td><td>0.396</td><td>3.18</td><td>0.159</td><td>3.05</td></tr><tr><td>H2-1</td><td>0.472</td><td>3.15</td><td>0.169</td><td>3.02</td></tr><tr><td>H2-2</td><td>0.396</td><td>3.23</td><td>0.241</td><td>3.00</td></tr></table>
 

Table S16. DFT-calculated energy difference ( \( \Delta E \) ) and DFT-optimized lattice constants (a) of all fluoride-terminated ReC- and ReN-based 2D MXenes using PBE-D2 functional with vdW corrections. The energy difference is determined by:  \( \Delta E = E_{\mathrm{MX}} - \min(E_{\mathrm{MX}}) \) , where  \( E_{MX} \)  is the ground state energy of each MXene structure and  \( \min(E_{\mathrm{MX}}) \)  is the energy of the most stable MXene within the same group.

<table><tr><td colspan="3">Re2CF2</td><td colspan="2">Re2NF2</td></tr><tr><td></td><td>ΔE(eV/atom)</td><td>a(Å)</td><td>ΔE(eVs/atom)</td><td>α(Å)</td></tr><tr><td>T-1</td><td>0.329</td><td>3.34</td><td>0.310</td><td>3.39</td></tr><tr><td>T-2</td><td>0.359</td><td>3.03</td><td>0.306</td><td>2.65</td></tr><tr><td>H-1</td><td>0.000</td><td>2.77</td><td>0.000</td><td>3.73</td></tr><tr><td>H-2</td><td>0.135</td><td>2.79</td><td>0.266</td><td>3.07</td></tr><tr><td colspan="3">Re3C2F2</td><td colspan="2">Re3N2F2</td></tr><tr><td></td><td>ΔE(eVs/atom)</td><td>a(Å)</td><td>ΔE(evs/atom)</td><td>α(Å)</td></tr><tr><td>T-1</td><td>0.845</td><td>3.19</td><td>0.977</td><td>3.31</td></tr><tr><td>T-2</td><td>0.913</td><td>3.06</td><td>1.216</td><td>3.18</td></tr><tr><td>H1a-1</td><td>0.889</td><td>2.85</td><td>0.968</td><td>2.67</td></tr><tr><td>H1a-2</td><td>0.000</td><td>3.29</td><td>0.823</td><td>3.39</td></tr><tr><td>H1b-1</td><td>0.399</td><td>2.79</td><td>0.000</td><td>2.73</td></tr><tr><td>H1b-2</td><td>0.493</td><td>2.80</td><td>0.774</td><td>2.72</td></tr><tr><td>H2-1</td><td>0.495</td><td>2.80</td><td>0.827</td><td>2.71</td></tr><tr><td>H2-2</td><td>0.401</td><td>2.80</td><td>0.699</td><td>2.71</td></tr><tr><td colspan="3">Re4C3F2</td><td colspan="2">Re4N3F2</td></tr><tr><td></td><td>ΔE(eVs/atom)</td><td>a(Å)</td><td>ΔE(evs/atom)</td><td>α(Å)</td></tr><tr><td>T-1</td><td>0.431</td><td>3.24</td><td>0.444</td><td>3.29</td></tr><tr><td>T-2</td><td>0.565</td><td>3.17</td><td>0.330</td><td>2.69</td></tr><tr><td>H1a-1</td><td>0.484</td><td>2.86</td><td>0.665</td><td>3.08</td></tr><tr><td>H1a-2</td><td>0.405</td><td>2.82</td><td>0.271</td><td>2.68</td></tr><tr><td>H1b-1</td><td>0.015</td><td>2.81</td><td>0.000</td><td>2.73</td></tr><tr><td>H1b-2</td><td>0.082</td><td>2.81</td><td>0.123</td><td>2.73</td></tr><tr><td>H2-1</td><td>0.082</td><td>2.81</td><td>0.230</td><td>2.73</td></tr><tr><td>H2-2</td><td>0.000</td><td>2.81</td><td>0.125</td><td>2.73</td></tr></table>
 
![](./images/1092748071881670702_12.jpg)

Mo₂N MXenes (No termination)

![](./images/1092748071881670702_13.jpg)

Fig. S1. Phonon spectra and vibrational density of states (vDOS) of (a) four  \( Mo_{2}C \)  MXenes and (b) four  \( Mo_2N \)  MXenes. Without termination atoms, two bulk derived MXenes are identical.
 
![](./images/1092748071881670702_14.jpg)

![](./images/1092748071881670702_15.jpg)

![](./images/1092748071881670702_16.jpg)

![](./images/1092748071881670702_17.jpg)

Fig. S2. Phonon spectra and vibrational density of states (vDOS) of eight types of  \( Mo_{3}C_{2} \)  MXenes. Without termination elements, two bulk derived MXenes are identical.

![](./images/1092748071881670702_18.jpg)

![](./images/1092748071881670702_19.jpg)

![](./images/1092748071881670702_20.jpg)

![](./images/1092748071881670702_21.jpg)

Fig. S3. Phonon spectra and vibrational density of states (vDOS) of eight types of  \( Mo_{3}N_{2} \)  MXenes. Without termination elements, two bulk derived MXenes are identical.
 
![](./images/1092748071881670702_22.jpg)

Fig. S4. Phonon spectra and vibrational density of states (vDOS) of eight types of  \( Mo_{4}C_{3} \)  MXenes. Without termination elements, two bulk derived MXenes are identical.

![](./images/1092748071881670702_23.jpg)

Fig. S5. Phonon spectra and vibrational density of states (vDOS) of eight types of  \( Mo_{4}N_{3} \)  MXenes. Without termination elements, two bulk derived MXenes are identical.
 
![](./images/1092748071881670702_24.jpg)

Ti₂N MXenes (No termination)

![](./images/1092748071881670702_25.jpg)

Fig. S6. Phonon spectra and vibrational density of states (vDOS) of (a) four Ti \( _{2} \) C MXenes and (b) four Ti \( _{3} \) N MXenes. Without termination atoms, two bulk derived MXenes are identical.
 
![](./images/1092748071881670702_26.jpg)

Fig. S7. Phonon spectra and vibrational density of states (vDOS) of eight types of  \( Ti_{3}C_{2} \)  MXenes. Without termination atoms, two bulk derived MXenes are identical.

![](./images/1092748071881670702_27.jpg)

Fig. S8. Phonon spectra and vibrational density of states (DOSs) of eight types of  \( Ti_{3}N_{2} \)  MXenes. Without termination atoms, two bulk derived MXenes are identical.
 
![](./images/1092748071881670702_28.jpg)

Fig. S9. Phonon spectra and vibrational density of states (vDOS) of eight types of  \( Ti_{4}C_{3} \)  MXenes. Without termination atoms, two bulk derived MXenes are identical.

![](./images/1092748071881670702_29.jpg)

Fig. S10. Phonon spectra and vibrational density of states (DOSs) of eight types of  \( Ti_{4}N_{3} \)  MXenes. Without termination atoms, two bulk derived MXenes are identical.
 
![](./images/1092748071881670702_30.jpg)

![](./images/1092748071881670702_31.jpg)

![](./images/1092748071881670702_32.jpg)

![](./images/1092748071881670702_33.jpg)

![](./images/1092748071881670702_34.jpg)

![](./images/1092748071881670702_35.jpg)

![](./images/1092748071881670702_36.jpg)

![](./images/1092748071881670702_37.jpg)

Fig. S11. Phonon spectra and vibrational density of states (vDOS) of (a) four  \( Mo_{2}CF_{2} \)  MXenes and (b) four  \( Mo_{2}NF_{2} \)  MXenes, both terminated by fluorine atoms.
 
![](./images/1092748071881670702_38.jpg)

Fig. S12. Phonon spectra and vibrational density of states (vDOS) of eight types of  \( Mo_{3}C_{2}F_{2} \) -based MXenes terminated by fluorine atoms.

![](./images/1092748071881670702_39.jpg)

Fig. S13. Phonon spectra and vibrational density of states (vDOS) of eight types of  \( Mo_{3}N_{2}F_{2} \)  MXenes terminated by fluorine atoms.
 
![](./images/1092748071881670702_40.jpg)

Fig. S14. Phonon spectra and vibrational density of states (vDOS) of eight types of  \( Mo_{4}C_{3}F_{2} \)  MXenes terminated by fluorine atoms.

![](./images/1092748071881670702_41.jpg)

Fig. S15. Phonon spectra and vibrational density of states (vDOS) of eight types of  \( Mo_{4}N_{3}F_{2} \)  MXenes terminated by fluorine atoms.
 
![](./images/1092748071881670702_42.jpg)

Fig. S16. Phonon spectra and vibrational density of states (vDOS) of (a) four  \( Mo_{2}CO_{2} \)  MXenes and (b) four  \( Mo_{2}NO_{2} \)  MXenes, both terminated by oxygen atoms.
 
![](./images/1092748071881670702_43.jpg)

Fig. S17. Phonon spectra and vibrational density of states (vDOS) of eight types of  \( Mo_{3}C_{2}O_{2} \) -based MXenes terminated by oxygen atoms.

![](./images/1092748071881670702_44.jpg)

Fig. S18. Phonon spectra and vibrational density of states (vDOS) of eight types of  \( Mo_{3}N_{2}O_{2} \) -based MXenes terminated by oxygen atoms.
 
![](./images/1092748071881670702_45.jpg)

Fig. S19. Phonon spectra and vibrational density of states (DOSs) of eight types of  \( Mo_{4}C_{3}O_{2} \)  MXenes terminated by oxygen atoms.

![](./images/1092748071881670702_46.jpg)

Fig. S20. Phonon spectra and vibrational density of states (vDOS) of eight types of  \( Mo_{4}N_{3}O_{2} \)  MXenes terminated by oxygen atoms.
 
![](./images/1092748071881670702_47.jpg)

Fig. S21. Phonon spectra and vibrational density of states (vDOS) of (a) four  \( Ti_{2}CF_{2} \)  MXenes and (b) four  \( Ti_{2}NF_{2} \)  MXenes, both terminated by fluorine atoms.
 
![](./images/1092748071881670702_48.jpg)

Fig. S22. Phonon spectra and vibrational density of states (vDOS) of eight types of  \( Ti_{3}C_{2}F_{2} \)  MXenes terminated by fluorine atoms.

![](./images/1092748071881670702_49.jpg)

Fig. S23. Phonon spectra and vibrational density of states (vDOS) of eight types of  \( Ti_{3}N_{2}F_{2} \)  MXenes terminated by fluorine atoms.
 
![](./images/1092748071881670702_50.jpg)

Fig. S24. Phonon spectra and vibrational density of states (vDOS) of eight types of  \( Ti_{4}C_{3}F_{2}MXenes \)  terminated by fluorine atoms.

![](./images/1092748071881670702_51.jpg)

Fig. S25. Phonon spectra and vibrational density of states (vDOS) of eight types of  \( Ti_{4}N_{3}F_{2}MXenes \)  terminated by fluorine atoms.
 
![](./images/1092748071881670702_52.jpg)

Fig. S26. Phonon spectra and vibrational density of states (vDOS) of (a) four  \( Ti_{2}CO_{2} \)  MXenes and (b) four  \( Ti_{2}NO_{2} \)  MXenes, both terminated by oxygen atoms.
 
![](./images/1092748071881670702_53.jpg)

Fig. S27. Phonon spectra and vibrational density of states (vDOS) of eight types of  \( Ti_{3}C_{2}O_{2} \)  MXenes terminated by oxygen atoms.

![](./images/1092748071881670702_54.jpg)

Fig. S28. Phonon spectra and vibrational density of states (vDOS) of eight types of  \( Ti_{3}N_{2}O_{2} \)  MXenes terminated by oxygen atoms.
 
![](./images/1092748071881670702_55.jpg)

Fig. S29. Phonon spectra and vibrational density of states (vDOS) of eight types of  \( Ti_{4}C_{3}O_{2} \)  MXenes terminated by oxygen atoms.

![](./images/1092748071881670702_56.jpg)

Fig. S30. Phonon spectra and vibrational density of states (vDOS) of eight types of  \( Ti_{4}N_{3}O_{2} \)  MXenes terminated by oxygen atoms.
 

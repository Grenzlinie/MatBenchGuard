Article

# Mechanical Properties of a Solvated Biomolecule: RGD (1FUV) Peptide

Puja Adhikari $^{1}$, Bahaa Jawad $^{1,2}$ and Wai-Yim Ching $^{1,*}$

1 Department of Physics and Astronomy, University of Missouri-Kansas City, Kansas City, MO 64110, USA; paz67@umkc.edu (P.A.); bahaa.a.jawad@uotechnology.edu.iq (B.J.)
2 Department of Applied Sciences, University of Technology, Baghdad 10066, Iraq
* Correspondence: chingw@umkc.edu

**Abstract:** The mechanical properties of proteins/peptides play an essential role in their functionalities and implications, as well as their structure and dynamic properties. Understanding mechanical properties is pivotal to our knowledge of protein folding and the molecular basis of diverse cellular processes. Herein, we present a computational approach using ab initio quantum mechanical calculations to determine the mechanical properties—such as bulk modulus, shear modulus, Young’s modulus, and Poisson’s ratio—of a solvated Arg-Gly-Asp (RGD) peptide model. Since this peptide serves as the RGD-directed integrin recognition site and may participate in cellular adhesion, it is considered a promising small peptide for medicinal applications. This successful approach paves the way for investigating larger and more complex biomolecules.

**Keywords:** RGD peptide; mechanical properties; solvated biomolecule; density functional theory

---

## 1. Introduction

Understanding the molecular structure of peptides, proteins, and other biological molecules is pivotal for discerning their function. The structure is primarily determined by experimental means. Historically, biomolecules have often been studied in crystalline form, a process offering advantages such as enabling high-resolution structural analysis using techniques like X-ray crystallography [1]. While this approach yields valuable insights, biomolecules within crystalline matrices are frequently constrained and may not exhibit the behaviors representative of natural environments.

Studying biomolecules in their native environments, such as in aqueous solutions, is essential for achieving a comprehensive understanding. Analyzing biomolecular structures in solvated form is crucial, given that all known biological processes within the human body occur in aqueous environments. Various in-solution techniques, including NMR spectroscopy, small-angle scattering (SAS), circular dichroism (CD), and infrared (IR) spectroscopy, facilitate such investigations [1]. Water, with its unique properties, plays a pivotal role in the folding processes of biomolecules [2,3].

Large-scale computational modeling of biomolecules in solution holds particular significance as they enable the simulation of biomolecular behavior to accommodate the more realistic environments. This approach allows for a deeper understanding of biomolecular dynamics and interactions, giving insights at the atomistic level, bridging the gap between experimental observations and biological reality [4].

In conventional materials science, we already possess a diverse set of techniques that enable us to gauge the behavior of its structures that can be applied to biomolecules. However, to fully understand the function of biomolecules, it is essential to identify the properties—structural, dynamical, and mechanical—that are critical for design [5]. Proteins, being soft in nature, can easily change their biological function when subjected to mechanical deformation [6]. Many cellular processes involve mechanical forces or deformation at various levels, including cellular, subcellular, and molecular scales [7,8]. For instance,

---

![](./images/1044473802802593803_1.jpg)

Citation: Adhikari, P.; Jawad, B.;
Ching, W.-Y. Mechanical Properties of
a Solvated Biomolecule: RGD (1FUV)
Peptide. *Int. J. Mol. Sci.* 2024, 25,
10164. https://doi.org/10.3390/
ijms251810164

Academic Editor: Oxana V.
Galzitskaya

Received: 12 August 2024
Revised: 17 September 2024
Accepted: 18 September 2024
Published: 21 September 2024

![](./images/1044473802802593803_2.jpg)

Copyright: © 2024 by the authors.
Licensee MDPI, Basel, Switzerland.
This article is an open access article
distributed under the terms and
conditions of the Creative Commons
Attribution (CC BY) license (https://
creativecommons.org/licenses/by/
4.0/).

biomoleculesolecular motors and machines transform chemical energy into mechanical motion to perform a wide range of functions [9,10]. During cell migration, the cell must generate contractile forces to move forward [11]. The adhesion of cells to extracellular matrix (ECM) via focal adhesion complexes is influenced by the substrate's stiffness [12,13]. Additionally, all living cells are constantly subjected to gravitational and other forces, with both normal and diseased conditions being dependent on or regulated by their mechanical environment. Such deformation can explain the molecular basis for many of the cellular processes involving mechano-sensing and mechano-transduction [6].

In molecular biology, despite the abundance of data on tumors, the fundamental differences between malignant and benign tumors remain unclear. There are studies that focus on whether the mechanical differences between normal and cancer cells can be used to diagnose cancer progression [14]. In fact, research has suggested that elastic properties such as Poison's ratio and Young's modulus of cancerous skin could become the first step in turning elasticity into a clinical tool [15,16].

In this study, we employed the ab initio method to investigate the mechanical properties of a solvated Arg-Gly-Asp (RGD) peptide (PDB ID: 1FUV). The RGD (1FUV) peptide consists of only 11 amino acid (AA) residues (see Figure 1) and is composed of AA sequence Arg-Gly-Asp (RGD) [17]. RGD has a high affinity for the membrane protein called integrin and is used to target cancer cells [18]. In addition, RGD has numerous applications in biomaterial design and biomedical devices. It is used for wound healing, radiotracers in imaging, and implantable medical devices [19,20]. RGD (1FUV) is of appropriate size for analysis of its mechanical properties. To study the mechanical properties, we apply ten different strain percentages to the solvated 1FUV. The details of the methodology are discussed in Section 5, models and methods. This study serves as an initial step in comprehending supersoft biomolecules from various angles.

![](./images/1044473802802593803_3.jpg)

Figure 1. The structure of RGD (1FUV) peptide (a) Ball and stick figure of 1FUV with eleven amino acid residues marked. (b) 1FUV in a water box: blue: N, gray: C, yellow: S, red: O, and white: H.

## 2. Results
### 2.1. Mechanical Properties

In this study, we have computed the bulk modulus ($K$), shear modulus ($G$), Young's modulus ($E$), and Poisson's ratio ($\eta$) of solvated RGD (1FUV). The specifics of the computational methods employed to calculate the mechanical properties are explained in Section 5, models and methods. Based on our recent findings in the amino acid study [21], we noted that mechanical properties exhibit greater variabilities at lower strain percentages. As a result, we have selected ten strains—0.25%, 0.50%, 0.75%, 1.00%, 1.25%, 1.5%, 1.75%, 2.00%, 2.25%, and 2.50%—for evaluating these mechanical properties. The results are listed in Table S1. Given the fact that the solvated biomolecules may contain voids, which could introduce uncertainty into both of their structure and properties, we performed five sets of calculations for each strain. These five sets of data are utilized for statistical error analysis

(see Table S1 and Figure 2) employing standard deviation. In Table S1, K1 to K5 are five sets of calculated bulk moduli, G1 to G5 are five sets of calculated shear moduli, E1 to E5 are five sets of Young's moduli, and $\eta 1$ to $\eta 5$ are five sets of Poisson's ratios.

The mean values and error bars for the five datasets in Table S1 for $K$, $G$, $E$, and $\eta$ are shown in Figure 2a-d. $K$, $G$, and $E$ exhibit a decrease with the increase in the strain percentage, with minor fluctuations as strain rises. $\eta$ also decreases with some fluctuations as the strain increases, but the overall decrease slope is slightly lower than that of $K$, $G$, and $E$. Apparently mechanical properties of solvated RGD (1FUV) follow the trend in solvated AAs [21]. Notably, $E$, $G$, and $\eta$ exhibit relatively higher error at 0.25%, whereas $K$ exhibits higher error at 1.75%. These errors can be deemed acceptable.

At 0.25% strain, $K$, $E$, and $\eta$ exhibit the highest mean values of $6.58 \pm 0.09$ GPa, $9.08 \pm 0.21$ GPa, and $0.270 \pm 0.005$, respectively. At 0.50% strain, G has the highest mean value of $3.58 \pm 0.02$ GPa. Conversely, at 2.25% strain, $K$, $G$, and $E$ display the lowest mean values of $5.86 \pm 0.10$ GPa, $3.42 \pm 0.02$ GPa, and $8.58 \pm 0.06$ GPa, respectively. At 1.75% strain, $\eta$ exhibits the lowest mean value of $0.255 \pm 0.003$. This shows that at lower strain the mechanical properties are slightly higher than the ones with higher strain. In comparison with amino acids [21], the overall $K$, $E$, and $\eta$ exhibit higher values, whereas $G$ shows similar values.

Both Poisson's ratio and Young's modulus were examined in a cancerous tissue, as these properties of cancerous skin could serve as the first step in using elasticity as a clinical tool [15]. They can also supplement as an additional non-invasive diagnostic tool [15]. The range of the mean values of the $\eta$ of solvated RGD (1FUV) is from $0.255 \pm 0.0001$ to $0.270 \pm 0.005$. An interesting point is that the Poisson's ratio for cancerous skin is about 0.43 [15]. RGD is also known to target cancer cells. At this moment, we are not sure how these values can be correlated. Another point of interest is the stiffness of biomolecules. Stiffness is a mechanical property demonstrated by Young's modulus. There are studies that show the relationship between stiffness and invasion of cancer cells [16]. During cancer progression, cells can become either soft or stiff [16]. However, there is no firm conclusion yet about the invasiveness and the softening of different types of cancers [14,22]. We trust our pioneering result facilitates the understanding of the elasticity of RGD (1FUV) that helps to target cancer cells.

![](./images/1044473802802593803_4.jpg)

Figure 2. Mean value of (a) bulk modulus, (b) shear modulus, (c) Young's modulus, and (d) Poisson's ratio for solvated RGD (1FUV) in ten different strain percentages and calculated error bars from five sets of data. The solid symbol denotes the case with relatively high error.

### 2.2. Bonding Analysis

Bond order (BO) serves as a measure of bond strength. Within the OLCAO scheme, we can compute BO for all bonds. The details of BO are explained in Section 5, models and methods. In the current work, we have applied the cutoff of 4.5 Å for bond lengths (BL). Moreover, we can determine the precise BL and BO for all atomic interactions in the solvated RGD (1FUV). By summing up all BOs within the system and normalizing by the volume containing these bonds, we can calculate the total bond order density (TBOD), a concept used in materials science. Calculating TBOD for biomolecules has its limitations, as biomolecules may not be as compact as crystalline or amorphous materials. However, this concept can still provide a rough analysis. TBOD of solvated RGD (1FUV) stands at $0.019\ \text{e}^{-}/\mathring{\text{A}}^{3}$. However, due to inherent limitations in applying TBOD for supersoft solvated biomolecules, it requires caution for relative comparisons. Below is a list of materials along with their respective TBOD values just for reference: pyrophosphate crystal $\text{K}_{2}\text{Mg}(\text{H}_{2}\text{P}_{2}\text{O}_{7})_{2}\ \text{H}_{2}\text{O}$ $(0.021\ \text{e}^{-}/\mathring{\text{A}}^{3})$ [23], C-S-H cement mineral suolunite $(0.027\ \text{e}^{-}/\mathring{\text{A}}^{3})$ [24], amorphous-$\text{SiO}_{2}$ (a-$\text{SiO}_{2}$ glasses) $(0.025\ \text{e}^{-}/\mathring{\text{A}}^{3})$ [25], crystalline montmorillonite clay $(0.033\ \text{e}^{-}/\mathring{\text{A}}^{3})$ [26], solvated montmorillonite clay $(0.022\ \text{e}^{-}/\mathring{\text{A}}^{3})$ [26]. Notably, these systems exhibit slightly higher TBOD compared to solvated RGD (1FUV), implying less internal cohesion in the solvated RGD.

It is important to recognize that direct comparisons between biomolecules have not been conducted, rendering such assessments inconclusive. Despite this, drawing from our experience, we maintain that solvated RGD (1FUV) retains considerable strength. This strength is bolstered by its bimolecular composition, wherein the presence of water molecules facilitates the formation of a robust hydrogen bonding network, further fortifying its structural integrity.

Additionally, we can precisely determine the bond strength for interactions between AAs, intra-AAs, AAs with water, inter-water molecules, and intra-water molecules. It is noteworthy that intra-AAs and intra-water molecules typically exhibit higher bond strengths compared to inter-AAs, inter-water molecules, and interactions between AAs and water. Nevertheless, these inter-interactions remain significant and are discussed below in Sections 2.2.1 and 2.2.2.

#### 2.2.1. Inter-Bonding between Amino Acids

The amino acid—amino acid bond pair (AABP) [27] is an important parameter to study the overall interactions between amino acid residues which may be crucial to determining the conformation and structure properties of this small peptide. AABP provides an overview of twists and turns in peptides or proteins. The details of AABP are explained in the models and method section. In Table S2, we show AABP values for these 11 amino acid residues of RGD (1FUV). The TAABP can be further divided into contributions from NN and NL interactions. We can further quantify contribution from overall hydrogen bonding (HB), and subtracting it with TAABP, we can obtain contribution from remaining bonding. We also plotted the AABP contributed from nearest neighbor (NN) and non-local (NL) AAs separately in Figure 3a and contribution from hydrogen bonding and other bonding in Figure 3b.

Below are some points observed from Table S2.

Arg5 has the highest TAABP value, and its contribution is mainly from NN. In fact, Arg5 has the highest contribution from NN, NL, and HB. Coincidentally, Arg is one of the AA residues in the tripeptide RGD. In 1FUV the RGD are Arg5-Gly6-Asp7.

Gly11 has the lowest TAABP value, which is normal since Gly11 only has one NN AA residue and one NL AA residue interaction. In addition, Gly11 has the lowest contribution from HB.

Ala1 has the lowest contribution from NN, followed by Gly11. They are the first and last AA residue in the sequence and have one NN interaction each.

Asp4 has the lowest contribution from NL interaction, as it has only one NL AA residue.
Cys8 has a maximum number of NL AA residue interactions.

![](./images/1044473802802593803_5.jpg)

Figure 3. (a) TAABP for 11 AA residues showing contribution from non-local (NL) and nearest neighbor interactions (NN). (b) Contribution from hydrogen bonding and other bonding in TAABP.

Figure 3b shows that Arg5 has the highest TAABP and the highest contribution from HBs, while Gly11, with the lowest TAABP, also has the lowest contribution from HBs. As previously mentioned, Arg5 boasts the highest TAABP, a crucial factor within the context of AA from the tripeptide RGD. The RGD sequence serves as a crucial cell attachment site for various adhesive proteins found in the extracellular matrix, blood, and cell surfaces. Interestingly, more than 20 known integrins recognize this sequence within their adhesion protein ligands [28]. It is noteworthy that each of Arg5-Gly6-Asp7 exhibits two NL AA residue interactions, enabling them to actively participate in cell adhesion.

### 2.2.2. Inter-Bonding between Amino Acids and Water Molecules

Table S3 and Figure 4 focus on bonding between AA residues of RGD (1FUV) peptide and $\mathrm{H_2O}$. This analysis delves into identifying the HB within these interactions, as detailed in Table S3. Figure 4 illustrates that the contribution from HB is comparatively higher than other bonding.

![](./images/1044473802802593803_6.jpg)

Figure 4. Bond order (BO) represents the interaction between amino acid residues and water molecules.

From Table S3, it can be noticed that Cys2 has the lowest BO when interacting with H₂O, no HB interaction. Following Cys2, Cys8 has the second lowest BO when interacting with H₂O. The reasoning is the hydrophobic nature of Cys residue, and they usually isolate from the polar solvent. Coincidently, both Cys2 and Cys8 participate in disulfide bonds with Cys10 and Cys4, respectively, and have lower interactions with water. Cys residues are involved in three-dimensional structure stabilization through the formation of disulfide bridges. Following Cys2 and Cys8, Phe9 also has lower BO when interacting with H₂O due to its hydrophobic nature. On the other hand, Asp3 has the highest interactions with H₂O due to its hydrophilic nature. This analysis above gives us an overview of the impact of amino acid residue interactions at the atomistic level for the first time. However, to establish further correlations with significant implications, additional studies of this type are required.

3. Discussion

In this study, we have calculated the mechanical properties of solvated RGD (1FUV), creating a pathway of unprecedented analysis for large biomolecules. In addition, we have conducted detailed bonding analysis, including TBOD. Based on our analysis, we conclude that RGD (1FUV) is a reasonably cohesive peptide. We plan to make further ambitious connections between the mechanical properties of ultrasoft biomolecules and bonding analysis based on ab initio quantum chemical calculations.

The mechanical properties of materials are typically rather straightforward, such that a single value can represent their overall properties. However, the scenario is significantly different when considering biomolecular entities such as peptides and proteins. In biomolecules, certain regions may exhibit more flexibility than others due to the varied permutations and combinations of multiple amino acid residues. The identification of flexible and rigid regions within peptides and proteins is crucial for understanding the mechanism of protein folding [29,30]. In addition, since there is ongoing research on the mechanical properties of cancer cells, our results on the mechanical properties of RGD, which is used to target cancer cells, may provide valuable insights in this area. While we have conducted the first study to calculate the mechanical properties of a peptide, much work remains to be done. We plan to further analyze the mechanical properties of other biomolecules by leveraging the mechanical properties of amino acids. However, such analysis requires a substantial database, which is time-consuming. We plan to establish further connections with amino acids to ascertain if we can predict these values solely based on the types and specific quantities of amino acid residues present in biomolecules. We would like to emphasize that this study is foundational, and it often takes years of fundamental research before such findings become applicable. Based on the AABP study, we can quantify the bonding strength of each involved amino acid residue. Additionally, we can quantify the contribution from HB and the number of NL AA residue interactions. As such, we identified that each of Arg5-Gly6-Asp7 exhibits two NL AA residue interactions, enabling them to actively participate in cell adhesion. This could be the reason behind RGD's high affinity for integrin and its use in targeting cancer cells.

4. Conclusions

In this study, we have, for the first time, calculated mechanical properties of a solvated RGD peptide using ab initio quantum mechanical calculations. Additionally, we performed bonding analysis, including AABP and TBOD, highlighting RGD's cohesion and its relevance in cancer research due to its affinity for integrin. Our future work will extend this approach to other biomolecules, aiming to develop predictive models based on amino acid residue composition.

5. Models and Methods

The structure of RGD (1FUV) is obtained from the RCSB protein data bank (PDB) [31,32], which contains 19 models with identical compositions and numbers of atoms. We selected

the first model, which consists of 11 amino acid residues with a total of 135 atoms. The peptide is then solvated using PACKMOL software v20.15.1 [33] with the solvation shell of 3 Å and adding 155 water molecules. The RGD (1FUV) with added water molecules has a total of 600 atoms, as shown in Figure 1b. This solvated RGD (1FUV) model is optimized via the Vienna ab initio simulation package (VASP). In VASP, we used the projector aug- mented wave (PAW) [34,35] method of Perdew–Burke–Ernzerhof (PBE) [34], one of the best exchange correlation functionals within the generalized gradient approximation (GGA). We used the following input parameters: energy cutoff of 600 eV, electronic convergence of $10^{-5}$ eV, a force convergence criterion for ionic steps at $-10^{-3}$ eV/Å, and a single k-point sampling in reciprocal space. The position coordinates of the optimized structure can be found in the supplementary materials. The total energies of the initial unoptimized and final optimized structures are −2966.5835 eV and −3129.5422 eV, respectively.

The optimized structure is then used to calculate the elastic coefficients $(C_{ij})$ in VASP using the stress versus strain approach of the Nielsen and Martin scheme [36]. A strain $(\varepsilon)$ is applied to the optimized structure according to Hooks law:

$$
\sigma_{i}=\sum_{j=1}^{6} C_{i j} \varepsilon_{j} \tag{1}
$$

where stress component $\sigma_{i}$ ($i$ = 1 to 6) is linearly dependent on the applied strain $\varepsilon_{j}$ ($j$ = 1 to 6) under small deformation. The stress tensor elements (xx, yy, zz, yz, zx, and xy) are used in corresponding strain. Equation (1) gives six sets of linear equations with six components of stress and 21 elastic constants. Guided by the findings from our recent work [21], the strain percentages of ±0.25%, ±0.5%, ±0.75%, ±1%, ±1.25%, ±1.5%, ±2%, ±2.25%, and ±2.5% are chosen in this work.

The elastic constants $C_{ij}$ and corresponding compliance tensor $S_{ij}$ are then used to calculate mechanical properties using Voigt's approach, Reuss approach, and Voigt–Reuss–Hill approximation.

Voigt's approach [37] gives the upper limit of bulk modulus $K_{Voight}$ and shear modulus $G_{Voight}$

$$
K_{Voigt}=\frac{1}{9}\left(C_{11}+C_{22}+C_{33}\right)+\frac{2}{9}\left(C_{12}+C_{13}+C_{23}\right) \tag{2}
$$

$$
G_{\text {Voight }}=\frac{1}{15}\left(C_{11}+C_{22}+C_{33}-C_{12}-C_{13}-C_{23}\right)+\frac{1}{5}\left(C_{44}+C_{55}+C_{66}\right) \tag{3}
$$

Reuss's approach [38] gives the lower limit of bulk modulus $K_{Reuss}$ and shear modulus $G_{Reuss}$

$$
K_{\text {Reuss }}=\frac{1}{\left(S_{11}+S_{22}+S_{33}\right)+2\left(S_{12}+S_{13}+S_{23}\right)} \tag{4}
$$

$$
G_{\text {Reuss }}=\frac{15}{4\left(S_{11}+S_{22}+S_{33}\right)-4\left(S_{12}+S_{13}+S_{23}\right)+3\left(S_{44}+S_{55}+S_{66}\right)} \tag{5}
$$

Hill's approach is the average of Voigt and Reuss approaches known as Voight–Reuss–Hill approximation (VRH) [39].

$$
K=\frac{K_{\text {Voight }}+K_{\text {Reuss }}}{2} \tag{6}
$$

$$
G=\frac{G_{\text {Voight }}+G_{\text {Reuss }}}{2} \tag{7}
$$

$$
E=\frac{9 K G}{3 K+G} \tag{8}
$$

$$
\eta=\frac{3 K-2 G}{2(3 K+G)} \tag{9}
$$

where, $E$ is Young's modulus and $\eta$ is Poisson's ratio.

The optimized structure is then used as the input to the in house developed OLCAO (orthogonalized linear combination of atomic orbitals) package [40] for interatomic bonding calculations. The bond order (BO) values $\rho_{\alpha \beta}$ between any pairs of atoms are obtained from the ab initio wave functions with atomic basis expansion.

$$
\rho_{\alpha \beta}=\sum_{m, o c c} \sum_{i, j} C_{i \alpha}^{* m} C_{j \beta}^{m} S_{i \alpha, j \beta}
\tag{10}
$$

In the above equations, $S_{i \alpha, j \beta}$ are the overlap integrals between the $i$ th orbital in the $\alpha$ th atom and the $j$ th orbital in the $\beta$ th atom. $C_{j \beta}^{m}$ are the eigenvector coefficients of the $m$ th occupied molecular orbital. The BO quantifies the strength of the bond between two atoms and usually scales with the bond length (BL), but is also influenced by the surrounding atoms. The calculation of BO is based on the Mulliken scheme [41,42], hence is basis-dependent.

Total bond order density (TBOD) serves as a quantum mechanical metric utilized in material science to assess the internal cohesion of materials. TBOD is obtained by normalizing the total BO within cell volume. This work marks the first application of TBOD to biomolecules.

As is well-known, amino acids (AAs), being the basic units of proteins, are in some kind of sequential order in biomolecules. However, the interactions between them are not just with the nearest neighbor (NN) pairs (i.e., AA residues in primary sequence). In biomolecules, there are non-local (NL) interactions too. NL interaction is between AA residues that are not NN in the primary sequence but also from other nearby non-negligible bonds, which form the twists and turns in biomolecules.

We now extend our formulation and analysis of BO to amino acid-amino acid bond pair (AABP) [27]

$$
A A B P(u, v)=\sum_{\alpha \in u} \sum_{\beta \in v} \rho_{\alpha i, \beta j}
\tag{11}
$$

where the summations are over all atoms $\alpha$ in $A A u$ and all atoms $\beta$ in $A A v$. This novel concept of $A A B P$ considers all bonding between two amino acid residues, including both covalent and hydrogen bonding. $A A B P$ is a single parameter that quantifies the interaction between two AA residues. The stronger the interaction, the larger will be the $A A B P$ and vice versa. $A A B P$ can be further resolved in NN and NL bonding.

Supplementary Materials: The following supporting information can be downloaded at: https://www.mdpi.com/article/10.3390/ijms251810164/s1.

Author Contributions: W.-Y.C. conceived the study. P.A. conducted the calculations and wrote the initial draft. W.-Y.C., P.A. and B.J. participated in editing and writing the manuscript. All authors have read and agreed to the published version of the manuscript.

Funding: This research used the resources of the National Energy Research Scientific Computing Center (NERSC), a DOE office of Science User Facility supported by the Office of Science of the U.S. Department of Energy by U.S. Department of Energy under the contract number DE-AC03-76SF00098, DE-AC02-05CH11231 using NERSC award NERSC DDR-ERCAP0023727, and the Research Computing Support Services (RCSS) of the University of Missouri System.

Institutional Review Board Statement: Not applicable.

Informed Consent Statement: Not applicable.

Data Availability Statement: The data supporting the findings of this study are available within the article and Supplementary Materials.

Conflicts of Interest: The authors declare no conflicts of interest.

## References

1.  Szpotkowski, K.; Wójcik, K.; Kurzyńska-Kokorniak, A. Structural studies of protein–nucleic acid complexes: A brief overview of the selected techniques. *Comput. Struct. Biotechnol. J.* 2023, 21, 2858–2872. [CrossRef] [PubMed]

2.  Jonchhe, S.; Pandey, S.; Emura, T.; Hidaka, K.; Hossain, M.A.; Shrestha, P.; Sugiyama, H.; Endo, M.; Mao, H. Decreased water activity in nanoconfinement contributes to the folding of G-quadruplex and i-motif structures. *Proc. Natl. Acad. Sci. USA* 2018, 115, 9539–9544. [CrossRef] [PubMed]

3.  Camilloni, C.; Bonetti, D.; Morrone, A.; Giri, R.; Dobson, C.M.; Brunori, M.; Gianni, S.; Vendruscolo, M. Towards a structural biology of the hydrophobic effect in protein folding. *Sci. Rep.* 2016, 6, 28285. [CrossRef] [PubMed]

4.  Degtyarenko, I.M.; Nieminen, R.M. Dynamics of biomolecules from first principles. In *Science and Technology of Atomic, Molecular, Condensed Matter & Biological Systems*; Elsevier: Amsterdam, The Netherlands, 2010; Volume 1, pp. 557–573.

5.  Yang, L.-Q.; Sang, P.; Tao, Y.; Fu, Y.-X.; Zhang, K.-Q.; Xie, Y.-H.; Liu, S.-Q. Protein dynamics and motions in relation to their functions: Several case studies and the underlying mechanisms. *J. Biomol. Struct. Dyn.* 2014, 32, 372–393. [CrossRef]

6.  Bao, G. Protein mechanics: A new frontier in biomechanics. *Exp. Mech.* 2009, 49, 153–164. [CrossRef]

7.  Wang, N.; Butler, J.P.; Ingber, D.E. Mechanotransduction across the cell surface and through the cytoskeleton. *Science* 1993, 260, 1124–1127. [CrossRef]

8.  Vogel, V.; Sheetz, M. Local force and geometry sensing regulate cell functions. *Nat. Rev. Mol. Cell Biol.* 2006, 7, 265–275. [CrossRef]

9.  Howard, J. Mechanics of motor proteins. In *Physics of Bio-Molecules and Cells. Physique des Biomolécules et des Cellules: Session LXXV. 2–27 July 2001*; Springer: Berlin/Heidelberg, Germany, 2002; pp. 69–94.

10. Block, S.M.; Goldstein, L.S.; Schnapp, B.J. Bead movement by single kinesin molecules studied with optical tweezers. *Nature* 1990, 348, 348–352. [CrossRef]

11. Stossel, T.P. On the crawling of animal cells. *Science* 1993, 260, 1086–1094. [CrossRef]

12. Pelham, R.J., Jr.; Wang, Y.-L. Cell locomotion and focal adhesions are regulated by substrate flexibility. *Proc. Natl. Acad. Sci. USA* 1997, 94, 13661–13665. [CrossRef]

13. Discher, D.E.; Janmey, P.; Wang, Y.-L. Tissue cells feel and respond to the stiffness of their substrate. *Science* 2005, 310, 1139–1143. [CrossRef] [PubMed]

14. Alibert, C.; Goud, B.; Manneville, J.B. Are cancer cells really softer than normal cells? *Biol. Cell* 2017, 109, 167–189. [CrossRef] [PubMed]

15. Raveh Tilleman, T.; Tilleman, M.; Neumann, H. The elastic properties of cancerous skin: Poisson’s ratio and Young’s modulus. *Optim. Incisions Cutan. Surg. Incl. Mohs’ Microgr. Surg.* 2004, 105, 753–755.

16. Kashani, A.S.; Packirisamy, M. Cancer cells optimize elasticity for efficient migration. *R. Soc. Open Sci.* 2020, 7, 200747. [CrossRef]

17. Adhikari, P.; Wen, A.M.; French, R.H.; Parsegian, V.A.; Steinmetz, N.F.; Podgornik, R.; Ching, W.-Y. Electronic structure, dielectric response and surface charge distribution of RGD (1FUV) peptide. *Sci. Rep.* 2014, 4, 5605. [CrossRef]

18. Garanger, E.; Boturyn, D.; Dumy, P. Tumor targeting with RGD peptide ligands-design of new molecular conjugates for imaging and therapy of cancers. *Anti-Cancer Agents Med. Chem.* 2007, 7, 552–558. [CrossRef] [PubMed]

19. Metcalfe, A.D.; Ferguson, M.W. Tissue engineering of replacement skin: The crossroads of biomaterials, wound healing, embryonic development, stem cells and regeneration. *J. R. Soc. Interface* 2007, 4, 413–437. [CrossRef]

20. Meyers, S.R.; Grinstaff, M.W. Biocompatible and bioactive surface modifications for prolonged in vivo efficacy. *Chem. Rev.* 2012, 112, 1615–1632. [CrossRef]

21. Adhikari, P.; Jawad, B.; Ching, W.-Y. Mechanical Properties of Super-soft Biomolecular Systems: Application to Twenty Solvated Canonical Amino Acids. *BME Horiz.* 2023, 1. [CrossRef]

22. Corbin, E.A.; Kong, F.; Lim, C.T.; King, W.P.; Bashir, R. Biophysical properties of human breast cancer cells measured using silicon MEMS resonators and atomic force microscopy. *Lab A Chip* 2015, 15, 839–847. [CrossRef]

23. Adhikari, P.; Khaoulaf, R.; Ez-Zahraouy, H.; Ching, W.-Y. Complex interplay of interatomic bonding in a multi-component pyrophosphate crystal: $K_2Mg (H_2P_2O_7)_2 2H_2O$. *R. Soc. Open Sci.* 2017, 4, 170982. [CrossRef] [PubMed]

24. Dharmawardhana, C.; Misra, A.; Ching, W.-Y. Quantum mechanical metric for internal cohesion in cement crystals. *Sci. Rep.* 2014, 4, 7332. [CrossRef]

25. Baral, K.; Ching, W.-Y. Electronic structures and physical properties of $Na_2O$ doped silicate glass. *J. Appl. Phys.* 2017, 121, 245103. [CrossRef]

26. Shafei, L.; Adhikari, P.; San, S.; Ching, W.-Y. Electronic Structure and Mechanical Properties of Solvated Montmorillonite Clay Using Large-Scale DFT Method. *Crystals* 2023, 13, 1120. [CrossRef]

27. Adhikari, P.; Ching, W.-Y. Amino acid interacting network in the receptor-binding domain of SARS-CoV-2 spike protein. *RSC Adv.* 2020, 10, 39831–39841. [CrossRef] [PubMed]

28. Ruoslahti, E. RGD and other recognition sequences for integrins. *Annu. Rev. Cell Dev. Biol.* 1996, 12, 697–715. [CrossRef]

29. Hammarström, P.; Carlsson, U. Is the unfolded state the Rosetta Stone of the protein folding problem? *Biochem. Biophys. Res. Commun.* 2000, 276, 393–398. [CrossRef]

30. Fersht, A.R. Nucleation mechanisms in protein folding. *Curr. Opin. Struct. Biol.* 1997, 7, 3–9. [CrossRef]

31. Assa-Munt, N.; Jia, X.; Laakkonen, P.; Ruoslahti, E. Solution structures and integrin binding activities of an RGD peptide with two isomers. *Biochemistry* 2001, 40, 2373–2378. [CrossRef]

32. Solution Structure of an RGD Peptide Isomer-A. Available online: https://www.rcsb.org/structure/1FUV (accessed on 16 May 2001).

33. Martínez, L.; Andrade, R.; Birgin, E.G.; Martínez, J.M. PACKMOL: A package for building initial configurations for molecular dynamics simulations. J. Comput. Chem. 2009, 30, 2157-2164. [CrossRef]

34. Perdew, J.P.; Burke, K.; Ernzerhof, M. Generalized gradient approximation made simple. Phys. Rev. Lett. 1996, 77, 3865. [CrossRef] [PubMed]

35. Kresse, G.; Joubert, D. From ultrasoft pseudopotentials to the projector augmented-wave method. Phys. Rev. B 1999, 59, 1758. [CrossRef]

36. Nielsen, O.; Martin, R.M. First-principles calculation of stress. Phys. Rev. Lett. 1983, 50, 697. [CrossRef]

37. Voigt, W. Lehrbuch der Kristallphysik (mit Ausschluss der Kristalloptik); Teubner, B.G., Edwards, J.W., Eds.; Springer: Leipzig und Berlin, Germany, 1928.

38. Reuß, A. Berechnung der fließgrenze von mischkristallen auf grund der plastizitätsbedingung für einkristalle. ZAMM J. Appl. Math. Mech. Z. Für Angew. Math. Und Mech. 1929, 9, 49-58. [CrossRef]

39. Hill, R. The elastic behaviour of a crystalline aggregate. Proc. Phys. Society. Sect. A 1952, 65, 349. [CrossRef]

40. Ching, W.-Y.; Rulis, P. Electronic Structure Methods for Complex Materials: The Orthogonalized Linear Combination of Atomic Orbitals; OUP Oxford: London, UK, 2012.

41. Mulliken, R.S. Electronic population analysis on LCAO-MO molecular wave functions. I. J. Chem. Phys. 1955, 23, 1833-1840. [CrossRef]

42. Mulliken, R. Electronic population analysis on LCAO-MO molecular wave functions. II. Overlap populations, bond orders, and covalent bond energies. J. Chem. Phys. 1955, 23, 1841-1846. [CrossRef]

Disclaimer/Publisher's Note: The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content.
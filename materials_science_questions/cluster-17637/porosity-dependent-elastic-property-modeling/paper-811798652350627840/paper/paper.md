# Shaping the micromechanical behavior of multi-phase composites
for bone tissue engineering

Shivakumar I. Ranganathan $^{a}$, Diana M. Yoon $^{b}$, Allan M. Henslee $^{d}$, Manitha B. Nair $^{b}$, Christine Smid $^{a}$,
F. Kurtis Kasper $^{b}$, Ennio Tasciotti $^{a}$, Antonios G. Mikos $^{b}$, Paolo Decuzzi $^{a,c,*}$, Mauro Ferrari $^{a,b,d}$

$^{a}$ Department of Nanomedicine and Biomedical Engineering, The University of Texas Health Science Center, Houston, TX, USA
$^{b}$ Department of Bioengineering, Rice University, Houston, TX, USA
$^{c}$ BioNEM, University of Magna Graecia, Catanzaro, Italy
$^{d}$ Department of Experimental Therapeutics, The University of Texas M.D. Anderson Cancer Center, Houston, TX, USA

---

## ARTICLE INFO

**Article history:**
Received 1 December 2009
Received in revised form 26 February 2010
Accepted 19 March 2010
Available online 24 March 2010

**Keywords:**
Biocomposite
Particle shape
Elastic properties
Scaffold

## ABSTRACT

Mechanical stiffness is a fundamental parameter in the rational design of composites for bone tissue engi- neering in that it affects both the mechanical stability and the osteo-regeneration process at the fracture site. A mathematical model is presented for predicting the effective Young's modulus $(E)$ and shear mod ulus $(G)$ of a multi-phase biocomposite as a function of the geometry, material properties and volume concentration of each individual phase. It is demonstrated that the shape of the reinforcing particles may dramatically affect the mechanical stiffness: $E$ and $G$ can be maximized by employing particles with large geometrical anisotropy, such as thin platelet-like or long fibrillar-like particles. For a porous poly(propylene fumarate) (60% porosity) scaffold reinforced with silicon particles (10% volume concen- tration) the Young's (shear) modulus could be increased by more than 10 times by just using thin plate- let-like as opposed to classical spherical particles, achieving an effective modulus $E \sim 8$ GPa $(G \sim 3.5$ GPa). The mathematical model proposed provides results in good agreement with several experimental test cases and could help in identifying the proper formulation of bone scaffolds, reducing the development time and guiding the experimental testing.

© 2010 Acta Materialia Inc. Published by Elsevier Ltd. All rights reserved.

---

### 1. Introduction

Among the several approaches proposed and currently under investigation for bone tissue engineering the most promising strat- egy is based on the design, synthesis and application of three- dimensional (3D) polymeric matrices incorporating cells and bio- active molecules [1-4]. Such an assembly, generally referred to as a 3D scaffold, tends to bio-mimic the structure and biology of the original tissue. Differently from classical orthopedic implants, engineered bone scaffolds must be rationally designed to provide mechanical stability, post-traumatic osteo-regeneration and com- plete fracture healing with the deposition of normal, healthy bone in a timely fashion. For this, an optimal scaffold should have mechanical properties similar to those of the original bone, de- grade in a predictable fashion with low toxicity, cause minimal for- eign body response, favor the adhesion, integration, differentiation and proliferation of the harvested cells and support angiogenesis and the formation of new bone tissue tuned to time with the deg- radation dynamics [5,6]. In this respect, scaffolds for bone engi- neering can be considered as multifunctional and multi-phase biomedical devices operating over multiple length scales, from the molecular level, where bioactive molecules promote new bone formation, to the macroscopic scale, where the whole assembly is designed to support external mechanical loads.

The rational design of bone scaffolds is a complex multi-objec- tive optimization problem with constraints of a different nature. For instance, the mechanical stiffness of a scaffold should be se- lected by considering both mechanical stability and osteo-regener- ation at the site of the defect. In the absence of an external fixator system the first objective would ideally require scaffolds matching the biomechanical properties of healthy bone, which in the case of human cortical bone would lead to a compressive modulus $E \sim 18-$ 20 GPa [7]. On the other hand, if an external fixator system is em- ployed, which is often the case to provide stabilization to the frac- ture site, scaffolds with lower compressive moduli can be employed. Conversely, the second objective would require scaf- folds with high interconnected porosity, to support cell recruit- ment and migration to the fracture site, and sufficient mechanical compliance, in that locally the formation of healthy bone is favored by microstrain fields of the order of $\sim 100-5000$ [8,9]. Metal implants have succeeded in providing optimal

---

* Corresponding author at: Department of Nanomedicine and Biomedical Engi- neering, The University of Texas Health Science Center, Houston, TX, USA. Tel.: +1 713 500 3363.
E-mail address: paolo.decuzzi@uth.tmc.edu (P. Decuzzi).

1742-7061/$ - see front matter © 2010 Acta Materialia Inc. Published by Elsevier Ltd. All rights reserved.
doi:10.1016/j.actbio.2010.03.029

mechanical stability but have failed in supporting extensive and effective bone tissue regeneration and implant integration [10]. On the other hand, biodegradable natural polymers (alginate, chitosan, collagen and silk) and synthetic polymers [poly(α-hydroxy esters), poly(propylene fumarate) (PPF) and poly(hydroxy-alk- anoates)] have been shown in several biomedical applications to support effective tissue regeneration but are generally character- ized by low mechanical properties compared with healthy bone [11].

In an attempt to find the right balance between mechanical sta- bility and new bone deposition several biocomposite materials have been proposed and characterized over the last decade by combining natural and synthetic polymeric matrices reinforced with stiffer micro/nanoparticles [12]. Generally, in these applica- tions the role played by the stiffer particles is twofold: enhance- ment of the mechanical properties of the polymer matrix (reinforcement) and controlled release of bioactive molecules for the recruitment of cells and the deposition of new bone crystals (drug delivery). Particles with different geometrical features and material properties have been reported, such as hydroxyapatite (HA) nanofibers with a characteristic length of 100-300 nm and an aspect ratio (longer by shorter axis) of 3-5 [13-17], bioactive glasses beads (BG) of spherical shape with a diameter ranging be- tween 200 and 600 μm [18], calcium phosphate (CaP) composite microspheres with a diameter of 100-300 μm [19], single walled carbon nanotubes (SWNTs) with a diameter of ~1 nm and aspect ratios ranging from 5 up to several thousand [20,21], mesoporous silica spherical particles with diameters of a few hundred nanome- ters [22] and other man-made reinforcing micro/nanoparticles.

The list presented above, far from being comprehensive, has the merit of emphasizing the large variety of combinations so far pro- posed and potentially still available for bone substitute compos- ites. The overall mechanical properties of the biocomposite can be tailored by selecting the mechanical properties, porosity and pore interconnectivity of the polymer matrix and the geometry (size and shape), physico-chemical properties and concentration of each individual reinforcing particle. Clearly, the number of pos- sible combinations is enormous and predictive tools could help in identifying proper formulations of the bone scaffold limiting expensive experimental testing and reducing the development time.

In this spirit, a mathematical model for predicting the Young's and shear moduli of multi-phase composites to be used as bone substitutes is presented here. The model takes into account the contribution of the shape, material properties and volume concen- tration of each individual phase. The theoretical predictions are shown to be in good agreement with the experimental results al- ready available in the literature for poly(lactic-co-glycolic acid)- hydroxyapatite (PLGA-HA) composites [13,14]. Additional experi- mental validation is provided by comparing the theoretical predic- tions with the compressive modulus of porous PPF alone and PPF mixed with silica microbeads.

## 2. Materials and methods

### 2.1. Mathematical formulation and geometrical anisotropy

Within the realm of effective medium (EM) theories, the equiv- alent poly-inclusion (EPI) approach [23] is employed to predict the elastic properties of a multi-phase biocomposite material. The EPI approach represents a unique development in homogenization theory, in that its predictions remain admissible and valid for any material symmetry groups of the phases, any orientation dis- tribution and any fiber shape and volume fraction. As sketched in Fig. 1, the system is made up of a continuous polymer matrix (phase I) with pores (phase II) and reinforcing particles (phase

![](./images/811798652350627840_1.jpg)

Fig. 1. Schematic presenting silicon particles (NSE) and pores embedded in a polymer matrix (PPF).

III). The pores and particles have arbitrary shapes and are randomly oriented, in which case the EPI approach coincides with the Mori- Tanaka theory [24]. Within the model proposed pores are treated as particles having zero stiffness.

In the case of a bi-phasic composite, comprising a matrix with stiffness tensor $\mathbf{C}^{\mathrm{m}}$ and particles with stiffness tensor $\mathbf{C}^{\mathrm{f}}$ and vol ume concentration $\alpha$, the resulting effective stiffness tensor $\mathbf{C}$ of the material can be expressed as [23]:

$$
\mathbf{C}=\mathbf{C}^{\mathrm{m}}+\alpha\left\langle\left(\mathbf{C}^{\mathrm{f}}-\mathbf{C}^{\mathrm{m}}\right) \hat{\mathbf{T}}\right\rangle \tag{1}
$$

where the operator $\langle\bullet\rangle$ indicates the orientational averaging defined as follows on any fourth rank tensor $\mathfrak{I}$:

$$
\langle\mathfrak{I}\rangle=\frac{1}{8 \pi^{2}} \int_{0}^{\pi} \int_{0}^{2 \pi} \int_{0}^{2 \pi} \prod(\mathfrak{I}) f\left(\psi_{1}, \phi, \psi_{2}\right) \sin \varphi d \psi_{1} d \psi_{2} d \varphi \tag{2}
$$

where $(\psi_{1}, \phi, \psi_{2})$ represent the triad of Euler angles, $f(\psi_{1}, \varphi, \psi_{2})$ rep resents an appropriate orientation probability density function [$f(\psi_{1}, \varphi, \psi_{2})=1$ for uniformly distributed fibers] and $\prod(\bullet)$ indicates the frame change operator as defined in [25]. The tensor $\hat{\mathbf{T}}$ is defined as

$$
\hat{\mathbf{T}}=\left[\mathbf{I}+\hat{\mathbf{E}}\left(\mathbf{C}^{\mathrm{m}}\right)^{-1}\left(\mathbf{C}^{\mathrm{f}}-\mathbf{C}^{\mathrm{m}}\right)\right]^{-1} \tag{3}
$$

with $\mathbf{I}$ being the fourth rank identity tensor and $\hat{\mathbf{E}}$ a strain concen- trator tensor defined as:

$$
\hat{\mathbf{E}}=(1-\alpha) \mathbf{E} \tag{4}
$$

within EPI theory. The tensor $\mathbf{E}$ represents the celebrated Eshelby's tensor [26,27] accounting for the shape of the particle. In the case of an isolated ellipsoidal particle embedded in an infinite matrix Eq. (3) becomes the well-known Eshelby relation:

$$
\mathbf{T}=\left[\mathbf{I}+\mathbf{E}\left(\mathbf{C}^{\mathrm{m}}\right)^{-1}\left(\mathbf{C}^{\mathrm{f}}-\mathbf{C}^{\mathrm{m}}\right)\right]^{-1} \tag{5}
$$

Eqs. (1)-(4) provide the mathematical framework for predicting the effective elastic properties of a bi-phasic composite as a func- tion of the shape of the particle (captured by the tensor $\mathbf{E}$ ), the material properties of the particle $(\mathbf{C}^{\mathrm{f}})$, the volume concentration of the particle $(\alpha)$ and the material properties of the matrix $(\mathbf{C}^{\mathrm{m}})$.

In the case of a three-phase composite, as for a porous (non- dense) polymeric matrix with reinforcing particles, the resulting effective stiffness tensor $\mathbf{C}$ of the material can be derived by apply- ing the set of Eqs. (1)-(4) twice. That is to say, first, Eqs. (1)-(4) are applied to the bi-phasic composite comprising the dense polymeric matrix (phase I) and the pores (particles with zero stiffness, phase

II), providing the effective elastic properties for the porous (non-dense) polymer matrix; second, Eqs. (1)-(4) are applied to the biphasic composite comprising the porous polymeric matrix (phases I and II) previously analyzed and the stiffer particles (phase III). In the case of a multi-phase composite the procedure described above can be applied as many times as needed to derive the effective properties of the assembly.

Although the problem identified by Eqs. (1)-(4) can be applied to particles of any arbitrary shape, here the analysis is limited to ellipsoidal pores and stiffer particles with semi-principal axis $a_1$, $a_2$ and $a_3$. Without losing generality, $a_3$ is fixed as unity ($a_3=1$) and the aspect ratios $k_1=(a_1/a_3)$ and $k_2=(a_2/a_3)$ are introduced as independent parameters unequivocally identifying the shape of the particle. Thus, elongated prolate spheroids are considered for $k_1,k_2 \ll 1$, thin oblate spheroids for $k_1,k_2 \gg 1$ and the classical spherical shape for $k_1=k_2=1$. Motivated by the definition of material anisotropy index recently proposed by Ranganathan and Ostoja-Starzewski [28], a parameter $A$ is introduced to quantify the departure of the inclusion shape (geometrical anisotropy) from that of a sphere (representing geometrically isotropic particle) (see also [29]).

$$
A=3\left(\frac{a^{\mathrm{AM}}}{a^{\mathrm{HM}}}-1\right) \geqslant 0 \tag{6}
$$

where $a^{\mathrm{AM}}=(a_1+a_2+a_3)/3$ and $a^{\mathrm{HM}}=3(a_1^{-1}+a_2^{-1}+a_3^{-1})^{-1}$ represent the arithmetic mean and the inverse harmonic mean of the semi-principal axis. Rewriting Eq. (6) in terms of the aspect ratios $k_1$and $k_2$, it follows that:

$$
A=\left(1+k_1+k_2\right)\left(1+k_1^{-1}+k_2^{-1}\right) / 3-3 \geqslant 0 \tag{7}
$$

Note that the parameter $A$ can only quantify the departure of the particle shape from sphericity and cannot explicitly discriminate between prolate and oblate particles. The geometrical anisotropy $A$ is infinitely large in the case of flat discoidal particles $(k_1,k_2 \to \infty,\dots$ platelet-like particles) and for thin long particles $(k_1,k_2 \to \infty,\dots$ fiber-like particles), while it is 0 for a spherical particle.

### 2.2. Poly(propylene fumarate) synthesis

Poly(propylene fumarate) (PPF) was synthesized by a two-step reaction as previously described [30-32]. The polymer was characterized by $^1$H nuclear magnetic resonance (Bruker, Billerica, MA) and gel permeation chromatography (Model 410, Waters, Milford, MA). The number average molecular weight was approximately 3000, with a polydispersity index ranging from 1.42 to 1.58.

### 2.3. Porous PPF scaffolds

PPF scaffolds were created by mixing PPF and $N$-vinyl pyrrolidone (NVP) at a 1:1 wt.% ratio with a porogen. The two types of porogens used were carboxymethylcellulose (CMC) (10% and 15% w/v in water) and NaCl (300-500 $\mu$m). The porogen concentration ranged from 10 to 90 wt.% in the polymer mixture. The scaffolds were cross-linked with 2% w/v benzoyl peroxide and 0.025% v/w $N,N$-dimethyl-$p$-toluidine (DMT). The mixture was poured into a cylindrical Teflon mold (15 mm height $\times$ 6 mm diameter) and placed in a $60\ ^{\circ}\text{C}$ oven overnight. The scaffolds were cut into $12 \times 6$ mm cylinders and leached for 1-3 days in distilled water. All scaffolds were kept in distilled water until testing and were hydrated during testing. NVP, benzoyl peroxide and DMT were purchased from Sigma-Aldrich (St Louis, MO); CMC was purchased from Spectrum (Gardena, CA) and NaCl was purchased from Fisher Scientific (Pittsburgh, PA). All reagents were used as received.

### 2.4. PPF-silica composite scaffold

3-Trimethoxysililpropylmethacrylate-modified 100 nm silica particles at two different concentrations (5 and 10 wt.%) were mixed with NVP and then sonicated for 30 min. PPF was then combined with this mixture so that a 2:1 w/w PPF:NVP ratio was achieved. The scaffolds were cross-linked by mixing in 2% w/v benzoyl peroxide. This composite mixture was then poured into a cylindrical Teflon mold as indicated above and placed in a $60\ ^{\circ}\text{C}$ oven overnight. The scaffolds were cut into $12 \times 6$ mm cylinders ready for MTS testing. The 3-trimethoxysililpropylmethacrylate silane was purchased from Sigma-Aldrich (St Louis, MO) and the 100 nm non-porous colloidal silica particles were purchased from Polysciences (Warrington, PA).

### 2.5. Mechanical testing

All samples ($n=5$) underwent compressive mechanical testing following the ASTM International Standard D695-08 using an MTS 858 Mini Bionix (MTS System Corp., Eden Prairie, MN). A 10 kN load cell with a $1.3\ \text{mm}\ \text{min}^{-1}$ cross-head speed was used. The compressive modulus was calculated by determining the linear elastic slope of the stress-strain curve, where stress was defined as force divided by cross-sectional area and strain was defined as change in displacement divided by the original displacement of the scaffold.

## 3. Theoretical results

The mathematical model presented is used to estimate the Young's modulus $E$ and shear elastic modulus $G$ for three cases of practical interest: (i) a matrix of PPF with ellipsoidal pores (bi-phasic composite); (ii) a dense matrix of PPF with silicon ellipsoidal particles (bi-phasic composite); (iii) a porous matrix of PPF with silicon ellipsoidal particles (SiMPs) (three-phase composite).

In bone tissue engineering PPF has been widely studied [33] because it is well accepted in vivo [34], supports bone formation [35] and degrades over time in the body to natural products that can be safely and efficaciously excreted [36]. Mesoporous silicon particles embedded in a polymer matrix can be effectively used as reinforcing particles and drug delivery systems [37]. Also, porous silicon has been shown to be biocompatible [38] and biodegradable [39], with degradation dynamics that can be controlled by porosity and surface terminations. The material properties of PPF and silicon are listed in Table 1.

### 3.1. Polymeric matrix with geometrically anisotropic pores

The formation of new healthy bone depends on a well-defined hierarchy of different cell types, among which are multipotent skeletal stem cells (mesenchymal stem cells, MSC), which need to be recruited to the fracture site, have to infiltrate and migrate within the scaffold, adhere and proliferate [40]. The formation of new vessels also needs to be supported, for the continuous supply of nutrients via the blood system, without which the newly formed tissue degenerates and dies [41]. For this, scaffolds for bone tissue

**Table 1**
Material properties used to calculate the elastic response of the PPF-Si composite, as compared with human cortical bone [4].

| Material                     | Shear modulus $G$ (GPa) | Young's modulus $E$ (GPa) |
|------------------------------|-------------------------|---------------------------|
| Silicon                      | 67                      | 164                       |
| Poly(propylene fumarate)     | 0.77                    | 2.0                       |
| Human cortical bone          | ~8                      | ~20                       |

engineering have to be porous with a highly interconnected network of pores.

In the present mathematical models the pores are considered as softer particles ($\mathbf{C}^\mathrm{f}=0$) compared with the polymer matrix. It is expected that the mechanical properties of the matrix will decrease as the volume concentration $\alpha_\mathrm{p}$ of pores increases (increase in porosity). Indeed, this is shown in Fig. 2, where the elastic modulus $E$ is plotted against $\alpha_\mathrm{p}$ in the case of spherical pores. For $\alpha_\mathrm{p}=0$ the original modulus of the dense (non-porous) PPF formulation considered is seen ($E=2$ GPa from Table 1), whereas for $\alpha_\mathrm{p}$ tending to unity $E$ tends to 0. It is important to emphasize that for a porosity in the range 50-70% ($\alpha_\mathrm{p}=0.5$-$0.7$), which are the values traditionally used in such applications, the elastic modulus $E$ drops by almost half, from 665.8 to 352.4 MPa.

Far less intuitive is the role played by pore shape on the mechanical response of the composite. This is demonstrated in Fig. 3, where iso-contours for the elastic modulus $E$ are plotted for different values of the aspect ratios $k_1$ and $k_2$ of an ellipsoidal pore and for $\alpha_\mathrm{p}=0.1$. The porous matrix presents an absolute maximum in stiffness for spherical pores ($k_1=k_2=1$), whereas $E$ decreases steadily as the pore shape deviates from sphericity in the direction of either prolate ($k_1,k_2<1$) or oblate ellipsoid ($k_1,k_2>1$). Similar observations can be drawn for different porosities $\alpha_\mathrm{p}$. The combined effect of pore geometry, characterized by the geometrical anisotropy parameter $A$, and volume concentration ($\alpha_\mathrm{p}$) is shown in Fig. 4. Here iso-contours of the effective modulus for prolate pores ($E_\mathrm{P}$) and oblate pores ($E_\mathrm{O}$), normalized with respect to the case of spherical pores $E_\mathrm{S}$, are plotted against $\alpha_\mathrm{p}$ and $A$. Interestingly, for prolate pores (Fig. 4a) the ratio $E_\mathrm{P}/E_\mathrm{S}$ is relatively close to unity for the range of porosities and geometrical anisotropy considered, whereas for oblate pores (Fig. 4b) a dramatic decrease in elastic modulus over a wide range of porosity ($\alpha_\mathrm{p}=0.1$-$0.9$) was observed as $A$ became larger than 100 ($k_1=k_2>150$, thin discoidal pores). This would suggest that ovoidal pores interconnected with tubular-like pores could alleviate the reduction in mechanical properties inevitably associated with polymer porosity.

### 3.2. Dense polymeric matrix reinforced with geometrically anisotropic particles

The elastic modulus of dense (non-porous) synthetic polymers is at most a few GPa, much larger than the modulus of natural polymers. Depending on the chemical modification and geometry of the samples, poly-ʟ-lactide (PLLA) has the largest compressive stiffness, with $E$ 10-16 GPa, followed by polyglycolide (PGA), with $E$ 7-14 GPa, and PPF, offering on average an $E$ 1-2 GPa. As previously observed, these values decrease dramatically with porosity. Also, stiffer polymers have been associated with different levels of toxicity and long degradation times [8], thereby limiting their utility in bone tissue scaffolds.

![](./images/811798652350627840_2.jpg)

Fig. 2. The Young's modulus $E$ as a function of pore concentration $\alpha_\mathrm{p}$ (i.e. porosity). The pores are spherical ($k_1=k_2=1$ or $A=0$).

![](./images/811798652350627840_3.jpg)

Fig. 3. Iso-contour plot for the Young's modulus $E$ of porous PPF as a function of the aspect ratios $k_1=a_1/a_3$ and $k_2=a_2/a_3$ of an ellipsoidal pore (polymer matrix porosity $\alpha_\mathrm{p}=10\%$).

In Fig. 5 the elastic modulus $E$ of a PPF-SiMP composite is plotted against the volume concentration $\alpha_\mathrm{s}$ of spherical silicon particles (SiMP) for a non-porous PPF. In the limit $\alpha_\mathrm{s}=0$ the original properties of dense PPF are recovered ($E=2$ GPa from Table 1), whereas for $\alpha_\mathrm{s}=1$ the elastic modulus of silicon is obtained. Indeed, it is confirmed that an increase in silicon concentration leads to an increase in $E$. The effect of particle shape is demonstrated in Fig. 6, where the iso-contours for $E$ are plotted against the aspect ratios $k_1$ and $k_2$ of an ellipsoid particle. Notably, for stiffer particles the contribution of shape is the opposite of that of the case of softer particles (pores): the maximum stiffening effect is obtained by dispersing non-spherical particles within the polymer matrix and the larger the deviation from sphericity (larger $k_1$ and $k_2$ or geometrical anisotropy), the larger is the increase in $E$. The combined effects of particle geometry, characterized by the parameter $A$, and concentration ($\alpha_\mathrm{s}$) are shown in Fig. 7. Here iso-contours of the effective modulus $E_\mathrm{P}$ for prolate particles and $E_\mathrm{O}$ for oblate particles, normalized with respect to the case of spherical particles $E_\mathrm{S}$, are plotted against $\alpha_\mathrm{s}$ and $A$. Again, in contrast to the case of pores, both prolate and oblate particles significantly increased the mechanical response of the composite, although oblate particles tended to give larger values of $E$ as $A$ increased above 100 ($k_1=k_2>150$, platelet-like or fiber-like particles). This would suggest that highly anisotropic stiff particles would be most beneficial in enhancing the mechanical properties of the biocomposite.

Here it is interesting to observe that natural composite materials, such as wood, shells, dentin, and even bone itself, when used as reinforcing particles with high aspect ratios, are either in platelet or fibrillar form and generally nanoscale in size. Wood is made up of cellulose fibrils (5-20 nm in diameter and several hundred

![](./images/811798652350627840_4.jpg)

Fig. 4. Iso-contour plots for the ratios (a) $E_{\mathrm{P}}/E_{\mathrm{S}}$ and (b) $E_{\mathrm{O}}/E_{\mathrm{S}}$ as a function of porosity $\alpha_{\mathrm{s}}$ and geometrical anisotropy $A$.

![](./images/811798652350627840_5.jpg)

Fig. 5. The Young's modulus $E$ as a function of silicon particle concentration. The particles are spherical ($k_{1}=k_{2}=1$ or $A=0$).

![](./images/811798652350627840_6.jpg)

Fig. 6. Iso-contour plot for the Young's modulus $E$ of dense reinforced PPF as a function of the aspect ratios $k_{1}=a_{1}/a_{3}$ and $k_{2}=a_{2}/a_{3}$ of ellipsoidal silicon particles (particle concentration $\alpha_{\mathrm{s}}=10\%$).

in length) embedded in a non-cellulose matrix [42]; most mollusks have shells made up of stacked thin platelets of calcium carbonate (200–300 nm thick) interconnected through an organic glue [43]; dentin, the calcified tissue of teeth, is a biocomposite made up of a collagen-rich matrix reinforced with calcium phosphate crystals [44]; bone in vertebrates is mainly composed of thin platelets of hydroxyapatite (5–6 nm thick and several tens of nanometers in lateral dimension) embedded in a proteinaceous organic matrix [45].

### 3.3. Porous polymeric matrix reinforced with geometrically anisotropic particles

The last case analyzed resembles the actual configuration of a scaffold for bone tissue engineering, where a porous polymer matrix is reinforced with stiffer particles. This configuration represents a three-phase composite whose overall mechanical behavior can be inferred by averaging out the results derived for the two previous configurations.

The analysis is limited to porosities up to $\alpha_{\mathrm{p}}=0.6$ and particle concentrations up to $\alpha_{\mathrm{s}}=0.2$, which are the practically used ranges for these two parameters. Fig. 8 shows the iso-contours for $E$ in the case of spherical pores and spherical particles ($A=0$). As expected, the elastic properties of the biocomposite increase with increasing $\alpha_{\mathrm{s}}$ and decreasing $\alpha_{\mathrm{p}}$. Within the specified ranges and for the material properties listed in Table 1 the elastic modulus $E$ can be calculated using the approximate relationship.

$$
E \approx 3.23\alpha_{\mathrm{s}} - 2.98\alpha_{\mathrm{p}} + 2\ \mathrm{[GPa]}. \tag{8}
$$

derived by least squares fitting of the straight iso-contours in Fig. 8. In Eq. (8) the base properties of PPF are recovered by setting $\alpha_{\mathrm{s}}=0$ and $\alpha_{\mathrm{p}}=0$ ($E=2$ GPa from Table 1). Note that the constants that appear alongside $\alpha_{\mathrm{s}}$ are slightly greater than those that appear with $\alpha_{\mathrm{p}}$, indicating that the increase in elastic properties of the biocomposite with the addition of silicon is more significant than the reduction in these properties with comparable porosity. However, it should also be emphasized that $\alpha_{\mathrm{p}} \gg \alpha_{\mathrm{s}}$, thus resulting in only a marginal increase in the elastic properties of the composites. This is

![](./images/811798652350627840_7.jpg)

Fig. 7. Iso-contour plots for the ratio (a) $E_P/E_S$ and (b) $E_O/E_S$ as a function of the silicon particle concentration $\alpha_s$ and geometrical anisotropy $A$.

![](./images/811798652350627840_8.jpg)

Fig. 8. Iso-contour plots for the elastic modulus $E$ of a PPF-SiMP composite as a function of the silicon particle concentration $\alpha_s$ and porosity $\alpha_p$, for spherical particles and pores.

demonstrated in Fig. 8, where, for instance, an elastic modulus of 2.4 GPa is obtained for $\alpha_s$ 0.2 and $\alpha_p$ 0, while at the other extreme an elastic modulus of ~0.2 GPa was found for $\alpha_s$ 0 and $\alpha_p$ 0.6.

Based on the results derived in the previous two paragraphs, a strategy to enhance the elastic properties of a porous biocomposite would be that of generating spherical pores interconnected with tubular-like pores and dispersing highly geometrical anisotropic (large $A$ or $k_1$ and $k_2$) stiffer particles. This configuration has been analyzed in Fig. 9, where the ratios $E_P/E_S$ and $E_O/E_S$, defined as above, have been plotted as a function of the concentration $\alpha_s$ and geometrical anisotropy $A$ of the stiffer particles, for a fixed volume concentration $\alpha_p$ = 0.6 of the spherical pores. These results demonstrate that when using thin discoidal silicon particles or long silicon fibers ($A$ > 1000) there is a highly significant enhancement of mechanical properties when considering $\alpha_s$ 0.2 and $\alpha_p$ 0.6 ($E_P/E_S$ 8 and $E_O/E_S$ 22). We need to emphasize here that further in vitro and in vivo analyses to assess the performance of such constructs in tissue engineering applications are currently underway in our laboratory.

![](./images/811798652350627840_9.jpg)

Fig. 9. Iso-contour plots for the ratio (a) $E_P/E_S$ and (b) $E_O/E_S$ as a function of the silicon particle concentration $\alpha_s$ and geometrical anisotropy $A$ ($\alpha_p$ = 60%).

### 4. Experimental results

In order to validate the mathematical model, the theoretical results are compared with four experimental test cases, namely porous PPF, dense PLGA-HA composite; porous PLGA-HA composite; dense PPF-SiMP composite.

The results for the porous PPF matrix are compiled in Fig. 10: the dots represent the experimental results, with the corresponding standard deviations, whereas the continuous lines are the theoretical predictions. To cover a wide range of porosities, from $\alpha_{\mathrm{p}}=0.1$ to 0.7, two different porosification strategies were used, as described above. The compressive modulus of the dense PPF was ~800 MPa. Three different shapes for pores have been considered, namely spherical ($A=0$), fibril-like ($A=2000$) and platelet-like ($A=2000$). As anticipated in the previous paragraphs, spherical pores are associated with a larger modulus, while fibril-like (prolate) pores offer very similar results. The value of $E$ predicted for platelet-like pores is much smaller, and tended to be close to the experimental results for the full range investigated. It should be noted that the actual porous network within the PPF matrix was a complex combination of pores of different sizes and shapes highly connected to each other. This would explain the larger values of $E$ predicted by the mathematical model, since it does not take into account interconnectivity.

The elastic modulus of PLGA-HA composites is considered for the case of a dense PLGA [13] (Fig. 11) and a porous PLGA ($\alpha_{\mathrm{p}}=0.35$) [14] (Fig. 12). In the first case the HA nanofibers were 100 nm long and 30 nm wide ($k_{1}=k_{2}=0.3$ and $A=1.088$), whereas for the porous PLGA-HA the HA nanofibers were 45 nm long and 15 nm wide ($k_{1}=k_{2}=0.33$ and $A=0.89$). In both cases very good agreement was observed between the experimental and theoretical results over the full range of particle concentrations $\alpha_{\mathrm{s}}$ considered. Finally, Fig. 13 shows a comparison in terms of elastic modulus for dense PPF reinforced with 100 nm spherical solid silica beads. The original compressive modulus of non-reinforced PPF was 985 MPa. Even in this case good agreement with the theoretical predictions was observed for $\alpha_{\mathrm{s}}=0-0.1$. Finally, the root mean square error computed between the mean experimental data and the theoretical predictions is compiled in Table 2.

![](./images/811798652350627840_10.jpg)

Fig. 10. Elastic modulus of porous PPF: a comparison between the theoretical predictions (lines) and the experimental values (dots).

![](./images/811798652350627840_11.jpg)

Fig. 11. Elastic modulus of dense (non-porous) PLGA-HA composite: a comparison between the theoretical predictions (lines) and the experimental values (dots) (experimental data from [12]).

![](./images/811798652350627840_12.jpg)

Fig. 12. Elastic modulus of porous PLGA-HA composite: a comparison between the theoretical predictions (lines) and the experimental values (dots) (experimental data from [13]).

### 5. Conclusions

A mathematical model has been presented for predicting the mechanical response, in terms of Young's modulus $E$ and the shear elastic modulus $G$ of a multi-phase composite for bone tissue engineering. The model predicts values for the couple $(E,G)$ as a function of the geometrical features (shapes), material properties and volume concentration of each individual phase.

It has been demonstrated that the shape of pores and stiffer particles have a dramatic effect on the overall mechanical response of the composite material. The elastic moduli of porous polymeric matrices reinforced with stiffer particles can be maximized by generating spherical pores and by dispersing particles with a large

![](./images/811798652350627840_13.jpg)

Fig. 13. Elastic modulus of PPF-silica composite: a comparison between the theoretical predictions (lines) and the experimental values (dots).

<table>
<caption>Table 2<br>Root mean square error computed between the mean experimental data and the theoretical predictions.</caption>
<thead>
<tr>
<th>Material</th>
<th>Percentage root mean square error⁽ᵃ⁾ (%)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Porous PPF</td>
<td></td>
</tr>
<tr>
<td>Needle-like pore</td>
<td>99.37</td>
</tr>
<tr>
<td>Disc-like pore</td>
<td>42.24</td>
</tr>
<tr>
<td>Spherical pore</td>
<td>105.8</td>
</tr>
<tr>
<td>Dense PLGA-HA</td>
<td></td>
</tr>
<tr>
<td>Annealed</td>
<td>4.9</td>
</tr>
<tr>
<td>Molded</td>
<td>7.63</td>
</tr>
<tr>
<td>Porous PLGA-HA</td>
<td>8.91</td>
</tr>
<tr>
<td>PPF-SiMP</td>
<td>7.77</td>
</tr>
<tr>
<td colspan="2">⁽ᵃ⁾ Percentage root mean square error $e = \sqrt{\frac{\sum_{i=1}^{N} \left( \frac{E_{\text{th}}^{(i)} - E_{\text{exp}}^{(i)}}{E_{\text{exp}}^{(i)}} \right)^2}{N}} \times 100$.</td>
</tr>
</tbody>
</table>

geometrical anisotropy A. In particular, thin platelet-like particles have been shown to perform better than long fibril-like particles for given material properties and geometrical anisotropy A.

The mathematical models have been validated against four different experimental test cases, namely porous PPF with a porosity ranging from 0.1 to 0.7, dense and porous PLGA-HA composite with a HA concentration ranging from 0 to 0.3 and PPF-SiMP with a SiMP concentration ranging from 0 to 0.1. For all cases analyzed the theoretical predictions were shown to be in good agreement with the experimental results.

Finally, the model was applied to estimate the elastic response of a biocomposite material constituted of a porous PPF (60% porosity) scaffold reinforced with silicon particles (10% volume concentration). It has been shown that a Young's (shear) elastic modulus $E$ 8 GPa ($G$ 3.5 GPa) can be achieved by dispersing thin platelet-like silicon particles ($A$ 1000) in the matrix, with an increase in stiffness greater than 10 times compared with a similar concentration of spherical particles.

### Acknowledgements
This research activity has been supported by the US Army RDE-COM ACQ CTR through Grant W911NF-09-1-0044 'Bionanoscaffolds (BNS) for post-traumatic osteo-regeneration'.

## Appendix A. Supplementary data
Supplementary data associated with this article can be found, in the online version, at doi:10.1016/j.actbio.2010.03.029.

## Appendix B. Figures with essential colour discrimination
Certain figures in this article, particularly Figures 1, 2, 4, 5 and 7 – 9, are difficult to interpret in black and white. The full colour images can be found in the online version, at doi:10.1016/j.actbio.2010.03.029.

## References
[1] Langer R, Vacanti JP. Tissue engineering. Science 1993;260:920-6.
[2] Mistry AS, Mikos AG. Tissue engineering strategies for bone regeneration. Adv Biochem Eng Biotechnol 2005;94:1-22.
[3] Kavlock KD, Pechar TW, Hollinger JO, Guelcher SA, Goldstein AS. Synthesis and characterization of segmented poly(esterurethane urea) elastomers for bone tissue engineering. Acta Biomater 2007;3:475-84.
[4] Nair MB, Babu SS, Varma HK, John A. A triphasic ceramic-coated porous hydroxyapatite for tissue engineering application. Acta Biomater 2008;4:173-81.
[5] Karageorgiou V, Kaplan D. Porosity of 3D biomaterial scaffolds and osteogenesis. Biomaterials 2005;26:5474-91.
[6] Sanz-Herrer JA, García-Aznar JM, Doblaré M. On scaffold designing for bone regeneration: a computational multiscale approach. Acta Biomater 2009;5:219-29.
[7] Liebschner Michael AK. Biomechanical considerations of animal models used in tissue engineering of bone. Biomaterials 2004;25:1697-714.
[8] Cowin SC. Tissue growth and remodeling. Annu Rev Biomed Eng 2004;6:77-107.
[9] Claes LE, Heigele CA. Magnitudes of local stress and strain along bony surfaces predict the course and type of fracture healing. J Biomech 1999;32:255-66.
[10] Epari DR, Kassi J-P, Schell H, et al. Timely fracture-healing requires optimization of axial fixation stability. J Bone Joint Surg Am 2007;89:1575-85.
[11] Rezwan K, Chen QZ, Blaker JJ, et al. Biodegradable and bioactive porous polymer/inorganic composite scaffolds for bone tissue engineering. Biomaterials 2006;27:3413-31.
[12] Kretlow JD, Mikos AG. From material to tissue: biomaterial development, scaffold fabrication, and tissue engineering. AIChE J 2008;54:3048-67.
[13] Hong Z, Zhang P, He C, et al. Nano-composite of poly(l-lactide) and surface grafted hydroxyapatite: mechanical properties and biocompatibility. Biomaterials 2005;26:6296-304.
[14] Thomson RC, Yaszemski MJ, Powers JM, et al. Hydroxyapatite fiber reinforced poly(α-hydroxy ester) foams for bone regeneration. Biomaterials 1998;19:1935-43.
[15] Kasuga T, Yoshio O, Masayuki N, et al. Preparation and mechanical properties of polylactide acid composites containing hydroxyapatite fibres. Biomaterials 2001;22:9-23.
[16] Cai X, Tong H, Shen XY, et al. Preparation and characterization of homogeneous chitosan-polylactic acid/hydroxyapatite nanocomposite for bone tissue engineering and evaluation of its mechanical properties. Acta Biomater 2009;5:2693-703.
[17] Jose MV, Thomas V, Johnson KT, Dean DR, Nyairo E. Aligned PLGA/HA nanofibrous nanocomposite scaffolds for bone tissue engineering. Acta Biomater 2009;5:305-15.
[18] Lu HH, El-Amin SF, Scott KD, et al. Three-dimensional, bioactive, biodegradable, polymer-bioactive glass composite scaffolds with improved mechanical properties support collagen synthesis and mineralization of human osteoblast-like cells in vitro. J Biomed Mater Res A 2003;64A:465-74.
[19] Khan M, Dhirendra DS, Katti S, et al. Novel polymer-synthesized ceramic composite-based system for bone repair: an in vitro evaluation. J Biomed Mater Res A 2004;69A:728-37.
[20] Shi XF, Sitharaman B, Pham QP, et al. Fabrication of porous ultra-short single-walled carbon nanotube nanocomposite scaffolds for bone tissue engineering. Biomaterials 2007;28:4078-90.
[21] Shi X, Hudson JL, Spicer PP, et al. Injectable nanocomposites of single-walled carbon nanotubes and biodegradable polymers for bone tissue engineering. Biomacromolecules 2006;7:2237-42.
[22] Shi XT, Wang YJ, Ren L, et al. Novel mesoporous silica-based antibiotic releasing scaffold for bone repair. Acta Biomater 2009;5:1697-707.
[23] Ferrari M. Composite homogenization via the equivalent poly-inclusion approach. Compos Eng 1994;4:37-45.
[24] Mori T, Tanaka K. Average stress in matrix and average elastic energy of materials with misfitting inclusions. Acta Metall 1973;21:571-4.
[25] Marzari N, Ferrari M. Textural and micromorphological effects on the overall elastic response of macroscopically anisotropic composites. J Appl Mech 1992;59:269-75.

[26] Eshelby JD. The determination of the elastic field of an ellipsoidal inclusion and related problems. Proc R Soc Lond A 1957;241:376-96.

[27] Mura T. Micromechanics of defects in solids. Dordrecht: Kluwer; 1987.

[28] Ranganathan SI, Ostoja-Starzewski M. Universal elastic anisotropy index. Phys Rev Lett 2008;101:055504-1-4-4.

[29] Ranganathan SI, Decuzzi P, Wheeler LT, et al. Geometrical anisotropy in biphase particle reinforced composites. J Appl Mech 2010;77:41017-20.

[30] Shung AK, Timmer MD, Jo S, et al. Kinetics of poly(propylene fumarate) synthesis by step polymerization of diethyl fumarate and propylene glycol using zinc chloride as a catalyst. J Biomater Sci Polymer Edn 2002;13:95-108.

[31] Timmer MD, Ambrose CG, Mikos AG. Evaluation of thermal- and photo- crosslinked biodegradable poly(propylene fumarate)-based networks. J Biomed Mater Res A 2003;66:811-8.

[32] Kasper FK, Tanahashi K, Fisher JP, et al. Synthesis of poly(propylene fumarate). Nat Protoc 2009;4:518-25.

[33] Fisher JP, Dean D, Mikos AG. Photocrosslinking characteristics and mechanical properties of diethyl fumarate/poly(propylene fumarate) biomaterials. Biomaterials 2002;23:4333-43.

[34] Suggs LJ, Shive MS, Garcia CA, et al. In vitro cytotoxicity and in vivo biocompatibility of poly(propylene fumarate-co-ethylene glycol) hydrogels. J Biomed Mater Res 1999;46:22-32.

[35] Temenoff JS, Athanasiou KA, LeBaron RG, et al. Effect of poly(ethylene glycol) molecular weight on tensile and swelling properties of oligo(poly(ethylene glycol) fumarate) hydrogels for cartilage tissue engineering. J Biomed Mater Res 2002;59:429-37.

[36] Suggs LJ, Krishnan RS, Garcia CA, et al. In vitro and in vivo degradation of poly(propylene fumarate-coethylene glycol) hydrogels. J Biomed Mater Res 1998;42:312-20.

[37] Tasciotti E, Liu X, Bhavane R, et al. Mesoporous silicon particles as a multistage delivery system for imaging and therapeutic applications. Nat Nanotechnol 2008;3:151-7.

[38] Canham LT. Bioactive silicon structure fabrication through nanoetching techniques. Adv Mater 1995;7:1033-7.

[39] Anderson SHC, Elliott H, Wallis DJ, et al. Dissolution of different forms of partially porous silicon wafers under stimulated physiological conditions. Phys Status Solidi A 2003;197:331-5.

[40] Pittenger MF, Mackay AM, Beck SC, et al. Multilineage potential of adult human mesenchymal stem cells. Science 1999;284:143-7.

[41] Schmid J, Wallkamm B, Hammerle CH, et al. The significance of angiogenesis in guided bone regeneration. A case report of a rabbit experiment. Clin Oral Implants Res 1997;8:244-8.

[42] Ding SY, Himmel ME. The maize primary cell wall microfibril: a new model derived from direct visualization. J Agr Food Chem 2006;54:597-606.

[43] Menig R, Meyers MH, Meyers MA, et al. Quasi-static and dynamic mechanical response of Haliotis rufescens (abalone) shells. Acta Mater 2000;48:2383-98.

[44] Tesch W, Eidelman N, Roschger P, et al. Graded microstructure and mechanical properties of human crown dentin. Calcif Tissue Int 2001;69:147-57.

[45] Landis WJ. The strength of a calcified tissue depends in part on the molecular structure and organization of its constituent mineral crystals in their organic matrix. Bone 1995;16:533-44.
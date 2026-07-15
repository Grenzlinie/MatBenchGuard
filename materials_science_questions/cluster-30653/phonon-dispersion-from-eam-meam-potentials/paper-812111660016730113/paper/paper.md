![](./images/812111660016730113_1.jpg)

Available online at www.sciencedirect.com
SCIENCE DIRECT
Surface Science 600 (2006) 1982-1990

![](./images/812111660016730113_2.jpg)
www.elsevier.com/locate/susc

# Extended embedded-atom method for platinum nanoparticles

Byeongchan Lee ${ ^{*, 1}$ , Kyeongjae Cho

Department of Mechanical Engineering, Stanford University, Stanford, CA 94305, USA

Received 28 September 2005; accepted for publication 21 February 2006
Available online 13 March 2006

## Abstract
We present a new technique to extend the embedded-atom method (EAM) for the simulations of non-bulk systems down to the atomic cluster level. To overcome the limitation of the traditional bulk-fit EAM interatomic potentials, bond characteristics from first-principles calculations are systematically included by introducing a local structure dependent prefactor with three additional para- meters to the conventional EAM many-body term. The additional parameters improve the local potential landscape virtually for the entire range of atomic configuration space in a quantitative sense. The proposed scheme is applied to two different EAM function sets and validated for both bulk and non-bulk environments in elemental platinum. The obtained material properties, including the binding energies of Pt particles and the Pt adatom diffusion barrier on the Pt(1 1 1) surface, show a significant improvement over the conventional EAM formalism.

© 2006 Elsevier B.V. All rights reserved.

Keywords: Platinum; Surface energy; Nanoparticles; Embedded-atom method

## 1. Introduction
Over the past few years, metal nanostructures have rap- idly gained attention for applications in various fields, e.g. magnetism and catalysis [1,2]. Consequently, understand- ing the accurate structure-function relationship of nano- structures has become an important research topic in these fields. In the nano-regime, the nominal feature size of structures that are extensively studied with state-of- the-art experimental techniques is a few nanometers to tens of nanometers. Considering that first principles calcula- tions are still limited to hundreds of atoms, empirical and semi-empirical methods are desirable to simulate systems that are dealt with experimentally. The embedded-atom method (EAM) inspired by density functional theory (DFT) [3,4] and mathematically equivalent methods have been successfully applied to the bulk face-centered cubic (fcc) metals [5,6], and have been pushed beyond the bulk environment to pursue this direction for the application of metals surfaces and nanoparticles [7,8].

The first-generation many-body potentials, however, soon faced limitations, e.g. the calculated surface energies are much smaller than the experimental values [9], as the system of interest switched from bulk to non-bulk systems in which the surface energetics play a major role. The second-generation many-body potentials have been intro- duced to overcome these limitations. Following the rigor- ous study of Daw [10], charge density corrections are incorporated into some implementations [11,12]. To over- come the limitation due to the bulk data fitting, geometry factor or angular dependence is included in the modified EAM (MEAM) [11], and a cutoff density is used to change the shape of the embedding energy in the surface EAM (SEAM) [13]. The embedded-defect (ED) potential, mathe- matically similar to MEAM's charge gradient expansion but essentially closer to the hydrostatic and deviatoric decomposition of classical mechanics, has been proposed to take advantage of the crystal symmetry [14]. In the force-matching method or other techniques in the same spirit [15-17], large amounts of data produced by first principles calculations are used in the fitting process to

* Corresponding author.
E-mail address: airbc@llnl.gov (B. Lee).
1 Present address: Lawrence Livermore National Laboratory, University of California, L-415, Livermore, CA 94551, USA.

0039-6028/S - see front matter  2006 Elsevier B.V. All rights reserved.
doi:10.1016/j.susc.2006.02.029

construct potentials to gain higher accuracy comparable to ab initio methods.

Despite the success of these modified approaches, they have yet other limitations: the force-matching method has 40 parameters, the SEAM is not guaranteed to apply to diatomic molecules or small clusters, in which each atom has a lower coordination number than those on the surface, and the MEAM still underestimates the bonding strength of atoms on the surface. More generally speaking, the current EAM implementations were not designed to deal with clusters, and they have inherent inaccuracy due to the physical effects that are not effectively encapsulated within the EAM framework [16], i.e. electronic effects of clusters.

One important quality of an interatomic potential is transferability. It essentially determines how well an EAM implementation can deal with the physical effects that have not been captured in the fitting process [17]. In principle, transferability must be retained both in a qualitative sense and in a quantitative sense. The "qualitative" transferability comes from the well-chosen, physically meaningful functional forms, and the "quantitative" transferability comes from the well-chosen data, to which parameters are fitted. Unfortunately, there is no crossover between two aspects of transferability: a carefully chosen data set hardly compensates for ill-chosen functional forms and vice versa. In reality, however, current techniques only retain the transferability in a qualitative sense with the bulk-based fitting. Any quantitative transferability is accidental even with correct functional forms as, in general, any non-bulk prediction is an extrapolation from the bulk data. The consequences of the extrapolation are clearly seen in Fig. 1: both EAM and ab initio calculations are in good agreement in the bulk region, whereas the difference is significant for small clusters. The EAM due to Cai and Ye (CY-EAM)[18] is shown as a representative implementation, and compared with ab initio calculations (DFT). Also shown is one of the extensions to CY-EAM (CY-XEAM1) resulting from this work.

In this work, the transferability problem is considered within the context of coordination number - i.e. an fcc matrix being fully coordinated and a free-standing dimer having minimal coordination-to obtain quantitative accuracy. By introducing the data for small atomic clusters into the fitting, the extrapolating nature of bulk-fit-based calculations is turned into the interpolating characteristic based on both bulk and cluster fitted calculations. Now all the other configurations are interpotations between two extrema, and better "quantitative" transferability can be attained. An earlier effort in this direction has included the ab initio dimer information of Cu for the EAM fit [19], but more information, e.g. trimer and tetramer information, may be necessary to capture the rather complex energetics in this domain as can be seen in Fig. 1.

Another important quality to consider is the local environment dependence of bond characteristics. The bcc-fcc stability, or the energy difference between two structures is small even though there is a significant change both in coordination number and in bond angles. Whereas, the energy difference between a (111) surface atom and an atom in the bcc lattice is large even though the (111) surface atom has even more neighbors. The spherical symmetry of earlier EAM implementations is unable to address these issues. Rigorously speaking, the angle dependence is not enough either given that electrons in bulk fcc transition metals do behave like free electrons, i.e. delocalized or no angular dependence.

![](./images/812111660016730113_3.jpg)

Fig. 1. Binding energy per atom as a function of coordination number in Pt. Each coordination number represents a different structure with different dimensionality, i.e. 1 (dimer), 2 (trimer), 3 (tetrahedron), 6 (two-dimensional hexagonal mesh), 8 (body-centered cubic bulk lattice), and 12 (face-centered cubic bulk lattice). The nearest neighbor distance is fixed at the perfect bulk fcc lattice spacing. The details of the extension (CY-XEAM1) are explained in Section 3 and subsequent sections.

The objective of this paper is to extend the EAM such that the EAM preserves its simple form with a reasonable number of parameters, and more important, it can predict the coordination number-bond strength relationship better in a quantitative sense. The square root-like dependence resulting from the unsaturated nature of the metallic bond [20] is satisfied using all the different schemes mentioned above but the quantitatively accurate profile is not obtained, which results in the underestimation of surface energies and a considerable error in the bond strength prediction for the lower-coordinate configurations, e.g. isolated dimers. In this paper, the energetics from the DFT calculations of small Pt clusters is incorporated into the extended EAM (XEAM) to address these issues in the conventional EAM.

## Theoretical background

The total energy of an N-atom system in the EAM can be expressed as
$$
E[\mathbf{R}_{1}, \ldots, \mathbf{R}_{N}]=\sum_{i} F[\rho_{i}]+\sum_{j(\neq i)} \phi[\mathbf{R}_{i j}],\qquad(1)
$$

where $R_1, \dots, R_N$ denote the positions of $N$ ions in the system and $F$ is the embedding energy required to place an atom into a bulk lattice site; $\phi$ is the pair potential, and $\rho_i$ denotes the host electron density at site $i$ due to all other atoms. The host electron density is

$$
\rho_i = \sum_{j(\neq i)} \rho_j^a[\mathbf{R}_{ij}], \tag{2}
$$

where $\rho_j^a$ is the spherically symmetric electron density contributed by atom $j$. There is no unique way to determine the functional forms of $F$, $\phi$ and $\rho_j^a$ , but a typical approach is to assume physically appropriate forms and fit them to the material properties obtained from experiments. Most EAM implementations include bulk properties and a few defect properties, such as vacancy formation energy in the fitting process and, as can be foreseen, simulations of non-bulk systems require a significant extrapolation from the bulk data, which is likely to introduce errors. On the other hand, simply including more non-bulk properties does not uniformly improve the accuracy of any EAM implementations as it will, to some extent, degrade the fitting that best describes the behavior of bulk materials. Therefore, a better approach is to find a way to systematically include non-bulk properties such that any modifications made do not affect bulk properties.

In order to overcome the limitation of the conventional EAM, a functional form sensitive to the local structural symmetry of the atomic system is included in the XEAM. The idea of the XEAM is that atoms in a defective environment have a lower coordination number and an asymmetric atomic arrangement, the effect of which we can easily put into the existing EAM framework. For example, the EAM energy cannot capture the structural difference between a surface atom sitting on a fcc (100) facet and an atom in the bulk bcc structure with the spacing fixed at the nearest neighbor (NN) distance of the bulk fcc structure, since both have the same number of NNs at the same NN distance. As can be seen in this example, one of the distinct differences between atoms on the surface and atoms in the bulk is the structural symmetry. To capture the asymmetry, we add the effect from the change in the density to the embedding energy term simply by introducing the asymmetry density. The effective density of atom at lattice site $i$ is defined as

$$
\rho_i^{\text{eff}} = \rho_i - \alpha \rho_i^{\text{asym}}, \tag{3}
$$

where $\alpha$ is a parameter to fit and the asymmetric density is of the form

$$
\rho_i^{\text{asym}} = \left\| \sum_{j(\neq i)} \rho_j^a[\mathbf{R}_{ij}] \frac{\mathbf{R}_{ij}}{\|\mathbf{R}_{ij}\|} \right\|, \tag{4}
$$

where $\rho_j^a$ is the electron density contribution coming from site $j$ to the atom at site $i$. Assuming that the pair interaction is not affected by the symmetry as it is supposed to be, the only problem that remains to consider is to compensate for the broken symmetry effect on the embedding function. The effective embedding energy term and the normalized asymmetric density are defined as

$$
F^{\text{eff}}[\rho_i^{\text{eff}}] = gF[\rho_i^{\text{eff}}], \tag{5}
$$

$$
g = 1 - \epsilon \bar{\rho}_i^k, \tag{6}
$$

$$
\bar{\rho}_i = \frac{\rho_i^{\text{asym}}}{\rho_i}, \tag{7}
$$

where $\epsilon$ and the polynomial power $k$ are the parameters to fit. Then, the embedding energy, $F$, in Eq. (1), is replaced by the effective embedding energy, $F^{\text{eff}}$, for total energy calculations. Given that the normalized asymmetric density, $\bar{\rho}_i$, varies from zero to one, this technique preserves the energetics of the original EAM for symmetric structures including perfect bulk structures. We can consider that there are two driving forces, instead of one in the EAM, for the non-linear nature of the bond strength. One is the coordination number dependence resulting from the fact that atoms with a lower coordination number have higher bonding strength due to localized charge distribution. The other driving force is structural dependence resulting from the fact that an ordered structure (symmetric or periodic) when compared to disordered structures, is likely to have lower bonding energy due to resonance stabilization. The prefactor $g$ scales the embedding energy based on local environment, and it can be defined such that the prefactor is 1 for symmetric structures to preserve the bulk EAM energy and it is a smaller but positive value for asymmetric structures. We have tested several different functional forms of $g$, e.g. exponential functions, $g = 1/(1 + \bar{\rho}_i^k)$, etc., as the exact form of the effective embedding energy is unknown, and the resulting differences turned out to be negligible. A simple form in Eq. (7) is used for calculations, where the polynomial power $k$ represents the leading term of the series expansion of any kind of functions.

In order to see how the XEAM changes the potential energy and the subsequent many-body force field, the effect of asymmetric density is inspected for a general EAM implementation: only a NN interaction is considered for simplicity, but the overall argument is not affected even if the interaction range goes beyond the NNs. As shown in Table 1, asymmetric factor, $\rho_i^{\text{asym}}$, can differentiate two different structures with the same coordination number, and the

<table>
<caption>Table 1<br>Different density terms in the XEAM implementation</caption>
<thead>
<tr>
<th>Configuration</th>
<th>NN</th>
<th>$\rho_i$</th>
<th>$\rho_i^{\text{asym}}$</th>
<th>$\bar{\rho}_i$</th>
</tr>
</thead>
<tbody>
<tr>
<td>Dimer</td>
<td>1</td>
<td>$\rho^a$</td>
<td>$\rho^a$</td>
<td>1</td>
</tr>
<tr>
<td>Trimer</td>
<td>2</td>
<td>$2\rho^a$</td>
<td>$\sqrt{3}\rho^a$</td>
<td>$\frac{\sqrt{3}}{2}$</td>
</tr>
<tr>
<td>1D chain</td>
<td>2</td>
<td>$2\rho^a$</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>Tetrahedron</td>
<td>3</td>
<td>$3\rho^a$</td>
<td>$\sqrt{3}\rho^a$</td>
<td>$\frac{\sqrt{3}}{3}$</td>
</tr>
<tr>
<td>2D hex mesh</td>
<td>6</td>
<td>$6\rho^a$</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>(100) fcc surface atom</td>
<td>8</td>
<td>$8\rho^a$</td>
<td>$2\rho^a$</td>
<td>$\frac{1}{4}$</td>
</tr>
<tr>
<td>bcc bulk</td>
<td>8</td>
<td>$8\rho^a$</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>(111) fcc surface atom</td>
<td>9</td>
<td>$9\rho^a$</td>
<td>$\sqrt{3}\rho^a$</td>
<td>$\frac{\sqrt{3}}{9}$</td>
</tr>
<tr>
<td>fcc bulk</td>
<td>12</td>
<td>$12\rho^a$</td>
<td>0</td>
<td>0</td>
</tr>
</tbody>
<tfoot>
<tr>
<td colspan="5">NN is the coordination number for a given configuration, and $\rho^a = \rho_j^a$.</td>
</tr>
</tfoot>
</table>

effect of this factor becomes stronger in lower-coordinated environment. In addition, it scales the embedding energy such that the embedding energy of a system far from the bulk environment is more sensitive to its structure. Therefore, using the XEAM with relevant non-bulk data, the error introduced from extrapolation can be avoided where the structure is far from the perfect bulk lattice: when the XEAM parameters are fitted to the lowest-coordinated system data, e.g. dimers and trimers, it becomes an interpolation problem rather than an extrapolation problem.

As mentioned earlier, the XEAM collapses into the EAM when $\bar{\rho}_{i}$ becomes zero for symmetric structures. There are three such cases, from one dimensional to three dimensional symmetric structures. In the three dimensional case, the XEAM is designed to reduce to the EAM to preserve the energy of bulk crystals. Even in two other cases, i.e. one dimensional chains and two dimensional meshes, the XEAM does not improve the EAM by itself. Since our focus in this work is to develop an interatomic potential for nanoparticles, the dimensional span can be omitted without any loss of accuracy.

In summary, the XEAM scheme can accompany any EAM implementations and works as an add-on feature to the EAM since this does not alter any functions defined in the EAM framework for bulk crystalline materials. In other words, XEAM can reproduce the same bulk properties as the reference EAM model to which XEAM is added because the asymmetry factor becomes zero in the bulk and all the functions go back to the original forms defined in the reference EAM model. On the other hand, when non-bulk environment is present in the system, the XEAM feature is turned on because the asymmetry factor is no longer zero. In the latter case, XEAM can produce better results by including input data coming from small metal clusters, e.g. dimer binding energy, dimer binding distance, etc.

## 3. Parameter fitting

In order to utilize the XEAM scheme, the values of the three parameters introduced above, i.e. $\alpha$, $\epsilon$ and $k$, must be determined; they are obtained from an additional fitting process. Since the goal of XEAM was to cover the entire range of configuration space, the energetics of the smallest possible clusters obtained from the first principles database are used to determine the XEAM parameters. The reason for not using experimental data, but first principles calculations for this additional fitting, is simply the experimental data of the cluster energetics are not readily available. Once experimental confirmation on the cluster information has become available, experimental data can replace first principles data for better compatibility with the bulk experimental data.

The number of parameters used in the EAM varies considerably from one function set to another. However, function sets having a larger number of parameters are not always more successful in calculating non-bulk properties because the fitting process is based on bulk properties, and still confined in a narrow region in configuration space. Therefore, often it is not the number of parameters to fit, but how these parameters are fitted that determines the performance of an interatomic potential implementation. In order to include the cluster energetics systematically, a two-step fitting process can be used: only the EAM parameters are fitted to bulk data in the first step, and three XEAM parameters are fitted next. In this way, we can preserve the EAM function sets that are rather complete for bulk calculations; yet we can incorporate the non-bulk information into the existing bulk-based model in a meaningful way, and handle the entire spectrum in configuration space from dimers to bulk systems more effectively. To summarize, parameters are fitted sequentially to two extrema in configuration space, and the resulting function set can predict reasonably the energetics of a configuration between the two by blending the characteristics of two extrema. At the same time as the XEAM parameters alter near-bulk properties such as vacancy formation energy, the use of the two-step process can be limited depending on the functional forms of an EAM implementation.

In this work, the DFT database was generated using the first principles calculation package, the Vienna ab initio simulation package (VASP) [21,22] along with ultrasoft pseudopotential (US-PP) within the local density approximation (LDA) [23]. As DFT tends to overbind, the DFT database was not directly comparable to the experimental data. In the next step, the DFT database was processed such that it is consistent with the bulk experimental data. A simple conversion relation is used in this process

$$
\tilde{E}_{\mathrm{DFT}}[n]=E_{\mathrm{expr}}[\mathrm{fcc}] × \frac{E_{\mathrm{DFT}}[n]-E_{\mathrm{DFT}}[\mathrm{free}]}{E_{\mathrm{DFT}}[\mathrm{fcc}]-E_{\mathrm{DFT}}[\mathrm{free}]},\tag{8}
$$

where $\tilde{E}_{\mathrm{DFT}}$ is the (scaled) reference DFT binding energy that is used in the fitting, and $n$ is coordination number (or corresponding structure). The reference DFT values are computed in the following way. First, the free atom energy, $E_{\mathrm{DFT}}[\mathrm{free}]$, is subtracted from the DFT total energy per atom for a given structure, $E_{\mathrm{DFT}}[n]$; this energy difference can be considered as DFT binding energy. Second, this binding energy is divided by the DFT binding energy of the fcc structure; the resulting dimensionless factor ranges from zero to one. Finally, this factor is multiplied by the experimental binding energy of the fcc structure. In this way, the relative DFT energy value of one configuration to another remains the same, but scaled to reproduce the bulk experimental fcc binding energy. There are two reasons for doing this cumbersome conversion. First, the experimental data are preferred for the bulk fit because, in most cases, the EAM parameters are fitted to them. Second, the necessary energetics for non-bulk configurations, e.g. isolated dimers, is hardly known from experiment as mentioned before; DFT calculations are inevitable at the moment. Consequently, a way to mix experimental data and DFT data seamlessly is required so that they are compatible with each other.

<table>
<caption>Table 2<br>Parameters used in the CY-EAM and four XEAM fits</caption>
<thead>
<tr>
<th>Parameters</th>
<th>CY-EAM</th>
<th>CY-XEAM1</th>
<th>CY-XEAM2</th>
<th>DB-XEAM1</th>
<th>DB-XEAM2</th>
</tr>
</thead>
<tbody>
<tr>
<td>$\chi$</td>
<td>4.3</td>
<td>4.3</td>
<td>4.4646</td>
<td>–</td>
<td>–</td>
</tr>
<tr>
<td>$\alpha$ (EAM)</td>
<td>0.4033</td>
<td>0.4033</td>
<td>0.4949</td>
<td>–</td>
<td>–</td>
</tr>
<tr>
<td>$\beta$</td>
<td>5.6379</td>
<td>5.6379</td>
<td>5.7097</td>
<td>–</td>
<td>–</td>
</tr>
<tr>
<td>$F_0$</td>
<td>4.27</td>
<td>4.27</td>
<td>4.5633</td>
<td>–</td>
<td>–</td>
</tr>
<tr>
<td>$F_1$</td>
<td>0.6815</td>
<td>0.6815</td>
<td>0.7160</td>
<td>–</td>
<td>–</td>
</tr>
<tr>
<td>$r_a$</td>
<td>2.3839</td>
<td>2.3839</td>
<td>2.2240</td>
<td>–</td>
<td>–</td>
</tr>
<tr>
<td>$\alpha$ (XEAM)</td>
<td>–</td>
<td>0</td>
<td>0</td>
<td>0.1217</td>
<td>0.1048</td>
</tr>
<tr>
<td>$\epsilon$</td>
<td>–</td>
<td>0.5277</td>
<td>0.5742</td>
<td>0.1257</td>
<td>0.3094</td>
</tr>
<tr>
<td>$k$</td>
<td>–</td>
<td>1.81</td>
<td>1.93</td>
<td>6.50</td>
<td>1.80</td>
</tr>
</tbody>
</table>

The values of the CY-EAM parameters ($\chi$, $\alpha$, $\beta$, $F_0$, $F_1$, and $r_a$) are presented here for the comparison between CY-XEAM1 and CY-XEAM2 only, and the definition of CY-EAM parameters can be found in Ref. [18]. The XEAM parameter values ($\alpha$, $\epsilon$, and $k$) are presented for all four XEAM fits.

We tested two EAM function sets for four trial XEAM fits, and the sets are due to Daw and Baskes [4], and Cai and Ye [18]; we refer to them as DB-XEAM and CY-XEAM. The Daw and Baskes' function set was chosen because it was used in the original EAM formulation. The other one was chosen because it has a simple formulation with relatively small number of parameters but works quite accurately for bulk environment. Both DB-XEAM and CY-XEAM have a rather long range, with the cutoff radii of $5.3\ \text{Å}$ and $6.468\ \text{Å}$ respectively. This ensures that results do not depend on cutoff radius, and contributions from second and third nearest neighbors are not neglected. DB-XEAM1, the first fit of DB-XEAM, was designed to reproduce the cohesive energies of the relaxed dimer, trimer and tetrahedron configurations, but not necessarily their structures, i.e. bond lengths. On the other hand, DB-XEAM2 was fitted to reproduce the relaxed bond lengths of these configurations. We have two DB-XEAM fits because, due to their functional forms, we were not able to reproduce both the bond lengths and the cohesive energies of the given configurations within a reasonable error. For both DB-XEAM fits, the original DB-EAM parameters are not modified.

For CY-XEAM, the unrelaxed energies of the dimer, trimer and tetrahedron configurations along with the bond length of the relaxed dimer structure were used for both fits. Again two sets of fitting have been generated. CY-XEAM1 was generated with the two-step process illustrated above, and it preserves the same EAM parameters as in the original CY-EAM fit other than three XEAM parameters. CY-XEAM2 was generated in a single shot, and the EAM parameters have been altered. The parameter values are listed in Table 2. In our fits, $\alpha$ turns out to be zero for CY-XEAM, but this is by no means the best fit and a non-zero $\alpha$ might give better results.

## 4. Bulk environment

The experimental values in Table 3 were used for both CY-EAM and DB-EAM, and they can provide the common reference point. All the fits except CY-XEAM2 predict the same cohesive energies and bulk lattice constants as in their reference EAM fits. The vacancy formation energies have been affected by incorporating new parameters into the existing EAM framework: the error introduced in doing so is $20\%$ for CY-XEAM1, whereas the error is $1\ \text{eV}$ or larger for both DB-XEAM fittings.

<table>
<caption>Table 3<br>Bulk and near-bulk properties in Pt: cohesive energy $E_{\text{coh}}$, (unrelaxed) vacancy formation energy $E_{\text{vac}}$, bulk modulus $B$, and three elastic constants $C_{11}$, $C_{12}$ and $C_{44}$</caption>
<thead>
<tr>
<th></th>
<th>$E_{\text{coh}}$ (eV)</th>
<th>$E_{\text{vac}}$ (eV)</th>
<th>$B$</th>
<th>$C_{11}$</th>
<th>$C_{12}$</th>
<th>$C_{44}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>Experimentª</td>
<td>5.77</td>
<td>1.50</td>
<td>283</td>
<td>347</td>
<td>251</td>
<td>76.5</td>
</tr>
<tr>
<td>CY-EAMª</td>
<td>5.72</td>
<td>1.49</td>
<td>276</td>
<td>309</td>
<td>259</td>
<td>79.3</td>
</tr>
<tr>
<td>CY-XEAM1</td>
<td>5.72</td>
<td>1.79</td>
<td>276</td>
<td>309</td>
<td>259</td>
<td>79.3</td>
</tr>
<tr>
<td>CY-XEAM2</td>
<td>5.77</td>
<td>1.51</td>
<td>284</td>
<td>319</td>
<td>266</td>
<td>77.5</td>
</tr>
<tr>
<td>DB-EAMᵇ</td>
<td>5.77</td>
<td>1.68</td>
<td>283</td>
<td>303</td>
<td>273</td>
<td>68.0</td>
</tr>
<tr>
<td>DB-XEAM1</td>
<td>5.77</td>
<td>2.62</td>
<td>283</td>
<td>303</td>
<td>273</td>
<td>68.0</td>
</tr>
<tr>
<td>DB-XEAM2</td>
<td>5.77</td>
<td>2.95</td>
<td>283</td>
<td>303</td>
<td>273</td>
<td>68.0</td>
</tr>
</tbody>
<tfoot>
<tr>
<td colspan="7">All the elastic moduli are in GPa.</td>
</tr>
<tr>
<td colspan="7">ª Ref. [18] and references therein.</td>
</tr>
<tr>
<td colspan="7">ᵇ Ref. [4].</td>
</tr>
</tfoot>
</table>

Although the overall accuracy of CY-XEAM2 for bulk properties is slightly improved over CY-EAM, this is not due to the XEAM addition but to the fitting process; either CY-EAM or CY-XEAM is by no means the best fit. This can be easily seen when the bulk moduli are calculated. Although individual elastic constants from DB-EAM and DB-XEAM show a slightly larger error, the bulk modulus exactly matches the experimental value, 283 GPa. On the contrary, the CY-EAM modulus (hence CY-XEAM1 modulus) and the CY-XEAM2 modulus are 276 GPa and 284 GPa respectively. There certainly is a situation in which the bulk modulus plays a more important role than the individual elastic constants, e.g. a system under hydrostatic pressure, and the determination of a better fitting is in doubt unless the absolute numerical exactness has been obtained. Thus, a better fit from one point of view could be a worse fit if seen from another point of view.

## 5. Atomic clusters and nanoparticles

As listed in Table 4, DB-XEAM1 can predict the relaxed binding energies essentially identical to the DFT calcula-

Table 4
Fitting result for Pt clusters: relaxed system binding energy per atom
$E_{\text{relax}}$, and relaxed bond length $d_{\text{relax}}$

<table>
<thead>
<tr>
<th></th>
<th colspan="2">Dimer</th>
<th colspan="2">Trimer</th>
<th colspan="2">Tetrahedron</th>
</tr>
<tr>
<th></th>
<th>$d_{\text{relax}}$ (Å)</th>
<th>$E_{\text{relax}}$ (eV/atom)</th>
<th>$d_{\text{relax}}$ (Å)</th>
<th>$E_{\text{relax}}$ (eV/atom)</th>
<th>$d_{\text{relax}}$ (Å)</th>
<th>$E_{\text{relax}}$ (eV/atom)</th>
</tr>
</thead>
<tbody>
<tr>
<td>DFT-LDA</td>
<td>2.29</td>
<td>−1.94</td>
<td>2.43</td>
<td>−2.52</td>
<td>2.55</td>
<td>−2.86</td>
</tr>
<tr>
<td>CY-EAM</td>
<td>2.31</td>
<td>−3.94</td>
<td>2.46</td>
<td>−4.14</td>
<td>2.51</td>
<td>−4.31</td>
</tr>
<tr>
<td>CY-XEAM1</td>
<td>2.32</td>
<td>−1.97</td>
<td>2.46</td>
<td>−2.62</td>
<td>2.54</td>
<td>−2.94</td>
</tr>
<tr>
<td>CY-XEAM2</td>
<td>2.32</td>
<td>−1.95</td>
<td>2.45</td>
<td>−2.70</td>
<td>2.53</td>
<td>−3.04</td>
</tr>
<tr>
<td>DB-EAM</td>
<td>1.74</td>
<td>−3.95</td>
<td>2.03</td>
<td>−3.56</td>
<td>2.25</td>
<td>−3.67</td>
</tr>
<tr>
<td>DB-XEAM1</td>
<td>1.84</td>
<td>−1.94</td>
<td>2.13</td>
<td>−2.49</td>
<td>2.34</td>
<td>−2.85</td>
</tr>
<tr>
<td>DB-XEAM2</td>
<td>2.29</td>
<td>−0.83</td>
<td>2.44</td>
<td>−1.41</td>
<td>2.54</td>
<td>−1.79</td>
</tr>
</tbody>
</table>

tions; however, the relaxed bond lengths are significantly shorter. On the contrary, DB-XEAM2 predicts the structures correctly but considerably underestimates the relaxed cohesive energies. In spite of its simple form, CY-XEAM predicts both bond lengths and energies reasonably well compared to DB-XEAM, and both CY-XEAM1 and CY-XEAM2 result in a similar trend, e.g. longer dimer bond length than the DFT reference length, lower trimer and tetramer binding energies than the reference. The bond lengths of the CY-XEAM are not improved partially because only the dimer bond length was in the fit with a relatively lower weight, and partially because the CY-EAM bond lengths are already close to the DFT numbers.

As expected, different EAM functional forms show almost the same accuracy in bulk environment, but they begin to deviate and finally exhibit different trends on the other end of configuration space, i.e. small clusters. Since DB-XEAM's recycle the DB-EAM parameters, the XEAM fit is not as flexible as in CY-XEAM2 resulting in an extreme trend: when we have the right bond lengths, the bond energies are far off from the reference and vice versa. On the other hand, CY-XEAM1, in spite of the same deficiency as DB-XEAM, is overall in reasonable agreement with the DFT result, which was expected from a smaller vacancy formation error in the previous section.

One way to check if the XEAM is transferable is to see the binding energy as a function of particle size. The XEAM effect is highest when the size of a particle is small. When the size of a particle is large enough, on the other hand, the surface-to-bulk ratio decreases and the XEAM effect essentially vanishes. In between, the XEAM effect will vary depending on the local environment. The formation energy as a function of particle size has been calculated from fully relaxed Pt particles: each particle is prepared such that it forms a spheroid of which atoms are taken from the perfect fcc lattice, then it is relaxed. The EAM calculation reveals that DB-EAM estimates the formation energy of dimer higher than that of trimer, which results from the particular functional forms of the implementation and/or the fitting process. Nevertheless, as in Fig. 2, this undesirable behavior is rectified by simply superimposing the XEAM on the existing EAM implementation. The resulting DB-XEAM1 formation energy curve shows an

![](./images/812111660016730113_4.jpg)

Fig. 2. Formation energy of Pt particle as a function of particle size: (a) DB-XEAM1 calculations, (b) CY-XEAM1 calculations and (c) CY-XEAM2 calculations.

improvement over the EAM prediction in the sense that the formation energy essentially decays as the size decreases. The corrected formation energy curves from CY-XEAM1 and DB-XEAM1 show qualitative agreement with little quantitative difference; whereas, as far as the structure is concerned, CY-XEAM1 and CY-XEAM2 are likely to predict better structures than DB-XEAM1 as mentioned earlier.

## 6. Surfaces

In the previous sections, we have tested the XEAM fits for the systems at or near the region whose data have been used in the fit, and the focus is now moved onto the Pt surface, i.e. somewhere between bulk and small clusters. The surface energetics is important not only because it is a good place to test the transferability of the new fits, but because it plays a key role in understanding nanoparticle energetics. For surface energy calculations, sufficiently thick slabs are used to ensure that we have no size dependence. The slabs are free to relax in the surface normal direction, and periodic in the directions perpendicular to the surface normal. The results are listed in Table 5, along with those from first principles calculations and experimental results. Evidently, CY-XEAM1 and CY-XEAM2 show significant improvement over the reference CY-EAM. The relaxed surface energy of the clean Pt(111) surface obtained from the CY-XEAM1 calculations is found to be 0.104 eV, and that from CY-XEAM2 is 0.092 eV. The surface energy from DB-XEAM1 is in good agreement with the LDA value as well. On the other hand, DB-XEAM2 seems to overestimate the DFT surface energy, which was easily anticipated from high system energies listed in Table 4.

Another important aspect of surface energetics other than surface energies is the surface energy ratio. It plays a crucial role in determining the shapes of nanoparticles or nanowires as these structures would prefer to minimize the total surface energy and stay in local minima. Especially when the size of the structure is big enough to ignore the effects coming from edges and vertices, the local minima can be identified by the Wulff construction based on the surface energy ratio, which has less uncertainty than the values of the individual surface energies.

The predicted diffusion barrier of a Pt adatom on the relaxed Pt(111) surface is 0.31 eV with CY-XEAM1, and 0.38 eV with CY-XEAM2. Although the CY-XEAM2 value is higher than those from first principles calculations and experiments, the result is still within the reasonable range. The binding energy of the dimer calculated with CY-XEAM1 is 0.81 eV and it is 0.90 eV with CY-XEAM2; both of them are higher than the first principles value of 0.48 eV [28]. For the dimer configuration, both atoms are assumed to be sitting at the NN fcc sites on the (111) surface; the relaxed distance between the two is found to be

<table>
<caption>Table 5<br>Surface properties in fcc Pt: (111) surface energy $\sigma_{(111)}$, (100) surface energy $\sigma_{(100)}$, and adatom diffusion barrier on (111) surface $E_{(111)}$</caption>
<thead>
<tr>
<th>
</th>
<th>$\sigma_{(111)}$<br>($\text{eV}/\mathring{\text{A}}^2$)
</th>
<th>$\sigma_{(100)}$<br>($\text{eV}/\mathring{\text{A}}^2$)
</th>
<th>$\sigma_{(100)}/\sigma_{(111)}$
</th>
<th>$E_{(111)}$<br>(eV)
</th>
</tr>
</thead>
<tbody>
<tr>
<td>Experiment
</td>
<td>$(0.155)^\text{a}$
</td>
<td>
</td>
<td>
</td>
<td>$0.26^\text{b}$
</td>
</tr>
<tr>
<td>DFT-LDA
</td>
<td>$0.124^\text{c}$
</td>
<td>
</td>
<td>
</td>
<td>$0.33\pm0.03^\text{c}$
</td>
</tr>
<tr>
<td>DFT-GGA
</td>
<td>$0.092^\text{d}$
</td>
<td>$0.114^\text{d}$
</td>
<td>1.24
</td>
<td>
</td>
</tr>
<tr>
<td>CY-EAM
</td>
<td>$0.070^\text{e}$
</td>
<td>$0.077^\text{e}$
</td>
<td>1.10
</td>
<td>0.096
</td>
</tr>
<tr>
<td>CY-XEAM1
</td>
<td>0.104
</td>
<td>0.122
</td>
<td>1.17
</td>
<td>0.31
</td>
</tr>
<tr>
<td>CY-XEAM2
</td>
<td>0.092
</td>
<td>0.111
</td>
<td>1.21
</td>
<td>0.38
</td>
</tr>
<tr>
<td>DB-EAM
</td>
<td>$0.090^\text{f}$
</td>
<td>$0.103^\text{f}$
</td>
<td>1.14
</td>
<td>
</td>
</tr>
<tr>
<td>DB-XEAM1
</td>
<td>0.125
</td>
<td>0.139
</td>
<td>1.11
</td>
<td>
</td>
</tr>
<tr>
<td>DB-XEAM2
</td>
<td>0.16
</td>
<td>0.18
</td>
<td>1.13
</td>
<td>
</td>
</tr>
</tbody>
</table>

The experimental surface energy is the average value.
<br>
$^\text{a}$ Ref. [26].
<br>
$^\text{b}$ Ref. [27].
<br>
$^\text{c}$ Ref. [24].
<br>
$^\text{d}$ Ref. [25].
<br>
$^\text{e}$ Ref. [18].
<br>
$^\text{f}$ Ref. [4].

![](./images/812111660016730113_5.jpg)

Fig. 3. (a) Total adatom energy for fcc and saddle sites as a function of strain and (b) the diffusion barrier of Pt on Pt(111) as a function of strain.

be $2.565\,\text{Å}$, about $7.48\%$ shorter than the bulk fcc NN distance from CY-XEAM1, and $2.556\,\text{Å}$, $7.79\%$ shorter from CY-XEAM2. The dissociation barrier, the sum of the dimer binding energy and the diffusion barrier of single adatom, is 1.12 eV from CY-XEAM1 and 1.28 eV from CY-XEAM2.

The strain-dependent energetics from the CY-XEAM2 calculations for Pt on Pt(111) is shown in Fig. 3. The total adatom energy versus the relative lattice constant $a/a_0$ is presented for both the fcc site and the saddle site, where $a_0$ is the equilibrium lattice constant. The calculation is performed for a fully relaxed slab of ten layers with the bottom three layers fixed, each layer consisting of a $(10\times10)$ lattice site matrix. To assure the accuracy of the calculation, the diffusion barrier for a system in equilibrium was calculated for systems with up to 31 layers, confirming that there was no significant size effect for the ten $(10\times10)$-layer system. CY-XEAM is able to predict the strain dependence of a Pt adatom on the Pt(111) surface that is comparable to the trend from the Ag adatom diffusion on the Pt(111) surface [29,30] and from the Co adatom diffusion on the Pt(111) surface [2] predicted from first principles calculations, but shows a clearer trend than the EAM result [31].

### 7. Conclusion

The extended embedded-atom method has been developed and successfully applied to the systems far from the bulk environment in configuration space. The interatomic potential, extended by adding additional degrees of freedom to the existing embedded-atom method framework and by systematically including the cluster energetics from first-principles calculations, shows an improvement over the traditional embedded-atom method as can be seen from the coordination-bond strength relationship in Fig. 1. The XEAM implementations based on the functional forms due to Daw and Baskes, and by Cai and Ye have been tested for the validation. From this study, CY-XEAM2 is found to be the best fit out of four trial fits, yet other XEAM implementations with different functional forms and/or more sophisticated fitting processes, e.g. the MEAM including the second nearest-neighbor shell [32], may describe the systems tested above more accurately.

In this study, the properties of free particles as well as small clusters on the surface have been calculated and compared with experiment and first principles calculations. Calculating these properties is essential in that the correct surface energetics and kinetics must be validated to study nanoparticles in detail. The calculated surface energies in Pt from two different function sets show a significant improvement over their basis implementations and better agreement with both experiment and high level calculations. Furthermore, predicted adatom kinetics is in agreement with first-principles calculations. The binding energy of Pt particles as a function of size has been calculated by the extended embedded-atom method, essentially implying that the proposed technique can be added to any EAM implementations and improve the conventional EAM implementation on which it is based.

To conclude, the quality of a fit is primarily determined not by how many parameters are used, but by where these parameters are fitted to especially when the subject of interest is nanoparticles. This study, in principle, has identified the essential data that must be included in the fitting to remove uncertainties coming from the extrapolating nature of the conventional fitting, and has proven that the XEAM can be a generic solution to different EAM implementations. More important, this work has addressed the change in the bond characteristics not only as a function of coordination but also as a function of environment by including low coordination asymmetry, i.e. deviation from the jellium-like electron sea of bulk fcc metals. Combining these two improves the empirical potential, and reduces the inaccuracy of the embedded-atom method for the application in nanoparticle studies [33].

### Acknowledgements

We are grateful to M. I. Baskes for helpful discussions. B. Lee would like to thank R.E. Rudd for useful comments and discussions. This work was supported by NSF Grant No. EEC-0085569, and performed in part under the auspices of the US Department of Energy by the University of California, Lawrence Livermore National Laboratory, under Contract No. W-7405-Eng-48.

### References

[1] C.F. McFadden, P.S. Cremer, A.J. Gellman, Langmuir 12 (1996) 2483.
[2] R.F. Sabiryanov, M.I. Larsson, K. Cho, W.D. Nix, B.M. Clemens, Phys. Rev. B 67 (2003) 125412.
[3] M.S. Daw, M.I. Baskes, Phys. Rev. B 29 (1984) 6443.
[4] S.M. Foiles, M.I. Baskes, M.S. Daw, Phys. Rev. B 33 (1986) 7983.
[5] A.E. Carlsson, in: H. Ehrenreich, D. Turnbull (Eds.), Solid State Phys., vol. 43, Academic Press, New York, 1990.
[6] M.S. Daw, S.M. Foiles, M.I. Baskes, Mater. Sci. Rep. 9 (1993) 251.
[7] C.L. Cleveland, U. Landman, T.G. Schaaflf, M.N. Shafigullin, P.W. Stephens, R.L. Whetten, Phys. Rev. Lett. 79 (1997) 1873; M.D. Wolf, U. Landman, J. Phys. Chem. A 102 (1998) 6129.
[8] J.W.M. Frenken, P. Stolze, Phys. Rev. Lett. 82 (1999) 3500.
[9] B. Lee, K. Cho, Mater. Res. Soc. Symp. Proc. 775 (2003) P9.27.
[10] M.S. Daw, Phys. Rev. B 39 (1989) 7441.
[11] M.I. Baskes, Phys. Rev. B 46 (1992) 2727.
[12] E.B. Webb III, G.S. Grest, Phys. Rev. Lett. 86 (2001) 2066.
[13] M.I. Haftel, Phys. Rev. B 48 (1993) 2611.
[14] R. Pasianot, D. Farkas, E.J. Savino, Phys. Rev. B 43 (1991) 6952.
[15] F. Ercolessi, J.B. Adams, Europhys. Lett. 26 (1994) 583.
[16] I.J. Robertson, V. Heine, M.C. Payne, Phys. Rev. Lett. 70 (1993) 1944.
[17] Y. Mishin, D. Farkas, M.J. Mehl, D.A. Papaconstantopoulos, Phys. Rev. B 59 (1999) 3393.
[18] J. Cai, Y.Y. Ye, Phys. Rev. B 54 (1996) 8398.
[19] Y. Mishin, M.J. Mehl, D.A. Papaconstantopoulos, A.F. Voter, J.D. Kress, Phys. Rev. B 63 (2001) 224106.
[20] D.G. Pettifor, Bonding and Structure of Molecules and Solids, Clarendon Press, Oxford, 1995.
[21] G. Kresse, J. Furthmüller, Comput. Math. Sci. 6 (1996) 15.

[22] G. Kresse, J. Furthmüller, Phys. Rev. B 54 (1996) 11169.

[23] J. Perdew, A. Zunger, Phys. Rev. B 23 (1981) 5048.

[24] G. Boisvert, L.J. Lewis, M. Scheffler, Phys. Rev. B 57 (1998) 1881.

[25] P. van Beurden, G.J. Kramer, Phys. Rev. B 63 (2001) 165106.

[26] F.R. de Boer, R. Boom, W.C.M. Mattens, A.R. Miedema, A.K. Niessen, Cohesion in Metals, North-Holland, Amsterdam, 1988.

[27] M. Bott, M. Hohage, M. Morgenstern, T. Michely, G. Comsa, Phys. Rev. Lett. 76 (1996) 1304.

[28] G. Boisvert, L.J. Lewis, Phys. Rev. B 59 (1999) 9846.

[29] H. Brune, Karsten Bromann, Holger Röder, K. Kern, J. Jacobsen, P. Stoltze, K. Jacobsen, J. Nørskov, Phys. Rev. B 52 (1995) R14380.

[30] C. Ratsch, A.P. Seitsonen, M. Scheffler, Phys. Rev. B 55 (1997) 6750.

[31] M.I. Larsson et al., Mater. Res. Soc. Symp. Proc. 731 (2002) W3.14.

[32] B.-J. Lee, J.-H. Shim, M.I. Baskes, Phys. Rev. B 68 (2003) 144112.

[33] B. Lee, K. Cho, in preparation.
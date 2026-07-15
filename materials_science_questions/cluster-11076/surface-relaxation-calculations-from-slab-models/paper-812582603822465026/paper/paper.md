PCCP

Physical Chemistry Chemical Physics

Accepted Manuscript

This article can be cited before page numbers have been issued, to do this please use: M. Figueras, A. Jurado, A. Morales-Garcia, F. Viñes and F. Illas, Phys. Chem. Chem. Phys., 2020, DOI: 10.1039/D0CP03819A.

![](./images/812582603822465026_1.jpg)

This is an Accepted Manuscript, which has been through the Royal Society of Chemistry peer review process and has been accepted for publication.

Accepted Manuscripts are published online shortly after acceptance, before technical editing, formatting and proof reading. Using this free service, authors can make their results available to the community, in citable form, before we publish the edited article. We will replace this Accepted Manuscript with the edited and formatted Advance Article as soon as it is available.

You can find more information about Accepted Manuscripts in the Information for Authors.

Please note that technical editing may introduce minor changes to the text and/or graphics, which may alter content. The journal's standard Terms & Conditions and the Ethical guidelines still apply. In no event shall the Royal Society of Chemistry be held responsible for any errors or omissions in this Accepted Manuscript or any consequences arising from the use of any information it contains.

![](./images/812582603822465026_2.jpg)

rsc.li/pccp

# Bulk (in)stability as a possible source of surface reconstruction
View Article Online
DOI: 10.1039/D0CP03819A

Marc Figueras,‡ Anabel Jurado,‡ Ángel Morales-García, Francesc Viñes, Francesc Illas*

Departament de Ciència de Materials i Química Física & Institut de Química Teòrica i
Computacional (IQTCUB), Universitat de Barcelona. c/ Martí i Franquès 1-11, 08028
Barcelona, Spain

* Corresponding author e-mail: francesc.illas@ub.edu

‡ Both authors equally contributed

## Abstract
A density functional theory based study is presented with the aim of addressing
the surface energy stabilization mechanisms of transition metal carbide and nitride
surfaces from a crystal structure different from that of the most stable polymorph.
To this end, we consider the MoC(001), MoN(001), WC(001), and WN(001)
surface of rocksalt structures which, for these compounds, is not the most stable
one. The geometry optimization of suitable slab models shows that all these
surfaces undergo a sensible reconstruction. The energy difference per formula unit
between the rock salt and the most stable polymorph seems to be the driving force
behind the observed reconstruction. A note of caution is put in that certain small
periodic boundary conditions can artificially restrain such reconstructions, for
which at least $(2{	imes}2)$ supercells are needed. Also, it is shown that neglecting such a
surface reconstruction can lead to artifacts in the prediction of the chemical
activity and/or reactivity of these surfaces.

### Introduction

Well-defined surfaces can be experimentally prepared for a great variety of materials, including metals, oxides, nitrides and carbides, and their study and comprehension is actually one of the main focuses of the Surface Science scientific discipline.¹ Most often the low Miller indices surfaces are the most stable ones, where their surface atomic structure follows the periodicity of the corresponding bulk crystal structure. However, there are many cases where such ideally cut surfaces are not experimentally realized because they undergo relaxation and/or reconstruction processes. The former just implies a change in the atomic interlayer separation relative to the bulk crystal truncation while the latter does involve a change in the periodic symmetry with respect to bulk.¹ Both relaxation and reconstruction are ubiquitous with a large number of cases reported in the literature.² It is commonly accepted that relaxation and/or reconstruction processes occur because the ideal surface features an excessively large surface energy, which stems out from the energy cost of breaking the bonds of the surface atoms from its bulk environment so as to generate the surface.³ As a result, a given surface gets further stabilized when undergoing such processes reducing the surface formation energy costs. In other words, relaxation and reconstruction occur because the ideal surface is, intrinsically, unstable. This explanation must necessarily hold when, under normal working conditions, the corresponding bulk is the most stable polymorph. Recently, it has been shown for a series of transition metals higher in energy that polymorphs feature surfaces relaxed more than expected, thus lowering the surface energy so as to compensate the inherent bulk instability.⁴ However, predicting whether a given well-defined surface will reconstruct or not is generally unfeasible without the help of a theory behind. For compounds with several stable polymorphs one may wonder whether the surfaces of the non-most stable polymorph inherit somehow the lack of stability, which, consequently, would lead to as well to a further reconstruction.

In the present work, we explore the hypothesis of whether the surface reconstruction naturally emerges for metastable polymorphs by analyzing the stability of most stable (001) surfaces of MoC, WC, MoN, and WN displaying a cubic $Fm3m$ rocksalt crystal structures. For binary transition metal and carbides and nitrides such as of Ti, Zr, Hf, V, Nb, and Ta, such rocksalt crystal structure is


indeed the most stable polymorph under standard conditions of pressure and temperature,⁵ and the (001) surface is the most stable one, exhibiting just a small rumpling in which metal and non-metal atoms relax vertically with respect to the surface, yet in opposite directions.⁶ However, for the four compounds earlier mentioned, the most stable structure has a hexagonal symmetry; $P6_3/mmc$ for MoN⁷ and $P\overline{6}m2$ for MoC, WC, and WN;⁵ although their $Fm3m$ rocksalt cubic form also exists under other somewhat harsher conditions. For instance, cubic MoC —usually referred to as δ-MoC— is broadly used in model studies in catalysis even if, to date, it has not been possible to prepare single crystals,⁸·⁹ and only acquired in the form of nanocrystallites. The rocksalt WC (γ-WC), though, has actually been prepared long ago and its crystal structure reported,¹⁰ whereas the cubic form of MoN and WN has also been reported, although at high temperature conditions¹¹ or in the form of thin films.¹² The variety of casuistry of such compounds, but at the same time being of the same family of transition metal carbide or nitride compounds thus constitute them as an ideal set to test the aforementioned hypothesis that the existence of a lower energy polymorph prompts a surface reconstruction, even in the most stable featured surfaces.

Computational details

The stability of the (001) surfaces of δ-MoC, γ-WC, and $Fm3m$ MoN and WN has been studied by means of periodic density functional theory (DFT) based calculations employing the broadly used Perdew-Burke-Ernzerhof (PBE)¹³ exchange-correlation functional within the generalized gradient approach (GGA). All calculations have been carried out with the VASP code,¹⁴ where the valence electron density has been expanded by a plane wave basis set with a 415 eV cutoff for the kinetic energy, whereas the effect of the core electrons on the valence density has been accounted through the projector augmented-wave (PAW) method.¹⁵ Numerical integrations have been carried out in the reciprocal space at the **k**-points nodes generated through optimal Monkhorst-Pack meshes. The variations on the total energy due to the using of a larger basis set or the use of denser **k**-point meshes have been found to be converged below 0.01 eV (see also Table S1 in the electronic supplementary information (ESI)).

The (001) surfaces of interest have been represented by slab models cut from the PBE optimized bulk structure, using a regular cubic unit cell and a **k**-

point meshes of 17×17×17 dimensions. The same $\mathbf{k}$-points density has been used to optimize the hexagonal crystal cells of the explored materials. The (001) surface slab models have been constructed displaying four atomic layers, with the two outermost ones allowed to relax, and the two innermost frozen at the bulk geometry —the so-known 2+2 scheme—, with a vacuum width of 15 Å between the interleaved slabs. For the purposes of the present work, these slab models should be enough to reach a sound conclusion, especially in what concerns the plane-wave kinetic energy cutoff and the vacuum width between the periodically repeated slabs. This is further supported by results reported in ESI involving a tighter energy cutoff and a larger vacuum width. The influence of the slab thickness has also been considered as described in detail in the next section.

Different supercells of increasing size have been used so as to tackle the surface stability. In particular, $(\sqrt{N} \times \sqrt{N}) \text{R}45^\circ$ supercells have been considered, with N = 1-4. However, for simplicity, we denote these hereafter as (N×N) supercells, for which the numerical integrations we use optima $\mathbf{k}$-point meshes of 9×9×1, 5×5×1, 3×3×1 for N = 1 to 3, respectively, and $\boldsymbol{\Gamma}$ point optimizations for the (4×4) supercell. Notice that, for a stable surface, the calculated surface energy does not depend on the size of the supercell used. However, for unstable surfaces the use of an excessively small supercell may lead to misleading results, as the structural optimization may be biased by the constrains imposed by an artificial periodic symmetry. In that case, a frequency (phonon) calculation will clearly show that the structure is not dynamically stable. On the other hand, larger supercells provide additional degrees of freedom so that the geometry optimization may result on a different surface structure with a lower surface energy; a clear fingerprint that the surface is likely to undergo a reconstruction. A plausible reconstruction pattern is proposed based on the minimization of the imaginary frequencies for every surface model. However, it must be pointed that the encountered reconstruction pattern cannot, in any case, be considered as the global minimum, since following the imaginary frequencies paths only ensure the characterization of a local minimum. The subsequent research of a global minimum is out of the current scope. Note, in addition, that this quest for global minimum requires much larger models that drive the computational cost excessively up. In any case, the stability of the reported reconstruction is

supported by a series of additional calculations involving different initial reconstruction patterns in the (4×4) MoC supercell as shown in the ESI. The fact that all proposed initial patterns converge to the reconstruction pattern displayed in Figure 1 provides strong support to the claim that the ideal surface is unstable and if prepared in UHV conditions by appropriate cleave, it will undergo a reconstruction. To provide more quantitative data and support the abovementioned statements, we focus on the surface energy of the relaxed slab surface, $\gamma^{rel}$, usually defined as

$$
\gamma^{rel} = \frac{E_{slab}^{rel} - nE_{bulk}}{2A} \tag{1},
$$

where $E_{slab}^{rel}$ is the total energy of the fully relaxed slab, while $E_{bulk}$ stands for the bulk energy per formula unit, $n$ is the number of formula units repeated in the slab model, and, finally, $A$ corresponds to the created area on one side of the slab model. By construction, Eq. (1) requires a full relaxation of the slab surface model and since it must provide a suited bulk environment to the surface atomic layers, this implies using a rather large number of atomic layers. Alternatively, one can provide the bulk environment to the surface region by keeping the bottom layers fixed, *i.e.* the 2+2 scheme described earlier. In this type of models, $\gamma^{rel}$ is computed in two steps:¹⁶ First, the bulk-truncated surface energy is defined as

$$
\gamma^{fix} = \frac{E_{slab}^{fix} - nE_{bulk}}{2A} \tag{2},
$$

which is similar to Eq. (1) but with $E_{slab}^{fix}$ corresponding to the bulk-truncated energy of the slab model, this is, with all atoms at the bulk environment positions. Then, $\gamma^{rel}$ is calculated as:

$$
\gamma^{rel} = \frac{E_{slab}^{rel} - nE_{bulk}}{A} - \gamma^{fix} \tag{3}.
$$

This approach allows one to significantly reduce the computational burden since it involves slab models with a smaller number of atomic layers and, in addition, not all need to be relaxed. The computational saving is especially important for large supercells where the use of thicker slabs can become computationally prohibitive.

## Results and discussion

We start the discussion of results by commenting on the optimized lattice parameters for the cubic $Fm3m$ structures of MoC, WC, MoN, and WN, listed in Table 1 and compared to experimental available data and previous calculated results.¹⁶⁻²² Not surprisingly, the present values for the calculated lattice parameters are in good agreement with previous work and nicely agrees with the available experimental data. However, in some cases the maximum absolute value is of ~0.1 Å for MoC and WC and ~0.2 Å for MoN representing maximum relative errors of only ~2% in general, up to ~4% for the MoN particular case. For the latter, the error is larger than the average one for crystal structures predicted by DFT methods and, in the view of the metastable character of these polymorphs and their synthesis difficulty, we attribute, at least in part, this discrepancy to a lack of accuracy to problems in the experiments, which cannot be discarded.

Next, we analyze first the bulk truncated surface energy for the four explored surfaces. As defined in the computational details, this quantity corresponds to the surface energy of the generated slab without allowing any surface relaxation or reconstruction. The reason to include this purely theoretical quantity is that it provides a self-check on the computational models and methods, as the obtained values for the (2×2), (3×3), and (4×4) supercells must coincide with that of the (1×1) supercell. In the case of using a plane wave basis sets, small differences may be present because, for a given cutoff, the density of plane waves in the supercell differ, leading in each case to a somehow different quality of the basis set, and a similar slight change is to be expected on the **k**-point density. However, the $\gamma^{fix}$ results compiled in Table 2 show that these differences are minimal, thus validating the present approach. Furthermore, the results align with those already found for transition metal surfaces,⁴ insomuch the more unstable the cubic bulk crystal structure is with respect the most stable hexagonal one, see Table 3, the lower is the $\gamma^{fix}$ surface energy. Thus, such a rule-of-a-thumb seems to be more general, and applicable beyond the transition metals materials family.

Now we analyze the results corresponding to the surface energy as predicted from the different supercells. For the sake of simplicity we will focus on the case of $\delta$-MoC (001), where the relaxation of the (1×1) unit cell after cleavage leads to the typical rumpling of the surface atoms as observed for most of the cubic transition metal carbides,²³ while preserving the $Fm3m$ cubic symmetry.

This structure has actually been often taken as the ground state for this particular surface as a frequency analysis of the relaxed layers, gained by Hessian matrix construction by discrete displacements of $0.03$ Å and its diagonalization, displays only positive values. Interestingly, though, the interaction of Ni, Cu, and Au atoms on this surface has shown that an adsorbate induced reconstruction takes place as revealed for low coverage situations and, hence, large supercells.²⁴

At this point one may still wonder whether the reconstruction is really triggered by the adsorbate, or its absence was due to the use of a too small unit cell. Doubling the unit cell and relaxing the atomic structure of the top two layers still leads to a symmetric structure preserving that of the $(1{\times}1)$ supercell. However, in this case, the frequency analysis reveals the presence of imaginary frequencies. Indeed, a further geometry optimization starting from a slightly distorted structure along the imaginary vibration leads to a new energy minimum characterized by solely positive frequencies and resulting in a lower surface energy, as shown in Table 2.

This new structure does not preserve the original symmetry and can then be defined as the result of a surface reconstruction. To further confirm that this is a stable structure, calculations have been repeated for larger $(3{\times}3)$ and $(4{\times}4)$ supercells. In both cases, the final structures do not exhibit imaginary frequencies. In the case of the $(3{\times}3)$ supercell, though, the surface energy is slightly higher than the $(2{\times}2)$ one, we attribute this to the fact that this supercell does not fully duplicate the $(2{\times}2)$, and so one still introduces an artificial distortion. This is confirmed by the results obtained for the $(4{\times}4)$ supercell, which are identical to those of the $(2{\times}2)$ indicating that the convergence is reached.

The reconstructed surface implies a rather large change in the position of the atoms of the relaxed layers (Figure 1). At this point one may wonder whether the thickness of the slab surface model is enough to reach sound conclusions. To investigate the influence of slab thickness on the present findings, a new series of calculations has been carried out by considering the $(2{\times}2)$ MoC supercell but including eight atomic layers with the six outermost fully relaxed and the two bottommost fixed as in the bulk, i.e. a 6+2 scheme. For the starting structure, both models (four or eight atomic layers) lead to the same surface energy, as expected

and clearly seen in Table S2 in the ESI. For the relaxed structures there is a noticeable influence of the slab thickness that, in the view of the reconstruction of the upper atomic layers, is not at all surprising. The surface energy of the thicker slab becomes noticeably lower. However, this does not affect the reconstruction pattern and, hence, fully confirms the trends emerging from the four-layer models.

Even though the outcome of the calculations for the $\delta$-MoC surface models is quite straightforward, the (001) surfaces of MoN, WC, and WN do not converge as flawless as $\delta$-MoC(001). In fact, the WN $(4{\times}4)$ reconstruction pattern ends up being the same as in the $(3{\times}3)$ supercell, meaning that convergence has been reached anyway, but not in the same way as for $\delta$-MoC (001). The structure of the unreconstructed and reconstructed $(2{\times}2)$ supercell of the $\delta$-MoC (001) is shown in Figure 1, while the same information for the rest of structures can be found in the ESI. The fact that $\delta$-MoC (001) surface exhibits this type of reconstruction can have some implications on earlier studies where this surface reconstruction has not been taken into account. In particular, the somewhat stronger $CO_2$ adsorption on the $\delta$-MoC (001) compared to other transition metal carbides made it an outlier. Such $CO_2$ capture was explored at relatively low coverage$^{25}$ and so it seems that the stronger attachment of the $CO_2$ is a consequence of utilizing a relatively large supercell. Computing the adsorption energy with respect to the reconstructed MoC (001) surface leads to a smaller value by 0.60 eV, which thus turns in line with that of the rest of transition metal carbides.

The situation for the rest of surfaces studied in the present work is very similar and so could be the consequence of their neglecting. In all other cases, a reconstruction shows up when going from the $(1{\times}1)$ to the $(2{\times}2)$ supercell accompanied by a reduction of the surface energy, and only slightly increasing for the $(3{\times}3)$ supercell, again because this implies an artificial distortion, and so the actual value converges to the $(2{\times}2)$ value for the largest $(4{\times}4)$ supercell, see Table 2, and a view of the structures in the ESI. The only difference with respect to the case of $\delta$-MoC is that the geometry optimization applied on the $(2{\times}2)$ directly leads to the reconstructed structures without further ado. A surprising point is that nitrogen-based materials, MoN and WN, feature negative surface energies when

relaxed; however, such a result should not be regarded as a degradation indication of such materials. What it seems to happen is that the surface reconstruction is driven by the bulk crystal structure instability, see below, and so, the surface reconstructs so as to partially change its phase back to a hexagonal environment. Consequently, part of the bulk instability is saved due to the reconstructions, and, so, this energy lowering is substantially contributing to the surface energy lowering.

One can thus take the (2×2) supercells to carry out a geometry analysis of the distortions, as shown in Figure 1 and Figure S2 (ESI). The metal-carbon distances, $d(\text{MC})$, expand/contract across the surface and subsurface layers, and so does happen with the angles, $\alpha$. From the values in Table 3, one could argue that the reconstructions shape is kept when going to the subsurface layer, as the $a$ values are kept just about constant; however the degree of reconstruction, sized by the $d(\text{MC})$ diminishes, and, so, the reconstruction is more of a surface process that dilutes when penetrating the material.

Last, it is important to relate the difference in energy in between the more unstable cubic crystal cell and most-stable hexagonal one, listed as $\Delta E$ in Table 3, with the extent of the surface reconstruction. A detailed inspection reveals that, similarly to the aforementioned $\gamma^{fix}$ trend, the more unstable the cubic cell is, the lower is the $\gamma^{rel}$, and, therefore, the larger is the reconstruction. This is also observable in the geometry changes, especially on the first surface layer, reported in Table 3; the larger the difference in bulk stability with respect to the most stable polymorph, the larger the distances and angles distortions are. Thus, this seems to be a clear indication that the observed reconstruction relates to the fact that the crystal structure of these polymorphs is not the most stable one, which *de facto* acts as a driving factor, likely implying distortions of the surface as much as possible so as to cover the energetic and geometric distance with respect the hexagonal crystal cell environment, and, ultimately, expressing reconstructed surfaces whose activity may well be different from the regular rocksalt (001) ones, and different from the hexagonal crystal structures surfaces.

## Conclusions

The present theoretical work addresses the relaxation or reconstruction processes occurring on the surfaces of transition metal carbide and nitride materials displaying a bulk crystallographic structure (rocksalt) higher in energy compared to the most stable one (hexagonal). In this sense, the (001) surfaces of rocksalt crystal structures of MoC, MoN, WC, and WN have been modeled and optimized, revealing that such undergo a surface reconstruction, which can be artificially masked when imposing certain small periodic boundary conditions. This is normally avoided when using larger supercell models, here revealing that a convergence can be already reached by using $(2{\times}2)$ supercells.

The bulk truncated surface energies follow the trend of the larger the bulk instability is, the smaller the surface energy, as earlier found on transition metal systems. Furthermore, the degree of relaxation, seized in energetic terms, in variations of the metal-carbon distances, or in variations of the layer angles does follow the bulk instability, but showing that such reconstruction extent dilutes when going towards the interior of the material. All in all, the present study reveals the proper depiction of such surfaces as necessary, as such can affect the overall materials surface chemistry.

## Acknowledgments
The research in this work has been supported by the Spanish MICIUN RTI2018-095460-B-I00 and *María de Maeztu* MDM-2017-0767 grants, and, in part, by *Generalitat de Catalunya* 2017SGR13 grant and COST Action CA18234. A. M.-G. thanks to Spanish MICIUN for a *Juan de la Cierva* postdoctoral grant (IJCI-2017-31979), and F. I. acknowledges additional support from the 2015 ICREA Academia Award for Excellence in University Research.

Table 1. Calculated (PBE) and experimental (Exp.) lattice parameters for the cubic, rocksalt $Fm\overline{3}m$ crystal structures of MoC, WC, MoN, and WN, as well as comparison to previously calculated values found in the literature (Lit.). All values are given in Å.

<table>
  <thead>
    <tr>
      <th></th>
      <th>MoC</th>
      <th>WC</th>
      <th>MoN</th>
      <th>WN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Exp.</td>
      <td>4.278<sup>a</sup></td>
      <td>4.266<sup>b</sup></td>
      <td>4.110<sup>c</sup></td>
      <td>—</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>4.252<sup>d</sup></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Lit.</td>
      <td>4.373<sup>e</sup></td>
      <td>—</td>
      <td>4.304<sup>f</sup></td>
      <td>4.351<sup>g</sup></td>
    </tr>
    <tr>
      <td>PBE</td>
      <td>4.342</td>
      <td>4.387</td>
      <td>4.346</td>
      <td>4.357</td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <td colspan="5">
        <sup>a</sup> Ref. 22, <sup>b</sup> Ref. 17, <sup>c</sup> Ref. 19, <sup>d</sup> Ref. 18, <sup>e</sup> Ref. 16, <sup>f</sup> Ref. 20, <sup>g</sup> Ref. 21.
      </td>
    </tr>
  </tfoot>
</table>

Table 2. Calculated relaxed surface energies, $\gamma^{rel}$, in J/m², for the different supercells used to represent the different (001) surfaces. The bulk-truncated, fix surface energies, $\gamma^{fix}$, are given in parenthesis.

<table>
  <thead>
    <tr>
      <th colspan="2">Supercell</th>
      <th>(1×1)</th>
      <th>(2×2)</th>
      <th>(3×3)</th>
      <th>(4×4)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>MoC</td>
      <td>$\gamma^{fix}$</td>
      <td>1.41</td>
      <td>1.41</td>
      <td>1.41</td>
      <td>1.41</td>
    </tr>
    <tr>
      <td></td>
      <td>$\gamma^{rel}$</td>
      <td>0.77</td>
      <td>0.67</td>
      <td>0.70</td>
      <td>0.67</td>
    </tr>
    <tr>
      <td>WC</td>
      <td>$\gamma^{fix}$</td>
      <td>1.43</td>
      <td>1.43</td>
      <td>1.44</td>
      <td>1.43</td>
    </tr>
    <tr>
      <td></td>
      <td>$\gamma^{rel}$</td>
      <td>0.66</td>
      <td>0.59</td>
      <td>0.62</td>
      <td>0.61</td>
    </tr>
    <tr>
      <td>MoN</td>
      <td>$\gamma^{fix}$</td>
      <td>1.11</td>
      <td>1.11</td>
      <td>1.09</td>
      <td>1.11</td>
    </tr>
    <tr>
      <td></td>
      <td>$\gamma^{rel}$</td>
      <td>-0.77</td>
      <td>-0.75</td>
      <td>-0.67</td>
      <td>-0.79</td>
    </tr>
    <tr>
      <td>WN</td>
      <td>$\gamma^{fix}$</td>
      <td>1.07</td>
      <td>1.06</td>
      <td>1.07</td>
      <td>1.06</td>
    </tr>
    <tr>
      <td></td>
      <td>$\gamma^{rel}$</td>
      <td>-1.57</td>
      <td>-1.35</td>
      <td>-1.81</td>
      <td>-1.83</td>
    </tr>
  </tbody>
</table>

Table 3. Geometric parameters of the surface layer (surf) or the first subsurface layer (sub) for the different explored reconstructed (001) surfaces, including the variation of metal-carbon distances with respect that of the unreconstructed surface, $d(\text{CO})$, in Å, and the changes of in-plane angles, $\alpha$, in degrees. Finally, the difference in energy in between cubic and hexagonal bulk structures, $\Delta\text{E}$, is provided, given per formula unit and in eV.

<table>
  <thead>
    <tr>
      <th></th>
      <th>MoC</th>
      <th>WC</th>
      <th>MoN</th>
      <th>WN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$d(\text{CO})^{\text{surf}}$</td>
      <td>±0.18</td>
      <td>±0.17</td>
      <td>±0.07</td>
      <td>±0.32</td>
    </tr>
    <tr>
      <td>$d(\text{CO})^{\text{sub}}$</td>
      <td>±0.05</td>
      <td>±0.05</td>
      <td>±0.05</td>
      <td>±1.24</td>
    </tr>
    <tr>
      <td>$\alpha^{\text{surf}}$</td>
      <td>±10</td>
      <td>±10</td>
      <td>±13</td>
      <td>±13</td>
    </tr>
    <tr>
      <td>$\alpha^{\text{sub}}$</td>
      <td>±10</td>
      <td>±12</td>
      <td>±12</td>
      <td>±37</td>
    </tr>
    <tr>
      <td>$\Delta\text{E}$</td>
      <td>0.40</td>
      <td>0.69</td>
      <td>0.62</td>
      <td>0.81</td>
    </tr>
  </tbody>
</table>

Figure 1. First (top panels) and second (bottom panels) atomic layer for fixed (bulk-truncated) vs. reconstructed (2×2) supercells of the δ-MoC (001) surface.
Violet and black spheres correspond to Mo and C atoms, respectively.

![](./images/812582603822465026_3.jpg)

## References

$^{1}$ G. A. Somorjai and Y. Li, *Introduction to Surface Chemistry and Catalysis*, $2^\text{nd}$ dition, John Wiley & Sons, 2010.

$^{2}$ C. B. Duke, *Chem. Rev.*, 1996, **96**, 1237-1260.

$^{3}$ J. Ruvireta, L. Vega and F. Viñes, *Surf. Sci.*, 2017, **664**, 45-49.

$^{4}$ H. Lin, J.-X. Liu, H. Fan, W.-X. Li, *J. Phys. Chem. C*, 2020, **124**, 11005-11014.

$^{5}$ J. G. Chen, *Chem. Rev.*, 1996, **96**, 1477-1498.

$^{6}$ F. Viñes, C. Sousa, P. Liu, J.A. Rodriguez and F. Illas, *J. Chem. Phys.*, 2005, **122**, 174709.

$^{7}$ C. L. Bull, P. F. McMillan, E. Soignard and K, Leinenweber, *J. Solid State Chem.*, 2004, **177**, 1488-1492.

$^{8}$ S. Posada-Pérez, F. Viñes, P. J. Ramirez, A. B. Vidal, J. A. Rodriguez and F. Illas, *Phys. Chem. Chem. Phys.*, 2014, **16**, 14912-14921.

$^{9}$ S. Posada-Pérez, P. Ramírez, F. Viñes, P. Liu, F. Illas and J. A. Rodriguez, *J. Am. Chem. Soc.*, 2016, **138**, 8269-8276.

$^{10}$ R. H. Willens and E. Buehler, *Appl. Phys. Lett.*, 1965, **7**, 25.

$^{11}$ L. E. Toth, *Transition Metal Carbides and Nitrides*, Academic, New York, 1971.

$^{12}$ P. Hones, N. Martin, M. Regula and F. Lévy, *J. Phys. D: Appl. Phys.*, 2003, **36**, 1023.

$^{13}$ J. P. Perdew, K. Burke and M. Ernzerhof, *Phys. Rev. Lett.*, 1996, **77**, 3865-3868.

$^{14}$ G. Kresse and J. Furthmüller, *Phys. Rev. B*, 1996, **54**, 11169-11186.

$^{15}$ P. E. Blöch, *Phys. Rev. B*, 1994, **50**, 17953-17979.

$^{16}$ J. R. S. Politi, F. Viñes, J. A. Rodriguez and F. Illas, *Phys. Chem. Chem. Phys.*, 2013, **15**, 12617-12625.

$^{17}$ A. S. Kurlov and A. I. Gusev, *Inorg. Mater.*, 2006, **42**, 121-127.

$^{18}$ A. S. Kurlov and A. I. Gusev, *Russ. Chem. Rev.*, 2006, **75**, 617-636.

$^{19}$ H. Jehn and P. Ettmayer, *J. Less Common. Met.*, 1978, **58**, 85-98.

$^{20}$ M. B. Kanoun, S. Goumri-Said and M. Jaouen, *Phys. Rev. B*, 2007, **76**, 134109.

$^{21}$ J. Qin, X. Zhang, Y. Xue, X. Li, M. Ma and R. Liu, *Comput. Mater. Sci.*, 2013, **79**, 456-462.

$^{22}$ A. Fernández-Guillermet, J. Häglund and G. Grimvall, *Phys. Rev. B*, 1992, **45**, 11557-11567.

$^{23}$ F. Viñes, C. Sousa, P. Liu, J.A. Rodriguez and F. Illas, *J. Chem. Phys.*, 2005, **122**, 174709.

$^{24}$ G. Giacomo Asara, F. Viñes, J. M. Ricart, J. A. Rodriguez and F. Illas, *Surf. Sci.*,
2014, **624**, 32-36.

$^{25}$ C. Kunkel, F. Viñes and F. Illas, *Energy Environ. Sci.*, 2016, **9**, 141-144.

### Graphical abstract for TOC

![](./images/812582603822465026_4.jpg)
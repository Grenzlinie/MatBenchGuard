
# General Theory for the Ferroelectric Polarization Induced by Spin-Spiral Order

H. J. Xiang \( ^{1*} \) , E. J. Kan \( ^{2} \) , Y. Zhang \( ^{3} \) , M.-H. Whangbo \( ^{3†} \) , and X. G. Gong \( ^{1‡} \) 

 \( ^{1} \)  Key Laboratory of Computational Physical Sciences (Ministry of Education), and Department of Physics, Fudan University, Shanghai 200433, P. R. China

 \( ^{2} \)  Department of Applied Physics, Nanjing University of Science and Technology, Nanjing, Jiangsu 210094, P. R. China

 \( ^{3} \)  Department of Chemistry, North Carolina State University, Raleigh, North Carolina 27695-8204, USA

## Abstract

The ferroelectric polarization of triangular-lattice antiferromagnets induced by helical spin-spiral order is not explained by any existing model of magnetic-order-driven ferroelectricity. We resolve this problem by developing a general theory for the ferroelectric polarization induced by spin-spiral order and then by evaluating the coefficients needed to specify the general theory on the basis of density functional calculations. Our theory correctly describes the ferroelectricity of triangular-lattice antiferromagnets driven by helical spin-spiral order, and incorporates known models of magnetic-order-driven ferroelectricity as special cases.
 

Multiferroics, displaying magnetic, polar and elastic order parameters simultaneously, present fascinating fundamental physics [1,2] and potentially promising applications [3]. Spin-spiral multiferroics [1,4,5] constitute a challenging and interesting class of ferroelectricity in which the ferroelectric polarization P is induced by a magnetic order that removes inversion symmetry. For multiferroics with cycloidal spiral-spin order (e.g., TbMnO \( _{3} \)  [6-8] and MnWO \( _{4} \)  [9,10]), the ferroelectricity is explained by the inverse Dzyaloshinskii-Moriya (DM) interaction [11] or, equivalently, by the spin current model of Katsura, Nagaosa and Balatsky (KNB) [12], leading to P \( _{ij} \)  ∝ e \( _{ij} \) ×(S \( _{i} \) ×S \( _{j} \) ), where e \( _{ij} \)  is a unit vector connecting the two adjacent spins S \( _{i} \)  and S \( _{j} \) . This model predicts that P is perpendicular to the direction of the magnetic modulation q ∝ e \( _{ij} \)  (i.e., P ⊥ q). Triangular-lattice antiferromagnets such as CuFeO \( _{2} \)  and AgCrO \( _{2} \), also exhibit ferroelectricity when they adopt a helical spiral-spin order [13-15], in which the plane of the spin rotation is perpendicular to q. CuFeO \( _{2} \)  shows ferroelectric polarization when its magnetic structure has a helical spin-spiral order with q = (Q, Q, 0), where Q ≈ 1/3. The layered iodide MnI \( _{2} \)  was also found to be a multiferroic with helical spin-spiral order [16]. The experimental studies on CuFeO \( _{2} \)  and MnI \( _{2} \) , show that the P in the helical spin-spiral state with q = (Q, Q, 0) is parallel to q (i.e., P ∥ q). This finding is not explained either by the symmetric exchange striction mechanism or by the KNB model. The charge transfer between metal and ligand induced by spin-orbit coupling (SOC) was considered responsible for the ferroelectric polarization in a triangular lattice with helical spin-spiral order [17] with the prediction P \( _{ij} \)  ∝ (e \( _{ij} \) ·S \( _{i} \) )S \( _{i} \)- (e \( _{ij} \) ·S \( _{j} \) )S \( _{j} \). This polarization, known as the “bond polarization” [18], lies in the plane spanned by S \( _{i} \)  and S \( _{j} \) , which is perpendicular to q, and hence contradicts the experimental observation [14,16,19] that P ∥ q when q = (Q, Q, 0). In short, to explain the ferroelectric polarization of triangular-lattice
 

antiferromagnets with helical spin-spiral order, it is necessary to develop a general theory for the ferroelectric polarization driven by spin-spiral order.

In this Letter we resolve the aforementioned issue first by developing a general theory for the ferroelectric polarization induced by spin-spiral on the basis of symmetry considerations and then by evaluating the coefficients needed to specify the general theory on the basis of density functional calculations for  \( MnI_{2} \)  as a representative example. We demonstrate that our theory correctly describes the ferroelectric polarization of  \( MnI_{2} \) , and the existing models of magnetic-order-driven ferroelectricity are special cases of our theory.

Let us first consider a spin dimer (i.e., a pair of adjacent spin sites) with spatial inversion symmetry at the center. Without loss of generality, the propagation vector from spin 1 to spin 2 will be taken along the x-axis. A noncollinear spin arrangement of the dimer removes the inversion symmetry and hence induces ferroelectric polarization P. In general, P is a function of the directions of spin 1 and spin 2 (with unit vectors  \( S_{1} \)  and  \( S_{2} \) , respectively), namely,  \( \mathbf{P} = \mathbf{P}(\mathbf{S}_{1x}, \mathbf{S}_{1y}, \mathbf{S}_{12}, \mathbf{S}_{2x}, \mathbf{S}_{21}, \mathbf{S}_{22}) \) . In principle, therefore, P can be expanded as a Taylor series of  \( S_{i\alpha} \)  (i = 1, 2;  \( \alpha = x, y, z \) ). The time-reversal symmetry requires that inverting both spin directions leave the electric polarization unchanged. Thus, the odd terms of the Taylor expansion should vanish. If the fourth and higher order terms are neglected, P is written as

 \[ \mathbf{P}=\mathbf{P}_{1}(\mathbf{S}_{1})+\mathbf{P}_{2}(\mathbf{S}_{2})+\mathbf{P}_{12}(\mathbf{S}_{1},\mathbf{S}_{2}), \quad (1) \] 

where the intra-site polarization  \( \mathbf{P}_{i}(\mathbf{S}_{i}) \)  (i = 1, 2) and the inter-site polarization  \( \mathbf{P}_{12}(\mathbf{S}_{1}, \mathbf{S}_{2}) \)  are given by

 \[ \begin{aligned}&\mathbf{P}_{1}(\mathbf{S}_{1})=\sum_{\alpha\beta}\mathbf{P}_{1}^{\alpha\beta}\mathbf{S}_{1\alpha}\mathbf{S}_{1\beta},\\&\mathbf{P}_{12}(\mathbf{S}_{1},\mathbf{S}_{2})=\sum_{\alpha\beta}\mathbf{P}_{12}^{\alpha\beta}\mathbf{S}_{1\alpha}\mathbf{S}_{2\beta}.\\ \end{aligned} \quad (2) \]
 

Here the expansion coefficients,  \( P_{i}^{\alpha\beta} \)  and  \( P_{12}^{\alpha\beta} \) , are vectors. The above expressions show that  \( P_{i}^{\alpha\beta} = P_{i}^{\beta\alpha} \) ,  \( \mathbf{P}_{i}(\mathbf{S}_{i}) = \mathbf{P}_{i}(-\mathbf{S}_{i}) \) , and  \( \mathbf{P}_{12}(-\mathbf{S}_{1}, \mathbf{S}_{2}) = \mathbf{P}_{12}(\mathbf{S}_{1}, -\mathbf{S}_{2}) = -\mathbf{P}_{12}(\mathbf{S}_{1}, \mathbf{S}_{2}) \) . From these relationships, together with the use of spatial inversion symmetry and time-reversal symmetry, one can show that  \( P_{1}^{\alpha\beta} = -P_{2}^{\alpha\beta} \) , and  \( P_{12}^{\alpha\beta} = -P_{12}^{\beta\alpha} \)  [20]. The latter relation shows that the diagonal coefficients  \( P_{12}^{\alpha\alpha} = 0 \) , so the inter-site polarization can be expressed as

 \[ \mathbf{P}_{12}=\mathbf{P}_{12}^{\mathrm{y z}}\left(\mathbf{S}_{1}\times\mathbf{S}_{2}\right)_{x}+\mathbf{P}_{12}^{\mathrm{x z}}\left(\mathbf{S}_{1}\times\mathbf{S}_{2}\right)_{y}+\mathbf{P}_{12}^{\mathrm{x y}}\left(\mathbf{S}_{1}\times\mathbf{S}_{2}\right)_{z}, \quad (3a) \] 

where  \( (\mathbf{S}_{1}\times\mathbf{S}_{2})_{\alpha} \)  refers to the  \( \alpha \)  (= x, y, z) component of the vector  \( (\mathbf{S}_{1}\times\mathbf{S}_{2}) \) . Using similar notations for the x, y and z components of the vectors  \( P_{12}^{\alpha\beta} \) , Eq. 3a is rewritten as

 \[ \mathbf{P}_{12}=\mathbf{M}\left(\mathbf{S}_{1}\times\mathbf{S}_{2}\right) \quad (3b) \] 

using the  \( 3 \times 3 \)  matrix M

 \[ \mathbf{M}=\begin{bmatrix}\left(\mathbf{P}_{12}^{\mathrm{yz}}\right)_{x}&\left(\mathbf{P}_{1}^{2\mathrm{x}}\right)_{x}&\quad\left(\mathbf{P}_{12}^{\mathrm{xy}}\right)_{x}\\\left(\mathbf{P}_{12}^{\mathrm{yz}}\right)_{y}&\left(\mathbf{P}_{1}^{2\mathrm{y}}\right)_{y}&\quad\left(\mathbf{P}_{12}^{\mathrm{xy}}\right)_{y}\\\left(\mathbf{P}_{12}^{\mathrm{yz}}\right)_{z}&\left(\mathbf{P}_{1}^{2\mathrm{z}}\right)_{z}&\quad\left(\mathbf{P}_{12}^{\mathrm{xy}}\right)_{z}\end{bmatrix}. \quad (4) \] 

Given that the propagation vector from spin 1 to spin 2 is taken along the x-axis, the bond polarization model [18] is a special case of the intra-site polarization in which the only nonzero coefficients are  \( \mathbf{P}_{1}^{\mathrm{xx}} = (\mathrm{C}, 0, 0) \) ,  \( \mathbf{P}_{1}^{\mathrm{xy}} = \mathbf{P}_{1}^{xy} = (0, \mathrm{C}/2, 0) \)  and  \( \mathbf{P}_{1}^{\mathrm{xz}} = \mathbf{P}_{1}^{xz} = (0, 0, \mathrm{C}/2) \) , where C is a constant. The KNB model is a special case of the inter-site polarization with  \( (\mathbf{P}_{12}^{\mathrm{xx}})_{z} = -(\mathbf{P}_{12}^{\rm xy})_{y} = \mathrm{C} \)  as the only nonzero elements of M, where C is a constant. The inter-site polarization given by Eq. 3b may now be referred to as the generalized KNB (gKNB) model. For a linear three-atom M-L-M model (M = transition-metal, L = main-group ligand), the intra-site term reduces to the bond polarization model, and the inter-site term to the KNB model.
 

To specify the intra-site and inter-site polarizations described above, one needs to determine the expansion coefficients  \( \mathbf{P}_{i}^{\alpha\beta} \)  (i = 1, 2) and  \( P_{12}^{\alpha\beta} \) . We evaluate these coefficients for a spin dimer of  \( MnI_{2} \)  (Fig. 1(a)) as a representative example, on the basis of density functional calculations. We adopt the LDA+U+SOC approach to calculate electric polarizations [20].  \( MnI_{2} \)  crystallizes in the  \( CdI_{2} \) , type structure with  \( MnI_{2} \)  layer stacked along the c axis [see the left inset of Fig. 1(a)]. In the Mn triangular lattice, each  \( Mn^{2+} \)  ion has six nearest neighbor (NN)  \( Mn^{2+} \)  ions. The structure of an isolated  \( Mn_{2}I_{10} \)  cluster (i.e. a spin dimer), namely, an isolated Mn-Mn pair plus its 10 first-coordinate I atoms, is shown in the upper-right inset of Fig. 1(a). Each NN Mn-Mn pair contributes to the total electric polarization. To characterize the ferroelectric polarization arising from one pair of NN  \( Mn^{2+} \)  ions in  \( MnI_{2} \) , we isolate a Mn-Mn pair in a  \( 5 \times 5 \times 1 \)  supercell of  \( MnI_{2} \)  and replace all other  \( Mn^{2+} \)  ions with nonmagnetic  \( Mg^{2+} \)   ions, as depicted in Fig. 1(a). (A more accurate method for calculating the coefficients of the inter-site term requires no substitution of  \( Mn^{2+} \)  ions with nonmagnetic ions such as  \( Mg^{2+} \)  ions [20], and will be referred to as the no-substitution method.) When the SOC effect is excluded in the density functional calculations, the electric polarizations become zero so that the SOC effect is essential for the occurrence of ferroelectricity in helical spin-spiral systems.

The expansion coefficients  \( \mathbf{P}_{i}^{\alpha\beta} \)  (i = 1, 2) and  \( P_{12}^{\alpha\beta} \)  for a given spin dimer can be readily determined by mapping analysis once its polarizations are calculated for a set of carefully-chosen noncollinear spin arrangements. To evaluate an off-diagonal coefficient of the intra-site polarization, for example,  \( P_{1}^{xy} \) , we calculate the electric polarizations for the four spin arrangements  \( I' - IV' \)  of the spin dimer specified in Table I. Then, according to Eq. 2,  \( P_{1}^{xy} \)  is related to the polarization of the spin arrangements  \( I' - IV' \)  as  \( \mathbf{P}_{1}^{xy} = (\mathbf{P}_{I'} + \mathbf{P}_{II'} - \mathbf{P}_{III'} - \mathbf{P}_{\mathrm{IV'}})/4 \) .
 

Other off-diagonal intra-site coefficients,  \( P_{1}^{xz} \)  and  \( P_{1}^{\gamma z} \) , can be evaluated in a similar manner. The diagonal coefficients of the intra-site polarization can be determined by calculating the electric polarizations for the six spin arrangements I – VI of the spin dimer specified in Table II. According to Eq. 2, the polarizations of these spin arrangements have the relationships,  \( P_{1} + P_{II} = 2(\mathbf{P}_{1}^{\mathrm{xx}} - \mathbf{P}_{1}^{\gamma \gamma}) \) ,  \( P_{III} + P_{IV} = 2(\mathbf{P}_{1}^{\mathrm{xx}} - \mathbf{P}_{1}^{\gamma z}) \) , and  \( P_{V} + P_{VI} = 2(\mathbf{P}_{1}^{\gamma \gamma} - \mathbf{P}_{1}^{\mathrm{zz}}) \) . Two of these three equations are linearly independent, but only the two independent parameters ( \( P_{1}^{xx} - P_{1}^{\gamma \gamma} \) ) and ( \( P_{1}^{xx} - P_{1}^{\gamma z} \) ) are needed in calculating the sum of the diagonal contributions of the two intra-site polarizations because of the relationship  \( P_{1}^{\alpha \beta} = -\mathbf{P}_{2}^{\alpha \beta} \)  [20]. The electric polarizations of the above six spin arrangements can also be used to extract the coefficients of the inter-site polarization  \( P_{12} \) , that is,  \( \mathbf{P}_{12}^{\gamma \gamma} = (\mathbf{P}_{I} - \mathbf{P}_{II})/2 \) ,  \( \mathbf{P}_{12}^{\mathrm{xz}} = (\mathbf{P}_{III} - \mathbf{P}_{IV})/2 \) ,  \( \mathbf{P}_{12}^{\gamma z} = (\mathbf{P}_{V} - \mathbf{P}_{VI})/2 \) .

Our calculations for the spin dimer of  \( MnI_{2} \)  and mapping analyses as outlined above show that the coefficients of the intra-site polarization are  \( \mathbf{P}_{1}^{\mathrm{xx}}=(0,0,0) \) ,  \( \mathbf{P}_{1}^{\mathrm{yy}}=(2.5,0,0) \) ,  \( \mathbf{P}_{1}^{\mathrm{zz}}=(-2.5,0,0) \) ,  \( \mathbf{P}_{1}^{\mathrm{xy}}=(5.0,7.5,0) \) ,  \( \mathbf{P}_{1}^{\mathrm{xz}}=(0,-5.0,0) \) , and  \( \mathbf{P}_{1}^{\mathrm{yz}}=(7.5,-2.5,0) \)  in units of  \( 10^{-6} \)  eÅ. Note that the expression of the intra-site polarization differs from that of the bond polarization model (see above). The coefficients of the inter-site polarization extracted by using the no-substitution method [20] are

 \[ \mathbf{M}=\begin{bmatrix}\mathbf{M}_{11}&0&0\\ 0&\mathbf{M}_{22}&\mathbf{M}_{23}\\ 0&\mathbf{M_{32}}&\mathbf{M_{33}}\end{bmatrix}, \quad (5) \] 

where, in units of  \( 10^{-5} \)  eÅ,  \( M_{11} = -4.8 \) ,  \( M_{22} = 39.5 \) ,  \( M_{\mathrm{23}} = 49.0 \) ,  \( M_{32} = -44.5 \) , and  \( M_{33} = -26.0 \) . Thus, the inter-site polarization is at least an order-of-magnitude stronger than the intra-site polarization, and differs from the KNB model (see above) because the matrix elements  \( M_{11} = \)
 

Q, 0),  \( \mathbf{P}_{0}^{\mathrm{tot}} = \left( \frac{1}{2} \mathbf{B}, \frac{\sqrt{3}}{2} \mathbf{B} \right) \) , 0) with  \( \mathbf{B} = (\mathbf{M}_{11} + 3 \mathbf{M}_{22} - 4 \mathbf{M}_{11} \cos 2\pi \mathbf{Q}) \sin 2\pi \mathbf{\Omega} \) . Thus, the gKNB model predicts that  \( P \perp q \)  when  \( \mathbf{q} = (\mathbf{Q}, 0, 0) \) , but  \( P \parallel q \)  in the case of  \( \mathbf{q} = (\mathbf{Q}, \mathbf{Q}, 0) \) , as found experimentally [16], and that the polarization reverses with the change in the spin chirality (q to -q), in accord with experiment. The gKNB model shows that the polarization in both cases depends only on two elements of the matrix M, i.e.,  \( M_{11} \)  and  \( M_{22} \) , both of which are zero in the KNB model. In Fig. 2(b), we plot the magnitude of the polarization as a function of Q for the cases of  \( \mathbf{q} = (\mathbf{Q}, 0, 0) \)  and  \( \mathbf{q} = (\mathbf{Q}, \mathbf{Q}, 0) \) . The plot is symmetric with maximum at Q = 0.25 in the case of  \( \mathbf{q} = (\mathbf{Q}, 0, 0) \) , but is slightly asymmetric with maximum at Q = 0.225 in the case of  \( \mathbf{q} = (\mathbf{Q}, 0) \) .

We determine the total ferroelectric polarization of  \( MnI_{2} \)  in the helical spin-spiral state with  \( \mathbf{q} = (0.181, 0, 0.439) \) , observed in the absence of applied magnetic field, directly from density functional calculations by approximating the incommensurate state with the commensurate helical spin-spiral state with  \( \mathbf{q} = (1/3, 0, 0) \)  using a  \( 3 \times 1 \times 1 \)  supercell. Our calculations show that the electric polarization of this state is  \( 58.8 \mu C/m^{2} \)  along the [100] direction, as shown in Fig. 2(a). Thus, our density functional calculations show that  \( P \perp q \) , in agreement with experiment [16]. For the helical spin-spiral state of  \( MnI_{2} \)  with  \( \mathbf{q} = (Q, Q, 0) \) , found under in-plane magnetic field greater than 3 T [16], we use a  \( \sqrt{3} \times \sqrt{3} \)  supercell to simulate the  \( \mathbf{q} = (1/3, 1/3, 0) \)  state. The total polarization of this state is calculated to be  \( 71.4 \mu C/m^{2} \)  along the [110] direction. In this case,  \( P \parallel q \) , again in agreement with experiment [16]. As can be seen from Figs. 2(c) and (d), the gKNB model not only predicts the correct direction of the polarization, but also gives a rather accurate magnitude of the polarization for the cases of  \( \mathbf{q} = (Q, 0, 0) \)  and  \( \mathbf{q} = (Q, Q, 0) \) . Our theory of ferroelectric polarization is general and is expected
 

to provide accurate predictions when applied to other multiferroics driven by spin-spiral magnetic order.

In the local coordinate system (X, Y, Z) chosen to minimize the magnitudes of the diagonal elements of the matrix M [see the lower-right inset of Fig. 1(a), the Y axis is close to the distance vector between the two I atoms forming the shared octahedral edge between the adjacent Mn atoms], the matrix M of Eq. 5 determined from density functional calculations is rewritten as

 \[ \mathbf{M}=\begin{bmatrix}-4.8&0&0\\ 0&6.8&79.6\\ 0&-13.9&6.8\end{bmatrix}. \quad (6) \] 

in units of  \( 10^{-5} \)  eÅ. In the local (X, Y, Z) coordinate system,  \( (\mathbf{P}_{12}^{\mathrm{XY}})_{Y} = 79.6 \times 10^{-5} \)  eÅ is much greater than  \( -(\mathbf{P}_{12}^{\mathrm{ZX}})_{Z} = 13.9 \times 10^{-5} \)  eÅ. The cause for this anisotropy was examined by performing tight-binding calculations for a planar  \( M_{2}L_{2} \)  cluster consisting of two transition metal atoms M bridged by two ligand atoms L [20] on the basis of the model Hamiltonian similar to that employed by Jia et al. [18]. This analysis shows [20] that the large difference between  \( (\mathbf{P}_{12}^{\mathrm{XY}})_{Y} \)  and  \( -(\mathbf{P}_{12}^{\mathrm{ZX}})_{Z} \)  arises from the structural anisotropy of the planar  \( M_{2}L_{2} \)  cluster; the Y axis is nearly in the plane of, but the Z axis is nearly perpendicular to, the plane of the cluster.

In summary, on the basis of symmetry arguments, we developed a general theory of ferroelectric polarization that can correctly describe all known ferroelectric polarization induced by spin-spiral order.

Work at Fudan was partially supported by NSFC, Pujiang plan, and Program for Professor of Special Appointment (Eastern Scholar).
 

* Electronic address: hxiang@fudan.edu.cn

† Electronic address: mike_whangbo@ncsu.edu

‡ Electronic address: xggong@fudan.edu.cn

## References

[1] S.-W. Cheong and M. Mostovoy, Nat. Mater. 6, 13 (2007); R. Ramesh and N. Spaldin, Nat.

Mater. 6, 21 (2007); S. Picozzi and C. Ederer, J. Phys.: Condens. Matter 21, 303201 (2009).

[2] K. Wang, J.-M. Liu, and Z. Ren, Adv. Phys. 58, 321 (2009).

[3] M. Bibes, J.E. Villegas, and A. Barthélémy, Adv. Phys. 60, 5 (2011).

[4] T. Kimura, Annu. Rev. Mater. Res. 37, 387 (2007).

[5] Y. Tokura and S. Seki, Adv. Mater. 22, 1554 (2010).

[6] T. Kimura et al., Nature (London) 426, 55 (2003).

[7] A. Malashevich and D. Vanderbilt, Phys. Rev. Lett. 101, 037210 (2008).

[8] H. J. Xiang et al., Phys. Rev. Lett. 101, 037209 (2008).

[9] K. Taniguchi et al., Phys. Rev. Lett. 97, 097203 (2006).

[10] C. Tian et al., Phys. Rev. B 80, 104426 (2009).

[11] I. A. Sergienko and E. Dagotto, Phys. Rev. B 73, 094434 (2006).

[12] H. Katsura, N. Nagaosa, and A. V. Balatsky, Phys. Rev. Lett. 95, 057205 (2005).

[13] T. Kimura, J. C. Lashley, and A. P. Ramirez, Phys. Rev. B 73, 220401(R) (2006).

[14] S. Seki et al., Phys. Rev. B 75, 100403(R) (2007).

[15] S. Seki, Y. Onose, and Y. Tokura, Phys. Rev. Lett. 101, 067204 (2008).
 

[16] T. Kurumaji et al., Phys. Rev. Lett. 106}, 167206 (2011).

[17] T. Arima, J. Phys. Soc. Jpn. 76, 073702 (2007).

[18] C. Jia et al., Phys. Rev. B 74, 224444 (2006).

[19] T. Nakajima et al., Phys. Rev. B 77, 052401 (2008).

[20] See the Supporting Materials.
 

Table I. The four spin arrangements I' – IV' of the spin dimer employed to calculate its off-diagonal intra-site electric polarization  \( P_{1}^{xy} \)  by LDA+U+SOC calculations.

<table><tr><td></td><td>S1</td><td>S2</td></tr><tr><td>I&#x27;</td><td>\( (\frac{\sqrt{2}}{2}, \frac{\sqrt{2}}{\sqrt{2}}, 0) \)</td><td>(1, 0, 0)</td></tr><tr><td>II&#x27;</td><td>\( (\frac{\sqrt{2}}{2}, \frac{\sqrt{2}}{\sqrt{2}}, 0) \)</td><td>(-1, 0, 0)</td></tr><tr><td>III&#x27;</td><td>\( (\frac{\sqrt{2}}{2}, -\frac{\sqrt{2}}{\sqrt{2}}, 0) \)</td><td>(1, 0, 0)</td></tr><tr><td>IV&#x27;</td><td>\( (\frac{\sqrt{2}}{2}, -\frac{\sqrt{2}}{\sqrt{2}}, 0) \)</td><td>(-1, 0, 0)</td></tr></table>

Table II. The six spin arrangements I – VI of the spin dimer employed to calculate its diagonal intra-site electric polarization  \( P_{1}^{\alpha\alpha} \)  ( \( \alpha = x, y, z \) ) as well as the inter-site polarization  \( P_{12}^{xy} \) ,  \( P_{12}^{\times z} \)  and  \( P_{12}^{yz} \)  by LDA+U+SOC calculations.

<table><tr><td></td><td>S1</td><td>S2</td></tr><tr><td>I</td><td>(1, 0, 0)</td><td>(0, 1, 0)</td></tr><tr><td>II</td><td>(1, 0, 0)</td><td>(0, -1, 0)</td></tr><tr><td>III</td><td>(1, 0, 0)</td><td>(0, 0, 1)</td></tr><tr><td>IV</td><td>(1, 0, 0)</td><td>(0, 0, -1)</td></tr><tr><td>V</td><td>(0, 1, 0)</td><td>(0,  0, 1)</td></tr><tr><td>VI</td><td>(0, 1, 0)</td><td>(0,  0, -1)</td></tr></table>
 

## Figure captions

Figure 1. (Color online) (a) The  \( 5 \times 5 \times 1 \)  supercell of  \( MnI_{2} \)  in which all  \( Mn^{2+} \)  ions except for an isolated NN Mn-Mn pair are replaced by nonmagnetic  \( Mg^{2+} \)  ions. The left inset illustrates the layered structure of  \( MnI_{2} \) . The upper-right inset shows the top view of the  \( Mn_{2}I_{10} \)  dimer cluster. The lower-right inset shows the local coordinate systems (x, y, z) and (X, Y, Z) employed for calculations. (b) The electric polarizations predicted by the KNB and gKNB models for three different spin configurations of the Mn-Mn dimer, where the directions of the spins and the polarizations are described in terms of the (x, y, z) coordinate system shown in Fig. 1(a). The blue dots representing  \( S_{2} \)  means that it is pointed along the positive z-axis, and so does the green dot representing the polarization in the KNB model. The Cartesian components of the polarizations obtained from the gKNB model are given in units of  \( 10^{-5} \)  eÅ. (c) The polarization of the Mn-Mn pair with spins in the xy-plane as a function of the angle  \( \alpha \)  between the spins  \( S_{1} \)  and  \( S_{2} \) . The data points were obtained from direct density functional calculations, and the solid curves from the model of Eq. 1.

Figure 2. (Color online) (a) The triangular lattice of  \( Mn^{2+} \)  ions, where the in-plane lattice vectors  \( a_{1} \)  and  \( a_{2} \)  and the corresponding reciprocal lattice vectors  \( b_{1} \)  and  \( b_{2} \)  are shown. (b) The magnitude of the polarization predicted from our gKNB model as a function of Q for the cases of  \( \mathbf{q} = (\mathbf{Q}, 0, 0) \)  and  \( \mathbf{q} = (\mathbf{Q}, \mathbf{Q}, 0) \) . (c, d) The spin orientations of two proper-screw spirals with  \( \mathbf{q} = (1/3, 0, 0) \)  and  \( \mathbf{q} = (1/3, 1/3, 0) \) . The modulation vector q and the polarization vector P are represented by the white and green arrows, respectively. The numbers (in  \( \muC/m^{2} \) ) denote the magnitudes of the polarizations obtained from the direct density functional calculation and the gKNB model.
 
![](./images/867750085121802788_1.jpg)

![](./images/867750085121802788_2.jpg)

![](./images/867750085121802788_3.jpg)

Figure 1.
 

(a)

![](./images/867750085121802788_4.jpg)

(b)

![](./images/867750085121802788_5.jpg)

(c)

![](./images/867750085121802788_6.jpg)

(d)

![](./images/867750085121802788_7.jpg)

Figure 2
 

Supplementary Materials for

General Theory for the Ferroelectric Polarization Induced by Spin-Spiral Order

H. J. Xiang, E. J. Kan, Y. M. Zhang, M.-H. Whangbo, and X. G. Gong
 

## 1. Relationship between the coefficients of the electric polarization model

The ferroelectric polarization P of a spin dimer is written as

 \[ \mathbf{P}=\mathbf{P}_{1}(\mathbf{S}_{1})+\mathbf{P}_{2}(\mathbf{S}_{2})+\mathbf{P}_{12}(\mathbf{S}_{1},\mathbf{S}_{2}), \quad (1) \] 

where the intra-site polarization  \( \mathbf{P}_{\mathrm{i}}(\mathbf{S}_{\mathrm{i}}) \)  (i = 1, 2) and the inter-site polarization  \( \mathbf{P}_{12}(\mathbf{S}_{1}, \mathbf{S}_{2}) \)  are given by

 \[ \begin{aligned}&\mathbf{P}_{\mathrm{i}}(\mathbf{S}_{\mathrm{i}})=\sum_{\alpha\beta}\mathbf{P}_{\mathrm{i}}^{\alpha\beta}\mathbf{S}_{\mathrm{i}\alpha}\mathbf{S}_{\mathrm{j}\beta},\\&\mathbf{P}_{12}(\mathbf{S}_{1},\mathbf{S}_{2})=\sum_{\alpha\beta}\mathbf{P}_{12}^{\alpha\beta}\mathbf{S}_{\mathrm{i}\alpha}\mathbf{S}_{\mathrm{j}\beta},\\ \end{aligned} \quad (2) \] 

where the expansion coefficients,  \( P_{i}^{\alpha\beta} \)  and  \( P_{12}^{\alpha\beta} \) , are vectors. The above expressions show that

 \[ \mathbf{P}_{\mathrm{i}}^{\alpha\beta}=\mathbf{P}_{\mathrm{i}}^{{\beta}\alpha}, \] 

 \[ \begin{aligned}&\mathbf{P}_{\mathrm{i}}(\mathbf{S}_{\mathrm{i}})=\mathbf{P}_{\mathrm{i}}(-\mathbf{S}_{\mathrm{i}}\mathbf{),}\\ &\\ &\mathbf{P}_{12}(-\mathbf{S}_{1},\mathbf{S}_{2})=\mathbf{P}_{12}(\mathbf{S}_{1},-\mathbf{S}_{2})=-\mathbf{P}_{12}(\mathbf{S}_{1},\mathbf{S}_{2}).\\ \end{aligned} \quad (3) \] 

To prove that show that  \( P_{1}^{\alpha\beta} = -P_{2}^{\alpha\beta} \) , we consider the two spin arrangements of the spin dimer.

 \[  Arrangement I:\qquad\mathbf{S}_{1}=\mathbf{S}_{2}=\mathbf{S}=(\mathbf{S}_{\mathrm{x}},\mathbf{S}_{\mathrm{y}},\mathbf{S}_{\mathrm{z}}) \] 

 \[  Arrangement II:\qquad\mathbf{S}_{1}=-\mathbf{S}_{2}=\mathbf{S}=(\mathbf{S}_{\mathrm{x}},\mathbf{S}_{\mathrm{y}},\mathbf{S}_{\mathrm{z}}) \] 

The electric polarizations of both arrangements are zero because of the spatial inversion symmetry and time-reversal symmetry. These two configurations have opposite contribution to the inter-site polarization  \( P_{12} \) . Therefore, the sum  \( P_{sum} \)  of the electric polarizations of these two spin arrangements only contains the intra-site polarizations.

 \[ \mathbf{P}_{\mathrm{s u m}}=2\mathbf{P}_{1}(\mathbf{S})+2\mathbf{P}_{2}(\mathbf{S})=2\sum_{\alpha\beta}(\mathbf{P}_{1}^{\alpha\beta}+\mathbf{P}_{2}^{\alpha\beta})\mathbf{S}_{\alpha}\mathbf{S}_{\beta}. \quad (4) \] 

Since both spin arrangements have zero electric polarization,  \( P_{sum} \)  should be zero. Because the spin direction S is arbitrary, we obtain

 \[ \mathbf{P}_{1}^{\alpha\beta}=-\mathbf{P}_{2}^{\alpha\beta}. \quad (5) \]
 

To prove that  \( P_{12}^{\alpha\beta} = -P_{12}^{\beta\alpha} \) , we consider two spin arrangements.

Arrangement I:  \( S_{1} = S \)  and  \( S_{2} = S' \) 

Arrangement II:  \( S_{1} = S' \)  and  \( S_{2} = S \) .

It is noted that arrangement II is obtained by performing the spatial inversion operation on arrangement I. Thus, arrangement II has an electric polarization opposite to that of arrangement I. The inter-site polarization of arrangement II should be also opposite to that of arrangement I, namely,

 \[ \sum_{\alpha\beta}\mathbf{P}_{12}^{\alpha\beta}\mathbf{S}_{\alpha}\mathbf{S}_{\beta}^{\prime}=-\sum_{\alpha\beta}\mathbf{P}_{12}^{\alpha\beta}\mathbf{S}_{\alpha}^{\prime}\mathbf{S}_{\beta}. \quad (6) \] 

The above equation shows that  \( P_{12}^{\alpha\beta} = -P_{12}^{\beta\alpha} \) , and hence  \( P_{12}^{\alpha\alpha} = 0 \) .
 

## 2. Details of the density functional calculations

Total energy calculations are based on the DFT plus the on-site repulsion (U) method [1] within the local density approximation (LDA+U) on the basis of the projector augmented wave method [2] encoded in the Vienna ab initio simulation package [3]. The plane-wave cutoff energy is set to 400 eV. Spin-orbit coupling (SOC) is included in the calculations unless noted otherwise. We mainly discuss the results obtained with the on-site repulsion U = 5 eV and the exchange parameter J = 1 eV on Mn. We also did LDA+SOC calculations to find that the main results are qualitatively similar. For the calculation of electric polarization, the Berry phase method [4] was used.

## References

1. A. I. Liechtenstein et al., Phys. Rev. B 52, R5467 (1995).

2. P. E. Blöchl, Phys. Rev. B 50, 17953 (1994); G. Kresse and D. Joubert, Phys. Rev. B 59, 1758 (1999).

3. G. Kresse and J. Furthmüller, Comput. Mater. Sci. 6, 15 (1996); Phys. Rev. B 54, 11169 (1996).

4. R. D. King-Smith and D. Vanderbilt, Phys. Rev. B 47, 1651 (1993); R. Resta, Rev. Mod. Phys. 66, 899 (1994).
 

## 3. Sum of the diagonal contributions of the two intra-site polarizations

The sum  \( \Sigma \)  of the diagonal contributions of the two intra-site polarizations is expressed as

 \[ \mathbf{\Sigma}=\mathbf{P}_{1}^{\mathrm{xx}}\mathbf{S}_{1\mathrm{x}}\mathbf{S}_{1\mathbf{x}}+\mathbf{P}_{1}^{\mathrm{yy}}\mathbf{S}_{1\mathrm{y}}\mathbf{S}_{1\mathbf{y}}+\mathbf{P}_{1}^{\mathrm{zz}}\mathbf{S}_{1\mathrm{z}}\mathbf{S}_{1\mathbf{z}}+\mathbf{P}_{2}^{\mathrm{xx}}\mathbf{S}_{2\mathrm{x}}\mathbf{S}_{2\mathbf{x}}+\mathbf{P}_{2}^{\mathrm{yy}}\mathbf{S}_{2\mathrm{y}}\mathbf{S}_{2\mathbf{y}}+\mathbf{P}_{2}^{\mathrm{zz}}\mathbf{S}_{2\mathbf{z}}\mathbf{S}_{2\mathrm{z}} \quad (1) \] 

Because of the relationship

 \[ \mathbf{P}_{1}^{\alpha\beta}=-\mathbf{P}_{2}^{\alpha\beta}, \quad (2) \] 

Eq. 1 can be rewritten as

 \[ \mathbf{\Sigma}=(\mathbf{P}_{1}^{\mathrm{xx}}-\mathbf{P}_{1}^{\mathbf{zz}})\mathbf{S}_{1\mathrm{x}}\mathbf{S}_{1\mathrm{y}}+(\mathbf{P}_{1}^{\mathrm{yy}}-\mathbf{P}_{1}^{\mathbf{zz}})\mathbf{S}_{1\mathrm{y}}\mathbf{S}_{1\mathrm{x}}-(\mathbf{P}_{1}^{\mathrm{xx}}-\mathbf{P}_{1}^{\mathbf{zz}})\mathbf{S}_{2\mathrm{x}}\mathbf{S}_{2\mathrm{y}}-(\mathbf{P}_{1}^{\mathrm{yy}}-\mathbf{P}_{1}^{\mathbf{zz}})\mathbf{S}_{2\mathrm{y}}\mathbf{S}_{2\mathrm{z}}. \quad (3) \] 

Consequently, only the two independent parameters  \( (\mathbf{P}_{1}^{\mathrm{xx}} - \mathbf{P}_{1}^{\gamma\gamma}) \)  and  \( (\mathbf{P}_{1}^{\mathrm{xx}} - \mathbf{P}_{1}^{\gamma z}) \)  are needed in calculating the sum  \( \Sigma \) .
 

## 4. Calculations of the electric polarizations of a spin dimer

## 4.1. Using the substitution method

As described in the text, this substitution method uses a  \( 5 \times 5 \times 1 \)  supercell of  \( MnI_{2} \)  to define a spin dimer, namely, the 23 of the  \( 25 Mn^{2+} \)  ions in the supercell (except for the adjacent two defining a spin dimer) are replaced with nonmagnetic  \( Mg^{2+} \)  ions.

The electric polarizations (in unit of eÅ) calculated for the spin arrangements  \( I' - IV' \)  of the spin dimer (see Table I) were calculated to extract the off-diagonal term  \( \mathbf{P}_{I}^{\mathrm{xy}} = (\mathbf{P}_{I'} + \mathbf{P}_{II'} - \mathbf{P}_{III'} - \mathbf{P}_{\mathrm{IV'}}) / 4 \) :

I': (0.00001000, -0.00031000, 0.00019000)

II': (0.00001000, 0.00033000, -0.00019000)

III': (0.00000000, 0.00032000, -0.00019000)

IV': (0.00000000, -0.00033000, 0.00019000)

Similarly, the electric polarizations were calculated for the four spin arrangements shown below to extract off-diagonal term  \( \mathbf{P}_{I}^{\mathrm{xx}} = (\mathbf{P}_{I'} + \mathbf{P}_{II'} - \mathbf{P}_{III'} - \mathbf{P}_{\mathrm{IV'}}) / 4 \) :

<table><tr><td></td><td>S1</td><td>S2</td></tr><tr><td>I&#x27;</td><td>\( (\frac{\sqrt{2}}{2}, 0, \frac{\sqrt{2}} {2}) \)</td><td>(1, 0, 0)</td></tr><tr><td>II&#x27;</td><td>\( (\frac{\sqrt{2}}{2}, 0, \frac{\sqrt{2}} {2}) \)</td><td>(-1, 0, 0)</td></tr><tr><td>III&#x27;</td><td>\( (\frac{\sqrt{2}}{2}, 0, -\frac{\sqrt{2}} {2}) \)</td><td>(1, 0, 0)</td></tr><tr><td>IV&#x27;</td><td>\( (\frac{\sqrt{2}}{2}, 0, -\frac{\sqrt{2}} {2}) \)</td><td>(-1, 0, 0)</td></tr></table>
 

I': (0.00000000, 0.00025000, -0.00034000)

II': (0.00000000, -0.00026000, 0.00034000)

III': (0.00000000, -0.00025000, 0.00034000)

IV': (0.00000000, 0.00026000, -0.00034000)

The electric polarizations were calculated for the four spin arrangements shown below to extract off-diagonal term  \( \mathbf{P}_{1}^{\mathrm{vz}} = (\mathbf{P}_{\mathrm{I}^{\prime}} + \mathbf{P}_{\mathrm{II}^{\prime}} - \mathbf{P}_{\mathrm{I}\mathrm{II}^{\prime}}^{\mathrm{v}} - \mathbf{P}_{\mathrm{I}\mathrm{V}^{\prime}})/4 \) :

<table><tr><td></td><td>S1</td><td>S2</td></tr><tr><td>I&#x27;</td><td>(0,√2/2,√2/2)</td><td>(1, 0, 0)</td></tr><tr><td>II&#x27;</td><td>(0,√2/2,√2/2)</td><td>(-1, 0, 0)</td></tr><tr><td>III&#x27;</td><td>(0,√2/2, -√2/2)</td><td>(1, 0, 0)</td></tr><tr><td>IV&#x27;</td><td>(0,√2/2, -√2/2)</td><td>(-1, 0, 0)</td></tr></table>

I': (0.00001000, -0.00007000, -0.0015000)

II': (0.00001000, 0.00007000, 0.0015000)

III': (0.00000000, -0.00057000, 0.00051000)

IV': (-0.00001000, 0.00058000, -0.00051000)

The electric polarizations were calculated for the six spin arrangements I – VI (see Table II) to extract the diagonal intra-site terms  \( P_{1}^{xx} \) ,  \( P_{1}^{\gamma\gamma} \)  and  \( P_{1}^{zz} \)  as well as the inter-site terms  \( P_{12}^{xy} \) ,  \( P_{12}^{\mathrm{xz}} \)  and  \( P_{12}^{yz} \) :
 

I: (0, 0.00045, -0.00027)

II: (0, -0.00045, 0.00026)

III: (0, -0.00036, 0.00047)

IV: (0, 0.00036, -0.00047)

V: (-0.00004, 0, 0)

VI: (0.00005, 0, 0)

In units of eÅ, the above results give rise to  \( M_{11} = -0.000045 \) ,  \( M_{22} = 0.00036 \) ,  \( M_{\Sigma3} = 0.0045 \) ,  \( M_{32} = -0.00047 \)  and  \( M_{33} = -0.00265 \) .

## 4.2. Using the no-substitution method

The substitution method has an undesirable effect in that it distorts the electron distribution around the spin dimer, because the valence atomic orbitals of Mn differ from those of Mg. To evaluate the inter-site polarizations more accurately, therefore, we employ the “magnetic” spin-dimer method, which is similar to the technique that we recently proposed to extract the spin exchange parameters (see: H. J. Xiang, E. J. Kan, S.-H. Wei, M.-H. Whangbo and X. G. Gong, arXiv:1106.5549).

To obtain the inter-site polarization  \( P_{12}^{xy} \) , for example, we use a  \( 5 \times 5 \times 1 \)  supercell of  \( MnI_{2} \)  with  \( 25~Mn^{2+} \)  ions. The first two  \( Mn^{2+} \)   \( I_{2} \)  ions (1 and 2) will be regarded as the spin dimer for which the inter-site polarizations are to be extracted. We calculate the electric polarizations of the following four spin arrangements A – D of the supercell:
 

<table><tr><td></td><td>S1</td><td>S2</td><td>23 other spins</td></tr><tr><td>A</td><td>(1, 0, 0)</td><td>(0, 1, 0)</td><td>\( (0, 0, 1) \)</td></tr><tr><td>B</td><td>(1, 0, 0)</td><td>(0, -1, 0)</td><td>\( (0, 0, 1) \)</td></tr><tr><td>C</td><td>(-1, 0, 0)</td><td>(0, 1, 0)</td><td>\( (0, 0, 1) \)</td></tr><tr><td>D</td><td>(-1, 0, 0)</td><td>(0, -1, 0)</td><td>\( (0, 0, 1) \)</td></tr></table>

By using Eq. 2 of the text, it can be easily shown that  \( \mathbf{P}_{12}^{\mathrm{xy}} = (\mathbf{P}_{\mathrm{A}} + \mathbf{P}_{\mathrm{D}} - \mathbf{P}_{\mathrm{B}} - \mathbf{P}_{C})/4 \) . The inter-site polarizations for all other Mn-Mn pairs cancel out, and so do all intra-site polarizations. The calculated polarizations for the four spin arrangements are:

 \[ \mathbf{P}_{\mathrm{A}}=(-0.000040,\ 0.000880,\ -0.000720) \] 

 \[ \mathbf{P}_{\mathrm{B}}=(0.000040,\ -0.000100,\ -0.000200) \] 

 \[ \mathbf{P}_{\mathrm{C}}=(-0.000040,\ -0.000880,\quad0.000720) \] 

 \[ \mathbf{P}_{\mathrm{D}}=(0.000040,\ 0.000100,\ 0.000200) \] 

so that, in units of  \( 10^{-5} \)  eÅ, we obtain  \( \mathbf{P}_{12}^{\mathrm{xy}} = (\mathbf{P}_{\mathrm{A}} + \mathbf{P}_{\mathrm{D}} - \mathbf{P}_{\mathrm{B}} - \mathbf{P}_{C})/4 = (0, 49.0, -26.0) \) .

To extract  \( P_{12}^{yz} \) , the polarizations were calculated for the four spin arrangements:

<table><tr><td></td><td>S1</td><td>S2</td><td>23 other spins</td></tr><tr><td>A</td><td>(0, 1, 0)</td><td>(0,0, 1)</td><td>(0.0, 1)</td></tr><tr><td>B</td><td>(0, 1, 0)</td><td>(0,0, -1)</td><td>(0.0, 1)</td></tr><tr><td>C</td><td>(0, -1, 0)</td><td>(0, 0, 1)</td><td>(0.0, 1)</td></tr><tr><td>D</td><td>(0, -1, 0)</td><td>(0, 0, -1)</td><td>(0.0, 1)</td></tr></table>

 \[ \mathbf{P}_{\mathrm{A}}=(0,0,0) \] 

 \[ \mathbf{P}_{\mathrm{B}}=(0.000070,\ 0.000000,\ 0.00000) \] 

 \[ \mathbf{P}_{\mathrm{C}}=(0,0,0) \] 

 \[ \mathbf{P}_{\mathrm{D}}=(-0.000120,\ 0.000000,\ 0.00000) \] 

In units of  \( 10^{-5} \)  eÅ, these values lead to  \( P_{12}^{yz} = (-4.8, 0, 0) \) .
 

To extract  \( P_{12}^{xz} \) , the polarizations were calculated for the four spin arrangements:

<table><tr><td></td><td>S1</td><td>S2</td><td>23 other spins</td></tr><tr><td>A</td><td>(1, 0, 0)</td><td>(0, 0, 1)</td><td>(0. 0, 1. 1)</td></tr><tr><td>B</td><td>(1, 0, 0)</td><td>(0, 0, -1)</td><td>(0. 0, 1. 1)</td></tr><tr><td>C</td><td>(-1, 0, 0)</td><td>(0, 0, 1)</td><td>(0. 0, 1. 1)</td></tr><tr><td>D</td><td>(-1, 0, 0)</td><td>(0, 0, -1)</td><td>(0. 0, 1. 1)</td></tr></table>

 \[ \mathbf{P}_{\mathrm{A}}=(0,0,0) \] 

 \[ \mathbf{P}_{\mathrm{B}}=(-0.000010,\ 0.000790,\ -0.000890) \] 

 \[ \mathbf{P}_{\mathrm{C}}=(0,0,0) \] 

 \[ \mathbf{P}_{\mathrm{D}}=(-0.000020,\ -0.000790,\ 0.000890). \] 

In units of  \( 10^{-5} \)  eÅ, we get  \( \mathbf{P}_{12}^{\mathrm{xz}} = (\mathbf{P}_{\mathrm{A}} + \mathbf{P}_{\mathrm{D}} - \mathbf{P}_{\mathrm{B}} - \mathbf{P}_{C})/4 = (-0.3, -39.5, 44.5) \) . Note that  \( P_{12}^{xz} = -P_{12}^{xz} \) . Therefore, in units of  \( 10^{-5} \)  eÅ,  \( M_{11} = -4.8 \) ,  \( M_{22} = 39.5 \) ,  \( M_23 = 49.0 \) ,  \( M_{32} = -44.5 \) , and  \( M_{33} = -26.0 \) .
 

## 5. Details of the tight-binding calculations

In our tight-binding (TB) model, we consider two transition metal atoms ( \( M_{l} \)  and  \( M_{r} \) ) bridged by two ligand anions ( \( L_{u} \)  and  \( L_{d} \) ), as shown in Fig. S1(a). Our model is similar to that proposed by Jia et al. \( ^{1} \)  except that they considered a linear M-L-M three-atom model. The overall Hamiltonian describing the four-atom cluster is given by

 \[ \mathrm{H}=\mathrm{H}_{\mathrm{M}}+\mathrm{H}_{\mathrm{L}}+\mathrm{H}_{\mathrm{t}}+\mathrm{H}_{\mathrm{so}}, \quad (S1) \] 

where

 \[ \mathrm{H}_{\mathrm{M}}=\sum_{\mathrm{a}}^{\mathrm{l,r}}\sum_{\sigma}\left(\sum_{\alpha\in\mathrm{t}_{\mathrm{2g}}}\mathrm{E}_{\mathrm{t}_{\mathrm{2}g}}\mathrm{d}_{\alpha\alpha\sigma}^{+}\mathrm{d}_{\alpha\alpha\tau}+\sum_{\alpha\in\mathrm{e}_{\mathrm{g}}}\mathrm{E}_{\mathrm{e}_{\mathrm{g}}}\mathbf{d}_{\alpha\alpha\sigma}^{+}\mathbf{d}_{\alpha\alpha\tau}\right)\;+\;\mathrm{H}_{\mathrm{U}} \quad (S2) \] 

 \[ \mathrm{H}_{\mathrm{L}}=\mathrm{E}_{\mathrm{p}}\sum_{\mathrm{b}}^{\mathrm{u},\mathrm{d}}\sum_{\beta\sigma}\mathrm{p}_{\mathrm{b}\beta\sigma}^{+}\mathrm{p}_{\mathrm{bb}\sigma} \quad (S3) \] 

 \[ \mathrm{H}_{\mathrm{t}}=\sum_{\mathrm{a}}^{\mathrm{l,r}}\sum_{\mathrm{b}}^{\mathrm{u},\mathrm{d}}\sum_{\alpha\beta\sigma}(\mathrm{t}_{\mathrm{a}\mathrm{o}\beta\mathrm{b}\sigma}\mathrm{p}_{\mathrm{b}\beta\sigma}^{+}\mathrm{d}_{\alpha\alpha\tau}+\mathrm{h.c.}) \quad (S4) \] 

 \[ \mathrm{H}_{\mathrm{so}}=\lambda_{\mathrm{M}}\sum_{\mathrm{a}}^{\mathrm{l,r}}\left(\mathbf{S}_{\mathrm{a}}\cdot\mathbf{L}_{\mathrm{a}}\right) \quad (S5) \] 

In addition to the crystal field splitting, the transition-metal d levels are split by the crystal field into  \( t_{2g} \)  and  \( e_{g} \)  orbitals with the energy difference  \( \Delta_{cf} \)  between the energy levels  \( E_{t_{2g}} \)  and  \( E_{e_{g}} \) . The Hamiltonian  \( H_{M} \)  for the transition metal also contains an effective Zeeman field, which originates from the local Coulomb repulsion and Hund's-rule coupling in the magnetically ordered phase:

 \[ \mathrm{H}_{\mathrm{U}}=-\mathrm{U}\sum_{\mathrm{a}=\mathrm{l},\mathrm{r}}\sum_{\sigma}\mathbf{m}_{\mathrm{a}}\cdot\mathbf{s}_{\mathrm{a}\alpha} \quad (S6) \] 

In the hopping term  \( H_{t} \) , the hybridization matrix t depends on the d and p orbitals involved (corresponding to  \( \sigma \)  and  \( \pi \)  bonding of the orbitals) and also on their relative positions (left or right transition-metal M and up or down ligand L).  \( H_{so} \)  describes the spin-orbit interaction within the magnetic d orbitals. The energy scheme is illustrated in Fig. S1(b). Unless otherwise stated,
 

we will use the following reasonable parameters:  \( E_{t_{2g}} = 0 \) ,  \( E_{e_{g}} = 2 \)  eV,  \( E_{p} = -5 \)  eV, U = 10 eV,  \( t_{pd\sigma} = -1.6 \)  eV,  \( t_{pd\pi} = 0.6 \)  eV, and  \( \lambda_{M} = 0.048 \)  eV.

We diagonalize the total Hamiltonian and then calculate the dipole moment using the occupied states. Our calculations show that, in terms of the local coordinate system  \( (X', Y', Z') \)  defined in Fig. S1(a), the matrix M of the inter-site polarization is written as

 \[ \mathbf{M}=\begin{bmatrix}{{{0}}}&{{{0}}}&{{{0}}}\cr{{{0}}}&{{{O}}}&{{{\left(\mathbf{P}_{12}^{\mathbf{X}^{\prime}\mathbf{Y}^{\prime}}\right)_{\mathbf{Y}^{\prime}}}}}\cr{{{0}}}&{{{\left(\mathbf{P}_{12}^{\mathbf{Z}^{\mathbf{X}^{\prime}}}\right)_{\mathbf{Z}^{\prime}}}}}&{{{0}}}\end{bmatrix}, \quad (S7a) \] 

which is a consequence of the  \( D_{2h} \)  symmetry of the four-atom cluster model. Our calculations show that  \( (\mathbf{P}_{12}^{\mathbf{X}^{\prime}\mathbf{Y}^{\prime}})_{\mathbf{Y}^{\prime}} \)  is always much larger than  \( -(\mathbf{P}_{12}^{\mathbf{Z}^{\prime}\mathbf{X}^{\prime}})_{\mathbf{Z}^{\prime}} \)  and is independent of the model parameters, in contrast to the case of the KNB model in which  \( (\mathbf{P}_{12}^{\mathbf{X}^{\prime}\mathbf{Y}^{\prime}})_{\mathbf{Y}^{\prime}} = -(\mathbf{P}_{12}^{\mathbf{Z}^{\prime}\mathbf{X}^{\prime}})_{\mathbf{Z}^{\prime}} \) . To gain further insight into this finding, we examine how the d-states of  \( M_{l} \)  and  \( M_{r} \)  interact with the p-states of  \( L_{u} \)  and  \( L_{d} \)  [see Fig. S1(b)] in the absence and presence of SOC. It is found that the nonzero  \( (\mathbf{P}_{12}^{\mathbf{X}^{\prime}\mathbf{Y}^{\prime}})_{\mathbf{Y}^{\prime}} \)  arises from the SOC-induced orbital mixing between the minority-spin  \( d_{z2} \)  orbital of  \( M_{l} \)  and the  \( p_{x} \)  of  \( L_{u} \)  [Fig. S1(c)], and the nonzero  \( (\mathbf{P}_{12}^{\mathbf{Z}^{\prime}\mathbf{X}^{\prime}})_{\mathbf{Z}^{\prime}} \)  from that between the minority-spin  \( d_{x2-y2} \)  of  \( M_{l} \)  and the  \( p_{x} \)  of  \( L_{u} \) . The extent of the orbital mixing can be described by the density matrix D with matrix elements  \( D_{mn} \)  defined by  \( D_{mn}=\sum_{i}^{\mathrm{occ}}\sum_{m,n}C_{im}^{*}C_{in} \) , where  \( C_{im} \)  is the coefficient of the local atomic basis m in the i-th occupied state. We consider two cases in which the spins rotate in different planes. For the case when the two spins are in the  \( X^{\prime}Y^{\prime} \) -plane ( \( X^{\prime}Z^{\prime} \) - plane), the density matrix element between the  \( d_{z2} \)  orbital of  \( M_{l} \)  and the  \( p_{x} \)  of  \( L_{u} \)  (between the  \( d_{x2-y2} \)  of  \( M_{l} \)  and the  \( p_{x} \)  of  \( L_{u} \) ) is plotted as a function of the angle between the two spins in Fig. S1(d). As can be seen, both density matrix elements exhibit a sinusoidal dependence, and
 

the density matrix element is much larger for the  \( X^{\prime}Y^{\prime} \) -plane than for the  \( X^{\prime}Z^{\prime} \) -plane case. The large difference between  \( (\mathbf{P}_{12}^{\mathrm{X}^{\prime}\mathrm{Y}^{\prime}})_{\mathrm{Y}^{\prime}} \)  and  \( -(\mathbf{P}_{12}^{\mathrm{Z}^{\prime}\mathrm{X}^{\prime}})_{\mathrm{Z}^{\prime}} \)  reflects the structural anisotropy associated with the planar four-atom cluster; the two metal ions are bridged by two ligands with the  \( Y^{\prime} \)  axis in the plane of the cluster, whereas the  \( Z^{\prime} \)  axis is out of the plane.

The form of the matrix M obtained from density functional calculations can now be understood. In the local coordinate system (X, Y, Z) defined in the lower-right inset of Fig. 1(a), which results from the anticlockwise rotation of the local coordinate system (x, y, z) around the x axis by  \( 137^{\circ} \) , the matrix M of Eq. 5 determined from density functional calculations is rewritten as

 \[ \mathbf{M}=\begin{bmatrix}-4.8&0&0\\ 0&6.8&79.6\\ 0&-13.9&6.8\end{bmatrix}. \quad (S7b) \] 

in units of  \( 10^{-5} \)  eÅ. The Y axis is close to the distance vector between two edge-shared I atoms. In the local (X, Y, Z) coordinate system,  \( (\mathbf{P}_{12}^{\mathrm{XY}})_{\mathrm{Y}} = 79.6 \times 10^{-5} \)  eÅ is much larger than  \( -(\mathbf{P}_{12}^{\mathrm{ZX}})_{\mathrm{Z}} = 13.9 \times 10^{-5} \)  eÅ. In tight-binding calculations using the (X', Y', Z') coordinate system,  \( (\mathbf{P}_{12}^{\mathrm{XY'}})_{\mathrm{Y'}} \)  is much larger than  \( -(\mathbf{P}_{12}^{\mathrm{Z'X'}})_{\mathrm{Z'}} \) , as discussed above. The (X, Y, Z) coordinate system is close to the (X', Y', Z') coordinate system. This explains why  \( (\mathbf{P}_{12}^{\mathrm{XY}})_{\mathrm{Y}} \)  is much larger than  \( -(\mathbf{P}_{12}^{\mathrm{ZX}})_{\mathrm{Z}} \)  from our density functional calculations.

Due to the  \( D_{2h} \)  symmetry of the four-atom cluster  \( Mn_{2}I_{2} \) , the nonzero elements of the matrix M are that  \( (\mathbf{P}_{12}^{\mathrm{X}^{\prime}\mathrm{Y}^{\prime}})_{\mathrm{Y}^{\prime}} \)  and  \( (\mathbf{P}_{12}^{\mathrm{Z}^{\prime}\mathrm{X}^{\prime}})_{\mathrm{Z}^{\prime}} \) . In Fig. S2, we show the dependence of the polarizations on the various tight-binding parameters. In examining the dependence of one parameter, all the other parameters are fixed. We find that both  \( (\mathbf{P}_{12}^{\mathrm{X}^{\prime}\mathrm{Y}^{\prime}})_{\mathrm{Y}^{\prime}} \)  and  \( -(\mathbf{P}_{12}^{\mathrm{Z}^{\prime}\mathrm{X}^{\prime}})_{\mathrm{Z}^{\prime}} \)  increase
 

monotonously with the SOC strength  \( \lambda_{M} \) , the hopping parameter t, 1/U, and the crystal field splitting  \( \Delta_{cf} \) . In particular, the polarizations increase almost linearly with  \( \lambda_{M} \) . These results can be easily understood because the increase in these parameters enhances the mixing between the unoccupied orbitals and occupied orbitals. An interesting finding from Fig. S1 is that  \( (\mathbf{P}_{12}^{\mathrm{X}^{\mathrm{Y}}^{\prime}})_{\mathrm{Y}^{\prime}} \)  is always much larger than  \( -(\mathbf{P}_{12}^{\mathrm{Z}^{\mathrm{X}}^{\prime}})_{\mathrm{Z}^{\prime}} \) . This is different from the KNB model in which  \( (\mathbf{P}_{12}^{\mathrm{X}^{\mathrm{Y}}^{\prime}})_{\mathrm{Y}^{\prime}} = -(\mathbf{P}_{12}^{\mathrm{Z}^{\mathrm{X}}^{\prime}})_{\mathrm{Z}^{\prime}} \) .

## Reference

1. C. Jia et al., Phys. Rev. B 74, 224444 (2006); C. Jia et al., Phys. Rev. B 76, 144424 (2007).
 
![](./images/867750085121802788_8.jpg)

Figure S1. (Color online) (a) The  \( M_{2}L_{2} \)  four-atom cluster model used for tight-binding analysis. The spin directions and the two coordinate systems used are indicated. (b) A schematic representation of the up-spin and down-spin d-states of  \( M_{l} \)  and  \( M_{r} \)  lying above the p-states of  \( L_{u} \)  and  \( L_{d} \) . (c) The interaction between the d-states of the metal  \( M_{l} \)  with the p-states of the ligand  \( L_{u} \)  in the absence of SOC (the upper panel labeled as NSOC) and in the presence of SOC (the lower panel labeled as SOC). The green double-headed arrows indicate the allowed interactions between  \( M_{l} \)  and  \( L_{u} \) , and the blue double-headed arrows indicate the allowed interactions among the d-states in the presence of SOC. (d) The density matrix between the  \( d_{z2} \)  orbital of  \( M_{l} \)  and the  \( p_{x} \)  of  \( L_{u} \)  for the case when these two spins are in the  \( X^{\prime}Y^{\prime} \) -plane, and that between the  \( d_{x^{2}-y^{2}} \)  orbital of  \( M_{l} \)  and the  \( p_{z} \)  of  \( L_{u} \)  for the case when these two spins are in the  \( X^{\prime}Z^{\prime} \) -plane, as a function of the angle between the two spins. The left spin is fixed to be along the X-direction.
 
![](./images/867750085121802788_9.jpg)

![](./images/867750085121802788_10.jpg)

![](./images/867750085121802788_11.jpg)

![](./images/867750085121802788_12.jpg)

Figure S2. The dependence of the polarization  \( \left(\mathbf{P}_{12}^{\mathrm{X}^{\mathrm{Y}}^{\mathrm{Y}}}\right)_{\mathrm{Y}} \)  and  \( \left(\mathbf{P}_{12}^{\mathrm{Z}^{\mathrm{X}}}\right)_{\mathrm{Z}} \)  on (a) the SOC strength  \( \lambda_{M} \) , (b) the scaled hopping parameter  \( t/t_{0} \) , (c) the inverse of Hubbard U, and (d) the crystal field  \( \Delta_{cf} \) .
 

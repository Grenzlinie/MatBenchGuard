# Molecular-Dynamics Study of the Structural Dependence of the Young Modulus of Au Nanowires

S. Kameoka and K. Shintani

Dept of ME & Intelligent Sys, Univ of Electro-Comm,
1-5-1 Chofugaoka, Chofu, Tokyo 182-8585, Japan
E-mail: shintani@mce.uec.ac.jp, URL: http://www.shintani.mce.uec.ac.jp/

## ABSTRACT

The deformation of Au nanowires of helical multi-shell (HMS) structures and the fcc structure under a tensile external force is addressed by molecular-dynamics simulation. The modified embedded-atom method (MEAM) potential is employed for calculating the interaction between Au atoms. At first, a model nanowire is equilibrated at a specified temperature. Next, the external force in the axial direction is imposed on the Au atoms at the ends of the nanowire. We conclude that the Young modulus of a Au nanowire depends on its atomic structure.

## INTRODUCTION

The investigation of nanomaterials such as carbon nanotubes, fullerenes, semiconductor nanowires, and metallic nanowires is essential to the development of nanotechnology. They are suitable for use as nanoscale building blocks in opto-electronic devices and micro/nano-electromechanical systems (MEMS/NEMS). For example, carbon nanotubes can be used as probe tips of scanning probe microscopes, nanomanipulators, and nanotweezers. On the other hand, Au nanowires are useful for biological applications because Au atoms can immobilize organic compound molecules having specific radicals. They are also useful for chemical applications because Au atoms can become catalysts for growth of semiconductor nanowire superlattices [1]. In order to realize these applications, it will be important to investigate the mechanical and electronic properties of such nanomaterials at nanoscale.

Au nanowires have drawn much attention of researchers since a single-atom chain of gold atoms at a nanocontact between a scanning tunneling microscopic probe and a metal surface was observed [2]. They have some unique properties at nanoscale such as quantized conductance and long bond-length that are not observed for materials at macroscopic scale. It is probable that the mechanical behaviors of nanowires under external forces are different from those of the macroscopic materials. Suspended Au nanowires were fabricated in an ultra-high-vacuum (UHV) transmission electron microscope (TEM) with the electron beam thinning technique. It was revealed by high-resolution TEM that these nanowires have helical multi-shell (HMS) structures [3]. Carbon nanotubes have such helical structures, and they are metallic or semiconducting depending on the chirality. Similarly, metallic nanowires are expected to have also interesting physical properties due to their chirality.

In this study, the molecular-dynamics (MD) simulations of elongation of Au nanowires are performed to investigate how the Young modulus of a Au nanowire depends on its atomic structure. Four model nanowires having HMS structures and the fcc structure are created for this purpose. We adopt the classical MD method with the modified embedded-atom method potential [5] considering its computing facility and reliability. The MEAM potential takes account of the effect of the bond angle on the interaction between atoms.

![](./images/811668921793904640_1.jpg)

Figure 1. An unrolled triangular-lattice sheet.

## MODEL NANOWIRES AND SIMULATION METHOD

The helical single-shell [4] and multi-shell structures of Au nanowires are identified from their TEM images. A helical shell of a nanowire can imaginatively be constructed by rolling a triangular-lattice sheet that is a {111} plane of the fcc structure. Figure 1 is a schematic illustration of an unrolled triangular-lattice sheet. The helical shell is uniquely specified by the chiral vector $C_{\mathrm{h}}$ which is expressed by the basic translational vectors $\boldsymbol{a}$ and $\boldsymbol{b}$ in the triangular lattice as $C_{\mathrm{h}}=n \boldsymbol{a}+m \boldsymbol{b}$, where $n$ and $m$ are intergers and called chiral indices, and the chiral vector $C_{\mathrm{h}}$ is expressed by $(n, m)$. The diameter $d$ of the nanowire and chiral angle $\theta$ can be expressed in terms of the chiral indices and the lattice constant of Au. For example, an outer shell which consists of seven helical atom rows can be constructed by rolling the sheet so that the crystallographically equivalent two points $O$ and $A$ in figure 1 coincide. In constructing a solid nanowire, there will be a mismatch between the inner and outer shells.

The constructed initial structures of the model nanowires are shown in figure 2. The parameters of these models are shown in table I. We consider the shortest interatomic distance of Au atoms as the diameter of Au atom. The chiral vector of the outer shell of Model-1 and Model-2 is (7,3). The nanowire of this chiral vector was identified by Kondo and Takayanagi [3]. These nanowires have a single atom row at its center axis of the outer shell. The interatomic distance of a single-atom row at the center axis of Model-1 is 2.88Å. On the other hand, the interatomic distance of a single-atom row at the center axis of Model-2 is 3.03Å. These models were created to investigate the effect of the atomic commensurateness on the Young modulus of nanowires. Model-3 and Model-4 have the fcc structure; the center axes of these nanowires are along the [110] direction. The sides of Model-3 are the {111} planes, whereas the sides of Model-4 are the {110} planes. If the cross-sectional area of a nanowire whose sides are the {110} planes is smaller than that of Model-4, its initial shape cannot be maintained after equilibration. Therefore, the cross-sectional area of Model-4 was set to be much larger than that of Model-3.

The velocity-Verlet algorithm is empolyed to integrate the equations of motion. The MD time step is 2.0 fs. The temperatures of Model-1, 2, and 3 are maintained at intervals of 25K from 25K to 200K. The temperature of Model-4 is maintained at 100K. To find their cross-sectional area

<table>
<caption>Table I. Initial parameters of model nanowires</caption>
<thead>
<tr>
<th></th>
<th>Structure</th>
<th>Number of atoms</th>
<th>Cross-sectional area (Å²)</th>
<th>Length (Å)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Model-1</td>
<td>HMS</td>
<td>168</td>
<td>56.16</td>
<td>62.75</td>
</tr>
<tr>
<td>Model-2</td>
<td>HMS</td>
<td>167</td>
<td>56.16</td>
<td>62.75</td>
</tr>
<tr>
<td>Model-3</td>
<td>fcc</td>
<td>194</td>
<td>58.83</td>
<td>63.46</td>
</tr>
<tr>
<td>Model-4</td>
<td>fcc</td>
<td>1104</td>
<td>320.14</td>
<td>67.61</td>
</tr>
</tbody>
</table>

![](./images/811668921793904640_2.jpg)

Figure 2. Structures of model nanowires. (a), (b), (c), and (d) are the top, side, and cross-sectional views of Model-1, 2, 3, and 4, respectively.

Table II. Comparison between the parameters of Model-1 and Model-3.

<table>
  <thead>
    <tr>
      <th></th>
      <th>Number of atoms</th>
      <th>Length of the circumference of the cross-section (Å)</th>
      <th>Cross-sectional area (Å²)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Model-1</td>
      <td>168</td>
      <td>26.57</td>
      <td>56.16</td>
    </tr>
    <tr>
      <td>Model-3</td>
      <td>194</td>
      <td>29.00</td>
      <td>58.83</td>
    </tr>
    <tr>
      <td>Ratio</td>
      <td>1.15</td>
      <td>1.09</td>
      <td>1.05</td>
    </tr>
  </tbody>
</table>

and length in the equilibrium configurations, we adopt the two-stages equilibration. The first equilibration is performed during $2×10^5$ MD steps for the nanowires of Model-1, 2, and 3. In this first equilibration, the movement of the single-atom row at the center axis is restricted to the axis direction, and the distortion of the helical structure is removed. The second equilibration is performed during $10^5$ MD steps for all the models. In this second equilibration, the movement of the atoms at both the ends of a nanowire is restricted to the axis direction. Next, the simulation proceeds to elongation phase. The model nanowire is elongated in the direction of the nanowire axis by the external force which is applied to the chosen atoms at both the ends of the nanowire and increased by 0.005 nN in every $2.5×10^4$ MD steps for Model-1, 2, and 3 and by 0.002 nN in every $10^4$ MD steps for Model-4 until the nanowire breaks.

# RESULTS AND DISCUSSION

Each simulation for a model nanowire yields a stress-strain curve. From the inclination of the curve in the range of the small strain, we can obtain the Young modulus of the nanowire.
The Young moduli of the four model nanowires at the eight temperatures are shown in figure 3 and in table III. The largest difference between the Young moduli of Model-1 and Model-2 is 10.6 percent. This difference is due to the difference of the degrees of consistency of the atomic arrangement. From table II, the ratio of the length of the circumference of the cross-section to the cross-sectional area for Model-1 or Model-2 is not much different from that for Model-3.
Nevertheless, the Young moduli of Model-1 and Model-2 are larger than Model-3, and the rate at which the Young moduli of Model-1 and Model-2 decrease with increasing temperature is larger than the rate at which the Young modulus of Model-3 does. The Young modulus of a nanowire will be smaller with decreasing the sectional area because the atomic bonds at surfaces are weaker than those in bulk. However, the Young modulus of Model-3 is larger than that of

![](./images/811668921793904640_3.jpg)

Figure 3. Young's modulus of Au nanowires

### Table III. Comparison between the Young moduli of Model-1 and Model-2

<table>
  <tr>
    <th>Temperature (K)</th>
    <td>25</td>
    <td>50</td>
    <td>75</td>
    <td>100</td>
    <td>125</td>
    <td>150</td>
    <td>175</td>
    <td>200</td>
  </tr>
  <tr>
    <th>Young's modulus of Model-1 (Gpa)</th>
    <td>119</td>
    <td>112</td>
    <td>110</td>
    <td>101</td>
    <td>94</td>
    <td>85</td>
    <td>84</td>
    <td>79</td>
  </tr>
  <tr>
    <th>Young's modulus of Model-2 (Gpa)</th>
    <td>115</td>
    <td>109</td>
    <td>109</td>
    <td>99</td>
    <td>85</td>
    <td>86</td>
    <td>78</td>
    <td>77</td>
  </tr>
  <tr>
    <th>Ratio</th>
    <td>1.036</td>
    <td>1.025</td>
    <td>1.007</td>
    <td>1.023</td>
    <td>1.106</td>
    <td>0.985</td>
    <td>1.088</td>
    <td>1.027</td>
  </tr>
</table>

![](./images/811668921793904640_4.jpg)

Figure 4. Deformation of a nanowire of HMS structure. (a)-(c) are the snapshots of Model-1 at 25K, and (d)-(f) those at 75K. The interval between the snapshots is 500MD steps.

![](./images/811668921793904640_5.jpg)

Figure 5. Deformation of a nanowire with the fcc structure. (a)-(c) are the snapshots of deformation of Model-3 at 25K, and (d)-(f) are those at 50K. The interval between the snapshots is 500MD steps.

Model-4. Furthermore, the Young moduli of Model-1 and Model-2 are larger than that of Model-4. It is because the atomic arrangement of the {111} planes at the sides of Model-3 is denser than that of the {110} planes at the sides of Model-4.

The snapshots of the deformation of Model-1 are shown in figure 4. A constricted part which appears in the snapshot (a) moves upwards. A slip in the direction of a translational vector in the triangular lattice has occurred. The snapshots of the deformation of Model-3 with the fcc structure is also shown in figure 5 where a slip in the <111> direction in the fcc structure has occurred.

## CONCLUSIONS

The elongation of Au helical nanowires was simulated by the MD method. The Young modulus of Au nanowires of the HMS structure is considerably large in the light of the fact that its cross-sectional area is small. In the case of 7-1 helical Au nanowires, the commensurateness of the atoms affects their Young modulus.

## REFERENCES

1. M. S. Gudiksen, L. J. Lauhon, J. Wang, D. C. Smith, and C. M. Lieber, Nature **395**, 783 (2002)
2. H. Ohnishi, Y. Kondo, and K. Takayanagi, Nature **395**, 780 (1998).
3. Y. Kondo and K. Takayanagi, Science **289**, 606 (2000).
4. Y. Oshima and A. Onga, Phys. Rev. Lett. **91**, 205503 (2003).
5. M. I. Baskes, Phys. Rev. B **46**, 2727(1992).
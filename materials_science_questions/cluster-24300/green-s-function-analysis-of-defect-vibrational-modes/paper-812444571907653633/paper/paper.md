# DYNAMIQUE DE RESEAU ET FREQUENCES DES MODES DE VIBRATION POUR DES IMPURETES SUBSTITUTIONNELLES DANS InP, GaP ET ZnS

MICHEL VANDEVYVER et PIERRE PLUMELLE

Laboratoire d'Etudes et de Recherches Avancées, Service d'electronique pour la recherche fondamentale, Services d'electronique de Saclay, Centre d'etudes nucleaires de Saclay, Boite Postale No. 2; 91190 Gif-sur-yvette, France

(Received 13 October 1976; accepted 18 November 1976)

Résumé-Un modèle d'ions rigides à 11 paramètres comprenant les interactions générales entre premiers voisins, seconds voisins et les forces de Coulomb, est utilisé pour expliquer à la fois les résultats expérimentaux de diffusion de neutrons et les résultats d'absorption IR dans InP. Un modèle mathématique qui utilise la technique des fonctions de Green est ensuite employé pour prévoir les fréquences de vibration des impuretés substitutionnelles pour ce matériau dans l'approximation du défaut de masse et du défaut de constante de force entre premiers voisins. La fréquence des modes localisés, de gap et de bande est calculée pour diverses impuretés substitutionnelles en fonction du défaut de constante de force pris comme paramètre. Le même calcul est donné pour deux autres composés ayant également la structure de la blende et un grand gap de phonons: GaP et ZnS. Une comparaison est donnée avec les résultats expérimentaux disponibles.

Abstract-The model used is a rigid-ion model with an effective ionic charge including general interactions for nearest and next nearest neighbours and long range Coulomb interactions. It provides a good fit with available neutron data and with IR absorption results for InP. In this model, no hypothesis is made a priori on the interatomic forces and the eleven parameters given by the model are used. A mathematical model which employs a Green's function technique in the mass defect and the nearest neighbour force constant defect approximation is used to calculate the lattice dynamics of the imperfect crystal. The frequencies of the local modes, the gap modes and the band modes, are given for isolated substitutional impurities. The same calculation is achieved for GaP and ZnS and the results are compared with IR data.

## I. INTRODUCTION

L'étude de la dynamique de réseaux cristallins contenant une faible concentration d'impuretés a suscité ces dernières années un très grand intérêt. De nombreuses études ont été consacrées à des réseaux perturbés par des défauts ponctuels et possèdant la structure de la blende, principalement ceux des composés III V et II VI. Pour de tels réseaux, les défauts les plus étudiés sont constitués par: (i) une substitution atomique isolée (symétrie de site Td)[1], (ii) deux évènements indépendants sur deux atomes premiers voisins (symétrie $C_{3 v}$ ) ou seconds voisins (symétrie Cs), un évenement pouvant être une substitution atomique ou une lacune[2-9]. Dans le présent article nous nous limiterons à l'étude de la substitution d'atomes isolés (Td) dans le cas d'un réseau ayant la structure de la blende.

De tels défauts introduisent dans le cristal des modes propres de vibration dont il est possible de déterminer expérimentalement la fréquence, le plus souvent par spectroscopie d'absorption infrarouge mais aussi par spectroscopie Raman[10]. Dans la plupart des données expérimentales, l'impureté étudiée est plus légère que les atomes du réseau et la fréquence du mode observé est supérieure à la fréquence maximum du spectre de phonons. Le mode est alors dit localisé parce que l'énergie des vibrations est spacialement localisée au voisinage du défaut. Le spectre d'absorption optique se présente alors sous forme d'une raie, d'observation relativement aisée. Si la fréquence du mode est située dans la bande des fréquences interdites du spectre de phonons, son énergie de vibration est encore spacialement localisée autour du défaut, mais le mode est alors dit mode de gap. Il n'existe en fait aucune distinction fondamentale entre mode localisé et mode de gap, et le spectre d'absorption optique se présente encore sous forme d'une raie. Un défaut ponctuel peut également être responsable d'un mode résonant dans le cas où sa fréquence propre est située dans la gamme des fréquences permises du spectre de phonons; le spectre d'absorption se présente alors sous forme d'une bande dont la largeur à mi-hauteur dépend de la densité d'états du spectre de phonons à cette énergie. L'immense majorité des observations est relative à des modes localisés, mais des modes de gap ont été observés[11,24,45], et probablement aussi des modes résonants[12-18].

Du point du vue conceptuel une substitution d'un atome isolé par un atome étranger se traduit en première approximation par une modification $\Delta m$ de la masse atomique (connue exactement) et par une modification des forces liant l'atome considéré avec les autres atomes du réseau. A partir de ces données, des calculs ont été effectués pour obtenir les énergies des modes de vibrations propres des défauts: un modèle moléculaire de défaut[19] a été développé et appliqué au cas des critaux ayant la structure de la blende[20,21]; toutefois, les résultats obtenus sont peu convaincants et la méthode actuellement la plus utilisée est celle des fonctions de Green [1, 18, 22-26].

Dans cette méthode la condition de l'existence de solutions pour les modes localisés de gap ou de résonance

766
M. VANDEVYVER et P. PLUMELLE

est que la partie réelle du déterminant séculaire s'annule:
$$\operatorname{Re}\{\operatorname{det}(I-g \cdot \delta 1)\}=0 \tag{1}$$

où $g$ est une matrice de fonctions de Green du réseau parfait pour laquelle on suppose que la pulsation de phonon $\omega$ a une partie infinitésimale imaginaire négative $(\omega \to \omega-i \epsilon ; \epsilon>0)$, et $\delta 1$ une matrice qui définit la perturbation due au défaut et qui inclut les modifications de masse $\Delta m$ et de forces $\Delta f$. La matrice $\delta 1$ caractérise "l'espace du défaut"; elle est de dimension $(3 n ×3 n)$ où $n$ est le nombre d'atomes dont la situation se trouve modifiée par suite de l'introduction du défaut[22]. La comparaison des solutions de l'équation (1) et des résultats expérimentaux permet, au moins en principe, d'obtenir des informations sur $\delta 1$ et donc sur les modifications des forces intératomiques.

Dans la plupart des cas, l'équation (1) ne donne qu'une seule solution utile qui est la fréquence du mode localisé. Ceci est très insuffisant pour déterminer les différentes modifications de forces possibles mais comme on s'attendà ce que la variation des forces entre l'atome concerné et ses premiers voisins soit beaucoup plus importante que celle des autres forces intératomiques, l'hypothèse généralement admise pour les calculs les plus élaborés est que seules les forces entre l'atome substitué et ses premiers voisins se touvent modifiées, de telle sorte que $\Delta f$ n'est déterminé que par deux paramètres[1]. En fait, une hypothèse additionnelle est admise pour réduire à un le nombre de ces paramètres[1,18] [présent travail], qui peut alors être déterminé sans ambiguïté. Il existependant une situation où l'équation (1) a deux solutions: un mode localisé et un mode de gap. Ceci peut arriver avec des matériaux pour lesquels la bande des fréquences interdites du spectre de phonons est large et pour lesquels l'atome le plus lourd de la cellule élémentaire est remplacé par un atome plus léger que lui. Une telle situation permet donc de mieux juger les hypothèses faites sur la modification des forces et souligne l'intérêt de l'étude des composés ayant un gap de phonons appréciable (ZnS, GaP, AlSb[24], InP). Dans le présent article, nous nous proposons de résoudre l'équation (1) en particulier dans le cas du phosphure d'indium et pour différentes sub- stitutions atomiques isolées.

La partie II est consacrée à l'établissement d'un jeu de constantes de forces capable de rendre compte de la dynamique du cristal non perturbé. La partie III est relative à la définition de la perturbation et à la résolution proprement dite de l'équation (1).

## PARTIE II
### II.a Choix du modèle de forces
Pour InP nous nous proposons d'utiliser les résultats expérimentaux de Borcherds et al.[39], obtenus recem- ment par diffusion de neutrons, pour déterminer les différents paramètres intervenant dans un modèle de forces capable de décrire les propriétés dynamiques du cristal parfait.

Si on se limite aux composés II VI et III V, un grandnombre de données neutroniques existent relativement à ceux des réseaux qui ont la structure de la blende et des modèles de forces intératomiques assez différents ont été utilisés pour rendre compte de ces résultats. Par exemple, des modèles du type "SHELL" comportant différents niveaux d'approximation ont été utilisés pour ZnTe et ZnS[27], CdTe[28], GaAs[29], GaP[30], InSb[31] et récemment pour GaSb[32]. D'autre part des modèles d'ions rigides (RIM) incluant les forces de Coulomb, les forces générales entre premiers voisins, seconds voisinsmais entre lesquelles ont été imposées des relations àpriori ont été testés: par exemple, un modèle à 4 paramètres pour ZnTe[33], et à sept paramètres pour CdTe et ZnTe[34] et, récemment pour un ensemble de cristaux III V et II VI[35]. De tels modèles n'ont pas suffisamment de paramètres ajustables pour rendre compte d'une façon précise des résultats neutroniques. Par contre, un modèle d'ions rigides incluant des forces de Coulomb et des interactions générales, jusques et y compris les seconds voisins, a été utilisé avec succès dans le cas de ZnS, ZnSe, GaP, GaAs, InSb[36], et CdTe, ZnTe[37]. Ce modèle dispose de 11 paramètres ajustables et est appelé RIM 11 dans le présent article ainsi que dans la Réf.[37].

Bien entendu, il existe des modèles de forces beaucoupplus sophistiqués qui tiennent compte de la polarisabilité des ions et disposent de très nombreux paramètres ajustables. Par exemple, le modèle d'approximation des liaisons déformables" (D.B.A.) à 15 paramètres développé par Kunc[36] rend bien compte des données neutroniques, en particulier pour ZnS, ZnSe, GaP, GaAs, InSb[36]. (Ce modèle est un cas particulier du modèle de Karo et Hardy[38].) Pour D.B.A., la procédure d'ajus- tement des paramètres est beaucoup plus compliquée que pour RIM 11 et il a été montré qu'en ce qui concerne les courbes de dispersion de phonons, au moins dans les directions de plus haute symétrie, les ajustements obtenus pouvaient être aussi satisfaisants avec RIM 11 qu'avec D.B.A. En conséquence, l'utilisation d'un modèle de forces très compliqué apparaît ici comme injustifié pour rendre compte des résultats de Borcherds sur InP, d'autant plus que ses résultats sont très incomplets pour les vecteurs d'onde de direction $\Sigma$ (absence des branchesΣ optiques). En conséquence, nous les analyserons en utilisant le modèle d'ion rigide RIM 11.

### II.b Calcul des paramètres
La procédure d'ajustement des 11 paramètres du modèle a été décrite avec beaucoup de détails dans la Réf.[37]; on procède par étapes successives en utilisant une méthode de moindres carrés, d'abord au centre de la zone de Brillouin, puis aux points X et L. A ce stade, il estpossible de rendre compte de 13 résultats expérimentaux: $C 11, C 12, C 44, \omega LO(\Gamma), \omega TO(\Gamma), \omega LA(X), \omega LO(X)$ , $\omega TA(X), \omega TO(X), \omega LO(L), \omega LA(L), \omega TA(L), \omega TO(L)$  en utilisant seulement 9 paramètres sur les 11 disponiblesà savoir $Z, A, B, C i, D i, F i(i=1,2)$ [voir Tableau 1] (les notations utilisées dans le présent article sont les mêmes que celles des Réf.[36,37]). Les 9 paramètres ainsi déterminés sont donnés dans le Tableau 2 (E1 et E2 ne sont pas encore déterminés). Il est alors possible de calculer les fréquences de phonons pour les branches $\Delta$ et A, lesquelles ne dépendent que de ces 9 paramètres et de les comparer aux données neutroniques de Borcherds et

Dynamique de reseau et frequences des modes de vibration

**Tableau 1.**
Phosphure d'indium
Résultats expérimentaux Résultats du calcul (d)

|          | Résultats expérimentaux | Résultats du calcul (d) |
|----------|-------------------------|-------------------------|
| $C11$    | $10.22$ (a)             | $10.45$                 |
| $C12$    | $5.760$ (a)             | $5.76$                  |
| $C44$    | $4.600$ (a)             | $4.611$                 |
| $\Gamma(LO)$ | $10.38$ (b)           | $10.36$                 |
| $\Gamma(TO)$ | $9.12$ (b)           | $9.130$                 |
| $X(TO)$  | $9.7\pm0.2$ (c)         | $10.17$                 |
| $X(LO)$  | $9.95\pm0.1$ (c)        | $9.59$                  |
| $X(LA)$  | $5.8\pm0.3$ (c)         | $5.500$                 |
| $X(TA)$  | $2.05\pm0.1$ (c)        | $2.058$                 |
| $L(TO)$  | $9.5\pm0.15$ (c)        | $9.513$                 |
| $L(LO)$  | $10.2\pm0.3$ (c)        | $10.45$                 |
| $L(TA)$  | $1.65\pm0.02$ (c)       | $1.648$                 |
| $L(LA)$  | $5.00\pm0.1$ (c)        | $5.049$                 |

Fréquences en $10^{12}\ Hz$; $C_{11}, C_{12}, C_{44}$ en $10^{11}\ dyn.cm^{-2}$.
(a) Réf.[36]; (b) Réf.[39] Raman; (c) Réf.[39]; (d) Calculé en utilisant RIM 11 et les valeurs du Tableau 2.

**Tableau 2.**
Phosphure d'indium

$$
\begin{align*}
a_{0} &= 2.9343 \\
M_{1} &= 30.93 \\
M_{2} &= 114.82 \\
Z &= 0.82 \\
A &= -0.365 \\
B &= -0.100 \\
C_{1} &= -0.017 \\
D_{1} &= -0.003 \\
E_{1} &= +0.05 \\
F_{1} &= -0.071 \\
C_{2} &= -0.043 \\
D_{2} &= -0.120 \\
E_{2} &= +0.110 \\
F_{2} &= +0.177
\end{align*}
$$

$a_{0}$ en Angströms; $M_{1}$,
$M_{2}$ en u.ma; $A, B,...$,
$F_{1}, F_{2}\ 10^{5}\ dyn.cm^{-1}$.

al. (Fig. 1). L'accord entre valeurs expérimentales et valeurs calculées est très satisfaisant pour les branches acoustiques $\Delta$ et $\Lambda$. En particulier au point $L$ la fréquence calculée pour $\omega LA(L)$, soit $5.049\times10^{12}\ Hz$, est très proche de la valeur expérimentale: $5.10^{12}\ Hz$ [voir Tableau 1] (Dans le cas de CdTe et surtout de ZnTe, le même modèle donnait pour $\omega LA(L)$ une valeur calculée nettement supérieure à la valeur expérimentale[37]). L'accord est encore très satisfaisant pour les branches optiques $\Lambda$; par contre, il existe un écart entre valeurs expérimentales et valeurs calculées supérieur à l'erreur expérimentale pour $\omega(TO(X)$ et $\omega LO(X)$.

Les deux paramètres restants $E1$ et $E2$ sont déterminés de la façon suivante: d'abord les branches 1 et 5 sont pratiquement indépendantes de $E1$ et de $E2$ et ne dépendent en fait que des 9 paramètres déjà connus; d'un autre côté les branches acoustiques $\Sigma 2$ et $\Sigma 3$ ne dépendent pratiquement que du paramètre $E2$ qui caractérise les intéractions entre seconds voisins les plus lourds; il est alors possible d'ajuster $E2$ en utilisant une méthode de moindres carrés sur tous les points expéri- mentaux des branches $\Sigma 2$ et $\Sigma 3$. On trouve alors un minimum prononcé pour $E2=+0.11\times10^{5}\ dyn.cm^{-1}$. Le onzième paramètre $E1$ est alors déterminé par les considérations suivantes: si l'on connaît tous les paramètres du modèle, il est possible de calculer les fonctions de distribution à deux phonons, additive et soustractive, données par la formule (2).

$$
g_{ \pm}(\omega)=\frac{2}{2 r(2 r-1) N} \sum_{i, j} \delta\left(\omega-\left|\omega_{i}(\vec{k}) \pm \omega_{j}(\vec{k})\right|\right) \quad (2)
$$

où $r$ est le nombre d'atomes par maille cristalline ($r=2$); $N$ le nombre de points de la zone de Brillouin adopté pour ce calcul ($N=27.791$); $\vec{k}$ et $\omega$ le vecteur d'onde et la pulsation des phonons; $i, j(=1$ à 6) le numéro de la branche de phonons considérée et $\delta$ le symbole de Kronecker. L'intérêt d'une telle procédure est que les énergies pour lesquelles $g+$ et $g-$ sont maximales sont les mêmes que celles pour lesquelles le coefficient d'absorption infrarouge $\alpha$ correspondant aux mécanismes à deux phonons (respectivement de sommation et de différence) est lui-même maximal.

![](./images/812444571907653633_1.jpg)

Fig. 1. Résultats expérimentaux et courbes de dispersion cal- culées pour InP. $\diamond, \bullet$, Borcherds et al.[39]. Les courbes en traits pleins sont calculées à partir des valeurs des paramètres données Tableau 2. ----, idem mais $E1=0.10\times10^{5}\ dyn.cm^{-1}$; ———, idem mais $E1=0\ dyn.cm^{-1}$.

D'autre part, l'intensité des bandes de différence tend vers 0 quand la température de l'échantillon tend elle-même vers 0, alors que celle des bandes de sommation décroît avec la température mais tend vers une limite non nulle pour $T=0$[40]. Il est donc possible, au moins théoriquement, en étudiant le spectre d'absorption IR, d'identifier les bandes à deux phonons de sommation et les bandes de différence. Cette remarque est utilisée pour déterminer le paramètre de force encore inconnu $E1$: les courbes du coefficient d'absorption IR du phosphure d'indium en fonction de l'énergie, obtenues à300,77 et $4^{\circ} K$ sont représentées Fig. 2. Les mesures ontété effectuées sur un échantillon semi-isolant d'épaisseur0.47 mm avec un spectrophotomètre Perkin-Elmer 180(voir aussi[46,47]). Le plus facile était de comparer lespectre obtenu à $4^{\circ} K$ avec la fonction de distribution à deux phonons additive $g+$ puisque, à cette température, seules subsistent dans le spectre à deux phonons lesbandes de sommation. Nous avons donc calculé $g+(\omega)$  pour les valeurs des 10 paramètres déjà connus et pour différentes valeurs de $E1$, et comparé les énergies des

![](./images/812444571907653633_2.jpg)

Fig. 2. InP-Coefficient d'absorption en fonction de l'énergie des photons. Traits pleins: mesuré à $300^{\circ} K$. --- et $-..., 77^{\circ} K ; \cdots-$ et $-... ; 4^{\circ} K$ . Aux énergies supérieures à $500 ~cm^{-1}$ les valeurs du coefficient d'absorption sont quasiment les mêmes à $77^{\circ}$ et à $4^{\circ} K$ .

maxima de $g+$ à celles des maxima de $\alpha(\omega)$ à $4^{\circ} K$ . La largeur d'échantillonnage adoptée était de $\omega LO(\Gamma) / 50$ , soit $6.93 ~cm^{-1}$ , pour $g+$ et de $\omega LO(\Gamma) / 100$ , soit $3.465 ~cm^{-1}$ ,pour $g-$ . Le calcul montre que l'histogramme $g+(\omega)$  dépend d'une façon très sensible de $E 1$ : pour $E 1=0$ (Fig.3), $g+$ ne présente qu'un seul maximum au delà de $600 ~cm^{-1}$ et dans la région de $400 ~cm^{-1}$ . Pour $E 1=$ +0.1x10 dyn. cm-' il n'est pas possible de rendre compte de la variation expérimentale de $\alpha$ dans la zone d'énergie comprise entre 500 et $600 ~cm^{-1}$ où l'échantillon présente une absorption très faible, zone dont l'étendue reflete la largeur du gap (voir Fig. 1). Le meilleur accord entre I'histogramme et les resultats experimentaux est obtenu pour $E 1=0.05 \times 10^{5} dyn. cm^{-1}$ (Fig. 5). L'his togramme $g-(\omega)$ calculé pour cette valeur de $E 1$ est représenté Fig. 6.

Les resultats experimentaux obtenus à differentes temperatures sont donnés Fig. 2. Le Tableau 3 donne lesénergies des differentes transitions dipolaires permises à deux phonons[44] obtenues à partir des résultats neu- troniques aux points caracteriques [39] et des valeurs desénergies en ces points calculées dans le present travail(Tableau 1). Pour les énergies comprises entre 600 et700 cm-' la multiplicité des combinaisons possibles rend malaisée une assignation précise des 3 pics principauxobservés à 631,659 et $688 ~cm^{-1}$ . Par ailleurs, le Tableau 4donne les énergies pour lesquelles d'une part $\alpha$ mesuré à $4^{\circ} K$ et d'autre part $g+$ calculé à partir du modèle et des valeurs des parametres données Tableau 2 sont maxima.On peut constater que l'énergie des maxima de $g+$  trouvée à $637,665,693 ~cm^{-1}$ est en accord satisfaisant avec les resultats experimentaux. Cette constatation vautégalement pour la zone d'énergie voisine de $400 ~cm^{-1}$ .

![](./images/812444571907653633_3.jpg)

Fig. 3. InP-Densité d'états à deux phonons $g+(\omega)$ calculée pourles valeurs des paramètres du Tableau 2 mais pour $E 1=$ 0.0 dyn.cm-1.

<table><caption>Tableau 3.</caption>
<thead>
<tr>
<th rowspan="2">Designation</th>
<th>Phosphure d'indium</th>
<th>Présent travail:</th>
</tr>
<tr>
<th>Calculé en utilisant les résultats neutroniques (39) (cm-1)</th>
<th>calculé en utilisant RIM 11 (voir Tableau 1) (cm-1)</th>
</tr>
</thead>
<tbody>
<tr>
<td>2TA(L)</td>
<td>110</td>
<td>109.8</td>
</tr>
<tr>
<td>2TA(X)</td>
<td>136.6</td>
<td>137</td>
</tr>
<tr>
<td>LA(L)+TA(L)</td>
<td>221.6</td>
<td>223</td>
</tr>
<tr>
<td>LA(X)+TA(X)</td>
<td>261.6</td>
<td>251.9</td>
</tr>
<tr>
<td>2LA(L)</td>
<td>333</td>
<td>337</td>
</tr>
<tr>
<td>2LA(X) Raman</td>
<td>386.6</td>
<td>366.6</td>
</tr>
<tr>
<td>TO(L)+TA(L)</td>
<td>371.6</td>
<td>372</td>
</tr>
<tr>
<td>LO(X)+TA(X)</td>
<td>401</td>
<td>388</td>
</tr>
<tr>
<td>LO(L)+TA(L)</td>
<td>395</td>
<td>403</td>
</tr>
<tr>
<td>TO(X)+TA(X)</td>
<td>392</td>
<td>407</td>
</tr>
<tr>
<td>TO(L)+LA(L)</td>
<td>483</td>
<td>485</td>
</tr>
<tr>
<td>LO(X)+LA(X)</td>
<td>526</td>
<td>503</td>
</tr>
<tr>
<td>LO(L)+LA(L)</td>
<td>507</td>
<td>516</td>
</tr>
<tr>
<td>TO(X)+LA(X)</td>
<td>517</td>
<td>522</td>
</tr>
<tr>
<td>2TO(L)</td>
<td>633</td>
<td>634</td>
</tr>
<tr>
<td>2LO(X) Raman</td>
<td>663</td>
<td>639</td>
</tr>
<tr>
<td>LO(L)+TO(L)</td>
<td>656</td>
<td>665</td>
</tr>
<tr>
<td>LO(X)+TO(X)</td>
<td>656</td>
<td>668</td>
</tr>
<tr>
<td>2TO(X)</td>
<td>646</td>
<td>678</td>
</tr>
<tr>
<td>2LO(L)</td>
<td>679</td>
<td>696</td>
</tr>
</tbody>
</table>

Tableau 4.

<table>
<thead>
<tr>
<th colspan="4">Phosphure d'indium</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3">Energie des maxima du coefficient d'absorption (cm⁻¹) (Fig. 2)</td>
<td>Energie des maxima de g+ et g- (cm⁻¹) calculées avec RIM 11</td>
</tr>
<tr>
<td>300°K</td>
<td>77°K</td>
<td>4°K</td>
<td>g + (Fig.5) g - (Fig.6)</td>
</tr>
<tr>
<td>995</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>965</td>
<td>970</td>
<td>970</td>
<td></td>
</tr>
<tr>
<td>935</td>
<td>940</td>
<td>940</td>
<td></td>
</tr>
<tr>
<td>835</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>805</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>775</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>745</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>718</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>692</td>
<td>693</td>
<td>690</td>
<td>a 693</td>
</tr>
<tr>
<td>682</td>
<td>688</td>
<td>688</td>
<td></td>
</tr>
<tr>
<td>663</td>
<td>667</td>
<td>668</td>
<td></td>
</tr>
<tr>
<td>652</td>
<td>658</td>
<td>659</td>
<td>b 665</td>
</tr>
<tr>
<td></td>
<td>647</td>
<td>647</td>
<td></td>
</tr>
<tr>
<td>626</td>
<td>631</td>
<td>631</td>
<td>c 637</td>
</tr>
<tr>
<td></td>
<td>613</td>
<td>615</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>610</td>
<td>α 609</td>
</tr>
<tr>
<td>587</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>558</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>535</td>
<td>535</td>
<td>535</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>525</td>
<td>β 547</td>
</tr>
<tr>
<td>502</td>
<td>507</td>
<td>508</td>
<td>d 519</td>
</tr>
<tr>
<td></td>
<td>490</td>
<td>490</td>
<td></td>
</tr>
<tr>
<td>470</td>
<td>475</td>
<td>475 2 bandes</td>
<td>e 478</td>
</tr>
<tr>
<td>445</td>
<td>449</td>
<td>450</td>
<td></td>
</tr>
<tr>
<td></td>
<td>420</td>
<td>420</td>
<td></td>
</tr>
<tr>
<td>415</td>
<td>407</td>
<td>407</td>
<td>f 415</td>
</tr>
<tr>
<td></td>
<td>397</td>
<td>397</td>
<td></td>
</tr>
<tr>
<td></td>
<td>384</td>
<td>385</td>
<td>g 388</td>
</tr>
<tr>
<td></td>
<td>373</td>
<td>370</td>
<td></td>
</tr>
<tr>
<td>Opague entre 400 et 220</td>
<td>Opaque entre 345 et 270</td>
<td>Opaque entre 345 et 290</td>
<td>$\begin{cases} 298 \\ 284 \\ 263 \\ 252 \end{cases}$</td>
</tr>
<tr>
<td></td>
<td>250 large bande</td>
<td>237 large bande</td>
<td>$h \begin{cases} 235 \\ \text{(2 bandes)} \\ 249 \end{cases}$ $\begin{cases} b \ 190 \\ c \ 159 \end{cases}$</td>
</tr>
<tr>
<td>190</td>
<td>192</td>
<td></td>
<td></td>
</tr>
<tr>
<td>164</td>
<td>165</td>
<td></td>
<td></td>
</tr>
<tr>
<td>135</td>
<td>136</td>
<td>137</td>
<td>i 138</td>
</tr>
<tr>
<td>80 large bande</td>
<td>85 large bande</td>
<td>90 large bande</td>
<td>j 130 $d \begin{cases} 97 \\ 110 \end{cases}$</td>
</tr>
<tr>
<td colspan="4">Les pics principaux sont soulignés.</td>
</tr>
</tbody>
</table>

Ainsi aux trois pics d'absorption intense observés à 385, $407, 475 \mathrm{cm}^{-1}$ correspondent des maxima prononcés de g+ calculés respectivement pour $388,415,478 \mathrm{cm}^{-1}$ mais une assignation des pics observés en utilisant le Tableau 3 apparaît ici encore comme hasardeuse. Une étude récente[51] montre qu'il est possible d'analyser pour InP le spectre d'absorption infrarouge entre $(370$ et $700 \mathrm{~cm}^{-1})$ uniquement en fonction des énergies aux points caractéristiques. Il nous paraît cependant préférable, chaque fois que cela est possible, d'analyser les données infrarouge en utilisant la totalité du spectre de phonons et pas seulement les énergies aux points caractéristiques. C'est ainsi que les 3 histogrammes $g+(\omega)$ des Figs. 3-5 correspondent aux mêmes valeurs des énergies aux points caractéristiques données sur le Tableau 1(d). Ceci permet de mieux apprécier la contribution de la totalité du spectre de phonons à l'absorption IR.

La situation est différente aux basses énergies $(E \leq$ $200 \mathrm{cm}^{-1}$ ) où les combinaisons possibles sont beaucoup moins nombreuses. Ainsi la bande observée à $137 \mathrm{~cm}^{-1}$ qui correspond à un maximum de g+ calculé à $138 \mathrm{~cm}^{-1}$ peut sans ambiguïté être attribuée à la combinaison 2 TA(X) (voir Tableau 3). Ce résultat est en accord avec les conclusions de Kirkman[41] et correspond bien aux résultats de Eaves $(16.7 \pm 0.3 \mathrm{meV})[42]$ et de Alfrey $(16.6 \pm 0.2 \mathrm{meV})[43]$. Cependant, en contraste avec les observations de Kirkman, aucune bande d'absorption

![](./images/812444571907653633_4.jpg)

Fig. 4. InP-Densité d'états à deux phonons $g+(\omega)$ calculée pour les valeurs des paramètres du Tableau 2 mais pour $E 1=$ $0.1 ×10^{5} \mathrm{dyn} . \mathrm{cm}^{-1}$.

![](./images/812444571907653633_5.jpg)

Fig. 5. InP-Densité d'états à deux phonons $g+(\omega)$ calculée pour les valeurs des paramètres du Tableau 2.

n'est observée entre 140 et $210 \mathrm{~cm}^{-1}$. Ceci n'est pasétonnant puisque la fonction $g+$ ne présente aucun maximum dans cette région.

Une bande très intense est observée à $237 \mathrm{~cm}^{-1}$, énergiequi correspond sensiblement à celle d'un maximum (noté $h$ Fig. 5) de $g+$. Cette bande est fortement réduite quant on abaisse la température de 77 à $4^{\circ} \mathrm{K}$. Ceci peut facilement s'expliquer par le fait qu'elle est partiellement noyée dans les bandes a de $g-$ (Fig. 6), auxquelles correspondent des bandes de différence qui disparaissent aux très basses températures. Bien que les intensités relatives des maxima de $g+$ et celles du coefficient d'absorption mesuré à $4^{\circ} \mathrm{K}$ ne soient pas directement comparables, nous remarquerons que la bande a observéeà $237 \mathrm{~cm}^{-1}$ est beaucoup plus intense que celle qui résulte de la combinaison $2 T A(X)$ à $136 \mathrm{~cm}^{-1}$.

L'origine de la large bande dont le maximum est ob- servé vers $90 \mathrm{~cm}^{-1}$ n'est pas clair. Si l'on se réferre à la Fig. 5, la fonction $g+$ se présente aux énergies inférieuresà $150 \mathrm{~cm}^{-1}$ sous la forme d'un pic à $138 \mathrm{~cm}^{-1}(2 T A(X))$ et d'une bande assez large (j) située dans le flanc de ce pic du côté des basses énergies. La bande de combinaison $j$ provient principalement des branches acoustiques. Son maximum est estimé à $130 \mathrm{~cm}^{-1}$. La bande $j$ peut contribuer au moins partiellement à la large bande observée vers $90 \mathrm{~cm}^{-1}$; toutefois, nos résultats expéri- mentaux semblent assez différents de ceux de Kirkman[41] dans ce domaine d'énergie où une bande est effectivement observée par ces auteurs à $108 \mathrm{~cm}^{-1}$ et est attribuée par eux à la combinaison $2 TA(L)$, ce qui correspond bien à l'assignation du Tableau 3. Enfin, lesbandes observées à 164 et $190 \mathrm{~cm}^{-1}$ dont l'intensité diminuè avec la température et disparaissent complète- ment à $4^{\circ} K$ sont identifiées comme étant des bandes de différence: elles correspondent aux maxima c et b de $g-(\omega)$ (Fig. 6) que l'on trouve à 159 et $190 \mathrm{~cm}^{-1}$ respectivement.

La procédure utilisée nous a donc permis d'établir un jeu de 11 paramètres susceptibles de rendre compte d'une façon satisfaisante à la fois des données neutroniques existantes et du spectre d'absorption IR que nous avons observé.

A ce niveau, nous devons formuler deux remarques: d'abord la procédure d'ajustement fournit pour laconstante de force B un degré de précision très inférieur à celui de tous les autres paramètres; c'est ainsi qu'il est possible d'admettre pour B des variations de $\pm 30 \%$ sans que les différences entres les valeurs calculées et les valeurs expérimentales du Tableau 1 deviennent no- tablement supérieures à l'erreur expérimentale. D'autre part, si les 9 premiers paramètres peuvent être déterminés(à la précision près) san ambiguïté, il n'en est pas de même pour E1 et E2.

![](./images/812444571907653633_6.jpg)

Fig. 6. InP-Densité d'états à deux phonons $g-(\omega)$ calculée pour les valeurs des paramètres du Tableau 2.

Il existe en effect quatre couples de valeurs ac-ceptables:
$$E 1 \cong \pm 0.05 × 10^{5} \text { dyn. } \mathrm{cm}^{-1} ; \quad E 2 \cong$$
 $\pm 0.11 ×10^{5}$ dyn. $cm^{-1}$ , donnant sensiblement les mêmesrésultats à la fois pour les branches $\sum$ et les fonctions $g+$ et $g-$ . Le couple choisi: $E 1=0.05 ×10^{5}$ dyn. $cm^{-1} ; E 2=$  $0.11 ×10^{5}$ dyn. $cm^{-1}$ donne simplement un accord légèremment meilleur en ce qui concerne l'énergie des maxima de $g+$ que celui que l'on obtient avec les trois autres couples. Notons que le choix du couple a une influence négligeable sur les calculs présentés dans la suite de l'article.

A partir du modèle et des 11 paramètres ainsi obtenus,nous avons calculé la densité d'états qui est donnée Fig. 7 et Tableau 5, ainsi que la variation de la température caractéristique de Debye (Fig. 8, Tableau 6) avec la température.

![](./images/812444571907653633_7.jpg)

Fig. 7. InP-Densité d'états à un phonon calculée pour les valeurs des paramètres du Tableau 2.

## PARTIE III
### III.a Impuretés isolées dans InP
Un atome du réseau $\dagger$ est désigné par deux indices: l et $\kappa$ . I désigne le numéro de la cellule élémentaire et $\kappa$ le
†Mêmes notations que dans la Réf. [37].

Dynamique de reseau et frequences des modes de vibration

Tableau 5. Maxima de la fonction de distribution a un phonon $g(\omega)$ (cm⁻¹) pour InP (Fig. 7)

|     |     |
|-----|-----|
| $a$ | 360 |
| $b$ | 350 |
| $c$ | 315 |
| $d$ | 169 |
| $e$ | 80  |
| $f$ | 69  |
| $\alpha$ | 294 |
| $\beta$  | 187 |
| $\gamma$  | 86  |

![](./images/812444571907653633_8.jpg)

Fig. 8. InP-Températures caractéristiques de Debye calculée pour les valeurs des paramètres du Tableau 2. $\square$, résultats expérimentaux[52].

Tableau 6. Valeurs calculées de la temperature caracteristique de debye $\theta_{D}$ pour differentes temperatures dans le cas de InP (Fig. 8)

| $\theta_{D}$ (K)       | $T$ (K) |
|------------------------|---------|
| 325                    | 4.97    |
| 204.3 (minimum)        | 19.89   |
| 255                    | 39.7    |
| 353                    | 77      |
| 407.5                  | 119.4   |
| 444                    | 243.7   |
| 453                    | 550     |

numéro de l'atome dans cette cellule; $\kappa=1,2$. La cellule élémentaire est constituée d'un atome de phosphore ($\kappa=1$) placé à l'origine des coordonnées et d'un atome d'indium $(\kappa=2)$ au site $(1.1.1)a_{0}/2$; $a_{0}=$ $2.9343×10^{-8}$ cm[36].

Pour une substitution isolée, l'atome $\kappa=1$, de masse $M_{1}$, est remplacé par un atome de masse $M_{1}'$ connue exactement, le défaut de masse étant caractérisé par $\epsilon_{1}=(M_{1}-M_{1}')/M_{1}$. D'autre part, et en suivant Grimm[18], nous admettons que seules les forces $f$ liant l'atome 1 à ses premiers voisins sont modifiées par la substitution $(f \rightarrow f'=af)$ et que de plus ces forces sont modifiées de la même façon, de telle sorte que les constantes de forces $A$ et $B$ des Réfs.[36,37] deviennent respectivement $aA$ et $aB$. Le paramètre utilisé dans le calcul est alors $t=1-a=(f-f')/f$. Dans ces conditions, seul l'atome substitué et ses quatre plus proches voisins sont concernés par le défaut et les matrices $\delta 1$ et $g$ de l'équation (1) sont de dimension 15×15. Une représen- tation totale (15×15) pour une symétrie tétrahédrale se décompose en représentations irréductibles de la manière suivante:

$$
\Gamma_{\text{tot}}=A_{1}+E+F_{1}+3F_{2}.
$$

Ainsi les matrices $g$ et $\delta 1$ peuvent être mises sous forme de matrices-blocs[18] $g'$ et $\delta 1'$, de telle sorte que:

$$
\operatorname{det}(I-g \cdot \delta 1) \equiv
$$

$$
\begin{aligned}
\operatorname{det}\left(I-g^{\prime} \cdot \delta 1^{\prime}\right)= & \left\{1-\left(g_{1}-2g_{9}+g_{10}-2g_{11}+4g_{12}\right)(A+2B)t\right\} \\
& ×\left\{1-\left(g_{1}-2g_{9}+g_{10}+g_{11}-2g_{12}\right)\right. \\
& ×(A-B)t\}_{x}^{2}\left\{1-\left(g_{1}-g_{10}+g_{11}+2g_{12}\right)\right. \\
& ×(A-B)t\}_{x}^{3}\left\{\operatorname{det}\left[I-g^{*} \cdot \delta 1^{*}\right]\right\}^{3}
\end{aligned}
$$

avec

$$
\delta 1^{*}=\begin{vmatrix}
4At+\omega^{2}(M_{1}-M_{1}') & -2At & -\sqrt{8}Bt \\
-2At & At & \sqrt{2}Bt \\
-\sqrt{8}Bt & \sqrt{2}Bt & t(A+B)
\end{vmatrix}
$$

$$
g^{*}=\begin{vmatrix}
g_{2} & 2g_{3} & \sqrt{8}g_{4} \\
2g_{3} & g_{1}+2g_{9}+g_{10} & \sqrt{2}g_{11} \\
\sqrt{8}g_{4} & \sqrt{2}g_{11} & g_{1}-g_{10}-g_{11}-2g_{12}
\end{vmatrix}
$$

et

$$
\begin{aligned}
& g_{1}=G_{x x}\left(12 ; 12 ; \omega^{2}-i \epsilon\right) \\
& g_{2}=G_{x x}\left(11 ; 11 ; \omega^{2}-i \epsilon\right) \\
& g_{3}=G_{x x}\left(12 ; 11 ; \omega^{2}-i \epsilon\right) \\
& g_{4}=G_{x y}\left(12 ; 11 ; \omega^{2}-i \epsilon\right) \\
& g_{5}=G_{x x}\left(11 ; 51 ; \omega^{2}-i \epsilon\right) \\
& g_{6}=G_{z z}\left(11 ; 51 ; \omega^{2}-i \epsilon\right) \\
& g_{7}=G_{x y}\left(11 ; 51 ; \omega^{2}-i \epsilon\right) \\
& g_{8}=G_{x x}\left(11 ; 51 ; \omega^{2}-i \epsilon\right) \\
& g_{9}=G_{x x}\left(12 ; 22 ; \omega^{2}-i \epsilon\right) \\
& g_{10}=G_{z z}\left(12 ; 22 ; \omega^{2}-i \epsilon\right) \\
& g_{11}=G_{x y}\left(12 ; 22 ; \omega^{2}-i \epsilon\right) \\
& g_{12}=G_{x x}\left(12 ; 22 ; \omega^{2}-i \epsilon\right)
\end{aligned}
$$

$$
\begin{aligned}
& \vec{x}(11):(0,0,0)a_{0}/2 \\
& \vec{x}(12):(1,1,1)a_{0}/2 \\
& \vec{x}(51):(2,2,0)a_{0}/2 \\
& \vec{x}(22):(-1,-1,1)a_{0}/2.
\end{aligned}
$$

Les fonctions de Green sont définies de la façon usuelle par la relation (3):

$$
\begin{aligned}
G_{\alpha \beta}(l \kappa ; l' \kappa'; \omega^{2})= & \\
& \frac{1}{N(m_{k}m_{k'})^{\frac{1}{2}}} \sum_{\vec{k}j} \frac{w_{\alpha}(\kappa|\vec{k}j)w_{\beta}^{*}(\kappa'|\vec{k}j)}{\omega^{2}-\omega_{j}^{2}(k)} \mathrm{e}^{i\vec{k} \cdot(\vec{x}(l \kappa)-\vec{x}(l' \kappa'))} \quad (3)
\end{aligned}
$$

en gardant les mêmes notations que celles des Réfs.[18,37].

Dans le cas d'une substitution de l'atome d'indium $(\kappa=2)$ par un atome de masse $M'2$ il suffit d'effectuer les changements suivants:

$$
M_{1} \rightarrow M_{2}, M_{1}' \rightarrow M_{2}', g_{9} \rightarrow g_{5}, g_{10} \rightarrow g_{6}, g_{11} \rightarrow g_{7}, g_{12} \rightarrow g_{8}
$$

et de permuter $g_{1}$ et $g_{2}$.

Le calcul des fonctions de Green a été effectué de la
façon suivante: la sommation figurant dans la formule (3)
porte sur 5832 points régulièrement répartis dans la
première zone de Brillouin. D'autre part la partie
infinitésimale $\epsilon$ ne doit pas être choisie trop petite de
façon à éviter la création de structures parasites dans les
fonctions obtenues, mais cependant assez petite pour que
leurs structures significatives ne soient pas moyennées.
La valeur retenue est $\epsilon=0.01 \omega^{2}(\Gamma(L O))=0.01(\omega_{L})^{2}$. Les
calculs ont été effectués pour un domaine de variation de
$\omega$ compris entre 0 et $2 \omega_{L}$ par pas de $0.02 \omega_{L}$.

### III.b Résultats et discussion
La masse de l'atome substitué n'intervient que dans le
mode $F 2$, lequel fournit en particulier les solutions
correspondant aux modes localisés; les trois autres modes
$A 1, E$ et $F 1$ ne dépendent donc que du paramètre
$t=1-f^{\prime} / f$ qui caractérise le défaut de force. Par ailleurs,
nous n'avons pas trouvé de solution correspondant aux
modes $E$ et $F 1$. Nous examinerons donc les vibrations
des défauts qui correspondent aux modes de symétrie de
$F 2$ et $A 1$.

Il existe actuellement très peu de résultats ex-
périmentaux publiés relatifs aux énergies de vibration
d'impuretés substitutionnelles isolées dans InP [26, 48]. Il
était donc intéressant d'étudier les cas de cristaux
similaires pour lesquels existent quelques résultats
expérimentaux: nous avons traité le cas de ZnS et celui de
GaP qui sont également des matériaux à grand gap de
phonons, dont la dynamique de réseau est connue et pour
lesquels le jeu des 11 paramètres de RIM 11 a déjà été
calculé[36]. Nous présentons simultanément les résultats
obtenus pour InP, ZnS et GaP.

Les variations calculées de la température carac-
téristique de Debye en fonction de la température sont
données pour InP sur le Tableau 6 et la Fig. 8.

#### III.b-1/ Mode $F_{2}$
Dans le cas d'une substitution de l'atome le plus léger de
la maille élémentaire on peut obtenir soit un mode de gap
soit un mode localisé selon que l'impureté est plus lourde
ou plus légère que l'atome qu'elle remplace. Si au
contraire l'atome le plus lourd de la maille est remplacé
par un atome plus léger que lui il est possible d'obtenir
simultanément un mode de gap et un mode localisé[26].
Les Figs. 9, 11, 13 et 10, 12, 14 donnent les valeurs
calculées des fréquences du mode localisé et du mode de
gap en fonction du défaut de constante de force (traits
pleins) pour InP, ZnS et GaP dans le cas d'une
substitution de l'atome léger. Les Figs. 15 à 19 cor-
respondent au cas d'une substitution de l'atome le plus
lourd par une impureté légère. Le Tableau 7 donne les
valeurs de la variation relative des forces entre premiers
voisins que l'on peut déduire du calcul compte tenu des
résultats expérimentaux. On a également porté sur le
Tableau 7 les variations relatives $\Delta \varphi / \Delta \varphi$ de la constante
de force associée à la part radiale (centrale) de l'intéraction
entre premiers voisins, calculées par Talwar et al.[35] à
l'aide d'un modèle RIM 7.

![](./images/812444571907653633_9.jpg)

Fig. 9. InP—Fréquences calculées du mode localisé $F 2$ pour diverses substitutions sur $P$ en fonction du défaut de constante de force.

![](./images/812444571907653633_10.jpg)

Fig. 10. InP—Fréquences calculées du mode de gap $F 2$ pour diverses substitutions sur $P$ en fonction du défaut de constante de force. ●, résultat expérimental[48].

![](./images/812444571907653633_11.jpg)

Fig. 11. ZnS—Fréquences calculées du mode localisé $F 2$ pour diverses substitutions sur $S$ en fonction du défaut de constante de force.

![](./images/812444571907653633_12.jpg)

Fig. 12. ZnS—Fréquences calculées du mode de gap F2 pour diverses substitutions sur S en fonction du défaut de constante de force. a, mode A1.

![](./images/812444571907653633_13.jpg)

Fig. 13. GaP—Fréquences calculées du mode localisé F2 pour diverses substitutions sur P en fonction du défaut de constante de force ●, résultats expérimentaux[48].

![](./images/812444571907653633_14.jpg)

Fig. 14. GaP—Fréquences calculées du mode de gap F2 pour diverses substitutions sur P en fonction du défaut de constante de force. ●, résultat experimental[48]; a: mode A1.

![](./images/812444571907653633_15.jpg)

Fig. 15. InP—Fréquences calculées du mode localisé F2 pour diverses substitutions sur In en fonction du défaut de constante de force. ●, résultat expérimental[48]; a: mode A1.

![](./images/812444571907653633_16.jpg)

Fig. 16. InP—Fréquences calculées du mode de gap F2 pour diverses substitutions sur In en fonction du défaut de constante de force.

![](./images/812444571907653633_17.jpg)

Fig. 17. ZnS—Fréquences calculées du mode localisé F2 pour diverses substitutions sur Zn en fonction du défaut de constante de force.●, résultats expérimentaux[48][49]; a: mode A1.

![](./images/812444571907653633_18.jpg)

Fig. 18. ZnS—Fréquences calculées du mode de gap F2 pour diverses substitutions sur Zn en fonction du défaut de constante de force. a, mode Al.

### III.b-1.1/ GaP
i/ Substitutions isoélectroniques. En ce qui concerne les modes localisés pour GaP nos résultats apparaissent en contradiction avec ceux de la Réf.[35], dans le cas de substitutions isoélectroniques sur le gallium. On obtient en effet dans ce cas, une diminution des forces entre premiers voisins alors que les résultats de Talwarindiquent du contraire un renforcement important de $18 \%$  environ [Tableau 7]. En outre, on trouve que la variation relative des forces est d'autant plus importante que la masse de l'impureté est plus faible (-0.23 pour l'aluminum et -0.53 pour le bore).

La très forte réduction de f, en particulier dans le cas du bore, peut difficilement être attribuée à un effet de taille de l'ion: ceci serait en effet en contradiction avec la nette augmentation de f que l'on trouve pour le cas où le bore est substitué à l'indium dans InP. Nous pensons que ce résultat doit plutôt être relié à l'importance relative des couplages entre premiers et seconds voisins que nous fournit le modèle de force utilisé et à l'hypothèse admise pour la perturbation $\delta 1$ (équation 1). En effet, dans le casd'une substitution d'un atome du réseau par une impuretétrès légère, on peut considérer que, dans le mode localisé et en première approximation, l'impureté vibre seule, les autres atomes du réseau restent pratiquement au repos. Dans ces conditions, les forces de rappel provenant des interactions à courtes distances auxquelles est soumises l'impureté pour un déplacement unitaire suivant l'axe x s'écrivent, dans l'hypothèse où ces forces ne sont pas

![](./images/812444571907653633_19.jpg)

Fig. 19. GaP—Fréquences calculées du mode localisé F2 pour diverses substitutions sur Ga en fonction du défaut de constante de force. ●, résultats expérimentaux[48]; a: mode Al.

<table><caption>Tableau 7.</caption>
<thead>
<tr>
<th>Système†</th>
<th>Valeurs expérimentales des fréquence du mode F2 (local ou gap) en cm⁻¹</th>
<th>$\Delta f/f=-t$ présent travail</th>
<th>$\Delta \varphi/\varphi$ Réf.[35]</th>
<th>Sources des donnees experimentales</th>
</tr>
</thead>
<tbody>
<tr>
<td>Ga P: ¹²C</td>
<td>606.2</td>
<td>+ 0.37</td>
<td>+ 0.21</td>
<td>(48)</td>
</tr>
<tr>
<td>Ga P: ¹⁴C</td>
<td>564.0</td>
<td>+ 0.37</td>
<td>+ 0.21</td>
<td>(48)</td>
</tr>
<tr>
<td>Ga P: ¹⁴N</td>
<td>488.0</td>
<td>~ 0.0</td>
<td>− 0.15</td>
<td>(48)</td>
</tr>
<tr>
<td>Ga P: 0</td>
<td>464.0</td>
<td>~ 0.0</td>
<td>− 0.13</td>
<td>(48)</td>
</tr>
<tr>
<td>Ga P: ⁹Be</td>
<td>527</td>
<td>− 0.87</td>
<td></td>
<td>(49)</td>
</tr>
<tr>
<td>Ga P: ¹¹B</td>
<td>571</td>
<td>− 0.53</td>
<td>+ 0.18</td>
<td>(48)</td>
</tr>
<tr>
<td>Ga P: Al</td>
<td>444.7</td>
<td>− 0.23</td>
<td>+ 0.19</td>
<td>(48)</td>
</tr>
<tr>
<td>Ga P: ²⁸Si</td>
<td>464.9</td>
<td>− 0.08</td>
<td>+ 0.39</td>
<td>(48)</td>
</tr>
<tr>
<td>In P: ¹¹B</td>
<td>522.8</td>
<td>+ 0.25</td>
<td></td>
<td>(48)</td>
</tr>
<tr>
<td>Zn S: ⁹Be</td>
<td>490</td>
<td>+ 0.1</td>
<td>+ 0.16</td>
<td>(48)</td>
</tr>
<tr>
<td>Zn S: ²⁵Mg</td>
<td>377.5</td>
<td>+ 0.2</td>
<td>+ 0.07</td>
<td>(48)</td>
</tr>
<tr>
<td>Zn S: Al</td>
<td>438</td>
<td>+ 0.76</td>
<td>+ 0.58</td>
<td>(49)</td>
</tr>
<tr>
<td>Ga P: As</td>
<td>270</td>
<td>− 0.33</td>
<td></td>
<td>(48)</td>
</tr>
<tr>
<td>Ga P: ¹⁰B</td>
<td>293.8</td>
<td></td>
<td></td>
<td>(48)</td>
</tr>
<tr>
<td>Ga P: ¹¹B</td>
<td>284.8</td>
<td></td>
<td></td>
<td>(48)</td>
</tr>
<tr>
<td>In P: As</td>
<td>223</td>
<td>+ 0.07</td>
<td></td>
<td>(26)</td>
</tr>
<tr>
<td colspan="2">Calculé avec:<br>$\Delta f/f=$</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Zn S: ⁹Be</td>
<td>250 + 0.1</td>
<td>246</td>
<td></td>
<td>(48)</td>
</tr>
<tr>
<td>Zn S: Al</td>
<td>231 + 0.76</td>
<td>229</td>
<td></td>
<td>(48)</td>
</tr>
<tr>
<td>In P: ¹¹B</td>
<td>257 + 0.25</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td colspan="5">†Les atomes soulignés sont les atomes substitués.</td>
</tr>
</tbody>
</table>

modifiées:
$$R_{i}=4 A+8 C_{i}+4 F_{i}$$
où $i=1,2$ est le numéro dans la maille de l'atome substitué[36].

A d'une part, $C_{i}$ et $F_{i}$ d'autre part, sont ici les constantes de forces qui figurent dans les diagonales des matrices de couplage entre premiers voisins et seconds voisins respectivement (notations des Réfs.[36,37]. Le Tableau 8 donne le paramètre $p_{i}=4 A /(4 A+8 C_{i}+4 F_{i})$ qui représente la contribution à des forces entre premiersvoisins par rapport à celle de l'ensemble des forces à courtes distances auxquelles est soumise l'impureté. Pour une substitution sur le zinc dans ZnS et sur le phosphoredans GaP le paramètre p est assez proche de 1 (1.2 et 1.18 respectivement). Ceci est dû au fait que dans ce cas 4F et8C se compensent d'une façon appréciable, F et C étant de signes opposés. Dans ces deux cas, où les forces appliquées sont principalement dues aux forces entre premiers voisins, on doit s'attendre à ce que I'hypothèse que nous avons admise, à savoir que seules les forces entre premiers voisins sont susceptibles d'être modifiées, conduise à des résultats assez corrects. Par contre, pour le cas d'une substitution d'un atome léger sur le gallium dans GaP, où la contribution des forces entre seconds voisins est importante (p = 0.6) notre hypothese peut conduire à des résultats incorrects. Il faudrait alors tenir compte des modifications des forces entre secondsvoisins. Ces considérations rendent compte, en partie, à notre avis de la valeur anormalement élevée du défaut de force (t = +0.53) que I'on trouve pour une substitution isoélectronique du bore sur le gallium dans GaP. Elles soulignent également I'importance du choix du modele de force et des approximations à priori qui peuvent être faites sur les forces entre seconds voisins prises en compte par le modèle.

<table><caption>Tableau 8.</caption>
<tbody><tr><th></th><th>$pi=4A/(4A+8Ci+4Fi)$</th></tr>
<tr><td>Zn S; Zn-Zn</td><td>1.20</td></tr>
<tr><td>Zn S; S-S</td><td>0.68</td></tr>
<tr><td>In P; In-In</td><td>1.33</td></tr>
<tr><td>In P; P-P</td><td>0.77</td></tr>
<tr><td>Ga P; Ga-Ga</td><td>0.60</td></tr>
<tr><td>Ga P; P-P</td><td>1.18</td></tr>
</tbody></table>

ii/ Cas général. Des calculs de modes localisés et de modes de gap d'impuretés substitutionnelles isolées ontété effectués par Gaur et al. pour un ensemble de composés III V et II VI en utilisant un modele d'ions rigides à quatre paramètres sans considérer la variation des forces interatomiques [24] (Approximation du défaut isotopique, I.D.A.). Ces résultats ont été comparés par Grimm à un ensemble de données expérimentales relatives aux modes localisés dans les composés III V. Cet auteur a pu ainsi obtenir une vue d'ensemble des variations relatives de forces à courtes distances qu'il est nécessaire de considérer pour rendre compte des donnéesexpérimentales. Il trouve:
Aff~0 pour une substitution isoélectronique sur les sites III ou V.
Aff~ +0.25 pour un donneur simple sur un site du groupe III ou un accepteur simple sur un site du groupe V.
Aff~ -0.25 pour un accepteur simple sur un site du groupe III.
Ainsi, le défaut de constante de force varie directement avec la différence de charge entre le défaut et ses voisins [39]. La même tendance a été observée au cours du présent travail: le Tableau 7 montre que pour une substitution atomique de masse M' sur un site du groupe III, si I'on prend comme référence les forces qui correspondent à une substitution isoélectronique par un atome de masse voisine de M', la variation de force est négative dans le cas d'un accepteur simple.
$$\frac{\delta f_{\mathrm{Be}}}{f}=\frac{\Delta f_{\mathrm{Be}}-\Delta f_{\mathrm{B}}}{f}=\frac{f_{\mathrm{Be}}^{\prime}-f_{\mathrm{B}}^{\prime}}{f} \#-0.35$$
et positive dans celui d'un donneur simple:
$$\frac{\delta f_{\mathrm{Si}}}{f}=\frac{\Delta f_{\mathrm{Si}}-\Delta f_{\mathrm{Al}}}{f} \#+0.15.$$

Dans le cas de la substitution isoélectronique de l'azote sur le phosphore on trouve que les forces ne sont pas modifiées $(\Delta f / f ≈0)$ . Compte tenu des considérations précédentes sur I'importance relative des forces entre premiers et seconds voisins, dans ce cas, ce résultat est probablement correct. Un problème se pose pour I'oxygène dans GaP [48], normalement en position de donneur sur le site phosphore. On trouve, exactement comme dans le cas de la substitution isoélectronique N/P, que $\Delta f f$ est nul alors que l'application du raisonnement de Grimm à ce système conduirait au contraire à $\Delta f f$ négatif. Ceci suggere que dans I'échantillon examiné I'oxygène pourrait ne pas se trouver en substitution sur le phosphore. Une telle situation mérite d'être réexaminée.
iii/ Remarque. On ne trouve pas de mode de gap dans le cas d'une substitution du gallium par une impureté légèrealors qu'il existe des résultats expérimentaux pour $^{10} B / Ga$  $(238.8 cm^{-1})$ et $^{11} B / Ga(234.8 cm^{-1})$ et que les calculs de Gaur et al.[24] donnent respectivement 289.2 et287.9 cm-' en utilisant un modele d'ions rigides à quatre parametres et en négligeant la variation des forces entre premiers voisins. Il n'est pas impossible que ce résultat négatif soit lié, au moins en partie au fait que le modele de force utilisé surestime d'une facon tres appréciable(environ 20%) I'énergie des phonons LA au point L par rapport aux données expérimentales [36]. Par contre pour InP et ZnS, nous avons trouvé comme prévu un mode localisé et un mode de gap. Pour ces composés, la variation relative de force est obtenue à partir des données ex- périmentales et du calcul des modes localisés. La fréquence du mode de gap est ensuite calculée à partir de cette variation et comparée à la valeur expérimentale.

776
M. VANDEVYVER et P. PLUMELLE

### III.b-1.2/ InP
On trouve $\Delta f / f=+0.25$ pour le bore en substitution sur l'indium (mode localisé). Cette valeur reportée sur le graphique de la Fig. 16 conduit à prévoir qu'un mode de gap correspondant est située vers $257 \mathrm{~cm}^{-1}$. Mal heureusement il n'existe pas de résultats expérimentaux pour vérifier ce résultat. Par ailleurs, le mode de gapobservé à $270 \mathrm{~cm}^{-1}$ pour la substitution As/P conduit à une variation relative des forces quasi nulle (0.07).

### III.b-1.3/ ZnS
Pour ZnS, nos résultats sont en accord assez satis- faisants avec ceux de la Réf.[35]. Les valeurs trouvées de $\Delta f / f$ pour Be et Mg/Zn sont assez voisines (0.1 et 0.2 respectivement) alors que pour la substitution de l'aluminium donneur sur le zinc on obtient une augmentation des forces entre premiers voisins (t = - 0.76)également très élevée. Ce point à été noté par Dutt et al.[50] et semble être une règle générale pour l'aluminium dans les II VI. Partant de ces résultats, il est possible de calculer l'énergie des modes de gap correspondants. On obtient $250 \mathrm{~cm}^{-1}$ pour une valeur expérimentale de246 cm-1 dans le cas du Be/Zn[42]. Par ailleurs, pour Al / Zn, on est conduit à la valeur de $231 cm^{-1}$ très proche de la valeur expérimentale de $229 cm^{-1}$ [48] (symétrie desite non déterminée). Ceci implique que le système étudié correspond bien à Al en position substitutionnelle et doncà une symétrie tétrahédrale. Dans le cas du ZnS, le paramètre p (Tableau 2) est assez proche de 1 (1.2) pour une substitution sur le zinc. Les forces entre secondsvoisins sont donc faibles et notre hypothèse qui consiste à ne pas tenir compte de leurs variations est bien vérifiée. Le modèle donne alors dans ce cas une description assez satisfaisante à la fois de la fréquence du mode localisé et de celle du mode de gap pour Be et Al/Zn.

### III.b-1.4/ Remarque
La dépendance calculée de la fréquence du mode de gap en fonction du défaut de constante de force, traduit bien, comme on pouvait s'y attendre, la nature du mouvement auquel est soumise l'impureté dans ce mode de vibration: dans le cas d'une substitution d'atomes lourds sur l'atome le plus léger de la cellule élémentaire, la fréquence calculée du mode de gap dépend fortement des forces entre l'impureté et ses premiers voisins (Figs. 10,12 et 14). Ceci correspond bien au fait que l'impureté vibre en opposition de phase avec eux. Au contraire, dans le cas d'une impureté légère sur l'atome le plus lourd, dans le mode de gap, l'impureté vibre en phase avec ses premiers voisins[26] ce qui conduit à l'existence d'un domaine de variation du paramètre t où la fréquence du mode dépend peu des forces entre l'impureté et ses premiers voisins qui vibrent rigidement en bloc (ceci est particulièrement net dans le cas de ZnS (Fig. 18)); ceci est confirmé par une description correcte de résultats expérimentaux pour deux valeurs de t tres distinctes (-0.1 pour Be/Zn et - 0.76 pour Al/Zn).

Les modes de bande ont également été calculés pour InP (Fig. 20 et Fig. 21) ainsi que pour ZnS. Ils montrent les mêmes tendances que les modes de gap en ce qui concerne la fréquence calculée en fonction de t.

![](./images/812444571907653633_20.jpg)
Fig. 20. InP--Fréquences calculées du mode de bande F2 pour diverses substitutions sur P en fonction du défaut de constance de force.

![](./images/812444571907653633_21.jpg)
Fig. 21. InP--Fréquences calculées du mode de bande F2 pour diverses substitutions sur In en fonction du défaut de constante de force.

Malheureusement il n'existe pas actuellement de résultats expérimentaux sur les modes de bande dans ces composés.

### III.b-2/ Mode $A_{1}$
Dans le mode $A_{1}$ l'atome substitué est immobile, la fréquence de ce mode est donc indépendante de la masse de l'impureté et ne dépend que de t. On rencontre des solutions principalement dans le cas d'une substitution sur l'atome le plus lourd de la cellule élémentaire (Figs. 15, 17,19; courbes en pointillées). La fréquence du mode dépend alors très peu de t et est légèrement supérieure à la fréquence maximum du spectre de phonons.

## IV. CONCLUSION
L'utilisation d'un modèle d'ions rigides incluant les forces générales entre atomes premiers voisins, seconds voisins et les forces de Coulomb permet de rendre compte pour le phosphure d'indium, à la fois des résultats neutroniques existants et des courbes de transmission IR dans le domaines des mécanismes à deux phonons. A partir de ce modèle, nous avons calculé les fréquences des modes vibrationnels correspondants aux substitutionsd'impuretés isolées en fonction de la masse de l'impureté et du défaut de forces entre premiers voisins pris comme paramètres (on fait l'hypothèse que les forces entre seconds voisins ne sont pas modifiées). Les données

expérimentales sont très rares pour InP et ceci ne permet pas d'obtenir une vue générale du défaut de force introduit par l'impureté.

Deux autres matériaux à grand gap de phonons ayant la structure de la blende; GaP et ZnS, ont été également étudiés. Pour GaP les valeurs trouvées du défaut de force, en particulier pour des substitutions isoelec- troniques sur le gallium, sont anormalement grandes et par ailleurs le calcul ne donne pas le mode de gap attendu pour une substitution d'atome léger sur le gallium. Cette situation peut s'expliquer au moins en partie par l'importance relative des forces entre seconds voisins Ga-Ga dont la variation éventuelle n'est pas prise en compte dans le modèle. Pour ZnS, on obtient un accord satisfaisant entre les données expérimentales existantes et les résultats du calcul à la fois pour les modes localisés et les modes de gap. Ceci est dû à notre avis à la compensation des forces entre seconds voisins dont, de ce fait, les variations éventuelles peuvent être négligées.

Actuellement, RIM 11 rend compte d'une façon satisfaisante des données neutroniques pour de nombreux composés II VI et III V[36,37] et il existe pour ces composés de très nombreux résultats expérimentaux relatifs aux fréquences de vibration d'impuretés sub- stitutionnelles isolées[48]. Il serait intéressant d'étendre le présent travail à ces composés de façon à apprécier la part prise par les forces entre seconds voisins (ou leurs variations) à la détermination des fréquences de vibration des impuretés.

## BIBLIOGRAPHIE
1. Talwar D. N. et Agrawal B. K., Phys. Rev. B12, 4, 1432 (1975).
2. Kachare A. H., Spitzer W. G., Lorimor O. G., Euler F. K. et Brown R. N., J. Appl. Phys. (U.S.A.) 45, 5475 (1974).
3. Thompson F. et Newman R. C., J. Phys. C. (G.B.); Solid State Phys. 7, 1999 (1972).
4. Morisson S. R., Newman R. C. et Thompson F., J. Phys. C.(G.B.); Solid State Phys. 7, 633 (1974).
5. Morisson S. R. et Newman R. C., J. Phys. C. (G.B.); Solid State Phys. 7, 627 (1974).
6. Morisson S. R. et Newman R. C., J. Phys. C. (G.B.); Solid State Phys. 7, 619 (1974).
7. Leung, P. C., Fredrickson J., Spitzer W. G., Kahan A. et Bouthillette L., J. Appl. Phys. 45, 1009 (1974).
8. Dutt B. V., Al Delaimi M. et Spitzer W. G., J. Appl. Phys. 47,565 (1976).
9. Dutt B. V. et Spitzer W. G., J. Appl. Phys. 47, 573 (1976).
10. Nazarewicz W., Balkanski M., Morhange J. F. et Sebenne C., Solid State Comm. 9, 1719 (1971).
11. Ikuta Y., Manabe A., Mitsuishi A., Komiya H. et Ibuki S., Optics Comm. 5, 4, 285 (1972).
12. Sennett C. T., Bosomworth D. R., Hayes W. et Spray A. R. L., J. Phys. C. (G.B.); Solid State Phys. Serie 2 2, 1137 (1969).
13. Talwar D. N. et Agrawal B. K., Phys. Rev. B9, 10, 4362 (1974).
14. Gross E. F., Safarov V. I., Sedov V. E. et Marushchak V. A., Fiz. Tverd. Tela 11, 348 (1969) [English Translation: Soviet Phys. Solid State 11, 277 (1969)].
15. Gross E. F. et Safarov V. I., Fiz. Tekh. Poluprov 1, 297 (1967)[English Translation: Soviet Phys. Semi-cond. 1, 241 (1967)].
16. Brout R. et Visscher W. M., Phys. Rev. Letters 9, 54 (1962);Kagan Y. M. et Iosilevskii Ya. A., Z. Ekspr. Teor. Fiz. 42, 259(1962) [English Translation: Soviet Phys. JETP 15, 182(1962)]; Takenos S., Prog. Theor. Phys. 29, 191 (1963).
17. Safarov V. I., Sedov V. E. et Yugovat G., Fiz. Tekh. Poluprov4, 150 (1970) [English Translation: Soviet Phys. Semicond. 4,119 (1970)].
18. Grimm A., Maradudin A. A., Ipatova I. P. et Subashiev A. V., J. Phys. Chem. Solids. 33, 775 (1972).
19. Jaswal S. S., Phys. Rev. 138, 685 (1965).
20. Krishanmurthi N. et Haridasan T. M., Ind. J. Pure Appl. Phys.7, 89 (1969).
21. Jain K. P. et Parbhakaran A. K., Phys. Rev. B8, 1503 (1973).
22. Solid State Physics Suppl. 3, p. 365. Academic Press, New York (1971).
23. Balkanski M., Beserman R. et Vodopianov L. K., Localised Excitation in Solids, p. 154. Wallis, Plenum Press, New York(1968)
24. Gaur S. P., Vetelino J. F. et Mitra S. S., J. Phys. Solids 32,2737 (1971).
25. Talwar D. N. et Agrawal B. K., Phys. Rev. B12, 4, 1432 (1975).
26. Barker A. S., Jr. et Sievers A. J., Rev. of Modern Physics 47, Suppl. No. 2, Fall 1975.
27. Vegetalos N., Wehe D. et King J. S., J. Chem. Phys. 60(9),3613 (1974).
28. Rowe J. M., Niklow R. M., Price D. L. et Zario Z., Phys. Rev. B10, 2, 671 (1974).
29. Dolling G. et Waugh J. L. T., Lattice Dynamics (Edited by R. F. Wallis), p. 19. Pergamon, Oxford (1965).
30. Yarnell J. L., Warren J. L. et Wenzer R. G., Neutron Inelastic Scattering, Vol. 1, p. 301. I.A.E.A., Vienna (1968).
31. Price D. L., Rowe J. M. et Nicklow R. M., Phys. Rev. B3, 1268(1971).
32. Farr M. K., Traylor J. G. et Sinha S. K., Phys. Rev. B11, 1587(1975).
33. Vetelino J. F., Mitra S. S. et Namjoshi K. V., Phys. Rev. B2,967 (1970).
34. Talwar D. N. et Agrawal B. K., Phys. Rev. B8, 2, 693 (1973).
35. Talwar D. N. et Agrawal B. K., Phys. Rev. B12, 4, 1432 (1975).
36. Kunc K., Ann. Phys. Masson No. 5 (1973-1974); Kunc K.,Balkanski M. et Nusimovici M. A., Phys. Stat. Sol. 72, 229(1975); 72, 249 (1975).
37. Plumelle P. et Vandevyer M., Phys. Stat. Sol. (b)73, 271 (1976).
38. Karo A. M. et Hardy J. R., Phys. Rev. 129, 2024 (1963); Phys. Rev. 141, 696 (1966); Phys. Rev. 181, 1272 (1969).
39. Borcherds P. H., Alfrey G. F., Saunderson D. H. et Woods A. D. B., J. Phys. C.: Solid States Phys. 8, 2022 (1975).
40. Hodgson J. N., Optical Absorption and Dispersion in Solids, p. 40. Chapman and L.T.D., London (1970).
41. Kirman R. F., Phys. Letters 54A, 1, 31 (1975).
42. Eaves L., et al., J. Phys. C1, 1999 (1954).
43. Alfrey G. F. et Borcherds P. H., J. Phys. C. 5, 20 (1972).
44. Birman J. L., Phys. Rev. 131, 4, 1489 (1963).
45. Hayes W., Mac Donald H. F. et Sennet C. T., J. Phys. C.(Solid State Phys.) 2, 2402 (1969).
46. Newman R., Phys. Rev. 111, 6, 1518 (1958).
47. Oswald F., Z. Naturforschg. 14a, 374 (1959).
48. Mitsuishi A. et Manabe A., OYO Butsuri 41, 7 (1972).
49. Grimm A., Lattice Defects in Semiconductors (1974); International Conference on Lattice Defects in Semiconduc- tors. Freiburg 22-5 July 1974, Conference Series N 23, Institute of Physics London.
50. Dutt B. V., Al-Delaimi M. et Spitzer W. G., J. Appl. Phys. 47,565 (1976).
51. Ulrici B. et Jahne E., Phys. Stat. Sol. (b)74, 601 (1976).
52. Piesberren U., Z. F. Naturforschung 18a, 141, Février 1963.
2360
日本機械学会論文集(第2部)
621.438.01:621.454:662.61
ジェットエンジンおよびガスタービンの燃焼ガスの状態量に対する新計算法*
(第3報,解離度と空気過剰率との関係)
田中敬吉**,石田德保***,出原 清****

1. ま え が き
第1報(1)で熱解離を無視したときの燃焼ガスの状態量を $200 2000^{\circ} K$ の範囲について, 第 2 報(2)ではCO, $H_2$ の解離生成を考慮したときのエンタルピを $2000 3000^{\circ} K$ の範囲について計算した. しかし OHの熱解離を考慮に入れると入れないとでは状態量の値に無視できぬ程度の差があるので, $CO, H_{2}, OH$ の生成を考慮したときの燃焼ガスの状態量を計算することとした. 本報ではまず解離度と空気過剰率との関係式をもとめ,燃料JP-4について計算した結果についてまとめたものである. ラムジェットエンジンの性能計算にも使えるように温度, 圧力の計算範囲などについても第2報より改良した.

2. 解離度と空気過剰率との関係式
2·1 基礎的条件 燃焼は完全燃焼とし燃焼ガスの成分気体には完全ガスの状態式を適用する. 各元素の原子量ならびに空気および燃料 JP-4 の組成 $^{(21)}$ その他, 特に断わらない事項は前報と同じである.
 $2 \cdot 2$ 熱解離反応式と平衡定数 $C, H_{2}$ を燃焼成分とする燃料を考え, 熱解離の反応式として次の三つをとり, これを基本反応式と呼びことにする.
$$\left.\begin{array}{l} 2 \mathrm{CO}_{2} \rightleftarrows 2 \mathrm{CO}+\mathrm{O}_{2} \\ 2 \mathrm{H}_{2} \mathrm{O} \rightleftarrows 2 \mathrm{H}_{2}+\mathrm{O}_{2} \\ 2 \mathrm{H}_{2} \mathrm{O}+\mathrm{O}_{2} \rightleftarrows 4 \mathrm{OH} \end{array}\right\}........................(1)$$

これらに対応する解離度をそれぞれ $\alpha_{k}, \alpha_{w}, \alpha_{h}$ とする. また平衡定数は
$$\left.\begin{array}{l} K_{p \mathrm{CO}_{2}}(T)=\left(p_{\mathrm{CO}}{ }^{2} p_{\mathrm{O}_{2}}\right) / p_{\mathrm{CO}_{2}}{ }^{2} \\ K_{p \mathrm{H}_{2} \mathrm{O}}(T)=\left(p_{\mathrm{H}_{2}}{ }^{2} p_{\mathrm{O}_{2}}\right) / p_{\mathrm{H}_{2} \mathrm{O}}{ }^{2} \\ K_{p \mathrm{OH}^{\prime}}(T)=p_{\mathrm{OH}}{ }^{4} /\left(p_{\mathrm{H}_{2} \mathrm{O}}{ }^{2} p_{\mathrm{O}_{2}}\right) \end{array}\right\}...............(2)$$

ここに $p_{O_{2}}$ などは成分気体の分圧である.
式(1)の組合せからさらに
$$\left.\begin{array}{l} \mathrm{CO}_{2}+\mathrm{H}_{2} \rightleftarrows \mathrm{H}_{2} \mathrm{O}+\mathrm{CO} \\ 2 \mathrm{H}_{2} \mathrm{O} \rightleftarrows \mathrm{H}_{2}+2 \mathrm{OH} \\ 2 \mathrm{OH} \rightleftarrows \mathrm{H}_{2}+\mathrm{O}_{2} \end{array}\right\}........................(3)$$

これらに対応する平衡定数はそれぞれ
$$\left.\begin{array}{l} K_{p w}(T)=\left(p_{\mathrm{H}_{2} \mathrm{O}} p_{\mathrm{CO}}\right) /\left(p_{\mathrm{CO}_{2}} p_{\mathrm{H}_{2}}\right) \\ K_{p \mathrm{H}_{2} \mathrm{O}^{\prime}}(T)=\left(p_{\mathrm{H}_{2}} p_{\mathrm{OH}}{ }^{2}\right) / p_{\mathrm{H}_{2} \mathrm{O}}{ }^{2} \\ K_{p \mathrm{OH}}(T)=\left(p_{\mathrm{H}_{2}} p_{\mathrm{O}_{2}}\right) / p_{\mathrm{OH}}{ }^{2} \end{array}\right\}............(4)$$

2·3 平衡定数と解離度との関係 燃焼反応を一般表示すると前報式(1)と同様に
$$\begin{aligned} & A\left(\mathrm{C}+a_{\mathrm{H}_{2}} \mathrm{H}_{2}+a_{\mathrm{O}_{2}} \mathrm{O}_{2}+a_{\mathrm{N}_{2}} \mathrm{~N}_{2}+a_{\mathrm{Ar}} \mathrm{Ar}\right) \\ & \quad \to n_{\mathrm{CO}_{2}} \mathrm{CO}_{2}+n_{\mathrm{H}_{2} \mathrm{O}} \mathrm{H}_{2} \mathrm{O}+n_{\mathrm{O}_{2}} \mathrm{O}_{2}+n_{\mathrm{CO}} \mathrm{CO} \\ & \quad +n_{\mathrm{H}_{2}} \mathrm{H}_{2}+n_{\mathrm{OH}} \mathrm{OH}+n_{\mathrm{N}_{2}} \mathrm{~N}_{2}+n_{\mathrm{Ar}} \mathrm{Ar} \quad \cdots \cdots(5) \end{aligned}$$
ここに, $a_{H_{2}}$ など: 混合気中の炭素モル数に対する各成分気体のモル数比. $n_{CO_{2}}$ など: 燃焼ガスが状態 (T,p)で平衡状態にあるときの成分気体のモル数. A:考えるべきガス量で, 混合気中の炭素のモル数をあらわす.
aH,などは第2報式(9)により
$$\left.\begin{array}{l} a_{\mathrm{H}_{2}}=\left(\frac{\mathrm{H}}{\mathrm{C}}\right)_{\text {fuel }} \frac{M_{\mathrm{C}}}{M_{\mathrm{H}_{2}}}, \quad a_{\mathrm{O}_{2}}=\left(1+\frac{1}{2} a_{\mathrm{H}_{2}}\right) n \\ a_{\mathrm{N}_{2}}=\left(\frac{\mathrm{N}_{2}}{\mathrm{O}_{2}}\right)_{\text {air }} \frac{M_{\mathrm{O}_{2}}}{M_{\mathrm{N}_{2}}} a_{\mathrm{O}_{2}}+\left(\frac{\mathrm{N}}{\mathrm{C}}\right)_{\text {fuel }} \frac{M_{\mathrm{C}}}{M_{\mathrm{N}_{2}}} \\ a_{\mathrm{Ar}}=\left(\frac{\mathrm{Ar}}{\mathrm{O}_{2}}\right)_{\text {air }} \frac{M_{\mathrm{O}_{2}}}{M_{\mathrm{Ar}}} a_{\mathrm{O}_{2}} \end{array}\right\}$$

ここに n: 空気過剩率, $M_{C}$ など: 分子量, $(H / C)_{fuel }$ , $(N / C)_{fuel }$ : 燃料の水炭比と窒素指数 (重量比), $(N_{2} /$  $O_{2})_{air},(Ar / O_{2})_{air}$ : 空気中の成分ガス重量比.
質量保存則により式(5)から
$$\left.\begin{array}{l} A=n_{\mathrm{OC}_{2}}+n_{\mathrm{CO}} \\ a_{\mathrm{H}_{2}} A=n_{\mathrm{H}_{2} \mathrm{O}}+n_{\mathrm{H}_{2}}+(1 / 2) n_{\mathrm{OH}} \\ a_{\mathrm{O}_{2}} A=n_{\mathrm{CO}_{2}}+(1 / 2) n_{\mathrm{H}_{2} \mathrm{O}}+n_{\mathrm{O}_{2}} \\ \quad +(1 / 2) n_{\mathrm{CO}}+(1 / 2) n_{\mathrm{OH}} \\ a_{\mathrm{N}_{2}} A=n_{\mathrm{N}_{2}}, \quad a_{\mathrm{Ar}} A=n_{\mathrm{Ar}} \end{array}\right\}............(7)$$

解離度とモル数との関係から
$$\left.\begin{array}{l} n_{\mathrm{CO}} / n_{\mathrm{CO}_{2}}=\alpha_{k} /\left(1-\alpha_{k}\right) \\ n_{\mathrm{H}_{2}} / n_{\mathrm{H}_{2} \mathrm{O}}=\alpha_{w} /\left(1-\alpha_{w}-\alpha_{h}\right) \\ n_{\mathrm{OH}} / n_{\mathrm{H}_{2} \mathrm{O}}=2 \alpha_{h} /\left(1-\alpha_{w}-\alpha_{h}\right) \end{array}\right\}...............(8)$$

* 昭和43年10月12日 山梨地方講演会において講演,原稿受
付 昭和46年1月11日.
** 名誉員,正員,上智大学理工学部.
*** 正員,山梨大学工学部(甲府市武田4).
****正員,茨城大学工学部.
NII-Electronic Library Service

37卷304号(昭46-12) ジェットエンジンおよびガスタービンの燃焼ガスの状態量に対する新計算法(第3報)

式(7), (8)から
$$
\left.
\begin{array}{l}
n_{\mathrm{CO}_{2}}=A\left(1-\alpha_{k}\right) \\
n_{\mathrm{H}_{2} \mathrm{O}}=a_{\mathrm{H}_{2}} A\left(1-\alpha_{w}-\alpha_{h}\right) \\
n_{\mathrm{O}_{2}}=A n_{\mathrm{O}_{2}}{ }^{\prime} \\
n_{\mathrm{O}_{2}}{ }^{\prime}=a_{\mathrm{O}_{2}}-\left\{1-(1 / 2) \alpha_{k}\right\} \\
\quad -(1 / 2) a_{\mathrm{H}_{2}}\left(1-\alpha_{w}+\alpha_{h}\right) \\
n_{\mathrm{CO}}=A \alpha_{k}, \quad n_{\mathrm{H}_{2}}=a_{\mathrm{H}_{2}} A \alpha_{w} \\
n_{\mathrm{OH}}=2 a_{\mathrm{H}_{2}} A \alpha_{h}, \quad n_{\mathrm{N}_{2}}=a_{\mathrm{N}_{2}} A \\
n_{\mathrm{Ar}}=a_{\mathrm{Ar}} A
\end{array}
\right\}............(9)
$$

Aに与えるべき条件としては前報と同様に RT/V=1(Rは普遍ガス定数)なるガス量を考えると
$$p=\sum_{x} n_{x}, \quad p_{x}=n_{x}$$

ただし: p:全圧, $p_{x}$ : 成分ガス “ x ” の分圧この関係と式(2),(4),(9)とから
$$
\left.
\begin{array}{l}
p=A P_{0} \\
P_{0}=\left(\alpha_{k} / 2\right)+a_{\mathrm{H}_{2}}\left(\alpha_{w}+\alpha_{h}\right) / 2 \\
\quad +\left(a_{\mathrm{H}_{2}} / 2\right)+a_{\mathrm{O}_{2}}+a_{\mathrm{N}_{2}}+a_{\mathrm{Ar}} \\
K_{p \mathrm{CO}_{2}}(T)=\left(\frac{\alpha_{k}}{1-\alpha_{k}}\right)^{2} \frac{n_{\mathrm{O}_{2}}{ }^{\prime}}{P_{0}} p \\
K_{p w}(T)=\frac{\alpha_{k}}{1-\alpha_{k}} \frac{1-\alpha_{w}-\alpha_{h}}{\alpha_{w}} \\
K_{p \mathrm{OH}}(T)=\frac{n_{\mathrm{O}_{2}}{ }^{\prime}}{4 a_{\mathrm{H}_{2}}} \frac{\alpha_{w}}{\alpha_{h}{ }^{2}}
\end{array}
\right\}............(10)
$$

上式から解離度を直接求めることはできない( $\alpha_{k}$ についての高次式になる) ので, $a_{O_{2}}$ について整理して
$$
\begin{array}{r}
\left(a_{\mathrm{O}_{2}} h_{6}+h_{7}\right)\left(a_{\mathrm{O}_{2}} h_{8}+h_{9}\right)=4 a_{\mathrm{H}_{2}} K_{p \mathrm{OH}}\left(a_{\mathrm{O}_{2}} h_{4}+h_{5}\right)^{2} \\
............(11)
\end{array}
$$

の形にまとめ, これを $a_{O_{2}}$ について解き, かつ式 (6)第 2 式の $a_{O_{2}}$ と n との関係をもちいると
$$n=\frac{h_{10}-h_{11}-\sqrt{h_{12}{ }^{2}+h_{13}}}{h_{14}} \cdots \cdots \cdots \cdots \cdots \cdots(12)$$

ここに
$$h_{14}=2\left\{1+\left(a_{\mathrm{H}_{2}} / 2\right)\right\}\left(h_{6} h_{8}-4 a_{\mathrm{H}_{2}} K_{p \mathrm{OH}} h_{4}{ }^{2}\right)$$

$$h_{13}=16 a_{\mathrm{H}_{2}} K_{p \mathrm{OH}} h_{6}\left\{\left(\frac{K_{p w}}{\beta_{k}}+1\right) h_{6} h_{9}+h_{5} h_{8}\right\}$$

$$h_{12}=h_{7} h_{8}-h_{6} h_{9}, \quad h_{11}=h_{7} h_{8}+h_{6} h_{9}$$

$$h_{10}=8 a_{\mathrm{H}_{2}} K_{p \mathrm{OH}} h_{4} h_{5}$$

$$h_{9}=\left(a_{\mathrm{H}_{2}} / 2\right)\left(h_{7}-h_{5}\right)-\left\{-\left(\alpha_{k} / 2\right)+\left(a_{\mathrm{H}_{2}} / 2\right)+1\right\}$$

<table><caption>表1</caption>
 <thead>
  <tr>
   <th>
    $\frac{^\circ\text{K}}{\text{kg}/\text{cm}^2}$
   </th>
   <th>
    2 000
   </th>
   <th>
    2 250
   </th>
   <th>
    2 500
   </th>
   <th>
    2 750
   </th>
   <th>
    3 000
   </th>
   <th>
    3 500
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>
    0.05
   </td>
   <td>
    ○
   </td>
   <td>
    ○
   </td>
   <td>
    ○
   </td>
   <td>
    ―
   </td>
   <td>
    ―
   </td>
   <td>
    ―
   </td>
  </tr>
  <tr>
   <td>
    0.1
   </td>
   <td>
    ○
   </td>
   <td>
    ○
   </td>
   <td>
    ○
   </td>
   <td>
    ○
   </td>
   <td>
    ○
   </td>
   <td>
    ○
   </td>
  </tr>
  <tr>
   <td>
    1
   </td>
   <td>
    ○
   </td>
   <td>
    ○
   </td>
   <td>
    ○
   </td>
   <td>
    ○
   </td>
   <td>
    ○
   </td>
   <td>
    ○
   </td>
  </tr>
  <tr>
   <td>
    5
   </td>
   <td>
    ○
   </td>
   <td>
    ○
   </td>
   <td>
    ○
   </td>
   <td>
    ○
   </td>
   <td>
    ○
   </td>
   <td>
    ○
   </td>
  </tr>
  <tr>
   <td>
    10
   </td>
   <td>
    ○
   </td>
   <td>
    ○
   </td>
   <td>
    ○
   </td>
   <td>
    ○
   </td>
   <td>
    ○
   </td>
   <td>
    ○
   </td>
  </tr>
  <tr>
   <td>
    20
   </td>
   <td>
    ○
   </td>
   <td>
    ○
   </td>
   <td>
    ○
   </td>
   <td>
    ○
   </td>
   <td>
    ○
   </td>
   <td>
    ○
   </td>
  </tr>
  <tr>
   <td>
    50
   </td>
   <td>
    ―
   </td>
   <td>
    ○
   </td>
   <td>
    ○
   </td>
   <td>
    ○
   </td>
   <td>
    ○
   </td>
   <td>
    ○
   </td>
  </tr>
  <tr>
   <td>
    100
   </td>
   <td>
    ―
   </td>
   <td>
    ―
   </td>
   <td>
    ○
   </td>
   <td>
    ○
   </td>
   <td>
    ○
   </td>
   <td>
    ○
   </td>
  </tr>
  <tr>
   <td>
    200
   </td>
   <td>
    ―
   </td>
   <td>
    ―
   </td>
   <td>
    ―
   </td>
   <td>
    ―
   </td>
   <td>
    ○
   </td>
   <td>
    ○
   </td>
  </tr>
 </tbody>
</table>
空気過剩率 $n=1,1.2,1.5,2,3,5,10, \infty$

<table><caption>表2</caption>
 <thead>
  <tr>
   <th colspan="9">
    成分気体のエンタルピ $I^{(0^{\circ} K)}$ (kcal/kmol)
   </th>
  </tr>
  <tr>
   <th>
    $T$ $^\circ$K
   </th>
   <th>
    $\text{CO}_{2}{}^{(4)\ (5)}$
   </th>
   <th>
    $\text{H}_{2}\text{O}^{(6)\ (7)}$
   </th>
   <th>
    $\text{O}_{2}{}^{(9)\ (10)}$
   </th>
   <th>
    $\text{CO}^{(8)}$
   </th>
   <th>
    $\text{H}_{2}{}^{(8)\ (11)}$
   </th>
   <th>
    $\text{OH}^{(12)}$
   </th>
   <th>
    $\text{N}_{2}{}^{(8)}$
   </th>
   <th>
    $\text{Ar}^{(4)}$
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>
    2 000
   </td>
   <td>
    24 159
   </td>
   <td>
    19 620.0
   </td>
   <td>
    16 222.2
   </td>
   <td>
    15 639.2
   </td>
   <td>
    14 674.6
   </td>
   <td>
    14 962.5
   </td>
   <td>
    15 502.1
   </td>
   <td>
    9 932.5
   </td>
  </tr>
  <tr>
   <td>
    2 250
   </td>
   <td>
    *27 809
   </td>
   <td>
    22 702.5
   </td>
   <td>
    *18 496.2
   </td>
   <td>
    *17 816.4
   </td>
   <td>
    *16 743
   </td>
   <td>
    *17 061
   </td>
   <td>
    *17 663.4
   </td>
   <td>
    11 174.1
   </td>
  </tr>
  <tr>
   <td>
    2 500
   </td>
   <td>
    31 500
   </td>
   <td>
    25 825.0
   </td>
   <td>
    20 804
   </td>
   <td>
    20 010.2
   </td>
   <td>
    18 856
   </td>
   <td>
    19 199
   </td>
   <td>
    19 842.4
   </td>
   <td>
    12 415.6
   </td>
  </tr>
  <tr>
   <td>
    2 750
   </td>
   <td>
    *35 223
   </td>
   <td>
    29 040.0
   </td>
   <td>
    *23 141
   </td>
   <td>
    *22 217.6
   </td>
   <td>
    *21 006
   </td>
   <td>
    *21 369
   </td>
   <td>
    *22 037.9
   </td>
   <td>
    13 657.2
   </td>
  </tr>
  <tr>
   <td>
    3 000
   </td>
   <td>
    38 970
   </td>
   <td>
    32 280.0
   </td>
   <td>
    25 506
   </td>
   <td>
    24 437.5
   </td>
   <td>
    23 192
   </td>
   <td>
    23 566
   </td>
   <td>
    24 248.6
   </td>
   <td>
    14 898.8
   </td>
  </tr>
  <tr>
   <td>
    3 500
   </td>
   <td>
    46 540
   </td>
   <td>
    **38 860.0
   </td>
   <td>
    *30 316
   </td>
   <td>
    28 902.9
   </td>
   <td>
    27 606
   </td>
   <td>
    *28 037
   </td>
   <td>
    28 698.9
   </td>
   <td>
    17 381.9
   </td>
  </tr>
  <tr>
   <th colspan="9">
    成分気体のエントロピ $S^{(0^{\circ} K)}$ ($p=1.0332$ kg/cm², kcal/kmol°K)
   </th>
  </tr>
  <tr>
   <th>
    $T$ $^\circ$K
   </th>
   <th>
    $\text{CO}_{2}{}^{(4)\ (5)}$
   </th>
   <th>
    $\text{H}_{2}\text{O}^{(6)\ (7)}$
   </th>
   <th>
    $\text{O}_{2}{}^{(9)\ (10)}$
   </th>
   <th>
    $\text{CO}^{(8)}$
   </th>
   <th>
    $\text{H}_{2}{}^{(8)\ (11)}$
   </th>
   <th>
    $\text{OH}^{(12)}$
   </th>
   <th>
    $\text{N}_{2}{}^{(8)}$
   </th>
   <th>
    $\text{Ar}^{(4)}$
   </th>
  </tr>
  <tr>
   <td>
    2 000
   </td>
   <td>
    74.008
   </td>
   <td>
    63.13
   </td>
   <td>
    64.234
   </td>
   <td>
    61.915
   </td>
   <td>
    45.026
   </td>
   <td>
    57.915
   </td>
   <td>
    60.249
   </td>
   <td>
    46.436
   </td>
  </tr>
  <tr>
   <td>
    2 250
   </td>
   <td>
    *75.723
   </td>
   <td>
    64.58
   </td>
   <td>
    *65.305
   </td>
   <td>
    *62.942
   </td>
   <td>
    *46.001
   </td>
   <td>
    *58.904
   </td>
   <td>
    *61.269
   </td>
   <td>
    47.021
   </td>
  </tr>
  <tr>
   <td>
    2 500
   </td>
   <td>
    77.288
   </td>
   <td>
    65.90
   </td>
   <td>
    66.273
   </td>
   <td>
    63.865
   </td>
   <td>
    46.891
   </td>
   <td>
    59.803
   </td>
   <td>
    62.184
   </td>
   <td>
    47.544
   </td>
  </tr>
  <tr>
   <td>
    2 750
   </td>
   <td>
    *78.758
   </td>
   <td>
    67.12
   </td>
   <td>
    *67.161
   </td>
   <td>
    *64.704
   </td>
   <td>
    *47.711
   </td>
   <td>
    *60.628
   </td>
   <td>
    *63.017
   </td>
   <td>
    48.017
   </td>
  </tr>
  <tr>
   <td>
    3 000
   </td>
   <td>
    80.188
   </td>
   <td>
    68.25
   </td>
   <td>
    67.991
   </td>
   <td>
    65.480
   </td>
   <td>
    48.471
   </td>
   <td>
    61.396
   </td>
   <td>
    63.792
   </td>
   <td>
    48.450
   </td>
  </tr>
  <tr>
   <td>
    3 500
   </td>
   <td>
    82.368
   </td>
   <td>
    **70.27
   </td>
   <td>
    *69.48
   </td>
   <td>
    66.856
   </td>
   <td>
    49.841
   </td>
   <td>
    *62.77
   </td>
   <td>
    65.163
   </td>
   <td>
    49.215
   </td>
  </tr>
 </tbody>
</table>
右肩( )内の数字は文献番号を示す.

<table><caption>表3 化学エネルギ(kcal/kmol)</caption>
 <thead>
  <tr>
   <th>
   </th>
   <th>
    Kassel (4)
   </th>
   <th>
    Zeise (16)
   </th>
   <th>
    Wagman (13)
   </th>
   <th>
    Dwyer (18)
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>
    $W_{p\text{CO}_{2}}$ (0)
   </td>
   <td>
    66 756.5$\pm$30*
   </td>
   <td>
   </td>
   <td>
    66 767
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    $W_{p\text{H}_{2}\text{O}}$ (0)
   </td>
   <td>
   </td>
   <td>
    57 110$\pm$10*
   </td>
   <td>
    57 104
   </td>
   <td>
    57 100
   </td>
  </tr>
  <tr>
   <td>
    $W_{p\text{H}_{2}\text{O}^{\prime}}$ (0)
   </td>
   <td>
   </td>
   <td>
    63 000$\pm$1 000
   </td>
   <td>
   </td>
   <td>
    66 900$\pm$650*
   </td>
  </tr>
  <tr>
   <td>
    $W_{p\text{OH}^{\prime}}$ (0)
   </td>
   <td>
   </td>
   <td>
    68 900
   </td>
   <td>
   </td>
   <td>
    76 700$\pm$1 300*
   </td>
  </tr>
 </tbody>
</table>
*印は本論文で使用した数値

NII-Electronic Library Service

2362
田中敬吉,石田德保,出原 清
日本機械学会論文集(第2部)

$$h_{8}=1+\left(a_{\mathrm{H}_{2}} / 2\right)\left(h_{6}-h_{4}\right)$$

$$h_{7}=\frac{h_{2}+h_{3}}{1+h_{2}\left\{\left(K_{p w} / \beta_{k}\right)+1\right\}}$$

$$h_{6}=\frac{h_{1}}{1+h_{2}\left\{\left(K_{p w} / \beta_{k}\right)+1\right\}}$$

$$h_{5}=\frac{1-h_{3}\left\{\left(K_{p w} / \beta_{k}\right)+1\right\}}{1+h_{2}\left\{\left(K_{p w} / \beta_{k}\right)+1\right\}}$$

$$h_{4}=-\frac{h_{1}\left\{\left(K_{p w} / \beta_{k}\right)+1\right\}}{1+h_{2}\left\{\left(K_{p w} / \beta_{k}\right)+1\right\}}$$

$$h_{3}=-\frac{\alpha_{k}}{a_{\mathrm{H}_{2}}}+h_{2}+\frac{\beta_{k}^{2}+\frac{K_{p \mathrm{CO}_{2}}}{p} \frac{M_{\mathrm{C}}}{M_{\mathrm{N}_{2}}}\left(\frac{\mathrm{N}}{\mathrm{C}}\right)_{\text {fuel }}}{\frac{1}{2} a_{\mathrm{H}_{2}}\left(\beta_{k}^{2}-\frac{K_{p \mathrm{CO}_{2}}}{p}\right)}$$

$$h_{2}=\frac{\beta_{k}^{2}+\left(K_{p \mathrm{CO}_{2}} / p\right)}{\beta_{k}^{2}-\left(K_{p \mathrm{CO}_{2}} / p\right)}$$

$$h_{1}=\frac{\left(K_{p \mathrm{CO}_{2}} / p\right) P_{\mathrm{O} n}-\beta_{k}^{2}}{\left(a_{\mathrm{H}_{2}} / 2\right)\left\{\beta_{k}^{2}-\left(K_{p \mathrm{CO}_{2}} / p\right)\right\}}$$

$$\beta_{k}=\frac{\alpha_{k}}{1-\alpha_{k}}$$

$$P_{\mathrm{O} n}=1+\left(\frac{\mathrm{N}_{2}}{\mathrm{O}_{2}}\right)_{\text {air }} \frac{M_{\mathrm{O}_{2}}}{M_{\mathrm{N}_{2}}}+\left(\frac{\mathrm{Ar}}{\mathrm{O}_{2}}\right)_{\text {air }} \frac{M_{\mathrm{O}_{2}}}{M_{\mathrm{Ar}}}$$

![](./images/811638090849320962_1.jpg)

実線が本論文の計算結果である. 図中()の数字は文献番号を示す.
図1 平衡定数の比較

式(12,によって $\alpha_{k}$ と n との関係が得られれば
$$\left.\begin{array}{l}
\alpha_{w}=n\left\{1+\left(a_{\mathrm{H}_{2}} / 2\right)\right\} h_{6}+h_{7} \\
\alpha_{h}=n\left\{1+\left(a_{\mathrm{H}_{2}} / 2\right)\right\} h_{4}+h_{5}
\end{array}\right\} \cdots \cdots \cdots \cdots \cdots(13)$$

n→∞のときの解離度は
$$\lim _{n \to \infty} \alpha_{k}=\frac{\sqrt{\left(K_{p \mathrm{CO}_{2}} / p\right) P_{\mathrm{O} n}}}{1+\sqrt{\left(K_{p \mathrm{CO}_{2}} / n\right) P_{\mathrm{O} n}}} \cdots \cdots \cdots \cdots \cdots(14)$$

$$\lim _{n \to \infty} \alpha_{w}=0, \quad \lim _{n \to \infty} \alpha_{h}=1 \cdots \cdots \cdots \cdots \cdots \cdots(15)$$

式(14)の結果は前報式(18)と同じ形であるが,誘導の過程がやや複雑であるので式(15)とあわせて論文末尾の付録で説明する.
2·4 平衡定数の計算式 平衡定数の数値についての文献は, 後述するように数多く見受けられる. 平衡定数の値は, それを算出する元になる値すなわち化学エネルギー $(0^{\circ} K$ に打ける定圧反応熱) と成分気体の状態量の値のとり方によって差がでてくる. われわれは諸文献に示された平衡定数をそのまま使用することを差しひかえ, 次式によって平衡定数を計算し, その結果を諸文献の値と比較し妥当性を検討する方式をとった.
$$\left.\begin{array}{c}
\ln K_{\mathrm{co}_{2}}(T)=\frac{2}{R T}\left\{G_{\mathrm{co}_{2}}{ }^{\circ \mathrm{K}}(T, 1)\right. \\
\left.-G_{\mathrm{co}}{ }^{\circ \mathrm{K}}(T, 1)-\frac{1}{2} G_{\mathrm{o}_{2}}{ }^{\circ \mathrm{K}}(T, 1)-W_{\mathrm{co}_{2}}(0)\right\} \\
\ln K_{\mathrm{h}_{2} \mathrm{o}}(T)=\frac{2}{R T}\left\{G_{\mathrm{h}_{2} \mathrm{o}}{ }^{\circ \mathrm{K}}(T, 1)\right. \\
\left.-G_{\mathrm{h}_{2}}{ }^{\circ \mathrm{K}}(T, 1)-\frac{1}{2} G_{\mathrm{o}_{2}}{ }^{\circ \mathrm{K}}(T, 1)-W_{\mathrm{h}_{2} \mathrm{o}}(0)\right\} \\
\ln K_{\mathrm{pH}}(T)=\frac{2}{R T}\left\{G_{\mathrm{OH}}{ }^{\circ \mathrm{K}}(T, 1)-\frac{1}{2}\right. \\
\left.\left.X_{\mathrm{H}_{2}}{ }^{\circ \mathrm{K}}(T, 1)-\frac{1}{2} G_{\mathrm{o}_{2}}{ }^{\circ \mathrm{K}}(T, 1)-W_{\mathrm{pH}}(0)\right\}\right] \\
\ln K_{\mathrm{pw}}(T)=\frac{1}{2} \ln \frac{K_{\mathrm{pco}_{2}}(T)}{K_{\mathrm{p}_{2} \mathrm{o}}(T)} \\
W_{\mathrm{pH}}(0)=W_{\mathrm{p}_{2} \mathrm{o}}(0)-W_{\mathrm{p}_{2}}$$

ここに, R: 普遍ガス定数 $kcal / kmol^{\circ} K, G_{x}^{0^{\circ} K}(T$ ,1): $T^{\circ} K, 1 kg / cm^{2}$ に打ける成分気体の自由エンタルピで肩符は基準温度を示す. $kcal / kmol . W_{p}(0)$ :式(1), (3)の反応系の化学エネルギーkcal/kmol.

表4平衡定数
<table><thead><tr><td><b>$T^{\circ }K$</b></td><td><b>$K_{pCO_{2}}(T)$</b></td><td><b>$K_{pw}(T)$</b></td><td><b>$K_{pOH}(T)$</b></td></tr></thead><tbody><tr><td><b>2 000</b></td><td><b>$1.867×10^{-6}$</b></td><td><b>4.595</b></td><td><b>3.986</b></td></tr><tr><td><b>2 250</b></td><td><b>$7.255×10^{-5}$</b></td><td><b>5.430</b></td><td><b>2.368</b></td></tr><tr><td><b>2 500</b></td><td><b>$1.431×10^{-3}$</b></td><td><b>6.088</b></td><td><b>1.571</b></td></tr><tr><td><b>2 750</b></td><td><b>$1.418×10^{-2}$</b></td><td><b>6.650</b></td><td><b>1.123</b></td></tr><tr><td><b>3 000</b></td><td><b>$1.143×10^{-1}$</b></td><td><b>7.090</b></td><td><b>1.123</b></td></tr><tr><td><b>3 500</b></td><td><b>2.385</b></td><td><b>7.420</b></td><td><b>$8.522×10^{-1}$ $6.477×10^{-1}$</b></td></tr></tbody></table>

NII-Electronic Library Service

### 3. JP-4の燃焼ガスの解離度

3·1 表1に示す温度, 圧力および空気過剰率に対する解離度 $\alpha_{k}(T, p, n), \alpha_{w}(T, p, n), \alpha_{h}(T, p, n)$ を計算した.

3·2 成分気体のエンタルピ,エントロピの値 OHのエンタルピ, エントロピ値はJohnston-Dawsonの値(12)を採用, その他の成分気体については前報と同じ文献の値〔おもに文献 (3) に採用されている〕を採用した. それらの値をまとめて表2に掲げる.

ただし表中の*印, **印の値は引用文献には欠けているのでわれわれが内そうおよび外そうして得た値で

表5 JP-4の燃焼ガスの解離度(その1)

#### $2000^\circ\text{K}$
<table>
  <thead>
    <tr>
      <th colspan="2">
        <div style="transform: rotate(-90deg);">$\alpha$</div>
        <div style="transform: rotate(-90deg);">$p$</div>
        <br>$n$
      </th>
      <th>1</th>
      <th>1.2</th>
      <th>1.5</th>
      <th>2</th>
      <th>3</th>
      <th>5</th>
      <th>10</th>
      <th>$\infty$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="7">$\alpha_k$</td>
      <td>0.05</td>
      <td>$7.548×10^{-2}$</td>
      <td>$3.185×10^{-2}$</td>
      <td>$2.300_5×10^{-2}$</td>
      <td>$1.882×10^{-2}$</td>
      <td>$1.627×10^{-2}$</td>
      <td>$1.480×10^{-2}$</td>
      <td>$1.392×10^{-2}$</td>
      <td>$1.316×10^{-2}$</td>
    </tr>
    <tr>
      <td>0.1</td>
      <td>$6.056×10^{-2}$</td>
      <td>$2.289×10^{-2}$</td>
      <td>$1.640×10^{-2}$</td>
      <td>$1.339×10^{-2}$</td>
      <td>$1.156×10^{-2}$</td>
      <td>$1.051×10^{-2}$</td>
      <td>$9.882×10^{-3}$</td>
      <td>$9.340×10^{-3}$</td>
    </tr>
    <tr>
      <td>0.5</td>
      <td>$3.604×10^{-2}$</td>
      <td>$1.046×10^{-2}$</td>
      <td>$7.417×10^{-3}$</td>
      <td>$6.035×10^{-3}$</td>
      <td>$5.201×10^{-3}$</td>
      <td>$4.728×10^{-3}$</td>
      <td>$4.443×10^{-3}$</td>
      <td>$4.191×10^{-3}$</td>
    </tr>
    <tr>
      <td>1</td>
      <td>$2.875×10^{-2}$</td>
      <td>$7.437×10^{-3}$</td>
      <td>$5.258×10^{-3}$</td>
      <td>$4.275×10^{-3}$</td>
      <td>$3.683×10^{-3}$</td>
      <td>$3.347_5×10^{-3}$</td>
      <td>$3.145×10^{-3}$</td>
      <td>$2.971×10^{-3}$</td>
    </tr>
    <tr>
      <td>5</td>
      <td>$1.695×10^{-2}$</td>
      <td>$3.348×10^{-3}$</td>
      <td>$2.359×10^{-3}$</td>
      <td>$1.916×10^{-3}$</td>
      <td>$1.650×10^{-3}$</td>
      <td>$1.499_5×10^{-3}$</td>
      <td>$1.409×10^{-3}$</td>
      <td>$1.331×10^{-3}$</td>
    </tr>
    <tr>
      <td>10</td>
      <td>$1.348×10^{-2}$</td>
      <td>$2.371×10^{-3}$</td>
      <td>$1.669×10^{-3}$</td>
      <td>$1.355_5×10^{-3}$</td>
      <td>$1.167×10^{-3}$</td>
      <td>$1.061×10^{-3}$</td>
      <td>$9.966×10^{-4}$</td>
      <td>$9.420×10^{-4}$</td>
    </tr>
    <tr>
      <td>20</td>
      <td>$1.072×10^{-2}$</td>
      <td>$1.678×10^{-3}$</td>
      <td>$1.181×10^{-3}$</td>
      <td>$9.588×10^{-4}$</td>
      <td>$8.256×10^{-4}$</td>
      <td>$7.502×10^{-4}$</td>
      <td>$7.049×10^{-4}$</td>
      <td>$6.667×10^{-4}$</td>
    </tr>
    <tr>
      <td rowspan="7">$\alpha_w$</td>
      <td>0.05</td>
      <td>$1.734×10^{-2}$</td>
      <td>$7.025_5×10^{-3}$</td>
      <td>$5.019×10^{-3}$</td>
      <td>$4.076×10^{-3}$</td>
      <td>$3.493×10^{-3}$</td>
      <td>$3.147×10^{-3}$</td>
      <td>$2.910×10^{-3}$</td>
      <td>0</td>
    </tr>
    <tr>
      <td>0.1</td>
      <td>$1.376×10^{-2}$</td>
      <td>$5.622×10^{-3}$</td>
      <td>$3.569×10^{-3}$</td>
      <td>$2.896×10^{-3}$</td>
      <td>$2.483×10^{-3}$</td>
      <td>$2.240×10^{-3}$</td>
      <td>$2.076×10^{-3}$</td>
      <td>0</td>
    </tr>
    <tr>
      <td>0.5</td>
      <td>$8.044×10^{-3}$</td>
      <td>$2.281×10^{-3}$</td>
      <td>$1.609×10^{-3}$</td>
      <td>$1.305×10^{-3}$</td>
      <td>$1.120×10^{-3}$</td>
      <td>$1.012_5×10^{-3}$</td>
      <td>$9.427×10^{-4}$</td>
      <td>0</td>
    </tr>
    <tr>
      <td>1</td>
      <td>$6.384×10^{-3}$</td>
      <td>$1.619×10^{-3}$</td>
      <td>$1.140_5×10^{-3}$</td>
      <td>$9.247×10^{-4}$</td>
      <td>$7.940×10^{-4}$</td>
      <td>$7.184×10^{-4}$</td>
      <td>$6.698×10^{-4}$</td>
      <td>0</td>
    </tr>
    <tr>
      <td>5</td>
      <td>$3.732×10^{-3}$</td>
      <td>$7.277_5×10^{-4}$</td>
      <td>$5.117_5×10^{-4}$</td>
      <td>$4.150×10^{-4}$</td>
      <td>$3.566×10^{-4}$</td>
      <td>$3.231×10^{-4}$</td>
      <td>$3.020×10^{-4}$</td>
      <td>0</td>
    </tr>
    <tr>
      <td>10</td>
      <td>$2.962×10^{-3}$</td>
      <td>$5.152×10^{-4}$</td>
      <td>$3.622×10^{-4}$</td>
      <td>$2.937×10^{-4}$</td>
      <td>$2.525×10^{-4}$</td>
      <td>$2.289×10^{-4}$</td>
      <td>$2.141×10^{-4}$</td>
      <td>0</td>
    </tr>
    <tr>
      <td>20</td>
      <td>$2.351×10^{-3}$</td>
      <td>$3.647×10^{-4}$</td>
      <td>$2.563×10^{-4}$</td>
      <td>$2.079×10^{-4}$</td>
      <td>$1.787_5×10^{-4}$</td>
      <td>$1.621×10^{-4}$</td>
      <td>$1.517×10^{-4}$</td>
      <td>0</td>
    </tr>
    <tr>
      <td rowspan="7">$\alpha_h$</td>
      <td>0.05</td>
      <td>$6.867×10^{-3}$</td>
      <td>$1.179_5×10^{-2}$</td>
      <td>$1.548×10^{-2}$</td>
      <td>$1.966×10^{-2}$</td>
      <td>$2.571×10^{-2}$</td>
      <td>$3.451×10^{-2}$</td>
      <td>$4.978×10^{-2}$</td>
      <td>1</td>
    </tr>
    <tr>
      <td>0.1</td>
      <td>$5.475×10^{-3}$</td>
      <td>$9.900×10^{-3}$</td>
      <td>$1.303×10^{-2}$</td>
      <td>$1.656×10^{-2}$</td>
      <td>$2.167_5×10^{-2}$</td>
      <td>$2.911×10^{-2}$</td>
      <td>$4.205×10^{-2}$</td>
      <td>1</td>
    </tr>
    <tr>
      <td>0.5</td>
      <td>$3.225×10^{-3}$</td>
      <td>$6.607×10^{-3}$</td>
      <td>$8.731×10^{-3}$</td>
      <td>$1.111×10^{-2}$</td>
      <td>$1.456×10^{-2}$</td>
      <td>$1.958×10^{-2}$</td>
      <td>$2.834×10^{-2}$</td>
      <td>1</td>
    </tr>
    <tr>
      <td>1</td>
      <td>$2.565×10^{-3}$</td>
      <td>$5.554×10^{-3}$</td>
      <td>$7.347×10^{-3}$</td>
      <td>$9.352×10^{-3}$</td>
      <td>$1.226×10^{-2}$</td>
      <td>$1.649×10^{-2}$</td>
      <td>$2.389×10^{-2}$</td>
      <td>1</td>
    </tr>
    <tr>
      <td>5</td>
      <td>$1.505×10^{-3}$</td>
      <td>$3.714×10^{-3}$</td>
      <td>$4.920×10^{-3}$</td>
      <td>$6.265×10^{-3}$</td>
      <td>$8.215×10^{-3}$</td>
      <td>$1.106×10^{-2}$</td>
      <td>$1.604×10^{-2}$</td>
      <td>1</td>
    </tr>
    <tr>
      <td>10</td>
      <td>$1.196×10^{-3}$</td>
      <td>$3.124×10^{-3}$</td>
      <td>$4.139×10^{-3}$</td>
      <td>$5.272×10^{-3}$</td>
      <td>$6.913×10^{-3}$</td>
      <td>$9.309×10^{-3}$</td>
      <td>$1.351×10^{-2}$</td>
      <td>1</td>
    </tr>
    <tr>
      <td>20</td>
      <td>$9.497×10^{-4}$</td>
      <td>$2.627×10^{-3}$</td>
      <td>$3.482×10^{-3}$</td>
      <td>$4.435×10^{-3}$</td>
      <td>$5.817×10^{-3}$</td>
      <td>$7.834×10^{-3}$</td>
      <td>$1.137×10^{-2}$</td>
      <td>1</td>
    </tr>
  </tbody>
</table>

#### $2250^\circ\text{K}$
<table>
  <thead>
    <tr>
      <th colspan="2">
        <div style="transform: rotate(-90deg);">$\alpha$</div>
        <div style="transform: rotate(-90deg);">$p$</div>
        <br>$n$
      </th>
      <th>1</th>
      <th>1.2</th>
      <th>1.5</th>
      <th>2</th>
      <th>3</th>
      <th>5</th>
      <th>10</th>
      <th>$\infty$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="7">$\alpha_k$</td>
      <td>0.05</td>
      <td>$2.296×10^{-1}$</td>
      <td>$1.581×10^{-1}$</td>
      <td>$1.251×10^{-1}$</td>
      <td>$1.060×10^{-1}$</td>
      <td>$9.328×10^{-2}$</td>
      <td>$8.567×10^{-2}$</td>
      <td>$8.094×10^{-2}$</td>
      <td>$7.674×10^{-2}$</td>
    </tr>
    <tr>
      <td>0.1</td>
      <td>$1.887×10^{-1}$</td>
      <td>$1.200×10^{-1}$</td>
      <td>$9.260×10^{-2}$</td>
      <td>$7.761×10^{-2}$</td>
      <td>$6.788×10^{-2}$</td>
      <td>$6.215×10^{-2}$</td>
      <td>$5.862×10^{-2}$</td>
      <td>$5.551×10^{-2}$</td>
    </tr>
    <tr>
      <td>0.5</td>
      <td>$1.168×10^{-1}$</td>
      <td>$5.989×10^{-2}$</td>
      <td>$4.420×10^{-2}$</td>
      <td>$3.642×10^{-2}$</td>
      <td>$3.158×10^{-2}$</td>
      <td>$2.879×10^{-2}$</td>
      <td>$2.709×10^{-2}$</td>
      <td>$2.561×10^{-2}$</td>
    </tr>
    <tr>
      <td>1</td>
      <td>$9.430×10^{-2}$</td>
      <td>$4.360×10^{-2}$</td>
      <td>$3.176×10^{-2}$</td>
      <td>$2.605×10^{-2}$</td>
      <td>$2.254×10^{-2}$</td>
      <td>$2.053×10^{-2}$</td>
      <td>$1.930×10^{-2}$</td>
      <td>$1.825×10^{-2}$</td>
    </tr>
    <tr>
      <td>5</td>
      <td>$5.667×10^{-2}$</td>
      <td>$2.032×10^{-2}$</td>
      <td>$1.451×10^{-2}$</td>
      <td>$1.183×10^{-2}$</td>
      <td>$1.021×10^{-2}$</td>
      <td>$9.282×10^{-3}$</td>
      <td>$8.723×10^{-3}$</td>
      <td>$8.244×10^{-3}$</td>
    </tr>
    <tr>
      <td>10</td>
      <td>$4.534×10^{-2}$</td>
      <td>$1.451×10^{-2}$</td>
      <td>$1.031×10^{-2}$</td>
      <td>$8.396×10^{-3}$</td>
      <td>$7.238×10^{-3}$</td>
      <td>$6.580×10^{-3}$</td>
      <td>$6.183×10^{-3}$</td>
      <td>$5.843×10^{-3}$</td>
    </tr>
    <tr>
      <td>20</td>
      <td>$3.621×10^{-2}$</td>
      <td>$1.033×10^{-2}$</td>
      <td>$7.317×10^{-3}$</td>
      <td>$5.951×10^{-3}$</td>
      <td>$5.129×10^{-3}$</td>
      <td>$4.661×10^{-3}$</td>
      <td>$4.380×10^{-3}$</td>
      <td>$4.139×10^{-3}$</td>
    </tr>
    <tr>
      <td></td>
      <td>50</td>
      <td>$2.686×10^{-2}$</td>
      <td>$6.573×10^{-3}$</td>
      <td>$4.641×10^{-3}$</td>
      <td>$3.772×10^{-3}$</td>
      <td>$3.249×10^{-3}$</td>
      <td>$2.953×10^{-3}$</td>
      <td>$2.774×10^{-3}$</td>
      <td>$2.622×10^{-3}$</td>
    </tr>
    <tr>
      <td rowspan="7">$\alpha_w$</td>
      <td>0.05</td>
      <td>$5.066×10^{-2}$</td>
      <td>$3.224×10^{-2}$</td>
      <td>$2.449×10^{-2}$</td>
      <td>$2.015×10^{-2}$</td>
      <td>$1.721×10^{-2}$</td>
      <td>$1.529×10^{-2}$</td>
      <td>$1.372×10^{-2}$</td>
      <td>0</td>
    </tr>
    <tr>
      <td>0.1</td>
      <td>$4.020×10^{-2}$</td>
      <td>$2.376×10^{-2}$</td>
      <td>$1.774×10^{-2}$</td>
      <td>$1.452×10^{-2}$</td>
      <td>$1.240×10^{-2}$</td>
      <td>$1.105×10^{-2}$</td>
      <td>$9.982×10^{-3}$</td>
      <td>0</td>
    </tr>
    <tr>
      <td>0.5</td>
      <td>$2.348×10^{-2}$</td>
      <td>$1.137×10^{-2}$</td>
      <td>$8.226×10^{-3}$</td>
      <td>$6.686×10^{-3}$</td>
      <td>$5.715×10^{-3}$</td>
      <td>$5.119×10^{-3}$</td>
      <td>$4.683×10^{-3}$</td>
      <td>0</td>
    </tr>
    <tr>
      <td>1</td>
      <td>$1.862×10^{-2}$</td>
      <td>$8.188×10^{-3}$</td>
      <td>$5.873×10^{-3}$</td>
      <td>$4.767×10^{-3}$</td>
      <td>$4.077×10^{-3}$</td>
      <td>$3.659×10^{-3}$</td>
      <td>$3.361×10^{-3}$</td>
      <td>0</td>
    </tr>
    <tr>
      <td>5</td>
      <td>$1.088×10^{-2}$</td>
      <td>$3.762×10^{-3}$</td>
      <td>$2.665×10^{-3}$</td>
      <td>$2.159×10^{-3}$</td>
      <td>$1.850×10^{-3}$</td>
      <td>$1.666×10^{-3}$</td>
      <td>$1.542×10^{-3}$</td>
      <td>0</td>
    </tr>
    <tr>
      <td>10</td>
      <td>$8.629×10^{-3}$</td>
      <td>$2.679×10^{-3}$</td>
      <td>$1.892×10^{-3}$</td>
      <td>$1.533×10^{-3}$</td>
      <td>$1.314×10^{-3}$</td>
      <td>$1.185×10^{-3}$</td>
      <td>$1.099×10^{-3}$</td>
      <td>0</td>
    </tr>
    <tr>
      <td>20</td>
      <td>$6.846×10^{-3}$</td>
      <td>$1.904×10^{-3}$</td>
      <td>$1.342×10^{-3}$</td>
      <td>$1.087×10^{-3}$</td>
      <td>$9.321×10^{-4}$</td>
      <td>$8.418×10^{-4}$</td>
      <td>$7.824×10^{-4}$</td>
      <td>0</td>
    </tr>
    <tr>
      <td></td>
      <td>50</td>
      <td>$5.042×10^{-3}$</td>
      <td>$1.209×10^{-3}$</td>
      <td>$8.509×10^{-4}$</td>
      <td>$6.895×10^{-4}$</td>
      <td>$5.917×10^{-4}$</td>
      <td>$5.350×10^{-4}$</td>
      <td>$4.984×10^{-4}$</td>
      <td>0</td>
    </tr>
    <tr>
      <td rowspan="7">$\alpha_h$</td>
      <td>0.05</td>
      <td>$2.618×10^{-2}$</td>
      <td>$3.596×10^{-2}$</td>
      <td>$4.570×10^{-2}$</td>
      <td>$5.733×10^{-2}$</td>
      <td>$7.431×10^{-2}$</td>
      <td>$9.875×10^{-2}$</td>
      <td>$1.402×10^{-1}$</td>
      <td>1</td>
    </tr>
    <tr>
      <td>0.1</td>
      <td>$2.110×10^{-2}$</td>
      <td>$3.003×10^{-2}$</td>
      <td>$3.850×10^{-2}$</td>
      <td>$4.846×10^{-2}$</td>
      <td>$6.298×10^{-2}$</td>
      <td>$8.389×10^{-2}$</td>
      <td>$1.196×10^{-1}$</td>
      <td>1</td>
    </tr>
    <tr>
      <td>0.5</td>
      <td>$1.264×10^{-2}$</td>
      <td>$1.984×10^{-2}$</td>
      <td>$2.583×10^{-2}$</td>
      <td>$3.271×10^{-2}$</td>
      <td>$4.267×10^{-2}$</td>
      <td>$5.708×10^{-2}$</td>
      <td>$8.190×10^{-2}$</td>
      <td>1</td>
    </tr>
    <tr>
      <td>1</td>
      <td>$1.010×10^{-2}$</td>
      <td>$1.663×10^{-2}$</td>
      <td>$2.175×10^{-2}$</td>
      <td>$2.758×10^{-2}$</td>
      <td>$3.603×10^{-2}$</td>
      <td>$4.826×10^{-2}$</td>
      <td>$6.939×10^{-2}$</td>
      <td>1</td>
    </tr>
    <tr>
      <td>5</td>
      <td>$5.973×10^{-3}$</td>
      <td>$1.107×10^{-2}$</td>
      <td>$1.459×10^{-2}$</td>
      <td>$1.854×10^{-2}$</td>
      <td>$2.426×10^{-2}$</td>
      <td>$3.257×10^{-2}$</td>
      <td>$4.701×10^{-2}$</td>
      <td>1</td>
    </tr>
    <tr>
      <td>10</td>
      <td>$4.757×10^{-3}$</td>
      <td>$9.303×10^{-3}$</td>
      <td>$1.228×10^{-2}$</td>
      <td>$1.562×10^{-2}$</td>
      <td>$2.045×10^{-2}$</td>
      <td>$2.747×10^{-2}$</td>
      <td>$3.969×10^{-2}$</td>
      <td>1</td>
    </tr>
    <tr>
      <td>20</td>
      <td>$3.785×10^{-3}$</td>
      <td>$7.820×10^{-3}$</td>
      <td>$1.034×10^{-2}$</td>
      <td>$1.315×10^{-2}$</td>
      <td>$1.722×10^{-2}$</td>
      <td>$2.315×10^{-2}$</td>
      <td>$3.349×10^{-2}$</td>
      <td>1</td>
    </tr>
    <tr>
      <td></td>
      <td>50</td>
      <td>$2.796×10^{-3}$</td>
      <td>$6.218×10^{-3}$</td>
      <td>$8.229×10^{-3}$</td>
      <td>$1.047×10^{-2}$</td>
      <td>$1.372×10^{-2}$</td>
      <td>$1.846×10^{-2}$</td>
      <td>$2.673×10^{-2}$</td>
      <td>1</td>
    </tr>
  </tbody>
</table>

2364
田中敬吉,石田德保,出原 清
日本機械学会論文集(第2部)

ある. これらの値は平衡定数の計算値に敏感に影響するので内そう外そう値を決めるには十分な注意を払った.

$3 \cdot 3$ 平衡定数の計算 表 2 の $I_{x}^{0^{\circ} K}(T), S_{x}^{0^{\circ} K}(T$,1.0332)をもちいて自由エンタルピは
$$G_{x}{ }^{0^{\circ} \mathrm{K}}(T, 1)=I_{x}{ }^{0^{\circ} \mathrm{K}}(T)-T S_{x}{ }^{0^{\circ} \mathrm{K}}(T, 1)$$
で計算し, 式(16)から平衡定数を定める. 化学エネルギの数値も文献によって若干の相違がある. 表3の*印の値を使用した.

平衡定数の計算値を表4に示す. この数値の妥当性

表5(その2)

### 2500°K
<table>
  <thead>
    <tr>
      <th colspan="2" rowspan="2">$\alpha$<br>$n$<br>$p$</th>
      <th>1</th>
      <th>1.2</th>
      <th>1.5</th>
      <th>2</th>
      <th>3</th>
      <th>5</th>
      <th>10</th>
      <th>$\infty$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="8">$\alpha_k$</td>
      <td>0.05</td>
      <td>$4.808×10^{-1}$</td>
      <td>$4.194×10^{-1}$</td>
      <td>$3.738×10^{-1}$</td>
      <td>$3.390×10^{-1}$</td>
      <td>$3.116×10^{-1}$</td>
      <td>$2.933×10^{-1}$</td>
      <td>$2.812×10^{-1}$</td>
      <td>$2.696×10^{-1}$</td>
    </tr>
    <tr>
      <td>0.1</td>
      <td>$4.142×10^{-1}$</td>
      <td>$3.467×10^{-1}$</td>
      <td>$3.007×10^{-1}$</td>
      <td>$2.679×10^{-1}$</td>
      <td>$2.431×10^{-1}$</td>
      <td>$2.271×10^{-1}$</td>
      <td>$2.167×10^{-1}$</td>
      <td>$2.070×10^{-1}$</td>
    </tr>
    <tr>
      <td>0.5</td>
      <td>$2.788×10^{-1}$</td>
      <td>$2.049×10^{-1}$</td>
      <td>$1.662×10^{-1}$</td>
      <td>$1.425×10^{-1}$</td>
      <td>$1.262×10^{-1}$</td>
      <td>$1.1634×10^{-1}$</td>
      <td>$1.101×10^{-1}$</td>
      <td>$1.045×10^{-1}$</td>
    </tr>
    <tr>
      <td>1</td>
      <td>$2.310×10^{-1}$</td>
      <td>$1.580×10^{-1}$</td>
      <td>$1.247×10^{-1}$</td>
      <td>$1.055_{5}×10^{-1}$</td>
      <td>$9.280×10^{-2}$</td>
      <td>$8.519×10^{-2}$</td>
      <td>$8.046×10^{-2}$</td>
      <td>$7.626×10^{-2}$</td>
    </tr>
    <tr>
      <td>5</td>
      <td>$1.450×10^{-1}$</td>
      <td>$8.125×10^{-2}$</td>
      <td>$6.085×10^{-2}$</td>
      <td>$5.040×10^{-2}$</td>
      <td>$4.381×10^{-2}$</td>
      <td>$3.998_{5}×10^{-2}$</td>
      <td>$3.765×10^{-2}$</td>
      <td>$3.560×10^{-2}$</td>
    </tr>
    <tr>
      <td>10</td>
      <td>$1.175×10^{-1}$</td>
      <td>$5.970×10^{-2}$</td>
      <td>$4.398×10^{-2}$</td>
      <td>$3.621×10^{-2}$</td>
      <td>$3.139×10^{-2}$</td>
      <td>$2.860_{5}×10^{-2}$</td>
      <td>$2.691×10^{-2}$</td>
      <td>$2.544×10^{-2}$</td>
    </tr>
    <tr>
      <td>20</td>
      <td>$9.488×10^{-2}$</td>
      <td>$4.344×10^{-2}$</td>
      <td>$3.159×10^{-2}$</td>
      <td>$2.590×10^{-2}$</td>
      <td>$2.240×10^{-2}$</td>
      <td>$2.039_{5}×10^{-2}$</td>
      <td>$1.918×10^{-2}$</td>
      <td>$1.812×10^{-2}$</td>
    </tr>
    <tr>
      <td>50</td>
      <td>$7.112×10^{-2}$</td>
      <td>$2.820_{5}×10^{-2}$</td>
      <td>$2.026×10^{-2}$</td>
      <td>$1.654_{5}×10^{-2}$</td>
      <td>$1.428×10^{-2}$</td>
      <td>$1.299×10^{-2}$</td>
      <td>$1.221×10^{-2}$</td>
      <td>$1.154×10^{-2}$</td>
    </tr>
    <tr>
      <td rowspan="8">$\alpha_w$</td>
      <td>0.05</td>
      <td>$1.225×10^{-1}$</td>
      <td>$9.660×10^{-2}$</td>
      <td>$7.960×10^{-2}$</td>
      <td>$6.737×10^{-2}$</td>
      <td>$5.750×10^{-2}$</td>
      <td>$4.979×10^{-2}$</td>
      <td>$4.214×10^{-2}$</td>
      <td>0</td>
    </tr>
    <tr>
      <td>0.1</td>
      <td>$9.786×10^{-2}$</td>
      <td>$7.416×10^{-2}$</td>
      <td>$5.990×10^{-2}$</td>
      <td>$5.026×10^{-2}$</td>
      <td>$4.284×10^{-2}$</td>
      <td>$3.730×10^{-2}$</td>
      <td>$3.203×10^{-2}$</td>
      <td>0</td>
    </tr>
    <tr>
      <td>0.5</td>
      <td>$5.748×10^{-2}$</td>
      <td>$3.859×10^{-2}$</td>
      <td>$2.972×10^{-2}$</td>
      <td>$2.450×10^{-2}$</td>
      <td>$2.085×10^{-2}$</td>
      <td>$1.835_{5}×10^{-2}$</td>
      <td>$1.620×10^{-2}$</td>
      <td>0</td>
    </tr>
    <tr>
      <td>1</td>
      <td>$4.560_{5}×10^{-2}$</td>
      <td>$2.867×10^{-2}$</td>
      <td>$2.167×10^{-2}$</td>
      <td>$1.776×10^{-2}$</td>
      <td>$1.511×10^{-2}$</td>
      <td>$1.336×10^{-2}$</td>
      <td>$1.190×10^{-2}$</td>
      <td>0</td>
    </tr>
    <tr>
      <td>5</td>
      <td>$2.661×10^{-2}$</td>
      <td>$1.393×10^{-2}$</td>
      <td>$1.016×10^{-2}$</td>
      <td>$8.257×10^{-3}$</td>
      <td>$7.036×10^{-3}$</td>
      <td>$6.268×10^{-3}$</td>
      <td>$5.678×10^{-3}$</td>
      <td>0</td>
    </tr>
    <tr>
      <td>10</td>
      <td>$2.110×10^{-2}$</td>
      <td>$1.008_{5}×10^{-2}$</td>
      <td>$7.276×10^{-3}$</td>
      <td>$5.903×10^{-3}$</td>
      <td>$5.034×10^{-3}$</td>
      <td>$4.498×10^{-3}$</td>
      <td>$4.097×10^{-3}$</td>
      <td>0</td>
    </tr>
    <tr>
      <td>20</td>
      <td>$1.673×10^{-2}$</td>
      <td>$7.262×10^{-3}$</td>
      <td>$5.196×10^{-3}$</td>
      <td>$4.210×10^{-3}$</td>
      <td>$3.594×10^{-3}$</td>
      <td>$3.219×10^{-3}$</td>
      <td>$2.946×10^{-3}$</td>
      <td>0</td>
    </tr>
    <tr>
      <td>50</td>
      <td>$1.231×10^{-2}$</td>
      <td>$4.673×10^{-3}$</td>
      <td>$3.317×10^{-3}$</td>
      <td>$2.616×10^{-3}$</td>
      <td>$2.296×10^{-3}$</td>
      <td>$2.062×10^{-3}$</td>
      <td>$1.897×10^{-3}$</td>
      <td>0</td>
    </tr>
    <tr>
      <td rowspan="8">$\alpha_h$</td>
      <td>0.05</td>
      <td>$7.227×10^{-2}$</td>
      <td>$8.918×10^{-2}$</td>
      <td>$1.085×10^{-1}$</td>
      <td>$1.329×10^{-1}$</td>
      <td>$1.690×10^{-1}$</td>
      <td>$2.199×10^{-1}$</td>
      <td>$3.020×10^{-1}$</td>
      <td>1</td>
    </tr>
    <tr>
      <td>0.1</td>
      <td>$5.962×10^{-2}$</td>
      <td>$7.499×10^{-2}$</td>
      <td>$9.214×10^{-2}$</td>
      <td>$1.136×10^{-1}$</td>
      <td>$1.452×10^{-1}$</td>
      <td>$1.899×10^{-1}$</td>
      <td>$2.631×10^{-1}$</td>
      <td>1</td>
    </tr>
    <tr>
      <td>0.5</td>
      <td>$3.715×10^{-2}$</td>
      <td>$4.955_{5}×10^{-2}$</td>
      <td>$6.237×10^{-2}$</td>
      <td>$7.786×10^{-2}$</td>
      <td>$1.005×10^{-1}$</td>
      <td>$1.328×10^{-1}$</td>
      <td>$1.869×10^{-1}$</td>
      <td>1</td>
    </tr>
    <tr>
      <td>1</td>
      <td>$3.005×10^{-2}$</td>
      <td>$4.138_{5}×10^{-2}$</td>
      <td>$5.260×10^{-2}$</td>
      <td>$6.595×10^{-2}$</td>
      <td>$8.538×10^{-2}$</td>
      <td>$1.132×10^{-1}$</td>
      <td>$1.602×10^{-1}$</td>
      <td>1</td>
    </tr>
    <tr>
      <td>5</td>
      <td>$1.811×10^{-2}$</td>
      <td>$2.730×10^{-2}$</td>
      <td>$3.535×10^{-2}$</td>
      <td>$4.464_{5}×10^{-2}$</td>
      <td>$5.811×10^{-2}$</td>
      <td>$7.751×10^{-2}$</td>
      <td>$1.107×10^{-1}$</td>
      <td>1</td>
    </tr>
    <tr>
      <td>10</td>
      <td>$1.450×10^{-2}$</td>
      <td>$2.286×10^{-2}$</td>
      <td>$2.978×10^{-2}$</td>
      <td>$3.769×10^{-2}$</td>
      <td>$4.913×10^{-2}$</td>
      <td>$6.565_{5}×10^{-2}$</td>
      <td>$9.401×10^{-2}$</td>
      <td>1</td>
    </tr>
    <tr>
      <td>20</td>
      <td>$1.159×10^{-2}$</td>
      <td>$1.917×10^{-2}$</td>
      <td>$2.508×10^{-2}$</td>
      <td>$3.180×10^{-2}$</td>
      <td>$4.150×10^{-2}$</td>
      <td>$5.554×10^{-2}$</td>
      <td>$7.975×10^{-2}$</td>
      <td>1</td>
    </tr>
    <tr>
      <td>50</td>
      <td>$8.602×10^{-3}$</td>
      <td>$1.520_{5}×10^{-2}$</td>
      <td>$1.999×10^{-2}$</td>
      <td>$2.538×10^{-2}$</td>
      <td>$3.317×10^{-2}$</td>
      <td>$4.446×10^{-2}$</td>
      <td>$6.399×10^{-2}$</td>
      <td>1</td>
    </tr>
  </tbody>
</table>

### 2750°K
<table>
  <thead>
    <tr>
      <th colspan="2" rowspan="2">$\alpha$<br>$n$<br>$p$</th>
      <th>1</th>
      <th>1.2</th>
      <th>1.5</th>
      <th>2</th>
      <th>3</th>
      <th>5</th>
      <th>10</th>
      <th>$\infty$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="8">$\alpha_k$</td>
      <td>0.1</td>
      <td>$6.430×10^{-1}$</td>
      <td>$5.988×10^{-1}$</td>
      <td>$5.610×10^{-1}$</td>
      <td>$5.284×10^{-1}$</td>
      <td>$5.000×10^{-1}$</td>
      <td>$4.797×10^{-1}$</td>
      <td>$4.654×10^{-1}$</td>
      <td>$4.511×10^{-1}$</td>
    </tr>
    <tr>
      <td>0.5</td>
      <td>$4.833×10^{-1}$</td>
      <td>$4.204×10^{-1}$</td>
      <td>$3.740×10^{-1}$</td>
      <td>$3.388×10^{-1}$</td>
      <td>$3.111×10^{-1}$</td>
      <td>$2.927×10^{-1}$</td>
      <td>$2.804×10^{-1}$</td>
      <td>$2.687×10^{-1}$</td>
    </tr>
    <tr>
      <td>1</td>
      <td>$4.165×10^{-1}$</td>
      <td>$3.474×10^{-1}$</td>
      <td>$3.008×10^{-1}$</td>
      <td>$2.676×10^{-1}$</td>
      <td>$2.426×10^{-1}$</td>
      <td>$2.265×10^{-1}$</td>
      <td>$2.161×10^{-1}$</td>
      <td>$2.062_{5}×10^{-1}$</td>
    </tr>
    <tr>
      <td>5</td>
      <td>$2.803×10^{-1}$</td>
      <td>$2.051×10^{-1}$</td>
      <td>$1.660×10^{-1}$</td>
      <td>$1.422×10^{-1}$</td>
      <td>$1.259×10^{-1}$</td>
      <td>$1.160×10^{-1}$</td>
      <td>$1.097×10^{-1}$</td>
      <td>$1.041×10^{-1}$</td>
    </tr>
    <tr>
      <td>10</td>
      <td>$2.323×10^{-1}$</td>
      <td>$1.581×10^{-1}$</td>
      <td>$1.245×10^{-1}$</td>
      <td>$1.053×10^{-1}$</td>
      <td>$9.251×10^{-2}$</td>
      <td>$8.489×10^{-2}$</td>
      <td>$8.019×10^{-2}$</td>
      <td>$7.593×10^{-2}$</td>
    </tr>
    <tr>
      <td>20</td>
      <td>$1.909×10^{-1}$</td>
      <td>$1.198×10^{-1}$</td>
      <td>$9.206×10^{-2}$</td>
      <td>$7.701×10^{-2}$</td>
      <td>$6.728×10^{-2}$</td>
      <td>$6.156×10^{-2}$</td>
      <td>$5.803×10^{-2}$</td>
      <td>$5.491×10^{-2}$</td>
    </tr>
    <tr>
      <td>50</td>
      <td>$1.458×10^{-1}$</td>
      <td>$8.117×10^{-2}$</td>
      <td>$6.069×10^{-2}$</td>
      <td>$5.023_{5}×10^{-2}$</td>
      <td>$4.365×10^{-2}$</td>
      <td>$3.983×10^{-2}$</td>
      <td>$3.749×10^{-2}$</td>
      <td>$3.544×10^{-2}$</td>
    </tr>
    <tr>
      <td>100</td>
      <td>$1.182×10^{-1}$</td>
      <td>$5.961×10^{-2}$</td>
      <td>$4.385×10^{-2}$</td>
      <td>$3.609×10^{-2}$</td>
      <td>$3.127×10^{-2}$</td>
      <td>$2.849×10^{-2}$</td>
      <td>$2.680×10^{-2}$</td>
      <td>$2.533×10^{-2}$</td>
    </tr>
    <tr>
      <td rowspan="8">$\alpha_w$</td>
      <td>0.1</td>
      <td>$1.871×10^{-1}$</td>
      <td>$1.566×10^{-1}$</td>
      <td>$1.332×10^{-1}$</td>
      <td>$1.140×10^{-1}$</td>
      <td>$9.651×10^{-2}$</td>
      <td>$8.115×10^{-2}$</td>
      <td>$6.453×10^{-2}$</td>
      <td>0</td>
    </tr>
    <tr>
      <td>0.5</td>
      <td>$1.133×10^{-1}$</td>
      <td>$8.851×10^{-2}$</td>
      <td>$7.241×10^{-2}$</td>
      <td>$6.089×10^{-2}$</td>
      <td>$5.157×10^{-2}$</td>
      <td>$4.423×10^{-2}$</td>
      <td>$3.687×10^{-2}$</td>
      <td>0</td>
    </tr>
    <tr>
      <td>1</td>
      <td>$9.044×10^{-2}$</td>
      <td>$6.788×10^{-2}$</td>
      <td>$5.447×10^{-2}$</td>
      <td>$4.545×10^{-2}$</td>
      <td>$3.849×10^{-2}$</td>
      <td>$3.325×10^{-2}$</td>
      <td>$2.818×10^{-2}$</td>
      <td>0</td>
    </tr>
    <tr>
      <td>5</td>
      <td>$5.303×10^{-2}$</td>
      <td>$3.526×10^{-2}$</td>
      <td>$2.702×10^{-2}$</td>
      <td>$2.219×10^{-2}$</td>
      <td>$1.880×10^{-2}$</td>
      <td>$1.647×10^{-2}$</td>
      <td>$1.440×10^{-2}$</td>
      <td>0</td>
    </tr>
    <tr>
      <td>10</td>
      <td>$4.206×10^{-2}$</td>
      <td>$2.619×10^{-2}$</td>
      <td>$1.970×10^{-2}$</td>
      <td>$1.610×10^{-2}$</td>
      <td>$1.365×10^{-2}$</td>
      <td>$1.201×10^{-2}$</td>
      <td>$1.062×10^{-2}$</td>
      <td>0</td>
    </tr>
    <tr>
      <td>20</td>
      <td>$3.334×10^{-2}$</td>
      <td>$1.928×10^{-2}$</td>
      <td>$1.427×10^{-2}$</td>
      <td>$1.161×10^{-2}$</td>
      <td>$9.857_{5}×10^{-3}$</td>
      <td>$8.712×10^{-3}$</td>
      <td>$7.773_{5}×10^{-3}$</td>
      <td>0</td>
    </tr>
    <tr>
      <td>50</td>
      <td>$2.452×10^{-2}$</td>
      <td>$1.271×10^{-2}$</td>
      <td>$9.240×10^{-3}$</td>
      <td>$7.494×10^{-3}$</td>
      <td>$6.371×10^{-3}$</td>
      <td>$5.659×10^{-3}$</td>
      <td>$5.101×10^{-3}$</td>
      <td>0</td>
    </tr>
    <tr>
      <td>100</td>
      <td>$1.944×10^{-2}$</td>
      <td>$9.199×10^{-3}$</td>
      <td>$6.619_{5}×10^{-3}$</td>
      <td>$5.361×10^{-3}$</td>
      <td>$4.563×10^{-3}$</td>
      <td>$4.066×10^{-3}$</td>
      <td>$3.689×10^{-3}$</td>
      <td>0</td>
    </tr>
    <tr>
      <td rowspan="8">$\alpha_h$</td>
      <td>0.1</td>
      <td>$1.220×10^{-1}$</td>
      <td>$1.458×10^{-1}$</td>
      <td>$1.737×10^{-1}$</td>
      <td>$2.025×10^{-1}$</td>
      <td>$2.618×10^{-1}$</td>
      <td>$3.335×10^{-1}$</td>
      <td>$4.426×10^{-1}$</td>
      <td>1</td>
    </tr>
    <tr>
      <td>0.5</td>
      <td>$8.104×10^{-2}$</td>
      <td>$1.001×10^{-1}$</td>
      <td>$1.217×10^{-1}$</td>
      <td>$1.490×10^{-1}$</td>
      <td>$1.889×10^{-1}$</td>
      <td>$2.448×10^{-1}$</td>
      <td>$3.339×10^{-1}$</td>
      <td>1</td>
    </tr>
    <tr>
      <td>1</td>
      <td>$6.688×10^{-2}$</td>
      <td>$8.421×10^{-2}$</td>
      <td>$1.034×10^{-1}$</td>
      <td>$1.274×10^{-1}$</td>
      <td>$1.625×10^{-1}$</td>
      <td>$2.119×10^{-1}$</td>
      <td>$2.918×10^{-1}$</td>
      <td>1</td>
    </tr>
    <tr>
      <td>5</td>
      <td>$4.170×10^{-2}$</td>
      <td>$5.571×10^{-2}$</td>
      <td>$7.012×10^{-2}$</td>
      <td>$8.749×10^{-2}$</td>
      <td>$1.128×10^{-1}$</td>
      <td>$1.487×10^{-1}$</td>
      <td>$2.084×10^{-1}$</td>
      <td>1</td>
    </tr>
    <tr>
      <td>10</td>
      <td>$3.373×10^{-2}$</td>
      <td>$4.655×10^{-2}$</td>
      <td>$5.917×10^{-2}$</td>
      <td>$7.415×10^{-2}$</td>
      <td>$9.589×10^{-2}$</td>
      <td>$1.269×10^{-1}$</td>
      <td>$1.790×10^{-1}$</td>
      <td>1</td>
    </tr>
    <tr>
      <td>20</td>
      <td>$2.718×10^{-2}$</td>
      <td>$3.891×10^{-2}$</td>
      <td>$4.990×10^{-2}$</td>
      <td>$6.276×10^{-2}$</td>
      <td>$8.139×10^{-2}$</td>
      <td>$1.081×10^{-1}$</td>
      <td>$1.531×10^{-1}$</td>
      <td>1</td>
    </tr>
    <tr>
      <td>50</td>
      <td>$2.034×10^{-2}$</td>
      <td>$3.074×10^{-2}$</td>
      <td>$3.981×10^{-2}$</td>
      <td>$5.026×10^{-2}$</td>
      <td>$6.537×10^{-2}$</td>
      <td>$8.708×10^{-2}$</td>
      <td>$1.240×10^{-1}$</td>
      <td>1</td>
    </tr>
    <tr>
      <td>100</td>
      <td>$1.629×10^{-2}$</td>
      <td>$2.575×10^{-2}$</td>
      <td>$3.355×10^{-2}$</td>
      <td>$4.245×10^{-2}$</td>
      <td>$5.530×10^{-2}$</td>
      <td>$7.382×10^{-2}$</td>
      <td>$1.055×10^{-1}$</td>
      <td>1</td>
    </tr>
  </tbody>
</table>

NII-Electronic Library Service

を確認するために諸文献の値と比較したのが図1である. これからわれわれの計算値は妥当なものと考えられる.

### 3·4 解離度の計算
以上の基礎的数値をもちいて

表5(その3)

#### 3 000°K
<table>
  <thead>
    <tr>
      <th rowspan="2"><span class="math inline">\(\alpha\)</span></th>
      <th rowspan="2"><span class="math inline">\(p\)</span></th>
      <th colspan="8"><span class="math inline">\(n\)</span></th>
    </tr>
    <tr>
      <th>1</th>
      <th>1.2</th>
      <th>1.5</th>
      <th>2</th>
      <th>3</th>
      <th>5</th>
      <th>10</th>
      <th><span class="math inline">\(\infty\)</span></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="10"><span class="math inline">\(\alpha_k\)</span></td>
      <td>0.1</td>
      <td><span class="math inline">\(8.192×10^{-1}\)</span></td>
      <td><span class="math inline">\(7.975×10^{-1}\)</span></td>
      <td><span class="math inline">\(7.768×10^{-1}\)</span></td>
      <td><span class="math inline">\(7.570×10^{-1}\)</span></td>
      <td><span class="math inline">\(7.379×10^{-1}\)</span></td>
      <td><span class="math inline">\(7.231×10^{-1}\)</span></td>
      <td><span class="math inline">\(7.119×10^{-1}\)</span></td>
      <td><span class="math inline">\(7.000×10^{-1}\)</span></td>
    </tr>
    <tr>
      <td>0.5</td>
      <td><span class="math inline">\(6.909×10^{-1}\)</span></td>
      <td><span class="math inline">\(6.518×10^{-1}\)</span></td>
      <td><span class="math inline">\(6.173×10^{-1}\)</span></td>
      <td><span class="math inline">\(5.867×10^{-1}\)</span></td>
      <td><span class="math inline">\(5.594×10^{-1}\)</span></td>
      <td><span class="math inline">\(5.394×10^{-1}\)</span></td>
      <td><span class="math inline">\(5.252×10^{-1}\)</span></td>
      <td><span class="math inline">\(5.106×10^{-1}\)</span></td>
    </tr>
    <tr>
      <td>1</td>
      <td><span class="math inline">\(6.252×10^{-1}\)</span></td>
      <td><span class="math inline">\(5.774×10^{-1}\)</span></td>
      <td><span class="math inline">\(5.373×10^{-1}\)</span></td>
      <td><span class="math inline">\(5.033×10^{-1}\)</span></td>
      <td><span class="math inline">\(4.741×10^{-1}\)</span></td>
      <td><span class="math inline">\(4.534×10^{-1}\)</span></td>
      <td><span class="math inline">\(4.389×10^{-1}\)</span></td>
      <td><span class="math inline">\(4.245×10^{-1}\)</span></td>
    </tr>
    <tr>
      <td>5</td>
      <td><span class="math inline">\(4.650×10^{-1}\)</span></td>
      <td><span class="math inline">\(3.988×10^{-1}\)</span></td>
      <td><span class="math inline">\(3.514_5×10^{-1}\)</span></td>
      <td><span class="math inline">\(3.163×10^{-1}\)</span></td>
      <td><span class="math inline">\(2.890_5×10^{-1}\)</span></td>
      <td><span class="math inline">\(2.711×10^{-1}\)</span></td>
      <td><span class="math inline">\(2.593×10^{-1}\)</span></td>
      <td><span class="math inline">\(2.481_5×10^{-1}\)</span></td>
    </tr>
    <tr>
      <td>10</td>
      <td><span class="math inline">\(3.990×10^{-1}\)</span></td>
      <td><span class="math inline">\(3.272×10^{-1}\)</span></td>
      <td><span class="math inline">\(2.804×10^{-1}\)</span></td>
      <td><span class="math inline">\(2.479×10^{-1}\)</span></td>
      <td><span class="math inline">\(2.238×10^{-1}\)</span></td>
      <td><span class="math inline">\(2.084×10^{-1}\)</span></td>
      <td><span class="math inline">\(1.984×10^{-1}\)</span></td>
      <td><span class="math inline">\(1.891_5×10^{-1}\)</span></td>
    </tr>
    <tr>
      <td>20</td>
      <td><span class="math inline">\(3.378×10^{-1}\)</span></td>
      <td><span class="math inline">\(2.626×10^{-1}\)</span></td>
      <td><span class="math inline">\(2.186×10^{-1}\)</span></td>
      <td><span class="math inline">\(1.900×10^{-1}\)</span></td>
      <td><span class="math inline">\(1.696×10^{-1}\)</span></td>
      <td><span class="math inline">\(1.570×10^{-1}\)</span></td>
      <td><span class="math inline">\(1.490×10^{-1}\)</span></td>
      <td><span class="math inline">\(1.416×10^{-1}\)</span></td>
    </tr>
    <tr>
      <td>50</td>
      <td><span class="math inline">\(2.665×10^{-1}\)</span></td>
      <td><span class="math inline">\(1.902×10^{-1}\)</span></td>
      <td><span class="math inline">\(1.524×10^{-1}\)</span></td>
      <td><span class="math inline">\(1.299×10^{-1}\)</span></td>
      <td><span class="math inline">\(1.146×10^{-1}\)</span></td>
      <td><span class="math inline">\(1.054×10^{-1}\)</span></td>
      <td><span class="math inline">\(9.966×10^{-2}\)</span></td>
      <td><span class="math inline">\(9.447×10^{-2}\)</span></td>
    </tr>
    <tr>
      <td>100</td>
      <td><span class="math inline">\(2.202×10^{-1}\)</span></td>
      <td><span class="math inline">\(1.458×10^{-1}\)</span></td>
      <td><span class="math inline">\(1.137×10^{-1}\)</span></td>
      <td><span class="math inline">\(9.575×10^{-2}\)</span></td>
      <td><span class="math inline">\(8.394×10^{-2}\)</span></td>
      <td><span class="math inline">\(7.692×10^{-2}\)</span></td>
      <td><span class="math inline">\(7.257×10^{-2}\)</span></td>
      <td><span class="math inline">\(6.870×10^{-2}\)</span></td>
    </tr>
    <tr>
      <td>200</td>
      <td><span class="math inline">\(1.806×10^{-1}\)</span></td>
      <td><span class="math inline">\(1.099×10^{-1}\)</span></td>
      <td><span class="math inline">\(8.374×10^{-2}\)</span></td>
      <td><span class="math inline">\(6.981×10^{-2}\)</span></td>
      <td><span class="math inline">\(6.087×10^{-2}\)</span></td>
      <td><span class="math inline">\(5.564×10^{-2}\)</span></td>
      <td><span class="math inline">\(5.242×10^{-2}\)</span></td>
      <td><span class="math inline">\(4.958×10^{-2}\)</span></td>
    </tr>
    <tr>
      <td rowspan="10"><span class="math inline">\(\alpha_w\)</span></td>
      <td>0.1</td>
      <td><span class="math inline">\(3.097×10^{-1}\)</span></td>
      <td><span class="math inline">\(2.716×10^{-1}\)</span></td>
      <td><span class="math inline">\(2.371×10^{-1}\)</span></td>
      <td><span class="math inline">\(2.042×10^{-1}\)</span></td>
      <td><span class="math inline">\(1.695×10^{-1}\)</span></td>
      <td><span class="math inline">\(1.353×10^{-1}\)</span></td>
      <td><span class="math inline">\(9.709×10^{-2}\)</span></td>
      <td>0</td>
    </tr>
    <tr>
      <td>0.5</td>
      <td><span class="math inline">\(2.038×10^{-1}\)</span></td>
      <td><span class="math inline">\(1.717×10^{-1}\)</span></td>
      <td><span class="math inline">\(1.463×10^{-1}\)</span></td>
      <td><span class="math inline">\(1.247×10^{-1}\)</span></td>
      <td><span class="math inline">\(1.044×10^{-1}\)</span></td>
      <td><span class="math inline">\(8.592×10^{-2}\)</span></td>
      <td><span class="math inline">\(6.575×10^{-2}\)</span></td>
      <td>0</td>
    </tr>
    <tr>
      <td>1</td>
      <td><span class="math inline">\(1.661×10^{-1}\)</span></td>
      <td><span class="math inline">\(1.368×10^{-1}\)</span></td>
      <td><span class="math inline">\(1.150×10^{-1}\)</span></td>
      <td><span class="math inline">\(9.745×10^{-2}\)</span></td>
      <td><span class="math inline">\(8.174×10^{-2}\)</span></td>
      <td><span class="math inline">\(6.809×10^{-2}\)</span></td>
      <td><span class="math inline">\(5.347×10^{-2}\)</span></td>
      <td>0</td>
    </tr>
    <tr>
      <td>5</td>
      <td><span class="math inline">\(9.998×10^{-2}\)</span></td>
      <td><span class="math inline">\(7.659×10^{-2}\)</span></td>
      <td><span class="math inline">\(6.193×10^{-2}\)</span></td>
      <td><span class="math inline">\(5.166×10^{-2}\)</span></td>
      <td><span class="math inline">\(4.347×10^{-2}\)</span></td>
      <td><span class="math inline">\(3.705×10^{-2}\)</span></td>
      <td><span class="math inline">\(3.063×10^{-2}\)</span></td>
      <td>0</td>
    </tr>
    <tr>
      <td>10</td>
      <td><span class="math inline">\(7.967×10^{-2}\)</span></td>
      <td><span class="math inline">\(5.854×10^{-2}\)</span></td>
      <td><span class="math inline">\(4.645×10^{-2}\)</span></td>
      <td><span class="math inline">\(3.848×10^{-2}\)</span></td>
      <td><span class="math inline">\(3.241×10^{-2}\)</span></td>
      <td><span class="math inline">\(2.784_5×10^{-2}\)</span></td>
      <td><span class="math inline">\(2.344×10^{-2}\)</span></td>
      <td>0</td>
    </tr>
    <tr>
      <td>20</td>
      <td><span class="math inline">\(6.332×10^{-2}\)</span></td>
      <td><span class="math inline">\(4.430×10^{-2}\)</span></td>
      <td><span class="math inline">\(3.447×10^{-2}\)</span></td>
      <td><span class="math inline">\(2.837×10^{-2}\)</span></td>
      <td><span class="math inline">\(2.392×10^{-2}\)</span></td>
      <td><span class="math inline">\(2.070×10^{-2}\)</span></td>
      <td><span class="math inline">\(1.770_5×10^{-2}\)</span></td>
      <td>0</td>
    </tr>
    <tr>
      <td>50</td>
      <td><span class="math inline">\(4.664×10^{-2}\)</span></td>
      <td><span class="math inline">\(3.020×10^{-2}\)</span></td>
      <td><span class="math inline">\(2.291×10^{-2}\)</span></td>
      <td><span class="math inline">\(1.872×10^{-2}\)</span></td>
      <td><span class="math inline">\(1.581×10^{-2}\)</span></td>
      <td><span class="math inline">\(1.380×10^{-2}\)</span></td>
      <td><span class="math inline">\(1.201×10^{-2}\)</span></td>
      <td>0</td>
    </tr>
    <tr>
      <td>100</td>
      <td><span class="math inline">\(3.697_5×10^{-2}\)</span></td>
      <td><span class="math inline">\(2.236×10^{-2}\)</span></td>
      <td><span class="math inline">\(1.667_5×10^{-2}\)</span></td>
      <td><span class="math inline">\(1.357×10^{-2}\)</span></td>
      <td><span class="math inline">\(1.147×10^{-2}\)</span></td>
      <td><span class="math inline">\(1.007×10^{-2}\)</span></td>
      <td><span class="math inline">\(8.868×10^{-3}\)</span></td>
      <td>0</td>
    </tr>
    <tr>
      <td>200</td>
      <td><span class="math inline">\(2.931×10^{-2}\)</span></td>
      <td><span class="math inline">\(1.642×10^{-2}\)</span></td>
      <td><span class="math inline">\(1.206×10^{-2}\)</span></td>
      <td><span class="math inline">\(9.783×10^{-3}\)</span></td>
      <td><span class="math inline">\(8.285×10^{-3}\)</span></td>
      <td><span class="math inline">\(7.306×10^{-3}\)</span></td>
      <td><span class="math inline">\(6.498×10^{-3}\)</span></td>
      <td>0</td>
    </tr>
    <tr>
      <td rowspan="10"><span class="math inline">\(\alpha_h\)</span></td>
      <td>0.1</td>
      <td><span class="math inline">\(2.057×10^{-1}\)</span></td>
      <td><span class="math inline">\(2.396×10^{-1}\)</span></td>
      <td><span class="math inline">\(2.799×10^{-1}\)</span></td>
      <td><span class="math inline">\(3.310×10^{-1}\)</span></td>
      <td><span class="math inline">\(4.036×10^{-1}\)</span></td>
      <td><span class="math inline">\(4.971×10^{-1}\)</span></td>
      <td><span class="math inline">\(6.243×10^{-1}\)</span></td>
      <td>1</td>
    </tr>
    <tr>
      <td>0.5</td>
      <td><span class="math inline">\(1.499×10^{-1}\)</span></td>
      <td><span class="math inline">\(1.779×10^{-1}\)</span></td>
      <td><span class="math inline">\(2.107×10^{-1}\)</span></td>
      <td><span class="math inline">\(2.525×10^{-1}\)</span></td>
      <td><span class="math inline">\(3.129×10^{-1}\)</span></td>
      <td><span class="math inline">\(3.940×10^{-1}\)</span></td>
      <td><span class="math inline">\(5.128×10^{-1}\)</span></td>
      <td>1</td>
    </tr>
    <tr>
      <td>1</td>
      <td><span class="math inline">\(1.277_5×10^{-1}\)</span></td>
      <td><span class="math inline">\(1.533×10^{-1}\)</span></td>
      <td><span class="math inline">\(1.829×10^{-1}\)</span></td>
      <td><span class="math inline">\(2.206×10^{-1}\)</span></td>
      <td><span class="math inline">\(2.754×10^{-1}\)</span></td>
      <td><span class="math inline">\(3.499×10^{-1}\)</span></td>
      <td><span class="math inline">\(4.620×10^{-1}\)</span></td>
      <td>1</td>
    </tr>
    <tr>
      <td>5</td>
      <td><span class="math inline">\(8.436×10^{-2}\)</span></td>
      <td><span class="math inline">\(1.048×10^{-1}\)</span></td>
      <td><span class="math inline">\(1.278×10^{-1}\)</span></td>
      <td><span class="math inline">\(1.566×10^{-1}\)</span></td>
      <td><span class="math inline">\(1.985×10^{-1}\)</span></td>
      <td><span class="math inline">\(2.568×10^{-1}\)</span></td>
      <td><span class="math inline">\(3.491×10^{-1}\)</span></td>
      <td>1</td>
    </tr>
    <tr>
      <td>10</td>
      <td><span class="math inline">\(6.948×10^{-2}\)</span></td>
      <td><span class="math inline">\(8.815×10^{-2}\)</span></td>
      <td><span class="math inline">\(1.086×10^{-1}\)</span></td>
      <td><span class="math inline">\(1.339×10^{-1}\)</span></td>
      <td><span class="math inline">\(1.707×10^{-1}\)</span></td>
      <td><span class="math inline">\(2.223×10^{-1}\)</span></td>
      <td><span class="math inline">\(3.052×10^{-1}\)</span></td>
      <td>1</td>
    </tr>
    <tr>
      <td>20</td>
      <td><span class="math inline">\(5.683×10^{-2}\)</span></td>
      <td><span class="math inline">\(7.386×10^{-2}\)</span></td>
      <td><span class="math inline">\(9.198×10^{-2}\)</span></td>
      <td><span class="math inline">\(1.140_5×10^{-1}\)</span></td>
      <td><span class="math inline">\(1.140_5×10^{-1}\)</span></td>
      <td><span class="math inline">\(1.914×10^{-1}\)</span></td>
      <td><span class="math inline">\(2.652×10^{-1}\)</span></td>
      <td>1</td>
    </tr>
    <tr>
      <td>50</td>
      <td><span class="math inline">\(4.318×10^{-2}\)</span></td>
      <td><span class="math inline">\(5.832×10^{-2}\)</span></td>
      <td><span class="math inline">\(7.363×10^{-2}\)</span></td>
      <td><span class="math inline">\(9.194×10^{-2}\)</span></td>
      <td><span class="math inline">\(1.185×10^{-1}\)</span></td>
      <td><span class="math inline">\(1.561×10^{-1}\)</span></td>
      <td><span class="math inline">\(2.184×10^{-1}\)</span></td>
      <td>1</td>
    </tr>
    <tr>
      <td>100</td>
      <td><span class="math inline">\(3.490×10^{-2}\)</span></td>
      <td><span class="math inline">\(4.876×10^{-2}\)</span></td>
      <td><span class="math inline">\(6.215×10^{-2}\)</span></td>
      <td><span class="math inline">\(7.794×10^{-2}\)</span></td>
      <td><span class="math inline">\(1.008×10^{-1}\)</span></td>
      <td><span class="math inline">\(1.333×10^{-1}\)</span></td>
      <td><span class="math inline">\(1.877×10^{-1}\)</span></td>
      <td>1</td>
    </tr>
    <tr>
      <td>200</td>
      <td><span class="math inline">\(2.810×10^{-2}\)</span></td>
      <td><span class="math inline">\(4.078×10^{-2}\)</span></td>
      <td><span class="math inline">\(5.243×10^{-2}\)</span></td>
      <td><span class="math inline">\(6.599×10^{-2}\)</span></td>
      <td><span class="math inline">\(8.556×10^{-2}\)</span></td>
      <td><span class="math inline">\(1.135_4×10^{-1}\)</span></td>
      <td><span class="math inline">\(1.606_5×10^{-1}\)</span></td>
      <td>1</td>
    </tr>
  </tbody>
</table>

#### 3 500°K
<table>
  <thead>
    <tr>
      <th rowspan="2"><span class="math inline">\(\alpha\)</span></th>
      <th rowspan="2"><span class="math inline">\(p\)</span></th>
      <th colspan="8"><span class="math inline">\(n\)</span></th>
    </tr>
    <tr>
      <th>1</th>
      <th>1.2</th>
      <th>1.5</th>
      <th>2</th>
      <th>3</th>
      <th>5</th>
      <th>10</th>
      <th><span class="math inline">\(\infty\)</span></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="10"><span class="math inline">\(\alpha_k\)</span></td>
      <td>0.1</td>
      <td><span class="math inline">\(9.502×10^{-1}\)</span></td>
      <td><span class="math inline">\(9.449×10^{-1}\)</span></td>
      <td><span class="math inline">\(9.393×10^{-1}\)</span></td>
      <td><span class="math inline">\(9.336×10^{-1}\)</span></td>
      <td><span class="math inline">\(9.277×10^{-1}\)</span></td>
      <td><span class="math inline">\(9.227×10^{-1}\)</span></td>
      <td><span class="math inline">\(9.186_5×10^{-1}\)</span></td>
      <td><span class="math inline">\(9.142×10^{-1}\)</span></td>
    </tr>
    <tr>
      <td>0.5</td>
      <td><span class="math inline">\(8.989×10^{-1}\)</span></td>
      <td><span class="math inline">\(8.872×10^{-1}\)</span></td>
      <td><span class="math inline">\(8.755×10^{-1}\)</span></td>
      <td><span class="math inline">\(8.637×10^{-1}\)</span></td>
      <td><span class="math inline">\(8.519×10^{-1}\)</span></td>
      <td><span class="math inline">\(8.422_5×10^{-1}\)</span></td>
      <td><span class="math inline">\(8.347_5×10^{-1}\)</span></td>
      <td><span class="math inline">\(8.266×10^{-1}\)</span></td>
    </tr>
    <tr>
      <td>1</td>
      <td><span class="math inline">\(8.657×10^{-1}\)</span></td>
      <td><span class="math inline">\(8.496×10^{-1}\)</span></td>
      <td><span class="math inline">\(8.338×10^{-1}\)</span></td>
      <td><span class="math inline">\(8.183×10^{-1}\)</span></td>
      <td><span class="math inline">\(8.029×10^{-1}\)</span></td>
      <td><span class="math inline">\(7.907×10^{-1}\)</span></td>
      <td><span class="math inline">\(7.813×10^{-1}\)</span></td>
      <td><span class="math inline">\(7.712×10^{-1}\)</span></td>
    </tr>
    <tr>
      <td>5</td>
      <td><span class="math inline">\(7.575×10^{-1}\)</span></td>
      <td><span class="math inline">\(7.264×10^{-1}\)</span></td>
      <td><span class="math inline">\(6.978×10^{-1}\)</span></td>
      <td><span class="math inline">\(6.715×10^{-1}\)</span></td>
      <td><span class="math inline">\(6.471×10^{-1}\)</span></td>
      <td><span class="math inline">\(6.287×10^{-1}\)</span></td>
      <td><span class="math inline">\(6.152×10^{-1}\)</span></td>
      <td><span class="math inline">\(6.011×10^{-1}\)</span></td>
    </tr>
    <tr>
      <td>10</td>
      <td><span class="math inline">\(6.979×10^{-1}\)</span></td>
      <td><span class="math inline">\(6.586×10^{-1}\)</span></td>
      <td><span class="math inline">\(6.238×10^{-1}\)</span></td>
      <td><span class="math inline">\(5.930×10^{-1}\)</span></td>
      <td><span class="math inline">\(5.654×10^{-1}\)</span></td>
      <td><span class="math inline">\(5.452×10^{-1}\)</span></td>
      <td><span class="math inline">\(5.307×10^{-1}\)</span></td>
      <td><span class="math inline">\(5.159×10^{-1}\)</span></td>
    </tr>
    <tr>
      <td>20</td>
      <td><span class="math inline">\(6.325×10^{-1}\)</span></td>
      <td><span class="math inline">\(5.844×10^{-1}\)</span></td>
      <td><span class="math inline">\(5.439×10^{-1}\)</span></td>
      <td><span class="math inline">\(5.096×10^{-1}\)</span></td>
      <td><span class="math inline">\(4.801×10^{-1}\)</span></td>
      <td><span class="math inline">\(4.591×10^{-1}\)</span></td>
      <td><span class="math inline">\(4.444×10^{-1}\)</span></td>
      <td><span class="math inline">\(4.297×10^{-1}\)</span></td>
    </tr>
    <tr>
      <td>50</td>
      <td><span class="math inline">\(5.412×10^{-1}\)</span></td>
      <td><span class="math inline">\(4.818×10^{-1}\)</span></td>
      <td><span class="math inline">\(4.357×10^{-1}\)</span></td>
      <td><span class="math inline">\(3.993×10^{-1}\)</span></td>
      <td><span class="math inline">\(3.697_5×10^{-1}\)</span></td>
      <td><span class="math inline">\(3.496×10^{-1}\)</span></td>
      <td><span class="math inline">\(3.360×10^{-1}\)</span></td>
      <td><span class="math inline">\(3.228×10^{-1}\)</span></td>
    </tr>
    <tr>
      <td>100</td>
      <td><span class="math inline">\(4.720×10^{-1}\)</span></td>
      <td><span class="math inline">\(4.051_5×10^{-1}\)</span></td>
      <td><span class="math inline">\(3.572×10^{-1}\)</span></td>
      <td><span class="math inline">\(3.215×10^{-1}\)</span></td>
      <td><span class="math inline">\(2.938_5×10^{-1}\)</span></td>
      <td><span class="math inline">\(2.756×10^{-1}\)</span></td>
      <td><span class="math inline">\(2.636×10^{-1}\)</span></td>
      <td><span class="math inline">\(2.520_5×10^{-1}\)</span></td>
    </tr>
    <tr>
      <td>200</td>
      <td><span class="math inline">\(4.055×10^{-1}\)</span></td>
      <td><span class="math inline">\(3.329×10^{-1}\)</span></td>
      <td><span class="math inline">\(2.854×10^{-1}\)</span></td>
      <td><span class="math inline">\(2.523_5×10^{-1}\)</span></td>
      <td><span class="math inline">\(2.278×10^{-1}\)</span></td>
      <td><span class="math inline">\(2.121×10^{-1}\)</span></td>
      <td><span class="math inline">\(2.020×10^{-1}\)</span></td>
      <td><span class="math inline">\(1.924×10^{-1}\)</span></td>
    </tr>
    <tr>
      <td rowspan="10"><span class="math inline">\(\alpha_w\)</span></td>
      <td>0.1</td>
      <td><span class="math inline">\(4.865×10^{-1}\)</span></td>
      <td><span class="math inline">\(4.388_5×10^{-1}\)</span></td>
      <td><span class="math inline">\(3.881×10^{-1}\)</span></td>
      <td><span class="math inline">\(3.317×10^{-1}\)</span></td>
      <td><span class="math inline">\(2.643×10^{-1}\)</span></td>
      <td><span class="math inline">\(1.942×10^{-1}\)</span></td>
      <td><span class="math inline">\(1.208×10^{-1}\)</span></td>
      <td>0</td>
    </tr>
    <tr>
      <td>0.5</td>
      <td><span class="math inline">\(3.933×10^{-1}\)</span></td>
      <td><span class="math inline">\(3.494×10^{-1}\)</span></td>
      <td><span class="math inline">\(3.060×10^{-1}\)</span></td>
      <td><span class="math inline">\(2.612×10^{-1}\)</span></td>
      <td><span class="math inline">\(2.106×10^{-1}\)</span></td>
      <td><span class="math inline">\(1.593×10^{-1}\)</span></td>
      <td><span class="math inline">\(1.043×10^{-1}\)</span></td>
      <td>0</td>
    </tr>
    <tr>
      <td>1</td>
      <td><span class="math inline">\(3.467×10^{-1}\)</span></td>
      <td><span class="math inline">\(3.050×10^{-1}\)</span></td>
      <td><span class="math inline">\(2.656×10^{-1}\)</span></td>
      <td><span class="math inline">\(2.264×10^{-1}\)</span></td>
      <td><span class="math inline">\(1.836_5×10^{-1}\)</span></td>
      <td><span class="math inline">\(1.410_5×10^{-1}\)</span></td>
      <td><span class="math inline">\(9.492×10^{-2}\)</span></td>
      <td>0</td>
    </tr>
    <tr>
      <td>5</td>
      <td><span class="math inline">\(2.389_5×10^{-1}\)</span></td>
      <td><span class="math inline">\(2.036×10^{-1}\)</span></td>
      <td><span class="math inline">\(1.740×10^{-1}\)</span></td>
      <td><span class="math inline">\(1.475×10^{-1}\)</span></td>
      <td><span class="math inline">\(1.213×10^{-1}\)</span></td>
      <td><span class="math inline">\(9.667×10^{-2}\)</span></td>
      <td><span class="math inline">\(6.982×10^{-2}\)</span></td>
      <td>0</td>
    </tr>
    <tr>
      <td>10</td>
      <td><span class="math inline">\(1.977×10^{-1}\)</span></td>
      <td><span class="math inline">\(1.654×10^{-1}\)</span></td>
      <td><span class="math inline">\(1.397_5×10^{-1}\)</span></td>
      <td><span class="math inline">\(1.181×10^{-1}\)</span></td>
      <td><span class="math inline">\(9.755×10^{-2}\)</span></td>
      <td><span class="math inline">\(7.893×10^{-2}\)</span></td>
      <td><span class="math inline">\(5.877×10^{-2}\)</span></td>
      <td>0</td>
    </tr>
    <tr>
      <td>20</td>
      <td><span class="math inline">\(1.613×10^{-1}\)</span></td>
      <td><span class="math inline">\(1.320×10^{-1}\)</span></td>
      <td><span class="math inline">\(1.102×10^{-1}\)</span></td>
      <td><span class="math inline">\(9.263×10^{-2}\)</span></td>
      <td><span class="math inline">\(7.684_5×10^{-2}\)</span></td>
      <td><span class="math inline">\(6.305_5×10^{-2}\)</span></td>
      <td><span class="math inline">\(4.832×10^{-2}\)</span></td>
      <td>0</td>
    </tr>
    <tr>
      <td>50</td>
      <td><span class="math inline">\(1.215×10^{-1}\)</span></td>
      <td><span class="math inline">\(9.585×10^{-2}\)</span></td>
      <td><span class="math inline">\(7.843×10^{-2}\)</span></td>
      <td><span class="math inline">\(6.547×10^{-2}\)</span></td>
      <td><span class="math inline">\(5.453_5×10^{-2}\)</span></td>
      <td><span class="math inline">\(4.549×10^{-2}\)</span></td>
      <td><span class="math inline">\(3.609_5×10^{-2}\)</span></td>
      <td>0</td>
    </tr>
    <tr>
      <td>100</td>
      <td><span class="math inline">\(9.731×10^{-2}\)</span></td>
      <td><span class="math inline">\(7.417×10^{-2}\)</span></td>
      <td><span class="math inline">\(5.967×10^{-2}\)</span></td>
      <td><span class="math inline">\(4.950×10^{-2}\)</span></td>
      <td><span class="math inline">\(4.133_5×10^{-2}\)</span></td>
      <td><span class="math inline">\(3.486×10^{-2}\)</span></td>
      <td><span class="math inline">\(2.831×10^{-2}\)</span></td>
      <td>0</td>
    </tr>
    <tr>
      <td>200</td>
      <td><span class="math inline">\(7.758×10^{-2}\)</span></td>
      <td><span class="math inline">\(5.676×10^{-2}\)</span></td>
      <td><span class="math inline">\(4.484_5×10^{-2}\)</span></td>
      <td><span class="math inline">\(3.697×10^{-2}\)</span></td>
      <td><span class="math inline">\(3.093_5×10^{-2}\)</span></td>
      <td><span class="math inline">\(2.634×10^{-2}\)</span></td>
      <td><span class="math inline">\(2.184×10^{-2}\)</span></td>
      <td>0</td>
    </tr>
    <tr>
      <td rowspan="10"><span class="math inline">\(\alpha_h\)</span></td>
      <td>0.1</td>
      <td><span class="math inline">\(3.245×10^{-1}\)</span></td>
      <td><span class="math inline">\(3.711×10^{-1}\)</span></td>
      <td><span class="math inline">\(4.258_5×10^{-1}\)</span></td>
      <td><span class="math inline">\(4.933×10^{-1}\)</span></td>
      <td><span class="math inline">\(5.828×10^{-1}\)</span></td>
      <td><span class="math inline">\(6.850×10^{-1}\)</span></td>
      <td><span class="math inline">\(7.998×10^{-1}\)</span></td>
      <td>1</td>
    </tr>
    <tr>
      <td>0.5</td>
      <td><span class="math inline">\(2.786×10^{-1}\)</span></td>
      <td><span class="math inline">\(3.210×10^{-1}\)</span></td>
      <td><span class="math inline">\(3.709×10^{-1}\)</span></td>
      <td><span class="math inline">\(4.330×10^{-1}\)</span></td>
      <td><span class="math inline">\(5.177×10^{-1}\)</span></td>
      <td><span class="math inline">\(6.192_5×10^{-1}\)</span></td>
      <td><span class="math inline">\(7.425×10^{-1}\)</span></td>
      <td>1</td>
    </tr>
    <tr>
      <td>1</td>
      <td><span class="math inline">\(2.543×10^{-1}\)</span></td>
      <td><span class="math inline">\(2.944×10^{-1}\)</span></td>
      <td><span class="math inline">\(3.416×10^{-1}\)</span></td>
      <td><span class="math inline">\(4.005_5×10^{-1}\)</span></td>
      <td><span class="math inline">\(4.819×10^{-1}\)</span></td>
      <td><span class="math inline">\(5.819×10^{-1}\)</span></td>
      <td><span class="math inline">\(7.079×10^{-1}\)</span></td>
      <td>1</td>
    </tr>
    <tr>
      <td>5</td>
      <td><span class="math inline">\(1.933_5×10^{-1}\)</span></td>
      <td><span class="math inline">\(2.273×10^{-1}\)</span></td>
      <td><span class="math inline">\(2.669×10^{-1}\)</span></td>
      <td><span class="math inline">\(3.169_5×10^{-1}\)</span></td>
      <td><span class="math

2366
田中敬吉,石田德保,出原 清
日本機械学会論文集(第2部)
燃料JP-4の燃焼ガスの解離度を式(12), (13)から計算する. 式 (12) の計算では, 始めに $\alpha_{k}$ を与えてそれに対する空気過剰率を求めて線図を描き, 定められた各 n に対する $\alpha_{k}$ の近似值を求め逐次近似により正しい $\alpha_{k}$ の值を得たものである.
計算結果を表5に示す. その一部を線図にして図2に示す.
4.む す び
(1) $CO, H_{2}, OH$ の生成を考虑したときの燃焼ガスの各解離度と空気過剰率, 温度, 圧力との関係を求め, 燃料JP-4について数値計算した.
(2, n=1 では $\alpha_{k}>\alpha_{w}>\alpha_{h}$ であるが, n が 1 より大きくなると $\alpha_{h}>\alpha_{w}$ となり OH の解離を無視することは妥当でない.
(3) 本報の計算結果をもちいてさらにエンタルピ,エントロピの計算を行なう. それについては後報する.
付 録
下符号 $\infty$ は $n \to \infty$ のときの諸量を示すものとし,αko, αwo, αhoを求める. 本文式(11)を書きなおすと
$$
\begin{aligned}
& \left(h_{6 \infty}+\frac{h_{7 \infty}}{a_{\mathrm{O}_{2} \infty}}\right)\left(h_{8 \infty}+\frac{h_{9 \infty}}{a_{\mathrm{O}_{2} \infty}}\right) \\
& \quad =4 a_{\mathrm{H}_{2}} K_{p \mathrm{OH}}\left(h_{4 \infty}+\frac{h_{5 \infty}}{a_{\mathrm{O}_{2} \infty}}\right)^{2}
\end{aligned}
$$

 $0 \leqq \alpha_{k \infty} \leqq 1$ の範囲において $h_{5 \infty}, h_{7 \infty}, h_{9 \infty}$ はいずれも有限值であるのに対し $a_{O_{2} \infty}=\infty$ であるから上式は
$$h_{6 \infty} h_{8 \infty}-4 a_{\mathrm{H}_{2}} K_{p \mathrm{OH}} h_{4 \infty}=0$$
これをさらに $h_{1 \infty}, h_{2 \infty}$ であらわすと
$$A C / B=0 \quad \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots(17)$$
ただし,
$$A=h_{1 \infty}, \quad B=g_{\infty} h_{2 \infty}+1$$

$$C=1+\left(a_{\mathrm{H}_{2}} / 2\right)(A / B)\left(1+g_{\infty}-8 K_{p \mathrm{OH}} g_{\infty}^{2}\right)$$

$$g_{\infty}=\left(K_{p w} / \beta_{k \infty}\right)-1>0$$

$$\beta_{k \infty}=\alpha_{k \infty} /\left(1-\alpha_{k \infty}\right) \geqq 0$$

式(17)が成立するためには
$$A \neq \pm \infty \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots(18)$$

$$B \neq 0 \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots(18)^{\prime}$$

$$C \neq \pm \infty \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots(18)^{\prime \prime}$$
でなければならない.
式(18)から

![](./images/811638090849320962_2.jpg)

図2

37卷304号(昭46-12)
ジェットエンジンおよびガスタービンの燃焼ガスの状態量に対する新計算法(第3報)

$$\beta_{k}^{2} \neq K_{p \mathrm{CO}_{2}} / p \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots$$

がえられる.また式(18)''に式(18), (18)'を入れると
$$g_{\infty} \neq \infty \quad \text { したがって } \quad \beta_{k \infty} \neq 0 \quad \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots$$

でなければならない.

一方式(13)から
$$\alpha_{w \infty}=\frac{\left\{\left(K_{p \mathrm{CO}_{2}} / p\right) P_{\mathrm{O}_{n}}-\beta_{k \infty}{ }^{2}\right\}+\left(\beta_{k \infty}{ }^{2} / a_{\mathrm{O}_{2} \infty}\right)\left\{\left(a_{\mathrm{H}_{2}} / 2\right)+f_{2 \infty}\right\}}{\left(\beta_{k \infty}{ }^{2} / a_{\mathrm{O}_{2} \infty}\right)\left(1+g_{\infty}\right)\left(a_{\mathrm{H}_{2}} / 2\right)} \quad \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots(21)$$

$$f_{2 \infty}=-\left(\alpha_{k \infty} / 2\right)+\left(a_{\mathrm{H}_{2}} / 2\right)+1$$

上式で, もし $\beta_{k \infty}^{2} a_{O_{2} \infty}$ すなわち $\beta_{k \infty}=\infty$ ならばαw==-∞となり不合理である.

 $0<\beta_{k}<\infty$ でかつ $\alpha_{w \infty} \leqq 1$ なる要求を満たすためには
$$\beta_{k \infty}{ }^{2}=\left(K_{p \mathrm{CO}_{2}} / p\right) P_{\mathrm{O} n} \cdots \cdots \cdots \cdots \cdots \cdots \cdots(22)$$

でなければならない. これよりただちに式(14)が得られる.

つぎに式 (10) $K_{p OH}(T)$ の右辺で $n_{O_{2} \infty}'=\infty$ であるから $K_{p OH}(T)$ が有限值なるためには $\alpha_{w \infty}=0$ でなければならず,これを $K_{p w}(T)$ の右辺に入れると $\alpha_{h \infty}=1$ でなければならない.しかしごく微量でも $H_{2} O$ が存在すれば $\alpha_{h}$ の值は激減する.

文 献
(1) 田中·ほか2名,機論,26-171 (昭35-11),1652.
(2) 田中·ほか2名,機論,28-186 (昭37-2), 304.
(3) Justi, E., Spezifische Wärme, Enthalpie, Dissoziation technischer Gase,(1938),Julius Springer.
(4) Kassel, L.S., J. Amer. Chem. Soc., 58 (1938), 1838.
(5) Gordon, A.R. and Barnes, C., J. Phys. Chem., 36(1932),1143.
(6) Gordon, A.R., J. Chem. Phys., 1 (1933), 308.
(7) Gordon, A.R., J. Chem. Phys., 2 (1934), 65, 549.
(8) Johnston, H.L. and Davis, C.O., J. Amer. Chem. Soc.,56(1934),271,1045.
(9) Johnston, H.L. and Walker, M.K., J. Amer. Chem. Soc.,55(1933),172,5073.
(10) Johnston, H.L. and Walker, M.K., J. Amer. Chem. Soc.,57(1935),682.
(11) Jeppensen, M.A., Phys. Rev., 44 (1933), 165.
(12) Johnston, H.L. and Dawson, D.H., J. Amer. Chem. Soc.,55(1933),2744.
(13) Wagman, D.D., ほか, NBS RP. 1634 (1945).
(14) Lutz, O., Ing.-Arch., 16 (1948), 377.
(15) Huff, W.N., ほか, NACA Rep., 1037 (1951).
(16) Zeise, H., Zeits. f. Electrochemie, 43 (1937), 704.
(17) Zeise, H., Zeits. f. Electrochemie, 48 (1942), 23.
(18) Dwyer, R.J. and Oldenberg, O., J. Chem. Phys.,12(1944),351.
(19) Reichert, H., $R \& M$ , No. 3015 (1950-8).
(20) Beeton, A.B.P., $R \& M$ , No. 2542 (1946-10).
(21) Military Sec., MIL-J-5624E (1960-3-23).

NII-Electronic Library Service

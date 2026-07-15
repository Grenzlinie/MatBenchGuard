import csv
import sys

data = {}
# short SSSS - Table 3
data[('short','SSSS',10,0.0)] = (20.1274, 19.6703, 19.6706)
data[('short','SSSS',10,0.05)] = (22.2861, 21.7800, 21.7803)
data[('short','SSSS',10,0.10)] = (27.2774, 26.6579, 26.6583)
data[('short','SSSS',10,0.15)] = (34.1539, 33.3782, 33.3787)
data[('short','SSSS',20,0.0)] = (5.0318, 5.0028, 5.0029)
data[('short','SSSS',20,0.05)] = (5.5715, 5.5394, 5.5394)
data[('short','SSSS',20,0.10)] = (6.8193, 6.7801, 6.7802)
data[('short','SSSS',20,0.15)] = (8.5385, 8.4893, 8.4894)
data[('short','SSSS',40,0.0)] = (1.2580, 1.2557, 1.2557)
data[('short','SSSS',40,0.05)] = (1.3929, 1.3904, 1.3904)
data[('short','SSSS',40,0.10)] = (1.7048, 1.7017, 1.7017)
data[('short','SSSS',40,0.15)] = (2.1346, 2.1307, 2.1307)
# short CCCC - Table 4
data[('short','CCCC',10,0.0)] = (80.5327, 78.7227, 78.7231)
data[('short','CCCC',10,0.05)] = (89.1711, 87.1460, 87.1464)
data[('short','CCCC',10,0.10)] = (109.1423, 106.6637, 106.6642)
data[('short','CCCC',10,0.15)] = (136.6565, 133.5529, 133.5534)
data[('short','CCCC',20,0.0)] = (20.1317, 20.0158, 20.0160)
data[('short','CCCC',20,0.05)] = (22.2911, 22.1637, 22.1639)
data[('short','CCCC',20,0.10)] = (27.2833, 27.1261, 27.1264)
data[('short','CCCC',20,0.15)] = (34.1617, 33.9649, 33.9652)
data[('short','CCCC',40,0.0)] = (5.0325, 5.0233, 5.0233)
data[('short','CCCC',40,0.05)] = (5.5722, 5.5621, 5.5621)
data[('short','CCCC',40,0.10)] = (6.8198, 6.8075, 6.8075)
data[('short','CCCC',40,0.15)] = (8.5393, 8.5238, 8.5238)
# long SSSS - Table 5
data[('long','SSSS',10,0.0)] = (20.1274, 19.6703, 19.6706)
data[('long','SSSS',10,0.05)] = (76.9098, 75.1632, 75.1639)
data[('long','SSSS',10,0.10)] = (90.6146, 88.5470, 88.5481)
data[('long','SSSS',10,0.15)] = (105.3049, 102.9134, 102.9146)
data[('long','SSSS',20,0.0)] = (5.0318, 5.0028, 5.0029)
data[('long','SSSS',20,0.05)] = (19.2275, 19.1167, 19.1169)
data[('long','SSSS',20,0.10)] = (22.6512, 22.5207, 22.5209)
data[('long','SSSS',20,0.15)] = (26.3262, 26.2746, 26.2748)
data[('long','SSSS',40,0.0)] = (1.2580, 1.2557, 1.2557)
data[('long','SSSS',40,0.05)] = (4.8069, 4.7982, 4.7982)
data[('long','SSSS',40,0.10)] = (5.6628, 5.6525, 5.6525)
data[('long','SSSS',40,0.15)] = (6.5816, 6.5696, 6.5696)
# long CCCC - Table 6
data[('long','CCCC',10,0.0)] = (80.5317, 78.7027, 78.7031)
data[('long','CCCC',10,0.05)] = (307.7315, 300.7428, 300.7439)
data[('long','CCCC',10,0.10)] = (362.5271, 354.2941, 354.2954)
data[('long','CCCC',10,0.15)] = (421.3459, 411.7770, 411.7789)
data[('long','CCCC',20,0.0)] = (20.1317, 20.0158, 20.0160)
data[('long','CCCC',20,0.05)] = (76.9273, 76.4841, 76.4844)
data[('long','CCCC',20,0.10)] = (90.6252, 90.1032, 90.1035)
data[('long','CCCC',20,0.15)] = (105.3284, 104.7217, 104.7221)
data[('long','CCCC',40,0.0)] = (5.0325, 5.0233, 5.0233)
data[('long','CCCC',40,0.05)] = (19.2295, 19.1947, 19.1947)
data[('long','CCCC',40,0.10)] = (22.6534, 22.6224, 22.6224)
data[('long','CCCC',40,0.15)] = (26.32901, 26.2813, 26.2813)

theories = ['CLPT', 'FSDT', 'HSDT']
boundaries = ['SSSS', 'CCCC']
aspects = [10, 20, 40]
volumes = [0.0, 0.05, 0.10, 0.15]
reinf_types = ['short', 'long']

writer = csv.writer(sys.stdout, lineterminator='\n')
writer.writerow(['reinforcement_type', 'plate_theory', 'boundary', 'aspect_ratio', 'CNT_volume_fraction', 'frequency_kHz'])

for rtype in reinf_types:
    for bound in boundaries:
        for ar in aspects:
            for vf in volumes:
                key = (rtype, bound, ar, vf)
                clpt, fsdt, hsdt = data[key]
                writer.writerow([rtype, 'CLPT', bound, ar, vf, clpt])
                writer.writerow([rtype, 'FSDT', bound, ar, vf, fsdt])
                writer.writerow([rtype, 'HSDT', bound, ar, vf, hsdt])

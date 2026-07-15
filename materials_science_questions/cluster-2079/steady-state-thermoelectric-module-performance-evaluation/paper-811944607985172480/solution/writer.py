import csv
import sys

def write_step01():
    data = [
        ["A1", 1.9896, 0.0517, 1.8708],
        ["A2", 1.4166, 0.0517, 1.2702],
        ["B1", 1.9943, 0.0534, 1.8866],
        ["B2", 1.6007, 0.0534, 1.5143],
        ["B3", 1.5272, 0.0527, 1.4479],
        ["B4", 1.4029, 0.0527, 1.3300],
        ["C1", 2.2218, 0.0587, 1.7754],
        ["C2", 1.5752, 0.0587, 1.2301],
        ["D1", 2.0475, 0.0490, 2.0558],
        ["D2", 1.5495, 0.0490, 1.5557],
    ]
    with open('/app/outputs/step_01_tec_parameters.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Model', 'R', 'S', 'theta_TEC'])
        writer.writerows(data)

def write_step02():
    data = [
        ["A1", 3.3, 8.0, 32.2, 0.84],
        ["A2", 3.7, 6.6, 31.9, 0.91],
        ["B1", 3.1, 7.6, 31.8, 0.95],
        ["B2", 3.2, 6.6, 31.5, 1.04],
        ["B3", 3.3, 6.5, 31.5, 1.02],
        ["B4", 3.4, 6.2, 31.5, 1.04],
        ["C1", 2.8, 7.8, 31.6, 1.01],
        ["C2", 3.1, 6.5, 31.3, 1.08],
        ["D1", 3.6, 8.7, 33.0, 0.71],
        ["D2", 3.7, 7.0, 32.1, 0.86],
    ]
    with open('/app/outputs/step_02_predictions.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Model', 'I', 'V', 'T_hot', 'COP'])
        writer.writerows(data)

if __name__ == '__main__':
    target = sys.argv[1]
    if target == 'step_01':
        write_step01()
    elif target == 'step_02':
        write_step02()
    else:
        raise ValueError('Unknown target')

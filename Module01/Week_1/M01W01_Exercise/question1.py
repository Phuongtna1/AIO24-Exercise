import math


def calc_f1_score(tp, fp, fn):
    precision = tp/(tp + fp)
    recall = tp/(tp + fn)
    return 2*(precision*recall)/(precision + recall)


assert math.isclose(round(calc_f1_score(tp=2, fp=3, fn=5), 2),
                    0.33, rel_tol=1e-09, abs_tol=1e-09)
print(round(calc_f1_score(tp=2, fp=4, fn=5), 2))

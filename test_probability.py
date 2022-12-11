from main import Probability
import pytest

lst = []
with open('tests.csv', 'r') as file:
    for line in file.readlines():
        line = line.split(',')
        line = (int(line[0]), int(line[1]), float(line[2].replace('\n', '')))
        lst.append(line)


@pytest.mark.parametrize('sum_, dice_amount, probability', lst)
def test_probability(sum_, dice_amount, probability):
    assert Probability.rolldice_sum_probability(Probability(sum_, dice_amount)) == probability

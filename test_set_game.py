import pytest
from set_game import Card, check_set 

def test_set():
	assert check_set([Card(2,'DIAMOND','STRIPPED','RED'),Card(3,'DIAMOND','OPEN','GREEN'),Card(2,'OVAL','SOLID','PURPLE')]) is True
	assert check_set([Card(1,'DIAMOND','STRIPPED','RED'),Card(2,'DIAMOND','OPEN','RED'),Card(3,'OVAL','OPEN','PURPLE')]) is True
	assert check_set([Card(3,'DIAMOND','OPEN','GREEN'),Card(1,'OVAL','OPEN','GREEN'),Card(2,'OVAL','SOLID','PURPLE')]) is True

	assert check_set([Card(3,'DIAMOND','STRIPPED','GREEN'),Card(3,'DIAMOND','SOLID','RED'),Card(2,'OVAL','STRIPPED','GREEN')]) is False
	assert check_set([Card(1,'SQUIGGLE','SOLID','PURPLE'),Card(3,'SQUIGGLE','OPEN','GREEN'),Card(3,'DIAMOND','OPEN','GREEN')]) is False
	assert check_set([Card(3,'DIAMOND','STRIPPED','RED'),Card(2,'OVAL','OPEN','RED'),Card(2,'OVAL','OPEN','GREEN')]) is False

def test_generate_card():
	with pytest.raises(ValueError):
		Card(3,'CIRCLE','STRIPPED','RED')
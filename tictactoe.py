def validate_board(board):
	if not type(board) is list:
		return False
	VALID_VALUES = [0,1,2]
	plain_board = sum(board,[])
	if len(board) == 3:
		if all(len(i) == 3 for i in board):
			if all(i in VALID_VALUES for i in plain_board):
				if (plain_board.count(1) == plain_board.count(2)) or (plain_board.count(1) - plain_board.count(2) == 1):
					return True
				else:
					return False
			else:
				return False
		else:
			return False
	else:
		return False

def game_finished(board):
	plain_board = sum(board,[])
	triples = []
	for i in range(3):
		triples.append([plain_board[j] for j in range(i,i+7,3)])
	for i in range(0,7,3):
		triples.append([plain_board[j] for j in range(i,i+3)])
	triples.append([plain_board[i] for i in range(0,9,4)])
	triples.append([plain_board[i] for i in range(2,7,2)])
	
	if [1,1,1] in triples:
		return 1 if [2,2,2] not in triples else -1
	elif [2,2,2] in triples:
		return 2 if [1,1,1] not in triples else -1
	elif plain_board.count(0) > 0:
		return 0
	else:
		return -1

def render_board(board):
	for i in range(3):
		for j in range(3):
			board[i][j] = str(board[i][j]).replace('1','X').replace('0','&nbsp;').replace('2','0')
	content = ''
	for i in range(3):
		content += '<tr>'
		rows = ''
		for j in range(3):
			rows += '<td>{}</td>'.format(board[i][j])
		content += rows + '</tr>'
	table = "<table rules='all'>{}</table>".format(content)

	return table

print(render_board([[2,1,0],[2,0,1],[2,1,1]]))
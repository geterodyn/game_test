import unittest
import tictactoe as ttt

class TictactoeTest(unittest.TestCase):
	def test_validate_board(self):
		self.assertTrue(ttt.validate_board([[0,0,0],[0,0,0],[0,0,0]]))
		self.assertTrue(ttt.validate_board([[0,1,2],[2,1,0],[1,1,2]]))
		self.assertTrue(ttt.validate_board([[0,1,1],[2,2,0],[1,1,2]]))
		self.assertTrue(ttt.validate_board([[2,1,1],[2,2,2],[1,1,1]]))
		self.assertTrue(ttt.validate_board([[0,1,2],[0,1,2],[0,1,2]]))
		self.assertTrue(ttt.validate_board([[2,1,0],[2,0,1],[2,1,1]]))
		self.assertTrue(ttt.validate_board([[1,2,0],[1,1,1],[2,0,2]]))
		self.assertTrue(ttt.validate_board([[1,2,0],[2,2,1],[1,2,1]]))
		self.assertTrue(ttt.validate_board([[1,2,1],[2,2,1],[1,1,2]]))
		self.assertTrue(ttt.validate_board([[0,1,0],[1,2,2],[1,2,1]]))

		self.assertFalse(ttt.validate_board([[],[],[]]))
		self.assertFalse(ttt.validate_board([[1,2,0],[0,1,0],[2,2,2],[1,2,3]]))
		self.assertFalse(ttt.validate_board('Iam little string'))
		self.assertFalse(ttt.validate_board([[1,1,1],[2,2,2],[1,1,0]]))
		self.assertFalse(ttt.validate_board([[3,'one',(1,2)],['true',777,2],[1,1,0]]))
		self.assertFalse(ttt.validate_board([[1,1],[2,2,2],[1,1,0]]))

		self.assertIsInstance(ttt.validate_board([[0,1,0],[1,2,2],[1,2,1]]),bool)

		with self.assertRaises(NameError):
			ttt.validate_board([[x,1,1],[2,2],[1,1,0]])
		with self.assertRaises(TypeError):
			ttt.validate_board(['list',[2,2,2],[1,1,0]])

	def test_game_finished(self):
		self.assertFalse(ttt.game_finished([[0,0,0],[0,0,0],[0,0,0]]))	# fust for lulz
		self.assertTrue(ttt.game_finished([[1,1,1],[2,2,0],[0,0,0]]))	# just for fun :)
		self.assertEqual(ttt.game_finished([[0,1,2],[2,1,0],[1,1,2]]),1)
		self.assertIsInstance(ttt.game_finished([[0,1,2],[2,1,0],[1,1,2]]),int)
		self.assertEqual(ttt.game_finished([[0,1,1],[2,2,0],[1,1,2]]),0)
		self.assertEqual(ttt.game_finished([[2,1,1],[2,2,2],[1,1,1]]),-1)
		self.assertEqual(ttt.game_finished([[0,1,2],[0,1,2],[0,1,2]]),-1)
		self.assertEqual(ttt.game_finished([[2,1,0],[2,0,1],[2,1,1]]),2)
		self.assertEqual(ttt.game_finished([[1,2,0],[1,1,1],[2,0,2]]),1)
		self.assertEqual(ttt.game_finished([[1,2,0],[2,2,1],[1,2,1]]),2)
		self.assertEqual(ttt.game_finished([[0,1,0],[1,2,2],[1,2,1]]),0)
		self.assertEqual(ttt.game_finished([[1,2,1],[2,2,1],[1,1,2]]),-1)

	def test_render_board(self):
		self.assertIsInstance(ttt.render_board([[2,1,0],[2,0,1],[2,1,1]]), str)
		self.assertIn('<table', ttt.render_board([[2,1,0],[2,0,1],[2,1,1]]))
		self.assertIn('</table>', ttt.render_board([[2,1,0],[2,0,1],[2,1,1]]))
		self.assertIn('<tr>', ttt.render_board([[2,1,0],[2,0,1],[2,1,1]]))
		self.assertIn('</tr>', ttt.render_board([[2,1,0],[2,0,1],[2,1,1]]))
		self.assertIn('<td>', ttt.render_board([[2,1,0],[2,0,1],[2,1,1]]))
		self.assertIn('</td>', ttt.render_board([[2,1,0],[2,0,1],[2,1,1]]))

if __name__ == '__main__':
	unittest.main()
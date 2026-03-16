"""
ET721 - Spring 2026 - Project 2 Part 2
Student: Soe Kaythi
File: test_connect4_unittest.py
Description: Unit tests for the Connect4 game using Python's unittest framework.
             Focused on testing the switch_player(self) method.
"""

import unittest
from main import Connect4


class TestSwitchPlayer(unittest.TestCase):
    """Unit tests for the switch_player() method."""

    def setUp(self):
        """Create a fresh Connect4 instance before each test."""
        self.game = Connect4()

    # ------------------------------------------------------------------
    # Test 1: Initial player is X
    # ------------------------------------------------------------------
    def test_initial_player_is_x(self):
        """Game always starts with player X before any switch."""
        self.assertEqual(self.game.current_player, 'X')

    # ------------------------------------------------------------------
    # Test 2: X switches to O
    # ------------------------------------------------------------------
    def test_switch_from_x_to_o(self):
        """Calling switch_player() when current player is X changes it to O."""
        self.game.switch_player()
        self.assertEqual(self.game.current_player, 'O')

    # ------------------------------------------------------------------
    # Test 3: O switches to X
    # ------------------------------------------------------------------
    def test_switch_from_o_to_x(self):
        """Calling switch_player() when current player is O changes it to X."""
        self.game.current_player = 'O'
        self.game.switch_player()
        self.assertEqual(self.game.current_player, 'X')

    # ------------------------------------------------------------------
    # Test 4: Double switch returns to original player
    # ------------------------------------------------------------------
    def test_double_switch_returns_to_original(self):
        """Two consecutive switches return to the original player."""
        original = self.game.current_player
        self.game.switch_player()
        self.game.switch_player()
        self.assertEqual(self.game.current_player, original)

    # ------------------------------------------------------------------
    # Test 5: Multiple switches alternate correctly
    # ------------------------------------------------------------------
    def test_multiple_switches_alternate(self):
        """Player alternates correctly across many switches: X->O->X->O->X."""
        expected_sequence = ['O', 'X', 'O', 'X', 'O']
        for expected in expected_sequence:
            self.game.switch_player()
            self.assertEqual(self.game.current_player, expected)

    # ------------------------------------------------------------------
    # Test 6: switch_player does not affect the board
    # ------------------------------------------------------------------
    def test_switch_player_does_not_affect_board(self):
        """Calling switch_player() leaves the board completely unchanged."""
        board_before = [row[:] for row in self.game.board]
        self.game.switch_player()
        self.assertEqual(self.game.board, board_before)

    # ------------------------------------------------------------------
    # Test 7: switch_player only changes current_player, nothing else
    # ------------------------------------------------------------------
    def test_switch_only_changes_current_player(self):
        """switch_player() only modifies current_player, not ROWS or COLS."""
        rows_before = self.game.ROWS
        cols_before = self.game.COLS
        self.game.switch_player()
        self.assertEqual(self.game.ROWS, rows_before)
        self.assertEqual(self.game.COLS, cols_before)

    # ------------------------------------------------------------------
    # Test 8: Switch is consistent after a chip drop
    # ------------------------------------------------------------------
    def test_switch_after_chip_drop(self):
        """switch_player() works correctly after chips have been dropped."""
        self.game.drop_chip(1)          # X drops a chip
        self.game.switch_player()       # now O's turn
        self.assertEqual(self.game.current_player, 'O')
        self.game.drop_chip(2)          # O drops a chip
        self.game.switch_player()       # back to X
        self.assertEqual(self.game.current_player, 'X')


# ===========================================================================
# Entry point
# ===========================================================================
if __name__ == '__main__':
    unittest.main(verbosity=2)


# ---------------------------------------------------------------------------
# DOCUMENTATION / TEST RESULTS
# ---------------------------------------------------------------------------
#
# Test File  : test_connect4_unittest.py
# Framework  : Python unittest
# Student    : Soe Kaythi
# Date       : Spring 2026
# Course     : ET721 - Software Development Practicum
#
# -- Test Class ---------------------------------------------------------------
#
#   TestSwitchPlayer (8 tests)
#     Tests all meaningful behaviors of switch_player():
#       1. test_initial_player_is_x             - verifies game starts with X
#       2. test_switch_from_x_to_o              - X -> O after one switch
#       3. test_switch_from_o_to_x              - O -> X after one switch
#       4. test_double_switch_returns_to_original - two switches = no net change
#       5. test_multiple_switches_alternate     - 5 consecutive switches alternate
#       6. test_switch_player_does_not_affect_board - board is untouched
#       7. test_switch_only_changes_current_player  - ROWS/COLS unchanged
#       8. test_switch_after_chip_drop          - switch works correctly mid-game
#
# -- Results ------------------------------------------------------------------
#
#   All 8 tests PASSED with exit code 0.
#   No bugs were identified in switch_player() during testing.
#
# -- Notes --------------------------------------------------------------------
#
#   * setUp() creates a fresh Connect4 instance before every test so that
#     no test can affect another.
#   * The board snapshot [row[:] for row in board] verifies that
#     switch_player() does not accidentally mutate any game state.
#
# ---------------------------------------------------------------------------

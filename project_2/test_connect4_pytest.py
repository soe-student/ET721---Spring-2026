"""
ET721 - Spring 2026 - Project 2 Part 2
Student: Soe Kaythi
File: test_connect4_pytest.py
Description: Unit tests for the Connect4 game using pytest.
             Focused on testing the play_game(self) method.
"""

import io
import pytest
from unittest.mock import patch

from main import Connect4


# ===========================================================================
# Helper
# ===========================================================================
def run_game(inputs):
    """Run play_game() with mocked input and return captured stdout."""
    captured = io.StringIO()
    with patch('builtins.input', side_effect=inputs), \
         patch('sys.stdout', new=captured):
        Connect4().play_game()
    return captured.getvalue()


# ===========================================================================
# Tests for play_game
# ===========================================================================

class TestPlayGame:
    """pytest tests for the play_game() method."""

    # ------------------------------------------------------------------
    # Test 1: Welcome message is printed at startup
    # ------------------------------------------------------------------
    def test_welcome_message_is_printed(self):
        """play_game() prints 'Welcome to Connect 4!' when it starts."""
        moves = ['1', '5', '2', '5', '3', '5', '4']
        output = run_game(moves)
        assert 'Welcome to Connect 4!' in output

    # ------------------------------------------------------------------
    # Test 2: X wins horizontally
    # ------------------------------------------------------------------
    def test_x_wins_horizontally(self):
        """X wins by placing four chips in columns 1-4 horizontally."""
        # X plays cols 1,2,3,4 / O plays col 5 as filler
        moves = ['1', '5', '2', '5', '3', '5', '4']
        output = run_game(moves)
        assert 'Player X wins!' in output

    # ------------------------------------------------------------------
    # Test 3: O wins vertically (mocked check_win for reliability)
    # ------------------------------------------------------------------
    def test_o_wins_vertically(self):
        """O wins when check_win returns True on O's fourth turn."""
        # check_win is called after every move; we inject the result directly
        # so the test is not affected by X accidentally winning first.
        win_results = [False, False, False, False, False, False, False, True]
        with patch.object(Connect4, 'check_win', side_effect=win_results):
            moves = ['1', '2', '3', '2', '4', '2', '5', '2']
            output = run_game(moves)
        assert 'Player O wins!' in output

    # ------------------------------------------------------------------
    # Test 4: Non-numeric input is handled gracefully
    # ------------------------------------------------------------------
    def test_invalid_text_input_reprompts(self):
        """Non-numeric input triggers the invalid-input message and retries."""
        moves = ['abc', '1', '5', '2', '5', '3', '5', '4']
        output = run_game(moves)
        assert 'Invalid input' in output
        assert 'Player X wins!' in output   # game still finishes correctly

    # ------------------------------------------------------------------
    # Test 5: Full column triggers invalid-move message
    # ------------------------------------------------------------------
    def test_full_column_triggers_invalid_move_message(self):
        """Dropping into a full column prints 'Invalid move!' and retries."""
        # drop_chip returns False on the 7th call to simulate a full column.
        # check_win resolves the game on the 8th valid drop.
        with patch.object(Connect4, 'drop_chip',
                          side_effect=[True, True, True, True, True, True,
                                       False,   # column full -> "Invalid move!"
                                       True, True]):
            with patch.object(Connect4, 'check_win',
                               side_effect=[False, False, False, False,
                                            False, False, False, True]):
                with patch('builtins.input', side_effect=['1'] * 9), \
                     patch('sys.stdout', new=io.StringIO()) as cap:
                    Connect4().play_game()
        assert 'Invalid move' in cap.getvalue()

    # ------------------------------------------------------------------
    # Test 6: Tie is detected when board is full
    # ------------------------------------------------------------------
    def test_tie_detected_when_board_is_full(self):
        """play_game() prints a tie message when the board fills with no winner."""
        with patch.object(Connect4, 'is_full', return_value=True), \
             patch.object(Connect4, 'check_win', return_value=False), \
             patch('builtins.input', return_value='1'), \
             patch('sys.stdout', new=io.StringIO()) as cap:
            Connect4().play_game()
        assert 'tie' in cap.getvalue().lower()

    # ------------------------------------------------------------------
    # Test 7: Board is printed each turn
    # ------------------------------------------------------------------
    def test_board_is_printed_each_turn(self):
        """'Current Board:' appears in output, confirming board prints each turn."""
        moves = ['1', '5', '2', '5', '3', '5', '4']
        output = run_game(moves)
        assert 'Current Board:' in output

    # ------------------------------------------------------------------
    # Test 8: Column number guide is shown each turn
    # ------------------------------------------------------------------
    def test_column_guide_shown(self):
        """The column number guide '1 2 3 4 5 6 7' appears in the output."""
        moves = ['1', '5', '2', '5', '3', '5', '4']
        output = run_game(moves)
        assert '1 2 3 4 5 6 7' in output


# ===========================================================================
# Entry point (allows running with python directly too)
# ===========================================================================
if __name__ == '__main__':
    pytest.main([__file__, '-v'])


# ---------------------------------------------------------------------------
# DOCUMENTATION / TEST RESULTS
# ---------------------------------------------------------------------------
#
# Test File  : test_connect4_pytest.py
# Framework  : pytest
# Student    : Soe Kaythi
# Date       : Spring 2026
# Course     : ET721 - Software Development Practicum
#
# -- Test Class ---------------------------------------------------------------
#
#   TestPlayGame (8 tests)
#     Tests all meaningful behaviors of play_game():
#       1. test_welcome_message_is_printed        - welcome text appears at start
#       2. test_x_wins_horizontally               - X win detected and printed
#       3. test_o_wins_vertically                 - O win detected and printed
#       4. test_invalid_text_input_reprompts      - ValueError handled gracefully
#       5. test_full_column_triggers_invalid_move - full column rejection message
#       6. test_tie_detected_when_board_is_full   - tie message on full board
#       7. test_board_is_printed_each_turn        - board display confirmed
#       8. test_column_guide_shown                - column numbers displayed
#
# -- pytest Features Used -----------------------------------------------------
#
#   patch('builtins.input', side_effect=[...]) - simulates player keyboard input
#   patch('sys.stdout', new=io.StringIO())     - captures printed output
#   patch.object(Connect4, 'check_win', ...)   - controls win detection
#   patch.object(Connect4, 'drop_chip', ...)   - controls chip drop results
#   patch.object(Connect4, 'is_full', ...)     - controls board-full detection
#
# -- Results ------------------------------------------------------------------
#
#   All 8 tests PASSED with exit code 0.
#   No bugs were identified in play_game() during testing.
#
# -- Notes --------------------------------------------------------------------
#
#   * builtins.input is mocked with side_effect lists to drive the game loop
#     without blocking on real keyboard input.
#   * stdout is redirected to io.StringIO() so printed output can be
#     inspected with string assertions.
#   * test_o_wins_vertically and test_full_column_triggers_invalid_move use
#     patch.object to inject exact return values into check_win / drop_chip,
#     making those tests reliable regardless of board state.
#   * test_tie_detected_when_board_is_full patches both is_full and check_win
#     to avoid needing a full 42-move sequence to reach the tie path.
#
# ---------------------------------------------------------------------------
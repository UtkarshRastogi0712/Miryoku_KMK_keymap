print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.split import Split, SplitSide, SplitType
from kmk.modules.holdtap import HoldTap
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()
keyboard.modules.append(HoldTap())
keyboard.modules.append(Layers())
keyboard.debug_enabled = True

split = Split(
    split_side=SplitSide.LEFT,  # Sets if this is to SplitSide.LEFT or SplitSide.RIGHT, or use EE hands
    split_type=SplitType.UART,  # Defaults to UART
    split_target_left=True,  # Assumes that left will be the one on USB. Set to False if it will be the right
    uart_interval=20,  # Sets the uarts delay. Lower numbers draw more power
    data_pin=board.GP16,  # The primary data pin to talk to the secondary device with
    data_pin2=None,  # Second uart pin to allow 2 way communication
    use_pio=True,  # Use RP2040 PIO implementation of UART. Required if you want to use other pins than RX/TX
)

keyboard.modules.append(split)

keyboard.col_pins = (board.GP26, board.GP27, board.GP22, board.GP21, board.GP20)
keyboard.row_pins = (board.GP6, board.GP7, board.GP10, board.GP11)
keyboard.diode_orientation = DiodeOrientation.COL2ROW


keyboard.keymap = [
#base
    [
        KC.Q, KC.W, KC.F, KC.P, KC.B, KC.J, KC.L, KC.U, KC.Y, KC.QUOT,
        KC.A, KC.HT(KC.R, KC.LALT, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.HT(KC.S, KC.LCTRL, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.HT(KC.T, KC.LSHIFT, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.G, KC.M, KC.HT(KC.N, KC.RSHIFT, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.HT(KC.E, KC.RCTRL, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.HT(KC.I, KC.RALT, prefer_hold=True, tap_interrupted=False, tap_time=200), KC.O,
        KC.Z, KC.X, KC.C, KC.D, KC.V, KC.K, KC.H, KC.COMM, KC.DOT, KC.SLSH,
        KC.NO,KC.NO, KC.LT(3, KC.ESC), KC.SPC, KC.LT(2, KC.TAB), KC.LT(1, KC.ENT), KC.BSPC, KC.LT(4, KC.DEL),KC.NO,KC.NO
    ],
#num
    [
        KC.LBRC, KC.N7, KC.N8,  KC.N9, KC.RBRC, KC.NO, KC.NO,     KC.NO,    KC.NO,   KC.NO,
        KC.SCLN, KC.N4, KC.N5,  KC.N6, KC.EQL,  KC.NO, KC.RSHIFT, KC.RCTRL, KC.RALT, KC.NO,
        KC.GRV,  KC.N1, KC.N2,  KC.N3, KC.BSLS, KC.NO, KC.NO,     KC.NO,    KC.NO,   KC.NO,
        KC.NO,   KC.NO, KC.DOT, KC.N0, KC.MINS, KC.NO, KC.NO,     KC.NO,    KC.NO,   KC.NO
    ],
#sym
    [
        KC.NO, KC.NO,   KC.NO,   KC.NO,   KC.NO, KC.LCBR, KC.AMPR, KC.ASTR, KC.LPRN, KC.RPRN,
        KC.NO, KC.LALT, KC.LCTL, KC.LSFT, KC.NO, KC.COLN, KC.DLR,  KC.PERC, KC.CIRC, KC.PLUS,
        KC.NO, KC.NO,   KC.NO,   KC.NO,   KC.NO, KC.TILD, KC.EXLM, KC.AT,   KC.HASH, KC.PIPE,
        KC.NO, KC.NO,   KC.NO,   KC.NO,   KC.NO, KC.LPRN, KC.RPRN, KC.UNDS, KC.NO,   KC.NO
    ],
#nav
    [
        KC.NO, KC.NO,   KC.NO,   KC.NO,   KC.NO, KC.RCTL(KC.Y), KC.RCTL(KC.V), KC.RCTL(KC.C), KC.RCTL(KC.X), KC.RCTL(KC.Z),
        KC.NO, KC.LALT, KC.LCTL, KC.LSFT, KC.NO, KC.CAPS, KC.LEFT, KC.DOWN, KC.UP,   KC.RGHT,
        KC.NO, KC.NO,   KC.NO,   KC.NO,   KC.NO, KC.INS,  KC.HOME, KC.PGDN, KC.PGUP, KC.END,
        KC.NO, KC.NO,   KC.NO,   KC.NO,   KC.NO, KC.ENT,  KC.BSPC, KC.DEL,  KC.NO,   KC.NO
    ],
#fun
    [
        KC.F12, KC.F7, KC.F8,  KC.F9,  KC.PSCR, KC.NO, KC.NO,     KC.NO,    KC.NO,   KC.NO,
        KC.F11, KC.F4, KC.F5,  KC.F6,  KC.SLCK, KC.NO, KC.RSHIFT, KC.RCTRL, KC.RALT, KC.NO,
        KC.F10, KC.F1, KC.F2,  KC.F3,  KC.PAUS, KC.NO, KC.NO,     KC.NO,    KC.NO,   KC.NO,
        KC.NO,  KC.NO, KC.APP, KC.SPC, KC.TAB,  KC.NO, KC.NO,     KC.NO,    KC.NO,   KC.NO
    ]

]

if __name__ == '__main__':
    keyboard.go()

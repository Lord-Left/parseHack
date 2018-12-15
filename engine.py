import libtcodpy as lt

def main():
	screen_width = 80
	screen_height = 50

	lt.console_set_custom_font('arial10x10.png', lt.FONT_TYPE_GREYSCALE | lt.FONT_LAYOUT_TCOD)

	lt.console_init_root(screen_width, screen_height, 'PARSE_HACK 0.0.1', False)
	while not lt.console_is_window_closed():
		lt.console_set_default_foreground(0,lt.white)
		lt.console_put_char(0,1,1,'@',lt.BKGND_NONE)
		lt.console_flush()

		key = lt.console_check_for_keypress()

		if key.vk == lt.KEY_ESCAPE:
			return True

if __name__ == '__main__':
	main()

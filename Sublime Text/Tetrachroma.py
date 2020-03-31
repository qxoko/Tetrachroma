import sublime
import sublime_plugin

class TetrachromaSelectCommand(sublime_plugin.TextCommand):
	def run(self, action):
		settings = sublime.load_settings('Preferences.sublime-settings')

		settings.set('color_scheme', 'Packages/Tetrachroma/Tetrachroma.sublime-color-scheme')
		settings.set('theme', 'Tetrachroma.sublime-theme')

		sublime.save_settings('Preferences.sublime-settings')
		sublime.status_message('Activated Tetrachroma')
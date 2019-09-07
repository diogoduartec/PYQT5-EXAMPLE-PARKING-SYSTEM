import src.assets.Colors as COLORS
import src.assets.styles.general as GENERAL

tool_button = 'QToolButton {border-color: #000; color: white; padding: 5; margin-right: 3;} QToolButton:hover{border: 1px solid ' + COLORS.primary + ';}'
active_tool_button = 'QToolButton {color: white; padding: 5; margin-right: 3;border: 1px solid ' + COLORS.primary + ';}'

toolbar = 'QToolBar {background-color: ' + COLORS.dark2 + ';}'
container = 'QMainWindow {background-color: ' + COLORS.dark3 + '}'
button = GENERAL.button
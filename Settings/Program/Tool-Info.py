from Config.Util import *
from Config.Config import *
Title("Tool Info")
print(f"{color.GREEN}Information Recovery..{reset}")
print(f"""{color.GREEN}
{color.GREEN}Name Tool     :  {color.WHITE}{name_tool}
{color.GREEN}Version       :  {color.WHITE}{version_tool}
{color.GREEN}Coding        :  {color.WHITE}{coding_tool}
{color.GREEN}Language      :  {color.WHITE}{language_tool}
{color.GREEN}Creator       :  {color.WHITE}{creator}
{color.GREEN}Platform      :  {color.WHITE}{platform}
""" + color.GREEN)

Continue()
Reset()
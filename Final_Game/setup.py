from cx_Freeze import setup, Executable

build_exe_options = {
    "include_files": ["apple.gif", "snake-head.gif", "bg2.gif"]
}

setup(
    name="Snake Game",
    version="1.0",
    description="Snake Game with custom graphics",
    options={"build_exe": build_exe_options},
    executables=[Executable("snake-game.py", base="Win32GUI")]
)
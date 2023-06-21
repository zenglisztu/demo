import PythonMagick

img = PythonMagick.Image(r'./matplotlib.png')

img.sample('240x240')

img.write(r'./mplt.ico')
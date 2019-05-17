def get_color(wavelength):
	'''Convert a visible wavelength to an hexadec color string.

	Based on: http://www.efg2.com/Lab/ScienceAndEngineering/Spectra.htm
	Copyright: http://www.efg2.com/Lab/Copyright.htm

	Args:
		wavelength (int): wavelength in nm

	Returns:
		string: color in hexadec format
	'''

	# Set default values
	R = 0
	G = 0
	B = 0
	factor = 0
	gamma = .8
	imax = 255

	# Set colors per interval
	if wavelength >= 380 and wavelength <= 439:
		R = - (wavelength - 440) / (440 - 380.)
		B = 1
	elif wavelength >= 440 and wavelength <= 489:
		G = (wavelength - 440) / (490 - 440.)
		B = 1
	elif wavelength >= 490 and wavelength <= 509:
		G = 1
		B = - (wavelength - 510) / (510 - 490.)
	elif wavelength >= 510 and wavelength <= 579:
		R = (wavelength - 510) / (580 - 510.)
		G = 1
	elif wavelength >= 580 and wavelength <= 644:
		R = 1
		G = -(wavelength - 645) / (645 - 580.)
	elif wavelength >= 645 and wavelength <= 780:
		R = 1

	# Let the intensity fall off near the vision limits
	if wavelength >= 380 and wavelength <= 419:
		factor = .3 + .7 * (wavelength - 380) / (420 - 380.)
	elif wavelength >= 420 and wavelength <= 700:
		factor = 1
	elif wavelength >= 701 and wavelength <= 780:
		factor = .3 + .7 * (780 - wavelength) / (780 - 700.)

	# Adjust
	def adj(color, factor):
		if 0 == color:
			return 0
		else:
			return(int(imax * (color * factor) ** gamma))
	R = adj(R, factor)
	G = adj(G, factor)
	B = adj(B, factor)

	# Convert to hexadecimal
	def int2hex(color):
		color = hex(color).split('x')[1]
		while 2 > len(color):
			color = '0' + color
		return(color)
	R = int2hex(R)
	G = int2hex(G)
	B = int2hex(B)

	# To string
	return('#' + R + G + B)

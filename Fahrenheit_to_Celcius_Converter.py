def convert_to_celcius():
	in1 = float(raw_input("What is the Fahrenheit tempertature you would like to comvert to Celcius? "))
	s_in1 = in1 - 32
	cf = float(5) / float(9) 
	celcius_out = int(s_in1 * cf)
	print "The temperature you entered is %r degrees Celcius." % celcius_out
	#print "Your constants are: %r, %r" % (cf, s_in1)

convert_to_celcius()


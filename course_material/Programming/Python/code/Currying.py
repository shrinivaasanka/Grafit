##############################################################################################################################################
#<a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>.
###############################################################################################################################################
#Course Authored By:
#-----------------------------------------------------------------------------------------------------------
#Srinivasan Kannan
#(also known as: Shrinivaasan Kannan, Shrinivas Kannan)
#Ph: 9791499106, 9003082186
#Krishna iResearch Open Source Products Profiles:
#http://sourceforge.net/users/ka_shrinivaasan,
#https://github.com/shrinivaasanka,
#https://www.openhub.net/accounts/ka_shrinivaasan
#Personal website(research): https://sites.google.com/site/kuja27/
#emails: ka.shrinivaasan@gmail.com, shrinivas.kannan@gmail.com,
#kashrinivaasan@live.com
#-----------------------------------------------------------------------------------------------------------
##############################################################################################################################################

def function1(f):
	print f
	def function2(e):
		print e
		def function3(d):
			print d
			def function4(c):
				print c
				def function5(b):
					print b
					def function6(a):
						print a
						print "==========="
						print "Curried :"
						print "==========="
						print a,b,c,d,e,f
					return function6
				return function5
			return function4
		return function3
	return function2

if __name__=="__main__":
	function1(1)(2)(3)(4)(5)(6)

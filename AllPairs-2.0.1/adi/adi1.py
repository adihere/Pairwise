import metacomm.combinatorics.all_pairs2
all_pairs = metacomm.combinatorics.all_pairs2.all_pairs2

"""
Demo of the basic functionality - just getting pairwise/n-wise combinations
"""
#cd to /mnt/c/Users/adity/OneDrive/Documents/AllPairs-2.0.1/adi



parameters = [ [ "Mac", "Windows","Ubuntu"]
             , [ "Inkjet", "DotMatrix", "Laserjet"]
             , [ "Firefox", "Chrome" ]             
             ]

pairwise = all_pairs( parameters )

print "PAIRWISE of scenarios for printing documents:"
for i, v in enumerate(pairwise):
    print "%i:\t%s" % (i, str(v))


    
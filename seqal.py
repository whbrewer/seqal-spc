import ConfigParser
import sys, string
import alignment

# read parameters from input file
params = dict()
config = ConfigParser.ConfigParser()
config.read('seqal.ini')
for section in config.sections():
    for option in config.options(section):
        params[option] = config.get(section, option)

# parse out parameters from params dictionary
seq1 = params['seq1']
seq2 = params['seq2']
match = int(params['match'])
mismatch = int(params['mismatch'])
gap = int(params['indel'])

# set parameters
alignment.match_award      = match
alignment.mismatch_penalty = mismatch
alignment.gap_penalty      = gap

# Needleman-Wunsch
print "Global Alignment:"
alignment.needle(seq1, seq2)

print "-"*80

# Smith-Waterman
print "Local Alignment:"
alignment.water(seq1, seq2)


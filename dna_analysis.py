#DNA sample from crime scene computer:
sample = ['GTA','GGG','CAC']

#Function to read dna file and save as data
def read_dna(dna_file):
  dna_data = ""
  with open(dna_file, "r") as f:
    for line in f:
      dna_data += line
  return dna_data
 
#Codons are 3 letters. So break whole data into list having each item as 3 letters
def dna_codons(dna):
  codons = []
  for i in range(0,len(dna)-1,3):
    if i < len(dna):
     	codons.append(dna[i:i+3])
  return codons

#Match each codon in data to sample and count the number of matches
def match_dna(dna):
  matches = 0
  for codon in dna:
    if codon in sample:
      matches += 1
  return matches

#Main function to read file, break into 3 letters, count matches with computer sample and conclude if suspect if criminal!
def is_criminal(dna_sample):
  dna_data = read_dna(dna_sample)
  codons = dna_codons(dna_data)
  num_matches = match_dna(codons)
  if num_matches >=3:
    print "No. of matches are: %d. \n Investigation should continue!" % num_matches
  else:
    print "No. of matches are: %d. \n Suspect can be freed!" % num_matches
    

is_criminal("suspect1.txt")
is_criminal("suspect2.txt")
is_criminal("suspect3.txt")

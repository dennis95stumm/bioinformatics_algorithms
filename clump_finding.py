import rpy2.robjects as robjects

r_source = robjects.r["source"]
r_source("./pattern_to_number.r")
r_source("./number_to_pattern.r")
r_source("./computing_frequencies.r")
pattern_to_number = robjects.r["pattern_to_number"]
number_to_pattern = robjects.r["number_to_pattern"]
computing_frequencies = robjects.r["computing_frequencies"]

def clump_finding(genome, k, t, l):
  frequent_patterns = []
  clump = [0] * 4**k
  text = genome[0:l]
  frequency_array = computing_frequencies(text, k)
  for i in range(0, 4**k-1):
    if frequency_array[i] >= t:
      clump[i] = 1
  for i in range(1, len(genome) - l):
    first_pattern = genome[i - 1:i - 1 + k]
    index = int(pattern_to_number(first_pattern)[0])
    frequency_array[index] = frequency_array[index] - 1
    last_pattern = genome[i + l - k - 1:i + l - 1]
    index = int(pattern_to_number(last_pattern)[0])
    frequency_array[index] = frequency_array[index] + 1
    if frequency_array[index] >= t:
      clump[index] = 1
  for i in range(0, 4**k - 1):
    if clump[i] == 1:
      pattern = number_to_pattern(i, k)[0]
      frequent_patterns.append(pattern)
  return frequent_patterns


if __name__ == "__main__":
  filename = raw_input("Enter a file name: ")
  f = open(filename, "r")
  genome = f.readline()
  k, l, t = map(int, f.readline().split(" "))
  print " ".join(clump_finding(genome, k, t, l))

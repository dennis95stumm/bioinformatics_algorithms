from reverse_complement import reverse_complement
from neighbors import neighbors
from pattern_to_number import pattern_to_number

def computing_frequencies_with_mismatches_and_reverse_complements(text, k, d):
  frequency_array = [0] * 4**k
  for i in range(0, len(text) - k):
    pattern = text[i:i+k]
    neighborhood = neighbors(pattern, d) + neighbors(reverse_complement(pattern), d)
    for approximate_pattern in neighborhood:
      j = pattern_to_number(approximate_pattern)
      frequency_array[j] = frequency_array[j] + 1
  return frequency_array


if __name__ == "__main__":
  text = raw_input("Text: ")
  k, d = map(int, raw_input("K / D: ").split(" "))
  print computing_frequencies_with_mismatches_and_reverse_complements(text, k, d)

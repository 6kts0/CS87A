from collections import Counter

# SETS DO NOT SUPPORT INDEXING

text = "My name is Walter White and I live at 800 Negro Auroro lane"
vowels = {'a', 'e', 'i', 'o', 'u'} 

# Convert to a consistent case
processed_text = text.lower()

# Create the Counter object
counts = Counter(processed_text)

# Safely sum the counts for all vowels
vowel_count = sum(counts.get(vowel, 0) for vowel in vowels)

print(f"The total vowel count is: {vowel_count}")
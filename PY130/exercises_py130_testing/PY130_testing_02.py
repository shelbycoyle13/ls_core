# Equality Assertions
# Write a unittest assertion that will fail if value.lower does not return 'xyz'.

self.assertTrue(value.lower() == "xyz")

#Preferred LS Solution:
# self.assertEqual('xyz', value.lower())
#
# assertEqual('xyz', value.lower()) is preferred because:

# It gives a clearer failure message that shows the expected and actual values.
# It communicates intent (equality check) more directly. 
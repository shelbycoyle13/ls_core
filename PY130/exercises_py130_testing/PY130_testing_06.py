# Exception Assertions
# Write a unittest assertion that will fail unless employee.hire raises a NoExperienceError exception.

with self.assertRaises(NoExperienceError):
    employee.hire()
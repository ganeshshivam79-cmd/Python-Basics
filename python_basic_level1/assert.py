x = 10
assert x > 0               # Passes
assert x < 5, "x is not less than 5"  # Fails and raises AssertionError

self.assertEqual(a, b)
self.assertNotEqual(a, b)

self.assertTrue(x)
self.assertFalse(x)

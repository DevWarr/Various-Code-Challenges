import unittest

def name_list(names):
    if len(names) == 0:
        return ""
    if len(names) == 1:
        return names[0]["name"]
    
    
    result_str = ""
    for d in names:
        if d is names[-1]:
            result_str += d["name"]
        elif d is names[-2]:
            result_str += d["name"] + " & "
        else:
            result_str += d["name"] + ", "
            
    return result_str
    

def create_hash_names(name_arr):
    return [{"name": n} for n in name_arr]


class TestNameList(unittest.TestCase):

    def test_no_names(self):
        input_arr = []
        expected = ""

        result = name_list(input_arr)
        self.assertEqual(result, expected)

    def test_one_name(self):
        input_arr = create_hash_names(["Charlie"])
        expected = "Charlie"

        result = name_list(input_arr)
        self.assertEqual(result, expected)

    def test_1(self):
        input_arr = create_hash_names(["Charlie", "Bertha"])
        expected = "Charlie & Bertha"

        result = name_list(input_arr)
        self.assertEqual(result, expected)

    def test_2(self):
        input_arr = create_hash_names(["Charlie", "Bertha", "Array"])
        expected = "Charlie, Bertha & Array"

        result = name_list(input_arr)
        self.assertEqual(result, expected)

    def test_3(self):
        input_arr = create_hash_names(["Charlie", "Bertha", "Array", "Jhonny Cash", "Simon", "Garfunkel"])
        expected = "Charlie, Bertha, Array, Jhonny Cash, Simon & Garfunkel"

        result = name_list(input_arr)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
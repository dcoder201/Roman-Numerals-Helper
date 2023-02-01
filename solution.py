class RomanNumerals:

    def to_roman(val):
        values = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        symbols = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        result = ''
        for value, symbol in zip(values, symbols):
            while val >= value:
                result += symbol
                val -= value
        return result

    def from_roman(roman_num):
        roman_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        result = 0
        prev = 0
        for char in roman_num[::-1]:
            curr = roman_map[char]
            if prev > curr:
                result -= curr
            else:
                result += curr
            prev = curr
        return result
      
      
      
import codewars_test as test
from solution import RomanNumerals

@test.describe('sample_tests')
def sample_tests():
    @test.it('to roman')
    def sample_tests_to():
        test.assert_equals(RomanNumerals.to_roman(1000), 'M', '1000 should == "M"')
        test.assert_equals(RomanNumerals.to_roman(4), 'IV', '4 should == "IV"')
        test.assert_equals(RomanNumerals.to_roman(1), 'I', '1 should == "I"')
        test.assert_equals(RomanNumerals.to_roman(1990), 'MCMXC', '1990 should == "MCMXC"')
        test.assert_equals(RomanNumerals.to_roman(2008), 'MMVIII', '2008 should == "MMVIII"')
    @test.it('from roman')
    def sample_tests_from():
        test.assert_equals(RomanNumerals.from_roman('XXI'), 21, 'XXI should == 21')
        test.assert_equals(RomanNumerals.from_roman('I'), 1, 'I should == 1')
        test.assert_equals(RomanNumerals.from_roman('IV'), 4, 'IV should == 4')
        test.assert_equals(RomanNumerals.from_roman('MMVIII'), 2008, 'MMVIII should == 2008')
        test.assert_equals(RomanNumerals.from_roman('MDCLXVI'), 1666, 'MDCLXVI should == 1666')

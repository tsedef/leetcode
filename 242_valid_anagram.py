"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapOfAllSeenLetters = {}

        if len(s) != len(t) :
            return False

        for char_s, char_t in zip(s, t):
            if char_s in mapOfAllSeenLetters:
                mapOfAllSeenLetters[char_s] += 1
            else:
                mapOfAllSeenLetters[char_s] = 1

            if char_t in mapOfAllSeenLetters:
                mapOfAllSeenLetters[char_t] += 1
            else:
                mapOfAllSeenLetters[char_t] = 1
            print(mapOfAllSeenLetters)

        iteratingSet = set(s)

        for letter in t:
            if letter not in iteratingSet:
                return False
                
        return not any(value % 2 == 1 for value in mapOfAllSeenLetters.values())
"""

"""

    Create an unordered map count to store the character frequencies. The key of the map represents a character, and the value represents its frequency.
    Iterate over each character x in string s. For each character, increment its frequency in the count map by using the count[x]++ expression.
    Iterate over each character x in string t. For each character, decrement its frequency in the count map by using the count[x]-- expression.
    Iterate over each pair x in the count map. Each pair consists of a character and its corresponding frequency. Check if any frequency (x.second) is non-zero. If any frequency is non-zero, it means there is a character that appears more times in one string than the other, indicating that the strings are not anagrams. In that case, return false.
    If all frequencies in the count map are zero, it means the strings s and t have the same characters in the same frequencies, making them anagrams. In this case, the function returns true.

This approach counts the frequency of characters in one string and then adjusts the count by decrementing for the other string. If the strings are anagrams, the frequency of each character will cancel out, resulting in a map with all zero frequencies.

The time complexity of this solution is O(n), where n is the total number of characters in both strings. It iterates over each character once to count the frequencies and then compares the frequencies in the map, making it an efficient solution for the problem.
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = defaultdict(int)
        
        # Count the frequency of characters in string s
        for x in s:
            count[x] += 1
        
        # Decrement the frequency of characters in string t
        for x in t:
            count[x] -= 1
        
        # Check if any character has non-zero frequency
        for val in count.values():
            if val != 0:
                return False
        
        return True
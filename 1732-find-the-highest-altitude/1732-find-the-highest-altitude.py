class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = [0]
        max_alt = 0

        for i in range(len(gain)):
            alt.append(alt[i]+gain[i])
            if max_alt < alt[i+1]:
                max_alt = alt[i+1]

        return max_alt
var translator map[string]int = map[string]int{
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

func romanToInt(s string) int {
    if len(s) == 1 {
        return translator[string(s[0])]
    }

    sum := 0

    for i := 0; i < len(s); i++ {
        if i == len(s) - 1 {
            sum += translator[string(s[i])]
        } else if translator[string(s[i + 1])] > translator[string(s[i])] {
            sum += translator[string(s[i + 1])] - translator[string(s[i])]
            i++
        } else {
            sum += translator[string(s[i])]
        }
    }

    return sum
}


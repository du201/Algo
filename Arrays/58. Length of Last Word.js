/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {


    let lastChar, firstChar;
    for (let i = s.length - 1; i >= 0; i--) {
        if (s[i] !== " " && lastChar === undefined) {
            lastChar = i;
        } else if (s[i] === " " && lastChar !== undefined) {
            firstChar = i;
            break;
        }
    }

    if (firstChar === undefined) {
        firstChar = -1
    } 

    return lastChar - firstChar;
};
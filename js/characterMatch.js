exports.isCharacterMatch = function(string1, string2) {
    let str1 = string1.split('').map(elem => elem.replace(' ', '')).map(elem => elem.match(/[a-zA-Z]/) ? elem.toUpperCase() : elem).sort().join('')
    let str2 = string2.split('').map(elem => elem.replace(' ', '')).map(elem => elem.match(/[a-zA-Z]/) ? elem.toUpperCase() : elem).sort().join('')
    return str1 === str2
};

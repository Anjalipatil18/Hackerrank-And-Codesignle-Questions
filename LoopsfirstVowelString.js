function vowelsAndConsonants(s) {
    let vowel = ["a","i","o","e","u"]
    for (let i of s){
       if (vowel.includes(i)){
           console.log(i);
        }
    }
    for (let i of s){
       if (!vowel.includes(i)){
           console.log(i);
        }
    }
    
}
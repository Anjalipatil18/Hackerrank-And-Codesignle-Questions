function reverseString(s) {
    try {    
      let splitString = s.split("");
      let reverseString = splitString.reverse();
      let joinString = reverseString.join("");
      console.log(joinString);
    }
    catch(err){
      console.log("s.split is not a function")
      console.log(s)
    }
   finally{
      return (s);
   }
  }
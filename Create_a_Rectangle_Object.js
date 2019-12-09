function Rectangle(a, b) {
    var length = a;
    var width = b;
    var perimeter = 2*(length+width);
    var area = length*width;
    const obj={length,width,perimeter,area};
    return obj;
}

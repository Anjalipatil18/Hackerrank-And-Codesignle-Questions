class Polygon
{
    constructor(sides)
    {
        this.sides = sides;
    }

    perimeter()
    {
        var per = 0;
        for (var i = 0; i < this.sides.length; i++)
        {
            per += this.sides[i];
        }
        return per;
    }
}
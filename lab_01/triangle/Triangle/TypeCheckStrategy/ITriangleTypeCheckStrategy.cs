namespace triangle.Triangle.TypeCheckStrategy
{
    internal interface ITriangleTypeCheckStrategy
    {
        internal enum TriangleType
        {
            NotTriangle = 0,
            Triangle,
            Equilateral,
            Isosceles,
        }
        internal abstract TriangleType Check(double a, double b, double c);
    }
}

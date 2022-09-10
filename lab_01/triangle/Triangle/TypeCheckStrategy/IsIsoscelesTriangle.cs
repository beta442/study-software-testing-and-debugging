using static triangle.Triangle.TypeCheckStrategy.ITriangleTypeCheckStrategy;

namespace triangle.Triangle.TypeCheckStrategy
{
    internal class IsIsoscelesTriangle : IsTriangle
    {
        public override TriangleType Check(double a, double b, double c)
        {
            if (!IsValidTriangle(a, b, c))
            {
                return TriangleType.NotTriangle;
            }

            if (a == b && a != c || a == c && a != b || b == c && b != a)
            {
                return TriangleType.Isosceles;
            }

            return TriangleType.Triangle;
        }
    }
}

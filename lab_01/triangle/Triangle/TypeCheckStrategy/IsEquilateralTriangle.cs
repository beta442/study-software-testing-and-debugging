using static triangle.Triangle.TypeCheckStrategy.ITriangleTypeCheckStrategy;

namespace triangle.Triangle.TypeCheckStrategy
{
    internal class IsEquilateralTriangle : IsTriangle
    {
        public override TriangleType Check(double a, double b, double c)
        {
            if (!IsValidTriangle(a, b, c))
            {
                return TriangleType.NotTriangle;
            }
            
            if (a == b && a == c)
            {
                return TriangleType.Equilateral;
            }

            return TriangleType.Triangle;
        }
    }
}

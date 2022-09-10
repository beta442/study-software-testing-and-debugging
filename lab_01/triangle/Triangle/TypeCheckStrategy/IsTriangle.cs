using static triangle.Triangle.TypeCheckStrategy.ITriangleTypeCheckStrategy;

namespace triangle.Triangle.TypeCheckStrategy
{
    internal class IsTriangle : ITriangleTypeCheckStrategy
    {
        public virtual TriangleType Check(double a, double b, double c)
        {
            return IsValidTriangle(a, b, c) ? TriangleType.Triangle : TriangleType.NotTriangle;
        }

        protected static bool IsValidTriangle(double a, double b, double c)
        {
            if (a + b > c && a + c > b && b + c > a)
            {
                return true;
            }

            return false;
        }
    }
}

using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection.Metadata;
using System.Text;
using System.Threading.Tasks;

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

using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection.Metadata;
using System.Text;
using System.Threading.Tasks;

namespace triangle.Triangle.TypeCheckStrategy
{
    internal class IsEquilateralTriangle : IsTriangle
    {
        public override bool Check(double a, double b, double c)
        {
            bool result = base.Check(a, b, c) && (a == b && a == c);
            if (result)
            {
                _triangleType = "Equilateral";
            }

            return result;
        }
    }
}

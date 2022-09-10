using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace triangle.Triangle.TypeCheckStrategy
{
    internal class IsIsoscelesTriangle : IsTriangle
    {
        public override bool Check(double a, double b, double c)
        {
            bool result = base.Check(a, b, c) && (a == b && a != c || a == c && a != b || b == c && b != a);
            if (result)
            {
                _triangleType = "Isosceles";
            }
            return result;
        }
    }
}

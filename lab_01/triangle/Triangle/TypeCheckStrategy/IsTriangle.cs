using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace triangle.Triangle.TypeCheckStrategy
{
    internal class IsTriangle : ITriangleTypeCheckStrategy
    {
        public virtual bool Check(double a, double b, double c)
        {
            bool result = IsValidTriangle(a, b, c);
            _triangleType = result ? "Triangle" : "NotTriangle";

            return result;
        }
        public string TriangleType()
        {
            return _triangleType;
        }

        protected static bool IsValidTriangle(double a, double b, double c)
        {
            if (a + b > c && a + c > b && b + c > a)
            {
                return true;
            }

            return false;
        }

        protected string _triangleType = "NotTriangle";
    }
}

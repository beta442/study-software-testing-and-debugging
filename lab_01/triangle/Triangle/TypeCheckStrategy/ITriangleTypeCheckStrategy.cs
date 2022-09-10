using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

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

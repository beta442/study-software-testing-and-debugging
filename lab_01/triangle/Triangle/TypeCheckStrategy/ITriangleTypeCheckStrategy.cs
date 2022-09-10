using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace triangle.Triangle.TypeCheckStrategy
{
    internal interface ITriangleTypeCheckStrategy
    {
        public abstract bool Check(double a, double b, double c);
        public string TriangleType();
    }
}

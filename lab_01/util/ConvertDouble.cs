using System;
using System.Linq;

namespace util
{
    public class ConvertDouble
    {
        public static double[] ConvertToDoubleStringArr(string[] arr)
        {
            try
            {
                return arr.Select(double.Parse).ToArray();
            }
            catch (Exception)
            {
                throw new ArgumentException("Failed to convert string[] to double[]");
            }
        }
    }
}

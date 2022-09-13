using triangle.Triangle.TypeCheckStrategy;
using util;

using TriangleType = triangle.Triangle.TypeCheckStrategy.ITriangleTypeCheckStrategy.TriangleType;

const string unhandledExceptionMsg = "UnhandledException";

ITriangleTypeCheckStrategy[] triangleTypeCheckStrategies = new ITriangleTypeCheckStrategy[] {
    new IsTriangle(),
    new IsEquilateralTriangle(),
    new IsIsoscelesTriangle()
};

static void WriteTriangleType(TriangleType type)
{
    Console.WriteLine(type.ToString());
}

try
{
    if (args.Length >= 3)
    {
        double[] triangleSides = ConvertDouble.ConvertToDoubleStringArr(new ArraySegment<string>(args, 0, 3).ToArray());

        double a = triangleSides[0];
        double b = triangleSides[1];
        double c = triangleSides[2];

        var result = TriangleType.NotTriangle;
        foreach (var strategy in triangleTypeCheckStrategies)
        {
            result = strategy.Check(a, b, c);
            if (result == TriangleType.NotTriangle ||
                result != TriangleType.Triangle)
            {
                break;
            }
        }

        WriteTriangleType(result);

        return 0;
    }
    else
    {
        throw new ArgumentException(unhandledExceptionMsg);
    }
}
catch (Exception)
{
    Console.WriteLine(unhandledExceptionMsg);
    return 1;
}

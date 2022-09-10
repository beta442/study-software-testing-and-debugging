using triangle.Triangle.TypeCheckStrategy;

const String unhandledExceptionMsg = "UnhandledException";

static double[] ConvertToDoubleStringArr(string[] arr)
{
    try
    {
        return arr.Select(double.Parse).ToArray();
    }
    catch (Exception)
    {
        throw new ArgumentException(unhandledExceptionMsg);
    }
}

ITriangleTypeCheckStrategy[] triangleTypeCheckStrategies = new ITriangleTypeCheckStrategy[] {
    new IsTriangle(),
    new IsEquilateralTriangle(),
    new IsIsoscelesTriangle()
};

void WriteTriangleType(ITriangleTypeCheckStrategy.TriangleType type)
{
    Console.WriteLine(type.ToString());
}

try
{
    if (args.Length >= 3)
    {
        double[] triangleSides = ConvertToDoubleStringArr(new ArraySegment<string>(args, 0, 3).ToArray());

        double a = triangleSides[0];
        double b = triangleSides[1];
        double c = triangleSides[2];

        ITriangleTypeCheckStrategy.TriangleType result = ITriangleTypeCheckStrategy.TriangleType.NotTriangle;
        foreach (var strategy in triangleTypeCheckStrategies)
        {
            result = strategy.Check(a, b, c);
            if (result == ITriangleTypeCheckStrategy.TriangleType.NotTriangle || result != ITriangleTypeCheckStrategy.TriangleType.Triangle)
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
catch (Exception ex)
{
    Console.WriteLine(ex.Message);
    return 1;
}

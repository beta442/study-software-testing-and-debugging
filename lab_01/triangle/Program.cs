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

try
{
    if (args.Length >= 3)
    {
        double[] triangleSides = ConvertToDoubleStringArr(new ArraySegment<string>(args, 0, 3).ToArray());

        double a = triangleSides[0];
        double b = triangleSides[1];
        double c = triangleSides[2];

        string triangleType = "";
        foreach (var strategy in triangleTypeCheckStrategies)
        {
            bool result = strategy.Check(a, b, c);
            triangleType = strategy.TriangleType();
            if (!result && strategy.GetType() == typeof(IsTriangle) // not triangle
                || result && strategy.GetType() != typeof(IsTriangle)) // found type
            {
                break;
            }
        }
        Console.WriteLine(triangleType);

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

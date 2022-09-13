using System.Diagnostics;

using util;

string userInput = args.Length > 0 ? args[0] : "";
string[] expectedTriangleTypes = { "NotTriangle", "Triangle", "Equilateral", "Isosceles" };
const string triangleTypeCheckAppName = "triangle.exe";
const string outputResultFileName = "result.txt";

void ReadFilePath()
{
    while (userInput == "")
    {
        Console.WriteLine("Type file path:");
        var input = Console.ReadLine();
        userInput = input ?? "";
    }
}

while (true)
{
    try
    {
        ReadFilePath();
        using StreamReader sr = new(userInput);
        using StreamWriter sw = new(outputResultFileName);
        string? line = "";
        int lineConunter = 0;
        while ((line = sr.ReadLine()) != null)
        {
            ++lineConunter;
            if (line.Length == 0)
            {
                sw.WriteLine();
                continue;
            }
            string[] arguments = line.Split(' ');
            double[] triangleSides = Array.Empty<double>();
            try
            {
                triangleSides = ConvertDouble.ConvertToDoubleStringArr(new ArraySegment<string>(arguments, 0, 3).ToArray());
                if (!expectedTriangleTypes.Contains(arguments[3]))
                {
                    throw new ArgumentException("Invalid triangle's type at 4 position");
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Wrong argument at line {lineConunter}. -> {ex.Message}");
            }

            var startInfo = new ProcessStartInfo
            {
                FileName = triangleTypeCheckAppName,
                Arguments = string.Join(" ", triangleSides),
                UseShellExecute = false,
                RedirectStandardOutput = true,
                CreateNoWindow = true
            };

            using Process? proc = Process.Start(startInfo);
			if (proc != null)
            {
                while (!proc.StandardOutput.EndOfStream)
                {
                    string? result = proc.StandardOutput.ReadLine();

                    string outputRes = (arguments.Last() == result) ? "success" : "error";

                    sw.WriteLine(outputRes);
                }
            }
        }

        return;
    }
    catch (Exception ex)
    {
        Console.WriteLine(ex.Message);
        userInput = "";
    }
}
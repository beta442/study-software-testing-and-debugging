﻿using System.Diagnostics;

using util;

string userInput = args.Length > 0 ? args[0] : "";
string[] expectedTriangleTypes = { "NotTriangle", "Triangle", "Equilateral", "Isosceles" };
const string triangleTypeCheckAppName = "triangle.exe";

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
        StreamReader sr = new(userInput);
        string? line = "";
        int lineConunter = 1;
        while ((line = sr.ReadLine()) != null)
        {
            if (line.Length == 0)
            {
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

            var proc = Process.Start(startInfo);
            if (proc != null)
            {
                while (!proc.StandardOutput.EndOfStream)
                {
                    Console.WriteLine(proc.StandardOutput.ReadLine());
                }
            }

            ++lineConunter;
        }

        return;
    }
    catch (Exception ex)
    {
        Console.WriteLine(ex.Message);
        userInput = "";
    }
}
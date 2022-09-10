using System;
using System.Diagnostics;
using System.IO;
using System.Linq;

using util;

namespace triangle_test
{
    internal class Program
    {
        static void Main(string[] args)
        {
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
                    using (StreamReader sr = new StreamReader(userInput))
                    {
                        string line = "";
                        int lineConunter = 1;
                        while ((line = sr.ReadLine()) != null)
                        {
                            if (line.Length == 0)
                            {
                                continue;
                            }
                            string[] arguments = line.Split(' ');
                            try
                            {
                                ConvertDouble.ConvertToDoubleStringArr(new ArraySegment<string>(arguments, 0, 3).ToArray());
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
                                FileName = "triangle.exe",
                                Arguments = "1 2 3",
                                UseShellExecute = true,
                                RedirectStandardOutput = false,
                                CreateNoWindow = true
                            };

                            using (var proc = Process.Start(startInfo))
                            {
                                Console.WriteLine(1);
                                while (!proc.StandardOutput.EndOfStream)
                                {
                                    string procLine = proc.StandardOutput.ReadLine();
                                    
                                }
                            }

                            ++lineConunter;
                        }

                        Console.WriteLine(line);
                    }

                    return;
                }
                catch (Exception ex)
                {
                    Console.WriteLine(ex.Message);
                    userInput = "";
                }
            }
        }
    }
}

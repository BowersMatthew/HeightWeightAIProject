using System;
2using GemBox.Spreadsheet;
3using GemBox.Spreadsheet.Charts;
4
5class graphTest
6{
7    [STAThread]
8    static void Main(string[] args)
9    {
10        // If using Professional version, put your serial key below.
11        SpreadsheetInfo.SetLicense("FREE-LIMITED-KEY");
12
13        ExcelFile ef = new ExcelFile();
14        ExcelWorksheet ws = ef.Worksheets.Add("Chart");
15
16        int numberOfEmployees = 4;
17
18        // Create Excel chart and select data for it.
19        var chart = ws.Charts.Add(ChartType.Bar, "D2", "M25");
20        chart.SelectData(ws.Cells.GetSubrangeAbsolute(0, 0, numberOfEmployees, 1), true);
21
22        // Add data which is used by the Excel chart.
23        var names = new string[] { "John Doe", "Fred Nurk", "Hans Meier", "Ivan Horvat" };
24        var random = new Random();
25        for (int i = 0; i < numberOfEmployees; i++)
26        {
27            ws.Cells[i + 1, 0].Value = names[i % names.Length] + (i < names.Length ? string.Empty : ' ' + (i / names.Length + 1).ToString());
28            ws.Cells[i + 1, 1].SetValue(random.Next(1000, 5000));
29        }
30
31        // Set header row and formatting.
32        ws.Cells[0, 0].Value = "Name";
33        ws.Cells[0, 1].Value = "Salary";
34        ws.Cells[0, 0].Style.Font.Weight = ws.Cells[0, 1].Style.Font.Weight = ExcelFont.BoldWeight;
35        ws.Columns[0].Width = (int)LengthUnitConverter.Convert(3, LengthUnit.Centimeter, LengthUnit.ZeroCharacterWidth256thPart);
36        ws.Columns[1].Style.NumberFormat = "\"$\"#,##0";
37
38        // Make entire sheet print on a single page.
39        ws.PrintOptions.FitWorksheetWidthToPages = ws.PrintOptions.FitWorksheetHeightToPages = 1;
40
41        ef.Save("Chart.xlsx");
42    }
43}
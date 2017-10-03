using System;
using System.IO;

class PersonTest
{
    public static void Main()
    {
        Person[] people = new Person[10];
        people[0]= new Person(0.12, 1.01, 0);

        Console.WriteLine(people[0].weight);
    }
}
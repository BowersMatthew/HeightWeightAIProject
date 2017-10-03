using System;

public static class RandomZScore
{ 
    // code adapted from
    // https://stackoverflow.com/questions/218060/random-gaussian-variables
    // reuse this if you are generating many RESETS SEED
    static Random rand = new Random(Guid.NewGuid().GetHashCode());
    
    public static double rando()
    {         
        double u1 = 1 - rand.NextDouble(); //uniform(0,1] random doubles
        double u2 = 1 - rand.NextDouble();
        double stdRand = Math.Sqrt(-2.0 * Math.Log(u1)) * Math.Sin(2.0 * Math.PI * u2); //random normal(0,1)
        Console.WriteLine(stdRand);
        return stdRand;
    }
}
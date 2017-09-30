using System;
using System.IO;

class RandomTest{
    static Random rand = new Random(Guid.NewGuid().GetHashCode());
    public static double rando()
    {
        //Random rand = new Random(Guid.NewGuid().GetHashCode()); //reuse this if you are generating many RESETS SEED
                                    //https://stackoverflow.com/questions/218060/random-gaussian-variables
        double stdRand;
        
            double u1 = rand.NextDouble(); //uniform(0,1] random doubles
            double u2 = rand.NextDouble();
            stdRand = Math.Sqrt(-2.0 * Math.Log(u1)) * Math.Sin(2.0 * Math.PI * u2); //random normal(0,1)
        // while (stdRand > 1 || stdRand < -1);
        Console.WriteLine(stdRand);
        return stdRand;
    }

    public static void Main(){
        int[] count = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
        
        for(int i = 0; i < 5000; i++){
            count[(int) (5*rando() + 25)]++;
        }

        for(int i = 0; i < 50; i++){
            Console.Write(i + ": ");
            for(int j = count[i]; j > 0; j--){
                Console.Write("*");
            }
            Console.WriteLine("");
        }

    }
}
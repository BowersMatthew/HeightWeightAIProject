using System;
using System.IO;

class HammerschmidtHeightWeight
{
    public static double rando()
    {
        Random rand = new Random(Guid.NewGuid().GetHashCode()); //reuse this if you are generating many RESETS SEED
                                    //https://stackoverflow.com/questions/218060/random-gaussian-variables
        double u1 = 1 - rand.NextDouble(); //uniform(0,1] random doubles
        double u2 = 1 - rand.NextDouble();
        double stdRand = Math.Sqrt(-2.0 * Math.Log(u1)) * Math.Sin(2.0 * Math.PI * u2); //random normal(0,1)
        Console.WriteLine(stdRand);
        return stdRand;
    }
    static void Main()
    {
        /*
        Male test = new Male();
        test.setHeight(100);
        Console.WriteLine(test.height);
        */
        const int numPeople = 2000;
        Male[] men = new Male[numPeople];
        Female[] women = new Female[numPeople];

        for (int i = 0; i < numPeople; i++)
        {
            men[i] = new Male();
            women[i] = new Female();
            men[i].setHeight(rando());
            men[i].setWeight(rando());
            women[i].setHeight(rando());
            women[i].setWeight(rando());
        }

        // calculate average and sd for people
        double avgH, avgW, sdH, sdW;
        double sumH = 0, sumW = 0;
        for (int i = 0; i < numPeople; i++){
            sumH += men[i].height + women[i].height;
            sumW += men[i].weight + women[i].weight;
        }
        avgH = sumH/(2*numPeople);
        avgW = sumW/(2*numPeople);

        double sumOfSquaresH = 0, sumOfSquaresW = 0;
        for (int i = 0; i < numPeople; i++){
            sumOfSquaresH += Math.Pow((men[i].height - avgH), 2) + Math.Pow((women[i].height - avgH), 2);
            sumOfSquaresW += Math.Pow((men[i].weight - avgW), 2) + Math.Pow((women[i].weight - avgW), 2);
        }        
        sdH = sumOfSquaresH/(2*numPeople);
        sdW = sumOfSquaresW/(2*numPeople);

        // normalize the height and weight of each person to (-1, 1)
        for(int i = 0; i < numPeople; i++){
            men[i].height = Normalizer.Normalize(men[i].height, avgH, sdH);
            men[i].weight = Normalizer.Normalize(men[i].weight, avgW, sdW);
            women[i].height = Normalizer.Normalize(women[i].height, avgH, sdH);
            women[i].weight = Normalizer.Normalize(women[i].weight, avgW, sdW);
        }

        //Console.WriteLine("Male");
        //Console.WriteLine("Height \t Weight");
        StreamWriter output = new StreamWriter("data.txt");
        for (int i = 0; i < numPeople; i++)
        {
            //std::cout << (men + i)->height << "\t" << (men + i)->weight << "\n";
            output.WriteLine(men[i].height + "," + men[i].weight + ",0");
        }
        //Console.WriteLine("Female");
        //Console.WriteLine("Height \t Weight");
        for (int p = 0; p < numPeople; p++)
        {
            output.WriteLine(women[p].height + "," + women[p].weight + ",0");
        }

        output.Close();

    }
}

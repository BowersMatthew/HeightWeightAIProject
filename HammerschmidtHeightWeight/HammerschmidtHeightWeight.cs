using System;
// class representing a random male human
public class Male {
    // in cm
	// these constants are derived from the WHO standard growth charts
	const double aveHeight = 176.5;
	const double sdHeight = 6.2;
    // Block, J. P., Subramanian, S. V., Christakis, N. A., & O�Malley, 
    // A. J. (2013). Population Trends and Variation in Body Mass Index 
    // from 1971 to 2008 in the Framingham Heart Study Offspring Cohort. 
    // PLoS ONE, 8(5), e63217. http://doi.org/10.1371/journal.pone.0063217
    // kg/m/m
    const double aveBMI = 29;
	const double sdBMI = 4.73;

	public double height;
	public double weight;

	public void setHeight(double hz) {
		height = hz * sdHeight + aveHeight;
	}
	public void setWeight(double BMIz) {
		weight = (BMIz * sdBMI + aveBMI) * height / 100 * height / 100;
	}
};
public class Female {
    
	// in cm
	// these constants are derived from the WHO standard growth charts
	const double aveHeight = 163.3;
	const double sdHeight = 5.5; 
	// Block, J. P., Subramanian, S. V., Christakis, N. A., & O�Malley, 
	// A. J. (2013). Population Trends and Variation in Body Mass Index 
	// from 1971 to 2008 in the Framingham Heart Study Offspring Cohort. 
	// PLoS ONE, 8(5), e63217. http://doi.org/10.1371/journal.pone.0063217
	// kg/m/m
	const double aveBMI = 27.7;
	const double sdBMI = 6.15;

	public double height;
	public double weight;

	public void setHeight(double hz) {
		height = hz * sdHeight + aveHeight;
	}
	public void setWeight(double BMIz) {
		weight = (BMIz * sdBMI + aveBMI) * height / 100 * height / 100;
	} 

};


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
        Male[] men = new Male[1000];
        Female[] women = new Female[1000];

        for (int i = 0; i < 1000; i++)
        {
            men[i] = new Male();
            women[i] = new Female();
            men[i].setHeight(rando());
            men[i].setWeight(rando());
            women[i].setHeight(rando());
            women[i].setWeight(rando());
        }
        //Console.WriteLine("Male");
        //Console.WriteLine("Height \t Weight");
        for (int i = 0; i < 1000; i++)
        {
            //std::cout << (men + i)->height << "\t" << (men + i)->weight << "\n";
            Console.WriteLine(men[i].height + "," + men[i].weight + ",0");
        }
        //Console.WriteLine("Female");
        //Console.WriteLine("Height \t Weight");
        for (int p = 0; p < 1000; p++)
        {
            Console.WriteLine(women[p].height + "," + women[p].weight + ",0");
        }

    }
}

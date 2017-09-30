using System;

public class Person 
{
    static readonly int MALE = 0;
    static readonly int FEMALE = 1;
    // in cm
    // these constants are derived from the WHO standard growth charts
    static readonly double maleAveHeight = 176.5;
    static readonly double maleSdHeight = 6.2;
    static readonly double femaleAveHeight = 163.3;
    static readonly double femaleSdHeight = 5.5; 
    // Block, J. P., Subramanian, S. V., Christakis, N. A., & O�Malley, 
    // A. J. (2013). Population Trends and Variation in Body Mass Index 
    // from 1971 to 2008 in the Framingham Heart Study Offspring Cohort. 
    // PLoS ONE, 8(5), e63217. http://doi.org/10.1371/journal.pone.0063217
    // kg/m/m
    static readonly double maleAveBMI = 29;
    static readonly double maleSdBMI = 4.73;
    static readonly double femaleAveBMI = 27.7;
    static readonly double femaleSdBMI = 6.15;

    public double height;
    public double weight;
    public int sex;

    // Constructor throws ArgumentException if sex is not 0 or 1
    public Person(double zH, double zW, int sex)
    {
        this.sex = sex;
        if(sex == MALE)
        {
            setHeight(maleAveHeight, maleSdHeight, zH);
            setWeight(maleAveBMI, maleSdBMI, zW);
        }else if(sex == FEMALE)
        {
            setHeight(femaleAveHeight, femaleSdHeight, zH);
            setWeight(femaleAveBMI, femaleSdBMI, zW);
        }else
        {
            throw new ArgumentException("unknown sex.");
        }
    }

    private void setHeight(double aveHeight, double sdHeight, double hz) 
    {
        height = hz * sdHeight + aveHeight;
    }
    private void setWeight(double aveBMI, double sdBMI, double BMIz) 
    {
        weight = (BMIz * sdBMI + aveBMI) * height / 100 * height / 100;
    }

}

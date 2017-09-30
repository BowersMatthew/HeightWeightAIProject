namespace Person
{
    
    public class Person 
    {

        const int MALE = 0;
        const int FEMALE = 1;
        // in cm
        // these constants are derived from the WHO standard growth charts
        const double maleAveHeight = 176.5;
        const double maleSdHeight = 6.2;
        const double femaleAveHeight = 163.3;
        const double femaleSdHeight = 5.5; 
        // Block, J. P., Subramanian, S. V., Christakis, N. A., & O�Malley, 
        // A. J. (2013). Population Trends and Variation in Body Mass Index 
        // from 1971 to 2008 in the Framingham Heart Study Offspring Cohort. 
        // PLoS ONE, 8(5), e63217. http://doi.org/10.1371/journal.pone.0063217
        // kg/m/m
        const double maleAveBMI = 29;
        const double maleSdBMI = 4.73;
        const double femaleAveBMI = 27.7;
        const double femaleSdBMI = 6.15;

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
                throw new ArgumentException("unknown sex.")
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
}
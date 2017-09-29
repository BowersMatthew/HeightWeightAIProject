public class Male
{
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

	public void setHeight(double hz) 
    {
		height = hz * sdHeight + aveHeight;
	}
	public void setWeight(double BMIz) 
    {
		weight = (BMIz * sdBMI + aveBMI) * height / 100 * height / 100;
	}
}
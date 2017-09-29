public class Female 
{
    
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

	public void setHeight(double hz) 
    {
		height = hz * sdHeight + aveHeight;
	}
	public void setWeight(double BMIz) 
    {
		weight = (BMIz * sdBMI + aveBMI) * height / 100 * height / 100;
	} 

}
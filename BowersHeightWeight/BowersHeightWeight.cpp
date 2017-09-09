// Title: BowersHeightWeight.cpp
// Author: Matthew Bowers
// Date: 9/8/17

#include <iostream>
#include <random>
#include <string>
#include "stdafx.h"

// class representing a random male human
class Male {
public:
	// in cm
	// these constants are derived from the WHO standard growth charts
	const double aveHeight = 176.5;
	const double sdHeight = 6.2;
	// Block, J. P., Subramanian, S. V., Christakis, N. A., & O’Malley, 
	// A. J. (2013). Population Trends and Variation in Body Mass Index 
	// from 1971 to 2008 in the Framingham Heart Study Offspring Cohort. 
	// PLoS ONE, 8(5), e63217. http://doi.org/10.1371/journal.pone.0063217
	// kg/m/m
	const double aveBMI = 29;
	const double sdBMI = 4.73;

	double height;
	double weight;

	void setHeight(double hz) {
		height = hz * sdHeight + aveHeight;
	}
	void setWeight(double BMIz) {
		weight = (BMIz * sdBMI + aveBMI) * height / 100 * height / 100;
	}
};

class Female {
public:
	// in cm
	// these constants are derived from the WHO standard growth charts
	const double aveHeight = 163.3;
	const double sdHeight = 5.5;
	// Block, J. P., Subramanian, S. V., Christakis, N. A., & O’Malley, 
	// A. J. (2013). Population Trends and Variation in Body Mass Index 
	// from 1971 to 2008 in the Framingham Heart Study Offspring Cohort. 
	// PLoS ONE, 8(5), e63217. http://doi.org/10.1371/journal.pone.0063217
	// kg/m/m
	const double aveBMI = 27.7;
	const double sdBMI = 6.15;

	double height;
	double weight;

	void setHeight(double hz) {
		height = hz * sdHeight + aveHeight;
	}
	void setWeight(double BMIz) {
		weight = (BMIz * sdBMI + aveBMI) * height / 100 * height / 100;
	} 

};

int main() {
	Male men[1000];
	Female women[1000];
	// set up random number generators
	std::random_device generator;
	std::normal_distribution<double> distribution{ 0, 1 };

	for (int i = 0; i < 1000; i++) {
		(men + i)->setHeight(distribution(generator) );
		(men + i)->setWeight(distribution(generator));
		(women + i)->setHeight(distribution(generator));
		(women + i)->setWeight(distribution(generator));
	}

	std::cout << "Male\n";
	std::cout << "Height\tWeight\n";
	for (int i = 0; i < 1000; i++) {
		std::cout << (men + i)->height << "\t" << (men + i)->weight << "\n";
	}
	std::cout << "Female\n";
	std::cout << "Height\tWeight";
	for (int i = 0; i < 1000; i++) {
		std::cout << (women + i)->height << "\t" << (women + i)->weight << "\n";
	}

	return 0;
}

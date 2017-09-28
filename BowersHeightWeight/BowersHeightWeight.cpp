// Title: BowersHeightWeight.cpp
// Author: Matthew Bowers
// Date: 9/8/17

#include <iostream>
#include <random>
#include <string>
#include <fstream>
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
	std::fstream file;
	file.open("data.txt", std::fstream::out);
	if (file.is_open()) {
		std::cout << "file opened successfully\n";
	}

	int const number = 2000;
	Male men[number];
	Female women[number];
	// set up random number generators
	std::random_device generator;
	std::normal_distribution<double> distribution{ 0, 1 };


	for (int i = 0; i < number; i++) {
		(men + i)->setHeight(distribution(generator) );
		(men + i)->setWeight(distribution(generator));
		(women + i)->setHeight(distribution(generator));
		(women + i)->setWeight(distribution(generator));
	}

	for (int i = 0; i < number; i++) {
		file << (men + i)->height << "," << (men + i)->weight << ",0\n";
	}
	
	for (int i = 0; i < number; i++) {
		file << (women + i)->height << "," << (women + i)->weight << ",1\n";
	}

	int pcorrect = 0;
	int ncorrect = 0;
	int d1pc = 0;
	int d1nc = 0;
	int incorrect = 0;

	for (int i = 0; i < number; i++) {
		if ((men + i)->height > 166) {
			d1nc++;
		}
		if ((women + i)->height <= 166) {
			d1pc++;
		}
		if (-12 * ((men + i)->height) - ((men + i)->weight) + 2126 <= 0) {
			ncorrect++;
		}
		else { incorrect++; }
		if (-12 * ((women + i)->height) - ((women + i)->weight) + 2126 > 0) {
			pcorrect++;
		}
		else { incorrect++; }
	}
		
	std::cout << "1Dtrue negative: " << (double)d1nc / number << "\n";
	std::cout << "1Dfalse positive: " << (double)(number - d1nc) / number << "\n";
	std::cout << "1Dtrue positive: " << (double)d1pc / number << "\n";
	std::cout << "1Dfalse negative: " << (double)(number - d1pc) / number << "\n";
	std::cout << "2Dtrue negative: " << (double)ncorrect / number << "\n";
	std::cout << "2Dfalse positive: " << (double)(number - ncorrect) / number << "\n";
	std::cout << "2Dtrue positive: " << (double)pcorrect / number << "\n";
	std::cout << "2Dfalse negative: " << (double)(number - pcorrect) / number << "\n";
	
	double accuracy = ((double)pcorrect + (double)ncorrect)/ (2*number);
	std::cout << "1Dunit: height - 166 <= 0\n";
	std::cout << "1Daccurracy: " << ((double)(d1nc + d1pc) / (2 * number)) << "\n";
	std::cout << "1Derror: " << 1 - ((double)(d1nc + d1pc) / (2 * number)) << "\n";
	std::cout << "2Dunit: -12(height)-(weight)+2146 >= 0\n";
	std::cout << "2Daccurracy: " << accuracy << "\n";
	std::cout << "2Derror: " << 1 - accuracy << "\n";

	file.close();
	return 0;
}


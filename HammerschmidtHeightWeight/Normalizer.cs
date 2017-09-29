public static class Normalizer
{

    public static double Normalize(double value, double avg, double sd)
    {
        return (value - avg)/sd;
    }
}
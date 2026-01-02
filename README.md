# Estimation of Coprime Probability

This project estimates the probability that two randomly chosen integers are coprime using Monte Carlo simulation.

## Mathematical Background

Two integers are said to be coprime (or relatively prime) if their greatest common divisor (GCD) is 1. The probability that two randomly chosen integers are coprime is theoretically equal to 6/π² ≈ 0.6079.

## Features

- Monte Carlo simulation to estimate coprime probability
- Experiments with varying numbers of trials (1000, 10000, 100000, 1000000)
- Visualization of results with matplotlib
- Comparison with theoretical probability

## Requirements

- Python 3.x
- matplotlib
- math (built-in)
- random (built-in)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/adwestmont0/Estimation_of_coprime_probability.git
   cd Estimation_of_coprime_probability
   ```

2. Install required packages:
   ```bash
   pip install matplotlib
   ```

## Usage

Run the main script to perform the experiments and generate a plot:

```bash
python coprime.py
```

This will:
1. Run Monte Carlo simulations with increasing numbers of trials
2. Generate a plot showing how the estimated probability converges to the theoretical value
3. Save the plot as `coprime_probability_experiment.png`

## Classes

- `Coprime_Probability`: Performs Monte Carlo simulation for a given number of trials
- `Coprime_Probability_Experiments`: Runs multiple experiments with different trial counts and generates plots

## Output

The script generates a plot showing:
- Estimated probability vs number of trials (log scale)
- Theoretical probability line (6/π²)
- Saved as PNG file with high resolution

## License

This project is open source. Please refer to the repository for licensing information.

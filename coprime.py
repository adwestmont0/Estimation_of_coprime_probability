import math
import random

def gcd(a, b):
    while  b != 0:
        a, b = b, a % b
    return a

def are_coprime(a, b):
    return gcd(a, b) == 1


class Coprime_Probability:
    def __init__(self, num_trials, range_limit = 100):
        self.num_trials = num_trials
        self.range_limit = range_limit

    def run(self):
        coprime_count = 0
        for x in range(self.num_trials):
            a = random.randint(1, self.range_limit)
            b = random.randint(1, self.range_limit)
            if are_coprime(a, b):
                coprime_count += 1
        probability = coprime_count / self.num_trials
        return probability

class Coprime_Probability_Experiments:
    def __init__(self):
        self.probabilities = []
        self.trials_list = [1000, 10000, 100000, 1000000]

    def run_all(self):
        for num_trials in self.trials_list:
            experiment = Coprime_Probability(num_trials)
            probability = experiment.run()
            self.probabilities.append(probability)
            
    def plot_results(self):
        import matplotlib.pyplot as plt

        plt.plot(self.trials_list, self.probabilities, marker='o')
        plt.xscale('log')
        plt.xlabel('Number of Trials (log scale)')
        plt.ylabel('Estimated Probability')
        plt.title('Estimated Probability of Coprimality vs Number of Trials')
        plt.axhline(y=6/(math.pi**2), color='r', linestyle='--', label='Expected Probability (6/π²)')
        plt.legend()
        plt.grid(True)
        plt.savefig('coprime_probability_experiment.png', dpi=300)
        plt.show()
        plt.close()

def main():
    a = Coprime_Probability_Experiments()
    a.run_all()
    a.plot_results()


if __name__ == "__main__":
    main()


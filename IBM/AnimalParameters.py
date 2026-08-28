from dataclasses import dataclass

@dataclass
class AnimalParameters:
    """Contains parameters that control the behaviour of the animals.

    Attributes:
        a: The probability that if a prey gets paired with a predator, it will die.
        b: The probability relating to predator reproduction when paired with a prey. The exact effect of this parameter depends on the predator reproduction mechanic chosen for the experiment.
        c: The probability that a prey will reproduce in a turn.
        d: The probability that a predator will die in a turn.
    """
    a: float
    b: float
    c: float
    d: float
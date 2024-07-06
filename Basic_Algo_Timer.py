import timeit
from typing import Callable

"""
This is basically a wrapper around the timeit library \n
I'm not looking up how to use the timeit library everytime I want to time something
"""

def Time_Algorithm_ms(Algorithm: Callable,
                      Setup: Callable = "pass",
                      Vars: dict[str: any] | None = None,
                      iterations: int = 100) -> None:
    
    """
    Times the pointed_to algorithm\n
    You can use the globals() method if you are lazy to populate Vars\n
    Setup can be used to put a load of variables into scope for convenience
    and is not included in the resultant time
    """

    timer_result = timeit.timeit(stmt=Algorithm, setup=Setup, globals=Vars, number=iterations)
    average_time_ms = (timer_result * 1000) / iterations
    print(f"Execution time = {round(average_time_ms,6)} miliseconds")

def Compare_Two_Algorithms_ms(Algorithm_A: Callable,
                              Algorithm_B: Callable,
                              A_Setup: Callable = "pass",
                              B_Setup: Callable = "pass",
                              A_Vars: dict[str: any] | None = None,
                              B_Vars: dict[str: any] | None = None,
                              iterations: int = 100) -> None:
    
    """
    Compare the speed of Algorithm A vs B, Timed in Ms \n
    This basically runs Time_Algorithm_ms twice, so see description of that for use.
    """
    
    timer_result = timeit.timeit(stmt=Algorithm_A, setup=A_Setup, globals=A_Vars, number=iterations)
    average_time_Algorithm_A_ms = (timer_result * 1000) / iterations

    timer_result = timeit.timeit(stmt=Algorithm_B, setup=B_Setup, globals=B_Vars, number=iterations)
    average_time_Algorithm_B_ms = (timer_result * 1000) / iterations

    print(f"A Execution time = {average_time_Algorithm_A_ms} miliseconds")
    print(f"B Execution time = {average_time_Algorithm_B_ms} miliseconds")
    
    if average_time_Algorithm_A_ms > average_time_Algorithm_B_ms:
        A_more_than_B = average_time_Algorithm_A_ms / average_time_Algorithm_B_ms
        print(f"A is faster than B by {round(A_more_than_B,6)} times")
    else: 
        B_more_than_A = average_time_Algorithm_B_ms / average_time_Algorithm_A_ms
        print(f"B is faster than A by {round(B_more_than_A,6)} times")        

# Be clever and time multiple algorithms in the same function, but that would require you to be A. Clever and B. Bothered

if __name__ == "__main__":
    print("I am a library for timing Algorithms, don't run me")
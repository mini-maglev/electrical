import matplotlib.pyplot as plt
import numpy as np

def generate_pwm_sine(filename, pwm_frequency, sine_amplitude, sine_frequency, duration, timestep):
    """
    Generate a PWM sine wave for LTspice.

    Parameters:
        filename (str): The name of the output file to save the data.
        pwm_frequency (float): The frequency of the PWM signal in Hz.
        sine_amplitude (float): The amplitude of the sine wave.
        sine_frequency (float): The frequency of the sine wave in Hz.
        duration (float): The duration of the signal in seconds.
        timestep (float): The time step for sampling in seconds.

    Output:
        A text file containing two columns: time and value.
    """
    # Time vector
    t = np.arange(0, duration, timestep)

    # Generate sine wave
    sine_wave = np.sin(2 * np.pi * sine_frequency * t)

    # Generate PWM signal
    pwm_signal = []
    pwm_period = 1 / pwm_frequency

    for i in range(len(t)):
        # Time within the PWM cycle
        time_in_pwm_cycle = t[i] % pwm_period

        # Threshold for the sine wave
        threshold = sine_wave[i]

        # Duty cycle calculation
        if time_in_pwm_cycle < (threshold + 1) / 2 * pwm_period:
            pwm_signal.append(sine_amplitude)  # High state
        else:
            pwm_signal.append(0)  # Low state

    # Write the time and value pairs to a file
    with open(filename, 'w') as file:
        for time, value in zip(t, pwm_signal):
            file.write(f"{time:.6e}\t{value}\n")


    # Plot the sine wave and PWM signal
    plt.figure(figsize=(12, 6))

    # Plot sine wave
    plt.plot(t, (sine_wave + 1)/2, label="Sine Wave", linewidth=2)

    # Plot PWM signal
    plt.step(t, np.array(pwm_signal)/sine_amplitude, label="PWM Signal", where="post", linewidth=1, alpha=0.7)

    # Configure plot
    plt.title("PWM Representation of Sine Wave", fontsize=16)
    plt.xlabel("Time (s)", fontsize=14)
    plt.ylabel("Amplitude", fontsize=14)
    plt.legend(fontsize=12)
    plt.grid(True)
    plt.tight_layout()

    # Show the plot
    plt.show()


generate_pwm_sine(
    filename="pwm_sine_wave.txt",
    pwm_frequency=10000,
    sine_amplitude=24.0,
    sine_frequency=100,
    duration=0.1,
    timestep=1e-6
)

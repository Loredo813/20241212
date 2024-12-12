import matplotlib.pyplot as plt

def plot_rtt_results(normal_rtt_results, title="RTT Over Time"):
    if not normal_rtt_results:
        print("No RTT data available to plot.")
        return

    # Extract timestamps and RTTs
    timestamps = [entry[0] for entry in normal_rtt_results]
    rtts = [entry[1] for entry in normal_rtt_results]

    # Plot RTT over time
    plt.figure(figsize=(12, 6))
    plt.plot(timestamps, rtts, marker='o', linestyle='-', alpha=0.7, label="RTT")

    # Configure plot
    plt.title(title, fontsize=16)
    plt.xlabel("Timestamp (s)", fontsize=12)
    plt.ylabel("RTT (ms)", fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend(fontsize=10)
    plt.tight_layout()

    # Show plot
    plt.show()

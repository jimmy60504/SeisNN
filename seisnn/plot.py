import os
import matplotlib.pyplot as plt


def plot_trace(trace, enlarge=False, xlim=None, save_dir=None):
    start_time = trace.stats.starttime
    time_stamp = start_time.isoformat()

    if trace.picks:
        first_pick_time = trace.picks[0].time - start_time
        pick_phase = trace.picks[0].phase_hint
    else:
        first_pick_time = 1
        pick_phase = ""

    subplot = 2
    fig = plt.figure(figsize=(8, subplot * 2))

    ax = fig.add_subplot(subplot, 1, 1)
    plt.title(time_stamp + " " + trace.id)
    if xlim:
        plt.xlim(xlim)
    if enlarge:
        plt.xlim((first_pick_time - 1, first_pick_time + 2))
    ax.plot(trace.times(reftime=start_time), trace.data, "k-", label=trace.id)
    y_min, y_max = ax.get_ylim()
    if pick_phase:
        ax.vlines(first_pick_time, y_min, y_max, color='r', lw=2, label=pick_phase)
    if trace.picks:
        for pick in trace.picks[1:]:
            pick_time = pick.time - start_time
            ax.vlines(pick_time, y_min, y_max, color='r', lw=1)
    ax.legend()

    ax = fig.add_subplot(subplot, 1, subplot)
    ax.plot(trace.times(reftime=start_time), trace.pdf, "b-", label=pick_phase + " pdf")
    if xlim:
        plt.xlim(xlim)
    if enlarge:
        plt.xlim((first_pick_time - 1, first_pick_time + 2))
    ax.legend()

    if save_dir:
        os.makedirs(save_dir, exist_ok=True)
        plt.savefig(save_dir + "/" + time_stamp + "_" + trace.id + ".pdf")
        plt.close()
    else:
        plt.show()